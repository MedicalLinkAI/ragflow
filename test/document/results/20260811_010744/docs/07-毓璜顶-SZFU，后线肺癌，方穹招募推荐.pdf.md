# 基准结果：07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf

## 基本信息

- 文件：`07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf`
- 大小：5688.5 KB
- PDF 总页数：13
- doc_id：`d60771c094e511f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-11T02:03:47  完成时间：2026-08-11T02:09:36  耗时：349.1s
- progress_msg：`18:09:33 Indexing done (0.05s). Task done (323.01s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | eb199ef1 | 1 | 1-1 | 姓名 性别：男 年龄：57 门诊号： 科别： 病区 床号 住院号： 取材部位：左 |
| 2 | 0dd56dd0 | 1 | 2-2 | 性别：男 年龄：57 门诊号： 科别： 床号 送检医生 住院号 病区 送检日期： |
| 3 | 69f8a61d | 2 | 3-4 | 病理会诊报告单 病理号: 姓名 性别: 男 年龄: 54岁 送检单位 送检日期: |
| 4 | fbb41cbf | 3 | 4-6 | 2026-03-04 15:46 入院记录 性别：男 职业：其他 年龄：57岁  |
| 5 | 7f9df696 | 1 | 7-7 | 检查项目： 胸部磁共振平扫+DWI+动态增强成像 影像登录号： MR100603 |
| 6 | 136ca214 | 1 | 8-8 | 检查项目：十二通道 检查名称：十二通道 检查部位： □检查所见： □检查结论：  |
| 7 | bf5f6a6c | 1 | 10-10 | <table><tr><td>凝血酶原时间活动度</td><td>60110</ |
| 8 | 6ee19d89 | 1 | 11-11 | <table><tr><td>游离甲状腺素</td><td>None</td>< |
| 9 | 47fbfbc0 | 1 | 9-9 | <table><tr><td>天门冬氨酸氨基转移酶</td><td>None</ |
| 10 | 25ce2cbc | 1 | 12-12 | <table><tr><td>中性粒细胞计数</td><td>None</td> |

- chunks 总数：10
- 各 chunk 页数合计（含跨页重复）：13
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]`
- 覆盖页数：12 / 13；缺失页：`[13]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：❌ 未完全覆盖：覆盖 12/13 页，缺失 [13]，超范围 []**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 0 | 0 | 0 | encounter_date, chief_complaint, diagnosis | **-** |
| AdmissionRecord | 入院 | 1 | 1 | 1 | encounter_date, dm_admission_time, cc_text, department | **OK** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 5 | 5 | 5 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 4 | 0 | 4 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"ExaminationReport": 5, "AdmissionRecord": 1, "LabReport": 4}`
- ChunkMerger：`{"found": true, "merged": 10, "sources": 9, "stats": {"Extractor:LabExam": 4, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 5, "Extractor:Progress": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 18:09:31,733 INFO     29 [ChunkMerger] Merged 10 chunks from 9 sources: {'Extractor:LabExam': 4, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 18:03:48,951 INFO     29 handle_task begin for task {"id": "d64c79b494e511f1bd9827cf206dfa2d", "doc_id": "d60771c094e511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 5825068, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385028897, "task_type": "dataflow", "root_trace_id": "93629fbf7f764cf397a9e7f896dd05c6", "root_traceparent": "00-93629fbf7f764cf397a9e7f896dd05c6-e7dded3dfece48a2-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 18:03:49,169 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 18:03:49,289 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 18:03:49,300 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:03:49,300 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 18:03:49,300 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 18:03:49,315 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 18:03:49,315 INFO     29 ============================================================
2026-08-10 18:03:49,315 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 18:03:49,315 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 18:03:49,315 INFO     29 ============================================================
2026-08-10 18:03:49,315 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 18:03:49,315 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 18:03:49,317 INFO     29 No torch found.
2026-08-10 18:03:50,637 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=13
2026-08-10 18:03:50,719 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=488933, prompt_len=764
2026-08-10 18:03:52,005 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:03:52,006 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 18:03:52,014 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=488933, prompt_len=401
2026-08-10 18:03:53,646 INFO     29 [qwen-vl-parser] text API response (len=277):
["姓名", "性别：男", "年龄：57", "门诊号：", "科别：", "病区", "床号", "住院号：", "取材部位：左肺", "补充内容：", "快速石蜡病理诊断：", "（左肺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，免疫组化", "及特殊染色待补充报告。", "免疫组化结果：CK5/6（-）、TTF-1（-）、NapsinA（-）、P40（部分+）、Villin（-）、CK7", "（+）、CDX2（-）", "ALK伴随诊断：", "ALK（D5F3）：阴性；（兔单克隆阴性对照：阴性；阳性对照：阳性）"]
2026-08-10 18:03:53,647 INFO     29 [qwen-vl-parser] page=1 text: 17 lines (bbox 0-16)
2026-08-10 18:03:53,647 INFO     29 [qwen-vl-parser] page=1 text: 17 sections
2026-08-10 18:03:53,719 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=343188, prompt_len=764
2026-08-10 18:03:54,946 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-03-06"}
```
2026-08-10 18:03:54,947 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=2026-03-06
2026-08-10 18:03:54,957 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=343188, prompt_len=401
2026-08-10 18:03:56,084 INFO     29 [qwen-vl-parser] text API response (len=173):
["性别：男", "年龄：57", "门诊号：", "科别：", "床号", "送检医生", "住院号", "病区", "送检日期：2026-3-6 15:05:29", "取材信息：", "灰白灰红条状碎组织一堆，共计直径0.8cm。", "病理诊断：", "快速石蜡病理诊断：", "（左肺活检）分化差的癌，待免疫组化结果进一步明确分型。"]
2026-08-10 18:03:56,084 INFO     29 [qwen-vl-parser] page=2 text: 14 lines (bbox 17-30)
2026-08-10 18:03:56,084 INFO     29 [qwen-vl-parser] page=2 text: 14 sections
2026-08-10 18:03:56,203 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1002288, prompt_len=764
2026-08-10 18:03:57,490 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2023-04-04"}
```
2026-08-10 18:03:57,490 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=2023-04-04
2026-08-10 18:03:57,502 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1002288, prompt_len=401
2026-08-10 18:04:00,361 INFO     29 [qwen-vl-parser] text API response (len=521):
["病理会诊报告单", "病理号:", "姓名", "性别: 男", "年龄: 54岁", "送检单位", "送检日期: 2023/4/4", "送检医生:", "镜下所见:", "原病理诊断:", "读“青岛市中心医疗集团”报告, 病理号: 2307637, HE×1, IHC*5, 原诊断: (左锁骨上淋", "巴结穿刺活检) 纤维组织内查见分化差的癌, 结合免疫组化及病史, 不除外肺非小细胞癌转", "移。", "免疫组化结果: TTF-1 (-), NapsinA (-), CK7 (+), CK 5/6 (-), P40 (灶+)。", "病理会诊诊断:", "(左锁骨上淋巴结穿刺活检) 纤维组织内查见片状、实体状异型上皮样细胞浸润, 结合临床及", "免疫标记, 考虑低分化癌, 可能为肺非小细胞癌转移, 倾向腺癌, 建议粘液染色进一步协助诊", "断。", "原单位免疫组化结果: TTF-1 (-), NapsinA (-), CK7 (+), CK 5/6 (-), P40 (个别细胞", "+)。", "报告时间:2023-4-4", "诊断医师:姜慧峰", "注: 病理医师个人会诊咨询意见, 仅供原病理学"]
2026-08-10 18:04:00,361 INFO     29 [qwen-vl-parser] page=3 text: 23 lines (bbox 31-53)
2026-08-10 18:04:00,361 INFO     29 [qwen-vl-parser] page=3 text: 23 sections
2026-08-10 18:04:00,586 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1943887, prompt_len=764
2026-08-10 18:04:01,998 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:04:01,999 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 18:04:02,011 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1943887, prompt_len=401
2026-08-10 18:04:04,539 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:04:04.536+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 84, "failed": 0, "current": {"d64c79b494e511f1bd9827cf206dfa2d": {"id": "d64c79b494e511f1bd9827cf206dfa2d", "doc_id": "d60771c094e511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 5825068, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385028897, "task_type": "dataflow", "root_trace_id": "93629fbf7f764cf397a9e7f896dd05c6", "root_traceparent": "00-93629fbf7f764cf397a9e7f896dd05c6-e7dded3dfece48a2-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:04:16,951 INFO     29 [qwen-vl-parser] text API response (len=2215):
["开始 | 病历列表", "35_孙正福_住院", "< > X", "页", "控", "消", "息", "2026-03-04 15:46 入院记录", "性别：男", "职业：其他", "年龄：57岁", "入院时间：2026-03-04 15:38:00", "民族：汉族", "记录时间：2026-03-04 15:46", "婚姻：已婚", "病史陈述者：患者本人及家属", "主诉：确诊左肺癌2年余，双下肢疼痛1周。", "现病史：患者2年余前查体发现左颈部肿物，约豆粒大小，无疼痛，偶有咳嗽、咳痰，无痰中带血丝，活动后偶感胸闷、憋气，无咯血，无胸痛，无发热。后肿物逐渐增大，遂就诊于我院，2023-03-30行", "PET/CT：1，左肺上叶高代谢占位，考虑肺癌（并累及邻近胸膜），（左侧颈部V区、左锁骨上、纵隔、左肺门10区、左肺内11-12区）多发淋巴结转移；建议病理学检查；左肺门10区淋巴结旁肺组织见网格样密度", "增高影，轻度PDG代谢增高，建议结合临床并复查。未行特殊治疗。后就诊于我科，2023-04-03行快速石蜡病理诊断：（左锁骨上淋巴结穿刺活检）纤维组织内查见分化差的癌，结合免疫组化及病史，不除外肺非", "小细胞癌转移。经齐鲁医院会诊：倾向肺腺癌。免疫组化结果：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（-）、P40（灶+）。2023-04-06行胸部增强CT：左肺上叶恶性肿瘤并累及邻近胸膜，左锁骨上、左", "肺门及纵隔多发淋巴结转移。快速石蜡病理诊断：（左肺上叶穿刺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，特殊染色待补充报告。免疫组化结果：CK5/6（-）、P40（部分+）、", "TTF-1（-）、NapsinA（-）、CK7（+）。ALK（D5F3）：阴性；（兔单克隆阴性对照：阴性；阳性对照：阳性）。2023-04-07至2023-06-30行替雷利珠单抗200mg免疫治疗+贝伐珠单抗注射液900.00mg靶向治", "疗，联合卡铂500.00mg d1+培美曲塞二钠850.00mg d1化疗5周期。排除禁忌，患者于2023-07-06行胸部IMRT放疗，具体：IMRT,PTV 60GY/30F，末次放疗时间为2023-08-09。2023-07-19行卡铂500mg化疗联合恩度", "靶向及替雷利珠单抗免疫治疗。2023-08-10予以患者恩度靶向及替雷利珠单抗免疫治疗。2024-09-30行顺铂40mgd1化疗，联合贝伐珠单抗注射液靶向、替雷利珠单抗免疫治疗。2024-11-6复查CT示：左肺上叶团片", "影，较前2024.07.10范围增大，较2024.10.23示实性成分增多。病情较前进展。2024-11-07、2024-12-3行贝伐珠单抗800mg+替雷丽珠单抗200mg+顺铂80.00mg d1+紫杉醇脂质体270.00mg d1全身化疗2周期，因患", "者消化道反应重，2025-1-16、2025-2-6行贝伐珠单抗800mg+替雷丽珠单抗200mg+顺铂60.00mg d1+紫杉醇脂质体240.00mg d1全身化疗2周。因出现消化道反应III级，后2025-3-25改行紫杉醇聚合物胶束300mgd1联", "合卡铂400mgd1化疗，并行贝伐珠单抗800mg靶向联合替雷丽珠单抗200mg免疫治疗，2025-4-15行贝伐珠单抗800mgd0+替雷丽珠单抗200mgd0+紫杉醇聚合物胶束300mgd1+卡铂500mgd1，过程顺利。因医院紫杉醇聚合", "物胶束无货，2025-5-7行顺铂80.00mg d1+紫杉醇脂质体270mg d1化疗1周期，2025-7-28至2025-12按期行卡铂500mg d1+紫杉醇聚合物胶束300mg，并行贝伐珠单抗注射液400mg靶向、（百泽安）替雷利珠单抗注射液", "200.00mg d1免疫治疗。2026-01-19行注射用紫杉醇脂质体270mgd1+卡铂 500.00mg d1化疗1周期。2025-12-27行颈+胸部增强CT：肺癌复查：左肺团片影，较前2025-09-03增大；左肺门及纵隔多发肿大淋巴结，较", "前部分增大。病情较前进展。1周前患者无明显诱因出现双下肢疼痛，间断性，走路踩棉花样，影响夜间睡眠。现为行进一步治疗收住我科。自发病以来，精神可，饮食、睡眠欠佳，大小便无异常，近1个月体重", "较前无明显变化。", "既往史：否认“冠心病、高血压、糖尿病”病史。否认“肝炎、结核”等传染病病史及密切接触史。否认重大外伤史，否认手术史，否认输血史。无药物及食物过敏。预防接种随当地进行。", "个人史：生于原籍，无外地久居史，无疫区长期居住史，无聚集性发病。生活规律，吸烟30余年，约20支/天，偶有饮酒史，现烟酒均已戒2年，无毒物、粉尘及放射性物质接触史，无冶游史，无重大精神创", "伤史。全程接种新冠疫苗。", "婚育史：23岁结婚，配偶健在，育2女，女儿健康。", "家族史：父亲去世（具体不详），母亲健在。兄弟2人，1个弟弟健在。家族中无遗传病病史及类似病史。", "体 格 检 查", "T:36.6℃ P:80次/分 R:20次/分 Bp:132/82mmHg VTE:3分", ""]
2026-08-10 18:04:16,952 INFO     29 [qwen-vl-parser] page=4 text: 39 lines (bbox 54-92)
2026-08-10 18:04:16,952 INFO     29 [qwen-vl-parser] page=4 text: 39 sections
2026-08-10 18:04:17,194 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2150959, prompt_len=764
2026-08-10 18:04:18,541 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:04:18,542 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 18:04:18,551 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2150959, prompt_len=401
2026-08-10 18:04:30,774 INFO     29 [qwen-vl-parser] text API response (len=2106):
["个人史：生于原籍，无外地久居史，无疫区长期居住史，无聚集性发病。生活规律，吸烟30余年，约20支/天，偶有饮酒史，现烟酒均已戒2年，无毒物、粉尘及放射性物质接触史，无冶游史，无重大精神创伤史，全程接种新冠疫苗。", "婚育史：23岁结婚，配偶健在，育2女，女儿健康。", "家族史：父亲去世（具体不详），母亲健在。兄弟2人，1个弟弟健在。家族中无遗传病病史及类似病史。", "体格检查", "T:36.6℃ P:80次/分 R:20次/分 Bp:132/82mmHg VTE:3分", "H:168cm W:65kg S:1.71平方米 NRS:0分 PS:1分 NRS-2002:1分", "中年男性，发育正常，营养中等，神志清楚，自主体位，正常面容，检查合作。全身皮肤、黏膜无苍白、紫绀、黄染，无水肿、皮疹、瘀点、紫癜、皮下结节，无蜘蛛痣、肝掌。全身浅表淋巴结未触及肿大，", "局部皮肤无红肿、波动、压痛、瘘管。左侧锁骨上触及大约3×2cm肿物，质硬，固定，颈部柔软，双侧对称，颈静脉无怒张，肝颈静脉回流征阴性，无颈动脉异常搏动，气管位置居中，甲状腺无肿大，胸廓对", "称，无畸形，胸骨无压痛，胸壁无皮下气肿及静脉曲张，呼吸节律正常。双侧呼吸活动度对称，双侧语音震颤正常，无胸膜摩擦感、皮下捻发感；叩诊双肺呈清音，两肺下界在锁骨中线第六肋间，腋中线第八肋", "间，肩胛下角线第十肋间，肺下界活动度正常。双肺呼吸音粗，未闻及干湿性罗音，未闻及胸膜摩擦音。心前区无隆起，心尖搏动在锁骨中线第五肋间隙内侧0.5cm处，搏动范围及强度无异常，无震颤及心包摩擦", "感。心脏左右浊音界正常。心音正常，心率76次/分，心律规整，各瓣膜听诊区无心音分裂、额外心音、杂音，无心包摩擦音。无毛细血管搏动、射枪音、水冲脉和无动脉异常搏动。腹部对称、平坦，无肠型及胃", "肠蠕动波，无皮疹、色素、条纹，无腹壁静脉曲张，无疝和局部隆起，腹部柔软，腹无压痛、反跳痛，未触及包块，无液波震颤，肝脾肋下未触及。墨菲氏征阴性。腹部叩诊鼓音，肝上界在右锁骨中线第五肋", "间，肝肾区无叩痛，无移动性浊音。肠鸣音正常4次/分，无振水音，无血管杂音。肛门直肠及外生殖器未检查。脊柱生理弯曲正常，无畸形，无压痛和叩击痛，活动自如，腰骶部无异常。四肢无畸形，肌张力正", "常，关节无红肿，活动正常，双下肢无水肿及静脉曲张。腹壁反射、肱二、三头肌肌腱反射、膝腱反射、跟腱反射均正常存在；Babinski征阴性，Gordon征阴性，Oppenheim征阴性，Hoffmann征阴性；Kernig征阴", "性，Brudzinski征阴性。", "专科检查：双肺呼吸音粗，未闻及干湿性罗音，未闻及胸膜摩擦音。心音正常，心率76次/分，心律规整，腹部柔软，腹无压痛、反跳痛，未触及包块，无液波震颤，肝脾肋下未触及。", "辅助检查", "检查日期 检查项目 结果（检查医院）", "2023-03-30 PET/CT：1，左肺上叶高代谢占位，考虑肺癌（并累及邻近胸膜），（左侧颈部V区、左锁骨上、纵隔、左肺门10区、左肺内11-12区）多发淋巴结转移；建议病理学检查；左肺门", "10区淋巴结旁肺组织见网格样密度增高影，轻度PDG代谢增高，建议结合临床并复查。2.双肺肺气肿；双肺少许纤维条索灶。3.副鼻窦炎（双侧上颌窦、右侧筛窦）。4.冠状动脉钙化灶。5.十二指肠圈小憩室。6.", "肝脏囊肿。7.左肾囊肿。8.脊椎骨质增生；骶3水平椎管囊肿。（本院）", "2023-04-03 （左锁骨上淋巴结穿刺活检）纤维组织内查见分化差的癌，结合免疫组化及病史，不除外肺非小细胞癌转移。免疫组化结果：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（-）、", "P40（灶+）。（本院）经齐鲁医院会诊：倾向肺腺癌。", "2023-04-03 颅脑磁共振平扫+DVI+增强扫描MRI：脑内多发缺血灶，建议复查双侧上颌窦囊肿。（本院）", "2023-04-06 胸部CT增强扫描CT：1.左肺上叶恶性肿瘤并累及邻近胸膜，左锁骨上、左肺门及纵隔多发淋巴结转移 2.双肺肺气肿；双肺少许纤维条索灶 3.冠状动脉钙化灶 4.扫及肝囊肿、左", "肾囊肿。（本院）", "2023-04-10 快速石蜡病理诊断：（左肺上叶穿刺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，特殊染色待补充报告。免疫组化结果：CK5/6（-）、P40（部分", "+）、TTF-1（-）、NapsinA（-）、CK7（+）。ALK（D5F3）：阴性；（免单克隆阴性对照：阴性；阳性对照：阳性）。（本院）", "2023-04-05 基因检测：未检出与靶向治疗相关基因突变；PD-L1检测：TPS约3%。（赛泽检验）", "2023-07-20 胸部CT：1.肺癌复查：左肺上叶占位，较前（2023-06-30）范围缩小；左锁骨上、左肺门及纵隔多发淋巴结转移，较前变化不大 2.双肺肺气肿；双肺少许纤维条索灶 3.主动脉及", ""]
2026-08-10 18:04:30,775 INFO     29 [qwen-vl-parser] page=5 text: 30 lines (bbox 93-122)
2026-08-10 18:04:30,775 INFO     29 [qwen-vl-parser] page=5 text: 30 sections
2026-08-10 18:04:30,960 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1358780, prompt_len=764
2026-08-10 18:04:32,303 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:04:32,304 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-10 18:04:32,322 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1358780, prompt_len=401
2026-08-10 18:04:36,579 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:04:36.579+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 84, "failed": 0, "current": {"d64c79b494e511f1bd9827cf206dfa2d": {"id": "d64c79b494e511f1bd9827cf206dfa2d", "doc_id": "d60771c094e511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 5825068, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385028897, "task_type": "dataflow", "root_trace_id": "93629fbf7f764cf397a9e7f896dd05c6", "root_traceparent": "00-93629fbf7f764cf397a9e7f896dd05c6-e7dded3dfece48a2-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:04:40,107 INFO     29 [qwen-vl-parser] text API response (len=1317):
["2023-07-20", "胸部CT：1.肺癌复查：左肺上叶占位，较前（2023-06-30）范围缩小；左锁骨上、左肺门及纵隔多发淋巴结转移，较前变化不大2.双肺肺气肿；双肺少许纤维条索灶3.主动脉及", "冠状动脉钙化4.扫及肝囊肿胸部CT平扫，下腹部（肾）CT平扫，上腹部CT平扫，盆腔CT平扫CT（2023-08-11）：1.肺癌复查：左肺上叶占位，范围较前（2023-7-20）减小；左锁骨上、左肺门及纵隔多发稍大淋巴", "结，较前变化不大2.双肺肺气肿；双肺少许条索灶3.主动脉及冠状动脉钙化4.肝囊肿5.左肾稍低密度灶，建议超声检查；左肾囊肿6.十二指肠降段憩室7.右侧髂骨稍高密度灶，建议复查8.考虑骶管（S3-4", "水平）囊肿。（本院）", "2025-03-11", "颈部+胸部增强CT：1.肺癌复查：左肺团片影，较前25.2.6范围相仿；2.双肺微小结节，原左肺新增结节较前略小（im149薄层），转移不除外，余较前相仿，定期复查；3.双肺", "肺气肿；双肺条索灶；4.左肺门及纵隔多发稍大淋巴结，较前相仿；5.主动脉及冠状动脉钙化；心包少量积液；左侧胸膜局限性增厚；6.扫及肝囊肿；左肾囊肿。（本院）", "2025-09-02", "颅脑磁共振成像+DWI（特殊序列成像）MR：考虑脑内多发小缺血灶，较前（2024-11-8）变化不著，建议复查。左侧上颌窦囊肿。（本院）", "2025-09-03", "颈部CT增强扫描，胸部CT增强扫描，上腹部CT增强扫描，盆腔CT增强扫描，下腹部CT增强扫描：1.肺癌复查：左肺团片影，较前2025.05.07范围略增大，建议复查2.双肺微小结节，", "较前变化不大，转移不除外，建议定期复查3.双肺肺气肿；双肺条索灶4.左肺门及纵隔多发稍大淋巴结，较前略大5.主动脉及冠状动脉钙化；心包少量积液；左侧胸膜局限性增厚6.肝囊肿；左肾囊肿7.", "十二指肠降段憩室8.右侧髂骨稍高密度灶，较前2024.11.06变化不大，建议复查9.考虑骶管囊肿10.颈部未见明显异常；扫及双侧上颌窦炎。（本院）", "2025-12-27", "颈+胸部增强CT：1.肺癌复查：左肺团片影，较前2025-09-03增大；周围新发实变及网格影，请结合临床，建议复查；2.双肺小结节及小斑片影，较前部分增大，部分新发，部分", "变化不大，建议定期复查；3.双肺肺气肿；双肺条索灶；双肺胸膜下磨玻璃密度影，请结合临床随诊复查；4.左肺门及纵隔多发肿大淋巴结，较前部分增大；5.主动脉及冠状动脉钙化；心包少量积液；左侧胸", "膜局限性增厚；左侧胸腔少量积液；6.扫及肝囊肿；左肾囊肿7.颈部未见明显异常；扫及双侧上颌窦炎。（本院）", "初步诊断", "1、左肺上叶癌腺癌cT3N3MOIIIC期", "纵隔淋巴结转移", "锁骨上淋巴结转移", "肺门淋巴结转移", "颈部淋巴结转移", "2、肺气肿", "3、鼻窦炎", "4、肝囊肿", "5、肾囊肿", "6、上颌窦囊肿", "我审核病史记录内容属实无遗漏，我交给医院的病例资料已收回，患方签字：", "宗茹"]
2026-08-10 18:04:40,108 INFO     29 [qwen-vl-parser] page=6 text: 31 lines (bbox 123-153)
2026-08-10 18:04:40,108 INFO     29 [qwen-vl-parser] page=6 text: 31 sections
2026-08-10 18:04:40,263 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=754375, prompt_len=764
2026-08-10 18:04:41,725 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-03-09"}
```
2026-08-10 18:04:41,726 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=2026-03-09
2026-08-10 18:04:41,734 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=754375, prompt_len=401
2026-08-10 18:04:44,218 INFO     29 [qwen-vl-parser] text API response (len=417):
["出生日期：", "1968/12/4", "年龄", "57年，M", "检查项目：", "胸部磁共振平扫+DWI+动态增强成像", "影像登录号：", "MR10060372", "报告状态：", "Correction", "原因：", "不可选", "主要位置：", "2328", "检查日期：", "2026/3/9 7:44:30", "顺序 #：", "MR10060372", "影像诊断", "左肺癌复查所见。", "纵隔内多发淋巴结肿大。", "肝脏、左肾多发囊肿。", "影像表现", "左上肺示一截面约99x61mm的团块影，呈等长T1等长T2、DWI等高信号，不均匀强化，左上肺门及纵隔与之紧密相贴。右肺未见明显异常信号影，右肺门未见明显增大。纵隔内隆凸下示多发稍大淋巴结，心影大小形态可。未见明显胸腔积液。肝脏、左肾示", "多发囊状长T1长T2信号影，大者直径约21mm。", "成像方法", ""]
2026-08-10 18:04:44,219 INFO     29 [qwen-vl-parser] page=7 text: 26 lines (bbox 154-179)
2026-08-10 18:04:44,219 INFO     29 [qwen-vl-parser] page=7 text: 26 sections
2026-08-10 18:04:44,416 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1143459, prompt_len=764
2026-08-10 18:04:45,814 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-01-24"}
```
2026-08-10 18:04:45,815 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=2026-01-24
2026-08-10 18:04:45,824 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1143459, prompt_len=401
2026-08-10 18:04:52,225 INFO     29 [qwen-vl-parser] text API response (len=654):
["年龄：57岁 住院号：5 入院日期：2026-03-04 15:35 床号：35床", "单项 多项 全选 反选 取消", "插入病历 插入预览", "检查时间 项目名称", "2026-03-10 09:49:54 快速石蜡+免疫组", "2026-03-09 08:04:30 MR", "2026-03-07 15:12:50 快速石蜡+免疫组", "2026-02-02 08:40:51 核医学检查", "2026-01-30 08:16:50 MR", "2026-01-27 15:36:02 双下肢浅静脉彩色", "2026-01-27 15:33:31 双下肢动脉彩色多", "2026-01-27 13:41:19 CT", "2026-01-26 09:27:13 CT", "2026-01-25 15:07:01 MR", "2026-01-24 10:22:13 十二通道", "2025-09-03 08:09:17 CT", "2025-09-02 19:12:41 MR", "2024-11-08 11:13:19 MRI", "2024-11-07 09:14:33 腋窝淋巴结彩超|", "2024-11-07 08:08:48 核医学检查", "2024-11-06 17:18:00 CT", "检查项目：十二通道 检查名称：十二通道 检查部位：", "□检查所见：", "□检查结论：", "1、窦性心动过速 2、ST段轻度改变", "报告医 审核医生："]
2026-08-10 18:04:52,226 INFO     29 [qwen-vl-parser] page=8 text: 26 lines (bbox 180-205)
2026-08-10 18:04:52,226 INFO     29 [qwen-vl-parser] page=8 text: 26 sections
2026-08-10 18:04:52,571 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2631672, prompt_len=764
2026-08-10 18:04:54,118 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2026-03-05"}
```
2026-08-10 18:04:54,120 INFO     29 [qwen-vl-parser] page=9 classify=table report_date=2026-03-05
2026-08-10 18:04:54,143 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2631672, prompt_len=756
2026-08-10 18:05:06,917 INFO     29 [qwen-vl-parser] table API response (len=2578):
\begin{tabular}{|c|c|l|l|l|c|l|l|l|l|}
\hline
采样 & 行号 & 中文名 & 项目... & 结果 & 状态 & 项目... & 参考范围 & 单位 & \\
\hline
26-03- & 2 & 天门冬氨酸氨基转移... & & 19 & & 10010 & 15-40 & U/L & \\
\hline
26-03- & 3 & AST/ALT & 肝脏... & 1.73 & & 10021 & 0.10-3.00 & & \\
\hline
26-03- & 4 & 总胆红素*#☆ & & 6.9 & & 10080 & ≤23.0 & um & \\
\hline
26-03- & 5 & 直接胆红素*#☆ & & 2.0 & & 10090 & 0-6.8 & um & \\
\hline
& 6 & 间接胆红素 & & 4.9 & & 10100 & 3.4-17.1 & um & \\
\hline
& 7 & 总蛋白*#☆ & 项目... & 64.1 & $\downarrow$ & 10040 & 65.0-85.0 & g/L & \\
\hline
& 8 & 白蛋白*#☆ & 可作... & 29.8 & $\downarrow$ & 10050 & 40.0-55.0 & g/L & \\
\hline
& 9 & 球蛋白 & & 34.3 & & 10060 & 20.0-40.0 & g/L & \\
\hline
& 10 & 白球比 & & 0.87 & $\downarrow$ & 10070 & 1.20-2.40 & & \\
\hline
& 11 & 碱性磷酸酶*#☆ & 骨骼... & 95 & & 10110 & 45-125 & U/L & \\
\hline
& 12 & 谷氨酸脱氢酶 & 肝脏... & 5 & & 10470 & 0-7 & U/L & \\
\hline
& 13 & γ-谷氨酰转肽酶*#☆ & & 20 & & 10130 & 10-60 & U/L & \\
\hline
& 14 & 胆碱酯酶*# & & 5357 & & 10020 & 5000-12000 & U/L & \\
\hline
& 15 & 甘胆酸 & & 1.43 & & 11160 & 0.00-2.70 & ug/ & \\
\hline
& 16 & 总胆汁酸* & & 1.40 & & 10030 & 0.00-10.00 & um & \\
\hline
& 17 & 前白蛋白*☆ & & 100 & $\downarrow$ & 10400 & 200-430 & mg & \\
\hline
& 18 & 尿素*#☆ & & 1.6 & $\downarrow$ & 10180 & 3.1-8.0 & mm & \\
\hline
& 19 & 肌酐*#☆ & & 34.0 & $\downarrow$ & 10190 & 57-97 & um & \\
\hline
& 20 & 尿素/肌酐 & & 0.05 & & 10191 & 0.01-0.70 & & \\
\hline
& 21 & 估算肾小球滤过率 & & 130 & & 10192 & & mL & \\
\hline
& 22 & 葡萄糖*#☆ & & 7.8 & $\uparrow$ & 10170 & 3.9-6.1 & mm & \\
\hline
& 23 & 尿酸*#☆ & & 183 & $\downarrow$ & 10200 & 208-428 & um & \\
\hline
& 24 & 乳酸脱氢酶*#☆ & 心肌... & 241 & & 10120 & 120-250 & U/L & \\
\hline
& 25 & 肌酸激酶*#☆ & 心肌... & 36 & $\downarrow$ & 10140 & 50-310 & U/L & \\
\hline
& 26 & 钾*#☆ & & 4.1 & & 10320 & 3.5-5.3 & mm & \\
\hline
& 27 & 钠*#☆ & & 132 & $\downarrow$ & 10330 & 137-147 & mm & \\
\hline
& 28 & 氯*#☆ & & 93 & $\downarrow$ & 10340 & 99-110 & mm & \\
\hline
& 29 & 总二氧化碳 & TCO... & 30 & $\uparrow$ & 10351 & 22-29 & mm & \\
\hline
& 30 & 总钙*#☆ & & 2.28 & & 10280 & 2.11-2.52 & mm & \\
\hline
& 31 & 磷*#☆ & & 0.97 & & 10290 & 0.85-1.51 & mm & \\
\hline
& 32 & 镁*#☆ & & 0.69 & $\downarrow$ & 10310 & 0.75-1.02 & mm & \\
\hline
& 33 & 阴离子间隙 & & 9 & & 10660 & 8-16 & mm & \\
\hline
& 34 & 渗透压 & & 264 & $\downarrow$ & 10670 & 275-300 & mC & \\
\hline
& 35 & α-羟丁酸脱氢酶*#☆ & & 154 & & 10160 & 72-182 & U/L & \\
\hline
& 36 & 唾液酸 & & 1126 & $\uparrow$ & 10560 & 456-754 & mg & \\
\hline
& 37 & 淀粉酶*#☆ & & 28 & $\downarrow$ & 10341 & 35-135 & U/L & \\
\hline
& 38 & 肌酸激酶同工酶质量... & & 1.95 & & 10950 & 0-5.0 & ng/ & \\
\hline
\end{tabular}
2026-08-10 18:05:06,920 INFO     29 [qwen-vl-parser] page=9 table: 80 LaTeX lines (bbox 206-285)
2026-08-10 18:05:06,920 INFO     29 [qwen-vl-parser] page=9 table: 80 sections
2026-08-10 18:05:07,145 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1371720, prompt_len=764
2026-08-10 18:05:08,624 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2026-03-05"}
```
2026-08-10 18:05:08,625 INFO     29 [qwen-vl-parser] page=10 classify=table report_date=2026-03-05
2026-08-10 18:05:08,652 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1371720, prompt_len=756
2026-08-10 18:05:08,680 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:05:08.679+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 84, "failed": 0, "current": {"d64c79b494e511f1bd9827cf206dfa2d": {"id": "d64c79b494e511f1bd9827cf206dfa2d", "doc_id": "d60771c094e511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 5825068, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385028897, "task_type": "dataflow", "root_trace_id": "93629fbf7f764cf397a9e7f896dd05c6", "root_traceparent": "00-93629fbf7f764cf397a9e7f896dd05c6-e7dded3dfece48a2-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:05:13,017 INFO     29 [qwen-vl-parser] table API response (len=830):
\begin{tabular}{|c|c|l|c|c|c|l|l|}
\hline
\textbf{行号} & \textbf{中文名} & \textbf{项目...} & \textbf{结果} & \textbf{状态} & \textbf{项目...} & \textbf{参考范围} & \textbf{单位} \\
\hline
1 & 凝血酶原时间活动度 & & 84.89 & & 60110 & 70.0-130.0 & \% \\
\hline
2 & 凝血酶原时间比值 & & 1.16 & $\uparrow$ & 60120 & 0.82-1.15 & \\
\hline
3 & 国际标准化比值*#☆ & & 1.17 & & 60020 & 1.0-2.0;口服抗凝... & \\
\hline
4 & 活化部分凝血活酶时... & 是内... & 31.3 & & 60030 & 20.5-33.4 & 秒 \\
\hline
5 & 活化部分凝血活酶时... & 是内... & 1.18 & & 60031 & 0.77-1.25 & \\
\hline
6 & 纤维蛋白原*# & & 9.170 & $\uparrow$ & 60040 & 2.00-4.00 & g/L \\
\hline
7 & 凝血酶时间*# & & 15.80 & & 60050 & 15.2-22.0 & 秒 \\
\hline
8 & D-二聚体* & 继发... & 0.55 & & 60070 & 0.00-0.56 & mg/L \\
\hline
9 & 抗凝血酶活性* & & 100.74 & & 60080 & 80.0-120.0 & \% \\
\hline
10 & 纤维蛋白(原)降解产物* & & 3.53 & & 60130 & 0.0-5.0 & mg/L \\
\hline
\end{tabular}
2026-08-10 18:05:13,018 INFO     29 [qwen-vl-parser] page=10 table: 26 LaTeX lines (bbox 286-311)
2026-08-10 18:05:13,018 INFO     29 [qwen-vl-parser] page=10 table: 26 sections
2026-08-10 18:05:13,333 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1962680, prompt_len=764
2026-08-10 18:05:14,924 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2016-03-03"}
```
2026-08-10 18:05:14,924 INFO     29 [qwen-vl-parser] page=11 classify=table report_date=2016-03-03
2026-08-10 18:05:14,931 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1962680, prompt_len=756
2026-08-10 18:05:22,879 INFO     29 [qwen-vl-parser] table API response (len=1141):
\begin{tabular}{|c|l|l|c|c|l|l|l|}
\hline
行号 & 中文名 & 项目... & 结果 & 状态 & 项目... & 参考范围 & 单位 \\
\hline
2 & 游离甲状腺素*#☆ & & 14.70 & & 1002... & 12-22 & pmol.. \\
\hline
3 & 促甲状腺激素*#☆ & & 1.320 & & 1002... & 0.27-4.2 & uIU/... \\
\hline
4 & 鳞状细胞癌相关抗原*☆ & & 0.54 & & 1009... & 0-2.5 & ng/ml \\
\hline
5 & 糖类抗原CA-50* & & 3.73 & & 1003... & 0-25 & IU/ml \\
\hline
6 & 糖类抗原CA-242* & & 0.94 & & 1003... & 0-20 & IU/ml \\
\hline
7 & 糖类抗原CA-724*☆ & & 0.95 & & 1003... & 0-6.0 & U/mL \\
\hline
8 & 癌胚抗原*#☆ & & 41.00 & $\uparrow$ & 1001... & 0-5.09 & ng/ml \\
\hline
9 & 糖类抗原CA-199*# & & 9.28 & & 1003... & 0.00-27.00 & U/mL \\
\hline
10 & 糖类抗原CA-125*#☆ & & 21.50 & & 1003... & 0.00-35.00 & U/mL \\
\hline
11 & 糖类抗原CA-153*#☆ & & 15.40 & & 1003... & 0.00-26.2 & U/mL \\
\hline
12 & 神经元特异性烯醇化... & & 17.60 & $\uparrow$ & 1007... & 0.00-16.30 & ng/ml \\
\hline
13 & 细胞角蛋白19片段*☆ & & 4.57 & $\uparrow$ & 1007... & 0.00-3.30 & ng/ml \\
\hline
14 & 铁蛋白*#☆ & & 416.00 & $\uparrow$ & 1007... & 30.00-400.00 & ng/ml \\
\hline
15 & β2微球蛋白*# & & 1.380 & & 1011... & 0.90-2.70 & mg/L \\
\hline
16 & 胃泌素释放肽前体 & & 22.100 & & 1015... & 0-68.3 & pg/ml \\
\hline
\end{tabular}
2026-08-10 18:05:22,881 INFO     29 [qwen-vl-parser] page=11 table: 36 LaTeX lines (bbox 312-347)
2026-08-10 18:05:22,881 INFO     29 [qwen-vl-parser] page=11 table: 36 sections
2026-08-10 18:05:23,171 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2065147, prompt_len=764
2026-08-10 18:05:24,635 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "table", "report_date": "2026-3-10"}
```
2026-08-10 18:05:24,636 INFO     29 [qwen-vl-parser] page=12 classify=table report_date=2026-3-10
2026-08-10 18:05:24,653 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2065147, prompt_len=756
2026-08-10 18:05:34,101 INFO     29 [qwen-vl-parser] table API response (len=1920):
\begin{tabular}{|c|l|l|l|l|l|l|l|}
\hline
行号 & 中文名 & 项目... & 结果 & 状态 & 项目... & 参考范围 & 单位 \\
\hline
6-03- & & & & & & & \\
\hline
6-03-2 & 中性粒细胞计数 & 正常... & 13.55 & $\uparrow$ & 30070 & 1.80-6.30 & *10^... \\
\hline
6-03-3 & 淋巴细胞计数 & 正常... & 1.86 & & 30050 & 1.10-3.20 & *10^... \\
\hline
5-03-4 & 单核细胞计数 & 正常... & 1.32 & $\uparrow$ & 30060 & 0.10-0.60 & *10^... \\
\hline
5-03-5 & 嗜酸细胞计数 & & 0.00 & $\downarrow$ & 30210 & 0.02-0.52 & *10^... \\
\hline
6 & 嗜碱细胞计数 & & 0.07 & $\uparrow$ & 30220 & 0.00-0.06 & *10^... \\
\hline
7 & 中性粒细胞百分比 & 正常... & 80.6 & $\uparrow$ & 30040 & 40.0-75.0 & \% \\
\hline
8 & 淋巴细胞百分比 & 正常... & 11.1 & $\downarrow$ & 30020 & 20.0-50.0 & \% \\
\hline
9 & 单核细胞百分比 & 正常... & 7.9 & & 30030 & 3.0-10.0 & \% \\
\hline
10 & 嗜酸细胞百分比 & 参考... & 0.0 & $\downarrow$ & 30190 & 0.40-8.00 & \% \\
\hline
11 & 嗜碱细胞百分比 & & 0.4 & & 30200 & 0.00-1.00 & \% \\
\hline
12 & 红细胞计数*#☆ & 参考... & 3.69 & $\downarrow$ & 30080 & 4.30-5.80 & *10^... \\
\hline
13 & 血红蛋白含量*#☆ & 正常... & 102 & $\downarrow$ & 30090 & 130-175 & g/L \\
\hline
14 & 红细胞比容*#☆ & 正常... & 0.32 & $\downarrow$ & 30100 & 0.40-0.50 & L/L \\
\hline
15 & 平均红细胞血红蛋白... & 正常... & 27.6 & & 30120 & 27.0-34.0 & pg \\
\hline
16 & 平均红细胞血红蛋白... & 正常... & 318 & & 30130 & 316-354 & g/L \\
\hline
17 & 平均红细胞体积*#☆ & 正常... & 87.0 & & 30110 & 82.0-100.0 & fL \\
\hline
18 & 红细胞分布宽度（CV） & 正常... & 17.3 & $\uparrow$ & 30140 & 11.6-16.5 & \% \\
\hline
19 & 红细胞分布宽度（SD） & & 54.6 & $\uparrow$ & 30230 & 37.0-54.0 & fL \\
\hline
20 & 血小板计数*#☆ & 参考... & 466 & $\uparrow$ & 30150 & 125-350 & *10^... \\
\hline
21 & 平均血小板体积 & 正常... & 8.8 & & 30160 & 7.4-11.0 & fL \\
\hline
22 & 大血小板比率 & 正常... & 15.7 & & 30170 & 13.0-43.0 & \% \\
\hline
23 & 血小板比容 & & 0.41 & $\uparrow$ & 30240 & 0.170-0.350 & \% \\
\hline
24 & 血小板分布宽度 & 正常... & 8.5 & $\downarrow$ & 30180 & 9.6-15.2 & fL \\
\hline
25 & C-反应蛋白* & & 177.... & $\uparrow$ & 30340 & 0.000-5.000 & mg/L \\
\hline
\end{tabular}
2026-08-10 18:05:34,101 INFO     29 [qwen-vl-parser] page=12 table: 56 LaTeX lines (bbox 348-403)
2026-08-10 18:05:34,102 INFO     29 [qwen-vl-parser] page=12 table: 56 sections
2026-08-10 18:05:34,157 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=193590, prompt_len=764
2026-08-10 18:05:35,298 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:05:35,298 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=None
2026-08-10 18:05:35,307 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=193590, prompt_len=401
2026-08-10 18:05:37,464 INFO     29 [qwen-vl-parser] text API response (len=302):
["20230403穿刺病理确诊肺鳞癌", "20230407~20230630替雷+贝伐+卡铂+培美5周期", "20230706放疗，结束时间20230809", "20230719卡铂+恩度+替雷", "20230810恩度+替雷", "20240930顺铂+贝伐+替雷", "202411进展", "20241107、20241203、20250116、20250206、20250325贝伐+替雷+顺铂+紫", "衫", "20250415贝伐+替雷+卡铂+紫衫", "20250507顺铂+紫衫", "20250728~202512贝伐+替雷+卡铂+紫衫", "20260119卡铂+紫衫"]
2026-08-10 18:05:37,465 INFO     29 [qwen-vl-parser] page=13 text: 13 lines (bbox 404-416)
2026-08-10 18:05:37,465 INFO     29 [qwen-vl-parser] page=13 text: 13 sections
2026-08-10 18:05:37,465 INFO     29 [qwen-vl-parser] parse_pdf done: 417 sections from 13 pages.
2026-08-10 18:05:37,479 INFO     29 Close text detector.
2026-08-10 18:05:37,976 INFO     29 Close text recognizer.
2026-08-10 18:05:38,396 INFO     29 Close recognizer.
2026-08-10 18:05:38,824 INFO     29 Close recognizer.
2026-08-10 18:05:39,641 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 18:05:39,641 INFO     29 [Trace] task=d64c79b4 | doc=07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf | Parser:MedLink | outputs={"html": "", "json": "417 items", "markdown": "", "text": "", "name": "07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf", "output_format": "json"}
2026-08-10 18:05:39,641 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 18:05:39,658 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:05:39,658 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 姓名\n[BBOX-1] 性别：男\n[BBOX-2] 年龄：57\n[BBOX-3] 门诊号：\n[BBOX-4] 科别：\n[BBOX-5] 病区\n[BBOX-6] 床号\n[BBOX-7] 住院号：\n[BBOX-8] 取材部位：左肺\n[BBOX-9] 补充内容：\n[BBOX-10] 快速石蜡病理诊断：\n[BBOX-11] （左肺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，免疫组化\n[BBOX-12] 及特殊染色待补充报告。\n[BBOX-13] 免疫组化结果：CK5/6（-）、TTF-1（-）、NapsinA（-）、P40（部分+）、Villin（-）、CK7\n[BBOX-14] （+）、CDX2（-）\n[BBOX-15] ALK伴随诊断：\n[BBOX-16] ALK（D5F3）：阴性；（兔单克隆阴性对照：阴性；阳性对照：阳性）\n[BBOX-17] 性别：男\n[BBOX-18] 年龄：57\n[BBOX-19] 门诊号：\n[BBOX-20] 科别：\n[BBOX-21] 床号\n[BBOX-22] 送检医生\n[BBOX-23] 住院号\n[BBOX-24] 病区\n[BBOX-25] 送检日期：2026-3-6 15:05:29\n[BBOX-26] 取材信息：\n[BBOX-27] 灰白灰红条状碎组织一堆，共计直径0.8cm。\n[BBOX-28] 病理诊断：\n[BBOX-29] 快速石蜡病理诊断：\n[BBOX-30] （左肺活检）分化差的癌，待免疫组化结果进一步明确分型。\n[BBOX-31] 病理会诊报告单\n[BBOX-32] 病理号:\n[BBOX-33] 姓名\n[BBOX-34] 性别: 男\n[BBOX-35] 年龄: 54岁\n[BBOX-36] 送检单位\n[BBOX-37] 送检日期: 2023/4/4\n[BBOX-38] 送检医生:\n[BBOX-39] 镜下所见:\n[BBOX-40] 原病理诊断:\n[BBOX-41] 读“青岛市中心医疗集团”报告, 病理号: 2307637, HE×1, IHC*5, 原诊断: (左锁骨上淋\n[BBOX-42] 巴结穿刺活检) 纤维组织内查见分化差的癌, 结合免疫组化及病史, 不除外肺非小细胞癌转\n[BBOX-43] 移。\n[BBOX-44] 免疫组化结果: TTF-1 (-), NapsinA (-), CK7 (+), CK 5/6 (-), P40 (灶+)。\n[BBOX-45] 病理会诊诊断:\n[BBOX-46] (左锁骨上淋巴结穿刺活检) 纤维组织内查见片状、实体状异型上皮样细胞浸润, 结合临床及\n[BBOX-47] 免疫标记, 考虑低分化癌, 可能为肺非小细胞癌转移, 倾向腺癌, 建议粘液染色进一步协助诊\n[BBOX-48] 断。\n[BBOX-49] 原单位免疫组化结果: TTF-1 (-), NapsinA (-), CK7 (+), CK 5/6 (-), P40 (个别细胞\n[BBOX-50] +)。\n[BBOX-51] 报告时间:2023-4-4\n[BBOX-52] 诊断医师:姜慧峰\n[BBOX-53] 注: 病理医师个人会诊咨询意见, 仅供原病理学\n[BBOX-54] 开始 | 病历列表\n[BBOX-55] 35_孙正福_住院\n[BBOX-56] < > X\n[BBOX-57] 页\n[BBOX-58] 控\n[BBOX-59] 消\n[BBOX-60] 息\n[BBOX-61] 2026-03-04 15:46 入院记录\n[BBOX-62] 性别：男\n[BBOX-63] 职业：其他\n[BBOX-64] 年龄：57岁\n[BBOX-65] 入院时间：2026-03-04 15:38:00\n[BBOX-66] 民族：汉族\n[BBOX-67] 记录时间：2026-03-04 15:46\n[BBOX-68] 婚姻：已婚\n[BBOX-69] 病史陈述者：患者本人及家属\n[BBOX-70] 主诉：确诊左肺癌2年余，双下肢疼痛1周。\n[BBOX-71] 现病史：患者2年余前查体发现左颈部肿物，约豆粒大小，无疼痛，偶有咳嗽、咳痰，无痰中带血丝，活动后偶感胸闷、憋气，无咯血，无胸痛，无发热。后肿物逐渐增大，遂就诊于我院，2023-03-30行\n[BBOX-72] PET/CT：1，左肺上叶高代谢占位，考虑肺癌（并累及邻近胸膜），（左侧颈部V区、左锁骨上、纵隔、左肺门10区、左肺内11-12区）多发淋巴结转移；建议病理学检查；左肺门10区淋巴结旁肺组织见网格样密度\n[BBOX-73] 增高影，轻度PDG代谢增高，建议结合临床并复查。未行特殊治疗。后就诊于我科，2023-04-03行快速石蜡病理诊断：（左锁骨上淋巴结穿刺活检）纤维组织内查见分化差的癌，结合免疫组化及病史，不除外肺非\n[BBOX-74] 小细胞癌转移。经齐鲁医院会诊：倾向肺腺癌。免疫组化结果：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（-）、P40（灶+）。2023-04-06行胸部增强CT：左肺上叶恶性肿瘤并累及邻近胸膜，左锁骨上、左\n[BBOX-75] 肺门及纵隔多发淋巴结转移。快速石蜡病理诊断：（左肺上叶穿刺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，特殊染色待补充报告。免疫组化结果：CK5/6（-）、P40（部分+）、\n[BBOX-76] TTF-1（-）、NapsinA（-）、CK7（+）。ALK（D5F3）：阴性；（兔单克隆阴性对照：阴性；阳性对照：阳性）。2023-04-07至2023-06-30行替雷利珠单抗200mg免疫治疗+贝伐珠单抗注射液900.00mg靶向治\n[BBOX-77] 疗，联合卡铂500.00mg d1+培美曲塞二钠850.00mg d1化疗5周期。排除禁忌，患者于2023-07-06行胸部IMRT放疗，具体：IMRT,PTV 60GY/30F，末次放疗时间为2023-08-09。2023-07-19行卡铂500mg化疗联合恩度\n[BBOX-78] 靶向及替雷利珠单抗免疫治疗。2023-08-10予以患者恩度靶向及替雷利珠单抗免疫治疗。2024-09-30行顺铂40mgd1化疗，联合贝伐珠单抗注射液靶向、替雷利珠单抗免疫治疗。2024-11-6复查CT示：左肺上叶团片\n[BBOX-79] 影，较前2024.07.10范围增大，较2024.10.23示实性成分增多。病情较前进展。2024-11-07、2024-12-3行贝伐珠单抗800mg+替雷丽珠单抗200mg+顺铂80.00mg d1+紫杉醇脂质体270.00mg d1全身化疗2周期，因患\n[BBOX-80] 者消化道反应重，2025-1-16、2025-2-6行贝伐珠单抗800mg+替雷丽珠单抗200mg+顺铂60.00mg d1+紫杉醇脂质体240.00mg d1全身化疗2周。因出现消化道反应III级，后2025-3-25改行紫杉醇聚合物胶束300mgd1联\n[BBOX-81] 合卡铂400mgd1化疗，并行贝伐珠单抗800mg靶向联合替雷丽珠单抗200mg免疫治疗，2025-4-15行贝伐珠单抗800mgd0+替雷丽珠单抗200mgd0+紫杉醇聚合物胶束300mgd1+卡铂500mgd1，过程顺利。因医院紫杉醇聚合\n[BBOX-82] 物胶束无货，2025-5-7行顺铂80.00mg d1+紫杉醇脂质体270mg d1化疗1周期，2025-7-28至2025-12按期行卡铂500mg d1+紫杉醇聚合物胶束300mg，并行贝伐珠单抗注射液400mg靶向、（百泽安）替雷利珠单抗注射液\n[BBOX-83] 200.00mg d1免疫治疗。2026-01-19行注射用紫杉醇脂质体270mgd1+卡铂 500.00mg d1化疗1周期。2025-12-27行颈+胸部增强CT：肺癌复查：左肺团片影，较前2025-09-03增大；左肺门及纵隔多发肿大淋巴结，较\n[BBOX-84] 前部分增大。病情较前进展。1周前患者无明显诱因出现双下肢疼痛，间断性，走路踩棉花样，影响夜间睡眠。现为行进一步治疗收住我科。自发病以来，精神可，饮食、睡眠欠佳，大小便无异常，近1个月体重\n[BBOX-85] 较前无明显变化。\n[BBOX-86] 既往史：否认“冠心病、高血压、糖尿病”病史。否认“肝炎、结核”等传染病病史及密切接触史。否认重大外伤史，否认手术史，否认输血史。无药物及食物过敏。预防接种随当地进行。\n[BBOX-87] 个人史：生于原籍，无外地久居史，无疫区长期居住史，无聚集性发病。生活规律，吸烟30余年，约20支/天，偶有饮酒史，现烟酒均已戒2年，无毒物、粉尘及放射性物质接触史，无冶游史，无重大精神创\n[BBOX-88] 伤史。全程接种新冠疫苗。\n[BBOX-89] 婚育史：23岁结婚，配偶健在，育2女，女儿健康。\n[BBOX-90] 家族史：父亲去世（具体不详），母亲健在。兄弟2人，1个弟弟健在。家族中无遗传病病史及类似病史。\n[BBOX-91] 体 格 检 查\n[BBOX-92] T:36.6℃ P:80次/分 R:20次/分 Bp:132/82mmHg VTE:3分\n[BBOX-93] 个人史：生于原籍，无外地久居史，无疫区长期居住史，无聚集性发病。生活规律，吸烟30余年，约20支/天，偶有饮酒史，现烟酒均已戒2年，无毒物、粉尘及放射性物质接触史，无冶游史，无重大精神创伤史，全程接种新冠疫苗。\n[BBOX-94] 婚育史：23岁结婚，配偶健在，育2女，女儿健康。\n[BBOX-95] 家族史：父亲去世（具体不详），母亲健在。兄弟2人，1个弟弟健在。家族中无遗传病病史及类似病史。\n[BBOX-96] 体格检查\n[BBOX-97] T:36.6℃ P:80次/分 R:20次/分 Bp:132/82mmHg VTE:3分\n[BBOX-98] H:168cm W:65kg S:1.71平方米 NRS:0分 PS:1分 NRS-2002:1分\n[BBOX-99] 中年男性，发育正常，营养中等，神志清楚，自主体位，正常面容，检查合作。全身皮肤、黏膜无苍白、紫绀、黄染，无水肿、皮疹、瘀点、紫癜、皮下结节，无蜘蛛痣、肝掌。全身浅表淋巴结未触及肿大，\n[BBOX-100] 局部皮肤无红肿、波动、压痛、瘘管。左侧锁骨上触及大约3×2cm肿物，质硬，固定，颈部柔软，双侧对称，颈静脉无怒张，肝颈静脉回流征阴性，无颈动脉异常搏动，气管位置居中，甲状腺无肿大，胸廓对\n[BBOX-101] 称，无畸形，胸骨无压痛，胸壁无皮下气肿及静脉曲张，呼吸节律正常。双侧呼吸活动度对称，双侧语音震颤正常，无胸膜摩擦感、皮下捻发感；叩诊双肺呈清音，两肺下界在锁骨中线第六肋间，腋中线第八肋\n[BBOX-102] 间，肩胛下角线第十肋间，肺下界活动度正常。双肺呼吸音粗，未闻及干湿性罗音，未闻及胸膜摩擦音。心前区无隆起，心尖搏动在锁骨中线第五肋间隙内侧0.5cm处，搏动范围及强度无异常，无震颤及心包摩擦\n[BBOX-103] 感。心脏左右浊音界正常。心音正常，心率76次/分，心律规整，各瓣膜听诊区无心音分裂、额外心音、杂音，无心包摩擦音。无毛细血管搏动、射枪音、水冲脉和无动脉异常搏动。腹部对称、平坦，无肠型及胃\n[BBOX-104] 肠蠕动波，无皮疹、色素、条纹，无腹壁静脉曲张，无疝和局部隆起，腹部柔软，腹无压痛、反跳痛，未触及包块，无液波震颤，肝脾肋下未触及。墨菲氏征阴性。腹部叩诊鼓音，肝上界在右锁骨中线第五肋\n[BBOX-105] 间，肝肾区无叩痛，无移动性浊音。肠鸣音正常4次/分，无振水音，无血管杂音。肛门直肠及外生殖器未检查。脊柱生理弯曲正常，无畸形，无压痛和叩击痛，活动自如，腰骶部无异常。四肢无畸形，肌张力正\n[BBOX-106] 常，关节无红肿，活动正常，双下肢无水肿及静脉曲张。腹壁反射、肱二、三头肌肌腱反射、膝腱反射、跟腱反射均正常存在；Babinski征阴性，Gordon征阴性，Oppenheim征阴性，Hoffmann征阴性；Kernig征阴\n[BBOX-107] 性，Brudzinski征阴性。\n[BBOX-108] 专科检查：双肺呼吸音粗，未闻及干湿性罗音，未闻及胸膜摩擦音。心音正常，心率76次/分，心律规整，腹部柔软，腹无压痛、反跳痛，未触及包块，无液波震颤，肝脾肋下未触及。\n[BBOX-109] 辅助检查\n[BBOX-110] 检查日期 检查项目 结果（检查医院）\n[BBOX-111] 2023-03-30 PET/CT：1，左肺上叶高代谢占位，考虑肺癌（并累及邻近胸膜），（左侧颈部V区、左锁骨上、纵隔、左肺门10区、左肺内11-12区）多发淋巴结转移；建议病理学检查；左肺门\n[BBOX-112] 10区淋巴结旁肺组织见网格样密度增高影，轻度PDG代谢增高，建议结合临床并复查。2.双肺肺气肿；双肺少许纤维条索灶。3.副鼻窦炎（双侧上颌窦、右侧筛窦）。4.冠状动脉钙化灶。5.十二指肠圈小憩室。6.\n[BBOX-113] 肝脏囊肿。7.左肾囊肿。8.脊椎骨质增生；骶3水平椎管囊肿。（本院）\n[BBOX-114] 2023-04-03 （左锁骨上淋巴结穿刺活检）纤维组织内查见分化差的癌，结合免疫组化及病史，不除外肺非小细胞癌转移。免疫组化结果：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（-）、\n[BBOX-115] P40（灶+）。（本院）经齐鲁医院会诊：倾向肺腺癌。\n[BBOX-116] 2023-04-03 颅脑磁共振平扫+DVI+增强扫描MRI：脑内多发缺血灶，建议复查双侧上颌窦囊肿。（本院）\n[BBOX-117] 2023-04-06 胸部CT增强扫描CT：1.左肺上叶恶性肿瘤并累及邻近胸膜，左锁骨上、左肺门及纵隔多发淋巴结转移 2.双肺肺气肿；双肺少许纤维条索灶 3.冠状动脉钙化灶 4.扫及肝囊肿、左\n[BBOX-118] 肾囊肿。（本院）\n[BBOX-119] 2023-04-10 快速石蜡病理诊断：（左肺上叶穿刺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，特殊染色待补充报告。免疫组化结果：CK5/6（-）、P40（部分\n[BBOX-120] +）、TTF-1（-）、NapsinA（-）、CK7（+）。ALK（D5F3）：阴性；（免单克隆阴性对照：阴性；阳性对照：阳性）。（本院）\n[BBOX-121] 2023-04-05 基因检测：未检出与靶向治疗相关基因突变；PD-L1检测：TPS约3%。（赛泽检验）\n[BBOX-122] 2023-07-20 胸部CT：1.肺癌复查：左肺上叶占位，较前（2023-06-30）范围缩小；左锁骨上、左肺门及纵隔多发淋巴结转移，较前变化不大 2.双肺肺气肿；双肺少许纤维条索灶 3.主动脉及\n[BBOX-123] 2023-07-20\n[BBOX-124] 胸部CT：1.肺癌复查：左肺上叶占位，较前（2023-06-30）范围缩小；左锁骨上、左肺门及纵隔多发淋巴结转移，较前变化不大2.双肺肺气肿；双肺少许纤维条索灶3.主动脉及\n[BBOX-125] 冠状动脉钙化4.扫及肝囊肿胸部CT平扫，下腹部（肾）CT平扫，上腹部CT平扫，盆腔CT平扫CT（2023-08-11）：1.肺癌复查：左肺上叶占位，范围较前（2023-7-20）减小；左锁骨上、左肺门及纵隔多发稍大淋巴\n[BBOX-126] 结，较前变化不大2.双肺肺气肿；双肺少许条索灶3.主动脉及冠状动脉钙化4.肝囊肿5.左肾稍低密度灶，建议超声检查；左肾囊肿6.十二指肠降段憩室7.右侧髂骨稍高密度灶，建议复查8.考虑骶管（S3-4\n[BBOX-127] 水平）囊肿。（本院）\n[BBOX-128] 2025-03-11\n[BBOX-129] 颈部+胸部增强CT：1.肺癌复查：左肺团片影，较前25.2.6范围相仿；2.双肺微小结节，原左肺新增结节较前略小（im149薄层），转移不除外，余较前相仿，定期复查；3.双肺\n[BBOX-130] 肺气肿；双肺条索灶；4.左肺门及纵隔多发稍大淋巴结，较前相仿；5.主动脉及冠状动脉钙化；心包少量积液；左侧胸膜局限性增厚；6.扫及肝囊肿；左肾囊肿。（本院）\n[BBOX-131] 2025-09-02\n[BBOX-132] 颅脑磁共振成像+DWI（特殊序列成像）MR：考虑脑内多发小缺血灶，较前（2024-11-8）变化不著，建议复查。左侧上颌窦囊肿。（本院）\n[BBOX-133] 2025-09-03\n[BBOX-134] 颈部CT增强扫描，胸部CT增强扫描，上腹部CT增强扫描，盆腔CT增强扫描，下腹部CT增强扫描：1.肺癌复查：左肺团片影，较前2025.05.07范围略增大，建议复查2.双肺微小结节，\n[BBOX-135] 较前变化不大，转移不除外，建议定期复查3.双肺肺气肿；双肺条索灶4.左肺门及纵隔多发稍大淋巴结，较前略大5.主动脉及冠状动脉钙化；心包少量积液；左侧胸膜局限性增厚6.肝囊肿；左肾囊肿7.\n[BBOX-136] 十二指肠降段憩室8.右侧髂骨稍高密度灶，较前2024.11.06变化不大，建议复查9.考虑骶管囊肿10.颈部未见明显异常；扫及双侧上颌窦炎。（本院）\n[BBOX-137] 2025-12-27\n[BBOX-138] 颈+胸部增强CT：1.肺癌复查：左肺团片影，较前2025-09-03增大；周围新发实变及网格影，请结合临床，建议复查；2.双肺小结节及小斑片影，较前部分增大，部分新发，部分\n[BBOX-139] 变化不大，建议定期复查；3.双肺肺气肿；双肺条索灶；双肺胸膜下磨玻璃密度影，请结合临床随诊复查；4.左肺门及纵隔多发肿大淋巴结，较前部分增大；5.主动脉及冠状动脉钙化；心包少量积液；左侧胸\n[BBOX-140] 膜局限性增厚；左侧胸腔少量积液；6.扫及肝囊肿；左肾囊肿7.颈部未见明显异常；扫及双侧上颌窦炎。（本院）\n[BBOX-141] 初步诊断\n[BBOX-142] 1、左肺上叶癌腺癌cT3N3MOIIIC期\n[BBOX-143] 纵隔淋巴结转移\n[BBOX-144] 锁骨上淋巴结转移\n[BBOX-145] 肺门淋巴结转移\n[BBOX-146] 颈部淋巴结转移\n[BBOX-147] 2、肺气肿\n[BBOX-148] 3、鼻���炎\n[BBOX-149] 4、肝囊肿\n[BBOX-150] 5、肾囊肿\n[BBOX-151] 6、上颌窦囊肿\n[BBOX-152] 我审核病史记录内容属实无遗漏，我交给医院的病例资料已收回，患方签字：\n[BBOX-153] 宗茹\n[BBOX-154] 出生日期：\n[BBOX-155] 1968/12/4\n[BBOX-156] 年龄\n[BBOX-157] 57年，M\n[BBOX-158] 检查项目：\n[BBOX-159] 胸部磁共振平扫+DWI+动态增强成像\n[BBOX-160] 影像登录号：\n[BBOX-161] MR10060372\n[BBOX-162] 报告状态：\n[BBOX-163] Correction\n[BBOX-164] 原因：\n[BBOX-165] 不可选\n[BBOX-166] 主要位置：\n[BBOX-167] 2328\n[BBOX-168] 检查日期：\n[BBOX-169] 2026/3/9 7:44:30\n[BBOX-170] 顺序 #：\n[BBOX-171] MR10060372\n[BBOX-172] 影像诊断\n[BBOX-173] 左肺癌复查所见。\n[BBOX-174] 纵隔内多发淋巴结肿大。\n[BBOX-175] 肝脏、左肾多发囊肿。\n[BBOX-176] 影像表现\n[BBOX-177] 左上肺示一截面约99x61mm的团块影，呈等长T1等长T2、DWI等高信号，不均匀强化，左上肺门及纵隔与之紧密相贴。右肺未见明显异常信号影，右肺门未见明显增大。纵隔内隆凸下示多发稍大淋巴结，心影大小形态可。未见明显胸腔积液。肝脏、左肾示\n[BBOX-178] 多发囊状长T1长T2信号影，大者直径约21mm。\n[BBOX-179] 成像方法\n[BBOX-180] 年龄：57岁 住院号：5 入院日期：2026-03-04 15:35 床号：35床\n[BBOX-181] 单项 多项 全选 反选 取消\n[BBOX-182] 插入病历 插入预览\n[BBOX-183] 检查时间 项目名称\n[BBOX-184] 2026-03-10 09:49:54 快速石蜡+免疫组\n[BBOX-185] 2026-03-09 08:04:30 MR\n[BBOX-186] 2026-03-07 15:12:50 快速石蜡+免疫组\n[BBOX-187] 2026-02-02 08:40:51 核医学检查\n[BBOX-188] 2026-01-30 08:16:50 MR\n[BBOX-189] 2026-01-27 15:36:02 双下肢浅静脉彩色\n[BBOX-190] 2026-01-27 15:33:31 双下肢动脉彩色多\n[BBOX-191] 2026-01-27 13:41:19 CT\n[BBOX-192] 2026-01-26 09:27:13 CT\n[BBOX-193] 2026-01-25 15:07:01 MR\n[BBOX-194] 2026-01-24 10:22:13 十二通道\n[BBOX-195] 2025-09-03 08:09:17 CT\n[BBOX-196] 2025-09-02 19:12:41 MR\n[BBOX-197] 2024-11-08 11:13:19 MRI\n[BBOX-198] 2024-11-07 09:14:33 腋窝淋巴结彩超|\n[BBOX-199] 2024-11-07 08:08:48 核医学检查\n[BBOX-200] 2024-11-06 17:18:00 CT\n[BBOX-201] 检查项目：十二通道 检查名称：十二通道 检查部位：\n[BBOX-202] □检查所见：\n[BBOX-203] □检查结论：\n[BBOX-204] 1、窦性心动过速 2、ST段轻度改变\n[BBOX-205] 报告医 审核医生：\n[BBOX-206] \\begin{tabular}{|c|c|l|l|l|c|l|l|l|l|}\n[BBOX-207] 报告时间: 2026-03-05\n[BBOX-208] \\hline\n[BBOX-209] 采样 & 行号 & 中文名 & 项目... & 结果 & 状态 & 项目... & 参考范围 & 单位 & \\\\\n[BBOX-210] \\hline\n[BBOX-211] 26-03- & 2 & 天门冬氨酸氨基转移... & & 19 & & 10010 & 15-40 & U/L & \\\\\n[BBOX-212] \\hline\n[BBOX-213] 26-03- & 3 & AST/ALT & 肝脏... & 1.73 & & 10021 & 0.10-3.00 & & \\\\\n[BBOX-214] \\hline\n[BBOX-215] 26-03- & 4 & 总胆红素*#☆ & & 6.9 & & 10080 & ≤23.0 & um & \\\\\n[BBOX-216] \\hline\n[BBOX-217] 26-03- & 5 & 直接胆红素*#☆ & & 2.0 & & 10090 & 0-6.8 & um & \\\\\n[BBOX-218] \\hline\n[BBOX-219] & 6 & 间接胆红素 & & 4.9 & & 10100 & 3.4-17.1 & um & \\\\\n[BBOX-220] \\hline\n[BBOX-221] & 7 & 总蛋白*#☆ & 项目... & 64.1 & $\\downarrow$ & 10040 & 65.0-85.0 & g/L & \\\\\n[BBOX-222] \\hline\n[BBOX-223] & 8 & 白蛋白*#☆ & 可作... & 29.8 & $\\downarrow$ & 10050 & 40.0-55.0 & g/L & \\\\\n[BBOX-224] \\hline\n[BBOX-225] & 9 & 球蛋白 & & 34.3 & & 10060 & 20.0-40.0 & g/L & \\\\\n[BBOX-226] \\hline\n[BBOX-227] & 10 & 白球比 & & 0.87 & $\\downarrow$ & 10070 & 1.20-2.40 & & \\\\\n[BBOX-228] \\hline\n[BBOX-229] & 11 & 碱性磷酸酶*#☆ & 骨骼... & 95 & & 10110 & 45-125 & U/L & \\\\\n[BBOX-230] \\hline\n[BBOX-231] & 12 & 谷氨酸脱氢酶 & 肝脏... & 5 & & 10470 & 0-7 & U/L & \\\\\n[BBOX-232] \\hline\n[BBOX-233] & 13 & γ-谷氨酰转肽酶*#☆ & & 20 & & 10130 & 10-60 & U/L & \\\\\n[BBOX-234] \\hline\n[BBOX-235] & 14 & 胆碱酯酶*# & & 5357 & & 10020 & 5000-12000 & U/L & \\\\\n[BBOX-236] \\hline\n[BBOX-237] & 15 & 甘胆酸 & & 1.43 & & 11160 & 0.00-2.70 & ug/ & \\\\\n[BBOX-238] \\hline\n[BBOX-239] & 16 & 总胆汁酸* & & 1.40 & & 10030 & 0.00-10.00 & um & \\\\\n[BBOX-240] \\hline\n[BBOX-241] & 17 & 前白蛋白*☆ & & 100 & $\\downarrow$ & 10400 & 200-430 & mg & \\\\\n[BBOX-242] \\hline\n[BBOX-243] & 18 & 尿素*#☆ & & 1.6 & $\\downarrow$ & 10180 & 3.1-8.0 & mm & \\\\\n[BBOX-244] \\hline\n[BBOX-245] & 19 & 肌酐*#☆ & & 34.0 & $\\downarrow$ & 10190 & 57-97 & um & \\\\\n[BBOX-246] \\hline\n[BBOX-247] & 20 & 尿素/肌酐 & & 0.05 & & 10191 & 0.01-0.70 & & \\\\\n[BBOX-248] \\hline\n[BBOX-249] & 21 & 估算肾小球滤过率 & & 130 & & 10192 & & mL & \\\\\n[BBOX-250] \\hline\n[BBOX-251] & 22 & 葡萄糖*#☆ & & 7.8 & $\\uparrow$ & 10170 & 3.9-6.1 & mm & \\\\\n[BBOX-252] \\hline\n[BBOX-253] & 23 & 尿酸*#☆ & & 183 & $\\downarrow$ & 10200 & 208-428 & um & \\\\\n[BBOX-254] \\hline\n[BBOX-255] & 24 & 乳酸脱氢酶*#☆ & 心肌... & 241 & & 10120 & 120-250 & U/L & \\\\\n[BBOX-256] \\hline\n[BBOX-257] & 25 & 肌酸激酶*#☆ & 心肌... & 36 & $\\downarrow$ & 10140 & 50-310 & U/L & \\\\\n[BBOX-258] \\hline\n[BBOX-259] & 26 & 钾*#☆ & & 4.1 & & 10320 & 3.5-5.3 & mm & \\\\\n[BBOX-260] \\hline\n[BBOX-261] & 27 & 钠*#☆ & & 132 & $\\downarrow$ & 10330 & 137-147 & mm & \\\\\n[BBOX-262] \\hline\n[BBOX-263] & 28 & 氯*#☆ & & 93 & $\\downarrow$ & 10340 & 99-110 & mm & \\\\\n[BBOX-264] \\hline\n[BBOX-265] & 29 & 总二氧化碳 & TCO... & 30 & $\\uparrow$ & 10351 & 22-29 & mm & \\\\\n[BBOX-266] \\hline\n[BBOX-267] & 30 & 总钙*#☆ & & 2.28 & & 10280 & 2.11-2.52 & mm & \\\\\n[BBOX-268] \\hline\n[BBOX-269] & 31 & 磷*#☆ & & 0.97 & & 10290 & 0.85-1.51 & mm & \\\\\n[BBOX-270] \\hline\n[BBOX-271] & 32 & 镁*#☆ & & 0.69 & $\\downarrow$ & 10310 & 0.75-1.02 & mm & \\\\\n[BBOX-272] \\hline\n[BBOX-273] & 33 & 阴离子间隙 & & 9 & & 10660 & 8-16 & mm & \\\\\n[BBOX-274] \\hline\n[BBOX-275] & 34 & 渗透压 & & 264 & $\\downarrow$ & 10670 & 275-300 & mC & \\\\\n[BBOX-276] \\hline\n[BBOX-277] & 35 & α-羟丁酸脱氢酶*#☆ & & 154 & & 10160 & 72-182 & U/L & \\\\\n[BBOX-278] \\hline\n[BBOX-279] & 36 & 唾液酸 & & 1126 & $\\uparrow$ & 10560 & 456-754 & mg & \\\\\n[BBOX-280] \\hline\n[BBOX-281] & 37 & 淀粉酶*#☆ & & 28 & $\\downarrow$ & 10341 & 35-135 & U/L & \\\\\n[BBOX-282] \\hline\n[BBOX-283] & 38 & 肌酸激酶同工酶质量... & & 1.95 & & 10950 & 0-5.0 & ng/ & \\\\\n[BBOX-284] \\hline\n[BBOX-285] \\end{tabular}\n[BBOX-286] \\begin{tabular}{|c|c|l|c|c|c|l|l|}\n[BBOX-287] 报告时间: 2026-03-05\n[BBOX-288] \\hline\n[BBOX-289] \\textbf{行号} & \\textbf{中文名} & \\textbf{项目...} & \\textbf{结果} & \\textbf{状态} & \\textbf{项目...} & \\textbf{参考范围} & \\textbf{单位} \\\\\n[BBOX-290] \\hline\n[BBOX-291] 1 & 凝血酶原时间活动度 & & 84.89 & & 60110 & 70.0-130.0 & \\% \\\\\n[BBOX-292] \\hline\n[BBOX-293] 2 & 凝血酶原时间比值 & & 1.16 & $\\uparrow$ & 60120 & 0.82-1.15 & \\\\\n[BBOX-294] \\hline\n[BBOX-295] 3 & 国际标准化比值*#☆ & & 1.17 & & 60020 & 1.0-2.0;口服抗凝... & \\\\\n[BBOX-296] \\hline\n[BBOX-297] 4 & 活化部分凝血活酶时... & 是内... & 31.3 & & 60030 & 20.5-33.4 & 秒 \\\\\n[BBOX-298] \\hline\n[BBOX-299] 5 & 活化部分凝血活酶时... & 是内... & 1.18 & & 60031 & 0.77-1.25 & \\\\\n[BBOX-300] \\hline\n[BBOX-301] 6 & 纤维蛋白原*# & & 9.170 & $\\uparrow$ & 60040 & 2.00-4.00 & g/L \\\\\n[BBOX-302] \\hline\n[BBOX-303] 7 & 凝血酶时间*# & & 15.80 & & 60050 & 15.2-22.0 & 秒 \\\\\n[BBOX-304] \\hline\n[BBOX-305] 8 & D-二聚体* & 继发... & 0.55 & & 60070 & 0.00-0.56 & mg/L \\\\\n[BBOX-306] \\hline\n[BBOX-307] 9 & 抗凝血酶活性* & & 100.74 & & 60080 & 80.0-120.0 & \\% \\\\\n[BBOX-308] \\hline\n[BBOX-309] 10 & 纤维蛋白(原)降解产物* & & 3.53 & & 60130 & 0.0-5.0 & mg/L \\\\\n[BBOX-310] \\hline\n[BBOX-311] \\end{tabular}\n[BBOX-312] \\begin{tabular}{|c|l|l|c|c|l|l|l|}\n[BBOX-313] 报告时间: 2016-03-03\n[BBOX-314] \\hline\n[BBOX-315] 行号 & 中文名 & 项目... & 结果 & 状态 & 项目... & 参考范围 & 单位 \\\\\n[BBOX-316] \\hline\n[BBOX-317] 2 & 游离甲状腺素*#☆ & & 14.70 & & 1002... & 12-22 & pmol.. \\\\\n[BBOX-318] \\hline\n[BBOX-319] 3 & 促甲状腺激素*#☆ & & 1.320 & & 1002... & 0.27-4.2 & uIU/... \\\\\n[BBOX-320] \\hline\n[BBOX-321] 4 & 鳞状细胞癌相关抗原*☆ & & 0.54 & & 1009... & 0-2.5 & ng/ml \\\\\n[BBOX-322] \\hline\n[BBOX-323] 5 & 糖类抗原CA-50* & & 3.73 & & 1003... & 0-25 & IU/ml \\\\\n[BBOX-324] \\hline\n[BBOX-325] 6 & 糖类抗原CA-242* & & 0.94 & & 1003... & 0-20 & IU/ml \\\\\n[BBOX-326] \\hline\n[BBOX-327] 7 & 糖类抗原CA-724*☆ & & 0.95 & & 1003... & 0-6.0 & U/mL \\\\\n[BBOX-328] \\hline\n[BBOX-329] 8 & 癌胚抗原*#☆ & & 41.00 & $\\uparrow$ & 1001... & 0-5.09 & ng/ml \\\\\n[BBOX-330] \\hline\n[BBOX-331] 9 & 糖类抗原CA-199*# & & 9.28 & & 1003... & 0.00-27.00 & U/mL \\\\\n[BBOX-332] \\hline\n[BBOX-333] 10 & 糖类抗原CA-125*#☆ & & 21.50 & & 1003... & 0.00-35.00 & U/mL \\\\\n[BBOX-334] \\hline\n[BBOX-335] 11 & 糖类抗原CA-153*#☆ & & 15.40 & & 1003... & 0.00-26.2 & U/mL \\\\\n[BBOX-336] \\hline\n[BBOX-337] 12 & 神经元特异性烯醇化... & & 17.60 & $\\uparrow$ & 1007... & 0.00-16.30 & ng/ml \\\\\n[BBOX-338] \\hline\n[BBOX-339] 13 & 细胞角蛋白19片段*☆ & & 4.57 & $\\uparrow$ & 1007... & 0.00-3.30 & ng/ml \\\\\n[BBOX-340] \\hline\n[BBOX-341] 14 & 铁蛋白*#☆ & & 416.00 & $\\uparrow$ & 1007... & 30.00-400.00 & ng/ml \\\\\n[BBOX-342] \\hline\n[BBOX-343] 15 & β2微球蛋白*# & & 1.380 & & 1011... & 0.90-2.70 & mg/L \\\\\n[BBOX-344] \\hline\n[BBOX-345] 16 & 胃泌素释放肽前体 & & 22.100 & & 1015... & 0-68.3 & pg/ml \\\\\n[BBOX-346] \\hline\n[BBOX-347] \\end{tabular}\n[BBOX-348] \\begin{tabular}{|c|l|l|l|l|l|l|l|}\n[BBOX-349] 报告时间: 2026-3-10\n[BBOX-350] \\hline\n[BBOX-351] 行号 & 中文名 & 项目... & 结果 & 状态 & 项目... & 参考范围 & 单位 \\\\\n[BBOX-352] \\hline\n[BBOX-353] 6-03- & & & & & & & \\\\\n[BBOX-354] \\hline\n[BBOX-355] 6-03-2 & 中性粒细胞计数 & 正常... & 13.55 & $\\uparrow$ & 30070 & 1.80-6.30 & *10^... \\\\\n[BBOX-356] \\hline\n[BBOX-357] 6-03-3 & 淋巴细胞计数 & 正常... & 1.86 & & 30050 & 1.10-3.20 & *10^... \\\\\n[BBOX-358] \\hline\n[BBOX-359] 5-03-4 & 单核细胞计数 & 正常... & 1.32 & $\\uparrow$ & 30060 & 0.10-0.60 & *10^... \\\\\n[BBOX-360] \\hline\n[BBOX-361] 5-03-5 & 嗜酸细胞计数 & & 0.00 & $\\downarrow$ & 30210 & 0.02-0.52 & *10^... \\\\\n[BBOX-362] \\hline\n[BBOX-363] 6 & 嗜碱细胞计数 & & 0.07 & $\\uparrow$ & 30220 & 0.00-0.06 & *10^... \\\\\n[BBOX-364] \\hline\n[BBOX-365] 7 & 中性粒细胞百分比 & 正常... & 80.6 & $\\uparrow$ & 30040 & 40.0-75.0 & \\% \\\\\n[BBOX-366] \\hline\n[BBOX-367] 8 & 淋巴细胞百分比 & 正常... & 11.1 & $\\downarrow$ & 30020 & 20.0-50.0 & \\% \\\\\n[BBOX-368] \\hline\n[BBOX-369] 9 & 单核细胞百分比 & 正常... & 7.9 & & 30030 & 3.0-10.0 & \\% \\\\\n[BBOX-370] \\hline\n[BBOX-371] 10 & 嗜酸细胞百分比 & 参考... & 0.0 & $\\downarrow$ & 30190 & 0.40-8.00 & \\% \\\\\n[BBOX-372] \\hline\n[BBOX-373] 11 & 嗜碱细胞百分比 & & 0.4 & & 30200 & 0.00-1.00 & \\% \\\\\n[BBOX-374] \\hline\n[BBOX-375] 12 & 红细胞计数*#☆ & 参考... & 3.69 & $\\downarrow$ & 30080 & 4.30-5.80 & *10^... \\\\\n[BBOX-376] \\hline\n[BBOX-377] 13 & 血红蛋白含量*#☆ & 正常... & 102 & $\\downarrow$ & 30090 & 130-175 & g/L \\\\\n[BBOX-378] \\hline\n[BBOX-379] 14 & 红细胞比容*#☆ & 正常... & 0.32 & $\\downarrow$ & 30100 & 0.40-0.50 & L/L \\\\\n[BBOX-380] \\hline\n[BBOX-381] 15 & 平均红细胞血红蛋白... & 正常... & 27.6 & & 30120 & 27.0-34.0 & pg \\\\\n[BBOX-382] \\hline\n[BBOX-383] 16 & 平均红细胞血红蛋白... & 正常... & 318 & & 30130 & 316-354 & g/L \\\\\n[BBOX-384] \\hline\n[BBOX-385] 17 & 平均红细胞体积*#☆ & 正常... & 87.0 & & 30110 & 82.0-100.0 & fL \\\\\n[BBOX-386] \\hline\n[BBOX-387] 18 & 红细胞分布宽度（CV） & 正常... & 17.3 & $\\uparrow$ & 30140 & 11.6-16.5 & \\% \\\\\n[BBOX-388] \\hline\n[BBOX-389] 19 & 红细胞分布宽度（SD） & & 54.6 & $\\uparrow$ & 30230 & 37.0-54.0 & fL \\\\\n[BBOX-390] \\hline\n[BBOX-391] 20 & 血小板计数*#☆ & 参考... & 466 & $\\uparrow$ & 30150 & 125-350 & *10^... \\\\\n[BBOX-392] \\hline\n[BBOX-393] 21 & 平均血小板体积 & 正常... & 8.8 & & 30160 & 7.4-11.0 & fL \\\\\n[BBOX-394] \\hline\n[BBOX-395] 22 & 大血小板比率 & 正常... & 15.7 & & 30170 & 13.0-43.0 & \\% \\\\\n[BBOX-396] \\hline\n[BBOX-397] 23 & 血小板比容 & & 0.41 & $\\uparrow$ & 30240 & 0.170-0.350 & \\% \\\\\n[BBOX-398] \\hline\n[BBOX-399] 24 & 血小板分布宽度 & 正常... & 8.5 & $\\downarrow$ & 30180 & 9.6-15.2 & fL \\\\\n[BBOX-400] \\hline\n[BBOX-401] 25 & C-反应蛋白* & & 177.... & $\\uparrow$ & 30340 & 0.000-5.000 & mg/L \\\\\n[BBOX-402] \\hline\n[BBOX-403] \\end{tabular}\n[BBOX-404] 20230403穿刺病理确诊肺鳞癌\n[BBOX-405] 20230407~20230630替雷+贝伐+卡铂+培美5周期\n[BBOX-406] 20230706放疗，结束时间20230809\n[BBOX-407] 20230719卡铂+恩度+替雷\n[BBOX-408] 20230810恩度+替雷\n[BBOX-409] 20240930顺铂+贝伐+替雷\n[BBOX-410] 202411进展\n[BBOX-411] 20241107、20241203、20250116、20250206、20250325贝伐+替雷+顺铂+紫\n[BBOX-412] 衫\n[BBOX-413] 20250415贝伐+替雷+卡铂+紫衫\n[BBOX-414] 20250507顺铂+紫衫\n[BBOX-415] 20250728~202512贝伐+替雷+卡铂+紫衫\n[BBOX-416] 20260119卡铂+紫衫"
  }
]
2026-08-10 18:05:40,753 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:05:40.752+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 84, "failed": 0, "current": {"d64c79b494e511f1bd9827cf206dfa2d": {"id": "d64c79b494e511f1bd9827cf206dfa2d", "doc_id": "d60771c094e511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 5825068, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385028897, "task_type": "dataflow", "root_trace_id": "93629fbf7f764cf397a9e7f896dd05c6", "root_traceparent": "00-93629fbf7f764cf397a9e7f896dd05c6-e7dded3dfece48a2-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:05:54,537 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:05:54,556 INFO     29 [SmartSplitter] SmartSplitter done: 10 chunks from 10 LLM segments (all bbox_id). Types: {'ExaminationReport': 5, 'AdmissionRecord': 1, 'LabReport': 4}
2026-08-10 18:05:54,565 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 18:05:54,565 INFO     29 [Trace] task=d64c79b4 | doc=07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "417 items", "markdown": "", "text": "", "name": "07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks": "10 items, types={'ExaminationReport': 5, 'AdmissionRecord': 1, 'LabReport': 4}"}
2026-08-10 18:05:54,565 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 18:05:54,566 INFO     29 [ChunkRouter] Routed 10 chunks into 3 groups: {'chunks_Examination': 5, 'chunks_Admission': 1, 'chunks_LabExam': 4}
2026-08-10 18:05:54,573 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 18:05:54,573 INFO     29 [Trace] task=d64c79b4 | doc=07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf | ChunkRouter:Router | outputs={"html": "", "json": "417 items", "markdown": "", "text": "", "name": "07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks": "10 items, types={'ExaminationReport': 5, 'AdmissionRecord': 1, 'LabReport': 4}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Admission\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 18:05:54,573 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 18:05:54,578 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:05:54,578 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:05:54,579 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[8]
2026-08-10 18:05:54,579 INFO     29 [qwen-vl-table] positions ： [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:05:54,913 INFO     29 [qwen-vl-table] page=8, rect=595x842, img=(1653x2339)
2026-08-10 18:05:54,914 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:05:54,915 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 206, \"bbox_end\": 285, \"encounter_dates\": [\"2026-03-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{|c|c|l|l|l|c|l|l|l|l|}\n报告时间: 2026-03-05\n\\hline\n采样 & 行号 & 中文名 & 项目... & 结果 & 状态 & 项目... & 参考范围 & 单位 & \\\\\n\\hline\n26-03- & 2 & 天门冬氨酸氨基转移... & & 19 & & 10010 & 15-40 & U/L & \\\\\n\\hline\n26-03- & 3 & AST/ALT & 肝脏... & 1.73 & & 10021 & 0.10-3.00 & & \\\\\n\\hline\n26-03- & 4 & 总胆红素*#☆ & & 6.9 & & 10080 & ≤23.0 & um & \\\\\n\\hline\n26-03- & 5 & 直接胆红素*#☆ & & 2.0 & & 10090 & 0-6.8 & um & \\\\\n\\hline\n& 6 & 间接胆红素 & & 4.9 & & 10100 & 3.4-17.1 & um & \\\\\n\\hline\n& 7 & 总蛋白*#☆ & 项目... & 64.1 & $\\downarrow$ & 10040 & 65.0-85.0 & g/L & \\\\\n\\hline\n& 8 & 白蛋白*#☆ & 可作... & 29.8 & $\\downarrow$ & 10050 & 40.0-55.0 & g/L & \\\\\n\\hline\n& 9 & 球蛋白 & & 34.3 & & 10060 & 20.0-40.0 & g/L & \\\\\n\\hline\n& 10 & 白球比 & & 0.87 & $\\downarrow$ & 10070 & 1.20-2.40 & & \\\\\n\\hline\n& 11 & 碱性磷酸酶*#☆ & 骨骼... & 95 & & 10110 & 45-125 & U/L & \\\\\n\\hline\n& 12 & 谷氨酸脱氢酶 & 肝脏... & 5 & & 10470 & 0-7 & U/L & \\\\\n\\hline\n& 13 & γ-谷氨酰转肽酶*#☆ & & 20 & & 10130 & 10-60 & U/L & \\\\\n\\hline\n& 14 & 胆碱酯酶*# & & 5357 & & 10020 & 5000-12000 & U/L & \\\\\n\\hline\n& 15 & 甘胆酸 & & 1.43 & & 11160 & 0.00-2.70 & ug/ & \\\\\n\\hline\n& 16 & 总胆汁酸* & & 1.40 & & 10030 & 0.00-10.00 & um & \\\\\n\\hline\n& 17 & 前白蛋白*☆ & & 100 & $\\downarrow$ & 10400 & 200-430 & mg & \\\\\n\\hline\n& 18 & 尿素*#☆ & & 1.6 & $\\downarrow$ & 10180 & 3.1-8.0 & mm & \\\\\n\\hline\n& 19 & 肌酐*#☆ & & 34.0 & $\\downarrow$ & 10190 & 57-97 & um & \\\\\n\\hline\n& 20 & 尿素/肌酐 & & 0.05 & & 10191 & 0.01-0.70 & & \\\\\n\\hline\n& 21 & 估算肾小球滤过率 & & 130 & & 10192 & & mL & \\\\\n\\hline\n& 22 & 葡萄糖*#☆ & & 7.8 & $\\uparrow$ & 10170 & 3.9-6.1 & mm & \\\\\n\\hline\n& 23 & 尿酸*#☆ & & 183 & $\\downarrow$ & 10200 & 208-428 & um & \\\\\n\\hline\n& 24 & 乳酸脱氢酶*#☆ & 心肌... & 241 & & 10120 & 120-250 & U/L & \\\\\n\\hline\n& 25 & 肌酸激酶*#☆ & 心肌... & 36 & $\\downarrow$ & 10140 & 50-310 & U/L & \\\\\n\\hline\n& 26 & 钾*#☆ & & 4.1 & & 10320 & 3.5-5.3 & mm & \\\\\n\\hline\n& 27 & 钠*#☆ & & 132 & $\\downarrow$ & 10330 & 137-147 & mm & \\\\\n\\hline\n& 28 & 氯*#☆ & & 93 & $\\downarrow$ & 10340 & 99-110 & mm & \\\\\n\\hline\n& 29 & 总二氧化碳 & TCO... & 30 & $\\uparrow$ & 10351 & 22-29 & mm & \\\\\n\\hline\n& 30 & 总钙*#☆ & & 2.28 & & 10280 & 2.11-2.52 & mm & \\\\\n\\hline\n& 31 & 磷*#☆ & & 0.97 & & 10290 & 0.85-1.51 & mm & \\\\\n\\hline\n& 32 & 镁*#☆ & & 0.69 & $\\downarrow$ & 10310 & 0.75-1.02 & mm & \\\\\n\\hline\n& 33 & 阴离子间隙 & & 9 & & 10660 & 8-16 & mm & \\\\\n\\hline\n& 34 & 渗透压 & & 264 & $\\downarrow$ & 10670 & 275-300 & mC & \\\\\n\\hline\n& 35 & α-羟丁酸脱氢酶*#☆ & & 154 & & 10160 & 72-182 & U/L & \\\\\n\\hline\n& 36 & 唾液酸 & & 1126 & $\\uparrow$ & 10560 & 456-754 & mg & \\\\\n\\hline\n& 37 & 淀粉酶*#☆ & & 28 & $\\downarrow$ & 10341 & 35-135 & U/L & \\\\\n\\hline\n& 38 & 肌酸激酶同工酶质量... & & 1.95 & & 10950 & 0-5.0 & ng/ & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 18:06:12,840 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:06:12.837+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 84, "failed": 0, "current": {"d64c79b494e511f1bd9827cf206dfa2d": {"id": "d64c79b494e511f1bd9827cf206dfa2d", "doc_id": "d60771c094e511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 5825068, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385028897, "task_type": "dataflow", "root_trace_id": "93629fbf7f764cf397a9e7f896dd05c6", "root_traceparent": "00-93629fbf7f764cf397a9e7f896dd05c6-e7dded3dfece48a2-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:06:13,851 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:06:13,852 INFO     29 [qwen-vl-table] page=8 LLM output (len=6046):
{
  "report_date": "2026-03-05",
  "items": [
    {
      "name": "天门冬氨酸氨基转移酶",
      "item_code": null,
      "value": "19",
      "unit": "U/L",
      "reference_range": "15-40",
      "abnormal": false
    },
    {
      "name": "AST/ALT",
      "item_code": null,
      "value": "1.73",
      "unit": null,
      "reference_range": "0.10-3.00",
      "abnormal": false
    },
    {
      "name": "总胆红素",
      "item_code": null,
      "value": "6.9",
      "unit": "um",
      "reference_range": "≤23.0",
      "abnormal": false
    },
    {
      "name": "直接胆红素",
      "item_code": null,
      "value": "2.0",
      "unit": "um",
      "reference_range": "0-6.8",
      "abnormal": false
    },
    {
      "name": "间接胆红素",
      "item_code": null,
      "value": "4.9",
      "unit": "um",
      "reference_range": "3.4-17.1",
      "abnormal": false
    },
    {
      "name": "总蛋白",
      "item_code": null,
      "value": "64.1",
      "unit": "g/L",
      "reference_range": "65.0-85.0",
      "abnormal": true
    },
    {
      "name": "白蛋白",
      "item_code": null,
      "value": "29.8",
      "unit": "g/L",
      "reference_range": "40.0-55.0",
      "abnormal": true
    },
    {
      "name": "球蛋白",
      "item_code": null,
      "value": "34.3",
      "unit": "g/L",
      "reference_range": "20.0-40.0",
      "abnormal": false
    },
    {
      "name": "白球比",
      "item_code": null,
      "value": "0.87",
      "unit": null,
      "reference_range": "1.20-2.40",
      "abnormal": true
    },
    {
      "name": "碱性磷酸酶",
      "item_code": null,
      "value": "95",
      "unit": "U/L",
      "reference_range": "45-125",
      "abnormal": false
    },
    {
      "name": "谷氨酸脱氢酶",
      "item_code": null,
      "value": "5",
      "unit": "U/L",
      "reference_range": "0-7",
      "abnormal": false
    },
    {
      "name": "γ-谷氨酰转肽酶",
      "item_code": null,
      "value": "20",
      "unit": "U/L",
      "reference_range": "10-60",
      "abnormal": false
    },
    {
      "name": "胆碱酯酶",
      "item_code": null,
      "value": "5357",
      "unit": "U/L",
      "reference_range": "5000-12000",
      "abnormal": false
    },
    {
      "name": "甘胆酸",
      "item_code": null,
      "value": "1.43",
      "unit": "ug/",
      "reference_range": "0.00-2.70",
      "abnormal": false
    },
    {
      "name": "总胆汁酸",
      "item_code": null,
      "value": "1.40",
      "unit": "um",
      "reference_range": "0.00-10.00",
      "abnormal": false
    },
    {
      "name": "前白蛋白",
      "item_code": null,
      "value": "100",
      "unit": "mg",
      "reference_range": "200-430",
      "abnormal": true
    },
    {
      "name": "尿素",
      "item_code": null,
      "value": "1.6",
      "unit": "mm",
      "reference_range": "3.1-8.0",
      "abnormal": true
    },
    {
      "name": "肌酐",
      "item_code": null,
      "value": "34.0",
      "unit": "um",
      "reference_range": "57-97",
      "abnormal": true
    },
    {
      "name": "尿素/肌酐",
      "item_code": null,
      "value": "0.05",
      "unit": null,
      "reference_range": "0.01-0.70",
      "abnormal": false
    },
    {
      "name": "估算肾小球滤过率",
      "item_code": null,
      "value": "130",
      "unit": "mL",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "葡萄糖",
      "item_code": null,
      "value": "7.8",
      "unit": "mm",
      "reference_range": "3.9-6.1",
      "abnormal": true
    },
    {
      "name": "尿酸",
      "item_code": null,
      "value": "183",
      "unit": "um",
      "reference_range": "208-428",
      "abnormal": true
    },
    {
      "name": "乳酸脱氢酶",
      "item_code": null,
      "value": "241",
      "unit": "U/L",
      "reference_range": "120-250",
      "abnormal": false
    },
    {
      "name": "肌酸激酶",
      "item_code": null,
      "value": "36",
      "unit": "U/L",
      "reference_range": "50-310",
      "abnormal": true
    },
    {
      "name": "钾",
      "item_code": null,
      "value": "4.1",
      "unit": "mm",
      "reference_range": "3.5-5.3",
      "abnormal": false
    },
    {
      "name": "钠",
      "item_code": null,
      "value": "132",
      "unit": "mm",
      "reference_range": "137-147",
      "abnormal": true
    },
    {
      "name": "氯",
      "item_code": null,
      "value": "93",
      "unit": "mm",
      "reference_range": "99-110",
      "abnormal": true
    },
    {
      "name": "总二氧化碳",
      "item_code": "TCO",
      "value": "30",
      "unit": "mm",
      "reference_range": "22-29",
      "abnormal": true
    },
    {
      "name": "总钙",
      "item_code": null,
      "value": "2.28",
      "unit": "mm",
      "reference_range": "2.11-2.52",
      "abnormal": false
    },
    {
      "name": "磷",
      "item_code": null,
      "value": "0.97",
      "unit": "mm",
      "reference_range": "0.85-1.51",
      "abnormal": false
    },
    {
      "name": "镁",
      "item_code": null,
      "value": "0.69",
      "unit": "mm",
      "reference_range": "0.75-1.02",
      "abnormal": true
    },
    {
      "name": "阴离子间隙",
      "item_code": null,
      "value": "9",
      "unit": "mm",
      "reference_range": "8-16",
      "abnormal": false
    },
    {
      "name": "渗透压",
      "item_code": null,
      "value": "264",
      "unit": "mC",
      "reference_range": "275-300",
      "abnormal": true
    },
    {
      "name": "α-羟丁酸脱氢酶",
      "item_code": null,
      "value": "154",
      "unit": "U/L",
      "reference_range": "72-182",
      "abnormal": false
    },
    {
      "name": "唾液酸",
      "item_code": null,
      "value": "1126",
      "unit": "mg",
      "reference_range": "456-754",
      "abnormal": true
    },
    {
      "name": "淀粉酶",
      "item_code": null,
      "value": "28",
      "unit": "U/L",
      "reference_range": "35-135",
      "abnormal": true
    },
    {
      "name": "肌酸激酶同工酶质量",
      "item_code": null,
      "value": "1.95",
      "unit": "ng/",
      "reference_range": "0-5.0",
      "abnormal": false
    }
  ]
}
2026-08-10 18:06:13,852 INFO     29 [qwen-vl-table] coord grouping: {8: 37}
2026-08-10 18:06:13,862 INFO     29 [qwen-vl-table] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3311927, prompt_len=694
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
天门冬氨酸氨基转移酶、AST/ALT、总胆红素、直接胆红素、间接胆红素、总蛋白、白蛋白、球蛋白、白球比、碱性磷酸酶、谷氨酸脱氢酶、γ-谷氨酰转肽酶、胆碱酯酶、甘胆酸、总胆汁酸、前白蛋白、尿素、肌酐、尿素/肌酐、估算肾小球滤过率、葡萄糖、尿酸、乳酸脱氢酶、肌酸激酶、钾、钠、氯、总二氧化碳、总钙、磷、镁、阴离子间隙、渗透压、α-羟丁酸脱氢酶、唾液酸、淀粉酶、肌酸激酶同工酶质量

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
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord API raw response (len=1815):
[
	{"text": "天门冬氨酸氨基转移酶", "bbox": [148, 70, 324, 88]},
	{"text": "AST/ALT", "bbox": [148, 95, 222, 110]},
	{"text": "总胆红素", "bbox": [148, 117, 255, 132]},
	{"text": "直接胆红素", "bbox": [148, 140, 272, 155]},
	{"text": "间接胆红素", "bbox": [148, 162, 239, 177]},
	{"text": "总蛋白", "bbox": [148, 185, 237, 199]},
	{"text": "白蛋白", "bbox": [148, 207, 237, 222]},
	{"text": "球蛋白", "bbox": [148, 230, 202, 245]},
	{"text": "白球比", "bbox": [148, 252, 202, 267]},
	{"text": "碱性磷酸酶", "bbox": [148, 275, 272, 290]},
	{"text": "谷氨酸脱氢酶", "bbox": [148, 298, 255, 313]},
	{"text": "γ-谷氨酰转肽酶", "bbox": [148, 321, 308, 336]},
	{"text": "胆碱酯酶", "bbox": [148, 344, 239, 358]},
	{"text": "甘胆酸", "bbox": [148, 366, 202, 381]},
	{"text": "总胆汁酸", "bbox": [148, 389, 227, 404]},
	{"text": "前白蛋白", "bbox": [148, 411, 243, 426]},
	{"text": "尿素", "bbox": [148, 434, 218, 449]},
	{"text": "肌酐", "bbox": [148, 457, 218, 471]},
	{"text": "尿素/肌酐", "bbox": [148, 479, 227, 494]},
	{"text": "估算肾小球滤过率", "bbox": [148, 502, 291, 517]},
	{"text": "葡萄糖", "bbox": [148, 524, 237, 539]},
	{"text": "尿酸", "bbox": [148, 547, 218, 562]},
	{"text": "乳酸脱氢酶", "bbox": [148, 570, 272, 585]},
	{"text": "肌酸激酶", "bbox": [148, 592, 255, 607]},
	{"text": "钾", "bbox": [148, 615, 202, 630]},
	{"text": "钠", "bbox": [148, 638, 202, 653]},
	{"text": "氯", "bbox": [148, 660, 202, 675]},
	{"text": "总二氧化碳", "bbox": [148, 683, 239, 698]},
	{"text": "总钙", "bbox": [148, 706, 218, 720]},
	{"text": "磷", "bbox": [148, 728, 202, 743]},
	{"text": "镁", "bbox": [148, 751, 202, 766]},
	{"text": "阴离子间隙", "bbox": [148, 773, 239, 788]},
	{"text": "渗透压", "bbox": [148, 796, 202, 811]},
	{"text": "α-羟丁酸脱氢酶", "bbox": [148, 818, 310, 833]},
	{"text": "唾液酸", "bbox": [148, 841, 202, 856]},
	{"text": "淀粉酶", "bbox": [148, 863, 237, 878]},
	{"text": "肌酸激酶同工酶质量", "bbox": [148, 886, 322, 901]}
]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord API: raw_items=37, valid_items=37, elapsed=11.9s
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[0]: text=天门冬氨酸氨基转移酶, bbox=[148, 70, 324, 88]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[1]: text=AST/ALT, bbox=[148, 95, 222, 110]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[2]: text=总胆红素, bbox=[148, 117, 255, 132]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[3]: text=直接胆红素, bbox=[148, 140, 272, 155]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[4]: text=间接胆红素, bbox=[148, 162, 239, 177]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[5]: text=总蛋白, bbox=[148, 185, 237, 199]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[6]: text=白蛋白, bbox=[148, 207, 237, 222]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[7]: text=球蛋白, bbox=[148, 230, 202, 245]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[8]: text=白球比, bbox=[148, 252, 202, 267]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[9]: text=碱性磷酸酶, bbox=[148, 275, 272, 290]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[10]: text=谷氨酸脱氢酶, bbox=[148, 298, 255, 313]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[11]: text=γ-谷氨酰转肽酶, bbox=[148, 321, 308, 336]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[12]: text=胆碱酯酶, bbox=[148, 344, 239, 358]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[13]: text=甘胆酸, bbox=[148, 366, 202, 381]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[14]: text=总胆汁酸, bbox=[148, 389, 227, 404]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[15]: text=前白蛋白, bbox=[148, 411, 243, 426]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[16]: text=尿素, bbox=[148, 434, 218, 449]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[17]: text=肌酐, bbox=[148, 457, 218, 471]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[18]: text=尿素/肌酐, bbox=[148, 479, 227, 494]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[19]: text=估算肾小球滤过率, bbox=[148, 502, 291, 517]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[20]: text=葡萄糖, bbox=[148, 524, 237, 539]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[21]: text=尿酸, bbox=[148, 547, 218, 562]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[22]: text=乳酸脱氢酶, bbox=[148, 570, 272, 585]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[23]: text=肌酸激酶, bbox=[148, 592, 255, 607]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[24]: text=钾, bbox=[148, 615, 202, 630]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[25]: text=钠, bbox=[148, 638, 202, 653]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[26]: text=氯, bbox=[148, 660, 202, 675]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[27]: text=总二氧化碳, bbox=[148, 683, 239, 698]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[28]: text=总钙, bbox=[148, 706, 218, 720]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[29]: text=磷, bbox=[148, 728, 202, 743]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[30]: text=镁, bbox=[148, 751, 202, 766]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[31]: text=阴离子间隙, bbox=[148, 773, 239, 788]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[32]: text=渗透压, bbox=[148, 796, 202, 811]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[33]: text=α-羟丁酸脱氢酶, bbox=[148, 818, 310, 833]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[34]: text=唾液酸, bbox=[148, 841, 202, 856]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[35]: text=淀粉酶, bbox=[148, 863, 237, 878]
2026-08-10 18:06:25,742 INFO     29 [qwen-vl-table] coord item[36]: text=肌酸激酶同工酶质量, bbox=[148, 886, 322, 901]
2026-08-10 18:06:25,743 INFO     29 [qwen-vl-table] page=8 coord: matched 37/37, time=11.9s
2026-08-10 18:06:25,743 INFO     29 [qwen-vl-table] new_positions (37):
[[9, 88.06, 192.78, 58.94, 74.096], [9, 88.06, 132.09, 79.99, 92.61999999999999], [9, 88.06, 151.725, 98.514, 111.14399999999999], [9, 88.06, 161.84, 117.88, 130.51], [9, 88.06, 142.20499999999998, 136.404, 149.034], [9, 88.06, 141.015, 155.76999999999998, 167.558], [9, 88.06, 141.015, 174.29399999999998, 186.924], [9, 88.06, 120.19, 193.66, 206.29], [9, 88.06, 120.19, 212.184, 224.814], [9, 88.06, 161.84, 231.54999999999998, 244.17999999999998], [9, 88.06, 151.725, 250.916, 263.546], [9, 88.06, 183.26, 270.282, 282.912], [9, 88.06, 142.20499999999998, 289.64799999999997, 301.436], [9, 88.06, 120.19, 308.17199999999997, 320.80199999999996], [9, 88.06, 135.065, 327.538, 340.168], [9, 88.06, 144.58499999999998, 346.062, 358.692], [9, 88.06, 129.71, 365.428, 378.058], [9, 88.06, 129.71, 384.794, 396.582], [9, 88.06, 135.065, 403.318, 415.948], [9, 88.06, 173.14499999999998, 422.68399999999997, 435.31399999999996], [9, 88.06, 141.015, 441.20799999999997, 453.83799999999997], [9, 88.06, 129.71, 460.574, 473.204], [9, 88.06, 161.84, 479.94, 492.57], [9, 88.06, 151.725, 498.464, 511.094], [9, 88.06, 120.19, 517.8299999999999, 530.46], [9, 88.06, 120.19, 537.196, 549.826], [9, 88.06, 120.19, 555.72, 568.35], [9, 88.06, 142.20499999999998, 575.086, 587.716], [9, 88.06, 129.71, 594.452, 606.24], [9, 88.06, 120.19, 612.976, 625.606], [9, 88.06, 120.19, 632.342, 644.972], [9, 88.06, 142.20499999999998, 650.866, 663.496], [9, 88.06, 120.19, 670.232, 682.862], [9, 88.06, 184.45, 688.756, 701.386], [9, 88.06, 120.19, 708.122, 720.752], [9, 88.06, 141.015, 726.646, 739.276], [9, 88.06, 191.59, 746.012, 758.6419999999999]]
2026-08-10 18:06:25,743 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=37, matched=37, pages=1, time=31.2s
2026-08-10 18:06:25,744 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:06:25,745 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:06:25,745 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[9]
2026-08-10 18:06:25,745 INFO     29 [qwen-vl-table] positions ： [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:06:25,948 INFO     29 [qwen-vl-table] page=9, rect=595x842, img=(1653x2339)
2026-08-10 18:06:25,948 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:06:25,949 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 286, \"bbox_end\": 311, \"encounter_dates\": [\"2026-03-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{|c|c|l|c|c|c|l|l|}\n报告时间: 2026-03-05\n\\hline\n\\textbf{行号} & \\textbf{中文名} & \\textbf{项目...} & \\textbf{结果} & \\textbf{状态} & \\textbf{项目...} & \\textbf{参考范围} & \\textbf{单位} \\\\\n\\hline\n1 & 凝血酶原时间活动度 & & 84.89 & & 60110 & 70.0-130.0 & \\% \\\\\n\\hline\n2 & 凝血酶原时间比值 & & 1.16 & $\\uparrow$ & 60120 & 0.82-1.15 & \\\\\n\\hline\n3 & 国际标准化比值*#☆ & & 1.17 & & 60020 & 1.0-2.0;口服抗凝... & \\\\\n\\hline\n4 & 活化部分凝血活酶时... & 是内... & 31.3 & & 60030 & 20.5-33.4 & 秒 \\\\\n\\hline\n5 & 活化部分凝血活酶时... & 是内... & 1.18 & & 60031 & 0.77-1.25 & \\\\\n\\hline\n6 & 纤维蛋白原*# & & 9.170 & $\\uparrow$ & 60040 & 2.00-4.00 & g/L \\\\\n\\hline\n7 & 凝血酶时间*# & & 15.80 & & 60050 & 15.2-22.0 & 秒 \\\\\n\\hline\n8 & D-二聚体* & 继发... & 0.55 & & 60070 & 0.00-0.56 & mg/L \\\\\n\\hline\n9 & 抗凝血酶活性* & & 100.74 & & 60080 & 80.0-120.0 & \\% \\\\\n\\hline\n10 & 纤维蛋白(原)降解产物* & & 3.53 & & 60130 & 0.0-5.0 & mg/L \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 18:06:32,580 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:06:32,580 INFO     29 [qwen-vl-table] page=9 LLM output (len=1778):
{
  "report_date": "2026-03-05",
  "items": [
    {
      "name": "凝血酶原时间活动度",
      "item_code": "60110",
      "value": "84.89",
      "unit": "%",
      "reference_range": "70.0-130.0",
      "abnormal": false
    },
    {
      "name": "凝血酶原时间比值",
      "item_code": "60120",
      "value": "1.16",
      "unit": null,
      "reference_range": "0.82-1.15",
      "abnormal": true
    },
    {
      "name": "国际标准化比值",
      "item_code": "60020",
      "value": "1.17",
      "unit": null,
      "reference_range": "1.0-2.0;口服抗凝...",
      "abnormal": false
    },
    {
      "name": "活化部分凝血活酶时间",
      "item_code": "60030",
      "value": "31.3",
      "unit": "秒",
      "reference_range": "20.5-33.4",
      "abnormal": false
    },
    {
      "name": "活化部分凝血活酶时间比值",
      "item_code": "60031",
      "value": "1.18",
      "unit": null,
      "reference_range": "0.77-1.25",
      "abnormal": false
    },
    {
      "name": "纤维蛋白原",
      "item_code": "60040",
      "value": "9.170",
      "unit": "g/L",
      "reference_range": "2.00-4.00",
      "abnormal": true
    },
    {
      "name": "凝血酶时间",
      "item_code": "60050",
      "value": "15.80",
      "unit": "秒",
      "reference_range": "15.2-22.0",
      "abnormal": false
    },
    {
      "name": "D-二聚体",
      "item_code": "60070",
      "value": "0.55",
      "unit": "mg/L",
      "reference_range": "0.00-0.56",
      "abnormal": false
    },
    {
      "name": "抗凝血酶活性",
      "item_code": "60080",
      "value": "100.74",
      "unit": "%",
      "reference_range": "80.0-120.0",
      "abnormal": false
    },
    {
      "name": "纤维蛋白(原)降解产物",
      "item_code": "60130",
      "value": "3.53",
      "unit": "mg/L",
      "reference_range": "0.0-5.0",
      "abnormal": false
    }
  ]
}
2026-08-10 18:06:32,580 INFO     29 [qwen-vl-table] coord grouping: {9: 10}
2026-08-10 18:06:32,586 INFO     29 [qwen-vl-table] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1965013, prompt_len=594
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
凝血酶原时间活动度、凝血酶原时间比值、国际标准化比值、活化部分凝血活酶时间、活化部分凝血活酶时间比值、纤维蛋白原、凝血酶时间、D-二聚体、抗凝血酶活性、纤维蛋白(原)降解产物

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
2026-08-10 18:06:36,230 INFO     29 [qwen-vl-table] coord API raw response (len=530):
[
	{"text": "凝血酶原时间活动度", "bbox": [164, 116, 325, 132]},
	{"text": "凝血酶原时间比值", "bbox": [164, 140, 308, 155]},
	{"text": "国际标准化比值", "bbox": [164, 162, 324, 177]},
	{"text": "活化部分凝血活酶时间", "bbox": [164, 185, 338, 199]},
	{"text": "活化部分凝血活酶时间比值", "bbox": [164, 207, 338, 222]},
	{"text": "纤维蛋白原", "bbox": [164, 230, 274, 245]},
	{"text": "凝血酶时间", "bbox": [164, 252, 274, 267]},
	{"text": "D-二聚体", "bbox": [164, 275, 249, 289]},
	{"text": "抗凝血酶活性", "bbox": [164, 298, 280, 312]},
	{"text": "纤维蛋白(原)降解产物", "bbox": [164, 320, 344, 335]}
]
2026-08-10 18:06:36,230 INFO     29 [qwen-vl-table] coord API: raw_items=10, valid_items=10, elapsed=3.6s
2026-08-10 18:06:36,231 INFO     29 [qwen-vl-table] coord item[0]: text=凝血酶原时间活动度, bbox=[164, 116, 325, 132]
2026-08-10 18:06:36,231 INFO     29 [qwen-vl-table] coord item[1]: text=凝血酶原时间比值, bbox=[164, 140, 308, 155]
2026-08-10 18:06:36,231 INFO     29 [qwen-vl-table] coord item[2]: text=国际标准化比值, bbox=[164, 162, 324, 177]
2026-08-10 18:06:36,231 INFO     29 [qwen-vl-table] coord item[3]: text=活化部分凝血活酶时间, bbox=[164, 185, 338, 199]
2026-08-10 18:06:36,231 INFO     29 [qwen-vl-table] coord item[4]: text=活化部分凝血活酶时间比值, bbox=[164, 207, 338, 222]
2026-08-10 18:06:36,231 INFO     29 [qwen-vl-table] coord item[5]: text=纤维蛋白原, bbox=[164, 230, 274, 245]
2026-08-10 18:06:36,231 INFO     29 [qwen-vl-table] coord item[6]: text=凝血酶时间, bbox=[164, 252, 274, 267]
2026-08-10 18:06:36,231 INFO     29 [qwen-vl-table] coord item[7]: text=D-二聚体, bbox=[164, 275, 249, 289]
2026-08-10 18:06:36,231 INFO     29 [qwen-vl-table] coord item[8]: text=抗凝血酶活性, bbox=[164, 298, 280, 312]
2026-08-10 18:06:36,231 INFO     29 [qwen-vl-table] coord item[9]: text=纤维蛋白(原)降解产物, bbox=[164, 320, 344, 335]
2026-08-10 18:06:36,231 INFO     29 [qwen-vl-table] page=9 coord: matched 10/10, time=3.6s
2026-08-10 18:06:36,231 INFO     29 [qwen-vl-table] new_positions (10):
[[10, 97.58, 193.375, 97.672, 111.14399999999999], [10, 97.58, 183.26, 117.88, 130.51], [10, 97.58, 192.78, 136.404, 149.034], [10, 97.58, 201.10999999999999, 155.76999999999998, 167.558], [10, 97.58, 201.10999999999999, 174.29399999999998, 186.924], [10, 97.58, 163.03, 193.66, 206.29], [10, 97.58, 163.03, 212.184, 224.814], [10, 97.58, 148.155, 231.54999999999998, 243.338], [10, 97.58, 166.6, 250.916, 262.704], [10, 97.58, 204.67999999999998, 269.44, 282.07]]
2026-08-10 18:06:36,231 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=10, matched=10, pages=1, time=10.5s
2026-08-10 18:06:36,232 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:06:36,233 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:06:36,233 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[10]
2026-08-10 18:06:36,233 INFO     29 [qwen-vl-table] positions ： [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:06:36,499 INFO     29 [qwen-vl-table] page=10, rect=595x842, img=(1653x2339)
2026-08-10 18:06:36,499 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:06:36,499 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 312, \"bbox_end\": 347, \"encounter_dates\": [\"2026-03-03\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{|c|l|l|c|c|l|l|l|}\n报告时间: 2016-03-03\n\\hline\n行号 & 中文名 & 项目... & 结果 & 状态 & 项目... & 参考范围 & 单位 \\\\\n\\hline\n2 & 游离甲状腺素*#☆ & & 14.70 & & 1002... & 12-22 & pmol.. \\\\\n\\hline\n3 & 促甲状腺激素*#☆ & & 1.320 & & 1002... & 0.27-4.2 & uIU/... \\\\\n\\hline\n4 & 鳞状细胞癌相关抗原*☆ & & 0.54 & & 1009... & 0-2.5 & ng/ml \\\\\n\\hline\n5 & 糖类抗原CA-50* & & 3.73 & & 1003... & 0-25 & IU/ml \\\\\n\\hline\n6 & 糖类抗原CA-242* & & 0.94 & & 1003... & 0-20 & IU/ml \\\\\n\\hline\n7 & 糖类抗原CA-724*☆ & & 0.95 & & 1003... & 0-6.0 & U/mL \\\\\n\\hline\n8 & 癌胚抗原*#☆ & & 41.00 & $\\uparrow$ & 1001... & 0-5.09 & ng/ml \\\\\n\\hline\n9 & 糖类抗原CA-199*# & & 9.28 & & 1003... & 0.00-27.00 & U/mL \\\\\n\\hline\n10 & 糖类抗原CA-125*#☆ & & 21.50 & & 1003... & 0.00-35.00 & U/mL \\\\\n\\hline\n11 & 糖类抗原CA-153*#☆ & & 15.40 & & 1003... & 0.00-26.2 & U/mL \\\\\n\\hline\n12 & 神经元特异性烯醇化... & & 17.60 & $\\uparrow$ & 1007... & 0.00-16.30 & ng/ml \\\\\n\\hline\n13 & 细胞角蛋白19片段*☆ & & 4.57 & $\\uparrow$ & 1007... & 0.00-3.30 & ng/ml \\\\\n\\hline\n14 & 铁蛋白*#☆ & & 416.00 & $\\uparrow$ & 1007... & 30.00-400.00 & ng/ml \\\\\n\\hline\n15 & β2微球蛋白*# & & 1.380 & & 1011... & 0.90-2.70 & mg/L \\\\\n\\hline\n16 & 胃泌素释放肽前体 & & 22.100 & & 1015... & 0-68.3 & pg/ml \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 18:06:44,809 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:06:44,809 INFO     29 [qwen-vl-table] page=10 LLM output (len=2611):
{
  "report_date": "2016-03-03",
  "items": [
    {
      "name": "游离甲状腺素",
      "item_code": null,
      "value": "14.70",
      "unit": "pmol/L",
      "reference_range": "12-22",
      "abnormal": false
    },
    {
      "name": "促甲状腺激素",
      "item_code": null,
      "value": "1.320",
      "unit": "uIU/mL",
      "reference_range": "0.27-4.2",
      "abnormal": false
    },
    {
      "name": "鳞状细胞癌相关抗原",
      "item_code": null,
      "value": "0.54",
      "unit": "ng/ml",
      "reference_range": "0-2.5",
      "abnormal": false
    },
    {
      "name": "糖类抗原CA-50",
      "item_code": null,
      "value": "3.73",
      "unit": "IU/ml",
      "reference_range": "0-25",
      "abnormal": false
    },
    {
      "name": "糖类抗原CA-242",
      "item_code": null,
      "value": "0.94",
      "unit": "IU/ml",
      "reference_range": "0-20",
      "abnormal": false
    },
    {
      "name": "糖类抗原CA-724",
      "item_code": null,
      "value": "0.95",
      "unit": "U/mL",
      "reference_range": "0-6.0",
      "abnormal": false
    },
    {
      "name": "癌胚抗原",
      "item_code": null,
      "value": "41.00",
      "unit": "ng/ml",
      "reference_range": "0-5.09",
      "abnormal": true
    },
    {
      "name": "糖类抗原CA-199",
      "item_code": null,
      "value": "9.28",
      "unit": "U/mL",
      "reference_range": "0.00-27.00",
      "abnormal": false
    },
    {
      "name": "糖类抗原CA-125",
      "item_code": null,
      "value": "21.50",
      "unit": "U/mL",
      "reference_range": "0.00-35.00",
      "abnormal": false
    },
    {
      "name": "糖类抗原CA-153",
      "item_code": null,
      "value": "15.40",
      "unit": "U/mL",
      "reference_range": "0.00-26.2",
      "abnormal": false
    },
    {
      "name": "神经元特异性烯醇化酶",
      "item_code": null,
      "value": "17.60",
      "unit": "ng/ml",
      "reference_range": "0.00-16.30",
      "abnormal": true
    },
    {
      "name": "细胞角蛋白19片段",
      "item_code": null,
      "value": "4.57",
      "unit": "ng/ml",
      "reference_range": "0.00-3.30",
      "abnormal": true
    },
    {
      "name": "铁蛋白",
      "item_code": null,
      "value": "416.00",
      "unit": "ng/ml",
      "reference_range": "30.00-400.00",
      "abnormal": true
    },
    {
      "name": "β2微球蛋白",
      "item_code": null,
      "value": "1.380",
      "unit": "mg/L",
      "reference_range": "0.90-2.70",
      "abnormal": false
    },
    {
      "name": "胃泌素释放肽前体",
      "item_code": null,
      "value": "22.100",
      "unit": "pg/ml",
      "reference_range": "0-68.3",
      "abnormal": false
    }
  ]
}
2026-08-10 18:06:44,809 INFO     29 [qwen-vl-table] coord grouping: {10: 15}
2026-08-10 18:06:44,815 INFO     29 [qwen-vl-table] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2705753, prompt_len=641
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
游离甲状腺素、促甲状腺激素、鳞状细胞癌相关抗原、糖类抗原CA-50、糖类抗原CA-242、糖类抗原CA-724、癌胚抗原、糖类抗原CA-199、糖类抗原CA-125、糖类抗原CA-153、神经元特异性烯醇化酶、细胞角蛋白19片段、铁蛋白、β2微球蛋白、胃泌素释放肽前体

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
2026-08-10 18:06:49,944 INFO     29 [qwen-vl-table] coord API raw response (len=797):
[
	{"text": "游离甲状腺素", "bbox": [144, 115, 290, 131]},
	{"text": "促甲状腺激素", "bbox": [144, 140, 290, 155]},
	{"text": "鳞状细胞癌相关抗原", "bbox": [144, 163, 333, 179]},
	{"text": "糖类抗原CA-50", "bbox": [144, 187, 282, 202]},
	{"text": "糖类抗原CA-242", "bbox": [144, 210, 293, 225]},
	{"text": "糖类抗原CA-724", "bbox": [144, 234, 309, 249]},
	{"text": "癌胚抗原", "bbox": [144, 257, 254, 272]},
	{"text": "糖类抗原CA-199", "bbox": [144, 280, 304, 295]},
	{"text": "糖类抗原CA-125", "bbox": [144, 304, 320, 319]},
	{"text": "糖类抗原CA-153", "bbox": [144, 327, 320, 342]},
	{"text": "神经元特异性烯醇化酶", "bbox": [144, 351, 320, 366]},
	{"text": "细胞角蛋白19片段", "bbox": [144, 374, 319, 389]},
	{"text": "铁蛋白", "bbox": [144, 398, 236, 413]},
	{"text": "β2微球蛋白", "bbox": [144, 421, 260, 436]},
	{"text": "胃泌素释放肽前体", "bbox": [144, 445, 291, 460]}
]
2026-08-10 18:06:49,944 INFO     29 [qwen-vl-table] coord API: raw_items=15, valid_items=15, elapsed=5.1s
2026-08-10 18:06:49,944 INFO     29 [qwen-vl-table] coord item[0]: text=游离甲状腺素, bbox=[144, 115, 290, 131]
2026-08-10 18:06:49,945 INFO     29 [qwen-vl-table] coord item[1]: text=促甲状腺激素, bbox=[144, 140, 290, 155]
2026-08-10 18:06:49,945 INFO     29 [qwen-vl-table] coord item[2]: text=鳞状细胞癌相关抗原, bbox=[144, 163, 333, 179]
2026-08-10 18:06:49,945 INFO     29 [qwen-vl-table] coord item[3]: text=糖类抗原CA-50, bbox=[144, 187, 282, 202]
2026-08-10 18:06:49,945 INFO     29 [qwen-vl-table] coord item[4]: text=糖类抗原CA-242, bbox=[144, 210, 293, 225]
2026-08-10 18:06:49,945 INFO     29 [qwen-vl-table] coord item[5]: text=糖类抗原CA-724, bbox=[144, 234, 309, 249]
2026-08-10 18:06:49,945 INFO     29 [qwen-vl-table] coord item[6]: text=癌胚抗原, bbox=[144, 257, 254, 272]
2026-08-10 18:06:49,945 INFO     29 [qwen-vl-table] coord item[7]: text=糖类抗原CA-199, bbox=[144, 280, 304, 295]
2026-08-10 18:06:49,945 INFO     29 [qwen-vl-table] coord item[8]: text=糖类抗原CA-125, bbox=[144, 304, 320, 319]
2026-08-10 18:06:49,945 INFO     29 [qwen-vl-table] coord item[9]: text=糖类抗原CA-153, bbox=[144, 327, 320, 342]
2026-08-10 18:06:49,945 INFO     29 [qwen-vl-table] coord item[10]: text=神经元特异性烯醇化酶, bbox=[144, 351, 320, 366]
2026-08-10 18:06:49,945 INFO     29 [qwen-vl-table] coord item[11]: text=细胞角蛋白19片段, bbox=[144, 374, 319, 389]
2026-08-10 18:06:49,945 INFO     29 [qwen-vl-table] coord item[12]: text=铁蛋白, bbox=[144, 398, 236, 413]
2026-08-10 18:06:49,945 INFO     29 [qwen-vl-table] coord item[13]: text=β2微球蛋白, bbox=[144, 421, 260, 436]
2026-08-10 18:06:49,945 INFO     29 [qwen-vl-table] coord item[14]: text=胃泌素释放肽前体, bbox=[144, 445, 291, 460]
2026-08-10 18:06:49,947 INFO     29 [qwen-vl-table] page=10 coord: matched 15/15, time=5.1s
2026-08-10 18:06:49,947 INFO     29 [qwen-vl-table] new_positions (15):
[[11, 85.67999999999999, 172.54999999999998, 96.83, 110.30199999999999], [11, 85.67999999999999, 172.54999999999998, 117.88, 130.51], [11, 85.67999999999999, 198.135, 137.246, 150.718], [11, 85.67999999999999, 167.79, 157.454, 170.084], [11, 85.67999999999999, 174.33499999999998, 176.82, 189.45], [11, 85.67999999999999, 183.855, 197.028, 209.658], [11, 85.67999999999999, 151.13, 216.394, 229.024], [11, 85.67999999999999, 180.88, 235.76, 248.39], [11, 85.67999999999999, 190.39999999999998, 255.968, 268.598], [11, 85.67999999999999, 190.39999999999998, 275.334, 287.964], [11, 85.67999999999999, 190.39999999999998, 295.542, 308.17199999999997], [11, 85.67999999999999, 189.80499999999998, 314.908, 327.538], [11, 85.67999999999999, 140.42, 335.116, 347.746], [11, 85.67999999999999, 154.7, 354.48199999999997, 367.11199999999997], [11, 85.67999999999999, 173.14499999999998, 374.69, 387.32]]
2026-08-10 18:06:49,947 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=15, matched=15, pages=1, time=13.7s
2026-08-10 18:06:49,949 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:06:49,951 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:06:49,951 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[11]
2026-08-10 18:06:49,951 INFO     29 [qwen-vl-table] positions ： [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:06:50,206 INFO     29 [qwen-vl-table] page=11, rect=595x842, img=(1653x2339)
2026-08-10 18:06:50,206 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:06:50,207 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 348, \"bbox_end\": 403, \"encounter_dates\": [\"2026-03-10\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{|c|l|l|l|l|l|l|l|}\n报告时间: 2026-3-10\n\\hline\n行号 & 中文名 & 项目... & 结果 & 状态 & 项目... & 参考范围 & 单位 \\\\\n\\hline\n6-03- & & & & & & & \\\\\n\\hline\n6-03-2 & 中性粒细胞计数 & 正常... & 13.55 & $\\uparrow$ & 30070 & 1.80-6.30 & *10^... \\\\\n\\hline\n6-03-3 & 淋巴细胞计数 & 正常... & 1.86 & & 30050 & 1.10-3.20 & *10^... \\\\\n\\hline\n5-03-4 & 单核细胞计数 & 正常... & 1.32 & $\\uparrow$ & 30060 & 0.10-0.60 & *10^... \\\\\n\\hline\n5-03-5 & 嗜酸细胞计数 & & 0.00 & $\\downarrow$ & 30210 & 0.02-0.52 & *10^... \\\\\n\\hline\n6 & 嗜碱细胞计数 & & 0.07 & $\\uparrow$ & 30220 & 0.00-0.06 & *10^... \\\\\n\\hline\n7 & 中性粒细胞百分比 & 正常... & 80.6 & $\\uparrow$ & 30040 & 40.0-75.0 & \\% \\\\\n\\hline\n8 & 淋巴细胞百分比 & 正常... & 11.1 & $\\downarrow$ & 30020 & 20.0-50.0 & \\% \\\\\n\\hline\n9 & 单核细胞百分比 & 正常... & 7.9 & & 30030 & 3.0-10.0 & \\% \\\\\n\\hline\n10 & 嗜酸细胞百分比 & 参考... & 0.0 & $\\downarrow$ & 30190 & 0.40-8.00 & \\% \\\\\n\\hline\n11 & 嗜碱细胞百分比 & & 0.4 & & 30200 & 0.00-1.00 & \\% \\\\\n\\hline\n12 & 红细胞计数*#☆ & 参考... & 3.69 & $\\downarrow$ & 30080 & 4.30-5.80 & *10^... \\\\\n\\hline\n13 & 血红蛋白含量*#☆ & 正常... & 102 & $\\downarrow$ & 30090 & 130-175 & g/L \\\\\n\\hline\n14 & 红细胞比容*#☆ & 正常... & 0.32 & $\\downarrow$ & 30100 & 0.40-0.50 & L/L \\\\\n\\hline\n15 & 平均红细胞血红蛋白... & 正常... & 27.6 & & 30120 & 27.0-34.0 & pg \\\\\n\\hline\n16 & 平均红细胞血红蛋白... & 正常... & 318 & & 30130 & 316-354 & g/L \\\\\n\\hline\n17 & 平均红细胞体积*#☆ & 正常... & 87.0 & & 30110 & 82.0-100.0 & fL \\\\\n\\hline\n18 & 红细胞分布宽度（CV） & 正常... & 17.3 & $\\uparrow$ & 30140 & 11.6-16.5 & \\% \\\\\n\\hline\n19 & 红细胞分布宽度（SD） & & 54.6 & $\\uparrow$ & 30230 & 37.0-54.0 & fL \\\\\n\\hline\n20 & 血小板计数*#☆ & 参考... & 466 & $\\uparrow$ & 30150 & 125-350 & *10^... \\\\\n\\hline\n21 & 平均血小板体积 & 正常... & 8.8 & & 30160 & 7.4-11.0 & fL \\\\\n\\hline\n22 & 大血小板比率 & 正常... & 15.7 & & 30170 & 13.0-43.0 & \\% \\\\\n\\hline\n23 & 血小板比容 & & 0.41 & $\\uparrow$ & 30240 & 0.170-0.350 & \\% \\\\\n\\hline\n24 & 血小板分布宽度 & 正常... & 8.5 & $\\downarrow$ & 30180 & 9.6-15.2 & fL \\\\\n\\hline\n25 & C-反应蛋白* & & 177.... & $\\uparrow$ & 30340 & 0.000-5.000 & mg/L \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 18:06:50,208 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:06:50.208+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 84, "failed": 0, "current": {"d64c79b494e511f1bd9827cf206dfa2d": {"id": "d64c79b494e511f1bd9827cf206dfa2d", "doc_id": "d60771c094e511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 5825068, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385028897, "task_type": "dataflow", "root_trace_id": "93629fbf7f764cf397a9e7f896dd05c6", "root_traceparent": "00-93629fbf7f764cf397a9e7f896dd05c6-e7dded3dfece48a2-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:07:06,115 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:07:06,116 INFO     29 [qwen-vl-table] page=11 LLM output (len=4089):
{
  "report_date": "2026-03-10",
  "items": [
    {
      "name": "中性粒细胞计数",
      "item_code": null,
      "value": "13.55",
      "unit": "*10^9/L",
      "reference_range": "1.80-6.30",
      "abnormal": true
    },
    {
      "name": "淋巴细胞计数",
      "item_code": null,
      "value": "1.86",
      "unit": "*10^9/L",
      "reference_range": "1.10-3.20",
      "abnormal": false
    },
    {
      "name": "单核细胞计数",
      "item_code": null,
      "value": "1.32",
      "unit": "*10^9/L",
      "reference_range": "0.10-0.60",
      "abnormal": true
    },
    {
      "name": "嗜酸细胞计数",
      "item_code": null,
      "value": "0.00",
      "unit": "*10^9/L",
      "reference_range": "0.02-0.52",
      "abnormal": true
    },
    {
      "name": "嗜碱细胞计数",
      "item_code": null,
      "value": "0.07",
      "unit": "*10^9/L",
      "reference_range": "0.00-0.06",
      "abnormal": true
    },
    {
      "name": "中性粒细胞百分比",
      "item_code": null,
      "value": "80.6",
      "unit": "%",
      "reference_range": "40.0-75.0",
      "abnormal": true
    },
    {
      "name": "淋巴细胞百分比",
      "item_code": null,
      "value": "11.1",
      "unit": "%",
      "reference_range": "20.0-50.0",
      "abnormal": true
    },
    {
      "name": "单核细胞百分比",
      "item_code": null,
      "value": "7.9",
      "unit": "%",
      "reference_range": "3.0-10.0",
      "abnormal": false
    },
    {
      "name": "嗜酸细胞百分比",
      "item_code": null,
      "value": "0.0",
      "unit": "%",
      "reference_range": "0.40-8.00",
      "abnormal": true
    },
    {
      "name": "嗜碱细胞百分比",
      "item_code": null,
      "value": "0.4",
      "unit": "%",
      "reference_range": "0.00-1.00",
      "abnormal": false
    },
    {
      "name": "红细胞计数",
      "item_code": null,
      "value": "3.69",
      "unit": "*10^12/L",
      "reference_range": "4.30-5.80",
      "abnormal": true
    },
    {
      "name": "血红蛋白含量",
      "item_code": null,
      "value": "102",
      "unit": "g/L",
      "reference_range": "130-175",
      "abnormal": true
    },
    {
      "name": "红细胞比容",
      "item_code": null,
      "value": "0.32",
      "unit": "L/L",
      "reference_range": "0.40-0.50",
      "abnormal": true
    },
    {
      "name": "平均红细胞血红蛋白含量",
      "item_code": null,
      "value": "27.6",
      "unit": "pg",
      "reference_range": "27.0-34.0",
      "abnormal": false
    },
    {
      "name": "平均红细胞血红蛋白浓度",
      "item_code": null,
      "value": "318",
      "unit": "g/L",
      "reference_range": "316-354",
      "abnormal": false
    },
    {
      "name": "平均红细胞体积",
      "item_code": null,
      "value": "87.0",
      "unit": "fL",
      "reference_range": "82.0-100.0",
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度（CV）",
      "item_code": null,
      "value": "17.3",
      "unit": "%",
      "reference_range": "11.6-16.5",
      "abnormal": true
    },
    {
      "name": "红细胞分布宽度（SD）",
      "item_code": null,
      "value": "54.6",
      "unit": "fL",
      "reference_range": "37.0-54.0",
      "abnormal": true
    },
    {
      "name": "血小板计数",
      "item_code": null,
      "value": "466",
      "unit": "*10^9/L",
      "reference_range": "125-350",
      "abnormal": true
    },
    {
      "name": "平均血小板体积",
      "item_code": null,
      "value": "8.8",
      "unit": "fL",
      "reference_range": "7.4-11.0",
      "abnormal": false
    },
    {
      "name": "大血小板比率",
      "item_code": null,
      "value": "15.7",
      "unit": "%",
      "reference_range": "13.0-43.0",
      "abnormal": false
    },
    {
      "name": "血小板比容",
      "item_code": null,
      "value": "0.41",
      "unit": "%",
      "reference_range": "0.170-0.350",
      "abnormal": true
    },
    {
      "name": "血小板分布宽度",
      "item_code": null,
      "value": "8.5",
      "unit": "fL",
      "reference_range": "9.6-15.2",
      "abnormal": true
    },
    {
      "name": "C-反应蛋白",
      "item_code": null,
      "value": "177",
      "unit": "mg/L",
      "reference_range": "0.000-5.000",
      "abnormal": true
    }
  ]
}
2026-08-10 18:07:06,116 INFO     29 [qwen-vl-table] coord grouping: {11: 24}
2026-08-10 18:07:06,120 INFO     29 [qwen-vl-table] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2563508, prompt_len=700
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
中性粒细胞计数、淋巴细胞计数、单核细胞计数、嗜酸细胞计数、嗜碱细胞计数、中性粒细胞百分比、淋巴细胞百分比、单核细胞百分比、嗜酸细胞百分比、嗜碱细胞百分比、红细胞计数、血红蛋白含量、红细胞比容、平均红细胞血红蛋白含量、平均红细胞血红蛋白浓度、平均红细胞体积、红细胞分布宽度（CV）、红细胞分布宽度（SD）、血小板计数、平均血小板体积、大血小板比率、血小板比容、血小板分布宽度、C-反应蛋白

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
2026-08-10 18:07:13,061 INFO     29 [qwen-vl-table] coord API raw response (len=1250):
[
	{"text": "中性粒细胞计数", "bbox": [129, 80, 260, 97]},
	{"text": "淋巴细胞计数", "bbox": [129, 104, 240, 120]},
	{"text": "单核细胞计数", "bbox": [129, 128, 240, 144]},
	{"text": "嗜酸细胞计数", "bbox": [129, 151, 240, 167]},
	{"text": "嗜碱细胞计数", "bbox": [129, 174, 240, 190]},
	{"text": "中性粒细胞百分比", "bbox": [129, 198, 277, 214]},
	{"text": "淋巴细胞百分比", "bbox": [129, 221, 258, 237]},
	{"text": "单核细胞百分比", "bbox": [129, 245, 258, 261]},
	{"text": "嗜酸细胞百分比", "bbox": [129, 268, 258, 284]},
	{"text": "嗜碱细胞百分比", "bbox": [129, 292, 258, 308]},
	{"text": "红细胞计数", "bbox": [129, 315, 255, 331]},
	{"text": "血红蛋白含量", "bbox": [129, 339, 274, 355]},
	{"text": "红细胞比容", "bbox": [129, 362, 255, 378]},
	{"text": "平均红细胞血红蛋白含量", "bbox": [129, 386, 308, 402]},
	{"text": "平均红细胞血红蛋白浓度", "bbox": [129, 409, 308, 425]},
	{"text": "平均红细胞体积", "bbox": [129, 433, 293, 449]},
	{"text": "红细胞分布宽度（CV）", "bbox": [129, 456, 314, 472]},
	{"text": "红细胞分布宽度（SD）", "bbox": [129, 479, 314, 495]},
	{"text": "血小板计数", "bbox": [129, 503, 255, 519]},
	{"text": "平均血小板体积", "bbox": [129, 526, 255, 542]},
	{"text": "大血小板比率", "bbox": [129, 550, 239, 566]},
	{"text": "血小板比容", "bbox": [129, 573, 219, 589]},
	{"text": "血小板分布宽度", "bbox": [129, 597, 255, 613]},
	{"text": "C-反应蛋白", "bbox": [129, 620, 230, 636]}
]
2026-08-10 18:07:13,061 INFO     29 [qwen-vl-table] coord API: raw_items=24, valid_items=24, elapsed=6.9s
2026-08-10 18:07:13,061 INFO     29 [qwen-vl-table] coord item[0]: text=中性粒细胞计数, bbox=[129, 80, 260, 97]
2026-08-10 18:07:13,061 INFO     29 [qwen-vl-table] coord item[1]: text=淋巴细胞计数, bbox=[129, 104, 240, 120]
2026-08-10 18:07:13,061 INFO     29 [qwen-vl-table] coord item[2]: text=单核细胞计数, bbox=[129, 128, 240, 144]
2026-08-10 18:07:13,061 INFO     29 [qwen-vl-table] coord item[3]: text=嗜酸细胞计数, bbox=[129, 151, 240, 167]
2026-08-10 18:07:13,061 INFO     29 [qwen-vl-table] coord item[4]: text=嗜碱细胞计数, bbox=[129, 174, 240, 190]
2026-08-10 18:07:13,061 INFO     29 [qwen-vl-table] coord item[5]: text=中性粒细胞百分比, bbox=[129, 198, 277, 214]
2026-08-10 18:07:13,061 INFO     29 [qwen-vl-table] coord item[6]: text=淋巴细胞百分比, bbox=[129, 221, 258, 237]
2026-08-10 18:07:13,061 INFO     29 [qwen-vl-table] coord item[7]: text=单核细胞百分比, bbox=[129, 245, 258, 261]
2026-08-10 18:07:13,061 INFO     29 [qwen-vl-table] coord item[8]: text=嗜酸细胞百分比, bbox=[129, 268, 258, 284]
2026-08-10 18:07:13,061 INFO     29 [qwen-vl-table] coord item[9]: text=嗜碱细胞百分比, bbox=[129, 292, 258, 308]
2026-08-10 18:07:13,061 INFO     29 [qwen-vl-table] coord item[10]: text=红细胞计数, bbox=[129, 315, 255, 331]
2026-08-10 18:07:13,061 INFO     29 [qwen-vl-table] coord item[11]: text=血红蛋白含量, bbox=[129, 339, 274, 355]
2026-08-10 18:07:13,061 INFO     29 [qwen-vl-table] coord item[12]: text=红细胞比容, bbox=[129, 362, 255, 378]
2026-08-10 18:07:13,061 INFO     29 [qwen-vl-table] coord item[13]: text=平均红细胞血红蛋白含量, bbox=[129, 386, 308, 402]
2026-08-10 18:07:13,062 INFO     29 [qwen-vl-table] coord item[14]: text=平均红细胞血红蛋白浓度, bbox=[129, 409, 308, 425]
2026-08-10 18:07:13,062 INFO     29 [qwen-vl-table] coord item[15]: text=平均红细胞体积, bbox=[129, 433, 293, 449]
2026-08-10 18:07:13,062 INFO     29 [qwen-vl-table] coord item[16]: text=红细胞分布宽度（CV）, bbox=[129, 456, 314, 472]
2026-08-10 18:07:13,062 INFO     29 [qwen-vl-table] coord item[17]: text=红细胞分布宽度（SD）, bbox=[129, 479, 314, 495]
2026-08-10 18:07:13,062 INFO     29 [qwen-vl-table] coord item[18]: text=血小板计数, bbox=[129, 503, 255, 519]
2026-08-10 18:07:13,062 INFO     29 [qwen-vl-table] coord item[19]: text=平均血小板体积, bbox=[129, 526, 255, 542]
2026-08-10 18:07:13,062 INFO     29 [qwen-vl-table] coord item[20]: text=大血小板比率, bbox=[129, 550, 239, 566]
2026-08-10 18:07:13,062 INFO     29 [qwen-vl-table] coord item[21]: text=血小板比容, bbox=[129, 573, 219, 589]
2026-08-10 18:07:13,062 INFO     29 [qwen-vl-table] coord item[22]: text=血小板分布宽度, bbox=[129, 597, 255, 613]
2026-08-10 18:07:13,062 INFO     29 [qwen-vl-table] coord item[23]: text=C-反应蛋白, bbox=[129, 620, 230, 636]
2026-08-10 18:07:13,062 INFO     29 [qwen-vl-table] page=11 coord: matched 24/24, time=6.9s
2026-08-10 18:07:13,063 INFO     29 [qwen-vl-table] new_positions (24):
[[12, 76.755, 154.7, 67.36, 81.67399999999999], [12, 76.755, 142.79999999999998, 87.568, 101.03999999999999], [12, 76.755, 142.79999999999998, 107.776, 121.24799999999999], [12, 76.755, 142.79999999999998, 127.142, 140.614], [12, 76.755, 142.79999999999998, 146.50799999999998, 159.98], [12, 76.755, 164.815, 166.716, 180.188], [12, 76.755, 153.51, 186.082, 199.554], [12, 76.755, 153.51, 206.29, 219.762], [12, 76.755, 153.51, 225.656, 239.128], [12, 76.755, 153.51, 245.864, 259.336], [12, 76.755, 151.725, 265.23, 278.702], [12, 76.755, 163.03, 285.438, 298.90999999999997], [12, 76.755, 151.725, 304.804, 318.276], [12, 76.755, 183.26, 325.012, 338.484], [12, 76.755, 183.26, 344.378, 357.84999999999997], [12, 76.755, 174.33499999999998, 364.586, 378.058], [12, 76.755, 186.82999999999998, 383.952, 397.424], [12, 76.755, 186.82999999999998, 403.318, 416.78999999999996], [12, 76.755, 151.725, 423.526, 436.998], [12, 76.755, 151.725, 442.892, 456.364], [12, 76.755, 142.20499999999998, 463.09999999999997, 476.572], [12, 76.755, 130.305, 482.466, 495.938], [12, 76.755, 151.725, 502.674, 516.146], [12, 76.755, 136.85, 522.04, 535.512]]
2026-08-10 18:07:13,063 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=24, matched=24, pages=1, time=23.1s
2026-08-10 18:07:13,070 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 18:07:13,071 INFO     29 [Trace] task=d64c79b4 | doc=07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf | Extractor:LabExam | outputs={"chunks": "4 items, types={'LabReport': 4}", "html": "", "json": "417 items", "markdown": "", "text": "", "name": "07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Admission\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 18:07:13,071 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 18:07:13,076 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:07:13,076 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 18:07:14,312 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:07:14,319 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 18:07:14,319 INFO     29 [Trace] task=d64c79b4 | doc=07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "417 items", "markdown": "", "text": "", "name": "07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Admission\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 18:07:14,320 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 18:07:14,325 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:07:14,325 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 18:07:14,859 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:07:14,865 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 18:07:14,865 INFO     29 [Trace] task=d64c79b4 | doc=07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf | Extractor:Clinical | outputs={"chunks": "1 items", "html": "", "json": "417 items", "markdown": "", "text": "", "name": "07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Admission\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 18:07:14,865 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 18:07:14,869 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:07:14,870 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 18:07:15,570 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:07:15,577 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 18:07:15,577 INFO     29 [Trace] task=d64c79b4 | doc=07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "417 items", "markdown": "", "text": "", "name": "07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Admission\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 18:07:15,578 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 18:07:15,583 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:07:15,583 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 18:07:16,005 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:07:16,009 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 18:07:16,009 INFO     29 [Trace] task=d64c79b4 | doc=07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "417 items", "markdown": "", "text": "", "name": "07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Admission\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 18:07:16,009 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 18:07:16,013 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:07:16,013 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 18:07:16,434 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:07:16,439 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 18:07:16,439 INFO     29 [Trace] task=d64c79b4 | doc=07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "417 items", "markdown": "", "text": "", "name": "07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Admission\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 18:07:16,439 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 18:07:16,446 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:07:16,447 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:07:16,448 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-10 18:07:16,448 INFO     29 [qwen-vl-text] positions(93): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:07:16,448 INFO     29 [qwen-vl-text] page grouping: [3, 4, 5], lines per page: [32, 30, 31]
2026-08-10 18:07:16,701 INFO     29 [qwen-vl-text] page=3, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 18:07:16,981 INFO     29 [qwen-vl-text] page=4, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 18:07:17,192 INFO     29 [qwen-vl-text] page=5, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 18:07:17,193 INFO     29 [qwen-vl-text] LLM extraction start, text_len=5295
2026-08-10 18:07:17,193 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:07:17,193 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 61, \"bbox_end\": 153, \"encounter_dates\": [\"2026-03-04\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "2026-03-04 15:46 入院记录\n性别：男\n职业：其他\n年龄：57岁\n入院时间：2026-03-04 15:38:00\n民族：汉族\n记录时间：2026-03-04 15:46\n婚姻：已婚\n病史陈述者：患者本人及家属\n主诉：确诊左肺癌2年余，双下肢疼痛1周。\n现病史：患者2年余前查体发现左颈部肿物，约豆粒大小，无疼痛，偶有咳嗽、咳痰，无痰中带血丝，活动后偶感胸闷、憋气，无咯血，无胸痛，无发热。后肿物逐渐增大，遂就诊于我院，2023-03-30行\nPET/CT：1，左肺上叶高代谢占位，考虑肺癌（并累及邻近胸膜），（左侧颈部V区、左锁骨上、纵隔、左肺门10区、左肺内11-12区）多发淋巴结转移；建议病理学检查；左肺门10区淋巴结旁肺组织见网格样密度\n增高影，轻度PDG代谢增高，建议结合临床并复查。未行特殊治疗。后就诊于我科，2023-04-03行快速石蜡病理诊断：（左锁骨上淋巴结穿刺活检）纤维组织内查见分化差的癌，结合免疫组化及病史，不除外肺非\n小细胞癌转移。经齐鲁医院会诊：倾向肺腺癌。免疫组化结果：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（-）、P40（灶+）。2023-04-06行胸部增强CT：左肺上叶恶性肿瘤并累及邻近胸膜，左锁骨上、左\n肺门及纵隔多发淋巴结转移。快速石蜡病理诊断：（左肺上叶穿刺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，特殊染色待补充报告。免疫组化结果：CK5/6（-）、P40（部分+）、\nTTF-1（-）、NapsinA（-）、CK7（+）。ALK（D5F3）：阴性；（兔单克隆阴性对照：阴性；阳性对照：阳性）。2023-04-07至2023-06-30行替雷利珠单抗200mg免疫治疗+贝伐珠单抗注射液900.00mg靶向治\n疗，联合卡铂500.00mg d1+培美曲塞二钠850.00mg d1化疗5周期。排除禁忌，患者于2023-07-06行胸部IMRT放疗，具体：IMRT,PTV 60GY/30F，末次放疗时间为2023-08-09。2023-07-19行卡铂500mg化疗联合恩度\n靶向及替雷利珠单抗免疫治疗。2023-08-10予以患者恩度靶向及替雷利珠单抗免疫治疗。2024-09-30行顺铂40mgd1化疗，联合贝伐珠单抗注射液靶向、替雷利珠单抗免疫治疗。2024-11-6复查CT示：左肺上叶团片\n影，较前2024.07.10范围增大，较2024.10.23示实性成分增多。病情较前进展。2024-11-07、2024-12-3行贝伐珠单抗800mg+替雷丽珠单抗200mg+顺铂80.00mg d1+紫杉醇脂质体270.00mg d1全身化疗2周期，因患\n者消化道反应重，2025-1-16、2025-2-6行贝伐珠单抗800mg+替雷丽珠单抗200mg+顺铂60.00mg d1+紫杉醇脂质体240.00mg d1全身化疗2周。因出现消化道反应III级，后2025-3-25改行紫杉醇聚合物胶束300mgd1联\n合卡铂400mgd1化疗，并行贝伐珠单抗800mg靶向联合替雷丽珠单抗200mg免疫治疗，2025-4-15行贝伐珠单抗800mgd0+替雷丽珠单抗200mgd0+紫杉醇聚合物胶束300mgd1+卡铂500mgd1，过程顺利。因医院紫杉醇聚合\n物胶束无货，2025-5-7行顺铂80.00mg d1+紫杉醇脂质体270mg d1化疗1周期，2025-7-28至2025-12按期行卡铂500mg d1+紫杉醇聚合物胶束300mg，并行贝伐珠单抗注射液400mg靶向、（百泽安）替雷利珠单抗注射液\n200.00mg d1免疫治疗。2026-01-19行注射用紫杉醇脂质体270mgd1+卡铂 500.00mg d1化疗1周期。2025-12-27行颈+胸部增强CT：肺癌复查：左肺团片影，较前2025-09-03增大；左肺门及纵隔多发肿大淋巴结，较\n前部分增大。病情较前进展。1周前患者无明显诱因出现双下肢疼痛，间断性，走路踩棉花样，影响夜间睡眠。现为行进一步治疗收住我科。自发病以来，精神可，饮食、睡眠欠佳，大小便无异常，近1个月体重\n较前无明显变化。\n既往史：否认“冠心病、高血压、糖尿病”病史。否认“肝炎、结核”等传染病病史及密切接触史。否认重大外伤史，否认手术史，否认输血史。无药物及食物过敏。预防接种随当地进行。\n个人史：生于原籍，无外地久居史，无疫区长期居住史，无聚集性发病。生活规律，吸烟30余年，约20支/天，偶有饮酒史，现烟酒均已戒2年，无毒物、粉尘及放射性物质接触史，无冶游史，无重大精神创\n伤史。全程接种新冠疫苗。\n婚育史：23岁结婚，配偶健在，育2女，女儿健康。\n家族史：父亲去世（具体不详），母亲健在。兄弟2人，1个弟弟健在。家族中无遗传病病史及类似病史。\n体 格 检 查\nT:36.6℃ P:80次/分 R:20次/分 Bp:132/82mmHg VTE:3分\n个人史：生于原籍，无外地久居史，无疫区长期居住史，无聚集性发病。生活规律，吸烟30余年，约20支/天，偶有饮酒史，现烟酒均已戒2年，无毒物、粉尘及放射性物质接触史，无冶游史，无重大精神创伤史，全程接种新冠疫苗。\n婚育史：23岁结婚，配偶健在，育2女，女儿健康。\n家族史：父亲去世（具体不详），母亲健在。兄弟2人，1个弟弟健在。家族中无遗传病病史及类似病史。\n体格检查\nT:36.6℃ P:80次/分 R:20次/分 Bp:132/82mmHg VTE:3分\nH:168cm W:65kg S:1.71平方米 NRS:0分 PS:1分 NRS-2002:1分\n中年男性，发育正常，营养中等，神志清楚，自主体位，正常面容，检查合作。全身皮肤、黏膜无苍白、紫绀、黄染，无水肿、皮疹、瘀点、紫癜、皮下结节，无蜘蛛痣、肝掌。全身浅表淋巴结未触及肿大，\n局部皮肤无红肿、波动、压痛、瘘管。左侧锁骨上触及大约3×2cm肿物，质硬，固定，颈部柔软，双侧对称，颈静脉无怒张，肝颈静脉回流征阴性，无颈动脉异常搏动，气管位置居中，甲状腺无肿大，胸廓对\n称，无畸形，胸骨无压痛，胸壁无皮下气肿及静脉曲张，呼吸节律正常。双侧呼吸活动度对称，双侧语音震颤正常，无胸膜摩擦感、皮下捻发感；叩诊双肺呈清音，两肺下界在锁骨中线第六肋间，腋中线第八肋\n间，肩胛下角线第十肋间，肺下界活动度正常。双肺呼吸音粗，未闻及干湿性罗音，未闻及胸膜摩擦音。心前区无隆起，心尖搏动在锁骨中线第五肋间隙内侧0.5cm处，搏动范围及强度无异常，无震颤及心包摩擦\n感。心脏左右浊音界正常。心音正常，心率76次/分，心律规整，各瓣膜听诊区无心音分裂、额外心音、杂音，无心包摩擦音。无毛细血管搏动、射枪音、水冲脉和无动脉异常搏动。腹部对称、平坦，无肠型及胃\n肠蠕动波，无皮疹、色素、条纹，无腹壁静脉曲张，无疝和局部隆起，腹部柔软，腹无压痛、反跳痛，未触及包块，无液波震颤，肝脾肋下未触及。墨菲氏征阴性。腹部叩诊鼓音，肝上界在右锁骨中线第五肋\n间，肝肾区无叩痛，无移动性浊音。肠鸣音正常4次/分，无振水音，无血管杂音。肛门直肠及外生殖器未检查。脊柱生理弯曲正常，无畸形，无压痛和叩击痛，活动自如，腰骶部无异常。四肢无畸形，肌张力正\n常，关节无红肿，活动正常，双下肢无水肿及静脉曲张。腹壁反射、肱二、三头肌肌腱反射、膝腱反射、跟腱反射均正常存在；Babinski征阴性，Gordon征阴性，Oppenheim征阴性，Hoffmann征阴性；Kernig征阴\n性，Brudzinski征阴性。\n专科检查：双肺呼吸音粗，未闻及干湿性罗音，未闻及胸膜摩擦音。心音正常，心率76次/分，心律规整，腹部柔软，腹无压痛、反跳痛，未触及包块，无液波震颤，肝脾肋下未触及。\n辅助检查\n检查日期 检查项目 结果（检查医院）\n2023-03-30 PET/CT：1，左肺上叶高代谢占位，考虑肺癌（并累及邻近胸膜），（左侧颈部V区、左锁骨上、纵隔、左肺门10区、左肺内11-12区）多发淋巴结转移；建议病理学检查；左肺门\n10区淋巴结旁肺组织见网格样密度增高影，轻度PDG代谢增高，建议结合临床并复查。2.双肺肺气肿；双肺少许纤维条索灶。3.副鼻窦炎（双侧上颌窦、右侧筛窦）。4.冠状动脉钙化灶。5.十二指肠圈小憩室。6.\n肝脏囊肿。7.左肾囊肿。8.脊椎骨质增生；骶3水平椎管囊肿。（本院）\n2023-04-03 （左锁骨上淋巴结穿刺活检）纤维组织内查见分化差的癌，结合免疫组化及病史，不除外肺非小细胞癌转移。免疫组化结果：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（-）、\nP40（灶+）。（本院）经齐鲁医院会诊：倾向肺腺癌。\n2023-04-03 颅脑磁共振平扫+DVI+增强扫描MRI：脑内多发缺血灶，建议复查双侧上颌窦囊肿。（本院）\n2023-04-06 胸部CT增强扫描CT：1.左肺上叶恶性肿瘤并累及邻近胸膜，左锁骨上、左肺门及纵隔多发淋巴结转移 2.双肺肺气肿；双肺少许纤维条索灶 3.冠状动脉钙化灶 4.扫及肝囊肿、左\n肾囊肿。（本院）\n2023-04-10 快速石蜡病理诊断：（左肺上叶穿刺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，特殊染色待补充报告。免疫组化结果：CK5/6（-）、P40（部分\n+）、TTF-1（-）、NapsinA（-）、CK7（+）。ALK（D5F3）：阴性；（免单克隆阴性对照：阴性；阳性对照：阳性）。（本院）\n2023-04-05 基因检测：未检出与靶向治疗相关基因突变；PD-L1检测：TPS约3%。（赛泽检验）\n2023-07-20 胸部CT：1.肺癌复查：左肺上叶占位，较前（2023-06-30）范围缩小；左锁骨上、左肺门及纵隔多发淋巴结转移，较前变化不大 2.双肺肺气肿；双肺少许纤维条索灶 3.主动脉及\n2023-07-20\n胸部CT：1.肺癌复查：左肺上叶占位，较前（2023-06-30）范围缩小；左锁骨上、左肺门及纵隔多发淋巴结转移，较前变化不大2.双肺肺气肿；双肺少许纤维条索灶3.主动脉及\n冠状动脉钙化4.扫及肝囊肿胸部CT平扫，下腹部（肾）CT平扫，上腹部CT平扫，盆腔CT平扫CT（2023-08-11）：1.肺癌复查：左肺上叶占位，范围较前（2023-7-20）减小；左锁骨上、左肺门及纵隔多发稍大淋巴\n结，较前变化不大2.双肺肺气肿；双肺少许条索灶3.主动脉及冠状动脉钙化4.肝囊肿5.左肾稍低密度灶，建议超声检查；左肾囊肿6.十二指肠降段憩室7.右侧髂骨稍高密度灶，建议复查8.考虑骶管（S3-4\n水平）囊肿。（本院）\n2025-03-11\n颈部+胸部增强CT：1.肺癌复查：左肺团片影，较前25.2.6范围相仿；2.双肺微小结节，原左肺新增结节较前略小（im149薄层），转移不除外，余较前相仿，定期复查；3.双肺\n肺气肿；双肺条索灶；4.左肺门及纵隔多发稍大淋巴结，较前相仿；5.主动脉及冠状动脉钙化；心包少量积液；左侧胸膜局限性增厚；6.扫及肝囊肿；左肾囊肿。（本院）\n2025-09-02\n颅脑磁共振成像+DWI（特殊序列成像）MR：考虑脑内多发小缺血灶，较前（2024-11-8）变化不著，建议复查。左侧上颌窦囊肿。（本院）\n2025-09-03\n颈部CT增强扫描，胸部CT增强扫描，上腹部CT增强扫描，盆腔CT增强扫描，下腹部CT增强扫描：1.肺癌复查：左肺团片影，较前2025.05.07范围略增大，建议复查2.双肺微小结节，\n较前变化不大，转移不除外，建议定期复查3.双肺肺气肿；双肺条索灶4.左肺门及纵隔多发稍大淋巴结，较前略大5.主动脉及冠状动脉钙化；心包少量积液；左侧胸膜局限性增厚6.肝囊肿；左肾囊肿7.\n十二指肠降段憩室8.右侧髂骨稍高密度灶，较前2024.11.06变化不大，建议复查9.考虑骶管囊肿10.颈部未见明显异常；扫及双侧上颌窦炎。（本院）\n2025-12-27\n颈+胸部增强CT：1.肺癌复查：左肺团片影，较前2025-09-03增大；周围新发实变及网格影，请结合临床，建议复查；2.双肺小结节及小斑片影，较前部分增大，部分新发，部分\n变化不大，建议定期复查；3.双肺肺气肿；双肺条索灶；双肺胸膜下磨玻璃密度影，请结合临床随诊复查；4.左肺门及纵隔多发肿大淋巴结，较前部分增大；5.主动脉及冠状动脉钙化；心包少量积液；左侧胸\n膜局限性增厚；左侧胸腔少量积液；6.扫及肝囊肿；左肾囊肿7.颈部未见明显异常；扫及双侧上颌窦炎。（本院）\n初步诊断\n1、左肺上叶癌腺癌cT3N3MOIIIC期\n纵隔淋巴结转移\n锁骨上淋巴结转移\n肺门淋巴结转移\n颈部淋巴结转移\n2、肺气肿\n3、鼻窦炎\n4、肝囊肿\n5、肾囊肿\n6、上颌窦囊肿\n我审核病史记录内容属实无遗漏，我交给医院的病例资料已收回，患方签字：\n宗茹",
    "role": "user"
  }
]
2026-08-10 18:07:22,302 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:07:22.301+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 84, "failed": 0, "current": {"d64c79b494e511f1bd9827cf206dfa2d": {"id": "d64c79b494e511f1bd9827cf206dfa2d", "doc_id": "d60771c094e511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 5825068, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385028897, "task_type": "dataflow", "root_trace_id": "93629fbf7f764cf397a9e7f896dd05c6", "root_traceparent": "00-93629fbf7f764cf397a9e7f896dd05c6-e7dded3dfece48a2-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:07:48,177 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:07:48,177 INFO     29 [qwen-vl-text] LLM output (len=5382):
{
  "encounter_date": "2026-03-04",
  "dm_name": null,
  "dm_gender": "男",
  "dm_age": 57,
  "dm_ethnicity": "汉族",
  "dm_marital_status": "已婚",
  "dm_occupation": "其他",
  "dm_admission_time": "2026-03-04 15:38",
  "dm_record_time": "2026-03-04 15:46",
  "dm_history_provider": "患者本人及家属",
  "cc_text": "确诊左肺癌2年余，双下肢疼痛1周。",
  "cc_main_symptoms": [
    "确诊左肺癌",
    "双下肢疼痛"
  ],
  "cc_duration": "2年余",
  "pi_text": "患者2年余前查体发现左颈部肿物，约豆粒大小，无疼痛，偶有咳嗽、咳痰，无痰中带血丝，活动后偶感胸闷、憋气，无咯血，无胸痛，无发热。后肿物逐渐增大，遂就诊于我院，2023-03-30行PET/CT：1，左肺上叶高代谢占位，考虑肺癌（并累及邻近胸膜），（左侧颈部V区、左锁骨上、纵隔、左肺门10区、左肺内11-12区）多发淋巴结转移；建议病理学检查；左肺门10区淋巴结旁肺组织见网格样密度增高影，轻度PDG代谢增高，建议结合临床并复查。未行特殊治疗。后就诊于我科，2023-04-03行快速石蜡病理诊断：（左锁骨上淋巴结穿刺活检）纤维组织内查见分化差的癌，结合免疫组化及病史，不除外肺非小细胞癌转移。经齐鲁医院会诊：倾向肺腺癌。免疫组化结果：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（-）、P40（灶+）。2023-04-06行胸部增强CT：左肺上叶恶性肿瘤并累及邻近胸膜，左锁骨上、左肺门及纵隔多发淋巴结转移。快速石蜡病理诊断：（左肺上叶穿刺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，特殊染色待补充报告。免疫组化结果：CK5/6（-）、P40（部分+）、TTF-1（-）、NapsinA（-）、CK7（+）。ALK（D5F3）：阴性；（兔单克隆阴性对照：阴性；阳性对照：阳性）。2023-04-07至2023-06-30行替雷利珠单抗200mg免疫治疗+贝伐珠单抗注射液900.00mg靶向治疗，联合卡铂500.00mg d1+培美曲塞二钠850.00mg d1化疗5周期。排除禁忌，患者于2023-07-06行胸部IMRT放疗，具体：IMRT,PTV 60GY/30F，末次放疗时间为2023-08-09。2023-07-19行卡铂500mg化疗联合恩度靶向及替雷利珠单抗免疫治疗。2023-08-10予以患者恩度靶向及替雷利珠单抗免疫治疗。2024-09-30行顺铂40mgd1化疗，联合贝伐珠单抗注射液靶向、替雷利珠单抗免疫治疗。2024-11-6复查CT示：左肺上叶团片影，较前2024.07.10范围增大，较2024.10.23示实性成分增多。病情较前进展。2024-11-07、2024-12-3行贝伐珠单抗800mg+替雷丽珠单抗200mg+顺铂80.00mg d1+紫杉醇脂质体270.00mg d1全身化疗2周期，因患者消化道反应重，2025-1-16、2025-2-6行贝伐珠单抗800mg+替雷丽珠单抗200mg+顺铂60.00mg d1+紫杉醇脂质体240.00mg d1全身化疗2周。因出现消化道反应III级，后2025-3-25改行紫杉醇聚合物胶束300mgd1联合卡铂400mgd1化疗，并行贝伐珠单抗800mg靶向联合替雷丽珠单抗200mg免疫治疗，2025-4-15行贝伐珠单抗800mgd0+替雷丽珠单抗200mgd0+紫杉醇聚合物胶束300mgd1+卡铂500mgd1，过程顺利。因医院紫杉醇聚合物胶束无货，2025-5-7行顺铂80.00mg d1+紫杉醇脂质体270mg d1化疗1周期，2025-7-28至2025-12按期行卡铂500mg d1+紫杉醇聚合物胶束300mg，并行贝伐珠单抗注射液400mg靶向、（百泽安）替雷利珠单抗注射液200.00mg d1免疫治疗。2026-01-19行注射用紫杉醇脂质体270mgd1+卡铂 500.00mg d1化疗1周期。2025-12-27行颈+胸部增强CT：肺癌复查：左肺团片影，较前2025-09-03增大；左肺门及纵隔多发肿大淋巴结，较前部分增大。病情较前进展。1周前患者无明显诱因出现双下肢疼痛，间断性，走路踩棉花样，影响夜间睡眠。现为行进一步治疗收住我科。自发病以来，精神可，饮食、睡眠欠佳，大小便无异常，近1个月体重较前无明显变化。",
  "pmh_disease_history": [
    "否认冠心病",
    "否认高血压",
    "否认糖尿病",
    "否认肝炎",
    "否认结核"
  ],
  "pmh_allergy_history": [
    "无药物过敏",
    "无食物过敏"
  ],
  "pmh_surgery_trauma_history": [
    "否认重大外伤史",
    "否认手术史",
    "否认输血史"
  ],
  "ph_smoking": "吸烟30余年，约20支/天，现已戒2年",
  "ph_drinking": "偶有饮酒史，现已戒2年",
  "oh_menarche_age": null,
  "oh_menopause_age": null,
  "oh_pregnancies": null,
  "fh_text": "父亲去世（具体不详），母亲健在。兄弟2人，1个弟弟健在。家族中无遗传病病史及类似病史。",
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36.6,
  "vs_pulse_bpm": 80,
  "vs_respiration_rpm": 20,
  "vs_systolic_bp_mmhg": 132,
  "vs_diastolic_bp_mmhg": 82,
  "pe_general_condition": "中年男性，发育正常，营养中等，神志清楚，自主体位，正常面容，检查合作。",
  "pe_skin_mucosa": "全身皮肤、黏膜无苍白、紫绀、黄染，无水肿、皮疹、瘀点、紫癜、皮下结节，无蜘蛛痣、肝掌。",
  "pe_lymph_nodes": "全身浅表淋巴结未触及肿大，局部皮肤无红肿、波动、压痛、瘘管。左侧锁骨上触及大约3×2cm肿物，质硬，固定。",
  "pe_lungs": "胸廓对称，无畸形，胸骨无压痛，胸壁无皮下气肿及静脉曲张，呼吸节律正常。双侧呼吸活动度对称，双侧语音震颤正常，无胸膜摩擦感、皮下捻发感；叩诊双肺呈清音，两肺下界在锁骨中线第六肋间，腋中线第八肋间，肩胛下角线第十肋间，肺下界活动度正常。双肺呼吸音粗，未闻及干湿性罗音，未闻及胸膜摩擦音。",
  "pe_heart": "心前区无隆起，心尖搏动在锁骨中线第五肋间隙内侧0.5cm处，搏动范围及强度无异常，无震颤及心包摩擦感。心脏左右浊音界正常。心音正常，心率76次/分，心律规整，各瓣膜听诊区无心音分裂、额外心音、杂音，无心包摩擦音。无毛细血管搏动、射枪音、水冲脉和无动脉异常搏动。",
  "pe_abdomen": "腹部对称、平坦，无肠型及胃肠蠕动波，无皮疹、色素、条纹，无腹壁静脉曲张，无疝和局部隆起，腹部柔软，腹无压痛、反跳痛，未触及包块，无液波震颤，肝脾肋下未触及。墨菲氏征阴性。腹部叩诊鼓音，肝上界在右锁骨中线第五肋间，肝肾区无叩痛，无移动性浊音。肠鸣音正常4次/分，无振水音，无血管杂音。",
  "pe_extremities": "脊柱生理弯曲正常，无畸形，无压痛和叩击痛，活动自如，腰骶部无异常。四肢无畸形，肌张力正常，关节无红肿，活动正常，双下肢无水肿及静脉曲张。",
  "pe_nervous_system": "腹壁反射、肱二、三头肌肌腱反射、膝腱反射、跟腱反射均正常存在；Babinski征阴性，Gordon征阴性，Oppenheim征阴性，Hoffmann征阴性；Kernig征阴性，Brudzinski征阴性。",
  "pe_specialist_exam": "双肺呼吸音粗，未闻及干湿性罗音，未闻及胸膜摩擦音。心音正常，心率76次/分，心律规整，腹部柔软，腹无压痛、反跳痛，未触及包块，无液波震颤，肝脾肋下未触及。",
  "pe_ecog_score": null,
  "pat_text": "2023-03-30 PET/CT：左肺上叶高代谢占位，考虑肺癌，多发淋巴结转移。2023-04-03 病理：左锁骨上淋巴结穿刺活检见分化差的癌，不除外肺非小细胞癌转移。2023-04-06 胸部CT：左肺上叶恶性肿瘤并累及邻近胸膜，多发淋巴结转移。2023-04-10 病理：左肺上叶穿刺活检非小细胞癌伴坏死，部分区域伴鳞状细胞癌分化。2023-04-05 基因检测：未检出与靶向治疗相关基因突变；PD-L1 TPS约3%。2025-12-27 颈+胸部增强CT：左肺团片影较前增大，左肺门及纵隔多发肿大淋巴结较前部分增大。",
  "pat_items": [
    "2023-03-30 PET/CT：左肺上叶高代谢占位，考虑肺癌（并累及邻近胸膜），（左侧颈部V区、左锁骨上、纵隔、左肺门10区、左肺内11-12区）多发淋巴结转移",
    "2023-04-03 病理：（左锁骨上淋巴结穿刺活检）纤维组织内查见分化差的癌，结合免疫组化及病史，不除外肺非小细胞癌转移",
    "2023-04-03 颅脑MRI：脑内多发缺血灶，建议复查双侧上颌窦囊肿",
    "2023-04-06 胸部CT：左肺上叶恶性肿瘤并累及邻近胸膜，左锁骨上、左肺门及纵隔多发淋巴结转移",
    "2023-04-10 病理：（左肺上叶穿刺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化",
    "2023-04-05 基因检测：未检出与靶向治疗相关基因突变；PD-L1检测：TPS约3%",
    "2025-12-27 颈+胸部增强CT：左肺团片影，较前2025-09-03增大；左肺门及纵隔多发肿大淋巴结，较前部分增大"
  ],
  "preliminary_diagnoses": [
    {
      "name": "左肺上叶癌腺癌cT3N3MOIIIC期",
      "diagnosis_type": "西医",
      "is_primary": true
    },
    {
      "name": "纵隔淋巴结转移",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "锁骨上淋巴结转移",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "肺门淋巴结转移",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "颈部淋巴结转移",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "肺气肿",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "鼻窦炎",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "肝囊肿",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "肾囊肿",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "上颌窦囊肿",
      "diagnosis_type": "西医",
      "is_primary": false
    }
  ],
  "department": null
}
2026-08-10 18:07:48,177 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-03-04]
2026-08-10 18:07:48,180 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1640693, prompt_len=2768
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共32行）
["2026-03-04 15:46 入院记录", "性别：男", "职业：其他", "年龄：57岁", "入院时间：2026-03-04 15:38:00", "民族：汉族", "记录时间：2026-03-04 15:46", "婚姻：已婚", "病史陈述者：患者本人及家属", "主诉：确诊左肺癌2年余，双下肢疼痛1周。", "现病史：患者2年余前查体发现左颈部肿物，约豆粒大小，无疼痛，偶有咳嗽、咳痰，无痰中带血丝，活动后偶感胸闷、憋气，无咯血，无胸痛，无发热。后肿物逐渐增大，遂就诊于我院，2023-03-30行", "PET/CT：1，左肺上叶高代谢占位，考虑肺癌（并累及邻近胸膜），（左侧颈部V区、左锁骨上、纵隔、左肺门10区、左肺内11-12区）多发淋巴结转移；建议病理学检查；左肺门10区淋巴结旁肺组织见网格样密度", "增高影，轻度PDG代谢增高，建议结合临床并复查。未行特殊治疗。后就诊于我科，2023-04-03行快速石蜡病理诊断：（左锁骨上淋巴结穿刺活检）纤维组织内查见分化差的癌，结合免疫组化及病史，不除外肺非", "小细胞癌转移。经齐鲁医院会诊：倾向肺腺癌。免疫组化结果：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（-）、P40（灶+）。2023-04-06行胸部增强CT：左肺上叶恶性肿瘤并累及邻近胸膜，左锁骨上、左", "肺门及纵隔多发淋巴结转移。快速石蜡病理诊断：（左肺上叶穿刺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，特殊染色待补充报告。免疫组化结果：CK5/6（-）、P40（部分+）、", "TTF-1（-）、NapsinA（-）、CK7（+）。ALK（D5F3）：阴性；（兔单克隆阴性对照：阴性；阳性对照：阳性）。2023-04-07至2023-06-30行替雷利珠单抗200mg免疫治疗+贝伐珠单抗注射液900.00mg靶向治", "疗，联合卡铂500.00mg d1+培美曲塞二钠850.00mg d1化疗5周期。排除禁忌，患者于2023-07-06行胸部IMRT放疗，具体：IMRT,PTV 60GY/30F，末次放疗时间为2023-08-09。2023-07-19行卡铂500mg化疗联合恩度", "靶向及替雷利珠单抗免疫治疗。2023-08-10予以患者恩度靶向及替雷利珠单抗免疫治疗。2024-09-30行顺铂40mgd1化疗，联合贝伐珠单抗注射液靶向、替雷利珠单抗免疫治疗。2024-11-6复查CT示：左肺上叶团片", "影，较前2024.07.10范围增大，较2024.10.23示实性成分增多。病情较前进展。2024-11-07、2024-12-3行贝伐珠单抗800mg+替雷丽珠单抗200mg+顺铂80.00mg d1+紫杉醇脂质体270.00mg d1全身化疗2周期，因患", "者消化道反应重，2025-1-16、2025-2-6行贝伐珠单抗800mg+替雷丽珠单抗200mg+顺铂60.00mg d1+紫杉醇脂质体240.00mg d1全身化疗2周。因出现消化道反应III级，后2025-3-25改行紫杉醇聚合物胶束300mgd1联", "合卡铂400mgd1化疗，并行贝伐珠单抗800mg靶向联合替雷丽珠单抗200mg免疫治疗，2025-4-15行贝伐珠单抗800mgd0+替雷丽珠单抗200mgd0+紫杉醇聚合物胶束300mgd1+卡铂500mgd1，过程顺利。因医院紫杉醇聚合", "物胶束无货，2025-5-7行顺铂80.00mg d1+紫杉醇脂质体270mg d1化疗1周期，2025-7-28至2025-12按期行卡铂500mg d1+紫杉醇聚合物胶束300mg，并行贝伐珠单抗注射液400mg靶向、（百泽安）替雷利珠单抗注射液", "200.00mg d1免疫治疗。2026-01-19行注射用紫杉醇脂质体270mgd1+卡铂 500.00mg d1化疗1周期。2025-12-27行颈+胸部增强CT：肺癌复查：左肺团片影，较前2025-09-03增大；左肺门及纵隔多发肿大淋巴结，较", "前部分增大。病情较前进展。1周前患者无明显诱因出现双下肢疼痛，间断性，走路踩棉花样，影响夜间睡眠。现为行进一步治疗收住我科。自发病以来，精神可，饮食、睡眠欠佳，大小便无异常，近1个月体重", "较前无明显变化。", "既往史：否认“冠心病、高血压、糖尿病”病史。否认“肝炎、结核”等传染病病史及密切接触史。否认重大外伤史，否认手术史，否认输血史。无药物及食物过敏。预防接种随当地进行。", "个人史：生于原籍，无外地久居史，无疫区长期居住史，无聚集性发病。生活规律，吸烟30余年，约20支/天，偶有饮酒史，现烟酒均已戒2年，无毒物、粉尘及放射性物质接触史，无冶游史，无重大精神创", "伤史。全程接种新冠疫苗。", "婚育史：23岁结婚，配偶健在，育2女，女儿健康。", "家族史：父亲去世（具体不详），母亲健在。兄弟2人，1个弟弟健在。家族中无遗传病病史及类似病史。", "体 格 检 查", "T:36.6℃ P:80次/分 R:20次/分 Bp:132/82mmHg VTE:3分"]

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
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord API raw response (len=3448):
[
	{"text": "2026-03-04 15:46 入院记录", "bbox": [28, 160, 170, 178]},
	{"text": "性别：男", "bbox": [218, 217, 266, 237]},
	{"text": "职业：其他", "bbox": [499, 217, 559, 237]},
	{"text": "年龄：57岁", "bbox": [218, 245, 280, 265]},
	{"text": "入院时间：2026-03-04 15:38:00", "bbox": [499, 245, 691, 265]},
	{"text": "民族：汉族", "bbox": [218, 273, 280, 293]},
	{"text": "记录时间：2026-03-04 15:46", "bbox": [499, 273, 670, 293]},
	{"text": "婚姻：已婚", "bbox": [218, 303, 280, 323]},
	{"text": "病史陈述者：患者本人及家属", "bbox": [499, 303, 665, 323]},
	{"text": "主诉：确诊左肺癌2年余，双下肢疼痛1周。", "bbox": [48, 332, 241, 349]},
	{"text": "现病史：患者2年余前查体发现左颈部肿物，约豆粒大小，无疼痛，偶有咳嗽、咳痰，无痰中带血丝，活动后偶感胸闷、憋气，无咯血，无胸痛，无发热。后肿物逐渐增大，遂就诊于我院，2023-03-30行", "bbox": [43, 356, 948, 374]},
	{"text": "PET/CT：1，左肺上叶高代谢占位，考虑肺癌（并累及邻近胸膜），（左侧颈部V区、左锁骨上、纵隔、左肺门10区、左肺内11-12区）多发淋巴结转移；建议病理学检查；左肺门10区淋巴结旁肺组织见网格样密度", "bbox": [28, 379, 961, 397]},
	{"text": "增高影，轻度PDG代谢增高，建议结合临床并复查。未行特殊治疗。后就诊于我科，2023-04-03行快速石蜡病理诊断：（左锁骨上淋巴结穿刺活检）纤维组织内查见分化差的癌，结合免疫组化及病史，不除外肺非", "bbox": [28, 402, 961, 420]},
	{"text": "小细胞癌转移。经齐鲁医院会诊：倾向肺腺癌。免疫组化结果：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（-）、P40（灶+）。2023-04-06行胸部增强CT：左肺上叶恶性肿瘤并累及邻近胸膜，左锁骨上、左", "bbox": [28, 425, 961, 443]},
	{"text": "肺门及纵隔多发淋巴结转移。快速石蜡病理诊断：（左肺上叶穿刺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，特殊染色待补充报告。免疫组化结果：CK5/6（-）、P40（部分+）、", "bbox": [28, 448, 955, 466]},
	{"text": "TTF-1（-）、NapsinA（-）、CK7（+）。ALK（D5F3）：阴性；（兔单克隆阴性对照：阴性；阳性对照：阳性）。2023-04-07至2023-06-30行替雷利珠单抗200mg免疫治疗+贝伐珠单抗注射液900.00mg靶向治", "bbox": [28, 471, 950, 489]},
	{"text": "疗，联合卡铂500.00mg d1+培美曲塞二钠850.00mg d1化疗5周期。排除禁忌，患者于2023-07-06行胸部IMRT放疗，具体：IMRT,PTV 60GY/30F，末次放疗时间为2023-08-09。2023-07-19行卡铂500mg化疗联合恩度", "bbox": [28, 494, 961, 512]},
	{"text": "靶向及替雷利珠单抗免疫治疗。2023-08-10予以患者恩度靶向及替雷利珠单抗免疫治疗。2024-09-30行顺铂40mgd1化疗，联合贝伐珠单抗注射液靶向、替雷利珠单抗免疫治疗。2024-11-6复查CT示：左肺上叶团片", "bbox": [28, 517, 961, 535]},
	{"text": "影，较前2024.07.10范围增大，较2024.10.23示实性成分增多。病情较前进展。2024-11-07、2024-12-3行贝伐珠单抗800mg+替雷丽珠单抗200mg+顺铂80.00mg d1+紫杉醇脂质体270.00mg d1全身化疗2周期，因患", "bbox": [28, 540, 961, 558]},
	{"text": "者消化道反应重，2025-1-16、2025-2-6行贝伐珠单抗800mg+替雷丽珠单抗200mg+顺铂60.00mg d1+紫杉醇脂质体240.00mg d1全身化疗2周。因出现消化道反应III级，后2025-3-25改行紫杉醇聚合物胶束300mgd1联", "bbox": [28, 563, 965, 581]},
	{"text": "合卡铂400mgd1化疗，并行贝伐珠单抗800mg靶向联合替雷丽珠单抗200mg免疫治疗，2025-4-15行贝伐珠单抗800mgd0+替雷丽珠单抗200mgd0+紫杉醇聚合物胶束300mgd1+卡铂500mgd1，过程顺利。因医院紫杉醇聚合", "bbox": [28, 586, 965, 604]},
	{"text": "物胶束无货，2025-5-7行顺铂80.00mg d1+紫杉醇脂质体270mg d1化疗1周期，2025-7-28至2025-12按期行卡铂500mg d1+紫杉醇聚合物胶束300mg，并行贝伐珠单抗注射液400mg靶向、（百泽安）替雷利珠单抗注射液", "bbox": [28, 609, 965, 627]},
	{"text": "200.00mg d1免疫治疗。2026-01-19行注射用紫杉醇脂质体270mgd1+卡铂 500.00mg d1化疗1周期。2025-12-27行颈+胸部增强CT：肺癌复查：左肺团片影，较前2025-09-03增大；左肺门及纵隔多发肿大淋巴结，较", "bbox": [28, 632, 965, 650]},
	{"text": "前部分增大。病情较前进展。1周前患者无明显诱因出现双下肢疼痛，间断性，走路踩棉花样，影响夜间睡眠。现为行进一步治疗收住我科。自发病以来，精神可，饮食、睡眠欠佳，大小便无异常，近1个月体重", "bbox": [28, 655, 959, 673]},
	{"text": "较前无明显变化。", "bbox": [28, 684, 103, 702]},
	{"text": "既往史：否认“冠心病、高血压、糖尿病”病史。否认“肝炎、结核”等传染病病史及密切接触史。否认重大外伤史，否认手术史，否认输血史。无药物及食物过敏。预防接种随当地进行。", "bbox": [48, 708, 880, 726]},
	{"text": "个人史：生于原籍，无外地久居史，无疫区长期居住史，无聚集性发病。生活规律，吸烟30余年，约20支/天，偶有饮酒史，现烟酒均已戒2年，无毒物、粉尘及放射性物质接触史，无冶游史，无重大精神创", "bbox": [48, 731, 961, 749]},
	{"text": "伤史。全程接种新冠疫苗。", "bbox": [28, 755, 142, 773]},
	{"text": "婚育史：23岁结婚，配偶健在，育2女，女儿健康。", "bbox": [48, 778, 268, 796]},
	{"text": "家族史：父亲去世（具体不详），母亲健在。兄弟2人，1个弟弟健在。家族中无遗传病病史及类似病史。", "bbox": [48, 801, 500, 819]},
	{"text": "体 格 检 查", "bbox": [438, 825, 531, 843]},
	{"text": "T:36.6℃ P:80次/分 R:20次/分 Bp:132/82mmHg VTE:3分", "bbox": [327, 848, 635, 866]}
]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord API: raw_items=32, valid_items=32, elapsed=21.8s
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[0]: text=2026-03-04 15:46 入院记录, bbox=[28, 160, 170, 178]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[1]: text=性别：男, bbox=[218, 217, 266, 237]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[2]: text=职业：其他, bbox=[499, 217, 559, 237]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：57岁, bbox=[218, 245, 280, 265]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[4]: text=入院时间：2026-03-04 15:38:00, bbox=[499, 245, 691, 265]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[5]: text=民族：汉族, bbox=[218, 273, 280, 293]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[6]: text=记录时间：2026-03-04 15:46, bbox=[499, 273, 670, 293]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[7]: text=婚姻：已婚, bbox=[218, 303, 280, 323]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[8]: text=病史陈述者：患者本人及家属, bbox=[499, 303, 665, 323]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[9]: text=主诉：确诊左肺癌2年余，双下肢疼痛1周。, bbox=[48, 332, 241, 349]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[10]: text=现病史：患者2年余前查体发现左颈部肿物，约豆粒大小，无疼痛，偶有咳嗽、咳痰，无痰中带血丝，活动后偶感胸闷、憋气，无咯血，无胸痛，无发热。后肿物逐渐增大，遂就诊于我院，2023-03-30行, bbox=[43, 356, 948, 374]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[11]: text=PET/CT：1，左肺上叶高代谢占位，考虑肺癌（并累及邻近胸膜），（左侧颈部V区、左锁骨上、纵隔、左肺门10区、左肺内11-12区）多发淋巴结转移；建议病理学检查；左肺门10区淋巴结旁肺组织见网格样密度, bbox=[28, 379, 961, 397]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[12]: text=增高影，轻度PDG代谢增高，建议结合临床并复查。未行特殊治疗。后就诊于我科，2023-04-03行快速石蜡病理诊断：（左锁骨上淋巴结穿刺活检）纤维组织内查见分化差的癌，结合免疫组化及病史，不除外肺非, bbox=[28, 402, 961, 420]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[13]: text=小细胞癌转移。经齐鲁医院会诊：倾向肺腺癌。免疫组化结果：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（-）、P40（灶+）。2023-04-06行胸部增强CT：左肺上叶恶性肿瘤并累及邻近胸膜，左锁骨上、左, bbox=[28, 425, 961, 443]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[14]: text=肺门及纵隔多发淋巴结转移。快速石蜡病理诊断：（左肺上叶穿刺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，特殊染色待补充报告。免疫组化结果：CK5/6（-）、P40（部分+）、, bbox=[28, 448, 955, 466]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[15]: text=TTF-1（-）、NapsinA（-）、CK7（+）。ALK（D5F3）：阴性；（兔单克隆阴性对照：阴性；阳性对照：阳性）。2023-04-07至2023-06-30行替雷利珠单抗200mg免疫治疗+贝伐珠单抗注射液900.00mg靶向治, bbox=[28, 471, 950, 489]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[16]: text=疗，联合卡铂500.00mg d1+培美曲塞二钠850.00mg d1化疗5周期。排除禁忌，患者于2023-07-06行胸部IMRT放疗，具体：IMRT,PTV 60GY/30F，末次放疗时间为2023-08-09。2023-07-19行卡铂500mg化疗联合恩度, bbox=[28, 494, 961, 512]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[17]: text=靶向及替雷利珠单抗免疫治疗。2023-08-10予以患者恩度靶向及替雷利珠单抗免疫治疗。2024-09-30行顺铂40mgd1化疗，联合贝伐珠单抗注射液靶向、替雷利珠单抗免疫治疗。2024-11-6复查CT示：左肺上叶团片, bbox=[28, 517, 961, 535]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[18]: text=影，较前2024.07.10范围增大，较2024.10.23示实性成分增多。病情较前进展。2024-11-07、2024-12-3行贝伐珠单抗800mg+替雷丽珠单抗200mg+顺铂80.00mg d1+紫杉醇脂质体270.00mg d1全身化疗2周期，因患, bbox=[28, 540, 961, 558]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[19]: text=者消化道反应重，2025-1-16、2025-2-6行贝伐珠单抗800mg+替雷丽珠单抗200mg+顺铂60.00mg d1+紫杉醇脂质体240.00mg d1全身化疗2周。因出现消化道反应III级，后2025-3-25改行紫杉醇聚合物胶束300mgd1联, bbox=[28, 563, 965, 581]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[20]: text=合卡铂400mgd1化疗，并行贝伐珠单抗800mg靶向联合替雷丽珠单抗200mg免疫治疗，2025-4-15行贝伐珠单抗800mgd0+替雷丽珠单抗200mgd0+紫杉醇聚合物胶束300mgd1+卡铂500mgd1，过程顺利。因医院紫杉醇聚合, bbox=[28, 586, 965, 604]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[21]: text=物胶束无货，2025-5-7行顺铂80.00mg d1+紫杉醇脂质体270mg d1化疗1周期，2025-7-28至2025-12按期行卡铂500mg d1+紫杉醇聚合物胶束300mg，并行贝伐珠单抗注射液400mg靶向、（百泽安）替雷利珠单抗注射液, bbox=[28, 609, 965, 627]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[22]: text=200.00mg d1免疫治疗。2026-01-19行注射用紫杉醇脂质体270mgd1+卡铂 500.00mg d1化疗1周期。2025-12-27行颈+胸部增强CT：肺癌复查：左肺团片影，较前2025-09-03增大；左肺门及纵隔多发肿大淋巴结，较, bbox=[28, 632, 965, 650]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[23]: text=前部分增大。病情较前进展。1周前患者无明显诱因出现双下肢疼痛，间断性，走路踩棉花样，影响夜间睡眠。现为行进一步治疗收住我科。自发病以来，精神可，饮食、睡眠欠佳，大小便无异常，近1个月体重, bbox=[28, 655, 959, 673]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[24]: text=较前无明显变化。, bbox=[28, 684, 103, 702]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[25]: text=既往史：否认“冠心病、高血压、糖尿病”病史。否认“肝炎、结核”等传染病病史及密切接触史。否认重大外伤史，否认手术史，否认输血史。无药物及食物过敏。预防接种随当地进行。, bbox=[48, 708, 880, 726]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[26]: text=个人史：生于原籍，无外地久居史，无疫区长期居住史，无聚集性发病。生活规律，吸烟30余年，约20支/天，偶有饮酒史，现烟酒均已戒2年，无毒物、粉尘及放射性物质接触史，无冶游史，无重大精神创, bbox=[48, 731, 961, 749]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[27]: text=伤史。全程接种新冠疫苗。, bbox=[28, 755, 142, 773]
2026-08-10 18:08:10,009 INFO     29 [qwen-vl-text] coord item[28]: text=婚育史：23岁结婚，配偶健在，育2女，女儿健康。, bbox=[48, 778, 268, 796]
2026-08-10 18:08:10,010 INFO     29 [qwen-vl-text] coord item[29]: text=家族史：父亲去世（具体不详），母亲健在。兄弟2人，1个弟弟健在。家族中无遗传病病史及类似病史。, bbox=[48, 801, 500, 819]
2026-08-10 18:08:10,010 INFO     29 [qwen-vl-text] coord item[30]: text=体 格 检 查, bbox=[438, 825, 531, 843]
2026-08-10 18:08:10,010 INFO     29 [qwen-vl-text] coord item[31]: text=T:36.6℃ P:80次/分 R:20次/分 Bp:132/82mmHg VTE:3分, bbox=[327, 848, 635, 866]
2026-08-10 18:08:10,010 INFO     29 [qwen-vl-text] page=3 — 32/32 coords, api_time=21.8s
2026-08-10 18:08:10,013 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1851555, prompt_len=2714
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共30行）
["个人史：生于原籍，无外地久居史，无疫区长期居住史，无聚集性发病。生活规律，吸烟30余年，约20支/天，偶有饮酒史，现烟酒均已戒2年，无毒物、粉尘及放射性物质接触史，无冶游史，无重大精神创伤史，全程接种新冠疫苗。", "婚育史：23岁结婚，配偶健在，育2女，女儿健康。", "家族史：父亲去世（具体不详），母亲健在。兄弟2人，1个弟弟健在。家族中无遗传病病史及类似病史。", "体格检查", "T:36.6℃ P:80次/分 R:20次/分 Bp:132/82mmHg VTE:3分", "H:168cm W:65kg S:1.71平方米 NRS:0分 PS:1分 NRS-2002:1分", "中年男性，发育正常，营养中等，神志清楚，自主体位，正常面容，检查合作。全身皮肤、黏膜无苍白、紫绀、黄染，无水肿、皮疹、瘀点、紫癜、皮下结节，无蜘蛛痣、肝掌。全身浅表淋巴结未触及肿大，", "局部皮肤无红肿、波动、压痛、瘘管。左侧锁骨上触及大约3×2cm肿物，质硬，固定，颈部柔软，双侧对称，颈静脉无怒张，肝颈静脉回流征阴性，无颈动脉异常搏动，气管位置居中，甲状腺无肿大，胸廓对", "称，无畸形，胸骨无压痛，胸壁无皮下气肿及静脉曲张，呼吸节律正常。双侧呼吸活动度对称，双侧语音震颤正常，无胸膜摩擦感、皮下捻发感；叩诊双肺呈清音，两肺下界在锁骨中线第六肋间，腋中线第八肋", "间，肩胛下角线第十肋间，肺下界活动度正常。双肺呼吸音粗，未闻及干湿性罗音，未闻及胸膜摩擦音。心前区无隆起，心尖搏动在锁骨中线第五肋间隙内侧0.5cm处，搏动范围及强度无异常，无震颤及心包摩擦", "感。心脏左右浊音界正常。心音正常，心率76次/分，心律规整，各瓣膜听诊区无心音分裂、额外心音、杂音，无心包摩擦音。无毛细血管搏动、射枪音、水冲脉和无动脉异常搏动。腹部对称、平坦，无肠型及胃", "肠蠕动波，无皮疹、色素、条纹，无腹壁静脉曲张，无疝和局部隆起，腹部柔软，腹无压痛、反跳痛，未触及包块，无液波震颤，肝脾肋下未触及。墨菲氏征阴性。腹部叩诊鼓音，肝上界在右锁骨中线第五肋", "间，肝肾区无叩痛，无移动性浊音。肠鸣音正常4次/分，无振水音，无血管杂音。肛门直肠及外生殖器未检查。脊柱生理弯曲正常，无畸形，无压痛和叩击痛，活动自如，腰骶部无异常。四肢无畸形，肌张力正", "常，关节无红肿，活动正常，双下肢无水肿及静脉曲张。腹壁反射、肱二、三头肌肌腱反射、膝腱反射、跟腱反射均正常存在；Babinski征阴性，Gordon征阴性，Oppenheim征阴性，Hoffmann征阴性；Kernig征阴", "性，Brudzinski征阴性。", "专科检查：双肺呼吸音粗，未闻及干湿性罗音，未闻及胸膜摩擦音。心音正常，心率76次/分，心律规整，腹部柔软，腹无压痛、反跳痛，未触及包块，无液波震颤，肝脾肋下未触及。", "辅助检查", "检查日期 检查项目 结果（检查医院）", "2023-03-30 PET/CT：1，左肺上叶高代谢占位，考虑肺癌（并累及邻近胸膜），（左侧颈部V区、左锁骨上、纵隔、左肺门10区、左肺内11-12区）多发淋巴结转移；建议病理学检查；左肺门", "10区淋巴结旁肺组织见网格样密度增高影，轻度PDG代谢增高，建议结合临床并复查。2.双肺肺气肿；双肺少许纤维条索灶。3.副鼻窦炎（双侧上颌窦、右侧筛窦）。4.冠状动脉钙化灶。5.十二指肠圈小憩室。6.", "肝脏囊肿。7.左肾囊肿。8.脊椎骨质增生；骶3水平椎管囊肿。（本院）", "2023-04-03 （左锁骨上淋巴结穿刺活检）纤维组织内查见分化差的癌，结合免疫组化及病史，不除外肺非小细胞癌转移。免疫组化结果：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（-）、", "P40（灶+）。（本院）经齐鲁医院会诊：倾向肺腺癌。", "2023-04-03 颅脑磁共振平扫+DVI+增强扫描MRI：脑内多发缺血灶，建议复查双侧上颌窦囊肿。（本院）", "2023-04-06 胸部CT增强扫描CT：1.左肺上叶恶性肿瘤并累及邻近胸膜，左锁骨上、左肺门及纵隔多发淋巴结转移 2.双肺肺气肿；双肺少许纤维条索灶 3.冠状动脉钙化灶 4.扫及肝囊肿、左", "肾囊肿。（本院）", "2023-04-10 快速石蜡病理诊断：（左肺上叶穿刺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，特殊染色待补充报告。免疫组化结果：CK5/6（-）、P40（部分", "+）、TTF-1（-）、NapsinA（-）、CK7（+）。ALK（D5F3）：阴性；（免单克隆阴性对照：阴性；阳性对照：阳性）。（本院）", "2023-04-05 基因检测：未检出与靶向治疗相关基因突变；PD-L1检测：TPS约3%。（赛泽检验）", "2023-07-20 胸部CT：1.肺癌复查：左肺上叶占位，较前（2023-06-30）范围缩小；左锁骨上、左肺门及纵隔多发淋巴结转移，较前变化不大 2.双肺肺气肿；双肺少许纤维条索灶 3.主动脉及"]

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
2026-08-10 18:08:28,723 INFO     29 [qwen-vl-text] coord API raw response (len=3309):
[
	{"text": "个人史：生于原籍，无外地久居史，无疫区长期居住史，无聚集性发病。生活规律，吸烟30余年，约20支/天，偶有饮酒史，现烟酒均已戒2年，无毒物、粉尘及放射性物质接触史，无冶游史，无重大精神创伤史，全程接种新冠疫苗。", "bbox": [28, 134, 975, 175]},
	{"text": "婚育史：23岁结婚，配偶健在，育2女，女儿健康。", "bbox": [47, 181, 281, 200]},
	{"text": "家族史：父亲去世（具体不详），母亲健在。兄弟2人，1个弟弟健在。家族中无遗传病病史及类似病史。", "bbox": [47, 205, 521, 224]},
	{"text": "体格检查", "bbox": [458, 231, 555, 249]},
	{"text": "T:36.6℃ P:80次/分 R:20次/分 Bp:132/82mmHg VTE:3分", "bbox": [341, 255, 660, 273]},
	{"text": "H:168cm W:65kg S:1.71平方米 NRS:0分 PS:1分 NRS-2002:1分", "bbox": [322, 279, 672, 297]},
	{"text": "中年男性，发育正常，营养中等，神志清楚，自主体位，正常面容，检查合作。全身皮肤、黏膜无苍白、紫绀、黄染，无水肿、皮疹、瘀点、紫癜、皮下结节，无蜘蛛痣、肝掌。全身浅表淋巴结未触及肿大，", "bbox": [27, 304, 972, 324]},
	{"text": "局部皮肤无红肿、波动、压痛、瘘管。左侧锁骨上触及大约3×2cm肿物，质硬，固定，颈部柔软，双侧对称，颈静脉无怒张，肝颈静脉回流征阴性，无颈动脉异常搏动，气管位置居中，甲状腺无肿大，胸廓对", "bbox": [27, 329, 963, 348]},
	{"text": "称，无畸形，胸骨无压痛，胸壁无皮下气肿及静脉曲张，呼吸节律正常。双侧呼吸活动度对称，双侧语音震颤正常，无胸膜摩擦感、皮下捻发感；叩诊双肺呈清音，两肺下界在锁骨中线第六肋间，腋中线第八肋", "bbox": [27, 353, 973, 372]},
	{"text": "间，肩胛下角线第十肋间，肺下界活动度正常。双肺呼吸音粗，未闻及干湿性罗音，未闻及胸膜摩擦音。心前区无隆起，心尖搏动在锁骨中线第五肋间隙内侧0.5cm处，搏动范围及强度无异常，无震颤及心包摩擦", "bbox": [27, 377, 977, 396]},
	{"text": "感。心脏左右浊音界正常。心音正常，心率76次/分，心律规整，各瓣膜听诊区无心音分裂、额外心音、杂音，无心包摩擦音。无毛细血管搏动、射枪音、水冲脉和无动脉异常搏动。腹部对称、平坦，无肠型及胃", "bbox": [27, 401, 976, 420]},
	{"text": "肠蠕动波，无皮疹、色素、条纹，无腹壁静脉曲张，无疝和局部隆起，腹部柔软，腹无压痛、反跳痛，未触及包块，无液波震颤，肝脾肋下未触及。墨菲氏征阴性。腹部叩诊鼓音，肝上界在右锁骨中线第五肋", "bbox": [27, 425, 960, 444]},
	{"text": "间，肝肾区无叩痛，无移动性浊音。肠鸣音正常4次/分，无振水音，无血管杂音。肛门直肠及外生殖器未检查。脊柱生理弯曲正常，无畸形，无压痛和叩击痛，活动自如，腰骶部无异常。四肢无畸形，肌张力正", "bbox": [27, 450, 970, 469]},
	{"text": "常，关节无红肿，活动正常，双下肢无水肿及静脉曲张。腹壁反射、肱二、三头肌肌腱反射、膝腱反射、跟腱反射均正常存在；Babinski征阴性，Gordon征阴性，Oppenheim征阴性，Hoffmann征阴性；Kernig征阴", "bbox": [27, 474, 974, 493]},
	{"text": "性，Brudzinski征阴性。", "bbox": [27, 498, 134, 516]},
	{"text": "专科检查：双肺呼吸音粗，未闻及干湿性罗音，未闻及胸膜摩擦音。心音正常，心率76次/分，心律规整，腹部柔软，腹无压痛、反跳痛，未触及包块，无液波震颤，肝脾肋下未触及。", "bbox": [47, 521, 868, 540]},
	{"text": "辅助检查", "bbox": [452, 546, 547, 564]},
	{"text": "检查日期 检查项目 结果（检查医院）", "bbox": [51, 570, 440, 589]},
	{"text": "2023-03-30 PET/CT：1，左肺上叶高代谢占位，考虑肺癌（并累及邻近胸膜），（左侧颈部V区、左锁骨上、纵隔、左肺门10区、左肺内11-12区）多发淋巴结转移；建议病理学检查；左肺门", "bbox": [47, 594, 964, 613]},
	{"text": "10区淋巴结旁肺组织见网格样密度增高影，轻度PDG代谢增高，建议结合临床并复查。2.双肺肺气肿；双肺少许纤维条索灶。3.副鼻窦炎（双侧上颌窦、右侧筛窦）。4.冠状动脉钙化灶。5.十二指肠圈小憩室。6.", "bbox": [27, 618, 966, 637]},
	{"text": "肝脏囊肿。7.左肾囊肿。8.脊椎骨质增生；骶3水平椎管囊肿。（本院）", "bbox": [27, 642, 342, 661]},
	{"text": "2023-04-03 （左锁骨上淋巴结穿刺活检）纤维组织内查见分化差的癌，结合免疫组化及病史，不除外肺非小细胞癌转移。免疫组化结果：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（-）、", "bbox": [47, 666, 961, 685]},
	{"text": "P40（灶+）。（本院）经齐鲁医院会诊：倾向肺腺癌。", "bbox": [27, 690, 269, 709]},
	{"text": "2023-04-03 颅脑磁共振平扫+DVI+增强扫描MRI：脑内多发缺血灶，建议复查双侧上颌窦囊肿。（本院）", "bbox": [47, 714, 570, 733]},
	{"text": "2023-04-06 胸部CT增强扫描CT：1.左肺上叶恶性肿瘤并累及邻近胸膜，左锁骨上、左肺门及纵隔多发淋巴结转移 2.双肺肺气肿；双肺少许纤维条索灶 3.冠状动脉钙化灶 4.扫及肝囊肿、左", "bbox": [47, 738, 958, 757]},
	{"text": "肾囊肿。（本院）", "bbox": [27, 762, 102, 781]},
	{"text": "2023-04-10 快速石蜡病理诊断：（左肺上叶穿刺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，特殊染色待补充报告。免疫组化结果：CK5/6（-）、P40（部分", "bbox": [47, 786, 945, 805]},
	{"text": "+）、TTF-1（-）、NapsinA（-）、CK7（+）。ALK（D5F3）：阴性；（免单克隆阴性对照：阴性；阳性对照：阳性）。（本院）", "bbox": [27, 810, 598, 829]},
	{"text": "2023-04-05 基因检测：未检出与靶向治疗相关基因突变；PD-L1检测：TPS约3%。（赛泽检验）", "bbox": [47, 834, 527, 853]},
	{"text": "2023-07-20 胸部CT：1.肺癌复查：左肺上叶占位，较前（2023-06-30）范围缩小；左锁骨上、左肺门及纵隔多发淋巴结转移，较前变化不大 2.双肺肺气肿；双肺少许纤维条索灶 3.主动脉及", "bbox": [171, 858, 957, 877]}
]
2026-08-10 18:08:28,723 INFO     29 [qwen-vl-text] coord API: raw_items=30, valid_items=30, elapsed=18.7s
2026-08-10 18:08:28,724 INFO     29 [qwen-vl-text] coord item[0]: text=个人史：生于原籍，无外地久居史，无疫区长期居住史，无聚集性发病。生活规律，吸烟30余年，约20支/天，偶有饮酒史，现烟酒均已戒2年，无毒物、粉尘及放射性物质接触史，无冶游史，无重大精神创伤史，全程接种新冠疫苗。, bbox=[28, 134, 975, 175]
2026-08-10 18:08:28,724 INFO     29 [qwen-vl-text] coord item[1]: text=婚育史：23岁结婚，配偶健在，育2女，女儿健康。, bbox=[47, 181, 281, 200]
2026-08-10 18:08:28,724 INFO     29 [qwen-vl-text] coord item[2]: text=家族史：父亲去世（具体不详），母亲健在。兄弟2人，1个弟弟健在。家族中无遗传病病史及类似病史。, bbox=[47, 205, 521, 224]
2026-08-10 18:08:28,724 INFO     29 [qwen-vl-text] coord item[3]: text=体格检查, bbox=[458, 231, 555, 249]
2026-08-10 18:08:28,724 INFO     29 [qwen-vl-text] coord item[4]: text=T:36.6℃ P:80次/分 R:20次/分 Bp:132/82mmHg VTE:3分, bbox=[341, 255, 660, 273]
2026-08-10 18:08:28,724 INFO     29 [qwen-vl-text] coord item[5]: text=H:168cm W:65kg S:1.71平方米 NRS:0分 PS:1分 NRS-2002:1分, bbox=[322, 279, 672, 297]
2026-08-10 18:08:28,724 INFO     29 [qwen-vl-text] coord item[6]: text=中年男性，发育正常，营养中等，神志清楚，自主体位，正常面容，检查合作。全身皮肤、黏膜无苍白、紫绀、黄染，无水肿、皮疹、瘀点、紫癜、皮下结节，无蜘蛛痣、肝掌。全身浅表淋巴结未触及肿大，, bbox=[27, 304, 972, 324]
2026-08-10 18:08:28,724 INFO     29 [qwen-vl-text] coord item[7]: text=局部皮肤无红肿、波动、压痛、瘘管。左侧锁骨上触及大约3×2cm肿物，质硬，固定，颈部柔软，双侧对称，颈静脉无怒张，肝颈静脉回流征阴性，无颈动脉异常搏动，气管位置居中，甲状腺无肿大，胸廓对, bbox=[27, 329, 963, 348]
2026-08-10 18:08:28,724 INFO     29 [qwen-vl-text] coord item[8]: text=称，无畸形，胸骨无压痛，胸壁无皮下气肿及静脉曲张，呼吸节律正常。双侧呼吸活动度对称，双侧语音震颤正常，无胸膜摩擦感、皮下捻发感；叩诊双肺呈清音，两肺下界在锁骨中线第六肋间，腋中线第八肋, bbox=[27, 353, 973, 372]
2026-08-10 18:08:28,724 INFO     29 [qwen-vl-text] coord item[9]: text=间，肩胛下角线第十肋间，肺下界活动度正常。双肺呼吸音粗，未闻及干湿性罗音，未闻及胸膜摩擦音。心前区无隆起，心尖搏动在锁骨中线第五肋间隙内侧0.5cm处，搏动范围及强度无异常，无震颤及心包摩擦, bbox=[27, 377, 977, 396]
2026-08-10 18:08:28,724 INFO     29 [qwen-vl-text] coord item[10]: text=感。心脏左右浊音界正常。心音正常，心率76次/分，心律规整，各瓣膜听诊区无心音分裂、额外心音、杂音，无心包摩擦音。无毛细血管搏动、射枪音、水冲脉和无动脉异常搏动。腹部对称、平坦，无肠型及胃, bbox=[27, 401, 976, 420]
2026-08-10 18:08:28,724 INFO     29 [qwen-vl-text] coord item[11]: text=肠蠕动波，无皮疹、色素、条纹，无腹壁静脉曲张，无疝和局部隆起，腹部柔软，腹无压痛、反跳痛，未触及包块，无液波震颤，肝脾肋下未触及。墨菲氏征阴性。腹部叩诊鼓音，肝上界在右锁骨中线第五肋, bbox=[27, 425, 960, 444]
2026-08-10 18:08:28,724 INFO     29 [qwen-vl-text] coord item[12]: text=间，肝肾区无叩痛，无移动性浊音。肠鸣音正常4次/分，无振水音，无血管杂音。肛门直肠及外生殖器未检查。脊柱生理弯曲正常，无畸形，无压痛和叩击痛，活动自如，腰骶部无异常。四肢无畸形，肌张力正, bbox=[27, 450, 970, 469]
2026-08-10 18:08:28,724 INFO     29 [qwen-vl-text] coord item[13]: text=常，关节无红肿，活动正常，双下肢无水肿及静脉曲张。腹壁反射、肱二、三头肌肌腱反射、膝腱反射、跟腱反射均正常存在；Babinski征阴性，Gordon征阴性，Oppenheim征阴性，Hoffmann征阴性；Kernig征阴, bbox=[27, 474, 974, 493]
2026-08-10 18:08:28,724 INFO     29 [qwen-vl-text] coord item[14]: text=性，Brudzinski征阴性。, bbox=[27, 498, 134, 516]
2026-08-10 18:08:28,724 INFO     29 [qwen-vl-text] coord item[15]: text=专科检查：双肺呼吸音粗，未闻及干湿性罗音，未闻及胸膜摩擦音。心音正常，心率76次/分，心律规整，腹部柔软，腹无压痛、反跳痛，未触及包块，无液波震颤，肝脾肋下未触及。, bbox=[47, 521, 868, 540]
2026-08-10 18:08:28,725 INFO     29 [qwen-vl-text] coord item[16]: text=辅助检查, bbox=[452, 546, 547, 564]
2026-08-10 18:08:28,725 INFO     29 [qwen-vl-text] coord item[17]: text=检查日期 检查项目 结果（检查医院）, bbox=[51, 570, 440, 589]
2026-08-10 18:08:28,725 INFO     29 [qwen-vl-text] coord item[18]: text=2023-03-30 PET/CT：1，左肺上叶高代谢占位，考虑肺癌（并累及邻近胸膜），（左侧颈部V区、左锁骨上、纵隔、左肺门10区、左肺内11-12区）多发淋巴结转移；建议病理学检查；左肺门, bbox=[47, 594, 964, 613]
2026-08-10 18:08:28,725 INFO     29 [qwen-vl-text] coord item[19]: text=10区淋巴结旁肺组织见网格样密度增高影，轻度PDG代谢增高，建议结合临床并复查。2.双肺肺气肿；双肺少许纤维条索灶。3.副鼻窦炎（双侧上颌窦、右侧筛窦）。4.冠状动脉钙化灶。5.十二指肠圈小憩室。6., bbox=[27, 618, 966, 637]
2026-08-10 18:08:28,725 INFO     29 [qwen-vl-text] coord item[20]: text=肝脏囊肿。7.左肾囊肿。8.脊椎骨质增生；骶3水平椎管囊肿。（本院）, bbox=[27, 642, 342, 661]
2026-08-10 18:08:28,725 INFO     29 [qwen-vl-text] coord item[21]: text=2023-04-03 （左锁骨上淋巴结穿刺活检）纤维组织内查见分化差的癌，结合免疫组化及病史，不除外肺非小细胞癌转移。免疫组化结果：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（-）、, bbox=[47, 666, 961, 685]
2026-08-10 18:08:28,725 INFO     29 [qwen-vl-text] coord item[22]: text=P40（灶+）。（本院）经齐鲁医院会诊：倾向肺腺癌。, bbox=[27, 690, 269, 709]
2026-08-10 18:08:28,725 INFO     29 [qwen-vl-text] coord item[23]: text=2023-04-03 颅脑磁共振平扫+DVI+增强扫描MRI：脑内多发缺血灶，建议复查双侧上颌窦囊肿。（本院）, bbox=[47, 714, 570, 733]
2026-08-10 18:08:28,725 INFO     29 [qwen-vl-text] coord item[24]: text=2023-04-06 胸部CT增强扫描CT：1.左肺上叶恶性肿瘤并累及邻近胸膜，左锁骨上、左肺门及纵隔多发淋巴结转移 2.双肺肺气肿；双肺少许纤维条索灶 3.冠状动脉钙化灶 4.扫及肝囊肿、左, bbox=[47, 738, 958, 757]
2026-08-10 18:08:28,725 INFO     29 [qwen-vl-text] coord item[25]: text=肾囊肿。（本院）, bbox=[27, 762, 102, 781]
2026-08-10 18:08:28,725 INFO     29 [qwen-vl-text] coord item[26]: text=2023-04-10 快速石蜡病理诊断：（左肺上叶穿刺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，特殊染色待补充报告。免疫组化结果：CK5/6（-）、P40（部分, bbox=[47, 786, 945, 805]
2026-08-10 18:08:28,725 INFO     29 [qwen-vl-text] coord item[27]: text=+）、TTF-1（-）、NapsinA（-）、CK7（+）。ALK（D5F3）：阴性；（免单克隆阴性对照：阴性；阳性对照：阳性）。（本院）, bbox=[27, 810, 598, 829]
2026-08-10 18:08:28,725 INFO     29 [qwen-vl-text] coord item[28]: text=2023-04-05 基因检测：未检出与靶向治疗相关基因突变；PD-L1检测：TPS约3%。（赛泽检验）, bbox=[47, 834, 527, 853]
2026-08-10 18:08:28,725 INFO     29 [qwen-vl-text] coord item[29]: text=2023-07-20 胸部CT：1.肺癌复查：左肺上叶占位，较前（2023-06-30）范围缩小；左锁骨上、左肺门及纵隔多发淋巴结转移，较前变化不大 2.双肺肺气肿；双肺少许纤维条索灶 3.主动脉及, bbox=[171, 858, 957, 877]
2026-08-10 18:08:28,726 INFO     29 [qwen-vl-text] page=4 — 30/30 coords, api_time=18.7s
2026-08-10 18:08:28,729 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1212796, prompt_len=1929
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共31行）
["2023-07-20", "胸部CT：1.肺癌复查：左肺上叶占位，较前（2023-06-30）范围缩小；左锁骨上、左肺门及纵隔多发淋巴结转移，较前变化不大2.双肺肺气肿；双肺少许纤维条索灶3.主动脉及", "冠状动脉钙化4.扫及肝囊肿胸部CT平扫，下腹部（肾）CT平扫，上腹部CT平扫，盆腔CT平扫CT（2023-08-11）：1.肺癌复查：左肺上叶占位，范围较前（2023-7-20）减小；左锁骨上、左肺门及纵隔多发稍大淋巴", "结，较前变化不大2.双肺肺气肿；双肺少许条索灶3.主动脉及冠状动脉钙化4.肝囊肿5.左肾稍低密度灶，建议超声检查；左肾囊肿6.十二指肠降段憩室7.右侧髂骨稍高密度灶，建议复查8.考虑骶管（S3-4", "水平）囊肿。（本院）", "2025-03-11", "颈部+胸部增强CT：1.肺癌复查：左肺团片影，较前25.2.6范围相仿；2.双肺微小结节，原左肺新增结节较前略小（im149薄层），转移不除外，余较前相仿，定期复查；3.双肺", "肺气肿；双肺条索灶；4.左肺门及纵隔多发稍大淋巴结，较前相仿；5.主动脉及冠状动脉钙化；心包少量积液；左侧胸膜局限性增厚；6.扫及肝囊肿；左肾囊肿。（本院）", "2025-09-02", "颅脑磁共振成像+DWI（特殊序列成像）MR：考虑脑内多发小缺血灶，较前（2024-11-8）变化不著，建议复查。左侧上颌窦囊肿。（本院）", "2025-09-03", "颈部CT增强扫描，胸部CT增强扫描，上腹部CT增强扫描，盆腔CT增强扫描，下腹部CT增强扫描：1.肺癌复查：左肺团片影，较前2025.05.07范围略增大，建议复查2.双肺微小结节，", "较前变化不大，转移不除外，建议定期复查3.双肺肺气肿；双肺条索灶4.左肺门及纵隔多发稍大淋巴结，较前略大5.主动脉及冠状动脉钙化；心包少量积液；左侧胸膜局限性增厚6.肝囊肿；左肾囊肿7.", "十二指肠降段憩室8.右侧髂骨稍高密度灶，较前2024.11.06变化不大，建议复查9.考虑骶管囊肿10.颈部未见明显异常；扫及双侧上颌窦炎。（本院）", "2025-12-27", "颈+胸部增强CT：1.肺癌复查：左肺团片影，较前2025-09-03增大；周围新发实变及网格影，请结合临床，建议复查；2.双肺小结节及小斑片影，较前部分增大，部分新发，部分", "变化不大，建议定期复查；3.双肺肺气肿；双肺条索灶；双肺胸膜下磨玻璃密度影，请结合临床随诊复查；4.左肺门及纵隔多发肿大淋巴结，较前部分增大；5.主动脉及冠状动脉钙化；心包少量积液；左侧胸", "膜局限性增厚；左侧胸腔少量积液；6.扫及肝囊肿；左肾囊肿7.颈部未见明显异常；扫及双侧上颌窦炎。（本院）", "初步诊断", "1、左肺上叶癌腺癌cT3N3MOIIIC期", "纵隔淋巴结转移", "锁骨上淋巴结转移", "肺门淋巴结转移", "颈部淋巴结转移", "2、肺气肿", "3、鼻窦炎", "4、肝囊肿", "5、肾囊肿", "6、上颌窦囊肿", "我审核病史记录内容属实无遗漏，我交给医院的病例资料已收回，患方签字：", "宗茹"]

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
2026-08-10 18:08:45,282 INFO     29 [qwen-vl-text] coord API raw response (len=2574):
[
	{"text": "2023-07-20", "bbox": [40, 168, 92, 184]},
	{"text": "胸部CT：1.肺癌复查：左肺上叶占位，较前（2023-06-30）范围缩小；左锁骨上、左肺门及纵隔多发淋巴结转移，较前变化不大2.双肺肺气肿；双肺少许纤维条索灶3.主动脉及", "bbox": [170, 168, 971, 186]},
	{"text": "冠状动脉钙化4.扫及肝囊肿胸部CT平扫，下腹部（肾）CT平扫，上腹部CT平扫，盆腔CT平扫CT（2023-08-11）：1.肺癌复查：左肺上叶占位，范围较前（2023-7-20）减小；左锁骨上、左肺门及纵隔多发稍大淋巴", "bbox": [25, 190, 956, 208]},
	{"text": "结，较前变化不大2.双肺肺气肿；双肺少许条索灶3.主动脉及冠状动脉钙化4.肝囊肿5.左肾稍低密度灶，建议超声检查；左肾囊肿6.十二指肠降段憩室7.右侧髂骨稍高密度灶，建议复查8.考虑骶管（S3-4", "bbox": [25, 214, 971, 232]},
	{"text": "水平）囊肿。（本院）", "bbox": [25, 239, 122, 256]},
	{"text": "2025-03-11", "bbox": [40, 264, 92, 280]},
	{"text": "颈部+胸部增强CT：1.肺癌复查：左肺团片影，较前25.2.6范围相仿；2.双肺微小结节，原左肺新增结节较前略小（im149薄层），转移不除外，余较前相仿，定期复查；3.双肺", "bbox": [170, 264, 970, 281]},
	{"text": "肺气肿；双肺条索灶；4.左肺门及纵隔多发稍大淋巴结，较前相仿；5.主动脉及冠状动脉钙化；心包少量积液；左侧胸膜局限性增厚；6.扫及肝囊肿；左肾囊肿。（本院）", "bbox": [25, 288, 800, 305]},
	{"text": "2025-09-02", "bbox": [40, 314, 92, 329]},
	{"text": "颅脑磁共振成像+DWI（特殊序列成像）MR：考虑脑内多发小缺血灶，较前（2024-11-8）变化不著，建议复查。左侧上颌窦囊肿。（本院）", "bbox": [168, 313, 784, 330]},
	{"text": "2025-09-03", "bbox": [40, 338, 92, 354]},
	{"text": "颈部CT增强扫描，胸部CT增强扫描，上腹部CT增强扫描，盆腔CT增强扫描，下腹部CT增强扫描：1.肺癌复查：左肺团片影，较前2025.05.07范围略增大，建议复查2.双肺微小结节，", "bbox": [168, 338, 962, 355]},
	{"text": "较前变化不大，转移不除外，建议定期复查3.双肺肺气肿；双肺条索灶4.左肺门及纵隔多发稍大淋巴结，较前略大5.主动脉及冠状动脉钙化；心包少量积液；左侧胸膜局限性增厚6.肝囊肿；左肾囊肿7.", "bbox": [25, 361, 966, 379]},
	{"text": "十二指肠降段憩室8.右侧髂骨稍高密度灶，较前2024.11.06变化不大，建议复查9.考虑骶管囊肿10.颈部未见明显异常；扫及双侧上颌窦炎。（本院）", "bbox": [25, 385, 717, 402]},
	{"text": "2025-12-27", "bbox": [36, 410, 89, 426]},
	{"text": "颈+胸部增强CT：1.肺癌复查：左肺团片影，较前2025-09-03增大；周围新发实变及网格影，请结合临床，建议复查；2.双肺小结节及小斑片影，较前部分增大，部分新发，部分", "bbox": [168, 409, 967, 427]},
	{"text": "变化不大，建议定期复查；3.双肺肺气肿；双肺条索灶；双肺胸膜下磨玻璃密度影，请结合临床随诊复查；4.左肺门及纵隔多发肿大淋巴结，较前部分增大；5.主动脉及冠状动脉钙化；心包少量积液；左侧胸", "bbox": [25, 433, 968, 451]},
	{"text": "膜局限性增厚；左侧胸腔少量积液；6.扫及肝囊肿；左肾囊肿7.颈部未见明显异常；扫及双侧上颌窦炎。（本院）", "bbox": [25, 457, 539, 474]},
	{"text": "初步诊断", "bbox": [496, 481, 538, 498]},
	{"text": "1、左肺上叶癌 腺癌 cT3N3MO IIIC期", "bbox": [496, 505, 662, 522]},
	{"text": "纵隔淋巴结转移", "bbox": [515, 528, 585, 545]},
	{"text": "锁骨上淋巴结转移", "bbox": [515, 551, 594, 568]},
	{"text": "肺门淋巴结转移", "bbox": [515, 575, 585, 592]},
	{"text": "颈部淋巴结转移", "bbox": [515, 598, 584, 615]},
	{"text": "2、肺气肿", "bbox": [493, 622, 538, 639]},
	{"text": "3、鼻窦炎", "bbox": [493, 646, 538, 663]},
	{"text": "4、肝囊肿", "bbox": [492, 670, 537, 687]},
	{"text": "5、肾囊肿", "bbox": [490, 693, 536, 710]},
	{"text": "6、上颌窦囊肿", "bbox": [489, 716, 554, 733]},
	{"text": "我审核病史记录内容属实无遗漏，我交给医院的病例资料已收回，患方签字：", "bbox": [53, 764, 386, 781]},
	{"text": "宗茹", "bbox": [945, 747, 969, 764]}
]
2026-08-10 18:08:45,282 INFO     29 [qwen-vl-text] coord API: raw_items=31, valid_items=31, elapsed=16.6s
2026-08-10 18:08:45,282 INFO     29 [qwen-vl-text] coord item[0]: text=2023-07-20, bbox=[40, 168, 92, 184]
2026-08-10 18:08:45,283 INFO     29 [qwen-vl-text] coord item[1]: text=胸部CT：1.肺癌复查：左肺上叶占位，较前（2023-06-30）范围缩小；左锁骨上、左肺门及纵隔多发淋巴结转移，较前变化不大2.双肺肺气肿；双肺少许纤维条索灶3.主动脉及, bbox=[170, 168, 971, 186]
2026-08-10 18:08:45,283 INFO     29 [qwen-vl-text] coord item[2]: text=冠状动脉钙化4.扫及肝囊肿胸部CT平扫，下腹部（肾）CT平扫，上腹部CT平扫，盆腔CT平扫CT（2023-08-11）：1.肺癌复查：左肺上叶占位，范围较前（2023-7-20）减小；左锁骨上、左肺门及纵隔多发稍大淋巴, bbox=[25, 190, 956, 208]
2026-08-10 18:08:45,283 INFO     29 [qwen-vl-text] coord item[3]: text=结，较前变化不大2.双肺肺气肿；双肺少许条索灶3.主动脉及冠状动脉钙化4.肝囊肿5.左肾稍低密度灶，建议超声检查；左肾囊肿6.十二指肠降段憩室7.右侧髂骨稍高密度灶，建议复查8.考虑骶管（S3-4, bbox=[25, 214, 971, 232]
2026-08-10 18:08:45,283 INFO     29 [qwen-vl-text] coord item[4]: text=水平）囊肿。（本院）, bbox=[25, 239, 122, 256]
2026-08-10 18:08:45,283 INFO     29 [qwen-vl-text] coord item[5]: text=2025-03-11, bbox=[40, 264, 92, 280]
2026-08-10 18:08:45,283 INFO     29 [qwen-vl-text] coord item[6]: text=颈部+胸部增强CT：1.肺癌复查：左肺团片影，较前25.2.6范围相仿；2.双肺微小结节，原左肺新增结节较前略小（im149薄层），转移不除外，余较前相仿，定期复查；3.双肺, bbox=[170, 264, 970, 281]
2026-08-10 18:08:45,283 INFO     29 [qwen-vl-text] coord item[7]: text=肺气肿；双肺条索灶；4.左肺门及纵隔多发稍大淋巴结，较前相仿；5.主动脉及冠状动脉钙化；心包少量积液；左侧胸膜局限性增厚；6.扫及肝囊肿；左肾囊肿。（本院）, bbox=[25, 288, 800, 305]
2026-08-10 18:08:45,283 INFO     29 [qwen-vl-text] coord item[8]: text=2025-09-02, bbox=[40, 314, 92, 329]
2026-08-10 18:08:45,283 INFO     29 [qwen-vl-text] coord item[9]: text=颅脑磁共振成像+DWI（特殊序列成像）MR：考虑脑内多发小缺血灶，较前（2024-11-8）变化不著，建议复查。左侧上颌窦囊肿。（本院）, bbox=[168, 313, 784, 330]
2026-08-10 18:08:45,283 INFO     29 [qwen-vl-text] coord item[10]: text=2025-09-03, bbox=[40, 338, 92, 354]
2026-08-10 18:08:45,283 INFO     29 [qwen-vl-text] coord item[11]: text=颈部CT增强扫描，胸部CT增强扫描，上腹部CT增强扫描，盆腔CT增强扫描，下腹部CT增强扫描：1.肺癌复查：左肺团片影，较前2025.05.07范围略增大，建议复查2.双肺微小结节，, bbox=[168, 338, 962, 355]
2026-08-10 18:08:45,283 INFO     29 [qwen-vl-text] coord item[12]: text=较前变化不大，转移不除外，建议定期复查3.双肺肺气肿；双肺条索灶4.左肺门及纵隔多发稍大淋巴结，较前略大5.主动脉及冠状动脉钙化；心包少量积液；左侧胸膜局限性增厚6.肝囊肿；左肾囊肿7., bbox=[25, 361, 966, 379]
2026-08-10 18:08:45,284 INFO     29 [qwen-vl-text] coord item[13]: text=十二指肠降段憩室8.右侧髂骨稍高密度灶，较前2024.11.06变化不大，建议复查9.考虑骶管囊肿10.颈部未见明显异常；扫及双侧上颌窦炎。（本院）, bbox=[25, 385, 717, 402]
2026-08-10 18:08:45,284 INFO     29 [qwen-vl-text] coord item[14]: text=2025-12-27, bbox=[36, 410, 89, 426]
2026-08-10 18:08:45,284 INFO     29 [qwen-vl-text] coord item[15]: text=颈+胸部增强CT：1.肺癌复查：左肺团片影，较前2025-09-03增大；周围新发实变及网格影，请结合临床，建议复查；2.双肺小结节及小斑片影，较前部分增大，部分新发，部分, bbox=[168, 409, 967, 427]
2026-08-10 18:08:45,284 INFO     29 [qwen-vl-text] coord item[16]: text=变化不大，建议定期复查；3.双肺肺气肿；双肺条索灶；双肺胸膜下磨玻璃密度影，请结合临床随诊复查；4.左肺门及纵隔多发肿大淋巴结，较前部分增大；5.主动脉及冠状动脉钙化；心包少量积液；左侧胸, bbox=[25, 433, 968, 451]
2026-08-10 18:08:45,284 INFO     29 [qwen-vl-text] coord item[17]: text=膜局限性增厚；左侧胸腔少量积液；6.扫及肝囊肿；左肾囊肿7.颈部未见明显异常；扫及双侧上颌窦炎。（本院）, bbox=[25, 457, 539, 474]
2026-08-10 18:08:45,284 INFO     29 [qwen-vl-text] coord item[18]: text=初步诊断, bbox=[496, 481, 538, 498]
2026-08-10 18:08:45,284 INFO     29 [qwen-vl-text] coord item[19]: text=1、左肺上叶癌 腺癌 cT3N3MO IIIC期, bbox=[496, 505, 662, 522]
2026-08-10 18:08:45,284 INFO     29 [qwen-vl-text] coord item[20]: text=纵隔淋巴结转移, bbox=[515, 528, 585, 545]
2026-08-10 18:08:45,284 INFO     29 [qwen-vl-text] coord item[21]: text=锁骨上淋巴结转移, bbox=[515, 551, 594, 568]
2026-08-10 18:08:45,284 INFO     29 [qwen-vl-text] coord item[22]: text=肺门淋巴结转移, bbox=[515, 575, 585, 592]
2026-08-10 18:08:45,285 INFO     29 [qwen-vl-text] coord item[23]: text=颈部淋巴结转移, bbox=[515, 598, 584, 615]
2026-08-10 18:08:45,285 INFO     29 [qwen-vl-text] coord item[24]: text=2、肺气肿, bbox=[493, 622, 538, 639]
2026-08-10 18:08:45,285 INFO     29 [qwen-vl-text] coord item[25]: text=3、鼻窦炎, bbox=[493, 646, 538, 663]
2026-08-10 18:08:45,285 INFO     29 [qwen-vl-text] coord item[26]: text=4、肝囊肿, bbox=[492, 670, 537, 687]
2026-08-10 18:08:45,285 INFO     29 [qwen-vl-text] coord item[27]: text=5、肾囊肿, bbox=[490, 693, 536, 710]
2026-08-10 18:08:45,285 INFO     29 [qwen-vl-text] coord item[28]: text=6、上颌窦囊肿, bbox=[489, 716, 554, 733]
2026-08-10 18:08:45,285 INFO     29 [qwen-vl-text] coord item[29]: text=我审核病史记录内容属实无遗漏，我交给医院的病例资料已收回，患方签字：, bbox=[53, 764, 386, 781]
2026-08-10 18:08:45,285 INFO     29 [qwen-vl-text] coord item[30]: text=宗茹, bbox=[945, 747, 969, 764]
2026-08-10 18:08:45,285 INFO     29 [qwen-vl-text] page=5 — 31/31 coords, api_time=16.6s
2026-08-10 18:08:45,286 INFO     29 [qwen-vl-text] new_positions (93):
[[3, 23.576, 143.14, 95.19999999999999, 105.91], [3, 183.55599999999998, 223.97199999999998, 129.11499999999998, 141.015], [3, 420.15799999999996, 470.678, 129.11499999999998, 141.015], [3, 183.55599999999998, 235.76, 145.775, 157.67499999999998], [3, 420.15799999999996, 581.822, 145.775, 157.67499999999998], [3, 183.55599999999998, 235.76, 162.435, 174.33499999999998], [3, 420.15799999999996, 564.14, 162.435, 174.33499999999998], [3, 183.55599999999998, 235.76, 180.285, 192.185], [3, 420.15799999999996, 559.93, 180.285, 192.185], [3, 40.416, 202.922, 197.54, 207.655], [3, 36.205999999999996, 798.216, 211.82, 222.53], [3, 23.576, 809.1619999999999, 225.505, 236.215], [3, 23.576, 809.1619999999999, 239.19, 249.89999999999998], [3, 23.576, 809.1619999999999, 252.875, 263.585], [3, 23.576, 804.11, 266.56, 277.27], [3, 23.576, 799.9, 280.245, 290.955], [3, 23.576, 809.1619999999999, 293.93, 304.64], [3, 23.576, 809.1619999999999, 307.615, 318.325], [3, 23.576, 809.1619999999999, 321.3, 332.01], [3, 23.576, 812.53, 334.98499999999996, 345.695], [3, 23.576, 812.53, 348.66999999999996, 359.38], [3, 23.576, 812.53, 362.35499999999996, 373.065], [3, 23.576, 812.53, 376.03999999999996, 386.75], [3, 23.576, 807.478, 389.72499999999997, 400.435], [3, 23.576, 86.726, 406.97999999999996, 417.69], [3, 40.416, 740.9599999999999, 421.26, 431.96999999999997], [3, 40.416, 809.1619999999999, 434.945, 445.655], [3, 23.576, 119.564, 449.22499999999997, 459.935], [3, 40.416, 225.656, 462.90999999999997, 473.62], [3, 40.416, 421.0, 476.59499999999997, 487.30499999999995], [3, 368.796, 447.102, 490.875, 501.585], [3, 275.334, 534.67, 504.56, 515.27], [4, 23.576, 820.9499999999999, 79.72999999999999, 104.125], [4, 39.574, 236.602, 107.695, 119.0], [4, 39.574, 438.68199999999996, 121.975, 133.28], [4, 385.63599999999997, 467.31, 137.445, 148.155], [4, 287.122, 555.72, 151.725, 162.435], [4, 271.12399999999997, 565.824, 166.005, 176.715], [4, 22.733999999999998, 818.424, 180.88, 192.78], [4, 22.733999999999998, 810.846, 195.755, 207.06], [4, 22.733999999999998, 819.266, 210.035, 221.34], [4, 22.733999999999998, 822.634, 224.315, 235.61999999999998], [4, 22.733999999999998, 821.7919999999999, 238.595, 249.89999999999998], [4, 22.733999999999998, 808.3199999999999, 252.875, 264.18], [4, 22.733999999999998, 816.74, 267.75, 279.055], [4, 22.733999999999998, 820.108, 282.03, 293.335], [4, 22.733999999999998, 112.828, 296.31, 307.02], [4, 39.574, 730.856, 309.995, 321.3], [4, 380.584, 460.574, 324.87, 335.58], [4, 42.942, 370.47999999999996, 339.15, 350.455], [4, 39.574, 811.688, 353.43, 364.73499999999996], [4, 22.733999999999998, 813.372, 367.71, 379.015], [4, 22.733999999999998, 287.964, 381.99, 393.29499999999996], [4, 39.574, 809.1619999999999, 396.27, 407.575], [4, 22.733999999999998, 226.498, 410.54999999999995, 421.85499999999996], [4, 39.574, 479.94, 424.83, 436.135], [4, 39.574, 806.636, 439.10999999999996, 450.41499999999996], [4, 22.733999999999998, 85.884, 453.39, 464.695], [4, 39.574, 795.6899999999999, 467.66999999999996, 478.97499999999997], [4, 22.733999999999998, 503.51599999999996, 481.95, 493.255], [4, 39.574, 443.734, 496.22999999999996, 507.53499999999997], [4, 143.982, 805.794, 510.51, 521.8149999999999], [5, 33.68, 77.464, 99.96, 109.47999999999999], [5, 143.14, 817.582, 99.96, 110.67], [5, 21.05, 804.952, 113.05, 123.75999999999999], [5, 21.05, 817.582, 127.33, 138.04], [5, 21.05, 102.72399999999999, 142.20499999999998, 152.32], [5, 33.68, 77.464, 157.07999999999998, 166.6], [5, 143.14, 816.74, 157.07999999999998, 167.195], [5, 21.05, 673.6, 171.35999999999999, 181.475], [5, 33.68, 77.464, 186.82999999999998, 195.755], [5, 141.456, 660.1279999999999, 186.23499999999999, 196.35], [5, 33.68, 77.464, 201.10999999999999, 210.63], [5, 141.456, 810.004, 201.10999999999999, 211.225], [5, 21.05, 813.372, 214.795, 225.505], [5, 21.05, 603.7139999999999, 229.075, 239.19], [5, 30.311999999999998, 74.938, 243.95, 253.47], [5, 141.456, 814.2139999999999, 243.355, 254.065], [5, 21.05, 815.0559999999999, 257.635, 268.34499999999997], [5, 21.05, 453.83799999999997, 271.91499999999996, 282.03], [5, 417.632, 452.996, 286.195, 296.31], [5, 417.632, 557.404, 300.47499999999997, 310.59], [5, 433.63, 492.57, 314.15999999999997, 324.275], [5, 433.63, 500.14799999999997, 327.84499999999997, 337.96], [5, 433.63, 492.57, 342.125, 352.24], [5, 433.63, 491.728, 355.81, 365.925], [5, 415.106, 452.996, 370.09, 380.205], [5, 415.106, 452.996, 384.37, 394.48499999999996], [5, 414.264, 452.154, 398.65, 408.765], [5, 412.58, 451.312, 412.335, 422.45], [5, 411.738, 466.46799999999996, 426.02, 436.135], [5, 44.626, 325.012, 454.58, 464.695], [5, 795.6899999999999, 815.898, 444.465, 454.58]]
2026-08-10 18:08:45,286 INFO     29 [qwen-vl-text] ═══ DONE ═══ 93 positions, pages=3, time=88.8s
2026-08-10 18:08:45,299 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 18:08:45,300 INFO     29 [Trace] task=d64c79b4 | doc=07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf | Extractor:Admission | outputs={"chunks": "1 items, types={'AdmissionRecord': 1}", "html": "", "json": "417 items", "markdown": "", "text": "", "name": "07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Admission\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 18:08:45,300 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 18:08:45,300 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:08:45.300+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 84, "failed": 0, "current": {"d64c79b494e511f1bd9827cf206dfa2d": {"id": "d64c79b494e511f1bd9827cf206dfa2d", "doc_id": "d60771c094e511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 5825068, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385028897, "task_type": "dataflow", "root_trace_id": "93629fbf7f764cf397a9e7f896dd05c6", "root_traceparent": "00-93629fbf7f764cf397a9e7f896dd05c6-e7dded3dfece48a2-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:08:45,305 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:08:45,306 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:08:45,306 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 18:08:45,306 INFO     29 [qwen-vl-text] positions(17): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:08:45,306 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [17]
2026-08-10 18:08:45,422 INFO     29 [qwen-vl-text] page=0, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 18:08:45,422 INFO     29 [qwen-vl-text] LLM extraction start, text_len=225
2026-08-10 18:08:45,422 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:08:45,423 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 0, \"bbox_end\": 16, \"encounter_dates\": [\"2026-03-06\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "姓名\n性别：男\n年龄：57\n门诊号：\n科别：\n病区\n床号\n住院号：\n取材部位：左肺\n补充内容：\n快速石蜡病理诊断：\n（左肺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，免疫组化\n及特殊染色待补充报告。\n免疫组化结果：CK5/6（-）、TTF-1（-）、NapsinA（-）、P40（部分+）、Villin（-）、CK7\n（+）、CDX2（-）\nALK伴随诊断：\nALK（D5F3）：阴性；（兔单克隆阴性对照：阴性；阳性对照：阳性）",
    "role": "user"
  }
]
2026-08-10 18:08:48,253 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:08:48,253 INFO     29 [qwen-vl-text] LLM output (len=475):
{
  "exam_date": null,
  "report_date": null,
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "左肺",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "快速石蜡病理诊断：\n（左肺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，免疫组化\n及特殊染色待补充报告。",
  "conclusion": "免疫组化结果：CK5/6（-）、TTF-1（-）、NapsinA（-）、P40（部分+）、Villin（-）、CK7\n（+）、CDX2（-）\nALK伴随诊断：\nALK（D5F3）：阴性；（兔单克隆阴性对照：阴性；阳性对照：阳性）",
  "physician": null,
  "reviewer": null
}
2026-08-10 18:08:48,254 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=480124, prompt_len=889
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共17行）
["姓名", "性别：男", "年龄：57", "门诊号：", "科别：", "病区", "床号", "住院号：", "取材部位：左肺", "补充内容：", "快速石蜡病理诊断：", "（左肺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，免疫组化", "及特殊染色待补充报告。", "免疫组化结果：CK5/6（-）、TTF-1（-）、NapsinA（-）、P40（部分+）、Villin（-）、CK7", "（+）、CDX2（-）", "ALK伴随诊断：", "ALK（D5F3）：阴性；（兔单克隆阴性对照：阴性；阳性对照：阳性）"]

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
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] coord API raw response (len=965):
[
	{"text": "姓名", "bbox": [70, 210, 107, 235]},
	{"text": "性别：男", "bbox": [300, 211, 370, 237]},
	{"text": "年龄：57", "bbox": [522, 212, 590, 238]},
	{"text": "门诊号：", "bbox": [732, 212, 792, 238]},
	{"text": "科别：", "bbox": [70, 273, 112, 298]},
	{"text": "病区", "bbox": [299, 274, 329, 299]},
	{"text": "床号", "bbox": [521, 274, 555, 299]},
	{"text": "住院号：", "bbox": [730, 274, 791, 299]},
	{"text": "取材部位：左肺", "bbox": [70, 355, 218, 383]},
	{"text": "补充内容：", "bbox": [74, 438, 155, 464]},
	{"text": "快速石蜡病理诊断：", "bbox": [74, 492, 260, 520]},
	{"text": "（左肺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，免疫组化", "bbox": [74, 520, 954, 551]},
	{"text": "及特殊染色待补充报告。", "bbox": [74, 551, 307, 580]},
	{"text": "免疫组化结果：CK5/6（-）、TTF-1（-）、NapsinA（-）、P40（部分+）、Villin（-）、CK7", "bbox": [74, 581, 940, 611]},
	{"text": "（+）、CDX2（-）", "bbox": [84, 611, 246, 640]},
	{"text": "ALK伴随诊断：", "bbox": [74, 642, 207, 671]},
	{"text": "ALK（D5F3）：阴性；（兔单克隆阴性对照：阴性；阳性对照：阳性）", "bbox": [74, 672, 755, 702]}
]
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] coord API: raw_items=17, valid_items=17, elapsed=5.6s
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] coord item[0]: text=姓名, bbox=[70, 210, 107, 235]
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] coord item[1]: text=性别：男, bbox=[300, 211, 370, 237]
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：57, bbox=[522, 212, 590, 238]
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] coord item[3]: text=门诊号：, bbox=[732, 212, 792, 238]
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] coord item[4]: text=科别：, bbox=[70, 273, 112, 298]
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] coord item[5]: text=病区, bbox=[299, 274, 329, 299]
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] coord item[6]: text=床号, bbox=[521, 274, 555, 299]
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] coord item[7]: text=住院号：, bbox=[730, 274, 791, 299]
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] coord item[8]: text=取材部位：左肺, bbox=[70, 355, 218, 383]
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] coord item[9]: text=补充内容：, bbox=[74, 438, 155, 464]
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] coord item[10]: text=快速石蜡病理诊断：, bbox=[74, 492, 260, 520]
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] coord item[11]: text=（左肺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，免疫组化, bbox=[74, 520, 954, 551]
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] coord item[12]: text=及特殊染色待补充报告。, bbox=[74, 551, 307, 580]
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] coord item[13]: text=免疫组化结果：CK5/6（-）、TTF-1（-）、NapsinA（-）、P40（部分+）、Villin（-）、CK7, bbox=[74, 581, 940, 611]
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] coord item[14]: text=（+）、CDX2（-）, bbox=[84, 611, 246, 640]
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] coord item[15]: text=ALK伴随诊断：, bbox=[74, 642, 207, 671]
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] coord item[16]: text=ALK（D5F3）：阴性；（兔单克隆阴性对照：阴性；阳性对照：阳性）, bbox=[74, 672, 755, 702]
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] page=0 — 17/17 coords, api_time=5.6s
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] new_positions (17):
[[0, 58.94, 90.094, 124.94999999999999, 139.825], [0, 252.6, 311.53999999999996, 125.54499999999999, 141.015], [0, 439.524, 496.78, 126.14, 141.60999999999999], [0, 616.3439999999999, 666.864, 126.14, 141.60999999999999], [0, 58.94, 94.304, 162.435, 177.31], [0, 251.75799999999998, 277.018, 163.03, 177.905], [0, 438.68199999999996, 467.31, 163.03, 177.905], [0, 614.66, 666.0219999999999, 163.03, 177.905], [0, 58.94, 183.55599999999998, 211.225, 227.885], [0, 62.308, 130.51, 260.61, 276.08], [0, 62.308, 218.92, 292.74, 309.4], [0, 62.308, 803.2679999999999, 309.4, 327.84499999999997], [0, 62.308, 258.49399999999997, 327.84499999999997, 345.09999999999997], [0, 62.308, 791.48, 345.695, 363.54499999999996], [0, 70.728, 207.132, 363.54499999999996, 380.79999999999995], [0, 62.308, 174.29399999999998, 381.99, 399.245], [0, 62.308, 635.7099999999999, 399.84, 417.69]]
2026-08-10 18:08:53,854 INFO     29 [qwen-vl-text] ═══ DONE ═══ 17 positions, pages=1, time=8.5s
2026-08-10 18:08:53,854 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:08:53,855 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:08:53,855 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 18:08:53,855 INFO     29 [qwen-vl-text] positions(14): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:08:53,855 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [14]
2026-08-10 18:08:53,967 INFO     29 [qwen-vl-text] page=1, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 18:08:53,967 INFO     29 [qwen-vl-text] LLM extraction start, text_len=130
2026-08-10 18:08:53,968 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:08:53,968 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 17, \"bbox_end\": 30, \"encounter_dates\": [\"2026-03-06\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "性别：男\n年龄：57\n门诊号：\n科别：\n床号\n送检医生\n住院号\n病区\n送检日期：2026-3-6 15:05:29\n取材信息：\n灰白灰红条状碎组织一堆，共计直径0.8cm。\n病理诊断：\n快速石蜡病理诊断：\n（左肺活检）分化差的癌，待免疫组化结果进一步明确分型。",
    "role": "user"
  }
]
2026-08-10 18:08:56,411 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:08:56,411 INFO     29 [qwen-vl-text] LLM output (len=373):
{
  "exam_date": "2026-03-06",
  "report_date": null,
  "exam_name": "快速石蜡病理诊断",
  "exam_category": "pathology",
  "body_part": "左肺",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "取材信息：\n灰白灰红条状碎组织一堆，共计直径0.8cm。",
  "conclusion": "快速石蜡病理诊断：\n（左肺活检）分化差的癌，待免疫组化结果进一步明确分型。",
  "physician": null,
  "reviewer": null
}
2026-08-10 18:08:56,413 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=365180, prompt_len=785
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共14行）
["性别：男", "年龄：57", "门诊号：", "科别：", "床号", "送检医生", "住院号", "病区", "送检日期：2026-3-6 15:05:29", "取材信息：", "灰白灰红条状碎组织一堆，共计直径0.8cm。", "病理诊断：", "快速石蜡病理诊断：", "（左肺活检）分化差的癌，待免疫组化结果进一步明确分型。"]

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
2026-08-10 18:09:01,022 INFO     29 [qwen-vl-text] coord API raw response (len=741):
[
	{"text": "性别：男", "bbox": [284, 223, 353, 249]},
	{"text": "年龄： 57", "bbox": [496, 223, 580, 249]},
	{"text": "门诊号：", "bbox": [730, 228, 794, 254]},
	{"text": "科别：", "bbox": [34, 272, 79, 298]},
	{"text": "床号", "bbox": [281, 272, 318, 297]},
	{"text": "送检医生", "bbox": [496, 272, 562, 297]},
	{"text": "住院号", "bbox": [730, 272, 788, 297]},
	{"text": "病区", "bbox": [34, 320, 68, 345]},
	{"text": "送检日期：2026-3-6 15:05:29", "bbox": [496, 320, 729, 345]},
	{"text": "取材信息：", "bbox": [35, 377, 118, 402]},
	{"text": "灰白灰红条状碎组织一堆，共计直径0.8cm。", "bbox": [54, 415, 473, 443]},
	{"text": "病理诊断：", "bbox": [31, 666, 119, 691]},
	{"text": "快速石蜡病理诊断：", "bbox": [58, 707, 239, 733]},
	{"text": "（左肺活检）分化差的癌，待免疫组化结果进一步明确分型。", "bbox": [68, 735, 638, 762]}
]
2026-08-10 18:09:01,022 INFO     29 [qwen-vl-text] coord API: raw_items=14, valid_items=14, elapsed=4.6s
2026-08-10 18:09:01,023 INFO     29 [qwen-vl-text] coord item[0]: text=性别：男, bbox=[284, 223, 353, 249]
2026-08-10 18:09:01,023 INFO     29 [qwen-vl-text] coord item[1]: text=年龄： 57, bbox=[496, 223, 580, 249]
2026-08-10 18:09:01,023 INFO     29 [qwen-vl-text] coord item[2]: text=门诊号：, bbox=[730, 228, 794, 254]
2026-08-10 18:09:01,023 INFO     29 [qwen-vl-text] coord item[3]: text=科别：, bbox=[34, 272, 79, 298]
2026-08-10 18:09:01,023 INFO     29 [qwen-vl-text] coord item[4]: text=床号, bbox=[281, 272, 318, 297]
2026-08-10 18:09:01,023 INFO     29 [qwen-vl-text] coord item[5]: text=送检医生, bbox=[496, 272, 562, 297]
2026-08-10 18:09:01,023 INFO     29 [qwen-vl-text] coord item[6]: text=住院号, bbox=[730, 272, 788, 297]
2026-08-10 18:09:01,023 INFO     29 [qwen-vl-text] coord item[7]: text=病区, bbox=[34, 320, 68, 345]
2026-08-10 18:09:01,023 INFO     29 [qwen-vl-text] coord item[8]: text=送检日期：2026-3-6 15:05:29, bbox=[496, 320, 729, 345]
2026-08-10 18:09:01,024 INFO     29 [qwen-vl-text] coord item[9]: text=取材信息：, bbox=[35, 377, 118, 402]
2026-08-10 18:09:01,024 INFO     29 [qwen-vl-text] coord item[10]: text=灰白灰红条状碎组织一堆，共计直径0.8cm。, bbox=[54, 415, 473, 443]
2026-08-10 18:09:01,024 INFO     29 [qwen-vl-text] coord item[11]: text=病理诊断：, bbox=[31, 666, 119, 691]
2026-08-10 18:09:01,024 INFO     29 [qwen-vl-text] coord item[12]: text=快速石蜡病理诊断：, bbox=[58, 707, 239, 733]
2026-08-10 18:09:01,024 INFO     29 [qwen-vl-text] coord item[13]: text=（左肺活检）分化差的癌，待免疫组化结果进一步明确分型。, bbox=[68, 735, 638, 762]
2026-08-10 18:09:01,024 INFO     29 [qwen-vl-text] page=1 — 14/14 coords, api_time=4.6s
2026-08-10 18:09:01,024 INFO     29 [qwen-vl-text] new_positions (14):
[[1, 239.128, 297.226, 132.685, 148.155], [1, 417.632, 488.35999999999996, 132.685, 148.155], [1, 614.66, 668.548, 135.66, 151.13], [1, 28.628, 66.518, 161.84, 177.31], [1, 236.602, 267.756, 161.84, 176.715], [1, 417.632, 473.204, 161.84, 176.715], [1, 614.66, 663.496, 161.84, 176.715], [1, 28.628, 57.256, 190.39999999999998, 205.27499999999998], [1, 417.632, 613.818, 190.39999999999998, 205.27499999999998], [1, 29.47, 99.356, 224.315, 239.19], [1, 45.467999999999996, 398.26599999999996, 246.92499999999998, 263.585], [1, 26.102, 100.198, 396.27, 411.145], [1, 48.836, 201.238, 420.66499999999996, 436.135], [1, 57.256, 537.196, 437.325, 453.39]]
2026-08-10 18:09:01,024 INFO     29 [qwen-vl-text] ═══ DONE ═══ 14 positions, pages=1, time=7.2s
2026-08-10 18:09:01,025 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:09:01,027 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:09:01,027 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 18:09:01,027 INFO     29 [qwen-vl-text] positions(24): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:09:01,027 INFO     29 [qwen-vl-text] page grouping: [2, 3], lines per page: [23, 1]
2026-08-10 18:09:01,197 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 18:09:01,455 INFO     29 [qwen-vl-text] page=3, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 18:09:01,456 INFO     29 [qwen-vl-text] LLM extraction start, text_len=461
2026-08-10 18:09:01,456 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:09:01,456 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 31, \"bbox_end\": 54, \"encounter_dates\": [\"2023-04-04\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "病理会诊报告单\n病理号:\n姓名\n性别: 男\n年龄: 54岁\n送检单位\n送检日期: 2023/4/4\n送检医生:\n镜下所见:\n原病理诊断:\n读“青岛市中心医疗集团”报告, 病理号: 2307637, HE×1, IHC*5, 原诊断: (左锁骨上淋\n巴结穿刺活检) 纤维组织内查见分化差的癌, 结合免疫组化及病史, 不除外肺非小细胞癌转\n移。\n免疫组化结果: TTF-1 (-), NapsinA (-), CK7 (+), CK 5/6 (-), P40 (灶+)。\n病理会诊诊断:\n(左锁骨上淋巴结穿刺活检) 纤维组织内查见片状、实体状异型上皮样细胞浸润, 结合临床及\n免疫标记, 考虑低分化癌, 可能为肺非小细胞癌转移, 倾向腺癌, 建议粘液染色进一步协助诊\n断。\n原单位免疫组化结果: TTF-1 (-), NapsinA (-), CK7 (+), CK 5/6 (-), P40 (个别细胞\n+)。\n报告时间:2023-4-4\n诊断医师:姜慧峰\n注: 病理医师个人会诊咨询意见, 仅供原病理学\n开始 | 病历列表",
    "role": "user"
  }
]
2026-08-10 18:09:07,450 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:09:07,450 INFO     29 [qwen-vl-text] LLM output (len=663):
{
  "exam_date": "2023-04-04",
  "report_date": "2023-04-04",
  "exam_name": "病理会诊",
  "exam_category": "pathology",
  "body_part": "左锁骨上淋巴结",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "镜下所见:\n原病理诊断:\n读“青岛市中心医疗集团”报告, 病理号: 2307637, HE×1, IHC*5, 原诊断: (左锁骨上淋巴结穿刺活检) 纤维组织内查见分化差的癌, 结合免疫组化及病史, 不除外肺非小细胞癌转移。\n免疫组化结果: TTF-1 (-), NapsinA (-), CK7 (+), CK 5/6 (-), P40 (灶+)。",
  "conclusion": "病理会诊诊断:\n(左锁骨上淋巴结穿刺活检) 纤维组织内查见片状、实体状异型上皮样细胞浸润, 结合临床及免疫标记, 考虑低分化癌, 可能为肺非小细胞癌转移, 倾向腺癌, 建议粘液染色进一步协助诊断。\n原单位免疫组化结果: TTF-1 (-), NapsinA (-), CK7 (+), CK 5/6 (-), P40 (个别细胞+)。",
  "physician": "姜慧峰",
  "reviewer": null
}
2026-08-10 18:09:07,452 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=964183, prompt_len=1133
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["病理会诊报告单", "病理号:", "姓名", "性别: 男", "年龄: 54岁", "送检单位", "送检日期: 2023/4/4", "送检医生:", "镜下所见:", "原病理诊断:", "读“青岛市中心医疗集团”报告, 病理号: 2307637, HE×1, IHC*5, 原诊断: (左锁骨上淋", "巴结穿刺活检) 纤维组织内查见分化差的癌, 结合免疫组化及病史, 不除外肺非小细胞癌转", "移。", "免疫组化结果: TTF-1 (-), NapsinA (-), CK7 (+), CK 5/6 (-), P40 (灶+)。", "病理会诊诊断:", "(左锁骨上淋巴结穿刺活检) 纤维组织内查见片状、实体状异型上皮样细胞浸润, 结合临床及", "免疫标记, 考虑低分化癌, 可能为肺非小细胞癌转移, 倾向腺癌, 建议粘液染色进一步协助诊", "断。", "原单位免疫组化结果: TTF-1 (-), NapsinA (-), CK7 (+), CK 5/6 (-), P40 (个别细胞", "+)。", "报告时间:2023-4-4", "诊断医师:姜慧峰", "注: 病理医师个人会诊咨询意见, 仅供原病理学"]

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
2026-08-10 18:09:15,510 INFO     29 [qwen-vl-text] coord API raw response (len=1458):
[
	{"text": "病理会诊报告单", "bbox": [394, 76, 580, 100]},
	{"text": "病理号:", "bbox": [644, 98, 719, 116]},
	{"text": "姓名", "bbox": [81, 131, 146, 147]},
	{"text": "性别: 男", "bbox": [353, 129, 475, 146]},
	{"text": "年龄: 54岁", "bbox": [627, 127, 776, 144]},
	{"text": "送检单位", "bbox": [81, 159, 162, 175]},
	{"text": "送检日期: 2023/4/4", "bbox": [360, 158, 540, 174]},
	{"text": "送检医生:", "bbox": [636, 158, 723, 174]},
	{"text": "镜下所见:", "bbox": [81, 208, 166, 225]},
	{"text": "原病理诊断:", "bbox": [79, 364, 183, 380]},
	{"text": "读“青岛市中心医疗集团”报告, 病理号: 2307637, HE×1, IHC*5, 原诊断: (左锁骨上淋", "bbox": [118, 385, 904, 401]},
	{"text": "巴结穿刺活检) 纤维组织内查见分化差的癌, 结合免疫组化及病史, 不除外肺非小细胞癌转", "bbox": [118, 402, 874, 418]},
	{"text": "移。", "bbox": [117, 420, 143, 435]},
	{"text": "免疫组化结果: TTF-1 (-), NapsinA (-), CK7 (+), CK 5/6 (-), P40 (灶+)。", "bbox": [117, 437, 839, 453]},
	{"text": "病理会诊诊断:", "bbox": [78, 507, 203, 523]},
	{"text": "(左锁骨上淋巴结穿刺活检) 纤维组织内查见片状、实体状异型上皮样细胞浸润, 结合临床及", "bbox": [129, 533, 898, 549]},
	{"text": "免疫标记, 考虑低分化癌, 可能为肺非小细胞癌转移, 倾向腺癌, 建议粘液染色进一步协助诊", "bbox": [117, 550, 898, 566]},
	{"text": "断。", "bbox": [117, 567, 143, 581]},
	{"text": "原单位免疫组化结果: TTF-1 (-), NapsinA (-), CK7 (+), CK 5/6 (-), P40 (个别细胞", "bbox": [118, 583, 918, 599]},
	{"text": "+)。", "bbox": [121, 601, 160, 616]},
	{"text": "报告时间:2023-4-4", "bbox": [102, 839, 276, 855]},
	{"text": "诊断医师:姜慧峰", "bbox": [394, 839, 538, 856]},
	{"text": "注: 病理医师个人会诊咨询意见, 仅供原病理学", "bbox": [85, 868, 511, 885]}
]
2026-08-10 18:09:15,510 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=8.1s
2026-08-10 18:09:15,510 INFO     29 [qwen-vl-text] coord item[0]: text=病理会诊报告单, bbox=[394, 76, 580, 100]
2026-08-10 18:09:15,510 INFO     29 [qwen-vl-text] coord item[1]: text=病理号:, bbox=[644, 98, 719, 116]
2026-08-10 18:09:15,510 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[81, 131, 146, 147]
2026-08-10 18:09:15,510 INFO     29 [qwen-vl-text] coord item[3]: text=性别: 男, bbox=[353, 129, 475, 146]
2026-08-10 18:09:15,511 INFO     29 [qwen-vl-text] coord item[4]: text=年龄: 54岁, bbox=[627, 127, 776, 144]
2026-08-10 18:09:15,511 INFO     29 [qwen-vl-text] coord item[5]: text=送检单位, bbox=[81, 159, 162, 175]
2026-08-10 18:09:15,511 INFO     29 [qwen-vl-text] coord item[6]: text=送检日期: 2023/4/4, bbox=[360, 158, 540, 174]
2026-08-10 18:09:15,511 INFO     29 [qwen-vl-text] coord item[7]: text=送检医生:, bbox=[636, 158, 723, 174]
2026-08-10 18:09:15,511 INFO     29 [qwen-vl-text] coord item[8]: text=镜下所见:, bbox=[81, 208, 166, 225]
2026-08-10 18:09:15,511 INFO     29 [qwen-vl-text] coord item[9]: text=原病理诊断:, bbox=[79, 364, 183, 380]
2026-08-10 18:09:15,511 INFO     29 [qwen-vl-text] coord item[10]: text=读“青岛市中心医疗集团”报告, 病理号: 2307637, HE×1, IHC*5, 原诊断: (左锁骨上淋, bbox=[118, 385, 904, 401]
2026-08-10 18:09:15,511 INFO     29 [qwen-vl-text] coord item[11]: text=巴结穿刺活检) 纤维组织内查见分化差的癌, 结合免疫组化及病史, 不除外肺非小细胞癌转, bbox=[118, 402, 874, 418]
2026-08-10 18:09:15,511 INFO     29 [qwen-vl-text] coord item[12]: text=移。, bbox=[117, 420, 143, 435]
2026-08-10 18:09:15,511 INFO     29 [qwen-vl-text] coord item[13]: text=免疫组化结果: TTF-1 (-), NapsinA (-), CK7 (+), CK 5/6 (-), P40 (灶+)。, bbox=[117, 437, 839, 453]
2026-08-10 18:09:15,511 INFO     29 [qwen-vl-text] coord item[14]: text=病理会诊诊断:, bbox=[78, 507, 203, 523]
2026-08-10 18:09:15,511 INFO     29 [qwen-vl-text] coord item[15]: text=(左锁骨上淋巴结穿刺活检) 纤维组织内查见片状、实体状异型上皮样细胞浸润, 结合临床及, bbox=[129, 533, 898, 549]
2026-08-10 18:09:15,511 INFO     29 [qwen-vl-text] coord item[16]: text=免疫标记, 考虑低分化癌, 可能为肺非小细胞癌转移, 倾向腺癌, 建议粘液染色进一步协助诊, bbox=[117, 550, 898, 566]
2026-08-10 18:09:15,511 INFO     29 [qwen-vl-text] coord item[17]: text=断。, bbox=[117, 567, 143, 581]
2026-08-10 18:09:15,511 INFO     29 [qwen-vl-text] coord item[18]: text=原单位免疫组化结果: TTF-1 (-), NapsinA (-), CK7 (+), CK 5/6 (-), P40 (个别细胞, bbox=[118, 583, 918, 599]
2026-08-10 18:09:15,511 INFO     29 [qwen-vl-text] coord item[19]: text=+)。, bbox=[121, 601, 160, 616]
2026-08-10 18:09:15,511 INFO     29 [qwen-vl-text] coord item[20]: text=报告时间:2023-4-4, bbox=[102, 839, 276, 855]
2026-08-10 18:09:15,511 INFO     29 [qwen-vl-text] coord item[21]: text=诊断医师:姜慧峰, bbox=[394, 839, 538, 856]
2026-08-10 18:09:15,511 INFO     29 [qwen-vl-text] coord item[22]: text=注: 病理医师个人会诊咨询意见, 仅供原病理学, bbox=[85, 868, 511, 885]
2026-08-10 18:09:15,512 INFO     29 [qwen-vl-text] page=2 — 23/23 coords, api_time=8.1s
2026-08-10 18:09:15,517 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1640693, prompt_len=624
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["开始 | 病历列表"]

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
2026-08-10 18:09:16,237 INFO     29 [qwen-vl-text] coord API raw response (len=66):
```json
[
	{"text": "开始 | 病历列表", "bbox": [28, 118, 92, 134]}
]
```
2026-08-10 18:09:16,237 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=0.7s
2026-08-10 18:09:16,238 INFO     29 [qwen-vl-text] coord item[0]: text=开始 | 病历列表, bbox=[28, 118, 92, 134]
2026-08-10 18:09:16,238 INFO     29 [qwen-vl-text] page=3 — 1/1 coords, api_time=0.7s
2026-08-10 18:09:16,238 INFO     29 [qwen-vl-text] new_positions (24):
[[2, 234.42999999999998, 345.09999999999997, 63.992, 84.2], [2, 383.18, 427.805, 82.51599999999999, 97.672], [2, 48.195, 86.86999999999999, 110.30199999999999, 123.774], [2, 210.035, 282.625, 108.618, 122.932], [2, 373.065, 461.71999999999997, 106.934, 121.24799999999999], [2, 48.195, 96.39, 133.878, 147.35], [2, 214.2, 321.3, 133.036, 146.50799999999998], [2, 378.41999999999996, 430.185, 133.036, 146.50799999999998], [2, 48.195, 98.77, 175.136, 189.45], [2, 47.004999999999995, 108.88499999999999, 306.488, 319.96], [2, 70.21, 537.88, 324.17, 337.642], [2, 70.21, 520.03, 338.484, 351.95599999999996], [2, 69.615, 85.085, 353.64, 366.27], [2, 69.615, 499.205, 367.954, 381.426], [2, 46.41, 120.785, 426.894, 440.366], [2, 76.755, 534.31, 448.786, 462.258], [2, 69.615, 534.31, 463.09999999999997, 476.572], [2, 69.615, 85.085, 477.414, 489.202], [2, 70.21, 546.2099999999999, 490.88599999999997, 504.358], [2, 71.99499999999999, 95.19999999999999, 506.042, 518.672], [2, 60.69, 164.22, 706.438, 719.91], [2, 234.42999999999998, 320.11, 706.438, 720.752], [2, 50.574999999999996, 304.04499999999996, 730.856, 745.17], [3, 23.576, 77.464, 70.21, 79.72999999999999]]
2026-08-10 18:09:16,238 INFO     29 [qwen-vl-text] ═══ DONE ═══ 24 positions, pages=2, time=15.2s
2026-08-10 18:09:16,238 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:09:16,244 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:09:16,244 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 18:09:16,244 INFO     29 [qwen-vl-text] positions(21): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:09:16,244 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [21]
2026-08-10 18:09:16,380 INFO     29 [qwen-vl-text] page=6, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 18:09:16,381 INFO     29 [qwen-vl-text] LLM extraction start, text_len=304
2026-08-10 18:09:16,382 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:09:16,383 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 158, \"bbox_end\": 178, \"encounter_dates\": [\"2026-03-09\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "检查项目：\n胸部磁共振平扫+DWI+动态增强成像\n影像登录号：\nMR10060372\n报告状态：\nCorrection\n原因：\n不可选\n主要位置：\n2328\n检查日期：\n2026/3/9 7:44:30\n顺序 #：\nMR10060372\n影像诊断\n左肺癌复查所见。\n纵隔内多发淋巴结肿大。\n肝脏、左肾多发囊肿。\n影像表现\n左上肺示一截面约99x61mm的团块影，呈等长T1等长T2、DWI等高信号，不均匀强化，左上肺门及纵隔与之紧密相贴。右肺未见明显异常信号影，右肺门未见明显增大。纵隔内隆凸下示多发稍大淋巴结，心影大小形态可。未见明显胸腔积液。肝脏、左肾示\n多发囊状长T1长T2信号影，大者直径约21mm。",
    "role": "user"
  }
]
2026-08-10 18:09:17,458 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:09:17.456+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 84, "failed": 0, "current": {"d64c79b494e511f1bd9827cf206dfa2d": {"id": "d64c79b494e511f1bd9827cf206dfa2d", "doc_id": "d60771c094e511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 5825068, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385028897, "task_type": "dataflow", "root_trace_id": "93629fbf7f764cf397a9e7f896dd05c6", "root_traceparent": "00-93629fbf7f764cf397a9e7f896dd05c6-e7dded3dfece48a2-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:09:19,441 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:09:19,441 INFO     29 [qwen-vl-text] LLM output (len=490):
{
  "exam_date": "2026-03-09",
  "report_date": null,
  "exam_name": "胸部磁共振平扫+DWI+动态增强成像",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "左上肺示一截面约99x61mm的团块影，呈等长T1等长T2、DWI等高信号，不均匀强化，左上肺门及纵隔与之紧密相贴。右肺未见明显异常信号影，右肺门未见明显增大。纵隔内隆凸下示多发稍大淋巴结，心影大小形态可。未见明显胸腔积液。肝脏、左肾示多发囊状长T1长T2信号影，大者直径约21mm。",
  "conclusion": "左肺癌复查所见。\n纵隔内多发淋巴结肿大。\n肝脏、左肾多发囊肿。",
  "physician": null,
  "reviewer": null
}
2026-08-10 18:09:19,444 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1020638, prompt_len=980
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共21行）
["检查项目：", "胸部磁共振平扫+DWI+动态增强成像", "影像登录号：", "MR10060372", "报告状态：", "Correction", "原因：", "不可选", "主要位置：", "2328", "检查日期：", "2026/3/9 7:44:30", "顺序 #：", "MR10060372", "影像诊断", "左肺癌复查所见。", "纵隔内多发淋巴结肿大。", "肝脏、左肾多发囊肿。", "影像表现", "左上肺示一截面约99x61mm的团块影，呈等长T1等长T2、DWI等高信号，不均匀强化，左上肺门及纵隔与之紧密相贴。右肺未见明显异常信号影，右肺门未见明显增大。纵隔内隆凸下示多发稍大淋巴结，心影大小形态可。未见明显胸腔积液。肝脏、左肾示", "多发囊状长T1长T2信号影，大者直径约21mm。"]

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
2026-08-10 18:09:26,514 INFO     29 [qwen-vl-text] coord API raw response (len=1216):
[
	{"text": "检查项目：", "bbox": [62, 355, 100, 369]},
	{"text": "胸部磁共振平扫+DWI+动态增强成像", "bbox": [158, 355, 314, 369]},
	{"text": "影像登录号：", "bbox": [62, 372, 108, 386]},
	{"text": "MR10060372", "bbox": [158, 372, 224, 386]},
	{"text": "报告状态：", "bbox": [62, 388, 100, 402]},
	{"text": "Correction", "bbox": [158, 388, 207, 402]},
	{"text": "原因：", "bbox": [62, 404, 83, 418]},
	{"text": "不可选", "bbox": [158, 404, 186, 418]},
	{"text": "主要位置：", "bbox": [397, 337, 435, 351]},
	{"text": "2328", "bbox": [540, 337, 566, 351]},
	{"text": "检查日期：", "bbox": [397, 355, 435, 369]},
	{"text": "2026/3/9 7:44:30", "bbox": [540, 355, 633, 369]},
	{"text": "顺序 #：", "bbox": [397, 372, 430, 386]},
	{"text": "MR10060372", "bbox": [540, 372, 606, 386]},
	{"text": "影像诊断", "bbox": [30, 495, 66, 509]},
	{"text": "左肺癌复查所见。", "bbox": [30, 509, 96, 523]},
	{"text": "纵隔内多发淋巴结肿大。", "bbox": [30, 523, 122, 537]},
	{"text": "肝脏、左肾多发囊肿。", "bbox": [30, 537, 114, 551]},
	{"text": "影像表现", "bbox": [30, 577, 66, 591]},
	{"text": "左上肺示一截面约99x61mm的团块影，呈等长T1等长T2、DWI等高信号，不均匀强化，左上肺门及纵隔与之紧密相贴。右肺未见明显异常信号影，右肺门未见明显增大。纵隔内隆凸下示多发稍大淋巴结，心影大小形态可。未见明显胸腔积液。肝脏、左肾示", "bbox": [30, 591, 982, 605]},
	{"text": "多发囊状长T1长T2信号影，大者直径约21mm。", "bbox": [30, 605, 198, 619]}
]
2026-08-10 18:09:26,514 INFO     29 [qwen-vl-text] coord API: raw_items=21, valid_items=21, elapsed=7.1s
2026-08-10 18:09:26,514 INFO     29 [qwen-vl-text] coord item[0]: text=检查项目：, bbox=[62, 355, 100, 369]
2026-08-10 18:09:26,514 INFO     29 [qwen-vl-text] coord item[1]: text=胸部磁共振平扫+DWI+动态增强成像, bbox=[158, 355, 314, 369]
2026-08-10 18:09:26,515 INFO     29 [qwen-vl-text] coord item[2]: text=影像登录号：, bbox=[62, 372, 108, 386]
2026-08-10 18:09:26,515 INFO     29 [qwen-vl-text] coord item[3]: text=MR10060372, bbox=[158, 372, 224, 386]
2026-08-10 18:09:26,515 INFO     29 [qwen-vl-text] coord item[4]: text=报告状态：, bbox=[62, 388, 100, 402]
2026-08-10 18:09:26,515 INFO     29 [qwen-vl-text] coord item[5]: text=Correction, bbox=[158, 388, 207, 402]
2026-08-10 18:09:26,515 INFO     29 [qwen-vl-text] coord item[6]: text=原因：, bbox=[62, 404, 83, 418]
2026-08-10 18:09:26,515 INFO     29 [qwen-vl-text] coord item[7]: text=不可选, bbox=[158, 404, 186, 418]
2026-08-10 18:09:26,515 INFO     29 [qwen-vl-text] coord item[8]: text=主要位置：, bbox=[397, 337, 435, 351]
2026-08-10 18:09:26,515 INFO     29 [qwen-vl-text] coord item[9]: text=2328, bbox=[540, 337, 566, 351]
2026-08-10 18:09:26,515 INFO     29 [qwen-vl-text] coord item[10]: text=检查日期：, bbox=[397, 355, 435, 369]
2026-08-10 18:09:26,515 INFO     29 [qwen-vl-text] coord item[11]: text=2026/3/9 7:44:30, bbox=[540, 355, 633, 369]
2026-08-10 18:09:26,515 INFO     29 [qwen-vl-text] coord item[12]: text=顺序 #：, bbox=[397, 372, 430, 386]
2026-08-10 18:09:26,515 INFO     29 [qwen-vl-text] coord item[13]: text=MR10060372, bbox=[540, 372, 606, 386]
2026-08-10 18:09:26,515 INFO     29 [qwen-vl-text] coord item[14]: text=影像诊断, bbox=[30, 495, 66, 509]
2026-08-10 18:09:26,515 INFO     29 [qwen-vl-text] coord item[15]: text=左肺癌复查所见。, bbox=[30, 509, 96, 523]
2026-08-10 18:09:26,515 INFO     29 [qwen-vl-text] coord item[16]: text=纵隔内多发淋巴结肿大。, bbox=[30, 523, 122, 537]
2026-08-10 18:09:26,515 INFO     29 [qwen-vl-text] coord item[17]: text=肝脏、左肾多发囊肿。, bbox=[30, 537, 114, 551]
2026-08-10 18:09:26,515 INFO     29 [qwen-vl-text] coord item[18]: text=影像表现, bbox=[30, 577, 66, 591]
2026-08-10 18:09:26,515 INFO     29 [qwen-vl-text] coord item[19]: text=左上肺示一截面约99x61mm的团块影，呈等长T1等长T2、DWI等高信号，不均匀强化，左上肺门及纵隔与之紧密相贴。右肺未见明显异常信号影，右肺门未见明显增大。纵隔内隆凸下示多发稍大淋巴结，心影大小形态可。未见明显胸腔积液。肝脏、左肾示, bbox=[30, 591, 982, 605]
2026-08-10 18:09:26,515 INFO     29 [qwen-vl-text] coord item[20]: text=多发囊状长T1长T2信号影，大者直径约21mm。, bbox=[30, 605, 198, 619]
2026-08-10 18:09:26,516 INFO     29 [qwen-vl-text] page=6 — 21/21 coords, api_time=7.1s
2026-08-10 18:09:26,516 INFO     29 [qwen-vl-text] new_positions (21):
[[6, 52.204, 84.2, 211.225, 219.55499999999998], [6, 133.036, 264.388, 211.225, 219.55499999999998], [6, 52.204, 90.93599999999999, 221.34, 229.67], [6, 133.036, 188.608, 221.34, 229.67], [6, 52.204, 84.2, 230.85999999999999, 239.19], [6, 133.036, 174.29399999999998, 230.85999999999999, 239.19], [6, 52.204, 69.886, 240.38, 248.70999999999998], [6, 133.036, 156.612, 240.38, 248.70999999999998], [6, 334.274, 366.27, 200.515, 208.845], [6, 454.68, 476.572, 200.515, 208.845], [6, 334.274, 366.27, 211.225, 219.55499999999998], [6, 454.68, 532.986, 211.225, 219.55499999999998], [6, 334.274, 362.06, 221.34, 229.67], [6, 454.68, 510.252, 221.34, 229.67], [6, 25.259999999999998, 55.571999999999996, 294.525, 302.85499999999996], [6, 25.259999999999998, 80.832, 302.85499999999996, 311.185], [6, 25.259999999999998, 102.72399999999999, 311.185, 319.515], [6, 25.259999999999998, 95.988, 319.515, 327.84499999999997], [6, 25.259999999999998, 55.571999999999996, 343.315, 351.645], [6, 25.259999999999998, 826.8439999999999, 351.645, 359.97499999999997], [6, 25.259999999999998, 166.716, 359.97499999999997, 368.305]]
2026-08-10 18:09:26,516 INFO     29 [qwen-vl-text] ═══ DONE ═══ 21 positions, pages=1, time=10.3s
2026-08-10 18:09:26,516 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:09:26,518 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:09:26,518 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 18:09:26,518 INFO     29 [qwen-vl-text] positions(5): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:09:26,518 INFO     29 [qwen-vl-text] page grouping: [7], lines per page: [5]
2026-08-10 18:09:26,709 INFO     29 [qwen-vl-text] page=7, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 18:09:26,710 INFO     29 [qwen-vl-text] LLM extraction start, text_len=68
2026-08-10 18:09:26,710 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:09:26,711 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 201, \"bbox_end\": 205, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "检查项目：十二通道 检查名称：十二通道 检查部位：\n□检查所见：\n□检查结论：\n1、窦性心动过速 2、ST段轻度改变\n报告医 审核医生：",
    "role": "user"
  }
]
2026-08-10 18:09:28,489 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:09:28,490 INFO     29 [qwen-vl-text] LLM output (len=311):
{
  "exam_date": null,
  "report_date": null,
  "exam_name": "十二通道",
  "exam_category": "other",
  "body_part": null,
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": null,
  "conclusion": "1、窦性心动过速 2、ST段轻度改变",
  "physician": null,
  "reviewer": null
}
2026-08-10 18:09:28,492 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1522471, prompt_len=695
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共5行）
["检查项目：十二通道 检查名称：十二通道 检查部位：", "□检查所见：", "□检查结论：", "1、窦性心动过速 2、ST段轻度改变", "报告医 审核医生："]

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
2026-08-10 18:09:31,220 INFO     29 [qwen-vl-text] coord API raw response (len=303):
```json
[
	{"text": "检查项目：十二通道 检查名称：十二通道 检查部位：", "bbox": [320, 387, 895, 413]},
	{"text": "□检查所见：", "bbox": [318, 467, 403, 491]},
	{"text": "□检查结论：", "bbox": [318, 557, 402, 580]},
	{"text": "1、窦性心动过速 2、ST段轻度改变", "bbox": [410, 607, 644, 630]},
	{"text": "报告医 审核医生：", "bbox": [451, 693, 819, 716]}
]
```
2026-08-10 18:09:31,220 INFO     29 [qwen-vl-text] coord API: raw_items=5, valid_items=5, elapsed=2.7s
2026-08-10 18:09:31,220 INFO     29 [qwen-vl-text] coord item[0]: text=检查项目：十二通道 检查名称：十二通道 检查部位：, bbox=[320, 387, 895, 413]
2026-08-10 18:09:31,221 INFO     29 [qwen-vl-text] coord item[1]: text=□检查所见：, bbox=[318, 467, 403, 491]
2026-08-10 18:09:31,221 INFO     29 [qwen-vl-text] coord item[2]: text=□检查结论：, bbox=[318, 557, 402, 580]
2026-08-10 18:09:31,221 INFO     29 [qwen-vl-text] coord item[3]: text=1、窦性心动过速 2、ST段轻度改变, bbox=[410, 607, 644, 630]
2026-08-10 18:09:31,221 INFO     29 [qwen-vl-text] coord item[4]: text=报告医 审核医生：, bbox=[451, 693, 819, 716]
2026-08-10 18:09:31,221 INFO     29 [qwen-vl-text] page=7 — 5/5 coords, api_time=2.7s
2026-08-10 18:09:31,221 INFO     29 [qwen-vl-text] new_positions (5):
[[7, 269.44, 753.5899999999999, 230.265, 245.73499999999999], [7, 267.756, 339.32599999999996, 277.865, 292.145], [7, 267.756, 338.484, 331.41499999999996, 345.09999999999997], [7, 345.21999999999997, 542.2479999999999, 361.16499999999996, 374.84999999999997], [7, 379.74199999999996, 689.598, 412.335, 426.02]]
2026-08-10 18:09:31,222 INFO     29 [qwen-vl-text] ═══ DONE ═══ 5 positions, pages=1, time=4.7s
2026-08-10 18:09:31,233 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 18:09:31,234 INFO     29 [Trace] task=d64c79b4 | doc=07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf | Extractor:ExaminationReport | outputs={"chunks": "5 items, types={'ExaminationReport': 5}", "html": "", "json": "417 items", "markdown": "", "text": "", "name": "07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Admission\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 18:09:31,234 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 18:09:31,240 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:09:31,240 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 18:09:31,724 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:09:31,732 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 18:09:31,732 INFO     29 [Trace] task=d64c79b4 | doc=07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "417 items", "markdown": "", "text": "", "name": "07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Admission\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 18:09:31,732 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 18:09:31,733 INFO     29 [ChunkMerger] Merged 10 chunks from 9 sources: {'Extractor:LabExam': 4, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 5, 'Extractor:Progress': 1} (filtered 6 noise chunks)
2026-08-10 18:09:31,741 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 18:09:31,741 INFO     29 [Trace] task=d64c79b4 | doc=07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "10 items, types={'LabReport': 4, 'AdmissionRecord': 1, 'ExaminationReport': 5}", "name": "07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf"}
2026-08-10 18:09:31,741 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 18:09:31,880 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786385029166, 'update_date': datetime.datetime(2026, 8, 10, 18, 3, 49), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1335042, 'status': '1'}
2026-08-10 18:09:32,083 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   天门冬氨酸氨基转移酶  None  19  U/L  15-40  False    AST/ALT  None  1.73  None  0.10-3.00  False    总胆红素  None  6.9  um  ≤23.0  False    直接胆红素  None  2.0  um  0-6.8  False    间接胆红素  None  4.9  um  3.4-17.1  False    总蛋白  None  64.1  g/L  65.0-85.0  True    白蛋白  None  29.8  g/L  40.0-55.0  True    球蛋白  None  34.3  g/L  20.0-40.0  False    白球比  None  0.87  None  1.20-2.40  True    碱性磷酸酶  None  95  U/L  45-125  False    谷氨酸脱氢酶  None  5  U/L  0-7  False    γ-谷氨酰转肽酶  None  20  U/L  10-60  False    胆碱酯酶  None  5357  U/L  5000-12000  False    甘胆酸  None  1.43  ug/  0.00-2.70  False    总胆汁酸  None  1.40  um  0.00-10.00  False    前白蛋白  None  100  mg  200-430  True    尿素  None  1.6  mm  3.1-8.0  True    肌酐  None  34.0  um  57-97  True    尿素/肌酐  None  0.05  None  0.01-0.70  False    估算肾小球滤过率  None  130  mL  None  False    葡萄糖  None  7.8  mm  3.9-6.1  True    尿酸  None  183  um  208-428  True    乳酸脱氢酶  None  241  U/L  120-250  False    肌酸激酶  None  36  U/L  50-310  True    钾  None  4.1  mm  3.5-5.3  False    钠  None  132  mm  137-147  True    氯  None  93  mm  99-110  True    总二氧化碳  TCO  30  mm  22-29  True    总钙  None  2.28  mm  2.11-2.52  False    磷  None  0.97  mm  0.85-1.51  False    镁  None  0.69  mm  0.75-1.02  True    阴离子间隙  None  9  mm  8-16  False    渗透压  None  264  mC  275-300  True    α-羟丁酸脱氢酶  None  154  U/L  72-182  False    唾液酸  None  1126  mg  456-754  True    淀粉酶  None  28  U/L  35-135  True    肌酸激酶同工酶质量  None  1.95  ng/  0-5.0  False   
---
   凝血酶原时间活动度  60110  84.89  %  70.0-130.0  False    凝血酶原时间比值  60120  1.16  None  0.82-1.15  True    国际标准化比值  60020  1.17  None  1.0-2.0;口服抗凝...  False    活化部分凝血活酶时间  60030  31.3  秒  20.5-33.4  False    活化部分凝血活酶时间比值  60031  1.18  None  0.77-1.25  False    纤维蛋白原  60040  9.170  g/L  2.00-4.00  True    凝血酶时间  60050  15.80  秒  15.2-22.0  False    D-二聚体  60070  0.55  mg/L  0.00-0.56  False    抗凝血酶活性  60080  100.74  %  80.0-120.0  False    纤维蛋白(原)降解产物  60130  3.53  mg/L  0.0-5.0  False   
