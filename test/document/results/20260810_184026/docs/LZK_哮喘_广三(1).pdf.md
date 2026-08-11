# 基准结果：LZK 哮喘 广三(1).pdf

## 基本信息

- 文件：`LZK 哮喘 广三(1).pdf`
- 大小：5325.3 KB
- PDF 总页数：16
- doc_id：`ea1b0b1894ae11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T19:30:39  完成时间：2026-08-10T19:39:55  耗时：556.5s
- progress_msg：`11:39:54 Indexing done (0.13s). Task done (530.77s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 41b1b016 | 2 | 1-2 | 病历编号： 性别：男 年龄：40岁 就诊科室：内科门诊（荔湾） 就诊时间：202 |
| 2 | eee4ddee | 1 | 3-3 | 就诊卡 流水号： 姓名 龄：40岁 就诊科 日：2025-10-24 15:45 |
| 3 | 80b2b18f | 1 | 4-4 | 病历编号： 姓名： 性别： 年龄：40岁 就诊科室： 就诊时间：2025-11- |
| 4 | 98bad621 | 1 | 5-5 | 门(急)诊处方 就诊时间:2025-07-18 就诊科室:内科门诊 主诊医 姓名 |
| 5 | 6c0375cb | 1 | 6-6 | 门(急)诊处方 就诊时间:2025-04-25 就诊科室:内科门诊 主诊 姓名  |
| 6 | 468130c4 | 1 | 7-7 | 门(急)诊处方 就诊时间：2025-02-26 就诊科室：内科门诊 主诊 性别： |
| 7 | e6ceb5ee | 1 | 8-8 | 门(急)诊处方 就诊时间:2025-01-24 就诊科室:内科门诊 主诊医 姓名 |
| 8 | 94a93e9d | 1 | 9-9 | 门(急)诊处方 就诊时间:2025-01-03 就诊科室:内科门诊 主诊 性别: |
| 9 | ec4ce4d7 | 1 | 10-10 | 门(急)诊处方 就诊时间:2024-12-04 就诊科室:内科门诊 姓名 性别: |
| 10 | 954b4035 | 1 | 11-11 | 激发试验检查报告 姓名： 测试号： 门诊/住院号： 000 年龄： 出生日期：  |
| 11 | 196f00fe | 1 | 12-12 | 检查日期：2021/1/21 检查时间：16:43 编号：16 广州医科大学附属 |
| 12 | 58bb2d44 | 1 | 13-13 | 广州医科大学附属第三医院 处方笺 普通 诊疗卡 患者姓名 年龄：41岁 费别：南 |
| 13 | ea2df857 | 1 | 14-14 | 广州医科大学附属第三医院 The Third Affiliated Hospit |
| 14 | ae941ece | 1 | 15-15 | 门诊/住院病历信息 就诊卡号： 病历编号： 流水号 姓名 性别：男 年龄：41岁 |
| 15 | df46f447 | 1 | 16-16 | 广州医科大学附属第三医院 肺功能检查报告 地址：广州市多宝路63号 电话：020 |

- chunks 总数：15
- 各 chunk 页数合计（含跨页重复）：16
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]`
- 覆盖页数：16 / 16；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 5 | 0 | 0 | encounter_date, chief_complaint, diagnosis | **LOST** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 7 | 7 | 0 | encounter_date, prescriber, diagnosis | **LOST** |
| ExaminationReport | 检查报告 | 3 | 3 | 3 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 5, "PrescriptionRecord": 7, "ExaminationReport": 3}`
- ChunkMerger：`{"found": true, "merged": 15, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 5, "Extractor:Medication": 1, "Extractor:Prescription": 7, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 3, "Extractor:Progress": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 11:39:52,869 INFO     29 [ChunkMerger] Merged 15 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 5, 'Extractor:Medication': 1, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 11:30:43,295 INFO     29 handle_task begin for task {"id": "ea51b5dc94ae11f1bd9827cf206dfa2d", "doc_id": "ea1b0b1894ae11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786361440167, "task_type": "dataflow", "root_trace_id": "bca8d639df704cd29f0107370613ab01", "root_traceparent": "00-bca8d639df704cd29f0107370613ab01-b8b3c91a32048c1c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 11:30:43,496 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 11:30:43,616 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 11:30:43,628 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:30:43,628 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 11:30:43,628 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 11:30:43,655 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 11:30:43,655 INFO     29 ============================================================
2026-08-10 11:30:43,655 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 11:30:43,655 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 11:30:43,655 INFO     29 ============================================================
2026-08-10 11:30:43,656 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 11:30:43,656 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 11:30:43,667 INFO     29 No torch found.
2026-08-10 11:30:45,201 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=16
2026-08-10 11:30:45,369 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1449002, prompt_len=764
2026-08-10 11:30:46,849 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:30:46,849 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 11:30:46,860 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1449002, prompt_len=401
2026-08-10 11:30:54,820 INFO     29 [qwen-vl-parser] text API response (len=1120):
["病历编号：", "性别：男", "年龄：40岁", "就诊科室：内科门诊（荔湾）", "就诊时间：2025-10-10 14:36:06", "主诉：BAIYUN V8", "现病史：自上次访视至今，询问及查询HIS系统受试者有新增AE，无SAE、哮喘急性发作，有新增合并用药，发生2次医疗相关事件[2025年9月3日因过敏性鼻炎就诊专科门诊、本周曾因上呼吸道感染到社区医院就诊(具体不详，因HIS系统滞后无法收集具体情况及受试者无法回忆起当时情况及用药情况，待收集具体情况后补充详情)]。于2025年8月4日、2025年9月1日收到加重警报邮件，联系受试者后，均判断非哮喘急性发作。", "完成下流操作：", "1、查看受试者电子日志，受试者漏填2025年8月16日，2025年9月4日晚间日志，2025年9月4日、2025年9月25日早间日志；", "2、填写AQLQ+12和ACQ-5问卷，ACQ-5评分：0.8分；", "3、休息10分钟后，测量坐位生命体征：血压113/81mmHg，脉搏87次/分，呼吸频率20次/分，体温36.6℃，测量身高177.5cm，体重90.5kg(BMI=28.7kg/m2)；", "4、14:35体格检查：神志清，体查合作，自主体位，一般外表无异常，皮肤、粘膜无异常，唇甲无发绀，眼睛、耳、鼻、咽喉无异常，口咽部粘膜无异常，颈软，气管居中，甲状腺未及肿大，全身浅表淋巴结未及肿大，颈静脉无怒张，胸廓无畸形，双肺呼吸运动对称，双肺触觉语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及啰音。心前区无隆起，心尖搏动无弥散，心界不大，心率：87次/分，律齐，各瓣膜听诊区未闻及病理性杂音。腹平软，全腹无压痛、反跳痛。肝、脾肋下未及，肝肾区无叩击痛，肠鸣音存，4次/分，脊柱、四肢无畸形，生理征存，未引出病理征，其他系统未见明显异常；", "5、休息至少10分钟后，于14:58行12导联ECG检查；", "6、于15:01采集中心实验室样本(血常规，血生化)并送往中心试验室；", "7、回收试验药物BDAMDI@ASMDI3盒(152968-AH及185936-HK未开封，148729-UA未用60揿，实际使用46揿，发药当天预喷4揿，2025年9月10日前因超过7天未使用试验药物空喷2次共4揿，2025年9月10日后受试者每七天清洗一次后空喷5次共10揿，总计预喷18揿；epro记录使用总共46揿，与实际使用情况一致。", "8、回收epro以及AM3。", "既往史：更新合并用药：", "1、糠酸莫米松鼻喷雾剂2025.4.3-2025.7.25 每鼻 2喷/次 qm 治疗过敏性鼻炎。"]
2026-08-10 11:30:54,820 INFO     29 [qwen-vl-parser] page=1 text: 18 lines (bbox 0-17)
2026-08-10 11:30:54,820 INFO     29 [qwen-vl-parser] page=1 text: 18 sections
2026-08-10 11:30:54,927 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=608187, prompt_len=764
2026-08-10 11:30:56,297 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:30:56,298 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 11:30:56,307 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=608187, prompt_len=401
2026-08-10 11:31:01,196 INFO     29 [qwen-vl-parser] text API response (len=803):
["病历文书", "门诊病历", "25/10/10 14时 门诊病历", "25/10/24 15时 门诊病历（GCP专用）", "25/11/17 10时 门诊病历", "头降使用40瓶，平均每天使用4瓶，2025年9月10日用完4瓶（大木使用试验药剂空瓶2次共4", "瓶，2025年9月10日后受试者每七天青光一次后空瓶5次共10瓶，总计空瓶10瓶（qrs记录使", "用总共46瓶，与实际使用情况一致。", "8、回访qrs以及MD。", "既往史：更新合并用药：", "1、鼻腔莫米松鼻喷雾剂C025 4 3-2025 7 25 每鼻 2喷/次 qd 治疗过敏性鼻炎。", "2、苯环喹氯桉鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。", "4、氯卓斯汀氟替卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。", "5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/", "次 治疗过敏性鼻炎。", "6、枯草抗感染治疗（生理盐水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过", "敏性鼻炎", "已预约受试者安全性随访时间。", "过敏史：", "个人史：", "体格检查：", "专科情况：", "辅助检查：", "治疗项目：", "门诊诊断：", "支气管哮喘", "单病种：", "发病时间：", "处", "置：", "1心电图（心电图室做）", "2布地奈德福莫特罗吸入粉雾剂(II)(省采)●①② 2盒2000,日入用药,一天2次", "30天", "备注：", "病情评估：", "病情分级：", "是否抢救病例：否", "是否抢救成功：", "是否为绿色通道患者：否", "病人去向：", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 11:31:01,197 INFO     29 [qwen-vl-parser] page=2 text: 42 lines (bbox 18-59)
2026-08-10 11:31:01,197 INFO     29 [qwen-vl-parser] page=2 text: 42 sections
2026-08-10 11:31:01,349 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1138149, prompt_len=764
2026-08-10 11:31:02,646 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:31:02,647 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 11:31:02,659 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1138149, prompt_len=401
2026-08-10 11:31:05,619 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:31:05.618+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 23, "failed": 0, "current": {"ea51b5dc94ae11f1bd9827cf206dfa2d": {"id": "ea51b5dc94ae11f1bd9827cf206dfa2d", "doc_id": "ea1b0b1894ae11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786361440167, "task_type": "dataflow", "root_trace_id": "bca8d639df704cd29f0107370613ab01", "root_traceparent": "00-bca8d639df704cd29f0107370613ab01-b8b3c91a32048c1c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:31:08,500 INFO     29 [qwen-vl-parser] text API response (len=962):
["就诊卡", "流水号：", "姓名", "龄：40岁", "就诊科", "日：2025-10-24 15:45:39", "主诉：安全性电话随访", "现病史：今日10:27", "固定电话（020-", "（159", "5），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无", "不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对", "V8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试", "者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，", "目前无安全性异常表现。", "合并用药更新：", "1、小柴胡颗粒、（自行购药）2025.10.6-2025.10.8 10g tid 治疗上呼吸道感染", "2、苯环喹溴铵鼻喷雾剂 2025.4.3-至今 每鼻2喷/次 qid 治疗过敏性鼻炎", "3、氮卓斯汀氟替卡松鼻喷雾剂 2025.9.3-至今 每鼻2喷/次 bid 治疗过敏性鼻炎", "4、辛芩颗粒 2024.8.21-2024.8.27 1袋 冲服 tid 治疗过敏性鼻炎", "AE：", "上呼吸道感染 2025年10月5日-2025年10月8日 中度，非SAE，采取药物治疗措施，对试验", "药物采取措施：剂量不变，与试验药物无关，未因该AE退出研究。", "病历更正：", "1、更正2024年10月22日病历，合并用药“辛芩颗粒”为“辛芩颗粒”；", "2、更正2024年10月22日病历，合并用药“苯环喹溴铵鼻喷雾剂”为“苯环喹溴铵鼻喷雾", "剂”；", "3、更正2026年1月24日病历，“无收到ePro触发的哮喘警报邮件”为“有收到ePro触发的哮", "喘警报邮件”；", "4、更正2025年7月18日病历，“受试者漏填2025年4月28日晚间日志” 更正为：“受试者", "漏填2025年4月28日早间日志”；", "5、更正2024年11月6日病历，“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共", "计用了26喷”为：“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了28", "喷”。", "随行中·"]
2026-08-10 11:31:08,501 INFO     29 [qwen-vl-parser] page=3 text: 35 lines (bbox 60-94)
2026-08-10 11:31:08,501 INFO     29 [qwen-vl-parser] page=3 text: 35 sections
2026-08-10 11:31:08,657 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1126349, prompt_len=764
2026-08-10 11:31:10,039 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:31:10,040 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 11:31:10,060 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1126349, prompt_len=401
2026-08-10 11:31:15,113 INFO     29 [qwen-vl-parser] text API response (len=843):
["病历编号：", "姓名：", "性别：", "年龄：40岁", "就诊科室：", "就诊时间：2025-11-17 10:10:48", "主诉：支气管哮喘治疗后复查：", "现病史：2021年2月前开始出现咳嗽、咯痰，粘白，量中，能咯出，咳嗽呈阵发性、刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏。无咽痛，无伴反酸、嗳气、腹胀。无上腹部隐痛不适感，无伴发热、畏寒，影响睡眠。晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：", "12.52*109/L 嗜酸粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定。本次门诊距上次门诊间隔时间30天。症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确。急性发作情况：两次，就诊期间急性发作：无，发作次数：0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。近3天来出现咽痛不适", "既往史：鼻炎病史无规则治疗。打鼾明显。", "过敏史：未发现。", "个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。", "体格检查：神志清，颈软，双肺呼吸音粗，未闻及明显干、湿性罗音，口腔粘膜无白斑。", "专科情况：", "辅助检查：", "治疗项目：", "门诊诊断：", "1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、阻塞性睡眠呼吸暂停低通气综合征,4、急性咽炎", "单病种：", "发病时间：", "处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不适随诊。", "1金银花口服液◆⑤ 2盒 20.0ml,口服,一天3次(口服) 6天", "2氨卓斯汀氟替卡松鼻喷雾剂◆ 1瓶 2.0喷,喷鼻,一天2次 30天", "3苯环喹溴铵鼻喷雾剂◆ 3瓶 2.0喷,喷鼻,一天4次 30天", "备注：建议在住地附近社区医疗机构随诊。"]
2026-08-10 11:31:15,114 INFO     29 [qwen-vl-parser] page=4 text: 25 lines (bbox 95-119)
2026-08-10 11:31:15,114 INFO     29 [qwen-vl-parser] page=4 text: 25 sections
2026-08-10 11:31:15,226 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=674431, prompt_len=764
2026-08-10 11:31:16,614 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:31:16,615 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 11:31:16,629 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=674431, prompt_len=401
2026-08-10 11:31:18,361 INFO     29 [qwen-vl-parser] text API response (len=278):
["门(急)诊处方", "就诊时间:2025-07-18", "就诊科室:内科门诊", "主诊医", "姓名", "性别:男", "年龄:40岁", "卡号:", "患者", "医疗证号:", "处方号", "地址:PT027气雾剂 2024017-呼吸科", "身份证", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂0.125/0.0006*60吸6盒", "183.41100.46", "Sig", "2吸/次,吸入,bid*90天"]
2026-08-10 11:31:18,362 INFO     29 [qwen-vl-parser] page=5 text: 26 lines (bbox 120-145)
2026-08-10 11:31:18,362 INFO     29 [qwen-vl-parser] page=5 text: 26 sections
2026-08-10 11:31:18,471 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=687923, prompt_len=764
2026-08-10 11:31:19,856 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:31:19,857 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-10 11:31:19,869 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=687923, prompt_len=401
2026-08-10 11:31:21,595 INFO     29 [qwen-vl-parser] text API response (len=284):
["门(急)诊处方", "就诊时间:2025-04-25", "就诊科室:内科门诊", "主诊", "姓名", "性别:男", "年龄:40岁", "卡号:", "患者类型:GLP支付", "医疗证号:", "处方号", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂(II)●●@ug*60吸6盒", "183.41100.46", "Sig", "2吸/次,吸入,bid*90天"]
2026-08-10 11:31:21,596 INFO     29 [qwen-vl-parser] page=6 text: 26 lines (bbox 146-171)
2026-08-10 11:31:21,596 INFO     29 [qwen-vl-parser] page=6 text: 26 sections
2026-08-10 11:31:21,707 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=642003, prompt_len=764
2026-08-10 11:31:23,077 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:31:23,078 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-10 11:31:23,086 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=642003, prompt_len=401
2026-08-10 11:31:25,926 INFO     29 [qwen-vl-parser] text API response (len=272):
["门(急)诊处方", "就诊时间：2025-02-26", "就诊科室：内科门诊", "主诊", "性别：男", "年龄：40岁", "卡号", "医疗证号：", "处方", "015", "地址：PT027气雾剂 2024017-呼吸科", "身份证号：", "诊断：支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂BUD/●@1g*60吸2盒", "183.41", "366.82", "Sig", "2吸/次,吸入,bid*30天"]
2026-08-10 11:31:25,927 INFO     29 [qwen-vl-parser] page=7 text: 26 lines (bbox 172-197)
2026-08-10 11:31:25,927 INFO     29 [qwen-vl-parser] page=7 text: 26 sections
2026-08-10 11:31:26,044 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=635678, prompt_len=764
2026-08-10 11:31:27,494 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-01-24"}
```
2026-08-10 11:31:27,495 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=2025-01-24
2026-08-10 11:31:27,512 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=635678, prompt_len=401
2026-08-10 11:31:29,292 INFO     29 [qwen-vl-parser] text API response (len=287):
["门(急)诊处方", "就诊时间:2025-01-24", "就诊科室:内科门诊", "主诊医", "姓名", "性别:男", "年龄:40岁", "卡号:4", "患者类型:GCP支付", "医疗证号:", "处方号:", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂HIV●@1ug*60吸4盒", "183.41 733.64", "Sig", "2吸/次,吸入,bid*60天"]
2026-08-10 11:31:29,293 INFO     29 [qwen-vl-parser] page=8 text: 26 lines (bbox 198-223)
2026-08-10 11:31:29,293 INFO     29 [qwen-vl-parser] page=8 text: 26 sections
2026-08-10 11:31:29,390 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=545840, prompt_len=764
2026-08-10 11:31:30,715 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-01-03"}
```
2026-08-10 11:31:30,716 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=2025-01-03
2026-08-10 11:31:30,732 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=545840, prompt_len=401
2026-08-10 11:31:32,851 INFO     29 [qwen-vl-parser] text API response (len=356):
["门(急)诊处方", "就诊时间:2025-01-03", "就诊科室:内科门诊", "主诊", "性别:男", "年龄:40岁", "卡号", "患者类型:GCP支付", "医疗证号:", "处方", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂(Ⅱ)●●60ug*60吸2盒", "183.41 366.82", "Sig", "2吸/次,吸入,bid*30天", "医师:", "医生编号:1326", "配剂人:", "核对人:", "合计:", "收费员:", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 11:31:32,852 INFO     29 [qwen-vl-parser] page=9 text: 33 lines (bbox 224-256)
2026-08-10 11:31:32,852 INFO     29 [qwen-vl-parser] page=9 text: 33 sections
2026-08-10 11:31:32,966 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=642925, prompt_len=764
2026-08-10 11:31:34,398 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-12-04"}
```
2026-08-10 11:31:34,398 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=2024-12-04
2026-08-10 11:31:34,408 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=642925, prompt_len=401
2026-08-10 11:31:36,112 INFO     29 [qwen-vl-parser] text API response (len=271):
["门(急)诊处方", "就诊时间:2024-12-04", "就诊科室:内科门诊", "姓名", "性别:男", "年龄:39岁", "卡号", "患者", "医疗证号:", "处方", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●(50ug*60吸2盒", "183.41 366.82", "Sig", "2吸/次,吸入,bid*30天"]
2026-08-10 11:31:36,113 INFO     29 [qwen-vl-parser] page=10 text: 25 lines (bbox 257-281)
2026-08-10 11:31:36,113 INFO     29 [qwen-vl-parser] page=10 text: 25 sections
2026-08-10 11:31:36,262 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1233186, prompt_len=764
2026-08-10 11:31:36,740 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:31:36.739+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 23, "failed": 0, "current": {"ea51b5dc94ae11f1bd9827cf206dfa2d": {"id": "ea51b5dc94ae11f1bd9827cf206dfa2d", "doc_id": "ea1b0b1894ae11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786361440167, "task_type": "dataflow", "root_trace_id": "bca8d639df704cd29f0107370613ab01", "root_traceparent": "00-bca8d639df704cd29f0107370613ab01-b8b3c91a32048c1c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:31:37,688 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 11:31:37,688 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=None
2026-08-10 11:31:37,702 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1233186, prompt_len=401
2026-08-10 11:31:47,385 INFO     29 [qwen-vl-parser] text API response (len=1965):
["激发试验检查报告", "姓名：", "测试号：", "门诊/住院号：", "000", "年龄：", "出生日期：", "19", "性别：", "男", "身高：", "170", "病区：", "内科门诊", "体重：", "81 kg", "机器编号：", "床号：", "电话：", "Pred", "A1", "A1/Pd", "NS", "P1 chg%1", "P2 chg%2", "P3 chg%3", "FVC", "[L]", "4.84", "4.69", "97.1", "4.29", "4.22", "-10.1", "3.64", "-22.5", "4.01", "-14.6", "PEV 1", "[L]", "4.01", "3.05", "76.2", "2.72", "2.69", "-11.8", "2.24", "-26.5", "2.44", "-20.0", "PEV 1 % PVC", "[%]", "83.32", "65.02", "78.0", "63.54", "63.83", "-1.82", "61.73", "-5.06", "60.92", "-6.30", "PEV 1 % VC MAX", "[%]", "80.55", "64.94", "80.6", "62.34", "63.83", "-1.70", "61.73", "-4.94", "60.92", "-6.18", "VC MAX", "[L]", "5.05", "4.70", "93.1", "4.37", "4.22", "-10.2", "3.64", "-22.6", "4.01", "-14.7", "PEP", "[L/s]", "9.37", "9.95", "106.2", "9.06", "7.81", "-21.5", "6.73", "-32.3", "8.22", "-17.4", "MMEF 75/25", "[L/s]", "4.52", "1.54", "34.1", "1.33", "1.34", "-12.9", "1.14", "-25.8", "1.23", "-20.0", "MEF 50", "[L/s]", "5.17", "1.97", "38.1", "1.66", "1.71", "-13.4", "1.34", "-31.8", "1.42", "-28.0", "MEF 25", "[L/s]", "2.29", "0.58", "25.5", "0.52", "0.53", "-9.87", "0.50", "-14.6", "0.49", "-15.7", "PET", "[s]", "6.72", "6.87", "6.93", "3.16", "6.75", "0.57", "6.74", "0.38", "V backextrapolation ex", "[L]", "0.13", "0.09", "0.10", "-20.0", "0.08", "-41.6", "0.08", "-38.5", "PIF", "[L/s]", "8.04", "7.96", "7.58", "-5.76", "6.16", "-23.3", "7.78", "-3.20", "FIF 50", "[L/s]", "7.99", "7.86", "7.16", "-10.3", "5.36", "-32.9", "7.08", "-11.3", "MVV", "[L/min]", "141.88", "BF MVV", "[1/min]", "Cumulated dose", "0.072 0.078", "0.312", "2 Puf", "F/V ex", "F/V in", "Vol [L]", "Vol%VCmax", "VCmax", "Time [s]", "PD[-20] FEV 1: 0.2117 mg Cumulated", "PD[-20] PEF: < 0.078 mg Cumulated", "PD[] FEV1%I: could not be calculated!", "意见：", "2022/6/08 10:23:56上午", "1.轻度阻塞性通气功能障碍。", "2.支气管激发试验阳性(累计吸入乙酰甲胆碱0.312mg，FEV1下降大于20%，PD20=0.2117mg，气道高反应性(AHR)为中度", "通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后FEV1恢复至预计值80%。", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 11:31:47,386 INFO     29 [qwen-vl-parser] page=11 text: 199 lines (bbox 282-480)
2026-08-10 11:31:47,386 INFO     29 [qwen-vl-parser] page=11 text: 199 sections
2026-08-10 11:31:47,561 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1298077, prompt_len=764
2026-08-10 11:31:49,033 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2021-01-21"
}
```
2026-08-10 11:31:49,033 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=2021-01-21
2026-08-10 11:31:49,056 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1298077, prompt_len=401
2026-08-10 11:31:59,997 INFO     29 [qwen-vl-parser] text API response (len=1940):
["检查日期：2021/1/21", "检查时间：16:43", "编号：16", "广州医科大学附属第三医院", "支气管扩张试验检查报告", "姓名：", "测试号：", "年龄：36岁", "性别：男", "病区：", "机器编号：", "门诊/住院号：", "出生日期：", "身高：", "体重：", "床号：", "电话：", "Pred", "A1", "A1/Pd", "P1", "A2/Pd", "chg%1", "P2", "A3/Pd", "chg%2", "P3", "A4/Pd", "chg%3", "FVC", "[L]", "4.86", "3.48", "71.5%", "4.01", "82.4%", "15.19", "4.15", "85.4%", "19.47", "4.01", "82.6%", "15.47", "FEV 1", "[L]", "4.03", "1.97", "48.8%", "2.33", "57.9%", "18.59", "2.33", "57.8%", "18.48", "2.44", "60.5%", "24.02", "FEV 1 % FVC", "[%]", "83.32", "56.62", "68.0%", "58.29", "70.0%", "2.95", "56.15", "67.4%", "-0.83", "60.81", "73.0%", "7.40", "FEV 1 % VC MAX", "[%]", "80.73", "56.07", "69.5%", "58.29", "72.2%", "3.96", "56.15", "69.5%", "0.14", "60.81", "75.3%", "8.45", "VC MAX", "[L]", "5.08", "3.51", "69.1%", "4.01", "78.9%", "14.07", "4.15", "81.8%", "18.31", "4.01", "79.1%", "14.35", "PEF", "[L/s]", "9.41", "6.61", "70.3%", "7.99", "85.0%", "20.93", "7.91", "84.1%", "19.63", "8.07", "85.7%", "22.02", "MMEF 75/25", "[L/s]", "4.57", "0.81", "17.7%", "0.96", "21.1%", "19.59", "1.03", "22.6%", "28.17", "1.12", "24.6%", "39.07", "MEF 50", "[L/s]", "5.20", "1.00", "19.2%", "1.29", "24.8%", "29.25", "1.30", "24.9%", "29.87", "1.53", "29.3%", "52.75", "MEF 25", "[L/s]", "2.32", "0.39", "16.7%", "0.38", "16.4%", "-1.68", "0.50", "21.6%", "29.78", "0.41", "17.9%", "7.18", "FET", "[s]", "15.24", "6.42", "-57.87", "6.30", "-58.63", "6.55", "-57.05", "V backextrapolati", "[L/s]", "0.07", "0.07", "0.89", "0.09", "17.79", "0.08", "6.12", "PIF", "[L/s]", "7.03", "7.39", "5.19", "7.17", "1.99", "7.16", "1.91", "FIV1", "[L]", "3.40", "3.76", "10.58", "3.68", "8.26", "3.60", "5.96", "PEF50 % PIF50", "[%]", "16.56", "21.70", "31.06", "19.81", "19.65", "24.71", "49.20", "MVV", "[L/min]", "142.69", "BF MVV", "[1/min]", "意见：", "1.重度混合性肺通气功能障碍。", "2.支气管舒张试验阳性。", "（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后PEV1较基线增加大于12%，且绝对值增加大于200ml）", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 11:31:59,998 INFO     29 [qwen-vl-parser] page=12 text: 211 lines (bbox 481-691)
2026-08-10 11:31:59,999 INFO     29 [qwen-vl-parser] page=12 text: 211 sections
2026-08-10 11:32:00,130 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=712860, prompt_len=764
2026-08-10 11:32:01,651 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:32:01,651 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=None
2026-08-10 11:32:01,666 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=712860, prompt_len=401
2026-08-10 11:32:03,785 INFO     29 [qwen-vl-parser] text API response (len=350):
["广州医科大学附属第三医院", "处方笺", "普通", "诊疗卡", "患者姓名", "年龄：41岁", "费别：南医保", "科室：内科门诊（荔湾）", "日期：2026-01-05 17:17:14", "处方号", "地址：荔湾", "2024017-呼吸科", "联系电话", "身份号码：", "2739", "诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],急性气管支气管炎", "R", "P:", "布地奈德福莫特罗吸入粉雾剂(II) 160ug/4.5ug*60吸", "2盒", "剂量：每次2吸", "（", "1", "30", "盒）", "用法：吸入用药", "bid", "01-05", "处方金额：366.82元", "取药药房：门诊西药房（荔湾）"]
2026-08-10 11:32:03,785 INFO     29 [qwen-vl-parser] page=13 text: 30 lines (bbox 692-721)
2026-08-10 11:32:03,785 INFO     29 [qwen-vl-parser] page=13 text: 30 sections
2026-08-10 11:32:03,925 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=972380, prompt_len=764
2026-08-10 11:32:05,397 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-01-05"}
```
2026-08-10 11:32:05,397 INFO     29 [qwen-vl-parser] page=14 classify=text report_date=2026-01-05
2026-08-10 11:32:05,406 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=972380, prompt_len=401
2026-08-10 11:32:07,830 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:32:07.827+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 23, "failed": 0, "current": {"ea51b5dc94ae11f1bd9827cf206dfa2d": {"id": "ea51b5dc94ae11f1bd9827cf206dfa2d", "doc_id": "ea1b0b1894ae11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786361440167, "task_type": "dataflow", "root_trace_id": "bca8d639df704cd29f0107370613ab01", "root_traceparent": "00-bca8d639df704cd29f0107370613ab01-b8b3c91a32048c1c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:32:12,344 INFO     29 [qwen-vl-parser] text API response (len=1267):
["广州医科大学附属第三医院", "The Third Affiliated Hospital of Guangzhou Medical University", "门(急)诊病历信息", "就诊卡", "流水", "姓", "病历编号:", "年 龄:41岁", "就诊科室:内科门诊(荔湾) 医", "就诊时间:2026-01-05 17:07:54", "主 诉:支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天", "现 病 史:2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激", "性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流", "涕、喷嚏,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响", "睡眠,晨起有咽干,曾到本院就诊两次,症状不见明显缓解。2021-1-9血常规:白细胞:", "12.52*109/L 嗜酸粒细胞:0.65*109/L 5.2%,经治疗后症状明显缓解。无咳嗽、咯痰、气", "促。病情稳定,本次门诊距上次门诊间隔时间30天。症状控制情况:过去4周,患者:吸入", "药物使用情况:遵医嘱使用;吸入装置使用情况:正确。急性发作情况:两次,就诊期间急", "性发作:无,发作次数:0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。长期规律使用信必", "可160/4.5ug 2吸 bid治疗,5天前开始出现咳嗽、咯痰,黄白痰,量少,难以咯出,咳嗽以", "夜间为主。无气促,伴咽息,鼻塞、流涕、喷嚏,无发热。", "既 往 史:鼻炎病史无规则治疗。打鼾明显。", "过 敏 史:未发现;", "个 人 史:否认遗传病史,吸烟10年,20支/日,2018年戒烟。偶饮酒。2021-12-20已打第", "三针新冠疫苗。", "体格检查:神志清,颈软,双肺呼吸音粗,可闻及散在哮鸣音,口腔粘膜无白斑。", "专科情况:", "辅助检查:", "治疗项目:", "门诊诊断:", "1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎", "处 置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。", "布地奈德福莫特罗吸入粉雾剂(II)2盒 2.0吸,吸入用药,一天2次 30天", "(省采)●①⑤", "左氧氟沙星片(省采)●⑥ 5片 0.5g,口服,每日1次(口服) 5天", "第1页", "广州医科大学附属第三医院", "The Third Affiliated Hospital of Guangzhou Medical University", "门(急)诊病历信息", "复方甲氧那明胶囊(省采)◆② 1瓶 1.0粒,餐后口服,一天3次(口服) 5天", "盐酸氨溴索分散片(省采)●⑥ 15片 30.0mg,餐后口服,一天3次(口服) 5", "天", "醋酸泼尼松片●②④ 6片 10.0mg,口服,每早1次(口服) 3天", "备 注:建议在住地附近社区医疗机构随诊。"]
2026-08-10 11:32:12,345 INFO     29 [qwen-vl-parser] page=14 text: 44 lines (bbox 722-765)
2026-08-10 11:32:12,345 INFO     29 [qwen-vl-parser] page=14 text: 44 sections
2026-08-10 11:32:12,577 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1211412, prompt_len=764
2026-08-10 11:32:13,934 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-02-04"}
```
2026-08-10 11:32:13,935 INFO     29 [qwen-vl-parser] page=15 classify=text report_date=2026-02-04
2026-08-10 11:32:13,958 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1211412, prompt_len=401
2026-08-10 11:32:18,840 INFO     29 [qwen-vl-parser] text API response (len=807):
["门诊/住院病历信息", "就诊卡号：", "病历编号：", "流水号", "姓名", "性别：男", "年龄：41岁", "就诊科室：内科门诊（荔湾）", "就诊时间：2026-02-04 11:21:11", "主诉：支气管哮喘治疗后复查", "现病史：2021年2月前开始出现咳嗽、咳痰，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sng 2吸 bid治疗。", "既往史：鼻炎病史无规则治疗，打鼾明显。", "过敏史：未发现；", "个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。", "体格检查：神志清，颈软，双肺呼吸音粗，可闻及散在哮鸣音，口腔粘膜无白斑。", "专科情况：", "辅助检查：", "治疗项目：", "门诊诊断：", "1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、急性气管支气管炎", "单病种：", "发病时间：", "处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不遥随诊。", "布地奈德福莫特罗吸入粉雾剂(II)(省", "2 2.0班，吸入用药，一天2次", "30", "采)●①②", "查天"]
2026-08-10 11:32:18,841 INFO     29 [qwen-vl-parser] page=15 text: 28 lines (bbox 766-793)
2026-08-10 11:32:18,841 INFO     29 [qwen-vl-parser] page=15 text: 28 sections
2026-08-10 11:32:19,017 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1642425, prompt_len=764
2026-08-10 11:32:23,708 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2024-10-22"
}
```
2026-08-10 11:32:23,708 INFO     29 [qwen-vl-parser] page=16 classify=text report_date=2024-10-22
2026-08-10 11:32:23,736 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1642425, prompt_len=401
2026-08-10 11:32:37,136 INFO     29 [qwen-vl-parser] text API response (len=2514):
["广州医科大学附属第三医院", "肺功能检查报告", "地址：广州市多宝路63号 电话：020-81292126", "COSMED", "姓名：", "科室/床号：", "ID：", "出生日期：1984/12/8", "预计值：ERS 93", "日期：2024/10/22", "性别：Male", "地区修正：Chinese", "详细描述：内科门诊", "Company：", "年龄：39", "体重(Kg)：89.0", "身高(cm)：177.5", "BMI(Kg/m²：28.2", "吸烟：曾经(10/20)", "用力肺活量 Forced Vital Capacity", "F(l/s)", "V(l)", "BEST #3 - 2024/10/22 11:03", "沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38", "沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39", "沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41", "沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38", "沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39", "沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41", "BEST #3 - 2024/10/22 11:03", "FVC", "PEF", "MEF75%", "MEF50%", "MEF25%", "FVC", "8V(l)", "FEV1", "ATS", "12t(s)", "-1 0 1 2 3 4 5 6 7 8 9 10 11 12t(s)", "218133", "ST", "2024-10-22", "Parameter", "UM", "Pred.", "BEST#3", "%Pred.", "POST#4", "%Pred.", "%Test#3", "POST#5", "%Pred.", "%Test#3", "POST#6", "%F", "FVC", "l(btps)", "4.87", "3.48", "71", "3.72", "76", "+6.9", "4.24", "87", "+22.0", "4.11", "FEV1", "l(btps)", "4.01", "2.58", "64", "2.94", "73", "+13.7", "3.15", "79", "+21.9", "3.15", "FEV1/FVC%", "%", "80.2", "74.3", "93", "79.0", "98", "+6.4", "74.2", "93", "0.0", "76.6", "PEF", "l/sec", "9.37", "9.86", "105", "9.98", "107", "+1.3", "10.48", "112", "+6.3", "10.52", "1", "FEV6", "l(btps)", "5.17", "3.68", "71", "4.22", "82", "4.11", "PIF", "l/sec", "7.33", "7.76", "+5.8", "7.78", "+6.1", "7.88", "FEV6/FVC%", "%", "99.0", "99.4", "100.0", "FEF25-75%", "l/sec", "4.47", "1.88", "42", "2.59", "58", "+37.8", "2.31", "52", "+22.8", "2.52", "FEV3", "l(btps)", "3.25", "3.44", "+5.8", "3.94", "+21.3", "3.78", "FEV3/FVC%", "%", "93.3", "92.4", "-1.0", "92.9", "-0.5", "92.1", "FEV1/FEV6%", "%", "79.8", "74.7", "76.6", "MEF75%", "l/sec", "8.09", "5.96", "74", "9.28", "115", "+55.7", "7.53", "93", "+26.3", "7.17", "MEF50%", "l/sec", "5.17", "2.57", "50", "3.49", "68", "+35.8", "3.08", "59", "+19.6", "3.28", "MEF25%", "l/sec", "2.28", "0.71", "31", "0.95", "42", "+33.9", "0.83", "36", "+16.6", "0.87", "FET100%", "sec", "6.0", "6.7", "+12.8", "6.5", "+9.4", "6.5", "VEXT", "ml", "208", "192", "162", "IC", "l(btps)", "3.33", "3.38", "+1.5", "3.50", "+5.1", "3.35", "FIVC", "l(btps)", "4.29", "4.70", "+9.6", "4.51", "+5.1", "4.46", "PEFr", "l/min", "562.3", "591.4", "105", "599.0", "107", "+1.3", "628.8", "112", "+6.3", "630.9", "1", "诊断：", "中度限制性通气功能障碍。支气管舒张试验阳性（吸入沙丁胺醇400μg，FEV1上升>12%，且绝对值>200ml）。", "打印2024/10/22", "PFT Suite 10.0d", "页 1 of 1", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 11:32:37,137 INFO     29 [qwen-vl-parser] page=16 text: 245 lines (bbox 794-1038)
2026-08-10 11:32:37,137 INFO     29 [qwen-vl-parser] page=16 text: 245 sections
2026-08-10 11:32:37,137 INFO     29 [qwen-vl-parser] parse_pdf done: 1039 sections from 16 pages.
2026-08-10 11:32:37,150 INFO     29 Close text detector.
2026-08-10 11:32:37,636 INFO     29 Close text recognizer.
2026-08-10 11:32:38,035 INFO     29 Close recognizer.
2026-08-10 11:32:38,464 INFO     29 Close recognizer.
2026-08-10 11:32:38,930 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:32:38.464+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 23, "failed": 0, "current": {"ea51b5dc94ae11f1bd9827cf206dfa2d": {"id": "ea51b5dc94ae11f1bd9827cf206dfa2d", "doc_id": "ea1b0b1894ae11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786361440167, "task_type": "dataflow", "root_trace_id": "bca8d639df704cd29f0107370613ab01", "root_traceparent": "00-bca8d639df704cd29f0107370613ab01-b8b3c91a32048c1c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:32:38,966 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 11:32:38,966 INFO     29 [Trace] task=ea51b5dc | doc=LZK 哮喘 广三(2).pdf | Parser:MedLink | outputs={"html": "", "json": "1039 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(2).pdf", "output_format": "json"}
2026-08-10 11:32:38,966 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 11:32:38,998 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:32:38,998 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 病历编号：\n[BBOX-1] 性别：男\n[BBOX-2] 年龄：40岁\n[BBOX-3] 就诊科室：内科门诊（荔湾）\n[BBOX-4] 就诊时间：2025-10-10 14:36:06\n[BBOX-5] 主诉：BAIYUN V8\n[BBOX-6] 现病史：自上次访视至今，询问及查询HIS系统受试者有新增AE，无SAE、哮喘急性发作，有新增合并用药，发生2次医疗相关事件[2025年9月3日因过敏性鼻炎就诊专科门诊、本周曾因上呼吸道感染到社区医院就诊(具体不详，因HIS系统滞后无法收集具体情况及受试者无法回忆起当时情况及用药情况，待收集具体情况后补充详情)]。于2025年8月4日、2025年9月1日收到加重警报邮件，联系受试者后，均判断非哮喘急性发作。\n[BBOX-7] 完成下流操作：\n[BBOX-8] 1、查看受试者电子日志，受试者漏填2025年8月16日，2025年9月4日晚间日志，2025年9月4日、2025年9月25日早间日志；\n[BBOX-9] 2、填写AQLQ+12和ACQ-5问卷，ACQ-5评分：0.8分；\n[BBOX-10] 3、休息10分钟后，测量坐位生命体征：血压113/81mmHg，脉搏87次/分，呼吸频率20次/分，体温36.6℃，测量身高177.5cm，体重90.5kg(BMI=28.7kg/m2)；\n[BBOX-11] 4、14:35体格检查：神志清，体查合作，自主体位，一般外表无异常，皮肤、粘膜无异常，唇甲无发绀，眼睛、耳、鼻、咽喉无异常，口咽部粘膜无异常，颈软，气管居中，甲状腺未及肿大，全身浅表淋巴结未及肿大，颈静脉无怒张，胸廓无畸形，双肺呼吸运动对称，双肺触觉语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及啰音。心前区无隆起，心尖搏动无弥散，心界不大，心率：87次/分，律齐，各瓣膜听诊区未闻及病理性杂音。腹平软，全腹无压痛、反跳痛。肝、脾肋下未及，肝肾区无叩击痛，肠鸣音存，4次/分，脊柱、四肢无畸形，生理征存，未引出病理征，其他系统未见明显异常；\n[BBOX-12] 5、休息至少10分钟后，于14:58行12导联ECG检查；\n[BBOX-13] 6、于15:01采集中心实验室样本(血常规，血生化)并送往中心试验室；\n[BBOX-14] 7、回收试验药物BDAMDI@ASMDI3盒(152968-AH及185936-HK未开封，148729-UA未用60揿，实际使用46揿，发药当天预喷4揿，2025年9月10日前因超过7天未使用试验药物空喷2次共4揿，2025年9月10日后受试者每七天清洗一次后空喷5次共10揿，总计预喷18揿；epro记录使用总共46揿，与实际使用情况一致。\n[BBOX-15] 8、回收epro以及AM3。\n[BBOX-16] 既往史：更新合并用药：\n[BBOX-17] 1、糠酸莫米松鼻喷雾剂2025.4.3-2025.7.25 每鼻 2喷/次 qm 治疗过敏性鼻炎。\n[BBOX-18] 病历文书\n[BBOX-19] 门诊病历\n[BBOX-20] 25/10/10 14时 门诊病历\n[BBOX-21] 25/10/24 15时 门诊病历（GCP专用）\n[BBOX-22] 25/11/17 10时 门诊病历\n[BBOX-23] 头降使用40瓶，平均每天使用4瓶，2025年9月10日用完4瓶（大木使用试验药剂空瓶2次共4\n[BBOX-24] 瓶，2025年9月10日后受试者每七天青光一次后空瓶5次共10瓶，总计空瓶10瓶（qrs记录使\n[BBOX-25] 用总共46瓶，与实际使用情况一致。\n[BBOX-26] 8、回访qrs以及MD。\n[BBOX-27] 既往史：更新合并用药：\n[BBOX-28] 1、鼻腔莫米松鼻喷雾剂C025 4 3-2025 7 25 每鼻 2喷/次 qd 治疗过敏性鼻炎。\n[BBOX-29] 2、苯环喹氯桉鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。\n[BBOX-30] 4、氯卓斯汀氟替卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。\n[BBOX-31] 5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/\n[BBOX-32] 次 治疗过敏性鼻炎。\n[BBOX-33] 6、枯草抗感染治疗（生理盐水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过\n[BBOX-34] 敏性鼻炎\n[BBOX-35] 已预约受试者安全性随访时间。\n[BBOX-36] 过敏史：\n[BBOX-37] 个人史：\n[BBOX-38] 体格检查：\n[BBOX-39] 专科情况：\n[BBOX-40] 辅助检查：\n[BBOX-41] 治疗项目：\n[BBOX-42] 门诊诊断：\n[BBOX-43] 支气管哮喘\n[BBOX-44] 单病种：\n[BBOX-45] 发病时间：\n[BBOX-46] 处\n[BBOX-47] 置：\n[BBOX-48] 1心电图（心电图室做）\n[BBOX-49] 2布地奈德福莫特罗吸入粉雾剂(II)(省采)●①② 2盒2000,日入用药,一天2次\n[BBOX-50] 30天\n[BBOX-51] 备注：\n[BBOX-52] 病情评估：\n[BBOX-53] 病情分级：\n[BBOX-54] 是否抢救病例：否\n[BBOX-55] 是否抢救成功：\n[BBOX-56] 是否为绿色通道患者：否\n[BBOX-57] 病人去向：\n[BBOX-58] CS 扫描全能王\n[BBOX-59] 3亿人都在用的扫描App\n[BBOX-60] 就诊卡\n[BBOX-61] 流水号：\n[BBOX-62] 姓名\n[BBOX-63] 龄：40岁\n[BBOX-64] 就诊科\n[BBOX-65] 日：2025-10-24 15:45:39\n[BBOX-66] 主诉：安全性电话随访\n[BBOX-67] 现病史：今日10:27\n[BBOX-68] 固定电话（020-\n[BBOX-69] （159\n[BBOX-70] 5），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无\n[BBOX-71] 不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对\n[BBOX-72] V8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试\n[BBOX-73] 者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，\n[BBOX-74] 目前无安全性异常表现。\n[BBOX-75] 合并用药更新：\n[BBOX-76] 1、小柴胡颗粒、（自行购药）2025.10.6-2025.10.8 10g tid 治疗上呼吸道感染\n[BBOX-77] 2、苯环喹溴铵鼻喷雾剂 2025.4.3-至今 每鼻2喷/次 qid 治疗过敏性鼻炎\n[BBOX-78] 3、氮卓斯汀氟替卡松鼻喷雾剂 2025.9.3-至今 每鼻2喷/次 bid 治疗过敏性鼻炎\n[BBOX-79] 4、辛芩颗粒 2024.8.21-2024.8.27 1袋 冲服 tid 治疗过敏性鼻炎\n[BBOX-80] AE：\n[BBOX-81] 上呼吸道感染 2025年10月5日-2025年10月8日 中度，非SAE，采取药物治疗措施，对试验\n[BBOX-82] 药物采取措施：剂量不变，与试验药物无关，未因该AE退出研究。\n[BBOX-83] 病历更正：\n[BBOX-84] 1、更正2024年10月22日病历，合并用药“辛芩颗粒”为“辛芩颗粒”；\n[BBOX-85] 2、更正2024年10月22日病历，合并用药“苯环喹溴铵鼻喷雾剂”为“苯环喹溴铵鼻喷雾\n[BBOX-86] 剂”；\n[BBOX-87] 3、更正2026年1月24日病历，“无收到ePro触发的哮喘警报邮件”为“有收到ePro触发的哮\n[BBOX-88] 喘警报邮件”；\n[BBOX-89] 4、更正2025年7月18日病历，“受试者漏填2025年4月28日晚间日志” 更正为：“受试者\n[BBOX-90] 漏填2025年4月28日早间日志”；\n[BBOX-91] 5、更正2024年11月6日病历，“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共\n[BBOX-92] 计用了26喷”为：“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了28\n[BBOX-93] 喷”。\n[BBOX-94] 随行中·\n[BBOX-95] 病历编号：\n[BBOX-96] 姓名：\n[BBOX-97] 性别：\n[BBOX-98] 年龄：40岁\n[BBOX-99] 就诊科室：\n[BBOX-100] 就诊时间：2025-11-17 10:10:48\n[BBOX-101] 主诉：支气管哮喘治疗后复查：\n[BBOX-102] 现病史：2021年2月前开始出现咳嗽、咯痰，粘白，量中，能咯出，咳嗽呈阵发性、刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏。无咽痛，无伴反酸、嗳气、腹胀。无上腹部隐痛不适感，无伴发热、畏寒，影响睡眠。晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：\n[BBOX-103] 12.52*109/L 嗜酸粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定。本次门诊距上次门诊间隔时间30天。症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确。急性发作情况：两次，就诊期间急性发作：无，发作次数：0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。近3天来出现咽痛不适\n[BBOX-104] 既往史：鼻炎病史无规则治疗。打鼾明显。\n[BBOX-105] 过敏史：未发现。\n[BBOX-106] 个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。\n[BBOX-107] 体格检查：神志清，颈软，双肺呼吸音粗，未闻及明显干、湿性罗音，口腔粘膜无白斑。\n[BBOX-108] 专科情况：\n[BBOX-109] 辅助检查：\n[BBOX-110] 治疗项目：\n[BBOX-111] 门诊诊断：\n[BBOX-112] 1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、阻塞性睡眠呼吸暂停低通气综合征,4、急性咽炎\n[BBOX-113] 单病种：\n[BBOX-114] 发病时间：\n[BBOX-115] 处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不适随诊。\n[BBOX-116] 1金银花口服液◆⑤ 2盒 20.0ml,口服,一天3次(口服) 6天\n[BBOX-117] 2氨卓斯汀氟替卡松鼻喷雾剂◆ 1瓶 2.0喷,喷鼻,一天2次 30天\n[BBOX-118] 3苯环喹溴铵鼻喷雾剂◆ 3瓶 2.0喷,喷鼻,一天4次 30天\n[BBOX-119] 备注：建议在住地附近社区医疗机构随诊。\n[BBOX-120] 门(急)诊处方\n[BBOX-121] 就诊时间:2025-07-18\n[BBOX-122] 就诊科室:内科门诊\n[BBOX-123] 主诊医\n[BBOX-124] 姓名\n[BBOX-125] 性别:男\n[BBOX-126] 年龄:40岁\n[BBOX-127] 卡号:\n[BBOX-128] 患者\n[BBOX-129] 医疗证号:\n[BBOX-130] 处方号\n[BBOX-131] 地址:PT027气雾剂 2024017-呼吸科\n[BBOX-132] 身份证\n[BBOX-133] 诊断:支气管哮喘\n[BBOX-134] 西药处方\n[BBOX-135] 组号\n[BBOX-136] 项目名称\n[BBOX-137] 规格\n[BBOX-138] 总量\n[BBOX-139] 单价\n[BBOX-140] 金额\n[BBOX-141] R:\n[BBOX-142] 布地奈德福莫特罗吸入粉雾剂0.125/0.0006*60吸6盒\n[BBOX-143] 183.41100.46\n[BBOX-144] Sig\n[BBOX-145] 2吸/次,吸入,bid*90天\n[BBOX-146] 门(急)诊处方\n[BBOX-147] 就诊时间:2025-04-25\n[BBOX-148] 就诊科室:内科门诊\n[BBOX-149] 主诊\n[BBOX-150] 姓名\n[BBOX-151] 性别:男\n[BBOX-152] 年龄:40岁\n[BBOX-153] 卡号:\n[BBOX-154] 患者类型:GLP支付\n[BBOX-155] 医疗证号:\n[BBOX-156] 处方号\n[BBOX-157] 地址:PT027气雾剂 2024017-呼吸科\n[BBOX-158] 身份证号:\n[BBOX-159] 诊断:支气管哮喘\n[BBOX-160] 西药处方\n[BBOX-161] 组号\n[BBOX-162] 项目名称\n[BBOX-163] 规格\n[BBOX-164] 总量\n[BBOX-165] 单价\n[BBOX-166] 金额\n[BBOX-167] R:\n[BBOX-168] 布地奈德福莫特罗吸入粉雾剂(II)●●@ug*60吸6盒\n[BBOX-169] 183.41100.46\n[BBOX-170] Sig\n[BBOX-171] 2吸/次,吸入,bid*90天\n[BBOX-172] 门(急)诊处方\n[BBOX-173] 就诊时间：2025-02-26\n[BBOX-174] 就诊科室：内科门诊\n[BBOX-175] 主诊\n[BBOX-176] 性别：男\n[BBOX-177] 年龄：40岁\n[BBOX-178] 卡号\n[BBOX-179] 医疗证号：\n[BBOX-180] 处方\n[BBOX-181] 015\n[BBOX-182] 地址：PT027气雾剂 2024017-呼吸科\n[BBOX-183] 身份证号：\n[BBOX-184] 诊断：支气管哮喘\n[BBOX-185] 西药处方\n[BBOX-186] 组号\n[BBOX-187] 项目名称\n[BBOX-188] 规格\n[BBOX-189] 总量\n[BBOX-190] 单价\n[BBOX-191] 金额\n[BBOX-192] R:\n[BBOX-193] 布地奈德福莫特罗吸入粉雾剂BUD/●@1g*60吸2盒\n[BBOX-194] 183.41\n[BBOX-195] 366.82\n[BBOX-196] Sig\n[BBOX-197] 2吸/次,吸入,bid*30天\n[BBOX-198] 门(急)诊处方\n[BBOX-199] 就诊时间:2025-01-24\n[BBOX-200] 就诊科室:内科门诊\n[BBOX-201] 主诊医\n[BBOX-202] 姓名\n[BBOX-203] 性别:男\n[BBOX-204] 年龄:40岁\n[BBOX-205] 卡号:4\n[BBOX-206] 患者类型:GCP支付\n[BBOX-207] 医疗证号:\n[BBOX-208] 处方号:\n[BBOX-209] 地址:PT027气雾剂 2024017-呼吸科\n[BBOX-210] 身份证号:\n[BBOX-211] 诊断:支气管哮喘\n[BBOX-212] 西药处方\n[BBOX-213] 组号\n[BBOX-214] 项目名称\n[BBOX-215] 规格\n[BBOX-216] 总量\n[BBOX-217] 单价\n[BBOX-218] 金额\n[BBOX-219] R:\n[BBOX-220] 布地奈德福莫特罗吸入粉雾剂HIV●@1ug*60吸4盒\n[BBOX-221] 183.41 733.64\n[BBOX-222] Sig\n[BBOX-223] 2吸/次,吸入,bid*60天\n[BBOX-224] 门(急)诊处方\n[BBOX-225] 就诊时间:2025-01-03\n[BBOX-226] 就诊科室:内科门诊\n[BBOX-227] 主诊\n[BBOX-228] 性别:男\n[BBOX-229] 年龄:40岁\n[BBOX-230] 卡号\n[BBOX-231] 患者类型:GCP支付\n[BBOX-232] 医疗证号:\n[BBOX-233] 处方\n[BBOX-234] 地址:PT027气雾剂 2024017-呼吸科\n[BBOX-235] 身份证号:\n[BBOX-236] 诊断:支气管哮喘\n[BBOX-237] 西药处方\n[BBOX-238] 组号\n[BBOX-239] 项目名称\n[BBOX-240] 规格\n[BBOX-241] 总量\n[BBOX-242] 单价\n[BBOX-243] 金额\n[BBOX-244] R:\n[BBOX-245] 布地奈德福莫特罗吸入粉雾剂(Ⅱ)●●60ug*60吸2盒\n[BBOX-246] 183.41 366.82\n[BBOX-247] Sig\n[BBOX-248] 2吸/次,吸入,bid*30天\n[BBOX-249] 医师:\n[BBOX-250] 医生编号:1326\n[BBOX-251] 配剂人:\n[BBOX-252] 核对人:\n[BBOX-253] 合计:\n[BBOX-254] 收费员:\n[BBOX-255] CS 扫描全能王\n[BBOX-256] 3亿人都在用的扫描App\n[BBOX-257] 门(急)诊处方\n[BBOX-258] 就诊时间:2024-12-04\n[BBOX-259] 就诊科室:内科门诊\n[BBOX-260] 姓名\n[BBOX-261] 性别:男\n[BBOX-262] 年龄:39岁\n[BBOX-263] 卡号\n[BBOX-264] 患者\n[BBOX-265] 医疗证号:\n[BBOX-266] 处方\n[BBOX-267] 地址:PT027气雾剂 2024017-呼吸科\n[BBOX-268] 身份证号:\n[BBOX-269] 诊断:支气管哮喘\n[BBOX-270] 西药处方\n[BBOX-271] 组号\n[BBOX-272] 项目名称\n[BBOX-273] 规格\n[BBOX-274] 总量\n[BBOX-275] 单价\n[BBOX-276] 金额\n[BBOX-277] R:\n[BBOX-278] 布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●(50ug*60吸2盒\n[BBOX-279] 183.41 366.82\n[BBOX-280] Sig\n[BBOX-281] 2吸/次,吸入,bid*30天\n[BBOX-282] 激发试验检查报告\n[BBOX-283] 姓名：\n[BBOX-284] 测试号：\n[BBOX-285] 门诊/住院号：\n[BBOX-286] 000\n[BBOX-287] 年龄：\n[BBOX-288] 出生日期：\n[BBOX-289] 19\n[BBOX-290] 性别：\n[BBOX-291] 男\n[BBOX-292] 身高：\n[BBOX-293] 170\n[BBOX-294] 病区：\n[BBOX-295] 内科门诊\n[BBOX-296] 体重：\n[BBOX-297] 81 kg\n[BBOX-298] 机器编号：\n[BBOX-299] 床号：\n[BBOX-300] 电话：\n[BBOX-301] Pred\n[BBOX-302] A1\n[BBOX-303] A1/Pd\n[BBOX-304] NS\n[BBOX-305] P1 chg%1\n[BBOX-306] P2 chg%2\n[BBOX-307] P3 chg%3\n[BBOX-308] FVC\n[BBOX-309] [L]\n[BBOX-310] 4.84\n[BBOX-311] 4.69\n[BBOX-312] 97.1\n[BBOX-313] 4.29\n[BBOX-314] 4.22\n[BBOX-315] -10.1\n[BBOX-316] 3.64\n[BBOX-317] -22.5\n[BBOX-318] 4.01\n[BBOX-319] -14.6\n[BBOX-320] PEV 1\n[BBOX-321] [L]\n[BBOX-322] 4.01\n[BBOX-323] 3.05\n[BBOX-324] 76.2\n[BBOX-325] 2.72\n[BBOX-326] 2.69\n[BBOX-327] -11.8\n[BBOX-328] 2.24\n[BBOX-329] -26.5\n[BBOX-330] 2.44\n[BBOX-331] -20.0\n[BBOX-332] PEV 1 % PVC\n[BBOX-333] [%]\n[BBOX-334] 83.32\n[BBOX-335] 65.02\n[BBOX-336] 78.0\n[BBOX-337] 63.54\n[BBOX-338] 63.83\n[BBOX-339] -1.82\n[BBOX-340] 61.73\n[BBOX-341] -5.06\n[BBOX-342] 60.92\n[BBOX-343] -6.30\n[BBOX-344] PEV 1 % VC MAX\n[BBOX-345] [%]\n[BBOX-346] 80.55\n[BBOX-347] 64.94\n[BBOX-348] 80.6\n[BBOX-349] 62.34\n[BBOX-350] 63.83\n[BBOX-351] -1.70\n[BBOX-352] 61.73\n[BBOX-353] -4.94\n[BBOX-354] 60.92\n[BBOX-355] -6.18\n[BBOX-356] VC MAX\n[BBOX-357] [L]\n[BBOX-358] 5.05\n[BBOX-359] 4.70\n[BBOX-360] 93.1\n[BBOX-361] 4.37\n[BBOX-362] 4.22\n[BBOX-363] -10.2\n[BBOX-364] 3.64\n[BBOX-365] -22.6\n[BBOX-366] 4.01\n[BBOX-367] -14.7\n[BBOX-368] PEP\n[BBOX-369] [L/s]\n[BBOX-370] 9.37\n[BBOX-371] 9.95\n[BBOX-372] 106.2\n[BBOX-373] 9.06\n[BBOX-374] 7.81\n[BBOX-375] -21.5\n[BBOX-376] 6.73\n[BBOX-377] -32.3\n[BBOX-378] 8.22\n[BBOX-379] -17.4\n[BBOX-380] MMEF 75/25\n[BBOX-381] [L/s]\n[BBOX-382] 4.52\n[BBOX-383] 1.54\n[BBOX-384] 34.1\n[BBOX-385] 1.33\n[BBOX-386] 1.34\n[BBOX-387] -12.9\n[BBOX-388] 1.14\n[BBOX-389] -25.8\n[BBOX-390] 1.23\n[BBOX-391] -20.0\n[BBOX-392] MEF 50\n[BBOX-393] [L/s]\n[BBOX-394] 5.17\n[BBOX-395] 1.97\n[BBOX-396] 38.1\n[BBOX-397] 1.66\n[BBOX-398] 1.71\n[BBOX-399] -13.4\n[BBOX-400] 1.34\n[BBOX-401] -31.8\n[BBOX-402] 1.42\n[BBOX-403] -28.0\n[BBOX-404] MEF 25\n[BBOX-405] [L/s]\n[BBOX-406] 2.29\n[BBOX-407] 0.58\n[BBOX-408] 25.5\n[BBOX-409] 0.52\n[BBOX-410] 0.53\n[BBOX-411] -9.87\n[BBOX-412] 0.50\n[BBOX-413] -14.6\n[BBOX-414] 0.49\n[BBOX-415] -15.7\n[BBOX-416] PET\n[BBOX-417] [s]\n[BBOX-418] 6.72\n[BBOX-419] 6.87\n[BBOX-420] 6.93\n[BBOX-421] 3.16\n[BBOX-422] 6.75\n[BBOX-423] 0.57\n[BBOX-424] 6.74\n[BBOX-425] 0.38\n[BBOX-426] V backextrapolation ex\n[BBOX-427] [L]\n[BBOX-428] 0.13\n[BBOX-429] 0.09\n[BBOX-430] 0.10\n[BBOX-431] -20.0\n[BBOX-432] 0.08\n[BBOX-433] -41.6\n[BBOX-434] 0.08\n[BBOX-435] -38.5\n[BBOX-436] PIF\n[BBOX-437] [L/s]\n[BBOX-438] 8.04\n[BBOX-439] 7.96\n[BBOX-440] 7.58\n[BBOX-441] -5.76\n[BBOX-442] 6.16\n[BBOX-443] -23.3\n[BBOX-444] 7.78\n[BBOX-445] -3.20\n[BBOX-446] FIF 50\n[BBOX-447] [L/s]\n[BBOX-448] 7.99\n[BBOX-449] 7.86\n[BBOX-450] 7.16\n[BBOX-451] -10.3\n[BBOX-452] 5.36\n[BBOX-453] -32.9\n[BBOX-454] 7.08\n[BBOX-455] -11.3\n[BBOX-456] MVV\n[BBOX-457] [L/min]\n[BBOX-458] 141.88\n[BBOX-459] BF MVV\n[BBOX-460] [1/min]\n[BBOX-461] Cumulated dose\n[BBOX-462] 0.072 0.078\n[BBOX-463] 0.312\n[BBOX-464] 2 Puf\n[BBOX-465] F/V ex\n[BBOX-466] F/V in\n[BBOX-467] Vol [L]\n[BBOX-468] Vol%VCmax\n[BBOX-469] VCmax\n[BBOX-470] Time [s]\n[BBOX-471] PD[-20] FEV 1: 0.2117 mg Cumulated\n[BBOX-472] PD[-20] PEF: < 0.078 mg Cumulated\n[BBOX-473] PD[] FEV1%I: could not be calculated!\n[BBOX-474] 意见：\n[BBOX-475] 2022/6/08 10:23:56上午\n[BBOX-476] 1.轻度阻塞性通气功能障碍。\n[BBOX-477] 2.支气管激发试验阳性(累计吸入乙酰甲胆碱0.312mg，FEV1下降大于20%，PD20=0.2117mg，气道高反应性(AHR)为中度\n[BBOX-478] 通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后FEV1恢复至预计值80%。\n[BBOX-479] CS 扫描全能王\n[BBOX-480] 3亿人都在用的扫描App\n[BBOX-481] 检查日期：2021/1/21\n[BBOX-482] 检查时间：16:43\n[BBOX-483] 编号：16\n[BBOX-484] 广州医科大学附属第三医院\n[BBOX-485] 支气管扩张试验检查报告\n[BBOX-486] 姓名：\n[BBOX-487] 测试号：\n[BBOX-488] 年龄：36岁\n[BBOX-489] 性别：男\n[BBOX-490] 病区：\n[BBOX-491] 机器编号：\n[BBOX-492] 门诊/住院号：\n[BBOX-493] 出生日期：\n[BBOX-494] 身高：\n[BBOX-495] 体重：\n[BBOX-496] 床号：\n[BBOX-497] 电话：\n[BBOX-498] Pred\n[BBOX-499] A1\n[BBOX-500] A1/Pd\n[BBOX-501] P1\n[BBOX-502] A2/Pd\n[BBOX-503] chg%1\n[BBOX-504] P2\n[BBOX-505] A3/Pd\n[BBOX-506] chg%2\n[BBOX-507] P3\n[BBOX-508] A4/Pd\n[BBOX-509] chg%3\n[BBOX-510] FVC\n[BBOX-511] [L]\n[BBOX-512] 4.86\n[BBOX-513] 3.48\n[BBOX-514] 71.5%\n[BBOX-515] 4.01\n[BBOX-516] 82.4%\n[BBOX-517] 15.19\n[BBOX-518] 4.15\n[BBOX-519] 85.4%\n[BBOX-520] 19.47\n[BBOX-521] 4.01\n[BBOX-522] 82.6%\n[BBOX-523] 15.47\n[BBOX-524] FEV 1\n[BBOX-525] [L]\n[BBOX-526] 4.03\n[BBOX-527] 1.97\n[BBOX-528] 48.8%\n[BBOX-529] 2.33\n[BBOX-530] 57.9%\n[BBOX-531] 18.59\n[BBOX-532] 2.33\n[BBOX-533] 57.8%\n[BBOX-534] 18.48\n[BBOX-535] 2.44\n[BBOX-536] 60.5%\n[BBOX-537] 24.02\n[BBOX-538] FEV 1 % FVC\n[BBOX-539] [%]\n[BBOX-540] 83.32\n[BBOX-541] 56.62\n[BBOX-542] 68.0%\n[BBOX-543] 58.29\n[BBOX-544] 70.0%\n[BBOX-545] 2.95\n[BBOX-546] 56.15\n[BBOX-547] 67.4%\n[BBOX-548] -0.83\n[BBOX-549] 60.81\n[BBOX-550] 73.0%\n[BBOX-551] 7.40\n[BBOX-552] FEV 1 % VC MAX\n[BBOX-553] [%]\n[BBOX-554] 80.73\n[BBOX-555] 56.07\n[BBOX-556] 69.5%\n[BBOX-557] 58.29\n[BBOX-558] 72.2%\n[BBOX-559] 3.96\n[BBOX-560] 56.15\n[BBOX-561] 69.5%\n[BBOX-562] 0.14\n[BBOX-563] 60.81\n[BBOX-564] 75.3%\n[BBOX-565] 8.45\n[BBOX-566] VC MAX\n[BBOX-567] [L]\n[BBOX-568] 5.08\n[BBOX-569] 3.51\n[BBOX-570] 69.1%\n[BBOX-571] 4.01\n[BBOX-572] 78.9%\n[BBOX-573] 14.07\n[BBOX-574] 4.15\n[BBOX-575] 81.8%\n[BBOX-576] 18.31\n[BBOX-577] 4.01\n[BBOX-578] 79.1%\n[BBOX-579] 14.35\n[BBOX-580] PEF\n[BBOX-581] [L/s]\n[BBOX-582] 9.41\n[BBOX-583] 6.61\n[BBOX-584] 70.3%\n[BBOX-585] 7.99\n[BBOX-586] 85.0%\n[BBOX-587] 20.93\n[BBOX-588] 7.91\n[BBOX-589] 84.1%\n[BBOX-590] 19.63\n[BBOX-591] 8.07\n[BBOX-592] 85.7%\n[BBOX-593] 22.02\n[BBOX-594] MMEF 75/25\n[BBOX-595] [L/s]\n[BBOX-596] 4.57\n[BBOX-597] 0.81\n[BBOX-598] 17.7%\n[BBOX-599] 0.96\n[BBOX-600] 21.1%\n[BBOX-601] 19.59\n[BBOX-602] 1.03\n[BBOX-603] 22.6%\n[BBOX-604] 28.17\n[BBOX-605] 1.12\n[BBOX-606] 24.6%\n[BBOX-607] 39.07\n[BBOX-608] MEF 50\n[BBOX-609] [L/s]\n[BBOX-610] 5.20\n[BBOX-611] 1.00\n[BBOX-612] 19.2%\n[BBOX-613] 1.29\n[BBOX-614] 24.8%\n[BBOX-615] 29.25\n[BBOX-616] 1.30\n[BBOX-617] 24.9%\n[BBOX-618] 29.87\n[BBOX-619] 1.53\n[BBOX-620] 29.3%\n[BBOX-621] 52.75\n[BBOX-622] MEF 25\n[BBOX-623] [L/s]\n[BBOX-624] 2.32\n[BBOX-625] 0.39\n[BBOX-626] 16.7%\n[BBOX-627] 0.38\n[BBOX-628] 16.4%\n[BBOX-629] -1.68\n[BBOX-630] 0.50\n[BBOX-631] 21.6%\n[BBOX-632] 29.78\n[BBOX-633] 0.41\n[BBOX-634] 17.9%\n[BBOX-635] 7.18\n[BBOX-636] FET\n[BBOX-637] [s]\n[BBOX-638] 15.24\n[BBOX-639] 6.42\n[BBOX-640] -57.87\n[BBOX-641] 6.30\n[BBOX-642] -58.63\n[BBOX-643] 6.55\n[BBOX-644] -57.05\n[BBOX-645] V backextrapolati\n[BBOX-646] [L/s]\n[BBOX-647] 0.07\n[BBOX-648] 0.07\n[BBOX-649] 0.89\n[BBOX-650] 0.09\n[BBOX-651] 17.79\n[BBOX-652] 0.08\n[BBOX-653] 6.12\n[BBOX-654] PIF\n[BBOX-655] [L/s]\n[BBOX-656] 7.03\n[BBOX-657] 7.39\n[BBOX-658] 5.19\n[BBOX-659] 7.17\n[BBOX-660] 1.99\n[BBOX-661] 7.16\n[BBOX-662] 1.91\n[BBOX-663] FIV1\n[BBOX-664] [L]\n[BBOX-665] 3.40\n[BBOX-666] 3.76\n[BBOX-667] 10.58\n[BBOX-668] 3.68\n[BBOX-669] 8.26\n[BBOX-670] 3.60\n[BBOX-671] 5.96\n[BBOX-672] PEF50 % PIF50\n[BBOX-673] [%]\n[BBOX-674] 16.56\n[BBOX-675] 21.70\n[BBOX-676] 31.06\n[BBOX-677] 19.81\n[BBOX-678] 19.65\n[BBOX-679] 24.71\n[BBOX-680] 49.20\n[BBOX-681] MVV\n[BBOX-682] [L/min]\n[BBOX-683] 142.69\n[BBOX-684] BF MVV\n[BBOX-685] [1/min]\n[BBOX-686] 意见：\n[BBOX-687] 1.重度混合性肺通气功能障碍。\n[BBOX-688] 2.支气管舒张试验阳性。\n[BBOX-689] （通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后PEV1较基线增加大于12%，且绝对值增加大于200ml）\n[BBOX-690] CS 扫描全能王\n[BBOX-691] 3亿人都在用的扫描App\n[BBOX-692] 广州医科大学附属第三医院\n[BBOX-693] 处方笺\n[BBOX-694] 普通\n[BBOX-695] 诊疗卡\n[BBOX-696] 患者姓名\n[BBOX-697] 年龄：41岁\n[BBOX-698] 费别：南医保\n[BBOX-699] 科室：内科门诊（荔湾）\n[BBOX-700] 日期：2026-01-05 17:17:14\n[BBOX-701] 处方号\n[BBOX-702] 地址：荔湾\n[BBOX-703] 2024017-呼吸科\n[BBOX-704] 联系电话\n[BBOX-705] 身份号码：\n[BBOX-706] 2739\n[BBOX-707] 诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],急性气管支气管炎\n[BBOX-708] R\n[BBOX-709] P:\n[BBOX-710] 布地奈德福莫特罗吸入粉雾剂(II) 160ug/4.5ug*60吸\n[BBOX-711] 2盒\n[BBOX-712] 剂量：每次2吸\n[BBOX-713] （\n[BBOX-714] 1\n[BBOX-715] 30\n[BBOX-716] 盒）\n[BBOX-717] 用法：吸入用药\n[BBOX-718] bid\n[BBOX-719] 01-05\n[BBOX-720] 处方金额：366.82元\n[BBOX-721] 取药药房：门诊西药房（荔湾）\n[BBOX-722] 广州医科大学附属第三医院\n[BBOX-723] The Third Affiliated Hospital of Guangzhou Medical University\n[BBOX-724] 门(急)诊病历信息\n[BBOX-725] 就诊卡\n[BBOX-726] 流水\n[BBOX-727] 姓\n[BBOX-728] 病历编号:\n[BBOX-729] 年 龄:41岁\n[BBOX-730] 就诊科室:内科门诊(荔湾) 医\n[BBOX-731] 就诊时间:2026-01-05 17:07:54\n[BBOX-732] 主 诉:支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天\n[BBOX-733] 现 病 史:2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激\n[BBOX-734] 性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流\n[BBOX-735] 涕、喷嚏,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响\n[BBOX-736] 睡眠,晨起有咽干,曾到本院就诊两次,症状不见明显缓解。2021-1-9血常规:白细胞:\n[BBOX-737] 12.52*109/L 嗜酸粒细胞:0.65*109/L 5.2%,经治疗后症状明显缓解。无咳嗽、咯痰、气\n[BBOX-738] 促。病情稳定,本次门诊距上次门诊间隔时间30天。症状控制情况:过去4周,患者:吸入\n[BBOX-739] 药物使用情况:遵医嘱使用;吸入装置使用情况:正确。急性发作情况:两次,就诊期间急\n[BBOX-740] 性发作:无,发作次数:0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。长期规律使用信必\n[BBOX-741] 可160/4.5ug 2吸 bid治疗,5天前开始出现咳嗽、咯痰,黄白痰,量少,难以咯出,咳嗽以\n[BBOX-742] 夜间为主。无气促,伴咽息,鼻塞、流涕、喷嚏,无发热。\n[BBOX-743] 既 往 史:鼻炎病史无规则治疗。打鼾明显。\n[BBOX-744] 过 敏 史:未发现;\n[BBOX-745] 个 人 史:否认遗传病史,吸烟10年,20支/日,2018年戒烟。偶饮酒。2021-12-20已打第\n[BBOX-746] 三针新冠疫苗。\n[BBOX-747] 体格检查:神志清,颈软,双肺呼吸音粗,可闻及散在哮鸣音,口腔粘膜无白斑。\n[BBOX-748] 专科情况:\n[BBOX-749] 辅助检查:\n[BBOX-750] 治疗项目:\n[BBOX-751] 门诊诊断:\n[BBOX-752] 1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎\n[BBOX-753] 处 置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。\n[BBOX-754] 布地奈德福莫特罗吸入粉雾剂(II)2盒 2.0吸,吸入用药,一天2次 30天\n[BBOX-755] (省采)●①⑤\n[BBOX-756] 左氧氟沙星片(省采)●⑥ 5片 0.5g,口服,每日1次(口服) 5天\n[BBOX-757] 第1页\n[BBOX-758] 广州医科大学附属第三医院\n[BBOX-759] The Third Affiliated Hospital of Guangzhou Medical University\n[BBOX-760] 门(急)诊病历信息\n[BBOX-761] 复方甲氧那明胶囊(省采)◆② 1瓶 1.0粒,餐后口服,一天3次(口服) 5天\n[BBOX-762] 盐酸氨溴索分散片(省采)●⑥ 15片 30.0mg,餐后口服,一天3次(口服) 5\n[BBOX-763] 天\n[BBOX-764] 醋酸泼尼松片●②④ 6片 10.0mg,口服,每早1次(口服) 3天\n[BBOX-765] 备 注:建议在住地附近社区医疗机构随诊。\n[BBOX-766] 门诊/住院病历信息\n[BBOX-767] 就诊卡号：\n[BBOX-768] 病历编号：\n[BBOX-769] 流水号\n[BBOX-770] 姓名\n[BBOX-771] 性别：男\n[BBOX-772] 年龄：41岁\n[BBOX-773] 就诊科室：内科门诊（荔湾）\n[BBOX-774] 就诊时间：2026-02-04 11:21:11\n[BBOX-775] 主诉：支气管哮喘治疗后复查\n[BBOX-776] 现病史：2021年2月前开始出现咳嗽、咳痰，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sng 2吸 bid治疗。\n[BBOX-777] 既往史：鼻炎病史无规则治疗，打鼾明显。\n[BBOX-778] 过敏史：未发现；\n[BBOX-779] 个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。\n[BBOX-780] 体格检查：神志清，颈软，双肺呼吸音粗，可闻及散在哮鸣音，口腔粘膜无白斑。\n[BBOX-781] 专科情况：\n[BBOX-782] 辅助检查：\n[BBOX-783] 治疗项目：\n[BBOX-784] 门诊诊断：\n[BBOX-785] 1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、急性气管支气管炎\n[BBOX-786] 单病种：\n[BBOX-787] 发病时间：\n[BBOX-788] 处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不遥随诊。\n[BBOX-789] 布地奈德福莫特罗吸入粉雾剂(II)(省\n[BBOX-790] 2 2.0班，吸入用药，一天2次\n[BBOX-791] 30\n[BBOX-792] 采)●①②\n[BBOX-793] 查天\n[BBOX-794] 广州医科大学附属第三医院\n[BBOX-795] 肺功能检查报告\n[BBOX-796] 地址：广州市多宝路63号 电话：020-81292126\n[BBOX-797] COSMED\n[BBOX-798] 姓名：\n[BBOX-799] 科室/床号：\n[BBOX-800] ID：\n[BBOX-801] 出生日期：1984/12/8\n[BBOX-802] 预计值：ERS 93\n[BBOX-803] 日期：2024/10/22\n[BBOX-804] 性别：Male\n[BBOX-805] 地区修正：Chinese\n[BBOX-806] 详细描述：内科门诊\n[BBOX-807] Company：\n[BBOX-808] 年龄：39\n[BBOX-809] 体重(Kg)：89.0\n[BBOX-810] 身高(cm)：177.5\n[BBOX-811] BMI(Kg/m²：28.2\n[BBOX-812] 吸烟：曾经(10/20)\n[BBOX-813] 用力肺活量 Forced Vital Capacity\n[BBOX-814] F(l/s)\n[BBOX-815] V(l)\n[BBOX-816] BEST #3 - 2024/10/22 11:03\n[BBOX-817] 沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38\n[BBOX-818] 沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39\n[BBOX-819] 沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41\n[BBOX-820] 沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38\n[BBOX-821] 沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39\n[BBOX-822] 沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41\n[BBOX-823] BEST #3 - 2024/10/22 11:03\n[BBOX-824] FVC\n[BBOX-825] PEF\n[BBOX-826] MEF75%\n[BBOX-827] MEF50%\n[BBOX-828] MEF25%\n[BBOX-829] FVC\n[BBOX-830] 8V(l)\n[BBOX-831] FEV1\n[BBOX-832] ATS\n[BBOX-833] 12t(s)\n[BBOX-834] -1 0 1 2 3 4 5 6 7 8 9 10 11 12t(s)\n[BBOX-835] 218133\n[BBOX-836] ST\n[BBOX-837] 2024-10-22\n[BBOX-838] Parameter\n[BBOX-839] UM\n[BBOX-840] Pred.\n[BBOX-841] BEST#3\n[BBOX-842] %Pred.\n[BBOX-843] POST#4\n[BBOX-844] %Pred.\n[BBOX-845] %Test#3\n[BBOX-846] POST#5\n[BBOX-847] %Pred.\n[BBOX-848] %Test#3\n[BBOX-849] POST#6\n[BBOX-850] %F\n[BBOX-851] FVC\n[BBOX-852] l(btps)\n[BBOX-853] 4.87\n[BBOX-854] 3.48\n[BBOX-855] 71\n[BBOX-856] 3.72\n[BBOX-857] 76\n[BBOX-858] +6.9\n[BBOX-859] 4.24\n[BBOX-860] 87\n[BBOX-861] +22.0\n[BBOX-862] 4.11\n[BBOX-863] FEV1\n[BBOX-864] l(btps)\n[BBOX-865] 4.01\n[BBOX-866] 2.58\n[BBOX-867] 64\n[BBOX-868] 2.94\n[BBOX-869] 73\n[BBOX-870] +13.7\n[BBOX-871] 3.15\n[BBOX-872] 79\n[BBOX-873] +21.9\n[BBOX-874] 3.15\n[BBOX-875] FEV1/FVC%\n[BBOX-876] %\n[BBOX-877] 80.2\n[BBOX-878] 74.3\n[BBOX-879] 93\n[BBOX-880] 79.0\n[BBOX-881] 98\n[BBOX-882] +6.4\n[BBOX-883] 74.2\n[BBOX-884] 93\n[BBOX-885] 0.0\n[BBOX-886] 76.6\n[BBOX-887] PEF\n[BBOX-888] l/sec\n[BBOX-889] 9.37\n[BBOX-890] 9.86\n[BBOX-891] 105\n[BBOX-892] 9.98\n[BBOX-893] 107\n[BBOX-894] +1.3\n[BBOX-895] 10.48\n[BBOX-896] 112\n[BBOX-897] +6.3\n[BBOX-898] 10.52\n[BBOX-899] 1\n[BBOX-900] FEV6\n[BBOX-901] l(btps)\n[BBOX-902] 5.17\n[BBOX-903] 3.68\n[BBOX-904] 71\n[BBOX-905] 4.22\n[BBOX-906] 82\n[BBOX-907] 4.11\n[BBOX-908] PIF\n[BBOX-909] l/sec\n[BBOX-910] 7.33\n[BBOX-911] 7.76\n[BBOX-912] +5.8\n[BBOX-913] 7.78\n[BBOX-914] +6.1\n[BBOX-915] 7.88\n[BBOX-916] FEV6/FVC%\n[BBOX-917] %\n[BBOX-918] 99.0\n[BBOX-919] 99.4\n[BBOX-920] 100.0\n[BBOX-921] FEF25-75%\n[BBOX-922] l/sec\n[BBOX-923] 4.47\n[BBOX-924] 1.88\n[BBOX-925] 42\n[BBOX-926] 2.59\n[BBOX-927] 58\n[BBOX-928] +37.8\n[BBOX-929] 2.31\n[BBOX-930] 52\n[BBOX-931] +22.8\n[BBOX-932] 2.52\n[BBOX-933] FEV3\n[BBOX-934] l(btps)\n[BBOX-935] 3.25\n[BBOX-936] 3.44\n[BBOX-937] +5.8\n[BBOX-938] 3.94\n[BBOX-939] +21.3\n[BBOX-940] 3.78\n[BBOX-941] FEV3/FVC%\n[BBOX-942] %\n[BBOX-943] 93.3\n[BBOX-944] 92.4\n[BBOX-945] -1.0\n[BBOX-946] 92.9\n[BBOX-947] -0.5\n[BBOX-948] 92.1\n[BBOX-949] FEV1/FEV6%\n[BBOX-950] %\n[BBOX-951] 79.8\n[BBOX-952] 74.7\n[BBOX-953] 76.6\n[BBOX-954] MEF75%\n[BBOX-955] l/sec\n[BBOX-956] 8.09\n[BBOX-957] 5.96\n[BBOX-958] 74\n[BBOX-959] 9.28\n[BBOX-960] 115\n[BBOX-961] +55.7\n[BBOX-962] 7.53\n[BBOX-963] 93\n[BBOX-964] +26.3\n[BBOX-965] 7.17\n[BBOX-966] MEF50%\n[BBOX-967] l/sec\n[BBOX-968] 5.17\n[BBOX-969] 2.57\n[BBOX-970] 50\n[BBOX-971] 3.49\n[BBOX-972] 68\n[BBOX-973] +35.8\n[BBOX-974] 3.08\n[BBOX-975] 59\n[BBOX-976] +19.6\n[BBOX-977] 3.28\n[BBOX-978] MEF25%\n[BBOX-979] l/sec\n[BBOX-980] 2.28\n[BBOX-981] 0.71\n[BBOX-982] 31\n[BBOX-983] 0.95\n[BBOX-984] 42\n[BBOX-985] +33.9\n[BBOX-986] 0.83\n[BBOX-987] 36\n[BBOX-988] +16.6\n[BBOX-989] 0.87\n[BBOX-990] FET100%\n[BBOX-991] sec\n[BBOX-992] 6.0\n[BBOX-993] 6.7\n[BBOX-994] +12.8\n[BBOX-995] 6.5\n[BBOX-996] +9.4\n[BBOX-997] 6.5\n[BBOX-998] VEXT\n[BBOX-999] ml\n[BBOX-1000] 208\n[BBOX-1001] 192\n[BBOX-1002] 162\n[BBOX-1003] IC\n[BBOX-1004] l(btps)\n[BBOX-1005] 3.33\n[BBOX-1006] 3.38\n[BBOX-1007] +1.5\n[BBOX-1008] 3.50\n[BBOX-1009] +5.1\n[BBOX-1010] 3.35\n[BBOX-1011] FIVC\n[BBOX-1012] l(btps)\n[BBOX-1013] 4.29\n[BBOX-1014] 4.70\n[BBOX-1015] +9.6\n[BBOX-1016] 4.51\n[BBOX-1017] +5.1\n[BBOX-1018] 4.46\n[BBOX-1019] PEFr\n[BBOX-1020] l/min\n[BBOX-1021] 562.3\n[BBOX-1022] 591.4\n[BBOX-1023] 105\n[BBOX-1024] 599.0\n[BBOX-1025] 107\n[BBOX-1026] +1.3\n[BBOX-1027] 628.8\n[BBOX-1028] 112\n[BBOX-1029] +6.3\n[BBOX-1030] 630.9\n[BBOX-1031] 1\n[BBOX-1032] 诊断：\n[BBOX-1033] 中度限制性通气功能障碍。支气管舒张试验阳性（吸入沙丁胺醇400μg，FEV1上升>12%，且绝对值>200ml）。\n[BBOX-1034] 打印2024/10/22\n[BBOX-1035] PFT Suite 10.0d\n[BBOX-1036] 页 1 of 1\n[BBOX-1037] CS 扫描全能王\n[BBOX-1038] 3亿人都在用的扫描App"
  }
]
2026-08-10 11:33:00,902 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:33:00,924 INFO     29 [SmartSplitter] SmartSplitter done: 15 chunks from 15 LLM segments (all bbox_id). Types: {'OutpatientRecord': 5, 'PrescriptionRecord': 7, 'ExaminationReport': 3}
2026-08-10 11:33:00,939 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 11:33:00,939 INFO     29 [Trace] task=ea51b5dc | doc=LZK 哮喘 广三(2).pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "1039 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(2).pdf", "output_format": "chunks", "chunks": "15 items, types={'OutpatientRecord': 5, 'PrescriptionRecord': 7, 'ExaminationReport': 3}"}
2026-08-10 11:33:00,939 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 11:33:00,941 INFO     29 [ChunkRouter] Routed 15 chunks into 3 groups: {'chunks_Clinical': 5, 'chunks_Prescription': 7, 'chunks_Examination': 3}
2026-08-10 11:33:00,952 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 11:33:00,952 INFO     29 [Trace] task=ea51b5dc | doc=LZK 哮喘 广三(2).pdf | ChunkRouter:Router | outputs={"html": "", "json": "1039 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(2).pdf", "output_format": "chunks", "chunks": "15 items, types={'OutpatientRecord': 5, 'PrescriptionRecord': 7, 'ExaminationReport': 3}", "chunks_Clinical": "5 items, types={'OutpatientRecord': 5}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 5, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-10 11:33:00,952 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 11:33:00,961 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:33:00,961 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:33:01,649 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:33:01,660 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 11:33:01,661 INFO     29 [Trace] task=ea51b5dc | doc=LZK 哮喘 广三(2).pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "1039 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(2).pdf", "output_format": "chunks", "chunks_Clinical": "5 items, types={'OutpatientRecord': 5}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 5, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-10 11:33:01,661 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 11:33:01,669 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:33:01,669 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:33:02,121 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:33:02,136 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 11:33:02,136 INFO     29 [Trace] task=ea51b5dc | doc=LZK 哮喘 广三(2).pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "1039 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(2).pdf", "output_format": "chunks", "chunks_Clinical": "5 items, types={'OutpatientRecord': 5}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 5, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-10 11:33:02,136 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 11:33:02,149 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:33:02,150 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:33:02,150 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:33:02,151 INFO     29 [qwen-vl-text] positions(60): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:33:02,151 INFO     29 [qwen-vl-text] page grouping: [0, 1], lines per page: [18, 42]
2026-08-10 11:33:02,368 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:33:02,514 INFO     29 [qwen-vl-text] page=1, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:33:02,515 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1742
2026-08-10 11:33:02,515 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:33:02,515 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 59, \"encounter_dates\": [\"2025-10-10\"], \"department\": \"内科门诊（荔湾）\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "病历编号：\n性别：男\n年龄：40岁\n就诊科室：内科门诊（荔湾）\n就诊时间：2025-10-10 14:36:06\n主诉：BAIYUN V8\n现病史：自上次访视至今，询问及查询HIS系统受试者有新增AE，无SAE、哮喘急性发作，有新增合并用药，发生2次医疗相关事件[2025年9月3日因过敏性鼻炎就诊专科门诊、本周曾因上呼吸道感染到社区医院就诊(具体不详，因HIS系统滞后无法收集具体情况及受试者无法回忆起当时情况及用药情况，待收集具体情况后补充详情)]。于2025年8月4日、2025年9月1日收到加重警报邮件，联系受试者后，均判断非哮喘急性发作。\n完成下流操作：\n1、查看受试者电子日志，受试者漏填2025年8月16日，2025年9月4日晚间日志，2025年9月4日、2025年9月25日早间日志；\n2、填写AQLQ+12和ACQ-5问卷，ACQ-5评分：0.8分；\n3、休息10分钟后，测量坐位生命体征：血压113/81mmHg，脉搏87次/分，呼吸频率20次/分，体温36.6℃，测量身高177.5cm，体重90.5kg(BMI=28.7kg/m2)；\n4、14:35体格检查：神志清，体查合作，自主体位，一般外表无异常，皮肤、粘膜无异常，唇甲无发绀，眼睛、耳、鼻、咽喉无异常，口咽部粘膜无异常，颈软，气管居中，甲状腺未及肿大，全身浅表淋巴结未及肿大，颈静脉无怒张，胸廓无畸形，双肺呼吸运动对称，双肺触觉语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及啰音。心前区无隆起，心尖搏动无弥散，心界不大，心率：87次/分，律齐，各瓣膜听诊区未闻及病理性杂音。腹平软，全腹无压痛、反跳痛。肝、脾肋下未及，肝肾区无叩击痛，肠鸣音存，4次/分，脊柱、四肢无畸形，生理征存，未引出病理征，其他系统未见明显异常；\n5、休息至少10分钟后，于14:58行12导联ECG检查；\n6、于15:01采集中心实验室样本(血常规，血生化)并送往中心试验室；\n7、回收试验药物BDAMDI@ASMDI3盒(152968-AH及185936-HK未开封，148729-UA未用60揿，实际使用46揿，发药当天预喷4揿，2025年9月10日前因超过7天未使用试验药物空喷2次共4揿，2025年9月10日后受试者每七天清洗一次后空喷5次共10揿，总计预喷18揿；epro记录使用总共46揿，与实际使用情况一致。\n8、回收epro以及AM3。\n既往史：更新合并用药：\n1、糠酸莫米松鼻喷雾剂2025.4.3-2025.7.25 每鼻 2喷/次 qm 治疗过敏性鼻炎。\n病历文书\n门诊病历\n25/10/10 14时 门诊病历\n25/10/24 15时 门诊病历（GCP专用）\n25/11/17 10时 门诊病历\n头降使用40瓶，平均每天使用4瓶，2025年9月10日用完4瓶（大木使用试验药剂空瓶2次共4\n瓶，2025年9月10日后受试者每七天青光一次后空瓶5次共10瓶，总计空瓶10瓶（qrs记录使\n用总共46瓶，与实际使用情况一致。\n8、回访qrs以及MD。\n既往史：更新合并用药：\n1、鼻腔莫米松鼻喷雾剂C025 4 3-2025 7 25 每鼻 2喷/次 qd 治疗过敏性鼻炎。\n2、苯环喹氯桉鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。\n4、氯卓斯汀氟替卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。\n5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/\n次 治疗过敏性鼻炎。\n6、枯草抗感染治疗（生理盐水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过\n敏性鼻炎\n已预约受试者安全性随访时间。\n过敏史：\n个人史：\n体格检查：\n专科情况：\n辅助检查：\n治疗项目：\n门诊诊断：\n支气管哮喘\n单病种：\n发病时间：\n处\n置：\n1心电图（心电图室做）\n2布地奈德福莫特罗吸入粉雾剂(II)(省采)●①② 2盒2000,日入用药,一天2次\n30天\n备注：\n病情评估：\n病情分级：\n是否抢救病例：否\n是否抢救成功：\n是否为绿色通道患者：否\n病人去向：\nCS 扫描全能王\n3亿人都在用的扫描App",
    "role": "user"
  }
]
2026-08-10 11:33:10,672 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:33:10.669+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 23, "failed": 0, "current": {"ea51b5dc94ae11f1bd9827cf206dfa2d": {"id": "ea51b5dc94ae11f1bd9827cf206dfa2d", "doc_id": "ea1b0b1894ae11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786361440167, "task_type": "dataflow", "root_trace_id": "bca8d639df704cd29f0107370613ab01", "root_traceparent": "00-bca8d639df704cd29f0107370613ab01-b8b3c91a32048c1c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:33:11,646 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:33:11,647 INFO     29 [qwen-vl-text] LLM output (len=1401):
{
  "encounter_date": "2025-10-10",
  "chief_complaint": "BAIYUN V8",
  "present_illness": "自上次访视至今，询问及查询HIS系统受试者有新增AE，无SAE、哮喘急性发作，有新增合并用药，发生2次医疗相关事件[2025年9月3日因过敏性鼻炎就诊专科门诊、本周曾因上呼吸道感染到社区医院就诊(具体不详，因HIS系统滞后无法收集具体情况及受试者无法回忆起当时情况及用药情况，待收集具体情况后补充详情)]。于2025年8月4日、2025年9月1日收到加重警报邮件，联系受试者后，均判断非哮喘急性发作。完成下流操作：1、查看受试者电子日志，受试者漏填2025年8月16日，2025年9月4日晚间日志，2025年9月4日、2025年9月25日早间日志；2、填写AQLQ+12和ACQ-5问卷，ACQ-5评分：0.8分；3、休息10分钟后，测量坐位生命体征：血压113/81mmHg，脉搏87次/分，呼吸频率20次/分，体温36.6℃，测量身高177.5cm，体重90.5kg(BMI=28.7kg/m2)；4、14:35体格检查：神志清，体查合作，自主体位，一般外表无异常，皮肤、粘膜无异常，唇甲无发绀，眼睛、耳、鼻、咽喉无异常，口咽部粘膜无异常，颈软，气管居中，甲状腺未及肿大，全身浅表淋巴结未及肿大，颈静脉无怒张，胸廓无畸形，双肺呼吸运动对称，双肺触觉语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及啰音。心前区无隆起，心尖搏动无弥散，心界不大，心率：87次/分，律齐，各瓣膜听诊区未闻及病理性杂音。腹平软，全腹无压痛、反跳痛。肝、脾肋下未及，肝肾区无叩击痛，肠鸣音存，4次/分，脊柱、四肢无畸形，生理征存，未引出病理征，其他系统未见明显异常；5、休息至少10分钟后，于14:58行12导联ECG检查；6、于15:01采集中心实验室样本(血常规，血生化)并送往中心试验室；7、回收试验药物BDAMDI@ASMDI3盒(152968-AH及185936-HK未开封，148729-UA未用60揿，实际使用46揿，发药当天预喷4揿，2025年9月10日前因超过7天未使用试验药物空喷2次共4揿，2025年9月10日后受试者每七天清洗一次后空喷5次共10揿，总计预喷18揿；epro记录使用总共46揿，与实际使用情况一致。8、回收epro以及AM3。",
  "past_history": "更新合并用药：1、糠酸莫米松鼻喷雾剂2025.4.3-2025.7.25 每鼻 2喷/次 qm 治疗过敏性鼻炎。2、苯环喹氯桉鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。4、氯卓斯汀氟替卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/次 治疗过敏性鼻炎。6、枯草抗感染治疗（生理盐水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过敏性鼻炎",
  "diagnosis": "支气管哮喘",
  "treatment_plan": "1心电图（心电图室做）\n2布地奈德福莫特罗吸入粉雾剂(II)(省采) 2盒 2000,日入用药,一天2次 30天"
}
2026-08-10 11:33:11,647 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-10-10]
2026-08-10 11:33:11,651 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1320554, prompt_len=1732
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共18行）
["病历编号：", "性别：男", "年龄：40岁", "就诊科室：内科门诊（荔湾）", "就诊时间：2025-10-10 14:36:06", "主诉：BAIYUN V8", "现病史：自上次访视至今，询问及查询HIS系统受试者有新增AE，无SAE、哮喘急性发作，有新增合并用药，发生2次医疗相关事件[2025年9月3日因过敏性鼻炎就诊专科门诊、本周曾因上呼吸道感染到社区医院就诊(具体不详，因HIS系统滞后无法收集具体情况及受试者无法回忆起当时情况及用药情况，待收集具体情况后补充详情)]。于2025年8月4日、2025年9月1日收到加重警报邮件，联系受试者后，均判断非哮喘急性发作。", "完成下流操作：", "1、查看受试者电子日志，受试者漏填2025年8月16日，2025年9月4日晚间日志，2025年9月4日、2025年9月25日早间日志；", "2、填写AQLQ+12和ACQ-5问卷，ACQ-5评分：0.8分；", "3、休息10分钟后，测量坐位生命体征：血压113/81mmHg，脉搏87次/分，呼吸频率20次/分，体温36.6℃，测量身高177.5cm，体重90.5kg(BMI=28.7kg/m2)；", "4、14:35体格检查：神志清，体查合作，自主体位，一般外表无异常，皮肤、粘膜无异常，唇甲无发绀，眼睛、耳、鼻、咽喉无异常，口咽部粘膜无异常，颈软，气管居中，甲状腺未及肿大，全身浅表淋巴结未及肿大，颈静脉无怒张，胸廓无畸形，双肺呼吸运动对称，双肺触觉语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及啰音。心前区无隆起，心尖搏动无弥散，心界不大，心率：87次/分，律齐，各瓣膜听诊区未闻及病理性杂音。腹平软，全腹无压痛、反跳痛。肝、脾肋下未及，肝肾区无叩击痛，肠鸣音存，4次/分，脊柱、四肢无畸形，生理征存，未引出病理征，其他系统未见明显异常；", "5、休息至少10分钟后，于14:58行12导联ECG检查；", "6、于15:01采集中心实验室样本(血常规，血生化)并送往中心试验室；", "7、回收试验药物BDAMDI@ASMDI3盒(152968-AH及185936-HK未开封，148729-UA未用60揿，实际使用46揿，发药当天预喷4揿，2025年9月10日前因超过7天未使用试验药物空喷2次共4揿，2025年9月10日后受试者每七天清洗一次后空喷5次共10揿，总计预喷18揿；epro记录使用总共46揿，与实际使用情况一致。", "8、回收epro以及AM3。", "既往史：更新合并用药：", "1、糠酸莫米松鼻喷雾剂2025.4.3-2025.7.25 每鼻 2喷/次 qm 治疗过敏性鼻炎。"]

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
2026-08-10 11:33:23,025 INFO     29 [qwen-vl-text] coord API raw response (len=1890):
[
	{"text": "病历编号：", "bbox": [541, 117, 617, 134]},
	{"text": "性别：男", "bbox": [438, 150, 501, 167], "bbox": [438, 150, 501, 167]},
	{"text": "年龄：40岁", "bbox": [627, 151, 690, 167]},
	{"text": "就诊科室：内科门诊（荔湾）", "bbox": [162, 182, 372, 199]},
	{"text": "就诊时间：2025-10-10 14:36:06", "bbox": [541, 183, 795, 199]},
	{"text": "主诉：BAIYUN V8", "bbox": [160, 214, 400, 231]},
	{"text": "现病史：自上次访视至今，询问及查询HIS系统受试者有新增AE，无SAE、哮喘急性发作，有新增合并用药，发生2次医疗相关事件[2025年9月3日因过敏性鼻炎就诊专科门诊、本周曾因上呼吸道感染到社区医院就诊(具体不详，因HIS系统滞后无法收集具体情况及受试者无法回忆起当时情况及用药情况，待收集具体情况后补充详情)]。于2025年8月4日、2025年9月1日收到加重警报邮件，联系受试者后，均判断非哮喘急性发作。", "bbox": [160, 245, 855, 345]},
	{"text": "完成下流操作：", "bbox": [160, 359, 275, 375]},
	{"text": "1、查看受试者电子日志，受试者漏填2025年8月16日，2025年9月4日晚间日志，2025年9月4日、2025年9月25日早间日志；", "bbox": [160, 389, 851, 425]},
	{"text": "2、填写AQLQ+12和ACQ-5问卷，ACQ-5评分：0.8分；", "bbox": [160, 439, 540, 455]},
	{"text": "3、休息10分钟后，测量坐位生命体征：血压113/81mmHg，脉搏87次/分，呼吸频率20次/分，体温36.6℃，测量身高177.5cm，体重90.5kg(BMI=28.7kg/m2)；", "bbox": [160, 468, 822, 505]},
	{"text": "4、14:35体格检查：神志清，体查合作，自主体位，一般外表无异常，皮肤、粘膜无异常，唇甲无发绀，眼睛、耳、鼻、咽喉无异常，口咽部粘膜无异常，颈软，气管居中，甲状腺未及肿大，全身浅表淋巴结未及肿大，颈静脉无怒张，胸廓无畸形，双肺呼吸运动对称，双肺触觉语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及啰音。心前区无隆起，心尖搏动无弥散，心界不大，心率：87次/分，律齐，各瓣膜听诊区未闻及病理性杂音。腹平软，全腹无压痛、反跳痛。肝、脾肋下未及，肝肾区无叩击痛，肠鸣音存，4次/分，脊柱、四肢无畸形，生理征存，未引出病理征，其他系统未见明显异常；", "bbox": [160, 519, 842, 658]},
	{"text": "5、休息至少10分钟后，于14:58行12导联ECG检查；", "bbox": [160, 672, 532, 688]},
	{"text": "6、于15:01采集中心实验室样本(血常规，血生化)并送往中心试验室；", "bbox": [160, 702, 672, 718]},
	{"text": "7、回收试验药物BDAMDI@ASMDI3盒(152968-AH及185936-HK未开封，148729-UA未用60揿，实际使用46揿，发药当天预喷4揿，2025年9月10日前因超过7天未使用试验药物空喷2次共4揿，2025年9月10日后受试者每七天清洗一次后空喷5次共10揿，总计预喷18揿；epro记录使用总共46揿，与实际使用情况一致。", "bbox": [160, 732, 822, 809]},
	{"text": "8、回收epro以及AM3。", "bbox": [160, 823, 325, 839]},
	{"text": "既往史：更新合并用药：", "bbox": [160, 854, 379, 870]},
	{"text": "1、糠酸莫米松鼻喷雾剂2025.4.3-2025.7.25 每鼻 2喷/次 qm 治疗过敏性鼻炎。", "bbox": [160, 883, 767, 899]}
]
2026-08-10 11:33:23,025 INFO     29 [qwen-vl-text] coord API: raw_items=18, valid_items=18, elapsed=11.4s
2026-08-10 11:33:23,025 INFO     29 [qwen-vl-text] coord item[0]: text=病历编号：, bbox=[541, 117, 617, 134]
2026-08-10 11:33:23,025 INFO     29 [qwen-vl-text] coord item[1]: text=性别：男, bbox=[438, 150, 501, 167]
2026-08-10 11:33:23,025 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：40岁, bbox=[627, 151, 690, 167]
2026-08-10 11:33:23,025 INFO     29 [qwen-vl-text] coord item[3]: text=就诊科室：内科门诊（荔湾）, bbox=[162, 182, 372, 199]
2026-08-10 11:33:23,025 INFO     29 [qwen-vl-text] coord item[4]: text=就诊时间：2025-10-10 14:36:06, bbox=[541, 183, 795, 199]
2026-08-10 11:33:23,025 INFO     29 [qwen-vl-text] coord item[5]: text=主诉：BAIYUN V8, bbox=[160, 214, 400, 231]
2026-08-10 11:33:23,025 INFO     29 [qwen-vl-text] coord item[6]: text=现病史：自上次访视至今，询问及查询HIS系统受试者有新增AE，无SAE、哮喘急性发作，有新增合并用药，发生2次医疗相关事件[2025年9月3日因过敏性鼻炎就诊专科门诊、本周曾因上呼吸道感染到社区医院就诊(具体不详，因HIS系统滞后无法收集具体情况及受试者无法回忆起当时情况及用药情况，待收集具体情况后补充详情)]。于2025年8月4日、2025年9月1日收到加重警报邮件，联系受试者后，均判断非哮喘急性发作。, bbox=[160, 245, 855, 345]
2026-08-10 11:33:23,025 INFO     29 [qwen-vl-text] coord item[7]: text=完成下流操作：, bbox=[160, 359, 275, 375]
2026-08-10 11:33:23,025 INFO     29 [qwen-vl-text] coord item[8]: text=1、查看受试者电子日志，受试者漏填2025年8月16日，2025年9月4日晚间日志，2025年9月4日、2025年9月25日早间日志；, bbox=[160, 389, 851, 425]
2026-08-10 11:33:23,025 INFO     29 [qwen-vl-text] coord item[9]: text=2、填写AQLQ+12和ACQ-5问卷，ACQ-5评分：0.8分；, bbox=[160, 439, 540, 455]
2026-08-10 11:33:23,025 INFO     29 [qwen-vl-text] coord item[10]: text=3、休息10分钟后，测量坐位生命体征：血压113/81mmHg，脉搏87次/分，呼吸频率20次/分，体温36.6℃，测量身高177.5cm，体重90.5kg(BMI=28.7kg/m2)；, bbox=[160, 468, 822, 505]
2026-08-10 11:33:23,025 INFO     29 [qwen-vl-text] coord item[11]: text=4、14:35体格检查：神志清，体查合作，自主体位，一般外表无异常，皮肤、粘膜无异常，唇甲无发绀，眼睛、耳、鼻、咽喉无异常，口咽部粘膜无异常，颈软，气管居中，甲状腺未及肿大，全身浅表淋巴结未及肿大，颈静脉无怒张，胸廓无畸形，双肺呼吸运动对称，双肺触觉语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及啰音。心前区无隆起，心尖搏动无弥散，心界不大，心率：87次/分，律齐，各瓣膜听诊区未闻及病理性杂音。腹平软，全腹无压痛、反跳痛。肝、脾肋下未及，肝肾区无叩击痛，肠鸣音存，4次/分，脊柱、四肢无畸形，生理征存，未引出病理征，其他系统未见明显异常；, bbox=[160, 519, 842, 658]
2026-08-10 11:33:23,025 INFO     29 [qwen-vl-text] coord item[12]: text=5、休息至少10分钟后，于14:58行12导联ECG检查；, bbox=[160, 672, 532, 688]
2026-08-10 11:33:23,025 INFO     29 [qwen-vl-text] coord item[13]: text=6、于15:01采集中心实验室样本(血常规，血生化)并送往中心试验室；, bbox=[160, 702, 672, 718]
2026-08-10 11:33:23,025 INFO     29 [qwen-vl-text] coord item[14]: text=7、回收试验药物BDAMDI@ASMDI3盒(152968-AH及185936-HK未开封，148729-UA未用60揿，实际使用46揿，发药当天预喷4揿，2025年9月10日前因超过7天未使用试验药物空喷2次共4揿，2025年9月10日后受试者每七天清洗一次后空喷5次共10揿，总计预喷18揿；epro记录使用总共46揿，与实际使用情况一致。, bbox=[160, 732, 822, 809]
2026-08-10 11:33:23,025 INFO     29 [qwen-vl-text] coord item[15]: text=8、回收epro以及AM3。, bbox=[160, 823, 325, 839]
2026-08-10 11:33:23,025 INFO     29 [qwen-vl-text] coord item[16]: text=既往史：更新合并用药：, bbox=[160, 854, 379, 870]
2026-08-10 11:33:23,025 INFO     29 [qwen-vl-text] coord item[17]: text=1、糠酸莫米松鼻喷雾剂2025.4.3-2025.7.25 每鼻 2喷/次 qm 治疗过敏性鼻炎。, bbox=[160, 883, 767, 899]
2026-08-10 11:33:23,026 INFO     29 [qwen-vl-text] page=0 — 18/18 coords, api_time=11.4s
2026-08-10 11:33:23,026 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=708232, prompt_len=1415
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共42行）
["病历文书", "门诊病历", "25/10/10 14时 门诊病历", "25/10/24 15时 门诊病历（GCP专用）", "25/11/17 10时 门诊病历", "头降使用40瓶，平均每天使用4瓶，2025年9月10日用完4瓶（大木使用试验药剂空瓶2次共4", "瓶，2025年9月10日后受试者每七天青光一次后空瓶5次共10瓶，总计空瓶10瓶（qrs记录使", "用总共46瓶，与实际使用情况一致。", "8、回访qrs以及MD。", "既往史：更新合并用药：", "1、鼻腔莫米松鼻喷雾剂C025 4 3-2025 7 25 每鼻 2喷/次 qd 治疗过敏性鼻炎。", "2、苯环喹氯桉鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。", "4、氯卓斯汀氟替卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。", "5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/", "次 治疗过敏性鼻炎。", "6、枯草抗感染治疗（生理盐水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过", "敏性鼻炎", "已预约受试者安全性随访时间。", "过敏史：", "个人史：", "体格检查：", "专科情况：", "辅助检查：", "治疗项目：", "门诊诊断：", "支气管哮喘", "单病种：", "发病时间：", "处", "置：", "1心电图（心电图室做）", "2布地奈德福莫特罗吸入粉雾剂(II)(省采)●①② 2盒2000,日入用药,一天2次", "30天", "备注：", "病情评估：", "病情分级：", "是否抢救病例：否", "是否抢救成功：", "是否为绿色通道患者：否", "病人去向：", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-10 11:33:37,961 INFO     29 [qwen-vl-text] coord API raw response (len=2514):
[
	{"text": "病历文书", "bbox": [18, 35, 58, 49]},
	{"text": "门诊病历", "bbox": [18, 93, 63, 109]},
	{"text": "25/10/10 14时 门诊病历", "bbox": [18, 139, 127, 153]},
	{"text": "25/10/24 15时 门诊病历（GCP专用）", "bbox": [18, 188, 180, 202]},
	{"text": "25/11/17 10时 门诊病历", "bbox": [18, 237, 127, 251]},
	{"text": "头降使用40瓶，平均每天使用4瓶，2025年9月10日用完4瓶（大木使用试验药剂空瓶2次共4", "bbox": [630, 73, 943, 86]},
	{"text": "瓶，2025年9月10日后受试者每七天青光一次后空瓶5次共10瓶，总计空瓶10瓶（qrs记录使", "bbox": [630, 90, 947, 103]},
	{"text": "用总共46瓶，与实际使用情况一致。", "bbox": [630, 109, 754, 122]},
	{"text": "8、回访qrs以及MD。", "bbox": [630, 138, 707, 151]},
	{"text": "既往史：更新合并用药：", "bbox": [630, 168, 733, 181]},
	{"text": "1、鼻腔莫米松鼻喷雾剂C025 4 3-2025 7 25 每鼻 2喷/次 qd 治疗过敏性鼻炎。", "bbox": [630, 196, 926, 209]},
	{"text": "2、苯环喹氯桉鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。", "bbox": [630, 225, 911, 238]},
	{"text": "4、氯卓斯汀氟替卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。", "bbox": [630, 253, 942, 266]},
	{"text": "5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/", "bbox": [630, 282, 933, 295]},
	{"text": "次 治疗过敏性鼻炎。", "bbox": [630, 300, 707, 313]},
	{"text": "6、枯草抗感染治疗（生理盐水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过", "bbox": [630, 330, 949, 343]},
	{"text": "敏性鼻炎", "bbox": [630, 350, 663, 363]},
	{"text": "已预约受试者安全性随访时间。", "bbox": [630, 378, 738, 391]},
	{"text": "过敏史：", "bbox": [630, 407, 684, 420]},
	{"text": "个人史：", "bbox": [630, 435, 678, 448]},
	{"text": "体格检查：", "bbox": [630, 464, 670, 477]},
	{"text": "专科情况：", "bbox": [630, 492, 670, 505]},
	{"text": "辅助检查：", "bbox": [630, 521, 670, 534]},
	{"text": "治疗项目：", "bbox": [630, 550, 668, 563]},
	{"text": "门诊诊断：", "bbox": [630, 578, 668, 591]},
	{"text": "支气管哮喘", "bbox": [683, 608, 723, 621]},
	{"text": "单病种：", "bbox": [630, 636, 678, 649]},
	{"text": "发病时间：", "bbox": [630, 665, 668, 678]},
	{"text": "处", "bbox": [630, 694, 639, 707]},
	{"text": "置：", "bbox": [674, 694, 688, 707]},
	{"text": "1心电图（心电图室做）", "bbox": [638, 723, 719, 736]},
	{"text": "2布地奈德福莫特罗吸入粉雾剂(II)(省采)●①② 2盒2000,日入用药,一天2次", "bbox": [638, 753, 915, 766]},
	{"text": "30天", "bbox": [930, 755, 947, 767]},
	{"text": "备注：", "bbox": [630, 783, 688, 796]},
	{"text": "病情评估：", "bbox": [630, 813, 670, 826]},
	{"text": "病情分级：", "bbox": [787, 813, 825, 826]},
	{"text": "是否抢救病例：否", "bbox": [630, 841, 699, 854]},
	{"text": "是否抢救成功：", "bbox": [748, 841, 803, 854]},
	{"text": "是否为绿色通道患者：否", "bbox": [832, 841, 924, 854]},
	{"text": "病人去向：", "bbox": [630, 869, 670, 882]},
	{"text": "CS 扫描全能王", "bbox": [902, 942, 984, 963]},
	{"text": "3亿人都在用的扫描App", "bbox": [902, 970, 984, 981]}
]
2026-08-10 11:33:37,962 INFO     29 [qwen-vl-text] coord API: raw_items=42, valid_items=42, elapsed=14.9s
2026-08-10 11:33:37,962 INFO     29 [qwen-vl-text] coord item[0]: text=病历文书, bbox=[18, 35, 58, 49]
2026-08-10 11:33:37,962 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[18, 93, 63, 109]
2026-08-10 11:33:37,962 INFO     29 [qwen-vl-text] coord item[2]: text=25/10/10 14时 门诊病历, bbox=[18, 139, 127, 153]
2026-08-10 11:33:37,962 INFO     29 [qwen-vl-text] coord item[3]: text=25/10/24 15时 门诊病历（GCP专用）, bbox=[18, 188, 180, 202]
2026-08-10 11:33:37,962 INFO     29 [qwen-vl-text] coord item[4]: text=25/11/17 10时 门诊病历, bbox=[18, 237, 127, 251]
2026-08-10 11:33:37,962 INFO     29 [qwen-vl-text] coord item[5]: text=头降使用40瓶，平均每天使用4瓶，2025年9月10日用完4瓶（大木使用试验药剂空瓶2次共4, bbox=[630, 73, 943, 86]
2026-08-10 11:33:37,962 INFO     29 [qwen-vl-text] coord item[6]: text=瓶，2025年9月10日后受试者每七天青光一次后空瓶5次共10瓶，总计空瓶10瓶（qrs记录使, bbox=[630, 90, 947, 103]
2026-08-10 11:33:37,962 INFO     29 [qwen-vl-text] coord item[7]: text=用总共46瓶，与实际使用情况一致。, bbox=[630, 109, 754, 122]
2026-08-10 11:33:37,963 INFO     29 [qwen-vl-text] coord item[8]: text=8、回访qrs以及MD。, bbox=[630, 138, 707, 151]
2026-08-10 11:33:37,963 INFO     29 [qwen-vl-text] coord item[9]: text=既往史：更新合并用药：, bbox=[630, 168, 733, 181]
2026-08-10 11:33:37,963 INFO     29 [qwen-vl-text] coord item[10]: text=1、鼻腔莫米松鼻喷雾剂C025 4 3-2025 7 25 每鼻 2喷/次 qd 治疗过敏性鼻炎。, bbox=[630, 196, 926, 209]
2026-08-10 11:33:37,963 INFO     29 [qwen-vl-text] coord item[11]: text=2、苯环喹氯桉鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。, bbox=[630, 225, 911, 238]
2026-08-10 11:33:37,963 INFO     29 [qwen-vl-text] coord item[12]: text=4、氯卓斯汀氟替卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。, bbox=[630, 253, 942, 266]
2026-08-10 11:33:37,963 INFO     29 [qwen-vl-text] coord item[13]: text=5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/, bbox=[630, 282, 933, 295]
2026-08-10 11:33:37,963 INFO     29 [qwen-vl-text] coord item[14]: text=次 治疗过敏性鼻炎。, bbox=[630, 300, 707, 313]
2026-08-10 11:33:37,963 INFO     29 [qwen-vl-text] coord item[15]: text=6、枯草抗感染治疗（生理盐水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过, bbox=[630, 330, 949, 343]
2026-08-10 11:33:37,963 INFO     29 [qwen-vl-text] coord item[16]: text=敏性鼻炎, bbox=[630, 350, 663, 363]
2026-08-10 11:33:37,963 INFO     29 [qwen-vl-text] coord item[17]: text=已预约受试者安全性随访时间。, bbox=[630, 378, 738, 391]
2026-08-10 11:33:37,963 INFO     29 [qwen-vl-text] coord item[18]: text=过敏史：, bbox=[630, 407, 684, 420]
2026-08-10 11:33:37,963 INFO     29 [qwen-vl-text] coord item[19]: text=个人史：, bbox=[630, 435, 678, 448]
2026-08-10 11:33:37,963 INFO     29 [qwen-vl-text] coord item[20]: text=体格检查：, bbox=[630, 464, 670, 477]
2026-08-10 11:33:37,963 INFO     29 [qwen-vl-text] coord item[21]: text=专科情况：, bbox=[630, 492, 670, 505]
2026-08-10 11:33:37,963 INFO     29 [qwen-vl-text] coord item[22]: text=辅助检查：, bbox=[630, 521, 670, 534]
2026-08-10 11:33:37,963 INFO     29 [qwen-vl-text] coord item[23]: text=治疗项目：, bbox=[630, 550, 668, 563]
2026-08-10 11:33:37,963 INFO     29 [qwen-vl-text] coord item[24]: text=门诊诊断：, bbox=[630, 578, 668, 591]
2026-08-10 11:33:37,963 INFO     29 [qwen-vl-text] coord item[25]: text=支气管哮喘, bbox=[683, 608, 723, 621]
2026-08-10 11:33:37,963 INFO     29 [qwen-vl-text] coord item[26]: text=单病种：, bbox=[630, 636, 678, 649]
2026-08-10 11:33:37,963 INFO     29 [qwen-vl-text] coord item[27]: text=发病时间：, bbox=[630, 665, 668, 678]
2026-08-10 11:33:37,963 INFO     29 [qwen-vl-text] coord item[28]: text=处, bbox=[630, 694, 639, 707]
2026-08-10 11:33:37,964 INFO     29 [qwen-vl-text] coord item[29]: text=置：, bbox=[674, 694, 688, 707]
2026-08-10 11:33:37,964 INFO     29 [qwen-vl-text] coord item[30]: text=1心电图（心电图室做）, bbox=[638, 723, 719, 736]
2026-08-10 11:33:37,964 INFO     29 [qwen-vl-text] coord item[31]: text=2布地奈德福莫特罗吸入粉雾剂(II)(省采)●①② 2盒2000,日入用药,一天2次, bbox=[638, 753, 915, 766]
2026-08-10 11:33:37,964 INFO     29 [qwen-vl-text] coord item[32]: text=30天, bbox=[930, 755, 947, 767]
2026-08-10 11:33:37,964 INFO     29 [qwen-vl-text] coord item[33]: text=备注：, bbox=[630, 783, 688, 796]
2026-08-10 11:33:37,964 INFO     29 [qwen-vl-text] coord item[34]: text=病情评估：, bbox=[630, 813, 670, 826]
2026-08-10 11:33:37,964 INFO     29 [qwen-vl-text] coord item[35]: text=病情分级：, bbox=[787, 813, 825, 826]
2026-08-10 11:33:37,964 INFO     29 [qwen-vl-text] coord item[36]: text=是否抢救病例：否, bbox=[630, 841, 699, 854]
2026-08-10 11:33:37,964 INFO     29 [qwen-vl-text] coord item[37]: text=是否抢救成功：, bbox=[748, 841, 803, 854]
2026-08-10 11:33:37,964 INFO     29 [qwen-vl-text] coord item[38]: text=是否为绿色通道患者：否, bbox=[832, 841, 924, 854]
2026-08-10 11:33:37,964 INFO     29 [qwen-vl-text] coord item[39]: text=病人去向：, bbox=[630, 869, 670, 882]
2026-08-10 11:33:37,964 INFO     29 [qwen-vl-text] coord item[40]: text=CS 扫描全能王, bbox=[902, 942, 984, 963]
2026-08-10 11:33:37,964 INFO     29 [qwen-vl-text] coord item[41]: text=3亿人都在用的扫描App, bbox=[902, 970, 984, 981]
2026-08-10 11:33:37,964 INFO     29 [qwen-vl-text] page=1 — 42/42 coords, api_time=14.9s
2026-08-10 11:33:37,965 INFO     29 [qwen-vl-text] new_positions (60):
[[0, 321.895, 367.115, 98.514, 112.828], [0, 260.61, 298.09499999999997, 126.3, 140.614], [0, 373.065, 410.54999999999995, 127.142, 140.614], [0, 96.39, 221.34, 153.244, 167.558], [0, 321.895, 473.025, 154.08599999999998, 167.558], [0, 95.19999999999999, 238.0, 180.188, 194.50199999999998], [0, 95.19999999999999, 508.72499999999997, 206.29, 290.49], [0, 95.19999999999999, 163.625, 302.27799999999996, 315.75], [0, 95.19999999999999, 506.34499999999997, 327.538, 357.84999999999997], [0, 95.19999999999999, 321.3, 369.638, 383.11], [0, 95.19999999999999, 489.09, 394.056, 425.21], [0, 95.19999999999999, 500.98999999999995, 436.998, 554.036], [0, 95.19999999999999, 316.53999999999996, 565.824, 579.2959999999999], [0, 95.19999999999999, 399.84, 591.084, 604.5559999999999], [0, 95.19999999999999, 489.09, 616.3439999999999, 681.178], [0, 95.19999999999999, 193.375, 692.966, 706.438], [0, 95.19999999999999, 225.505, 719.068, 732.54], [0, 95.19999999999999, 456.36499999999995, 743.486, 756.958], [1, 15.155999999999999, 48.836, 20.825, 29.154999999999998], [1, 15.155999999999999, 53.046, 55.335, 64.855], [1, 15.155999999999999, 106.934, 82.705, 91.035], [1, 15.155999999999999, 151.56, 111.86, 120.19], [1, 15.155999999999999, 106.934, 141.015, 149.345], [1, 530.46, 794.006, 43.434999999999995, 51.169999999999995], [1, 530.46, 797.374, 53.55, 61.285], [1, 530.46, 634.8679999999999, 64.855, 72.59], [1, 530.46, 595.294, 82.11, 89.845], [1, 530.46, 617.1859999999999, 99.96, 107.695], [1, 530.46, 779.692, 116.61999999999999, 124.35499999999999], [1, 530.46, 767.062, 133.875, 141.60999999999999], [1, 530.46, 793.164, 150.535, 158.26999999999998], [1, 530.46, 785.586, 167.79, 175.525], [1, 530.46, 595.294, 178.5, 186.23499999999999], [1, 530.46, 799.058, 196.35, 204.08499999999998], [1, 530.46, 558.246, 208.25, 215.98499999999999], [1, 530.46, 621.396, 224.91, 232.64499999999998], [1, 530.46, 575.928, 242.165, 249.89999999999998], [1, 530.46, 570.876, 258.825, 266.56], [1, 530.46, 564.14, 276.08, 283.815], [1, 530.46, 564.14, 292.74, 300.47499999999997], [1, 530.46, 564.14, 309.995, 317.72999999999996], [1, 530.46, 562.456, 327.25, 334.98499999999996], [1, 530.46, 562.456, 343.90999999999997, 351.645], [1, 575.086, 608.766, 361.76, 369.495], [1, 530.46, 570.876, 378.41999999999996, 386.155], [1, 530.46, 562.456, 395.67499999999995, 403.40999999999997], [1, 530.46, 538.038, 412.93, 420.66499999999996], [1, 567.5079999999999, 579.2959999999999, 412.93, 420.66499999999996], [1, 537.196, 605.398, 430.185, 437.91999999999996], [1, 537.196, 770.43, 448.03499999999997, 455.77], [1, 783.06, 797.374, 449.22499999999997, 456.36499999999995], [1, 530.46, 579.2959999999999, 465.885, 473.62], [1, 530.46, 564.14, 483.73499999999996, 491.46999999999997], [1, 662.654, 694.65, 483.73499999999996, 491.46999999999997], [1, 530.46, 588.558, 500.395, 508.13], [1, 629.816, 676.126, 500.395, 508.13], [1, 700.544, 778.0079999999999, 500.395, 508.13], [1, 530.46, 564.14, 517.055, 524.79], [1, 759.4839999999999, 828.528, 560.49, 572.985], [1, 759.4839999999999, 828.528, 577.15, 583.6949999999999]]
2026-08-10 11:33:37,965 INFO     29 [qwen-vl-text] ═══ DONE ═══ 60 positions, pages=2, time=35.8s
2026-08-10 11:33:37,965 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:33:37,973 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:33:37,973 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:33:37,973 INFO     29 [qwen-vl-text] positions(35): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:33:37,973 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [35]
2026-08-10 11:33:38,160 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:33:38,160 INFO     29 [qwen-vl-text] LLM extraction start, text_len=856
2026-08-10 11:33:38,160 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:33:38,161 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 60, \"bbox_end\": 94, \"encounter_dates\": [\"2025-10-24\"], \"department\": \"内科门诊（荔湾）\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "就诊卡\n流水号：\n姓名\n龄：40岁\n就诊科\n日：2025-10-24 15:45:39\n主诉：安全性电话随访\n现病史：今日10:27\n固定电话（020-\n（159\n5），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无\n不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对\nV8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试\n者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，\n目前无安全性异常表现。\n合并用药更新：\n1、小柴胡颗粒、（自行购药）2025.10.6-2025.10.8 10g tid 治疗上呼吸道感染\n2、苯环喹溴铵鼻喷雾剂 2025.4.3-至今 每鼻2喷/次 qid 治疗过敏性鼻炎\n3、氮卓斯汀氟替卡松鼻喷雾剂 2025.9.3-至今 每鼻2喷/次 bid 治疗过敏性鼻炎\n4、辛芩颗粒 2024.8.21-2024.8.27 1袋 冲服 tid 治疗过敏性鼻炎\nAE：\n上呼吸道感染 2025年10月5日-2025年10月8日 中度，非SAE，采取药物治疗措施，对试验\n药物采取措施：剂量不变，与试验药物无关，未因该AE退出研究。\n病历更正：\n1、更正2024年10月22日病历，合并用药“辛芩颗粒”为“辛芩颗粒”；\n2、更正2024年10月22日病历，合并用药“苯环喹溴铵鼻喷雾剂”为“苯环喹溴铵鼻喷雾\n剂”；\n3、更正2026年1月24日病历，“无收到ePro触发的哮喘警报邮件”为“有收到ePro触发的哮\n喘警报邮件”；\n4、更正2025年7月18日病历，“受试者漏填2025年4月28日晚间日志” 更正为：“受试者\n漏填2025年4月28日早间日志”；\n5、更正2024年11月6日病历，“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共\n计用了26喷”为：“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了28\n喷”。\n随行中·",
    "role": "user"
  }
]
2026-08-10 11:33:41,817 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:33:41.816+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 23, "failed": 0, "current": {"ea51b5dc94ae11f1bd9827cf206dfa2d": {"id": "ea51b5dc94ae11f1bd9827cf206dfa2d", "doc_id": "ea1b0b1894ae11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786361440167, "task_type": "dataflow", "root_trace_id": "bca8d639df704cd29f0107370613ab01", "root_traceparent": "00-bca8d639df704cd29f0107370613ab01-b8b3c91a32048c1c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:33:43,178 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:33:43,179 INFO     29 [qwen-vl-text] LLM output (len=995):
{
  "encounter_date": "2025-10-24",
  "chief_complaint": "安全性电话随访",
  "present_illness": "今日10:27固定电话（020-（159 5），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对V8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，目前无安全性异常表现。",
  "past_history": null,
  "diagnosis": null,
  "treatment_plan": [
    {
      "drug_name": "小柴胡颗粒",
      "dosage": "10g",
      "frequency": "tid",
      "route": null,
      "notes": "自行购药，2025.10.6-2025.10.8，治疗上呼吸道感染"
    },
    {
      "drug_name": "苯环喹溴铵鼻喷雾剂",
      "dosage": "每鼻2喷/次",
      "frequency": "qid",
      "route": null,
      "notes": "2025.4.3-至今，治疗过敏性鼻炎"
    },
    {
      "drug_name": "氮卓斯汀氟替卡松鼻喷雾剂",
      "dosage": "每鼻2喷/次",
      "frequency": "bid",
      "route": null,
      "notes": "2025.9.3-至今，治疗过敏性鼻炎"
    },
    {
      "drug_name": "辛芩颗粒",
      "dosage": "1袋",
      "frequency": "tid",
      "route": "冲服",
      "notes": "2024.8.21-2024.8.27，治疗过敏性鼻炎"
    }
  ]
}
2026-08-10 11:33:43,179 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-10-24]
2026-08-10 11:33:43,182 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1082890, prompt_len=1574
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["就诊卡", "流水号：", "姓名", "龄：40岁", "就诊科", "日：2025-10-24 15:45:39", "主诉：安全性电话随访", "现病史：今日10:27", "固定电话（020-", "（159", "5），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无", "不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对", "V8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试", "者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，", "目前无安全性异常表现。", "合并用药更新：", "1、小柴胡颗粒、（自行购药）2025.10.6-2025.10.8 10g tid 治疗上呼吸道感染", "2、苯环喹溴铵鼻喷雾剂 2025.4.3-至今 每鼻2喷/次 qid 治疗过敏性鼻炎", "3、氮卓斯汀氟替卡松鼻喷雾剂 2025.9.3-至今 每鼻2喷/次 bid 治疗过敏性鼻炎", "4、辛芩颗粒 2024.8.21-2024.8.27 1袋 冲服 tid 治疗过敏性鼻炎", "AE：", "上呼吸道感染 2025年10月5日-2025年10月8日 中度，非SAE，采取药物治疗措施，对试验", "药物采取措施：剂量不变，与试验药物无关，未因该AE退出研究。", "病历更正：", "1、更正2024年10月22日病历，合并用药“辛芩颗粒”为“辛芩颗粒”；", "2、更正2024年10月22日病历，合并用药“苯环喹溴铵鼻喷雾剂”为“苯环喹溴铵鼻喷雾", "剂”；", "3、更正2026年1月24日病历，“无收到ePro触发的哮喘警报邮件”为“有收到ePro触发的哮", "喘警报邮件”；", "4、更正2025年7月18日病历，“受试者漏填2025年4月28日晚间日志” 更正为：“受试者", "漏填2025年4月28日早间日志”；", "5、更正2024年11月6日病历，“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共", "计用了26喷”为：“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了28", "喷”。", "随行中·"]

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
2026-08-10 11:33:56,678 INFO     29 [qwen-vl-text] coord API raw response (len=2398):
[
	{"text": "就诊卡", "bbox": [170, 98, 218, 115]},
	{"text": "流水号：", "bbox": [170, 131, 218, 148]},
	{"text": "姓名", "bbox": [170, 164, 187, 181]},
	{"text": "龄：40岁", "bbox": [647, 165, 710, 180]},
	{"text": "就诊科", "bbox": [170, 196, 218, 213]},
	{"text": "日：2025-10-24 15:45:39", "bbox": [617, 197, 819, 211]},
	{"text": "主诉：安全性电话随访", "bbox": [166, 228, 428, 246]},
	{"text": "现病史：今日10:27", "bbox": [166, 259, 360, 276]},
	{"text": "固定电话（020-", "bbox": [514, 260, 644, 276]},
	{"text": "（159", "bbox": [173, 281, 210, 297]},
	{"text": "5），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无", "bbox": [268, 281, 872, 297]},
	{"text": "不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对", "bbox": [166, 302, 878, 318]},
	{"text": "V8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试", "bbox": [166, 323, 877, 339]},
	{"text": "者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，", "bbox": [166, 344, 865, 360]},
	{"text": "目前无安全性异常表现。", "bbox": [166, 365, 355, 380]},
	{"text": "合并用药更新：", "bbox": [166, 395, 280, 411]},
	{"text": "1、小柴胡颗粒、（自行购药）2025.10.6-2025.10.8 10g tid 治疗上呼吸道感染", "bbox": [166, 425, 806, 441]},
	{"text": "2、苯环喹溴铵鼻喷雾剂 2025.4.3-至今 每鼻2喷/次 qid 治疗过敏性鼻炎", "bbox": [166, 455, 768, 471]},
	{"text": "3、氮卓斯汀氟替卡松鼻喷雾剂 2025.9.3-至今 每鼻2喷/次 bid 治疗过敏性鼻炎", "bbox": [166, 484, 817, 500]},
	{"text": "4、辛芩颗粒 2024.8.21-2024.8.27 1袋 冲服 tid 治疗过敏性鼻炎", "bbox": [166, 514, 718, 529]},
	{"text": "AE：", "bbox": [166, 545, 192, 558]},
	{"text": "上呼吸道感染 2025年10月5日-2025年10月8日 中度，非SAE，采取药物治疗措施，对试验", "bbox": [166, 573, 851, 589]},
	{"text": "药物采取措施：剂量不变，与试验药物无关，未因该AE退出研究。", "bbox": [166, 593, 656, 609]},
	{"text": "病历更正：", "bbox": [166, 622, 244, 638]},
	{"text": "1、更正2024年10月22日病历，合并用药“辛芩颗粒”为“辛芩颗粒”；", "bbox": [166, 651, 693, 667]},
	{"text": "2、更正2024年10月22日病历，合并用药“苯环喹溴铵鼻喷雾剂”为“苯环喹溴铵鼻喷雾", "bbox": [166, 679, 812, 695]},
	{"text": "剂”；", "bbox": [166, 698, 210, 713]},
	{"text": "3、更正2026年1月24日病历，“无收到ePro触发的哮喘警报邮件”为“有收到ePro触发的哮", "bbox": [166, 726, 831, 742]},
	{"text": "喘警报邮件”；", "bbox": [166, 745, 277, 760]},
	{"text": "4、更正2025年7月18日病历，“受试者漏填2025年4月28日晚间日志” 更正为：“受试者", "bbox": [166, 772, 817, 788]},
	{"text": "漏填2025年4月28日早间日志”；", "bbox": [166, 790, 402, 805]},
	{"text": "5、更正2024年11月6日病历，“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共", "bbox": [166, 817, 819, 833]},
	{"text": "计用了26喷”为：“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了28", "bbox": [166, 835, 802, 851]},
	{"text": "喷”。", "bbox": [166, 853, 213, 867]},
	{"text": "随行中·", "bbox": [166, 877, 268, 891]}
]
2026-08-10 11:33:56,679 INFO     29 [qwen-vl-text] coord API: raw_items=35, valid_items=35, elapsed=13.5s
2026-08-10 11:33:56,679 INFO     29 [qwen-vl-text] coord item[0]: text=就诊卡, bbox=[170, 98, 218, 115]
2026-08-10 11:33:56,679 INFO     29 [qwen-vl-text] coord item[1]: text=流水号：, bbox=[170, 131, 218, 148]
2026-08-10 11:33:56,679 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[170, 164, 187, 181]
2026-08-10 11:33:56,679 INFO     29 [qwen-vl-text] coord item[3]: text=龄：40岁, bbox=[647, 165, 710, 180]
2026-08-10 11:33:56,679 INFO     29 [qwen-vl-text] coord item[4]: text=就诊科, bbox=[170, 196, 218, 213]
2026-08-10 11:33:56,679 INFO     29 [qwen-vl-text] coord item[5]: text=日：2025-10-24 15:45:39, bbox=[617, 197, 819, 211]
2026-08-10 11:33:56,680 INFO     29 [qwen-vl-text] coord item[6]: text=主诉：安全性电话随访, bbox=[166, 228, 428, 246]
2026-08-10 11:33:56,680 INFO     29 [qwen-vl-text] coord item[7]: text=现病史：今日10:27, bbox=[166, 259, 360, 276]
2026-08-10 11:33:56,680 INFO     29 [qwen-vl-text] coord item[8]: text=固定电话（020-, bbox=[514, 260, 644, 276]
2026-08-10 11:33:56,680 INFO     29 [qwen-vl-text] coord item[9]: text=（159, bbox=[173, 281, 210, 297]
2026-08-10 11:33:56,680 INFO     29 [qwen-vl-text] coord item[10]: text=5），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无, bbox=[268, 281, 872, 297]
2026-08-10 11:33:56,680 INFO     29 [qwen-vl-text] coord item[11]: text=不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对, bbox=[166, 302, 878, 318]
2026-08-10 11:33:56,680 INFO     29 [qwen-vl-text] coord item[12]: text=V8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试, bbox=[166, 323, 877, 339]
2026-08-10 11:33:56,680 INFO     29 [qwen-vl-text] coord item[13]: text=者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，, bbox=[166, 344, 865, 360]
2026-08-10 11:33:56,680 INFO     29 [qwen-vl-text] coord item[14]: text=目前无安全性异常表现。, bbox=[166, 365, 355, 380]
2026-08-10 11:33:56,680 INFO     29 [qwen-vl-text] coord item[15]: text=合并用药更新：, bbox=[166, 395, 280, 411]
2026-08-10 11:33:56,680 INFO     29 [qwen-vl-text] coord item[16]: text=1、小柴胡颗粒、（自行购药）2025.10.6-2025.10.8 10g tid 治疗上呼吸道感染, bbox=[166, 425, 806, 441]
2026-08-10 11:33:56,680 INFO     29 [qwen-vl-text] coord item[17]: text=2、苯环喹溴铵鼻喷雾剂 2025.4.3-至今 每鼻2喷/次 qid 治疗过敏性鼻炎, bbox=[166, 455, 768, 471]
2026-08-10 11:33:56,680 INFO     29 [qwen-vl-text] coord item[18]: text=3、氮卓斯汀氟替卡松鼻喷雾剂 2025.9.3-至今 每鼻2喷/次 bid 治疗过敏性鼻炎, bbox=[166, 484, 817, 500]
2026-08-10 11:33:56,680 INFO     29 [qwen-vl-text] coord item[19]: text=4、辛芩颗粒 2024.8.21-2024.8.27 1袋 冲服 tid 治疗过敏性鼻炎, bbox=[166, 514, 718, 529]
2026-08-10 11:33:56,681 INFO     29 [qwen-vl-text] coord item[20]: text=AE：, bbox=[166, 545, 192, 558]
2026-08-10 11:33:56,681 INFO     29 [qwen-vl-text] coord item[21]: text=上呼吸道感染 2025年10月5日-2025年10月8日 中度，非SAE，采取药物治疗措施，对试验, bbox=[166, 573, 851, 589]
2026-08-10 11:33:56,681 INFO     29 [qwen-vl-text] coord item[22]: text=药物采取措施：剂量不变，与试验药物无关，未因该AE退出研究。, bbox=[166, 593, 656, 609]
2026-08-10 11:33:56,681 INFO     29 [qwen-vl-text] coord item[23]: text=病历更正：, bbox=[166, 622, 244, 638]
2026-08-10 11:33:56,681 INFO     29 [qwen-vl-text] coord item[24]: text=1、更正2024年10月22日病历，合并用药“辛芩颗粒”为“辛芩颗粒”；, bbox=[166, 651, 693, 667]
2026-08-10 11:33:56,681 INFO     29 [qwen-vl-text] coord item[25]: text=2、更正2024年10月22日病历，合并用药“苯环喹溴铵鼻喷雾剂”为“苯环喹溴铵鼻喷雾, bbox=[166, 679, 812, 695]
2026-08-10 11:33:56,681 INFO     29 [qwen-vl-text] coord item[26]: text=剂”；, bbox=[166, 698, 210, 713]
2026-08-10 11:33:56,681 INFO     29 [qwen-vl-text] coord item[27]: text=3、更正2026年1月24日病历，“无收到ePro触发的哮喘警报邮件”为“有收到ePro触发的哮, bbox=[166, 726, 831, 742]
2026-08-10 11:33:56,682 INFO     29 [qwen-vl-text] coord item[28]: text=喘警报邮件”；, bbox=[166, 745, 277, 760]
2026-08-10 11:33:56,682 INFO     29 [qwen-vl-text] coord item[29]: text=4、更正2025年7月18日病历，“受试者漏填2025年4月28日晚间日志” 更正为：“受试者, bbox=[166, 772, 817, 788]
2026-08-10 11:33:56,682 INFO     29 [qwen-vl-text] coord item[30]: text=漏填2025年4月28日早间日志”；, bbox=[166, 790, 402, 805]
2026-08-10 11:33:56,682 INFO     29 [qwen-vl-text] coord item[31]: text=5、更正2024年11月6日病历，“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共, bbox=[166, 817, 819, 833]
2026-08-10 11:33:56,682 INFO     29 [qwen-vl-text] coord item[32]: text=计用了26喷”为：“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了28, bbox=[166, 835, 802, 851]
2026-08-10 11:33:56,682 INFO     29 [qwen-vl-text] coord item[33]: text=喷”。, bbox=[166, 853, 213, 867]
2026-08-10 11:33:56,682 INFO     29 [qwen-vl-text] coord item[34]: text=随行中·, bbox=[166, 877, 268, 891]
2026-08-10 11:33:56,682 INFO     29 [qwen-vl-text] page=2 — 35/35 coords, api_time=13.5s
2026-08-10 11:33:56,682 INFO     29 [qwen-vl-text] new_positions (35):
[[2, 101.14999999999999, 129.71, 82.51599999999999, 96.83], [2, 101.14999999999999, 129.71, 110.30199999999999, 124.616], [2, 101.14999999999999, 111.265, 138.088, 152.402], [2, 384.965, 422.45, 138.93, 151.56], [2, 101.14999999999999, 129.71, 165.03199999999998, 179.346], [2, 367.115, 487.30499999999995, 165.874, 177.662], [2, 98.77, 254.66, 191.976, 207.132], [2, 98.77, 214.2, 218.078, 232.392], [2, 305.83, 383.18, 218.92, 232.392], [2, 102.935, 124.94999999999999, 236.602, 250.07399999999998], [2, 159.45999999999998, 518.84, 236.602, 250.07399999999998], [2, 98.77, 522.41, 254.284, 267.756], [2, 98.77, 521.8149999999999, 271.966, 285.438], [2, 98.77, 514.675, 289.64799999999997, 303.12], [2, 98.77, 211.225, 307.33, 319.96], [2, 98.77, 166.6, 332.59, 346.062], [2, 98.77, 479.57, 357.84999999999997, 371.322], [2, 98.77, 456.96, 383.11, 396.582], [2, 98.77, 486.11499999999995, 407.52799999999996, 421.0], [2, 98.77, 427.21, 432.788, 445.418], [2, 98.77, 114.24, 458.89, 469.83599999999996], [2, 98.77, 506.34499999999997, 482.466, 495.938], [2, 98.77, 390.32, 499.306, 512.778], [2, 98.77, 145.18, 523.7239999999999, 537.196], [2, 98.77, 412.335, 548.1419999999999, 561.614], [2, 98.77, 483.14, 571.718, 585.1899999999999], [2, 98.77, 124.94999999999999, 587.716, 600.346], [2, 98.77, 494.445, 611.292, 624.764], [2, 98.77, 164.815, 627.29, 639.92], [2, 98.77, 486.11499999999995, 650.024, 663.496], [2, 98.77, 239.19, 665.18, 677.81], [2, 98.77, 487.30499999999995, 687.914, 701.386], [2, 98.77, 477.19, 703.0699999999999, 716.542], [2, 98.77, 126.735, 718.226, 730.014], [2, 98.77, 159.45999999999998, 738.434, 750.222]]
2026-08-10 11:33:56,682 INFO     29 [qwen-vl-text] ═══ DONE ═══ 35 positions, pages=1, time=18.7s
2026-08-10 11:33:56,683 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:33:56,684 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:33:56,685 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:33:56,685 INFO     29 [qwen-vl-text] positions(25): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:33:56,685 INFO     29 [qwen-vl-text] page grouping: [3], lines per page: [25]
2026-08-10 11:33:56,890 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:33:56,892 INFO     29 [qwen-vl-text] LLM extraction start, text_len=767
2026-08-10 11:33:56,892 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:33:56,892 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 95, \"bbox_end\": 119, \"encounter_dates\": [\"2025-11-17\"], \"department\": \"内科门诊（荔湾）\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "病历编号：\n姓名：\n性别：\n年龄：40岁\n就诊科室：\n就诊时间：2025-11-17 10:10:48\n主诉：支气管哮喘治疗后复查：\n现病史：2021年2月前开始出现咳嗽、咯痰，粘白，量中，能咯出，咳嗽呈阵发性、刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏。无咽痛，无伴反酸、嗳气、腹胀。无上腹部隐痛不适感，无伴发热、畏寒，影响睡眠。晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：\n12.52*109/L 嗜酸粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定。本次门诊距上次门诊间隔时间30天。症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确。急性发作情况：两次，就诊期间急性发作：无，发作次数：0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。近3天来出现咽痛不适\n既往史：鼻炎病史无规则治疗。打鼾明显。\n过敏史：未发现。\n个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。\n体格检查：神志清，颈软，双肺呼吸音粗，未闻及明显干、湿性罗音，口腔粘膜无白斑。\n专科情况：\n辅助检查：\n治疗项目：\n门诊诊断：\n1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、阻塞性睡眠呼吸暂停低通气综合征,4、急性咽炎\n单病种：\n发病时间：\n处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不适随诊。\n1金银花口服液◆⑤ 2盒 20.0ml,口服,一天3次(口服) 6天\n2氨卓斯汀氟替卡松鼻喷雾剂◆ 1瓶 2.0喷,喷鼻,一天2次 30天\n3苯环喹溴铵鼻喷雾剂◆ 3瓶 2.0喷,喷鼻,一天4次 30天\n备注：建议在住地附近社区医疗机构随诊。",
    "role": "user"
  }
]
2026-08-10 11:34:03,536 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:34:03,536 INFO     29 [qwen-vl-text] LLM output (len=1107):
{
  "encounter_date": "2025-11-17",
  "chief_complaint": "支气管哮喘治疗后复查",
  "present_illness": "2021年2月前开始出现咳嗽、咯痰，粘白，量中，能咯出，咳嗽呈阵发性、刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏。无咽痛，无伴反酸、嗳气、腹胀。无上腹部隐痛不适感，无伴发热、畏寒，影响睡眠。晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定。本次门诊距上次门诊间隔时间30天。症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确。急性发作情况：两次，就诊期间急性发作：无，发作次数：0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。近3天来出现咽痛不适",
  "past_history": "鼻炎病史无规则治疗。打鼾明显。否认遗传病史，吸烟10年，20支/日，2016年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。",
  "diagnosis": "1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、阻塞性睡眠呼吸暂停低通气综合征,4、急性咽炎",
  "treatment_plan": [
    {
      "drug_name": "金银花口服液",
      "dosage": "20.0ml",
      "route": "口服",
      "frequency": "一天3次",
      "duration": "6天",
      "quantity": "2盒"
    },
    {
      "drug_name": "氨卓斯汀氟替卡松鼻喷雾剂",
      "dosage": "2.0喷",
      "route": "喷鼻",
      "frequency": "一天2次",
      "duration": "30天",
      "quantity": "1瓶"
    },
    {
      "drug_name": "苯环喹溴铵鼻喷雾剂",
      "dosage": "2.0喷",
      "route": "喷鼻",
      "frequency": "一天4次",
      "duration": "30天",
      "quantity": "3瓶"
    }
  ]
}
2026-08-10 11:34:03,536 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-17]
2026-08-10 11:34:03,542 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1159920, prompt_len=1455
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["病历编号：", "姓名：", "性别：", "年龄：40岁", "就诊科室：", "就诊时间：2025-11-17 10:10:48", "主诉：支气管哮喘治疗后复查：", "现病史：2021年2月前开始出现咳嗽、咯痰，粘白，量中，能咯出，咳嗽呈阵发性、刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏。无咽痛，无伴反酸、嗳气、腹胀。无上腹部隐痛不适感，无伴发热、畏寒，影响睡眠。晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：", "12.52*109/L 嗜酸粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定。本次门诊距上次门诊间隔时间30天。症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确。急性发作情况：两次，就诊期间急性发作：无，发作次数：0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。近3天来出现咽痛不适", "既往史：鼻炎病史无规则治疗。打鼾明显。", "过敏史：未发现。", "个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。", "体格检查：神志清，颈软，双肺呼吸音粗，未闻及明显干、湿性罗音，口腔粘膜无白斑。", "专科情况：", "辅助检查：", "治疗项目：", "门诊诊断：", "1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、阻塞性睡眠呼吸暂停低通气综合征,4、急性咽炎", "单病种：", "发病时间：", "处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不适随诊。", "1金银花口服液◆⑤ 2盒 20.0ml,口服,一天3次(口服) 6天", "2氨卓斯汀氟替卡松鼻喷雾剂◆ 1瓶 2.0喷,喷鼻,一天2次 30天", "3苯环喹溴铵鼻喷雾剂◆ 3瓶 2.0喷,喷鼻,一天4次 30天", "备注：建议在住地附近社区医疗机构随诊。"]

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
2026-08-10 11:34:14,501 INFO     29 [qwen-vl-text] coord API raw response (len=1870):
[
	{"text": "病历编号：", "bbox": [545, 130, 600, 144]},
	{"text": "姓名：", "bbox": [177, 130, 225, 144]},
	{"text": "性别：", "bbox": [177, 160, 192, 174]},
	{"text": "年龄：40岁", "bbox": [607, 160, 665, 174]},
	{"text": "就诊科室：", "bbox": [177, 189, 228, 204]},
	{"text": "就诊时间：2025-11-17 10:10:48", "bbox": [545, 189, 763, 203]},
	{"text": "主诉：支气管哮喘治疗后复查：", "bbox": [175, 218, 466, 234]},
	{"text": "现病史：2021年2月前开始出现咳嗽、咯痰，粘白，量中，能咯出，咳嗽呈阵发性、刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏。无咽痛，无伴反酸、嗳气、腹胀。无上腹部隐痛不适感，无伴发热、畏寒，影响睡眠。晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：", "bbox": [175, 247, 821, 285]},
	{"text": "12.52*109/L 嗜酸粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定。本次门诊距上次门诊间隔时间30天。症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确。急性发作情况：两次，就诊期间急性发作：无，发作次数：0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。近3天来出现咽痛不适", "bbox": [175, 323, 813, 412]},
	{"text": "既往史：鼻炎病史无规则治疗。打鼾明显。", "bbox": [175, 425, 508, 440]},
	{"text": "过敏史：未发现。", "bbox": [175, 453, 334, 468]},
	{"text": "个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。", "bbox": [175, 479, 800, 512]},
	{"text": "体格检查：神志清，颈软，双肺呼吸音粗，未闻及明显干、湿性罗音，口腔粘膜无白斑。", "bbox": [177, 524, 780, 539]},
	{"text": "专科情况：", "bbox": [177, 551, 254, 565]},
	{"text": "辅助检查：", "bbox": [177, 577, 254, 591]},
	{"text": "治疗项目：", "bbox": [177, 604, 254, 618]},
	{"text": "门诊诊断：", "bbox": [177, 630, 254, 644]},
	{"text": "1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、阻塞性睡眠呼吸暂停低通气综合征,4、急性咽炎", "bbox": [193, 657, 770, 687]},
	{"text": "单病种：", "bbox": [177, 700, 269, 714]},
	{"text": "发病时间：", "bbox": [177, 724, 254, 738]},
	{"text": "处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不适随诊。", "bbox": [260, 750, 675, 764]},
	{"text": "1金银花口服液◆⑤ 2盒 20.0ml,口服,一天3次(口服) 6天", "bbox": [198, 774, 716, 788]},
	{"text": "2氨卓斯汀氟替卡松鼻喷雾剂◆ 1瓶 2.0喷,喷鼻,一天2次 30天", "bbox": [198, 799, 672, 813]},
	{"text": "3苯环喹溴铵鼻喷雾剂◆ 3瓶 2.0喷,喷鼻,一天4次 30天", "bbox": [198, 824, 670, 838]},
	{"text": "备注：建议在住地附近社区医疗机构随诊。", "bbox": [260, 848, 520, 861]}
]
2026-08-10 11:34:14,501 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=11.0s
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[0]: text=病历编号：, bbox=[545, 130, 600, 144]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[177, 130, 225, 144]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[2]: text=性别：, bbox=[177, 160, 192, 174]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：40岁, bbox=[607, 160, 665, 174]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[4]: text=就诊科室：, bbox=[177, 189, 228, 204]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[5]: text=就诊时间：2025-11-17 10:10:48, bbox=[545, 189, 763, 203]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[6]: text=主诉：支气管哮喘治疗后复查：, bbox=[175, 218, 466, 234]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[7]: text=现病史：2021年2月前开始出现咳嗽、咯痰，粘白，量中，能咯出，咳嗽呈阵发性、刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏。无咽痛，无伴反酸、嗳气、腹胀。无上腹部隐痛不适感，无伴发热、畏寒，影响睡眠。晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：, bbox=[175, 247, 821, 285]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[8]: text=12.52*109/L 嗜酸粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定。本次门诊距上次门诊间隔时间30天。症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确。急性发作情况：两次，就诊期间急性发作：无，发作次数：0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。近3天来出现咽痛不适, bbox=[175, 323, 813, 412]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[9]: text=既往史：鼻炎病史无规则治疗。打鼾明显。, bbox=[175, 425, 508, 440]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[10]: text=过敏史：未发现。, bbox=[175, 453, 334, 468]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[11]: text=个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。, bbox=[175, 479, 800, 512]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[12]: text=体格检查：神志清，颈软，双肺呼吸音粗，未闻及明显干、湿性罗音，口腔粘膜无白斑。, bbox=[177, 524, 780, 539]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[13]: text=专科情况：, bbox=[177, 551, 254, 565]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[14]: text=辅助检查：, bbox=[177, 577, 254, 591]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[15]: text=治疗项目：, bbox=[177, 604, 254, 618]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[16]: text=门诊诊断：, bbox=[177, 630, 254, 644]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[17]: text=1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、阻塞性睡眠呼吸暂停低通气综合征,4、急性咽炎, bbox=[193, 657, 770, 687]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[18]: text=单病种：, bbox=[177, 700, 269, 714]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[19]: text=发病时间：, bbox=[177, 724, 254, 738]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[20]: text=处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不适随诊。, bbox=[260, 750, 675, 764]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[21]: text=1金银花口服液◆⑤ 2盒 20.0ml,口服,一天3次(口服) 6天, bbox=[198, 774, 716, 788]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[22]: text=2氨卓斯汀氟替卡松鼻喷雾剂◆ 1瓶 2.0喷,喷鼻,一天2次 30天, bbox=[198, 799, 672, 813]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[23]: text=3苯环喹溴铵鼻喷雾剂◆ 3瓶 2.0喷,喷鼻,一天4次 30天, bbox=[198, 824, 670, 838]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] coord item[24]: text=备注：建议在住地附近社区医疗机构随诊。, bbox=[260, 848, 520, 861]
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] page=3 — 25/25 coords, api_time=11.0s
2026-08-10 11:34:14,502 INFO     29 [qwen-vl-text] new_positions (25):
[[3, 324.275, 357.0, 109.46, 121.24799999999999], [3, 105.315, 133.875, 109.46, 121.24799999999999], [3, 105.315, 114.24, 134.72, 146.50799999999998], [3, 361.16499999999996, 395.67499999999995, 134.72, 146.50799999999998], [3, 105.315, 135.66, 159.138, 171.768], [3, 324.275, 453.98499999999996, 159.138, 170.926], [3, 104.125, 277.27, 183.55599999999998, 197.028], [3, 104.125, 488.495, 207.974, 239.97], [3, 104.125, 483.73499999999996, 271.966, 346.904], [3, 104.125, 302.26, 357.84999999999997, 370.47999999999996], [3, 104.125, 198.73, 381.426, 394.056], [3, 104.125, 476.0, 403.318, 431.104], [3, 105.315, 464.09999999999997, 441.20799999999997, 453.83799999999997], [3, 105.315, 151.13, 463.942, 475.72999999999996], [3, 105.315, 151.13, 485.834, 497.62199999999996], [3, 105.315, 151.13, 508.568, 520.356], [3, 105.315, 151.13, 530.46, 542.2479999999999], [3, 114.835, 458.15, 553.194, 578.454], [3, 105.315, 160.055, 589.4, 601.188], [3, 105.315, 151.13, 609.608, 621.396], [3, 154.7, 401.625, 631.5, 643.288], [3, 117.80999999999999, 426.02, 651.708, 663.496], [3, 117.80999999999999, 399.84, 672.7579999999999, 684.5459999999999], [3, 117.80999999999999, 398.65, 693.808, 705.596], [3, 154.7, 309.4, 714.016, 724.962]]
2026-08-10 11:34:14,503 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=17.8s
2026-08-10 11:34:14,503 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:34:14,514 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:34:14,514 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:34:14,514 INFO     29 [qwen-vl-text] positions(44): [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:34:14,514 INFO     29 [qwen-vl-text] page grouping: [13], lines per page: [44]
2026-08-10 11:34:14,691 INFO     29 [qwen-vl-text] page=13, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:34:14,692 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1134
2026-08-10 11:34:14,692 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:34:14,693 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 722, \"bbox_end\": 765, \"encounter_dates\": [\"2026-01-05\"], \"department\": \"内科门诊(荔湾)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "广州医科大学附属第三医院\nThe Third Affiliated Hospital of Guangzhou Medical University\n门(急)诊病历信息\n就诊卡\n流水\n姓\n病历编号:\n年 龄:41岁\n就诊科室:内科门诊(荔湾) 医\n就诊时间:2026-01-05 17:07:54\n主 诉:支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天\n现 病 史:2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激\n性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流\n涕、喷嚏,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响\n睡眠,晨起有咽干,曾到本院就诊两次,症状不见明显缓解。2021-1-9血常规:白细胞:\n12.52*109/L 嗜酸粒细胞:0.65*109/L 5.2%,经治疗后症状明显缓解。无咳嗽、咯痰、气\n促。病情稳定,本次门诊距上次门诊间隔时间30天。症状控制情况:过去4周,患者:吸入\n药物使用情况:遵医嘱使用;吸入装置使用情况:正确。急性发作情况:两次,就诊期间急\n性发作:无,发作次数:0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。长期规律使用信必\n可160/4.5ug 2吸 bid治疗,5天前开始出现咳嗽、咯痰,黄白痰,量少,难以咯出,咳嗽以\n夜间为主。无气促,伴咽息,鼻塞、流涕、喷嚏,无发热。\n既 往 史:鼻炎病史无规则治疗。打鼾明显。\n过 敏 史:未发现;\n个 人 史:否认遗传病史,吸烟10年,20支/日,2018年戒烟。偶饮酒。2021-12-20已打第\n三针新冠疫苗。\n体格检查:神志清,颈软,双肺呼吸音粗,可闻及散在哮鸣音,口腔粘膜无白斑。\n专科情况:\n辅助检查:\n治疗项目:\n门诊诊断:\n1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎\n处 置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。\n布地奈德福莫特罗吸入粉雾剂(II)2盒 2.0吸,吸入用药,一天2次 30天\n(省采)●①⑤\n左氧氟沙星片(省采)●⑥ 5片 0.5g,口服,每日1次(口服) 5天\n第1页\n广州医科大学附属第三医院\nThe Third Affiliated Hospital of Guangzhou Medical University\n门(急)诊病历信息\n复方甲氧那明胶囊(省采)◆② 1瓶 1.0粒,餐后口服,一天3次(口服) 5天\n盐酸氨溴索分散片(省采)●⑥ 15片 30.0mg,餐后口服,一天3次(口服) 5\n天\n醋酸泼尼松片●②④ 6片 10.0mg,口服,每早1次(口服) 3天\n备 注:建议在住地附近社区医疗机构随诊。",
    "role": "user"
  }
]
2026-08-10 11:34:14,695 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:34:14.694+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 23, "failed": 0, "current": {"ea51b5dc94ae11f1bd9827cf206dfa2d": {"id": "ea51b5dc94ae11f1bd9827cf206dfa2d", "doc_id": "ea1b0b1894ae11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786361440167, "task_type": "dataflow", "root_trace_id": "bca8d639df704cd29f0107370613ab01", "root_traceparent": "00-bca8d639df704cd29f0107370613ab01-b8b3c91a32048c1c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:34:21,888 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:34:21,888 INFO     29 [qwen-vl-text] LLM output (len=1519):
{
  "encounter_date": "2026-01-05",
  "chief_complaint": "支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天",
  "present_illness": "2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流涕、喷嚏,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响睡眠,晨起有咽干,曾到本院就诊两次,症状不见明显缓解。2021-1-9血常规:白细胞:12.52*109/L 嗜酸粒细胞:0.65*109/L 5.2%,经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定,本次门诊距上次门诊间隔时间30天。症状控制情况:过去4周,患者:吸入药物使用情况:遵医嘱使用;吸入装置使用情况:正确。急性发作情况:两次,就诊期间急性发作:无,发作次数:0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。长期规律使用信必可160/4.5ug 2吸 bid治疗,5天前开始出现咳嗽、咯痰,黄白痰,量少,难以咯出,咳嗽以夜间为主。无气促,伴咽息,鼻塞、流涕、喷嚏,无发热。",
  "past_history": "鼻炎病史无规则治疗。打鼾明显。否认遗传病史,吸烟10年,20支/日,2018年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。",
  "diagnosis": "1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎",
  "treatment_plan": [
    {
      "drug_name": "布地奈德福莫特罗吸入粉雾剂(II)",
      "dosage": "2.0吸",
      "route": "吸入用药",
      "frequency": "一天2次",
      "duration": "30天",
      "quantity": "2盒"
    },
    {
      "drug_name": "左氧氟沙星片",
      "dosage": "0.5g",
      "route": "口服",
      "frequency": "每日1次",
      "duration": "5天",
      "quantity": "5片"
    },
    {
      "drug_name": "复方甲氧那明胶囊",
      "dosage": "1.0粒",
      "route": "餐后口服",
      "frequency": "一天3次",
      "duration": "5天",
      "quantity": "1瓶"
    },
    {
      "drug_name": "盐酸氨溴索分散片",
      "dosage": "30.0mg",
      "route": "餐后口服",
      "frequency": "一天3次",
      "duration": "5天",
      "quantity": "15片"
    },
    {
      "drug_name": "醋酸泼尼松片",
      "dosage": "10.0mg",
      "route": "口服",
      "frequency": "每早1次",
      "duration": "3天",
      "quantity": "6片"
    }
  ]
}
2026-08-10 11:34:21,888 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-05]
2026-08-10 11:34:21,892 INFO     29 [qwen-vl-text] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1091238, prompt_len=1879
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共44行）
["广州医科大学附属第三医院", "The Third Affiliated Hospital of Guangzhou Medical University", "门(急)诊病历信息", "就诊卡", "流水", "姓", "病历编号:", "年 龄:41岁", "就诊科室:内科门诊(荔湾) 医", "就诊时间:2026-01-05 17:07:54", "主 诉:支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天", "现 病 史:2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激", "性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流", "涕、喷嚏,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响", "睡眠,晨起有咽干,曾到本院就诊两次,症状不见明显缓解。2021-1-9血常规:白细胞:", "12.52*109/L 嗜酸粒细胞:0.65*109/L 5.2%,经治疗后症状明显缓解。无咳嗽、咯痰、气", "促。病情稳定,本次门诊距上次门诊间隔时间30天。症状控制情况:过去4周,患者:吸入", "药物使用情况:遵医嘱使用;吸入装置使用情况:正确。急性发作情况:两次,就诊期间急", "性发作:无,发作次数:0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。长期规律使用信必", "可160/4.5ug 2吸 bid治疗,5天前开始出现咳嗽、咯痰,黄白痰,量少,难以咯出,咳嗽以", "夜间为主。无气促,伴咽息,鼻塞、流涕、喷嚏,无发热。", "既 往 史:鼻炎病史无规则治疗。打鼾明显。", "过 敏 史:未发现;", "个 人 史:否认遗传病史,吸烟10年,20支/日,2018年戒烟。偶饮酒。2021-12-20已打第", "三针新冠疫苗。", "体格检查:神志清,颈软,双肺呼吸音粗,可闻及散在哮鸣音,口腔粘膜无白斑。", "专科情况:", "辅助检查:", "治疗项目:", "门诊诊断:", "1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎", "处 置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。", "布地奈德福莫特罗吸入粉雾剂(II)2盒 2.0吸,吸入用药,一天2次 30天", "(省采)●①⑤", "左氧氟沙星片(省采)●⑥ 5片 0.5g,口服,每日1次(口服) 5天", "第1页", "广州医科大学附属第三医院", "The Third Affiliated Hospital of Guangzhou Medical University", "门(急)诊病历信息", "复方甲氧那明胶囊(省采)◆② 1瓶 1.0粒,餐后口服,一天3次(口服) 5天", "盐酸氨溴索分散片(省采)●⑥ 15片 30.0mg,餐后口服,一天3次(口服) 5", "天", "醋酸泼尼松片●②④ 6片 10.0mg,口服,每早1次(口服) 3天", "备 注:建议在住地附近社区医疗机构随诊。"]

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
2026-08-10 11:34:39,141 INFO     29 [qwen-vl-text] coord API raw response (len=3050):
```json
[
	{"text": "广州医科大学附属第三医院", "bbox": [98, 250, 252, 263]},
	{"text": "The Third Affiliated Hospital of Guangzhou Medical University", "bbox": [98, 261, 252, 268]},
	{"text": "门(急)诊病历信息", "bbox": [188, 280, 314, 294]},
	{"text": "就诊卡", "bbox": [50, 314, 83, 323]},
	{"text": "流水", "bbox": [50, 327, 77, 336]},
	{"text": "姓", "bbox": [50, 340, 63, 349]},
	{"text": "病历编号:", "bbox": [297, 327, 344, 336]},
	{"text": "年 龄:41岁", "bbox": [297, 340, 366, 349]},
	{"text": "就诊科室:内科门诊(荔湾) 医", "bbox": [50, 353, 214, 362]},
	{"text": "就诊时间:2026-01-05 17:07:54", "bbox": [297, 353, 446, 362]},
	{"text": "主 诉:支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天", "bbox": [50, 365, 314, 374]},
	{"text": "现 病 史:2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激", "bbox": [50, 378, 460, 387]},
	{"text": "性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流", "bbox": [50, 391, 455, 400]},
	{"text": "涕、喷嚏,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响", "bbox": [50, 404, 466, 413]},
	{"text": "睡眠,晨起有咽干,曾到本院就诊两次,症状不见明显缓解。2021-1-9血常规:白细胞:", "bbox": [50, 417, 451, 426]},
	{"text": "12.52*109/L 嗜酸粒细胞:0.65*109/L 5.2%,经治疗后症状明显缓解。无咳嗽、咯痰、气", "bbox": [50, 430, 465, 439]},
	{"text": "促。病情稳定,本次门诊距上次门诊间隔时间30天。症状控制情况:过去4周,患者:吸入", "bbox": [50, 443, 464, 452]},
	{"text": "药物使用情况:遵医嘱使用;吸入装置使用情况:正确。急性发作情况:两次,就诊期间急", "bbox": [50, 456, 469, 465]},
	{"text": "性发作:无,发作次数:0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。长期规律使用信必", "bbox": [50, 469, 465, 478]},
	{"text": "可160/4.5ug 2吸 bid治疗,5天前开始出现咳嗽、咯痰,黄白痰,量少,难以咯出,咳嗽以", "bbox": [50, 482, 472, 491]},
	{"text": "夜间为主。无气促,伴咽息,鼻塞、流涕、喷嚏,无发热。", "bbox": [50, 495, 319, 504]},
	{"text": "既 往 史:鼻炎病史无规则治疗。打鼾明显。", "bbox": [50, 508, 255, 517]},
	{"text": "过 敏 史:未发现;", "bbox": [50, 521, 140, 530]},
	{"text": "个 人 史:否认遗传病史,吸烟10年,20支/日,2018年戒烟。偶饮酒。2021-12-20已打第", "bbox": [50, 534, 471, 543]},
	{"text": "三针新冠疫苗。", "bbox": [50, 547, 118, 556]},
	{"text": "体格检查:神志清,颈软,双肺呼吸音粗,可闻及散在哮鸣音,口腔粘膜无白斑。", "bbox": [50, 560, 428, 570]},
	{"text": "专科情况:", "bbox": [50, 574, 97, 583]},
	{"text": "辅助检查:", "bbox": [50, 587, 97, 596]},
	{"text": "治疗项目:", "bbox": [50, 601, 97, 610]},
	{"text": "门诊诊断:", "bbox": [50, 615, 97, 624]},
	{"text": "1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎", "bbox": [50, 631, 432, 640]},
	{"text": "处 置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。", "bbox": [50, 645, 377, 655]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(II)2盒 2.0吸,吸入用药,一天2次 30天", "bbox": [109, 660, 458, 669]},
	{"text": "(省采)●①⑤", "bbox": [110, 674, 173, 683]},
	{"text": "左氧氟沙星片(省采)●⑥ 5片 0.5g,口服,每日1次(口服) 5天", "bbox": [109, 688, 460, 698]},
	{"text": "第1页", "bbox": [246, 706, 283, 714]},
	{"text": "广州医科大学附属第三医院", "bbox": [558, 245, 720, 258]},
	{"text": "The Third Affiliated Hospital of Guangzhou Medical University", "bbox": [558, 256, 720, 263]},
	{"text": "门(急)诊病历信息", "bbox": [654, 275, 786, 289]},
	{"text": "复方甲氧那明胶囊(省采)◆② 1瓶 1.0粒,餐后口服,一天3次(口服) 5天", "bbox": [569, 309, 945, 319]},
	{"text": "盐酸氨溴索分散片(省采)●⑥ 15片 30.0mg,餐后口服,一天3次(口服) 5", "bbox": [569, 323, 941, 333]},
	{"text": "天", "bbox": [766, 337, 779, 346]},
	{"text": "醋酸泼尼松片●②④ 6片 10.0mg,口服,每早1次(口服) 3天", "bbox": [569, 350, 931, 360]},
	{"text": "备 注:建议在住地附近社区医疗机构随诊。", "bbox": [511, 363, 732, 372]}
]
```
2026-08-10 11:34:39,142 INFO     29 [qwen-vl-text] coord API: raw_items=44, valid_items=44, elapsed=17.2s
2026-08-10 11:34:39,142 INFO     29 [qwen-vl-text] coord item[0]: text=广州医科大学附属第三医院, bbox=[98, 250, 252, 263]
2026-08-10 11:34:39,142 INFO     29 [qwen-vl-text] coord item[1]: text=The Third Affiliated Hospital of Guangzhou Medical University, bbox=[98, 261, 252, 268]
2026-08-10 11:34:39,142 INFO     29 [qwen-vl-text] coord item[2]: text=门(急)诊病历信息, bbox=[188, 280, 314, 294]
2026-08-10 11:34:39,142 INFO     29 [qwen-vl-text] coord item[3]: text=就诊卡, bbox=[50, 314, 83, 323]
2026-08-10 11:34:39,142 INFO     29 [qwen-vl-text] coord item[4]: text=流水, bbox=[50, 327, 77, 336]
2026-08-10 11:34:39,142 INFO     29 [qwen-vl-text] coord item[5]: text=姓, bbox=[50, 340, 63, 349]
2026-08-10 11:34:39,142 INFO     29 [qwen-vl-text] coord item[6]: text=病历编号:, bbox=[297, 327, 344, 336]
2026-08-10 11:34:39,142 INFO     29 [qwen-vl-text] coord item[7]: text=年 龄:41岁, bbox=[297, 340, 366, 349]
2026-08-10 11:34:39,142 INFO     29 [qwen-vl-text] coord item[8]: text=就诊科室:内科门诊(荔湾) 医, bbox=[50, 353, 214, 362]
2026-08-10 11:34:39,142 INFO     29 [qwen-vl-text] coord item[9]: text=就诊时间:2026-01-05 17:07:54, bbox=[297, 353, 446, 362]
2026-08-10 11:34:39,142 INFO     29 [qwen-vl-text] coord item[10]: text=主 诉:支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天, bbox=[50, 365, 314, 374]
2026-08-10 11:34:39,142 INFO     29 [qwen-vl-text] coord item[11]: text=现 病 史:2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激, bbox=[50, 378, 460, 387]
2026-08-10 11:34:39,142 INFO     29 [qwen-vl-text] coord item[12]: text=性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流, bbox=[50, 391, 455, 400]
2026-08-10 11:34:39,142 INFO     29 [qwen-vl-text] coord item[13]: text=涕、喷嚏,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响, bbox=[50, 404, 466, 413]
2026-08-10 11:34:39,142 INFO     29 [qwen-vl-text] coord item[14]: text=睡眠,晨起有咽干,曾到本院就诊两次,症状不见明显缓解。2021-1-9血常规:白细胞:, bbox=[50, 417, 451, 426]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[15]: text=12.52*109/L 嗜酸粒细胞:0.65*109/L 5.2%,经治疗后症状明显缓解。无咳嗽、咯痰、气, bbox=[50, 430, 465, 439]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[16]: text=促。病情稳定,本次门诊距上次门诊间隔时间30天。症状控制情况:过去4周,患者:吸入, bbox=[50, 443, 464, 452]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[17]: text=药物使用情况:遵医嘱使用;吸入装置使用情况:正确。急性发作情况:两次,就诊期间急, bbox=[50, 456, 469, 465]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[18]: text=性发作:无,发作次数:0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。长期规律使用信必, bbox=[50, 469, 465, 478]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[19]: text=可160/4.5ug 2吸 bid治疗,5天前开始出现咳嗽、咯痰,黄白痰,量少,难以咯出,咳嗽以, bbox=[50, 482, 472, 491]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[20]: text=夜间为主。无气促,伴咽息,鼻塞、流涕、喷嚏,无发热。, bbox=[50, 495, 319, 504]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[21]: text=既 往 史:鼻炎病史无规则治疗。打鼾明显。, bbox=[50, 508, 255, 517]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[22]: text=过 敏 史:未发现;, bbox=[50, 521, 140, 530]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[23]: text=个 人 史:否认遗传病史,吸烟10年,20支/日,2018年戒烟。偶饮酒。2021-12-20已打第, bbox=[50, 534, 471, 543]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[24]: text=三针新冠疫苗。, bbox=[50, 547, 118, 556]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[25]: text=体格检查:神志清,颈软,双肺呼吸音粗,可闻及散在哮鸣音,口腔粘膜无白斑。, bbox=[50, 560, 428, 570]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[26]: text=专科情况:, bbox=[50, 574, 97, 583]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[27]: text=辅助检查:, bbox=[50, 587, 97, 596]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[28]: text=治疗项目:, bbox=[50, 601, 97, 610]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[29]: text=门诊诊断:, bbox=[50, 615, 97, 624]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[30]: text=1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎, bbox=[50, 631, 432, 640]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[31]: text=处 置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。, bbox=[50, 645, 377, 655]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[32]: text=布地奈德福莫特罗吸入粉雾剂(II)2盒 2.0吸,吸入用药,一天2次 30天, bbox=[109, 660, 458, 669]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[33]: text=(省采)●①⑤, bbox=[110, 674, 173, 683]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[34]: text=左氧氟沙星片(省采)●⑥ 5片 0.5g,口服,每日1次(口服) 5天, bbox=[109, 688, 460, 698]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[35]: text=第1页, bbox=[246, 706, 283, 714]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[36]: text=广州医科大学附属第三医院, bbox=[558, 245, 720, 258]
2026-08-10 11:34:39,143 INFO     29 [qwen-vl-text] coord item[37]: text=The Third Affiliated Hospital of Guangzhou Medical University, bbox=[558, 256, 720, 263]
2026-08-10 11:34:39,144 INFO     29 [qwen-vl-text] coord item[38]: text=门(急)诊病历信息, bbox=[654, 275, 786, 289]
2026-08-10 11:34:39,144 INFO     29 [qwen-vl-text] coord item[39]: text=复方甲氧那明胶囊(省采)◆② 1瓶 1.0粒,餐后口服,一天3次(口服) 5天, bbox=[569, 309, 945, 319]
2026-08-10 11:34:39,144 INFO     29 [qwen-vl-text] coord item[40]: text=盐酸氨溴索分散片(省采)●⑥ 15片 30.0mg,餐后口服,一天3次(口服) 5, bbox=[569, 323, 941, 333]
2026-08-10 11:34:39,144 INFO     29 [qwen-vl-text] coord item[41]: text=天, bbox=[766, 337, 779, 346]
2026-08-10 11:34:39,144 INFO     29 [qwen-vl-text] coord item[42]: text=醋酸泼尼松片●②④ 6片 10.0mg,口服,每早1次(口服) 3天, bbox=[569, 350, 931, 360]
2026-08-10 11:34:39,144 INFO     29 [qwen-vl-text] coord item[43]: text=备 注:建议在住地附近社区医疗机构随诊。, bbox=[511, 363, 732, 372]
2026-08-10 11:34:39,144 INFO     29 [qwen-vl-text] page=13 — 44/44 coords, api_time=17.2s
2026-08-10 11:34:39,144 INFO     29 [qwen-vl-text] new_positions (44):
[[13, 58.309999999999995, 149.94, 210.5, 221.446], [13, 58.309999999999995, 149.94, 219.762, 225.656], [13, 111.86, 186.82999999999998, 235.76, 247.548], [13, 29.75, 49.385, 264.388, 271.966], [13, 29.75, 45.815, 275.334, 282.912], [13, 29.75, 37.485, 286.28, 293.858], [13, 176.715, 204.67999999999998, 275.334, 282.912], [13, 176.715, 217.76999999999998, 286.28, 293.858], [13, 29.75, 127.33, 297.226, 304.804], [13, 176.715, 265.37, 297.226, 304.804], [13, 29.75, 186.82999999999998, 307.33, 314.908], [13, 29.75, 273.7, 318.276, 325.854], [13, 29.75, 270.72499999999997, 329.222, 336.8], [13, 29.75, 277.27, 340.168, 347.746], [13, 29.75, 268.34499999999997, 351.114, 358.692], [13, 29.75, 276.675, 362.06, 369.638], [13, 29.75, 276.08, 373.006, 380.584], [13, 29.75, 279.055, 383.952, 391.53], [13, 29.75, 276.675, 394.89799999999997, 402.476], [13, 29.75, 280.84, 405.844, 413.42199999999997], [13, 29.75, 189.80499999999998, 416.78999999999996, 424.368], [13, 29.75, 151.725, 427.736, 435.31399999999996], [13, 29.75, 83.3, 438.68199999999996, 446.26], [13, 29.75, 280.245, 449.628, 457.20599999999996], [13, 29.75, 70.21, 460.574, 468.152], [13, 29.75, 254.66, 471.52, 479.94], [13, 29.75, 57.714999999999996, 483.308, 490.88599999999997], [13, 29.75, 57.714999999999996, 494.25399999999996, 501.832], [13, 29.75, 57.714999999999996, 506.042, 513.62], [13, 29.75, 57.714999999999996, 517.8299999999999, 525.408], [13, 29.75, 257.03999999999996, 531.302, 538.88], [13, 29.75, 224.315, 543.09, 551.51], [13, 64.855, 272.51, 555.72, 563.298], [13, 65.45, 102.935, 567.5079999999999, 575.086], [13, 64.855, 273.7, 579.2959999999999, 587.716], [13, 146.37, 168.385, 594.452, 601.188], [13, 332.01, 428.4, 206.29, 217.236], [13, 332.01, 428.4, 215.552, 221.446], [13, 389.13, 467.66999999999996, 231.54999999999998, 243.338], [13, 338.555, 562.275, 260.178, 268.598], [13, 338.555, 559.895, 271.966, 280.38599999999997], [13, 455.77, 463.505, 283.75399999999996, 291.332], [13, 338.555, 553.9449999999999, 294.7, 303.12], [13, 304.04499999999996, 435.53999999999996, 305.646, 313.224]]
2026-08-10 11:34:39,144 INFO     29 [qwen-vl-text] ═══ DONE ═══ 44 positions, pages=1, time=24.6s
2026-08-10 11:34:39,145 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:34:39,146 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:34:39,146 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:34:39,146 INFO     29 [qwen-vl-text] positions(28): [[14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:34:39,147 INFO     29 [qwen-vl-text] page grouping: [14], lines per page: [28]
2026-08-10 11:34:39,378 INFO     29 [qwen-vl-text] page=14, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:34:39,379 INFO     29 [qwen-vl-text] LLM extraction start, text_len=722
2026-08-10 11:34:39,379 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:34:39,379 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 766, \"bbox_end\": 793, \"encounter_dates\": [\"2026-02-04\"], \"department\": \"内科门诊（荔湾）\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊/住院病历信息\n就诊卡号：\n病历编号：\n流水号\n姓名\n性别：男\n年龄：41岁\n就诊科室：内科门诊（荔湾）\n就诊时间：2026-02-04 11:21:11\n主诉：支气管哮喘治疗后复查\n现病史：2021年2月前开始出现咳嗽、咳痰，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sng 2吸 bid治疗。\n既往史：鼻炎病史无规则治疗，打鼾明显。\n过敏史：未发现；\n个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。\n体格检查：神志清，颈软，双肺呼吸音粗，可闻及散在哮鸣音，口腔粘膜无白斑。\n专科情况：\n辅助检查：\n治疗项目：\n门诊诊断：\n1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、急性气管支气管炎\n单病种：\n发病时间：\n处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不遥随诊。\n布地奈德福莫特罗吸入粉雾剂(II)(省\n2 2.0班，吸入用药，一天2次\n30\n采)●①②\n查天",
    "role": "user"
  }
]
2026-08-10 11:34:43,613 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:34:43,613 INFO     29 [qwen-vl-text] LLM output (len=646):
{
  "encounter_date": "2026-02-04",
  "chief_complaint": "支气管哮喘治疗后复查",
  "present_illness": "2021年2月前开始出现咳嗽、咳痰，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sng 2吸 bid治疗。",
  "past_history": "鼻炎病史无规则治疗，打鼾明显。否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。",
  "diagnosis": "1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、急性气管支气管炎",
  "treatment_plan": "布地奈德福莫特罗吸入粉雾剂(II) 2.0班，吸入用药，一天2次"
}
2026-08-10 11:34:43,613 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-04]
2026-08-10 11:34:43,620 INFO     29 [qwen-vl-text] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1605519, prompt_len=1419
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["门诊/住院病历信息", "就诊卡号：", "病历编号：", "流水号", "姓名", "性别：男", "年龄：41岁", "就诊科室：内科门诊（荔湾）", "就诊时间：2026-02-04 11:21:11", "主诉：支气管哮喘治疗后复查", "现病史：2021年2月前开始出现咳嗽、咳痰，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sng 2吸 bid治疗。", "既往史：鼻炎病史无规则治疗，打鼾明显。", "过敏史：未发现；", "个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。", "体格检查：神志清，颈软，双肺呼吸音粗，可闻及散在哮鸣音，口腔粘膜无白斑。", "专科情况：", "辅助检查：", "治疗项目：", "门诊诊断：", "1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、急性气管支气管炎", "单病种：", "发病时间：", "处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不遥随诊。", "布地奈德福莫特罗吸入粉雾剂(II)(省", "2 2.0班，吸入用药，一天2次", "30", "采)●①②", "查天"]

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
2026-08-10 11:34:55,095 INFO     29 [qwen-vl-text] coord API raw response (len=1987):
[
	{"text": "门诊/住院病历信息", "bbox": [338, 155, 525, 169]},
	{"text": "就诊卡号：", "bbox": [187, 194, 262, 207], "bbox": [187, 194, 262, 207]},
	{"text": "病历编号：", "bbox": [509, 220, 577, 233]},
	{"text": "流水号", "bbox": [187, 220, 262, 233]},
	{"text": "姓名", "bbox": [187, 246, 202, 259]},
	{"text": "性别：男", "bbox": [431, 246, 475, 259]},
	{"text": "年龄：41岁", "bbox": [585, 246, 639, 259]},
	{"text": "就诊科室：内科门诊（荔湾）", "bbox": [187, 271, 373, 284]},
	{"text": "就诊时间：2026-02-04 11:21:11", "bbox": [517, 271, 732, 284]},
	{"text": "主诉：支气管哮喘治疗后复查", "bbox": [187, 297, 465, 310]},
	{"text": "现病史：2021年2月前开始出现咳嗽、咳痰，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sng 2吸 bid治疗。", "bbox": [187, 323, 774, 467]},
	{"text": "既往史：鼻炎病史无规则治疗，打鼾明显。", "bbox": [187, 477, 507, 490]},
	{"text": "过敏史：未发现；", "bbox": [187, 502, 339, 515]},
	{"text": "个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。", "bbox": [187, 526, 762, 554]},
	{"text": "体格检查：神志清，颈软，双肺呼吸音粗，可闻及散在哮鸣音，口腔粘膜无白斑。", "bbox": [187, 567, 727, 580]},
	{"text": "专科情况：", "bbox": [187, 591, 258, 604]},
	{"text": "辅助检查：", "bbox": [187, 616, 258, 629]},
	{"text": "治疗项目：", "bbox": [187, 639, 258, 652]},
	{"text": "门诊诊断：", "bbox": [187, 664, 258, 677]},
	{"text": "1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、急性气管支气管炎", "bbox": [207, 687, 645, 699]},
	{"text": "单病种：", "bbox": [187, 710, 274, 723]},
	{"text": "发病时间：", "bbox": [187, 733, 258, 746]},
	{"text": "处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不遥随诊。", "bbox": [269, 755, 677, 767]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(II)(省", "bbox": [217, 779, 461, 791]},
	{"text": "2 2.0班，吸入用药，一天2次", "bbox": [519, 779, 703, 791]},
	{"text": "30", "bbox": [732, 779, 746, 789]},
	{"text": "采)●①②", "bbox": [217, 795, 283, 807]},
	{"text": "查天", "bbox": [519, 795, 555, 807]}
]
2026-08-10 11:34:55,096 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=11.5s
2026-08-10 11:34:55,096 INFO     29 [qwen-vl-text] coord item[0]: text=门诊/住院病历信息, bbox=[338, 155, 525, 169]
2026-08-10 11:34:55,096 INFO     29 [qwen-vl-text] coord item[1]: text=就诊卡号：, bbox=[187, 194, 262, 207]
2026-08-10 11:34:55,096 INFO     29 [qwen-vl-text] coord item[2]: text=病历编号：, bbox=[509, 220, 577, 233]
2026-08-10 11:34:55,097 INFO     29 [qwen-vl-text] coord item[3]: text=流水号, bbox=[187, 220, 262, 233]
2026-08-10 11:34:55,097 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[187, 246, 202, 259]
2026-08-10 11:34:55,097 INFO     29 [qwen-vl-text] coord item[5]: text=性别：男, bbox=[431, 246, 475, 259]
2026-08-10 11:34:55,097 INFO     29 [qwen-vl-text] coord item[6]: text=年龄：41岁, bbox=[585, 246, 639, 259]
2026-08-10 11:34:55,097 INFO     29 [qwen-vl-text] coord item[7]: text=就诊科室：内科门诊（荔湾）, bbox=[187, 271, 373, 284]
2026-08-10 11:34:55,097 INFO     29 [qwen-vl-text] coord item[8]: text=就诊时间：2026-02-04 11:21:11, bbox=[517, 271, 732, 284]
2026-08-10 11:34:55,097 INFO     29 [qwen-vl-text] coord item[9]: text=主诉：支气管哮喘治疗后复查, bbox=[187, 297, 465, 310]
2026-08-10 11:34:55,097 INFO     29 [qwen-vl-text] coord item[10]: text=现病史：2021年2月前开始出现咳嗽、咳痰，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sng 2吸 bid治疗。, bbox=[187, 323, 774, 467]
2026-08-10 11:34:55,097 INFO     29 [qwen-vl-text] coord item[11]: text=既往史：鼻炎病史无规则治疗，打鼾明显。, bbox=[187, 477, 507, 490]
2026-08-10 11:34:55,097 INFO     29 [qwen-vl-text] coord item[12]: text=过敏史：未发现；, bbox=[187, 502, 339, 515]
2026-08-10 11:34:55,097 INFO     29 [qwen-vl-text] coord item[13]: text=个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。, bbox=[187, 526, 762, 554]
2026-08-10 11:34:55,097 INFO     29 [qwen-vl-text] coord item[14]: text=体格检查：神志清，颈软，双肺呼吸音粗，可闻及散在哮鸣音，口腔粘膜无白斑。, bbox=[187, 567, 727, 580]
2026-08-10 11:34:55,097 INFO     29 [qwen-vl-text] coord item[15]: text=专科情况：, bbox=[187, 591, 258, 604]
2026-08-10 11:34:55,098 INFO     29 [qwen-vl-text] coord item[16]: text=辅助检查：, bbox=[187, 616, 258, 629]
2026-08-10 11:34:55,098 INFO     29 [qwen-vl-text] coord item[17]: text=治疗项目：, bbox=[187, 639, 258, 652]
2026-08-10 11:34:55,098 INFO     29 [qwen-vl-text] coord item[18]: text=门诊诊断：, bbox=[187, 664, 258, 677]
2026-08-10 11:34:55,098 INFO     29 [qwen-vl-text] coord item[19]: text=1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、急性气管支气管炎, bbox=[207, 687, 645, 699]
2026-08-10 11:34:55,098 INFO     29 [qwen-vl-text] coord item[20]: text=单病种：, bbox=[187, 710, 274, 723]
2026-08-10 11:34:55,098 INFO     29 [qwen-vl-text] coord item[21]: text=发病时间：, bbox=[187, 733, 258, 746]
2026-08-10 11:34:55,098 INFO     29 [qwen-vl-text] coord item[22]: text=处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不遥随诊。, bbox=[269, 755, 677, 767]
2026-08-10 11:34:55,098 INFO     29 [qwen-vl-text] coord item[23]: text=布地奈德福莫特罗吸入粉雾剂(II)(省, bbox=[217, 779, 461, 791]
2026-08-10 11:34:55,098 INFO     29 [qwen-vl-text] coord item[24]: text=2 2.0班，吸入用药，一天2次, bbox=[519, 779, 703, 791]
2026-08-10 11:34:55,098 INFO     29 [qwen-vl-text] coord item[25]: text=30, bbox=[732, 779, 746, 789]
2026-08-10 11:34:55,098 INFO     29 [qwen-vl-text] coord item[26]: text=采)●①②, bbox=[217, 795, 283, 807]
2026-08-10 11:34:55,099 INFO     29 [qwen-vl-text] coord item[27]: text=查天, bbox=[519, 795, 555, 807]
2026-08-10 11:34:55,099 INFO     29 [qwen-vl-text] page=14 — 28/28 coords, api_time=11.5s
2026-08-10 11:34:55,099 INFO     29 [qwen-vl-text] new_positions (28):
[[14, 201.10999999999999, 312.375, 130.51, 142.298], [14, 111.265, 155.89, 163.34799999999998, 174.29399999999998], [14, 302.85499999999996, 343.315, 185.23999999999998, 196.186], [14, 111.265, 155.89, 185.23999999999998, 196.186], [14, 111.265, 120.19, 207.132, 218.078], [14, 256.445, 282.625, 207.132, 218.078], [14, 348.075, 380.205, 207.132, 218.078], [14, 111.265, 221.935, 228.182, 239.128], [14, 307.615, 435.53999999999996, 228.182, 239.128], [14, 111.265, 276.675, 250.07399999999998, 261.02], [14, 111.265, 460.53, 271.966, 393.214], [14, 111.265, 301.66499999999996, 401.63399999999996, 412.58], [14, 111.265, 201.70499999999998, 422.68399999999997, 433.63], [14, 111.265, 453.39, 442.892, 466.46799999999996], [14, 111.265, 432.565, 477.414, 488.35999999999996], [14, 111.265, 153.51, 497.62199999999996, 508.568], [14, 111.265, 153.51, 518.672, 529.6179999999999], [14, 111.265, 153.51, 538.038, 548.984], [14, 111.265, 153.51, 559.088, 570.034], [14, 123.16499999999999, 383.775, 578.454, 588.558], [14, 111.265, 163.03, 597.8199999999999, 608.766], [14, 111.265, 153.51, 617.1859999999999, 628.132], [14, 160.055, 402.815, 635.7099999999999, 645.814], [14, 129.11499999999998, 274.295, 655.918, 666.0219999999999], [14, 308.805, 418.28499999999997, 655.918, 666.0219999999999], [14, 435.53999999999996, 443.87, 655.918, 664.338], [14, 129.11499999999998, 168.385, 669.39, 679.494], [14, 308.805, 330.22499999999997, 669.39, 679.494]]
2026-08-10 11:34:55,099 INFO     29 [qwen-vl-text] ═══ DONE ═══ 28 positions, pages=1, time=16.0s
2026-08-10 11:34:55,116 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 11:34:55,117 INFO     29 [Trace] task=ea51b5dc | doc=LZK 哮喘 广三(2).pdf | Extractor:Clinical | outputs={"chunks": "5 items, types={'OutpatientRecord': 5}", "html": "", "json": "1039 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(2).pdf", "output_format": "chunks", "chunks_Clinical": "5 items, types={'OutpatientRecord': 5}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 5, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-10 11:34:55,117 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 11:34:55,118 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:34:55.117+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 23, "failed": 0, "current": {"ea51b5dc94ae11f1bd9827cf206dfa2d": {"id": "ea51b5dc94ae11f1bd9827cf206dfa2d", "doc_id": "ea1b0b1894ae11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786361440167, "task_type": "dataflow", "root_trace_id": "bca8d639df704cd29f0107370613ab01", "root_traceparent": "00-bca8d639df704cd29f0107370613ab01-b8b3c91a32048c1c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:34:55,126 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:34:55,126 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:34:56,274 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:34:56,282 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 11:34:56,282 INFO     29 [Trace] task=ea51b5dc | doc=LZK 哮喘 广三(2).pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "1039 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(2).pdf", "output_format": "chunks", "chunks_Clinical": "5 items, types={'OutpatientRecord': 5}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 5, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-10 11:34:56,282 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 11:34:56,294 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:34:56,295 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:34:56,295 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:34:56,295 INFO     29 [qwen-vl-text] positions(26): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:34:56,296 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [26]
2026-08-10 11:34:56,458 INFO     29 [qwen-vl-text] page=4, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:34:56,459 INFO     29 [qwen-vl-text] LLM extraction start, text_len=199
2026-08-10 11:34:56,459 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:34:56,459 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 120, \"bbox_end\": 145, \"encounter_dates\": [\"2025-07-18\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-07-18\n就诊科室:内科门诊\n主诊医\n姓名\n性别:男\n年龄:40岁\n卡号:\n患者\n医疗证号:\n处方号\n地址:PT027气雾剂 2024017-呼吸科\n身份证\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n布地奈德福莫特罗吸入粉雾剂0.125/0.0006*60吸6盒\n183.41100.46\nSig\n2吸/次,吸入,bid*90天",
    "role": "user"
  }
]
2026-08-10 11:34:58,175 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:34:58,175 INFO     29 [qwen-vl-text] LLM output (len=413):
{
  "encounter_date": "2025-07-18",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "布地奈德福莫特罗吸入粉雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "2吸/次",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 90,
      "quantity": "6盒",
      "notes": null
    }
  ]
}
2026-08-10 11:34:58,176 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-07-18]
2026-08-10 11:34:58,178 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=919286, prompt_len=890
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["门(急)诊处方", "就诊时间:2025-07-18", "就诊科室:内科门诊", "主诊医", "姓名", "性别:男", "年龄:40岁", "卡号:", "患者", "医疗证号:", "处方号", "地址:PT027气雾剂 2024017-呼吸科", "身份证", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂0.125/0.0006*60吸6盒", "183.41100.46", "Sig", "2吸/次,吸入,bid*90天"]

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
2026-08-10 11:35:06,935 INFO     29 [qwen-vl-text] coord API raw response (len=1336):
[
	{"text": "门(急)诊处方", "bbox": [385, 24, 625, 92]},
	{"text": "就诊时间:2025-07-18", "bbox": [38, 117, 284, 150]},
	{"text": "就诊科室:内科门诊", "bbox": [321, 117, 531, 150]},
	{"text": "主诊医", "bbox": [617, 117, 685, 150]},
	{"text": "姓名", "bbox": [38, 170, 85, 203]},
	{"text": "性别:男", "bbox": [321, 170, 407, 203]},
	{"text": "年龄:40岁", "bbox": [457, 170, 568, 203]},
	{"text": "卡号:", "bbox": [617, 170, 678, 203]},
	{"text": "患者", "bbox": [38, 222, 85, 255]},
	{"text": "医疗证号:", "bbox": [321, 222, 426, 255]},
	{"text": "处方号", "bbox": [613, 224, 684, 257]},
	{"text": "地址:PT027气雾剂 2024017-呼吸科", "bbox": [38, 276, 436, 309]},
	{"text": "身份证", "bbox": [612, 276, 683, 309]},
	{"text": "诊断:支气管哮喘", "bbox": [38, 324, 222, 357]},
	{"text": "西药处方", "bbox": [434, 383, 564, 416]},
	{"text": "组号", "bbox": [107, 444, 156, 477]},
	{"text": "项目名称", "bbox": [215, 444, 314, 477]},
	{"text": "规格", "bbox": [506, 444, 550, 477]},
	{"text": "总量", "bbox": [709, 444, 755, 477]},
	{"text": "单价", "bbox": [812, 444, 858, 477]},
	{"text": "金额", "bbox": [893, 444, 938, 477]},
	{"text": "R:", "bbox": [61, 504, 108, 554]},
	{"text": "布地奈德福莫特罗吸入粉雾剂0.125/0.0006*60吸6盒", "bbox": [195, 498, 737, 531]},
	{"text": "183.41100.46", "bbox": [767, 500, 923, 528]},
	{"text": "Sig", "bbox": [424, 550, 461, 580]},
	{"text": "2吸/次,吸入,bid*90天", "bbox": [504, 548, 747, 580]}
]
2026-08-10 11:35:06,935 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=8.8s
2026-08-10 11:35:06,935 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[385, 24, 625, 92]
2026-08-10 11:35:06,935 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-07-18, bbox=[38, 117, 284, 150]
2026-08-10 11:35:06,935 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[321, 117, 531, 150]
2026-08-10 11:35:06,935 INFO     29 [qwen-vl-text] coord item[3]: text=主诊医, bbox=[617, 117, 685, 150]
2026-08-10 11:35:06,935 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[38, 170, 85, 203]
2026-08-10 11:35:06,935 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[321, 170, 407, 203]
2026-08-10 11:35:06,935 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:40岁, bbox=[457, 170, 568, 203]
2026-08-10 11:35:06,935 INFO     29 [qwen-vl-text] coord item[7]: text=卡号:, bbox=[617, 170, 678, 203]
2026-08-10 11:35:06,935 INFO     29 [qwen-vl-text] coord item[8]: text=患者, bbox=[38, 222, 85, 255]
2026-08-10 11:35:06,935 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[321, 222, 426, 255]
2026-08-10 11:35:06,935 INFO     29 [qwen-vl-text] coord item[10]: text=处方号, bbox=[613, 224, 684, 257]
2026-08-10 11:35:06,935 INFO     29 [qwen-vl-text] coord item[11]: text=地址:PT027气雾剂 2024017-呼吸科, bbox=[38, 276, 436, 309]
2026-08-10 11:35:06,935 INFO     29 [qwen-vl-text] coord item[12]: text=身份证, bbox=[612, 276, 683, 309]
2026-08-10 11:35:06,935 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[38, 324, 222, 357]
2026-08-10 11:35:06,935 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[434, 383, 564, 416]
2026-08-10 11:35:06,935 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[107, 444, 156, 477]
2026-08-10 11:35:06,936 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[215, 444, 314, 477]
2026-08-10 11:35:06,937 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[506, 444, 550, 477]
2026-08-10 11:35:06,937 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[709, 444, 755, 477]
2026-08-10 11:35:06,937 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[812, 444, 858, 477]
2026-08-10 11:35:06,937 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[893, 444, 938, 477]
2026-08-10 11:35:06,937 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[61, 504, 108, 554]
2026-08-10 11:35:06,937 INFO     29 [qwen-vl-text] coord item[22]: text=布地奈德福莫特罗吸入粉雾剂0.125/0.0006*60吸6盒, bbox=[195, 498, 737, 531]
2026-08-10 11:35:06,937 INFO     29 [qwen-vl-text] coord item[23]: text=183.41100.46, bbox=[767, 500, 923, 528]
2026-08-10 11:35:06,937 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[424, 550, 461, 580]
2026-08-10 11:35:06,937 INFO     29 [qwen-vl-text] coord item[25]: text=2吸/次,吸入,bid*90天, bbox=[504, 548, 747, 580]
2026-08-10 11:35:06,937 INFO     29 [qwen-vl-text] page=4 — 26/26 coords, api_time=8.8s
2026-08-10 11:35:06,937 INFO     29 [qwen-vl-text] new_positions (26):
[[4, 324.17, 526.25, 14.28, 54.739999999999995], [4, 31.996, 239.128, 69.615, 89.25], [4, 270.282, 447.102, 69.615, 89.25], [4, 519.514, 576.77, 69.615, 89.25], [4, 31.996, 71.57, 101.14999999999999, 120.785], [4, 270.282, 342.69399999999996, 101.14999999999999, 120.785], [4, 384.794, 478.256, 101.14999999999999, 120.785], [4, 519.514, 570.876, 101.14999999999999, 120.785], [4, 31.996, 71.57, 132.09, 151.725], [4, 270.282, 358.692, 132.09, 151.725], [4, 516.146, 575.928, 133.28, 152.915], [4, 31.996, 367.11199999999997, 164.22, 183.855], [4, 515.304, 575.086, 164.22, 183.855], [4, 31.996, 186.924, 192.78, 212.415], [4, 365.428, 474.888, 227.885, 247.51999999999998], [4, 90.094, 131.352, 264.18, 283.815], [4, 181.03, 264.388, 264.18, 283.815], [4, 426.05199999999996, 463.09999999999997, 264.18, 283.815], [4, 596.978, 635.7099999999999, 264.18, 283.815], [4, 683.704, 722.4359999999999, 264.18, 283.815], [4, 751.906, 789.7959999999999, 264.18, 283.815], [4, 51.361999999999995, 90.93599999999999, 299.88, 329.63], [4, 164.19, 620.554, 296.31, 315.945], [4, 645.814, 777.1659999999999, 297.5, 314.15999999999997], [4, 357.008, 388.162, 327.25, 345.09999999999997], [4, 424.368, 628.9739999999999, 326.06, 345.09999999999997]]
2026-08-10 11:35:06,937 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=10.6s
2026-08-10 11:35:06,937 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:35:06,938 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:35:06,938 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:35:06,938 INFO     29 [qwen-vl-text] positions(26): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:35:06,938 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [26]
2026-08-10 11:35:07,104 INFO     29 [qwen-vl-text] page=5, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:35:07,105 INFO     29 [qwen-vl-text] LLM extraction start, text_len=205
2026-08-10 11:35:07,105 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:35:07,105 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 146, \"bbox_end\": 171, \"encounter_dates\": [\"2025-04-25\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-04-25\n就诊科室:内科门诊\n主诊\n姓名\n性别:男\n年龄:40岁\n卡号:\n患者类型:GLP支付\n医疗证号:\n处方号\n地址:PT027气雾剂 2024017-呼吸科\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n布地奈德福莫特罗吸入粉雾剂(II)●●@ug*60吸6盒\n183.41100.46\nSig\n2吸/次,吸入,bid*90天",
    "role": "user"
  }
]
2026-08-10 11:35:09,303 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:35:09,304 INFO     29 [qwen-vl-text] LLM output (len=417):
{
  "encounter_date": "2025-04-25",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "布地奈德福莫特罗吸入粉雾剂(II)",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "2吸/次",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 90,
      "quantity": "6盒",
      "notes": null
    }
  ]
}
2026-08-10 11:35:09,304 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-04-25]
2026-08-10 11:35:09,309 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=892488, prompt_len=896
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["门(急)诊处方", "就诊时间:2025-04-25", "就诊科室:内科门诊", "主诊", "姓名", "性别:男", "年龄:40岁", "卡号:", "患者类型:GLP支付", "医疗证号:", "处方号", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂(II)●●@ug*60吸6盒", "183.41100.46", "Sig", "2吸/次,吸入,bid*90天"]

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
2026-08-10 11:35:17,002 INFO     29 [qwen-vl-text] coord API raw response (len=1343):
[
	{"text": "门(急)诊处方", "bbox": [375, 21, 604, 88]},
	{"text": "就诊时间:2025-04-25", "bbox": [48, 117, 283, 153]},
	{"text": "就诊科室:内科门诊", "bbox": [317, 115, 518, 150]},
	{"text": "主诊", "bbox": [601, 115, 661, 150]},
	{"text": "姓名", "bbox": [48, 172, 97, 207]},
	{"text": "性别:男", "bbox": [317, 170, 401, 205]},
	{"text": "年龄:40岁", "bbox": [448, 170, 555, 205]},
	{"text": "卡号:", "bbox": [601, 170, 655, 205]},
	{"text": "患者类型:GLP支付", "bbox": [50, 228, 245, 262]},
	{"text": "医疗证号:", "bbox": [318, 227, 421, 262]},
	{"text": "处方号", "bbox": [601, 227, 661, 262]},
	{"text": "地址:PT027气雾剂 2024017-呼吸科", "bbox": [50, 280, 432, 317]},
	{"text": "身份证号:", "bbox": [601, 280, 704, 315]},
	{"text": "诊断:支气管哮喘", "bbox": [51, 333, 229, 368]},
	{"text": "西药处方", "bbox": [431, 393, 559, 428]},
	{"text": "组号", "bbox": [119, 458, 167, 493]},
	{"text": "项目名称", "bbox": [223, 458, 317, 493]},
	{"text": "规格", "bbox": [503, 458, 546, 491]},
	{"text": "总量", "bbox": [702, 458, 748, 491]},
	{"text": "单价", "bbox": [805, 456, 851, 491]},
	{"text": "金额", "bbox": [886, 456, 933, 491]},
	{"text": "R:", "bbox": [74, 522, 120, 575]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(II)●●@ug*60吸6盒", "bbox": [204, 517, 731, 553]},
	{"text": "183.41100.46", "bbox": [761, 517, 919, 548]},
	{"text": "Sig", "bbox": [424, 570, 462, 604]},
	{"text": "2吸/次,吸入,bid*90天", "bbox": [503, 568, 743, 603]}
]
2026-08-10 11:35:17,003 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=7.7s
2026-08-10 11:35:17,003 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[375, 21, 604, 88]
2026-08-10 11:35:17,003 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-04-25, bbox=[48, 117, 283, 153]
2026-08-10 11:35:17,003 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[317, 115, 518, 150]
2026-08-10 11:35:17,003 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[601, 115, 661, 150]
2026-08-10 11:35:17,003 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[48, 172, 97, 207]
2026-08-10 11:35:17,003 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[317, 170, 401, 205]
2026-08-10 11:35:17,003 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:40岁, bbox=[448, 170, 555, 205]
2026-08-10 11:35:17,004 INFO     29 [qwen-vl-text] coord item[7]: text=卡号:, bbox=[601, 170, 655, 205]
2026-08-10 11:35:17,004 INFO     29 [qwen-vl-text] coord item[8]: text=患者类型:GLP支付, bbox=[50, 228, 245, 262]
2026-08-10 11:35:17,004 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[318, 227, 421, 262]
2026-08-10 11:35:17,004 INFO     29 [qwen-vl-text] coord item[10]: text=处方号, bbox=[601, 227, 661, 262]
2026-08-10 11:35:17,004 INFO     29 [qwen-vl-text] coord item[11]: text=地址:PT027气雾剂 2024017-呼吸科, bbox=[50, 280, 432, 317]
2026-08-10 11:35:17,004 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[601, 280, 704, 315]
2026-08-10 11:35:17,004 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[51, 333, 229, 368]
2026-08-10 11:35:17,004 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[431, 393, 559, 428]
2026-08-10 11:35:17,004 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[119, 458, 167, 493]
2026-08-10 11:35:17,004 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[223, 458, 317, 493]
2026-08-10 11:35:17,004 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[503, 458, 546, 491]
2026-08-10 11:35:17,004 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[702, 458, 748, 491]
2026-08-10 11:35:17,004 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[805, 456, 851, 491]
2026-08-10 11:35:17,004 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[886, 456, 933, 491]
2026-08-10 11:35:17,004 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[74, 522, 120, 575]
2026-08-10 11:35:17,004 INFO     29 [qwen-vl-text] coord item[22]: text=布地奈德福莫特罗吸入粉雾剂(II)●●@ug*60吸6盒, bbox=[204, 517, 731, 553]
2026-08-10 11:35:17,004 INFO     29 [qwen-vl-text] coord item[23]: text=183.41100.46, bbox=[761, 517, 919, 548]
2026-08-10 11:35:17,004 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[424, 570, 462, 604]
2026-08-10 11:35:17,004 INFO     29 [qwen-vl-text] coord item[25]: text=2吸/次,吸入,bid*90天, bbox=[503, 568, 743, 603]
2026-08-10 11:35:17,005 INFO     29 [qwen-vl-text] page=5 — 26/26 coords, api_time=7.7s
2026-08-10 11:35:17,005 INFO     29 [qwen-vl-text] new_positions (26):
[[5, 315.75, 508.568, 12.495, 52.36], [5, 40.416, 238.286, 69.615, 91.035], [5, 266.914, 436.156, 68.425, 89.25], [5, 506.042, 556.562, 68.425, 89.25], [5, 40.416, 81.67399999999999, 102.33999999999999, 123.16499999999999], [5, 266.914, 337.642, 101.14999999999999, 121.975], [5, 377.216, 467.31, 101.14999999999999, 121.975], [5, 506.042, 551.51, 101.14999999999999, 121.975], [5, 42.1, 206.29, 135.66, 155.89], [5, 267.756, 354.48199999999997, 135.065, 155.89], [5, 506.042, 556.562, 135.065, 155.89], [5, 42.1, 363.74399999999997, 166.6, 188.61499999999998], [5, 506.042, 592.768, 166.6, 187.42499999999998], [5, 42.942, 192.81799999999998, 198.135, 218.95999999999998], [5, 362.902, 470.678, 233.83499999999998, 254.66], [5, 100.198, 140.614, 272.51, 293.335], [5, 187.766, 266.914, 272.51, 293.335], [5, 423.526, 459.73199999999997, 272.51, 292.145], [5, 591.084, 629.816, 272.51, 292.145], [5, 677.81, 716.542, 271.32, 292.145], [5, 746.012, 785.586, 271.32, 292.145], [5, 62.308, 101.03999999999999, 310.59, 342.125], [5, 171.768, 615.502, 307.615, 329.03499999999997], [5, 640.762, 773.798, 307.615, 326.06], [5, 357.008, 389.00399999999996, 339.15, 359.38], [5, 423.526, 625.606, 337.96, 358.78499999999997]]
2026-08-10 11:35:17,005 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=10.1s
2026-08-10 11:35:17,005 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:35:17,007 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:35:17,007 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:35:17,007 INFO     29 [qwen-vl-text] positions(26): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:35:17,008 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [26]
2026-08-10 11:35:17,172 INFO     29 [qwen-vl-text] page=6, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:35:17,173 INFO     29 [qwen-vl-text] LLM extraction start, text_len=193
2026-08-10 11:35:17,173 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:35:17,173 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 172, \"bbox_end\": 197, \"encounter_dates\": [\"2025-02-26\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间：2025-02-26\n就诊科室：内科门诊\n主诊\n性别：男\n年龄：40岁\n卡号\n医疗证号：\n处方\n015\n地址：PT027气雾剂 2024017-呼吸科\n身份证号：\n诊断：支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n布地奈德福莫特罗吸入粉雾剂BUD/●@1g*60吸2盒\n183.41\n366.82\nSig\n2吸/次,吸入,bid*30天",
    "role": "user"
  }
]
2026-08-10 11:35:19,243 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:35:19,243 INFO     29 [qwen-vl-text] LLM output (len=413):
{
  "encounter_date": "2025-02-26",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "布地奈德福莫特罗吸入粉雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "2吸/次",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 30,
      "quantity": "2盒",
      "notes": null
    }
  ]
}
2026-08-10 11:35:19,243 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-02-26]
2026-08-10 11:35:19,245 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=825853, prompt_len=884
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["门(急)诊处方", "就诊时间：2025-02-26", "就诊科室：内科门诊", "主诊", "性别：男", "年龄：40岁", "卡号", "医疗证号：", "处方", "015", "地址：PT027气雾剂 2024017-呼吸科", "身份证号：", "诊断：支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂BUD/●@1g*60吸2盒", "183.41", "366.82", "Sig", "2吸/次,吸入,bid*30天"]

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
2026-08-10 11:35:26,787 INFO     29 [qwen-vl-text] coord API raw response (len=1334):
[
	{"text": "门(急)诊处方", "bbox": [394, 28, 630, 94]},
	{"text": "就诊时间：2025-02-26", "bbox": [54, 123, 294, 153]},
	{"text": "就诊科室：内科门诊", "bbox": [330, 120, 537, 155]},
	{"text": "主诊", "bbox": [623, 122, 668, 155]},
	{"text": "性别：男", "bbox": [330, 175, 415, 209]},
	{"text": "年龄：40岁", "bbox": [464, 175, 573, 209]},
	{"text": "卡号", "bbox": [621, 175, 667, 209]},
	{"text": "医疗证号：", "bbox": [330, 229, 435, 263]},
	{"text": "处方", "bbox": [619, 231, 666, 264]},
	{"text": "015", "bbox": [900, 229, 939, 258]},
	{"text": "地址：PT027气雾剂 2024017-呼吸科", "bbox": [54, 281, 444, 316]},
	{"text": "身份证号：", "bbox": [618, 281, 721, 316]},
	{"text": "诊断：支气管哮喘", "bbox": [55, 331, 235, 366]},
	{"text": "西药处方", "bbox": [442, 390, 571, 423]},
	{"text": "组号", "bbox": [120, 452, 169, 485]},
	{"text": "项目名称", "bbox": [227, 452, 324, 485]},
	{"text": "规格", "bbox": [514, 451, 557, 483]},
	{"text": "总量", "bbox": [716, 451, 763, 483]},
	{"text": "单价", "bbox": [820, 451, 866, 483]},
	{"text": "金额", "bbox": [902, 450, 948, 483]},
	{"text": "R:", "bbox": [75, 513, 121, 564]},
	{"text": "布地奈德福莫特罗吸入粉雾剂BUD/●@1g*60吸2盒", "bbox": [206, 507, 744, 541]},
	{"text": "183.41", "bbox": [775, 508, 848, 536]},
	{"text": "366.82", "bbox": [857, 508, 932, 536]},
	{"text": "Sig", "bbox": [432, 558, 469, 589]},
	{"text": "2吸/次,吸入,bid*30天", "bbox": [511, 557, 755, 589]}
]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=7.5s
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[394, 28, 630, 94]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间：2025-02-26, bbox=[54, 123, 294, 153]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室：内科门诊, bbox=[330, 120, 537, 155]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[623, 122, 668, 155]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[4]: text=性别：男, bbox=[330, 175, 415, 209]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：40岁, bbox=[464, 175, 573, 209]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[6]: text=卡号, bbox=[621, 175, 667, 209]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[7]: text=医疗证号：, bbox=[330, 229, 435, 263]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[8]: text=处方, bbox=[619, 231, 666, 264]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[9]: text=015, bbox=[900, 229, 939, 258]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[10]: text=地址：PT027气雾剂 2024017-呼吸科, bbox=[54, 281, 444, 316]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[11]: text=身份证号：, bbox=[618, 281, 721, 316]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[12]: text=诊断：支气管哮喘, bbox=[55, 331, 235, 366]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[13]: text=西药处方, bbox=[442, 390, 571, 423]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[14]: text=组号, bbox=[120, 452, 169, 485]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[15]: text=项目名称, bbox=[227, 452, 324, 485]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[16]: text=规格, bbox=[514, 451, 557, 483]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[17]: text=总量, bbox=[716, 451, 763, 483]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[18]: text=单价, bbox=[820, 451, 866, 483]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[19]: text=金额, bbox=[902, 450, 948, 483]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[20]: text=R:, bbox=[75, 513, 121, 564]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[21]: text=布地奈德福莫特罗吸入粉雾剂BUD/●@1g*60吸2盒, bbox=[206, 507, 744, 541]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[22]: text=183.41, bbox=[775, 508, 848, 536]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[23]: text=366.82, bbox=[857, 508, 932, 536]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[432, 558, 469, 589]
2026-08-10 11:35:26,788 INFO     29 [qwen-vl-text] coord item[25]: text=2吸/次,吸入,bid*30天, bbox=[511, 557, 755, 589]
2026-08-10 11:35:26,789 INFO     29 [qwen-vl-text] page=6 — 26/26 coords, api_time=7.5s
2026-08-10 11:35:26,789 INFO     29 [qwen-vl-text] new_positions (26):
[[6, 331.748, 530.46, 16.66, 55.93], [6, 45.467999999999996, 247.548, 73.185, 91.035], [6, 277.86, 452.154, 71.39999999999999, 92.225], [6, 524.566, 562.456, 72.59, 92.225], [6, 277.86, 349.43, 104.125, 124.35499999999999], [6, 390.688, 482.466, 104.125, 124.35499999999999], [6, 522.882, 561.614, 104.125, 124.35499999999999], [6, 277.86, 366.27, 136.255, 156.48499999999999], [6, 521.198, 560.7719999999999, 137.445, 157.07999999999998], [6, 757.8, 790.6379999999999, 136.255, 153.51], [6, 45.467999999999996, 373.848, 167.195, 188.01999999999998], [6, 520.356, 607.082, 167.195, 188.01999999999998], [6, 46.309999999999995, 197.87, 196.945, 217.76999999999998], [6, 372.164, 480.782, 232.04999999999998, 251.685], [6, 101.03999999999999, 142.298, 268.94, 288.575], [6, 191.134, 272.808, 268.94, 288.575], [6, 432.788, 468.99399999999997, 268.34499999999997, 287.385], [6, 602.872, 642.446, 268.34499999999997, 287.385], [6, 690.4399999999999, 729.172, 268.34499999999997, 287.385], [6, 759.4839999999999, 798.216, 267.75, 287.385], [6, 63.15, 101.88199999999999, 305.235, 335.58], [6, 173.452, 626.448, 301.66499999999996, 321.895], [6, 652.55, 714.016, 302.26, 318.91999999999996], [6, 721.5939999999999, 784.744, 302.26, 318.91999999999996], [6, 363.74399999999997, 394.89799999999997, 332.01, 350.455], [6, 430.262, 635.7099999999999, 331.41499999999996, 350.455]]
2026-08-10 11:35:26,789 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=9.8s
2026-08-10 11:35:26,789 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:35:26,795 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:35:26,795 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:35:26,795 INFO     29 [qwen-vl-text] positions(26): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:35:26,795 INFO     29 [qwen-vl-text] page grouping: [7], lines per page: [26]
2026-08-10 11:35:26,953 INFO     29 [qwen-vl-text] page=7, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:35:26,954 INFO     29 [qwen-vl-text] LLM extraction start, text_len=208
2026-08-10 11:35:26,954 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:35:26,954 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 198, \"bbox_end\": 223, \"encounter_dates\": [\"2025-01-24\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-01-24\n就诊科室:内科门诊\n主诊医\n姓名\n性别:男\n年龄:40岁\n卡号:4\n患者类型:GCP支付\n医疗证号:\n处方号:\n地址:PT027气雾剂 2024017-呼吸科\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n布地奈德福莫特罗吸入粉雾剂HIV●@1ug*60吸4盒\n183.41 733.64\nSig\n2吸/次,吸入,bid*60天",
    "role": "user"
  }
]
2026-08-10 11:35:26,956 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:35:26.955+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 23, "failed": 0, "current": {"ea51b5dc94ae11f1bd9827cf206dfa2d": {"id": "ea51b5dc94ae11f1bd9827cf206dfa2d", "doc_id": "ea1b0b1894ae11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786361440167, "task_type": "dataflow", "root_trace_id": "bca8d639df704cd29f0107370613ab01", "root_traceparent": "00-bca8d639df704cd29f0107370613ab01-b8b3c91a32048c1c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:35:29,109 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:35:29,109 INFO     29 [qwen-vl-text] LLM output (len=413):
{
  "encounter_date": "2025-01-24",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "布地奈德福莫特罗吸入粉雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "2吸/次",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 60,
      "quantity": "4盒",
      "notes": null
    }
  ]
}
2026-08-10 11:35:29,109 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-01-24]
2026-08-10 11:35:29,110 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=834734, prompt_len=899
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["门(急)诊处方", "就诊时间:2025-01-24", "就诊科室:内科门诊", "主诊医", "姓名", "性别:男", "年龄:40岁", "卡号:4", "患者类型:GCP支付", "医疗证号:", "处方号:", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂HIV●@1ug*60吸4盒", "183.41 733.64", "Sig", "2吸/次,吸入,bid*60天"]

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
2026-08-10 11:35:37,936 INFO     29 [qwen-vl-text] coord API raw response (len=1347):
[
	{"text": "门(急)诊处方", "bbox": [385, 24, 604, 87]},
	{"text": "就诊时间:2025-01-24", "bbox": [69, 112, 294, 146]},
	{"text": "就诊科室:内科门诊", "bbox": [327, 112, 521, 146]},
	{"text": "主诊医", "bbox": [601, 112, 670, 146]},
	{"text": "姓名", "bbox": [69, 164, 109, 198]},
	{"text": "性别:男", "bbox": [327, 164, 408, 198]},
	{"text": "年龄:40岁", "bbox": [454, 164, 557, 198]},
	{"text": "卡号:4", "bbox": [601, 164, 672, 198]},
	{"text": "患者类型:GCP支付", "bbox": [69, 216, 258, 250]},
	{"text": "医疗证号:", "bbox": [327, 216, 427, 250]},
	{"text": "处方号:", "bbox": [600, 216, 669, 250]},
	{"text": "地址:PT027气雾剂 2024017-呼吸科", "bbox": [69, 267, 437, 301]},
	{"text": "身份证号:", "bbox": [600, 267, 695, 301]},
	{"text": "诊断:支气管哮喘", "bbox": [70, 316, 240, 350]},
	{"text": "西药处方", "bbox": [436, 375, 560, 409]},
	{"text": "组号", "bbox": [132, 436, 178, 470]},
	{"text": "项目名称", "bbox": [232, 436, 325, 470]},
	{"text": "规格", "bbox": [505, 436, 547, 470]},
	{"text": "总量", "bbox": [697, 436, 740, 470]},
	{"text": "单价", "bbox": [795, 436, 838, 470]},
	{"text": "金额", "bbox": [871, 436, 914, 470]},
	{"text": "R:", "bbox": [89, 497, 134, 548]},
	{"text": "布地奈德福莫特罗吸入粉雾剂HIV●@1ug*60吸4盒", "bbox": [213, 493, 724, 527]},
	{"text": "183.41 733.64", "bbox": [753, 495, 902, 523]},
	{"text": "Sig", "bbox": [428, 545, 465, 575]},
	{"text": "2吸/次,吸入,bid*60天", "bbox": [504, 545, 735, 575]}
]
2026-08-10 11:35:37,936 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=8.8s
2026-08-10 11:35:37,936 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[385, 24, 604, 87]
2026-08-10 11:35:37,936 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-01-24, bbox=[69, 112, 294, 146]
2026-08-10 11:35:37,936 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[327, 112, 521, 146]
2026-08-10 11:35:37,936 INFO     29 [qwen-vl-text] coord item[3]: text=主诊医, bbox=[601, 112, 670, 146]
2026-08-10 11:35:37,936 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[69, 164, 109, 198]
2026-08-10 11:35:37,936 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[327, 164, 408, 198]
2026-08-10 11:35:37,936 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:40岁, bbox=[454, 164, 557, 198]
2026-08-10 11:35:37,936 INFO     29 [qwen-vl-text] coord item[7]: text=卡号:4, bbox=[601, 164, 672, 198]
2026-08-10 11:35:37,936 INFO     29 [qwen-vl-text] coord item[8]: text=患者类型:GCP支付, bbox=[69, 216, 258, 250]
2026-08-10 11:35:37,936 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[327, 216, 427, 250]
2026-08-10 11:35:37,936 INFO     29 [qwen-vl-text] coord item[10]: text=处方号:, bbox=[600, 216, 669, 250]
2026-08-10 11:35:37,937 INFO     29 [qwen-vl-text] coord item[11]: text=地址:PT027气雾剂 2024017-呼吸科, bbox=[69, 267, 437, 301]
2026-08-10 11:35:37,937 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[600, 267, 695, 301]
2026-08-10 11:35:37,937 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[70, 316, 240, 350]
2026-08-10 11:35:37,937 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[436, 375, 560, 409]
2026-08-10 11:35:37,937 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[132, 436, 178, 470]
2026-08-10 11:35:37,937 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[232, 436, 325, 470]
2026-08-10 11:35:37,937 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[505, 436, 547, 470]
2026-08-10 11:35:37,937 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[697, 436, 740, 470]
2026-08-10 11:35:37,937 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[795, 436, 838, 470]
2026-08-10 11:35:37,937 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[871, 436, 914, 470]
2026-08-10 11:35:37,937 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[89, 497, 134, 548]
2026-08-10 11:35:37,937 INFO     29 [qwen-vl-text] coord item[22]: text=布地奈德福莫特罗吸入粉雾剂HIV●@1ug*60吸4盒, bbox=[213, 493, 724, 527]
2026-08-10 11:35:37,937 INFO     29 [qwen-vl-text] coord item[23]: text=183.41 733.64, bbox=[753, 495, 902, 523]
2026-08-10 11:35:37,937 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[428, 545, 465, 575]
2026-08-10 11:35:37,937 INFO     29 [qwen-vl-text] coord item[25]: text=2吸/次,吸入,bid*60天, bbox=[504, 545, 735, 575]
2026-08-10 11:35:37,937 INFO     29 [qwen-vl-text] page=7 — 26/26 coords, api_time=8.8s
2026-08-10 11:35:37,937 INFO     29 [qwen-vl-text] new_positions (26):
[[7, 324.17, 508.568, 14.28, 51.765], [7, 58.098, 247.548, 66.64, 86.86999999999999], [7, 275.334, 438.68199999999996, 66.64, 86.86999999999999], [7, 506.042, 564.14, 66.64, 86.86999999999999], [7, 58.098, 91.77799999999999, 97.58, 117.80999999999999], [7, 275.334, 343.536, 97.58, 117.80999999999999], [7, 382.268, 468.99399999999997, 97.58, 117.80999999999999], [7, 506.042, 565.824, 97.58, 117.80999999999999], [7, 58.098, 217.236, 128.51999999999998, 148.75], [7, 275.334, 359.534, 128.51999999999998, 148.75], [7, 505.2, 563.298, 128.51999999999998, 148.75], [7, 58.098, 367.954, 158.86499999999998, 179.095], [7, 505.2, 585.1899999999999, 158.86499999999998, 179.095], [7, 58.94, 202.07999999999998, 188.01999999999998, 208.25], [7, 367.11199999999997, 471.52, 223.125, 243.355], [7, 111.14399999999999, 149.876, 259.42, 279.65], [7, 195.344, 273.65, 259.42, 279.65], [7, 425.21, 460.574, 259.42, 279.65], [7, 586.874, 623.0799999999999, 259.42, 279.65], [7, 669.39, 705.596, 259.42, 279.65], [7, 733.382, 769.588, 259.42, 279.65], [7, 74.938, 112.828, 295.715, 326.06], [7, 179.346, 609.608, 293.335, 313.565], [7, 634.026, 759.4839999999999, 294.525, 311.185], [7, 360.376, 391.53, 324.275, 342.125], [7, 424.368, 618.87, 324.275, 342.125]]
2026-08-10 11:35:37,938 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=11.1s
2026-08-10 11:35:37,938 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:35:37,939 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:35:37,939 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:35:37,939 INFO     29 [qwen-vl-text] positions(31): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:35:37,939 INFO     29 [qwen-vl-text] page grouping: [8], lines per page: [31]
2026-08-10 11:35:38,110 INFO     29 [qwen-vl-text] page=8, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:35:38,111 INFO     29 [qwen-vl-text] LLM extraction start, text_len=234
2026-08-10 11:35:38,111 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:35:38,111 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 224, \"bbox_end\": 254, \"encounter_dates\": [\"2025-01-03\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-01-03\n就诊科室:内科门诊\n主诊\n性别:男\n年龄:40岁\n卡号\n患者类型:GCP支付\n医疗证号:\n处方\n地址:PT027气雾剂 2024017-呼吸科\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n布地奈德福莫特罗吸入粉雾剂(Ⅱ)●●60ug*60吸2盒\n183.41 366.82\nSig\n2吸/次,吸入,bid*30天\n医师:\n医生编号:1326\n配剂人:\n核对人:\n合计:\n收费员:",
    "role": "user"
  }
]
2026-08-10 11:35:40,215 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:35:40,215 INFO     29 [qwen-vl-text] LLM output (len=416):
{
  "encounter_date": "2025-01-03",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "布地奈德福莫特罗吸入粉雾剂(Ⅱ)",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "2吸/次",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 30,
      "quantity": "2盒",
      "notes": null
    }
  ]
}
2026-08-10 11:35:40,215 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-01-03]
2026-08-10 11:35:40,216 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=595064, prompt_len=940
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共31行）
["门(急)诊处方", "就诊时间:2025-01-03", "就诊科室:内科门诊", "主诊", "性别:男", "年龄:40岁", "卡号", "患者类型:GCP支付", "医疗证号:", "处方", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂(Ⅱ)●●60ug*60吸2盒", "183.41 366.82", "Sig", "2吸/次,吸入,bid*30天", "医师:", "医生编号:1326", "配剂人:", "核对人:", "合计:", "收费员:"]

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
2026-08-10 11:35:48,972 INFO     29 [qwen-vl-text] coord API raw response (len=1589):
[
	{"text": "门(急)诊处方", "bbox": [366, 58, 604, 92]},
	{"text": "就诊时间:2025-01-03", "bbox": [18, 105, 263, 123]},
	{"text": "就诊科室:内科门诊", "bbox": [300, 105, 514, 123]},
	{"text": "主诊", "bbox": [603, 105, 648, 123]},
	{"text": "性别:男", "bbox": [300, 132, 390, 150]},
	{"text": "年龄:40岁", "bbox": [440, 132, 553, 150]},
	{"text": "卡号", "bbox": [603, 132, 648, 150]},
	{"text": "患者类型:GCP支付", "bbox": [18, 159, 224, 177]},
	{"text": "医疗证号:", "bbox": [301, 159, 412, 177]},
	{"text": "处方", "bbox": [602, 159, 648, 177]},
	{"text": "地址:PT027气雾剂 2024017-呼吸科", "bbox": [18, 186, 422, 204]},
	{"text": "身份证号:", "bbox": [603, 186, 707, 204]},
	{"text": "诊断:支气管哮喘", "bbox": [18, 212, 204, 230]},
	{"text": "西药处方", "bbox": [421, 244, 557, 262]},
	{"text": "组号", "bbox": [90, 275, 139, 294]},
	{"text": "项目名称", "bbox": [198, 275, 300, 294]},
	{"text": "规格", "bbox": [497, 275, 543, 294]},
	{"text": "总量", "bbox": [707, 275, 755, 294]},
	{"text": "单价", "bbox": [815, 275, 863, 294]},
	{"text": "金额", "bbox": [899, 275, 947, 294]},
	{"text": "R:", "bbox": [44, 308, 93, 338]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(Ⅱ)●●60ug*60吸2盒", "bbox": [179, 305, 738, 324]},
	{"text": "183.41 366.82", "bbox": [768, 307, 934, 323]},
	{"text": "Sig", "bbox": [415, 333, 455, 351]},
	{"text": "2吸/次,吸入,bid*30天", "bbox": [497, 333, 751, 351]},
	{"text": "医师:", "bbox": [43, 627, 98, 646]},
	{"text": "医生编号:1326", "bbox": [347, 627, 510, 646]},
	{"text": "配剂人:", "bbox": [556, 627, 637, 646]},
	{"text": "核对人:", "bbox": [765, 627, 845, 646]},
	{"text": "合计:", "bbox": [60, 884, 113, 902]},
	{"text": "收费员:", "bbox": [270, 884, 350, 902]}
]
2026-08-10 11:35:48,973 INFO     29 [qwen-vl-text] coord API: raw_items=31, valid_items=31, elapsed=8.8s
2026-08-10 11:35:48,973 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[366, 58, 604, 92]
2026-08-10 11:35:48,973 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-01-03, bbox=[18, 105, 263, 123]
2026-08-10 11:35:48,973 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[300, 105, 514, 123]
2026-08-10 11:35:48,973 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[603, 105, 648, 123]
2026-08-10 11:35:48,973 INFO     29 [qwen-vl-text] coord item[4]: text=性别:男, bbox=[300, 132, 390, 150]
2026-08-10 11:35:48,973 INFO     29 [qwen-vl-text] coord item[5]: text=年龄:40岁, bbox=[440, 132, 553, 150]
2026-08-10 11:35:48,973 INFO     29 [qwen-vl-text] coord item[6]: text=卡号, bbox=[603, 132, 648, 150]
2026-08-10 11:35:48,973 INFO     29 [qwen-vl-text] coord item[7]: text=患者类型:GCP支付, bbox=[18, 159, 224, 177]
2026-08-10 11:35:48,973 INFO     29 [qwen-vl-text] coord item[8]: text=医疗证号:, bbox=[301, 159, 412, 177]
2026-08-10 11:35:48,973 INFO     29 [qwen-vl-text] coord item[9]: text=处方, bbox=[602, 159, 648, 177]
2026-08-10 11:35:48,973 INFO     29 [qwen-vl-text] coord item[10]: text=地址:PT027气雾剂 2024017-呼吸科, bbox=[18, 186, 422, 204]
2026-08-10 11:35:48,973 INFO     29 [qwen-vl-text] coord item[11]: text=身份证号:, bbox=[603, 186, 707, 204]
2026-08-10 11:35:48,973 INFO     29 [qwen-vl-text] coord item[12]: text=诊断:支气管哮喘, bbox=[18, 212, 204, 230]
2026-08-10 11:35:48,974 INFO     29 [qwen-vl-text] coord item[13]: text=西药处方, bbox=[421, 244, 557, 262]
2026-08-10 11:35:48,974 INFO     29 [qwen-vl-text] coord item[14]: text=组号, bbox=[90, 275, 139, 294]
2026-08-10 11:35:48,974 INFO     29 [qwen-vl-text] coord item[15]: text=项目名称, bbox=[198, 275, 300, 294]
2026-08-10 11:35:48,974 INFO     29 [qwen-vl-text] coord item[16]: text=规格, bbox=[497, 275, 543, 294]
2026-08-10 11:35:48,974 INFO     29 [qwen-vl-text] coord item[17]: text=总量, bbox=[707, 275, 755, 294]
2026-08-10 11:35:48,974 INFO     29 [qwen-vl-text] coord item[18]: text=单价, bbox=[815, 275, 863, 294]
2026-08-10 11:35:48,974 INFO     29 [qwen-vl-text] coord item[19]: text=金额, bbox=[899, 275, 947, 294]
2026-08-10 11:35:48,974 INFO     29 [qwen-vl-text] coord item[20]: text=R:, bbox=[44, 308, 93, 338]
2026-08-10 11:35:48,974 INFO     29 [qwen-vl-text] coord item[21]: text=布地奈德福莫特罗吸入粉雾剂(Ⅱ)●●60ug*60吸2盒, bbox=[179, 305, 738, 324]
2026-08-10 11:35:48,974 INFO     29 [qwen-vl-text] coord item[22]: text=183.41 366.82, bbox=[768, 307, 934, 323]
2026-08-10 11:35:48,974 INFO     29 [qwen-vl-text] coord item[23]: text=Sig, bbox=[415, 333, 455, 351]
2026-08-10 11:35:48,974 INFO     29 [qwen-vl-text] coord item[24]: text=2吸/次,吸入,bid*30天, bbox=[497, 333, 751, 351]
2026-08-10 11:35:48,974 INFO     29 [qwen-vl-text] coord item[25]: text=医师:, bbox=[43, 627, 98, 646]
2026-08-10 11:35:48,974 INFO     29 [qwen-vl-text] coord item[26]: text=医生编号:1326, bbox=[347, 627, 510, 646]
2026-08-10 11:35:48,974 INFO     29 [qwen-vl-text] coord item[27]: text=配剂人:, bbox=[556, 627, 637, 646]
2026-08-10 11:35:48,974 INFO     29 [qwen-vl-text] coord item[28]: text=核对人:, bbox=[765, 627, 845, 646]
2026-08-10 11:35:48,974 INFO     29 [qwen-vl-text] coord item[29]: text=合计:, bbox=[60, 884, 113, 902]
2026-08-10 11:35:48,974 INFO     29 [qwen-vl-text] coord item[30]: text=收费员:, bbox=[270, 884, 350, 902]
2026-08-10 11:35:48,974 INFO     29 [qwen-vl-text] page=8 — 31/31 coords, api_time=8.8s
2026-08-10 11:35:48,975 INFO     29 [qwen-vl-text] new_positions (31):
[[8, 217.76999999999998, 359.38, 48.836, 77.464], [8, 10.709999999999999, 156.48499999999999, 88.41, 103.566], [8, 178.5, 305.83, 88.41, 103.566], [8, 358.78499999999997, 385.56, 88.41, 103.566], [8, 178.5, 232.04999999999998, 111.14399999999999, 126.3], [8, 261.8, 329.03499999999997, 111.14399999999999, 126.3], [8, 358.78499999999997, 385.56, 111.14399999999999, 126.3], [8, 10.709999999999999, 133.28, 133.878, 149.034], [8, 179.095, 245.14, 133.878, 149.034], [8, 358.19, 385.56, 133.878, 149.034], [8, 10.709999999999999, 251.08999999999997, 156.612, 171.768], [8, 358.78499999999997, 420.66499999999996, 156.612, 171.768], [8, 10.709999999999999, 121.38, 178.504, 193.66], [8, 250.49499999999998, 331.41499999999996, 205.44799999999998, 220.60399999999998], [8, 53.55, 82.705, 231.54999999999998, 247.548], [8, 117.80999999999999, 178.5, 231.54999999999998, 247.548], [8, 295.715, 323.085, 231.54999999999998, 247.548], [8, 420.66499999999996, 449.22499999999997, 231.54999999999998, 247.548], [8, 484.92499999999995, 513.485, 231.54999999999998, 247.548], [8, 534.905, 563.4649999999999, 231.54999999999998, 247.548], [8, 26.18, 55.335, 259.336, 284.596], [8, 106.505, 439.10999999999996, 256.81, 272.808], [8, 456.96, 555.73, 258.49399999999997, 271.966], [8, 246.92499999999998, 270.72499999999997, 280.38599999999997, 295.542], [8, 295.715, 446.84499999999997, 280.38599999999997, 295.542], [8, 25.584999999999997, 58.309999999999995, 527.934, 543.932], [8, 206.465, 303.45, 527.934, 543.932], [8, 330.82, 379.015, 527.934, 543.932], [8, 455.17499999999995, 502.775, 527.934, 543.932], [8, 35.699999999999996, 67.235, 744.328, 759.4839999999999], [8, 160.65, 208.25, 744.328, 759.4839999999999]]
2026-08-10 11:35:48,975 INFO     29 [qwen-vl-text] ═══ DONE ═══ 31 positions, pages=1, time=11.0s
2026-08-10 11:35:48,975 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:35:48,976 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:35:48,976 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:35:48,976 INFO     29 [qwen-vl-text] positions(25): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:35:48,976 INFO     29 [qwen-vl-text] page grouping: [9], lines per page: [25]
2026-08-10 11:35:49,139 INFO     29 [qwen-vl-text] page=9, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:35:49,139 INFO     29 [qwen-vl-text] LLM extraction start, text_len=195
2026-08-10 11:35:49,139 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:35:49,140 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 257, \"bbox_end\": 281, \"encounter_dates\": [\"2024-12-04\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2024-12-04\n就诊科室:内科门诊\n姓名\n性别:男\n年龄:39岁\n卡号\n患者\n医疗证号:\n处方\n地址:PT027气雾剂 2024017-呼吸科\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●(50ug*60吸2盒\n183.41 366.82\nSig\n2吸/次,吸入,bid*30天",
    "role": "user"
  }
]
2026-08-10 11:35:51,311 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:35:51,311 INFO     29 [qwen-vl-text] LLM output (len=417):
{
  "encounter_date": "2024-12-04",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "布地奈德福莫特罗吸入粉雾剂(Ⅱ型)",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "2吸/次",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 30,
      "quantity": "2盒",
      "notes": null
    }
  ]
}
2026-08-10 11:35:51,311 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-12-04]
2026-08-10 11:35:51,314 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=820637, prompt_len=883
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["门(急)诊处方", "就诊时间:2024-12-04", "就诊科室:内科门诊", "姓名", "性别:男", "年龄:39岁", "卡号", "患者", "医疗证号:", "处方", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●(50ug*60吸2盒", "183.41 366.82", "Sig", "2吸/次,吸入,bid*30天"]

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
2026-08-10 11:35:58,742 INFO     29 [qwen-vl-text] coord API raw response (len=1290):
[
	{"text": "门(急)诊处方", "bbox": [387, 18, 617, 80]},
	{"text": "就诊时间:2024-12-04", "bbox": [60, 110, 293, 143]},
	{"text": "就诊科室:内科门诊", "bbox": [328, 107, 530, 141]},
	{"text": "姓名", "bbox": [60, 164, 102, 197]},
	{"text": "性别:男", "bbox": [328, 161, 412, 195]},
	{"text": "年龄:39岁", "bbox": [460, 161, 567, 195]},
	{"text": "卡号", "bbox": [614, 161, 656, 194]},
	{"text": "患者", "bbox": [60, 217, 107, 250]},
	{"text": "医疗证号:", "bbox": [328, 215, 432, 250]},
	{"text": "处方", "bbox": [613, 215, 656, 248]},
	{"text": "地址:PT027气雾剂 2024017-呼吸科", "bbox": [60, 268, 442, 303]},
	{"text": "身份证号:", "bbox": [613, 267, 715, 300]},
	{"text": "诊断:支气管哮喘", "bbox": [60, 320, 236, 354]},
	{"text": "西药处方", "bbox": [441, 379, 570, 413]},
	{"text": "组号", "bbox": [124, 444, 172, 478]},
	{"text": "项目名称", "bbox": [228, 443, 325, 477]},
	{"text": "规格", "bbox": [514, 442, 557, 475]},
	{"text": "总量", "bbox": [714, 441, 760, 474]},
	{"text": "单价", "bbox": [817, 439, 864, 472]},
	{"text": "金额", "bbox": [899, 437, 945, 470]},
	{"text": "R:", "bbox": [80, 508, 126, 561]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●(50ug*60吸2盒", "bbox": [209, 500, 744, 535]},
	{"text": "183.41 366.82", "bbox": [774, 500, 932, 530]},
	{"text": "Sig", "bbox": [434, 554, 471, 586]},
	{"text": "2吸/次,吸入,bid*30天", "bbox": [513, 552, 755, 585]}
]
2026-08-10 11:35:58,742 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=7.4s
2026-08-10 11:35:58,742 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[387, 18, 617, 80]
2026-08-10 11:35:58,742 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2024-12-04, bbox=[60, 110, 293, 143]
2026-08-10 11:35:58,742 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[328, 107, 530, 141]
2026-08-10 11:35:58,742 INFO     29 [qwen-vl-text] coord item[3]: text=姓名, bbox=[60, 164, 102, 197]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] coord item[4]: text=性别:男, bbox=[328, 161, 412, 195]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] coord item[5]: text=年龄:39岁, bbox=[460, 161, 567, 195]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] coord item[6]: text=卡号, bbox=[614, 161, 656, 194]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] coord item[7]: text=患者, bbox=[60, 217, 107, 250]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] coord item[8]: text=医疗证号:, bbox=[328, 215, 432, 250]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] coord item[9]: text=处方, bbox=[613, 215, 656, 248]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] coord item[10]: text=地址:PT027气雾剂 2024017-呼吸科, bbox=[60, 268, 442, 303]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] coord item[11]: text=身份证号:, bbox=[613, 267, 715, 300]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] coord item[12]: text=诊断:支气管哮喘, bbox=[60, 320, 236, 354]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] coord item[13]: text=西药处方, bbox=[441, 379, 570, 413]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] coord item[14]: text=组号, bbox=[124, 444, 172, 478]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] coord item[15]: text=项目名称, bbox=[228, 443, 325, 477]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] coord item[16]: text=规格, bbox=[514, 442, 557, 475]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] coord item[17]: text=总量, bbox=[714, 441, 760, 474]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] coord item[18]: text=单价, bbox=[817, 439, 864, 472]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] coord item[19]: text=金额, bbox=[899, 437, 945, 470]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] coord item[20]: text=R:, bbox=[80, 508, 126, 561]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] coord item[21]: text=布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●(50ug*60吸2盒, bbox=[209, 500, 744, 535]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] coord item[22]: text=183.41 366.82, bbox=[774, 500, 932, 530]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] coord item[23]: text=Sig, bbox=[434, 554, 471, 586]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] coord item[24]: text=2吸/次,吸入,bid*30天, bbox=[513, 552, 755, 585]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] page=9 — 25/25 coords, api_time=7.4s
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] new_positions (25):
[[9, 325.854, 519.514, 10.709999999999999, 47.599999999999994], [9, 50.519999999999996, 246.706, 65.45, 85.085], [9, 276.176, 446.26, 63.665, 83.895], [9, 50.519999999999996, 85.884, 97.58, 117.21499999999999], [9, 276.176, 346.904, 95.795, 116.02499999999999], [9, 387.32, 477.414, 95.795, 116.02499999999999], [9, 516.9879999999999, 552.352, 95.795, 115.42999999999999], [9, 50.519999999999996, 90.094, 129.11499999999998, 148.75], [9, 276.176, 363.74399999999997, 127.925, 148.75], [9, 516.146, 552.352, 127.925, 147.56], [9, 50.519999999999996, 372.164, 159.45999999999998, 180.285], [9, 516.146, 602.03, 158.86499999999998, 178.5], [9, 50.519999999999996, 198.712, 190.39999999999998, 210.63], [9, 371.322, 479.94, 225.505, 245.73499999999999], [9, 104.408, 144.82399999999998, 264.18, 284.40999999999997], [9, 191.976, 273.65, 263.585, 283.815], [9, 432.788, 468.99399999999997, 262.99, 282.625], [9, 601.188, 639.92, 262.395, 282.03], [9, 687.914, 727.4879999999999, 261.205, 280.84], [9, 756.958, 795.6899999999999, 260.015, 279.65], [9, 67.36, 106.092, 302.26, 333.79499999999996], [9, 175.97799999999998, 626.448, 297.5, 318.325], [9, 651.708, 784.744, 297.5, 315.34999999999997], [9, 365.428, 396.582, 329.63, 348.66999999999996], [9, 431.94599999999997, 635.7099999999999, 328.44, 348.075]]
2026-08-10 11:35:58,743 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=9.8s
2026-08-10 11:35:58,743 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:35:58,749 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:35:58,749 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:35:58,749 INFO     29 [qwen-vl-text] positions(30): [[12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:35:58,749 INFO     29 [qwen-vl-text] page grouping: [12], lines per page: [30]
2026-08-10 11:35:58,922 INFO     29 [qwen-vl-text] page=12, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:35:58,923 INFO     29 [qwen-vl-text] LLM extraction start, text_len=259
2026-08-10 11:35:58,923 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:35:58,923 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 692, \"bbox_end\": 721, \"encounter_dates\": [\"2026-01-05\"], \"department\": \"内科门诊（荔湾）\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "广州医科大学附属第三医院\n处方笺\n普通\n诊疗卡\n患者姓名\n年龄：41岁\n费别：南医保\n科室：内科门诊（荔湾）\n日期：2026-01-05 17:17:14\n处方号\n地址：荔湾\n2024017-呼吸科\n联系电话\n身份号码：\n2739\n诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],急性气管支气管炎\nR\nP:\n布地奈德福莫特罗吸入粉雾剂(II) 160ug/4.5ug*60吸\n2盒\n剂量：每次2吸\n（\n1\n30\n盒）\n用法：吸入用药\nbid\n01-05\n处方金额：366.82元\n取药药房：门诊西药房（荔湾）",
    "role": "user"
  }
]
2026-08-10 11:35:58,925 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:35:58.924+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 23, "failed": 0, "current": {"ea51b5dc94ae11f1bd9827cf206dfa2d": {"id": "ea51b5dc94ae11f1bd9827cf206dfa2d", "doc_id": "ea1b0b1894ae11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786361440167, "task_type": "dataflow", "root_trace_id": "bca8d639df704cd29f0107370613ab01", "root_traceparent": "00-bca8d639df704cd29f0107370613ab01-b8b3c91a32048c1c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:36:01,277 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:36:01,277 INFO     29 [qwen-vl-text] LLM output (len=467):
{
  "encounter_date": "2026-01-05",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊（荔湾）",
  "diagnosis": "支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],急性气管支气管炎",
  "items": [
    {
      "drug_generic_name": "布地奈德福莫特罗吸入粉雾剂(II)",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "每次2吸",
      "frequency": "bid",
      "route": "吸入用药",
      "duration_days": null,
      "quantity": "2盒",
      "notes": "160ug/4.5ug*60吸"
    }
  ]
}
2026-08-10 11:36:01,278 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-05]
2026-08-10 11:36:01,282 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=831131, prompt_len=962
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共30行）
["广州医科大学附属第三医院", "处方笺", "普通", "诊疗卡", "患者姓名", "年龄：41岁", "费别：南医保", "科室：内科门诊（荔湾）", "日期：2026-01-05 17:17:14", "处方号", "地址：荔湾", "2024017-呼吸科", "联系电话", "身份号码：", "2739", "诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],急性气管支气管炎", "R", "P:", "布地奈德福莫特罗吸入粉雾剂(II) 160ug/4.5ug*60吸", "2盒", "剂量：每次2吸", "（", "1", "30", "盒）", "用法：吸入用药", "bid", "01-05", "处方金额：366.82元", "取药药房：门诊西药房（荔湾）"]

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
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord API raw response (len=1582):
[
	{"text": "广州医科大学附属第三医院", "bbox": [325, 100, 667, 123]},
	{"text": "处方笺", "bbox": [465, 135, 570, 160]},
	{"text": "普通", "bbox": [812, 168, 850, 182]},
	{"text": "诊疗卡", "bbox": [218, 211, 280, 227]},
	{"text": "患者姓名", "bbox": [218, 237, 284, 251]},
	{"text": "年龄：41岁", "bbox": [545, 236, 634, 250]},
	{"text": "费别：南医保", "bbox": [702, 235, 809, 248]},
	{"text": "科室：内科门诊（荔湾）", "bbox": [217, 260, 408, 274]},
	{"text": "日期：2026-01-05 17:17:14", "bbox": [437, 260, 661, 273]},
	{"text": "处方号", "bbox": [702, 258, 755, 273]},
	{"text": "地址：荔湾", "bbox": [218, 282, 312, 296]},
	{"text": "2024017-呼吸科", "bbox": [438, 281, 565, 295]},
	{"text": "联系电话", "bbox": [702, 282, 755, 296]},
	{"text": "身份号码：", "bbox": [218, 304, 298, 319]},
	{"text": "2739", "bbox": [437, 305, 474, 318]},
	{"text": "诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],急性气管支气管炎", "bbox": [220, 321, 835, 337]},
	{"text": "R", "bbox": [244, 361, 278, 389]},
	{"text": "P:", "bbox": [278, 372, 297, 387]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(II) 160ug/4.5ug*60吸", "bbox": [250, 404, 714, 420]},
	{"text": "2盒", "bbox": [768, 404, 794, 417]},
	{"text": "剂量：每次2吸", "bbox": [328, 430, 438, 444]},
	{"text": "（", "bbox": [463, 428, 474, 444]},
	{"text": "1", "bbox": [485, 424, 497, 438]},
	{"text": "30", "bbox": [484, 438, 502, 450]},
	{"text": "盒）", "bbox": [510, 430, 544, 446]},
	{"text": "用法：吸入用药", "bbox": [581, 431, 697, 445]},
	{"text": "bid", "bbox": [739, 433, 766, 445]},
	{"text": "01-05", "bbox": [784, 433, 838, 447]},
	{"text": "处方金额：366.82元", "bbox": [252, 857, 474, 875]},
	{"text": "取药药房：门诊西药房（荔湾）", "bbox": [625, 858, 917, 875]}
]
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord API: raw_items=30, valid_items=30, elapsed=10.0s
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord item[0]: text=广州医科大学附属第三医院, bbox=[325, 100, 667, 123]
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord item[1]: text=处方笺, bbox=[465, 135, 570, 160]
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord item[2]: text=普通, bbox=[812, 168, 850, 182]
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord item[3]: text=诊疗卡, bbox=[218, 211, 280, 227]
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord item[4]: text=患者姓名, bbox=[218, 237, 284, 251]
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：41岁, bbox=[545, 236, 634, 250]
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord item[6]: text=费别：南医保, bbox=[702, 235, 809, 248]
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord item[7]: text=科室：内科门诊（荔湾）, bbox=[217, 260, 408, 274]
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord item[8]: text=日期：2026-01-05 17:17:14, bbox=[437, 260, 661, 273]
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord item[9]: text=处方号, bbox=[702, 258, 755, 273]
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord item[10]: text=地址：荔湾, bbox=[218, 282, 312, 296]
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord item[11]: text=2024017-呼吸科, bbox=[438, 281, 565, 295]
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord item[12]: text=联系电话, bbox=[702, 282, 755, 296]
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord item[13]: text=身份号码：, bbox=[218, 304, 298, 319]
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord item[14]: text=2739, bbox=[437, 305, 474, 318]
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord item[15]: text=诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],急性气管支气管炎, bbox=[220, 321, 835, 337]
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord item[16]: text=R, bbox=[244, 361, 278, 389]
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord item[17]: text=P:, bbox=[278, 372, 297, 387]
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord item[18]: text=布地奈德福莫特罗吸入粉雾剂(II) 160ug/4.5ug*60吸, bbox=[250, 404, 714, 420]
2026-08-10 11:36:11,297 INFO     29 [qwen-vl-text] coord item[19]: text=2盒, bbox=[768, 404, 794, 417]
2026-08-10 11:36:11,298 INFO     29 [qwen-vl-text] coord item[20]: text=剂量：每次2吸, bbox=[328, 430, 438, 444]
2026-08-10 11:36:11,298 INFO     29 [qwen-vl-text] coord item[21]: text=（, bbox=[463, 428, 474, 444]
2026-08-10 11:36:11,298 INFO     29 [qwen-vl-text] coord item[22]: text=1, bbox=[485, 424, 497, 438]
2026-08-10 11:36:11,298 INFO     29 [qwen-vl-text] coord item[23]: text=30, bbox=[484, 438, 502, 450]
2026-08-10 11:36:11,298 INFO     29 [qwen-vl-text] coord item[24]: text=盒）, bbox=[510, 430, 544, 446]
2026-08-10 11:36:11,298 INFO     29 [qwen-vl-text] coord item[25]: text=用法：吸入用药, bbox=[581, 431, 697, 445]
2026-08-10 11:36:11,298 INFO     29 [qwen-vl-text] coord item[26]: text=bid, bbox=[739, 433, 766, 445]
2026-08-10 11:36:11,298 INFO     29 [qwen-vl-text] coord item[27]: text=01-05, bbox=[784, 433, 838, 447]
2026-08-10 11:36:11,298 INFO     29 [qwen-vl-text] coord item[28]: text=处方金额：366.82元, bbox=[252, 857, 474, 875]
2026-08-10 11:36:11,298 INFO     29 [qwen-vl-text] coord item[29]: text=取药药房：门诊西药房（荔湾）, bbox=[625, 858, 917, 875]
2026-08-10 11:36:11,298 INFO     29 [qwen-vl-text] page=12 — 30/30 coords, api_time=10.0s
2026-08-10 11:36:11,298 INFO     29 [qwen-vl-text] new_positions (30):
[[12, 193.375, 396.865, 84.2, 103.566], [12, 276.675, 339.15, 113.67, 134.72], [12, 483.14, 505.75, 141.456, 153.244], [12, 129.71, 166.6, 177.662, 191.134], [12, 129.71, 168.98, 199.554, 211.34199999999998], [12, 324.275, 377.22999999999996, 198.712, 210.5], [12, 417.69, 481.35499999999996, 197.87, 208.816], [12, 129.11499999999998, 242.76, 218.92, 230.708], [12, 260.015, 393.29499999999996, 218.92, 229.86599999999999], [12, 417.69, 449.22499999999997, 217.236, 229.86599999999999], [12, 129.71, 185.64, 237.444, 249.232], [12, 260.61, 336.175, 236.602, 248.39], [12, 417.69, 449.22499999999997, 237.444, 249.232], [12, 129.71, 177.31, 255.968, 268.598], [12, 260.015, 282.03, 256.81, 267.756], [12, 130.9, 496.825, 270.282, 283.75399999999996], [12, 145.18, 165.41, 303.962, 327.538], [12, 165.41, 176.715, 313.224, 325.854], [12, 148.75, 424.83, 340.168, 353.64], [12, 456.96, 472.43, 340.168, 351.114], [12, 195.16, 260.61, 362.06, 373.848], [12, 275.485, 282.03, 360.376, 373.848], [12, 288.575, 295.715, 357.008, 368.796], [12, 287.97999999999996, 298.69, 368.796, 378.9], [12, 303.45, 323.68, 362.06, 375.532], [12, 345.695, 414.715, 362.902, 374.69], [12, 439.705, 455.77, 364.586, 374.69], [12, 466.47999999999996, 498.60999999999996, 364.586, 376.37399999999997], [12, 149.94, 282.03, 721.5939999999999, 736.75], [12, 371.875, 545.615, 722.4359999999999, 736.75]]
2026-08-10 11:36:11,298 INFO     29 [qwen-vl-text] ═══ DONE ═══ 30 positions, pages=1, time=12.6s
2026-08-10 11:36:11,308 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 11:36:11,308 INFO     29 [Trace] task=ea51b5dc | doc=LZK 哮喘 广三(2).pdf | Extractor:Prescription | outputs={"chunks": "7 items, types={'PrescriptionRecord': 7}", "html": "", "json": "1039 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(2).pdf", "output_format": "chunks", "chunks_Clinical": "5 items, types={'OutpatientRecord': 5}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 5, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-10 11:36:11,308 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 11:36:11,318 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:36:11,318 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:36:12,213 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:36:12,227 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 11:36:12,228 INFO     29 [Trace] task=ea51b5dc | doc=LZK 哮喘 广三(2).pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "1039 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(2).pdf", "output_format": "chunks", "chunks_Clinical": "5 items, types={'OutpatientRecord': 5}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 5, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-10 11:36:12,228 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 11:36:12,241 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:36:12,242 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:36:12,792 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:36:12,797 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 11:36:12,798 INFO     29 [Trace] task=ea51b5dc | doc=LZK 哮喘 广三(2).pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "1039 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(2).pdf", "output_format": "chunks", "chunks_Clinical": "5 items, types={'OutpatientRecord': 5}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 5, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-10 11:36:12,798 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 11:36:12,806 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:36:12,807 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:36:12,807 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 11:36:12,807 INFO     29 [qwen-vl-text] positions(197): [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:36:12,808 INFO     29 [qwen-vl-text] page grouping: [10], lines per page: [197]
2026-08-10 11:36:13,018 INFO     29 [qwen-vl-text] page=10, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:36:13,019 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1345
2026-08-10 11:36:13,020 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:36:13,020 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 282, \"bbox_end\": 478, \"encounter_dates\": [\"2022-06-08\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "激发试验检查报告\n姓名：\n测试号：\n门诊/住院号：\n000\n年龄：\n出生日期：\n19\n性别：\n男\n身高：\n170\n病区：\n内科门诊\n体重：\n81 kg\n机器编号：\n床号：\n电话：\nPred\nA1\nA1/Pd\nNS\nP1 chg%1\nP2 chg%2\nP3 chg%3\nFVC\n[L]\n4.84\n4.69\n97.1\n4.29\n4.22\n-10.1\n3.64\n-22.5\n4.01\n-14.6\nPEV 1\n[L]\n4.01\n3.05\n76.2\n2.72\n2.69\n-11.8\n2.24\n-26.5\n2.44\n-20.0\nPEV 1 % PVC\n[%]\n83.32\n65.02\n78.0\n63.54\n63.83\n-1.82\n61.73\n-5.06\n60.92\n-6.30\nPEV 1 % VC MAX\n[%]\n80.55\n64.94\n80.6\n62.34\n63.83\n-1.70\n61.73\n-4.94\n60.92\n-6.18\nVC MAX\n[L]\n5.05\n4.70\n93.1\n4.37\n4.22\n-10.2\n3.64\n-22.6\n4.01\n-14.7\nPEP\n[L/s]\n9.37\n9.95\n106.2\n9.06\n7.81\n-21.5\n6.73\n-32.3\n8.22\n-17.4\nMMEF 75/25\n[L/s]\n4.52\n1.54\n34.1\n1.33\n1.34\n-12.9\n1.14\n-25.8\n1.23\n-20.0\nMEF 50\n[L/s]\n5.17\n1.97\n38.1\n1.66\n1.71\n-13.4\n1.34\n-31.8\n1.42\n-28.0\nMEF 25\n[L/s]\n2.29\n0.58\n25.5\n0.52\n0.53\n-9.87\n0.50\n-14.6\n0.49\n-15.7\nPET\n[s]\n6.72\n6.87\n6.93\n3.16\n6.75\n0.57\n6.74\n0.38\nV backextrapolation ex\n[L]\n0.13\n0.09\n0.10\n-20.0\n0.08\n-41.6\n0.08\n-38.5\nPIF\n[L/s]\n8.04\n7.96\n7.58\n-5.76\n6.16\n-23.3\n7.78\n-3.20\nFIF 50\n[L/s]\n7.99\n7.86\n7.16\n-10.3\n5.36\n-32.9\n7.08\n-11.3\nMVV\n[L/min]\n141.88\nBF MVV\n[1/min]\nCumulated dose\n0.072 0.078\n0.312\n2 Puf\nF/V ex\nF/V in\nVol [L]\nVol%VCmax\nVCmax\nTime [s]\nPD[-20] FEV 1: 0.2117 mg Cumulated\nPD[-20] PEF: < 0.078 mg Cumulated\nPD[] FEV1%I: could not be calculated!\n意见：\n2022/6/08 10:23:56上午\n1.轻度阻塞性通气功能障碍。\n2.支气管激发试验阳性(累计吸入乙酰甲胆碱0.312mg，FEV1下降大于20%，PD20=0.2117mg，气道高反应性(AHR)为中度\n通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后FEV1恢复至预计值80%。",
    "role": "user"
  }
]
2026-08-10 11:36:22,065 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:36:22,065 INFO     29 [qwen-vl-text] LLM output (len=1562):
{
  "exam_date": "2022-06-08",
  "report_date": "2022-06-08",
  "exam_name": "激发试验检查",
  "exam_category": "other",
  "body_part": "肺功能",
  "patient_name": null,
  "patient_gender": "男",
  "department": "内科门诊",
  "bed_number": null,
  "findings": "Pred A1 A1/Pd NS P1 chg%1 P2 chg%2 P3 chg%3\nFVC [L] 4.84 4.69 97.1 4.29 4.22 -10.1 3.64 -22.5 4.01 -14.6\nPEV 1 [L] 4.01 3.05 76.2 2.72 2.69 -11.8 2.24 -26.5 2.44 -20.0\nPEV 1 % PVC [%] 83.32 65.02 78.0 63.54 63.83 -1.82 61.73 -5.06 60.92 -6.30\nPEV 1 % VC MAX [%] 80.55 64.94 80.6 62.34 63.83 -1.70 61.73 -4.94 60.92 -6.18\nVC MAX [L] 5.05 4.70 93.1 4.37 4.22 -10.2 3.64 -22.6 4.01 -14.7\nPEP [L/s] 9.37 9.95 106.2 9.06 7.81 -21.5 6.73 -32.3 8.22 -17.4\nMMEF 75/25 [L/s] 4.52 1.54 34.1 1.33 1.34 -12.9 1.14 -25.8 1.23 -20.0\nMEF 50 [L/s] 5.17 1.97 38.1 1.66 1.71 -13.4 1.34 -31.8 1.42 -28.0\nMEF 25 [L/s] 2.29 0.58 25.5 0.52 0.53 -9.87 0.50 -14.6 0.49 -15.7\nPET [s] 6.72 6.87 6.93 3.16 6.75 0.57 6.74 0.38\nV backextrapolation ex [L] 0.13 0.09 0.10 -20.0 0.08 -41.6 0.08 -38.5\nPIF [L/s] 8.04 7.96 7.58 -5.76 6.16 -23.3 7.78 -3.20\nFIF 50 [L/s] 7.99 7.86 7.16 -10.3 5.36 -32.9 7.08 -11.3\nMVV [L/min] 141.88\nBF MVV [1/min]\nCumulated dose 0.072 0.078 0.312 2 Puf\nF/V ex F/V in Vol [L] Vol%VCmax VCmax Time [s]\nPD[-20] FEV 1: 0.2117 mg Cumulated\nPD[-20] PEF: < 0.078 mg Cumulated\nPD[] FEV1%I: could not be calculated!",
  "conclusion": "1.轻度阻塞性通气功能障碍。\n2.支气管激发试验阳性(累计吸入乙酰甲胆碱0.312mg，FEV1下降大于20%，PD20=0.2117mg，气道高反应性(AHR)为中度\n通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后FEV1恢复至预计值80%。",
  "physician": null,
  "reviewer": null
}
2026-08-10 11:36:22,067 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1393927, prompt_len=2550
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共197行）
["激发试验检查报告", "姓名：", "测试号：", "门诊/住院号：", "000", "年龄：", "出生日期：", "19", "性别：", "男", "身高：", "170", "病区：", "内科门诊", "体重：", "81 kg", "机器编号：", "床号：", "电话：", "Pred", "A1", "A1/Pd", "NS", "P1 chg%1", "P2 chg%2", "P3 chg%3", "FVC", "[L]", "4.84", "4.69", "97.1", "4.29", "4.22", "-10.1", "3.64", "-22.5", "4.01", "-14.6", "PEV 1", "[L]", "4.01", "3.05", "76.2", "2.72", "2.69", "-11.8", "2.24", "-26.5", "2.44", "-20.0", "PEV 1 % PVC", "[%]", "83.32", "65.02", "78.0", "63.54", "63.83", "-1.82", "61.73", "-5.06", "60.92", "-6.30", "PEV 1 % VC MAX", "[%]", "80.55", "64.94", "80.6", "62.34", "63.83", "-1.70", "61.73", "-4.94", "60.92", "-6.18", "VC MAX", "[L]", "5.05", "4.70", "93.1", "4.37", "4.22", "-10.2", "3.64", "-22.6", "4.01", "-14.7", "PEP", "[L/s]", "9.37", "9.95", "106.2", "9.06", "7.81", "-21.5", "6.73", "-32.3", "8.22", "-17.4", "MMEF 75/25", "[L/s]", "4.52", "1.54", "34.1", "1.33", "1.34", "-12.9", "1.14", "-25.8", "1.23", "-20.0", "MEF 50", "[L/s]", "5.17", "1.97", "38.1", "1.66", "1.71", "-13.4", "1.34", "-31.8", "1.42", "-28.0", "MEF 25", "[L/s]", "2.29", "0.58", "25.5", "0.52", "0.53", "-9.87", "0.50", "-14.6", "0.49", "-15.7", "PET", "[s]", "6.72", "6.87", "6.93", "3.16", "6.75", "0.57", "6.74", "0.38", "V backextrapolation ex", "[L]", "0.13", "0.09", "0.10", "-20.0", "0.08", "-41.6", "0.08", "-38.5", "PIF", "[L/s]", "8.04", "7.96", "7.58", "-5.76", "6.16", "-23.3", "7.78", "-3.20", "FIF 50", "[L/s]", "7.99", "7.86", "7.16", "-10.3", "5.36", "-32.9", "7.08", "-11.3", "MVV", "[L/min]", "141.88", "BF MVV", "[1/min]", "Cumulated dose", "0.072 0.078", "0.312", "2 Puf", "F/V ex", "F/V in", "Vol [L]", "Vol%VCmax", "VCmax", "Time [s]", "PD[-20] FEV 1: 0.2117 mg Cumulated", "PD[-20] PEF: < 0.078 mg Cumulated", "PD[] FEV1%I: could not be calculated!", "意见：", "2022/6/08 10:23:56上午", "1.轻度阻塞性通气功能障碍。", "2.支气管激发试验阳性(累计吸入乙酰甲胆碱0.312mg，FEV1下降大于20%，PD20=0.2117mg，气道高反应性(AHR)为中度", "通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后FEV1恢复至预计值80%。"]

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
2026-08-10 11:37:26,510 INFO     29 [qwen-vl-text] coord API raw response (len=13341):
[
	{"text": "激发试验检查报告", "bbox": [427, 37, 620, 56]},
	{"text": "姓名：", "bbox": [215, 75, 260, 88], "label": "姓名："},
	{"text": "测试号：", "bbox": [215, 89, 275, 102], "label": "测试号："},
	{"text": "门诊/住院号：", "bbox": [542, 74, 644, 87], "label": "门诊/住院号："},
	{"text": "000", "bbox": [699, 75, 721, 87], "label": "000"},
	{"text": "年龄：", "bbox": [215, 103, 260, 116], "label": "年龄："},
	{"text": "出生日期：", "bbox": [542, 88, 618, 101], "label": "出生日期："},
	{"text": "19", "bbox": [700, 90, 718, 101], "label": "19"},
	{"text": "性别：", "bbox": [215, 117, 260, 130], "label": "性别："},
	{"text": "身高：", "bbox": [542, 102, 584, 115], "label": "身高："},
	{"text": "170", "bbox": [700, 103, 718, 114], "label": "170"},
	{"text": "病区：", "bbox": [215, 131, 260, 144], "label": "病区："},
	{"text": "内科门诊", "bbox": [375, 131, 445, 144], "label": "内科门诊"},
	{"text": "体重：", "bbox": [542, 116, 584, 129], "label": "体重："},
	{"text": "81 kg", "bbox": [699, 116, 741, 128], "label": "81 kg"},
	{"text": "机器编号：", "bbox": [215, 145, 294, 158], "label": "机器编号："},
	{"text": "床号：", "bbox": [542, 130, 584, 143], "label": "床号："},
	{"text": "电话：", "bbox": [542, 144, 584, 157], "label": "电话："},
	{"text": "Pred", "bbox": [332, 175, 368, 188], "label": "Pred"},
	{"text": "A1", "bbox": [402, 175, 418, 188], "label": "A1"},
	{"text": "A1/Pd", "bbox": [434, 175, 474, 188], "label": "A1/Pd"},
	{"text": "NS", "bbox": [508, 175, 525, 188], "label": "NS"},
	{"text": "P1 chg%1", "bbox": [558, 175, 628, 188], "label": "P1 chg%1"},
	{"text": "P2 chg%2", "bbox": [664, 175, 734, 188], "label": "P2 chg%2"},
	{"text": "P3 chg%3", "bbox": [769, 175, 838, 188], "label": "P3 chg%3"},
	{"text": "FVC", "bbox": [56, 203, 84, 215], "label": "FVC"},
	{"text": "[L]", "bbox": [263, 203, 287, 216], "label": "[L]"},
	{"text": "4.84", "bbox": [334, 203, 368, 215], "label": "4.84"},
	{"text": "4.69", "bbox": [398, 203, 424, 215], "label": "4.69"},
	{"text": "97.1", "bbox": [438, 203, 472, 215], "label": "97.1"},
	{"text": "4.29", "bbox": [494, 203, 524, 215], "label": "4.29"},
	{"text": "4.22", "bbox": [542, 203, 570, 215], "label": "4.22"},
	{"text": "-10.1", "bbox": [594, 203, 628, 215], "label": "-10.1"},
	{"text": "3.64", "bbox": [648, 203, 676, 215], "label": "3.64"},
	{"text": "-22.5", "bbox": [700, 203, 734, 215], "label": "-22.5"},
	{"text": "4.01", "bbox": [754, 203, 782, 215], "label": "4.01"},
	{"text": "-14.6", "bbox": [806, 203, 838, 215], "label": "-14.6"},
	{"text": "PEV 1", "bbox": [56, 217, 99, 229], "label": "PEV 1"},
	{"text": "[L]", "bbox": [263, 217, 287, 230], "label": "[L]"},
	{"text": "4.01", "bbox": [334, 217, 368, 229], "label": "4.01"},
	{"text": "3.05", "bbox": [398, 217, 424, 229], "label": "3.05"},
	{"text": "76.2", "bbox": [438, 217, 472, 229], "label": "76.2"},
	{"text": "2.72", "bbox": [494, 217, 524, 229], "label": "2.72"},
	{"text": "2.69", "bbox": [542, 217, 570, 229], "label": "2.69"},
	{"text": "-11.8", "bbox": [594, 217, 628, 229], "label": "-11.8"},
	{"text": "2.24", "bbox": [648, 217, 676, 229], "label": "2.24"},
	{"text": "-26.5", "bbox": [700, 217, 734, 229], "label": "-26.5"},
	{"text": "2.44", "bbox": [754, 217, 782, 229], "label": "2.44"},
	{"text": "-20.0", "bbox": [806, 217, 838, 229], "label": "-20.0"},
	{"text": "PEV 1 % PVC", "bbox": [56, 231, 152, 243], "label": "PEV 1 % PVC"},
	{"text": "[%]", "bbox": [263, 231, 287, 244], "label": "[%]"},
	{"text": "83.32", "bbox": [324, 231, 368, 243], "label": "83.32"},
	{"text": "65.02", "bbox": [388, 231, 424, 243], "label": "65.02"},
	{"text": "78.0", "bbox": [438, 231, 472, 243], "label": "78.0"},
	{"text": "63.54", "bbox": [484, 231, 524, 243], "label": "63.54"},
	{"text": "63.83", "bbox": [532, 231, 570, 243], "label": "63.83"},
	{"text": "-1.82", "bbox": [594, 231, 628, 243], "label": "-1.82"},
	{"text": "61.73", "bbox": [648, 231, 676, 243], "label": "61.73"},
	{"text": "-5.06", "bbox": [700, 231, 734, 243], "label": "-5.06"},
	{"text": "60.92", "bbox": [754, 231, 782, 243], "label": "60.92"},
	{"text": "-6.30", "bbox": [806, 231, 838, 243], "label": "-6.30"},
	{"text": "PEV 1 % VC MAX", "bbox": [56, 245, 177, 257], "label": "PEV 1 % VC MAX"},
	{"text": "[%]", "bbox": [263, 245, 287, 258], "label": "[%]"},
	{"text": "80.55", "bbox": [324, 245, 368, 257], "label": "80.55"},
	{"text": "64.94", "bbox": [388, 245, 424, 257], "label": "64.94"},
	{"text": "80.6", "bbox": [438, 245, 472, 257], "label": "80.6"},
	{"text": "62.34", "bbox": [484, 245, 524, 257], "label": "62.34"},
	{"text": "63.83", "bbox": [532, 245, 570, 257], "label": "63.83"},
	{"text": "-1.70", "bbox": [594, 245, 628, 257], "label": "-1.70"},
	{"text": "61.73", "bbox": [648, 245, 676, 257], "label": "61.73"},
	{"text": "-4.94", "bbox": [700, 245, 734, 257], "label": "-4.94"},
	{"text": "60.92", "bbox": [754, 245, 782, 257], "label": "60.92"},
	{"text": "-6.18", "bbox": [806, 245, 838, 257], "label": "-6.18"},
	{"text": "VC MAX", "bbox": [56, 259, 109, 271], "label": "VC MAX"},
	{"text": "[L]", "bbox": [263, 259, 287, 272], "label": "[L]"},
	{"text": "5.05", "bbox": [334, 259, 368, 271], "label": "5.05"},
	{"text": "4.70", "bbox": [398, 259, 424, 271], "label": "4.70"},
	{"text": "93.1", "bbox": [438, 259, 472, 271], "label": "93.1"},
	{"text": "4.37", "bbox": [494, 259, 524, 271], "label": "4.37"},
	{"text": "4.22", "bbox": [542, 259, 570, 271], "label": "4.22"},
	{"text": "-10.2", "bbox": [594, 259, 628, 271], "label": "-10.2"},
	{"text": "3.64", "bbox": [648, 259, 676, 271], "label": "3.64"},
	{"text": "-22.6", "bbox": [700, 259, 734, 271], "label": "-22.6"},
	{"text": "4.01", "bbox": [754, 259, 782, 271], "label": "4.01"},
	{"text": "-14.7", "bbox": [806, 259, 838, 271], "label": "-14.7"},
	{"text": "PEP", "bbox": [56, 273, 83, 285], "label": "PEP"},
	{"text": "[L/s]", "bbox": [246, 273, 287, 286], "label": "[L/s]"},
	{"text": "9.37", "bbox": [334, 273, 368, 285], "label": "9.37"},
	{"text": "9.95", "bbox": [398, 273, 424, 285], "label": "9.95"},
	{"text": "106.2", "bbox": [430, 273, 472, 285], "label": "106.2"},
	{"text": "9.06", "bbox": [494, 273, 524, 285], "label": "9.06"},
	{"text": "7.81", "bbox": [542, 273, 570, 285], "label": "7.81"},
	{"text": "-21.5", "bbox": [594, 273, 628, 285], "label": "-21.5"},
	{"text": "6.73", "bbox": [648, 273, 676, 285], "label": "6.73"},
	{"text": "-32.3", "bbox": [700, 273, 734, 285], "label": "-32.3"},
	{"text": "8.22", "bbox": [754, 273, 782, 285], "label": "8.22"},
	{"text": "-17.4", "bbox": [806, 273, 838, 285], "label": "-17.4"},
	{"text": "MMEF 75/25", "bbox": [56, 287, 143, 300], "label": "MMEF 75/25"},
	{"text": "[L/s]", "bbox": [246, 287, 287, 300], "label": "[L/s]"},
	{"text": "4.52", "bbox": [334, 287, 368, 300], "label": "4.52"},
	{"text": "1.54", "bbox": [398, 287, 424, 300], "label": "1.54"},
	{"text": "34.1", "bbox": [438, 287, 472, 300], "label": "34.1"},
	{"text": "1.33", "bbox": [494, 287, 524, 300], "label": "1.33"},
	{"text": "1.34", "bbox": [542, 287, 570, 300], "label": "1.34"},
	{"text": "-12.9", "bbox": [594, 287, 628, 300], "label": "-12.9"},
	{"text": "1.14", "bbox": [648, 287, 676, 300], "label": "1.14"},
	{"text": "-25.8", "bbox": [700, 287, 734, 300], "label": "-25.8"},
	{"text": "1.23", "bbox": [754, 287, 782, 300], "label": "1.23"},
	{"text": "-20.0", "bbox": [806, 287, 838, 300], "label": "-20.0"},
	{"text": "MEF 50", "bbox": [56, 301, 109, 314], "label": "MEF 50"},
	{"text": "[L/s]", "bbox": [246, 301, 287, 314], "label": "[L/s]"},
	{"text": "5.17", "bbox": [334, 301, 368, 314], "label": "5.17"},
	{"text": "1.97", "bbox": [398, 301, 424, 314], "label": "1.97"},
	{"text": "38.1", "bbox": [438, 301, 472, 314], "label": "38.1"},
	{"text": "1.66", "bbox": [494, 301, 524, 314], "label": "1.66"},
	{"text": "1.71", "bbox": [542, 301, 570, 314], "label": "1.71"},
	{"text": "-13.4", "bbox": [594, 301, 628, 314], "label": "-13.4"},
	{"text": "1.34", "bbox": [648, 301, 676, 314], "label": "1.34"},
	{"text": "-31.8", "bbox": [700, 301, 734, 314], "label": "-31.8"},
	{"text": "1.42", "bbox": [754, 301, 782, 314], "label": "1.42"},
	{"text": "-28.0", "bbox": [806, 301, 838, 314], "label": "-28.0"},
	{"text": "MEF 25", "bbox": [56, 315, 109, 328], "label": "MEF 25"},
	{"text": "[L/s]", "bbox": [246, 315, 287, 328], "label": "[L/s]"},
	{"text": "2.29", "bbox": [334, 315, 368, 328], "label": "2.29"},
	{"text": "0.58", "bbox": [398, 315, 424, 328], "label": "0.58"},
	{"text": "25.5", "bbox": [438, 315, 472, 328], "label": "25.5"},
	{"text": "0.52", "bbox": [494, 315, 524, 328], "label": "0.52"},
	{"text": "0.53", "bbox": [542, 315, 570, 328], "label": "0.53"},
	{"text": "-9.87", "bbox": [594, 315, 628, 328], "label": "-9.87"},
	{"text": "0.50", "bbox": [648, 315, 676, 328], "label": "0.50"},
	{"text": "-14.6", "bbox": [700, 315, 734, 328], "label": "-14.6"},
	{"text": "0.49", "bbox": [754, 315, 782, 328], "label": "0.49"},
	{"text": "-15.7", "bbox": [806, 315, 838, 328], "label": "-15.7"},
	{"text": "PET", "bbox": [56, 330, 83, 342], "label": "PET"},
	{"text": "[s]", "bbox": [263, 330, 287, 343], "label": "[s]"},
	{"text": "6.72", "bbox": [388, 330, 420, 342], "label": "6.72"},
	{"text": "6.87", "bbox": [490, 330, 522, 342], "label": "6.87"},
	{"text": "6.93", "bbox": [542, 330, 574, 342], "label": "6.93"},
	{"text": "3.16", "bbox": [594, 330, 626, 342], "label": "3.16"},
	{"text": "6.75", "bbox": [648, 330, 680, 342], "label": "6.75"},
	{"text": "0.57", "bbox": [700, 330, 732, 342], "label": "0.57"},
	{"text": "6.74", "bbox": [754, 330, 786, 342], "label": "6.74"},
	{"text": "0.38", "bbox": [806, 330, 838, 342], "label": "0.38"},
	{"text": "V backextrapolation ex", "bbox": [56, 344, 234, 357], "label": "V backextrapolation ex"},
	{"text": "[L]", "bbox": [263, 344, 287, 357], "label": "[L]"},
	{"text": "0.13", "bbox": [388, 344, 420, 357], "label": "0.13"},
	{"text": "0.09", "bbox": [490, 344, 522, 357], "label": "0.09"},
	{"text": "0.10", "bbox": [542, 344, 574, 357], "label": "0.10"},
	{"text": "-20.0", "bbox": [594, 344, 626, 357], "label": "-20.0"},
	{"text": "0.08", "bbox": [648, 344, 680, 357], "label": "0.08"},
	{"text": "-41.6", "bbox": [700, 344, 732, 357], "label": "-41.6"},
	{"text": "0.08", "bbox": [754, 344, 786, 357], "label": "0.08"},
	{"text": "-38.5", "bbox": [806, 344, 838, 357], "label": "-38.5"},
	{"text": "PIF", "bbox": [56, 358, 83, 371], "label": "PIF"},
	{"text": "[L/s]", "bbox": [246, 358, 287, 371], "label": "[L/s]"},
	{"text": "8.04", "bbox": [388, 358, 420, 371], "label": "8.04"},
	{"text": "7.96", "bbox": [490, 358, 522, 371], "label": "7.96"},
	{"text": "7.58", "bbox": [542, 358, 574, 371], "label": "7.58"},
	{"text": "-5.76", "bbox": [594, 358, 626, 371], "label": "-5.76"},
	{"text": "6.16", "bbox": [648, 358, 680, 371], "label": "6.16"},
	{"text": "-23.3", "bbox": [700, 358, 732, 371], "label": "-23.3"},
	{"text": "7.78", "bbox": [754, 358, 786, 371], "label": "7.78"},
	{"text": "-3.20", "bbox": [806, 358, 838, 371], "label": "-3.20"},
	{"text": "FIF 50", "bbox": [56, 372, 109, 385], "label": "FIF 50"},
	{"text": "[L/s]", "bbox": [246, 372, 287, 385], "label": "[L/s]"},
	{"text": "7.99", "bbox": [388, 372, 420, 385], "label": "7.99"},
	{"text": "7.86", "bbox": [490, 372, 522, 385], "label": "7.86"},
	{"text": "7.16", "bbox": [542, 372, 574, 385], "label": "7.16"},
	{"text": "-10.3", "bbox": [594, 372, 626, 385], "label": "-10.3"},
	{"text": "5.36", "bbox": [648, 372, 680, 385], "label": "5.36"},
	{"text": "-32.9", "bbox": [700, 372, 732, 385], "label": "-32.9"},
	{"text": "7.08", "bbox": [754, 372, 786, 385], "label": "7.08"},
	{"text": "-11.3", "bbox": [806, 372, 838, 385], "label": "-11.3"},
	{"text": "MVV", "bbox": [56, 386, 83, 399], "label": "MVV"},
	{"text": "[L/min]", "bbox": [229, 386, 287, 399], "label": "[L/min]"},
	{"text": "141.88", "bbox": [317, 386, 368, 399], "label": "141.88"},
	{"text": "BF MVV", "bbox": [56, 400, 109, 413], "label": "BF MVV"},
	{"text": "[1/min]", "bbox": [229, 400, 287, 413], "label": "[1/min]"},
	{"text": "Cumulated dose", "bbox": [56, 428, 179, 441], "label": "Cumulated dose"},
	{"text": "0.072 0.078", "bbox": [479, 428, 574, 441], "label": "0.072 0.078"},
	{"text": "0.312", "bbox": [637, 428, 680, 441], "label": "0.312"},
	{"text": "2 Puf", "bbox": [740, 428, 786, 441], "label": "2 Puf"},
	{"text": "F/V ex", "bbox": [349, 472, 386, 484], "label": "F/V ex"},
	{"text": "F/V in", "bbox": [349, 719, 383, 730], "label": "F/V in"},
	{"text": "Vol [L]", "bbox": [644, 507, 680, 520], "label": "Vol [L]"},
	{"text": "Vol%VCmax", "bbox": [590, 530, 658, 540], "label": "Vol%VCmax"},
	{"text": "VCmax", "bbox": [657, 545, 697, 555], "label": "VCmax"},
	{"text": "Time [s]", "bbox": [775, 658, 819, 669], "label": "Time [s]"},
	{"text": "PD[-20] FEV 1: 0.2117 mg Cumulated", "bbox": [96, 750, 389, 763], "label": "PD[-20] FEV 1: 0.2117 mg Cumulated"},
	{"text": "PD[-20] PEF: < 0.078 mg Cumulated", "bbox": [96, 762, 381, 775], "label": "PD[-20] PEF: < 0.078 mg Cumulated"},
	{"text": "PD[] FEV1%I: could not be calculated!", "bbox": [96, 786, 414, 799], "label": "PD[] FEV1%I: could not be calculated!"},
	{"text": "意见：", "bbox": [86, 808, 134, 822], "label": "意见："},
	{"text": "2022/6/08 10:23:56上午", "bbox": [86, 830, 273, 843], "label": "2022/6/08 10:23:56上午"},
	{"text": "1.轻度阻塞性通气功能障碍。", "bbox": [86, 842, 314, 855], "label": "1.轻度阻塞性通气功能障碍。"},
	{"text": "2.支气管激发试验阳性(累计吸入乙酰甲胆碱0.312mg，FEV1下降大于20%，PD20=0.2117mg，气道高
2026-08-10 11:37:26,514 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord API: raw_items=195, valid_items=194, elapsed=64.4s
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[0]: text=激发试验检查报告, bbox=[427, 37, 620, 56]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[215, 75, 260, 88]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[2]: text=测试号：, bbox=[215, 89, 275, 102]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[3]: text=门诊/住院号：, bbox=[542, 74, 644, 87]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[4]: text=000, bbox=[699, 75, 721, 87]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：, bbox=[215, 103, 260, 116]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[6]: text=出生日期：, bbox=[542, 88, 618, 101]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[7]: text=19, bbox=[700, 90, 718, 101]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[8]: text=性别：, bbox=[215, 117, 260, 130]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[9]: text=身高：, bbox=[542, 102, 584, 115]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[10]: text=170, bbox=[700, 103, 718, 114]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[11]: text=病区：, bbox=[215, 131, 260, 144]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[12]: text=内科门诊, bbox=[375, 131, 445, 144]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[13]: text=体重：, bbox=[542, 116, 584, 129]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[14]: text=81 kg, bbox=[699, 116, 741, 128]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[15]: text=机器编号：, bbox=[215, 145, 294, 158]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[16]: text=床号：, bbox=[542, 130, 584, 143]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[17]: text=电话：, bbox=[542, 144, 584, 157]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[18]: text=Pred, bbox=[332, 175, 368, 188]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[19]: text=A1, bbox=[402, 175, 418, 188]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[20]: text=A1/Pd, bbox=[434, 175, 474, 188]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[21]: text=NS, bbox=[508, 175, 525, 188]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[22]: text=P1 chg%1, bbox=[558, 175, 628, 188]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[23]: text=P2 chg%2, bbox=[664, 175, 734, 188]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[24]: text=P3 chg%3, bbox=[769, 175, 838, 188]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[25]: text=FVC, bbox=[56, 203, 84, 215]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[26]: text=[L], bbox=[263, 203, 287, 216]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[27]: text=4.84, bbox=[334, 203, 368, 215]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[28]: text=4.69, bbox=[398, 203, 424, 215]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[29]: text=97.1, bbox=[438, 203, 472, 215]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[30]: text=4.29, bbox=[494, 203, 524, 215]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[31]: text=4.22, bbox=[542, 203, 570, 215]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[32]: text=-10.1, bbox=[594, 203, 628, 215]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[33]: text=3.64, bbox=[648, 203, 676, 215]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[34]: text=-22.5, bbox=[700, 203, 734, 215]
2026-08-10 11:37:26,519 INFO     29 [qwen-vl-text] coord item[35]: text=4.01, bbox=[754, 203, 782, 215]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[36]: text=-14.6, bbox=[806, 203, 838, 215]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[37]: text=PEV 1, bbox=[56, 217, 99, 229]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[38]: text=[L], bbox=[263, 217, 287, 230]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[39]: text=4.01, bbox=[334, 217, 368, 229]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[40]: text=3.05, bbox=[398, 217, 424, 229]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[41]: text=76.2, bbox=[438, 217, 472, 229]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[42]: text=2.72, bbox=[494, 217, 524, 229]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[43]: text=2.69, bbox=[542, 217, 570, 229]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[44]: text=-11.8, bbox=[594, 217, 628, 229]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[45]: text=2.24, bbox=[648, 217, 676, 229]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[46]: text=-26.5, bbox=[700, 217, 734, 229]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[47]: text=2.44, bbox=[754, 217, 782, 229]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[48]: text=-20.0, bbox=[806, 217, 838, 229]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[49]: text=PEV 1 % PVC, bbox=[56, 231, 152, 243]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[50]: text=[%], bbox=[263, 231, 287, 244]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[51]: text=83.32, bbox=[324, 231, 368, 243]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[52]: text=65.02, bbox=[388, 231, 424, 243]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[53]: text=78.0, bbox=[438, 231, 472, 243]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[54]: text=63.54, bbox=[484, 231, 524, 243]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[55]: text=63.83, bbox=[532, 231, 570, 243]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[56]: text=-1.82, bbox=[594, 231, 628, 243]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[57]: text=61.73, bbox=[648, 231, 676, 243]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[58]: text=-5.06, bbox=[700, 231, 734, 243]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[59]: text=60.92, bbox=[754, 231, 782, 243]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[60]: text=-6.30, bbox=[806, 231, 838, 243]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[61]: text=PEV 1 % VC MAX, bbox=[56, 245, 177, 257]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[62]: text=[%], bbox=[263, 245, 287, 258]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[63]: text=80.55, bbox=[324, 245, 368, 257]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[64]: text=64.94, bbox=[388, 245, 424, 257]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[65]: text=80.6, bbox=[438, 245, 472, 257]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[66]: text=62.34, bbox=[484, 245, 524, 257]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[67]: text=63.83, bbox=[532, 245, 570, 257]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[68]: text=-1.70, bbox=[594, 245, 628, 257]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[69]: text=61.73, bbox=[648, 245, 676, 257]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[70]: text=-4.94, bbox=[700, 245, 734, 257]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[71]: text=60.92, bbox=[754, 245, 782, 257]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[72]: text=-6.18, bbox=[806, 245, 838, 257]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[73]: text=VC MAX, bbox=[56, 259, 109, 271]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[74]: text=[L], bbox=[263, 259, 287, 272]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[75]: text=5.05, bbox=[334, 259, 368, 271]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[76]: text=4.70, bbox=[398, 259, 424, 271]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[77]: text=93.1, bbox=[438, 259, 472, 271]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[78]: text=4.37, bbox=[494, 259, 524, 271]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[79]: text=4.22, bbox=[542, 259, 570, 271]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[80]: text=-10.2, bbox=[594, 259, 628, 271]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[81]: text=3.64, bbox=[648, 259, 676, 271]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[82]: text=-22.6, bbox=[700, 259, 734, 271]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[83]: text=4.01, bbox=[754, 259, 782, 271]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[84]: text=-14.7, bbox=[806, 259, 838, 271]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[85]: text=PEP, bbox=[56, 273, 83, 285]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[86]: text=[L/s], bbox=[246, 273, 287, 286]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[87]: text=9.37, bbox=[334, 273, 368, 285]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[88]: text=9.95, bbox=[398, 273, 424, 285]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[89]: text=106.2, bbox=[430, 273, 472, 285]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[90]: text=9.06, bbox=[494, 273, 524, 285]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[91]: text=7.81, bbox=[542, 273, 570, 285]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[92]: text=-21.5, bbox=[594, 273, 628, 285]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[93]: text=6.73, bbox=[648, 273, 676, 285]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[94]: text=-32.3, bbox=[700, 273, 734, 285]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[95]: text=8.22, bbox=[754, 273, 782, 285]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[96]: text=-17.4, bbox=[806, 273, 838, 285]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[97]: text=MMEF 75/25, bbox=[56, 287, 143, 300]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[98]: text=[L/s], bbox=[246, 287, 287, 300]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[99]: text=4.52, bbox=[334, 287, 368, 300]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[100]: text=1.54, bbox=[398, 287, 424, 300]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[101]: text=34.1, bbox=[438, 287, 472, 300]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[102]: text=1.33, bbox=[494, 287, 524, 300]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[103]: text=1.34, bbox=[542, 287, 570, 300]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[104]: text=-12.9, bbox=[594, 287, 628, 300]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[105]: text=1.14, bbox=[648, 287, 676, 300]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[106]: text=-25.8, bbox=[700, 287, 734, 300]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[107]: text=1.23, bbox=[754, 287, 782, 300]
2026-08-10 11:37:26,520 INFO     29 [qwen-vl-text] coord item[108]: text=-20.0, bbox=[806, 287, 838, 300]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[109]: text=MEF 50, bbox=[56, 301, 109, 314]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[110]: text=[L/s], bbox=[246, 301, 287, 314]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[111]: text=5.17, bbox=[334, 301, 368, 314]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[112]: text=1.97, bbox=[398, 301, 424, 314]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[113]: text=38.1, bbox=[438, 301, 472, 314]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[114]: text=1.66, bbox=[494, 301, 524, 314]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[115]: text=1.71, bbox=[542, 301, 570, 314]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[116]: text=-13.4, bbox=[594, 301, 628, 314]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[117]: text=1.34, bbox=[648, 301, 676, 314]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[118]: text=-31.8, bbox=[700, 301, 734, 314]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[119]: text=1.42, bbox=[754, 301, 782, 314]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[120]: text=-28.0, bbox=[806, 301, 838, 314]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[121]: text=MEF 25, bbox=[56, 315, 109, 328]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[122]: text=[L/s], bbox=[246, 315, 287, 328]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[123]: text=2.29, bbox=[334, 315, 368, 328]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[124]: text=0.58, bbox=[398, 315, 424, 328]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[125]: text=25.5, bbox=[438, 315, 472, 328]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[126]: text=0.52, bbox=[494, 315, 524, 328]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[127]: text=0.53, bbox=[542, 315, 570, 328]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[128]: text=-9.87, bbox=[594, 315, 628, 328]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[129]: text=0.50, bbox=[648, 315, 676, 328]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[130]: text=-14.6, bbox=[700, 315, 734, 328]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[131]: text=0.49, bbox=[754, 315, 782, 328]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[132]: text=-15.7, bbox=[806, 315, 838, 328]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[133]: text=PET, bbox=[56, 330, 83, 342]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[134]: text=[s], bbox=[263, 330, 287, 343]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[135]: text=6.72, bbox=[388, 330, 420, 342]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[136]: text=6.87, bbox=[490, 330, 522, 342]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[137]: text=6.93, bbox=[542, 330, 574, 342]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[138]: text=3.16, bbox=[594, 330, 626, 342]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[139]: text=6.75, bbox=[648, 330, 680, 342]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[140]: text=0.57, bbox=[700, 330, 732, 342]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[141]: text=6.74, bbox=[754, 330, 786, 342]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[142]: text=0.38, bbox=[806, 330, 838, 342]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[143]: text=V backextrapolation ex, bbox=[56, 344, 234, 357]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[144]: text=[L], bbox=[263, 344, 287, 357]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[145]: text=0.13, bbox=[388, 344, 420, 357]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[146]: text=0.09, bbox=[490, 344, 522, 357]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[147]: text=0.10, bbox=[542, 344, 574, 357]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[148]: text=-20.0, bbox=[594, 344, 626, 357]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[149]: text=0.08, bbox=[648, 344, 680, 357]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[150]: text=-41.6, bbox=[700, 344, 732, 357]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[151]: text=0.08, bbox=[754, 344, 786, 357]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[152]: text=-38.5, bbox=[806, 344, 838, 357]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[153]: text=PIF, bbox=[56, 358, 83, 371]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[154]: text=[L/s], bbox=[246, 358, 287, 371]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[155]: text=8.04, bbox=[388, 358, 420, 371]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[156]: text=7.96, bbox=[490, 358, 522, 371]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[157]: text=7.58, bbox=[542, 358, 574, 371]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[158]: text=-5.76, bbox=[594, 358, 626, 371]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[159]: text=6.16, bbox=[648, 358, 680, 371]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[160]: text=-23.3, bbox=[700, 358, 732, 371]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[161]: text=7.78, bbox=[754, 358, 786, 371]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[162]: text=-3.20, bbox=[806, 358, 838, 371]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[163]: text=FIF 50, bbox=[56, 372, 109, 385]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[164]: text=[L/s], bbox=[246, 372, 287, 385]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[165]: text=7.99, bbox=[388, 372, 420, 385]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[166]: text=7.86, bbox=[490, 372, 522, 385]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[167]: text=7.16, bbox=[542, 372, 574, 385]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[168]: text=-10.3, bbox=[594, 372, 626, 385]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[169]: text=5.36, bbox=[648, 372, 680, 385]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[170]: text=-32.9, bbox=[700, 372, 732, 385]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[171]: text=7.08, bbox=[754, 372, 786, 385]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[172]: text=-11.3, bbox=[806, 372, 838, 385]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[173]: text=MVV, bbox=[56, 386, 83, 399]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[174]: text=[L/min], bbox=[229, 386, 287, 399]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[175]: text=141.88, bbox=[317, 386, 368, 399]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[176]: text=BF MVV, bbox=[56, 400, 109, 413]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[177]: text=[1/min], bbox=[229, 400, 287, 413]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[178]: text=Cumulated dose, bbox=[56, 428, 179, 441]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[179]: text=0.072 0.078, bbox=[479, 428, 574, 441]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[180]: text=0.312, bbox=[637, 428, 680, 441]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[181]: text=2 Puf, bbox=[740, 428, 786, 441]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[182]: text=F/V ex, bbox=[349, 472, 386, 484]
2026-08-10 11:37:26,521 INFO     29 [qwen-vl-text] coord item[183]: text=F/V in, bbox=[349, 719, 383, 730]
2026-08-10 11:37:26,522 INFO     29 [qwen-vl-text] coord item[184]: text=Vol [L], bbox=[644, 507, 680, 520]
2026-08-10 11:37:26,522 INFO     29 [qwen-vl-text] coord item[185]: text=Vol%VCmax, bbox=[590, 530, 658, 540]
2026-08-10 11:37:26,522 INFO     29 [qwen-vl-text] coord item[186]: text=VCmax, bbox=[657, 545, 697, 555]
2026-08-10 11:37:26,522 INFO     29 [qwen-vl-text] coord item[187]: text=Time [s], bbox=[775, 658, 819, 669]
2026-08-10 11:37:26,522 INFO     29 [qwen-vl-text] coord item[188]: text=PD[-20] FEV 1: 0.2117 mg Cumulated, bbox=[96, 750, 389, 763]
2026-08-10 11:37:26,522 INFO     29 [qwen-vl-text] coord item[189]: text=PD[-20] PEF: < 0.078 mg Cumulated, bbox=[96, 762, 381, 775]
2026-08-10 11:37:26,522 INFO     29 [qwen-vl-text] coord item[190]: text=PD[] FEV1%I: could not be calculated!, bbox=[96, 786, 414, 799]
2026-08-10 11:37:26,522 INFO     29 [qwen-vl-text] coord item[191]: text=意见：, bbox=[86, 808, 134, 822]
2026-08-10 11:37:26,522 INFO     29 [qwen-vl-text] coord item[192]: text=2022/6/08 10:23:56上午, bbox=[86, 830, 273, 843]
2026-08-10 11:37:26,522 INFO     29 [qwen-vl-text] coord item[193]: text=1.轻度阻塞性通气功能障碍。, bbox=[86, 842, 314, 855]
2026-08-10 11:37:26,535 INFO     29 [qwen-vl-text] page=10 — 195/197 coords, api_time=64.4s
2026-08-10 11:37:26,535 INFO     29 [qwen-vl-text] new_positions (197):
[[10, 254.065, 368.9, 31.154, 47.152], [10, 127.925, 154.7, 63.15, 74.096], [10, 127.925, 163.625, 74.938, 85.884], [10, 322.49, 383.18, 62.308, 73.25399999999999], [10, 415.905, 428.995, 63.15, 73.25399999999999], [10, 127.925, 154.7, 86.726, 97.672], [10, 322.49, 367.71, 74.096, 85.042], [10, 416.5, 427.21, 75.78, 85.042], [10, 127.925, 154.7, 98.514, 109.46], [10, 322.49, 347.47999999999996, 85.884, 96.83], [10, 416.5, 427.21, 86.726, 95.988], [10, 127.925, 154.7, 110.30199999999999, 121.24799999999999], [10, 223.125, 264.775, 110.30199999999999, 121.24799999999999], [10, 322.49, 347.47999999999996, 97.672, 108.618], [10, 415.905, 440.895, 97.672, 107.776], [10, 127.925, 174.92999999999998, 122.08999999999999, 133.036], [10, 322.49, 347.47999999999996, 109.46, 120.40599999999999], [10, 322.49, 347.47999999999996, 121.24799999999999, 132.194], [10, 197.54, 218.95999999999998, 147.35, 158.296], [10, 239.19, 248.70999999999998, 147.35, 158.296], [10, 258.22999999999996, 282.03, 147.35, 158.296], [10, 302.26, 312.375, 147.35, 158.296], [10, 332.01, 373.65999999999997, 147.35, 158.296], [10, 395.08, 436.72999999999996, 147.35, 158.296], [10, 457.555, 498.60999999999996, 147.35, 158.296], [10, 33.32, 49.98, 170.926, 181.03], [10, 156.48499999999999, 170.765, 170.926, 181.87199999999999], [10, 198.73, 218.95999999999998, 170.926, 181.03], [10, 236.81, 252.28, 170.926, 181.03], [10, 260.61, 280.84, 170.926, 181.03], [10, 293.93, 311.78, 170.926, 181.03], [10, 322.49, 339.15, 170.926, 181.03], [10, 353.43, 373.65999999999997, 170.926, 181.03], [10, 385.56, 402.21999999999997, 170.926, 181.03], [10, 416.5, 436.72999999999996, 170.926, 181.03], [10, 448.63, 465.28999999999996, 170.926, 181.03], [10, 479.57, 498.60999999999996, 170.926, 181.03], [10, 33.32, 58.904999999999994, 182.714, 192.81799999999998], [10, 156.48499999999999, 170.765, 182.714, 193.66], [10, 198.73, 218.95999999999998, 182.714, 192.81799999999998], [10, 236.81, 252.28, 182.714, 192.81799999999998], [10, 260.61, 280.84, 182.714, 192.81799999999998], [10, 293.93, 311.78, 182.714, 192.81799999999998], [10, 322.49, 339.15, 182.714, 192.81799999999998], [10, 353.43, 373.65999999999997, 182.714, 192.81799999999998], [10, 385.56, 402.21999999999997, 182.714, 192.81799999999998], [10, 416.5, 436.72999999999996, 182.714, 192.81799999999998], [10, 448.63, 465.28999999999996, 182.714, 192.81799999999998], [10, 479.57, 498.60999999999996, 182.714, 192.81799999999998], [10, 33.32, 90.44, 194.50199999999998, 204.606], [10, 156.48499999999999, 170.765, 194.50199999999998, 205.44799999999998], [10, 192.78, 218.95999999999998, 194.50199999999998, 204.606], [10, 230.85999999999999, 252.28, 194.50199999999998, 204.606], [10, 260.61, 280.84, 194.50199999999998, 204.606], [10, 287.97999999999996, 311.78, 194.50199999999998, 204.606], [10, 316.53999999999996, 339.15, 194.50199999999998, 204.606], [10, 353.43, 373.65999999999997, 194.50199999999998, 204.606], [10, 385.56, 402.21999999999997, 194.50199999999998, 204.606], [10, 416.5, 436.72999999999996, 194.50199999999998, 204.606], [10, 448.63, 465.28999999999996, 194.50199999999998, 204.606], [10, 479.57, 498.60999999999996, 194.50199999999998, 204.606], [10, 33.32, 105.315, 206.29, 216.394], [10, 156.48499999999999, 170.765, 206.29, 217.236], [10, 192.78, 218.95999999999998, 206.29, 216.394], [10, 230.85999999999999, 252.28, 206.29, 216.394], [10, 260.61, 280.84, 206.29, 216.394], [10, 287.97999999999996, 311.78, 206.29, 216.394], [10, 316.53999999999996, 339.15, 206.29, 216.394], [10, 353.43, 373.65999999999997, 206.29, 216.394], [10, 385.56, 402.21999999999997, 206.29, 216.394], [10, 416.5, 436.72999999999996, 206.29, 216.394], [10, 448.63, 465.28999999999996, 206.29, 216.394], [10, 479.57, 498.60999999999996, 206.29, 216.394], [10, 33.32, 64.855, 218.078, 228.182], [10, 156.48499999999999, 170.765, 218.078, 229.024], [10, 198.73, 218.95999999999998, 218.078, 228.182], [10, 236.81, 252.28, 218.078, 228.182], [10, 260.61, 280.84, 218.078, 228.182], [10, 293.93, 311.78, 218.078, 228.182], [10, 322.49, 339.15, 218.078, 228.182], [10, 353.43, 373.65999999999997, 218.078, 228.182], [10, 385.56, 402.21999999999997, 218.078, 228.182], [10, 416.5, 436.72999999999996, 218.078, 228.182], [10, 448.63, 465.28999999999996, 218.078, 228.182], [10, 479.57, 498.60999999999996, 218.078, 228.182], [10, 33.32, 49.385, 229.86599999999999, 239.97], [10, 146.37, 170.765, 229.86599999999999, 240.81199999999998], [10, 198.73, 218.95999999999998, 229.86599999999999, 239.97], [10, 236.81, 252.28, 229.86599999999999, 239.97], [10, 255.85, 280.84, 229.86599999999999, 239.97], [10, 293.93, 311.78, 229.86599999999999, 239.97], [10, 322.49, 339.15, 229.86599999999999, 239.97], [10, 353.43, 373.65999999999997, 229.86599999999999, 239.97], [10, 385.56, 402.21999999999997, 229.86599999999999, 239.97], [10, 416.5, 436.72999999999996, 229.86599999999999, 239.97], [10, 448.63, 465.28999999999996, 229.86599999999999, 239.97], [10, 479.57, 498.60999999999996, 229.86599999999999, 239.97], [10, 33.32, 85.085, 241.654, 252.6], [10, 146.37, 170.765, 241.654, 252.6], [10, 198.73, 218.95999999999998, 241.654, 252.6], [10, 236.81, 252.28, 241.654, 252.6], [10, 260.61, 280.84, 241.654, 252.6], [10, 293.93, 311.78, 241.654, 252.6], [10, 322.49, 339.15, 241.654, 252.6], [10, 353.43, 373.65999999999997, 241.654, 252.6], [10, 385.56, 402.21999999999997, 241.654, 252.6], [10, 416.5, 436.72999999999996, 241.654, 252.6], [10, 448.63, 465.28999999999996, 241.654, 252.6], [10, 479.57, 498.60999999999996, 241.654, 252.6], [10, 33.32, 64.855, 253.44199999999998, 264.388], [10, 146.37, 170.765, 253.44199999999998, 264.388], [10, 198.73, 218.95999999999998, 253.44199999999998, 264.388], [10, 236.81, 252.28, 253.44199999999998, 264.388], [10, 260.61, 280.84, 253.44199999999998, 264.388], [10, 293.93, 311.78, 253.44199999999998, 264.388], [10, 322.49, 339.15, 253.44199999999998, 264.388], [10, 353.43, 373.65999999999997, 253.44199999999998, 264.388], [10, 385.56, 402.21999999999997, 253.44199999999998, 264.388], [10, 416.5, 436.72999999999996, 253.44199999999998, 264.388], [10, 448.63, 465.28999999999996, 253.44199999999998, 264.388], [10, 479.57, 498.60999999999996, 253.44199999999998, 264.388], [10, 33.32, 64.855, 265.23, 276.176], [10, 146.37, 170.765, 265.23, 276.176], [10, 198.73, 218.95999999999998, 265.23, 276.176], [10, 236.81, 252.28, 265.23, 276.176], [10, 260.61, 280.84, 265.23, 276.176], [10, 293.93, 311.78, 265.23, 276.176], [10, 322.49, 339.15, 265.23, 276.176], [10, 353.43, 373.65999999999997, 265.23, 276.176], [10, 385.56, 402.21999999999997, 265.23, 276.176], [10, 416.5, 436.72999999999996, 265.23, 276.176], [10, 448.63, 465.28999999999996, 265.23, 276.176], [10, 479.57, 498.60999999999996, 265.23, 276.176], [10, 33.32, 49.385, 277.86, 287.964], [10, 156.48499999999999, 170.765, 277.86, 288.806], [10, 230.85999999999999, 249.89999999999998, 277.86, 287.964], [10, 291.55, 310.59, 277.86, 287.964], [10, 322.49, 341.53, 277.86, 287.964], [10, 353.43, 372.46999999999997, 277.86, 287.964], [10, 385.56, 404.59999999999997, 277.86, 287.964], [10, 416.5, 435.53999999999996, 277.86, 287.964], [10, 448.63, 467.66999999999996, 277.86, 287.964], [10, 479.57, 498.60999999999996, 277.86, 287.964], [10, 33.32, 139.23, 289.64799999999997, 300.594], [10, 156.48499999999999, 170.765, 289.64799999999997, 300.594], [10, 230.85999999999999, 249.89999999999998, 289.64799999999997, 300.594], [10, 291.55, 310.59, 289.64799999999997, 300.594], [10, 322.49, 341.53, 289.64799999999997, 300.594], [10, 353.43, 372.46999999999997, 289.64799999999997, 300.594], [10, 385.56, 404.59999999999997, 289.64799999999997, 300.594], [10, 416.5, 435.53999999999996, 289.64799999999997, 300.594], [10, 448.63, 467.66999999999996, 289.64799999999997, 300.594], [10, 479.57, 498.60999999999996, 289.64799999999997, 300.594], [10, 33.32, 49.385, 301.436, 312.382], [10, 146.37, 170.765, 301.436, 312.382], [10, 230.85999999999999, 249.89999999999998, 301.436, 312.382], [10, 291.55, 310.59, 301.436, 312.382], [10, 322.49, 341.53, 301.436, 312.382], [10, 353.43, 372.46999999999997, 301.436, 312.382], [10, 385.56, 404.59999999999997, 301.436, 312.382], [10, 416.5, 435.53999999999996, 301.436, 312.382], [10, 448.63, 467.66999999999996, 301.436, 312.382], [10, 479.57, 498.60999999999996, 301.436, 312.382], [10, 33.32, 64.855, 313.224, 324.17], [10, 146.37, 170.765, 313.224, 324.17], [10, 230.85999999999999, 249.89999999999998, 313.224, 324.17], [10, 291.55, 310.59, 313.224, 324.17], [10, 322.49, 341.53, 313.224, 324.17], [10, 353.43, 372.46999999999997, 313.224, 324.17], [10, 385.56, 404.59999999999997, 313.224, 324.17], [10, 416.5, 435.53999999999996, 313.224, 324.17], [10, 448.63, 467.66999999999996, 313.224, 324.17], [10, 479.57, 498.60999999999996, 313.224, 324.17], [10, 33.32, 49.385, 325.012, 335.95799999999997], [10, 136.255, 170.765, 325.012, 335.95799999999997], [10, 188.61499999999998, 218.95999999999998, 325.012, 335.95799999999997], [10, 33.32, 64.855, 336.8, 347.746], [10, 136.255, 170.765, 336.8, 347.746], [10, 33.32, 106.505, 360.376, 371.322], [10, 285.005, 341.53, 360.376, 371.322], [10, 379.015, 404.59999999999997, 360.376, 371.322], [10, 440.29999999999995, 467.66999999999996, 360.376, 371.322], [10, 207.655, 229.67, 397.424, 407.52799999999996], [10, 207.655, 227.885, 605.398, 614.66], [10, 383.18, 404.59999999999997, 426.894, 437.84], [10, 351.05, 391.51, 446.26, 454.68], [10, 390.91499999999996, 414.715, 458.89, 467.31], [10, 461.125, 487.30499999999995, 554.036, 563.298], [10, 57.12, 231.45499999999998, 631.5, 642.446], [10, 57.12, 226.695, 641.6039999999999, 652.55], [10, 57.12, 246.32999999999998, 661.812, 672.7579999999999], [10, 51.169999999999995, 79.72999999999999, 680.336, 692.124], [10, 51.169999999999995, 162.435, 698.86, 709.8059999999999], [10, 51.169999999999995, 186.82999999999998, 708.9639999999999, 719.91], [10, 51.169999999999995, 186.82999999999998, 708.9639999999999, 719.91], [10, 0, 0, 0, 0], [10, 0, 0, 0, 0]]
2026-08-10 11:37:26,535 INFO     29 [qwen-vl-text] ═══ DONE ═══ 197 positions, pages=1, time=73.7s
2026-08-10 11:37:26,535 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:37:26,542 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:37:26,542 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 11:37:26,542 INFO     29 [qwen-vl-text] positions(209): [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:37:26,542 INFO     29 [qwen-vl-text] page grouping: [11], lines per page: [209]
2026-08-10 11:37:26,757 INFO     29 [qwen-vl-text] page=11, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:37:26,758 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1284
2026-08-10 11:37:26,758 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:37:26,758 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 481, \"bbox_end\": 689, \"encounter_dates\": [\"2021-01-21\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "检查日期：2021/1/21\n检查时间：16:43\n编号：16\n广州医科大学附属第三医院\n支气管扩张试验检查报告\n姓名：\n测试号：\n年龄：36岁\n性别：男\n病区：\n机器编号：\n门诊/住院号：\n出生日期：\n身高：\n体重：\n床号：\n电话：\nPred\nA1\nA1/Pd\nP1\nA2/Pd\nchg%1\nP2\nA3/Pd\nchg%2\nP3\nA4/Pd\nchg%3\nFVC\n[L]\n4.86\n3.48\n71.5%\n4.01\n82.4%\n15.19\n4.15\n85.4%\n19.47\n4.01\n82.6%\n15.47\nFEV 1\n[L]\n4.03\n1.97\n48.8%\n2.33\n57.9%\n18.59\n2.33\n57.8%\n18.48\n2.44\n60.5%\n24.02\nFEV 1 % FVC\n[%]\n83.32\n56.62\n68.0%\n58.29\n70.0%\n2.95\n56.15\n67.4%\n-0.83\n60.81\n73.0%\n7.40\nFEV 1 % VC MAX\n[%]\n80.73\n56.07\n69.5%\n58.29\n72.2%\n3.96\n56.15\n69.5%\n0.14\n60.81\n75.3%\n8.45\nVC MAX\n[L]\n5.08\n3.51\n69.1%\n4.01\n78.9%\n14.07\n4.15\n81.8%\n18.31\n4.01\n79.1%\n14.35\nPEF\n[L/s]\n9.41\n6.61\n70.3%\n7.99\n85.0%\n20.93\n7.91\n84.1%\n19.63\n8.07\n85.7%\n22.02\nMMEF 75/25\n[L/s]\n4.57\n0.81\n17.7%\n0.96\n21.1%\n19.59\n1.03\n22.6%\n28.17\n1.12\n24.6%\n39.07\nMEF 50\n[L/s]\n5.20\n1.00\n19.2%\n1.29\n24.8%\n29.25\n1.30\n24.9%\n29.87\n1.53\n29.3%\n52.75\nMEF 25\n[L/s]\n2.32\n0.39\n16.7%\n0.38\n16.4%\n-1.68\n0.50\n21.6%\n29.78\n0.41\n17.9%\n7.18\nFET\n[s]\n15.24\n6.42\n-57.87\n6.30\n-58.63\n6.55\n-57.05\nV backextrapolati\n[L/s]\n0.07\n0.07\n0.89\n0.09\n17.79\n0.08\n6.12\nPIF\n[L/s]\n7.03\n7.39\n5.19\n7.17\n1.99\n7.16\n1.91\nFIV1\n[L]\n3.40\n3.76\n10.58\n3.68\n8.26\n3.60\n5.96\nPEF50 % PIF50\n[%]\n16.56\n21.70\n31.06\n19.81\n19.65\n24.71\n49.20\nMVV\n[L/min]\n142.69\nBF MVV\n[1/min]\n意见：\n1.重度混合性肺通气功能障碍。\n2.支气管舒张试验阳性。\n（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后PEV1较基线增加大于12%，且绝对值增加大于200ml）",
    "role": "user"
  }
]
2026-08-10 11:37:26,761 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:37:26.760+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 23, "failed": 0, "current": {"ea51b5dc94ae11f1bd9827cf206dfa2d": {"id": "ea51b5dc94ae11f1bd9827cf206dfa2d", "doc_id": "ea1b0b1894ae11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786361440167, "task_type": "dataflow", "root_trace_id": "bca8d639df704cd29f0107370613ab01", "root_traceparent": "00-bca8d639df704cd29f0107370613ab01-b8b3c91a32048c1c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:37:40,253 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:37:40,254 INFO     29 [qwen-vl-text] LLM output (len=2059):
{
  "exam_date": "2021-01-21",
  "report_date": null,
  "exam_name": "支气管扩张试验检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "| 指标 | Pred | A1 | A1/Pd | P1 | A2/Pd | chg%1 | P2 | A3/Pd | chg%2 | P3 | A4/Pd | chg%3 |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n| FVC [L] | 4.86 | 3.48 | 71.5% | 4.01 | 82.4% | 15.19 | 4.15 | 85.4% | 19.47 | 4.01 | 82.6% | 15.47 |\n| FEV 1 [L] | 4.03 | 1.97 | 48.8% | 2.33 | 57.9% | 18.59 | 2.33 | 57.8% | 18.48 | 2.44 | 60.5% | 24.02 |\n| FEV 1 % FVC [%] | 83.32 | 56.62 | 68.0% | 58.29 | 70.0% | 2.95 | 56.15 | 67.4% | -0.83 | 60.81 | 73.0% | 7.40 |\n| FEV 1 % VC MAX [%] | 80.73 | 56.07 | 69.5% | 58.29 | 72.2% | 3.96 | 56.15 | 69.5% | 0.14 | 60.81 | 75.3% | 8.45 |\n| VC MAX [L] | 5.08 | 3.51 | 69.1% | 4.01 | 78.9% | 14.07 | 4.15 | 81.8% | 18.31 | 4.01 | 79.1% | 14.35 |\n| PEF [L/s] | 9.41 | 6.61 | 70.3% | 7.99 | 85.0% | 20.93 | 7.91 | 84.1% | 19.63 | 8.07 | 85.7% | 22.02 |\n| MMEF 75/25 [L/s] | 4.57 | 0.81 | 17.7% | 0.96 | 21.1% | 19.59 | 1.03 | 22.6% | 28.17 | 1.12 | 24.6% | 39.07 |\n| MEF 50 [L/s] | 5.20 | 1.00 | 19.2% | 1.29 | 24.8% | 29.25 | 1.30 | 24.9% | 29.87 | 1.53 | 29.3% | 52.75 |\n| MEF 25 [L/s] | 2.32 | 0.39 | 16.7% | 0.38 | 16.4% | -1.68 | 0.50 | 21.6% | 29.78 | 0.41 | 17.9% | 7.18 |\n| FET [s] | 15.24 | 6.42 | -57.87 | 6.30 | -58.63 | 6.55 | -57.05 | | | | | |\n| V backextrapolati [L/s] | 0.07 | 0.07 | 0.89 | 0.09 | 17.79 | 0.08 | 6.12 | | | | | |\n| PIF [L/s] | 7.03 | 7.39 | 5.19 | 7.17 | 1.99 | 7.16 | 1.91 | | | | | |\n| FIV1 [L] | 3.40 | 3.76 | 10.58 | 3.68 | 8.26 | 3.60 | 5.96 | | | | | |\n| PEF50 % PIF50 [%] | 16.56 | 21.70 | 31.06 | 19.81 | 19.65 | 24.71 | 49.20 | | | | | |\n| MVV [L/min] | 142.69 | | | | | | | | | | | |\n| BF MVV [1/min] | | | | | | | | | | | | |",
  "conclusion": "意见：\n1.重度混合性肺通气功能障碍。\n2.支气管舒张试验阳性。\n（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后PEV1较基线增加大于12%，且绝对值增加大于200ml）",
  "physician": null,
  "reviewer": null
}
2026-08-10 11:37:40,259 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1426724, prompt_len=2525
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共209行）
["检查日期：2021/1/21", "检查时间：16:43", "编号：16", "广州医科大学附属第三医院", "支气管扩张试验检查报告", "姓名：", "测试号：", "年龄：36岁", "性别：男", "病区：", "机器编号：", "门诊/住院号：", "出生日期：", "身高：", "体重：", "床号：", "电话：", "Pred", "A1", "A1/Pd", "P1", "A2/Pd", "chg%1", "P2", "A3/Pd", "chg%2", "P3", "A4/Pd", "chg%3", "FVC", "[L]", "4.86", "3.48", "71.5%", "4.01", "82.4%", "15.19", "4.15", "85.4%", "19.47", "4.01", "82.6%", "15.47", "FEV 1", "[L]", "4.03", "1.97", "48.8%", "2.33", "57.9%", "18.59", "2.33", "57.8%", "18.48", "2.44", "60.5%", "24.02", "FEV 1 % FVC", "[%]", "83.32", "56.62", "68.0%", "58.29", "70.0%", "2.95", "56.15", "67.4%", "-0.83", "60.81", "73.0%", "7.40", "FEV 1 % VC MAX", "[%]", "80.73", "56.07", "69.5%", "58.29", "72.2%", "3.96", "56.15", "69.5%", "0.14", "60.81", "75.3%", "8.45", "VC MAX", "[L]", "5.08", "3.51", "69.1%", "4.01", "78.9%", "14.07", "4.15", "81.8%", "18.31", "4.01", "79.1%", "14.35", "PEF", "[L/s]", "9.41", "6.61", "70.3%", "7.99", "85.0%", "20.93", "7.91", "84.1%", "19.63", "8.07", "85.7%", "22.02", "MMEF 75/25", "[L/s]", "4.57", "0.81", "17.7%", "0.96", "21.1%", "19.59", "1.03", "22.6%", "28.17", "1.12", "24.6%", "39.07", "MEF 50", "[L/s]", "5.20", "1.00", "19.2%", "1.29", "24.8%", "29.25", "1.30", "24.9%", "29.87", "1.53", "29.3%", "52.75", "MEF 25", "[L/s]", "2.32", "0.39", "16.7%", "0.38", "16.4%", "-1.68", "0.50", "21.6%", "29.78", "0.41", "17.9%", "7.18", "FET", "[s]", "15.24", "6.42", "-57.87", "6.30", "-58.63", "6.55", "-57.05", "V backextrapolati", "[L/s]", "0.07", "0.07", "0.89", "0.09", "17.79", "0.08", "6.12", "PIF", "[L/s]", "7.03", "7.39", "5.19", "7.17", "1.99", "7.16", "1.91", "FIV1", "[L]", "3.40", "3.76", "10.58", "3.68", "8.26", "3.60", "5.96", "PEF50 % PIF50", "[%]", "16.56", "21.70", "31.06", "19.81", "19.65", "24.71", "49.20", "MVV", "[L/min]", "142.69", "BF MVV", "[1/min]", "意见：", "1.重度混合性肺通气功能障碍。", "2.支气管舒张试验阳性。", "（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后PEV1较基线增加大于12%，且绝对值增加大于200ml）"]

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
2026-08-10 11:38:33,365 INFO     29 [qwen-vl-text] coord API raw response (len=10399):
[
	{"text": "检查日期：2021/1/21", "bbox": [49, 88, 158, 98]},
	{"text": "检查时间：16:43", "bbox": [186, 88, 273, 98]},
	{"text": "编号：16", "bbox": [295, 88, 342, 98]},
	{"text": "广州医科大学附属第三医院", "bbox": [367, 104, 644, 120]},
	{"text": "支气管扩张试验检查报告", "bbox": [378, 120, 632, 136]},
	{"text": "姓名：", "bbox": [191, 144, 234, 157]},
	{"text": "测试号：", "bbox": [191, 157, 248, 170]},
	{"text": "年龄：36岁", "bbox": [191, 170, 382, 183]},
	{"text": "性别：男", "bbox": [191, 183, 358, 196]},
	{"text": "病区：", "bbox": [191, 196, 234, 209]},
	{"text": "机器编号：", "bbox": [191, 209, 264, 222]},
	{"text": "门诊/住院号：", "bbox": [500, 143, 596, 156]},
	{"text": "出生日期：", "bbox": [500, 156, 572, 169]},
	{"text": "身高：", "bbox": [500, 169, 540, 182]},
	{"text": "体重：", "bbox": [500, 182, 540, 195]},
	{"text": "床号：", "bbox": [500, 195, 540, 208]},
	{"text": "电话：", "bbox": [500, 208, 540, 221]},
	{"text": "Pred", "bbox": [265, 231, 300, 243]},
	{"text": "A1", "bbox": [340, 231, 358, 243]},
	{"text": "A1/Pd", "bbox": [375, 231, 417, 243]},
	{"text": "P1", "bbox": [457, 231, 472, 243]},
	{"text": "A2/Pd", "bbox": [490, 231, 532, 243]},
	{"text": "chg%1", "bbox": [549, 231, 589, 243]},
	{"text": "P2", "bbox": [630, 231, 646, 243]},
	{"text": "A3/Pd", "bbox": [664, 231, 705, 243]},
	{"text": "chg%2", "bbox": [722, 231, 763, 243]},
	{"text": "P3", "bbox": [804, 231, 819, 243]},
	{"text": "A4/Pd", "bbox": [837, 231, 878, 243]},
	{"text": "chg%3", "bbox": [895, 231, 935, 243]},
	{"text": "FVC", "bbox": [54, 257, 81, 269]},
	{"text": "[L]", "bbox": [198, 257, 221, 270]},
	{"text": "4.86", "bbox": [265, 257, 300, 269]},
	{"text": "3.48", "bbox": [324, 257, 358, 269]},
	{"text": "71.5%", "bbox": [375, 257, 417, 269]},
	{"text": "4.01", "bbox": [444, 257, 472, 269]},
	{"text": "82.4%", "bbox": [490, 257, 532, 269]},
	{"text": "15.19", "bbox": [549, 257, 589, 269]},
	{"text": "4.15", "bbox": [613, 257, 646, 269]},
	{"text": "85.4%", "bbox": [664, 257, 705, 269]},
	{"text": "19.47", "bbox": [722, 257, 763, 269]},
	{"text": "4.01", "bbox": [797, 257, 819, 269]},
	{"text": "82.6%", "bbox": [837, 257, 878, 269]},
	{"text": "15.47", "bbox": [895, 257, 935, 269]},
	{"text": "FEV 1", "bbox": [54, 270, 95, 283]},
	{"text": "[L]", "bbox": [198, 270, 221, 283]},
	{"text": "4.03", "bbox": [265, 270, 300, 283]},
	{"text": "1.97", "bbox": [324, 270, 358, 283]},
	{"text": "48.8%", "bbox": [324, 270, 417, 283]},
	{"text": "2.33", "bbox": [444, 270, 472, 283]},
	{"text": "57.9%", "bbox": [490, 270, 532, 283]},
	{"text": "18.59", "bbox": [549, 270, 589, 283]},
	{"text": "2.33", "bbox": [613, 270, 646, 283]},
	{"text": "57.8%", "bbox": [664, 270, 705, 283]},
	{"text": "18.48", "bbox": [722, 270, 763, 283]},
	{"text": "2.44", "bbox": [797, 270, 819, 283]},
	{"text": "60.5%", "bbox": [837, 270, 878, 283]},
	{"text": "24.02", "bbox": [895, 270, 935, 283]},
	{"text": "FEV 1 % FVC", "bbox": [54, 284, 146, 297]},
	{"text": "[%]", "bbox": [198, 284, 221, 297]},
	{"text": "83.32", "bbox": [258, 284, 300, 297]},
	{"text": "56.62", "bbox": [317, 284, 358, 297]},
	{"text": "68.0%", "bbox": [375, 284, 417, 297]},
	{"text": "58.29", "bbox": [435, 284, 472, 297]},
	{"text": "70.0%", "bbox": [490, 284, 532, 297]},
	{"text": "2.95", "bbox": [557, 284, 589, 297]},
	{"text": "56.15", "bbox": [606, 284, 646, 297]},
	{"text": "67.4%", "bbox": [664, 284, 705, 297]},
	{"text": "-0.83", "bbox": [722, 284, 763, 297]},
	{"text": "60.81", "bbox": [782, 284, 819, 297]},
	{"text": "73.0%", "bbox": [837, 284, 878, 297]},
	{"text": "7.40", "bbox": [903, 284, 935, 297]},
	{"text": "FEV 1 % VC MAX", "bbox": [54, 297, 170, 310]},
	{"text": "[%]", "bbox": [198, 297, 221, 310]},
	{"text": "80.73", "bbox": [258, 297, 300, 310]},
	{"text": "56.07", "bbox": [317, 297, 358, 310]},
	{"text": "69.5%", "bbox": [375, 297, 417, 310]},
	{"text": "58.29", "bbox": [435, 297, 472, 310]},
	{"text": "72.2%", "bbox": [490, 297, 532, 310]},
	{"text": "3.96", "bbox": [557, 297, 589, 310]},
	{"text": "56.15", "bbox": [606, 297, 646, 310]},
	{"text": "69.5%", "bbox": [664, 297, 705, 310]},
	{"text": "0.14", "bbox": [730, 297, 763, 310]},
	{"text": "60.81", "bbox": [782, 297, 819, 310]},
	{"text": "75.3%", "bbox": [837, 297, 878, 310]},
	{"text": "8.45", "bbox": [903, 297, 935, 310]},
	{"text": "VC MAX", "bbox": [54, 310, 105, 323]},
	{"text": "[L]", "bbox": [198, 310, 221, 323]},
	{"text": "5.08", "bbox": [265, 310, 300, 323]},
	{"text": "3.51", "bbox": [324, 310, 358, 323]},
	{"text": "69.1%", "bbox": [375, 310, 417, 323]},
	{"text": "4.01", "bbox": [444, 310, 472, 323]},
	{"text": "78.9%", "bbox": [490, 310, 532, 323]},
	{"text": "14.07", "bbox": [549, 310, 589, 323]},
	{"text": "4.15", "bbox": [613, 310, 646, 323]},
	{"text": "81.8%", "bbox": [664, 310, 705, 323]},
	{"text": "18.31", "bbox": [722, 310, 763, 323]},
	{"text": "4.01", "bbox": [797, 310, 819, 323]},
	{"text": "79.1%", "bbox": [837, 310, 878, 323]},
	{"text": "14.35", "bbox": [895, 310, 935, 323]},
	{"text": "PEF", "bbox": [54, 324, 80, 337]},
	{"text": "[L/s]", "bbox": [182, 324, 221, 337]},
	{"text": "9.41", "bbox": [265, 324, 300, 337]},
	{"text": "6.61", "bbox": [324, 324, 358, 337]},
	{"text": "70.3%", "bbox": [375, 324, 417, 337]},
	{"text": "7.99", "bbox": [444, 324, 472, 337]},
	{"text": "85.0%", "bbox": [490, 324, 532, 337]},
	{"text": "20.93", "bbox": [549, 324, 589, 337]},
	{"text": "7.91", "bbox": [613, 324, 646, 337]},
	{"text": "84.1%", "bbox": [664, 324, 705, 337]},
	{"text": "19.63", "bbox": [722, 324, 763, 337]},
	{"text": "8.07", "bbox": [797, 324, 819, 337]},
	{"text": "85.7%", "bbox": [837, 324, 878, 337]},
	{"text": "22.02", "bbox": [895, 324, 935, 337]},
	{"text": "MMEF 75/25", "bbox": [54, 338, 137, 351]},
	{"text": "[L/s]", "bbox": [182, 338, 221, 351]},
	{"text": "4.57", "bbox": [265, 338, 300, 351]},
	{"text": "0.81", "bbox": [324, 338, 358, 351]},
	{"text": "17.7%", "bbox": [375, 338, 417, 351]},
	{"text": "0.96", "bbox": [444, 338, 472, 351]},
	{"text": "21.1%", "bbox": [490, 338, 532, 351]},
	{"text": "19.59", "bbox": [549, 338, 589, 351]},
	{"text": "1.03", "bbox": [613, 338, 646, 351]},
	{"text": "22.6%", "bbox": [664, 338, 705, 351]},
	{"text": "28.17", "bbox": [722, 338, 763, 351]},
	{"text": "1.12", "bbox": [797, 338, 819, 351]},
	{"text": "24.6%", "bbox": [837, 338, 878, 351]},
	{"text": "39.07", "bbox": [895, 338, 935, 351]},
	{"text": "MEF 50", "bbox": [54, 351, 104, 364]},
	{"text": "[L/s]", "bbox": [182, 351, 221, 364]},
	{"text": "5.20", "bbox": [265, 351, 300, 364]},
	{"text": "1.00", "bbox": [324, 351, 358, 364]},
	{"text": "19.2%", "bbox": [375, 351, 417, 364]},
	{"text": "1.29", "bbox": [444, 351, 472, 364]},
	{"text": "24.8%", "bbox": [490, 351, 532, 364]},
	{"text": "29.25", "bbox": [549, 351, 589, 364]},
	{"text": "1.30", "bbox": [613, 351, 646, 364]},
	{"text": "24.9%", "bbox": [664, 351, 705, 364]},
	{"text": "29.87", "bbox": [722, 351, 763, 364]},
	{"text": "1.53", "bbox": [797, 351, 819, 364]},
	{"text": "29.3%", "bbox": [837, 351, 878, 364]},
	{"text": "52.75", "bbox": [895, 351, 935, 364]},
	{"text": "MEF 25", "bbox": [54, 365, 104, 378]},
	{"text": "[L/s]", "bbox": [182, 365, 221, 378]},
	{"text": "2.32", "bbox": [265, 365, 300, 378]},
	{"text": "0.39", "bbox": [324, 365, 358, 378]},
	{"text": "16.7%", "bbox": [375, 365, 417, 378]},
	{"text": "0.38", "bbox": [444, 365, 472, 378]},
	{"text": "16.4%", "bbox": [490, 365, 532, 378]},
	{"text": "-1.68", "bbox": [549, 365, 589, 378]},
	{"text": "0.50", "bbox": [613, 365, 646, 378]},
	{"text": "21.6%", "bbox": [664, 365, 705, 378]},
	{"text": "29.78", "bbox": [722, 365, 763, 378]},
	{"text": "0.41", "bbox": [797, 365, 819, 378]},
	{"text": "17.9%", "bbox": [837, 365, 878, 378]},
	{"text": "7.18", "bbox": [903, 365, 935, 378]},
	{"text": "FET", "bbox": [54, 378, 80, 391]},
	{"text": "[s]", "bbox": [200, 378, 221, 391]},
	{"text": "15.24", "bbox": [320, 378, 358, 391]},
	{"text": "6.42", "bbox": [441, 378, 472, 391]},
	{"text": "-57.87", "bbox": [543, 378, 589, 391]},
	{"text": "6.30", "bbox": [613, 378, 646, 391]},
	{"text": "-58.63", "bbox": [715, 378, 763, 391]},
	{"text": "6.55", "bbox": [790, 378, 819, 391]},
	{"text": "-57.05", "bbox": [887, 378, 935, 391]},
	{"text": "V backextrapolati", "bbox": [54, 392, 225, 405]},
	{"text": "[L/s]", "bbox": [182, 405, 221, 418]},
	{"text": "0.07", "bbox": [326, 392, 358, 405]},
	{"text": "0.07", "bbox": [441, 392, 472, 405]},
	{"text": "0.89", "bbox": [555, 392, 589, 405]},
	{"text": "0.09", "bbox": [613, 392, 646, 405]},
	{"text": "17.79", "bbox": [722, 392, 763, 405]},
	{"text": "0.08", "bbox": [790, 392, 819, 405]},
	{"text": "6.12", "bbox": [903, 392, 935, 405]},
	{"text": "PIF", "bbox": [54, 405, 80, 418]},
	{"text": "7.03", "bbox": [326, 405, 358, 418]},
	{"text": "7.39", "bbox": [441, 405, 472, 418]},
	{"text": "5.19", "bbox": [555, 405, 589, 418]},
	{"text": "7.17", "bbox": [613, 405, 646, 418]},
	{"text": "1.99", "bbox": [730, 405, 763, 418]},
	{"text": "7.16", "bbox": [790, 405, 819, 418]},
	{"text": "1.91", "bbox": [903, 405, 935, 418]},
	{"text": "FIV1", "bbox": [54, 419, 87, 432]},
	{"text": "[L]", "bbox": [198, 419, 221, 432]},
	{"text": "3.40", "bbox": [326, 419, 358, 432]},
	{"text": "3.76", "bbox": [441, 419, 472, 432]},
	{"text": "10.58", "bbox": [549, 419, 589, 432]},
	{"text": "3.68", "bbox": [613, 419, 646, 432]},
	{"text": "8.26", "bbox": [730, 419, 763, 432]},
	{"text": "3.60", "bbox": [790, 419, 819, 432]},
	{"text": "5.96", "bbox": [903, 419, 935, 432]},
	{"text": "PEF50 % PIF50", "bbox": [54, 432, 162, 445]},
	{"text": "[%]", "bbox": [198, 432, 221, 445]},
	{"text": "16.56", "bbox": [317, 432, 358, 445]},
	{"text": "21.70", "bbox": [433, 432, 472, 445]},
	{"text": "31.06", "bbox": [549, 432, 589, 445]},
	{"text": "19.81", "bbox": [606, 432, 646, 445]},
	{"text": "19.65", "bbox": [722, 432, 763, 445]},
	{"text": "24.71", "bbox": [782, 432, 819, 445]},
	{"text": "49.20", "bbox": [895, 432, 935, 445]},
	{"text": "MVV", "bbox": [54, 446, 80, 459]},
	{"text": "[L/min]", "bbox": [167, 446, 221, 459]},
	{"text": "142.69", "bbox": [251, 446, 300, 459]},
	{"text": "BF MVV", "bbox": [54, 459, 104, 472]},
	{"text": "[1/min]", "bbox": [167, 459, 221, 472]},
	{"text": "意见：", "bbox": [73, 789, 120, 803]},
	{"text": "1.重度混合性肺通气功能障碍。", "bbox": [73, 803, 292, 816]},
	{"text": "2.支气管舒张试验阳性。", "bbox": [73, 815, 244, 828]},
	{"text": "（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后PEV1较基线增加大于12%，且绝对值增加大于200ml）", "bbox": [80, 826, 800, 839]}
]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord API: raw_items=208, valid_items=208, elapsed=53.1s
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[0]: text=检查日期：2021/1/21, bbox=[49, 88, 158, 98]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[1]: text=检查时间：16:43, bbox=[186, 88, 273, 98]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[2]: text=编号：16, bbox=[295, 88, 342, 98]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[3]: text=广州医科大学附属第三医院, bbox=[367, 104, 644, 120]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[4]: text=支气管扩张试验检查报告, bbox=[378, 120, 632, 136]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[5]: text=姓名：, bbox=[191, 144, 234, 157]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[6]: text=测试号：, bbox=[191, 157, 248, 170]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[7]: text=年龄：36岁, bbox=[191, 170, 382, 183]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[8]: text=性别：男, bbox=[191, 183, 358, 196]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[9]: text=病区：, bbox=[191, 196, 234, 209]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[10]: text=机器编号：, bbox=[191, 209, 264, 222]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[11]: text=门诊/住院号：, bbox=[500, 143, 596, 156]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[12]: text=出生日期：, bbox=[500, 156, 572, 169]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[13]: text=身高：, bbox=[500, 169, 540, 182]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[14]: text=体重：, bbox=[500, 182, 540, 195]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[15]: text=床号：, bbox=[500, 195, 540, 208]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[16]: text=电话：, bbox=[500, 208, 540, 221]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[17]: text=Pred, bbox=[265, 231, 300, 243]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[18]: text=A1, bbox=[340, 231, 358, 243]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[19]: text=A1/Pd, bbox=[375, 231, 417, 243]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[20]: text=P1, bbox=[457, 231, 472, 243]
2026-08-10 11:38:33,366 INFO     29 [qwen-vl-text] coord item[21]: text=A2/Pd, bbox=[490, 231, 532, 243]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[22]: text=chg%1, bbox=[549, 231, 589, 243]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[23]: text=P2, bbox=[630, 231, 646, 243]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[24]: text=A3/Pd, bbox=[664, 231, 705, 243]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[25]: text=chg%2, bbox=[722, 231, 763, 243]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[26]: text=P3, bbox=[804, 231, 819, 243]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[27]: text=A4/Pd, bbox=[837, 231, 878, 243]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[28]: text=chg%3, bbox=[895, 231, 935, 243]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[29]: text=FVC, bbox=[54, 257, 81, 269]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[30]: text=[L], bbox=[198, 257, 221, 270]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[31]: text=4.86, bbox=[265, 257, 300, 269]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[32]: text=3.48, bbox=[324, 257, 358, 269]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[33]: text=71.5%, bbox=[375, 257, 417, 269]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[34]: text=4.01, bbox=[444, 257, 472, 269]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[35]: text=82.4%, bbox=[490, 257, 532, 269]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[36]: text=15.19, bbox=[549, 257, 589, 269]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[37]: text=4.15, bbox=[613, 257, 646, 269]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[38]: text=85.4%, bbox=[664, 257, 705, 269]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[39]: text=19.47, bbox=[722, 257, 763, 269]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[40]: text=4.01, bbox=[797, 257, 819, 269]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[41]: text=82.6%, bbox=[837, 257, 878, 269]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[42]: text=15.47, bbox=[895, 257, 935, 269]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[43]: text=FEV 1, bbox=[54, 270, 95, 283]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[44]: text=[L], bbox=[198, 270, 221, 283]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[45]: text=4.03, bbox=[265, 270, 300, 283]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[46]: text=1.97, bbox=[324, 270, 358, 283]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[47]: text=48.8%, bbox=[324, 270, 417, 283]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[48]: text=2.33, bbox=[444, 270, 472, 283]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[49]: text=57.9%, bbox=[490, 270, 532, 283]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[50]: text=18.59, bbox=[549, 270, 589, 283]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[51]: text=2.33, bbox=[613, 270, 646, 283]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[52]: text=57.8%, bbox=[664, 270, 705, 283]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[53]: text=18.48, bbox=[722, 270, 763, 283]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[54]: text=2.44, bbox=[797, 270, 819, 283]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[55]: text=60.5%, bbox=[837, 270, 878, 283]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[56]: text=24.02, bbox=[895, 270, 935, 283]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[57]: text=FEV 1 % FVC, bbox=[54, 284, 146, 297]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[58]: text=[%], bbox=[198, 284, 221, 297]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[59]: text=83.32, bbox=[258, 284, 300, 297]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[60]: text=56.62, bbox=[317, 284, 358, 297]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[61]: text=68.0%, bbox=[375, 284, 417, 297]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[62]: text=58.29, bbox=[435, 284, 472, 297]
2026-08-10 11:38:33,367 INFO     29 [qwen-vl-text] coord item[63]: text=70.0%, bbox=[490, 284, 532, 297]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[64]: text=2.95, bbox=[557, 284, 589, 297]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[65]: text=56.15, bbox=[606, 284, 646, 297]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[66]: text=67.4%, bbox=[664, 284, 705, 297]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[67]: text=-0.83, bbox=[722, 284, 763, 297]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[68]: text=60.81, bbox=[782, 284, 819, 297]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[69]: text=73.0%, bbox=[837, 284, 878, 297]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[70]: text=7.40, bbox=[903, 284, 935, 297]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[71]: text=FEV 1 % VC MAX, bbox=[54, 297, 170, 310]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[72]: text=[%], bbox=[198, 297, 221, 310]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[73]: text=80.73, bbox=[258, 297, 300, 310]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[74]: text=56.07, bbox=[317, 297, 358, 310]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[75]: text=69.5%, bbox=[375, 297, 417, 310]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[76]: text=58.29, bbox=[435, 297, 472, 310]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[77]: text=72.2%, bbox=[490, 297, 532, 310]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[78]: text=3.96, bbox=[557, 297, 589, 310]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[79]: text=56.15, bbox=[606, 297, 646, 310]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[80]: text=69.5%, bbox=[664, 297, 705, 310]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[81]: text=0.14, bbox=[730, 297, 763, 310]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[82]: text=60.81, bbox=[782, 297, 819, 310]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[83]: text=75.3%, bbox=[837, 297, 878, 310]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[84]: text=8.45, bbox=[903, 297, 935, 310]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[85]: text=VC MAX, bbox=[54, 310, 105, 323]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[86]: text=[L], bbox=[198, 310, 221, 323]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[87]: text=5.08, bbox=[265, 310, 300, 323]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[88]: text=3.51, bbox=[324, 310, 358, 323]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[89]: text=69.1%, bbox=[375, 310, 417, 323]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[90]: text=4.01, bbox=[444, 310, 472, 323]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[91]: text=78.9%, bbox=[490, 310, 532, 323]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[92]: text=14.07, bbox=[549, 310, 589, 323]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[93]: text=4.15, bbox=[613, 310, 646, 323]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[94]: text=81.8%, bbox=[664, 310, 705, 323]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[95]: text=18.31, bbox=[722, 310, 763, 323]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[96]: text=4.01, bbox=[797, 310, 819, 323]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[97]: text=79.1%, bbox=[837, 310, 878, 323]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[98]: text=14.35, bbox=[895, 310, 935, 323]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[99]: text=PEF, bbox=[54, 324, 80, 337]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[100]: text=[L/s], bbox=[182, 324, 221, 337]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[101]: text=9.41, bbox=[265, 324, 300, 337]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[102]: text=6.61, bbox=[324, 324, 358, 337]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[103]: text=70.3%, bbox=[375, 324, 417, 337]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[104]: text=7.99, bbox=[444, 324, 472, 337]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[105]: text=85.0%, bbox=[490, 324, 532, 337]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[106]: text=20.93, bbox=[549, 324, 589, 337]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[107]: text=7.91, bbox=[613, 324, 646, 337]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[108]: text=84.1%, bbox=[664, 324, 705, 337]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[109]: text=19.63, bbox=[722, 324, 763, 337]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[110]: text=8.07, bbox=[797, 324, 819, 337]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[111]: text=85.7%, bbox=[837, 324, 878, 337]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[112]: text=22.02, bbox=[895, 324, 935, 337]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[113]: text=MMEF 75/25, bbox=[54, 338, 137, 351]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[114]: text=[L/s], bbox=[182, 338, 221, 351]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[115]: text=4.57, bbox=[265, 338, 300, 351]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[116]: text=0.81, bbox=[324, 338, 358, 351]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[117]: text=17.7%, bbox=[375, 338, 417, 351]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[118]: text=0.96, bbox=[444, 338, 472, 351]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[119]: text=21.1%, bbox=[490, 338, 532, 351]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[120]: text=19.59, bbox=[549, 338, 589, 351]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[121]: text=1.03, bbox=[613, 338, 646, 351]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[122]: text=22.6%, bbox=[664, 338, 705, 351]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[123]: text=28.17, bbox=[722, 338, 763, 351]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[124]: text=1.12, bbox=[797, 338, 819, 351]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[125]: text=24.6%, bbox=[837, 338, 878, 351]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[126]: text=39.07, bbox=[895, 338, 935, 351]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[127]: text=MEF 50, bbox=[54, 351, 104, 364]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[128]: text=[L/s], bbox=[182, 351, 221, 364]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[129]: text=5.20, bbox=[265, 351, 300, 364]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[130]: text=1.00, bbox=[324, 351, 358, 364]
2026-08-10 11:38:33,368 INFO     29 [qwen-vl-text] coord item[131]: text=19.2%, bbox=[375, 351, 417, 364]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[132]: text=1.29, bbox=[444, 351, 472, 364]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[133]: text=24.8%, bbox=[490, 351, 532, 364]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[134]: text=29.25, bbox=[549, 351, 589, 364]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[135]: text=1.30, bbox=[613, 351, 646, 364]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[136]: text=24.9%, bbox=[664, 351, 705, 364]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[137]: text=29.87, bbox=[722, 351, 763, 364]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[138]: text=1.53, bbox=[797, 351, 819, 364]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[139]: text=29.3%, bbox=[837, 351, 878, 364]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[140]: text=52.75, bbox=[895, 351, 935, 364]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[141]: text=MEF 25, bbox=[54, 365, 104, 378]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[142]: text=[L/s], bbox=[182, 365, 221, 378]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[143]: text=2.32, bbox=[265, 365, 300, 378]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[144]: text=0.39, bbox=[324, 365, 358, 378]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[145]: text=16.7%, bbox=[375, 365, 417, 378]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[146]: text=0.38, bbox=[444, 365, 472, 378]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[147]: text=16.4%, bbox=[490, 365, 532, 378]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[148]: text=-1.68, bbox=[549, 365, 589, 378]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[149]: text=0.50, bbox=[613, 365, 646, 378]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[150]: text=21.6%, bbox=[664, 365, 705, 378]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[151]: text=29.78, bbox=[722, 365, 763, 378]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[152]: text=0.41, bbox=[797, 365, 819, 378]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[153]: text=17.9%, bbox=[837, 365, 878, 378]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[154]: text=7.18, bbox=[903, 365, 935, 378]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[155]: text=FET, bbox=[54, 378, 80, 391]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[156]: text=[s], bbox=[200, 378, 221, 391]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[157]: text=15.24, bbox=[320, 378, 358, 391]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[158]: text=6.42, bbox=[441, 378, 472, 391]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[159]: text=-57.87, bbox=[543, 378, 589, 391]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[160]: text=6.30, bbox=[613, 378, 646, 391]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[161]: text=-58.63, bbox=[715, 378, 763, 391]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[162]: text=6.55, bbox=[790, 378, 819, 391]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[163]: text=-57.05, bbox=[887, 378, 935, 391]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[164]: text=V backextrapolati, bbox=[54, 392, 225, 405]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[165]: text=[L/s], bbox=[182, 405, 221, 418]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[166]: text=0.07, bbox=[326, 392, 358, 405]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[167]: text=0.07, bbox=[441, 392, 472, 405]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[168]: text=0.89, bbox=[555, 392, 589, 405]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[169]: text=0.09, bbox=[613, 392, 646, 405]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[170]: text=17.79, bbox=[722, 392, 763, 405]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[171]: text=0.08, bbox=[790, 392, 819, 405]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[172]: text=6.12, bbox=[903, 392, 935, 405]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[173]: text=PIF, bbox=[54, 405, 80, 418]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[174]: text=7.03, bbox=[326, 405, 358, 418]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[175]: text=7.39, bbox=[441, 405, 472, 418]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[176]: text=5.19, bbox=[555, 405, 589, 418]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[177]: text=7.17, bbox=[613, 405, 646, 418]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[178]: text=1.99, bbox=[730, 405, 763, 418]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[179]: text=7.16, bbox=[790, 405, 819, 418]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[180]: text=1.91, bbox=[903, 405, 935, 418]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[181]: text=FIV1, bbox=[54, 419, 87, 432]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[182]: text=[L], bbox=[198, 419, 221, 432]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[183]: text=3.40, bbox=[326, 419, 358, 432]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[184]: text=3.76, bbox=[441, 419, 472, 432]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[185]: text=10.58, bbox=[549, 419, 589, 432]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[186]: text=3.68, bbox=[613, 419, 646, 432]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[187]: text=8.26, bbox=[730, 419, 763, 432]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[188]: text=3.60, bbox=[790, 419, 819, 432]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[189]: text=5.96, bbox=[903, 419, 935, 432]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[190]: text=PEF50 % PIF50, bbox=[54, 432, 162, 445]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[191]: text=[%], bbox=[198, 432, 221, 445]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[192]: text=16.56, bbox=[317, 432, 358, 445]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[193]: text=21.70, bbox=[433, 432, 472, 445]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[194]: text=31.06, bbox=[549, 432, 589, 445]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[195]: text=19.81, bbox=[606, 432, 646, 445]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[196]: text=19.65, bbox=[722, 432, 763, 445]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[197]: text=24.71, bbox=[782, 432, 819, 445]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[198]: text=49.20, bbox=[895, 432, 935, 445]
2026-08-10 11:38:33,369 INFO     29 [qwen-vl-text] coord item[199]: text=MVV, bbox=[54, 446, 80, 459]
2026-08-10 11:38:33,370 INFO     29 [qwen-vl-text] coord item[200]: text=[L/min], bbox=[167, 446, 221, 459]
2026-08-10 11:38:33,370 INFO     29 [qwen-vl-text] coord item[201]: text=142.69, bbox=[251, 446, 300, 459]
2026-08-10 11:38:33,370 INFO     29 [qwen-vl-text] coord item[202]: text=BF MVV, bbox=[54, 459, 104, 472]
2026-08-10 11:38:33,370 INFO     29 [qwen-vl-text] coord item[203]: text=[1/min], bbox=[167, 459, 221, 472]
2026-08-10 11:38:33,370 INFO     29 [qwen-vl-text] coord item[204]: text=意见：, bbox=[73, 789, 120, 803]
2026-08-10 11:38:33,370 INFO     29 [qwen-vl-text] coord item[205]: text=1.重度混合性肺通气功能障碍。, bbox=[73, 803, 292, 816]
2026-08-10 11:38:33,370 INFO     29 [qwen-vl-text] coord item[206]: text=2.支气管舒张试验阳性。, bbox=[73, 815, 244, 828]
2026-08-10 11:38:33,370 INFO     29 [qwen-vl-text] coord item[207]: text=（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后PEV1较基线增加大于12%，且绝对值增加大于200ml）, bbox=[80, 826, 800, 839]
2026-08-10 11:38:33,370 INFO     29 [qwen-vl-text] page=11 — 209/209 coords, api_time=53.1s
2026-08-10 11:38:33,370 INFO     29 [qwen-vl-text] new_positions (209):
[[11, 29.154999999999998, 94.00999999999999, 74.096, 82.51599999999999], [11, 110.67, 162.435, 74.096, 82.51599999999999], [11, 175.525, 203.48999999999998, 74.096, 82.51599999999999], [11, 218.36499999999998, 383.18, 87.568, 101.03999999999999], [11, 224.91, 376.03999999999996, 101.03999999999999, 114.512], [11, 113.645, 139.23, 121.24799999999999, 132.194], [11, 113.645, 147.56, 132.194, 143.14], [11, 113.645, 227.29, 143.14, 154.08599999999998], [11, 113.645, 213.01, 154.08599999999998, 165.03199999999998], [11, 113.645, 139.23, 165.03199999999998, 175.97799999999998], [11, 113.645, 157.07999999999998, 175.97799999999998, 186.924], [11, 297.5, 354.62, 120.40599999999999, 131.352], [11, 297.5, 340.34, 131.352, 142.298], [11, 297.5, 321.3, 142.298, 153.244], [11, 297.5, 321.3, 153.244, 164.19], [11, 297.5, 321.3, 164.19, 175.136], [11, 297.5, 321.3, 175.136, 186.082], [11, 157.67499999999998, 178.5, 194.50199999999998, 204.606], [11, 202.29999999999998, 213.01, 194.50199999999998, 204.606], [11, 223.125, 248.11499999999998, 194.50199999999998, 204.606], [11, 271.91499999999996, 280.84, 194.50199999999998, 204.606], [11, 291.55, 316.53999999999996, 194.50199999999998, 204.606], [11, 326.655, 350.455, 194.50199999999998, 204.606], [11, 374.84999999999997, 384.37, 194.50199999999998, 204.606], [11, 395.08, 419.47499999999997, 194.50199999999998, 204.606], [11, 429.59, 453.98499999999996, 194.50199999999998, 204.606], [11, 478.38, 487.30499999999995, 194.50199999999998, 204.606], [11, 498.015, 522.41, 194.50199999999998, 204.606], [11, 532.525, 556.3249999999999, 194.50199999999998, 204.606], [11, 32.129999999999995, 48.195, 216.394, 226.498], [11, 117.80999999999999, 131.495, 216.394, 227.34], [11, 157.67499999999998, 178.5, 216.394, 226.498], [11, 192.78, 213.01, 216.394, 226.498], [11, 223.125, 248.11499999999998, 216.394, 226.498], [11, 264.18, 280.84, 216.394, 226.498], [11, 291.55, 316.53999999999996, 216.394, 226.498], [11, 326.655, 350.455, 216.394, 226.498], [11, 364.73499999999996, 384.37, 216.394, 226.498], [11, 395.08, 419.47499999999997, 216.394, 226.498], [11, 429.59, 453.98499999999996, 216.394, 226.498], [11, 474.215, 487.30499999999995, 216.394, 226.498], [11, 498.015, 522.41, 216.394, 226.498], [11, 532.525, 556.3249999999999, 216.394, 226.498], [11, 32.129999999999995, 56.525, 227.34, 238.286], [11, 117.80999999999999, 131.495, 227.34, 238.286], [11, 157.67499999999998, 178.5, 227.34, 238.286], [11, 192.78, 213.01, 227.34, 238.286], [11, 192.78, 248.11499999999998, 227.34, 238.286], [11, 264.18, 280.84, 227.34, 238.286], [11, 291.55, 316.53999999999996, 227.34, 238.286], [11, 326.655, 350.455, 227.34, 238.286], [11, 364.73499999999996, 384.37, 227.34, 238.286], [11, 395.08, 419.47499999999997, 227.34, 238.286], [11, 429.59, 453.98499999999996, 227.34, 238.286], [11, 474.215, 487.30499999999995, 227.34, 238.286], [11, 498.015, 522.41, 227.34, 238.286], [11, 532.525, 556.3249999999999, 227.34, 238.286], [11, 32.129999999999995, 86.86999999999999, 239.128, 250.07399999999998], [11, 117.80999999999999, 131.495, 239.128, 250.07399999999998], [11, 153.51, 178.5, 239.128, 250.07399999999998], [11, 188.61499999999998, 213.01, 239.128, 250.07399999999998], [11, 223.125, 248.11499999999998, 239.128, 250.07399999999998], [11, 258.825, 280.84, 239.128, 250.07399999999998], [11, 291.55, 316.53999999999996, 239.128, 250.07399999999998], [11, 331.41499999999996, 350.455, 239.128, 250.07399999999998], [11, 360.57, 384.37, 239.128, 250.07399999999998], [11, 395.08, 419.47499999999997, 239.128, 250.07399999999998], [11, 429.59, 453.98499999999996, 239.128, 250.07399999999998], [11, 465.28999999999996, 487.30499999999995, 239.128, 250.07399999999998], [11, 498.015, 522.41, 239.128, 250.07399999999998], [11, 537.285, 556.3249999999999, 239.128, 250.07399999999998], [11, 32.129999999999995, 101.14999999999999, 250.07399999999998, 261.02], [11, 117.80999999999999, 131.495, 250.07399999999998, 261.02], [11, 153.51, 178.5, 250.07399999999998, 261.02], [11, 188.61499999999998, 213.01, 250.07399999999998, 261.02], [11, 223.125, 248.11499999999998, 250.07399999999998, 261.02], [11, 258.825, 280.84, 250.07399999999998, 261.02], [11, 291.55, 316.53999999999996, 250.07399999999998, 261.02], [11, 331.41499999999996, 350.455, 250.07399999999998, 261.02], [11, 360.57, 384.37, 250.07399999999998, 261.02], [11, 395.08, 419.47499999999997, 250.07399999999998, 261.02], [11, 434.34999999999997, 453.98499999999996, 250.07399999999998, 261.02], [11, 465.28999999999996, 487.30499999999995, 250.07399999999998, 261.02], [11, 498.015, 522.41, 250.07399999999998, 261.02], [11, 537.285, 556.3249999999999, 250.07399999999998, 261.02], [11, 32.129999999999995, 62.474999999999994, 261.02, 271.966], [11, 117.80999999999999, 131.495, 261.02, 271.966], [11, 157.67499999999998, 178.5, 261.02, 271.966], [11, 192.78, 213.01, 261.02, 271.966], [11, 223.125, 248.11499999999998, 261.02, 271.966], [11, 264.18, 280.84, 261.02, 271.966], [11, 291.55, 316.53999999999996, 261.02, 271.966], [11, 326.655, 350.455, 261.02, 271.966], [11, 364.73499999999996, 384.37, 261.02, 271.966], [11, 395.08, 419.47499999999997, 261.02, 271.966], [11, 429.59, 453.98499999999996, 261.02, 271.966], [11, 474.215, 487.30499999999995, 261.02, 271.966], [11, 498.015, 522.41, 261.02, 271.966], [11, 532.525, 556.3249999999999, 261.02, 271.966], [11, 32.129999999999995, 47.599999999999994, 272.808, 283.75399999999996], [11, 108.28999999999999, 131.495, 272.808, 283.75399999999996], [11, 157.67499999999998, 178.5, 272.808, 283.75399999999996], [11, 192.78, 213.01, 272.808, 283.75399999999996], [11, 223.125, 248.11499999999998, 272.808, 283.75399999999996], [11, 264.18, 280.84, 272.808, 283.75399999999996], [11, 291.55, 316.53999999999996, 272.808, 283.75399999999996], [11, 326.655, 350.455, 272.808, 283.75399999999996], [11, 364.73499999999996, 384.37, 272.808, 283.75399999999996], [11, 395.08, 419.47499999999997, 272.808, 283.75399999999996], [11, 429.59, 453.98499999999996, 272.808, 283.75399999999996], [11, 474.215, 487.30499999999995, 272.808, 283.75399999999996], [11, 498.015, 522.41, 272.808, 283.75399999999996], [11, 532.525, 556.3249999999999, 272.808, 283.75399999999996], [11, 32.129999999999995, 81.515, 284.596, 295.542], [11, 108.28999999999999, 131.495, 284.596, 295.542], [11, 157.67499999999998, 178.5, 284.596, 295.542], [11, 192.78, 213.01, 284.596, 295.542], [11, 223.125, 248.11499999999998, 284.596, 295.542], [11, 264.18, 280.84, 284.596, 295.542], [11, 291.55, 316.53999999999996, 284.596, 295.542], [11, 326.655, 350.455, 284.596, 295.542], [11, 364.73499999999996, 384.37, 284.596, 295.542], [11, 395.08, 419.47499999999997, 284.596, 295.542], [11, 429.59, 453.98499999999996, 284.596, 295.542], [11, 474.215, 487.30499999999995, 284.596, 295.542], [11, 498.015, 522.41, 284.596, 295.542], [11, 532.525, 556.3249999999999, 284.596, 295.542], [11, 32.129999999999995, 61.879999999999995, 295.542, 306.488], [11, 108.28999999999999, 131.495, 295.542, 306.488], [11, 157.67499999999998, 178.5, 295.542, 306.488], [11, 192.78, 213.01, 295.542, 306.488], [11, 223.125, 248.11499999999998, 295.542, 306.488], [11, 264.18, 280.84, 295.542, 306.488], [11, 291.55, 316.53999999999996, 295.542, 306.488], [11, 326.655, 350.455, 295.542, 306.488], [11, 364.73499999999996, 384.37, 295.542, 306.488], [11, 395.08, 419.47499999999997, 295.542, 306.488], [11, 429.59, 453.98499999999996, 295.542, 306.488], [11, 474.215, 487.30499999999995, 295.542, 306.488], [11, 498.015, 522.41, 295.542, 306.488], [11, 532.525, 556.3249999999999, 295.542, 306.488], [11, 32.129999999999995, 61.879999999999995, 307.33, 318.276], [11, 108.28999999999999, 131.495, 307.33, 318.276], [11, 157.67499999999998, 178.5, 307.33, 318.276], [11, 192.78, 213.01, 307.33, 318.276], [11, 223.125, 248.11499999999998, 307.33, 318.276], [11, 264.18, 280.84, 307.33, 318.276], [11, 291.55, 316.53999999999996, 307.33, 318.276], [11, 326.655, 350.455, 307.33, 318.276], [11, 364.73499999999996, 384.37, 307.33, 318.276], [11, 395.08, 419.47499999999997, 307.33, 318.276], [11, 429.59, 453.98499999999996, 307.33, 318.276], [11, 474.215, 487.30499999999995, 307.33, 318.276], [11, 498.015, 522.41, 307.33, 318.276], [11, 537.285, 556.3249999999999, 307.33, 318.276], [11, 32.129999999999995, 47.599999999999994, 318.276, 329.222], [11, 119.0, 131.495, 318.276, 329.222], [11, 190.39999999999998, 213.01, 318.276, 329.222], [11, 262.395, 280.84, 318.276, 329.222], [11, 323.085, 350.455, 318.276, 329.222], [11, 364.73499999999996, 384.37, 318.276, 329.222], [11, 425.42499999999995, 453.98499999999996, 318.276, 329.222], [11, 470.04999999999995, 487.30499999999995, 318.276, 329.222], [11, 527.765, 556.3249999999999, 318.276, 329.222], [11, 32.129999999999995, 133.875, 330.06399999999996, 341.01], [11, 108.28999999999999, 131.495, 341.01, 351.95599999999996], [11, 193.97, 213.01, 330.06399999999996, 341.01], [11, 262.395, 280.84, 330.06399999999996, 341.01], [11, 330.22499999999997, 350.455, 330.06399999999996, 341.01], [11, 364.73499999999996, 384.37, 330.06399999999996, 341.01], [11, 429.59, 453.98499999999996, 330.06399999999996, 341.01], [11, 470.04999999999995, 487.30499999999995, 330.06399999999996, 341.01], [11, 537.285, 556.3249999999999, 330.06399999999996, 341.01], [11, 32.129999999999995, 47.599999999999994, 341.01, 351.95599999999996], [11, 193.97, 213.01, 341.01, 351.95599999999996], [11, 262.395, 280.84, 341.01, 351.95599999999996], [11, 330.22499999999997, 350.455, 341.01, 351.95599999999996], [11, 364.73499999999996, 384.37, 341.01, 351.95599999999996], [11, 434.34999999999997, 453.98499999999996, 341.01, 351.95599999999996], [11, 470.04999999999995, 487.30499999999995, 341.01, 351.95599999999996], [11, 537.285, 556.3249999999999, 341.01, 351.95599999999996], [11, 32.129999999999995, 51.765, 352.798, 363.74399999999997], [11, 117.80999999999999, 131.495, 352.798, 363.74399999999997], [11, 193.97, 213.01, 352.798, 363.74399999999997], [11, 262.395, 280.84, 352.798, 363.74399999999997], [11, 326.655, 350.455, 352.798, 363.74399999999997], [11, 364.73499999999996, 384.37, 352.798, 363.74399999999997], [11, 434.34999999999997, 453.98499999999996, 352.798, 363.74399999999997], [11, 470.04999999999995, 487.30499999999995, 352.798, 363.74399999999997], [11, 537.285, 556.3249999999999, 352.798, 363.74399999999997], [11, 32.129999999999995, 96.39, 363.74399999999997, 374.69], [11, 117.80999999999999, 131.495, 363.74399999999997, 374.69], [11, 188.61499999999998, 213.01, 363.74399999999997, 374.69], [11, 257.635, 280.84, 363.74399999999997, 374.69], [11, 326.655, 350.455, 363.74399999999997, 374.69], [11, 360.57, 384.37, 363.74399999999997, 374.69], [11, 429.59, 453.98499999999996, 363.74399999999997, 374.69], [11, 465.28999999999996, 487.30499999999995, 363.74399999999997, 374.69], [11, 532.525, 556.3249999999999, 363.74399999999997, 374.69], [11, 32.129999999999995, 47.599999999999994, 375.532, 386.478], [11, 99.365, 131.495, 375.532, 386.478], [11, 149.345, 178.5, 375.532, 386.478], [11, 32.129999999999995, 61.879999999999995, 386.478, 397.424], [11, 99.365, 131.495, 386.478, 397.424], [11, 43.434999999999995, 71.39999999999999, 664.338, 676.126], [11, 43.434999999999995, 173.73999999999998, 676.126, 687.072], [11, 43.434999999999995, 145.18, 686.23, 697.1759999999999], [11, 47.599999999999994, 476.0, 695.492, 706.438], [11, 47.599999999999994, 476.0, 695.492, 706.438]]
2026-08-10 11:38:33,370 INFO     29 [qwen-vl-text] ═══ DONE ═══ 209 positions, pages=1, time=66.8s
2026-08-10 11:38:33,371 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:38:33,377 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:38:33,377 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 11:38:33,377 INFO     29 [qwen-vl-text] positions(243): [[15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:38:33,378 INFO     29 [qwen-vl-text] page grouping: [15], lines per page: [243]
2026-08-10 11:38:33,586 INFO     29 [qwen-vl-text] page=15, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:38:33,587 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1756
2026-08-10 11:38:33,587 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:38:33,587 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 794, \"bbox_end\": 1036, \"encounter_dates\": [\"2024-10-22\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "广州医科大学附属第三医院\n肺功能检查报告\n地址：广州市多宝路63号 电话：020-81292126\nCOSMED\n姓名：\n科室/床号：\nID：\n出生日期：1984/12/8\n预计值：ERS 93\n日期：2024/10/22\n性别：Male\n地区修正：Chinese\n详细描述：内科门诊\nCompany：\n年龄：39\n体重(Kg)：89.0\n身高(cm)：177.5\nBMI(Kg/m²：28.2\n吸烟：曾经(10/20)\n用力肺活量 Forced Vital Capacity\nF(l/s)\nV(l)\nBEST #3 - 2024/10/22 11:03\n沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38\n沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39\n沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41\n沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38\n沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39\n沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41\nBEST #3 - 2024/10/22 11:03\nFVC\nPEF\nMEF75%\nMEF50%\nMEF25%\nFVC\n8V(l)\nFEV1\nATS\n12t(s)\n-1 0 1 2 3 4 5 6 7 8 9 10 11 12t(s)\n218133\nST\n2024-10-22\nParameter\nUM\nPred.\nBEST#3\n%Pred.\nPOST#4\n%Pred.\n%Test#3\nPOST#5\n%Pred.\n%Test#3\nPOST#6\n%F\nFVC\nl(btps)\n4.87\n3.48\n71\n3.72\n76\n+6.9\n4.24\n87\n+22.0\n4.11\nFEV1\nl(btps)\n4.01\n2.58\n64\n2.94\n73\n+13.7\n3.15\n79\n+21.9\n3.15\nFEV1/FVC%\n%\n80.2\n74.3\n93\n79.0\n98\n+6.4\n74.2\n93\n0.0\n76.6\nPEF\nl/sec\n9.37\n9.86\n105\n9.98\n107\n+1.3\n10.48\n112\n+6.3\n10.52\n1\nFEV6\nl(btps)\n5.17\n3.68\n71\n4.22\n82\n4.11\nPIF\nl/sec\n7.33\n7.76\n+5.8\n7.78\n+6.1\n7.88\nFEV6/FVC%\n%\n99.0\n99.4\n100.0\nFEF25-75%\nl/sec\n4.47\n1.88\n42\n2.59\n58\n+37.8\n2.31\n52\n+22.8\n2.52\nFEV3\nl(btps)\n3.25\n3.44\n+5.8\n3.94\n+21.3\n3.78\nFEV3/FVC%\n%\n93.3\n92.4\n-1.0\n92.9\n-0.5\n92.1\nFEV1/FEV6%\n%\n79.8\n74.7\n76.6\nMEF75%\nl/sec\n8.09\n5.96\n74\n9.28\n115\n+55.7\n7.53\n93\n+26.3\n7.17\nMEF50%\nl/sec\n5.17\n2.57\n50\n3.49\n68\n+35.8\n3.08\n59\n+19.6\n3.28\nMEF25%\nl/sec\n2.28\n0.71\n31\n0.95\n42\n+33.9\n0.83\n36\n+16.6\n0.87\nFET100%\nsec\n6.0\n6.7\n+12.8\n6.5\n+9.4\n6.5\nVEXT\nml\n208\n192\n162\nIC\nl(btps)\n3.33\n3.38\n+1.5\n3.50\n+5.1\n3.35\nFIVC\nl(btps)\n4.29\n4.70\n+9.6\n4.51\n+5.1\n4.46\nPEFr\nl/min\n562.3\n591.4\n105\n599.0\n107\n+1.3\n628.8\n112\n+6.3\n630.9\n1\n诊断：\n中度限制性通气功能障碍。支气管舒张试验阳性（吸入沙丁胺醇400μg，FEV1上升>12%，且绝对值>200ml）。\n打印2024/10/22\nPFT Suite 10.0d\n页 1 of 1",
    "role": "user"
  }
]
2026-08-10 11:38:33,590 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:38:33.589+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 23, "failed": 0, "current": {"ea51b5dc94ae11f1bd9827cf206dfa2d": {"id": "ea51b5dc94ae11f1bd9827cf206dfa2d", "doc_id": "ea1b0b1894ae11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786361440167, "task_type": "dataflow", "root_trace_id": "bca8d639df704cd29f0107370613ab01", "root_traceparent": "00-bca8d639df704cd29f0107370613ab01-b8b3c91a32048c1c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:38:47,232 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:38:47,232 INFO     29 [qwen-vl-text] LLM output (len=2036):
{
  "exam_date": "2024-10-22",
  "report_date": "2024-10-22",
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "Male",
  "department": "内科门诊",
  "bed_number": null,
  "findings": "用力肺活量 Forced Vital Capacity\nF(l/s)\nV(l)\nBEST #3 - 2024/10/22 11:03\n沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38\n沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39\n沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41\n沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38\n沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39\n沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41\nBEST #3 - 2024/10/22 11:03\nFVC\nPEF\nMEF75%\nMEF50%\nMEF25%\nFVC\n8V(l)\nFEV1\nATS\n12t(s)\n-1 0 1 2 3 4 5 6 7 8 9 10 11 12t(s)\n218133\nST\n2024-10-22\nParameter\nUM\nPred.\nBEST#3\n%Pred.\nPOST#4\n%Pred.\n%Test#3\nPOST#5\n%Pred.\n%Test#3\nPOST#6\n%F\nFVC\nl(btps)\n4.87\n3.48\n71\n3.72\n76\n+6.9\n4.24\n87\n+22.0\n4.11\nFEV1\nl(btps)\n4.01\n2.58\n64\n2.94\n73\n+13.7\n3.15\n79\n+21.9\n3.15\nFEV1/FVC%\n%\n80.2\n74.3\n93\n79.0\n98\n+6.4\n74.2\n93\n0.0\n76.6\nPEF\nl/sec\n9.37\n9.86\n105\n9.98\n107\n+1.3\n10.48\n112\n+6.3\n10.52\n1\nFEV6\nl(btps)\n5.17\n3.68\n71\n4.22\n82\n4.11\nPIF\nl/sec\n7.33\n7.76\n+5.8\n7.78\n+6.1\n7.88\nFEV6/FVC%\n%\n99.0\n99.4\n100.0\nFEF25-75%\nl/sec\n4.47\n1.88\n42\n2.59\n58\n+37.8\n2.31\n52\n+22.8\n2.52\nFEV3\nl(btps)\n3.25\n3.44\n+5.8\n3.94\n+21.3\n3.78\nFEV3/FVC%\n%\n93.3\n92.4\n-1.0\n92.9\n-0.5\n92.1\nFEV1/FEV6%\n%\n79.8\n74.7\n76.6\nMEF75%\nl/sec\n8.09\n5.96\n74\n9.28\n115\n+55.7\n7.53\n93\n+26.3\n7.17\nMEF50%\nl/sec\n5.17\n2.57\n50\n3.49\n68\n+35.8\n3.08\n59\n+19.6\n3.28\nMEF25%\nl/sec\n2.28\n0.71\n31\n0.95\n42\n+33.9\n0.83\n36\n+16.6\n0.87\nFET100%\nsec\n6.0\n6.7\n+12.8\n6.5\n+9.4\n6.5\nVEXT\nml\n208\n192\n162\nIC\nl(btps)\n3.33\n3.38\n+1.5\n3.50\n+5.1\n3.35\nFIVC\nl(btps)\n4.29\n4.70\n+9.6\n4.51\n+5.1\n4.46\nPEFr\nl/min\n562.3\n591.4\n105\n599.0\n107\n+1.3\n628.8\n112\n+6.3\n630.9\n1",
  "conclusion": "诊断：\n中度限制性通气功能障碍。支气管舒张试验阳性（吸入沙丁胺醇400μg，FEV1上升>12%，且绝对值>200ml）。",
  "physician": null,
  "reviewer": null
}
2026-08-10 11:38:47,238 INFO     29 [qwen-vl-text] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1606814, prompt_len=3099
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共243行）
["广州医科大学附属第三医院", "肺功能检查报告", "地址：广州市多宝路63号 电话：020-81292126", "COSMED", "姓名：", "科室/床号：", "ID：", "出生日期：1984/12/8", "预计值：ERS 93", "日期：2024/10/22", "性别：Male", "地区修正：Chinese", "详细描述：内科门诊", "Company：", "年龄：39", "体重(Kg)：89.0", "身高(cm)：177.5", "BMI(Kg/m²：28.2", "吸烟：曾经(10/20)", "用力肺活量 Forced Vital Capacity", "F(l/s)", "V(l)", "BEST #3 - 2024/10/22 11:03", "沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38", "沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39", "沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41", "沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38", "沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39", "沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41", "BEST #3 - 2024/10/22 11:03", "FVC", "PEF", "MEF75%", "MEF50%", "MEF25%", "FVC", "8V(l)", "FEV1", "ATS", "12t(s)", "-1 0 1 2 3 4 5 6 7 8 9 10 11 12t(s)", "218133", "ST", "2024-10-22", "Parameter", "UM", "Pred.", "BEST#3", "%Pred.", "POST#4", "%Pred.", "%Test#3", "POST#5", "%Pred.", "%Test#3", "POST#6", "%F", "FVC", "l(btps)", "4.87", "3.48", "71", "3.72", "76", "+6.9", "4.24", "87", "+22.0", "4.11", "FEV1", "l(btps)", "4.01", "2.58", "64", "2.94", "73", "+13.7", "3.15", "79", "+21.9", "3.15", "FEV1/FVC%", "%", "80.2", "74.3", "93", "79.0", "98", "+6.4", "74.2", "93", "0.0", "76.6", "PEF", "l/sec", "9.37", "9.86", "105", "9.98", "107", "+1.3", "10.48", "112", "+6.3", "10.52", "1", "FEV6", "l(btps)", "5.17", "3.68", "71", "4.22", "82", "4.11", "PIF", "l/sec", "7.33", "7.76", "+5.8", "7.78", "+6.1", "7.88", "FEV6/FVC%", "%", "99.0", "99.4", "100.0", "FEF25-75%", "l/sec", "4.47", "1.88", "42", "2.59", "58", "+37.8", "2.31", "52", "+22.8", "2.52", "FEV3", "l(btps)", "3.25", "3.44", "+5.8", "3.94", "+21.3", "3.78", "FEV3/FVC%", "%", "93.3", "92.4", "-1.0", "92.9", "-0.5", "92.1", "FEV1/FEV6%", "%", "79.8", "74.7", "76.6", "MEF75%", "l/sec", "8.09", "5.96", "74", "9.28", "115", "+55.7", "7.53", "93", "+26.3", "7.17", "MEF50%", "l/sec", "5.17", "2.57", "50", "3.49", "68", "+35.8", "3.08", "59", "+19.6", "3.28", "MEF25%", "l/sec", "2.28", "0.71", "31", "0.95", "42", "+33.9", "0.83", "36", "+16.6", "0.87", "FET100%", "sec", "6.0", "6.7", "+12.8", "6.5", "+9.4", "6.5", "VEXT", "ml", "208", "192", "162", "IC", "l(btps)", "3.33", "3.38", "+1.5", "3.50", "+5.1", "3.35", "FIVC", "l(btps)", "4.29", "4.70", "+9.6", "4.51", "+5.1", "4.46", "PEFr", "l/min", "562.3", "591.4", "105", "599.0", "107", "+1.3", "628.8", "112", "+6.3", "630.9", "1", "诊断：", "中度限制性通气功能障碍。支气管舒张试验阳性（吸入沙丁胺醇400μg，FEV1上升>12%，且绝对值>200ml）。", "打印2024/10/22", "PFT Suite 10.0d", "页 1 of 1"]

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
2026-08-10 11:39:51,856 INFO     29 [qwen-vl-text] coord API raw response (len=11808):
[
	{"text": "广州医科大学附属第三医院", "bbox": [407, 44, 639, 59]},
	{"text": "肺功能检查报告", "bbox": [455, 60, 589, 75]},
	{"text": "地址：广州市多宝路63号 电话：020-81292126", "bbox": [313, 76, 737, 91]},
	{"text": "COSMED", "bbox": [123, 96, 188, 108]},
	{"text": "姓名：", "bbox": [109, 117, 150, 130]},
	{"text": "科室/床号：", "bbox": [109, 131, 185, 144]},
	{"text": "ID：", "bbox": [109, 145, 132, 158]},
	{"text": "出生日期：1984/12/8", "bbox": [109, 159, 267, 171]},
	{"text": "预计值：ERS 93", "bbox": [109, 172, 251, 185]},
	{"text": "日期：2024/10/22", "bbox": [406, 117, 567, 130]},
	{"text": "性别：Male", "bbox": [406, 131, 522, 144]},
	{"text": "地区修正：Chinese", "bbox": [406, 145, 547, 158]},
	{"text": "详细描述：内科门诊", "bbox": [406, 158, 551, 171]},
	{"text": "Company：", "bbox": [406, 172, 481, 185]},
	{"text": "年龄：39", "bbox": [755, 117, 873, 130]},
	{"text": "体重(Kg)：89.0", "bbox": [755, 131, 887, 144]},
	{"text": "身高(cm)：177.5", "bbox": [755, 145, 895, 158]},
	{"text": "BMI(Kg/m²：28.2", "bbox": [755, 158, 887, 171]},
	{"text": "吸烟：曾经(10/20)", "bbox": [755, 172, 936, 185]},
	{"text": "用力肺活量 Forced Vital Capacity", "bbox": [195, 191, 441, 204]},
	{"text": "F(l/s)", "bbox": [127, 205, 157, 216]},
	{"text": "V(l)", "bbox": [531, 191, 555, 204]},
	{"text": "BEST #3 - 2024/10/22 11:03", "bbox": [348, 205, 515, 214]},
	{"text": "沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38", "bbox": [240, 215, 515, 224]},
	{"text": "沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39", "bbox": [240, 225, 515, 234]},
	{"text": "沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41", "bbox": [240, 235, 515, 244]},
	{"text": "沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38", "bbox": [652, 202, 930, 211]},
	{"text": "沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39", "bbox": [652, 212, 930, 221]},
	{"text": "沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41", "bbox": [652, 222, 930, 231]},
	{"text": "FVC", "bbox": [888, 267, 915, 276], "bbox": [888, 267, 915, 276]},
	{"text": "PEF", "bbox": [470, 291, 496, 300], "bbox": [470, 291, 496, 300]},
	{"text": "MEF75%", "bbox": [195, 312, 250, 322], "bbox": [195, 312, 250, 322]},
	{"text": "MEF50%", "bbox": [248, 358, 304, 368], "bbox": [248, 358, 304, 368]},
	{"text": "MEF25%", "bbox": [303, 402, 357, 412], "bbox": [303, 402, 357, 412]},
	{"text": "FVC", "bbox": [357, 437, 384, 446], "bbox": [357, 437, 384, 446]},
	{"text": "8V(l)", "bbox": [492, 446, 519, 456], "bbox": [492, 446, 519, 456]},
	{"text": "FEV1", "bbox": [603, 282, 635, 292], "bbox": [603, 282, 635, 292]},
	{"text": "ATS", "bbox": [744, 364, 773, 373], "bbox": [744, 364, 773, 373]},
	{"text": "12t(s)", "bbox": [909, 373, 942, 383], "bbox": [909, 373, 942, 383]},
	{"text": "-1 0 1 2 3 4 5 6 7 8 9 10 11 12t(s)", "bbox": [543, 373, 942, 383], "bbox": [543, 373, 942, 383]},
	{"text": "218133", "bbox": [613, 477, 714, 511], "bbox": [613, 477, 714, 511]},
	{"text": "ST", "bbox": [611, 538, 692, 587], "bbox": [611, 538, 692, 587]},
	{"text": "2024-10-22", "bbox": [657, 585, 788, 604], "bbox": [657, 585, 788, 604]},
	{"text": "Parameter", "bbox": [112, 611, 184, 620], "bbox": [112, 611, 184, 620]},
	{"text": "UM", "bbox": [208, 611, 230, 620], "bbox": [208, 611, 230, 620]},
	{"text": "Pred.", "bbox": [277, 611, 313, 620], "bbox": [277, 611, 313, 620]},
	{"text": "BEST#3", "bbox": [329, 611, 383, 620], "bbox": [329, 611, 383, 620]},
	{"text": "%Pred.", "bbox": [398, 611, 445, 620], "bbox": [398, 611, 445, 620]},
	{"text": "POST#4", "bbox": [458, 611, 511, 620], "bbox": [458, 611, 511, 620]},
	{"text": "%Pred.", "bbox": [526, 611, 572, 620], "bbox": [526, 611, 572, 620]},
	{"text": "%Test#3", "bbox": [586, 611, 642, 620], "bbox": [586, 611, 642, 620]},
	{"text": "POST#5", "bbox": [655, 611, 709, 620], "bbox": [655, 611, 709, 620]},
	{"text": "%Pred.", "bbox": [724, 611, 770, 620], "bbox": [724, 611, 770, 620]},
	{"text": "%Test#3", "bbox": [784, 611, 841, 620], "bbox": [784, 611, 841, 620]},
	{"text": "POST#6", "bbox": [855, 611, 909, 620], "bbox": [855, 611, 909, 620]},
	{"text": "%F", "bbox": [924, 611, 946, 620], "bbox": [924, 611, 946, 620]},
	{"text": "FVC", "bbox": [112, 628, 142, 638], "bbox": [112, 628, 142, 638]},
	{"text": "l(btps)", "bbox": [208, 628, 247, 638], "bbox": [208, 628, 247, 638]},
	{"text": "4.87", "bbox": [286, 628, 318, 638], "bbox": [286, 628, 318, 638]},
	{"text": "3.48", "bbox": [338, 628, 370, 638], "bbox": [338, 628, 370, 638]},
	{"text": "71", "bbox": [414, 628, 431, 638], "bbox": [414, 628, 431, 638]},
	{"text": "3.72", "bbox": [466, 628, 498, 638], "bbox": [466, 628, 498, 638]},
	{"text": "76", "bbox": [544, 628, 559, 638], "bbox": [544, 628, 559, 638]},
	{"text": "+6.9", "bbox": [586, 628, 619, 638], "bbox": [586, 628, 619, 638]},
	{"text": "4.24", "bbox": [664, 628, 696, 638], "bbox": [664, 628, 696, 638]},
	{"text": "87", "bbox": [742, 628, 757, 638], "bbox": [742, 628, 757, 638]},
	{"text": "+22.0", "bbox": [786, 628, 828, 638], "bbox": [786, 628, 828, 638]},
	{"text": "4.11", "bbox": [864, 628, 896, 638], "bbox": [864, 628, 896, 638]},
	{"text": "FEV1", "bbox": [112, 641, 147, 651], "bbox": [112, 641, 147, 651]},
	{"text": "l(btps)", "bbox": [208, 641, 247, 651], "bbox": [208, 641, 247, 651]},
	{"text": "4.01", "bbox": [286, 641, 318, 651], "bbox": [286, 641, 318, 651]},
	{"text": "2.58", "bbox": [338, 641, 370, 651], "bbox": [338, 641, 370, 651]},
	{"text": "64", "bbox": [414, 641, 431, 651], "bbox": [414, 641, 431, 651]},
	{"text": "2.94", "bbox": [466, 641, 498, 651], "bbox": [466, 641, 498, 651]},
	{"text": "73", "bbox": [544, 641, 559, 651], "bbox": [544, 641, 559, 651]},
	{"text": "+13.7", "bbox": [586, 641, 627, 651], "bbox": [586, 641, 627, 651]},
	{"text": "3.15", "bbox": [664, 641, 696, 651], "bbox": [664, 641, 696, 651]},
	{"text": "79", "bbox": [742, 641, 757, 651], "bbox": [742, 641, 757, 651]},
	{"text": "+21.9", "bbox": [786, 641, 828, 651], "bbox": [786, 641, 828, 651]},
	{"text": "3.15", "bbox": [864, 641, 896, 651], "bbox": [864, 641, 896, 651]},
	{"text": "FEV1/FVC%", "bbox": [112, 653, 194, 663], "bbox": [112, 653, 194, 663]},
	{"text": "%", "bbox": [208, 653, 219, 663], "bbox": [208, 653, 219, 663]},
	{"text": "80.2", "bbox": [286, 653, 318, 663], "bbox": [286, 653, 318, 663]},
	{"text": "74.3", "bbox": [338, 653, 370, 663], "bbox": [338, 653, 370, 663]},
	{"text": "93", "bbox": [414, 653, 431, 663], "bbox": [414, 653, 431, 663]},
	{"text": "79.0", "bbox": [466, 653, 498, 663], "bbox": [466, 653, 498, 663]},
	{"text": "98", "bbox": [544, 653, 559, 663], "bbox": [544, 653, 559, 663]},
	{"text": "+6.4", "bbox": [586, 653, 619, 663], "bbox": [586, 653, 619, 663]},
	{"text": "74.2", "bbox": [664, 653, 696, 663], "bbox": [664, 653, 696, 663]},
	{"text": "93", "bbox": [742, 653, 757, 663], "bbox": [742, 653, 757, 663]},
	{"text": "0.0", "bbox": [786, 653, 810, 663], "bbox": [786, 653, 810, 663]},
	{"text": "76.6", "bbox": [864, 653, 896, 663], "bbox": [864, 653, 896, 663]},
	{"text": "PEF", "bbox": [112, 665, 140, 675], "bbox": [112, 665, 140, 675]},
	{"text": "l/sec", "bbox": [208, 665, 239, 675], "bbox": [208, 665, 239, 675]},
	{"text": "9.37", "bbox": [286, 665, 318, 675], "bbox": [286, 665, 318, 675]},
	{"text": "9.86", "bbox": [338, 665, 370, 675], "bbox": [338, 665, 370, 675]},
	{"text": "105", "bbox": [406, 665, 431, 675], "bbox": [406, 665, 431, 675]},
	{"text": "9.98", "bbox": [466, 665, 498, 675], "bbox": [466, 665, 498, 675]},
	{"text": "107", "bbox": [535, 665, 559, 675], "bbox": [535, 665, 559, 675]},
	{"text": "+1.3", "bbox": [586, 665, 619, 675], "bbox": [586, 665, 619, 675]},
	{"text": "10.48", "bbox": [655, 665, 696, 675], "bbox": [655, 665, 696, 675]},
	{"text": "112", "bbox": [734, 665, 757, 675], "bbox": [734, 665, 757, 675]},
	{"text": "+6.3", "bbox": [786, 665, 819, 675], "bbox": [786, 665, 819, 675]},
	{"text": "10.52", "bbox": [856, 665, 896, 675], "bbox": [856, 665, 896, 675]},
	{"text": "1", "bbox": [934, 665, 942, 675], "bbox": [934, 665, 942, 675]},
	{"text": "FEV6", "bbox": [112, 677, 148, 687], "bbox": [112, 677, 148, 687]},
	{"text": "l(btps)", "bbox": [208, 677, 247, 687], "bbox": [208, 677, 247, 687]},
	{"text": "5.17", "bbox": [286, 677, 318, 687], "bbox": [286, 677, 318, 687]},
	{"text": "3.68", "bbox": [466, 677, 498, 687], "bbox": [466, 677, 498, 687]},
	{"text": "71", "bbox": [544, 677, 559, 687], "bbox": [544, 677, 559, 687]},
	{"text": "4.22", "bbox": [664, 677, 696, 687], "bbox": [664, 677, 696, 687]},
	{"text": "82", "bbox": [742, 677, 757, 687], "bbox": [742, 677, 757, 687]},
	{"text": "4.11", "bbox": [864, 677, 896, 687], "bbox": [864, 677, 896, 687]},
	{"text": "PIF", "bbox": [112, 689, 135, 699], "bbox": [112, 689, 135, 699]},
	{"text": "l/sec", "bbox": [208, 689, 239, 699], "bbox": [208, 689, 239, 699]},
	{"text": "7.33", "bbox": [338, 689, 370, 699], "bbox": [338, 689, 370, 699]},
	{"text": "7.76", "bbox": [466, 689, 498, 699], "bbox": [466, 689, 498, 699]},
	{"text": "+5.8", "bbox": [586, 689, 619, 699], "bbox": [586, 689, 619, 699]},
	{"text": "7.78", "bbox": [664, 689, 696, 699], "bbox": [664, 689, 696, 699]},
	{"text": "+6.1", "bbox": [786, 689, 819, 699], "bbox": [786, 689, 819, 699]},
	{"text": "7.88", "bbox": [864, 689, 896, 699], "bbox": [864, 689, 896, 699]},
	{"text": "FEV6/FVC%", "bbox": [112, 701, 194, 711], "bbox": [112, 701, 194, 711]},
	{"text": "%", "bbox": [208, 701, 219, 711], "bbox": [208, 701, 219, 711]},
	{"text": "99.0", "bbox": [466, 701, 498, 711], "bbox": [466, 701, 498, 711]},
	{"text": "99.4", "bbox": [664, 701, 696, 711], "bbox": [664, 701, 696, 711]},
	{"text": "100.0", "bbox": [856, 701, 896, 711], "bbox": [856, 701, 896, 711]},
	{"text": "FEF25-75%", "bbox": [112, 713, 190, 723], "bbox": [112, 713, 190, 723]},
	{"text": "l/sec", "bbox": [208, 713, 239, 723], "bbox": [208, 713, 239, 723]},
	{"text": "4.47", "bbox": [286, 713, 318, 723], "bbox": [286, 713, 318, 723]},
	{"text": "1.88", "bbox": [338, 713, 370, 723], "bbox": [338, 713, 370, 723]},
	{"text": "42", "bbox": [414, 713, 431, 723], "bbox": [414, 713, 431, 723]},
	{"text": "2.59", "bbox": [466, 713, 498, 723], "bbox": [466, 713, 498, 723]},
	{"text": "58", "bbox": [544, 713, 559, 723], "bbox": [544, 713, 559, 723]},
	{"text": "+37.8", "bbox": [586, 713, 627, 723], "bbox": [586, 713, 627, 723]},
	{"text": "2.31", "bbox": [664, 713, 696, 723], "bbox": [664, 713, 696, 723]},
	{"text": "52", "bbox": [742, 713, 757, 723], "bbox": [742, 713, 757, 723]},
	{"text": "+22.8", "bbox": [786, 713, 828, 723], "bbox": [786, 713, 828, 723]},
	{"text": "2.52", "bbox": [864, 713, 896, 723], "bbox": [864, 713, 896, 723]},
	{"text": "FEV3", "bbox": [112, 725, 149, 735], "bbox": [112, 725, 149, 735]},
	{"text": "l(btps)", "bbox": [208, 725, 247, 735], "bbox": [208, 725, 247, 735]},
	{"text": "3.25", "bbox": [338, 725, 370, 735], "bbox": [338, 725, 370, 735]},
	{"text": "3.44", "bbox": [466, 725, 498, 735], "bbox": [466, 725, 498, 735]},
	{"text": "+5.8", "bbox": [586, 725, 619, 735], "bbox": [586, 725, 619, 735]},
	{"text": "3.94", "bbox": [664, 725, 696, 735], "bbox": [664, 725, 696, 735]},
	{"text": "+21.3", "bbox": [786, 725, 828, 735], "bbox": [786, 725, 828, 735]},
	{"text": "3.78", "bbox": [864, 725, 896, 735], "bbox": [864, 725, 896, 735]},
	{"text": "FEV3/FVC%", "bbox": [112, 737, 194, 747], "bbox": [112, 737, 194, 747]},
	{"text": "%", "bbox": [208, 737, 219, 747], "bbox": [208, 737, 219, 747]},
	{"text": "93.3", "bbox": [338, 737, 370, 747], "bbox": [338, 737, 370, 747]},
	{"text": "92.4", "bbox": [466, 737, 498, 747], "bbox": [466, 737, 498, 747]},
	{"text": "-1.0", "bbox": [586, 737, 619, 747], "bbox": [586, 737, 619, 747]},
	{"text": "92.9", "bbox": [664, 737, 696, 747], "bbox": [664, 737, 696, 747]},
	{"text": "-0.5", "bbox": [786, 737, 819, 747], "bbox": [786, 737, 819, 747]},
	{"text": "92.1", "bbox": [864, 737, 896, 747], "bbox": [864, 737, 896, 747]},
	{"text": "FEV1/FEV6%", "bbox": [112, 749, 200, 759], "bbox": [112, 749
2026-08-10 11:39:51,857 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-10 11:39:51,869 INFO     29 [qwen-vl-text] coord API: raw_items=281, valid_items=155, elapsed=64.6s
2026-08-10 11:39:51,869 INFO     29 [qwen-vl-text] coord item[0]: text=广州医科大学附属第三医院, bbox=[407, 44, 639, 59]
2026-08-10 11:39:51,869 INFO     29 [qwen-vl-text] coord item[1]: text=肺功能检查报告, bbox=[455, 60, 589, 75]
2026-08-10 11:39:51,869 INFO     29 [qwen-vl-text] coord item[2]: text=地址：广州市多宝路63号 电话：020-81292126, bbox=[313, 76, 737, 91]
2026-08-10 11:39:51,869 INFO     29 [qwen-vl-text] coord item[3]: text=COSMED, bbox=[123, 96, 188, 108]
2026-08-10 11:39:51,870 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[109, 117, 150, 130]
2026-08-10 11:39:51,870 INFO     29 [qwen-vl-text] coord item[5]: text=科室/床号：, bbox=[109, 131, 185, 144]
2026-08-10 11:39:51,870 INFO     29 [qwen-vl-text] coord item[6]: text=ID：, bbox=[109, 145, 132, 158]
2026-08-10 11:39:51,870 INFO     29 [qwen-vl-text] coord item[7]: text=出生日期：1984/12/8, bbox=[109, 159, 267, 171]
2026-08-10 11:39:51,870 INFO     29 [qwen-vl-text] coord item[8]: text=预计值：ERS 93, bbox=[109, 172, 251, 185]
2026-08-10 11:39:51,870 INFO     29 [qwen-vl-text] coord item[9]: text=日期：2024/10/22, bbox=[406, 117, 567, 130]
2026-08-10 11:39:51,871 INFO     29 [qwen-vl-text] coord item[10]: text=性别：Male, bbox=[406, 131, 522, 144]
2026-08-10 11:39:51,871 INFO     29 [qwen-vl-text] coord item[11]: text=地区修正：Chinese, bbox=[406, 145, 547, 158]
2026-08-10 11:39:51,871 INFO     29 [qwen-vl-text] coord item[12]: text=详细描述：内科门诊, bbox=[406, 158, 551, 171]
2026-08-10 11:39:51,871 INFO     29 [qwen-vl-text] coord item[13]: text=Company：, bbox=[406, 172, 481, 185]
2026-08-10 11:39:51,871 INFO     29 [qwen-vl-text] coord item[14]: text=年龄：39, bbox=[755, 117, 873, 130]
2026-08-10 11:39:51,871 INFO     29 [qwen-vl-text] coord item[15]: text=体重(Kg)：89.0, bbox=[755, 131, 887, 144]
2026-08-10 11:39:51,871 INFO     29 [qwen-vl-text] coord item[16]: text=身高(cm)：177.5, bbox=[755, 145, 895, 158]
2026-08-10 11:39:51,871 INFO     29 [qwen-vl-text] coord item[17]: text=BMI(Kg/m²：28.2, bbox=[755, 158, 887, 171]
2026-08-10 11:39:51,871 INFO     29 [qwen-vl-text] coord item[18]: text=吸烟：曾经(10/20), bbox=[755, 172, 936, 185]
2026-08-10 11:39:51,871 INFO     29 [qwen-vl-text] coord item[19]: text=用力肺活量 Forced Vital Capacity, bbox=[195, 191, 441, 204]
2026-08-10 11:39:51,871 INFO     29 [qwen-vl-text] coord item[20]: text=F(l/s), bbox=[127, 205, 157, 216]
2026-08-10 11:39:51,871 INFO     29 [qwen-vl-text] coord item[21]: text=V(l), bbox=[531, 191, 555, 204]
2026-08-10 11:39:51,871 INFO     29 [qwen-vl-text] coord item[22]: text=BEST #3 - 2024/10/22 11:03, bbox=[348, 205, 515, 214]
2026-08-10 11:39:51,871 INFO     29 [qwen-vl-text] coord item[23]: text=沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38, bbox=[240, 215, 515, 224]
2026-08-10 11:39:51,872 INFO     29 [qwen-vl-text] coord item[24]: text=沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39, bbox=[240, 225, 515, 234]
2026-08-10 11:39:51,872 INFO     29 [qwen-vl-text] coord item[25]: text=沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41, bbox=[240, 235, 515, 244]
2026-08-10 11:39:51,873 INFO     29 [qwen-vl-text] coord item[26]: text=沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38, bbox=[652, 202, 930, 211]
2026-08-10 11:39:51,874 INFO     29 [qwen-vl-text] coord item[27]: text=沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39, bbox=[652, 212, 930, 221]
2026-08-10 11:39:51,874 INFO     29 [qwen-vl-text] coord item[28]: text=沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41, bbox=[652, 222, 930, 231]
2026-08-10 11:39:51,875 INFO     29 [qwen-vl-text] coord item[29]: text=FVC, bbox=[888, 267, 915, 276]
2026-08-10 11:39:51,876 INFO     29 [qwen-vl-text] coord item[30]: text=PEF, bbox=[470, 291, 496, 300]
2026-08-10 11:39:51,876 INFO     29 [qwen-vl-text] coord item[31]: text=MEF75%, bbox=[195, 312, 250, 322]
2026-08-10 11:39:51,877 INFO     29 [qwen-vl-text] coord item[32]: text=MEF50%, bbox=[248, 358, 304, 368]
2026-08-10 11:39:51,877 INFO     29 [qwen-vl-text] coord item[33]: text=MEF25%, bbox=[303, 402, 357, 412]
2026-08-10 11:39:51,877 INFO     29 [qwen-vl-text] coord item[34]: text=FVC, bbox=[357, 437, 384, 446]
2026-08-10 11:39:51,877 INFO     29 [qwen-vl-text] coord item[35]: text=8V(l), bbox=[492, 446, 519, 456]
2026-08-10 11:39:51,877 INFO     29 [qwen-vl-text] coord item[36]: text=FEV1, bbox=[603, 282, 635, 292]
2026-08-10 11:39:51,877 INFO     29 [qwen-vl-text] coord item[37]: text=ATS, bbox=[744, 364, 773, 373]
2026-08-10 11:39:51,877 INFO     29 [qwen-vl-text] coord item[38]: text=12t(s), bbox=[909, 373, 942, 383]
2026-08-10 11:39:51,877 INFO     29 [qwen-vl-text] coord item[39]: text=-1 0 1 2 3 4 5 6 7 8 9 10 11 12t(s), bbox=[543, 373, 942, 383]
2026-08-10 11:39:51,877 INFO     29 [qwen-vl-text] coord item[40]: text=218133, bbox=[613, 477, 714, 511]
2026-08-10 11:39:51,877 INFO     29 [qwen-vl-text] coord item[41]: text=ST, bbox=[611, 538, 692, 587]
2026-08-10 11:39:51,877 INFO     29 [qwen-vl-text] coord item[42]: text=2024-10-22, bbox=[657, 585, 788, 604]
2026-08-10 11:39:51,877 INFO     29 [qwen-vl-text] coord item[43]: text=Parameter, bbox=[112, 611, 184, 620]
2026-08-10 11:39:51,877 INFO     29 [qwen-vl-text] coord item[44]: text=UM, bbox=[208, 611, 230, 620]
2026-08-10 11:39:51,878 INFO     29 [qwen-vl-text] coord item[45]: text=Pred., bbox=[277, 611, 313, 620]
2026-08-10 11:39:51,878 INFO     29 [qwen-vl-text] coord item[46]: text=BEST#3, bbox=[329, 611, 383, 620]
2026-08-10 11:39:51,878 INFO     29 [qwen-vl-text] coord item[47]: text=%Pred., bbox=[398, 611, 445, 620]
2026-08-10 11:39:51,878 INFO     29 [qwen-vl-text] coord item[48]: text=POST#4, bbox=[458, 611, 511, 620]
2026-08-10 11:39:51,878 INFO     29 [qwen-vl-text] coord item[49]: text=%Pred., bbox=[526, 611, 572, 620]
2026-08-10 11:39:51,878 INFO     29 [qwen-vl-text] coord item[50]: text=%Test#3, bbox=[586, 611, 642, 620]
2026-08-10 11:39:51,878 INFO     29 [qwen-vl-text] coord item[51]: text=POST#5, bbox=[655, 611, 709, 620]
2026-08-10 11:39:51,878 INFO     29 [qwen-vl-text] coord item[52]: text=%Pred., bbox=[724, 611, 770, 620]
2026-08-10 11:39:51,878 INFO     29 [qwen-vl-text] coord item[53]: text=%Test#3, bbox=[784, 611, 841, 620]
2026-08-10 11:39:51,878 INFO     29 [qwen-vl-text] coord item[54]: text=POST#6, bbox=[855, 611, 909, 620]
2026-08-10 11:39:51,878 INFO     29 [qwen-vl-text] coord item[55]: text=%F, bbox=[924, 611, 946, 620]
2026-08-10 11:39:51,878 INFO     29 [qwen-vl-text] coord item[56]: text=FVC, bbox=[112, 628, 142, 638]
2026-08-10 11:39:51,878 INFO     29 [qwen-vl-text] coord item[57]: text=l(btps), bbox=[208, 628, 247, 638]
2026-08-10 11:39:51,878 INFO     29 [qwen-vl-text] coord item[58]: text=4.87, bbox=[286, 628, 318, 638]
2026-08-10 11:39:51,878 INFO     29 [qwen-vl-text] coord item[59]: text=3.48, bbox=[338, 628, 370, 638]
2026-08-10 11:39:51,878 INFO     29 [qwen-vl-text] coord item[60]: text=71, bbox=[414, 628, 431, 638]
2026-08-10 11:39:51,878 INFO     29 [qwen-vl-text] coord item[61]: text=3.72, bbox=[466, 628, 498, 638]
2026-08-10 11:39:51,878 INFO     29 [qwen-vl-text] coord item[62]: text=76, bbox=[544, 628, 559, 638]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[63]: text=+6.9, bbox=[586, 628, 619, 638]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[64]: text=4.24, bbox=[664, 628, 696, 638]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[65]: text=87, bbox=[742, 628, 757, 638]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[66]: text=+22.0, bbox=[786, 628, 828, 638]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[67]: text=4.11, bbox=[864, 628, 896, 638]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[68]: text=FEV1, bbox=[112, 641, 147, 651]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[69]: text=l(btps), bbox=[208, 641, 247, 651]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[70]: text=4.01, bbox=[286, 641, 318, 651]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[71]: text=2.58, bbox=[338, 641, 370, 651]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[72]: text=64, bbox=[414, 641, 431, 651]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[73]: text=2.94, bbox=[466, 641, 498, 651]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[74]: text=73, bbox=[544, 641, 559, 651]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[75]: text=+13.7, bbox=[586, 641, 627, 651]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[76]: text=3.15, bbox=[664, 641, 696, 651]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[77]: text=79, bbox=[742, 641, 757, 651]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[78]: text=+21.9, bbox=[786, 641, 828, 651]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[79]: text=3.15, bbox=[864, 641, 896, 651]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[80]: text=FEV1/FVC%, bbox=[112, 653, 194, 663]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[81]: text=%, bbox=[208, 653, 219, 663]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[82]: text=80.2, bbox=[286, 653, 318, 663]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[83]: text=74.3, bbox=[338, 653, 370, 663]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[84]: text=93, bbox=[414, 653, 431, 663]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[85]: text=79.0, bbox=[466, 653, 498, 663]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[86]: text=98, bbox=[544, 653, 559, 663]
2026-08-10 11:39:51,879 INFO     29 [qwen-vl-text] coord item[87]: text=+6.4, bbox=[586, 653, 619, 663]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[88]: text=74.2, bbox=[664, 653, 696, 663]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[89]: text=93, bbox=[742, 653, 757, 663]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[90]: text=0.0, bbox=[786, 653, 810, 663]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[91]: text=76.6, bbox=[864, 653, 896, 663]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[92]: text=PEF, bbox=[112, 665, 140, 675]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[93]: text=l/sec, bbox=[208, 665, 239, 675]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[94]: text=9.37, bbox=[286, 665, 318, 675]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[95]: text=9.86, bbox=[338, 665, 370, 675]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[96]: text=105, bbox=[406, 665, 431, 675]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[97]: text=9.98, bbox=[466, 665, 498, 675]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[98]: text=107, bbox=[535, 665, 559, 675]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[99]: text=+1.3, bbox=[586, 665, 619, 675]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[100]: text=10.48, bbox=[655, 665, 696, 675]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[101]: text=112, bbox=[734, 665, 757, 675]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[102]: text=+6.3, bbox=[786, 665, 819, 675]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[103]: text=10.52, bbox=[856, 665, 896, 675]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[104]: text=1, bbox=[934, 665, 942, 675]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[105]: text=FEV6, bbox=[112, 677, 148, 687]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[106]: text=l(btps), bbox=[208, 677, 247, 687]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[107]: text=5.17, bbox=[286, 677, 318, 687]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[108]: text=3.68, bbox=[466, 677, 498, 687]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[109]: text=71, bbox=[544, 677, 559, 687]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[110]: text=4.22, bbox=[664, 677, 696, 687]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[111]: text=82, bbox=[742, 677, 757, 687]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[112]: text=4.11, bbox=[864, 677, 896, 687]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[113]: text=PIF, bbox=[112, 689, 135, 699]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[114]: text=l/sec, bbox=[208, 689, 239, 699]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[115]: text=7.33, bbox=[338, 689, 370, 699]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[116]: text=7.76, bbox=[466, 689, 498, 699]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[117]: text=+5.8, bbox=[586, 689, 619, 699]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[118]: text=7.78, bbox=[664, 689, 696, 699]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[119]: text=+6.1, bbox=[786, 689, 819, 699]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[120]: text=7.88, bbox=[864, 689, 896, 699]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[121]: text=FEV6/FVC%, bbox=[112, 701, 194, 711]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[122]: text=%, bbox=[208, 701, 219, 711]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[123]: text=99.0, bbox=[466, 701, 498, 711]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[124]: text=99.4, bbox=[664, 701, 696, 711]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[125]: text=100.0, bbox=[856, 701, 896, 711]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[126]: text=FEF25-75%, bbox=[112, 713, 190, 723]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[127]: text=l/sec, bbox=[208, 713, 239, 723]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[128]: text=4.47, bbox=[286, 713, 318, 723]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[129]: text=1.88, bbox=[338, 713, 370, 723]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[130]: text=42, bbox=[414, 713, 431, 723]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[131]: text=2.59, bbox=[466, 713, 498, 723]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[132]: text=58, bbox=[544, 713, 559, 723]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[133]: text=+37.8, bbox=[586, 713, 627, 723]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[134]: text=2.31, bbox=[664, 713, 696, 723]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[135]: text=52, bbox=[742, 713, 757, 723]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[136]: text=+22.8, bbox=[786, 713, 828, 723]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[137]: text=2.52, bbox=[864, 713, 896, 723]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[138]: text=FEV3, bbox=[112, 725, 149, 735]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[139]: text=l(btps), bbox=[208, 725, 247, 735]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[140]: text=3.25, bbox=[338, 725, 370, 735]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[141]: text=3.44, bbox=[466, 725, 498, 735]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[142]: text=+5.8, bbox=[586, 725, 619, 735]
2026-08-10 11:39:51,880 INFO     29 [qwen-vl-text] coord item[143]: text=3.94, bbox=[664, 725, 696, 735]
2026-08-10 11:39:51,881 INFO     29 [qwen-vl-text] coord item[144]: text=+21.3, bbox=[786, 725, 828, 735]
2026-08-10 11:39:51,881 INFO     29 [qwen-vl-text] coord item[145]: text=3.78, bbox=[864, 725, 896, 735]
2026-08-10 11:39:51,881 INFO     29 [qwen-vl-text] coord item[146]: text=FEV3/FVC%, bbox=[112, 737, 194, 747]
2026-08-10 11:39:51,881 INFO     29 [qwen-vl-text] coord item[147]: text=%, bbox=[208, 737, 219, 747]
2026-08-10 11:39:51,881 INFO     29 [qwen-vl-text] coord item[148]: text=93.3, bbox=[338, 737, 370, 747]
2026-08-10 11:39:51,881 INFO     29 [qwen-vl-text] coord item[149]: text=92.4, bbox=[466, 737, 498, 747]
2026-08-10 11:39:51,881 INFO     29 [qwen-vl-text] coord item[150]: text=-1.0, bbox=[586, 737, 619, 747]
2026-08-10 11:39:51,881 INFO     29 [qwen-vl-text] coord item[151]: text=92.9, bbox=[664, 737, 696, 747]
2026-08-10 11:39:51,881 INFO     29 [qwen-vl-text] coord item[152]: text=-0.5, bbox=[786, 737, 819, 747]
2026-08-10 11:39:51,881 INFO     29 [qwen-vl-text] coord item[153]: text=92.1, bbox=[864, 737, 896, 747]
2026-08-10 11:39:51,881 INFO     29 [qwen-vl-text] coord item[154]: text=FEV1/FEV6%, bbox=[112, 749, 200, 759]
2026-08-10 11:39:51,918 INFO     29 [qwen-vl-text] page=15 — 234/243 coords, api_time=64.6s
2026-08-10 11:39:51,918 INFO     29 [qwen-vl-text] new_positions (243):
[[15, 242.165, 380.205, 37.048, 49.678], [15, 270.72499999999997, 350.455, 50.519999999999996, 63.15], [15, 186.23499999999999, 438.515, 63.992, 76.622], [15, 73.185, 111.86, 80.832, 90.93599999999999], [15, 64.855, 89.25, 98.514, 109.46], [15, 64.855, 110.07499999999999, 110.30199999999999, 121.24799999999999], [15, 64.855, 78.53999999999999, 122.08999999999999, 133.036], [15, 64.855, 158.86499999999998, 133.878, 143.982], [15, 64.855, 149.345, 144.82399999999998, 155.76999999999998], [15, 241.57, 337.365, 98.514, 109.46], [15, 241.57, 310.59, 110.30199999999999, 121.24799999999999], [15, 241.57, 325.465, 122.08999999999999, 133.036], [15, 241.57, 327.84499999999997, 133.036, 143.982], [15, 241.57, 286.195, 144.82399999999998, 155.76999999999998], [15, 449.22499999999997, 519.435, 98.514, 109.46], [15, 449.22499999999997, 527.765, 110.30199999999999, 121.24799999999999], [15, 449.22499999999997, 532.525, 122.08999999999999, 133.036], [15, 449.22499999999997, 527.765, 133.036, 143.982], [15, 449.22499999999997, 556.92, 144.82399999999998, 155.76999999999998], [15, 116.02499999999999, 262.395, 160.822, 171.768], [15, 75.565, 93.41499999999999, 172.60999999999999, 181.87199999999999], [15, 315.945, 330.22499999999997, 160.822, 171.768], [15, 207.06, 306.425, 172.60999999999999, 180.188], [15, 142.79999999999998, 306.425, 181.03, 188.608], [15, 142.79999999999998, 306.425, 189.45, 197.028], [15, 142.79999999999998, 306.425, 197.87, 205.44799999999998], [15, 387.94, 553.35, 170.084, 177.662], [15, 387.94, 553.35, 178.504, 186.082], [15, 387.94, 553.35, 186.924, 194.50199999999998], [15, 528.36, 544.425, 224.814, 232.392], [15, 279.65, 295.12, 245.022, 252.6], [15, 116.02499999999999, 148.75, 262.704, 271.12399999999997], [15, 147.56, 180.88, 301.436, 309.856], [15, 180.285, 212.415, 338.484, 346.904], [15, 212.415, 228.48, 367.954, 375.532], [15, 292.74, 308.805, 375.532, 383.952], [15, 358.78499999999997, 377.825, 237.444, 245.864], [15, 442.68, 459.935, 306.488, 314.066], [15, 540.855, 560.49, 314.066, 322.486], [15, 323.085, 560.49, 314.066, 322.486], [15, 364.73499999999996, 424.83, 401.63399999999996, 430.262], [15, 363.54499999999996, 411.74, 452.996, 494.25399999999996], [15, 390.91499999999996, 468.85999999999996, 492.57, 508.568], [15, 66.64, 109.47999999999999, 514.462, 522.04], [15, 123.75999999999999, 136.85, 514.462, 522.04], [15, 164.815, 186.23499999999999, 514.462, 522.04], [15, 195.755, 227.885, 514.462, 522.04], [15, 236.81, 264.775, 514.462, 522.04], [15, 272.51, 304.04499999999996, 514.462, 522.04], [15, 312.96999999999997, 340.34, 514.462, 522.04], [15, 348.66999999999996, 381.99, 514.462, 522.04], [15, 389.72499999999997, 421.85499999999996, 514.462, 522.04], [15, 430.78, 458.15, 514.462, 522.04], [15, 466.47999999999996, 500.395, 514.462, 522.04], [15, 508.72499999999997, 540.855, 514.462, 522.04], [15, 549.78, 562.87, 514.462, 522.04], [15, 66.64, 84.49, 528.776, 537.196], [15, 123.75999999999999, 146.965, 528.776, 537.196], [15, 170.17, 189.20999999999998, 528.776, 537.196], [15, 201.10999999999999, 220.14999999999998, 528.776, 537.196], [15, 246.32999999999998, 256.445, 528.776, 537.196], [15, 277.27, 296.31, 528.776, 537.196], [15, 323.68, 332.60499999999996, 528.776, 537.196], [15, 348.66999999999996, 368.305, 528.776, 537.196], [15, 395.08, 414.12, 528.776, 537.196], [15, 441.48999999999995, 450.41499999999996, 528.776, 537.196], [15, 467.66999999999996, 492.65999999999997, 528.776, 537.196], [15, 514.0799999999999, 533.12, 528.776, 537.196], [15, 66.64, 87.46499999999999, 539.722, 548.1419999999999], [15, 123.75999999999999, 146.965, 539.722, 548.1419999999999], [15, 170.17, 189.20999999999998, 539.722, 548.1419999999999], [15, 201.10999999999999, 220.14999999999998, 539.722, 548.1419999999999], [15, 246.32999999999998, 256.445, 539.722, 548.1419999999999], [15, 277.27, 296.31, 539.722, 548.1419999999999], [15, 323.68, 332.60499999999996, 539.722, 548.1419999999999], [15, 348.66999999999996, 373.065, 539.722, 548.1419999999999], [15, 395.08, 414.12, 539.722, 548.1419999999999], [15, 441.48999999999995, 450.41499999999996, 539.722, 548.1419999999999], [15, 467.66999999999996, 492.65999999999997, 539.722, 548.1419999999999], [15, 514.0799999999999, 533.12, 539.722, 548.1419999999999], [15, 66.64, 115.42999999999999, 549.826, 558.246], [15, 123.75999999999999, 130.305, 549.826, 558.246], [15, 170.17, 189.20999999999998, 549.826, 558.246], [15, 201.10999999999999, 220.14999999999998, 549.826, 558.246], [15, 246.32999999999998, 256.445, 549.826, 558.246], [15, 277.27, 296.31, 549.826, 558.246], [15, 323.68, 332.60499999999996, 549.826, 558.246], [15, 348.66999999999996, 368.305, 549.826, 558.246], [15, 395.08, 414.12, 549.826, 558.246], [15, 441.48999999999995, 450.41499999999996, 549.826, 558.246], [15, 467.66999999999996, 481.95, 549.826, 558.246], [15, 514.0799999999999, 533.12, 549.826, 558.246], [15, 66.64, 83.3, 559.93, 568.35], [15, 123.75999999999999, 142.20499999999998, 559.93, 568.35], [15, 170.17, 189.20999999999998, 559.93, 568.35], [15, 201.10999999999999, 220.14999999999998, 559.93, 568.35], [15, 241.57, 256.445, 559.93, 568.35], [15, 277.27, 296.31, 559.93, 568.35], [15, 318.325, 332.60499999999996, 559.93, 568.35], [15, 348.66999999999996, 368.305, 559.93, 568.35], [15, 389.72499999999997, 414.12, 559.93, 568.35], [15, 436.72999999999996, 450.41499999999996, 559.93, 568.35], [15, 467.66999999999996, 487.30499999999995, 559.93, 568.35], [15, 509.32, 533.12, 559.93, 568.35], [15, 555.73, 560.49, 559.93, 568.35], [15, 66.64, 88.06, 570.034, 578.454], [15, 123.75999999999999, 146.965, 570.034, 578.454], [15, 170.17, 189.20999999999998, 570.034, 578.454], [15, 277.27, 296.31, 570.034, 578.454], [15, 323.68, 332.60499999999996, 570.034, 578.454], [15, 395.08, 414.12, 570.034, 578.454], [15, 441.48999999999995, 450.41499999999996, 570.034, 578.454], [15, 514.0799999999999, 533.12, 570.034, 578.454], [15, 66.64, 80.325, 580.138, 588.558], [15, 123.75999999999999, 142.20499999999998, 580.138, 588.558], [15, 201.10999999999999, 220.14999999999998, 580.138, 588.558], [15, 277.27, 296.31, 580.138, 588.558], [15, 348.66999999999996, 368.305, 580.138, 588.558], [15, 395.08, 414.12, 580.138, 588.558], [15, 467.66999999999996, 487.30499999999995, 580.138, 588.558], [15, 514.0799999999999, 533.12, 580.138, 588.558], [15, 66.64, 115.42999999999999, 590.242, 598.662], [15, 123.75999999999999, 130.305, 590.242, 598.662], [15, 277.27, 296.31, 590.242, 598.662], [15, 395.08, 414.12, 590.242, 598.662], [15, 509.32, 533.12, 590.242, 598.662], [15, 66.64, 113.05, 600.346, 608.766], [15, 123.75999999999999, 142.20499999999998, 600.346, 608.766], [15, 170.17, 189.20999999999998, 600.346, 608.766], [15, 201.10999999999999, 220.14999999999998, 600.346, 608.766], [15, 246.32999999999998, 256.445, 600.346, 608.766], [15, 277.27, 296.31, 600.346, 608.766], [15, 323.68, 332.60499999999996, 600.346, 608.766], [15, 348.66999999999996, 373.065, 600.346, 608.766], [15, 395.08, 414.12, 600.346, 608.766], [15, 441.48999999999995, 450.41499999999996, 600.346, 608.766], [15, 467.66999999999996, 492.65999999999997, 600.346, 608.766], [15, 514.0799999999999, 533.12, 600.346, 608.766], [15, 66.64, 88.655, 610.4499999999999, 618.87], [15, 123.75999999999999, 146.965, 610.4499999999999, 618.87], [15, 201.10999999999999, 220.14999999999998, 610.4499999999999, 618.87], [15, 277.27, 296.31, 610.4499999999999, 618.87], [15, 348.66999999999996, 368.305, 610.4499999999999, 618.87], [15, 395.08, 414.12, 610.4499999999999, 618.87], [15, 467.66999999999996, 492.65999999999997, 610.4499999999999, 618.87], [15, 514.0799999999999, 533.12, 610.4499999999999, 618.87], [15, 66.64, 115.42999999999999, 620.554, 628.9739999999999], [15, 123.75999999999999, 130.305, 620.554, 628.9739999999999], [15, 201.10999999999999, 220.14999999999998, 620.554, 628.9739999999999], [15, 277.27, 296.31, 620.554, 628.9739999999999], [15, 348.66999999999996, 368.305, 620.554, 628.9739999999999], [15, 395.08, 414.12, 620.554, 628.9739999999999], [15, 467.66999999999996, 487.30499999999995, 620.554, 628.9739999999999], [15, 514.0799999999999, 533.12, 620.554, 628.9739999999999], [15, 66.64, 119.0, 630.658, 639.078], [15, 66.64, 119.0, 630.658, 639.078], [15, 123.75999999999999, 130.305, 620.554, 628.9739999999999], [15, 277.27, 296.31, 549.826, 558.246], [15, 170.17, 189.20999999999998, 528.776, 537.196], [15, 514.0799999999999, 533.12, 549.826, 558.246], [15, 116.02499999999999, 148.75, 262.704, 271.12399999999997], [15, 123.75999999999999, 142.20499999999998, 600.346, 608.766], [15, 348.66999999999996, 368.305, 528.776, 537.196], [15, 348.66999999999996, 368.305, 528.776, 537.196], [15, 323.68, 332.60499999999996, 570.034, 578.454], [15, 201.10999999999999, 220.14999999999998, 559.93, 568.35], [15, 241.57, 256.445, 559.93, 568.35], [15, 348.66999999999996, 373.065, 539.722, 548.1419999999999], [15, 201.10999999999999, 220.14999999999998, 549.826, 558.246], [15, 441.48999999999995, 450.41499999999996, 549.826, 558.246], [15, 467.66999999999996, 487.30499999999995, 559.93, 568.35], [15, 170.17, 189.20999999999998, 570.034, 578.454], [15, 147.56, 180.88, 301.436, 309.856], [15, 123.75999999999999, 142.20499999999998, 600.346, 608.766], [15, 170.17, 189.20999999999998, 570.034, 578.454], [15, 201.10999999999999, 220.14999999999998, 539.722, 548.1419999999999], [15, 323.68, 332.60499999999996, 600.346, 608.766], [15, 201.10999999999999, 220.14999999999998, 528.776, 537.196], [15, 323.68, 332.60499999999996, 528.776, 537.196], [15, 348.66999999999996, 368.305, 610.4499999999999, 618.87], [15, 201.10999999999999, 220.14999999999998, 528.776, 537.196], [15, 441.48999999999995, 450.41499999999996, 539.722, 548.1419999999999], [15, 348.66999999999996, 373.065, 539.722, 548.1419999999999], [15, 201.10999999999999, 220.14999999999998, 528.776, 537.196], [15, 180.285, 212.415, 338.484, 346.904], [15, 123.75999999999999, 142.20499999999998, 600.346, 608.766], [15, 201.10999999999999, 220.14999999999998, 539.722, 548.1419999999999], [15, 170.17, 189.20999999999998, 528.776, 537.196], [15, 323.68, 332.60499999999996, 570.034, 578.454], [15, 467.66999999999996, 487.30499999999995, 620.554, 628.9739999999999], [15, 246.32999999999998, 256.445, 600.346, 608.766], [15, 348.66999999999996, 368.305, 528.776, 537.196], [15, 389.72499999999997, 414.12, 559.93, 568.35], [15, 323.68, 332.60499999999996, 528.776, 537.196], [15, 348.66999999999996, 368.305, 528.776, 537.196], [15, 170.17, 189.20999999999998, 528.776, 537.196], [15, 0, 0, 0, 0], [15, 123.75999999999999, 142.20499999999998, 600.346, 608.766], [15, 467.66999999999996, 481.95, 549.826, 558.246], [15, 170.17, 189.20999999999998, 528.776, 537.196], [15, 467.66999999999996, 492.65999999999997, 600.346, 608.766], [15, 348.66999999999996, 368.305, 528.776, 537.196], [15, 348.66999999999996, 368.305, 549.826, 558.246], [15, 348.66999999999996, 368.305, 528.776, 537.196], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 201.10999999999999, 220.14999999999998, 539.722, 548.1419999999999], [15, 436.72999999999996, 450.41499999999996, 559.93, 568.35], [15, 436.72999999999996, 450.41499999999996, 559.93, 568.35], [15, 0, 0, 0, 0], [15, 123.75999999999999, 146.965, 610.4499999999999, 618.87], [15, 201.10999999999999, 220.14999999999998, 580.138, 588.558], [15, 201.10999999999999, 220.14999999999998, 528.776, 537.196], [15, 348.66999999999996, 368.305, 559.93, 568.35], [15, 514.0799999999999, 533.12, 539.722, 548.1419999999999], [15, 170.17, 189.20999999999998, 570.034, 578.454], [15, 514.0799999999999, 533.12, 539.722, 548.1419999999999], [15, 66.64, 84.49, 528.776, 537.196], [15, 123.75999999999999, 146.965, 610.4499999999999, 618.87], [15, 395.08, 414.12, 528.776, 537.196], [15, 170.17, 189.20999999999998, 528.776, 537.196], [15, 201.10999999999999, 220.14999999999998, 559.93, 568.35], [15, 514.0799999999999, 533.12, 570.034, 578.454], [15, 170.17, 189.20999999999998, 570.034, 578.454], [15, 395.08, 414.12, 528.776, 537.196], [15, 66.64, 83.3, 559.93, 568.35], [15, 0, 0, 0, 0], [15, 467.66999999999996, 487.30499999999995, 559.93, 568.35], [15, 389.72499999999997, 414.12, 559.93, 568.35], [15, 241.57, 256.445, 559.93, 568.35], [15, 277.27, 296.31, 590.242, 598.662], [15, 318.325, 332.60499999999996, 559.93, 568.35], [15, 348.66999999999996, 368.305, 559.93, 568.35], [15, 201.10999999999999, 220.14999999999998, 539.722, 548.1419999999999], [15, 436.72999999999996, 450.41499999999996, 559.93, 568.35], [15, 467.66999999999996, 487.30499999999995, 559.93, 568.35], [15, 348.66999999999996, 368.305, 528.776, 537.196], [15, 555.73, 560.49, 559.93, 568.35], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 241.57, 337.365, 98.514, 109.46], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0]]
2026-08-10 11:39:51,918 INFO     29 [qwen-vl-text] ═══ DONE ═══ 243 positions, pages=1, time=78.5s
2026-08-10 11:39:51,934 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 11:39:51,935 INFO     29 [Trace] task=ea51b5dc | doc=LZK 哮喘 广三(2).pdf | Extractor:ExaminationReport | outputs={"chunks": "3 items, types={'ExaminationReport': 3}", "html": "", "json": "1039 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(2).pdf", "output_format": "chunks", "chunks_Clinical": "5 items, types={'OutpatientRecord': 5}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 5, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-10 11:39:51,935 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 11:39:51,935 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:39:51.935+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 23, "failed": 0, "current": {"ea51b5dc94ae11f1bd9827cf206dfa2d": {"id": "ea51b5dc94ae11f1bd9827cf206dfa2d", "doc_id": "ea1b0b1894ae11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786361440167, "task_type": "dataflow", "root_trace_id": "bca8d639df704cd29f0107370613ab01", "root_traceparent": "00-bca8d639df704cd29f0107370613ab01-b8b3c91a32048c1c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:39:51,943 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:39:51,943 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:39:52,854 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:39:52,866 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 11:39:52,867 INFO     29 [Trace] task=ea51b5dc | doc=LZK 哮喘 广三(2).pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "1039 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(2).pdf", "output_format": "chunks", "chunks_Clinical": "5 items, types={'OutpatientRecord': 5}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 5, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-10 11:39:52,867 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 11:39:52,869 INFO     29 [ChunkMerger] Merged 15 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 5, 'Extractor:Medication': 1, 'Extractor:Prescription': 7, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 3, 'Extractor:Progress': 1} (filtered 6 noise chunks)
2026-08-10 11:39:52,880 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 11:39:52,880 INFO     29 [Trace] task=ea51b5dc | doc=LZK 哮喘 广三(2).pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "15 items, types={'OutpatientRecord': 5, 'PrescriptionRecord': 7, 'ExaminationReport': 3}", "name": "LZK 哮喘 广三(2).pdf"}
2026-08-10 11:39:52,880 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 11:39:53,033 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786361443493, 'update_date': datetime.datetime(2026, 8, 10, 11, 30, 43), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 927168, 'status': '1'}
2026-08-10 11:39:53,290 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=病历编号：
性别：男
年龄：40岁
就诊科室：内科门诊（荔湾）
就诊时间：2025-10-10 14:36:06
主诉：BAIYUN V8
现病史：自上次访视至今，询问及查询HIS系统受试者有新增AE，无SAE、哮喘急性发作，有新增合并用药，发生2次医疗相关事件[2025年9月3日因过敏性鼻炎就诊专科门诊、本周曾因上呼吸道感染到社区医院就诊(具体不详，因HIS系统滞后无法收集具体情况及受试者无法回忆起当时情况及用药情况，待收集具体情况后补充详情)]。于2025年8月4日、2025年9月1日收到加重警报邮件，联系受试者后，均判断非哮喘急性发作。
完成下流操作：
1、查看受试者电子日志，受试者漏填2025年8月16日，2025年9月4日晚间日志，2025年9月4日、2025年9月25日早间日志；
2、填写AQLQ+12和ACQ-5问卷，ACQ-5评分：0.8分；
3、休息10分钟后，测量坐位生命体征：血压113/81mmHg，脉搏87次/分，呼吸频率20次/分，体温36.6℃，测量身高177.5cm，体重90.5kg(BMI=28.7kg/m2)；
4、14:35体格检查：神志清，体查合作，自主体位，一般外表无异常，皮肤、粘膜无异常，唇甲无发绀，眼睛、耳、鼻、咽喉无异常，口咽部粘膜无异常，颈软，气管居中，甲状腺未及肿大，全身浅表淋巴结未及肿大，颈静脉无怒张，胸廓无畸形，双肺呼吸运动对称，双肺触觉语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及啰音。心前区无隆起，心尖搏动无弥散，心界不大，心率：87次/分，律齐，各瓣膜听诊区未闻及病理性杂音。腹平软，全腹无压痛、反跳痛。肝、脾肋下未及，肝肾区无叩击痛，肠鸣音存，4次/分，脊柱、四肢无畸形，生理征存，未引出病理征，其他系统未见明显异常；
5、休息至少10分钟后，于14:58行12导联ECG检查；
6、于15:01采集中心实验室样本(血常规，血生化)并送往中心试验室；
7、回收试验药物BDAMDI@ASMDI3盒(152968-AH及185936-HK未开封，148729-UA未用60揿，实际使用46揿，发药当天预喷4揿，2025年9月10日前因超过7天未使用试验药物空喷2次共4揿，2025年9月10日后受试者每七天清洗一次后空喷5次共10揿，总计预喷18揿；epro记录使用总共46揿，与实际使用情况一致。
8、回收epro以及AM3。
既往史：更新合并用药：
1、糠酸莫米松鼻喷雾剂2025.4.3-2025.7.25 每鼻 2喷/次 qm 治疗过敏性鼻炎。
病历文书
门诊病历
25/10/10 14时 门诊病历
25/10/24 15时 门诊病历（GCP专用）
25/11/17 10时 门诊病历
头降使用40瓶，平均每天使用4瓶，2025年9月10日用完4瓶（大木使用试验药剂空瓶2次共4
瓶，2025年9月10日后受试者每七天青光一次后空瓶5次共10瓶，总计空瓶10瓶（qrs记录使
用总共46瓶，与实际使用情况一致。
8、回访qrs以及MD。
既往史：更新合并用药：
1、鼻腔莫米松鼻喷雾剂C025 4 3-2025 7 25 每鼻 2喷/次 qd 治疗过敏性鼻炎。
2、苯环喹氯桉鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。
4、氯卓斯汀氟替卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。
5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/
次 治疗过敏性鼻炎。
6、枯草抗感染治疗（生理盐水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过
敏性鼻炎
已预约受试者安全性随访时间。
过敏史：
个人史：
体格检查：
专科情况：
辅助检查：
治疗项目：
门诊诊断：
支气管哮喘
单病种：
发病时间：
处
置：
1心电图（心电图室做）
2布地奈德福莫特罗吸入粉雾剂(II)(省采)●①② 2盒2000,日入用药,一天2次
30天
备注：
病情评估：
病情分级：
是否抢救病例：否
是否抢救成功：
是否为绿色通道患者：否
病人去向：
CS 扫描全能王
3亿人都在用的扫描App
---
就诊卡
流水号：
姓名
龄：40岁
就诊科
日：2025-10-24 15:45:39
主诉：安全性电话随访
现病史：今日10:27
固定电话（020-
（159
5），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无
不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对
V8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试
者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，
目前无安全性异常表现。
合并用药更新：
1、小柴胡颗粒、（自行购药）2025.10.6-2025.10.8 10g tid 治疗上呼吸道感染
2、苯环喹溴铵鼻喷雾剂 2025.4.3-至今 每鼻2喷/次 qid 治疗过敏性鼻炎
3、氮卓斯汀氟替卡松鼻喷雾剂 2025.9.3-至今 每鼻2喷/次 bid 治疗过敏性鼻炎
4、辛芩颗粒 2024.8.21-2024.8.27 1袋 冲服 tid 治疗过敏性鼻炎
AE：
上呼吸道感染 2025年10月5日-2025年10月8日 中度，非SAE，采取药物治疗措施，对试验
药物采取措施：剂量不变，与试验药物无关，未因该AE退出研究。
病历更正：
1、更正2024年10月22日病历，合并用药“辛芩颗粒”为“辛芩颗粒”；
2、更正2024年10月22日病历，合并用药“苯环喹溴铵鼻喷雾剂”为“苯环喹溴铵鼻喷雾
剂”；
3、更正2026年1月24日病历，“无收到ePro触发的哮喘警报邮件”为“有收到ePro触发的哮
喘警报邮件”；
4、更正2025年7月18日病历，“受试者漏填2025年4月28日晚间日志” 更正为：“受试者
漏填2025年4月28日早间日志”；
5、更正2024年11月6日病历，“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共
计用了26喷”为：“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了28
喷”。
随行中·
---
病历编号：
姓名：
性别：
年龄：40岁
就诊科室：
就诊时间：2025-11-17 10:10:48
主诉：支气管哮喘治疗后复查：
现病史：2021年2月前开始出现咳嗽、咯痰，粘白，量中，能咯出，咳嗽呈阵发性、刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏。无咽痛，无伴反酸、嗳气、腹胀。无上腹部隐痛不适感，无伴发热、畏寒，影响睡眠。晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：
12.52*109/L 嗜酸粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定。本次门诊距上次门诊间隔时间30天。症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确。急性发作情况：两次，就诊期间急性发作：无，发作次数：0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。近3天来出现咽痛不适
既往史：鼻炎病史无规则治疗。打鼾明显。
过敏史：未发现。
个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。
体格检查：神志清，颈软，双肺呼吸音粗，未闻及明显干、湿性罗音，口腔粘膜无白斑。
专科情况：
辅助检查：
治疗项目：
门诊诊断：
1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、阻塞性睡眠呼吸暂停低通气综合征,4、急性咽炎
单病种：
发病时间：
处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不适随诊。
1金银花口服液◆⑤ 2盒 20.0ml,口服,一天3次(口服) 6天
2氨卓斯汀氟替卡松鼻喷雾剂◆ 1瓶 2.0喷,喷鼻,一天2次 30天
3苯环喹溴铵鼻喷雾剂◆ 3瓶 2.0喷,喷鼻,一天4次 30天
备注：建议在住地附近社区医疗机构随诊。
---
广州医科大学附属第三医院
The Third Affiliated Hospital of Guangzhou Medical University
门(急)诊病历信息
就诊卡
流水
姓
病历编号:
年 龄:41岁
就诊科室:内科门诊(荔湾) 医
就诊时间:2026-01-05 17:07:54
主 诉:支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天
现 病 史:2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激
性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流
涕、喷嚏,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响
睡眠,晨起有咽干,曾到本院就诊两次,症状不见明显缓解。2021-1-9血常规:白细胞:
12.52*109/L 嗜酸粒细胞:0.65*109/L 5.2%,经治疗后症状明显缓解。无咳嗽、咯痰、气
促。病情稳定,本次门诊距上次门诊间隔时间30天。症状控制情况:过去4周,患者:吸入
药物使用情况:遵医嘱使用;吸入装置使用情况:正确。急性发作情况:两次,就诊期间急
性发作:无,发作次数:0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。长期规律使用信必
可160/4.5ug 2吸 bid治疗,5天前开始出现咳嗽、咯痰,黄白痰,量少,难以咯出,咳嗽以
夜间为主。无气促,伴咽息,鼻塞、流涕、喷嚏,无发热。
既 往 史:鼻炎病史无规则治疗。打鼾明显。
过 敏 史:未发现;
个 人 史:否认遗传病史,吸烟10年,20支/日,2018年戒烟。偶饮酒。2021-12-20已打第
三针新冠疫苗。
体格检查:神志清,颈软,双肺呼吸音粗,可闻及散在哮鸣音,口腔粘膜无白斑。
专科情况:
辅助检查:
治疗项目:
门诊诊断:
1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎
处 置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。
布地奈德福莫特罗吸入粉雾剂(II)2盒 2.0吸,吸入用药,一天2次 30天
(省采)●①⑤
左氧氟沙星片(省采)●⑥ 5片 0.5g,口服,每日1次(口服) 5天
第1页
广州医科大学附属第三医院
The Third Affiliated Hospital of Guangzhou Medical University
门(急)诊病历信息
复方甲氧那明胶囊(省采)◆② 1瓶 1.0粒,餐后口服,一天3次(口服) 5天
盐酸氨溴索分散片(省采)●⑥ 15片 30.0mg,餐后口服,一天3次(口服) 5
天
醋酸泼尼松片●②④ 6片 10.0mg,口服,每早1次(口服) 3天
备 注:建议在住地附近社区医疗机构随诊。
---
门诊/住院病历信息
就诊卡号：
病历编号：
流水号
姓名
性别：男
年龄：41岁
就诊科室：内科门诊（荔湾）
就诊时间：2026-02-04 11:21:11
主诉：支气管哮喘治疗后复查
现病史：2021年2月前开始出现咳嗽、咳痰，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sng 2吸 bid治疗。
既往史：鼻炎病史无规则治疗，打鼾明显。
过敏史：未发现；
个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。
体格检查：神志清，颈软，双肺呼吸音粗，可闻及散在哮鸣音，口腔粘膜无白斑。
专科情况：
辅助检查：
治疗项目：
门诊诊断：
1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、急性气管支气管炎
单病种：
发病时间：
处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不遥随诊。
布地奈德福莫特罗吸入粉雾剂(II)(省
2 2.0班，吸入用药，一天2次
30
采)●①②
查天
---
门(急)诊处方
就诊时间:2025-07-18
就诊科室:内科门诊
主诊医
姓名
性别:男
年龄:40岁
卡号:
患者
医疗证号:
处方号
地址:PT027气雾剂 2024017-呼吸科
身份证
诊断:支气管哮喘
西药处方
组号
项目名称
规格
总量
单价
金额
R:
布地奈德福莫特罗吸入粉雾剂0.125/0.0006*60吸6盒
183.41100.46
Sig
2吸/次,吸入,bid*90天
---
门(急)诊处方
就诊时间:2025-04-25
就诊科室:内科门诊
主诊
姓名
性别:男
年龄:40岁
卡号:
患者类型:GLP支付
医疗证号:
处方号
地址:PT027气雾剂 2024017-呼吸科
身份证号:
诊断:支气管哮喘
西药处方
组号
项目名称
规格
总量
单价
金额
R:
布地奈德福莫特罗吸入粉雾剂(II)●●@ug*60吸6盒
183.41100.46
Sig
2吸/次,吸入,bid*90天
---
门(急)诊处方
就诊时间：2025-02-26
就诊科室：内科门诊
主诊
性别：男
年龄：40岁
卡号
医疗证号：
处方
015
地址：PT027气雾剂 2024017-呼吸科
身份证号：
诊断：支气管哮喘
西药处方
组号
项目名称
规格
总量
单价
金额
R:
布地奈德福莫特罗吸入粉雾剂BUD/●@1g*60吸2盒
183.41
366.82
Sig
2吸/次,吸入,bid*30天
---
门(急)诊处方
就诊时间:2025-01-24
就诊科室:内科门诊
主诊医
姓名
性别:男
年龄:40岁
卡号:4
患者类型:GCP支付
医疗证号:
处方号:
地址:PT027气雾剂 2024017-呼吸科
身份证号:
诊断:支气管哮喘
西药处方
组号
项目名称
规格
总量
单价
金额
R:
布地奈德福莫特罗吸入粉雾剂HIV●@1ug*60吸4盒
183.41 733.64
Sig
2吸/次,吸入,bid*60天
---
门(急)诊处方
就诊时间:2025-01-03
就诊科室:内科门诊
主诊
性别:男
年龄:40岁
卡号
患者类型:GCP支付
医疗证号:
处方
地址:PT027气雾剂 2024017-呼吸科
身份证号:
诊断:支气管哮喘
西药处方
组号
项目名称
规格
总量
单价
金额
R:
布地奈德福莫特罗吸入粉雾剂(Ⅱ)●●60ug*60吸2盒
183.41 366.82
Sig
2吸/次,吸入,bid*30天
医师:
医生编号:1326
配剂人:
核对人:
合计:
收费员:
---
门(急)诊处方
就诊时间:2024-12-04
就诊科室:内科门诊
姓名
性别:男
年龄:39岁
卡号
患者
医疗证号:
处方
地址:PT027气雾剂 2024017-呼吸科
身份证号:
诊断:支气管哮喘
西药处方
组号
项目名称
规格
总量
单价
金额
R:
布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●(50ug*60吸2盒
183.41 366.82
Sig
2吸/次,吸入,bid*30天
---
广州医科大学附属第三医院
处方笺
普通
诊疗卡
患者姓名
年龄：41岁
费别：南医保
科室：内科门诊（荔湾）
日期：2026-01-05 17:17:14
处方号
地址：荔湾
2024017-呼吸科
联系电话
身份号码：
2739
诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],急性气管支气管炎
R
P:
布地奈德福莫特罗吸入粉雾剂(II) 160ug/4.5ug*60吸
2盒
剂量：每次2吸
（
1
30
盒）
用法：吸入用药
bid
01-05
处方金额：366.82元
取药药房：门诊西药房（荔湾）
---
激发试验检查报告
姓名：
测试号：
门诊/住院号：
000
年龄：
出生日期：
19
性别：
男
身高：
170
病区：
内科门诊
体重：
81 kg
机器编号：
床号：
电话：
Pred
A1
A1/Pd
NS
P1 chg%1
P2 chg%2
P3 chg%3
FVC
[L]
4.84
4.69
97.1
4.29
4.22
-10.1
3.64
-22.5
4.01
-14.6
PEV 1
[L]
4.01
3.05
76.2
2.72
2.69
-11.8
2.24
-26.5
2.44
-20.0
PEV 1 % PVC
[%]
83.32
65.02
78.0
63.54
63.83
-1.82
61.73
-5.06
60.92
-6.30
PEV 1 % VC MAX
[%]
80.55
64.94
80.6
62.34
63.83
-1.70
61.73
-4.94
60.92
-6.18
VC MAX
[L]
5.05
4.70
93.1
4.37
4.22
-10.2
3.64
-22.6
4.01
-14.7
PEP
[L/s]
9.37
9.95
106.2
9.06
7.81
-21.5
6.73
-32.3
8.22
-17.4
MMEF 75/25
[L/s]
4.52
1.54
34.1
1.33
1.34
-12.9
1.14
-25.8
1.23
-20.0
MEF 50
[L/s]
5.17
1.97
38.1
1.66
1.71
-13.4
1.34
-31.8
1.42
-28.0
MEF 25
[L/s]
2.29
0.58
25.5
0.52
0.53
-9.87
0.50
-14.6
0.49
-15.7
PET
[s]
6.72
6.87
6.93
3.16
6.75
0.57
6.74
0.38
V backextrapolation ex
[L]
0.13
0.09
0.10
-20.0
0.08
-41.6
0.08
-38.5
PIF
[L/s]
8.04
7.96
7.58
-5.76
6.16
-23.3
7.78
-3.20
FIF 50
[L/s]
7.99
7.86
7.16
-10.3
5.36
-32.9
7.08
-11.3
MVV
[L/min]
141.88
BF MVV
[1/min]
Cumulated dose
0.072 0.078
0.312
2 Puf
F/V ex
F/V in
Vol [L]
Vol%VCmax
VCmax
Time [s]
PD[-20] FEV 1: 0.2117 mg Cumulated
PD[-20] PEF: < 0.078 mg Cumulated
PD[] FEV1%I: could not be calculated!
意见：
2022/6/08 10:23:56上午
1.轻度阻塞性通气功能障碍。
2.支气管激发试验阳性(累计吸入乙酰甲胆碱0.312mg，FEV1下降大于20%，PD20=0.2117mg，气道高反应性(AHR)为中度
通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后FEV1恢复至预计值80%。
---
检查日期：2021/1/21
检查时间：16:43
编号：16
广州医科大学附属第三医院
支气管扩张试验检查报告
姓名：
测试号：
年龄：36岁
性别：男
病区：
机器编号：
门诊/住院号：
出生日期：
身高：
体重：
床号：
电话：
Pred
A1
A1/Pd
P1
A2/Pd
chg%1
P2
A3/Pd
chg%2
P3
A4/Pd
chg%3
FVC
[L]
4.86
3.48
71.5%
4.01
82.4%
15.19
4.15
85.4%
19.47
4.01
82.6%
15.47
FEV 1
[L]
4.03
1.97
48.8%
2.33
57.9%
18.59
2.33
57.8%
18.48
2.44
60.5%
24.02
FEV 1 % FVC
[%]
83.32
56.62
68.0%
58.29
70.0%
2.95
56.15
67.4%
-0.83
60.81
73.0%
7.40
FEV 1 % VC MAX
[%]
80.73
56.07
69.5%
58.29
72.2%
3.96
56.15
69.5%
0.14
60.81
75.3%
8.45
VC MAX
[L]
5.08
3.51
69.1%
4.01
78.9%
14.07
4.15
81.8%
18.31
4.01
79.1%
14.35
PEF
[L/s]
9.41
6.61
70.3%
7.99
85.0%
20.93
7.91
84.1%
19.63
8.07
85.7%
22.02
MMEF 75/25
[L/s]
4.57
0.81
17.7%
0.96
21.1%
19.59
1.03
22.6%
28.17
1.12
24.6%
39.07
MEF 50
[L/s]
5.20
1.00
19.2%
1.29
24.8%
29.25
1.30
24.9%
29.87
1.53
29.3%
52.75
MEF 25
[L/s]
2.32
0.39
16.7%
0.38
16.4%
-1.68
0.50
21.6%
29.78
0.41
17.9%
7.18
FET
[s]
15.24
6.42
-57.87
6.30
-58.63
6.55
-57.05
V backextrapolati
[L/s]
0.07
0.07
0.89
0.09
17.79
0.08
6.12
PIF
[L/s]
7.03
7.39
5.19
7.17
1.99
7.16
1.91
FIV1
[L]
3.40
3.76
10.58
3.68
8.26
3.60
5.96
PEF50 % PIF50
[%]
16.56
21.70
31.06
19.81
19.65
24.71
49.20
MVV
[L/min]
142.69
BF MVV
[1/min]
意见：
1.重度混合性肺通气功能障碍。
2.支气管舒张试验阳性。
（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后PEV1较基线增加大于12%，且绝对值增加大于200ml）
---
广州医科大学附属第三医院
肺功能检查报告
地址：广州市多宝路63号 电话：020-81292126
COSMED
姓名：
科室/床号：
ID：
出生日期：1984/12/8
预计值：ERS 93
日期：2024/10/22
性别：Male
地区修正：Chinese
详细描述：内科门诊
Company：
年龄：39
体重(Kg)：89.0
身高(cm)：177.5
BMI(Kg/m²：28.2
吸烟：曾经(10/20)
用力肺活量 Forced Vital Capacity
F(l/s)
V(l)
BEST #3 - 2024/10/22 11:03
沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38
沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39
沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41
沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38
沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39
沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41
BEST #3 - 2024/10/22 11:03
FVC
PEF
MEF75%
MEF50%
MEF25%
FVC
8V(l)
FEV1
ATS
12t(s)
-1 0 1 2 3 4 5 6 7 8 9 10 11 12t(s)
218133
ST
2024-10-22
Parameter
UM
Pred.
BEST#3
%Pred.
POST#4
%Pred.
%Test#3
POST#5
%Pred.
%Test#3
POST#6
%F
FVC
l(btps)
4.87
3.48
71
3.72
76
+6.9
4.24
87
+22.0
4.11
FEV1
l(btps)
4.01
2.58
64
2.94
73
+13.7
3.15
79
+21.9
3.15
FEV1/FVC%
%
80.2
74.3
93
79.0
98
+6.4
74.2
93
0.0
76.6
PEF
l/sec
9.37
9.86
105
9.98
107
+1.3
10.48
112
+6.3
10.52
1
FEV6
l(btps)
5.17
3.68
71
4.22
82
4.11
PIF
l/sec
7.33
7.76
+5.8
7.78
+6.1
7.88
FEV6/FVC%
%
99.0
99.4
100.0
FEF25-75%
l/sec
4.47
1.88
42
2.59
58
+37.8
2.31
52
+22.8
2.52
FEV3
l(btps)
3.25
3.44
+5.8
3.94
+21.3
3.78
FEV3/FVC%
%
93.3
92.4
-1.0
92.9
-0.5
92.1
FEV1/FEV6%
%
79.8
74.7
76.6
MEF75%
l/sec
8.09
5.96
74
9.28
115
+55.7
7.53
93
+26.3
7.17
MEF50%
l/sec
5.17
2.57
50
3.49
68
+35.8
3.08
59
+19.6
3.28
MEF25%
l/sec
2.28
0.71
31
0.95
42
+33.9
0.83
36
+16.6
0.87
FET100%
sec
6.0
6.7
+12.8
6.5
+9.4
6.5
VEXT
ml
208
192
162
IC
l(btps)
3.33
3.38
+1.5
3.50
+5.1
3.35
FIVC
l(btps)
4.29
4.70
+9.6
4.51
+5.1
4.46
PEFr
l/min
562.3
591.4
105
599.0
107
+1.3
628.8
112
+6.3
630.9
1
诊断：
中度限制性通气功能障碍。支气管舒张试验阳性（吸入沙丁胺醇400μg，FEV1上升>12%，且绝对值>200ml）。
打印2024/10/22
PFT Suite 10.0d
页 1 of 1
2026-08-10 11:39:54,166 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 11:39:54,166 INFO     29 [Trace] task=ea51b5dc | doc=LZK 哮喘 广三(2).pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "15 items, types={'OutpatientRecord': 5, 'PrescriptionRecord': 7, 'ExaminationReport': 3}", "name": "LZK 哮喘 广三(2).pdf", "embedding_token_consumption": 9028}
2026-08-10 11:39:54,166 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 11:39:54,433 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 11:39:54,433 INFO     29 [Trace] task=ea51b5dc | doc=LZK 哮喘 广三(2).pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":15,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 11:39:54,440 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:39:54,440 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:39:54,440 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:39:54,441 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:39:54,441 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:39:54,441 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:39:54,441 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:39:54,441 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:39:54,441 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:39:54,441 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:39:54,441 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:39:54,441 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:39:54,441 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:39:54,441 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:39:54,442 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:39:54,448 INFO     29 set_progress(ea51b5dc94ae11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 11:39:54 [DOC Engine]:
Start to index...
2026-08-10 11:39:54,486 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.033s]
2026-08-10 11:39:54,490 INFO     29 set_progress(ea51b5dc94ae11f1bd9827cf206dfa2d), progress: 0.8066666666666668, progress_msg: 
2026-08-10 11:39:54,516 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.019s]
2026-08-10 11:39:54,543 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.016s]
2026-08-10 11:39:54,570 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.019s]
2026-08-10 11:39:54,578 INFO     29 set_progress(ea51b5dc94ae11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 11:39:54 Indexing done (0.13s). Task done (530.77s)
2026-08-10 11:39:54,584 INFO     29 [Done], chunks(15), token(9028), elapsed:530.77
2026-08-10 11:39:54,826 INFO     29 handle_task done for task {"id": "ea51b5dc94ae11f1bd9827cf206dfa2d", "doc_id": "ea1b0b1894ae11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(2).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786361440167, "task_type": "dataflow", "root_trace_id": "bca8d639df704cd29f0107370613ab01", "root_traceparent": "00-bca8d639df704cd29f0107370613ab01-b8b3c91a32048c1c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
