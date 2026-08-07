# 基准结果：广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf

## 基本信息

- 文件：`广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf`
- 大小：27147.7 KB
- PDF 总页数：26
- doc_id：`f701d642918211f18dbe1f8f96f1c395`
- 上传方式：skip
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-07T12:59:08  完成时间：2026-08-07T12:59:10  耗时：1.2s
- progress_msg：`04:54:48 Indexing done (0.19s). Task done (848.55s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | b223f96c | 9 | 1-9 | 病史 主诉：咳嗽、咳痰1月余 现病史：患者及家属共诉1月余前无明显诱因下出现阵发 |
| 2 | 32456967 | 1 | 10-10 | 影像检查报告单 病人 ID: 姓名: 性别: 男 年龄: 67岁 申请科室: 老 |
| 3 | 53fcc41a | 2 | 11-12 | 科 检查部位：全身骨显像 显像剂：99mTc-MDP 临床诊断：1.肺占位性病变 |
| 4 | 077854ca | 1 | 12-12 | 影像检查报告单 病人ID: 姓名: 性别: 男 年龄: 67岁 申请科室: 机器 |
| 5 | 0a6c1157 | 1 | 13-13 | 广西医科大学第一附属医院 影像检查报告单 病人ID: 姓名: 男 年龄: 67岁 |
| 6 | 928aee47 | 1 | 14-14 | 测量参数值: 测量项目 结果 单位 参考范围 测量项目 结果 单位 参考范围 主 |
| 7 | 635cb426 | 1 | 26-26 | 广西金域医学检验实验室 本报告单经过电子签名认证 Guangxi Kingmed |
| 8 | 7fe3ba9e | 1 | 16-16 | <table><tr><td>乙型肝炎表面抗原*</td><td>None</t |
| 9 | 1a44a92b | 1 | 17-17 | <table><tr><td>丙型肝炎抗体定量*</td><td>None</t |
| 10 | 1fef5186 | 1 | 19-19 | <table><tr><td>凝血酶原时间</td><td>None</td>< |
| 11 | edf1a7a5 | 1 | 20-20 | <table><tr><td>总胆红素*</td><td>TBIL</td><t |
| 12 | ee833205 | 1 | 21-21 | <table><tr><td>胆碱酯酶*</td><td>CHE</td><td |
| 13 | c2df376f | 1 | 23-23 | <table><tr><td>吸氧浓度</td><td>FI02</td><td |
| 14 | 49317722 | 1 | 24-24 | <table><tr><td>酸碱度 (PH)</td><td>PH</td>< |
| 15 | 4e6c548e | 1 | 15-15 | <table><tr><td>结核杆菌DNA*</td><td>TB-DNA</ |
| 16 | c34a1eb6 | 1 | 18-18 | <table><tr><td>糖化血红蛋白HbA1c*</td><td>HbA1 |
| 17 | 511a7f93 | 1 | 22-22 | <table><tr><td>白细胞计数*</td><td>WBC</td><t |
| 18 | c4d69b55 | 1 | 25-25 | <table><tr><td>KRAS</td><td>None</td><td |

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
- ChunkMerger：`{"found": true, "merged": 18, "sources": 8, "stats": {"Extractor:LabExam": 11, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 6}, "filtered_noise": 5}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-07 04:54:44,870 INFO     29 [ChunkMerger] Merged 18 chunks from 8 sources: {'Extractor:LabExam': 11, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Pres`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-07 04:40:46,459 INFO     29 handle_task begin for task {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-07 04:40:46,745 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-07 04:40:46,870 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-07 04:40:46,958 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-07 04:40:46,958 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-07 04:40:46,985 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-07 04:40:46,985 INFO     29 ============================================================
2026-08-07 04:40:46,985 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-07 04:40:46,985 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-07 04:40:46,985 INFO     29 ============================================================
2026-08-07 04:40:46,985 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-07 04:40:46,985 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-07 04:40:46,995 INFO     29 No torch found.
2026-08-07 04:40:51,446 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=26
2026-08-07 04:40:52,369 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5346931, prompt_len=764
2026-08-07 04:40:55,035 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:40:55.034+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:40:57,372 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-07 04:40:57,373 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-07 04:40:57,395 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5346931, prompt_len=401
2026-08-07 04:41:02,745 INFO     29 [qwen-vl-parser] text API response (len=714):
["病史", "主诉：咳嗽、咳痰1月余", "现病史：患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、", "呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。至当地医院体检发现肺部阴影，具体不详。2026-02-26至中", "山大学附属第一医院广西医院就诊，查胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm", "，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋", "巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。具体诊治不详。为进一步治疗，遂", "至我院门诊就诊，门诊拟“肺占位性病变”收治入院。自发病以来，患者精神、食欲、睡眠正常，大小便正", "常，体重无明显变化。", "既往史：平素健康状况：良好。", "既往病史：否认高血压、冠心病、糖尿病史。", "传染病史：否，否认肝炎、结核或其他传染病史。", "预防接种史：正规。", "过敏史：否认过敏史。", "外伤史：否认外伤史。", "手术史：2年前曾行尿道结石手术，具体不详。", "输血史：否认输血史。", "系统回顾：无特殊。", "个人史：出生地：广西壮族自治区南宁市青秀区", "地方病地区居住情况：无", "冶游史：否认冶游史", "职业与工作条件有无工业毒物、粉尘、放射性物质及接触史：无", "广西医科大学第一附属医院 孔令祈", "11:24", "2026-03-19", "姜晓红 (D450199...", "姜晓红 (D450199...", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-07 04:41:02,748 INFO     29 [qwen-vl-parser] page=1 text: 29 lines (bbox 0-28)
2026-08-07 04:41:02,749 INFO     29 [qwen-vl-parser] page=1 text: 29 sections
2026-08-07 04:41:03,346 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3061308, prompt_len=764
2026-08-07 04:41:06,726 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-07 04:41:06,727 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-07 04:41:06,740 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3061308, prompt_len=401
2026-08-07 04:41:08,964 INFO     29 [qwen-vl-parser] text API response (len=307):
["烟酒嗜好及药物使用史：有吸烟史，约10支/天，已吸烟40年，否认饮酒史。", "婚姻史：有婚姻史，结婚年龄：适龄结婚。有生育史，育有1子。", "家族史：否认相似家族病史及遗传病史。", "请患者或病史叙述者仔细确认以上病史记录并签字：[患者]", "体格检查", "一般情况：", "体温：36.8℃", "脉搏：75次/分", "呼吸：21次/分", "血压：138/72mmHg", "身高：161CM", "体重：74kg", "发育：正常", "营养：良好", "神志：清楚", "体位：自主体位", "面容：正常面容", "表情：自如", "步态：正常", "体型：正力型", "配合检查：合作"]
2026-08-07 04:41:08,965 INFO     29 [qwen-vl-parser] page=2 text: 21 lines (bbox 29-49)
2026-08-07 04:41:08,966 INFO     29 [qwen-vl-parser] page=2 text: 21 sections
2026-08-07 04:41:09,524 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3743105, prompt_len=764
2026-08-07 04:41:10,177 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-07 04:41:10,179 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-07 04:41:10,201 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3743105, prompt_len=401
2026-08-07 04:41:14,508 INFO     29 [qwen-vl-parser] text API response (len=436):
["皮肤黏膜:", "色泽: 正常", "皮疹: 全身皮肤未见皮疹", "皮下出血: 全身皮肤未见皮下出血", "毛发分布: 毛发分布正常", "温度与湿度: 温度、湿度、弹性均正常", "水肿: 未见水肿", "肝掌: 无", "蜘蛛痣: 未见蜘蛛痣", "其他表现: 无", "淋巴结: 全身浅表淋巴结未扪及肿大", "头部:", "头颅: 头颅大小正常, 无畸形", "眼: 眉毛, 眼睑, 结膜, 眼球未见异常, 双侧巩膜无黄染", "耳: 双耳外观未见异常, 乳突无压痛, 外耳道未见分泌物", "鼻: 鼻部外观未见异常, 鼻翼无扇动, 鼻腔无分泌物, 鼻窦区无压痛", "咽喉: 双侧扁桃体未见肿大, 表面未见脓性分泌物, 咽未见异常, 声音正常", "口腔: 唇, 舌, 牙齿, 牙龈正常", "颈部:", "颈部运动: 颈软无抵抗", "颈静脉: 无怒张", "气管: 居中", "颈动脉搏动: 正常", "肝-颈静脉回流征: 阴性", "广西医科大:"]
2026-08-07 04:41:14,510 INFO     29 [qwen-vl-parser] page=3 text: 25 lines (bbox 50-74)
2026-08-07 04:41:14,511 INFO     29 [qwen-vl-parser] page=3 text: 25 sections
2026-08-07 04:41:15,141 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3863999, prompt_len=764
2026-08-07 04:41:16,770 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-07 04:41:16,770 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-07 04:41:16,803 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3863999, prompt_len=401
2026-08-07 04:41:24,304 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:41:24.301+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:41:54,381 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:41:54.380+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:42:24,182 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:42:24.181+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:42:54,068 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:42:54.067+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:43:23,876 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:43:23.872+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:43:26,838 INFO     29 [qwen-vl-parser] text API response (len=18170):
["预览 验证CA签名 手工解锁 删除 病历参考 更新数据 加载全部病程 个人模板管理 返回", "20 部：", "003470 20.2.11", "003470 20.2.11", "003470 20.2.11", "003470 20.2.11", "胸部：胸廓对称无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常", "肺部：", "视诊：双侧呼吸运动均匀对称，无增强或者减弱", "触诊：双肺触觉语颤对称无异常，未触及胸膜摩擦感", "叩诊：双肺叩诊呈清音", "听诊：双肺呼吸音清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音", "心脏：", "视诊：心尖搏动未见异常，位于左侧第五肋间锁骨中线内0.5cm，无异常隆起及凹陷", "触诊：心尖搏动未触及异常，未触及震颤及心包摩擦感", "叩诊：心界不大", "听诊：心率：75次/分，心律：齐 A2 > P2", "心音 S1：有力， 心音 S2：有力， 心音 S3：无， 心音 S4：无", "杂音：各瓣膜区未闻及杂音", "额外心音：无", "心包摩擦音：无", "周围血管：未见异常血管征", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.
2026-08-07 04:43:26,846 INFO     29 [qwen-vl-parser] page=4 text: 864 lines (bbox 75-938)
2026-08-07 04:43:26,846 INFO     29 [qwen-vl-parser] page=4 text: 864 sections
2026-08-07 04:43:27,464 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3635836, prompt_len=764
2026-08-07 04:43:29,270 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-07 04:43:29,272 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-07 04:43:29,303 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3635836, prompt_len=401
2026-08-07 04:43:33,111 INFO     29 [qwen-vl-parser] text API response (len=506):
["编辑", "功能", "表格", "签名", "其他", "打印", "预览", "验证CA签名", "手工解锁", "删除", "病历参考", "更新数据", "加载全部病程", "个人模板管理", "返回", "腹部:", "视诊: 外形: 腹部外形正常", "腹围: 未测", "脐部: 正常", "胃形: 未见", "肠形: 未见", "蠕动波: 未见", "腹式呼吸: 正常", "腹壁静脉曲张: 无", "腹壁其它情况: 无", "触诊: 全腹柔软", "压痛反跳痛: 无压痛及反跳痛", "波动感: 无", "振水声: 无", "腹部包块: 腹部未触及包块", "肝脏: 肝脏肋下未触及", "胆囊: 未触及, Murphy征阴性", "脾脏: 脾脏肋下未触及", "肾脏: 未触及", "输尿管压痛点: 无压痛", "叩诊: 肝浊音界: 正常,", "肝上界位于锁骨中线, 第五肋间", "移动性浊音: 阴性,", "肾区叩痛: 无", "听诊: 肠鸣音无明显增强或减弱, 未闻及血管杂音", "肛门直肠: 未查", "生殖器: 未查", "脊柱四肢:", "脊柱外形: 脊柱正常生理弯曲"]
2026-08-07 04:43:33,112 INFO     29 [qwen-vl-parser] page=5 text: 44 lines (bbox 939-982)
2026-08-07 04:43:33,112 INFO     29 [qwen-vl-parser] page=5 text: 44 sections
2026-08-07 04:43:33,785 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3572570, prompt_len=764
2026-08-07 04:43:35,689 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-07 04:43:35,690 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-07 04:43:35,706 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3572570, prompt_len=401
2026-08-07 04:43:38,864 INFO     29 [qwen-vl-parser] text API response (len=389):
["70 四 肢：四肢无畸形，未见杵状指（趾），未见静脉曲张，双下肢无凹陷性水肿", "关 节：各关节未见异常，活动无受限", "肌 肉：未见肌肉萎缩，肌张力正常。四肢肌力5级。", "神经系统：", "浅反射：双侧浅反射正常引出", "深反射：双侧深反射正常引出", "病理反射：未引出", "脑膜刺激征：阴性", "专科情况", "神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下肢无凹陷性水肿。", "实验室及器械检查结果", "(2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm", "，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋巴结彩超", "：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。"]
2026-08-07 04:43:38,867 INFO     29 [qwen-vl-parser] page=6 text: 14 lines (bbox 983-996)
2026-08-07 04:43:38,867 INFO     29 [qwen-vl-parser] page=6 text: 14 sections
2026-08-07 04:43:39,657 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4796920, prompt_len=764
2026-08-07 04:43:43,590 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-02-28"}
```
2026-08-07 04:43:43,591 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=2026-02-28
2026-08-07 04:43:43,607 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4796920, prompt_len=401
2026-08-07 04:43:50,731 INFO     29 [qwen-vl-parser] text API response (len=964):
["2026-02-28 18:30", "男，因“咳嗽、咳痰1月余”于2026-02-28 15:23入非急诊步行入科。", "病例特点如下：1、老年期男性，起病缓，病程短。2、患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，", "伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。3、既往史：平素", "健康状况：良好。既往病史：否认高血压、冠心病、糖尿病史。传染病史：否，否认肝炎、结核或其他传染病史。预", "防接种史：正规。过敏史：否认过敏史。外伤史：否认外伤史。手术史：2年前曾行尿道结石手术，具体不详。输血", "史：否认输血史。系统回顾：无特殊。否认新冠肺炎流行病接触史。4、查体：T：36.8℃，P：75次/分，R：21次/分", "，BP：138/72mmHg。神志清楚，正常面容，皮肤巩膜无黄染，全身浅表淋巴结未扪及肿大，颈静脉无怒张。胸廓对称", "无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常，双肺叩诊呈清音，双肺呼吸音", "清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音。心界不大，心率75次/分，心律齐，各瓣膜区未闻及杂音。腹", "部外形正常，全腹柔软，无压痛及反跳痛，腹部未触及包块，肝脏肋下未触及，脾脏肋下未触及。移动性浊音阴性。", "双下肢无凹陷性水肿。浅反射：双侧浅反射正常引出。深反射：双侧深反射正常引出。病理反射：未引出。脑膜刺激", "征：阴性5、专科情况：神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下", "肢无凹陷性水肿。6、辅助检查：（2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组", "织肿块，最大截断面约77mm*60mm，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧", "胸膜肥厚、钙化。浅表淋巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。", "初步诊断：1.肺部阴影", "2.细菌性肺炎", "诊断依据：1.老年男性，起步缓，病程短", "2.咳嗽，咳淡黄色粘液痰", "3.外院胸部CT提示右肺下叶后基底段软组织肿块", "鉴别诊断。", "1.肺结核球"]
2026-08-07 04:43:50,731 INFO     29 [qwen-vl-parser] page=7 text: 23 lines (bbox 997-1019)
2026-08-07 04:43:50,732 INFO     29 [qwen-vl-parser] page=7 text: 23 sections
2026-08-07 04:43:51,615 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4914358, prompt_len=764
2026-08-07 04:43:53,704 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:43:53.702+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:43:55,134 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-07 04:43:55,136 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-07 04:43:55,156 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4914358, prompt_len=401
2026-08-07 04:44:01,353 INFO     29 [qwen-vl-parser] text API response (len=905):
["编辑", "功能", "表格", "签名", "其他", "打印", "预览", "验证CA签名", "手工解锁", "删除", "病历参考", "更新数据", "加载全部病程", "个人模板管理", "返回", "鉴别诊断：", "1.肺结核球：多见于年轻患者，病灶多见于结核好发部位，如肺上叶尖后段和下叶背段，直径一般<3", "cm。一般无症状，病灶边界清楚，密度高，可有包膜。有时含钙化点，周围有卫星灶。", "2.急性粟粒性肺结核：应与弥漫型细支气管肺泡癌相鉴别。通常粟粒型肺结核患者年龄较轻，有发热", "，盗汗等全身中毒症状，呼吸道症状不明显。x线表现为细小、分布均匀、密度较淡的粟粒样结节病灶。", "而细支气管—肺泡细胞癌两肺多有大小不等的结节状播散病灶，边界清楚、密度较高，进行性发展和增大", "，且有进行性呼吸困难。", "3.肺炎：若无毒性症状，抗生素治疗后肺部阴影吸收缓慢，或同一部位反复发生肺炎时，应考虑到肺", "癌可能。肺部慢性炎症机化，形成团块状的炎性假瘤，也易与肺癌相混淆。但炎性假瘤往往形态不整，边", "缘不齐，核心密度较高，易伴有胸膜增厚，病灶长期无明显变化。", "4.肺脓肿：起病急，中毒症状严重，多有寒战、高热、咳嗽、咳大量脓臭痰等症状。肺部x线表现为", "均匀的大片状炎性阴影，空洞内常见较深液平。结合纤支镜检查和痰脱落细胞检查可以鉴别。", "5.纵隔淋巴瘤：颇似中央型肺癌，常为双侧性，可有发热等全身症状，需病理诊断。", "VTE血栓风险评估：创建时间:2026-02-28 15:37:11,评估节点:入院,量表名称:Padua评分,分数:0,评分描述:低危,", "预防措施:undefined", "VTE出血风险评估：创建时间:2026-02-28 18:35:54,评估节点:入院,量表名称:内科出血风险评估,分数:1,评分描述：", "低危,预防措施:undefined", "诊疗计划：1.内科护理常规,II级护理。", "2.完善必要辅助检查如血肿瘤标志物、痰液化验、胸部增强CT、支气管镜检查或浅表淋巴结及肺穿刺活检", ""]
2026-08-07 04:44:01,355 INFO     29 [qwen-vl-parser] page=8 text: 34 lines (bbox 1020-1053)
2026-08-07 04:44:01,355 INFO     29 [qwen-vl-parser] page=8 text: 34 sections
2026-08-07 04:44:02,087 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5287322, prompt_len=764
2026-08-07 04:44:03,961 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-07 04:44:03,963 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-07 04:44:03,994 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5287322, prompt_len=401
2026-08-07 04:44:06,017 INFO     29 [qwen-vl-parser] text API response (len=128):
["以确诊，必要时行颅脑MRI、腹部超声、骨扫描或PET-CT等检查以利进一步疾病诊治。", "3.给予吸氧、抗感染及止血、镇痛等对症支持治疗；明确病理类型拟定下一步治疗方案。", "是否需手术治疗：否", "医师签名：姜晓红 住院医师：孙超群", ""]
2026-08-07 04:44:06,018 INFO     29 [qwen-vl-parser] page=9 text: 4 lines (bbox 1054-1057)
2026-08-07 04:44:06,018 INFO     29 [qwen-vl-parser] page=9 text: 4 sections
2026-08-07 04:44:06,594 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3019472, prompt_len=764
2026-08-07 04:44:07,413 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-03-16"}
```
2026-08-07 04:44:07,413 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=2026-03-16
2026-08-07 04:44:07,425 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3019472, prompt_len=401
2026-08-07 04:44:11,174 INFO     29 [qwen-vl-parser] text API response (len=551):
["影像检查报告单", "病人 ID:", "姓名:", "性别: 男", "年龄: 67岁", "申请科室: 老年医学呼吸内科", "机器型号: SE-MR4", "住院号", "检查部位: 颅脑颅脑MR平扫及增强+DWI,*钆特酸葡胺注射液【广西HR】", "检查日期: 2026-03-13", "(此报告仅供临床医师诊断参考,不作为疾病证明)", "检查所见:", "左侧基底节区、两侧放射冠、右侧侧脑室前后角旁见小斑片状、斑点状等T1、稍", "长T2信号灶,FLAIR呈高信号,边界欠清,DWI未见弥散受限;余脑实质信号未见异", "常,DWI未见明确弥散受限区,增强扫描未见异常强化灶;静脉窦强化充盈良好,未", "见异常;各脑室及脑沟、裂、池对称性轻度增宽;中线结构无移位。", "诊断意见:", "脑白质病变--改良Fasekas1级;轻度脑萎缩。", "检查技师: 唐成", "报告医师: 郭仟", "审核医师: 张", "报告日期: 2026-03-16 15:13:19", "审核日期: 2026-03-16 18:28:39", "地址: 广西医科大学第一附属医院放射科", "联系电话: 0771-5356934", "“广西HR”解释: 广西影像检查项目互认", ""]
2026-08-07 04:44:11,175 INFO     29 [qwen-vl-parser] page=10 text: 26 lines (bbox 1058-1083)
2026-08-07 04:44:11,175 INFO     29 [qwen-vl-parser] page=10 text: 26 sections
2026-08-07 04:44:11,857 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3431852, prompt_len=764
2026-08-07 04:44:14,266 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-03-10"}
```
2026-08-07 04:44:14,268 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=2026-03-10
2026-08-07 04:44:14,284 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3431852, prompt_len=401
2026-08-07 04:44:17,436 INFO     29 [qwen-vl-parser] text API response (len=292):
["科", "检查部位：全身骨显像 显像剂：99mTc-MDP 临床诊断：1.肺占位性病变,2.细菌性肺炎,3.肺", "剂量：25mCi 部阴影", "（此报告仅供临床医师诊断参考，不作为疾病证明）", "检查所见：", "静脉注射99mTc-MDP 3小时后行全身骨显像前位、后位各1帧：", "全身骨像完整、显影基本清晰。颅骨、胸骨、椎体、肩胛骨、肋骨、骨盆及四肢骨显像剂分", "布未见明显异常改变。", "双肾显影，膀胱部分充盈。", "诊断意见：", "全身骨显像未见明显异常改变。", "报告医师：巫殷豪", "审核医师：彭盛梅", "报告日期：2026-03-10"]
2026-08-07 04:44:17,437 INFO     29 [qwen-vl-parser] page=11 text: 14 lines (bbox 1084-1097)
2026-08-07 04:44:17,437 INFO     29 [qwen-vl-parser] page=11 text: 14 sections
2026-08-07 04:44:18,225 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4396640, prompt_len=764
2026-08-07 04:44:20,580 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-03-11"}
```
2026-08-07 04:44:20,582 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=2026-03-11
2026-08-07 04:44:20,607 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4396640, prompt_len=401
2026-08-07 04:44:23,534 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:44:23.533+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:44:26,129 INFO     29 [qwen-vl-parser] text API response (len=749):
["广西医科大学第一附属医院", "影像检查报告单", "病人ID:", "姓名:", "性别: 男", "年龄: 67岁", "申请科室:", "机器型号: SE-", "床号: 49床", "住院号: 1959", "Force-2", "检查部位: 下腹部,上腹部CT平扫+增强,(新)碘帕醇注射液", "【广西HR】", "检查日期: 2026-03-11", "(此报告仅供临床医师诊断参考,不作为疾病证明)", "检查所见:", "双侧肾上腺见多个结节状稍低/低密度影,较大者大小约1.6cm×1.2cm,增强扫", "描不均匀强化。肝脏各叶比例正常,肝实质内见多发类圆形低密度无强化灶,较大者", "位于S8,大小约1.2cm×1.1cm;余肝实质未见异常密度影及异常强化灶。肝内、外胆", "管未见扩张,胆囊不大,囊壁均匀,囊内密度未见异常。脾脏、胰腺形态、大小、密", "度未见异常,增强扫描未见异常强化,右肾体积缩小,双肾实质内见多个类圆形低密", "度无强化灶,较大者大小约0.9cm×1.5cm;双侧肾盂肾盏及输尿管未见扩张。腹部肠", "管分布正常,管腔未见扩张、积液,腹腔内未见明确肿块影;肝门及腹主动脉旁未见", "增大淋巴结,腹膜腔未见积液。", "诊断意见:", "1.双侧肾上腺占位,考虑转移瘤可能性大,请结合临床;", "2.肝多发囊肿;", "3.右肾萎缩,双肾囊肿。", "检查技师:刘辰民 报告医师:谢金桓 审核医师: 冯涛", "报告日期:2026-03-11 14:21:30 审核日期:2026-03-11 16:15:45", "地址:广西医科大学第一附属医院放射科 联系电话:0771-5356934 “广西HR”解释:广西影像检查项目互认"]
2026-08-07 04:44:26,130 INFO     29 [qwen-vl-parser] page=12 text: 31 lines (bbox 1098-1128)
2026-08-07 04:44:26,130 INFO     29 [qwen-vl-parser] page=12 text: 31 sections
2026-08-07 04:44:26,819 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3306564, prompt_len=764
2026-08-07 04:44:28,637 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-03-02"}
```
2026-08-07 04:44:28,638 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=2026-03-02
2026-08-07 04:44:28,651 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3306564, prompt_len=401
2026-08-07 04:44:34,698 INFO     29 [qwen-vl-parser] text API response (len=876):
["广西医科大学第一附属医院", "影像检查报告单", "病人ID:", "姓名:", "男", "年龄: 67岁", "申请科室: 老年医学呼吸内科", "机器型号: SE-", "Force-2", "床号", "号", "检查部位: 胸部CT平扫+增强,*碘海醇注射液【广西HR】", "检查日期: 2026-03-02", "(此报告仅供临床医师诊断参考,不作为疾病证明)", "检查所见:", "两肺尖胸膜下见类圆形透亮影,较大者长径约0.8cm;右肺下叶基底段(Se4:IM144)见团", "块状密度增高灶,大小约为7.7cm×5.1cm×6.9cm,增强扫描中度强化;两肺可见多发实性结节", "影,较大位于右肺下叶外基底段(Se4:IM344),内可见空泡,长径约为1.1cm,增强扫描似见", "血管穿行。右肺中叶、左肺上叶下舌段及两肺下叶见条索状密度增高影;余肺叶内未见异常密", "度影及异常强化灶,右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张,两肺部分支气管", "管壁增厚,管腔变窄,气管、其余支气管通畅;肺门、纵隔结构清楚,纵隔、两侧肺门见多发", "淋巴结,大者短径约1.1cm。两侧胸膜增厚、钙化,胸膜腔未见积液。主动脉、冠状动脉见斑片", "状钙化灶。", "诊断意见:", "1.右肺下叶后基底段软组织肿块,肿瘤性病变?感染性病变?请结合临床及实验室检查;", "2.两肺多发实性结节,建议短期复查;", "3.右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张并两肺炎症;", "4.两肺上叶间隔旁型肺气肿;", "5.纵隔、两侧肺门淋巴结,建议复查;", "6.两侧胸膜肥厚、钙化;", "7.主动脉、冠状动脉硬化。", "检查技师:周春燚 报告医师:肖芳艳 审核医师:", "报告日期:2026-03-03 18:39:05 审核日期:2026-03-04 09:21:01", "地址:广西医科大学第一附属医院放射科 联系电话:0771-5356934 “广西HR”解码:广西影像检查项目互认", ""]
2026-08-07 04:44:34,700 INFO     29 [qwen-vl-parser] page=13 text: 34 lines (bbox 1129-1162)
2026-08-07 04:44:34,701 INFO     29 [qwen-vl-parser] page=13 text: 34 sections
2026-08-07 04:44:35,314 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5122646, prompt_len=764
2026-08-07 04:44:37,451 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-03-02"}
```
2026-08-07 04:44:37,451 INFO     29 [qwen-vl-parser] page=14 classify=text report_date=2026-03-02
2026-08-07 04:44:37,479 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5122646, prompt_len=401
2026-08-07 04:44:43,938 INFO     29 [qwen-vl-parser] text API response (len=864):
["测量参数值:", "测量项目", "结果", "单位", "参考范围", "测量项目", "结果", "单位", "参考范围", "主动脉根部内径:", "27", "mm", "(20-35)", "左房前后径:", "35", "mm", "(24-39)", "左室舒末前后径:", "53", "mm", "(38-54)", "左室缩末前后径:", "32", "mm", "(24-37)", "室间隔舒末厚:", "10", "mm", "(6-11)", "左室后壁舒末厚:", "10", "mm", "(6-11)", "右室舒末前后径:", "18", "mm", "(15-30)", "右室流出道:", "27", "mm", "(15-32)", "主肺动脉内径:", "22", "mm", "(15-26)", "E/A", "<1", "(0.8-2.0)", "e'/a'", "<1", "(->)", "E/e'", "11.7", "(->)", "超声描述:", "描述:", "1、按比例各房室大小正常，房、室间隔连续完整，室间隔与左室壁厚度正常，静息状态下室壁收", "缩运动有力，未见节段性运动异常。左室收缩功能测定在正常范围，FS:40%，EF:70%，SV:95ml/B", "，CO:6.4L/min，EDV:135ml，心包腔内未探及液性区声像。", "2、三尖瓣形态结构正常，瓣口轻度反流，速度2.4m/s，压差22mmHg，瞬时反流量约2ml（无血流动", "力学意义），余各瓣膜形态结构正常，启闭运动好，二尖瓣血流图示E峰小于A峰。", "3、主动脉根部内径正常，升主动脉内径正常，管壁增厚，弹性降低，主肺动脉内径正常，内回声", "及血流信号未见异常。", "超声诊断:", "1、心脏形态结构及瓣膜功能大致正常。", "2、左室舒张功能降低，收缩功能测定在正常范围，", "诊断医师：吴颖/肖彩意", "报告日期：2026-03-02 10:12:46"]
2026-08-07 04:44:43,939 INFO     29 [qwen-vl-parser] page=14 text: 68 lines (bbox 1163-1230)
2026-08-07 04:44:43,939 INFO     29 [qwen-vl-parser] page=14 text: 68 sections
2026-08-07 04:44:44,561 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2321993, prompt_len=764
2026-08-07 04:44:46,108 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2026-02-28"}
```
2026-08-07 04:44:46,108 INFO     29 [qwen-vl-parser] page=15 classify=table report_date=2026-02-28
2026-08-07 04:44:46,125 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2321993, prompt_len=756
2026-08-07 04:44:47,684 INFO     29 [qwen-vl-parser] table API response (len=191):
\begin{tabular}{ccccccccc}
\hline
缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\
\hline
TB-DNA & 结核杆菌DNA* & $<$5.00E+02 & & & & 拷贝 & $<$5.00E+02 & $<$5.00E+02 \\
\hline
\end{tabular}
2026-08-07 04:44:47,687 INFO     29 [qwen-vl-parser] page=15 table: 8 LaTeX lines (bbox 1231-1238)
2026-08-07 04:44:47,687 INFO     29 [qwen-vl-parser] page=15 table: 8 sections
2026-08-07 04:44:48,327 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3750809, prompt_len=764
2026-08-07 04:44:50,191 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2026-02-28"}
```
2026-08-07 04:44:50,193 INFO     29 [qwen-vl-parser] page=16 classify=table report_date=2026-02-28
2026-08-07 04:44:50,220 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3750809, prompt_len=756
2026-08-07 04:44:52,826 INFO     29 [qwen-vl-parser] table API response (len=348):
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
2026-08-07 04:44:52,827 INFO     29 [qwen-vl-parser] page=16 table: 12 LaTeX lines (bbox 1239-1250)
2026-08-07 04:44:52,827 INFO     29 [qwen-vl-parser] page=16 table: 12 sections
2026-08-07 04:44:53,432 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:44:53.432+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:44:53,476 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3532896, prompt_len=764
2026-08-07 04:44:54,488 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2026-02-28"}
```
2026-08-07 04:44:54,489 INFO     29 [qwen-vl-parser] page=17 classify=table report_date=2026-02-28
2026-08-07 04:44:54,506 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3532896, prompt_len=756
2026-08-07 04:44:56,810 INFO     29 [qwen-vl-parser] table API response (len=295):
\begin{tabular}{lllllllll}
\hline
& 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\
\hline
& 丙型肝炎抗体定量* & 0.06 & & & & COI & 0-1 & \\
ST & 不加热血清反应素试验* & 阴性(-) & & & & & 阴性(-) & \\
V & 人免疫缺陷病毒抗体定量* & 0.08 & & & & COI & 0-1 & \\
PA & 梅毒螺旋体抗体定量* & 0.08 & & & & COI & 0-1 & \\
\hline
\end{tabular}
2026-08-07 04:44:56,811 INFO     29 [qwen-vl-parser] page=17 table: 11 LaTeX lines (bbox 1251-1261)
2026-08-07 04:44:56,811 INFO     29 [qwen-vl-parser] page=17 table: 11 sections
2026-08-07 04:44:57,440 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3260841, prompt_len=764
2026-08-07 04:44:58,361 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2026-02-28"}
```
2026-08-07 04:44:58,362 INFO     29 [qwen-vl-parser] page=18 classify=table report_date=2026-02-28
2026-08-07 04:44:58,376 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3260841, prompt_len=756
2026-08-07 04:45:00,841 INFO     29 [qwen-vl-parser] table API response (len=260):
\begin{tabular}{ccccccccc}
\hline
项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\
\hline
糖化血红蛋白HbA1c* & 6.40 & & $\uparrow$ & & \% & 4.0-6.0 & \\
糖化血红蛋白HbA1a & 0.50 & & & & \% & 0-0.91 & \\
糖化血红蛋白HbA1b & 1.10 & & & & \% & 0.35-1.82 & \\
\hline
\end{tabular}
2026-08-07 04:45:00,844 INFO     29 [qwen-vl-parser] page=18 table: 10 LaTeX lines (bbox 1262-1271)
2026-08-07 04:45:00,844 INFO     29 [qwen-vl-parser] page=18 table: 10 sections
2026-08-07 04:45:01,437 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3468749, prompt_len=764
2026-08-07 04:45:04,658 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2026-02-28"}
```
2026-08-07 04:45:04,659 INFO     29 [qwen-vl-parser] page=19 classify=table report_date=2026-02-28
2026-08-07 04:45:04,674 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3468749, prompt_len=756
2026-08-07 04:45:07,160 INFO     29 [qwen-vl-parser] table API response (len=409):
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
2026-08-07 04:45:07,162 INFO     29 [qwen-vl-parser] page=19 table: 14 LaTeX lines (bbox 1272-1285)
2026-08-07 04:45:07,162 INFO     29 [qwen-vl-parser] page=19 table: 14 sections
2026-08-07 04:45:07,845 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3985539, prompt_len=764
2026-08-07 04:45:09,357 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2026-02-02"}
```
2026-08-07 04:45:09,358 INFO     29 [qwen-vl-parser] page=20 classify=table report_date=2026-02-02
2026-08-07 04:45:09,383 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3985539, prompt_len=756
2026-08-07 04:45:15,776 INFO     29 [qwen-vl-parser] table API response (len=1170):
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
2026-08-07 04:45:15,778 INFO     29 [qwen-vl-parser] page=20 table: 28 LaTeX lines (bbox 1286-1313)
2026-08-07 04:45:15,778 INFO     29 [qwen-vl-parser] page=20 table: 28 sections
2026-08-07 04:45:16,604 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4020865, prompt_len=764
2026-08-07 04:45:18,310 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2025-04-01"}
```
2026-08-07 04:45:18,310 INFO     29 [qwen-vl-parser] page=21 classify=table report_date=2025-04-01
2026-08-07 04:45:18,330 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4020865, prompt_len=756
2026-08-07 04:45:23,046 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:45:23.044+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:45:25,258 INFO     29 [qwen-vl-parser] table API response (len=1138):
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
2026-08-07 04:45:25,259 INFO     29 [qwen-vl-parser] page=21 table: 27 LaTeX lines (bbox 1314-1340)
2026-08-07 04:45:25,260 INFO     29 [qwen-vl-parser] page=21 table: 27 sections
2026-08-07 04:45:26,088 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4026758, prompt_len=764
2026-08-07 04:45:27,564 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-07 04:45:27,564 INFO     29 [qwen-vl-parser] page=22 classify=table report_date=None
2026-08-07 04:45:27,578 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4026758, prompt_len=756
2026-08-07 04:45:34,425 INFO     29 [qwen-vl-parser] table API response (len=1136):
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
2026-08-07 04:45:34,428 INFO     29 [qwen-vl-parser] page=22 table: 26 LaTeX lines (bbox 1341-1366)
2026-08-07 04:45:34,428 INFO     29 [qwen-vl-parser] page=22 table: 26 sections
2026-08-07 04:45:35,156 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4115824, prompt_len=764
2026-08-07 04:45:43,629 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-07 04:45:43,630 INFO     29 [qwen-vl-parser] page=23 classify=table report_date=None
2026-08-07 04:45:43,651 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4115824, prompt_len=756
2026-08-07 04:45:50,991 INFO     29 [qwen-vl-parser] table API response (len=1366):
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
2026-08-07 04:45:50,994 INFO     29 [qwen-vl-parser] page=23 table: 27 LaTeX lines (bbox 1367-1393)
2026-08-07 04:45:50,995 INFO     29 [qwen-vl-parser] page=23 table: 27 sections
2026-08-07 04:45:51,744 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4168304, prompt_len=764
2026-08-07 04:45:52,833 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:45:52.832+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:45:53,632 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-07 04:45:53,635 INFO     29 [qwen-vl-parser] page=24 classify=table report_date=None
2026-08-07 04:45:53,664 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4168304, prompt_len=756
2026-08-07 04:46:00,214 INFO     29 [qwen-vl-parser] table API response (len=1157):
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
2026-08-07 04:46:00,218 INFO     29 [qwen-vl-parser] page=24 table: 27 LaTeX lines (bbox 1394-1420)
2026-08-07 04:46:00,219 INFO     29 [qwen-vl-parser] page=24 table: 27 sections
2026-08-07 04:46:00,444 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1101847, prompt_len=764
2026-08-07 04:46:01,240 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-03-16"
}
```
2026-08-07 04:46:01,241 INFO     29 [qwen-vl-parser] page=25 classify=text report_date=2026-03-16
2026-08-07 04:46:01,255 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1101847, prompt_len=401
2026-08-07 04:46:06,900 INFO     29 [qwen-vl-parser] text API response (len=1195):
["临床诊断：肺癌", "样本采集时间：2026-03-10", "检测项目", "本产品对与肺癌密切相关的68个基因进行高通量测序。检测突变形式为点突变(SNV)、小片段插入缺失(INDEL)、拷贝数变异(CNV)以及融合(FUSION)。通过免疫组化检测PD-L1表达。", "本报告分析基因变异与靶向药物、化疗药物的相关性，给出靶向药物(FDA/NMPA批准药物、临床试验", "药物等)、化疗药物的用药提示信息，从而为临床制定治疗方案提供参考信息。", "注：检测基因列表见附录。", "检测结果小结", "检测类型", "检测结果", "靶向用药指导", "共检出3个变异位点,其中3个与靶向药物相关(KRAS", "p.G12V;CDKN2A p.R80*;TP53 p.G279E)", "PD-L1蛋白表达水平", "使用CSTE1L3N抗体;TPS:<1%, CPS:1", "化疗药物检测", "详见“化疗药物检测解析”部分", "样品总体质量评估", "合格", "注:", "1. 本报告为基因检测结果,基因、药物等信息列举未按照重要性排序。", "2. 本报告只对本次采集样本负责,如有疑问,请在7个工作日内与我们联系。", "检测人:", "张紫叶", "复核人:", "王建丽", "日期:", "2026-03-16", "日期:", "2026-03-16", "1/26", "孔令祈 Novogene", "诺禾致源", "肺癌精准诊疗相关基因结果汇总", "基因", "变异类型", "检测结果", "变异丰度/拷贝数", "ALK", "突变/融合", "未检测到与用药相关突变", "-", "BRAF", "突变/融合", "未检测到与用药相关突变", "-", "BRCA1", "突变/缺失", "未检测到与用药相关突变", "-", "BRCA2", "突变/缺失", "未检测到与用药相关突变", "-", "EGFR", "突变", "未检测到与用药相关突变", "-", "ERBB2(HER2)", "突变/扩增", "未检测到与用药相关突变", "-", "FGFR2", "突变/融合", "未检测到与用药相关突变", "-", "FGFR3", "突变/融合", "未检测到与用药相关突变", "-", "KIT", "突变", "未检测到与用药相关突变", "-", "KRAS", "突变", "NM_033360.4 exon2 c.35G>T p.G12V", "35.80%", "MET", "突变/扩增/14号外", "未检测到与用药相关突变", "-", "显子跳跃", "NRG1", "融合", "未检测到与用药相关突变", "-", "NTRK1", "融合", "未检测到与用药相关突变", "-"]
2026-08-07 04:46:06,901 INFO     29 [qwen-vl-parser] page=25 text: 79 lines (bbox 1421-1499)
2026-08-07 04:46:06,901 INFO     29 [qwen-vl-parser] page=25 text: 79 sections
2026-08-07 04:46:07,101 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1246411, prompt_len=764
2026-08-07 04:46:07,941 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-03-10"
}
```
2026-08-07 04:46:07,941 INFO     29 [qwen-vl-parser] page=26 classify=text report_date=2026-03-10
2026-08-07 04:46:07,951 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1246411, prompt_len=401
2026-08-07 04:46:12,668 INFO     29 [qwen-vl-parser] text API response (len=888):
["广西金域医学检验实验室", "本报告单经过电子签名认证", "Guangxi Kingmed Center for Clinical Laboratory", "金域医学", "KingMed Diagnostics", "病理诊断报告书", "1/1", "标本条码", "1223023095", "医院", "广西医科大学第一附属医院", "病人姓名", "孔令祈", "科室", "老年呼吸", "病理号", "26018339", "性别", "男", "房/床号", "49", "住院门诊号", "1959880", "年龄", "67岁", "接收时间", "2026-03-08 14:15:50", "申请医生", "", "项目名称", "免疫组化8项", "送检材料", "肺组织", "临床诊断", "", "患者电话", "", "大体描述:", "福尔马林固定标本，核对送检标本、病人姓名和条形码与申请单一致。", "灰红条索状组织3段，长0.5-1.8cm，直径均0.05cm。取1盒全（共1盒蜡块）", "镜下所见：", "诊断意见：", "肺组织穿刺活检：", "-结合免疫组化，符合浸润性黏液型腺癌，请结合临床。", "-免疫组化：CK7（+），CK20（+），Villin（+），TTF-1（散在+），NapsinA（散在+），P40（-），CDX2（-），Ki67（", "热点区约60%+）。", "报告医师：陈明坚", "本检测仅对送检负责，如果对结果有疑义，请在报告发布后7天内与我们联系，多谢合作！", "收样点：广西医科大学第一附属医院-呼吸内", "科", "主检实验室：广西金域", "地址：南宁市西乡塘区总部路3号中国-东盟科技企业孵化基地二期1号厂房一、三、", "四层", "报告专用章", "网址：www.kingmed.com.cn", "GX003SCEJL7RJLY", "报告日期：2026-03-10 21:16:16", "更多报告服务", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-07 04:46:12,669 INFO     29 [qwen-vl-parser] page=26 text: 57 lines (bbox 1500-1556)
2026-08-07 04:46:12,669 INFO     29 [qwen-vl-parser] page=26 text: 57 sections
2026-08-07 04:46:12,669 INFO     29 [qwen-vl-parser] parse_pdf done: 1557 sections from 26 pages.
2026-08-07 04:46:12,685 INFO     29 Close text detector.
2026-08-07 04:46:13,263 INFO     29 Close text recognizer.
2026-08-07 04:46:13,719 INFO     29 Close recognizer.
2026-08-07 04:46:14,258 INFO     29 Close recognizer.
2026-08-07 04:46:15,288 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-07 04:46:15,289 INFO     29 [Trace] task=26a40982 | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Parser:MedLink | outputs={"html": "", "json": "1557 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "json"}
2026-08-07 04:46:15,289 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-07 04:46:15,312 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:46:15,312 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n⚠️ 住院病程文书归属：病程记录、查房记录、术前小结、术后首次病程记录等住院期间病程文书，与入院记录同属一次住院事件；当它们与入院记录页相邻时，必须合并为一个 AdmissionRecord 片段，不得单独成段、不得归入 DischargeRecord。\n- 病程文书识别特征：标题含\"病程记录\"/\"查房记录\"/\"术前小结\"/\"术后首次病程记录\"，带住院患者信息（科室/床号/住院号），有\"入院时间\"（如\"2020年07月08日 08:36:09入院\"），无\"出院诊断\"/\"出院医嘱\"\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。只有主诉，病史的也属于OutpatientRecord（门诊病历）\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 病史\n[BBOX-1] 主诉：咳嗽、咳痰1月余\n[BBOX-2] 现病史：患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、\n[BBOX-3] 呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。至当地医院体检发现肺部阴影，具体不详。2026-02-26至中\n[BBOX-4] 山大学附属第一医院广西医院就诊，查胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm\n[BBOX-5] ，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋\n[BBOX-6] 巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。具体诊治不详。为进一步治疗，遂\n[BBOX-7] 至我院门诊就诊，门诊拟“肺占位性病变”收治入院。自发病以来，患者精神、食欲、睡眠正常，大小便正\n[BBOX-8] 常，体重无明显变化。\n[BBOX-9] 既往史：平素健康状况：良好。\n[BBOX-10] 既往病史：否认高血压、冠心病、糖尿病史。\n[BBOX-11] 传染病史：否，否认肝炎、结核或其他传染病史。\n[BBOX-12] 预防接种史：正规。\n[BBOX-13] 过敏史：否认过敏史。\n[BBOX-14] 外伤史：否认外伤史。\n[BBOX-15] 手术史：2年前曾行尿道结石手术，具体不详。\n[BBOX-16] 输血史：否认输血史。\n[BBOX-17] 系统回顾：无特殊。\n[BBOX-18] 个人史：出生地：广西壮族自治区南宁市青秀区\n[BBOX-19] 地方病地区居住情况：无\n[BBOX-20] 冶游史：否认冶游史\n[BBOX-21] 职业与工作条件有无工业毒物、粉尘、放射性物质及接触史：无\n[BBOX-22] 广西医科大学第一附属医院 孔令祈\n[BBOX-23] 11:24\n[BBOX-24] 2026-03-19\n[BBOX-25] 姜晓红 (D450199...\n[BBOX-26] 姜晓红 (D450199...\n[BBOX-27] CS 扫描全能王\n[BBOX-28] 3亿人都在用的扫描App\n[BBOX-29] 烟酒嗜好及药物使用史：有吸烟史，约10支/天，已吸烟40年，否认饮酒史。\n[BBOX-30] 婚姻史：有婚姻史，结婚年龄：适龄结婚。有生育史，育有1子。\n[BBOX-31] 家族史：否认相似家族病史及遗传病史。\n[BBOX-32] 请患者或病史叙述者仔细确认以上病史记录并签字：[患者]\n[BBOX-33] 体格检查\n[BBOX-34] 一般情况：\n[BBOX-35] 体温：36.8℃\n[BBOX-36] 脉搏：75次/分\n[BBOX-37] 呼吸：21次/分\n[BBOX-38] 血压：138/72mmHg\n[BBOX-39] 身高：161CM\n[BBOX-40] 体重：74kg\n[BBOX-41] 发育：正常\n[BBOX-42] 营养：良好\n[BBOX-43] 神志：清楚\n[BBOX-44] 体位：自主体位\n[BBOX-45] 面容：正常面容\n[BBOX-46] 表情：自如\n[BBOX-47] 步态：正常\n[BBOX-48] 体型：正力型\n[BBOX-49] 配合检查：合作\n[BBOX-50] 皮肤黏膜:\n[BBOX-51] 色泽: 正常\n[BBOX-52] 皮疹: 全身皮肤未见皮疹\n[BBOX-53] 皮下出血: 全身皮肤未见皮下出血\n[BBOX-54] 毛发分布: 毛发分布正常\n[BBOX-55] 温度与湿度: 温度、湿度、弹性均正常\n[BBOX-56] 水肿: 未见水肿\n[BBOX-57] 肝掌: 无\n[BBOX-58] 蜘蛛痣: 未见蜘蛛痣\n[BBOX-59] 其他表现: 无\n[BBOX-60] 淋巴结: 全身浅表淋巴结未扪及肿大\n[BBOX-61] 头部:\n[BBOX-62] 头颅: 头颅大小正常, 无畸形\n[BBOX-63] 眼: 眉毛, 眼睑, 结膜, 眼球未见异常, 双侧巩膜无黄染\n[BBOX-64] 耳: 双耳外观未见异常, 乳突无压痛, 外耳道未见分泌物\n[BBOX-65] 鼻: 鼻部外观未见异常, 鼻翼无扇动, 鼻腔无分泌物, 鼻窦区无压痛\n[BBOX-66] 咽喉: 双侧扁桃体未见肿大, 表面未见脓性分泌物, 咽未见异常, 声音正常\n[BBOX-67] 口腔: 唇, 舌, 牙齿, 牙龈正常\n[BBOX-68] 颈部:\n[BBOX-69] 颈部运动: 颈软无抵抗\n[BBOX-70] 颈静脉: 无怒张\n[BBOX-71] 气管: 居中\n[BBOX-72] 颈动脉搏动: 正常\n[BBOX-73] 肝-颈静脉回流征: 阴性\n[BBOX-74] 广西医科大:\n[BBOX-75] 预览 验证CA签名 手工解锁 删除 病历参考 更新数据 加载全部病程 个人模板管理 返回\n[BBOX-76] 20 部：\n[BBOX-77] 003470 20.2.11\n[BBOX-78] 003470 20.2.11\n[BBOX-79] 003470 20.2.11\n[BBOX-80] 003470 20.2.11\n[BBOX-81] 胸部：胸廓对称无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常\n[BBOX-82] 肺部：\n[BBOX-83] 视诊：双侧呼吸运动均匀对称，无增强或者减弱\n[BBOX-84] 触诊：双肺触觉语颤对称无异常，未触及胸膜摩擦感\n[BBOX-85] 叩诊：双肺叩诊呈清音\n[BBOX-86] 听诊：双肺呼吸音清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音\n[BBOX-87] 心脏：\n[BBOX-88] 视诊：心尖搏动未见异常，位于左侧第五肋间锁骨中线内0.5cm，无异常隆起及凹陷\n[BBOX-89] 触诊：心尖搏动未触及异常，未触及震颤及心包摩擦感\n[BBOX-90] 叩诊：心界不大\n[BBOX-91] 听诊：心率：75次/分，心律：齐 A2 > P2\n[BBOX-92] 心音 S1：有力， 心音 S2：有力， 心音 S3：无， 心音 S4：无\n[BBOX-93] 杂音：各瓣膜区未闻及杂音\n[BBOX-94] 额外心音：无\n[BBOX-95] 心包摩擦音：无\n[BBOX-96] 周围血管：未见异常血管征\n[BBOX-97] 003470 20.2.41.64\n[BBOX-98] 003470 20.2.41.64\n[BBOX-99] 003470 20.2.41.64\n[BBOX-100] 003470 20.2.41.64\n[BBOX-101] 003470 20.2.41.64\n[BBOX-102] 003470 20.2.41.64\n[BBOX-103] 003470 20.2.41.64\n[BBOX-104] 003470 20.2.41.64\n[BBOX-105] 003470 20.2.41.64\n[BBOX-106] 003470 20.2.41.64\n[BBOX-107] 003470 20.2.41.64\n[BBOX-108] 003470 20.2.41.64\n[BBOX-109] 003470 20.2.41.64\n[BBOX-110] 003470 20.2.41.64\n[BBOX-111] 003470 20.2.41.64\n[BBOX-112] 003470 20.2.41.64\n[BBOX-113] 003470 20.2.41.64\n[BBOX-114] 003470 20.2.41.64\n[BBOX-115] 003470 20.2.41.64\n[BBOX-116] 003470 20.2.41.64\n[BBOX-117] 003470 20.2.41.64\n[BBOX-118] 003470 20.2.41.64\n[BBOX-119] 003470 20.2.41.64\n[BBOX-120] 003470 20.2.41.64\n[BBOX-121] 003470 20.2.41.64\n[BBOX-122] 003470 20.2.41.64\n[BBOX-123] 003470 20.2.41.64\n[BBOX-124] 003470 20.2.41.64\n[BBOX-125] 003470 20.2.41.64\n[BBOX-126] 003470 20.2.41.64\n[BBOX-127] 003470 20.2.41.64\n[BBOX-128] 003470 20.2.41.64\n[BBOX-129] 003470 20.2.41.64\n[BBOX-130] 003470 20.2.41.64\n[BBOX-131] 003470 20.2.41.64\n[BBOX-132] 003470 20.2.41.64\n[BBOX-133] 003470 20.2.41.64\n[BBOX-134] 003470 20.2.41.64\n[BBOX-135] 003470 20.2.41.64\n[BBOX-136] 003470 20.2.41.64\n[BBOX-137] 003470 20.2.41.64\n[BBOX-138] 003470 20.2.41.64\n[BBOX-139] 003470 20.2.41.64\n[BBOX-140] 003470 20.2.41.64\n[BBOX-141] 003470 20.2.41.64\n[BBOX-142] 003470 20.2.41.64\n[BBOX-143] 003470 20.2.41.64\n[BBOX-144] 003470 20.2.41.64\n[BBOX-145] 003470 20.2.41.64\n[BBOX-146] 003470 20.2.41.64\n[BBOX-147] 003470 20.2.41.64\n[BBOX-148] 003470 20.2.41.64\n[BBOX-149] 003470 20.2.41.64\n[BBOX-150] 003470 20.2.41.64\n[BBOX-151] 003470 20.2.41.64\n[BBOX-152] 003470 20.2.41.64\n[BBOX-153] 003470 20.2.41.64\n[BBOX-154] 003470 20.2.41.64\n[BBOX-155] 003470 20.2.41.64\n[BBOX-156] 003470 20.2.41.64\n[BBOX-157] 003470 20.2.41.64\n[BBOX-158] 003470 20.2.41.64\n[BBOX-159] 003470 20.2.41.64\n[BBOX-160] 003470 20.2.41.64\n[BBOX-161] 003470 20.2.41.64\n[BBOX-162] 003470 20.2.41.64\n[BBOX-163] 003470 20.2.41.64\n[BBOX-164] 003470 20.2.41.64\n[BBOX-165] 003470 20.2.41.64\n[BBOX-166] 003470 20.2.41.64\n[BBOX-167] 003470 20.2.41.64\n[BBOX-168] 003470 20.2.41.64\n[BBOX-169] 003470 20.2.41.64\n[BBOX-170] 003470 20.2.41.64\n[BBOX-171] 003470 20.2.41.64\n[BBOX-172] 003470 20.2.41.64\n[BBOX-173] 003470 20.2.41.64\n[BBOX-174] 003470 20.2.41.64\n[BBOX-175] 003470 20.2.41.64\n[BBOX-176] 003470 20.2.41.64\n[BBOX-177] 003470 20.2.41.64\n[BBOX-178] 003470 20.2.41.64\n[BBOX-179] 003470 20.2.41.64\n[BBOX-180] 003470 20.2.41.64\n[BBOX-181] 003470 20.2.41.64\n[BBOX-182] 003470 20.2.41.64\n[BBOX-183] 003470 20.2.41.64\n[BBOX-184] 003470 20.2.41.64\n[BBOX-185] 003470 20.2.41.64\n[BBOX-186] 003470 20.2.41.64\n[BBOX-187] 003470 20.2.41.64\n[BBOX-188] 003470 20.2.41.64\n[BBOX-189] 003470 20.2.41.64\n[BBOX-190] 003470 20.2.41.64\n[BBOX-191] 003470 20.2.41.64\n[BBOX-192] 003470 20.2.41.64\n[BBOX-193] 003470 20.2.41.64\n[BBOX-194] 003470 20.2.41.64\n[BBOX-195] 003470 20.2.41.64\n[BBOX-196] 003470 20.2.41.64\n[BBOX-197] 003470 20.2.41.64\n[BBOX-198] 003470 20.2.41.64\n[BBOX-199] 003470 20.2.41.64\n[BBOX-200] 003470 20.2.41.64\n[BBOX-201] 003470 20.2.41.64\n[BBOX-202] 003470 20.2.41.64\n[BBOX-203] 003470 20.2.41.64\n[BBOX-204] 003470 20.2.41.64\n[BBOX-205] 003470 20.2.41.64\n[BBOX-206] 003470 20.2.41.64\n[BBOX-207] 003470 20.2.41.64\n[BBOX-208] 003470 20.2.41.64\n[BBOX-209] 003470 20.2.41.64\n[BBOX-210] 003470 20.2.41.64\n[BBOX-211] 003470 20.2.41.64\n[BBOX-212] 003470 20.2.41.64\n[BBOX-213] 003470 20.2.41.64\n[BBOX-214] 003470 20.2.41.64\n[BBOX-215] 003470 20.2.41.64\n[BBOX-216] 003470 20.2.41.64\n[BBOX-217] 003470 20.2.41.64\n[BBOX-218] 003470 20.2.41.64\n[BBOX-219] 003470 20.2.41.64\n[BBOX-220] 003470 20.2.41.64\n[BBOX-221] 003470 20.2.41.64\n[BBOX-222] 003470 20.2.41.64\n[BBOX-223] 003470 20.2.41.64\n[BBOX-224] 003470 20.2.41.64\n[BBOX-225] 003470 20.2.41.64\n[BBOX-226] 003470 20.2.41.64\n[BBOX-227] 003470 20.2.41.64\n[BBOX-228] 003470 20.2.41.64\n[BBOX-229] 003470 20.2.41.64\n[BBOX-230] 003470 20.2.41.64\n[BBOX-231] 003470 20.2.41.64\n[BBOX-232] 003470 20.2.41.64\n[BBOX-233] 003470 20.2.41.64\n[BBOX-234] 003470 20.2.41.64\n[BBOX-235] 003470 20.2.41.64\n[BBOX-236] 003470 20.2.41.64\n[BBOX-237] 003470 20.2.41.64\n[BBOX-238] 003470 20.2.41.64\n[BBOX-239] 003470 20.2.41.64\n[BBOX-240] 003470 20.2.41.64\n[BBOX-241] 003470 20.2.41.64\n[BBOX-242] 003470 20.2.41.64\n[BBOX-243] 003470 20.2.41.64\n[BBOX-244] 003470 20.2.41.64\n[BBOX-245] 003470 20.2.41.64\n[BBOX-246] 003470 20.2.41.64\n[BBOX-247] 003470 20.2.41.64\n[BBOX-248] 003470 20.2.41.64\n[BBOX-249] 003470 20.2.41.64\n[BBOX-250] 003470 20.2.41.64\n[BBOX-251] 003470 20.2.41.64\n[BBOX-252] 003470 20.2.41.64\n[BBOX-253] 003470 20.2.41.64\n[BBOX-254] 003470 20.2.41.64\n[BBOX-255] 003470 20.2.41.64\n[BBOX-256] 003470 20.2.41.64\n[BBOX-257] 003470 20.2.41.64\n[BBOX-258] 003470 20.2.41.64\n[BBOX-259] 003470 20.2.41.64\n[BBOX-260] 003470 20.2.41.64\n[BBOX-261] 003470 20.2.41.64\n[BBOX-262] 003470 20.2.41.64\n[BBOX-263] 003470 20.2.41.64\n[BBOX-264] 003470 20.2.41.64\n[BBOX-265] 003470 20.2.41.64\n[BBOX-266] 003470 20.2.41.64\n[BBOX-267] 003470 20.2.41.64\n[BBOX-268] 003470 20.2.41.64\n[BBOX-269] 003470 20.2.41.64\n[BBOX-270] 003470 20.2.41.64\n[BBOX-271] 003470 20.2.41.64\n[BBOX-272] 003470 20.2.41.64\n[BBOX-273] 003470 20.2.41.64\n[BBOX-274] 003470 20.2.41.64\n[BBOX-275] 003470 20.2.41.64\n[BBOX-276] 003470 20.2.41.64\n[BBOX-277] 003470 20.2.41.64\n[BBOX-278] 003470 20.2.41.64\n[BBOX-279] 003470 20.2.41.64\n[BBOX-280] 003470 20.2.41.64\n[BBOX-281] 003470 20.2.41.64\n[BBOX-282] 003470 20.2.41.64\n[BBOX-283] 003470 20.2.41.64\n[BBOX-284] 003470 20.2.41.64\n[BBOX-285] 003470 20.2.41.64\n[BBOX-286] 003470 20.2.41.64\n[BBOX-287] 003470 20.2.41.64\n[BBOX-288] 003470 20.2.41.64\n[BBOX-289] 003470 20.2.41.64\n[BBOX-290] 003470 20.2.41.64\n[BBOX-291] 003470 20.2.41.64\n[BBOX-292] 003470 20.2.41.64\n[BBOX-293] 003470 20.2.41.64\n[BBOX-294] 003470 20.2.41.64\n[BBOX-295] 003470 20.2.41.64\n[BBOX-296] 003470 20.2.41.64\n[BBOX-297] 003470 20.2.41.64\n[BBOX-298] 003470 20.2.41.64\n[BBOX-299] 003470 20.2.41.64\n[BBOX-300] 003470 20.2.41.64\n[BBOX-301] 003470 20.2.41.64\n[BBOX-302] 003470 20.2.41.64\n[BBOX-303] 003470 20.2.41.64\n[BBOX-304] 003470 20.2.41.64\n[BBOX-305] 003470 20.2.41.64\n[BBOX-306] 003470 20.2.41.64\n[BBOX-307] 003470 20.2.41.64\n[BBOX-308] 003470 20.2.41.64\n[BBOX-309] 003470 20.2.41.64\n[BBOX-310] 003470 20.2.41.64\n[BBOX-311] 003470 20.2.41.64\n[BBOX-312] 003470 20.2.41.64\n[BBOX-313] 003470 20.2.41.64\n[BBOX-314] 003470 20.2.41.64\n[BBOX-315] 003470 20.2.41.64\n[BBOX-316] 003470 20.2.41.64\n[BBOX-317] 003470 20.2.41.64\n[BBOX-318] 003470 20.2.41.64\n[BBOX-319] 003470 20.2.41.64\n[BBOX-320] 003470 20.2.41.64\n[BBOX-321] 003470 20.2.41.64\n[BBOX-322] 003470 20.2.41.64\n[BBOX-323] 003470 20.2.41.64\n[BBOX-324] 003470 20.2.41.64\n[BBOX-325] 003470 20.2.41.64\n[BBOX-326] 003470 20.2.41.64\n[BBOX-327] 003470 20.2.41.64\n[BBOX-328] 003470 20.2.41.64\n[BBOX-329] 003470 20.2.41.64\n[BBOX-330] 003470 20.2.41.64\n[BBOX-331] 003470 20.2.41.64\n[BBOX-332] 003470 20.2.41.64\n[BBOX-333] 003470 20.2.41.64\n[BBOX-334] 003470 20.2.41.64\n[BBOX-335] 003470 20.2.41.64\n[BBOX-336] 003470 20.2.41.64\n[BBOX-337] 003470 20.2.41.64\n[BBOX-338] 003470 20.2.41.64\n[BBOX-339] 003470 20.2.41.64\n[BBOX-340] 003470 20.2.41.64\n[BBOX-341] 003470 20.2.41.64\n[BBOX-342] 003470 20.2.41.64\n[BBOX-343] 003470 20.2.41.64\n[BBOX-344] 003470 20.2.41.64\n[BBOX-345] 003470 20.2.41.64\n[BBOX-346] 003470 20.2.41.64\n[BBOX-347] 003470 20.2.41.64\n[BBOX-348] 003470 20.2.41.64\n[BBOX-349] 003470 20.2.41.64\n[BBOX-350] 003470 20.2.41.64\n[BBOX-351] 003470 20.2.41.64\n[BBOX-352] 003470 20.2.41.64\n[BBOX-353] 003470 20.2.41.64\n[BBOX-354] 003470 20.2.41.64\n[BBOX-355] 003470 20.2.41.64\n[BBOX-356] 003470 20.2.41.64\n[BBOX-357] 003470 20.2.41.64\n[BBOX-358] 003470 20.2.41.64\n[BBOX-359] 003470 20.2.41.64\n[BBOX-360] 003470 20.2.41.64\n[BBOX-361] 003470 20.2.41.64\n[BBOX-362] 003470 20.2.41.64\n[BBOX-363] 003470 20.2.41.64\n[BBOX-364] 003470 20.2.41.64\n[BBOX-365] 003470 20.2.41.64\n[BBOX-366] 003470 20.2.41.64\n[BBOX-367] 003470 20.2.41.64\n[BBOX-368] 003470 20.2.41.64\n[BBOX-369] 003470 20.2.41.64\n[BBOX-370] 003470 20.2.41.64\n[BBOX-371] 003470 20.2.41.64\n[BBOX-372] 003470 20.2.41.64\n[BBOX-373] 003470 20.2.41.64\n[BBOX-374] 003470 20.2.41.64\n[BBOX-375] 003470 20.2.41.64\n[BBOX-376] 003470 20.2.41.64\n[BBOX-377] 003470 20.2.41.64\n[BBOX-378] 003470 20.2.41.64\n[BBOX-379] 003470 20.2.41.64\n[BBOX-380] 003470 20.2.41.64\n[BBOX-381] 003470 20.2.41.64\n[BBOX-382] 003470 20.2.41.64\n[BBOX-383] 003470 20.2.41.64\n[BBOX-384] 003470 20.2.41.64\n[BBOX-385] 003470 20.2.41.64\n[BBOX-386] 003470 20.2.41.64\n[BBOX-387] 003470 20.2.41.64\n[BBOX-388] 003470 20.2.41.64\n[BBOX-389] 003470 20.2.41.64\n[BBOX-390] 003470 20.2.41.64\n[BBOX-391] 003470 20.2.41.64\n[BBOX-392] 003470 20.2.41.64\n[BBOX-393] 003470 20.2.41.64\n[BBOX-394] 003470 20.2.41.64\n[BBOX-395] 003470 20.2.41.64\n[BBOX-396] 003470 20.2.41.64\n[BBOX-397] 003470 20.2.41.64\n[BBOX-398] 003470 20.2.41.64\n[BBOX-399] 003470 20.2.41.64\n[BBOX-400] 003470 20.2.41.64\n[BBOX-401] 003470 20.2.41.64\n[BBOX-402] 003470 20.2.41.64\n[BBOX-403] 003470 20.2.41.64\n[BBOX-404] 003470 20.2.41.64\n[BBOX-405] 003470 20.2.41.64\n[BBOX-406] 003470 20.2.41.64\n[BBOX-407] 003470 20.2.41.64\n[BBOX-408] 003470 20.2.41.64\n[BBOX-409] 003470 20.2.41.64\n[BBOX-410] 003470 20.2.41.64\n[BBOX-411] 003470 20.2.41.64\n[BBOX-412] 003470 20.2.41.64\n[BBOX-413] 003470 20.2.41.64\n[BBOX-414] 003470 20.2.41.64\n[BBOX-415] 003470 20.2.41.64\n[BBOX-416] 003470 20.2.41.64\n[BBOX-417] 003470 20.2.41.64\n[BBOX-418] 003470 20.2.41.64\n[BBOX-419] 003470 20.2.41.64\n[BBOX-420] 003470 20.2.41.64\n[BBOX-421] 003470 20.2.41.64\n[BBOX-422] 003470 20.2.41.64\n[BBOX-423] 003470 20.2.41.64\n[BBOX-424] 003470 20.2.41.64\n[BBOX-425] 003470 20.2.41.64\n[BBOX-426] 003470 20.2.41.64\n[BBOX-427] 003470 20.2.41.64\n[BBOX-428] 003470 20.2.41.64\n[BBOX-429] 003470 20.2.41.64\n[BBOX-430] 003470 20.2.41.64\n[BBOX-431] 003470 20.2.41.64\n[BBOX-432] 003470 20.2.41.64\n[BBOX-433] 003470 20.2.41.64\n[BBOX-434] 003470 20.2.41.64\n[BBOX-435] 003470 20.2.41.64\n[BBOX-436] 003470 20.2.41.64\n[BBOX-437] 003470 20.2.41.64\n[BBOX-438] 003470 20.2.41.64\n[BBOX-439] 003470 20.2.41.64\n[BBOX-440] 003470 20.2.41.64\n[BBOX-441] 003470 20.2.41.64\n[BBOX-442] 003470 20.2.41.64\n[BBOX-443] 003470 20.2.41.64\n[BBOX-444] 003470 20.2.41.64\n[BBOX-445] 003470 20.2.41.64\n[BBOX-446] 003470 20.2.41.64\n[BBOX-447] 003470 20.2.41.64\n[BBOX-448] 003470 20.2.41.64\n[BBOX-449] 003470 20.2.41.64\n[BBOX-450] 003470 20.2.41.64\n[BBOX-451] 003470 20.2.41.64\n[BBOX-452] 003470 20.2.41.64\n[BBOX-453] 003470 20.2.41.64\n[BBOX-454] 003470 20.2.41.64\n[BBOX-455] 003470 20.2.41.64\n[BBOX-456] 003470 20.2.41.64\n[BBOX-457] 003470 20.2.41.64\n[BBOX-458] 003470 20.2.41.64\n[BBOX-459] 003470 20.2.41.64\n[BBOX-460] 003470 20.2.41.64\n[BBOX-461] 003470 20.2.41.64\n[BBOX-462] 003470 20.2.41.64\n[BBOX-463] 003470 20.2.41.64\n[BBOX-464] 003470 20.2.41.64\n[BBOX-465] 003470 20.2.41.64\n[BBOX-466] 003470 20.2.41.64\n[BBOX-467] 003470 20.2.41.64\n[BBOX-468] 003470 20.2.41.64\n[BBOX-469] 003470 20.2.41.64\n[BBOX-470] 003470 20.2.41.64\n[BBOX-471] 003470 20.2.41.64\n[BBOX-472] 003470 20.2.41.64\n[BBOX-473] 003470 20.2.41.64\n[BBOX-474] 003470 20.2.41.64\n[BBOX-475] 003470 20.2.41.64\n[BBOX-476] 003470 20.2.41.64\n[BBOX-477] 003470 20.2.41.64\n[BBOX-478] 003470 20.2.41.64\n[BBOX-479] 003470 20.2.41.64\n[BBOX-480] 003470 20.2.41.64\n[BBOX-481] 003470 20.2.41.64\n[BBOX-482] 003470 20.2.41.64\n[BBOX-483] 003470 20.2.41.64\n[BBOX-484] 003470 20.2.41.64\n[BBOX-485] 003470 20.2.41.64\n[BBOX-486] 003470 20.2.41.64\n[BBOX-487] 003470 20.2.41.64\n[BBOX-488] 003470 20.2.41.64\n[BBOX-489] 003470 20.2.41.64\n[BBOX-490] 003470 20.2.41.64\n[BBOX-491] 003470 20.2.41.64\n[BBOX-492] 003470 20.2.41.64\n[BBOX-493] 003470 20.2.41.64\n[BBOX-494] 003470 20.2.41.64\n[BBOX-495] 003470 20.2.41.64\n[BBOX-496] 003470 20.2.41.64\n[BBOX-497] 003470 20.2.41.64\n[BBOX-498] 003470 20.2.41.64\n[BBOX-499] 003470 20.2.41.64\n[BBOX-500] 003470 20.2.41.64\n[BBOX-501] 003470 20.2.41.64\n[BBOX-502] 003470 20.2.41.64\n[BBOX-503] 003470 20.2.41.64\n[BBOX-504] 003470 20.2.41.64\n[BBOX-505] 003470 20.2.41.64\n[BBOX-506] 003470 20.2.41.64\n[BBOX-507] 003470 20.2.41.64\n[BBOX-508] 003470 20.2.41.64\n[BBOX-509] 003470 20.2.41.64\n[BBOX-510] 003470 20.2.41.64\n[BBOX-511] 003470 20.2.41.64\n[BBOX-512] 003470 20.2.41.64\n[BBOX-513] 003470 20.2.41.64\n[BBOX-514] 003470 20.2.41.64\n[BBOX-515] 003470 20.2.41.64\n[BBOX-516] 003470 20.2.41.64\n[BBOX-517] 003470 20.2.41.64\n[BBOX-518] 003470 20.2.41.64\n[BBOX-519] 003470 20.2.41.64\n[BBOX-520] 003470 20.2.41.64\n[BBOX-521] 003470 20.2.41.64\n[BBOX-522] 003470 20.2.41.64\n[BBOX-523] 003470 20.2.41.64\n[BBOX-524] 003470 20.2.41.64\n[BBOX-525] 003470 20.2.41.64\n[BBOX-526] 003470 20.2.41.64\n[BBOX-527] 003470 20.2.41.64\n[BBOX-528] 003470 20.2.41.64\n[BBOX-529] 003470 20.2.41.64\n[BBOX-530] 003470 20.2.41.64\n[BBOX-531] 003470 20.2.41.64\n[BBOX-532] 003470 20.2.41.64\n[BBOX-533] 003470 20.2.41.64\n[BBOX-534] 003470 20.2.41.64\n[BBOX-535] 003470 20.2.41.64\n[BBOX-536] 003470 20.2.41.64\n[BBOX-537] 003470 20.2.41.64\n[BBOX-538] 003470 20.2.41.64\n[BBOX-539] 003470 20.2.41.64\n[BBOX-540] 003470 20.2.41.64\n[BBOX-541] 003470 20.2.41.64\n[BBOX-542] 003470 20.2.41.64\n[BBOX-543] 003470 20.2.41.64\n[BBOX-544] 003470 20.2.41.64\n[BBOX-545] 003470 20.2.41.64\n[BBOX-546] 003470 20.2.41.64\n[BBOX-547] 003470 20.2.41.64\n[BBOX-548] 003470 20.2.41.64\n[BBOX-549] 003470 20.2.41.64\n[BBOX-550] 003470 20.2.41.64\n[BBOX-551] 003470 20.2.41.64\n[BBOX-552] 003470 20.2.41.64\n[BBOX-553] 003470 20.2.41.64\n[BBOX-554] 003470 20.2.41.64\n[BBOX-555] 003470 20.2.41.64\n[BBOX-556] 003470 20.2.41.64\n[BBOX-557] 003470 20.2.41.64\n[BBOX-558] 003470 20.2.41.64\n[BBOX-559] 003470 20.2.41.64\n[BBOX-560] 003470 20.2.41.64\n[BBOX-561] 003470 20.2.41.64\n[BBOX-562] 003470 20.2.41.64\n[BBOX-563] 003470 20.2.41.64\n[BBOX-564] 003470 20.2.41.64\n[BBOX-565] 003470 20.2.41.64\n[BBOX-566] 003470 20.2.41.64\n[BBOX-567] 003470 20.2.41.64\n[BBOX-568] 003470 20.2.41.64\n[BBOX-569] 003470 20.2.41.64\n[BBOX-570] 003470 20.2.41.64\n[BBOX-571] 003470 20.2.41.64\n[BBOX-572] 003470 20.2.41.64\n[BBOX-573] 003470 20.2.41.64\n[BBOX-574] 003470 20.2.41.64\n[BBOX-575] 003470 20.2.41.64\n[BBOX-576] 003470 20.2.41.64\n[BBOX-577] 003470 20.2.41.64\n[BBOX-578] 003470 20.2.41.64\n[BBOX-579] 003470 20.2.41.64\n[BBOX-580] 003470 20.2.41.64\n[BBOX-581] 003470 20.2.41.64\n[BBOX-582] 003470 20.2.41.64\n[BBOX-583] 003470 20.2.41.64\n[BBOX-584] 003470 20.2.41.64\n[BBOX-585] 003470 20.2.41.64\n[BBOX-586] 003470 20.2.41.64\n[BBOX-587] 003470 20.2.41.64\n[BBOX-588] 003470 20.2.41.64\n[BBOX-589] 003470 20.2.41.64\n[BBOX-590] 003470 20.2.41.64\n[BBOX-591] 003470 20.2.41.64\n[BBOX-592] 003470 20.2.41.64\n[BBOX-593] 003470 20.2.41.64\n[BBOX-594] 003470 20.2.41.64\n[BBOX-595] 003470 20.2.41.64\n[BBOX-596] 003470 20.2.41.64\n[BBOX-597] 003470 20.2.41.64\n[BBOX-598] 003470 20.2.41.64\n[BBOX-599] 003470 20.2.41.64\n[BBOX-600] 003470 20.2.41.64\n[BBOX-601] 003470 20.2.41.64\n[BBOX-602] 003470 20.2.41.64\n[BBOX-603] 003470 20.2.41.64\n[BBOX-604] 003470 20.2.41.64\n[BBOX-605] 003470 20.2.41.64\n[BBOX-606] 003470 20.2.41.64\n[BBOX-607] 003470 20.2.41.64\n[BBOX-608] 003470 20.2.41.64\n[BBOX-609] 003470 20.2.41.64\n[BBOX-610] 003470 20.2.41.64\n[BBOX-611] 003470 20.2.41.64\n[BBOX-612] 003470 20.2.41.64\n[BBOX-613] 003470 20.2.41.64\n[BBOX-614] 003470 20.2.41.64\n[BBOX-615] 003470 20.2.41.64\n[BBOX-616] 003470 20.2.41.64\n[BBOX-617] 003470 20.2.41.64\n[BBOX-618] 003470 20.2.41.64\n[BBOX-619] 003470 20.2.41.64\n[BBOX-620] 003470 20.2.41.64\n[BBOX-621] 003470 20.2.41.64\n[BBOX-622] 003470 20.2.41.64\n[BBOX-623] 003470 20.2.41.64\n[BBOX-624] 003470 20.2.41.64\n[BBOX-625] 003470 20.2.41.64\n[BBOX-626] 003470 20.2.41.64\n[BBOX-627] 003470 20.2.41.64\n[BBOX-628] 003470 20.2.41.64\n[BBOX-629] 003470 20.2.41.64\n[BBOX-630] 003470 20.2.41.64\n[BBOX-631] 003470 20.2.41.64\n[BBOX-632] 003470 20.2.41.64\n[BBOX-633] 003470 20.2.41.64\n[BBOX-634] 003470 20.2.41.64\n[BBOX-635] 003470 20.2.41.64\n[BBOX-636] 003470 20.2.41.64\n[BBOX-637] 003470 20.2.41.64\n[BBOX-638] 003470 20.2.41.64\n[BBOX-639] 003470 20.2.41.64\n[BBOX-640] 003470 20.2.41.64\n[BBOX-641] 003470 20.2.41.64\n[BBOX-642] 003470 20.2.41.64\n[BBOX-643] 003470 20.2.41.64\n[BBOX-644] 003470 20.2.41.64\n[BBOX-645] 003470 20.2.41.64\n[BBOX-646] 003470 20.2.41.64\n[BBOX-647] 003470 20.2.41.64\n[BBOX-648] 003470 20.2.41.64\n[BBOX-649] 003470 20.2.41.64\n[BBOX-650] 003470 20.2.41.64\n[BBOX-651] 003470 20.2.41.64\n[BBOX-652] 003470 20.2.41.64\n[BBOX-653] 003470 20.2.41.64\n[BBOX-654] 003470 20.2.41.64\n[BBOX-655] 003470 20.2.41.64\n[BBOX-656] 003470 20.2.41.64\n[BBOX-657] 003470 20.2.41.64\n[BBOX-658] 003470 20.2.41.64\n[BBOX-659] 003470 20.2.41.64\n[BBOX-660] 003470 20.2.41.64\n[BBOX-661] 003470 20.2.41.64\n[BBOX-662] 003470 20.2.41.64\n[BBOX-663] 003470 20.2.41.64\n[BBOX-664] 003470 20.2.41.64\n[BBOX-665] 003470 20.2.41.64\n[BBOX-666] 003470 20.2.41.64\n[BBOX-667] 003470 20.2.41.64\n[BBOX-668] 003470 20.2.41.64\n[BBOX-669] 003470 20.2.41.64\n[BBOX-670] 003470 20.2.41.64\n[BBOX-671] 003470 20.2.41.64\n[BBOX-672] 003470 20.2.41.64\n[BBOX-673] 003470 20.2.41.64\n[BBOX-674] 003470 20.2.41.64\n[BBOX-675] 003470 20.2.41.64\n[BBOX-676] 003470 20.2.41.64\n[BBOX-677] 003470 20.2.41.64\n[BBOX-678] 003470 20.2.41.64\n[BBOX-679] 003470 20.2.41.64\n[BBOX-680] 003470 20.2.41.64\n[BBOX-681] 003470 20.2.41.64\n[BBOX-682] 003470 20.2.41.64\n[BBOX-683] 003470 20.2.41.64\n[BBOX-684] 003470 20.2.41.64\n[BBOX-685] 003470 20.2.41.64\n[BBOX-686] 003470 20.2.41.64\n[BBOX-687] 003470 20.2.41.64\n[BBOX-688] 003470 20.2.41.64\n[BBOX-689] 003470 20.2.41.64\n[BBOX-690] 003470 20.2.41.64\n[BBOX-691] 003470 20.2.41.64\n[BBOX-692] 003470 20.2.41.64\n[BBOX-693] 003470 20.2.41.64\n[BBOX-694] 003470 20.2.41.64\n[BBOX-695] 003470 20.2.41.64\n[BBOX-696] 003470 20.2.41.64\n[BBOX-697] 003470 20.2.41.64\n[BBOX-698] 003470 20.2.41.64\n[BBOX-699] 003470 20.2.41.64\n[BBOX-700] 003470 20.2.41.64\n[BBOX-701] 003470 20.2.41.64\n[BBOX-702] 003470 20.2.41.64\n[BBOX-703] 003470 20.2.41.64\n[BBOX-704] 003470 20.2.41.64\n[BBOX-705] 003470 20.2.41.64\n[BBOX-706] 003470 20.2.41.64\n[BBOX-707] 003470 20.2.41.64\n[BBOX-708] 003470 20.2.41.64\n[BBOX-709] 003470 20.2.41.64\n[BBOX-710] 003470 20.2.41.64\n[BBOX-711] 003470 20.2.41.64\n[BBOX-712] 003470 20.2.41.64\n[BBOX-713] 003470 20.2.41.64\n[BBOX-714] 003470 20.2.41.64\n[BBOX-715] 003470 20.2.41.64\n[BBOX-716] 003470 20.2.41.64\n[BBOX-717] 003470 20.2.41.64\n[BBOX-718] 003470 20.2.41.64\n[BBOX-719] 003470 20.2.41.64\n[BBOX-720] 003470 20.2.41.64\n[BBOX-721] 003470 20.2.41.64\n[BBOX-722] 003470 20.2.41.64\n[BBOX-723] 003470 20.2.41.64\n[BBOX-724] 003470 20.2.41.64\n[BBOX-725] 003470 20.2.41.64\n[BBOX-726] 003470 20.2.41.64\n[BBOX-727] 003470 20.2.41.64\n[BBOX-728] 003470 20.2.41.64\n[BBOX-729] 003470 20.2.41.64\n[BBOX-730] 003470 20.2.41.64\n[BBOX-731] 003470 20.2.41.64\n[BBOX-732] 003470 20.2.41.64\n[BBOX-733] 003470 20.2.41.64\n[BBOX-734] 003470 20.2.41.64\n[BBOX-735] 003470 20.2.41.64\n[BBOX-736] 003470 20.2.41.64\n[BBOX-737] 003470 20.2.41.64\n[BBOX-738] 003470 20.2.41.64\n[BBOX-739] 003470 20.2.41.64\n[BBOX-740] 003470 20.2.41.64\n[BBOX-741] 003470 20.2.41.64\n[BBOX-742] 003470 20.2.41.64\n[BBOX-743] 003470 20.2.41.64\n[BBOX-744] 003470 20.2.41.64\n[BBOX-745] 003470 20.2.41.64\n[BBOX-746] 003470 20.2.41.64\n[BBOX-747] 003470 20.2.41.64\n[BBOX-748] 003470 20.2.41.64\n[BBOX-749] 003470 20.2.41.64\n[BBOX-750] 003470 20.2.41.64\n[BBOX-751] 003470 20.2.41.64\n[BBOX-752] 003470 20.2.41.64\n[BBOX-753] 003470 20.2.41.64\n[BBOX-754] 003470 20.2.41.64\n[BBOX-755] 003470 20.2.41.64\n[BBOX-756] 003470 20.2.41.64\n[BBOX-757] 003470 20.2.41.64\n[BBOX-758] 003470 20.2.41.64\n[BBOX-759] 003470 20.2.41.64\n[BBOX-760] 003470 20.2.41.64\n[BBOX-761] 003470 20.2.41.64\n[BBOX-762] 003470 20.2.41.64\n[BBOX-763] 003470 20.2.41.64\n[BBOX-764] 003470 20.2.41.64\n[BBOX-765] 003470 20.2.41.64\n[BBOX-766] 003470 20.2.41.64\n[BBOX-767] 003470 20.2.41.64\n[BBOX-768] 003470 20.2.41.64\n[BBOX-769] 003470 20.2.41.64\n[BBOX-770] 003470 20.2.41.64\n[BBOX-771] 003470 20.2.41.64\n[BBOX-772] 003470 20.2.41.64\n[BBOX-773] 003470 20.2.41.64\n[BBOX-774] 003470 20.2.41.64\n[BBOX-775] 003470 20.2.41.64\n[BBOX-776] 003470 20.2.41.64\n[BBOX-777] 003470 20.2.41.64\n[BBOX-778] 003470 20.2.41.64\n[BBOX-779] 003470 20.2.41.64\n[BBOX-780] 003470 20.2.41.64\n[BBOX-781] 003470 20.2.41.64\n[BBOX-782] 003470 20.2.41.64\n[BBOX-783] 003470 20.2.41.64\n[BBOX-784] 003470 20.2.41.64\n[BBOX-785] 003470 20.2.41.64\n[BBOX-786] 003470 20.2.41.64\n[BBOX-787] 003470 20.2.41.64\n[BBOX-788] 003470 20.2.41.64\n[BBOX-789] 003470 20.2.41.64\n[BBOX-790] 003470 20.2.41.64\n[BBOX-791] 003470 20.2.41.64\n[BBOX-792] 003470 20.2.41.64\n[BBOX-793] 003470 20.2.41.64\n[BBOX-794] 003470 20.2.41.64\n[BBOX-795] 003470 20.2.41.64\n[BBOX-796] 003470 20.2.41.64\n[BBOX-797] 003470 20.2.41.64\n[BBOX-798] 003470 20.2.41.64\n[BBOX-799] 003470 20.2.41.64\n[BBOX-800] 003470 20.2.41.64\n[BBOX-801] 003470 20.2.41.64\n[BBOX-802] 003470 20.2.41.64\n[BBOX-803] 003470 20.2.41.64\n[BBOX-804] 003470 20.2.41.64\n[BBOX-805] 003470 20.2.41.64\n[BBOX-806] 003470 20.2.41.64\n[BBOX-807] 003470 20.2.41.64\n[BBOX-808] 003470 20.2.41.64\n[BBOX-809] 003470 20.2.41.64\n[BBOX-810] 003470 20.2.41.64\n[BBOX-811] 003470 20.2.41.64\n[BBOX-812] 003470 20.2.41.64\n[BBOX-813] 003470 20.2.41.64\n[BBOX-814] 003470 20.2.41.64\n[BBOX-815] 003470 20.2.41.64\n[BBOX-816] 003470 20.2.41.64\n[BBOX-817] 003470 20.2.41.64\n[BBOX-818] 003470 20.2.41.64\n[BBOX-819] 003470 20.2.41.64\n[BBOX-820] 003470 20.2.41.64\n[BBOX-821] 003470 20.2.41.64\n[BBOX-822] 003470 20.2.41.64\n[BBOX-823] 003470 20.2.41.64\n[BBOX-824] 003470 20.2.41.64\n[BBOX-825] 003470 20.2.41.64\n[BBOX-826] 003470 20.2.41.64\n[BBOX-827] 003470 20.2.41.64\n[BBOX-828] 003470 20.2.41.64\n[BBOX-829] 003470 20.2.41.64\n[BBOX-830] 003470 20.2.41.64\n[BBOX-831] 003470 20.2.41.64\n[BBOX-832] 003470 20.2.41.64\n[BBOX-833] 003470 20.2.41.64\n[BBOX-834] 003470 20.2.41.64\n[BBOX-835] 003470 20.2.41.64\n[BBOX-836] 003470 20.2.41.64\n[BBOX-837] 003470 20.2.41.64\n[BBOX-838] 003470 20.2.41.64\n[BBOX-839] 003470 20.2.41.64\n[BBOX-840] 003470 20.2.41.64\n[BBOX-841] 003470 20.2.41.64\n[BBOX-842] 003470 20.2.41.64\n[BBOX-843] 003470 20.2.41.64\n[BBOX-844] 003470 20.2.41.64\n[BBOX-845] 003470 20.2.41.64\n[BBOX-846] 003470 20.2.41.64\n[BBOX-847] 003470 20.2.41.64\n[BBOX-848] 003470 20.2.41.64\n[BBOX-849] 003470 20.2.41.64\n[BBOX-850] 003470 20.2.41.64\n[BBOX-851] 003470 20.2.41.64\n[BBOX-852] 003470 20.2.41.64\n[BBOX-853] 003470 20.2.41.64\n[BBOX-854] 003470 20.2.41.64\n[BBOX-855] 003470 20.2.41.64\n[BBOX-856] 003470 20.2.41.64\n[BBOX-857] 003470 20.2.41.64\n[BBOX-858] 003470 20.2.41.64\n[BBOX-859] 003470 20.2.41.64\n[BBOX-860] 003470 20.2.41.64\n[BBOX-861] 003470 20.2.41.64\n[BBOX-862] 003470 20.2.41.64\n[BBOX-863] 003470 20.2.41.64\n[BBOX-864] 003470 20.2.41.64\n[BBOX-865] 003470 20.2.41.64\n[BBOX-866] 003470 20.2.41.64\n[BBOX-867] 003470 20.2.41.64\n[BBOX-868] 003470 20.2.41.64\n[BBOX-869] 003470 20.2.41.64\n[BBOX-870] 003470 20.2.41.64\n[BBOX-871] 003470 20.2.41.64\n[BBOX-872] 003470 20.2.41.64\n[BBOX-873] 003470 20.2.41.64\n[BBOX-874] 003470 20.2.41.64\n[BBOX-875] 003470 20.2.41.64\n[BBOX-876] 003470 20.2.41.64\n[BBOX-877] 003470 20.2.41.64\n[BBOX-878] 003470 20.2.41.64\n[BBOX-879] 003470 20.2.41.64\n[BBOX-880] 003470 20.2.41.64\n[BBOX-881] 003470 20.2.41.64\n[BBOX-882] 003470 20.2.41.64\n[BBOX-883] 003470 20.2.41.64\n[BBOX-884] 003470 20.2.41.64\n[BBOX-885] 003470 20.2.41.64\n[BBOX-886] 003470 20.2.41.64\n[BBOX-887] 003470 20.2.41.64\n[BBOX-888] 003470 20.2.41.64\n[BBOX-889] 003470 20.2.41.64\n[BBOX-890] 003470 20.2.41.64\n[BBOX-891] 003470 20.2.41.64\n[BBOX-892] 003470 20.2.41.64\n[BBOX-893] 003470 20.2.41.64\n[BBOX-894] 003470 20.2.41.64\n[BBOX-895] 003470 20.2.41.64\n[BBOX-896] 003470 20.2.41.64\n[BBOX-897] 003470 20.2.41.64\n[BBOX-898] 003470 20.2.41.64\n[BBOX-899] 003470 20.2.41.64\n[BBOX-900] 003470 20.2.41.64\n[BBOX-901] 003470 20.2.41.64\n[BBOX-902] 003470 20.2.41.64\n[BBOX-903] 003470 20.2.41.64\n[BBOX-904] 003470 20.2.41.64\n[BBOX-905] 003470 20.2.41.64\n[BBOX-906] 003470 20.2.41.64\n[BBOX-907] 003470 20.2.41.64\n[BBOX-908] 003470 20.2.41.64\n[BBOX-909] 003470 20.2.41.64\n[BBOX-910] 003470 20.2.41.64\n[BBOX-911] 003470 20.2.41.64\n[BBOX-912] 003470 20.2.41.64\n[BBOX-913] 003470 20.2.41.64\n[BBOX-914] 003470 20.2.41.64\n[BBOX-915] 003470 20.2.41.64\n[BBOX-916] 003470 20.2.41.64\n[BBOX-917] 003470 20.2.41.64\n[BBOX-918] 003470 20.2.41.64\n[BBOX-919] 003470 20.2.41.64\n[BBOX-920] 003470 20.2.41.64\n[BBOX-921] 003470 20.2.41.64\n[BBOX-922] 003470 20.2.41.64\n[BBOX-923] 003470 20.2.41.64\n[BBOX-924] 003470 20.2.41.64\n[BBOX-925] 003470 20.2.41.64\n[BBOX-926] 003470 20.2.41.64\n[BBOX-927] 003470 20.2.41.64\n[BBOX-928] 003470 20.2.41.64\n[BBOX-929] 003470 20.2.41.64\n[BBOX-930] 003470 20.2.41.64\n[BBOX-931] 003470 20.2.41.64\n[BBOX-932] 003470 20.2.41.64\n[BBOX-933] 003470 20.2.41.64\n[BBOX-934] 003470 20.2.41.64\n[BBOX-935] 003470 20.2.41.64\n[BBOX-936] 003470 20.2.41.64\n[BBOX-937] 003470 20.2.41.64\n[BBOX-938] 003470 20.2.\n[BBOX-939] 编辑\n[BBOX-940] 功能\n[BBOX-941] 表格\n[BBOX-942] 签名\n[BBOX-943] 其他\n[BBOX-944] 打印\n[BBOX-945] 预览\n[BBOX-946] 验证CA签名\n[BBOX-947] 手工解锁\n[BBOX-948] 删除\n[BBOX-949] 病历参考\n[BBOX-950] 更新数据\n[BBOX-951] 加载全部病程\n[BBOX-952] 个人模板管理\n[BBOX-953] 返回\n[BBOX-954] 腹部:\n[BBOX-955] 视诊: 外形: 腹部外形正常\n[BBOX-956] 腹围: 未测\n[BBOX-957] 脐部: 正常\n[BBOX-958] 胃形: 未见\n[BBOX-959] 肠形: 未见\n[BBOX-960] 蠕动波: 未见\n[BBOX-961] 腹式呼吸: 正常\n[BBOX-962] 腹壁静脉曲张: 无\n[BBOX-963] 腹壁其它情况: 无\n[BBOX-964] 触诊: 全腹柔软\n[BBOX-965] 压痛反跳痛: 无压痛及反跳痛\n[BBOX-966] 波动感: 无\n[BBOX-967] 振水声: 无\n[BBOX-968] 腹部包块: 腹部未触及包块\n[BBOX-969] 肝脏: 肝脏肋下未触及\n[BBOX-970] 胆囊: 未触及, Murphy征阴性\n[BBOX-971] 脾脏: 脾脏肋下未触及\n[BBOX-972] 肾脏: 未触及\n[BBOX-973] 输尿管压痛点: 无压痛\n[BBOX-974] 叩诊: 肝浊音界: 正常,\n[BBOX-975] 肝上界位于锁骨中线, 第五肋间\n[BBOX-976] 移动性浊音: 阴性,\n[BBOX-977] 肾区叩痛: 无\n[BBOX-978] 听诊: 肠鸣音无明显增强或减弱, 未闻及血管杂音\n[BBOX-979] 肛门直肠: 未查\n[BBOX-980] 生殖器: 未查\n[BBOX-981] 脊柱四肢:\n[BBOX-982] 脊柱外形: 脊柱正常生理弯曲\n[BBOX-983] 70 四 肢：四肢无畸形，未见杵状指（趾），未见静脉曲张，双下肢无凹陷性水肿\n[BBOX-984] 关 节：各关节未见异常，活动无受限\n[BBOX-985] 肌 肉：未见肌肉萎缩，肌张力正常。四肢肌力5级。\n[BBOX-986] 神经系统：\n[BBOX-987] 浅反射：双侧浅反射正常引出\n[BBOX-988] 深反射：双侧深反射正常引出\n[BBOX-989] 病理反射：未引出\n[BBOX-990] 脑膜刺激征：阴性\n[BBOX-991] 专科情况\n[BBOX-992] 神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下肢无凹陷性水肿。\n[BBOX-993] 实验室及器械检查结果\n[BBOX-994] (2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组织肿块，最大截断���约77mm*60mm\n[BBOX-995] ，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋巴结彩超\n[BBOX-996] ：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。\n[BBOX-997] 2026-02-28 18:30\n[BBOX-998] 男，因“咳嗽、咳痰1月余”于2026-02-28 15:23入非急诊步行入科。\n[BBOX-999] 病例特点如下：1、老年期男性，起病缓，病程短。2、患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，\n[BBOX-1000] 伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。3、既往史：平素\n[BBOX-1001] 健康状况：良好。既往病史：否认高血压、冠心病、糖尿病史。传染病史：否，否认肝炎、结核或其他传染病史。预\n[BBOX-1002] 防接种史：正规。过敏史：否认过敏史。外伤史：否认外伤史。手术史：2年前曾行尿道结石手术，具体不详。输血\n[BBOX-1003] 史：否认输血史。系统回顾：无特殊。否认新冠肺炎流行病接触史。4、查体：T：36.8℃，P：75次/分，R：21次/分\n[BBOX-1004] ，BP：138/72mmHg。神志清楚，正常面容，皮肤巩膜无黄染，全身浅表淋巴结未扪及肿大，颈静脉无怒张。胸廓对称\n[BBOX-1005] 无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常，双肺叩诊呈清音，双肺呼吸音\n[BBOX-1006] 清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音。心界不大，心率75次/分，心律齐，各瓣膜区未闻及杂音。腹\n[BBOX-1007] 部外形正常，全腹柔软，无压痛及反跳痛，腹部未触及包块，肝脏肋下未触及，脾脏肋下未触及。移动性浊音阴性。\n[BBOX-1008] 双下肢无凹陷性水肿。浅反射：双侧浅反射正常引出。深反射：双侧深反射正常引出。病理反射：未引出。脑膜刺激\n[BBOX-1009] 征：阴性5、专科情况：神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下\n[BBOX-1010] 肢无凹陷性水肿。6、辅助检查：（2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组\n[BBOX-1011] 织肿块，最大截断面约77mm*60mm，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧\n[BBOX-1012] 胸膜肥厚、钙化。浅表淋巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。\n[BBOX-1013] 初步诊断：1.肺部阴影\n[BBOX-1014] 2.细菌性肺炎\n[BBOX-1015] 诊断依据：1.老年男性，起步缓，病程短\n[BBOX-1016] 2.咳嗽，咳淡黄色粘液痰\n[BBOX-1017] 3.外院胸部CT提示右肺下叶后基底段软组织肿块\n[BBOX-1018] 鉴别诊断。\n[BBOX-1019] 1.肺结核球\n[BBOX-1020] 编辑\n[BBOX-1021] 功能\n[BBOX-1022] 表格\n[BBOX-1023] 签名\n[BBOX-1024] 其他\n[BBOX-1025] 打印\n[BBOX-1026] 预览\n[BBOX-1027] 验证CA签名\n[BBOX-1028] 手工解锁\n[BBOX-1029] 删除\n[BBOX-1030] 病历参考\n[BBOX-1031] 更新数据\n[BBOX-1032] 加载全部病程\n[BBOX-1033] 个人模板管理\n[BBOX-1034] 返回\n[BBOX-1035] 鉴别诊断：\n[BBOX-1036] 1.肺结核球：多见于年轻患者，病灶多见于结核好发部位，如肺上叶尖后段和下叶背段，直径一般<3\n[BBOX-1037] cm。一般无症状，病灶边界清楚，密度高，可有包膜。有时含钙化点，周围有卫星灶。\n[BBOX-1038] 2.急性粟粒性肺结核：应与弥漫型细支气管肺泡癌相鉴别。通常粟粒型肺结核患者年龄较轻，有发热\n[BBOX-1039] ，盗汗等全身中毒症状，呼吸道症状不明显。x线表现为细小、分布均匀、密度较淡的粟粒样结节病灶。\n[BBOX-1040] 而细支气管—肺泡细胞癌两肺多有大小不等的结节状播散病灶，边界清楚、密度较高，进行性发展和增大\n[BBOX-1041] ，且有进行性呼吸困难。\n[BBOX-1042] 3.肺炎：若无毒性症状，抗生素治疗后肺部阴影吸收缓慢，或同一部位反复发生肺炎时，应考虑到肺\n[BBOX-1043] 癌可能。肺部慢性炎症机化，形成团块状的炎性假瘤，也易与肺癌相混淆。但炎性假瘤往往形态不整，边\n[BBOX-1044] 缘不齐，核心密度较高，易伴有胸膜增厚，病灶长期无明显变化。\n[BBOX-1045] 4.肺脓肿：起病急，中毒症状严重，多有寒战、高热、咳嗽、咳大量脓臭痰等症状。肺部x线表现为\n[BBOX-1046] 均匀的大片状炎性阴影，空洞内常见较深液平。结合纤支镜检查和痰脱落细胞检查可以鉴别。\n[BBOX-1047] 5.纵隔淋巴瘤：颇似中央型肺癌，常为双侧性，可有发热等全身症状，需病理诊断。\n[BBOX-1048] VTE血栓风险评估：创建时间:2026-02-28 15:37:11,评估节点:入院,量表名称:Padua评分,分数:0,评分描述:低危,\n[BBOX-1049] 预防措施:undefined\n[BBOX-1050] VTE出血风险评估：创建时间:2026-02-28 18:35:54,评估节点:入院,量表名称:内科出血风险评估,分数:1,评分描述：\n[BBOX-1051] 低危,预防措施:undefined\n[BBOX-1052] 诊疗计划：1.内科护理常规,II级护理。\n[BBOX-1053] 2.完善必要辅助检查如血肿瘤标志物、痰液化验、胸部增强CT、支气管镜检查或浅表淋巴结及肺穿刺活检\n[BBOX-1054] 以确诊，必要时行颅脑MRI、腹部超声、骨扫描或PET-CT等检查以利进一步疾病诊治。\n[BBOX-1055] 3.给予吸氧、抗感染及止血、镇痛等对症支持治疗；明确病理类型拟定下一步治疗方案。\n[BBOX-1056] 是否需手术治疗：否\n[BBOX-1057] 医师签名：姜晓红 住院医师：孙超群\n[BBOX-1058] 影像检查报告单\n[BBOX-1059] 病人 ID:\n[BBOX-1060] 姓名:\n[BBOX-1061] 性别: 男\n[BBOX-1062] 年龄: 67岁\n[BBOX-1063] 申请科室: 老年医学呼吸内科\n[BBOX-1064] 机器型号: SE-MR4\n[BBOX-1065] 住院号\n[BBOX-1066] 检查部位: 颅脑颅脑MR平扫及增强+DWI,*钆特酸葡胺注射液【广西HR】\n[BBOX-1067] 检查日期: 2026-03-13\n[BBOX-1068] (此报告仅供临床医师诊断参考,不作为疾病证明)\n[BBOX-1069] 检查所见:\n[BBOX-1070] 左侧基底节区、两侧放射冠、右侧侧脑室前后角旁见小斑片状、斑点状等T1、稍\n[BBOX-1071] 长T2信号灶,FLAIR呈高信号,边界欠清,DWI未见弥散受限;余脑实质信号未见异\n[BBOX-1072] 常,DWI未见明确弥散受限区,增强扫描未见异常强化灶;静脉窦强化充盈良好,未\n[BBOX-1073] 见异常;各脑室及脑沟、裂、池对称性轻度增宽;中线结构无移位。\n[BBOX-1074] 诊断意见:\n[BBOX-1075] 脑白质病变--改良Fasekas1级;轻度脑萎缩。\n[BBOX-1076] 检查技师: 唐成\n[BBOX-1077] 报告医师: 郭仟\n[BBOX-1078] 审核医师: 张\n[BBOX-1079] 报告日期: 2026-03-16 15:13:19\n[BBOX-1080] 审核日期: 2026-03-16 18:28:39\n[BBOX-1081] 地址: 广西医科大学第一附属医院放射科\n[BBOX-1082] 联系电话: 0771-5356934\n[BBOX-1083] “广西HR”解释: 广西影像检查项目互认\n[BBOX-1084] 科\n[BBOX-1085] 检查部位：全身骨显像 显像剂：99mTc-MDP 临床诊断：1.肺占位性病变,2.细菌性肺炎,3.肺\n[BBOX-1086] 剂量：25mCi 部阴影\n[BBOX-1087] （此报告仅供临床医师诊断参考，不作为疾病证明）\n[BBOX-1088] 检查所见：\n[BBOX-1089] 静脉注射99mTc-MDP 3小时后行全身骨显像前位、后位各1帧：\n[BBOX-1090] 全身骨像完整、显影基本清晰。颅骨、胸骨、椎体、肩胛骨、肋骨、骨盆及四肢骨显像剂分\n[BBOX-1091] 布未见明显异常改变。\n[BBOX-1092] 双肾显影，膀胱部分充盈。\n[BBOX-1093] 诊断意见：\n[BBOX-1094] 全身骨显像未见明显异常改变。\n[BBOX-1095] 报告医师：巫殷豪\n[BBOX-1096] 审核医师：彭盛梅\n[BBOX-1097] 报告日期：2026-03-10\n[BBOX-1098] 广西医科大学第一附属医院\n[BBOX-1099] 影像检查报告单\n[BBOX-1100] 病人ID:\n[BBOX-1101] 姓名:\n[BBOX-1102] 性别: 男\n[BBOX-1103] 年龄: 67岁\n[BBOX-1104] 申请科室:\n[BBOX-1105] 机器型号: SE-\n[BBOX-1106] 床号: 49床\n[BBOX-1107] 住院号: 1959\n[BBOX-1108] Force-2\n[BBOX-1109] 检查部位: 下腹部,上腹部CT平扫+增强,(新)碘帕醇注射液\n[BBOX-1110] 【广西HR】\n[BBOX-1111] 检查日期: 2026-03-11\n[BBOX-1112] (此报告仅供临床医师诊断参考,不作为疾病证明)\n[BBOX-1113] 检查所见:\n[BBOX-1114] 双侧肾上腺见多个结节状稍低/低密度影,较大者大小约1.6cm×1.2cm,增强扫\n[BBOX-1115] 描不均匀强化。肝脏各叶比例正常,肝实质内见多发类圆形低密度无强化灶,较大者\n[BBOX-1116] 位于S8,大小约1.2cm×1.1cm;余肝实质未见异常密度影及异常强化灶。肝内、外胆\n[BBOX-1117] 管未见扩张,胆囊不大,囊壁均匀,囊内密度未见异常。脾脏、胰腺形态、大小、密\n[BBOX-1118] 度未见异常,增强扫描未见异常强化,右肾体积缩小,双肾实质内见多个类圆形低密\n[BBOX-1119] 度无强化灶,较大者大小约0.9cm×1.5cm;双侧肾盂肾盏及输尿管未见扩张。腹部肠\n[BBOX-1120] 管分布正常,管腔未见扩张、积液,腹腔内未见明确肿块影;肝门及腹主动脉旁未见\n[BBOX-1121] 增大淋巴结,腹膜腔未见积液。\n[BBOX-1122] 诊断意见:\n[BBOX-1123] 1.双侧肾上腺占位,考虑转移瘤可能性大,请结合临床;\n[BBOX-1124] 2.肝多发囊肿;\n[BBOX-1125] 3.右肾萎缩,双肾囊肿。\n[BBOX-1126] 检查技师:刘辰民 报告医师:谢金桓 审核医师: 冯涛\n[BBOX-1127] 报告日期:2026-03-11 14:21:30 审核日期:2026-03-11 16:15:45\n[BBOX-1128] 地址:广西医科大学第一附属医院放射科 联系电话:0771-5356934 “广西HR”解释:广西影像检查项目互认\n[BBOX-1129] 广西医科大学第一附属医院\n[BBOX-1130] 影像检查报告单\n[BBOX-1131] 病人ID:\n[BBOX-1132] 姓名:\n[BBOX-1133] 男\n[BBOX-1134] 年龄: 67岁\n[BBOX-1135] 申请科室: 老年医学呼吸内科\n[BBOX-1136] 机器型号: SE-\n[BBOX-1137] Force-2\n[BBOX-1138] 床号\n[BBOX-1139] 号\n[BBOX-1140] 检查部位: 胸部CT平扫+增强,*碘海醇注射液【广西HR】\n[BBOX-1141] 检查日期: 2026-03-02\n[BBOX-1142] (此报告仅供临床医师诊断参考,不作为疾病证明)\n[BBOX-1143] 检查所见:\n[BBOX-1144] 两肺尖胸膜下见类圆形透亮影,较大者长径约0.8cm;右肺下叶基底段(Se4:IM144)见团\n[BBOX-1145] 块状密度增高灶,大小约为7.7cm×5.1cm×6.9cm,增强扫描中度强化;两肺可见多发实性结节\n[BBOX-1146] 影,较大位于右肺下叶外基底段(Se4:IM344),内可见空泡,长径约为1.1cm,增强扫描似见\n[BBOX-1147] 血管穿行。右肺中叶、左肺上叶下舌段及两肺下叶见条索状密度增高影;余肺叶内未见异常密\n[BBOX-1148] 度影及异常强化灶,右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张,两肺部分支气管\n[BBOX-1149] 管壁增厚,管腔变窄,气管、其余支气管通畅;肺门、纵隔结构清楚,纵隔、两侧肺门见多发\n[BBOX-1150] 淋巴结,大者短径约1.1cm。两侧胸膜增厚、钙化,胸膜腔未见积液。主动脉、冠状动脉见斑片\n[BBOX-1151] 状钙化灶。\n[BBOX-1152] 诊断意见:\n[BBOX-1153] 1.右肺下叶后基底段软组织肿块,肿瘤性病变?感染性病变?请结合临床及实验室检查;\n[BBOX-1154] 2.两肺多发实性结节,建议短期复查;\n[BBOX-1155] 3.右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张并两肺炎症;\n[BBOX-1156] 4.两肺上叶间隔旁型肺气肿;\n[BBOX-1157] 5.纵隔、两侧肺门淋巴结,建议复查;\n[BBOX-1158] 6.两侧胸膜肥厚、钙化;\n[BBOX-1159] 7.主动脉、冠状动脉硬化。\n[BBOX-1160] 检查技师:周春燚 报告医师:肖芳艳 审核医师:\n[BBOX-1161] 报告日期:2026-03-03 18:39:05 审核日期:2026-03-04 09:21:01\n[BBOX-1162] 地址:广西医科大学第一附属医院放射科 联系电话:0771-5356934 “广西HR”解码:广西影像检查项目互认\n[BBOX-1163] 测量参数值:\n[BBOX-1164] 测量项目\n[BBOX-1165] 结果\n[BBOX-1166] 单位\n[BBOX-1167] 参考范围\n[BBOX-1168] 测量项目\n[BBOX-1169] 结果\n[BBOX-1170] 单位\n[BBOX-1171] 参考范围\n[BBOX-1172] 主动脉根部内径:\n[BBOX-1173] 27\n[BBOX-1174] mm\n[BBOX-1175] (20-35)\n[BBOX-1176] 左房前后径:\n[BBOX-1177] 35\n[BBOX-1178] mm\n[BBOX-1179] (24-39)\n[BBOX-1180] 左室舒末前后径:\n[BBOX-1181] 53\n[BBOX-1182] mm\n[BBOX-1183] (38-54)\n[BBOX-1184] 左室缩末前后径:\n[BBOX-1185] 32\n[BBOX-1186] mm\n[BBOX-1187] (24-37)\n[BBOX-1188] 室间隔舒末厚:\n[BBOX-1189] 10\n[BBOX-1190] mm\n[BBOX-1191] (6-11)\n[BBOX-1192] 左室后壁舒末厚:\n[BBOX-1193] 10\n[BBOX-1194] mm\n[BBOX-1195] (6-11)\n[BBOX-1196] 右室舒末前后径:\n[BBOX-1197] 18\n[BBOX-1198] mm\n[BBOX-1199] (15-30)\n[BBOX-1200] 右室流出道:\n[BBOX-1201] 27\n[BBOX-1202] mm\n[BBOX-1203] (15-32)\n[BBOX-1204] 主肺动脉内径:\n[BBOX-1205] 22\n[BBOX-1206] mm\n[BBOX-1207] (15-26)\n[BBOX-1208] E/A\n[BBOX-1209] <1\n[BBOX-1210] (0.8-2.0)\n[BBOX-1211] e'/a'\n[BBOX-1212] <1\n[BBOX-1213] (->)\n[BBOX-1214] E/e'\n[BBOX-1215] 11.7\n[BBOX-1216] (->)\n[BBOX-1217] 超声描述:\n[BBOX-1218] 描述:\n[BBOX-1219] 1、按比例各房室大小正常，房、室间隔连续完整，室间隔与左室壁厚度正常，静息状态下室壁收\n[BBOX-1220] 缩运动有力，未见节段性运动异常。左室收缩功能测定在正常范围，FS:40%，EF:70%，SV:95ml/B\n[BBOX-1221] ，CO:6.4L/min，EDV:135ml，心包腔内未探及液性区声像。\n[BBOX-1222] 2、三尖瓣形态结构正常，瓣口轻度反流，速度2.4m/s，压差22mmHg，瞬时反流量约2ml（无血流动\n[BBOX-1223] 力学意义），余各瓣膜形态结构正常，启闭运动好，二尖瓣血流图示E峰小于A峰。\n[BBOX-1224] 3、主动脉根部内径正常，升主动脉内径正常，管壁增厚，弹性降低，主肺动脉内径正常，内回声\n[BBOX-1225] 及血流信号未见异常。\n[BBOX-1226] 超声诊断:\n[BBOX-1227] 1、心脏形态结构及瓣膜功能大致正常。\n[BBOX-1228] 2、左室舒张功能降低，收缩功能测定在正常范围，\n[BBOX-1229] 诊断医师：吴颖/肖彩意\n[BBOX-1230] 报告日期：2026-03-02 10:12:46\n[BBOX-1231] \\begin{tabular}{ccccccccc}\n[BBOX-1232] 报告时间: 2026-02-28\n[BBOX-1233] \\hline\n[BBOX-1234] 缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\\\\n[BBOX-1235] \\hline\n[BBOX-1236] TB-DNA & 结核杆菌DNA* & $<$5.00E+02 & & & & 拷贝 & $<$5.00E+02 & $<$5.00E+02 \\\\\n[BBOX-1237] \\hline\n[BBOX-1238] \\end{tabular}\n[BBOX-1239] \\begin{tabular}{ccccccccc}\n[BBOX-1240] 报告时间: 2026-02-28\n[BBOX-1241] \\hline\n[BBOX-1242] 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\\\\n[BBOX-1243] \\hline\n[BBOX-1244] 乙型肝炎表面抗原* & 0.00 & & & & IU/ml & 0-0.08 & \\\\\n[BBOX-1245] 乙型肝炎表面抗体* & 14.85 & & $\\uparrow$ & & mIU/mL & 0-10 & \\\\\n[BBOX-1246] 乙型肝炎e抗原* & 0.00 & & & & PElu/ml & 0-0.10 & \\\\\n[BBOX-1247] 乙型肝炎e抗体* & 0.14 & & & & IU/mL & 0-0.20 & \\\\\n[BBOX-1248] 乙型肝炎核心抗体* & 0.27 & & & & IU/mL & 0-0.50 & \\\\\n[BBOX-1249] \\hline\n[BBOX-1250] \\end{tabular}\n[BBOX-1251] \\begin{tabular}{lllllllll}\n[BBOX-1252] 报告时间: 2026-02-28\n[BBOX-1253] \\hline\n[BBOX-1254] & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\\\\n[BBOX-1255] \\hline\n[BBOX-1256] & 丙型肝炎抗体定量* & 0.06 & & & & COI & 0-1 & \\\\\n[BBOX-1257] ST & 不加热血清反应素试验* & 阴性(-) & & & & & 阴性(-) & \\\\\n[BBOX-1258] V & 人免疫缺陷病毒抗体定量* & 0.08 & & & & COI & 0-1 & \\\\\n[BBOX-1259] PA & 梅毒螺旋体抗体定量* & 0.08 & & & & COI & 0-1 & \\\\\n[BBOX-1260] \\hline\n[BBOX-1261] \\end{tabular}\n[BBOX-1262] \\begin{tabular}{ccccccccc}\n[BBOX-1263] 报告时间: 2026-02-28\n[BBOX-1264] \\hline\n[BBOX-1265] 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\\\\n[BBOX-1266] \\hline\n[BBOX-1267] 糖化血红蛋白HbA1c* & 6.40 & & $\\uparrow$ & & \\% & 4.0-6.0 & \\\\\n[BBOX-1268] 糖化血红蛋白HbA1a & 0.50 & & & & \\% & 0-0.91 & \\\\\n[BBOX-1269] 糖化血红蛋白HbA1b & 1.10 & & & & \\% & 0.35-1.82 & \\\\\n[BBOX-1270] \\hline\n[BBOX-1271] \\end{tabular}\n[BBOX-1272] \\begin{tabular}{l c c c c c c c}\n[BBOX-1273] 报告时间: 2026-02-28\n[BBOX-1274] \\hline\n[BBOX-1275] 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历 \\\\\n[BBOX-1276] \\hline\n[BBOX-1277] 凝血酶原时间* & 11.50 & & & & S & 9-15 & \\\\\n[BBOX-1278] 国际标准化比值* & 1.04 & & & & & 0.8-1.4 & \\\\\n[BBOX-1279] 纤维蛋白原* & 4.43 & & & & g/L & 2.00 -5.00 & \\\\\n[BBOX-1280] 活化部分凝血活酶时间* & 32.30 & & & & S & 23.00 -40.00 & \\\\\n[BBOX-1281] 凝血酶时间* & 13.00 & & & & S & 10.3-16.6 & \\\\\n[BBOX-1282] 凝血酶原活动度 & 98 & & & & \\% & 70-130 & \\\\\n[BBOX-1283] D-二聚体定量* & 69 & & & & ng/ml & 0-450 & \\\\\n[BBOX-1284] \\hline\n[BBOX-1285] \\end{tabular}\n[BBOX-1286] \\begin{tabular}{ccccccccc}\n[BBOX-1287] 报告时间: 2026-02-02\n[BBOX-1288] \\hline\n[BBOX-1289] 缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & \\\\\n[BBOX-1290] \\hline\n[BBOX-1291] TBIL & 总胆红素* & 8.7 & & & & \\textmu mol/L & 0-26.0 & \\\\\n[BBOX-1292] DBIL & 直接胆红素* & 3.6 & & & & \\textmu mol/L & 0-6.8 & \\\\\n[BBOX-1293] IBIL & 间接胆红素 & 5.1 & & & & \\textmu mol/L & 3.1-14.3 & \\\\\n[BBOX-1294] DB/TB & 直/总胆比值 & 0.41 & & & & & & \\\\\n[BBOX-1295] TP & 总蛋白\\# & 74.5 & & & & g/L & 65-85 & \\\\\n[BBOX-1296] ALB & 白蛋白* & 39.3 & & \\downarrow & & g/L & 40-55 & \\\\\n[BBOX-1297] GLO & 球蛋白 & 35.2 & & & & g/L & 20-40 & \\\\\n[BBOX-1298] A/G & 白蛋白/球蛋白 & 1.1 & & \\downarrow & & & 1.2-2.4 & \\\\\n[BBOX-1299] GGT & 谷氨酰转肽酶* & 30 & & & & U/L & 10-60 & \\\\\n[BBOX-1300] TBA & 总胆汁酸* & 13.2 & & \\uparrow & & \\textmu mol/L & 0-10 & \\\\\n[BBOX-1301] AST & 天门冬氨酸氨基转移酶* & 15 & & & & U/L & 15-40 & \\\\\n[BBOX-1302] ALT & 丙氨酸氨基转移酶* & 14 & & & & U/L & 9-50 & \\\\\n[BBOX-1303] AST/ALT & 谷草/谷丙比值 & 1.1 & & & & & & \\\\\n[BBOX-1304] ALP & 碱性磷酸酶* & 64 & & & & U/L & 45-125 & \\\\\n[BBOX-1305] PA & 前白蛋白* & 251.5 & & & & mg/L & 200-430 & \\\\\n[BBOX-1306] CHE & 胆碱酯酶* & 8382 & & & & U/L & 5000-12000 & \\\\\n[BBOX-1307] UREA & 尿素* & 6.98 & & & & mmol/L & 3.6-9.5 & \\\\\n[BBOX-1308] CREA & 肌酐* & 136 & & \\uparrow & & \\textmu mol/L & 57-111 & \\\\\n[BBOX-1309] UA & 尿酸* & 551 & & \\uparrow & & \\textmu mol/L & 208-428 & \\\\\n[BBOX-1310] HCO3 & 碳酸氢根* & 21.6 & & \\downarrow & & mmol/L & 22-29 & \\\\\n[BBOX-1311] T-CHO & 总胆固醇* & 3.10 & & & & mmol/L & 3.1-5.7 & \\\\\n[BBOX-1312] \\hline\n[BBOX-1313] \\end{tabular}\n[BBOX-1314] \\begin{tabular}{ccccccccc}\n[BBOX-1315] 报告时间: 2025-04-01\n[BBOX-1316] \\hline\n[BBOX-1317] 缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & \\\\\n[BBOX-1318] \\hline\n[BBOX-1319] CHE & 胆碱酯酶* & 8382 & & & & U/L & 5000-12000 & \\\\\n[BBOX-1320] UREA & 尿素* & 6.98 & & & & mmol/L & 3.6-9.5 & \\\\\n[BBOX-1321] CREA & 肌酐* & 136 & & $\\uparrow$ & & $\\mu$mol/L & 57-111 & \\\\\n[BBOX-1322] UA & 尿酸* & 551 & & $\\uparrow$ & & $\\mu$mol/L & 208-428 & \\\\\n[BBOX-1323] HCO3 & 碳酸氢根* & 21.6 & & $\\downarrow$ & & mmol/L & 22-29 & \\\\\n[BBOX-1324] T-CHO & 总胆固醇* & 3.18 & & & & mmol/L & $<$5.2 & \\\\\n[BBOX-1325] TG & 甘油三酯* & 1.27 & & & & mmol/L & $<$1.7 & \\\\\n[BBOX-1326] LDL-C & 低密度脂蛋白胆固醇* & 1.78 & & & & mmol/L & $<$3.4(低危人群) & \\\\\n[BBOX-1327] GLU & 空腹血葡萄糖* & 4.79 & & & & mmol/L & 3.9-6.1 & \\\\\n[BBOX-1328] K & 钾* & 4.18 & & & & mmol/L & 3.5-5.3 & \\\\\n[BBOX-1329] Na & 钠* & 141.1 & & & & mmol/L & 137-147 & \\\\\n[BBOX-1330] CL & 氯* & 106.4 & & & & mmol/L & 99-110 & \\\\\n[BBOX-1331] Ca & 总钙* & 2.25 & & & & mmol/L & 2.11-2.52 & \\\\\n[BBOX-1332] Mg & 镁* & 0.78 & & & & mmol/L & 0.75-1.02 & \\\\\n[BBOX-1333] P & 磷* & 0.95 & & & & mmol/L & 0.85-1.51 & \\\\\n[BBOX-1334] CK & 肌酸激酶* & 84 & & & & U/L & 50-310 & \\\\\n[BBOX-1335] CK-MB & 肌酸激酶同工酶MB & 13 & & & & U/L & 0-25 & \\\\\n[BBOX-1336] LD & 乳酸脱氢酶* & 167 & & & & U/L & 120-250 & \\\\\n[BBOX-1337] $\\alpha$-HBD & $\\alpha$-羟丁酸脱氢酶* & 109 & & & & U/L & 72-182 & \\\\\n[BBOX-1338] IgE & 免疫球蛋白E* & 1960.6 & & $\\uparrow$ & & IU/ml & $<$100 & \\\\\n[BBOX-1339] \\hline\n[BBOX-1340] \\end{tabular}\n[BBOX-1341] \\begin{tabular}{ccccccccc}\n[BBOX-1342] \\hline\n[BBOX-1343] 缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 \\\\\n[BBOX-1344] \\hline\n[BBOX-1345] WBC & 白细胞计数* & 8.490 & & & & 10~9/L & 3.5-9.5 \\\\\n[BBOX-1346] RBC & 红细胞计数* & 5.81 & & $\\uparrow$ & & 10~12/L & 4.3-5.8 \\\\\n[BBOX-1347] HGB & 血红蛋白* & 157.00 & & & & g/L & 130-175 \\\\\n[BBOX-1348] PLT & 血小板计数* & 268.00 & & & & 10~9/L & 125-350 \\\\\n[BBOX-1349] NEU\\% & 中性粒细胞百分比 & 0.6920 & & & & & 0.4-0.75 \\\\\n[BBOX-1350] LYM\\% & 淋巴细胞百分比 & 0.1970 & & $\\downarrow$ & & & 0.2-0.5 \\\\\n[BBOX-1351] MONO\\% & 单核细胞百分比 & 0.0630 & & & & & 0.03-0.1 \\\\\n[BBOX-1352] EO\\% & 嗜酸性粒细胞百分比 & 0.0450 & & & & & 0.004-0.08 \\\\\n[BBOX-1353] BA SO\\% & 嗜碱性粒细胞百分比 & 0.0030 & & & & & 0-0.01 \\\\\n[BBOX-1354] NEU & 中性粒细胞绝对值 & 5.88 & & & & 10~9/L & 1.8-6.3 \\\\\n[BBOX-1355] LYM & 淋巴细胞绝对值 & 1.67 & & & & 10~9/L & 1.1-3.2 \\\\\n[BBOX-1356] MONO & 单核细胞绝对值 & 0.53 & & & & 10~9/L & 0.1-0.6 \\\\\n[BBOX-1357] EOS & 嗜酸性粒细胞绝对值 & 0.38 & & & & 10~9/L & 0.02-0.52 \\\\\n[BBOX-1358] BA SO & 嗜碱性粒细胞绝对值 & 0.03 & & & & 10~9/L & 0-0.06 \\\\\n[BBOX-1359] MCV & 平均红细胞体积* & 83.70 & & & & fl & 82-100 \\\\\n[BBOX-1360] MCH & 平均RBC血红蛋白含量* & 26.90 & & $\\downarrow$ & & pg & 27-34 \\\\\n[BBOX-1361] MCHC & 平均RBC血红蛋白浓度* & 323.00 & & & & g/L & 316-354 \\\\\n[BBOX-1362] HCT & 红细胞比容* & 0.486 & & & & & 0.4-0.5 \\\\\n[BBOX-1363] RDWCV & RBC体积分布宽度CV & 0.15 & & $\\uparrow$ & & & 0.11-0.14 \\\\\n[BBOX-1364] PDW & 血小板体积分布宽度 & 0.16 & & & & & 0.15-0.18 \\\\\n[BBOX-1365] \\hline\n[BBOX-1366] \\end{tabular}\n[BBOX-1367] \\begin{tabular}{ccccccccc}\n[BBOX-1368] \\hline\n[BBOX-1369] \\multicolumn{1}{c}{\\textbf{缩写}} & \\multicolumn{1}{c}{\\textbf{项目名称}} & \\multicolumn{1}{c}{\\textbf{结果}} & \\multicolumn{1}{c}{\\textbf{结果提示}} & \\multicolumn{1}{c}{\\textbf{异常提示}} & \\multicolumn{1}{c}{\\textbf{辅助诊断}} & \\multicolumn{1}{c}{\\textbf{单位}} & \\multicolumn{1}{c}{\\textbf{参考范围}} \\\\\n[BBOX-1370] \\hline\n[BBOX-1371] FI02 & 吸氧浓度 & 21.00 & & & & \\% & 21-100 \\\\\n[BBOX-1372] T & 体温 & 36.4 & & & & & 29-41 \\\\\n[BBOX-1373] Ca++ & 钙测定 & 1.19 & & & & mmol/L & 1.15-1.29 \\\\\n[BBOX-1374] Na+ & 钠测定 & 143.20 & & & & mmol/L & 136-146 \\\\\n[BBOX-1375] K+ & 钾测定 & 3.98 & & & & mmol/L & 3.5-4.5 \\\\\n[BBOX-1376] p02(a,T)/F02 & 氧合指数(p/f) & 315.0 & & $\\downarrow$ & & & 400-500 \\\\\n[BBOX-1377] BEecf & 红细胞外剩余碱 & -1.80 & & & & mmol/l & -3-3 \\\\\n[BBOX-1378] PH & 酸碱度 (PH) & 7.383 & & & & & 7.35-7.45 \\\\\n[BBOX-1379] pH(T) & pH校正值(pHT) & 7.392 & & & & & 7.35-7.45 \\\\\n[BBOX-1380] pO2 & 氧分压 (pO2) & 66.20 & & $\\downarrow$ & & mmHg & 83-108 \\\\\n[BBOX-1381] pO2(T) & 氧分压校正值 & 63.50 & & $\\downarrow$ & & mmHg & 83-108 \\\\\n[BBOX-1382] pCO2 & 二氧化碳分压 & 39.90 & & & & mmHg & 35-45 \\\\\n[BBOX-1383] PCO2(T) & CO2分压校正 & 38.90 & & & & mmHg & 35-45 \\\\\n[BBOX-1384] Cl- & 氯测定 & 102.00 & & & & mmol/L & 98-106 \\\\\n[BBOX-1385] Hb & 血红蛋白测定(Hb) & 162.00 & & $\\uparrow$ & & g/L & 120-160 \\\\\n[BBOX-1386] F02Hb & 氧合血红蛋白 & 92.0 & & $\\downarrow$ & & \\% & 94-98 \\\\\n[BBOX-1387] MetHb & 高铁血红蛋白 & 0.10 & & & & & \\\\\n[BBOX-1388] s02 & 总血氧饱和度 & 92.9 & & $\\downarrow$ & & \\% & 93-98 \\\\\n[BBOX-1389] COHb & CO红蛋白 & 1.00 & & & & \\% & 0-2 \\\\\n[BBOX-1390] ctCO2 & 血CO2含量 & 24.50 & & & & mmol/L & 24-32 \\\\\n[BBOX-1391] FHHB & 还原血红蛋白 & 6.9 & & & & & \\\\\n[BBOX-1392] \\hline\n[BBOX-1393] \\end{tabular}\n[BBOX-1394] \\begin{tabular}{ccccccccc}\n[BBOX-1395] \\hline\n[BBOX-1396] 缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 \\\\\n[BBOX-1397] \\hline\n[BBOX-1398] PH & 酸碱度 (PH) & 7.383 & & & & & 7.35-7.45 \\\\\n[BBOX-1399] pH(T) & pH校正值(pHT) & 7.392 & & & & & 7.35-7.45 \\\\\n[BBOX-1400] pO2 & 氧分压 (pO2) & 66.20 & & $\\downarrow$ & & mmHg & 83-108 \\\\\n[BBOX-1401] pO2(T) & 氧分压校正值 & 63.50 & & $\\downarrow$ & & mmHg & 83-108 \\\\\n[BBOX-1402] pCO2 & 二氧化碳分压 & 39.90 & & & & mmHg & 35-45 \\\\\n[BBOX-1403] PCO2(T) & CO2分压校正 & 38.90 & & & & mmHg & 35-45 \\\\\n[BBOX-1404] Cl- & 氯测定 & 102.00 & & & & mmol/L & 98-106 \\\\\n[BBOX-1405] Hb & 血红蛋白测定(Hb) & 162.00 & & $\\uparrow$ & & g/L & 120-160 \\\\\n[BBOX-1406] F02Hb & 氧合血红蛋白 & 92.0 & & $\\downarrow$ & & \\% & 94-98 \\\\\n[BBOX-1407] MetHb & 高铁血红蛋白 & 0.10 & & & & & \\\\\n[BBOX-1408] s02 & 总血氧饱和度 & 92.9 & & $\\downarrow$ & & \\% & 93-98 \\\\\n[BBOX-1409] C0Hb & CO红蛋白 & 1.00 & & & & \\% & 0-2 \\\\\n[BBOX-1410] ctCO2 & 血CO2含量 & 24.50 & & & & mmol/L & 24-32 \\\\\n[BBOX-1411] FHHB & 还原血红蛋白 & 6.9 & & & & \\% & 2-7 \\\\\n[BBOX-1412] cHCO3 & 标准碳酸氢根 & 23.00 & & & & mmol/L & 22-26 \\\\\n[BBOX-1413] ABE (BE(B)) & 实际剩余碱 & -1.6 & & & & mmol/L & -3-3 \\\\\n[BBOX-1414] HCO3- & 实际碳酸氢根 & 23.20 & & & & mmol/L & \\\\\n[BBOX-1415] P02(A-a,T)e & 肺泡动脉氧分压差 & 36.0 & & $\\uparrow$ & & mmHg & 10-25 \\\\\n[BBOX-1416] P02(a/A,T) & 动脉与肺泡氧分压比 & 64.0 & & $\\downarrow$ & & \\% & 85-95 \\\\\n[BBOX-1417] RI & 呼吸指数 & 57.0 & & & & & \\\\\n[BBOX-1418] Glu & 葡萄糖测定 & 6.70 & & $\\uparrow$ & & & \\\\\n[BBOX-1419] \\hline\n[BBOX-1420] \\end{tabular}\n[BBOX-1421] 临床诊断：肺癌\n[BBOX-1422] 样本采集时间：2026-03-10\n[BBOX-1423] 检测项目\n[BBOX-1424] 本产品对与肺癌密切相关的68个基因进行高通量测序。检测突变形式为点突变(SNV)、小片段插入缺失(INDEL)、拷贝数变异(CNV)以及融合(FUSION)。通过免疫组化检测PD-L1表达。\n[BBOX-1425] 本报告分析基因变异与靶向药物、化疗药物的相关性，给出靶向药物(FDA/NMPA批准药物、临床试验\n[BBOX-1426] 药物等)、化疗药物的用药提示信息，从而为临床制定治疗方案提供参考信息。\n[BBOX-1427] 注：检测基因列表见附录。\n[BBOX-1428] 检测结果小结\n[BBOX-1429] 检测类型\n[BBOX-1430] 检测结果\n[BBOX-1431] 靶向用药指导\n[BBOX-1432] 共检出3个变异位点,其中3个与靶向药物相关(KRAS\n[BBOX-1433] p.G12V;CDKN2A p.R80*;TP53 p.G279E)\n[BBOX-1434] PD-L1蛋白表达水平\n[BBOX-1435] 使用CSTE1L3N抗体;TPS:<1%, CPS:1\n[BBOX-1436] 化疗药物检测\n[BBOX-1437] 详见“化疗药物检测解析”部分\n[BBOX-1438] 样品总体质量评估\n[BBOX-1439] 合格\n[BBOX-1440] 注:\n[BBOX-1441] 1. 本报告为基因检测结果,基因、药物等信息列举未按照重要性排序。\n[BBOX-1442] 2. 本报告只对本次采集样本负责,如有疑问,请在7个工作日内与我们联系。\n[BBOX-1443] 检测人:\n[BBOX-1444] 张紫叶\n[BBOX-1445] 复核人:\n[BBOX-1446] 王建丽\n[BBOX-1447] 日期:\n[BBOX-1448] 2026-03-16\n[BBOX-1449] 日期:\n[BBOX-1450] 2026-03-16\n[BBOX-1451] 1/26\n[BBOX-1452] 孔令祈 Novogene\n[BBOX-1453] 诺禾致源\n[BBOX-1454] 肺癌精准诊疗相关基因结果汇总\n[BBOX-1455] 基因\n[BBOX-1456] 变异类型\n[BBOX-1457] 检测结果\n[BBOX-1458] 变异丰度/拷贝数\n[BBOX-1459] ALK\n[BBOX-1460] 突变/融合\n[BBOX-1461] 未检测到与用药相关突变\n[BBOX-1462] BRAF\n[BBOX-1463] 突变/融合\n[BBOX-1464] 未检测到与用药相关突变\n[BBOX-1465] BRCA1\n[BBOX-1466] 突变/缺失\n[BBOX-1467] 未检测到与用药相关突变\n[BBOX-1468] BRCA2\n[BBOX-1469] 突变/缺失\n[BBOX-1470] 未检测到与用药相关突变\n[BBOX-1471] EGFR\n[BBOX-1472] 突变\n[BBOX-1473] 未检测到与用药相关突变\n[BBOX-1474] ERBB2(HER2)\n[BBOX-1475] 突变/扩增\n[BBOX-1476] 未检测到与用药相关突变\n[BBOX-1477] FGFR2\n[BBOX-1478] 突变/融合\n[BBOX-1479] 未检测到与用药相关突变\n[BBOX-1480] FGFR3\n[BBOX-1481] 突变/融合\n[BBOX-1482] 未检测到与用药相关突变\n[BBOX-1483] KIT\n[BBOX-1484] 突变\n[BBOX-1485] 未检测到与用药相关突变\n[BBOX-1486] KRAS\n[BBOX-1487] 突变\n[BBOX-1488] NM_033360.4 exon2 c.35G>T p.G12V\n[BBOX-1489] 35.80%\n[BBOX-1490] MET\n[BBOX-1491] 突变/扩增/14号外\n[BBOX-1492] 未检测到与用药相关突变\n[BBOX-1493] 显子跳跃\n[BBOX-1494] NRG1\n[BBOX-1495] 融合\n[BBOX-1496] 未检测到与用药相关突变\n[BBOX-1497] NTRK1\n[BBOX-1498] 融合\n[BBOX-1499] 未检测到与用药相关突变\n[BBOX-1500] 广西金域医学检验实验室\n[BBOX-1501] 本报告单经过电子签名认证\n[BBOX-1502] Guangxi Kingmed Center for Clinical Laboratory\n[BBOX-1503] 金域医学\n[BBOX-1504] KingMed Diagnostics\n[BBOX-1505] 病理诊断报告书\n[BBOX-1506] 1/1\n[BBOX-1507] 标本条码\n[BBOX-1508] 1223023095\n[BBOX-1509] 医院\n[BBOX-1510] 广西医科大学第一附属医院\n[BBOX-1511] 病人姓名\n[BBOX-1512] 孔令祈\n[BBOX-1513] 科室\n[BBOX-1514] 老年呼吸\n[BBOX-1515] 病理号\n[BBOX-1516] 26018339\n[BBOX-1517] 性别\n[BBOX-1518] 男\n[BBOX-1519] 房/床号\n[BBOX-1520] 49\n[BBOX-1521] 住院门诊号\n[BBOX-1522] 1959880\n[BBOX-1523] 年龄\n[BBOX-1524] 67岁\n[BBOX-1525] 接收时间\n[BBOX-1526] 2026-03-08 14:15:50\n[BBOX-1527] 申请医生\n[BBOX-1528] 项目名称\n[BBOX-1529] 免疫组化8项\n[BBOX-1530] 送检材料\n[BBOX-1531] 肺组织\n[BBOX-1532] 临床诊断\n[BBOX-1533] 患者电话\n[BBOX-1534] 大体描述:\n[BBOX-1535] 福尔马林固定标本，核对送检标本、病人姓名和条形码与申请单一致。\n[BBOX-1536] 灰红条索状组织3段，长0.5-1.8cm，直径均0.05cm。取1盒全（共1盒蜡块）\n[BBOX-1537] 镜下所见：\n[BBOX-1538] 诊断意见：\n[BBOX-1539] 肺组织穿刺活检：\n[BBOX-1540] -结合免疫组化，符合浸润性黏液型腺癌，请结合临床。\n[BBOX-1541] -免疫组化：CK7（+），CK20（+），Villin（+），TTF-1（散在+），NapsinA（散在+），P40（-），CDX2（-），Ki67（\n[BBOX-1542] 热点区约60%+）。\n[BBOX-1543] 报告医师：陈明坚\n[BBOX-1544] 本检测仅对送检负责，如果对结果有疑义，请在报告发布后7天内与我们联系，多谢合作！\n[BBOX-1545] 收样点：广西医科大学第一附属医院-呼吸内\n[BBOX-1546] 科\n[BBOX-1547] 主检实验室：广西金域\n[BBOX-1548] 地址：南宁市西乡塘区总部路3号中国-东盟科技企业孵化基地二期1号厂房一、三、\n[BBOX-1549] 四层\n[BBOX-1550] 报告专用章\n[BBOX-1551] 网址：www.kingmed.com.cn\n[BBOX-1552] GX003SCEJL7RJLY\n[BBOX-1553] 报告日期：2026-03-10 21:16:16\n[BBOX-1554] 更多报告服务\n[BBOX-1555] CS 扫描全能王\n[BBOX-1556] 3亿人都在用的扫描App"
  }
]
2026-08-07 04:46:22,232 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:46:22.230+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:46:52,292 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:46:52.291+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:46:53,112 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:46:53,139 INFO     29 [SmartSplitter] SmartSplitter done: 18 chunks from 18 LLM segments (all bbox_id). Types: {'AdmissionRecord': 1, 'ExaminationReport': 6, 'LabReport': 11}
2026-08-07 04:46:53,151 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-07 04:46:53,151 INFO     29 [Trace] task=26a40982 | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "1557 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks": "18 items, types={'AdmissionRecord': 1, 'ExaminationReport': 6, 'LabReport': 11}"}
2026-08-07 04:46:53,151 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-07 04:46:53,153 INFO     29 [ChunkRouter] Routed 18 chunks into 3 groups: {'chunks_Admission': 1, 'chunks_Examination': 6, 'chunks_LabExam': 11}
2026-08-07 04:46:53,164 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-07 04:46:53,164 INFO     29 [Trace] task=26a40982 | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | ChunkRouter:Router | outputs={"html": "", "json": "1557 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks": "18 items, types={'AdmissionRecord': 1, 'ExaminationReport': 6, 'LabReport': 11}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 11}"}
2026-08-07 04:46:53,165 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-07 04:46:53,169 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-07 04:46:53,169 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[14]
2026-08-07 04:46:53,169 INFO     29 [qwen-vl-table] positions ： [[14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0]]
2026-08-07 04:46:53,581 INFO     29 [qwen-vl-table] page=14, rect=842x595, img=(2339x1653)
2026-08-07 04:46:53,581 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:46:53,581 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 1232, \"bbox_end\": 1238, \"encounter_dates\": [\"2026-02-28\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "报告时间: 2026-02-28\n\\hline\n缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\\\\n\\hline\nTB-DNA & 结核杆菌DNA* & $<$5.00E+02 & & & & 拷贝 & $<$5.00E+02 & $<$5.00E+02 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-07 04:46:55,048 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:46:55,049 INFO     29 [qwen-vl-table] page=14 LLM output (len=228):
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
2026-08-07 04:46:55,049 INFO     29 [qwen-vl-table] coord grouping: {14: 1}
2026-08-07 04:46:55,059 INFO     29 [qwen-vl-table] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3493919, prompt_len=515
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
2026-08-07 04:46:57,247 INFO     29 [qwen-vl-table] coord API raw response (len=67):
```json
[
	{"text": "结核杆菌DNA*", "bbox": [228, 258, 298, 275]}
]
```
2026-08-07 04:46:57,248 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=2.2s
2026-08-07 04:46:57,248 INFO     29 [qwen-vl-table] coord item[0]: text=结核杆菌DNA*, bbox=[228, 258, 298, 275]
2026-08-07 04:46:57,249 INFO     29 [qwen-vl-table] page=14 coord: matched 1/1, time=2.2s
2026-08-07 04:46:57,249 INFO     29 [qwen-vl-table] new_positions (1):
[[15, 191.976, 250.916, 153.51, 163.625]]
2026-08-07 04:46:57,249 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=4.1s
2026-08-07 04:46:57,251 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-07 04:46:57,251 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[15]
2026-08-07 04:46:57,251 INFO     29 [qwen-vl-table] positions ： [[15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0]]
2026-08-07 04:46:57,710 INFO     29 [qwen-vl-table] page=15, rect=842x595, img=(2339x1653)
2026-08-07 04:46:57,710 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:46:57,710 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 1239, \"bbox_end\": 1250, \"encounter_dates\": [\"2026-02-28\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2026-02-28\n\\hline\n项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\\\\n\\hline\n乙型肝炎表面抗原* & 0.00 & & & & IU/ml & 0-0.08 & \\\\\n乙型肝炎表面抗体* & 14.85 & & $\\uparrow$ & & mIU/mL & 0-10 & \\\\\n乙型肝炎e抗原* & 0.00 & & & & PElu/ml & 0-0.10 & \\\\\n乙型肝炎e抗体* & 0.14 & & & & IU/mL & 0-0.20 & \\\\\n乙型肝炎核心抗体* & 0.27 & & & & IU/mL & 0-0.50 & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-07 04:47:01,160 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:47:01,160 INFO     29 [qwen-vl-table] page=15 LLM output (len=899):
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
2026-08-07 04:47:01,160 INFO     29 [qwen-vl-table] coord grouping: {15: 5}
2026-08-07 04:47:01,182 INFO     29 [qwen-vl-table] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5124959, prompt_len=554
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
2026-08-07 04:47:04,811 INFO     29 [qwen-vl-table] coord API raw response (len=270):
[
	{"text": "乙型肝炎表面抗原*", "bbox": [124, 250, 207, 266]},
	{"text": "乙型肝炎表面抗体*", "bbox": [124, 283, 207, 299]},
	{"text": "乙型肝炎e抗原*", "bbox": [132, 317, 201, 333]},
	{"text": "乙型肝炎e抗体*", "bbox": [132, 350, 201, 366]},
	{"text": "乙型肝炎核心抗体*", "bbox": [127, 383, 208, 399]}
]
2026-08-07 04:47:04,811 INFO     29 [qwen-vl-table] coord API: raw_items=5, valid_items=5, elapsed=3.6s
2026-08-07 04:47:04,811 INFO     29 [qwen-vl-table] coord item[0]: text=乙型肝炎表面抗原*, bbox=[124, 250, 207, 266]
2026-08-07 04:47:04,811 INFO     29 [qwen-vl-table] coord item[1]: text=乙型肝炎表面抗体*, bbox=[124, 283, 207, 299]
2026-08-07 04:47:04,811 INFO     29 [qwen-vl-table] coord item[2]: text=乙型肝炎e抗原*, bbox=[132, 317, 201, 333]
2026-08-07 04:47:04,811 INFO     29 [qwen-vl-table] coord item[3]: text=乙型肝炎e抗体*, bbox=[132, 350, 201, 366]
2026-08-07 04:47:04,811 INFO     29 [qwen-vl-table] coord item[4]: text=乙型肝炎核心抗体*, bbox=[127, 383, 208, 399]
2026-08-07 04:47:04,812 INFO     29 [qwen-vl-table] page=15 coord: matched 5/5, time=3.6s
2026-08-07 04:47:04,812 INFO     29 [qwen-vl-table] new_positions (5):
[[16, 104.408, 174.29399999999998, 148.75, 158.26999999999998], [16, 104.408, 174.29399999999998, 168.385, 177.905], [16, 111.14399999999999, 169.242, 188.61499999999998, 198.135], [16, 111.14399999999999, 169.242, 208.25, 217.76999999999998], [16, 106.934, 175.136, 227.885, 237.405]]
2026-08-07 04:47:04,812 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=5, matched=5, pages=1, time=7.6s
2026-08-07 04:47:04,814 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-07 04:47:04,814 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[16]
2026-08-07 04:47:04,814 INFO     29 [qwen-vl-table] positions ： [[16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0]]
2026-08-07 04:47:05,046 INFO     29 [qwen-vl-table] page=16, rect=842x595, img=(2339x1653)
2026-08-07 04:47:05,046 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:47:05,046 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 1251, \"bbox_end\": 1261, \"encounter_dates\": [\"2026-02-28\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{lllllllll}\n报告时间: 2026-02-28\n\\hline\n& 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\\\\n\\hline\n& 丙型肝炎抗体定量* & 0.06 & & & & COI & 0-1 & \\\\\nST & 不加热血清反应素试验* & 阴性(-) & & & & & 阴性(-) & \\\\\nV & 人免疫缺陷病毒抗体定量* & 0.08 & & & & COI & 0-1 & \\\\\nPA & 梅毒螺旋体抗体定量* & 0.08 & & & & COI & 0-1 & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-07 04:47:07,889 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:47:07,889 INFO     29 [qwen-vl-table] page=16 LLM output (len=717):
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
      "item_code": "ST",
      "value": "阴性(-)",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": false
    },
    {
      "name": "人免疫缺陷病毒抗体定量*",
      "item_code": "V",
      "value": "0.08",
      "unit": "COI",
      "reference_range": "0-1",
      "abnormal": false
    },
    {
      "name": "梅毒螺旋体抗体定量*",
      "item_code": "PA",
      "value": "0.08",
      "unit": "COI",
      "reference_range": "0-1",
      "abnormal": false
    }
  ]
}
2026-08-07 04:47:07,890 INFO     29 [qwen-vl-table] coord grouping: {16: 4}
2026-08-07 04:47:07,903 INFO     29 [qwen-vl-table] coord API call start, page=16, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4759042, prompt_len=552
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
2026-08-07 04:47:11,391 INFO     29 [qwen-vl-table] coord API raw response (len=236):
```json
[
	{"text": "丙型肝炎抗体定量*", "bbox": [164, 254, 247, 270]},
	{"text": "不加热血清反应素试验*", "bbox": [155, 289, 256, 304]},
	{"text": "人免疫缺陷病毒抗体定量*", "bbox": [152, 322, 261, 338]},
	{"text": "梅毒螺旋体抗体定量*", "bbox": [161, 356, 252, 371]}
]
```
2026-08-07 04:47:11,391 INFO     29 [qwen-vl-table] coord API: raw_items=4, valid_items=4, elapsed=3.5s
2026-08-07 04:47:11,391 INFO     29 [qwen-vl-table] coord item[0]: text=丙型肝炎抗体定量*, bbox=[164, 254, 247, 270]
2026-08-07 04:47:11,391 INFO     29 [qwen-vl-table] coord item[1]: text=不加热血清反应素试验*, bbox=[155, 289, 256, 304]
2026-08-07 04:47:11,391 INFO     29 [qwen-vl-table] coord item[2]: text=人免疫缺陷病毒抗体定量*, bbox=[152, 322, 261, 338]
2026-08-07 04:47:11,391 INFO     29 [qwen-vl-table] coord item[3]: text=梅毒螺旋体抗体定量*, bbox=[161, 356, 252, 371]
2026-08-07 04:47:11,392 INFO     29 [qwen-vl-table] page=16 coord: matched 4/4, time=3.5s
2026-08-07 04:47:11,392 INFO     29 [qwen-vl-table] new_positions (4):
[[17, 138.088, 207.974, 151.13, 160.65], [17, 130.51, 215.552, 171.95499999999998, 180.88], [17, 127.984, 219.762, 191.59, 201.10999999999999], [17, 135.56199999999998, 212.184, 211.82, 220.74499999999998]]
2026-08-07 04:47:11,392 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=4, matched=4, pages=1, time=6.6s
2026-08-07 04:47:11,393 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-07 04:47:11,394 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[17]
2026-08-07 04:47:11,394 INFO     29 [qwen-vl-table] positions ： [[17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0]]
2026-08-07 04:47:11,822 INFO     29 [qwen-vl-table] page=17, rect=842x595, img=(2339x1653)
2026-08-07 04:47:11,823 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:47:11,823 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 1262, \"bbox_end\": 1271, \"encounter_dates\": [\"2026-02-28\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2026-02-28\n\\hline\n项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历次 \\\\\n\\hline\n糖化血红蛋白HbA1c* & 6.40 & & $\\uparrow$ & & \\% & 4.0-6.0 & \\\\\n糖化血红蛋白HbA1a & 0.50 & & & & \\% & 0-0.91 & \\\\\n糖化血红蛋白HbA1b & 1.10 & & & & \\% & 0.35-1.82 & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-07 04:47:14,465 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:47:14,466 INFO     29 [qwen-vl-table] page=17 LLM output (len=567):
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
2026-08-07 04:47:14,466 INFO     29 [qwen-vl-table] coord grouping: {17: 3}
2026-08-07 04:47:14,480 INFO     29 [qwen-vl-table] coord API call start, page=17, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4492034, prompt_len=543
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
2026-08-07 04:47:17,663 INFO     29 [qwen-vl-table] coord API raw response (len=183):
```json
[
	{"text": "糖化血红蛋白HbA1c*", "bbox": [147, 263, 245, 279]},
	{"text": "糖化血红蛋白HbA1a", "bbox": [148, 297, 243, 312]},
	{"text": "糖化血红蛋白HbA1b", "bbox": [147, 330, 243, 346]}
]
```
2026-08-07 04:47:17,663 INFO     29 [qwen-vl-table] coord API: raw_items=3, valid_items=3, elapsed=3.2s
2026-08-07 04:47:17,663 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白HbA1c*, bbox=[147, 263, 245, 279]
2026-08-07 04:47:17,663 INFO     29 [qwen-vl-table] coord item[1]: text=糖化血红蛋白HbA1a, bbox=[148, 297, 243, 312]
2026-08-07 04:47:17,663 INFO     29 [qwen-vl-table] coord item[2]: text=糖化血红蛋白HbA1b, bbox=[147, 330, 243, 346]
2026-08-07 04:47:17,665 INFO     29 [qwen-vl-table] page=17 coord: matched 3/3, time=3.2s
2026-08-07 04:47:17,665 INFO     29 [qwen-vl-table] new_positions (3):
[[18, 123.774, 206.29, 156.48499999999999, 166.005], [18, 124.616, 204.606, 176.715, 185.64], [18, 123.774, 204.606, 196.35, 205.87]]
2026-08-07 04:47:17,666 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=3, matched=3, pages=1, time=6.3s
2026-08-07 04:47:17,669 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-07 04:47:17,669 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[18]
2026-08-07 04:47:17,669 INFO     29 [qwen-vl-table] positions ： [[18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0]]
2026-08-07 04:47:18,121 INFO     29 [qwen-vl-table] page=18, rect=842x595, img=(2339x1653)
2026-08-07 04:47:18,122 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:47:18,122 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 1272, \"bbox_end\": 1285, \"encounter_dates\": [\"2026-02-28\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l c c c c c c c}\n报告时间: 2026-02-28\n\\hline\n项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & 历 \\\\\n\\hline\n凝血酶原时间* & 11.50 & & & & S & 9-15 & \\\\\n国际标准化比值* & 1.04 & & & & & 0.8-1.4 & \\\\\n纤维蛋白原* & 4.43 & & & & g/L & 2.00 -5.00 & \\\\\n活化部分凝血活酶时间* & 32.30 & & & & S & 23.00 -40.00 & \\\\\n凝血酶时间* & 13.00 & & & & S & 10.3-16.6 & \\\\\n凝血酶原活动度 & 98 & & & & \\% & 70-130 & \\\\\nD-二聚体定量* & 69 & & & & ng/ml & 0-450 & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-07 04:47:22,069 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:47:22.068+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:47:22,639 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:47:22,639 INFO     29 [qwen-vl-table] page=18 LLM output (len=1211):
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
      "reference_range": "2.00-5.00",
      "abnormal": false
    },
    {
      "name": "活化部分凝血活酶时间",
      "item_code": null,
      "value": "32.30",
      "unit": "S",
      "reference_range": "23.00-40.00",
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
2026-08-07 04:47:22,639 INFO     29 [qwen-vl-table] coord grouping: {18: 7}
2026-08-07 04:47:22,656 INFO     29 [qwen-vl-table] coord API call start, page=18, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4503128, prompt_len=560
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
2026-08-07 04:47:27,270 INFO     29 [qwen-vl-table] coord API raw response (len=364):
[
	{"text": "凝血酶原时间", "bbox": [176, 261, 241, 277]},
	{"text": "国际标准化比值", "bbox": [171, 295, 245, 311]},
	{"text": "纤维蛋白原", "bbox": [181, 329, 236, 345]},
	{"text": "活化部分凝血活酶时间", "bbox": [157, 363, 261, 379]},
	{"text": "凝血酶时间", "bbox": [182, 397, 237, 413]},
	{"text": "凝血酶原活动度", "bbox": [175, 430, 246, 446]},
	{"text": "D-二聚体定量", "bbox": [177, 464, 245, 480]}
]
2026-08-07 04:47:27,270 INFO     29 [qwen-vl-table] coord API: raw_items=7, valid_items=7, elapsed=4.6s
2026-08-07 04:47:27,270 INFO     29 [qwen-vl-table] coord item[0]: text=凝血酶原时间, bbox=[176, 261, 241, 277]
2026-08-07 04:47:27,270 INFO     29 [qwen-vl-table] coord item[1]: text=国际标准化比值, bbox=[171, 295, 245, 311]
2026-08-07 04:47:27,270 INFO     29 [qwen-vl-table] coord item[2]: text=纤维蛋白原, bbox=[181, 329, 236, 345]
2026-08-07 04:47:27,270 INFO     29 [qwen-vl-table] coord item[3]: text=活化部分凝血活酶时间, bbox=[157, 363, 261, 379]
2026-08-07 04:47:27,270 INFO     29 [qwen-vl-table] coord item[4]: text=凝血酶时间, bbox=[182, 397, 237, 413]
2026-08-07 04:47:27,270 INFO     29 [qwen-vl-table] coord item[5]: text=凝血酶原活动度, bbox=[175, 430, 246, 446]
2026-08-07 04:47:27,270 INFO     29 [qwen-vl-table] coord item[6]: text=D-二聚体定量, bbox=[177, 464, 245, 480]
2026-08-07 04:47:27,271 INFO     29 [qwen-vl-table] page=18 coord: matched 7/7, time=4.6s
2026-08-07 04:47:27,272 INFO     29 [qwen-vl-table] new_positions (7):
[[19, 148.192, 202.922, 155.295, 164.815], [19, 143.982, 206.29, 175.525, 185.045], [19, 152.402, 198.712, 195.755, 205.27499999999998], [19, 132.194, 219.762, 215.98499999999999, 225.505], [19, 153.244, 199.554, 236.215, 245.73499999999999], [19, 147.35, 207.132, 255.85, 265.37], [19, 149.034, 206.29, 276.08, 285.59999999999997]]
2026-08-07 04:47:27,272 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=7, matched=7, pages=1, time=9.6s
2026-08-07 04:47:27,276 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-07 04:47:27,276 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[19]
2026-08-07 04:47:27,276 INFO     29 [qwen-vl-table] positions ： [[19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0]]
2026-08-07 04:47:27,737 INFO     29 [qwen-vl-table] page=19, rect=842x595, img=(2339x1653)
2026-08-07 04:47:27,737 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:47:27,738 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 1286, \"bbox_end\": 1313, \"encounter_dates\": [\"2026-02-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2026-02-02\n\\hline\n缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & \\\\\n\\hline\nTBIL & 总胆红素* & 8.7 & & & & \\textmu mol/L & 0-26.0 & \\\\\nDBIL & 直接胆红素* & 3.6 & & & & \\textmu mol/L & 0-6.8 & \\\\\nIBIL & 间接胆红素 & 5.1 & & & & \\textmu mol/L & 3.1-14.3 & \\\\\nDB/TB & 直/总胆比值 & 0.41 & & & & & & \\\\\nTP & 总蛋白\\# & 74.5 & & & & g/L & 65-85 & \\\\\nALB & 白蛋白* & 39.3 & & \\downarrow & & g/L & 40-55 & \\\\\nGLO & 球蛋白 & 35.2 & & & & g/L & 20-40 & \\\\\nA/G & 白蛋白/球蛋白 & 1.1 & & \\downarrow & & & 1.2-2.4 & \\\\\nGGT & 谷氨酰转肽酶* & 30 & & & & U/L & 10-60 & \\\\\nTBA & 总胆汁酸* & 13.2 & & \\uparrow & & \\textmu mol/L & 0-10 & \\\\\nAST & 天门冬氨酸氨基转移酶* & 15 & & & & U/L & 15-40 & \\\\\nALT & 丙氨酸氨基转移酶* & 14 & & & & U/L & 9-50 & \\\\\nAST/ALT & 谷草/谷丙比值 & 1.1 & & & & & & \\\\\nALP & 碱性磷酸酶* & 64 & & & & U/L & 45-125 & \\\\\nPA & 前白蛋白* & 251.5 & & & & mg/L & 200-430 & \\\\\nCHE & 胆碱酯酶* & 8382 & & & & U/L & 5000-12000 & \\\\\nUREA & 尿素* & 6.98 & & & & mmol/L & 3.6-9.5 & \\\\\nCREA & 肌酐* & 136 & & \\uparrow & & \\textmu mol/L & 57-111 & \\\\\nUA & 尿酸* & 551 & & \\uparrow & & \\textmu mol/L & 208-428 & \\\\\nHCO3 & 碳酸氢根* & 21.6 & & \\downarrow & & mmol/L & 22-29 & \\\\\nT-CHO & 总胆固醇* & 3.10 & & & & mmol/L & 3.1-5.7 & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-07 04:47:40,739 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:47:40,739 INFO     29 [qwen-vl-table] page=19 LLM output (len=3562):
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
2026-08-07 04:47:40,739 INFO     29 [qwen-vl-table] coord grouping: {19: 21}
2026-08-07 04:47:40,784 INFO     29 [qwen-vl-table] coord API call start, page=19, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5840961, prompt_len=641
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
2026-08-07 04:47:49,633 INFO     29 [qwen-vl-table] coord API raw response (len=1061):
[
	{"text": "总胆红素*", "bbox": [235, 244, 278, 258]},
	{"text": "直接胆红素*", "bbox": [230, 277, 282, 290]},
	{"text": "间接胆红素", "bbox": [232, 310, 280, 324]},
	{"text": "直/总胆比值", "bbox": [229, 343, 282, 357]},
	{"text": "总蛋白#", "bbox": [239, 376, 273, 390]},
	{"text": "白蛋白*", "bbox": [240, 409, 272, 423]},
	{"text": "球蛋白", "bbox": [241, 442, 270, 456]},
	{"text": "白蛋白/球蛋白", "bbox": [225, 475, 288, 489]},
	{"text": "谷氨酰转肽酶*", "bbox": [225, 508, 288, 522]},
	{"text": "总胆汁酸*", "bbox": [236, 540, 278, 554]},
	{"text": "天门冬氨酸氨基转移酶*", "bbox": [207, 573, 308, 587]},
	{"text": "丙氨酸氨基转移酶*", "bbox": [217, 606, 298, 620]},
	{"text": "谷草/谷丙比值", "bbox": [227, 639, 290, 653]},
	{"text": "碱性磷酸酶*", "bbox": [232, 672, 284, 686]},
	{"text": "前白蛋白*", "bbox": [238, 705, 280, 719]},
	{"text": "胆碱酯酶*", "bbox": [238, 737, 280, 751]},
	{"text": "尿素*", "bbox": [248, 769, 270, 783]},
	{"text": "肌酐*", "bbox": [248, 802, 270, 816]},
	{"text": "尿酸*", "bbox": [250, 835, 272, 849]},
	{"text": "碳酸氢根*", "bbox": [240, 867, 281, 881]},
	{"text": "总胆固醇*", "bbox": [235, 900, 282, 913]}
]
2026-08-07 04:47:49,633 INFO     29 [qwen-vl-table] coord API: raw_items=21, valid_items=21, elapsed=8.8s
2026-08-07 04:47:49,633 INFO     29 [qwen-vl-table] coord item[0]: text=总胆红素*, bbox=[235, 244, 278, 258]
2026-08-07 04:47:49,633 INFO     29 [qwen-vl-table] coord item[1]: text=直接胆红素*, bbox=[230, 277, 282, 290]
2026-08-07 04:47:49,633 INFO     29 [qwen-vl-table] coord item[2]: text=间接胆红素, bbox=[232, 310, 280, 324]
2026-08-07 04:47:49,633 INFO     29 [qwen-vl-table] coord item[3]: text=直/总胆比值, bbox=[229, 343, 282, 357]
2026-08-07 04:47:49,633 INFO     29 [qwen-vl-table] coord item[4]: text=总蛋白#, bbox=[239, 376, 273, 390]
2026-08-07 04:47:49,633 INFO     29 [qwen-vl-table] coord item[5]: text=白蛋白*, bbox=[240, 409, 272, 423]
2026-08-07 04:47:49,633 INFO     29 [qwen-vl-table] coord item[6]: text=球蛋白, bbox=[241, 442, 270, 456]
2026-08-07 04:47:49,633 INFO     29 [qwen-vl-table] coord item[7]: text=白蛋白/球蛋白, bbox=[225, 475, 288, 489]
2026-08-07 04:47:49,633 INFO     29 [qwen-vl-table] coord item[8]: text=谷氨酰转肽酶*, bbox=[225, 508, 288, 522]
2026-08-07 04:47:49,633 INFO     29 [qwen-vl-table] coord item[9]: text=总胆汁酸*, bbox=[236, 540, 278, 554]
2026-08-07 04:47:49,633 INFO     29 [qwen-vl-table] coord item[10]: text=天门冬氨酸氨基转移酶*, bbox=[207, 573, 308, 587]
2026-08-07 04:47:49,634 INFO     29 [qwen-vl-table] coord item[11]: text=丙氨酸氨基转移酶*, bbox=[217, 606, 298, 620]
2026-08-07 04:47:49,634 INFO     29 [qwen-vl-table] coord item[12]: text=谷草/谷丙比值, bbox=[227, 639, 290, 653]
2026-08-07 04:47:49,634 INFO     29 [qwen-vl-table] coord item[13]: text=碱性磷酸酶*, bbox=[232, 672, 284, 686]
2026-08-07 04:47:49,634 INFO     29 [qwen-vl-table] coord item[14]: text=前白蛋白*, bbox=[238, 705, 280, 719]
2026-08-07 04:47:49,634 INFO     29 [qwen-vl-table] coord item[15]: text=胆碱酯酶*, bbox=[238, 737, 280, 751]
2026-08-07 04:47:49,634 INFO     29 [qwen-vl-table] coord item[16]: text=尿素*, bbox=[248, 769, 270, 783]
2026-08-07 04:47:49,634 INFO     29 [qwen-vl-table] coord item[17]: text=肌酐*, bbox=[248, 802, 270, 816]
2026-08-07 04:47:49,634 INFO     29 [qwen-vl-table] coord item[18]: text=尿酸*, bbox=[250, 835, 272, 849]
2026-08-07 04:47:49,634 INFO     29 [qwen-vl-table] coord item[19]: text=碳酸氢根*, bbox=[240, 867, 281, 881]
2026-08-07 04:47:49,634 INFO     29 [qwen-vl-table] coord item[20]: text=总胆固醇*, bbox=[235, 900, 282, 913]
2026-08-07 04:47:49,637 INFO     29 [qwen-vl-table] page=19 coord: matched 21/21, time=8.8s
2026-08-07 04:47:49,637 INFO     29 [qwen-vl-table] new_positions (21):
[[20, 197.87, 234.076, 145.18, 153.51], [20, 193.66, 237.444, 164.815, 172.54999999999998], [20, 195.344, 235.76, 184.45, 192.78], [20, 192.81799999999998, 237.444, 204.08499999999998, 212.415], [20, 201.238, 229.86599999999999, 223.72, 232.04999999999998], [20, 202.07999999999998, 229.024, 243.355, 251.685], [20, 202.922, 227.34, 262.99, 271.32], [20, 189.45, 242.49599999999998, 282.625, 290.955], [20, 189.45, 242.49599999999998, 302.26, 310.59], [20, 198.712, 234.076, 321.3, 329.63], [20, 174.29399999999998, 259.336, 340.935, 349.265], [20, 182.714, 250.916, 360.57, 368.9], [20, 191.134, 244.17999999999998, 380.205, 388.53499999999997], [20, 195.344, 239.128, 399.84, 408.16999999999996], [20, 200.396, 235.76, 419.47499999999997, 427.805], [20, 200.396, 235.76, 438.515, 446.84499999999997], [20, 208.816, 227.34, 457.555, 465.885], [20, 208.816, 227.34, 477.19, 485.52], [20, 210.5, 229.024, 496.825, 505.155], [20, 202.07999999999998, 236.602, 515.865, 524.1949999999999], [20, 197.87, 237.444, 535.5, 543.235]]
2026-08-07 04:47:49,637 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=21, matched=21, pages=1, time=22.4s
2026-08-07 04:47:49,643 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-07 04:47:49,643 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[20]
2026-08-07 04:47:49,644 INFO     29 [qwen-vl-table] positions ： [[20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0]]
2026-08-07 04:47:50,139 INFO     29 [qwen-vl-table] page=20, rect=842x595, img=(2339x1653)
2026-08-07 04:47:50,140 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:47:50,140 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 1314, \"bbox_end\": 1340, \"encounter_dates\": [\"2025-04-01\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2025-04-01\n\\hline\n缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 & \\\\\n\\hline\nCHE & 胆碱酯酶* & 8382 & & & & U/L & 5000-12000 & \\\\\nUREA & 尿素* & 6.98 & & & & mmol/L & 3.6-9.5 & \\\\\nCREA & 肌酐* & 136 & & $\\uparrow$ & & $\\mu$mol/L & 57-111 & \\\\\nUA & 尿酸* & 551 & & $\\uparrow$ & & $\\mu$mol/L & 208-428 & \\\\\nHCO3 & 碳酸氢根* & 21.6 & & $\\downarrow$ & & mmol/L & 22-29 & \\\\\nT-CHO & 总胆固醇* & 3.18 & & & & mmol/L & $<$5.2 & \\\\\nTG & 甘油三酯* & 1.27 & & & & mmol/L & $<$1.7 & \\\\\nLDL-C & 低密度脂蛋白胆固醇* & 1.78 & & & & mmol/L & $<$3.4(低危人群) & \\\\\nGLU & 空腹血葡萄糖* & 4.79 & & & & mmol/L & 3.9-6.1 & \\\\\nK & 钾* & 4.18 & & & & mmol/L & 3.5-5.3 & \\\\\nNa & 钠* & 141.1 & & & & mmol/L & 137-147 & \\\\\nCL & 氯* & 106.4 & & & & mmol/L & 99-110 & \\\\\nCa & 总钙* & 2.25 & & & & mmol/L & 2.11-2.52 & \\\\\nMg & 镁* & 0.78 & & & & mmol/L & 0.75-1.02 & \\\\\nP & 磷* & 0.95 & & & & mmol/L & 0.85-1.51 & \\\\\nCK & 肌酸激酶* & 84 & & & & U/L & 50-310 & \\\\\nCK-MB & 肌酸激酶同工酶MB & 13 & & & & U/L & 0-25 & \\\\\nLD & 乳酸脱氢酶* & 167 & & & & U/L & 120-250 & \\\\\n$\\alpha$-HBD & $\\alpha$-羟丁酸脱氢酶* & 109 & & & & U/L & 72-182 & \\\\\nIgE & 免疫球蛋白E* & 1960.6 & & $\\uparrow$ & & IU/ml & $<$100 & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-07 04:47:51,898 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:47:51.897+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:48:02,872 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:48:02,872 INFO     29 [qwen-vl-table] page=20 LLM output (len=3420):
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
      "unit": "$\\mu$mol/L",
      "reference_range": "57-111",
      "abnormal": true
    },
    {
      "name": "尿酸*",
      "item_code": "UA",
      "value": "551",
      "unit": "$\\mu$mol/L",
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
      "name": "$\\alpha$-羟丁酸脱氢酶*",
      "item_code": "$\\alpha$-HBD",
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
2026-08-07 04:48:02,872 INFO     29 [qwen-vl-table] coord grouping: {20: 20}
2026-08-07 04:48:02,902 INFO     29 [qwen-vl-table] coord API call start, page=20, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5648298, prompt_len=621
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
2026-08-07 04:48:10,780 INFO     29 [qwen-vl-table] coord API raw response (len=997):
[
	{"text": "胆碱酯酶*", "bbox": [235, 235, 278, 250]},
	{"text": "尿素*", "bbox": [245, 268, 268, 283]},
	{"text": "肌酐*", "bbox": [245, 302, 268, 317]},
	{"text": "尿酸*", "bbox": [245, 335, 268, 350]},
	{"text": "碳酸氢根*", "bbox": [235, 368, 277, 383]},
	{"text": "总胆固醇*", "bbox": [235, 401, 277, 416]},
	{"text": "甘油三酯*", "bbox": [235, 435, 277, 450]},
	{"text": "低密度脂蛋白胆固醇*", "bbox": [211, 468, 301, 483]},
	{"text": "空腹血葡萄糖*", "bbox": [225, 502, 287, 517]},
	{"text": "钾*", "bbox": [249, 535, 263, 550]},
	{"text": "钠*", "bbox": [249, 569, 263, 584]},
	{"text": "氯*", "bbox": [249, 603, 263, 618]},
	{"text": "总钙*", "bbox": [245, 636, 268, 651]},
	{"text": "镁*", "bbox": [250, 670, 264, 685]},
	{"text": "磷*", "bbox": [250, 704, 264, 719]},
	{"text": "肌酸激酶*", "bbox": [236, 737, 279, 752]},
	{"text": "肌酸激酶同工酶MB", "bbox": [216, 771, 300, 786]},
	{"text": "乳酸脱氢酶*", "bbox": [232, 804, 285, 819]},
	{"text": "α-羟丁酸脱氢酶*", "bbox": [225, 838, 293, 853]},
	{"text": "免疫球蛋白E*", "bbox": [231, 871, 288, 886]}
]
2026-08-07 04:48:10,780 INFO     29 [qwen-vl-table] coord API: raw_items=20, valid_items=20, elapsed=7.9s
2026-08-07 04:48:10,780 INFO     29 [qwen-vl-table] coord item[0]: text=胆碱酯酶*, bbox=[235, 235, 278, 250]
2026-08-07 04:48:10,780 INFO     29 [qwen-vl-table] coord item[1]: text=尿素*, bbox=[245, 268, 268, 283]
2026-08-07 04:48:10,780 INFO     29 [qwen-vl-table] coord item[2]: text=肌酐*, bbox=[245, 302, 268, 317]
2026-08-07 04:48:10,780 INFO     29 [qwen-vl-table] coord item[3]: text=尿酸*, bbox=[245, 335, 268, 350]
2026-08-07 04:48:10,780 INFO     29 [qwen-vl-table] coord item[4]: text=碳酸氢根*, bbox=[235, 368, 277, 383]
2026-08-07 04:48:10,780 INFO     29 [qwen-vl-table] coord item[5]: text=总胆固醇*, bbox=[235, 401, 277, 416]
2026-08-07 04:48:10,781 INFO     29 [qwen-vl-table] coord item[6]: text=甘油三酯*, bbox=[235, 435, 277, 450]
2026-08-07 04:48:10,781 INFO     29 [qwen-vl-table] coord item[7]: text=低密度脂蛋白胆固醇*, bbox=[211, 468, 301, 483]
2026-08-07 04:48:10,781 INFO     29 [qwen-vl-table] coord item[8]: text=空腹血葡萄糖*, bbox=[225, 502, 287, 517]
2026-08-07 04:48:10,781 INFO     29 [qwen-vl-table] coord item[9]: text=钾*, bbox=[249, 535, 263, 550]
2026-08-07 04:48:10,781 INFO     29 [qwen-vl-table] coord item[10]: text=钠*, bbox=[249, 569, 263, 584]
2026-08-07 04:48:10,781 INFO     29 [qwen-vl-table] coord item[11]: text=氯*, bbox=[249, 603, 263, 618]
2026-08-07 04:48:10,781 INFO     29 [qwen-vl-table] coord item[12]: text=总钙*, bbox=[245, 636, 268, 651]
2026-08-07 04:48:10,781 INFO     29 [qwen-vl-table] coord item[13]: text=镁*, bbox=[250, 670, 264, 685]
2026-08-07 04:48:10,781 INFO     29 [qwen-vl-table] coord item[14]: text=磷*, bbox=[250, 704, 264, 719]
2026-08-07 04:48:10,781 INFO     29 [qwen-vl-table] coord item[15]: text=肌酸激酶*, bbox=[236, 737, 279, 752]
2026-08-07 04:48:10,781 INFO     29 [qwen-vl-table] coord item[16]: text=肌酸激酶同工酶MB, bbox=[216, 771, 300, 786]
2026-08-07 04:48:10,781 INFO     29 [qwen-vl-table] coord item[17]: text=乳酸脱氢酶*, bbox=[232, 804, 285, 819]
2026-08-07 04:48:10,781 INFO     29 [qwen-vl-table] coord item[18]: text=α-羟丁酸脱氢酶*, bbox=[225, 838, 293, 853]
2026-08-07 04:48:10,781 INFO     29 [qwen-vl-table] coord item[19]: text=免疫球蛋白E*, bbox=[231, 871, 288, 886]
2026-08-07 04:48:10,783 INFO     29 [qwen-vl-table] page=20 coord: matched 20/20, time=7.9s
2026-08-07 04:48:10,783 INFO     29 [qwen-vl-table] new_positions (20):
[[21, 197.87, 234.076, 139.825, 148.75], [21, 206.29, 225.656, 159.45999999999998, 168.385], [21, 206.29, 225.656, 179.69, 188.61499999999998], [21, 206.29, 225.656, 199.325, 208.25], [21, 197.87, 233.23399999999998, 218.95999999999998, 227.885], [21, 197.87, 233.23399999999998, 238.595, 247.51999999999998], [21, 197.87, 233.23399999999998, 258.825, 267.75], [21, 177.662, 253.44199999999998, 278.46, 287.385], [21, 189.45, 241.654, 298.69, 307.615], [21, 209.658, 221.446, 318.325, 327.25], [21, 209.658, 221.446, 338.555, 347.47999999999996], [21, 209.658, 221.446, 358.78499999999997, 367.71], [21, 206.29, 225.656, 378.41999999999996, 387.34499999999997], [21, 210.5, 222.28799999999998, 398.65, 407.575], [21, 210.5, 222.28799999999998, 418.88, 427.805], [21, 198.712, 234.91799999999998, 438.515, 447.44], [21, 181.87199999999999, 252.6, 458.745, 467.66999999999996], [21, 195.344, 239.97, 478.38, 487.30499999999995], [21, 189.45, 246.706, 498.60999999999996, 507.53499999999997], [21, 194.50199999999998, 242.49599999999998, 518.245, 527.17]]
2026-08-07 04:48:10,783 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=20, matched=20, pages=1, time=21.1s
2026-08-07 04:48:10,786 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-07 04:48:10,786 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[21]
2026-08-07 04:48:10,786 INFO     29 [qwen-vl-table] positions ： [[21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0]]
2026-08-07 04:48:11,252 INFO     29 [qwen-vl-table] page=21, rect=842x595, img=(2339x1653)
2026-08-07 04:48:11,252 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:48:11,252 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 1341, \"bbox_end\": 1366, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n\\hline\n缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 \\\\\n\\hline\nWBC & 白细胞计数* & 8.490 & & & & 10~9/L & 3.5-9.5 \\\\\nRBC & 红细胞计数* & 5.81 & & $\\uparrow$ & & 10~12/L & 4.3-5.8 \\\\\nHGB & 血红蛋白* & 157.00 & & & & g/L & 130-175 \\\\\nPLT & 血小板计数* & 268.00 & & & & 10~9/L & 125-350 \\\\\nNEU\\% & 中性粒细胞百分比 & 0.6920 & & & & & 0.4-0.75 \\\\\nLYM\\% & 淋巴细胞百分比 & 0.1970 & & $\\downarrow$ & & & 0.2-0.5 \\\\\nMONO\\% & 单核细胞百分比 & 0.0630 & & & & & 0.03-0.1 \\\\\nEO\\% & 嗜酸性粒细胞百分比 & 0.0450 & & & & & 0.004-0.08 \\\\\nBA SO\\% & 嗜碱性粒细胞百分比 & 0.0030 & & & & & 0-0.01 \\\\\nNEU & 中性粒细胞绝对值 & 5.88 & & & & 10~9/L & 1.8-6.3 \\\\\nLYM & 淋巴细胞绝对值 & 1.67 & & & & 10~9/L & 1.1-3.2 \\\\\nMONO & 单核细胞绝对值 & 0.53 & & & & 10~9/L & 0.1-0.6 \\\\\nEOS & 嗜酸性粒细胞绝对值 & 0.38 & & & & 10~9/L & 0.02-0.52 \\\\\nBA SO & 嗜碱性粒细胞绝对值 & 0.03 & & & & 10~9/L & 0-0.06 \\\\\nMCV & 平均红细胞体积* & 83.70 & & & & fl & 82-100 \\\\\nMCH & 平均RBC血红蛋白含量* & 26.90 & & $\\downarrow$ & & pg & 27-34 \\\\\nMCHC & 平均RBC血红蛋白浓度* & 323.00 & & & & g/L & 316-354 \\\\\nHCT & 红细胞比容* & 0.486 & & & & & 0.4-0.5 \\\\\nRDWCV & RBC体积分布宽度CV & 0.15 & & $\\uparrow$ & & & 0.11-0.14 \\\\\nPDW & 血小板体积分布宽度 & 0.16 & & & & & 0.15-0.18 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-07 04:48:21,709 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:48:21.708+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:48:24,444 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:48:24,444 INFO     29 [qwen-vl-table] page=21 LLM output (len=3473):
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
2026-08-07 04:48:24,444 INFO     29 [qwen-vl-table] coord grouping: {21: 20}
2026-08-07 04:48:24,468 INFO     29 [qwen-vl-table] coord API call start, page=21, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5649844, prompt_len=687
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
2026-08-07 04:48:32,111 INFO     29 [qwen-vl-table] coord API raw response (len=1063):
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
2026-08-07 04:48:32,111 INFO     29 [qwen-vl-table] coord API: raw_items=20, valid_items=20, elapsed=7.6s
2026-08-07 04:48:32,111 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞计数*, bbox=[247, 250, 300, 267]
2026-08-07 04:48:32,111 INFO     29 [qwen-vl-table] coord item[1]: text=红细胞计数*, bbox=[247, 283, 300, 299]
2026-08-07 04:48:32,111 INFO     29 [qwen-vl-table] coord item[2]: text=血红蛋白*, bbox=[252, 316, 295, 332]
2026-08-07 04:48:32,111 INFO     29 [qwen-vl-table] coord item[3]: text=血小板计数*, bbox=[247, 349, 300, 365]
2026-08-07 04:48:32,111 INFO     29 [qwen-vl-table] coord item[4]: text=中性粒细胞百分比, bbox=[236, 381, 312, 397]
2026-08-07 04:48:32,112 INFO     29 [qwen-vl-table] coord item[5]: text=淋巴细胞百分比, bbox=[240, 414, 308, 430]
2026-08-07 04:48:32,112 INFO     29 [qwen-vl-table] coord item[6]: text=单核细胞百分比, bbox=[240, 447, 308, 463]
2026-08-07 04:48:32,112 INFO     29 [qwen-vl-table] coord item[7]: text=嗜酸性粒细胞百分比, bbox=[231, 479, 318, 495]
2026-08-07 04:48:32,112 INFO     29 [qwen-vl-table] coord item[8]: text=嗜碱性粒细胞百分比, bbox=[231, 512, 318, 528]
2026-08-07 04:48:32,112 INFO     29 [qwen-vl-table] coord item[9]: text=中性粒细胞绝对值, bbox=[236, 545, 312, 561]
2026-08-07 04:48:32,112 INFO     29 [qwen-vl-table] coord item[10]: text=淋巴细胞绝对值, bbox=[240, 577, 308, 593]
2026-08-07 04:48:32,112 INFO     29 [qwen-vl-table] coord item[11]: text=单核细胞绝对值, bbox=[240, 610, 308, 626]
2026-08-07 04:48:32,112 INFO     29 [qwen-vl-table] coord item[12]: text=嗜酸性粒细胞绝对值, bbox=[231, 643, 318, 659]
2026-08-07 04:48:32,112 INFO     29 [qwen-vl-table] coord item[13]: text=嗜碱性粒细胞绝对值, bbox=[231, 676, 318, 692]
2026-08-07 04:48:32,112 INFO     29 [qwen-vl-table] coord item[14]: text=平均红细胞体积*, bbox=[240, 708, 310, 724]
2026-08-07 04:48:32,112 INFO     29 [qwen-vl-table] coord item[15]: text=平均RBC血红蛋白含量*, bbox=[225, 741, 325, 757]
2026-08-07 04:48:32,112 INFO     29 [qwen-vl-table] coord item[16]: text=平均RBC血红蛋白浓度*, bbox=[225, 774, 325, 790]
2026-08-07 04:48:32,112 INFO     29 [qwen-vl-table] coord item[17]: text=红细胞比容*, bbox=[249, 807, 301, 823]
2026-08-07 04:48:32,112 INFO     29 [qwen-vl-table] coord item[18]: text=RBC体积分布宽度CV, bbox=[231, 840, 320, 856]
2026-08-07 04:48:32,112 INFO     29 [qwen-vl-table] coord item[19]: text=血小板体积分布宽度, bbox=[233, 873, 319, 889]
2026-08-07 04:48:32,115 INFO     29 [qwen-vl-table] page=21 coord: matched 20/20, time=7.6s
2026-08-07 04:48:32,115 INFO     29 [qwen-vl-table] new_positions (20):
[[22, 207.974, 252.6, 148.75, 158.86499999999998], [22, 207.974, 252.6, 168.385, 177.905], [22, 212.184, 248.39, 188.01999999999998, 197.54], [22, 207.974, 252.6, 207.655, 217.17499999999998], [22, 198.712, 262.704, 226.695, 236.215], [22, 202.07999999999998, 259.336, 246.32999999999998, 255.85], [22, 202.07999999999998, 259.336, 265.965, 275.485], [22, 194.50199999999998, 267.756, 285.005, 294.525], [22, 194.50199999999998, 267.756, 304.64, 314.15999999999997], [22, 198.712, 262.704, 324.275, 333.79499999999996], [22, 202.07999999999998, 259.336, 343.315, 352.835], [22, 202.07999999999998, 259.336, 362.95, 372.46999999999997], [22, 194.50199999999998, 267.756, 382.585, 392.10499999999996], [22, 194.50199999999998, 267.756, 402.21999999999997, 411.74], [22, 202.07999999999998, 261.02, 421.26, 430.78], [22, 189.45, 273.65, 440.895, 450.41499999999996], [22, 189.45, 273.65, 460.53, 470.04999999999995], [22, 209.658, 253.44199999999998, 480.16499999999996, 489.685], [22, 194.50199999999998, 269.44, 499.79999999999995, 509.32], [22, 196.186, 268.598, 519.435, 528.9549999999999]]
2026-08-07 04:48:32,115 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=20, matched=20, pages=1, time=21.3s
2026-08-07 04:48:32,119 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-07 04:48:32,119 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[22]
2026-08-07 04:48:32,119 INFO     29 [qwen-vl-table] positions ： [[22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0]]
2026-08-07 04:48:32,614 INFO     29 [qwen-vl-table] page=22, rect=842x595, img=(2339x1653)
2026-08-07 04:48:32,614 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:48:32,614 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 1367, \"bbox_end\": 1393, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n\\hline\n\\multicolumn{1}{c}{\\textbf{缩写}} & \\multicolumn{1}{c}{\\textbf{项目名称}} & \\multicolumn{1}{c}{\\textbf{结果}} & \\multicolumn{1}{c}{\\textbf{结果提示}} & \\multicolumn{1}{c}{\\textbf{异常提示}} & \\multicolumn{1}{c}{\\textbf{辅助诊断}} & \\multicolumn{1}{c}{\\textbf{单位}} & \\multicolumn{1}{c}{\\textbf{参考范围}} \\\\\n\\hline\nFI02 & 吸氧浓度 & 21.00 & & & & \\% & 21-100 \\\\\nT & 体温 & 36.4 & & & & & 29-41 \\\\\nCa++ & 钙测定 & 1.19 & & & & mmol/L & 1.15-1.29 \\\\\nNa+ & 钠测定 & 143.20 & & & & mmol/L & 136-146 \\\\\nK+ & 钾测定 & 3.98 & & & & mmol/L & 3.5-4.5 \\\\\np02(a,T)/F02 & 氧合指数(p/f) & 315.0 & & $\\downarrow$ & & & 400-500 \\\\\nBEecf & 红细胞外剩余碱 & -1.80 & & & & mmol/l & -3-3 \\\\\nPH & 酸碱度 (PH) & 7.383 & & & & & 7.35-7.45 \\\\\npH(T) & pH校正值(pHT) & 7.392 & & & & & 7.35-7.45 \\\\\npO2 & 氧分压 (pO2) & 66.20 & & $\\downarrow$ & & mmHg & 83-108 \\\\\npO2(T) & 氧分压校正值 & 63.50 & & $\\downarrow$ & & mmHg & 83-108 \\\\\npCO2 & 二氧化碳分压 & 39.90 & & & & mmHg & 35-45 \\\\\nPCO2(T) & CO2分压校正 & 38.90 & & & & mmHg & 35-45 \\\\\nCl- & 氯测定 & 102.00 & & & & mmol/L & 98-106 \\\\\nHb & 血红蛋白测定(Hb) & 162.00 & & $\\uparrow$ & & g/L & 120-160 \\\\\nF02Hb & 氧合血红蛋白 & 92.0 & & $\\downarrow$ & & \\% & 94-98 \\\\\nMetHb & 高铁血红蛋白 & 0.10 & & & & & \\\\\ns02 & 总血氧饱和度 & 92.9 & & $\\downarrow$ & & \\% & 93-98 \\\\\nCOHb & CO红蛋白 & 1.00 & & & & \\% & 0-2 \\\\\nctCO2 & 血CO2含量 & 24.50 & & & & mmol/L & 24-32 \\\\\nFHHB & 还原血红蛋白 & 6.9 & & & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-07 04:48:45,643 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:48:45,643 INFO     29 [qwen-vl-table] page=22 LLM output (len=3564):
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
2026-08-07 04:48:45,643 INFO     29 [qwen-vl-table] coord grouping: {22: 21}
2026-08-07 04:48:45,661 INFO     29 [qwen-vl-table] coord API call start, page=22, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5775830, prompt_len=652
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
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord API raw response (len=1072):
[
	{"text": "吸氧浓度", "bbox": [263, 246, 304, 262]},
	{"text": "体温", "bbox": [273, 278, 294, 293]},
	{"text": "钙测定", "bbox": [269, 311, 298, 326]},
	{"text": "钠测定", "bbox": [269, 344, 298, 359]},
	{"text": "钾测定", "bbox": [269, 376, 298, 391]},
	{"text": "氧合指数(p/f)", "bbox": [254, 408, 313, 423]},
	{"text": "红细胞外剩余碱", "bbox": [250, 440, 318, 455]},
	{"text": "酸碱度 (PH)", "bbox": [254, 472, 309, 487]},
	{"text": "pH校正值(pHT)", "bbox": [250, 504, 318, 519]},
	{"text": "氧分压 (pO2)", "bbox": [251, 536, 313, 551]},
	{"text": "氧分压校正值", "bbox": [256, 569, 314, 584]},
	{"text": "二氧化碳分压", "bbox": [256, 601, 314, 616]},
	{"text": "CO2分压校正", "bbox": [256, 633, 314, 648]},
	{"text": "氯测定", "bbox": [270, 666, 299, 681]},
	{"text": "血红蛋白测定(Hb)", "bbox": [246, 698, 324, 713]},
	{"text": "氧合血红蛋白", "bbox": [256, 730, 314, 745]},
	{"text": "高铁血红蛋白", "bbox": [256, 762, 314, 777]},
	{"text": "总血氧饱和度", "bbox": [256, 794, 314, 809]},
	{"text": "CO红蛋白", "bbox": [263, 827, 307, 842]},
	{"text": "血CO2含量", "bbox": [261, 858, 309, 873]},
	{"text": "还原血红蛋白", "bbox": [256, 890, 314, 905]}
]
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord API: raw_items=21, valid_items=21, elapsed=9.0s
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord item[0]: text=吸氧浓度, bbox=[263, 246, 304, 262]
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord item[1]: text=体温, bbox=[273, 278, 294, 293]
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord item[2]: text=钙测定, bbox=[269, 311, 298, 326]
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord item[3]: text=钠测定, bbox=[269, 344, 298, 359]
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord item[4]: text=钾测定, bbox=[269, 376, 298, 391]
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord item[5]: text=氧合指数(p/f), bbox=[254, 408, 313, 423]
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord item[6]: text=红细胞外剩余碱, bbox=[250, 440, 318, 455]
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord item[7]: text=酸碱度 (PH), bbox=[254, 472, 309, 487]
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord item[8]: text=pH校正值(pHT), bbox=[250, 504, 318, 519]
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord item[9]: text=氧分压 (pO2), bbox=[251, 536, 313, 551]
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord item[10]: text=氧分压校正值, bbox=[256, 569, 314, 584]
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord item[11]: text=二氧化碳分压, bbox=[256, 601, 314, 616]
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord item[12]: text=CO2分压校正, bbox=[256, 633, 314, 648]
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord item[13]: text=氯测定, bbox=[270, 666, 299, 681]
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord item[14]: text=血红蛋白测定(Hb), bbox=[246, 698, 324, 713]
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord item[15]: text=氧合血红蛋白, bbox=[256, 730, 314, 745]
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord item[16]: text=高铁血红蛋白, bbox=[256, 762, 314, 777]
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord item[17]: text=总血氧饱和度, bbox=[256, 794, 314, 809]
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord item[18]: text=CO红蛋白, bbox=[263, 827, 307, 842]
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord item[19]: text=血CO2含量, bbox=[261, 858, 309, 873]
2026-08-07 04:48:54,673 INFO     29 [qwen-vl-table] coord item[20]: text=还原血红蛋白, bbox=[256, 890, 314, 905]
2026-08-07 04:48:54,675 INFO     29 [qwen-vl-table] page=22 coord: matched 21/21, time=9.0s
2026-08-07 04:48:54,675 INFO     29 [qwen-vl-table] new_positions (21):
[[23, 221.446, 255.968, 146.37, 155.89], [23, 229.86599999999999, 247.548, 165.41, 174.33499999999998], [23, 226.498, 250.916, 185.045, 193.97], [23, 226.498, 250.916, 204.67999999999998, 213.605], [23, 226.498, 250.916, 223.72, 232.64499999999998], [23, 213.868, 263.546, 242.76, 251.685], [23, 210.5, 267.756, 261.8, 270.72499999999997], [23, 213.868, 260.178, 280.84, 289.765], [23, 210.5, 267.756, 299.88, 308.805], [23, 211.34199999999998, 263.546, 318.91999999999996, 327.84499999999997], [23, 215.552, 264.388, 338.555, 347.47999999999996], [23, 215.552, 264.388, 357.59499999999997, 366.52], [23, 215.552, 264.388, 376.635, 385.56], [23, 227.34, 251.75799999999998, 396.27, 405.195], [23, 207.132, 272.808, 415.31, 424.23499999999996], [23, 215.552, 264.388, 434.34999999999997, 443.275], [23, 215.552, 264.388, 453.39, 462.315], [23, 215.552, 264.388, 472.43, 481.35499999999996], [23, 221.446, 258.49399999999997, 492.065, 500.98999999999995], [23, 219.762, 260.178, 510.51, 519.435], [23, 215.552, 264.388, 529.55, 538.475]]
2026-08-07 04:48:54,675 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=21, matched=21, pages=1, time=22.6s
2026-08-07 04:48:54,677 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-07 04:48:54,677 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[23]
2026-08-07 04:48:54,677 INFO     29 [qwen-vl-table] positions ： [[23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0]]
2026-08-07 04:48:55,147 INFO     29 [qwen-vl-table] page=23, rect=842x595, img=(2339x1653)
2026-08-07 04:48:55,147 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:48:55,147 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 1394, \"bbox_end\": 1420, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n\\hline\n缩写 & 项目名称 & 结果 & 结果提示 & 异常提示 & 辅助诊断 & 单位 & 参考范围 \\\\\n\\hline\nPH & 酸碱度 (PH) & 7.383 & & & & & 7.35-7.45 \\\\\npH(T) & pH校正值(pHT) & 7.392 & & & & & 7.35-7.45 \\\\\npO2 & 氧分压 (pO2) & 66.20 & & $\\downarrow$ & & mmHg & 83-108 \\\\\npO2(T) & 氧分压校正值 & 63.50 & & $\\downarrow$ & & mmHg & 83-108 \\\\\npCO2 & 二氧化碳分压 & 39.90 & & & & mmHg & 35-45 \\\\\nPCO2(T) & CO2分压校正 & 38.90 & & & & mmHg & 35-45 \\\\\nCl- & 氯测定 & 102.00 & & & & mmol/L & 98-106 \\\\\nHb & 血红蛋白测定(Hb) & 162.00 & & $\\uparrow$ & & g/L & 120-160 \\\\\nF02Hb & 氧合血红蛋白 & 92.0 & & $\\downarrow$ & & \\% & 94-98 \\\\\nMetHb & 高铁血红蛋白 & 0.10 & & & & & \\\\\ns02 & 总血氧饱和度 & 92.9 & & $\\downarrow$ & & \\% & 93-98 \\\\\nC0Hb & CO红蛋白 & 1.00 & & & & \\% & 0-2 \\\\\nctCO2 & 血CO2含量 & 24.50 & & & & mmol/L & 24-32 \\\\\nFHHB & 还原血红蛋白 & 6.9 & & & & \\% & 2-7 \\\\\ncHCO3 & 标准碳酸氢根 & 23.00 & & & & mmol/L & 22-26 \\\\\nABE (BE(B)) & 实际剩余碱 & -1.6 & & & & mmol/L & -3-3 \\\\\nHCO3- & 实际碳酸氢根 & 23.20 & & & & mmol/L & \\\\\nP02(A-a,T)e & 肺泡动脉氧分压差 & 36.0 & & $\\uparrow$ & & mmHg & 10-25 \\\\\nP02(a/A,T) & 动脉与肺泡氧分压比 & 64.0 & & $\\downarrow$ & & \\% & 85-95 \\\\\nRI & 呼吸指数 & 57.0 & & & & & \\\\\nGlu & 葡萄糖测定 & 6.70 & & $\\uparrow$ & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-07 04:48:55,150 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:48:55.149+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:49:08,227 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:49:08,227 INFO     29 [qwen-vl-table] page=23 LLM output (len=3566):
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
      "abnormal": false
    }
  ]
}
2026-08-07 04:49:08,227 INFO     29 [qwen-vl-table] coord grouping: {23: 21}
2026-08-07 04:49:08,244 INFO     29 [qwen-vl-table] coord API call start, page=23, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5930452, prompt_len=664
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
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord API raw response (len=1084):
[
	{"text": "酸碱度 (PH)", "bbox": [248, 246, 306, 262]},
	{"text": "pH校正值(pHT)", "bbox": [245, 277, 315, 293]},
	{"text": "氧分压 (pO2)", "bbox": [245, 310, 309, 326]},
	{"text": "氧分压校正值", "bbox": [250, 342, 310, 358]},
	{"text": "二氧化碳分压", "bbox": [251, 374, 310, 390]},
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
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord API: raw_items=21, valid_items=21, elapsed=7.8s
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord item[0]: text=酸碱度 (PH), bbox=[248, 246, 306, 262]
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord item[1]: text=pH校正值(pHT), bbox=[245, 277, 315, 293]
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord item[2]: text=氧分压 (pO2), bbox=[245, 310, 309, 326]
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord item[3]: text=氧分压校正值, bbox=[250, 342, 310, 358]
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord item[4]: text=二氧化碳分压, bbox=[251, 374, 310, 390]
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord item[5]: text=CO2分压校正, bbox=[250, 406, 310, 422]
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord item[6]: text=氯测定, bbox=[265, 438, 296, 454]
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord item[7]: text=血红蛋白测定(Hb), bbox=[242, 469, 320, 485]
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord item[8]: text=氧合血红蛋白, bbox=[251, 501, 310, 517]
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord item[9]: text=高铁血红蛋白, bbox=[251, 533, 310, 549]
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord item[10]: text=总血氧饱和度, bbox=[251, 565, 310, 581]
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord item[11]: text=CO红蛋白, bbox=[259, 597, 303, 613]
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord item[12]: text=血CO2含量, bbox=[256, 629, 307, 645]
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord item[13]: text=还原血红蛋白, bbox=[252, 661, 310, 677]
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord item[14]: text=标准碳酸氢根, bbox=[252, 693, 310, 709]
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord item[15]: text=实际剩余碱, bbox=[257, 725, 307, 741]
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord item[16]: text=实际碳酸氢根, bbox=[252, 757, 310, 773]
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord item[17]: text=肺泡动脉氧分压差, bbox=[243, 789, 321, 805]
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord item[18]: text=动脉与肺泡氧分压比, bbox=[238, 821, 325, 837]
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord item[19]: text=呼吸指数, bbox=[262, 853, 302, 869]
2026-08-07 04:49:16,014 INFO     29 [qwen-vl-table] coord item[20]: text=葡萄糖测定, bbox=[257, 885, 307, 901]
2026-08-07 04:49:16,016 INFO     29 [qwen-vl-table] page=23 coord: matched 21/21, time=7.8s
2026-08-07 04:49:16,016 INFO     29 [qwen-vl-table] new_positions (21):
[[24, 208.816, 257.652, 146.37, 155.89], [24, 206.29, 265.23, 164.815, 174.33499999999998], [24, 206.29, 260.178, 184.45, 193.97], [24, 210.5, 261.02, 203.48999999999998, 213.01], [24, 211.34199999999998, 261.02, 222.53, 232.04999999999998], [24, 210.5, 261.02, 241.57, 251.08999999999997], [24, 223.13, 249.232, 260.61, 270.13], [24, 203.76399999999998, 269.44, 279.055, 288.575], [24, 211.34199999999998, 261.02, 298.09499999999997, 307.615], [24, 211.34199999999998, 261.02, 317.135, 326.655], [24, 211.34199999999998, 261.02, 336.175, 345.695], [24, 218.078, 255.126, 355.215, 364.73499999999996], [24, 215.552, 258.49399999999997, 374.255, 383.775], [24, 212.184, 261.02, 393.29499999999996, 402.815], [24, 212.184, 261.02, 412.335, 421.85499999999996], [24, 216.394, 258.49399999999997, 431.375, 440.895], [24, 212.184, 261.02, 450.41499999999996, 459.935], [24, 204.606, 270.282, 469.455, 478.97499999999997], [24, 200.396, 273.65, 488.495, 498.015], [24, 220.60399999999998, 254.284, 507.53499999999997, 517.055], [24, 216.394, 258.49399999999997, 526.5749999999999, 536.095]]
2026-08-07 04:49:16,016 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=21, matched=21, pages=1, time=21.3s
2026-08-07 04:49:16,020 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-07 04:49:16,020 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[24]
2026-08-07 04:49:16,020 INFO     29 [qwen-vl-table] positions ： [[24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0]]
2026-08-07 04:49:16,233 INFO     29 [qwen-vl-table] page=24, rect=595x842, img=(1653x2339)
2026-08-07 04:49:16,233 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:49:16,234 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 1421, \"bbox_end\": 1453, \"encounter_dates\": [\"2026-03-10\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "临床诊断：肺癌\n样本采集时间：2026-03-10\n检测项目\n本产品对与肺癌密切相关的68个基因进行高通量测序。检测突变形式为点突变(SNV)、小片段插入缺失(INDEL)、拷贝数变异(CNV)以及融合(FUSION)。通过免疫组化检测PD-L1表达。\n本报告分析基因变异与靶向药物、化疗药物的相关性，给出靶向药物(FDA/NMPA批准药物、临床试验\n药物等)、化疗药物的用药提示信息，从而为临床制定治疗方案提供参考信息。\n注：检测基因列表见附录。\n检测结果小结\n检测类型\n检测结果\n靶向用药指导\n共检出3个变异位点,其中3个与靶向药物相关(KRAS\np.G12V;CDKN2A p.R80*;TP53 p.G279E)\nPD-L1蛋白表达水平\n使用CSTE1L3N抗体;TPS:<1%, CPS:1\n化疗药物检测\n详见“化疗药物检测解析”部分\n样品总体质量评估\n合格\n注:\n1. 本报告为基因检测结果,基因、药物等信息列举未按照重要性排序。\n2. 本报告只对本次采集样本负责,如有疑问,请在7个工作日内与我们联系。\n检测人:\n张紫叶\n复核人:\n王建丽\n日期:\n2026-03-16\n日期:\n2026-03-16\n1/26\n孔令祈 Novogene\n诺禾致源",
    "role": "user"
  }
]
2026-08-07 04:49:20,305 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:49:20,306 INFO     29 [qwen-vl-table] page=24 LLM output (len=854):
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
      "unit": null,
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
    }
  ]
}
2026-08-07 04:49:20,306 INFO     29 [qwen-vl-table] coord grouping: {24: 5}
2026-08-07 04:49:20,308 INFO     29 [qwen-vl-table] coord API call start, page=24, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1313362, prompt_len=543
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
KRAS、CDKN2A、TP53、PD-L1 TPS、PD-L1 CPS

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
2026-08-07 04:49:22,284 INFO     29 [qwen-vl-table] coord API raw response (len=259):
[
	{"text": "KRAS", "bbox": [484, 193, 814, 204]},
	{"text": "CDKN2A", "bbox": [530, 206, 630, 217]},
	{"text": "TP53", "bbox": [635, 206, 731, 217]},
	{"text": "PD-L1 TPS", "bbox": [545, 224, 692, 235]},
	{"text": "PD-L1 CPS", "bbox": [705, 224, 750, 235]}
]
2026-08-07 04:49:22,284 INFO     29 [qwen-vl-table] coord API: raw_items=5, valid_items=5, elapsed=2.0s
2026-08-07 04:49:22,284 INFO     29 [qwen-vl-table] coord item[0]: text=KRAS, bbox=[484, 193, 814, 204]
2026-08-07 04:49:22,284 INFO     29 [qwen-vl-table] coord item[1]: text=CDKN2A, bbox=[530, 206, 630, 217]
2026-08-07 04:49:22,285 INFO     29 [qwen-vl-table] coord item[2]: text=TP53, bbox=[635, 206, 731, 217]
2026-08-07 04:49:22,285 INFO     29 [qwen-vl-table] coord item[3]: text=PD-L1 TPS, bbox=[545, 224, 692, 235]
2026-08-07 04:49:22,285 INFO     29 [qwen-vl-table] coord item[4]: text=PD-L1 CPS, bbox=[705, 224, 750, 235]
2026-08-07 04:49:22,285 INFO     29 [qwen-vl-table] page=24 coord: matched 5/5, time=2.0s
2026-08-07 04:49:22,285 INFO     29 [qwen-vl-table] new_positions (5):
[[25, 287.97999999999996, 484.33, 162.506, 171.768], [25, 315.34999999999997, 374.84999999999997, 173.452, 182.714], [25, 377.825, 434.945, 173.452, 182.714], [25, 324.275, 411.74, 188.608, 197.87], [25, 419.47499999999997, 446.25, 188.608, 197.87]]
2026-08-07 04:49:22,285 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=5, matched=5, pages=1, time=6.3s
2026-08-07 04:49:22,299 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-07 04:49:22,300 INFO     29 [Trace] task=26a40982 | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Extractor:LabExam | outputs={"chunks": "11 items, types={'LabReport': 11}", "html": "", "json": "1557 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 11}"}
2026-08-07 04:49:22,300 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-07 04:49:22,306 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:49:22,306 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-07 04:49:23,503 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:49:23,509 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-07 04:49:23,509 INFO     29 [Trace] task=26a40982 | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "1557 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 11}"}
2026-08-07 04:49:23,510 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-07 04:49:23,515 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:49:23,515 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-07 04:49:24,161 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:49:24,167 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-07 04:49:24,168 INFO     29 [Trace] task=26a40982 | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Extractor:Clinical | outputs={"chunks": "1 items", "html": "", "json": "1557 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 11}"}
2026-08-07 04:49:24,168 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-07 04:49:24,173 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:49:24,174 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-07 04:49:24,930 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:49:24,936 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-07 04:49:24,937 INFO     29 [Trace] task=26a40982 | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "1557 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 11}"}
2026-08-07 04:49:24,937 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-07 04:49:24,942 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:49:24,942 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-07 04:49:24,961 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:49:24.960+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:49:25,396 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:49:25,403 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-07 04:49:25,404 INFO     29 [Trace] task=26a40982 | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "1557 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 11}"}
2026-08-07 04:49:25,404 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-07 04:49:25,409 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:49:25,409 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-07 04:49:25,865 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:49:25,872 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-07 04:49:25,872 INFO     29 [Trace] task=26a40982 | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "1557 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 11}"}
2026-08-07 04:49:25,872 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-07 04:49:25,880 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-07 04:49:25,880 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-07 04:49:25,881 INFO     29 [qwen-vl-text] positions(1058): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-07 04:49:25,882 INFO     29 [qwen-vl-text] page grouping: [0, 1, 2, 3, 4, 5, 6, 7, 8], lines per page: [29, 21, 25, 864, 44, 14, 23, 34, 4]
2026-08-07 04:49:26,330 INFO     29 [qwen-vl-text] page=0, rect=842x595, img=(2339x1653), dpi=200
2026-08-07 04:49:26,652 INFO     29 [qwen-vl-text] page=1, rect=842x595, img=(2339x1653), dpi=200
2026-08-07 04:49:27,120 INFO     29 [qwen-vl-text] page=2, rect=842x595, img=(2339x1653), dpi=200
2026-08-07 04:49:27,582 INFO     29 [qwen-vl-text] page=3, rect=842x595, img=(2339x1653), dpi=200
2026-08-07 04:49:28,043 INFO     29 [qwen-vl-text] page=4, rect=842x595, img=(2339x1653), dpi=200
2026-08-07 04:49:28,444 INFO     29 [qwen-vl-text] page=5, rect=842x595, img=(2339x1653), dpi=200
2026-08-07 04:49:28,829 INFO     29 [qwen-vl-text] page=6, rect=842x595, img=(2339x1653), dpi=200
2026-08-07 04:49:29,280 INFO     29 [qwen-vl-text] page=7, rect=842x595, img=(2339x1653), dpi=200
2026-08-07 04:49:29,712 INFO     29 [qwen-vl-text] page=8, rect=842x595, img=(2339x1653), dpi=200
2026-08-07 04:49:29,714 INFO     29 [qwen-vl-text] LLM extraction start, text_len=19338
2026-08-07 04:49:29,714 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:49:29,714 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 0, \"bbox_end\": 1057, \"encounter_dates\": [\"2026-02-28\"], \"department\": \"老年医学呼吸内科\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "病史\n主诉：咳嗽、咳痰1月余\n现病史：患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、\n呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。至当地医院体检发现肺部阴影，具体不详。2026-02-26至中\n山大学附属第一医院广西医院就诊，查胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm\n，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋\n巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。具体诊治不详。为进一步治疗，遂\n至我院门诊就诊，门诊拟“肺占位性病变”收治入院。自发病以来，患者精神、食欲、睡眠正常，大小便正\n常，体重无明显变化。\n既往史：平素健康状况：良好。\n既往病史：否认高血压、冠心病、糖尿病史。\n传染病史：否，否认肝炎、结核或其他传染病史。\n预防接种史：正规。\n过敏史：否认过敏史。\n外伤史：否认外伤史。\n手术史：2年前曾行尿道结石手术，具体不详。\n输血史：否认输血史。\n系统回顾：无特殊。\n个人史：出生地：广西壮族自治区南宁市青秀区\n地方病地区居住情况：无\n冶游史：否认冶游史\n职业与工作条件有无工业毒物、粉尘、放射性物质及接触史：无\n广西医科大学第一附属医院 孔令祈\n11:24\n2026-03-19\n姜晓红 (D450199...\n姜晓红 (D450199...\nCS 扫描全能王\n3亿人都在用的扫描App\n烟酒嗜好及药物使用史：有吸烟史，约10支/天，已吸烟40年，否认饮酒史。\n婚姻史：有婚姻史，结婚年龄：适龄结婚。有生育史，育有1子。\n家族史：否认相似家族病史及遗传病史。\n请患者或病史叙述者仔细确认以上病史记录并签字：[患者]\n体格检查\n一般情况：\n体温：36.8℃\n脉搏：75次/分\n呼吸：21次/分\n血压：138/72mmHg\n身高：161CM\n体重：74kg\n发育：正常\n营养：良好\n神志：清楚\n体位：自主体位\n面容：正常面容\n表情：自如\n步态：正常\n体型：正力型\n配合检查：合作\n皮肤黏膜:\n色泽: 正常\n皮疹: 全身皮肤未见皮疹\n皮下出血: 全身皮肤未见皮下出血\n毛发分布: 毛发分布正常\n温度与湿度: 温度、湿度、弹性均正常\n水肿: 未见水肿\n肝掌: 无\n蜘蛛痣: 未见蜘蛛痣\n其他表现: 无\n淋巴结: 全身浅表淋巴结未扪及肿大\n头部:\n头颅: 头颅大小正常, 无畸形\n眼: 眉毛, 眼睑, 结膜, 眼球未见异常, 双侧巩膜无黄染\n耳: 双耳外观未见异常, 乳突无压痛, 外耳道未见分泌物\n鼻: 鼻部外观未见异常, 鼻翼无扇动, 鼻腔无分泌物, 鼻窦区无压痛\n咽喉: 双侧扁桃体未见肿大, 表面未见脓性分泌物, 咽未见异常, 声音正常\n口腔: 唇, 舌, 牙齿, 牙龈正常\n颈部:\n颈部运动: 颈软无抵抗\n颈静脉: 无怒张\n气管: 居中\n颈动脉搏动: 正常\n肝-颈静脉回流征: 阴性\n广西医科大:\n预览 验证CA签名 手工解锁 删除 病历参考 更新数据 加载全部病程 个人模板管理 返回\n20 部：\n003470 20.2.11\n003470 20.2.11\n003470 20.2.11\n003470 20.2.11\n胸部：胸廓对称无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常\n肺部：\n视诊：双侧呼吸运动均匀对称，无增强或者减弱\n触诊：双肺触觉语颤对称无异常，未触及胸膜摩擦感\n叩诊：双肺叩诊呈清音\n听诊：双肺呼吸音清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音\n心脏：\n视诊：心尖搏动未见异常，位于左侧第五肋间锁骨中线内0.5cm，无异常隆起及凹陷\n触诊：心尖搏动未触及异常，未触及震颤及心包摩擦感\n叩诊：心界不大\n听诊：心率：75次/分，心律：齐 A2 > P2\n心音 S1：有力， 心音 S2：有力， 心音 S3：无， 心音 S4：无\n杂音：各瓣膜区未闻及杂音\n额外心音：无\n心包摩擦音：无\n周围血管：未见异常血管征\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.41.64\n003470 20.2.\n编辑\n功能\n表格\n签名\n其他\n打印\n预览\n验证CA签名\n手工解锁\n删除\n病历参考\n更新数据\n加载全部病程\n个人模板管理\n返回\n腹部:\n视诊: 外形: 腹部外形正常\n腹围: 未测\n脐部: 正常\n胃形: 未见\n肠形: 未见\n蠕动波: 未见\n腹式呼吸: 正常\n腹壁静脉曲张: 无\n腹壁其它情况: 无\n触诊: 全腹柔软\n压痛反跳痛: 无压痛及反跳痛\n波动感: 无\n振水声: 无\n腹部包块: 腹部未触及包块\n肝脏: 肝脏肋下未触及\n胆囊: 未触及, Murphy征阴性\n脾脏: 脾脏肋下未触及\n肾脏: 未触及\n输尿管压痛点: 无压痛\n叩诊: 肝浊音界: 正常,\n肝上界位于锁骨中线, 第五肋间\n移动性浊音: 阴性,\n肾区叩痛: 无\n听诊: 肠鸣音无明显增强或减弱, 未闻及血管杂音\n肛门直肠: 未查\n生殖器: 未查\n脊柱四肢:\n脊柱外形: 脊柱正常生理弯曲\n70 四 肢：四肢无畸形，未见杵状指（趾），未见静脉曲张，双下肢无凹陷性水肿\n关 节：各关节未见异常，活动无受限\n肌 肉：未见肌肉萎缩，肌张力正常。四肢肌力5级。\n神经系统：\n浅反射：双侧浅反射正常引出\n深反射：双侧深反射正常引出\n病理反射：未引出\n脑膜刺激征：阴性\n专科情况\n神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下肢无凹陷性水肿。\n实验室及器械检查结果\n(2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm\n，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋巴结彩超\n：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。\n2026-02-28 18:30\n男，因“咳嗽、咳痰1月余”于2026-02-28 15:23入非急诊步行入科。\n病例特点如下：1、老年期男性，起病缓，病程短。2、患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，\n伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。3、既往史：平素\n健康状况：良好。既往病史：否认高血压、冠心病、糖尿病史。传染病史：否，否认肝炎、结核或其他传染病史。预\n防接种史：正规。过敏史：否认过敏史。外伤史：否认外伤史。手术史：2年前曾行尿道结石手术，具体不详。输血\n史：否认输血史。系统回顾：无特殊。否认新冠肺炎流行病接触史。4、查体：T：36.8℃，P：75次/分，R：21次/分\n，BP：138/72mmHg。神志清楚，正常面容，皮肤巩膜无黄染，全身浅表淋巴结未扪及肿大，颈静脉无怒张。胸廓对称\n无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常，双肺叩诊呈清音，双肺呼吸音\n清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音。心界不大，心率75次/分，心律齐，各瓣膜区未闻及杂音。腹\n部外形正常，全腹柔软，无压痛及反跳痛，腹部未触及包块，肝脏肋下未触及，脾脏肋下未触及。移动性浊音阴性。\n双下肢无凹陷性水肿。浅反射：双侧浅反射正常引出。深反射：双侧深反射正常引出。病理反射：未引出。脑膜刺激\n征：阴性5、专科情况：神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下\n肢无凹陷性水肿。6、辅助检查：（2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组\n织肿块，最大截断面约77mm*60mm，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧\n胸膜肥厚、钙化。浅表淋巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。\n初步诊断：1.肺部阴影\n2.细菌性肺炎\n诊断依据：1.老年男性，起步缓，病程短\n2.咳嗽，咳淡黄色粘液痰\n3.外院胸部CT提示右肺下叶后基底段软组织肿块\n鉴别诊断。\n1.肺结核球\n编辑\n功能\n表格\n签名\n其他\n打印\n预览\n验证CA签名\n手工解锁\n删除\n病历参考\n更新数据\n加载全部病程\n个人模板管理\n返回\n鉴别诊断：\n1.肺结核球：多见于年轻患者，病灶多见于结核好发部位，如肺上叶尖后段和下叶背段，直径一般<3\ncm。一般无症状，病灶边界清楚，密度高，可有包膜。有时含钙化点，周围有卫星灶。\n2.急性粟粒性肺结核：应与弥漫型细支气管肺泡癌相鉴别。通常粟粒型肺结核患者年龄较轻，有发热\n，盗汗等全身中毒症状，呼吸道症状不明显。x线表现为细小、分布均匀、密度较淡的粟粒样结节病灶。\n而细支气管—肺泡细胞癌两肺多有大小不等的结节状播散病灶，边界清楚、密度较高，进行性发展和增大\n，且有进行性呼吸困难。\n3.肺炎：若无毒性症状，抗生素治疗后肺部阴影吸收缓慢，或同一部位反复发生肺炎时，应考虑到肺\n癌可能。肺部慢性炎症机化，形成团块状的炎性假瘤，也易与肺癌相混淆。但炎性假瘤往往形态不整，边\n缘不齐，核心密度较高，易伴有胸膜增厚，病灶长期无明显变化。\n4.肺脓肿：起病急，中毒症状严重，多有寒战、高热、咳嗽、咳大量脓臭痰等症状。肺部x线表现为\n均匀的大片状炎性阴影，空洞内常见较深液平。结合纤支镜检查和痰脱落细胞检查可以鉴别。\n5.纵隔淋巴瘤：颇似中央型肺癌，常为双侧性，可有发热等全身症状，需病理诊断。\nVTE血栓风险评估：创建时间:2026-02-28 15:37:11,评估节点:入院,量表名称:Padua评分,分数:0,评分描述:低危,\n预防措施:undefined\nVTE出血风险评估：创建时间:2026-02-28 18:35:54,评估节点:入院,量表名称:内科出血风险评估,分数:1,评分描述：\n低危,预防措施:undefined\n诊疗计划：1.内科护理常规,II级护理。\n2.完善必要辅助检查如血肿瘤标志物、痰液化验、胸部增强CT、支气管镜检查或浅表淋巴结及肺穿刺活检\n以确诊，必要时行颅脑MRI、腹部超声、骨扫描或PET-CT等检查以利进一步疾病诊治。\n3.给予吸氧、抗感染及止血、镇痛等对症支持治疗；明确病理类型拟定下一步治疗方案。\n是否需手术治疗：否\n医师签名：姜晓红 住院医师：孙超群",
    "role": "user"
  }
]
2026-08-07 04:49:54,759 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:49:54.758+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:49:55,515 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:49:55,515 INFO     29 [qwen-vl-text] LLM output (len=2746):
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
  "oh_pregnancies": null,
  "fh_text": "否认相似家族病史及遗传病史。",
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36.8,
  "vs_pulse_bpm": 75,
  "vs_respiration_rpm": 21,
  "vs_systolic_bp_mmhg": 138,
  "vs_diastolic_bp_mmhg": 72,
  "pe_general_condition": "发育正常，营养良好，神志清楚，自主体位，正常面容，表情自如，步态正常，正力型，合作",
  "pe_skin_mucosa": "色泽正常，全身皮肤未见皮疹，全身皮肤未见皮下出血，毛发分布正常，温度、湿度、弹性均正常，未见水肿，无肝掌，未见蜘蛛痣",
  "pe_lymph_nodes": "全身浅表淋巴结未扪及肿大",
  "pe_lungs": "胸廓对称无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧呼吸运动均匀对称，无增强或者减弱。双肺触觉语颤对称无异常，未触及胸膜摩擦感。双肺叩诊呈清音。双肺呼吸音清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音",
  "pe_heart": "心尖搏动未见异常，位于左侧第五肋间锁骨中线内0.5cm，无异常隆起及凹陷。心尖搏动未触及异常，未触及震颤及心包摩擦感。心界不大。心率：75次/分，心律：齐 A2 > P2。心音 S1：有力，心音 S2：有力，心音 S3：无，心音 S4：无。各瓣膜区未闻及杂音。无额外心音。无心包摩擦音。周围血管：未见异常血管征",
  "pe_abdomen": "腹部外形正常，腹式呼吸正常，无腹壁静脉曲张。全腹柔软，无压痛及反跳痛，无波动感，无振水声，腹部未触及包块。肝脏肋下未触及，胆囊未触及，Murphy征阴性，脾脏肋下未触及，肾脏未触及，输尿管无压痛。肝浊音界正常，肝上界位于锁骨中线第五肋间，移动性浊音阴性，肾区无叩痛。肠鸣音无明显增强或减弱，未闻及血管杂音",
  "pe_extremities": "四肢无畸形，未见杵状指（趾），未见静脉曲张，双下肢无凹陷性水肿。各关节未见异常，活动无受限。未见肌肉萎缩，肌张力正常。四肢肌力5级",
  "pe_nervous_system": "双侧浅反射正常引出，双侧深反射正常引出，病理反射未引出，脑膜刺激征阴性",
  "pe_specialist_exam": "神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下肢无凹陷性水肿。",
  "pe_ecog_score": null,
  "pat_text": "(2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。",
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
2026-08-07 04:49:55,515 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-28]
2026-08-07 04:49:55,541 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7951862, prompt_len=1326
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["病史", "主诉：咳嗽、咳痰1月余", "现病史：患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、", "呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。至当地医院体检发现肺部阴影，具体不详。2026-02-26至中", "山大学附属第一医院广西医院就诊，查胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm", "，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋", "巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。具体诊治不详。为进一步治疗，遂", "至我院门诊就诊，门诊拟“肺占位性病变”收治入院。自发病以来，患者精神、食欲、睡眠正常，大小便正", "常，体重无明显变化。", "既往史：平素健康状况：良好。", "既往病史：否认高血压、冠心病、糖尿病史。", "传染病史：否，否认肝炎、结核或其他传染病史。", "预防接种史：正规。", "过敏史：否认过敏史。", "外伤史：否认外伤史。", "手术史：2年前曾行尿道结石手术，具体不详。", "输血史：否认输血史。", "系统回顾：无特殊。", "个人史：出生地：广西壮族自治区南宁市青秀区", "地方病地区居住情况：无", "冶游史：否认冶游史", "职业与工作条件有无工业毒物、粉尘、放射性物质及接触史：无", "广西医科大学第一附属医院 孔令祈", "11:24", "2026-03-19", "姜晓红 (D450199...", "姜晓红 (D450199...", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-07 04:50:08,618 INFO     29 [qwen-vl-text] coord API raw response (len=1907):
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
	{"text": "传染病史：否，否认肝炎、结核或其他传染病史。", "bbox": [112, 441, 494, 469]},
	{"text": "预防接种史：正规。", "bbox": [112, 480, 262, 507]},
	{"text": "过敏史：否认过敏史。", "bbox": [112, 519, 280, 547]},
	{"text": "外伤史：否认外伤史。", "bbox": [112, 558, 280, 586]},
	{"text": "手术史：2年前曾行尿道结石手术，具体不详。", "bbox": [112, 597, 467, 625]},
	{"text": "输血史：否认输血史。", "bbox": [112, 637, 280, 664]},
	{"text": "系统回顾：无特殊。", "bbox": [112, 676, 270, 704]},
	{"text": "个人史：出生地：广西壮族自治区南宁市青秀区", "bbox": [40, 715, 412, 743]},
	{"text": "地方病地区居住情况：无", "bbox": [110, 754, 307, 782]},
	{"text": "冶游史：否认冶游史", "bbox": [110, 793, 270, 821]},
	{"text": "职业与工作条件有无工业毒物、粉尘、放射性物质及接触史：无", "bbox": [110, 832, 604, 860]},
	{"text": "广西医科大学第一附属医院 孔令祈", "bbox": [764, 832, 938, 851]},
	{"text": "11:24", "bbox": [963, 862, 988, 875]},
	{"text": "2026-03-19", "bbox": [950, 880, 998, 893]},
	{"text": "姜晓红 (D450199...", "bbox": [33, 873, 113, 887]},
	{"text": "姜晓红 (D450199...", "bbox": [148, 873, 228, 887]},
	{"text": "CS 扫描全能王", "bbox": [902, 938, 979, 958]},
	{"text": "3亿人都在用的扫描App", "bbox": [900, 965, 979, 977]}
]
```
2026-08-07 04:50:08,618 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=13.1s
2026-08-07 04:50:08,618 INFO     29 [qwen-vl-text] coord item[0]: text=病史, bbox=[459, 14, 540, 48]
2026-08-07 04:50:08,618 INFO     29 [qwen-vl-text] coord item[1]: text=主诉：咳嗽、咳痰1月余, bbox=[39, 47, 248, 75]
2026-08-07 04:50:08,618 INFO     29 [qwen-vl-text] coord item[2]: text=现病史：患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、, bbox=[39, 87, 950, 116]
2026-08-07 04:50:08,618 INFO     29 [qwen-vl-text] coord item[3]: text=呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。至当地医院体检发现肺部阴影，具体不详。2026-02-26至中, bbox=[115, 126, 956, 154]
2026-08-07 04:50:08,618 INFO     29 [qwen-vl-text] coord item[4]: text=山大学附属第一医院广西医院就诊，查胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm, bbox=[115, 166, 958, 194]
2026-08-07 04:50:08,618 INFO     29 [qwen-vl-text] coord item[5]: text=，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋, bbox=[115, 205, 956, 233]
2026-08-07 04:50:08,618 INFO     29 [qwen-vl-text] coord item[6]: text=巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。具体诊治不详。为进一步治疗，遂, bbox=[115, 244, 956, 272]
2026-08-07 04:50:08,618 INFO     29 [qwen-vl-text] coord item[7]: text=至我院门诊就诊，门诊拟“肺占位性病变”收治入院。自发病以来，患者精神、食欲、睡眠正常，大小便正, bbox=[115, 283, 956, 311]
2026-08-07 04:50:08,618 INFO     29 [qwen-vl-text] coord item[8]: text=常，体重无明显变化。, bbox=[115, 323, 280, 350]
2026-08-07 04:50:08,618 INFO     29 [qwen-vl-text] coord item[9]: text=既往史：平素健康状况：良好。, bbox=[39, 362, 280, 390]
2026-08-07 04:50:08,618 INFO     29 [qwen-vl-text] coord item[10]: text=既往病史：否认高血压、冠心病、糖尿病史。, bbox=[112, 401, 458, 429]
2026-08-07 04:50:08,619 INFO     29 [qwen-vl-text] coord item[11]: text=传染病史：否，否认肝炎、结核或其他传染病史。, bbox=[112, 441, 494, 469]
2026-08-07 04:50:08,619 INFO     29 [qwen-vl-text] coord item[12]: text=预防接种史：正规。, bbox=[112, 480, 262, 507]
2026-08-07 04:50:08,619 INFO     29 [qwen-vl-text] coord item[13]: text=过敏史：否认过敏史。, bbox=[112, 519, 280, 547]
2026-08-07 04:50:08,619 INFO     29 [qwen-vl-text] coord item[14]: text=外伤史：否认外伤史。, bbox=[112, 558, 280, 586]
2026-08-07 04:50:08,619 INFO     29 [qwen-vl-text] coord item[15]: text=手术史：2年前曾行尿道结石手术，具体不详。, bbox=[112, 597, 467, 625]
2026-08-07 04:50:08,619 INFO     29 [qwen-vl-text] coord item[16]: text=输血史：否认输血史。, bbox=[112, 637, 280, 664]
2026-08-07 04:50:08,619 INFO     29 [qwen-vl-text] coord item[17]: text=系统回顾：无特殊。, bbox=[112, 676, 270, 704]
2026-08-07 04:50:08,619 INFO     29 [qwen-vl-text] coord item[18]: text=个人史：出生地：广西壮族自治区南宁市青秀区, bbox=[40, 715, 412, 743]
2026-08-07 04:50:08,619 INFO     29 [qwen-vl-text] coord item[19]: text=地方病地区居住情况：无, bbox=[110, 754, 307, 782]
2026-08-07 04:50:08,619 INFO     29 [qwen-vl-text] coord item[20]: text=冶游史：否认冶游史, bbox=[110, 793, 270, 821]
2026-08-07 04:50:08,619 INFO     29 [qwen-vl-text] coord item[21]: text=职业与工作条件有无工业毒物、粉尘、放射性物质及接触史：无, bbox=[110, 832, 604, 860]
2026-08-07 04:50:08,619 INFO     29 [qwen-vl-text] coord item[22]: text=广西医科大学第一附属医院 孔令祈, bbox=[764, 832, 938, 851]
2026-08-07 04:50:08,619 INFO     29 [qwen-vl-text] coord item[23]: text=11:24, bbox=[963, 862, 988, 875]
2026-08-07 04:50:08,619 INFO     29 [qwen-vl-text] coord item[24]: text=2026-03-19, bbox=[950, 880, 998, 893]
2026-08-07 04:50:08,619 INFO     29 [qwen-vl-text] coord item[25]: text=姜晓红 (D450199..., bbox=[33, 873, 113, 887]
2026-08-07 04:50:08,620 INFO     29 [qwen-vl-text] coord item[26]: text=姜晓红 (D450199..., bbox=[148, 873, 228, 887]
2026-08-07 04:50:08,620 INFO     29 [qwen-vl-text] coord item[27]: text=CS 扫描全能王, bbox=[902, 938, 979, 958]
2026-08-07 04:50:08,620 INFO     29 [qwen-vl-text] coord item[28]: text=3亿人都在用的扫描App, bbox=[900, 965, 979, 977]
2026-08-07 04:50:08,624 INFO     29 [qwen-vl-text] page=0 — 29/29 coords, api_time=13.1s
2026-08-07 04:50:08,646 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4556708, prompt_len=919
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
2026-08-07 04:50:15,910 INFO     29 [qwen-vl-text] coord API raw response (len=1163):
[
	{"text": "烟酒嗜好及药物使用史：有吸烟史，约10支/天，已吸烟40年，否认饮酒史。", "bbox": [105, 245, 741, 275]},
	{"text": "婚姻史：有婚姻史，结婚年龄：适龄结婚。有生育史，育有1子。", "bbox": [25, 287, 565, 315]},
	{"text": "家族史：否认相似家族病史及遗传病史。", "bbox": [25, 330, 365, 357]},
	{"text": "请患者或病史叙述者仔细确认以上病史记录并签字：[患者]", "bbox": [384, 410, 876, 438]},
	{"text": "体格检查", "bbox": [450, 492, 585, 526]},
	{"text": "一般情况：", "bbox": [24, 545, 108, 572]},
	{"text": "体温：36.8℃", "bbox": [60, 587, 172, 614]},
	{"text": "脉搏：75次/分", "bbox": [253, 587, 379, 614]},
	{"text": "呼吸：21次/分", "bbox": [474, 587, 598, 614]},
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
	{"text": "配合检查：合作", "bbox": [474, 728, 606, 755]}
]
2026-08-07 04:50:15,910 INFO     29 [qwen-vl-text] coord API: raw_items=21, valid_items=21, elapsed=7.3s
2026-08-07 04:50:15,910 INFO     29 [qwen-vl-text] coord item[0]: text=烟酒嗜好及药物使用史：有吸烟史，约10支/天，已吸烟40年，否认饮酒史。, bbox=[105, 245, 741, 275]
2026-08-07 04:50:15,910 INFO     29 [qwen-vl-text] coord item[1]: text=婚姻史：有婚姻史，结婚年龄：适龄结婚。有生育史，育有1子。, bbox=[25, 287, 565, 315]
2026-08-07 04:50:15,911 INFO     29 [qwen-vl-text] coord item[2]: text=家族史：否认相似家族病史及遗传病史。, bbox=[25, 330, 365, 357]
2026-08-07 04:50:15,911 INFO     29 [qwen-vl-text] coord item[3]: text=请患者或病史叙述者仔细确认以上病史记录并签字：[患者], bbox=[384, 410, 876, 438]
2026-08-07 04:50:15,912 INFO     29 [qwen-vl-text] coord item[4]: text=体格检查, bbox=[450, 492, 585, 526]
2026-08-07 04:50:15,912 INFO     29 [qwen-vl-text] coord item[5]: text=一般情况：, bbox=[24, 545, 108, 572]
2026-08-07 04:50:15,912 INFO     29 [qwen-vl-text] coord item[6]: text=体温：36.8℃, bbox=[60, 587, 172, 614]
2026-08-07 04:50:15,912 INFO     29 [qwen-vl-text] coord item[7]: text=脉搏：75次/分, bbox=[253, 587, 379, 614]
2026-08-07 04:50:15,912 INFO     29 [qwen-vl-text] coord item[8]: text=呼吸：21次/分, bbox=[474, 587, 598, 614]
2026-08-07 04:50:15,912 INFO     29 [qwen-vl-text] coord item[9]: text=血压：138/72mmHg, bbox=[683, 587, 838, 614]
2026-08-07 04:50:15,912 INFO     29 [qwen-vl-text] coord item[10]: text=身高：161CM, bbox=[61, 636, 164, 663]
2026-08-07 04:50:15,912 INFO     29 [qwen-vl-text] coord item[11]: text=体重：74kg, bbox=[253, 636, 351, 663]
2026-08-07 04:50:15,912 INFO     29 [qwen-vl-text] coord item[12]: text=发育：正常, bbox=[474, 636, 568, 663]
2026-08-07 04:50:15,912 INFO     29 [qwen-vl-text] coord item[13]: text=营养：良好, bbox=[682, 636, 777, 663]
2026-08-07 04:50:15,912 INFO     29 [qwen-vl-text] coord item[14]: text=神志：清楚, bbox=[61, 682, 154, 709]
2026-08-07 04:50:15,913 INFO     29 [qwen-vl-text] coord item[15]: text=体位：自主体位, bbox=[253, 682, 389, 709]
2026-08-07 04:50:15,913 INFO     29 [qwen-vl-text] coord item[16]: text=面容：正常面容, bbox=[474, 682, 607, 709]
2026-08-07 04:50:15,913 INFO     29 [qwen-vl-text] coord item[17]: text=表情：自如, bbox=[682, 682, 777, 709]
2026-08-07 04:50:15,913 INFO     29 [qwen-vl-text] coord item[18]: text=步态：正常, bbox=[61, 728, 154, 755]
2026-08-07 04:50:15,913 INFO     29 [qwen-vl-text] coord item[19]: text=体型：正力型, bbox=[253, 728, 368, 755]
2026-08-07 04:50:15,913 INFO     29 [qwen-vl-text] coord item[20]: text=配合检查：合作, bbox=[474, 728, 606, 755]
2026-08-07 04:50:15,913 INFO     29 [qwen-vl-text] page=1 — 21/21 coords, api_time=7.3s
2026-08-07 04:50:15,928 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5051128, prompt_len=1048
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["皮肤黏膜:", "色泽: 正常", "皮疹: 全身皮肤未见皮疹", "皮下出血: 全身皮肤未见皮下出血", "毛发分布: 毛发分布正常", "温度与湿度: 温度、湿度、弹性均正常", "水肿: 未见水肿", "肝掌: 无", "蜘蛛痣: 未见蜘蛛痣", "其他表现: 无", "淋巴结: 全身浅表淋巴结未扪及肿大", "头部:", "头颅: 头颅大小正常, 无畸形", "眼: 眉毛, 眼睑, 结膜, 眼球未见异常, 双侧巩膜无黄染", "耳: 双耳外观未见异常, 乳突无压痛, 外耳道未见分泌物", "鼻: 鼻部外观未见异常, 鼻翼无扇动, 鼻腔无分泌物, 鼻窦区无压痛", "咽喉: 双侧扁桃体未见肿大, 表面未见脓性分泌物, 咽未见异常, 声音正常", "口腔: 唇, 舌, 牙齿, 牙龈正常", "颈部:", "颈部运动: 颈软无抵抗", "颈静脉: 无怒张", "气管: 居中", "颈动脉搏动: 正常", "肝-颈静脉回流征: 阴性", "广西医科大:"]

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
2026-08-07 04:50:28,597 INFO     29 [qwen-vl-text] coord API raw response (len=1456):
[
	{"text": "皮肤黏膜:", "bbox": [94, 7, 181, 37]},
	{"text": "色泽: 正常", "bbox": [222, 52, 300, 80]},
	{"text": "皮疹: 全身皮肤未见皮疹", "bbox": [222, 93, 415, 121]},
	{"text": "皮下出血: 全身皮肤未见皮下出血", "bbox": [138, 137, 452, 165]},
	{"text": "毛发分布: 毛发分布正常", "bbox": [138, 178, 375, 206]},
	{"text": "温度与湿度: 温度、湿度、弹性均正常", "bbox": [138, 221, 498, 249]},
	{"text": "水肿: 未见水肿", "bbox": [222, 264, 337, 292]},
	{"text": "肝掌: 无", "bbox": [138, 305, 290, 334]},
	{"text": "蜘蛛痣: 未见蜘蛛痣", "bbox": [184, 349, 355, 377]},
	{"text": "其他表现: 无", "bbox": [138, 390, 278, 418]},
	{"text": "淋巴结: 全身浅表淋巴结未扪及肿大", "bbox": [100, 433, 421, 461]},
	{"text": "头部:", "bbox": [100, 475, 181, 503]},
	{"text": "头颅: 头颅大小正常, 无畸形", "bbox": [138, 517, 384, 545]},
	{"text": "眼: 眉毛, 眼睑, 结膜, 眼球未见异常, 双侧巩膜无黄染", "bbox": [138, 558, 604, 586]},
	{"text": "耳: 双耳外观未见异常, 乳突无压痛, 外耳道未见分泌物", "bbox": [138, 600, 604, 628]},
	{"text": "鼻: 鼻部外观未见异常, 鼻翼无扇动, 鼻腔无分泌物, 鼻窦区无压痛", "bbox": [138, 641, 696, 669]},
	{"text": "咽喉: 双侧扁桃体未见肿大, 表面未见脓性分泌物, 咽未见异常, 声音正常", "bbox": [138, 683, 749, 711]},
	{"text": "口腔: 唇, 舌, 牙齿, 牙龈正常", "bbox": [138, 724, 401, 752]},
	{"text": "颈部:", "bbox": [156, 767, 181, 794]},
	{"text": "颈部运动: 颈软无抵抗", "bbox": [134, 808, 321, 836]},
	{"text": "颈静脉: 无怒张", "bbox": [498, 808, 626, 836]},
	{"text": "气管: 居中", "bbox": [754, 807, 844, 835]},
	{"text": "颈动脉搏动: 正常", "bbox": [134, 855, 321, 883]},
	{"text": "肝-颈静脉回流征: 阴性", "bbox": [498, 855, 692, 883]},
	{"text": "广西医科大:", "bbox": [861, 880, 938, 900]}
]
2026-08-07 04:50:28,597 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=12.7s
2026-08-07 04:50:28,597 INFO     29 [qwen-vl-text] coord item[0]: text=皮肤黏膜:, bbox=[94, 7, 181, 37]
2026-08-07 04:50:28,597 INFO     29 [qwen-vl-text] coord item[1]: text=色泽: 正常, bbox=[222, 52, 300, 80]
2026-08-07 04:50:28,597 INFO     29 [qwen-vl-text] coord item[2]: text=皮疹: 全身皮肤未见皮疹, bbox=[222, 93, 415, 121]
2026-08-07 04:50:28,597 INFO     29 [qwen-vl-text] coord item[3]: text=皮下出血: 全身皮肤未见皮下出血, bbox=[138, 137, 452, 165]
2026-08-07 04:50:28,597 INFO     29 [qwen-vl-text] coord item[4]: text=毛发分布: 毛发分布正常, bbox=[138, 178, 375, 206]
2026-08-07 04:50:28,597 INFO     29 [qwen-vl-text] coord item[5]: text=温度与湿度: 温度、湿度、弹性均正常, bbox=[138, 221, 498, 249]
2026-08-07 04:50:28,597 INFO     29 [qwen-vl-text] coord item[6]: text=水肿: 未见水肿, bbox=[222, 264, 337, 292]
2026-08-07 04:50:28,597 INFO     29 [qwen-vl-text] coord item[7]: text=肝掌: 无, bbox=[138, 305, 290, 334]
2026-08-07 04:50:28,597 INFO     29 [qwen-vl-text] coord item[8]: text=蜘蛛痣: 未见蜘蛛痣, bbox=[184, 349, 355, 377]
2026-08-07 04:50:28,597 INFO     29 [qwen-vl-text] coord item[9]: text=其他表现: 无, bbox=[138, 390, 278, 418]
2026-08-07 04:50:28,597 INFO     29 [qwen-vl-text] coord item[10]: text=淋巴结: 全身浅表淋巴结未扪及肿大, bbox=[100, 433, 421, 461]
2026-08-07 04:50:28,597 INFO     29 [qwen-vl-text] coord item[11]: text=头部:, bbox=[100, 475, 181, 503]
2026-08-07 04:50:28,598 INFO     29 [qwen-vl-text] coord item[12]: text=头颅: 头颅大小正常, 无畸形, bbox=[138, 517, 384, 545]
2026-08-07 04:50:28,598 INFO     29 [qwen-vl-text] coord item[13]: text=眼: 眉毛, 眼睑, 结膜, 眼球未见异常, 双侧巩膜无黄染, bbox=[138, 558, 604, 586]
2026-08-07 04:50:28,598 INFO     29 [qwen-vl-text] coord item[14]: text=耳: 双耳外观未见异常, 乳突无压痛, 外耳道未见分泌物, bbox=[138, 600, 604, 628]
2026-08-07 04:50:28,598 INFO     29 [qwen-vl-text] coord item[15]: text=鼻: 鼻部外观未见异常, 鼻翼无扇动, 鼻腔无分泌物, 鼻窦区无压痛, bbox=[138, 641, 696, 669]
2026-08-07 04:50:28,598 INFO     29 [qwen-vl-text] coord item[16]: text=咽喉: 双侧扁桃体未见肿大, 表面未见脓性分泌物, 咽未见异常, 声音正常, bbox=[138, 683, 749, 711]
2026-08-07 04:50:28,598 INFO     29 [qwen-vl-text] coord item[17]: text=口腔: 唇, 舌, 牙齿, 牙龈正常, bbox=[138, 724, 401, 752]
2026-08-07 04:50:28,598 INFO     29 [qwen-vl-text] coord item[18]: text=颈部:, bbox=[156, 767, 181, 794]
2026-08-07 04:50:28,598 INFO     29 [qwen-vl-text] coord item[19]: text=颈部运动: 颈软无抵抗, bbox=[134, 808, 321, 836]
2026-08-07 04:50:28,598 INFO     29 [qwen-vl-text] coord item[20]: text=颈静脉: 无怒张, bbox=[498, 808, 626, 836]
2026-08-07 04:50:28,598 INFO     29 [qwen-vl-text] coord item[21]: text=气管: 居中, bbox=[754, 807, 844, 835]
2026-08-07 04:50:28,598 INFO     29 [qwen-vl-text] coord item[22]: text=颈动脉搏动: 正常, bbox=[134, 855, 321, 883]
2026-08-07 04:50:28,598 INFO     29 [qwen-vl-text] coord item[23]: text=肝-颈静脉回流征: 阴性, bbox=[498, 855, 692, 883]
2026-08-07 04:50:28,598 INFO     29 [qwen-vl-text] coord item[24]: text=广西医科大:, bbox=[861, 880, 938, 900]
2026-08-07 04:50:28,599 INFO     29 [qwen-vl-text] page=2 — 25/25 coords, api_time=12.7s
2026-08-07 04:50:28,610 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5275194, prompt_len=18785
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共864行）
["预览 验证CA签名 手工解锁 删除 病历参考 更新数据 加载全部病程 个人模板管理 返回", "20 部：", "003470 20.2.11", "003470 20.2.11", "003470 20.2.11", "003470 20.2.11", "胸部：胸廓对称无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常", "肺部：", "视诊：双侧呼吸运动均匀对称，无增强或者减弱", "触诊：双肺触觉语颤对称无异常，未触及胸膜摩擦感", "叩诊：双肺叩诊呈清音", "听诊：双肺呼吸音清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音", "心脏：", "视诊：心尖搏动未见异常，位于左侧第五肋间锁骨中线内0.5cm，无异常隆起及凹陷", "触诊：心尖搏动未触及异常，未触及震颤及心包摩擦感", "叩诊：心界不大", "听诊：心率：75次/分，心律：齐 A2 > P2", "心音 S1：有力， 心音 S2：有力， 心音 S3：无， 心音 S4：无", "杂音：各瓣膜区未闻及杂音", "额外心音：无", "心包摩擦音：无", "周围血管：未见异常血管征", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2.41.64", "003470 20.2."]

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
2026-08-07 04:51:43,040 INFO     29 [qwen-vl-text] coord API raw response (len=11065):
[
	{"text": "预览 验证CA签名 手工解锁 删除 病历参考 更新数据 加载全部病程 个人模板管理 返回", "bbox": [28, 116, 607, 140]},
	{"text": "20 部：", "bbox": [37, 148, 92, 182]},
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
	{"text": "听诊：心率：75次/分，心律：齐 A2 > P2", "bbox": [83, 635, 572, 667]},
	{"text": "心音 S1：有力， 心音 S2：有力， 心音 S3： 无， 心音 S4： 无", "bbox": [166, 680, 710, 712]},
	{"text": "杂音：各瓣膜区未闻及杂音", "bbox": [166, 724, 409, 756]},
	{"text": "额外心音：无", "bbox": [166, 768, 290, 799]},
	{"text": "心包摩擦音：无", "bbox": [166, 812, 311, 844]},
	{"text": "周围血管：未见异常血管征", "bbox": [13, 855, 250, 887]},
	{"text": "003470 20.2.41.64", "bbox": [413, 838, 550, 890]},
	{"text": "003470 20.2.41.64", "bbox": [633, 838, 770, 890]},
	{"text": "003470 20.2.41.64", "bbox": [855, 838, 992, 890]},
	{"text": "003470 20.2.41.64", "bbox": [37, 604, 112, 648]},
	{"text": "003470 20.2.41.64", "bbox": [184, 604, 260, 648]},
	{"text": "003470 20.2.41.64", "bbox": [487, 604, 563, 648]},
	{"text": "003470 20.2.41.64", "bbox": [633, 604, 710, 648]},
	{"text": "003470 20.2.41.64", "bbox": [710, 580, 835, 648]},
	{"text": "003470 20.2.41.64", "bbox": [855, 604, 980, 667]},
	{"text": "003470 20.2.41.64", "bbox": [37, 373, 112, 417]},
	{"text": "003470 20.2.41.64", "bbox": [184, 373, 260, 417]},
	{"text": "003470 20.2.41.64", "bbox": [487, 373, 563, 417]},
	{"text": "003470 20.2.41.64", "bbox": [633, 373, 710, 417]},
	{"text": "003470 20.2.41.64", "bbox": [710, 349, 835, 417]},
	{"text": "003470 20.2.41.64", "bbox": [855, 373, 980, 436]},
	{"text": "003470 20.2.41.64", "bbox": [37, 458, 112, 502]},
	{"text": "003470 20.2.41.64", "bbox": [184, 458, 260, 502]},
	{"text": "003470 20.2.41.64", "bbox": [487, 458, 563, 502]},
	{"text": "003470 20.2.41.64", "bbox": [633, 458, 710, 502]},
	{"text": "003470 20.2.41.64", "bbox": [710, 434, 835, 502]},
	{"text": "003470 20.2.41.64", "bbox": [855, 458, 980, 521]},
	{"text": "003470 20.2.41.64", "bbox": [37, 546, 112, 590]},
	{"text": "003470 20.2.41.64", "bbox": [184, 546, 260, 590]},
	{"text": "003470 20.2.41.64", "bbox": [487, 546, 563, 590]},
	{"text": "003470 20.2.41.64", "bbox": [633, 546, 710, 590]},
	{"text": "003470 20.2.41.64", "bbox": [710, 521, 835, 590]},
	{"text": "003470 20.2.41.64", "bbox": [855, 546, 980, 609]},
	{"text": "003470 20.2.41.64", "bbox": [37, 635, 112, 679]},
	{"text": "003470 20.2.41.64", "bbox": [184, 635, 260, 679]},
	{"text": "003470 20.2.41.64", "bbox": [487, 635, 563, 679]},
	{"text": "003470 20.2.41.64", "bbox": [633, 635, 710, 679]},
	{"text": "003470 20.2.41.64", "bbox": [710, 611, 835, 679]},
	{"text": "003470 20.2.41.64", "bbox": [855, 635, 980, 698]},
	{"text": "003470 20.2.41.64", "bbox": [37, 724, 112, 768]},
	{"text": "003470 20.2.41.64", "bbox": [184, 724, 260, 768]},
	{"text": "003470 20.2.41.64", "bbox": [487, 724, 563, 768]},
	{"text": "003470 20.2.41.64", "bbox": [633, 724, 710, 768]},
	{"text": "003470 20.2.41.64", "bbox": [710, 700, 835, 768]},
	{"text": "003470 20.2.41.64", "bbox": [855, 724, 980, 787]},
	{"text": "003470 20.2.41.64", "bbox": [37, 812, 112, 856]},
	{"text": "003470 20.2.41.64", "bbox": [184, 812, 260, 856]},
	{"text": "003470 20.2.41.64", "bbox": [487, 812, 563, 856]},
	{"text": "003470 20.2.41.64", "bbox": [633, 812, 710, 856]},
	{"text": "003470 20.2.41.64", "bbox": [710, 788, 835, 856]},
	{"text": "003470 20.2.41.64", "bbox": [855, 812, 980, 875]},
	{"text": "003470 20.2.41.64", "bbox": [37, 856, 112, 900]},
	{"text": "003470 20.2.41.64", "bbox": [184, 856, 260, 900]},
	{"text": "003470 20.2.41.64", "bbox": [487, 856, 563, 900]},
	{"text": "003470 20.2.41.64", "bbox": [633, 856, 710, 900]},
	{"text": "003470 20.2.41.64", "bbox": [710, 832, 835, 900]},
	{"text": "003470 20.2.41.64", "bbox": [855, 856, 980, 919]},
	{"text": "003470 20.2.41.64", "bbox": [37, 900, 112, 944]},
	{"text": "003470 20.2.41.64", "bbox": [184, 900, 260, 944]},
	{"text": "003470 20.2.41.64", "bbox": [487, 900, 563, 944]},
	{"text": "003470 20.2.41.64", "bbox": [633, 900, 710, 944]},
	{"text": "003470 20.2.41.64", "bbox": [710, 876, 835, 944]},
	{"text": "003470 20.2.41.64", "bbox": [855, 900, 980, 963]},
	{"text": "003470 20.2.41.64", "bbox": [37, 944, 112, 988]},
	{"text": "003470 20.2.41.64", "bbox": [184, 944, 260, 988]},
	{"text": "003470 20.2.41.64", "bbox": [487, 944, 563, 988]},
	{"text": "003470 20.2.41.64", "bbox": [633, 944, 710, 988]},
	{"text": "003470 20.2.41.64", "bbox": [710, 920, 835, 988]},
	{"text": "003470 20.2.41.64", "bbox": [855, 944, 980, 1007]},
	{"text": "003470 20.2.41.64", "bbox": [37, 988, 112, 1032]},
	{"text": "003470 20.2.41.64", "bbox": [184, 988, 260, 1032]},
	{"text": "003470 20.2.41.64", "bbox": [487, 988, 563, 1032]},
	{"text": "003470 20.2.41.64", "bbox": [633, 988, 710, 1032]},
	{"text": "003470 20.2.41.64", "bbox": [710, 964, 835, 1032]},
	{"text": "003470 20.2.41.64", "bbox": [855, 988, 980, 1051]},
	{"text": "003470 20.2.41.64", "bbox": [37, 1032, 112, 1076]},
	{"text": "003470 20.2.41.64", "bbox": [184, 1032, 260, 1076]},
	{"text": "003470 20.2.41.64", "bbox": [487, 1032, 563, 1076]},
	{"text": "003470 20.2.41.64", "bbox": [633, 1032, 710, 1076]},
	{"text": "003470 20.2.41.64", "bbox": [710, 1008, 835, 1076]},
	{"text": "003470 20.2.41.64", "bbox": [855, 1032, 980, 1095]},
	{"text": "003470 20.2.41.64", "bbox": [37, 1076, 112, 1120]},
	{"text": "003470 20.2.41.64", "bbox": [184, 1076, 260, 1120]},
	{"text": "003470 20.2.41.64", "bbox": [487, 1076, 563, 1120]},
	{"text": "003470 20.2.41.64", "bbox": [633, 1076, 710, 1120]},
	{"text": "003470 20.2.41.64", "bbox": [710, 1052, 835, 1120]},
	{"text": "003470 20.2.41.64", "bbox": [855, 1076, 980, 1139]},
	{"text": "003470 20.2.41.64", "bbox": [37, 1120, 112, 1164]},
	{"text": "003470 20.2.41.64", "bbox": [184, 1120, 260, 1164]},
	{"text": "003470 20.2.41.64", "bbox": [487, 1120, 563, 1164]},
	{"text": "003470 20.2.41.64", "bbox": [633, 1120, 710, 1164]},
	{"text": "003470 20.2.41.64", "bbox": [710, 1096, 835, 1164]},
	{"text": "003470 20.2.41.64", "bbox": [855, 1120, 980, 1183]},
	{"text": "003470 20.2.41.64", "bbox": [37, 1164, 112, 1208]},
	{"text": "003470 20.2.41.64", "bbox": [184, 1164, 260, 1208]},
	{"text": "003470 20.2.41.64", "bbox": [487, 1164, 563, 1208]},
	{"text": "003470 20.2.41.64", "bbox": [633, 1164, 710, 1208]},
	{"text": "003470 20.2.41.64", "bbox": [710, 1140, 835, 1208]},
	{"text": "003470 20.2.41.64", "bbox": [855, 1164, 980, 1227]},
	{"text": "003470 20.2.41.64", "bbox": [37, 1208, 112, 1252]},
	{"text": "003470 20.2.41.64", "bbox": [184, 1208, 260, 1252]},
	{"text": "003470 20.2.41.64", "bbox": [487, 1208, 563, 1252]},
	{"text": "003470 20.2.41.64", "bbox": [633, 1208, 710, 1252]},
	{"text": "003470 20.2.41.64", "bbox": [710, 1184, 835, 1252]},
	{"text": "003470 20.2.41.64", "bbox": [855, 1208, 980, 1271]},
	{"text": "003470 20.2.41.64", "bbox": [37, 1252, 112, 1296]},
	{"text": "003470 20.2.41.64", "bbox": [184, 1252, 260, 1296]},
	{"text": "003470 20.2.41.64", "bbox": [487, 1252, 563, 1296]},
	{"text": "003470 20.2.41.64", "bbox": [633, 1252, 710, 1296]},
	{"text": "003470 20.2.41.64", "bbox": [710, 1228, 835, 1296]},
	{"text": "003470 20.2.41.64", "bbox": [855, 1252, 980, 1315]},
	{"text": "003470 20.2.41.64", "bbox": [37, 1296, 112, 1340]},
	{"text": "003470 20.2.41.64", "bbox": [184, 1296, 260, 1340]},
	{"text": "003470 20.2.41.64", "bbox": [487, 1296, 563, 1340]},
	{"text": "003470 20.2.41.64", "bbox": [633, 1296, 710, 1340]},
	{"text": "003470 20.2.41.64", "bbox": [710, 1272, 835, 1340]},
	{"text": "003470 20.2.41.64", "bbox": [855, 1296, 980, 1359]},
	{"text": "003470 20.2.41.64", "bbox": [37, 1340, 112, 1384]},
	{"text": "003470 20.2.41.64", "bbox": [184, 1340, 260, 1384]},
	{"text": "003470 20.2.41.64", "bbox": [487, 1340, 563, 1384]},
	{"text": "003470 20.2.41.64", "bbox": [633, 1340, 710, 1384]},
	{"text": "003470 20.2.41.64", "bbox": [710, 1316, 835, 1384]},
	{"text": "003470 20.2.41.64", "bbox": [855, 1340, 980, 1403]},
	{"text": "003470 20.2.41.64", "bbox": [37, 1384, 112, 1428]},
	{"text": "003470 20.2.41.64", "bbox": [184, 1384, 260, 1428]},
	{"text": "003470 20.2.41.64", "bbox": [487, 1384, 563, 1428]},
	{"text": "003470 20.2.41.64", "bbox": [633, 1384, 710, 1428]},
	{"text": "003470 20.2.41.64", "bbox": [710, 1360, 835, 1428]},
	{"text": "003470 20.2.41.64", "bbox": [855, 1384, 980, 1447]},
	{"text": "003470 20.2.41.64", "bbox": [37, 1428, 112, 1472]},
	{"text": "003470 20.2.41.64", "bbox": [184, 1428, 260, 1472]},
	{"text": "003470 20.2.41.64", "bbox": [487, 1428, 563, 1472]},
	{"text": "003470 20.2.41.64", "bbox": [633, 1428, 710, 1472]},
	{"text": "003470 20.2.41.64", "bbox": [710, 1404, 835, 1472]},
	{"text": "003470 20.2.41.64", "bbox": [855, 1428, 980, 1491]},
	{"text": "003470 20.2.41.64", "bbox": [37, 1472, 112, 1516]},
	{"text": "003470 20.2.41.64", "bbox": [184, 1472, 260, 1516]},
	{"text": "003470 20.2.41.64", "bbox": [487, 1472, 563, 1516]},
	{"text": "003470 20.2.41.64", "bbox": [633, 1472, 710, 1516]},
	{"text": "003470 20.2.41.64", "bbox": [710, 1448, 835, 1516]},
	{"text": "003470 20.2.41.64", "bbox": [855, 1472, 980, 1535]},
	{"text": "003470 20.2.41.64", "bbox": [37, 1516, 112, 1560]},
	{"text": "003470 20.2.41.64", "bbox": [184, 1516, 260, 1560]},
	{"text": "003470 20.2.41.64", "bbox": [487, 1516, 563, 1560]},
	{"text": "003470 20.2.41.64", "bbox": [633, 1516, 710, 1560]},
	{"text": "003470 20.2.41.64", "bbox": [710, 1492, 835, 1560]},
	{"text": "003470 20.2.41.64", "bbox": [855, 1516, 980, 1579]},
	{"text": "003470 20.2.41.64", "bbox": [37, 1560, 112, 1604]},
	{"text": "003470 20.2.41.64", "bbox": [184, 1560, 260, 1604]},
	{"text": "003470 20.2.41.64", "bbox": [487, 1560, 563, 1604]},
	{"text": "003470 20.2.41.64", "bbox": [633, 1560, 710, 1604]},
	{"text": "003470 20.2.41.64", "bbox": [710, 1536, 835, 1604]},
	{"text": "003470 20.2.41.64", "bbox": [855, 1560, 980, 1623]},
	{"text": "003470 20.2.41.64", "bbox": [37, 1604, 112, 1648]},
	{"text": "003470 20.2.41.64", "bbox": [184, 1604, 260, 1648]},
	{"text": "003470 20.2.41.64", "bbox": [487, 1604, 563, 1648]},
	{"text": "003470 20.2.41.64", "bbox": [633, 1604, 710, 1648]},
	{"text": "003470 20.2.41.64", "bbox": [710, 1580, 835, 1648]},
	{"text": "003470 20.2.41.64", "bbox": [855, 1604, 980, 1667]},
	{"text": "003470 20.2.41.64", "bbox": [37,
2026-08-07 04:51:43,041 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-07 04:51:43,044 INFO     29 [qwen-vl-text] coord API: raw_items=176, valid_items=175, elapsed=74.4s
2026-08-07 04:51:43,045 INFO     29 [qwen-vl-text] coord item[0]: text=预览 验证CA签名 手工解锁 删除 病历参考 更新数据 加载全部病程 个人模板管理 返回, bbox=[28, 116, 607, 140]
2026-08-07 04:51:43,045 INFO     29 [qwen-vl-text] coord item[1]: text=20 部：, bbox=[37, 148, 92, 182]
2026-08-07 04:51:43,045 INFO     29 [qwen-vl-text] coord item[2]: text=003470 20.2.11, bbox=[184, 154, 354, 192]
2026-08-07 04:51:43,045 INFO     29 [qwen-vl-text] coord item[3]: text=003470 20.2.11, bbox=[413, 154, 550, 192]
2026-08-07 04:51:43,045 INFO     29 [qwen-vl-text] coord item[4]: text=003470 20.2.11, bbox=[643, 154, 780, 192]
2026-08-07 04:51:43,045 INFO     29 [qwen-vl-text] coord item[5]: text=003470 20.2.11, bbox=[872, 154, 984, 192]
2026-08-07 04:51:43,045 INFO     29 [qwen-vl-text] coord item[6]: text=胸部：胸廓对称无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常, bbox=[38, 188, 967, 222]
2026-08-07 04:51:43,045 INFO     29 [qwen-vl-text] coord item[7]: text=肺部：, bbox=[38, 234, 112, 266]
2026-08-07 04:51:43,045 INFO     29 [qwen-vl-text] coord item[8]: text=视诊：双侧呼吸运动均匀对称，无增强或者减弱, bbox=[83, 278, 532, 310]
2026-08-07 04:51:43,045 INFO     29 [qwen-vl-text] coord item[9]: text=触诊：双肺触觉语颤对称无异常，未触及胸膜摩擦感, bbox=[83, 323, 572, 355]
2026-08-07 04:51:43,046 INFO     29 [qwen-vl-text] coord item[10]: text=叩诊：双肺叩诊呈清音, bbox=[83, 367, 307, 400]
2026-08-07 04:51:43,046 INFO     29 [qwen-vl-text] coord item[11]: text=听诊：双肺呼吸音清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音, bbox=[83, 412, 736, 444]
2026-08-07 04:51:43,046 INFO     29 [qwen-vl-text] coord item[12]: text=心脏：, bbox=[40, 458, 112, 490]
2026-08-07 04:51:43,046 INFO     29 [qwen-vl-text] coord item[13]: text=视诊：心尖搏动未见异常，位于左侧第五肋间锁骨中线内0.5cm，无异常隆起及凹陷, bbox=[83, 502, 848, 534]
2026-08-07 04:51:43,046 INFO     29 [qwen-vl-text] coord item[14]: text=触诊：心尖搏动未触及异常，未触及震颤及心包摩擦感, bbox=[83, 546, 591, 578]
2026-08-07 04:51:43,046 INFO     29 [qwen-vl-text] coord item[15]: text=叩诊：心界不大, bbox=[83, 591, 247, 623]
2026-08-07 04:51:43,046 INFO     29 [qwen-vl-text] coord item[16]: text=听诊：心率：75次/分，心律：齐 A2 > P2, bbox=[83, 635, 572, 667]
2026-08-07 04:51:43,046 INFO     29 [qwen-vl-text] coord item[17]: text=心音 S1：有力， 心音 S2：有力， 心音 S3： 无， 心音 S4： 无, bbox=[166, 680, 710, 712]
2026-08-07 04:51:43,046 INFO     29 [qwen-vl-text] coord item[18]: text=杂音：各瓣膜区未闻及杂音, bbox=[166, 724, 409, 756]
2026-08-07 04:51:43,046 INFO     29 [qwen-vl-text] coord item[19]: text=额外心音：无, bbox=[166, 768, 290, 799]
2026-08-07 04:51:43,046 INFO     29 [qwen-vl-text] coord item[20]: text=心包摩擦音：无, bbox=[166, 812, 311, 844]
2026-08-07 04:51:43,046 INFO     29 [qwen-vl-text] coord item[21]: text=周围血管：未见异常血管征, bbox=[13, 855, 250, 887]
2026-08-07 04:51:43,046 INFO     29 [qwen-vl-text] coord item[22]: text=003470 20.2.41.64, bbox=[413, 838, 550, 890]
2026-08-07 04:51:43,046 INFO     29 [qwen-vl-text] coord item[23]: text=003470 20.2.41.64, bbox=[633, 838, 770, 890]
2026-08-07 04:51:43,046 INFO     29 [qwen-vl-text] coord item[24]: text=003470 20.2.41.64, bbox=[855, 838, 992, 890]
2026-08-07 04:51:43,046 INFO     29 [qwen-vl-text] coord item[25]: text=003470 20.2.41.64, bbox=[37, 604, 112, 648]
2026-08-07 04:51:43,047 INFO     29 [qwen-vl-text] coord item[26]: text=003470 20.2.41.64, bbox=[184, 604, 260, 648]
2026-08-07 04:51:43,047 INFO     29 [qwen-vl-text] coord item[27]: text=003470 20.2.41.64, bbox=[487, 604, 563, 648]
2026-08-07 04:51:43,047 INFO     29 [qwen-vl-text] coord item[28]: text=003470 20.2.41.64, bbox=[633, 604, 710, 648]
2026-08-07 04:51:43,047 INFO     29 [qwen-vl-text] coord item[29]: text=003470 20.2.41.64, bbox=[710, 580, 835, 648]
2026-08-07 04:51:43,047 INFO     29 [qwen-vl-text] coord item[30]: text=003470 20.2.41.64, bbox=[855, 604, 980, 667]
2026-08-07 04:51:43,047 INFO     29 [qwen-vl-text] coord item[31]: text=003470 20.2.41.64, bbox=[37, 373, 112, 417]
2026-08-07 04:51:43,047 INFO     29 [qwen-vl-text] coord item[32]: text=003470 20.2.41.64, bbox=[184, 373, 260, 417]
2026-08-07 04:51:43,047 INFO     29 [qwen-vl-text] coord item[33]: text=003470 20.2.41.64, bbox=[487, 373, 563, 417]
2026-08-07 04:51:43,047 INFO     29 [qwen-vl-text] coord item[34]: text=003470 20.2.41.64, bbox=[633, 373, 710, 417]
2026-08-07 04:51:43,047 INFO     29 [qwen-vl-text] coord item[35]: text=003470 20.2.41.64, bbox=[710, 349, 835, 417]
2026-08-07 04:51:43,047 INFO     29 [qwen-vl-text] coord item[36]: text=003470 20.2.41.64, bbox=[855, 373, 980, 436]
2026-08-07 04:51:43,047 INFO     29 [qwen-vl-text] coord item[37]: text=003470 20.2.41.64, bbox=[37, 458, 112, 502]
2026-08-07 04:51:43,047 INFO     29 [qwen-vl-text] coord item[38]: text=003470 20.2.41.64, bbox=[184, 458, 260, 502]
2026-08-07 04:51:43,047 INFO     29 [qwen-vl-text] coord item[39]: text=003470 20.2.41.64, bbox=[487, 458, 563, 502]
2026-08-07 04:51:43,047 INFO     29 [qwen-vl-text] coord item[40]: text=003470 20.2.41.64, bbox=[633, 458, 710, 502]
2026-08-07 04:51:43,047 INFO     29 [qwen-vl-text] coord item[41]: text=003470 20.2.41.64, bbox=[710, 434, 835, 502]
2026-08-07 04:51:43,047 INFO     29 [qwen-vl-text] coord item[42]: text=003470 20.2.41.64, bbox=[855, 458, 980, 521]
2026-08-07 04:51:43,047 INFO     29 [qwen-vl-text] coord item[43]: text=003470 20.2.41.64, bbox=[37, 546, 112, 590]
2026-08-07 04:51:43,047 INFO     29 [qwen-vl-text] coord item[44]: text=003470 20.2.41.64, bbox=[184, 546, 260, 590]
2026-08-07 04:51:43,047 INFO     29 [qwen-vl-text] coord item[45]: text=003470 20.2.41.64, bbox=[487, 546, 563, 590]
2026-08-07 04:51:43,047 INFO     29 [qwen-vl-text] coord item[46]: text=003470 20.2.41.64, bbox=[633, 546, 710, 590]
2026-08-07 04:51:43,048 INFO     29 [qwen-vl-text] coord item[47]: text=003470 20.2.41.64, bbox=[710, 521, 835, 590]
2026-08-07 04:51:43,048 INFO     29 [qwen-vl-text] coord item[48]: text=003470 20.2.41.64, bbox=[855, 546, 980, 609]
2026-08-07 04:51:43,048 INFO     29 [qwen-vl-text] coord item[49]: text=003470 20.2.41.64, bbox=[37, 635, 112, 679]
2026-08-07 04:51:43,048 INFO     29 [qwen-vl-text] coord item[50]: text=003470 20.2.41.64, bbox=[184, 635, 260, 679]
2026-08-07 04:51:43,048 INFO     29 [qwen-vl-text] coord item[51]: text=003470 20.2.41.64, bbox=[487, 635, 563, 679]
2026-08-07 04:51:43,048 INFO     29 [qwen-vl-text] coord item[52]: text=003470 20.2.41.64, bbox=[633, 635, 710, 679]
2026-08-07 04:51:43,048 INFO     29 [qwen-vl-text] coord item[53]: text=003470 20.2.41.64, bbox=[710, 611, 835, 679]
2026-08-07 04:51:43,049 INFO     29 [qwen-vl-text] coord item[54]: text=003470 20.2.41.64, bbox=[855, 635, 980, 698]
2026-08-07 04:51:43,050 INFO     29 [qwen-vl-text] coord item[55]: text=003470 20.2.41.64, bbox=[37, 724, 112, 768]
2026-08-07 04:51:43,050 INFO     29 [qwen-vl-text] coord item[56]: text=003470 20.2.41.64, bbox=[184, 724, 260, 768]
2026-08-07 04:51:43,050 INFO     29 [qwen-vl-text] coord item[57]: text=003470 20.2.41.64, bbox=[487, 724, 563, 768]
2026-08-07 04:51:43,050 INFO     29 [qwen-vl-text] coord item[58]: text=003470 20.2.41.64, bbox=[633, 724, 710, 768]
2026-08-07 04:51:43,051 INFO     29 [qwen-vl-text] coord item[59]: text=003470 20.2.41.64, bbox=[710, 700, 835, 768]
2026-08-07 04:51:43,051 INFO     29 [qwen-vl-text] coord item[60]: text=003470 20.2.41.64, bbox=[855, 724, 980, 787]
2026-08-07 04:51:43,051 INFO     29 [qwen-vl-text] coord item[61]: text=003470 20.2.41.64, bbox=[37, 812, 112, 856]
2026-08-07 04:51:43,051 INFO     29 [qwen-vl-text] coord item[62]: text=003470 20.2.41.64, bbox=[184, 812, 260, 856]
2026-08-07 04:51:43,051 INFO     29 [qwen-vl-text] coord item[63]: text=003470 20.2.41.64, bbox=[487, 812, 563, 856]
2026-08-07 04:51:43,051 INFO     29 [qwen-vl-text] coord item[64]: text=003470 20.2.41.64, bbox=[633, 812, 710, 856]
2026-08-07 04:51:43,051 INFO     29 [qwen-vl-text] coord item[65]: text=003470 20.2.41.64, bbox=[710, 788, 835, 856]
2026-08-07 04:51:43,051 INFO     29 [qwen-vl-text] coord item[66]: text=003470 20.2.41.64, bbox=[855, 812, 980, 875]
2026-08-07 04:51:43,051 INFO     29 [qwen-vl-text] coord item[67]: text=003470 20.2.41.64, bbox=[37, 856, 112, 900]
2026-08-07 04:51:43,051 INFO     29 [qwen-vl-text] coord item[68]: text=003470 20.2.41.64, bbox=[184, 856, 260, 900]
2026-08-07 04:51:43,051 INFO     29 [qwen-vl-text] coord item[69]: text=003470 20.2.41.64, bbox=[487, 856, 563, 900]
2026-08-07 04:51:43,051 INFO     29 [qwen-vl-text] coord item[70]: text=003470 20.2.41.64, bbox=[633, 856, 710, 900]
2026-08-07 04:51:43,051 INFO     29 [qwen-vl-text] coord item[71]: text=003470 20.2.41.64, bbox=[710, 832, 835, 900]
2026-08-07 04:51:43,051 INFO     29 [qwen-vl-text] coord item[72]: text=003470 20.2.41.64, bbox=[855, 856, 980, 919]
2026-08-07 04:51:43,052 INFO     29 [qwen-vl-text] coord item[73]: text=003470 20.2.41.64, bbox=[37, 900, 112, 944]
2026-08-07 04:51:43,052 INFO     29 [qwen-vl-text] coord item[74]: text=003470 20.2.41.64, bbox=[184, 900, 260, 944]
2026-08-07 04:51:43,052 INFO     29 [qwen-vl-text] coord item[75]: text=003470 20.2.41.64, bbox=[487, 900, 563, 944]
2026-08-07 04:51:43,052 INFO     29 [qwen-vl-text] coord item[76]: text=003470 20.2.41.64, bbox=[633, 900, 710, 944]
2026-08-07 04:51:43,052 INFO     29 [qwen-vl-text] coord item[77]: text=003470 20.2.41.64, bbox=[710, 876, 835, 944]
2026-08-07 04:51:43,052 INFO     29 [qwen-vl-text] coord item[78]: text=003470 20.2.41.64, bbox=[855, 900, 980, 963]
2026-08-07 04:51:43,052 INFO     29 [qwen-vl-text] coord item[79]: text=003470 20.2.41.64, bbox=[37, 944, 112, 988]
2026-08-07 04:51:43,052 INFO     29 [qwen-vl-text] coord item[80]: text=003470 20.2.41.64, bbox=[184, 944, 260, 988]
2026-08-07 04:51:43,052 INFO     29 [qwen-vl-text] coord item[81]: text=003470 20.2.41.64, bbox=[487, 944, 563, 988]
2026-08-07 04:51:43,052 INFO     29 [qwen-vl-text] coord item[82]: text=003470 20.2.41.64, bbox=[633, 944, 710, 988]
2026-08-07 04:51:43,053 INFO     29 [qwen-vl-text] coord item[83]: text=003470 20.2.41.64, bbox=[710, 920, 835, 988]
2026-08-07 04:51:43,053 INFO     29 [qwen-vl-text] coord item[84]: text=003470 20.2.41.64, bbox=[855, 944, 980, 1007]
2026-08-07 04:51:43,053 INFO     29 [qwen-vl-text] coord item[85]: text=003470 20.2.41.64, bbox=[37, 988, 112, 1032]
2026-08-07 04:51:43,053 INFO     29 [qwen-vl-text] coord item[86]: text=003470 20.2.41.64, bbox=[184, 988, 260, 1032]
2026-08-07 04:51:43,053 INFO     29 [qwen-vl-text] coord item[87]: text=003470 20.2.41.64, bbox=[487, 988, 563, 1032]
2026-08-07 04:51:43,053 INFO     29 [qwen-vl-text] coord item[88]: text=003470 20.2.41.64, bbox=[633, 988, 710, 1032]
2026-08-07 04:51:43,053 INFO     29 [qwen-vl-text] coord item[89]: text=003470 20.2.41.64, bbox=[710, 964, 835, 1032]
2026-08-07 04:51:43,053 INFO     29 [qwen-vl-text] coord item[90]: text=003470 20.2.41.64, bbox=[855, 988, 980, 1051]
2026-08-07 04:51:43,054 INFO     29 [qwen-vl-text] coord item[91]: text=003470 20.2.41.64, bbox=[37, 1032, 112, 1076]
2026-08-07 04:51:43,054 INFO     29 [qwen-vl-text] coord item[92]: text=003470 20.2.41.64, bbox=[184, 1032, 260, 1076]
2026-08-07 04:51:43,054 INFO     29 [qwen-vl-text] coord item[93]: text=003470 20.2.41.64, bbox=[487, 1032, 563, 1076]
2026-08-07 04:51:43,054 INFO     29 [qwen-vl-text] coord item[94]: text=003470 20.2.41.64, bbox=[633, 1032, 710, 1076]
2026-08-07 04:51:43,054 INFO     29 [qwen-vl-text] coord item[95]: text=003470 20.2.41.64, bbox=[710, 1008, 835, 1076]
2026-08-07 04:51:43,054 INFO     29 [qwen-vl-text] coord item[96]: text=003470 20.2.41.64, bbox=[855, 1032, 980, 1095]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[97]: text=003470 20.2.41.64, bbox=[37, 1076, 112, 1120]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[98]: text=003470 20.2.41.64, bbox=[184, 1076, 260, 1120]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[99]: text=003470 20.2.41.64, bbox=[487, 1076, 563, 1120]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[100]: text=003470 20.2.41.64, bbox=[633, 1076, 710, 1120]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[101]: text=003470 20.2.41.64, bbox=[710, 1052, 835, 1120]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[102]: text=003470 20.2.41.64, bbox=[855, 1076, 980, 1139]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[103]: text=003470 20.2.41.64, bbox=[37, 1120, 112, 1164]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[104]: text=003470 20.2.41.64, bbox=[184, 1120, 260, 1164]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[105]: text=003470 20.2.41.64, bbox=[487, 1120, 563, 1164]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[106]: text=003470 20.2.41.64, bbox=[633, 1120, 710, 1164]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[107]: text=003470 20.2.41.64, bbox=[710, 1096, 835, 1164]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[108]: text=003470 20.2.41.64, bbox=[855, 1120, 980, 1183]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[109]: text=003470 20.2.41.64, bbox=[37, 1164, 112, 1208]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[110]: text=003470 20.2.41.64, bbox=[184, 1164, 260, 1208]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[111]: text=003470 20.2.41.64, bbox=[487, 1164, 563, 1208]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[112]: text=003470 20.2.41.64, bbox=[633, 1164, 710, 1208]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[113]: text=003470 20.2.41.64, bbox=[710, 1140, 835, 1208]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[114]: text=003470 20.2.41.64, bbox=[855, 1164, 980, 1227]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[115]: text=003470 20.2.41.64, bbox=[37, 1208, 112, 1252]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[116]: text=003470 20.2.41.64, bbox=[184, 1208, 260, 1252]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[117]: text=003470 20.2.41.64, bbox=[487, 1208, 563, 1252]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[118]: text=003470 20.2.41.64, bbox=[633, 1208, 710, 1252]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[119]: text=003470 20.2.41.64, bbox=[710, 1184, 835, 1252]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[120]: text=003470 20.2.41.64, bbox=[855, 1208, 980, 1271]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[121]: text=003470 20.2.41.64, bbox=[37, 1252, 112, 1296]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[122]: text=003470 20.2.41.64, bbox=[184, 1252, 260, 1296]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[123]: text=003470 20.2.41.64, bbox=[487, 1252, 563, 1296]
2026-08-07 04:51:43,055 INFO     29 [qwen-vl-text] coord item[124]: text=003470 20.2.41.64, bbox=[633, 1252, 710, 1296]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[125]: text=003470 20.2.41.64, bbox=[710, 1228, 835, 1296]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[126]: text=003470 20.2.41.64, bbox=[855, 1252, 980, 1315]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[127]: text=003470 20.2.41.64, bbox=[37, 1296, 112, 1340]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[128]: text=003470 20.2.41.64, bbox=[184, 1296, 260, 1340]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[129]: text=003470 20.2.41.64, bbox=[487, 1296, 563, 1340]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[130]: text=003470 20.2.41.64, bbox=[633, 1296, 710, 1340]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[131]: text=003470 20.2.41.64, bbox=[710, 1272, 835, 1340]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[132]: text=003470 20.2.41.64, bbox=[855, 1296, 980, 1359]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[133]: text=003470 20.2.41.64, bbox=[37, 1340, 112, 1384]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[134]: text=003470 20.2.41.64, bbox=[184, 1340, 260, 1384]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[135]: text=003470 20.2.41.64, bbox=[487, 1340, 563, 1384]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[136]: text=003470 20.2.41.64, bbox=[633, 1340, 710, 1384]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[137]: text=003470 20.2.41.64, bbox=[710, 1316, 835, 1384]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[138]: text=003470 20.2.41.64, bbox=[855, 1340, 980, 1403]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[139]: text=003470 20.2.41.64, bbox=[37, 1384, 112, 1428]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[140]: text=003470 20.2.41.64, bbox=[184, 1384, 260, 1428]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[141]: text=003470 20.2.41.64, bbox=[487, 1384, 563, 1428]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[142]: text=003470 20.2.41.64, bbox=[633, 1384, 710, 1428]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[143]: text=003470 20.2.41.64, bbox=[710, 1360, 835, 1428]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[144]: text=003470 20.2.41.64, bbox=[855, 1384, 980, 1447]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[145]: text=003470 20.2.41.64, bbox=[37, 1428, 112, 1472]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[146]: text=003470 20.2.41.64, bbox=[184, 1428, 260, 1472]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[147]: text=003470 20.2.41.64, bbox=[487, 1428, 563, 1472]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[148]: text=003470 20.2.41.64, bbox=[633, 1428, 710, 1472]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[149]: text=003470 20.2.41.64, bbox=[710, 1404, 835, 1472]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[150]: text=003470 20.2.41.64, bbox=[855, 1428, 980, 1491]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[151]: text=003470 20.2.41.64, bbox=[37, 1472, 112, 1516]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[152]: text=003470 20.2.41.64, bbox=[184, 1472, 260, 1516]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[153]: text=003470 20.2.41.64, bbox=[487, 1472, 563, 1516]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[154]: text=003470 20.2.41.64, bbox=[633, 1472, 710, 1516]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[155]: text=003470 20.2.41.64, bbox=[710, 1448, 835, 1516]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[156]: text=003470 20.2.41.64, bbox=[855, 1472, 980, 1535]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[157]: text=003470 20.2.41.64, bbox=[37, 1516, 112, 1560]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[158]: text=003470 20.2.41.64, bbox=[184, 1516, 260, 1560]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[159]: text=003470 20.2.41.64, bbox=[487, 1516, 563, 1560]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[160]: text=003470 20.2.41.64, bbox=[633, 1516, 710, 1560]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[161]: text=003470 20.2.41.64, bbox=[710, 1492, 835, 1560]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[162]: text=003470 20.2.41.64, bbox=[855, 1516, 980, 1579]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[163]: text=003470 20.2.41.64, bbox=[37, 1560, 112, 1604]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[164]: text=003470 20.2.41.64, bbox=[184, 1560, 260, 1604]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[165]: text=003470 20.2.41.64, bbox=[487, 1560, 563, 1604]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[166]: text=003470 20.2.41.64, bbox=[633, 1560, 710, 1604]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[167]: text=003470 20.2.41.64, bbox=[710, 1536, 835, 1604]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[168]: text=003470 20.2.41.64, bbox=[855, 1560, 980, 1623]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[169]: text=003470 20.2.41.64, bbox=[37, 1604, 112, 1648]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[170]: text=003470 20.2.41.64, bbox=[184, 1604, 260, 1648]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[171]: text=003470 20.2.41.64, bbox=[487, 1604, 563, 1648]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[172]: text=003470 20.2.41.64, bbox=[633, 1604, 710, 1648]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[173]: text=003470 20.2.41.64, bbox=[710, 1580, 835, 1648]
2026-08-07 04:51:43,056 INFO     29 [qwen-vl-text] coord item[174]: text=003470 20.2.41.64, bbox=[855, 1604, 980, 1667]
2026-08-07 04:51:43,062 INFO     29 [qwen-vl-text] page=3 — 864/864 coords, api_time=74.4s
2026-08-07 04:51:43,093 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5097454, prompt_len=1118
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
2026-08-07 04:52:00,718 INFO     29 [qwen-vl-text] coord API raw response (len=2292):
[
	{"text": "编辑", "bbox": [103, 38, 124, 54]},
	{"text": "功能", "bbox": [137, 38, 158, 54]},
	{"text": "表格", "bbox": [171, 38, 191, 54]},
	{"text": "签名", "bbox": [204, 38, 224, 54]},
	{"text": "其他", "bbox": [238, 38, 258, 54]},
	{"text": "打印", "bbox": [100, 98, 120, 113]},
	{"text": "预览", "bbox": [135, 98, 155, 113]},
	{"text": "验证CA签名", "bbox": [168, 98, 220, 113]},
	{"text": "手工解锁", "bbox": [240, 98, 279, 113]},
	{"text": "删除", "bbox": [298, 98, 318, 113]},
	{"text": "病历参考", "bbox": [332, 98, 371, 113]},
	{"text": "更新数据", "bbox": [385, 98, 424, 113]},
	{"text": "加载全部病程", "bbox": [440, 98, 499, 113]},
	{"text": "个人模板管理", "bbox": [513, 98, 572, 113]},
	{"text": "返回", "bbox": [593, 98, 612, 113]},
	{"text": "腹部:", "bbox": [107, 142, 124, 165]},
	{"text": "视诊: 外形: 腹部外形正常", "bbox": [176, 179, 396, 204]},
	{"text": "腹围: 未测", "bbox": [492, 180, 576, 204]},
	{"text": "脐部: 正常", "bbox": [708, 180, 792, 204]},
	{"text": "胃形: 未见", "bbox": [244, 216, 328, 241]},
	{"text": "肠形: 未见", "bbox": [371, 216, 456, 241]},
	{"text": "蠕动波: 未见", "bbox": [492, 216, 594, 241]},
	{"text": "腹式呼吸: 正常", "bbox": [708, 216, 827, 241]},
	{"text": "腹壁静脉曲张: 无", "bbox": [244, 253, 380, 278]},
	{"text": "腹壁其它情况: 无", "bbox": [244, 289, 380, 314]},
	{"text": "触诊: 全腹柔软", "bbox": [176, 326, 312, 351]},
	{"text": "压痛反跳痛: 无压痛及反跳痛", "bbox": [244, 362, 465, 387]},
	{"text": "波动感: 无", "bbox": [244, 398, 354, 423]},
	{"text": "振水声: 无", "bbox": [474, 398, 568, 423]},
	{"text": "腹部包块: 腹部未触及包块", "bbox": [244, 435, 449, 460]},
	{"text": "肝脏: 肝脏肋下未触及", "bbox": [244, 471, 422, 496]},
	{"text": "胆囊: 未触及, Murphy征阴性", "bbox": [244, 508, 473, 533]},
	{"text": "脾脏: 脾脏肋下未触及", "bbox": [244, 544, 422, 569]},
	{"text": "肾脏: 未触及", "bbox": [244, 580, 354, 605]},
	{"text": "输尿管压痛点: 无压痛", "bbox": [242, 617, 413, 642]},
	{"text": "叩诊: 肝浊音界: 正常,", "bbox": [174, 654, 368, 679]},
	{"text": "肝上界位于锁骨中线, 第五肋间", "bbox": [515, 654, 753, 679]},
	{"text": "移动性浊音: 阴性,", "bbox": [242, 690, 385, 715]},
	{"text": "肾区叩痛: 无", "bbox": [515, 690, 629, 715]},
	{"text": "听诊: 肠鸣音无明显增强或减弱, 未闻及血管杂音", "bbox": [174, 726, 563, 751]},
	{"text": "肛门直肠: 未查", "bbox": [107, 763, 223, 788]},
	{"text": "生殖器: 未查", "bbox": [107, 799, 223, 824]},
	{"text": "脊柱四肢:", "bbox": [107, 836, 179, 860]},
	{"text": "脊柱外形: 脊柱正常生理弯曲", "bbox": [140, 871, 359, 896]}
]
2026-08-07 04:52:00,718 INFO     29 [qwen-vl-text] coord API: raw_items=44, valid_items=44, elapsed=17.6s
2026-08-07 04:52:00,718 INFO     29 [qwen-vl-text] coord item[0]: text=编辑, bbox=[103, 38, 124, 54]
2026-08-07 04:52:00,718 INFO     29 [qwen-vl-text] coord item[1]: text=功能, bbox=[137, 38, 158, 54]
2026-08-07 04:52:00,718 INFO     29 [qwen-vl-text] coord item[2]: text=表格, bbox=[171, 38, 191, 54]
2026-08-07 04:52:00,718 INFO     29 [qwen-vl-text] coord item[3]: text=签名, bbox=[204, 38, 224, 54]
2026-08-07 04:52:00,718 INFO     29 [qwen-vl-text] coord item[4]: text=其他, bbox=[238, 38, 258, 54]
2026-08-07 04:52:00,718 INFO     29 [qwen-vl-text] coord item[5]: text=打印, bbox=[100, 98, 120, 113]
2026-08-07 04:52:00,718 INFO     29 [qwen-vl-text] coord item[6]: text=预览, bbox=[135, 98, 155, 113]
2026-08-07 04:52:00,718 INFO     29 [qwen-vl-text] coord item[7]: text=验证CA签名, bbox=[168, 98, 220, 113]
2026-08-07 04:52:00,718 INFO     29 [qwen-vl-text] coord item[8]: text=手工解锁, bbox=[240, 98, 279, 113]
2026-08-07 04:52:00,718 INFO     29 [qwen-vl-text] coord item[9]: text=删除, bbox=[298, 98, 318, 113]
2026-08-07 04:52:00,718 INFO     29 [qwen-vl-text] coord item[10]: text=病历参考, bbox=[332, 98, 371, 113]
2026-08-07 04:52:00,718 INFO     29 [qwen-vl-text] coord item[11]: text=更新数据, bbox=[385, 98, 424, 113]
2026-08-07 04:52:00,718 INFO     29 [qwen-vl-text] coord item[12]: text=加载全部病程, bbox=[440, 98, 499, 113]
2026-08-07 04:52:00,718 INFO     29 [qwen-vl-text] coord item[13]: text=个人模板管理, bbox=[513, 98, 572, 113]
2026-08-07 04:52:00,718 INFO     29 [qwen-vl-text] coord item[14]: text=返回, bbox=[593, 98, 612, 113]
2026-08-07 04:52:00,718 INFO     29 [qwen-vl-text] coord item[15]: text=腹部:, bbox=[107, 142, 124, 165]
2026-08-07 04:52:00,718 INFO     29 [qwen-vl-text] coord item[16]: text=视诊: 外形: 腹部外形正常, bbox=[176, 179, 396, 204]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[17]: text=腹围: 未测, bbox=[492, 180, 576, 204]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[18]: text=脐部: 正常, bbox=[708, 180, 792, 204]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[19]: text=胃形: 未见, bbox=[244, 216, 328, 241]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[20]: text=肠形: 未见, bbox=[371, 216, 456, 241]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[21]: text=蠕动波: 未见, bbox=[492, 216, 594, 241]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[22]: text=腹式呼吸: 正常, bbox=[708, 216, 827, 241]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[23]: text=腹壁静脉曲张: 无, bbox=[244, 253, 380, 278]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[24]: text=腹壁其它情况: 无, bbox=[244, 289, 380, 314]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[25]: text=触诊: 全腹柔软, bbox=[176, 326, 312, 351]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[26]: text=压痛反跳痛: 无压痛及反跳痛, bbox=[244, 362, 465, 387]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[27]: text=波动感: 无, bbox=[244, 398, 354, 423]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[28]: text=振水声: 无, bbox=[474, 398, 568, 423]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[29]: text=腹部包块: 腹部未触及包块, bbox=[244, 435, 449, 460]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[30]: text=肝脏: 肝脏肋下未触及, bbox=[244, 471, 422, 496]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[31]: text=胆囊: 未触及, Murphy征阴性, bbox=[244, 508, 473, 533]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[32]: text=脾脏: 脾脏肋下未触及, bbox=[244, 544, 422, 569]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[33]: text=肾脏: 未触及, bbox=[244, 580, 354, 605]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[34]: text=输尿管压痛点: 无压痛, bbox=[242, 617, 413, 642]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[35]: text=叩诊: 肝浊音界: 正常,, bbox=[174, 654, 368, 679]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[36]: text=肝上界位于锁骨中线, 第五肋间, bbox=[515, 654, 753, 679]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[37]: text=移动性浊音: 阴性,, bbox=[242, 690, 385, 715]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[38]: text=肾区叩痛: 无, bbox=[515, 690, 629, 715]
2026-08-07 04:52:00,719 INFO     29 [qwen-vl-text] coord item[39]: text=听诊: 肠鸣音无明显增强或减弱, 未闻及血管杂音, bbox=[174, 726, 563, 751]
2026-08-07 04:52:00,720 INFO     29 [qwen-vl-text] coord item[40]: text=肛门直肠: 未查, bbox=[107, 763, 223, 788]
2026-08-07 04:52:00,720 INFO     29 [qwen-vl-text] coord item[41]: text=生殖器: 未查, bbox=[107, 799, 223, 824]
2026-08-07 04:52:00,720 INFO     29 [qwen-vl-text] coord item[42]: text=脊柱四肢:, bbox=[107, 836, 179, 860]
2026-08-07 04:52:00,720 INFO     29 [qwen-vl-text] coord item[43]: text=脊柱外形: 脊柱正常生理弯曲, bbox=[140, 871, 359, 896]
2026-08-07 04:52:00,721 INFO     29 [qwen-vl-text] page=4 — 44/44 coords, api_time=17.6s
2026-08-07 04:52:00,734 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5198409, prompt_len=1001
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共14行）
["70 四 肢：四肢无畸形，未见杵状指（趾），未见静脉曲张，双下肢无凹陷性水肿", "关 节：各关节未见异常，活动无受限", "肌 肉：未见肌肉萎缩，肌张力正常。四肢肌力5级。", "神经系统：", "浅反射：双侧浅反射正常引出", "深反射：双侧深反射正常引出", "病理反射：未引出", "脑膜刺激征：阴性", "专科情况", "神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下肢无凹陷性水肿。", "实验室及器械检查结果", "(2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm", "，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋巴结彩超", "：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。"]

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
2026-08-07 04:52:07,531 INFO     29 [qwen-vl-text] coord API raw response (len=983):
[
	{"text": "70 四 肢：四肢无畸形，未见杵状指（趾），未见静脉曲张，双下肢无凹陷性水肿", "bbox": [16, 160, 748, 202]},
	{"text": "关 节：各关节未见异常，活动无受限", "bbox": [55, 208, 402, 244]},
	{"text": "肌 肉：未见肌肉萎缩，肌张力正常。四肢肌力5级。", "bbox": [55, 252, 516, 287]},
	{"text": "神经系统：", "bbox": [18, 295, 103, 325]},
	{"text": "浅反射：双侧浅反射正常引出", "bbox": [55, 338, 324, 371],
	"bbox": [55, 338, 324, 371]},
	{"text": "深反射：双侧深反射正常引出", "bbox": [55, 378, 324, 410]},
	{"text": "病理反射：未引出", "bbox": [55, 420, 237, 451]},
	{"text": "脑膜刺激征：阴性", "bbox": [55, 462, 247, 494]},
	{"text": "专科情况", "bbox": [460, 505, 556, 539]},
	{"text": "神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下肢无凹陷性水肿。", "bbox": [20, 595, 915, 628]},
	{"text": "实验室及器械检查结果", "bbox": [385, 641, 626, 675]},
	{"text": "(2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm", "bbox": [32, 692, 984, 721]},
	{"text": "，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋巴结彩超", "bbox": [25, 731, 980, 761]},
	{"text": "：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。", "bbox": [25, 770, 538, 800]}
]
2026-08-07 04:52:07,531 INFO     29 [qwen-vl-text] coord API: raw_items=14, valid_items=14, elapsed=6.8s
2026-08-07 04:52:07,531 INFO     29 [qwen-vl-text] coord item[0]: text=70 四 肢：四肢无畸形，未见杵状指（趾），未见静脉曲张，双下肢无凹陷性水肿, bbox=[16, 160, 748, 202]
2026-08-07 04:52:07,531 INFO     29 [qwen-vl-text] coord item[1]: text=关 节：各关节未见异常，活动无受限, bbox=[55, 208, 402, 244]
2026-08-07 04:52:07,531 INFO     29 [qwen-vl-text] coord item[2]: text=肌 肉：未见肌肉萎缩，肌张力正常。四肢肌力5级。, bbox=[55, 252, 516, 287]
2026-08-07 04:52:07,531 INFO     29 [qwen-vl-text] coord item[3]: text=神经系统：, bbox=[18, 295, 103, 325]
2026-08-07 04:52:07,531 INFO     29 [qwen-vl-text] coord item[4]: text=浅反射：双侧浅反射正常引出, bbox=[55, 338, 324, 371]
2026-08-07 04:52:07,531 INFO     29 [qwen-vl-text] coord item[5]: text=深反射：双侧深反射正常引出, bbox=[55, 378, 324, 410]
2026-08-07 04:52:07,531 INFO     29 [qwen-vl-text] coord item[6]: text=病理反射：未引出, bbox=[55, 420, 237, 451]
2026-08-07 04:52:07,531 INFO     29 [qwen-vl-text] coord item[7]: text=脑膜刺激征：阴性, bbox=[55, 462, 247, 494]
2026-08-07 04:52:07,531 INFO     29 [qwen-vl-text] coord item[8]: text=专科情况, bbox=[460, 505, 556, 539]
2026-08-07 04:52:07,531 INFO     29 [qwen-vl-text] coord item[9]: text=神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下肢无凹陷性水肿。, bbox=[20, 595, 915, 628]
2026-08-07 04:52:07,531 INFO     29 [qwen-vl-text] coord item[10]: text=实验室及器械检查结果, bbox=[385, 641, 626, 675]
2026-08-07 04:52:07,531 INFO     29 [qwen-vl-text] coord item[11]: text=(2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm, bbox=[32, 692, 984, 721]
2026-08-07 04:52:07,531 INFO     29 [qwen-vl-text] coord item[12]: text=，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋巴结彩超, bbox=[25, 731, 980, 761]
2026-08-07 04:52:07,531 INFO     29 [qwen-vl-text] coord item[13]: text=：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。, bbox=[25, 770, 538, 800]
2026-08-07 04:52:07,532 INFO     29 [qwen-vl-text] page=5 — 14/14 coords, api_time=6.8s
2026-08-07 04:52:07,557 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7017107, prompt_len=1576
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
2026-08-07 04:52:20,483 INFO     29 [qwen-vl-text] coord API raw response (len=1891):
[
	{"text": "2026-02-28 18:30", "bbox": [31, 108, 180, 132]},
	{"text": "男，因“咳嗽、咳痰1月余”于2026-02-28 15:23入非急诊步行入科。", "bbox": [226, 147, 775, 174]},
	{"text": "病例特点如下：1、老年期男性，起病缓，病程短。2、患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，", "bbox": [71, 183, 961, 209]},
	{"text": "伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。3、既往史：平素", "bbox": [32, 220, 961, 247]},
	{"text": "健康状况：良好。既往病史：否认高血压、冠心病、糖尿病史。传染病史：否，否认肝炎、结核或其他传染病史。预", "bbox": [32, 257, 971, 284]},
	{"text": "防接种史：正规。过敏史：否认过敏史。外伤史：否认外伤史。手术史：2年前曾行尿道结石手术，具体不详。输血", "bbox": [32, 294, 969, 321]},
	{"text": "史：否认输血史。系统回顾：无特殊。否认新冠肺炎流行病接触史。4、查体：T：36.8℃，P：75次/分，R：21次/分", "bbox": [32, 331, 969, 358]},
	{"text": "，BP：138/72mmHg。神志清楚，正常面容，皮肤巩膜无黄染，全身浅表淋巴结未扪及肿大，颈静脉无怒张。胸廓对称", "bbox": [32, 368, 969, 395]},
	{"text": "无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常，双肺叩诊呈清音，双肺呼吸音", "bbox": [32, 405, 967, 432]},
	{"text": "清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音。心界不大，心率75次/分，心律齐，各瓣膜区未闻及杂音。腹", "bbox": [32, 442, 967, 469]},
	{"text": "部外形正常，全腹柔软，无压痛及反跳痛，腹部未触及包块，肝脏肋下未触及，脾脏肋下未触及。移动性浊音阴性。", "bbox": [32, 479, 956, 506]},
	{"text": "双下肢无凹陷性水肿。浅反射：双侧浅反射正常引出。深反射：双侧深反射正常引出。病理反射：未引出。脑膜刺激", "bbox": [32, 516, 965, 543]},
	{"text": "征：阴性5、专科情况：神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下", "bbox": [32, 553, 963, 580]},
	{"text": "肢无凹陷性水肿。6、辅助检查：（2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组", "bbox": [32, 590, 965, 617]},
	{"text": "织肿块，最大截断面约77mm*60mm，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧", "bbox": [32, 627, 964, 654]},
	{"text": "胸膜肥厚、钙化。浅表淋巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。", "bbox": [32, 664, 800, 691]},
	{"text": "初步诊断：1.肺部阴影", "bbox": [34, 702, 212, 728]},
	{"text": "2.细菌性肺炎", "bbox": [125, 738, 232, 765]},
	{"text": "诊断依据：1.老年男性，起步缓，病程短", "bbox": [35, 775, 357, 802]},
	{"text": "2.咳嗽，咳淡黄色粘液痰", "bbox": [125, 812, 323, 838]},
	{"text": "3.外院胸部CT提示右肺下叶后基底段软组织肿块", "bbox": [125, 849, 500, 875]},
	{"text": "鉴别诊断。", "bbox": [36, 881, 111, 900]},
	{"text": "1.肺结核球", "bbox": [159, 885, 248, 901]}
]
2026-08-07 04:52:20,483 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=12.9s
2026-08-07 04:52:20,483 INFO     29 [qwen-vl-text] coord item[0]: text=2026-02-28 18:30, bbox=[31, 108, 180, 132]
2026-08-07 04:52:20,483 INFO     29 [qwen-vl-text] coord item[1]: text=男，因“咳嗽、咳痰1月余”于2026-02-28 15:23入非急诊步行入科。, bbox=[226, 147, 775, 174]
2026-08-07 04:52:20,483 INFO     29 [qwen-vl-text] coord item[2]: text=病例特点如下：1、老年期男性，起病缓，病程短。2、患者及家属共诉1月余前无明显诱因下出现阵发性咳嗽，, bbox=[71, 183, 961, 209]
2026-08-07 04:52:20,483 INFO     29 [qwen-vl-text] coord item[3]: text=伴咳痰，咳少量淡黄色痰，无发热、寒战、咯血、呼吸困难，无胸闷、胸痛、盗汗、心慌等不适。3、既往史：平素, bbox=[32, 220, 961, 247]
2026-08-07 04:52:20,483 INFO     29 [qwen-vl-text] coord item[4]: text=健康状况：良好。既往病史：否认高血压、冠心病、糖尿病史。传染病史：否，否认肝炎、结核或其他传染病史。预, bbox=[32, 257, 971, 284]
2026-08-07 04:52:20,483 INFO     29 [qwen-vl-text] coord item[5]: text=防接种史：正规。过敏史：否认过敏史。外伤史：否认外伤史。手术史：2年前曾行尿道结石手术，具体不详。输血, bbox=[32, 294, 969, 321]
2026-08-07 04:52:20,483 INFO     29 [qwen-vl-text] coord item[6]: text=史：否认输血史。系统回顾：无特殊。否认新冠肺炎流行病接触史。4、查体：T：36.8℃，P：75次/分，R：21次/分, bbox=[32, 331, 969, 358]
2026-08-07 04:52:20,483 INFO     29 [qwen-vl-text] coord item[7]: text=，BP：138/72mmHg。神志清楚，正常面容，皮肤巩膜无黄染，全身浅表淋巴结未扪及肿大，颈静脉无怒张。胸廓对称, bbox=[32, 368, 969, 395]
2026-08-07 04:52:20,483 INFO     29 [qwen-vl-text] coord item[8]: text=无畸形，无局部隆起或凹陷，胸壁无压痛，呼吸节律规整。双侧乳房对称，未见异常，双肺叩诊呈清音，双肺呼吸音, bbox=[32, 405, 967, 432]
2026-08-07 04:52:20,483 INFO     29 [qwen-vl-text] coord item[9]: text=清，可闻及少量湿啰音，未闻及干啰音及胸膜摩擦音。心界不大，心率75次/分，心律齐，各瓣膜区未闻及杂音。腹, bbox=[32, 442, 967, 469]
2026-08-07 04:52:20,483 INFO     29 [qwen-vl-text] coord item[10]: text=部外形正常，全腹柔软，无压痛及反跳痛，腹部未触及包块，肝脏肋下未触及，脾脏肋下未触及。移动性浊音阴性。, bbox=[32, 479, 956, 506]
2026-08-07 04:52:20,483 INFO     29 [qwen-vl-text] coord item[11]: text=双下肢无凹陷性水肿。浅反射：双侧浅反射正常引出。深反射：双侧深反射正常引出。病理反射：未引出。脑膜刺激, bbox=[32, 516, 965, 543]
2026-08-07 04:52:20,483 INFO     29 [qwen-vl-text] coord item[12]: text=征：阴性5、专科情况：神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下, bbox=[32, 553, 963, 580]
2026-08-07 04:52:20,484 INFO     29 [qwen-vl-text] coord item[13]: text=肢无凹陷性水肿。6、辅助检查：（2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组, bbox=[32, 590, 965, 617]
2026-08-07 04:52:20,484 INFO     29 [qwen-vl-text] coord item[14]: text=织肿块，最大截断面约77mm*60mm，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧, bbox=[32, 627, 964, 654]
2026-08-07 04:52:20,484 INFO     29 [qwen-vl-text] coord item[15]: text=胸膜肥厚、钙化。浅表淋巴结彩超：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。, bbox=[32, 664, 800, 691]
2026-08-07 04:52:20,484 INFO     29 [qwen-vl-text] coord item[16]: text=初步诊断：1.肺部阴影, bbox=[34, 702, 212, 728]
2026-08-07 04:52:20,484 INFO     29 [qwen-vl-text] coord item[17]: text=2.细菌性肺炎, bbox=[125, 738, 232, 765]
2026-08-07 04:52:20,484 INFO     29 [qwen-vl-text] coord item[18]: text=诊断依据：1.老年男性，起步缓，病程短, bbox=[35, 775, 357, 802]
2026-08-07 04:52:20,484 INFO     29 [qwen-vl-text] coord item[19]: text=2.咳嗽，咳淡黄色粘液痰, bbox=[125, 812, 323, 838]
2026-08-07 04:52:20,484 INFO     29 [qwen-vl-text] coord item[20]: text=3.外院胸部CT提示右肺下叶后基底段软组织肿块, bbox=[125, 849, 500, 875]
2026-08-07 04:52:20,484 INFO     29 [qwen-vl-text] coord item[21]: text=鉴别诊断。, bbox=[36, 881, 111, 900]
2026-08-07 04:52:20,484 INFO     29 [qwen-vl-text] coord item[22]: text=1.肺结核球, bbox=[159, 885, 248, 901]
2026-08-07 04:52:20,485 INFO     29 [qwen-vl-text] page=6 — 23/23 coords, api_time=12.9s
2026-08-07 04:52:20,503 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7290009, prompt_len=1513
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
2026-08-07 04:52:35,665 INFO     29 [qwen-vl-text] coord API raw response (len=2273):
[
	{"text": "编辑", "bbox": [21, 47, 44, 64]},
	{"text": "功能", "bbox": [59, 47, 82, 64]},
	{"text": "表格", "bbox": [96, 47, 118, 64]},
	{"text": "签名", "bbox": [132, 47, 154, 64]},
	{"text": "其他", "bbox": [169, 47, 191, 64]},
	{"text": "打印", "bbox": [19, 115, 41, 131]},
	{"text": "预览", "bbox": [56, 115, 79, 131]},
	{"text": "验证CA签名", "bbox": [93, 115, 150, 131]},
	{"text": "手工解锁", "bbox": [170, 115, 213, 131]},
	{"text": "删除", "bbox": [234, 115, 256, 131]},
	{"text": "病历参考", "bbox": [270, 115, 313, 131]},
	{"text": "更新数据", "bbox": [330, 115, 373, 131]},
	{"text": "加载全部病程", "bbox": [388, 115, 453, 131]},
	{"text": "个人模板管理", "bbox": [468, 115, 533, 131]},
	{"text": "返回", "bbox": [555, 115, 577, 131]},
	{"text": "鉴别诊断：", "bbox": [27, 167, 110, 193]},
	{"text": "1.肺结核球：多见于年轻患者，病灶多见于结核好发部位，如肺上叶尖后段和下叶背段，直径一般<3", "bbox": [159, 167, 990, 195]},
	{"text": "cm。一般无症状，病灶边界清楚，密度高，可有包膜。有时含钙化点，周围有卫星灶。", "bbox": [122, 207, 820, 237]},
	{"text": "2.急性粟粒性肺结核：应与弥漫型细支气管肺泡癌相鉴别。通常粟粒型肺结核患者年龄较轻，有发热", "bbox": [159, 247, 987, 277]},
	{"text": "，盗汗等全身中毒症状，呼吸道症状不明显。x线表现为细小、分布均匀、密度较淡的粟粒样结节病灶。", "bbox": [123, 288, 975, 317]},
	{"text": "而细支气管—肺泡细胞癌两肺多有大小不等的结节状播散病灶，边界清楚、密度较高，进行性发展和增大", "bbox": [123, 330, 983, 359]},
	{"text": "，且有进行性呼吸困难。", "bbox": [123, 370, 321, 398]},
	{"text": "3.肺炎：若无毒性症状，抗生素治疗后肺部阴影吸收缓慢，或同一部位反复发生肺炎时，应考虑到肺", "bbox": [160, 411, 982, 440]},
	{"text": "癌可能。肺部慢性炎症机化，形成团块状的炎性假瘤，也易与肺癌相混淆。但炎性假瘤往往形态不整，边", "bbox": [124, 451, 982, 480]},
	{"text": "缘不齐，核心密度较高，易伴有胸膜增厚，病灶长期无明显变化。", "bbox": [125, 491, 650, 520]},
	{"text": "4.肺脓肿：起病急，中毒症状严重，多有寒战、高热、咳嗽、咳大量脓臭痰等症状。肺部x线表现为", "bbox": [163, 531, 977, 560]},
	{"text": "均匀的大片状炎性阴影，空洞内常见较深液平。结合纤支镜检查和痰脱落细胞检查可以鉴别。", "bbox": [127, 571, 872, 600]},
	{"text": "5.纵隔淋巴瘤：颇似中央型肺癌，常为双侧性，可有发热等全身症状，需病理诊断。", "bbox": [163, 611, 835, 640]},
	{"text": "VTE血栓风险评估：创建时间:2026-02-28 15:37:11,评估节点:入院,量表名称:Padua评分,分数:0,评分描述:低危,", "bbox": [35, 652, 970, 681]},
	{"text": "预防措施:undefined", "bbox": [130, 692, 293, 720]},
	{"text": "VTE出血风险评估：创建时间:2026-02-28 18:35:54,评估节点:入院,量表名称:内科出血风险评估,分数:1,评分描述：", "bbox": [36, 732, 972, 761]},
	{"text": "低危,预防措施:undefined", "bbox": [130, 772, 340, 801]},
	{"text": "诊疗计划：1.内科护理常规,II级护理。", "bbox": [37, 812, 355, 841]},
	{"text": "2.完善必要辅助检查如血肿瘤标志物、痰液化验、胸部增强CT、支气管镜检查或浅表淋巴结及肺穿刺活检", "bbox": [128, 852, 970, 882]}
]
2026-08-07 04:52:35,665 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=15.2s
2026-08-07 04:52:35,665 INFO     29 [qwen-vl-text] coord item[0]: text=编辑, bbox=[21, 47, 44, 64]
2026-08-07 04:52:35,665 INFO     29 [qwen-vl-text] coord item[1]: text=功能, bbox=[59, 47, 82, 64]
2026-08-07 04:52:35,665 INFO     29 [qwen-vl-text] coord item[2]: text=表格, bbox=[96, 47, 118, 64]
2026-08-07 04:52:35,665 INFO     29 [qwen-vl-text] coord item[3]: text=签名, bbox=[132, 47, 154, 64]
2026-08-07 04:52:35,666 INFO     29 [qwen-vl-text] coord item[4]: text=其他, bbox=[169, 47, 191, 64]
2026-08-07 04:52:35,666 INFO     29 [qwen-vl-text] coord item[5]: text=打印, bbox=[19, 115, 41, 131]
2026-08-07 04:52:35,666 INFO     29 [qwen-vl-text] coord item[6]: text=预览, bbox=[56, 115, 79, 131]
2026-08-07 04:52:35,666 INFO     29 [qwen-vl-text] coord item[7]: text=验证CA签名, bbox=[93, 115, 150, 131]
2026-08-07 04:52:35,666 INFO     29 [qwen-vl-text] coord item[8]: text=手工解锁, bbox=[170, 115, 213, 131]
2026-08-07 04:52:35,666 INFO     29 [qwen-vl-text] coord item[9]: text=删除, bbox=[234, 115, 256, 131]
2026-08-07 04:52:35,666 INFO     29 [qwen-vl-text] coord item[10]: text=病历参考, bbox=[270, 115, 313, 131]
2026-08-07 04:52:35,666 INFO     29 [qwen-vl-text] coord item[11]: text=更新数据, bbox=[330, 115, 373, 131]
2026-08-07 04:52:35,666 INFO     29 [qwen-vl-text] coord item[12]: text=加载全部病程, bbox=[388, 115, 453, 131]
2026-08-07 04:52:35,666 INFO     29 [qwen-vl-text] coord item[13]: text=个人模板管理, bbox=[468, 115, 533, 131]
2026-08-07 04:52:35,666 INFO     29 [qwen-vl-text] coord item[14]: text=返回, bbox=[555, 115, 577, 131]
2026-08-07 04:52:35,666 INFO     29 [qwen-vl-text] coord item[15]: text=鉴别诊断：, bbox=[27, 167, 110, 193]
2026-08-07 04:52:35,666 INFO     29 [qwen-vl-text] coord item[16]: text=1.肺结核球：多见于年轻患者，病灶多见于结核好发部位，如肺上叶尖后段和下叶背段，直径一般<3, bbox=[159, 167, 990, 195]
2026-08-07 04:52:35,666 INFO     29 [qwen-vl-text] coord item[17]: text=cm。一般无症状，病灶边界清楚，密度高，可有包膜。有时含钙化点，周围有卫星灶。, bbox=[122, 207, 820, 237]
2026-08-07 04:52:35,666 INFO     29 [qwen-vl-text] coord item[18]: text=2.急性粟粒性肺结核：应与弥漫型细支气管肺泡癌相鉴别。通常粟粒型肺结核患者年龄较轻，有发热, bbox=[159, 247, 987, 277]
2026-08-07 04:52:35,666 INFO     29 [qwen-vl-text] coord item[19]: text=，盗汗等全身中毒症状，呼吸道症状不明显。x线表现为细小、分布均匀、密度较淡的粟粒样结节病灶。, bbox=[123, 288, 975, 317]
2026-08-07 04:52:35,667 INFO     29 [qwen-vl-text] coord item[20]: text=而细支气管—肺泡细胞癌两肺多有大小不等的结节状播散病灶，边界清楚、密度较高，进行性发展和增大, bbox=[123, 330, 983, 359]
2026-08-07 04:52:35,667 INFO     29 [qwen-vl-text] coord item[21]: text=，且有进行性呼吸困难。, bbox=[123, 370, 321, 398]
2026-08-07 04:52:35,667 INFO     29 [qwen-vl-text] coord item[22]: text=3.肺炎：若无毒性症状，抗生素治疗后肺部阴影吸收缓慢，或同一部位反复发生肺炎时，应考虑到肺, bbox=[160, 411, 982, 440]
2026-08-07 04:52:35,667 INFO     29 [qwen-vl-text] coord item[23]: text=癌可能。肺部慢性炎症机化，形成团块状的炎性假瘤，也易与肺癌相混淆。但炎性假瘤往往形态不整，边, bbox=[124, 451, 982, 480]
2026-08-07 04:52:35,667 INFO     29 [qwen-vl-text] coord item[24]: text=缘不齐，核心密度较高，易伴有胸膜增厚，病灶长期无明显变化。, bbox=[125, 491, 650, 520]
2026-08-07 04:52:35,667 INFO     29 [qwen-vl-text] coord item[25]: text=4.肺脓肿：起病急，中毒症状严重，多有寒战、高热、咳嗽、咳大量脓臭痰等症状。肺部x线表现为, bbox=[163, 531, 977, 560]
2026-08-07 04:52:35,667 INFO     29 [qwen-vl-text] coord item[26]: text=均匀的大片状炎性阴影，空洞内常见较深液平。结合纤支镜检查和痰脱落细胞检查可以鉴别。, bbox=[127, 571, 872, 600]
2026-08-07 04:52:35,667 INFO     29 [qwen-vl-text] coord item[27]: text=5.纵隔淋巴瘤：颇似中央型肺癌，常为双侧性，可有发热等全身症状，需病理诊断。, bbox=[163, 611, 835, 640]
2026-08-07 04:52:35,667 INFO     29 [qwen-vl-text] coord item[28]: text=VTE血栓风险评估：创建时间:2026-02-28 15:37:11,评估节点:入院,量表名称:Padua评分,分数:0,评分描述:低危,, bbox=[35, 652, 970, 681]
2026-08-07 04:52:35,667 INFO     29 [qwen-vl-text] coord item[29]: text=预防措施:undefined, bbox=[130, 692, 293, 720]
2026-08-07 04:52:35,667 INFO     29 [qwen-vl-text] coord item[30]: text=VTE出血风险评估：创建时间:2026-02-28 18:35:54,评估节点:入院,量表名称:内科出血风险评估,分数:1,评分描述：, bbox=[36, 732, 972, 761]
2026-08-07 04:52:35,667 INFO     29 [qwen-vl-text] coord item[31]: text=低危,预防措施:undefined, bbox=[130, 772, 340, 801]
2026-08-07 04:52:35,667 INFO     29 [qwen-vl-text] coord item[32]: text=诊疗计划：1.内科护理常规,II级护理。, bbox=[37, 812, 355, 841]
2026-08-07 04:52:35,667 INFO     29 [qwen-vl-text] coord item[33]: text=2.完善必要辅助检查如血肿瘤标志物、痰液化验、胸部增强CT、支气管镜检查或浅表淋巴结及肺穿刺活检, bbox=[128, 852, 970, 882]
2026-08-07 04:52:35,670 INFO     29 [qwen-vl-text] page=7 — 34/34 coords, api_time=15.2s
2026-08-07 04:52:35,696 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7301526, prompt_len=735
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共4行）
["以确诊，必要时行颅脑MRI、腹部超声、骨扫描或PET-CT等检查以利进一步疾病诊治。", "3.给予吸氧、抗感染及止血、镇痛等对症支持治疗；明确病理类型拟定下一步治疗方案。", "是否需手术治疗：否", "医师签名：姜晓红 住院医师：孙超群"]

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
2026-08-07 04:52:39,627 INFO     29 [qwen-vl-text] coord API raw response (len=298):
```json
[
	{"text": "以确诊，必要时行颅脑MRI、腹部超声、骨扫描或PET-CT等检查以利进一步疾病诊治。", "bbox": [113, 47, 830, 81]},
	{"text": "3.给予吸氧、抗感染及止血、镇痛等对症支持治疗；明确病理类型拟定下一步治疗方案。", "bbox": [113, 91, 848, 124]},
	{"text": "是否需手术治疗：否", "bbox": [18, 131, 178, 159]},
	{"text": "医师签名：姜晓红 住院医师：孙超群", "bbox": [588, 180, 995, 243]}
]
```
2026-08-07 04:52:39,629 INFO     29 [qwen-vl-text] coord API: raw_items=4, valid_items=4, elapsed=3.9s
2026-08-07 04:52:39,629 INFO     29 [qwen-vl-text] coord item[0]: text=以确诊，必要时行颅脑MRI、腹部超声、骨扫描或PET-CT等检查以利进一步疾病诊治。, bbox=[113, 47, 830, 81]
2026-08-07 04:52:39,629 INFO     29 [qwen-vl-text] coord item[1]: text=3.给予吸氧、抗感染及止血、镇痛等对症支持治疗；明确病理类型拟定下一步治疗方案。, bbox=[113, 91, 848, 124]
2026-08-07 04:52:39,629 INFO     29 [qwen-vl-text] coord item[2]: text=是否需手术治疗：否, bbox=[18, 131, 178, 159]
2026-08-07 04:52:39,629 INFO     29 [qwen-vl-text] coord item[3]: text=医师签名：姜晓红 住院医师：孙超群, bbox=[588, 180, 995, 243]
2026-08-07 04:52:39,631 INFO     29 [qwen-vl-text] page=8 — 4/4 coords, api_time=3.9s
2026-08-07 04:52:39,633 INFO     29 [qwen-vl-text] new_positions (1058):
[[0, 386.478, 454.68, 8.33, 28.56], [0, 32.838, 208.816, 27.965, 44.625], [0, 32.838, 799.9, 51.765, 69.02], [0, 96.83, 804.952, 74.97, 91.63], [0, 96.83, 806.636, 98.77, 115.42999999999999], [0, 96.83, 804.952, 121.975, 138.635], [0, 96.83, 804.952, 145.18, 161.84], [0, 96.83, 804.952, 168.385, 185.045], [0, 96.83, 235.76, 192.185, 208.25], [0, 32.838, 235.76, 215.39, 232.04999999999998], [0, 94.304, 385.63599999999997, 238.595, 255.255], [0, 94.304, 415.948, 262.395, 279.055], [0, 94.304, 220.60399999999998, 285.59999999999997, 301.66499999999996], [0, 94.304, 235.76, 308.805, 325.465], [0, 94.304, 235.76, 332.01, 348.66999999999996], [0, 94.304, 393.214, 355.215, 371.875], [0, 94.304, 235.76, 379.015, 395.08], [0, 94.304, 227.34, 402.21999999999997, 418.88], [0, 33.68, 346.904, 425.42499999999995, 442.085], [0, 92.61999999999999, 258.49399999999997, 448.63, 465.28999999999996], [0, 92.61999999999999, 227.34, 471.835, 488.495], [0, 92.61999999999999, 508.568, 495.03999999999996, 511.7], [0, 643.288, 789.7959999999999, 495.03999999999996, 506.34499999999997], [0, 810.846, 831.896, 512.89, 520.625], [0, 799.9, 840.3159999999999, 523.6, 531.3349999999999], [0, 27.785999999999998, 95.146, 519.435, 527.765], [0, 124.616, 191.976, 519.435, 527.765], [0, 759.4839999999999, 824.318, 558.11, 570.01], [0, 757.8, 824.318, 574.175, 581.3149999999999], [1, 88.41, 623.922, 145.775, 163.625], [1, 21.05, 475.72999999999996, 170.765, 187.42499999999998], [1, 21.05, 307.33, 196.35, 212.415], [1, 323.328, 737.592, 243.95, 260.61], [1, 378.9, 492.57, 292.74, 312.96999999999997], [1, 20.208, 90.93599999999999, 324.275, 340.34], [1, 50.519999999999996, 144.82399999999998, 349.265, 365.33], [1, 213.02599999999998, 319.118, 349.265, 365.33], [1, 399.108, 503.51599999999996, 349.265, 365.33], [1, 575.086, 705.596, 349.265, 365.33], [1, 51.361999999999995, 138.088, 378.41999999999996, 394.48499999999996], [1, 213.02599999999998, 295.542, 378.41999999999996, 394.48499999999996], [1, 399.108, 478.256, 378.41999999999996, 394.48499999999996], [1, 574.244, 654.2339999999999, 378.41999999999996, 394.48499999999996], [1, 51.361999999999995, 129.668, 405.78999999999996, 421.85499999999996], [1, 213.02599999999998, 327.538, 405.78999999999996, 421.85499999999996], [1, 399.108, 511.094, 405.78999999999996, 421.85499999999996], [1, 574.244, 654.2339999999999, 405.78999999999996, 421.85499999999996], [1, 51.361999999999995, 129.668, 433.15999999999997, 449.22499999999997], [1, 213.02599999999998, 309.856, 433.15999999999997, 449.22499999999997], [1, 399.108, 510.252, 433.15999999999997, 449.22499999999997], [2, 79.148, 152.402, 4.165, 22.015], [2, 186.924, 252.6, 30.939999999999998, 47.599999999999994], [2, 186.924, 349.43, 55.335, 71.99499999999999], [2, 116.196, 380.584, 81.515, 98.175], [2, 116.196, 315.75, 105.91, 122.57], [2, 116.196, 419.316, 131.495, 148.155], [2, 186.924, 283.75399999999996, 157.07999999999998, 173.73999999999998], [2, 116.196, 244.17999999999998, 181.475, 198.73], [2, 154.928, 298.90999999999997, 207.655, 224.315], [2, 116.196, 234.076, 232.04999999999998, 248.70999999999998], [2, 84.2, 354.48199999999997, 257.635, 274.295], [2, 84.2, 152.402, 282.625, 299.28499999999997], [2, 116.196, 323.328, 307.615, 324.275], [2, 116.196, 508.568, 332.01, 348.66999999999996], [2, 116.196, 508.568, 357.0, 373.65999999999997], [2, 116.196, 586.0319999999999, 381.395, 398.055], [2, 116.196, 630.658, 406.385, 423.04499999999996], [2, 116.196, 337.642, 430.78, 447.44], [2, 131.352, 152.402, 456.36499999999995, 472.43], [2, 112.828, 270.282, 480.76, 497.41999999999996], [2, 419.316, 527.092, 480.76, 497.41999999999996], [2, 634.8679999999999, 710.648, 480.16499999999996, 496.825], [2, 112.828, 270.282, 508.72499999999997, 525.385], [2, 419.316, 582.664, 508.72499999999997, 525.385], [2, 724.962, 789.7959999999999, 523.6, 535.5], [3, 23.576, 511.094, 69.02, 83.3], [3, 31.154, 77.464, 88.06, 108.28999999999999], [3, 154.928, 298.068, 91.63, 114.24], [3, 347.746, 463.09999999999997, 91.63, 114.24], [3, 541.406, 656.76, 91.63, 114.24], [3, 734.2239999999999, 828.528, 91.63, 114.24], [3, 31.996, 814.2139999999999, 111.86, 132.09], [3, 31.996, 94.304, 139.23, 158.26999999999998], [3, 69.886, 447.94399999999996, 165.41, 184.45], [3, 69.886, 481.62399999999997, 192.185, 211.225], [3, 69.886, 258.49399999999997, 218.36499999999998, 238.0], [3, 69.886, 619.712, 245.14, 264.18], [3, 33.68, 94.304, 272.51, 291.55], [3, 69.886, 714.016, 298.69, 317.72999999999996], [3, 69.886, 497.62199999999996, 324.87, 343.90999999999997], [3, 69.886, 207.974, 351.645, 370.685], [3, 69.886, 481.62399999999997, 377.825, 396.865], [3, 139.772, 597.8199999999999, 404.59999999999997, 423.64], [3, 139.772, 344.378, 430.78, 449.82], [3, 139.772, 244.17999999999998, 456.96, 475.405], [3, 139.772, 261.86199999999997, 483.14, 502.17999999999995], [3, 10.946, 210.5, 508.72499999999997, 527.765], [3, 347.746, 463.09999999999997, 498.60999999999996, 529.55], [3, 532.986, 648.34, 498.60999999999996, 529.55], [3, 719.91, 835.264, 498.60999999999996, 529.55], [3, 31.154, 94.304, 359.38, 385.56], [3, 154.928, 218.92, 359.38, 385.56], [3, 410.054, 474.046, 359.38, 385.56], [3, 532.986, 597.8199999999999, 359.38, 385.56], [3, 597.8199999999999, 703.0699999999999, 345.09999999999997, 385.56], [3, 719.91, 825.16, 359.38, 396.865], [3, 31.154, 94.304, 221.935, 248.11499999999998], [3, 154.928, 218.92, 221.935, 248.11499999999998], [3, 410.054, 474.046, 221.935, 248.11499999999998], [3, 532.986, 597.8199999999999, 221.935, 248.11499999999998], [3, 597.8199999999999, 703.0699999999999, 207.655, 248.11499999999998], [3, 719.91, 825.16, 221.935, 259.42], [3, 31.154, 94.304, 272.51, 298.69], [3, 154.928, 218.92, 272.51, 298.69], [3, 410.054, 474.046, 272.51, 298.69], [3, 532.986, 597.8199999999999, 272.51, 298.69], [3, 597.8199999999999, 703.0699999999999, 258.22999999999996, 298.69], [3, 719.91, 825.16, 272.51, 309.995], [3, 31.154, 94.304, 324.87, 351.05], [3, 154.928, 218.92, 324.87, 351.05], [3, 410.054, 474.046, 324.87, 351.05], [3, 532.986, 597.8199999999999, 324.87, 351.05], [3, 597.8199999999999, 703.0699999999999, 309.995, 351.05], [3, 719.91, 825.16, 324.87, 362.35499999999996], [3, 31.154, 94.304, 377.825, 404.005], [3, 154.928, 218.92, 377.825, 404.005], [3, 410.054, 474.046, 377.825, 404.005], [3, 532.986, 597.8199999999999, 377.825, 404.005], [3, 597.8199999999999, 703.0699999999999, 363.54499999999996, 404.005], [3, 719.91, 825.16, 377.825, 415.31], [3, 31.154, 94.304, 430.78, 456.96], [3, 154.928, 218.92, 430.78, 456.96], [3, 410.054, 474.046, 430.78, 456.96], [3, 532.986, 597.8199999999999, 430.78, 456.96], [3, 597.8199999999999, 703.0699999999999, 416.5, 456.96], [3, 719.91, 825.16, 430.78, 468.265], [3, 31.154, 94.304, 483.14, 509.32], [3, 154.928, 218.92, 483.14, 509.32], [3, 410.054, 474.046, 483.14, 509.32], [3, 532.986, 597.8199999999999, 483.14, 509.32], [3, 597.8199999999999, 703.0699999999999, 468.85999999999996, 509.32], [3, 719.91, 825.16, 483.14, 520.625], [3, 31.154, 94.304, 509.32, 535.5], [3, 154.928, 218.92, 509.32, 535.5], [3, 410.054, 474.046, 509.32, 535.5], [3, 532.986, 597.8199999999999, 509.32, 535.5], [3, 597.8199999999999, 703.0699999999999, 495.03999999999996, 535.5], [3, 719.91, 825.16, 509.32, 546.805], [3, 31.154, 94.304, 535.5, 561.68], [3, 154.928, 218.92, 535.5, 561.68], [3, 410.054, 474.046, 535.5, 561.68], [3, 532.986, 597.8199999999999, 535.5, 561.68], [3, 597.8199999999999, 703.0699999999999, 521.22, 561.68], [3, 719.91, 825.16, 535.5, 572.985], [3, 31.154, 94.304, 561.68, 587.86], [3, 154.928, 218.92, 561.68, 587.86], [3, 410.054, 474.046, 561.68, 587.86], [3, 532.986, 597.8199999999999, 561.68, 587.86], [3, 597.8199999999999, 703.0699999999999, 547.4, 587.86], [3, 719.91, 825.16, 561.68, 599.165], [3, 31.154, 94.304, 587.86, 614.04], [3, 154.928, 218.92, 587.86, 614.04], [3, 410.054, 474.046, 587.86, 614.04], [3, 532.986, 597.8199999999999, 587.86, 614.04], [3, 597.8199999999999, 703.0699999999999, 573.5799999999999, 614.04], [3, 719.91, 825.16, 587.86, 625.345], [3, 31.154, 94.304, 614.04, 640.22], [3, 154.928, 218.92, 614.04, 640.22], [3, 410.054, 474.046, 614.04, 640.22], [3, 532.986, 597.8199999999999, 614.04, 640.22], [3, 597.8199999999999, 703.0699999999999, 599.76, 640.22], [3, 719.91, 825.16, 614.04, 651.525], [3, 31.154, 94.304, 640.22, 666.4], [3, 154.928, 218.92, 640.22, 666.4], [3, 410.054, 474.046, 640.22, 666.4], [3, 532.986, 597.8199999999999, 640.22, 666.4], [3, 597.8199999999999, 703.0699999999999, 625.9399999999999, 666.4], [3, 719.91, 825.16, 640.22, 677.7049999999999], [3, 31.154, 94.304, 666.4, 692.5799999999999], [3, 154.928, 218.92, 666.4, 692.5799999999999], [3, 410.054, 474.046, 666.4, 692.5799999999999], [3, 532.986, 597.8199999999999, 666.4, 692.5799999999999], [3, 597.8199999999999, 703.0699999999999, 652.12, 692.5799999999999], [3, 719.91, 825.16, 666.4, 703.885], [3, 31.154, 94.304, 692.5799999999999, 718.76], [3, 154.928, 218.92, 692.5799999999999, 718.76], [3, 410.054, 474.046, 692.5799999999999, 718.76], [3, 532.986, 597.8199999999999, 692.5799999999999, 718.76], [3, 597.8199999999999, 703.0699999999999, 678.3, 718.76], [3, 719.91, 825.16, 692.5799999999999, 730.0649999999999], [3, 31.154, 94.304, 718.76, 744.9399999999999], [3, 154.928, 218.92, 718.76, 744.9399999999999], [3, 410.054, 474.046, 718.76, 744.9399999999999], [3, 532.986, 597.8199999999999, 718.76, 744.9399999999999], [3, 597.8199999999999, 703.0699999999999, 704.48, 744.9399999999999], [3, 719.91, 825.16, 718.76, 756.245], [3, 31.154, 94.304, 744.9399999999999, 771.12], [3, 154.928, 218.92, 744.9399999999999, 771.12], [3, 410.054, 474.046, 744.9399999999999, 771.12], [3, 532.986, 597.8199999999999, 744.9399999999999, 771.12], [3, 597.8199999999999, 703.0699999999999, 730.66, 771.12], [3, 719.91, 825.16, 744.9399999999999, 782.425], [3, 31.154, 94.304, 771.12, 797.3], [3, 154.928, 218.92, 771.12, 797.3], [3, 410.054, 474.046, 771.12, 797.3], [3, 532.986, 597.8199999999999, 771.12, 797.3], [3, 597.8199999999999, 703.0699999999999, 756.8399999999999, 797.3], [3, 719.91, 825.16, 771.12, 808.605], [3, 31.154, 94.304, 797.3, 823.48], [3, 154.928, 218.92, 797.3, 823.48], [3, 410.054, 474.046, 797.3, 823.48], [3, 532.986, 597.8199999999999, 797.3, 823.48], [3, 597.8199999999999, 703.0699999999999, 783.02, 823.48], [3, 719.91, 825.16, 797.3, 834.785], [3, 31.154, 94.304, 823.48, 849.66], [3, 154.928, 218.92, 823.48, 849.66], [3, 410.054, 474.046, 823.48, 849.66], [3, 532.986, 597.8199999999999, 823.48, 849.66], [3, 597.8199999999999, 703.0699999999999, 809.1999999999999, 849.66], [3, 719.91, 825.16, 823.48, 860.9649999999999], [3, 31.154, 94.304, 849.66, 875.8399999999999], [3, 154.928, 218.92, 849.66, 875.8399999999999], [3, 410.054, 474.046, 849.66, 875.8399999999999], [3, 532.986, 597.8199999999999, 849.66, 875.8399999999999], [3, 597.8199999999999, 703.0699999999999, 835.38, 875.8399999999999], [3, 719.91, 825.16, 849.66, 887.145], [3, 31.154, 94.304, 875.8399999999999, 902.02], [3, 154.928, 218.92, 875.8399999999999, 902.02], [3, 410.054, 474.046, 875.8399999999999, 902.02], [3, 532.986, 597.8199999999999, 875.8399999999999, 902.02], [3, 597.8199999999999, 703.0699999999999, 861.56, 902.02], [3, 719.91, 825.16, 875.8399999999999, 913.3249999999999], [3, 31.154, 94.304, 902.02, 928.1999999999999], [3, 154.928, 218.92, 902.02, 928.1999999999999], [3, 410.054, 474.046, 902.02, 928.1999999999999], [3, 532.986, 597.8199999999999, 902.02, 928.1999999999999], [3, 597.8199999999999, 703.0699999999999, 887.74, 928.1999999999999], [3, 719.91, 825.16, 902.02, 939.505], [3, 31.154, 94.304, 928.1999999999999, 954.38], [3, 154.928, 218.92, 928.1999999999999, 954.38], [3, 410.054, 474.046, 928.1999999999999, 954.38], [3, 532.986, 597.8199999999999, 928.1999999999999, 954.38], [3, 597.8199999999999, 703.0699999999999, 913.92, 954.38], [3, 719.91, 825.16, 928.1999999999999, 965.685], [3, 31.154, 94.304, 954.38, 980.56], [3, 154.928, 218.92, 954.38, 980.56], [3, 410.054, 474.046, 954.38, 980.56], [3, 532.986, 597.8199999999999, 954.38, 980.56], [3, 597.8199999999999, 703.0699999999999, 940.0999999999999, 980.56], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 719.91, 825.16, 954.38, 991.865], [3, 734.2239999999999, 828.528, 91.63, 114.24], [4, 86.726, 104.408, 22.61, 32.129999999999995], [4, 115.354, 133.036, 22.61, 32.129999999999995], [4, 143.982, 160.822, 22.61, 32.129999999999995], [4, 171.768, 188.608, 22.61, 32.129999999999995], [4, 200.396, 217.236, 22.61, 32.129999999999995], [4, 84.2, 101.03999999999999, 58.309999999999995, 67.235], [4, 113.67, 130.51, 58.309999999999995, 67.235], [4, 141.456, 185.23999999999998, 58.309999999999995, 67.235], [4, 202.07999999999998, 234.91799999999998, 58.309999999999995, 67.235], [4, 250.916, 267.756, 58.309999999999995, 67.235], [4, 279.544, 312.382, 58.309999999999995, 67.235], [4, 324.17, 357.008, 58.309999999999995, 67.235], [4, 370.47999999999996, 420.15799999999996, 58.309999999999995, 67.235], [4, 431.94599999999997, 481.62399999999997, 58.309999999999995, 67.235], [4, 499.306, 515.304, 58.309999999999995, 67.235], [4, 90.094, 104.408, 84.49, 98.175], [4, 148.192, 333.432, 106.505, 121.38], [4, 414.264, 484.99199999999996, 107.1, 121.38], [4, 596.136, 666.864, 107.1, 121.38], [4, 205.44799999999998, 276.176, 128.51999999999998, 143.39499999999998], [4, 312.382, 383.952, 128.51999999999998, 143.39499999999998], [4, 414.264, 500.14799999999997, 128.51999999999998, 143.39499999999998], [4, 596.136, 696.334, 128.51999999999998, 143.39499999999998], [4, 205.44799999999998, 319.96, 150.535, 165.41], [4, 205.44799999999998, 319.96, 171.95499999999998, 186.82999999999998], [4, 148.192, 262.704, 193.97, 208.845], [4, 205.44799999999998, 391.53, 215.39, 230.265], [4, 205.44799999999998, 298.068, 236.81, 251.685], [4, 399.108, 478.256, 236.81, 251.685], [4, 205.44799999999998, 378.058, 258.825, 273.7], [4, 205.44799999999998, 355.324, 280.245, 295.12], [4, 205.44799999999998, 398.26599999999996, 302.26, 317.135], [4, 205.44799999999998, 355.324, 323.68, 338.555], [4, 205.44799999999998, 298.068, 345.09999999999997, 359.97499999999997], [4, 203.76399999999998, 347.746, 367.115, 381.99], [4, 146.50799999999998, 309.856, 389.13, 404.005], [4, 433.63, 634.026, 389.13, 404.005], [4, 203.76399999999998, 324.17, 410.54999999999995, 425.42499999999995], [4, 433.63, 529.6179999999999, 410.54999999999995, 425.42499999999995], [4, 146.50799999999998, 474.046, 431.96999999999997, 446.84499999999997], [4, 90.094, 187.766, 453.98499999999996, 468.85999999999996], [4, 90.094, 187.766, 475.405, 490.28], [4, 90.094, 150.718, 497.41999999999996, 511.7], [4, 117.88, 302.27799999999996, 518.245, 533.12], [5, 13.472, 629.816, 95.19999999999999, 120.19], [5, 46.309999999999995, 338.484, 123.75999999999999, 145.18], [5, 46.309999999999995, 434.472, 149.94, 170.765], [5, 15.155999999999999, 86.726, 175.525, 193.375], [5, 46.309999999999995, 272.808, 201.10999999999999, 220.74499999999998], [5, 46.309999999999995, 272.808, 224.91, 243.95], [5, 46.309999999999995, 199.554, 249.89999999999998, 268.34499999999997], [5, 46.309999999999995, 207.974, 274.89, 293.93], [5, 387.32, 468.152, 300.47499999999997, 320.705], [5, 16.84, 770.43, 354.025, 373.65999999999997], [5, 324.17, 527.092, 381.395, 401.625], [5, 26.944, 828.528, 411.74, 428.995], [5, 21.05, 825.16, 434.945, 452.79499999999996], [5, 21.05, 452.996, 458.15, 476.0], [6, 26.102, 151.56, 64.25999999999999, 78.53999999999999], [6, 190.292, 652.55, 87.46499999999999, 103.53], [6, 59.782, 809.1619999999999, 108.88499999999999, 124.35499999999999], [6, 26.944, 809.1619999999999, 130.9, 146.965], [6, 26.944, 817.582, 152.915, 168.98], [6, 26.944, 815.898, 174.92999999999998, 190.995], [6, 26.944, 815.898, 196.945, 213.01], [6, 26.944, 815.898, 218.95999999999998, 235.02499999999998], [6, 26.944, 814.2139999999999, 240.975, 257.03999999999996], [6, 26.944, 814.2139999999999, 262.99, 279.055], [6, 26.944, 804.952, 285.005, 301.07], [6, 26.944, 812.53, 307.02, 323.085], [6, 26.944, 810.846, 329.03499999999997, 345.09999999999997], [6, 26.944, 812.53, 351.05, 367.115], [6, 26.944, 811.688, 373.065, 389.13], [6, 26.944, 673.6, 395.08, 411.145], [6, 28.628, 178.504, 417.69, 433.15999999999997], [6, 105.25, 195.344, 439.10999999999996, 455.17499999999995], [6, 29.47, 300.594, 461.125, 477.19], [6, 105.25, 271.966, 483.14, 498.60999999999996], [6, 105.25, 421.0, 505.155, 520.625], [6, 30.311999999999998, 93.462, 524.1949999999999, 535.5], [6, 133.878, 208.816, 526.5749999999999, 536.095], [7, 17.682, 37.048, 27.965, 38.08], [7, 49.678, 69.044, 27.965, 38.08], [7, 80.832, 99.356, 27.965, 38.08], [7, 111.14399999999999, 129.668, 27.965, 38.08], [7, 142.298, 160.822, 27.965, 38.08], [7, 15.998, 34.522, 68.425, 77.945], [7, 47.152, 66.518, 68.425, 77.945], [7, 78.306, 126.3, 68.425, 77.945], [7, 143.14, 179.346, 68.425, 77.945], [7, 197.028, 215.552, 68.425, 77.945], [7, 227.34, 263.546, 68.425, 77.945], [7, 277.86, 314.066, 68.425, 77.945], [7, 326.69599999999997, 381.426, 68.425, 77.945], [7, 394.056, 448.786, 68.425, 77.945], [7, 467.31, 485.834, 68.425, 77.945], [7, 22.733999999999998, 92.61999999999999, 99.365, 114.835], [7, 133.878, 833.5799999999999, 99.365, 116.02499999999999], [7, 102.72399999999999, 690.4399999999999, 123.16499999999999, 141.015], [7, 133.878, 831.054, 146.965, 164.815], [7, 103.566, 820.9499999999999, 171.35999999999999, 188.61499999999998], [7, 103.566, 827.6859999999999, 196.35, 213.605], [7, 103.566, 270.282, 220.14999999999998, 236.81], [7, 134.72, 826.8439999999999, 244.545, 261.8], [7, 104.408, 826.8439999999999, 268.34499999999997, 285.59999999999997], [7, 105.25, 547.3, 292.145, 309.4], [7, 137.246, 822.634, 315.945, 333.2], [7, 106.934, 734.2239999999999, 339.745, 357.0], [7, 137.246, 703.0699999999999, 363.54499999999996, 380.79999999999995], [7, 29.47, 816.74, 387.94, 405.195], [7, 109.46, 246.706, 411.74, 428.4], [7, 30.311999999999998, 818.424, 435.53999999999996, 452.79499999999996], [7, 109.46, 286.28, 459.34, 476.59499999999997], [7, 31.154, 298.90999999999997, 483.14, 500.395], [7, 107.776, 816.74, 506.94, 524.79], [8, 95.146, 698.86, 27.965, 48.195], [8, 95.146, 714.016, 54.144999999999996, 73.78], [8, 15.155999999999999, 149.876, 77.945, 94.60499999999999], [8, 495.096, 837.79, 107.1, 144.58499999999998]]
2026-08-07 04:52:39,634 INFO     29 [qwen-vl-text] ═══ DONE ═══ 1058 positions, pages=9, time=193.8s
2026-08-07 04:52:39,650 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-07 04:52:39,651 INFO     29 [Trace] task=26a40982 | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Extractor:Admission | outputs={"chunks": "1 items, types={'AdmissionRecord': 1}", "html": "", "json": "1557 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 11}"}
2026-08-07 04:52:39,651 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-07 04:52:39,651 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:52:39.651+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:52:39,659 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-07 04:52:39,659 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-07 04:52:39,660 INFO     29 [qwen-vl-text] positions(26): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-07 04:52:39,660 INFO     29 [qwen-vl-text] page grouping: [9], lines per page: [26]
2026-08-07 04:52:40,078 INFO     29 [qwen-vl-text] page=9, rect=595x842, img=(1653x2339), dpi=200
2026-08-07 04:52:40,080 INFO     29 [qwen-vl-text] LLM extraction start, text_len=468
2026-08-07 04:52:40,080 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:52:40,080 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 1058, \"bbox_end\": 1083, \"encounter_dates\": [\"2026-03-13\"], \"department\": \"老年医学呼吸内科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "影像检查报告单\n病人 ID:\n姓名:\n性别: 男\n年龄: 67岁\n申请科室: 老年医学呼吸内科\n机器型号: SE-MR4\n住院号\n检查部位: 颅脑颅脑MR平扫及增强+DWI,*钆特酸葡胺注射液【广西HR】\n检查日期: 2026-03-13\n(此报告仅供临床医师诊断参考,不作为疾病证明)\n检查所见:\n左侧基底节区、两侧放射冠、右侧侧脑室前后角旁见小斑片状、斑点状等T1、稍\n长T2信号灶,FLAIR呈高信号,边界欠清,DWI未见弥散受限;余脑实质信号未见异\n常,DWI未见明确弥散受限区,增强扫描未见异常强化灶;静脉窦强化充盈良好,未\n见异常;各脑室及脑沟、裂、池对称性轻度增宽;中线结构无移位。\n诊断意见:\n脑白质病变--改良Fasekas1级;轻度脑萎缩。\n检查技师: 唐成\n报告医师: 郭仟\n审核医师: 张\n报告日期: 2026-03-16 15:13:19\n审核日期: 2026-03-16 18:28:39\n地址: 广西医科大学第一附属医院放射科\n联系电话: 0771-5356934\n“广西HR”解释: 广西影像检查项目互认",
    "role": "user"
  }
]
2026-08-07 04:52:43,479 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:52:43,479 INFO     29 [qwen-vl-text] LLM output (len=492):
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
2026-08-07 04:52:43,490 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4405620, prompt_len=1159
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
2026-08-07 04:52:57,362 INFO     29 [qwen-vl-text] coord API raw response (len=2414):
[
	{"text": "影像检查报告单", "bbox": [360, 141, 643, 172]},
	{"text": "病人 ID:", "bbox": [78, 221, 155, 237], "bbox_2d": [78, 221, 155, 237]},
	{"text": "姓名:", "bbox": [340, 220, 388, 236], "bbox_2d": [340, 220, 388, 236]},
	{"text": "性别: 男", "bbox": [529, 219, 625, 236], "bbox_2d": [529, 219, 625, 236]},
	{"text": "年龄: 67岁", "bbox": [676, 219, 801, 236], "bbox_2d": [676, 219, 801, 236]},
	{"text": "申请科室: 老年医学呼吸内科", "bbox": [80, 247, 327, 271], "bbox_2d": [80, 247, 327, 271]},
	{"text": "机器型号: SE-MR4", "bbox": [340, 247, 514, 264], "bbox_2d": [340, 247, 514, 264]},
	{"text": "住院号", "bbox": [676, 247, 736, 264], "bbox_2d": [676, 247, 736, 264]},
	{"text": "检查部位: 颅脑颅脑MR平扫及增强+DWI,*钆特酸葡胺注射液【广西HR】", "bbox": [78, 273, 590, 306], "bbox_2d": [78, 273, 590, 306]},
	{"text": "检查日期: 2026-03-13", "bbox": [606, 280, 864, 297], "bbox_2d": [606, 280, 864, 297]},
	{"text": "(此报告仅供临床医师诊断参考,不作为疾病证明)", "bbox": [82, 310, 574, 328], "bbox_2d": [82, 310, 574, 328]},
	{"text": "检查所见:", "bbox": [78, 333, 176, 350], "bbox_2d": [78, 333, 176, 350]},
	{"text": "左侧基底节区、两侧放射冠、右侧侧脑室前后角旁见小斑片状、斑点状等T1、稍", "bbox": [82, 359, 928, 377], "bbox_2d": [82, 359, 928, 377]},
	{"text": "长T2信号灶,FLAIR呈高信号,边界欠清,DWI未见弥散受限;余脑实质信号未见异", "bbox": [82, 382, 905, 400], "bbox_2d": [82, 382, 905, 400]},
	{"text": "常,DWI未见明确弥散受限区,增强扫描未见异常强化灶;静脉窦强化充盈良好,未", "bbox": [82, 405, 916, 423], "bbox_2d": [82, 405, 916, 423]},
	{"text": "见异常;各脑室及脑沟、裂、池对称性轻度增宽;中线结构无移位。", "bbox": [82, 428, 754, 446], "bbox_2d": [82, 428, 754, 446]},
	{"text": "诊断意见:", "bbox": [74, 614, 172, 631], "bbox_2d": [74, 614, 172, 631]},
	{"text": "脑白质病变--改良Fasekas1级;轻度脑萎缩。", "bbox": [118, 641, 560, 659], "bbox_2d": [118, 641, 560, 659]},
	{"text": "检查技师: 唐成", "bbox": [73, 768, 214, 784], "bbox_2d": [73, 768, 214, 784]},
	{"text": "报告医师: 郭仟", "bbox": [260, 768, 402, 784], "bbox_2d": [260, 768, 402, 784]},
	{"text": "审核医师: 张", "bbox": [448, 768, 537, 784], "bbox_2d": [448, 768, 537, 784]},
	{"text": "报告日期: 2026-03-16 15:13:19", "bbox": [73, 792, 376, 808], "bbox_2d": [73, 792, 376, 808]},
	{"text": "审核日期: 2026-03-16 18:28:39", "bbox": [560, 792, 866, 808], "bbox_2d": [560, 792, 866, 808]},
	{"text": "地址: 广西医科大学第一附属医院放射科", "bbox": [77, 827, 380, 842], "bbox_2d": [77, 827, 380, 842]},
	{"text": "联系电话: 0771-5356934", "bbox": [404, 827, 590, 842], "bbox_2d": [404, 827, 590, 842]},
	{"text": "“广西HR”解释: 广西影像检查项目互认", "bbox": [622, 827, 920, 842], "bbox_2d": [622, 827, 920, 842]}
]
2026-08-07 04:52:57,362 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=13.9s
2026-08-07 04:52:57,362 INFO     29 [qwen-vl-text] coord item[0]: text=影像检查报告单, bbox=[360, 141, 643, 172]
2026-08-07 04:52:57,362 INFO     29 [qwen-vl-text] coord item[1]: text=病人 ID:, bbox=[78, 221, 155, 237]
2026-08-07 04:52:57,362 INFO     29 [qwen-vl-text] coord item[2]: text=姓名:, bbox=[340, 220, 388, 236]
2026-08-07 04:52:57,362 INFO     29 [qwen-vl-text] coord item[3]: text=性别: 男, bbox=[529, 219, 625, 236]
2026-08-07 04:52:57,362 INFO     29 [qwen-vl-text] coord item[4]: text=年龄: 67岁, bbox=[676, 219, 801, 236]
2026-08-07 04:52:57,363 INFO     29 [qwen-vl-text] coord item[5]: text=申请科室: 老年医学呼吸内科, bbox=[80, 247, 327, 271]
2026-08-07 04:52:57,363 INFO     29 [qwen-vl-text] coord item[6]: text=机器型号: SE-MR4, bbox=[340, 247, 514, 264]
2026-08-07 04:52:57,363 INFO     29 [qwen-vl-text] coord item[7]: text=住院号, bbox=[676, 247, 736, 264]
2026-08-07 04:52:57,363 INFO     29 [qwen-vl-text] coord item[8]: text=检查部位: 颅脑颅脑MR平扫及增强+DWI,*钆特酸葡胺注射液【广西HR】, bbox=[78, 273, 590, 306]
2026-08-07 04:52:57,363 INFO     29 [qwen-vl-text] coord item[9]: text=检查日期: 2026-03-13, bbox=[606, 280, 864, 297]
2026-08-07 04:52:57,363 INFO     29 [qwen-vl-text] coord item[10]: text=(此报告仅供临床医师诊断参考,不作为疾病证明), bbox=[82, 310, 574, 328]
2026-08-07 04:52:57,363 INFO     29 [qwen-vl-text] coord item[11]: text=检查所见:, bbox=[78, 333, 176, 350]
2026-08-07 04:52:57,363 INFO     29 [qwen-vl-text] coord item[12]: text=左侧基底节区、两侧放射冠、右侧侧脑室前后角旁见小斑片状、斑点状等T1、稍, bbox=[82, 359, 928, 377]
2026-08-07 04:52:57,363 INFO     29 [qwen-vl-text] coord item[13]: text=长T2信号灶,FLAIR呈高信号,边界欠清,DWI未见弥散受限;余脑实质信号未见异, bbox=[82, 382, 905, 400]
2026-08-07 04:52:57,363 INFO     29 [qwen-vl-text] coord item[14]: text=常,DWI未见明确弥散受限区,增强扫描未见异常强化灶;静脉窦强化充盈良好,未, bbox=[82, 405, 916, 423]
2026-08-07 04:52:57,364 INFO     29 [qwen-vl-text] coord item[15]: text=见异常;各脑室及脑沟、裂、池对称性轻度增宽;中线结构无移位。, bbox=[82, 428, 754, 446]
2026-08-07 04:52:57,364 INFO     29 [qwen-vl-text] coord item[16]: text=诊断意见:, bbox=[74, 614, 172, 631]
2026-08-07 04:52:57,364 INFO     29 [qwen-vl-text] coord item[17]: text=脑白质病变--改良Fasekas1级;轻度脑萎缩。, bbox=[118, 641, 560, 659]
2026-08-07 04:52:57,364 INFO     29 [qwen-vl-text] coord item[18]: text=检查技师: 唐成, bbox=[73, 768, 214, 784]
2026-08-07 04:52:57,364 INFO     29 [qwen-vl-text] coord item[19]: text=报告医师: 郭仟, bbox=[260, 768, 402, 784]
2026-08-07 04:52:57,364 INFO     29 [qwen-vl-text] coord item[20]: text=审核医师: 张, bbox=[448, 768, 537, 784]
2026-08-07 04:52:57,364 INFO     29 [qwen-vl-text] coord item[21]: text=报告日期: 2026-03-16 15:13:19, bbox=[73, 792, 376, 808]
2026-08-07 04:52:57,364 INFO     29 [qwen-vl-text] coord item[22]: text=审核日期: 2026-03-16 18:28:39, bbox=[560, 792, 866, 808]
2026-08-07 04:52:57,364 INFO     29 [qwen-vl-text] coord item[23]: text=地址: 广西医科大学第一附属医院放射科, bbox=[77, 827, 380, 842]
2026-08-07 04:52:57,364 INFO     29 [qwen-vl-text] coord item[24]: text=联系电话: 0771-5356934, bbox=[404, 827, 590, 842]
2026-08-07 04:52:57,364 INFO     29 [qwen-vl-text] coord item[25]: text=“广西HR”解释: 广西影像检查项目互认, bbox=[622, 827, 920, 842]
2026-08-07 04:52:57,366 INFO     29 [qwen-vl-text] page=9 — 26/26 coords, api_time=13.9s
2026-08-07 04:52:57,366 INFO     29 [qwen-vl-text] new_positions (26):
[[9, 214.2, 382.585, 118.722, 144.82399999999998], [9, 46.41, 92.225, 186.082, 199.554], [9, 202.29999999999998, 230.85999999999999, 185.23999999999998, 198.712], [9, 314.755, 371.875, 184.398, 198.712], [9, 402.21999999999997, 476.59499999999997, 184.398, 198.712], [9, 47.599999999999994, 194.565, 207.974, 228.182], [9, 202.29999999999998, 305.83, 207.974, 222.28799999999998], [9, 402.21999999999997, 437.91999999999996, 207.974, 222.28799999999998], [9, 46.41, 351.05, 229.86599999999999, 257.652], [9, 360.57, 514.0799999999999, 235.76, 250.07399999999998], [9, 48.79, 341.53, 261.02, 276.176], [9, 46.41, 104.72, 280.38599999999997, 294.7], [9, 48.79, 552.16, 302.27799999999996, 317.43399999999997], [9, 48.79, 538.475, 321.644, 336.8], [9, 48.79, 545.02, 341.01, 356.166], [9, 48.79, 448.63, 360.376, 375.532], [9, 44.03, 102.33999999999999, 516.9879999999999, 531.302], [9, 70.21, 333.2, 539.722, 554.8779999999999], [9, 43.434999999999995, 127.33, 646.656, 660.1279999999999], [9, 154.7, 239.19, 646.656, 660.1279999999999], [9, 266.56, 319.515, 646.656, 660.1279999999999], [9, 43.434999999999995, 223.72, 666.864, 680.336], [9, 333.2, 515.27, 666.864, 680.336], [9, 45.815, 226.1, 696.334, 708.9639999999999], [9, 240.38, 351.05, 696.334, 708.9639999999999], [9, 370.09, 547.4, 696.334, 708.9639999999999]]
2026-08-07 04:52:57,366 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=17.7s
2026-08-07 04:52:57,366 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-07 04:52:57,366 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-07 04:52:57,367 INFO     29 [qwen-vl-text] positions(15): [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-07 04:52:57,367 INFO     29 [qwen-vl-text] page grouping: [10, 11], lines per page: [14, 1]
2026-08-07 04:52:57,772 INFO     29 [qwen-vl-text] page=10, rect=595x842, img=(1653x2339), dpi=200
2026-08-07 04:52:58,171 INFO     29 [qwen-vl-text] page=11, rect=595x842, img=(1653x2339), dpi=200
2026-08-07 04:52:58,173 INFO     29 [qwen-vl-text] LLM extraction start, text_len=262
2026-08-07 04:52:58,173 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:52:58,173 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 1084, \"bbox_end\": 1098, \"encounter_dates\": [\"2026-03-10\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "科\n检查部位：全身骨显像 显像剂：99mTc-MDP 临床诊断：1.肺占位性病变,2.细菌性肺炎,3.肺\n剂量：25mCi 部阴影\n（此报告仅供临床医师诊断参考，不作为疾病证明）\n检查所见：\n静脉注射99mTc-MDP 3小时后行全身骨显像前位、后位各1帧：\n全身骨像完整、显影基本清晰。颅骨、胸骨、椎体、肩胛骨、肋骨、骨盆及四肢骨显像剂分\n布未见明显异常改变。\n双肾显影，膀胱部分充盈。\n诊断意见：\n全身骨显像未见明显异常改变。\n报告医师：巫殷豪\n审核医师：彭盛梅\n报告日期：2026-03-10\n广西医科大学第一附属医院",
    "role": "user"
  }
]
2026-08-07 04:53:01,317 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:53:01,317 INFO     29 [qwen-vl-text] LLM output (len=435):
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
2026-08-07 04:53:01,332 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5328166, prompt_len=904
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
2026-08-07 04:53:08,408 INFO     29 [qwen-vl-text] coord API raw response (len=854):
[
	{"text": "科", "bbox": [50, 93, 70, 107]},
	{"text": "检查部位：全身骨显像 显像剂：99mTc-MDP 临床诊断：1.肺占位性病变,2.细菌性肺炎,3.肺", "bbox": [50, 110, 925, 127]},
	{"text": "剂量：25mCi 部阴影", "bbox": [50, 130, 567, 146]},
	{"text": "（此报告仅供临床医师诊断参考，不作为疾病证明）", "bbox": [60, 489, 522, 505]},
	{"text": "检查所见：", "bbox": [50, 508, 141, 523]},
	{"text": "静脉注射99mTc-MDP 3小时后行全身骨显像前位、后位各1帧：", "bbox": [93, 527, 668, 543]},
	{"text": "全身骨像完整、显影基本清晰。颅骨、胸骨、椎体、肩胛骨、肋骨、骨盆及四肢骨显像剂分", "bbox": [93, 547, 923, 564]},
	{"text": "布未见明显异常改变。", "bbox": [50, 567, 248, 582]},
	{"text": "双肾显影，膀胱部分充盈。", "bbox": [93, 586, 334, 602]},
	{"text": "诊断意见：", "bbox": [52, 683, 141, 699]},
	{"text": "全身骨显像未见明显异常改变。", "bbox": [95, 703, 375, 719]},
	{"text": "报告医师：巫殷豪", "bbox": [60, 853, 239, 870]},
	{"text": "审核医师：彭盛梅", "bbox": [356, 853, 550, 877]},
	{"text": "报告日期：2026-03-10", "bbox": [650, 856, 862, 872]}
]
2026-08-07 04:53:08,409 INFO     29 [qwen-vl-text] coord API: raw_items=14, valid_items=14, elapsed=7.1s
2026-08-07 04:53:08,409 INFO     29 [qwen-vl-text] coord item[0]: text=科, bbox=[50, 93, 70, 107]
2026-08-07 04:53:08,409 INFO     29 [qwen-vl-text] coord item[1]: text=检查部位：全身骨显像 显像剂：99mTc-MDP 临床诊断：1.肺占位性病变,2.细菌性肺炎,3.肺, bbox=[50, 110, 925, 127]
2026-08-07 04:53:08,409 INFO     29 [qwen-vl-text] coord item[2]: text=剂量：25mCi 部阴影, bbox=[50, 130, 567, 146]
2026-08-07 04:53:08,409 INFO     29 [qwen-vl-text] coord item[3]: text=（此报告仅供临床医师诊断参考，不作为疾病证明）, bbox=[60, 489, 522, 505]
2026-08-07 04:53:08,409 INFO     29 [qwen-vl-text] coord item[4]: text=检查所见：, bbox=[50, 508, 141, 523]
2026-08-07 04:53:08,409 INFO     29 [qwen-vl-text] coord item[5]: text=静脉注射99mTc-MDP 3小时后行全身骨显像前位、后位各1帧：, bbox=[93, 527, 668, 543]
2026-08-07 04:53:08,409 INFO     29 [qwen-vl-text] coord item[6]: text=全身骨像完整、显影基本清晰。颅骨、胸骨、椎体、肩胛骨、肋骨、骨盆及四肢骨显像剂分, bbox=[93, 547, 923, 564]
2026-08-07 04:53:08,409 INFO     29 [qwen-vl-text] coord item[7]: text=布未见明显异常改变。, bbox=[50, 567, 248, 582]
2026-08-07 04:53:08,409 INFO     29 [qwen-vl-text] coord item[8]: text=双肾显影，膀胱部分充盈。, bbox=[93, 586, 334, 602]
2026-08-07 04:53:08,409 INFO     29 [qwen-vl-text] coord item[9]: text=诊断意见：, bbox=[52, 683, 141, 699]
2026-08-07 04:53:08,409 INFO     29 [qwen-vl-text] coord item[10]: text=全身骨显像未见明显异常改变。, bbox=[95, 703, 375, 719]
2026-08-07 04:53:08,409 INFO     29 [qwen-vl-text] coord item[11]: text=报告医师：巫殷豪, bbox=[60, 853, 239, 870]
2026-08-07 04:53:08,410 INFO     29 [qwen-vl-text] coord item[12]: text=审核医师：彭盛梅, bbox=[356, 853, 550, 877]
2026-08-07 04:53:08,410 INFO     29 [qwen-vl-text] coord item[13]: text=报告日期：2026-03-10, bbox=[650, 856, 862, 872]
2026-08-07 04:53:08,411 INFO     29 [qwen-vl-text] page=10 — 14/14 coords, api_time=7.1s
2026-08-07 04:53:08,434 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6618177, prompt_len=627
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
2026-08-07 04:53:11,085 INFO     29 [qwen-vl-text] coord API raw response (len=70):
```json
[
	{"text": "广西医科大学第一附属医院", "bbox": [342, 72, 834, 104]}
]
```
2026-08-07 04:53:11,085 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=2.7s
2026-08-07 04:53:11,085 INFO     29 [qwen-vl-text] coord item[0]: text=广西医科大学第一附属医院, bbox=[342, 72, 834, 104]
2026-08-07 04:53:11,087 INFO     29 [qwen-vl-text] page=11 — 1/1 coords, api_time=2.7s
2026-08-07 04:53:11,087 INFO     29 [qwen-vl-text] new_positions (15):
[[10, 29.75, 41.65, 78.306, 90.094], [10, 29.75, 550.375, 92.61999999999999, 106.934], [10, 29.75, 337.365, 109.46, 122.932], [10, 35.699999999999996, 310.59, 411.738, 425.21], [10, 29.75, 83.895, 427.736, 440.366], [10, 55.335, 397.46, 443.734, 457.20599999999996], [10, 55.335, 549.185, 460.574, 474.888], [10, 29.75, 147.56, 477.414, 490.044], [10, 55.335, 198.73, 493.412, 506.88399999999996], [10, 30.939999999999998, 83.895, 575.086, 588.558], [10, 56.525, 223.125, 591.9259999999999, 605.398], [10, 35.699999999999996, 142.20499999999998, 718.226, 732.54], [10, 211.82, 327.25, 718.226, 738.434], [10, 386.75, 512.89, 720.752, 734.2239999999999], [11, 203.48999999999998, 496.22999999999996, 60.623999999999995, 87.568]]
2026-08-07 04:53:11,087 INFO     29 [qwen-vl-text] ═══ DONE ═══ 15 positions, pages=2, time=13.7s
2026-08-07 04:53:11,088 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-07 04:53:11,089 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-07 04:53:11,089 INFO     29 [qwen-vl-text] positions(30): [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-07 04:53:11,089 INFO     29 [qwen-vl-text] page grouping: [11], lines per page: [30]
2026-08-07 04:53:11,496 INFO     29 [qwen-vl-text] page=11, rect=595x842, img=(1653x2339), dpi=200
2026-08-07 04:53:11,498 INFO     29 [qwen-vl-text] LLM extraction start, text_len=642
2026-08-07 04:53:11,498 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:53:11,498 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 1099, \"bbox_end\": 1128, \"encounter_dates\": [\"2026-03-11\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "影像检查报告单\n病人ID:\n姓名:\n性别: 男\n年龄: 67岁\n申请科室:\n机器型号: SE-\n床号: 49床\n住院号: 1959\nForce-2\n检查部位: 下腹部,上腹部CT平扫+增强,(新)碘帕醇注射液\n【广西HR】\n检查日期: 2026-03-11\n(此报告仅供临床医师诊断参考,不作为疾病证明)\n检查所见:\n双侧肾上腺见多个结节状稍低/低密度影,较大者大小约1.6cm×1.2cm,增强扫\n描不均匀强化。肝脏各叶比例正常,肝实质内见多发类圆形低密度无强化灶,较大者\n位于S8,大小约1.2cm×1.1cm;余肝实质未见异常密度影及异常强化灶。肝内、外胆\n管未见扩张,胆囊不大,囊壁均匀,囊内密度未见异常。脾脏、胰腺形态、大小、密\n度未见异常,增强扫描未见异常强化,右肾体积缩小,双肾实质内见多个类圆形低密\n度无强化灶,较大者大小约0.9cm×1.5cm;双侧肾盂肾盏及输尿管未见扩张。腹部肠\n管分布正常,管腔未见扩张、积液,腹腔内未见明确肿块影;肝门及腹主动脉旁未见\n增大淋巴结,腹膜腔未见积液。\n诊断意见:\n1.双侧肾上腺占位,考虑转移瘤可能性大,请结合临床;\n2.肝多发囊肿;\n3.右肾萎缩,双肾囊肿。\n检查技师:刘辰民 报告医师:谢金桓 审核医师: 冯涛\n报告日期:2026-03-11 14:21:30 审核日期:2026-03-11 16:15:45\n地址:广西医科大学第一附属医院放射科 联系电话:0771-5356934 “广西HR”解释:广西影像检查项目互认",
    "role": "user"
  }
]
2026-08-07 04:53:11,502 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:53:11.501+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:53:15,979 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:53:15,979 INFO     29 [qwen-vl-text] LLM output (len=662):
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
2026-08-07 04:53:15,998 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6618177, prompt_len=1345
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共30行）
["影像检查报告单", "病人ID:", "姓名:", "性别: 男", "年龄: 67岁", "申请科室:", "机器型号: SE-", "床号: 49床", "住院号: 1959", "Force-2", "检查部位: 下腹部,上腹部CT平扫+增强,(新)碘帕醇注射液", "【广西HR】", "检查日期: 2026-03-11", "(此报告仅供临床医师诊断参考,不作为疾病证明)", "检查所见:", "双侧肾上腺见多个结节状稍低/低密度影,较大者大小约1.6cm×1.2cm,增强扫", "描不均匀强化。肝脏各叶比例正常,肝实质内见多发类圆形低密度无强化灶,较大者", "位于S8,大小约1.2cm×1.1cm;余肝实质未见异常密度影及异常强化灶。肝内、外胆", "管未见扩张,胆囊不大,囊壁均匀,囊内密度未见异常。脾脏、胰腺形态、大小、密", "度未见异常,增强扫描未见异常强化,右肾体积缩小,双肾实质内见多个类圆形低密", "度无强化灶,较大者大小约0.9cm×1.5cm;双侧肾盂肾盏及输尿管未见扩张。腹部肠", "管分布正常,管腔未见扩张、积液,腹腔内未见明确肿块影;肝门及腹主动脉旁未见", "增大淋巴结,腹膜腔未见积液。", "诊断意见:", "1.双侧肾上腺占位,考虑转移瘤可能性大,请结合临床;", "2.肝多发囊肿;", "3.右肾萎缩,双肾囊肿。", "检查技师:刘辰民 报告医师:谢金桓 审核医师: 冯涛", "报告日期:2026-03-11 14:21:30 审核日期:2026-03-11 16:15:45", "地址:广西医科大学第一附属医院放射科 联系电话:0771-5356934 “广西HR”解释:广西影像检查项目互认"]

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
2026-08-07 04:53:28,745 INFO     29 [qwen-vl-text] coord API raw response (len=2017):
```json
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
	{"text": "住院号: 1959", "bbox": [687, 213, 812, 228]},
	{"text": "Force-2", "bbox": [457, 225, 531, 238]},
	{"text": "检查部位: 下腹部,上腹部CT平扫+增强,(新)碘帕醇注射液", "bbox": [78, 240, 609, 255]},
	{"text": "【广西HR】", "bbox": [195, 255, 282, 270]},
	{"text": "检查日期: 2026-03-11", "bbox": [616, 247, 874, 263]},
	{"text": "(此报告仅供临床医师诊断参考,不作为疾病证明)", "bbox": [81, 277, 584, 294]},
	{"text": "检查所见:", "bbox": [78, 301, 177, 318]},
	{"text": "双侧肾上腺见多个结节状稍低/低密度影,较大者大小约1.6cm×1.2cm,增强扫", "bbox": [81, 328, 930, 345]},
	{"text": "描不均匀强化。肝脏各叶比例正常,肝实质内见多发类圆形低密度无强化灶,较大者", "bbox": [81, 352, 940, 369]},
	{"text": "位于S8,大小约1.2cm×1.1cm;余肝实质未见异常密度影及异常强化灶。肝内、外胆", "bbox": [81, 375, 940, 393]},
	{"text": "管未见扩张,胆囊不大,囊壁均匀,囊内密度未见异常。脾脏、胰腺形态、大小、密", "bbox": [81, 399, 940, 417]},
	{"text": "度未见异常,增强扫描未见异常强化,右肾体积缩小,双肾实质内见多个类圆形低密", "bbox": [81, 423, 940, 441]},
	{"text": "度无强化灶,较大者大小约0.9cm×1.5cm;双侧肾盂肾盏及输尿管未见扩张。腹部肠", "bbox": [81, 447, 940, 465]},
	{"text": "管分布正常,管腔未见扩张、积液,腹腔内未见明确肿块影;肝门及腹主动脉旁未见", "bbox": [81, 471, 940, 489]},
	{"text": "增大淋巴结,腹膜腔未见积液。", "bbox": [81, 495, 393, 513]},
	{"text": "诊断意见:", "bbox": [78, 590, 177, 607]},
	{"text": "1.双侧肾上腺占位,考虑转移瘤可能性大,请结合临床;", "bbox": [123, 617, 684, 634]},
	{"text": "2.肝多发囊肿;", "bbox": [123, 641, 268, 658]},
	{"text": "3.右肾萎缩,双肾囊肿。", "bbox": [123, 665, 363, 682]},
	{"text": "检查技师:刘辰民 报告医师:谢金桓 审核医师: 冯涛", "bbox": [78, 745, 641, 763]},
	{"text": "报告日期:2026-03-11 14:21:30 审核日期:2026-03-11 16:15:45", "bbox": [78, 770, 871, 787]},
	{"text": "地址:广西医科大学第一附属医院放射科 联系电话:0771-5356934 “广西HR”解释:广西影像检查项目互认", "bbox": [81, 805, 924, 820]}
]
```
2026-08-07 04:53:28,745 INFO     29 [qwen-vl-text] coord API: raw_items=31, valid_items=31, elapsed=12.7s
2026-08-07 04:53:28,745 INFO     29 [qwen-vl-text] coord item[0]: text=广西医科大学第一附属医院, bbox=[342, 72, 834, 104]
2026-08-07 04:53:28,745 INFO     29 [qwen-vl-text] coord item[1]: text=影像检查报告单, bbox=[444, 110, 731, 140]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[2]: text=病人 ID:, bbox=[78, 184, 156, 199]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[3]: text=姓名:, bbox=[345, 184, 394, 199]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[4]: text=性别: 男, bbox=[538, 184, 634, 199]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[5]: text=年龄: 67岁, bbox=[687, 184, 812, 199]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[6]: text=申请科室:, bbox=[78, 213, 165, 228]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[7]: text=机器型号: SE-, bbox=[345, 213, 488, 228]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[8]: text=床号: 49床, bbox=[538, 213, 658, 228]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[9]: text=住院号: 1959, bbox=[687, 213, 812, 228]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[10]: text=Force-2, bbox=[457, 225, 531, 238]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[11]: text=检查部位: 下腹部,上腹部CT平扫+增强,(新)碘帕醇注射液, bbox=[78, 240, 609, 255]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[12]: text=【广西HR】, bbox=[195, 255, 282, 270]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[13]: text=检查日期: 2026-03-11, bbox=[616, 247, 874, 263]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[14]: text=(此报告仅供临床医师诊断参考,不作为疾病证明), bbox=[81, 277, 584, 294]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[15]: text=检查所见:, bbox=[78, 301, 177, 318]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[16]: text=双侧肾上腺见多个结节状稍低/低密度影,较大者大小约1.6cm×1.2cm,增强扫, bbox=[81, 328, 930, 345]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[17]: text=描不均匀强化。肝脏各叶比例正常,肝实质内见多发类圆形低密度无强化灶,较大者, bbox=[81, 352, 940, 369]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[18]: text=位于S8,大小约1.2cm×1.1cm;余肝实质未见异常密度影及异常强化灶。肝内、外胆, bbox=[81, 375, 940, 393]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[19]: text=管未见扩张,胆囊不大,囊壁均匀,囊内密度未见异常。脾脏、胰腺形态、大小、密, bbox=[81, 399, 940, 417]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[20]: text=度未见异常,增强扫描未见异常强化,右肾体积缩小,双肾实质内见多个类圆形低密, bbox=[81, 423, 940, 441]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[21]: text=度无强化灶,较大者大小约0.9cm×1.5cm;双侧肾盂肾盏及输尿管未见扩张。腹部肠, bbox=[81, 447, 940, 465]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[22]: text=管分布正常,管腔未见扩张、积液,腹腔内未见明确肿块影;肝门及腹主动脉旁未见, bbox=[81, 471, 940, 489]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[23]: text=增大淋巴结,腹膜腔未见积液。, bbox=[81, 495, 393, 513]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[24]: text=诊断意见:, bbox=[78, 590, 177, 607]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[25]: text=1.双侧肾上腺占位,考虑转移瘤可能性大,请结合临床;, bbox=[123, 617, 684, 634]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[26]: text=2.肝多发囊肿;, bbox=[123, 641, 268, 658]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[27]: text=3.右肾萎缩,双肾囊肿。, bbox=[123, 665, 363, 682]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[28]: text=检查技师:刘辰民 报告医师:谢金桓 审核医师: 冯涛, bbox=[78, 745, 641, 763]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[29]: text=报告日期:2026-03-11 14:21:30 审核日期:2026-03-11 16:15:45, bbox=[78, 770, 871, 787]
2026-08-07 04:53:28,746 INFO     29 [qwen-vl-text] coord item[30]: text=地址:广西医科大学第一附属医院放射科 联系电话:0771-5356934 “广西HR”解释:广西影像检查项目互认, bbox=[81, 805, 924, 820]
2026-08-07 04:53:28,749 INFO     29 [qwen-vl-text] page=11 — 30/30 coords, api_time=12.7s
2026-08-07 04:53:28,749 INFO     29 [qwen-vl-text] new_positions (30):
[[11, 203.48999999999998, 496.22999999999996, 60.623999999999995, 87.568], [11, 264.18, 434.945, 92.61999999999999, 117.88], [11, 46.41, 92.82, 154.928, 167.558], [11, 205.27499999999998, 234.42999999999998, 154.928, 167.558], [11, 320.11, 377.22999999999996, 154.928, 167.558], [11, 408.765, 483.14, 154.928, 167.558], [11, 46.41, 98.175, 179.346, 191.976], [11, 205.27499999999998, 290.36, 179.346, 191.976], [11, 320.11, 391.51, 179.346, 191.976], [11, 408.765, 483.14, 179.346, 191.976], [11, 271.91499999999996, 315.945, 189.45, 200.396], [11, 46.41, 362.35499999999996, 202.07999999999998, 214.70999999999998], [11, 116.02499999999999, 167.79, 214.70999999999998, 227.34], [11, 366.52, 520.03, 207.974, 221.446], [11, 48.195, 347.47999999999996, 233.23399999999998, 247.548], [11, 46.41, 105.315, 253.44199999999998, 267.756], [11, 48.195, 553.35, 276.176, 290.49], [11, 48.195, 559.3, 296.384, 310.698], [11, 48.195, 559.3, 315.75, 330.906], [11, 48.195, 559.3, 335.95799999999997, 351.114], [11, 48.195, 559.3, 356.166, 371.322], [11, 48.195, 559.3, 376.37399999999997, 391.53], [11, 48.195, 559.3, 396.582, 411.738], [11, 48.195, 233.83499999999998, 416.78999999999996, 431.94599999999997], [11, 46.41, 105.315, 496.78, 511.094], [11, 73.185, 406.97999999999996, 519.514, 533.828], [11, 73.185, 159.45999999999998, 539.722, 554.036], [11, 73.185, 215.98499999999999, 559.93, 574.244], [11, 46.41, 381.395, 627.29, 642.446], [11, 46.41, 518.245, 648.34, 662.654]]
2026-08-07 04:53:28,750 INFO     29 [qwen-vl-text] ═══ DONE ═══ 30 positions, pages=1, time=17.7s
2026-08-07 04:53:28,750 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-07 04:53:28,751 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-07 04:53:28,751 INFO     29 [qwen-vl-text] positions(34): [[12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-07 04:53:28,751 INFO     29 [qwen-vl-text] page grouping: [12], lines per page: [34]
2026-08-07 04:53:29,147 INFO     29 [qwen-vl-text] page=12, rect=595x842, img=(1653x2339), dpi=200
2026-08-07 04:53:29,149 INFO     29 [qwen-vl-text] LLM extraction start, text_len=769
2026-08-07 04:53:29,149 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:53:29,149 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 1129, \"bbox_end\": 1162, \"encounter_dates\": [\"2026-03-02\"], \"department\": \"老年医学呼吸内科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "广西医科大学第一附属医院\n影像检查报告单\n病人ID:\n姓名:\n男\n年龄: 67岁\n申请科室: 老年医学呼吸内科\n机器型号: SE-\nForce-2\n床号\n号\n检查部位: 胸部CT平扫+增强,*碘海醇注射液【广西HR】\n检查日期: 2026-03-02\n(此报告仅供临床医师诊断参考,不作为疾病证明)\n检查所见:\n两肺尖胸膜下见类圆形透亮影,较大者长径约0.8cm;右肺下叶基底段(Se4:IM144)见团\n块状密度增高灶,大小约为7.7cm×5.1cm×6.9cm,增强扫描中度强化;两肺可见多发实性结节\n影,较大位于右肺下叶外基底段(Se4:IM344),内可见空泡,长径约为1.1cm,增强扫描似见\n血管穿行。右肺中叶、左肺上叶下舌段及两肺下叶见条索状密度增高影;余肺叶内未见异常密\n度影及异常强化灶,右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张,两肺部分支气管\n管壁增厚,管腔变窄,气管、其余支气管通畅;肺门、纵隔结构清楚,纵隔、两侧肺门见多发\n淋巴结,大者短径约1.1cm。两侧胸膜增厚、钙化,胸膜腔未见积液。主动脉、冠状动脉见斑片\n状钙化灶。\n诊断意见:\n1.右肺下叶后基底段软组织肿块,肿瘤性病变?感染性病变?请结合临床及实验室检查;\n2.两肺多发实性结节,建议短期复查;\n3.右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张并两肺炎症;\n4.两肺上叶间隔旁型肺气肿;\n5.纵隔、两侧肺门淋巴结,建议复查;\n6.两侧胸膜肥厚、钙化;\n7.主动脉、冠状动脉硬化。\n检查技师:周春燚 报告医师:肖芳艳 审核医师:\n报告日期:2026-03-03 18:39:05 审核日期:2026-03-04 09:21:01\n地址:广西医科大学第一附属医院放射科 联系电话:0771-5356934 “广西HR”解码:广西影像检查项目互认",
    "role": "user"
  }
]
2026-08-07 04:53:34,287 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:53:34,287 INFO     29 [qwen-vl-text] LLM output (len=794):
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
2026-08-07 04:53:34,302 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5214598, prompt_len=1484
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
2026-08-07 04:53:48,401 INFO     29 [qwen-vl-text] coord API raw response (len=2251):
[
	{"text": "广西医科大学第一附属医院", "bbox": [336, 111, 820, 141]},
	{"text": "影像检查报告单", "bbox": [436, 148, 718, 178]},
	{"text": "病人ID:", "bbox": [74, 222, 150, 238]},
	{"text": "姓名:", "bbox": [338, 222, 388, 238]},
	{"text": "男", "bbox": [607, 222, 625, 237]},
	{"text": "年龄: 67岁", "bbox": [676, 222, 799, 238]},
	{"text": "申请科室: 老年医学呼吸内科", "bbox": [75, 248, 325, 264]},
	{"text": "机器型号: SE-", "bbox": [338, 248, 477, 264]},
	{"text": "Force-2", "bbox": [450, 262, 522, 277]},
	{"text": "床号", "bbox": [528, 250, 568, 266]},
	{"text": "号", "bbox": [695, 250, 734, 266]},
	{"text": "检查部位: 胸部CT平扫+增强,*碘海醇注射液【广西HR】", "bbox": [74, 281, 570, 297]},
	{"text": "检查日期: 2026-03-02", "bbox": [606, 281, 861, 297]},
	{"text": "(此报告仅供临床医师诊断参考,不作为疾病证明)", "bbox": [77, 305, 574, 323]},
	{"text": "检查所见:", "bbox": [75, 331, 173, 348]},
	{"text": "两肺尖胸膜下见类圆形透亮影,较大者长径约0.8cm;右肺下叶基底段(Se4:IM144)见团", "bbox": [80, 356, 918, 372]},
	{"text": "块状密度增高灶,大小约为7.7cm×5.1cm×6.9cm,增强扫描中度强化;两肺可见多发实性结节", "bbox": [80, 373, 918, 389]},
	{"text": "影,较大位于右肺下叶外基底段(Se4:IM344),内可见空泡,长径约为1.1cm,增强扫描似见", "bbox": [80, 390, 918, 406]},
	{"text": "血管穿行。右肺中叶、左肺上叶下舌段及两肺下叶见条索状密度增高影;余肺叶内未见异常密", "bbox": [80, 407, 909, 423]},
	{"text": "度影及异常强化灶,右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张,两肺部分支气管", "bbox": [80, 424, 909, 440]},
	{"text": "管壁增厚,管腔变窄,气管、其余支气管通畅;肺门、纵隔结构清楚,纵隔、两侧肺门见多发", "bbox": [80, 441, 909, 457]},
	{"text": "淋巴结,大者短径约1.1cm。两侧胸膜增厚、钙化,胸膜腔未见积液。主动脉、冠状动脉见斑片", "bbox": [80, 458, 918, 474]},
	{"text": "状钙化灶。", "bbox": [80, 475, 166, 491]},
	{"text": "诊断意见:", "bbox": [75, 625, 173, 643]},
	{"text": "1.右肺下叶后基底段软组织肿块,肿瘤性病变?感染性病变?请结合临床及实验室检查;", "bbox": [119, 650, 899, 666]},
	{"text": "2.两肺多发实性结节,建议短期复查;", "bbox": [119, 667, 452, 683]},
	{"text": "3.右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张并两肺炎症;", "bbox": [119, 684, 735, 699]},
	{"text": "4.两肺上叶间隔旁型肺气肿;", "bbox": [119, 701, 370, 717]},
	{"text": "5.纵隔、两侧肺门淋巴结,建议复查;", "bbox": [119, 718, 452, 734]},
	{"text": "6.两侧胸膜肥厚、钙化;", "bbox": [119, 735, 331, 751]},
	{"text": "7.主动脉、冠状动脉硬化。", "bbox": [119, 752, 352, 768]},
	{"text": "检查技师:周春燚 报告医师:肖芳艳 审核医师:", "bbox": [75, 785, 540, 801]},
	{"text": "报告日期:2026-03-03 18:39:05 审核日期:2026-03-04 09:21:01", "bbox": [75, 811, 866, 827]},
	{"text": "地址:广西医科大学第一附属医院放射科 联系电话:0771-5356934 “广西HR”解码:广西影像检查项目互认", "bbox": [80, 845, 920, 860]}
]
2026-08-07 04:53:48,402 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=14.1s
2026-08-07 04:53:48,402 INFO     29 [qwen-vl-text] coord item[0]: text=广西医科大学第一附属医院, bbox=[336, 111, 820, 141]
2026-08-07 04:53:48,402 INFO     29 [qwen-vl-text] coord item[1]: text=影像检查报告单, bbox=[436, 148, 718, 178]
2026-08-07 04:53:48,402 INFO     29 [qwen-vl-text] coord item[2]: text=病人ID:, bbox=[74, 222, 150, 238]
2026-08-07 04:53:48,402 INFO     29 [qwen-vl-text] coord item[3]: text=姓名:, bbox=[338, 222, 388, 238]
2026-08-07 04:53:48,402 INFO     29 [qwen-vl-text] coord item[4]: text=男, bbox=[607, 222, 625, 237]
2026-08-07 04:53:48,402 INFO     29 [qwen-vl-text] coord item[5]: text=年龄: 67岁, bbox=[676, 222, 799, 238]
2026-08-07 04:53:48,402 INFO     29 [qwen-vl-text] coord item[6]: text=申请科室: 老年医学呼吸内科, bbox=[75, 248, 325, 264]
2026-08-07 04:53:48,402 INFO     29 [qwen-vl-text] coord item[7]: text=机器型号: SE-, bbox=[338, 248, 477, 264]
2026-08-07 04:53:48,402 INFO     29 [qwen-vl-text] coord item[8]: text=Force-2, bbox=[450, 262, 522, 277]
2026-08-07 04:53:48,402 INFO     29 [qwen-vl-text] coord item[9]: text=床号, bbox=[528, 250, 568, 266]
2026-08-07 04:53:48,402 INFO     29 [qwen-vl-text] coord item[10]: text=号, bbox=[695, 250, 734, 266]
2026-08-07 04:53:48,403 INFO     29 [qwen-vl-text] coord item[11]: text=检查部位: 胸部CT平扫+增强,*碘海醇注射液【广西HR】, bbox=[74, 281, 570, 297]
2026-08-07 04:53:48,403 INFO     29 [qwen-vl-text] coord item[12]: text=检查日期: 2026-03-02, bbox=[606, 281, 861, 297]
2026-08-07 04:53:48,403 INFO     29 [qwen-vl-text] coord item[13]: text=(此报告仅供临床医师诊断参考,不作为疾病证明), bbox=[77, 305, 574, 323]
2026-08-07 04:53:48,403 INFO     29 [qwen-vl-text] coord item[14]: text=检查所见:, bbox=[75, 331, 173, 348]
2026-08-07 04:53:48,403 INFO     29 [qwen-vl-text] coord item[15]: text=两肺尖胸膜下见类圆形透亮影,较大者长径约0.8cm;右肺下叶基底段(Se4:IM144)见团, bbox=[80, 356, 918, 372]
2026-08-07 04:53:48,403 INFO     29 [qwen-vl-text] coord item[16]: text=块状密度增高灶,大小约为7.7cm×5.1cm×6.9cm,增强扫描中度强化;两肺可见多发实性结节, bbox=[80, 373, 918, 389]
2026-08-07 04:53:48,403 INFO     29 [qwen-vl-text] coord item[17]: text=影,较大位于右肺下叶外基底段(Se4:IM344),内可见空泡,长径约为1.1cm,增强扫描似见, bbox=[80, 390, 918, 406]
2026-08-07 04:53:48,403 INFO     29 [qwen-vl-text] coord item[18]: text=血管穿行。右肺中叶、左肺上叶下舌段及两肺下叶见条索状密度增高影;余肺叶内未见异常密, bbox=[80, 407, 909, 423]
2026-08-07 04:53:48,403 INFO     29 [qwen-vl-text] coord item[19]: text=度影及异常强化灶,右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张,两肺部分支气管, bbox=[80, 424, 909, 440]
2026-08-07 04:53:48,403 INFO     29 [qwen-vl-text] coord item[20]: text=管壁增厚,管腔变窄,气管、其余支气管通畅;肺门、纵隔结构清楚,纵隔、两侧肺门见多发, bbox=[80, 441, 909, 457]
2026-08-07 04:53:48,403 INFO     29 [qwen-vl-text] coord item[21]: text=淋巴结,大者短径约1.1cm。两侧胸膜增厚、钙化,胸膜腔未见积液。主动脉、冠状动脉见斑片, bbox=[80, 458, 918, 474]
2026-08-07 04:53:48,404 INFO     29 [qwen-vl-text] coord item[22]: text=状钙化灶。, bbox=[80, 475, 166, 491]
2026-08-07 04:53:48,404 INFO     29 [qwen-vl-text] coord item[23]: text=诊断意见:, bbox=[75, 625, 173, 643]
2026-08-07 04:53:48,404 INFO     29 [qwen-vl-text] coord item[24]: text=1.右肺下叶后基底段软组织肿块,肿瘤性病变?感染性病变?请结合临床及实验室检查;, bbox=[119, 650, 899, 666]
2026-08-07 04:53:48,404 INFO     29 [qwen-vl-text] coord item[25]: text=2.两肺多发实性结节,建议短期复查;, bbox=[119, 667, 452, 683]
2026-08-07 04:53:48,404 INFO     29 [qwen-vl-text] coord item[26]: text=3.右肺中叶外段、两肺下叶后、外基底段支气管轻度扩张并两肺炎症;, bbox=[119, 684, 735, 699]
2026-08-07 04:53:48,404 INFO     29 [qwen-vl-text] coord item[27]: text=4.两肺上叶间隔旁型肺气肿;, bbox=[119, 701, 370, 717]
2026-08-07 04:53:48,404 INFO     29 [qwen-vl-text] coord item[28]: text=5.纵隔、两侧肺门淋巴结,建议复查;, bbox=[119, 718, 452, 734]
2026-08-07 04:53:48,404 INFO     29 [qwen-vl-text] coord item[29]: text=6.两侧胸膜肥厚、钙化;, bbox=[119, 735, 331, 751]
2026-08-07 04:53:48,404 INFO     29 [qwen-vl-text] coord item[30]: text=7.主动脉、冠状动脉硬化。, bbox=[119, 752, 352, 768]
2026-08-07 04:53:48,404 INFO     29 [qwen-vl-text] coord item[31]: text=检查技师:周春燚 报告医师:肖芳艳 审核医师:, bbox=[75, 785, 540, 801]
2026-08-07 04:53:48,404 INFO     29 [qwen-vl-text] coord item[32]: text=报告日期:2026-03-03 18:39:05 审核日期:2026-03-04 09:21:01, bbox=[75, 811, 866, 827]
2026-08-07 04:53:48,404 INFO     29 [qwen-vl-text] coord item[33]: text=地址:广西医科大学第一附属医院放射科 联系电话:0771-5356934 “广西HR”解码:广西影像检查项目互认, bbox=[80, 845, 920, 860]
2026-08-07 04:53:48,406 INFO     29 [qwen-vl-text] page=12 — 34/34 coords, api_time=14.1s
2026-08-07 04:53:48,407 INFO     29 [qwen-vl-text] new_positions (34):
[[12, 199.92, 487.9, 93.462, 118.722], [12, 259.42, 427.21, 124.616, 149.876], [12, 44.03, 89.25, 186.924, 200.396], [12, 201.10999999999999, 230.85999999999999, 186.924, 200.396], [12, 361.16499999999996, 371.875, 186.924, 199.554], [12, 402.21999999999997, 475.405, 186.924, 200.396], [12, 44.625, 193.375, 208.816, 222.28799999999998], [12, 201.10999999999999, 283.815, 208.816, 222.28799999999998], [12, 267.75, 310.59, 220.60399999999998, 233.23399999999998], [12, 314.15999999999997, 337.96, 210.5, 223.97199999999998], [12, 413.525, 436.72999999999996, 210.5, 223.97199999999998], [12, 44.03, 339.15, 236.602, 250.07399999999998], [12, 360.57, 512.295, 236.602, 250.07399999999998], [12, 45.815, 341.53, 256.81, 271.966], [12, 44.625, 102.935, 278.702, 293.01599999999996], [12, 47.599999999999994, 546.2099999999999, 299.752, 313.224], [12, 47.599999999999994, 546.2099999999999, 314.066, 327.538], [12, 47.599999999999994, 546.2099999999999, 328.38, 341.852], [12, 47.599999999999994, 540.855, 342.69399999999996, 356.166], [12, 47.599999999999994, 540.855, 357.008, 370.47999999999996], [12, 47.599999999999994, 540.855, 371.322, 384.794], [12, 47.599999999999994, 546.2099999999999, 385.63599999999997, 399.108], [12, 47.599999999999994, 98.77, 399.95, 413.42199999999997], [12, 44.625, 102.935, 526.25, 541.406], [12, 70.80499999999999, 534.905, 547.3, 560.7719999999999], [12, 70.80499999999999, 268.94, 561.614, 575.086], [12, 70.80499999999999, 437.325, 575.928, 588.558], [12, 70.80499999999999, 220.14999999999998, 590.242, 603.7139999999999], [12, 70.80499999999999, 268.94, 604.5559999999999, 618.028], [12, 70.80499999999999, 196.945, 618.87, 632.342], [12, 70.80499999999999, 209.44, 633.184, 646.656], [12, 44.625, 321.3, 660.97, 674.442], [12, 44.625, 515.27, 682.862, 696.334], [12, 47.599999999999994, 547.4, 711.49, 724.12]]
2026-08-07 04:53:48,407 INFO     29 [qwen-vl-text] ═══ DONE ═══ 34 positions, pages=1, time=19.7s
2026-08-07 04:53:48,409 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-07 04:53:48,409 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-07 04:53:48,409 INFO     29 [qwen-vl-text] positions(69): [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0]]
2026-08-07 04:53:48,410 INFO     29 [qwen-vl-text] page grouping: [13], lines per page: [68]
2026-08-07 04:53:48,938 INFO     29 [qwen-vl-text] page=13, rect=595x842, img=(1653x2339), dpi=200
2026-08-07 04:53:48,940 INFO     29 [qwen-vl-text] LLM extraction start, text_len=659
2026-08-07 04:53:48,940 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:53:48,940 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 1163, \"bbox_end\": 1231, \"encounter_dates\": [\"2026-03-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "测量参数值:\n测量项目\n结果\n单位\n参考范围\n测量项目\n结果\n单位\n参考范围\n主动脉根部内径:\n27\nmm\n(20-35)\n左房前后径:\n35\nmm\n(24-39)\n左室舒末前后径:\n53\nmm\n(38-54)\n左室缩末前后径:\n32\nmm\n(24-37)\n室间隔舒末厚:\n10\nmm\n(6-11)\n左室后壁舒末厚:\n10\nmm\n(6-11)\n右室舒末前后径:\n18\nmm\n(15-30)\n右室流出道:\n27\nmm\n(15-32)\n主肺动脉内径:\n22\nmm\n(15-26)\nE/A\n<1\n(0.8-2.0)\ne'/a'\n<1\n(->)\nE/e'\n11.7\n(->)\n超声描述:\n描述:\n1、按比例各房室大小正常，房、室间隔连续完整，室间隔与左室壁厚度正常，静息状态下室壁收\n缩运动有力，未见节段性运动异常。左室收缩功能测定在正常范围，FS:40%，EF:70%，SV:95ml/B\n，CO:6.4L/min，EDV:135ml，心包腔内未探及液性区声像。\n2、三尖瓣形态结构正常，瓣口轻度反流，速度2.4m/s，压差22mmHg，瞬时反流量约2ml（无血流动\n力学意义），余各瓣膜形态结构正常，启闭运动好，二尖瓣血流图示E峰小于A峰。\n3、主动脉根部内径正常，升主动脉内径正常，管壁增厚，弹性降低，主肺动脉内径正常，内回声\n及血流信号未见异常。\n超声诊断:\n1、心脏形态结构及瓣膜功能大致正常。\n2、左室舒张功能降低，收缩功能测定在正常范围，\n诊断医师：吴颖/肖彩意\n报告日期：2026-03-02 10:12:46",
    "role": "user"
  }
]
2026-08-07 04:53:48,943 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:53:48.942+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:53:54,957 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:53:54,957 INFO     29 [qwen-vl-text] LLM output (len=923):
{
  "exam_date": null,
  "report_date": "2026-03-02",
  "exam_name": "心脏超声检查",
  "exam_category": "imaging",
  "body_part": "心脏",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "测量参数值:\n测量项目 结果 单位 参考范围\n主动脉根部内径: 27 mm (20-35)\n左房前后径: 35 mm (24-39)\n左室舒末前后径: 53 mm (38-54)\n左室缩末前后径: 32 mm (24-37)\n室间隔舒末厚: 10 mm (6-11)\n左室后壁舒末厚: 10 mm (6-11)\n右室舒末前后径: 18 mm (15-30)\n右室流出道: 27 mm (15-32)\n主肺动脉内径: 22 mm (15-26)\nE/A <1 (0.8-2.0)\ne'/a' <1 (->)\nE/e' 11.7 (->)\n超声描述:\n1、按比例各房室大小正常，房、室间隔连续完整，室间隔与左室壁厚度正常，静息状态下室壁收缩运动有力，未见节段性运动异常。左室收缩功能测定在正常范围，FS:40%，EF:70%，SV:95ml/B，CO:6.4L/min，EDV:135ml，心包腔内未探及液性区声像。\n2、三尖瓣形态结构正常，瓣口轻度反流，速度2.4m/s，压差22mmHg，瞬时反流量约2ml（无血流动力学意义），余各瓣膜形态结构正常，启闭运动好，二尖瓣血流图示E峰小于A峰。\n3、主动脉根部内径正常，升主动脉内径正常，管壁增厚，弹性降低，主肺动脉内径正常，内回声及血流信号未见异常。",
  "conclusion": "超声诊断:\n1、心脏形态结构及瓣膜功能大致正常。\n2、左室舒张功能降低，收缩功能测定在正常范围，",
  "physician": "吴颖/肖彩意",
  "reviewer": null
}
2026-08-07 04:53:54,977 INFO     29 [qwen-vl-text] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6753644, prompt_len=1476
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共68行）
["测量参数值:", "测量项目", "结果", "单位", "参考范围", "测量项目", "结果", "单位", "参考范围", "主动脉根部内径:", "27", "mm", "(20-35)", "左房前后径:", "35", "mm", "(24-39)", "左室舒末前后径:", "53", "mm", "(38-54)", "左室缩末前后径:", "32", "mm", "(24-37)", "室间隔舒末厚:", "10", "mm", "(6-11)", "左室后壁舒末厚:", "10", "mm", "(6-11)", "右室舒末前后径:", "18", "mm", "(15-30)", "右室流出道:", "27", "mm", "(15-32)", "主肺动脉内径:", "22", "mm", "(15-26)", "E/A", "<1", "(0.8-2.0)", "e'/a'", "<1", "(->)", "E/e'", "11.7", "(->)", "超声描述:", "描述:", "1、按比例各房室大小正常，房、室间隔连续完整，室间隔与左室壁厚度正常，静息状态下室壁收", "缩运动有力，未见节段性运动异常。左室收缩功能测定在正常范围，FS:40%，EF:70%，SV:95ml/B", "，CO:6.4L/min，EDV:135ml，心包腔内未探及液性区声像。", "2、三尖瓣形态结构正常，瓣口轻度反流，速度2.4m/s，压差22mmHg，瞬时反流量约2ml（无血流动", "力学意义），余各瓣膜形态结构正常，启闭运动好，二尖瓣血流图示E峰小于A峰。", "3、主动脉根部内径正常，升主动脉内径正常，管壁增厚，弹性降低，主肺动脉内径正常，内回声", "及血流信号未见异常。", "超声诊断:", "1、心脏形态结构及瓣膜功能大致正常。", "2、左室舒张功能降低，收缩功能测定在正常范围，", "诊断医师：吴颖/肖彩意", "报告日期：2026-03-02 10:12:46"]

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
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord API raw response (len=3633):
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
	{"text": "(->)", "bbox": [402, 462, 424, 474]},
	{"text": "E/e'", "bbox": [500, 461, 528, 474]},
	{"text": "11.7", "bbox": [678, 462, 710, 474]},
	{"text": "(->)", "bbox": [846, 462, 867, 474]},
	{"text": "超声描述:", "bbox": [52, 481, 138, 498]},
	{"text": "描述:", "bbox": [61, 504, 108, 520]},
	{"text": "1、按比例各房室大小正常，房、室间隔连续完整，室间隔与左室壁厚度正常，静息状态下室壁收", "bbox": [61, 523, 914, 540]},
	{"text": "缩运动有力，未见节段性运动异常。左室收缩功能测定在正常范围，FS:40%，EF:70%，SV:95ml/B", "bbox": [61, 543, 914, 560]},
	{"text": "，CO:6.4L/min，EDV:135ml，心包腔内未探及液性区声像。", "bbox": [61, 563, 570, 580]},
	{"text": "2、三尖瓣形态结构正常，瓣口轻度反流，速度2.4m/s，压差22mmHg，瞬时反流量约2ml（无血流动", "bbox": [61, 583, 922, 600]},
	{"text": "力学意义），余各瓣膜形态结构正常，启闭运动好，二尖瓣血流图示E峰小于A峰。", "bbox": [61, 603, 770, 620]},
	{"text": "3、主动脉根部内径正常，升主动脉内径正常，管壁增厚，弹性降低，主肺动脉内径正常，内回声", "bbox": [61, 623, 912, 640]},
	{"text": "及血流信号未见异常。", "bbox": [61, 643, 248, 660]},
	{"text": "超声诊断:", "bbox": [52, 660, 138, 676]},
	{"text": "1、心脏形态结构及瓣膜功能大致正常。", "bbox": [61, 686, 400, 703]},
	{"text": "2、左室舒张功能降低，收缩功能测定在正常范围，", "bbox": [61, 706, 500, 723]},
	{"text": "诊断医师：吴颖/肖彩意", "bbox": [674, 809, 876, 827]},
	{"text": "报告日期：2026-03-02 10:12:46", "bbox": [674, 830, 954, 847]}
]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord API: raw_items=68, valid_items=68, elapsed=20.6s
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[0]: text=测量参数值:, bbox=[52, 314, 159, 332]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[1]: text=测量项目, bbox=[97, 336, 174, 353]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[2]: text=结果, bbox=[232, 337, 265, 350]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[3]: text=单位, bbox=[298, 337, 331, 350]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[4]: text=参考范围, bbox=[378, 337, 447, 350]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[5]: text=测量项目, bbox=[542, 335, 620, 352]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[6]: text=结果, bbox=[678, 337, 711, 350]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[7]: text=单位, bbox=[744, 337, 776, 350]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[8]: text=参考范围, bbox=[824, 337, 891, 350]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[9]: text=主动脉根部内径:, bbox=[57, 358, 177, 371]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[10]: text=27, bbox=[240, 359, 258, 371]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[11]: text=mm, bbox=[304, 361, 324, 371]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[12]: text=(20-35), bbox=[386, 359, 440, 371]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[13]: text=左房前后径:, bbox=[502, 358, 592, 371]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[14]: text=35, bbox=[687, 359, 704, 371]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[15]: text=mm, bbox=[750, 361, 770, 371]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[16]: text=(24-39), bbox=[830, 359, 882, 371]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[17]: text=左室舒末前后径:, bbox=[57, 378, 177, 391]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[18]: text=53, bbox=[240, 379, 258, 391]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[19]: text=mm, bbox=[304, 381, 324, 391]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[20]: text=(38-54), bbox=[386, 379, 440, 391]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[21]: text=左室缩末前后径:, bbox=[502, 378, 624, 391]
2026-08-07 04:54:15,615 INFO     29 [qwen-vl-text] coord item[22]: text=32, bbox=[687, 379, 704, 391]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[23]: text=mm, bbox=[750, 381, 770, 391]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[24]: text=(24-37), bbox=[830, 379, 882, 391]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[25]: text=室间隔舒末厚:, bbox=[57, 399, 159, 412]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[26]: text=10, bbox=[240, 400, 258, 412]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[27]: text=mm, bbox=[304, 402, 324, 412]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[28]: text=(6-11), bbox=[389, 400, 437, 412]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[29]: text=左室后壁舒末厚:, bbox=[502, 399, 624, 412]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[30]: text=10, bbox=[687, 400, 704, 412]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[31]: text=mm, bbox=[750, 402, 770, 412]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[32]: text=(6-11), bbox=[835, 400, 880, 412]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[33]: text=右室舒末前后径:, bbox=[57, 419, 177, 432]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[34]: text=18, bbox=[240, 420, 258, 432]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[35]: text=mm, bbox=[304, 422, 324, 432]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[36]: text=(15-30), bbox=[386, 420, 440, 432]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[37]: text=右室流出道:, bbox=[502, 419, 592, 432]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[38]: text=27, bbox=[687, 420, 704, 432]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[39]: text=mm, bbox=[750, 422, 770, 432]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[40]: text=(15-32), bbox=[830, 420, 882, 432]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[41]: text=主肺动脉内径:, bbox=[57, 440, 159, 453]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[42]: text=22, bbox=[240, 441, 258, 453]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[43]: text=mm, bbox=[304, 443, 324, 453]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[44]: text=(15-26), bbox=[386, 441, 440, 453]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[45]: text=E/A, bbox=[500, 440, 527, 453]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[46]: text=<1, bbox=[687, 441, 701, 453]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[47]: text=(0.8-2.0), bbox=[821, 440, 891, 453]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[48]: text=e'/a', bbox=[57, 461, 93, 474]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[49]: text=<1, bbox=[240, 462, 258, 474]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[50]: text=(->), bbox=[402, 462, 424, 474]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[51]: text=E/e', bbox=[500, 461, 528, 474]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[52]: text=11.7, bbox=[678, 462, 710, 474]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[53]: text=(->), bbox=[846, 462, 867, 474]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[54]: text=超声描述:, bbox=[52, 481, 138, 498]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[55]: text=描述:, bbox=[61, 504, 108, 520]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[56]: text=1、按比例各房室大小正常，房、室间隔连续完整，室间隔与左室壁厚度正常，静息状态下室壁收, bbox=[61, 523, 914, 540]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[57]: text=缩运动有力，未见节段性运动异常。左室收缩功能测定在正常范围，FS:40%，EF:70%，SV:95ml/B, bbox=[61, 543, 914, 560]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[58]: text=，CO:6.4L/min，EDV:135ml，心包腔内未探及液性区声像。, bbox=[61, 563, 570, 580]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[59]: text=2、三尖瓣形态结构正常，瓣口轻度反流，速度2.4m/s，压差22mmHg，瞬时反流量约2ml（无血流动, bbox=[61, 583, 922, 600]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[60]: text=力学意义），余各瓣膜形态结构正常，启闭运动好，二尖瓣血流图示E峰小于A峰。, bbox=[61, 603, 770, 620]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[61]: text=3、主动脉根部内径正常，升主动脉内径正常，管壁增厚，弹性降低，主肺动脉内径正常，内回声, bbox=[61, 623, 912, 640]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[62]: text=及血流信号未见异常。, bbox=[61, 643, 248, 660]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[63]: text=超声诊断:, bbox=[52, 660, 138, 676]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[64]: text=1、心脏形态结构及瓣膜功能大致正常。, bbox=[61, 686, 400, 703]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[65]: text=2、左室舒张功能降低，收缩功能测定在正常范围，, bbox=[61, 706, 500, 723]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[66]: text=诊断医师：吴颖/肖彩意, bbox=[674, 809, 876, 827]
2026-08-07 04:54:15,616 INFO     29 [qwen-vl-text] coord item[67]: text=报告日期：2026-03-02 10:12:46, bbox=[674, 830, 954, 847]
2026-08-07 04:54:15,618 INFO     29 [qwen-vl-text] page=13 — 68/68 coords, api_time=20.6s
2026-08-07 04:54:15,618 INFO     29 [qwen-vl-text] new_positions (68):
[[13, 30.939999999999998, 94.60499999999999, 264.388, 279.544], [13, 57.714999999999996, 103.53, 282.912, 297.226], [13, 138.04, 157.67499999999998, 283.75399999999996, 294.7], [13, 177.31, 196.945, 283.75399999999996, 294.7], [13, 224.91, 265.965, 283.75399999999996, 294.7], [13, 322.49, 368.9, 282.07, 296.384], [13, 403.40999999999997, 423.04499999999996, 283.75399999999996, 294.7], [13, 442.68, 461.71999999999997, 283.75399999999996, 294.7], [13, 490.28, 530.145, 283.75399999999996, 294.7], [13, 33.915, 105.315, 301.436, 312.382], [13, 142.79999999999998, 153.51, 302.27799999999996, 312.382], [13, 180.88, 192.78, 303.962, 312.382], [13, 229.67, 261.8, 302.27799999999996, 312.382], [13, 298.69, 352.24, 301.436, 312.382], [13, 408.765, 418.88, 302.27799999999996, 312.382], [13, 446.25, 458.15, 303.962, 312.382], [13, 493.84999999999997, 524.79, 302.27799999999996, 312.382], [13, 33.915, 105.315, 318.276, 329.222], [13, 142.79999999999998, 153.51, 319.118, 329.222], [13, 180.88, 192.78, 320.80199999999996, 329.222], [13, 229.67, 261.8, 319.118, 329.222], [13, 298.69, 371.28, 318.276, 329.222], [13, 408.765, 418.88, 319.118, 329.222], [13, 446.25, 458.15, 320.80199999999996, 329.222], [13, 493.84999999999997, 524.79, 319.118, 329.222], [13, 33.915, 94.60499999999999, 335.95799999999997, 346.904], [13, 142.79999999999998, 153.51, 336.8, 346.904], [13, 180.88, 192.78, 338.484, 346.904], [13, 231.45499999999998, 260.015, 336.8, 346.904], [13, 298.69, 371.28, 335.95799999999997, 346.904], [13, 408.765, 418.88, 336.8, 346.904], [13, 446.25, 458.15, 338.484, 346.904], [13, 496.825, 523.6, 336.8, 346.904], [13, 33.915, 105.315, 352.798, 363.74399999999997], [13, 142.79999999999998, 153.51, 353.64, 363.74399999999997], [13, 180.88, 192.78, 355.324, 363.74399999999997], [13, 229.67, 261.8, 353.64, 363.74399999999997], [13, 298.69, 352.24, 352.798, 363.74399999999997], [13, 408.765, 418.88, 353.64, 363.74399999999997], [13, 446.25, 458.15, 355.324, 363.74399999999997], [13, 493.84999999999997, 524.79, 353.64, 363.74399999999997], [13, 33.915, 94.60499999999999, 370.47999999999996, 381.426], [13, 142.79999999999998, 153.51, 371.322, 381.426], [13, 180.88, 192.78, 373.006, 381.426], [13, 229.67, 261.8, 371.322, 381.426], [13, 297.5, 313.565, 370.47999999999996, 381.426], [13, 408.765, 417.09499999999997, 371.322, 381.426], [13, 488.495, 530.145, 370.47999999999996, 381.426], [13, 33.915, 55.335, 388.162, 399.108], [13, 142.79999999999998, 153.51, 389.00399999999996, 399.108], [13, 239.19, 252.28, 389.00399999999996, 399.108], [13, 297.5, 314.15999999999997, 388.162, 399.108], [13, 403.40999999999997, 422.45, 389.00399999999996, 399.108], [13, 503.37, 515.865, 389.00399999999996, 399.108], [13, 30.939999999999998, 82.11, 405.002, 419.316], [13, 36.295, 64.25999999999999, 424.368, 437.84], [13, 36.295, 543.8299999999999, 440.366, 454.68], [13, 36.295, 543.8299999999999, 457.20599999999996, 471.52], [13, 36.295, 339.15, 474.046, 488.35999999999996], [13, 36.295, 548.59, 490.88599999999997, 505.2], [13, 36.295, 458.15, 507.726, 522.04], [13, 36.295, 542.64, 524.566, 538.88], [13, 36.295, 147.56, 541.406, 555.72], [13, 30.939999999999998, 82.11, 555.72, 569.192], [13, 36.295, 238.0, 577.612, 591.9259999999999], [13, 36.295, 297.5, 594.452, 608.766], [13, 401.03, 521.22, 681.178, 696.334], [13, 401.03, 567.63, 698.86, 713.174]]
2026-08-07 04:54:15,618 INFO     29 [qwen-vl-text] ═══ DONE ═══ 68 positions, pages=1, time=27.2s
2026-08-07 04:54:15,618 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-07 04:54:15,618 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-07 04:54:15,618 INFO     29 [qwen-vl-text] positions(57): [[25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0]]
2026-08-07 04:54:15,618 INFO     29 [qwen-vl-text] page grouping: [25], lines per page: [57]
2026-08-07 04:54:15,834 INFO     29 [qwen-vl-text] page=25, rect=595x842, img=(1653x2339), dpi=200
2026-08-07 04:54:15,836 INFO     29 [qwen-vl-text] LLM extraction start, text_len=704
2026-08-07 04:54:15,836 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:54:15,836 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 1500, \"bbox_end\": 1556, \"encounter_dates\": [\"2026-03-10\"], \"department\": \"老年呼吸\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "广西金域医学检验实验室\n本报告单经过电子签名认证\nGuangxi Kingmed Center for Clinical Laboratory\n金域医学\nKingMed Diagnostics\n病理诊断报告书\n1/1\n标本条码\n1223023095\n医院\n广西医科大学第一附属医院\n病人姓名\n孔令祈\n科室\n老年呼吸\n病理号\n26018339\n性别\n男\n房/床号\n49\n住院门诊号\n1959880\n年龄\n67岁\n接收时间\n2026-03-08 14:15:50\n申请医生\n项目名称\n免疫组化8项\n送检材料\n肺组织\n临床诊断\n患者电话\n大体描述:\n福尔马林固定标本，核对送检标本、病人姓名和条形码与申请单一致。\n灰红条索状组织3段，长0.5-1.8cm，直径均0.05cm。取1盒全（共1盒蜡块）\n镜下所见：\n诊断意见：\n肺组织穿刺活检：\n-结合免疫组化，符合浸润性黏液型腺癌，请结合临床。\n-免疫组化：CK7（+），CK20（+），Villin（+），TTF-1（散在+），NapsinA（散在+），P40（-），CDX2（-），Ki67（\n热点区约60%+）。\n报告医师：陈明坚\n本检测仅对送检负责，如果对结果有疑义，请在报告发布后7天内与我们联系，多谢合作！\n收样点：广西医科大学第一附属医院-呼吸内\n科\n主检实验室：广西金域\n地址：南宁市西乡塘区总部路3号中国-东盟科技企业孵化基地二期1号厂房一、三、\n四层\n报告专用章\n网址：www.kingmed.com.cn\nGX003SCEJL7RJLY\n报告日期：2026-03-10 21:16:16\n更多报告服务\nCS 扫描全能王\n3亿人都在用的扫描App",
    "role": "user"
  }
]
2026-08-07 04:54:18,751 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-07T04:54:18.750+00:00", "boot_at": "2026-08-07T03:19:18.699+00:00", "pending": 7, "lag": 0, "done": 1, "failed": 0, "current": {"26a40982921a11f18b9f1b2113099832": {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-07 04:54:19,749 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-07 04:54:19,749 INFO     29 [qwen-vl-text] LLM output (len=537):
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
  "findings": "大体描述:\n福尔马林固定标本，核对送检标本、病人姓名和条形码与申请单一致。\n灰红条索状组织3段，长0.5-1.8cm，直径均0.05cm。取1盒全（共1盒蜡块）\n镜下所见：",
  "conclusion": "诊断意见：\n肺组织穿刺活检：\n-结合免疫组化，符合浸润性黏液型腺癌，请结合临床。\n-免疫组化：CK7（+），CK20（+），Villin（+），TTF-1（散在+），NapsinA（散在+），P40（-），CDX2（-），Ki67（\n热点区约60%+）。",
  "physician": "陈明坚",
  "reviewer": null
}
2026-08-07 04:54:19,755 INFO     29 [qwen-vl-text] coord API call start, page=25, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1763221, prompt_len=1488
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共57行）
["广西金域医学检验实验室", "本报告单经过电子签名认证", "Guangxi Kingmed Center for Clinical Laboratory", "金域医学", "KingMed Diagnostics", "病理诊断报告书", "1/1", "标本条码", "1223023095", "医院", "广西医科大学第一附属医院", "病人姓名", "孔令祈", "科室", "老年呼吸", "病理号", "26018339", "性别", "男", "房/床号", "49", "住院门诊号", "1959880", "年龄", "67岁", "接收时间", "2026-03-08 14:15:50", "申请医生", "项目名称", "免疫组化8项", "送检材料", "肺组织", "临床诊断", "患者电话", "大体描述:", "福尔马林固定标本，核对送检标本、病人姓名和条形码与申请单一致。", "灰红条索状组织3段，长0.5-1.8cm，直径均0.05cm。取1盒全（共1盒蜡块）", "镜下所见：", "诊断意见：", "肺组织穿刺活检：", "-结合免疫组化，符合浸润性黏液型腺癌，请结合临床。", "-免疫组化：CK7（+），CK20（+），Villin（+），TTF-1（散在+），NapsinA（散在+），P40（-），CDX2（-），Ki67（", "热点区约60%+）。", "报告医师：陈明坚", "本检测仅对送检负责，如果对结果有疑义，请在报告发布后7天内与我们联系，多谢合作！", "收样点：广西医科大学第一附属医院-呼吸内", "科", "主检实验室：广西金域", "地址：南宁市西乡塘区总部路3号中国-东盟科技企业孵化基地二期1号厂房一、三、", "四层", "报告专用章", "网址：www.kingmed.com.cn", "GX003SCEJL7RJLY", "报告日期：2026-03-10 21:16:16", "更多报告服务", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-07 04:54:44,841 INFO     29 [qwen-vl-text] coord API raw response (len=4666):
[
	{"text": "广西金域医学检验实验室", "bbox": [388, 26, 631, 43]},
	{"text": "本报告单经过电子签名认证", "bbox": [763, 28, 917, 39]},
	{"text": "Guangxi Kingmed Center for Clinical Laboratory", "bbox": [325, 45, 696, 58]},
	{"text": "金域医学", "bbox": [107, 58, 203, 76]},
	{"text": "KingMed Diagnostics", "bbox": [131, 77, 203, 84]},
	{"text": "病理诊断报告书", "bbox": [423, 64, 595, 82]},
	{"text": "1/1", "bbox": [892, 93, 915, 101]},
	{"text": "标本条码", "bbox": [82, 113, 143, 125], "bbox": [82, 113, 143, 125]},
	{"text": "1223023095", "bbox": [170, 114, 252, 124], "bbox": [170, 114, 252, 124]},
	{"text": "医院", "bbox": [346, 113, 385, 125], "bbox": [346, 113, 385, 125]},
	{"text": "广西医科大学第一附属医院", "bbox": [435, 114, 617, 124], "bbox": [435, 114, 617, 124]},
	{"text": "病人姓名", "bbox": [82, 128, 143, 140], "bbox": [82, 128, 143, 140]},
	{"text": "孔令祈", "bbox": [170, 129, 215, 140], "bbox": [170, 129, 215, 140]},
	{"text": "科室", "bbox": [346, 128, 385, 140], "bbox": [346, 128, 385, 140]},
	{"text": "老年呼吸", "bbox": [435, 129, 496, 140], "bbox": [435, 129, 496, 140]},
	{"text": "病理号", "bbox": [633, 128, 680, 140], "bbox": [633, 128, 680, 140]},
	{"text": "26018339", "bbox": [743, 130, 808, 140], "bbox": [743, 130, 808, 140]},
	{"text": "性别", "bbox": [82, 144, 120, 156], "bbox": [82, 144, 120, 156]},
	{"text": "男", "bbox": [170, 145, 185, 156], "bbox": [170, 145, 185, 156]},
	{"text": "房/床号", "bbox": [346, 144, 397, 156], "bbox": [346, 144, 397, 156]},
	{"text": "49", "bbox": [435, 145, 452, 156], "bbox": [435, 145, 452, 156]},
	{"text": "住院门诊号", "bbox": [633, 144, 715, 156], "bbox": [633, 144, 715, 156]},
	{"text": "1959880", "bbox": [743, 145, 800, 156], "bbox": [743, 145, 800, 156]},
	{"text": "年龄", "bbox": [82, 159, 120, 171], "bbox": [82, 159, 120, 171]},
	{"text": "67岁", "bbox": [170, 160, 200, 171], "bbox": [170, 160, 200, 171]},
	{"text": "接收时间", "bbox": [346, 159, 407, 171], "bbox": [346, 159, 407, 171]},
	{"text": "2026-03-08 14:15:50", "bbox": [435, 160, 590, 171], "bbox": [435, 160, 590, 171]},
	{"text": "申请医生", "bbox": [633, 159, 695, 171], "bbox": [633, 159, 695, 171]},
	{"text": "项目名称", "bbox": [82, 175, 143, 187], "bbox": [82, 175, 143, 187]},
	{"text": "免疫组化8项", "bbox": [170, 176, 254, 187], "bbox": [170, 176, 254, 187]},
	{"text": "送检材料", "bbox": [633, 175, 695, 187], "bbox": [633, 175, 695, 187]},
	{"text": "肺组织", "bbox": [743, 176, 790, 187], "bbox": [743, 176, 790, 187]},
	{"text": "临床诊断", "bbox": [82, 190, 143, 202], "bbox": [82, 190, 143, 202]},
	{"text": "患者电话", "bbox": [633, 190, 695, 202], "bbox": [633, 190, 695, 202]},
	{"text": "大体描述：", "bbox": [82, 209, 150, 221], "bbox": [82, 209, 150, 221]},
	{"text": "福尔马林固定标本，核对送检标本、病人姓名和条形码与申请单一致。", "bbox": [82, 225, 544, 237], "bbox": [82, 225, 544, 237]},
	{"text": "灰红条索状组织3段，长0.5-1.8cm，直径均0.05cm。取1盒全（共1盒蜡块）", "bbox": [82, 239, 586, 251], "bbox": [82, 239, 586, 251]},
	{"text": "镜下所见：", "bbox": [82, 272, 150, 284], "bbox": [82, 272, 150, 284]},
	{"text": "诊断意见：", "bbox": [82, 492, 150, 504], "bbox": [82, 492, 150, 504]},
	{"text": "肺组织穿刺活检：", "bbox": [82, 507, 194, 519], "bbox": [82, 507, 194, 519]},
	{"text": "-结合免疫组化，符合浸润性黏液型腺癌，请结合临床。", "bbox": [82, 521, 447, 533], "bbox": [82, 521, 447, 533]},
	{"text": "-免疫组化：CK7（+），CK20（+），Villin（+），TTF-1（散在+），NapsinA（散在+），P40（-），CDX2（-），Ki67（", "bbox": [82, 535, 912, 547], "bbox": [82, 535, 912, 547]},
	{"text": "热点区约60%+）。", "bbox": [82, 548, 200, 560], "bbox": [82, 548, 200, 560]},
	{"text": "报告医师：陈明坚", "bbox": [723, 809, 915, 823], "bbox": [723, 809, 915, 823]},
	{"text": "本检测仅对送检负责，如果对结果有疑义，请在报告发布后7天内与我们联系，多谢合作！", "bbox": [82, 834, 584, 846], "bbox": [82, 834, 584, 846]},
	{"text": "收样点：广西医科大学第一附属医院-呼吸内", "bbox": [640, 831, 917, 841], "bbox": [640, 831, 917, 841]},
	{"text": "科", "bbox": [700, 841, 715, 852], "bbox": [700, 841, 715, 852]},
	{"text": "主检实验室：广西金域", "bbox": [82, 854, 230, 866], "bbox": [82, 854, 230, 866]},
	{"text": "地址：南宁市西乡塘区总部路3号中国-东盟科技企业孵化基地二期1号厂房一、三、", "bbox": [82, 868, 551, 879], "bbox": [82, 868, 551, 879]},
	{"text": "四层", "bbox": [124, 880, 151, 890], "bbox": [124, 880, 151, 890]},
	{"text": "报告专用章", "bbox": [107, 882, 178, 900], "bbox": [107, 882, 178, 900]},
	{"text": "网址：www.kingmed.com.cn", "bbox": [348, 893, 517, 903], "bbox": [348, 893, 517, 903]},
	{"text": "GX003SCEJL7RJLY", "bbox": [656, 874, 760, 883], "bbox": [656, 874, 760, 883]},
	{"text": "报告日期：2026-03-10 21:16:16", "bbox": [609, 893, 811, 903], "bbox": [609, 893, 811, 903]},
	{"text": "更多报告服务", "bbox": [857, 897, 913, 905], "bbox": [857, 897, 913, 905]},
	{"text": "CS 扫描全能王", "bbox": [857, 955, 972, 970], "bbox": [857, 955, 972, 970]},
	{"text": "3亿人都在用的扫描App", "bbox": [857, 975, 972, 984], "bbox": [857, 975, 972, 984]}
]
2026-08-07 04:54:44,841 INFO     29 [qwen-vl-text] coord API: raw_items=57, valid_items=57, elapsed=25.1s
2026-08-07 04:54:44,841 INFO     29 [qwen-vl-text] coord item[0]: text=广西金域医学检验实验室, bbox=[388, 26, 631, 43]
2026-08-07 04:54:44,842 INFO     29 [qwen-vl-text] coord item[1]: text=本报告单经过电子签名认证, bbox=[763, 28, 917, 39]
2026-08-07 04:54:44,842 INFO     29 [qwen-vl-text] coord item[2]: text=Guangxi Kingmed Center for Clinical Laboratory, bbox=[325, 45, 696, 58]
2026-08-07 04:54:44,842 INFO     29 [qwen-vl-text] coord item[3]: text=金域医学, bbox=[107, 58, 203, 76]
2026-08-07 04:54:44,842 INFO     29 [qwen-vl-text] coord item[4]: text=KingMed Diagnostics, bbox=[131, 77, 203, 84]
2026-08-07 04:54:44,842 INFO     29 [qwen-vl-text] coord item[5]: text=病理诊断报告书, bbox=[423, 64, 595, 82]
2026-08-07 04:54:44,842 INFO     29 [qwen-vl-text] coord item[6]: text=1/1, bbox=[892, 93, 915, 101]
2026-08-07 04:54:44,842 INFO     29 [qwen-vl-text] coord item[7]: text=标本条码, bbox=[82, 113, 143, 125]
2026-08-07 04:54:44,842 INFO     29 [qwen-vl-text] coord item[8]: text=1223023095, bbox=[170, 114, 252, 124]
2026-08-07 04:54:44,842 INFO     29 [qwen-vl-text] coord item[9]: text=医院, bbox=[346, 113, 385, 125]
2026-08-07 04:54:44,842 INFO     29 [qwen-vl-text] coord item[10]: text=广西医科大学第一附属医院, bbox=[435, 114, 617, 124]
2026-08-07 04:54:44,842 INFO     29 [qwen-vl-text] coord item[11]: text=病人姓名, bbox=[82, 128, 143, 140]
2026-08-07 04:54:44,842 INFO     29 [qwen-vl-text] coord item[12]: text=孔令祈, bbox=[170, 129, 215, 140]
2026-08-07 04:54:44,842 INFO     29 [qwen-vl-text] coord item[13]: text=科室, bbox=[346, 128, 385, 140]
2026-08-07 04:54:44,842 INFO     29 [qwen-vl-text] coord item[14]: text=老年呼吸, bbox=[435, 129, 496, 140]
2026-08-07 04:54:44,842 INFO     29 [qwen-vl-text] coord item[15]: text=病理号, bbox=[633, 128, 680, 140]
2026-08-07 04:54:44,842 INFO     29 [qwen-vl-text] coord item[16]: text=26018339, bbox=[743, 130, 808, 140]
2026-08-07 04:54:44,842 INFO     29 [qwen-vl-text] coord item[17]: text=性别, bbox=[82, 144, 120, 156]
2026-08-07 04:54:44,843 INFO     29 [qwen-vl-text] coord item[18]: text=男, bbox=[170, 145, 185, 156]
2026-08-07 04:54:44,843 INFO     29 [qwen-vl-text] coord item[19]: text=房/床号, bbox=[346, 144, 397, 156]
2026-08-07 04:54:44,843 INFO     29 [qwen-vl-text] coord item[20]: text=49, bbox=[435, 145, 452, 156]
2026-08-07 04:54:44,843 INFO     29 [qwen-vl-text] coord item[21]: text=住院门诊号, bbox=[633, 144, 715, 156]
2026-08-07 04:54:44,843 INFO     29 [qwen-vl-text] coord item[22]: text=1959880, bbox=[743, 145, 800, 156]
2026-08-07 04:54:44,843 INFO     29 [qwen-vl-text] coord item[23]: text=年龄, bbox=[82, 159, 120, 171]
2026-08-07 04:54:44,843 INFO     29 [qwen-vl-text] coord item[24]: text=67岁, bbox=[170, 160, 200, 171]
2026-08-07 04:54:44,843 INFO     29 [qwen-vl-text] coord item[25]: text=接收时间, bbox=[346, 159, 407, 171]
2026-08-07 04:54:44,843 INFO     29 [qwen-vl-text] coord item[26]: text=2026-03-08 14:15:50, bbox=[435, 160, 590, 171]
2026-08-07 04:54:44,843 INFO     29 [qwen-vl-text] coord item[27]: text=申请医生, bbox=[633, 159, 695, 171]
2026-08-07 04:54:44,843 INFO     29 [qwen-vl-text] coord item[28]: text=项目名称, bbox=[82, 175, 143, 187]
2026-08-07 04:54:44,843 INFO     29 [qwen-vl-text] coord item[29]: text=免疫组化8项, bbox=[170, 176, 254, 187]
2026-08-07 04:54:44,843 INFO     29 [qwen-vl-text] coord item[30]: text=送检材料, bbox=[633, 175, 695, 187]
2026-08-07 04:54:44,844 INFO     29 [qwen-vl-text] coord item[31]: text=肺组织, bbox=[743, 176, 790, 187]
2026-08-07 04:54:44,844 INFO     29 [qwen-vl-text] coord item[32]: text=临床诊断, bbox=[82, 190, 143, 202]
2026-08-07 04:54:44,844 INFO     29 [qwen-vl-text] coord item[33]: text=患者电话, bbox=[633, 190, 695, 202]
2026-08-07 04:54:44,844 INFO     29 [qwen-vl-text] coord item[34]: text=大体描述：, bbox=[82, 209, 150, 221]
2026-08-07 04:54:44,844 INFO     29 [qwen-vl-text] coord item[35]: text=福尔马林固定标本，核对送检标本、病人姓名和条形码与申请单一致。, bbox=[82, 225, 544, 237]
2026-08-07 04:54:44,844 INFO     29 [qwen-vl-text] coord item[36]: text=灰红条索状组织3段，长0.5-1.8cm，直径均0.05cm。取1盒全（共1盒蜡块）, bbox=[82, 239, 586, 251]
2026-08-07 04:54:44,844 INFO     29 [qwen-vl-text] coord item[37]: text=镜下所见：, bbox=[82, 272, 150, 284]
2026-08-07 04:54:44,844 INFO     29 [qwen-vl-text] coord item[38]: text=诊断意见：, bbox=[82, 492, 150, 504]
2026-08-07 04:54:44,844 INFO     29 [qwen-vl-text] coord item[39]: text=肺组织穿刺活检：, bbox=[82, 507, 194, 519]
2026-08-07 04:54:44,844 INFO     29 [qwen-vl-text] coord item[40]: text=-结合免疫组化，符合浸润性黏液型腺癌，请结合临床。, bbox=[82, 521, 447, 533]
2026-08-07 04:54:44,844 INFO     29 [qwen-vl-text] coord item[41]: text=-免疫组化：CK7（+），CK20（+），Villin（+），TTF-1（散在+），NapsinA（散在+），P40（-），CDX2（-），Ki67（, bbox=[82, 535, 912, 547]
2026-08-07 04:54:44,844 INFO     29 [qwen-vl-text] coord item[42]: text=热点区约60%+）。, bbox=[82, 548, 200, 560]
2026-08-07 04:54:44,844 INFO     29 [qwen-vl-text] coord item[43]: text=报告医师：陈明坚, bbox=[723, 809, 915, 823]
2026-08-07 04:54:44,844 INFO     29 [qwen-vl-text] coord item[44]: text=本检测仅对送检负责，如果对结果有疑义，请在报告发布后7天内与我们联系，多谢合作！, bbox=[82, 834, 584, 846]
2026-08-07 04:54:44,844 INFO     29 [qwen-vl-text] coord item[45]: text=收样点：广西医科大学第一附属医院-呼吸内, bbox=[640, 831, 917, 841]
2026-08-07 04:54:44,844 INFO     29 [qwen-vl-text] coord item[46]: text=科, bbox=[700, 841, 715, 852]
2026-08-07 04:54:44,845 INFO     29 [qwen-vl-text] coord item[47]: text=主检实验室：广西金域, bbox=[82, 854, 230, 866]
2026-08-07 04:54:44,845 INFO     29 [qwen-vl-text] coord item[48]: text=地址：南宁市西乡塘区总部路3号中国-东盟科技企业孵化基地二期1号厂房一、三、, bbox=[82, 868, 551, 879]
2026-08-07 04:54:44,845 INFO     29 [qwen-vl-text] coord item[49]: text=四层, bbox=[124, 880, 151, 890]
2026-08-07 04:54:44,845 INFO     29 [qwen-vl-text] coord item[50]: text=报告专用章, bbox=[107, 882, 178, 900]
2026-08-07 04:54:44,845 INFO     29 [qwen-vl-text] coord item[51]: text=网址：www.kingmed.com.cn, bbox=[348, 893, 517, 903]
2026-08-07 04:54:44,845 INFO     29 [qwen-vl-text] coord item[52]: text=GX003SCEJL7RJLY, bbox=[656, 874, 760, 883]
2026-08-07 04:54:44,845 INFO     29 [qwen-vl-text] coord item[53]: text=报告日期：2026-03-10 21:16:16, bbox=[609, 893, 811, 903]
2026-08-07 04:54:44,845 INFO     29 [qwen-vl-text] coord item[54]: text=更多报告服务, bbox=[857, 897, 913, 905]
2026-08-07 04:54:44,845 INFO     29 [qwen-vl-text] coord item[55]: text=CS 扫描全能王, bbox=[857, 955, 972, 970]
2026-08-07 04:54:44,845 INFO     29 [qwen-vl-text] coord item[56]: text=3亿人都在用的扫描App, bbox=[857, 975, 972, 984]
2026-08-07 04:54:44,845 INFO     29 [qwen-vl-text] page=25 — 57/57 coords, api_time=25.1s
2026-08-07 04:54:44,846 INFO     29 [qwen-vl-text] new_positions (57):
[[25, 230.85999999999999, 375.445, 21.892, 36.205999999999996], [25, 453.98499999999996, 545.615, 23.576, 32.838], [25, 193.375, 414.12, 37.89, 48.836], [25, 63.665, 120.785, 48.836, 63.992], [25, 77.945, 120.785, 64.834, 70.728], [25, 251.685, 354.025, 53.888, 69.044], [25, 530.74, 544.425, 78.306, 85.042], [25, 48.79, 85.085, 95.146, 105.25], [25, 101.14999999999999, 149.94, 95.988, 104.408], [25, 205.87, 229.075, 95.146, 105.25], [25, 258.825, 367.115, 95.988, 104.408], [25, 48.79, 85.085, 107.776, 117.88], [25, 101.14999999999999, 127.925, 108.618, 117.88], [25, 205.87, 229.075, 107.776, 117.88], [25, 258.825, 295.12, 108.618, 117.88], [25, 376.635, 404.59999999999997, 107.776, 117.88], [25, 442.085, 480.76, 109.46, 117.88], [25, 48.79, 71.39999999999999, 121.24799999999999, 131.352], [25, 101.14999999999999, 110.07499999999999, 122.08999999999999, 131.352], [25, 205.87, 236.215, 121.24799999999999, 131.352], [25, 258.825, 268.94, 122.08999999999999, 131.352], [25, 376.635, 425.42499999999995, 121.24799999999999, 131.352], [25, 442.085, 476.0, 122.08999999999999, 131.352], [25, 48.79, 71.39999999999999, 133.878, 143.982], [25, 101.14999999999999, 119.0, 134.72, 143.982], [25, 205.87, 242.165, 133.878, 143.982], [25, 258.825, 351.05, 134.72, 143.982], [25, 376.635, 413.525, 133.878, 143.982], [25, 48.79, 85.085, 147.35, 157.454], [25, 101.14999999999999, 151.13, 148.192, 157.454], [25, 376.635, 413.525, 147.35, 157.454], [25, 442.085, 470.04999999999995, 148.192, 157.454], [25, 48.79, 85.085, 159.98, 170.084], [25, 376.635, 413.525, 159.98, 170.084], [25, 48.79, 89.25, 175.97799999999998, 186.082], [25, 48.79, 323.68, 189.45, 199.554], [25, 48.79, 348.66999999999996, 201.238, 211.34199999999998], [25, 48.79, 89.25, 229.024, 239.128], [25, 48.79, 89.25, 414.264, 424.368], [25, 48.79, 115.42999999999999, 426.894, 436.998], [25, 48.79, 265.965, 438.68199999999996, 448.786], [25, 48.79, 542.64, 450.46999999999997, 460.574], [25, 48.79, 119.0, 461.416, 471.52], [25, 430.185, 544.425, 681.178, 692.966], [25, 48.79, 347.47999999999996, 702.228, 712.332], [25, 380.79999999999995, 545.615, 699.702, 708.122], [25, 416.5, 425.42499999999995, 708.122, 717.384], [25, 48.79, 136.85, 719.068, 729.172], [25, 48.79, 327.84499999999997, 730.856, 740.1179999999999], [25, 73.78, 89.845, 740.9599999999999, 749.38], [25, 63.665, 105.91, 742.644, 757.8], [25, 207.06, 307.615, 751.906, 760.326], [25, 390.32, 452.2, 735.908, 743.486], [25, 362.35499999999996, 482.54499999999996, 751.906, 760.326], [25, 509.91499999999996, 543.235, 755.274, 762.01], [25, 509.91499999999996, 578.3399999999999, 804.11, 816.74], [25, 509.91499999999996, 578.3399999999999, 820.9499999999999, 828.528]]
2026-08-07 04:54:44,846 INFO     29 [qwen-vl-text] ═══ DONE ═══ 57 positions, pages=1, time=29.2s
2026-08-07 04:54:44,864 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-07 04:54:44,864 INFO     29 [Trace] task=26a40982 | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Extractor:ExaminationReport | outputs={"chunks": "6 items, types={'ExaminationReport': 6}", "html": "", "json": "1557 items", "markdown": "", "text": "", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 11}"}
2026-08-07 04:54:44,864 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-07 04:54:44,870 INFO     29 [ChunkMerger] Merged 18 chunks from 8 sources: {'Extractor:LabExam': 11, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 6} (filtered 5 noise chunks)
2026-08-07 04:54:45,473 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-07 04:54:45,474 INFO     29 [Trace] task=26a40982 | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "18 items, types={'LabReport': 11, 'AdmissionRecord': 1, 'ExaminationReport': 6}", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf"}
2026-08-07 04:54:45,474 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-07 04:54:45,803 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786077646742, 'update_date': datetime.datetime(2026, 8, 7, 4, 40, 46), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 668582, 'status': '1'}
2026-08-07 04:54:46,076 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   结核杆菌DNA*  TB-DNA  <5.00E+02  拷贝  <5.00E+02  False   
---
   乙型肝炎表面抗原*  None  0.00  IU/ml  0-0.08  False    乙型肝炎表面抗体*  None  14.85  mIU/mL  0-10  True    乙型肝炎e抗原*  None  0.00  PElu/ml  0-0.10  False    乙型肝炎e抗体*  None  0.14  IU/mL  0-0.20  False    乙型肝炎核心抗体*  None  0.27  IU/mL  0-0.50  False   
---
   丙型肝炎抗体定量*  None  0.06  COI  0-1  False    不加热血清反应素试验*  ST  阴性(-)  None  阴性(-)  False    人免疫缺陷病毒抗体定量*  V  0.08  COI  0-1  False    梅毒螺旋体抗体定量*  PA  0.08  COI  0-1  False   
---
   糖化血红蛋白HbA1c*  HbA1c  6.40  %  4.0-6.0  True    糖化血红蛋白HbA1a  HbA1a  0.50  %  0-0.91  False    糖化血红蛋白HbA1b  HbA1b  1.10  %  0.35-1.82  False   
---
   凝血酶原时间  None  11.50  S  9-15  False    国际标准化比值  None  1.04  None  0.8-1.4  False    纤维蛋白原  None  4.43  g/L  2.00-5.00  False    活化部分凝血活酶时间  None  32.30  S  23.00-40.00  False    凝血酶时间  None  13.00  S  10.3-16.6  False    凝血酶原活动度  None  98  %  70-130  False    D-二聚体定量  None  69  ng/ml  0-450  False   
---
   总胆红素*  TBIL  8.7  µmol/L  0-26.0  False    直接胆红素*  DBIL  3.6  µmol/L  0-6.8  False    间接胆红素  IBIL  5.1  µmol/L  3.1-14.3  False    直/总胆比值  DB/TB  0.41  None  None  False    总蛋白#  TP  74.5  g/L  65-85  False    白蛋白*  ALB  39.3  g/L  40-55  True    球蛋白  GLO  35.2  g/L  20-40  False    白蛋白/球蛋白  A/G  1.1  None  1.2-2.4  True    谷氨酰转肽酶*  GGT  30  U/L  10-60  False    总胆汁酸*  TBA  13.2  µmol/L  0-10  True    天门冬氨酸氨基转移酶*  AST  15  U/L  15-40  False    丙氨酸氨基转移酶*  ALT  14  U/L  9-50  False    谷草/谷丙比值  AST/ALT  1.1  None  None  False    碱性磷酸酶*  ALP  64  U/L  45-125  False    前白蛋白*  PA  251.5  mg/L  200-430  False    胆碱酯酶*  CHE  8382  U/L  5000-12000  False    尿素*  UREA  6.98  mmol/L  3.6-9.5  False    肌酐*  CREA  136  µmol/L  57-111  True    尿酸*  UA  551  µmol/L  208-428  True    碳酸氢根*  HCO3  21.6  mmol/L  22-29  True    总胆固醇*  T-CHO  3.10  mmol/L  3.1-5.7  False   
---
   胆碱酯酶*  CHE  8382  U/L  5000-12000  False    尿素*  UREA  6.98  mmol/L  3.6-9.5  False    肌酐*  CREA  136  μmol/L  57-111  True    尿酸*  UA  551  μmol/L  208-428  True    碳酸氢根*  HCO3  21.6  mmol/L  22-29  True    总胆固醇*  T-CHO  3.18  mmol/L  <5.2  False    甘油三酯*  TG  1.27  mmol/L  <1.7  False    低密度脂蛋白胆固醇*  LDL-C  1.78  mmol/L  <3.4(低危人群)  False    空腹血葡萄糖*  GLU  4.79  mmol/L  3.9-6.1  False    钾*  K  4.18  mmol/L  3.5-5.3  False    钠*  Na  141.1  mmol/L  137-147  False    氯*  CL  106.4  mmol/L  99-110  False    总钙*  Ca  2.25  mmol/L  2.11-2.52  False    镁*  Mg  0.78  mmol/L  0.75-1.02  False    磷*  P  0.95  mmol/L  0.85-1.51  False    肌酸激酶*  CK  84  U/L  50-310  False    肌酸激酶同工酶MB  CK-MB  13  U/L  0-25  False    乳酸脱氢酶*  LD  167  U/L  120-250  False    α-羟丁酸脱氢酶*  α-HBD  109  U/L  72-182  False    免疫球蛋白E*  IgE  1960.6  IU/ml  <100  True   
---
   白细胞计数*  WBC  8.490  10~9/L  3.5-9.5  False    红细胞计数*  RBC  5.81  10~12/L  4.3-5.8  True    血红蛋白*  HGB  157.00  g/L  130-175  False    血小板计数*  PLT  268.00  10~9/L  125-350  False    中性粒细胞百分比  NEU%  0.6920  None  0.4-0.75  False    淋巴细胞百分比  LYM%  0.1970  None  0.2-0.5  True    单核细胞百分比  MONO%  0.0630  None  0.03-0.1  False    嗜酸性粒细胞百分比  EO%  0.0450  None  0.004-0.08  False    嗜碱性粒细胞百分比  BA SO%  0.0030  None  0-0.01  False    中性粒细胞绝对值  NEU  5.88  10~9/L  1.8-6.3  False    淋巴细胞绝对值  LYM  1.67  10~9/L  1.1-3.2  False    单核细胞绝对值  MONO  0.53  10~9/L  0.1-0.6  False    嗜酸性粒细胞绝对值  EOS  0.38  10~9/L  0.02-0.52  False    嗜碱性粒细胞绝对值  BA SO  0.03  10~9/L  0-0.06  False    平均红细胞体积*  MCV  83.70  fl  82-100  False    平均RBC血红蛋白含量*  MCH  26.90  pg  27-34  True    平均RBC血红蛋白浓度*  MCHC  323.00  g/L  316-354  False    红细胞比容*  HCT  0.486  None  0.4-0.5  False    RBC体积分布宽度CV  RDWCV  0.15  None  0.11-0.14  True    血小板体积分布宽度  PDW  0.16  None  0.15-0.18  False   
---
   吸氧浓度  FI02  21.00  %  21-100  False    体温  T  36.4  None  29-41  False    钙测定  Ca++  1.19  mmol/L  1.15-1.29  False    钠测定  Na+  143.20  mmol/L  136-146  False    钾测定  K+  3.98  mmol/L  3.5-4.5  False    氧合指数(p/f)  p02(a,T)/F02  315.0  None  400-500  True    红细胞外剩余碱  BEecf  -1.80  mmol/l  -3-3  False    酸碱度 (PH)  PH  7.383  None  7.35-7.45  False    pH校正值(pHT)  pH(T)  7.392  None  7.35-7.45  False    氧分压 (pO2)  pO2  66.20  mmHg  83-108  True    氧分压校正值  pO2(T)  63.50  mmHg  83-108  True    二氧化碳分压  pCO2  39.90  mmHg  35-45  False    CO2分压校正  PCO2(T)  38.90  mmHg  35-45  False    氯测定  Cl-  102.00  mmol/L  98-106  False    血红蛋白测定(Hb)  Hb  162.00  g/L  120-160  True    氧合血红蛋白  F02Hb  92.0  %  94-98  True    高铁血红蛋白  MetHb  0.10  None  None  False    总血氧饱和度  s02  92.9  %  93-98  True    CO红蛋白  COHb  1.00  %  0-2  False    血CO2含量  ctCO2  24.50  mmol/L  24-32  False    还原血红蛋白  FHHB  6.9  None  None  False   
---
   酸碱度 (PH)  PH  7.383  None  7.35-7.45  False    pH校正值(pHT)  pH(T)  7.392  None  7.35-7.45  False    氧分压 (pO2)  pO2  66.20  mmHg  83-108  True    氧分压校正值  pO2(T)  63.50  mmHg  83-108  True    二氧化碳分压  pCO2  39.90  mmHg  35-45  False    CO2分压校正  PCO2(T)  38.90  mmHg  35-45  False    氯测定  Cl-  102.00  mmol/L  98-106  False    血红蛋白测定(Hb)  Hb  162.00  g/L  120-160  True    氧合血红蛋白  F02Hb  92.0  %  94-98  True    高铁血红蛋白  MetHb  0.10  None  None  False    总血氧饱和度  s02  92.9  %  93-98  True    CO红蛋白  C0Hb  1.00  %  0-2  False    血CO2含量  ctCO2  24.50  mmol/L  24-32  False    还原血红蛋白  FHHB  6.9  %  2-7  False    标准碳酸氢根  cHCO3  23.00  mmol/L  22-26  False    实际剩余碱  ABE (BE(B))  -1.6  mmol/L  -3-3  False    实际碳酸氢根  HCO3-  23.20  mmol/L  None  False    肺泡动脉氧分压差  P02(A-a,T)e  36.0  mmHg  10-25  True    动脉与肺泡氧分压比  P02(a/A,T)  64.0  %  85-95  True    呼吸指数  RI  57.0  None  None  False    葡萄糖测定  Glu  6.70  None  None  False   
---
   KRAS  None  p.G12V  None  None  True    CDKN2A  None  p.R80*  None  None  True    TP53  None  p.G279E  None  None  True    PD-L1 TPS  TPS  <1%  None  None  False    PD-L1 CPS  CPS  1  None  None  False   
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
CS 扫描全能王
3亿人都在用的扫描App
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
色泽: 正常
皮疹: 全身皮肤未见皮疹
皮下出血: 全身皮肤未见皮下出血
毛发分布: 毛发分布正常
温度与湿度: 温度、湿度、弹性均正常
水肿: 未见水肿
肝掌: 无
蜘蛛痣: 未见蜘蛛痣
其他表现: 无
淋巴结: 全身浅表淋巴结未扪及肿大
头部:
头颅: 头颅大小正常, 无畸形
眼: 眉毛, 眼睑, 结膜, 眼球未见异常, 双侧巩膜无黄染
耳: 双耳外观未见异常, 乳突无压痛, 外耳道未见分泌物
鼻: 鼻部外观未见异常, 鼻翼无扇动, 鼻腔无分泌物, 鼻窦区无压痛
咽喉: 双侧扁桃体未见肿大, 表面未见脓性分泌物, 咽未见异常, 声音正常
口腔: 唇, 舌, 牙齿, 牙龈正常
颈部:
颈部运动: 颈软无抵抗
颈静脉: 无怒张
气管: 居中
颈动脉搏动: 正常
肝-颈静脉回流征: 阴性
广西医科大:
预览 验证CA签名 手工解锁 删除 病历参考 更新数据 加载全部病程 个人模板管理 返回
20 部：
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
003470 20.2.
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
关 节：各关节未见异常，活动无受限
肌 肉：未见肌肉萎缩，肌张力正常。四肢肌力5级。
神经系统：
浅反射：双侧浅反射正常引出
深反射：双侧深反射正常引出
病理反射：未引出
脑膜刺激征：阴性
专科情况
神清，两肺叩诊清音，两肺呼吸音清，可闻及细湿啰音，未闻及干啰音及胸膜摩擦音，双下肢无凹陷性水肿。
实验室及器械检查结果
(2026-02-26 中山大学附属第一医院广西医院）胸部CT：1.右肺下叶后基底段软组织肿块，最大截断面约77mm*60mm
，肿瘤可能；2.双肺多发实性结节，转移瘤？3.双肺上叶间隔旁型肺气肿。4.双侧胸膜肥厚、钙化。浅表淋巴结彩超
：双侧颈部、锁骨上窝、腋窝、腹股沟区未见明显肿大淋巴结。
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
医师签名：姜晓红 住院医师：孙超群
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
检查技师:刘辰民 报告医师:谢金桓 审核医师: 冯涛
报告日期:2026-03-11 14:21:30 审核日期:2026-03-11 16:15:45
地址:广西医科大学第一附属医院放射科 联系电话:0771-5356934 “广西HR”解释:广西影像检查项目互认
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
2026-08-07 04:54:47,449 INFO     29 [EMBED-PIPELINE] batch[16:32] text_for_embed=测量参数值:
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
(0.8-2.0)
e'/a'
<1
(->)
E/e'
11.7
(->)
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
广西金域医学检验实验室
本报告单经过电子签名认证
Guangxi Kingmed Center for Clinical Laboratory
金域医学
KingMed Diagnostics
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
2026-08-07 04:54:47,817 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-07 04:54:47,818 INFO     29 [Trace] task=26a40982 | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "18 items, types={'LabReport': 11, 'AdmissionRecord': 1, 'ExaminationReport': 6}", "name": "广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf", "embedding_token_consumption": 17870}
2026-08-07 04:54:47,818 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-07 04:54:48,336 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-07 04:54:48,336 INFO     29 [Trace] task=26a40982 | doc=广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":18,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-07 04:54:48,349 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(15, 191, 250, 153, 163) row[-1]=(15, 191, 250, 153, 163)
2026-08-07 04:54:48,349 INFO     29 [DIAG-EXECUTOR] row_position_int len=5 row[0]=(16, 104, 174, 148, 158) row[-1]=(16, 106, 175, 227, 237)
2026-08-07 04:54:48,349 INFO     29 [DIAG-EXECUTOR] row_position_int len=4 row[0]=(17, 138, 207, 151, 160) row[-1]=(17, 135, 212, 211, 220)
2026-08-07 04:54:48,349 INFO     29 [DIAG-EXECUTOR] row_position_int len=3 row[0]=(18, 123, 206, 156, 166) row[-1]=(18, 123, 204, 196, 205)
2026-08-07 04:54:48,349 INFO     29 [DIAG-EXECUTOR] row_position_int len=7 row[0]=(19, 148, 202, 155, 164) row[-1]=(19, 149, 206, 276, 285)
2026-08-07 04:54:48,349 INFO     29 [DIAG-EXECUTOR] row_position_int len=21 row[0]=(20, 197, 234, 145, 153) row[-1]=(20, 197, 237, 535, 543)
2026-08-07 04:54:48,349 INFO     29 [DIAG-EXECUTOR] row_position_int len=20 row[0]=(21, 197, 234, 139, 148) row[-1]=(21, 194, 242, 518, 527)
2026-08-07 04:54:48,349 INFO     29 [DIAG-EXECUTOR] row_position_int len=20 row[0]=(22, 207, 252, 148, 158) row[-1]=(22, 196, 268, 519, 528)
2026-08-07 04:54:48,349 INFO     29 [DIAG-EXECUTOR] row_position_int len=21 row[0]=(23, 221, 255, 146, 155) row[-1]=(23, 215, 264, 529, 538)
2026-08-07 04:54:48,349 INFO     29 [DIAG-EXECUTOR] row_position_int len=21 row[0]=(24, 208, 257, 146, 155) row[-1]=(24, 216, 258, 526, 536)
2026-08-07 04:54:48,349 INFO     29 [DIAG-EXECUTOR] row_position_int len=5 row[0]=(25, 287, 484, 162, 171) row[-1]=(25, 419, 446, 188, 197)
2026-08-07 04:54:48,350 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-07 04:54:48,350 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-07 04:54:48,350 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-07 04:54:48,350 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-07 04:54:48,350 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-07 04:54:48,351 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-07 04:54:48,351 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-07 04:54:48,360 INFO     29 set_progress(26a40982921a11f18b9f1b2113099832), progress: 0.82, progress_msg: 04:54:48 [DOC Engine]:
Start to index...
2026-08-07 04:54:48,418 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.052s]
2026-08-07 04:54:48,424 INFO     29 set_progress(26a40982921a11f18b9f1b2113099832), progress: 0.8055555555555556, progress_msg: 
2026-08-07 04:54:48,465 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.029s]
2026-08-07 04:54:48,508 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.026s]
2026-08-07 04:54:48,526 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.008s]
2026-08-07 04:54:48,539 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.007s]
2026-08-07 04:54:48,546 INFO     29 set_progress(26a40982921a11f18b9f1b2113099832), progress: 1.0, progress_msg: 04:54:48 Indexing done (0.19s). Task done (848.55s)
2026-08-07 04:54:48,550 INFO     29 [Done], chunks(18), token(17870), elapsed:848.55
2026-08-07 04:54:48,904 INFO     29 handle_task done for task {"id": "26a40982921a11f18b9f1b2113099832", "doc_id": "f701d642918211f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u5e7f\u897f-KLYY-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 27799240, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786077644033, "task_type": "dataflow", "root_trace_id": "f513e95aa5674767affd022391246ccb", "root_traceparent": "00-f513e95aa5674767affd022391246ccb-03354b7dbcc1445e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