---
   游离甲状腺素  None  14.70  pmol/L  12-22  False    促甲状腺激素  None  1.320  uIU/mL  0.27-4.2  False    鳞状细胞癌相关抗原  None  0.54  ng/ml  0-2.5  False    糖类抗原CA-50  None  3.73  IU/ml  0-25  False    糖类抗原CA-242  None  0.94  IU/ml  0-20  False    糖类抗原CA-724  None  0.95  U/mL  0-6.0  False    癌胚抗原  None  41.00  ng/ml  0-5.09  True    糖类抗原CA-199  None  9.28  U/mL  0.00-27.00  False    糖类抗原CA-125  None  21.50  U/mL  0.00-35.00  False    糖类抗原CA-153  None  15.40  U/mL  0.00-26.2  False    神经元特异性烯醇化酶  None  17.60  ng/ml  0.00-16.30  True    细胞角蛋白19片段  None  4.57  ng/ml  0.00-3.30  True    铁蛋白  None  416.00  ng/ml  30.00-400.00  True    β2微球蛋白  None  1.380  mg/L  0.90-2.70  False    胃泌素释放肽前体  None  22.100  pg/ml  0-68.3  False   
---
   中性粒细胞计数  None  13.55  *10^9/L  1.80-6.30  True    淋巴细胞计数  None  1.86  *10^9/L  1.10-3.20  False    单核细胞计数  None  1.32  *10^9/L  0.10-0.60  True    嗜酸细胞计数  None  0.00  *10^9/L  0.02-0.52  True    嗜碱细胞计数  None  0.07  *10^9/L  0.00-0.06  True    中性粒细胞百分比  None  80.6  %  40.0-75.0  True    淋巴细胞百分比  None  11.1  %  20.0-50.0  True    单核细胞百分比  None  7.9  %  3.0-10.0  False    嗜酸细胞百分比  None  0.0  %  0.40-8.00  True    嗜碱细胞百分比  None  0.4  %  0.00-1.00  False    红细胞计数  None  3.69  *10^12/L  4.30-5.80  True    血红蛋白含量  None  102  g/L  130-175  True    红细胞比容  None  0.32  L/L  0.40-0.50  True    平均红细胞血红蛋白含量  None  27.6  pg  27.0-34.0  False    平均红细胞血红蛋白浓度  None  318  g/L  316-354  False    平均红细胞体积  None  87.0  fL  82.0-100.0  False    红细胞分布宽度（CV）  None  17.3  %  11.6-16.5  True    红细胞分布宽度（SD）  None  54.6  fL  37.0-54.0  True    血小板计数  None  466  *10^9/L  125-350  True    平均血小板体积  None  8.8  fL  7.4-11.0  False    大血小板比率  None  15.7  %  13.0-43.0  False    血小板比容  None  0.41  %  0.170-0.350  True    血小板分布宽度  None  8.5  fL  9.6-15.2  True    C-反应蛋白  None  177  mg/L  0.000-5.000  True   
