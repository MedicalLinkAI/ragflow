# 基准结果：07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf

## 基本信息

- 文件：`07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf`
- 大小：11225.9 KB
- PDF 总页数：14
- doc_id：`a646f41e94e611f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-11T02:09:36  完成时间：2026-08-11T02:16:07  耗时：391.2s
- progress_msg：`18:16:06 Indexing done (0.09s). Task done (361.51s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 0639b6cb | 1 | 2-2 | 康复大学青岛中心医院 门诊病历 姓名： 性别：男 出生日期：19 龄：53岁 门 |
| 2 | 18595845 | 1 | 3-3 | 青岛大学附属医院 市南院区 病理检查诊断报告 病理号 姓名 性别：男 年龄：51 |
| 3 | 7740bc71 | 1 | 4-4 | 青岛大学附属医院 市南院区 病理检查诊断报告 病理号. 姓  夕 性  别：男  |
| 4 | 54f39f12 | 2 | 5-6 | 青岛市中心医疗集团 2.检测结果总览 本检测基于MGI（DNBSeq T7）测序 |
| 5 | 4562e1e4 | 2 | 7-8 | 报告单详情 www.jkqd.org.cn 20260307检 查 1.双肺多发 |
| 6 | bf9b0f13 | 1 | 9-9 | <table><tr><td>唾液酸</td><td>SA</td><td>96 |
| 7 | c00c9cd9 | 1 | 10-10 | <table><tr><td>凝血酶原时间</td><td>PT</td><td |
| 8 | abbe06f7 | 1 | 12-12 | <table><tr><td>粪便颜色</td><td>Colour</td>< |
| 9 | 8f73a2e9 | 1 | 14-14 | <table><tr><td>乙型肝炎病毒表面抗原</td><td>HBsAg< |
| 10 | 07f42712 | 1 | 9-9 | <table><tr><td>丙氨酸氨基转移酶</td><td>ALT</td> |
| 11 | f5433495 | 1 | 11-11 | <table><tr><td>白细胞计数</td><td>WBC</td><td |
| 12 | 58a29619 | 1 | 13-13 | <table><tr><td>红细胞计数</td><td>RBC</td><td |

- chunks 总数：12
- 各 chunk 页数合计（含跨页重复）：14
- 页码并集：`[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`
- 覆盖页数：13 / 14；缺失页：`[1]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：❌ 未完全覆盖：覆盖 13/14 页，缺失 [1]，超范围 []**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 1 | 0 | 1 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 4 | 4 | 4 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 7 | 0 | 7 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 1, "ExaminationReport": 4, "LabReport": 7}`
- ChunkMerger：`{"found": true, "merged": 12, "sources": 9, "stats": {"Extractor:LabExam": 7, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 4, "Extractor:Progress": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 18:16:05,056 INFO     29 [ChunkMerger] Merged 12 chunks from 9 sources: {'Extractor:LabExam': 7, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 18:09:39,300 INFO     29 handle_task begin for task {"id": "a677452e94e611f1bd9827cf206dfa2d", "doc_id": "a646f41e94e611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 11495294, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385378144, "task_type": "dataflow", "root_trace_id": "971de7c4c0604c27afceabc8ac295233", "root_traceparent": "00-971de7c4c0604c27afceabc8ac295233-de3f877b239fe0d8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 18:09:39,495 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 18:09:39,605 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 18:09:39,619 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:09:39,619 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 18:09:39,619 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 18:09:39,629 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 18:09:39,629 INFO     29 ============================================================
2026-08-10 18:09:39,629 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 18:09:39,629 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 18:09:39,629 INFO     29 ============================================================
2026-08-10 18:09:39,629 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 18:09:39,629 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 18:09:39,631 INFO     29 No torch found.
2026-08-10 18:09:41,020 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=14
2026-08-10 18:09:41,062 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=70848, prompt_len=764
2026-08-10 18:09:42,303 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:09:42,303 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 18:09:42,309 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=70848, prompt_len=401
2026-08-10 18:09:43,120 INFO     29 [qwen-vl-parser] text API response (len=100):
["20231129根治术，术后无治疗", "20240410肝转移，一线治疗奥沙+卡培", "20250620影像进展，二线治疗伊利替康+卡培+贝伐", "20251016影像进展，三线呋喹替尼"]
2026-08-10 18:09:43,120 INFO     29 [qwen-vl-parser] page=1 text: 4 lines (bbox 0-3)
2026-08-10 18:09:43,120 INFO     29 [qwen-vl-parser] page=1 text: 4 sections
2026-08-10 18:09:43,351 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2071922, prompt_len=764
2026-08-10 18:09:44,785 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 18:09:44,786 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 18:09:44,803 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2071922, prompt_len=401
2026-08-10 18:09:49,486 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:09:49.483+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 85, "failed": 0, "current": {"a677452e94e611f1bd9827cf206dfa2d": {"id": "a677452e94e611f1bd9827cf206dfa2d", "doc_id": "a646f41e94e611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 11495294, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385378144, "task_type": "dataflow", "root_trace_id": "971de7c4c0604c27afceabc8ac295233", "root_traceparent": "00-971de7c4c0604c27afceabc8ac295233-de3f877b239fe0d8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:09:52,667 INFO     29 [qwen-vl-parser] text API response (len=1406):
["康复大学青岛中心医院", "门诊病历", "姓名：", "性别：男", "出生日期：19", "龄：53岁", "门诊号", "科别：肿瘤内一科门诊", "就诊时间：2026-03-02 17:35:26", "主诉：乙状结肠癌术后复发，会阴区疼痛", "现病史：患者2023-11-29于青医附院行“腹腔镜中转乙状结肠癌根治术+直肠部分切除术+预防性回", "肠末端造口术+左侧输尿管支架植入术”，2023-11-30术后病理示：“浸润深度：侵达浆膜，切缘：", "小肠切缘（-），结肠切缘（-），其他：另见绒毛状-管状腺瘤，伴多灶高级别上皮内瘤变（多枚，直", "径0.3-1.5cm）。淋巴结：肠周（4/20）淋巴结内见癌转移；送检小肠系膜（0/3）淋巴结内未见癌转", "移。病理学分期：pT3N2aMx。术后恢复可，2024-4-10发现“肝转移”，一线行“奥沙利铂+卡培他", "滨”化疗。2025-06-13肠镜：直肠术后，吻合口占位Ca？肠镜病理：“（直肠吻合口）腺癌（中分", "化）。2025-06-20 PET/CT：1.直肠癌术后治疗后，肝转移瘤术后，现示：直肠吻合口区高代谢占位，", "符合肿瘤复发（并与前列腺、双侧精囊腺关系密切，建议MRI检查），盆腔直肠周围、腹腔（右半肠系", "膜区）、腹膜后（双侧髂内血管走行区、骶前区）多发淋巴结转移，双肺转移（两处）；右肺上叶实", "性小结节，无明显异常FDG代谢增高，不除外转移。提示吻合口复发、双肺转移，病情进展，二线给予", "“伊立替康脂质体43mg d1、2+卡培他滨1.5g d1-14”化疗2周期。基因检测（2025-07-02）：1.KRAS", "p.G12D突变丰度12.81%，NRAS突变阴性。2025-08-06行贝伐珠单抗400mg靶向治疗。2025-10-16复查", "CT：1.直肠术后，吻合区软组织影，考虑肿瘤复发，与前列腺分界不清，较2025.8.1范围略大；直肠", "周围、右腹膜后、骶前区多发淋巴结转移，部分较前略缩小，建议复查2.肝内多发转移瘤，较前进展", "3.肝囊肿。病情进展，患者既往接受过氟尿嘧啶类、奥沙利铂和伊立替康为基础的化疗，以及抗血管", "内皮生成因子治疗，病情进展，予呋喹替尼三线治疗。近期反复睾丸感染于泌尿外科行手术治疗，目", "前患者会阴区疼痛明显，NRS 3-5分，予止痛药物治疗，食欲差、乏力，夜间睡眠欠佳，外院2026-02-", "03血常规示血红蛋白80g/L。", "体格检查：双肺呼吸音粗，未闻及干湿啰音。。", "辅助检查结果：暂无", "初步诊断：结肠恶性肿瘤", "诊疗意见：1.(瑞乐芬)氨酚羟考酮片4盒间隔6小时1片口服×12天", "2.蒙脱石散5盒日三次3g口服×25天", "3.(易蒙停)盐酸洛哌丁胺胶囊10盒日三次2mg口服×25天", "门诊病历专用章", "3702080719401", "医生签名：梁华", "门诊健康教育记录单", "教育对象：", "患者及家属", "疾病预防：", "烟草有害健康，远离烟草。", "病情和诊断：", "告知主要病情和诊断，不适随诊。", "用药知识：", "告知药物名称、用途、主要副作用、注意事项等。", "温馨提示：此病历只打印一次，请妥善保管！", "第1页", ""]
2026-08-10 18:09:52,668 INFO     29 [qwen-vl-parser] page=2 text: 48 lines (bbox 4-51)
2026-08-10 18:09:52,668 INFO     29 [qwen-vl-parser] page=2 text: 48 sections
2026-08-10 18:09:52,827 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1360930, prompt_len=764
2026-08-10 18:09:54,299 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2024-04-11"
}
```
2026-08-10 18:09:54,299 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=2024-04-11
2026-08-10 18:09:54,312 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1360930, prompt_len=401
2026-08-10 18:10:00,166 INFO     29 [qwen-vl-parser] text API response (len=1068):
["青岛大学附属医院", "市南院区", "病理检查诊断报告", "病理号", "姓名", "性别：男", "年龄：51岁", "送检单位：青岛大学附属医院市 送检科室：胃肠外科", "收到日期：2024-04-11", "送检医生：赵蕊蕊", "病区：胃肠外科病区", "住院号：", "送检材料：肝肿物，造口端回肠，直肠息", "临床诊断：1.乙状结肠恶性肿瘤,2.回肠造口状态", "大体检查:", "肝肿物：肝组织一件，大小4*3*2cm，剖开，距离肝断端0.4cm见一灰白肿物，范围", "0.5*0.4cm，质软，紧邻肝被膜0.5cm，其余肝组织灰红灰黄质软。", "造口组织一件，大小6.5*5*3cm，皮肤范围4*2.5cm，连接肠管两段，长分别为", "3cm、3.5cm，直径分别为1.5cm、1.7cm，肠粘膜灰白灰红。", "直肠息肉1：息肉样物一枚，大小2*2*1cm，未见明显蒂部及基底，于疑似基底处涂", "墨。", "直肠息肉2：息肉样物一枚，大小2*1*0.8cm，未见明显蒂部。", "直肠息肉3：息肉样物三枚，大小1.5*1*0.6cm，中者大小1*1*0.5cm，小者大小", "0.7*0.6*0.4cm，未见明显蒂部及基底。", "病理诊断:", "1、（肝肿物）肝组织内见中分化腺癌浸润，结合形态、病史及免疫组化结果，符合", "转移性肠腺癌。", "免疫组化结果：CK7（-），CK20（灶+），Arginase-1（-），CDX-2（+），SATB2", "（+），Ki-67（+，约80%）。", "2、（造口端回肠）皮肤及肠粘膜组织呈慢性活动性炎伴糜烂，复鳞上皮乳头状增", "生，间质纤维组织增生，血管扩张、充血及出血，部分区域肌层排列紊乱，符合造口", "改变。", "3、（直肠息肉1、2、3）均为绒毛状-管状腺瘤，部分腺体呈高级别上皮内瘤变，局", "灶癌变-中分化腺癌。", "免疫组化结果：CK-Desmin示未见确切粘膜肌。", "报告医生：张丽", "初诊医生：张晶晶", "报告日期：2024-04-19", "注：1.病理诊断分级注解：明确及基本明确的诊断，无任何修饰语；如有“考虑为”、“疑为”、“符合”、", "“不除外”及“可能性大”等修饰语，提示诊断具有不同程度的不确定性，请结合临床相关检查综合判断。", "2.如本诊断与临床表现及相关检查不符，请临床医生及时与病理科联系后再行处置。", "3.此报告以纸质版为准。", "审核专用章", "（4）"]
2026-08-10 18:10:00,166 INFO     29 [qwen-vl-parser] page=3 text: 44 lines (bbox 52-95)
2026-08-10 18:10:00,166 INFO     29 [qwen-vl-parser] page=3 text: 44 sections
2026-08-10 18:10:00,311 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1090603, prompt_len=764
2026-08-10 18:10:01,702 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-02-20"
}
```
2026-08-10 18:10:01,703 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=2025-02-20
2026-08-10 18:10:01,718 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1090603, prompt_len=401
2026-08-10 18:10:05,738 INFO     29 [qwen-vl-parser] text API response (len=707):
["青岛大学附属医院", "市南院区", "病理检查诊断报告", "病理号.", "姓  夕", "性  别：男", "年  龄：52", "送检单位：青岛大学附属医院市 送检科室：消化内科", "收到日期：", "送检医生：李晓宇", "病  区：", "住院号：", "送检材料：肠镜活检", "临床诊断：直肠多发息肉完成ESD吻合口溃疡", "大体检查:", "直肠息肉ESD：粘膜组织一件，大小3.5*2.5*0.8cm，距一侧切缘0.1cm，距另一侧", "切缘0.4cm，粘膜表面见一隆起，范围3*2.3cm，切面灰白质脆，基底涂墨。", "直肠吻合口：粘膜组织三块，合计直径0.4cm。", "病理诊断:", "1.标本类型：直肠息肉ESD", "标本数量：1件", "病变数量：1灶", "病变范围：3*2.3cm", "组织学类型：绒毛状--管状腺瘤伴高级别上皮内瘤变，局灶区域恶变--中分化腺癌，", "局限于粘膜层内", "脉管癌栓：（-）", "神经侵犯：（-）", "水平切缘：（-）", "垂直切缘：（-）", "2.（直肠吻合口）腺癌（中分化）。", "免疫组化结果示（直肠息肉ESD）：MLH1（+），MSH2（+），MSH6（+），PMS2", "(+），p53（+，约20%），CK-Desmin示粘膜肌连续，HER2（1+），S100示神经侵犯", "（-），CD31及D2-40示脉管癌栓（-），Ki-67（+，约60%）。", "报告医生：李丹", "初诊医生：赵玉洁", "报告日期：2025-02-20", "注：1.病理诊断分级注解：明确及基本明确的诊断", ""]
2026-08-10 18:10:05,739 INFO     29 [qwen-vl-parser] page=4 text: 37 lines (bbox 96-132)
2026-08-10 18:10:05,739 INFO     29 [qwen-vl-parser] page=4 text: 37 sections
2026-08-10 18:10:05,870 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1083893, prompt_len=764
2026-08-10 18:10:09,327 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:10:09,327 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 18:10:09,335 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1083893, prompt_len=401
2026-08-10 18:10:16,423 INFO     29 [qwen-vl-parser] text API response (len=1563):
["青岛市中心医疗集团", "2.检测结果总览", "本检测基于MGI（DNBSeq T7）测序平台对样本进行高通量测序。覆盖肿瘤相关的566个基因，检测内容包含目标基", "因覆盖范围内的单核苷酸变异、小片段插入/缺失、拷贝数变异、重排（融合），以及微卫星不稳定性（MSI）分析、肿瘤", "突变负荷（TMB）分析等。", "检测类别", "检测结果", "基因变异1", "体系", "I类（具有明确临床意义的变异）：KRAS p.G12D, KRAS p.A146V", "II类（具有潜在临床意义的变异）：TP53 p.G245D, FBXW7 p.R367*", "III类（临床意义不确定的变异）：RBM10 p.R97*, MUC16 p.A7208T, ALDH2 p", ".A5T, MTOR p.G1491S, CARD11 p.R207C等26个", "胚系", "致病性/疑似致病性变异：APC p.L180Yfs*5", "靶向药物提示", "KRAS p.G12D提示：司美替尼(C级)、Avutometinib and defactinib (C级)可能敏感；西妥昔单抗(A级)、Panitumumab (A级)可能耐药。", "KRAS p.A146V提示：Avutometinib and defactinib (C级)可能敏感；西妥昔单抗(A级)、Pan", "itumumab (A级)可能耐药。", "TP53 p.G245D提示：AZD1775 (C级)可能敏感。", "FBXW7 p.R367*提示：恩替司他(D级)、Belinostat (D级)可能敏感。", "APC p.L180Yfs*5提示：达沙替尼(D级)、厄洛替尼(D级)可能敏感。", "诊断/预后提示", "目前暂未发现与本癌种诊断/预后相关的基因变异。", "免疫治疗疗效提示", "TMB(同义突变&非同义突变)", "13.89Muts/Mb", "TMB(非同义突变)", "10.42Muts/Mb (前12.62%)", "MSI状态", "MSS (微卫星稳定)", "其他潜在免疫疗效相关标志物2", "正相关：未检出", "负相关：未检出", "超进展相关：未检出", "化疗用药提示", "可能药物敏感性较高：暂无，详见实验结果", "可能毒副作用风险较低：卡培他滨，伊立替康", "肿瘤遗传风险提示", "检出APC p.L180Yfs*5疑似致病性变异，建议对受检者及血亲进行适当的遗传咨询或临床管理", "注：1. 基因变异", "58", "青岛市中心医疗集团", "(1) 体系变异参考AMP/ASCO/CAP 共识《Standards and Guidelines for the Interpretation and Reporting of", "Sequence Variants in Cancer》，基因变异按照临床意义的重要性分为四个类别", "I类：具有明确临床意义的变异，包括NMPA、FDA批准疗法，或专业临床指南（如CSCO诊疗指南、NCCN临", "床实践指南）推荐（A级证据），或基于证据充分的临床研究，并获得专家共识有明确治疗、诊断、预后的", "变异（B级证据）；", "II类：具有潜在临床意义的变异，包括其他癌种的A级证据（跨适应症用药），或多项小型临床研究支持，或", "已作为当前临床研究的入组标准（C级证据），或临床前研究或案例报道，未获得专家共识的药物（D级证", "据）；", "III类：临床意义不确定的变异（尚无相关临床证据）", "“类：下事或示能于事的变异（在全人群或特定人群数据库中观察到高变异率）", "扫描全能王 创建"]
2026-08-10 18:10:16,424 INFO     29 [qwen-vl-parser] page=5 text: 54 lines (bbox 133-186)
2026-08-10 18:10:16,424 INFO     29 [qwen-vl-parser] page=5 text: 54 sections
2026-08-10 18:10:16,540 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1005421, prompt_len=764
2026-08-10 18:10:17,883 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:10:17,884 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-10 18:10:17,899 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1005421, prompt_len=401
2026-08-10 18:10:21,684 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:10:21.681+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 85, "failed": 0, "current": {"a677452e94e611f1bd9827cf206dfa2d": {"id": "a677452e94e611f1bd9827cf206dfa2d", "doc_id": "a646f41e94e611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 11495294, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385378144, "task_type": "dataflow", "root_trace_id": "971de7c4c0604c27afceabc8ac295233", "root_traceparent": "00-971de7c4c0604c27afceabc8ac295233-de3f877b239fe0d8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:10:26,970 INFO     29 [qwen-vl-parser] text API response (len=1917):
["青岛市中心医疗集团", "3.基因变异临床意义综合提示", "3.1诊断/预后及靶向药物提示", "基因变异1", "突变丰度2/拷贝数", "变异分类", "可能敏感药物", "可能耐药药物", "突变说明", "KRAS", "NM_004985.5", "12.81%", "I类", "司美替尼(C级)", "西妥昔单抗(A", "级)", "KRAS基因的G12D突变，发生在第", "2号外显子，位于GTP结合蛋白结", "构域(UniProt.org)，突变导致", "第12位氨基酸由甘氨酸变为天冬氨", "酸，G12突变将降低自身的GTP酶", "活性，使KRAS长期处于与GTP结", "合的激活状态，导致细胞增殖异常", "(PMID:12509763,20736745,2", "6037647,6092966)，为功能获", "得突变。", "exon2", "p.G12D", "c.35G>A", "Avutometinib a", "nd defactinib(C", "级)", "Pantitumuma", "b(A级)", "KRAS", "NM_004985.5", "1.46%", "I类", "Avutometinib a", "nd defactinib(C", "级)", "西妥昔单抗(A", "级)", "KRAS基因的A146V突变，发生在", "第4号外显子，突变导致146位氨基", "酸由丙氨酸变为缬氨酸，为功能获", "得突变。在两个不同的细胞系中，", "与野生型Kras相比，A146V可能会", "降低Kras的GTPase活性，从而导", "致下游通路激活增加(PMID:205", "70890)，与野生型Kras相比，A1", "46V突变会增加细胞增殖和细胞活", "力(PMID:29533785)，为功能", "获得突变。", "exon4", "p.A146V", "c.437C>T", "Panitumuma", "b(A级)", "TP53", "NM_000546.6", "12.73%", "II类", "AZD1775(C级)", "TP53基因的G245D突变，发生在", "第7号外显子，位于Tp53蛋白的D", "NA结合域(PMID:22713868)", "，突变导致245位甘氨酸变为天冬", "氨酸。G245D导致Tp53靶基因的", "激活减少(PMID:22214764,256", "34208,27533082)，为功能丧失", "突变。", "exon7", "p.G245D", "c.734G>A", "FBXW7", "NM_033632.3", "2.75%", "II类", "恩替司他(D级)", "FBXW7基因的R367*突变，发生在", "第7号外显子，突变导致终止密码", "子提前编码(UniProt.org)。由于W", "D重复域的丢失，预测R367*会导", "致Fbxw7蛋白功能的丢失(UniProt", ".org)。", "exon7", "p.R367*", "c.1099C>T", "Belinostat(D级)", "APC", "NM_000038.6", "杂合", "II类", "达沙替尼(D级)", "APC基因的p.L180Yfs*5、c.539de", "l突变，发生在第6外显子，不在已", "知功能域内(UniProt.org)，突", "变导致其编码的氨基酸在180位开", "始框移，可能影响蛋白功能(Uni", "Prot.org)。已知APC的功能丧失", "变异具有致病性(PMID:17963004", ",20685668)。Clinvar数据库记录", "该变异为Pathogenic。其在人群", "基因组数据库未收录。综上分析，", "该突变是一个疑似致病性变异。", "exon6", "p.L180Yfs*5", "c.539del", "厄洛替尼(D级)", "注:1.基因变异：“exon”为外显子，“intron”为内含子，“c”为DNA序列，“p”为蛋白质，“NM”为基因的转录", "本编号;", "2.突变丰度:在某位点产生突变的等位基因在该位点全部等位基因中所占比率。例如,突变丰度10%意为该位点含", "有10%的突变等位基因和90%的野生型等位基因。拷贝数:是指某一种基因或某一段特定的DNA序列在单倍体基", "因组中出现的数目。", "4/58", "青岛市中心医疗集团", "扫描全能王 创建"]
2026-08-10 18:10:26,971 INFO     29 [qwen-vl-parser] page=6 text: 118 lines (bbox 187-304)
2026-08-10 18:10:26,971 INFO     29 [qwen-vl-parser] page=6 text: 118 sections
2026-08-10 18:10:27,103 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1158323, prompt_len=764
2026-08-10 18:10:28,491 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:10:28,492 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-10 18:10:28,512 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1158323, prompt_len=401
2026-08-10 18:10:32,589 INFO     29 [qwen-vl-parser] text API response (len=707):
["19:08", "41", "×", "报告单详情", "www.jkqd.org.cn", "20260307检", "查", "1.双肺多发结节，较前2025-12-26部分缩", "小，考虑转移；/>右肺门区及纵隔内多发肿", "大淋巴结，考虑转移2.直肠术后，吻合区软", "组织影，考虑肿瘤复发，与前列腺分界不", "清，大致同前（2025-10-16）；/>直肠周", "围、右腹膜后、骶前区多发淋巴结转移，部", "分较前略缩小，建议复查3.肝内多发转移", "瘤，较前（2025-10-16）进展4.肝囊肿5.", "膀胱内气体，建议结合临床", "诊断意见", "骨性胸廓对称，纵隔气管居中。双肺支气管", "血管束增多。双肺见弥漫多发类圆形实性结", "节影，大者位于右肺下叶内基底段（薄层", "IM181），大小约为16×16mm，边界清，轻", "度均匀强化。气管及中心支气管通畅。右肺", "门区及纵隔内多发肿大淋巴结，最大者短径", "约14mm，轻度强化。心脏不大。双侧胸膜", "未见明显增厚。双侧胸腔内未见明显液体密", "度影。肝脏增大，肝内见多发类圆形稍低密", "度影，边界不清，大者长径约110mm，增强", "扫描边缘轻度强化。肝右叶可见直径3mm的", "无强化的囊性密度灶，边界清；/>肝内外胆", "管未见明显扩张。胆囊内未见异常密度影。", "胰腺、脾脏未见明显异常密度灶及异常强化", "灶。双肾上腺及双肾大小、形态、密度未见", "明显异常密度灶及异常强化灶。肠管未见梗", "阻征象。直肠术后直肠吻合口区见团片样", ">", "扫描全能王 创建"]
2026-08-10 18:10:32,590 INFO     29 [qwen-vl-parser] page=7 text: 36 lines (bbox 305-340)
2026-08-10 18:10:32,590 INFO     29 [qwen-vl-parser] page=7 text: 36 sections
2026-08-10 18:10:32,738 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1221041, prompt_len=764
2026-08-10 18:10:34,081 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-10-16"}
```
2026-08-10 18:10:34,082 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=2025-10-16
2026-08-10 18:10:34,092 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1221041, prompt_len=401
2026-08-10 18:10:37,753 INFO     29 [qwen-vl-parser] text API response (len=631):
["19:08", "41", "×", "报告单详情", "www.jkqd.org.cn", "瘤，较前（2025-10-16）进展 4. 肝囊肿 5.", "膀胱内气体，建议结合临床", "诊断意见", "骨性胸廓对称，纵隔气管居中。双肺支气管", "血管束增多。双肺见弥漫多发类圆形实性结", "节影，大者位于右肺下叶内基底段（薄层", "IM181），大小约为16×16mm，边界清，轻", "度均匀强化。气管及中心支气管通畅。右肺", "门区及纵隔内多发肿大淋巴结，最大者短径", "约14mm，轻度强化。心脏不大。双侧胸膜", "未见明显增厚。双侧胸腔内未见明显液体密", "度影。肝脏增大，肝内见多发类圆形稍低密", "度影，边界不清，大者长径约110mm，增强", "扫描边缘轻度强化。肝右叶可见直径3mm的", "无强化的囊性密度灶，边界清； />肝内外胆", "管未见明显扩张。胆囊内未见异常密度影。", "胰腺、脾脏未见明显异常密度灶及异常强化", "灶。双肾上腺及双肾大小、形态、密度未见", "明显异常密度灶及异常强化灶。肠管未见梗", "阻征象。直肠术后，直肠吻合口区见团片样", "软组织密度影，与前列腺分界不清，增强扫", "描不均匀强化。直肠周围、右腹膜后、骶前", "区见多发肿大淋巴结，大者短径约11mm，", "增强扫描不均匀强化。膀胱充盈良好，膀胱", "壁光整，膀胱内见气体影。盆腔未见明显积", "液。", ""]
2026-08-10 18:10:37,754 INFO     29 [qwen-vl-parser] page=8 text: 31 lines (bbox 341-371)
2026-08-10 18:10:37,754 INFO     29 [qwen-vl-parser] page=8 text: 31 sections
2026-08-10 18:10:37,879 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1082288, prompt_len=764
2026-08-10 18:10:41,438 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-07"
}
```
2026-08-10 18:10:41,438 INFO     29 [qwen-vl-parser] page=9 classify=table report_date=2026-03-07
2026-08-10 18:10:41,446 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1082288, prompt_len=756
2026-08-10 18:10:49,980 INFO     29 [qwen-vl-parser] table API response (len=1718):
\begin{tabular}{llllllll}
\hline
中文名称 & 英文缩写 & 结果 & 单位 & 提示 & 参考区间 & 检测方法 \\
\hline
1. 丙氨酸氨基转移酶**☆ & ALT & 12 & U/L & & 9-50 & 速率法 \\
2. 天门冬氨酸氨基转移酶**☆AST & & 30 & U/L & & 15-40 & 速率法 \\
3. AST/ALT & AST/ALT & 2.50 & & & 0.10-3.00 & 计算法 \\
4. 总胆红素**☆ & TBIL & 6.3 & umol/L & & ≤23.0 & 钒酸盐法 \\
5. 直接胆红素**☆ & DBIL & 2.1 & umol/L & & 0-6.8 & 钒酸盐法 \\
6. 间接胆红素 & IBIL & 4.2 & umol/L & & 3.4-17.1 & 计算法 \\
7. 总蛋白**☆ & TP & 66.9 & g/L & & 65.0-85.0 & 双缩脲法 \\
8. 白蛋白**☆ & ALB & 31.8 & g/L & ↓ & 40.0-55.0 & 溴甲酚绿法 \\
9. 球蛋白 & GLB & 35.1 & g/L & & 20.0-40.0 & 计算法 \\
10. 白球比 & A/G & 0.91 & & ↓ & 1.20-2.40 & 计算法 \\
11. 碱性磷酸酶**☆ & ALP & 240 & U/L & ↑ & 45-125 & 速率法 \\
12. 谷氨酸脱氢酶 & GLDH & 11 & U/L & ↑ & 0-7 & 速率法 \\
13. γ-谷氨酰转肽酶**☆ & GGT & 151 & U/L & ↑ & 10-60 & 速率法 \\
14. 胆碱酯酶**☆ & CHE & 4919 & U/L & ↓ & 5000-12000 & 速率法 \\
15. 甘胆酸 & CG & 1.61 & ug/ml & & 0.00-2.70 & 均相酶免法 \\
16. 总胆汁酸* & TBA & 4.20 & umol/L & & 0.00-10.00 & 酶循环法 \\
17. 前白蛋白*☆ & PA & 135 & mg/L & ↓ & 200-430 & 免疫比浊法 \\
18. 尿素**☆ & UREA & 4.7 & mmol/L & & 3.1-8.0 & 酶法 \\
19. 肌酐**☆ & CREA & 50.0 & umol/L & ↓ & 57-97 & 酶法 \\
20. 尿素/肌酐 & UREA/CREA & 0.09 & & & 0.01-0.70 & 计算法 \\
21. 估算肾小球滤过率 & eGFR & 119 & mL/min/1.73m2 & & & 计算法 \\
22. 尿酸**☆ & UA & 326 & umol/L & & 208-428 & 酶法 \\
23. 钾**☆ & K & 4.0 & mmol/L & & 3.5-5.3 & 电极法 \\
24. 钠**☆ & Na & 139 & mmol/L & & 137-147 & 电极法 \\
25. 氯**☆ & CL & 104 & mmol/L & & 99-110 & 电极法 \\
26. 总二氧化碳 & CO2 & 22 & mmol/L & & 22-29 & 酶法 \\
27. 阴离子间隙 & AG & 13 & mmol/L & & 8-16 & 计算法 \\
\hline
\end{tabular}

\begin{tabular}{llllllll}
\hline
中文名称 & 英文缩写 & 结果 & 单位 & 提示 & 参考区间 & 检测方法 \\
\hline
28. 唾液酸 & SA & 969 & mg/L & ↑ & 456-754 & 酶法 \\
29. 补体Clq & Clq & 16.5 & mg/dl & & 15.7-23.7 & 免疫比浊法 \\
\hline
\end{tabular}
2026-08-10 18:10:49,984 INFO     29 [qwen-vl-parser] page=9 table: 43 LaTeX lines (bbox 372-414)
2026-08-10 18:10:49,984 INFO     29 [qwen-vl-parser] page=9 table: 43 sections
2026-08-10 18:10:50,092 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=869618, prompt_len=764
2026-08-10 18:10:51,521 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-07"
}
```
2026-08-10 18:10:51,522 INFO     29 [qwen-vl-parser] page=10 classify=table report_date=2026-03-07
2026-08-10 18:10:51,540 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=869618, prompt_len=756
2026-08-10 18:10:53,826 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:10:53.823+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 85, "failed": 0, "current": {"a677452e94e611f1bd9827cf206dfa2d": {"id": "a677452e94e611f1bd9827cf206dfa2d", "doc_id": "a646f41e94e611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 11495294, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385378144, "task_type": "dataflow", "root_trace_id": "971de7c4c0604c27afceabc8ac295233", "root_traceparent": "00-971de7c4c0604c27afceabc8ac295233-de3f877b239fe0d8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:10:56,144 INFO     29 [qwen-vl-parser] table API response (len=958):
\begin{tabular}{llllllll}
\hline
中文名称 & 英文缩写 & 结果 & 单位 & 提示参考区间 & 检测方法 \\
\hline
1. 凝血酶原时间$\ast\ast\star$ & PT & 14.4 & 秒 & 10.70--14.80 & 凝固法 \\
2. 凝血酶原时间活动度 & PT\% & 85.00 & \% & 70.00--150.00 & 换算值 \\
3. 凝血酶原时间比值 & PT. R & 1.08 & & 0.82--1.15 & 换算值 \\
4. & PT. INR & 1.10 & & 1.0--2.0 & \\
\multicolumn{2}{l}{国际标准化比值$\ast\ast\star$} & & & \multicolumn{2}{l}{口服抗凝剂：换算值} \\
\multicolumn{2}{l}{} & & & \multicolumn{2}{l}{1.8--2.5} \\
5. 活化部分凝血活酶时间$\ast\ast\star$ & APTT & 43.2 & 秒 & $\uparrow$ 28.00--43.00 & 凝固法 \\
6. 活化部分凝血活酶时间比值 & APTT R & 1.27 & & $\uparrow$ 0.82--1.26 & 换算值 \\
7. 纤维蛋白原$\ast\ast$ & Fib & 6.490 & g/L & $\uparrow$ 2.000--4.000 & Clauss法 \\
8. 凝血酶时间$\ast\ast$ & TT & 17.10 & 秒 & 14.00--21.00 & 凝固法 \\
9. D-二聚体$\ast$ & D-Dimer & 3.20 & mg/L(FEU) & $\uparrow$ 0.00--0.50 & 免疫比浊法 \\
10抗凝血酶活性$\ast$ & AT:A & 92.00 & \% & 80.00--130.00 & 发色底物法 \\
11纤维蛋白(原)降解产物$\ast$ & FDP & 14.63 & mg/L & $\uparrow$ 0.00--5.00 & 免疫比浊法 \\
\hline
\end{tabular}
2026-08-10 18:10:56,145 INFO     29 [qwen-vl-parser] page=10 table: 20 LaTeX lines (bbox 415-434)
2026-08-10 18:10:56,145 INFO     29 [qwen-vl-parser] page=10 table: 20 sections
2026-08-10 18:10:56,274 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1239038, prompt_len=764
2026-08-10 18:10:57,600 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-07"
}
```
2026-08-10 18:10:57,600 INFO     29 [qwen-vl-parser] page=11 classify=table report_date=2026-03-07
2026-08-10 18:10:57,608 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1239038, prompt_len=756
2026-08-10 18:11:06,357 INFO     29 [qwen-vl-parser] table API response (len=1861):
\begin{tabular}{llllllll}
\hline
中文名称 & 英文缩写 & 结果 & 提示 & 参考区间 & 单位 & 检测方法 \\
\hline
1. 白细胞计数$\text{##}\star$ & WBC & 3.96 & & 3.50--9.50 & $*10^9/\text{L}$ & 仪器法 \\
2. 中性粒细胞计数 & NEUT\# & 2.89 & & 1.80--6.30 & $*10^9/\text{L}$ & 仪器法 \\
3. 淋巴细胞计数 & LYMPH\# & 0.65 & $\downarrow$ & 1.10--3.20 & $*10^9/\text{L}$ & 仪器法 \\
4. 单核细胞计数 & MONO\# & 0.30 & & 0.10--0.60 & $*10^9/\text{L}$ & 仪器法 \\
5. 嗜酸细胞计数 & EO\# & 0.10 & & 0.02--0.52 & $*10^9/\text{L}$ & 仪器法 \\
6. 嗜碱细胞计数 & BASO\# & 0.02 & & 0.00--0.06 & $*10^9/\text{L}$ & 仪器法 \\
7. 中性粒细胞百分比 & NEUT\% & 73.0 & & 40.0--75.0 & \% & 仪器法 \\
8. 淋巴细胞百分比 & LYMPH\% & 16.4 & $\downarrow$ & 20.0--50.0 & \% & 仪器法 \\
9. 单核细胞百分比 & MONO\% & 7.6 & & 3.0--10.0 & \% & 仪器法 \\
10. 嗜酸细胞百分比 & E0\% & 2.6 & & 0.40--8.00 & \% & 仪器法 \\
11. 嗜碱细胞百分比 & BASO\% & 0.4 & & 0.00--1.00 & \% & 仪器法 \\
12. 红细胞计数$\text{##}\star$ & RBC & 3.57 & $\downarrow$ & 4.30--5.80 & $*10^12/\text{L}$ & 仪器法 \\
13. 血红蛋白含量$\text{##}\star$ & HGB & 88 & $\downarrow$ & 130--175 & g/L & 仪器法 \\
14. 红细胞比容$\text{##}\star$ & HCT & 0.28 & $\downarrow$ & 0.40--0.50 & L/L & 仪器法 \\
15. 平均红细胞血红蛋白含量$\text{##}\star$ & MCH & 24.6 & $\downarrow$ & 27.0--34.0 & pg & 仪器法 \\
16. 平均红细胞血红蛋白浓度$\text{##}\star$ & MCHC & 319 & & 316--354 & g/L & 仪器法 \\
17. 平均红细胞体积$\text{##}\star$ & MCV & 77.2 & $\downarrow$ & 82.0--100.0 & fL & 仪器法 \\
18. 红细胞分布宽度（CV） & RDW--CV & 17.4 & $\uparrow$ & 11.6--16.5 & \% & 仪器法 \\
19. 红细胞分布宽度（SD） & RDW--SD & 50.1 & & 37.0--54.0 & fL & 仪器法 \\
20. 血小板计数$\text{##}\star$ & PLT & 268 & & 125--350 & $*10^9/\text{L}$ & 仪器法 \\
21. 平均血小板体积 & MPV & 8.2 & & 7.4--11.0 & fL & 仪器法 \\
22. 大血小板比率 & P--LCR & 14.8 & & 13.0--43.0 & \% & 仪器法 \\
23. 血小板比容 & PCT & 0.22 & & 0.170--0.350 & \% & 仪器法 \\
24. 血小板分布宽度 & PDW & 15.4 & $\downarrow$ & 15.5--16.8 & fL & 仪器法 \\
25. C--反应蛋白$\text{*}$ & CRP & 30.830 & $\uparrow$ & 0.000--5.000 & mg/L & 散射比浊法 \\
\hline
\end{tabular}
2026-08-10 18:11:06,359 INFO     29 [qwen-vl-parser] page=11 table: 32 LaTeX lines (bbox 435-466)
2026-08-10 18:11:06,360 INFO     29 [qwen-vl-parser] page=11 table: 32 sections
2026-08-10 18:11:06,456 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=704397, prompt_len=764
2026-08-10 18:11:07,931 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-07"
}
```
2026-08-10 18:11:07,931 INFO     29 [qwen-vl-parser] page=12 classify=table report_date=2026-03-07
2026-08-10 18:11:07,946 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=704397, prompt_len=756
2026-08-10 18:11:10,341 INFO     29 [qwen-vl-parser] table API response (len=445):
\begin{tabular}{llllllll}
\hline
中文名称 & 英文缩写 & 结果 & 单位 & 提示参考区间 & 检测方法 \\
\hline
1. 粪便颜色 & Colour & 黄色 & & 棕黄 & 手工法 \\
2. 粪便性状 & Stool-type & 软 & & 软 & 手工法 \\
3. 白细胞 & WBC & 未见 & /HPF & 0-3/阴性 & 手工法 \\
4. 红细胞 & RBC & 未见 & /HPF & 阴性 & 手工法 \\
5. 脂肪滴 & Fat droplet & 未见 & /HPF & 阴性 & 手工法 \\
6. 真菌 & Fungus & 未见 & /HPF & 阴性 & 手工法 \\
7. 寄生虫卵 & Parasitic ovum & 未见 & & 阴性 & 手工法 \\
8. 隐血试验 & OBT & 阳性反应 (+) & & A 阴性反应 (-) & 胶体金法 \\
\hline
\end{tabular}
2026-08-10 18:11:10,342 INFO     29 [qwen-vl-parser] page=12 table: 15 LaTeX lines (bbox 467-481)
2026-08-10 18:11:10,342 INFO     29 [qwen-vl-parser] page=12 table: 15 sections
2026-08-10 18:11:10,465 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1101605, prompt_len=764
2026-08-10 18:11:13,969 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-07"
}
```
2026-08-10 18:11:13,970 INFO     29 [qwen-vl-parser] page=13 classify=table report_date=2026-03-07
2026-08-10 18:11:13,982 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1101605, prompt_len=756
2026-08-10 18:11:20,331 INFO     29 [qwen-vl-parser] table API response (len=1271):
\begin{tabular}{l l l l l l l}
\hline
中文名称 & 英文缩写 & 结果 & 单位 & 提示参考区间 & 检测方法 \\
\hline
1. 红细胞计数 & RBC & 43.00 & 个/ul & $\uparrow$ 0.00--17.00 & \\
2. 白细胞计数 & WBC & 3117.00 & 个/ul & $\uparrow$ 0.00--28.00 & \\
3. 白细胞团 & WBCC & 180.00 & 个/ul & $\uparrow$ 0.00--2.00 & 仪器法 \\
4. 鳞状上皮细胞 & SQEP & 15.00 & 个/ul & 0.00--28.00 & 仪器法 \\
5. 非鳞状上皮细胞 & NSE & 0.00 & 个/ul & 0.00--6.00 & 仪器法 \\
6. 透明管型 & HYAL & 0.00 & 个/ul & 0.00--1.00 & 仪器法 \\
7. 病理管型 & UNCC & 1.00 & 个/ul & 0.00--1.00 & 仪器法 \\
8. 酵母 & BYST & 0.00 & 个/ul & 0.00--1.00 & 仪器法 \\
9. 未分类结晶 & UNCX & 49.00 & 个/ul & $\uparrow$ 0.00--28.00 & 仪器法 \\
10粘液丝 & MUCS & 12.00 & 个/ul & 0.00--46.00 & \\
11细菌 & BACT & 11801.00 & 个/ul & $\uparrow$ 0.00--340.00 & \\
12潜血**☆ & BLD & 痕量(++) & & 阴性(-) & 干化学法 \\
13白细胞酯酶* & LEU & 阳性(2+) & & 阴性(-) & 干化学法 \\
14亚硝酸盐**☆ & NIT & 阳性(2+) & & 阴性(-) & 干化学法 \\
15尿胆素原**☆ & UBG & Normal & & Normal & 干化学法 \\
16胆红素**☆ & BIL & 阴性(-) & & 阴性(-) & 干化学法 \\
17维生素C & VC & 阳性(+) & & 阴性(-) & 干化学法 \\
18蛋白质**☆ & PRO & 痕量(++) & & 阴性(-) & 干化学法 \\
19酸碱度**☆ & PH & 5.5 & & 5.0--8.0 & 干化学法 \\
20比密**☆ & SG & 1.025 & & 1.005--1.030 & 干化学法 \\
21葡萄糖**☆ & GLU & 阴性(-) & & 阴性(-) & 干化学法 \\
22酮体**☆ & KET & 阴性(-) & & 阴性(-) & 干化学法 \\
23颜色 & Colour & 黄色 & & & 手工法 \\
24透明度 & Clarity & 浑浊 & & & 手工法 \\
\hline
\end{tabular}
2026-08-10 18:11:20,334 INFO     29 [qwen-vl-parser] page=13 table: 31 LaTeX lines (bbox 482-512)
2026-08-10 18:11:20,334 INFO     29 [qwen-vl-parser] page=13 table: 31 sections
2026-08-10 18:11:20,431 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=633668, prompt_len=764
2026-08-10 18:11:21,783 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-07"
}
```
2026-08-10 18:11:21,783 INFO     29 [qwen-vl-parser] page=14 classify=table report_date=2026-03-07
2026-08-10 18:11:21,791 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=633668, prompt_len=756
2026-08-10 18:11:23,923 INFO     29 [qwen-vl-parser] table API response (len=402):
\begin{tabular}{llllllll}
\hline
中文名称 & 英文缩写 & 结果 & 单位 & 提示参考区间 & 检测方法 \\
\hline
1. 乙型肝炎病毒表面抗原$\ast\ast\star$ & HBsAg & $<0.05$ 阴性反应(-) & IU/ml & $<0.08$ & \\
2. 丙型肝炎病毒抗体$\ast\ast\star$ & HCV & 0.060 阴性反应(-) & & $<1$ & 化学发光法 \\
3. 梅毒螺旋体抗体$\ast\ast\star$ & antiTP & 0.0 阴性反应(-) & & 0.000-1.000 & 化学发光法 \\
4. 人免疫缺陷病毒抗体$\ast\ast\star$ & HIV Ab & 0.0 阴性反应(-) & & 0.000-1.000 & 化学发光法 \\
\hline
\end{tabular}
2026-08-10 18:11:23,923 INFO     29 [qwen-vl-parser] page=14 table: 11 LaTeX lines (bbox 513-523)
2026-08-10 18:11:23,924 INFO     29 [qwen-vl-parser] page=14 table: 11 sections
2026-08-10 18:11:23,924 INFO     29 [qwen-vl-parser] parse_pdf done: 524 sections from 14 pages.
2026-08-10 18:11:23,930 INFO     29 Close text detector.
2026-08-10 18:11:24,382 INFO     29 Close text recognizer.
2026-08-10 18:11:24,786 INFO     29 Close recognizer.
2026-08-10 18:11:25,195 INFO     29 Close recognizer.
2026-08-10 18:11:25,660 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 18:11:25,660 INFO     29 [Trace] task=a677452e | doc=07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf | Parser:MedLink | outputs={"html": "", "json": "524 items", "markdown": "", "text": "", "name": "07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf", "output_format": "json"}
2026-08-10 18:11:25,660 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 18:11:25,676 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:11:25,676 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 20231129根治术，术后无治疗\n[BBOX-1] 20240410肝转移，一线治疗奥沙+卡培\n[BBOX-2] 20250620影像进展，二线治疗伊利替康+卡培+贝伐\n[BBOX-3] 20251016影像进展，三线呋喹替尼\n[BBOX-4] 康复大学青岛中心医院\n[BBOX-5] 门诊病历\n[BBOX-6] 姓名：\n[BBOX-7] 性别：男\n[BBOX-8] 出生日期：19\n[BBOX-9] 龄：53岁\n[BBOX-10] 门诊号\n[BBOX-11] 科别：肿瘤内一科门诊\n[BBOX-12] 就诊时间：2026-03-02 17:35:26\n[BBOX-13] 主诉：乙状结肠癌术后复发，会阴区疼痛\n[BBOX-14] 现病史：患者2023-11-29于青医附院行“腹腔镜中转乙状结肠癌根治术+直肠部分切除术+预防性回\n[BBOX-15] 肠末端造口术+左侧输尿管支架植入术”，2023-11-30术后病理示：“浸润深度：侵达浆膜，切缘：\n[BBOX-16] 小肠切缘（-），结肠切缘（-），其他：另见绒毛状-管状腺瘤，伴多灶高级别上皮内瘤变（多枚，直\n[BBOX-17] 径0.3-1.5cm）。淋巴结：肠周（4/20）淋巴结内见癌转移；送检小肠系膜（0/3）淋巴结内未见癌转\n[BBOX-18] 移。病理学分期：pT3N2aMx。术后恢复可，2024-4-10发现“肝转移”，一线行“奥沙利铂+卡培他\n[BBOX-19] 滨”化疗。2025-06-13肠镜：直肠术后，吻合口占位Ca？肠镜病理：“（直肠吻合口）腺癌（中分\n[BBOX-20] 化）。2025-06-20 PET/CT：1.直肠癌术后治疗后，肝转移瘤术后，现示：直肠吻合口区高代谢占位，\n[BBOX-21] 符合肿瘤复发（并与前列腺、双侧精囊腺关系密切，建议MRI检查），盆腔直肠周围、腹腔（右半肠系\n[BBOX-22] 膜区）、腹膜后（双侧髂内血管走行区、骶前区）多发淋巴结转移，双肺转移（两处）；右肺上叶实\n[BBOX-23] 性小结节，无明显异常FDG代谢增高，不除外转移。提示吻合口复发、双肺转移，病情进展，二线给予\n[BBOX-24] “伊立替康脂质体43mg d1、2+卡培他滨1.5g d1-14”化疗2周期。基因检测（2025-07-02）：1.KRAS\n[BBOX-25] p.G12D突变丰度12.81%，NRAS突变阴性。2025-08-06行贝伐珠单抗400mg靶向治疗。2025-10-16复查\n[BBOX-26] CT：1.直肠术后，吻合区软组织影，考虑肿瘤复发，与前列腺分界不清，较2025.8.1范围略大；直肠\n[BBOX-27] 周围、右腹膜后、骶前区多发淋巴结转移，部分较前略缩小，建议复查2.肝内多发转移瘤，较前进展\n[BBOX-28] 3.肝囊肿。病情进展，患者既往接受过氟尿嘧啶类、奥沙利铂和伊立替康为基础的化疗，以及抗血管\n[BBOX-29] 内皮生成因子治疗，病情进展，予呋喹替尼三线治疗。近期反复睾丸感染于泌尿外科行手术治疗，目\n[BBOX-30] 前患者会阴区疼痛明显，NRS 3-5分，予止痛药物治疗，食欲差、乏力，夜间睡眠欠佳，外院2026-02-\n[BBOX-31] 03血常规示血红蛋白80g/L。\n[BBOX-32] 体格检查：双肺呼吸音粗，未闻及干湿啰音。。\n[BBOX-33] 辅助检查结果：暂无\n[BBOX-34] 初步诊断：结肠恶性肿瘤\n[BBOX-35] 诊疗意见：1.(瑞乐芬)氨酚羟考酮片4盒间隔6小时1片口服×12天\n[BBOX-36] 2.蒙脱石散5盒日三次3g口服×25天\n[BBOX-37] 3.(易蒙停)盐酸洛哌丁胺胶囊10盒日三次2mg口服×25天\n[BBOX-38] 门诊病历专用章\n[BBOX-39] 3702080719401\n[BBOX-40] 医生签名：梁华\n[BBOX-41] 门诊健康教育记录单\n[BBOX-42] 教育对象：\n[BBOX-43] 患者及家属\n[BBOX-44] 疾病预防：\n[BBOX-45] 烟草有害健康，远离烟草。\n[BBOX-46] 病情和诊断：\n[BBOX-47] 告知主要病情和诊断，不适随诊。\n[BBOX-48] 用药知识：\n[BBOX-49] 告知药物名称、用途、主要副作用、注意事项等。\n[BBOX-50] 温馨提示：此病历只打印一次，请妥善保管！\n[BBOX-51] 第1页\n[BBOX-52] 青岛大学附属医院\n[BBOX-53] 市南院区\n[BBOX-54] 病理检查诊断报告\n[BBOX-55] 病理号\n[BBOX-56] 姓名\n[BBOX-57] 性别：男\n[BBOX-58] 年龄：51岁\n[BBOX-59] 送检单位：青岛大学附属医院市 送检科室：胃肠外科\n[BBOX-60] 收到日期：2024-04-11\n[BBOX-61] 送检医生：赵蕊蕊\n[BBOX-62] 病区：胃肠外科病区\n[BBOX-63] 住院号：\n[BBOX-64] 送检材料：肝肿物，造口端回肠，直肠息\n[BBOX-65] 临床诊断：1.乙状结肠恶性肿瘤,2.回肠造口状态\n[BBOX-66] 大体检查:\n[BBOX-67] 肝肿物：肝组织一件，大小4*3*2cm，剖开，距离肝断端0.4cm见一灰白肿物，范围\n[BBOX-68] 0.5*0.4cm，质软，紧邻肝被膜0.5cm，其余肝组织灰红灰黄质软。\n[BBOX-69] 造口组织一件，大小6.5*5*3cm，皮肤范围4*2.5cm，连接肠管两段，长分别为\n[BBOX-70] 3cm、3.5cm，直径分别为1.5cm、1.7cm，肠粘膜灰白灰红。\n[BBOX-71] 直肠息肉1：息肉样物一枚，大小2*2*1cm，未见明显蒂部及基底，于疑似基底处涂\n[BBOX-72] 墨。\n[BBOX-73] 直肠息肉2：息肉样物一枚，大小2*1*0.8cm，未见明显蒂部。\n[BBOX-74] 直肠息肉3：息肉样物三枚，大小1.5*1*0.6cm，中者大小1*1*0.5cm，小者大小\n[BBOX-75] 0.7*0.6*0.4cm，未见明显蒂部及基底。\n[BBOX-76] 病理诊断:\n[BBOX-77] 1、（肝肿物）肝组织内见中分化腺癌浸润，结合形态、病史及免疫组化结果，符合\n[BBOX-78] 转移性肠腺癌。\n[BBOX-79] 免疫组化结果：CK7（-），CK20（灶+），Arginase-1（-），CDX-2（+），SATB2\n[BBOX-80] （+），Ki-67（+，约80%）。\n[BBOX-81] 2、（造口端回肠）皮肤及肠粘膜组织呈慢性活动性炎伴糜烂，复鳞上皮乳头状增\n[BBOX-82] 生，间质纤维组织增生，血管扩张、充血及出血，部分区域肌层排列紊乱，符合造口\n[BBOX-83] 改变。\n[BBOX-84] 3、（直肠息肉1、2、3）均为绒毛状-管状腺瘤，部分腺体呈高级别上皮内瘤变，局\n[BBOX-85] 灶癌变-中分化腺癌。\n[BBOX-86] 免疫组化结果：CK-Desmin示未见确切粘膜肌。\n[BBOX-87] 报告医生：张丽\n[BBOX-88] 初诊医生：张晶晶\n[BBOX-89] 报告日期：2024-04-19\n[BBOX-90] 注：1.病理诊断分级注解：明确及基本明确的诊断，无任何修饰语；如有“考虑为”、“疑为”、“符合”、\n[BBOX-91] “不除外”及“可能性大”等修饰语，提示诊断具有不同程度的不确定性，请结合临床相关检查综合判断。\n[BBOX-92] 2.如本诊断与临床表现及相关检查不符，请临床医生及时与病理科联系后再行处置。\n[BBOX-93] 3.此报告以纸质版为准。\n[BBOX-94] 审核专用章\n[BBOX-95] （4）\n[BBOX-96] 青岛大学附属医院\n[BBOX-97] 市南院区\n[BBOX-98] 病理检查诊断报告\n[BBOX-99] 病理号.\n[BBOX-100] 姓  夕\n[BBOX-101] 性  别：男\n[BBOX-102] 年  龄：52\n[BBOX-103] 送检单位：青岛大学附属医院市 送检科室：消化内科\n[BBOX-104] 收到日期：\n[BBOX-105] 送检医生：李晓宇\n[BBOX-106] 病  区：\n[BBOX-107] 住院号：\n[BBOX-108] 送检材料：肠镜活检\n[BBOX-109] 临床诊断：直肠多发息肉完成ESD吻合口溃疡\n[BBOX-110] 大体检查:\n[BBOX-111] 直肠息肉ESD：粘膜组织一件，大小3.5*2.5*0.8cm，距一侧切缘0.1cm，距另一侧\n[BBOX-112] 切缘0.4cm，粘膜表面见一隆起，范围3*2.3cm，切面灰白质脆，基底涂墨。\n[BBOX-113] 直肠吻合口：粘膜组织三块，合计直径0.4cm。\n[BBOX-114] 病理诊断:\n[BBOX-115] 1.标本类型：直肠息肉ESD\n[BBOX-116] 标本数量：1件\n[BBOX-117] 病变数量：1灶\n[BBOX-118] 病变范围：3*2.3cm\n[BBOX-119] 组织学类型：绒毛状--管状腺瘤伴高级别上皮内瘤变，局灶区域恶变--中分化腺癌，\n[BBOX-120] 局限于粘膜层内\n[BBOX-121] 脉管癌栓：（-）\n[BBOX-122] 神经侵犯：（-）\n[BBOX-123] 水平切缘：（-）\n[BBOX-124] 垂直切缘：（-）\n[BBOX-125] 2.（直肠吻合口）腺癌（中分化）。\n[BBOX-126] 免疫组化结果示（直肠息肉ESD）：MLH1（+），MSH2（+），MSH6（+），PMS2\n[BBOX-127] (+），p53（+，约20%），CK-Desmin示粘膜肌连续，HER2（1+），S100示神经侵犯\n[BBOX-128] （-），CD31及D2-40示脉管癌栓（-），Ki-67（+，约60%）。\n[BBOX-129] 报告医生：李丹\n[BBOX-130] 初诊医生：赵玉洁\n[BBOX-131] 报告日期：2025-02-20\n[BBOX-132] 注：1.病理诊断分级注解：明确及基本明确的诊断\n[BBOX-133] 青岛市中心医疗集团\n[BBOX-134] 2.检测结果总览\n[BBOX-135] 本检测基于MGI（DNBSeq T7）测序平台对样本进行高通量测序。覆盖肿瘤相关的566个基因，检测内容包含目标基\n[BBOX-136] 因覆盖范围内的单核苷酸变异、小片段插入/缺失、拷贝数变异、重排（融合），以及微卫星不稳定性（MSI）分析、肿瘤\n[BBOX-137] 突变负荷（TMB）分析等。\n[BBOX-138] 检测类别\n[BBOX-139] 检测结果\n[BBOX-140] 基因变异1\n[BBOX-141] 体系\n[BBOX-142] I类（具有明确临床意义的变异）：KRAS p.G12D, KRAS p.A146V\n[BBOX-143] II类（具有潜在临床意义的变异）：TP53 p.G245D, FBXW7 p.R367*\n[BBOX-144] III类（临床意义不确定的变异）：RBM10 p.R97*, MUC16 p.A7208T, ALDH2 p\n[BBOX-145] .A5T, MTOR p.G1491S, CARD11 p.R207C等26个\n[BBOX-146] 胚系\n[BBOX-147] 致病性/疑似致病性变异：APC p.L180Yfs*5\n[BBOX-148] 靶向药物提示\n[BBOX-149] KRAS p.G12D提示：司美替尼(C级)、Avutometinib and defactinib (C级)可能敏感；西妥昔单抗(A级)、Panitumumab (A级)可能耐药。\n[BBOX-150] KRAS p.A146V提示：Avutometinib and defactinib (C级)可能敏感；西妥昔单抗(A级)、Pan\n[BBOX-151] itumumab (A级)可能耐药。\n[BBOX-152] TP53 p.G245D提示：AZD1775 (C级)可能敏感。\n[BBOX-153] FBXW7 p.R367*提示：恩替司他(D级)、Belinostat (D级)可能敏感。\n[BBOX-154] APC p.L180Yfs*5提示：达沙替尼(D级)、厄洛替尼(D级)可能敏感。\n[BBOX-155] 诊断/预后提示\n[BBOX-156] 目前暂未发现与本癌种诊断/预后相关的基因变异。\n[BBOX-157] 免疫治疗疗效提示\n[BBOX-158] TMB(同义突变&非同义突变)\n[BBOX-159] 13.89Muts/Mb\n[BBOX-160] TMB(非同义突变)\n[BBOX-161] 10.42Muts/Mb (前12.62%)\n[BBOX-162] MSI状态\n[BBOX-163] MSS (微卫星稳定)\n[BBOX-164] 其他潜在免疫疗效相关标志物2\n[BBOX-165] 正相关：未检出\n[BBOX-166] 负相关：未检出\n[BBOX-167] 超进展相关：未检出\n[BBOX-168] 化疗用药提示\n[BBOX-169] 可能药物敏感性较高：暂无，详见实验结果\n[BBOX-170] 可能毒副作用风险较低：卡培他滨，伊立替康\n[BBOX-171] 肿瘤遗传风险提示\n[BBOX-172] 检出APC p.L180Yfs*5疑似致病性变异，建议对受检者及血亲进行适当的遗传咨询或临床管理\n[BBOX-173] 注：1. 基因变异\n[BBOX-174] 58\n[BBOX-175] 青岛市中心医疗集团\n[BBOX-176] (1) 体系变异参考AMP/ASCO/CAP 共识《Standards and Guidelines for the Interpretation and Reporting of\n[BBOX-177] Sequence Variants in Cancer》，基因变异按照临床意义的重要性分为四个类别\n[BBOX-178] I类：具有明确临床意义的变异，包括NMPA、FDA批准疗法，或专业临床指南（如CSCO诊疗指南、NCCN临\n[BBOX-179] 床实践指南）推荐（A级证据），或基于证据充分的临床研究，并获得专家共识有明确治疗、诊断、预后的\n[BBOX-180] 变异（B级证据）；\n[BBOX-181] II类：具有潜在临床意义的变异，包括其他癌种的A级证据（跨适应症用药），或多项小型临床研究支持，或\n[BBOX-182] 已作为当前临床研究的入组标准（C级证据），或临床前研究或案例报道，未获得专家共识的药物（D级证\n[BBOX-183] 据）；\n[BBOX-184] III类：临床意义不确定的变异（尚无相关临床证据）\n[BBOX-185] “类：下事或示能于事的变异（在全人群或特定人群数据库中观察到高变异率）\n[BBOX-186] 扫描全能王 创建\n[BBOX-187] 青岛市中心医疗集团\n[BBOX-188] 3.基因变异临床意义综合提示\n[BBOX-189] 3.1诊断/预后及靶向药物提示\n[BBOX-190] 基因变异1\n[BBOX-191] 突变丰度2/拷贝数\n[BBOX-192] 变异分类\n[BBOX-193] 可能敏感药物\n[BBOX-194] 可能耐药药物\n[BBOX-195] 突变说明\n[BBOX-196] KRAS\n[BBOX-197] NM_004985.5\n[BBOX-198] 12.81%\n[BBOX-199] I类\n[BBOX-200] 司美替尼(C级)\n[BBOX-201] 西妥昔单抗(A\n[BBOX-202] 级)\n[BBOX-203] KRAS基因的G12D突变，发生在第\n[BBOX-204] 2号外显子，位于GTP结合蛋白结\n[BBOX-205] 构域(UniProt.org)，突变导致\n[BBOX-206] 第12位氨基酸由甘氨酸变为天冬氨\n[BBOX-207] 酸，G12突变将降低自身的GTP酶\n[BBOX-208] 活性，使KRAS长期处于与GTP结\n[BBOX-209] 合的激活状态，导致细胞增殖异常\n[BBOX-210] (PMID:12509763,20736745,2\n[BBOX-211] 6037647,6092966)，为功能获\n[BBOX-212] 得突变。\n[BBOX-213] exon2\n[BBOX-214] p.G12D\n[BBOX-215] c.35G>A\n[BBOX-216] Avutometinib a\n[BBOX-217] nd defactinib(C\n[BBOX-218] 级)\n[BBOX-219] Pantitumuma\n[BBOX-220] b(A级)\n[BBOX-221] KRAS\n[BBOX-222] NM_004985.5\n[BBOX-223] 1.46%\n[BBOX-224] I类\n[BBOX-225] Avutometinib a\n[BBOX-226] nd defactinib(C\n[BBOX-227] 级)\n[BBOX-228] 西妥昔单抗(A\n[BBOX-229] 级)\n[BBOX-230] KRAS基因的A146V突变，发生在\n[BBOX-231] 第4号外显子，突变导致146位氨基\n[BBOX-232] 酸由丙氨酸变为缬氨酸，为功能获\n[BBOX-233] 得突变。在两个不同的细胞系中，\n[BBOX-234] 与野生型Kras相比，A146V可能会\n[BBOX-235] 降低Kras的GTPase活性，从而导\n[BBOX-236] 致下游通路激活增加(PMID:205\n[BBOX-237] 70890)，与野生型Kras相比，A1\n[BBOX-238] 46V突变会增加细胞增殖和细胞活\n[BBOX-239] 力(PMID:29533785)，为功能\n[BBOX-240] 获得突变。\n[BBOX-241] exon4\n[BBOX-242] p.A146V\n[BBOX-243] c.437C>T\n[BBOX-244] Panitumuma\n[BBOX-245] b(A级)\n[BBOX-246] TP53\n[BBOX-247] NM_000546.6\n[BBOX-248] 12.73%\n[BBOX-249] II类\n[BBOX-250] AZD1775(C级)\n[BBOX-251] TP53基因的G245D突变，发生在\n[BBOX-252] 第7号外显子，位于Tp53蛋白的D\n[BBOX-253] NA结合域(PMID:22713868)\n[BBOX-254] ，突变导致245位甘氨酸变为天冬\n[BBOX-255] 氨酸。G245D导致Tp53靶基因的\n[BBOX-256] 激活减少(PMID:22214764,256\n[BBOX-257] 34208,27533082)，为功能丧失\n[BBOX-258] 突变。\n[BBOX-259] exon7\n[BBOX-260] p.G245D\n[BBOX-261] c.734G>A\n[BBOX-262] FBXW7\n[BBOX-263] NM_033632.3\n[BBOX-264] 2.75%\n[BBOX-265] II类\n[BBOX-266] 恩替司他(D级)\n[BBOX-267] FBXW7基因的R367*突变，发生在\n[BBOX-268] 第7号外显子，突变导致终止密码\n[BBOX-269] 子提前编码(UniProt.org)。由于W\n[BBOX-270] D重复域的丢失，预测R367*会导\n[BBOX-271] 致Fbxw7蛋白功能的丢失(UniProt\n[BBOX-272] .org)。\n[BBOX-273] exon7\n[BBOX-274] p.R367*\n[BBOX-275] c.1099C>T\n[BBOX-276] Belinostat(D级)\n[BBOX-277] APC\n[BBOX-278] NM_000038.6\n[BBOX-279] 杂合\n[BBOX-280] II类\n[BBOX-281] 达沙替尼(D级)\n[BBOX-282] APC基因的p.L180Yfs*5、c.539de\n[BBOX-283] l突变，发生在第6外显子，不在已\n[BBOX-284] 知功能域内(UniProt.org)，突\n[BBOX-285] 变导致其编码的氨基酸在180位开\n[BBOX-286] 始框移，可能影响蛋白功能(Uni\n[BBOX-287] Prot.org)。已知APC的功能丧失\n[BBOX-288] 变异具有致病性(PMID:17963004\n[BBOX-289] ,20685668)。Clinvar数据库记录\n[BBOX-290] 该变异为Pathogenic。其在人群\n[BBOX-291] 基因组数据库未收录。综上分析，\n[BBOX-292] 该突变是一个疑似致病性变异。\n[BBOX-293] exon6\n[BBOX-294] p.L180Yfs*5\n[BBOX-295] c.539del\n[BBOX-296] 厄洛替尼(D级)\n[BBOX-297] 注:1.基因变异：“exon”为外显子，“intron”为内含子，“c”为DNA序列，“p”为蛋白质，“NM”为基因的转录\n[BBOX-298] 本编号;\n[BBOX-299] 2.突变丰度:在某位点产生突变的等位基因在该位点全部等位基因中所占比率。例如,突变丰度10%意为该位点含\n[BBOX-300] 有10%的突变等位基因和90%的野生型等位基因。拷贝数:是指某一种基因或某一段特定的DNA序列在单倍体基\n[BBOX-301] 因组中出现的数目。\n[BBOX-302] 4/58\n[BBOX-303] 青岛市中心医疗集团\n[BBOX-304] 扫描全能王 创建\n[BBOX-305] 19:08\n[BBOX-306] 41\n[BBOX-307] ×\n[BBOX-308] 报告单详情\n[BBOX-309] www.jkqd.org.cn\n[BBOX-310] 20260307检\n[BBOX-311] 查\n[BBOX-312] 1.双肺多发结节，较前2025-12-26部分缩\n[BBOX-313] 小，考虑转移；/>右肺门区及纵隔内多发肿\n[BBOX-314] 大淋巴结，考虑转移2.直肠术后，吻合区软\n[BBOX-315] 组织影，考虑肿瘤复发，与前列腺分界不\n[BBOX-316] 清，大致同前（2025-10-16）；/>直肠周\n[BBOX-317] 围、右腹膜后、骶前区多发淋巴结转移，部\n[BBOX-318] 分较前略缩小，建议复查3.肝内多发转移\n[BBOX-319] 瘤，较前（2025-10-16）进展4.肝囊肿5.\n[BBOX-320] 膀胱内气体，建议结合临床\n[BBOX-321] 诊断意见\n[BBOX-322] 骨性胸廓对称，纵隔气管居中。双肺支气管\n[BBOX-323] 血管束增多。双肺见弥漫多发类圆形实性结\n[BBOX-324] 节影，大者位于右肺下叶内基底段（薄层\n[BBOX-325] IM181），大小约为16×16mm，边界清，轻\n[BBOX-326] 度均匀强化。气管及中心支气管通畅。右肺\n[BBOX-327] 门区及纵隔内多发肿大淋巴结，最大者短径\n[BBOX-328] 约14mm，轻度强化。心脏不大。双侧胸膜\n[BBOX-329] 未见明显增厚。双侧胸腔内未见明显液体密\n[BBOX-330] 度影。肝脏增大，肝内见多发类圆形稍低密\n[BBOX-331] 度影，边界不清，大者长径约110mm，增强\n[BBOX-332] 扫描边缘轻度强化。肝右叶可见直径3mm的\n[BBOX-333] 无强化的囊性密度灶，边界清；/>肝内外胆\n[BBOX-334] 管未见明显扩张。胆囊内未见异常密度影。\n[BBOX-335] 胰腺、脾脏未见明显异常密度灶及异常强化\n[BBOX-336] 灶。双肾上腺及双肾大小、形态、密度未见\n[BBOX-337] 明显异常密度灶及异常强化灶。肠管未见梗\n[BBOX-338] 阻征象。直肠术后直肠吻合口区见团片样\n[BBOX-339] >\n[BBOX-340] 扫描全能王 创建\n[BBOX-341] 19:08\n[BBOX-342] 41\n[BBOX-343] ×\n[BBOX-344] 报告单详情\n[BBOX-345] www.jkqd.org.cn\n[BBOX-346] 瘤，较前（2025-10-16）进展 4. 肝囊肿 5.\n[BBOX-347] 膀胱内气体，建议结合临床\n[BBOX-348] 诊断意见\n[BBOX-349] 骨性胸廓对称，纵隔气管居中。双肺支气管\n[BBOX-350] 血管束增多。双肺见弥漫多发类圆形实性结\n[BBOX-351] 节影，大者位于右肺下叶内基底段（薄层\n[BBOX-352] IM181），大小约为16×16mm，边界清，轻\n[BBOX-353] 度均匀强化。气管及中心支气管通畅。右肺\n[BBOX-354] 门区及纵隔内多发肿大淋巴结，最大者短径\n[BBOX-355] 约14mm，轻度强化。心脏不大。双侧胸膜\n[BBOX-356] 未见明显增厚。双侧胸腔内未见明显液体密\n[BBOX-357] 度影。肝脏增大，肝内见多发类圆形稍低密\n[BBOX-358] 度影，边界不清，大者长径约110mm，增强\n[BBOX-359] 扫描边缘轻度强化。肝右叶可见直径3mm的\n[BBOX-360] 无强化的囊性密度灶，边界清； />肝内外胆\n[BBOX-361] 管未见明显扩张。胆囊内未见异常密度影。\n[BBOX-362] 胰腺、脾脏未见明显异常密度灶及异常强化\n[BBOX-363] 灶。双肾上腺及双肾大小、形态、密度未见\n[BBOX-364] 明显异常密度灶及异常强化灶。肠管未见梗\n[BBOX-365] 阻征象。直肠术后，直肠吻合口区见团片样\n[BBOX-366] 软组织密度影，与前列腺分界不清，增强扫\n[BBOX-367] 描不均匀强化。直肠周围、右腹膜后、骶前\n[BBOX-368] 区见多发肿大淋巴结，大者短径约11mm，\n[BBOX-369] 增强扫描不均匀强化。膀胱充盈良好，膀胱\n[BBOX-370] 壁光整，膀胱内见气体影。盆腔未见明显积\n[BBOX-371] 液。\n[BBOX-372] \\begin{tabular}{llllllll}\n[BBOX-373] 报告时间: 2026-03-07\n[BBOX-374] \\hline\n[BBOX-375] 中文名称 & 英文缩写 & 结果 & 单位 & 提示 & 参考区间 & 检测方法 \\\\\n[BBOX-376] \\hline\n[BBOX-377] 1. 丙氨酸氨基转移酶**☆ & ALT & 12 & U/L & & 9-50 & 速率法 \\\\\n[BBOX-378] 2. 天门冬氨酸氨基转移酶**☆AST & & 30 & U/L & & 15-40 & 速率法 \\\\\n[BBOX-379] 3. AST/ALT & AST/ALT & 2.50 & & & 0.10-3.00 & 计算法 \\\\\n[BBOX-380] 4. 总胆红素**☆ & TBIL & 6.3 & umol/L & & ≤23.0 & 钒酸盐法 \\\\\n[BBOX-381] 5. 直接胆红素**☆ & DBIL & 2.1 & umol/L & & 0-6.8 & 钒酸盐法 \\\\\n[BBOX-382] 6. 间接胆红素 & IBIL & 4.2 & umol/L & & 3.4-17.1 & 计算法 \\\\\n[BBOX-383] 7. 总蛋白**☆ & TP & 66.9 & g/L & & 65.0-85.0 & 双缩脲法 \\\\\n[BBOX-384] 8. 白蛋白**☆ & ALB & 31.8 & g/L & ↓ & 40.0-55.0 & 溴甲酚绿法 \\\\\n[BBOX-385] 9. 球蛋白 & GLB & 35.1 & g/L & & 20.0-40.0 & 计算法 \\\\\n[BBOX-386] 10. 白球比 & A/G & 0.91 & & ↓ & 1.20-2.40 & 计算法 \\\\\n[BBOX-387] 11. 碱性磷酸酶**☆ & ALP & 240 & U/L & ↑ & 45-125 & 速率法 \\\\\n[BBOX-388] 12. 谷氨酸脱氢酶 & GLDH & 11 & U/L & ↑ & 0-7 & 速率法 \\\\\n[BBOX-389] 13. γ-谷氨酰转肽酶**☆ & GGT & 151 & U/L & ↑ & 10-60 & 速率法 \\\\\n[BBOX-390] 14. 胆碱酯酶**☆ & CHE & 4919 & U/L & ↓ & 5000-12000 & 速率法 \\\\\n[BBOX-391] 15. 甘胆酸 & CG & 1.61 & ug/ml & & 0.00-2.70 & 均相酶免法 \\\\\n[BBOX-392] 16. 总胆汁酸* & TBA & 4.20 & umol/L & & 0.00-10.00 & 酶循环法 \\\\\n[BBOX-393] 17. 前白蛋白*☆ & PA & 135 & mg/L & ↓ & 200-430 & 免疫比浊法 \\\\\n[BBOX-394] 18. 尿素**☆ & UREA & 4.7 & mmol/L & & 3.1-8.0 & 酶法 \\\\\n[BBOX-395] 19. 肌酐**☆ & CREA & 50.0 & umol/L & ↓ & 57-97 & 酶法 \\\\\n[BBOX-396] 20. 尿素/肌酐 & UREA/CREA & 0.09 & & & 0.01-0.70 & 计算法 \\\\\n[BBOX-397] 21. 估算肾小球滤过率 & eGFR & 119 & mL/min/1.73m2 & & & 计算法 \\\\\n[BBOX-398] 22. 尿酸**☆ & UA & 326 & umol/L & & 208-428 & 酶法 \\\\\n[BBOX-399] 23. 钾**☆ & K & 4.0 & mmol/L & & 3.5-5.3 & 电极法 \\\\\n[BBOX-400] 24. 钠**☆ & Na & 139 & mmol/L & & 137-147 & 电极法 \\\\\n[BBOX-401] 25. 氯**☆ & CL & 104 & mmol/L & & 99-110 & 电极法 \\\\\n[BBOX-402] 26. 总二氧化碳 & CO2 & 22 & mmol/L & & 22-29 & 酶法 \\\\\n[BBOX-403] 27. 阴离子间隙 & AG & 13 & mmol/L & & 8-16 & 计算法 \\\\\n[BBOX-404] \\hline\n[BBOX-405] \\end{tabular}\n[BBOX-406] \\begin{tabular}{llllllll}\n[BBOX-407] 报告时间: 2026-03-07\n[BBOX-408] \\hline\n[BBOX-409] 中文名称 & 英文缩写 & 结果 & 单位 & 提示 & 参考区间 & 检测方法 \\\\\n[BBOX-410] \\hline\n[BBOX-411] 28. 唾液酸 & SA & 969 & mg/L & ↑ & 456-754 & 酶法 \\\\\n[BBOX-412] 29. 补体Clq & Clq & 16.5 & mg/dl & & 15.7-23.7 & 免疫比浊法 \\\\\n[BBOX-413] \\hline\n[BBOX-414] \\end{tabular}\n[BBOX-415] \\begin{tabular}{llllllll}\n[BBOX-416] 报告时间: 2026-03-07\n[BBOX-417] \\hline\n[BBOX-418] 中文名称 & 英文缩写 & 结果 & 单位 & 提示参考区间 & 检测方法 \\\\\n[BBOX-419] \\hline\n[BBOX-420] 1. 凝血酶原时间$\\ast\\ast\\star$ & PT & 14.4 & 秒 & 10.70--14.80 & 凝固法 \\\\\n[BBOX-421] 2. 凝血酶原时间活动度 & PT\\% & 85.00 & \\% & 70.00--150.00 & 换算值 \\\\\n[BBOX-422] 3. 凝血酶原时间比值 & PT. R & 1.08 & & 0.82--1.15 & 换算值 \\\\\n[BBOX-423] 4. & PT. INR & 1.10 & & 1.0--2.0 & \\\\\n[BBOX-424] \\multicolumn{2}{l}{国际标准化比值$\\ast\\ast\\star$} & & & \\multicolumn{2}{l}{口服抗凝剂：换算值} \\\\\n[BBOX-425] \\multicolumn{2}{l}{} & & & \\multicolumn{2}{l}{1.8--2.5} \\\\\n[BBOX-426] 5. 活化部分凝血活酶时间$\\ast\\ast\\star$ & APTT & 43.2 & 秒 & $\\uparrow$ 28.00--43.00 & 凝固法 \\\\\n[BBOX-427] 6. 活化部分凝血活酶时间比值 & APTT R & 1.27 & & $\\uparrow$ 0.82--1.26 & 换算值 \\\\\n[BBOX-428] 7. 纤维蛋白原$\\ast\\ast$ & Fib & 6.490 & g/L & $\\uparrow$ 2.000--4.000 & Clauss法 \\\\\n[BBOX-429] 8. 凝血酶时间$\\ast\\ast$ & TT & 17.10 & 秒 & 14.00--21.00 & 凝固法 \\\\\n[BBOX-430] 9. D-二聚体$\\ast$ & D-Dimer & 3.20 & mg/L(FEU) & $\\uparrow$ 0.00--0.50 & 免疫比浊法 \\\\\n[BBOX-431] 10抗凝血酶活性$\\ast$ & AT:A & 92.00 & \\% & 80.00--130.00 & 发色底物法 \\\\\n[BBOX-432] 11纤维蛋白(原)降解产物$\\ast$ & FDP & 14.63 & mg/L & $\\uparrow$ 0.00--5.00 & 免疫比浊法 \\\\\n[BBOX-433] \\hline\n[BBOX-434] \\end{tabular}\n[BBOX-435] \\begin{tabular}{llllllll}\n[BBOX-436] 报告时间: 2026-03-07\n[BBOX-437] \\hline\n[BBOX-438] 中文名称 & 英文缩写 & 结果 & 提示 & 参考区间 & 单位 & 检测方法 \\\\\n[BBOX-439] \\hline\n[BBOX-440] 1. 白细胞计数$\\text{##}\\star$ & WBC & 3.96 & & 3.50--9.50 & $*10^9/\\text{L}$ & 仪器法 \\\\\n[BBOX-441] 2. 中性粒细胞计数 & NEUT\\# & 2.89 & & 1.80--6.30 & $*10^9/\\text{L}$ & 仪器法 \\\\\n[BBOX-442] 3. 淋巴细胞计数 & LYMPH\\# & 0.65 & $\\downarrow$ & 1.10--3.20 & $*10^9/\\text{L}$ & 仪器法 \\\\\n[BBOX-443] 4. 单核细胞计数 & MONO\\# & 0.30 & & 0.10--0.60 & $*10^9/\\text{L}$ & 仪器法 \\\\\n[BBOX-444] 5. 嗜酸细胞计数 & EO\\# & 0.10 & & 0.02--0.52 & $*10^9/\\text{L}$ & 仪器法 \\\\\n[BBOX-445] 6. 嗜碱细胞计数 & BASO\\# & 0.02 & & 0.00--0.06 & $*10^9/\\text{L}$ & 仪器法 \\\\\n[BBOX-446] 7. 中性粒细胞百分比 & NEUT\\% & 73.0 & & 40.0--75.0 & \\% & 仪器法 \\\\\n[BBOX-447] 8. 淋巴细胞百分比 & LYMPH\\% & 16.4 & $\\downarrow$ & 20.0--50.0 & \\% & 仪器法 \\\\\n[BBOX-448] 9. 单核细胞百分比 & MONO\\% & 7.6 & & 3.0--10.0 & \\% & 仪器法 \\\\\n[BBOX-449] 10. 嗜酸细胞百分比 & E0\\% & 2.6 & & 0.40--8.00 & \\% & 仪器法 \\\\\n[BBOX-450] 11. 嗜碱细胞百分比 & BASO\\% & 0.4 & & 0.00--1.00 & \\% & 仪器法 \\\\\n[BBOX-451] 12. 红细胞计数$\\text{##}\\star$ & RBC & 3.57 & $\\downarrow$ & 4.30--5.80 & $*10^12/\\text{L}$ & 仪器法 \\\\\n[BBOX-452] 13. 血红蛋白含量$\\text{##}\\star$ & HGB & 88 & $\\downarrow$ & 130--175 & g/L & 仪器法 \\\\\n[BBOX-453] 14. 红细胞比容$\\text{##}\\star$ & HCT & 0.28 & $\\downarrow$ & 0.40--0.50 & L/L & 仪器法 \\\\\n[BBOX-454] 15. 平均红细胞血红蛋白含量$\\text{##}\\star$ & MCH & 24.6 & $\\downarrow$ & 27.0--34.0 & pg & 仪器法 \\\\\n[BBOX-455] 16. 平均红细胞血红蛋白浓度$\\text{##}\\star$ & MCHC & 319 & & 316--354 & g/L & 仪器法 \\\\\n[BBOX-456] 17. 平均红细胞体积$\\text{##}\\star$ & MCV & 77.2 & $\\downarrow$ & 82.0--100.0 & fL & 仪器法 \\\\\n[BBOX-457] 18. 红细胞分布宽度（CV） & RDW--CV & 17.4 & $\\uparrow$ & 11.6--16.5 & \\% & 仪器法 \\\\\n[BBOX-458] 19. 红细胞分布宽度（SD） & RDW--SD & 50.1 & & 37.0--54.0 & fL & 仪器法 \\\\\n[BBOX-459] 20. 血小板计数$\\text{##}\\star$ & PLT & 268 & & 125--350 & $*10^9/\\text{L}$ & 仪器法 \\\\\n[BBOX-460] 21. 平均血小板体积 & MPV & 8.2 & & 7.4--11.0 & fL & 仪器法 \\\\\n[BBOX-461] 22. 大血小板比率 & P--LCR & 14.8 & & 13.0--43.0 & \\% & 仪器法 \\\\\n[BBOX-462] 23. 血小板比容 & PCT & 0.22 & & 0.170--0.350 & \\% & 仪器法 \\\\\n[BBOX-463] 24. 血小板分布宽度 & PDW & 15.4 & $\\downarrow$ & 15.5--16.8 & fL & 仪器法 \\\\\n[BBOX-464] 25. C--反应蛋白$\\text{*}$ & CRP & 30.830 & $\\uparrow$ & 0.000--5.000 & mg/L & 散射比浊法 \\\\\n[BBOX-465] \\hline\n[BBOX-466] \\end{tabular}\n[BBOX-467] \\begin{tabular}{llllllll}\n[BBOX-468] 报告时间: 2026-03-07\n[BBOX-469] \\hline\n[BBOX-470] 中文名称 & 英文缩写 & 结果 & 单位 & 提示参考区间 & 检测方法 \\\\\n[BBOX-471] \\hline\n[BBOX-472] 1. 粪便颜色 & Colour & 黄色 & & 棕黄 & 手工法 \\\\\n[BBOX-473] 2. 粪便性状 & Stool-type & 软 & & 软 & 手工法 \\\\\n[BBOX-474] 3. 白细胞 & WBC & 未见 & /HPF & 0-3/阴性 & 手工法 \\\\\n[BBOX-475] 4. 红细胞 & RBC & 未见 & /HPF & 阴性 & 手工法 \\\\\n[BBOX-476] 5. 脂肪滴 & Fat droplet & 未见 & /HPF & 阴性 & 手工法 \\\\\n[BBOX-477] 6. 真菌 & Fungus & 未见 & /HPF & 阴性 & 手工法 \\\\\n[BBOX-478] 7. 寄生虫卵 & Parasitic ovum & 未见 & & 阴性 & 手工法 \\\\\n[BBOX-479] 8. 隐血试验 & OBT & 阳性反应 (+) & & A 阴性反应 (-) & 胶体金法 \\\\\n[BBOX-480] \\hline\n[BBOX-481] \\end{tabular}\n[BBOX-482] \\begin{tabular}{l l l l l l l}\n[BBOX-483] 报告时间: 2026-03-07\n[BBOX-484] \\hline\n[BBOX-485] 中文名称 & 英文缩写 & 结果 & 单位 & 提示参考区间 & 检测方法 \\\\\n[BBOX-486] \\hline\n[BBOX-487] 1. 红细胞计数 & RBC & 43.00 & 个/ul & $\\uparrow$ 0.00--17.00 & \\\\\n[BBOX-488] 2. 白细胞计数 & WBC & 3117.00 & 个/ul & $\\uparrow$ 0.00--28.00 & \\\\\n[BBOX-489] 3. 白细胞团 & WBCC & 180.00 & 个/ul & $\\uparrow$ 0.00--2.00 & 仪器法 \\\\\n[BBOX-490] 4. 鳞状上皮细胞 & SQEP & 15.00 & 个/ul & 0.00--28.00 & 仪器法 \\\\\n[BBOX-491] 5. 非鳞状上皮细胞 & NSE & 0.00 & 个/ul & 0.00--6.00 & 仪器法 \\\\\n[BBOX-492] 6. 透明管型 & HYAL & 0.00 & 个/ul & 0.00--1.00 & 仪器法 \\\\\n[BBOX-493] 7. 病理管型 & UNCC & 1.00 & 个/ul & 0.00--1.00 & 仪器法 \\\\\n[BBOX-494] 8. 酵母 & BYST & 0.00 & 个/ul & 0.00--1.00 & 仪器法 \\\\\n[BBOX-495] 9. 未分类结晶 & UNCX & 49.00 & 个/ul & $\\uparrow$ 0.00--28.00 & 仪器法 \\\\\n[BBOX-496] 10粘液丝 & MUCS & 12.00 & 个/ul & 0.00--46.00 & \\\\\n[BBOX-497] 11细菌 & BACT & 11801.00 & 个/ul & $\\uparrow$ 0.00--340.00 & \\\\\n[BBOX-498] 12潜血**☆ & BLD & 痕量(++) & & 阴性(-) & 干化学法 \\\\\n[BBOX-499] 13白细胞酯酶* & LEU & 阳性(2+) & & 阴性(-) & 干化学法 \\\\\n[BBOX-500] 14亚硝酸盐**☆ & NIT & 阳性(2+) & & 阴性(-) & 干化学法 \\\\\n[BBOX-501] 15尿胆素原**☆ & UBG & Normal & & Normal & 干化学法 \\\\\n[BBOX-502] 16胆红素**☆ & BIL & 阴性(-) & & 阴性(-) & 干化学法 \\\\\n[BBOX-503] 17维生素C & VC & 阳性(+) & & 阴性(-) & 干化学法 \\\\\n[BBOX-504] 18蛋白质**☆ & PRO & 痕量(++) & & 阴性(-) & 干化学法 \\\\\n[BBOX-505] 19酸碱度**☆ & PH & 5.5 & & 5.0--8.0 & 干化学法 \\\\\n[BBOX-506] 20比密**☆ & SG & 1.025 & & 1.005--1.030 & 干化学法 \\\\\n[BBOX-507] 21葡萄糖**☆ & GLU & 阴性(-) & & 阴性(-) & 干化学法 \\\\\n[BBOX-508] 22酮体**☆ & KET & 阴性(-) & & 阴性(-) & 干化学法 \\\\\n[BBOX-509] 23颜色 & Colour & 黄色 & & & 手工法 \\\\\n[BBOX-510] 24透明度 & Clarity & 浑浊 & & & 手工法 \\\\\n[BBOX-511] \\hline\n[BBOX-512] \\end{tabular}\n[BBOX-513] \\begin{tabular}{llllllll}\n[BBOX-514] 报告时间: 2026-03-07\n[BBOX-515] \\hline\n[BBOX-516] 中文名称 & 英文缩写 & 结果 & 单位 & 提示参考区间 & 检测方法 \\\\\n[BBOX-517] \\hline\n[BBOX-518] 1. 乙型肝炎病毒表面抗原$\\ast\\ast\\star$ & HBsAg & $<0.05$ 阴性反应(-) & IU/ml & $<0.08$ & \\\\\n[BBOX-519] 2. 丙型肝炎病毒抗体$\\ast\\ast\\star$ & HCV & 0.060 阴性反应(-) & & $<1$ & 化学发光法 \\\\\n[BBOX-520] 3. 梅毒螺旋体抗体$\\ast\\ast\\star$ & antiTP & 0.0 阴性反应(-) & & 0.000-1.000 & 化学发光法 \\\\\n[BBOX-521] 4. 人免疫缺陷病毒抗体$\\ast\\ast\\star$ & HIV Ab & 0.0 阴性反应(-) & & 0.000-1.000 & 化学发光法 \\\\\n[BBOX-522] \\hline\n[BBOX-523] \\end{tabular}"
  }
]
2026-08-10 18:11:25,940 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:11:25.938+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 85, "failed": 0, "current": {"a677452e94e611f1bd9827cf206dfa2d": {"id": "a677452e94e611f1bd9827cf206dfa2d", "doc_id": "a646f41e94e611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 11495294, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385378144, "task_type": "dataflow", "root_trace_id": "971de7c4c0604c27afceabc8ac295233", "root_traceparent": "00-971de7c4c0604c27afceabc8ac295233-de3f877b239fe0d8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:11:40,361 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:11:40,376 INFO     29 [SmartSplitter] SmartSplitter done: 12 chunks from 12 LLM segments (all bbox_id). Types: {'OutpatientRecord': 1, 'ExaminationReport': 4, 'LabReport': 7}
2026-08-10 18:11:40,384 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 18:11:40,384 INFO     29 [Trace] task=a677452e | doc=07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "524 items", "markdown": "", "text": "", "name": "07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks": "12 items, types={'OutpatientRecord': 1, 'ExaminationReport': 4, 'LabReport': 7}"}
2026-08-10 18:11:40,384 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 18:11:40,385 INFO     29 [ChunkRouter] Routed 12 chunks into 3 groups: {'chunks_Clinical': 1, 'chunks_Examination': 4, 'chunks_LabExam': 7}
2026-08-10 18:11:40,393 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 18:11:40,393 INFO     29 [Trace] task=a677452e | doc=07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf | ChunkRouter:Router | outputs={"html": "", "json": "524 items", "markdown": "", "text": "", "name": "07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks": "12 items, types={'OutpatientRecord': 1, 'ExaminationReport': 4, 'LabReport': 7}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "7 items, types={'LabReport': 7}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 4, \"chunks_LabExam\": 7}"}
2026-08-10 18:11:40,393 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 18:11:40,397 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:11:40,398 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:11:40,399 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[8]
2026-08-10 18:11:40,399 INFO     29 [qwen-vl-table] positions ： [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:11:40,564 INFO     29 [qwen-vl-table] page=8, rect=595x842, img=(1653x2339)
2026-08-10 18:11:40,564 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:11:40,564 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 372, \"bbox_end\": 405, \"encounter_dates\": [\"2026-03-07\"], \"department\": \"检验科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllll}\n报告时间: 2026-03-07\n\\hline\n中文名称 & 英文缩写 & 结果 & 单位 & 提示 & 参考区间 & 检测方法 \\\\\n\\hline\n1. 丙氨酸氨基转移酶**☆ & ALT & 12 & U/L & & 9-50 & 速率法 \\\\\n2. 天门冬氨酸氨基转移酶**☆AST & & 30 & U/L & & 15-40 & 速率法 \\\\\n3. AST/ALT & AST/ALT & 2.50 & & & 0.10-3.00 & 计算法 \\\\\n4. 总胆红素**☆ & TBIL & 6.3 & umol/L & & ≤23.0 & 钒酸盐法 \\\\\n5. 直接胆红素**☆ & DBIL & 2.1 & umol/L & & 0-6.8 & 钒酸盐法 \\\\\n6. 间接胆红素 & IBIL & 4.2 & umol/L & & 3.4-17.1 & 计算法 \\\\\n7. 总蛋白**☆ & TP & 66.9 & g/L & & 65.0-85.0 & 双缩脲法 \\\\\n8. 白蛋白**☆ & ALB & 31.8 & g/L & ↓ & 40.0-55.0 & 溴甲酚绿法 \\\\\n9. 球蛋白 & GLB & 35.1 & g/L & & 20.0-40.0 & 计算法 \\\\\n10. 白球比 & A/G & 0.91 & & ↓ & 1.20-2.40 & 计算法 \\\\\n11. 碱性磷酸酶**☆ & ALP & 240 & U/L & ↑ & 45-125 & 速率法 \\\\\n12. 谷氨酸脱氢酶 & GLDH & 11 & U/L & ↑ & 0-7 & 速率法 \\\\\n13. γ-谷氨酰转肽酶**☆ & GGT & 151 & U/L & ↑ & 10-60 & 速率法 \\\\\n14. 胆碱酯酶**☆ & CHE & 4919 & U/L & ↓ & 5000-12000 & 速率法 \\\\\n15. 甘胆酸 & CG & 1.61 & ug/ml & & 0.00-2.70 & 均相酶免法 \\\\\n16. 总胆汁酸* & TBA & 4.20 & umol/L & & 0.00-10.00 & 酶循环法 \\\\\n17. 前白蛋白*☆ & PA & 135 & mg/L & ↓ & 200-430 & 免疫比浊法 \\\\\n18. 尿素**☆ & UREA & 4.7 & mmol/L & & 3.1-8.0 & 酶法 \\\\\n19. 肌酐**☆ & CREA & 50.0 & umol/L & ↓ & 57-97 & 酶法 \\\\\n20. 尿素/肌酐 & UREA/CREA & 0.09 & & & 0.01-0.70 & 计算法 \\\\\n21. 估算肾小球滤过率 & eGFR & 119 & mL/min/1.73m2 & & & 计算法 \\\\\n22. 尿酸**☆ & UA & 326 & umol/L & & 208-428 & 酶法 \\\\\n23. 钾**☆ & K & 4.0 & mmol/L & & 3.5-5.3 & 电极法 \\\\\n24. 钠**☆ & Na & 139 & mmol/L & & 137-147 & 电极法 \\\\\n25. 氯**☆ & CL & 104 & mmol/L & & 99-110 & 电极法 \\\\\n26. 总二氧化碳 & CO2 & 22 & mmol/L & & 22-29 & 酶法 \\\\\n27. 阴离子间隙 & AG & 13 & mmol/L & & 8-16 & 计算法 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 18:11:56,913 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:11:56,913 INFO     29 [qwen-vl-table] page=8 LLM output (len=4530):
{
  "report_date": "2026-03-07",
  "items": [
    {
      "name": "丙氨酸氨基转移酶",
      "item_code": "ALT",
      "value": "12",
      "unit": "U/L",
      "reference_range": "9-50",
      "abnormal": false
    },
    {
      "name": "天门冬氨酸氨基转移酶",
      "item_code": "AST",
      "value": "30",
      "unit": "U/L",
      "reference_range": "15-40",
      "abnormal": false
    },
    {
      "name": "AST/ALT",
      "item_code": "AST/ALT",
      "value": "2.50",
      "unit": null,
      "reference_range": "0.10-3.00",
      "abnormal": false
    },
    {
      "name": "总胆红素",
      "item_code": "TBIL",
      "value": "6.3",
      "unit": "umol/L",
      "reference_range": "≤23.0",
      "abnormal": false
    },
    {
      "name": "直接胆红素",
      "item_code": "DBIL",
      "value": "2.1",
      "unit": "umol/L",
      "reference_range": "0-6.8",
      "abnormal": false
    },
    {
      "name": "间接胆红素",
      "item_code": "IBIL",
      "value": "4.2",
      "unit": "umol/L",
      "reference_range": "3.4-17.1",
      "abnormal": false
    },
    {
      "name": "总蛋白",
      "item_code": "TP",
      "value": "66.9",
      "unit": "g/L",
      "reference_range": "65.0-85.0",
      "abnormal": false
    },
    {
      "name": "白蛋白",
      "item_code": "ALB",
      "value": "31.8",
      "unit": "g/L",
      "reference_range": "40.0-55.0",
      "abnormal": true
    },
    {
      "name": "球蛋白",
      "item_code": "GLB",
      "value": "35.1",
      "unit": "g/L",
      "reference_range": "20.0-40.0",
      "abnormal": false
    },
    {
      "name": "白球比",
      "item_code": "A/G",
      "value": "0.91",
      "unit": null,
      "reference_range": "1.20-2.40",
      "abnormal": true
    },
    {
      "name": "碱性磷酸酶",
      "item_code": "ALP",
      "value": "240",
      "unit": "U/L",
      "reference_range": "45-125",
      "abnormal": true
    },
    {
      "name": "谷氨酸脱氢酶",
      "item_code": "GLDH",
      "value": "11",
      "unit": "U/L",
      "reference_range": "0-7",
      "abnormal": true
    },
    {
      "name": "γ-谷氨酰转肽酶",
      "item_code": "GGT",
      "value": "151",
      "unit": "U/L",
      "reference_range": "10-60",
      "abnormal": true
    },
    {
      "name": "胆碱酯酶",
      "item_code": "CHE",
      "value": "4919",
      "unit": "U/L",
      "reference_range": "5000-12000",
      "abnormal": true
    },
    {
      "name": "甘胆酸",
      "item_code": "CG",
      "value": "1.61",
      "unit": "ug/ml",
      "reference_range": "0.00-2.70",
      "abnormal": false
    },
    {
      "name": "总胆汁酸",
      "item_code": "TBA",
      "value": "4.20",
      "unit": "umol/L",
      "reference_range": "0.00-10.00",
      "abnormal": false
    },
    {
      "name": "前白蛋白",
      "item_code": "PA",
      "value": "135",
      "unit": "mg/L",
      "reference_range": "200-430",
      "abnormal": true
    },
    {
      "name": "尿素",
      "item_code": "UREA",
      "value": "4.7",
      "unit": "mmol/L",
      "reference_range": "3.1-8.0",
      "abnormal": false
    },
    {
      "name": "肌酐",
      "item_code": "CREA",
      "value": "50.0",
      "unit": "umol/L",
      "reference_range": "57-97",
      "abnormal": true
    },
    {
      "name": "尿素/肌酐",
      "item_code": "UREA/CREA",
      "value": "0.09",
      "unit": null,
      "reference_range": "0.01-0.70",
      "abnormal": false
    },
    {
      "name": "估算肾小球滤过率",
      "item_code": "eGFR",
      "value": "119",
      "unit": "mL/min/1.73m2",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "尿酸",
      "item_code": "UA",
      "value": "326",
      "unit": "umol/L",
      "reference_range": "208-428",
      "abnormal": false
    },
    {
      "name": "钾",
      "item_code": "K",
      "value": "4.0",
      "unit": "mmol/L",
      "reference_range": "3.5-5.3",
      "abnormal": false
    },
    {
      "name": "钠",
      "item_code": "Na",
      "value": "139",
      "unit": "mmol/L",
      "reference_range": "137-147",
      "abnormal": false
    },
    {
      "name": "氯",
      "item_code": "CL",
      "value": "104",
      "unit": "mmol/L",
      "reference_range": "99-110",
      "abnormal": false
    },
    {
      "name": "总二氧化碳",
      "item_code": "CO2",
      "value": "22",
      "unit": "mmol/L",
      "reference_range": "22-29",
      "abnormal": false
    },
    {
      "name": "阴离子间隙",
      "item_code": "AG",
      "value": "13",
      "unit": "mmol/L",
      "reference_range": "8-16",
      "abnormal": false
    }
  ]
}
2026-08-10 18:11:56,913 INFO     29 [qwen-vl-table] coord grouping: {8: 27}
2026-08-10 18:11:56,915 INFO     29 [qwen-vl-table] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=937748, prompt_len=650
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
丙氨酸氨基转移酶、天门冬氨酸氨基转移酶、AST/ALT、总胆红素、直接胆红素、间接胆红素、总蛋白、白蛋白、球蛋白、白球比、碱性磷酸酶、谷氨酸脱氢酶、γ-谷氨酰转肽酶、胆碱酯酶、甘胆酸、总胆汁酸、前白蛋白、尿素、肌酐、尿素/肌酐、估算肾小球滤过率、尿酸、钾、钠、氯、总二氧化碳、阴离子间隙

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
2026-08-10 18:12:04,140 INFO     29 [qwen-vl-table] coord API raw response (len=1334):
[
	{"text": "丙氨酸氨基转移酶", "bbox": [184, 116, 312, 126]},
	{"text": "天门冬氨酸氨基转移酶", "bbox": [184, 134, 348, 143]},
	{"text": "AST/ALT", "bbox": [184, 151, 228, 160]},
	{"text": "总胆红素", "bbox": [184, 168, 260, 177]},
	{"text": "直接胆红素", "bbox": [184, 185, 273, 194]},
	{"text": "间接胆红素", "bbox": [184, 202, 248, 211]},
	{"text": "总蛋白", "bbox": [184, 220, 248, 229]},
	{"text": "白蛋白", "bbox": [184, 237, 248, 246]},
	{"text": "球蛋白", "bbox": [184, 254, 222, 263]},
	{"text": "白球比", "bbox": [184, 271, 222, 280]},
	{"text": "碱性磷酸酶", "bbox": [184, 288, 273, 297]},
	{"text": "谷氨酸脱氢酶", "bbox": [184, 305, 260, 314]},
	{"text": "γ-谷氨酰转肽酶", "bbox": [184, 322, 306, 331]},
	{"text": "胆碱酯酶", "bbox": [184, 340, 248, 349]},
	{"text": "甘胆酸", "bbox": [184, 357, 222, 366]},
	{"text": "总胆汁酸", "bbox": [184, 374, 243, 383]},
	{"text": "前白蛋白", "bbox": [184, 391, 254, 400]},
	{"text": "尿素", "bbox": [184, 408, 236, 417]},
	{"text": "肌酐", "bbox": [184, 425, 236, 434]},
	{"text": "尿素/肌酐", "bbox": [162, 442, 243, 451]},
	{"text": "估算肾小球滤过率", "bbox": [162, 459, 286, 468]},
	{"text": "尿酸", "bbox": [184, 476, 236, 485]},
	{"text": "钾", "bbox": [184, 493, 222, 502]},
	{"text": "钠", "bbox": [184, 510, 222, 519]},
	{"text": "氯", "bbox": [184, 527, 222, 536]},
	{"text": "总二氧化碳", "bbox": [184, 544, 250, 553]},
	{"text": "阴离子间隙", "bbox": [162, 560, 250, 569]}
]
2026-08-10 18:12:04,140 INFO     29 [qwen-vl-table] coord API: raw_items=27, valid_items=27, elapsed=7.2s
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[0]: text=丙氨酸氨基转移酶, bbox=[184, 116, 312, 126]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[1]: text=天门冬氨酸氨基转移酶, bbox=[184, 134, 348, 143]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[2]: text=AST/ALT, bbox=[184, 151, 228, 160]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[3]: text=总胆红素, bbox=[184, 168, 260, 177]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[4]: text=直接胆红素, bbox=[184, 185, 273, 194]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[5]: text=间接胆红素, bbox=[184, 202, 248, 211]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[6]: text=总蛋白, bbox=[184, 220, 248, 229]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[7]: text=白蛋白, bbox=[184, 237, 248, 246]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[8]: text=球蛋白, bbox=[184, 254, 222, 263]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[9]: text=白球比, bbox=[184, 271, 222, 280]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[10]: text=碱性磷酸酶, bbox=[184, 288, 273, 297]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[11]: text=谷氨酸脱氢酶, bbox=[184, 305, 260, 314]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[12]: text=γ-谷氨酰转肽酶, bbox=[184, 322, 306, 331]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[13]: text=胆碱酯酶, bbox=[184, 340, 248, 349]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[14]: text=甘胆酸, bbox=[184, 357, 222, 366]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[15]: text=总胆汁酸, bbox=[184, 374, 243, 383]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[16]: text=前白蛋白, bbox=[184, 391, 254, 400]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[17]: text=尿素, bbox=[184, 408, 236, 417]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[18]: text=肌酐, bbox=[184, 425, 236, 434]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[19]: text=尿素/肌酐, bbox=[162, 442, 243, 451]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[20]: text=估算肾小球滤过率, bbox=[162, 459, 286, 468]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[21]: text=尿酸, bbox=[184, 476, 236, 485]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[22]: text=钾, bbox=[184, 493, 222, 502]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[23]: text=钠, bbox=[184, 510, 222, 519]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[24]: text=氯, bbox=[184, 527, 222, 536]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[25]: text=总二氧化碳, bbox=[184, 544, 250, 553]
2026-08-10 18:12:04,141 INFO     29 [qwen-vl-table] coord item[26]: text=阴离子间隙, bbox=[162, 560, 250, 569]
2026-08-10 18:12:04,142 INFO     29 [qwen-vl-table] page=8 coord: matched 27/27, time=7.2s
2026-08-10 18:12:04,142 INFO     29 [qwen-vl-table] new_positions (27):
[[9, 109.47999999999999, 185.64, 97.672, 106.092], [9, 109.47999999999999, 207.06, 112.828, 120.40599999999999], [9, 109.47999999999999, 135.66, 127.142, 134.72], [9, 109.47999999999999, 154.7, 141.456, 149.034], [9, 109.47999999999999, 162.435, 155.76999999999998, 163.34799999999998], [9, 109.47999999999999, 147.56, 170.084, 177.662], [9, 109.47999999999999, 147.56, 185.23999999999998, 192.81799999999998], [9, 109.47999999999999, 147.56, 199.554, 207.132], [9, 109.47999999999999, 132.09, 213.868, 221.446], [9, 109.47999999999999, 132.09, 228.182, 235.76], [9, 109.47999999999999, 162.435, 242.49599999999998, 250.07399999999998], [9, 109.47999999999999, 154.7, 256.81, 264.388], [9, 109.47999999999999, 182.07, 271.12399999999997, 278.702], [9, 109.47999999999999, 147.56, 286.28, 293.858], [9, 109.47999999999999, 132.09, 300.594, 308.17199999999997], [9, 109.47999999999999, 144.58499999999998, 314.908, 322.486], [9, 109.47999999999999, 151.13, 329.222, 336.8], [9, 109.47999999999999, 140.42, 343.536, 351.114], [9, 109.47999999999999, 140.42, 357.84999999999997, 365.428], [9, 96.39, 144.58499999999998, 372.164, 379.74199999999996], [9, 96.39, 170.17, 386.478, 394.056], [9, 109.47999999999999, 140.42, 400.792, 408.37], [9, 109.47999999999999, 132.09, 415.106, 422.68399999999997], [9, 109.47999999999999, 132.09, 429.41999999999996, 436.998], [9, 109.47999999999999, 132.09, 443.734, 451.312], [9, 109.47999999999999, 148.75, 458.048, 465.626], [9, 96.39, 148.75, 471.52, 479.09799999999996]]
2026-08-10 18:12:04,142 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=27, matched=27, pages=1, time=23.7s
2026-08-10 18:12:04,143 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:12:04,143 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:12:04,144 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[8]
2026-08-10 18:12:04,144 INFO     29 [qwen-vl-table] positions ： [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:12:04,302 INFO     29 [qwen-vl-table] page=8, rect=595x842, img=(1653x2339)
2026-08-10 18:12:04,302 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:12:04,303 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 406, \"bbox_end\": 414, \"encounter_dates\": [\"2026-03-07\"], \"department\": \"检验科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllll}\n报告时间: 2026-03-07\n\\hline\n中文名称 & 英文缩写 & 结果 & 单位 & 提示 & 参考区间 & 检测方法 \\\\\n\\hline\n28. 唾液酸 & SA & 969 & mg/L & ↑ & 456-754 & 酶法 \\\\\n29. 补体Clq & Clq & 16.5 & mg/dl & & 15.7-23.7 & 免疫比浊法 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 18:12:04,304 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:12:04.304+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 85, "failed": 0, "current": {"a677452e94e611f1bd9827cf206dfa2d": {"id": "a677452e94e611f1bd9827cf206dfa2d", "doc_id": "a646f41e94e611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 11495294, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385378144, "task_type": "dataflow", "root_trace_id": "971de7c4c0604c27afceabc8ac295233", "root_traceparent": "00-971de7c4c0604c27afceabc8ac295233-de3f877b239fe0d8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:12:06,408 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:12:06,408 INFO     29 [qwen-vl-table] page=8 LLM output (len=382):
{
  "report_date": "2026-03-07",
  "items": [
    {
      "name": "唾液酸",
      "item_code": "SA",
      "value": "969",
      "unit": "mg/L",
      "reference_range": "456-754",
      "abnormal": true
    },
    {
      "name": "补体Clq",
      "item_code": "Clq",
      "value": "16.5",
      "unit": "mg/dl",
      "reference_range": "15.7-23.7",
      "abnormal": false
    }
  ]
}
2026-08-10 18:12:06,408 INFO     29 [qwen-vl-table] coord grouping: {8: 2}
2026-08-10 18:12:06,409 INFO     29 [qwen-vl-table] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=937748, prompt_len=516
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
唾液酸、补体Clq

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
2026-08-10 18:12:07,283 INFO     29 [qwen-vl-table] coord API raw response (len=112):
```json
[
	{"text": "唾液酸", "bbox": [165, 860, 227, 871]},
	{"text": "补体Clq", "bbox": [165, 878, 234, 889]}
]
```
2026-08-10 18:12:07,283 INFO     29 [qwen-vl-table] coord API: raw_items=2, valid_items=2, elapsed=0.9s
2026-08-10 18:12:07,284 INFO     29 [qwen-vl-table] coord item[0]: text=唾液酸, bbox=[165, 860, 227, 871]
2026-08-10 18:12:07,284 INFO     29 [qwen-vl-table] coord item[1]: text=补体Clq, bbox=[165, 878, 234, 889]
2026-08-10 18:12:07,284 INFO     29 [qwen-vl-table] page=8 coord: matched 2/2, time=0.9s
2026-08-10 18:12:07,284 INFO     29 [qwen-vl-table] new_positions (2):
[[9, 98.175, 135.065, 724.12, 733.382], [9, 98.175, 139.23, 739.276, 748.538]]
2026-08-10 18:12:07,285 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=2, matched=2, pages=1, time=3.1s
2026-08-10 18:12:07,287 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:12:07,289 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:12:07,289 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[9]
2026-08-10 18:12:07,289 INFO     29 [qwen-vl-table] positions ： [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:12:07,464 INFO     29 [qwen-vl-table] page=9, rect=595x842, img=(1653x2339)
2026-08-10 18:12:07,464 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:12:07,465 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 415, \"bbox_end\": 434, \"encounter_dates\": [\"2026-03-07\"], \"department\": \"检验科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllll}\n报告时间: 2026-03-07\n\\hline\n中文名称 & 英文缩写 & 结果 & 单位 & 提示参考区间 & 检测方法 \\\\\n\\hline\n1. 凝血酶原时间$\\ast\\ast\\star$ & PT & 14.4 & 秒 & 10.70--14.80 & 凝固法 \\\\\n2. 凝血酶原时间活动度 & PT\\% & 85.00 & \\% & 70.00--150.00 & 换算值 \\\\\n3. 凝血酶原时间比值 & PT. R & 1.08 & & 0.82--1.15 & 换算值 \\\\\n4. & PT. INR & 1.10 & & 1.0--2.0 & \\\\\n\\multicolumn{2}{l}{国际标准化比值$\\ast\\ast\\star$} & & & \\multicolumn{2}{l}{口服抗凝剂：换算值} \\\\\n\\multicolumn{2}{l}{} & & & \\multicolumn{2}{l}{1.8--2.5} \\\\\n5. 活化部分凝血活酶时间$\\ast\\ast\\star$ & APTT & 43.2 & 秒 & $\\uparrow$ 28.00--43.00 & 凝固法 \\\\\n6. 活化部分凝血活酶时间比值 & APTT R & 1.27 & & $\\uparrow$ 0.82--1.26 & 换算值 \\\\\n7. 纤维蛋白原$\\ast\\ast$ & Fib & 6.490 & g/L & $\\uparrow$ 2.000--4.000 & Clauss法 \\\\\n8. 凝血酶时间$\\ast\\ast$ & TT & 17.10 & 秒 & 14.00--21.00 & 凝固法 \\\\\n9. D-二聚体$\\ast$ & D-Dimer & 3.20 & mg/L(FEU) & $\\uparrow$ 0.00--0.50 & 免疫比浊法 \\\\\n10抗凝血酶活性$\\ast$ & AT:A & 92.00 & \\% & 80.00--130.00 & 发色底物法 \\\\\n11纤维蛋白(原)降解产物$\\ast$ & FDP & 14.63 & mg/L & $\\uparrow$ 0.00--5.00 & 免疫比浊法 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 18:12:13,948 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:12:13,948 INFO     29 [qwen-vl-table] page=9 LLM output (len=1957):
{
  "report_date": "2026-03-07",
  "items": [
    {
      "name": "凝血酶原时间",
      "item_code": "PT",
      "value": "14.4",
      "unit": "秒",
      "reference_range": "10.70--14.80",
      "abnormal": false
    },
    {
      "name": "凝血酶原时间活动度",
      "item_code": "PT%",
      "value": "85.00",
      "unit": "%",
      "reference_range": "70.00--150.00",
      "abnormal": false
    },
    {
      "name": "凝血酶原时间比值",
      "item_code": "PT. R",
      "value": "1.08",
      "unit": null,
      "reference_range": "0.82--1.15",
      "abnormal": false
    },
    {
      "name": "国际标准化比值",
      "item_code": "PT. INR",
      "value": "1.10",
      "unit": null,
      "reference_range": "1.0--2.0",
      "abnormal": false
    },
    {
      "name": "活化部分凝血活酶时间",
      "item_code": "APTT",
      "value": "43.2",
      "unit": "秒",
      "reference_range": "28.00--43.00",
      "abnormal": true
    },
    {
      "name": "活化部分凝血活酶时间比值",
      "item_code": "APTT R",
      "value": "1.27",
      "unit": null,
      "reference_range": "0.82--1.26",
      "abnormal": true
    },
    {
      "name": "纤维蛋白原",
      "item_code": "Fib",
      "value": "6.490",
      "unit": "g/L",
      "reference_range": "2.000--4.000",
      "abnormal": true
    },
    {
      "name": "凝血酶时间",
      "item_code": "TT",
      "value": "17.10",
      "unit": "秒",
      "reference_range": "14.00--21.00",
      "abnormal": false
    },
    {
      "name": "D-二聚体",
      "item_code": "D-Dimer",
      "value": "3.20",
      "unit": "mg/L(FEU)",
      "reference_range": "0.00--0.50",
      "abnormal": true
    },
    {
      "name": "抗凝血酶活性",
      "item_code": "AT:A",
      "value": "92.00",
      "unit": "%",
      "reference_range": "80.00--130.00",
      "abnormal": false
    },
    {
      "name": "纤维蛋白(原)降解产物",
      "item_code": "FDP",
      "value": "14.63",
      "unit": "mg/L",
      "reference_range": "0.00--5.00",
      "abnormal": true
    }
  ]
}
2026-08-10 18:12:13,948 INFO     29 [qwen-vl-table] coord grouping: {9: 11}
2026-08-10 18:12:13,950 INFO     29 [qwen-vl-table] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=738348, prompt_len=601
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
凝血酶原时间、凝血酶原时间活动度、凝血酶原时间比值、国际标准化比值、活化部分凝血活酶时间、活化部分凝血活酶时间比值、纤维蛋白原、凝血酶时间、D-二聚体、抗凝血酶活性、纤维蛋白(原)降解产物

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
2026-08-10 18:12:19,887 INFO     29 [qwen-vl-table] coord API raw response (len=582):
```json
[
	{"text": "凝血酶原时间", "bbox": [57, 164, 207, 177]},
	{"text": "凝血酶原时间活动度", "bbox": [57, 185, 225, 198]},
	{"text": "凝血酶原时间比值", "bbox": [57, 206, 207, 219]},
	{"text": "国际标准化比值", "bbox": [75, 241, 225, 254]},
	{"text": "活化部分凝血活酶时间", "bbox": [57, 274, 275, 288]},
	{"text": "活化部分凝血活酶时间比值", "bbox": [57, 295, 275, 308]},
	{"text": "纤维蛋白原", "bbox": [57, 317, 174, 330]},
	{"text": "凝血酶时间", "bbox": [57, 338, 174, 351]},
	{"text": "D-二聚体", "bbox": [57, 359, 150, 372]},
	{"text": "抗凝血酶活性", "bbox": [57, 379, 183, 392]},
	{"text": "纤维蛋白(原)降解产物", "bbox": [57, 400, 250, 413]}
]
```
2026-08-10 18:12:19,888 INFO     29 [qwen-vl-table] coord API: raw_items=11, valid_items=11, elapsed=5.9s
2026-08-10 18:12:19,888 INFO     29 [qwen-vl-table] coord item[0]: text=凝血酶原时间, bbox=[57, 164, 207, 177]
2026-08-10 18:12:19,888 INFO     29 [qwen-vl-table] coord item[1]: text=凝血酶原时间活动度, bbox=[57, 185, 225, 198]
2026-08-10 18:12:19,888 INFO     29 [qwen-vl-table] coord item[2]: text=凝血酶原时间比值, bbox=[57, 206, 207, 219]
2026-08-10 18:12:19,888 INFO     29 [qwen-vl-table] coord item[3]: text=国际标准化比值, bbox=[75, 241, 225, 254]
2026-08-10 18:12:19,888 INFO     29 [qwen-vl-table] coord item[4]: text=活化部分凝血活酶时间, bbox=[57, 274, 275, 288]
2026-08-10 18:12:19,888 INFO     29 [qwen-vl-table] coord item[5]: text=活化部分凝血活酶时间比值, bbox=[57, 295, 275, 308]
2026-08-10 18:12:19,888 INFO     29 [qwen-vl-table] coord item[6]: text=纤维蛋白原, bbox=[57, 317, 174, 330]
2026-08-10 18:12:19,888 INFO     29 [qwen-vl-table] coord item[7]: text=凝血酶时间, bbox=[57, 338, 174, 351]
2026-08-10 18:12:19,888 INFO     29 [qwen-vl-table] coord item[8]: text=D-二聚体, bbox=[57, 359, 150, 372]
2026-08-10 18:12:19,888 INFO     29 [qwen-vl-table] coord item[9]: text=抗凝血酶活性, bbox=[57, 379, 183, 392]
2026-08-10 18:12:19,888 INFO     29 [qwen-vl-table] coord item[10]: text=纤维蛋白(原)降解产物, bbox=[57, 400, 250, 413]
2026-08-10 18:12:19,889 INFO     29 [qwen-vl-table] page=9 coord: matched 11/11, time=5.9s
2026-08-10 18:12:19,889 INFO     29 [qwen-vl-table] new_positions (11):
[[10, 33.915, 123.16499999999999, 138.088, 149.034], [10, 33.915, 133.875, 155.76999999999998, 166.716], [10, 33.915, 123.16499999999999, 173.452, 184.398], [10, 44.625, 133.875, 202.922, 213.868], [10, 33.915, 163.625, 230.708, 242.49599999999998], [10, 33.915, 163.625, 248.39, 259.336], [10, 33.915, 103.53, 266.914, 277.86], [10, 33.915, 103.53, 284.596, 295.542], [10, 33.915, 89.25, 302.27799999999996, 313.224], [10, 33.915, 108.88499999999999, 319.118, 330.06399999999996], [10, 33.915, 148.75, 336.8, 347.746]]
2026-08-10 18:12:19,889 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=11, matched=11, pages=1, time=12.6s
2026-08-10 18:12:19,891 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:12:19,894 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:12:19,894 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[10]
2026-08-10 18:12:19,894 INFO     29 [qwen-vl-table] positions ： [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:12:20,091 INFO     29 [qwen-vl-table] page=10, rect=595x842, img=(1653x2339)
2026-08-10 18:12:20,091 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:12:20,091 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 435, \"bbox_end\": 466, \"encounter_dates\": [\"2026-03-07\"], \"department\": \"检验科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllll}\n报告时间: 2026-03-07\n\\hline\n中文名称 & 英文缩写 & 结果 & 提示 & 参考区间 & 单位 & 检测方法 \\\\\n\\hline\n1. 白细胞计数$\\text{##}\\star$ & WBC & 3.96 & & 3.50--9.50 & $*10^9/\\text{L}$ & 仪器法 \\\\\n2. 中性粒细胞计数 & NEUT\\# & 2.89 & & 1.80--6.30 & $*10^9/\\text{L}$ & 仪器法 \\\\\n3. 淋巴细胞计数 & LYMPH\\# & 0.65 & $\\downarrow$ & 1.10--3.20 & $*10^9/\\text{L}$ & 仪器法 \\\\\n4. 单核细胞计数 & MONO\\# & 0.30 & & 0.10--0.60 & $*10^9/\\text{L}$ & 仪器法 \\\\\n5. 嗜酸细胞计数 & EO\\# & 0.10 & & 0.02--0.52 & $*10^9/\\text{L}$ & 仪器法 \\\\\n6. 嗜碱细胞计数 & BASO\\# & 0.02 & & 0.00--0.06 & $*10^9/\\text{L}$ & 仪器法 \\\\\n7. 中性粒细胞百分比 & NEUT\\% & 73.0 & & 40.0--75.0 & \\% & 仪器法 \\\\\n8. 淋巴细胞百分比 & LYMPH\\% & 16.4 & $\\downarrow$ & 20.0--50.0 & \\% & 仪器法 \\\\\n9. 单核细胞百分比 & MONO\\% & 7.6 & & 3.0--10.0 & \\% & 仪器法 \\\\\n10. 嗜酸细胞百分比 & E0\\% & 2.6 & & 0.40--8.00 & \\% & 仪器法 \\\\\n11. 嗜碱细胞百分比 & BASO\\% & 0.4 & & 0.00--1.00 & \\% & 仪器法 \\\\\n12. 红细胞计数$\\text{##}\\star$ & RBC & 3.57 & $\\downarrow$ & 4.30--5.80 & $*10^12/\\text{L}$ & 仪器法 \\\\\n13. 血红蛋白含量$\\text{##}\\star$ & HGB & 88 & $\\downarrow$ & 130--175 & g/L & 仪器法 \\\\\n14. 红细胞比容$\\text{##}\\star$ & HCT & 0.28 & $\\downarrow$ & 0.40--0.50 & L/L & 仪器法 \\\\\n15. 平均红细胞血红蛋白含量$\\text{##}\\star$ & MCH & 24.6 & $\\downarrow$ & 27.0--34.0 & pg & 仪器法 \\\\\n16. 平均红细胞血红蛋白浓度$\\text{##}\\star$ & MCHC & 319 & & 316--354 & g/L & 仪器法 \\\\\n17. 平均红细胞体积$\\text{##}\\star$ & MCV & 77.2 & $\\downarrow$ & 82.0--100.0 & fL & 仪器法 \\\\\n18. 红细胞分布宽度（CV） & RDW--CV & 17.4 & $\\uparrow$ & 11.6--16.5 & \\% & 仪器法 \\\\\n19. 红细胞分布宽度（SD） & RDW--SD & 50.1 & & 37.0--54.0 & fL & 仪器法 \\\\\n20. 血小板计数$\\text{##}\\star$ & PLT & 268 & & 125--350 & $*10^9/\\text{L}$ & 仪器法 \\\\\n21. 平均血小板体积 & MPV & 8.2 & & 7.4--11.0 & fL & 仪器法 \\\\\n22. 大血小板比率 & P--LCR & 14.8 & & 13.0--43.0 & \\% & 仪器法 \\\\\n23. 血小板比容 & PCT & 0.22 & & 0.170--0.350 & \\% & 仪器法 \\\\\n24. 血小板分布宽度 & PDW & 15.4 & $\\downarrow$ & 15.5--16.8 & fL & 仪器法 \\\\\n25. C--反应蛋白$\\text{*}$ & CRP & 30.830 & $\\uparrow$ & 0.000--5.000 & mg/L & 散射比浊法 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 18:12:33,769 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:12:33,769 INFO     29 [qwen-vl-table] page=10 LLM output (len=4350):
{
  "report_date": "2026-03-07",
  "items": [
    {
      "name": "白细胞计数",
      "item_code": "WBC",
      "value": "3.96",
      "unit": "*10^9/L",
      "reference_range": "3.50--9.50",
      "abnormal": false
    },
    {
      "name": "中性粒细胞计数",
      "item_code": "NEUT#",
      "value": "2.89",
      "unit": "*10^9/L",
      "reference_range": "1.80--6.30",
      "abnormal": false
    },
    {
      "name": "淋巴细胞计数",
      "item_code": "LYMPH#",
      "value": "0.65",
      "unit": "*10^9/L",
      "reference_range": "1.10--3.20",
      "abnormal": true
    },
    {
      "name": "单核细胞计数",
      "item_code": "MONO#",
      "value": "0.30",
      "unit": "*10^9/L",
      "reference_range": "0.10--0.60",
      "abnormal": false
    },
    {
      "name": "嗜酸细胞计数",
      "item_code": "EO#",
      "value": "0.10",
      "unit": "*10^9/L",
      "reference_range": "0.02--0.52",
      "abnormal": false
    },
    {
      "name": "嗜碱细胞计数",
      "item_code": "BASO#",
      "value": "0.02",
      "unit": "*10^9/L",
      "reference_range": "0.00--0.06",
      "abnormal": false
    },
    {
      "name": "中性粒细胞百分比",
      "item_code": "NEUT%",
      "value": "73.0",
      "unit": "%",
      "reference_range": "40.0--75.0",
      "abnormal": false
    },
    {
      "name": "淋巴细胞百分比",
      "item_code": "LYMPH%",
      "value": "16.4",
      "unit": "%",
      "reference_range": "20.0--50.0",
      "abnormal": true
    },
    {
      "name": "单核细胞百分比",
      "item_code": "MONO%",
      "value": "7.6",
      "unit": "%",
      "reference_range": "3.0--10.0",
      "abnormal": false
    },
    {
      "name": "嗜酸细胞百分比",
      "item_code": "E0%",
      "value": "2.6",
      "unit": "%",
      "reference_range": "0.40--8.00",
      "abnormal": false
    },
    {
      "name": "嗜碱细胞百分比",
      "item_code": "BASO%",
      "value": "0.4",
      "unit": "%",
      "reference_range": "0.00--1.00",
      "abnormal": false
    },
    {
      "name": "红细胞计数",
      "item_code": "RBC",
      "value": "3.57",
      "unit": "*10^12/L",
      "reference_range": "4.30--5.80",
      "abnormal": true
    },
    {
      "name": "血红蛋白含量",
      "item_code": "HGB",
      "value": "88",
      "unit": "g/L",
      "reference_range": "130--175",
      "abnormal": true
    },
    {
      "name": "红细胞比容",
      "item_code": "HCT",
      "value": "0.28",
      "unit": "L/L",
      "reference_range": "0.40--0.50",
      "abnormal": true
    },
    {
      "name": "平均红细胞血红蛋白含量",
      "item_code": "MCH",
      "value": "24.6",
      "unit": "pg",
      "reference_range": "27.0--34.0",
      "abnormal": true
    },
    {
      "name": "平均红细胞血红蛋白浓度",
      "item_code": "MCHC",
      "value": "319",
      "unit": "g/L",
      "reference_range": "316--354",
      "abnormal": false
    },
    {
      "name": "平均红细胞体积",
      "item_code": "MCV",
      "value": "77.2",
      "unit": "fL",
      "reference_range": "82.0--100.0",
      "abnormal": true
    },
    {
      "name": "红细胞分布宽度（CV）",
      "item_code": "RDW--CV",
      "value": "17.4",
      "unit": "%",
      "reference_range": "11.6--16.5",
      "abnormal": true
    },
    {
      "name": "红细胞分布宽度（SD）",
      "item_code": "RDW--SD",
      "value": "50.1",
      "unit": "fL",
      "reference_range": "37.0--54.0",
      "abnormal": false
    },
    {
      "name": "血小板计数",
      "item_code": "PLT",
      "value": "268",
      "unit": "*10^9/L",
      "reference_range": "125--350",
      "abnormal": false
    },
    {
      "name": "平均血小板体积",
      "item_code": "MPV",
      "value": "8.2",
      "unit": "fL",
      "reference_range": "7.4--11.0",
      "abnormal": false
    },
    {
      "name": "大血小板比率",
      "item_code": "P--LCR",
      "value": "14.8",
      "unit": "%",
      "reference_range": "13.0--43.0",
      "abnormal": false
    },
    {
      "name": "血小板比容",
      "item_code": "PCT",
      "value": "0.22",
      "unit": "%",
      "reference_range": "0.170--0.350",
      "abnormal": false
    },
    {
      "name": "血小板分布宽度",
      "item_code": "PDW",
      "value": "15.4",
      "unit": "fL",
      "reference_range": "15.5--16.8",
      "abnormal": true
    },
    {
      "name": "C--反应蛋白",
      "item_code": "CRP",
      "value": "30.830",
      "unit": "mg/L",
      "reference_range": "0.000--5.000",
      "abnormal": true
    }
  ]
}
2026-08-10 18:12:33,770 INFO     29 [qwen-vl-table] coord grouping: {10: 25}
2026-08-10 18:12:33,772 INFO     29 [qwen-vl-table] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1072851, prompt_len=707
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞计数、中性粒细胞计数、淋巴细胞计数、单核细胞计数、嗜酸细胞计数、嗜碱细胞计数、中性粒细胞百分比、淋巴细胞百分比、单核细胞百分比、嗜酸细胞百分比、嗜碱细胞百分比、红细胞计数、血红蛋白含量、红细胞比容、平均红细胞血红蛋白含量、平均红细胞血红蛋白浓度、平均红细胞体积、红细胞分布宽度（CV）、红细胞分布宽度（SD）、血小板计数、平均血小板体积、大血小板比率、血小板比容、血小板分布宽度、C--反应蛋白

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
2026-08-10 18:12:40,931 INFO     29 [qwen-vl-table] coord API raw response (len=1290):
```json
[
	{"text": "白细胞计数", "bbox": [88, 161, 206, 174]},
	{"text": "中性粒细胞计数", "bbox": [88, 178, 206, 191]},
	{"text": "淋巴细胞计数", "bbox": [88, 197, 188, 209]},
	{"text": "单核细胞计数", "bbox": [88, 214, 188, 227]},
	{"text": "嗜酸细胞计数", "bbox": [88, 231, 188, 244]},
	{"text": "嗜碱细胞计数", "bbox": [88, 249, 188, 262]},
	{"text": "中性粒细胞百分比", "bbox": [88, 266, 222, 279]},
	{"text": "淋巴细胞百分比", "bbox": [88, 284, 206, 297]},
	{"text": "单核细胞百分比", "bbox": [88, 301, 206, 314]},
	{"text": "嗜酸细胞百分比", "bbox": [88, 320, 206, 333]},
	{"text": "嗜碱细胞百分比", "bbox": [88, 337, 206, 350]},
	{"text": "红细胞计数", "bbox": [65, 355, 206, 368]},
	{"text": "血红蛋白含量", "bbox": [65, 372, 222, 385]},
	{"text": "红细胞比容", "bbox": [65, 390, 206, 403]},
	{"text": "平均红细胞血红蛋白含量", "bbox": [65, 407, 306, 420]},
	{"text": "平均红细胞血红蛋白浓度", "bbox": [65, 425, 306, 438]},
	{"text": "平均红细胞体积", "bbox": [65, 442, 240, 455]},
	{"text": "红细胞分布宽度（CV）", "bbox": [65, 460, 248, 473]},
	{"text": "红细胞分布宽度（SD）", "bbox": [65, 477, 248, 490]},
	{"text": "血小板计数", "bbox": [65, 495, 206, 508]},
	{"text": "平均血小板体积", "bbox": [65, 512, 206, 525]},
	{"text": "大血小板比率", "bbox": [65, 530, 188, 543]},
	{"text": "血小板比容", "bbox": [65, 547, 172, 560]},
	{"text": "血小板分布宽度", "bbox": [65, 565, 206, 578]},
	{"text": "C--反应蛋白", "bbox": [65, 582, 180, 595]}
]
```
2026-08-10 18:12:40,932 INFO     29 [qwen-vl-table] coord API: raw_items=25, valid_items=25, elapsed=7.2s
2026-08-10 18:12:40,932 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞计数, bbox=[88, 161, 206, 174]
2026-08-10 18:12:40,932 INFO     29 [qwen-vl-table] coord item[1]: text=中性粒细胞计数, bbox=[88, 178, 206, 191]
2026-08-10 18:12:40,932 INFO     29 [qwen-vl-table] coord item[2]: text=淋巴细胞计数, bbox=[88, 197, 188, 209]
2026-08-10 18:12:40,932 INFO     29 [qwen-vl-table] coord item[3]: text=单核细胞计数, bbox=[88, 214, 188, 227]
2026-08-10 18:12:40,932 INFO     29 [qwen-vl-table] coord item[4]: text=嗜酸细胞计数, bbox=[88, 231, 188, 244]
2026-08-10 18:12:40,932 INFO     29 [qwen-vl-table] coord item[5]: text=嗜碱细胞计数, bbox=[88, 249, 188, 262]
2026-08-10 18:12:40,932 INFO     29 [qwen-vl-table] coord item[6]: text=中性粒细胞百分比, bbox=[88, 266, 222, 279]
2026-08-10 18:12:40,932 INFO     29 [qwen-vl-table] coord item[7]: text=淋巴细胞百分比, bbox=[88, 284, 206, 297]
2026-08-10 18:12:40,932 INFO     29 [qwen-vl-table] coord item[8]: text=单核细胞百分比, bbox=[88, 301, 206, 314]
2026-08-10 18:12:40,932 INFO     29 [qwen-vl-table] coord item[9]: text=嗜酸细胞百分比, bbox=[88, 320, 206, 333]
2026-08-10 18:12:40,932 INFO     29 [qwen-vl-table] coord item[10]: text=嗜碱细胞百分比, bbox=[88, 337, 206, 350]
2026-08-10 18:12:40,932 INFO     29 [qwen-vl-table] coord item[11]: text=红细胞计数, bbox=[65, 355, 206, 368]
2026-08-10 18:12:40,932 INFO     29 [qwen-vl-table] coord item[12]: text=血红蛋白含量, bbox=[65, 372, 222, 385]
2026-08-10 18:12:40,932 INFO     29 [qwen-vl-table] coord item[13]: text=红细胞比容, bbox=[65, 390, 206, 403]
2026-08-10 18:12:40,932 INFO     29 [qwen-vl-table] coord item[14]: text=平均红细胞血红蛋白含量, bbox=[65, 407, 306, 420]
2026-08-10 18:12:40,932 INFO     29 [qwen-vl-table] coord item[15]: text=平均红细胞血红蛋白浓度, bbox=[65, 425, 306, 438]
2026-08-10 18:12:40,932 INFO     29 [qwen-vl-table] coord item[16]: text=平均红细胞体积, bbox=[65, 442, 240, 455]
2026-08-10 18:12:40,932 INFO     29 [qwen-vl-table] coord item[17]: text=红细胞分布宽度（CV）, bbox=[65, 460, 248, 473]
2026-08-10 18:12:40,932 INFO     29 [qwen-vl-table] coord item[18]: text=红细胞分布宽度（SD）, bbox=[65, 477, 248, 490]
2026-08-10 18:12:40,933 INFO     29 [qwen-vl-table] coord item[19]: text=血小板计数, bbox=[65, 495, 206, 508]
2026-08-10 18:12:40,933 INFO     29 [qwen-vl-table] coord item[20]: text=平均血小板体积, bbox=[65, 512, 206, 525]
2026-08-10 18:12:40,933 INFO     29 [qwen-vl-table] coord item[21]: text=大血小板比率, bbox=[65, 530, 188, 543]
2026-08-10 18:12:40,933 INFO     29 [qwen-vl-table] coord item[22]: text=血小板比容, bbox=[65, 547, 172, 560]
2026-08-10 18:12:40,933 INFO     29 [qwen-vl-table] coord item[23]: text=血小板分布宽度, bbox=[65, 565, 206, 578]
2026-08-10 18:12:40,933 INFO     29 [qwen-vl-table] coord item[24]: text=C--反应蛋白, bbox=[65, 582, 180, 595]
2026-08-10 18:12:40,933 INFO     29 [qwen-vl-table] page=10 coord: matched 25/25, time=7.2s
2026-08-10 18:12:40,933 INFO     29 [qwen-vl-table] new_positions (25):
[[11, 52.36, 122.57, 135.56199999999998, 146.50799999999998], [11, 52.36, 122.57, 149.876, 160.822], [11, 52.36, 111.86, 165.874, 175.97799999999998], [11, 52.36, 111.86, 180.188, 191.134], [11, 52.36, 111.86, 194.50199999999998, 205.44799999999998], [11, 52.36, 111.86, 209.658, 220.60399999999998], [11, 52.36, 132.09, 223.97199999999998, 234.91799999999998], [11, 52.36, 122.57, 239.128, 250.07399999999998], [11, 52.36, 122.57, 253.44199999999998, 264.388], [11, 52.36, 122.57, 269.44, 280.38599999999997], [11, 52.36, 122.57, 283.75399999999996, 294.7], [11, 38.675, 122.57, 298.90999999999997, 309.856], [11, 38.675, 132.09, 313.224, 324.17], [11, 38.675, 122.57, 328.38, 339.32599999999996], [11, 38.675, 182.07, 342.69399999999996, 353.64], [11, 38.675, 182.07, 357.84999999999997, 368.796], [11, 38.675, 142.79999999999998, 372.164, 383.11], [11, 38.675, 147.56, 387.32, 398.26599999999996], [11, 38.675, 147.56, 401.63399999999996, 412.58], [11, 38.675, 122.57, 416.78999999999996, 427.736], [11, 38.675, 122.57, 431.104, 442.05], [11, 38.675, 111.86, 446.26, 457.20599999999996], [11, 38.675, 102.33999999999999, 460.574, 471.52], [11, 38.675, 122.57, 475.72999999999996, 486.676], [11, 38.675, 107.1, 490.044, 500.99]]
2026-08-10 18:12:40,933 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=25, matched=25, pages=1, time=21.0s
2026-08-10 18:12:40,935 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:12:40,937 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:12:40,937 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[11]
2026-08-10 18:12:40,937 INFO     29 [qwen-vl-table] positions ： [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:12:41,097 INFO     29 [qwen-vl-table] page=11, rect=595x842, img=(1653x2339)
2026-08-10 18:12:41,097 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:12:41,098 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 467, \"bbox_end\": 481, \"encounter_dates\": [\"2026-03-07\"], \"department\": \"检验科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllll}\n报告时间: 2026-03-07\n\\hline\n中文名称 & 英文缩写 & 结果 & 单位 & 提示参考区间 & 检测方法 \\\\\n\\hline\n1. 粪便颜色 & Colour & 黄色 & & 棕黄 & 手工法 \\\\\n2. 粪便性状 & Stool-type & 软 & & 软 & 手工法 \\\\\n3. 白细胞 & WBC & 未见 & /HPF & 0-3/阴性 & 手工法 \\\\\n4. 红细胞 & RBC & 未见 & /HPF & 阴性 & 手工法 \\\\\n5. 脂肪滴 & Fat droplet & 未见 & /HPF & 阴性 & 手工法 \\\\\n6. 真菌 & Fungus & 未见 & /HPF & 阴性 & 手工法 \\\\\n7. 寄生虫卵 & Parasitic ovum & 未见 & & 阴性 & 手工法 \\\\\n8. 隐血试验 & OBT & 阳性反应 (+) & & A 阴性反应 (-) & 胶体金法 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 18:12:41,100 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:12:41.099+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 85, "failed": 0, "current": {"a677452e94e611f1bd9827cf206dfa2d": {"id": "a677452e94e611f1bd9827cf206dfa2d", "doc_id": "a646f41e94e611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 11495294, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385378144, "task_type": "dataflow", "root_trace_id": "971de7c4c0604c27afceabc8ac295233", "root_traceparent": "00-971de7c4c0604c27afceabc8ac295233-de3f877b239fe0d8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:12:45,580 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:12:45,581 INFO     29 [qwen-vl-table] page=11 LLM output (len=1356):
{
  "report_date": "2026-03-07",
  "items": [
    {
      "name": "粪便颜色",
      "item_code": "Colour",
      "value": "黄色",
      "unit": null,
      "reference_range": "棕黄",
      "abnormal": false
    },
    {
      "name": "粪便性状",
      "item_code": "Stool-type",
      "value": "软",
      "unit": null,
      "reference_range": "软",
      "abnormal": false
    },
    {
      "name": "白细胞",
      "item_code": "WBC",
      "value": "未见",
      "unit": "/HPF",
      "reference_range": "0-3/阴性",
      "abnormal": false
    },
    {
      "name": "红细胞",
      "item_code": "RBC",
      "value": "未见",
      "unit": "/HPF",
      "reference_range": "阴性",
      "abnormal": false
    },
    {
      "name": "脂肪滴",
      "item_code": "Fat droplet",
      "value": "未见",
      "unit": "/HPF",
      "reference_range": "阴性",
      "abnormal": false
    },
    {
      "name": "真菌",
      "item_code": "Fungus",
      "value": "未见",
      "unit": "/HPF",
      "reference_range": "阴性",
      "abnormal": false
    },
    {
      "name": "寄生虫卵",
      "item_code": "Parasitic ovum",
      "value": "未见",
      "unit": null,
      "reference_range": "阴性",
      "abnormal": false
    },
    {
      "name": "隐血试验",
      "item_code": "OBT",
      "value": "阳性反应 (+)",
      "unit": null,
      "reference_range": "A 阴性反应 (-)",
      "abnormal": true
    }
  ]
}
2026-08-10 18:12:45,581 INFO     29 [qwen-vl-table] coord grouping: {11: 8}
2026-08-10 18:12:45,581 INFO     29 [qwen-vl-table] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=612293, prompt_len=541
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
粪便颜色、粪便性状、白细胞、红细胞、脂肪滴、真菌、寄生虫卵、隐血试验

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
2026-08-10 18:12:50,628 INFO     29 [qwen-vl-table] coord API raw response (len=393):
```json
[
	{"text": "粪便颜色", "bbox": [52, 163, 138, 176]},
	{"text": "粪便性状", "bbox": [52, 184, 138, 197]},
	{"text": "白细胞", "bbox": [52, 205, 119, 218]},
	{"text": "红细胞", "bbox": [52, 225, 119, 238]},
	{"text": "脂肪滴", "bbox": [52, 246, 119, 259]},
	{"text": "真菌", "bbox": [52, 267, 103, 280]},
	{"text": "寄生虫卵", "bbox": [52, 288, 138, 301]},
	{"text": "隐血试验", "bbox": [52, 309, 138, 322]}
]
```
2026-08-10 18:12:50,628 INFO     29 [qwen-vl-table] coord API: raw_items=8, valid_items=8, elapsed=5.0s
2026-08-10 18:12:50,628 INFO     29 [qwen-vl-table] coord item[0]: text=粪便颜色, bbox=[52, 163, 138, 176]
2026-08-10 18:12:50,628 INFO     29 [qwen-vl-table] coord item[1]: text=粪便性状, bbox=[52, 184, 138, 197]
2026-08-10 18:12:50,628 INFO     29 [qwen-vl-table] coord item[2]: text=白细胞, bbox=[52, 205, 119, 218]
2026-08-10 18:12:50,628 INFO     29 [qwen-vl-table] coord item[3]: text=红细胞, bbox=[52, 225, 119, 238]
2026-08-10 18:12:50,628 INFO     29 [qwen-vl-table] coord item[4]: text=脂肪滴, bbox=[52, 246, 119, 259]
2026-08-10 18:12:50,628 INFO     29 [qwen-vl-table] coord item[5]: text=真菌, bbox=[52, 267, 103, 280]
2026-08-10 18:12:50,628 INFO     29 [qwen-vl-table] coord item[6]: text=寄生虫卵, bbox=[52, 288, 138, 301]
2026-08-10 18:12:50,628 INFO     29 [qwen-vl-table] coord item[7]: text=隐血试验, bbox=[52, 309, 138, 322]
2026-08-10 18:12:50,628 INFO     29 [qwen-vl-table] page=11 coord: matched 8/8, time=5.0s
2026-08-10 18:12:50,629 INFO     29 [qwen-vl-table] new_positions (8):
[[12, 30.939999999999998, 82.11, 137.246, 148.192], [12, 30.939999999999998, 82.11, 154.928, 165.874], [12, 30.939999999999998, 70.80499999999999, 172.60999999999999, 183.55599999999998], [12, 30.939999999999998, 70.80499999999999, 189.45, 200.396], [12, 30.939999999999998, 70.80499999999999, 207.132, 218.078], [12, 30.939999999999998, 61.285, 224.814, 235.76], [12, 30.939999999999998, 82.11, 242.49599999999998, 253.44199999999998], [12, 30.939999999999998, 82.11, 260.178, 271.12399999999997]]
2026-08-10 18:12:50,629 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=8, matched=8, pages=1, time=9.7s
2026-08-10 18:12:50,630 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:12:50,634 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:12:50,634 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[12]
2026-08-10 18:12:50,634 INFO     29 [qwen-vl-table] positions ： [[12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:12:50,818 INFO     29 [qwen-vl-table] page=12, rect=595x842, img=(1653x2339)
2026-08-10 18:12:50,818 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:12:50,818 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 482, \"bbox_end\": 512, \"encounter_dates\": [\"2026-03-07\"], \"department\": \"检验科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l l l l l l l}\n报告时间: 2026-03-07\n\\hline\n中文名称 & 英文缩写 & 结果 & 单位 & 提示参考区间 & 检测方法 \\\\\n\\hline\n1. 红细胞计数 & RBC & 43.00 & 个/ul & $\\uparrow$ 0.00--17.00 & \\\\\n2. 白细胞计数 & WBC & 3117.00 & 个/ul & $\\uparrow$ 0.00--28.00 & \\\\\n3. 白细胞团 & WBCC & 180.00 & 个/ul & $\\uparrow$ 0.00--2.00 & 仪器法 \\\\\n4. 鳞状上皮细胞 & SQEP & 15.00 & 个/ul & 0.00--28.00 & 仪器法 \\\\\n5. 非鳞状上皮细胞 & NSE & 0.00 & 个/ul & 0.00--6.00 & 仪器法 \\\\\n6. 透明管型 & HYAL & 0.00 & 个/ul & 0.00--1.00 & 仪器法 \\\\\n7. 病理管型 & UNCC & 1.00 & 个/ul & 0.00--1.00 & 仪器法 \\\\\n8. 酵母 & BYST & 0.00 & 个/ul & 0.00--1.00 & 仪器法 \\\\\n9. 未分类结晶 & UNCX & 49.00 & 个/ul & $\\uparrow$ 0.00--28.00 & 仪器法 \\\\\n10粘液丝 & MUCS & 12.00 & 个/ul & 0.00--46.00 & \\\\\n11细菌 & BACT & 11801.00 & 个/ul & $\\uparrow$ 0.00--340.00 & \\\\\n12潜血**☆ & BLD & 痕量(++) & & 阴性(-) & 干化学法 \\\\\n13白细胞酯酶* & LEU & 阳性(2+) & & 阴性(-) & 干化学法 \\\\\n14亚硝酸盐**☆ & NIT & 阳性(2+) & & 阴性(-) & 干化学法 \\\\\n15尿胆素原**☆ & UBG & Normal & & Normal & 干化学法 \\\\\n16胆红素**☆ & BIL & 阴性(-) & & 阴性(-) & 干化学法 \\\\\n17维生素C & VC & 阳性(+) & & 阴性(-) & 干化学法 \\\\\n18蛋白质**☆ & PRO & 痕量(++) & & 阴性(-) & 干化学法 \\\\\n19酸碱度**☆ & PH & 5.5 & & 5.0--8.0 & 干化学法 \\\\\n20比密**☆ & SG & 1.025 & & 1.005--1.030 & 干化学法 \\\\\n21葡萄糖**☆ & GLU & 阴性(-) & & 阴性(-) & 干化学法 \\\\\n22酮体**☆ & KET & 阴性(-) & & 阴性(-) & 干化学法 \\\\\n23颜色 & Colour & 黄色 & & & 手工法 \\\\\n24透明度 & Clarity & 浑浊 & & & 手工法 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 18:13:03,014 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:13:03,014 INFO     29 [qwen-vl-table] page=12 LLM output (len=4043):
{
  "report_date": "2026-03-07",
  "items": [
    {
      "name": "红细胞计数",
      "item_code": "RBC",
      "value": "43.00",
      "unit": "个/ul",
      "reference_range": "0.00--17.00",
      "abnormal": true
    },
    {
      "name": "白细胞计数",
      "item_code": "WBC",
      "value": "3117.00",
      "unit": "个/ul",
      "reference_range": "0.00--28.00",
      "abnormal": true
    },
    {
      "name": "白细胞团",
      "item_code": "WBCC",
      "value": "180.00",
      "unit": "个/ul",
      "reference_range": "0.00--2.00",
      "abnormal": true
    },
    {
      "name": "鳞状上皮细胞",
      "item_code": "SQEP",
      "value": "15.00",
      "unit": "个/ul",
      "reference_range": "0.00--28.00",
      "abnormal": false
    },
    {
      "name": "非鳞状上皮细胞",
      "item_code": "NSE",
      "value": "0.00",
      "unit": "个/ul",
      "reference_range": "0.00--6.00",
      "abnormal": false
    },
    {
      "name": "透明管型",
      "item_code": "HYAL",
      "value": "0.00",
      "unit": "个/ul",
      "reference_range": "0.00--1.00",
      "abnormal": false
    },
    {
      "name": "病理管型",
      "item_code": "UNCC",
      "value": "1.00",
      "unit": "个/ul",
      "reference_range": "0.00--1.00",
      "abnormal": false
    },
    {
      "name": "酵母",
      "item_code": "BYST",
      "value": "0.00",
      "unit": "个/ul",
      "reference_range": "0.00--1.00",
      "abnormal": false
    },
    {
      "name": "未分类结晶",
      "item_code": "UNCX",
      "value": "49.00",
      "unit": "个/ul",
      "reference_range": "0.00--28.00",
      "abnormal": true
    },
    {
      "name": "粘液丝",
      "item_code": "MUCS",
      "value": "12.00",
      "unit": "个/ul",
      "reference_range": "0.00--46.00",
      "abnormal": false
    },
    {
      "name": "细菌",
      "item_code": "BACT",
      "value": "11801.00",
      "unit": "个/ul",
      "reference_range": "0.00--340.00",
      "abnormal": true
    },
    {
      "name": "潜血",
      "item_code": "BLD",
      "value": "痕量(++)",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": true
    },
    {
      "name": "白细胞酯酶",
      "item_code": "LEU",
      "value": "阳性(2+)",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": true
    },
    {
      "name": "亚硝酸盐",
      "item_code": "NIT",
      "value": "阳性(2+)",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": true
    },
    {
      "name": "尿胆素原",
      "item_code": "UBG",
      "value": "Normal",
      "unit": null,
      "reference_range": "Normal",
      "abnormal": false
    },
    {
      "name": "胆红素",
      "item_code": "BIL",
      "value": "阴性(-)",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": false
    },
    {
      "name": "维生素C",
      "item_code": "VC",
      "value": "阳性(+)",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": true
    },
    {
      "name": "蛋白质",
      "item_code": "PRO",
      "value": "痕量(++)",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": true
    },
    {
      "name": "酸碱度",
      "item_code": "PH",
      "value": "5.5",
      "unit": null,
      "reference_range": "5.0--8.0",
      "abnormal": false
    },
    {
      "name": "比密",
      "item_code": "SG",
      "value": "1.025",
      "unit": null,
      "reference_range": "1.005--1.030",
      "abnormal": false
    },
    {
      "name": "葡萄糖",
      "item_code": "GLU",
      "value": "阴性(-)",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": false
    },
    {
      "name": "酮体",
      "item_code": "KET",
      "value": "阴性(-)",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": false
    },
    {
      "name": "颜色",
      "item_code": "Colour",
      "value": "黄色",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "透明度",
      "item_code": "Clarity",
      "value": "浑浊",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 18:13:03,014 INFO     29 [qwen-vl-table] coord grouping: {12: 24}
2026-08-10 18:13:03,017 INFO     29 [qwen-vl-table] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=956213, prompt_len=617
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
红细胞计数、白细胞计数、白细胞团、鳞状上皮细胞、非鳞状上皮细胞、透明管型、病理管型、酵母、未分类结晶、粘液丝、细菌、潜血、白细胞酯酶、亚硝酸盐、尿胆素原、胆红素、维生素C、蛋白质、酸碱度、比密、葡萄糖、酮体、颜色、透明度

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
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord API raw response (len=1145):
[
	{"text": "红细胞计数", "bbox": [53, 167, 155, 181]},
	{"text": "白细胞计数", "bbox": [53, 189, 155, 203]},
	{"text": "白细胞团", "bbox": [53, 210, 140, 224]},
	{"text": "鳞状上皮细胞", "bbox": [53, 231, 170, 245]},
	{"text": "非鳞状上皮细胞", "bbox": [53, 252, 189, 266]},
	{"text": "透明管型", "bbox": [53, 274, 140, 288]},
	{"text": "病理管型", "bbox": [53, 295, 140, 309]},
	{"text": "酵母", "bbox": [53, 316, 106, 330]},
	{"text": "未分类结晶", "bbox": [53, 337, 155, 351]},
	{"text": "粘液丝", "bbox": [53, 359, 122, 373]},
	{"text": "细菌", "bbox": [53, 380, 106, 394]},
	{"text": "潜血", "bbox": [53, 401, 140, 415]},
	{"text": "白细胞酯酶", "bbox": [53, 421, 164, 435]},
	{"text": "亚硝酸盐", "bbox": [53, 443, 170, 457]},
	{"text": "尿胆素原", "bbox": [53, 464, 170, 478]},
	{"text": "胆红素", "bbox": [53, 485, 155, 499]},
	{"text": "维生素C", "bbox": [53, 506, 132, 520]},
	{"text": "蛋白质", "bbox": [53, 527, 155, 541]},
	{"text": "酸碱度", "bbox": [53, 547, 155, 561]},
	{"text": "比密", "bbox": [53, 568, 140, 582]},
	{"text": "葡萄糖", "bbox": [53, 589, 155, 603]},
	{"text": "酮体", "bbox": [53, 610, 140, 624]},
	{"text": "颜色", "bbox": [53, 631, 108, 645]},
	{"text": "透明度", "bbox": [53, 652, 124, 666]}
]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord API: raw_items=24, valid_items=24, elapsed=6.3s
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[0]: text=红细胞计数, bbox=[53, 167, 155, 181]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[1]: text=白细胞计数, bbox=[53, 189, 155, 203]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[2]: text=白细胞团, bbox=[53, 210, 140, 224]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[3]: text=鳞状上皮细胞, bbox=[53, 231, 170, 245]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[4]: text=非鳞状上皮细胞, bbox=[53, 252, 189, 266]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[5]: text=透明管型, bbox=[53, 274, 140, 288]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[6]: text=病理管型, bbox=[53, 295, 140, 309]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[7]: text=酵母, bbox=[53, 316, 106, 330]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[8]: text=未分类结晶, bbox=[53, 337, 155, 351]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[9]: text=粘液丝, bbox=[53, 359, 122, 373]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[10]: text=细菌, bbox=[53, 380, 106, 394]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[11]: text=潜血, bbox=[53, 401, 140, 415]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[12]: text=白细胞酯酶, bbox=[53, 421, 164, 435]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[13]: text=亚硝酸盐, bbox=[53, 443, 170, 457]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[14]: text=尿胆素原, bbox=[53, 464, 170, 478]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[15]: text=胆红素, bbox=[53, 485, 155, 499]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[16]: text=维生素C, bbox=[53, 506, 132, 520]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[17]: text=蛋白质, bbox=[53, 527, 155, 541]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[18]: text=酸碱度, bbox=[53, 547, 155, 561]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[19]: text=比密, bbox=[53, 568, 140, 582]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[20]: text=葡萄糖, bbox=[53, 589, 155, 603]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[21]: text=酮体, bbox=[53, 610, 140, 624]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[22]: text=颜色, bbox=[53, 631, 108, 645]
2026-08-10 18:13:09,337 INFO     29 [qwen-vl-table] coord item[23]: text=透明度, bbox=[53, 652, 124, 666]
2026-08-10 18:13:09,338 INFO     29 [qwen-vl-table] page=12 coord: matched 24/24, time=6.3s
2026-08-10 18:13:09,338 INFO     29 [qwen-vl-table] new_positions (24):
[[13, 31.535, 92.225, 140.614, 152.402], [13, 31.535, 92.225, 159.138, 170.926], [13, 31.535, 83.3, 176.82, 188.608], [13, 31.535, 101.14999999999999, 194.50199999999998, 206.29], [13, 31.535, 112.455, 212.184, 223.97199999999998], [13, 31.535, 83.3, 230.708, 242.49599999999998], [13, 31.535, 83.3, 248.39, 260.178], [13, 31.535, 63.07, 266.072, 277.86], [13, 31.535, 92.225, 283.75399999999996, 295.542], [13, 31.535, 72.59, 302.27799999999996, 314.066], [13, 31.535, 63.07, 319.96, 331.748], [13, 31.535, 83.3, 337.642, 349.43], [13, 31.535, 97.58, 354.48199999999997, 366.27], [13, 31.535, 101.14999999999999, 373.006, 384.794], [13, 31.535, 101.14999999999999, 390.688, 402.476], [13, 31.535, 92.225, 408.37, 420.15799999999996], [13, 31.535, 78.53999999999999, 426.05199999999996, 437.84], [13, 31.535, 92.225, 443.734, 455.522], [13, 31.535, 92.225, 460.574, 472.36199999999997], [13, 31.535, 83.3, 478.256, 490.044], [13, 31.535, 92.225, 495.938, 507.726], [13, 31.535, 83.3, 513.62, 525.408], [13, 31.535, 64.25999999999999, 531.302, 543.09], [13, 31.535, 73.78, 548.984, 560.7719999999999]]
2026-08-10 18:13:09,338 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=24, matched=24, pages=1, time=18.7s
2026-08-10 18:13:09,339 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:13:09,340 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:13:09,340 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[13]
2026-08-10 18:13:09,340 INFO     29 [qwen-vl-table] positions ： [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:13:09,501 INFO     29 [qwen-vl-table] page=13, rect=595x842, img=(1653x2339)
2026-08-10 18:13:09,501 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:13:09,502 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 513, \"bbox_end\": 523, \"encounter_dates\": [\"2026-03-07\"], \"department\": \"检验科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllll}\n报告时间: 2026-03-07\n\\hline\n中文名称 & 英文缩写 & 结果 & 单位 & 提示参考区间 & 检测方法 \\\\\n\\hline\n1. 乙型肝炎病毒表面抗原$\\ast\\ast\\star$ & HBsAg & $<0.05$ 阴性反应(-) & IU/ml & $<0.08$ & \\\\\n2. 丙型肝炎病毒抗体$\\ast\\ast\\star$ & HCV & 0.060 阴性反应(-) & & $<1$ & 化学发光法 \\\\\n3. 梅毒螺旋体抗体$\\ast\\ast\\star$ & antiTP & 0.0 阴性反应(-) & & 0.000-1.000 & 化学发光法 \\\\\n4. 人免疫缺陷病毒抗体$\\ast\\ast\\star$ & HIV Ab & 0.0 阴性反应(-) & & 0.000-1.000 & 化学发光法 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 18:13:12,656 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:13:12,657 INFO     29 [qwen-vl-table] page=13 LLM output (len=768):
{
  "report_date": "2026-03-07",
  "items": [
    {
      "name": "乙型肝炎病毒表面抗原",
      "item_code": "HBsAg",
      "value": "<0.05 阴性反应(-)",
      "unit": "IU/ml",
      "reference_range": "<0.08",
      "abnormal": false
    },
    {
      "name": "丙型肝炎病毒抗体",
      "item_code": "HCV",
      "value": "0.060 阴性反应(-)",
      "unit": null,
      "reference_range": "<1",
      "abnormal": false
    },
    {
      "name": "梅毒螺旋体抗体",
      "item_code": "antiTP",
      "value": "0.0 阴性反应(-)",
      "unit": null,
      "reference_range": "0.000-1.000",
      "abnormal": false
    },
    {
      "name": "人免疫缺陷病毒抗体",
      "item_code": "HIV Ab",
      "value": "0.0 阴性反应(-)",
      "unit": null,
      "reference_range": "0.000-1.000",
      "abnormal": false
    }
  ]
}
2026-08-10 18:13:12,657 INFO     29 [qwen-vl-table] coord grouping: {13: 4}
2026-08-10 18:13:12,659 INFO     29 [qwen-vl-table] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=543317, prompt_len=544
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
乙型肝炎病毒表面抗原、丙型肝炎病毒抗体、梅毒螺旋体抗体、人免疫缺陷病毒抗体

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
2026-08-10 18:13:14,778 INFO     29 [qwen-vl-table] coord API raw response (len=224):
```json
[
	{"text": "乙型肝炎病毒表面抗原", "bbox": [54, 162, 274, 175]},
	{"text": "丙型肝炎病毒抗体", "bbox": [54, 183, 240, 196]},
	{"text": "梅毒螺旋体抗体", "bbox": [54, 204, 223, 217]},
	{"text": "人免疫缺陷病毒抗体", "bbox": [54, 224, 256, 237]}
]
```
2026-08-10 18:13:14,778 INFO     29 [qwen-vl-table] coord API: raw_items=4, valid_items=4, elapsed=2.1s
2026-08-10 18:13:14,778 INFO     29 [qwen-vl-table] coord item[0]: text=乙型肝炎病毒表面抗原, bbox=[54, 162, 274, 175]
2026-08-10 18:13:14,778 INFO     29 [qwen-vl-table] coord item[1]: text=丙型肝炎病毒抗体, bbox=[54, 183, 240, 196]
2026-08-10 18:13:14,778 INFO     29 [qwen-vl-table] coord item[2]: text=梅毒螺旋体抗体, bbox=[54, 204, 223, 217]
2026-08-10 18:13:14,778 INFO     29 [qwen-vl-table] coord item[3]: text=人免疫缺陷病毒抗体, bbox=[54, 224, 256, 237]
2026-08-10 18:13:14,778 INFO     29 [qwen-vl-table] page=13 coord: matched 4/4, time=2.1s
2026-08-10 18:13:14,778 INFO     29 [qwen-vl-table] new_positions (4):
[[14, 32.129999999999995, 163.03, 136.404, 147.35], [14, 32.129999999999995, 142.79999999999998, 154.08599999999998, 165.03199999999998], [14, 32.129999999999995, 132.685, 171.768, 182.714], [14, 32.129999999999995, 152.32, 188.608, 199.554]]
2026-08-10 18:13:14,778 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=4, matched=4, pages=1, time=5.4s
2026-08-10 18:13:14,787 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 18:13:14,787 INFO     29 [Trace] task=a677452e | doc=07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf | Extractor:LabExam | outputs={"chunks": "7 items, types={'LabReport': 7}", "html": "", "json": "524 items", "markdown": "", "text": "", "name": "07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "7 items, types={'LabReport': 7}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 4, \"chunks_LabExam\": 7}"}
2026-08-10 18:13:14,787 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 18:13:14,787 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:13:14.787+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 85, "failed": 0, "current": {"a677452e94e611f1bd9827cf206dfa2d": {"id": "a677452e94e611f1bd9827cf206dfa2d", "doc_id": "a646f41e94e611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 11495294, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385378144, "task_type": "dataflow", "root_trace_id": "971de7c4c0604c27afceabc8ac295233", "root_traceparent": "00-971de7c4c0604c27afceabc8ac295233-de3f877b239fe0d8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:13:14,793 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:13:14,793 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 18:13:15,736 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:13:15,747 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 18:13:15,748 INFO     29 [Trace] task=a677452e | doc=07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "524 items", "markdown": "", "text": "", "name": "07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "7 items, types={'LabReport': 7}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 4, \"chunks_LabExam\": 7}"}
2026-08-10 18:13:15,748 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 18:13:15,756 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:13:15,757 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:13:15,757 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 18:13:15,757 INFO     29 [qwen-vl-text] positions(37): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:13:15,758 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [37]
2026-08-10 18:13:16,058 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 18:13:16,059 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1139
2026-08-10 18:13:16,059 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:13:16,059 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 4, \"bbox_end\": 40, \"encounter_dates\": [\"2026-03-02\"], \"department\": \"肿瘤内一科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "康复大学青岛中心医院\n门诊病历\n姓名：\n性别：男\n出生日期：19\n龄：53岁\n门诊号\n科别：肿瘤内一科门诊\n就诊时间：2026-03-02 17:35:26\n主诉：乙状结肠癌术后复发，会阴区疼痛\n现病史：患者2023-11-29于青医附院行“腹腔镜中转乙状结肠癌根治术+直肠部分切除术+预防性回\n肠末端造口术+左侧输尿管支架植入术”，2023-11-30术后病理示：“浸润深度：侵达浆膜，切缘：\n小肠切缘（-），结肠切缘（-），其他：另见绒毛状-管状腺瘤，伴多灶高级别上皮内瘤变（多枚，直\n径0.3-1.5cm）。淋巴结：肠周（4/20）淋巴结内见癌转移；送检小肠系膜（0/3）淋巴结内未见癌转\n移。病理学分期：pT3N2aMx。术后恢复可，2024-4-10发现“肝转移”，一线行“奥沙利铂+卡培他\n滨”化疗。2025-06-13肠镜：直肠术后，吻合口占位Ca？肠镜病理：“（直肠吻合口）腺癌（中分\n化）。2025-06-20 PET/CT：1.直肠癌术后治疗后，肝转移瘤术后，现示：直肠吻合口区高代谢占位，\n符合肿瘤复发（并与前列腺、双侧精囊腺关系密切，建议MRI检查），盆腔直肠周围、腹腔（右半肠系\n膜区）、腹膜后（双侧髂内血管走行区、骶前区）多发淋巴结转移，双肺转移（两处）；右肺上叶实\n性小结节，无明显异常FDG代谢增高，不除外转移。提示吻合口复发、双肺转移，病情进展，二线给予\n“伊立替康脂质体43mg d1、2+卡培他滨1.5g d1-14”化疗2周期。基因检测（2025-07-02）：1.KRAS\np.G12D突变丰度12.81%，NRAS突变阴性。2025-08-06行贝伐珠单抗400mg靶向治疗。2025-10-16复查\nCT：1.直肠术后，吻合区软组织影，考虑肿瘤复发，与前列腺分界不清，较2025.8.1范围略大；直肠\n周围、右腹膜后、骶前区多发淋巴结转移，部分较前略缩小，建议复查2.肝内多发转移瘤，较前进展\n3.肝囊肿。病情进展，患者既往接受过氟尿嘧啶类、奥沙利铂和伊立替康为基础的化疗，以及抗血管\n内皮生成因子治疗，病情进展，予呋喹替尼三线治疗。近期反复睾丸感染于泌尿外科行手术治疗，目\n前患者会阴区疼痛明显，NRS 3-5分，予止痛药物治疗，食欲差、乏力，夜间睡眠欠佳，外院2026-02-\n03血常规示血红蛋白80g/L。\n体格检查：双肺呼吸音粗，未闻及干湿啰音。。\n辅助检查结果：暂无\n初步诊断：结肠恶性肿瘤\n诊疗意见：1.(瑞乐芬)氨酚羟考酮片4盒间隔6小时1片口服×12天\n2.蒙脱石散5盒日三次3g口服×25天\n3.(易蒙停)盐酸洛哌丁胺胶囊10盒日三次2mg口服×25天\n门诊病历专用章\n3702080719401\n医生签名：梁华",
    "role": "user"
  }
]
2026-08-10 18:13:24,816 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:13:24,816 INFO     29 [qwen-vl-text] LLM output (len=1145):
{
  "encounter_date": "2026-03-02",
  "chief_complaint": "乙状结肠癌术后复发，会阴区疼痛",
  "present_illness": "患者2023-11-29于青医附院行“腹腔镜中转乙状结肠癌根治术+直肠部分切除术+预防性回肠末端造口术+左侧输尿管支架植入术”，2023-11-30术后病理示：“浸润深度：侵达浆膜，切缘：小肠切缘（-），结肠切缘（-），其他：另见绒毛状-管状腺瘤，伴多灶高级别上皮内瘤变（多枚，直径0.3-1.5cm）。淋巴结：肠周（4/20）淋巴结内见癌转移；送检小肠系膜（0/3）淋巴结内未见癌转移。病理学分期：pT3N2aMx。术后恢复可，2024-4-10发现“肝转移”，一线行“奥沙利铂+卡培他滨”化疗。2025-06-13肠镜：直肠术后，吻合口占位Ca？肠镜病理：“（直肠吻合口）腺癌（中分化）。2025-06-20 PET/CT：1.直肠癌术后治疗后，肝转移瘤术后，现示：直肠吻合口区高代谢占位，符合肿瘤复发（并与前列腺、双侧精囊腺关系密切，建议MRI检查），盆腔直肠周围、腹腔（右半肠系膜区）、腹膜后（双侧髂内血管走行区、骶前区）多发淋巴结转移，双肺转移（两处）；右肺上叶实性小结节，无明显异常FDG代谢增高，不除外转移。提示吻合口复发、双肺转移，病情进展，二线给予“伊立替康脂质体43mg d1、2+卡培他滨1.5g d1-14”化疗2周期。基因检测（2025-07-02）：1.KRAS p.G12D突变丰度12.81%，NRAS突变阴性。2025-08-06行贝伐珠单抗400mg靶向治疗。2025-10-16复查CT：1.直肠术后，吻合区软组织影，考虑肿瘤复发，与前列腺分界不清，较2025.8.1范围略大；直肠周围、右腹膜后、骶前区多发淋巴结转移，部分较前略缩小，建议复查2.肝内多发转移瘤，较前进展3.肝囊肿。病情进展，患者既往接受过氟尿嘧啶类、奥沙利铂和伊立替康为基础的化疗，以及抗血管内皮生成因子治疗，病情进展，予呋喹替尼三线治疗。近期反复睾丸感染于泌尿外科行手术治疗，目前患者会阴区疼痛明显，NRS 3-5分，予止痛药物治疗，食欲差、乏力，夜间睡眠欠佳，外院2026-02-03血常规示血红蛋白80g/L。",
  "past_history": null,
  "diagnosis": "结肠恶性肿瘤",
  "treatment_plan": [
    "(瑞乐芬)氨酚羟考酮片 4盒 间隔6小时1片 口服 ×12天",
    "蒙脱石散 5盒 日三次3g 口服 ×25天",
    "(易蒙停)盐酸洛哌丁胺胶囊 10盒 日三次2mg 口服 ×25天"
  ]
}
2026-08-10 18:13:24,816 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-03-02]
2026-08-10 18:13:24,820 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1806890, prompt_len=1863
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共37行）
["康复大学青岛中心医院", "门诊病历", "姓名：", "性别：男", "出生日期：19", "龄：53岁", "门诊号", "科别：肿瘤内一科门诊", "就诊时间：2026-03-02 17:35:26", "主诉：乙状结肠癌术后复发，会阴区疼痛", "现病史：患者2023-11-29于青医附院行“腹腔镜中转乙状结肠癌根治术+直肠部分切除术+预防性回", "肠末端造口术+左侧输尿管支架植入术”，2023-11-30术后病理示：“浸润深度：侵达浆膜，切缘：", "小肠切缘（-），结肠切缘（-），其他：另见绒毛状-管状腺瘤，伴多灶高级别上皮内瘤变（多枚，直", "径0.3-1.5cm）。淋巴结：肠周（4/20）淋巴结内见癌转移；送检小肠系膜（0/3）淋巴结内未见癌转", "移。病理学分期：pT3N2aMx。术后恢复可，2024-4-10发现“肝转移”，一线行“奥沙利铂+卡培他", "滨”化疗。2025-06-13肠镜：直肠术后，吻合口占位Ca？肠镜病理：“（直肠吻合口）腺癌（中分", "化）。2025-06-20 PET/CT：1.直肠癌术后治疗后，肝转移瘤术后，现示：直肠吻合口区高代谢占位，", "符合肿瘤复发（并与前列腺、双侧精囊腺关系密切，建议MRI检查），盆腔直肠周围、腹腔（右半肠系", "膜区）、腹膜后（双侧髂内血管走行区、骶前区）多发淋巴结转移，双肺转移（两处）；右肺上叶实", "性小结节，无明显异常FDG代谢增高，不除外转移。提示吻合口复发、双肺转移，病情进展，二线给予", "“伊立替康脂质体43mg d1、2+卡培他滨1.5g d1-14”化疗2周期。基因检测（2025-07-02）：1.KRAS", "p.G12D突变丰度12.81%，NRAS突变阴性。2025-08-06行贝伐珠单抗400mg靶向治疗。2025-10-16复查", "CT：1.直肠术后，吻合区软组织影，考虑肿瘤复发，与前列腺分界不清，较2025.8.1范围略大；直肠", "周围、右腹膜后、骶前区多发淋巴结转移，部分较前略缩小，建议复查2.肝内多发转移瘤，较前进展", "3.肝囊肿。病情进展，患者既往接受过氟尿嘧啶类、奥沙利铂和伊立替康为基础的化疗，以及抗血管", "内皮生成因子治疗，病情进展，予呋喹替尼三线治疗。近期反复睾丸感染于泌尿外科行手术治疗，目", "前患者会阴区疼痛明显，NRS 3-5分，予止痛药物治疗，食欲差、乏力，夜间睡眠欠佳，外院2026-02-", "03血常规示血红蛋白80g/L。", "体格检查：双肺呼吸音粗，未闻及干湿啰音。。", "辅助检查结果：暂无", "初步诊断：结肠恶性肿瘤", "诊疗意见：1.(瑞乐芬)氨酚羟考酮片4盒间隔6小时1片口服×12天", "2.蒙脱石散5盒日三次3g口服×25天", "3.(易蒙停)盐酸洛哌丁胺胶囊10盒日三次2mg口服×25天", "门诊病历专用章", "3702080719401", "医生签名：梁华"]

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
2026-08-10 18:13:39,804 INFO     29 [qwen-vl-text] coord API raw response (len=2781):
[
	{"text": "康复大学青岛中心医院", "bbox": [320, 19, 678, 46]},
	{"text": "门诊病历", "bbox": [433, 50, 567, 73]},
	{"text": "姓名：", "bbox": [67, 78, 115, 93]},
	{"text": "性别：男", "bbox": [216, 77, 297, 92]},
	{"text": "出生日期：19", "bbox": [317, 77, 440, 92]},
	{"text": "龄：53岁", "bbox": [591, 76, 666, 91]},
	{"text": "门诊号", "bbox": [719, 76, 777, 91]},
	{"text": "科别：肿瘤内一科门诊", "bbox": [67, 94, 262, 110]},
	{"text": "就诊时间：2026-03-02 17:35:26", "bbox": [67, 114, 350, 128]},
	{"text": "主诉：乙状结肠癌术后复发，会阴区疼痛", "bbox": [67, 136, 447, 151]},
	{"text": "现病史：患者2023-11-29于青医附院行“腹腔镜中转乙状结肠癌根治术+直肠部分切除术+预防性回", "bbox": [67, 158, 948, 174]},
	{"text": "肠末端造口术+左侧输尿管支架植入术”，2023-11-30术后病理示：“浸润深度：侵达浆膜，切缘：", "bbox": [67, 180, 935, 197]},
	{"text": "小肠切缘（-），结肠切缘（-），其他：另见绒毛状-管状腺瘤，伴多灶高级别上皮内瘤变（多枚，直", "bbox": [67, 203, 944, 220]},
	{"text": "径0.3-1.5cm）。淋巴结：肠周（4/20）淋巴结内见癌转移；送检小肠系膜（0/3）淋巴结内未见癌转", "bbox": [71, 226, 941, 243]},
	{"text": "移。病理学分期：pT3N2aMx。术后恢复可，2024-4-10发现“肝转移”，一线行“奥沙利铂+卡培他", "bbox": [71, 248, 941, 265]},
	{"text": "滨”化疗。2025-06-13肠镜：直肠术后，吻合口占位Ca？肠镜病理：“（直肠吻合口）腺癌（中分", "bbox": [67, 269, 941, 286]},
	{"text": "化）。2025-06-20 PET/CT：1.直肠癌术后治疗后，肝转移瘤术后，现示：直肠吻合口区高代谢占位，", "bbox": [67, 290, 932, 307]},
	{"text": "符合肿瘤复发（并与前列腺、双侧精囊腺关系密切，建议MRI检查），盆腔直肠周围、腹腔（右半肠系", "bbox": [67, 312, 943, 329]},
	{"text": "膜区）、腹膜后（双侧髂内血管走行区、骶前区）多发淋巴结转移，双肺转移（两处）；右肺上叶实", "bbox": [67, 334, 943, 351]},
	{"text": "性小结节，无明显异常FDG代谢增高，不除外转移。提示吻合口复发、双肺转移，病情进展，二线给予", "bbox": [67, 356, 943, 373]},
	{"text": "“伊立替康脂质体43mg d1、2+卡培他滨1.5g d1-14”化疗2周期。基因检测（2025-07-02）：1.KRAS", "bbox": [75, 377, 940, 394]},
	{"text": "p.G12D突变丰度12.81%，NRAS突变阴性。2025-08-06行贝伐珠单抗400mg靶向治疗。2025-10-16复查", "bbox": [67, 399, 943, 416]},
	{"text": "CT：1.直肠术后，吻合区软组织影，考虑肿瘤复发，与前列腺分界不清，较2025.8.1范围略大；直肠", "bbox": [67, 420, 943, 437]},
	{"text": "周围、右腹膜后、骶前区多发淋巴结转移，部分较前略缩小，建议复查2.肝内多发转移瘤，较前进展", "bbox": [71, 442, 940, 459]},
	{"text": "3.肝囊肿。病情进展，患者既往接受过氟尿嘧啶类、奥沙利铂和伊立替康为基础的化疗，以及抗血管", "bbox": [71, 464, 943, 481]},
	{"text": "内皮生成因子治疗，病情进展，予呋喹替尼三线治疗。近期反复睾丸感染于泌尿外科行手术治疗，目", "bbox": [71, 485, 943, 502]},
	{"text": "前患者会阴区疼痛明显，NRS 3-5分，予止痛药物治疗，食欲差、乏力，夜间睡眠欠佳，外院2026-02-", "bbox": [71, 506, 945, 523]},
	{"text": "03血常规示血红蛋白80g/L。", "bbox": [71, 527, 308, 543]},
	{"text": "体格检查：双肺呼吸音粗，未闻及干湿啰音。。", "bbox": [74, 548, 478, 564]},
	{"text": "辅助检查结果：暂无", "bbox": [74, 570, 253, 586]},
	{"text": "初步诊断：结肠恶性肿瘤", "bbox": [74, 592, 292, 608]},
	{"text": "诊疗意见：1.(瑞乐芬)氨酚羟考酮片4盒间隔6小时1片口服×12天", "bbox": [74, 613, 629, 631]},
	{"text": "2.蒙脱石散5盒日三次3g口服×25天", "bbox": [69, 637, 377, 654]},
	{"text": "3.(易蒙停)盐酸洛哌丁胺胶囊10盒日三次2mg口服×25天", "bbox": [69, 659, 548, 677]},
	{"text": "门诊病历专用章", "bbox": [470, 671, 597, 710]},
	{"text": "3702080719401", "bbox": [484, 705, 590, 723]},
	{"text": "医生签名：梁华", "bbox": [595, 694, 815, 716]},
	{"text": "门诊健康教育记录单", "bbox": [414, 716, 588, 734]}
]
2026-08-10 18:13:39,805 INFO     29 [qwen-vl-text] coord API: raw_items=38, valid_items=38, elapsed=15.0s
2026-08-10 18:13:39,805 INFO     29 [qwen-vl-text] coord item[0]: text=康复大学青岛中心医院, bbox=[320, 19, 678, 46]
2026-08-10 18:13:39,805 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[433, 50, 567, 73]
2026-08-10 18:13:39,805 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[67, 78, 115, 93]
2026-08-10 18:13:39,805 INFO     29 [qwen-vl-text] coord item[3]: text=性别：男, bbox=[216, 77, 297, 92]
2026-08-10 18:13:39,805 INFO     29 [qwen-vl-text] coord item[4]: text=出生日期：19, bbox=[317, 77, 440, 92]
2026-08-10 18:13:39,805 INFO     29 [qwen-vl-text] coord item[5]: text=龄：53岁, bbox=[591, 76, 666, 91]
2026-08-10 18:13:39,805 INFO     29 [qwen-vl-text] coord item[6]: text=门诊号, bbox=[719, 76, 777, 91]
2026-08-10 18:13:39,805 INFO     29 [qwen-vl-text] coord item[7]: text=科别：肿瘤内一科门诊, bbox=[67, 94, 262, 110]
2026-08-10 18:13:39,805 INFO     29 [qwen-vl-text] coord item[8]: text=就诊时间：2026-03-02 17:35:26, bbox=[67, 114, 350, 128]
2026-08-10 18:13:39,805 INFO     29 [qwen-vl-text] coord item[9]: text=主诉：乙状结肠癌术后复发，会阴区疼痛, bbox=[67, 136, 447, 151]
2026-08-10 18:13:39,805 INFO     29 [qwen-vl-text] coord item[10]: text=现病史：患者2023-11-29于青医附院行“腹腔镜中转乙状结肠癌根治术+直肠部分切除术+预防性回, bbox=[67, 158, 948, 174]
2026-08-10 18:13:39,805 INFO     29 [qwen-vl-text] coord item[11]: text=肠末端造口术+左侧输尿管支架植入术”，2023-11-30术后病理示：“浸润深度：侵达浆膜，切缘：, bbox=[67, 180, 935, 197]
2026-08-10 18:13:39,805 INFO     29 [qwen-vl-text] coord item[12]: text=小肠切缘（-），结肠切缘（-），其他：另见绒毛状-管状腺瘤，伴多灶高级别上皮内瘤变（多枚，直, bbox=[67, 203, 944, 220]
2026-08-10 18:13:39,805 INFO     29 [qwen-vl-text] coord item[13]: text=径0.3-1.5cm）。淋巴结：肠周（4/20）淋巴结内见癌转移；送检小肠系膜（0/3）淋巴结内未见癌转, bbox=[71, 226, 941, 243]
2026-08-10 18:13:39,805 INFO     29 [qwen-vl-text] coord item[14]: text=移。病理学分期：pT3N2aMx。术后恢复可，2024-4-10发现“肝转移”，一线行“奥沙利铂+卡培他, bbox=[71, 248, 941, 265]
2026-08-10 18:13:39,805 INFO     29 [qwen-vl-text] coord item[15]: text=滨”化疗。2025-06-13肠镜：直肠术后，吻合口占位Ca？肠镜病理：“（直肠吻合口）腺癌（中分, bbox=[67, 269, 941, 286]
2026-08-10 18:13:39,806 INFO     29 [qwen-vl-text] coord item[16]: text=化）。2025-06-20 PET/CT：1.直肠癌术后治疗后，肝转移瘤术后，现示：直肠吻合口区高代谢占位，, bbox=[67, 290, 932, 307]
2026-08-10 18:13:39,806 INFO     29 [qwen-vl-text] coord item[17]: text=符合肿瘤复发（并与前列腺、双侧精囊腺关系密切，建议MRI检查），盆腔直肠周围、腹腔（右半肠系, bbox=[67, 312, 943, 329]
2026-08-10 18:13:39,806 INFO     29 [qwen-vl-text] coord item[18]: text=膜区）、腹膜后（双侧髂内血管走行区、骶前区）多发淋巴结转移，双肺转移（两处）；右肺上叶实, bbox=[67, 334, 943, 351]
2026-08-10 18:13:39,806 INFO     29 [qwen-vl-text] coord item[19]: text=性小结节，无明显异常FDG代谢增高，不除外转移。提示吻合口复发、双肺转移，病情进展，二线给予, bbox=[67, 356, 943, 373]
2026-08-10 18:13:39,806 INFO     29 [qwen-vl-text] coord item[20]: text=“伊立替康脂质体43mg d1、2+卡培他滨1.5g d1-14”化疗2周期。基因检测（2025-07-02）：1.KRAS, bbox=[75, 377, 940, 394]
2026-08-10 18:13:39,806 INFO     29 [qwen-vl-text] coord item[21]: text=p.G12D突变丰度12.81%，NRAS突变阴性。2025-08-06行贝伐珠单抗400mg靶向治疗。2025-10-16复查, bbox=[67, 399, 943, 416]
2026-08-10 18:13:39,806 INFO     29 [qwen-vl-text] coord item[22]: text=CT：1.直肠术后，吻合区软组织影，考虑肿瘤复发，与前列腺分界不清，较2025.8.1范围略大；直肠, bbox=[67, 420, 943, 437]
2026-08-10 18:13:39,806 INFO     29 [qwen-vl-text] coord item[23]: text=周围、右腹膜后、骶前区多发淋巴结转移，部分较前略缩小，建议复查2.肝内多发转移瘤，较前进展, bbox=[71, 442, 940, 459]
2026-08-10 18:13:39,806 INFO     29 [qwen-vl-text] coord item[24]: text=3.肝囊肿。病情进展，患者既往接受过氟尿嘧啶类、奥沙利铂和伊立替康为基础的化疗，以及抗血管, bbox=[71, 464, 943, 481]
2026-08-10 18:13:39,806 INFO     29 [qwen-vl-text] coord item[25]: text=内皮生成因子治疗，病情进展，予呋喹替尼三线治疗。近期反复睾丸感染于泌尿外科行手术治疗，目, bbox=[71, 485, 943, 502]
2026-08-10 18:13:39,806 INFO     29 [qwen-vl-text] coord item[26]: text=前患者会阴区疼痛明显，NRS 3-5分，予止痛药物治疗，食欲差、乏力，夜间睡眠欠佳，外院2026-02-, bbox=[71, 506, 945, 523]
2026-08-10 18:13:39,806 INFO     29 [qwen-vl-text] coord item[27]: text=03血常规示血红蛋白80g/L。, bbox=[71, 527, 308, 543]
2026-08-10 18:13:39,806 INFO     29 [qwen-vl-text] coord item[28]: text=体格检查：双肺呼吸音粗，未闻及干湿啰音。。, bbox=[74, 548, 478, 564]
2026-08-10 18:13:39,806 INFO     29 [qwen-vl-text] coord item[29]: text=辅助检查结果：暂无, bbox=[74, 570, 253, 586]
2026-08-10 18:13:39,806 INFO     29 [qwen-vl-text] coord item[30]: text=初步诊断：结肠恶性肿瘤, bbox=[74, 592, 292, 608]
2026-08-10 18:13:39,806 INFO     29 [qwen-vl-text] coord item[31]: text=诊疗意见：1.(瑞乐芬)氨酚羟考酮片4盒间隔6小时1片口服×12天, bbox=[74, 613, 629, 631]
2026-08-10 18:13:39,806 INFO     29 [qwen-vl-text] coord item[32]: text=2.蒙脱石散5盒日三次3g口服×25天, bbox=[69, 637, 377, 654]
2026-08-10 18:13:39,806 INFO     29 [qwen-vl-text] coord item[33]: text=3.(易蒙停)盐酸洛哌丁胺胶囊10盒日三次2mg口服×25天, bbox=[69, 659, 548, 677]
2026-08-10 18:13:39,806 INFO     29 [qwen-vl-text] coord item[34]: text=门诊病历专用章, bbox=[470, 671, 597, 710]
2026-08-10 18:13:39,806 INFO     29 [qwen-vl-text] coord item[35]: text=3702080719401, bbox=[484, 705, 590, 723]
2026-08-10 18:13:39,806 INFO     29 [qwen-vl-text] coord item[36]: text=医生签名：梁华, bbox=[595, 694, 815, 716]
2026-08-10 18:13:39,807 INFO     29 [qwen-vl-text] coord item[37]: text=门诊健康教育记录单, bbox=[414, 716, 588, 734]
2026-08-10 18:13:39,808 INFO     29 [qwen-vl-text] page=1 — 37/37 coords, api_time=15.0s
2026-08-10 18:13:39,808 INFO     29 [qwen-vl-text] new_positions (37):
[[1, 190.39999999999998, 403.40999999999997, 15.998, 38.732], [1, 257.635, 337.365, 42.1, 61.466], [1, 39.864999999999995, 68.425, 65.676, 78.306], [1, 128.51999999999998, 176.715, 64.834, 77.464], [1, 188.61499999999998, 261.8, 64.834, 77.464], [1, 351.645, 396.27, 63.992, 76.622], [1, 427.805, 462.315, 63.992, 76.622], [1, 39.864999999999995, 155.89, 79.148, 92.61999999999999], [1, 39.864999999999995, 208.25, 95.988, 107.776], [1, 39.864999999999995, 265.965, 114.512, 127.142], [1, 39.864999999999995, 564.06, 133.036, 146.50799999999998], [1, 39.864999999999995, 556.3249999999999, 151.56, 165.874], [1, 39.864999999999995, 561.68, 170.926, 185.23999999999998], [1, 42.245, 559.895, 190.292, 204.606], [1, 42.245, 559.895, 208.816, 223.13], [1, 39.864999999999995, 559.895, 226.498, 240.81199999999998], [1, 39.864999999999995, 554.54, 244.17999999999998, 258.49399999999997], [1, 39.864999999999995, 561.0849999999999, 262.704, 277.018], [1, 39.864999999999995, 561.0849999999999, 281.228, 295.542], [1, 39.864999999999995, 561.0849999999999, 299.752, 314.066], [1, 44.625, 559.3, 317.43399999999997, 331.748], [1, 39.864999999999995, 561.0849999999999, 335.95799999999997, 350.272], [1, 39.864999999999995, 561.0849999999999, 353.64, 367.954], [1, 42.245, 559.3, 372.164, 386.478], [1, 42.245, 561.0849999999999, 390.688, 405.002], [1, 42.245, 561.0849999999999, 408.37, 422.68399999999997], [1, 42.245, 562.275, 426.05199999999996, 440.366], [1, 42.245, 183.26, 443.734, 457.20599999999996], [1, 44.03, 284.40999999999997, 461.416, 474.888], [1, 44.03, 150.535, 479.94, 493.412], [1, 44.03, 173.73999999999998, 498.464, 511.936], [1, 44.03, 374.255, 516.146, 531.302], [1, 41.055, 224.315, 536.3539999999999, 550.668], [1, 41.055, 326.06, 554.8779999999999, 570.034], [1, 279.65, 355.215, 564.982, 597.8199999999999], [1, 287.97999999999996, 351.05, 593.61, 608.766], [1, 354.025, 484.92499999999995, 584.348, 602.872]]
2026-08-10 18:13:39,808 INFO     29 [qwen-vl-text] ═══ DONE ═══ 37 positions, pages=1, time=24.1s
2026-08-10 18:13:39,818 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 18:13:39,819 INFO     29 [Trace] task=a677452e | doc=07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "524 items", "markdown": "", "text": "", "name": "07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "7 items, types={'LabReport': 7}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 4, \"chunks_LabExam\": 7}"}
2026-08-10 18:13:39,819 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 18:13:39,824 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:13:39,824 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 18:13:40,923 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:13:40,930 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 18:13:40,931 INFO     29 [Trace] task=a677452e | doc=07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "524 items", "markdown": "", "text": "", "name": "07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "7 items, types={'LabReport': 7}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 4, \"chunks_LabExam\": 7}"}
2026-08-10 18:13:40,931 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 18:13:40,937 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:13:40,937 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 18:13:41,384 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:13:41,389 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 18:13:41,389 INFO     29 [Trace] task=a677452e | doc=07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "524 items", "markdown": "", "text": "", "name": "07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "7 items, types={'LabReport': 7}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 4, \"chunks_LabExam\": 7}"}
2026-08-10 18:13:41,389 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 18:13:41,394 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:13:41,394 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 18:13:41,836 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:13:41,841 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 18:13:41,841 INFO     29 [Trace] task=a677452e | doc=07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "524 items", "markdown": "", "text": "", "name": "07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "7 items, types={'LabReport': 7}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 4, \"chunks_LabExam\": 7}"}
2026-08-10 18:13:41,841 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 18:13:41,845 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:13:41,845 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 18:13:42,339 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:13:42,344 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 18:13:42,344 INFO     29 [Trace] task=a677452e | doc=07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "524 items", "markdown": "", "text": "", "name": "07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "7 items, types={'LabReport': 7}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 4, \"chunks_LabExam\": 7}"}
2026-08-10 18:13:42,344 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 18:13:42,349 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:13:42,350 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:13:42,350 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 18:13:42,350 INFO     29 [qwen-vl-text] positions(43): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:13:42,350 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [43]
2026-08-10 18:13:42,554 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 18:13:42,555 INFO     29 [qwen-vl-text] LLM extraction start, text_len=931
2026-08-10 18:13:42,555 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:13:42,556 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 52, \"bbox_end\": 94, \"encounter_dates\": [\"2024-04-19\"], \"department\": \"病理科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "青岛大学附属医院\n市南院区\n病理检查诊断报告\n病理号\n姓名\n性别：男\n年龄：51岁\n送检单位：青岛大学附属医院市 送检科室：胃肠外科\n收到日期：2024-04-11\n送检医生：赵蕊蕊\n病区：胃肠外科病区\n住院号：\n送检材料：肝肿物，造口端回肠，直肠息\n临床诊断：1.乙状结肠恶性肿瘤,2.回肠造口状态\n大体检查:\n肝肿物：肝组织一件，大小4*3*2cm，剖开，距离肝断端0.4cm见一灰白肿物，范围\n0.5*0.4cm，质软，紧邻肝被膜0.5cm，其余肝组织灰红灰黄质软。\n造口组织一件，大小6.5*5*3cm，皮肤范围4*2.5cm，连接肠管两段，长分别为\n3cm、3.5cm，直径分别为1.5cm、1.7cm，肠粘膜灰白灰红。\n直肠息肉1：息肉样物一枚，大小2*2*1cm，未见明显蒂部及基底，于疑似基底处涂\n墨。\n直肠息肉2：息肉样物一枚，大小2*1*0.8cm，未见明显蒂部。\n直肠息肉3：息肉样物三枚，大小1.5*1*0.6cm，中者大小1*1*0.5cm，小者大小\n0.7*0.6*0.4cm，未见明显蒂部及基底。\n病理诊断:\n1、（肝肿物）肝组织内见中分化腺癌浸润，结合形态、病史及免疫组化结果，符合\n转移性肠腺癌。\n免疫组化结果：CK7（-），CK20（灶+），Arginase-1（-），CDX-2（+），SATB2\n（+），Ki-67（+，约80%）。\n2、（造口端回肠）皮肤及肠粘膜组织呈慢性活动性炎伴糜烂，复鳞上皮乳头状增\n生，间质纤维组织增生，血管扩张、充血及出血，部分区域肌层排列紊乱，符合造口\n改变。\n3、（直肠息肉1、2、3）均为绒毛状-管状腺瘤，部分腺体呈高级别上皮内瘤变，局\n灶癌变-中分化腺癌。\n免疫组化结果：CK-Desmin示未见确切粘膜肌。\n报告医生：张丽\n初诊医生：张晶晶\n报告日期：2024-04-19\n注：1.病理诊断分级注解：明确及基本明确的诊断，无任何修饰语；如有“考虑为”、“疑为”、“符合”、\n“不除外”及“可能性大”等修饰语，提示诊断具有不同程度的不确定性，请结合临床相关检查综合判断。\n2.如本诊断与临床表现及相关检查不符，请临床医生及时与病理科联系后再行处置。\n3.此报告以纸质版为准。\n审核专用章",
    "role": "user"
  }
]
2026-08-10 18:13:46,906 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:13:46.904+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 85, "failed": 0, "current": {"a677452e94e611f1bd9827cf206dfa2d": {"id": "a677452e94e611f1bd9827cf206dfa2d", "doc_id": "a646f41e94e611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 11495294, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385378144, "task_type": "dataflow", "root_trace_id": "971de7c4c0604c27afceabc8ac295233", "root_traceparent": "00-971de7c4c0604c27afceabc8ac295233-de3f877b239fe0d8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:13:47,450 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:13:47,450 INFO     29 [qwen-vl-text] LLM output (len=916):
{
  "exam_date": "2024-04-11",
  "report_date": "2024-04-19",
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "肝肿物，造口端回肠，直肠息肉",
  "patient_name": null,
  "patient_gender": "男",
  "department": "胃肠外科",
  "bed_number": null,
  "findings": "大体检查:\n肝肿物：肝组织一件，大小4*3*2cm，剖开，距离肝断端0.4cm见一灰白肿物，范围0.5*0.4cm，质软，紧邻肝被膜0.5cm，其余肝组织灰红灰黄质软。\n造口组织一件，大小6.5*5*3cm，皮肤范围4*2.5cm，连接肠管两段，长分别为3cm、3.5cm，直径分别为1.5cm、1.7cm，肠粘膜灰白灰红。\n直肠息肉1：息肉样物一枚，大小2*2*1cm，未见明显蒂部及基底，于疑似基底处涂墨。\n直肠息肉2：息肉样物一枚，大小2*1*0.8cm，未见明显蒂部。\n直肠息肉3：息肉样物三枚，大小1.5*1*0.6cm，中者大小1*1*0.5cm，小者大小0.7*0.6*0.4cm，未见明显蒂部及基底。",
  "conclusion": "病理诊断:\n1、（肝肿物）肝组织内见中分化腺癌浸润，结合形态、病史及免疫组化结果，符合转移性肠腺癌。\n免疫组化结果：CK7（-），CK20（灶+），Arginase-1（-），CDX-2（+），SATB2（+），Ki-67（+，约80%）。\n2、（造口端回肠）皮肤及肠粘膜组织呈慢性活动性炎伴糜烂，复鳞上皮乳头状增生，间质纤维组织增生，血管扩张、充血及出血，部分区域肌层排列紊乱，符合造口改变。\n3、（直肠息肉1、2、3）均为绒毛状-管状腺瘤，部分腺体呈高级别上皮内瘤变，局灶癌变-中分化腺癌。\n免疫组化结果：CK-Desmin示未见确切粘膜肌。",
  "physician": "张丽",
  "reviewer": "张晶晶"
}
2026-08-10 18:13:47,452 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1172680, prompt_len=1673
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共43行）
["青岛大学附属医院", "市南院区", "病理检查诊断报告", "病理号", "姓名", "性别：男", "年龄：51岁", "送检单位：青岛大学附属医院市 送检科室：胃肠外科", "收到日期：2024-04-11", "送检医生：赵蕊蕊", "病区：胃肠外科病区", "住院号：", "送检材料：肝肿物，造口端回肠，直肠息", "临床诊断：1.乙状结肠恶性肿瘤,2.回肠造口状态", "大体检查:", "肝肿物：肝组织一件，大小4*3*2cm，剖开，距离肝断端0.4cm见一灰白肿物，范围", "0.5*0.4cm，质软，紧邻肝被膜0.5cm，其余肝组织灰红灰黄质软。", "造口组织一件，大小6.5*5*3cm，皮肤范围4*2.5cm，连接肠管两段，长分别为", "3cm、3.5cm，直径分别为1.5cm、1.7cm，肠粘膜灰白灰红。", "直肠息肉1：息肉样物一枚，大小2*2*1cm，未见明显蒂部及基底，于疑似基底处涂", "墨。", "直肠息肉2：息肉样物一枚，大小2*1*0.8cm，未见明显蒂部。", "直肠息肉3：息肉样物三枚，大小1.5*1*0.6cm，中者大小1*1*0.5cm，小者大小", "0.7*0.6*0.4cm，未见明显蒂部及基底。", "病理诊断:", "1、（肝肿物）肝组织内见中分化腺癌浸润，结合形态、病史及免疫组化结果，符合", "转移性肠腺癌。", "免疫组化结果：CK7（-），CK20（灶+），Arginase-1（-），CDX-2（+），SATB2", "（+），Ki-67（+，约80%）。", "2、（造口端回肠）皮肤及肠粘膜组织呈慢性活动性炎伴糜烂，复鳞上皮乳头状增", "生，间质纤维组织增生，血管扩张、充血及出血，部分区域肌层排列紊乱，符合造口", "改变。", "3、（直肠息肉1、2、3）均为绒毛状-管状腺瘤，部分腺体呈高级别上皮内瘤变，局", "灶癌变-中分化腺癌。", "免疫组化结果：CK-Desmin示未见确切粘膜肌。", "报告医生：张丽", "初诊医生：张晶晶", "报告日期：2024-04-19", "注：1.病理诊断分级注解：明确及基本明确的诊断，无任何修饰语；如有“考虑为”、“疑为”、“符合”、", "“不除外”及“可能性大”等修饰语，提示诊断具有不同程度的不确定性，请结合临床相关检查综合判断。", "2.如本诊断与临床表现及相关检查不符，请临床医生及时与病理科联系后再行处置。", "3.此报告以纸质版为准。", "审核专用章"]

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
2026-08-10 18:14:04,469 INFO     29 [qwen-vl-text] coord API raw response (len=2823):
[
	{"text": "青岛大学附属医院", "bbox": [363, 65, 647, 94]},
	{"text": "市南院区", "bbox": [735, 83, 815, 100]},
	{"text": "病理检查诊断报告", "bbox": [387, 101, 622, 124]},
	{"text": "病理号", "bbox": [156, 134, 219, 151]},
	{"text": "姓名", "bbox": [157, 162, 226, 177]},
	{"text": "性别：男", "bbox": [409, 159, 508, 175]},
	{"text": "年龄：51岁", "bbox": [645, 160, 768, 175]},
	{"text": "送检单位：青岛大学附属医院市 送检科室：胃肠外科", "bbox": [157, 187, 559, 202]},
	{"text": "收到日期：2024-04-11", "bbox": [645, 187, 820, 201]},
	{"text": "送检医生：赵蕊蕊", "bbox": [157, 217, 296, 232]},
	{"text": "病区：胃肠外科病区", "bbox": [407, 216, 593, 231]},
	{"text": "住院号：", "bbox": [645, 216, 722, 231]},
	{"text": "送检材料：肝肿物，造口端回肠，直肠息", "bbox": [157, 240, 470, 254]},
	{"text": "临床诊断：1.乙状结肠恶性肿瘤,2.回肠造口状态", "bbox": [488, 240, 863, 254]},
	{"text": "大体检查:", "bbox": [157, 264, 243, 280]},
	{"text": "肝肿物：肝组织一件，大小4*3*2cm，剖开，距离肝断端0.4cm见一灰白肿物，范围", "bbox": [172, 280, 801, 295]},
	{"text": "0.5*0.4cm，质软，紧邻肝被膜0.5cm，其余肝组织灰红灰黄质软。", "bbox": [172, 295, 669, 310]},
	{"text": "造口组织一件，大小6.5*5*3cm，皮肤范围4*2.5cm，连接肠管两段，长分别为", "bbox": [172, 310, 765, 325]},
	{"text": "3cm、3.5cm，直径分别为1.5cm、1.7cm，肠粘膜灰白灰红。", "bbox": [172, 325, 617, 340]},
	{"text": "直肠息肉1：息肉样物一枚，大小2*2*1cm，未见明显蒂部及基底，于疑似基底处涂", "bbox": [172, 340, 801, 355]},
	{"text": "墨。", "bbox": [172, 355, 198, 369]},
	{"text": "直肠息肉2：息肉样物一枚，大小2*1*0.8cm，未见明显蒂部。", "bbox": [172, 370, 633, 385]},
	{"text": "直肠息肉3：息肉样物三枚，大小1.5*1*0.6cm，中者大小1*1*0.5cm，小者大小", "bbox": [172, 385, 773, 399]},
	{"text": "0.7*0.6*0.4cm，未见明显蒂部及基底。", "bbox": [172, 400, 470, 414]},
	{"text": "病理诊断:", "bbox": [157, 443, 243, 459]},
	{"text": "1、（肝肿物）肝组织内见中分化腺癌浸润，结合形态、病史及免疫组化结果，符合", "bbox": [157, 460, 794, 475]},
	{"text": "转移性肠腺癌。", "bbox": [157, 475, 273, 489]},
	{"text": "免疫组化结果：CK7（-），CK20（灶+），Arginase-1（-），CDX-2（+），SATB2", "bbox": [157, 490, 777, 504]},
	{"text": "（+），Ki-67（+，约80%）。", "bbox": [157, 504, 379, 519]},
	{"text": "2、（造口端回肠）皮肤及肠粘膜组织呈慢性活动性炎伴糜烂，复鳞上皮乳头状增", "bbox": [157, 519, 776, 533]},
	{"text": "生，间质纤维组织增生，血管扩张、充血及出血，部分区域肌层排列紊乱，符合造口", "bbox": [157, 533, 801, 548]},
	{"text": "改变。", "bbox": [157, 548, 202, 562]},
	{"text": "3、（直肠息肉1、2、3）均为绒毛状-管状腺瘤，部分腺体呈高级别上皮内瘤变，局", "bbox": [157, 563, 794, 577]},
	{"text": "灶癌变-中分化腺癌。", "bbox": [157, 577, 317, 592]},
	{"text": "免疫组化结果：CK-Desmin示未见确切粘膜肌。", "bbox": [157, 592, 505, 607]},
	{"text": "报告医生：张丽", "bbox": [143, 809, 310, 827]},
	{"text": "初诊医生：张晶晶", "bbox": [637, 812, 778, 828]},
	{"text": "报告日期：2024-04-19", "bbox": [637, 839, 818, 854]},
	{"text": "注：1.病理诊断分级注解：明确及基本明确的诊断，无任何修饰语；如有“考虑为”、“疑为”、“符合”、", "bbox": [140, 856, 860, 872]},
	{"text": "“不除外”及“可能性大”等修饰语，提示诊断具有不同程度的不确定性，请结合临床相关检查综合判断。", "bbox": [143, 870, 847, 887]},
	{"text": "2.如本诊断与临床表现及相关检查不符，请临床医生及时与病理科联系后再行处置。", "bbox": [176, 888, 732, 904]},
	{"text": "3.此报告以纸质版为准。", "bbox": [176, 903, 333, 917]},
	{"text": "审核专用章", "bbox": [762, 702, 857, 739]}
]
2026-08-10 18:14:04,469 INFO     29 [qwen-vl-text] coord API: raw_items=43, valid_items=43, elapsed=17.0s
2026-08-10 18:14:04,469 INFO     29 [qwen-vl-text] coord item[0]: text=青岛大学附属医院, bbox=[363, 65, 647, 94]
2026-08-10 18:14:04,469 INFO     29 [qwen-vl-text] coord item[1]: text=市南院区, bbox=[735, 83, 815, 100]
2026-08-10 18:14:04,469 INFO     29 [qwen-vl-text] coord item[2]: text=病理检查诊断报告, bbox=[387, 101, 622, 124]
2026-08-10 18:14:04,469 INFO     29 [qwen-vl-text] coord item[3]: text=病理号, bbox=[156, 134, 219, 151]
2026-08-10 18:14:04,469 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[157, 162, 226, 177]
2026-08-10 18:14:04,469 INFO     29 [qwen-vl-text] coord item[5]: text=性别：男, bbox=[409, 159, 508, 175]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[6]: text=年龄：51岁, bbox=[645, 160, 768, 175]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[7]: text=送检单位：青岛大学附属医院市 送检科室：胃肠外科, bbox=[157, 187, 559, 202]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[8]: text=收到日期：2024-04-11, bbox=[645, 187, 820, 201]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[9]: text=送检医生：赵蕊蕊, bbox=[157, 217, 296, 232]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[10]: text=病区：胃肠外科病区, bbox=[407, 216, 593, 231]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[11]: text=住院号：, bbox=[645, 216, 722, 231]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[12]: text=送检材料：肝肿物，造口端回肠，直肠息, bbox=[157, 240, 470, 254]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[13]: text=临床诊断：1.乙状结肠恶性肿瘤,2.回肠造口状态, bbox=[488, 240, 863, 254]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[14]: text=大体检查:, bbox=[157, 264, 243, 280]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[15]: text=肝肿物：肝组织一件，大小4*3*2cm，剖开，距离肝断端0.4cm见一灰白肿物，范围, bbox=[172, 280, 801, 295]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[16]: text=0.5*0.4cm，质软，紧邻肝被膜0.5cm，其余肝组织灰红灰黄质软。, bbox=[172, 295, 669, 310]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[17]: text=造口组织一件，大小6.5*5*3cm，皮肤范围4*2.5cm，连接肠管两段，长分别为, bbox=[172, 310, 765, 325]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[18]: text=3cm、3.5cm，直径分别为1.5cm、1.7cm，肠粘膜灰白灰红。, bbox=[172, 325, 617, 340]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[19]: text=直肠息肉1：息肉样物一枚，大小2*2*1cm，未见明显蒂部及基底，于疑似基底处涂, bbox=[172, 340, 801, 355]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[20]: text=墨。, bbox=[172, 355, 198, 369]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[21]: text=直肠息肉2：息肉样物一枚，大小2*1*0.8cm，未见明显蒂部。, bbox=[172, 370, 633, 385]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[22]: text=直肠息肉3：息肉样物三枚，大小1.5*1*0.6cm，中者大小1*1*0.5cm，小者大小, bbox=[172, 385, 773, 399]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[23]: text=0.7*0.6*0.4cm，未见明显蒂部及基底。, bbox=[172, 400, 470, 414]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[24]: text=病理诊断:, bbox=[157, 443, 243, 459]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[25]: text=1、（肝肿物）肝组织内见中分化腺癌浸润，结合形态、病史及免疫组化结果，符合, bbox=[157, 460, 794, 475]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[26]: text=转移性肠腺癌。, bbox=[157, 475, 273, 489]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[27]: text=免疫组化结果：CK7（-），CK20（灶+），Arginase-1（-），CDX-2（+），SATB2, bbox=[157, 490, 777, 504]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[28]: text=（+），Ki-67（+，约80%）。, bbox=[157, 504, 379, 519]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[29]: text=2、（造口端回肠）皮肤及肠粘膜组织呈慢性活动性炎伴糜烂，复鳞上皮乳头状增, bbox=[157, 519, 776, 533]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[30]: text=生，间质纤维组织增生，血管扩张、充血及出血，部分区域肌层排列紊乱，符合造口, bbox=[157, 533, 801, 548]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[31]: text=改变。, bbox=[157, 548, 202, 562]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[32]: text=3、（直肠息肉1、2、3）均为绒毛状-管状腺瘤，部分腺体呈高级别上皮内瘤变，局, bbox=[157, 563, 794, 577]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[33]: text=灶癌变-中分化腺癌。, bbox=[157, 577, 317, 592]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[34]: text=免疫组化结果：CK-Desmin示未见确切粘膜肌。, bbox=[157, 592, 505, 607]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[35]: text=报告医生：张丽, bbox=[143, 809, 310, 827]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[36]: text=初诊医生：张晶晶, bbox=[637, 812, 778, 828]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[37]: text=报告日期：2024-04-19, bbox=[637, 839, 818, 854]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[38]: text=注：1.病理诊断分级注解：明确及基本明确的诊断，无任何修饰语；如有“考虑为”、“疑为”、“符合”、, bbox=[140, 856, 860, 872]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[39]: text=“不除外”及“可能性大”等修饰语，提示诊断具有不同程度的不确定性，请结合临床相关检查综合判断。, bbox=[143, 870, 847, 887]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[40]: text=2.如本诊断与临床表现及相关检查不符，请临床医生及时与病理科联系后再行处置。, bbox=[176, 888, 732, 904]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[41]: text=3.此报告以纸质版为准。, bbox=[176, 903, 333, 917]
2026-08-10 18:14:04,470 INFO     29 [qwen-vl-text] coord item[42]: text=审核专用章, bbox=[762, 702, 857, 739]
2026-08-10 18:14:04,471 INFO     29 [qwen-vl-text] page=2 — 43/43 coords, api_time=17.0s
2026-08-10 18:14:04,471 INFO     29 [qwen-vl-text] new_positions (43):
[[2, 215.98499999999999, 384.965, 54.73, 79.148], [2, 437.325, 484.92499999999995, 69.886, 84.2], [2, 230.265, 370.09, 85.042, 104.408], [2, 92.82, 130.305, 112.828, 127.142], [2, 93.41499999999999, 134.47, 136.404, 149.034], [2, 243.355, 302.26, 133.878, 147.35], [2, 383.775, 456.96, 134.72, 147.35], [2, 93.41499999999999, 332.60499999999996, 157.454, 170.084], [2, 383.775, 487.9, 157.454, 169.242], [2, 93.41499999999999, 176.12, 182.714, 195.344], [2, 242.165, 352.835, 181.87199999999999, 194.50199999999998], [2, 383.775, 429.59, 181.87199999999999, 194.50199999999998], [2, 93.41499999999999, 279.65, 202.07999999999998, 213.868], [2, 290.36, 513.485, 202.07999999999998, 213.868], [2, 93.41499999999999, 144.58499999999998, 222.28799999999998, 235.76], [2, 102.33999999999999, 476.59499999999997, 235.76, 248.39], [2, 102.33999999999999, 398.055, 248.39, 261.02], [2, 102.33999999999999, 455.17499999999995, 261.02, 273.65], [2, 102.33999999999999, 367.115, 273.65, 286.28], [2, 102.33999999999999, 476.59499999999997, 286.28, 298.90999999999997], [2, 102.33999999999999, 117.80999999999999, 298.90999999999997, 310.698], [2, 102.33999999999999, 376.635, 311.53999999999996, 324.17], [2, 102.33999999999999, 459.935, 324.17, 335.95799999999997], [2, 102.33999999999999, 279.65, 336.8, 348.58799999999997], [2, 93.41499999999999, 144.58499999999998, 373.006, 386.478], [2, 93.41499999999999, 472.43, 387.32, 399.95], [2, 93.41499999999999, 162.435, 399.95, 411.738], [2, 93.41499999999999, 462.315, 412.58, 424.368], [2, 93.41499999999999, 225.505, 424.368, 436.998], [2, 93.41499999999999, 461.71999999999997, 436.998, 448.786], [2, 93.41499999999999, 476.59499999999997, 448.786, 461.416], [2, 93.41499999999999, 120.19, 461.416, 473.204], [2, 93.41499999999999, 472.43, 474.046, 485.834], [2, 93.41499999999999, 188.61499999999998, 485.834, 498.464], [2, 93.41499999999999, 300.47499999999997, 498.464, 511.094], [2, 85.085, 184.45, 681.178, 696.334], [2, 379.015, 462.90999999999997, 683.704, 697.1759999999999], [2, 379.015, 486.71, 706.438, 719.068], [2, 83.3, 511.7, 720.752, 734.2239999999999], [2, 85.085, 503.965, 732.54, 746.8539999999999], [2, 104.72, 435.53999999999996, 747.696, 761.168], [2, 104.72, 198.135, 760.326, 772.1139999999999], [2, 453.39, 509.91499999999996, 591.084, 622.2379999999999]]
2026-08-10 18:14:04,471 INFO     29 [qwen-vl-text] ═══ DONE ═══ 43 positions, pages=1, time=22.1s
2026-08-10 18:14:04,471 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:14:04,472 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:14:04,472 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 18:14:04,472 INFO     29 [qwen-vl-text] positions(37): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:14:04,472 INFO     29 [qwen-vl-text] page grouping: [3], lines per page: [37]
2026-08-10 18:14:04,667 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 18:14:04,669 INFO     29 [qwen-vl-text] LLM extraction start, text_len=591
2026-08-10 18:14:04,669 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:14:04,669 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 96, \"bbox_end\": 132, \"encounter_dates\": [\"2025-02-20\"], \"department\": \"病理科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "青岛大学附属医院\n市南院区\n病理检查诊断报告\n病理号.\n姓  夕\n性  别：男\n年  龄：52\n送检单位：青岛大学附属医院市 送检科室：消化内科\n收到日期：\n送检医生：李晓宇\n病  区：\n住院号：\n送检材料：肠镜活检\n临床诊断：直肠多发息肉完成ESD吻合口溃疡\n大体检查:\n直肠息肉ESD：粘膜组织一件，大小3.5*2.5*0.8cm，距一侧切缘0.1cm，距另一侧\n切缘0.4cm，粘膜表面见一隆起，范围3*2.3cm，切面灰白质脆，基底涂墨。\n直肠吻合口：粘膜组织三块，合计直径0.4cm。\n病理诊断:\n1.标本类型：直肠息肉ESD\n标本数量：1件\n病变数量：1灶\n病变范围：3*2.3cm\n组织学类型：绒毛状--管状腺瘤伴高级别上皮内瘤变，局灶区域恶变--中分化腺癌，\n局限于粘膜层内\n脉管癌栓：（-）\n神经侵犯：（-）\n水平切缘：（-）\n垂直切缘：（-）\n2.（直肠吻合口）腺癌（中分化）。\n免疫组化结果示（直肠息肉ESD）：MLH1（+），MSH2（+），MSH6（+），PMS2\n(+），p53（+，约20%），CK-Desmin示粘膜肌连续，HER2（1+），S100示神经侵犯\n（-），CD31及D2-40示脉管癌栓（-），Ki-67（+，约60%）。\n报告医生：李丹\n初诊医生：赵玉洁\n报告日期：2025-02-20\n注：1.病理诊断分级注解：明确及基本明确的诊断",
    "role": "user"
  }
]
2026-08-10 18:14:08,700 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:14:08,700 INFO     29 [qwen-vl-text] LLM output (len=724):
{
  "exam_date": "2025-02-20",
  "report_date": "2025-02-20",
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "直肠",
  "patient_name": null,
  "patient_gender": "男",
  "department": "消化内科",
  "bed_number": null,
  "findings": "大体检查:\n直肠息肉ESD：粘膜组织一件，大小3.5*2.5*0.8cm，距一侧切缘0.1cm，距另一侧切缘0.4cm，粘膜表面见一隆起，范围3*2.3cm，切面灰白质脆，基底涂墨。\n直肠吻合口：粘膜组织三块，合计直径0.4cm。",
  "conclusion": "病理诊断:\n1.标本类型：直肠息肉ESD\n标本数量：1件\n病变数量：1灶\n病变范围：3*2.3cm\n组织学类型：绒毛状--管状腺瘤伴高级别上皮内瘤变，局灶区域恶变--中分化腺癌，局限于粘膜层内\n脉管癌栓：（-）\n神经侵犯：（-）\n水平切缘：（-）\n垂直切缘：（-）\n2.（直肠吻合口）腺癌（中分化）。\n免疫组化结果示（直肠息肉ESD）：MLH1（+），MSH2（+），MSH6（+），PMS2(+），p53（+，约20%），CK-Desmin示粘膜肌连续，HER2（1+），S100示神经侵犯（-），CD31及D2-40示脉管癌栓（-），Ki-67（+，约60%）。",
  "physician": "李丹",
  "reviewer": "赵玉洁"
}
2026-08-10 18:14:08,703 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=979697, prompt_len=1315
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共37行）
["青岛大学附属医院", "市南院区", "病理检查诊断报告", "病理号.", "姓  夕", "性  别：男", "年  龄：52", "送检单位：青岛大学附属医院市 送检科室：消化内科", "收到日期：", "送检医生：李晓宇", "病  区：", "住院号：", "送检材料：肠镜活检", "临床诊断：直肠多发息肉完成ESD吻合口溃疡", "大体检查:", "直肠息肉ESD：粘膜组织一件，大小3.5*2.5*0.8cm，距一侧切缘0.1cm，距另一侧", "切缘0.4cm，粘膜表面见一隆起，范围3*2.3cm，切面灰白质脆，基底涂墨。", "直肠吻合口：粘膜组织三块，合计直径0.4cm。", "病理诊断:", "1.标本类型：直肠息肉ESD", "标本数量：1件", "病变数量：1灶", "病变范围：3*2.3cm", "组织学类型：绒毛状--管状腺瘤伴高级别上皮内瘤变，局灶区域恶变--中分化腺癌，", "局限于粘膜层内", "脉管癌栓：（-）", "神经侵犯：（-）", "水平切缘：（-）", "垂直切缘：（-）", "2.（直肠吻合口）腺癌（中分化）。", "免疫组化结果示（直肠息肉ESD）：MLH1（+），MSH2（+），MSH6（+），PMS2", "(+），p53（+，约20%），CK-Desmin示粘膜肌连续，HER2（1+），S100示神经侵犯", "（-），CD31及D2-40示脉管癌栓（-），Ki-67（+，约60%）。", "报告医生：李丹", "初诊医生：赵玉洁", "报告日期：2025-02-20", "注：1.病理诊断分级注解：明确及基本明确的诊断"]

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
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord API raw response (len=2217):
[
	{"text": "青岛大学附属医院", "bbox": [366, 57, 674, 88]},
	{"text": "市南院区", "bbox": [770, 77, 855, 97]},
	{"text": "病理检查诊断报告", "bbox": [391, 95, 648, 119]},
	{"text": "病理号.", "bbox": [138, 129, 215, 146]},
	{"text": "姓  夕", "bbox": [138, 158, 215, 172]},
	{"text": "性  别：男", "bbox": [414, 158, 524, 173]},
	{"text": "年  龄：52", "bbox": [675, 159, 790, 174]},
	{"text": "送检单位：青岛大学附属医院市 送检科室：消化内科", "bbox": [138, 186, 582, 202]},
	{"text": "收到日期：", "bbox": [675, 188, 759, 203]},
	{"text": "送检医生：李晓宇", "bbox": [138, 216, 291, 232]},
	{"text": "病  区：", "bbox": [414, 218, 500, 233]},
	{"text": "住院号：", "bbox": [675, 218, 760, 234]},
	{"text": "送检材料：肠镜活检", "bbox": [138, 242, 311, 257]},
	{"text": "临床诊断：直肠多发息肉完成ESD吻合口溃疡", "bbox": [506, 243, 874, 259]},
	{"text": "大体检查:", "bbox": [138, 267, 232, 284]},
	{"text": "直肠息肉ESD：粘膜组织一件，大小3.5*2.5*0.8cm，距一侧切缘0.1cm，距另一侧", "bbox": [155, 286, 839, 302]},
	{"text": "切缘0.4cm，粘膜表面见一隆起，范围3*2.3cm，切面灰白质脆，基底涂墨。", "bbox": [155, 302, 782, 318]},
	{"text": "直肠吻合口：粘膜组织三块，合计直径0.4cm。", "bbox": [155, 319, 542, 335]},
	{"text": "病理诊断:", "bbox": [143, 464, 240, 480]},
	{"text": "1.标本类型：直肠息肉ESD", "bbox": [144, 482, 374, 498]},
	{"text": "标本数量：1件", "bbox": [144, 499, 276, 514]},
	{"text": "病变数量：1灶", "bbox": [144, 515, 276, 530]},
	{"text": "病变范围：3*2.3cm", "bbox": [144, 531, 318, 547]},
	{"text": "组织学类型：绒毛状--管状腺瘤伴高级别上皮内瘤变，局灶区域恶变--中分化腺癌，", "bbox": [144, 547, 857, 563]},
	{"text": "局限于粘膜层内", "bbox": [147, 564, 287, 580]},
	{"text": "脉管癌栓：（-）", "bbox": [147, 580, 288, 596]},
	{"text": "神经侵犯：（-）", "bbox": [147, 596, 288, 612]},
	{"text": "水平切缘：（-）", "bbox": [147, 612, 288, 628]},
	{"text": "垂直切缘：（-）", "bbox": [147, 628, 288, 644]},
	{"text": "2.（直肠吻合口）腺癌（中分化）。", "bbox": [147, 644, 453, 661]},
	{"text": "免疫组化结果示（直肠息肉ESD）：MLH1（+），MSH2（+），MSH6（+），PMS2", "bbox": [147, 661, 825, 678]},
	{"text": "(+），p53（+，约20%），CK-Desmin示粘膜肌连续，HER2（1+），S100示神经侵犯", "bbox": [155, 678, 879, 695]},
	{"text": "（-），CD31及D2-40示脉管癌栓（-），Ki-67（+，约60%）。", "bbox": [155, 695, 675, 711]},
	{"text": "报告医生：李丹", "bbox": [127, 872, 323, 896]},
	{"text": "初诊医生：赵玉洁", "bbox": [703, 885, 871, 904]},
	{"text": "报告日期：2025-02-20", "bbox": [705, 917, 921, 937]},
	{"text": "注：1.病理诊断分级注解：明确及基本明确的诊断", "bbox": [124, 926, 504, 946]}
]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord API: raw_items=37, valid_items=37, elapsed=11.8s
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[0]: text=青岛大学附属医院, bbox=[366, 57, 674, 88]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[1]: text=市南院区, bbox=[770, 77, 855, 97]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[2]: text=病理检查诊断报告, bbox=[391, 95, 648, 119]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[3]: text=病理号., bbox=[138, 129, 215, 146]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[4]: text=姓  夕, bbox=[138, 158, 215, 172]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[5]: text=性  别：男, bbox=[414, 158, 524, 173]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[6]: text=年  龄：52, bbox=[675, 159, 790, 174]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[7]: text=送检单位：青岛大学附属医院市 送检科室：消化内科, bbox=[138, 186, 582, 202]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[8]: text=收到日期：, bbox=[675, 188, 759, 203]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[9]: text=送检医生：李晓宇, bbox=[138, 216, 291, 232]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[10]: text=病  区：, bbox=[414, 218, 500, 233]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[11]: text=住院号：, bbox=[675, 218, 760, 234]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[12]: text=送检材料：肠镜活检, bbox=[138, 242, 311, 257]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[13]: text=临床诊断：直肠多发息肉完成ESD吻合口溃疡, bbox=[506, 243, 874, 259]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[14]: text=大体检查:, bbox=[138, 267, 232, 284]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[15]: text=直肠息肉ESD：粘膜组织一件，大小3.5*2.5*0.8cm，距一侧切缘0.1cm，距另一侧, bbox=[155, 286, 839, 302]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[16]: text=切缘0.4cm，粘膜表面见一隆起，范围3*2.3cm，切面灰白质脆，基底涂墨。, bbox=[155, 302, 782, 318]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[17]: text=直肠吻合口：粘膜组织三块，合计直径0.4cm。, bbox=[155, 319, 542, 335]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[18]: text=病理诊断:, bbox=[143, 464, 240, 480]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[19]: text=1.标本类型：直肠息肉ESD, bbox=[144, 482, 374, 498]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[20]: text=标本数量：1件, bbox=[144, 499, 276, 514]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[21]: text=病变数量：1灶, bbox=[144, 515, 276, 530]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[22]: text=病变范围：3*2.3cm, bbox=[144, 531, 318, 547]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[23]: text=组织学类型：绒毛状--管状腺瘤伴高级别上皮内瘤变，局灶区域恶变--中分化腺癌，, bbox=[144, 547, 857, 563]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[24]: text=局限于粘膜层内, bbox=[147, 564, 287, 580]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[25]: text=脉管癌栓：（-）, bbox=[147, 580, 288, 596]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[26]: text=神经侵犯：（-）, bbox=[147, 596, 288, 612]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[27]: text=水平切缘：（-）, bbox=[147, 612, 288, 628]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[28]: text=垂直切缘：（-）, bbox=[147, 628, 288, 644]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[29]: text=2.（直肠吻合口）腺癌（中分化）。, bbox=[147, 644, 453, 661]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[30]: text=免疫组化结果示（直肠息肉ESD）：MLH1（+），MSH2（+），MSH6（+），PMS2, bbox=[147, 661, 825, 678]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[31]: text=(+），p53（+，约20%），CK-Desmin示粘膜肌连续，HER2（1+），S100示神经侵犯, bbox=[155, 678, 879, 695]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[32]: text=（-），CD31及D2-40示脉管癌栓（-），Ki-67（+，约60%）。, bbox=[155, 695, 675, 711]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[33]: text=报告医生：李丹, bbox=[127, 872, 323, 896]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[34]: text=初诊医生：赵玉洁, bbox=[703, 885, 871, 904]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[35]: text=报告日期：2025-02-20, bbox=[705, 917, 921, 937]
2026-08-10 18:14:20,458 INFO     29 [qwen-vl-text] coord item[36]: text=注：1.病理诊断分级注解：明确及基本明确的诊断, bbox=[124, 926, 504, 946]
2026-08-10 18:14:20,459 INFO     29 [qwen-vl-text] page=3 — 37/37 coords, api_time=11.8s
2026-08-10 18:14:20,459 INFO     29 [qwen-vl-text] new_positions (37):
[[3, 217.76999999999998, 401.03, 47.994, 74.096], [3, 458.15, 508.72499999999997, 64.834, 81.67399999999999], [3, 232.64499999999998, 385.56, 79.99, 100.198], [3, 82.11, 127.925, 108.618, 122.932], [3, 82.11, 127.925, 133.036, 144.82399999999998], [3, 246.32999999999998, 311.78, 133.036, 145.666], [3, 401.625, 470.04999999999995, 133.878, 146.50799999999998], [3, 82.11, 346.28999999999996, 156.612, 170.084], [3, 401.625, 451.60499999999996, 158.296, 170.926], [3, 82.11, 173.14499999999998, 181.87199999999999, 195.344], [3, 246.32999999999998, 297.5, 183.55599999999998, 196.186], [3, 401.625, 452.2, 183.55599999999998, 197.028], [3, 82.11, 185.045, 203.76399999999998, 216.394], [3, 301.07, 520.03, 204.606, 218.078], [3, 82.11, 138.04, 224.814, 239.128], [3, 92.225, 499.205, 240.81199999999998, 254.284], [3, 92.225, 465.28999999999996, 254.284, 267.756], [3, 92.225, 322.49, 268.598, 282.07], [3, 85.085, 142.79999999999998, 390.688, 404.15999999999997], [3, 85.67999999999999, 222.53, 405.844, 419.316], [3, 85.67999999999999, 164.22, 420.15799999999996, 432.788], [3, 85.67999999999999, 164.22, 433.63, 446.26], [3, 85.67999999999999, 189.20999999999998, 447.102, 460.574], [3, 85.67999999999999, 509.91499999999996, 460.574, 474.046], [3, 87.46499999999999, 170.765, 474.888, 488.35999999999996], [3, 87.46499999999999, 171.35999999999999, 488.35999999999996, 501.832], [3, 87.46499999999999, 171.35999999999999, 501.832, 515.304], [3, 87.46499999999999, 171.35999999999999, 515.304, 528.776], [3, 87.46499999999999, 171.35999999999999, 528.776, 542.2479999999999], [3, 87.46499999999999, 269.53499999999997, 542.2479999999999, 556.562], [3, 87.46499999999999, 490.875, 556.562, 570.876], [3, 92.225, 523.005, 570.876, 585.1899999999999], [3, 92.225, 401.625, 585.1899999999999, 598.662], [3, 75.565, 192.185, 734.2239999999999, 754.432], [3, 418.28499999999997, 518.245, 745.17, 761.168], [3, 419.47499999999997, 547.995, 772.1139999999999, 788.954], [3, 73.78, 299.88, 779.692, 796.5319999999999]]
2026-08-10 18:14:20,459 INFO     29 [qwen-vl-text] ═══ DONE ═══ 37 positions, pages=1, time=16.0s
2026-08-10 18:14:20,459 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:14:20,466 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:14:20,467 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 18:14:20,467 INFO     29 [qwen-vl-text] positions(170): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:14:20,467 INFO     29 [qwen-vl-text] page grouping: [4, 5], lines per page: [54, 116]
2026-08-10 18:14:20,644 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 18:14:20,798 INFO     29 [qwen-vl-text] page=5, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 18:14:20,799 INFO     29 [qwen-vl-text] LLM extraction start, text_len=2944
2026-08-10 18:14:20,799 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:14:20,800 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 133, \"bbox_end\": 302, \"encounter_dates\": [], \"department\": \"基因检测中心\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "青岛市中心医疗集团\n2.检测结果总览\n本检测基于MGI（DNBSeq T7）测序平台对样本进行高通量测序。覆盖肿瘤相关的566个基因，检测内容包含目标基\n因覆盖范围内的单核苷酸变异、小片段插入/缺失、拷贝数变异、重排（融合），以及微卫星不稳定性（MSI）分析、肿瘤\n突变负荷（TMB）分析等。\n检测类别\n检测结果\n基因变异1\n体系\nI类（具有明确临床意义的变异）：KRAS p.G12D, KRAS p.A146V\nII类（具有潜在临床意义的变异）：TP53 p.G245D, FBXW7 p.R367*\nIII类（临床意义不确定的变异）：RBM10 p.R97*, MUC16 p.A7208T, ALDH2 p\n.A5T, MTOR p.G1491S, CARD11 p.R207C等26个\n胚系\n致病性/疑似致病性变异：APC p.L180Yfs*5\n靶向药物提示\nKRAS p.G12D提示：司美替尼(C级)、Avutometinib and defactinib (C级)可能敏感；西妥昔单抗(A级)、Panitumumab (A级)可能耐药。\nKRAS p.A146V提示：Avutometinib and defactinib (C级)可能敏感；西妥昔单抗(A级)、Pan\nitumumab (A级)可能耐药。\nTP53 p.G245D提示：AZD1775 (C级)可能敏感。\nFBXW7 p.R367*提示：恩替司他(D级)、Belinostat (D级)可能敏感。\nAPC p.L180Yfs*5提示：达沙替尼(D级)、厄洛替尼(D级)可能敏感。\n诊断/预后提示\n目前暂未发现与本癌种诊断/预后相关的基因变异。\n免疫治疗疗效提示\nTMB(同义突变 非同义突变)\n13.89Muts/Mb\nTMB(非同义突变)\n10.42Muts/Mb (前12.62%)\nMSI状态\nMSS (微卫星稳定)\n其他潜在免疫疗效相关标志物2\n正相关：未检出\n负相关：未检出\n超进展相关：未检出\n化疗用药提示\n可能药物敏感性较高：暂无，详见实验结果\n可能毒副作用风险较低：卡培他滨，伊立替康\n肿瘤遗传风险提示\n检出APC p.L180Yfs*5疑似致病性变异，建议对受检者及血亲进行适当的遗传咨询或临床管理\n注：1. 基因变异\n58\n青岛市中心医疗集团\n(1) 体系变异参考AMP/ASCO/CAP 共识《Standards and Guidelines for the Interpretation and Reporting of\nSequence Variants in Cancer》，基因变异按照临床意义的重要性分为四个类别\nI类：具有明确临床意义的变异，包括NMPA、FDA批准疗法，或专业临床指南（如CSCO诊疗指南、NCCN临\n床实践指南）推荐（A级证据），或基于证据充分的临床研究，并获得专家共识有明确治疗、诊断、预后的\n变异（B级证据）；\nII类：具有潜在临床意义的变异，包括其他癌种的A级证据（跨适应症用药），或多项小型临床研究支持，或\n已作为当前临床研究的入组标准（C级证据），或临床前研究或案例报道，未获得专家共识的药物（D级证\n据）；\nIII类：临床意义不确定的变异（尚无相关临床证据）\n“类：下事或示能于事的变异（在全人群或特定人群数据库中观察到高变异率）\n扫描全能王 创建\n青岛市中心医疗集团\n3.基因变异临床意义综合提示\n3.1诊断/预后及靶向药物提示\n基因变异1\n突变丰度2/拷贝数\n变异分类\n可能敏感药物\n可能耐药药物\n突变说明\nKRAS\nNM_004985.5\n12.81%\nI类\n司美替尼(C级)\n西妥昔单抗(A\n级)\nKRAS基因的G12D突变，发生在第\n2号外显子，位于GTP结合蛋白结\n构域(UniProt.org)，突变导致\n第12位氨基酸由甘氨酸变为天冬氨\n酸，G12突变将降低自身的GTP酶\n活性，使KRAS长期处于与GTP结\n合的激活状态，导致细胞增殖异常\n(PMID:12509763,20736745,2\n6037647,6092966)，为功能获\n得突变。\nexon2\np.G12D\nc.35G>A\nAvutometinib a\nnd defactinib(C\n级)\nPantitumuma\nb(A级)\nKRAS\nNM_004985.5\n1.46%\nI类\nAvutometinib a\nnd defactinib(C\n级)\n西妥昔单抗(A\n级)\nKRAS基因的A146V突变，发生在\n第4号外显子，突变导致146位氨基\n酸由丙氨酸变为缬氨酸，为功能获\n得突变。在两个不同的细胞系中，\n与野生型Kras相比，A146V可能会\n降低Kras的GTPase活性，从而导\n致下游通路激活增加(PMID:205\n70890)，与野生型Kras相比，A1\n46V突变会增加细胞增殖和细胞活\n力(PMID:29533785)，为功能\n获得突变。\nexon4\np.A146V\nc.437C>T\nPanitumuma\nb(A级)\nTP53\nNM_000546.6\n12.73%\nII类\nAZD1775(C级)\nTP53基因的G245D突变，发生在\n第7号外显子，位于Tp53蛋白的D\nNA结合域(PMID:22713868)\n，突变导致245位甘氨酸变为天冬\n氨酸。G245D导致Tp53靶基因的\n激活减少(PMID:22214764,256\n34208,27533082)，为功能丧失\n突变。\nexon7\np.G245D\nc.734G>A\nFBXW7\nNM_033632.3\n2.75%\nII类\n恩替司他(D级)\nFBXW7基因的R367*突变，发生在\n第7号外显子，突变导致终止密码\n子提前编码(UniProt.org)。由于W\nD重复域的丢失，预测R367*会导\n致Fbxw7蛋白功能的丢失(UniProt\n.org)。\nexon7\np.R367*\nc.1099C>T\nBelinostat(D级)\nAPC\nNM_000038.6\n杂合\nII类\n达沙替尼(D级)\nAPC基因的p.L180Yfs*5、c.539de\nl突变，发生在第6外显子，不在已\n知功能域内(UniProt.org)，突\n变导致其编码的氨基酸在180位开\n始框移，可能影响蛋白功能(Uni\nProt.org)。已知APC的功能丧失\n变异具有致病性(PMID:17963004\n,20685668)。Clinvar数据库记录\n该变异为Pathogenic。其在人群\n基因组数据库未收录。综上分析，\n该突变是一个疑似致病性变异。\nexon6\np.L180Yfs*5\nc.539del\n厄洛替尼(D级)\n注:1.基因变异：“exon”为外显子，“intron”为内含子，“c”为DNA序列，“p”为蛋白质，“NM”为基因的转录\n本编号;\n2.突变丰度:在某位点产生突变的等位基因在该位点全部等位基因中所占比率。例如,突变丰度10%意为该位点含\n有10%的突变等位基因和90%的野生型等位基因。拷贝数:是指某一种基因或某一段特定的DNA序列在单倍体基\n因组中出现的数目。\n4/58",
    "role": "user"
  }
]
2026-08-10 18:14:20,803 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:14:20.802+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 85, "failed": 0, "current": {"a677452e94e611f1bd9827cf206dfa2d": {"id": "a677452e94e611f1bd9827cf206dfa2d", "doc_id": "a646f41e94e611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 11495294, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385378144, "task_type": "dataflow", "root_trace_id": "971de7c4c0604c27afceabc8ac295233", "root_traceparent": "00-971de7c4c0604c27afceabc8ac295233-de3f877b239fe0d8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:14:39,102 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:14:39,102 INFO     29 [qwen-vl-text] LLM output (len=3305):
{
  "exam_date": null,
  "report_date": null,
  "exam_name": "肿瘤相关基因检测",
  "exam_category": "pathology",
  "body_part": null,
  "patient_name": null,
  "patient_gender": null,
  "department": "基因检测中心",
  "bed_number": null,
  "findings": "2.检测结果总览\n本检测基于MGI（DNBSeq T7）测序平台对样本进行高通量测序。覆盖肿瘤相关的566个基因，检测内容包含目标基因覆盖范围内的单核苷酸变异、小片段插入/缺失、拷贝数变异、重排（融合），以及微卫星不稳定性（MSI）分析、肿瘤突变负荷（TMB）分析等。\n检测类别\t检测结果\n基因变异1\n体系\tI类（具有明确临床意义的变异）：KRAS p.G12D, KRAS p.A146V\n\tII类（具有潜在临床意义的变异）：TP53 p.G245D, FBXW7 p.R367*\n\tIII类（临床意义不确定的变异）：RBM10 p.R97*, MUC16 p.A7208T, ALDH2 p.A5T, MTOR p.G1491S, CARD11 p.R207C等26个\n胚系\t致病性/疑似致病性变异：APC p.L180Yfs*5\n靶向药物提示\nKRAS p.G12D提示：司美替尼(C级)、Avutometinib and defactinib (C级)可能敏感；西妥昔单抗(A级)、Panitumumab (A级)可能耐药。\nKRAS p.A146V提示：Avutometinib and defactinib (C级)可能敏感；西妥昔单抗(A级)、Panitumumab (A级)可能耐药。\nTP53 p.G245D提示：AZD1775 (C级)可能敏感。\nFBXW7 p.R367*提示：恩替司他(D级)、Belinostat (D级)可能敏感。\nAPC p.L180Yfs*5提示：达沙替尼(D级)、厄洛替尼(D级)可能敏感。\n诊断/预后提示\n目前暂未发现与本癌种诊断/预后相关的基因变异。\n免疫治疗疗效提示\nTMB(同义突变 非同义突变)\t13.89Muts/Mb\nTMB(非同义突变)\t10.42Muts/Mb (前12.62%)\nMSI状态\tMSS (微卫星稳定)\n其他潜在免疫疗效相关标志物2\n正相关：未检出\n负相关：未检出\n超进展相关：未检出\n化疗用药提示\n可能药物敏感性较高：暂无，详见实验结果\n可能毒副作用风险较低：卡培他滨，伊立替康\n肿瘤遗传风险提示\n检出APC p.L180Yfs*5疑似致病性变异，建议对受检者及血亲进行适当的遗传咨询或临床管理\n注：1. 基因变异\n(1) 体系变异参考AMP/ASCO/CAP 共识《Standards and Guidelines for the Interpretation and Reporting of Sequence Variants in Cancer》，基因变异按照临床意义的重要性分为四个类别\nI类：具有明确临床意义的变异，包括NMPA、FDA批准疗法，或专业临床指南（如CSCO诊疗指南、NCCN临床实践指南）推荐（A级证据），或基于证据充分的临床研究，并获得专家共识有明确治疗、诊断、预后的变异（B级证据）；\nII类：具有潜在临床意义的变异，包括其他癌种的A级证据（跨适应症用药），或多项小型临床研究支持，或已作为当前临床研究的入组标准（C级证据），或临床前研究或案例报道，未获得专家共识的药物（D级证据）；\nIII类：临床意义不确定的变异（尚无相关临床证据）\n“类：下事或示能于事的变异（在全人群或特定人群数据库中观察到高变异率）",
  "conclusion": "3.基因变异临床意义综合提示\n3.1诊断/预后及靶向药物提示\n| 基因变异1 | 突变丰度2/拷贝数 | 变异分类 | 可能敏感药物 | 可能耐药药物 | 突变说明 |\n|---|---|---|---|---|---|\n| KRAS NM_004985.5 exon2 p.G12D c.35G>A | 12.81% | I类 | 司美替尼(C级) Avutometinib and defactinib(C级) | 西妥昔单抗(A级) Pantitumumab(A级) | KRAS基因的G12D突变，发生在第2号外显子，位于GTP结合蛋白结构域(UniProt.org)，突变导致第12位氨基酸由甘氨酸变为天冬氨酸，G12突变将降低自身的GTP酶活性，使KRAS长期处于与GTP结合的激活状态，导致细胞增殖异常(PMID:12509763,20736745,26037647,6092966)，为功能获得突变。 |\n| KRAS NM_004985.5 exon4 p.A146V c.437C>T | 1.46% | I类 | Avutometinib and defactinib(C级) | 西妥昔单抗(A级) Panitumumab(A级) | KRAS基因的A146V突变，发生在第4号外显子，突变导致146位氨基酸由丙氨酸变为缬氨酸，为功能获得突变。在两个不同的细胞系中，与野生型Kras相比，A146V可能会降低Kras的GTPase活性，从而导致下游通路激活增加(PMID:20570890)，与野生型Kras相比，A146V突变会增加细胞增殖和细胞活力(PMID:29533785)，为功能获得突变。 |\n| TP53 NM_000546.6 exon7 p.G245D c.734G>A | 12.73% | II类 | AZD1775(C级) | | TP53基因的G245D突变，发生在第7号外显子，位于Tp53蛋白的DNA结合域(PMID:22713868)，突变导致245位甘氨酸变为天冬氨酸。G245D导致Tp53靶基因的激活减少(PMID:22214764,25634208,27533082)，为功能丧失突变。 |\n| FBXW7 NM_033632.3 exon7 p.R367* c.1099C>T | 2.75% | II类 | 恩替司他(D级) Belinostat(D级) | | FBXW7基因的R367*突变，发生在第7号外显子，突变导致终止密码子提前编码(UniProt.org)。由于WD重复域的丢失，预测R367*会导致Fbxw7蛋白功能的丢失(UniProt.org)。 |\n| APC NM_000038.6 exon6 p.L180Yfs*5 c.539del | 杂合 | II类 | 达沙替尼(D级) 厄洛替尼(D级) | | APC基因的p.L180Yfs*5、c.539del突变，发生在第6外显子，不在已知功能域内(UniProt.org)，突变导致其编码的氨基酸在180位开始框移，可能影响蛋白功能(UniProt.org)。已知APC的功能丧失变异具有致病性(PMID:17963004,20685668)。Clinvar数据库记录该变异为Pathogenic。其在人群基因组数据库未收录。综上分析，该突变是一个疑似致病性变异。 |\n\n注:1.基因变异：“exon”为外显子，“intron”为内含子，“c”为DNA序列，“p”为蛋白质，“NM”为基因的转录本编号;\n2.突变丰度:在某位点产生突变的等位基因在该位点全部等位基因中所占比率。例如,突变丰度10%意为该位点含有10%的突变等位基因和90%的野生型等位基因。拷贝数:是指某一种基因或某一段特定的DNA序列在单倍体基因组中出现的数目。",
  "physician": null,
  "reviewer": null
}
2026-08-10 18:14:39,107 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1020840, prompt_len=2175
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共54行）
["青岛市中心医疗集团", "2.检测结果总览", "本检测基于MGI（DNBSeq T7）测序平台对样本进行高通量测序。覆盖肿瘤相关的566个基因，检测内容包含目标基", "因覆盖范围内的单核苷酸变异、小片段插入/缺失、拷贝数变异、重排（融合），以及微卫星不稳定性（MSI）分析、肿瘤", "突变负荷（TMB）分析等。", "检测类别", "检测结果", "基因变异1", "体系", "I类（具有明确临床意义的变异）：KRAS p.G12D, KRAS p.A146V", "II类（具有潜在临床意义的变异）：TP53 p.G245D, FBXW7 p.R367*", "III类（临床意义不确定的变异）：RBM10 p.R97*, MUC16 p.A7208T, ALDH2 p", ".A5T, MTOR p.G1491S, CARD11 p.R207C等26个", "胚系", "致病性/疑似致病性变异：APC p.L180Yfs*5", "靶向药物提示", "KRAS p.G12D提示：司美替尼(C级)、Avutometinib and defactinib (C级)可能敏感；西妥昔单抗(A级)、Panitumumab (A级)可能耐药。", "KRAS p.A146V提示：Avutometinib and defactinib (C级)可能敏感；西妥昔单抗(A级)、Pan", "itumumab (A级)可能耐药。", "TP53 p.G245D提示：AZD1775 (C级)可能敏感。", "FBXW7 p.R367*提示：恩替司他(D级)、Belinostat (D级)可能敏感。", "APC p.L180Yfs*5提示：达沙替尼(D级)、厄洛替尼(D级)可能敏感。", "诊断/预后提示", "目前暂未发现与本癌种诊断/预后相关的基因变异。", "免疫治疗疗效提示", "TMB(同义突变 非同义突变)", "13.89Muts/Mb", "TMB(非同义突变)", "10.42Muts/Mb (前12.62%)", "MSI状态", "MSS (微卫星稳定)", "其他潜在免疫疗效相关标志物2", "正相关：未检出", "负相关：未检出", "超进展相关：未检出", "化疗用药提示", "可能药物敏感性较高：暂无，详见实验结果", "可能毒副作用风险较低：卡培他滨，伊立替康", "肿瘤遗传风险提示", "检出APC p.L180Yfs*5疑似致病性变异，建议对受检者及血亲进行适当的遗传咨询或临床管理", "注：1. 基因变异", "58", "青岛市中心医疗集团", "(1) 体系变异参考AMP/ASCO/CAP 共识《Standards and Guidelines for the Interpretation and Reporting of", "Sequence Variants in Cancer》，基因变异按照临床意义的重要性分为四个类别", "I类：具有明确临床意义的变异，包括NMPA、FDA批准疗法，或专业临床指南（如CSCO诊疗指南、NCCN临", "床实践指南）推荐（A级证据），或基于证据充分的临床研究，并获得专家共识有明确治疗、诊断、预后的", "变异（B级证据）；", "II类：具有潜在临床意义的变异，包括其他癌种的A级证据（跨适应症用药），或多项小型临床研究支持，或", "已作为当前临床研究的入组标准（C级证据），或临床前研究或案例报道，未获得专家共识的药物（D级证", "据）；", "III类：临床意义不确定的变异（尚无相关临床证据）", "“类：下事或示能于事的变异（在全人群或特定人群数据库中观察到高变异率）", "扫描全能王 创建"]

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
2026-08-10 18:14:59,477 INFO     29 [qwen-vl-text] coord API raw response (len=3775):
[
	{"text": "青岛市中心医疗集团", "bbox": [690, 26, 791, 35]},
	{"text": "2.检测结果总览", "bbox": [175, 77, 335, 94]},
	{"text": "本检测基于MGI（DNBSeq T7）测序平台对样本进行高通量测序。覆盖肿瘤相关的566个基因，检测内容包含目标基", "bbox": [175, 110, 811, 121]},
	{"text": "因覆盖范围内的单核苷酸变异、小片段插入/缺失、拷贝数变异、重排（融合），以及微卫星不稳定性（MSI）分析、肿瘤", "bbox": [175, 121, 814, 132]},
	{"text": "突变负荷（TMB）分析等。", "bbox": [175, 132, 314, 142]},
	{"text": "检测类别", "bbox": [211, 158, 259, 168]},
	{"text": "检测结果", "bbox": [529, 158, 578, 168]},
	{"text": "基因变异1", "bbox": [182, 216, 236, 226]},
	{"text": "体系", "bbox": [303, 208, 328, 218]},
	{"text": "I类（具有明确临床意义的变异）：KRAS p.G12D, KRAS p.A146V", "bbox": [373, 177, 727, 187]},
	{"text": "II类（具有潜在临床意义的变异）：TP53 p.G245D, FBXW7 p.R367*", "bbox": [373, 196, 741, 206]},
	{"text": "III类（临床意义不确定的变异）：RBM10 p.R97*, MUC16 p.A7208T, ALDH2 p", "bbox": [373, 226, 804, 237]},
	{"text": ".A5T, MTOR p.G1491S, CARD11 p.R207C等26个", "bbox": [373, 237, 648, 248]},
	{"text": "胚系", "bbox": [303, 258, 328, 268]},
	{"text": "致病性/疑似致病性变异：APC p.L180Yfs*5", "bbox": [373, 258, 604, 268]},
	{"text": "靶向药物提示", "bbox": [182, 327, 254, 337]},
	{"text": "KRAS p.G12D提示：司美替尼(C级)、Avutometinib and defactinib (C级)可能敏感；西妥昔单抗(A级)、Panitumumab (A级)可能耐药。", "bbox": [303, 276, 794, 287]},
	{"text": "KRAS p.A146V提示：Avutometinib and defactinib (C级)可能敏感；西妥昔单抗(A级)、Pan", "bbox": [303, 307, 803, 317]},
	{"text": "itumumab (A级)可能耐药。", "bbox": [303, 317, 450, 328]},
	{"text": "TP53 p.G245D提示：AZD1775 (C级)可能敏感。", "bbox": [303, 339, 554, 349]},
	{"text": "FBXW7 p.R367*提示：恩替司他(D级)、Belinostat (D级)可能敏感。", "bbox": [303, 359, 664, 369]},
	{"text": "APC p.L180Yfs*5提示：达沙替尼(D级)、厄洛替尼(D级)可能敏感。", "bbox": [303, 377, 658, 387]},
	{"text": "诊断/预后提示", "bbox": [182, 395, 259, 405]},
	{"text": "目前暂未发现与本癌种诊断/预后相关的基因变异。", "bbox": [303, 395, 567, 405]},
	{"text": "免疫治疗疗效提示", "bbox": [182, 460, 278, 470]},
	{"text": "TMB(同义突变&非同义突变)", "bbox": [303, 414, 455, 424]},
	{"text": "13.89Muts/Mb", "bbox": [496, 414, 576, 424]},
	{"text": "TMB(非同义突变)", "bbox": [303, 433, 398, 443]},
	{"text": "10.42Muts/Mb (前12.62%)", "bbox": [496, 433, 648, 443]},
	{"text": "MSI状态", "bbox": [303, 452, 349, 462]},
	{"text": "MSS (微卫星稳定)", "bbox": [496, 452, 596, 462]},
	{"text": "其他潜在免疫疗效相关标志物2", "bbox": [303, 487, 466, 497]},
	{"text": "正相关：未检出", "bbox": [496, 470, 579, 480]},
	{"text": "负相关：未检出", "bbox": [496, 487, 579, 497]},
	{"text": "超进展相关：未检出", "bbox": [496, 506, 603, 516]},
	{"text": "化疗用药提示", "bbox": [182, 533, 254, 543]},
	{"text": "可能药物敏感性较高：暂无，详见实验结果", "bbox": [303, 524, 532, 534]},
	{"text": "可能毒副作用风险较低：卡培他滨，伊立替康", "bbox": [303, 543, 544, 553]},
	{"text": "肿瘤遗传风险提示", "bbox": [182, 567, 278, 577]},
	{"text": "检出APC p.L180Yfs*5疑似致病性变异，建议对受检者及血亲进行适当的遗传咨询或临床管理", "bbox": [303, 562, 795, 572]},
	{"text": "注：1. 基因变异", "bbox": [175, 598, 263, 608]},
	{"text": "58", "bbox": [495, 713, 508, 720]},
	{"text": "青岛市中心医疗集团", "bbox": [690, 775, 791, 784]},
	{"text": "(1) 体系变异参考AMP/ASCO/CAP 共识《Standards and Guidelines for the Interpretation and Reporting of", "bbox": [223, 824, 793, 835]},
	{"text": "Sequence Variants in Cancer》，基因变异按照临床意义的重要性分为四个类别", "bbox": [247, 836, 665, 847]},
	{"text": "I类：具有明确临床意义的变异，包括NMPA、FDA批准疗法，或专业临床指南（如CSCO诊疗指南、NCCN临", "bbox": [247, 849, 811, 860]},
	{"text": "床实践指南）推荐（A级证据），或基于证据充分的临床研究，并获得专家共识有明确治疗、诊断、预后的", "bbox": [247, 861, 806, 872]},
	{"text": "变异（B级证据）；", "bbox": [247, 873, 345, 884]},
	{"text": "II类：具有潜在临床意义的变异，包括其他癌种的A级证据（跨适应症用药），或多项小型临床研究支持，或", "bbox": [247, 886, 813, 897]},
	{"text": "已作为当前临床研究的入组标准（C级证据），或临床前研究或案例报道，未获得专家共识的药物（D级证", "bbox": [247, 898, 803, 909]},
	{"text": "据）；", "bbox": [247, 910, 275, 921]},
	{"text": "III类：临床意义不确定的变异（尚无相关临床证据）", "bbox": [247, 923, 525, 934]},
	{"text": "“类：下事或示能于事的变异（在全人群或特定人群数据库中观察到高变异率）", "bbox": [247, 936, 672, 946]},
	{"text": "扫描全能王 创建", "bbox": [801, 962, 965, 978]}
]
2026-08-10 18:14:59,477 INFO     29 [qwen-vl-text] coord API: raw_items=54, valid_items=54, elapsed=20.4s
2026-08-10 18:14:59,478 INFO     29 [qwen-vl-text] coord item[0]: text=青岛市中心医疗集团, bbox=[690, 26, 791, 35]
2026-08-10 18:14:59,478 INFO     29 [qwen-vl-text] coord item[1]: text=2.检测结果总览, bbox=[175, 77, 335, 94]
2026-08-10 18:14:59,478 INFO     29 [qwen-vl-text] coord item[2]: text=本检测基于MGI（DNBSeq T7）测序平台对样本进行高通量测序。覆盖肿瘤相关的566个基因，检测内容包含目标基, bbox=[175, 110, 811, 121]
2026-08-10 18:14:59,478 INFO     29 [qwen-vl-text] coord item[3]: text=因覆盖范围内的单核苷酸变异、小片段插入/缺失、拷贝数变异、重排（融合），以及微卫星不稳定性（MSI）分析、肿瘤, bbox=[175, 121, 814, 132]
2026-08-10 18:14:59,478 INFO     29 [qwen-vl-text] coord item[4]: text=突变负荷（TMB）分析等。, bbox=[175, 132, 314, 142]
2026-08-10 18:14:59,478 INFO     29 [qwen-vl-text] coord item[5]: text=检测类别, bbox=[211, 158, 259, 168]
2026-08-10 18:14:59,478 INFO     29 [qwen-vl-text] coord item[6]: text=检测结果, bbox=[529, 158, 578, 168]
2026-08-10 18:14:59,478 INFO     29 [qwen-vl-text] coord item[7]: text=基因变异1, bbox=[182, 216, 236, 226]
2026-08-10 18:14:59,478 INFO     29 [qwen-vl-text] coord item[8]: text=体系, bbox=[303, 208, 328, 218]
2026-08-10 18:14:59,478 INFO     29 [qwen-vl-text] coord item[9]: text=I类（具有明确临床意义的变异）：KRAS p.G12D, KRAS p.A146V, bbox=[373, 177, 727, 187]
2026-08-10 18:14:59,478 INFO     29 [qwen-vl-text] coord item[10]: text=II类（具有潜在临床意义的变异）：TP53 p.G245D, FBXW7 p.R367*, bbox=[373, 196, 741, 206]
2026-08-10 18:14:59,478 INFO     29 [qwen-vl-text] coord item[11]: text=III类（临床意义不确定的变异）：RBM10 p.R97*, MUC16 p.A7208T, ALDH2 p, bbox=[373, 226, 804, 237]
2026-08-10 18:14:59,478 INFO     29 [qwen-vl-text] coord item[12]: text=.A5T, MTOR p.G1491S, CARD11 p.R207C等26个, bbox=[373, 237, 648, 248]
2026-08-10 18:14:59,478 INFO     29 [qwen-vl-text] coord item[13]: text=胚系, bbox=[303, 258, 328, 268]
2026-08-10 18:14:59,478 INFO     29 [qwen-vl-text] coord item[14]: text=致病性/疑似致病性变异：APC p.L180Yfs*5, bbox=[373, 258, 604, 268]
2026-08-10 18:14:59,478 INFO     29 [qwen-vl-text] coord item[15]: text=靶向药物提示, bbox=[182, 327, 254, 337]
2026-08-10 18:14:59,479 INFO     29 [qwen-vl-text] coord item[16]: text=KRAS p.G12D提示：司美替尼(C级)、Avutometinib and defactinib (C级)可能敏感；西妥昔单抗(A级)、Panitumumab (A级)可能耐药。, bbox=[303, 276, 794, 287]
2026-08-10 18:14:59,479 INFO     29 [qwen-vl-text] coord item[17]: text=KRAS p.A146V提示：Avutometinib and defactinib (C级)可能敏感；西妥昔单抗(A级)、Pan, bbox=[303, 307, 803, 317]
2026-08-10 18:14:59,479 INFO     29 [qwen-vl-text] coord item[18]: text=itumumab (A级)可能耐药。, bbox=[303, 317, 450, 328]
2026-08-10 18:14:59,479 INFO     29 [qwen-vl-text] coord item[19]: text=TP53 p.G245D提示：AZD1775 (C级)可能敏感。, bbox=[303, 339, 554, 349]
2026-08-10 18:14:59,479 INFO     29 [qwen-vl-text] coord item[20]: text=FBXW7 p.R367*提示：恩替司他(D级)、Belinostat (D级)可能敏感。, bbox=[303, 359, 664, 369]
2026-08-10 18:14:59,479 INFO     29 [qwen-vl-text] coord item[21]: text=APC p.L180Yfs*5提示：达沙替尼(D级)、厄洛替尼(D级)可能敏感。, bbox=[303, 377, 658, 387]
2026-08-10 18:14:59,479 INFO     29 [qwen-vl-text] coord item[22]: text=诊断/预后提示, bbox=[182, 395, 259, 405]
2026-08-10 18:14:59,479 INFO     29 [qwen-vl-text] coord item[23]: text=目前暂未发现与本癌种诊断/预后相关的基因变异。, bbox=[303, 395, 567, 405]
2026-08-10 18:14:59,479 INFO     29 [qwen-vl-text] coord item[24]: text=免疫治疗疗效提示, bbox=[182, 460, 278, 470]
2026-08-10 18:14:59,479 INFO     29 [qwen-vl-text] coord item[25]: text=TMB(同义突变&非同义突变), bbox=[303, 414, 455, 424]
2026-08-10 18:14:59,479 INFO     29 [qwen-vl-text] coord item[26]: text=13.89Muts/Mb, bbox=[496, 414, 576, 424]
2026-08-10 18:14:59,479 INFO     29 [qwen-vl-text] coord item[27]: text=TMB(非同义突变), bbox=[303, 433, 398, 443]
2026-08-10 18:14:59,479 INFO     29 [qwen-vl-text] coord item[28]: text=10.42Muts/Mb (前12.62%), bbox=[496, 433, 648, 443]
2026-08-10 18:14:59,479 INFO     29 [qwen-vl-text] coord item[29]: text=MSI状态, bbox=[303, 452, 349, 462]
2026-08-10 18:14:59,479 INFO     29 [qwen-vl-text] coord item[30]: text=MSS (微卫星稳定), bbox=[496, 452, 596, 462]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[31]: text=其他潜在免疫疗效相关标志物2, bbox=[303, 487, 466, 497]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[32]: text=正相关：未检出, bbox=[496, 470, 579, 480]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[33]: text=负相关：未检出, bbox=[496, 487, 579, 497]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[34]: text=超进展相关：未检出, bbox=[496, 506, 603, 516]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[35]: text=化疗用药提示, bbox=[182, 533, 254, 543]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[36]: text=可能药物敏感性较高：暂无，详见实验结果, bbox=[303, 524, 532, 534]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[37]: text=可能毒副作用风险较低：卡培他滨，伊立替康, bbox=[303, 543, 544, 553]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[38]: text=肿瘤遗传风险提示, bbox=[182, 567, 278, 577]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[39]: text=检出APC p.L180Yfs*5疑似致病性变异，建议对受检者及血亲进行适当的遗传咨询或临床管理, bbox=[303, 562, 795, 572]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[40]: text=注：1. 基因变异, bbox=[175, 598, 263, 608]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[41]: text=58, bbox=[495, 713, 508, 720]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[42]: text=青岛市中心医疗集团, bbox=[690, 775, 791, 784]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[43]: text=(1) 体系变异参考AMP/ASCO/CAP 共识《Standards and Guidelines for the Interpretation and Reporting of, bbox=[223, 824, 793, 835]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[44]: text=Sequence Variants in Cancer》，基因变异按照临床意义的重要性分为四个类别, bbox=[247, 836, 665, 847]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[45]: text=I类：具有明确临床意义的变异，包括NMPA、FDA批准疗法，或专业临床指南（如CSCO诊疗指南、NCCN临, bbox=[247, 849, 811, 860]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[46]: text=床实践指南）推荐（A级证据），或基于证据充分的临床研究，并获得专家共识有明确治疗、诊断、预后的, bbox=[247, 861, 806, 872]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[47]: text=变异（B级证据）；, bbox=[247, 873, 345, 884]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[48]: text=II类：具有潜在临床意义的变异，包括其他癌种的A级证据（跨适应症用药），或多项小型临床研究支持，或, bbox=[247, 886, 813, 897]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[49]: text=已作为当前临床研究的入组标准（C级证据），或临床前研究或案例报道，未获得专家共识的药物（D级证, bbox=[247, 898, 803, 909]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[50]: text=据）；, bbox=[247, 910, 275, 921]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[51]: text=III类：临床意义不确定的变异（尚无相关临床证据）, bbox=[247, 923, 525, 934]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[52]: text=“类：下事或示能于事的变异（在全人群或特定人群数据库中观察到高变异率）, bbox=[247, 936, 672, 946]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] coord item[53]: text=扫描全能王 创建, bbox=[801, 962, 965, 978]
2026-08-10 18:14:59,480 INFO     29 [qwen-vl-text] page=4 — 54/54 coords, api_time=20.4s
2026-08-10 18:14:59,482 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1012563, prompt_len=2505
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共116行）
["青岛市中心医疗集团", "3.基因变异临床意义综合提示", "3.1诊断/预后及靶向药物提示", "基因变异1", "突变丰度2/拷贝数", "变异分类", "可能敏感药物", "可能耐药药物", "突变说明", "KRAS", "NM_004985.5", "12.81%", "I类", "司美替尼(C级)", "西妥昔单抗(A", "级)", "KRAS基因的G12D突变，发生在第", "2号外显子，位于GTP结合蛋白结", "构域(UniProt.org)，突变导致", "第12位氨基酸由甘氨酸变为天冬氨", "酸，G12突变将降低自身的GTP酶", "活性，使KRAS长期处于与GTP结", "合的激活状态，导致细胞增殖异常", "(PMID:12509763,20736745,2", "6037647,6092966)，为功能获", "得突变。", "exon2", "p.G12D", "c.35G>A", "Avutometinib a", "nd defactinib(C", "级)", "Pantitumuma", "b(A级)", "KRAS", "NM_004985.5", "1.46%", "I类", "Avutometinib a", "nd defactinib(C", "级)", "西妥昔单抗(A", "级)", "KRAS基因的A146V突变，发生在", "第4号外显子，突变导致146位氨基", "酸由丙氨酸变为缬氨酸，为功能获", "得突变。在两个不同的细胞系中，", "与野生型Kras相比，A146V可能会", "降低Kras的GTPase活性，从而导", "致下游通路激活增加(PMID:205", "70890)，与野生型Kras相比，A1", "46V突变会增加细胞增殖和细胞活", "力(PMID:29533785)，为功能", "获得突变。", "exon4", "p.A146V", "c.437C>T", "Panitumuma", "b(A级)", "TP53", "NM_000546.6", "12.73%", "II类", "AZD1775(C级)", "TP53基因的G245D突变，发生在", "第7号外显子，位于Tp53蛋白的D", "NA结合域(PMID:22713868)", "，突变导致245位甘氨酸变为天冬", "氨酸。G245D导致Tp53靶基因的", "激活减少(PMID:22214764,256", "34208,27533082)，为功能丧失", "突变。", "exon7", "p.G245D", "c.734G>A", "FBXW7", "NM_033632.3", "2.75%", "II类", "恩替司他(D级)", "FBXW7基因的R367*突变，发生在", "第7号外显子，突变导致终止密码", "子提前编码(UniProt.org)。由于W", "D重复域的丢失，预测R367*会导", "致Fbxw7蛋白功能的丢失(UniProt", ".org)。", "exon7", "p.R367*", "c.1099C>T", "Belinostat(D级)", "APC", "NM_000038.6", "杂合", "II类", "达沙替尼(D级)", "APC基因的p.L180Yfs*5、c.539de", "l突变，发生在第6外显子，不在已", "知功能域内(UniProt.org)，突", "变导致其编码的氨基酸在180位开", "始框移，可能影响蛋白功能(Uni", "Prot.org)。已知APC的功能丧失", "变异具有致病性(PMID:17963004", ",20685668)。Clinvar数据库记录", "该变异为Pathogenic。其在人群", "基因组数据库未收录。综上分析，", "该突变是一个疑似致病性变异。", "exon6", "p.L180Yfs*5", "c.539del", "厄洛替尼(D级)", "注:1.基因变异：“exon”为外显子，“intron”为内含子，“c”为DNA序列，“p”为蛋白质，“NM”为基因的转录", "本编号;", "2.突变丰度:在某位点产生突变的等位基因在该位点全部等位基因中所占比率。例如,突变丰度10%意为该位点含", "有10%的突变等位基因和90%的野生型等位基因。拷贝数:是指某一种基因或某一段特定的DNA序列在单倍体基", "因组中出现的数目。", "4/58"]

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
2026-08-10 18:15:34,323 INFO     29 [qwen-vl-text] coord API raw response (len=6758):
[
	{"text": "青岛市中心医疗集团", "bbox": [667, 31, 756, 39]},
	{"text": "3.基因变异临床意义综合提示", "bbox": [212, 75, 473, 91]},
	{"text": "3.1诊断/预后及靶向药物提示", "bbox": [212, 104, 420, 117]},
	{"text": "基因变异1", "bbox": [235, 135, 288, 144]},
	{"text": "突变丰度2/拷贝数", "bbox": [311, 132, 359, 148]},
	{"text": "变异分类", "bbox": [371, 135, 415, 144]},
	{"text": "可能敏感药物", "bbox": [437, 135, 501, 144]},
	{"text": "可能耐药药物", "bbox": [526, 135, 591, 144]},
	{"text": "突变说明", "bbox": [667, 135, 710, 144]},
	{"text": "KRAS", "bbox": [218, 185, 245, 193]},
	{"text": "NM_004985.5", "bbox": [218, 196, 287, 204]},
	{"text": "exon2", "bbox": [218, 207, 248, 215]},
	{"text": "p.G12D", "bbox": [218, 218, 255, 226]},
	{"text": "c.35G>A", "bbox": [218, 230, 259, 238]},
	{"text": "12.81%", "bbox": [309, 207, 348, 215]},
	{"text": "I类", "bbox": [371, 207, 386, 215]},
	{"text": "司美替尼(C级)", "bbox": [427, 185, 498, 193]},
	{"text": "Avutometinib a", "bbox": [427, 196, 506, 204]},
	{"text": "nd defactinib(C", "bbox": [427, 207, 508, 215]},
	{"text": "级)", "bbox": [427, 218, 442, 226]},
	{"text": "Salirasib(C级)", "bbox": [427, 230, 498, 238]},
	{"text": "西妥昔单抗(A", "bbox": [524, 190, 589, 198]},
	{"text": "级)", "bbox": [524, 201, 537, 209]},
	{"text": "Pantitumuma", "bbox": [524, 212, 589, 220]},
	{"text": "b(A级)", "bbox": [524, 223, 556, 232]},
	{"text": "KRAS基因的G12D突变，发生在第", "bbox": [608, 157, 768, 166]},
	{"text": "2号外显子，位于GTP结合蛋白结", "bbox": [608, 168, 764, 177]},
	{"text": "构域(UniProt.org)，突变导致", "bbox": [608, 179, 764, 188]},
	{"text": "第12位氨基酸由甘氨酸变为天冬氨", "bbox": [608, 190, 768, 199]},
	{"text": "酸，G12突变将降低自身的GTP酶", "bbox": [608, 201, 764, 210]},
	{"text": "活性，使KRAS长期处于与GTP结", "bbox": [608, 212, 762, 221]},
	{"text": "合的激活状态，导致细胞增殖异常", "bbox": [608, 223, 768, 232]},
	{"text": "(PMID:12509763,20736745,2", "bbox": [608, 234, 768, 243]},
	{"text": "6037647,6092966)，为功能获", "bbox": [608, 245, 768, 254]},
	{"text": "得突变。", "bbox": [608, 256, 646, 265]},
	{"text": "KRAS", "bbox": [218, 309, 245, 317]},
	{"text": "NM_004985.5", "bbox": [218, 320, 287, 328]},
	{"text": "exon4", "bbox": [218, 331, 248, 339]},
	{"text": "p.A146V", "bbox": [218, 343, 259, 351]},
	{"text": "c.437C>T", "bbox": [218, 354, 263, 362]},
	{"text": "1.46%", "bbox": [309, 331, 343, 339]},
	{"text": "I类", "bbox": [371, 331, 386, 339]},
	{"text": "Avutometinib a", "bbox": [427, 320, 506, 328]},
	{"text": "nd defactinib(C", "bbox": [427, 331, 508, 339]},
	{"text": "级)", "bbox": [427, 343, 442, 351]},
	{"text": "西妥昔单抗(A", "bbox": [524, 315, 589, 323]},
	{"text": "级)", "bbox": [524, 326, 537, 334]},
	{"text": "Panitumuma", "bbox": [524, 337, 589, 345]},
	{"text": "b(A级)", "bbox": [524, 348, 556, 357]},
	{"text": "KRAS基因的A146V突变，发生在", "bbox": [608, 275, 764, 284]},
	{"text": "第4号外显子，突变导致146位氨基", "bbox": [608, 286, 770, 295]},
	{"text": "酸由丙氨酸变为缬氨酸，为功能获", "bbox": [608, 297, 768, 306]},
	{"text": "得突变。在两个不同的细胞系中，", "bbox": [608, 308, 768, 317]},
	{"text": "与野生型Kras相比，A146V可能会", "bbox": [608, 319, 768, 328]},
	{"text": "降低Kras的GTPase活性，从而导", "bbox": [608, 330, 764, 339]},
	{"text": "致下游通路激活增加(PMID:205", "bbox": [608, 341, 770, 350]},
	{"text": "70890)，与野生型Kras相比，A1", "bbox": [608, 352, 770, 361]},
	{"text": "46V突变会增加细胞增殖和细胞活", "bbox": [608, 363, 764, 372]},
	{"text": "力(PMID:29533785)，为功能", "bbox": [608, 374, 768, 383]},
	{"text": "获得突变。", "bbox": [608, 385, 656, 394]},
	{"text": "TP53", "bbox": [218, 421, 244, 429]},
	{"text": "NM_000546.6", "bbox": [218, 432, 287, 440]},
	{"text": "exon7", "bbox": [218, 444, 248, 452]},
	{"text": "p.G245D", "bbox": [218, 455, 260, 463]},
	{"text": "c.734G>A", "bbox": [218, 466, 263, 474]},
	{"text": "12.73%", "bbox": [309, 444, 348, 452]},
	{"text": "II类", "bbox": [371, 444, 388, 452]},
	{"text": "AZD1775(C级)", "bbox": [427, 444, 500, 452]},
	{"text": "TP53基因的G245D突变，发生在", "bbox": [608, 404, 764, 413]},
	{"text": "第7号外显子，位于Tp53蛋白的D", "bbox": [608, 415, 764, 424]},
	{"text": "NA结合域(PMID:22713868)", "bbox": [608, 426, 760, 435]},
	{"text": "，突变导致245位甘氨酸变为天冬", "bbox": [608, 437, 764, 446]},
	{"text": "氨酸。G245D导致Tp53靶基因的", "bbox": [608, 448, 764, 457]},
	{"text": "激活减少(PMID:22214764,256", "bbox": [608, 459, 768, 468]},
	{"text": "34208,27533082)，为功能丧失", "bbox": [608, 470, 768, 479]},
	{"text": "突变。", "bbox": [608, 481, 634, 490]},
	{"text": "FBXW7", "bbox": [218, 504, 253, 512]},
	{"text": "NM_033632.3", "bbox": [218, 515, 287, 523]},
	{"text": "exon7", "bbox": [218, 526, 248, 534]},
	{"text": "p.R367*", "bbox": [218, 537, 258, 545]},
	{"text": "c.1099C>T", "bbox": [218, 548, 270, 556]},
	{"text": "2.75%", "bbox": [309, 526, 343, 534]},
	{"text": "II类", "bbox": [371, 526, 388, 534]},
	{"text": "恩替司他(D级)", "bbox": [427, 520, 498, 529]},
	{"text": "Belinostat(D级)", "bbox": [427, 531, 506, 540]},
	{"text": "FBXW7基因的R367*突变，发生在", "bbox": [608, 499, 768, 508]},
	{"text": "第7号外显子，突变导致终止密码", "bbox": [608, 510, 760, 519]},
	{"text": "子提前编码(UniProt.org)。由于W", "bbox": [608, 521, 770, 530]},
	{"text": "D重复域的丢失，预测R367*会导", "bbox": [608, 532, 764, 541]},
	{"text": "致Fbxw7蛋白功能的丢失(UniProt", "bbox": [608, 543, 770, 552]},
	{"text": ".org)。", "bbox": [608, 554, 636, 563]},
	{"text": "APC", "bbox": [218, 773, 239, 781]},
	{"text": "NM_000038.6", "bbox": [218, 784, 287, 792]},
	{"text": "exon6", "bbox": [218, 795, 248, 803]},
	{"text": "p.L180Yfs*5", "bbox": [218, 807, 278, 815]},
	{"text": "c.539del", "bbox": [218, 818, 260, 826]},
	{"text": "杂合", "bbox": [309, 795, 331, 803]},
	{"text": "II类", "bbox": [371, 795, 388, 803]},
	{"text": "达沙替尼(D级)", "bbox": [427, 790, 498, 799]},
	{"text": "厄洛替尼(D级)", "bbox": [427, 801, 498, 810]},
	{"text": "APC基因的p.L180Yfs*5、c.539de", "bbox": [608, 738, 770, 747]},
	{"text": "l突变，发生在第6外显子，不在已", "bbox": [608, 749, 764, 758]},
	{"text": "知功能域内(UniProt.org)，突", "bbox": [608, 760, 764, 769]},
	{"text": "变导致其编码的氨基酸在180位开", "bbox": [608, 771, 764, 780]},
	{"text": "始框移，可能影响蛋白功能(Uni", "bbox": [608, 782, 764, 791]},
	{"text": "Prot.org)。已知APC的功能丧失", "bbox": [608, 793, 764, 802]},
	{"text": "变异具有致病性(PMID:17963004", "bbox": [608, 804, 768, 813]},
	{"text": ",20685668)。Clinvar数据库记录", "bbox": [608, 815, 764, 824]},
	{"text": "该变异为Pathogenic。其在人群", "bbox": [608, 826, 764, 835]},
	{"text": "基因组数据库未收录。综上分析，", "bbox": [608, 837, 764, 846]},
	{"text": "该突变是一个疑似致病性变异。", "bbox": [608, 848, 756, 857]},
	{"text": "注:1.基因变异：“exon”为外显子，“intron”为内含子，“c”为DNA序列，“p”为蛋白质，“NM”为基因的转录", "bbox": [212, 871, 776, 880]},
	{"text": "本编号;", "bbox": [248, 882, 287, 891]},
	{"text": "2.突变丰度:在某位点产生突变的等位基因在该位点全部等位基因中所占比率。例如,突变丰度10%意为该位点含", "bbox": [233, 893, 768, 902]},
	{"text": "有10%的突变等位基因和90%的野生型等位基因。拷贝数:是指某一种基因或某一段特定的DNA序列在单倍体基", "bbox": [248, 904, 768, 913]},
	{"text": "因组中出现的数目。", "bbox": [248, 915, 343, 924]},
	{"text": "4/58", "bbox": [483, 638, 506, 645]},
	{"text": "青岛市中心医疗集团", "bbox": [667, 692, 756, 700]}
]
2026-08-10 18:15:34,323 INFO     29 [qwen-vl-text] coord API: raw_items=118, valid_items=118, elapsed=34.8s
2026-08-10 18:15:34,323 INFO     29 [qwen-vl-text] coord item[0]: text=青岛市中心医疗集团, bbox=[667, 31, 756, 39]
2026-08-10 18:15:34,324 INFO     29 [qwen-vl-text] coord item[1]: text=3.基因变异临床意义综合提示, bbox=[212, 75, 473, 91]
2026-08-10 18:15:34,324 INFO     29 [qwen-vl-text] coord item[2]: text=3.1诊断/预后及靶向药物提示, bbox=[212, 104, 420, 117]
2026-08-10 18:15:34,324 INFO     29 [qwen-vl-text] coord item[3]: text=基因变异1, bbox=[235, 135, 288, 144]
2026-08-10 18:15:34,324 INFO     29 [qwen-vl-text] coord item[4]: text=突变丰度2/拷贝数, bbox=[311, 132, 359, 148]
2026-08-10 18:15:34,324 INFO     29 [qwen-vl-text] coord item[5]: text=变异分类, bbox=[371, 135, 415, 144]
2026-08-10 18:15:34,324 INFO     29 [qwen-vl-text] coord item[6]: text=可能敏感药物, bbox=[437, 135, 501, 144]
2026-08-10 18:15:34,324 INFO     29 [qwen-vl-text] coord item[7]: text=可能耐药药物, bbox=[526, 135, 591, 144]
2026-08-10 18:15:34,324 INFO     29 [qwen-vl-text] coord item[8]: text=突变说明, bbox=[667, 135, 710, 144]
2026-08-10 18:15:34,324 INFO     29 [qwen-vl-text] coord item[9]: text=KRAS, bbox=[218, 185, 245, 193]
2026-08-10 18:15:34,324 INFO     29 [qwen-vl-text] coord item[10]: text=NM_004985.5, bbox=[218, 196, 287, 204]
2026-08-10 18:15:34,324 INFO     29 [qwen-vl-text] coord item[11]: text=exon2, bbox=[218, 207, 248, 215]
2026-08-10 18:15:34,324 INFO     29 [qwen-vl-text] coord item[12]: text=p.G12D, bbox=[218, 218, 255, 226]
2026-08-10 18:15:34,324 INFO     29 [qwen-vl-text] coord item[13]: text=c.35G>A, bbox=[218, 230, 259, 238]
2026-08-10 18:15:34,324 INFO     29 [qwen-vl-text] coord item[14]: text=12.81%, bbox=[309, 207, 348, 215]
2026-08-10 18:15:34,324 INFO     29 [qwen-vl-text] coord item[15]: text=I类, bbox=[371, 207, 386, 215]
2026-08-10 18:15:34,324 INFO     29 [qwen-vl-text] coord item[16]: text=司美替尼(C级), bbox=[427, 185, 498, 193]
2026-08-10 18:15:34,324 INFO     29 [qwen-vl-text] coord item[17]: text=Avutometinib a, bbox=[427, 196, 506, 204]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[18]: text=nd defactinib(C, bbox=[427, 207, 508, 215]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[19]: text=级), bbox=[427, 218, 442, 226]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[20]: text=Salirasib(C级), bbox=[427, 230, 498, 238]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[21]: text=西妥昔单抗(A, bbox=[524, 190, 589, 198]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[22]: text=级), bbox=[524, 201, 537, 209]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[23]: text=Pantitumuma, bbox=[524, 212, 589, 220]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[24]: text=b(A级), bbox=[524, 223, 556, 232]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[25]: text=KRAS基因的G12D突变，发生在第, bbox=[608, 157, 768, 166]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[26]: text=2号外显子，位于GTP结合蛋白结, bbox=[608, 168, 764, 177]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[27]: text=构域(UniProt.org)，突变导致, bbox=[608, 179, 764, 188]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[28]: text=第12位氨基酸由甘氨酸变为天冬氨, bbox=[608, 190, 768, 199]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[29]: text=酸，G12突变将降低自身的GTP酶, bbox=[608, 201, 764, 210]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[30]: text=活性，使KRAS长期处于与GTP结, bbox=[608, 212, 762, 221]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[31]: text=合的激活状态，导致细胞增殖异常, bbox=[608, 223, 768, 232]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[32]: text=(PMID:12509763,20736745,2, bbox=[608, 234, 768, 243]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[33]: text=6037647,6092966)，为功能获, bbox=[608, 245, 768, 254]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[34]: text=得突变。, bbox=[608, 256, 646, 265]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[35]: text=KRAS, bbox=[218, 309, 245, 317]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[36]: text=NM_004985.5, bbox=[218, 320, 287, 328]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[37]: text=exon4, bbox=[218, 331, 248, 339]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[38]: text=p.A146V, bbox=[218, 343, 259, 351]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[39]: text=c.437C>T, bbox=[218, 354, 263, 362]
2026-08-10 18:15:34,325 INFO     29 [qwen-vl-text] coord item[40]: text=1.46%, bbox=[309, 331, 343, 339]
2026-08-10 18:15:34,326 INFO     29 [qwen-vl-text] coord item[41]: text=I类, bbox=[371, 331, 386, 339]
2026-08-10 18:15:34,326 INFO     29 [qwen-vl-text] coord item[42]: text=Avutometinib a, bbox=[427, 320, 506, 328]
2026-08-10 18:15:34,326 INFO     29 [qwen-vl-text] coord item[43]: text=nd defactinib(C, bbox=[427, 331, 508, 339]
2026-08-10 18:15:34,326 INFO     29 [qwen-vl-text] coord item[44]: text=级), bbox=[427, 343, 442, 351]
2026-08-10 18:15:34,326 INFO     29 [qwen-vl-text] coord item[45]: text=西妥昔单抗(A, bbox=[524, 315, 589, 323]
2026-08-10 18:15:34,326 INFO     29 [qwen-vl-text] coord item[46]: text=级), bbox=[524, 326, 537, 334]
2026-08-10 18:15:34,326 INFO     29 [qwen-vl-text] coord item[47]: text=Panitumuma, bbox=[524, 337, 589, 345]
2026-08-10 18:15:34,326 INFO     29 [qwen-vl-text] coord item[48]: text=b(A级), bbox=[524, 348, 556, 357]
2026-08-10 18:15:34,326 INFO     29 [qwen-vl-text] coord item[49]: text=KRAS基因的A146V突变，发生在, bbox=[608, 275, 764, 284]
2026-08-10 18:15:34,326 INFO     29 [qwen-vl-text] coord item[50]: text=第4号外显子，突变导致146位氨基, bbox=[608, 286, 770, 295]
2026-08-10 18:15:34,326 INFO     29 [qwen-vl-text] coord item[51]: text=酸由丙氨酸变为缬氨酸，为功能获, bbox=[608, 297, 768, 306]
2026-08-10 18:15:34,326 INFO     29 [qwen-vl-text] coord item[52]: text=得突变。在两个不同的细胞系中，, bbox=[608, 308, 768, 317]
2026-08-10 18:15:34,326 INFO     29 [qwen-vl-text] coord item[53]: text=与野生型Kras相比，A146V可能会, bbox=[608, 319, 768, 328]
2026-08-10 18:15:34,326 INFO     29 [qwen-vl-text] coord item[54]: text=降低Kras的GTPase活性，从而导, bbox=[608, 330, 764, 339]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[55]: text=致下游通路激活增加(PMID:205, bbox=[608, 341, 770, 350]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[56]: text=70890)，与野生型Kras相比，A1, bbox=[608, 352, 770, 361]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[57]: text=46V突变会增加细胞增殖和细胞活, bbox=[608, 363, 764, 372]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[58]: text=力(PMID:29533785)，为功能, bbox=[608, 374, 768, 383]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[59]: text=获得突变。, bbox=[608, 385, 656, 394]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[60]: text=TP53, bbox=[218, 421, 244, 429]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[61]: text=NM_000546.6, bbox=[218, 432, 287, 440]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[62]: text=exon7, bbox=[218, 444, 248, 452]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[63]: text=p.G245D, bbox=[218, 455, 260, 463]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[64]: text=c.734G>A, bbox=[218, 466, 263, 474]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[65]: text=12.73%, bbox=[309, 444, 348, 452]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[66]: text=II类, bbox=[371, 444, 388, 452]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[67]: text=AZD1775(C级), bbox=[427, 444, 500, 452]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[68]: text=TP53基因的G245D突变，发生在, bbox=[608, 404, 764, 413]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[69]: text=第7号外显子，位于Tp53蛋白的D, bbox=[608, 415, 764, 424]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[70]: text=NA结合域(PMID:22713868), bbox=[608, 426, 760, 435]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[71]: text=，突变导致245位甘氨酸变为天冬, bbox=[608, 437, 764, 446]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[72]: text=氨酸。G245D导致Tp53靶基因的, bbox=[608, 448, 764, 457]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[73]: text=激活减少(PMID:22214764,256, bbox=[608, 459, 768, 468]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[74]: text=34208,27533082)，为功能丧失, bbox=[608, 470, 768, 479]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[75]: text=突变。, bbox=[608, 481, 634, 490]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[76]: text=FBXW7, bbox=[218, 504, 253, 512]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[77]: text=NM_033632.3, bbox=[218, 515, 287, 523]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[78]: text=exon7, bbox=[218, 526, 248, 534]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[79]: text=p.R367*, bbox=[218, 537, 258, 545]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[80]: text=c.1099C>T, bbox=[218, 548, 270, 556]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[81]: text=2.75%, bbox=[309, 526, 343, 534]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[82]: text=II类, bbox=[371, 526, 388, 534]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[83]: text=恩替司他(D级), bbox=[427, 520, 498, 529]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[84]: text=Belinostat(D级), bbox=[427, 531, 506, 540]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[85]: text=FBXW7基因的R367*突变，发生在, bbox=[608, 499, 768, 508]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[86]: text=第7号外显子，突变导致终止密码, bbox=[608, 510, 760, 519]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[87]: text=子提前编码(UniProt.org)。由于W, bbox=[608, 521, 770, 530]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[88]: text=D重复域的丢失，预测R367*会导, bbox=[608, 532, 764, 541]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[89]: text=致Fbxw7蛋白功能的丢失(UniProt, bbox=[608, 543, 770, 552]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[90]: text=.org)。, bbox=[608, 554, 636, 563]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[91]: text=APC, bbox=[218, 773, 239, 781]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[92]: text=NM_000038.6, bbox=[218, 784, 287, 792]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[93]: text=exon6, bbox=[218, 795, 248, 803]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[94]: text=p.L180Yfs*5, bbox=[218, 807, 278, 815]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[95]: text=c.539del, bbox=[218, 818, 260, 826]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[96]: text=杂合, bbox=[309, 795, 331, 803]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[97]: text=II类, bbox=[371, 795, 388, 803]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[98]: text=达沙替尼(D级), bbox=[427, 790, 498, 799]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[99]: text=厄洛替尼(D级), bbox=[427, 801, 498, 810]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[100]: text=APC基因的p.L180Yfs*5、c.539de, bbox=[608, 738, 770, 747]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[101]: text=l突变，发生在第6外显子，不在已, bbox=[608, 749, 764, 758]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[102]: text=知功能域内(UniProt.org)，突, bbox=[608, 760, 764, 769]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[103]: text=变导致其编码的氨基酸在180位开, bbox=[608, 771, 764, 780]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[104]: text=始框移，可能影响蛋白功能(Uni, bbox=[608, 782, 764, 791]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[105]: text=Prot.org)。已知APC的功能丧失, bbox=[608, 793, 764, 802]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[106]: text=变异具有致病性(PMID:17963004, bbox=[608, 804, 768, 813]
2026-08-10 18:15:34,327 INFO     29 [qwen-vl-text] coord item[107]: text=,20685668)。Clinvar数据库记录, bbox=[608, 815, 764, 824]
2026-08-10 18:15:34,328 INFO     29 [qwen-vl-text] coord item[108]: text=该变异为Pathogenic。其在人群, bbox=[608, 826, 764, 835]
2026-08-10 18:15:34,328 INFO     29 [qwen-vl-text] coord item[109]: text=基因组数据库未收录。综上分析，, bbox=[608, 837, 764, 846]
2026-08-10 18:15:34,328 INFO     29 [qwen-vl-text] coord item[110]: text=该突变是一个疑似致病性变异。, bbox=[608, 848, 756, 857]
2026-08-10 18:15:34,328 INFO     29 [qwen-vl-text] coord item[111]: text=注:1.基因变异：“exon”为外显子，“intron”为内含子，“c”为DNA序列，“p”为蛋白质，“NM”为基因的转录, bbox=[212, 871, 776, 880]
2026-08-10 18:15:34,328 INFO     29 [qwen-vl-text] coord item[112]: text=本编号;, bbox=[248, 882, 287, 891]
2026-08-10 18:15:34,328 INFO     29 [qwen-vl-text] coord item[113]: text=2.突变丰度:在某位点产生突变的等位基因在该位点全部等位基因中所占比率。例如,突变丰度10%意为该位点含, bbox=[233, 893, 768, 902]
2026-08-10 18:15:34,328 INFO     29 [qwen-vl-text] coord item[114]: text=有10%的突变等位基因和90%的野生型等位基因。拷贝数:是指某一种基因或某一段特定的DNA序列在单倍体基, bbox=[248, 904, 768, 913]
2026-08-10 18:15:34,328 INFO     29 [qwen-vl-text] coord item[115]: text=因组中出现的数目。, bbox=[248, 915, 343, 924]
2026-08-10 18:15:34,328 INFO     29 [qwen-vl-text] coord item[116]: text=4/58, bbox=[483, 638, 506, 645]
2026-08-10 18:15:34,328 INFO     29 [qwen-vl-text] coord item[117]: text=青岛市中心医疗集团, bbox=[667, 692, 756, 700]
2026-08-10 18:15:34,328 INFO     29 [qwen-vl-text] page=5 — 116/116 coords, api_time=34.8s
2026-08-10 18:15:34,328 INFO     29 [qwen-vl-text] new_positions (170):
[[4, 410.54999999999995, 470.645, 21.892, 29.47], [4, 104.125, 199.325, 64.834, 79.148], [4, 104.125, 482.54499999999996, 92.61999999999999, 101.88199999999999], [4, 104.125, 484.33, 101.88199999999999, 111.14399999999999], [4, 104.125, 186.82999999999998, 111.14399999999999, 119.564], [4, 125.54499999999999, 154.105, 133.036, 141.456], [4, 314.755, 343.90999999999997, 133.036, 141.456], [4, 108.28999999999999, 140.42, 181.87199999999999, 190.292], [4, 180.285, 195.16, 175.136, 183.55599999999998], [4, 221.935, 432.565, 149.034, 157.454], [4, 221.935, 440.895, 165.03199999999998, 173.452], [4, 221.935, 478.38, 190.292, 199.554], [4, 221.935, 385.56, 199.554, 208.816], [4, 180.285, 195.16, 217.236, 225.656], [4, 221.935, 359.38, 217.236, 225.656], [4, 108.28999999999999, 151.13, 275.334, 283.75399999999996], [4, 180.285, 472.43, 232.392, 241.654], [4, 180.285, 477.78499999999997, 258.49399999999997, 266.914], [4, 180.285, 267.75, 266.914, 276.176], [4, 180.285, 329.63, 285.438, 293.858], [4, 180.285, 395.08, 302.27799999999996, 310.698], [4, 180.285, 391.51, 317.43399999999997, 325.854], [4, 108.28999999999999, 154.105, 332.59, 341.01], [4, 180.285, 337.365, 332.59, 341.01], [4, 108.28999999999999, 165.41, 387.32, 395.74], [4, 180.285, 270.72499999999997, 348.58799999999997, 357.008], [4, 295.12, 342.71999999999997, 348.58799999999997, 357.008], [4, 180.285, 236.81, 364.586, 373.006], [4, 295.12, 385.56, 364.586, 373.006], [4, 180.285, 207.655, 380.584, 389.00399999999996], [4, 295.12, 354.62, 380.584, 389.00399999999996], [4, 180.285, 277.27, 410.054, 418.474], [4, 295.12, 344.505, 395.74, 404.15999999999997], [4, 295.12, 344.505, 410.054, 418.474], [4, 295.12, 358.78499999999997, 426.05199999999996, 434.472], [4, 108.28999999999999, 151.13, 448.786, 457.20599999999996], [4, 180.285, 316.53999999999996, 441.20799999999997, 449.628], [4, 180.285, 323.68, 457.20599999999996, 465.626], [4, 108.28999999999999, 165.41, 477.414, 485.834], [4, 180.285, 473.025, 473.204, 481.62399999999997], [4, 104.125, 156.48499999999999, 503.51599999999996, 511.936], [4, 294.525, 302.26, 600.346, 606.24], [4, 410.54999999999995, 470.645, 652.55, 660.1279999999999], [4, 132.685, 471.835, 693.808, 703.0699999999999], [4, 146.965, 395.67499999999995, 703.9119999999999, 713.174], [4, 146.965, 482.54499999999996, 714.858, 724.12], [4, 146.965, 479.57, 724.962, 734.2239999999999], [4, 146.965, 205.27499999999998, 735.066, 744.328], [4, 146.965, 483.73499999999996, 746.012, 755.274], [4, 146.965, 477.78499999999997, 756.116, 765.3779999999999], [4, 146.965, 163.625, 766.22, 775.482], [4, 146.965, 312.375, 777.1659999999999, 786.428], [4, 146.965, 399.84, 788.112, 796.5319999999999], [4, 476.59499999999997, 574.175, 810.004, 823.476], [5, 396.865, 449.82, 26.102, 32.838], [5, 126.14, 281.435, 63.15, 76.622], [5, 126.14, 249.89999999999998, 87.568, 98.514], [5, 139.825, 171.35999999999999, 113.67, 121.24799999999999], [5, 185.045, 213.605, 111.14399999999999, 124.616], [5, 220.74499999999998, 246.92499999999998, 113.67, 121.24799999999999], [5, 260.015, 298.09499999999997, 113.67, 121.24799999999999], [5, 312.96999999999997, 351.645, 113.67, 121.24799999999999], [5, 396.865, 422.45, 113.67, 121.24799999999999], [5, 129.71, 145.775, 155.76999999999998, 162.506], [5, 129.71, 170.765, 165.03199999999998, 171.768], [5, 129.71, 147.56, 174.29399999999998, 181.03], [5, 129.71, 151.725, 183.55599999999998, 190.292], [5, 129.71, 154.105, 193.66, 200.396], [5, 183.855, 207.06, 174.29399999999998, 181.03], [5, 220.74499999999998, 229.67, 174.29399999999998, 181.03], [5, 254.065, 296.31, 155.76999999999998, 162.506], [5, 254.065, 301.07, 165.03199999999998, 171.768], [5, 254.065, 302.26, 174.29399999999998, 181.03], [5, 254.065, 262.99, 183.55599999999998, 190.292], [5, 254.065, 296.31, 193.66, 200.396], [5, 311.78, 350.455, 159.98, 166.716], [5, 311.78, 319.515, 169.242, 175.97799999999998], [5, 311.78, 350.455, 178.504, 185.23999999999998], [5, 311.78, 330.82, 187.766, 195.344], [5, 361.76, 456.96, 132.194, 139.772], [5, 361.76, 454.58, 141.456, 149.034], [5, 361.76, 454.58, 150.718, 158.296], [5, 361.76, 456.96, 159.98, 167.558], [5, 361.76, 454.58, 169.242, 176.82], [5, 361.76, 453.39, 178.504, 186.082], [5, 361.76, 456.96, 187.766, 195.344], [5, 361.76, 456.96, 197.028, 204.606], [5, 361.76, 456.96, 206.29, 213.868], [5, 361.76, 384.37, 215.552, 223.13], [5, 129.71, 145.775, 260.178, 266.914], [5, 129.71, 170.765, 269.44, 276.176], [5, 129.71, 147.56, 278.702, 285.438], [5, 129.71, 154.105, 288.806, 295.542], [5, 129.71, 156.48499999999999, 298.068, 304.804], [5, 183.855, 204.08499999999998, 278.702, 285.438], [5, 220.74499999999998, 229.67, 278.702, 285.438], [5, 254.065, 301.07, 269.44, 276.176], [5, 254.065, 302.26, 278.702, 285.438], [5, 254.065, 262.99, 288.806, 295.542], [5, 311.78, 350.455, 265.23, 271.966], [5, 311.78, 319.515, 274.492, 281.228], [5, 311.78, 350.455, 283.75399999999996, 290.49], [5, 311.78, 330.82, 293.01599999999996, 300.594], [5, 361.76, 454.58, 231.54999999999998, 239.128], [5, 361.76, 458.15, 240.81199999999998, 248.39], [5, 361.76, 456.96, 250.07399999999998, 257.652], [5, 361.76, 456.96, 259.336, 266.914], [5, 361.76, 456.96, 268.598, 276.176], [5, 361.76, 454.58, 277.86, 285.438], [5, 361.76, 458.15, 287.122, 294.7], [5, 361.76, 458.15, 296.384, 303.962], [5, 361.76, 454.58, 305.646, 313.224], [5, 361.76, 456.96, 314.908, 322.486], [5, 361.76, 390.32, 324.17, 331.748], [5, 129.71, 145.18, 354.48199999999997, 361.21799999999996], [5, 129.71, 170.765, 363.74399999999997, 370.47999999999996], [5, 129.71, 147.56, 373.848, 380.584], [5, 129.71, 154.7, 383.11, 389.846], [5, 129.71, 156.48499999999999, 392.372, 399.108], [5, 183.855, 207.06, 373.848, 380.584], [5, 220.74499999999998, 230.85999999999999, 373.848, 380.584], [5, 254.065, 297.5, 373.848, 380.584], [5, 361.76, 454.58, 340.168, 347.746], [5, 361.76, 454.58, 349.43, 357.008], [5, 361.76, 452.2, 358.692, 366.27], [5, 361.76, 454.58, 367.954, 375.532], [5, 361.76, 454.58, 377.216, 384.794], [5, 361.76, 456.96, 386.478, 394.056], [5, 361.76, 456.96, 395.74, 403.318], [5, 361.76, 377.22999999999996, 405.002, 412.58], [5, 129.71, 150.535, 424.368, 431.104], [5, 129.71, 170.765, 433.63, 440.366], [5, 129.71, 147.56, 442.892, 449.628], [5, 129.71, 153.51, 452.154, 458.89], [5, 129.71, 160.65, 461.416, 468.152], [5, 183.855, 204.08499999999998, 442.892, 449.628], [5, 220.74499999999998, 230.85999999999999, 442.892, 449.628], [5, 254.065, 296.31, 437.84, 445.418], [5, 254.065, 301.07, 447.102, 454.68], [5, 361.76, 456.96, 420.15799999999996, 427.736], [5, 361.76, 452.2, 429.41999999999996, 436.998], [5, 361.76, 458.15, 438.68199999999996, 446.26], [5, 361.76, 454.58, 447.94399999999996, 455.522], [5, 361.76, 458.15, 457.20599999999996, 464.784], [5, 361.76, 378.41999999999996, 466.46799999999996, 474.046], [5, 129.71, 142.20499999999998, 650.866, 657.602], [5, 129.71, 170.765, 660.1279999999999, 666.864], [5, 129.71, 147.56, 669.39, 676.126], [5, 129.71, 165.41, 679.494, 686.23], [5, 129.71, 154.7, 688.756, 695.492], [5, 183.855, 196.945, 669.39, 676.126], [5, 220.74499999999998, 230.85999999999999, 669.39, 676.126], [5, 254.065, 296.31, 665.18, 672.7579999999999], [5, 254.065, 296.31, 674.442, 682.02], [5, 361.76, 458.15, 621.396, 628.9739999999999], [5, 361.76, 454.58, 630.658, 638.236], [5, 361.76, 454.58, 639.92, 647.4979999999999], [5, 361.76, 454.58, 649.182, 656.76], [5, 361.76, 454.58, 658.444, 666.0219999999999], [5, 361.76, 454.58, 667.706, 675.284], [5, 361.76, 456.96, 676.968, 684.5459999999999], [5, 361.76, 454.58, 686.23, 693.808], [5, 361.76, 454.58, 695.492, 703.0699999999999], [5, 361.76, 454.58, 704.754, 712.332], [5, 361.76, 449.82, 714.016, 721.5939999999999], [5, 126.14, 461.71999999999997, 733.382, 740.9599999999999], [5, 147.56, 170.765, 742.644, 750.222], [5, 138.635, 456.96, 751.906, 759.4839999999999], [5, 147.56, 456.96, 761.168, 768.746], [5, 147.56, 204.08499999999998, 770.43, 778.0079999999999]]
2026-08-10 18:15:34,328 INFO     29 [qwen-vl-text] ═══ DONE ═══ 170 positions, pages=2, time=73.9s
2026-08-10 18:15:34,329 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:15:34,336 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:15:34,336 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 18:15:34,336 INFO     29 [qwen-vl-text] positions(64): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:15:34,336 INFO     29 [qwen-vl-text] page grouping: [6, 7], lines per page: [33, 31]
2026-08-10 18:15:34,506 INFO     29 [qwen-vl-text] page=6, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 18:15:34,702 INFO     29 [qwen-vl-text] page=7, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 18:15:34,703 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1121
2026-08-10 18:15:34,703 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:15:34,703 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 308, \"bbox_end\": 371, \"encounter_dates\": [\"2026-03-07\"], \"department\": \"放射科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "报告单详情\nwww.jkqd.org.cn\n20260307检\n查\n1.双肺多发结节，较前2025-12-26部分缩\n小，考虑转移；/>右肺门区及纵隔内多发肿\n大淋巴结，考虑转移2.直肠术后，吻合区软\n组织影，考虑肿瘤复发，与前列腺分界不\n清，大致同前（2025-10-16）；/>直肠周\n围、右腹膜后、骶前区多发淋巴结转移，部\n分较前略缩小，建议复查3.肝内多发转移\n瘤，较前（2025-10-16）进展4.肝囊肿5.\n膀胱内气体，建议结合临床\n诊断意见\n骨性胸廓对称，纵隔气管居中。双肺支气管\n血管束增多。双肺见弥漫多发类圆形实性结\n节影，大者位于右肺下叶内基底段（薄层\nIM181），大小约为16×16mm，边界清，轻\n度均匀强化。气管及中心支气管通畅。右肺\n门区及纵隔内多发肿大淋巴结，最大者短径\n约14mm，轻度强化。心脏不大。双侧胸膜\n未见明显增厚。双侧胸腔内未见明显液体密\n度影。肝脏增大，肝内见多发类圆形稍低密\n度影，边界不清，大者长径约110mm，增强\n扫描边缘轻度强化。肝右叶可见直径3mm的\n无强化的囊性密度灶，边界清；/>肝内外胆\n管未见明显扩张。胆囊内未见异常密度影。\n胰腺、脾脏未见明显异常密度灶及异常强化\n灶。双肾上腺及双肾大小、形态、密度未见\n明显异常密度灶及异常强化灶。肠管未见梗\n阻征象。直肠术后直肠吻合口区见团片样\n>\n扫描全能王 创建\n19:08\n41\n×\n报告单详情\nwww.jkqd.org.cn\n瘤，较前（2025-10-16）进展 4. 肝囊肿 5.\n膀胱内气体，建议结合临床\n诊断意见\n骨性胸廓对称，纵隔气管居中。双肺支气管\n血管束增多。双肺见弥漫多发类圆形实性结\n节影，大者位于右肺下叶内基底段（薄层\nIM181），大小约为16×16mm，边界清，轻\n度均匀强化。气管及中心支气管通畅。右肺\n门区及纵隔内多发肿大淋巴结，最大者短径\n约14mm，轻度强化。心脏不大。双侧胸膜\n未见明显增厚。双侧胸腔内未见明显液体密\n度影。肝脏增大，肝内见多发类圆形稍低密\n度影，边界不清，大者长径约110mm，增强\n扫描边缘轻度强化。肝右叶可见直径3mm的\n无强化的囊性密度灶，边界清； />肝内外胆\n管未见明显扩张。胆囊内未见异常密度影。\n胰腺、脾脏未见明显异常密度灶及异常强化\n灶。双肾上腺及双肾大小、形态、密度未见\n明显异常密度灶及异常强化灶。肠管未见梗\n阻征象。直肠术后，直肠吻合口区见团片样\n软组织密度影，与前列腺分界不清，增强扫\n描不均匀强化。直肠周围、右腹膜后、骶前\n区见多发肿大淋巴结，大者短径约11mm，\n增强扫描不均匀强化。膀胱充盈良好，膀胱\n壁光整，膀胱内见气体影。盆腔未见明显积\n液。",
    "role": "user"
  }
]
2026-08-10 18:15:34,705 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:15:34.704+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 85, "failed": 0, "current": {"a677452e94e611f1bd9827cf206dfa2d": {"id": "a677452e94e611f1bd9827cf206dfa2d", "doc_id": "a646f41e94e611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 11495294, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385378144, "task_type": "dataflow", "root_trace_id": "971de7c4c0604c27afceabc8ac295233", "root_traceparent": "00-971de7c4c0604c27afceabc8ac295233-de3f877b239fe0d8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:15:40,389 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:15:40,389 INFO     29 [qwen-vl-text] LLM output (len=940):
{
  "exam_date": "2026-03-07",
  "report_date": "2026-03-07",
  "exam_name": "胸部+腹部+盆腔CT平扫+增强",
  "exam_category": "imaging",
  "body_part": "胸部、腹部、盆腔",
  "patient_name": null,
  "patient_gender": null,
  "department": "放射科",
  "bed_number": null,
  "findings": "骨性胸廓对称，纵隔气管居中。双肺支气管血管束增多。双肺见弥漫多发类圆形实性结节影，大者位于右肺下叶内基底段（薄层IM181），大小约为16×16mm，边界清，轻度均匀强化。气管及中心支气管通畅。右肺门区及纵隔内多发肿大淋巴结，最大者短径约14mm，轻度强化。心脏不大。双侧胸膜未见明显增厚。双侧胸腔内未见明显液体密度影。肝脏增大，肝内见多发类圆形稍低密度影，边界不清，大者长径约110mm，增强扫描边缘轻度强化。肝右叶可见直径3mm的无强化的囊性密度灶，边界清；肝内外胆管未见明显扩张。胆囊内未见异常密度影。胰腺、脾脏未见明显异常密度灶及异常强化灶。双肾上腺及双肾大小、形态、密度未见明显异常密度灶及异常强化灶。肠管未见梗阻征象。直肠术后，直肠吻合口区见团片样软组织密度影，与前列腺分界不清，增强扫描不均匀强化。直肠周围、右腹膜后、骶前区见多发肿大淋巴结，大者短径约11mm，增强扫描不均匀强化。膀胱充盈良好，膀胱壁光整，膀胱内见气体影。盆腔未见明显积液。",
  "conclusion": "1.双肺多发结节，较前2025-12-26部分缩小，考虑转移；右肺门区及纵隔内多发肿大淋巴结，考虑转移\n2.直肠术后，吻合区软组织影，考虑肿瘤复发，与前列腺分界不清，大致同前（2025-10-16）；直肠周围、右腹膜后、骶前区多发淋巴结转移，部分较前略缩小，建议复查\n3.肝内多发转移瘤，较前（2025-10-16）进展\n4.肝囊肿\n5.膀胱内气体，建议结合临床",
  "physician": null,
  "reviewer": null
}
2026-08-10 18:15:40,391 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1054967, prompt_len=1299
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["报告单详情", "www.jkqd.org.cn", "20260307检", "查", "1.双肺多发结节，较前2025-12-26部分缩", "小，考虑转移；/>右肺门区及纵隔内多发肿", "大淋巴结，考虑转移2.直肠术后，吻合区软", "组织影，考虑肿瘤复发，与前列腺分界不", "清，大致同前（2025-10-16）；/>直肠周", "围、右腹膜后、骶前区多发淋巴结转移，部", "分较前略缩小，建议复查3.肝内多发转移", "瘤，较前（2025-10-16）进展4.肝囊肿5.", "膀胱内气体，建议结合临床", "诊断意见", "骨性胸廓对称，纵隔气管居中。双肺支气管", "血管束增多。双肺见弥漫多发类圆形实性结", "节影，大者位于右肺下叶内基底段（薄层", "IM181），大小约为16×16mm，边界清，轻", "度均匀强化。气管及中心支气管通畅。右肺", "门区及纵隔内多发肿大淋巴结，最大者短径", "约14mm，轻度强化。心脏不大。双侧胸膜", "未见明显增厚。双侧胸腔内未见明显液体密", "度影。肝脏增大，肝内见多发类圆形稍低密", "度影，边界不清，大者长径约110mm，增强", "扫描边缘轻度强化。肝右叶可见直径3mm的", "无强化的囊性密度灶，边界清；/>肝内外胆", "管未见明显扩张。胆囊内未见异常密度影。", "胰腺、脾脏未见明显异常密度灶及异常强化", "灶。双肾上腺及双肾大小、形态、密度未见", "明显异常密度灶及异常强化灶。肠管未见梗", "阻征象。直肠术后直肠吻合口区见团片样", ">", "扫描全能王 创建"]

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
2026-08-10 18:15:51,355 INFO     29 [qwen-vl-text] coord API raw response (len=2035):
[
	{"text": "报告单详情", "bbox": [432, 60, 566, 81]},
	{"text": "www.jkqd.org.cn", "bbox": [434, 83, 566, 95]},
	{"text": "20260307检", "bbox": [585, 67, 721, 84]},
	{"text": "查", "bbox": [585, 90, 611, 108]},
	{"text": "1.双肺多发结节，较前2025-12-26部分缩", "bbox": [250, 119, 713, 138]},
	{"text": "小，考虑转移；/>右肺门区及纵隔内多发肿", "bbox": [250, 144, 736, 164]},
	{"text": "大淋巴结，考虑转移2.直肠术后，吻合区软", "bbox": [250, 170, 742, 190]},
	{"text": "组织影，考虑肿瘤复发，与前列腺分界不", "bbox": [250, 196, 707, 216]},
	{"text": "清，大致同前（2025-10-16）；/>直肠周", "bbox": [250, 222, 713, 242]},
	{"text": "围、右腹膜后、骶前区多发淋巴结转移，部", "bbox": [250, 248, 732, 268]},
	{"text": "分较前略缩小，建议复查3.肝内多发转移", "bbox": [250, 274, 717, 294]},
	{"text": "瘤，较前（2025-10-16）进展4.肝囊肿5.", "bbox": [250, 300, 722, 320]},
	{"text": "膀胱内气体，建议结合临床", "bbox": [250, 326, 555, 346]},
	{"text": "诊断意见", "bbox": [250, 387, 364, 408]},
	{"text": "骨性胸廓对称，纵隔气管居中。双肺支气管", "bbox": [250, 427, 732, 447]},
	{"text": "血管束增多。双肺见弥漫多发类圆形实性结", "bbox": [250, 453, 732, 473]},
	{"text": "节影，大者位于右肺下叶内基底段（薄层", "bbox": [250, 479, 707, 499]},
	{"text": "IM181），大小约为16×16mm，边界清，轻", "bbox": [250, 505, 738, 525]},
	{"text": "度均匀强化。气管及中心支气管通畅。右肺", "bbox": [250, 530, 732, 550]},
	{"text": "门区及纵隔内多发肿大淋巴结，最大者短径", "bbox": [250, 556, 732, 576]},
	{"text": "约14mm，轻度强化。心脏不大。双侧胸膜", "bbox": [250, 582, 726, 602]},
	{"text": "未见明显增厚。双侧胸腔内未见明显液体密", "bbox": [250, 608, 732, 628]},
	{"text": "度影。肝脏增大，肝内见多发类圆形稍低密", "bbox": [250, 634, 738, 654]},
	{"text": "度影，边界不清，大者长径约110mm，增强", "bbox": [250, 660, 736, 680]},
	{"text": "扫描边缘轻度强化。肝右叶可见直径3mm的", "bbox": [250, 686, 728, 706]},
	{"text": "无强化的囊性密度灶，边界清；/>肝内外胆", "bbox": [250, 712, 732, 732]},
	{"text": "管未见明显扩张。胆囊内未见异常密度影。", "bbox": [250, 738, 720, 758]},
	{"text": "胰腺、脾脏未见明显异常密度灶及异常强化", "bbox": [250, 764, 732, 784]},
	{"text": "灶。双肾上腺及双肾大小、形态、密度未见", "bbox": [250, 790, 732, 810]},
	{"text": "明显异常密度灶及异常强化灶。肠管未见梗", "bbox": [250, 816, 732, 836]},
	{"text": "阻征象。直肠术后直肠吻合口区见团片样", "bbox": [250, 842, 738, 860]},
	{"text": ">", "bbox": [570, 871, 588, 891]},
	{"text": "扫描全能王 创建", "bbox": [800, 962, 965, 978]}
]
2026-08-10 18:15:51,355 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=11.0s
2026-08-10 18:15:51,355 INFO     29 [qwen-vl-text] coord item[0]: text=报告单详情, bbox=[432, 60, 566, 81]
2026-08-10 18:15:51,355 INFO     29 [qwen-vl-text] coord item[1]: text=www.jkqd.org.cn, bbox=[434, 83, 566, 95]
2026-08-10 18:15:51,355 INFO     29 [qwen-vl-text] coord item[2]: text=20260307检, bbox=[585, 67, 721, 84]
2026-08-10 18:15:51,355 INFO     29 [qwen-vl-text] coord item[3]: text=查, bbox=[585, 90, 611, 108]
2026-08-10 18:15:51,355 INFO     29 [qwen-vl-text] coord item[4]: text=1.双肺多发结节，较前2025-12-26部分缩, bbox=[250, 119, 713, 138]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[5]: text=小，考虑转移；/>右肺门区及纵隔内多发肿, bbox=[250, 144, 736, 164]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[6]: text=大淋巴结，考虑转移2.直肠术后，吻合区软, bbox=[250, 170, 742, 190]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[7]: text=组织影，考虑肿瘤复发，与前列腺分界不, bbox=[250, 196, 707, 216]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[8]: text=清，大致同前（2025-10-16）；/>直肠周, bbox=[250, 222, 713, 242]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[9]: text=围、右腹膜后、骶前区多发淋巴结转移，部, bbox=[250, 248, 732, 268]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[10]: text=分较前略缩小，建议复查3.肝内多发转移, bbox=[250, 274, 717, 294]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[11]: text=瘤，较前（2025-10-16）进展4.肝囊肿5., bbox=[250, 300, 722, 320]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[12]: text=膀胱内气体，建议结合临床, bbox=[250, 326, 555, 346]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[13]: text=诊断意见, bbox=[250, 387, 364, 408]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[14]: text=骨性胸廓对称，纵隔气管居中。双肺支气管, bbox=[250, 427, 732, 447]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[15]: text=血管束增多。双肺见弥漫多发类圆形实性结, bbox=[250, 453, 732, 473]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[16]: text=节影，大者位于右肺下叶内基底段（薄层, bbox=[250, 479, 707, 499]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[17]: text=IM181），大小约为16×16mm，边界清，轻, bbox=[250, 505, 738, 525]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[18]: text=度均匀强化。气管及中心支气管通畅。右肺, bbox=[250, 530, 732, 550]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[19]: text=门区及纵隔内多发肿大淋巴结，最大者短径, bbox=[250, 556, 732, 576]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[20]: text=约14mm，轻度强化。心脏不大。双侧胸膜, bbox=[250, 582, 726, 602]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[21]: text=未见明显增厚。双侧胸腔内未见明显液体密, bbox=[250, 608, 732, 628]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[22]: text=度影。肝脏增大，肝内见多发类圆形稍低密, bbox=[250, 634, 738, 654]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[23]: text=度影，边界不清，大者长径约110mm，增强, bbox=[250, 660, 736, 680]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[24]: text=扫描边缘轻度强化。肝右叶可见直径3mm的, bbox=[250, 686, 728, 706]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[25]: text=无强化的囊性密度灶，边界清；/>肝内外胆, bbox=[250, 712, 732, 732]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[26]: text=管未见明显扩张。胆囊内未见异常密度影。, bbox=[250, 738, 720, 758]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[27]: text=胰腺、脾脏未见明显异常密度灶及异常强化, bbox=[250, 764, 732, 784]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[28]: text=灶。双肾上腺及双肾大小、形态、密度未见, bbox=[250, 790, 732, 810]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[29]: text=明显异常密度灶及异常强化灶。肠管未见梗, bbox=[250, 816, 732, 836]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[30]: text=阻征象。直肠术后直肠吻合口区见团片样, bbox=[250, 842, 738, 860]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[31]: text=>, bbox=[570, 871, 588, 891]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] coord item[32]: text=扫描全能王 创建, bbox=[800, 962, 965, 978]
2026-08-10 18:15:51,356 INFO     29 [qwen-vl-text] page=6 — 33/33 coords, api_time=11.0s
2026-08-10 18:15:51,357 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1117749, prompt_len=1239
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共31行）
["19:08", "41", "×", "报告单详情", "www.jkqd.org.cn", "瘤，较前（2025-10-16）进展 4. 肝囊肿 5.", "膀胱内气体，建议结合临床", "诊断意见", "骨性胸廓对称，纵隔气管居中。双肺支气管", "血管束增多。双肺见弥漫多发类圆形实性结", "节影，大者位于右肺下叶内基底段（薄层", "IM181），大小约为16×16mm，边界清，轻", "度均匀强化。气管及中心支气管通畅。右肺", "门区及纵隔内多发肿大淋巴结，最大者短径", "约14mm，轻度强化。心脏不大。双侧胸膜", "未见明显增厚。双侧胸腔内未见明显液体密", "度影。肝脏增大，肝内见多发类圆形稍低密", "度影，边界不清，大者长径约110mm，增强", "扫描边缘轻度强化。肝右叶可见直径3mm的", "无强化的囊性密度灶，边界清； />肝内外胆", "管未见明显扩张。胆囊内未见异常密度影。", "胰腺、脾脏未见明显异常密度灶及异常强化", "灶。双肾上腺及双肾大小、形态、密度未见", "明显异常密度灶及异常强化灶。肠管未见梗", "阻征象。直肠术后，直肠吻合口区见团片样", "软组织密度影，与前列腺分界不清，增强扫", "描不均匀强化。直肠周围、右腹膜后、骶前", "区见多发肿大淋巴结，大者短径约11mm，", "增强扫描不均匀强化。膀胱充盈良好，膀胱", "壁光整，膀胱内见气体影。盆腔未见明显积", "液。"]

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
2026-08-10 18:16:03,740 INFO     29 [qwen-vl-text] coord API raw response (len=1891):
[
	{"text": "19:08", "bbox": [228, 22, 310, 42]},
	{"text": "41", "bbox": [758, 23, 784, 39]},
	{"text": "×", "bbox": [190, 74, 222, 97]},
	{"text": "报告单详情", "bbox": [425, 67, 573, 89]},
	{"text": "www.jkqd.org.cn", "bbox": [427, 91, 573, 104]},
	{"text": "瘤，较前（2025-10-16）进展 4. 肝囊肿 5.", "bbox": [222, 113, 746, 134]},
	{"text": "膀胱内气体，建议结合临床", "bbox": [222, 141, 561, 162]},
	{"text": "诊断意见", "bbox": [222, 208, 350, 233]},
	{"text": "骨性胸廓对称，纵隔气管居中。双肺支气管", "bbox": [222, 253, 757, 275]},
	{"text": "血管束增多。双肺见弥漫多发类圆形实性结", "bbox": [222, 281, 757, 303]},
	{"text": "节影，大者位于右肺下叶内基底段（薄层", "bbox": [222, 310, 730, 332]},
	{"text": "IM181），大小约为16×16mm，边界清，轻", "bbox": [222, 338, 764, 360]},
	{"text": "度均匀强化。气管及中心支气管通畅。右肺", "bbox": [222, 367, 757, 389]},
	{"text": "门区及纵隔内多发肿大淋巴结，最大者短径", "bbox": [222, 395, 757, 417]},
	{"text": "约14mm，轻度强化。心脏不大。双侧胸膜", "bbox": [222, 423, 751, 445]},
	{"text": "未见明显增厚。双侧胸腔内未见明显液体密", "bbox": [222, 452, 757, 474]},
	{"text": "度影。肝脏增大，肝内见多发类圆形稍低密", "bbox": [222, 480, 764, 502]},
	{"text": "度影，边界不清，大者长径约110mm，增强", "bbox": [222, 509, 764, 531]},
	{"text": "扫描边缘轻度强化。肝右叶可见直径3mm的", "bbox": [222, 537, 762, 559]},
	{"text": "无强化的囊性密度灶，边界清； />肝内外胆", "bbox": [222, 566, 760, 588]},
	{"text": "管未见明显扩张。胆囊内未见异常密度影。", "bbox": [222, 594, 742, 616]},
	{"text": "胰腺、脾脏未见明显异常密度灶及异常强化", "bbox": [222, 623, 757, 645]},
	{"text": "灶。双肾上腺及双肾大小、形态、密度未见", "bbox": [222, 651, 757, 673]},
	{"text": "明显异常密度灶及异常强化灶。肠管未见梗", "bbox": [222, 679, 757, 701]},
	{"text": "阻征象。直肠术后，直肠吻合口区见团片样", "bbox": [222, 708, 764, 730]},
	{"text": "软组织密度影，与前列腺分界不清，增强扫", "bbox": [222, 736, 757, 758]},
	{"text": "描不均匀强化。直肠周围、右腹膜后、骶前", "bbox": [222, 765, 753, 787]},
	{"text": "区见多发肿大淋巴结，大者短径约11mm，", "bbox": [222, 793, 730, 815]},
	{"text": "增强扫描不均匀强化。膀胱充盈良好，膀胱", "bbox": [222, 822, 757, 844]},
	{"text": "壁光整，膀胱内见气体影。盆腔未见明显积", "bbox": [222, 850, 757, 872]},
	{"text": "液。", "bbox": [222, 879, 264, 901]}
]
2026-08-10 18:16:03,741 INFO     29 [qwen-vl-text] coord API: raw_items=31, valid_items=31, elapsed=12.4s
2026-08-10 18:16:03,741 INFO     29 [qwen-vl-text] coord item[0]: text=19:08, bbox=[228, 22, 310, 42]
2026-08-10 18:16:03,741 INFO     29 [qwen-vl-text] coord item[1]: text=41, bbox=[758, 23, 784, 39]
2026-08-10 18:16:03,741 INFO     29 [qwen-vl-text] coord item[2]: text=×, bbox=[190, 74, 222, 97]
2026-08-10 18:16:03,741 INFO     29 [qwen-vl-text] coord item[3]: text=报告单详情, bbox=[425, 67, 573, 89]
2026-08-10 18:16:03,741 INFO     29 [qwen-vl-text] coord item[4]: text=www.jkqd.org.cn, bbox=[427, 91, 573, 104]
2026-08-10 18:16:03,741 INFO     29 [qwen-vl-text] coord item[5]: text=瘤，较前（2025-10-16）进展 4. 肝囊肿 5., bbox=[222, 113, 746, 134]
2026-08-10 18:16:03,741 INFO     29 [qwen-vl-text] coord item[6]: text=膀胱内气体，建议结合临床, bbox=[222, 141, 561, 162]
2026-08-10 18:16:03,741 INFO     29 [qwen-vl-text] coord item[7]: text=诊断意见, bbox=[222, 208, 350, 233]
2026-08-10 18:16:03,742 INFO     29 [qwen-vl-text] coord item[8]: text=骨性胸廓对称，纵隔气管居中。双肺支气管, bbox=[222, 253, 757, 275]
2026-08-10 18:16:03,742 INFO     29 [qwen-vl-text] coord item[9]: text=血管束增多。双肺见弥漫多发类圆形实性结, bbox=[222, 281, 757, 303]
2026-08-10 18:16:03,742 INFO     29 [qwen-vl-text] coord item[10]: text=节影，大者位于右肺下叶内基底段（薄层, bbox=[222, 310, 730, 332]
2026-08-10 18:16:03,742 INFO     29 [qwen-vl-text] coord item[11]: text=IM181），大小约为16×16mm，边界清，轻, bbox=[222, 338, 764, 360]
2026-08-10 18:16:03,742 INFO     29 [qwen-vl-text] coord item[12]: text=度均匀强化。气管及中心支气管通畅。右肺, bbox=[222, 367, 757, 389]
2026-08-10 18:16:03,742 INFO     29 [qwen-vl-text] coord item[13]: text=门区及纵隔内多发肿大淋巴结，最大者短径, bbox=[222, 395, 757, 417]
2026-08-10 18:16:03,742 INFO     29 [qwen-vl-text] coord item[14]: text=约14mm，轻度强化。心脏不大。双侧胸膜, bbox=[222, 423, 751, 445]
2026-08-10 18:16:03,742 INFO     29 [qwen-vl-text] coord item[15]: text=未见明显增厚。双侧胸腔内未见明显液体密, bbox=[222, 452, 757, 474]
2026-08-10 18:16:03,742 INFO     29 [qwen-vl-text] coord item[16]: text=度影。肝脏增大，肝内见多发类圆形稍低密, bbox=[222, 480, 764, 502]
2026-08-10 18:16:03,742 INFO     29 [qwen-vl-text] coord item[17]: text=度影，边界不清，大者长径约110mm，增强, bbox=[222, 509, 764, 531]
2026-08-10 18:16:03,742 INFO     29 [qwen-vl-text] coord item[18]: text=扫描边缘轻度强化。肝右叶可见直径3mm的, bbox=[222, 537, 762, 559]
2026-08-10 18:16:03,742 INFO     29 [qwen-vl-text] coord item[19]: text=无强化的囊性密度灶，边界清； />肝内外胆, bbox=[222, 566, 760, 588]
2026-08-10 18:16:03,742 INFO     29 [qwen-vl-text] coord item[20]: text=管未见明显扩张。胆囊内未见异常密度影。, bbox=[222, 594, 742, 616]
2026-08-10 18:16:03,742 INFO     29 [qwen-vl-text] coord item[21]: text=胰腺、脾脏未见明显异常密度灶及异常强化, bbox=[222, 623, 757, 645]
2026-08-10 18:16:03,742 INFO     29 [qwen-vl-text] coord item[22]: text=灶。双肾上腺及双肾大小、形态、密度未见, bbox=[222, 651, 757, 673]
2026-08-10 18:16:03,743 INFO     29 [qwen-vl-text] coord item[23]: text=明显异常密度灶及异常强化灶。肠管未见梗, bbox=[222, 679, 757, 701]
2026-08-10 18:16:03,743 INFO     29 [qwen-vl-text] coord item[24]: text=阻征象。直肠术后，直肠吻合口区见团片样, bbox=[222, 708, 764, 730]
2026-08-10 18:16:03,743 INFO     29 [qwen-vl-text] coord item[25]: text=软组织密度影，与前列腺分界不清，增强扫, bbox=[222, 736, 757, 758]
2026-08-10 18:16:03,743 INFO     29 [qwen-vl-text] coord item[26]: text=描不均匀强化。直肠周围、右腹膜后、骶前, bbox=[222, 765, 753, 787]
2026-08-10 18:16:03,743 INFO     29 [qwen-vl-text] coord item[27]: text=区见多发肿大淋巴结，大者短径约11mm，, bbox=[222, 793, 730, 815]
2026-08-10 18:16:03,743 INFO     29 [qwen-vl-text] coord item[28]: text=增强扫描不均匀强化。膀胱充盈良好，膀胱, bbox=[222, 822, 757, 844]
2026-08-10 18:16:03,743 INFO     29 [qwen-vl-text] coord item[29]: text=壁光整，膀胱内见气体影。盆腔未见明显积, bbox=[222, 850, 757, 872]
2026-08-10 18:16:03,743 INFO     29 [qwen-vl-text] coord item[30]: text=液。, bbox=[222, 879, 264, 901]
2026-08-10 18:16:03,743 INFO     29 [qwen-vl-text] page=7 — 31/31 coords, api_time=12.4s
2026-08-10 18:16:03,744 INFO     29 [qwen-vl-text] new_positions (64):
[[6, 257.03999999999996, 336.77, 50.519999999999996, 68.202], [6, 258.22999999999996, 336.77, 69.886, 79.99], [6, 348.075, 428.995, 56.414, 70.728], [6, 348.075, 363.54499999999996, 75.78, 90.93599999999999], [6, 148.75, 424.23499999999996, 100.198, 116.196], [6, 148.75, 437.91999999999996, 121.24799999999999, 138.088], [6, 148.75, 441.48999999999995, 143.14, 159.98], [6, 148.75, 420.66499999999996, 165.03199999999998, 181.87199999999999], [6, 148.75, 424.23499999999996, 186.924, 203.76399999999998], [6, 148.75, 435.53999999999996, 208.816, 225.656], [6, 148.75, 426.615, 230.708, 247.548], [6, 148.75, 429.59, 252.6, 269.44], [6, 148.75, 330.22499999999997, 274.492, 291.332], [6, 148.75, 216.57999999999998, 325.854, 343.536], [6, 148.75, 435.53999999999996, 359.534, 376.37399999999997], [6, 148.75, 435.53999999999996, 381.426, 398.26599999999996], [6, 148.75, 420.66499999999996, 403.318, 420.15799999999996], [6, 148.75, 439.10999999999996, 425.21, 442.05], [6, 148.75, 435.53999999999996, 446.26, 463.09999999999997], [6, 148.75, 435.53999999999996, 468.152, 484.99199999999996], [6, 148.75, 431.96999999999997, 490.044, 506.88399999999996], [6, 148.75, 435.53999999999996, 511.936, 528.776], [6, 148.75, 439.10999999999996, 533.828, 550.668], [6, 148.75, 437.91999999999996, 555.72, 572.56], [6, 148.75, 433.15999999999997, 577.612, 594.452], [6, 148.75, 435.53999999999996, 599.504, 616.3439999999999], [6, 148.75, 428.4, 621.396, 638.236], [6, 148.75, 435.53999999999996, 643.288, 660.1279999999999], [6, 148.75, 435.53999999999996, 665.18, 682.02], [6, 148.75, 435.53999999999996, 687.072, 703.9119999999999], [6, 148.75, 439.10999999999996, 708.9639999999999, 724.12], [6, 339.15, 349.85999999999996, 733.382, 750.222], [6, 476.0, 574.175, 810.004, 823.476], [7, 135.66, 184.45, 18.524, 35.364], [7, 451.01, 466.47999999999996, 19.366, 32.838], [7, 113.05, 132.09, 62.308, 81.67399999999999], [7, 252.875, 340.935, 56.414, 74.938], [7, 254.065, 340.935, 76.622, 87.568], [7, 132.09, 443.87, 95.146, 112.828], [7, 132.09, 333.79499999999996, 118.722, 136.404], [7, 132.09, 208.25, 175.136, 196.186], [7, 132.09, 450.41499999999996, 213.02599999999998, 231.54999999999998], [7, 132.09, 450.41499999999996, 236.602, 255.126], [7, 132.09, 434.34999999999997, 261.02, 279.544], [7, 132.09, 454.58, 284.596, 303.12], [7, 132.09, 450.41499999999996, 309.014, 327.538], [7, 132.09, 450.41499999999996, 332.59, 351.114], [7, 132.09, 446.84499999999997, 356.166, 374.69], [7, 132.09, 450.41499999999996, 380.584, 399.108], [7, 132.09, 454.58, 404.15999999999997, 422.68399999999997], [7, 132.09, 454.58, 428.578, 447.102], [7, 132.09, 453.39, 452.154, 470.678], [7, 132.09, 452.2, 476.572, 495.096], [7, 132.09, 441.48999999999995, 500.14799999999997, 518.672], [7, 132.09, 450.41499999999996, 524.566, 543.09], [7, 132.09, 450.41499999999996, 548.1419999999999, 566.6659999999999], [7, 132.09, 450.41499999999996, 571.718, 590.242], [7, 132.09, 454.58, 596.136, 614.66], [7, 132.09, 450.41499999999996, 619.712, 638.236], [7, 132.09, 448.03499999999997, 644.13, 662.654], [7, 132.09, 434.34999999999997, 667.706, 686.23], [7, 132.09, 450.41499999999996, 692.124, 710.648], [7, 132.09, 450.41499999999996, 715.6999999999999, 734.2239999999999], [7, 132.09, 157.07999999999998, 740.1179999999999, 758.6419999999999]]
2026-08-10 18:16:03,744 INFO     29 [qwen-vl-text] ═══ DONE ═══ 64 positions, pages=2, time=29.4s
2026-08-10 18:16:03,753 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 18:16:03,754 INFO     29 [Trace] task=a677452e | doc=07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf | Extractor:ExaminationReport | outputs={"chunks": "4 items, types={'ExaminationReport': 4}", "html": "", "json": "524 items", "markdown": "", "text": "", "name": "07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "7 items, types={'LabReport': 7}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 4, \"chunks_LabExam\": 7}"}
2026-08-10 18:16:03,754 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 18:16:03,760 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:16:03,760 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 18:16:05,048 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:16:05,054 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 18:16:05,055 INFO     29 [Trace] task=a677452e | doc=07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "524 items", "markdown": "", "text": "", "name": "07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "7 items, types={'LabReport': 7}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 4, \"chunks_LabExam\": 7}"}
2026-08-10 18:16:05,055 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 18:16:05,056 INFO     29 [ChunkMerger] Merged 12 chunks from 9 sources: {'Extractor:LabExam': 7, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 4, 'Extractor:Progress': 1} (filtered 6 noise chunks)
2026-08-10 18:16:05,064 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 18:16:05,064 INFO     29 [Trace] task=a677452e | doc=07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "12 items, types={'LabReport': 7, 'OutpatientRecord': 1, 'ExaminationReport': 4}", "name": "07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf"}
2026-08-10 18:16:05,064 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 18:16:05,229 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786385379491, 'update_date': datetime.datetime(2026, 8, 10, 18, 9, 39), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1342976, 'status': '1'}
2026-08-10 18:16:05,461 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   丙氨酸氨基转移酶  ALT  12  U/L  9-50  False    天门冬氨酸氨基转移酶  AST  30  U/L  15-40  False    AST/ALT  AST/ALT  2.50  None  0.10-3.00  False    总胆红素  TBIL  6.3  umol/L  ≤23.0  False    直接胆红素  DBIL  2.1  umol/L  0-6.8  False    间接胆红素  IBIL  4.2  umol/L  3.4-17.1  False    总蛋白  TP  66.9  g/L  65.0-85.0  False    白蛋白  ALB  31.8  g/L  40.0-55.0  True    球蛋白  GLB  35.1  g/L  20.0-40.0  False    白球比  A/G  0.91  None  1.20-2.40  True    碱性磷酸酶  ALP  240  U/L  45-125  True    谷氨酸脱氢酶  GLDH  11  U/L  0-7  True    γ-谷氨酰转肽酶  GGT  151  U/L  10-60  True    胆碱酯酶  CHE  4919  U/L  5000-12000  True    甘胆酸  CG  1.61  ug/ml  0.00-2.70  False    总胆汁酸  TBA  4.20  umol/L  0.00-10.00  False    前白蛋白  PA  135  mg/L  200-430  True    尿素  UREA  4.7  mmol/L  3.1-8.0  False    肌酐  CREA  50.0  umol/L  57-97  True    尿素/肌酐  UREA/CREA  0.09  None  0.01-0.70  False    估算肾小球滤过率  eGFR  119  mL/min/1.73m2  None  False    尿酸  UA  326  umol/L  208-428  False    钾  K  4.0  mmol/L  3.5-5.3  False    钠  Na  139  mmol/L  137-147  False    氯  CL  104  mmol/L  99-110  False    总二氧化碳  CO2  22  mmol/L  22-29  False    阴离子间隙  AG  13  mmol/L  8-16  False   
---
   唾液酸  SA  969  mg/L  456-754  True    补体Clq  Clq  16.5  mg/dl  15.7-23.7  False   
---
   凝血酶原时间  PT  14.4  秒  10.70--14.80  False    凝血酶原时间活动度  PT%  85.00  %  70.00--150.00  False    凝血酶原时间比值  PT. R  1.08  None  0.82--1.15  False    国际标准化比值  PT. INR  1.10  None  1.0--2.0  False    活化部分凝血活酶时间  APTT  43.2  秒  28.00--43.00  True    活化部分凝血活酶时间比值  APTT R  1.27  None  0.82--1.26  True    纤维蛋白原  Fib  6.490  g/L  2.000--4.000  True    凝血酶时间  TT  17.10  秒  14.00--21.00  False    D-二聚体  D-Dimer  3.20  mg/L(FEU)  0.00--0.50  True    抗凝血酶活性  AT:A  92.00  %  80.00--130.00  False    纤维蛋白(原)降解产物  FDP  14.63  mg/L  0.00--5.00  True   
---
   白细胞计数  WBC  3.96  *10^9/L  3.50--9.50  False    中性粒细胞计数  NEUT#  2.89  *10^9/L  1.80--6.30  False    淋巴细胞计数  LYMPH#  0.65  *10^9/L  1.10--3.20  True    单核细胞计数  MONO#  0.30  *10^9/L  0.10--0.60  False    嗜酸细胞计数  EO#  0.10  *10^9/L  0.02--0.52  False    嗜碱细胞计数  BASO#  0.02  *10^9/L  0.00--0.06  False    中性粒细胞百分比  NEUT%  73.0  %  40.0--75.0  False    淋巴细胞百分比  LYMPH%  16.4  %  20.0--50.0  True    单核细胞百分比  MONO%  7.6  %  3.0--10.0  False    嗜酸细胞百分比  E0%  2.6  %  0.40--8.00  False    嗜碱细胞百分比  BASO%  0.4  %  0.00--1.00  False    红细胞计数  RBC  3.57  *10^12/L  4.30--5.80  True    血红蛋白含量  HGB  88  g/L  130--175  True    红细胞比容  HCT  0.28  L/L  0.40--0.50  True    平均红细胞血红蛋白含量  MCH  24.6  pg  27.0--34.0  True    平均红细胞血红蛋白浓度  MCHC  319  g/L  316--354  False    平均红细胞体积  MCV  77.2  fL  82.0--100.0  True    红细胞分布宽度（CV）  RDW--CV  17.4  %  11.6--16.5  True    红细胞分布宽度（SD）  RDW--SD  50.1  fL  37.0--54.0  False    血小板计数  PLT  268  *10^9/L  125--350  False    平均血小板体积  MPV  8.2  fL  7.4--11.0  False    大血小板比率  P--LCR  14.8  %  13.0--43.0  False    血小板比容  PCT  0.22  %  0.170--0.350  False    血小板分布宽度  PDW  15.4  fL  15.5--16.8  True    C--反应蛋白  CRP  30.830  mg/L  0.000--5.000  True   
---
   粪便颜色  Colour  黄色  None  棕黄  False    粪便性状  Stool-type  软  None  软  False    白细胞  WBC  未见  /HPF  0-3/阴性  False    红细胞  RBC  未见  /HPF  阴性  False    脂肪滴  Fat droplet  未见  /HPF  阴性  False    真菌  Fungus  未见  /HPF  阴性  False    寄生虫卵  Parasitic ovum  未见  None  阴性  False    隐血试验  OBT  阳性反应 (+)  None  A 阴性反应 (-)  True   
---
   红细胞计数  RBC  43.00  个/ul  0.00--17.00  True    白细胞计数  WBC  3117.00  个/ul  0.00--28.00  True    白细胞团  WBCC  180.00  个/ul  0.00--2.00  True    鳞状上皮细胞  SQEP  15.00  个/ul  0.00--28.00  False    非鳞状上皮细胞  NSE  0.00  个/ul  0.00--6.00  False    透明管型  HYAL  0.00  个/ul  0.00--1.00  False    病理管型  UNCC  1.00  个/ul  0.00--1.00  False    酵母  BYST  0.00  个/ul  0.00--1.00  False    未分类结晶  UNCX  49.00  个/ul  0.00--28.00  True    粘液丝  MUCS  12.00  个/ul  0.00--46.00  False    细菌  BACT  11801.00  个/ul  0.00--340.00  True    潜血  BLD  痕量(++)  None  阴性(-)  True    白细胞酯酶  LEU  阳性(2+)  None  阴性(-)  True    亚硝酸盐  NIT  阳性(2+)  None  阴性(-)  True    尿胆素原  UBG  Normal  None  Normal  False    胆红素  BIL  阴性(-)  None  阴性(-)  False    维生素C  VC  阳性(+)  None  阴性(-)  True    蛋白质  PRO  痕量(++)  None  阴性(-)  True    酸碱度  PH  5.5  None  5.0--8.0  False    比密  SG  1.025  None  1.005--1.030  False    葡萄糖  GLU  阴性(-)  None  阴性(-)  False    酮体  KET  阴性(-)  None  阴性(-)  False    颜色  Colour  黄色  None  None  False    透明度  Clarity  浑浊  None  None  False   
---
   乙型肝炎病毒表面抗原  HBsAg  <0.05 阴性反应(-)  IU/ml  <0.08  False    丙型肝炎病毒抗体  HCV  0.060 阴性反应(-)  None  <1  False    梅毒螺旋体抗体  antiTP  0.0 阴性反应(-)  None  0.000-1.000  False    人免疫缺陷病毒抗体  HIV Ab  0.0 阴性反应(-)  None  0.000-1.000  False   
---
康复大学青岛中心医院
门诊病历
姓名：
性别：男
出生日期：19
龄：53岁
门诊号
科别：肿瘤内一科门诊
就诊时间：2026-03-02 17:35:26
主诉：乙状结肠癌术后复发，会阴区疼痛
现病史：患者2023-11-29于青医附院行“腹腔镜中转乙状结肠癌根治术+直肠部分切除术+预防性回
肠末端造口术+左侧输尿管支架植入术”，2023-11-30术后病理示：“浸润深度：侵达浆膜，切缘：
小肠切缘（-），结肠切缘（-），其他：另见绒毛状-管状腺瘤，伴多灶高级别上皮内瘤变（多枚，直
径0.3-1.5cm）。淋巴结：肠周（4/20）淋巴结内见癌转移；送检小肠系膜（0/3）淋巴结内未见癌转
移。病理学分期：pT3N2aMx。术后恢复可，2024-4-10发现“肝转移”，一线行“奥沙利铂+卡培他
滨”化疗。2025-06-13肠镜：直肠术后，吻合口占位Ca？肠镜病理：“（直肠吻合口）腺癌（中分
化）。2025-06-20 PET/CT：1.直肠癌术后治疗后，肝转移瘤术后，现示：直肠吻合口区高代谢占位，
符合肿瘤复发（并与前列腺、双侧精囊腺关系密切，建议MRI检查），盆腔直肠周围、腹腔（右半肠系
膜区）、腹膜后（双侧髂内血管走行区、骶前区）多发淋巴结转移，双肺转移（两处）；右肺上叶实
性小结节，无明显异常FDG代谢增高，不除外转移。提示吻合口复发、双肺转移，病情进展，二线给予
“伊立替康脂质体43mg d1、2+卡培他滨1.5g d1-14”化疗2周期。基因检测（2025-07-02）：1.KRAS
p.G12D突变丰度12.81%，NRAS突变阴性。2025-08-06行贝伐珠单抗400mg靶向治疗。2025-10-16复查
CT：1.直肠术后，吻合区软组织影，考虑肿瘤复发，与前列腺分界不清，较2025.8.1范围略大；直肠
周围、右腹膜后、骶前区多发淋巴结转移，部分较前略缩小，建议复查2.肝内多发转移瘤，较前进展
3.肝囊肿。病情进展，患者既往接受过氟尿嘧啶类、奥沙利铂和伊立替康为基础的化疗，以及抗血管
内皮生成因子治疗，病情进展，予呋喹替尼三线治疗。近期反复睾丸感染于泌尿外科行手术治疗，目
前患者会阴区疼痛明显，NRS 3-5分，予止痛药物治疗，食欲差、乏力，夜间睡眠欠佳，外院2026-02-
03血常规示血红蛋白80g/L。
体格检查：双肺呼吸音粗，未闻及干湿啰音。。
辅助检查结果：暂无
初步诊断：结肠恶性肿瘤
诊疗意见：1.(瑞乐芬)氨酚羟考酮片4盒间隔6小时1片口服×12天
2.蒙脱石散5盒日三次3g口服×25天
3.(易蒙停)盐酸洛哌丁胺胶囊10盒日三次2mg口服×25天
门诊病历专用章
3702080719401
医生签名：梁华
---
青岛大学附属医院
市南院区
病理检查诊断报告
病理号
姓名
性别：男
年龄：51岁
送检单位：青岛大学附属医院市 送检科室：胃肠外科
收到日期：2024-04-11
送检医生：赵蕊蕊
病区：胃肠外科病区
住院号：
送检材料：肝肿物，造口端回肠，直肠息
临床诊断：1.乙状结肠恶性肿瘤,2.回肠造口状态
大体检查:
肝肿物：肝组织一件，大小4*3*2cm，剖开，距离肝断端0.4cm见一灰白肿物，范围
0.5*0.4cm，质软，紧邻肝被膜0.5cm，其余肝组织灰红灰黄质软。
造口组织一件，大小6.5*5*3cm，皮肤范围4*2.5cm，连接肠管两段，长分别为
3cm、3.5cm，直径分别为1.5cm、1.7cm，肠粘膜灰白灰红。
直肠息肉1：息肉样物一枚，大小2*2*1cm，未见明显蒂部及基底，于疑似基底处涂
墨。
直肠息肉2：息肉样物一枚，大小2*1*0.8cm，未见明显蒂部。
直肠息肉3：息肉样物三枚，大小1.5*1*0.6cm，中者大小1*1*0.5cm，小者大小
0.7*0.6*0.4cm，未见明显蒂部及基底。
病理诊断:
1、（肝肿物）肝组织内见中分化腺癌浸润，结合形态、病史及免疫组化结果，符合
转移性肠腺癌。
免疫组化结果：CK7（-），CK20（灶+），Arginase-1（-），CDX-2（+），SATB2
（+），Ki-67（+，约80%）。
2、（造口端回肠）皮肤及肠粘膜组织呈慢性活动性炎伴糜烂，复鳞上皮乳头状增
生，间质纤维组织增生，血管扩张、充血及出血，部分区域肌层排列紊乱，符合造口
改变。
3、（直肠息肉1、2、3）均为绒毛状-管状腺瘤，部分腺体呈高级别上皮内瘤变，局
灶癌变-中分化腺癌。
免疫组化结果：CK-Desmin示未见确切粘膜肌。
报告医生：张丽
初诊医生：张晶晶
报告日期：2024-04-19
注：1.病理诊断分级注解：明确及基本明确的诊断，无任何修饰语；如有“考虑为”、“疑为”、“符合”、
“不除外”及“可能性大”等修饰语，提示诊断具有不同程度的不确定性，请结合临床相关检查综合判断。
2.如本诊断与临床表现及相关检查不符，请临床医生及时与病理科联系后再行处置。
3.此报告以纸质版为准。
审核专用章
---
青岛大学附属医院
市南院区
病理检查诊断报告
病理号.
姓  夕
性  别：男
年  龄：52
送检单位：青岛大学附属医院市 送检科室：消化内科
收到日期：
送检医生：李晓宇
病  区：
住院号：
送检材料：肠镜活检
临床诊断：直肠多发息肉完成ESD吻合口溃疡
大体检查:
直肠息肉ESD：粘膜组织一件，大小3.5*2.5*0.8cm，距一侧切缘0.1cm，距另一侧
切缘0.4cm，粘膜表面见一隆起，范围3*2.3cm，切面灰白质脆，基底涂墨。
直肠吻合口：粘膜组织三块，合计直径0.4cm。
病理诊断:
1.标本类型：直肠息肉ESD
标本数量：1件
病变数量：1灶
病变范围：3*2.3cm
组织学类型：绒毛状--管状腺瘤伴高级别上皮内瘤变，局灶区域恶变--中分化腺癌，
局限于粘膜层内
脉管癌栓：（-）
神经侵犯：（-）
水平切缘：（-）
垂直切缘：（-）
2.（直肠吻合口）腺癌（中分化）。
免疫组化结果示（直肠息肉ESD）：MLH1（+），MSH2（+），MSH6（+），PMS2
(+），p53（+，约20%），CK-Desmin示粘膜肌连续，HER2（1+），S100示神经侵犯
（-），CD31及D2-40示脉管癌栓（-），Ki-67（+，约60%）。
报告医生：李丹
初诊医生：赵玉洁
报告日期：2025-02-20
注：1.病理诊断分级注解：明确及基本明确的诊断
---
青岛市中心医疗集团
2.检测结果总览
本检测基于MGI（DNBSeq T7）测序平台对样本进行高通量测序。覆盖肿瘤相关的566个基因，检测内容包含目标基
因覆盖范围内的单核苷酸变异、小片段插入/缺失、拷贝数变异、重排（融合），以及微卫星不稳定性（MSI）分析、肿瘤
突变负荷（TMB）分析等。
检测类别
检测结果
基因变异1
体系
I类（具有明确临床意义的变异）：KRAS p.G12D, KRAS p.A146V
II类（具有潜在临床意义的变异）：TP53 p.G245D, FBXW7 p.R367*
III类（临床意义不确定的变异）：RBM10 p.R97*, MUC16 p.A7208T, ALDH2 p
.A5T, MTOR p.G1491S, CARD11 p.R207C等26个
胚系
致病性/疑似致病性变异：APC p.L180Yfs*5
靶向药物提示
KRAS p.G12D提示：司美替尼(C级)、Avutometinib and defactinib (C级)可能敏感；西妥昔单抗(A级)、Panitumumab (A级)可能耐药。
KRAS p.A146V提示：Avutometinib and defactinib (C级)可能敏感；西妥昔单抗(A级)、Pan
itumumab (A级)可能耐药。
TP53 p.G245D提示：AZD1775 (C级)可能敏感。
FBXW7 p.R367*提示：恩替司他(D级)、Belinostat (D级)可能敏感。
APC p.L180Yfs*5提示：达沙替尼(D级)、厄洛替尼(D级)可能敏感。
诊断/预后提示
目前暂未发现与本癌种诊断/预后相关的基因变异。
免疫治疗疗效提示
TMB(同义突变 非同义突变)
13.89Muts/Mb
TMB(非同义突变)
10.42Muts/Mb (前12.62%)
MSI状态
MSS (微卫星稳定)
其他潜在免疫疗效相关标志物2
正相关：未检出
负相关：未检出
超进展相关：未检出
化疗用药提示
可能药物敏感性较高：暂无，详见实验结果
可能毒副作用风险较低：卡培他滨，伊立替康
肿瘤遗传风险提示
检出APC p.L180Yfs*5疑似致病性变异，建议对受检者及血亲进行适当的遗传咨询或临床管理
注：1. 基因变异
58
青岛市中心医疗集团
(1) 体系变异参考AMP/ASCO/CAP 共识《Standards and Guidelines for the Interpretation and Reporting of
Sequence Variants in Cancer》，基因变异按照临床意义的重要性分为四个类别
I类：具有明确临床意义的变异，包括NMPA、FDA批准疗法，或专业临床指南（如CSCO诊疗指南、NCCN临
床实践指南）推荐（A级证据），或基于证据充分的临床研究，并获得专家共识有明确治疗、诊断、预后的
变异（B级证据）；
II类：具有潜在临床意义的变异，包括其他癌种的A级证据（跨适应症用药），或多项小型临床研究支持，或
已作为当前临床研究的入组标准（C级证据），或临床前研究或案例报道，未获得专家共识的药物（D级证
据）；
III类：临床意义不确定的变异（尚无相关临床证据）
“类：下事或示能于事的变异（在全人群或特定人群数据库中观察到高变异率）
扫描全能王 创建
青岛市中心医疗集团
3.基因变异临床意义综合提示
3.1诊断/预后及靶向药物提示
基因变异1
突变丰度2/拷贝数
变异分类
可能敏感药物
可能耐药药物
突变说明
KRAS
NM_004985.5
12.81%
I类
司美替尼(C级)
西妥昔单抗(A
级)
KRAS基因的G12D突变，发生在第
2号外显子，位于GTP结合蛋白结
构域(UniProt.org)，突变导致
第12位氨基酸由甘氨酸变为天冬氨
酸，G12突变将降低自身的GTP酶
活性，使KRAS长期处于与GTP结
合的激活状态，导致细胞增殖异常
(PMID:12509763,20736745,2
6037647,6092966)，为功能获
得突变。
exon2
p.G12D
c.35G>A
Avutometinib a
nd defactinib(C
级)
Pantitumuma
b(A级)
KRAS
NM_004985.5
1.46%
I类
Avutometinib a
nd defactinib(C
级)
西妥昔单抗(A
级)
KRAS基因的A146V突变，发生在
第4号外显子，突变导致146位氨基
酸由丙氨酸变为缬氨酸，为功能获
得突变。在两个不同的细胞系中，
与野生型Kras相比，A146V可能会
降低Kras的GTPase活性，从而导
致下游通路激活增加(PMID:205
70890)，与野生型Kras相比，A1
46V突变会增加细胞增殖和细胞活
力(PMID:29533785)，为功能
获得突变。
exon4
p.A146V
c.437C>T
Panitumuma
b(A级)
TP53
NM_000546.6
12.73%
II类
AZD1775(C级)
TP53基因的G245D突变，发生在
第7号外显子，位于Tp53蛋白的D
NA结合域(PMID:22713868)
，突变导致245位甘氨酸变为天冬
氨酸。G245D导致Tp53靶基因的
激活减少(PMID:22214764,256
34208,27533082)，为功能丧失
突变。
exon7
p.G245D
c.734G>A
FBXW7
NM_033632.3
2.75%
II类
恩替司他(D级)
FBXW7基因的R367*突变，发生在
第7号外显子，突变导致终止密码
子提前编码(UniProt.org)。由于W
D重复域的丢失，预测R367*会导
致Fbxw7蛋白功能的丢失(UniProt
.org)。
exon7
p.R367*
c.1099C>T
Belinostat(D级)
APC
NM_000038.6
杂合
II类
达沙替尼(D级)
APC基因的p.L180Yfs*5、c.539de
l突变，发生在第6外显子，不在已
知功能域内(UniProt.org)，突
变导致其编码的氨基酸在180位开
始框移，可能影响蛋白功能(Uni
Prot.org)。已知APC的功能丧失
变异具有致病性(PMID:17963004
,20685668)。Clinvar数据库记录
该变异为Pathogenic。其在人群
基因组数据库未收录。综上分析，
该突变是一个疑似致病性变异。
exon6
p.L180Yfs*5
c.539del
厄洛替尼(D级)
注:1.基因变异：“exon”为外显子，“intron”为内含子，“c”为DNA序列，“p”为蛋白质，“NM”为基因的转录
本编号;
2.突变丰度:在某位点产生突变的等位基因在该位点全部等位基因中所占比率。例如,突变丰度10%意为该位点含
有10%的突变等位基因和90%的野生型等位基因。拷贝数:是指某一种基因或某一段特定的DNA序列在单倍体基
因组中出现的数目。
4/58
---
报告单详情
www.jkqd.org.cn
20260307检
查
1.双肺多发结节，较前2025-12-26部分缩
小，考虑转移；/>右肺门区及纵隔内多发肿
大淋巴结，考虑转移2.直肠术后，吻合区软
组织影，考虑肿瘤复发，与前列腺分界不
清，大致同前（2025-10-16）；/>直肠周
围、右腹膜后、骶前区多发淋巴结转移，部
分较前略缩小，建议复查3.肝内多发转移
瘤，较前（2025-10-16）进展4.肝囊肿5.
膀胱内气体，建议结合临床
诊断意见
骨性胸廓对称，纵隔气管居中。双肺支气管
血管束增多。双肺见弥漫多发类圆形实性结
节影，大者位于右肺下叶内基底段（薄层
IM181），大小约为16×16mm，边界清，轻
度均匀强化。气管及中心支气管通畅。右肺
门区及纵隔内多发肿大淋巴结，最大者短径
约14mm，轻度强化。心脏不大。双侧胸膜
未见明显增厚。双侧胸腔内未见明显液体密
度影。肝脏增大，肝内见多发类圆形稍低密
度影，边界不清，大者长径约110mm，增强
扫描边缘轻度强化。肝右叶可见直径3mm的
无强化的囊性密度灶，边界清；/>肝内外胆
管未见明显扩张。胆囊内未见异常密度影。
胰腺、脾脏未见明显异常密度灶及异常强化
灶。双肾上腺及双肾大小、形态、密度未见
明显异常密度灶及异常强化灶。肠管未见梗
阻征象。直肠术后直肠吻合口区见团片样
>
扫描全能王 创建
19:08
41
×
报告单详情
www.jkqd.org.cn
瘤，较前（2025-10-16）进展 4. 肝囊肿 5.
膀胱内气体，建议结合临床
诊断意见
骨性胸廓对称，纵隔气管居中。双肺支气管
血管束增多。双肺见弥漫多发类圆形实性结
节影，大者位于右肺下叶内基底段（薄层
IM181），大小约为16×16mm，边界清，轻
度均匀强化。气管及中心支气管通畅。右肺
门区及纵隔内多发肿大淋巴结，最大者短径
约14mm，轻度强化。心脏不大。双侧胸膜
未见明显增厚。双侧胸腔内未见明显液体密
度影。肝脏增大，肝内见多发类圆形稍低密
度影，边界不清，大者长径约110mm，增强
扫描边缘轻度强化。肝右叶可见直径3mm的
无强化的囊性密度灶，边界清； />肝内外胆
管未见明显扩张。胆囊内未见异常密度影。
胰腺、脾脏未见明显异常密度灶及异常强化
灶。双肾上腺及双肾大小、形态、密度未见
明显异常密度灶及异常强化灶。肠管未见梗
阻征象。直肠术后，直肠吻合口区见团片样
软组织密度影，与前列腺分界不清，增强扫
描不均匀强化。直肠周围、右腹膜后、骶前
区见多发肿大淋巴结，大者短径约11mm，
增强扫描不均匀强化。膀胱充盈良好，膀胱
壁光整，膀胱内见气体影。盆腔未见明显积
液。
2026-08-10 18:16:06,195 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 18:16:06,195 INFO     29 [Trace] task=a677452e | doc=07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "12 items, types={'LabReport': 7, 'OutpatientRecord': 1, 'ExaminationReport': 4}", "name": "07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf", "embedding_token_consumption": 8227}
2026-08-10 18:16:06,195 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 18:16:06,434 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 18:16:06,434 INFO     29 [Trace] task=a677452e | doc=07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":12,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 18:16:06,439 INFO     29 [DIAG-EXECUTOR] row_position_int len=27 row[0]=(9, 109, 185, 97, 106) row[-1]=(9, 96, 148, 471, 479)
2026-08-10 18:16:06,439 INFO     29 [DIAG-EXECUTOR] row_position_int len=2 row[0]=(9, 98, 135, 724, 733) row[-1]=(9, 98, 139, 739, 748)
2026-08-10 18:16:06,439 INFO     29 [DIAG-EXECUTOR] row_position_int len=11 row[0]=(10, 33, 123, 138, 149) row[-1]=(10, 33, 148, 336, 347)
2026-08-10 18:16:06,440 INFO     29 [DIAG-EXECUTOR] row_position_int len=25 row[0]=(11, 52, 122, 135, 146) row[-1]=(11, 38, 107, 490, 500)
2026-08-10 18:16:06,440 INFO     29 [DIAG-EXECUTOR] row_position_int len=8 row[0]=(12, 30, 82, 137, 148) row[-1]=(12, 30, 82, 260, 271)
2026-08-10 18:16:06,440 INFO     29 [DIAG-EXECUTOR] row_position_int len=24 row[0]=(13, 31, 92, 140, 152) row[-1]=(13, 31, 73, 548, 560)
2026-08-10 18:16:06,440 INFO     29 [DIAG-EXECUTOR] row_position_int len=4 row[0]=(14, 32, 163, 136, 147) row[-1]=(14, 32, 152, 188, 199)
2026-08-10 18:16:06,440 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 18:16:06,440 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 18:16:06,440 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 18:16:06,440 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 18:16:06,440 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 18:16:06,445 INFO     29 set_progress(a677452e94e611f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 18:16:06 [DOC Engine]:
Start to index...
2026-08-10 18:16:06,459 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.008s]
2026-08-10 18:16:06,465 INFO     29 set_progress(a677452e94e611f1bd9827cf206dfa2d), progress: 0.8083333333333333, progress_msg: 
2026-08-10 18:16:06,490 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.016s]
2026-08-10 18:16:06,528 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.029s]
2026-08-10 18:16:06,535 INFO     29 set_progress(a677452e94e611f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 18:16:06 Indexing done (0.09s). Task done (361.51s)
2026-08-10 18:16:06,544 INFO     29 [Done], chunks(12), token(8227), elapsed:361.51
2026-08-10 18:16:06,728 INFO     29 handle_task done for task {"id": "a677452e94e611f1bd9827cf206dfa2d", "doc_id": "a646f41e94e611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-WGJU\uff0c\u7ed3\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 11495294, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786385378144, "task_type": "dataflow", "root_trace_id": "971de7c4c0604c27afceabc8ac295233", "root_traceparent": "00-971de7c4c0604c27afceabc8ac295233-de3f877b239fe0d8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
