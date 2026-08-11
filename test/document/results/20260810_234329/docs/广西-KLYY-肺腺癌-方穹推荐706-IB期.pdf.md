# 基准结果：广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf

## 基本信息

- 文件：`广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf`
- 大小：27147.7 KB
- PDF 总页数：26
- doc_id：`5146dde294d411f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE  progress=1.0
- 开始时间：2026-08-10T23:58:23  完成时间：2026-08-11T00:13:58  耗时：935.6s
- progress_msg：`16:13:48 Indexing done (0.15s). Task done (867.54s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 685d4901 | 9 | 1-9 | 病史 主诉：咳嗽、咳痰1月余 现病史：患者及家属共诉1月余前无明显诱因下出现阵发 |
| 2 | a94ca7d1 | 1 | 10-10 | 影像检查报告单 病人 ID: 姓名: 性别: 男 年龄: 67岁 申请科室: 老 |
| 3 | a97cf9bf | 2 | 11-12 | 科 检查部位：全身骨显像 显像剂：99mTc-MDP 临床诊断：1.肺占位性病变 |
| 4 | f9bb2f9d | 1 | 12-12 | 影像检查报告单 病人ID: 姓名: 性别: 男 年龄: 67岁 申请科室: 机器 |
| 5 | 88d90a7f | 1 | 13-13 | 广西医科大学第一附属医院 影像检查报告单 病人ID: 姓名: 男 年龄: 67岁 |
| 6 | 145bbdeb | 1 | 14-14 | 测量参数值: 测量项目 结果 单位 参考范围 测量项目 结果 单位 参考范围 主 |
| 7 | 65a17235 | 1 | 26-26 | 病理诊断报告书 1/1 标本条码 1223023095 医院 广西医科大学第一附 |
| 8 | e0f87a7e | 1 | 23-23 | <table><tr><td>吸氧浓度</td><td>FI02</td><td |
| 9 | 64cd07e5 | 1 | 15-15 | <table><tr><td>结核杆菌DNA*</td><td>TB-DNA</ |
| 10 | e55d554f | 1 | 16-16 | <table><tr><td>乙型肝炎表面抗原*</td><td>None</t |
| 11 | c18c7879 | 1 | 17-17 | <table><tr><td>丙型肝炎抗体定量*</td><td>None</t |
| 12 | e94ddc75 | 1 | 19-19 | <table><tr><td>凝血酶原时间</td><td>None</td>< |
| 13 | a6985d50 | 1 | 20-20 | <table><tr><td>总胆红素*</td><td>TBIL</td><t |
| 14 | 263a9a80 | 1 | 24-24 | <table><tr><td>酸碱度 (PH)</td><td>PH</td>< |
| 15 | 1ee55c28 | 1 | 25-25 | <table><tr><td>KRAS</td><td>None</td><td |
| 16 | c5b6d91f | 1 | 21-21 | <table><tr><td>胆碱酯酶*</td><td>CHE</td><td |
| 17 | 5c1cac66 | 1 | 22-22 | <table><tr><td>白细胞计数*</td><td>WBC</td><t |
| 18 | 9d3115f4 | 1 | 18-18 | <table><tr><td>糖化血红蛋白HbA1c*</td><td>HbA1 |

- chunks 总数：18
- 各 chunk 页数合计（含跨页重复）：27
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]`
- 覆盖页数：26 / 26；缺失页：`[]`
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
| ExaminationReport | 检查报告 | 6 | 6 | 6 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 11 | 0 | 11 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"AdmissionRecord": 1, "ExaminationReport": 6, "LabReport": 11}`
- ChunkMerger：`{"found": true, "merged": 18, "sources": 9, "stats": {"Extractor:LabExam": 11, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 6, "Extractor:Progress": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 16:13:45,785 INFO     29 [ChunkMerger] Merged 18 chunks from 9 sources: {'Extractor:LabExam': 11, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Pres`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 15:58:29,485 INFO     29 handle_task begin for task {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 15:58:29,688 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 15:58:29,806 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 15:58:29,836 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:58:29,836 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 15:58:29,836 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 15:58:29,891 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 15:58:29,891 INFO     29 ============================================================
2026-08-10 15:58:29,891 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 15:58:29,891 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 15:58:29,891 INFO     29 ============================================================
2026-08-10 15:58:29,892 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 15:58:29,892 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 15:58:29,897 INFO     29 No torch found.
2026-08-10 15:58:33,435 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=26
2026-08-10 15:58:34,302 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5346931, prompt_len=764
2026-08-10 15:58:35,923 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 15:58:35,924 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 15:58:35,938 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5346931, prompt_len=401
2026-08-10 15:58:40,320 INFO     29 [qwen-vl-parser] text API response (len=686):
["病史", "主诉：咳嗽、咳痰1月余", "现病史：患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、", "呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。至当地医院体检发现肺部阴影，具体不详。2026-02-26至中", "山大学附属第一医院广西医院就诊，查胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm", "，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋", "巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。具体诊治不详。为进一步治疗，遂", "至我院门诊就诊，门诊拟“肺占位性病变”收治入院。自发病以来，患者精神、食欲、睡眠正常，大小便正", "常，体重无明显变化。", "既往史：平素健康状况：良好。", "既往病史：否认高血压、冠心病、糖尿病史。", "传染病史：否，否认肝炎、结核或其他传染病史。", "预防接种史：正规。", "过敏史：否认过敏史。", "外伤史：否认外伤史。", "手术史：2年前曾行尿道结石手术，具体不详。", "输血史：否认输血史。", "系统回顾：无特殊。", "个人史：出生地：广西壮族自治区南宁市青秀区", "地方病地区居住情况：无", "冶游史：否认冶游史", "职业与工作条件有无工业毒物、粉尘、放射性物质及接触史：无", "广西医科大学第一附属医院 孔令祈", "11:24", "2026-03-19", "姜晓红 (D450199...", "姜晓红 (D450199..."]
2026-08-10 15:58:40,323 INFO     29 [qwen-vl-parser] page=1 text: 27 lines (bbox 0-26)
2026-08-10 15:58:40,324 INFO     29 [qwen-vl-parser] page=1 text: 27 sections
2026-08-10 15:58:40,841 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3061308, prompt_len=764
2026-08-10 15:58:42,289 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 15:58:42,290 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 15:58:42,311 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3061308, prompt_len=401
2026-08-10 15:58:44,303 INFO     29 [qwen-vl-parser] text API response (len=307):
["烟酒嗜好及药物使用史：有吸烟史，约10支/天，已吸烟40年，否认饮酒史。", "婚姻史：有婚姻史，结婚年龄：适龄结婚。有生育史，育有1子。", "家族史：否认相似家族病史及遗传病史。", "请患者或病史叙述者仔细确认以上病史记录并签字：[患者]", "体格检查", "一般情况：", "体温：36.8℃", "脉搏：75次/分", "呼吸：21次/分", "血压：138/72mmHg", "身高：161CM", "体重：74kg", "发育：正常", "营养：良好", "神志：清楚", "体位：自主体位", "面容：正常面容", "表情：自如", "步态：正常", "体型：正力型", "配合检查：合作"]
2026-08-10 15:58:44,304 INFO     29 [qwen-vl-parser] page=2 text: 21 lines (bbox 27-47)
2026-08-10 15:58:44,304 INFO     29 [qwen-vl-parser] page=2 text: 21 sections
2026-08-10 15:58:44,836 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3743105, prompt_len=764
2026-08-10 15:58:46,343 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 15:58:46,344 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 15:58:46,365 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3743105, prompt_len=401
2026-08-10 15:58:48,993 INFO     29 [qwen-vl-parser] text API response (len=423):
["皮肤黏膜:", "色", "泽:正常", "皮", "疹:全身皮肤未见皮疹", "皮下出血:全身皮肤未见皮下出血", "毛发分布:毛发分布正常", "温度与湿度:温度、湿度、弹性均正常", "水", "肿:未见水肿", "肝", "掌:无", "蜘", "蛛", "痣:未见蜘蛛痣", "其他表现:无", "淋巴结:全身浅表淋巴结未扪及肿大", "头部:", "头颅:头颅大小正常,无畸形", "眼:眉毛,眼睑,结膜,眼球未见异常,双侧巩膜无黄染", "耳:双耳外观未见异常,乳突无压痛,外耳道未见分泌物", "鼻:鼻部外观未见异常,鼻翼无扇动,鼻腔无分泌物,鼻窦区无压痛", "咽喉:双侧扁桃体未见肿大,表面未见脓性分泌物,咽未见异常,声音正常", "口腔:唇,舌,牙齿,牙龈正常", "颈部:", "颈部运动:颈软无抵抗", "颈静脉:无怒张", "气管:居中", "颈动脉搏动:正常", "肝-颈静脉回流征:阴性", "广西医科大:"]
2026-08-10 15:58:48,995 INFO     29 [qwen-vl-parser] page=3 text: 31 lines (bbox 48-78)
2026-08-10 15:58:48,995 INFO     29 [qwen-vl-parser] page=3 text: 31 sections
2026-08-10 15:58:49,574 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3863999, prompt_len=764
2026-08-10 15:58:51,108 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 15:58:51,110 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 15:58:51,139 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3863999, prompt_len=401
2026-08-10 15:58:56,380 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:58:56.377+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:59:28,201 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:59:28.198+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:00:00,082 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:00:00.081+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:00:31,913 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:00:31.912+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:01:00,701 INFO     29 [qwen-vl-parser] text API response (len=18171):
["预览 验证CA签名 手工解锁 删除 病历参考 更新数据 加载全部病程 个人模板管理 返回", "20部：", "003470 20.2.11", "003470 20.2.11", "003470 20.2.11", "003470 20.2.11", "胸部：胸廓对称无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常", "肺部：", "视诊：双侧呼吸运动均匀对称，无增强或者减弱", "触诊：双肺触觉语颤对称无异常，未触及胸膜摩擦感", "叩诊：双肺叩诊呈清音", "听诊：双肺呼吸音清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音", "心脏：", "视诊：心尖搏动未见异常，位于左侧第五肋间锁骨中线内0.5cm，无异常隆起及凹陷", "触诊：心尖搏动未触及异常，未触及震颤及心包摩擦感", "叩诊：心界不大", "听诊：心率：75次/分，心律：齐 A2 > P2", "心音 S1：有力， 心音 S2：有力， 心音 S3：无， 心音 S4：无", "杂音：各瓣膜区未闻及杂音", "额外心音：无", "心包摩擦音：无", "周围血管：未见异常血管征", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41
2026-08-10 16:01:00,706 INFO     29 [qwen-vl-parser] page=4 text: 864 lines (bbox 79-942)
2026-08-10 16:01:00,707 INFO     29 [qwen-vl-parser] page=4 text: 864 sections
2026-08-10 16:01:01,277 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3635836, prompt_len=764
2026-08-10 16:01:02,791 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 16:01:02,794 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 16:01:02,819 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3635836, prompt_len=401
2026-08-10 16:01:03,727 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:01:03.725+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:01:05,904 INFO     29 [qwen-vl-parser] text API response (len=506):
["编辑", "功能", "表格", "签名", "其他", "打印", "预览", "验证CA签名", "手工解锁", "删除", "病历参考", "更新数据", "加载全部病程", "个人模板管理", "返回", "腹部:", "视诊: 外形: 腹部外形正常", "腹围: 未测", "脐部: 正常", "胃形: 未见", "肠形: 未见", "蠕动波: 未见", "腹式呼吸: 正常", "腹壁静脉曲张: 无", "腹壁其它情况: 无", "触诊: 全腹柔软", "压痛反跳痛: 无压痛及反跳痛", "波动感: 无", "振水声: 无", "腹部包块: 腹部未触及包块", "肝脏: 肝脏肋下未触及", "胆囊: 未触及, Murphy征阴性", "脾脏: 脾脏肋下未触及", "肾脏: 未触及", "输尿管压痛点: 无压痛", "叩诊: 肝浊音界: 正常,", "肝上界位于锁骨中线, 第五肋间", "移动性浊音: 阴性,", "肾区叩痛: 无", "听诊: 肠鸣音无明显增强或减弱, 未闻及血管杂音", "肛门直肠: 未查", "生殖器: 未查", "脊柱四肢:", "脊柱外形: 脊柱正常生理弯曲"]
2026-08-10 16:01:05,906 INFO     29 [qwen-vl-parser] page=5 text: 44 lines (bbox 943-986)
2026-08-10 16:01:05,907 INFO     29 [qwen-vl-parser] page=5 text: 44 sections
2026-08-10 16:01:08,317 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3572570, prompt_len=764
2026-08-10 16:01:09,779 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 16:01:09,782 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-10 16:01:09,801 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3572570, prompt_len=401
2026-08-10 16:01:13,825 INFO     29 [qwen-vl-parser] text API response (len=606):
["70 四 肢：四肢无畸形，未见杵状指（趾），未见静脉曲张，双下肢无凹陷性水肿", "003470 20.2.41.64", "关 节：各关节未见异常，活动无受限", "肌 肉：未见肌肉萎缩，肌张力正常。四肢肌力5级。", "神经系统：", "浅反射：双侧浅反射正常引出", "深反射：双侧深反射正常引出", "病理反射：未引出", "脑膜刺激征：阴性", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "专科情况", "神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下肢无凹陷性水肿。", "实验室及器械检查结果", "(2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm", "，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋巴结彩超", "：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 16:01:13,827 INFO     29 [qwen-vl-parser] page=6 text: 25 lines (bbox 987-1011)
2026-08-10 16:01:13,827 INFO     29 [qwen-vl-parser] page=6 text: 25 sections
2026-08-10 16:01:14,597 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4796920, prompt_len=764
2026-08-10 16:01:16,397 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 16:01:16,397 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-10 16:01:16,413 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4796920, prompt_len=401
2026-08-10 16:01:22,493 INFO     29 [qwen-vl-parser] text API response (len=964):
["2026-02-28 18:30", "男，因“咳嗽、咳痰1月余”于2026-02-28 15:23入非急诊步行入科。", "病例特点如下：1、老年期男性，起病缓，病程短。2、患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，", "伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。3、既往史：平素", "健康状况：良好。既往病史：否认高血压、冠心病、糖尿病史。传染病史：否，否认肝炎、结核或其他传染病史。预", "防接种史：正规。过敏史：否认过敏史。外伤史：否认外伤史。手术史：2年前曾行尿道结石手术，具体不详。输血", "史：否认输血史。系统回顾：无特殊。否认新冠肺炎流行病接触史。4、查体：T：36.8℃，P：75次/分，R：21次/分", "，BP：138/72mmHg。神志清楚，正常面容，皮肤巩膜无黄染，全身浅表淋巴结未扪及肿大，颈静脉无怒张。胸廓对称", "无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常，双肺叩诊呈清音，双肺呼吸音", "清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音。心界不大，心率75次/分，心律齐，各瓣膜区未闻及杂音。腹", "部外形正常，全腹柔软，无压痛及反跳痛，腹部未触及包块，肝脏肋下未触及，脾脏肋下未触及。移动性浊音阴性。", "双下肢无凹陷性水肿。浅反射：双侧浅反射正常引出。深反射：双侧深反射正常引出。病理反射：未引出。脑膜刺激", "征：阴性5、专科情况：神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下", "肢无凹陷性水肿。6、辅助检查：（2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组", "织肿块，最大截断面约77mm*60mm，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧", "胸膜肥厚、钙化。浅表淋巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。", "初步诊断：1.肺部阴影", "2.细菌性肺炎", "诊断依据：1.老年男性，起步缓，病程短", "2.咳嗽，咳淡黄色粘液痰", "3.外院胸部CT提示右肺下叶后基底段软组织肿块", "鉴别诊断。", "1.肺结核球"]
2026-08-10 16:01:22,493 INFO     29 [qwen-vl-parser] page=7 text: 23 lines (bbox 1012-1034)
2026-08-10 16:01:22,493 INFO     29 [qwen-vl-parser] page=7 text: 23 sections
2026-08-10 16:01:23,291 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4914358, prompt_len=764
2026-08-10 16:01:24,763 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 16:01:24,764 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-10 16:01:24,780 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4914358, prompt_len=401
2026-08-10 16:01:29,783 INFO     29 [qwen-vl-parser] text API response (len=905):
["编辑", "功能", "表格", "签名", "其他", "打印", "预览", "验证CA签名", "手工解锁", "删除", "病历参考", "更新数据", "加载全部病程", "个人模板管理", "返回", "鉴别诊断：", "1.肺结核球：多见于年轻患者，病灶多见于结核好发部位，如肺上叶尖后段和下叶背段，直径一般<3", "cm。一般无症状，病灶边界清楚，密度高，可有包膜。有时含钙化点，周围有卫星灶。", "2.急性粟粒性肺结核：应与弥漫型细支气管肺泡癌相鉴别。通常粟粒型肺结核患者年龄较轻，有发热", "，盗汗等全身中毒症状，呼吸道症状不明显。x线表现为细小、分布均匀、密度较淡的粟粒样结节病灶。", "而细支气管—肺泡细胞癌两肺多有大小不等的结节状播散病灶，边界清楚、密度较高，进行性发展和增大", "，且有进行性呼吸困难。", "3.肺炎：若无毒性症状，抗生素治疗后肺部阴影吸收缓慢，或同一部位反复发生肺炎时，应考虑到肺", "癌可能。肺部慢性炎症机化，形成团块状的炎性假瘤，也易与肺癌相混淆。但炎性假瘤往往形态不整，边", "缘不齐，核心密度较高，易伴有胸膜增厚，病灶长期无明显变化。", "4.肺脓肿：起病急，中毒症状严重，多有寒战、高热、咳嗽、咳大量脓臭痰等症状。肺部x线表现为", "均匀的大片状炎性阴影，空洞内常见较深液平。结合纤支镜检查和痰脱落细胞检查可以鉴别。", "5.纵隔淋巴瘤：颇似中央型肺癌，常为双侧性，可有发热等全身症状，需病理诊断。", "VTE血栓风险评估：创建时间:2026-02-28 15:37:11,评估节点:入院,量表名称:Padua评分,分数:0,评分描述:低危,", "预防措施:undefined", "VTE出血风险评估：创建时间:2026-02-28 18:35:54,评估节点:入院,量表名称:内科出血风险评估,分数:1,评分描述：", "低危,预防措施:undefined", "诊疗计划：1.内科护理常规,II级护理。", "2.完善必要辅助检查如血肿瘤标志物、痰液化验、胸部增强CT、支气管镜检查或浅表淋巴结及肺穿刺活检", ""]
2026-08-10 16:01:29,784 INFO     29 [qwen-vl-parser] page=8 text: 34 lines (bbox 1035-1068)
2026-08-10 16:01:29,784 INFO     29 [qwen-vl-parser] page=8 text: 34 sections
2026-08-10 16:01:30,443 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5287322, prompt_len=764
2026-08-10 16:01:31,944 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 16:01:31,944 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-10 16:01:31,968 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5287322, prompt_len=401
2026-08-10 16:01:35,517 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:01:35.516+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:02:07,328 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:02:07.326+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:02:39,138 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:02:39.136+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:03:10,989 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:03:10.986+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:03:41,453 INFO     29 [qwen-vl-parser] text API response (len=18144):
["以确诊，必要时行颅脑MRI、腹部超声、骨扫描或PET-CT等检查以利进一步疾病诊治。", "3.给予吸氧、抗感染及止血、镇痛等对症支持治疗；明确病理类型拟定下一步治疗方案。", "是否需手术治疗：否", "医师签名：", "住院医师：", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003
2026-08-10 16:03:41,458 INFO     29 [qwen-vl-parser] page=9 text: 864 lines (bbox 1069-1932)
2026-08-10 16:03:41,458 INFO     29 [qwen-vl-parser] page=9 text: 864 sections
2026-08-10 16:03:41,962 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3019472, prompt_len=764
2026-08-10 16:03:42,832 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:03:42.832+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:03:43,535 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-03-16"}
```
2026-08-10 16:03:43,536 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=2026-03-16
2026-08-10 16:03:43,561 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3019472, prompt_len=401
2026-08-10 16:03:48,526 INFO     29 [qwen-vl-parser] text API response (len=551):
["影像检查报告单", "病人 ID:", "姓名:", "性别: 男", "年龄: 67岁", "申请科室: 老年医学呼吸内科", "机器型号: SE-MR4", "住院号", "检查部位: 颅脑颅脑MR平扫及增强+DWI,*钆特酸葡胺注射液【广西HR】", "检查日期: 2026-03-13", "(此报告仅供临床医师诊断参考,不作为疾病证明)", "检查所见:", "左侧基底节区、两侧放射冠、右侧侧脑室前后角旁见小斑片状、斑点状等T1、稍", "长T2信号灶,FLAIR呈高信号,边界欠清,DWI未见弥散受限;余脑实质信号未见异", "常,DWI未见明确弥散受限区,增强扫描未见异常强化灶;静脉窦强化充盈良好,未", "见异常;各脑室及脑沟、裂、池对称性轻度增宽;中线结构无移位。", "诊断意见:", "脑白质病变--改良Fasekas1级;轻度脑萎缩。", "检查技师: 唐成", "报告医师: 郭仟", "审核医师: 张", "报告日期: 2026-03-16 15:13:19", "审核日期: 2026-03-16 18:28:39", "地址: 广西医科大学第一附属医院放射科", "联系电话: 0771-5356934", "“广西HR”解释: 广西影像检查项目互认", ""]
2026-08-10 16:03:48,526 INFO     29 [qwen-vl-parser] page=10 text: 26 lines (bbox 1933-1958)
2026-08-10 16:03:48,526 INFO     29 [qwen-vl-parser] page=10 text: 26 sections
2026-08-10 16:03:49,167 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3431852, prompt_len=764
2026-08-10 16:03:50,757 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-03-10"}
```
2026-08-10 16:03:50,758 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=2026-03-10
2026-08-10 16:03:50,777 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3431852, prompt_len=401
2026-08-10 16:03:52,846 INFO     29 [qwen-vl-parser] text API response (len=292):
["科", "检查部位：全身骨显像 显像剂：99mTc-MDP 临床诊断：1.肺占位性病变,2.细菌性肺炎,3.肺", "剂量：25mCi 部阴影", "（此报告仅供临床医师诊断参考，不作为疾病证明）", "检查所见：", "静脉注射99mTc-MDP 3小时后行全身骨显像前位、后位各1帧：", "全身骨像完整、显影基本清晰。颅骨、胸骨、椎体、肩胛骨、肋骨、骨盆及四肢骨显像剂分", "布未见明显异常改变。", "双肾显影，膀胱部分充盈。", "诊断意见：", "全身骨显像未见明显异常改变。", "报告医师：巫殷豪", "审核医师：彭盛梅", "报告日期：2026-03-10"]
2026-08-10 16:03:52,847 INFO     29 [qwen-vl-parser] page=11 text: 14 lines (bbox 1959-1972)
2026-08-10 16:03:52,847 INFO     29 [qwen-vl-parser] page=11 text: 14 sections
2026-08-10 16:03:53,593 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4396640, prompt_len=764
2026-08-10 16:03:55,174 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-03-11"}
```
2026-08-10 16:03:55,177 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=2026-03-11
2026-08-10 16:03:55,199 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4396640, prompt_len=401
2026-08-10 16:03:59,618 INFO     29 [qwen-vl-parser] text API response (len=768):
["广西医科大学第一附属医院", "影像检查报告单", "病人ID:", "姓名:", "性别: 男", "年龄: 67岁", "申请科室:", "机器型号: SE-", "床号: 49床", "住院号: 1959", "Force-2", "检查部位: 下腹部,上腹部CT平扫+增强,(新)碘帕醇注射液", "【广西HR】", "检查日期: 2026-03-11", "(此报告仅供临床医师诊断参考,不作为疾病证明)", "检查所见:", "双侧肾上腺见多个结节状稍低/低密度影,较大者大小约1.6cm×1.2cm,增强扫", "描不均匀强化。肝脏各叶比例正常,肝实质内见多发类圆形低密度无强化灶,较大者", "位于S8,大小约1.2cm×1.1cm;余肝实质未见异常密度影及异常强化灶。肝内、外胆", "管未见扩张,胆囊不大,囊壁均匀,囊内密度未见异常。脾脏、胰腺形态、大小、密", "度未见异常,增强扫描未见异常强化,右肾体积缩小,双肾实质内见多个类圆形低密", "度无强化灶,较大者大小约0.9cm×1.5cm;双侧肾盂肾盏及输尿管未见扩张。腹部肠", "管分布正常,管腔未见扩张、积液,腹腔内未见明确肿块影;肝门及腹主动脉旁未见", "增大淋巴结,腹膜腔未见积液。", "诊断意见:", "1.双侧肾上腺占位,考虑转移瘤可能性大,请结合临床;", "2.肝多发囊肿;", "3.右肾萎缩,双肾囊肿。", "检查技师:刘辰民", "报告医师:谢金桓", "审核医师: 冯涛", "报告日期:2026-03-11 14:21:30", "审核日期:2026-03-11 16:15:45", "地址:广西医科大学第一附属医院放射科", "联系电话:0771-5356934", "“广西HR”解释:广西影像检查项目互认", ""]
2026-08-10 16:03:59,621 INFO     29 [qwen-vl-parser] page=12 text: 36 lines (bbox 1973-2008)
2026-08-10 16:03:59,622 INFO     29 [qwen-vl-parser] page=12 text: 36 sections
2026-08-10 16:04:00,269 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3306564, prompt_len=764
2026-08-10 16:04:01,742 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-03-02"}
```
2026-08-10 16:04:01,743 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=2026-03-02
2026-08-10 16:04:01,757 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3306564, prompt_len=401
2026-08-10 16:04:06,838 INFO     29 [qwen-vl-parser] text API response (len=876):
["广西医科大学第一附属医院", "影像检查报告单", "病人ID:", "姓名:", "男", "年龄: 67岁", "申请科室: 老年医学呼吸内科", "机器型号: SE-", "Force-2", "床号", "号", "检查部位: 胸部CT平扫+增强,*碘海醇注射液【广西HR】", "检查日期: 2026-03-02", "(此报告仅供临床医师诊断参考,不作为疾病证明)", "检查所见:", "两肺尖胸膜下见类圆形透亮影,较大者长径约0.8cm;右肺下叶基底段(Se4:IM144)见团", "块状密度增高灶,大小约为7.7cm×5.1cm×6.9cm,增强扫描中度强化;两肺可见多发实性结节", "影,较大位于右肺下叶外基底段(Se4:IM344),内可见空泡,长径约为1.1cm,增强扫描似见", "血管穿行。右肺中叶、左肺上叶下舌段及两肺下叶见条索状密度增高影;余肺叶内未见异常密", "度影及异常强化灶,右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张,两肺部分支气管", "管壁增厚,管腔变窄,气管、其余支气管通畅;肺门、纵隔结构清楚,纵隔、两侧肺门见多发", "淋巴结,大者短径约1.1cm。两侧胸膜增厚、钙化,胸膜腔未见积液。主动脉、冠状动脉见斑片", "状钙化灶。", "诊断意见:", "1.右肺下叶后基底段软组织肿块,肿瘤性病变?感染性病变?请结合临床及实验室检查;", "2.两肺多发实性结节,建议短期复查;", "3.右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张并两肺炎症;", "4.两肺上叶间隔旁型肺气肿;", "5.纵隔、两侧肺门淋巴结,建议复查;", "6.两侧胸膜肥厚、钙化;", "7.主动脉、冠状动脉硬化。", "检查技师:周春燚 报告医师:肖芳艳 审核医师:", "报告日期:2026-03-03 18:39:05 审核日期:2026-03-04 09:21:01", "地址:广西医科大学第一附属医院放射科 联系电话:0771-5356934 “广西HR”解码:广西影像检查项目互认", ""]
2026-08-10 16:04:06,839 INFO     29 [qwen-vl-parser] page=13 text: 34 lines (bbox 2009-2042)
2026-08-10 16:04:06,839 INFO     29 [qwen-vl-parser] page=13 text: 34 sections
2026-08-10 16:04:07,390 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5122646, prompt_len=764
2026-08-10 16:04:09,034 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-03-02"
}
```
2026-08-10 16:04:09,035 INFO     29 [qwen-vl-parser] page=14 classify=text report_date=2026-03-02
2026-08-10 16:04:09,057 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5122646, prompt_len=401
2026-08-10 16:04:13,738 INFO     29 [qwen-vl-parser] text API response (len=866):
["测量参数值:", "测量项目", "结果", "单位", "参考范围", "测量项目", "结果", "单位", "参考范围", "主动脉根部内径:", "27", "mm", "(20-35)", "左房前后径:", "35", "mm", "(24-39)", "左室舒末前后径:", "53", "mm", "(38-54)", "左室缩末前后径:", "32", "mm", "(24-37)", "室间隔舒末厚:", "10", "mm", "(6-11)", "左室后壁舒末厚:", "10", "mm", "(6-11)", "右室舒末前后径:", "18", "mm", "(15-30)", "右室流出道:", "27", "mm", "(15-32)", "主肺动脉内径:", "22", "mm", "(15-26)", "E/A", "<1", "(", "0.8-2.0)", "e'/a'", "<1", "(-)", "E/e'", "11.7", "(-)", "超声描述:", "描述:", "1、按比例各房室大小正常，房、室间隔连续完整，室间隔与左室壁厚度正常，静息状态下室壁收", "缩运动有力，未见节段性运动异常。左室收缩功能测定在正常范围，FS:40%，EF:70%，SV:95ml/B", "，CO:6.4L/min，EDV:135ml，心包腔内未探及液性区声像。", "2、三尖瓣形态结构正常，瓣口轻度反流，速度2.4m/s，压差22mmHg，瞬时反流量约2ml（无血流动", "力学意义），余各瓣膜形态结构正常，启闭运动好，二尖瓣血流图示E峰小于A峰。", "3、主动脉根部内径正常，升主动脉内径正常，管壁增厚，弹性降低，主肺动脉内径正常，内回声", "及血流信号未见异常。", "超声诊断:", "1、心脏形态结构及瓣膜功能大致正常。", "2、左室舒张功能降低，收缩功能测定在正常范围，", "诊断医师：吴颖/肖彩意", "报告日期：2026-03-02 10:12:46"]
2026-08-10 16:04:13,739 INFO     29 [qwen-vl-parser] page=14 text: 69 lines (bbox 2043-2111)
2026-08-10 16:04:13,739 INFO     29 [qwen-vl-parser] page=14 text: 69 sections
2026-08-10 16:04:14,301 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2321993, prompt_len=764
2026-08-10 16:04:14,613 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:04:14.611+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:04:15,749 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2026-02-28"}
```
2026-08-10 16:04:15,750 INFO     29 [qwen-vl-parser] page=15 classify=table report_date=2026-02-28
2026-08-10 16:04:15,770 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2321993, prompt_len=756
2026-08-10 16:04:17,810 INFO     29 [qwen-vl-parser] table API response (len=191):
\begin{tabular}{ccccccccc}
\hline
缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\
\hline
TB-DNA & 结核杆菌DNA* & $<$5.00E+02 & & & & 拷贝 & $<$5.00E+02 & $<$5.00E+02 \\
\hline
\end{tabular}
2026-08-10 16:04:17,815 INFO     29 [qwen-vl-parser] page=15 table: 8 LaTeX lines (bbox 2112-2119)
2026-08-10 16:04:17,815 INFO     29 [qwen-vl-parser] page=15 table: 8 sections
2026-08-10 16:04:19,453 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3750809, prompt_len=764
2026-08-10 16:04:21,024 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2026-02-28"}
```
2026-08-10 16:04:21,024 INFO     29 [qwen-vl-parser] page=16 classify=table report_date=2026-02-28
2026-08-10 16:04:21,035 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3750809, prompt_len=756
2026-08-10 16:04:23,184 INFO     29 [qwen-vl-parser] table API response (len=348):
\begin{tabular}{ccccccccc}
\hline
项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\
\hline
乙型肝炎表面抗原* & 0.00 & & & & IU/ml & 0-0.08 & \\
乙型肝炎表面抗体* & 14.85 & & $\uparrow$ & & mIU/mL & 0-10 & \\
乙型肝炎e抗原* & 0.00 & & & & PElu/ml & 0-0.10 & \\
乙型肝炎e抗体* & 0.14 & & & & IU/mL & 0-0.20 & \\
乙型肝炎核心抗体* & 0.27 & & & & IU/mL & 0-0.50 & \\
\hline
\end{tabular}
2026-08-10 16:04:23,184 INFO     29 [qwen-vl-parser] page=16 table: 12 LaTeX lines (bbox 2120-2131)
2026-08-10 16:04:23,185 INFO     29 [qwen-vl-parser] page=16 table: 12 sections
2026-08-10 16:04:23,833 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3532896, prompt_len=764
2026-08-10 16:04:25,309 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2026-02-28"}
```
2026-08-10 16:04:25,310 INFO     29 [qwen-vl-parser] page=17 classify=table report_date=2026-02-28
2026-08-10 16:04:25,327 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3532896, prompt_len=756
2026-08-10 16:04:27,167 INFO     29 [qwen-vl-parser] table API response (len=307):
\begin{tabular}{llcccllcc}
\hline
& & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\
\hline
& / & 丙型肝炎抗体定量* & 0.06 & & & & COI & 0-1 & \\
& ST & 不加热血清反应素试验* & 阴性(-) & & & & & 阴性(-) & \\
& V & 人免疫缺陷病毒抗体定量* & 0.08 & & & & COI & 0-1 & \\
& PA & 梅毒螺旋体抗体定量* & 0.08 & & & & COI & 0-1 & \\
\hline
\end{tabular}
2026-08-10 16:04:27,169 INFO     29 [qwen-vl-parser] page=17 table: 11 LaTeX lines (bbox 2132-2142)
2026-08-10 16:04:27,169 INFO     29 [qwen-vl-parser] page=17 table: 11 sections
2026-08-10 16:04:27,745 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3260841, prompt_len=764
2026-08-10 16:04:29,192 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2026-02-28"}
```
2026-08-10 16:04:29,192 INFO     29 [qwen-vl-parser] page=18 classify=table report_date=2026-02-28
2026-08-10 16:04:29,204 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3260841, prompt_len=756
2026-08-10 16:04:32,210 INFO     29 [qwen-vl-parser] table API response (len=260):
\begin{tabular}{ccccccccc}
\hline
项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\
\hline
糖化血红蛋白HbA1c* & 6.40 & & $\uparrow$ & & \% & 4.0-6.0 & \\
糖化血红蛋白HbA1a & 0.50 & & & & \% & 0-0.91 & \\
糖化血红蛋白HbA1b & 1.10 & & & & \% & 0.35-1.82 & \\
\hline
\end{tabular}
2026-08-10 16:04:32,213 INFO     29 [qwen-vl-parser] page=18 table: 10 LaTeX lines (bbox 2143-2152)
2026-08-10 16:04:32,213 INFO     29 [qwen-vl-parser] page=18 table: 10 sections
2026-08-10 16:04:32,743 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3468749, prompt_len=764
2026-08-10 16:04:34,386 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2026-02-28"}
```
2026-08-10 16:04:34,387 INFO     29 [qwen-vl-parser] page=19 classify=table report_date=2026-02-28
2026-08-10 16:04:34,404 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3468749, prompt_len=756
2026-08-10 16:04:36,953 INFO     29 [qwen-vl-parser] table API response (len=409):
\begin{tabular}{l c c c c c c c}
\hline
项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历 \\
\hline
凝血酶原时间* & 11.50 & & & & S & 9-15 & \\
国际标准化比值* & 1.04 & & & & & 0.8-1.4 & \\
纤维蛋白原* & 4.43 & & & & g/L & 2.00 -5.00 & \\
活化部分凝血活酶时间* & 32.30 & & & & S & 23.00 -40.00 & \\
凝血酶时间* & 13.00 & & & & S & 10.3-16.6 & \\
凝血酶原活动度 & 98 & & & & \% & 70-130 & \\
D-二聚体定量* & 69 & & & & ng/ml & 0-450 & \\
\hline
\end{tabular}
2026-08-10 16:04:36,956 INFO     29 [qwen-vl-parser] page=19 table: 14 LaTeX lines (bbox 2153-2166)
2026-08-10 16:04:36,956 INFO     29 [qwen-vl-parser] page=19 table: 14 sections
2026-08-10 16:04:37,678 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3985539, prompt_len=764
2026-08-10 16:04:39,354 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2026-02-02"}
```
2026-08-10 16:04:39,354 INFO     29 [qwen-vl-parser] page=20 classify=table report_date=2026-02-02
2026-08-10 16:04:39,367 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3985539, prompt_len=756
2026-08-10 16:04:44,947 INFO     29 [qwen-vl-parser] table API response (len=1170):
\begin{tabular}{ccccccccc}
\hline
缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & \\
\hline
TBIL & 总胆红素* & 8.7 & & & & \textmu mol/L & 0-26.0 & \\
DBIL & 直接胆红素* & 3.6 & & & & \textmu mol/L & 0-6.8 & \\
IBIL & 间接胆红素 & 5.1 & & & & \textmu mol/L & 3.1-14.3 & \\
DB/TB & 直/总胆比值 & 0.41 & & & & & & \\
TP & 总蛋白\# & 74.5 & & & & g/L & 65-85 & \\
ALB & 白蛋白* & 39.3 & & \downarrow & & g/L & 40-55 & \\
GLO & 球蛋白 & 35.2 & & & & g/L & 20-40 & \\
A/G & 白蛋白/球蛋白 & 1.1 & & \downarrow & & & 1.2-2.4 & \\
GGT & 谷氨酰转肽酶* & 30 & & & & U/L & 10-60 & \\
TBA & 总胆汁酸* & 13.2 & & \uparrow & & \textmu mol/L & 0-10 & \\
AST & 天门冬氨酸氨基转移酶* & 15 & & & & U/L & 15-40 & \\
ALT & 丙氨酸氨基转移酶* & 14 & & & & U/L & 9-50 & \\
AST/ALT & 谷草/谷丙比值 & 1.1 & & & & & & \\
ALP & 碱性磷酸酶* & 64 & & & & U/L & 45-125 & \\
PA & 前白蛋白* & 251.5 & & & & mg/L & 200-430 & \\
CHE & 胆碱酯酶* & 8382 & & & & U/L & 5000-12000 & \\
UREA & 尿素* & 6.98 & & & & mmol/L & 3.6-9.5 & \\
CREA & 肌酐* & 136 & & \uparrow & & \textmu mol/L & 57-111 & \\
UA & 尿酸* & 551 & & \uparrow & & \textmu mol/L & 208-428 & \\
HCO3 & 碳酸氢根* & 21.6 & & \downarrow & & mmol/L & 22-29 & \\
T-CHO & 总胆固醇* & 3.10 & & & & mmol/L & 3.1-5.7 & \\
\hline
\end{tabular}
2026-08-10 16:04:44,948 INFO     29 [qwen-vl-parser] page=20 table: 28 LaTeX lines (bbox 2167-2194)
2026-08-10 16:04:44,948 INFO     29 [qwen-vl-parser] page=20 table: 28 sections
2026-08-10 16:04:45,623 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4020865, prompt_len=764
2026-08-10 16:04:46,406 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:04:46.403+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:04:47,312 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2025-04-01"}
```
2026-08-10 16:04:47,313 INFO     29 [qwen-vl-parser] page=21 classify=table report_date=2025-04-01
2026-08-10 16:04:47,335 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4020865, prompt_len=756
2026-08-10 16:04:54,836 INFO     29 [qwen-vl-parser] table API response (len=1138):
\begin{tabular}{ccccccccc}
\hline
缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & \\
\hline
CHE & 胆碱酯酶* & 8382 & & & & U/L & 5000-12000 & \\
UREA & 尿素* & 6.98 & & & & mmol/L & 3.6-9.5 & \\
CREA & 肌酐* & 136 & & $\uparrow$ & & $\mu$mol/L & 57-111 & \\
UA & 尿酸* & 551 & & $\uparrow$ & & $\mu$mol/L & 208-428 & \\
HCO3 & 碳酸氢根* & 21.6 & & $\downarrow$ & & mmol/L & 22-29 & \\
T-CHO & 总胆固醇* & 3.18 & & & & mmol/L & $<$5.2 & \\
TG & 甘油三酯* & 1.27 & & & & mmol/L & $<$1.7 & \\
LDL-C & 低密度脂蛋白胆固醇* & 1.78 & & & & mmol/L & $<$3.4(低危人群) & \\
GLU & 空腹血葡萄糖* & 4.79 & & & & mmol/L & 3.9-6.1 & \\
K & 钾* & 4.18 & & & & mmol/L & 3.5-5.3 & \\
Na & 钠* & 141.1 & & & & mmol/L & 137-147 & \\
CL & 氯* & 106.4 & & & & mmol/L & 99-110 & \\
Ca & 总钙* & 2.25 & & & & mmol/L & 2.11-2.52 & \\
Mg & 镁* & 0.78 & & & & mmol/L & 0.75-1.02 & \\
P & 磷* & 0.95 & & & & mmol/L & 0.85-1.51 & \\
CK & 肌酸激酶* & 84 & & & & U/L & 50-310 & \\
CK-MB & 肌酸激酶同工酶MB & 13 & & & & U/L & 0-25 & \\
LD & 乳酸脱氢酶* & 167 & & & & U/L & 120-250 & \\
$\alpha$-HBD & $\alpha$-羟丁酸脱氢酶* & 109 & & & & U/L & 72-182 & \\
IgE & 免疫球蛋白E* & 1960.6 & & $\uparrow$ & & IU/ml & $<$100 & \\
\hline
\end{tabular}
2026-08-10 16:04:54,838 INFO     29 [qwen-vl-parser] page=21 table: 27 LaTeX lines (bbox 2195-2221)
2026-08-10 16:04:54,838 INFO     29 [qwen-vl-parser] page=21 table: 27 sections
2026-08-10 16:04:55,502 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4026758, prompt_len=764
2026-08-10 16:04:57,076 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-10 16:04:57,078 INFO     29 [qwen-vl-parser] page=22 classify=table report_date=None
2026-08-10 16:04:57,098 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4026758, prompt_len=756
2026-08-10 16:05:03,147 INFO     29 [qwen-vl-parser] table API response (len=1136):
\begin{tabular}{ccccccccc}
\hline
缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 \\
\hline
WBC & 白细胞计数* & 8.490 & & & & 10~9/L & 3.5-9.5 \\
RBC & 红细胞计数* & 5.81 & & $\uparrow$ & & 10~12/L & 4.3-5.8 \\
HGB & 血红蛋白* & 157.00 & & & & g/L & 130-175 \\
PLT & 血小板计数* & 268.00 & & & & 10~9/L & 125-350 \\
NEU\% & 中性粒细胞百分比 & 0.6920 & & & & & 0.4-0.75 \\
LYM\% & 淋巴细胞百分比 & 0.1970 & & $\downarrow$ & & & 0.2-0.5 \\
MONO\% & 单核细胞百分比 & 0.0630 & & & & & 0.03-0.1 \\
EO\% & 嗜酸性粒细胞百分比 & 0.0450 & & & & & 0.004-0.08 \\
BA SO\% & 嗜碱性粒细胞百分比 & 0.0030 & & & & & 0-0.01 \\
NEU & 中性粒细胞绝对值 & 5.88 & & & & 10~9/L & 1.8-6.3 \\
LYM & 淋巴细胞绝对值 & 1.67 & & & & 10~9/L & 1.1-3.2 \\
MONO & 单核细胞绝对值 & 0.53 & & & & 10~9/L & 0.1-0.6 \\
EOS & 嗜酸性粒细胞绝对值 & 0.38 & & & & 10~9/L & 0.02-0.52 \\
BA SO & 嗜碱性粒细胞绝对值 & 0.03 & & & & 10~9/L & 0-0.06 \\
MCV & 平均红细胞体积* & 83.70 & & & & fl & 82-100 \\
MCH & 平均RBC血红蛋白含量* & 26.90 & & $\downarrow$ & & pg & 27-34 \\
MCHC & 平均RBC血红蛋白浓度* & 323.00 & & & & g/L & 316-354 \\
HCT & 红细胞比容* & 0.486 & & & & & 0.4-0.5 \\
RDWCV & RBC体积分布宽度CV & 0.15 & & $\uparrow$ & & & 0.11-0.14 \\
PDW & 血小板体积分布宽度 & 0.16 & & & & & 0.15-0.18 \\
\hline
\end{tabular}
2026-08-10 16:05:03,149 INFO     29 [qwen-vl-parser] page=22 table: 26 LaTeX lines (bbox 2222-2247)
2026-08-10 16:05:03,149 INFO     29 [qwen-vl-parser] page=22 table: 26 sections
2026-08-10 16:05:03,804 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4115824, prompt_len=764
2026-08-10 16:05:05,344 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-10 16:05:05,345 INFO     29 [qwen-vl-parser] page=23 classify=table report_date=None
2026-08-10 16:05:05,360 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4115824, prompt_len=756
2026-08-10 16:05:11,668 INFO     29 [qwen-vl-parser] table API response (len=1366):
\begin{tabular}{ccccccccc}
\hline
\multicolumn{1}{c}{\textbf{缩写}} & \multicolumn{1}{c}{\textbf{项目名称}} & \multicolumn{1}{c}{\textbf{结果}} & \multicolumn{1}{c}{\textbf{结果提示}} & \multicolumn{1}{c}{\textbf{异常提示}} & \multicolumn{1}{c}{\textbf{辅助诊断}} & \multicolumn{1}{c}{\textbf{单位}} & \multicolumn{1}{c}{\textbf{参考范围}} \\
\hline
FI02 & 吸氧浓度 & 21.00 & & & & \% & 21-100 \\
T & 体温 & 36.4 & & & & & 29-41 \\
Ca++ & 钙测定 & 1.19 & & & & mmol/L & 1.15-1.29 \\
Na+ & 钠测定 & 143.20 & & & & mmol/L & 136-146 \\
K+ & 钾测定 & 3.98 & & & & mmol/L & 3.5-4.5 \\
p02(a,T)/F02 & 氧合指数(p/f) & 315.0 & & $\downarrow$ & & & 400-500 \\
BEecf & 红细胞外剩余碱 & -1.80 & & & & mmol/l & -3-3 \\
PH & 酸碱度 (PH) & 7.383 & & & & & 7.35-7.45 \\
pH(T) & pH校正值(pHT) & 7.392 & & & & & 7.35-7.45 \\
pO2 & 氧分压 (pO2) & 66.20 & & $\downarrow$ & & mmHg & 83-108 \\
pO2(T) & 氧分压校正值 & 63.50 & & $\downarrow$ & & mmHg & 83-108 \\
pCO2 & 二氧化碳分压 & 39.90 & & & & mmHg & 35-45 \\
PCO2(T) & CO2分压校正 & 38.90 & & & & mmHg & 35-45 \\
Cl- & 氯测定 & 102.00 & & & & mmol/L & 98-106 \\
Hb & 血红蛋白测定(Hb) & 162.00 & & $\uparrow$ & & g/L & 120-160 \\
F02Hb & 氧合血红蛋白 & 92.0 & & $\downarrow$ & & \% & 94-98 \\
MetHb & 高铁血红蛋白 & 0.10 & & & & & \\
s02 & 总血氧饱和度 & 92.9 & & $\downarrow$ & & \% & 93-98 \\
COHb & CO红蛋白 & 1.00 & & & & \% & 0-2 \\
ctCO2 & 血CO2含量 & 24.50 & & & & mmol/L & 24-32 \\
FHHB & 还原血红蛋白 & 6.9 & & & & & \\
\hline
\end{tabular}
2026-08-10 16:05:11,670 INFO     29 [qwen-vl-parser] page=23 table: 27 LaTeX lines (bbox 2248-2274)
2026-08-10 16:05:11,670 INFO     29 [qwen-vl-parser] page=23 table: 27 sections
2026-08-10 16:05:12,349 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4168304, prompt_len=764
2026-08-10 16:05:13,984 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-10 16:05:13,985 INFO     29 [qwen-vl-parser] page=24 classify=table report_date=None
2026-08-10 16:05:14,000 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4168304, prompt_len=756
2026-08-10 16:05:18,305 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:05:18.303+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:05:20,030 INFO     29 [qwen-vl-parser] table API response (len=1157):
\begin{tabular}{ccccccccc}
\hline
缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 \\
\hline
PH & 酸碱度 (PH) & 7.383 & & & & & 7.35-7.45 \\
pH(T) & pH校正值(pHT) & 7.392 & & & & & 7.35-7.45 \\
pO2 & 氧分压 (pO2) & 66.20 & & $\downarrow$ & & mmHg & 83-108 \\
pO2(T) & 氧分压校正值 & 63.50 & & $\downarrow$ & & mmHg & 83-108 \\
pCO2 & 二氧化碳分压 & 39.90 & & & & mmHg & 35-45 \\
PCO2(T) & CO2分压校正 & 38.90 & & & & mmHg & 35-45 \\
Cl- & 氯测定 & 102.00 & & & & mmol/L & 98-106 \\
Hb & 血红蛋白测定(Hb) & 162.00 & & $\uparrow$ & & g/L & 120-160 \\
F02Hb & 氧合血红蛋白 & 92.0 & & $\downarrow$ & & \% & 94-98 \\
MetHb & 高铁血红蛋白 & 0.10 & & & & & \\
s02 & 总血氧饱和度 & 92.9 & & $\downarrow$ & & \% & 93-98 \\
C0Hb & CO红蛋白 & 1.00 & & & & \% & 0-2 \\
ctCO2 & 血CO2含量 & 24.50 & & & & mmol/L & 24-32 \\
FHHB & 还原血红蛋白 & 6.9 & & & & \% & 2-7 \\
cHCO3 & 标准碳酸氢根 & 23.00 & & & & mmol/L & 22-26 \\
ABE (BE(B)) & 实际剩余碱 & -1.6 & & & & mmol/L & -3-3 \\
HCO3- & 实际碳酸氢根 & 23.20 & & & & mmol/L & \\
P02(A-a,T)e & 肺泡动脉氧分压差 & 36.0 & & $\uparrow$ & & mmHg & 10-25 \\
P02(a/A,T) & 动脉与肺泡氧分压比 & 64.0 & & $\downarrow$ & & \% & 85-95 \\
RI & 呼吸指数 & 57.0 & & & & & \\
Glu & 葡萄糖测定 & 6.70 & & $\uparrow$ & & & \\
\hline
\end{tabular}
2026-08-10 16:05:20,034 INFO     29 [qwen-vl-parser] page=24 table: 27 LaTeX lines (bbox 2275-2301)
2026-08-10 16:05:20,034 INFO     29 [qwen-vl-parser] page=24 table: 27 sections
2026-08-10 16:05:20,195 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1101847, prompt_len=764
2026-08-10 16:05:23,443 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-03-16"
}
```
2026-08-10 16:05:23,443 INFO     29 [qwen-vl-parser] page=25 classify=text report_date=2026-03-16
2026-08-10 16:05:23,463 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1101847, prompt_len=401
2026-08-10 16:05:28,987 INFO     29 [qwen-vl-parser] text API response (len=1198):
["临床诊断：肺癌", "样本采集时间：2026-03-10", "检测项目", "本产品对与肺癌密切相关的68个基因进行高通量测序。检测突变形式为点突变(SNV)、小片段插入缺失(INDEL)、拷贝数变异(CNV)以及融合(FUSION)。通过免疫组化检测PD-L1表达。", "本报告分析基因变异与靶向药物、化疗药物的相关性，给出靶向药物(FDA/NMPA批准药物、临床试验", "药物等)、化疗药物的用药提示信息，从而为临床制定治疗方案提供参考信息。", "注：检测基因列表见附录。", "检测结果小结", "检测类型", "检测结果", "靶向用药指导", "共检出3个变异位点,其中3个与靶向药物相关(KRAS", "p.G12V; CDKN2A p.R80*; TP53 p.G279E)", "PD-L1蛋白表达水平", "使用CSTE1L3N抗体; TPS:<1%, CPS:1", "化疗药物检测", "详见“化疗药物检测解析”部分", "样品总体质量评估", "合格", "注:", "1. 本报告为基因检测结果,基因、药物等信息列举未按照重要性排序。", "2. 本报告只对本次采集样本负责,如有疑问,请在7个工作日内与我们联系。", "检测人:", "张紫叶", "复核人:", "王建丽", "日期:", "2026-03-16", "日期:", "2026-03-16", "1/26", "孔令祈 Novogene", "诺禾致源", "肺癌精准诊疗相关基因结果汇总", "基因", "变异类型", "检测结果", "变异丰度/拷贝数", "ALK", "突变/融合", "未检测到与用药相关突变", "-", "BRAF", "突变/融合", "未检测到与用药相关突变", "-", "BRCA1", "突变/缺失", "未检测到与用药相关突变", "-", "BRCA2", "突变/缺失", "未检测到与用药相关突变", "-", "EGFR", "突变", "未检测到与用药相关突变", "-", "ERBB2(HER2)", "突变/扩增", "未检测到与用药相关突变", "-", "FGFR2", "突变/融合", "未检测到与用药相关突变", "-", "FGFR3", "突变/融合", "未检测到与用药相关突变", "-", "KIT", "突变", "未检测到与用药相关突变", "-", "KRAS", "突变", "NM_033360.4 exon2 c.35G>T p.G12V", "35.80%", "MET", "突变/扩增/14号外", "未检测到与用药相关突变", "-", "显子跳跃", "NRG1", "融合", "未检测到与用药相关突变", "-", "NTRK1", "融合", "未检测到与用药相关突变", "-"]
2026-08-10 16:05:28,988 INFO     29 [qwen-vl-parser] page=25 text: 79 lines (bbox 2302-2380)
2026-08-10 16:05:28,988 INFO     29 [qwen-vl-parser] page=25 text: 79 sections
2026-08-10 16:05:29,173 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1246411, prompt_len=764
2026-08-10 16:05:30,662 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-03-10"
}
```
2026-08-10 16:05:30,663 INFO     29 [qwen-vl-parser] page=26 classify=text report_date=2026-03-10
2026-08-10 16:05:30,680 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1246411, prompt_len=401
2026-08-10 16:05:34,985 INFO     29 [qwen-vl-parser] text API response (len=888):
["广西金域医学检验实验室", "本报告单经过电子签名认证", "Guangxi Kingmed Center for Clinical Laboratory", "金域医学", "KingMed Diagnostics", "病理诊断报告书", "1/1", "标本条码", "1223023095", "医院", "广西医科大学第一附属医院", "病人姓名", "孔令祈", "科室", "老年呼吸", "病理号", "26018339", "性别", "男", "房/床号", "49", "住院门诊号", "1959880", "年龄", "67岁", "接收时间", "2026-03-08 14:15:50", "申请医生", "", "项目名称", "免疫组化8项", "送检材料", "肺组织", "临床诊断", "", "患者电话", "", "大体描述:", "福尔马林固定标本，核对送检标本、病人姓名和条形码与申请单一致。", "灰红条索状组织3段，长0.5-1.8cm，直径均0.05cm。取1盒全（共1盒蜡块）", "镜下所见：", "诊断意见：", "肺组织穿刺活检：", "-结合免疫组化，符合浸润性黏液型腺癌，请结合临床。", "-免疫组化：CK7（+），CK20（+），Villin（+），TTF-1（散在+），NapsinA（散在+），P40（-），CDX2（-），Ki67（", "热点区约60%+）。", "报告医师：陈明坚", "本检测仅对送检负责，如果对结果有疑义，请在报告发布后7天内与我们联系，多谢合作！", "收样点：广西医科大学第一附属医院-呼吸内", "科", "主检实验室：广西金域", "地址：南宁市西乡塘区总部路3号中国-东盟科技企业孵化基地二期1号厂房一、三、", "四层", "报告专用章", "网址：www.kingmed.com.cn", "GX003SCEJL7RJLY", "报告日期：2026-03-10 21:16:16", "更多报告服务", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 16:05:34,985 INFO     29 [qwen-vl-parser] page=26 text: 57 lines (bbox 2381-2437)
2026-08-10 16:05:34,985 INFO     29 [qwen-vl-parser] page=26 text: 57 sections
2026-08-10 16:05:34,985 INFO     29 [qwen-vl-parser] parse_pdf done: 2438 sections from 26 pages.
2026-08-10 16:05:34,998 INFO     29 Close text detector.
2026-08-10 16:05:35,609 INFO     29 Close text recognizer.
2026-08-10 16:05:36,058 INFO     29 Close recognizer.
2026-08-10 16:05:36,434 INFO     29 Close recognizer.
2026-08-10 16:05:36,882 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 16:05:36,882 INFO     29 [Trace] task=5212989c | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Parser:MedLink | outputs={"html": "", "json": "2438 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "json"}
2026-08-10 16:05:36,882 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 16:05:36,914 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:05:36,918 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 病史\n[BBOX-1] 主诉：咳嗽、咳痰1月余\n[BBOX-2] 现病史：患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、\n[BBOX-3] 呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。至当地医院体检发现肺部阴影，具体不详。2026-02-26至中\n[BBOX-4] 山大学附属第一医院广西医院就诊，查胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm\n[BBOX-5] ，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋\n[BBOX-6] 巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。具体诊治不详。为进一步治疗，遂\n[BBOX-7] 至我院门诊就诊，门诊拟“肺占位性病变”收治入院。自发病以来，患者精神、食欲、睡眠正常，大小便正\n[BBOX-8] 常，体重无明显变化。\n[BBOX-9] 既往史：平素健康状况：良好。\n[BBOX-10] 既往病史：否认高血压、冠心病、糖尿病史。\n[BBOX-11] 传染病史：否，否认肝炎、结核或其他传染病史。\n[BBOX-12] 预防接种史：正规。\n[BBOX-13] 过敏史：否认过敏史。\n[BBOX-14] 外伤史：否认外伤史。\n[BBOX-15] 手术史：2年前曾行尿道结石手术，具体不详。\n[BBOX-16] 输血史：否认输血史。\n[BBOX-17] 系统回顾：无特殊。\n[BBOX-18] 个人史：出生地：广西壮族自治区南宁市青秀区\n[BBOX-19] 地方病地区居住情况：无\n[BBOX-20] 冶游史：否认冶游史\n[BBOX-21] 职业与工作条件有无工业毒物、粉尘、放射性物质及接触史：无\n[BBOX-22] 广西医科大学第一附属医院 孔令祈\n[BBOX-23] 11:24\n[BBOX-24] 2026-03-19\n[BBOX-25] 姜晓红 (D450199...\n[BBOX-26] 姜晓红 (D450199...\n[BBOX-27] 烟酒嗜好及药物使用史：有吸烟史，约10支/天，已吸烟40年，否认饮酒史。\n[BBOX-28] 婚姻史：有婚姻史，结婚年龄：适龄结婚。有生育史，育有1子。\n[BBOX-29] 家族史：否认相似家族病史及遗传病史。\n[BBOX-30] 请患者或病史叙述者仔细确认以上病史记录并签字：[患者]\n[BBOX-31] 体格检查\n[BBOX-32] 一般情况：\n[BBOX-33] 体温：36.8℃\n[BBOX-34] 脉搏：75次/分\n[BBOX-35] 呼吸：21次/分\n[BBOX-36] 血压：138/72mmHg\n[BBOX-37] 身高：161CM\n[BBOX-38] 体重：74kg\n[BBOX-39] 发育：正常\n[BBOX-40] 营养：良好\n[BBOX-41] 神志：清楚\n[BBOX-42] 体位：自主体位\n[BBOX-43] 面容：正常面容\n[BBOX-44] 表情：自如\n[BBOX-45] 步态：正常\n[BBOX-46] 体型：正力型\n[BBOX-47] 配合检查：合作\n[BBOX-48] 皮肤黏膜:\n[BBOX-49] 色\n[BBOX-50] 泽:正常\n[BBOX-51] 皮\n[BBOX-52] 疹:全身皮肤未见皮疹\n[BBOX-53] 皮下出血:全身皮肤未见皮下出血\n[BBOX-54] 毛发分布:毛发分布正常\n[BBOX-55] 温度与湿度:温度、湿度、弹性均正常\n[BBOX-56] 水\n[BBOX-57] 肿:未见水肿\n[BBOX-58] 肝\n[BBOX-59] 掌:无\n[BBOX-60] 蜘\n[BBOX-61] 蛛\n[BBOX-62] 痣:未见蜘蛛痣\n[BBOX-63] 其他表现:无\n[BBOX-64] 淋巴结:全身浅表淋巴结未扪及肿大\n[BBOX-65] 头部:\n[BBOX-66] 头颅:头颅大小正常,无畸形\n[BBOX-67] 眼:眉毛,眼睑,结膜,眼球未见异常,双侧巩膜无黄染\n[BBOX-68] 耳:双耳外观未见异常,乳突无压痛,外耳道未见分泌物\n[BBOX-69] 鼻:鼻部外观未见异常,鼻翼无扇动,鼻腔无分泌物,鼻窦区无压痛\n[BBOX-70] 咽喉:双侧扁桃体未见肿大,表面未见脓性分泌物,咽未见异常,声音正常\n[BBOX-71] 口腔:唇,舌,牙齿,牙龈正常\n[BBOX-72] 颈部:\n[BBOX-73] 颈部运动:颈软无抵抗\n[BBOX-74] 颈静脉:无怒张\n[BBOX-75] 气管:居中\n[BBOX-76] 颈动脉搏动:正常\n[BBOX-77] 肝-颈静脉回流征:阴性\n[BBOX-78] 广西医科大:\n[BBOX-79] 预览 验证CA签名 手工解锁 删除 病历参考 更新数据 加载全部病程 个人模板管理 返回\n[BBOX-80] 20部：\n[BBOX-81] 003470 20.2.11\n[BBOX-82] 003470 20.2.11\n[BBOX-83] 003470 20.2.11\n[BBOX-84] 003470 20.2.11\n[BBOX-85] 胸部：胸廓对称无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常\n[BBOX-86] 肺部：\n[BBOX-87] 视诊：双侧呼吸运动均匀对称，无增强或者减弱\n[BBOX-88] 触诊：双肺触觉语颤对称无异常，未触及胸膜摩擦感\n[BBOX-89] 叩诊：双肺叩诊呈清音\n[BBOX-90] 听诊：双肺呼吸音清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音\n[BBOX-91] 心脏：\n[BBOX-92] 视诊：心尖搏动未见异常，位于左侧第五肋间锁骨中线内0.5cm，无异常隆起及凹陷\n[BBOX-93] 触诊：心尖搏动未触及异常，未触及震颤及心包摩擦感\n[BBOX-94] 叩诊：心界不大\n[BBOX-95] 听诊：心率：75次/分，心律：齐 A2 > P2\n[BBOX-96] 心音 S1：有力， 心音 S2：有力， 心音 S3：无， 心音 S4：无\n[BBOX-97] 杂音：各瓣膜区未闻及杂音\n[BBOX-98] 额外心音：无\n[BBOX-99] 心包摩擦音：无\n[BBOX-100] 周围血管：未见异常血管征\n[BBOX-101] 003470 20.2.41.64\n[BBOX-102] 003470 20.2.41.64\n[BBOX-103] 003470 20.2.41.64\n[BBOX-104] 003470 20.2.41.64\n[BBOX-105] 003470 20.2.41.64\n[BBOX-106] 003470 20.2.41.64\n[BBOX-107] 003470 20.2.41.64\n[BBOX-108] 003470 20.2.41.64\n[BBOX-109] 003470 20.2.41.64\n[BBOX-110] 003470 20.2.41.64\n[BBOX-111] 003470 20.2.41.64\n[BBOX-112] 003470 20.2.41.64\n[BBOX-113] 003470 20.2.41.64\n[BBOX-114] 003470 20.2.41.64\n[BBOX-115] 003470 20.2.41.64\n[BBOX-116] 003470 20.2.41.64\n[BBOX-117] 003470 20.2.41.64\n[BBOX-118] 003470 20.2.41.64\n[BBOX-119] 003470 20.2.41.64\n[BBOX-120] 003470 20.2.41.64\n[BBOX-121] 003470 20.2.41.64\n[BBOX-122] 003470 20.2.41.64\n[BBOX-123] 003470 20.2.41.64\n[BBOX-124] 003470 20.2.41.64\n[BBOX-125] 003470 20.2.41.64\n[BBOX-126] 003470 20.2.41.64\n[BBOX-127] 003470 20.2.41.64\n[BBOX-128] 003470 20.2.41.64\n[BBOX-129] 003470 20.2.41.64\n[BBOX-130] 003470 20.2.41.64\n[BBOX-131] 003470 20.2.41.64\n[BBOX-132] 003470 20.2.41.64\n[BBOX-133] 003470 20.2.41.64\n[BBOX-134] 003470 20.2.41.64\n[BBOX-135] 003470 20.2.41.64\n[BBOX-136] 003470 20.2.41.64\n[BBOX-137] 003470 20.2.41.64\n[BBOX-138] 003470 20.2.41.64\n[BBOX-139] 003470 20.2.41.64\n[BBOX-140] 003470 20.2.41.64\n[BBOX-141] 003470 20.2.41.64\n[BBOX-142] 003470 20.2.41.64\n[BBOX-143] 003470 20.2.41.64\n[BBOX-144] 003470 20.2.41.64\n[BBOX-145] 003470 20.2.41.64\n[BBOX-146] 003470 20.2.41.64\n[BBOX-147] 003470 20.2.41.64\n[BBOX-148] 003470 20.2.41.64\n[BBOX-149] 003470 20.2.41.64\n[BBOX-150] 003470 20.2.41.64\n[BBOX-151] 003470 20.2.41.64\n[BBOX-152] 003470 20.2.41.64\n[BBOX-153] 003470 20.2.41.64\n[BBOX-154] 003470 20.2.41.64\n[BBOX-155] 003470 20.2.41.64\n[BBOX-156] 003470 20.2.41.64\n[BBOX-157] 003470 20.2.41.64\n[BBOX-158] 003470 20.2.41.64\n[BBOX-159] 003470 20.2.41.64\n[BBOX-160] 003470 20.2.41.64\n[BBOX-161] 003470 20.2.41.64\n[BBOX-162] 003470 20.2.41.64\n[BBOX-163] 003470 20.2.41.64\n[BBOX-164] 003470 20.2.41.64\n[BBOX-165] 003470 20.2.41.64\n[BBOX-166] 003470 20.2.41.64\n[BBOX-167] 003470 20.2.41.64\n[BBOX-168] 003470 20.2.41.64\n[BBOX-169] 003470 20.2.41.64\n[BBOX-170] 003470 20.2.41.64\n[BBOX-171] 003470 20.2.41.64\n[BBOX-172] 003470 20.2.41.64\n[BBOX-173] 003470 20.2.41.64\n[BBOX-174] 003470 20.2.41.64\n[BBOX-175] 003470 20.2.41.64\n[BBOX-176] 003470 20.2.41.64\n[BBOX-177] 003470 20.2.41.64\n[BBOX-178] 003470 20.2.41.64\n[BBOX-179] 003470 20.2.41.64\n[BBOX-180] 003470 20.2.41.64\n[BBOX-181] 003470 20.2.41.64\n[BBOX-182] 003470 20.2.41.64\n[BBOX-183] 003470 20.2.41.64\n[BBOX-184] 003470 20.2.41.64\n[BBOX-185] 003470 20.2.41.64\n[BBOX-186] 003470 20.2.41.64\n[BBOX-187] 003470 20.2.41.64\n[BBOX-188] 003470 20.2.41.64\n[BBOX-189] 003470 20.2.41.64\n[BBOX-190] 003470 20.2.41.64\n[BBOX-191] 003470 20.2.41.64\n[BBOX-192] 003470 20.2.41.64\n[BBOX-193] 003470 20.2.41.64\n[BBOX-194] 003470 20.2.41.64\n[BBOX-195] 003470 20.2.41.64\n[BBOX-196] 003470 20.2.41.64\n[BBOX-197] 003470 20.2.41.64\n[BBOX-198] 003470 20.2.41.64\n[BBOX-199] 003470 20.2.41.64\n[BBOX-200] 003470 20.2.41.64\n[BBOX-201] 003470 20.2.41.64\n[BBOX-202] 003470 20.2.41.64\n[BBOX-203] 003470 20.2.41.64\n[BBOX-204] 003470 20.2.41.64\n[BBOX-205] 003470 20.2.41.64\n[BBOX-206] 003470 20.2.41.64\n[BBOX-207] 003470 20.2.41.64\n[BBOX-208] 003470 20.2.41.64\n[BBOX-209] 003470 20.2.41.64\n[BBOX-210] 003470 20.2.41.64\n[BBOX-211] 003470 20.2.41.64\n[BBOX-212] 003470 20.2.41.64\n[BBOX-213] 003470 20.2.41.64\n[BBOX-214] 003470 20.2.41.64\n[BBOX-215] 003470 20.2.41.64\n[BBOX-216] 003470 20.2.41.64\n[BBOX-217] 003470 20.2.41.64\n[BBOX-218] 003470 20.2.41.64\n[BBOX-219] 003470 20.2.41.64\n[BBOX-220] 003470 20.2.41.64\n[BBOX-221] 003470 20.2.41.64\n[BBOX-222] 003470 20.2.41.64\n[BBOX-223] 003470 20.2.41.64\n[BBOX-224] 003470 20.2.41.64\n[BBOX-225] 003470 20.2.41.64\n[BBOX-226] 003470 20.2.41.64\n[BBOX-227] 003470 20.2.41.64\n[BBOX-228] 003470 20.2.41.64\n[BBOX-229] 003470 20.2.41.64\n[BBOX-230] 003470 20.2.41.64\n[BBOX-231] 003470 20.2.41.64\n[BBOX-232] 003470 20.2.41.64\n[BBOX-233] 003470 20.2.41.64\n[BBOX-234] 003470 20.2.41.64\n[BBOX-235] 003470 20.2.41.64\n[BBOX-236] 003470 20.2.41.64\n[BBOX-237] 003470 20.2.41.64\n[BBOX-238] 003470 20.2.41.64\n[BBOX-239] 003470 20.2.41.64\n[BBOX-240] 003470 20.2.41.64\n[BBOX-241] 003470 20.2.41.64\n[BBOX-242] 003470 20.2.41.64\n[BBOX-243] 003470 20.2.41.64\n[BBOX-244] 003470 20.2.41.64\n[BBOX-245] 003470 20.2.41.64\n[BBOX-246] 003470 20.2.41.64\n[BBOX-247] 003470 20.2.41.64\n[BBOX-248] 003470 20.2.41.64\n[BBOX-249] 003470 20.2.41.64\n[BBOX-250] 003470 20.2.41.64\n[BBOX-251] 003470 20.2.41.64\n[BBOX-252] 003470 20.2.41.64\n[BBOX-253] 003470 20.2.41.64\n[BBOX-254] 003470 20.2.41.64\n[BBOX-255] 003470 20.2.41.64\n[BBOX-256] 003470 20.2.41.64\n[BBOX-257] 003470 20.2.41.64\n[BBOX-258] 003470 20.2.41.64\n[BBOX-259] 003470 20.2.41.64\n[BBOX-260] 003470 20.2.41.64\n[BBOX-261] 003470 20.2.41.64\n[BBOX-262] 003470 20.2.41.64\n[BBOX-263] 003470 20.2.41.64\n[BBOX-264] 003470 20.2.41.64\n[BBOX-265] 003470 20.2.41.64\n[BBOX-266] 003470 20.2.41.64\n[BBOX-267] 003470 20.2.41.64\n[BBOX-268] 003470 20.2.41.64\n[BBOX-269] 003470 20.2.41.64\n[BBOX-270] 003470 20.2.41.64\n[BBOX-271] 003470 20.2.41.64\n[BBOX-272] 003470 20.2.41.64\n[BBOX-273] 003470 20.2.41.64\n[BBOX-274] 003470 20.2.41.64\n[BBOX-275] 003470 20.2.41.64\n[BBOX-276] 003470 20.2.41.64\n[BBOX-277] 003470 20.2.41.64\n[BBOX-278] 003470 20.2.41.64\n[BBOX-279] 003470 20.2.41.64\n[BBOX-280] 003470 20.2.41.64\n[BBOX-281] 003470 20.2.41.64\n[BBOX-282] 003470 20.2.41.64\n[BBOX-283] 003470 20.2.41.64\n[BBOX-284] 003470 20.2.41.64\n[BBOX-285] 003470 20.2.41.64\n[BBOX-286] 003470 20.2.41.64\n[BBOX-287] 003470 20.2.41.64\n[BBOX-288] 003470 20.2.41.64\n[BBOX-289] 003470 20.2.41.64\n[BBOX-290] 003470 20.2.41.64\n[BBOX-291] 003470 20.2.41.64\n[BBOX-292] 003470 20.2.41.64\n[BBOX-293] 003470 20.2.41.64\n[BBOX-294] 003470 20.2.41.64\n[BBOX-295] 003470 20.2.41.64\n[BBOX-296] 003470 20.2.41.64\n[BBOX-297] 003470 20.2.41.64\n[BBOX-298] 003470 20.2.41.64\n[BBOX-299] 003470 20.2.41.64\n[BBOX-300] 003470 20.2.41.64\n[BBOX-301] 003470 20.2.41.64\n[BBOX-302] 003470 20.2.41.64\n[BBOX-303] 003470 20.2.41.64\n[BBOX-304] 003470 20.2.41.64\n[BBOX-305] 003470 20.2.41.64\n[BBOX-306] 003470 20.2.41.64\n[BBOX-307] 003470 20.2.41.64\n[BBOX-308] 003470 20.2.41.64\n[BBOX-309] 003470 20.2.41.64\n[BBOX-310] 003470 20.2.41.64\n[BBOX-311] 003470 20.2.41.64\n[BBOX-312] 003470 20.2.41.64\n[BBOX-313] 003470 20.2.41.64\n[BBOX-314] 003470 20.2.41.64\n[BBOX-315] 003470 20.2.41.64\n[BBOX-316] 003470 20.2.41.64\n[BBOX-317] 003470 20.2.41.64\n[BBOX-318] 003470 20.2.41.64\n[BBOX-319] 003470 20.2.41.64\n[BBOX-320] 003470 20.2.41.64\n[BBOX-321] 003470 20.2.41.64\n[BBOX-322] 003470 20.2.41.64\n[BBOX-323] 003470 20.2.41.64\n[BBOX-324] 003470 20.2.41.64\n[BBOX-325] 003470 20.2.41.64\n[BBOX-326] 003470 20.2.41.64\n[BBOX-327] 003470 20.2.41.64\n[BBOX-328] 003470 20.2.41.64\n[BBOX-329] 003470 20.2.41.64\n[BBOX-330] 003470 20.2.41.64\n[BBOX-331] 003470 20.2.41.64\n[BBOX-332] 003470 20.2.41.64\n[BBOX-333] 003470 20.2.41.64\n[BBOX-334] 003470 20.2.41.64\n[BBOX-335] 003470 20.2.41.64\n[BBOX-336] 003470 20.2.41.64\n[BBOX-337] 003470 20.2.41.64\n[BBOX-338] 003470 20.2.41.64\n[BBOX-339] 003470 20.2.41.64\n[BBOX-340] 003470 20.2.41.64\n[BBOX-341] 003470 20.2.41.64\n[BBOX-342] 003470 20.2.41.64\n[BBOX-343] 003470 20.2.41.64\n[BBOX-344] 003470 20.2.41.64\n[BBOX-345] 003470 20.2.41.64\n[BBOX-346] 003470 20.2.41.64\n[BBOX-347] 003470 20.2.41.64\n[BBOX-348] 003470 20.2.41.64\n[BBOX-349] 003470 20.2.41.64\n[BBOX-350] 003470 20.2.41.64\n[BBOX-351] 003470 20.2.41.64\n[BBOX-352] 003470 20.2.41.64\n[BBOX-353] 003470 20.2.41.64\n[BBOX-354] 003470 20.2.41.64\n[BBOX-355] 003470 20.2.41.64\n[BBOX-356] 003470 20.2.41.64\n[BBOX-357] 003470 20.2.41.64\n[BBOX-358] 003470 20.2.41.64\n[BBOX-359] 003470 20.2.41.64\n[BBOX-360] 003470 20.2.41.64\n[BBOX-361] 003470 20.2.41.64\n[BBOX-362] 003470 20.2.41.64\n[BBOX-363] 003470 20.2.41.64\n[BBOX-364] 003470 20.2.41.64\n[BBOX-365] 003470 20.2.41.64\n[BBOX-366] 003470 20.2.41.64\n[BBOX-367] 003470 20.2.41.64\n[BBOX-368] 003470 20.2.41.64\n[BBOX-369] 003470 20.2.41.64\n[BBOX-370] 003470 20.2.41.64\n[BBOX-371] 003470 20.2.41.64\n[BBOX-372] 003470 20.2.41.64\n[BBOX-373] 003470 20.2.41.64\n[BBOX-374] 003470 20.2.41.64\n[BBOX-375] 003470 20.2.41.64\n[BBOX-376] 003470 20.2.41.64\n[BBOX-377] 003470 20.2.41.64\n[BBOX-378] 003470 20.2.41.64\n[BBOX-379] 003470 20.2.41.64\n[BBOX-380] 003470 20.2.41.64\n[BBOX-381] 003470 20.2.41.64\n[BBOX-382] 003470 20.2.41.64\n[BBOX-383] 003470 20.2.41.64\n[BBOX-384] 003470 20.2.41.64\n[BBOX-385] 003470 20.2.41.64\n[BBOX-386] 003470 20.2.41.64\n[BBOX-387] 003470 20.2.41.64\n[BBOX-388] 003470 20.2.41.64\n[BBOX-389] 003470 20.2.41.64\n[BBOX-390] 003470 20.2.41.64\n[BBOX-391] 003470 20.2.41.64\n[BBOX-392] 003470 20.2.41.64\n[BBOX-393] 003470 20.2.41.64\n[BBOX-394] 003470 20.2.41.64\n[BBOX-395] 003470 20.2.41.64\n[BBOX-396] 003470 20.2.41.64\n[BBOX-397] 003470 20.2.41.64\n[BBOX-398] 003470 20.2.41.64\n[BBOX-399] 003470 20.2.41.64\n[BBOX-400] 003470 20.2.41.64\n[BBOX-401] 003470 20.2.41.64\n[BBOX-402] 003470 20.2.41.64\n[BBOX-403] 003470 20.2.41.64\n[BBOX-404] 003470 20.2.41.64\n[BBOX-405] 003470 20.2.41.64\n[BBOX-406] 003470 20.2.41.64\n[BBOX-407] 003470 20.2.41.64\n[BBOX-408] 003470 20.2.41.64\n[BBOX-409] 003470 20.2.41.64\n[BBOX-410] 003470 20.2.41.64\n[BBOX-411] 003470 20.2.41.64\n[BBOX-412] 003470 20.2.41.64\n[BBOX-413] 003470 20.2.41.64\n[BBOX-414] 003470 20.2.41.64\n[BBOX-415] 003470 20.2.41.64\n[BBOX-416] 003470 20.2.41.64\n[BBOX-417] 003470 20.2.41.64\n[BBOX-418] 003470 20.2.41.64\n[BBOX-419] 003470 20.2.41.64\n[BBOX-420] 003470 20.2.41.64\n[BBOX-421] 003470 20.2.41.64\n[BBOX-422] 003470 20.2.41.64\n[BBOX-423] 003470 20.2.41.64\n[BBOX-424] 003470 20.2.41.64\n[BBOX-425] 003470 20.2.41.64\n[BBOX-426] 003470 20.2.41.64\n[BBOX-427] 003470 20.2.41.64\n[BBOX-428] 003470 20.2.41.64\n[BBOX-429] 003470 20.2.41.64\n[BBOX-430] 003470 20.2.41.64\n[BBOX-431] 003470 20.2.41.64\n[BBOX-432] 003470 20.2.41.64\n[BBOX-433] 003470 20.2.41.64\n[BBOX-434] 003470 20.2.41.64\n[BBOX-435] 003470 20.2.41.64\n[BBOX-436] 003470 20.2.41.64\n[BBOX-437] 003470 20.2.41.64\n[BBOX-438] 003470 20.2.41.64\n[BBOX-439] 003470 20.2.41.64\n[BBOX-440] 003470 20.2.41.64\n[BBOX-441] 003470 20.2.41.64\n[BBOX-442] 003470 20.2.41.64\n[BBOX-443] 003470 20.2.41.64\n[BBOX-444] 003470 20.2.41.64\n[BBOX-445] 003470 20.2.41.64\n[BBOX-446] 003470 20.2.41.64\n[BBOX-447] 003470 20.2.41.64\n[BBOX-448] 003470 20.2.41.64\n[BBOX-449] 003470 20.2.41.64\n[BBOX-450] 003470 20.2.41.64\n[BBOX-451] 003470 20.2.41.64\n[BBOX-452] 003470 20.2.41.64\n[BBOX-453] 003470 20.2.41.64\n[BBOX-454] 003470 20.2.41.64\n[BBOX-455] 003470 20.2.41.64\n[BBOX-456] 003470 20.2.41.64\n[BBOX-457] 003470 20.2.41.64\n[BBOX-458] 003470 20.2.41.64\n[BBOX-459] 003470 20.2.41.64\n[BBOX-460] 003470 20.2.41.64\n[BBOX-461] 003470 20.2.41.64\n[BBOX-462] 003470 20.2.41.64\n[BBOX-463] 003470 20.2.41.64\n[BBOX-464] 003470 20.2.41.64\n[BBOX-465] 003470 20.2.41.64\n[BBOX-466] 003470 20.2.41.64\n[BBOX-467] 003470 20.2.41.64\n[BBOX-468] 003470 20.2.41.64\n[BBOX-469] 003470 20.2.41.64\n[BBOX-470] 003470 20.2.41.64\n[BBOX-471] 003470 20.2.41.64\n[BBOX-472] 003470 20.2.41.64\n[BBOX-473] 003470 20.2.41.64\n[BBOX-474] 003470 20.2.41.64\n[BBOX-475] 003470 20.2.41.64\n[BBOX-476] 003470 20.2.41.64\n[BBOX-477] 003470 20.2.41.64\n[BBOX-478] 003470 20.2.41.64\n[BBOX-479] 003470 20.2.41.64\n[BBOX-480] 003470 20.2.41.64\n[BBOX-481] 003470 20.2.41.64\n[BBOX-482] 003470 20.2.41.64\n[BBOX-483] 003470 20.2.41.64\n[BBOX-484] 003470 20.2.41.64\n[BBOX-485] 003470 20.2.41.64\n[BBOX-486] 003470 20.2.41.64\n[BBOX-487] 003470 20.2.41.64\n[BBOX-488] 003470 20.2.41.64\n[BBOX-489] 003470 20.2.41.64\n[BBOX-490] 003470 20.2.41.64\n[BBOX-491] 003470 20.2.41.64\n[BBOX-492] 003470 20.2.41.64\n[BBOX-493] 003470 20.2.41.64\n[BBOX-494] 003470 20.2.41.64\n[BBOX-495] 003470 20.2.41.64\n[BBOX-496] 003470 20.2.41.64\n[BBOX-497] 003470 20.2.41.64\n[BBOX-498] 003470 20.2.41.64\n[BBOX-499] 003470 20.2.41.64\n[BBOX-500] 003470 20.2.41.64\n[BBOX-501] 003470 20.2.41.64\n[BBOX-502] 003470 20.2.41.64\n[BBOX-503] 003470 20.2.41.64\n[BBOX-504] 003470 20.2.41.64\n[BBOX-505] 003470 20.2.41.64\n[BBOX-506] 003470 20.2.41.64\n[BBOX-507] 003470 20.2.41.64\n[BBOX-508] 003470 20.2.41.64\n[BBOX-509] 003470 20.2.41.64\n[BBOX-510] 003470 20.2.41.64\n[BBOX-511] 003470 20.2.41.64\n[BBOX-512] 003470 20.2.41.64\n[BBOX-513] 003470 20.2.41.64\n[BBOX-514] 003470 20.2.41.64\n[BBOX-515] 003470 20.2.41.64\n[BBOX-516] 003470 20.2.41.64\n[BBOX-517] 003470 20.2.41.64\n[BBOX-518] 003470 20.2.41.64\n[BBOX-519] 003470 20.2.41.64\n[BBOX-520] 003470 20.2.41.64\n[BBOX-521] 003470 20.2.41.64\n[BBOX-522] 003470 20.2.41.64\n[BBOX-523] 003470 20.2.41.64\n[BBOX-524] 003470 20.2.41.64\n[BBOX-525] 003470 20.2.41.64\n[BBOX-526] 003470 20.2.41.64\n[BBOX-527] 003470 20.2.41.64\n[BBOX-528] 003470 20.2.41.64\n[BBOX-529] 003470 20.2.41.64\n[BBOX-530] 003470 20.2.41.64\n[BBOX-531] 003470 20.2.41.64\n[BBOX-532] 003470 20.2.41.64\n[BBOX-533] 003470 20.2.41.64\n[BBOX-534] 003470 20.2.41.64\n[BBOX-535] 003470 20.2.41.64\n[BBOX-536] 003470 20.2.41.64\n[BBOX-537] 003470 20.2.41.64\n[BBOX-538] 003470 20.2.41.64\n[BBOX-539] 003470 20.2.41.64\n[BBOX-540] 003470 20.2.41.64\n[BBOX-541] 003470 20.2.41.64\n[BBOX-542] 003470 20.2.41.64\n[BBOX-543] 003470 20.2.41.64\n[BBOX-544] 003470 20.2.41.64\n[BBOX-545] 003470 20.2.41.64\n[BBOX-546] 003470 20.2.41.64\n[BBOX-547] 003470 20.2.41.64\n[BBOX-548] 003470 20.2.41.64\n[BBOX-549] 003470 20.2.41.64\n[BBOX-550] 003470 20.2.41.64\n[BBOX-551] 003470 20.2.41.64\n[BBOX-552] 003470 20.2.41.64\n[BBOX-553] 003470 20.2.41.64\n[BBOX-554] 003470 20.2.41.64\n[BBOX-555] 003470 20.2.41.64\n[BBOX-556] 003470 20.2.41.64\n[BBOX-557] 003470 20.2.41.64\n[BBOX-558] 003470 20.2.41.64\n[BBOX-559] 003470 20.2.41.64\n[BBOX-560] 003470 20.2.41.64\n[BBOX-561] 003470 20.2.41.64\n[BBOX-562] 003470 20.2.41.64\n[BBOX-563] 003470 20.2.41.64\n[BBOX-564] 003470 20.2.41.64\n[BBOX-565] 003470 20.2.41.64\n[BBOX-566] 003470 20.2.41.64\n[BBOX-567] 003470 20.2.41.64\n[BBOX-568] 003470 20.2.41.64\n[BBOX-569] 003470 20.2.41.64\n[BBOX-570] 003470 20.2.41.64\n[BBOX-571] 003470 20.2.41.64\n[BBOX-572] 003470 20.2.41.64\n[BBOX-573] 003470 20.2.41.64\n[BBOX-574] 003470 20.2.41.64\n[BBOX-575] 003470 20.2.41.64\n[BBOX-576] 003470 20.2.41.64\n[BBOX-577] 003470 20.2.41.64\n[BBOX-578] 003470 20.2.41.64\n[BBOX-579] 003470 20.2.41.64\n[BBOX-580] 003470 20.2.41.64\n[BBOX-581] 003470 20.2.41.64\n[BBOX-582] 003470 20.2.41.64\n[BBOX-583] 003470 20.2.41.64\n[BBOX-584] 003470 20.2.41.64\n[BBOX-585] 003470 20.2.41.64\n[BBOX-586] 003470 20.2.41.64\n[BBOX-587] 003470 20.2.41.64\n[BBOX-588] 003470 20.2.41.64\n[BBOX-589] 003470 20.2.41.64\n[BBOX-590] 003470 20.2.41.64\n[BBOX-591] 003470 20.2.41.64\n[BBOX-592] 003470 20.2.41.64\n[BBOX-593] 003470 20.2.41.64\n[BBOX-594] 003470 20.2.41.64\n[BBOX-595] 003470 20.2.41.64\n[BBOX-596] 003470 20.2.41.64\n[BBOX-597] 003470 20.2.41.64\n[BBOX-598] 003470 20.2.41.64\n[BBOX-599] 003470 20.2.41.64\n[BBOX-600] 003470 20.2.41.64\n[BBOX-601] 003470 20.2.41.64\n[BBOX-602] 003470 20.2.41.64\n[BBOX-603] 003470 20.2.41.64\n[BBOX-604] 003470 20.2.41.64\n[BBOX-605] 003470 20.2.41.64\n[BBOX-606] 003470 20.2.41.64\n[BBOX-607] 003470 20.2.41.64\n[BBOX-608] 003470 20.2.41.64\n[BBOX-609] 003470 20.2.41.64\n[BBOX-610] 003470 20.2.41.64\n[BBOX-611] 003470 20.2.41.64\n[BBOX-612] 003470 20.2.41.64\n[BBOX-613] 003470 20.2.41.64\n[BBOX-614] 003470 20.2.41.64\n[BBOX-615] 003470 20.2.41.64\n[BBOX-616] 003470 20.2.41.64\n[BBOX-617] 003470 20.2.41.64\n[BBOX-618] 003470 20.2.41.64\n[BBOX-619] 003470 20.2.41.64\n[BBOX-620] 003470 20.2.41.64\n[BBOX-621] 003470 20.2.41.64\n[BBOX-622] 003470 20.2.41.64\n[BBOX-623] 003470 20.2.41.64\n[BBOX-624] 003470 20.2.41.64\n[BBOX-625] 003470 20.2.41.64\n[BBOX-626] 003470 20.2.41.64\n[BBOX-627] 003470 20.2.41.64\n[BBOX-628] 003470 20.2.41.64\n[BBOX-629] 003470 20.2.41.64\n[BBOX-630] 003470 20.2.41.64\n[BBOX-631] 003470 20.2.41.64\n[BBOX-632] 003470 20.2.41.64\n[BBOX-633] 003470 20.2.41.64\n[BBOX-634] 003470 20.2.41.64\n[BBOX-635] 003470 20.2.41.64\n[BBOX-636] 003470 20.2.41.64\n[BBOX-637] 003470 20.2.41.64\n[BBOX-638] 003470 20.2.41.64\n[BBOX-639] 003470 20.2.41.64\n[BBOX-640] 003470 20.2.41.64\n[BBOX-641] 003470 20.2.41.64\n[BBOX-642] 003470 20.2.41.64\n[BBOX-643] 003470 20.2.41.64\n[BBOX-644] 003470 20.2.41.64\n[BBOX-645] 003470 20.2.41.64\n[BBOX-646] 003470 20.2.41.64\n[BBOX-647] 003470 20.2.41.64\n[BBOX-648] 003470 20.2.41.64\n[BBOX-649] 003470 20.2.41.64\n[BBOX-650] 003470 20.2.41.64\n[BBOX-651] 003470 20.2.41.64\n[BBOX-652] 003470 20.2.41.64\n[BBOX-653] 003470 20.2.41.64\n[BBOX-654] 003470 20.2.41.64\n[BBOX-655] 003470 20.2.41.64\n[BBOX-656] 003470 20.2.41.64\n[BBOX-657] 003470 20.2.41.64\n[BBOX-658] 003470 20.2.41.64\n[BBOX-659] 003470 20.2.41.64\n[BBOX-660] 003470 20.2.41.64\n[BBOX-661] 003470 20.2.41.64\n[BBOX-662] 003470 20.2.41.64\n[BBOX-663] 003470 20.2.41.64\n[BBOX-664] 003470 20.2.41.64\n[BBOX-665] 003470 20.2.41.64\n[BBOX-666] 003470 20.2.41.64\n[BBOX-667] 003470 20.2.41.64\n[BBOX-668] 003470 20.2.41.64\n[BBOX-669] 003470 20.2.41.64\n[BBOX-670] 003470 20.2.41.64\n[BBOX-671] 003470 20.2.41.64\n[BBOX-672] 003470 20.2.41.64\n[BBOX-673] 003470 20.2.41.64\n[BBOX-674] 003470 20.2.41.64\n[BBOX-675] 003470 20.2.41.64\n[BBOX-676] 003470 20.2.41.64\n[BBOX-677] 003470 20.2.41.64\n[BBOX-678] 003470 20.2.41.64\n[BBOX-679] 003470 20.2.41.64\n[BBOX-680] 003470 20.2.41.64\n[BBOX-681] 003470 20.2.41.64\n[BBOX-682] 003470 20.2.41.64\n[BBOX-683] 003470 20.2.41.64\n[BBOX-684] 003470 20.2.41.64\n[BBOX-685] 003470 20.2.41.64\n[BBOX-686] 003470 20.2.41.64\n[BBOX-687] 003470 20.2.41.64\n[BBOX-688] 003470 20.2.41.64\n[BBOX-689] 003470 20.2.41.64\n[BBOX-690] 003470 20.2.41.64\n[BBOX-691] 003470 20.2.41.64\n[BBOX-692] 003470 20.2.41.64\n[BBOX-693] 003470 20.2.41.64\n[BBOX-694] 003470 20.2.41.64\n[BBOX-695] 003470 20.2.41.64\n[BBOX-696] 003470 20.2.41.64\n[BBOX-697] 003470 20.2.41.64\n[BBOX-698] 003470 20.2.41.64\n[BBOX-699] 003470 20.2.41.64\n[BBOX-700] 003470 20.2.41.64\n[BBOX-701] 003470 20.2.41.64\n[BBOX-702] 003470 20.2.41.64\n[BBOX-703] 003470 20.2.41.64\n[BBOX-704] 003470 20.2.41.64\n[BBOX-705] 003470 20.2.41.64\n[BBOX-706] 003470 20.2.41.64\n[BBOX-707] 003470 20.2.41.64\n[BBOX-708] 003470 20.2.41.64\n[BBOX-709] 003470 20.2.41.64\n[BBOX-710] 003470 20.2.41.64\n[BBOX-711] 003470 20.2.41.64\n[BBOX-712] 003470 20.2.41.64\n[BBOX-713] 003470 20.2.41.64\n[BBOX-714] 003470 20.2.41.64\n[BBOX-715] 003470 20.2.41.64\n[BBOX-716] 003470 20.2.41.64\n[BBOX-717] 003470 20.2.41.64\n[BBOX-718] 003470 20.2.41.64\n[BBOX-719] 003470 20.2.41.64\n[BBOX-720] 003470 20.2.41.64\n[BBOX-721] 003470 20.2.41.64\n[BBOX-722] 003470 20.2.41.64\n[BBOX-723] 003470 20.2.41.64\n[BBOX-724] 003470 20.2.41.64\n[BBOX-725] 003470 20.2.41.64\n[BBOX-726] 003470 20.2.41.64\n[BBOX-727] 003470 20.2.41.64\n[BBOX-728] 003470 20.2.41.64\n[BBOX-729] 003470 20.2.41.64\n[BBOX-730] 003470 20.2.41.64\n[BBOX-731] 003470 20.2.41.64\n[BBOX-732] 003470 20.2.41.64\n[BBOX-733] 003470 20.2.41.64\n[BBOX-734] 003470 20.2.41.64\n[BBOX-735] 003470 20.2.41.64\n[BBOX-736] 003470 20.2.41.64\n[BBOX-737] 003470 20.2.41.64\n[BBOX-738] 003470 20.2.41.64\n[BBOX-739] 003470 20.2.41.64\n[BBOX-740] 003470 20.2.41.64\n[BBOX-741] 003470 20.2.41.64\n[BBOX-742] 003470 20.2.41.64\n[BBOX-743] 003470 20.2.41.64\n[BBOX-744] 003470 20.2.41.64\n[BBOX-745] 003470 20.2.41.64\n[BBOX-746] 003470 20.2.41.64\n[BBOX-747] 003470 20.2.41.64\n[BBOX-748] 003470 20.2.41.64\n[BBOX-749] 003470 20.2.41.64\n[BBOX-750] 003470 20.2.41.64\n[BBOX-751] 003470 20.2.41.64\n[BBOX-752] 003470 20.2.41.64\n[BBOX-753] 003470 20.2.41.64\n[BBOX-754] 003470 20.2.41.64\n[BBOX-755] 003470 20.2.41.64\n[BBOX-756] 003470 20.2.41.64\n[BBOX-757] 003470 20.2.41.64\n[BBOX-758] 003470 20.2.41.64\n[BBOX-759] 003470 20.2.41.64\n[BBOX-760] 003470 20.2.41.64\n[BBOX-761] 003470 20.2.41.64\n[BBOX-762] 003470 20.2.41.64\n[BBOX-763] 003470 20.2.41.64\n[BBOX-764] 003470 20.2.41.64\n[BBOX-765] 003470 20.2.41.64\n[BBOX-766] 003470 20.2.41.64\n[BBOX-767] 003470 20.2.41.64\n[BBOX-768] 003470 20.2.41.64\n[BBOX-769] 003470 20.2.41.64\n[BBOX-770] 003470 20.2.41.64\n[BBOX-771] 003470 20.2.41.64\n[BBOX-772] 003470 20.2.41.64\n[BBOX-773] 003470 20.2.41.64\n[BBOX-774] 003470 20.2.41.64\n[BBOX-775] 003470 20.2.41.64\n[BBOX-776] 003470 20.2.41.64\n[BBOX-777] 003470 20.2.41.64\n[BBOX-778] 003470 20.2.41.64\n[BBOX-779] 003470 20.2.41.64\n[BBOX-780] 003470 20.2.41.64\n[BBOX-781] 003470 20.2.41.64\n[BBOX-782] 003470 20.2.41.64\n[BBOX-783] 003470 20.2.41.64\n[BBOX-784] 003470 20.2.41.64\n[BBOX-785] 003470 20.2.41.64\n[BBOX-786] 003470 20.2.41.64\n[BBOX-787] 003470 20.2.41.64\n[BBOX-788] 003470 20.2.41.64\n[BBOX-789] 003470 20.2.41.64\n[BBOX-790] 003470 20.2.41.64\n[BBOX-791] 003470 20.2.41.64\n[BBOX-792] 003470 20.2.41.64\n[BBOX-793] 003470 20.2.41.64\n[BBOX-794] 003470 20.2.41.64\n[BBOX-795] 003470 20.2.41.64\n[BBOX-796] 003470 20.2.41.64\n[BBOX-797] 003470 20.2.41.64\n[BBOX-798] 003470 20.2.41.64\n[BBOX-799] 003470 20.2.41.64\n[BBOX-800] 003470 20.2.41.64\n[BBOX-801] 003470 20.2.41.64\n[BBOX-802] 003470 20.2.41.64\n[BBOX-803] 003470 20.2.41.64\n[BBOX-804] 003470 20.2.41.64\n[BBOX-805] 003470 20.2.41.64\n[BBOX-806] 003470 20.2.41.64\n[BBOX-807] 003470 20.2.41.64\n[BBOX-808] 003470 20.2.41.64\n[BBOX-809] 003470 20.2.41.64\n[BBOX-810] 003470 20.2.41.64\n[BBOX-811] 003470 20.2.41.64\n[BBOX-812] 003470 20.2.41.64\n[BBOX-813] 003470 20.2.41.64\n[BBOX-814] 003470 20.2.41.64\n[BBOX-815] 003470 20.2.41.64\n[BBOX-816] 003470 20.2.41.64\n[BBOX-817] 003470 20.2.41.64\n[BBOX-818] 003470 20.2.41.64\n[BBOX-819] 003470 20.2.41.64\n[BBOX-820] 003470 20.2.41.64\n[BBOX-821] 003470 20.2.41.64\n[BBOX-822] 003470 20.2.41.64\n[BBOX-823] 003470 20.2.41.64\n[BBOX-824] 003470 20.2.41.64\n[BBOX-825] 003470 20.2.41.64\n[BBOX-826] 003470 20.2.41.64\n[BBOX-827] 003470 20.2.41.64\n[BBOX-828] 003470 20.2.41.64\n[BBOX-829] 003470 20.2.41.64\n[BBOX-830] 003470 20.2.41.64\n[BBOX-831] 003470 20.2.41.64\n[BBOX-832] 003470 20.2.41.64\n[BBOX-833] 003470 20.2.41.64\n[BBOX-834] 003470 20.2.41.64\n[BBOX-835] 003470 20.2.41.64\n[BBOX-836] 003470 20.2.41.64\n[BBOX-837] 003470 20.2.41.64\n[BBOX-838] 003470 20.2.41.64\n[BBOX-839] 003470 20.2.41.64\n[BBOX-840] 003470 20.2.41.64\n[BBOX-841] 003470 20.2.41.64\n[BBOX-842] 003470 20.2.41.64\n[BBOX-843] 003470 20.2.41.64\n[BBOX-844] 003470 20.2.41.64\n[BBOX-845] 003470 20.2.41.64\n[BBOX-846] 003470 20.2.41.64\n[BBOX-847] 003470 20.2.41.64\n[BBOX-848] 003470 20.2.41.64\n[BBOX-849] 003470 20.2.41.64\n[BBOX-850] 003470 20.2.41.64\n[BBOX-851] 003470 20.2.41.64\n[BBOX-852] 003470 20.2.41.64\n[BBOX-853] 003470 20.2.41.64\n[BBOX-854] 003470 20.2.41.64\n[BBOX-855] 003470 20.2.41.64\n[BBOX-856] 003470 20.2.41.64\n[BBOX-857] 003470 20.2.41.64\n[BBOX-858] 003470 20.2.41.64\n[BBOX-859] 003470 20.2.41.64\n[BBOX-860] 003470 20.2.41.64\n[BBOX-861] 003470 20.2.41.64\n[BBOX-862] 003470 20.2.41.64\n[BBOX-863] 003470 20.2.41.64\n[BBOX-864] 003470 20.2.41.64\n[BBOX-865] 003470 20.2.41.64\n[BBOX-866] 003470 20.2.41.64\n[BBOX-867] 003470 20.2.41.64\n[BBOX-868] 003470 20.2.41.64\n[BBOX-869] 003470 20.2.41.64\n[BBOX-870] 003470 20.2.41.64\n[BBOX-871] 003470 20.2.41.64\n[BBOX-872] 003470 20.2.41.64\n[BBOX-873] 003470 20.2.41.64\n[BBOX-874] 003470 20.2.41.64\n[BBOX-875] 003470 20.2.41.64\n[BBOX-876] 003470 20.2.41.64\n[BBOX-877] 003470 20.2.41.64\n[BBOX-878] 003470 20.2.41.64\n[BBOX-879] 003470 20.2.41.64\n[BBOX-880] 003470 20.2.41.64\n[BBOX-881] 003470 20.2.41.64\n[BBOX-882] 003470 20.2.41.64\n[BBOX-883] 003470 20.2.41.64\n[BBOX-884] 003470 20.2.41.64\n[BBOX-885] 003470 20.2.41.64\n[BBOX-886] 003470 20.2.41.64\n[BBOX-887] 003470 20.2.41.64\n[BBOX-888] 003470 20.2.41.64\n[BBOX-889] 003470 20.2.41.64\n[BBOX-890] 003470 20.2.41.64\n[BBOX-891] 003470 20.2.41.64\n[BBOX-892] 003470 20.2.41.64\n[BBOX-893] 003470 20.2.41.64\n[BBOX-894] 003470 20.2.41.64\n[BBOX-895] 003470 20.2.41.64\n[BBOX-896] 003470 20.2.41.64\n[BBOX-897] 003470 20.2.41.64\n[BBOX-898] 003470 20.2.41.64\n[BBOX-899] 003470 20.2.41.64\n[BBOX-900] 003470 20.2.41.64\n[BBOX-901] 003470 20.2.41.64\n[BBOX-902] 003470 20.2.41.64\n[BBOX-903] 003470 20.2.41.64\n[BBOX-904] 003470 20.2.41.64\n[BBOX-905] 003470 20.2.41.64\n[BBOX-906] 003470 20.2.41.64\n[BBOX-907] 003470 20.2.41.64\n[BBOX-908] 003470 20.2.41.64\n[BBOX-909] 003470 20.2.41.64\n[BBOX-910] 003470 20.2.41.64\n[BBOX-911] 003470 20.2.41.64\n[BBOX-912] 003470 20.2.41.64\n[BBOX-913] 003470 20.2.41.64\n[BBOX-914] 003470 20.2.41.64\n[BBOX-915] 003470 20.2.41.64\n[BBOX-916] 003470 20.2.41.64\n[BBOX-917] 003470 20.2.41.64\n[BBOX-918] 003470 20.2.41.64\n[BBOX-919] 003470 20.2.41.64\n[BBOX-920] 003470 20.2.41.64\n[BBOX-921] 003470 20.2.41.64\n[BBOX-922] 003470 20.2.41.64\n[BBOX-923] 003470 20.2.41.64\n[BBOX-924] 003470 20.2.41.64\n[BBOX-925] 003470 20.2.41.64\n[BBOX-926] 003470 20.2.41.64\n[BBOX-927] 003470 20.2.41.64\n[BBOX-928] 003470 20.2.41.64\n[BBOX-929] 003470 20.2.41.64\n[BBOX-930] 003470 20.2.41.64\n[BBOX-931] 003470 20.2.41.64\n[BBOX-932] 003470 20.2.41.64\n[BBOX-933] 003470 20.2.41.64\n[BBOX-934] 003470 20.2.41.64\n[BBOX-935] 003470 20.2.41.64\n[BBOX-936] 003470 20.2.41.64\n[BBOX-937] 003470 20.2.41.64\n[BBOX-938] 003470 20.2.41.64\n[BBOX-939] 003470 20.2.41.64\n[BBOX-940] 003470 20.2.41.64\n[BBOX-941] 003470 20.2.41.64\n[BBOX-942] 003470 20.2.41\n[BBOX-943] 编辑\n[BBOX-944] 功能\n[BBOX-945] 表格\n[BBOX-946] 签名\n[BBOX-947] 其他\n[BBOX-948] 打印\n[BBOX-949] 预览\n[BBOX-950] 验证CA签名\n[BBOX-951] 手工解锁\n[BBOX-952] 删除\n[BBOX-953] 病历参考\n[BBOX-954] 更新数据\n[BBOX-955] 加载全部病程\n[BBOX-956] 个人模板管理\n[BBOX-957] 返回\n[BBOX-958] 腹部:\n[BBOX-959] 视诊: 外形: 腹部外形正常\n[BBOX-960] 腹围: 未测\n[BBOX-961] 脐部: 正常\n[BBOX-962] 胃形: 未见\n[BBOX-963] 肠形: 未见\n[BBOX-964] 蠕动波: 未见\n[BBOX-965] 腹式呼吸: 正常\n[BBOX-966] 腹壁静脉曲张: 无\n[BBOX-967] 腹壁其它情况: 无\n[BBOX-968] 触诊: 全腹柔软\n[BBOX-969] 压痛反跳痛: 无压痛及反跳痛\n[BBOX-970] 波动感: 无\n[BBOX-971] 振水声: 无\n[BBOX-972] 腹部包块: 腹部未触及包块\n[BBOX-973] 肝脏: 肝脏肋下未触及\n[BBOX-974] 胆囊: 未触及, Murphy征阴性\n[BBOX-975] 脾脏: 脾脏肋下未触及\n[BBOX-976] 肾脏: 未触及\n[BBOX-977] 输尿管压痛点: 无压痛\n[BBOX-978] 叩诊: 肝浊音界: 正常,\n[BBOX-979] 肝上界位于锁骨中线, 第五肋间\n[BBOX-980] 移动性浊音: 阴性,\n[BBOX-981] 肾区叩痛: 无\n[BBOX-982] 听诊: 肠鸣音无明显增强或减弱, 未闻及血管杂音\n[BBOX-983] 肛门直肠: 未查\n[BBOX-984] 生殖器: 未查\n[BBOX-985] 脊柱四肢:\n[BBOX-986] 脊柱外形: 脊柱正常生理弯曲\n[BBOX-987] 70 四 肢：四肢无畸形，未见杵状指（趾），未见静脉曲张，双下肢无凹陷性水肿\n[BBOX-988] 003470 20.2.41.64\n[BBOX-989] 关 节：各关节未见异常，活动无受限\n[BBOX-990] 肌 肉：未见肌肉萎缩，肌张力正常。四肢肌力5级。\n[BBOX-991] 神经系统：\n[BBOX-992] 浅反射：双侧浅反射正常引出\n[BBOX-993] 深反射：双侧深反射正常引出\n[BBOX-994] 病理反射：未引出\n[BBOX-995] 脑膜刺激征：阴性\n[BBOX-996] 003470 20.2.41.64\n[BBOX-997] 003470 20.2.41.64\n[BBOX-998] 003470 20.2.41.64\n[BBOX-999] 003470 20.2.41.64\n[BBOX-1000] 专科情况\n[BBOX-1001] 神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下肢无凹陷性水肿。\n[BBOX-1002] 实验室及器械检查结果\n[BBOX-1003] (2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm\n[BBOX-1004] ，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋巴结彩超\n[BBOX-1005] ：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。\n[BBOX-1006] 003470 20.2.41.64\n[BBOX-1007] 003470 20.2.41.64\n[BBOX-1008] 003470 20.2.41.64\n[BBOX-1009] 003470 20.2.41.64\n[BBOX-1010] CS 扫描全能王\n[BBOX-1011] 3亿人都在用的扫描App\n[BBOX-1012] 2026-02-28 18:30\n[BBOX-1013] 男，因“咳嗽、咳痰1月余”于2026-02-28 15:23入非急诊步行入科。\n[BBOX-1014] 病例特点如下：1、老年期男性，起病缓，病程短。2、患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，\n[BBOX-1015] 伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。3、既往史：平素\n[BBOX-1016] 健康状况：良好。既往病史：否认高血压、冠心病、糖尿病史。传染病史：否，否认肝炎、结核或其他传染病史。预\n[BBOX-1017] 防接种史：正规。过敏史：否认过敏史。外伤史：否认外伤史。手术史：2年前曾行尿道结石手术，具体不详。输血\n[BBOX-1018] 史：否认输血史。系统回顾：无特殊。否认新冠肺炎流行病接触史。4、查体：T：36.8℃，P：75次/分，R：21次/分\n[BBOX-1019] ，BP：138/72mmHg。神志清楚，正常面容，皮肤巩膜无黄染，全身浅表淋巴结未扪及肿大，颈静脉无怒张。胸廓对称\n[BBOX-1020] 无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常，双肺叩诊呈清音，双肺呼吸音\n[BBOX-1021] 清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音。心界不大，心率75次/分，心律齐，各瓣膜区未闻及杂音。腹\n[BBOX-1022] 部外形正常，全腹柔软，无压痛及反跳痛，腹部未触及包块，肝脏肋下未触及，脾脏肋下未触及。移动性浊音阴性。\n[BBOX-1023] 双下肢无凹陷性水肿。浅反射：双侧浅反射正常引出。深反射：双侧深反射正常引出。病理反射：未引出。脑膜刺激\n[BBOX-1024] 征：阴性5、专科情况：神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下\n[BBOX-1025] 肢无凹陷性水肿。6、辅助检查：（2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组\n[BBOX-1026] 织肿块，最大截断面约77mm*60mm，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧\n[BBOX-1027] 胸膜肥厚、钙化。浅表淋巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。\n[BBOX-1028] 初步诊断：1.肺部阴影\n[BBOX-1029] 2.细菌性肺炎\n[BBOX-1030] 诊断依据：1.老年男性，起步缓，病程短\n[BBOX-1031] 2.咳嗽，咳淡黄色粘液痰\n[BBOX-1032] 3.外院胸部CT提示右肺下叶后基底段软组织肿块\n[BBOX-1033] 鉴别诊断。\n[BBOX-1034] 1.肺结核球\n[BBOX-1035] 编辑\n[BBOX-1036] 功能\n[BBOX-1037] 表格\n[BBOX-1038] 签名\n[BBOX-1039] 其他\n[BBOX-1040] 打印\n[BBOX-1041] 预览\n[BBOX-1042] 验证CA签名\n[BBOX-1043] 手工解锁\n[BBOX-1044] 删除\n[BBOX-1045] 病历参考\n[BBOX-1046] 更新数据\n[BBOX-1047] 加载全部病程\n[BBOX-1048] 个人模板管理\n[BBOX-1049] 返回\n[BBOX-1050] 鉴别诊断：\n[BBOX-1051] 1.肺结核球：多见于年轻患者，病灶多见于结核好发部位，如肺上叶尖后段和下叶背段，直径一般<3\n[BBOX-1052] cm。一般无症状，病灶边界清楚，密度高，可有包膜。有时含钙化点，周围有卫星灶。\n[BBOX-1053] 2.急性粟粒性肺结核：应与弥漫型细支气管肺泡癌相鉴别。通常粟粒型肺结核患者年龄较轻，有发热\n[BBOX-1054] ，盗汗等全身中毒症状，呼吸道症状不明显。x线表现为细小、分布均匀、密度较淡的粟粒样结节病灶。\n[BBOX-1055] 而细支气管—肺泡细胞癌两肺多有大小不等的结节状播散病灶，边界清楚、密度较高，进行性发展和增大\n[BBOX-1056] ，且有进行性呼吸困难。\n[BBOX-1057] 3.肺炎：若无毒性症状，抗生素治疗后肺部阴影吸收缓慢，或同一部位反复发生肺炎时，应考虑到肺\n[BBOX-1058] 癌可能。肺部慢性炎症机化，形成团块状的炎性假瘤，也易与肺癌相混淆。但炎性假瘤往往形态不整，边\n[BBOX-1059] 缘不齐，核心密度较高，易伴有胸膜增厚，病灶长期无明显变化。\n[BBOX-1060] 4.肺脓肿：起病急，中毒症状严重，多有寒战、高热、咳嗽、咳大量脓臭痰等症状。肺部x线表现为\n[BBOX-1061] 均匀的大片状炎性阴影，空洞内常见较深液平。结合纤支镜检查和痰脱落细胞检查可以鉴别。\n[BBOX-1062] 5.纵隔淋巴瘤：颇似中央型肺癌，常为双侧性，可有发热等全身症状，需病理诊断。\n[BBOX-1063] VTE血栓风险评估：创建时间:2026-02-28 15:37:11,评估节点:入院,量表名称:Padua评分,分数:0,评分描述:低危,\n[BBOX-1064] 预防措施:undefined\n[BBOX-1065] VTE出血风险评估：创建时间:2026-02-28 18:35:54,评估节点:入院,量表名称:内科出血风险评估,分数:1,评分描述：\n[BBOX-1066] 低危,预防措施:undefined\n[BBOX-1067] 诊疗计划：1.内科护理常规,II级护理。\n[BBOX-1068] 2.完善必要辅助检查如血肿瘤标志物、痰液化验、胸部增强CT、支气管镜检查或浅表淋巴结及肺穿刺活检\n[BBOX-1069] 以确诊，必要时行颅脑MRI、腹部超声、骨扫描或PET-CT等检查以利进一步疾病诊治。\n[BBOX-1070] 3.给予吸氧、抗感染及止血、镇痛等对症支持治疗；明确病理类型拟定下一步治疗方案。\n[BBOX-1071] 是否需手术治疗：否\n[BBOX-1072] 医师签名：\n[BBOX-1073] 住院医师：\n[BBOX-1074] 003470 20.2.41.64\n[BBOX-1075] 003470 20.2.41.64\n[BBOX-1076] 003470 20.2.41.64\n[BBOX-1077] 003470 20.2.41.64\n[BBOX-1078] 003470 20.2.41.64\n[BBOX-1079] 003470 20.2.41.64\n[BBOX-1080] 003470 20.2.41.64\n[BBOX-1081] 003470 20.2.41.64\n[BBOX-1082] 003470 20.2.41.64\n[BBOX-1083] 003470 20.2.41.64\n[BBOX-1084] 003470 20.2.41.64\n[BBOX-1085] 003470 20.2.41.64\n[BBOX-1086] 003470 20.2.41.64\n[BBOX-1087] 003470 20.2.41.64\n[BBOX-1088] 003470 20.2.41.64\n[BBOX-1089] 003470 20.2.41.64\n[BBOX-1090] 003470 20.2.41.64\n[BBOX-1091] 003470 20.2.41.64\n[BBOX-1092] 003470 20.2.41.64\n[BBOX-1093] 003470 20.2.41.64\n[BBOX-1094] 003470 20.2.41.64\n[BBOX-1095] 003470 20.2.41.64\n[BBOX-1096] 003470 20.2.41.64\n[BBOX-1097] 003470 20.2.41.64\n[BBOX-1098] 003470 20.2.41.64\n[BBOX-1099] 003470 20.2.41.64\n[BBOX-1100] 003470 20.2.41.64\n[BBOX-1101] 003470 20.2.41.64\n[BBOX-1102] 003470 20.2.41.64\n[BBOX-1103] 003470 20.2.41.64\n[BBOX-1104] 003470 20.2.41.64\n[BBOX-1105] 003470 20.2.41.64\n[BBOX-1106] 003470 20.2.41.64\n[BBOX-1107] 003470 20.2.41.64\n[BBOX-1108] 003470 20.2.41.64\n[BBOX-1109] 003470 20.2.41.64\n[BBOX-1110] 003470 20.2.41.64\n[BBOX-1111] 003470 20.2.41.64\n[BBOX-1112] 003470 20.2.41.64\n[BBOX-1113] 003470 20.2.41.64\n[BBOX-1114] 003470 20.2.41.64\n[BBOX-1115] 003470 20.2.41.64\n[BBOX-1116] 003470 20.2.41.64\n[BBOX-1117] 003470 20.2.41.64\n[BBOX-1118] 003470 20.2.41.64\n[BBOX-1119] 003470 20.2.41.64\n[BBOX-1120] 003470 20.2.41.64\n[BBOX-1121] 003470 20.2.41.64\n[BBOX-1122] 003470 20.2.41.64\n[BBOX-1123] 003470 20.2.41.64\n[BBOX-1124] 003470 20.2.41.64\n[BBOX-1125] 003470 20.2.41.64\n[BBOX-1126] 003470 20.2.41.64\n[BBOX-1127] 003470 20.2.41.64\n[BBOX-1128] 003470 20.2.41.64\n[BBOX-1129] 003470 20.2.41.64\n[BBOX-1130] 003470 20.2.41.64\n[BBOX-1131] 003470 20.2.41.64\n[BBOX-1132] 003470 20.2.41.64\n[BBOX-1133] 003470 20.2.41.64\n[BBOX-1134] 003470 20.2.41.64\n[BBOX-1135] 003470 20.2.41.64\n[BBOX-1136] 003470 20.2.41.64\n[BBOX-1137] 003470 20.2.41.64\n[BBOX-1138] 003470 20.2.41.64\n[BBOX-1139] 003470 20.2.41.64\n[BBOX-1140] 003470 20.2.41.64\n[BBOX-1141] 003470 20.2.41.64\n[BBOX-1142] 003470 20.2.41.64\n[BBOX-1143] 003470 20.2.41.64\n[BBOX-1144] 003470 20.2.41.64\n[BBOX-1145] 003470 20.2.41.64\n[BBOX-1146] 003470 20.2.41.64\n[BBOX-1147] 003470 20.2.41.64\n[BBOX-1148] 003470 20.2.41.64\n[BBOX-1149] 003470 20.2.41.64\n[BBOX-1150] 003470 20.2.41.64\n[BBOX-1151] 003470 20.2.41.64\n[BBOX-1152] 003470 20.2.41.64\n[BBOX-1153] 003470 20.2.41.64\n[BBOX-1154] 003470 20.2.41.64\n[BBOX-1155] 003470 20.2.41.64\n[BBOX-1156] 003470 20.2.41.64\n[BBOX-1157] 003470 20.2.41.64\n[BBOX-1158] 003470 20.2.41.64\n[BBOX-1159] 003470 20.2.41.64\n[BBOX-1160] 003470 20.2.41.64\n[BBOX-1161] 003470 20.2.41.64\n[BBOX-1162] 003470 20.2.41.64\n[BBOX-1163] 003470 20.2.41.64\n[BBOX-1164] 003470 20.2.41.64\n[BBOX-1165] 003470 20.2.41.64\n[BBOX-1166] 003470 20.2.41.64\n[BBOX-1167] 003470 20.2.41.64\n[BBOX-1168] 003470 20.2.41.64\n[BBOX-1169] 003470 20.2.41.64\n[BBOX-1170] 003470 20.2.41.64\n[BBOX-1171] 003470 20.2.41.64\n[BBOX-1172] 003470 20.2.41.64\n[BBOX-1173] 003470 20.2.41.64\n[BBOX-1174] 003470 20.2.41.64\n[BBOX-1175] 003470 20.2.41.64\n[BBOX-1176] 003470 20.2.41.64\n[BBOX-1177] 003470 20.2.41.64\n[BBOX-1178] 003470 20.2.41.64\n[BBOX-1179] 003470 20.2.41.64\n[BBOX-1180] 003470 20.2.41.64\n[BBOX-1181] 003470 20.2.41.64\n[BBOX-1182] 003470 20.2.41.64\n[BBOX-1183] 003470 20.2.41.64\n[BBOX-1184] 003470 20.2.41.64\n[BBOX-1185] 003470 20.2.41.64\n[BBOX-1186] 003470 20.2.41.64\n[BBOX-1187] 003470 20.2.41.64\n[BBOX-1188] 003470 20.2.41.64\n[BBOX-1189] 003470 20.2.41.64\n[BBOX-1190] 003470 20.2.41.64\n[BBOX-1191] 003470 20.2.41.64\n[BBOX-1192] 003470 20.2.41.64\n[BBOX-1193] 003470 20.2.41.64\n[BBOX-1194] 003470 20.2.41.64\n[BBOX-1195] 003470 20.2.41.64\n[BBOX-1196] 003470 20.2.41.64\n[BBOX-1197] 003470 20.2.41.64\n[BBOX-1198] 003470 20.2.41.64\n[BBOX-1199] 003470 20.2.41.64\n[BBOX-1200] 003470 20.2.41.64\n[BBOX-1201] 003470 20.2.41.64\n[BBOX-1202] 003470 20.2.41.64\n[BBOX-1203] 003470 20.2.41.64\n[BBOX-1204] 003470 20.2.41.64\n[BBOX-1205] 003470 20.2.41.64\n[BBOX-1206] 003470 20.2.41.64\n[BBOX-1207] 003470 20.2.41.64\n[BBOX-1208] 003470 20.2.41.64\n[BBOX-1209] 003470 20.2.41.64\n[BBOX-1210] 003470 20.2.41.64\n[BBOX-1211] 003470 20.2.41.64\n[BBOX-1212] 003470 20.2.41.64\n[BBOX-1213] 003470 20.2.41.64\n[BBOX-1214] 003470 20.2.41.64\n[BBOX-1215] 003470 20.2.41.64\n[BBOX-1216] 003470 20.2.41.64\n[BBOX-1217] 003470 20.2.41.64\n[BBOX-1218] 003470 20.2.41.64\n[BBOX-1219] 003470 20.2.41.64\n[BBOX-1220] 003470 20.2.41.64\n[BBOX-1221] 003470 20.2.41.64\n[BBOX-1222] 003470 20.2.41.64\n[BBOX-1223] 003470 20.2.41.64\n[BBOX-1224] 003470 20.2.41.64\n[BBOX-1225] 003470 20.2.41.64\n[BBOX-1226] 003470 20.2.41.64\n[BBOX-1227] 003470 20.2.41.64\n[BBOX-1228] 003470 20.2.41.64\n[BBOX-1229] 003470 20.2.41.64\n[BBOX-1230] 003470 20.2.41.64\n[BBOX-1231] 003470 20.2.41.64\n[BBOX-1232] 003470 20.2.41.64\n[BBOX-1233] 003470 20.2.41.64\n[BBOX-1234] 003470 20.2.41.64\n[BBOX-1235] 003470 20.2.41.64\n[BBOX-1236] 003470 20.2.41.64\n[BBOX-1237] 003470 20.2.41.64\n[BBOX-1238] 003470 20.2.41.64\n[BBOX-1239] 003470 20.2.41.64\n[BBOX-1240] 003470 20.2.41.64\n[BBOX-1241] 003470 20.2.41.64\n[BBOX-1242] 003470 20.2.41.64\n[BBOX-1243] 003470 20.2.41.64\n[BBOX-1244] 003470 20.2.41.64\n[BBOX-1245] 003470 20.2.41.64\n[BBOX-1246] 003470 20.2.41.64\n[BBOX-1247] 003470 20.2.41.64\n[BBOX-1248] 003470 20.2.41.64\n[BBOX-1249] 003470 20.2.41.64\n[BBOX-1250] 003470 20.2.41.64\n[BBOX-1251] 003470 20.2.41.64\n[BBOX-1252] 003470 20.2.41.64\n[BBOX-1253] 003470 20.2.41.64\n[BBOX-1254] 003470 20.2.41.64\n[BBOX-1255] 003470 20.2.41.64\n[BBOX-1256] 003470 20.2.41.64\n[BBOX-1257] 003470 20.2.41.64\n[BBOX-1258] 003470 20.2.41.64\n[BBOX-1259] 003470 20.2.41.64\n[BBOX-1260] 003470 20.2.41.64\n[BBOX-1261] 003470 20.2.41.64\n[BBOX-1262] 003470 20.2.41.64\n[BBOX-1263] 003470 20.2.41.64\n[BBOX-1264] 003470 20.2.41.64\n[BBOX-1265] 003470 20.2.41.64\n[BBOX-1266] 003470 20.2.41.64\n[BBOX-1267] 003470 20.2.41.64\n[BBOX-1268] 003470 20.2.41.64\n[BBOX-1269] 003470 20.2.41.64\n[BBOX-1270] 003470 20.2.41.64\n[BBOX-1271] 003470 20.2.41.64\n[BBOX-1272] 003470 20.2.41.64\n[BBOX-1273] 003470 20.2.41.64\n[BBOX-1274] 003470 20.2.41.64\n[BBOX-1275] 003470 20.2.41.64\n[BBOX-1276] 003470 20.2.41.64\n[BBOX-1277] 003470 20.2.41.64\n[BBOX-1278] 003470 20.2.41.64\n[BBOX-1279] 003470 20.2.41.64\n[BBOX-1280] 003470 20.2.41.64\n[BBOX-1281] 003470 20.2.41.64\n[BBOX-1282] 003470 20.2.41.64\n[BBOX-1283] 003470 20.2.41.64\n[BBOX-1284] 003470 20.2.41.64\n[BBOX-1285] 003470 20.2.41.64\n[BBOX-1286] 003470 20.2.41.64\n[BBOX-1287] 003470 20.2.41.64\n[BBOX-1288] 003470 20.2.41.64\n[BBOX-1289] 003470 20.2.41.64\n[BBOX-1290] 003470 20.2.41.64\n[BBOX-1291] 003470 20.2.41.64\n[BBOX-1292] 003470 20.2.41.64\n[BBOX-1293] 003470 20.2.41.64\n[BBOX-1294] 003470 20.2.41.64\n[BBOX-1295] 003470 20.2.41.64\n[BBOX-1296] 003470 20.2.41.64\n[BBOX-1297] 003470 20.2.41.64\n[BBOX-1298] 003470 20.2.41.64\n[BBOX-1299] 003470 20.2.41.64\n[BBOX-1300] 003470 20.2.41.64\n[BBOX-1301] 003470 20.2.41.64\n[BBOX-1302] 003470 20.2.41.64\n[BBOX-1303] 003470 20.2.41.64\n[BBOX-1304] 003470 20.2.41.64\n[BBOX-1305] 003470 20.2.41.64\n[BBOX-1306] 003470 20.2.41.64\n[BBOX-1307] 003470 20.2.41.64\n[BBOX-1308] 003470 20.2.41.64\n[BBOX-1309] 003470 20.2.41.64\n[BBOX-1310] 003470 20.2.41.64\n[BBOX-1311] 003470 20.2.41.64\n[BBOX-1312] 003470 20.2.41.64\n[BBOX-1313] 003470 20.2.41.64\n[BBOX-1314] 003470 20.2.41.64\n[BBOX-1315] 003470 20.2.41.64\n[BBOX-1316] 003470 20.2.41.64\n[BBOX-1317] 003470 20.2.41.64\n[BBOX-1318] 003470 20.2.41.64\n[BBOX-1319] 003470 20.2.41.64\n[BBOX-1320] 003470 20.2.41.64\n[BBOX-1321] 003470 20.2.41.64\n[BBOX-1322] 003470 20.2.41.64\n[BBOX-1323] 003470 20.2.41.64\n[BBOX-1324] 003470 20.2.41.64\n[BBOX-1325] 003470 20.2.41.64\n[BBOX-1326] 003470 20.2.41.64\n[BBOX-1327] 003470 20.2.41.64\n[BBOX-1328] 003470 20.2.41.64\n[BBOX-1329] 003470 20.2.41.64\n[BBOX-1330] 003470 20.2.41.64\n[BBOX-1331] 003470 20.2.41.64\n[BBOX-1332] 003470 20.2.41.64\n[BBOX-1333] 003470 20.2.41.64\n[BBOX-1334] 003470 20.2.41.64\n[BBOX-1335] 003470 20.2.41.64\n[BBOX-1336] 003470 20.2.41.64\n[BBOX-1337] 003470 20.2.41.64\n[BBOX-1338] 003470 20.2.41.64\n[BBOX-1339] 003470 20.2.41.64\n[BBOX-1340] 003470 20.2.41.64\n[BBOX-1341] 003470 20.2.41.64\n[BBOX-1342] 003470 20.2.41.64\n[BBOX-1343] 003470 20.2.41.64\n[BBOX-1344] 003470 20.2.41.64\n[BBOX-1345] 003470 20.2.41.64\n[BBOX-1346] 003470 20.2.41.64\n[BBOX-1347] 003470 20.2.41.64\n[BBOX-1348] 003470 20.2.41.64\n[BBOX-1349] 003470 20.2.41.64\n[BBOX-1350] 003470 20.2.41.64\n[BBOX-1351] 003470 20.2.41.64\n[BBOX-1352] 003470 20.2.41.64\n[BBOX-1353] 003470 20.2.41.64\n[BBOX-1354] 003470 20.2.41.64\n[BBOX-1355] 003470 20.2.41.64\n[BBOX-1356] 003470 20.2.41.64\n[BBOX-1357] 003470 20.2.41.64\n[BBOX-1358] 003470 20.2.41.64\n[BBOX-1359] 003470 20.2.41.64\n[BBOX-1360] 003470 20.2.41.64\n[BBOX-1361] 003470 20.2.41.64\n[BBOX-1362] 003470 20.2.41.64\n[BBOX-1363] 003470 20.2.41.64\n[BBOX-1364] 003470 20.2.41.64\n[BBOX-1365] 003470 20.2.41.64\n[BBOX-1366] 003470 20.2.41.64\n[BBOX-1367] 003470 20.2.41.64\n[BBOX-1368] 003470 20.2.41.64\n[BBOX-1369] 003470 20.2.41.64\n[BBOX-1370] 003470 20.2.41.64\n[BBOX-1371] 003470 20.2.41.64\n[BBOX-1372] 003470 20.2.41.64\n[BBOX-1373] 003470 20.2.41.64\n[BBOX-1374] 003470 20.2.41.64\n[BBOX-1375] 003470 20.2.41.64\n[BBOX-1376] 003470 20.2.41.64\n[BBOX-1377] 003470 20.2.41.64\n[BBOX-1378] 003470 20.2.41.64\n[BBOX-1379] 003470 20.2.41.64\n[BBOX-1380] 003470 20.2.41.64\n[BBOX-1381] 003470 20.2.41.64\n[BBOX-1382] 003470 20.2.41.64\n[BBOX-1383] 003470 20.2.41.64\n[BBOX-1384] 003470 20.2.41.64\n[BBOX-1385] 003470 20.2.41.64\n[BBOX-1386] 003470 20.2.41.64\n[BBOX-1387] 003470 20.2.41.64\n[BBOX-1388] 003470 20.2.41.64\n[BBOX-1389] 003470 20.2.41.64\n[BBOX-1390] 003470 20.2.41.64\n[BBOX-1391] 003470 20.2.41.64\n[BBOX-1392] 003470 20.2.41.64\n[BBOX-1393] 003470 20.2.41.64\n[BBOX-1394] 003470 20.2.41.64\n[BBOX-1395] 003470 20.2.41.64\n[BBOX-1396] 003470 20.2.41.64\n[BBOX-1397] 003470 20.2.41.64\n[BBOX-1398] 003470 20.2.41.64\n[BBOX-1399] 003470 20.2.41.64\n[BBOX-1400] 003470 20.2.41.64\n[BBOX-1401] 003470 20.2.41.64\n[BBOX-1402] 003470 20.2.41.64\n[BBOX-1403] 003470 20.2.41.64\n[BBOX-1404] 003470 20.2.41.64\n[BBOX-1405] 003470 20.2.41.64\n[BBOX-1406] 003470 20.2.41.64\n[BBOX-1407] 003470 20.2.41.64\n[BBOX-1408] 003470 20.2.41.64\n[BBOX-1409] 003470 20.2.41.64\n[BBOX-1410] 003470 20.2.41.64\n[BBOX-1411] 003470 20.2.41.64\n[BBOX-1412] 003470 20.2.41.64\n[BBOX-1413] 003470 20.2.41.64\n[BBOX-1414] 003470 20.2.41.64\n[BBOX-1415] 003470 20.2.41.64\n[BBOX-1416] 003470 20.2.41.64\n[BBOX-1417] 003470 20.2.41.64\n[BBOX-1418] 003470 20.2.41.64\n[BBOX-1419] 003470 20.2.41.64\n[BBOX-1420] 003470 20.2.41.64\n[BBOX-1421] 003470 20.2.41.64\n[BBOX-1422] 003470 20.2.41.64\n[BBOX-1423] 003470 20.2.41.64\n[BBOX-1424] 003470 20.2.41.64\n[BBOX-1425] 003470 20.2.41.64\n[BBOX-1426] 003470 20.2.41.64\n[BBOX-1427] 003470 20.2.41.64\n[BBOX-1428] 003470 20.2.41.64\n[BBOX-1429] 003470 20.2.41.64\n[BBOX-1430] 003470 20.2.41.64\n[BBOX-1431] 003470 20.2.41.64\n[BBOX-1432] 003470 20.2.41.64\n[BBOX-1433] 003470 20.2.41.64\n[BBOX-1434] 003470 20.2.41.64\n[BBOX-1435] 003470 20.2.41.64\n[BBOX-1436] 003470 20.2.41.64\n[BBOX-1437] 003470 20.2.41.64\n[BBOX-1438] 003470 20.2.41.64\n[BBOX-1439] 003470 20.2.41.64\n[BBOX-1440] 003470 20.2.41.64\n[BBOX-1441] 003470 20.2.41.64\n[BBOX-1442] 003470 20.2.41.64\n[BBOX-1443] 003470 20.2.41.64\n[BBOX-1444] 003470 20.2.41.64\n[BBOX-1445] 003470 20.2.41.64\n[BBOX-1446] 003470 20.2.41.64\n[BBOX-1447] 003470 20.2.41.64\n[BBOX-1448] 003470 20.2.41.64\n[BBOX-1449] 003470 20.2.41.64\n[BBOX-1450] 003470 20.2.41.64\n[BBOX-1451] 003470 20.2.41.64\n[BBOX-1452] 003470 20.2.41.64\n[BBOX-1453] 003470 20.2.41.64\n[BBOX-1454] 003470 20.2.41.64\n[BBOX-1455] 003470 20.2.41.64\n[BBOX-1456] 003470 20.2.41.64\n[BBOX-1457] 003470 20.2.41.64\n[BBOX-1458] 003470 20.2.41.64\n[BBOX-1459] 003470 20.2.41.64\n[BBOX-1460] 003470 20.2.41.64\n[BBOX-1461] 003470 20.2.41.64\n[BBOX-1462] 003470 20.2.41.64\n[BBOX-1463] 003470 20.2.41.64\n[BBOX-1464] 003470 20.2.41.64\n[BBOX-1465] 003470 20.2.41.64\n[BBOX-1466] 003470 20.2.41.64\n[BBOX-1467] 003470 20.2.41.64\n[BBOX-1468] 003470 20.2.41.64\n[BBOX-1469] 003470 20.2.41.64\n[BBOX-1470] 003470 20.2.41.64\n[BBOX-1471] 003470 20.2.41.64\n[BBOX-1472] 003470 20.2.41.64\n[BBOX-1473] 003470 20.2.41.64\n[BBOX-1474] 003470 20.2.41.64\n[BBOX-1475] 003470 20.2.41.64\n[BBOX-1476] 003470 20.2.41.64\n[BBOX-1477] 003470 20.2.41.64\n[BBOX-1478] 003470 20.2.41.64\n[BBOX-1479] 003470 20.2.41.64\n[BBOX-1480] 003470 20.2.41.64\n[BBOX-1481] 003470 20.2.41.64\n[BBOX-1482] 003470 20.2.41.64\n[BBOX-1483] 003470 20.2.41.64\n[BBOX-1484] 003470 20.2.41.64\n[BBOX-1485] 003470 20.2.41.64\n[BBOX-1486] 003470 20.2.41.64\n[BBOX-1487] 003470 20.2.41.64\n[BBOX-1488] 003470 20.2.41.64\n[BBOX-1489] 003470 20.2.41.64\n[BBOX-1490] 003470 20.2.41.64\n[BBOX-1491] 003470 20.2.41.64\n[BBOX-1492] 003470 20.2.41.64\n[BBOX-1493] 003470 20.2.41.64\n[BBOX-1494] 003470 20.2.41.64\n[BBOX-1495] 003470 20.2.41.64\n[BBOX-1496] 003470 20.2.41.64\n[BBOX-1497] 003470 20.2.41.64\n[BBOX-1498] 003470 20.2.41.64\n[BBOX-1499] 003470 20.2.41.64\n[BBOX-1500] 003470 20.2.41.64\n[BBOX-1501] 003470 20.2.41.64\n[BBOX-1502] 003470 20.2.41.64\n[BBOX-1503] 003470 20.2.41.64\n[BBOX-1504] 003470 20.2.41.64\n[BBOX-1505] 003470 20.2.41.64\n[BBOX-1506] 003470 20.2.41.64\n[BBOX-1507] 003470 20.2.41.64\n[BBOX-1508] 003470 20.2.41.64\n[BBOX-1509] 003470 20.2.41.64\n[BBOX-1510] 003470 20.2.41.64\n[BBOX-1511] 003470 20.2.41.64\n[BBOX-1512] 003470 20.2.41.64\n[BBOX-1513] 003470 20.2.41.64\n[BBOX-1514] 003470 20.2.41.64\n[BBOX-1515] 003470 20.2.41.64\n[BBOX-1516] 003470 20.2.41.64\n[BBOX-1517] 003470 20.2.41.64\n[BBOX-1518] 003470 20.2.41.64\n[BBOX-1519] 003470 20.2.41.64\n[BBOX-1520] 003470 20.2.41.64\n[BBOX-1521] 003470 20.2.41.64\n[BBOX-1522] 003470 20.2.41.64\n[BBOX-1523] 003470 20.2.41.64\n[BBOX-1524] 003470 20.2.41.64\n[BBOX-1525] 003470 20.2.41.64\n[BBOX-1526] 003470 20.2.41.64\n[BBOX-1527] 003470 20.2.41.64\n[BBOX-1528] 003470 20.2.41.64\n[BBOX-1529] 003470 20.2.41.64\n[BBOX-1530] 003470 20.2.41.64\n[BBOX-1531] 003470 20.2.41.64\n[BBOX-1532] 003470 20.2.41.64\n[BBOX-1533] 003470 20.2.41.64\n[BBOX-1534] 003470 20.2.41.64\n[BBOX-1535] 003470 20.2.41.64\n[BBOX-1536] 003470 20.2.41.64\n[BBOX-1537] 003470 20.2.41.64\n[BBOX-1538] 003470 20.2.41.64\n[BBOX-1539] 003470 20.2.41.64\n[BBOX-1540] 003470 20.2.41.64\n[BBOX-1541] 003470 20.2.41.64\n[BBOX-1542] 003470 20.2.41.64\n[BBOX-1543] 003470 20.2.41.64\n[BBOX-1544] 003470 20.2.41.64\n[BBOX-1545] 003470 20.2.41.64\n[BBOX-1546] 003470 20.2.41.64\n[BBOX-1547] 003470 20.2.41.64\n[BBOX-1548] 003470 20.2.41.64\n[BBOX-1549] 003470 20.2.41.64\n[BBOX-1550] 003470 20.2.41.64\n[BBOX-1551] 003470 20.2.41.64\n[BBOX-1552] 003470 20.2.41.64\n[BBOX-1553] 003470 20.2.41.64\n[BBOX-1554] 003470 20.2.41.64\n[BBOX-1555] 003470 20.2.41.64\n[BBOX-1556] 003470 20.2.41.64\n[BBOX-1557] 003470 20.2.41.64\n[BBOX-1558] 003470 20.2.41.64\n[BBOX-1559] 003470 20.2.41.64\n[BBOX-1560] 003470 20.2.41.64\n[BBOX-1561] 003470 20.2.41.64\n[BBOX-1562] 003470 20.2.41.64\n[BBOX-1563] 003470 20.2.41.64\n[BBOX-1564] 003470 20.2.41.64\n[BBOX-1565] 003470 20.2.41.64\n[BBOX-1566] 003470 20.2.41.64\n[BBOX-1567] 003470 20.2.41.64\n[BBOX-1568] 003470 20.2.41.64\n[BBOX-1569] 003470 20.2.41.64\n[BBOX-1570] 003470 20.2.41.64\n[BBOX-1571] 003470 20.2.41.64\n[BBOX-1572] 003470 20.2.41.64\n[BBOX-1573] 003470 20.2.41.64\n[BBOX-1574] 003470 20.2.41.64\n[BBOX-1575] 003470 20.2.41.64\n[BBOX-1576] 003470 20.2.41.64\n[BBOX-1577] 003470 20.2.41.64\n[BBOX-1578] 003470 20.2.41.64\n[BBOX-1579] 003470 20.2.41.64\n[BBOX-1580] 003470 20.2.41.64\n[BBOX-1581] 003470 20.2.41.64\n[BBOX-1582] 003470 20.2.41.64\n[BBOX-1583] 003470 20.2.41.64\n[BBOX-1584] 003470 20.2.41.64\n[BBOX-1585] 003470 20.2.41.64\n[BBOX-1586] 003470 20.2.41.64\n[BBOX-1587] 003470 20.2.41.64\n[BBOX-1588] 003470 20.2.41.64\n[BBOX-1589] 003470 20.2.41.64\n[BBOX-1590] 003470 20.2.41.64\n[BBOX-1591] 003470 20.2.41.64\n[BBOX-1592] 003470 20.2.41.64\n[BBOX-1593] 003470 20.2.41.64\n[BBOX-1594] 003470 20.2.41.64\n[BBOX-1595] 003470 20.2.41.64\n[BBOX-1596] 003470 20.2.41.64\n[BBOX-1597] 003470 20.2.41.64\n[BBOX-1598] 003470 20.2.41.64\n[BBOX-1599] 003470 20.2.41.64\n[BBOX-1600] 003470 20.2.41.64\n[BBOX-1601] 003470 20.2.41.64\n[BBOX-1602] 003470 20.2.41.64\n[BBOX-1603] 003470 20.2.41.64\n[BBOX-1604] 003470 20.2.41.64\n[BBOX-1605] 003470 20.2.41.64\n[BBOX-1606] 003470 20.2.41.64\n[BBOX-1607] 003470 20.2.41.64\n[BBOX-1608] 003470 20.2.41.64\n[BBOX-1609] 003470 20.2.41.64\n[BBOX-1610] 003470 20.2.41.64\n[BBOX-1611] 003470 20.2.41.64\n[BBOX-1612] 003470 20.2.41.64\n[BBOX-1613] 003470 20.2.41.64\n[BBOX-1614] 003470 20.2.41.64\n[BBOX-1615] 003470 20.2.41.64\n[BBOX-1616] 003470 20.2.41.64\n[BBOX-1617] 003470 20.2.41.64\n[BBOX-1618] 003470 20.2.41.64\n[BBOX-1619] 003470 20.2.41.64\n[BBOX-1620] 003470 20.2.41.64\n[BBOX-1621] 003470 20.2.41.64\n[BBOX-1622] 003470 20.2.41.64\n[BBOX-1623] 003470 20.2.41.64\n[BBOX-1624] 003470 20.2.41.64\n[BBOX-1625] 003470 20.2.41.64\n[BBOX-1626] 003470 20.2.41.64\n[BBOX-1627] 003470 20.2.41.64\n[BBOX-1628] 003470 20.2.41.64\n[BBOX-1629] 003470 20.2.41.64\n[BBOX-1630] 003470 20.2.41.64\n[BBOX-1631] 003470 20.2.41.64\n[BBOX-1632] 003470 20.2.41.64\n[BBOX-1633] 003470 20.2.41.64\n[BBOX-1634] 003470 20.2.41.64\n[BBOX-1635] 003470 20.2.41.64\n[BBOX-1636] 003470 20.2.41.64\n[BBOX-1637] 003470 20.2.41.64\n[BBOX-1638] 003470 20.2.41.64\n[BBOX-1639] 003470 20.2.41.64\n[BBOX-1640] 003470 20.2.41.64\n[BBOX-1641] 003470 20.2.41.64\n[BBOX-1642] 003470 20.2.41.64\n[BBOX-1643] 003470 20.2.41.64\n[BBOX-1644] 003470 20.2.41.64\n[BBOX-1645] 003470 20.2.41.64\n[BBOX-1646] 003470 20.2.41.64\n[BBOX-1647] 003470 20.2.41.64\n[BBOX-1648] 003470 20.2.41.64\n[BBOX-1649] 003470 20.2.41.64\n[BBOX-1650] 003470 20.2.41.64\n[BBOX-1651] 003470 20.2.41.64\n[BBOX-1652] 003470 20.2.41.64\n[BBOX-1653] 003470 20.2.41.64\n[BBOX-1654] 003470 20.2.41.64\n[BBOX-1655] 003470 20.2.41.64\n[BBOX-1656] 003470 20.2.41.64\n[BBOX-1657] 003470 20.2.41.64\n[BBOX-1658] 003470 20.2.41.64\n[BBOX-1659] 003470 20.2.41.64\n[BBOX-1660] 003470 20.2.41.64\n[BBOX-1661] 003470 20.2.41.64\n[BBOX-1662] 003470 20.2.41.64\n[BBOX-1663] 003470 20.2.41.64\n[BBOX-1664] 003470 20.2.41.64\n[BBOX-1665] 003470 20.2.41.64\n[BBOX-1666] 003470 20.2.41.64\n[BBOX-1667] 003470 20.2.41.64\n[BBOX-1668] 003470 20.2.41.64\n[BBOX-1669] 003470 20.2.41.64\n[BBOX-1670] 003470 20.2.41.64\n[BBOX-1671] 003470 20.2.41.64\n[BBOX-1672] 003470 20.2.41.64\n[BBOX-1673] 003470 20.2.41.64\n[BBOX-1674] 003470 20.2.41.64\n[BBOX-1675] 003470 20.2.41.64\n[BBOX-1676] 003470 20.2.41.64\n[BBOX-1677] 003470 20.2.41.64\n[BBOX-1678] 003470 20.2.41.64\n[BBOX-1679] 003470 20.2.41.64\n[BBOX-1680] 003470 20.2.41.64\n[BBOX-1681] 003470 20.2.41.64\n[BBOX-1682] 003470 20.2.41.64\n[BBOX-1683] 003470 20.2.41.64\n[BBOX-1684] 003470 20.2.41.64\n[BBOX-1685] 003470 20.2.41.64\n[BBOX-1686] 003470 20.2.41.64\n[BBOX-1687] 003470 20.2.41.64\n[BBOX-1688] 003470 20.2.41.64\n[BBOX-1689] 003470 20.2.41.64\n[BBOX-1690] 003470 20.2.41.64\n[BBOX-1691] 003470 20.2.41.64\n[BBOX-1692] 003470 20.2.41.64\n[BBOX-1693] 003470 20.2.41.64\n[BBOX-1694] 003470 20.2.41.64\n[BBOX-1695] 003470 20.2.41.64\n[BBOX-1696] 003470 20.2.41.64\n[BBOX-1697] 003470 20.2.41.64\n[BBOX-1698] 003470 20.2.41.64\n[BBOX-1699] 003470 20.2.41.64\n[BBOX-1700] 003470 20.2.41.64\n[BBOX-1701] 003470 20.2.41.64\n[BBOX-1702] 003470 20.2.41.64\n[BBOX-1703] 003470 20.2.41.64\n[BBOX-1704] 003470 20.2.41.64\n[BBOX-1705] 003470 20.2.41.64\n[BBOX-1706] 003470 20.2.41.64\n[BBOX-1707] 003470 20.2.41.64\n[BBOX-1708] 003470 20.2.41.64\n[BBOX-1709] 003470 20.2.41.64\n[BBOX-1710] 003470 20.2.41.64\n[BBOX-1711] 003470 20.2.41.64\n[BBOX-1712] 003470 20.2.41.64\n[BBOX-1713] 003470 20.2.41.64\n[BBOX-1714] 003470 20.2.41.64\n[BBOX-1715] 003470 20.2.41.64\n[BBOX-1716] 003470 20.2.41.64\n[BBOX-1717] 003470 20.2.41.64\n[BBOX-1718] 003470 20.2.41.64\n[BBOX-1719] 003470 20.2.41.64\n[BBOX-1720] 003470 20.2.41.64\n[BBOX-1721] 003470 20.2.41.64\n[BBOX-1722] 003470 20.2.41.64\n[BBOX-1723] 003470 20.2.41.64\n[BBOX-1724] 003470 20.2.41.64\n[BBOX-1725] 003470 20.2.41.64\n[BBOX-1726] 003470 20.2.41.64\n[BBOX-1727] 003470 20.2.41.64\n[BBOX-1728] 003470 20.2.41.64\n[BBOX-1729] 003470 20.2.41.64\n[BBOX-1730] 003470 20.2.41.64\n[BBOX-1731] 003470 20.2.41.64\n[BBOX-1732] 003470 20.2.41.64\n[BBOX-1733] 003470 20.2.41.64\n[BBOX-1734] 003470 20.2.41.64\n[BBOX-1735] 003470 20.2.41.64\n[BBOX-1736] 003470 20.2.41.64\n[BBOX-1737] 003470 20.2.41.64\n[BBOX-1738] 003470 20.2.41.64\n[BBOX-1739] 003470 20.2.41.64\n[BBOX-1740] 003470 20.2.41.64\n[BBOX-1741] 003470 20.2.41.64\n[BBOX-1742] 003470 20.2.41.64\n[BBOX-1743] 003470 20.2.41.64\n[BBOX-1744] 003470 20.2.41.64\n[BBOX-1745] 003470 20.2.41.64\n[BBOX-1746] 003470 20.2.41.64\n[BBOX-1747] 003470 20.2.41.64\n[BBOX-1748] 003470 20.2.41.64\n[BBOX-1749] 003470 20.2.41.64\n[BBOX-1750] 003470 20.2.41.64\n[BBOX-1751] 003470 20.2.41.64\n[BBOX-1752] 003470 20.2.41.64\n[BBOX-1753] 003470 20.2.41.64\n[BBOX-1754] 003470 20.2.41.64\n[BBOX-1755] 003470 20.2.41.64\n[BBOX-1756] 003470 20.2.41.64\n[BBOX-1757] 003470 20.2.41.64\n[BBOX-1758] 003470 20.2.41.64\n[BBOX-1759] 003470 20.2.41.64\n[BBOX-1760] 003470 20.2.41.64\n[BBOX-1761] 003470 20.2.41.64\n[BBOX-1762] 003470 20.2.41.64\n[BBOX-1763] 003470 20.2.41.64\n[BBOX-1764] 003470 20.2.41.64\n[BBOX-1765] 003470 20.2.41.64\n[BBOX-1766] 003470 20.2.41.64\n[BBOX-1767] 003470 20.2.41.64\n[BBOX-1768] 003470 20.2.41.64\n[BBOX-1769] 003470 20.2.41.64\n[BBOX-1770] 003470 20.2.41.64\n[BBOX-1771] 003470 20.2.41.64\n[BBOX-1772] 003470 20.2.41.64\n[BBOX-1773] 003470 20.2.41.64\n[BBOX-1774] 003470 20.2.41.64\n[BBOX-1775] 003470 20.2.41.64\n[BBOX-1776] 003470 20.2.41.64\n[BBOX-1777] 003470 20.2.41.64\n[BBOX-1778] 003470 20.2.41.64\n[BBOX-1779] 003470 20.2.41.64\n[BBOX-1780] 003470 20.2.41.64\n[BBOX-1781] 003470 20.2.41.64\n[BBOX-1782] 003470 20.2.41.64\n[BBOX-1783] 003470 20.2.41.64\n[BBOX-1784] 003470 20.2.41.64\n[BBOX-1785] 003470 20.2.41.64\n[BBOX-1786] 003470 20.2.41.64\n[BBOX-1787] 003470 20.2.41.64\n[BBOX-1788] 003470 20.2.41.64\n[BBOX-1789] 003470 20.2.41.64\n[BBOX-1790] 003470 20.2.41.64\n[BBOX-1791] 003470 20.2.41.64\n[BBOX-1792] 003470 20.2.41.64\n[BBOX-1793] 003470 20.2.41.64\n[BBOX-1794] 003470 20.2.41.64\n[BBOX-1795] 003470 20.2.41.64\n[BBOX-1796] 003470 20.2.41.64\n[BBOX-1797] 003470 20.2.41.64\n[BBOX-1798] 003470 20.2.41.64\n[BBOX-1799] 003470 20.2.41.64\n[BBOX-1800] 003470 20.2.41.64\n[BBOX-1801] 003470 20.2.41.64\n[BBOX-1802] 003470 20.2.41.64\n[BBOX-1803] 003470 20.2.41.64\n[BBOX-1804] 003470 20.2.41.64\n[BBOX-1805] 003470 20.2.41.64\n[BBOX-1806] 003470 20.2.41.64\n[BBOX-1807] 003470 20.2.41.64\n[BBOX-1808] 003470 20.2.41.64\n[BBOX-1809] 003470 20.2.41.64\n[BBOX-1810] 003470 20.2.41.64\n[BBOX-1811] 003470 20.2.41.64\n[BBOX-1812] 003470 20.2.41.64\n[BBOX-1813] 003470 20.2.41.64\n[BBOX-1814] 003470 20.2.41.64\n[BBOX-1815] 003470 20.2.41.64\n[BBOX-1816] 003470 20.2.41.64\n[BBOX-1817] 003470 20.2.41.64\n[BBOX-1818] 003470 20.2.41.64\n[BBOX-1819] 003470 20.2.41.64\n[BBOX-1820] 003470 20.2.41.64\n[BBOX-1821] 003470 20.2.41.64\n[BBOX-1822] 003470 20.2.41.64\n[BBOX-1823] 003470 20.2.41.64\n[BBOX-1824] 003470 20.2.41.64\n[BBOX-1825] 003470 20.2.41.64\n[BBOX-1826] 003470 20.2.41.64\n[BBOX-1827] 003470 20.2.41.64\n[BBOX-1828] 003470 20.2.41.64\n[BBOX-1829] 003470 20.2.41.64\n[BBOX-1830] 003470 20.2.41.64\n[BBOX-1831] 003470 20.2.41.64\n[BBOX-1832] 003470 20.2.41.64\n[BBOX-1833] 003470 20.2.41.64\n[BBOX-1834] 003470 20.2.41.64\n[BBOX-1835] 003470 20.2.41.64\n[BBOX-1836] 003470 20.2.41.64\n[BBOX-1837] 003470 20.2.41.64\n[BBOX-1838] 003470 20.2.41.64\n[BBOX-1839] 003470 20.2.41.64\n[BBOX-1840] 003470 20.2.41.64\n[BBOX-1841] 003470 20.2.41.64\n[BBOX-1842] 003470 20.2.41.64\n[BBOX-1843] 003470 20.2.41.64\n[BBOX-1844] 003470 20.2.41.64\n[BBOX-1845] 003470 20.2.41.64\n[BBOX-1846] 003470 20.2.41.64\n[BBOX-1847] 003470 20.2.41.64\n[BBOX-1848] 003470 20.2.41.64\n[BBOX-1849] 003470 20.2.41.64\n[BBOX-1850] 003470 20.2.41.64\n[BBOX-1851] 003470 20.2.41.64\n[BBOX-1852] 003470 20.2.41.64\n[BBOX-1853] 003470 20.2.41.64\n[BBOX-1854] 003470 20.2.41.64\n[BBOX-1855] 003470 20.2.41.64\n[BBOX-1856] 003470 20.2.41.64\n[BBOX-1857] 003470 20.2.41.64\n[BBOX-1858] 003470 20.2.41.64\n[BBOX-1859] 003470 20.2.41.64\n[BBOX-1860] 003470 20.2.41.64\n[BBOX-1861] 003470 20.2.41.64\n[BBOX-1862] 003470 20.2.41.64\n[BBOX-1863] 003470 20.2.41.64\n[BBOX-1864] 003470 20.2.41.64\n[BBOX-1865] 003470 20.2.41.64\n[BBOX-1866] 003470 20.2.41.64\n[BBOX-1867] 003470 20.2.41.64\n[BBOX-1868] 003470 20.2.41.64\n[BBOX-1869] 003470 20.2.41.64\n[BBOX-1870] 003470 20.2.41.64\n[BBOX-1871] 003470 20.2.41.64\n[BBOX-1872] 003470 20.2.41.64\n[BBOX-1873] 003470 20.2.41.64\n[BBOX-1874] 003470 20.2.41.64\n[BBOX-1875] 003470 20.2.41.64\n[BBOX-1876] 003470 20.2.41.64\n[BBOX-1877] 003470 20.2.41.64\n[BBOX-1878] 003470 20.2.41.64\n[BBOX-1879] 003470 20.2.41.64\n[BBOX-1880] 003470 20.2.41.64\n[BBOX-1881] 003470 20.2.41.64\n[BBOX-1882] 003470 20.2.41.64\n[BBOX-1883] 003470 20.2.41.64\n[BBOX-1884] 003470 20.2.41.64\n[BBOX-1885] 003470 20.2.41.64\n[BBOX-1886] 003470 20.2.41.64\n[BBOX-1887] 003470 20.2.41.64\n[BBOX-1888] 003470 20.2.41.64\n[BBOX-1889] 003470 20.2.41.64\n[BBOX-1890] 003470 20.2.41.64\n[BBOX-1891] 003470 20.2.41.64\n[BBOX-1892] 003470 20.2.41.64\n[BBOX-1893] 003470 20.2.41.64\n[BBOX-1894] 003470 20.2.41.64\n[BBOX-1895] 003470 20.2.41.64\n[BBOX-1896] 003470 20.2.41.64\n[BBOX-1897] 003470 20.2.41.64\n[BBOX-1898] 003470 20.2.41.64\n[BBOX-1899] 003470 20.2.41.64\n[BBOX-1900] 003470 20.2.41.64\n[BBOX-1901] 003470 20.2.41.64\n[BBOX-1902] 003470 20.2.41.64\n[BBOX-1903] 003470 20.2.41.64\n[BBOX-1904] 003470 20.2.41.64\n[BBOX-1905] 003470 20.2.41.64\n[BBOX-1906] 003470 20.2.41.64\n[BBOX-1907] 003470 20.2.41.64\n[BBOX-1908] 003470 20.2.41.64\n[BBOX-1909] 003470 20.2.41.64\n[BBOX-1910] 003470 20.2.41.64\n[BBOX-1911] 003470 20.2.41.64\n[BBOX-1912] 003470 20.2.41.64\n[BBOX-1913] 003470 20.2.41.64\n[BBOX-1914] 003470 20.2.41.64\n[BBOX-1915] 003470 20.2.41.64\n[BBOX-1916] 003470 20.2.41.64\n[BBOX-1917] 003470 20.2.41.64\n[BBOX-1918] 003470 20.2.41.64\n[BBOX-1919] 003470 20.2.41.64\n[BBOX-1920] 003470 20.2.41.64\n[BBOX-1921] 003470 20.2.41.64\n[BBOX-1922] 003470 20.2.41.64\n[BBOX-1923] 003470 20.2.41.64\n[BBOX-1924] 003470 20.2.41.64\n[BBOX-1925] 003470 20.2.41.64\n[BBOX-1926] 003470 20.2.41.64\n[BBOX-1927] 003470 20.2.41.64\n[BBOX-1928] 003470 20.2.41.64\n[BBOX-1929] 003470 20.2.41.64\n[BBOX-1930] 003470 20.2.41.64\n[BBOX-1931] 003470 20.2.41.64\n[BBOX-1932] 003\n[BBOX-1933] 影像检查报告单\n[BBOX-1934] 病人 ID:\n[BBOX-1935] 姓名:\n[BBOX-1936] 性别: 男\n[BBOX-1937] 年龄: 67岁\n[BBOX-1938] 申请科室: 老年医学呼吸内科\n[BBOX-1939] 机器型号: SE-MR4\n[BBOX-1940] 住院号\n[BBOX-1941] 检查部位: 颅脑颅脑MR平扫及增强+DWI,*钆特酸葡胺注射液【广西HR】\n[BBOX-1942] 检查日期: 2026-03-13\n[BBOX-1943] (此报告仅供临床医师诊断参考,不作为疾病证明)\n[BBOX-1944] 检查所见:\n[BBOX-1945] 左侧基底节区、两侧放射冠、右侧侧脑室前后角旁见小斑片状、斑点状等T1、稍\n[BBOX-1946] 长T2信号灶,FLAIR呈高信号,边界欠清,DWI未见弥散受限;余脑实质信号未见异\n[BBOX-1947] 常,DWI未见明确弥散受限区,增强扫描未见异常强化灶;静脉窦强化充盈良好,未\n[BBOX-1948] 见异常;各脑室及脑沟、裂、池对称性轻度增宽;中线结构无移位。\n[BBOX-1949] 诊断意见:\n[BBOX-1950] 脑白质病变--改良Fasekas1级;轻度脑萎缩。\n[BBOX-1951] 检查技师: 唐成\n[BBOX-1952] 报告医师: 郭仟\n[BBOX-1953] 审核医师: 张\n[BBOX-1954] 报告日期: 2026-03-16 15:13:19\n[BBOX-1955] 审核日期: 2026-03-16 18:28:39\n[BBOX-1956] 地址: 广西医科大学第一附属医院放射科\n[BBOX-1957] 联系电话: 0771-5356934\n[BBOX-1958] “广西HR”解释: 广西影像检查项目互认\n[BBOX-1959] 科\n[BBOX-1960] 检查部位：全身骨显像 显像剂：99mTc-MDP 临床诊断：1.肺占位性病变,2.细菌性肺炎,3.肺\n[BBOX-1961] 剂量：25mCi 部阴影\n[BBOX-1962] （此报告仅供临床医师诊断参考，不作为疾病证明）\n[BBOX-1963] 检查所见：\n[BBOX-1964] 静脉注射99mTc-MDP 3小时后行全身骨显像前位、后位各1帧：\n[BBOX-1965] 全身骨像完整、显影基本清晰。颅骨、胸骨、椎体、肩胛骨、肋骨、骨盆及四肢骨显像剂分\n[BBOX-1966] 布未见明显异常改变。\n[BBOX-1967] 双肾显影，膀胱部分充盈。\n[BBOX-1968] 诊断意见：\n[BBOX-1969] 全身骨显像未见明显异常改变。\n[BBOX-1970] 报告医师：巫殷豪\n[BBOX-1971] 审核医师：彭盛梅\n[BBOX-1972] 报告日期：2026-03-10\n[BBOX-1973] 广西医科大学第一附属医院\n[BBOX-1974] 影像检查报告单\n[BBOX-1975] 病人ID:\n[BBOX-1976] 姓名:\n[BBOX-1977] 性别: 男\n[BBOX-1978] 年龄: 67岁\n[BBOX-1979] 申请科室:\n[BBOX-1980] 机器型号: SE-\n[BBOX-1981] 床号: 49床\n[BBOX-1982] 住院号: 1959\n[BBOX-1983] Force-2\n[BBOX-1984] 检查部位: 下腹部,上腹部CT平扫+增强,(新)碘帕醇注射液\n[BBOX-1985] 【广西HR】\n[BBOX-1986] 检查日期: 2026-03-11\n[BBOX-1987] (此报告仅供临床医师诊断参考,不作为疾病证明)\n[BBOX-1988] 检查所见:\n[BBOX-1989] 双侧肾上腺见多个结节状稍低/低密度影,较大者大小约1.6cm×1.2cm,增强扫\n[BBOX-1990] 描不均匀强化。肝脏各叶比例正常,肝实质内见多发类圆形低密度无强化灶,较大者\n[BBOX-1991] 位于S8,大小约1.2cm×1.1cm;余肝实质未见异常密度影及异常强化灶。肝内、外胆\n[BBOX-1992] 管未见扩张,胆囊不大,囊壁均匀,囊内密度未见异常。脾脏、胰腺形态、大小、密\n[BBOX-1993] 度未见异常,增强扫描未见异常强化,右肾体积缩小,双肾实质内见多个类圆形低密\n[BBOX-1994] 度无强化灶,较大者大小约0.9cm×1.5cm;双侧肾盂肾盏及输尿管未见扩张。腹部肠\n[BBOX-1995] 管分布正常,管腔未见扩张、积液,腹腔内未见明确肿块影;肝门及腹主动脉旁未见\n[BBOX-1996] 增大淋巴结,腹膜腔未见积液。\n[BBOX-1997] 诊断意见:\n[BBOX-1998] 1.双侧肾上腺占位,考虑转移瘤可能性大,请结合临床;\n[BBOX-1999] 2.肝多发囊肿;\n[BBOX-2000] 3.右肾萎缩,双肾囊肿。\n[BBOX-2001] 检查技师:刘辰民\n[BBOX-2002] 报告医师:谢金桓\n[BBOX-2003] 审核医师: 冯涛\n[BBOX-2004] 报告日期:2026-03-11 14:21:30\n[BBOX-2005] 审核日期:2026-03-11 16:15:45\n[BBOX-2006] 地址:广西医科大学第一附属医院放射科\n[BBOX-2007] 联系电话:0771-5356934\n[BBOX-2008] “广西HR”解释:广西影像检查项目互认\n[BBOX-2009] 广西医科大学第一附属医院\n[BBOX-2010] 影像检查报告单\n[BBOX-2011] 病人ID:\n[BBOX-2012] 姓名:\n[BBOX-2013] 男\n[BBOX-2014] 年龄: 67岁\n[BBOX-2015] 申请科室: 老年医学呼吸内科\n[BBOX-2016] 机器型号: SE-\n[BBOX-2017] Force-2\n[BBOX-2018] 床号\n[BBOX-2019] 号\n[BBOX-2020] 检查部位: 胸部CT平扫+增强,*碘海醇注射液【广西HR】\n[BBOX-2021] 检查日期: 2026-03-02\n[BBOX-2022] (此报告仅供临床医师诊断参考,不作为疾病证明)\n[BBOX-2023] 检查所见:\n[BBOX-2024] 两肺尖胸膜下见类圆形透亮影,较大者长径约0.8cm;右肺下叶基底段(Se4:IM144)见团\n[BBOX-2025] 块状密度增高灶,大小约为7.7cm×5.1cm×6.9cm,增强扫描中度强化;两肺可见多发实性结节\n[BBOX-2026] 影,较大位于右肺下叶外基底段(Se4:IM344),内可见空泡,长径约为1.1cm,增强扫描似见\n[BBOX-2027] 血管穿行。右肺中叶、左肺上叶下舌段及两肺下叶见条索状密度增高影;余肺叶内未见异常密\n[BBOX-2028] 度影及异常强化灶,右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张,两肺部分支气管\n[BBOX-2029] 管壁增厚,管腔变窄,气管、其余支气管通畅;肺门、纵隔结构清楚,纵隔、两侧肺门见多发\n[BBOX-2030] 淋巴结,大者短径约1.1cm。两侧胸膜增厚、钙化,胸膜腔未见积液。主动脉、冠状动脉见斑片\n[BBOX-2031] 状钙化灶。\n[BBOX-2032] 诊断意见:\n[BBOX-2033] 1.右肺下叶后基底段软组织肿块,肿瘤性病变?感染性病变?请结合临床及实验室检查;\n[BBOX-2034] 2.两肺多发实性结节,建议短期复查;\n[BBOX-2035] 3.右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张并两肺炎症;\n[BBOX-2036] 4.两肺上叶间隔旁型肺气肿;\n[BBOX-2037] 5.纵隔、两侧肺门淋巴结,建议复查;\n[BBOX-2038] 6.两侧胸膜肥厚、钙化;\n[BBOX-2039] 7.主动脉、冠状动脉硬化。\n[BBOX-2040] 检查技师:周春燚 报告医师:肖芳艳 审核医师:\n[BBOX-2041] 报告日期:2026-03-03 18:39:05 审核日期:2026-03-04 09:21:01\n[BBOX-2042] 地址:广西医科大学第一附属医院放射科 联系电话:0771-5356934 “广西HR”解码:广西影像检查项目互认\n[BBOX-2043] 测量参数值:\n[BBOX-2044] 测量项目\n[BBOX-2045] 结果\n[BBOX-2046] 单位\n[BBOX-2047] 参考范围\n[BBOX-2048] 测量项目\n[BBOX-2049] 结果\n[BBOX-2050] 单位\n[BBOX-2051] 参考范围\n[BBOX-2052] 主动脉根部内径:\n[BBOX-2053] 27\n[BBOX-2054] mm\n[BBOX-2055] (20-35)\n[BBOX-2056] 左房前后径:\n[BBOX-2057] 35\n[BBOX-2058] mm\n[BBOX-2059] (24-39)\n[BBOX-2060] 左室舒末前后径:\n[BBOX-2061] 53\n[BBOX-2062] mm\n[BBOX-2063] (38-54)\n[BBOX-2064] 左室缩末前后径:\n[BBOX-2065] 32\n[BBOX-2066] mm\n[BBOX-2067] (24-37)\n[BBOX-2068] 室间隔舒末厚:\n[BBOX-2069] 10\n[BBOX-2070] mm\n[BBOX-2071] (6-11)\n[BBOX-2072] 左室后壁舒末厚:\n[BBOX-2073] 10\n[BBOX-2074] mm\n[BBOX-2075] (6-11)\n[BBOX-2076] 右室舒末前后径:\n[BBOX-2077] 18\n[BBOX-2078] mm\n[BBOX-2079] (15-30)\n[BBOX-2080] 右室流出道:\n[BBOX-2081] 27\n[BBOX-2082] mm\n[BBOX-2083] (15-32)\n[BBOX-2084] 主肺动脉内径:\n[BBOX-2085] 22\n[BBOX-2086] mm\n[BBOX-2087] (15-26)\n[BBOX-2088] E/A\n[BBOX-2089] <1\n[BBOX-2090] (\n[BBOX-2091] 0.8-2.0)\n[BBOX-2092] e'/a'\n[BBOX-2093] <1\n[BBOX-2094] (-)\n[BBOX-2095] E/e'\n[BBOX-2096] 11.7\n[BBOX-2097] (-)\n[BBOX-2098] 超声描述:\n[BBOX-2099] 描述:\n[BBOX-2100] 1、按比例各房室大小正常，房、室间隔连续完整，室间隔与左室壁厚度正常，静息状态下室壁收\n[BBOX-2101] 缩运动有力，未见节段性运动异常。左室收缩功能测定在正常范围，FS:40%，EF:70%，SV:95ml/B\n[BBOX-2102] ，CO:6.4L/min，EDV:135ml，心包腔内未探及液性区声像。\n[BBOX-2103] 2、三尖瓣形态结构正常，瓣口轻度反流，速度2.4m/s，压差22mmHg，瞬时反流量约2ml（无血流动\n[BBOX-2104] 力学意义），余各瓣膜形态结构正常，启闭运动好，二尖瓣血流图示E峰小于A峰。\n[BBOX-2105] 3、主动脉根部内径正常，升主动脉内径正常，管壁增厚，弹性降低，主肺动脉内径正常，内回声\n[BBOX-2106] 及血流信号未见异常。\n[BBOX-2107] 超声诊断:\n[BBOX-2108] 1、心脏形态结构及瓣膜功能大致正常。\n[BBOX-2109] 2、左室舒张功能降低，收缩功能测定在正常范围，\n[BBOX-2110] 诊断医师：吴颖/肖彩意\n[BBOX-2111] 报告日期：2026-03-02 10:12:46\n[BBOX-2112] \\begin{tabular}{ccccccccc}\n[BBOX-2113] 报告时间: 2026-02-28\n[BBOX-2114] \\hline\n[BBOX-2115] 缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\\\\n[BBOX-2116] \\hline\n[BBOX-2117] TB-DNA & 结核杆菌DNA* & $<$5.00E+02 & & & & 拷贝 & $<$5.00E+02 & $<$5.00E+02 \\\\\n[BBOX-2118] \\hline\n[BBOX-2119] \\end{tabular}\n[BBOX-2120] \\begin{tabular}{ccccccccc}\n[BBOX-2121] 报告时间: 2026-02-28\n[BBOX-2122] \\hline\n[BBOX-2123] 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\\\\n[BBOX-2124] \\hline\n[BBOX-2125] 乙型肝炎表面抗原* & 0.00 & & & & IU/ml & 0-0.08 & \\\\\n[BBOX-2126] 乙型肝炎表面抗体* & 14.85 & & $\\uparrow$ & & mIU/mL & 0-10 & \\\\\n[BBOX-2127] 乙型肝炎e抗原* & 0.00 & & & & PElu/ml & 0-0.10 & \\\\\n[BBOX-2128] 乙型肝炎e抗体* & 0.14 & & & & IU/mL & 0-0.20 & \\\\\n[BBOX-2129] 乙型肝炎核心抗体* & 0.27 & & & & IU/mL & 0-0.50 & \\\\\n[BBOX-2130] \\hline\n[BBOX-2131] \\end{tabular}\n[BBOX-2132] \\begin{tabular}{llcccllcc}\n[BBOX-2133] 报告时间: 2026-02-28\n[BBOX-2134] \\hline\n[BBOX-2135] & & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\\\\n[BBOX-2136] \\hline\n[BBOX-2137] & / & 丙型肝炎抗体定量* & 0.06 & & & & COI & 0-1 & \\\\\n[BBOX-2138] & ST & 不加热血清反应素试验* & 阴性(-) & & & & & 阴性(-) & \\\\\n[BBOX-2139] & V & 人免疫缺陷病毒抗体定量* & 0.08 & & & & COI & 0-1 & \\\\\n[BBOX-2140] & PA & 梅毒螺旋体抗体定量* & 0.08 & & & & COI & 0-1 & \\\\\n[BBOX-2141] \\hline\n[BBOX-2142] \\end{tabular}\n[BBOX-2143] \\begin{tabular}{ccccccccc}\n[BBOX-2144] 报告时间: 2026-02-28\n[BBOX-2145] \\hline\n[BBOX-2146] 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\\\\n[BBOX-2147] \\hline\n[BBOX-2148] 糖化血红蛋白HbA1c* & 6.40 & & $\\uparrow$ & & \\% & 4.0-6.0 & \\\\\n[BBOX-2149] 糖化血红蛋白HbA1a & 0.50 & & & & \\% & 0-0.91 & \\\\\n[BBOX-2150] 糖化血红蛋白HbA1b & 1.10 & & & & \\% & 0.35-1.82 & \\\\\n[BBOX-2151] \\hline\n[BBOX-2152] \\end{tabular}\n[BBOX-2153] \\begin{tabular}{l c c c c c c c}\n[BBOX-2154] 报告时间: 2026-02-28\n[BBOX-2155] \\hline\n[BBOX-2156] 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历 \\\\\n[BBOX-2157] \\hline\n[BBOX-2158] 凝血酶原时间* & 11.50 & & & & S & 9-15 & \\\\\n[BBOX-2159] 国际标准化比值* & 1.04 & & & & & 0.8-1.4 & \\\\\n[BBOX-2160] 纤维蛋白原* & 4.43 & & & & g/L & 2.00 -5.00 & \\\\\n[BBOX-2161] 活化部分凝血活酶时间* & 32.30 & & & & S & 23.00 -40.00 & \\\\\n[BBOX-2162] 凝血酶时间* & 13.00 & & & & S & 10.3-16.6 & \\\\\n[BBOX-2163] 凝血酶原活动度 & 98 & & & & \\% & 70-130 & \\\\\n[BBOX-2164] D-二聚体定量* & 69 & & & & ng/ml & 0-450 & \\\\\n[BBOX-2165] \\hline\n[BBOX-2166] \\end{tabular}\n[BBOX-2167] \\begin{tabular}{ccccccccc}\n[BBOX-2168] 报告时间: 2026-02-02\n[BBOX-2169] \\hline\n[BBOX-2170] 缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & \\\\\n[BBOX-2171] \\hline\n[BBOX-2172] TBIL & 总胆红素* & 8.7 & & & & \\textmu mol/L & 0-26.0 & \\\\\n[BBOX-2173] DBIL & 直接胆红素* & 3.6 & & & & \\textmu mol/L & 0-6.8 & \\\\\n[BBOX-2174] IBIL & 间接胆红素 & 5.1 & & & & \\textmu mol/L & 3.1-14.3 & \\\\\n[BBOX-2175] DB/TB & 直/总胆比值 & 0.41 & & & & & & \\\\\n[BBOX-2176] TP & 总蛋白\\# & 74.5 & & & & g/L & 65-85 & \\\\\n[BBOX-2177] ALB & 白蛋白* & 39.3 & & \\downarrow & & g/L & 40-55 & \\\\\n[BBOX-2178] GLO & 球蛋白 & 35.2 & & & & g/L & 20-40 & \\\\\n[BBOX-2179] A/G & 白蛋白/球蛋白 & 1.1 & & \\downarrow & & & 1.2-2.4 & \\\\\n[BBOX-2180] GGT & 谷氨酰转肽酶* & 30 & & & & U/L & 10-60 & \\\\\n[BBOX-2181] TBA & 总胆汁酸* & 13.2 & & \\uparrow & & \\textmu mol/L & 0-10 & \\\\\n[BBOX-2182] AST & 天门冬氨酸氨基转移酶* & 15 & & & & U/L & 15-40 & \\\\\n[BBOX-2183] ALT & 丙氨酸氨基转移酶* & 14 & & & & U/L & 9-50 & \\\\\n[BBOX-2184] AST/ALT & 谷草/谷丙比值 & 1.1 & & & & & & \\\\\n[BBOX-2185] ALP & 碱性磷酸酶* & 64 & & & & U/L & 45-125 & \\\\\n[BBOX-2186] PA & 前白蛋白* & 251.5 & & & & mg/L & 200-430 & \\\\\n[BBOX-2187] CHE & 胆碱酯酶* & 8382 & & & & U/L & 5000-12000 & \\\\\n[BBOX-2188] UREA & 尿素* & 6.98 & & & & mmol/L & 3.6-9.5 & \\\\\n[BBOX-2189] CREA & 肌酐* & 136 & & \\uparrow & & \\textmu mol/L & 57-111 & \\\\\n[BBOX-2190] UA & 尿酸* & 551 & & \\uparrow & & \\textmu mol/L & 208-428 & \\\\\n[BBOX-2191] HCO3 & 碳酸氢根* & 21.6 & & \\downarrow & & mmol/L & 22-29 & \\\\\n[BBOX-2192] T-CHO & 总胆固醇* & 3.10 & & & & mmol/L & 3.1-5.7 & \\\\\n[BBOX-2193] \\hline\n[BBOX-2194] \\end{tabular}\n[BBOX-2195] \\begin{tabular}{ccccccccc}\n[BBOX-2196] 报告时间: 2025-04-01\n[BBOX-2197] \\hline\n[BBOX-2198] 缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & \\\\\n[BBOX-2199] \\hline\n[BBOX-2200] CHE & 胆碱酯酶* & 8382 & & & & U/L & 5000-12000 & \\\\\n[BBOX-2201] UREA & 尿素* & 6.98 & & & & mmol/L & 3.6-9.5 & \\\\\n[BBOX-2202] CREA & 肌酐* & 136 & & $\\uparrow$ & & $\\mu$mol/L & 57-111 & \\\\\n[BBOX-2203] UA & 尿酸* & 551 & & $\\uparrow$ & & $\\mu$mol/L & 208-428 & \\\\\n[BBOX-2204] HCO3 & 碳酸氢根* & 21.6 & & $\\downarrow$ & & mmol/L & 22-29 & \\\\\n[BBOX-2205] T-CHO & 总胆固醇* & 3.18 & & & & mmol/L & $<$5.2 & \\\\\n[BBOX-2206] TG & 甘油三酯* & 1.27 & & & & mmol/L & $<$1.7 & \\\\\n[BBOX-2207] LDL-C & 低密度脂蛋白胆固醇* & 1.78 & & & & mmol/L & $<$3.4(低危人群) & \\\\\n[BBOX-2208] GLU & 空腹血葡萄糖* & 4.79 & & & & mmol/L & 3.9-6.1 & \\\\\n[BBOX-2209] K & 钾* & 4.18 & & & & mmol/L & 3.5-5.3 & \\\\\n[BBOX-2210] Na & 钠* & 141.1 & & & & mmol/L & 137-147 & \\\\\n[BBOX-2211] CL & 氯* & 106.4 & & & & mmol/L & 99-110 & \\\\\n[BBOX-2212] Ca & 总钙* & 2.25 & & & & mmol/L & 2.11-2.52 & \\\\\n[BBOX-2213] Mg & 镁* & 0.78 & & & & mmol/L & 0.75-1.02 & \\\\\n[BBOX-2214] P & 磷* & 0.95 & & & & mmol/L & 0.85-1.51 & \\\\\n[BBOX-2215] CK & 肌酸激酶* & 84 & & & & U/L & 50-310 & \\\\\n[BBOX-2216] CK-MB & 肌酸激酶同工酶MB & 13 & & & & U/L & 0-25 & \\\\\n[BBOX-2217] LD & 乳酸脱氢酶* & 167 & & & & U/L & 120-250 & \\\\\n[BBOX-2218] $\\alpha$-HBD & $\\alpha$-羟丁酸脱氢酶* & 109 & & & & U/L & 72-182 & \\\\\n[BBOX-2219] IgE & 免疫球蛋白E* & 1960.6 & & $\\uparrow$ & & IU/ml & $<$100 & \\\\\n[BBOX-2220] \\hline\n[BBOX-2221] \\end{tabular}\n[BBOX-2222] \\begin{tabular}{ccccccccc}\n[BBOX-2223] \\hline\n[BBOX-2224] 缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 \\\\\n[BBOX-2225] \\hline\n[BBOX-2226] WBC & 白细胞计数* & 8.490 & & & & 10~9/L & 3.5-9.5 \\\\\n[BBOX-2227] RBC & 红细胞计数* & 5.81 & & $\\uparrow$ & & 10~12/L & 4.3-5.8 \\\\\n[BBOX-2228] HGB & 血红蛋白* & 157.00 & & & & g/L & 130-175 \\\\\n[BBOX-2229] PLT & 血小板计数* & 268.00 & & & & 10~9/L & 125-350 \\\\\n[BBOX-2230] NEU\\% & 中性粒细胞百分比 & 0.6920 & & & & & 0.4-0.75 \\\\\n[BBOX-2231] LYM\\% & 淋巴细胞百分比 & 0.1970 & & $\\downarrow$ & & & 0.2-0.5 \\\\\n[BBOX-2232] MONO\\% & 单核细胞百分比 & 0.0630 & & & & & 0.03-0.1 \\\\\n[BBOX-2233] EO\\% & 嗜酸性粒细胞百分比 & 0.0450 & & & & & 0.004-0.08 \\\\\n[BBOX-2234] BA SO\\% & 嗜碱性粒细胞百分比 & 0.0030 & & & & & 0-0.01 \\\\\n[BBOX-2235] NEU & 中性粒细胞绝对值 & 5.88 & & & & 10~9/L & 1.8-6.3 \\\\\n[BBOX-2236] LYM & 淋巴细胞绝对值 & 1.67 & & & & 10~9/L & 1.1-3.2 \\\\\n[BBOX-2237] MONO & 单核细胞绝对值 & 0.53 & & & & 10~9/L & 0.1-0.6 \\\\\n[BBOX-2238] EOS & 嗜酸性粒细胞绝对值 & 0.38 & & & & 10~9/L & 0.02-0.52 \\\\\n[BBOX-2239] BA SO & 嗜碱性粒细胞绝对值 & 0.03 & & & & 10~9/L & 0-0.06 \\\\\n[BBOX-2240] MCV & 平均红细胞体积* & 83.70 & & & & fl & 82-100 \\\\\n[BBOX-2241] MCH & 平均RBC血红蛋白含量* & 26.90 & & $\\downarrow$ & & pg & 27-34 \\\\\n[BBOX-2242] MCHC & 平均RBC血红蛋白浓度* & 323.00 & & & & g/L & 316-354 \\\\\n[BBOX-2243] HCT & 红细胞比容* & 0.486 & & & & & 0.4-0.5 \\\\\n[BBOX-2244] RDWCV & RBC体积分布宽度CV & 0.15 & & $\\uparrow$ & & & 0.11-0.14 \\\\\n[BBOX-2245] PDW & 血小板体积分布宽度 & 0.16 & & & & & 0.15-0.18 \\\\\n[BBOX-2246] \\hline\n[BBOX-2247] \\end{tabular}\n[BBOX-2248] \\begin{tabular}{ccccccccc}\n[BBOX-2249] \\hline\n[BBOX-2250] \\multicolumn{1}{c}{\\textbf{缩写}} & \\multicolumn{1}{c}{\\textbf{项目名称}} & \\multicolumn{1}{c}{\\textbf{结果}} & \\multicolumn{1}{c}{\\textbf{结果提示}} & \\multicolumn{1}{c}{\\textbf{异常提示}} & \\multicolumn{1}{c}{\\textbf{辅助诊断}} & \\multicolumn{1}{c}{\\textbf{单位}} & \\multicolumn{1}{c}{\\textbf{参考范围}} \\\\\n[BBOX-2251] \\hline\n[BBOX-2252] FI02 & 吸氧浓度 & 21.00 & & & & \\% & 21-100 \\\\\n[BBOX-2253] T & 体温 & 36.4 & & & & & 29-41 \\\\\n[BBOX-2254] Ca++ & 钙测定 & 1.19 & & & & mmol/L & 1.15-1.29 \\\\\n[BBOX-2255] Na+ & 钠测定 & 143.20 & & & & mmol/L & 136-146 \\\\\n[BBOX-2256] K+ & 钾测定 & 3.98 & & & & mmol/L & 3.5-4.5 \\\\\n[BBOX-2257] p02(a,T)/F02 & 氧合指数(p/f) & 315.0 & & $\\downarrow$ & & & 400-500 \\\\\n[BBOX-2258] BEecf & 红细胞外剩余碱 & -1.80 & & & & mmol/l & -3-3 \\\\\n[BBOX-2259] PH & 酸碱度 (PH) & 7.383 & & & & & 7.35-7.45 \\\\\n[BBOX-2260] pH(T) & pH校正值(pHT) & 7.392 & & & & & 7.35-7.45 \\\\\n[BBOX-2261] pO2 & 氧分压 (pO2) & 66.20 & & $\\downarrow$ & & mmHg & 83-108 \\\\\n[BBOX-2262] pO2(T) & 氧分压校正值 & 63.50 & & $\\downarrow$ & & mmHg & 83-108 \\\\\n[BBOX-2263] pCO2 & 二氧化碳分压 & 39.90 & & & & mmHg & 35-45 \\\\\n[BBOX-2264] PCO2(T) & CO2分压校正 & 38.90 & & & & mmHg & 35-45 \\\\\n[BBOX-2265] Cl- & 氯测定 & 102.00 & & & & mmol/L & 98-106 \\\\\n[BBOX-2266] Hb & 血红蛋白测定(Hb) & 162.00 & & $\\uparrow$ & & g/L & 120-160 \\\\\n[BBOX-2267] F02Hb & 氧合血红蛋白 & 92.0 & & $\\downarrow$ & & \\% & 94-98 \\\\\n[BBOX-2268] MetHb & 高铁血红蛋白 & 0.10 & & & & & \\\\\n[BBOX-2269] s02 & 总血氧饱和度 & 92.9 & & $\\downarrow$ & & \\% & 93-98 \\\\\n[BBOX-2270] COHb & CO红蛋白 & 1.00 & & & & \\% & 0-2 \\\\\n[BBOX-2271] ctCO2 & 血CO2含量 & 24.50 & & & & mmol/L & 24-32 \\\\\n[BBOX-2272] FHHB & 还原血红蛋白 & 6.9 & & & & & \\\\\n[BBOX-2273] \\hline\n[BBOX-2274] \\end{tabular}\n[BBOX-2275] \\begin{tabular}{ccccccccc}\n[BBOX-2276] \\hline\n[BBOX-2277] 缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 \\\\\n[BBOX-2278] \\hline\n[BBOX-2279] PH & 酸碱度 (PH) & 7.383 & & & & & 7.35-7.45 \\\\\n[BBOX-2280] pH(T) & pH校正值(pHT) & 7.392 & & & & & 7.35-7.45 \\\\\n[BBOX-2281] pO2 & 氧分压 (pO2) & 66.20 & & $\\downarrow$ & & mmHg & 83-108 \\\\\n[BBOX-2282] pO2(T) & 氧分压校正值 & 63.50 & & $\\downarrow$ & & mmHg & 83-108 \\\\\n[BBOX-2283] pCO2 & 二氧化碳分压 & 39.90 & & & & mmHg & 35-45 \\\\\n[BBOX-2284] PCO2(T) & CO2分压校正 & 38.90 & & & & mmHg & 35-45 \\\\\n[BBOX-2285] Cl- & 氯测定 & 102.00 & & & & mmol/L & 98-106 \\\\\n[BBOX-2286] Hb & 血红蛋白测定(Hb) & 162.00 & & $\\uparrow$ & & g/L & 120-160 \\\\\n[BBOX-2287] F02Hb & 氧合血红蛋白 & 92.0 & & $\\downarrow$ & & \\% & 94-98 \\\\\n[BBOX-2288] MetHb & 高铁血红蛋白 & 0.10 & & & & & \\\\\n[BBOX-2289] s02 & 总血氧饱和度 & 92.9 & & $\\downarrow$ & & \\% & 93-98 \\\\\n[BBOX-2290] C0Hb & CO红蛋白 & 1.00 & & & & \\% & 0-2 \\\\\n[BBOX-2291] ctCO2 & 血CO2含量 & 24.50 & & & & mmol/L & 24-32 \\\\\n[BBOX-2292] FHHB & 还原血红蛋白 & 6.9 & & & & \\% & 2-7 \\\\\n[BBOX-2293] cHCO3 & 标准碳酸氢根 & 23.00 & & & & mmol/L & 22-26 \\\\\n[BBOX-2294] ABE (BE(B)) & 实际剩余碱 & -1.6 & & & & mmol/L & -3-3 \\\\\n[BBOX-2295] HCO3- & 实际碳酸氢根 & 23.20 & & & & mmol/L & \\\\\n[BBOX-2296] P02(A-a,T)e & 肺泡动脉氧分压差 & 36.0 & & $\\uparrow$ & & mmHg & 10-25 \\\\\n[BBOX-2297] P02(a/A,T) & 动脉与肺泡氧分压比 & 64.0 & & $\\downarrow$ & & \\% & 85-95 \\\\\n[BBOX-2298] RI & 呼吸指数 & 57.0 & & & & & \\\\\n[BBOX-2299] Glu & 葡萄糖测定 & 6.70 & & $\\uparrow$ & & & \\\\\n[BBOX-2300] \\hline\n[BBOX-2301] \\end{tabular}\n[BBOX-2302] 临床诊断：肺癌\n[BBOX-2303] 样本采集时间：2026-03-10\n[BBOX-2304] 检测项目\n[BBOX-2305] 本产品对与肺癌密切相关的68个基因进行高通量测序。检测突变形式为点突变(SNV)、小片段插入缺失(INDEL)、拷贝数变异(CNV)以及融合(FUSION)。通过免疫组化检测PD-L1表达。\n[BBOX-2306] 本报告分析基因变异与靶向药物、化疗药物的相关性，给出靶向药物(FDA/NMPA批准药物、临床试验\n[BBOX-2307] 药物等)、化疗药物的用药提示信息，从而为临床制定治疗方案提供参考信息。\n[BBOX-2308] 注：检测基因列表见附录。\n[BBOX-2309] 检测结果小结\n[BBOX-2310] 检测类型\n[BBOX-2311] 检测结果\n[BBOX-2312] 靶向用药指导\n[BBOX-2313] 共检出3个变异位点,其中3个与靶向药物相关(KRAS\n[BBOX-2314] p.G12V; CDKN2A p.R80*; TP53 p.G279E)\n[BBOX-2315] PD-L1蛋白表达水平\n[BBOX-2316] 使用CSTE1L3N抗体; TPS:<1%, CPS:1\n[BBOX-2317] 化疗药物检测\n[BBOX-2318] 详见“化疗药物检测解析”部分\n[BBOX-2319] 样品总体质量评估\n[BBOX-2320] 合格\n[BBOX-2321] 注:\n[BBOX-2322] 1. 本报告为基因检测结果,基因、药物等信息列举未按照重要性排序。\n[BBOX-2323] 2. 本报告只对本次采集样本负责,如有疑问,请在7个工作日内与我们联系。\n[BBOX-2324] 检测人:\n[BBOX-2325] 张紫叶\n[BBOX-2326] 复核人:\n[BBOX-2327] 王建丽\n[BBOX-2328] 日期:\n[BBOX-2329] 2026-03-16\n[BBOX-2330] 日期:\n[BBOX-2331] 2026-03-16\n[BBOX-2332] 1/26\n[BBOX-2333] 孔令祈 Novogene\n[BBOX-2334] 诺禾致源\n[BBOX-2335] 肺癌精准诊疗相关基因结果汇总\n[BBOX-2336] 基因\n[BBOX-2337] 变异类型\n[BBOX-2338] 检测结果\n[BBOX-2339] 变异丰度/拷贝数\n[BBOX-2340] ALK\n[BBOX-2341] 突变/融合\n[BBOX-2342] 未检测到与用药相关突变\n[BBOX-2343] BRAF\n[BBOX-2344] 突变/融合\n[BBOX-2345] 未检测到与用药相关突变\n[BBOX-2346] BRCA1\n[BBOX-2347] 突变/缺失\n[BBOX-2348] 未检测到与用药相关突变\n[BBOX-2349] BRCA2\n[BBOX-2350] 突变/缺失\n[BBOX-2351] 未检测到与用药相关突变\n[BBOX-2352] EGFR\n[BBOX-2353] 突变\n[BBOX-2354] 未检测到与用药相关突变\n[BBOX-2355] ERBB2(HER2)\n[BBOX-2356] 突变/扩增\n[BBOX-2357] 未检测到与用药相关突变\n[BBOX-2358] FGFR2\n[BBOX-2359] 突变/融合\n[BBOX-2360] 未检测到与用药相关突变\n[BBOX-2361] FGFR3\n[BBOX-2362] 突变/融合\n[BBOX-2363] 未检测到与用药相关突变\n[BBOX-2364] KIT\n[BBOX-2365] 突变\n[BBOX-2366] 未检测到与用药相关突变\n[BBOX-2367] KRAS\n[BBOX-2368] 突变\n[BBOX-2369] NM_033360.4 exon2 c.35G>T p.G12V\n[BBOX-2370] 35.80%\n[BBOX-2371] MET\n[BBOX-2372] 突变/扩增/14号外\n[BBOX-2373] 未检测到与用药相关突变\n[BBOX-2374] 显子跳跃\n[BBOX-2375] NRG1\n[BBOX-2376] 融合\n[BBOX-2377] 未检测到与用药相关突变\n[BBOX-2378] NTRK1\n[BBOX-2379] 融合\n[BBOX-2380] 未检测到与用药相关突变\n[BBOX-2381] 广西金域医学检验实验室\n[BBOX-2382] 本报告单经过电子签名认证\n[BBOX-2383] Guangxi Kingmed Center for Clinical Laboratory\n[BBOX-2384] 金域医学\n[BBOX-2385] KingMed Diagnostics\n[BBOX-2386] 病理诊断报告书\n[BBOX-2387] 1/1\n[BBOX-2388] 标本条码\n[BBOX-2389] 1223023095\n[BBOX-2390] 医院\n[BBOX-2391] 广西医科大学第一附属医院\n[BBOX-2392] 病人姓名\n[BBOX-2393] 孔令祈\n[BBOX-2394] 科室\n[BBOX-2395] 老年呼吸\n[BBOX-2396] 病理号\n[BBOX-2397] 26018339\n[BBOX-2398] 性别\n[BBOX-2399] 男\n[BBOX-2400] 房/床号\n[BBOX-2401] 49\n[BBOX-2402] 住院门诊号\n[BBOX-2403] 1959880\n[BBOX-2404] 年龄\n[BBOX-2405] 67岁\n[BBOX-2406] 接收时间\n[BBOX-2407] 2026-03-08 14:15:50\n[BBOX-2408] 申请医生\n[BBOX-2409] 项目名称\n[BBOX-2410] 免疫组化8项\n[BBOX-2411] 送检材料\n[BBOX-2412] 肺组织\n[BBOX-2413] 临床诊断\n[BBOX-2414] 患者电话\n[BBOX-2415] 大体描述:\n[BBOX-2416] 福尔马林固定标本，核对送检标本、病人姓名和条形码与申请单一致。\n[BBOX-2417] 灰红条索状组织3段，长0.5-1.8cm，直径均0.05cm。取1盒全（共1盒蜡块）\n[BBOX-2418] 镜下所见：\n[BBOX-2419] 诊断意见：\n[BBOX-2420] 肺组织穿刺活检：\n[BBOX-2421] -结合免疫组化，符合浸润性黏液型腺癌，请结合临床。\n[BBOX-2422] -免疫组化：CK7（+），CK20（+），Villin（+），TTF-1（散在+），NapsinA（散在+），P40（-），CDX2（-），Ki67（\n[BBOX-2423] 热点区约60%+）。\n[BBOX-2424] 报告医师：陈明坚\n[BBOX-2425] 本检测仅对送检负责，如果对结果有疑义，请在报告发布后7天内与我们联系，多谢合作！\n[BBOX-2426] 收样点：广西医科大学第一附属医院-呼吸内\n[BBOX-2427] 科\n[BBOX-2428] 主检实验室：广西金域\n[BBOX-2429] 地址：南宁市西乡塘区总部路3号中国-东盟科技企业孵化基地二期1号厂房一、三、\n[BBOX-2430] 四层\n[BBOX-2431] 报告专用章\n[BBOX-2432] 网址：www.kingmed.com.cn\n[BBOX-2433] GX003SCEJL7RJLY\n[BBOX-2434] 报告日期：2026-03-10 21:16:16\n[BBOX-2435] 更多报告服务\n[BBOX-2436] CS 扫描全能王\n[BBOX-2437] 3亿人都在用的扫描App"
  }
]
2026-08-10 16:05:50,219 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:05:50.217+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:06:22,051 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:06:22.050+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:06:33,017 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:06:33,051 INFO     29 [SmartSplitter] SmartSplitter done: 18 chunks from 18 LLM segments (all bbox_id). Types: {'AdmissionRecord': 1, 'ExaminationReport': 6, 'LabReport': 11}
2026-08-10 16:06:33,064 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 16:06:33,064 INFO     29 [Trace] task=5212989c | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "2438 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks": "18 items, types={'AdmissionRecord': 1, 'ExaminationReport': 6, 'LabReport': 11}"}
2026-08-10 16:06:33,064 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 16:06:33,066 INFO     29 [ChunkRouter] Routed 18 chunks into 3 groups: {'chunks_Admission': 1, 'chunks_Examination': 6, 'chunks_LabExam': 11}
2026-08-10 16:06:33,078 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 16:06:33,078 INFO     29 [Trace] task=5212989c | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | ChunkRouter:Router | outputs={"html": "", "json": "2438 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks": "18 items, types={'AdmissionRecord': 1, 'ExaminationReport': 6, 'LabReport': 11}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 11}"}
2026-08-10 16:06:33,078 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 16:06:33,087 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:06:33,087 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:06:33,088 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[14]
2026-08-10 16:06:33,088 INFO     29 [qwen-vl-table] positions ： [[14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:06:33,492 INFO     29 [qwen-vl-table] page=14, rect=842x595, img=(2339x1653)
2026-08-10 16:06:33,493 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:06:33,494 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2112, \"bbox_end\": 2119, \"encounter_dates\": [\"2026-02-28\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2026-02-28\n\\hline\n缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\\\\n\\hline\nTB-DNA & 结核杆菌DNA* & $<$5.00E+02 & & & & 拷贝 & $<$5.00E+02 & $<$5.00E+02 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 16:06:34,756 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:06:34,756 INFO     29 [qwen-vl-table] page=14 LLM output (len=228):
{
  "report_date": "2026-02-28",
  "items": [
    {
      "name": "结核杆菌DNA*",
      "item_code": "TB-DNA",
      "value": "<5.00E+02",
      "unit": "拷贝",
      "reference_range": "<5.00E+02",
      "abnormal": false
    }
  ]
}
2026-08-10 16:06:34,756 INFO     29 [qwen-vl-table] coord grouping: {14: 1}
2026-08-10 16:06:34,767 INFO     29 [qwen-vl-table] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3493919, prompt_len=515
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
结核杆菌DNA*

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
2026-08-10 16:06:36,402 INFO     29 [qwen-vl-table] coord API raw response (len=67):
```json
[
	{"text": "结核杆菌DNA*", "bbox": [228, 258, 298, 275]}
]
```
2026-08-10 16:06:36,404 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=1.6s
2026-08-10 16:06:36,404 INFO     29 [qwen-vl-table] coord item[0]: text=结核杆菌DNA*, bbox=[228, 258, 298, 275]
2026-08-10 16:06:36,406 INFO     29 [qwen-vl-table] page=14 coord: matched 1/1, time=1.6s
2026-08-10 16:06:36,406 INFO     29 [qwen-vl-table] new_positions (1):
[[15, 191.976, 250.916, 153.51, 163.625]]
2026-08-10 16:06:36,407 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=3.3s
2026-08-10 16:06:36,410 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:06:36,412 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:06:36,412 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[15]
2026-08-10 16:06:36,412 INFO     29 [qwen-vl-table] positions ： [[15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:06:36,806 INFO     29 [qwen-vl-table] page=15, rect=842x595, img=(2339x1653)
2026-08-10 16:06:36,806 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:06:36,807 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2120, \"bbox_end\": 2131, \"encounter_dates\": [\"2026-02-28\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2026-02-28\n\\hline\n项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\\\\n\\hline\n乙型肝炎表面抗原* & 0.00 & & & & IU/ml & 0-0.08 & \\\\\n乙型肝炎表面抗体* & 14.85 & & $\\uparrow$ & & mIU/mL & 0-10 & \\\\\n乙型肝炎e抗原* & 0.00 & & & & PElu/ml & 0-0.10 & \\\\\n乙型肝炎e抗体* & 0.14 & & & & IU/mL & 0-0.20 & \\\\\n乙型肝炎核心抗体* & 0.27 & & & & IU/mL & 0-0.50 & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 16:06:40,001 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:06:40,001 INFO     29 [qwen-vl-table] page=15 LLM output (len=899):
{
  "report_date": "2026-02-28",
  "items": [
    {
      "name": "乙型肝炎表面抗原*",
      "item_code": null,
      "value": "0.00",
      "unit": "IU/ml",
      "reference_range": "0-0.08",
      "abnormal": false
    },
    {
      "name": "乙型肝炎表面抗体*",
      "item_code": null,
      "value": "14.85",
      "unit": "mIU/mL",
      "reference_range": "0-10",
      "abnormal": true
    },
    {
      "name": "乙型肝炎e抗原*",
      "item_code": null,
      "value": "0.00",
      "unit": "PElu/ml",
      "reference_range": "0-0.10",
      "abnormal": false
    },
    {
      "name": "乙型肝炎e抗体*",
      "item_code": null,
      "value": "0.14",
      "unit": "IU/mL",
      "reference_range": "0-0.20",
      "abnormal": false
    },
    {
      "name": "乙型肝炎核心抗体*",
      "item_code": null,
      "value": "0.27",
      "unit": "IU/mL",
      "reference_range": "0-0.50",
      "abnormal": false
    }
  ]
}
2026-08-10 16:06:40,002 INFO     29 [qwen-vl-table] coord grouping: {15: 5}
2026-08-10 16:06:40,016 INFO     29 [qwen-vl-table] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5124959, prompt_len=554
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
乙型肝炎表面抗原*、乙型肝炎表面抗体*、乙型肝炎e抗原*、乙型肝炎e抗体*、乙型肝炎核心抗体*

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
2026-08-10 16:06:42,775 INFO     29 [qwen-vl-table] coord API raw response (len=270):
[
	{"text": "乙型肝炎表面抗原*", "bbox": [124, 250, 207, 266]},
	{"text": "乙型肝炎表面抗体*", "bbox": [124, 283, 207, 299]},
	{"text": "乙型肝炎e抗原*", "bbox": [132, 317, 201, 333]},
	{"text": "乙型肝炎e抗体*", "bbox": [132, 350, 201, 366]},
	{"text": "乙型肝炎核心抗体*", "bbox": [127, 383, 208, 399]}
]
2026-08-10 16:06:42,776 INFO     29 [qwen-vl-table] coord API: raw_items=5, valid_items=5, elapsed=2.8s
2026-08-10 16:06:42,776 INFO     29 [qwen-vl-table] coord item[0]: text=乙型肝炎表面抗原*, bbox=[124, 250, 207, 266]
2026-08-10 16:06:42,776 INFO     29 [qwen-vl-table] coord item[1]: text=乙型肝炎表面抗体*, bbox=[124, 283, 207, 299]
2026-08-10 16:06:42,776 INFO     29 [qwen-vl-table] coord item[2]: text=乙型肝炎e抗原*, bbox=[132, 317, 201, 333]
2026-08-10 16:06:42,776 INFO     29 [qwen-vl-table] coord item[3]: text=乙型肝炎e抗体*, bbox=[132, 350, 201, 366]
2026-08-10 16:06:42,776 INFO     29 [qwen-vl-table] coord item[4]: text=乙型肝炎核心抗体*, bbox=[127, 383, 208, 399]
2026-08-10 16:06:42,776 INFO     29 [qwen-vl-table] page=15 coord: matched 5/5, time=2.8s
2026-08-10 16:06:42,776 INFO     29 [qwen-vl-table] new_positions (5):
[[16, 104.408, 174.29399999999998, 148.75, 158.26999999999998], [16, 104.408, 174.29399999999998, 168.385, 177.905], [16, 111.14399999999999, 169.242, 188.61499999999998, 198.135], [16, 111.14399999999999, 169.242, 208.25, 217.76999999999998], [16, 106.934, 175.136, 227.885, 237.405]]
2026-08-10 16:06:42,777 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=5, matched=5, pages=1, time=6.4s
2026-08-10 16:06:42,778 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:06:42,779 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:06:42,779 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[16]
2026-08-10 16:06:42,779 INFO     29 [qwen-vl-table] positions ： [[16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:06:43,182 INFO     29 [qwen-vl-table] page=16, rect=842x595, img=(2339x1653)
2026-08-10 16:06:43,182 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:06:43,183 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2132, \"bbox_end\": 2142, \"encounter_dates\": [\"2026-02-28\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llcccllcc}\n报告时间: 2026-02-28\n\\hline\n& & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\\\\n\\hline\n& / & 丙型肝炎抗体定量* & 0.06 & & & & COI & 0-1 & \\\\\n& ST & 不加热血清反应素试验* & 阴性(-) & & & & & 阴性(-) & \\\\\n& V & 人免疫缺陷病毒抗体定量* & 0.08 & & & & COI & 0-1 & \\\\\n& PA & 梅毒螺旋体抗体定量* & 0.08 & & & & COI & 0-1 & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 16:06:45,734 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:06:45,735 INFO     29 [qwen-vl-table] page=16 LLM output (len=718):
{
  "report_date": "2026-02-28",
  "items": [
    {
      "name": "丙型肝炎抗体定量*",
      "item_code": null,
      "value": "0.06",
      "unit": "COI",
      "reference_range": "0-1",
      "abnormal": false
    },
    {
      "name": "不加热血清反应素试验*",
      "item_code": null,
      "value": "阴性(-)",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": false
    },
    {
      "name": "人免疫缺陷病毒抗体定量*",
      "item_code": null,
      "value": "0.08",
      "unit": "COI",
      "reference_range": "0-1",
      "abnormal": false
    },
    {
      "name": "梅毒螺旋体抗体定量*",
      "item_code": null,
      "value": "0.08",
      "unit": "COI",
      "reference_range": "0-1",
      "abnormal": false
    }
  ]
}
2026-08-10 16:06:45,735 INFO     29 [qwen-vl-table] coord grouping: {16: 4}
2026-08-10 16:06:45,748 INFO     29 [qwen-vl-table] coord API call start, page=16, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4759042, prompt_len=552
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
丙型肝炎抗体定量*、不加热血清反应素试验*、人免疫缺陷病毒抗体定量*、梅毒螺旋体抗体定量*

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
2026-08-10 16:06:48,100 INFO     29 [qwen-vl-table] coord API raw response (len=236):
```json
[
	{"text": "丙型肝炎抗体定量*", "bbox": [164, 254, 247, 270]},
	{"text": "不加热血清反应素试验*", "bbox": [155, 289, 256, 304]},
	{"text": "人免疫缺陷病毒抗体定量*", "bbox": [152, 322, 261, 338]},
	{"text": "梅毒螺旋体抗体定量*", "bbox": [161, 356, 252, 371]}
]
```
2026-08-10 16:06:48,101 INFO     29 [qwen-vl-table] coord API: raw_items=4, valid_items=4, elapsed=2.4s
2026-08-10 16:06:48,101 INFO     29 [qwen-vl-table] coord item[0]: text=丙型肝炎抗体定量*, bbox=[164, 254, 247, 270]
2026-08-10 16:06:48,101 INFO     29 [qwen-vl-table] coord item[1]: text=不加热血清反应素试验*, bbox=[155, 289, 256, 304]
2026-08-10 16:06:48,101 INFO     29 [qwen-vl-table] coord item[2]: text=人免疫缺陷病毒抗体定量*, bbox=[152, 322, 261, 338]
2026-08-10 16:06:48,101 INFO     29 [qwen-vl-table] coord item[3]: text=梅毒螺旋体抗体定量*, bbox=[161, 356, 252, 371]
2026-08-10 16:06:48,104 INFO     29 [qwen-vl-table] page=16 coord: matched 4/4, time=2.4s
2026-08-10 16:06:48,104 INFO     29 [qwen-vl-table] new_positions (4):
[[17, 138.088, 207.974, 151.13, 160.65], [17, 130.51, 215.552, 171.95499999999998, 180.88], [17, 127.984, 219.762, 191.59, 201.10999999999999], [17, 135.56199999999998, 212.184, 211.82, 220.74499999999998]]
2026-08-10 16:06:48,104 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=4, matched=4, pages=1, time=5.3s
2026-08-10 16:06:48,107 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:06:48,109 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:06:48,109 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[17]
2026-08-10 16:06:48,110 INFO     29 [qwen-vl-table] positions ： [[17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:06:48,528 INFO     29 [qwen-vl-table] page=17, rect=842x595, img=(2339x1653)
2026-08-10 16:06:48,529 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:06:48,529 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2143, \"bbox_end\": 2152, \"encounter_dates\": [\"2026-02-28\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2026-02-28\n\\hline\n项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\\\\n\\hline\n糖化血红蛋白HbA1c* & 6.40 & & $\\uparrow$ & & \\% & 4.0-6.0 & \\\\\n糖化血红蛋白HbA1a & 0.50 & & & & \\% & 0-0.91 & \\\\\n糖化血红蛋白HbA1b & 1.10 & & & & \\% & 0.35-1.82 & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 16:06:50,781 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:06:50,781 INFO     29 [qwen-vl-table] page=17 LLM output (len=567):
{
  "report_date": "2026-02-28",
  "items": [
    {
      "name": "糖化血红蛋白HbA1c*",
      "item_code": "HbA1c",
      "value": "6.40",
      "unit": "%",
      "reference_range": "4.0-6.0",
      "abnormal": true
    },
    {
      "name": "糖化血红蛋白HbA1a",
      "item_code": "HbA1a",
      "value": "0.50",
      "unit": "%",
      "reference_range": "0-0.91",
      "abnormal": false
    },
    {
      "name": "糖化血红蛋白HbA1b",
      "item_code": "HbA1b",
      "value": "1.10",
      "unit": "%",
      "reference_range": "0.35-1.82",
      "abnormal": false
    }
  ]
}
2026-08-10 16:06:50,781 INFO     29 [qwen-vl-table] coord grouping: {17: 3}
2026-08-10 16:06:50,793 INFO     29 [qwen-vl-table] coord API call start, page=17, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4492034, prompt_len=543
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
糖化血红蛋白HbA1c*、糖化血红蛋白HbA1a、糖化血红蛋白HbA1b

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
2026-08-10 16:06:53,074 INFO     29 [qwen-vl-table] coord API raw response (len=183):
```json
[
	{"text": "糖化血红蛋白HbA1c*", "bbox": [147, 263, 245, 279]},
	{"text": "糖化血红蛋白HbA1a", "bbox": [147, 296, 243, 312]},
	{"text": "糖化血红蛋白HbA1b", "bbox": [147, 330, 243, 346]}
]
```
2026-08-10 16:06:53,074 INFO     29 [qwen-vl-table] coord API: raw_items=3, valid_items=3, elapsed=2.3s
2026-08-10 16:06:53,075 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白HbA1c*, bbox=[147, 263, 245, 279]
2026-08-10 16:06:53,075 INFO     29 [qwen-vl-table] coord item[1]: text=糖化血红蛋白HbA1a, bbox=[147, 296, 243, 312]
2026-08-10 16:06:53,075 INFO     29 [qwen-vl-table] coord item[2]: text=糖化血红蛋白HbA1b, bbox=[147, 330, 243, 346]
2026-08-10 16:06:53,077 INFO     29 [qwen-vl-table] page=17 coord: matched 3/3, time=2.3s
2026-08-10 16:06:53,077 INFO     29 [qwen-vl-table] new_positions (3):
[[18, 123.774, 206.29, 156.48499999999999, 166.005], [18, 123.774, 204.606, 176.12, 185.64], [18, 123.774, 204.606, 196.35, 205.87]]
2026-08-10 16:06:53,077 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=3, matched=3, pages=1, time=5.0s
2026-08-10 16:06:53,082 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:06:53,083 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:06:53,084 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[18]
2026-08-10 16:06:53,084 INFO     29 [qwen-vl-table] positions ： [[18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:06:53,497 INFO     29 [qwen-vl-table] page=18, rect=842x595, img=(2339x1653)
2026-08-10 16:06:53,498 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:06:53,498 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2153, \"bbox_end\": 2166, \"encounter_dates\": [\"2026-02-28\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l c c c c c c c}\n报告时间: 2026-02-28\n\\hline\n项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历 \\\\\n\\hline\n凝血酶原时间* & 11.50 & & & & S & 9-15 & \\\\\n国际标准化比值* & 1.04 & & & & & 0.8-1.4 & \\\\\n纤维蛋白原* & 4.43 & & & & g/L & 2.00 -5.00 & \\\\\n活化部分凝血活酶时间* & 32.30 & & & & S & 23.00 -40.00 & \\\\\n凝血酶时间* & 13.00 & & & & S & 10.3-16.6 & \\\\\n凝血酶原活动度 & 98 & & & & \\% & 70-130 & \\\\\nD-二聚体定量* & 69 & & & & ng/ml & 0-450 & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 16:06:53,874 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:06:53.872+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:06:59,400 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:06:59,400 INFO     29 [qwen-vl-table] page=18 LLM output (len=1213):
{
  "report_date": "2026-02-28",
  "items": [
    {
      "name": "凝血酶原时间",
      "item_code": null,
      "value": "11.50",
      "unit": "S",
      "reference_range": "9-15",
      "abnormal": false
    },
    {
      "name": "国际标准化比值",
      "item_code": null,
      "value": "1.04",
      "unit": null,
      "reference_range": "0.8-1.4",
      "abnormal": false
    },
    {
      "name": "纤维蛋白原",
      "item_code": null,
      "value": "4.43",
      "unit": "g/L",
      "reference_range": "2.00 -5.00",
      "abnormal": false
    },
    {
      "name": "活化部分凝血活酶时间",
      "item_code": null,
      "value": "32.30",
      "unit": "S",
      "reference_range": "23.00 -40.00",
      "abnormal": false
    },
    {
      "name": "凝血酶时间",
      "item_code": null,
      "value": "13.00",
      "unit": "S",
      "reference_range": "10.3-16.6",
      "abnormal": false
    },
    {
      "name": "凝血酶原活动度",
      "item_code": null,
      "value": "98",
      "unit": "%",
      "reference_range": "70-130",
      "abnormal": false
    },
    {
      "name": "D-二聚体定量",
      "item_code": null,
      "value": "69",
      "unit": "ng/ml",
      "reference_range": "0-450",
      "abnormal": false
    }
  ]
}
2026-08-10 16:06:59,400 INFO     29 [qwen-vl-table] coord grouping: {18: 7}
2026-08-10 16:06:59,414 INFO     29 [qwen-vl-table] coord API call start, page=18, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4503128, prompt_len=560
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
凝血酶原时间、国际标准化比值、纤维蛋白原、活化部分凝血活酶时间、凝血酶时间、凝血酶原活动度、D-二聚体定量

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
2026-08-10 16:07:02,401 INFO     29 [qwen-vl-table] coord API raw response (len=364):
[
	{"text": "凝血酶原时间", "bbox": [176, 260, 241, 277]},
	{"text": "国际标准化比值", "bbox": [171, 294, 245, 311]},
	{"text": "纤维蛋白原", "bbox": [181, 328, 236, 345]},
	{"text": "活化部分凝血活酶时间", "bbox": [157, 362, 261, 379]},
	{"text": "凝血酶时间", "bbox": [182, 396, 237, 413]},
	{"text": "凝血酶原活动度", "bbox": [175, 429, 246, 446]},
	{"text": "D-二聚体定量", "bbox": [177, 463, 245, 480]}
]
2026-08-10 16:07:02,401 INFO     29 [qwen-vl-table] coord API: raw_items=7, valid_items=7, elapsed=3.0s
2026-08-10 16:07:02,401 INFO     29 [qwen-vl-table] coord item[0]: text=凝血酶原时间, bbox=[176, 260, 241, 277]
2026-08-10 16:07:02,401 INFO     29 [qwen-vl-table] coord item[1]: text=国际标准化比值, bbox=[171, 294, 245, 311]
2026-08-10 16:07:02,401 INFO     29 [qwen-vl-table] coord item[2]: text=纤维蛋白原, bbox=[181, 328, 236, 345]
2026-08-10 16:07:02,401 INFO     29 [qwen-vl-table] coord item[3]: text=活化部分凝血活酶时间, bbox=[157, 362, 261, 379]
2026-08-10 16:07:02,401 INFO     29 [qwen-vl-table] coord item[4]: text=凝血酶时间, bbox=[182, 396, 237, 413]
2026-08-10 16:07:02,401 INFO     29 [qwen-vl-table] coord item[5]: text=凝血酶原活动度, bbox=[175, 429, 246, 446]
2026-08-10 16:07:02,401 INFO     29 [qwen-vl-table] coord item[6]: text=D-二聚体定量, bbox=[177, 463, 245, 480]
2026-08-10 16:07:02,402 INFO     29 [qwen-vl-table] page=18 coord: matched 7/7, time=3.0s
2026-08-10 16:07:02,402 INFO     29 [qwen-vl-table] new_positions (7):
[[19, 148.192, 202.922, 154.7, 164.815], [19, 143.982, 206.29, 174.92999999999998, 185.045], [19, 152.402, 198.712, 195.16, 205.27499999999998], [19, 132.194, 219.762, 215.39, 225.505], [19, 153.244, 199.554, 235.61999999999998, 245.73499999999999], [19, 147.35, 207.132, 255.255, 265.37], [19, 149.034, 206.29, 275.485, 285.59999999999997]]
2026-08-10 16:07:02,402 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=7, matched=7, pages=1, time=9.3s
2026-08-10 16:07:02,404 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:07:02,406 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:07:02,406 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[19]
2026-08-10 16:07:02,406 INFO     29 [qwen-vl-table] positions ： [[19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:07:02,809 INFO     29 [qwen-vl-table] page=19, rect=842x595, img=(2339x1653)
2026-08-10 16:07:02,809 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:07:02,809 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2167, \"bbox_end\": 2194, \"encounter_dates\": [\"2026-02-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2026-02-02\n\\hline\n缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & \\\\\n\\hline\nTBIL & 总胆红素* & 8.7 & & & & \\textmu mol/L & 0-26.0 & \\\\\nDBIL & 直接胆红素* & 3.6 & & & & \\textmu mol/L & 0-6.8 & \\\\\nIBIL & 间接胆红素 & 5.1 & & & & \\textmu mol/L & 3.1-14.3 & \\\\\nDB/TB & 直/总胆比值 & 0.41 & & & & & & \\\\\nTP & 总蛋白\\# & 74.5 & & & & g/L & 65-85 & \\\\\nALB & 白蛋白* & 39.3 & & \\downarrow & & g/L & 40-55 & \\\\\nGLO & 球蛋白 & 35.2 & & & & g/L & 20-40 & \\\\\nA/G & 白蛋白/球蛋白 & 1.1 & & \\downarrow & & & 1.2-2.4 & \\\\\nGGT & 谷氨酰转肽酶* & 30 & & & & U/L & 10-60 & \\\\\nTBA & 总胆汁酸* & 13.2 & & \\uparrow & & \\textmu mol/L & 0-10 & \\\\\nAST & 天门冬氨酸氨基转移酶* & 15 & & & & U/L & 15-40 & \\\\\nALT & 丙氨酸氨基转移酶* & 14 & & & & U/L & 9-50 & \\\\\nAST/ALT & 谷草/谷丙比值 & 1.1 & & & & & & \\\\\nALP & 碱性磷酸酶* & 64 & & & & U/L & 45-125 & \\\\\nPA & 前白蛋白* & 251.5 & & & & mg/L & 200-430 & \\\\\nCHE & 胆碱酯酶* & 8382 & & & & U/L & 5000-12000 & \\\\\nUREA & 尿素* & 6.98 & & & & mmol/L & 3.6-9.5 & \\\\\nCREA & 肌酐* & 136 & & \\uparrow & & \\textmu mol/L & 57-111 & \\\\\nUA & 尿酸* & 551 & & \\uparrow & & \\textmu mol/L & 208-428 & \\\\\nHCO3 & 碳酸氢根* & 21.6 & & \\downarrow & & mmol/L & 22-29 & \\\\\nT-CHO & 总胆固醇* & 3.10 & & & & mmol/L & 3.1-5.7 & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 16:07:13,854 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:07:13,854 INFO     29 [qwen-vl-table] page=19 LLM output (len=3562):
{
  "report_date": "2026-02-02",
  "items": [
    {
      "name": "总胆红素*",
      "item_code": "TBIL",
      "value": "8.7",
      "unit": "\u00b5mol/L",
      "reference_range": "0-26.0",
      "abnormal": false
    },
    {
      "name": "直接胆红素*",
      "item_code": "DBIL",
      "value": "3.6",
      "unit": "\u00b5mol/L",
      "reference_range": "0-6.8",
      "abnormal": false
    },
    {
      "name": "间接胆红素",
      "item_code": "IBIL",
      "value": "5.1",
      "unit": "\u00b5mol/L",
      "reference_range": "3.1-14.3",
      "abnormal": false
    },
    {
      "name": "直/总胆比值",
      "item_code": "DB/TB",
      "value": "0.41",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "总蛋白#",
      "item_code": "TP",
      "value": "74.5",
      "unit": "g/L",
      "reference_range": "65-85",
      "abnormal": false
    },
    {
      "name": "白蛋白*",
      "item_code": "ALB",
      "value": "39.3",
      "unit": "g/L",
      "reference_range": "40-55",
      "abnormal": true
    },
    {
      "name": "球蛋白",
      "item_code": "GLO",
      "value": "35.2",
      "unit": "g/L",
      "reference_range": "20-40",
      "abnormal": false
    },
    {
      "name": "白蛋白/球蛋白",
      "item_code": "A/G",
      "value": "1.1",
      "unit": null,
      "reference_range": "1.2-2.4",
      "abnormal": true
    },
    {
      "name": "谷氨酰转肽酶*",
      "item_code": "GGT",
      "value": "30",
      "unit": "U/L",
      "reference_range": "10-60",
      "abnormal": false
    },
    {
      "name": "总胆汁酸*",
      "item_code": "TBA",
      "value": "13.2",
      "unit": "\u00b5mol/L",
      "reference_range": "0-10",
      "abnormal": true
    },
    {
      "name": "天门冬氨酸氨基转移酶*",
      "item_code": "AST",
      "value": "15",
      "unit": "U/L",
      "reference_range": "15-40",
      "abnormal": false
    },
    {
      "name": "丙氨酸氨基转移酶*",
      "item_code": "ALT",
      "value": "14",
      "unit": "U/L",
      "reference_range": "9-50",
      "abnormal": false
    },
    {
      "name": "谷草/谷丙比值",
      "item_code": "AST/ALT",
      "value": "1.1",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "碱性磷酸酶*",
      "item_code": "ALP",
      "value": "64",
      "unit": "U/L",
      "reference_range": "45-125",
      "abnormal": false
    },
    {
      "name": "前白蛋白*",
      "item_code": "PA",
      "value": "251.5",
      "unit": "mg/L",
      "reference_range": "200-430",
      "abnormal": false
    },
    {
      "name": "胆碱酯酶*",
      "item_code": "CHE",
      "value": "8382",
      "unit": "U/L",
      "reference_range": "5000-12000",
      "abnormal": false
    },
    {
      "name": "尿素*",
      "item_code": "UREA",
      "value": "6.98",
      "unit": "mmol/L",
      "reference_range": "3.6-9.5",
      "abnormal": false
    },
    {
      "name": "肌酐*",
      "item_code": "CREA",
      "value": "136",
      "unit": "\u00b5mol/L",
      "reference_range": "57-111",
      "abnormal": true
    },
    {
      "name": "尿酸*",
      "item_code": "UA",
      "value": "551",
      "unit": "\u00b5mol/L",
      "reference_range": "208-428",
      "abnormal": true
    },
    {
      "name": "碳酸氢根*",
      "item_code": "HCO3",
      "value": "21.6",
      "unit": "mmol/L",
      "reference_range": "22-29",
      "abnormal": true
    },
    {
      "name": "总胆固醇*",
      "item_code": "T-CHO",
      "value": "3.10",
      "unit": "mmol/L",
      "reference_range": "3.1-5.7",
      "abnormal": false
    }
  ]
}
2026-08-10 16:07:13,854 INFO     29 [qwen-vl-table] coord grouping: {19: 21}
2026-08-10 16:07:13,870 INFO     29 [qwen-vl-table] coord API call start, page=19, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5840961, prompt_len=641
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
总胆红素*、直接胆红素*、间接胆红素、直/总胆比值、总蛋白#、白蛋白*、球蛋白、白蛋白/球蛋白、谷氨酰转肽酶*、总胆汁酸*、天门冬氨酸氨基转移酶*、丙氨酸氨基转移酶*、谷草/谷丙比值、碱性磷酸酶*、前白蛋白*、胆碱酯酶*、尿素*、肌酐*、尿酸*、碳酸氢根*、总胆固醇*

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
2026-08-10 16:07:20,066 INFO     29 [qwen-vl-table] coord API raw response (len=1061):
[
	{"text": "总胆红素*", "bbox": [235, 243, 278, 258]},
	{"text": "直接胆红素*", "bbox": [230, 276, 282, 291]},
	{"text": "间接胆红素", "bbox": [232, 309, 280, 324]},
	{"text": "直/总胆比值", "bbox": [230, 343, 282, 358]},
	{"text": "总蛋白#", "bbox": [239, 376, 273, 391]},
	{"text": "白蛋白*", "bbox": [240, 409, 272, 424]},
	{"text": "球蛋白", "bbox": [242, 441, 270, 456]},
	{"text": "白蛋白/球蛋白", "bbox": [225, 474, 288, 489]},
	{"text": "谷氨酰转肽酶*", "bbox": [226, 507, 288, 522]},
	{"text": "总胆汁酸*", "bbox": [237, 539, 278, 554]},
	{"text": "天门冬氨酸氨基转移酶*", "bbox": [207, 572, 308, 587]},
	{"text": "丙氨酸氨基转移酶*", "bbox": [217, 605, 299, 620]},
	{"text": "谷草/谷丙比值", "bbox": [227, 638, 290, 653]},
	{"text": "碱性磷酸酶*", "bbox": [232, 671, 284, 686]},
	{"text": "前白蛋白*", "bbox": [238, 704, 280, 719]},
	{"text": "胆碱酯酶*", "bbox": [238, 736, 280, 751]},
	{"text": "尿素*", "bbox": [248, 769, 270, 784]},
	{"text": "肌酐*", "bbox": [248, 802, 270, 817]},
	{"text": "尿酸*", "bbox": [250, 834, 272, 849]},
	{"text": "碳酸氢根*", "bbox": [240, 866, 281, 881]},
	{"text": "总胆固醇*", "bbox": [230, 900, 282, 915]}
]
2026-08-10 16:07:20,067 INFO     29 [qwen-vl-table] coord API: raw_items=21, valid_items=21, elapsed=6.2s
2026-08-10 16:07:20,067 INFO     29 [qwen-vl-table] coord item[0]: text=总胆红素*, bbox=[235, 243, 278, 258]
2026-08-10 16:07:20,067 INFO     29 [qwen-vl-table] coord item[1]: text=直接胆红素*, bbox=[230, 276, 282, 291]
2026-08-10 16:07:20,067 INFO     29 [qwen-vl-table] coord item[2]: text=间接胆红素, bbox=[232, 309, 280, 324]
2026-08-10 16:07:20,067 INFO     29 [qwen-vl-table] coord item[3]: text=直/总胆比值, bbox=[230, 343, 282, 358]
2026-08-10 16:07:20,068 INFO     29 [qwen-vl-table] coord item[4]: text=总蛋白#, bbox=[239, 376, 273, 391]
2026-08-10 16:07:20,068 INFO     29 [qwen-vl-table] coord item[5]: text=白蛋白*, bbox=[240, 409, 272, 424]
2026-08-10 16:07:20,068 INFO     29 [qwen-vl-table] coord item[6]: text=球蛋白, bbox=[242, 441, 270, 456]
2026-08-10 16:07:20,068 INFO     29 [qwen-vl-table] coord item[7]: text=白蛋白/球蛋白, bbox=[225, 474, 288, 489]
2026-08-10 16:07:20,068 INFO     29 [qwen-vl-table] coord item[8]: text=谷氨酰转肽酶*, bbox=[226, 507, 288, 522]
2026-08-10 16:07:20,068 INFO     29 [qwen-vl-table] coord item[9]: text=总胆汁酸*, bbox=[237, 539, 278, 554]
2026-08-10 16:07:20,068 INFO     29 [qwen-vl-table] coord item[10]: text=天门冬氨酸氨基转移酶*, bbox=[207, 572, 308, 587]
2026-08-10 16:07:20,068 INFO     29 [qwen-vl-table] coord item[11]: text=丙氨酸氨基转移酶*, bbox=[217, 605, 299, 620]
2026-08-10 16:07:20,068 INFO     29 [qwen-vl-table] coord item[12]: text=谷草/谷丙比值, bbox=[227, 638, 290, 653]
2026-08-10 16:07:20,068 INFO     29 [qwen-vl-table] coord item[13]: text=碱性磷酸酶*, bbox=[232, 671, 284, 686]
2026-08-10 16:07:20,068 INFO     29 [qwen-vl-table] coord item[14]: text=前白蛋白*, bbox=[238, 704, 280, 719]
2026-08-10 16:07:20,069 INFO     29 [qwen-vl-table] coord item[15]: text=胆碱酯酶*, bbox=[238, 736, 280, 751]
2026-08-10 16:07:20,069 INFO     29 [qwen-vl-table] coord item[16]: text=尿素*, bbox=[248, 769, 270, 784]
2026-08-10 16:07:20,069 INFO     29 [qwen-vl-table] coord item[17]: text=肌酐*, bbox=[248, 802, 270, 817]
2026-08-10 16:07:20,069 INFO     29 [qwen-vl-table] coord item[18]: text=尿酸*, bbox=[250, 834, 272, 849]
2026-08-10 16:07:20,069 INFO     29 [qwen-vl-table] coord item[19]: text=碳酸氢根*, bbox=[240, 866, 281, 881]
2026-08-10 16:07:20,069 INFO     29 [qwen-vl-table] coord item[20]: text=总胆固醇*, bbox=[230, 900, 282, 915]
2026-08-10 16:07:20,071 INFO     29 [qwen-vl-table] page=19 coord: matched 21/21, time=6.2s
2026-08-10 16:07:20,071 INFO     29 [qwen-vl-table] new_positions (21):
[[20, 197.87, 234.076, 144.58499999999998, 153.51], [20, 193.66, 237.444, 164.22, 173.14499999999998], [20, 195.344, 235.76, 183.855, 192.78], [20, 193.66, 237.444, 204.08499999999998, 213.01], [20, 201.238, 229.86599999999999, 223.72, 232.64499999999998], [20, 202.07999999999998, 229.024, 243.355, 252.28], [20, 203.76399999999998, 227.34, 262.395, 271.32], [20, 189.45, 242.49599999999998, 282.03, 290.955], [20, 190.292, 242.49599999999998, 301.66499999999996, 310.59], [20, 199.554, 234.076, 320.705, 329.63], [20, 174.29399999999998, 259.336, 340.34, 349.265], [20, 182.714, 251.75799999999998, 359.97499999999997, 368.9], [20, 191.134, 244.17999999999998, 379.60999999999996, 388.53499999999997], [20, 195.344, 239.128, 399.245, 408.16999999999996], [20, 200.396, 235.76, 418.88, 427.805], [20, 200.396, 235.76, 437.91999999999996, 446.84499999999997], [20, 208.816, 227.34, 457.555, 466.47999999999996], [20, 208.816, 227.34, 477.19, 486.11499999999995], [20, 210.5, 229.024, 496.22999999999996, 505.155], [20, 202.07999999999998, 236.602, 515.27, 524.1949999999999], [20, 193.66, 237.444, 535.5, 544.425]]
2026-08-10 16:07:20,072 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=21, matched=21, pages=1, time=17.7s
2026-08-10 16:07:20,074 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:07:20,076 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:07:20,076 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[20]
2026-08-10 16:07:20,076 INFO     29 [qwen-vl-table] positions ： [[20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:07:20,479 INFO     29 [qwen-vl-table] page=20, rect=842x595, img=(2339x1653)
2026-08-10 16:07:20,480 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:07:20,480 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2195, \"bbox_end\": 2221, \"encounter_dates\": [\"2025-04-01\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2025-04-01\n\\hline\n缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & \\\\\n\\hline\nCHE & 胆碱酯酶* & 8382 & & & & U/L & 5000-12000 & \\\\\nUREA & 尿素* & 6.98 & & & & mmol/L & 3.6-9.5 & \\\\\nCREA & 肌酐* & 136 & & $\\uparrow$ & & $\\mu$mol/L & 57-111 & \\\\\nUA & 尿酸* & 551 & & $\\uparrow$ & & $\\mu$mol/L & 208-428 & \\\\\nHCO3 & 碳酸氢根* & 21.6 & & $\\downarrow$ & & mmol/L & 22-29 & \\\\\nT-CHO & 总胆固醇* & 3.18 & & & & mmol/L & $<$5.2 & \\\\\nTG & 甘油三酯* & 1.27 & & & & mmol/L & $<$1.7 & \\\\\nLDL-C & 低密度脂蛋白胆固醇* & 1.78 & & & & mmol/L & $<$3.4(低危人群) & \\\\\nGLU & 空腹血葡萄糖* & 4.79 & & & & mmol/L & 3.9-6.1 & \\\\\nK & 钾* & 4.18 & & & & mmol/L & 3.5-5.3 & \\\\\nNa & 钠* & 141.1 & & & & mmol/L & 137-147 & \\\\\nCL & 氯* & 106.4 & & & & mmol/L & 99-110 & \\\\\nCa & 总钙* & 2.25 & & & & mmol/L & 2.11-2.52 & \\\\\nMg & 镁* & 0.78 & & & & mmol/L & 0.75-1.02 & \\\\\nP & 磷* & 0.95 & & & & mmol/L & 0.85-1.51 & \\\\\nCK & 肌酸激酶* & 84 & & & & U/L & 50-310 & \\\\\nCK-MB & 肌酸激酶同工酶MB & 13 & & & & U/L & 0-25 & \\\\\nLD & 乳酸脱氢酶* & 167 & & & & U/L & 120-250 & \\\\\n$\\alpha$-HBD & $\\alpha$-羟丁酸脱氢酶* & 109 & & & & U/L & 72-182 & \\\\\nIgE & 免疫球蛋白E* & 1960.6 & & $\\uparrow$ & & IU/ml & $<$100 & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 16:07:25,769 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:07:25.767+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:07:33,422 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:07:33,422 INFO     29 [qwen-vl-table] page=20 LLM output (len=3394):
{
  "report_date": "2025-04-01",
  "items": [
    {
      "name": "胆碱酯酶*",
      "item_code": "CHE",
      "value": "8382",
      "unit": "U/L",
      "reference_range": "5000-12000",
      "abnormal": false
    },
    {
      "name": "尿素*",
      "item_code": "UREA",
      "value": "6.98",
      "unit": "mmol/L",
      "reference_range": "3.6-9.5",
      "abnormal": false
    },
    {
      "name": "肌酐*",
      "item_code": "CREA",
      "value": "136",
      "unit": "μmol/L",
      "reference_range": "57-111",
      "abnormal": true
    },
    {
      "name": "尿酸*",
      "item_code": "UA",
      "value": "551",
      "unit": "μmol/L",
      "reference_range": "208-428",
      "abnormal": true
    },
    {
      "name": "碳酸氢根*",
      "item_code": "HCO3",
      "value": "21.6",
      "unit": "mmol/L",
      "reference_range": "22-29",
      "abnormal": true
    },
    {
      "name": "总胆固醇*",
      "item_code": "T-CHO",
      "value": "3.18",
      "unit": "mmol/L",
      "reference_range": "<5.2",
      "abnormal": false
    },
    {
      "name": "甘油三酯*",
      "item_code": "TG",
      "value": "1.27",
      "unit": "mmol/L",
      "reference_range": "<1.7",
      "abnormal": false
    },
    {
      "name": "低密度脂蛋白胆固醇*",
      "item_code": "LDL-C",
      "value": "1.78",
      "unit": "mmol/L",
      "reference_range": "<3.4(低危人群)",
      "abnormal": false
    },
    {
      "name": "空腹血葡萄糖*",
      "item_code": "GLU",
      "value": "4.79",
      "unit": "mmol/L",
      "reference_range": "3.9-6.1",
      "abnormal": false
    },
    {
      "name": "钾*",
      "item_code": "K",
      "value": "4.18",
      "unit": "mmol/L",
      "reference_range": "3.5-5.3",
      "abnormal": false
    },
    {
      "name": "钠*",
      "item_code": "Na",
      "value": "141.1",
      "unit": "mmol/L",
      "reference_range": "137-147",
      "abnormal": false
    },
    {
      "name": "氯*",
      "item_code": "CL",
      "value": "106.4",
      "unit": "mmol/L",
      "reference_range": "99-110",
      "abnormal": false
    },
    {
      "name": "总钙*",
      "item_code": "Ca",
      "value": "2.25",
      "unit": "mmol/L",
      "reference_range": "2.11-2.52",
      "abnormal": false
    },
    {
      "name": "镁*",
      "item_code": "Mg",
      "value": "0.78",
      "unit": "mmol/L",
      "reference_range": "0.75-1.02",
      "abnormal": false
    },
    {
      "name": "磷*",
      "item_code": "P",
      "value": "0.95",
      "unit": "mmol/L",
      "reference_range": "0.85-1.51",
      "abnormal": false
    },
    {
      "name": "肌酸激酶*",
      "item_code": "CK",
      "value": "84",
      "unit": "U/L",
      "reference_range": "50-310",
      "abnormal": false
    },
    {
      "name": "肌酸激酶同工酶MB",
      "item_code": "CK-MB",
      "value": "13",
      "unit": "U/L",
      "reference_range": "0-25",
      "abnormal": false
    },
    {
      "name": "乳酸脱氢酶*",
      "item_code": "LD",
      "value": "167",
      "unit": "U/L",
      "reference_range": "120-250",
      "abnormal": false
    },
    {
      "name": "α-羟丁酸脱氢酶*",
      "item_code": "α-HBD",
      "value": "109",
      "unit": "U/L",
      "reference_range": "72-182",
      "abnormal": false
    },
    {
      "name": "免疫球蛋白E*",
      "item_code": "IgE",
      "value": "1960.6",
      "unit": "IU/ml",
      "reference_range": "<100",
      "abnormal": true
    }
  ]
}
2026-08-10 16:07:33,422 INFO     29 [qwen-vl-table] coord grouping: {20: 20}
2026-08-10 16:07:33,436 INFO     29 [qwen-vl-table] coord API call start, page=20, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5648298, prompt_len=621
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
胆碱酯酶*、尿素*、肌酐*、尿酸*、碳酸氢根*、总胆固醇*、甘油三酯*、低密度脂蛋白胆固醇*、空腹血葡萄糖*、钾*、钠*、氯*、总钙*、镁*、磷*、肌酸激酶*、肌酸激酶同工酶MB、乳酸脱氢酶*、α-羟丁酸脱氢酶*、免疫球蛋白E*

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
2026-08-10 16:07:39,467 INFO     29 [qwen-vl-table] coord API raw response (len=997):
[
	{"text": "胆碱酯酶*", "bbox": [235, 235, 278, 250]},
	{"text": "尿素*", "bbox": [245, 268, 268, 283]},
	{"text": "肌酐*", "bbox": [245, 302, 268, 317]},
	{"text": "尿酸*", "bbox": [245, 335, 268, 350]},
	{"text": "碳酸氢根*", "bbox": [235, 368, 277, 383]},
	{"text": "总胆固醇*", "bbox": [235, 401, 277, 416]},
	{"text": "甘油三酯*", "bbox": [235, 435, 277, 450]},
	{"text": "低密度脂蛋白胆固醇*", "bbox": [211, 468, 301, 483]},
	{"text": "空腹血葡萄糖*", "bbox": [224, 502, 287, 517]},
	{"text": "钾*", "bbox": [248, 535, 263, 550]},
	{"text": "钠*", "bbox": [248, 569, 263, 584]},
	{"text": "氯*", "bbox": [248, 603, 263, 618]},
	{"text": "总钙*", "bbox": [245, 636, 268, 651]},
	{"text": "镁*", "bbox": [248, 670, 263, 685]},
	{"text": "磷*", "bbox": [250, 704, 265, 719]},
	{"text": "肌酸激酶*", "bbox": [235, 737, 278, 752]},
	{"text": "肌酸激酶同工酶MB", "bbox": [216, 771, 300, 786]},
	{"text": "乳酸脱氢酶*", "bbox": [232, 804, 285, 819]},
	{"text": "α-羟丁酸脱氢酶*", "bbox": [224, 838, 293, 853]},
	{"text": "免疫球蛋白E*", "bbox": [230, 871, 288, 886]}
]
2026-08-10 16:07:39,467 INFO     29 [qwen-vl-table] coord API: raw_items=20, valid_items=20, elapsed=6.0s
2026-08-10 16:07:39,467 INFO     29 [qwen-vl-table] coord item[0]: text=胆碱酯酶*, bbox=[235, 235, 278, 250]
2026-08-10 16:07:39,467 INFO     29 [qwen-vl-table] coord item[1]: text=尿素*, bbox=[245, 268, 268, 283]
2026-08-10 16:07:39,467 INFO     29 [qwen-vl-table] coord item[2]: text=肌酐*, bbox=[245, 302, 268, 317]
2026-08-10 16:07:39,467 INFO     29 [qwen-vl-table] coord item[3]: text=尿酸*, bbox=[245, 335, 268, 350]
2026-08-10 16:07:39,467 INFO     29 [qwen-vl-table] coord item[4]: text=碳酸氢根*, bbox=[235, 368, 277, 383]
2026-08-10 16:07:39,467 INFO     29 [qwen-vl-table] coord item[5]: text=总胆固醇*, bbox=[235, 401, 277, 416]
2026-08-10 16:07:39,467 INFO     29 [qwen-vl-table] coord item[6]: text=甘油三酯*, bbox=[235, 435, 277, 450]
2026-08-10 16:07:39,467 INFO     29 [qwen-vl-table] coord item[7]: text=低密度脂蛋白胆固醇*, bbox=[211, 468, 301, 483]
2026-08-10 16:07:39,467 INFO     29 [qwen-vl-table] coord item[8]: text=空腹血葡萄糖*, bbox=[224, 502, 287, 517]
2026-08-10 16:07:39,467 INFO     29 [qwen-vl-table] coord item[9]: text=钾*, bbox=[248, 535, 263, 550]
2026-08-10 16:07:39,468 INFO     29 [qwen-vl-table] coord item[10]: text=钠*, bbox=[248, 569, 263, 584]
2026-08-10 16:07:39,468 INFO     29 [qwen-vl-table] coord item[11]: text=氯*, bbox=[248, 603, 263, 618]
2026-08-10 16:07:39,468 INFO     29 [qwen-vl-table] coord item[12]: text=总钙*, bbox=[245, 636, 268, 651]
2026-08-10 16:07:39,468 INFO     29 [qwen-vl-table] coord item[13]: text=镁*, bbox=[248, 670, 263, 685]
2026-08-10 16:07:39,468 INFO     29 [qwen-vl-table] coord item[14]: text=磷*, bbox=[250, 704, 265, 719]
2026-08-10 16:07:39,468 INFO     29 [qwen-vl-table] coord item[15]: text=肌酸激酶*, bbox=[235, 737, 278, 752]
2026-08-10 16:07:39,468 INFO     29 [qwen-vl-table] coord item[16]: text=肌酸激酶同工酶MB, bbox=[216, 771, 300, 786]
2026-08-10 16:07:39,468 INFO     29 [qwen-vl-table] coord item[17]: text=乳酸脱氢酶*, bbox=[232, 804, 285, 819]
2026-08-10 16:07:39,468 INFO     29 [qwen-vl-table] coord item[18]: text=α-羟丁酸脱氢酶*, bbox=[224, 838, 293, 853]
2026-08-10 16:07:39,468 INFO     29 [qwen-vl-table] coord item[19]: text=免疫球蛋白E*, bbox=[230, 871, 288, 886]
2026-08-10 16:07:39,469 INFO     29 [qwen-vl-table] page=20 coord: matched 20/20, time=6.0s
2026-08-10 16:07:39,469 INFO     29 [qwen-vl-table] new_positions (20):
[[21, 197.87, 234.076, 139.825, 148.75], [21, 206.29, 225.656, 159.45999999999998, 168.385], [21, 206.29, 225.656, 179.69, 188.61499999999998], [21, 206.29, 225.656, 199.325, 208.25], [21, 197.87, 233.23399999999998, 218.95999999999998, 227.885], [21, 197.87, 233.23399999999998, 238.595, 247.51999999999998], [21, 197.87, 233.23399999999998, 258.825, 267.75], [21, 177.662, 253.44199999999998, 278.46, 287.385], [21, 188.608, 241.654, 298.69, 307.615], [21, 208.816, 221.446, 318.325, 327.25], [21, 208.816, 221.446, 338.555, 347.47999999999996], [21, 208.816, 221.446, 358.78499999999997, 367.71], [21, 206.29, 225.656, 378.41999999999996, 387.34499999999997], [21, 208.816, 221.446, 398.65, 407.575], [21, 210.5, 223.13, 418.88, 427.805], [21, 197.87, 234.076, 438.515, 447.44], [21, 181.87199999999999, 252.6, 458.745, 467.66999999999996], [21, 195.344, 239.97, 478.38, 487.30499999999995], [21, 188.608, 246.706, 498.60999999999996, 507.53499999999997], [21, 193.66, 242.49599999999998, 518.245, 527.17]]
2026-08-10 16:07:39,469 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=20, matched=20, pages=1, time=19.4s
2026-08-10 16:07:39,471 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:07:39,472 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:07:39,472 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[21]
2026-08-10 16:07:39,473 INFO     29 [qwen-vl-table] positions ： [[21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:07:39,880 INFO     29 [qwen-vl-table] page=21, rect=842x595, img=(2339x1653)
2026-08-10 16:07:39,881 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:07:39,882 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2222, \"bbox_end\": 2247, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n\\hline\n缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 \\\\\n\\hline\nWBC & 白细胞计数* & 8.490 & & & & 10~9/L & 3.5-9.5 \\\\\nRBC & 红细胞计数* & 5.81 & & $\\uparrow$ & & 10~12/L & 4.3-5.8 \\\\\nHGB & 血红蛋白* & 157.00 & & & & g/L & 130-175 \\\\\nPLT & 血小板计数* & 268.00 & & & & 10~9/L & 125-350 \\\\\nNEU\\% & 中性粒细胞百分比 & 0.6920 & & & & & 0.4-0.75 \\\\\nLYM\\% & 淋巴细胞百分比 & 0.1970 & & $\\downarrow$ & & & 0.2-0.5 \\\\\nMONO\\% & 单核细胞百分比 & 0.0630 & & & & & 0.03-0.1 \\\\\nEO\\% & 嗜酸性粒细胞百分比 & 0.0450 & & & & & 0.004-0.08 \\\\\nBA SO\\% & 嗜碱性粒细胞百分比 & 0.0030 & & & & & 0-0.01 \\\\\nNEU & 中性粒细胞绝对值 & 5.88 & & & & 10~9/L & 1.8-6.3 \\\\\nLYM & 淋巴细胞绝对值 & 1.67 & & & & 10~9/L & 1.1-3.2 \\\\\nMONO & 单核细胞绝对值 & 0.53 & & & & 10~9/L & 0.1-0.6 \\\\\nEOS & 嗜酸性粒细胞绝对值 & 0.38 & & & & 10~9/L & 0.02-0.52 \\\\\nBA SO & 嗜碱性粒细胞绝对值 & 0.03 & & & & 10~9/L & 0-0.06 \\\\\nMCV & 平均红细胞体积* & 83.70 & & & & fl & 82-100 \\\\\nMCH & 平均RBC血红蛋白含量* & 26.90 & & $\\downarrow$ & & pg & 27-34 \\\\\nMCHC & 平均RBC血红蛋白浓度* & 323.00 & & & & g/L & 316-354 \\\\\nHCT & 红细胞比容* & 0.486 & & & & & 0.4-0.5 \\\\\nRDWCV & RBC体积分布宽度CV & 0.15 & & $\\uparrow$ & & & 0.11-0.14 \\\\\nPDW & 血小板体积分布宽度 & 0.16 & & & & & 0.15-0.18 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 16:07:51,146 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:07:51,146 INFO     29 [qwen-vl-table] page=21 LLM output (len=3473):
{
  "report_date": null,
  "items": [
    {
      "name": "白细胞计数*",
      "item_code": "WBC",
      "value": "8.490",
      "unit": "10~9/L",
      "reference_range": "3.5-9.5",
      "abnormal": false
    },
    {
      "name": "红细胞计数*",
      "item_code": "RBC",
      "value": "5.81",
      "unit": "10~12/L",
      "reference_range": "4.3-5.8",
      "abnormal": true
    },
    {
      "name": "血红蛋白*",
      "item_code": "HGB",
      "value": "157.00",
      "unit": "g/L",
      "reference_range": "130-175",
      "abnormal": false
    },
    {
      "name": "血小板计数*",
      "item_code": "PLT",
      "value": "268.00",
      "unit": "10~9/L",
      "reference_range": "125-350",
      "abnormal": false
    },
    {
      "name": "中性粒细胞百分比",
      "item_code": "NEU%",
      "value": "0.6920",
      "unit": null,
      "reference_range": "0.4-0.75",
      "abnormal": false
    },
    {
      "name": "淋巴细胞百分比",
      "item_code": "LYM%",
      "value": "0.1970",
      "unit": null,
      "reference_range": "0.2-0.5",
      "abnormal": true
    },
    {
      "name": "单核细胞百分比",
      "item_code": "MONO%",
      "value": "0.0630",
      "unit": null,
      "reference_range": "0.03-0.1",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞百分比",
      "item_code": "EO%",
      "value": "0.0450",
      "unit": null,
      "reference_range": "0.004-0.08",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞百分比",
      "item_code": "BA SO%",
      "value": "0.0030",
      "unit": null,
      "reference_range": "0-0.01",
      "abnormal": false
    },
    {
      "name": "中性粒细胞绝对值",
      "item_code": "NEU",
      "value": "5.88",
      "unit": "10~9/L",
      "reference_range": "1.8-6.3",
      "abnormal": false
    },
    {
      "name": "淋巴细胞绝对值",
      "item_code": "LYM",
      "value": "1.67",
      "unit": "10~9/L",
      "reference_range": "1.1-3.2",
      "abnormal": false
    },
    {
      "name": "单核细胞绝对值",
      "item_code": "MONO",
      "value": "0.53",
      "unit": "10~9/L",
      "reference_range": "0.1-0.6",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞绝对值",
      "item_code": "EOS",
      "value": "0.38",
      "unit": "10~9/L",
      "reference_range": "0.02-0.52",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞绝对值",
      "item_code": "BA SO",
      "value": "0.03",
      "unit": "10~9/L",
      "reference_range": "0-0.06",
      "abnormal": false
    },
    {
      "name": "平均红细胞体积*",
      "item_code": "MCV",
      "value": "83.70",
      "unit": "fl",
      "reference_range": "82-100",
      "abnormal": false
    },
    {
      "name": "平均RBC血红蛋白含量*",
      "item_code": "MCH",
      "value": "26.90",
      "unit": "pg",
      "reference_range": "27-34",
      "abnormal": true
    },
    {
      "name": "平均RBC血红蛋白浓度*",
      "item_code": "MCHC",
      "value": "323.00",
      "unit": "g/L",
      "reference_range": "316-354",
      "abnormal": false
    },
    {
      "name": "红细胞比容*",
      "item_code": "HCT",
      "value": "0.486",
      "unit": null,
      "reference_range": "0.4-0.5",
      "abnormal": false
    },
    {
      "name": "RBC体积分布宽度CV",
      "item_code": "RDWCV",
      "value": "0.15",
      "unit": null,
      "reference_range": "0.11-0.14",
      "abnormal": true
    },
    {
      "name": "血小板体积分布宽度",
      "item_code": "PDW",
      "value": "0.16",
      "unit": null,
      "reference_range": "0.15-0.18",
      "abnormal": false
    }
  ]
}
2026-08-10 16:07:51,146 INFO     29 [qwen-vl-table] coord grouping: {21: 20}
2026-08-10 16:07:51,159 INFO     29 [qwen-vl-table] coord API call start, page=21, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5649844, prompt_len=687
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞计数*、红细胞计数*、血红蛋白*、血小板计数*、中性粒细胞百分比、淋巴细胞百分比、单核细胞百分比、嗜酸性粒细胞百分比、嗜碱性粒细胞百分比、中性粒细胞绝对值、淋巴细胞绝对值、单核细胞绝对值、嗜酸性粒细胞绝对值、嗜碱性粒细胞绝对值、平均红细胞体积*、平均RBC血红蛋白含量*、平均RBC血红蛋白浓度*、红细胞比容*、RBC体积分布宽度CV、血小板体积分布宽度

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
2026-08-10 16:07:57,372 INFO     29 [qwen-vl-table] coord API raw response (len=1063):
[
	{"text": "白细胞计数*", "bbox": [247, 250, 300, 267]},
	{"text": "红细胞计数*", "bbox": [247, 283, 300, 299]},
	{"text": "血红蛋白*", "bbox": [252, 316, 295, 332]},
	{"text": "血小板计数*", "bbox": [247, 349, 300, 365]},
	{"text": "中性粒细胞百分比", "bbox": [236, 381, 312, 397]},
	{"text": "淋巴细胞百分比", "bbox": [240, 414, 308, 430]},
	{"text": "单核细胞百分比", "bbox": [240, 447, 308, 463]},
	{"text": "嗜酸性粒细胞百分比", "bbox": [231, 479, 318, 495]},
	{"text": "嗜碱性粒细胞百分比", "bbox": [231, 512, 318, 528]},
	{"text": "中性粒细胞绝对值", "bbox": [236, 545, 312, 561]},
	{"text": "淋巴细胞绝对值", "bbox": [240, 577, 308, 593]},
	{"text": "单核细胞绝对值", "bbox": [240, 610, 308, 626]},
	{"text": "嗜酸性粒细胞绝对值", "bbox": [231, 643, 318, 659]},
	{"text": "嗜碱性粒细胞绝对值", "bbox": [231, 676, 318, 692]},
	{"text": "平均红细胞体积*", "bbox": [240, 708, 310, 724]},
	{"text": "平均RBC血红蛋白含量*", "bbox": [225, 741, 325, 757]},
	{"text": "平均RBC血红蛋白浓度*", "bbox": [225, 774, 325, 790]},
	{"text": "红细胞比容*", "bbox": [249, 807, 301, 823]},
	{"text": "RBC体积分布宽度CV", "bbox": [231, 840, 320, 856]},
	{"text": "血小板体积分布宽度", "bbox": [233, 873, 319, 889]}
]
2026-08-10 16:07:57,372 INFO     29 [qwen-vl-table] coord API: raw_items=20, valid_items=20, elapsed=6.2s
2026-08-10 16:07:57,373 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞计数*, bbox=[247, 250, 300, 267]
2026-08-10 16:07:57,373 INFO     29 [qwen-vl-table] coord item[1]: text=红细胞计数*, bbox=[247, 283, 300, 299]
2026-08-10 16:07:57,374 INFO     29 [qwen-vl-table] coord item[2]: text=血红蛋白*, bbox=[252, 316, 295, 332]
2026-08-10 16:07:57,374 INFO     29 [qwen-vl-table] coord item[3]: text=血小板计数*, bbox=[247, 349, 300, 365]
2026-08-10 16:07:57,374 INFO     29 [qwen-vl-table] coord item[4]: text=中性粒细胞百分比, bbox=[236, 381, 312, 397]
2026-08-10 16:07:57,374 INFO     29 [qwen-vl-table] coord item[5]: text=淋巴细胞百分比, bbox=[240, 414, 308, 430]
2026-08-10 16:07:57,374 INFO     29 [qwen-vl-table] coord item[6]: text=单核细胞百分比, bbox=[240, 447, 308, 463]
2026-08-10 16:07:57,374 INFO     29 [qwen-vl-table] coord item[7]: text=嗜酸性粒细胞百分比, bbox=[231, 479, 318, 495]
2026-08-10 16:07:57,374 INFO     29 [qwen-vl-table] coord item[8]: text=嗜碱性粒细胞百分比, bbox=[231, 512, 318, 528]
2026-08-10 16:07:57,374 INFO     29 [qwen-vl-table] coord item[9]: text=中性粒细胞绝对值, bbox=[236, 545, 312, 561]
2026-08-10 16:07:57,374 INFO     29 [qwen-vl-table] coord item[10]: text=淋巴细胞绝对值, bbox=[240, 577, 308, 593]
2026-08-10 16:07:57,374 INFO     29 [qwen-vl-table] coord item[11]: text=单核细胞绝对值, bbox=[240, 610, 308, 626]
2026-08-10 16:07:57,375 INFO     29 [qwen-vl-table] coord item[12]: text=嗜酸性粒细胞绝对值, bbox=[231, 643, 318, 659]
2026-08-10 16:07:57,375 INFO     29 [qwen-vl-table] coord item[13]: text=嗜碱性粒细胞绝对值, bbox=[231, 676, 318, 692]
2026-08-10 16:07:57,375 INFO     29 [qwen-vl-table] coord item[14]: text=平均红细胞体积*, bbox=[240, 708, 310, 724]
2026-08-10 16:07:57,375 INFO     29 [qwen-vl-table] coord item[15]: text=平均RBC血红蛋白含量*, bbox=[225, 741, 325, 757]
2026-08-10 16:07:57,375 INFO     29 [qwen-vl-table] coord item[16]: text=平均RBC血红蛋白浓度*, bbox=[225, 774, 325, 790]
2026-08-10 16:07:57,375 INFO     29 [qwen-vl-table] coord item[17]: text=红细胞比容*, bbox=[249, 807, 301, 823]
2026-08-10 16:07:57,375 INFO     29 [qwen-vl-table] coord item[18]: text=RBC体积分布宽度CV, bbox=[231, 840, 320, 856]
2026-08-10 16:07:57,375 INFO     29 [qwen-vl-table] coord item[19]: text=血小板体积分布宽度, bbox=[233, 873, 319, 889]
2026-08-10 16:07:57,376 INFO     29 [qwen-vl-table] page=21 coord: matched 20/20, time=6.2s
2026-08-10 16:07:57,376 INFO     29 [qwen-vl-table] new_positions (20):
[[22, 207.974, 252.6, 148.75, 158.86499999999998], [22, 207.974, 252.6, 168.385, 177.905], [22, 212.184, 248.39, 188.01999999999998, 197.54], [22, 207.974, 252.6, 207.655, 217.17499999999998], [22, 198.712, 262.704, 226.695, 236.215], [22, 202.07999999999998, 259.336, 246.32999999999998, 255.85], [22, 202.07999999999998, 259.336, 265.965, 275.485], [22, 194.50199999999998, 267.756, 285.005, 294.525], [22, 194.50199999999998, 267.756, 304.64, 314.15999999999997], [22, 198.712, 262.704, 324.275, 333.79499999999996], [22, 202.07999999999998, 259.336, 343.315, 352.835], [22, 202.07999999999998, 259.336, 362.95, 372.46999999999997], [22, 194.50199999999998, 267.756, 382.585, 392.10499999999996], [22, 194.50199999999998, 267.756, 402.21999999999997, 411.74], [22, 202.07999999999998, 261.02, 421.26, 430.78], [22, 189.45, 273.65, 440.895, 450.41499999999996], [22, 189.45, 273.65, 460.53, 470.04999999999995], [22, 209.658, 253.44199999999998, 480.16499999999996, 489.685], [22, 194.50199999999998, 269.44, 499.79999999999995, 509.32], [22, 196.186, 268.598, 519.435, 528.9549999999999]]
2026-08-10 16:07:57,376 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=20, matched=20, pages=1, time=17.9s
2026-08-10 16:07:57,378 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:07:57,379 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:07:57,379 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[22]
2026-08-10 16:07:57,379 INFO     29 [qwen-vl-table] positions ： [[22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:07:57,780 INFO     29 [qwen-vl-table] page=22, rect=842x595, img=(2339x1653)
2026-08-10 16:07:57,780 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:07:57,781 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2248, \"bbox_end\": 2274, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n\\hline\n\\multicolumn{1}{c}{\\textbf{缩写}} & \\multicolumn{1}{c}{\\textbf{项目名称}} & \\multicolumn{1}{c}{\\textbf{结果}} & \\multicolumn{1}{c}{\\textbf{结果提示}} & \\multicolumn{1}{c}{\\textbf{异常提示}} & \\multicolumn{1}{c}{\\textbf{辅助诊断}} & \\multicolumn{1}{c}{\\textbf{单位}} & \\multicolumn{1}{c}{\\textbf{参考范围}} \\\\\n\\hline\nFI02 & 吸氧浓度 & 21.00 & & & & \\% & 21-100 \\\\\nT & 体温 & 36.4 & & & & & 29-41 \\\\\nCa++ & 钙测定 & 1.19 & & & & mmol/L & 1.15-1.29 \\\\\nNa+ & 钠测定 & 143.20 & & & & mmol/L & 136-146 \\\\\nK+ & 钾测定 & 3.98 & & & & mmol/L & 3.5-4.5 \\\\\np02(a,T)/F02 & 氧合指数(p/f) & 315.0 & & $\\downarrow$ & & & 400-500 \\\\\nBEecf & 红细胞外剩余碱 & -1.80 & & & & mmol/l & -3-3 \\\\\nPH & 酸碱度 (PH) & 7.383 & & & & & 7.35-7.45 \\\\\npH(T) & pH校正值(pHT) & 7.392 & & & & & 7.35-7.45 \\\\\npO2 & 氧分压 (pO2) & 66.20 & & $\\downarrow$ & & mmHg & 83-108 \\\\\npO2(T) & 氧分压校正值 & 63.50 & & $\\downarrow$ & & mmHg & 83-108 \\\\\npCO2 & 二氧化碳分压 & 39.90 & & & & mmHg & 35-45 \\\\\nPCO2(T) & CO2分压校正 & 38.90 & & & & mmHg & 35-45 \\\\\nCl- & 氯测定 & 102.00 & & & & mmol/L & 98-106 \\\\\nHb & 血红蛋白测定(Hb) & 162.00 & & $\\uparrow$ & & g/L & 120-160 \\\\\nF02Hb & 氧合血红蛋白 & 92.0 & & $\\downarrow$ & & \\% & 94-98 \\\\\nMetHb & 高铁血红蛋白 & 0.10 & & & & & \\\\\ns02 & 总血氧饱和度 & 92.9 & & $\\downarrow$ & & \\% & 93-98 \\\\\nCOHb & CO红蛋白 & 1.00 & & & & \\% & 0-2 \\\\\nctCO2 & 血CO2含量 & 24.50 & & & & mmol/L & 24-32 \\\\\nFHHB & 还原血红蛋白 & 6.9 & & & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 16:07:57,783 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:07:57.783+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:08:11,346 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:08:11,347 INFO     29 [qwen-vl-table] page=22 LLM output (len=3564):
{
  "report_date": null,
  "items": [
    {
      "name": "吸氧浓度",
      "item_code": "FI02",
      "value": "21.00",
      "unit": "%",
      "reference_range": "21-100",
      "abnormal": false
    },
    {
      "name": "体温",
      "item_code": "T",
      "value": "36.4",
      "unit": null,
      "reference_range": "29-41",
      "abnormal": false
    },
    {
      "name": "钙测定",
      "item_code": "Ca++",
      "value": "1.19",
      "unit": "mmol/L",
      "reference_range": "1.15-1.29",
      "abnormal": false
    },
    {
      "name": "钠测定",
      "item_code": "Na+",
      "value": "143.20",
      "unit": "mmol/L",
      "reference_range": "136-146",
      "abnormal": false
    },
    {
      "name": "钾测定",
      "item_code": "K+",
      "value": "3.98",
      "unit": "mmol/L",
      "reference_range": "3.5-4.5",
      "abnormal": false
    },
    {
      "name": "氧合指数(p/f)",
      "item_code": "p02(a,T)/F02",
      "value": "315.0",
      "unit": null,
      "reference_range": "400-500",
      "abnormal": true
    },
    {
      "name": "红细胞外剩余碱",
      "item_code": "BEecf",
      "value": "-1.80",
      "unit": "mmol/l",
      "reference_range": "-3-3",
      "abnormal": false
    },
    {
      "name": "酸碱度 (PH)",
      "item_code": "PH",
      "value": "7.383",
      "unit": null,
      "reference_range": "7.35-7.45",
      "abnormal": false
    },
    {
      "name": "pH校正值(pHT)",
      "item_code": "pH(T)",
      "value": "7.392",
      "unit": null,
      "reference_range": "7.35-7.45",
      "abnormal": false
    },
    {
      "name": "氧分压 (pO2)",
      "item_code": "pO2",
      "value": "66.20",
      "unit": "mmHg",
      "reference_range": "83-108",
      "abnormal": true
    },
    {
      "name": "氧分压校正值",
      "item_code": "pO2(T)",
      "value": "63.50",
      "unit": "mmHg",
      "reference_range": "83-108",
      "abnormal": true
    },
    {
      "name": "二氧化碳分压",
      "item_code": "pCO2",
      "value": "39.90",
      "unit": "mmHg",
      "reference_range": "35-45",
      "abnormal": false
    },
    {
      "name": "CO2分压校正",
      "item_code": "PCO2(T)",
      "value": "38.90",
      "unit": "mmHg",
      "reference_range": "35-45",
      "abnormal": false
    },
    {
      "name": "氯测定",
      "item_code": "Cl-",
      "value": "102.00",
      "unit": "mmol/L",
      "reference_range": "98-106",
      "abnormal": false
    },
    {
      "name": "血红蛋白测定(Hb)",
      "item_code": "Hb",
      "value": "162.00",
      "unit": "g/L",
      "reference_range": "120-160",
      "abnormal": true
    },
    {
      "name": "氧合血红蛋白",
      "item_code": "F02Hb",
      "value": "92.0",
      "unit": "%",
      "reference_range": "94-98",
      "abnormal": true
    },
    {
      "name": "高铁血红蛋白",
      "item_code": "MetHb",
      "value": "0.10",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "总血氧饱和度",
      "item_code": "s02",
      "value": "92.9",
      "unit": "%",
      "reference_range": "93-98",
      "abnormal": true
    },
    {
      "name": "CO红蛋白",
      "item_code": "COHb",
      "value": "1.00",
      "unit": "%",
      "reference_range": "0-2",
      "abnormal": false
    },
    {
      "name": "血CO2含量",
      "item_code": "ctCO2",
      "value": "24.50",
      "unit": "mmol/L",
      "reference_range": "24-32",
      "abnormal": false
    },
    {
      "name": "还原血红蛋白",
      "item_code": "FHHB",
      "value": "6.9",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 16:08:11,347 INFO     29 [qwen-vl-table] coord grouping: {22: 21}
2026-08-10 16:08:11,365 INFO     29 [qwen-vl-table] coord API call start, page=22, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5775830, prompt_len=652
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
吸氧浓度、体温、钙测定、钠测定、钾测定、氧合指数(p/f)、红细胞外剩余碱、酸碱度 (PH)、pH校正值(pHT)、氧分压 (pO2)、氧分压校正值、二氧化碳分压、CO2分压校正、氯测定、血红蛋白测定(Hb)、氧合血红蛋白、高铁血红蛋白、总血氧饱和度、CO红蛋白、血CO2含量、还原血红蛋白

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
2026-08-10 16:08:17,718 INFO     29 [qwen-vl-table] coord API raw response (len=1072):
[
	{"text": "吸氧浓度", "bbox": [263, 246, 304, 262]},
	{"text": "体温", "bbox": [273, 278, 294, 293]},
	{"text": "钙测定", "bbox": [268, 311, 298, 326]},
	{"text": "钠测定", "bbox": [268, 344, 298, 359]},
	{"text": "钾测定", "bbox": [268, 376, 298, 391]},
	{"text": "氧合指数(p/f)", "bbox": [254, 408, 313, 423]},
	{"text": "红细胞外剩余碱", "bbox": [250, 440, 318, 455]},
	{"text": "酸碱度 (PH)", "bbox": [253, 472, 309, 487]},
	{"text": "pH校正值(pHT)", "bbox": [250, 504, 318, 519]},
	{"text": "氧分压 (pO2)", "bbox": [250, 536, 313, 551]},
	{"text": "氧分压校正值", "bbox": [255, 569, 314, 584]},
	{"text": "二氧化碳分压", "bbox": [255, 601, 314, 616]},
	{"text": "CO2分压校正", "bbox": [255, 633, 314, 648]},
	{"text": "氯测定", "bbox": [270, 666, 299, 681]},
	{"text": "血红蛋白测定(Hb)", "bbox": [246, 698, 324, 713]},
	{"text": "氧合血红蛋白", "bbox": [255, 730, 314, 745]},
	{"text": "高铁血红蛋白", "bbox": [255, 762, 314, 777]},
	{"text": "总血氧饱和度", "bbox": [255, 794, 314, 809]},
	{"text": "CO红蛋白", "bbox": [263, 827, 307, 842]},
	{"text": "血CO2含量", "bbox": [260, 858, 310, 873]},
	{"text": "还原血红蛋白", "bbox": [255, 890, 314, 905]}
]
2026-08-10 16:08:17,718 INFO     29 [qwen-vl-table] coord API: raw_items=21, valid_items=21, elapsed=6.4s
2026-08-10 16:08:17,718 INFO     29 [qwen-vl-table] coord item[0]: text=吸氧浓度, bbox=[263, 246, 304, 262]
2026-08-10 16:08:17,719 INFO     29 [qwen-vl-table] coord item[1]: text=体温, bbox=[273, 278, 294, 293]
2026-08-10 16:08:17,719 INFO     29 [qwen-vl-table] coord item[2]: text=钙测定, bbox=[268, 311, 298, 326]
2026-08-10 16:08:17,719 INFO     29 [qwen-vl-table] coord item[3]: text=钠测定, bbox=[268, 344, 298, 359]
2026-08-10 16:08:17,719 INFO     29 [qwen-vl-table] coord item[4]: text=钾测定, bbox=[268, 376, 298, 391]
2026-08-10 16:08:17,719 INFO     29 [qwen-vl-table] coord item[5]: text=氧合指数(p/f), bbox=[254, 408, 313, 423]
2026-08-10 16:08:17,719 INFO     29 [qwen-vl-table] coord item[6]: text=红细胞外剩余碱, bbox=[250, 440, 318, 455]
2026-08-10 16:08:17,719 INFO     29 [qwen-vl-table] coord item[7]: text=酸碱度 (PH), bbox=[253, 472, 309, 487]
2026-08-10 16:08:17,719 INFO     29 [qwen-vl-table] coord item[8]: text=pH校正值(pHT), bbox=[250, 504, 318, 519]
2026-08-10 16:08:17,719 INFO     29 [qwen-vl-table] coord item[9]: text=氧分压 (pO2), bbox=[250, 536, 313, 551]
2026-08-10 16:08:17,719 INFO     29 [qwen-vl-table] coord item[10]: text=氧分压校正值, bbox=[255, 569, 314, 584]
2026-08-10 16:08:17,719 INFO     29 [qwen-vl-table] coord item[11]: text=二氧化碳分压, bbox=[255, 601, 314, 616]
2026-08-10 16:08:17,719 INFO     29 [qwen-vl-table] coord item[12]: text=CO2分压校正, bbox=[255, 633, 314, 648]
2026-08-10 16:08:17,719 INFO     29 [qwen-vl-table] coord item[13]: text=氯测定, bbox=[270, 666, 299, 681]
2026-08-10 16:08:17,719 INFO     29 [qwen-vl-table] coord item[14]: text=血红蛋白测定(Hb), bbox=[246, 698, 324, 713]
2026-08-10 16:08:17,719 INFO     29 [qwen-vl-table] coord item[15]: text=氧合血红蛋白, bbox=[255, 730, 314, 745]
2026-08-10 16:08:17,719 INFO     29 [qwen-vl-table] coord item[16]: text=高铁血红蛋白, bbox=[255, 762, 314, 777]
2026-08-10 16:08:17,720 INFO     29 [qwen-vl-table] coord item[17]: text=总血氧饱和度, bbox=[255, 794, 314, 809]
2026-08-10 16:08:17,720 INFO     29 [qwen-vl-table] coord item[18]: text=CO红蛋白, bbox=[263, 827, 307, 842]
2026-08-10 16:08:17,720 INFO     29 [qwen-vl-table] coord item[19]: text=血CO2含量, bbox=[260, 858, 310, 873]
2026-08-10 16:08:17,720 INFO     29 [qwen-vl-table] coord item[20]: text=还原血红蛋白, bbox=[255, 890, 314, 905]
2026-08-10 16:08:17,722 INFO     29 [qwen-vl-table] page=22 coord: matched 21/21, time=6.4s
2026-08-10 16:08:17,722 INFO     29 [qwen-vl-table] new_positions (21):
[[23, 221.446, 255.968, 146.37, 155.89], [23, 229.86599999999999, 247.548, 165.41, 174.33499999999998], [23, 225.656, 250.916, 185.045, 193.97], [23, 225.656, 250.916, 204.67999999999998, 213.605], [23, 225.656, 250.916, 223.72, 232.64499999999998], [23, 213.868, 263.546, 242.76, 251.685], [23, 210.5, 267.756, 261.8, 270.72499999999997], [23, 213.02599999999998, 260.178, 280.84, 289.765], [23, 210.5, 267.756, 299.88, 308.805], [23, 210.5, 263.546, 318.91999999999996, 327.84499999999997], [23, 214.70999999999998, 264.388, 338.555, 347.47999999999996], [23, 214.70999999999998, 264.388, 357.59499999999997, 366.52], [23, 214.70999999999998, 264.388, 376.635, 385.56], [23, 227.34, 251.75799999999998, 396.27, 405.195], [23, 207.132, 272.808, 415.31, 424.23499999999996], [23, 214.70999999999998, 264.388, 434.34999999999997, 443.275], [23, 214.70999999999998, 264.388, 453.39, 462.315], [23, 214.70999999999998, 264.388, 472.43, 481.35499999999996], [23, 221.446, 258.49399999999997, 492.065, 500.98999999999995], [23, 218.92, 261.02, 510.51, 519.435], [23, 214.70999999999998, 264.388, 529.55, 538.475]]
2026-08-10 16:08:17,723 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=21, matched=21, pages=1, time=20.3s
2026-08-10 16:08:17,725 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:08:17,727 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:08:17,727 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[23]
2026-08-10 16:08:17,727 INFO     29 [qwen-vl-table] positions ： [[23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:08:18,124 INFO     29 [qwen-vl-table] page=23, rect=842x595, img=(2339x1653)
2026-08-10 16:08:18,124 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:08:18,124 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2275, \"bbox_end\": 2301, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n\\hline\n缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 \\\\\n\\hline\nPH & 酸碱度 (PH) & 7.383 & & & & & 7.35-7.45 \\\\\npH(T) & pH校正值(pHT) & 7.392 & & & & & 7.35-7.45 \\\\\npO2 & 氧分压 (pO2) & 66.20 & & $\\downarrow$ & & mmHg & 83-108 \\\\\npO2(T) & 氧分压校正值 & 63.50 & & $\\downarrow$ & & mmHg & 83-108 \\\\\npCO2 & 二氧化碳分压 & 39.90 & & & & mmHg & 35-45 \\\\\nPCO2(T) & CO2分压校正 & 38.90 & & & & mmHg & 35-45 \\\\\nCl- & 氯测定 & 102.00 & & & & mmol/L & 98-106 \\\\\nHb & 血红蛋白测定(Hb) & 162.00 & & $\\uparrow$ & & g/L & 120-160 \\\\\nF02Hb & 氧合血红蛋白 & 92.0 & & $\\downarrow$ & & \\% & 94-98 \\\\\nMetHb & 高铁血红蛋白 & 0.10 & & & & & \\\\\ns02 & 总血氧饱和度 & 92.9 & & $\\downarrow$ & & \\% & 93-98 \\\\\nC0Hb & CO红蛋白 & 1.00 & & & & \\% & 0-2 \\\\\nctCO2 & 血CO2含量 & 24.50 & & & & mmol/L & 24-32 \\\\\nFHHB & 还原血红蛋白 & 6.9 & & & & \\% & 2-7 \\\\\ncHCO3 & 标准碳酸氢根 & 23.00 & & & & mmol/L & 22-26 \\\\\nABE (BE(B)) & 实际剩余碱 & -1.6 & & & & mmol/L & -3-3 \\\\\nHCO3- & 实际碳酸氢根 & 23.20 & & & & mmol/L & \\\\\nP02(A-a,T)e & 肺泡动脉氧分压差 & 36.0 & & $\\uparrow$ & & mmHg & 10-25 \\\\\nP02(a/A,T) & 动脉与肺泡氧分压比 & 64.0 & & $\\downarrow$ & & \\% & 85-95 \\\\\nRI & 呼吸指数 & 57.0 & & & & & \\\\\nGlu & 葡萄糖测定 & 6.70 & & $\\uparrow$ & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 16:08:29,646 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:08:29.644+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:08:29,663 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:08:29,663 INFO     29 [qwen-vl-table] page=23 LLM output (len=3565):
{
  "report_date": null,
  "items": [
    {
      "name": "酸碱度 (PH)",
      "item_code": "PH",
      "value": "7.383",
      "unit": null,
      "reference_range": "7.35-7.45",
      "abnormal": false
    },
    {
      "name": "pH校正值(pHT)",
      "item_code": "pH(T)",
      "value": "7.392",
      "unit": null,
      "reference_range": "7.35-7.45",
      "abnormal": false
    },
    {
      "name": "氧分压 (pO2)",
      "item_code": "pO2",
      "value": "66.20",
      "unit": "mmHg",
      "reference_range": "83-108",
      "abnormal": true
    },
    {
      "name": "氧分压校正值",
      "item_code": "pO2(T)",
      "value": "63.50",
      "unit": "mmHg",
      "reference_range": "83-108",
      "abnormal": true
    },
    {
      "name": "二氧化碳分压",
      "item_code": "pCO2",
      "value": "39.90",
      "unit": "mmHg",
      "reference_range": "35-45",
      "abnormal": false
    },
    {
      "name": "CO2分压校正",
      "item_code": "PCO2(T)",
      "value": "38.90",
      "unit": "mmHg",
      "reference_range": "35-45",
      "abnormal": false
    },
    {
      "name": "氯测定",
      "item_code": "Cl-",
      "value": "102.00",
      "unit": "mmol/L",
      "reference_range": "98-106",
      "abnormal": false
    },
    {
      "name": "血红蛋白测定(Hb)",
      "item_code": "Hb",
      "value": "162.00",
      "unit": "g/L",
      "reference_range": "120-160",
      "abnormal": true
    },
    {
      "name": "氧合血红蛋白",
      "item_code": "F02Hb",
      "value": "92.0",
      "unit": "%",
      "reference_range": "94-98",
      "abnormal": true
    },
    {
      "name": "高铁血红蛋白",
      "item_code": "MetHb",
      "value": "0.10",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "总血氧饱和度",
      "item_code": "s02",
      "value": "92.9",
      "unit": "%",
      "reference_range": "93-98",
      "abnormal": true
    },
    {
      "name": "CO红蛋白",
      "item_code": "C0Hb",
      "value": "1.00",
      "unit": "%",
      "reference_range": "0-2",
      "abnormal": false
    },
    {
      "name": "血CO2含量",
      "item_code": "ctCO2",
      "value": "24.50",
      "unit": "mmol/L",
      "reference_range": "24-32",
      "abnormal": false
    },
    {
      "name": "还原血红蛋白",
      "item_code": "FHHB",
      "value": "6.9",
      "unit": "%",
      "reference_range": "2-7",
      "abnormal": false
    },
    {
      "name": "标准碳酸氢根",
      "item_code": "cHCO3",
      "value": "23.00",
      "unit": "mmol/L",
      "reference_range": "22-26",
      "abnormal": false
    },
    {
      "name": "实际剩余碱",
      "item_code": "ABE (BE(B))",
      "value": "-1.6",
      "unit": "mmol/L",
      "reference_range": "-3-3",
      "abnormal": false
    },
    {
      "name": "实际碳酸氢根",
      "item_code": "HCO3-",
      "value": "23.20",
      "unit": "mmol/L",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "肺泡动脉氧分压差",
      "item_code": "P02(A-a,T)e",
      "value": "36.0",
      "unit": "mmHg",
      "reference_range": "10-25",
      "abnormal": true
    },
    {
      "name": "动脉与肺泡氧分压比",
      "item_code": "P02(a/A,T)",
      "value": "64.0",
      "unit": "%",
      "reference_range": "85-95",
      "abnormal": true
    },
    {
      "name": "呼吸指数",
      "item_code": "RI",
      "value": "57.0",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "葡萄糖测定",
      "item_code": "Glu",
      "value": "6.70",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    }
  ]
}
2026-08-10 16:08:29,663 INFO     29 [qwen-vl-table] coord grouping: {23: 21}
2026-08-10 16:08:29,678 INFO     29 [qwen-vl-table] coord API call start, page=23, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5930452, prompt_len=664
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
酸碱度 (PH)、pH校正值(pHT)、氧分压 (pO2)、氧分压校正值、二氧化碳分压、CO2分压校正、氯测定、血红蛋白测定(Hb)、氧合血红蛋白、高铁血红蛋白、总血氧饱和度、CO红蛋白、血CO2含量、还原血红蛋白、标准碳酸氢根、实际剩余碱、实际碳酸氢根、肺泡动脉氧分压差、动脉与肺泡氧分压比、呼吸指数、葡萄糖测定

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
2026-08-10 16:08:37,954 INFO     29 [qwen-vl-table] coord API raw response (len=1084):
[
	{"text": "酸碱度 (PH)", "bbox": [248, 246, 306, 262]},
	{"text": "pH校正值(pHT)", "bbox": [245, 277, 315, 293]},
	{"text": "氧分压 (pO2)", "bbox": [245, 310, 309, 326]},
	{"text": "氧分压校正值", "bbox": [250, 342, 310, 358]},
	{"text": "二氧化碳分压", "bbox": [250, 374, 310, 390]},
	{"text": "CO2分压校正", "bbox": [250, 406, 310, 422]},
	{"text": "氯测定", "bbox": [265, 438, 296, 454]},
	{"text": "血红蛋白测定(Hb)", "bbox": [242, 469, 320, 485]},
	{"text": "氧合血红蛋白", "bbox": [251, 501, 310, 517]},
	{"text": "高铁血红蛋白", "bbox": [251, 533, 310, 549]},
	{"text": "总血氧饱和度", "bbox": [251, 565, 310, 581]},
	{"text": "CO红蛋白", "bbox": [259, 597, 303, 613]},
	{"text": "血CO2含量", "bbox": [256, 629, 307, 645]},
	{"text": "还原血红蛋白", "bbox": [252, 661, 310, 677]},
	{"text": "标准碳酸氢根", "bbox": [252, 693, 310, 709]},
	{"text": "实际剩余碱", "bbox": [257, 725, 307, 741]},
	{"text": "实际碳酸氢根", "bbox": [252, 757, 310, 773]},
	{"text": "肺泡动脉氧分压差", "bbox": [243, 789, 321, 805]},
	{"text": "动脉与肺泡氧分压比", "bbox": [238, 821, 325, 837]},
	{"text": "呼吸指数", "bbox": [262, 853, 302, 869]},
	{"text": "葡萄糖测定", "bbox": [257, 885, 307, 901]}
]
2026-08-10 16:08:37,955 INFO     29 [qwen-vl-table] coord API: raw_items=21, valid_items=21, elapsed=8.3s
2026-08-10 16:08:37,955 INFO     29 [qwen-vl-table] coord item[0]: text=酸碱度 (PH), bbox=[248, 246, 306, 262]
2026-08-10 16:08:37,955 INFO     29 [qwen-vl-table] coord item[1]: text=pH校正值(pHT), bbox=[245, 277, 315, 293]
2026-08-10 16:08:37,955 INFO     29 [qwen-vl-table] coord item[2]: text=氧分压 (pO2), bbox=[245, 310, 309, 326]
2026-08-10 16:08:37,955 INFO     29 [qwen-vl-table] coord item[3]: text=氧分压校正值, bbox=[250, 342, 310, 358]
2026-08-10 16:08:37,955 INFO     29 [qwen-vl-table] coord item[4]: text=二氧化碳分压, bbox=[250, 374, 310, 390]
2026-08-10 16:08:37,955 INFO     29 [qwen-vl-table] coord item[5]: text=CO2分压校正, bbox=[250, 406, 310, 422]
2026-08-10 16:08:37,955 INFO     29 [qwen-vl-table] coord item[6]: text=氯测定, bbox=[265, 438, 296, 454]
2026-08-10 16:08:37,955 INFO     29 [qwen-vl-table] coord item[7]: text=血红蛋白测定(Hb), bbox=[242, 469, 320, 485]
2026-08-10 16:08:37,955 INFO     29 [qwen-vl-table] coord item[8]: text=氧合血红蛋白, bbox=[251, 501, 310, 517]
2026-08-10 16:08:37,955 INFO     29 [qwen-vl-table] coord item[9]: text=高铁血红蛋白, bbox=[251, 533, 310, 549]
2026-08-10 16:08:37,955 INFO     29 [qwen-vl-table] coord item[10]: text=总血氧饱和度, bbox=[251, 565, 310, 581]
2026-08-10 16:08:37,955 INFO     29 [qwen-vl-table] coord item[11]: text=CO红蛋白, bbox=[259, 597, 303, 613]
2026-08-10 16:08:37,955 INFO     29 [qwen-vl-table] coord item[12]: text=血CO2含量, bbox=[256, 629, 307, 645]
2026-08-10 16:08:37,955 INFO     29 [qwen-vl-table] coord item[13]: text=还原血红蛋白, bbox=[252, 661, 310, 677]
2026-08-10 16:08:37,955 INFO     29 [qwen-vl-table] coord item[14]: text=标准碳酸氢根, bbox=[252, 693, 310, 709]
2026-08-10 16:08:37,956 INFO     29 [qwen-vl-table] coord item[15]: text=实际剩余碱, bbox=[257, 725, 307, 741]
2026-08-10 16:08:37,956 INFO     29 [qwen-vl-table] coord item[16]: text=实际碳酸氢根, bbox=[252, 757, 310, 773]
2026-08-10 16:08:37,956 INFO     29 [qwen-vl-table] coord item[17]: text=肺泡动脉氧分压差, bbox=[243, 789, 321, 805]
2026-08-10 16:08:37,956 INFO     29 [qwen-vl-table] coord item[18]: text=动脉与肺泡氧分压比, bbox=[238, 821, 325, 837]
2026-08-10 16:08:37,956 INFO     29 [qwen-vl-table] coord item[19]: text=呼吸指数, bbox=[262, 853, 302, 869]
2026-08-10 16:08:37,956 INFO     29 [qwen-vl-table] coord item[20]: text=葡萄糖测定, bbox=[257, 885, 307, 901]
2026-08-10 16:08:37,958 INFO     29 [qwen-vl-table] page=23 coord: matched 21/21, time=8.3s
2026-08-10 16:08:37,958 INFO     29 [qwen-vl-table] new_positions (21):
[[24, 208.816, 257.652, 146.37, 155.89], [24, 206.29, 265.23, 164.815, 174.33499999999998], [24, 206.29, 260.178, 184.45, 193.97], [24, 210.5, 261.02, 203.48999999999998, 213.01], [24, 210.5, 261.02, 222.53, 232.04999999999998], [24, 210.5, 261.02, 241.57, 251.08999999999997], [24, 223.13, 249.232, 260.61, 270.13], [24, 203.76399999999998, 269.44, 279.055, 288.575], [24, 211.34199999999998, 261.02, 298.09499999999997, 307.615], [24, 211.34199999999998, 261.02, 317.135, 326.655], [24, 211.34199999999998, 261.02, 336.175, 345.695], [24, 218.078, 255.126, 355.215, 364.73499999999996], [24, 215.552, 258.49399999999997, 374.255, 383.775], [24, 212.184, 261.02, 393.29499999999996, 402.815], [24, 212.184, 261.02, 412.335, 421.85499999999996], [24, 216.394, 258.49399999999997, 431.375, 440.895], [24, 212.184, 261.02, 450.41499999999996, 459.935], [24, 204.606, 270.282, 469.455, 478.97499999999997], [24, 200.396, 273.65, 488.495, 498.015], [24, 220.60399999999998, 254.284, 507.53499999999997, 517.055], [24, 216.394, 258.49399999999997, 526.5749999999999, 536.095]]
2026-08-10 16:08:37,959 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=21, matched=21, pages=1, time=20.2s
2026-08-10 16:08:37,962 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:08:37,964 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:08:37,964 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[24, 25]
2026-08-10 16:08:37,964 INFO     29 [qwen-vl-table] positions ： [[24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:08:38,183 INFO     29 [qwen-vl-table] page=24, rect=595x842, img=(1653x2339)
2026-08-10 16:08:38,362 INFO     29 [qwen-vl-table] page=25, rect=595x842, img=(1653x2339)
2026-08-10 16:08:38,363 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:08:38,363 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2302, \"bbox_end\": 2385, \"encounter_dates\": [\"2026-03-10\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "临床诊断：肺癌\n样本采集时间：2026-03-10\n检测项目\n本产品对与肺癌密切相关的68个基因进行高通量测序。检测突变形式为点突变(SNV)、小片段插入缺失(INDEL)、拷贝数变异(CNV)以及融合(FUSION)。通过免疫组化检测PD-L1表达。\n本报告分析基因变异与靶向药物、化疗药物的相关性，给出靶向药物(FDA/NMPA批准药物、临床试验\n药物等)、化疗药物的用药提示信息，从而为临床制定治疗方案提供参考信息。\n注：检测基因列表见附录。\n检测结果小结\n检测类型\n检测结果\n靶向用药指导\n共检出3个变异位点,其中3个与靶向药物相关(KRAS\np.G12V; CDKN2A p.R80*; TP53 p.G279E)\nPD-L1蛋白表达水平\n使用CSTE1L3N抗体; TPS:<1%, CPS:1\n化疗药物检测\n详见“化疗药物检测解析”部分\n样品总体质量评估\n合格\n注:\n1. 本报告为基因检测结果,基因、药物等信息列举未按照重要性排序。\n2. 本报告只对本次采集样本负责,如有疑问,请在7个工作日内与我们联系。\n检测人:\n张紫叶\n复核人:\n王建丽\n日期:\n2026-03-16\n日期:\n2026-03-16\n1/26\n孔令祈 Novogene\n诺禾致源\n肺癌精准诊疗相关基因结果汇总\n基因\n变异类型\n检测结果\n变异丰度/拷贝数\nALK\n突变/融合\n未检测到与用药相关突变\nBRAF",
    "role": "user"
  }
]
2026-08-10 16:08:42,051 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:08:42,052 INFO     29 [qwen-vl-table] page=24 LLM output (len=1017):
{
  "report_date": "2026-03-16",
  "items": [
    {
      "name": "KRAS",
      "item_code": null,
      "value": "p.G12V",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "CDKN2A",
      "item_code": null,
      "value": "p.R80*",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "TP53",
      "item_code": null,
      "value": "p.G279E",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "PD-L1 TPS",
      "item_code": "TPS",
      "value": "<1%",
      "unit": "%",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "PD-L1 CPS",
      "item_code": "CPS",
      "value": "1",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "ALK",
      "item_code": null,
      "value": "未检测到与用药相关突变",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 16:08:42,052 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:08:42,053 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2302, \"bbox_end\": 2385, \"encounter_dates\": [\"2026-03-10\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "突变/融合\n未检测到与用药相关突变\nBRCA1\n突变/缺失\n未检测到与用药相关突变\nBRCA2\n突变/缺失\n未检测到与用药相关突变\nEGFR\n突变\n未检测到与用药相关突变\nERBB2(HER2)\n突变/扩增\n未检测到与用药相关突变\nFGFR2\n突变/融合\n未检测到与用药相关突变\nFGFR3\n突变/融合\n未检测到与用药相关突变\nKIT\n突变\n未检测到与用药相关突变\nKRAS\n突变\nNM_033360.4 exon2 c.35G>T p.G12V\n35.80%\nMET\n突变/扩增/14号外\n未检测到与用药相关突变\n显子跳跃\nNRG1\n融合\n未检测到与用药相关突变\nNTRK1\n融合\n未检测到与用药相关突变\n广西金域医学检验实验室\n本报告单经过电子签名认证\nGuangxi Kingmed Center for Clinical Laboratory\n金域医学\nKingMed Diagnostics",
    "role": "user"
  }
]
2026-08-10 16:08:47,431 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:08:47,431 INFO     29 [qwen-vl-table] page=25 LLM output (len=1894):
{
  "report_date": null,
  "items": [
    {
      "name": "BRCA1",
      "item_code": null,
      "value": "未检测到与用药相关突变",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "BRCA2",
      "item_code": null,
      "value": "未检测到与用药相关突变",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "EGFR",
      "item_code": null,
      "value": "未检测到与用药相关突变",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "ERBB2(HER2)",
      "item_code": null,
      "value": "未检测到与用药相关突变",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "FGFR2",
      "item_code": null,
      "value": "未检测到与用药相关突变",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "FGFR3",
      "item_code": null,
      "value": "未检测到与用药相关突变",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "KIT",
      "item_code": null,
      "value": "未检测到与用药相关突变",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "KRAS",
      "item_code": null,
      "value": "NM_033360.4 exon2 c.35G>T p.G12V 35.80%",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "MET",
      "item_code": null,
      "value": "未检测到与用药相关突变",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "NRG1",
      "item_code": null,
      "value": "未检测到与用药相关突变",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "NTRK1",
      "item_code": null,
      "value": "未检测到与用药相关突变",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 16:08:47,431 INFO     29 [qwen-vl-table] coord grouping: {24: 17}
2026-08-10 16:08:47,436 INFO     29 [qwen-vl-table] coord API call start, page=24, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1313362, prompt_len=612
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
KRAS、CDKN2A、TP53、PD-L1 TPS、PD-L1 CPS、ALK、BRCA1、BRCA2、EGFR、ERBB2(HER2)、FGFR2、FGFR3、KIT、KRAS、MET、NRG1、NTRK1

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
2026-08-10 16:08:52,507 INFO     29 [qwen-vl-table] coord API raw response (len=868):
```json
[
	{"text": "KRAS", "bbox": [484, 193, 814, 204]},
	{"text": "CDKN2A", "bbox": [530, 206, 630, 217]},
	{"text": "TP53", "bbox": [635, 206, 730, 217]},
	{"text": "PD-L1 TPS", "bbox": [578, 224, 694, 235]},
	{"text": "PD-L1 CPS", "bbox": [705, 224, 750, 235]},
	{"text": "ALK", "bbox": [226, 681, 255, 691]},
	{"text": "BRCA1", "bbox": [217, 720, 262, 730]},
	{"text": "BRCA2", "bbox": [217, 739, 263, 749]},
	{"text": "EGFR", "bbox": [222, 758, 258, 768]},
	{"text": "ERBB2(HER2)", "bbox": [196, 777, 285, 787]},
	{"text": "FGFR2", "bbox": [219, 796, 262, 806]},
	{"text": "FGFR3", "bbox": [219, 815, 262, 825]},
	{"text": "KIT", "bbox": [229, 834, 253, 844]},
	{"text": "KRAS", "bbox": [222, 853, 259, 863]},
	{"text": "MET", "bbox": [226, 878, 255, 888]},
	{"text": "NRG1", "bbox": [222, 905, 258, 915]},
	{"text": "NTRK1", "bbox": [217, 924, 262, 934]}
]
```
2026-08-10 16:08:52,508 INFO     29 [qwen-vl-table] coord API: raw_items=17, valid_items=17, elapsed=5.1s
2026-08-10 16:08:52,508 INFO     29 [qwen-vl-table] coord item[0]: text=KRAS, bbox=[484, 193, 814, 204]
2026-08-10 16:08:52,508 INFO     29 [qwen-vl-table] coord item[1]: text=CDKN2A, bbox=[530, 206, 630, 217]
2026-08-10 16:08:52,508 INFO     29 [qwen-vl-table] coord item[2]: text=TP53, bbox=[635, 206, 730, 217]
2026-08-10 16:08:52,508 INFO     29 [qwen-vl-table] coord item[3]: text=PD-L1 TPS, bbox=[578, 224, 694, 235]
2026-08-10 16:08:52,508 INFO     29 [qwen-vl-table] coord item[4]: text=PD-L1 CPS, bbox=[705, 224, 750, 235]
2026-08-10 16:08:52,508 INFO     29 [qwen-vl-table] coord item[5]: text=ALK, bbox=[226, 681, 255, 691]
2026-08-10 16:08:52,508 INFO     29 [qwen-vl-table] coord item[6]: text=BRCA1, bbox=[217, 720, 262, 730]
2026-08-10 16:08:52,509 INFO     29 [qwen-vl-table] coord item[7]: text=BRCA2, bbox=[217, 739, 263, 749]
2026-08-10 16:08:52,509 INFO     29 [qwen-vl-table] coord item[8]: text=EGFR, bbox=[222, 758, 258, 768]
2026-08-10 16:08:52,509 INFO     29 [qwen-vl-table] coord item[9]: text=ERBB2(HER2), bbox=[196, 777, 285, 787]
2026-08-10 16:08:52,509 INFO     29 [qwen-vl-table] coord item[10]: text=FGFR2, bbox=[219, 796, 262, 806]
2026-08-10 16:08:52,509 INFO     29 [qwen-vl-table] coord item[11]: text=FGFR3, bbox=[219, 815, 262, 825]
2026-08-10 16:08:52,509 INFO     29 [qwen-vl-table] coord item[12]: text=KIT, bbox=[229, 834, 253, 844]
2026-08-10 16:08:52,509 INFO     29 [qwen-vl-table] coord item[13]: text=KRAS, bbox=[222, 853, 259, 863]
2026-08-10 16:08:52,509 INFO     29 [qwen-vl-table] coord item[14]: text=MET, bbox=[226, 878, 255, 888]
2026-08-10 16:08:52,509 INFO     29 [qwen-vl-table] coord item[15]: text=NRG1, bbox=[222, 905, 258, 915]
2026-08-10 16:08:52,509 INFO     29 [qwen-vl-table] coord item[16]: text=NTRK1, bbox=[217, 924, 262, 934]
2026-08-10 16:08:52,510 INFO     29 [qwen-vl-table] page=24 coord: matched 17/17, time=5.1s
2026-08-10 16:08:52,510 INFO     29 [qwen-vl-table] new_positions (17):
[[25, 132.09, 154.105, 718.226, 726.646], [25, 315.34999999999997, 374.84999999999997, 173.452, 182.714], [25, 377.825, 434.34999999999997, 173.452, 182.714], [25, 343.90999999999997, 412.93, 188.608, 197.87], [25, 419.47499999999997, 446.25, 188.608, 197.87], [25, 134.47, 151.725, 573.4019999999999, 581.822], [25, 129.11499999999998, 155.89, 606.24, 614.66], [25, 129.11499999999998, 156.48499999999999, 622.2379999999999, 630.658], [25, 132.09, 153.51, 638.236, 646.656], [25, 116.61999999999999, 169.575, 654.2339999999999, 662.654], [25, 130.305, 155.89, 670.232, 678.6519999999999], [25, 130.305, 155.89, 686.23, 694.65], [25, 136.255, 150.535, 702.228, 710.648], [25, 132.09, 154.105, 718.226, 726.646], [25, 134.47, 151.725, 739.276, 747.696], [25, 132.09, 153.51, 762.01, 770.43], [25, 129.11499999999998, 155.89, 778.0079999999999, 786.428]]
2026-08-10 16:08:52,510 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=17, matched=17, pages=2, time=14.5s
2026-08-10 16:08:52,531 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 16:08:52,532 INFO     29 [Trace] task=5212989c | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Extractor:LabExam | outputs={"chunks": "11 items, types={'LabReport': 11}", "html": "", "json": "2438 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 11}"}
2026-08-10 16:08:52,532 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 16:08:52,541 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:08:52,541 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 16:08:53,367 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:08:53,376 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 16:08:53,376 INFO     29 [Trace] task=5212989c | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "2438 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 11}"}
2026-08-10 16:08:53,376 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 16:08:53,383 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:08:53,383 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 16:08:53,865 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:08:53,875 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 16:08:53,876 INFO     29 [Trace] task=5212989c | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Extractor:Clinical | outputs={"chunks": "1 items", "html": "", "json": "2438 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 11}"}
2026-08-10 16:08:53,876 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 16:08:53,885 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:08:53,886 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 16:08:54,612 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:08:54,624 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 16:08:54,625 INFO     29 [Trace] task=5212989c | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "2438 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 11}"}
2026-08-10 16:08:54,625 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 16:08:54,637 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:08:54,637 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 16:08:55,055 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:08:55,071 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 16:08:55,072 INFO     29 [Trace] task=5212989c | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "2438 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 11}"}
2026-08-10 16:08:55,072 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 16:08:55,081 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:08:55,081 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 16:08:55,500 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:08:55,508 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 16:08:55,508 INFO     29 [Trace] task=5212989c | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "2438 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 11}"}
2026-08-10 16:08:55,508 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 16:08:55,517 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:08:55,518 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:08:55,518 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-10 16:08:55,518 INFO     29 [qwen-vl-text] positions(1074): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:08:55,519 INFO     29 [qwen-vl-text] page grouping: [0, 1, 2, 3, 4, 5, 6, 7, 8], lines per page: [27, 21, 31, 864, 44, 25, 23, 34, 5]
2026-08-10 16:08:55,920 INFO     29 [qwen-vl-text] page=0, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 16:08:56,202 INFO     29 [qwen-vl-text] page=1, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 16:08:56,614 INFO     29 [qwen-vl-text] page=2, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 16:08:57,027 INFO     29 [qwen-vl-text] page=3, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 16:08:57,437 INFO     29 [qwen-vl-text] page=4, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 16:08:57,797 INFO     29 [qwen-vl-text] page=5, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 16:08:58,163 INFO     29 [qwen-vl-text] page=6, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 16:08:58,563 INFO     29 [qwen-vl-text] page=7, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 16:08:58,965 INFO     29 [qwen-vl-text] page=8, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 16:08:58,968 INFO     29 [qwen-vl-text] LLM extraction start, text_len=19464
2026-08-10 16:08:58,968 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:08:58,968 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 0, \"bbox_end\": 1073, \"encounter_dates\": [\"2026-02-28\"], \"department\": \"老年医学呼吸内科\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "病史\n主诉：咳嗽、咳痰1月余\n现病史：患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、\n呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。至当地医院体检发现肺部阴影，具体不详。2026-02-26至中\n山大学附属第一医院广西医院就诊，查胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm\n，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋\n巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。具体诊治不详。为进一步治疗，遂\n至我院门诊就诊，门诊拟“肺占位性病变”收治入院。自发病以来，患者精神、食欲、睡眠正常，大小便正\n常，体重无明显变化。\n既往史：平素健康状况：良好。\n既往病史：否认高血压、冠心病、糖尿病史。\n传染病史：否，否认肝炎、结核或其他传染病史。\n预防接种史：正规。\n过敏史：否认过敏史。\n外伤史：否认外伤史。\n手术史：2年前曾行尿道结石手术，具体不详。\n输血史：否认输血史。\n系统回顾：无特殊。\n个人史：出生地：广西壮族自治区南宁市青秀区\n地方病地区居住情况：无\n冶游史：否认冶游史\n职业与工作条件有无工业毒物、粉尘、放射性物质及接触史：无\n广西医科大学第一附属医院 孔令祈\n11:24\n2026-03-19\n姜晓红 (D450199...\n姜晓红 (D450199...\n烟酒嗜好及药物使用史：有吸烟史，约10支/天，已吸烟40年，否认饮酒史。\n婚姻史：有婚姻史，结婚年龄：适龄结婚。有生育史，育有1子。\n家族史：否认相似家族病史及遗传病史。\n请患者或病史叙述者仔细确认以上病史记录并签字：[患者]\n体格检查\n一般情况：\n体温：36.8℃\n脉搏：75次/分\n呼吸：21次/分\n血压：138/72mmHg\n身高：161CM\n体重：74kg\n发育：正常\n营养：良好\n神志：清楚\n体位：自主体位\n面容：正常面容\n表情：自如\n步态：正常\n体型：正力型\n配合检查：合作\n皮肤黏膜:\n色\n泽:正常\n皮\n疹:全身皮肤未见皮疹\n皮下出血:全身皮肤未见皮下出血\n毛发分布:毛发分布正常\n温度与湿度:温度、湿度、弹性均正常\n水\n肿:未见水肿\n肝\n掌:无\n蜘\n蛛\n痣:未见蜘蛛痣\n其他表现:无\n淋巴结:全身浅表淋巴结未扪及肿大\n头部:\n头颅:头颅大小正常,无畸形\n眼:眉毛,眼睑,结膜,眼球未见异常,双侧巩膜无黄染\n耳:双耳外观未见异常,乳突无压痛,外耳道未见分泌物\n鼻:鼻部外观未见异常,鼻翼无扇动,鼻腔无分泌物,鼻窦区无压痛\n咽喉:双侧扁桃体未见肿大,表面未见脓性分泌物,咽未见异常,声音正常\n口腔:唇,舌,牙齿,牙龈正常\n颈部:\n颈部运动:颈软无抵抗\n颈静脉:无怒张\n气管:居中\n颈动脉搏动:正常\n肝-颈静脉回流征:阴性\n广西医科大:\n预览 验证CA签名 手工解锁 删除 病历参考 更新数据 加载全部病程 个人模板管理 返回\n20部：\n003470 20.2.11\n003470 20.2.11\n003470 20.2.11\n003470 20.2.11\n胸部：胸廓对称无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常\n肺部：\n视诊：双侧呼吸运动均匀对称，无增强或者减弱\n触诊：双肺触觉语颤对称无异常，未触及胸膜摩擦感\n叩诊：双肺叩诊呈清音\n听诊：双肺呼吸音清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音\n心脏：\n视诊：心尖搏动未见异常，位于左侧第五肋间锁骨中线内0.5cm，无异常隆起及凹陷\n触诊：心尖搏动未触及异常，未触及震颤及心包摩擦感\n叩诊：心界不大\n听诊：心率：75次/分，心律：齐 A2 > P2\n心音 S1：有力， 心音 S2：有力， 心音 S3：无， 心音 S4：无\n杂音：各瓣膜区未闻及杂音\n额外心音：无\n心包摩擦音：无\n周围血管：未见异常血管征\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41\n编辑\n功能\n表格\n签名\n其他\n打印\n预览\n验证CA签名\n手工解锁\n删除\n病历参考\n更新数据\n加载全部病程\n个人模板管理\n返回\n腹部:\n视诊: 外形: 腹部外形正常\n腹围: 未测\n脐部: 正常\n胃形: 未见\n肠形: 未见\n蠕动波: 未见\n腹式呼吸: 正常\n腹壁静脉曲张: 无\n腹壁其它情况: 无\n触诊: 全腹柔软\n压痛反跳痛: 无压痛及反跳痛\n波动感: 无\n振水声: 无\n腹部包块: 腹部未触及包块\n肝脏: 肝脏肋下未触及\n胆囊: 未触及, Murphy征阴性\n脾脏: 脾脏肋下未触及\n肾脏: 未触及\n输尿管压痛点: 无压痛\n叩诊: 肝浊音界: 正常,\n肝上界位于锁骨中线, 第五肋间\n移动性浊音: 阴性,\n肾区叩痛: 无\n听诊: 肠鸣音无明显增强或减弱, 未闻及血管杂音\n肛门直肠: 未查\n生殖器: 未查\n脊柱四肢:\n脊柱外形: 脊柱正常生理弯曲\n70 四 肢：四肢无畸形，未见杵状指（趾），未见静脉曲张，双下肢无凹陷性水肿\n003470 20.2.41.64\n关 节：各关节未见异常，活动无受限\n肌 肉：未见肌肉萎缩，肌张力正常。四肢肌力5级。\n神经系统：\n浅反射：双侧浅反射正常引出\n深反射：双侧深反射正常引出\n病理反射：未引出\n脑膜刺激征：阴性\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n专科情况\n神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下肢无凹陷性水肿。\n实验室及器械检查结果\n(2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm\n，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋巴结彩超\n：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\nCS 扫描全能王\n3亿人都在用的扫描App\n2026-02-28 18:30\n男，因“咳嗽、咳痰1月余”于2026-02-28 15:23入非急诊步行入科。\n病例特点如下：1、老年期男性，起病缓，病程短。2、患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，\n伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。3、既往史：平素\n健康状况：良好。既往病史：否认高血压、冠心病、糖尿病史。传染病史：否，否认肝炎、结核或其他传染病史。预\n防接种史：正规。过敏史：否认过敏史。外伤史：否认外伤史。手术史：2年前曾行尿道结石手术，具体不详。输血\n史：否认输血史。系统回顾：无特殊。否认新冠肺炎流行病接触史。4、查体：T：36.8℃，P：75次/分，R：21次/分\n，BP：138/72mmHg。神志清楚，正常面容，皮肤巩膜无黄染，全身浅表淋巴结未扪及肿大，颈静脉无怒张。胸廓对称\n无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常，双肺叩诊呈清音，双肺呼吸音\n清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音。心界不大，心率75次/分，心律齐，各瓣膜区未闻及杂音。腹\n部外形正常，全腹柔软，无压痛及反跳痛，腹部未触及包块，肝脏肋下未触及，脾脏肋下未触及。移动性浊音阴性。\n双下肢无凹陷性水肿。浅反射：双侧浅反射正常引出。深反射：双侧深反射正常引出。病理反射：未引出。脑膜刺激\n征：阴性5、专科情况：神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下\n肢无凹陷性水肿。6、辅助检查：（2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组\n织肿块，最大截断面约77mm*60mm，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧\n胸膜肥厚、钙化。浅表淋巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。\n初步诊断：1.肺部阴影\n2.细菌性肺炎\n诊断依据：1.老年男性，起步缓，病程短\n2.咳嗽，咳淡黄色粘液痰\n3.外院胸部CT提示右肺下叶后基底段软组织肿块\n鉴别诊断。\n1.肺结核球\n编辑\n功能\n表格\n签名\n其他\n打印\n预览\n验证CA签名\n手工解锁\n删除\n病历参考\n更新数据\n加载全部病程\n个人模板管理\n返回\n鉴别诊断：\n1.肺结核球：多见于年轻患者，病灶多见于结核好发部位，如肺上叶尖后段和下叶背段，直径一般<3\ncm。一般无症状，病灶边界清楚，密度高，可有包膜。有时含钙化点，周围有卫星灶。\n2.急性粟粒性肺结核：应与弥漫型细支气管肺泡癌相鉴别。通常粟粒型肺结核患者年龄较轻，有发热\n，盗汗等全身中毒症状，呼吸道症状不明显。x线表现为细小、分布均匀、密度较淡的粟粒样结节病灶。\n而细支气管—肺泡细胞癌两肺多有大小不等的结节状播散病灶，边界清楚、密度较高，进行性发展和增大\n，且有进行性呼吸困难。\n3.肺炎：若无毒性症状，抗生素治疗后肺部阴影吸收缓慢，或同一部位反复发生肺炎时，应考虑到肺\n癌可能。肺部慢性炎症机化，形成团块状的炎性假瘤，也易与肺癌相混淆。但炎性假瘤往往形态不整，边\n缘不齐，核心密度较高，易伴有胸膜增厚，病灶长期无明显变化。\n4.肺脓肿：起病急，中毒症状严重，多有寒战、高热、咳嗽、咳大量脓臭痰等症状。肺部x线表现为\n均匀的大片状炎性阴影，空洞内常见较深液平。结合纤支镜检查和痰脱落细胞检查可以鉴别。\n5.纵隔淋巴瘤：颇似中央型肺癌，常为双侧性，可有发热等全身症状，需病理诊断。\nVTE血栓风险评估：创建时间:2026-02-28 15:37:11,评估节点:入院,量表名称:Padua评分,分数:0,评分描述:低危,\n预防措施:undefined\nVTE出血风险评估：创建时间:2026-02-28 18:35:54,评估节点:入院,量表名称:内科出血风险评估,分数:1,评分描述：\n低危,预防措施:undefined\n诊疗计划：1.内科护理常规,II级护理。\n2.完善必要辅助检查如血肿瘤标志物、痰液化验、胸部增强CT、支气管镜检查或浅表淋巴结及肺穿刺活检\n以确诊，必要时行颅脑MRI、腹部超声、骨扫描或PET-CT等检查以利进一步疾病诊治。\n3.给予吸氧、抗感染及止血、镇痛等对症支持治疗；明确病理类型拟定下一步治疗方案。\n是否需手术治疗：否\n医师签名：\n住院医师：",
    "role": "user"
  }
]
2026-08-10 16:09:01,448 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:09:01.447+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:09:24,881 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:09:24,881 INFO     29 [qwen-vl-text] LLM output (len=2729):
{
  "encounter_date": "2026-02-28",
  "dm_name": null,
  "dm_gender": "男",
  "dm_age": null,
  "dm_ethnicity": null,
  "dm_marital_status": "已婚",
  "dm_occupation": null,
  "dm_admission_time": "2026-02-28 15:23",
  "dm_record_time": "2026-03-19 11:24",
  "dm_history_provider": "患者及家属",
  "cc_text": "咳嗽、咳痰1月余",
  "cc_main_symptoms": [
    "咳嗽",
    "咳痰"
  ],
  "cc_duration": "1月余",
  "pi_text": "患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。至当地医院体检发现肺部阴影，具体不详。2026-02-26至中山大学附属第一医院广西医院就诊，查胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。具体诊治不详。为进一步治疗，遂至我院门诊就诊，门诊拟“肺占位性病变”收治入院。自发病以来，患者精神、食欲、睡眠正常，大小便正常，体重无明显变化。",
  "pmh_disease_history": [
    "否认高血压",
    "否认冠心病",
    "否认糖尿病",
    "否认肝炎",
    "否认结核",
    "否认其他传染病"
  ],
  "pmh_allergy_history": [
    "否认过敏史"
  ],
  "pmh_surgery_trauma_history": [
    "2年前曾行尿道结石手术",
    "否认外伤史"
  ],
  "ph_smoking": "有吸烟史，约10支/天，已吸烟40年",
  "ph_drinking": "否认饮酒史",
  "oh_menarche_age": null,
  "oh_menopause_age": null,
  "oh_pregnancies": "育有1子",
  "fh_text": "否认相似家族病史及遗传病史。",
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36.8,
  "vs_pulse_bpm": 75,
  "vs_respiration_rpm": 21,
  "vs_systolic_bp_mmhg": 138,
  "vs_diastolic_bp_mmhg": 72,
  "pe_general_condition": "神志清楚，正常面容，发育正常，营养良好，自主体位，表情自如，步态正常，正力型，合作",
  "pe_skin_mucosa": "全身皮肤未见皮疹，未见皮下出血，毛发分布正常，温度、湿度、弹性均正常，未见水肿，无肝掌，未见蜘蛛痣，皮肤巩膜无黄染",
  "pe_lymph_nodes": "全身浅表淋巴结未扪及肿大",
  "pe_lungs": "胸廓对称无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧呼吸运动均匀对称，双肺触觉语颤对称无异常，未触及胸膜摩擦感。双肺叩诊呈清音。双肺呼吸音清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音",
  "pe_heart": "心尖搏动未见异常，位于左侧第五肋间锁骨中线内0.5cm，无异常隆起及凹陷。心尖搏动未触及异常，未触及震颤及心包摩擦感。心界不大。心率：75次/分，心律：齐，A2 > P2。心音S1有力，心音S2有力，心音S3无，心音S4无。各瓣膜区未闻及杂音。无额外心音，无心包摩擦音。周围血管未见异常血管征",
  "pe_abdomen": "腹部外形正常，腹式呼吸正常，无腹壁静脉曲张。全腹柔软，无压痛及反跳痛，无波动感，无振水声，腹部未触及包块。肝脏肋下未触及，胆囊未触及，Murphy征阴性，脾脏肋下未触及，肾脏未触及，输尿管无压痛。肝浊音界正常，肝上界位于锁骨中线第五肋间，移动性浊音阴性，肾区无叩痛。肠鸣音无明显增强或减弱，未闻及血管杂音",
  "pe_extremities": "四肢无畸形，未见杵状指（趾），未见静脉曲张，双下肢无凹陷性水肿。各关节未见异常，活动无受限。未见肌肉萎缩，肌张力正常。四肢肌力5级",
  "pe_nervous_system": "双侧浅反射正常引出，双侧深反射正常引出，病理反射未引出，脑膜刺激征阴性",
  "pe_specialist_exam": "神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下肢无凹陷性水肿",
  "pe_ecog_score": null,
  "pat_text": "（2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。",
  "pat_items": [
    "胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化",
    "浅表淋巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结"
  ],
  "preliminary_diagnoses": [
    {
      "name": "肺部阴影",
      "diagnosis_type": "西医",
      "is_primary": true
    },
    {
      "name": "细菌性肺炎",
      "diagnosis_type": "西医",
      "is_primary": false
    }
  ],
  "department": "老年医学呼吸内科"
}
2026-08-10 16:09:24,881 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-28]
2026-08-10 16:09:24,899 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7951862, prompt_len=1298
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共27行）
["病史", "主诉：咳嗽、咳痰1月余", "现病史：患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、", "呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。至当地医院体检发现肺部阴影，具体不详。2026-02-26至中", "山大学附属第一医院广西医院就诊，查胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm", "，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋", "巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。具体诊治不详。为进一步治疗，遂", "至我院门诊就诊，门诊拟“肺占位性病变”收治入院。自发病以来，患者精神、食欲、睡眠正常，大小便正", "常，体重无明显变化。", "既往史：平素健康状况：良好。", "既往病史：否认高血压、冠心病、糖尿病史。", "传染病史：否，否认肝炎、结核或其他传染病史。", "预防接种史：正规。", "过敏史：否认过敏史。", "外伤史：否认外伤史。", "手术史：2年前曾行尿道结石手术，具体不详。", "输血史：否认输血史。", "系统回顾：无特殊。", "个人史：出生地：广西壮族自治区南宁市青秀区", "地方病地区居住情况：无", "冶游史：否认冶游史", "职业与工作条件有无工业毒物、粉尘、放射性物质及接触史：无", "广西医科大学第一附属医院 孔令祈", "11:24", "2026-03-19", "姜晓红 (D450199...", "姜晓红 (D450199..."]

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
2026-08-10 16:09:35,107 INFO     29 [qwen-vl-text] coord API raw response (len=1797):
```json
[
	{"text": "病史", "bbox": [459, 14, 540, 48]},
	{"text": "主诉：咳嗽、咳痰1月余", "bbox": [39, 47, 248, 75]},
	{"text": "现病史：患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、", "bbox": [39, 87, 950, 116]},
	{"text": "呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。至当地医院体检发现肺部阴影，具体不详。2026-02-26至中", "bbox": [115, 126, 956, 154]},
	{"text": "山大学附属第一医院广西医院就诊，查胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm", "bbox": [115, 166, 958, 194]},
	{"text": "，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋", "bbox": [115, 205, 956, 233]},
	{"text": "巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。具体诊治不详。为进一步治疗，遂", "bbox": [115, 244, 956, 272]},
	{"text": "至我院门诊就诊，门诊拟“肺占位性病变”收治入院。自发病以来，患者精神、食欲、睡眠正常，大小便正", "bbox": [115, 283, 956, 311]},
	{"text": "常，体重无明显变化。", "bbox": [115, 323, 280, 350]},
	{"text": "既往史：平素健康状况：良好。", "bbox": [39, 362, 280, 390]},
	{"text": "既往病史：否认高血压、冠心病、糖尿病史。", "bbox": [112, 401, 458, 429]},
	{"text": "传染病史：否，否认肝炎、结核或其他传染病史。", "bbox": [112, 440, 494, 468]},
	{"text": "预防接种史：正规。", "bbox": [112, 479, 262, 507]},
	{"text": "过敏史：否认过敏史。", "bbox": [112, 518, 280, 546]},
	{"text": "外伤史：否认外伤史。", "bbox": [112, 557, 280, 585]},
	{"text": "手术史：2年前曾行尿道结石手术，具体不详。", "bbox": [112, 597, 467, 625]},
	{"text": "输血史：否认输血史。", "bbox": [112, 636, 280, 664]},
	{"text": "系统回顾：无特殊。", "bbox": [112, 675, 270, 703]},
	{"text": "个人史：出生地：广西壮族自治区南宁市青秀区", "bbox": [40, 715, 412, 743]},
	{"text": "地方病地区居住情况：无", "bbox": [110, 754, 307, 782]},
	{"text": "冶游史：否认冶游史", "bbox": [110, 793, 270, 821]},
	{"text": "职业与工作条件有无工业毒物、粉尘、放射性物质及接触史：无", "bbox": [110, 832, 604, 860]},
	{"text": "广西医科大学第一附属医院 孔令祈", "bbox": [764, 832, 938, 851]},
	{"text": "11:24", "bbox": [963, 862, 988, 875]},
	{"text": "2026-03-19", "bbox": [950, 880, 998, 893]},
	{"text": "姜晓红 (D450199...", "bbox": [33, 873, 113, 887]},
	{"text": "姜晓红 (D450199...", "bbox": [148, 873, 228, 887]}
]
```
2026-08-10 16:09:35,107 INFO     29 [qwen-vl-text] coord API: raw_items=27, valid_items=27, elapsed=10.2s
2026-08-10 16:09:35,107 INFO     29 [qwen-vl-text] coord item[0]: text=病史, bbox=[459, 14, 540, 48]
2026-08-10 16:09:35,107 INFO     29 [qwen-vl-text] coord item[1]: text=主诉：咳嗽、咳痰1月余, bbox=[39, 47, 248, 75]
2026-08-10 16:09:35,107 INFO     29 [qwen-vl-text] coord item[2]: text=现病史：患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、, bbox=[39, 87, 950, 116]
2026-08-10 16:09:35,107 INFO     29 [qwen-vl-text] coord item[3]: text=呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。至当地医院体检发现肺部阴影，具体不详。2026-02-26至中, bbox=[115, 126, 956, 154]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[4]: text=山大学附属第一医院广西医院就诊，查胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm, bbox=[115, 166, 958, 194]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[5]: text=，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋, bbox=[115, 205, 956, 233]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[6]: text=巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。具体诊治不详。为进一步治疗，遂, bbox=[115, 244, 956, 272]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[7]: text=至我院门诊就诊，门诊拟“肺占位性病变”收治入院。自发病以来，患者精神、食欲、睡眠正常，大小便正, bbox=[115, 283, 956, 311]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[8]: text=常，体重无明显变化。, bbox=[115, 323, 280, 350]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[9]: text=既往史：平素健康状况：良好。, bbox=[39, 362, 280, 390]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[10]: text=既往病史：否认高血压、冠心病、糖尿病史。, bbox=[112, 401, 458, 429]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[11]: text=传染病史：否，否认肝炎、结核或其他传染病史。, bbox=[112, 440, 494, 468]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[12]: text=预防接种史：正规。, bbox=[112, 479, 262, 507]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[13]: text=过敏史：否认过敏史。, bbox=[112, 518, 280, 546]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[14]: text=外伤史：否认外伤史。, bbox=[112, 557, 280, 585]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[15]: text=手术史：2年前曾行尿道结石手术，具体不详。, bbox=[112, 597, 467, 625]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[16]: text=输血史：否认输血史。, bbox=[112, 636, 280, 664]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[17]: text=系统回顾：无特殊。, bbox=[112, 675, 270, 703]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[18]: text=个人史：出生地：广西壮族自治区南宁市青秀区, bbox=[40, 715, 412, 743]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[19]: text=地方病地区居住情况：无, bbox=[110, 754, 307, 782]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[20]: text=冶游史：否认冶游史, bbox=[110, 793, 270, 821]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[21]: text=职业与工作条件有无工业毒物、粉尘、放射性物质及接触史：无, bbox=[110, 832, 604, 860]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[22]: text=广西医科大学第一附属医院 孔令祈, bbox=[764, 832, 938, 851]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[23]: text=11:24, bbox=[963, 862, 988, 875]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[24]: text=2026-03-19, bbox=[950, 880, 998, 893]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[25]: text=姜晓红 (D450199..., bbox=[33, 873, 113, 887]
2026-08-10 16:09:35,108 INFO     29 [qwen-vl-text] coord item[26]: text=姜晓红 (D450199..., bbox=[148, 873, 228, 887]
2026-08-10 16:09:35,111 INFO     29 [qwen-vl-text] page=0 — 27/27 coords, api_time=10.2s
2026-08-10 16:09:35,125 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4556708, prompt_len=919
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共21行）
["烟酒嗜好及药物使用史：有吸烟史，约10支/天，已吸烟40年，否认饮酒史。", "婚姻史：有婚姻史，结婚年龄：适龄结婚。有生育史，育有1子。", "家族史：否认相似家族病史及遗传病史。", "请患者或病史叙述者仔细确认以上病史记录并签字：[患者]", "体格检查", "一般情况：", "体温：36.8℃", "脉搏：75次/分", "呼吸：21次/分", "血压：138/72mmHg", "身高：161CM", "体重：74kg", "发育：正常", "营养：良好", "神志：清楚", "体位：自主体位", "面容：正常面容", "表情：自如", "步态：正常", "体型：正力型", "配合检查：合作"]

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
2026-08-10 16:09:43,891 INFO     29 [qwen-vl-text] coord API raw response (len=1163):
[
	{"text": "烟酒嗜好及药物使用史：有吸烟史，约10支/天，已吸烟40年，否认饮酒史。", "bbox": [105, 245, 740, 275]},
	{"text": "婚姻史：有婚姻史，结婚年龄：适龄结婚。有生育史，育有1子。", "bbox": [25, 287, 565, 315]},
	{"text": "家族史：否认相似家族病史及遗传病史。", "bbox": [25, 329, 365, 357]},
	{"text": "请患者或病史叙述者仔细确认以上病史记录并签字：[患者]", "bbox": [384, 410, 876, 439]},
	{"text": "体格检查", "bbox": [450, 492, 585, 526]},
	{"text": "一般情况：", "bbox": [24, 545, 108, 573]},
	{"text": "体温：36.8℃", "bbox": [60, 587, 172, 614]},
	{"text": "脉搏：75次/分", "bbox": [253, 587, 379, 614]},
	{"text": "呼吸：21次/分", "bbox": [474, 587, 597, 614]},
	{"text": "血压：138/72mmHg", "bbox": [683, 587, 838, 614]},
	{"text": "身高：161CM", "bbox": [61, 636, 164, 663]},
	{"text": "体重：74kg", "bbox": [253, 636, 351, 663]},
	{"text": "发育：正常", "bbox": [474, 636, 568, 663]},
	{"text": "营养：良好", "bbox": [682, 636, 777, 663]},
	{"text": "神志：清楚", "bbox": [61, 682, 154, 709]},
	{"text": "体位：自主体位", "bbox": [253, 682, 389, 709]},
	{"text": "面容：正常面容", "bbox": [474, 682, 607, 709]},
	{"text": "表情：自如", "bbox": [682, 682, 777, 709]},
	{"text": "步态：正常", "bbox": [61, 728, 154, 755]},
	{"text": "体型：正力型", "bbox": [253, 728, 368, 755]},
	{"text": "配合检查：合作", "bbox": [473, 728, 606, 755]}
]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord API: raw_items=21, valid_items=21, elapsed=8.8s
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord item[0]: text=烟酒嗜好及药物使用史：有吸烟史，约10支/天，已吸烟40年，否认饮酒史。, bbox=[105, 245, 740, 275]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord item[1]: text=婚姻史：有婚姻史，结婚年龄：适龄结婚。有生育史，育有1子。, bbox=[25, 287, 565, 315]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord item[2]: text=家族史：否认相似家族病史及遗传病史。, bbox=[25, 329, 365, 357]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord item[3]: text=请患者或病史叙述者仔细确认以上病史记录并签字：[患者], bbox=[384, 410, 876, 439]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord item[4]: text=体格检查, bbox=[450, 492, 585, 526]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord item[5]: text=一般情况：, bbox=[24, 545, 108, 573]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord item[6]: text=体温：36.8℃, bbox=[60, 587, 172, 614]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord item[7]: text=脉搏：75次/分, bbox=[253, 587, 379, 614]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord item[8]: text=呼吸：21次/分, bbox=[474, 587, 597, 614]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord item[9]: text=血压：138/72mmHg, bbox=[683, 587, 838, 614]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord item[10]: text=身高：161CM, bbox=[61, 636, 164, 663]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord item[11]: text=体重：74kg, bbox=[253, 636, 351, 663]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord item[12]: text=发育：正常, bbox=[474, 636, 568, 663]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord item[13]: text=营养：良好, bbox=[682, 636, 777, 663]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord item[14]: text=神志：清楚, bbox=[61, 682, 154, 709]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord item[15]: text=体位：自主体位, bbox=[253, 682, 389, 709]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord item[16]: text=面容：正常面容, bbox=[474, 682, 607, 709]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord item[17]: text=表情：自如, bbox=[682, 682, 777, 709]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord item[18]: text=步态：正常, bbox=[61, 728, 154, 755]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord item[19]: text=体型：正力型, bbox=[253, 728, 368, 755]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] coord item[20]: text=配合检查：合作, bbox=[473, 728, 606, 755]
2026-08-10 16:09:43,892 INFO     29 [qwen-vl-text] page=1 — 21/21 coords, api_time=8.8s
2026-08-10 16:09:43,904 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5051128, prompt_len=1035
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共31行）
["皮肤黏膜:", "色", "泽:正常", "皮", "疹:全身皮肤未见皮疹", "皮下出血:全身皮肤未见皮下出血", "毛发分布:毛发分布正常", "温度与湿度:温度、湿度、弹性均正常", "水", "肿:未见水肿", "肝", "掌:无", "蜘", "蛛", "痣:未见蜘蛛痣", "其他表现:无", "淋巴结:全身浅表淋巴结未扪及肿大", "头部:", "头颅:头颅大小正常,无畸形", "眼:眉毛,眼睑,结膜,眼球未见异常,双侧巩膜无黄染", "耳:双耳外观未见异常,乳突无压痛,外耳道未见分泌物", "鼻:鼻部外观未见异常,鼻翼无扇动,鼻腔无分泌物,鼻窦区无压痛", "咽喉:双侧扁桃体未见肿大,表面未见脓性分泌物,咽未见异常,声音正常", "口腔:唇,舌,牙齿,牙龈正常", "颈部:", "颈部运动:颈软无抵抗", "颈静脉:无怒张", "气管:居中", "颈动脉搏动:正常", "肝-颈静脉回流征:阴性", "广西医科大:"]

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
2026-08-10 16:09:53,164 INFO     29 [qwen-vl-text] coord API raw response (len=1686):
[
	{"text": "皮肤黏膜:", "bbox": [94, 7, 181, 37]},
	{"text": "色", "bbox": [136, 52, 155, 80]},
	{"text": "泽:正常", "bbox": [222, 52, 299, 80]},
	{"text": "皮", "bbox": [136, 92, 155, 123]},
	{"text": "疹:全身皮肤未见皮疹", "bbox": [222, 92, 415, 121]},
	{"text": "皮下出血:全身皮肤未见皮下出血", "bbox": [137, 137, 452, 165]},
	{"text": "毛发分布:毛发分布正常", "bbox": [137, 178, 375, 207]},
	{"text": "温度与湿度:温度、湿度、弹性均正常", "bbox": [137, 221, 498, 250]},
	{"text": "水", "bbox": [137, 264, 155, 292]},
	{"text": "肿:未见水肿", "bbox": [222, 264, 337, 292]},
	{"text": "肝", "bbox": [137, 306, 155, 335]},
	{"text": "掌:无", "bbox": [222, 306, 290, 335]},
	{"text": "蜘", "bbox": [137, 350, 155, 377]},
	{"text": "蛛", "bbox": [184, 350, 203, 377]},
	{"text": "痣:未见蜘蛛痣", "bbox": [222, 350, 355, 377]},
	{"text": "其他表现:无", "bbox": [137, 391, 278, 419]},
	{"text": "淋巴结:全身浅表淋巴结未扪及肿大", "bbox": [100, 434, 421, 462]},
	{"text": "头部:", "bbox": [100, 475, 181, 503]},
	{"text": "头颅:头颅大小正常,无畸形", "bbox": [138, 517, 383, 545]},
	{"text": "眼:眉毛,眼睑,结膜,眼球未见异常,双侧巩膜无黄染", "bbox": [138, 558, 604, 586]},
	{"text": "耳:双耳外观未见异常,乳突无压痛,外耳道未见分泌物", "bbox": [138, 600, 604, 628]},
	{"text": "鼻:鼻部外观未见异常,鼻翼无扇动,鼻腔无分泌物,鼻窦区无压痛", "bbox": [138, 641, 696, 669]},
	{"text": "咽喉:双侧扁桃体未见肿大,表面未见脓性分泌物,咽未见异常,声音正常", "bbox": [138, 683, 749, 711]},
	{"text": "口腔:唇,舌,牙齿,牙龈正常", "bbox": [138, 724, 401, 752]},
	{"text": "颈部:", "bbox": [155, 766, 181, 793]},
	{"text": "颈部运动:颈软无抵抗", "bbox": [134, 808, 321, 836]},
	{"text": "颈静脉:无怒张", "bbox": [498, 808, 626, 836]},
	{"text": "气管:居中", "bbox": [754, 807, 844, 835]},
	{"text": "颈动脉搏动:正常", "bbox": [134, 855, 321, 883]},
	{"text": "肝-颈静脉回流征:阴性", "bbox": [498, 855, 692, 883]},
	{"text": "广西医科大:", "bbox": [862, 880, 938, 900]}
]
2026-08-10 16:09:53,164 INFO     29 [qwen-vl-text] coord API: raw_items=31, valid_items=31, elapsed=9.3s
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[0]: text=皮肤黏膜:, bbox=[94, 7, 181, 37]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[1]: text=色, bbox=[136, 52, 155, 80]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[2]: text=泽:正常, bbox=[222, 52, 299, 80]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[3]: text=皮, bbox=[136, 92, 155, 123]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[4]: text=疹:全身皮肤未见皮疹, bbox=[222, 92, 415, 121]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[5]: text=皮下出血:全身皮肤未见皮下出血, bbox=[137, 137, 452, 165]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[6]: text=毛发分布:毛发分布正常, bbox=[137, 178, 375, 207]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[7]: text=温度与湿度:温度、湿度、弹性均正常, bbox=[137, 221, 498, 250]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[8]: text=水, bbox=[137, 264, 155, 292]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[9]: text=肿:未见水肿, bbox=[222, 264, 337, 292]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[10]: text=肝, bbox=[137, 306, 155, 335]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[11]: text=掌:无, bbox=[222, 306, 290, 335]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[12]: text=蜘, bbox=[137, 350, 155, 377]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[13]: text=蛛, bbox=[184, 350, 203, 377]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[14]: text=痣:未见蜘蛛痣, bbox=[222, 350, 355, 377]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[15]: text=其他表现:无, bbox=[137, 391, 278, 419]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[16]: text=淋巴结:全身浅表淋巴结未扪及肿大, bbox=[100, 434, 421, 462]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[17]: text=头部:, bbox=[100, 475, 181, 503]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[18]: text=头颅:头颅大小正常,无畸形, bbox=[138, 517, 383, 545]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[19]: text=眼:眉毛,眼睑,结膜,眼球未见异常,双侧巩膜无黄染, bbox=[138, 558, 604, 586]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[20]: text=耳:双耳外观未见异常,乳突无压痛,外耳道未见分泌物, bbox=[138, 600, 604, 628]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[21]: text=鼻:鼻部外观未见异常,鼻翼无扇动,鼻腔无分泌物,鼻窦区无压痛, bbox=[138, 641, 696, 669]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[22]: text=咽喉:双侧扁桃体未见肿大,表面未见脓性分泌物,咽未见异常,声音正常, bbox=[138, 683, 749, 711]
2026-08-10 16:09:53,165 INFO     29 [qwen-vl-text] coord item[23]: text=口腔:唇,舌,牙齿,牙龈正常, bbox=[138, 724, 401, 752]
2026-08-10 16:09:53,166 INFO     29 [qwen-vl-text] coord item[24]: text=颈部:, bbox=[155, 766, 181, 793]
2026-08-10 16:09:53,166 INFO     29 [qwen-vl-text] coord item[25]: text=颈部运动:颈软无抵抗, bbox=[134, 808, 321, 836]
2026-08-10 16:09:53,166 INFO     29 [qwen-vl-text] coord item[26]: text=颈静脉:无怒张, bbox=[498, 808, 626, 836]
2026-08-10 16:09:53,166 INFO     29 [qwen-vl-text] coord item[27]: text=气管:居中, bbox=[754, 807, 844, 835]
2026-08-10 16:09:53,166 INFO     29 [qwen-vl-text] coord item[28]: text=颈动脉搏动:正常, bbox=[134, 855, 321, 883]
2026-08-10 16:09:53,166 INFO     29 [qwen-vl-text] coord item[29]: text=肝-颈静脉回流征:阴性, bbox=[498, 855, 692, 883]
2026-08-10 16:09:53,166 INFO     29 [qwen-vl-text] coord item[30]: text=广西医科大:, bbox=[862, 880, 938, 900]
2026-08-10 16:09:53,167 INFO     29 [qwen-vl-text] page=2 — 31/31 coords, api_time=9.3s
2026-08-10 16:09:53,181 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5275194, prompt_len=18786
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共864行）
["预览 验证CA签名 手工解锁 删除 病历参考 更新数据 加载全部病程 个人模板管理 返回", "20部：", "003470 20.2.11", "003470 20.2.11", "003470 20.2.11", "003470 20.2.11", "胸部：胸廓对称无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常", "肺部：", "视诊：双侧呼吸运动均匀对称，无增强或者减弱", "触诊：双肺触觉语颤对称无异常，未触及胸膜摩擦感", "叩诊：双肺叩诊呈清音", "听诊：双肺呼吸音清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音", "心脏：", "视诊：心尖搏动未见异常，位于左侧第五肋间锁骨中线内0.5cm，无异常隆起及凹陷", "触诊：心尖搏动未触及异常，未触及震颤及心包摩擦感", "叩诊：心界不大", "听诊：心率：75次/分，心律：齐 A2 > P2", "心音 S1：有力， 心音 S2：有力， 心音 S3：无， 心音 S4：无", "杂音：各瓣膜区未闻及杂音", "额外心音：无", "心包摩擦音：无", "周围血管：未见异常血管征", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41"]

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
2026-08-10 16:11:06,425 INFO     29 [qwen-vl-text] coord API raw response (len=11123):
[
	{"text": "预览 验证CA签名 手工解锁 删除 病历参考 更新数据 加载全部病程 个人模板管理 返回", "bbox": [29, 116, 607, 140]},
	{"text": "20部：", "bbox": [37, 148, 92, 182]},
	{"text": "003470 20.2.11", "bbox": [184, 154, 354, 192]},
	{"text": "003470 20.2.11", "bbox": [413, 154, 550, 192]},
	{"text": "003470 20.2.11", "bbox": [643, 154, 780, 192]},
	{"text": "003470 20.2.11", "bbox": [872, 154, 984, 192]},
	{"text": "胸部：胸廓对称无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常", "bbox": [38, 188, 967, 222]},
	{"text": "肺部：", "bbox": [38, 234, 112, 266]},
	{"text": "视诊：双侧呼吸运动均匀对称，无增强或者减弱", "bbox": [83, 278, 532, 310]},
	{"text": "触诊：双肺触觉语颤对称无异常，未触及胸膜摩擦感", "bbox": [83, 323, 572, 355]},
	{"text": "叩诊：双肺叩诊呈清音", "bbox": [83, 367, 307, 400]},
	{"text": "听诊：双肺呼吸音清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音", "bbox": [83, 412, 736, 444]},
	{"text": "心脏：", "bbox": [40, 458, 112, 490]},
	{"text": "视诊：心尖搏动未见异常，位于左侧第五肋间锁骨中线内0.5cm，无异常隆起及凹陷", "bbox": [83, 502, 848, 534]},
	{"text": "触诊：心尖搏动未触及异常，未触及震颤及心包摩擦感", "bbox": [83, 546, 591, 578]},
	{"text": "叩诊：心界不大", "bbox": [83, 591, 247, 623]},
	{"text": "听诊：心率：75次/分，心律：齐 A2 > P2", "bbox": [83, 635, 571, 667]},
	{"text": "心音 S1：有力， 心音 S2：有力， 心音 S3： 无， 心音 S4： 无", "bbox": [166, 680, 711, 712]},
	{"text": "杂音：各瓣膜区未闻及杂音", "bbox": [166, 724, 409, 756]},
	{"text": "额外心音：无", "bbox": [166, 768, 290, 799]},
	{"text": "心包摩擦音：无", "bbox": [166, 812, 311, 844]},
	{"text": "周围血管：未见异常血管征", "bbox": [13, 855, 250, 887]},
	{"text": "003470 20.2.41.64", "bbox": [413, 838, 550, 890]},
	{"text": "003470 20.2.41.64", "bbox": [633, 838, 770, 890]},
	{"text": "003470 20.2.41.64", "bbox": [855, 838, 992, 890]},
	{"text": "003470 20.2.41.64", "bbox": [32, 605, 112, 648]},
	{"text": "003470 20.2.41.64", "bbox": [112, 605, 192, 648]},
	{"text": "003470 20.2.41.64", "bbox": [192, 605, 272, 648]},
	{"text": "003470 20.2.41.64", "bbox": [272, 605, 352, 648]},
	{"text": "003470 20.2.41.64", "bbox": [352, 605, 432, 648]},
	{"text": "003470 20.2.41.64", "bbox": [432, 605, 512, 648]},
	{"text": "003470 20.2.41.64", "bbox": [512, 605, 592, 648]},
	{"text": "003470 20.2.41.64", "bbox": [592, 605, 672, 648]},
	{"text": "003470 20.2.41.64", "bbox": [672, 605, 752, 648]},
	{"text": "003470 20.2.41.64", "bbox": [752, 605, 832, 648]},
	{"text": "003470 20.2.41.64", "bbox": [832, 605, 912, 648]},
	{"text": "003470 20.2.41.64", "bbox": [912, 605, 992, 648]},
	{"text": "003470 20.2.41.64", "bbox": [32, 561, 112, 603]},
	{"text": "003470 20.2.41.64", "bbox": [112, 561, 192, 603]},
	{"text": "003470 20.2.41.64", "bbox": [192, 561, 272, 603]},
	{"text": "003470 20.2.41.64", "bbox": [272, 561, 352, 603]},
	{"text": "003470 20.2.41.64", "bbox": [352, 561, 432, 603]},
	{"text": "003470 20.2.41.64", "bbox": [432, 561, 512, 603]},
	{"text": "003470 20.2.41.64", "bbox": [512, 561, 592, 603]},
	{"text": "003470 20.2.41.64", "bbox": [592, 561, 672, 603]},
	{"text": "003470 20.2.41.64", "bbox": [672, 561, 752, 603]},
	{"text": "003470 20.2.41.64", "bbox": [752, 561, 832, 603]},
	{"text": "003470 20.2.41.64", "bbox": [832, 561, 912, 603]},
	{"text": "003470 20.2.41.64", "bbox": [912, 561, 992, 603]},
	{"text": "003470 20.2.41.64", "bbox": [32, 517, 112, 559]},
	{"text": "003470 20.2.41.64", "bbox": [112, 517, 192, 559]},
	{"text": "003470 20.2.41.64", "bbox": [192, 517, 272, 559]},
	{"text": "003470 20.2.41.64", "bbox": [272, 517, 352, 559]},
	{"text": "003470 20.2.41.64", "bbox": [352, 517, 432, 559]},
	{"text": "003470 20.2.41.64", "bbox": [432, 517, 512, 559]},
	{"text": "003470 20.2.41.64", "bbox": [512, 517, 592, 559]},
	{"text": "003470 20.2.41.64", "bbox": [592, 517, 672, 559]},
	{"text": "003470 20.2.41.64", "bbox": [672, 517, 752, 559]},
	{"text": "003470 20.2.41.64", "bbox": [752, 517, 832, 559]},
	{"text": "003470 20.2.41.64", "bbox": [832, 517, 912, 559]},
	{"text": "003470 20.2.41.64", "bbox": [912, 517, 992, 559]},
	{"text": "003470 20.2.41.64", "bbox": [32, 473, 112, 515]},
	{"text": "003470 20.2.41.64", "bbox": [112, 473, 192, 515]},
	{"text": "003470 20.2.41.64", "bbox": [192, 473, 272, 515]},
	{"text": "003470 20.2.41.64", "bbox": [272, 473, 352, 515]},
	{"text": "003470 20.2.41.64", "bbox": [352, 473, 432, 515]},
	{"text": "003470 20.2.41.64", "bbox": [432, 473, 512, 515]},
	{"text": "003470 20.2.41.64", "bbox": [512, 473, 592, 515]},
	{"text": "003470 20.2.41.64", "bbox": [592, 473, 672, 515]},
	{"text": "003470 20.2.41.64", "bbox": [672, 473, 752, 515]},
	{"text": "003470 20.2.41.64", "bbox": [752, 473, 832, 515]},
	{"text": "003470 20.2.41.64", "bbox": [832, 473, 912, 515]},
	{"text": "003470 20.2.41.64", "bbox": [912, 473, 992, 515]},
	{"text": "003470 20.2.41.64", "bbox": [32, 429, 112, 471]},
	{"text": "003470 20.2.41.64", "bbox": [112, 429, 192, 471]},
	{"text": "003470 20.2.41.64", "bbox": [192, 429, 272, 471]},
	{"text": "003470 20.2.41.64", "bbox": [272, 429, 352, 471]},
	{"text": "003470 20.2.41.64", "bbox": [352, 429, 432, 471]},
	{"text": "003470 20.2.41.64", "bbox": [432, 429, 512, 471]},
	{"text": "003470 20.2.41.64", "bbox": [512, 429, 592, 471]},
	{"text": "003470 20.2.41.64", "bbox": [592, 429, 672, 471]},
	{"text": "003470 20.2.41.64", "bbox": [672, 429, 752, 471]},
	{"text": "003470 20.2.41.64", "bbox": [752, 429, 832, 471]},
	{"text": "003470 20.2.41.64", "bbox": [832, 429, 912, 471]},
	{"text": "003470 20.2.41.64", "bbox": [912, 429, 992, 471]},
	{"text": "003470 20.2.41.64", "bbox": [32, 385, 112, 427]},
	{"text": "003470 20.2.41.64", "bbox": [112, 385, 192, 427]},
	{"text": "003470 20.2.41.64", "bbox": [192, 385, 272, 427]},
	{"text": "003470 20.2.41.64", "bbox": [272, 385, 352, 427]},
	{"text": "003470 20.2.41.64", "bbox": [352, 385, 432, 427]},
	{"text": "003470 20.2.41.64", "bbox": [432, 385, 512, 427]},
	{"text": "003470 20.2.41.64", "bbox": [512, 385, 592, 427]},
	{"text": "003470 20.2.41.64", "bbox": [592, 385, 672, 427]},
	{"text": "003470 20.2.41.64", "bbox": [672, 385, 752, 427]},
	{"text": "003470 20.2.41.64", "bbox": [752, 385, 832, 427]},
	{"text": "003470 20.2.41.64", "bbox": [832, 385, 912, 427]},
	{"text": "003470 20.2.41.64", "bbox": [912, 385, 992, 427]},
	{"text": "003470 20.2.41.64", "bbox": [32, 341, 112, 383]},
	{"text": "003470 20.2.41.64", "bbox": [112, 341, 192, 383]},
	{"text": "003470 20.2.41.64", "bbox": [192, 341, 272, 383]},
	{"text": "003470 20.2.41.64", "bbox": [272, 341, 352, 383]},
	{"text": "003470 20.2.41.64", "bbox": [352, 341, 432, 383]},
	{"text": "003470 20.2.41.64", "bbox": [432, 341, 512, 383]},
	{"text": "003470 20.2.41.64", "bbox": [512, 341, 592, 383]},
	{"text": "003470 20.2.41.64", "bbox": [592, 341, 672, 383]},
	{"text": "003470 20.2.41.64", "bbox": [672, 341, 752, 383]},
	{"text": "003470 20.2.41.64", "bbox": [752, 341, 832, 383]},
	{"text": "003470 20.2.41.64", "bbox": [832, 341, 912, 383]},
	{"text": "003470 20.2.41.64", "bbox": [912, 341, 992, 383]},
	{"text": "003470 20.2.41.64", "bbox": [32, 297, 112, 339]},
	{"text": "003470 20.2.41.64", "bbox": [112, 297, 192, 339]},
	{"text": "003470 20.2.41.64", "bbox": [192, 297, 272, 339]},
	{"text": "003470 20.2.41.64", "bbox": [272, 297, 352, 339]},
	{"text": "003470 20.2.41.64", "bbox": [352, 297, 432, 339]},
	{"text": "003470 20.2.41.64", "bbox": [432, 297, 512, 339]},
	{"text": "003470 20.2.41.64", "bbox": [512, 297, 592, 339]},
	{"text": "003470 20.2.41.64", "bbox": [592, 297, 672, 339]},
	{"text": "003470 20.2.41.64", "bbox": [672, 297, 752, 339]},
	{"text": "003470 20.2.41.64", "bbox": [752, 297, 832, 339]},
	{"text": "003470 20.2.41.64", "bbox": [832, 297, 912, 339]},
	{"text": "003470 20.2.41.64", "bbox": [912, 297, 992, 339]},
	{"text": "003470 20.2.41.64", "bbox": [32, 253, 112, 295]},
	{"text": "003470 20.2.41.64", "bbox": [112, 253, 192, 295]},
	{"text": "003470 20.2.41.64", "bbox": [192, 253, 272, 295]},
	{"text": "003470 20.2.41.64", "bbox": [272, 253, 352, 295]},
	{"text": "003470 20.2.41.64", "bbox": [352, 253, 432, 295]},
	{"text": "003470 20.2.41.64", "bbox": [432, 253, 512, 295]},
	{"text": "003470 20.2.41.64", "bbox": [512, 253, 592, 295]},
	{"text": "003470 20.2.41.64", "bbox": [592, 253, 672, 295]},
	{"text": "003470 20.2.41.64", "bbox": [672, 253, 752, 295]},
	{"text": "003470 20.2.41.64", "bbox": [752, 253, 832, 295]},
	{"text": "003470 20.2.41.64", "bbox": [832, 253, 912, 295]},
	{"text": "003470 20.2.41.64", "bbox": [912, 253, 992, 295]},
	{"text": "003470 20.2.41.64", "bbox": [32, 209, 112, 251]},
	{"text": "003470 20.2.41.64", "bbox": [112, 209, 192, 251]},
	{"text": "003470 20.2.41.64", "bbox": [192, 209, 272, 251]},
	{"text": "003470 20.2.41.64", "bbox": [272, 209, 352, 251]},
	{"text": "003470 20.2.41.64", "bbox": [352, 209, 432, 251]},
	{"text": "003470 20.2.41.64", "bbox": [432, 209, 512, 251]},
	{"text": "003470 20.2.41.64", "bbox": [512, 209, 592, 251]},
	{"text": "003470 20.2.41.64", "bbox": [592, 209, 672, 251]},
	{"text": "003470 20.2.41.64", "bbox": [672, 209, 752, 251]},
	{"text": "003470 20.2.41.64", "bbox": [752, 209, 832, 251]},
	{"text": "003470 20.2.41.64", "bbox": [832, 209, 912, 251]},
	{"text": "003470 20.2.41.64", "bbox": [912, 209, 992, 251]},
	{"text": "003470 20.2.41.64", "bbox": [32, 165, 112, 207]},
	{"text": "003470 20.2.41.64", "bbox": [112, 165, 192, 207]},
	{"text": "003470 20.2.41.64", "bbox": [192, 165, 272, 207]},
	{"text": "003470 20.2.41.64", "bbox": [272, 165, 352, 207]},
	{"text": "003470 20.2.41.64", "bbox": [352, 165, 432, 207]},
	{"text": "003470 20.2.41.64", "bbox": [432, 165, 512, 207]},
	{"text": "003470 20.2.41.64", "bbox": [512, 165, 592, 207]},
	{"text": "003470 20.2.41.64", "bbox": [592, 165, 672, 207]},
	{"text": "003470 20.2.41.64", "bbox": [672, 165, 752, 207]},
	{"text": "003470 20.2.41.64", "bbox": [752, 165, 832, 207]},
	{"text": "003470 20.2.41.64", "bbox": [832, 165, 912, 207]},
	{"text": "003470 20.2.41.64", "bbox": [912, 165, 992, 207]},
	{"text": "003470 20.2.41.64", "bbox": [32, 121, 112, 163]},
	{"text": "003470 20.2.41.64", "bbox": [112, 121, 192, 163]},
	{"text": "003470 20.2.41.64", "bbox": [192, 121, 272, 163]},
	{"text": "003470 20.2.41.64", "bbox": [272, 121, 352, 163]},
	{"text": "003470 20.2.41.64", "bbox": [352, 121, 432, 163]},
	{"text": "003470 20.2.41.64", "bbox": [432, 121, 512, 163]},
	{"text": "003470 20.2.41.64", "bbox": [512, 121, 592, 163]},
	{"text": "003470 20.2.41.64", "bbox": [592, 121, 672, 163]},
	{"text": "003470 20.2.41.64", "bbox": [672, 121, 752, 163]},
	{"text": "003470 20.2.41.64", "bbox": [752, 121, 832, 163]},
	{"text": "003470 20.2.41.64", "bbox": [832, 121, 912, 163]},
	{"text": "003470 20.2.41.64", "bbox": [912, 121, 992, 163]},
	{"text": "003470 20.2.41.64", "bbox": [32, 77, 112, 119]},
	{"text": "003470 20.2.41.64", "bbox": [112, 77, 192, 119]},
	{"text": "003470 20.2.41.64", "bbox": [192, 77, 272, 119]},
	{"text": "003470 20.2.41.64", "bbox": [272, 77, 352, 119]},
	{"text": "003470 20.2.41.64", "bbox": [352, 77, 432, 119]},
	{"text": "003470 20.2.41.64", "bbox": [432, 77, 512, 119]},
	{"text": "003470 20.2.41.64", "bbox": [512, 77, 592, 119]},
	{"text": "003470 20.2.41.64", "bbox": [592, 77, 672, 119]},
	{"text": "003470 20.2.41.64", "bbox": [672, 77, 752, 119]},
	{"text": "003470 20.2.41.64", "bbox": [752, 77, 832, 119]},
	{"text": "003470 20.2.41.6
2026-08-10 16:11:06,426 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-10 16:11:06,430 INFO     29 [qwen-vl-text] coord API: raw_items=180, valid_items=179, elapsed=73.2s
2026-08-10 16:11:06,430 INFO     29 [qwen-vl-text] coord item[0]: text=预览 验证CA签名 手工解锁 删除 病历参考 更新数据 加载全部病程 个人模板管理 返回, bbox=[29, 116, 607, 140]
2026-08-10 16:11:06,430 INFO     29 [qwen-vl-text] coord item[1]: text=20部：, bbox=[37, 148, 92, 182]
2026-08-10 16:11:06,430 INFO     29 [qwen-vl-text] coord item[2]: text=003470 20.2.11, bbox=[184, 154, 354, 192]
2026-08-10 16:11:06,430 INFO     29 [qwen-vl-text] coord item[3]: text=003470 20.2.11, bbox=[413, 154, 550, 192]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[4]: text=003470 20.2.11, bbox=[643, 154, 780, 192]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[5]: text=003470 20.2.11, bbox=[872, 154, 984, 192]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[6]: text=胸部：胸廓对称无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常, bbox=[38, 188, 967, 222]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[7]: text=肺部：, bbox=[38, 234, 112, 266]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[8]: text=视诊：双侧呼吸运动均匀对称，无增强或者减弱, bbox=[83, 278, 532, 310]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[9]: text=触诊：双肺触觉语颤对称无异常，未触及胸膜摩擦感, bbox=[83, 323, 572, 355]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[10]: text=叩诊：双肺叩诊呈清音, bbox=[83, 367, 307, 400]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[11]: text=听诊：双肺呼吸音清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音, bbox=[83, 412, 736, 444]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[12]: text=心脏：, bbox=[40, 458, 112, 490]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[13]: text=视诊：心尖搏动未见异常，位于左侧第五肋间锁骨中线内0.5cm，无异常隆起及凹陷, bbox=[83, 502, 848, 534]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[14]: text=触诊：心尖搏动未触及异常，未触及震颤及心包摩擦感, bbox=[83, 546, 591, 578]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[15]: text=叩诊：心界不大, bbox=[83, 591, 247, 623]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[16]: text=听诊：心率：75次/分，心律：齐 A2 > P2, bbox=[83, 635, 571, 667]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[17]: text=心音 S1：有力， 心音 S2：有力， 心音 S3： 无， 心音 S4： 无, bbox=[166, 680, 711, 712]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[18]: text=杂音：各瓣膜区未闻及杂音, bbox=[166, 724, 409, 756]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[19]: text=额外心音：无, bbox=[166, 768, 290, 799]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[20]: text=心包摩擦音：无, bbox=[166, 812, 311, 844]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[21]: text=周围血管：未见异常血管征, bbox=[13, 855, 250, 887]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[22]: text=003470 20.2.41.64, bbox=[413, 838, 550, 890]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[23]: text=003470 20.2.41.64, bbox=[633, 838, 770, 890]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[24]: text=003470 20.2.41.64, bbox=[855, 838, 992, 890]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[25]: text=003470 20.2.41.64, bbox=[32, 605, 112, 648]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[26]: text=003470 20.2.41.64, bbox=[112, 605, 192, 648]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[27]: text=003470 20.2.41.64, bbox=[192, 605, 272, 648]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[28]: text=003470 20.2.41.64, bbox=[272, 605, 352, 648]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[29]: text=003470 20.2.41.64, bbox=[352, 605, 432, 648]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[30]: text=003470 20.2.41.64, bbox=[432, 605, 512, 648]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[31]: text=003470 20.2.41.64, bbox=[512, 605, 592, 648]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[32]: text=003470 20.2.41.64, bbox=[592, 605, 672, 648]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[33]: text=003470 20.2.41.64, bbox=[672, 605, 752, 648]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[34]: text=003470 20.2.41.64, bbox=[752, 605, 832, 648]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[35]: text=003470 20.2.41.64, bbox=[832, 605, 912, 648]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[36]: text=003470 20.2.41.64, bbox=[912, 605, 992, 648]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[37]: text=003470 20.2.41.64, bbox=[32, 561, 112, 603]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[38]: text=003470 20.2.41.64, bbox=[112, 561, 192, 603]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[39]: text=003470 20.2.41.64, bbox=[192, 561, 272, 603]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[40]: text=003470 20.2.41.64, bbox=[272, 561, 352, 603]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[41]: text=003470 20.2.41.64, bbox=[352, 561, 432, 603]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[42]: text=003470 20.2.41.64, bbox=[432, 561, 512, 603]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[43]: text=003470 20.2.41.64, bbox=[512, 561, 592, 603]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[44]: text=003470 20.2.41.64, bbox=[592, 561, 672, 603]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[45]: text=003470 20.2.41.64, bbox=[672, 561, 752, 603]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[46]: text=003470 20.2.41.64, bbox=[752, 561, 832, 603]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[47]: text=003470 20.2.41.64, bbox=[832, 561, 912, 603]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[48]: text=003470 20.2.41.64, bbox=[912, 561, 992, 603]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[49]: text=003470 20.2.41.64, bbox=[32, 517, 112, 559]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[50]: text=003470 20.2.41.64, bbox=[112, 517, 192, 559]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[51]: text=003470 20.2.41.64, bbox=[192, 517, 272, 559]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[52]: text=003470 20.2.41.64, bbox=[272, 517, 352, 559]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[53]: text=003470 20.2.41.64, bbox=[352, 517, 432, 559]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[54]: text=003470 20.2.41.64, bbox=[432, 517, 512, 559]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[55]: text=003470 20.2.41.64, bbox=[512, 517, 592, 559]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[56]: text=003470 20.2.41.64, bbox=[592, 517, 672, 559]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[57]: text=003470 20.2.41.64, bbox=[672, 517, 752, 559]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[58]: text=003470 20.2.41.64, bbox=[752, 517, 832, 559]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[59]: text=003470 20.2.41.64, bbox=[832, 517, 912, 559]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[60]: text=003470 20.2.41.64, bbox=[912, 517, 992, 559]
2026-08-10 16:11:06,431 INFO     29 [qwen-vl-text] coord item[61]: text=003470 20.2.41.64, bbox=[32, 473, 112, 515]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[62]: text=003470 20.2.41.64, bbox=[112, 473, 192, 515]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[63]: text=003470 20.2.41.64, bbox=[192, 473, 272, 515]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[64]: text=003470 20.2.41.64, bbox=[272, 473, 352, 515]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[65]: text=003470 20.2.41.64, bbox=[352, 473, 432, 515]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[66]: text=003470 20.2.41.64, bbox=[432, 473, 512, 515]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[67]: text=003470 20.2.41.64, bbox=[512, 473, 592, 515]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[68]: text=003470 20.2.41.64, bbox=[592, 473, 672, 515]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[69]: text=003470 20.2.41.64, bbox=[672, 473, 752, 515]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[70]: text=003470 20.2.41.64, bbox=[752, 473, 832, 515]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[71]: text=003470 20.2.41.64, bbox=[832, 473, 912, 515]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[72]: text=003470 20.2.41.64, bbox=[912, 473, 992, 515]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[73]: text=003470 20.2.41.64, bbox=[32, 429, 112, 471]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[74]: text=003470 20.2.41.64, bbox=[112, 429, 192, 471]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[75]: text=003470 20.2.41.64, bbox=[192, 429, 272, 471]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[76]: text=003470 20.2.41.64, bbox=[272, 429, 352, 471]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[77]: text=003470 20.2.41.64, bbox=[352, 429, 432, 471]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[78]: text=003470 20.2.41.64, bbox=[432, 429, 512, 471]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[79]: text=003470 20.2.41.64, bbox=[512, 429, 592, 471]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[80]: text=003470 20.2.41.64, bbox=[592, 429, 672, 471]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[81]: text=003470 20.2.41.64, bbox=[672, 429, 752, 471]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[82]: text=003470 20.2.41.64, bbox=[752, 429, 832, 471]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[83]: text=003470 20.2.41.64, bbox=[832, 429, 912, 471]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[84]: text=003470 20.2.41.64, bbox=[912, 429, 992, 471]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[85]: text=003470 20.2.41.64, bbox=[32, 385, 112, 427]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[86]: text=003470 20.2.41.64, bbox=[112, 385, 192, 427]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[87]: text=003470 20.2.41.64, bbox=[192, 385, 272, 427]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[88]: text=003470 20.2.41.64, bbox=[272, 385, 352, 427]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[89]: text=003470 20.2.41.64, bbox=[352, 385, 432, 427]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[90]: text=003470 20.2.41.64, bbox=[432, 385, 512, 427]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[91]: text=003470 20.2.41.64, bbox=[512, 385, 592, 427]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[92]: text=003470 20.2.41.64, bbox=[592, 385, 672, 427]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[93]: text=003470 20.2.41.64, bbox=[672, 385, 752, 427]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[94]: text=003470 20.2.41.64, bbox=[752, 385, 832, 427]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[95]: text=003470 20.2.41.64, bbox=[832, 385, 912, 427]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[96]: text=003470 20.2.41.64, bbox=[912, 385, 992, 427]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[97]: text=003470 20.2.41.64, bbox=[32, 341, 112, 383]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[98]: text=003470 20.2.41.64, bbox=[112, 341, 192, 383]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[99]: text=003470 20.2.41.64, bbox=[192, 341, 272, 383]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[100]: text=003470 20.2.41.64, bbox=[272, 341, 352, 383]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[101]: text=003470 20.2.41.64, bbox=[352, 341, 432, 383]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[102]: text=003470 20.2.41.64, bbox=[432, 341, 512, 383]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[103]: text=003470 20.2.41.64, bbox=[512, 341, 592, 383]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[104]: text=003470 20.2.41.64, bbox=[592, 341, 672, 383]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[105]: text=003470 20.2.41.64, bbox=[672, 341, 752, 383]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[106]: text=003470 20.2.41.64, bbox=[752, 341, 832, 383]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[107]: text=003470 20.2.41.64, bbox=[832, 341, 912, 383]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[108]: text=003470 20.2.41.64, bbox=[912, 341, 992, 383]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[109]: text=003470 20.2.41.64, bbox=[32, 297, 112, 339]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[110]: text=003470 20.2.41.64, bbox=[112, 297, 192, 339]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[111]: text=003470 20.2.41.64, bbox=[192, 297, 272, 339]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[112]: text=003470 20.2.41.64, bbox=[272, 297, 352, 339]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[113]: text=003470 20.2.41.64, bbox=[352, 297, 432, 339]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[114]: text=003470 20.2.41.64, bbox=[432, 297, 512, 339]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[115]: text=003470 20.2.41.64, bbox=[512, 297, 592, 339]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[116]: text=003470 20.2.41.64, bbox=[592, 297, 672, 339]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[117]: text=003470 20.2.41.64, bbox=[672, 297, 752, 339]
2026-08-10 16:11:06,432 INFO     29 [qwen-vl-text] coord item[118]: text=003470 20.2.41.64, bbox=[752, 297, 832, 339]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[119]: text=003470 20.2.41.64, bbox=[832, 297, 912, 339]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[120]: text=003470 20.2.41.64, bbox=[912, 297, 992, 339]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[121]: text=003470 20.2.41.64, bbox=[32, 253, 112, 295]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[122]: text=003470 20.2.41.64, bbox=[112, 253, 192, 295]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[123]: text=003470 20.2.41.64, bbox=[192, 253, 272, 295]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[124]: text=003470 20.2.41.64, bbox=[272, 253, 352, 295]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[125]: text=003470 20.2.41.64, bbox=[352, 253, 432, 295]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[126]: text=003470 20.2.41.64, bbox=[432, 253, 512, 295]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[127]: text=003470 20.2.41.64, bbox=[512, 253, 592, 295]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[128]: text=003470 20.2.41.64, bbox=[592, 253, 672, 295]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[129]: text=003470 20.2.41.64, bbox=[672, 253, 752, 295]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[130]: text=003470 20.2.41.64, bbox=[752, 253, 832, 295]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[131]: text=003470 20.2.41.64, bbox=[832, 253, 912, 295]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[132]: text=003470 20.2.41.64, bbox=[912, 253, 992, 295]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[133]: text=003470 20.2.41.64, bbox=[32, 209, 112, 251]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[134]: text=003470 20.2.41.64, bbox=[112, 209, 192, 251]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[135]: text=003470 20.2.41.64, bbox=[192, 209, 272, 251]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[136]: text=003470 20.2.41.64, bbox=[272, 209, 352, 251]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[137]: text=003470 20.2.41.64, bbox=[352, 209, 432, 251]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[138]: text=003470 20.2.41.64, bbox=[432, 209, 512, 251]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[139]: text=003470 20.2.41.64, bbox=[512, 209, 592, 251]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[140]: text=003470 20.2.41.64, bbox=[592, 209, 672, 251]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[141]: text=003470 20.2.41.64, bbox=[672, 209, 752, 251]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[142]: text=003470 20.2.41.64, bbox=[752, 209, 832, 251]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[143]: text=003470 20.2.41.64, bbox=[832, 209, 912, 251]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[144]: text=003470 20.2.41.64, bbox=[912, 209, 992, 251]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[145]: text=003470 20.2.41.64, bbox=[32, 165, 112, 207]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[146]: text=003470 20.2.41.64, bbox=[112, 165, 192, 207]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[147]: text=003470 20.2.41.64, bbox=[192, 165, 272, 207]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[148]: text=003470 20.2.41.64, bbox=[272, 165, 352, 207]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[149]: text=003470 20.2.41.64, bbox=[352, 165, 432, 207]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[150]: text=003470 20.2.41.64, bbox=[432, 165, 512, 207]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[151]: text=003470 20.2.41.64, bbox=[512, 165, 592, 207]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[152]: text=003470 20.2.41.64, bbox=[592, 165, 672, 207]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[153]: text=003470 20.2.41.64, bbox=[672, 165, 752, 207]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[154]: text=003470 20.2.41.64, bbox=[752, 165, 832, 207]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[155]: text=003470 20.2.41.64, bbox=[832, 165, 912, 207]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[156]: text=003470 20.2.41.64, bbox=[912, 165, 992, 207]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[157]: text=003470 20.2.41.64, bbox=[32, 121, 112, 163]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[158]: text=003470 20.2.41.64, bbox=[112, 121, 192, 163]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[159]: text=003470 20.2.41.64, bbox=[192, 121, 272, 163]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[160]: text=003470 20.2.41.64, bbox=[272, 121, 352, 163]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[161]: text=003470 20.2.41.64, bbox=[352, 121, 432, 163]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[162]: text=003470 20.2.41.64, bbox=[432, 121, 512, 163]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[163]: text=003470 20.2.41.64, bbox=[512, 121, 592, 163]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[164]: text=003470 20.2.41.64, bbox=[592, 121, 672, 163]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[165]: text=003470 20.2.41.64, bbox=[672, 121, 752, 163]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[166]: text=003470 20.2.41.64, bbox=[752, 121, 832, 163]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[167]: text=003470 20.2.41.64, bbox=[832, 121, 912, 163]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[168]: text=003470 20.2.41.64, bbox=[912, 121, 992, 163]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[169]: text=003470 20.2.41.64, bbox=[32, 77, 112, 119]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[170]: text=003470 20.2.41.64, bbox=[112, 77, 192, 119]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[171]: text=003470 20.2.41.64, bbox=[192, 77, 272, 119]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[172]: text=003470 20.2.41.64, bbox=[272, 77, 352, 119]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[173]: text=003470 20.2.41.64, bbox=[352, 77, 432, 119]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[174]: text=003470 20.2.41.64, bbox=[432, 77, 512, 119]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[175]: text=003470 20.2.41.64, bbox=[512, 77, 592, 119]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[176]: text=003470 20.2.41.64, bbox=[592, 77, 672, 119]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[177]: text=003470 20.2.41.64, bbox=[672, 77, 752, 119]
2026-08-10 16:11:06,433 INFO     29 [qwen-vl-text] coord item[178]: text=003470 20.2.41.64, bbox=[752, 77, 832, 119]
2026-08-10 16:11:06,437 INFO     29 [qwen-vl-text] page=3 — 864/864 coords, api_time=73.2s
2026-08-10 16:11:06,447 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5097454, prompt_len=1118
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共44行）
["编辑", "功能", "表格", "签名", "其他", "打印", "预览", "验证CA签名", "手工解锁", "删除", "病历参考", "更新数据", "加载全部病程", "个人模板管理", "返回", "腹部:", "视诊: 外形: 腹部外形正常", "腹围: 未测", "脐部: 正常", "胃形: 未见", "肠形: 未见", "蠕动波: 未见", "腹式呼吸: 正常", "腹壁静脉曲张: 无", "腹壁其它情况: 无", "触诊: 全腹柔软", "压痛反跳痛: 无压痛及反跳痛", "波动感: 无", "振水声: 无", "腹部包块: 腹部未触及包块", "肝脏: 肝脏肋下未触及", "胆囊: 未触及, Murphy征阴性", "脾脏: 脾脏肋下未触及", "肾脏: 未触及", "输尿管压痛点: 无压痛", "叩诊: 肝浊音界: 正常,", "肝上界位于锁骨中线, 第五肋间", "移动性浊音: 阴性,", "肾区叩痛: 无", "听诊: 肠鸣音无明显增强或减弱, 未闻及血管杂音", "肛门直肠: 未查", "生殖器: 未查", "脊柱四肢:", "脊柱外形: 脊柱正常生理弯曲"]

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
2026-08-10 16:11:20,639 INFO     29 [qwen-vl-text] coord API raw response (len=2292):
[
	{"text": "编辑", "bbox": [103, 38, 124, 54]},
	{"text": "功能", "bbox": [137, 38, 158, 54]},
	{"text": "表格", "bbox": [170, 38, 191, 54]},
	{"text": "签名", "bbox": [204, 38, 224, 54]},
	{"text": "其他", "bbox": [237, 38, 258, 54]},
	{"text": "打印", "bbox": [100, 98, 120, 113]},
	{"text": "预览", "bbox": [134, 98, 155, 113]},
	{"text": "验证CA签名", "bbox": [168, 98, 220, 113]},
	{"text": "手工解锁", "bbox": [239, 98, 279, 113]},
	{"text": "删除", "bbox": [297, 98, 318, 113]},
	{"text": "病历参考", "bbox": [331, 98, 371, 113]},
	{"text": "更新数据", "bbox": [385, 98, 425, 113]},
	{"text": "加载全部病程", "bbox": [439, 98, 499, 113]},
	{"text": "个人模板管理", "bbox": [513, 98, 573, 113]},
	{"text": "返回", "bbox": [592, 98, 612, 113]},
	{"text": "腹部:", "bbox": [107, 143, 126, 165]},
	{"text": "视诊: 外形: 腹部外形正常", "bbox": [176, 180, 396, 204]},
	{"text": "腹围: 未测", "bbox": [492, 180, 576, 204]},
	{"text": "脐部: 正常", "bbox": [707, 180, 792, 204]},
	{"text": "胃形: 未见", "bbox": [244, 216, 328, 240]},
	{"text": "肠形: 未见", "bbox": [371, 216, 457, 240]},
	{"text": "蠕动波: 未见", "bbox": [491, 216, 595, 240]},
	{"text": "腹式呼吸: 正常", "bbox": [707, 216, 827, 240]},
	{"text": "腹壁静脉曲张: 无", "bbox": [244, 253, 380, 277]},
	{"text": "腹壁其它情况: 无", "bbox": [244, 289, 380, 313]},
	{"text": "触诊: 全腹柔软", "bbox": [176, 326, 312, 350]},
	{"text": "压痛反跳痛: 无压痛及反跳痛", "bbox": [244, 362, 465, 386]},
	{"text": "波动感: 无", "bbox": [244, 398, 354, 422]},
	{"text": "振水声: 无", "bbox": [473, 398, 568, 422]},
	{"text": "腹部包块: 腹部未触及包块", "bbox": [244, 435, 449, 459]},
	{"text": "肝脏: 肝脏肋下未触及", "bbox": [244, 471, 422, 495]},
	{"text": "胆囊: 未触及, Murphy征阴性", "bbox": [244, 508, 473, 532]},
	{"text": "脾脏: 脾脏肋下未触及", "bbox": [244, 544, 422, 568]},
	{"text": "肾脏: 未触及", "bbox": [244, 580, 354, 604]},
	{"text": "输尿管压痛点: 无压痛", "bbox": [242, 617, 413, 641]},
	{"text": "叩诊: 肝浊音界: 正常,", "bbox": [174, 653, 368, 677]},
	{"text": "肝上界位于锁骨中线, 第五肋间", "bbox": [514, 653, 753, 677]},
	{"text": "移动性浊音: 阴性,", "bbox": [241, 690, 385, 714]},
	{"text": "肾区叩痛: 无", "bbox": [514, 690, 630, 714]},
	{"text": "听诊: 肠鸣音无明显增强或减弱, 未闻及血管杂音", "bbox": [174, 726, 563, 750]},
	{"text": "肛门直肠: 未查", "bbox": [107, 762, 223, 786]},
	{"text": "生殖器: 未查", "bbox": [107, 798, 223, 822]},
	{"text": "脊柱四肢:", "bbox": [107, 835, 179, 859]},
	{"text": "脊柱外形: 脊柱正常生理弯曲", "bbox": [140, 871, 359, 895]}
]
2026-08-10 16:11:20,640 INFO     29 [qwen-vl-text] coord API: raw_items=44, valid_items=44, elapsed=14.2s
2026-08-10 16:11:20,640 INFO     29 [qwen-vl-text] coord item[0]: text=编辑, bbox=[103, 38, 124, 54]
2026-08-10 16:11:20,640 INFO     29 [qwen-vl-text] coord item[1]: text=功能, bbox=[137, 38, 158, 54]
2026-08-10 16:11:20,640 INFO     29 [qwen-vl-text] coord item[2]: text=表格, bbox=[170, 38, 191, 54]
2026-08-10 16:11:20,640 INFO     29 [qwen-vl-text] coord item[3]: text=签名, bbox=[204, 38, 224, 54]
2026-08-10 16:11:20,640 INFO     29 [qwen-vl-text] coord item[4]: text=其他, bbox=[237, 38, 258, 54]
2026-08-10 16:11:20,640 INFO     29 [qwen-vl-text] coord item[5]: text=打印, bbox=[100, 98, 120, 113]
2026-08-10 16:11:20,640 INFO     29 [qwen-vl-text] coord item[6]: text=预览, bbox=[134, 98, 155, 113]
2026-08-10 16:11:20,640 INFO     29 [qwen-vl-text] coord item[7]: text=验证CA签名, bbox=[168, 98, 220, 113]
2026-08-10 16:11:20,640 INFO     29 [qwen-vl-text] coord item[8]: text=手工解锁, bbox=[239, 98, 279, 113]
2026-08-10 16:11:20,640 INFO     29 [qwen-vl-text] coord item[9]: text=删除, bbox=[297, 98, 318, 113]
2026-08-10 16:11:20,640 INFO     29 [qwen-vl-text] coord item[10]: text=病历参考, bbox=[331, 98, 371, 113]
2026-08-10 16:11:20,640 INFO     29 [qwen-vl-text] coord item[11]: text=更新数据, bbox=[385, 98, 425, 113]
2026-08-10 16:11:20,640 INFO     29 [qwen-vl-text] coord item[12]: text=加载全部病程, bbox=[439, 98, 499, 113]
2026-08-10 16:11:20,640 INFO     29 [qwen-vl-text] coord item[13]: text=个人模板管理, bbox=[513, 98, 573, 113]
2026-08-10 16:11:20,640 INFO     29 [qwen-vl-text] coord item[14]: text=返回, bbox=[592, 98, 612, 113]
2026-08-10 16:11:20,640 INFO     29 [qwen-vl-text] coord item[15]: text=腹部:, bbox=[107, 143, 126, 165]
2026-08-10 16:11:20,640 INFO     29 [qwen-vl-text] coord item[16]: text=视诊: 外形: 腹部外形正常, bbox=[176, 180, 396, 204]
2026-08-10 16:11:20,640 INFO     29 [qwen-vl-text] coord item[17]: text=腹围: 未测, bbox=[492, 180, 576, 204]
2026-08-10 16:11:20,640 INFO     29 [qwen-vl-text] coord item[18]: text=脐部: 正常, bbox=[707, 180, 792, 204]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[19]: text=胃形: 未见, bbox=[244, 216, 328, 240]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[20]: text=肠形: 未见, bbox=[371, 216, 457, 240]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[21]: text=蠕动波: 未见, bbox=[491, 216, 595, 240]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[22]: text=腹式呼吸: 正常, bbox=[707, 216, 827, 240]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[23]: text=腹壁静脉曲张: 无, bbox=[244, 253, 380, 277]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[24]: text=腹壁其它情况: 无, bbox=[244, 289, 380, 313]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[25]: text=触诊: 全腹柔软, bbox=[176, 326, 312, 350]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[26]: text=压痛反跳痛: 无压痛及反跳痛, bbox=[244, 362, 465, 386]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[27]: text=波动感: 无, bbox=[244, 398, 354, 422]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[28]: text=振水声: 无, bbox=[473, 398, 568, 422]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[29]: text=腹部包块: 腹部未触及包块, bbox=[244, 435, 449, 459]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[30]: text=肝脏: 肝脏肋下未触及, bbox=[244, 471, 422, 495]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[31]: text=胆囊: 未触及, Murphy征阴性, bbox=[244, 508, 473, 532]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[32]: text=脾脏: 脾脏肋下未触及, bbox=[244, 544, 422, 568]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[33]: text=肾脏: 未触及, bbox=[244, 580, 354, 604]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[34]: text=输尿管压痛点: 无压痛, bbox=[242, 617, 413, 641]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[35]: text=叩诊: 肝浊音界: 正常,, bbox=[174, 653, 368, 677]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[36]: text=肝上界位于锁骨中线, 第五肋间, bbox=[514, 653, 753, 677]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[37]: text=移动性浊音: 阴性,, bbox=[241, 690, 385, 714]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[38]: text=肾区叩痛: 无, bbox=[514, 690, 630, 714]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[39]: text=听诊: 肠鸣音无明显增强或减弱, 未闻及血管杂音, bbox=[174, 726, 563, 750]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[40]: text=肛门直肠: 未查, bbox=[107, 762, 223, 786]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[41]: text=生殖器: 未查, bbox=[107, 798, 223, 822]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[42]: text=脊柱四肢:, bbox=[107, 835, 179, 859]
2026-08-10 16:11:20,641 INFO     29 [qwen-vl-text] coord item[43]: text=脊柱外形: 脊柱正常生理弯曲, bbox=[140, 871, 359, 895]
2026-08-10 16:11:20,644 INFO     29 [qwen-vl-text] page=4 — 44/44 coords, api_time=14.2s
2026-08-10 16:11:20,660 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5198409, prompt_len=1218
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["70 四 肢：四肢无畸形，未见杵状指（趾），未见静脉曲张，双下肢无凹陷性水肿", "003470 20.2.41.64", "关 节：各关节未见异常，活动无受限", "肌 肉：未见肌肉萎缩，肌张力正常。四肢肌力5级。", "神经系统：", "浅反射：双侧浅反射正常引出", "深反射：双侧深反射正常引出", "病理反射：未引出", "脑膜刺激征：阴性", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "专科情况", "神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下肢无凹陷性水肿。", "实验室及器械检查结果", "(2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm", "，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋巴结彩超", "：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord API raw response (len=1559):
[
	{"text": "70 四 肢：四肢无畸形，未见杵状指（趾），未见静脉曲张，双下肢无凹陷性水肿", "bbox": [16, 160, 748, 202]},
	{"text": "003470 20.2.41.64", "bbox": [832, 155, 958, 207]},
	{"text": "关 节：各关节未见异常，活动无受限", "bbox": [55, 209, 402, 244]},
	{"text": "肌 肉：未见肌肉萎缩，肌张力正常。四肢肌力5级。", "bbox": [55, 252, 515, 286]},
	{"text": "神经系统：", "bbox": [18, 295, 103, 325]},
	{"text": "浅反射：双侧浅反射正常引出", "bbox": [55, 338, 324, 370]},
	{"text": "深反射：双侧深反射正常引出", "bbox": [55, 378, 324, 409]},
	{"text": "病理反射：未引出", "bbox": [55, 420, 237, 451]},
	{"text": "脑膜刺激征：阴性", "bbox": [55, 462, 247, 493]},
	{"text": "003470 20.2.41.64", "bbox": [402, 338, 590, 420]},
	{"text": "003470 20.2.41.64", "bbox": [615, 338, 803, 420]},
	{"text": "003470 20.2.41.64", "bbox": [825, 338, 1000, 420]},
	{"text": "003470 20.2.41.64", "bbox": [16, 552, 165, 605]},
	{"text": "专科情况", "bbox": [460, 505, 555, 538]},
	{"text": "神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下肢无凹陷性水肿。", "bbox": [20, 595, 915, 628]},
	{"text": "实验室及器械检查结果", "bbox": [385, 640, 625, 674]},
	{"text": "(2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm", "bbox": [32, 692, 983, 720]},
	{"text": "，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋巴结彩超", "bbox": [25, 731, 980, 760]},
	{"text": "：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。", "bbox": [25, 770, 538, 800]},
	{"text": "003470 20.2.41.64", "bbox": [605, 770, 788, 843]},
	{"text": "003470 20.2.41.64", "bbox": [812, 758, 998, 843]},
	{"text": "003470 20.2.41.64", "bbox": [192, 795, 318, 843]},
	{"text": "CS 扫描全能王", "bbox": [898, 936, 980, 958]},
	{"text": "3亿人都在用的扫描App", "bbox": [898, 964, 980, 977]}
]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord API: raw_items=24, valid_items=24, elapsed=9.0s
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[0]: text=70 四 肢：四肢无畸形，未见杵状指（趾），未见静脉曲张，双下肢无凹陷性水肿, bbox=[16, 160, 748, 202]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[1]: text=003470 20.2.41.64, bbox=[832, 155, 958, 207]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[2]: text=关 节：各关节未见异常，活动无受限, bbox=[55, 209, 402, 244]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[3]: text=肌 肉：未见肌肉萎缩，肌张力正常。四肢肌力5级。, bbox=[55, 252, 515, 286]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[4]: text=神经系统：, bbox=[18, 295, 103, 325]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[5]: text=浅反射：双侧浅反射正常引出, bbox=[55, 338, 324, 370]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[6]: text=深反射：双侧深反射正常引出, bbox=[55, 378, 324, 409]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[7]: text=病理反射：未引出, bbox=[55, 420, 237, 451]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[8]: text=脑膜刺激征：阴性, bbox=[55, 462, 247, 493]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[9]: text=003470 20.2.41.64, bbox=[402, 338, 590, 420]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[10]: text=003470 20.2.41.64, bbox=[615, 338, 803, 420]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[11]: text=003470 20.2.41.64, bbox=[825, 338, 1000, 420]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[12]: text=003470 20.2.41.64, bbox=[16, 552, 165, 605]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[13]: text=专科情况, bbox=[460, 505, 555, 538]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[14]: text=神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下肢无凹陷性水肿。, bbox=[20, 595, 915, 628]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[15]: text=实验室及器械检查结果, bbox=[385, 640, 625, 674]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[16]: text=(2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm, bbox=[32, 692, 983, 720]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[17]: text=，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋巴结彩超, bbox=[25, 731, 980, 760]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[18]: text=：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。, bbox=[25, 770, 538, 800]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[19]: text=003470 20.2.41.64, bbox=[605, 770, 788, 843]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[20]: text=003470 20.2.41.64, bbox=[812, 758, 998, 843]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[21]: text=003470 20.2.41.64, bbox=[192, 795, 318, 843]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[22]: text=CS 扫描全能王, bbox=[898, 936, 980, 958]
2026-08-10 16:11:29,679 INFO     29 [qwen-vl-text] coord item[23]: text=3亿人都在用的扫描App, bbox=[898, 964, 980, 977]
2026-08-10 16:11:29,680 INFO     29 [qwen-vl-text] page=5 — 25/25 coords, api_time=9.0s
2026-08-10 16:11:29,695 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7017107, prompt_len=1576
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["2026-02-28 18:30", "男，因“咳嗽、咳痰1月余”于2026-02-28 15:23入非急诊步行入科。", "病例特点如下：1、老年期男性，起病缓，病程短。2、患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，", "伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。3、既往史：平素", "健康状况：良好。既往病史：否认高血压、冠心病、糖尿病史。传染病史：否，否认肝炎、结核或其他传染病史。预", "防接种史：正规。过敏史：否认过敏史。外伤史：否认外伤史。手术史：2年前曾行尿道结石手术，具体不详。输血", "史：否认输血史。系统回顾：无特殊。否认新冠肺炎流行病接触史。4、查体：T：36.8℃，P：75次/分，R：21次/分", "，BP：138/72mmHg。神志清楚，正常面容，皮肤巩膜无黄染，全身浅表淋巴结未扪及肿大，颈静脉无怒张。胸廓对称", "无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常，双肺叩诊呈清音，双肺呼吸音", "清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音。心界不大，心率75次/分，心律齐，各瓣膜区未闻及杂音。腹", "部外形正常，全腹柔软，无压痛及反跳痛，腹部未触及包块，肝脏肋下未触及，脾脏肋下未触及。移动性浊音阴性。", "双下肢无凹陷性水肿。浅反射：双侧浅反射正常引出。深反射：双侧深反射正常引出。病理反射：未引出。脑膜刺激", "征：阴性5、专科情况：神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下", "肢无凹陷性水肿。6、辅助检查：（2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组", "织肿块，最大截断面约77mm*60mm，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧", "胸膜肥厚、钙化。浅表淋巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。", "初步诊断：1.肺部阴影", "2.细菌性肺炎", "诊断依据：1.老年男性，起步缓，病程短", "2.咳嗽，咳淡黄色粘液痰", "3.外院胸部CT提示右肺下叶后基底段软组织肿块", "鉴别诊断。", "1.肺结核球"]

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
2026-08-10 16:11:40,916 INFO     29 [qwen-vl-text] coord API raw response (len=1891):
[
	{"text": "2026-02-28 18:30", "bbox": [31, 108, 180, 132]},
	{"text": "男，因“咳嗽、咳痰1月余”于2026-02-28 15:23入非急诊步行入科。", "bbox": [226, 147, 775, 174]},
	{"text": "病例特点如下：1、老年期男性，起病缓，病程短。2、患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，", "bbox": [71, 183, 961, 209]},
	{"text": "伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。3、既往史：平素", "bbox": [33, 220, 961, 247]},
	{"text": "健康状况：良好。既往病史：否认高血压、冠心病、糖尿病史。传染病史：否，否认肝炎、结核或其他传染病史。预", "bbox": [33, 257, 971, 284]},
	{"text": "防接种史：正规。过敏史：否认过敏史。外伤史：否认外伤史。手术史：2年前曾行尿道结石手术，具体不详。输血", "bbox": [33, 294, 969, 321]},
	{"text": "史：否认输血史。系统回顾：无特殊。否认新冠肺炎流行病接触史。4、查体：T：36.8℃，P：75次/分，R：21次/分", "bbox": [33, 331, 969, 358]},
	{"text": "，BP：138/72mmHg。神志清楚，正常面容，皮肤巩膜无黄染，全身浅表淋巴结未扪及肿大，颈静脉无怒张。胸廓对称", "bbox": [33, 368, 969, 395]},
	{"text": "无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常，双肺叩诊呈清音，双肺呼吸音", "bbox": [33, 405, 967, 432]},
	{"text": "清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音。心界不大，心率75次/分，心律齐，各瓣膜区未闻及杂音。腹", "bbox": [31, 442, 967, 469]},
	{"text": "部外形正常，全腹柔软，无压痛及反跳痛，腹部未触及包块，肝脏肋下未触及，脾脏肋下未触及。移动性浊音阴性。", "bbox": [31, 479, 956, 506]},
	{"text": "双下肢无凹陷性水肿。浅反射：双侧浅反射正常引出。深反射：双侧深反射正常引出。病理反射：未引出。脑膜刺激", "bbox": [31, 516, 965, 543]},
	{"text": "征：阴性5、专科情况：神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下", "bbox": [31, 553, 963, 580]},
	{"text": "肢无凹陷性水肿。6、辅助检查：（2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组", "bbox": [33, 590, 965, 617]},
	{"text": "织肿块，最大截断面约77mm*60mm，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧", "bbox": [33, 627, 964, 654]},
	{"text": "胸膜肥厚、钙化。浅表淋巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。", "bbox": [33, 664, 800, 691]},
	{"text": "初步诊断：1.肺部阴影", "bbox": [34, 701, 212, 728]},
	{"text": "2.细菌性肺炎", "bbox": [125, 738, 232, 765]},
	{"text": "诊断依据：1.老年男性，起步缓，病程短", "bbox": [35, 775, 357, 802]},
	{"text": "2.咳嗽，咳淡黄色粘液痰", "bbox": [125, 812, 323, 839]},
	{"text": "3.外院胸部CT提示右肺下叶后基底段软组织肿块", "bbox": [125, 849, 500, 876]},
	{"text": "鉴别诊断。", "bbox": [37, 881, 111, 900]},
	{"text": "1.肺结核球", "bbox": [160, 885, 248, 901]}
]
2026-08-10 16:11:40,916 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=11.2s
2026-08-10 16:11:40,916 INFO     29 [qwen-vl-text] coord item[0]: text=2026-02-28 18:30, bbox=[31, 108, 180, 132]
2026-08-10 16:11:40,916 INFO     29 [qwen-vl-text] coord item[1]: text=男，因“咳嗽、咳痰1月余”于2026-02-28 15:23入非急诊步行入科。, bbox=[226, 147, 775, 174]
2026-08-10 16:11:40,917 INFO     29 [qwen-vl-text] coord item[2]: text=病例特点如下：1、老年期男性，起病缓，病程短。2、患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，, bbox=[71, 183, 961, 209]
2026-08-10 16:11:40,917 INFO     29 [qwen-vl-text] coord item[3]: text=伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。3、既往史：平素, bbox=[33, 220, 961, 247]
2026-08-10 16:11:40,917 INFO     29 [qwen-vl-text] coord item[4]: text=健康状况：良好。既往病史：否认高血压、冠心病、糖尿病史。传染病史：否，否认肝炎、结核或其他传染病史。预, bbox=[33, 257, 971, 284]
2026-08-10 16:11:40,917 INFO     29 [qwen-vl-text] coord item[5]: text=防接种史：正规。过敏史：否认过敏史。外伤史：否认外伤史。手术史：2年前曾行尿道结石手术，具体不详。输血, bbox=[33, 294, 969, 321]
2026-08-10 16:11:40,917 INFO     29 [qwen-vl-text] coord item[6]: text=史：否认输血史。系统回顾：无特殊。否认新冠肺炎流行病接触史。4、查体：T：36.8℃，P：75次/分，R：21次/分, bbox=[33, 331, 969, 358]
2026-08-10 16:11:40,917 INFO     29 [qwen-vl-text] coord item[7]: text=，BP：138/72mmHg。神志清楚，正常面容，皮肤巩膜无黄染，全身浅表淋巴结未扪及肿大，颈静脉无怒张。胸廓对称, bbox=[33, 368, 969, 395]
2026-08-10 16:11:40,917 INFO     29 [qwen-vl-text] coord item[8]: text=无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常，双肺叩诊呈清音，双肺呼吸音, bbox=[33, 405, 967, 432]
2026-08-10 16:11:40,917 INFO     29 [qwen-vl-text] coord item[9]: text=清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音。心界不大，心率75次/分，心律齐，各瓣膜区未闻及杂音。腹, bbox=[31, 442, 967, 469]
2026-08-10 16:11:40,917 INFO     29 [qwen-vl-text] coord item[10]: text=部外形正常，全腹柔软，无压痛及反跳痛，腹部未触及包块，肝脏肋下未触及，脾脏肋下未触及。移动性浊音阴性。, bbox=[31, 479, 956, 506]
2026-08-10 16:11:40,917 INFO     29 [qwen-vl-text] coord item[11]: text=双下肢无凹陷性水肿。浅反射：双侧浅反射正常引出。深反射：双侧深反射正常引出。病理反射：未引出。脑膜刺激, bbox=[31, 516, 965, 543]
2026-08-10 16:11:40,917 INFO     29 [qwen-vl-text] coord item[12]: text=征：阴性5、专科情况：神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下, bbox=[31, 553, 963, 580]
2026-08-10 16:11:40,917 INFO     29 [qwen-vl-text] coord item[13]: text=肢无凹陷性水肿。6、辅助检查：（2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组, bbox=[33, 590, 965, 617]
2026-08-10 16:11:40,917 INFO     29 [qwen-vl-text] coord item[14]: text=织肿块，最大截断面约77mm*60mm，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧, bbox=[33, 627, 964, 654]
2026-08-10 16:11:40,917 INFO     29 [qwen-vl-text] coord item[15]: text=胸膜肥厚、钙化。浅表淋巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。, bbox=[33, 664, 800, 691]
2026-08-10 16:11:40,917 INFO     29 [qwen-vl-text] coord item[16]: text=初步诊断：1.肺部阴影, bbox=[34, 701, 212, 728]
2026-08-10 16:11:40,917 INFO     29 [qwen-vl-text] coord item[17]: text=2.细菌性肺炎, bbox=[125, 738, 232, 765]
2026-08-10 16:11:40,917 INFO     29 [qwen-vl-text] coord item[18]: text=诊断依据：1.老年男性，起步缓，病程短, bbox=[35, 775, 357, 802]
2026-08-10 16:11:40,917 INFO     29 [qwen-vl-text] coord item[19]: text=2.咳嗽，咳淡黄色粘液痰, bbox=[125, 812, 323, 839]
2026-08-10 16:11:40,917 INFO     29 [qwen-vl-text] coord item[20]: text=3.外院胸部CT提示右肺下叶后基底段软组织肿块, bbox=[125, 849, 500, 876]
2026-08-10 16:11:40,917 INFO     29 [qwen-vl-text] coord item[21]: text=鉴别诊断。, bbox=[37, 881, 111, 900]
2026-08-10 16:11:40,917 INFO     29 [qwen-vl-text] coord item[22]: text=1.肺结核球, bbox=[160, 885, 248, 901]
2026-08-10 16:11:40,918 INFO     29 [qwen-vl-text] page=6 — 23/23 coords, api_time=11.2s
2026-08-10 16:11:40,936 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7290009, prompt_len=1513
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共34行）
["编辑", "功能", "表格", "签名", "其他", "打印", "预览", "验证CA签名", "手工解锁", "删除", "病历参考", "更新数据", "加载全部病程", "个人模板管理", "返回", "鉴别诊断：", "1.肺结核球：多见于年轻患者，病灶多见于结核好发部位，如肺上叶尖后段和下叶背段，直径一般<3", "cm。一般无症状，病灶边界清楚，密度高，可有包膜。有时含钙化点，周围有卫星灶。", "2.急性粟粒性肺结核：应与弥漫型细支气管肺泡癌相鉴别。通常粟粒型肺结核患者年龄较轻，有发热", "，盗汗等全身中毒症状，呼吸道症状不明显。x线表现为细小、分布均匀、密度较淡的粟粒样结节病灶。", "而细支气管—肺泡细胞癌两肺多有大小不等的结节状播散病灶，边界清楚、密度较高，进行性发展和增大", "，且有进行性呼吸困难。", "3.肺炎：若无毒性症状，抗生素治疗后肺部阴影吸收缓慢，或同一部位反复发生肺炎时，应考虑到肺", "癌可能。肺部慢性炎症机化，形成团块状的炎性假瘤，也易与肺癌相混淆。但炎性假瘤往往形态不整，边", "缘不齐，核心密度较高，易伴有胸膜增厚，病灶长期无明显变化。", "4.肺脓肿：起病急，中毒症状严重，多有寒战、高热、咳嗽、咳大量脓臭痰等症状。肺部x线表现为", "均匀的大片状炎性阴影，空洞内常见较深液平。结合纤支镜检查和痰脱落细胞检查可以鉴别。", "5.纵隔淋巴瘤：颇似中央型肺癌，常为双侧性，可有发热等全身症状，需病理诊断。", "VTE血栓风险评估：创建时间:2026-02-28 15:37:11,评估节点:入院,量表名称:Padua评分,分数:0,评分描述:低危,", "预防措施:undefined", "VTE出血风险评估：创建时间:2026-02-28 18:35:54,评估节点:入院,量表名称:内科出血风险评估,分数:1,评分描述：", "低危,预防措施:undefined", "诊疗计划：1.内科护理常规,II级护理。", "2.完善必要辅助检查如血肿瘤标志物、痰液化验、胸部增强CT、支气管镜检查或浅表淋巴结及肺穿刺活检"]

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
2026-08-10 16:11:55,086 INFO     29 [qwen-vl-text] coord API raw response (len=2273):
[
	{"text": "编辑", "bbox": [21, 47, 44, 64]},
	{"text": "功能", "bbox": [59, 47, 82, 64]},
	{"text": "表格", "bbox": [96, 47, 118, 64]},
	{"text": "签名", "bbox": [132, 47, 154, 64]},
	{"text": "其他", "bbox": [169, 47, 191, 64]},
	{"text": "打印", "bbox": [19, 115, 42, 131]},
	{"text": "预览", "bbox": [56, 115, 80, 131]},
	{"text": "验证CA签名", "bbox": [93, 115, 150, 131]},
	{"text": "手工解锁", "bbox": [170, 115, 213, 131]},
	{"text": "删除", "bbox": [233, 115, 256, 131]},
	{"text": "病历参考", "bbox": [270, 115, 314, 131]},
	{"text": "更新数据", "bbox": [330, 115, 373, 131]},
	{"text": "加载全部病程", "bbox": [388, 115, 454, 131]},
	{"text": "个人模板管理", "bbox": [468, 115, 534, 131]},
	{"text": "返回", "bbox": [555, 115, 577, 131]},
	{"text": "鉴别诊断：", "bbox": [27, 167, 110, 193]},
	{"text": "1.肺结核球：多见于年轻患者，病灶多见于结核好发部位，如肺上叶尖后段和下叶背段，直径一般<3", "bbox": [159, 167, 990, 195]},
	{"text": "cm。一般无症状，病灶边界清楚，密度高，可有包膜。有时含钙化点，周围有卫星灶。", "bbox": [123, 207, 820, 237]},
	{"text": "2.急性粟粒性肺结核：应与弥漫型细支气管肺泡癌相鉴别。通常粟粒型肺结核患者年龄较轻，有发热", "bbox": [159, 247, 987, 277]},
	{"text": "，盗汗等全身中毒症状，呼吸道症状不明显。x线表现为细小、分布均匀、密度较淡的粟粒样结节病灶。", "bbox": [123, 288, 975, 317]},
	{"text": "而细支气管—肺泡细胞癌两肺多有大小不等的结节状播散病灶，边界清楚、密度较高，进行性发展和增大", "bbox": [123, 330, 983, 359]},
	{"text": "，且有进行性呼吸困难。", "bbox": [123, 370, 322, 398]},
	{"text": "3.肺炎：若无毒性症状，抗生素治疗后肺部阴影吸收缓慢，或同一部位反复发生肺炎时，应考虑到肺", "bbox": [160, 411, 982, 440]},
	{"text": "癌可能。肺部慢性炎症机化，形成团块状的炎性假瘤，也易与肺癌相混淆。但炎性假瘤往往形态不整，边", "bbox": [124, 451, 982, 480]},
	{"text": "缘不齐，核心密度较高，易伴有胸膜增厚，病灶长期无明显变化。", "bbox": [125, 491, 650, 520]},
	{"text": "4.肺脓肿：起病急，中毒症状严重，多有寒战、高热、咳嗽、咳大量脓臭痰等症状。肺部x线表现为", "bbox": [163, 531, 977, 560]},
	{"text": "均匀的大片状炎性阴影，空洞内常见较深液平。结合纤支镜检查和痰脱落细胞检查可以鉴别。", "bbox": [127, 571, 872, 600]},
	{"text": "5.纵隔淋巴瘤：颇似中央型肺癌，常为双侧性，可有发热等全身症状，需病理诊断。", "bbox": [163, 611, 836, 640]},
	{"text": "VTE血栓风险评估：创建时间:2026-02-28 15:37:11,评估节点:入院,量表名称:Padua评分,分数:0,评分描述:低危,", "bbox": [35, 652, 970, 681]},
	{"text": "预防措施:undefined", "bbox": [130, 692, 293, 720]},
	{"text": "VTE出血风险评估：创建时间:2026-02-28 18:35:54,评估节点:入院,量表名称:内科出血风险评估,分数:1,评分描述：", "bbox": [36, 732, 972, 761]},
	{"text": "低危,预防措施:undefined", "bbox": [130, 772, 340, 801]},
	{"text": "诊疗计划：1.内科护理常规,II级护理。", "bbox": [37, 812, 356, 841]},
	{"text": "2.完善必要辅助检查如血肿瘤标志物、痰液化验、胸部增强CT、支气管镜检查或浅表淋巴结及肺穿刺活检", "bbox": [128, 852, 970, 882]}
]
2026-08-10 16:11:55,086 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=14.1s
2026-08-10 16:11:55,086 INFO     29 [qwen-vl-text] coord item[0]: text=编辑, bbox=[21, 47, 44, 64]
2026-08-10 16:11:55,087 INFO     29 [qwen-vl-text] coord item[1]: text=功能, bbox=[59, 47, 82, 64]
2026-08-10 16:11:55,087 INFO     29 [qwen-vl-text] coord item[2]: text=表格, bbox=[96, 47, 118, 64]
2026-08-10 16:11:55,087 INFO     29 [qwen-vl-text] coord item[3]: text=签名, bbox=[132, 47, 154, 64]
2026-08-10 16:11:55,087 INFO     29 [qwen-vl-text] coord item[4]: text=其他, bbox=[169, 47, 191, 64]
2026-08-10 16:11:55,087 INFO     29 [qwen-vl-text] coord item[5]: text=打印, bbox=[19, 115, 42, 131]
2026-08-10 16:11:55,087 INFO     29 [qwen-vl-text] coord item[6]: text=预览, bbox=[56, 115, 80, 131]
2026-08-10 16:11:55,087 INFO     29 [qwen-vl-text] coord item[7]: text=验证CA签名, bbox=[93, 115, 150, 131]
2026-08-10 16:11:55,087 INFO     29 [qwen-vl-text] coord item[8]: text=手工解锁, bbox=[170, 115, 213, 131]
2026-08-10 16:11:55,087 INFO     29 [qwen-vl-text] coord item[9]: text=删除, bbox=[233, 115, 256, 131]
2026-08-10 16:11:55,087 INFO     29 [qwen-vl-text] coord item[10]: text=病历参考, bbox=[270, 115, 314, 131]
2026-08-10 16:11:55,087 INFO     29 [qwen-vl-text] coord item[11]: text=更新数据, bbox=[330, 115, 373, 131]
2026-08-10 16:11:55,087 INFO     29 [qwen-vl-text] coord item[12]: text=加载全部病程, bbox=[388, 115, 454, 131]
2026-08-10 16:11:55,087 INFO     29 [qwen-vl-text] coord item[13]: text=个人模板管理, bbox=[468, 115, 534, 131]
2026-08-10 16:11:55,087 INFO     29 [qwen-vl-text] coord item[14]: text=返回, bbox=[555, 115, 577, 131]
2026-08-10 16:11:55,087 INFO     29 [qwen-vl-text] coord item[15]: text=鉴别诊断：, bbox=[27, 167, 110, 193]
2026-08-10 16:11:55,088 INFO     29 [qwen-vl-text] coord item[16]: text=1.肺结核球：多见于年轻患者，病灶多见于结核好发部位，如肺上叶尖后段和下叶背段，直径一般<3, bbox=[159, 167, 990, 195]
2026-08-10 16:11:55,088 INFO     29 [qwen-vl-text] coord item[17]: text=cm。一般无症状，病灶边界清楚，密度高，可有包膜。有时含钙化点，周围有卫星灶。, bbox=[123, 207, 820, 237]
2026-08-10 16:11:55,088 INFO     29 [qwen-vl-text] coord item[18]: text=2.急性粟粒性肺结核：应与弥漫型细支气管肺泡癌相鉴别。通常粟粒型肺结核患者年龄较轻，有发热, bbox=[159, 247, 987, 277]
2026-08-10 16:11:55,088 INFO     29 [qwen-vl-text] coord item[19]: text=，盗汗等全身中毒症状，呼吸道症状不明显。x线表现为细小、分布均匀、密度较淡的粟粒样结节病灶。, bbox=[123, 288, 975, 317]
2026-08-10 16:11:55,088 INFO     29 [qwen-vl-text] coord item[20]: text=而细支气管—肺泡细胞癌两肺多有大小不等的结节状播散病灶，边界清楚、密度较高，进行性发展和增大, bbox=[123, 330, 983, 359]
2026-08-10 16:11:55,088 INFO     29 [qwen-vl-text] coord item[21]: text=，且有进行性呼吸困难。, bbox=[123, 370, 322, 398]
2026-08-10 16:11:55,088 INFO     29 [qwen-vl-text] coord item[22]: text=3.肺炎：若无毒性症状，抗生素治疗后肺部阴影吸收缓慢，或同一部位反复发生肺炎时，应考虑到肺, bbox=[160, 411, 982, 440]
2026-08-10 16:11:55,088 INFO     29 [qwen-vl-text] coord item[23]: text=癌可能。肺部慢性炎症机化，形成团块状的炎性假瘤，也易与肺癌相混淆。但炎性假瘤往往形态不整，边, bbox=[124, 451, 982, 480]
2026-08-10 16:11:55,088 INFO     29 [qwen-vl-text] coord item[24]: text=缘不齐，核心密度较高，易伴有胸膜增厚，病灶长期无明显变化。, bbox=[125, 491, 650, 520]
2026-08-10 16:11:55,088 INFO     29 [qwen-vl-text] coord item[25]: text=4.肺脓肿：起病急，中毒症状严重，多有寒战、高热、咳嗽、咳大量脓臭痰等症状。肺部x线表现为, bbox=[163, 531, 977, 560]
2026-08-10 16:11:55,088 INFO     29 [qwen-vl-text] coord item[26]: text=均匀的大片状炎性阴影，空洞内常见较深液平。结合纤支镜检查和痰脱落细胞检查可以鉴别。, bbox=[127, 571, 872, 600]
2026-08-10 16:11:55,088 INFO     29 [qwen-vl-text] coord item[27]: text=5.纵隔淋巴瘤：颇似中央型肺癌，常为双侧性，可有发热等全身症状，需病理诊断。, bbox=[163, 611, 836, 640]
2026-08-10 16:11:55,088 INFO     29 [qwen-vl-text] coord item[28]: text=VTE血栓风险评估：创建时间:2026-02-28 15:37:11,评估节点:入院,量表名称:Padua评分,分数:0,评分描述:低危,, bbox=[35, 652, 970, 681]
2026-08-10 16:11:55,088 INFO     29 [qwen-vl-text] coord item[29]: text=预防措施:undefined, bbox=[130, 692, 293, 720]
2026-08-10 16:11:55,089 INFO     29 [qwen-vl-text] coord item[30]: text=VTE出血风险评估：创建时间:2026-02-28 18:35:54,评估节点:入院,量表名称:内科出血风险评估,分数:1,评分描述：, bbox=[36, 732, 972, 761]
2026-08-10 16:11:55,089 INFO     29 [qwen-vl-text] coord item[31]: text=低危,预防措施:undefined, bbox=[130, 772, 340, 801]
2026-08-10 16:11:55,089 INFO     29 [qwen-vl-text] coord item[32]: text=诊疗计划：1.内科护理常规,II级护理。, bbox=[37, 812, 356, 841]
2026-08-10 16:11:55,089 INFO     29 [qwen-vl-text] coord item[33]: text=2.完善必要辅助检查如血肿瘤标志物、痰液化验、胸部增强CT、支气管镜检查或浅表淋巴结及肺穿刺活检, bbox=[128, 852, 970, 882]
2026-08-10 16:11:55,092 INFO     29 [qwen-vl-text] page=7 — 34/34 coords, api_time=14.1s
2026-08-10 16:11:55,112 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7301526, prompt_len=732
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共5行）
["以确诊，必要时行颅脑MRI、腹部超声、骨扫描或PET-CT等检查以利进一步疾病诊治。", "3.给予吸氧、抗感染及止血、镇痛等对症支持治疗；明确病理类型拟定下一步治疗方案。", "是否需手术治疗：否", "医师签名：", "住院医师："]

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
2026-08-10 16:11:57,866 INFO     29 [qwen-vl-text] coord API raw response (len=281):
```json
[
	{"text": "以确诊，必要时行颅脑MRI、腹部超声、骨扫描或PET-CT等检查以利进一步疾病诊治。", "bbox": [113, 47, 830, 81]},
	{"text": "3.给予吸氧、抗感染及止血、镇痛等对症支持治疗；明确病理类型拟定下一步治疗方案。", "bbox": [113, 91, 848, 124]},
	{"text": "是否需手术治疗：否", "bbox": [18, 131, 179, 160]},
	{"text": "医师签名：", "bbox": [588, 212, 672, 240]},
2026-08-10 16:11:57,866 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-10 16:11:57,867 INFO     29 [qwen-vl-text] coord API: raw_items=4, valid_items=4, elapsed=2.8s
2026-08-10 16:11:57,867 INFO     29 [qwen-vl-text] coord item[0]: text=以确诊，必要时行颅脑MRI、腹部超声、骨扫描或PET-CT等检查以利进一步疾病诊治。, bbox=[113, 47, 830, 81]
2026-08-10 16:11:57,867 INFO     29 [qwen-vl-text] coord item[1]: text=3.给予吸氧、抗感染及止血、镇痛等对症支持治疗；明确病理类型拟定下一步治疗方案。, bbox=[113, 91, 848, 124]
2026-08-10 16:11:57,867 INFO     29 [qwen-vl-text] coord item[2]: text=是否需手术治疗：否, bbox=[18, 131, 179, 160]
2026-08-10 16:11:57,867 INFO     29 [qwen-vl-text] coord item[3]: text=医师签名：, bbox=[588, 212, 672, 240]
2026-08-10 16:11:57,870 INFO     29 [qwen-vl-text] page=8 — 5/5 coords, api_time=2.8s
2026-08-10 16:11:57,873 INFO     29 [qwen-vl-text] new_positions (1074):
[[0, 386.478, 454.68, 8.33, 28.56], [0, 32.838, 208.816, 27.965, 44.625], [0, 32.838, 799.9, 51.765, 69.02], [0, 96.83, 804.952, 74.97, 91.63], [0, 96.83, 806.636, 98.77, 115.42999999999999], [0, 96.83, 804.952, 121.975, 138.635], [0, 96.83, 804.952, 145.18, 161.84], [0, 96.83, 804.952, 168.385, 185.045], [0, 96.83, 235.76, 192.185, 208.25], [0, 32.838, 235.76, 215.39, 232.04999999999998], [0, 94.304, 385.63599999999997, 238.595, 255.255], [0, 94.304, 415.948, 261.8, 278.46], [0, 94.304, 220.60399999999998, 285.005, 301.66499999999996], [0, 94.304, 235.76, 308.21, 324.87], [0, 94.304, 235.76, 331.41499999999996, 348.075], [0, 94.304, 393.214, 355.215, 371.875], [0, 94.304, 235.76, 378.41999999999996, 395.08], [0, 94.304, 227.34, 401.625, 418.28499999999997], [0, 33.68, 346.904, 425.42499999999995, 442.085], [0, 92.61999999999999, 258.49399999999997, 448.63, 465.28999999999996], [0, 92.61999999999999, 227.34, 471.835, 488.495], [0, 92.61999999999999, 508.568, 495.03999999999996, 511.7], [0, 643.288, 789.7959999999999, 495.03999999999996, 506.34499999999997], [0, 810.846, 831.896, 512.89, 520.625], [0, 799.9, 840.3159999999999, 523.6, 531.3349999999999], [0, 27.785999999999998, 95.146, 519.435, 527.765], [0, 124.616, 191.976, 519.435, 527.765], [1, 88.41, 623.0799999999999, 145.775, 163.625], [1, 21.05, 475.72999999999996, 170.765, 187.42499999999998], [1, 21.05, 307.33, 195.755, 212.415], [1, 323.328, 737.592, 243.95, 261.205], [1, 378.9, 492.57, 292.74, 312.96999999999997], [1, 20.208, 90.93599999999999, 324.275, 340.935], [1, 50.519999999999996, 144.82399999999998, 349.265, 365.33], [1, 213.02599999999998, 319.118, 349.265, 365.33], [1, 399.108, 502.674, 349.265, 365.33], [1, 575.086, 705.596, 349.265, 365.33], [1, 51.361999999999995, 138.088, 378.41999999999996, 394.48499999999996], [1, 213.02599999999998, 295.542, 378.41999999999996, 394.48499999999996], [1, 399.108, 478.256, 378.41999999999996, 394.48499999999996], [1, 574.244, 654.2339999999999, 378.41999999999996, 394.48499999999996], [1, 51.361999999999995, 129.668, 405.78999999999996, 421.85499999999996], [1, 213.02599999999998, 327.538, 405.78999999999996, 421.85499999999996], [1, 399.108, 511.094, 405.78999999999996, 421.85499999999996], [1, 574.244, 654.2339999999999, 405.78999999999996, 421.85499999999996], [1, 51.361999999999995, 129.668, 433.15999999999997, 449.22499999999997], [1, 213.02599999999998, 309.856, 433.15999999999997, 449.22499999999997], [1, 398.26599999999996, 510.252, 433.15999999999997, 449.22499999999997], [2, 79.148, 152.402, 4.165, 22.015], [2, 114.512, 130.51, 30.939999999999998, 47.599999999999994], [2, 186.924, 251.75799999999998, 30.939999999999998, 47.599999999999994], [2, 114.512, 130.51, 54.739999999999995, 73.185], [2, 186.924, 349.43, 54.739999999999995, 71.99499999999999], [2, 115.354, 380.584, 81.515, 98.175], [2, 115.354, 315.75, 105.91, 123.16499999999999], [2, 115.354, 419.316, 131.495, 148.75], [2, 115.354, 130.51, 157.07999999999998, 173.73999999999998], [2, 186.924, 283.75399999999996, 157.07999999999998, 173.73999999999998], [2, 115.354, 130.51, 182.07, 199.325], [2, 186.924, 244.17999999999998, 182.07, 199.325], [2, 115.354, 130.51, 208.25, 224.315], [2, 154.928, 170.926, 208.25, 224.315], [2, 186.924, 298.90999999999997, 208.25, 224.315], [2, 115.354, 234.076, 232.64499999999998, 249.30499999999998], [2, 84.2, 354.48199999999997, 258.22999999999996, 274.89], [2, 84.2, 152.402, 282.625, 299.28499999999997], [2, 116.196, 322.486, 307.615, 324.275], [2, 116.196, 508.568, 332.01, 348.66999999999996], [2, 116.196, 508.568, 357.0, 373.65999999999997], [2, 116.196, 586.0319999999999, 381.395, 398.055], [2, 116.196, 630.658, 406.385, 423.04499999999996], [2, 116.196, 337.642, 430.78, 447.44], [2, 130.51, 152.402, 455.77, 471.835], [2, 112.828, 270.282, 480.76, 497.41999999999996], [2, 419.316, 527.092, 480.76, 497.41999999999996], [2, 634.8679999999999, 710.648, 480.16499999999996, 496.825], [2, 112.828, 270.282, 508.72499999999997, 525.385], [2, 419.316, 582.664, 508.72499999999997, 525.385], [2, 725.804, 789.7959999999999, 523.6, 535.5], [3, 24.418, 511.094, 69.02, 83.3], [3, 31.154, 77.464, 88.06, 108.28999999999999], [3, 154.928, 298.068, 91.63, 114.24], [3, 347.746, 463.09999999999997, 91.63, 114.24], [3, 541.406, 656.76, 91.63, 114.24], [3, 734.2239999999999, 828.528, 91.63, 114.24], [3, 31.996, 814.2139999999999, 111.86, 132.09], [3, 31.996, 94.304, 139.23, 158.26999999999998], [3, 69.886, 447.94399999999996, 165.41, 184.45], [3, 69.886, 481.62399999999997, 192.185, 211.225], [3, 69.886, 258.49399999999997, 218.36499999999998, 238.0], [3, 69.886, 619.712, 245.14, 264.18], [3, 33.68, 94.304, 272.51, 291.55], [3, 69.886, 714.016, 298.69, 317.72999999999996], [3, 69.886, 497.62199999999996, 324.87, 343.90999999999997], [3, 69.886, 207.974, 351.645, 370.685], [3, 69.886, 480.782, 377.825, 396.865], [3, 139.772, 598.662, 404.59999999999997, 423.64], [3, 139.772, 344.378, 430.78, 449.82], [3, 139.772, 244.17999999999998, 456.96, 475.405], [3, 139.772, 261.86199999999997, 483.14, 502.17999999999995], [3, 10.946, 210.5, 508.72499999999997, 527.765], [3, 347.746, 463.09999999999997, 498.60999999999996, 529.55], [3, 532.986, 648.34, 498.60999999999996, 529.55], [3, 719.91, 835.264, 498.60999999999996, 529.55], [3, 26.944, 94.304, 359.97499999999997, 385.56], [3, 94.304, 161.664, 359.97499999999997, 385.56], [3, 161.664, 229.024, 359.97499999999997, 385.56], [3, 229.024, 296.384, 359.97499999999997, 385.56], [3, 296.384, 363.74399999999997, 359.97499999999997, 385.56], [3, 363.74399999999997, 431.104, 359.97499999999997, 385.56], [3, 431.104, 498.464, 359.97499999999997, 385.56], [3, 498.464, 565.824, 359.97499999999997, 385.56], [3, 565.824, 633.184, 359.97499999999997, 385.56], [3, 633.184, 700.544, 359.97499999999997, 385.56], [3, 700.544, 767.904, 359.97499999999997, 385.56], [3, 767.904, 835.264, 359.97499999999997, 385.56], [3, 26.944, 94.304, 333.79499999999996, 358.78499999999997], [3, 94.304, 161.664, 333.79499999999996, 358.78499999999997], [3, 161.664, 229.024, 333.79499999999996, 358.78499999999997], [3, 229.024, 296.384, 333.79499999999996, 358.78499999999997], [3, 296.384, 363.74399999999997, 333.79499999999996, 358.78499999999997], [3, 363.74399999999997, 431.104, 333.79499999999996, 358.78499999999997], [3, 431.104, 498.464, 333.79499999999996, 358.78499999999997], [3, 498.464, 565.824, 333.79499999999996, 358.78499999999997], [3, 565.824, 633.184, 333.79499999999996, 358.78499999999997], [3, 633.184, 700.544, 333.79499999999996, 358.78499999999997], [3, 700.544, 767.904, 333.79499999999996, 358.78499999999997], [3, 767.904, 835.264, 333.79499999999996, 358.78499999999997], [3, 26.944, 94.304, 307.615, 332.60499999999996], [3, 94.304, 161.664, 307.615, 332.60499999999996], [3, 161.664, 229.024, 307.615, 332.60499999999996], [3, 229.024, 296.384, 307.615, 332.60499999999996], [3, 296.384, 363.74399999999997, 307.615, 332.60499999999996], [3, 363.74399999999997, 431.104, 307.615, 332.60499999999996], [3, 431.104, 498.464, 307.615, 332.60499999999996], [3, 498.464, 565.824, 307.615, 332.60499999999996], [3, 565.824, 633.184, 307.615, 332.60499999999996], [3, 633.184, 700.544, 307.615, 332.60499999999996], [3, 700.544, 767.904, 307.615, 332.60499999999996], [3, 767.904, 835.264, 307.615, 332.60499999999996], [3, 26.944, 94.304, 281.435, 306.425], [3, 94.304, 161.664, 281.435, 306.425], [3, 161.664, 229.024, 281.435, 306.425], [3, 229.024, 296.384, 281.435, 306.425], [3, 296.384, 363.74399999999997, 281.435, 306.425], [3, 363.74399999999997, 431.104, 281.435, 306.425], [3, 431.104, 498.464, 281.435, 306.425], [3, 498.464, 565.824, 281.435, 306.425], [3, 565.824, 633.184, 281.435, 306.425], [3, 633.184, 700.544, 281.435, 306.425], [3, 700.544, 767.904, 281.435, 306.425], [3, 767.904, 835.264, 281.435, 306.425], [3, 26.944, 94.304, 255.255, 280.245], [3, 94.304, 161.664, 255.255, 280.245], [3, 161.664, 229.024, 255.255, 280.245], [3, 229.024, 296.384, 255.255, 280.245], [3, 296.384, 363.74399999999997, 255.255, 280.245], [3, 363.74399999999997, 431.104, 255.255, 280.245], [3, 431.104, 498.464, 255.255, 280.245], [3, 498.464, 565.824, 255.255, 280.245], [3, 565.824, 633.184, 255.255, 280.245], [3, 633.184, 700.544, 255.255, 280.245], [3, 700.544, 767.904, 255.255, 280.245], [3, 767.904, 835.264, 255.255, 280.245], [3, 26.944, 94.304, 229.075, 254.065], [3, 94.304, 161.664, 229.075, 254.065], [3, 161.664, 229.024, 229.075, 254.065], [3, 229.024, 296.384, 229.075, 254.065], [3, 296.384, 363.74399999999997, 229.075, 254.065], [3, 363.74399999999997, 431.104, 229.075, 254.065], [3, 431.104, 498.464, 229.075, 254.065], [3, 498.464, 565.824, 229.075, 254.065], [3, 565.824, 633.184, 229.075, 254.065], [3, 633.184, 700.544, 229.075, 254.065], [3, 700.544, 767.904, 229.075, 254.065], [3, 767.904, 835.264, 229.075, 254.065], [3, 26.944, 94.304, 202.89499999999998, 227.885], [3, 94.304, 161.664, 202.89499999999998, 227.885], [3, 161.664, 229.024, 202.89499999999998, 227.885], [3, 229.024, 296.384, 202.89499999999998, 227.885], [3, 296.384, 363.74399999999997, 202.89499999999998, 227.885], [3, 363.74399999999997, 431.104, 202.89499999999998, 227.885], [3, 431.104, 498.464, 202.89499999999998, 227.885], [3, 498.464, 565.824, 202.89499999999998, 227.885], [3, 565.824, 633.184, 202.89499999999998, 227.885], [3, 633.184, 700.544, 202.89499999999998, 227.885], [3, 700.544, 767.904, 202.89499999999998, 227.885], [3, 767.904, 835.264, 202.89499999999998, 227.885], [3, 26.944, 94.304, 176.715, 201.70499999999998], [3, 94.304, 161.664, 176.715, 201.70499999999998], [3, 161.664, 229.024, 176.715, 201.70499999999998], [3, 229.024, 296.384, 176.715, 201.70499999999998], [3, 296.384, 363.74399999999997, 176.715, 201.70499999999998], [3, 363.74399999999997, 431.104, 176.715, 201.70499999999998], [3, 431.104, 498.464, 176.715, 201.70499999999998], [3, 498.464, 565.824, 176.715, 201.70499999999998], [3, 565.824, 633.184, 176.715, 201.70499999999998], [3, 633.184, 700.544, 176.715, 201.70499999999998], [3, 700.544, 767.904, 176.715, 201.70499999999998], [3, 767.904, 835.264, 176.715, 201.70499999999998], [3, 26.944, 94.304, 150.535, 175.525], [3, 94.304, 161.664, 150.535, 175.525], [3, 161.664, 229.024, 150.535, 175.525], [3, 229.024, 296.384, 150.535, 175.525], [3, 296.384, 363.74399999999997, 150.535, 175.525], [3, 363.74399999999997, 431.104, 150.535, 175.525], [3, 431.104, 498.464, 150.535, 175.525], [3, 498.464, 565.824, 150.535, 175.525], [3, 565.824, 633.184, 150.535, 175.525], [3, 633.184, 700.544, 150.535, 175.525], [3, 700.544, 767.904, 150.535, 175.525], [3, 767.904, 835.264, 150.535, 175.525], [3, 26.944, 94.304, 124.35499999999999, 149.345], [3, 94.304, 161.664, 124.35499999999999, 149.345], [3, 161.664, 229.024, 124.35499999999999, 149.345], [3, 229.024, 296.384, 124.35499999999999, 149.345], [3, 296.384, 363.74399999999997, 124.35499999999999, 149.345], [3, 363.74399999999997, 431.104, 124.35499999999999, 149.345], [3, 431.104, 498.464, 124.35499999999999, 149.345], [3, 498.464, 565.824, 124.35499999999999, 149.345], [3, 565.824, 633.184, 124.35499999999999, 149.345], [3, 633.184, 700.544, 124.35499999999999, 149.345], [3, 700.544, 767.904, 124.35499999999999, 149.345], [3, 767.904, 835.264, 124.35499999999999, 149.345], [3, 26.944, 94.304, 98.175, 123.16499999999999], [3, 94.304, 161.664, 98.175, 123.16499999999999], [3, 161.664, 229.024, 98.175, 123.16499999999999], [3, 229.024, 296.384, 98.175, 123.16499999999999], [3, 296.384, 363.74399999999997, 98.175, 123.16499999999999], [3, 363.74399999999997, 431.104, 98.175, 123.16499999999999], [3, 431.104, 498.464, 98.175, 123.16499999999999], [3, 498.464, 565.824, 98.175, 123.16499999999999], [3, 565.824, 633.184, 98.175, 123.16499999999999], [3, 633.184, 700.544, 98.175, 123.16499999999999], [3, 700.544, 767.904, 98.175, 123.16499999999999], [3, 767.904, 835.264, 98.175, 123.16499999999999], [3, 26.944, 94.304, 71.99499999999999, 96.985], [3, 94.304, 161.664, 71.99499999999999, 96.985], [3, 161.664, 229.024, 71.99499999999999, 96.985], [3, 229.024, 296.384, 71.99499999999999, 96.985], [3, 296.384, 363.74399999999997, 71.99499999999999, 96.985], [3, 363.74399999999997, 431.104, 71.99499999999999, 96.985], [3, 431.104, 498.464, 71.99499999999999, 96.985], [3, 498.464, 565.824, 71.99499999999999, 96.985], [3, 565.824, 633.184, 71.99499999999999, 96.985], [3, 633.184, 700.544, 71.99499999999999, 96.985], [3, 700.544, 767.904, 71.99499999999999, 96.985], [3, 767.904, 835.264, 71.99499999999999, 96.985], [3, 26.944, 94.304, 45.815, 70.80499999999999], [3, 94.304, 161.664, 45.815, 70.80499999999999], [3, 161.664, 229.024, 45.815, 70.80499999999999], [3, 229.024, 296.384, 45.815, 70.80499999999999], [3, 296.384, 363.74399999999997, 45.815, 70.80499999999999], [3, 363.74399999999997, 431.104, 45.815, 70.80499999999999], [3, 431.104, 498.464, 45.815, 70.80499999999999], [3, 498.464, 565.824, 45.815, 70.80499999999999], [3, 565.824, 633.184, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 633.184, 700.544, 45.815, 70.80499999999999], [3, 734.2239999999999, 828.528, 91.63, 114.24], [4, 86.726, 104.408, 22.61, 32.129999999999995], [4, 115.354, 133.036, 22.61, 32.129999999999995], [4, 143.14, 160.822, 22.61, 32.129999999999995], [4, 171.768, 188.608, 22.61, 32.129999999999995], [4, 199.554, 217.236, 22.61, 32.129999999999995], [4, 84.2, 101.03999999999999, 58.309999999999995, 67.235], [4, 112.828, 130.51, 58.309999999999995, 67.235], [4, 141.456, 185.23999999999998, 58.309999999999995, 67.235], [4, 201.238, 234.91799999999998, 58.309999999999995, 67.235], [4, 250.07399999999998, 267.756, 58.309999999999995, 67.235], [4, 278.702, 312.382, 58.309999999999995, 67.235], [4, 324.17, 357.84999999999997, 58.309999999999995, 67.235], [4, 369.638, 420.15799999999996, 58.309999999999995, 67.235], [4, 431.94599999999997, 482.466, 58.309999999999995, 67.235], [4, 498.464, 515.304, 58.309999999999995, 67.235], [4, 90.094, 106.092, 85.085, 98.175], [4, 148.192, 333.432, 107.1, 121.38], [4, 414.264, 484.99199999999996, 107.1, 121.38], [4, 595.294, 666.864, 107.1, 121.38], [4, 205.44799999999998, 276.176, 128.51999999999998, 142.79999999999998], [4, 312.382, 384.794, 128.51999999999998, 142.79999999999998], [4, 413.42199999999997, 500.99, 128.51999999999998, 142.79999999999998], [4, 595.294, 696.334, 128.51999999999998, 142.79999999999998], [4, 205.44799999999998, 319.96, 150.535, 164.815], [4, 205.44799999999998, 319.96, 171.95499999999998, 186.23499999999999], [4, 148.192, 262.704, 193.97, 208.25], [4, 205.44799999999998, 391.53, 215.39, 229.67], [4, 205.44799999999998, 298.068, 236.81, 251.08999999999997], [4, 398.26599999999996, 478.256, 236.81, 251.08999999999997], [4, 205.44799999999998, 378.058, 258.825, 273.10499999999996], [4, 205.44799999999998, 355.324, 280.245, 294.525], [4, 205.44799999999998, 398.26599999999996, 302.26, 316.53999999999996], [4, 205.44799999999998, 355.324, 323.68, 337.96], [4, 205.44799999999998, 298.068, 345.09999999999997, 359.38], [4, 203.76399999999998, 347.746, 367.115, 381.395], [4, 146.50799999999998, 309.856, 388.53499999999997, 402.815], [4, 432.788, 634.026, 388.53499999999997, 402.815], [4, 202.922, 324.17, 410.54999999999995, 424.83], [4, 432.788, 530.46, 410.54999999999995, 424.83], [4, 146.50799999999998, 474.046, 431.96999999999997, 446.25], [4, 90.094, 187.766, 453.39, 467.66999999999996], [4, 90.094, 187.766, 474.81, 489.09], [4, 90.094, 150.718, 496.825, 511.10499999999996], [4, 117.88, 302.27799999999996, 518.245, 532.525], [5, 13.472, 629.816, 95.19999999999999, 120.19], [5, 700.544, 806.636, 92.225, 123.16499999999999], [5, 46.309999999999995, 338.484, 124.35499999999999, 145.18], [5, 46.309999999999995, 433.63, 149.94, 170.17], [5, 15.155999999999999, 86.726, 175.525, 193.375], [5, 46.309999999999995, 272.808, 201.10999999999999, 220.14999999999998], [5, 46.309999999999995, 272.808, 224.91, 243.355], [5, 46.309999999999995, 199.554, 249.89999999999998, 268.34499999999997], [5, 46.309999999999995, 207.974, 274.89, 293.335], [5, 338.484, 496.78, 201.10999999999999, 249.89999999999998], [5, 517.8299999999999, 676.126, 201.10999999999999, 249.89999999999998], [5, 694.65, 842.0, 201.10999999999999, 249.89999999999998], [5, 13.472, 138.93, 328.44, 359.97499999999997], [5, 387.32, 467.31, 300.47499999999997, 320.11], [5, 16.84, 770.43, 354.025, 373.65999999999997], [5, 324.17, 526.25, 380.79999999999995, 401.03], [5, 26.944, 827.6859999999999, 411.74, 428.4], [5, 21.05, 825.16, 434.945, 452.2], [5, 21.05, 452.996, 458.15, 476.0], [5, 509.40999999999997, 663.496, 458.15, 501.585], [5, 683.704, 840.3159999999999, 451.01, 501.585], [5, 161.664, 267.756, 473.025, 501.585], [5, 756.116, 825.16, 556.92, 570.01], [5, 756.116, 825.16, 573.5799999999999, 581.3149999999999], [5, 756.116, 825.16, 573.5799999999999, 581.3149999999999], [6, 26.102, 151.56, 64.25999999999999, 78.53999999999999], [6, 190.292, 652.55, 87.46499999999999, 103.53], [6, 59.782, 809.1619999999999, 108.88499999999999, 124.35499999999999], [6, 27.785999999999998, 809.1619999999999, 130.9, 146.965], [6, 27.785999999999998, 817.582, 152.915, 168.98], [6, 27.785999999999998, 815.898, 174.92999999999998, 190.995], [6, 27.785999999999998, 815.898, 196.945, 213.01], [6, 27.785999999999998, 815.898, 218.95999999999998, 235.02499999999998], [6, 27.785999999999998, 814.2139999999999, 240.975, 257.03999999999996], [6, 26.102, 814.2139999999999, 262.99, 279.055], [6, 26.102, 804.952, 285.005, 301.07], [6, 26.102, 812.53, 307.02, 323.085], [6, 26.102, 810.846, 329.03499999999997, 345.09999999999997], [6, 27.785999999999998, 812.53, 351.05, 367.115], [6, 27.785999999999998, 811.688, 373.065, 389.13], [6, 27.785999999999998, 673.6, 395.08, 411.145], [6, 28.628, 178.504, 417.09499999999997, 433.15999999999997], [6, 105.25, 195.344, 439.10999999999996, 455.17499999999995], [6, 29.47, 300.594, 461.125, 477.19], [6, 105.25, 271.966, 483.14, 499.205], [6, 105.25, 421.0, 505.155, 521.22], [6, 31.154, 93.462, 524.1949999999999, 535.5], [6, 134.72, 208.816, 526.5749999999999, 536.095], [7, 17.682, 37.048, 27.965, 38.08], [7, 49.678, 69.044, 27.965, 38.08], [7, 80.832, 99.356, 27.965, 38.08], [7, 111.14399999999999, 129.668, 27.965, 38.08], [7, 142.298, 160.822, 27.965, 38.08], [7, 15.998, 35.364, 68.425, 77.945], [7, 47.152, 67.36, 68.425, 77.945], [7, 78.306, 126.3, 68.425, 77.945], [7, 143.14, 179.346, 68.425, 77.945], [7, 196.186, 215.552, 68.425, 77.945], [7, 227.34, 264.388, 68.425, 77.945], [7, 277.86, 314.066, 68.425, 77.945], [7, 326.69599999999997, 382.268, 68.425, 77.945], [7, 394.056, 449.628, 68.425, 77.945], [7, 467.31, 485.834, 68.425, 77.945], [7, 22.733999999999998, 92.61999999999999, 99.365, 114.835], [7, 133.878, 833.5799999999999, 99.365, 116.02499999999999], [7, 103.566, 690.4399999999999, 123.16499999999999, 141.015], [7, 133.878, 831.054, 146.965, 164.815], [7, 103.566, 820.9499999999999, 171.35999999999999, 188.61499999999998], [7, 103.566, 827.6859999999999, 196.35, 213.605], [7, 103.566, 271.12399999999997, 220.14999999999998, 236.81], [7, 134.72, 826.8439999999999, 244.545, 261.8], [7, 104.408, 826.8439999999999, 268.34499999999997, 285.59999999999997], [7, 105.25, 547.3, 292.145, 309.4], [7, 137.246, 822.634, 315.945, 333.2], [7, 106.934, 734.2239999999999, 339.745, 357.0], [7, 137.246, 703.9119999999999, 363.54499999999996, 380.79999999999995], [7, 29.47, 816.74, 387.94, 405.195], [7, 109.46, 246.706, 411.74, 428.4], [7, 30.311999999999998, 818.424, 435.53999999999996, 452.79499999999996], [7, 109.46, 286.28, 459.34, 476.59499999999997], [7, 31.154, 299.752, 483.14, 500.395], [7, 107.776, 816.74, 506.94, 524.79], [8, 95.146, 698.86, 27.965, 48.195], [8, 95.146, 714.016, 54.144999999999996, 73.78], [8, 15.155999999999999, 150.718, 77.945, 95.19999999999999], [8, 495.096, 565.824, 126.14, 142.79999999999998], [8, 495.096, 565.824, 126.14, 142.79999999999998]]
2026-08-10 16:11:57,874 INFO     29 [qwen-vl-text] ═══ DONE ═══ 1074 positions, pages=9, time=182.4s
2026-08-10 16:11:57,892 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 16:11:57,893 INFO     29 [Trace] task=5212989c | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Extractor:Admission | outputs={"chunks": "1 items, types={'AdmissionRecord': 1}", "html": "", "json": "2438 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 11}"}
2026-08-10 16:11:57,893 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 16:11:57,894 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:11:57.893+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:11:57,905 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:11:57,906 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:11:57,906 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 16:11:57,906 INFO     29 [qwen-vl-text] positions(26): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:11:57,906 INFO     29 [qwen-vl-text] page grouping: [9], lines per page: [26]
2026-08-10 16:11:58,271 INFO     29 [qwen-vl-text] page=9, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 16:11:58,272 INFO     29 [qwen-vl-text] LLM extraction start, text_len=468
2026-08-10 16:11:58,272 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:11:58,272 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 1933, \"bbox_end\": 1958, \"encounter_dates\": [\"2026-03-13\"], \"department\": \"老年医学呼吸内科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "影像检查报告单\n病人 ID:\n姓名:\n性别: 男\n年龄: 67岁\n申请科室: 老年医学呼吸内科\n机器型号: SE-MR4\n住院号\n检查部位: 颅脑颅脑MR平扫及增强+DWI,*钆特酸葡胺注射液【广西HR】\n检查日期: 2026-03-13\n(此报告仅供临床医师诊断参考,不作为疾病证明)\n检查所见:\n左侧基底节区、两侧放射冠、右侧侧脑室前后角旁见小斑片状、斑点状等T1、稍\n长T2信号灶,FLAIR呈高信号,边界欠清,DWI未见弥散受限;余脑实质信号未见异\n常,DWI未见明确弥散受限区,增强扫描未见异常强化灶;静脉窦强化充盈良好,未\n见异常;各脑室及脑沟、裂、池对称性轻度增宽;中线结构无移位。\n诊断意见:\n脑白质病变--改良Fasekas1级;轻度脑萎缩。\n检查技师: 唐成\n报告医师: 郭仟\n审核医师: 张\n报告日期: 2026-03-16 15:13:19\n审核日期: 2026-03-16 18:28:39\n地址: 广西医科大学第一附属医院放射科\n联系电话: 0771-5356934\n“广西HR”解释: 广西影像检查项目互认",
    "role": "user"
  }
]
2026-08-10 16:12:01,100 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:12:01,100 INFO     29 [qwen-vl-text] LLM output (len=492):
{
  "exam_date": "2026-03-13",
  "report_date": "2026-03-16",
  "exam_name": "颅脑MR平扫及增强+DWI",
  "exam_category": "imaging",
  "body_part": "颅脑",
  "patient_name": null,
  "patient_gender": "男",
  "department": "老年医学呼吸内科",
  "bed_number": null,
  "findings": "左侧基底节区、两侧放射冠、右侧侧脑室前后角旁见小斑片状、斑点状等T1、稍长T2信号灶,FLAIR呈高信号,边界欠清,DWI未见弥散受限;余脑实质信号未见异常,DWI未见明确弥散受限区,增强扫描未见异常强化灶;静脉窦强化充盈良好,未见异常;各脑室及脑沟、裂、池对称性轻度增宽;中线结构无移位。",
  "conclusion": "脑白质病变--改良Fasekas1级;轻度脑萎缩。",
  "physician": "郭仟",
  "reviewer": "张"
}
2026-08-10 16:12:01,108 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4405620, prompt_len=1159
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["影像检查报告单", "病人 ID:", "姓名:", "性别: 男", "年龄: 67岁", "申请科室: 老年医学呼吸内科", "机器型号: SE-MR4", "住院号", "检查部位: 颅脑颅脑MR平扫及增强+DWI,*钆特酸葡胺注射液【广西HR】", "检查日期: 2026-03-13", "(此报告仅供临床医师诊断参考,不作为疾病证明)", "检查所见:", "左侧基底节区、两侧放射冠、右侧侧脑室前后角旁见小斑片状、斑点状等T1、稍", "长T2信号灶,FLAIR呈高信号,边界欠清,DWI未见弥散受限;余脑实质信号未见异", "常,DWI未见明确弥散受限区,增强扫描未见异常强化灶;静脉窦强化充盈良好,未", "见异常;各脑室及脑沟、裂、池对称性轻度增宽;中线结构无移位。", "诊断意见:", "脑白质病变--改良Fasekas1级;轻度脑萎缩。", "检查技师: 唐成", "报告医师: 郭仟", "审核医师: 张", "报告日期: 2026-03-16 15:13:19", "审核日期: 2026-03-16 18:28:39", "地址: 广西医科大学第一附属医院放射科", "联系电话: 0771-5356934", "“广西HR”解释: 广西影像检查项目互认"]

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
2026-08-10 16:12:13,901 INFO     29 [qwen-vl-text] coord API raw response (len=2339):
[
	{"text": "影像检查报告单", "bbox": [360, 141, 643, 172]},
	{"text": "病人 ID:", "bbox": [78, 221, 155, 237], "bbox": [78, 221, 155, 237]},
	{"text": "姓名:", "bbox": [340, 220, 388, 236], "bbox": [340, 220, 388, 236]},
	{"text": "性别: 男", "bbox": [529, 219, 625, 236], "bbox": [529, 219, 625, 236]},
	{"text": "年龄: 67岁", "bbox": [676, 219, 801, 236], "bbox": [676, 219, 801, 236]},
	{"text": "申请科室: 老年医学呼吸内科", "bbox": [80, 246, 327, 271], "bbox": [80, 246, 327, 271]},
	{"text": "机器型号: SE-MR4", "bbox": [340, 247, 513, 264], "bbox": [340, 247, 513, 264]},
	{"text": "住院号", "bbox": [676, 247, 736, 264], "bbox": [676, 247, 736, 264]},
	{"text": "检查部位: 颅脑颅脑MR平扫及增强+DWI,*钆特酸葡胺注射液【广西HR】", "bbox": [78, 273, 590, 306], "bbox": [78, 273, 590, 306]},
	{"text": "检查日期: 2026-03-13", "bbox": [606, 280, 863, 297], "bbox": [606, 280, 863, 297]},
	{"text": "(此报告仅供临床医师诊断参考,不作为疾病证明)", "bbox": [83, 310, 574, 328], "bbox": [83, 310, 574, 328]},
	{"text": "检查所见:", "bbox": [78, 334, 176, 350], "bbox": [78, 334, 176, 350]},
	{"text": "左侧基底节区、两侧放射冠、右侧侧脑室前后角旁见小斑片状、斑点状等T1、稍", "bbox": [82, 359, 927, 377], "bbox": [82, 359, 927, 377]},
	{"text": "长T2信号灶,FLAIR呈高信号,边界欠清,DWI未见弥散受限;余脑实质信号未见异", "bbox": [82, 382, 904, 400], "bbox": [82, 382, 904, 400]},
	{"text": "常,DWI未见明确弥散受限区,增强扫描未见异常强化灶;静脉窦强化充盈良好,未", "bbox": [82, 405, 915, 423], "bbox": [82, 405, 915, 423]},
	{"text": "见异常;各脑室及脑沟、裂、池对称性轻度增宽;中线结构无移位。", "bbox": [82, 428, 753, 446], "bbox": [82, 428, 753, 446]},
	{"text": "诊断意见:", "bbox": [74, 614, 171, 631], "bbox": [74, 614, 171, 631]},
	{"text": "脑白质病变--改良Fasekas1级;轻度脑萎缩。", "bbox": [118, 642, 560, 660], "bbox": [118, 642, 560, 660]},
	{"text": "检查技师: 唐成", "bbox": [73, 768, 213, 784], "bbox": [73, 768, 213, 784]},
	{"text": "报告医师: 郭仟", "bbox": [259, 768, 402, 784], "bbox": [259, 768, 402, 784]},
	{"text": "审核医师: 张", "bbox": [448, 768, 536, 784], "bbox": [448, 768, 536, 784]},
	{"text": "报告日期: 2026-03-16 15:13:19", "bbox": [73, 792, 376, 809], "bbox": [73, 792, 376, 809]},
	{"text": "审核日期: 2026-03-16 18:28:39", "bbox": [560, 792, 866, 809], "bbox": [560, 792, 866, 809]},
	{"text": "地址: 广西医科大学第一附属医院放射科", "bbox": [77, 827, 379, 842], "bbox": [77, 827, 379, 842]},
	{"text": "联系电话: 0771-5356934", "bbox": [404, 827, 590, 842], "bbox": [404, 827, 590, 842]},
	{"text": "“广西HR”解释: 广西影像检查项目互认", "bbox": [622, 827, 920, 842], "bbox": [622, 827, 920, 842]}
]
2026-08-10 16:12:13,901 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=12.8s
2026-08-10 16:12:13,901 INFO     29 [qwen-vl-text] coord item[0]: text=影像检查报告单, bbox=[360, 141, 643, 172]
2026-08-10 16:12:13,901 INFO     29 [qwen-vl-text] coord item[1]: text=病人 ID:, bbox=[78, 221, 155, 237]
2026-08-10 16:12:13,901 INFO     29 [qwen-vl-text] coord item[2]: text=姓名:, bbox=[340, 220, 388, 236]
2026-08-10 16:12:13,901 INFO     29 [qwen-vl-text] coord item[3]: text=性别: 男, bbox=[529, 219, 625, 236]
2026-08-10 16:12:13,902 INFO     29 [qwen-vl-text] coord item[4]: text=年龄: 67岁, bbox=[676, 219, 801, 236]
2026-08-10 16:12:13,902 INFO     29 [qwen-vl-text] coord item[5]: text=申请科室: 老年医学呼吸内科, bbox=[80, 246, 327, 271]
2026-08-10 16:12:13,902 INFO     29 [qwen-vl-text] coord item[6]: text=机器型号: SE-MR4, bbox=[340, 247, 513, 264]
2026-08-10 16:12:13,902 INFO     29 [qwen-vl-text] coord item[7]: text=住院号, bbox=[676, 247, 736, 264]
2026-08-10 16:12:13,902 INFO     29 [qwen-vl-text] coord item[8]: text=检查部位: 颅脑颅脑MR平扫及增强+DWI,*钆特酸葡胺注射液【广西HR】, bbox=[78, 273, 590, 306]
2026-08-10 16:12:13,902 INFO     29 [qwen-vl-text] coord item[9]: text=检查日期: 2026-03-13, bbox=[606, 280, 863, 297]
2026-08-10 16:12:13,902 INFO     29 [qwen-vl-text] coord item[10]: text=(此报告仅供临床医师诊断参考,不作为疾病证明), bbox=[83, 310, 574, 328]
2026-08-10 16:12:13,902 INFO     29 [qwen-vl-text] coord item[11]: text=检查所见:, bbox=[78, 334, 176, 350]
2026-08-10 16:12:13,902 INFO     29 [qwen-vl-text] coord item[12]: text=左侧基底节区、两侧放射冠、右侧侧脑室前后角旁见小斑片状、斑点状等T1、稍, bbox=[82, 359, 927, 377]
2026-08-10 16:12:13,902 INFO     29 [qwen-vl-text] coord item[13]: text=长T2信号灶,FLAIR呈高信号,边界欠清,DWI未见弥散受限;余脑实质信号未见异, bbox=[82, 382, 904, 400]
2026-08-10 16:12:13,902 INFO     29 [qwen-vl-text] coord item[14]: text=常,DWI未见明确弥散受限区,增强扫描未见异常强化灶;静脉窦强化充盈良好,未, bbox=[82, 405, 915, 423]
2026-08-10 16:12:13,902 INFO     29 [qwen-vl-text] coord item[15]: text=见异常;各脑室及脑沟、裂、池对称性轻度增宽;中线结构无移位。, bbox=[82, 428, 753, 446]
2026-08-10 16:12:13,902 INFO     29 [qwen-vl-text] coord item[16]: text=诊断意见:, bbox=[74, 614, 171, 631]
2026-08-10 16:12:13,902 INFO     29 [qwen-vl-text] coord item[17]: text=脑白质病变--改良Fasekas1级;轻度脑萎缩。, bbox=[118, 642, 560, 660]
2026-08-10 16:12:13,902 INFO     29 [qwen-vl-text] coord item[18]: text=检查技师: 唐成, bbox=[73, 768, 213, 784]
2026-08-10 16:12:13,902 INFO     29 [qwen-vl-text] coord item[19]: text=报告医师: 郭仟, bbox=[259, 768, 402, 784]
2026-08-10 16:12:13,902 INFO     29 [qwen-vl-text] coord item[20]: text=审核医师: 张, bbox=[448, 768, 536, 784]
2026-08-10 16:12:13,903 INFO     29 [qwen-vl-text] coord item[21]: text=报告日期: 2026-03-16 15:13:19, bbox=[73, 792, 376, 809]
2026-08-10 16:12:13,903 INFO     29 [qwen-vl-text] coord item[22]: text=审核日期: 2026-03-16 18:28:39, bbox=[560, 792, 866, 809]
2026-08-10 16:12:13,903 INFO     29 [qwen-vl-text] coord item[23]: text=地址: 广西医科大学第一附属医院放射科, bbox=[77, 827, 379, 842]
2026-08-10 16:12:13,903 INFO     29 [qwen-vl-text] coord item[24]: text=联系电话: 0771-5356934, bbox=[404, 827, 590, 842]
2026-08-10 16:12:13,903 INFO     29 [qwen-vl-text] coord item[25]: text=“广西HR”解释: 广西影像检查项目互认, bbox=[622, 827, 920, 842]
2026-08-10 16:12:13,903 INFO     29 [qwen-vl-text] page=9 — 26/26 coords, api_time=12.8s
2026-08-10 16:12:13,903 INFO     29 [qwen-vl-text] new_positions (26):
[[9, 214.2, 382.585, 118.722, 144.82399999999998], [9, 46.41, 92.225, 186.082, 199.554], [9, 202.29999999999998, 230.85999999999999, 185.23999999999998, 198.712], [9, 314.755, 371.875, 184.398, 198.712], [9, 402.21999999999997, 476.59499999999997, 184.398, 198.712], [9, 47.599999999999994, 194.565, 207.132, 228.182], [9, 202.29999999999998, 305.235, 207.974, 222.28799999999998], [9, 402.21999999999997, 437.91999999999996, 207.974, 222.28799999999998], [9, 46.41, 351.05, 229.86599999999999, 257.652], [9, 360.57, 513.485, 235.76, 250.07399999999998], [9, 49.385, 341.53, 261.02, 276.176], [9, 46.41, 104.72, 281.228, 294.7], [9, 48.79, 551.5649999999999, 302.27799999999996, 317.43399999999997], [9, 48.79, 537.88, 321.644, 336.8], [9, 48.79, 544.425, 341.01, 356.166], [9, 48.79, 448.03499999999997, 360.376, 375.532], [9, 44.03, 101.74499999999999, 516.9879999999999, 531.302], [9, 70.21, 333.2, 540.564, 555.72], [9, 43.434999999999995, 126.735, 646.656, 660.1279999999999], [9, 154.105, 239.19, 646.656, 660.1279999999999], [9, 266.56, 318.91999999999996, 646.656, 660.1279999999999], [9, 43.434999999999995, 223.72, 666.864, 681.178], [9, 333.2, 515.27, 666.864, 681.178], [9, 45.815, 225.505, 696.334, 708.9639999999999], [9, 240.38, 351.05, 696.334, 708.9639999999999], [9, 370.09, 547.4, 696.334, 708.9639999999999]]
2026-08-10 16:12:13,903 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=16.0s
2026-08-10 16:12:13,904 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:12:13,905 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:12:13,906 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 16:12:13,906 INFO     29 [qwen-vl-text] positions(15): [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:12:13,906 INFO     29 [qwen-vl-text] page grouping: [10, 11], lines per page: [14, 1]
2026-08-10 16:12:14,252 INFO     29 [qwen-vl-text] page=10, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 16:12:14,625 INFO     29 [qwen-vl-text] page=11, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 16:12:14,627 INFO     29 [qwen-vl-text] LLM extraction start, text_len=262
2026-08-10 16:12:14,627 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:12:14,628 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 1959, \"bbox_end\": 1973, \"encounter_dates\": [\"2026-03-10\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "科\n检查部位：全身骨显像 显像剂：99mTc-MDP 临床诊断：1.肺占位性病变,2.细菌性肺炎,3.肺\n剂量：25mCi 部阴影\n（此报告仅供临床医师诊断参考，不作为疾病证明）\n检查所见：\n静脉注射99mTc-MDP 3小时后行全身骨显像前位、后位各1帧：\n全身骨像完整、显影基本清晰。颅骨、胸骨、椎体、肩胛骨、肋骨、骨盆及四肢骨显像剂分\n布未见明显异常改变。\n双肾显影，膀胱部分充盈。\n诊断意见：\n全身骨显像未见明显异常改变。\n报告医师：巫殷豪\n审核医师：彭盛梅\n报告日期：2026-03-10\n广西医科大学第一附属医院",
    "role": "user"
  }
]
2026-08-10 16:12:18,907 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:12:18,907 INFO     29 [qwen-vl-text] LLM output (len=435):
{
  "exam_date": "2026-03-10",
  "report_date": "2026-03-10",
  "exam_name": "全身骨显像",
  "exam_category": "imaging",
  "body_part": "全身",
  "patient_name": null,
  "patient_gender": null,
  "department": "广西医科大学第一附属医院",
  "bed_number": null,
  "findings": "静脉注射99mTc-MDP 3小时后行全身骨显像前位、后位各1帧：\n全身骨像完整、显影基本清晰。颅骨、胸骨、椎体、肩胛骨、肋骨、骨盆及四肢骨显像剂分布未见明显异常改变。\n双肾显影，膀胱部分充盈。",
  "conclusion": "全身骨显像未见明显异常改变。",
  "physician": "巫殷豪",
  "reviewer": "彭盛梅"
}
2026-08-10 16:12:18,919 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5328166, prompt_len=904
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共14行）
["科", "检查部位：全身骨显像 显像剂：99mTc-MDP 临床诊断：1.肺占位性病变,2.细菌性肺炎,3.肺", "剂量：25mCi 部阴影", "（此报告仅供临床医师诊断参考，不作为疾病证明）", "检查所见：", "静脉注射99mTc-MDP 3小时后行全身骨显像前位、后位各1帧：", "全身骨像完整、显影基本清晰。颅骨、胸骨、椎体、肩胛骨、肋骨、骨盆及四肢骨显像剂分", "布未见明显异常改变。", "双肾显影，膀胱部分充盈。", "诊断意见：", "全身骨显像未见明显异常改变。", "报告医师：巫殷豪", "审核医师：彭盛梅", "报告日期：2026-03-10"]

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
2026-08-10 16:12:24,380 INFO     29 [qwen-vl-text] coord API raw response (len=854):
[
	{"text": "科", "bbox": [50, 93, 70, 107]},
	{"text": "检查部位：全身骨显像 显像剂：99mTc-MDP 临床诊断：1.肺占位性病变,2.细菌性肺炎,3.肺", "bbox": [50, 110, 925, 127]},
	{"text": "剂量：25mCi 部阴影", "bbox": [50, 130, 567, 147]},
	{"text": "（此报告仅供临床医师诊断参考，不作为疾病证明）", "bbox": [60, 489, 522, 505]},
	{"text": "检查所见：", "bbox": [50, 508, 141, 523]},
	{"text": "静脉注射99mTc-MDP 3小时后行全身骨显像前位、后位各1帧：", "bbox": [93, 527, 668, 543]},
	{"text": "全身骨像完整、显影基本清晰。颅骨、胸骨、椎体、肩胛骨、肋骨、骨盆及四肢骨显像剂分", "bbox": [93, 547, 923, 564]},
	{"text": "布未见明显异常改变。", "bbox": [50, 567, 248, 582]},
	{"text": "双肾显影，膀胱部分充盈。", "bbox": [93, 586, 334, 602]},
	{"text": "诊断意见：", "bbox": [50, 683, 141, 699]},
	{"text": "全身骨显像未见明显异常改变。", "bbox": [95, 703, 375, 719]},
	{"text": "报告医师：巫殷豪", "bbox": [58, 854, 239, 870]},
	{"text": "审核医师：彭盛梅", "bbox": [355, 854, 549, 877]},
	{"text": "报告日期：2026-03-10", "bbox": [650, 857, 862, 872]}
]
2026-08-10 16:12:24,381 INFO     29 [qwen-vl-text] coord API: raw_items=14, valid_items=14, elapsed=5.5s
2026-08-10 16:12:24,381 INFO     29 [qwen-vl-text] coord item[0]: text=科, bbox=[50, 93, 70, 107]
2026-08-10 16:12:24,381 INFO     29 [qwen-vl-text] coord item[1]: text=检查部位：全身骨显像 显像剂：99mTc-MDP 临床诊断：1.肺占位性病变,2.细菌性肺炎,3.肺, bbox=[50, 110, 925, 127]
2026-08-10 16:12:24,381 INFO     29 [qwen-vl-text] coord item[2]: text=剂量：25mCi 部阴影, bbox=[50, 130, 567, 147]
2026-08-10 16:12:24,381 INFO     29 [qwen-vl-text] coord item[3]: text=（此报告仅供临床医师诊断参考，不作为疾病证明）, bbox=[60, 489, 522, 505]
2026-08-10 16:12:24,381 INFO     29 [qwen-vl-text] coord item[4]: text=检查所见：, bbox=[50, 508, 141, 523]
2026-08-10 16:12:24,381 INFO     29 [qwen-vl-text] coord item[5]: text=静脉注射99mTc-MDP 3小时后行全身骨显像前位、后位各1帧：, bbox=[93, 527, 668, 543]
2026-08-10 16:12:24,381 INFO     29 [qwen-vl-text] coord item[6]: text=全身骨像完整、显影基本清晰。颅骨、胸骨、椎体、肩胛骨、肋骨、骨盆及四肢骨显像剂分, bbox=[93, 547, 923, 564]
2026-08-10 16:12:24,381 INFO     29 [qwen-vl-text] coord item[7]: text=布未见明显异常改变。, bbox=[50, 567, 248, 582]
2026-08-10 16:12:24,381 INFO     29 [qwen-vl-text] coord item[8]: text=双肾显影，膀胱部分充盈。, bbox=[93, 586, 334, 602]
2026-08-10 16:12:24,381 INFO     29 [qwen-vl-text] coord item[9]: text=诊断意见：, bbox=[50, 683, 141, 699]
2026-08-10 16:12:24,381 INFO     29 [qwen-vl-text] coord item[10]: text=全身骨显像未见明显异常改变。, bbox=[95, 703, 375, 719]
2026-08-10 16:12:24,381 INFO     29 [qwen-vl-text] coord item[11]: text=报告医师：巫殷豪, bbox=[58, 854, 239, 870]
2026-08-10 16:12:24,381 INFO     29 [qwen-vl-text] coord item[12]: text=审核医师：彭盛梅, bbox=[355, 854, 549, 877]
2026-08-10 16:12:24,381 INFO     29 [qwen-vl-text] coord item[13]: text=报告日期：2026-03-10, bbox=[650, 857, 862, 872]
2026-08-10 16:12:24,381 INFO     29 [qwen-vl-text] page=10 — 14/14 coords, api_time=5.5s
2026-08-10 16:12:24,395 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6618177, prompt_len=627
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["广西医科大学第一附属医院"]

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
2026-08-10 16:12:26,169 INFO     29 [qwen-vl-text] coord API raw response (len=70):
```json
[
	{"text": "广西医科大学第一附属医院", "bbox": [342, 72, 834, 104]}
]
```
2026-08-10 16:12:26,169 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=1.8s
2026-08-10 16:12:26,169 INFO     29 [qwen-vl-text] coord item[0]: text=广西医科大学第一附属医院, bbox=[342, 72, 834, 104]
2026-08-10 16:12:26,170 INFO     29 [qwen-vl-text] page=11 — 1/1 coords, api_time=1.8s
2026-08-10 16:12:26,170 INFO     29 [qwen-vl-text] new_positions (15):
[[10, 29.75, 41.65, 78.306, 90.094], [10, 29.75, 550.375, 92.61999999999999, 106.934], [10, 29.75, 337.365, 109.46, 123.774], [10, 35.699999999999996, 310.59, 411.738, 425.21], [10, 29.75, 83.895, 427.736, 440.366], [10, 55.335, 397.46, 443.734, 457.20599999999996], [10, 55.335, 549.185, 460.574, 474.888], [10, 29.75, 147.56, 477.414, 490.044], [10, 55.335, 198.73, 493.412, 506.88399999999996], [10, 29.75, 83.895, 575.086, 588.558], [10, 56.525, 223.125, 591.9259999999999, 605.398], [10, 34.51, 142.20499999999998, 719.068, 732.54], [10, 211.225, 326.655, 719.068, 738.434], [10, 386.75, 512.89, 721.5939999999999, 734.2239999999999], [11, 203.48999999999998, 496.22999999999996, 60.623999999999995, 87.568]]
2026-08-10 16:12:26,170 INFO     29 [qwen-vl-text] ═══ DONE ═══ 15 positions, pages=2, time=12.3s
2026-08-10 16:12:26,171 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:12:26,171 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:12:26,172 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 16:12:26,172 INFO     29 [qwen-vl-text] positions(35): [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:12:26,172 INFO     29 [qwen-vl-text] page grouping: [11], lines per page: [35]
2026-08-10 16:12:26,530 INFO     29 [qwen-vl-text] page=11, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 16:12:26,531 INFO     29 [qwen-vl-text] LLM extraction start, text_len=642
2026-08-10 16:12:26,532 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:12:26,532 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 1974, \"bbox_end\": 2008, \"encounter_dates\": [\"2026-03-11\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "影像检查报告单\n病人ID:\n姓名:\n性别: 男\n年龄: 67岁\n申请科室:\n机器型号: SE-\n床号: 49床\n住院号: 1959\nForce-2\n检查部位: 下腹部,上腹部CT平扫+增强,(新)碘帕醇注射液\n【广西HR】\n检查日期: 2026-03-11\n(此报告仅供临床医师诊断参考,不作为疾病证明)\n检查所见:\n双侧肾上腺见多个结节状稍低/低密度影,较大者大小约1.6cm×1.2cm,增强扫\n描不均匀强化。肝脏各叶比例正常,肝实质内见多发类圆形低密度无强化灶,较大者\n位于S8,大小约1.2cm×1.1cm;余肝实质未见异常密度影及异常强化灶。肝内、外胆\n管未见扩张,胆囊不大,囊壁均匀,囊内密度未见异常。脾脏、胰腺形态、大小、密\n度未见异常,增强扫描未见异常强化,右肾体积缩小,双肾实质内见多个类圆形低密\n度无强化灶,较大者大小约0.9cm×1.5cm;双侧肾盂肾盏及输尿管未见扩张。腹部肠\n管分布正常,管腔未见扩张、积液,腹腔内未见明确肿块影;肝门及腹主动脉旁未见\n增大淋巴结,腹膜腔未见积液。\n诊断意见:\n1.双侧肾上腺占位,考虑转移瘤可能性大,请结合临床;\n2.肝多发囊肿;\n3.右肾萎缩,双肾囊肿。\n检查技师:刘辰民\n报告医师:谢金桓\n审核医师: 冯涛\n报告日期:2026-03-11 14:21:30\n审核日期:2026-03-11 16:15:45\n地址:广西医科大学第一附属医院放射科\n联系电话:0771-5356934\n“广西HR”解释:广西影像检查项目互认",
    "role": "user"
  }
]
2026-08-10 16:12:29,737 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:12:29.736+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:12:30,340 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:12:30,340 INFO     29 [qwen-vl-text] LLM output (len=662):
{
  "exam_date": "2026-03-11",
  "report_date": "2026-03-11",
  "exam_name": "下腹部,上腹部CT平扫+增强",
  "exam_category": "imaging",
  "body_part": "下腹部,上腹部",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": "49床",
  "findings": "双侧肾上腺见多个结节状稍低/低密度影,较大者大小约1.6cm×1.2cm,增强扫描不均匀强化。肝脏各叶比例正常,肝实质内见多发类圆形低密度无强化灶,较大者位于S8,大小约1.2cm×1.1cm;余肝实质未见异常密度影及异常强化灶。肝内、外胆管未见扩张,胆囊不大,囊壁均匀,囊内密度未见异常。脾脏、胰腺形态、大小、密度未见异常,增强扫描未见异常强化,右肾体积缩小,双肾实质内见多个类圆形低密度无强化灶,较大者大小约0.9cm×1.5cm;双侧肾盂肾盏及输尿管未见扩张。腹部肠管分布正常,管腔未见扩张、积液,腹腔内未见明确肿块影;肝门及腹主动脉旁未见增大淋巴结,腹膜腔未见积液。",
  "conclusion": "1.双侧肾上腺占位,考虑转移瘤可能性大,请结合临床;\n2.肝多发囊肿;\n3.右肾萎缩,双肾囊肿。",
  "physician": "谢金桓",
  "reviewer": "冯涛"
}
2026-08-10 16:12:30,357 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6618177, prompt_len=1360
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["影像检查报告单", "病人ID:", "姓名:", "性别: 男", "年龄: 67岁", "申请科室:", "机器型号: SE-", "床号: 49床", "住院号: 1959", "Force-2", "检查部位: 下腹部,上腹部CT平扫+增强,(新)碘帕醇注射液", "【广西HR】", "检查日期: 2026-03-11", "(此报告仅供临床医师诊断参考,不作为疾病证明)", "检查所见:", "双侧肾上腺见多个结节状稍低/低密度影,较大者大小约1.6cm×1.2cm,增强扫", "描不均匀强化。肝脏各叶比例正常,肝实质内见多发类圆形低密度无强化灶,较大者", "位于S8,大小约1.2cm×1.1cm;余肝实质未见异常密度影及异常强化灶。肝内、外胆", "管未见扩张,胆囊不大,囊壁均匀,囊内密度未见异常。脾脏、胰腺形态、大小、密", "度未见异常,增强扫描未见异常强化,右肾体积缩小,双肾实质内见多个类圆形低密", "度无强化灶,较大者大小约0.9cm×1.5cm;双侧肾盂肾盏及输尿管未见扩张。腹部肠", "管分布正常,管腔未见扩张、积液,腹腔内未见明确肿块影;肝门及腹主动脉旁未见", "增大淋巴结,腹膜腔未见积液。", "诊断意见:", "1.双侧肾上腺占位,考虑转移瘤可能性大,请结合临床;", "2.肝多发囊肿;", "3.右肾萎缩,双肾囊肿。", "检查技师:刘辰民", "报告医师:谢金桓", "审核医师: 冯涛", "报告日期:2026-03-11 14:21:30", "审核日期:2026-03-11 16:15:45", "地址:广西医科大学第一附属医院放射科", "联系电话:0771-5356934", "“广西HR”解释:广西影像检查项目互认"]

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
2026-08-10 16:12:41,500 INFO     29 [qwen-vl-text] coord API raw response (len=2224):
[
	{"text": "广西医科大学第一附属医院", "bbox": [342, 72, 834, 104]},
	{"text": "影像检查报告单", "bbox": [444, 110, 731, 140]},
	{"text": "病人 ID:", "bbox": [78, 184, 156, 199]},
	{"text": "姓名:", "bbox": [345, 184, 394, 199]},
	{"text": "性别: 男", "bbox": [538, 184, 634, 199]},
	{"text": "年龄: 67岁", "bbox": [687, 184, 812, 199]},
	{"text": "申请科室:", "bbox": [78, 213, 165, 228]},
	{"text": "机器型号: SE-", "bbox": [345, 213, 488, 228]},
	{"text": "床号: 49床", "bbox": [538, 213, 658, 228]},
	{"text": "住院号 1959", "bbox": [687, 213, 812, 228]},
	{"text": "Force-2", "bbox": [457, 225, 531, 238]},
	{"text": "检查部位: 下腹部,上腹部CT平扫+增强,(新)碘帕醇注射液", "bbox": [78, 241, 609, 256]},
	{"text": "【广西HR】", "bbox": [195, 256, 281, 271]},
	{"text": "检查日期: 2026-03-11", "bbox": [616, 247, 874, 263]},
	{"text": "(此报告仅供临床医师诊断参考,不作为疾病证明)", "bbox": [81, 277, 584, 294]},
	{"text": "检查所见:", "bbox": [78, 301, 177, 318]},
	{"text": "双侧肾上腺见多个结节状稍低/低密度影,较大者大小约1.6cm×1.2cm,增强扫", "bbox": [81, 328, 929, 345]},
	{"text": "描不均匀强化。肝脏各叶比例正常,肝实质内见多发类圆形低密度无强化灶,较大者", "bbox": [81, 352, 940, 369]},
	{"text": "位于S8,大小约1.2cm×1.1cm;余肝实质未见异常密度影及异常强化灶。肝内、外胆", "bbox": [81, 375, 940, 393]},
	{"text": "管未见扩张,胆囊不大,囊壁均匀,囊内密度未见异常。脾脏、胰腺形态、大小、密", "bbox": [81, 399, 940, 417]},
	{"text": "度未见异常,增强扫描未见异常强化,右肾体积缩小,双肾实质内见多个类圆形低密", "bbox": [81, 423, 940, 441]},
	{"text": "度无强化灶,较大者大小约0.9cm×1.5cm;双侧肾盂肾盏及输尿管未见扩张。腹部肠", "bbox": [81, 447, 940, 465]},
	{"text": "管分布正常,管腔未见扩张、积液,腹腔内未见明确肿块影;肝门及腹主动脉旁未见", "bbox": [81, 471, 940, 489]},
	{"text": "增大淋巴结,腹膜腔未见积液。", "bbox": [81, 495, 392, 513]},
	{"text": "诊断意见:", "bbox": [78, 590, 177, 607]},
	{"text": "1.双侧肾上腺占位,考虑转移瘤可能性大,请结合临床;", "bbox": [123, 617, 683, 634]},
	{"text": "2.肝多发囊肿;", "bbox": [123, 641, 268, 658]},
	{"text": "3.右肾萎缩,双肾囊肿。", "bbox": [123, 665, 363, 682]},
	{"text": "检查技师:刘辰民", "bbox": [78, 746, 239, 761]},
	{"text": "报告医师:谢金桓", "bbox": [265, 746, 428, 761]},
	{"text": "审核医师: 冯涛", "bbox": [455, 746, 641, 764]},
	{"text": "报告日期:2026-03-11 14:21:30", "bbox": [78, 770, 383, 786]},
	{"text": "审核日期:2026-03-11 16:15:45", "bbox": [568, 770, 870, 786]},
	{"text": "地址:广西医科大学第一附属医院放射科", "bbox": [83, 805, 388, 819]},
	{"text": "联系电话:0771-5356934", "bbox": [412, 805, 598, 819]},
	{"text": "“广西HR”解释:广西影像检查项目互认", "bbox": [629, 805, 923, 819]}
]
2026-08-10 16:12:41,501 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=11.1s
2026-08-10 16:12:41,501 INFO     29 [qwen-vl-text] coord item[0]: text=广西医科大学第一附属医院, bbox=[342, 72, 834, 104]
2026-08-10 16:12:41,501 INFO     29 [qwen-vl-text] coord item[1]: text=影像检查报告单, bbox=[444, 110, 731, 140]
2026-08-10 16:12:41,501 INFO     29 [qwen-vl-text] coord item[2]: text=病人 ID:, bbox=[78, 184, 156, 199]
2026-08-10 16:12:41,501 INFO     29 [qwen-vl-text] coord item[3]: text=姓名:, bbox=[345, 184, 394, 199]
2026-08-10 16:12:41,501 INFO     29 [qwen-vl-text] coord item[4]: text=性别: 男, bbox=[538, 184, 634, 199]
2026-08-10 16:12:41,501 INFO     29 [qwen-vl-text] coord item[5]: text=年龄: 67岁, bbox=[687, 184, 812, 199]
2026-08-10 16:12:41,501 INFO     29 [qwen-vl-text] coord item[6]: text=申请科室:, bbox=[78, 213, 165, 228]
2026-08-10 16:12:41,501 INFO     29 [qwen-vl-text] coord item[7]: text=机器型号: SE-, bbox=[345, 213, 488, 228]
2026-08-10 16:12:41,501 INFO     29 [qwen-vl-text] coord item[8]: text=床号: 49床, bbox=[538, 213, 658, 228]
2026-08-10 16:12:41,501 INFO     29 [qwen-vl-text] coord item[9]: text=住院号 1959, bbox=[687, 213, 812, 228]
2026-08-10 16:12:41,501 INFO     29 [qwen-vl-text] coord item[10]: text=Force-2, bbox=[457, 225, 531, 238]
2026-08-10 16:12:41,502 INFO     29 [qwen-vl-text] coord item[11]: text=检查部位: 下腹部,上腹部CT平扫+增强,(新)碘帕醇注射液, bbox=[78, 241, 609, 256]
2026-08-10 16:12:41,502 INFO     29 [qwen-vl-text] coord item[12]: text=【广西HR】, bbox=[195, 256, 281, 271]
2026-08-10 16:12:41,502 INFO     29 [qwen-vl-text] coord item[13]: text=检查日期: 2026-03-11, bbox=[616, 247, 874, 263]
2026-08-10 16:12:41,502 INFO     29 [qwen-vl-text] coord item[14]: text=(此报告仅供临床医师诊断参考,不作为疾病证明), bbox=[81, 277, 584, 294]
2026-08-10 16:12:41,502 INFO     29 [qwen-vl-text] coord item[15]: text=检查所见:, bbox=[78, 301, 177, 318]
2026-08-10 16:12:41,502 INFO     29 [qwen-vl-text] coord item[16]: text=双侧肾上腺见多个结节状稍低/低密度影,较大者大小约1.6cm×1.2cm,增强扫, bbox=[81, 328, 929, 345]
2026-08-10 16:12:41,502 INFO     29 [qwen-vl-text] coord item[17]: text=描不均匀强化。肝脏各叶比例正常,肝实质内见多发类圆形低密度无强化灶,较大者, bbox=[81, 352, 940, 369]
2026-08-10 16:12:41,502 INFO     29 [qwen-vl-text] coord item[18]: text=位于S8,大小约1.2cm×1.1cm;余肝实质未见异常密度影及异常强化灶。肝内、外胆, bbox=[81, 375, 940, 393]
2026-08-10 16:12:41,502 INFO     29 [qwen-vl-text] coord item[19]: text=管未见扩张,胆囊不大,囊壁均匀,囊内密度未见异常。脾脏、胰腺形态、大小、密, bbox=[81, 399, 940, 417]
2026-08-10 16:12:41,502 INFO     29 [qwen-vl-text] coord item[20]: text=度未见异常,增强扫描未见异常强化,右肾体积缩小,双肾实质内见多个类圆形低密, bbox=[81, 423, 940, 441]
2026-08-10 16:12:41,502 INFO     29 [qwen-vl-text] coord item[21]: text=度无强化灶,较大者大小约0.9cm×1.5cm;双侧肾盂肾盏及输尿管未见扩张。腹部肠, bbox=[81, 447, 940, 465]
2026-08-10 16:12:41,503 INFO     29 [qwen-vl-text] coord item[22]: text=管分布正常,管腔未见扩张、积液,腹腔内未见明确肿块影;肝门及腹主动脉旁未见, bbox=[81, 471, 940, 489]
2026-08-10 16:12:41,503 INFO     29 [qwen-vl-text] coord item[23]: text=增大淋巴结,腹膜腔未见积液。, bbox=[81, 495, 392, 513]
2026-08-10 16:12:41,503 INFO     29 [qwen-vl-text] coord item[24]: text=诊断意见:, bbox=[78, 590, 177, 607]
2026-08-10 16:12:41,503 INFO     29 [qwen-vl-text] coord item[25]: text=1.双侧肾上腺占位,考虑转移瘤可能性大,请结合临床;, bbox=[123, 617, 683, 634]
2026-08-10 16:12:41,503 INFO     29 [qwen-vl-text] coord item[26]: text=2.肝多发囊肿;, bbox=[123, 641, 268, 658]
2026-08-10 16:12:41,503 INFO     29 [qwen-vl-text] coord item[27]: text=3.右肾萎缩,双肾囊肿。, bbox=[123, 665, 363, 682]
2026-08-10 16:12:41,503 INFO     29 [qwen-vl-text] coord item[28]: text=检查技师:刘辰民, bbox=[78, 746, 239, 761]
2026-08-10 16:12:41,503 INFO     29 [qwen-vl-text] coord item[29]: text=报告医师:谢金桓, bbox=[265, 746, 428, 761]
2026-08-10 16:12:41,503 INFO     29 [qwen-vl-text] coord item[30]: text=审核医师: 冯涛, bbox=[455, 746, 641, 764]
2026-08-10 16:12:41,503 INFO     29 [qwen-vl-text] coord item[31]: text=报告日期:2026-03-11 14:21:30, bbox=[78, 770, 383, 786]
2026-08-10 16:12:41,503 INFO     29 [qwen-vl-text] coord item[32]: text=审核日期:2026-03-11 16:15:45, bbox=[568, 770, 870, 786]
2026-08-10 16:12:41,503 INFO     29 [qwen-vl-text] coord item[33]: text=地址:广西医科大学第一附属医院放射科, bbox=[83, 805, 388, 819]
2026-08-10 16:12:41,503 INFO     29 [qwen-vl-text] coord item[34]: text=联系电话:0771-5356934, bbox=[412, 805, 598, 819]
2026-08-10 16:12:41,503 INFO     29 [qwen-vl-text] coord item[35]: text=“广西HR”解释:广西影像检查项目互认, bbox=[629, 805, 923, 819]
2026-08-10 16:12:41,506 INFO     29 [qwen-vl-text] page=11 — 35/35 coords, api_time=11.1s
2026-08-10 16:12:41,506 INFO     29 [qwen-vl-text] new_positions (35):
[[11, 203.48999999999998, 496.22999999999996, 60.623999999999995, 87.568], [11, 264.18, 434.945, 92.61999999999999, 117.88], [11, 46.41, 92.82, 154.928, 167.558], [11, 205.27499999999998, 234.42999999999998, 154.928, 167.558], [11, 320.11, 377.22999999999996, 154.928, 167.558], [11, 408.765, 483.14, 154.928, 167.558], [11, 46.41, 98.175, 179.346, 191.976], [11, 205.27499999999998, 290.36, 179.346, 191.976], [11, 320.11, 391.51, 179.346, 191.976], [11, 408.765, 483.14, 179.346, 191.976], [11, 271.91499999999996, 315.945, 189.45, 200.396], [11, 46.41, 362.35499999999996, 202.922, 215.552], [11, 116.02499999999999, 167.195, 215.552, 228.182], [11, 366.52, 520.03, 207.974, 221.446], [11, 48.195, 347.47999999999996, 233.23399999999998, 247.548], [11, 46.41, 105.315, 253.44199999999998, 267.756], [11, 48.195, 552.755, 276.176, 290.49], [11, 48.195, 559.3, 296.384, 310.698], [11, 48.195, 559.3, 315.75, 330.906], [11, 48.195, 559.3, 335.95799999999997, 351.114], [11, 48.195, 559.3, 356.166, 371.322], [11, 48.195, 559.3, 376.37399999999997, 391.53], [11, 48.195, 559.3, 396.582, 411.738], [11, 48.195, 233.23999999999998, 416.78999999999996, 431.94599999999997], [11, 46.41, 105.315, 496.78, 511.094], [11, 73.185, 406.385, 519.514, 533.828], [11, 73.185, 159.45999999999998, 539.722, 554.036], [11, 73.185, 215.98499999999999, 559.93, 574.244], [11, 46.41, 142.20499999999998, 628.132, 640.762], [11, 157.67499999999998, 254.66, 628.132, 640.762], [11, 270.72499999999997, 381.395, 628.132, 643.288], [11, 46.41, 227.885, 648.34, 661.812], [11, 337.96, 517.65, 648.34, 661.812], [11, 49.385, 230.85999999999999, 677.81, 689.598], [11, 245.14, 355.81, 677.81, 689.598]]
2026-08-10 16:12:41,507 INFO     29 [qwen-vl-text] ═══ DONE ═══ 35 positions, pages=1, time=15.3s
2026-08-10 16:12:41,507 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:12:41,509 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:12:41,509 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 16:12:41,509 INFO     29 [qwen-vl-text] positions(34): [[12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:12:41,509 INFO     29 [qwen-vl-text] page grouping: [12], lines per page: [34]
2026-08-10 16:12:41,893 INFO     29 [qwen-vl-text] page=12, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 16:12:41,895 INFO     29 [qwen-vl-text] LLM extraction start, text_len=769
2026-08-10 16:12:41,895 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:12:41,895 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 2009, \"bbox_end\": 2042, \"encounter_dates\": [\"2026-03-02\"], \"department\": \"老年医学呼吸内科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "广西医科大学第一附属医院\n影像检查报告单\n病人ID:\n姓名:\n男\n年龄: 67岁\n申请科室: 老年医学呼吸内科\n机器型号: SE-\nForce-2\n床号\n号\n检查部位: 胸部CT平扫+增强,*碘海醇注射液【广西HR】\n检查日期: 2026-03-02\n(此报告仅供临床医师诊断参考,不作为疾病证明)\n检查所见:\n两肺尖胸膜下见类圆形透亮影,较大者长径约0.8cm;右肺下叶基底段(Se4:IM144)见团\n块状密度增高灶,大小约为7.7cm×5.1cm×6.9cm,增强扫描中度强化;两肺可见多发实性结节\n影,较大位于右肺下叶外基底段(Se4:IM344),内可见空泡,长径约为1.1cm,增强扫描似见\n血管穿行。右肺中叶、左肺上叶下舌段及两肺下叶见条索状密度增高影;余肺叶内未见异常密\n度影及异常强化灶,右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张,两肺部分支气管\n管壁增厚,管腔变窄,气管、其余支气管通畅;肺门、纵隔结构清楚,纵隔、两侧肺门见多发\n淋巴结,大者短径约1.1cm。两侧胸膜增厚、钙化,胸膜腔未见积液。主动脉、冠状动脉见斑片\n状钙化灶。\n诊断意见:\n1.右肺下叶后基底段软组织肿块,肿瘤性病变?感染性病变?请结合临床及实验室检查;\n2.两肺多发实性结节,建议短期复查;\n3.右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张并两肺炎症;\n4.两肺上叶间隔旁型肺气肿;\n5.纵隔、两侧肺门淋巴结,建议复查;\n6.两侧胸膜肥厚、钙化;\n7.主动脉、冠状动脉硬化。\n检查技师:周春燚 报告医师:肖芳艳 审核医师:\n报告日期:2026-03-03 18:39:05 审核日期:2026-03-04 09:21:01\n地址:广西医科大学第一附属医院放射科 联系电话:0771-5356934 “广西HR”解码:广西影像检查项目互认",
    "role": "user"
  }
]
2026-08-10 16:12:46,341 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:12:46,341 INFO     29 [qwen-vl-text] LLM output (len=794):
{
  "exam_date": "2026-03-02",
  "report_date": "2026-03-03",
  "exam_name": "胸部CT平扫+增强",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": "男",
  "department": "老年医学呼吸内科",
  "bed_number": null,
  "findings": "两肺尖胸膜下见类圆形透亮影,较大者长径约0.8cm;右肺下叶基底段(Se4:IM144)见团块状密度增高灶,大小约为7.7cm×5.1cm×6.9cm,增强扫描中度强化;两肺可见多发实性结节影,较大位于右肺下叶外基底段(Se4:IM344),内可见空泡,长径约为1.1cm,增强扫描似见血管穿行。右肺中叶、左肺上叶下舌段及两肺下叶见条索状密度增高影;余肺叶内未见异常密度影及异常强化灶,右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张,两肺部分支气管管壁增厚,管腔变窄,气管、其余支气管通畅;肺门、纵隔结构清楚,纵隔、两侧肺门见多发淋巴结,大者短径约1.1cm。两侧胸膜增厚、钙化,胸膜腔未见积液。主动脉、冠状动脉见斑片状钙化灶。",
  "conclusion": "1.右肺下叶后基底段软组织肿块,肿瘤性病变?感染性病变?请结合临床及实验室检查;\n2.两肺多发实性结节,建议短期复查;\n3.右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张并两肺炎症;\n4.两肺上叶间隔旁型肺气肿;\n5.纵隔、两侧肺门淋巴结,建议复查;\n6.两侧胸膜肥厚、钙化;\n7.主动脉、冠状动脉硬化。",
  "physician": "肖芳艳",
  "reviewer": null
}
2026-08-10 16:12:46,359 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5214598, prompt_len=1484
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共34行）
["广西医科大学第一附属医院", "影像检查报告单", "病人ID:", "姓名:", "男", "年龄: 67岁", "申请科室: 老年医学呼吸内科", "机器型号: SE-", "Force-2", "床号", "号", "检查部位: 胸部CT平扫+增强,*碘海醇注射液【广西HR】", "检查日期: 2026-03-02", "(此报告仅供临床医师诊断参考,不作为疾病证明)", "检查所见:", "两肺尖胸膜下见类圆形透亮影,较大者长径约0.8cm;右肺下叶基底段(Se4:IM144)见团", "块状密度增高灶,大小约为7.7cm×5.1cm×6.9cm,增强扫描中度强化;两肺可见多发实性结节", "影,较大位于右肺下叶外基底段(Se4:IM344),内可见空泡,长径约为1.1cm,增强扫描似见", "血管穿行。右肺中叶、左肺上叶下舌段及两肺下叶见条索状密度增高影;余肺叶内未见异常密", "度影及异常强化灶,右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张,两肺部分支气管", "管壁增厚,管腔变窄,气管、其余支气管通畅;肺门、纵隔结构清楚,纵隔、两侧肺门见多发", "淋巴结,大者短径约1.1cm。两侧胸膜增厚、钙化,胸膜腔未见积液。主动脉、冠状动脉见斑片", "状钙化灶。", "诊断意见:", "1.右肺下叶后基底段软组织肿块,肿瘤性病变?感染性病变?请结合临床及实验室检查;", "2.两肺多发实性结节,建议短期复查;", "3.右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张并两肺炎症;", "4.两肺上叶间隔旁型肺气肿;", "5.纵隔、两侧肺门淋巴结,建议复查;", "6.两侧胸膜肥厚、钙化;", "7.主动脉、冠状动脉硬化。", "检查技师:周春燚 报告医师:肖芳艳 审核医师:", "报告日期:2026-03-03 18:39:05 审核日期:2026-03-04 09:21:01", "地址:广西医科大学第一附属医院放射科 联系电话:0771-5356934 “广西HR”解码:广西影像检查项目互认"]

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
2026-08-10 16:13:00,513 INFO     29 [qwen-vl-text] coord API raw response (len=2251):
[
	{"text": "广西医科大学第一附属医院", "bbox": [336, 111, 820, 141]},
	{"text": "影像检查报告单", "bbox": [436, 148, 719, 178]},
	{"text": "病人ID:", "bbox": [74, 222, 150, 238]},
	{"text": "姓名:", "bbox": [338, 222, 388, 238]},
	{"text": "男", "bbox": [607, 222, 625, 237]},
	{"text": "年龄: 67岁", "bbox": [676, 222, 800, 238]},
	{"text": "申请科室: 老年医学呼吸内科", "bbox": [75, 249, 325, 265]},
	{"text": "机器型号: SE-", "bbox": [338, 250, 478, 266]},
	{"text": "Force-2", "bbox": [450, 262, 522, 277]},
	{"text": "床号", "bbox": [528, 250, 568, 266]},
	{"text": "号", "bbox": [695, 250, 734, 266]},
	{"text": "检查部位: 胸部CT平扫+增强,*碘海醇注射液【广西HR】", "bbox": [74, 281, 570, 298]},
	{"text": "检查日期: 2026-03-02", "bbox": [606, 281, 862, 298]},
	{"text": "(此报告仅供临床医师诊断参考,不作为疾病证明)", "bbox": [77, 305, 574, 324]},
	{"text": "检查所见:", "bbox": [74, 331, 173, 348]},
	{"text": "两肺尖胸膜下见类圆形透亮影,较大者长径约0.8cm;右肺下叶基底段(Se4:IM144)见团", "bbox": [79, 356, 919, 372]},
	{"text": "块状密度增高灶,大小约为7.7cm×5.1cm×6.9cm,增强扫描中度强化;两肺可见多发实性结节", "bbox": [79, 373, 919, 389]},
	{"text": "影,较大位于右肺下叶外基底段(Se4:IM344),内可见空泡,长径约为1.1cm,增强扫描似见", "bbox": [79, 390, 919, 406]},
	{"text": "血管穿行。右肺中叶、左肺上叶下舌段及两肺下叶见条索状密度增高影;余肺叶内未见异常密", "bbox": [79, 407, 909, 423]},
	{"text": "度影及异常强化灶,右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张,两肺部分支气管", "bbox": [79, 424, 909, 440]},
	{"text": "管壁增厚,管腔变窄,气管、其余支气管通畅;肺门、纵隔结构清楚,纵隔、两侧肺门见多发", "bbox": [79, 441, 910, 457]},
	{"text": "淋巴结,大者短径约1.1cm。两侧胸膜增厚、钙化,胸膜腔未见积液。主动脉、冠状动脉见斑片", "bbox": [79, 458, 919, 474]},
	{"text": "状钙化灶。", "bbox": [79, 475, 166, 491]},
	{"text": "诊断意见:", "bbox": [74, 625, 173, 643]},
	{"text": "1.右肺下叶后基底段软组织肿块,肿瘤性病变?感染性病变?请结合临床及实验室检查;", "bbox": [119, 650, 899, 666]},
	{"text": "2.两肺多发实性结节,建议短期复查;", "bbox": [119, 668, 452, 684]},
	{"text": "3.右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张并两肺炎症;", "bbox": [119, 685, 735, 701]},
	{"text": "4.两肺上叶间隔旁型肺气肿;", "bbox": [119, 702, 371, 718]},
	{"text": "5.纵隔、两侧肺门淋巴结,建议复查;", "bbox": [119, 719, 452, 735]},
	{"text": "6.两侧胸膜肥厚、钙化;", "bbox": [119, 736, 331, 752]},
	{"text": "7.主动脉、冠状动脉硬化。", "bbox": [119, 753, 352, 769]},
	{"text": "检查技师:周春燚 报告医师:肖芳艳 审核医师:", "bbox": [74, 785, 540, 802]},
	{"text": "报告日期:2026-03-03 18:39:05 审核日期:2026-03-04 09:21:01", "bbox": [74, 811, 866, 828]},
	{"text": "地址:广西医科大学第一附属医院放射科 联系电话:0771-5356934 “广西HR”解码:广西影像检查项目互认", "bbox": [79, 845, 921, 861]}
]
2026-08-10 16:13:00,513 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=14.2s
2026-08-10 16:13:00,513 INFO     29 [qwen-vl-text] coord item[0]: text=广西医科大学第一附属医院, bbox=[336, 111, 820, 141]
2026-08-10 16:13:00,513 INFO     29 [qwen-vl-text] coord item[1]: text=影像检查报告单, bbox=[436, 148, 719, 178]
2026-08-10 16:13:00,514 INFO     29 [qwen-vl-text] coord item[2]: text=病人ID:, bbox=[74, 222, 150, 238]
2026-08-10 16:13:00,514 INFO     29 [qwen-vl-text] coord item[3]: text=姓名:, bbox=[338, 222, 388, 238]
2026-08-10 16:13:00,514 INFO     29 [qwen-vl-text] coord item[4]: text=男, bbox=[607, 222, 625, 237]
2026-08-10 16:13:00,514 INFO     29 [qwen-vl-text] coord item[5]: text=年龄: 67岁, bbox=[676, 222, 800, 238]
2026-08-10 16:13:00,514 INFO     29 [qwen-vl-text] coord item[6]: text=申请科室: 老年医学呼吸内科, bbox=[75, 249, 325, 265]
2026-08-10 16:13:00,514 INFO     29 [qwen-vl-text] coord item[7]: text=机器型号: SE-, bbox=[338, 250, 478, 266]
2026-08-10 16:13:00,514 INFO     29 [qwen-vl-text] coord item[8]: text=Force-2, bbox=[450, 262, 522, 277]
2026-08-10 16:13:00,514 INFO     29 [qwen-vl-text] coord item[9]: text=床号, bbox=[528, 250, 568, 266]
2026-08-10 16:13:00,514 INFO     29 [qwen-vl-text] coord item[10]: text=号, bbox=[695, 250, 734, 266]
2026-08-10 16:13:00,514 INFO     29 [qwen-vl-text] coord item[11]: text=检查部位: 胸部CT平扫+增强,*碘海醇注射液【广西HR】, bbox=[74, 281, 570, 298]
2026-08-10 16:13:00,514 INFO     29 [qwen-vl-text] coord item[12]: text=检查日期: 2026-03-02, bbox=[606, 281, 862, 298]
2026-08-10 16:13:00,514 INFO     29 [qwen-vl-text] coord item[13]: text=(此报告仅供临床医师诊断参考,不作为疾病证明), bbox=[77, 305, 574, 324]
2026-08-10 16:13:00,514 INFO     29 [qwen-vl-text] coord item[14]: text=检查所见:, bbox=[74, 331, 173, 348]
2026-08-10 16:13:00,514 INFO     29 [qwen-vl-text] coord item[15]: text=两肺尖胸膜下见类圆形透亮影,较大者长径约0.8cm;右肺下叶基底段(Se4:IM144)见团, bbox=[79, 356, 919, 372]
2026-08-10 16:13:00,514 INFO     29 [qwen-vl-text] coord item[16]: text=块状密度增高灶,大小约为7.7cm×5.1cm×6.9cm,增强扫描中度强化;两肺可见多发实性结节, bbox=[79, 373, 919, 389]
2026-08-10 16:13:00,514 INFO     29 [qwen-vl-text] coord item[17]: text=影,较大位于右肺下叶外基底段(Se4:IM344),内可见空泡,长径约为1.1cm,增强扫描似见, bbox=[79, 390, 919, 406]
2026-08-10 16:13:00,514 INFO     29 [qwen-vl-text] coord item[18]: text=血管穿行。右肺中叶、左肺上叶下舌段及两肺下叶见条索状密度增高影;余肺叶内未见异常密, bbox=[79, 407, 909, 423]
2026-08-10 16:13:00,514 INFO     29 [qwen-vl-text] coord item[19]: text=度影及异常强化灶,右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张,两肺部分支气管, bbox=[79, 424, 909, 440]
2026-08-10 16:13:00,514 INFO     29 [qwen-vl-text] coord item[20]: text=管壁增厚,管腔变窄,气管、其余支气管通畅;肺门、纵隔结构清楚,纵隔、两侧肺门见多发, bbox=[79, 441, 910, 457]
2026-08-10 16:13:00,514 INFO     29 [qwen-vl-text] coord item[21]: text=淋巴结,大者短径约1.1cm。两侧胸膜增厚、钙化,胸膜腔未见积液。主动脉、冠状动脉见斑片, bbox=[79, 458, 919, 474]
2026-08-10 16:13:00,515 INFO     29 [qwen-vl-text] coord item[22]: text=状钙化灶。, bbox=[79, 475, 166, 491]
2026-08-10 16:13:00,516 INFO     29 [qwen-vl-text] coord item[23]: text=诊断意见:, bbox=[74, 625, 173, 643]
2026-08-10 16:13:00,516 INFO     29 [qwen-vl-text] coord item[24]: text=1.右肺下叶后基底段软组织肿块,肿瘤性病变?感染性病变?请结合临床及实验室检查;, bbox=[119, 650, 899, 666]
2026-08-10 16:13:00,516 INFO     29 [qwen-vl-text] coord item[25]: text=2.两肺多发实性结节,建议短期复查;, bbox=[119, 668, 452, 684]
2026-08-10 16:13:00,516 INFO     29 [qwen-vl-text] coord item[26]: text=3.右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张并两肺炎症;, bbox=[119, 685, 735, 701]
2026-08-10 16:13:00,517 INFO     29 [qwen-vl-text] coord item[27]: text=4.两肺上叶间隔旁型肺气肿;, bbox=[119, 702, 371, 718]
2026-08-10 16:13:00,517 INFO     29 [qwen-vl-text] coord item[28]: text=5.纵隔、两侧肺门淋巴结,建议复查;, bbox=[119, 719, 452, 735]
2026-08-10 16:13:00,517 INFO     29 [qwen-vl-text] coord item[29]: text=6.两侧胸膜肥厚、钙化;, bbox=[119, 736, 331, 752]
2026-08-10 16:13:00,517 INFO     29 [qwen-vl-text] coord item[30]: text=7.主动脉、冠状动脉硬化。, bbox=[119, 753, 352, 769]
2026-08-10 16:13:00,517 INFO     29 [qwen-vl-text] coord item[31]: text=检查技师:周春燚 报告医师:肖芳艳 审核医师:, bbox=[74, 785, 540, 802]
2026-08-10 16:13:00,517 INFO     29 [qwen-vl-text] coord item[32]: text=报告日期:2026-03-03 18:39:05 审核日期:2026-03-04 09:21:01, bbox=[74, 811, 866, 828]
2026-08-10 16:13:00,517 INFO     29 [qwen-vl-text] coord item[33]: text=地址:广西医科大学第一附属医院放射科 联系电话:0771-5356934 “广西HR”解码:广西影像检查项目互认, bbox=[79, 845, 921, 861]
2026-08-10 16:13:00,519 INFO     29 [qwen-vl-text] page=12 — 34/34 coords, api_time=14.2s
2026-08-10 16:13:00,519 INFO     29 [qwen-vl-text] new_positions (34):
[[12, 199.92, 487.9, 93.462, 118.722], [12, 259.42, 427.805, 124.616, 149.876], [12, 44.03, 89.25, 186.924, 200.396], [12, 201.10999999999999, 230.85999999999999, 186.924, 200.396], [12, 361.16499999999996, 371.875, 186.924, 199.554], [12, 402.21999999999997, 476.0, 186.924, 200.396], [12, 44.625, 193.375, 209.658, 223.13], [12, 201.10999999999999, 284.40999999999997, 210.5, 223.97199999999998], [12, 267.75, 310.59, 220.60399999999998, 233.23399999999998], [12, 314.15999999999997, 337.96, 210.5, 223.97199999999998], [12, 413.525, 436.72999999999996, 210.5, 223.97199999999998], [12, 44.03, 339.15, 236.602, 250.916], [12, 360.57, 512.89, 236.602, 250.916], [12, 45.815, 341.53, 256.81, 272.808], [12, 44.03, 102.935, 278.702, 293.01599999999996], [12, 47.004999999999995, 546.805, 299.752, 313.224], [12, 47.004999999999995, 546.805, 314.066, 327.538], [12, 47.004999999999995, 546.805, 328.38, 341.852], [12, 47.004999999999995, 540.855, 342.69399999999996, 356.166], [12, 47.004999999999995, 540.855, 357.008, 370.47999999999996], [12, 47.004999999999995, 541.4499999999999, 371.322, 384.794], [12, 47.004999999999995, 546.805, 385.63599999999997, 399.108], [12, 47.004999999999995, 98.77, 399.95, 413.42199999999997], [12, 44.03, 102.935, 526.25, 541.406], [12, 70.80499999999999, 534.905, 547.3, 560.7719999999999], [12, 70.80499999999999, 268.94, 562.456, 575.928], [12, 70.80499999999999, 437.325, 576.77, 590.242], [12, 70.80499999999999, 220.74499999999998, 591.084, 604.5559999999999], [12, 70.80499999999999, 268.94, 605.398, 618.87], [12, 70.80499999999999, 196.945, 619.712, 633.184], [12, 70.80499999999999, 209.44, 634.026, 647.4979999999999], [12, 44.03, 321.3, 660.97, 675.284], [12, 44.03, 515.27, 682.862, 697.1759999999999], [12, 47.004999999999995, 547.995, 711.49, 724.962]]
2026-08-10 16:13:00,519 INFO     29 [qwen-vl-text] ═══ DONE ═══ 34 positions, pages=1, time=19.0s
2026-08-10 16:13:00,519 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:13:00,533 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:13:00,533 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 16:13:00,533 INFO     29 [qwen-vl-text] positions(69): [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:13:00,533 INFO     29 [qwen-vl-text] page grouping: [13], lines per page: [69]
2026-08-10 16:13:00,965 INFO     29 [qwen-vl-text] page=13, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 16:13:00,967 INFO     29 [qwen-vl-text] LLM extraction start, text_len=658
2026-08-10 16:13:00,967 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:13:00,968 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 2043, \"bbox_end\": 2111, \"encounter_dates\": [\"2026-03-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "测量参数值:\n测量项目\n结果\n单位\n参考范围\n测量项目\n结果\n单位\n参考范围\n主动脉根部内径:\n27\nmm\n(20-35)\n左房前后径:\n35\nmm\n(24-39)\n左室舒末前后径:\n53\nmm\n(38-54)\n左室缩末前后径:\n32\nmm\n(24-37)\n室间隔舒末厚:\n10\nmm\n(6-11)\n左室后壁舒末厚:\n10\nmm\n(6-11)\n右室舒末前后径:\n18\nmm\n(15-30)\n右室流出道:\n27\nmm\n(15-32)\n主肺动脉内径:\n22\nmm\n(15-26)\nE/A\n<1\n(\n0.8-2.0)\ne'/a'\n<1\n(-)\nE/e'\n11.7\n(-)\n超声描述:\n描述:\n1、按比例各房室大小正常，房、室间隔连续完整，室间隔与左室壁厚度正常，静息状态下室壁收\n缩运动有力，未见节段性运动异常。左室收缩功能测定在正常范围，FS:40%，EF:70%，SV:95ml/B\n，CO:6.4L/min，EDV:135ml，心包腔内未探及液性区声像。\n2、三尖瓣形态结构正常，瓣口轻度反流，速度2.4m/s，压差22mmHg，瞬时反流量约2ml（无血流动\n力学意义），余各瓣膜形态结构正常，启闭运动好，二尖瓣血流图示E峰小于A峰。\n3、主动脉根部内径正常，升主动脉内径正常，管壁增厚，弹性降低，主肺动脉内径正常，内回声\n及血流信号未见异常。\n超声诊断:\n1、心脏形态结构及瓣膜功能大致正常。\n2、左室舒张功能降低，收缩功能测定在正常范围，\n诊断医师：吴颖/肖彩意\n报告日期：2026-03-02 10:12:46",
    "role": "user"
  }
]
2026-08-10 16:13:01,571 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:13:01.570+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:13:06,768 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:13:06,769 INFO     29 [qwen-vl-text] LLM output (len=1084):
{
  "exam_date": "2026-03-02",
  "report_date": "2026-03-02",
  "exam_name": "心脏超声",
  "exam_category": "imaging",
  "body_part": "心脏",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "测量参数值:\n| 测量项目 | 结果 | 单位 | 参考范围 |\n|---|---|---|---|\n| 主动脉根部内径: | 27 | mm | (20-35) |\n| 左房前后径: | 35 | mm | (24-39) |\n| 左室舒末前后径: | 53 | mm | (38-54) |\n| 左室缩末前后径: | 32 | mm | (24-37) |\n| 室间隔舒末厚: | 10 | mm | (6-11) |\n| 左室后壁舒末厚: | 10 | mm | (6-11) |\n| 右室舒末前后径: | 18 | mm | (15-30) |\n| 右室流出道: | 27 | mm | (15-32) |\n| 主肺动脉内径: | 22 | mm | (15-26) |\n| E/A | <1 | | ( 0.8-2.0) |\n| e'/a' | <1 | | (-) |\n| E/e' | 11.7 | | (-) |\n\n超声描述:\n描述:\n1、按比例各房室大小正常，房、室间隔连续完整，室间隔与左室壁厚度正常，静息状态下室壁收缩运动有力，未见节段性运动异常。左室收缩功能测定在正常范围，FS:40%，EF:70%，SV:95ml/B，CO:6.4L/min，EDV:135ml，心包腔内未探及液性区声像。\n2、三尖瓣形态结构正常，瓣口轻度反流，速度2.4m/s，压差22mmHg，瞬时反流量约2ml（无血流动力学意义），余各瓣膜形态结构正常，启闭运动好，二尖瓣血流图示E峰小于A峰。\n3、主动脉根部内径正常，升主动脉内径正常，管壁增厚，弹性降低，主肺动脉内径正常，内回声及血流信号未见异常。",
  "conclusion": "超声诊断:\n1、心脏形态结构及瓣膜功能大致正常。\n2、左室舒张功能降低，收缩功能测定在正常范围，",
  "physician": "吴颖/肖彩意",
  "reviewer": null
}
2026-08-10 16:13:06,783 INFO     29 [qwen-vl-text] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6753644, prompt_len=1478
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共69行）
["测量参数值:", "测量项目", "结果", "单位", "参考范围", "测量项目", "结果", "单位", "参考范围", "主动脉根部内径:", "27", "mm", "(20-35)", "左房前后径:", "35", "mm", "(24-39)", "左室舒末前后径:", "53", "mm", "(38-54)", "左室缩末前后径:", "32", "mm", "(24-37)", "室间隔舒末厚:", "10", "mm", "(6-11)", "左室后壁舒末厚:", "10", "mm", "(6-11)", "右室舒末前后径:", "18", "mm", "(15-30)", "右室流出道:", "27", "mm", "(15-32)", "主肺动脉内径:", "22", "mm", "(15-26)", "E/A", "<1", "(", "0.8-2.0)", "e'/a'", "<1", "(-)", "E/e'", "11.7", "(-)", "超声描述:", "描述:", "1、按比例各房室大小正常，房、室间隔连续完整，室间隔与左室壁厚度正常，静息状态下室壁收", "缩运动有力，未见节段性运动异常。左室收缩功能测定在正常范围，FS:40%，EF:70%，SV:95ml/B", "，CO:6.4L/min，EDV:135ml，心包腔内未探及液性区声像。", "2、三尖瓣形态结构正常，瓣口轻度反流，速度2.4m/s，压差22mmHg，瞬时反流量约2ml（无血流动", "力学意义），余各瓣膜形态结构正常，启闭运动好，二尖瓣血流图示E峰小于A峰。", "3、主动脉根部内径正常，升主动脉内径正常，管壁增厚，弹性降低，主肺动脉内径正常，内回声", "及血流信号未见异常。", "超声诊断:", "1、心脏形态结构及瓣膜功能大致正常。", "2、左室舒张功能降低，收缩功能测定在正常范围，", "诊断医师：吴颖/肖彩意", "报告日期：2026-03-02 10:12:46"]

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
2026-08-10 16:13:26,953 INFO     29 [qwen-vl-text] coord API raw response (len=3631):
[
	{"text": "测量参数值:", "bbox": [52, 314, 159, 332]},
	{"text": "测量项目", "bbox": [97, 336, 174, 353]},
	{"text": "结果", "bbox": [232, 337, 265, 350]},
	{"text": "单位", "bbox": [298, 337, 331, 350]},
	{"text": "参考范围", "bbox": [378, 337, 447, 350]},
	{"text": "测量项目", "bbox": [542, 335, 620, 352]},
	{"text": "结果", "bbox": [678, 337, 711, 350]},
	{"text": "单位", "bbox": [744, 337, 776, 350]},
	{"text": "参考范围", "bbox": [824, 337, 891, 350]},
	{"text": "主动脉根部内径:", "bbox": [57, 358, 177, 371]},
	{"text": "27", "bbox": [240, 359, 258, 371]},
	{"text": "mm", "bbox": [304, 361, 324, 371]},
	{"text": "(20-35)", "bbox": [386, 359, 440, 371]},
	{"text": "左房前后径:", "bbox": [502, 358, 592, 371]},
	{"text": "35", "bbox": [687, 359, 704, 371]},
	{"text": "mm", "bbox": [750, 361, 770, 371]},
	{"text": "(24-39)", "bbox": [830, 359, 882, 371]},
	{"text": "左室舒末前后径:", "bbox": [57, 378, 177, 391]},
	{"text": "53", "bbox": [240, 379, 258, 391]},
	{"text": "mm", "bbox": [304, 381, 324, 391]},
	{"text": "(38-54)", "bbox": [386, 379, 440, 391]},
	{"text": "左室缩末前后径:", "bbox": [502, 378, 624, 391]},
	{"text": "32", "bbox": [687, 379, 704, 391]},
	{"text": "mm", "bbox": [750, 381, 770, 391]},
	{"text": "(24-37)", "bbox": [830, 379, 882, 391]},
	{"text": "室间隔舒末厚:", "bbox": [57, 399, 159, 412]},
	{"text": "10", "bbox": [240, 400, 258, 412]},
	{"text": "mm", "bbox": [304, 402, 324, 412]},
	{"text": "(6-11)", "bbox": [389, 400, 437, 412]},
	{"text": "左室后壁舒末厚:", "bbox": [502, 399, 624, 412]},
	{"text": "10", "bbox": [687, 400, 704, 412]},
	{"text": "mm", "bbox": [750, 402, 770, 412]},
	{"text": "(6-11)", "bbox": [835, 400, 880, 412]},
	{"text": "右室舒末前后径:", "bbox": [57, 419, 177, 432]},
	{"text": "18", "bbox": [240, 420, 258, 432]},
	{"text": "mm", "bbox": [304, 422, 324, 432]},
	{"text": "(15-30)", "bbox": [386, 420, 440, 432]},
	{"text": "右室流出道:", "bbox": [502, 419, 592, 432]},
	{"text": "27", "bbox": [687, 420, 704, 432]},
	{"text": "mm", "bbox": [750, 422, 770, 432]},
	{"text": "(15-32)", "bbox": [830, 420, 882, 432]},
	{"text": "主肺动脉内径:", "bbox": [57, 440, 159, 453]},
	{"text": "22", "bbox": [240, 441, 258, 453]},
	{"text": "mm", "bbox": [304, 443, 324, 453]},
	{"text": "(15-26)", "bbox": [386, 441, 440, 453]},
	{"text": "E/A", "bbox": [500, 440, 527, 453]},
	{"text": "<1", "bbox": [687, 441, 701, 453]},
	{"text": "(0.8-2.0)", "bbox": [821, 440, 891, 453]},
	{"text": "e'/a'", "bbox": [57, 461, 93, 474]},
	{"text": "<1", "bbox": [240, 462, 258, 474]},
	{"text": "(-)", "bbox": [402, 462, 424, 474]},
	{"text": "E/e'", "bbox": [500, 461, 528, 474]},
	{"text": "11.7", "bbox": [678, 462, 710, 474]},
	{"text": "(-)", "bbox": [846, 462, 867, 474]},
	{"text": "超声描述:", "bbox": [52, 481, 138, 498]},
	{"text": "描述:", "bbox": [61, 504, 108, 520]},
	{"text": "1、按比例各房室大小正常，房、室间隔连续完整，室间隔与左室壁厚度正常，静息状态下室壁收", "bbox": [61, 523, 914, 540]},
	{"text": "缩运动有力，未见节段性运动异常。左室收缩功能测定在正常范围，FS:40%，EF:70%，SV:95ml/B", "bbox": [61, 543, 914, 560]},
	{"text": "，CO:6.4L/min，EDV:135ml，心包腔内未探及液性区声像。", "bbox": [61, 563, 570, 580]},
	{"text": "2、三尖瓣形态结构正常，瓣口轻度反流，速度2.4m/s，压差22mmHg，瞬时反流量约2ml（无血流动", "bbox": [61, 583, 922, 600]},
	{"text": "力学意义），余各瓣膜形态结构正常，启闭运动好，二尖瓣血流图示E峰小于A峰。", "bbox": [61, 603, 770, 620]},
	{"text": "3、主动脉根部内径正常，升主动脉内径正常，管壁增厚，弹性降低，主肺动脉内径正常，内回声", "bbox": [61, 623, 912, 640]},
	{"text": "及血流信号未见异常。", "bbox": [61, 643, 248, 660]},
	{"text": "超声诊断:", "bbox": [52, 660, 138, 677]},
	{"text": "1、心脏形态结构及瓣膜功能大致正常。", "bbox": [61, 686, 400, 703]},
	{"text": "2、左室舒张功能降低，收缩功能测定在正常范围，", "bbox": [61, 706, 500, 723]},
	{"text": "诊断医师：吴颖/肖彩意", "bbox": [674, 809, 877, 827]},
	{"text": "报告日期：2026-03-02 10:12:46", "bbox": [674, 830, 954, 847]}
]
2026-08-10 16:13:26,954 INFO     29 [qwen-vl-text] coord API: raw_items=68, valid_items=68, elapsed=20.2s
2026-08-10 16:13:26,954 INFO     29 [qwen-vl-text] coord item[0]: text=测量参数值:, bbox=[52, 314, 159, 332]
2026-08-10 16:13:26,954 INFO     29 [qwen-vl-text] coord item[1]: text=测量项目, bbox=[97, 336, 174, 353]
2026-08-10 16:13:26,954 INFO     29 [qwen-vl-text] coord item[2]: text=结果, bbox=[232, 337, 265, 350]
2026-08-10 16:13:26,954 INFO     29 [qwen-vl-text] coord item[3]: text=单位, bbox=[298, 337, 331, 350]
2026-08-10 16:13:26,954 INFO     29 [qwen-vl-text] coord item[4]: text=参考范围, bbox=[378, 337, 447, 350]
2026-08-10 16:13:26,954 INFO     29 [qwen-vl-text] coord item[5]: text=测量项目, bbox=[542, 335, 620, 352]
2026-08-10 16:13:26,954 INFO     29 [qwen-vl-text] coord item[6]: text=结果, bbox=[678, 337, 711, 350]
2026-08-10 16:13:26,954 INFO     29 [qwen-vl-text] coord item[7]: text=单位, bbox=[744, 337, 776, 350]
2026-08-10 16:13:26,954 INFO     29 [qwen-vl-text] coord item[8]: text=参考范围, bbox=[824, 337, 891, 350]
2026-08-10 16:13:26,954 INFO     29 [qwen-vl-text] coord item[9]: text=主动脉根部内径:, bbox=[57, 358, 177, 371]
2026-08-10 16:13:26,954 INFO     29 [qwen-vl-text] coord item[10]: text=27, bbox=[240, 359, 258, 371]
2026-08-10 16:13:26,954 INFO     29 [qwen-vl-text] coord item[11]: text=mm, bbox=[304, 361, 324, 371]
2026-08-10 16:13:26,954 INFO     29 [qwen-vl-text] coord item[12]: text=(20-35), bbox=[386, 359, 440, 371]
2026-08-10 16:13:26,954 INFO     29 [qwen-vl-text] coord item[13]: text=左房前后径:, bbox=[502, 358, 592, 371]
2026-08-10 16:13:26,954 INFO     29 [qwen-vl-text] coord item[14]: text=35, bbox=[687, 359, 704, 371]
2026-08-10 16:13:26,955 INFO     29 [qwen-vl-text] coord item[15]: text=mm, bbox=[750, 361, 770, 371]
2026-08-10 16:13:26,955 INFO     29 [qwen-vl-text] coord item[16]: text=(24-39), bbox=[830, 359, 882, 371]
2026-08-10 16:13:26,955 INFO     29 [qwen-vl-text] coord item[17]: text=左室舒末前后径:, bbox=[57, 378, 177, 391]
2026-08-10 16:13:26,955 INFO     29 [qwen-vl-text] coord item[18]: text=53, bbox=[240, 379, 258, 391]
2026-08-10 16:13:26,955 INFO     29 [qwen-vl-text] coord item[19]: text=mm, bbox=[304, 381, 324, 391]
2026-08-10 16:13:26,955 INFO     29 [qwen-vl-text] coord item[20]: text=(38-54), bbox=[386, 379, 440, 391]
2026-08-10 16:13:26,955 INFO     29 [qwen-vl-text] coord item[21]: text=左室缩末前后径:, bbox=[502, 378, 624, 391]
2026-08-10 16:13:26,955 INFO     29 [qwen-vl-text] coord item[22]: text=32, bbox=[687, 379, 704, 391]
2026-08-10 16:13:26,955 INFO     29 [qwen-vl-text] coord item[23]: text=mm, bbox=[750, 381, 770, 391]
2026-08-10 16:13:26,955 INFO     29 [qwen-vl-text] coord item[24]: text=(24-37), bbox=[830, 379, 882, 391]
2026-08-10 16:13:26,955 INFO     29 [qwen-vl-text] coord item[25]: text=室间隔舒末厚:, bbox=[57, 399, 159, 412]
2026-08-10 16:13:26,955 INFO     29 [qwen-vl-text] coord item[26]: text=10, bbox=[240, 400, 258, 412]
2026-08-10 16:13:26,955 INFO     29 [qwen-vl-text] coord item[27]: text=mm, bbox=[304, 402, 324, 412]
2026-08-10 16:13:26,955 INFO     29 [qwen-vl-text] coord item[28]: text=(6-11), bbox=[389, 400, 437, 412]
2026-08-10 16:13:26,955 INFO     29 [qwen-vl-text] coord item[29]: text=左室后壁舒末厚:, bbox=[502, 399, 624, 412]
2026-08-10 16:13:26,955 INFO     29 [qwen-vl-text] coord item[30]: text=10, bbox=[687, 400, 704, 412]
2026-08-10 16:13:26,955 INFO     29 [qwen-vl-text] coord item[31]: text=mm, bbox=[750, 402, 770, 412]
2026-08-10 16:13:26,955 INFO     29 [qwen-vl-text] coord item[32]: text=(6-11), bbox=[835, 400, 880, 412]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[33]: text=右室舒末前后径:, bbox=[57, 419, 177, 432]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[34]: text=18, bbox=[240, 420, 258, 432]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[35]: text=mm, bbox=[304, 422, 324, 432]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[36]: text=(15-30), bbox=[386, 420, 440, 432]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[37]: text=右室流出道:, bbox=[502, 419, 592, 432]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[38]: text=27, bbox=[687, 420, 704, 432]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[39]: text=mm, bbox=[750, 422, 770, 432]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[40]: text=(15-32), bbox=[830, 420, 882, 432]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[41]: text=主肺动脉内径:, bbox=[57, 440, 159, 453]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[42]: text=22, bbox=[240, 441, 258, 453]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[43]: text=mm, bbox=[304, 443, 324, 453]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[44]: text=(15-26), bbox=[386, 441, 440, 453]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[45]: text=E/A, bbox=[500, 440, 527, 453]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[46]: text=<1, bbox=[687, 441, 701, 453]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[47]: text=(0.8-2.0), bbox=[821, 440, 891, 453]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[48]: text=e'/a', bbox=[57, 461, 93, 474]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[49]: text=<1, bbox=[240, 462, 258, 474]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[50]: text=(-), bbox=[402, 462, 424, 474]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[51]: text=E/e', bbox=[500, 461, 528, 474]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[52]: text=11.7, bbox=[678, 462, 710, 474]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[53]: text=(-), bbox=[846, 462, 867, 474]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[54]: text=超声描述:, bbox=[52, 481, 138, 498]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[55]: text=描述:, bbox=[61, 504, 108, 520]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[56]: text=1、按比例各房室大小正常，房、室间隔连续完整，室间隔与左室壁厚度正常，静息状态下室壁收, bbox=[61, 523, 914, 540]
2026-08-10 16:13:26,956 INFO     29 [qwen-vl-text] coord item[57]: text=缩运动有力，未见节段性运动异常。左室收缩功能测定在正常范围，FS:40%，EF:70%，SV:95ml/B, bbox=[61, 543, 914, 560]
2026-08-10 16:13:26,957 INFO     29 [qwen-vl-text] coord item[58]: text=，CO:6.4L/min，EDV:135ml，心包腔内未探及液性区声像。, bbox=[61, 563, 570, 580]
2026-08-10 16:13:26,957 INFO     29 [qwen-vl-text] coord item[59]: text=2、三尖瓣形态结构正常，瓣口轻度反流，速度2.4m/s，压差22mmHg，瞬时反流量约2ml（无血流动, bbox=[61, 583, 922, 600]
2026-08-10 16:13:26,957 INFO     29 [qwen-vl-text] coord item[60]: text=力学意义），余各瓣膜形态结构正常，启闭运动好，二尖瓣血流图示E峰小于A峰。, bbox=[61, 603, 770, 620]
2026-08-10 16:13:26,957 INFO     29 [qwen-vl-text] coord item[61]: text=3、主动脉根部内径正常，升主动脉内径正常，管壁增厚，弹性降低，主肺动脉内径正常，内回声, bbox=[61, 623, 912, 640]
2026-08-10 16:13:26,957 INFO     29 [qwen-vl-text] coord item[62]: text=及血流信号未见异常。, bbox=[61, 643, 248, 660]
2026-08-10 16:13:26,957 INFO     29 [qwen-vl-text] coord item[63]: text=超声诊断:, bbox=[52, 660, 138, 677]
2026-08-10 16:13:26,957 INFO     29 [qwen-vl-text] coord item[64]: text=1、心脏形态结构及瓣膜功能大致正常。, bbox=[61, 686, 400, 703]
2026-08-10 16:13:26,957 INFO     29 [qwen-vl-text] coord item[65]: text=2、左室舒张功能降低，收缩功能测定在正常范围，, bbox=[61, 706, 500, 723]
2026-08-10 16:13:26,957 INFO     29 [qwen-vl-text] coord item[66]: text=诊断医师：吴颖/肖彩意, bbox=[674, 809, 877, 827]
2026-08-10 16:13:26,957 INFO     29 [qwen-vl-text] coord item[67]: text=报告日期：2026-03-02 10:12:46, bbox=[674, 830, 954, 847]
2026-08-10 16:13:26,959 INFO     29 [qwen-vl-text] page=13 — 69/69 coords, api_time=20.2s
2026-08-10 16:13:26,959 INFO     29 [qwen-vl-text] new_positions (69):
[[13, 30.939999999999998, 94.60499999999999, 264.388, 279.544], [13, 57.714999999999996, 103.53, 282.912, 297.226], [13, 138.04, 157.67499999999998, 283.75399999999996, 294.7], [13, 177.31, 196.945, 283.75399999999996, 294.7], [13, 224.91, 265.965, 283.75399999999996, 294.7], [13, 322.49, 368.9, 282.07, 296.384], [13, 403.40999999999997, 423.04499999999996, 283.75399999999996, 294.7], [13, 442.68, 461.71999999999997, 283.75399999999996, 294.7], [13, 490.28, 530.145, 283.75399999999996, 294.7], [13, 33.915, 105.315, 301.436, 312.382], [13, 142.79999999999998, 153.51, 302.27799999999996, 312.382], [13, 180.88, 192.78, 303.962, 312.382], [13, 229.67, 261.8, 302.27799999999996, 312.382], [13, 298.69, 352.24, 301.436, 312.382], [13, 408.765, 418.88, 302.27799999999996, 312.382], [13, 446.25, 458.15, 303.962, 312.382], [13, 493.84999999999997, 524.79, 302.27799999999996, 312.382], [13, 33.915, 105.315, 318.276, 329.222], [13, 142.79999999999998, 153.51, 319.118, 329.222], [13, 180.88, 192.78, 320.80199999999996, 329.222], [13, 229.67, 261.8, 319.118, 329.222], [13, 298.69, 371.28, 318.276, 329.222], [13, 408.765, 418.88, 319.118, 329.222], [13, 446.25, 458.15, 320.80199999999996, 329.222], [13, 493.84999999999997, 524.79, 319.118, 329.222], [13, 33.915, 94.60499999999999, 335.95799999999997, 346.904], [13, 142.79999999999998, 153.51, 336.8, 346.904], [13, 180.88, 192.78, 338.484, 346.904], [13, 231.45499999999998, 260.015, 336.8, 346.904], [13, 298.69, 371.28, 335.95799999999997, 346.904], [13, 408.765, 418.88, 336.8, 346.904], [13, 446.25, 458.15, 338.484, 346.904], [13, 496.825, 523.6, 336.8, 346.904], [13, 33.915, 105.315, 352.798, 363.74399999999997], [13, 142.79999999999998, 153.51, 353.64, 363.74399999999997], [13, 180.88, 192.78, 355.324, 363.74399999999997], [13, 229.67, 261.8, 353.64, 363.74399999999997], [13, 298.69, 352.24, 352.798, 363.74399999999997], [13, 408.765, 418.88, 353.64, 363.74399999999997], [13, 446.25, 458.15, 355.324, 363.74399999999997], [13, 493.84999999999997, 524.79, 353.64, 363.74399999999997], [13, 33.915, 94.60499999999999, 370.47999999999996, 381.426], [13, 142.79999999999998, 153.51, 371.322, 381.426], [13, 180.88, 192.78, 373.006, 381.426], [13, 229.67, 261.8, 371.322, 381.426], [13, 297.5, 313.565, 370.47999999999996, 381.426], [13, 408.765, 417.09499999999997, 371.322, 381.426], [13, 488.495, 530.145, 370.47999999999996, 381.426], [13, 33.915, 55.335, 388.162, 399.108], [13, 142.79999999999998, 153.51, 389.00399999999996, 399.108], [13, 239.19, 252.28, 389.00399999999996, 399.108], [13, 297.5, 314.15999999999997, 388.162, 399.108], [13, 403.40999999999997, 422.45, 389.00399999999996, 399.108], [13, 503.37, 515.865, 389.00399999999996, 399.108], [13, 30.939999999999998, 82.11, 405.002, 419.316], [13, 36.295, 64.25999999999999, 424.368, 437.84], [13, 36.295, 543.8299999999999, 440.366, 454.68], [13, 36.295, 543.8299999999999, 457.20599999999996, 471.52], [13, 36.295, 339.15, 474.046, 488.35999999999996], [13, 36.295, 548.59, 490.88599999999997, 505.2], [13, 36.295, 458.15, 507.726, 522.04], [13, 36.295, 542.64, 524.566, 538.88], [13, 36.295, 147.56, 541.406, 555.72], [13, 30.939999999999998, 82.11, 555.72, 570.034], [13, 36.295, 238.0, 577.612, 591.9259999999999], [13, 36.295, 297.5, 594.452, 608.766], [13, 401.03, 521.8149999999999, 681.178, 696.334], [13, 401.03, 567.63, 698.86, 713.174], [13, 401.03, 567.63, 698.86, 713.174]]
2026-08-10 16:13:26,959 INFO     29 [qwen-vl-text] ═══ DONE ═══ 69 positions, pages=1, time=26.4s
2026-08-10 16:13:26,959 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:13:26,960 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:13:26,960 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 16:13:26,960 INFO     29 [qwen-vl-text] positions(52): [[25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:13:26,960 INFO     29 [qwen-vl-text] page grouping: [25], lines per page: [52]
2026-08-10 16:13:27,153 INFO     29 [qwen-vl-text] page=25, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 16:13:27,155 INFO     29 [qwen-vl-text] LLM extraction start, text_len=607
2026-08-10 16:13:27,155 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:13:27,156 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 2386, \"bbox_end\": 2437, \"encounter_dates\": [\"2026-03-10\"], \"department\": \"老年呼吸\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "病理诊断报告书\n1/1\n标本条码\n1223023095\n医院\n广西医科大学第一附属医院\n病人姓名\n孔令祈\n科室\n老年呼吸\n病理号\n26018339\n性别\n男\n房/床号\n49\n住院门诊号\n1959880\n年龄\n67岁\n接收时间\n2026-03-08 14:15:50\n申请医生\n项目名称\n免疫组化8项\n送检材料\n肺组织\n临床诊断\n患者电话\n大体描述:\n福尔马林固定标本，核对送检标本、病人姓名和条形码与申请单一致。\n灰红条索状组织3段，长0.5-1.8cm，直径均0.05cm。取1盒全（共1盒蜡块）\n镜下所见：\n诊断意见：\n肺组织穿刺活检：\n-结合免疫组化，符合浸润性黏液型腺癌，请结合临床。\n-免疫组化：CK7（+），CK20（+），Villin（+），TTF-1（散在+），NapsinA（散在+），P40（-），CDX2（-），Ki67（\n热点区约60%+）。\n报告医师：陈明坚\n本检测仅对送检负责，如果对结果有疑义，请在报告发布后7天内与我们联系，多谢合作！\n收样点：广西医科大学第一附属医院-呼吸内\n科\n主检实验室：广西金域\n地址：南宁市西乡塘区总部路3号中国-东盟科技企业孵化基地二期1号厂房一、三、\n四层\n报告专用章\n网址：www.kingmed.com.cn\nGX003SCEJL7RJLY\n报告日期：2026-03-10 21:16:16\n更多报告服务\nCS 扫描全能王\n3亿人都在用的扫描App",
    "role": "user"
  }
]
2026-08-10 16:13:30,310 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:13:30,310 INFO     29 [qwen-vl-text] LLM output (len=530):
{
  "exam_date": "2026-03-08",
  "report_date": "2026-03-10",
  "exam_name": "免疫组化8项",
  "exam_category": "pathology",
  "body_part": "肺组织",
  "patient_name": "孔令祈",
  "patient_gender": "男",
  "department": "老年呼吸",
  "bed_number": "49",
  "findings": "大体描述:\n福尔马林固定标本，核对送检标本、病人姓名和条形码与申请单一致。\n灰红条索状组织3段，长0.5-1.8cm，直径均0.05cm。取1盒全（共1盒蜡块）",
  "conclusion": "诊断意见：\n肺组织穿刺活检：\n-结合免疫组化，符合浸润性黏液型腺癌，请结合临床。\n-免疫组化：CK7（+），CK20（+），Villin（+），TTF-1（散在+），NapsinA（散在+），P40（-），CDX2（-），Ki67（\n热点区约60%+）。",
  "physician": "陈明坚",
  "reviewer": null
}
2026-08-10 16:13:30,317 INFO     29 [qwen-vl-text] coord API call start, page=25, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1763221, prompt_len=1376
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共52行）
["病理诊断报告书", "1/1", "标本条码", "1223023095", "医院", "广西医科大学第一附属医院", "病人姓名", "孔令祈", "科室", "老年呼吸", "病理号", "26018339", "性别", "男", "房/床号", "49", "住院门诊号", "1959880", "年龄", "67岁", "接收时间", "2026-03-08 14:15:50", "申请医生", "项目名称", "免疫组化8项", "送检材料", "肺组织", "临床诊断", "患者电话", "大体描述:", "福尔马林固定标本，核对送检标本、病人姓名和条形码与申请单一致。", "灰红条索状组织3段，长0.5-1.8cm，直径均0.05cm。取1盒全（共1盒蜡块）", "镜下所见：", "诊断意见：", "肺组织穿刺活检：", "-结合免疫组化，符合浸润性黏液型腺癌，请结合临床。", "-免疫组化：CK7（+），CK20（+），Villin（+），TTF-1（散在+），NapsinA（散在+），P40（-），CDX2（-），Ki67（", "热点区约60%+）。", "报告医师：陈明坚", "本检测仅对送检负责，如果对结果有疑义，请在报告发布后7天内与我们联系，多谢合作！", "收样点：广西医科大学第一附属医院-呼吸内", "科", "主检实验室：广西金域", "地址：南宁市西乡塘区总部路3号中国-东盟科技企业孵化基地二期1号厂房一、三、", "四层", "报告专用章", "网址：www.kingmed.com.cn", "GX003SCEJL7RJLY", "报告日期：2026-03-10 21:16:16", "更多报告服务", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-10 16:13:44,853 INFO     29 [qwen-vl-text] coord API raw response (len=2877):
[
	{"text": "病理诊断报告书", "bbox": [423, 65, 595, 82]},
	{"text": "1/1", "bbox": [892, 93, 915, 102]},
	{"text": "标本条码", "bbox": [82, 113, 143, 125]},
	{"text": "1223023095", "bbox": [170, 114, 252, 124]},
	{"text": "医院", "bbox": [346, 113, 385, 125]},
	{"text": "广西医科大学第一附属医院", "bbox": [435, 114, 617, 124]},
	{"text": "病人姓名", "bbox": [82, 128, 143, 140]},
	{"text": "孔令祈", "bbox": [170, 129, 215, 140]},
	{"text": "科室", "bbox": [346, 128, 385, 140]},
	{"text": "老年呼吸", "bbox": [435, 129, 496, 140]},
	{"text": "病理号", "bbox": [633, 128, 680, 140]},
	{"text": "26018339", "bbox": [743, 130, 808, 140]},
	{"text": "性别", "bbox": [82, 144, 120, 156]},
	{"text": "男", "bbox": [170, 145, 184, 156]},
	{"text": "房/床号", "bbox": [346, 144, 397, 156]},
	{"text": "49", "bbox": [435, 145, 452, 156]},
	{"text": "住院门诊号", "bbox": [633, 144, 715, 156]},
	{"text": "1959880", "bbox": [743, 145, 800, 156]},
	{"text": "年龄", "bbox": [82, 159, 120, 171]},
	{"text": "67岁", "bbox": [170, 160, 200, 171]},
	{"text": "接收时间", "bbox": [346, 159, 407, 171]},
	{"text": "2026-03-08 14:15:50", "bbox": [435, 160, 590, 171]},
	{"text": "申请医生", "bbox": [633, 159, 695, 171]},
	{"text": "项目名称", "bbox": [82, 175, 143, 187]},
	{"text": "免疫组化8项", "bbox": [170, 176, 254, 187]},
	{"text": "送检材料", "bbox": [633, 175, 695, 187]},
	{"text": "肺组织", "bbox": [743, 176, 790, 187]},
	{"text": "临床诊断", "bbox": [82, 190, 143, 202]},
	{"text": "患者电话", "bbox": [633, 190, 695, 202]},
	{"text": "大体描述：", "bbox": [82, 210, 150, 222]},
	{"text": "福尔马林固定标本，核对送检标本、病人姓名和条形码与申请单一致。", "bbox": [82, 225, 544, 237]},
	{"text": "灰红条索状组织3段，长0.5-1.8cm，直径均0.05cm。取1盒全（共1盒蜡块）", "bbox": [82, 239, 586, 251]},
	{"text": "镜下所见：", "bbox": [82, 272, 150, 284]},
	{"text": "诊断意见：", "bbox": [82, 491, 150, 503]},
	{"text": "肺组织穿刺活检：", "bbox": [82, 507, 194, 519]},
	{"text": "-结合免疫组化，符合浸润性黏液型腺癌，请结合临床。", "bbox": [82, 520, 447, 532]},
	{"text": "-免疫组化：CK7（+），CK20（+），Villin（+），TTF-1（散在+），NapsinA（散在+），P40（-），CDX2（-），Ki67（", "bbox": [82, 534, 912, 546]},
	{"text": "热点区约60%+）。", "bbox": [82, 547, 198, 559]},
	{"text": "报告医师：陈明坚", "bbox": [723, 809, 915, 823]},
	{"text": "本检测仅对送检负责，如果对结果有疑义，请在报告发布后7天内与我们联系，多谢合作！", "bbox": [82, 834, 584, 846]},
	{"text": "收样点：广西医科大学第一附属医院-呼吸内", "bbox": [640, 831, 917, 842]},
	{"text": "科", "bbox": [700, 842, 714, 852]},
	{"text": "主检实验室：广西金域", "bbox": [82, 854, 230, 866]},
	{"text": "地址：南宁市西乡塘区总部路3号中国-东盟科技企业孵化基地二期1号厂房一、三、", "bbox": [82, 868, 551, 879]},
	{"text": "四层", "bbox": [124, 880, 151, 890]},
	{"text": "报告专用章", "bbox": [106, 882, 178, 900]},
	{"text": "网址：www.kingmed.com.cn", "bbox": [347, 893, 517, 903]},
	{"text": "GX003SCEJL7RJLY", "bbox": [655, 874, 760, 883]},
	{"text": "报告日期：2026-03-10 21:16:16", "bbox": [608, 893, 811, 903]},
	{"text": "更多报告服务", "bbox": [857, 897, 913, 905]},
	{"text": "CS 扫描全能王", "bbox": [857, 955, 972, 970]},
	{"text": "3亿人都在用的扫描App", "bbox": [857, 975, 972, 984]}
]
2026-08-10 16:13:44,853 INFO     29 [qwen-vl-text] coord API: raw_items=52, valid_items=52, elapsed=14.5s
2026-08-10 16:13:44,854 INFO     29 [qwen-vl-text] coord item[0]: text=病理诊断报告书, bbox=[423, 65, 595, 82]
2026-08-10 16:13:44,854 INFO     29 [qwen-vl-text] coord item[1]: text=1/1, bbox=[892, 93, 915, 102]
2026-08-10 16:13:44,854 INFO     29 [qwen-vl-text] coord item[2]: text=标本条码, bbox=[82, 113, 143, 125]
2026-08-10 16:13:44,854 INFO     29 [qwen-vl-text] coord item[3]: text=1223023095, bbox=[170, 114, 252, 124]
2026-08-10 16:13:44,854 INFO     29 [qwen-vl-text] coord item[4]: text=医院, bbox=[346, 113, 385, 125]
2026-08-10 16:13:44,854 INFO     29 [qwen-vl-text] coord item[5]: text=广西医科大学第一附属医院, bbox=[435, 114, 617, 124]
2026-08-10 16:13:44,854 INFO     29 [qwen-vl-text] coord item[6]: text=病人姓名, bbox=[82, 128, 143, 140]
2026-08-10 16:13:44,854 INFO     29 [qwen-vl-text] coord item[7]: text=孔令祈, bbox=[170, 129, 215, 140]
2026-08-10 16:13:44,854 INFO     29 [qwen-vl-text] coord item[8]: text=科室, bbox=[346, 128, 385, 140]
2026-08-10 16:13:44,854 INFO     29 [qwen-vl-text] coord item[9]: text=老年呼吸, bbox=[435, 129, 496, 140]
2026-08-10 16:13:44,854 INFO     29 [qwen-vl-text] coord item[10]: text=病理号, bbox=[633, 128, 680, 140]
2026-08-10 16:13:44,854 INFO     29 [qwen-vl-text] coord item[11]: text=26018339, bbox=[743, 130, 808, 140]
2026-08-10 16:13:44,854 INFO     29 [qwen-vl-text] coord item[12]: text=性别, bbox=[82, 144, 120, 156]
2026-08-10 16:13:44,854 INFO     29 [qwen-vl-text] coord item[13]: text=男, bbox=[170, 145, 184, 156]
2026-08-10 16:13:44,854 INFO     29 [qwen-vl-text] coord item[14]: text=房/床号, bbox=[346, 144, 397, 156]
2026-08-10 16:13:44,854 INFO     29 [qwen-vl-text] coord item[15]: text=49, bbox=[435, 145, 452, 156]
2026-08-10 16:13:44,854 INFO     29 [qwen-vl-text] coord item[16]: text=住院门诊号, bbox=[633, 144, 715, 156]
2026-08-10 16:13:44,854 INFO     29 [qwen-vl-text] coord item[17]: text=1959880, bbox=[743, 145, 800, 156]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[18]: text=年龄, bbox=[82, 159, 120, 171]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[19]: text=67岁, bbox=[170, 160, 200, 171]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[20]: text=接收时间, bbox=[346, 159, 407, 171]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[21]: text=2026-03-08 14:15:50, bbox=[435, 160, 590, 171]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[22]: text=申请医生, bbox=[633, 159, 695, 171]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[23]: text=项目名称, bbox=[82, 175, 143, 187]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[24]: text=免疫组化8项, bbox=[170, 176, 254, 187]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[25]: text=送检材料, bbox=[633, 175, 695, 187]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[26]: text=肺组织, bbox=[743, 176, 790, 187]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[27]: text=临床诊断, bbox=[82, 190, 143, 202]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[28]: text=患者电话, bbox=[633, 190, 695, 202]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[29]: text=大体描述：, bbox=[82, 210, 150, 222]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[30]: text=福尔马林固定标本，核对送检标本、病人姓名和条形码与申请单一致。, bbox=[82, 225, 544, 237]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[31]: text=灰红条索状组织3段，长0.5-1.8cm，直径均0.05cm。取1盒全（共1盒蜡块）, bbox=[82, 239, 586, 251]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[32]: text=镜下所见：, bbox=[82, 272, 150, 284]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[33]: text=诊断意见：, bbox=[82, 491, 150, 503]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[34]: text=肺组织穿刺活检：, bbox=[82, 507, 194, 519]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[35]: text=-结合免疫组化，符合浸润性黏液型腺癌，请结合临床。, bbox=[82, 520, 447, 532]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[36]: text=-免疫组化：CK7（+），CK20（+），Villin（+），TTF-1（散在+），NapsinA（散在+），P40（-），CDX2（-），Ki67（, bbox=[82, 534, 912, 546]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[37]: text=热点区约60%+）。, bbox=[82, 547, 198, 559]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[38]: text=报告医师：陈明坚, bbox=[723, 809, 915, 823]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[39]: text=本检测仅对送检负责，如果对结果有疑义，请在报告发布后7天内与我们联系，多谢合作！, bbox=[82, 834, 584, 846]
2026-08-10 16:13:44,855 INFO     29 [qwen-vl-text] coord item[40]: text=收样点：广西医科大学第一附属医院-呼吸内, bbox=[640, 831, 917, 842]
2026-08-10 16:13:44,856 INFO     29 [qwen-vl-text] coord item[41]: text=科, bbox=[700, 842, 714, 852]
2026-08-10 16:13:44,856 INFO     29 [qwen-vl-text] coord item[42]: text=主检实验室：广西金域, bbox=[82, 854, 230, 866]
2026-08-10 16:13:44,856 INFO     29 [qwen-vl-text] coord item[43]: text=地址：南宁市西乡塘区总部路3号中国-东盟科技企业孵化基地二期1号厂房一、三、, bbox=[82, 868, 551, 879]
2026-08-10 16:13:44,856 INFO     29 [qwen-vl-text] coord item[44]: text=四层, bbox=[124, 880, 151, 890]
2026-08-10 16:13:44,856 INFO     29 [qwen-vl-text] coord item[45]: text=报告专用章, bbox=[106, 882, 178, 900]
2026-08-10 16:13:44,856 INFO     29 [qwen-vl-text] coord item[46]: text=网址：www.kingmed.com.cn, bbox=[347, 893, 517, 903]
2026-08-10 16:13:44,856 INFO     29 [qwen-vl-text] coord item[47]: text=GX003SCEJL7RJLY, bbox=[655, 874, 760, 883]
2026-08-10 16:13:44,856 INFO     29 [qwen-vl-text] coord item[48]: text=报告日期：2026-03-10 21:16:16, bbox=[608, 893, 811, 903]
2026-08-10 16:13:44,856 INFO     29 [qwen-vl-text] coord item[49]: text=更多报告服务, bbox=[857, 897, 913, 905]
2026-08-10 16:13:44,856 INFO     29 [qwen-vl-text] coord item[50]: text=CS 扫描全能王, bbox=[857, 955, 972, 970]
2026-08-10 16:13:44,856 INFO     29 [qwen-vl-text] coord item[51]: text=3亿人都在用的扫描App, bbox=[857, 975, 972, 984]
2026-08-10 16:13:44,856 INFO     29 [qwen-vl-text] page=25 — 52/52 coords, api_time=14.5s
2026-08-10 16:13:44,856 INFO     29 [qwen-vl-text] new_positions (52):
[[25, 251.685, 354.025, 54.73, 69.044], [25, 530.74, 544.425, 78.306, 85.884], [25, 48.79, 85.085, 95.146, 105.25], [25, 101.14999999999999, 149.94, 95.988, 104.408], [25, 205.87, 229.075, 95.146, 105.25], [25, 258.825, 367.115, 95.988, 104.408], [25, 48.79, 85.085, 107.776, 117.88], [25, 101.14999999999999, 127.925, 108.618, 117.88], [25, 205.87, 229.075, 107.776, 117.88], [25, 258.825, 295.12, 108.618, 117.88], [25, 376.635, 404.59999999999997, 107.776, 117.88], [25, 442.085, 480.76, 109.46, 117.88], [25, 48.79, 71.39999999999999, 121.24799999999999, 131.352], [25, 101.14999999999999, 109.47999999999999, 122.08999999999999, 131.352], [25, 205.87, 236.215, 121.24799999999999, 131.352], [25, 258.825, 268.94, 122.08999999999999, 131.352], [25, 376.635, 425.42499999999995, 121.24799999999999, 131.352], [25, 442.085, 476.0, 122.08999999999999, 131.352], [25, 48.79, 71.39999999999999, 133.878, 143.982], [25, 101.14999999999999, 119.0, 134.72, 143.982], [25, 205.87, 242.165, 133.878, 143.982], [25, 258.825, 351.05, 134.72, 143.982], [25, 376.635, 413.525, 133.878, 143.982], [25, 48.79, 85.085, 147.35, 157.454], [25, 101.14999999999999, 151.13, 148.192, 157.454], [25, 376.635, 413.525, 147.35, 157.454], [25, 442.085, 470.04999999999995, 148.192, 157.454], [25, 48.79, 85.085, 159.98, 170.084], [25, 376.635, 413.525, 159.98, 170.084], [25, 48.79, 89.25, 176.82, 186.924], [25, 48.79, 323.68, 189.45, 199.554], [25, 48.79, 348.66999999999996, 201.238, 211.34199999999998], [25, 48.79, 89.25, 229.024, 239.128], [25, 48.79, 89.25, 413.42199999999997, 423.526], [25, 48.79, 115.42999999999999, 426.894, 436.998], [25, 48.79, 265.965, 437.84, 447.94399999999996], [25, 48.79, 542.64, 449.628, 459.73199999999997], [25, 48.79, 117.80999999999999, 460.574, 470.678], [25, 430.185, 544.425, 681.178, 692.966], [25, 48.79, 347.47999999999996, 702.228, 712.332], [25, 380.79999999999995, 545.615, 699.702, 708.9639999999999], [25, 416.5, 424.83, 708.9639999999999, 717.384], [25, 48.79, 136.85, 719.068, 729.172], [25, 48.79, 327.84499999999997, 730.856, 740.1179999999999], [25, 73.78, 89.845, 740.9599999999999, 749.38], [25, 63.07, 105.91, 742.644, 757.8], [25, 206.465, 307.615, 751.906, 760.326], [25, 389.72499999999997, 452.2, 735.908, 743.486], [25, 361.76, 482.54499999999996, 751.906, 760.326], [25, 509.91499999999996, 543.235, 755.274, 762.01], [25, 509.91499999999996, 578.3399999999999, 804.11, 816.74], [25, 509.91499999999996, 578.3399999999999, 820.9499999999999, 828.528]]
2026-08-10 16:13:44,856 INFO     29 [qwen-vl-text] ═══ DONE ═══ 52 positions, pages=1, time=17.9s
2026-08-10 16:13:44,872 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 16:13:44,873 INFO     29 [Trace] task=5212989c | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Extractor:ExaminationReport | outputs={"chunks": "6 items, types={'ExaminationReport': 6}", "html": "", "json": "2438 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 11}"}
2026-08-10 16:13:44,873 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 16:13:44,874 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:13:44.874+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 71, "failed": 0, "current": {"5212989c94d411f1bd9827cf206dfa2d": {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:13:44,882 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:13:44,883 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 16:13:45,777 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:13:45,782 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 16:13:45,783 INFO     29 [Trace] task=5212989c | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "2438 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 11}"}
2026-08-10 16:13:45,783 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 16:13:45,785 INFO     29 [ChunkMerger] Merged 18 chunks from 9 sources: {'Extractor:LabExam': 11, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 6, 'Extractor:Progress': 1} (filtered 6 noise chunks)
2026-08-10 16:13:45,798 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 16:13:45,798 INFO     29 [Trace] task=5212989c | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "18 items, types={'LabReport': 11, 'AdmissionRecord': 1, 'ExaminationReport': 6}", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf"}
2026-08-10 16:13:45,798 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 16:13:46,404 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786377509684, 'update_date': datetime.datetime(2026, 8, 10, 15, 58, 29), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1195436, 'status': '1'}
2026-08-10 16:13:46,655 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   结核杆菌DNA*  TB-DNA  <5.00E+02  拷贝  <5.00E+02  False   
---
   乙型肝炎表面抗原*  None  0.00  IU/ml  0-0.08  False    乙型肝炎表面抗体*  None  14.85  mIU/mL  0-10  True    乙型肝炎e抗原*  None  0.00  PElu/ml  0-0.10  False    乙型肝炎e抗体*  None  0.14  IU/mL  0-0.20  False    乙型肝炎核心抗体*  None  0.27  IU/mL  0-0.50  False   
---
   丙型肝炎抗体定量*  None  0.06  COI  0-1  False    不加热血清反应素试验*  None  阴性(-)  None  阴性(-)  False    人免疫缺陷病毒抗体定量*  None  0.08  COI  0-1  False    梅毒螺旋体抗体定量*  None  0.08  COI  0-1  False   
---
   糖化血红蛋白HbA1c*  HbA1c  6.40  %  4.0-6.0  True    糖化血红蛋白HbA1a  HbA1a  0.50  %  0-0.91  False    糖化血红蛋白HbA1b  HbA1b  1.10  %  0.35-1.82  False   
---
   凝血酶原时间  None  11.50  S  9-15  False    国际标准化比值  None  1.04  None  0.8-1.4  False    纤维蛋白原  None  4.43  g/L  2.00 -5.00  False    活化部分凝血活酶时间  None  32.30  S  23.00 -40.00  False    凝血酶时间  None  13.00  S  10.3-16.6  False    凝血酶原活动度  None  98  %  70-130  False    D-二聚体定量  None  69  ng/ml  0-450  False   
---
   总胆红素*  TBIL  8.7  µmol/L  0-26.0  False    直接胆红素*  DBIL  3.6  µmol/L  0-6.8  False    间接胆红素  IBIL  5.1  µmol/L  3.1-14.3  False    直/总胆比值  DB/TB  0.41  None  None  False    总蛋白#  TP  74.5  g/L  65-85  False    白蛋白*  ALB  39.3  g/L  40-55  True    球蛋白  GLO  35.2  g/L  20-40  False    白蛋白/球蛋白  A/G  1.1  None  1.2-2.4  True    谷氨酰转肽酶*  GGT  30  U/L  10-60  False    总胆汁酸*  TBA  13.2  µmol/L  0-10  True    天门冬氨酸氨基转移酶*  AST  15  U/L  15-40  False    丙氨酸氨基转移酶*  ALT  14  U/L  9-50  False    谷草/谷丙比值  AST/ALT  1.1  None  None  False    碱性磷酸酶*  ALP  64  U/L  45-125  False    前白蛋白*  PA  251.5  mg/L  200-430  False    胆碱酯酶*  CHE  8382  U/L  5000-12000  False    尿素*  UREA  6.98  mmol/L  3.6-9.5  False    肌酐*  CREA  136  µmol/L  57-111  True    尿酸*  UA  551  µmol/L  208-428  True    碳酸氢根*  HCO3  21.6  mmol/L  22-29  True    总胆固醇*  T-CHO  3.10  mmol/L  3.1-5.7  False   
---
   胆碱酯酶*  CHE  8382  U/L  5000-12000  False    尿素*  UREA  6.98  mmol/L  3.6-9.5  False    肌酐*  CREA  136  μmol/L  57-111  True    尿酸*  UA  551  μmol/L  208-428  True    碳酸氢根*  HCO3  21.6  mmol/L  22-29  True    总胆固醇*  T-CHO  3.18  mmol/L  <5.2  False    甘油三酯*  TG  1.27  mmol/L  <1.7  False    低密度脂蛋白胆固醇*  LDL-C  1.78  mmol/L  <3.4(低危人群)  False    空腹血葡萄糖*  GLU  4.79  mmol/L  3.9-6.1  False    钾*  K  4.18  mmol/L  3.5-5.3  False    钠*  Na  141.1  mmol/L  137-147  False    氯*  CL  106.4  mmol/L  99-110  False    总钙*  Ca  2.25  mmol/L  2.11-2.52  False    镁*  Mg  0.78  mmol/L  0.75-1.02  False    磷*  P  0.95  mmol/L  0.85-1.51  False    肌酸激酶*  CK  84  U/L  50-310  False    肌酸激酶同工酶MB  CK-MB  13  U/L  0-25  False    乳酸脱氢酶*  LD  167  U/L  120-250  False    α-羟丁酸脱氢酶*  α-HBD  109  U/L  72-182  False    免疫球蛋白E*  IgE  1960.6  IU/ml  <100  True   
---
   白细胞计数*  WBC  8.490  10~9/L  3.5-9.5  False    红细胞计数*  RBC  5.81  10~12/L  4.3-5.8  True    血红蛋白*  HGB  157.00  g/L  130-175  False    血小板计数*  PLT  268.00  10~9/L  125-350  False    中性粒细胞百分比  NEU%  0.6920  None  0.4-0.75  False    淋巴细胞百分比  LYM%  0.1970  None  0.2-0.5  True    单核细胞百分比  MONO%  0.0630  None  0.03-0.1  False    嗜酸性粒细胞百分比  EO%  0.0450  None  0.004-0.08  False    嗜碱性粒细胞百分比  BA SO%  0.0030  None  0-0.01  False    中性粒细胞绝对值  NEU  5.88  10~9/L  1.8-6.3  False    淋巴细胞绝对值  LYM  1.67  10~9/L  1.1-3.2  False    单核细胞绝对值  MONO  0.53  10~9/L  0.1-0.6  False    嗜酸性粒细胞绝对值  EOS  0.38  10~9/L  0.02-0.52  False    嗜碱性粒细胞绝对值  BA SO  0.03  10~9/L  0-0.06  False    平均红细胞体积*  MCV  83.70  fl  82-100  False    平均RBC血红蛋白含量*  MCH  26.90  pg  27-34  True    平均RBC血红蛋白浓度*  MCHC  323.00  g/L  316-354  False    红细胞比容*  HCT  0.486  None  0.4-0.5  False    RBC体积分布宽度CV  RDWCV  0.15  None  0.11-0.14  True    血小板体积分布宽度  PDW  0.16  None  0.15-0.18  False   
---
   吸氧浓度  FI02  21.00  %  21-100  False    体温  T  36.4  None  29-41  False    钙测定  Ca++  1.19  mmol/L  1.15-1.29  False    钠测定  Na+  143.20  mmol/L  136-146  False    钾测定  K+  3.98  mmol/L  3.5-4.5  False    氧合指数(p/f)  p02(a,T)/F02  315.0  None  400-500  True    红细胞外剩余碱  BEecf  -1.80  mmol/l  -3-3  False    酸碱度 (PH)  PH  7.383  None  7.35-7.45  False    pH校正值(pHT)  pH(T)  7.392  None  7.35-7.45  False    氧分压 (pO2)  pO2  66.20  mmHg  83-108  True    氧分压校正值  pO2(T)  63.50  mmHg  83-108  True    二氧化碳分压  pCO2  39.90  mmHg  35-45  False    CO2分压校正  PCO2(T)  38.90  mmHg  35-45  False    氯测定  Cl-  102.00  mmol/L  98-106  False    血红蛋白测定(Hb)  Hb  162.00  g/L  120-160  True    氧合血红蛋白  F02Hb  92.0  %  94-98  True    高铁血红蛋白  MetHb  0.10  None  None  False    总血氧饱和度  s02  92.9  %  93-98  True    CO红蛋白  COHb  1.00  %  0-2  False    血CO2含量  ctCO2  24.50  mmol/L  24-32  False    还原血红蛋白  FHHB  6.9  None  None  False   
---
   酸碱度 (PH)  PH  7.383  None  7.35-7.45  False    pH校正值(pHT)  pH(T)  7.392  None  7.35-7.45  False    氧分压 (pO2)  pO2  66.20  mmHg  83-108  True    氧分压校正值  pO2(T)  63.50  mmHg  83-108  True    二氧化碳分压  pCO2  39.90  mmHg  35-45  False    CO2分压校正  PCO2(T)  38.90  mmHg  35-45  False    氯测定  Cl-  102.00  mmol/L  98-106  False    血红蛋白测定(Hb)  Hb  162.00  g/L  120-160  True    氧合血红蛋白  F02Hb  92.0  %  94-98  True    高铁血红蛋白  MetHb  0.10  None  None  False    总血氧饱和度  s02  92.9  %  93-98  True    CO红蛋白  C0Hb  1.00  %  0-2  False    血CO2含量  ctCO2  24.50  mmol/L  24-32  False    还原血红蛋白  FHHB  6.9  %  2-7  False    标准碳酸氢根  cHCO3  23.00  mmol/L  22-26  False    实际剩余碱  ABE (BE(B))  -1.6  mmol/L  -3-3  False    实际碳酸氢根  HCO3-  23.20  mmol/L  None  False    肺泡动脉氧分压差  P02(A-a,T)e  36.0  mmHg  10-25  True    动脉与肺泡氧分压比  P02(a/A,T)  64.0  %  85-95  True    呼吸指数  RI  57.0  None  None  False    葡萄糖测定  Glu  6.70  None  None  True   
---
   KRAS  None  p.G12V  None  None  True    CDKN2A  None  p.R80*  None  None  True    TP53  None  p.G279E  None  None  True    PD-L1 TPS  TPS  <1%  %  None  False    PD-L1 CPS  CPS  1  None  None  False    ALK  None  未检测到与用药相关突变  None  None  False    BRCA1  None  未检测到与用药相关突变  None  None  False    BRCA2  None  未检测到与用药相关突变  None  None  False    EGFR  None  未检测到与用药相关突变  None  None  False    ERBB2(HER2)  None  未检测到与用药相关突变  None  None  False    FGFR2  None  未检测到与用药相关突变  None  None  False    FGFR3  None  未检测到与用药相关突变  None  None  False    KIT  None  未检测到与用药相关突变  None  None  False    KRAS  None  NM_033360.4 exon2 c.35G>T p.G12V 35.80%  None  None  True    MET  None  未检测到与用药相关突变  None  None  False    NRG1  None  未检测到与用药相关突变  None  None  False    NTRK1  None  未检测到与用药相关突变  None  None  False   
---
病史
主诉：咳嗽、咳痰1月余
现病史：患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、
呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。至当地医院体检发现肺部阴影，具体不详。2026-02-26至中
山大学附属第一医院广西医院就诊，查胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm
，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋
巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。具体诊治不详。为进一步治疗，遂
至我院门诊就诊，门诊拟“肺占位性病变”收治入院。自发病以来，患者精神、食欲、睡眠正常，大小便正
常，体重无明显变化。
既往史：平素健康状况：良好。
既往病史：否认高血压、冠心病、糖尿病史。
传染病史：否，否认肝炎、结核或其他传染病史。
预防接种史：正规。
过敏史：否认过敏史。
外伤史：否认外伤史。
手术史：2年前曾行尿道结石手术，具体不详。
输血史：否认输血史。
系统回顾：无特殊。
个人史：出生地：广西壮族自治区南宁市青秀区
地方病地区居住情况：无
冶游史：否认冶游史
职业与工作条件有无工业毒物、粉尘、放射性物质及接触史：无
广西医科大学第一附属医院 孔令祈
11:24
2026-03-19
姜晓红 (D450199...
姜晓红 (D450199...
烟酒嗜好及药物使用史：有吸烟史，约10支/天，已吸烟40年，否认饮酒史。
婚姻史：有婚姻史，结婚年龄：适龄结婚。有生育史，育有1子。
家族史：否认相似家族病史及遗传病史。
请患者或病史叙述者仔细确认以上病史记录并签字：[患者]
体格检查
一般情况：
体温：36.8℃
脉搏：75次/分
呼吸：21次/分
血压：138/72mmHg
身高：161CM
体重：74kg
发育：正常
营养：良好
神志：清楚
体位：自主体位
面容：正常面容
表情：自如
步态：正常
体型：正力型
配合检查：合作
皮肤黏膜:
色
泽:正常
皮
疹:全身皮肤未见皮疹
皮下出血:全身皮肤未见皮下出血
毛发分布:毛发分布正常
温度与湿度:温度、湿度、弹性均正常
水
肿:未见水肿
肝
掌:无
蜘
蛛
痣:未见蜘蛛痣
其他表现:无
淋巴结:全身浅表淋巴结未扪及肿大
头部:
头颅:头颅大小正常,无畸形
眼:眉毛,眼睑,结膜,眼球未见异常,双侧巩膜无黄染
耳:双耳外观未见异常,乳突无压痛,外耳道未见分泌物
鼻:鼻部外观未见异常,鼻翼无扇动,鼻腔无分泌物,鼻窦区无压痛
咽喉:双侧扁桃体未见肿大,表面未见脓性分泌物,咽未见异常,声音正常
口腔:唇,舌,牙齿,牙龈正常
颈部:
颈部运动:颈软无抵抗
颈静脉:无怒张
气管:居中
颈动脉搏动:正常
肝-颈静脉回流征:阴性
广西医科大:
预览 验证CA签名 手工解锁 删除 病历参考 更新数据 加载全部病程 个人模板管理 返回
20部：
003470 20.2.11
003470 20.2.11
003470 20.2.11
003470 20.2.11
胸部：胸廓对称无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常
肺部：
视诊：双侧呼吸运动均匀对称，无增强或者减弱
触诊：双肺触觉语颤对称无异常，未触及胸膜摩擦感
叩诊：双肺叩诊呈清音
听诊：双肺呼吸音清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音
心脏：
视诊：心尖搏动未见异常，位于左侧第五肋间锁骨中线内0.5cm，无异常隆起及凹陷
触诊：心尖搏动未触及异常，未触及震颤及心包摩擦感
叩诊：心界不大
听诊：心率：75次/分，心律：齐 A2 > P2
心音 S1：有力， 心音 S2：有力， 心音 S3：无， 心音 S4：无
杂音：各瓣膜区未闻及杂音
额外心音：无
心包摩擦音：无
周围血管：未见异常血管征
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41
编辑
功能
表格
签名
其他
打印
预览
验证CA签名
手工解锁
删除
病历参考
更新数据
加载全部病程
个人模板管理
返回
腹部:
视诊: 外形: 腹部外形正常
腹围: 未测
脐部: 正常
胃形: 未见
肠形: 未见
蠕动波: 未见
腹式呼吸: 正常
腹壁静脉曲张: 无
腹壁其它情况: 无
触诊: 全腹柔软
压痛反跳痛: 无压痛及反跳痛
波动感: 无
振水声: 无
腹部包块: 腹部未触及包块
肝脏: 肝脏肋下未触及
胆囊: 未触及, Murphy征阴性
脾脏: 脾脏肋下未触及
肾脏: 未触及
输尿管压痛点: 无压痛
叩诊: 肝浊音界: 正常,
肝上界位于锁骨中线, 第五肋间
移动性浊音: 阴性,
肾区叩痛: 无
听诊: 肠鸣音无明显增强或减弱, 未闻及血管杂音
肛门直肠: 未查
生殖器: 未查
脊柱四肢:
脊柱外形: 脊柱正常生理弯曲
70 四 肢：四肢无畸形，未见杵状指（趾），未见静脉曲张，双下肢无凹陷性水肿
003470 20.2.41.64
关 节：各关节未见异常，活动无受限
肌 肉：未见肌肉萎缩，肌张力正常。四肢肌力5级。
神经系统：
浅反射：双侧浅反射正常引出
深反射：双侧深反射正常引出
病理反射：未引出
脑膜刺激征：阴性
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
专科情况
神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下肢无凹陷性水肿。
实验室及器械检查结果
(2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm
，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋巴结彩超
：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
003470 20.2.41.64
CS 扫描全能王
3亿人都在用的扫描App
2026-02-28 18:30
男，因“咳嗽、咳痰1月余”于2026-02-28 15:23入非急诊步行入科。
病例特点如下：1、老年期男性，起病缓，病程短。2、患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，
伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。3、既往史：平素
健康状况：良好。既往病史：否认高血压、冠心病、糖尿病史。传染病史：否，否认肝炎、结核或其他传染病史。预
防接种史：正规。过敏史：否认过敏史。外伤史：否认外伤史。手术史：2年前曾行尿道结石手术，具体不详。输血
史：否认输血史。系统回顾：无特殊。否认新冠肺炎流行病接触史。4、查体：T：36.8℃，P：75次/分，R：21次/分
，BP：138/72mmHg。神志清楚，正常面容，皮肤巩膜无黄染，全身浅表淋巴结未扪及肿大，颈静脉无怒张。胸廓对称
无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常，双肺叩诊呈清音，双肺呼吸音
清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音。心界不大，心率75次/分，心律齐，各瓣膜区未闻及杂音。腹
部外形正常，全腹柔软，无压痛及反跳痛，腹部未触及包块，肝脏肋下未触及，脾脏肋下未触及。移动性浊音阴性。
双下肢无凹陷性水肿。浅反射：双侧浅反射正常引出。深反射：双侧深反射正常引出。病理反射：未引出。脑膜刺激
征：阴性5、专科情况：神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下
肢无凹陷性水肿。6、辅助检查：（2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组
织肿块，最大截断面约77mm*60mm，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧
胸膜肥厚、钙化。浅表淋巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。
初步诊断：1.肺部阴影
2.细菌性肺炎
诊断依据：1.老年男性，起步缓，病程短
2.咳嗽，咳淡黄色粘液痰
3.外院胸部CT提示右肺下叶后基底段软组织肿块
鉴别诊断。
1.肺结核球
编辑
功能
表格
签名
其他
打印
预览
验证CA签名
手工解锁
删除
病历参考
更新数据
加载全部病程
个人模板管理
返回
鉴别诊断：
1.肺结核球：多见于年轻患者，病灶多见于结核好发部位，如肺上叶尖后段和下叶背段，直径一般<3
cm。一般无症状，病灶边界清楚，密度高，可有包膜。有时含钙化点，周围有卫星灶。
2.急性粟粒性肺结核：应与弥漫型细支气管肺泡癌相鉴别。通常粟粒型肺结核患者年龄较轻，有发热
，盗汗等全身中毒症状，呼吸道症状不明显。x线表现为细小、分布均匀、密度较淡的粟粒样结节病灶。
而细支气管—肺泡细胞癌两肺多有大小不等的结节状播散病灶，边界清楚、密度较高，进行性发展和增大
，且有进行性呼吸困难。
3.肺炎：若无毒性症状，抗生素治疗后肺部阴影吸收缓慢，或同一部位反复发生肺炎时，应考虑到肺
癌可能。肺部慢性炎症机化，形成团块状的炎性假瘤，也易与肺癌相混淆。但炎性假瘤往往形态不整，边
缘不齐，核心密度较高，易伴有胸膜增厚，病灶长期无明显变化。
4.肺脓肿：起病急，中毒症状严重，多有寒战、高热、咳嗽、咳大量脓臭痰等症状。肺部x线表现为
均匀的大片状炎性阴影，空洞内常见较深液平。结合纤支镜检查和痰脱落细胞检查可以鉴别。
5.纵隔淋巴瘤：颇似中央型肺癌，常为双侧性，可有发热等全身症状，需病理诊断。
VTE血栓风险评估：创建时间:2026-02-28 15:37:11,评估节点:入院,量表名称:Padua评分,分数:0,评分描述:低危,
预防措施:undefined
VTE出血风险评估：创建时间:2026-02-28 18:35:54,评估节点:入院,量表名称:内科出血风险评估,分数:1,评分描述：
低危,预防措施:undefined
诊疗计划：1.内科护理常规,II级护理。
2.完善必要辅助检查如血肿瘤标志物、痰液化验、胸部增强CT、支气管镜检查或浅表淋巴结及肺穿刺活检
以确诊，必要时行颅脑MRI、腹部超声、骨扫描或PET-CT等检查以利进一步疾病诊治。
3.给予吸氧、抗感染及止血、镇痛等对症支持治疗；明确病理类型拟定下一步治疗方案。
是否需手术治疗：否
医师签名：
住院医师：
---
影像检查报告单
病人 ID:
姓名:
性别: 男
年龄: 67岁
申请科室: 老年医学呼吸内科
机器型号: SE-MR4
住院号
检查部位: 颅脑颅脑MR平扫及增强+DWI,*钆特酸葡胺注射液【广西HR】
检查日期: 2026-03-13
(此报告仅供临床医师诊断参考,不作为疾病证明)
检查所见:
左侧基底节区、两侧放射冠、右侧侧脑室前后角旁见小斑片状、斑点状等T1、稍
长T2信号灶,FLAIR呈高信号,边界欠清,DWI未见弥散受限;余脑实质信号未见异
常,DWI未见明确弥散受限区,增强扫描未见异常强化灶;静脉窦强化充盈良好,未
见异常;各脑室及脑沟、裂、池对称性轻度增宽;中线结构无移位。
诊断意见:
脑白质病变--改良Fasekas1级;轻度脑萎缩。
检查技师: 唐成
报告医师: 郭仟
审核医师: 张
报告日期: 2026-03-16 15:13:19
审核日期: 2026-03-16 18:28:39
地址: 广西医科大学第一附属医院放射科
联系电话: 0771-5356934
“广西HR”解释: 广西影像检查项目互认
---
科
检查部位：全身骨显像 显像剂：99mTc-MDP 临床诊断：1.肺占位性病变,2.细菌性肺炎,3.肺
剂量：25mCi 部阴影
（此报告仅供临床医师诊断参考，不作为疾病证明）
检查所见：
静脉注射99mTc-MDP 3小时后行全身骨显像前位、后位各1帧：
全身骨像完整、显影基本清晰。颅骨、胸骨、椎体、肩胛骨、肋骨、骨盆及四肢骨显像剂分
布未见明显异常改变。
双肾显影，膀胱部分充盈。
诊断意见：
全身骨显像未见明显异常改变。
报告医师：巫殷豪
审核医师：彭盛梅
报告日期：2026-03-10
广西医科大学第一附属医院
---
影像检查报告单
病人ID:
姓名:
性别: 男
年龄: 67岁
申请科室:
机器型号: SE-
床号: 49床
住院号: 1959
Force-2
检查部位: 下腹部,上腹部CT平扫+增强,(新)碘帕醇注射液
【广西HR】
检查日期: 2026-03-11
(此报告仅供临床医师诊断参考,不作为疾病证明)
检查所见:
双侧肾上腺见多个结节状稍低/低密度影,较大者大小约1.6cm×1.2cm,增强扫
描不均匀强化。肝脏各叶比例正常,肝实质内见多发类圆形低密度无强化灶,较大者
位于S8,大小约1.2cm×1.1cm;余肝实质未见异常密度影及异常强化灶。肝内、外胆
管未见扩张,胆囊不大,囊壁均匀,囊内密度未见异常。脾脏、胰腺形态、大小、密
度未见异常,增强扫描未见异常强化,右肾体积缩小,双肾实质内见多个类圆形低密
度无强化灶,较大者大小约0.9cm×1.5cm;双侧肾盂肾盏及输尿管未见扩张。腹部肠
管分布正常,管腔未见扩张、积液,腹腔内未见明确肿块影;肝门及腹主动脉旁未见
增大淋巴结,腹膜腔未见积液。
诊断意见:
1.双侧肾上腺占位,考虑转移瘤可能性大,请结合临床;
2.肝多发囊肿;
3.右肾萎缩,双肾囊肿。
检查技师:刘辰民
报告医师:谢金桓
审核医师: 冯涛
报告日期:2026-03-11 14:21:30
审核日期:2026-03-11 16:15:45
地址:广西医科大学第一附属医院放射科
联系电话:0771-5356934
“广西HR”解释:广西影像检查项目互认
---
广西医科大学第一附属医院
影像检查报告单
病人ID:
姓名:
男
年龄: 67岁
申请科室: 老年医学呼吸内科
机器型号: SE-
Force-2
床号
号
检查部位: 胸部CT平扫+增强,*碘海醇注射液【广西HR】
检查日期: 2026-03-02
(此报告仅供临床医师诊断参考,不作为疾病证明)
检查所见:
两肺尖胸膜下见类圆形透亮影,较大者长径约0.8cm;右肺下叶基底段(Se4:IM144)见团
块状密度增高灶,大小约为7.7cm×5.1cm×6.9cm,增强扫描中度强化;两肺可见多发实性结节
影,较大位于右肺下叶外基底段(Se4:IM344),内可见空泡,长径约为1.1cm,增强扫描似见
血管穿行。右肺中叶、左肺上叶下舌段及两肺下叶见条索状密度增高影;余肺叶内未见异常密
度影及异常强化灶,右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张,两肺部分支气管
管壁增厚,管腔变窄,气管、其余支气管通畅;肺门、纵隔结构清楚,纵隔、两侧肺门见多发
淋巴结,大者短径约1.1cm。两侧胸膜增厚、钙化,胸膜腔未见积液。主动脉、冠状动脉见斑片
状钙化灶。
诊断意见:
1.右肺下叶后基底段软组织肿块,肿瘤性病变?感染性病变?请结合临床及实验室检查;
2.两肺多发实性结节,建议短期复查;
3.右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张并两肺炎症;
4.两肺上叶间隔旁型肺气肿;
5.纵隔、两侧肺门淋巴结,建议复查;
6.两侧胸膜肥厚、钙化;
7.主动脉、冠状动脉硬化。
检查技师:周春燚 报告医师:肖芳艳 审核医师:
报告日期:2026-03-03 18:39:05 审核日期:2026-03-04 09:21:01
地址:广西医科大学第一附属医院放射科 联系电话:0771-5356934 “广西HR”解码:广西影像检查项目互认
2026-08-10 16:13:48,024 INFO     29 [EMBED-PIPELINE] batch[16:32] text_for_embed=测量参数值:
测量项目
结果
单位
参考范围
测量项目
结果
单位
参考范围
主动脉根部内径:
27
mm
(20-35)
左房前后径:
35
mm
(24-39)
左室舒末前后径:
53
mm
(38-54)
左室缩末前后径:
32
mm
(24-37)
室间隔舒末厚:
10
mm
(6-11)
左室后壁舒末厚:
10
mm
(6-11)
右室舒末前后径:
18
mm
(15-30)
右室流出道:
27
mm
(15-32)
主肺动脉内径:
22
mm
(15-26)
E/A
<1
(
0.8-2.0)
e'/a'
<1
(-)
E/e'
11.7
(-)
超声描述:
描述:
1、按比例各房室大小正常，房、室间隔连续完整，室间隔与左室壁厚度正常，静息状态下室壁收
缩运动有力，未见节段性运动异常。左室收缩功能测定在正常范围，FS:40%，EF:70%，SV:95ml/B
，CO:6.4L/min，EDV:135ml，心包腔内未探及液性区声像。
2、三尖瓣形态结构正常，瓣口轻度反流，速度2.4m/s，压差22mmHg，瞬时反流量约2ml（无血流动
力学意义），余各瓣膜形态结构正常，启闭运动好，二尖瓣血流图示E峰小于A峰。
3、主动脉根部内径正常，升主动脉内径正常，管壁增厚，弹性降低，主肺动脉内径正常，内回声
及血流信号未见异常。
超声诊断:
1、心脏形态结构及瓣膜功能大致正常。
2、左室舒张功能降低，收缩功能测定在正常范围，
诊断医师：吴颖/肖彩意
报告日期：2026-03-02 10:12:46
---
病理诊断报告书
1/1
标本条码
1223023095
医院
广西医科大学第一附属医院
病人姓名
孔令祈
科室
老年呼吸
病理号
26018339
性别
男
房/床号
49
住院门诊号
1959880
年龄
67岁
接收时间
2026-03-08 14:15:50
申请医生
项目名称
免疫组化8项
送检材料
肺组织
临床诊断
患者电话
大体描述:
福尔马林固定标本，核对送检标本、病人姓名和条形码与申请单一致。
灰红条索状组织3段，长0.5-1.8cm，直径均0.05cm。取1盒全（共1盒蜡块）
镜下所见：
诊断意见：
肺组织穿刺活检：
-结合免疫组化，符合浸润性黏液型腺癌，请结合临床。
-免疫组化：CK7（+），CK20（+），Villin（+），TTF-1（散在+），NapsinA（散在+），P40（-），CDX2（-），Ki67（
热点区约60%+）。
报告医师：陈明坚
本检测仅对送检负责，如果对结果有疑义，请在报告发布后7天内与我们联系，多谢合作！
收样点：广西医科大学第一附属医院-呼吸内
科
主检实验室：广西金域
地址：南宁市西乡塘区总部路3号中国-东盟科技企业孵化基地二期1号厂房一、三、
四层
报告专用章
网址：www.kingmed.com.cn
GX003SCEJL7RJLY
报告日期：2026-03-10 21:16:16
更多报告服务
CS 扫描全能王
3亿人都在用的扫描App
2026-08-10 16:13:48,207 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 16:13:48,207 INFO     29 [Trace] task=5212989c | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "18 items, types={'LabReport': 11, 'AdmissionRecord': 1, 'ExaminationReport': 6}", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "embedding_token_consumption": 18115}
2026-08-10 16:13:48,207 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 16:13:48,587 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 16:13:48,587 INFO     29 [Trace] task=5212989c | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":18,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 16:13:48,596 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(15, 191, 250, 153, 163) row[-1]=(15, 191, 250, 153, 163)
2026-08-10 16:13:48,596 INFO     29 [DIAG-EXECUTOR] row_position_int len=5 row[0]=(16, 104, 174, 148, 158) row[-1]=(16, 106, 175, 227, 237)
2026-08-10 16:13:48,597 INFO     29 [DIAG-EXECUTOR] row_position_int len=4 row[0]=(17, 138, 207, 151, 160) row[-1]=(17, 135, 212, 211, 220)
2026-08-10 16:13:48,597 INFO     29 [DIAG-EXECUTOR] row_position_int len=3 row[0]=(18, 123, 206, 156, 166) row[-1]=(18, 123, 204, 196, 205)
2026-08-10 16:13:48,597 INFO     29 [DIAG-EXECUTOR] row_position_int len=7 row[0]=(19, 148, 202, 154, 164) row[-1]=(19, 149, 206, 275, 285)
2026-08-10 16:13:48,597 INFO     29 [DIAG-EXECUTOR] row_position_int len=21 row[0]=(20, 197, 234, 144, 153) row[-1]=(20, 193, 237, 535, 544)
2026-08-10 16:13:48,597 INFO     29 [DIAG-EXECUTOR] row_position_int len=20 row[0]=(21, 197, 234, 139, 148) row[-1]=(21, 193, 242, 518, 527)
2026-08-10 16:13:48,597 INFO     29 [DIAG-EXECUTOR] row_position_int len=20 row[0]=(22, 207, 252, 148, 158) row[-1]=(22, 196, 268, 519, 528)
2026-08-10 16:13:48,598 INFO     29 [DIAG-EXECUTOR] row_position_int len=21 row[0]=(23, 221, 255, 146, 155) row[-1]=(23, 214, 264, 529, 538)
2026-08-10 16:13:48,598 INFO     29 [DIAG-EXECUTOR] row_position_int len=21 row[0]=(24, 208, 257, 146, 155) row[-1]=(24, 216, 258, 526, 536)
2026-08-10 16:13:48,598 INFO     29 [DIAG-EXECUTOR] row_position_int len=17 row[0]=(25, 132, 154, 718, 726) row[-1]=(25, 129, 155, 778, 786)
2026-08-10 16:13:48,599 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 16:13:48,599 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 16:13:48,599 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 16:13:48,599 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 16:13:48,599 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 16:13:48,599 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 16:13:48,600 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 16:13:48,603 INFO     29 set_progress(5212989c94d411f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 16:13:48 [DOC Engine]:
Start to index...
2026-08-10 16:13:48,637 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.022s]
2026-08-10 16:13:48,641 INFO     29 set_progress(5212989c94d411f1bd9827cf206dfa2d), progress: 0.8055555555555556, progress_msg: 
2026-08-10 16:13:48,664 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.013s]
2026-08-10 16:13:48,717 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.015s]
2026-08-10 16:13:48,735 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.009s]
2026-08-10 16:13:48,746 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.006s]
2026-08-10 16:13:48,756 INFO     29 set_progress(5212989c94d411f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 16:13:48 Indexing done (0.15s). Task done (867.54s)
2026-08-10 16:13:48,760 INFO     29 [Done], chunks(18), token(18115), elapsed:867.54
2026-08-10 16:13:49,458 INFO     29 handle_task done for task {"id": "5212989c94d411f1bd9827cf206dfa2d", "doc_id": "5146dde294d411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786377505615, "task_type": "dataflow", "root_trace_id": "dcb79a3731f64433b8725399d8a8afc5", "root_traceparent": "00-dcb79a3731f64433b8725399d8a8afc5-302e6d507a1dc427-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