---
2026-03-04 15:46 入院记录
性别：男
职业：其他
年龄：57岁
入院时间：2026-03-04 15:38:00
民族：汉族
记录时间：2026-03-04 15:46
婚姻：已婚
病史陈述者：患者本人及家属
主诉：确诊左肺癌2年余，双下肢疼痛1周。
现病史：患者2年余前查体发现左颈部肿物，约豆粒大小，无疼痛，偶有咳嗽、咳痰，无痰中带血丝，活动后偶感胸闷、憋气，无咯血，无胸痛，无发热。后肿物逐渐增大，遂就诊于我院，2023-03-30行
PET/CT：1，左肺上叶高代谢占位，考虑肺癌（并累及邻近胸膜），（左侧颈部V区、左锁骨上、纵隔、左肺门10区、左肺内11-12区）多发淋巴结转移；建议病理学检查；左肺门10区淋巴结旁肺组织见网格样密度
增高影，轻度PDG代谢增高，建议结合临床并复查。未行特殊治疗。后就诊于我科，2023-04-03行快速石蜡病理诊断：（左锁骨上淋巴结穿刺活检）纤维组织内查见分化差的癌，结合免疫组化及病史，不除外肺非
小细胞癌转移。经齐鲁医院会诊：倾向肺腺癌。免疫组化结果：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（-）、P40（灶+）。2023-04-06行胸部增强CT：左肺上叶恶性肿瘤并累及邻近胸膜，左锁骨上、左
肺门及纵隔多发淋巴结转移。快速石蜡病理诊断：（左肺上叶穿刺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，特殊染色待补充报告。免疫组化结果：CK5/6（-）、P40（部分+）、
TTF-1（-）、NapsinA（-）、CK7（+）。ALK（D5F3）：阴性；（兔单克隆阴性对照：阴性；阳性对照：阳性）。2023-04-07至2023-06-30行替雷利珠单抗200mg免疫治疗+贝伐珠单抗注射液900.00mg靶向治
疗，联合卡铂500.00mg d1+培美曲塞二钠850.00mg d1化疗5周期。排除禁忌，患者于2023-07-06行胸部IMRT放疗，具体：IMRT,PTV 60GY/30F，末次放疗时间为2023-08-09。2023-07-19行卡铂500mg化疗联合恩度
靶向及替雷利珠单抗免疫治疗。2023-08-10予以患者恩度靶向及替雷利珠单抗免疫治疗。2024-09-30行顺铂40mgd1化疗，联合贝伐珠单抗注射液靶向、替雷利珠单抗免疫治疗。2024-11-6复查CT示：左肺上叶团片
影，较前2024.07.10范围增大，较2024.10.23示实性成分增多。病情较前进展。2024-11-07、2024-12-3行贝伐珠单抗800mg+替雷丽珠单抗200mg+顺铂80.00mg d1+紫杉醇脂质体270.00mg d1全身化疗2周期，因患
者消化道反应重，2025-1-16、2025-2-6行贝伐珠单抗800mg+替雷丽珠单抗200mg+顺铂60.00mg d1+紫杉醇脂质体240.00mg d1全身化疗2周。因出现消化道反应III级，后2025-3-25改行紫杉醇聚合物胶束300mgd1联
合卡铂400mgd1化疗，并行贝伐珠单抗800mg靶向联合替雷丽珠单抗200mg免疫治疗，2025-4-15行贝伐珠单抗800mgd0+替雷丽珠单抗200mgd0+紫杉醇聚合物胶束300mgd1+卡铂500mgd1，过程顺利。因医院紫杉醇聚合
物胶束无货，2025-5-7行顺铂80.00mg d1+紫杉醇脂质体270mg d1化疗1周期，2025-7-28至2025-12按期行卡铂500mg d1+紫杉醇聚合物胶束300mg，并行贝伐珠单抗注射液400mg靶向、（百泽安）替雷利珠单抗注射液
200.00mg d1免疫治疗。2026-01-19行注射用紫杉醇脂质体270mgd1+卡铂 500.00mg d1化疗1周期。2025-12-27行颈+胸部增强CT：肺癌复查：左肺团片影，较前2025-09-03增大；左肺门及纵隔多发肿大淋巴结，较
前部分增大。病情较前进展。1周前患者无明显诱因出现双下肢疼痛，间断性，走路踩棉花样，影响夜间睡眠。现为行进一步治疗收住我科。自发病以来，精神可，饮食、睡眠欠佳，大小便无异常，近1个月体重
较前无明显变化。
既往史：否认“冠心病、高血压、糖尿病”病史。否认“肝炎、结核”等传染病病史及密切接触史。否认重大外伤史，否认手术史，否认输血史。无药物及食物过敏。预防接种随当地进行。
个人史：生于原籍，无外地久居史，无疫区长期居住史，无聚集性发病。生活规律，吸烟30余年，约20支/天，偶有饮酒史，现烟酒均已戒2年，无毒物、粉尘及放射性物质接触史，无冶游史，无重大精神创
伤史。全程接种新冠疫苗。
婚育史：23岁结婚，配偶健在，育2女，女儿健康。
家族史：父亲去世（具体不详），母亲健在。兄弟2人，1个弟弟健在。家族中无遗传病病史及类似病史。
体 格 检 查
T:36.6℃ P:80次/分 R:20次/分 Bp:132/82mmHg VTE:3分
个人史：生于原籍，无外地久居史，无疫区长期居住史，无聚集性发病。生活规律，吸烟30余年，约20支/天，偶有饮酒史，现烟酒均已戒2年，无毒物、粉尘及放射性物质接触史，无冶游史，无重大精神创伤史，全程接种新冠疫苗。
婚育史：23岁结婚，配偶健在，育2女，女儿健康。
家族史：父亲去世（具体不详），母亲健在。兄弟2人，1个弟弟健在。家族中无遗传病病史及类似病史。
体格检查
T:36.6℃ P:80次/分 R:20次/分 Bp:132/82mmHg VTE:3分
H:168cm W:65kg S:1.71平方米 NRS:0分 PS:1分 NRS-2002:1分
中年男性，发育正常，营养中等，神志清楚，自主体位，正常面容，检查合作。全身皮肤、黏膜无苍白、紫绀、黄染，无水肿、皮疹、瘀点、紫癜、皮下结节，无蜘蛛痣、肝掌。全身浅表淋巴结未触及肿大，
局部皮肤无红肿、波动、压痛、瘘管。左侧锁骨上触及大约3×2cm肿物，质硬，固定，颈部柔软，双侧对称，颈静脉无怒张，肝颈静脉回流征阴性，无颈动脉异常搏动，气管位置居中，甲状腺无肿大，胸廓对
称，无畸形，胸骨无压痛，胸壁无皮下气肿及静脉曲张，呼吸节律正常。双侧呼吸活动度对称，双侧语音震颤正常，无胸膜摩擦感、皮下捻发感；叩诊双肺呈清音，两肺下界在锁骨中线第六肋间，腋中线第八肋
间，肩胛下角线第十肋间，肺下界活动度正常。双肺呼吸音粗，未闻及干湿性罗音，未闻及胸膜摩擦音。心前区无隆起，心尖搏动在锁骨中线第五肋间隙内侧0.5cm处，搏动范围及强度无异常，无震颤及心包摩擦
感。心脏左右浊音界正常。心音正常，心率76次/分，心律规整，各瓣膜听诊区无心音分裂、额外心音、杂音，无心包摩擦音。无毛细血管搏动、射枪音、水冲脉和无动脉异常搏动。腹部对称、平坦，无肠型及胃
肠蠕动波，无皮疹、色素、条纹，无腹壁静脉曲张，无疝和局部隆起，腹部柔软，腹无压痛、反跳痛，未触及包块，无液波震颤，肝脾肋下未触及。墨菲氏征阴性。腹部叩诊鼓音，肝上界在右锁骨中线第五肋
间，肝肾区无叩痛，无移动性浊音。肠鸣音正常4次/分，无振水音，无血管杂音。肛门直肠及外生殖器未检查。脊柱生理弯曲正常，无畸形，无压痛和叩击痛，活动自如，腰骶部无异常。四肢无畸形，肌张力正
常，关节无红肿，活动正常，双下肢无水肿及静脉曲张。腹壁反射、肱二、三头肌肌腱反射、膝腱反射、跟腱反射均正常存在；Babinski征阴性，Gordon征阴性，Oppenheim征阴性，Hoffmann征阴性；Kernig征阴
性，Brudzinski征阴性。
专科检查：双肺呼吸音粗，未闻及干湿性罗音，未闻及胸膜摩擦音。心音正常，心率76次/分，心律规整，腹部柔软，腹无压痛、反跳痛，未触及包块，无液波震颤，肝脾肋下未触及。
辅助检查
检查日期 检查项目 结果（检查医院）
2023-03-30 PET/CT：1，左肺上叶高代谢占位，考虑肺癌（并累及邻近胸膜），（左侧颈部V区、左锁骨上、纵隔、左肺门10区、左肺内11-12区）多发淋巴结转移；建议病理学检查；左肺门
10区淋巴结旁肺组织见网格样密度增高影，轻度PDG代谢增高，建议结合临床并复查。2.双肺肺气肿；双肺少许纤维条索灶。3.副鼻窦炎（双侧上颌窦、右侧筛窦）。4.冠状动脉钙化灶。5.十二指肠圈小憩室。6.
肝脏囊肿。7.左肾囊肿。8.脊椎骨质增生；骶3水平椎管囊肿。（本院）
2023-04-03 （左锁骨上淋巴结穿刺活检）纤维组织内查见分化差的癌，结合免疫组化及病史，不除外肺非小细胞癌转移。免疫组化结果：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（-）、
P40（灶+）。（本院）经齐鲁医院会诊：倾向肺腺癌。
2023-04-03 颅脑磁共振平扫+DVI+增强扫描MRI：脑内多发缺血灶，建议复查双侧上颌窦囊肿。（本院）
2023-04-06 胸部CT增强扫描CT：1.左肺上叶恶性肿瘤并累及邻近胸膜，左锁骨上、左肺门及纵隔多发淋巴结转移 2.双肺肺气肿；双肺少许纤维条索灶 3.冠状动脉钙化灶 4.扫及肝囊肿、左
肾囊肿。（本院）
2023-04-10 快速石蜡病理诊断：（左肺上叶穿刺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，特殊染色待补充报告。免疫组化结果：CK5/6（-）、P40（部分
+）、TTF-1（-）、NapsinA（-）、CK7（+）。ALK（D5F3）：阴性；（免单克隆阴性对照：阴性；阳性对照：阳性）。（本院）
2023-04-05 基因检测：未检出与靶向治疗相关基因突变；PD-L1检测：TPS约3%。（赛泽检验）
2023-07-20 胸部CT：1.肺癌复查：左肺上叶占位，较前（2023-06-30）范围缩小；左锁骨上、左肺门及纵隔多发淋巴结转移，较前变化不大 2.双肺肺气肿；双肺少许纤维条索灶 3.主动脉及
2023-07-20
胸部CT：1.肺癌复查：左肺上叶占位，较前（2023-06-30）范围缩小；左锁骨上、左肺门及纵隔多发淋巴结转移，较前变化不大2.双肺肺气肿；双肺少许纤维条索灶3.主动脉及
冠状动脉钙化4.扫及肝囊肿胸部CT平扫，下腹部（肾）CT平扫，上腹部CT平扫，盆腔CT平扫CT（2023-08-11）：1.肺癌复查：左肺上叶占位，范围较前（2023-7-20）减小；左锁骨上、左肺门及纵隔多发稍大淋巴
结，较前变化不大2.双肺肺气肿；双肺少许条索灶3.主动脉及冠状动脉钙化4.肝囊肿5.左肾稍低密度灶，建议超声检查；左肾囊肿6.十二指肠降段憩室7.右侧髂骨稍高密度灶，建议复查8.考虑骶管（S3-4
水平）囊肿。（本院）
2025-03-11
颈部+胸部增强CT：1.肺癌复查：左肺团片影，较前25.2.6范围相仿；2.双肺微小结节，原左肺新增结节较前略小（im149薄层），转移不除外，余较前相仿，定期复查；3.双肺
肺气肿；双肺条索灶；4.左肺门及纵隔多发稍大淋巴结，较前相仿；5.主动脉及冠状动脉钙化；心包少量积液；左侧胸膜局限性增厚；6.扫及肝囊肿；左肾囊肿。（本院）
2025-09-02
颅脑磁共振成像+DWI（特殊序列成像）MR：考虑脑内多发小缺血灶，较前（2024-11-8）变化不著，建议复查。左侧上颌窦囊肿。（本院）
2025-09-03
颈部CT增强扫描，胸部CT增强扫描，上腹部CT增强扫描，盆腔CT增强扫描，下腹部CT增强扫描：1.肺癌复查：左肺团片影，较前2025.05.07范围略增大，建议复查2.双肺微小结节，
较前变化不大，转移不除外，建议定期复查3.双肺肺气肿；双肺条索灶4.左肺门及纵隔多发稍大淋巴结，较前略大5.主动脉及冠状动脉钙化；心包少量积液；左侧胸膜局限性增厚6.肝囊肿；左肾囊肿7.
十二指肠降段憩室8.右侧髂骨稍高密度灶，较前2024.11.06变化不大，建议复查9.考虑骶管囊肿10.颈部未见明显异常；扫及双侧上颌窦炎。（本院）
2025-12-27
颈+胸部增强CT：1.肺癌复查：左肺团片影，较前2025-09-03增大；周围新发实变及网格影，请结合临床，建议复查；2.双肺小结节及小斑片影，较前部分增大，部分新发，部分
变化不大，建议定期复查；3.双肺肺气肿；双肺条索灶；双肺胸膜下磨玻璃密度影，请结合临床随诊复查；4.左肺门及纵隔多发肿大淋巴结，较前部分增大；5.主动脉及冠状动脉钙化；心包少量积液；左侧胸
膜局限性增厚；左侧胸腔少量积液；6.扫及肝囊肿；左肾囊肿7.颈部未见明显异常；扫及双侧上颌窦炎。（本院）
初步诊断
1、左肺上叶癌腺癌cT3N3MOIIIC期
纵隔淋巴结转移
锁骨上淋巴结转移
肺门淋巴结转移
颈部淋巴结转移
2、肺气肿
3、鼻窦炎
4、肝囊肿
5、肾囊肿
6、上颌窦囊肿
我审核病史记录内容属实无遗漏，我交给医院的病例资料已收回，患方签字：
宗茹
---
姓名
性别：男
年龄：57
门诊号：
科别：
病区
床号
住院号：
取材部位：左肺
补充内容：
快速石蜡病理诊断：
（左肺活检）非小细胞癌伴坏死，结合免疫组化结果部分区域伴鳞状细胞癌分化，免疫组化
及特殊染色待补充报告。
免疫组化结果：CK5/6（-）、TTF-1（-）、NapsinA（-）、P40（部分+）、Villin（-）、CK7
（+）、CDX2（-）
ALK伴随诊断：
ALK（D5F3）：阴性；（兔单克隆阴性对照：阴性；阳性对照：阳性）
---
性别：男
年龄：57
门诊号：
科别：
床号
送检医生
住院号
病区
送检日期：2026-3-6 15:05:29
取材信息：
灰白灰红条状碎组织一堆，共计直径0.8cm。
病理诊断：
快速石蜡病理诊断：
（左肺活检）分化差的癌，待免疫组化结果进一步明确分型。
---
病理会诊报告单
病理号:
姓名
性别: 男
年龄: 54岁
送检单位
送检日期: 2023/4/4
送检医生:
镜下所见:
原病理诊断:
读“青岛市中心医疗集团”报告, 病理号: 2307637, HE×1, IHC*5, 原诊断: (左锁骨上淋
巴结穿刺活检) 纤维组织内查见分化差的癌, 结合免疫组化及病史, 不除外肺非小细胞癌转
移。
免疫组化结果: TTF-1 (-), NapsinA (-), CK7 (+), CK 5/6 (-), P40 (灶+)。
病理会诊诊断:
(左锁骨上淋巴结穿刺活检) 纤维组织内查见片状、实体状异型上皮样细胞浸润, 结合临床及
免疫标记, 考虑低分化癌, 可能为肺非小细胞癌转移, 倾向腺癌, 建议粘液染色进一步协助诊
断。
原单位免疫组化结果: TTF-1 (-), NapsinA (-), CK7 (+), CK 5/6 (-), P40 (个别细胞
+)。
报告时间:2023-4-4
诊断医师:姜慧峰
注: 病理医师个人会诊咨询意见, 仅供原病理学
开始 | 病历列表
---
检查项目：
胸部磁共振平扫+DWI+动态增强成像
影像登录号：
MR10060372
报告状态：
Correction
原因：
不可选
主要位置：
2328
检查日期：
2026/3/9 7:44:30
顺序 #：
MR10060372
影像诊断
左肺癌复查所见。
纵隔内多发淋巴结肿大。
肝脏、左肾多发囊肿。
影像表现
左上肺示一截面约99x61mm的团块影，呈等长T1等长T2、DWI等高信号，不均匀强化，左上肺门及纵隔与之紧密相贴。右肺未见明显异常信号影，右肺门未见明显增大。纵隔内隆凸下示多发稍大淋巴结，心影大小形态可。未见明显胸腔积液。肝脏、左肾示
多发囊状长T1长T2信号影，大者直径约21mm。
---
检查项目：十二通道 检查名称：十二通道 检查部位：
□检查所见：
□检查结论：
1、窦性心动过速 2、ST段轻度改变
报告医 审核医生：
2026-08-10 18:09:32,823 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 18:09:32,823 INFO     29 [Trace] task=d64c79b4 | doc=07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "10 items, types={'LabReport': 4, 'AdmissionRecord': 1, 'ExaminationReport': 5}", "name": "07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf", "embedding_token_consumption": 7932}
2026-08-10 18:09:32,823 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 18:09:33,084 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 18:09:33,084 INFO     29 [Trace] task=d64c79b4 | doc=07-毓璜顶-SZFU，后线肺癌，方穹招募推荐.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":10,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 18:09:33,088 INFO     29 [DIAG-EXECUTOR] row_position_int len=37 row[0]=(9, 88, 192, 58, 74) row[-1]=(9, 88, 191, 746, 758)
2026-08-10 18:09:33,088 INFO     29 [DIAG-EXECUTOR] row_position_int len=10 row[0]=(10, 97, 193, 97, 111) row[-1]=(10, 97, 204, 269, 282)
2026-08-10 18:09:33,088 INFO     29 [DIAG-EXECUTOR] row_position_int len=15 row[0]=(11, 85, 172, 96, 110) row[-1]=(11, 85, 173, 374, 387)
2026-08-10 18:09:33,088 INFO     29 [DIAG-EXECUTOR] row_position_int len=24 row[0]=(12, 76, 154, 67, 81) row[-1]=(12, 76, 136, 522, 535)
2026-08-10 18:09:33,089 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 18:09:33,089 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 18:09:33,089 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 18:09:33,089 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 18:09:33,089 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 18:09:33,089 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 18:09:33,093 INFO     29 set_progress(d64c79b494e511f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 18:09:33 [DOC Engine]:
Start to index...
2026-08-10 18:09:33,107 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.008s]
2026-08-10 18:09:33,111 INFO     29 set_progress(d64c79b494e511f1bd9827cf206dfa2d), progress: 0.81, progress_msg: 
2026-08-10 18:09:33,125 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.007s]
2026-08-10 18:09:33,136 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.006s]
2026-08-10 18:09:33,142 INFO     29 set_progress(d64c79b494e511f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 18:09:33 Indexing done (0.05s). Task done (323.01s)
2026-08-10 18:09:33,145 INFO     29 [Done], chunks(10), token(7932), elapsed:323.01
2026-08-10 18:09:33,365 INFO     29 handle_task done for task {"id": "d64c79b494e511f1bd9827cf206dfa2d", "doc_id": "d60771c094e511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-SZFU\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 5825068, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786385028897, "task_type": "dataflow", "root_trace_id": "93629fbf7f764cf397a9e7f896dd05c6", "root_traceparent": "00-93629fbf7f764cf397a9e7f896dd05c6-e7dded3dfece48a2-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
