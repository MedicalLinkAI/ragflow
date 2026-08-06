# 基准结果：LZK 哮喘 广三(1).pdf

## 基本信息

- 文件：`LZK 哮喘 广三(1).pdf`
- 大小：5325.3 KB
- PDF 总页数：16
- doc_id：`5963bc44913b11f19b5e81513a69a703`
- 上传方式：existing
- 状态：run=None (code=None)  progress=None
- 开始时间：2026-08-06T10:30:48  完成时间：2026-08-06T10:30:49  耗时：1.6s
- progress_msg：`02:25:19 Indexing done (0.22s). Task done (668.68s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 9e3c7cfb | 2 | 1-2 | 病历编号： 性别：男 年龄：40岁 就诊科室：内科门诊（荔湾） 就诊时间：202 |
| 2 | a6d2d8e8 | 1 | 3-3 | 就诊卡 流水号： 姓名 龄：40岁 就诊科 目：2025-10-24 15:45 |
| 3 | 017ffd0c | 1 | 4-4 | 病历编号： 姓名： 性别： 年龄：40岁 就诊科： 就诊时间：2025-11-1 |
| 4 | d93c2e56 | 1 | 5-5 | 门(急)诊处方 就诊时间:2025-07-18 就诊科室:内科门诊 主诊医 姓名 |
| 5 | fdf864ca | 1 | 6-6 | 门(急)诊处方 就诊时间:2025-04-25 就诊科室:内科门诊 主诊 姓名  |
| 6 | 9315192c | 1 | 7-7 | 门(急)诊处方 就诊时间:2025-02-26 就诊科室:内科门诊 主诊 性别: |
| 7 | 070bf89c | 1 | 8-8 | 门(急)诊处方 就诊时间:2025-01-24 就诊科室:内科门诊 主诊医 姓名 |
| 8 | 51a08747 | 1 | 9-9 | 门(急)诊处方 就诊时间:2025-01-03 就诊科室:内科门诊 主诊 性别: |
| 9 | e870da93 | 1 | 10-10 | 门(急)诊处方 就诊时间:2024-12-04 就诊科室:内科门诊 主诊 姓名  |
| 10 | e8933ae3 | 1 | 11-11 | 激发试验检查报告 姓名： 测试号： 门诊/住院号： 000 年龄： 出生日期：  |
| 11 | 0be40ec4 | 1 | 12-12 | 检查日期：2021/1/21 检查时间：16:43 编号：16 广州医科大学附属 |
| 12 | 4f886dcf | 1 | 13-13 | 广州医科大学附属第三医院 处方笺 普通 诊疗卡 患者姓名 年龄：41岁 费别：南 |
| 13 | bb4ea41a | 1 | 14-14 | 广州医科大学附属第三医院 The Third Affiliated Hospit |
| 14 | 7861af5b | 1 | 15-15 | 门诊/住院病历信息 就诊卡号：0 病历编号： 姓名： 性别：男 年龄：41岁 就 |
| 15 | 709e6264 | 1 | 16-16 | 广州医科大学附属第三医院 肺功能检查报告 地址：广州市多宝路63号 电话：020 |

- chunks 总数：15
- 各 chunk 页数合计（含跨页重复）：16
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]`
- 覆盖页数：16 / 16；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 5 | 0 | 5 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 7 | 7 | 7 | encounter_date, prescriber, diagnosis | **OK** |
| ExaminationReport | 检查报告 | 3 | 3 | 3 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 5, "PrescriptionRecord": 7, "ExaminationReport": 3}`
- ChunkMerger：`{"found": true, "merged": 15, "sources": 8, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 5, "Extractor:Medication": 1, "Extractor:Prescription": 7, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 3}, "filtered_noise": 5}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-06 02:25:14,919 INFO     29 [ChunkMerger] Merged 15 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 5, 'Extractor:Medication': 1, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-06 02:13:13,226 INFO     29 handle_task begin for task {"id": "5d401ece913c11f19b5e81513a69a703", "doc_id": "5963bc44913b11f19b5e81513a69a703", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785982387379, "task_type": "dataflow", "root_trace_id": "7886908ae2584ba69682631c2a66f747", "root_traceparent": "00-7886908ae2584ba69682631c2a66f747-971004a6101741b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-06 02:13:13,800 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-06 02:13:14,479 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-06 02:13:14,982 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-06 02:13:14,982 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-06 02:13:14,990 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-06 02:13:14,990 INFO     29 ============================================================
2026-08-06 02:13:14,990 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-06 02:13:14,990 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-06 02:13:14,990 INFO     29 ============================================================
2026-08-06 02:13:15,695 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx uses CPU
2026-08-06 02:13:15,881 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx uses CPU
2026-08-06 02:13:15,895 INFO     29 No torch found.
2026-08-06 02:13:16,252 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T02:13:16.252+00:00", "boot_at": "2026-08-06T01:59:43.412+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"5d401ece913c11f19b5e81513a69a703": {"id": "5d401ece913c11f19b5e81513a69a703", "doc_id": "5963bc44913b11f19b5e81513a69a703", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785982387379, "task_type": "dataflow", "root_trace_id": "7886908ae2584ba69682631c2a66f747", "root_traceparent": "00-7886908ae2584ba69682631c2a66f747-971004a6101741b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 02:13:17,616 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=16
2026-08-06 02:13:17,810 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1449002, prompt_len=764
2026-08-06 02:13:19,226 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 02:13:19,227 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-06 02:13:19,235 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1449002, prompt_len=401
2026-08-06 02:13:25,732 INFO     29 [qwen-vl-parser] text API response (len=1120):
["病历编号：", "性别：男", "年龄：40岁", "就诊科室：内科门诊（荔湾）", "就诊时间：2025-10-10 14:36:06", "主诉：BAIYUN V8", "现病史：自上次访视至今，询问及查询HIS系统受试者有新增AE，无SAE、哮喘急性发作，有新增合并用药，发生2次医疗相关事件[2025年9月3日因过敏性鼻炎就诊专科门诊、本周曾因上呼吸道感染到社区医院就诊(具体不详，因HIS系统滞后无法收集具体情况及受试者无法回忆起当时情况及用药情况，待收集具体情况后补充详情)]。于2025年8月4日、2025年9月1日收到加重警报邮件，联系受试者后，均判断非哮喘急性发作。", "完成下流操作：", "1、查看受试者电子日志，受试者漏填2025年8月16日，2025年9月4日晚间日志，2025年9月4日、2025年9月25日早间日志；", "2、填写AQLQ+12和ACQ-5问卷，ACQ-5评分：0.8分；", "3、休息10分钟后，测量坐位生命体征：血压113/81mmHg，脉搏87次/分，呼吸频率20次/分，体温36.6℃，测量身高177.5cm，体重90.5kg(BMI=28.7kg/m2)；", "4、14:35体格检查：神志清，体查合作，自主体位，一般外表无异常，皮肤、粘膜无异常，唇甲无发绀，眼睛、耳、鼻、咽喉无异常，口咽部粘膜无异常，颈软，气管居中，甲状腺未及肿大，全身浅表淋巴结未及肿大，颈静脉无怒张，胸廓无畸形，双肺呼吸运动对称，双肺触觉语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及啰音。心前区无隆起，心尖搏动无弥散，心界不大，心率：87次/分，律齐，各瓣膜听诊区未闻及病理性杂音。腹平软，全腹无压痛、反跳痛。肝、脾肋下未及，肝肾区无叩击痛，肠鸣音存，4次/分，脊柱、四肢无畸形，生理征存，未引出病理征，其他系统未见明显异常；", "5、休息至少10分钟后，于14:58行12导联ECG检查；", "6、于15:01采集中心实验室样本(血常规，血生化)并送往中心试验室；", "7、回收试验药物BDAMDI@ASMDI3盒(152968-AH及185936-HK未开封，148729-UA未用60揿，实际使用46揿，发药当天预喷4揿，2025年9月10日前因超过7天未使用试验药物空喷2次共4揿，2025年9月10日后受试者每七天清洗一次后空喷5次共10揿，总计预喷18揿；epro记录使用总共46揿，与实际使用情况一致。", "8、回收epro以及AM3。", "既往史：更新合并用药：", "1、糠酸莫米松鼻喷雾剂2025.4.3-2025.7.25 每鼻 2喷/次 qm 治疗过敏性鼻炎。"]
2026-08-06 02:13:25,733 INFO     29 [qwen-vl-parser] page=1 text: 18 lines (bbox 0-17)
2026-08-06 02:13:25,733 INFO     29 [qwen-vl-parser] page=1 text: 18 sections
2026-08-06 02:13:25,846 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=608187, prompt_len=764
2026-08-06 02:13:27,179 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 02:13:27,179 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-06 02:13:27,191 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=608187, prompt_len=401
2026-08-06 02:13:31,900 INFO     29 [qwen-vl-parser] text API response (len=804):
["病历文书", "门诊病历", "25/10/10 14时 门诊病历", "25/10/24 15时 门诊病历（GCP专用）", "25/11/17 10时 门诊病历", "头降使用40瓶，平均每天使用4瓶，2025年9月10日用空4瓶（大木使用试验药剂空瓶2次共4", "瓶，2025年9月10日后受试者每七天清光一次后空瓶5次共10瓶，合计空瓶10瓶（qrs记录使", "用总共46瓶，与实际使用情况一致。", "8、回访qrs以及MD。", "既往史：更新合并用药：", "1、鼻腔莫米松鼻喷雾剂C025 4 3-2025 7 25 每鼻 2喷/次 qd 治疗过敏性鼻炎。", "2、苯环喹莫铵鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。", "4、氯卓斯汀氟替卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。", "5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/", "次 治疗过敏性鼻炎。", "6、枯草抗感染治疗（生理性海水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过", "敏性鼻炎", "已预约受试者安全性随访时间。", "过敏史：", "个人史：", "体格检查：", "专科情况：", "辅助检查：", "治疗项目：", "门诊诊断：", "支气管哮喘", "单病种：", "发病时间：", "处", "置：", "1心电图（心电图室做）", "2布地奈德福莫特罗吸入粉雾剂(II)(省采)●①② 2盒2000,日入用药,一天2次", "30天", "备注：", "病情评估：", "病情分级：", "是否抢救病例：否", "是否抢救成功：", "是否为绿色通道患者：否", "病人去向：", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-06 02:13:31,900 INFO     29 [qwen-vl-parser] page=2 text: 42 lines (bbox 18-59)
2026-08-06 02:13:31,900 INFO     29 [qwen-vl-parser] page=2 text: 42 sections
2026-08-06 02:13:32,044 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1138149, prompt_len=764
2026-08-06 02:13:33,348 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 02:13:33,348 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-06 02:13:33,357 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1138149, prompt_len=401
2026-08-06 02:13:38,901 INFO     29 [qwen-vl-parser] text API response (len=962):
["就诊卡", "流水号：", "姓名", "龄：40岁", "就诊科", "目：2025-10-24 15:45:39", "主诉：安全性电话随访", "现病史：今日10:27", "固定电话（020-", "(159", "5），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无", "不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对", "V8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试", "者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，", "目前无安全性异常表现。", "合并用药更新：", "1、小柴胡颗粒、（自行购药）2025.10.6-2025.10.8 10g tid 治疗上呼吸道感染", "2、苯环喹溴铵鼻喷雾剂 2025.4.3-至今 每鼻2喷/次 qid 治疗过敏性鼻炎", "3、氮卓斯汀氟替卡松鼻喷雾剂 2025.9.3-至今 每鼻2喷/次 bid 治疗过敏性鼻炎", "4、辛芩颗粒 2024.8.21-2024.8.27 1袋 冲服 tid 治疗过敏性鼻炎", "AE：", "上呼吸道感染 2025年10月5日-2025年10月8日 中度，非SAE，采取药物治疗措施，对试验", "药物采取措施：剂量不变，与试验药物无关，未因该AE退出研究。", "病历更正：", "1、更正2024年10月22日病历，合并用药“辛芩颗粒”为“辛芩颗粒”；", "2、更正2024年10月22日病历，合并用药“苯环喹溴铵鼻喷雾剂”为“苯环喹溴铵鼻喷雾", "剂”；", "3、更正2026年1月24日病历，“无收到ePro触发的哮喘警报邮件”为“有收到ePro触发的哮", "喘警报邮件”；", "4、更正2025年7月18日病历，“受试者漏填2025年4月28日晚间日志” 更正为：“受试者", "漏填2025年4月28日早间日志”；", "5、更正2024年11月6日病历，“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共", "计用了26喷”为：“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了28", "喷”。", "随行中·"]
2026-08-06 02:13:38,901 INFO     29 [qwen-vl-parser] page=3 text: 35 lines (bbox 60-94)
2026-08-06 02:13:38,902 INFO     29 [qwen-vl-parser] page=3 text: 35 sections
2026-08-06 02:13:39,051 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1126349, prompt_len=764
2026-08-06 02:13:40,307 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 02:13:40,308 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-06 02:13:40,317 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1126349, prompt_len=401
2026-08-06 02:13:47,587 INFO     29 [qwen-vl-parser] text API response (len=842):
["病历编号：", "姓名：", "性别：", "年龄：40岁", "就诊科：", "就诊时间：2025-11-17 10:10:48", "主诉：支气管哮喘治疗后复查：", "现病史：2021年2月前开始出现咳嗽、咯痰，粘白，量中，能咯出，咳嗽呈阵发性、刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏。无咽痛，无伴反酸、嗳气、腹胀。无上腹部隐痛不适感，无伴发热、畏寒，影响睡眠。晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：", "12.52*109/L 嗜酸粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定。本次门诊距上次门诊间隔时间30天。症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确。急性发作情况：两次，就诊期间急性发作：无，发作次数：0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。近3天来出现咽痛不适", "既往史：鼻炎病史无规则治疗。打鼾明显。", "过敏史：未发现。", "个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。", "体格检查：神志清，颈软，双肺呼吸音粗，未闻及明显干、湿性罗音，口腔粘膜无白斑。", "专科情况：", "辅助检查：", "治疗项目：", "门诊诊断：", "1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、阻塞性睡眠呼吸暂停低通气综合征,4、急性咽炎", "单病种：", "发病时间：", "处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不适随诊。", "1金银花口服液◆⑤ 2盒 20.0ml,口服,一天3次(口服) 6天", "2氨卓斯汀氟替卡松鼻喷雾剂◆ 1瓶 2.0喷,喷鼻,一天2次 30天", "3苯环喹溴铵鼻喷雾剂◆ 3瓶 2.0喷,喷鼻,一天4次 30天", "备注：建议在住地附近社区医疗机构随诊。"]
2026-08-06 02:13:47,588 INFO     29 [qwen-vl-parser] page=4 text: 25 lines (bbox 95-119)
2026-08-06 02:13:47,588 INFO     29 [qwen-vl-parser] page=4 text: 25 sections
2026-08-06 02:13:47,703 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=674431, prompt_len=764
2026-08-06 02:13:48,667 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T02:13:48.664+00:00", "boot_at": "2026-08-06T01:59:43.412+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"5d401ece913c11f19b5e81513a69a703": {"id": "5d401ece913c11f19b5e81513a69a703", "doc_id": "5963bc44913b11f19b5e81513a69a703", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785982387379, "task_type": "dataflow", "root_trace_id": "7886908ae2584ba69682631c2a66f747", "root_traceparent": "00-7886908ae2584ba69682631c2a66f747-971004a6101741b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 02:13:49,060 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 02:13:49,060 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-06 02:13:49,071 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=674431, prompt_len=401
2026-08-06 02:13:50,757 INFO     29 [qwen-vl-parser] text API response (len=277):
["门(急)诊处方", "就诊时间:2025-07-18", "就诊科室:内科门诊", "主诊医", "姓名", "性别:男", "年龄:40岁", "卡号:", "患者", "医疗证号:", "处方号", "地址:PT027气雾剂 2024017-呼吸科", "身份证", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂0.125/0.006*60吸6盒", "183.41100.46", "Sig", "2吸/次,吸入,bid*90天"]
2026-08-06 02:13:50,757 INFO     29 [qwen-vl-parser] page=5 text: 26 lines (bbox 120-145)
2026-08-06 02:13:50,758 INFO     29 [qwen-vl-parser] page=5 text: 26 sections
2026-08-06 02:13:50,864 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=687923, prompt_len=764
2026-08-06 02:13:52,182 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 02:13:52,182 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-06 02:13:52,188 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=687923, prompt_len=401
2026-08-06 02:13:53,856 INFO     29 [qwen-vl-parser] text API response (len=284):
["门(急)诊处方", "就诊时间:2025-04-25", "就诊科室:内科门诊", "主诊", "姓名", "性别:男", "年龄:40岁", "卡号:", "患者类型:GLP支付", "医疗证号:", "处方号", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂(II)●●@ug*60吸6盒", "183.41100.46", "Sig", "2吸/次,吸入,bid*90天"]
2026-08-06 02:13:53,856 INFO     29 [qwen-vl-parser] page=6 text: 26 lines (bbox 146-171)
2026-08-06 02:13:53,856 INFO     29 [qwen-vl-parser] page=6 text: 26 sections
2026-08-06 02:13:53,961 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=642003, prompt_len=764
2026-08-06 02:13:55,263 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 02:13:55,263 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-06 02:13:55,269 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=642003, prompt_len=401
2026-08-06 02:13:56,896 INFO     29 [qwen-vl-parser] text API response (len=272):
["门(急)诊处方", "就诊时间:2025-02-26", "就诊科室:内科门诊", "主诊", "性别:男", "年龄:40岁", "卡号", "医疗证号:", "处方", "015", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂BDII/●@0.1g*60吸2盒", "183.41 366.82", "Sig", "2吸/次,吸入,bid*30天"]
2026-08-06 02:13:56,897 INFO     29 [qwen-vl-parser] page=7 text: 25 lines (bbox 172-196)
2026-08-06 02:13:56,897 INFO     29 [qwen-vl-parser] page=7 text: 25 sections
2026-08-06 02:13:57,004 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=635678, prompt_len=764
2026-08-06 02:13:58,211 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 02:13:58,212 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-06 02:13:58,232 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=635678, prompt_len=401
2026-08-06 02:13:59,858 INFO     29 [qwen-vl-parser] text API response (len=287):
["门(急)诊处方", "就诊时间:2025-01-24", "就诊科室:内科门诊", "主诊医", "姓名", "性别:男", "年龄:40岁", "卡号:4", "患者类型:GCP支付", "医疗证号:", "处方号:", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂HIV●@1ug*60吸4盒", "183.41 733.64", "Sig", "2吸/次,吸入,bid*60天"]
2026-08-06 02:13:59,858 INFO     29 [qwen-vl-parser] page=8 text: 26 lines (bbox 197-222)
2026-08-06 02:13:59,858 INFO     29 [qwen-vl-parser] page=8 text: 26 sections
2026-08-06 02:13:59,942 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=545840, prompt_len=764
2026-08-06 02:14:01,176 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 02:14:01,176 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-06 02:14:01,193 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=545840, prompt_len=401
2026-08-06 02:14:03,177 INFO     29 [qwen-vl-parser] text API response (len=356):
["门(急)诊处方", "就诊时间:2025-01-03", "就诊科室:内科门诊", "主诊", "性别:男", "年龄:40岁", "卡号", "患者类型:GCP支付", "医疗证号:", "处方", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●⑥ug*60吸2盒", "183.41 366.82", "Sig", "2吸/次,吸入,bid*30天", "医师:", "医生编号:1326", "配剂人:", "核对人:", "合计:", "收费员:", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-06 02:14:03,177 INFO     29 [qwen-vl-parser] page=9 text: 33 lines (bbox 223-255)
2026-08-06 02:14:03,177 INFO     29 [qwen-vl-parser] page=9 text: 33 sections
2026-08-06 02:14:03,283 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=642925, prompt_len=764
2026-08-06 02:14:04,661 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-12-04"}
```
2026-08-06 02:14:04,662 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=2024-12-04
2026-08-06 02:14:04,676 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=642925, prompt_len=401
2026-08-06 02:14:06,354 INFO     29 [qwen-vl-parser] text API response (len=277):
["门(急)诊处方", "就诊时间:2024-12-04", "就诊科室:内科门诊", "主诊", "姓名", "性别:男", "年龄:39岁", "卡号", "患者", "医疗证号:", "处方", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●(50ug*60吸2盒", "183.41 366.82", "Sig", "2吸/次,吸入,bid*30天"]
2026-08-06 02:14:06,354 INFO     29 [qwen-vl-parser] page=10 text: 26 lines (bbox 256-281)
2026-08-06 02:14:06,354 INFO     29 [qwen-vl-parser] page=10 text: 26 sections
2026-08-06 02:14:06,499 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1233186, prompt_len=764
2026-08-06 02:14:07,934 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-06 02:14:07,934 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=None
2026-08-06 02:14:07,944 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1233186, prompt_len=401
2026-08-06 02:14:19,782 INFO     29 [qwen-vl-parser] text API response (len=1968):
["激发试验检查报告", "姓名：", "测试号：", "门诊/住院号：", "000", "年龄：", "出生日期：", "19", "性别：", "男", "身高：", "170", "病区：", "内科门诊", "体重：", "81 kg", "机器编号：", "床号：", "电话：", "Pred", "A1", "A1/Pd", "NS", "P1 chg%1", "P2 chg%2", "P3 chg%3", "FVC", "[L]", "4.84", "4.69", "97.1", "4.29", "4.22", "-10.1", "3.64", "-22.5", "4.01", "-14.6", "PEV 1", "[L]", "4.01", "3.05", "76.2", "2.72", "2.69", "-11.8", "2.24", "-26.5", "2.44", "-20.0", "PEV 1 % PVC", "[%]", "83.32", "65.02", "78.0", "63.54", "63.83", "-1.82", "61.73", "-5.06", "60.92", "-6.30", "PEV 1 % VC MAX", "[%]", "80.55", "64.94", "80.6", "62.34", "63.83", "-1.70", "61.73", "-4.94", "60.92", "-6.18", "VC MAX", "[L]", "5.05", "4.70", "93.1", "4.37", "4.22", "-10.2", "3.64", "-22.6", "4.01", "-14.7", "PEP", "[L/s]", "9.37", "9.95", "106.2", "9.06", "7.81", "-21.5", "6.73", "-32.3", "8.22", "-17.4", "MMEF 75/25", "[L/s]", "4.52", "1.54", "34.1", "1.33", "1.34", "-12.9", "1.14", "-25.8", "1.23", "-20.0", "MEF 50", "[L/s]", "5.17", "1.97", "38.1", "1.66", "1.71", "-13.4", "1.34", "-31.8", "1.42", "-28.0", "MEF 25", "[L/s]", "2.29", "0.58", "25.5", "0.52", "0.53", "-9.87", "0.50", "-14.6", "0.49", "-15.7", "PET", "[s]", "6.72", "6.87", "6.93", "3.16", "6.75", "0.57", "6.74", "0.38", "V backextrapolation ex", "[L]", "0.13", "0.09", "0.10", "-20.0", "0.08", "-41.6", "0.08", "-38.5", "PIF", "[L/s]", "8.04", "7.96", "7.58", "-5.76", "6.16", "-23.3", "7.78", "-3.20", "FIF 50", "[L/s]", "7.99", "7.86", "7.16", "-10.3", "5.36", "-32.9", "7.08", "-11.3", "MVV", "[L/min]", "141.88", "BF MVV", "[1/min]", "Cumulated dose", "0.072", "0.078", "0.312", "2 Puf", "F/V ex", "F/V in", "Vol [L]", "Vol%VCmax", "VCmax", "Time [s]", "PD[-20] FEV 1: 0.2117 mg Cumulated", "PD[-20] PEF: < 0.078 mg Cumulated", "PD[] FEV1%I: could not be calculated!", "意见：", "2022/6/08 10:23:56上午", "1.轻度阻塞性通气功能障碍。", "2.支气管激发试验阳性(累计吸入乙酰甲胆碱0.312mg，FEV1下降大于20%，PD20=0.2117mg，气道高反应性(AHR)为中度", "通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后FEV1恢复至预计值80%。", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-06 02:14:19,782 INFO     29 [qwen-vl-parser] page=11 text: 200 lines (bbox 282-481)
2026-08-06 02:14:19,782 INFO     29 [qwen-vl-parser] page=11 text: 200 sections
2026-08-06 02:14:19,941 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1298077, prompt_len=764
2026-08-06 02:14:21,251 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T02:14:21.250+00:00", "boot_at": "2026-08-06T01:59:43.412+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"5d401ece913c11f19b5e81513a69a703": {"id": "5d401ece913c11f19b5e81513a69a703", "doc_id": "5963bc44913b11f19b5e81513a69a703", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785982387379, "task_type": "dataflow", "root_trace_id": "7886908ae2584ba69682631c2a66f747", "root_traceparent": "00-7886908ae2584ba69682631c2a66f747-971004a6101741b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 02:14:21,538 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2021-01-21"
}
```
2026-08-06 02:14:21,539 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=2021-01-21
2026-08-06 02:14:21,566 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1298077, prompt_len=401
2026-08-06 02:14:31,052 INFO     29 [qwen-vl-parser] text API response (len=1940):
["检查日期：2021/1/21", "检查时间：16:43", "编号：16", "广州医科大学附属第三医院", "支气管扩张试验检查报告", "姓名：", "测试号：", "年龄：36岁", "性别：男", "病区：", "机器编号：", "门诊/住院号：", "出生日期：", "身高：", "体重：", "床号：", "电话：", "Pred", "A1", "A1/Pd", "P1", "A2/Pd", "chg%1", "P2", "A3/Pd", "chg%2", "P3", "A4/Pd", "chg%3", "FVC", "[L]", "4.86", "3.48", "71.5%", "4.01", "82.4%", "15.19", "4.15", "85.4%", "19.47", "4.01", "82.6%", "15.47", "FEV 1", "[L]", "4.03", "1.97", "48.8%", "2.33", "57.9%", "18.59", "2.33", "57.8%", "18.48", "2.44", "60.5%", "24.02", "FEV 1 % FVC", "[%]", "83.32", "56.62", "68.0%", "58.29", "70.0%", "2.95", "56.15", "67.4%", "-0.83", "60.81", "73.0%", "7.40", "FEV 1 % VC MAX", "[%]", "80.73", "56.07", "69.5%", "58.29", "72.2%", "3.96", "56.15", "69.5%", "0.14", "60.81", "75.3%", "8.45", "VC MAX", "[L]", "5.08", "3.51", "69.1%", "4.01", "78.9%", "14.07", "4.15", "81.8%", "18.31", "4.01", "79.1%", "14.35", "PEF", "[L/s]", "9.41", "6.61", "70.3%", "7.99", "85.0%", "20.93", "7.91", "84.1%", "19.63", "8.07", "85.7%", "22.02", "MMEF 75/25", "[L/s]", "4.57", "0.81", "17.7%", "0.96", "21.1%", "19.59", "1.03", "22.6%", "28.17", "1.12", "24.6%", "39.07", "MEF 50", "[L/s]", "5.20", "1.00", "19.2%", "1.29", "24.8%", "29.25", "1.30", "24.9%", "29.87", "1.53", "29.3%", "52.75", "MEF 25", "[L/s]", "2.32", "0.39", "16.7%", "0.38", "16.4%", "-1.68", "0.50", "21.6%", "29.78", "0.41", "17.9%", "7.18", "FET", "[s]", "15.24", "6.42", "-57.87", "6.30", "-58.63", "6.55", "-57.05", "V backextrapolati", "[L/s]", "0.07", "0.07", "0.89", "0.09", "17.79", "0.08", "6.12", "PIF", "[L/s]", "7.03", "7.39", "5.19", "7.17", "1.99", "7.16", "1.91", "FIV1", "[L]", "3.40", "3.76", "10.58", "3.68", "8.26", "3.60", "5.96", "PEF50 % PIF50", "[%]", "16.56", "21.70", "31.06", "19.81", "19.65", "24.71", "49.20", "MVV", "[L/min]", "142.69", "BF MVV", "[1/min]", "意见：", "1.重度混合性肺通气功能障碍。", "2.支气管舒张试验阳性。", "（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后PEV1较基线增加大于12%，且绝对值增加大于200ml）", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-06 02:14:31,052 INFO     29 [qwen-vl-parser] page=12 text: 211 lines (bbox 482-692)
2026-08-06 02:14:31,052 INFO     29 [qwen-vl-parser] page=12 text: 211 sections
2026-08-06 02:14:31,174 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=712860, prompt_len=764
2026-08-06 02:14:32,578 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 02:14:32,578 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=None
2026-08-06 02:14:32,600 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=712860, prompt_len=401
2026-08-06 02:14:34,599 INFO     29 [qwen-vl-parser] text API response (len=349):
["广州医科大学附属第三医院", "处方笺", "普通", "诊疗卡", "患者姓名", "年龄：41岁", "费别：南医保", "科室：内科门诊（荔湾）", "日期：2026-01-05 17:17:14", "处方号", "地址：荔湾", "2024017-呼吸科", "联系电", "身份号码：", "2739", "诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],急性气管支气管炎", "R", "P:", "布地奈德福莫特罗吸入粉雾剂(II) 160ug/4.5ug*60吸", "2盒", "剂量：每次2吸", "（", "1", "30", "盒）", "用法：吸入用药", "bid", "01-05", "处方金额：366.82元", "取药药房：门诊西药房（荔湾）"]
2026-08-06 02:14:34,600 INFO     29 [qwen-vl-parser] page=13 text: 30 lines (bbox 693-722)
2026-08-06 02:14:34,600 INFO     29 [qwen-vl-parser] page=13 text: 30 sections
2026-08-06 02:14:34,730 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=972380, prompt_len=764
2026-08-06 02:14:36,086 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-01-05"}
```
2026-08-06 02:14:36,086 INFO     29 [qwen-vl-parser] page=14 classify=text report_date=2026-01-05
2026-08-06 02:14:36,100 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=972380, prompt_len=401
2026-08-06 02:14:42,659 INFO     29 [qwen-vl-parser] text API response (len=1267):
["广州医科大学附属第三医院", "The Third Affiliated Hospital of Guangzhou Medical University", "门(急)诊病历信息", "就诊卡", "流水", "姓", "病历编号:", "年 龄:41岁", "就诊科室:内科门诊(荔湾) 医", "就诊时间:2026-01-05 17:07:54", "主 诉:支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天", "现 病 史:2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激", "性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流", "涕、喷嚏,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响", "睡眠,晨起有咽干,曾到本院就诊两次,症状不见明显缓解。2021-1-9血常规:白细胞:", "12.52*109/L 嗜酸粒细胞:0.65*109/L 5.2%,经治疗后症状明显缓解。无咳嗽、咯痰、气", "促。病情稳定,本次门诊距上次门诊间隔时间30天。症状控制情况:过去4周,患者:吸入", "药物使用情况:遵医嘱使用;吸入装置使用情况:正确。急性发作情况:两次,就诊期间急", "性发作:无,发作次数:0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。长期规律使用信必", "可160/4.5ug 2吸 bid治疗,5天前开始出现咳嗽、咯痰,黄白痰,量少,难以咯出,咳嗽以", "夜间为主。无气促,伴咽息,鼻塞、流涕、喷嚏,无发热。", "既 往 史:鼻炎病史无规则治疗。打鼾明显。", "过 敏 史:未发现;", "个 人 史:否认遗传病史,吸烟10年,20支/日,2018年戒烟。偶饮酒。2021-12-20已打第", "三针新冠疫苗。", "体格检查:神志清,颈软,双肺呼吸音粗,可闻及散在哮鸣音,口腔粘膜无白斑。", "专科情况:", "辅助检查:", "治疗项目:", "门诊诊断:", "1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎", "处 置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。", "布地奈德福莫特罗吸入粉雾剂(II)2盒 2.0吸,吸入用药,一天2次 30天", "(省采)●①⑤", "左氧氟沙星片(省采)●⑥ 5片 0.5g,口服,每日1次(口服) 5天", "第1页", "广州医科大学附属第三医院", "The Third Affiliated Hospital of Guangzhou Medical University", "门(急)诊病历信息", "复方甲氧那明胶囊(省采)●② 1瓶 1.0粒,餐后口服,一天3次(口服) 5天", "盐酸氨溴索分散片(省采)●⑥ 15片 30.0mg,餐后口服,一天3次(口服) 5", "天", "醋酸泼尼松片●②④ 6片 10.0mg,口服,每早1次(口服) 3天", "备 注:建议在住地附近社区医疗机构随诊。"]
2026-08-06 02:14:42,660 INFO     29 [qwen-vl-parser] page=14 text: 44 lines (bbox 723-766)
2026-08-06 02:14:42,660 INFO     29 [qwen-vl-parser] page=14 text: 44 sections
2026-08-06 02:14:42,882 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1211412, prompt_len=764
2026-08-06 02:14:44,430 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-02-04"}
```
2026-08-06 02:14:44,430 INFO     29 [qwen-vl-parser] page=15 classify=text report_date=2026-02-04
2026-08-06 02:14:44,441 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1211412, prompt_len=401
2026-08-06 02:14:51,635 INFO     29 [qwen-vl-parser] text API response (len=801):
["门诊/住院病历信息", "就诊卡号：0", "病历编号：", "姓名：", "性别：男", "年龄：41岁", "就诊科室：内科门诊（荔湾）", "就诊时间：2026-02-04 11:21:11", "主诉：支气管哮喘治疗后复查", "现病史：2021年2月前开始出现咳嗽、哮喘，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sg 2吸 bid治疗。", "既往史：鼻炎病史无规则治疗，打鼾明显。", "过敏史：未发现；", "个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。", "体格检查：神志清，颈软，双肺呼吸音粗，可闻及散在哮鸣音，口腔粘膜无白斑。", "专科情况：", "辅助检查：", "治疗项目：", "门诊诊断：", "1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎", "单病种：", "发病时间：", "处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不遥随诊。", "布地奈德福莫特罗吸入粉雾剂(II)(省", "2 2.0班,吸入用药,一天2次", "30", "采)●①②", "查天"]
2026-08-06 02:14:51,635 INFO     29 [qwen-vl-parser] page=15 text: 27 lines (bbox 767-793)
2026-08-06 02:14:51,635 INFO     29 [qwen-vl-parser] page=15 text: 27 sections
2026-08-06 02:14:51,805 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1642425, prompt_len=764
2026-08-06 02:14:53,256 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2024-10-22"
}
```
2026-08-06 02:14:53,256 INFO     29 [qwen-vl-parser] page=16 classify=text report_date=2024-10-22
2026-08-06 02:14:53,271 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1642425, prompt_len=401
2026-08-06 02:14:53,786 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T02:14:53.785+00:00", "boot_at": "2026-08-06T01:59:43.412+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"5d401ece913c11f19b5e81513a69a703": {"id": "5d401ece913c11f19b5e81513a69a703", "doc_id": "5963bc44913b11f19b5e81513a69a703", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785982387379, "task_type": "dataflow", "root_trace_id": "7886908ae2584ba69682631c2a66f747", "root_traceparent": "00-7886908ae2584ba69682631c2a66f747-971004a6101741b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 02:15:26,281 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T02:15:26.280+00:00", "boot_at": "2026-08-06T01:59:43.412+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"5d401ece913c11f19b5e81513a69a703": {"id": "5d401ece913c11f19b5e81513a69a703", "doc_id": "5963bc44913b11f19b5e81513a69a703", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785982387379, "task_type": "dataflow", "root_trace_id": "7886908ae2584ba69682631c2a66f747", "root_traceparent": "00-7886908ae2584ba69682631c2a66f747-971004a6101741b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 02:15:58,782 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T02:15:58.782+00:00", "boot_at": "2026-08-06T01:59:43.412+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"5d401ece913c11f19b5e81513a69a703": {"id": "5d401ece913c11f19b5e81513a69a703", "doc_id": "5963bc44913b11f19b5e81513a69a703", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785982387379, "task_type": "dataflow", "root_trace_id": "7886908ae2584ba69682631c2a66f747", "root_traceparent": "00-7886908ae2584ba69682631c2a66f747-971004a6101741b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 02:16:31,304 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T02:16:31.303+00:00", "boot_at": "2026-08-06T01:59:43.412+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"5d401ece913c11f19b5e81513a69a703": {"id": "5d401ece913c11f19b5e81513a69a703", "doc_id": "5963bc44913b11f19b5e81513a69a703", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785982387379, "task_type": "dataflow", "root_trace_id": "7886908ae2584ba69682631c2a66f747", "root_traceparent": "00-7886908ae2584ba69682631c2a66f747-971004a6101741b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 02:17:02,541 INFO     29 [qwen-vl-parser] text API response (len=22294):
["广州医科大学附属第三医院", "肺功能检查报告", "地址：广州市多宝路63号 电话：020-81292126", "COSMED", "姓名：", "科室/床号：", "ID：", "出生日期：1984/12/8", "预计值：ERS 93", "日期：2024/10/22", "性别：Male", "地区修正：Chinese", "详细描述：内科门诊", "Company：", "年龄：39", "体重(Kg)：89.0", "身高(cm)：177.5", "BMI(Kg/m²：28.2", "吸烟：曾经(10/20)", "用力肺活量 Forced Vital Capacity", "F(l/s)", "V(l)", "BEST #3 - 2024/10/22 11:03", "沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38", "沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39", "沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41", "沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38", "沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39", "沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41", "BEST #3 - 2024/10/22 11:03", "FVC", "PEF", "MEF75%", "MEF50%", "MEF25%", "FVC", "6", "7", "8V(l)", "FEV1", "ATS", "12t(s)", "-1", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120", "121", "122", "123", "124", "125", "126", "127", "128", "129", "130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "140", "141", "142", "143", "144", "145", "146", "147", "148", "149", "150", "151", "152", "153", "154", "155", "156", "157", "158", "159", "160", "161", "162", "163", "164", "165", "166", "167", "168", "169", "170", "171", "172", "173", "174", "175", "176", "177", "178", "179", "180", "181", "182", "183", "184", "185", "186", "187", "188", "189", "190", "191", "192", "193", "194", "195", "196", "197", "198", "199", "200", "201", "202", "203", "204", "205", "206", "207", "208", "209", "210", "211", "212", "213", "214", "215", "216", "217", "218", "219", "220", "221", "222", "223", "224", "225", "226", "227", "228", "229", "230", "231", "232", "233", "234", "235", "236", "237", "238", "239", "240", "241", "242", "243", "244", "245", "246", "247", "248", "249", "250", "251", "252", "253", "254", "255", "256", "257", "258", "259", "260", "261", "262", "263", "264", "265", "266", "267", "268", "269", "270", "271", "272", "273", "274", "275", "276", "277", "278", "279", "280", "281", "282", "283", "284", "285", "286", "287", "288", "289", "290", "291", "292", "293", "294", "295", "296", "297", "298", "299", "300", "301", "302", "303", "304", "305", "306", "307", "308", "309", "310", "311", "312", "313", "314", "315", "316", "317", "318", "319", "320", "321", "322", "323", "324", "325", "326", "327", "328", "329", "330", "331", "332", "333", "334", "335", "336", "337", "338", "339", "340", "341", "342", "343", "344", "345", "346", "347", "348", "349", "350", "351", "352", "353", "354", "355", "356", "357", "358", "359", "360", "361", "362", "363", "364", "365", "366", "367", "368", "369", "370", "371", "372", "373", "374", "375", "376", "377", "378", "379", "380", "381", "382", "383", "384", "385", "386", "387", "388", "389", "390", "391", "392", "393", "394", "395", "396", "397", "398", "399", "400", "401", "402", "403", "404", "405", "406", "407", "408", "409", "410", "411", "412", "413", "414", "415", "416", "417", "418", "419", "420", "421", "422", "423", "424", "425", "426", "427", "428", "429", "430", "431", "432", "433", "434", "435", "436", "437", "438", "439", "440", "441", "442", "443", "444", "445", "446", "447", "448", "449", "450", "451", "452", "453", "454", "455", "456", "457", "458", "459", "460", "461", "462", "463", "464", "465", "466", "467", "468", "469", "470", "471", "472", "473", "474", "475", "476", "477", "478", "479", "480", "481", "482", "483", "484", "485", "486", "487", "488", "489", "490", "491", "492", "493", "494", "495", "496", "497", "498", "499", "500", "501", "502", "503", "504", "505", "506", "507", "508", "509", "510", "511", "512", "513", "514", "515", "516", "517", "518", "519", "520", "521", "522", "523", "524", "525", "526", "527", "528", "529", "530", "531", "532", "533", "534", "535", "536", "537", "538", "539", "540", "541", "542", "543", "544", "545", "546", "547", "548", "549", "550", "551", "552", "553", "554", "555", "556", "557", "558", "559", "560", "561", "562", "563", "564", "565", "566", "567", "568", "569", "570", "571", "572", "573", "574", "575", "576", "577", "578", "579", "580", "581", "582", "583", "584", "585", "586", "587", "588", "589", "590", "591", "592", "593", "594", "595", "596", "597", "598", "599", "600", "601", "602", "603", "604", "605", "606", "607", "608", "609", "610", "611", "612", "613", "614", "615", "616", "617", "618", "619", "620", "621", "622", "623", "624", "625", "626", "627", "628", "629", "630", "631", "632", "633", "634", "635", "636", "637", "638", "639", "640", "641", "642", "643", "644", "645", "646", "647", "648", "649", "650", "651", "652", "653", "654", "655", "656", "657", "658", "659", "660", "661", "662", "663", "664", "665", "666", "667", "668", "669", "670", "671", "672", "673", "674", "675", "676", "677", "678", "679", "680", "681", "682", "683", "684", "685", "686", "687", "688", "689", "690", "691", "692", "693", "694", "695", "696", "697", "698", "699", "700", "701", "702", "703", "704", "705", "706", "707", "708", "709", "710", "711", "712", "713", "714", "715", "716", "717", "718", "719", "720", "721", "722", "723", "724", "725", "726", "727", "728", "729", "730", "731", "732", "733", "734", "735", "736", "737", "738", "739", "740", "741", "742", "743", "744", "745", "746", "747", "748", "749", "750", "751", "752", "753", "754", "755", "756", "757", "758", "759", "760", "761", "762", "763", "764", "765", "766", "767", "768", "769", "770", "771", "772", "773", "774", "775", "776", "777", "778", "779", "780", "781", "782", "783", "784", "785", "786", "787", "788", "789", "790", "791", "792", "793", "794", "795", "796", "797", "798", "799", "800", "801", "802", "803", "804", "805", "806", "807", "808", "809", "810", "811", "812", "813", "814", "815", "816", "817", "818", "819", "820", "821", "822", "823", "824", "825", "826", "827", "828", "829", "830", "831", "832", "833", "834", "835", "836", "837", "838", "839", "840", "841", "842", "843", "844", "845", "846", "847", "848", "849", "850", "851", "852", "853", "854", "855", "856", "857", "858", "859", "860", "861", "862", "863", "864", "865", "866", "867", "868", "869", "870", "871", "872", "873", "874", "875", "876", "877", "878", "879", "880", "881", "882", "883", "884", "885", "886", "887", "888", "889", "890", "891", "892", "893", "894", "895", "896", "897", "898", "899", "900", "901", "902", "903", "904", "905", "906", "907", "908", "909", "910", "911", "912", "913", "914", "915", "916", "917", "918", "919", "920", "921", "922", "923", "924", "925", "926", "927", "928", "929", "930", "931", "932", "933", "934", "935", "936", "937", "938", "939", "940", "941", "942", "943", "944", "945", "946", "947", "948", "949", "950", "951", "952", "953", "954", "955", "956", "957", "958", "959", "960", "961", "962", "963", "964", "965", "966", "967", "968", "969", "970", "971", "972", "973", "974", "975", "976", "977", "978", "979", "980", "981", "982", "983", "984", "985", "986", "987", "988", "989", "990", "991", "992", "993", "994", "995", "996", "997", "998", "999", "1000", "1001", "1002", "1003", "1004", "1005", "1006", "1007", "1008", "1009", "1010", "1011", "1012", "1013", "1014", "1015", "1016", "1017", "1018", "1019", "1020", "1021", "1022", "1023", "1024", "1025", "1026", "1027", "1028", "1029", "1030", "1031", "1032", "1033", "1034", "1035", "1036", "1037", "1038", "1039", "1040", "1041", "1042", "1043", "1044", "1045", "1046", "1047", "1048", "1049", "1050", "1051", "1052", "1053", "1054", "1055", "1056", "1057", "1058", "1059", "1060", "1061", "1062", "1063", "1064", "1065", "1066", "1067", "1068", "1069", "1070", "1071", "1072", "1073", "1074", "1075", "1076", "1077", "1078", "1079", "1080", "1081", "1082", "1083", "1084", "1085", "1086", "1087", "1088", "1089", "1090", "1091", "1092", "1093", "1094", "1095", "1096", "1097", "1098", "1099", "1100", "1101", "1102", "1103", "1104", "1105", "1106", "1107", "1108", "1109", "1110", "1111", "1112", "1113", "1114", "1115", "1116", "1117", "1118", "1119", "1120", "1121", "1122", "1123", "1124", "1125", "1126", "1127", "1128", "1129", "1130", "1131", "1132", "1133", "1134", "1135", "1136", "1137", "1138", "1139", "1140", "1141", "1142", "1143", "1144", "1145", "1146", "1147", "1148", "1149", "1150", "1151", "1152", "1153", "1154", "1155", "1156", "1157", "1158", "1159", "1160", "1161", "1162", "1163", "1164", "1165", "1166", "1167", "1168", "1169", "1170", "1171", "1172", "1173", "1174", "1175", "1176", "1177", "1178", "1179", "1180", "1181", "1182", "1183", "1184", "1185", "1186", "1187", "1188", "1189", "1190", "1191", "1192", "1193", "1194", "1195", "1196", "1197", "1198", "1199", "1200", "1201", "1202", "1203", "1204", "1205", "1206", "1207", "1208", "1209", "1210", "1211", "1212", "1213", "1214", "1215", "1216", "1217", "1218", "1219", "1220", "1221", "1222", "1223", "1224", "1225", "1226", "1227", "1228", "1229", "1230", "1231", "1232", "1233", "1234", "1235", "1236", "1237", "1238", "1239", "1240", "1241", "1242", "1243", "1244", "1245", "1246", "1247", "1248", "1249", "1250", "1251", "1252", "1253", "1254", "1255", "1256", "1257", "1258", "1259", "1260", "1261", "1262", "1263", "1264", "1265", "1266", "1267", "1268", "1269", "1270", "1271", "1272", "1273", "1274", "1275", "1276", "1277", "1278", "1279", "1280", "1281", "1282", "1283", "1284", "1285", "1286", "1287", "1288", "1289", "1290", "1291", "1292", "1293", "1294", "1295", "1296", "1297", "1298", "1299", "1300", "1301", "1302", "1303", "1304", "1305", "1306", "1307", "1308", "1309", "1310", "1311", "1312", "1313", "1314", "1315", "1316", "1317", "1318", "1319", "1320", "1321", "1322", "1323", "1324", "1325", "1326", "1327", "1328", "1329", "1330", "1331", "1332", "1333", "1334", "1335", "1336", "1337", "1338", "1339", "1340", "1341", "1342", "1343", "1344", "1345", "1346", "1347", "1348", "1349", "1350", "1351", "1352", "1353", "1354", "1355", "1356", "1357", "1358", "1359", "1360", "1361", "1362", "1363", "1364", "1365", "1366", "1367", "1368", "1369", "1370", "1371", "1372", "1373", "1374", "1375", "1376", "1377", "1378", "1379", "1380", "1381", "1382", "1383", "1384", "1385", "1386", "1387", "1388", "1389", "1390", "1391", "1392", "1393", "1394", "1395", "1396", "1397", "1398", "1399", "1400", "1401", "1402", "1403", "1404", "1405", "1406", "1407", "1408", "1409", "1410", "1411", "1412", "1413", "1414", "1415", "1416", "1417", "1418", "1419", "1420", "1421", "1422", "1423", "1424", "1425", "1426", "1427", "1428", "1429", "1430", "1431", "1432", "1433", "1434", "1435", "1436", "1437", "1438", "1439", "1440", "1441", "1442", "1443", "1444", "1445", "1446", "1447", "1448", "1449", "1450", "1451", "1452", "1453", "1454", "1455", "1456", "1457", "1458", "1459", "1460", "1461", "1462", "1463", "1464", "1465", "1466", "1467", "1468", "1469", "1470", "1471", "1472", "1473", "1474", "1475", "1476", "1477", "1478", "1479", "1480", "1481", "1482", "1483", "1484", "1485", "1486", "1487", "1488", "1489", "1490", "1491", "1492", "1493", "1494", "1495", "1496", "1497", "1498", "1499", "1500", "1501", "1502", "1503", "1504", "1505", "1506", "1507", "1508", "1509", "1510", "1511", "1512", "1513", "1514", "1515", "1516", "1517", "1518", "1519", "1520", "1521", "1522", "1523", "1524", "1525", "1526", "1527", "1528", "1529", "1530", "1531", "1532", "1533", "1534", "1535", "1536", "1537", "1538", "1539", "1540", "1541", "1542", "1543", "1544", "1545", "1546", "1547", "1548", "1549", "1550", "1551", "1552", "1553", "1554", "1555", "1556", "1557", "1558", "1559", "1560", "1561", "1562", "1563", "1564", "1565", "1566", "1567", "1568", "1569", "1570", "1571", "1572", "1573", "1574", "1575", "1576", "1577", "1578", "1579", "1580", "1581", "1582", "1583", "1584", "1585", "1586", "1587", "1588", "1589", "1590", "1591", "1592", "1593", "1594", "1595", "1596", "1597", "1598", "1599", "1600", "1601", "1602", "1603", "1604", "1605", "1606", "1607", "1608", "1609", "1610", "1611", "1612", "1613", "1614", "1615", "1616", "1617", "1618", "1619", "1620", "1621", "1622", "1623", "1624", "1625", "1626", "1627", "1628", "1629", "1630", "1631", "1632", "1633", "1634", "1635", "1636", "1637", "1638", "1639", "1640", "1641", "1642", "1643", "1644", "1645", "1646", "1647", "1648", "1649", "1650", "1651", "1652", "1653", "1654", "1655", "1656", "1657", "1658", "1659", "1660", "1661", "1662", "1663", "1664", "1665", "1666", "1667", "1668", "1669", "1670", "1671", "1672", "1673", "1674", "1675", "1676", "1677", "1678", "1679", "1680", "1681", "1682", "1683", "1684", "1685", "1686", "1687", "1688", "1689", "1690", "1691", "1692", "1693", "1694", "1695", "1696", "1697", "1698", "1699", "1700", "1701", "1702", "1703", "1704", "1705", "1706", "1707", "1708", "1709", "1710", "1711", "1712", "1713", "1714", "1715", "1716", "1717", "1718", "1719", "1720", "1721", "1722", "1723", "1724", "1725", "1726", "1727", "1728", "1729", "1730", "1731", "1732", "1733", "1734", "1735", "1736", "1737", "1738", "1739", "1740", "1741", "1742", "1743", "1744", "1745", "1746", "1747", "1748", "1749", "1750", "1751", "1752", "1753", "1754", "1755", "1756", "1757", "1758", "1759", "1760", "1761", "1762", "1763", "1764", "1765", "1766", "1767", "1768", "1769", "1770", "1771", "1772", "1773", "1774", "1775", "1776", "1777", "1778", "1779", "1780", "1781", "1782", "1783", "1784", "1785", "1786", "1787", "1788", "1789", "1790", "1791", "1792", "1793", "1794", "1795", "1796", "1797", "1798", "1799", "1800", "1801", "1802", "1803", "1804", "1805", "1806", "1807", "1808", "1809", "1810", "1811", "1812", "1813", "1814", "1815", "1816", "1817", "1818", "1819", "1820", "1821", "1822", "1823", "1824", "1825", "1826", "1827", "1828", "1829", "1830", "1831", "1832", "1833", "1834", "1835", "1836", "1837", "1838", "1839", "1840", "1841", "1842", "1843", "1844", "1845", "1846", "1847", "1848", "1849", "1850", "1851", "1852", "1853", "1854", "1855", "1856", "1857", "1858", "1859", "1860", "1861", "1862", "1863", "1864", "1865", "1866", "1867", "1868", "1869", "1870", "1871", "1872", "1873", "1874", "1875", "1876", "1877", "1878", "1879", "1880", "1881", "1882", "1883", "1884", "1885", "1886", "1887", "1888", "1889", "1890", "1891", "1892", "1893", "1894", "1895", "1896", "1897", "1898", "1899", "1900", "1901", "1902", "1903", "1904", "1905", "1906", "1907", "1908", "1909", "1910", "1911", "1912", "1913", "1914", "1915", "1916", "1917", "1918", "1919", "1920", "1921", "1922", "1923", "1924", "1925", "1926", "1927", "1928", "1929", "1930", "1931", "1932", "1933", "1934", "1935", "1936", "1937", "1938", "1939", "1940", "1941", "1942", "1943", "1944", "1945", "1946", "1947", "1948", "1949", "1950", "1951", "1952", "1953", "1954", "1955", "1956", "1957", "1958", "1959", "1960", "1961", "1962", "1963", "1964", "1965", "1966", "1967", "1968", "1969", "1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034", "2035", "2036", "2037", "2038", "2039", "2040", "2041", "2042", "2043", "2044", "2045", "2046", "2047", "2048", "2049", "2050", "2051", "2052", "2053", "2054", "2055", "2056", "2057", "2058", "2059", "2060", "2061", "2062", "2063", "2064", "2065", "2066", "2067", "2068", "2069", "2070", "2071", "2072", "2073", "2074", "2075", "2076", "2077", "2078", "2079", "2080", "2081", "2082", "2083", "2084", "2085", "2086", "2087", "2088", "2089", "2090", "2091", "2092", "2093", "2094", "2095", "2096", "2097", "2098", "2099", "2100", "2101", "2102", "2103", "2104", "2105", "2106", "2107", "2108", "2109", "2110", "2111", "2112", "2113", "2114", "2115", "2116", "2117", "2118", "2119", "2120", "2121", "2122", "2123", "2124", "2125", "2126", "2127", "2128", "2129", "2130", "2131", "2132", "2133", "2134", "2135", "2136", "2137", "2138", "2139", "2140", "2141", "2142", "2143", "2144", "2145", "2146", "2147", "2148", "2149", "2150", "2151", "2152", "2153", "2154", "2155", "2156", "2157", "2158", "2159", "2160", "2161", "2162", "2163", "2164", "2165", "2166", "2167", "2168", "2169", "2170", "2171", "2172", "2173", "2174", "2175", "2176", "2177", "2178", "2179", "2180", "2181", "2182", "2183", "2184", "2185", "2186", "2187", "2188", "2189", "2190", "2191", "2192", "2193", "2194", "2195", "2196", "2197", "2198", "2199", "2200", "2201", "2202", "2203", "2204", "2205", "2206", "2207", "2208", "2209", "2210", "2211", "2212", "2213", "2214", "2215", "2216", "2217", "2218", "2219", "2220", "2221", "2222", "2223", "2224", "2225", "2226", "2227", "2228", "2229", "2230", "2231", "2232", "2233", "2234", "2235", "2236", "2237", "2238", "2239", "2240", "2241", "2242", "2243", "2244", "2245", "2246", "2247", "2248", "2249", "2250", "2251", "2252", "2253", "2254", "2255", "2256", "2257", "2258", "2259", "2260", "2261", "2262", "2263", "2264", "2265", "2266", "2267", "2268", "2269", "2270", "2271", "2272", "2273", "2274", "2275", "2276", "2277", "2278", "2279", "2280", "2281", "2282", "2283", "2284", "2285", "2286", "2287", "2288", "2289", "2290", "2291", "2292", "2293", "2294", "2295", "2296", "2297", "2298", "2299", "2300", "2301", "2302", "2303", "2304", "2305", "2306", "2307", "2308", "2309", "2310", "2311", "2312", "2313", "2314", "2315", "2316", "2317", "2318", "2319", "2320", "2321", "2322", "2323", "2324", "2325", "2326", "2327", "2328", "2329", "2330", "2331", "2332", "2333", "2334", "2335", "2336", "2337", "2338", "2339", "2340", "2341", "2342", "2343", "2344", "2345", "2346", "2347", "2348", "2349", "2350", "2351", "2352", "2353", "2354", "2355", "2356", "2357", "2358", "2359", "2360", "2361", "2362", "2363", "2364", "2365", "2366", "2367", "2368", "2369", "2370", "2371", "2372", "2373", "2374", "2375", "2376", "2377", "2378", "2379", "2380", "2381", "2382", "2383", "2384", "2385", "2386", "2387", "2388", "2389", "2390", "2391", "2392", "2393", "2394", "2395", "2396", "2397", "2398", "2399", "2400", "2401", "2402", "2403", "2404", "2405", "2406", "2407", "2408", "2409", "2410", "2411", "2412", "2413", "2414", "2415", "2416", "2417", "2418", "2419", "2420", "2421", "2422", "2423", "2424", "2425", "2426", "2427", "2428", "2429", "2430", "2431", "2432", "2433", "2434", "2435", "2436", "2437", "2438", "2439", "2440", "2441", "2442", "2443", "2444", "2445", "2446", "2447", "2448", "2449", "2450", "2451", "2452", "2453", "2454", "2455", "2456", "2457", "2458", "2459", "2460", "2461", "2462", "2463", "2464", "2465", "2466", "2467", "2468", "2469", "2470", "2471", "2472", "2473", "2474", "2475", "2476", "2477", "2478", "2479", "2480", "2481", "2482", "2483", "2484", "2485", "2486", "2487", "2488", "2489", "2490", "2491", "2492", "2493", "2494", "2495", "2496", "2497", "2498", "2499", "2500", "2501", "2502", "2503", "2504", "2505", "2506", "2507", "2508", "2509", "2510", "2511", "2512", "2513", "2514", "2515", "2516", "2517", "2518", "2519", "2520", "2521", "2522", "2523", "2524", "2525", "2526", "2527", "2528", "2529", "2530", "2531", "2532", "2533", "2534", "2535", "2536", "2537", "2538", "2539", "2540", "2541", "2542", "2543", "2544", "2545", "2546", "2547", "2548", "2549", "2550", "2551", "2552", "2553", "2554", "2555", "2556", "2557", "2558", "2559", "2560", "2561", "2562", "2563", "2564", "2565", "2566", "2567", "2568", "2569", "2570", "2571", "2572", "2573", "2574", "2575", "2576", "2577", "2578", "2579", "2580", "2581", "2582", "2583", "2584", "2585", "2586", "2587", "2588", "2589", "2590", "2591", "2592", "2593", "2594", "2595", "2596", "2597", "2598", "2599", "2600", "2601", "2602", "2603", "2604", "2605", "2606", "2607", "2608", "2609", "2610", "2611", "2612", "2613", "2614", "2615", "2616", "2617", "2618", "2619", "2620", "2621", "2622", "2623", "2624", "2625", "2626", "2627", "2628", "2629", "2630", "2631", "2632", "2633", "2634", "2635", "2636", "2637", "2638", "2639", "2640", "2641", "2642", "2643", "2644", "2645", "2646", "2647", "2648", "2649", "2650", "2651", "2652", "2653", "2654", "2655", "2656", "2657", "2658", "2659", "2660", "2661", "2662", "2663", "2664", "2665", "2666", "2667", "2668", "2669", "2670", "2671", "2672", "2673", "2674", "2675", "2676", "2677", "2678", "2679", "2680", "2681", "2682", "2683", "2684", "2685", "2686", "2687", "2688", "2689", "2690", "2691", "2692", "2693", "2694", "2695", "2696", "2697", "2698", "2699", "2700", "2701", "2702", "2703", "2704", "2705", "2706", "2707", "2708", "2709", "2710", "2711", "2712", "2713", "2714", "2715", "2716", "2717", "2718", "2719", "2720", "2721", "2722", "2723", "2724", "2725", "2726", "2727", "2728", "2729", "2730", "2731", "2732", "2733", "2734", "2735", "2736", "2737", "2738", "2739", "2740", "2741", "2742", "2743", "2744", "2745", "2746", "2747", "2748", "2749", "2750", "2751", "2752", "2753", "2754", "2755", "2756", "2757", "2758", "2759", "2760", "2761", "2762", "2763", "2764", "2765", "2766", "2767", "2768", "2769", "2770", "2771", "2772", "2773", "2774", "2775", "2776", "2777", "2778", "2779", "2780", "2781", "2782", "2783", "2784", "2785", "2786", "2787", "2788", "2789", "2790", "2791", "2792", "2793", "2794", "2795", "2796", "2797", "2798", "2799", "2800", "2801", "2802", "2803", "2804", "2805", "2806", "2807", "2808", "2809", "2810", "2811", "2812", "2813", "2814
2026-08-06 02:17:02,550 INFO     29 [qwen-vl-parser] page=16 text: 2884 lines (bbox 794-3677)
2026-08-06 02:17:02,550 INFO     29 [qwen-vl-parser] page=16 text: 2884 sections
2026-08-06 02:17:02,550 INFO     29 [qwen-vl-parser] parse_pdf done: 3678 sections from 16 pages.
2026-08-06 02:17:02,566 INFO     29 Close text detector.
2026-08-06 02:17:03,042 INFO     29 Close text recognizer.
2026-08-06 02:17:03,432 INFO     29 Close recognizer.
2026-08-06 02:17:03,817 INFO     29 Close recognizer.
2026-08-06 02:17:04,430 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T02:17:04.429+00:00", "boot_at": "2026-08-06T01:59:43.412+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"5d401ece913c11f19b5e81513a69a703": {"id": "5d401ece913c11f19b5e81513a69a703", "doc_id": "5963bc44913b11f19b5e81513a69a703", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785982387379, "task_type": "dataflow", "root_trace_id": "7886908ae2584ba69682631c2a66f747", "root_traceparent": "00-7886908ae2584ba69682631c2a66f747-971004a6101741b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 02:17:04,618 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-06 02:17:04,618 INFO     29 [Trace] task=5d401ece | doc=LZK 哮喘 广三(1).pdf | Parser:MedLink | outputs={"html": "", "json": "3678 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "json"}
2026-08-06 02:17:04,618 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-06 02:17:04,655 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 02:17:04,656 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。只有主诉，病史的也属于OutpatientRecord（门诊病历）\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 病历编号：\n[BBOX-1] 性别：男\n[BBOX-2] 年龄：40岁\n[BBOX-3] 就诊科室：内科门诊（荔湾）\n[BBOX-4] 就诊时间：2025-10-10 14:36:06\n[BBOX-5] 主诉：BAIYUN V8\n[BBOX-6] 现病史：自上次访视至今，询问及查询HIS系统受试者有新增AE，无SAE、哮喘急性发作，有新增合并用药，发生2次医疗相关事件[2025年9月3日因过敏性鼻炎就诊专科门诊、本周曾因上呼吸道感染到社区医院就诊(具体不详，因HIS系统滞后无法收集具体情况及受试者无法回忆起当时情况及用药情况，待收集具体情况后补充详情)]。于2025年8月4日、2025年9月1日收到加重警报邮件，联系受试者后，均判断非哮喘急性发作。\n[BBOX-7] 完成下流操作：\n[BBOX-8] 1、查看受试者电子日志，受试者漏填2025年8月16日，2025年9月4日晚间日志，2025年9月4日、2025年9月25日早间日志；\n[BBOX-9] 2、填写AQLQ+12和ACQ-5问卷，ACQ-5评分：0.8分；\n[BBOX-10] 3、休息10分钟后，测量坐位生命体征：血压113/81mmHg，脉搏87次/分，呼吸频率20次/分，体温36.6℃，测量身高177.5cm，体重90.5kg(BMI=28.7kg/m2)；\n[BBOX-11] 4、14:35体格检查：神志清，体查合作，自主体位，一般外表无异常，皮肤、粘膜无异常，唇甲无发绀，眼睛、耳、鼻、咽喉无异常，口咽部粘膜无异常，颈软，气管居中，甲状腺未及肿大，全身浅表淋巴结未及肿大，颈静脉无怒张，胸廓无畸形，双肺呼吸运动对称，双肺触觉语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及啰音。心前区无隆起，心尖搏动无弥散，心界不大，心率：87次/分，律齐，各瓣膜听诊区未闻及病理性杂音。腹平软，全腹无压痛、反跳痛。肝、脾肋下未及，肝肾区无叩击痛，肠鸣音存，4次/分，脊柱、四肢无畸形，生理征存，未引出病理征，其他系统未见明显异常；\n[BBOX-12] 5、休息至少10分钟后，于14:58行12导联ECG检查；\n[BBOX-13] 6、于15:01采集中心实验室样本(血常规，血生化)并送往中心试验室；\n[BBOX-14] 7、回收试验药物BDAMDI@ASMDI3盒(152968-AH及185936-HK未开封，148729-UA未用60揿，实际使用46揿，发药当天预喷4揿，2025年9月10日前因超过7天未使用试验药物空喷2次共4揿，2025年9月10日后受试者每七天清洗一次后空喷5次共10揿，总计预喷18揿；epro记录使用总共46揿，与实际使用情况一致。\n[BBOX-15] 8、回收epro以及AM3。\n[BBOX-16] 既往史：更新合并用药：\n[BBOX-17] 1、糠酸莫米松鼻喷雾剂2025.4.3-2025.7.25 每鼻 2喷/次 qm 治疗过敏性鼻炎。\n[BBOX-18] 病历文书\n[BBOX-19] 门诊病历\n[BBOX-20] 25/10/10 14时 门诊病历\n[BBOX-21] 25/10/24 15时 门诊病历（GCP专用）\n[BBOX-22] 25/11/17 10时 门诊病历\n[BBOX-23] 头降使用40瓶，平均每天使用4瓶，2025年9月10日用空4瓶（大木使用试验药剂空瓶2次共4\n[BBOX-24] 瓶，2025年9月10日后受试者每七天清光一次后空瓶5次共10瓶，合计空瓶10瓶（qrs记录使\n[BBOX-25] 用总共46瓶，与实际使用情况一致。\n[BBOX-26] 8、回访qrs以及MD。\n[BBOX-27] 既往史：更新合并用药：\n[BBOX-28] 1、鼻腔莫米松鼻喷雾剂C025 4 3-2025 7 25 每鼻 2喷/次 qd 治疗过敏性鼻炎。\n[BBOX-29] 2、苯环喹莫铵鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。\n[BBOX-30] 4、氯卓斯汀氟替卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。\n[BBOX-31] 5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/\n[BBOX-32] 次 治疗过敏性鼻炎。\n[BBOX-33] 6、枯草抗感染治疗（生理性海水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过\n[BBOX-34] 敏性鼻炎\n[BBOX-35] 已预约受试者安全性随访时间。\n[BBOX-36] 过敏史：\n[BBOX-37] 个人史：\n[BBOX-38] 体格检查：\n[BBOX-39] 专科情况：\n[BBOX-40] 辅助检查：\n[BBOX-41] 治疗项目：\n[BBOX-42] 门诊诊断：\n[BBOX-43] 支气管哮喘\n[BBOX-44] 单病种：\n[BBOX-45] 发病时间：\n[BBOX-46] 处\n[BBOX-47] 置：\n[BBOX-48] 1心电图（心电图室做）\n[BBOX-49] 2布地奈德福莫特罗吸入粉雾剂(II)(省采)●①② 2盒2000,日入用药,一天2次\n[BBOX-50] 30天\n[BBOX-51] 备注：\n[BBOX-52] 病情评估：\n[BBOX-53] 病情分级：\n[BBOX-54] 是否抢救病例：否\n[BBOX-55] 是否抢救成功：\n[BBOX-56] 是否为绿色通道患者：否\n[BBOX-57] 病人去向：\n[BBOX-58] CS 扫描全能王\n[BBOX-59] 3亿人都在用的扫描App\n[BBOX-60] 就诊卡\n[BBOX-61] 流水号：\n[BBOX-62] 姓名\n[BBOX-63] 龄：40岁\n[BBOX-64] 就诊科\n[BBOX-65] 目：2025-10-24 15:45:39\n[BBOX-66] 主诉：安全性电话随访\n[BBOX-67] 现病史：今日10:27\n[BBOX-68] 固定电话（020-\n[BBOX-69] (159\n[BBOX-70] 5），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无\n[BBOX-71] 不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对\n[BBOX-72] V8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试\n[BBOX-73] 者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，\n[BBOX-74] 目前无安全性异常表现。\n[BBOX-75] 合并用药更新：\n[BBOX-76] 1、小柴胡颗粒、（自行购药）2025.10.6-2025.10.8 10g tid 治疗上呼吸道感染\n[BBOX-77] 2、苯环喹溴铵鼻喷雾剂 2025.4.3-至今 每鼻2喷/次 qid 治疗过敏性鼻炎\n[BBOX-78] 3、氮卓斯汀氟替卡松鼻喷雾剂 2025.9.3-至今 每鼻2喷/次 bid 治疗过敏性鼻炎\n[BBOX-79] 4、辛芩颗粒 2024.8.21-2024.8.27 1袋 冲服 tid 治疗过敏性鼻炎\n[BBOX-80] AE：\n[BBOX-81] 上呼吸道感染 2025年10月5日-2025年10月8日 中度，非SAE，采取药物治疗措施，对试验\n[BBOX-82] 药物采取措施：剂量不变，与试验药物无关，未因该AE退出研究。\n[BBOX-83] 病历更正：\n[BBOX-84] 1、更正2024年10月22日病历，合并用药“辛芩颗粒”为“辛芩颗粒”；\n[BBOX-85] 2、更正2024年10月22日病历，合并用药“苯环喹溴铵鼻喷雾剂”为“苯环喹溴铵鼻喷雾\n[BBOX-86] 剂”；\n[BBOX-87] 3、更正2026年1月24日病历，“无收到ePro触发的哮喘警报邮件”为“有收到ePro触发的哮\n[BBOX-88] 喘警报邮件”；\n[BBOX-89] 4、更正2025年7月18日病历，“受试者漏填2025年4月28日晚间日志” 更正为：“受试者\n[BBOX-90] 漏填2025年4月28日早间日志”；\n[BBOX-91] 5、更正2024年11月6日病历，“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共\n[BBOX-92] 计用了26喷”为：“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了28\n[BBOX-93] 喷”。\n[BBOX-94] 随行中·\n[BBOX-95] 病历编号：\n[BBOX-96] 姓名：\n[BBOX-97] 性别：\n[BBOX-98] 年龄：40岁\n[BBOX-99] 就诊科：\n[BBOX-100] 就诊时间：2025-11-17 10:10:48\n[BBOX-101] 主诉：支气管哮喘治疗后复查：\n[BBOX-102] 现病史：2021年2月前开始出现咳嗽、咯痰，粘白，量中，能咯出，咳嗽呈阵发性、刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏。无咽痛，无伴反酸、嗳气、腹胀。无上腹部隐痛不适感，无伴发热、畏寒，影响睡眠。晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：\n[BBOX-103] 12.52*109/L 嗜酸粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定。本次门诊距上次门诊间隔时间30天。症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确。急性发作情况：两次，就诊期间急性发作：无，发作次数：0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。近3天来出现咽痛不适\n[BBOX-104] 既往史：鼻炎病史无规则治疗。打鼾明显。\n[BBOX-105] 过敏史：未发现。\n[BBOX-106] 个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。\n[BBOX-107] 体格检查：神志清，颈软，双肺呼吸音粗，未闻及明显干、湿性罗音，口腔粘膜无白斑。\n[BBOX-108] 专科情况：\n[BBOX-109] 辅助检查：\n[BBOX-110] 治疗项目：\n[BBOX-111] 门诊诊断：\n[BBOX-112] 1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、阻塞性睡眠呼吸暂停低通气综合征,4、急性咽炎\n[BBOX-113] 单病种：\n[BBOX-114] 发病时间：\n[BBOX-115] 处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不适随诊。\n[BBOX-116] 1金银花口服液◆⑤ 2盒 20.0ml,口服,一天3次(口服) 6天\n[BBOX-117] 2氨卓斯汀氟替卡松鼻喷雾剂◆ 1瓶 2.0喷,喷鼻,一天2次 30天\n[BBOX-118] 3苯环喹溴铵鼻喷雾剂◆ 3瓶 2.0喷,喷鼻,一天4次 30天\n[BBOX-119] 备注：建议在住地附近社区医疗机构随诊。\n[BBOX-120] 门(急)诊处方\n[BBOX-121] 就诊时间:2025-07-18\n[BBOX-122] 就诊科室:内科门诊\n[BBOX-123] 主诊医\n[BBOX-124] 姓名\n[BBOX-125] 性别:男\n[BBOX-126] 年龄:40岁\n[BBOX-127] 卡号:\n[BBOX-128] 患者\n[BBOX-129] 医疗证号:\n[BBOX-130] 处方号\n[BBOX-131] 地址:PT027气雾剂 2024017-呼吸科\n[BBOX-132] 身份证\n[BBOX-133] 诊断:支气管哮喘\n[BBOX-134] 西药处方\n[BBOX-135] 组号\n[BBOX-136] 项目名称\n[BBOX-137] 规格\n[BBOX-138] 总量\n[BBOX-139] 单价\n[BBOX-140] 金额\n[BBOX-141] R:\n[BBOX-142] 布地奈德福莫特罗吸入粉雾剂0.125/0.006*60吸6盒\n[BBOX-143] 183.41100.46\n[BBOX-144] Sig\n[BBOX-145] 2吸/次,吸入,bid*90天\n[BBOX-146] 门(急)诊处方\n[BBOX-147] 就诊时间:2025-04-25\n[BBOX-148] 就诊科室:内科门诊\n[BBOX-149] 主诊\n[BBOX-150] 姓名\n[BBOX-151] 性别:男\n[BBOX-152] 年龄:40岁\n[BBOX-153] 卡号:\n[BBOX-154] 患者类型:GLP支付\n[BBOX-155] 医疗证号:\n[BBOX-156] 处方号\n[BBOX-157] 地址:PT027气雾剂 2024017-呼吸科\n[BBOX-158] 身份证号:\n[BBOX-159] 诊断:支气管哮喘\n[BBOX-160] 西药处方\n[BBOX-161] 组号\n[BBOX-162] 项目名称\n[BBOX-163] 规格\n[BBOX-164] 总量\n[BBOX-165] 单价\n[BBOX-166] 金额\n[BBOX-167] R:\n[BBOX-168] 布地奈德福莫特罗吸入粉雾剂(II)●●@ug*60吸6盒\n[BBOX-169] 183.41100.46\n[BBOX-170] Sig\n[BBOX-171] 2吸/次,吸入,bid*90天\n[BBOX-172] 门(急)诊处方\n[BBOX-173] 就诊时间:2025-02-26\n[BBOX-174] 就诊科室:内科门诊\n[BBOX-175] 主诊\n[BBOX-176] 性别:男\n[BBOX-177] 年龄:40岁\n[BBOX-178] 卡号\n[BBOX-179] 医疗证号:\n[BBOX-180] 处方\n[BBOX-181] 015\n[BBOX-182] 地址:PT027气雾剂 2024017-呼吸科\n[BBOX-183] 身份证号:\n[BBOX-184] 诊断:支气管哮喘\n[BBOX-185] 西药处方\n[BBOX-186] 组号\n[BBOX-187] 项目名称\n[BBOX-188] 规格\n[BBOX-189] 总量\n[BBOX-190] 单价\n[BBOX-191] 金额\n[BBOX-192] R:\n[BBOX-193] 布地奈德福莫特罗吸入粉雾剂BDII/●@0.1g*60吸2盒\n[BBOX-194] 183.41 366.82\n[BBOX-195] Sig\n[BBOX-196] 2吸/次,吸入,bid*30天\n[BBOX-197] 门(急)诊处方\n[BBOX-198] 就诊时间:2025-01-24\n[BBOX-199] 就诊科室:内科门诊\n[BBOX-200] 主诊医\n[BBOX-201] 姓名\n[BBOX-202] 性别:男\n[BBOX-203] 年龄:40岁\n[BBOX-204] 卡号:4\n[BBOX-205] 患者类型:GCP支付\n[BBOX-206] 医疗证号:\n[BBOX-207] 处方号:\n[BBOX-208] 地址:PT027气雾剂 2024017-呼吸科\n[BBOX-209] 身份证号:\n[BBOX-210] 诊断:支气管哮喘\n[BBOX-211] 西药处方\n[BBOX-212] 组号\n[BBOX-213] 项目名称\n[BBOX-214] 规格\n[BBOX-215] 总量\n[BBOX-216] 单价\n[BBOX-217] 金额\n[BBOX-218] R:\n[BBOX-219] 布地奈德福莫特罗吸入粉雾剂HIV●@1ug*60吸4盒\n[BBOX-220] 183.41 733.64\n[BBOX-221] Sig\n[BBOX-222] 2吸/次,吸入,bid*60天\n[BBOX-223] 门(急)诊处方\n[BBOX-224] 就诊时间:2025-01-03\n[BBOX-225] 就诊科室:内科门诊\n[BBOX-226] 主诊\n[BBOX-227] 性别:男\n[BBOX-228] 年龄:40岁\n[BBOX-229] 卡号\n[BBOX-230] 患者类型:GCP支付\n[BBOX-231] 医疗证号:\n[BBOX-232] 处方\n[BBOX-233] 地址:PT027气雾剂 2024017-呼吸科\n[BBOX-234] 身份证号:\n[BBOX-235] 诊断:支气管哮喘\n[BBOX-236] 西药处方\n[BBOX-237] 组号\n[BBOX-238] 项目名称\n[BBOX-239] 规格\n[BBOX-240] 总量\n[BBOX-241] 单价\n[BBOX-242] 金额\n[BBOX-243] R:\n[BBOX-244] 布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●⑥ug*60吸2盒\n[BBOX-245] 183.41 366.82\n[BBOX-246] Sig\n[BBOX-247] 2吸/次,吸入,bid*30天\n[BBOX-248] 医师:\n[BBOX-249] 医生编号:1326\n[BBOX-250] 配剂人:\n[BBOX-251] 核对人:\n[BBOX-252] 合计:\n[BBOX-253] 收费员:\n[BBOX-254] CS 扫描全能王\n[BBOX-255] 3亿人都在用的扫描App\n[BBOX-256] 门(急)诊处方\n[BBOX-257] 就诊时间:2024-12-04\n[BBOX-258] 就诊科室:内科门诊\n[BBOX-259] 主诊\n[BBOX-260] 姓名\n[BBOX-261] 性别:男\n[BBOX-262] 年龄:39岁\n[BBOX-263] 卡号\n[BBOX-264] 患者\n[BBOX-265] 医疗证号:\n[BBOX-266] 处方\n[BBOX-267] 地址:PT027气雾剂 2024017-呼吸科\n[BBOX-268] 身份证号:\n[BBOX-269] 诊断:支气管哮喘\n[BBOX-270] 西药处方\n[BBOX-271] 组号\n[BBOX-272] 项目名称\n[BBOX-273] 规格\n[BBOX-274] 总量\n[BBOX-275] 单价\n[BBOX-276] 金额\n[BBOX-277] R:\n[BBOX-278] 布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●(50ug*60吸2盒\n[BBOX-279] 183.41 366.82\n[BBOX-280] Sig\n[BBOX-281] 2吸/次,吸入,bid*30天\n[BBOX-282] 激发试验检查报告\n[BBOX-283] 姓名：\n[BBOX-284] 测试号：\n[BBOX-285] 门诊/住院号：\n[BBOX-286] 000\n[BBOX-287] 年龄：\n[BBOX-288] 出生日期：\n[BBOX-289] 19\n[BBOX-290] 性别：\n[BBOX-291] 男\n[BBOX-292] 身高：\n[BBOX-293] 170\n[BBOX-294] 病区：\n[BBOX-295] 内科门诊\n[BBOX-296] 体重：\n[BBOX-297] 81 kg\n[BBOX-298] 机器编号：\n[BBOX-299] 床号：\n[BBOX-300] 电话：\n[BBOX-301] Pred\n[BBOX-302] A1\n[BBOX-303] A1/Pd\n[BBOX-304] NS\n[BBOX-305] P1 chg%1\n[BBOX-306] P2 chg%2\n[BBOX-307] P3 chg%3\n[BBOX-308] FVC\n[BBOX-309] [L]\n[BBOX-310] 4.84\n[BBOX-311] 4.69\n[BBOX-312] 97.1\n[BBOX-313] 4.29\n[BBOX-314] 4.22\n[BBOX-315] -10.1\n[BBOX-316] 3.64\n[BBOX-317] -22.5\n[BBOX-318] 4.01\n[BBOX-319] -14.6\n[BBOX-320] PEV 1\n[BBOX-321] [L]\n[BBOX-322] 4.01\n[BBOX-323] 3.05\n[BBOX-324] 76.2\n[BBOX-325] 2.72\n[BBOX-326] 2.69\n[BBOX-327] -11.8\n[BBOX-328] 2.24\n[BBOX-329] -26.5\n[BBOX-330] 2.44\n[BBOX-331] -20.0\n[BBOX-332] PEV 1 % PVC\n[BBOX-333] [%]\n[BBOX-334] 83.32\n[BBOX-335] 65.02\n[BBOX-336] 78.0\n[BBOX-337] 63.54\n[BBOX-338] 63.83\n[BBOX-339] -1.82\n[BBOX-340] 61.73\n[BBOX-341] -5.06\n[BBOX-342] 60.92\n[BBOX-343] -6.30\n[BBOX-344] PEV 1 % VC MAX\n[BBOX-345] [%]\n[BBOX-346] 80.55\n[BBOX-347] 64.94\n[BBOX-348] 80.6\n[BBOX-349] 62.34\n[BBOX-350] 63.83\n[BBOX-351] -1.70\n[BBOX-352] 61.73\n[BBOX-353] -4.94\n[BBOX-354] 60.92\n[BBOX-355] -6.18\n[BBOX-356] VC MAX\n[BBOX-357] [L]\n[BBOX-358] 5.05\n[BBOX-359] 4.70\n[BBOX-360] 93.1\n[BBOX-361] 4.37\n[BBOX-362] 4.22\n[BBOX-363] -10.2\n[BBOX-364] 3.64\n[BBOX-365] -22.6\n[BBOX-366] 4.01\n[BBOX-367] -14.7\n[BBOX-368] PEP\n[BBOX-369] [L/s]\n[BBOX-370] 9.37\n[BBOX-371] 9.95\n[BBOX-372] 106.2\n[BBOX-373] 9.06\n[BBOX-374] 7.81\n[BBOX-375] -21.5\n[BBOX-376] 6.73\n[BBOX-377] -32.3\n[BBOX-378] 8.22\n[BBOX-379] -17.4\n[BBOX-380] MMEF 75/25\n[BBOX-381] [L/s]\n[BBOX-382] 4.52\n[BBOX-383] 1.54\n[BBOX-384] 34.1\n[BBOX-385] 1.33\n[BBOX-386] 1.34\n[BBOX-387] -12.9\n[BBOX-388] 1.14\n[BBOX-389] -25.8\n[BBOX-390] 1.23\n[BBOX-391] -20.0\n[BBOX-392] MEF 50\n[BBOX-393] [L/s]\n[BBOX-394] 5.17\n[BBOX-395] 1.97\n[BBOX-396] 38.1\n[BBOX-397] 1.66\n[BBOX-398] 1.71\n[BBOX-399] -13.4\n[BBOX-400] 1.34\n[BBOX-401] -31.8\n[BBOX-402] 1.42\n[BBOX-403] -28.0\n[BBOX-404] MEF 25\n[BBOX-405] [L/s]\n[BBOX-406] 2.29\n[BBOX-407] 0.58\n[BBOX-408] 25.5\n[BBOX-409] 0.52\n[BBOX-410] 0.53\n[BBOX-411] -9.87\n[BBOX-412] 0.50\n[BBOX-413] -14.6\n[BBOX-414] 0.49\n[BBOX-415] -15.7\n[BBOX-416] PET\n[BBOX-417] [s]\n[BBOX-418] 6.72\n[BBOX-419] 6.87\n[BBOX-420] 6.93\n[BBOX-421] 3.16\n[BBOX-422] 6.75\n[BBOX-423] 0.57\n[BBOX-424] 6.74\n[BBOX-425] 0.38\n[BBOX-426] V backextrapolation ex\n[BBOX-427] [L]\n[BBOX-428] 0.13\n[BBOX-429] 0.09\n[BBOX-430] 0.10\n[BBOX-431] -20.0\n[BBOX-432] 0.08\n[BBOX-433] -41.6\n[BBOX-434] 0.08\n[BBOX-435] -38.5\n[BBOX-436] PIF\n[BBOX-437] [L/s]\n[BBOX-438] 8.04\n[BBOX-439] 7.96\n[BBOX-440] 7.58\n[BBOX-441] -5.76\n[BBOX-442] 6.16\n[BBOX-443] -23.3\n[BBOX-444] 7.78\n[BBOX-445] -3.20\n[BBOX-446] FIF 50\n[BBOX-447] [L/s]\n[BBOX-448] 7.99\n[BBOX-449] 7.86\n[BBOX-450] 7.16\n[BBOX-451] -10.3\n[BBOX-452] 5.36\n[BBOX-453] -32.9\n[BBOX-454] 7.08\n[BBOX-455] -11.3\n[BBOX-456] MVV\n[BBOX-457] [L/min]\n[BBOX-458] 141.88\n[BBOX-459] BF MVV\n[BBOX-460] [1/min]\n[BBOX-461] Cumulated dose\n[BBOX-462] 0.072\n[BBOX-463] 0.078\n[BBOX-464] 0.312\n[BBOX-465] 2 Puf\n[BBOX-466] F/V ex\n[BBOX-467] F/V in\n[BBOX-468] Vol [L]\n[BBOX-469] Vol%VCmax\n[BBOX-470] VCmax\n[BBOX-471] Time [s]\n[BBOX-472] PD[-20] FEV 1: 0.2117 mg Cumulated\n[BBOX-473] PD[-20] PEF: < 0.078 mg Cumulated\n[BBOX-474] PD[] FEV1%I: could not be calculated!\n[BBOX-475] 意见：\n[BBOX-476] 2022/6/08 10:23:56上午\n[BBOX-477] 1.轻度阻塞性通气功能障碍。\n[BBOX-478] 2.支气管激发试验阳性(累计吸入乙酰甲胆碱0.312mg，FEV1下降大于20%，PD20=0.2117mg，气道高反应性(AHR)为中度\n[BBOX-479] 通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后FEV1恢复至预计值80%。\n[BBOX-480] CS 扫描全能王\n[BBOX-481] 3亿人都在用的扫描App\n[BBOX-482] 检查日期：2021/1/21\n[BBOX-483] 检查时间：16:43\n[BBOX-484] 编号：16\n[BBOX-485] 广州医科大学附属第三医院\n[BBOX-486] 支气管扩张试验检查报告\n[BBOX-487] 姓名：\n[BBOX-488] 测试号：\n[BBOX-489] 年龄：36岁\n[BBOX-490] 性别：男\n[BBOX-491] 病区：\n[BBOX-492] 机器编号：\n[BBOX-493] 门诊/住院号：\n[BBOX-494] 出生日期：\n[BBOX-495] 身高：\n[BBOX-496] 体重：\n[BBOX-497] 床号：\n[BBOX-498] 电话：\n[BBOX-499] Pred\n[BBOX-500] A1\n[BBOX-501] A1/Pd\n[BBOX-502] P1\n[BBOX-503] A2/Pd\n[BBOX-504] chg%1\n[BBOX-505] P2\n[BBOX-506] A3/Pd\n[BBOX-507] chg%2\n[BBOX-508] P3\n[BBOX-509] A4/Pd\n[BBOX-510] chg%3\n[BBOX-511] FVC\n[BBOX-512] [L]\n[BBOX-513] 4.86\n[BBOX-514] 3.48\n[BBOX-515] 71.5%\n[BBOX-516] 4.01\n[BBOX-517] 82.4%\n[BBOX-518] 15.19\n[BBOX-519] 4.15\n[BBOX-520] 85.4%\n[BBOX-521] 19.47\n[BBOX-522] 4.01\n[BBOX-523] 82.6%\n[BBOX-524] 15.47\n[BBOX-525] FEV 1\n[BBOX-526] [L]\n[BBOX-527] 4.03\n[BBOX-528] 1.97\n[BBOX-529] 48.8%\n[BBOX-530] 2.33\n[BBOX-531] 57.9%\n[BBOX-532] 18.59\n[BBOX-533] 2.33\n[BBOX-534] 57.8%\n[BBOX-535] 18.48\n[BBOX-536] 2.44\n[BBOX-537] 60.5%\n[BBOX-538] 24.02\n[BBOX-539] FEV 1 % FVC\n[BBOX-540] [%]\n[BBOX-541] 83.32\n[BBOX-542] 56.62\n[BBOX-543] 68.0%\n[BBOX-544] 58.29\n[BBOX-545] 70.0%\n[BBOX-546] 2.95\n[BBOX-547] 56.15\n[BBOX-548] 67.4%\n[BBOX-549] -0.83\n[BBOX-550] 60.81\n[BBOX-551] 73.0%\n[BBOX-552] 7.40\n[BBOX-553] FEV 1 % VC MAX\n[BBOX-554] [%]\n[BBOX-555] 80.73\n[BBOX-556] 56.07\n[BBOX-557] 69.5%\n[BBOX-558] 58.29\n[BBOX-559] 72.2%\n[BBOX-560] 3.96\n[BBOX-561] 56.15\n[BBOX-562] 69.5%\n[BBOX-563] 0.14\n[BBOX-564] 60.81\n[BBOX-565] 75.3%\n[BBOX-566] 8.45\n[BBOX-567] VC MAX\n[BBOX-568] [L]\n[BBOX-569] 5.08\n[BBOX-570] 3.51\n[BBOX-571] 69.1%\n[BBOX-572] 4.01\n[BBOX-573] 78.9%\n[BBOX-574] 14.07\n[BBOX-575] 4.15\n[BBOX-576] 81.8%\n[BBOX-577] 18.31\n[BBOX-578] 4.01\n[BBOX-579] 79.1%\n[BBOX-580] 14.35\n[BBOX-581] PEF\n[BBOX-582] [L/s]\n[BBOX-583] 9.41\n[BBOX-584] 6.61\n[BBOX-585] 70.3%\n[BBOX-586] 7.99\n[BBOX-587] 85.0%\n[BBOX-588] 20.93\n[BBOX-589] 7.91\n[BBOX-590] 84.1%\n[BBOX-591] 19.63\n[BBOX-592] 8.07\n[BBOX-593] 85.7%\n[BBOX-594] 22.02\n[BBOX-595] MMEF 75/25\n[BBOX-596] [L/s]\n[BBOX-597] 4.57\n[BBOX-598] 0.81\n[BBOX-599] 17.7%\n[BBOX-600] 0.96\n[BBOX-601] 21.1%\n[BBOX-602] 19.59\n[BBOX-603] 1.03\n[BBOX-604] 22.6%\n[BBOX-605] 28.17\n[BBOX-606] 1.12\n[BBOX-607] 24.6%\n[BBOX-608] 39.07\n[BBOX-609] MEF 50\n[BBOX-610] [L/s]\n[BBOX-611] 5.20\n[BBOX-612] 1.00\n[BBOX-613] 19.2%\n[BBOX-614] 1.29\n[BBOX-615] 24.8%\n[BBOX-616] 29.25\n[BBOX-617] 1.30\n[BBOX-618] 24.9%\n[BBOX-619] 29.87\n[BBOX-620] 1.53\n[BBOX-621] 29.3%\n[BBOX-622] 52.75\n[BBOX-623] MEF 25\n[BBOX-624] [L/s]\n[BBOX-625] 2.32\n[BBOX-626] 0.39\n[BBOX-627] 16.7%\n[BBOX-628] 0.38\n[BBOX-629] 16.4%\n[BBOX-630] -1.68\n[BBOX-631] 0.50\n[BBOX-632] 21.6%\n[BBOX-633] 29.78\n[BBOX-634] 0.41\n[BBOX-635] 17.9%\n[BBOX-636] 7.18\n[BBOX-637] FET\n[BBOX-638] [s]\n[BBOX-639] 15.24\n[BBOX-640] 6.42\n[BBOX-641] -57.87\n[BBOX-642] 6.30\n[BBOX-643] -58.63\n[BBOX-644] 6.55\n[BBOX-645] -57.05\n[BBOX-646] V backextrapolati\n[BBOX-647] [L/s]\n[BBOX-648] 0.07\n[BBOX-649] 0.07\n[BBOX-650] 0.89\n[BBOX-651] 0.09\n[BBOX-652] 17.79\n[BBOX-653] 0.08\n[BBOX-654] 6.12\n[BBOX-655] PIF\n[BBOX-656] [L/s]\n[BBOX-657] 7.03\n[BBOX-658] 7.39\n[BBOX-659] 5.19\n[BBOX-660] 7.17\n[BBOX-661] 1.99\n[BBOX-662] 7.16\n[BBOX-663] 1.91\n[BBOX-664] FIV1\n[BBOX-665] [L]\n[BBOX-666] 3.40\n[BBOX-667] 3.76\n[BBOX-668] 10.58\n[BBOX-669] 3.68\n[BBOX-670] 8.26\n[BBOX-671] 3.60\n[BBOX-672] 5.96\n[BBOX-673] PEF50 % PIF50\n[BBOX-674] [%]\n[BBOX-675] 16.56\n[BBOX-676] 21.70\n[BBOX-677] 31.06\n[BBOX-678] 19.81\n[BBOX-679] 19.65\n[BBOX-680] 24.71\n[BBOX-681] 49.20\n[BBOX-682] MVV\n[BBOX-683] [L/min]\n[BBOX-684] 142.69\n[BBOX-685] BF MVV\n[BBOX-686] [1/min]\n[BBOX-687] 意见：\n[BBOX-688] 1.重度混合性肺通气功能障碍。\n[BBOX-689] 2.支气管舒张试验阳性。\n[BBOX-690] （通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后PEV1较基线增加大于12%，且绝对值增加大于200ml）\n[BBOX-691] CS 扫描全能王\n[BBOX-692] 3亿人都在用的扫描App\n[BBOX-693] 广州医科大学附属第三医院\n[BBOX-694] 处方笺\n[BBOX-695] 普通\n[BBOX-696] 诊疗卡\n[BBOX-697] 患者姓名\n[BBOX-698] 年龄：41岁\n[BBOX-699] 费别：南医保\n[BBOX-700] 科室：内科门诊（荔湾）\n[BBOX-701] 日期：2026-01-05 17:17:14\n[BBOX-702] 处方号\n[BBOX-703] 地址：荔湾\n[BBOX-704] 2024017-呼吸科\n[BBOX-705] 联系电\n[BBOX-706] 身份号码：\n[BBOX-707] 2739\n[BBOX-708] 诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],急性气管支气管炎\n[BBOX-709] R\n[BBOX-710] P:\n[BBOX-711] 布地奈德福莫特罗吸入粉雾剂(II) 160ug/4.5ug*60吸\n[BBOX-712] 2盒\n[BBOX-713] 剂量：每次2吸\n[BBOX-714] （\n[BBOX-715] 1\n[BBOX-716] 30\n[BBOX-717] 盒）\n[BBOX-718] 用法：吸入用药\n[BBOX-719] bid\n[BBOX-720] 01-05\n[BBOX-721] 处方金额：366.82元\n[BBOX-722] 取药药房：门诊西药房（荔湾）\n[BBOX-723] 广州医科大学附属第三医院\n[BBOX-724] The Third Affiliated Hospital of Guangzhou Medical University\n[BBOX-725] 门(急)诊病历信息\n[BBOX-726] 就诊卡\n[BBOX-727] 流水\n[BBOX-728] 姓\n[BBOX-729] 病历编号:\n[BBOX-730] 年 龄:41岁\n[BBOX-731] 就诊科室:内科门诊(荔湾) 医\n[BBOX-732] 就诊时间:2026-01-05 17:07:54\n[BBOX-733] 主 诉:支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天\n[BBOX-734] 现 病 史:2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激\n[BBOX-735] 性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流\n[BBOX-736] 涕、喷嚏,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响\n[BBOX-737] 睡眠,晨起有咽干,曾到本院就诊两次,症状不见明显缓解。2021-1-9血常规:白细胞:\n[BBOX-738] 12.52*109/L 嗜酸粒细胞:0.65*109/L 5.2%,经治疗后症状明显缓解。无咳嗽、咯痰、气\n[BBOX-739] 促。病情稳定,本次门诊距上次门诊间隔时间30天。症状控制情况:过去4周,患者:吸入\n[BBOX-740] 药物使用情况:遵医嘱使用;吸入装置使用情况:正确。急性发作情况:两次,就诊期间急\n[BBOX-741] 性发作:无,发作次数:0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。长期规律使用信必\n[BBOX-742] 可160/4.5ug 2吸 bid治疗,5天前开始出现咳嗽、咯痰,黄白痰,量少,难以咯出,咳嗽以\n[BBOX-743] 夜间为主。无气促,伴咽息,鼻塞、流涕、喷嚏,无发热。\n[BBOX-744] 既 往 史:鼻炎病史无规则治疗。打鼾明显。\n[BBOX-745] 过 敏 史:未发现;\n[BBOX-746] 个 人 史:否认遗传病史,吸烟10年,20支/日,2018年戒烟。偶饮酒。2021-12-20已打第\n[BBOX-747] 三针新冠疫苗。\n[BBOX-748] 体格检查:神志清,颈软,双肺呼吸音粗,可闻及散在哮鸣音,口腔粘膜无白斑。\n[BBOX-749] 专科情况:\n[BBOX-750] 辅助检查:\n[BBOX-751] 治疗项目:\n[BBOX-752] 门诊诊断:\n[BBOX-753] 1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎\n[BBOX-754] 处 置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。\n[BBOX-755] 布地奈德福莫特罗吸入粉雾剂(II)2盒 2.0吸,吸入用药,一天2次 30天\n[BBOX-756] (省采)●①⑤\n[BBOX-757] 左氧氟沙星片(省采)●⑥ 5片 0.5g,口服,每日1次(口服) 5天\n[BBOX-758] 第1页\n[BBOX-759] 广州医科大学附属第三医院\n[BBOX-760] The Third Affiliated Hospital of Guangzhou Medical University\n[BBOX-761] 门(急)诊病历信息\n[BBOX-762] 复方甲氧那明胶囊(省采)●② 1瓶 1.0粒,餐后口服,一天3次(口服) 5天\n[BBOX-763] 盐酸氨溴索分散片(省采)●⑥ 15片 30.0mg,餐后口服,一天3次(口服) 5\n[BBOX-764] 天\n[BBOX-765] 醋酸泼尼松片●②④ 6片 10.0mg,口服,每早1次(口服) 3天\n[BBOX-766] 备 注:建议在住地附近社区医疗机构随诊。\n[BBOX-767] 门诊/住院病历信息\n[BBOX-768] 就诊卡号：0\n[BBOX-769] 病历编号：\n[BBOX-770] 姓名：\n[BBOX-771] 性别：男\n[BBOX-772] 年龄：41岁\n[BBOX-773] 就诊科室：内科门诊（荔湾）\n[BBOX-774] 就诊时间：2026-02-04 11:21:11\n[BBOX-775] 主诉：支气管哮喘治疗后复查\n[BBOX-776] 现病史：2021年2月前开始出现咳嗽、哮喘，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sg 2吸 bid治疗。\n[BBOX-777] 既往史：鼻炎病史无规则治疗，打鼾明显。\n[BBOX-778] 过敏史：未发现；\n[BBOX-779] 个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。\n[BBOX-780] 体格检查：神志清，颈软，双肺呼吸音粗，可闻及散在哮鸣音，口腔粘膜无白斑。\n[BBOX-781] 专科情况：\n[BBOX-782] 辅助检查：\n[BBOX-783] 治疗项目：\n[BBOX-784] 门诊诊断：\n[BBOX-785] 1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎\n[BBOX-786] 单病种：\n[BBOX-787] 发病时间：\n[BBOX-788] 处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不遥随诊。\n[BBOX-789] 布地奈德福莫特罗吸入粉雾剂(II)(省\n[BBOX-790] 2 2.0班,吸入用药,一天2次\n[BBOX-791] 30\n[BBOX-792] 采)●①②\n[BBOX-793] 查天\n[BBOX-794] 广州医科大学附属第三医院\n[BBOX-795] 肺功能检查报告\n[BBOX-796] 地址：广州市多宝路63号 电话：020-81292126\n[BBOX-797] COSMED\n[BBOX-798] 姓名：\n[BBOX-799] 科室/床号：\n[BBOX-800] ID：\n[BBOX-801] 出生日期：1984/12/8\n[BBOX-802] 预计值：ERS 93\n[BBOX-803] 日期：2024/10/22\n[BBOX-804] 性别：Male\n[BBOX-805] 地区修正：Chinese\n[BBOX-806] 详细描述：内科门诊\n[BBOX-807] Company：\n[BBOX-808] 年龄：39\n[BBOX-809] 体重(Kg)：89.0\n[BBOX-810] 身高(cm)：177.5\n[BBOX-811] BMI(Kg/m²：28.2\n[BBOX-812] 吸烟：曾经(10/20)\n[BBOX-813] 用力肺活量 Forced Vital Capacity\n[BBOX-814] F(l/s)\n[BBOX-815] V(l)\n[BBOX-816] BEST #3 - 2024/10/22 11:03\n[BBOX-817] 沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38\n[BBOX-818] 沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39\n[BBOX-819] 沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41\n[BBOX-820] 沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38\n[BBOX-821] 沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39\n[BBOX-822] 沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41\n[BBOX-823] BEST #3 - 2024/10/22 11:03\n[BBOX-824] FVC\n[BBOX-825] PEF\n[BBOX-826] MEF75%\n[BBOX-827] MEF50%\n[BBOX-828] MEF25%\n[BBOX-829] FVC\n[BBOX-830] 6\n[BBOX-831] 7\n[BBOX-832] 8V(l)\n[BBOX-833] FEV1\n[BBOX-834] ATS\n[BBOX-835] 12t(s)\n[BBOX-836] -1\n[BBOX-837] 0\n[BBOX-838] 1\n[BBOX-839] 2\n[BBOX-840] 3\n[BBOX-841] 4\n[BBOX-842] 5\n[BBOX-843] 6\n[BBOX-844] 7\n[BBOX-845] 8\n[BBOX-846] 9\n[BBOX-847] 10\n[BBOX-848] 11\n[BBOX-849] 12\n[BBOX-850] 1\n[BBOX-851] 2\n[BBOX-852] 3\n[BBOX-853] 4\n[BBOX-854] 5\n[BBOX-855] 6\n[BBOX-856] 7\n[BBOX-857] 8\n[BBOX-858] 9\n[BBOX-859] 10\n[BBOX-860] 11\n[BBOX-861] 12\n[BBOX-862] 13\n[BBOX-863] 14\n[BBOX-864] 1\n[BBOX-865] 2\n[BBOX-866] 3\n[BBOX-867] 4\n[BBOX-868] 5\n[BBOX-869] 6\n[BBOX-870] 7\n[BBOX-871] 8\n[BBOX-872] 9\n[BBOX-873] 10\n[BBOX-874] 11\n[BBOX-875] 12\n[BBOX-876] 13\n[BBOX-877] 14\n[BBOX-878] 15\n[BBOX-879] 16\n[BBOX-880] 17\n[BBOX-881] 18\n[BBOX-882] 19\n[BBOX-883] 20\n[BBOX-884] 21\n[BBOX-885] 22\n[BBOX-886] 23\n[BBOX-887] 24\n[BBOX-888] 25\n[BBOX-889] 26\n[BBOX-890] 27\n[BBOX-891] 28\n[BBOX-892] 29\n[BBOX-893] 30\n[BBOX-894] 31\n[BBOX-895] 32\n[BBOX-896] 33\n[BBOX-897] 34\n[BBOX-898] 35\n[BBOX-899] 36\n[BBOX-900] 37\n[BBOX-901] 38\n[BBOX-902] 39\n[BBOX-903] 40\n[BBOX-904] 41\n[BBOX-905] 42\n[BBOX-906] 43\n[BBOX-907] 44\n[BBOX-908] 45\n[BBOX-909] 46\n[BBOX-910] 47\n[BBOX-911] 48\n[BBOX-912] 49\n[BBOX-913] 50\n[BBOX-914] 51\n[BBOX-915] 52\n[BBOX-916] 53\n[BBOX-917] 54\n[BBOX-918] 55\n[BBOX-919] 56\n[BBOX-920] 57\n[BBOX-921] 58\n[BBOX-922] 59\n[BBOX-923] 60\n[BBOX-924] 61\n[BBOX-925] 62\n[BBOX-926] 63\n[BBOX-927] 64\n[BBOX-928] 65\n[BBOX-929] 66\n[BBOX-930] 67\n[BBOX-931] 68\n[BBOX-932] 69\n[BBOX-933] 70\n[BBOX-934] 71\n[BBOX-935] 72\n[BBOX-936] 73\n[BBOX-937] 74\n[BBOX-938] 75\n[BBOX-939] 76\n[BBOX-940] 77\n[BBOX-941] 78\n[BBOX-942] 79\n[BBOX-943] 80\n[BBOX-944] 81\n[BBOX-945] 82\n[BBOX-946] 83\n[BBOX-947] 84\n[BBOX-948] 85\n[BBOX-949] 86\n[BBOX-950] 87\n[BBOX-951] 88\n[BBOX-952] 89\n[BBOX-953] 90\n[BBOX-954] 91\n[BBOX-955] 92\n[BBOX-956] 93\n[BBOX-957] 94\n[BBOX-958] 95\n[BBOX-959] 96\n[BBOX-960] 97\n[BBOX-961] 98\n[BBOX-962] 99\n[BBOX-963] 100\n[BBOX-964] 101\n[BBOX-965] 102\n[BBOX-966] 103\n[BBOX-967] 104\n[BBOX-968] 105\n[BBOX-969] 106\n[BBOX-970] 107\n[BBOX-971] 108\n[BBOX-972] 109\n[BBOX-973] 110\n[BBOX-974] 111\n[BBOX-975] 112\n[BBOX-976] 113\n[BBOX-977] 114\n[BBOX-978] 115\n[BBOX-979] 116\n[BBOX-980] 117\n[BBOX-981] 118\n[BBOX-982] 119\n[BBOX-983] 120\n[BBOX-984] 121\n[BBOX-985] 122\n[BBOX-986] 123\n[BBOX-987] 124\n[BBOX-988] 125\n[BBOX-989] 126\n[BBOX-990] 127\n[BBOX-991] 128\n[BBOX-992] 129\n[BBOX-993] 130\n[BBOX-994] 131\n[BBOX-995] 132\n[BBOX-996] 133\n[BBOX-997] 134\n[BBOX-998] 135\n[BBOX-999] 136\n[BBOX-1000] 137\n[BBOX-1001] 138\n[BBOX-1002] 139\n[BBOX-1003] 140\n[BBOX-1004] 141\n[BBOX-1005] 142\n[BBOX-1006] 143\n[BBOX-1007] 144\n[BBOX-1008] 145\n[BBOX-1009] 146\n[BBOX-1010] 147\n[BBOX-1011] 148\n[BBOX-1012] 149\n[BBOX-1013] 150\n[BBOX-1014] 151\n[BBOX-1015] 152\n[BBOX-1016] 153\n[BBOX-1017] 154\n[BBOX-1018] 155\n[BBOX-1019] 156\n[BBOX-1020] 157\n[BBOX-1021] 158\n[BBOX-1022] 159\n[BBOX-1023] 160\n[BBOX-1024] 161\n[BBOX-1025] 162\n[BBOX-1026] 163\n[BBOX-1027] 164\n[BBOX-1028] 165\n[BBOX-1029] 166\n[BBOX-1030] 167\n[BBOX-1031] 168\n[BBOX-1032] 169\n[BBOX-1033] 170\n[BBOX-1034] 171\n[BBOX-1035] 172\n[BBOX-1036] 173\n[BBOX-1037] 174\n[BBOX-1038] 175\n[BBOX-1039] 176\n[BBOX-1040] 177\n[BBOX-1041] 178\n[BBOX-1042] 179\n[BBOX-1043] 180\n[BBOX-1044] 181\n[BBOX-1045] 182\n[BBOX-1046] 183\n[BBOX-1047] 184\n[BBOX-1048] 185\n[BBOX-1049] 186\n[BBOX-1050] 187\n[BBOX-1051] 188\n[BBOX-1052] 189\n[BBOX-1053] 190\n[BBOX-1054] 191\n[BBOX-1055] 192\n[BBOX-1056] 193\n[BBOX-1057] 194\n[BBOX-1058] 195\n[BBOX-1059] 196\n[BBOX-1060] 197\n[BBOX-1061] 198\n[BBOX-1062] 199\n[BBOX-1063] 200\n[BBOX-1064] 201\n[BBOX-1065] 202\n[BBOX-1066] 203\n[BBOX-1067] 204\n[BBOX-1068] 205\n[BBOX-1069] 206\n[BBOX-1070] 207\n[BBOX-1071] 208\n[BBOX-1072] 209\n[BBOX-1073] 210\n[BBOX-1074] 211\n[BBOX-1075] 212\n[BBOX-1076] 213\n[BBOX-1077] 214\n[BBOX-1078] 215\n[BBOX-1079] 216\n[BBOX-1080] 217\n[BBOX-1081] 218\n[BBOX-1082] 219\n[BBOX-1083] 220\n[BBOX-1084] 221\n[BBOX-1085] 222\n[BBOX-1086] 223\n[BBOX-1087] 224\n[BBOX-1088] 225\n[BBOX-1089] 226\n[BBOX-1090] 227\n[BBOX-1091] 228\n[BBOX-1092] 229\n[BBOX-1093] 230\n[BBOX-1094] 231\n[BBOX-1095] 232\n[BBOX-1096] 233\n[BBOX-1097] 234\n[BBOX-1098] 235\n[BBOX-1099] 236\n[BBOX-1100] 237\n[BBOX-1101] 238\n[BBOX-1102] 239\n[BBOX-1103] 240\n[BBOX-1104] 241\n[BBOX-1105] 242\n[BBOX-1106] 243\n[BBOX-1107] 244\n[BBOX-1108] 245\n[BBOX-1109] 246\n[BBOX-1110] 247\n[BBOX-1111] 248\n[BBOX-1112] 249\n[BBOX-1113] 250\n[BBOX-1114] 251\n[BBOX-1115] 252\n[BBOX-1116] 253\n[BBOX-1117] 254\n[BBOX-1118] 255\n[BBOX-1119] 256\n[BBOX-1120] 257\n[BBOX-1121] 258\n[BBOX-1122] 259\n[BBOX-1123] 260\n[BBOX-1124] 261\n[BBOX-1125] 262\n[BBOX-1126] 263\n[BBOX-1127] 264\n[BBOX-1128] 265\n[BBOX-1129] 266\n[BBOX-1130] 267\n[BBOX-1131] 268\n[BBOX-1132] 269\n[BBOX-1133] 270\n[BBOX-1134] 271\n[BBOX-1135] 272\n[BBOX-1136] 273\n[BBOX-1137] 274\n[BBOX-1138] 275\n[BBOX-1139] 276\n[BBOX-1140] 277\n[BBOX-1141] 278\n[BBOX-1142] 279\n[BBOX-1143] 280\n[BBOX-1144] 281\n[BBOX-1145] 282\n[BBOX-1146] 283\n[BBOX-1147] 284\n[BBOX-1148] 285\n[BBOX-1149] 286\n[BBOX-1150] 287\n[BBOX-1151] 288\n[BBOX-1152] 289\n[BBOX-1153] 290\n[BBOX-1154] 291\n[BBOX-1155] 292\n[BBOX-1156] 293\n[BBOX-1157] 294\n[BBOX-1158] 295\n[BBOX-1159] 296\n[BBOX-1160] 297\n[BBOX-1161] 298\n[BBOX-1162] 299\n[BBOX-1163] 300\n[BBOX-1164] 301\n[BBOX-1165] 302\n[BBOX-1166] 303\n[BBOX-1167] 304\n[BBOX-1168] 305\n[BBOX-1169] 306\n[BBOX-1170] 307\n[BBOX-1171] 308\n[BBOX-1172] 309\n[BBOX-1173] 310\n[BBOX-1174] 311\n[BBOX-1175] 312\n[BBOX-1176] 313\n[BBOX-1177] 314\n[BBOX-1178] 315\n[BBOX-1179] 316\n[BBOX-1180] 317\n[BBOX-1181] 318\n[BBOX-1182] 319\n[BBOX-1183] 320\n[BBOX-1184] 321\n[BBOX-1185] 322\n[BBOX-1186] 323\n[BBOX-1187] 324\n[BBOX-1188] 325\n[BBOX-1189] 326\n[BBOX-1190] 327\n[BBOX-1191] 328\n[BBOX-1192] 329\n[BBOX-1193] 330\n[BBOX-1194] 331\n[BBOX-1195] 332\n[BBOX-1196] 333\n[BBOX-1197] 334\n[BBOX-1198] 335\n[BBOX-1199] 336\n[BBOX-1200] 337\n[BBOX-1201] 338\n[BBOX-1202] 339\n[BBOX-1203] 340\n[BBOX-1204] 341\n[BBOX-1205] 342\n[BBOX-1206] 343\n[BBOX-1207] 344\n[BBOX-1208] 345\n[BBOX-1209] 346\n[BBOX-1210] 347\n[BBOX-1211] 348\n[BBOX-1212] 349\n[BBOX-1213] 350\n[BBOX-1214] 351\n[BBOX-1215] 352\n[BBOX-1216] 353\n[BBOX-1217] 354\n[BBOX-1218] 355\n[BBOX-1219] 356\n[BBOX-1220] 357\n[BBOX-1221] 358\n[BBOX-1222] 359\n[BBOX-1223] 360\n[BBOX-1224] 361\n[BBOX-1225] 362\n[BBOX-1226] 363\n[BBOX-1227] 364\n[BBOX-1228] 365\n[BBOX-1229] 366\n[BBOX-1230] 367\n[BBOX-1231] 368\n[BBOX-1232] 369\n[BBOX-1233] 370\n[BBOX-1234] 371\n[BBOX-1235] 372\n[BBOX-1236] 373\n[BBOX-1237] 374\n[BBOX-1238] 375\n[BBOX-1239] 376\n[BBOX-1240] 377\n[BBOX-1241] 378\n[BBOX-1242] 379\n[BBOX-1243] 380\n[BBOX-1244] 381\n[BBOX-1245] 382\n[BBOX-1246] 383\n[BBOX-1247] 384\n[BBOX-1248] 385\n[BBOX-1249] 386\n[BBOX-1250] 387\n[BBOX-1251] 388\n[BBOX-1252] 389\n[BBOX-1253] 390\n[BBOX-1254] 391\n[BBOX-1255] 392\n[BBOX-1256] 393\n[BBOX-1257] 394\n[BBOX-1258] 395\n[BBOX-1259] 396\n[BBOX-1260] 397\n[BBOX-1261] 398\n[BBOX-1262] 399\n[BBOX-1263] 400\n[BBOX-1264] 401\n[BBOX-1265] 402\n[BBOX-1266] 403\n[BBOX-1267] 404\n[BBOX-1268] 405\n[BBOX-1269] 406\n[BBOX-1270] 407\n[BBOX-1271] 408\n[BBOX-1272] 409\n[BBOX-1273] 410\n[BBOX-1274] 411\n[BBOX-1275] 412\n[BBOX-1276] 413\n[BBOX-1277] 414\n[BBOX-1278] 415\n[BBOX-1279] 416\n[BBOX-1280] 417\n[BBOX-1281] 418\n[BBOX-1282] 419\n[BBOX-1283] 420\n[BBOX-1284] 421\n[BBOX-1285] 422\n[BBOX-1286] 423\n[BBOX-1287] 424\n[BBOX-1288] 425\n[BBOX-1289] 426\n[BBOX-1290] 427\n[BBOX-1291] 428\n[BBOX-1292] 429\n[BBOX-1293] 430\n[BBOX-1294] 431\n[BBOX-1295] 432\n[BBOX-1296] 433\n[BBOX-1297] 434\n[BBOX-1298] 435\n[BBOX-1299] 436\n[BBOX-1300] 437\n[BBOX-1301] 438\n[BBOX-1302] 439\n[BBOX-1303] 440\n[BBOX-1304] 441\n[BBOX-1305] 442\n[BBOX-1306] 443\n[BBOX-1307] 444\n[BBOX-1308] 445\n[BBOX-1309] 446\n[BBOX-1310] 447\n[BBOX-1311] 448\n[BBOX-1312] 449\n[BBOX-1313] 450\n[BBOX-1314] 451\n[BBOX-1315] 452\n[BBOX-1316] 453\n[BBOX-1317] 454\n[BBOX-1318] 455\n[BBOX-1319] 456\n[BBOX-1320] 457\n[BBOX-1321] 458\n[BBOX-1322] 459\n[BBOX-1323] 460\n[BBOX-1324] 461\n[BBOX-1325] 462\n[BBOX-1326] 463\n[BBOX-1327] 464\n[BBOX-1328] 465\n[BBOX-1329] 466\n[BBOX-1330] 467\n[BBOX-1331] 468\n[BBOX-1332] 469\n[BBOX-1333] 470\n[BBOX-1334] 471\n[BBOX-1335] 472\n[BBOX-1336] 473\n[BBOX-1337] 474\n[BBOX-1338] 475\n[BBOX-1339] 476\n[BBOX-1340] 477\n[BBOX-1341] 478\n[BBOX-1342] 479\n[BBOX-1343] 480\n[BBOX-1344] 481\n[BBOX-1345] 482\n[BBOX-1346] 483\n[BBOX-1347] 484\n[BBOX-1348] 485\n[BBOX-1349] 486\n[BBOX-1350] 487\n[BBOX-1351] 488\n[BBOX-1352] 489\n[BBOX-1353] 490\n[BBOX-1354] 491\n[BBOX-1355] 492\n[BBOX-1356] 493\n[BBOX-1357] 494\n[BBOX-1358] 495\n[BBOX-1359] 496\n[BBOX-1360] 497\n[BBOX-1361] 498\n[BBOX-1362] 499\n[BBOX-1363] 500\n[BBOX-1364] 501\n[BBOX-1365] 502\n[BBOX-1366] 503\n[BBOX-1367] 504\n[BBOX-1368] 505\n[BBOX-1369] 506\n[BBOX-1370] 507\n[BBOX-1371] 508\n[BBOX-1372] 509\n[BBOX-1373] 510\n[BBOX-1374] 511\n[BBOX-1375] 512\n[BBOX-1376] 513\n[BBOX-1377] 514\n[BBOX-1378] 515\n[BBOX-1379] 516\n[BBOX-1380] 517\n[BBOX-1381] 518\n[BBOX-1382] 519\n[BBOX-1383] 520\n[BBOX-1384] 521\n[BBOX-1385] 522\n[BBOX-1386] 523\n[BBOX-1387] 524\n[BBOX-1388] 525\n[BBOX-1389] 526\n[BBOX-1390] 527\n[BBOX-1391] 528\n[BBOX-1392] 529\n[BBOX-1393] 530\n[BBOX-1394] 531\n[BBOX-1395] 532\n[BBOX-1396] 533\n[BBOX-1397] 534\n[BBOX-1398] 535\n[BBOX-1399] 536\n[BBOX-1400] 537\n[BBOX-1401] 538\n[BBOX-1402] 539\n[BBOX-1403] 540\n[BBOX-1404] 541\n[BBOX-1405] 542\n[BBOX-1406] 543\n[BBOX-1407] 544\n[BBOX-1408] 545\n[BBOX-1409] 546\n[BBOX-1410] 547\n[BBOX-1411] 548\n[BBOX-1412] 549\n[BBOX-1413] 550\n[BBOX-1414] 551\n[BBOX-1415] 552\n[BBOX-1416] 553\n[BBOX-1417] 554\n[BBOX-1418] 555\n[BBOX-1419] 556\n[BBOX-1420] 557\n[BBOX-1421] 558\n[BBOX-1422] 559\n[BBOX-1423] 560\n[BBOX-1424] 561\n[BBOX-1425] 562\n[BBOX-1426] 563\n[BBOX-1427] 564\n[BBOX-1428] 565\n[BBOX-1429] 566\n[BBOX-1430] 567\n[BBOX-1431] 568\n[BBOX-1432] 569\n[BBOX-1433] 570\n[BBOX-1434] 571\n[BBOX-1435] 572\n[BBOX-1436] 573\n[BBOX-1437] 574\n[BBOX-1438] 575\n[BBOX-1439] 576\n[BBOX-1440] 577\n[BBOX-1441] 578\n[BBOX-1442] 579\n[BBOX-1443] 580\n[BBOX-1444] 581\n[BBOX-1445] 582\n[BBOX-1446] 583\n[BBOX-1447] 584\n[BBOX-1448] 585\n[BBOX-1449] 586\n[BBOX-1450] 587\n[BBOX-1451] 588\n[BBOX-1452] 589\n[BBOX-1453] 590\n[BBOX-1454] 591\n[BBOX-1455] 592\n[BBOX-1456] 593\n[BBOX-1457] 594\n[BBOX-1458] 595\n[BBOX-1459] 596\n[BBOX-1460] 597\n[BBOX-1461] 598\n[BBOX-1462] 599\n[BBOX-1463] 600\n[BBOX-1464] 601\n[BBOX-1465] 602\n[BBOX-1466] 603\n[BBOX-1467] 604\n[BBOX-1468] 605\n[BBOX-1469] 606\n[BBOX-1470] 607\n[BBOX-1471] 608\n[BBOX-1472] 609\n[BBOX-1473] 610\n[BBOX-1474] 611\n[BBOX-1475] 612\n[BBOX-1476] 613\n[BBOX-1477] 614\n[BBOX-1478] 615\n[BBOX-1479] 616\n[BBOX-1480] 617\n[BBOX-1481] 618\n[BBOX-1482] 619\n[BBOX-1483] 620\n[BBOX-1484] 621\n[BBOX-1485] 622\n[BBOX-1486] 623\n[BBOX-1487] 624\n[BBOX-1488] 625\n[BBOX-1489] 626\n[BBOX-1490] 627\n[BBOX-1491] 628\n[BBOX-1492] 629\n[BBOX-1493] 630\n[BBOX-1494] 631\n[BBOX-1495] 632\n[BBOX-1496] 633\n[BBOX-1497] 634\n[BBOX-1498] 635\n[BBOX-1499] 636\n[BBOX-1500] 637\n[BBOX-1501] 638\n[BBOX-1502] 639\n[BBOX-1503] 640\n[BBOX-1504] 641\n[BBOX-1505] 642\n[BBOX-1506] 643\n[BBOX-1507] 644\n[BBOX-1508] 645\n[BBOX-1509] 646\n[BBOX-1510] 647\n[BBOX-1511] 648\n[BBOX-1512] 649\n[BBOX-1513] 650\n[BBOX-1514] 651\n[BBOX-1515] 652\n[BBOX-1516] 653\n[BBOX-1517] 654\n[BBOX-1518] 655\n[BBOX-1519] 656\n[BBOX-1520] 657\n[BBOX-1521] 658\n[BBOX-1522] 659\n[BBOX-1523] 660\n[BBOX-1524] 661\n[BBOX-1525] 662\n[BBOX-1526] 663\n[BBOX-1527] 664\n[BBOX-1528] 665\n[BBOX-1529] 666\n[BBOX-1530] 667\n[BBOX-1531] 668\n[BBOX-1532] 669\n[BBOX-1533] 670\n[BBOX-1534] 671\n[BBOX-1535] 672\n[BBOX-1536] 673\n[BBOX-1537] 674\n[BBOX-1538] 675\n[BBOX-1539] 676\n[BBOX-1540] 677\n[BBOX-1541] 678\n[BBOX-1542] 679\n[BBOX-1543] 680\n[BBOX-1544] 681\n[BBOX-1545] 682\n[BBOX-1546] 683\n[BBOX-1547] 684\n[BBOX-1548] 685\n[BBOX-1549] 686\n[BBOX-1550] 687\n[BBOX-1551] 688\n[BBOX-1552] 689\n[BBOX-1553] 690\n[BBOX-1554] 691\n[BBOX-1555] 692\n[BBOX-1556] 693\n[BBOX-1557] 694\n[BBOX-1558] 695\n[BBOX-1559] 696\n[BBOX-1560] 697\n[BBOX-1561] 698\n[BBOX-1562] 699\n[BBOX-1563] 700\n[BBOX-1564] 701\n[BBOX-1565] 702\n[BBOX-1566] 703\n[BBOX-1567] 704\n[BBOX-1568] 705\n[BBOX-1569] 706\n[BBOX-1570] 707\n[BBOX-1571] 708\n[BBOX-1572] 709\n[BBOX-1573] 710\n[BBOX-1574] 711\n[BBOX-1575] 712\n[BBOX-1576] 713\n[BBOX-1577] 714\n[BBOX-1578] 715\n[BBOX-1579] 716\n[BBOX-1580] 717\n[BBOX-1581] 718\n[BBOX-1582] 719\n[BBOX-1583] 720\n[BBOX-1584] 721\n[BBOX-1585] 722\n[BBOX-1586] 723\n[BBOX-1587] 724\n[BBOX-1588] 725\n[BBOX-1589] 726\n[BBOX-1590] 727\n[BBOX-1591] 728\n[BBOX-1592] 729\n[BBOX-1593] 730\n[BBOX-1594] 731\n[BBOX-1595] 732\n[BBOX-1596] 733\n[BBOX-1597] 734\n[BBOX-1598] 735\n[BBOX-1599] 736\n[BBOX-1600] 737\n[BBOX-1601] 738\n[BBOX-1602] 739\n[BBOX-1603] 740\n[BBOX-1604] 741\n[BBOX-1605] 742\n[BBOX-1606] 743\n[BBOX-1607] 744\n[BBOX-1608] 745\n[BBOX-1609] 746\n[BBOX-1610] 747\n[BBOX-1611] 748\n[BBOX-1612] 749\n[BBOX-1613] 750\n[BBOX-1614] 751\n[BBOX-1615] 752\n[BBOX-1616] 753\n[BBOX-1617] 754\n[BBOX-1618] 755\n[BBOX-1619] 756\n[BBOX-1620] 757\n[BBOX-1621] 758\n[BBOX-1622] 759\n[BBOX-1623] 760\n[BBOX-1624] 761\n[BBOX-1625] 762\n[BBOX-1626] 763\n[BBOX-1627] 764\n[BBOX-1628] 765\n[BBOX-1629] 766\n[BBOX-1630] 767\n[BBOX-1631] 768\n[BBOX-1632] 769\n[BBOX-1633] 770\n[BBOX-1634] 771\n[BBOX-1635] 772\n[BBOX-1636] 773\n[BBOX-1637] 774\n[BBOX-1638] 775\n[BBOX-1639] 776\n[BBOX-1640] 777\n[BBOX-1641] 778\n[BBOX-1642] 779\n[BBOX-1643] 780\n[BBOX-1644] 781\n[BBOX-1645] 782\n[BBOX-1646] 783\n[BBOX-1647] 784\n[BBOX-1648] 785\n[BBOX-1649] 786\n[BBOX-1650] 787\n[BBOX-1651] 788\n[BBOX-1652] 789\n[BBOX-1653] 790\n[BBOX-1654] 791\n[BBOX-1655] 792\n[BBOX-1656] 793\n[BBOX-1657] 794\n[BBOX-1658] 795\n[BBOX-1659] 796\n[BBOX-1660] 797\n[BBOX-1661] 798\n[BBOX-1662] 799\n[BBOX-1663] 800\n[BBOX-1664] 801\n[BBOX-1665] 802\n[BBOX-1666] 803\n[BBOX-1667] 804\n[BBOX-1668] 805\n[BBOX-1669] 806\n[BBOX-1670] 807\n[BBOX-1671] 808\n[BBOX-1672] 809\n[BBOX-1673] 810\n[BBOX-1674] 811\n[BBOX-1675] 812\n[BBOX-1676] 813\n[BBOX-1677] 814\n[BBOX-1678] 815\n[BBOX-1679] 816\n[BBOX-1680] 817\n[BBOX-1681] 818\n[BBOX-1682] 819\n[BBOX-1683] 820\n[BBOX-1684] 821\n[BBOX-1685] 822\n[BBOX-1686] 823\n[BBOX-1687] 824\n[BBOX-1688] 825\n[BBOX-1689] 826\n[BBOX-1690] 827\n[BBOX-1691] 828\n[BBOX-1692] 829\n[BBOX-1693] 830\n[BBOX-1694] 831\n[BBOX-1695] 832\n[BBOX-1696] 833\n[BBOX-1697] 834\n[BBOX-1698] 835\n[BBOX-1699] 836\n[BBOX-1700] 837\n[BBOX-1701] 838\n[BBOX-1702] 839\n[BBOX-1703] 840\n[BBOX-1704] 841\n[BBOX-1705] 842\n[BBOX-1706] 843\n[BBOX-1707] 844\n[BBOX-1708] 845\n[BBOX-1709] 846\n[BBOX-1710] 847\n[BBOX-1711] 848\n[BBOX-1712] 849\n[BBOX-1713] 850\n[BBOX-1714] 851\n[BBOX-1715] 852\n[BBOX-1716] 853\n[BBOX-1717] 854\n[BBOX-1718] 855\n[BBOX-1719] 856\n[BBOX-1720] 857\n[BBOX-1721] 858\n[BBOX-1722] 859\n[BBOX-1723] 860\n[BBOX-1724] 861\n[BBOX-1725] 862\n[BBOX-1726] 863\n[BBOX-1727] 864\n[BBOX-1728] 865\n[BBOX-1729] 866\n[BBOX-1730] 867\n[BBOX-1731] 868\n[BBOX-1732] 869\n[BBOX-1733] 870\n[BBOX-1734] 871\n[BBOX-1735] 872\n[BBOX-1736] 873\n[BBOX-1737] 874\n[BBOX-1738] 875\n[BBOX-1739] 876\n[BBOX-1740] 877\n[BBOX-1741] 878\n[BBOX-1742] 879\n[BBOX-1743] 880\n[BBOX-1744] 881\n[BBOX-1745] 882\n[BBOX-1746] 883\n[BBOX-1747] 884\n[BBOX-1748] 885\n[BBOX-1749] 886\n[BBOX-1750] 887\n[BBOX-1751] 888\n[BBOX-1752] 889\n[BBOX-1753] 890\n[BBOX-1754] 891\n[BBOX-1755] 892\n[BBOX-1756] 893\n[BBOX-1757] 894\n[BBOX-1758] 895\n[BBOX-1759] 896\n[BBOX-1760] 897\n[BBOX-1761] 898\n[BBOX-1762] 899\n[BBOX-1763] 900\n[BBOX-1764] 901\n[BBOX-1765] 902\n[BBOX-1766] 903\n[BBOX-1767] 904\n[BBOX-1768] 905\n[BBOX-1769] 906\n[BBOX-1770] 907\n[BBOX-1771] 908\n[BBOX-1772] 909\n[BBOX-1773] 910\n[BBOX-1774] 911\n[BBOX-1775] 912\n[BBOX-1776] 913\n[BBOX-1777] 914\n[BBOX-1778] 915\n[BBOX-1779] 916\n[BBOX-1780] 917\n[BBOX-1781] 918\n[BBOX-1782] 919\n[BBOX-1783] 920\n[BBOX-1784] 921\n[BBOX-1785] 922\n[BBOX-1786] 923\n[BBOX-1787] 924\n[BBOX-1788] 925\n[BBOX-1789] 926\n[BBOX-1790] 927\n[BBOX-1791] 928\n[BBOX-1792] 929\n[BBOX-1793] 930\n[BBOX-1794] 931\n[BBOX-1795] 932\n[BBOX-1796] 933\n[BBOX-1797] 934\n[BBOX-1798] 935\n[BBOX-1799] 936\n[BBOX-1800] 937\n[BBOX-1801] 938\n[BBOX-1802] 939\n[BBOX-1803] 940\n[BBOX-1804] 941\n[BBOX-1805] 942\n[BBOX-1806] 943\n[BBOX-1807] 944\n[BBOX-1808] 945\n[BBOX-1809] 946\n[BBOX-1810] 947\n[BBOX-1811] 948\n[BBOX-1812] 949\n[BBOX-1813] 950\n[BBOX-1814] 951\n[BBOX-1815] 952\n[BBOX-1816] 953\n[BBOX-1817] 954\n[BBOX-1818] 955\n[BBOX-1819] 956\n[BBOX-1820] 957\n[BBOX-1821] 958\n[BBOX-1822] 959\n[BBOX-1823] 960\n[BBOX-1824] 961\n[BBOX-1825] 962\n[BBOX-1826] 963\n[BBOX-1827] 964\n[BBOX-1828] 965\n[BBOX-1829] 966\n[BBOX-1830] 967\n[BBOX-1831] 968\n[BBOX-1832] 969\n[BBOX-1833] 970\n[BBOX-1834] 971\n[BBOX-1835] 972\n[BBOX-1836] 973\n[BBOX-1837] 974\n[BBOX-1838] 975\n[BBOX-1839] 976\n[BBOX-1840] 977\n[BBOX-1841] 978\n[BBOX-1842] 979\n[BBOX-1843] 980\n[BBOX-1844] 981\n[BBOX-1845] 982\n[BBOX-1846] 983\n[BBOX-1847] 984\n[BBOX-1848] 985\n[BBOX-1849] 986\n[BBOX-1850] 987\n[BBOX-1851] 988\n[BBOX-1852] 989\n[BBOX-1853] 990\n[BBOX-1854] 991\n[BBOX-1855] 992\n[BBOX-1856] 993\n[BBOX-1857] 994\n[BBOX-1858] 995\n[BBOX-1859] 996\n[BBOX-1860] 997\n[BBOX-1861] 998\n[BBOX-1862] 999\n[BBOX-1863] 1000\n[BBOX-1864] 1001\n[BBOX-1865] 1002\n[BBOX-1866] 1003\n[BBOX-1867] 1004\n[BBOX-1868] 1005\n[BBOX-1869] 1006\n[BBOX-1870] 1007\n[BBOX-1871] 1008\n[BBOX-1872] 1009\n[BBOX-1873] 1010\n[BBOX-1874] 1011\n[BBOX-1875] 1012\n[BBOX-1876] 1013\n[BBOX-1877] 1014\n[BBOX-1878] 1015\n[BBOX-1879] 1016\n[BBOX-1880] 1017\n[BBOX-1881] 1018\n[BBOX-1882] 1019\n[BBOX-1883] 1020\n[BBOX-1884] 1021\n[BBOX-1885] 1022\n[BBOX-1886] 1023\n[BBOX-1887] 1024\n[BBOX-1888] 1025\n[BBOX-1889] 1026\n[BBOX-1890] 1027\n[BBOX-1891] 1028\n[BBOX-1892] 1029\n[BBOX-1893] 1030\n[BBOX-1894] 1031\n[BBOX-1895] 1032\n[BBOX-1896] 1033\n[BBOX-1897] 1034\n[BBOX-1898] 1035\n[BBOX-1899] 1036\n[BBOX-1900] 1037\n[BBOX-1901] 1038\n[BBOX-1902] 1039\n[BBOX-1903] 1040\n[BBOX-1904] 1041\n[BBOX-1905] 1042\n[BBOX-1906] 1043\n[BBOX-1907] 1044\n[BBOX-1908] 1045\n[BBOX-1909] 1046\n[BBOX-1910] 1047\n[BBOX-1911] 1048\n[BBOX-1912] 1049\n[BBOX-1913] 1050\n[BBOX-1914] 1051\n[BBOX-1915] 1052\n[BBOX-1916] 1053\n[BBOX-1917] 1054\n[BBOX-1918] 1055\n[BBOX-1919] 1056\n[BBOX-1920] 1057\n[BBOX-1921] 1058\n[BBOX-1922] 1059\n[BBOX-1923] 1060\n[BBOX-1924] 1061\n[BBOX-1925] 1062\n[BBOX-1926] 1063\n[BBOX-1927] 1064\n[BBOX-1928] 1065\n[BBOX-1929] 1066\n[BBOX-1930] 1067\n[BBOX-1931] 1068\n[BBOX-1932] 1069\n[BBOX-1933] 1070\n[BBOX-1934] 1071\n[BBOX-1935] 1072\n[BBOX-1936] 1073\n[BBOX-1937] 1074\n[BBOX-1938] 1075\n[BBOX-1939] 1076\n[BBOX-1940] 1077\n[BBOX-1941] 1078\n[BBOX-1942] 1079\n[BBOX-1943] 1080\n[BBOX-1944] 1081\n[BBOX-1945] 1082\n[BBOX-1946] 1083\n[BBOX-1947] 1084\n[BBOX-1948] 1085\n[BBOX-1949] 1086\n[BBOX-1950] 1087\n[BBOX-1951] 1088\n[BBOX-1952] 1089\n[BBOX-1953] 1090\n[BBOX-1954] 1091\n[BBOX-1955] 1092\n[BBOX-1956] 1093\n[BBOX-1957] 1094\n[BBOX-1958] 1095\n[BBOX-1959] 1096\n[BBOX-1960] 1097\n[BBOX-1961] 1098\n[BBOX-1962] 1099\n[BBOX-1963] 1100\n[BBOX-1964] 1101\n[BBOX-1965] 1102\n[BBOX-1966] 1103\n[BBOX-1967] 1104\n[BBOX-1968] 1105\n[BBOX-1969] 1106\n[BBOX-1970] 1107\n[BBOX-1971] 1108\n[BBOX-1972] 1109\n[BBOX-1973] 1110\n[BBOX-1974] 1111\n[BBOX-1975] 1112\n[BBOX-1976] 1113\n[BBOX-1977] 1114\n[BBOX-1978] 1115\n[BBOX-1979] 1116\n[BBOX-1980] 1117\n[BBOX-1981] 1118\n[BBOX-1982] 1119\n[BBOX-1983] 1120\n[BBOX-1984] 1121\n[BBOX-1985] 1122\n[BBOX-1986] 1123\n[BBOX-1987] 1124\n[BBOX-1988] 1125\n[BBOX-1989] 1126\n[BBOX-1990] 1127\n[BBOX-1991] 1128\n[BBOX-1992] 1129\n[BBOX-1993] 1130\n[BBOX-1994] 1131\n[BBOX-1995] 1132\n[BBOX-1996] 1133\n[BBOX-1997] 1134\n[BBOX-1998] 1135\n[BBOX-1999] 1136\n[BBOX-2000] 1137\n[BBOX-2001] 1138\n[BBOX-2002] 1139\n[BBOX-2003] 1140\n[BBOX-2004] 1141\n[BBOX-2005] 1142\n[BBOX-2006] 1143\n[BBOX-2007] 1144\n[BBOX-2008] 1145\n[BBOX-2009] 1146\n[BBOX-2010] 1147\n[BBOX-2011] 1148\n[BBOX-2012] 1149\n[BBOX-2013] 1150\n[BBOX-2014] 1151\n[BBOX-2015] 1152\n[BBOX-2016] 1153\n[BBOX-2017] 1154\n[BBOX-2018] 1155\n[BBOX-2019] 1156\n[BBOX-2020] 1157\n[BBOX-2021] 1158\n[BBOX-2022] 1159\n[BBOX-2023] 1160\n[BBOX-2024] 1161\n[BBOX-2025] 1162\n[BBOX-2026] 1163\n[BBOX-2027] 1164\n[BBOX-2028] 1165\n[BBOX-2029] 1166\n[BBOX-2030] 1167\n[BBOX-2031] 1168\n[BBOX-2032] 1169\n[BBOX-2033] 1170\n[BBOX-2034] 1171\n[BBOX-2035] 1172\n[BBOX-2036] 1173\n[BBOX-2037] 1174\n[BBOX-2038] 1175\n[BBOX-2039] 1176\n[BBOX-2040] 1177\n[BBOX-2041] 1178\n[BBOX-2042] 1179\n[BBOX-2043] 1180\n[BBOX-2044] 1181\n[BBOX-2045] 1182\n[BBOX-2046] 1183\n[BBOX-2047] 1184\n[BBOX-2048] 1185\n[BBOX-2049] 1186\n[BBOX-2050] 1187\n[BBOX-2051] 1188\n[BBOX-2052] 1189\n[BBOX-2053] 1190\n[BBOX-2054] 1191\n[BBOX-2055] 1192\n[BBOX-2056] 1193\n[BBOX-2057] 1194\n[BBOX-2058] 1195\n[BBOX-2059] 1196\n[BBOX-2060] 1197\n[BBOX-2061] 1198\n[BBOX-2062] 1199\n[BBOX-2063] 1200\n[BBOX-2064] 1201\n[BBOX-2065] 1202\n[BBOX-2066] 1203\n[BBOX-2067] 1204\n[BBOX-2068] 1205\n[BBOX-2069] 1206\n[BBOX-2070] 1207\n[BBOX-2071] 1208\n[BBOX-2072] 1209\n[BBOX-2073] 1210\n[BBOX-2074] 1211\n[BBOX-2075] 1212\n[BBOX-2076] 1213\n[BBOX-2077] 1214\n[BBOX-2078] 1215\n[BBOX-2079] 1216\n[BBOX-2080] 1217\n[BBOX-2081] 1218\n[BBOX-2082] 1219\n[BBOX-2083] 1220\n[BBOX-2084] 1221\n[BBOX-2085] 1222\n[BBOX-2086] 1223\n[BBOX-2087] 1224\n[BBOX-2088] 1225\n[BBOX-2089] 1226\n[BBOX-2090] 1227\n[BBOX-2091] 1228\n[BBOX-2092] 1229\n[BBOX-2093] 1230\n[BBOX-2094] 1231\n[BBOX-2095] 1232\n[BBOX-2096] 1233\n[BBOX-2097] 1234\n[BBOX-2098] 1235\n[BBOX-2099] 1236\n[BBOX-2100] 1237\n[BBOX-2101] 1238\n[BBOX-2102] 1239\n[BBOX-2103] 1240\n[BBOX-2104] 1241\n[BBOX-2105] 1242\n[BBOX-2106] 1243\n[BBOX-2107] 1244\n[BBOX-2108] 1245\n[BBOX-2109] 1246\n[BBOX-2110] 1247\n[BBOX-2111] 1248\n[BBOX-2112] 1249\n[BBOX-2113] 1250\n[BBOX-2114] 1251\n[BBOX-2115] 1252\n[BBOX-2116] 1253\n[BBOX-2117] 1254\n[BBOX-2118] 1255\n[BBOX-2119] 1256\n[BBOX-2120] 1257\n[BBOX-2121] 1258\n[BBOX-2122] 1259\n[BBOX-2123] 1260\n[BBOX-2124] 1261\n[BBOX-2125] 1262\n[BBOX-2126] 1263\n[BBOX-2127] 1264\n[BBOX-2128] 1265\n[BBOX-2129] 1266\n[BBOX-2130] 1267\n[BBOX-2131] 1268\n[BBOX-2132] 1269\n[BBOX-2133] 1270\n[BBOX-2134] 1271\n[BBOX-2135] 1272\n[BBOX-2136] 1273\n[BBOX-2137] 1274\n[BBOX-2138] 1275\n[BBOX-2139] 1276\n[BBOX-2140] 1277\n[BBOX-2141] 1278\n[BBOX-2142] 1279\n[BBOX-2143] 1280\n[BBOX-2144] 1281\n[BBOX-2145] 1282\n[BBOX-2146] 1283\n[BBOX-2147] 1284\n[BBOX-2148] 1285\n[BBOX-2149] 1286\n[BBOX-2150] 1287\n[BBOX-2151] 1288\n[BBOX-2152] 1289\n[BBOX-2153] 1290\n[BBOX-2154] 1291\n[BBOX-2155] 1292\n[BBOX-2156] 1293\n[BBOX-2157] 1294\n[BBOX-2158] 1295\n[BBOX-2159] 1296\n[BBOX-2160] 1297\n[BBOX-2161] 1298\n[BBOX-2162] 1299\n[BBOX-2163] 1300\n[BBOX-2164] 1301\n[BBOX-2165] 1302\n[BBOX-2166] 1303\n[BBOX-2167] 1304\n[BBOX-2168] 1305\n[BBOX-2169] 1306\n[BBOX-2170] 1307\n[BBOX-2171] 1308\n[BBOX-2172] 1309\n[BBOX-2173] 1310\n[BBOX-2174] 1311\n[BBOX-2175] 1312\n[BBOX-2176] 1313\n[BBOX-2177] 1314\n[BBOX-2178] 1315\n[BBOX-2179] 1316\n[BBOX-2180] 1317\n[BBOX-2181] 1318\n[BBOX-2182] 1319\n[BBOX-2183] 1320\n[BBOX-2184] 1321\n[BBOX-2185] 1322\n[BBOX-2186] 1323\n[BBOX-2187] 1324\n[BBOX-2188] 1325\n[BBOX-2189] 1326\n[BBOX-2190] 1327\n[BBOX-2191] 1328\n[BBOX-2192] 1329\n[BBOX-2193] 1330\n[BBOX-2194] 1331\n[BBOX-2195] 1332\n[BBOX-2196] 1333\n[BBOX-2197] 1334\n[BBOX-2198] 1335\n[BBOX-2199] 1336\n[BBOX-2200] 1337\n[BBOX-2201] 1338\n[BBOX-2202] 1339\n[BBOX-2203] 1340\n[BBOX-2204] 1341\n[BBOX-2205] 1342\n[BBOX-2206] 1343\n[BBOX-2207] 1344\n[BBOX-2208] 1345\n[BBOX-2209] 1346\n[BBOX-2210] 1347\n[BBOX-2211] 1348\n[BBOX-2212] 1349\n[BBOX-2213] 1350\n[BBOX-2214] 1351\n[BBOX-2215] 1352\n[BBOX-2216] 1353\n[BBOX-2217] 1354\n[BBOX-2218] 1355\n[BBOX-2219] 1356\n[BBOX-2220] 1357\n[BBOX-2221] 1358\n[BBOX-2222] 1359\n[BBOX-2223] 1360\n[BBOX-2224] 1361\n[BBOX-2225] 1362\n[BBOX-2226] 1363\n[BBOX-2227] 1364\n[BBOX-2228] 1365\n[BBOX-2229] 1366\n[BBOX-2230] 1367\n[BBOX-2231] 1368\n[BBOX-2232] 1369\n[BBOX-2233] 1370\n[BBOX-2234] 1371\n[BBOX-2235] 1372\n[BBOX-2236] 1373\n[BBOX-2237] 1374\n[BBOX-2238] 1375\n[BBOX-2239] 1376\n[BBOX-2240] 1377\n[BBOX-2241] 1378\n[BBOX-2242] 1379\n[BBOX-2243] 1380\n[BBOX-2244] 1381\n[BBOX-2245] 1382\n[BBOX-2246] 1383\n[BBOX-2247] 1384\n[BBOX-2248] 1385\n[BBOX-2249] 1386\n[BBOX-2250] 1387\n[BBOX-2251] 1388\n[BBOX-2252] 1389\n[BBOX-2253] 1390\n[BBOX-2254] 1391\n[BBOX-2255] 1392\n[BBOX-2256] 1393\n[BBOX-2257] 1394\n[BBOX-2258] 1395\n[BBOX-2259] 1396\n[BBOX-2260] 1397\n[BBOX-2261] 1398\n[BBOX-2262] 1399\n[BBOX-2263] 1400\n[BBOX-2264] 1401\n[BBOX-2265] 1402\n[BBOX-2266] 1403\n[BBOX-2267] 1404\n[BBOX-2268] 1405\n[BBOX-2269] 1406\n[BBOX-2270] 1407\n[BBOX-2271] 1408\n[BBOX-2272] 1409\n[BBOX-2273] 1410\n[BBOX-2274] 1411\n[BBOX-2275] 1412\n[BBOX-2276] 1413\n[BBOX-2277] 1414\n[BBOX-2278] 1415\n[BBOX-2279] 1416\n[BBOX-2280] 1417\n[BBOX-2281] 1418\n[BBOX-2282] 1419\n[BBOX-2283] 1420\n[BBOX-2284] 1421\n[BBOX-2285] 1422\n[BBOX-2286] 1423\n[BBOX-2287] 1424\n[BBOX-2288] 1425\n[BBOX-2289] 1426\n[BBOX-2290] 1427\n[BBOX-2291] 1428\n[BBOX-2292] 1429\n[BBOX-2293] 1430\n[BBOX-2294] 1431\n[BBOX-2295] 1432\n[BBOX-2296] 1433\n[BBOX-2297] 1434\n[BBOX-2298] 1435\n[BBOX-2299] 1436\n[BBOX-2300] 1437\n[BBOX-2301] 1438\n[BBOX-2302] 1439\n[BBOX-2303] 1440\n[BBOX-2304] 1441\n[BBOX-2305] 1442\n[BBOX-2306] 1443\n[BBOX-2307] 1444\n[BBOX-2308] 1445\n[BBOX-2309] 1446\n[BBOX-2310] 1447\n[BBOX-2311] 1448\n[BBOX-2312] 1449\n[BBOX-2313] 1450\n[BBOX-2314] 1451\n[BBOX-2315] 1452\n[BBOX-2316] 1453\n[BBOX-2317] 1454\n[BBOX-2318] 1455\n[BBOX-2319] 1456\n[BBOX-2320] 1457\n[BBOX-2321] 1458\n[BBOX-2322] 1459\n[BBOX-2323] 1460\n[BBOX-2324] 1461\n[BBOX-2325] 1462\n[BBOX-2326] 1463\n[BBOX-2327] 1464\n[BBOX-2328] 1465\n[BBOX-2329] 1466\n[BBOX-2330] 1467\n[BBOX-2331] 1468\n[BBOX-2332] 1469\n[BBOX-2333] 1470\n[BBOX-2334] 1471\n[BBOX-2335] 1472\n[BBOX-2336] 1473\n[BBOX-2337] 1474\n[BBOX-2338] 1475\n[BBOX-2339] 1476\n[BBOX-2340] 1477\n[BBOX-2341] 1478\n[BBOX-2342] 1479\n[BBOX-2343] 1480\n[BBOX-2344] 1481\n[BBOX-2345] 1482\n[BBOX-2346] 1483\n[BBOX-2347] 1484\n[BBOX-2348] 1485\n[BBOX-2349] 1486\n[BBOX-2350] 1487\n[BBOX-2351] 1488\n[BBOX-2352] 1489\n[BBOX-2353] 1490\n[BBOX-2354] 1491\n[BBOX-2355] 1492\n[BBOX-2356] 1493\n[BBOX-2357] 1494\n[BBOX-2358] 1495\n[BBOX-2359] 1496\n[BBOX-2360] 1497\n[BBOX-2361] 1498\n[BBOX-2362] 1499\n[BBOX-2363] 1500\n[BBOX-2364] 1501\n[BBOX-2365] 1502\n[BBOX-2366] 1503\n[BBOX-2367] 1504\n[BBOX-2368] 1505\n[BBOX-2369] 1506\n[BBOX-2370] 1507\n[BBOX-2371] 1508\n[BBOX-2372] 1509\n[BBOX-2373] 1510\n[BBOX-2374] 1511\n[BBOX-2375] 1512\n[BBOX-2376] 1513\n[BBOX-2377] 1514\n[BBOX-2378] 1515\n[BBOX-2379] 1516\n[BBOX-2380] 1517\n[BBOX-2381] 1518\n[BBOX-2382] 1519\n[BBOX-2383] 1520\n[BBOX-2384] 1521\n[BBOX-2385] 1522\n[BBOX-2386] 1523\n[BBOX-2387] 1524\n[BBOX-2388] 1525\n[BBOX-2389] 1526\n[BBOX-2390] 1527\n[BBOX-2391] 1528\n[BBOX-2392] 1529\n[BBOX-2393] 1530\n[BBOX-2394] 1531\n[BBOX-2395] 1532\n[BBOX-2396] 1533\n[BBOX-2397] 1534\n[BBOX-2398] 1535\n[BBOX-2399] 1536\n[BBOX-2400] 1537\n[BBOX-2401] 1538\n[BBOX-2402] 1539\n[BBOX-2403] 1540\n[BBOX-2404] 1541\n[BBOX-2405] 1542\n[BBOX-2406] 1543\n[BBOX-2407] 1544\n[BBOX-2408] 1545\n[BBOX-2409] 1546\n[BBOX-2410] 1547\n[BBOX-2411] 1548\n[BBOX-2412] 1549\n[BBOX-2413] 1550\n[BBOX-2414] 1551\n[BBOX-2415] 1552\n[BBOX-2416] 1553\n[BBOX-2417] 1554\n[BBOX-2418] 1555\n[BBOX-2419] 1556\n[BBOX-2420] 1557\n[BBOX-2421] 1558\n[BBOX-2422] 1559\n[BBOX-2423] 1560\n[BBOX-2424] 1561\n[BBOX-2425] 1562\n[BBOX-2426] 1563\n[BBOX-2427] 1564\n[BBOX-2428] 1565\n[BBOX-2429] 1566\n[BBOX-2430] 1567\n[BBOX-2431] 1568\n[BBOX-2432] 1569\n[BBOX-2433] 1570\n[BBOX-2434] 1571\n[BBOX-2435] 1572\n[BBOX-2436] 1573\n[BBOX-2437] 1574\n[BBOX-2438] 1575\n[BBOX-2439] 1576\n[BBOX-2440] 1577\n[BBOX-2441] 1578\n[BBOX-2442] 1579\n[BBOX-2443] 1580\n[BBOX-2444] 1581\n[BBOX-2445] 1582\n[BBOX-2446] 1583\n[BBOX-2447] 1584\n[BBOX-2448] 1585\n[BBOX-2449] 1586\n[BBOX-2450] 1587\n[BBOX-2451] 1588\n[BBOX-2452] 1589\n[BBOX-2453] 1590\n[BBOX-2454] 1591\n[BBOX-2455] 1592\n[BBOX-2456] 1593\n[BBOX-2457] 1594\n[BBOX-2458] 1595\n[BBOX-2459] 1596\n[BBOX-2460] 1597\n[BBOX-2461] 1598\n[BBOX-2462] 1599\n[BBOX-2463] 1600\n[BBOX-2464] 1601\n[BBOX-2465] 1602\n[BBOX-2466] 1603\n[BBOX-2467] 1604\n[BBOX-2468] 1605\n[BBOX-2469] 1606\n[BBOX-2470] 1607\n[BBOX-2471] 1608\n[BBOX-2472] 1609\n[BBOX-2473] 1610\n[BBOX-2474] 1611\n[BBOX-2475] 1612\n[BBOX-2476] 1613\n[BBOX-2477] 1614\n[BBOX-2478] 1615\n[BBOX-2479] 1616\n[BBOX-2480] 1617\n[BBOX-2481] 1618\n[BBOX-2482] 1619\n[BBOX-2483] 1620\n[BBOX-2484] 1621\n[BBOX-2485] 1622\n[BBOX-2486] 1623\n[BBOX-2487] 1624\n[BBOX-2488] 1625\n[BBOX-2489] 1626\n[BBOX-2490] 1627\n[BBOX-2491] 1628\n[BBOX-2492] 1629\n[BBOX-2493] 1630\n[BBOX-2494] 1631\n[BBOX-2495] 1632\n[BBOX-2496] 1633\n[BBOX-2497] 1634\n[BBOX-2498] 1635\n[BBOX-2499] 1636\n[BBOX-2500] 1637\n[BBOX-2501] 1638\n[BBOX-2502] 1639\n[BBOX-2503] 1640\n[BBOX-2504] 1641\n[BBOX-2505] 1642\n[BBOX-2506] 1643\n[BBOX-2507] 1644\n[BBOX-2508] 1645\n[BBOX-2509] 1646\n[BBOX-2510] 1647\n[BBOX-2511] 1648\n[BBOX-2512] 1649\n[BBOX-2513] 1650\n[BBOX-2514] 1651\n[BBOX-2515] 1652\n[BBOX-2516] 1653\n[BBOX-2517] 1654\n[BBOX-2518] 1655\n[BBOX-2519] 1656\n[BBOX-2520] 1657\n[BBOX-2521] 1658\n[BBOX-2522] 1659\n[BBOX-2523] 1660\n[BBOX-2524] 1661\n[BBOX-2525] 1662\n[BBOX-2526] 1663\n[BBOX-2527] 1664\n[BBOX-2528] 1665\n[BBOX-2529] 1666\n[BBOX-2530] 1667\n[BBOX-2531] 1668\n[BBOX-2532] 1669\n[BBOX-2533] 1670\n[BBOX-2534] 1671\n[BBOX-2535] 1672\n[BBOX-2536] 1673\n[BBOX-2537] 1674\n[BBOX-2538] 1675\n[BBOX-2539] 1676\n[BBOX-2540] 1677\n[BBOX-2541] 1678\n[BBOX-2542] 1679\n[BBOX-2543] 1680\n[BBOX-2544] 1681\n[BBOX-2545] 1682\n[BBOX-2546] 1683\n[BBOX-2547] 1684\n[BBOX-2548] 1685\n[BBOX-2549] 1686\n[BBOX-2550] 1687\n[BBOX-2551] 1688\n[BBOX-2552] 1689\n[BBOX-2553] 1690\n[BBOX-2554] 1691\n[BBOX-2555] 1692\n[BBOX-2556] 1693\n[BBOX-2557] 1694\n[BBOX-2558] 1695\n[BBOX-2559] 1696\n[BBOX-2560] 1697\n[BBOX-2561] 1698\n[BBOX-2562] 1699\n[BBOX-2563] 1700\n[BBOX-2564] 1701\n[BBOX-2565] 1702\n[BBOX-2566] 1703\n[BBOX-2567] 1704\n[BBOX-2568] 1705\n[BBOX-2569] 1706\n[BBOX-2570] 1707\n[BBOX-2571] 1708\n[BBOX-2572] 1709\n[BBOX-2573] 1710\n[BBOX-2574] 1711\n[BBOX-2575] 1712\n[BBOX-2576] 1713\n[BBOX-2577] 1714\n[BBOX-2578] 1715\n[BBOX-2579] 1716\n[BBOX-2580] 1717\n[BBOX-2581] 1718\n[BBOX-2582] 1719\n[BBOX-2583] 1720\n[BBOX-2584] 1721\n[BBOX-2585] 1722\n[BBOX-2586] 1723\n[BBOX-2587] 1724\n[BBOX-2588] 1725\n[BBOX-2589] 1726\n[BBOX-2590] 1727\n[BBOX-2591] 1728\n[BBOX-2592] 1729\n[BBOX-2593] 1730\n[BBOX-2594] 1731\n[BBOX-2595] 1732\n[BBOX-2596] 1733\n[BBOX-2597] 1734\n[BBOX-2598] 1735\n[BBOX-2599] 1736\n[BBOX-2600] 1737\n[BBOX-2601] 1738\n[BBOX-2602] 1739\n[BBOX-2603] 1740\n[BBOX-2604] 1741\n[BBOX-2605] 1742\n[BBOX-2606] 1743\n[BBOX-2607] 1744\n[BBOX-2608] 1745\n[BBOX-2609] 1746\n[BBOX-2610] 1747\n[BBOX-2611] 1748\n[BBOX-2612] 1749\n[BBOX-2613] 1750\n[BBOX-2614] 1751\n[BBOX-2615] 1752\n[BBOX-2616] 1753\n[BBOX-2617] 1754\n[BBOX-2618] 1755\n[BBOX-2619] 1756\n[BBOX-2620] 1757\n[BBOX-2621] 1758\n[BBOX-2622] 1759\n[BBOX-2623] 1760\n[BBOX-2624] 1761\n[BBOX-2625] 1762\n[BBOX-2626] 1763\n[BBOX-2627] 1764\n[BBOX-2628] 1765\n[BBOX-2629] 1766\n[BBOX-2630] 1767\n[BBOX-2631] 1768\n[BBOX-2632] 1769\n[BBOX-2633] 1770\n[BBOX-2634] 1771\n[BBOX-2635] 1772\n[BBOX-2636] 1773\n[BBOX-2637] 1774\n[BBOX-2638] 1775\n[BBOX-2639] 1776\n[BBOX-2640] 1777\n[BBOX-2641] 1778\n[BBOX-2642] 1779\n[BBOX-2643] 1780\n[BBOX-2644] 1781\n[BBOX-2645] 1782\n[BBOX-2646] 1783\n[BBOX-2647] 1784\n[BBOX-2648] 1785\n[BBOX-2649] 1786\n[BBOX-2650] 1787\n[BBOX-2651] 1788\n[BBOX-2652] 1789\n[BBOX-2653] 1790\n[BBOX-2654] 1791\n[BBOX-2655] 1792\n[BBOX-2656] 1793\n[BBOX-2657] 1794\n[BBOX-2658] 1795\n[BBOX-2659] 1796\n[BBOX-2660] 1797\n[BBOX-2661] 1798\n[BBOX-2662] 1799\n[BBOX-2663] 1800\n[BBOX-2664] 1801\n[BBOX-2665] 1802\n[BBOX-2666] 1803\n[BBOX-2667] 1804\n[BBOX-2668] 1805\n[BBOX-2669] 1806\n[BBOX-2670] 1807\n[BBOX-2671] 1808\n[BBOX-2672] 1809\n[BBOX-2673] 1810\n[BBOX-2674] 1811\n[BBOX-2675] 1812\n[BBOX-2676] 1813\n[BBOX-2677] 1814\n[BBOX-2678] 1815\n[BBOX-2679] 1816\n[BBOX-2680] 1817\n[BBOX-2681] 1818\n[BBOX-2682] 1819\n[BBOX-2683] 1820\n[BBOX-2684] 1821\n[BBOX-2685] 1822\n[BBOX-2686] 1823\n[BBOX-2687] 1824\n[BBOX-2688] 1825\n[BBOX-2689] 1826\n[BBOX-2690] 1827\n[BBOX-2691] 1828\n[BBOX-2692] 1829\n[BBOX-2693] 1830\n[BBOX-2694] 1831\n[BBOX-2695] 1832\n[BBOX-2696] 1833\n[BBOX-2697] 1834\n[BBOX-2698] 1835\n[BBOX-2699] 1836\n[BBOX-2700] 1837\n[BBOX-2701] 1838\n[BBOX-2702] 1839\n[BBOX-2703] 1840\n[BBOX-2704] 1841\n[BBOX-2705] 1842\n[BBOX-2706] 1843\n[BBOX-2707] 1844\n[BBOX-2708] 1845\n[BBOX-2709] 1846\n[BBOX-2710] 1847\n[BBOX-2711] 1848\n[BBOX-2712] 1849\n[BBOX-2713] 1850\n[BBOX-2714] 1851\n[BBOX-2715] 1852\n[BBOX-2716] 1853\n[BBOX-2717] 1854\n[BBOX-2718] 1855\n[BBOX-2719] 1856\n[BBOX-2720] 1857\n[BBOX-2721] 1858\n[BBOX-2722] 1859\n[BBOX-2723] 1860\n[BBOX-2724] 1861\n[BBOX-2725] 1862\n[BBOX-2726] 1863\n[BBOX-2727] 1864\n[BBOX-2728] 1865\n[BBOX-2729] 1866\n[BBOX-2730] 1867\n[BBOX-2731] 1868\n[BBOX-2732] 1869\n[BBOX-2733] 1870\n[BBOX-2734] 1871\n[BBOX-2735] 1872\n[BBOX-2736] 1873\n[BBOX-2737] 1874\n[BBOX-2738] 1875\n[BBOX-2739] 1876\n[BBOX-2740] 1877\n[BBOX-2741] 1878\n[BBOX-2742] 1879\n[BBOX-2743] 1880\n[BBOX-2744] 1881\n[BBOX-2745] 1882\n[BBOX-2746] 1883\n[BBOX-2747] 1884\n[BBOX-2748] 1885\n[BBOX-2749] 1886\n[BBOX-2750] 1887\n[BBOX-2751] 1888\n[BBOX-2752] 1889\n[BBOX-2753] 1890\n[BBOX-2754] 1891\n[BBOX-2755] 1892\n[BBOX-2756] 1893\n[BBOX-2757] 1894\n[BBOX-2758] 1895\n[BBOX-2759] 1896\n[BBOX-2760] 1897\n[BBOX-2761] 1898\n[BBOX-2762] 1899\n[BBOX-2763] 1900\n[BBOX-2764] 1901\n[BBOX-2765] 1902\n[BBOX-2766] 1903\n[BBOX-2767] 1904\n[BBOX-2768] 1905\n[BBOX-2769] 1906\n[BBOX-2770] 1907\n[BBOX-2771] 1908\n[BBOX-2772] 1909\n[BBOX-2773] 1910\n[BBOX-2774] 1911\n[BBOX-2775] 1912\n[BBOX-2776] 1913\n[BBOX-2777] 1914\n[BBOX-2778] 1915\n[BBOX-2779] 1916\n[BBOX-2780] 1917\n[BBOX-2781] 1918\n[BBOX-2782] 1919\n[BBOX-2783] 1920\n[BBOX-2784] 1921\n[BBOX-2785] 1922\n[BBOX-2786] 1923\n[BBOX-2787] 1924\n[BBOX-2788] 1925\n[BBOX-2789] 1926\n[BBOX-2790] 1927\n[BBOX-2791] 1928\n[BBOX-2792] 1929\n[BBOX-2793] 1930\n[BBOX-2794] 1931\n[BBOX-2795] 1932\n[BBOX-2796] 1933\n[BBOX-2797] 1934\n[BBOX-2798] 1935\n[BBOX-2799] 1936\n[BBOX-2800] 1937\n[BBOX-2801] 1938\n[BBOX-2802] 1939\n[BBOX-2803] 1940\n[BBOX-2804] 1941\n[BBOX-2805] 1942\n[BBOX-2806] 1943\n[BBOX-2807] 1944\n[BBOX-2808] 1945\n[BBOX-2809] 1946\n[BBOX-2810] 1947\n[BBOX-2811] 1948\n[BBOX-2812] 1949\n[BBOX-2813] 1950\n[BBOX-2814] 1951\n[BBOX-2815] 1952\n[BBOX-2816] 1953\n[BBOX-2817] 1954\n[BBOX-2818] 1955\n[BBOX-2819] 1956\n[BBOX-2820] 1957\n[BBOX-2821] 1958\n[BBOX-2822] 1959\n[BBOX-2823] 1960\n[BBOX-2824] 1961\n[BBOX-2825] 1962\n[BBOX-2826] 1963\n[BBOX-2827] 1964\n[BBOX-2828] 1965\n[BBOX-2829] 1966\n[BBOX-2830] 1967\n[BBOX-2831] 1968\n[BBOX-2832] 1969\n[BBOX-2833] 1970\n[BBOX-2834] 1971\n[BBOX-2835] 1972\n[BBOX-2836] 1973\n[BBOX-2837] 1974\n[BBOX-2838] 1975\n[BBOX-2839] 1976\n[BBOX-2840] 1977\n[BBOX-2841] 1978\n[BBOX-2842] 1979\n[BBOX-2843] 1980\n[BBOX-2844] 1981\n[BBOX-2845] 1982\n[BBOX-2846] 1983\n[BBOX-2847] 1984\n[BBOX-2848] 1985\n[BBOX-2849] 1986\n[BBOX-2850] 1987\n[BBOX-2851] 1988\n[BBOX-2852] 1989\n[BBOX-2853] 1990\n[BBOX-2854] 1991\n[BBOX-2855] 1992\n[BBOX-2856] 1993\n[BBOX-2857] 1994\n[BBOX-2858] 1995\n[BBOX-2859] 1996\n[BBOX-2860] 1997\n[BBOX-2861] 1998\n[BBOX-2862] 1999\n[BBOX-2863] 2000\n[BBOX-2864] 2001\n[BBOX-2865] 2002\n[BBOX-2866] 2003\n[BBOX-2867] 2004\n[BBOX-2868] 2005\n[BBOX-2869] 2006\n[BBOX-2870] 2007\n[BBOX-2871] 2008\n[BBOX-2872] 2009\n[BBOX-2873] 2010\n[BBOX-2874] 2011\n[BBOX-2875] 2012\n[BBOX-2876] 2013\n[BBOX-2877] 2014\n[BBOX-2878] 2015\n[BBOX-2879] 2016\n[BBOX-2880] 2017\n[BBOX-2881] 2018\n[BBOX-2882] 2019\n[BBOX-2883] 2020\n[BBOX-2884] 2021\n[BBOX-2885] 2022\n[BBOX-2886] 2023\n[BBOX-2887] 2024\n[BBOX-2888] 2025\n[BBOX-2889] 2026\n[BBOX-2890] 2027\n[BBOX-2891] 2028\n[BBOX-2892] 2029\n[BBOX-2893] 2030\n[BBOX-2894] 2031\n[BBOX-2895] 2032\n[BBOX-2896] 2033\n[BBOX-2897] 2034\n[BBOX-2898] 2035\n[BBOX-2899] 2036\n[BBOX-2900] 2037\n[BBOX-2901] 2038\n[BBOX-2902] 2039\n[BBOX-2903] 2040\n[BBOX-2904] 2041\n[BBOX-2905] 2042\n[BBOX-2906] 2043\n[BBOX-2907] 2044\n[BBOX-2908] 2045\n[BBOX-2909] 2046\n[BBOX-2910] 2047\n[BBOX-2911] 2048\n[BBOX-2912] 2049\n[BBOX-2913] 2050\n[BBOX-2914] 2051\n[BBOX-2915] 2052\n[BBOX-2916] 2053\n[BBOX-2917] 2054\n[BBOX-2918] 2055\n[BBOX-2919] 2056\n[BBOX-2920] 2057\n[BBOX-2921] 2058\n[BBOX-2922] 2059\n[BBOX-2923] 2060\n[BBOX-2924] 2061\n[BBOX-2925] 2062\n[BBOX-2926] 2063\n[BBOX-2927] 2064\n[BBOX-2928] 2065\n[BBOX-2929] 2066\n[BBOX-2930] 2067\n[BBOX-2931] 2068\n[BBOX-2932] 2069\n[BBOX-2933] 2070\n[BBOX-2934] 2071\n[BBOX-2935] 2072\n[BBOX-2936] 2073\n[BBOX-2937] 2074\n[BBOX-2938] 2075\n[BBOX-2939] 2076\n[BBOX-2940] 2077\n[BBOX-2941] 2078\n[BBOX-2942] 2079\n[BBOX-2943] 2080\n[BBOX-2944] 2081\n[BBOX-2945] 2082\n[BBOX-2946] 2083\n[BBOX-2947] 2084\n[BBOX-2948] 2085\n[BBOX-2949] 2086\n[BBOX-2950] 2087\n[BBOX-2951] 2088\n[BBOX-2952] 2089\n[BBOX-2953] 2090\n[BBOX-2954] 2091\n[BBOX-2955] 2092\n[BBOX-2956] 2093\n[BBOX-2957] 2094\n[BBOX-2958] 2095\n[BBOX-2959] 2096\n[BBOX-2960] 2097\n[BBOX-2961] 2098\n[BBOX-2962] 2099\n[BBOX-2963] 2100\n[BBOX-2964] 2101\n[BBOX-2965] 2102\n[BBOX-2966] 2103\n[BBOX-2967] 2104\n[BBOX-2968] 2105\n[BBOX-2969] 2106\n[BBOX-2970] 2107\n[BBOX-2971] 2108\n[BBOX-2972] 2109\n[BBOX-2973] 2110\n[BBOX-2974] 2111\n[BBOX-2975] 2112\n[BBOX-2976] 2113\n[BBOX-2977] 2114\n[BBOX-2978] 2115\n[BBOX-2979] 2116\n[BBOX-2980] 2117\n[BBOX-2981] 2118\n[BBOX-2982] 2119\n[BBOX-2983] 2120\n[BBOX-2984] 2121\n[BBOX-2985] 2122\n[BBOX-2986] 2123\n[BBOX-2987] 2124\n[BBOX-2988] 2125\n[BBOX-2989] 2126\n[BBOX-2990] 2127\n[BBOX-2991] 2128\n[BBOX-2992] 2129\n[BBOX-2993] 2130\n[BBOX-2994] 2131\n[BBOX-2995] 2132\n[BBOX-2996] 2133\n[BBOX-2997] 2134\n[BBOX-2998] 2135\n[BBOX-2999] 2136\n[BBOX-3000] 2137\n[BBOX-3001] 2138\n[BBOX-3002] 2139\n[BBOX-3003] 2140\n[BBOX-3004] 2141\n[BBOX-3005] 2142\n[BBOX-3006] 2143\n[BBOX-3007] 2144\n[BBOX-3008] 2145\n[BBOX-3009] 2146\n[BBOX-3010] 2147\n[BBOX-3011] 2148\n[BBOX-3012] 2149\n[BBOX-3013] 2150\n[BBOX-3014] 2151\n[BBOX-3015] 2152\n[BBOX-3016] 2153\n[BBOX-3017] 2154\n[BBOX-3018] 2155\n[BBOX-3019] 2156\n[BBOX-3020] 2157\n[BBOX-3021] 2158\n[BBOX-3022] 2159\n[BBOX-3023] 2160\n[BBOX-3024] 2161\n[BBOX-3025] 2162\n[BBOX-3026] 2163\n[BBOX-3027] 2164\n[BBOX-3028] 2165\n[BBOX-3029] 2166\n[BBOX-3030] 2167\n[BBOX-3031] 2168\n[BBOX-3032] 2169\n[BBOX-3033] 2170\n[BBOX-3034] 2171\n[BBOX-3035] 2172\n[BBOX-3036] 2173\n[BBOX-3037] 2174\n[BBOX-3038] 2175\n[BBOX-3039] 2176\n[BBOX-3040] 2177\n[BBOX-3041] 2178\n[BBOX-3042] 2179\n[BBOX-3043] 2180\n[BBOX-3044] 2181\n[BBOX-3045] 2182\n[BBOX-3046] 2183\n[BBOX-3047] 2184\n[BBOX-3048] 2185\n[BBOX-3049] 2186\n[BBOX-3050] 2187\n[BBOX-3051] 2188\n[BBOX-3052] 2189\n[BBOX-3053] 2190\n[BBOX-3054] 2191\n[BBOX-3055] 2192\n[BBOX-3056] 2193\n[BBOX-3057] 2194\n[BBOX-3058] 2195\n[BBOX-3059] 2196\n[BBOX-3060] 2197\n[BBOX-3061] 2198\n[BBOX-3062] 2199\n[BBOX-3063] 2200\n[BBOX-3064] 2201\n[BBOX-3065] 2202\n[BBOX-3066] 2203\n[BBOX-3067] 2204\n[BBOX-3068] 2205\n[BBOX-3069] 2206\n[BBOX-3070] 2207\n[BBOX-3071] 2208\n[BBOX-3072] 2209\n[BBOX-3073] 2210\n[BBOX-3074] 2211\n[BBOX-3075] 2212\n[BBOX-3076] 2213\n[BBOX-3077] 2214\n[BBOX-3078] 2215\n[BBOX-3079] 2216\n[BBOX-3080] 2217\n[BBOX-3081] 2218\n[BBOX-3082] 2219\n[BBOX-3083] 2220\n[BBOX-3084] 2221\n[BBOX-3085] 2222\n[BBOX-3086] 2223\n[BBOX-3087] 2224\n[BBOX-3088] 2225\n[BBOX-3089] 2226\n[BBOX-3090] 2227\n[BBOX-3091] 2228\n[BBOX-3092] 2229\n[BBOX-3093] 2230\n[BBOX-3094] 2231\n[BBOX-3095] 2232\n[BBOX-3096] 2233\n[BBOX-3097] 2234\n[BBOX-3098] 2235\n[BBOX-3099] 2236\n[BBOX-3100] 2237\n[BBOX-3101] 2238\n[BBOX-3102] 2239\n[BBOX-3103] 2240\n[BBOX-3104] 2241\n[BBOX-3105] 2242\n[BBOX-3106] 2243\n[BBOX-3107] 2244\n[BBOX-3108] 2245\n[BBOX-3109] 2246\n[BBOX-3110] 2247\n[BBOX-3111] 2248\n[BBOX-3112] 2249\n[BBOX-3113] 2250\n[BBOX-3114] 2251\n[BBOX-3115] 2252\n[BBOX-3116] 2253\n[BBOX-3117] 2254\n[BBOX-3118] 2255\n[BBOX-3119] 2256\n[BBOX-3120] 2257\n[BBOX-3121] 2258\n[BBOX-3122] 2259\n[BBOX-3123] 2260\n[BBOX-3124] 2261\n[BBOX-3125] 2262\n[BBOX-3126] 2263\n[BBOX-3127] 2264\n[BBOX-3128] 2265\n[BBOX-3129] 2266\n[BBOX-3130] 2267\n[BBOX-3131] 2268\n[BBOX-3132] 2269\n[BBOX-3133] 2270\n[BBOX-3134] 2271\n[BBOX-3135] 2272\n[BBOX-3136] 2273\n[BBOX-3137] 2274\n[BBOX-3138] 2275\n[BBOX-3139] 2276\n[BBOX-3140] 2277\n[BBOX-3141] 2278\n[BBOX-3142] 2279\n[BBOX-3143] 2280\n[BBOX-3144] 2281\n[BBOX-3145] 2282\n[BBOX-3146] 2283\n[BBOX-3147] 2284\n[BBOX-3148] 2285\n[BBOX-3149] 2286\n[BBOX-3150] 2287\n[BBOX-3151] 2288\n[BBOX-3152] 2289\n[BBOX-3153] 2290\n[BBOX-3154] 2291\n[BBOX-3155] 2292\n[BBOX-3156] 2293\n[BBOX-3157] 2294\n[BBOX-3158] 2295\n[BBOX-3159] 2296\n[BBOX-3160] 2297\n[BBOX-3161] 2298\n[BBOX-3162] 2299\n[BBOX-3163] 2300\n[BBOX-3164] 2301\n[BBOX-3165] 2302\n[BBOX-3166] 2303\n[BBOX-3167] 2304\n[BBOX-3168] 2305\n[BBOX-3169] 2306\n[BBOX-3170] 2307\n[BBOX-3171] 2308\n[BBOX-3172] 2309\n[BBOX-3173] 2310\n[BBOX-3174] 2311\n[BBOX-3175] 2312\n[BBOX-3176] 2313\n[BBOX-3177] 2314\n[BBOX-3178] 2315\n[BBOX-3179] 2316\n[BBOX-3180] 2317\n[BBOX-3181] 2318\n[BBOX-3182] 2319\n[BBOX-3183] 2320\n[BBOX-3184] 2321\n[BBOX-3185] 2322\n[BBOX-3186] 2323\n[BBOX-3187] 2324\n[BBOX-3188] 2325\n[BBOX-3189] 2326\n[BBOX-3190] 2327\n[BBOX-3191] 2328\n[BBOX-3192] 2329\n[BBOX-3193] 2330\n[BBOX-3194] 2331\n[BBOX-3195] 2332\n[BBOX-3196] 2333\n[BBOX-3197] 2334\n[BBOX-3198] 2335\n[BBOX-3199] 2336\n[BBOX-3200] 2337\n[BBOX-3201] 2338\n[BBOX-3202] 2339\n[BBOX-3203] 2340\n[BBOX-3204] 2341\n[BBOX-3205] 2342\n[BBOX-3206] 2343\n[BBOX-3207] 2344\n[BBOX-3208] 2345\n[BBOX-3209] 2346\n[BBOX-3210] 2347\n[BBOX-3211] 2348\n[BBOX-3212] 2349\n[BBOX-3213] 2350\n[BBOX-3214] 2351\n[BBOX-3215] 2352\n[BBOX-3216] 2353\n[BBOX-3217] 2354\n[BBOX-3218] 2355\n[BBOX-3219] 2356\n[BBOX-3220] 2357\n[BBOX-3221] 2358\n[BBOX-3222] 2359\n[BBOX-3223] 2360\n[BBOX-3224] 2361\n[BBOX-3225] 2362\n[BBOX-3226] 2363\n[BBOX-3227] 2364\n[BBOX-3228] 2365\n[BBOX-3229] 2366\n[BBOX-3230] 2367\n[BBOX-3231] 2368\n[BBOX-3232] 2369\n[BBOX-3233] 2370\n[BBOX-3234] 2371\n[BBOX-3235] 2372\n[BBOX-3236] 2373\n[BBOX-3237] 2374\n[BBOX-3238] 2375\n[BBOX-3239] 2376\n[BBOX-3240] 2377\n[BBOX-3241] 2378\n[BBOX-3242] 2379\n[BBOX-3243] 2380\n[BBOX-3244] 2381\n[BBOX-3245] 2382\n[BBOX-3246] 2383\n[BBOX-3247] 2384\n[BBOX-3248] 2385\n[BBOX-3249] 2386\n[BBOX-3250] 2387\n[BBOX-3251] 2388\n[BBOX-3252] 2389\n[BBOX-3253] 2390\n[BBOX-3254] 2391\n[BBOX-3255] 2392\n[BBOX-3256] 2393\n[BBOX-3257] 2394\n[BBOX-3258] 2395\n[BBOX-3259] 2396\n[BBOX-3260] 2397\n[BBOX-3261] 2398\n[BBOX-3262] 2399\n[BBOX-3263] 2400\n[BBOX-3264] 2401\n[BBOX-3265] 2402\n[BBOX-3266] 2403\n[BBOX-3267] 2404\n[BBOX-3268] 2405\n[BBOX-3269] 2406\n[BBOX-3270] 2407\n[BBOX-3271] 2408\n[BBOX-3272] 2409\n[BBOX-3273] 2410\n[BBOX-3274] 2411\n[BBOX-3275] 2412\n[BBOX-3276] 2413\n[BBOX-3277] 2414\n[BBOX-3278] 2415\n[BBOX-3279] 2416\n[BBOX-3280] 2417\n[BBOX-3281] 2418\n[BBOX-3282] 2419\n[BBOX-3283] 2420\n[BBOX-3284] 2421\n[BBOX-3285] 2422\n[BBOX-3286] 2423\n[BBOX-3287] 2424\n[BBOX-3288] 2425\n[BBOX-3289] 2426\n[BBOX-3290] 2427\n[BBOX-3291] 2428\n[BBOX-3292] 2429\n[BBOX-3293] 2430\n[BBOX-3294] 2431\n[BBOX-3295] 2432\n[BBOX-3296] 2433\n[BBOX-3297] 2434\n[BBOX-3298] 2435\n[BBOX-3299] 2436\n[BBOX-3300] 2437\n[BBOX-3301] 2438\n[BBOX-3302] 2439\n[BBOX-3303] 2440\n[BBOX-3304] 2441\n[BBOX-3305] 2442\n[BBOX-3306] 2443\n[BBOX-3307] 2444\n[BBOX-3308] 2445\n[BBOX-3309] 2446\n[BBOX-3310] 2447\n[BBOX-3311] 2448\n[BBOX-3312] 2449\n[BBOX-3313] 2450\n[BBOX-3314] 2451\n[BBOX-3315] 2452\n[BBOX-3316] 2453\n[BBOX-3317] 2454\n[BBOX-3318] 2455\n[BBOX-3319] 2456\n[BBOX-3320] 2457\n[BBOX-3321] 2458\n[BBOX-3322] 2459\n[BBOX-3323] 2460\n[BBOX-3324] 2461\n[BBOX-3325] 2462\n[BBOX-3326] 2463\n[BBOX-3327] 2464\n[BBOX-3328] 2465\n[BBOX-3329] 2466\n[BBOX-3330] 2467\n[BBOX-3331] 2468\n[BBOX-3332] 2469\n[BBOX-3333] 2470\n[BBOX-3334] 2471\n[BBOX-3335] 2472\n[BBOX-3336] 2473\n[BBOX-3337] 2474\n[BBOX-3338] 2475\n[BBOX-3339] 2476\n[BBOX-3340] 2477\n[BBOX-3341] 2478\n[BBOX-3342] 2479\n[BBOX-3343] 2480\n[BBOX-3344] 2481\n[BBOX-3345] 2482\n[BBOX-3346] 2483\n[BBOX-3347] 2484\n[BBOX-3348] 2485\n[BBOX-3349] 2486\n[BBOX-3350] 2487\n[BBOX-3351] 2488\n[BBOX-3352] 2489\n[BBOX-3353] 2490\n[BBOX-3354] 2491\n[BBOX-3355] 2492\n[BBOX-3356] 2493\n[BBOX-3357] 2494\n[BBOX-3358] 2495\n[BBOX-3359] 2496\n[BBOX-3360] 2497\n[BBOX-3361] 2498\n[BBOX-3362] 2499\n[BBOX-3363] 2500\n[BBOX-3364] 2501\n[BBOX-3365] 2502\n[BBOX-3366] 2503\n[BBOX-3367] 2504\n[BBOX-3368] 2505\n[BBOX-3369] 2506\n[BBOX-3370] 2507\n[BBOX-3371] 2508\n[BBOX-3372] 2509\n[BBOX-3373] 2510\n[BBOX-3374] 2511\n[BBOX-3375] 2512\n[BBOX-3376] 2513\n[BBOX-3377] 2514\n[BBOX-3378] 2515\n[BBOX-3379] 2516\n[BBOX-3380] 2517\n[BBOX-3381] 2518\n[BBOX-3382] 2519\n[BBOX-3383] 2520\n[BBOX-3384] 2521\n[BBOX-3385] 2522\n[BBOX-3386] 2523\n[BBOX-3387] 2524\n[BBOX-3388] 2525\n[BBOX-3389] 2526\n[BBOX-3390] 2527\n[BBOX-3391] 2528\n[BBOX-3392] 2529\n[BBOX-3393] 2530\n[BBOX-3394] 2531\n[BBOX-3395] 2532\n[BBOX-3396] 2533\n[BBOX-3397] 2534\n[BBOX-3398] 2535\n[BBOX-3399] 2536\n[BBOX-3400] 2537\n[BBOX-3401] 2538\n[BBOX-3402] 2539\n[BBOX-3403] 2540\n[BBOX-3404] 2541\n[BBOX-3405] 2542\n[BBOX-3406] 2543\n[BBOX-3407] 2544\n[BBOX-3408] 2545\n[BBOX-3409] 2546\n[BBOX-3410] 2547\n[BBOX-3411] 2548\n[BBOX-3412] 2549\n[BBOX-3413] 2550\n[BBOX-3414] 2551\n[BBOX-3415] 2552\n[BBOX-3416] 2553\n[BBOX-3417] 2554\n[BBOX-3418] 2555\n[BBOX-3419] 2556\n[BBOX-3420] 2557\n[BBOX-3421] 2558\n[BBOX-3422] 2559\n[BBOX-3423] 2560\n[BBOX-3424] 2561\n[BBOX-3425] 2562\n[BBOX-3426] 2563\n[BBOX-3427] 2564\n[BBOX-3428] 2565\n[BBOX-3429] 2566\n[BBOX-3430] 2567\n[BBOX-3431] 2568\n[BBOX-3432] 2569\n[BBOX-3433] 2570\n[BBOX-3434] 2571\n[BBOX-3435] 2572\n[BBOX-3436] 2573\n[BBOX-3437] 2574\n[BBOX-3438] 2575\n[BBOX-3439] 2576\n[BBOX-3440] 2577\n[BBOX-3441] 2578\n[BBOX-3442] 2579\n[BBOX-3443] 2580\n[BBOX-3444] 2581\n[BBOX-3445] 2582\n[BBOX-3446] 2583\n[BBOX-3447] 2584\n[BBOX-3448] 2585\n[BBOX-3449] 2586\n[BBOX-3450] 2587\n[BBOX-3451] 2588\n[BBOX-3452] 2589\n[BBOX-3453] 2590\n[BBOX-3454] 2591\n[BBOX-3455] 2592\n[BBOX-3456] 2593\n[BBOX-3457] 2594\n[BBOX-3458] 2595\n[BBOX-3459] 2596\n[BBOX-3460] 2597\n[BBOX-3461] 2598\n[BBOX-3462] 2599\n[BBOX-3463] 2600\n[BBOX-3464] 2601\n[BBOX-3465] 2602\n[BBOX-3466] 2603\n[BBOX-3467] 2604\n[BBOX-3468] 2605\n[BBOX-3469] 2606\n[BBOX-3470] 2607\n[BBOX-3471] 2608\n[BBOX-3472] 2609\n[BBOX-3473] 2610\n[BBOX-3474] 2611\n[BBOX-3475] 2612\n[BBOX-3476] 2613\n[BBOX-3477] 2614\n[BBOX-3478] 2615\n[BBOX-3479] 2616\n[BBOX-3480] 2617\n[BBOX-3481] 2618\n[BBOX-3482] 2619\n[BBOX-3483] 2620\n[BBOX-3484] 2621\n[BBOX-3485] 2622\n[BBOX-3486] 2623\n[BBOX-3487] 2624\n[BBOX-3488] 2625\n[BBOX-3489] 2626\n[BBOX-3490] 2627\n[BBOX-3491] 2628\n[BBOX-3492] 2629\n[BBOX-3493] 2630\n[BBOX-3494] 2631\n[BBOX-3495] 2632\n[BBOX-3496] 2633\n[BBOX-3497] 2634\n[BBOX-3498] 2635\n[BBOX-3499] 2636\n[BBOX-3500] 2637\n[BBOX-3501] 2638\n[BBOX-3502] 2639\n[BBOX-3503] 2640\n[BBOX-3504] 2641\n[BBOX-3505] 2642\n[BBOX-3506] 2643\n[BBOX-3507] 2644\n[BBOX-3508] 2645\n[BBOX-3509] 2646\n[BBOX-3510] 2647\n[BBOX-3511] 2648\n[BBOX-3512] 2649\n[BBOX-3513] 2650\n[BBOX-3514] 2651\n[BBOX-3515] 2652\n[BBOX-3516] 2653\n[BBOX-3517] 2654\n[BBOX-3518] 2655\n[BBOX-3519] 2656\n[BBOX-3520] 2657\n[BBOX-3521] 2658\n[BBOX-3522] 2659\n[BBOX-3523] 2660\n[BBOX-3524] 2661\n[BBOX-3525] 2662\n[BBOX-3526] 2663\n[BBOX-3527] 2664\n[BBOX-3528] 2665\n[BBOX-3529] 2666\n[BBOX-3530] 2667\n[BBOX-3531] 2668\n[BBOX-3532] 2669\n[BBOX-3533] 2670\n[BBOX-3534] 2671\n[BBOX-3535] 2672\n[BBOX-3536] 2673\n[BBOX-3537] 2674\n[BBOX-3538] 2675\n[BBOX-3539] 2676\n[BBOX-3540] 2677\n[BBOX-3541] 2678\n[BBOX-3542] 2679\n[BBOX-3543] 2680\n[BBOX-3544] 2681\n[BBOX-3545] 2682\n[BBOX-3546] 2683\n[BBOX-3547] 2684\n[BBOX-3548] 2685\n[BBOX-3549] 2686\n[BBOX-3550] 2687\n[BBOX-3551] 2688\n[BBOX-3552] 2689\n[BBOX-3553] 2690\n[BBOX-3554] 2691\n[BBOX-3555] 2692\n[BBOX-3556] 2693\n[BBOX-3557] 2694\n[BBOX-3558] 2695\n[BBOX-3559] 2696\n[BBOX-3560] 2697\n[BBOX-3561] 2698\n[BBOX-3562] 2699\n[BBOX-3563] 2700\n[BBOX-3564] 2701\n[BBOX-3565] 2702\n[BBOX-3566] 2703\n[BBOX-3567] 2704\n[BBOX-3568] 2705\n[BBOX-3569] 2706\n[BBOX-3570] 2707\n[BBOX-3571] 2708\n[BBOX-3572] 2709\n[BBOX-3573] 2710\n[BBOX-3574] 2711\n[BBOX-3575] 2712\n[BBOX-3576] 2713\n[BBOX-3577] 2714\n[BBOX-3578] 2715\n[BBOX-3579] 2716\n[BBOX-3580] 2717\n[BBOX-3581] 2718\n[BBOX-3582] 2719\n[BBOX-3583] 2720\n[BBOX-3584] 2721\n[BBOX-3585] 2722\n[BBOX-3586] 2723\n[BBOX-3587] 2724\n[BBOX-3588] 2725\n[BBOX-3589] 2726\n[BBOX-3590] 2727\n[BBOX-3591] 2728\n[BBOX-3592] 2729\n[BBOX-3593] 2730\n[BBOX-3594] 2731\n[BBOX-3595] 2732\n[BBOX-3596] 2733\n[BBOX-3597] 2734\n[BBOX-3598] 2735\n[BBOX-3599] 2736\n[BBOX-3600] 2737\n[BBOX-3601] 2738\n[BBOX-3602] 2739\n[BBOX-3603] 2740\n[BBOX-3604] 2741\n[BBOX-3605] 2742\n[BBOX-3606] 2743\n[BBOX-3607] 2744\n[BBOX-3608] 2745\n[BBOX-3609] 2746\n[BBOX-3610] 2747\n[BBOX-3611] 2748\n[BBOX-3612] 2749\n[BBOX-3613] 2750\n[BBOX-3614] 2751\n[BBOX-3615] 2752\n[BBOX-3616] 2753\n[BBOX-3617] 2754\n[BBOX-3618] 2755\n[BBOX-3619] 2756\n[BBOX-3620] 2757\n[BBOX-3621] 2758\n[BBOX-3622] 2759\n[BBOX-3623] 2760\n[BBOX-3624] 2761\n[BBOX-3625] 2762\n[BBOX-3626] 2763\n[BBOX-3627] 2764\n[BBOX-3628] 2765\n[BBOX-3629] 2766\n[BBOX-3630] 2767\n[BBOX-3631] 2768\n[BBOX-3632] 2769\n[BBOX-3633] 2770\n[BBOX-3634] 2771\n[BBOX-3635] 2772\n[BBOX-3636] 2773\n[BBOX-3637] 2774\n[BBOX-3638] 2775\n[BBOX-3639] 2776\n[BBOX-3640] 2777\n[BBOX-3641] 2778\n[BBOX-3642] 2779\n[BBOX-3643] 2780\n[BBOX-3644] 2781\n[BBOX-3645] 2782\n[BBOX-3646] 2783\n[BBOX-3647] 2784\n[BBOX-3648] 2785\n[BBOX-3649] 2786\n[BBOX-3650] 2787\n[BBOX-3651] 2788\n[BBOX-3652] 2789\n[BBOX-3653] 2790\n[BBOX-3654] 2791\n[BBOX-3655] 2792\n[BBOX-3656] 2793\n[BBOX-3657] 2794\n[BBOX-3658] 2795\n[BBOX-3659] 2796\n[BBOX-3660] 2797\n[BBOX-3661] 2798\n[BBOX-3662] 2799\n[BBOX-3663] 2800\n[BBOX-3664] 2801\n[BBOX-3665] 2802\n[BBOX-3666] 2803\n[BBOX-3667] 2804\n[BBOX-3668] 2805\n[BBOX-3669] 2806\n[BBOX-3670] 2807\n[BBOX-3671] 2808\n[BBOX-3672] 2809\n[BBOX-3673] 2810\n[BBOX-3674] 2811\n[BBOX-3675] 2812\n[BBOX-3676] 2813\n[BBOX-3677] 2814"
  }
]
2026-08-06 02:17:36,896 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T02:17:36.895+00:00", "boot_at": "2026-08-06T01:59:43.412+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"5d401ece913c11f19b5e81513a69a703": {"id": "5d401ece913c11f19b5e81513a69a703", "doc_id": "5963bc44913b11f19b5e81513a69a703", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785982387379, "task_type": "dataflow", "root_trace_id": "7886908ae2584ba69682631c2a66f747", "root_traceparent": "00-7886908ae2584ba69682631c2a66f747-971004a6101741b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 02:17:48,260 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 02:17:48,293 INFO     29 [SmartSplitter] SmartSplitter done: 15 chunks from 15 LLM segments (all bbox_id). Types: {'OutpatientRecord': 5, 'PrescriptionRecord': 7, 'ExaminationReport': 3}
2026-08-06 02:17:48,304 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-06 02:17:48,305 INFO     29 [Trace] task=5d401ece | doc=LZK 哮喘 广三(1).pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "3678 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "chunks", "chunks": "15 items, types={'OutpatientRecord': 5, 'PrescriptionRecord': 7, 'ExaminationReport': 3}"}
2026-08-06 02:17:48,305 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-06 02:17:48,309 INFO     29 [ChunkRouter] Routed 15 chunks into 3 groups: {'chunks_Clinical': 5, 'chunks_Prescription': 7, 'chunks_Examination': 3}
2026-08-06 02:17:48,325 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-06 02:17:48,325 INFO     29 [Trace] task=5d401ece | doc=LZK 哮喘 广三(1).pdf | ChunkRouter:Router | outputs={"html": "", "json": "3678 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "chunks", "chunks": "15 items, types={'OutpatientRecord': 5, 'PrescriptionRecord': 7, 'ExaminationReport': 3}", "chunks_Clinical": "5 items, types={'OutpatientRecord': 5}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 5, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-06 02:17:48,325 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-06 02:17:48,332 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-06 02:17:48,333 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m02:17:48 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:17:48,346 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:17:49,104 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-06 02:17:49,116 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-06 02:17:49,117 INFO     29 [Trace] task=5d401ece | doc=LZK 哮喘 广三(1).pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "3678 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "chunks", "chunks_Clinical": "5 items, types={'OutpatientRecord': 5}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 5, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-06 02:17:49,117 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-06 02:17:49,131 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-06 02:17:49,132 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m02:17:49 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:17:49,133 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:17:52,453 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-06 02:17:52,463 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-06 02:17:52,464 INFO     29 [Trace] task=5d401ece | doc=LZK 哮喘 广三(1).pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "3678 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "chunks", "chunks_Clinical": "5 items, types={'OutpatientRecord': 5}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 5, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-06 02:17:52,464 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-06 02:17:52,474 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 02:17:52,474 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-06 02:17:52,474 INFO     29 [qwen-vl-text] positions(58): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 02:17:52,474 INFO     29 [qwen-vl-text] page grouping: [0, 1], lines per page: [18, 40]
2026-08-06 02:17:52,687 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-06 02:17:52,834 INFO     29 [qwen-vl-text] page=1, rect=842x595, img=(2339x1653), dpi=200
2026-08-06 02:17:52,835 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1721
2026-08-06 02:17:52,835 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-06 02:17:52,835 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 57, \"encounter_dates\": [\"2025-10-10\"], \"department\": \"内科门诊（荔湾）\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "病历编号：\n性别：男\n年龄：40岁\n就诊科室：内科门诊（荔湾）\n就诊时间：2025-10-10 14:36:06\n主诉：BAIYUN V8\n现病史：自上次访视至今，询问及查询HIS系统受试者有新增AE，无SAE、哮喘急性发作，有新增合并用药，发生2次医疗相关事件[2025年9月3日因过敏性鼻炎就诊专科门诊、本周曾因上呼吸道感染到社区医院就诊(具体不详，因HIS系统滞后无法收集具体情况及受试者无法回忆起当时情况及用药情况，待收集具体情况后补充详情)]。于2025年8月4日、2025年9月1日收到加重警报邮件，联系受试者后，均判断非哮喘急性发作。\n完成下流操作：\n1、查看受试者电子日志，受试者漏填2025年8月16日，2025年9月4日晚间日志，2025年9月4日、2025年9月25日早间日志；\n2、填写AQLQ+12和ACQ-5问卷，ACQ-5评分：0.8分；\n3、休息10分钟后，测量坐位生命体征：血压113/81mmHg，脉搏87次/分，呼吸频率20次/分，体温36.6℃，测量身高177.5cm，体重90.5kg(BMI=28.7kg/m2)；\n4、14:35体格检查：神志清，体查合作，自主体位，一般外表无异常，皮肤、粘膜无异常，唇甲无发绀，眼睛、耳、鼻、咽喉无异常，口咽部粘膜无异常，颈软，气管居中，甲状腺未及肿大，全身浅表淋巴结未及肿大，颈静脉无怒张，胸廓无畸形，双肺呼吸运动对称，双肺触觉语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及啰音。心前区无隆起，心尖搏动无弥散，心界不大，心率：87次/分，律齐，各瓣膜听诊区未闻及病理性杂音。腹平软，全腹无压痛、反跳痛。肝、脾肋下未及，肝肾区无叩击痛，肠鸣音存，4次/分，脊柱、四肢无畸形，生理征存，未引出病理征，其他系统未见明显异常；\n5、休息至少10分钟后，于14:58行12导联ECG检查；\n6、于15:01采集中心实验室样本(血常规，血生化)并送往中心试验室；\n7、回收试验药物BDAMDI@ASMDI3盒(152968-AH及185936-HK未开封，148729-UA未用60揿，实际使用46揿，发药当天预喷4揿，2025年9月10日前因超过7天未使用试验药物空喷2次共4揿，2025年9月10日后受试者每七天清洗一次后空喷5次共10揿，总计预喷18揿；epro记录使用总共46揿，与实际使用情况一致。\n8、回收epro以及AM3。\n既往史：更新合并用药：\n1、糠酸莫米松鼻喷雾剂2025.4.3-2025.7.25 每鼻 2喷/次 qm 治疗过敏性鼻炎。\n病历文书\n门诊病历\n25/10/10 14时 门诊病历\n25/10/24 15时 门诊病历（GCP专用）\n25/11/17 10时 门诊病历\n头降使用40瓶，平均每天使用4瓶，2025年9月10日用空4瓶（大木使用试验药剂空瓶2次共4\n瓶，2025年9月10日后受试者每七天清光一次后空瓶5次共10瓶，合计空瓶10瓶（qrs记录使\n用总共46瓶，与实际使用情况一致。\n8、回访qrs以及MD。\n既往史：更新合并用药：\n1、鼻腔莫米松鼻喷雾剂C025 4 3-2025 7 25 每鼻 2喷/次 qd 治疗过敏性鼻炎。\n2、苯环喹莫铵鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。\n4、氯卓斯汀氟替卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。\n5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/\n次 治疗过敏性鼻炎。\n6、枯草抗感染治疗（生理性海水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过\n敏性鼻炎\n已预约受试者安全性随访时间。\n过敏史：\n个人史：\n体格检查：\n专科情况：\n辅助检查：\n治疗项目：\n门诊诊断：\n支气管哮喘\n单病种：\n发病时间：\n处\n置：\n1心电图（心电图室做）\n2布地奈德福莫特罗吸入粉雾剂(II)(省采)●①② 2盒2000,日入用药,一天2次\n30天\n备注：\n病情评估：\n病情分级：\n是否抢救病例：否\n是否抢救成功：\n是否为绿色通道患者：否\n病人去向：",
    "role": "user"
  }
]
[92m02:17:52 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:17:52,837 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:17:57,967 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-06 02:17:57,968 INFO     29 [qwen-vl-text] LLM output (len=683):
{
  "encounter_date": "2025-10-10",
  "chief_complaint": "BAIYUN V8",
  "present_illness": "自上次访视至今，询问及查询HIS系统受试者有新增AE，无SAE、哮喘急性发作，有新增合并用药，发生2次医疗相关事件[2025年9月3日因过敏性鼻炎就诊专科门诊、本周曾因上呼吸道感染到社区医院就诊(具体不详，因HIS系统滞后无法收集具体情况及受试者无法回忆起当时情况及用药情况，待收集具体情况后补充详情)]。于2025年8月4日、2025年9月1日收到加重警报邮件，联系受试者后，均判断非哮喘急性发作。",
  "past_history": "更新合并用药：1、糠酸莫米松鼻喷雾剂2025.4.3-2025.7.25 每鼻 2喷/次 qm 治疗过敏性鼻炎；2、苯环喹莫铵鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎；4、氯卓斯汀氟替卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎；5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/次 治疗过敏性鼻炎；6、枯草抗感染治疗（生理性海水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过敏性鼻炎",
  "diagnosis": "支气管哮喘",
  "treatment_plan": "1心电图（心电图室做）；2布地奈德福莫特罗吸入粉雾剂(II)(省采)●①② 2盒2000,日入用药,一天2次 30天"
}
2026-08-06 02:17:57,968 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-10-10]
2026-08-06 02:17:57,969 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1320554, prompt_len=1732
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
2026-08-06 02:18:11,611 INFO     29 [qwen-vl-text] coord API raw response (len=1890):
[
	{"text": "病历编号：", "bbox": [541, 117, 617, 134]},
	{"text": "性别：男", "bbox": [438, 150, 501, 167], "bbox": [438, 150, 501, 167]},
	{"text": "年龄：40岁", "bbox": [627, 151, 690, 167]},
	{"text": "就诊科室：内科门诊（荔湾）", "bbox": [162, 182, 372, 199]},
	{"text": "就诊时间：2025-10-10 14:36:06", "bbox": [541, 183, 795, 199]},
	{"text": "主诉：BAIYUN V8", "bbox": [160, 214, 400, 231]},
	{"text": "现病史：自上次访视至今，询问及查询HIS系统受试者有新增AE，无SAE、哮喘急性发作，有新增合并用药，发生2次医疗相关事件[2025年9月3日因过敏性鼻炎就诊专科门诊、本周曾因上呼吸道感染到社区医院就诊(具体不详，因HIS系统滞后无法收集具体情况及受试者无法回忆起当时情况及用药情况，待收集具体情况后补充详情)]。于2025年8月4日、2025年9月1日收到加重警报邮件，联系受试者后，均判断非哮喘急性发作。", "bbox": [160, 246, 856, 345]},
	{"text": "完成下流操作：", "bbox": [160, 359, 275, 375]},
	{"text": "1、查看受试者电子日志，受试者漏填2025年8月16日，2025年9月4日晚间日志，2025年9月4日、2025年9月25日早间日志；", "bbox": [160, 389, 852, 425]},
	{"text": "2、填写AQLQ+12和ACQ-5问卷，ACQ-5评分：0.8分；", "bbox": [160, 438, 540, 455]},
	{"text": "3、休息10分钟后，测量坐位生命体征：血压113/81mmHg，脉搏87次/分，呼吸频率20次/分，体温36.6℃，测量身高177.5cm，体重90.5kg(BMI=28.7kg/m2)；", "bbox": [160, 468, 823, 505]},
	{"text": "4、14:35体格检查：神志清，体查合作，自主体位，一般外表无异常，皮肤、粘膜无异常，唇甲无发绀，眼睛、耳、鼻、咽喉无异常，口咽部粘膜无异常，颈软，气管居中，甲状腺未及肿大，全身浅表淋巴结未及肿大，颈静脉无怒张，胸廓无畸形，双肺呼吸运动对称，双肺触觉语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及啰音。心前区无隆起，心尖搏动无弥散，心界不大，心率：87次/分，律齐，各瓣膜听诊区未闻及病理性杂音。腹平软，全腹无压痛、反跳痛。肝、脾肋下未及，肝肾区无叩击痛，肠鸣音存，4次/分，脊柱、四肢无畸形，生理征存，未引出病理征，其他系统未见明显异常；", "bbox": [160, 518, 843, 658]},
	{"text": "5、休息至少10分钟后，于14:58行12导联ECG检查；", "bbox": [160, 672, 532, 689]},
	{"text": "6、于15:01采集中心实验室样本(血常规，血生化)并送往中心试验室；", "bbox": [160, 702, 673, 719]},
	{"text": "7、回收试验药物BDAMDI@ASMDI3盒(152968-AH及185936-HK未开封，148729-UA未用60揿，实际使用46揿，发药当天预喷4揿，2025年9月10日前因超过7天未使用试验药物空喷2次共4揿，2025年9月10日后受试者每七天清洗一次后空喷5次共10揿，总计预喷18揿；epro记录使用总共46揿，与实际使用情况一致。", "bbox": [160, 732, 823, 809]},
	{"text": "8、回收epro以及AM3。", "bbox": [160, 823, 325, 840]},
	{"text": "既往史：更新合并用药：", "bbox": [160, 854, 380, 871]},
	{"text": "1、糠酸莫米松鼻喷雾剂2025.4.3-2025.7.25 每鼻 2喷/次 qm 治疗过敏性鼻炎。", "bbox": [160, 883, 767, 899]}
]
2026-08-06 02:18:11,611 INFO     29 [qwen-vl-text] coord API: raw_items=18, valid_items=18, elapsed=13.6s
2026-08-06 02:18:11,611 INFO     29 [qwen-vl-text] coord item[0]: text=病历编号：, bbox=[541, 117, 617, 134]
2026-08-06 02:18:11,611 INFO     29 [qwen-vl-text] coord item[1]: text=性别：男, bbox=[438, 150, 501, 167]
2026-08-06 02:18:11,611 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：40岁, bbox=[627, 151, 690, 167]
2026-08-06 02:18:11,611 INFO     29 [qwen-vl-text] coord item[3]: text=就诊科室：内科门诊（荔湾）, bbox=[162, 182, 372, 199]
2026-08-06 02:18:11,611 INFO     29 [qwen-vl-text] coord item[4]: text=就诊时间：2025-10-10 14:36:06, bbox=[541, 183, 795, 199]
2026-08-06 02:18:11,611 INFO     29 [qwen-vl-text] coord item[5]: text=主诉：BAIYUN V8, bbox=[160, 214, 400, 231]
2026-08-06 02:18:11,611 INFO     29 [qwen-vl-text] coord item[6]: text=现病史：自上次访视至今，询问及查询HIS系统受试者有新增AE，无SAE、哮喘急性发作，有新增合并用药，发生2次医疗相关事件[2025年9月3日因过敏性鼻炎就诊专科门诊、本周曾因上呼吸道感染到社区医院就诊(具体不详，因HIS系统滞后无法收集具体情况及受试者无法回忆起当时情况及用药情况，待收集具体情况后补充详情)]。于2025年8月4日、2025年9月1日收到加重警报邮件，联系受试者后，均判断非哮喘急性发作。, bbox=[160, 246, 856, 345]
2026-08-06 02:18:11,611 INFO     29 [qwen-vl-text] coord item[7]: text=完成下流操作：, bbox=[160, 359, 275, 375]
2026-08-06 02:18:11,611 INFO     29 [qwen-vl-text] coord item[8]: text=1、查看受试者电子日志，受试者漏填2025年8月16日，2025年9月4日晚间日志，2025年9月4日、2025年9月25日早间日志；, bbox=[160, 389, 852, 425]
2026-08-06 02:18:11,611 INFO     29 [qwen-vl-text] coord item[9]: text=2、填写AQLQ+12和ACQ-5问卷，ACQ-5评分：0.8分；, bbox=[160, 438, 540, 455]
2026-08-06 02:18:11,611 INFO     29 [qwen-vl-text] coord item[10]: text=3、休息10分钟后，测量坐位生命体征：血压113/81mmHg，脉搏87次/分，呼吸频率20次/分，体温36.6℃，测量身高177.5cm，体重90.5kg(BMI=28.7kg/m2)；, bbox=[160, 468, 823, 505]
2026-08-06 02:18:11,611 INFO     29 [qwen-vl-text] coord item[11]: text=4、14:35体格检查：神志清，体查合作，自主体位，一般外表无异常，皮肤、粘膜无异常，唇甲无发绀，眼睛、耳、鼻、咽喉无异常，口咽部粘膜无异常，颈软，气管居中，甲状腺未及肿大，全身浅表淋巴结未及肿大，颈静脉无怒张，胸廓无畸形，双肺呼吸运动对称，双肺触觉语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及啰音。心前区无隆起，心尖搏动无弥散，心界不大，心率：87次/分，律齐，各瓣膜听诊区未闻及病理性杂音。腹平软，全腹无压痛、反跳痛。肝、脾肋下未及，肝肾区无叩击痛，肠鸣音存，4次/分，脊柱、四肢无畸形，生理征存，未引出病理征，其他系统未见明显异常；, bbox=[160, 518, 843, 658]
2026-08-06 02:18:11,611 INFO     29 [qwen-vl-text] coord item[12]: text=5、休息至少10分钟后，于14:58行12导联ECG检查；, bbox=[160, 672, 532, 689]
2026-08-06 02:18:11,611 INFO     29 [qwen-vl-text] coord item[13]: text=6、于15:01采集中心实验室样本(血常规，血生化)并送往中心试验室；, bbox=[160, 702, 673, 719]
2026-08-06 02:18:11,611 INFO     29 [qwen-vl-text] coord item[14]: text=7、回收试验药物BDAMDI@ASMDI3盒(152968-AH及185936-HK未开封，148729-UA未用60揿，实际使用46揿，发药当天预喷4揿，2025年9月10日前因超过7天未使用试验药物空喷2次共4揿，2025年9月10日后受试者每七天清洗一次后空喷5次共10揿，总计预喷18揿；epro记录使用总共46揿，与实际使用情况一致。, bbox=[160, 732, 823, 809]
2026-08-06 02:18:11,612 INFO     29 [qwen-vl-text] coord item[15]: text=8、回收epro以及AM3。, bbox=[160, 823, 325, 840]
2026-08-06 02:18:11,612 INFO     29 [qwen-vl-text] coord item[16]: text=既往史：更新合并用药：, bbox=[160, 854, 380, 871]
2026-08-06 02:18:11,612 INFO     29 [qwen-vl-text] coord item[17]: text=1、糠酸莫米松鼻喷雾剂2025.4.3-2025.7.25 每鼻 2喷/次 qm 治疗过敏性鼻炎。, bbox=[160, 883, 767, 899]
2026-08-06 02:18:11,612 INFO     29 [qwen-vl-text] page=0 — 18/18 coords, api_time=13.6s
2026-08-06 02:18:11,615 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=708232, prompt_len=1388
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共40行）
["病历文书", "门诊病历", "25/10/10 14时 门诊病历", "25/10/24 15时 门诊病历（GCP专用）", "25/11/17 10时 门诊病历", "头降使用40瓶，平均每天使用4瓶，2025年9月10日用空4瓶（大木使用试验药剂空瓶2次共4", "瓶，2025年9月10日后受试者每七天清光一次后空瓶5次共10瓶，合计空瓶10瓶（qrs记录使", "用总共46瓶，与实际使用情况一致。", "8、回访qrs以及MD。", "既往史：更新合并用药：", "1、鼻腔莫米松鼻喷雾剂C025 4 3-2025 7 25 每鼻 2喷/次 qd 治疗过敏性鼻炎。", "2、苯环喹莫铵鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。", "4、氯卓斯汀氟替卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。", "5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/", "次 治疗过敏性鼻炎。", "6、枯草抗感染治疗（生理性海水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过", "敏性鼻炎", "已预约受试者安全性随访时间。", "过敏史：", "个人史：", "体格检查：", "专科情况：", "辅助检查：", "治疗项目：", "门诊诊断：", "支气管哮喘", "单病种：", "发病时间：", "处", "置：", "1心电图（心电图室做）", "2布地奈德福莫特罗吸入粉雾剂(II)(省采)●①② 2盒2000,日入用药,一天2次", "30天", "备注：", "病情评估：", "病情分级：", "是否抢救病例：否", "是否抢救成功：", "是否为绿色通道患者：否", "病人去向："]

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
2026-08-06 02:18:24,171 INFO     29 [qwen-vl-text] coord API raw response (len=2405):
[
	{"text": "病历文书", "bbox": [18, 35, 58, 49]},
	{"text": "门诊病历", "bbox": [18, 93, 64, 110]},
	{"text": "25/10/10 14时 门诊病历", "bbox": [18, 139, 127, 154]},
	{"text": "25/10/24 15时 门诊病历（GCP专用）", "bbox": [18, 188, 180, 203]},
	{"text": "25/11/17 10时 门诊病历", "bbox": [18, 237, 127, 252]},
	{"text": "头降使用40瓶，平均每天使用4瓶，2025年9月10日用空4瓶（大木使用试验药剂空瓶2次共4", "bbox": [630, 73, 943, 86]},
	{"text": "瓶，2025年9月10日后受试者每七天清光一次后空瓶5次共10瓶，合计空瓶10瓶（qrs记录使", "bbox": [630, 90, 947, 104]},
	{"text": "用总共46瓶，与实际使用情况一致。", "bbox": [630, 109, 754, 122]},
	{"text": "8、回访qrs以及MD。", "bbox": [630, 138, 707, 151]},
	{"text": "既往史：更新合并用药：", "bbox": [630, 168, 733, 181]},
	{"text": "1、鼻腔莫米松鼻喷雾剂C025 4 3-2025 7 25 每鼻 2喷/次 qd 治疗过敏性鼻炎。", "bbox": [630, 196, 926, 210]},
	{"text": "2、苯环喹莫铵鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。", "bbox": [630, 225, 911, 239]},
	{"text": "4、氯卓斯汀氟替卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。", "bbox": [630, 253, 942, 267]},
	{"text": "5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/", "bbox": [630, 282, 933, 295]},
	{"text": "次 治疗过敏性鼻炎。", "bbox": [630, 300, 707, 313]},
	{"text": "6、枯草抗感染治疗（生理性海水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过", "bbox": [630, 330, 949, 343]},
	{"text": "敏性鼻炎", "bbox": [630, 350, 663, 363]},
	{"text": "已预约受试者安全性随访时间。", "bbox": [630, 378, 738, 391]},
	{"text": "过敏史：", "bbox": [630, 407, 685, 421]},
	{"text": "个人史：", "bbox": [630, 435, 678, 449]},
	{"text": "体格检查：", "bbox": [630, 464, 670, 477]},
	{"text": "专科情况：", "bbox": [630, 492, 670, 505]},
	{"text": "辅助检查：", "bbox": [630, 521, 670, 534]},
	{"text": "治疗项目：", "bbox": [630, 550, 668, 563]},
	{"text": "门诊诊断：", "bbox": [630, 578, 668, 591]},
	{"text": "支气管哮喘", "bbox": [683, 608, 723, 621]},
	{"text": "单病种：", "bbox": [630, 636, 678, 650]},
	{"text": "发病时间：", "bbox": [630, 665, 668, 678]},
	{"text": "处", "bbox": [630, 694, 639, 707]},
	{"text": "置：", "bbox": [674, 694, 687, 707]},
	{"text": "1心电图（心电图室做）", "bbox": [638, 723, 719, 736]},
	{"text": "2布地奈德福莫特罗吸入粉雾剂(II)(省采)●①② 2盒2000,日入用药,一天2次", "bbox": [638, 753, 915, 766]},
	{"text": "30天", "bbox": [930, 754, 947, 767]},
	{"text": "备注：", "bbox": [630, 782, 687, 796]},
	{"text": "病情评估：", "bbox": [630, 812, 670, 825]},
	{"text": "病情分级：", "bbox": [787, 812, 825, 825]},
	{"text": "是否抢救病例：否", "bbox": [630, 841, 699, 854]},
	{"text": "是否抢救成功：", "bbox": [748, 841, 803, 854]},
	{"text": "是否为绿色通道患者：否", "bbox": [832, 841, 924, 854]},
	{"text": "病人去向：", "bbox": [630, 869, 668, 882]}
]
2026-08-06 02:18:24,172 INFO     29 [qwen-vl-text] coord API: raw_items=40, valid_items=40, elapsed=12.6s
2026-08-06 02:18:24,172 INFO     29 [qwen-vl-text] coord item[0]: text=病历文书, bbox=[18, 35, 58, 49]
2026-08-06 02:18:24,172 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[18, 93, 64, 110]
2026-08-06 02:18:24,172 INFO     29 [qwen-vl-text] coord item[2]: text=25/10/10 14时 门诊病历, bbox=[18, 139, 127, 154]
2026-08-06 02:18:24,172 INFO     29 [qwen-vl-text] coord item[3]: text=25/10/24 15时 门诊病历（GCP专用）, bbox=[18, 188, 180, 203]
2026-08-06 02:18:24,172 INFO     29 [qwen-vl-text] coord item[4]: text=25/11/17 10时 门诊病历, bbox=[18, 237, 127, 252]
2026-08-06 02:18:24,172 INFO     29 [qwen-vl-text] coord item[5]: text=头降使用40瓶，平均每天使用4瓶，2025年9月10日用空4瓶（大木使用试验药剂空瓶2次共4, bbox=[630, 73, 943, 86]
2026-08-06 02:18:24,172 INFO     29 [qwen-vl-text] coord item[6]: text=瓶，2025年9月10日后受试者每七天清光一次后空瓶5次共10瓶，合计空瓶10瓶（qrs记录使, bbox=[630, 90, 947, 104]
2026-08-06 02:18:24,172 INFO     29 [qwen-vl-text] coord item[7]: text=用总共46瓶，与实际使用情况一致。, bbox=[630, 109, 754, 122]
2026-08-06 02:18:24,172 INFO     29 [qwen-vl-text] coord item[8]: text=8、回访qrs以及MD。, bbox=[630, 138, 707, 151]
2026-08-06 02:18:24,172 INFO     29 [qwen-vl-text] coord item[9]: text=既往史：更新合并用药：, bbox=[630, 168, 733, 181]
2026-08-06 02:18:24,172 INFO     29 [qwen-vl-text] coord item[10]: text=1、鼻腔莫米松鼻喷雾剂C025 4 3-2025 7 25 每鼻 2喷/次 qd 治疗过敏性鼻炎。, bbox=[630, 196, 926, 210]
2026-08-06 02:18:24,172 INFO     29 [qwen-vl-text] coord item[11]: text=2、苯环喹莫铵鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。, bbox=[630, 225, 911, 239]
2026-08-06 02:18:24,172 INFO     29 [qwen-vl-text] coord item[12]: text=4、氯卓斯汀氟替卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。, bbox=[630, 253, 942, 267]
2026-08-06 02:18:24,172 INFO     29 [qwen-vl-text] coord item[13]: text=5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/, bbox=[630, 282, 933, 295]
2026-08-06 02:18:24,172 INFO     29 [qwen-vl-text] coord item[14]: text=次 治疗过敏性鼻炎。, bbox=[630, 300, 707, 313]
2026-08-06 02:18:24,172 INFO     29 [qwen-vl-text] coord item[15]: text=6、枯草抗感染治疗（生理性海水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过, bbox=[630, 330, 949, 343]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[16]: text=敏性鼻炎, bbox=[630, 350, 663, 363]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[17]: text=已预约受试者安全性随访时间。, bbox=[630, 378, 738, 391]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[18]: text=过敏史：, bbox=[630, 407, 685, 421]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[19]: text=个人史：, bbox=[630, 435, 678, 449]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[20]: text=体格检查：, bbox=[630, 464, 670, 477]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[21]: text=专科情况：, bbox=[630, 492, 670, 505]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[22]: text=辅助检查：, bbox=[630, 521, 670, 534]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[23]: text=治疗项目：, bbox=[630, 550, 668, 563]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[24]: text=门诊诊断：, bbox=[630, 578, 668, 591]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[25]: text=支气管哮喘, bbox=[683, 608, 723, 621]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[26]: text=单病种：, bbox=[630, 636, 678, 650]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[27]: text=发病时间：, bbox=[630, 665, 668, 678]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[28]: text=处, bbox=[630, 694, 639, 707]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[29]: text=置：, bbox=[674, 694, 687, 707]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[30]: text=1心电图（心电图室做）, bbox=[638, 723, 719, 736]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[31]: text=2布地奈德福莫特罗吸入粉雾剂(II)(省采)●①② 2盒2000,日入用药,一天2次, bbox=[638, 753, 915, 766]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[32]: text=30天, bbox=[930, 754, 947, 767]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[33]: text=备注：, bbox=[630, 782, 687, 796]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[34]: text=病情评估：, bbox=[630, 812, 670, 825]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[35]: text=病情分级：, bbox=[787, 812, 825, 825]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[36]: text=是否抢救病例：否, bbox=[630, 841, 699, 854]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[37]: text=是否抢救成功：, bbox=[748, 841, 803, 854]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[38]: text=是否为绿色通道患者：否, bbox=[832, 841, 924, 854]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] coord item[39]: text=病人去向：, bbox=[630, 869, 668, 882]
2026-08-06 02:18:24,173 INFO     29 [qwen-vl-text] page=1 — 40/40 coords, api_time=12.6s
2026-08-06 02:18:24,174 INFO     29 [qwen-vl-text] new_positions (58):
[[0, 321.895, 367.115, 98.514, 112.828], [0, 260.61, 298.09499999999997, 126.3, 140.614], [0, 373.065, 410.54999999999995, 127.142, 140.614], [0, 96.39, 221.34, 153.244, 167.558], [0, 321.895, 473.025, 154.08599999999998, 167.558], [0, 95.19999999999999, 238.0, 180.188, 194.50199999999998], [0, 95.19999999999999, 509.32, 207.132, 290.49], [0, 95.19999999999999, 163.625, 302.27799999999996, 315.75], [0, 95.19999999999999, 506.94, 327.538, 357.84999999999997], [0, 95.19999999999999, 321.3, 368.796, 383.11], [0, 95.19999999999999, 489.685, 394.056, 425.21], [0, 95.19999999999999, 501.585, 436.156, 554.036], [0, 95.19999999999999, 316.53999999999996, 565.824, 580.138], [0, 95.19999999999999, 400.435, 591.084, 605.398], [0, 95.19999999999999, 489.685, 616.3439999999999, 681.178], [0, 95.19999999999999, 193.375, 692.966, 707.28], [0, 95.19999999999999, 226.1, 719.068, 733.382], [0, 95.19999999999999, 456.36499999999995, 743.486, 756.958], [1, 15.155999999999999, 48.836, 20.825, 29.154999999999998], [1, 15.155999999999999, 53.888, 55.335, 65.45], [1, 15.155999999999999, 106.934, 82.705, 91.63], [1, 15.155999999999999, 151.56, 111.86, 120.785], [1, 15.155999999999999, 106.934, 141.015, 149.94], [1, 530.46, 794.006, 43.434999999999995, 51.169999999999995], [1, 530.46, 797.374, 53.55, 61.879999999999995], [1, 530.46, 634.8679999999999, 64.855, 72.59], [1, 530.46, 595.294, 82.11, 89.845], [1, 530.46, 617.1859999999999, 99.96, 107.695], [1, 530.46, 779.692, 116.61999999999999, 124.94999999999999], [1, 530.46, 767.062, 133.875, 142.20499999999998], [1, 530.46, 793.164, 150.535, 158.86499999999998], [1, 530.46, 785.586, 167.79, 175.525], [1, 530.46, 595.294, 178.5, 186.23499999999999], [1, 530.46, 799.058, 196.35, 204.08499999999998], [1, 530.46, 558.246, 208.25, 215.98499999999999], [1, 530.46, 621.396, 224.91, 232.64499999999998], [1, 530.46, 576.77, 242.165, 250.49499999999998], [1, 530.46, 570.876, 258.825, 267.155], [1, 530.46, 564.14, 276.08, 283.815], [1, 530.46, 564.14, 292.74, 300.47499999999997], [1, 530.46, 564.14, 309.995, 317.72999999999996], [1, 530.46, 562.456, 327.25, 334.98499999999996], [1, 530.46, 562.456, 343.90999999999997, 351.645], [1, 575.086, 608.766, 361.76, 369.495], [1, 530.46, 570.876, 378.41999999999996, 386.75], [1, 530.46, 562.456, 395.67499999999995, 403.40999999999997], [1, 530.46, 538.038, 412.93, 420.66499999999996], [1, 567.5079999999999, 578.454, 412.93, 420.66499999999996], [1, 537.196, 605.398, 430.185, 437.91999999999996], [1, 537.196, 770.43, 448.03499999999997, 455.77], [1, 783.06, 797.374, 448.63, 456.36499999999995], [1, 530.46, 578.454, 465.28999999999996, 473.62], [1, 530.46, 564.14, 483.14, 490.875], [1, 662.654, 694.65, 483.14, 490.875], [1, 530.46, 588.558, 500.395, 508.13], [1, 629.816, 676.126, 500.395, 508.13], [1, 700.544, 778.0079999999999, 500.395, 508.13], [1, 530.46, 562.456, 517.055, 524.79]]
2026-08-06 02:18:24,174 INFO     29 [qwen-vl-text] ═══ DONE ═══ 58 positions, pages=2, time=31.7s
2026-08-06 02:18:24,174 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 02:18:24,174 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-06 02:18:24,174 INFO     29 [qwen-vl-text] positions(34): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 02:18:24,174 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [34]
2026-08-06 02:18:24,384 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-06 02:18:24,385 INFO     29 [qwen-vl-text] LLM extraction start, text_len=851
2026-08-06 02:18:24,385 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-06 02:18:24,385 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 60, \"bbox_end\": 93, \"encounter_dates\": [\"2025-10-24\"], \"department\": \"内科门诊（荔湾）\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "就诊卡\n流水号：\n姓名\n龄：40岁\n就诊科\n目：2025-10-24 15:45:39\n主诉：安全性电话随访\n现病史：今日10:27\n固定电话（020-\n(159\n5），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无\n不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对\nV8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试\n者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，\n目前无安全性异常表现。\n合并用药更新：\n1、小柴胡颗粒、（自行购药）2025.10.6-2025.10.8 10g tid 治疗上呼吸道感染\n2、苯环喹溴铵鼻喷雾剂 2025.4.3-至今 每鼻2喷/次 qid 治疗过敏性鼻炎\n3、氮卓斯汀氟替卡松鼻喷雾剂 2025.9.3-至今 每鼻2喷/次 bid 治疗过敏性鼻炎\n4、辛芩颗粒 2024.8.21-2024.8.27 1袋 冲服 tid 治疗过敏性鼻炎\nAE：\n上呼吸道感染 2025年10月5日-2025年10月8日 中度，非SAE，采取药物治疗措施，对试验\n药物采取措施：剂量不变，与试验药物无关，未因该AE退出研究。\n病历更正：\n1、更正2024年10月22日病历，合并用药“辛芩颗粒”为“辛芩颗粒”；\n2、更正2024年10月22日病历，合并用药“苯环喹溴铵鼻喷雾剂”为“苯环喹溴铵鼻喷雾\n剂”；\n3、更正2026年1月24日病历，“无收到ePro触发的哮喘警报邮件”为“有收到ePro触发的哮\n喘警报邮件”；\n4、更正2025年7月18日病历，“受试者漏填2025年4月28日晚间日志” 更正为：“受试者\n漏填2025年4月28日早间日志”；\n5、更正2024年11月6日病历，“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共\n计用了26喷”为：“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了28\n喷”。",
    "role": "user"
  }
]
[92m02:18:24 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:18:24,387 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:18:24,388 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T02:18:24.386+00:00", "boot_at": "2026-08-06T01:59:43.412+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"5d401ece913c11f19b5e81513a69a703": {"id": "5d401ece913c11f19b5e81513a69a703", "doc_id": "5963bc44913b11f19b5e81513a69a703", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785982387379, "task_type": "dataflow", "root_trace_id": "7886908ae2584ba69682631c2a66f747", "root_traceparent": "00-7886908ae2584ba69682631c2a66f747-971004a6101741b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 02:18:29,360 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-06 02:18:29,360 INFO     29 [qwen-vl-text] LLM output (len=638):
{
  "encounter_date": "2025-10-24",
  "chief_complaint": "安全性电话随访",
  "present_illness": "今日10:27固定电话（020-1595），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对V8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，目前无安全性异常表现。合并用药更新：1、小柴胡颗粒、（自行购药）2025.10.6-2025.10.8 10g tid 治疗上呼吸道感染；2、苯环喹溴铵鼻喷雾剂 2025.4.3-至今 每鼻2喷/次 qid 治疗过敏性鼻炎；3、氮卓斯汀氟替卡松鼻喷雾剂 2025.9.3-至今 每鼻2喷/次 bid 治疗过敏性鼻炎；4、辛芩颗粒 2024.8.21-2024.8.27 1袋 冲服 tid 治疗过敏性鼻炎。AE：上呼吸道感染 2025年10月5日-2025年10月8日 中度，非SAE，采取药物治疗措施，对试验药物采取措施：剂量不变，与试验药物无关，未因该AE退出研究。",
  "past_history": null,
  "diagnosis": null,
  "treatment_plan": null
}
2026-08-06 02:18:29,360 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-10-24]
2026-08-06 02:18:29,363 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1082890, prompt_len=1566
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共34行）
["就诊卡", "流水号：", "姓名", "龄：40岁", "就诊科", "目：2025-10-24 15:45:39", "主诉：安全性电话随访", "现病史：今日10:27", "固定电话（020-", "(159", "5），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无", "不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对", "V8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试", "者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，", "目前无安全性异常表现。", "合并用药更新：", "1、小柴胡颗粒、（自行购药）2025.10.6-2025.10.8 10g tid 治疗上呼吸道感染", "2、苯环喹溴铵鼻喷雾剂 2025.4.3-至今 每鼻2喷/次 qid 治疗过敏性鼻炎", "3、氮卓斯汀氟替卡松鼻喷雾剂 2025.9.3-至今 每鼻2喷/次 bid 治疗过敏性鼻炎", "4、辛芩颗粒 2024.8.21-2024.8.27 1袋 冲服 tid 治疗过敏性鼻炎", "AE：", "上呼吸道感染 2025年10月5日-2025年10月8日 中度，非SAE，采取药物治疗措施，对试验", "药物采取措施：剂量不变，与试验药物无关，未因该AE退出研究。", "病历更正：", "1、更正2024年10月22日病历，合并用药“辛芩颗粒”为“辛芩颗粒”；", "2、更正2024年10月22日病历，合并用药“苯环喹溴铵鼻喷雾剂”为“苯环喹溴铵鼻喷雾", "剂”；", "3、更正2026年1月24日病历，“无收到ePro触发的哮喘警报邮件”为“有收到ePro触发的哮", "喘警报邮件”；", "4、更正2025年7月18日病历，“受试者漏填2025年4月28日晚间日志” 更正为：“受试者", "漏填2025年4月28日早间日志”；", "5、更正2024年11月6日病历，“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共", "计用了26喷”为：“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了28", "喷”。"]

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
2026-08-06 02:18:44,545 INFO     29 [qwen-vl-text] coord API raw response (len=2349):
[
	{"text": "就诊卡", "bbox": [170, 98, 218, 115]},
	{"text": "流水号：", "bbox": [170, 131, 218, 148]},
	{"text": "姓名", "bbox": [170, 165, 187, 181]},
	{"text": "龄：40岁", "bbox": [647, 165, 710, 181]},
	{"text": "就诊科", "bbox": [170, 196, 218, 213]},
	{"text": "目：2025-10-24 15:45:39", "bbox": [616, 197, 819, 212]},
	{"text": "主诉：安全性电话随访", "bbox": [166, 228, 428, 246]},
	{"text": "现病史：今日10:27", "bbox": [166, 258, 361, 276]},
	{"text": "固定电话（020-", "bbox": [513, 258, 644, 276]},
	{"text": "(159", "bbox": [173, 281, 210, 298]},
	{"text": "5），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无", "bbox": [268, 281, 872, 298]},
	{"text": "不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对", "bbox": [166, 302, 878, 319]},
	{"text": "V8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试", "bbox": [166, 323, 877, 340]},
	{"text": "者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，", "bbox": [166, 344, 865, 361]},
	{"text": "目前无安全性异常表现。", "bbox": [166, 365, 355, 381]},
	{"text": "合并用药更新：", "bbox": [166, 395, 280, 411]},
	{"text": "1、小柴胡颗粒、（自行购药）2025.10.6-2025.10.8 10g tid 治疗上呼吸道感染", "bbox": [166, 425, 806, 442]},
	{"text": "2、苯环喹溴铵鼻喷雾剂 2025.4.3-至今 每鼻2喷/次 qid 治疗过敏性鼻炎", "bbox": [166, 455, 768, 472]},
	{"text": "3、氮卓斯汀氟替卡松鼻喷雾剂 2025.9.3-至今 每鼻2喷/次 bid 治疗过敏性鼻炎", "bbox": [166, 484, 818, 501]},
	{"text": "4、辛芩颗粒 2024.8.21-2024.8.27 1袋 冲服 tid 治疗过敏性鼻炎", "bbox": [166, 514, 718, 530]},
	{"text": "AE：", "bbox": [166, 545, 192, 558]},
	{"text": "上呼吸道感染 2025年10月5日-2025年10月8日 中度，非SAE，采取药物治疗措施，对试验", "bbox": [166, 573, 851, 590]},
	{"text": "药物采取措施：剂量不变，与试验药物无关，未因该AE退出研究。", "bbox": [166, 593, 656, 609]},
	{"text": "病历更正：", "bbox": [166, 622, 244, 638]},
	{"text": "1、更正2024年10月22日病历，合并用药“辛芩颗粒”为“辛芩颗粒”；", "bbox": [166, 651, 693, 668]},
	{"text": "2、更正2024年10月22日病历，合并用药“苯环喹溴铵鼻喷雾剂”为“苯环喹溴铵鼻喷雾", "bbox": [166, 679, 812, 696]},
	{"text": "剂”；", "bbox": [166, 698, 210, 714]},
	{"text": "3、更正2026年1月24日病历，“无收到ePro触发的哮喘警报邮件”为“有收到ePro触发的哮", "bbox": [166, 726, 831, 743]},
	{"text": "喘警报邮件”；", "bbox": [166, 745, 277, 761]},
	{"text": "4、更正2025年7月18日病历，“受试者漏填2025年4月28日晚间日志” 更正为：“受试者", "bbox": [166, 772, 817, 789]},
	{"text": "漏填2025年4月28日早间日志”；", "bbox": [166, 790, 402, 806]},
	{"text": "5、更正2024年11月6日病历，“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共", "bbox": [166, 817, 819, 834]},
	{"text": "计用了26喷”为：“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了28", "bbox": [166, 835, 802, 852]},
	{"text": "喷”。", "bbox": [166, 853, 213, 867]}
]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=15.2s
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[0]: text=就诊卡, bbox=[170, 98, 218, 115]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[1]: text=流水号：, bbox=[170, 131, 218, 148]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[170, 165, 187, 181]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[3]: text=龄：40岁, bbox=[647, 165, 710, 181]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[4]: text=就诊科, bbox=[170, 196, 218, 213]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[5]: text=目：2025-10-24 15:45:39, bbox=[616, 197, 819, 212]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[6]: text=主诉：安全性电话随访, bbox=[166, 228, 428, 246]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[7]: text=现病史：今日10:27, bbox=[166, 258, 361, 276]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[8]: text=固定电话（020-, bbox=[513, 258, 644, 276]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[9]: text=(159, bbox=[173, 281, 210, 298]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[10]: text=5），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无, bbox=[268, 281, 872, 298]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[11]: text=不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对, bbox=[166, 302, 878, 319]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[12]: text=V8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试, bbox=[166, 323, 877, 340]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[13]: text=者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，, bbox=[166, 344, 865, 361]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[14]: text=目前无安全性异常表现。, bbox=[166, 365, 355, 381]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[15]: text=合并用药更新：, bbox=[166, 395, 280, 411]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[16]: text=1、小柴胡颗粒、（自行购药）2025.10.6-2025.10.8 10g tid 治疗上呼吸道感染, bbox=[166, 425, 806, 442]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[17]: text=2、苯环喹溴铵鼻喷雾剂 2025.4.3-至今 每鼻2喷/次 qid 治疗过敏性鼻炎, bbox=[166, 455, 768, 472]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[18]: text=3、氮卓斯汀氟替卡松鼻喷雾剂 2025.9.3-至今 每鼻2喷/次 bid 治疗过敏性鼻炎, bbox=[166, 484, 818, 501]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[19]: text=4、辛芩颗粒 2024.8.21-2024.8.27 1袋 冲服 tid 治疗过敏性鼻炎, bbox=[166, 514, 718, 530]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[20]: text=AE：, bbox=[166, 545, 192, 558]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[21]: text=上呼吸道感染 2025年10月5日-2025年10月8日 中度，非SAE，采取药物治疗措施，对试验, bbox=[166, 573, 851, 590]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[22]: text=药物采取措施：剂量不变，与试验药物无关，未因该AE退出研究。, bbox=[166, 593, 656, 609]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[23]: text=病历更正：, bbox=[166, 622, 244, 638]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[24]: text=1、更正2024年10月22日病历，合并用药“辛芩颗粒”为“辛芩颗粒”；, bbox=[166, 651, 693, 668]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[25]: text=2、更正2024年10月22日病历，合并用药“苯环喹溴铵鼻喷雾剂”为“苯环喹溴铵鼻喷雾, bbox=[166, 679, 812, 696]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[26]: text=剂”；, bbox=[166, 698, 210, 714]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[27]: text=3、更正2026年1月24日病历，“无收到ePro触发的哮喘警报邮件”为“有收到ePro触发的哮, bbox=[166, 726, 831, 743]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[28]: text=喘警报邮件”；, bbox=[166, 745, 277, 761]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[29]: text=4、更正2025年7月18日病历，“受试者漏填2025年4月28日晚间日志” 更正为：“受试者, bbox=[166, 772, 817, 789]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[30]: text=漏填2025年4月28日早间日志”；, bbox=[166, 790, 402, 806]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[31]: text=5、更正2024年11月6日病历，“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共, bbox=[166, 817, 819, 834]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[32]: text=计用了26喷”为：“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了28, bbox=[166, 835, 802, 852]
2026-08-06 02:18:44,546 INFO     29 [qwen-vl-text] coord item[33]: text=喷”。, bbox=[166, 853, 213, 867]
2026-08-06 02:18:44,547 INFO     29 [qwen-vl-text] page=2 — 34/34 coords, api_time=15.2s
2026-08-06 02:18:44,547 INFO     29 [qwen-vl-text] new_positions (34):
[[2, 101.14999999999999, 129.71, 82.51599999999999, 96.83], [2, 101.14999999999999, 129.71, 110.30199999999999, 124.616], [2, 101.14999999999999, 111.265, 138.93, 152.402], [2, 384.965, 422.45, 138.93, 152.402], [2, 101.14999999999999, 129.71, 165.03199999999998, 179.346], [2, 366.52, 487.30499999999995, 165.874, 178.504], [2, 98.77, 254.66, 191.976, 207.132], [2, 98.77, 214.795, 217.236, 232.392], [2, 305.235, 383.18, 217.236, 232.392], [2, 102.935, 124.94999999999999, 236.602, 250.916], [2, 159.45999999999998, 518.84, 236.602, 250.916], [2, 98.77, 522.41, 254.284, 268.598], [2, 98.77, 521.8149999999999, 271.966, 286.28], [2, 98.77, 514.675, 289.64799999999997, 303.962], [2, 98.77, 211.225, 307.33, 320.80199999999996], [2, 98.77, 166.6, 332.59, 346.062], [2, 98.77, 479.57, 357.84999999999997, 372.164], [2, 98.77, 456.96, 383.11, 397.424], [2, 98.77, 486.71, 407.52799999999996, 421.842], [2, 98.77, 427.21, 432.788, 446.26], [2, 98.77, 114.24, 458.89, 469.83599999999996], [2, 98.77, 506.34499999999997, 482.466, 496.78], [2, 98.77, 390.32, 499.306, 512.778], [2, 98.77, 145.18, 523.7239999999999, 537.196], [2, 98.77, 412.335, 548.1419999999999, 562.456], [2, 98.77, 483.14, 571.718, 586.0319999999999], [2, 98.77, 124.94999999999999, 587.716, 601.188], [2, 98.77, 494.445, 611.292, 625.606], [2, 98.77, 164.815, 627.29, 640.762], [2, 98.77, 486.11499999999995, 650.024, 664.338], [2, 98.77, 239.19, 665.18, 678.6519999999999], [2, 98.77, 487.30499999999995, 687.914, 702.228], [2, 98.77, 477.19, 703.0699999999999, 717.384], [2, 98.77, 126.735, 718.226, 730.014]]
2026-08-06 02:18:44,547 INFO     29 [qwen-vl-text] ═══ DONE ═══ 34 positions, pages=1, time=20.4s
2026-08-06 02:18:44,547 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 02:18:44,548 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-06 02:18:44,548 INFO     29 [qwen-vl-text] positions(25): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 02:18:44,548 INFO     29 [qwen-vl-text] page grouping: [3], lines per page: [25]
2026-08-06 02:18:44,765 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-06 02:18:44,765 INFO     29 [qwen-vl-text] LLM extraction start, text_len=766
2026-08-06 02:18:44,765 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-06 02:18:44,766 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 95, \"bbox_end\": 119, \"encounter_dates\": [\"2025-11-17\"], \"department\": \"内科门诊（荔湾）\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "病历编号：\n姓名：\n性别：\n年龄：40岁\n就诊科：\n就诊时间：2025-11-17 10:10:48\n主诉：支气管哮喘治疗后复查：\n现病史：2021年2月前开始出现咳嗽、咯痰，粘白，量中，能咯出，咳嗽呈阵发性、刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏。无咽痛，无伴反酸、嗳气、腹胀。无上腹部隐痛不适感，无伴发热、畏寒，影响睡眠。晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：\n12.52*109/L 嗜酸粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定。本次门诊距上次门诊间隔时间30天。症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确。急性发作情况：两次，就诊期间急性发作：无，发作次数：0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。近3天来出现咽痛不适\n既往史：鼻炎病史无规则治疗。打鼾明显。\n过敏史：未发现。\n个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。\n体格检查：神志清，颈软，双肺呼吸音粗，未闻及明显干、湿性罗音，口腔粘膜无白斑。\n专科情况：\n辅助检查：\n治疗项目：\n门诊诊断：\n1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、阻塞性睡眠呼吸暂停低通气综合征,4、急性咽炎\n单病种：\n发病时间：\n处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不适随诊。\n1金银花口服液◆⑤ 2盒 20.0ml,口服,一天3次(口服) 6天\n2氨卓斯汀氟替卡松鼻喷雾剂◆ 1瓶 2.0喷,喷鼻,一天2次 30天\n3苯环喹溴铵鼻喷雾剂◆ 3瓶 2.0喷,喷鼻,一天4次 30天\n备注：建议在住地附近社区医疗机构随诊。",
    "role": "user"
  }
]
[92m02:18:44 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:18:44,767 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:18:50,473 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-06 02:18:50,473 INFO     29 [qwen-vl-text] LLM output (len=735):
{
  "encounter_date": "2025-11-17",
  "chief_complaint": "支气管哮喘治疗后复查",
  "present_illness": "2021年2月前开始出现咳嗽、咯痰，粘白，量中，能咯出，咳嗽呈阵发性、刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏。无咽痛，无伴反酸、嗳气、腹胀。无上腹部隐痛不适感，无伴发热、畏寒，影响睡眠。晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定。本次门诊距上次门诊间隔时间30天。症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确。急性发作情况：两次，就诊期间急性发作：无，发作次数：0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。近3天来出现咽痛不适",
  "past_history": "鼻炎病史无规则治疗。打鼾明显。过敏史：未发现。个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。",
  "diagnosis": "1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、阻塞性睡眠呼吸暂停低通气综合征,4、急性咽炎",
  "treatment_plan": [
    "金银花口服液 2盒 20.0ml 口服 一天3次 6天",
    "氨卓斯汀氟替卡松鼻喷雾剂 1瓶 2.0喷 喷鼻 一天2次 30天",
    "苯环喹溴铵鼻喷雾剂 3瓶 2.0喷 喷鼻 一天4次 30天"
  ]
}
2026-08-06 02:18:50,473 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-17]
2026-08-06 02:18:50,475 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1159920, prompt_len=1454
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["病历编号：", "姓名：", "性别：", "年龄：40岁", "就诊科：", "就诊时间：2025-11-17 10:10:48", "主诉：支气管哮喘治疗后复查：", "现病史：2021年2月前开始出现咳嗽、咯痰，粘白，量中，能咯出，咳嗽呈阵发性、刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏。无咽痛，无伴反酸、嗳气、腹胀。无上腹部隐痛不适感，无伴发热、畏寒，影响睡眠。晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：", "12.52*109/L 嗜酸粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定。本次门诊距上次门诊间隔时间30天。症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确。急性发作情况：两次，就诊期间急性发作：无，发作次数：0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。近3天来出现咽痛不适", "既往史：鼻炎病史无规则治疗。打鼾明显。", "过敏史：未发现。", "个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。", "体格检查：神志清，颈软，双肺呼吸音粗，未闻及明显干、湿性罗音，口腔粘膜无白斑。", "专科情况：", "辅助检查：", "治疗项目：", "门诊诊断：", "1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、阻塞性睡眠呼吸暂停低通气综合征,4、急性咽炎", "单病种：", "发病时间：", "处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不适随诊。", "1金银花口服液◆⑤ 2盒 20.0ml,口服,一天3次(口服) 6天", "2氨卓斯汀氟替卡松鼻喷雾剂◆ 1瓶 2.0喷,喷鼻,一天2次 30天", "3苯环喹溴铵鼻喷雾剂◆ 3瓶 2.0喷,喷鼻,一天4次 30天", "备注：建议在住地附近社区医疗机构随诊。"]

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
2026-08-06 02:19:00,742 INFO     29 [qwen-vl-text] coord API raw response (len=1869):
[
	{"text": "病历编号：", "bbox": [545, 130, 600, 144]},
	{"text": "姓名：", "bbox": [177, 130, 225, 144]},
	{"text": "性别：", "bbox": [177, 160, 192, 174]},
	{"text": "年龄：40岁", "bbox": [608, 160, 665, 174]},
	{"text": "就诊科：", "bbox": [177, 189, 228, 204]},
	{"text": "就诊时间：2025-11-17 10:10:48", "bbox": [545, 189, 763, 203]},
	{"text": "主诉：支气管哮喘治疗后复查：", "bbox": [175, 218, 466, 234]},
	{"text": "现病史：2021年2月前开始出现咳嗽、咯痰，粘白，量中，能咯出，咳嗽呈阵发性、刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏。无咽痛，无伴反酸、嗳气、腹胀。无上腹部隐痛不适感，无伴发热、畏寒，影响睡眠。晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：", "bbox": [175, 247, 821, 263]},
	{"text": "12.52*109/L 嗜酸粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定。本次门诊距上次门诊间隔时间30天。症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确。急性发作情况：两次，就诊期间急性发作：无，发作次数：0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。近3天来出现咽痛不适", "bbox": [175, 323, 813, 412]},
	{"text": "既往史：鼻炎病史无规则治疗。打鼾明显。", "bbox": [175, 425, 508, 440]},
	{"text": "过敏史：未发现。", "bbox": [175, 453, 335, 468]},
	{"text": "个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。", "bbox": [175, 480, 800, 496]},
	{"text": "体格检查：神志清，颈软，双肺呼吸音粗，未闻及明显干、湿性罗音，口腔粘膜无白斑。", "bbox": [177, 524, 780, 538]},
	{"text": "专科情况：", "bbox": [177, 551, 254, 565]},
	{"text": "辅助检查：", "bbox": [177, 577, 254, 591]},
	{"text": "治疗项目：", "bbox": [177, 604, 254, 618]},
	{"text": "门诊诊断：", "bbox": [177, 630, 254, 644]},
	{"text": "1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、阻塞性睡眠呼吸暂停低通气综合征,4、急性咽炎", "bbox": [193, 657, 770, 687]},
	{"text": "单病种：", "bbox": [177, 700, 269, 713]},
	{"text": "发病时间：", "bbox": [177, 724, 254, 738]},
	{"text": "处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不适随诊。", "bbox": [260, 750, 675, 763]},
	{"text": "1金银花口服液◆⑤ 2盒 20.0ml,口服,一天3次(口服) 6天", "bbox": [198, 774, 716, 788]},
	{"text": "2氨卓斯汀氟替卡松鼻喷雾剂◆ 1瓶 2.0喷,喷鼻,一天2次 30天", "bbox": [198, 800, 672, 813]},
	{"text": "3苯环喹溴铵鼻喷雾剂◆ 3瓶 2.0喷,喷鼻,一天4次 30天", "bbox": [198, 825, 670, 838]},
	{"text": "备注：建议在住地附近社区医疗机构随诊。", "bbox": [260, 848, 521, 861]}
]
2026-08-06 02:19:00,742 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=10.3s
2026-08-06 02:19:00,742 INFO     29 [qwen-vl-text] coord item[0]: text=病历编号：, bbox=[545, 130, 600, 144]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[177, 130, 225, 144]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[2]: text=性别：, bbox=[177, 160, 192, 174]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：40岁, bbox=[608, 160, 665, 174]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[4]: text=就诊科：, bbox=[177, 189, 228, 204]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[5]: text=就诊时间：2025-11-17 10:10:48, bbox=[545, 189, 763, 203]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[6]: text=主诉：支气管哮喘治疗后复查：, bbox=[175, 218, 466, 234]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[7]: text=现病史：2021年2月前开始出现咳嗽、咯痰，粘白，量中，能咯出，咳嗽呈阵发性、刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏。无咽痛，无伴反酸、嗳气、腹胀。无上腹部隐痛不适感，无伴发热、畏寒，影响睡眠。晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：, bbox=[175, 247, 821, 263]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[8]: text=12.52*109/L 嗜酸粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定。本次门诊距上次门诊间隔时间30天。症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确。急性发作情况：两次，就诊期间急性发作：无，发作次数：0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。近3天来出现咽痛不适, bbox=[175, 323, 813, 412]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[9]: text=既往史：鼻炎病史无规则治疗。打鼾明显。, bbox=[175, 425, 508, 440]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[10]: text=过敏史：未发现。, bbox=[175, 453, 335, 468]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[11]: text=个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。, bbox=[175, 480, 800, 496]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[12]: text=体格检查：神志清，颈软，双肺呼吸音粗，未闻及明显干、湿性罗音，口腔粘膜无白斑。, bbox=[177, 524, 780, 538]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[13]: text=专科情况：, bbox=[177, 551, 254, 565]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[14]: text=辅助检查：, bbox=[177, 577, 254, 591]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[15]: text=治疗项目：, bbox=[177, 604, 254, 618]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[16]: text=门诊诊断：, bbox=[177, 630, 254, 644]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[17]: text=1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、阻塞性睡眠呼吸暂停低通气综合征,4、急性咽炎, bbox=[193, 657, 770, 687]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[18]: text=单病种：, bbox=[177, 700, 269, 713]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[19]: text=发病时间：, bbox=[177, 724, 254, 738]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[20]: text=处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不适随诊。, bbox=[260, 750, 675, 763]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[21]: text=1金银花口服液◆⑤ 2盒 20.0ml,口服,一天3次(口服) 6天, bbox=[198, 774, 716, 788]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[22]: text=2氨卓斯汀氟替卡松鼻喷雾剂◆ 1瓶 2.0喷,喷鼻,一天2次 30天, bbox=[198, 800, 672, 813]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[23]: text=3苯环喹溴铵鼻喷雾剂◆ 3瓶 2.0喷,喷鼻,一天4次 30天, bbox=[198, 825, 670, 838]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] coord item[24]: text=备注：建议在住地附近社区医疗机构随诊。, bbox=[260, 848, 521, 861]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] page=3 — 25/25 coords, api_time=10.3s
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] new_positions (25):
[[3, 324.275, 357.0, 109.46, 121.24799999999999], [3, 105.315, 133.875, 109.46, 121.24799999999999], [3, 105.315, 114.24, 134.72, 146.50799999999998], [3, 361.76, 395.67499999999995, 134.72, 146.50799999999998], [3, 105.315, 135.66, 159.138, 171.768], [3, 324.275, 453.98499999999996, 159.138, 170.926], [3, 104.125, 277.27, 183.55599999999998, 197.028], [3, 104.125, 488.495, 207.974, 221.446], [3, 104.125, 483.73499999999996, 271.966, 346.904], [3, 104.125, 302.26, 357.84999999999997, 370.47999999999996], [3, 104.125, 199.325, 381.426, 394.056], [3, 104.125, 476.0, 404.15999999999997, 417.632], [3, 105.315, 464.09999999999997, 441.20799999999997, 452.996], [3, 105.315, 151.13, 463.942, 475.72999999999996], [3, 105.315, 151.13, 485.834, 497.62199999999996], [3, 105.315, 151.13, 508.568, 520.356], [3, 105.315, 151.13, 530.46, 542.2479999999999], [3, 114.835, 458.15, 553.194, 578.454], [3, 105.315, 160.055, 589.4, 600.346], [3, 105.315, 151.13, 609.608, 621.396], [3, 154.7, 401.625, 631.5, 642.446], [3, 117.80999999999999, 426.02, 651.708, 663.496], [3, 117.80999999999999, 399.84, 673.6, 684.5459999999999], [3, 117.80999999999999, 398.65, 694.65, 705.596], [3, 154.7, 309.995, 714.016, 724.962]]
2026-08-06 02:19:00,743 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=16.2s
2026-08-06 02:19:00,743 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 02:19:00,744 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-06 02:19:00,744 INFO     29 [qwen-vl-text] positions(44): [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 02:19:00,744 INFO     29 [qwen-vl-text] page grouping: [13], lines per page: [44]
2026-08-06 02:19:00,925 INFO     29 [qwen-vl-text] page=13, rect=595x842, img=(1653x2339), dpi=200
2026-08-06 02:19:00,925 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1134
2026-08-06 02:19:00,925 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-06 02:19:00,926 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 723, \"bbox_end\": 766, \"encounter_dates\": [\"2026-01-05\"], \"department\": \"内科门诊(荔湾)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "广州医科大学附属第三医院\nThe Third Affiliated Hospital of Guangzhou Medical University\n门(急)诊病历信息\n就诊卡\n流水\n姓\n病历编号:\n年 龄:41岁\n就诊科室:内科门诊(荔湾) 医\n就诊时间:2026-01-05 17:07:54\n主 诉:支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天\n现 病 史:2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激\n性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流\n涕、喷嚏,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响\n睡眠,晨起有咽干,曾到本院就诊两次,症状不见明显缓解。2021-1-9血常规:白细胞:\n12.52*109/L 嗜酸粒细胞:0.65*109/L 5.2%,经治疗后症状明显缓解。无咳嗽、咯痰、气\n促。病情稳定,本次门诊距上次门诊间隔时间30天。症状控制情况:过去4周,患者:吸入\n药物使用情况:遵医嘱使用;吸入装置使用情况:正确。急性发作情况:两次,就诊期间急\n性发作:无,发作次数:0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。长期规律使用信必\n可160/4.5ug 2吸 bid治疗,5天前开始出现咳嗽、咯痰,黄白痰,量少,难以咯出,咳嗽以\n夜间为主。无气促,伴咽息,鼻塞、流涕、喷嚏,无发热。\n既 往 史:鼻炎病史无规则治疗。打鼾明显。\n过 敏 史:未发现;\n个 人 史:否认遗传病史,吸烟10年,20支/日,2018年戒烟。偶饮酒。2021-12-20已打第\n三针新冠疫苗。\n体格检查:神志清,颈软,双肺呼吸音粗,可闻及散在哮鸣音,口腔粘膜无白斑。\n专科情况:\n辅助检查:\n治疗项目:\n门诊诊断:\n1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎\n处 置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。\n布地奈德福莫特罗吸入粉雾剂(II)2盒 2.0吸,吸入用药,一天2次 30天\n(省采)●①⑤\n左氧氟沙星片(省采)●⑥ 5片 0.5g,口服,每日1次(口服) 5天\n第1页\n广州医科大学附属第三医院\nThe Third Affiliated Hospital of Guangzhou Medical University\n门(急)诊病历信息\n复方甲氧那明胶囊(省采)●② 1瓶 1.0粒,餐后口服,一天3次(口服) 5天\n盐酸氨溴索分散片(省采)●⑥ 15片 30.0mg,餐后口服,一天3次(口服) 5\n天\n醋酸泼尼松片●②④ 6片 10.0mg,口服,每早1次(口服) 3天\n备 注:建议在住地附近社区医疗机构随诊。",
    "role": "user"
  }
]
[92m02:19:00 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:19:00,927 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:19:00,928 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T02:19:00.926+00:00", "boot_at": "2026-08-06T01:59:43.412+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"5d401ece913c11f19b5e81513a69a703": {"id": "5d401ece913c11f19b5e81513a69a703", "doc_id": "5963bc44913b11f19b5e81513a69a703", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785982387379, "task_type": "dataflow", "root_trace_id": "7886908ae2584ba69682631c2a66f747", "root_traceparent": "00-7886908ae2584ba69682631c2a66f747-971004a6101741b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 02:19:10,692 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-06 02:19:10,692 INFO     29 [qwen-vl-text] LLM output (len=890):
{
  "encounter_date": "2026-01-05",
  "chief_complaint": "支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天",
  "present_illness": "2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流涕、喷嚏,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响睡眠,晨起有咽干,曾到本院就诊两次,症状不见明显缓解。2021-1-9血常规:白细胞:12.52*109/L 嗜酸粒细胞:0.65*109/L 5.2%,经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定,本次门诊距上次门诊间隔时间30天。症状控制情况:过去4周,患者:吸入药物使用情况:遵医嘱使用;吸入装置使用情况:正确。急性发作情况:两次,就诊期间急性发作:无,发作次数:0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。长期规律使用信必可160/4.5ug 2吸 bid治疗,5天前开始出现咳嗽、咯痰,黄白痰,量少,难以咯出,咳嗽以夜间为主。无气促,伴咽息,鼻塞、流涕、喷嚏,无发热。",
  "past_history": "鼻炎病史无规则治疗。打鼾明显。过敏史:未发现;个人史:否认遗传病史,吸烟10年,20支/日,2018年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。",
  "diagnosis": "1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎",
  "treatment_plan": [
    "布地奈德福莫特罗吸入粉雾剂(II)2盒 2.0吸,吸入用药,一天2次 30天",
    "左氧氟沙星片 5片 0.5g,口服,每日1次 5天",
    "复方甲氧那明胶囊 1瓶 1.0粒,餐后口服,一天3次 5天",
    "盐酸氨溴索分散片 15片 30.0mg,餐后口服,一天3次 5天",
    "醋酸泼尼松片 6片 10.0mg,口服,每早1次 3天"
  ]
}
2026-08-06 02:19:10,692 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-05]
2026-08-06 02:19:10,694 INFO     29 [qwen-vl-text] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1091238, prompt_len=1879
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共44行）
["广州医科大学附属第三医院", "The Third Affiliated Hospital of Guangzhou Medical University", "门(急)诊病历信息", "就诊卡", "流水", "姓", "病历编号:", "年 龄:41岁", "就诊科室:内科门诊(荔湾) 医", "就诊时间:2026-01-05 17:07:54", "主 诉:支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天", "现 病 史:2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激", "性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流", "涕、喷嚏,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响", "睡眠,晨起有咽干,曾到本院就诊两次,症状不见明显缓解。2021-1-9血常规:白细胞:", "12.52*109/L 嗜酸粒细胞:0.65*109/L 5.2%,经治疗后症状明显缓解。无咳嗽、咯痰、气", "促。病情稳定,本次门诊距上次门诊间隔时间30天。症状控制情况:过去4周,患者:吸入", "药物使用情况:遵医嘱使用;吸入装置使用情况:正确。急性发作情况:两次,就诊期间急", "性发作:无,发作次数:0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。长期规律使用信必", "可160/4.5ug 2吸 bid治疗,5天前开始出现咳嗽、咯痰,黄白痰,量少,难以咯出,咳嗽以", "夜间为主。无气促,伴咽息,鼻塞、流涕、喷嚏,无发热。", "既 往 史:鼻炎病史无规则治疗。打鼾明显。", "过 敏 史:未发现;", "个 人 史:否认遗传病史,吸烟10年,20支/日,2018年戒烟。偶饮酒。2021-12-20已打第", "三针新冠疫苗。", "体格检查:神志清,颈软,双肺呼吸音粗,可闻及散在哮鸣音,口腔粘膜无白斑。", "专科情况:", "辅助检查:", "治疗项目:", "门诊诊断:", "1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎", "处 置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。", "布地奈德福莫特罗吸入粉雾剂(II)2盒 2.0吸,吸入用药,一天2次 30天", "(省采)●①⑤", "左氧氟沙星片(省采)●⑥ 5片 0.5g,口服,每日1次(口服) 5天", "第1页", "广州医科大学附属第三医院", "The Third Affiliated Hospital of Guangzhou Medical University", "门(急)诊病历信息", "复方甲氧那明胶囊(省采)●② 1瓶 1.0粒,餐后口服,一天3次(口服) 5天", "盐酸氨溴索分散片(省采)●⑥ 15片 30.0mg,餐后口服,一天3次(口服) 5", "天", "醋酸泼尼松片●②④ 6片 10.0mg,口服,每早1次(口服) 3天", "备 注:建议在住地附近社区医疗机构随诊。"]

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
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord API raw response (len=4455):
[
	{"text": "广州医科大学附属第三医院", "bbox": [98, 250, 252, 263], "bbox_2d": [98, 250, 252, 263]},
	{"text": "The Third Affiliated Hospital of Guangzhou Medical University", "bbox": [98, 261, 252, 268], "bbox_2d": [98, 261, 252, 268]},
	{"text": "门(急)诊病历信息", "bbox": [188, 280, 314, 294], "bbox_2d": [188, 280, 314, 294]},
	{"text": "就诊卡", "bbox": [50, 314, 82, 323], "bbox_2d": [50, 314, 82, 323]},
	{"text": "流水", "bbox": [50, 327, 77, 336], "bbox_2d": [50, 327, 77, 336]},
	{"text": "姓", "bbox": [50, 340, 62, 349], "bbox_2d": [50, 340, 62, 349]},
	{"text": "病历编号:", "bbox": [297, 327, 344, 336], "bbox_2d": [297, 327, 344, 336]},
	{"text": "年 龄:41岁", "bbox": [297, 340, 366, 349], "bbox_2d": [297, 340, 366, 349]},
	{"text": "就诊科室:内科门诊(荔湾) 医", "bbox": [50, 353, 214, 362], "bbox_2d": [50, 353, 214, 362]},
	{"text": "就诊时间:2026-01-05 17:07:54", "bbox": [297, 353, 446, 362], "bbox_2d": [297, 353, 446, 362]},
	{"text": "主 诉:支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天", "bbox": [50, 366, 315, 375], "bbox_2d": [50, 366, 315, 375]},
	{"text": "现 病 史:2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激", "bbox": [50, 379, 461, 388], "bbox_2d": [50, 379, 461, 388]},
	{"text": "性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流", "bbox": [50, 392, 455, 401], "bbox_2d": [50, 392, 455, 401]},
	{"text": "涕、喷嚏,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响", "bbox": [50, 405, 466, 414], "bbox_2d": [50, 405, 466, 414]},
	{"text": "睡眠,晨起有咽干,曾到本院就诊两次,症状不见明显缓解。2021-1-9血常规:白细胞:", "bbox": [50, 418, 451, 427], "bbox_2d": [50, 418, 451, 427]},
	{"text": "12.52*109/L 嗜酸粒细胞:0.65*109/L 5.2%,经治疗后症状明显缓解。无咳嗽、咯痰、气", "bbox": [50, 431, 465, 440], "bbox_2d": [50, 431, 465, 440]},
	{"text": "促。病情稳定,本次门诊距上次门诊间隔时间30天。症状控制情况:过去4周,患者:吸入", "bbox": [50, 444, 464, 453], "bbox_2d": [50, 444, 464, 453]},
	{"text": "药物使用情况:遵医嘱使用;吸入装置使用情况:正确。急性发作情况:两次,就诊期间急", "bbox": [50, 457, 469, 466], "bbox_2d": [50, 457, 469, 466]},
	{"text": "性发作:无,发作次数:0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。长期规律使用信必", "bbox": [50, 470, 465, 479], "bbox_2d": [50, 470, 465, 479]},
	{"text": "可160/4.5ug 2吸 bid治疗,5天前开始出现咳嗽、咯痰,黄白痰,量少,难以咯出,咳嗽以", "bbox": [50, 483, 472, 492], "bbox_2d": [50, 483, 472, 492]},
	{"text": "夜间为主。无气促,伴咽息,鼻塞、流涕、喷嚏,无发热。", "bbox": [50, 496, 319, 505], "bbox_2d": [50, 496, 319, 505]},
	{"text": "既 往 史:鼻炎病史无规则治疗。打鼾明显。", "bbox": [50, 509, 256, 518], "bbox_2d": [50, 509, 256, 518]},
	{"text": "过 敏 史:未发现;", "bbox": [50, 522, 140, 531], "bbox_2d": [50, 522, 140, 531]},
	{"text": "个 人 史:否认遗传病史,吸烟10年,20支/日,2018年戒烟。偶饮酒。2021-12-20已打第", "bbox": [50, 535, 471, 544], "bbox_2d": [50, 535, 471, 544]},
	{"text": "三针新冠疫苗。", "bbox": [50, 548, 118, 557], "bbox_2d": [50, 548, 118, 557]},
	{"text": "体格检查:神志清,颈软,双肺呼吸音粗,可闻及散在哮鸣音,口腔粘膜无白斑。", "bbox": [50, 561, 428, 570], "bbox_2d": [50, 561, 428, 570]},
	{"text": "专科情况:", "bbox": [50, 575, 97, 584], "bbox_2d": [50, 575, 97, 584]},
	{"text": "辅助检查:", "bbox": [50, 588, 97, 597], "bbox_2d": [50, 588, 97, 597]},
	{"text": "治疗项目:", "bbox": [50, 602, 97, 611], "bbox_2d": [50, 602, 97, 611]},
	{"text": "门诊诊断:", "bbox": [50, 616, 97, 625], "bbox_2d": [50, 616, 97, 625]},
	{"text": "1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎", "bbox": [50, 631, 432, 640], "bbox_2d": [50, 631, 432, 640]},
	{"text": "处 置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。", "bbox": [50, 645, 377, 654], "bbox_2d": [50, 645, 377, 654]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(II)2盒 2.0吸,吸入用药,一天2次 30天", "bbox": [109, 660, 458, 669], "bbox_2d": [109, 660, 458, 669]},
	{"text": "(省采)●①⑤", "bbox": [110, 674, 173, 683], "bbox_2d": [110, 674, 173, 683]},
	{"text": "左氧氟沙星片(省采)●⑥ 5片 0.5g,口服,每日1次(口服) 5天", "bbox": [109, 688, 460, 697], "bbox_2d": [109, 688, 460, 697]},
	{"text": "第1页", "bbox": [246, 706, 282, 714], "bbox_2d": [246, 706, 282, 714]},
	{"text": "广州医科大学附属第三医院", "bbox": [558, 245, 720, 258], "bbox_2d": [558, 245, 720, 258]},
	{"text": "The Third Affiliated Hospital of Guangzhou Medical University", "bbox": [558, 256, 720, 263], "bbox_2d": [558, 256, 720, 263]},
	{"text": "门(急)诊病历信息", "bbox": [654, 275, 786, 289], "bbox_2d": [654, 275, 786, 289]},
	{"text": "复方甲氧那明胶囊(省采)●② 1瓶 1.0粒,餐后口服,一天3次(口服) 5天", "bbox": [570, 309, 945, 318], "bbox_2d": [570, 309, 945, 318]},
	{"text": "盐酸氨溴索分散片(省采)●⑥ 15片 30.0mg,餐后口服,一天3次(口服) 5", "bbox": [570, 323, 941, 332], "bbox_2d": [570, 323, 941, 332]},
	{"text": "天", "bbox": [767, 336, 779, 345], "bbox_2d": [767, 336, 779, 345]},
	{"text": "醋酸泼尼松片●②④ 6片 10.0mg,口服,每早1次(口服) 3天", "bbox": [570, 350, 931, 359], "bbox_2d": [570, 350, 931, 359]},
	{"text": "备 注:建议在住地附近社区医疗机构随诊。", "bbox": [512, 363, 732, 372], "bbox_2d": [512, 363, 732, 372]}
]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord API: raw_items=44, valid_items=44, elapsed=23.1s
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[0]: text=广州医科大学附属第三医院, bbox=[98, 250, 252, 263]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[1]: text=The Third Affiliated Hospital of Guangzhou Medical University, bbox=[98, 261, 252, 268]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[2]: text=门(急)诊病历信息, bbox=[188, 280, 314, 294]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[3]: text=就诊卡, bbox=[50, 314, 82, 323]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[4]: text=流水, bbox=[50, 327, 77, 336]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[5]: text=姓, bbox=[50, 340, 62, 349]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[6]: text=病历编号:, bbox=[297, 327, 344, 336]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[7]: text=年 龄:41岁, bbox=[297, 340, 366, 349]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[8]: text=就诊科室:内科门诊(荔湾) 医, bbox=[50, 353, 214, 362]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[9]: text=就诊时间:2026-01-05 17:07:54, bbox=[297, 353, 446, 362]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[10]: text=主 诉:支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天, bbox=[50, 366, 315, 375]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[11]: text=现 病 史:2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激, bbox=[50, 379, 461, 388]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[12]: text=性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流, bbox=[50, 392, 455, 401]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[13]: text=涕、喷嚏,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响, bbox=[50, 405, 466, 414]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[14]: text=睡眠,晨起有咽干,曾到本院就诊两次,症状不见明显缓解。2021-1-9血常规:白细胞:, bbox=[50, 418, 451, 427]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[15]: text=12.52*109/L 嗜酸粒细胞:0.65*109/L 5.2%,经治疗后症状明显缓解。无咳嗽、咯痰、气, bbox=[50, 431, 465, 440]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[16]: text=促。病情稳定,本次门诊距上次门诊间隔时间30天。症状控制情况:过去4周,患者:吸入, bbox=[50, 444, 464, 453]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[17]: text=药物使用情况:遵医嘱使用;吸入装置使用情况:正确。急性发作情况:两次,就诊期间急, bbox=[50, 457, 469, 466]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[18]: text=性发作:无,发作次数:0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。长期规律使用信必, bbox=[50, 470, 465, 479]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[19]: text=可160/4.5ug 2吸 bid治疗,5天前开始出现咳嗽、咯痰,黄白痰,量少,难以咯出,咳嗽以, bbox=[50, 483, 472, 492]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[20]: text=夜间为主。无气促,伴咽息,鼻塞、流涕、喷嚏,无发热。, bbox=[50, 496, 319, 505]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[21]: text=既 往 史:鼻炎病史无规则治疗。打鼾明显。, bbox=[50, 509, 256, 518]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[22]: text=过 敏 史:未发现;, bbox=[50, 522, 140, 531]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[23]: text=个 人 史:否认遗传病史,吸烟10年,20支/日,2018年戒烟。偶饮酒。2021-12-20已打第, bbox=[50, 535, 471, 544]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[24]: text=三针新冠疫苗。, bbox=[50, 548, 118, 557]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[25]: text=体格检查:神志清,颈软,双肺呼吸音粗,可闻及散在哮鸣音,口腔粘膜无白斑。, bbox=[50, 561, 428, 570]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[26]: text=专科情况:, bbox=[50, 575, 97, 584]
2026-08-06 02:19:33,792 INFO     29 [qwen-vl-text] coord item[27]: text=辅助检查:, bbox=[50, 588, 97, 597]
2026-08-06 02:19:33,793 INFO     29 [qwen-vl-text] coord item[28]: text=治疗项目:, bbox=[50, 602, 97, 611]
2026-08-06 02:19:33,793 INFO     29 [qwen-vl-text] coord item[29]: text=门诊诊断:, bbox=[50, 616, 97, 625]
2026-08-06 02:19:33,793 INFO     29 [qwen-vl-text] coord item[30]: text=1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎, bbox=[50, 631, 432, 640]
2026-08-06 02:19:33,793 INFO     29 [qwen-vl-text] coord item[31]: text=处 置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。, bbox=[50, 645, 377, 654]
2026-08-06 02:19:33,793 INFO     29 [qwen-vl-text] coord item[32]: text=布地奈德福莫特罗吸入粉雾剂(II)2盒 2.0吸,吸入用药,一天2次 30天, bbox=[109, 660, 458, 669]
2026-08-06 02:19:33,793 INFO     29 [qwen-vl-text] coord item[33]: text=(省采)●①⑤, bbox=[110, 674, 173, 683]
2026-08-06 02:19:33,793 INFO     29 [qwen-vl-text] coord item[34]: text=左氧氟沙星片(省采)●⑥ 5片 0.5g,口服,每日1次(口服) 5天, bbox=[109, 688, 460, 697]
2026-08-06 02:19:33,793 INFO     29 [qwen-vl-text] coord item[35]: text=第1页, bbox=[246, 706, 282, 714]
2026-08-06 02:19:33,793 INFO     29 [qwen-vl-text] coord item[36]: text=广州医科大学附属第三医院, bbox=[558, 245, 720, 258]
2026-08-06 02:19:33,793 INFO     29 [qwen-vl-text] coord item[37]: text=The Third Affiliated Hospital of Guangzhou Medical University, bbox=[558, 256, 720, 263]
2026-08-06 02:19:33,793 INFO     29 [qwen-vl-text] coord item[38]: text=门(急)诊病历信息, bbox=[654, 275, 786, 289]
2026-08-06 02:19:33,793 INFO     29 [qwen-vl-text] coord item[39]: text=复方甲氧那明胶囊(省采)●② 1瓶 1.0粒,餐后口服,一天3次(口服) 5天, bbox=[570, 309, 945, 318]
2026-08-06 02:19:33,793 INFO     29 [qwen-vl-text] coord item[40]: text=盐酸氨溴索分散片(省采)●⑥ 15片 30.0mg,餐后口服,一天3次(口服) 5, bbox=[570, 323, 941, 332]
2026-08-06 02:19:33,793 INFO     29 [qwen-vl-text] coord item[41]: text=天, bbox=[767, 336, 779, 345]
2026-08-06 02:19:33,793 INFO     29 [qwen-vl-text] coord item[42]: text=醋酸泼尼松片●②④ 6片 10.0mg,口服,每早1次(口服) 3天, bbox=[570, 350, 931, 359]
2026-08-06 02:19:33,793 INFO     29 [qwen-vl-text] coord item[43]: text=备 注:建议在住地附近社区医疗机构随诊。, bbox=[512, 363, 732, 372]
2026-08-06 02:19:33,793 INFO     29 [qwen-vl-text] page=13 — 44/44 coords, api_time=23.1s
2026-08-06 02:19:33,793 INFO     29 [qwen-vl-text] new_positions (44):
[[13, 58.309999999999995, 149.94, 210.5, 221.446], [13, 58.309999999999995, 149.94, 219.762, 225.656], [13, 111.86, 186.82999999999998, 235.76, 247.548], [13, 29.75, 48.79, 264.388, 271.966], [13, 29.75, 45.815, 275.334, 282.912], [13, 29.75, 36.89, 286.28, 293.858], [13, 176.715, 204.67999999999998, 275.334, 282.912], [13, 176.715, 217.76999999999998, 286.28, 293.858], [13, 29.75, 127.33, 297.226, 304.804], [13, 176.715, 265.37, 297.226, 304.804], [13, 29.75, 187.42499999999998, 308.17199999999997, 315.75], [13, 29.75, 274.295, 319.118, 326.69599999999997], [13, 29.75, 270.72499999999997, 330.06399999999996, 337.642], [13, 29.75, 277.27, 341.01, 348.58799999999997], [13, 29.75, 268.34499999999997, 351.95599999999996, 359.534], [13, 29.75, 276.675, 362.902, 370.47999999999996], [13, 29.75, 276.08, 373.848, 381.426], [13, 29.75, 279.055, 384.794, 392.372], [13, 29.75, 276.675, 395.74, 403.318], [13, 29.75, 280.84, 406.686, 414.264], [13, 29.75, 189.80499999999998, 417.632, 425.21], [13, 29.75, 152.32, 428.578, 436.156], [13, 29.75, 83.3, 439.524, 447.102], [13, 29.75, 280.245, 450.46999999999997, 458.048], [13, 29.75, 70.21, 461.416, 468.99399999999997], [13, 29.75, 254.66, 472.36199999999997, 479.94], [13, 29.75, 57.714999999999996, 484.15, 491.728], [13, 29.75, 57.714999999999996, 495.096, 502.674], [13, 29.75, 57.714999999999996, 506.88399999999996, 514.462], [13, 29.75, 57.714999999999996, 518.672, 526.25], [13, 29.75, 257.03999999999996, 531.302, 538.88], [13, 29.75, 224.315, 543.09, 550.668], [13, 64.855, 272.51, 555.72, 563.298], [13, 65.45, 102.935, 567.5079999999999, 575.086], [13, 64.855, 273.7, 579.2959999999999, 586.874], [13, 146.37, 167.79, 594.452, 601.188], [13, 332.01, 428.4, 206.29, 217.236], [13, 332.01, 428.4, 215.552, 221.446], [13, 389.13, 467.66999999999996, 231.54999999999998, 243.338], [13, 339.15, 562.275, 260.178, 267.756], [13, 339.15, 559.895, 271.966, 279.544], [13, 456.36499999999995, 463.505, 282.912, 290.49], [13, 339.15, 553.9449999999999, 294.7, 302.27799999999996], [13, 304.64, 435.53999999999996, 305.646, 313.224]]
2026-08-06 02:19:33,794 INFO     29 [qwen-vl-text] ═══ DONE ═══ 44 positions, pages=1, time=33.0s
2026-08-06 02:19:33,794 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 02:19:33,794 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-06 02:19:33,794 INFO     29 [qwen-vl-text] positions(27): [[14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 02:19:33,794 INFO     29 [qwen-vl-text] page grouping: [14], lines per page: [27]
2026-08-06 02:19:34,029 INFO     29 [qwen-vl-text] page=14, rect=595x842, img=(1653x2339), dpi=200
2026-08-06 02:19:34,029 INFO     29 [qwen-vl-text] LLM extraction start, text_len=719
2026-08-06 02:19:34,030 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-06 02:19:34,030 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 767, \"bbox_end\": 793, \"encounter_dates\": [\"2026-02-04\"], \"department\": \"内科门诊（荔湾）\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊/住院病历信息\n就诊卡号：0\n病历编号：\n姓名：\n性别：男\n年龄：41岁\n就诊科室：内科门诊（荔湾）\n就诊时间：2026-02-04 11:21:11\n主诉：支气管哮喘治疗后复查\n现病史：2021年2月前开始出现咳嗽、哮喘，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sg 2吸 bid治疗。\n既往史：鼻炎病史无规则治疗，打鼾明显。\n过敏史：未发现；\n个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。\n体格检查：神志清，颈软，双肺呼吸音粗，可闻及散在哮鸣音，口腔粘膜无白斑。\n专科情况：\n辅助检查：\n治疗项目：\n门诊诊断：\n1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎\n单病种：\n发病时间：\n处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不遥随诊。\n布地奈德福莫特罗吸入粉雾剂(II)(省\n2 2.0班,吸入用药,一天2次\n30\n采)●①②\n查天",
    "role": "user"
  }
]
[92m02:19:34 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:19:34,031 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:19:34,033 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T02:19:34.031+00:00", "boot_at": "2026-08-06T01:59:43.412+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"5d401ece913c11f19b5e81513a69a703": {"id": "5d401ece913c11f19b5e81513a69a703", "doc_id": "5963bc44913b11f19b5e81513a69a703", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785982387379, "task_type": "dataflow", "root_trace_id": "7886908ae2584ba69682631c2a66f747", "root_traceparent": "00-7886908ae2584ba69682631c2a66f747-971004a6101741b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 02:19:39,322 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-06 02:19:39,322 INFO     29 [qwen-vl-text] LLM output (len=655):
{
  "encounter_date": "2026-02-04",
  "chief_complaint": "支气管哮喘治疗后复查",
  "present_illness": "2021年2月前开始出现咳嗽、哮喘，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sg 2吸 bid治疗。",
  "past_history": "鼻炎病史无规则治疗，打鼾明显。过敏史：未发现；个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。",
  "diagnosis": "1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎",
  "treatment_plan": "布地奈德福莫特罗吸入粉雾剂(II) 2吸 一天2次 吸入用药"
}
2026-08-06 02:19:39,322 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-04]
2026-08-06 02:19:39,325 INFO     29 [qwen-vl-text] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1605519, prompt_len=1413
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共27行）
["门诊/住院病历信息", "就诊卡号：0", "病历编号：", "姓名：", "性别：男", "年龄：41岁", "就诊科室：内科门诊（荔湾）", "就诊时间：2026-02-04 11:21:11", "主诉：支气管哮喘治疗后复查", "现病史：2021年2月前开始出现咳嗽、哮喘，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sg 2吸 bid治疗。", "既往史：鼻炎病史无规则治疗，打鼾明显。", "过敏史：未发现；", "个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。", "体格检查：神志清，颈软，双肺呼吸音粗，可闻及散在哮鸣音，口腔粘膜无白斑。", "专科情况：", "辅助检查：", "治疗项目：", "门诊诊断：", "1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎", "单病种：", "发病时间：", "处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不遥随诊。", "布地奈德福莫特罗吸入粉雾剂(II)(省", "2 2.0班,吸入用药,一天2次", "30", "采)●①②", "查天"]

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
2026-08-06 02:19:52,365 INFO     29 [qwen-vl-text] coord API raw response (len=1910):
[
	{"text": "门诊/住院病历信息", "bbox": [338, 155, 525, 169]},
	{"text": "就诊卡号：0", "bbox": [187, 194, 262, 207]},
	{"text": "病历编号：", "bbox": [509, 220, 577, 233]},
	{"text": "姓名：", "bbox": [187, 246, 202, 259]},
	{"text": "性别：男", "bbox": [431, 246, 475, 259]},
	{"text": "年龄：41岁", "bbox": [585, 246, 639, 259]},
	{"text": "就诊科室：内科门诊（荔湾）", "bbox": [187, 271, 373, 284]},
	{"text": "就诊时间：2026-02-04 11:21:11", "bbox": [517, 271, 732, 284]},
	{"text": "主诉：支气管哮喘治疗后复查", "bbox": [187, 297, 465, 310]},
	{"text": "现病史：2021年2月前开始出现咳嗽、哮喘，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sg 2吸 bid治疗。", "bbox": [187, 323, 774, 466]},
	{"text": "既往史：鼻炎病史无规则治疗，打鼾明显。", "bbox": [187, 477, 507, 490]},
	{"text": "过敏史：未发现；", "bbox": [187, 502, 339, 515]},
	{"text": "个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。", "bbox": [187, 526, 762, 554]},
	{"text": "体格检查：神志清，颈软，双肺呼吸音粗，可闻及散在哮鸣音，口腔粘膜无白斑。", "bbox": [187, 567, 727, 579]},
	{"text": "专科情况：", "bbox": [187, 591, 258, 604]},
	{"text": "辅助检查：", "bbox": [187, 616, 258, 628]},
	{"text": "治疗项目：", "bbox": [187, 640, 258, 652]},
	{"text": "门诊诊断：", "bbox": [187, 664, 258, 676]},
	{"text": "1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎", "bbox": [207, 687, 645, 699]},
	{"text": "单病种：", "bbox": [187, 710, 274, 722]},
	{"text": "发病时间：", "bbox": [187, 733, 258, 745]},
	{"text": "处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不遥随诊。", "bbox": [269, 755, 677, 767]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(II)(省", "bbox": [217, 779, 461, 791]},
	{"text": "2 2.0班,吸入用药,一天2次", "bbox": [519, 779, 703, 791]},
	{"text": "30", "bbox": [732, 779, 746, 789]},
	{"text": "采)●①②", "bbox": [217, 795, 283, 807]},
	{"text": "查天", "bbox": [519, 795, 555, 807]}
]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord API: raw_items=27, valid_items=27, elapsed=13.0s
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[0]: text=门诊/住院病历信息, bbox=[338, 155, 525, 169]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[1]: text=就诊卡号：0, bbox=[187, 194, 262, 207]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[2]: text=病历编号：, bbox=[509, 220, 577, 233]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[187, 246, 202, 259]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[4]: text=性别：男, bbox=[431, 246, 475, 259]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：41岁, bbox=[585, 246, 639, 259]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[6]: text=就诊科室：内科门诊（荔湾）, bbox=[187, 271, 373, 284]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[7]: text=就诊时间：2026-02-04 11:21:11, bbox=[517, 271, 732, 284]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[8]: text=主诉：支气管哮喘治疗后复查, bbox=[187, 297, 465, 310]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[9]: text=现病史：2021年2月前开始出现咳嗽、哮喘，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sg 2吸 bid治疗。, bbox=[187, 323, 774, 466]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[10]: text=既往史：鼻炎病史无规则治疗，打鼾明显。, bbox=[187, 477, 507, 490]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[11]: text=过敏史：未发现；, bbox=[187, 502, 339, 515]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[12]: text=个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。, bbox=[187, 526, 762, 554]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[13]: text=体格检查：神志清，颈软，双肺呼吸音粗，可闻及散在哮鸣音，口腔粘膜无白斑。, bbox=[187, 567, 727, 579]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[14]: text=专科情况：, bbox=[187, 591, 258, 604]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[15]: text=辅助检查：, bbox=[187, 616, 258, 628]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[16]: text=治疗项目：, bbox=[187, 640, 258, 652]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[17]: text=门诊诊断：, bbox=[187, 664, 258, 676]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[18]: text=1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎, bbox=[207, 687, 645, 699]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[19]: text=单病种：, bbox=[187, 710, 274, 722]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[20]: text=发病时间：, bbox=[187, 733, 258, 745]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[21]: text=处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不遥随诊。, bbox=[269, 755, 677, 767]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[22]: text=布地奈德福莫特罗吸入粉雾剂(II)(省, bbox=[217, 779, 461, 791]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[23]: text=2 2.0班,吸入用药,一天2次, bbox=[519, 779, 703, 791]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[24]: text=30, bbox=[732, 779, 746, 789]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[25]: text=采)●①②, bbox=[217, 795, 283, 807]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] coord item[26]: text=查天, bbox=[519, 795, 555, 807]
2026-08-06 02:19:52,366 INFO     29 [qwen-vl-text] page=14 — 27/27 coords, api_time=13.0s
2026-08-06 02:19:52,367 INFO     29 [qwen-vl-text] new_positions (27):
[[14, 201.10999999999999, 312.375, 130.51, 142.298], [14, 111.265, 155.89, 163.34799999999998, 174.29399999999998], [14, 302.85499999999996, 343.315, 185.23999999999998, 196.186], [14, 111.265, 120.19, 207.132, 218.078], [14, 256.445, 282.625, 207.132, 218.078], [14, 348.075, 380.205, 207.132, 218.078], [14, 111.265, 221.935, 228.182, 239.128], [14, 307.615, 435.53999999999996, 228.182, 239.128], [14, 111.265, 276.675, 250.07399999999998, 261.02], [14, 111.265, 460.53, 271.966, 392.372], [14, 111.265, 301.66499999999996, 401.63399999999996, 412.58], [14, 111.265, 201.70499999999998, 422.68399999999997, 433.63], [14, 111.265, 453.39, 442.892, 466.46799999999996], [14, 111.265, 432.565, 477.414, 487.518], [14, 111.265, 153.51, 497.62199999999996, 508.568], [14, 111.265, 153.51, 518.672, 528.776], [14, 111.265, 153.51, 538.88, 548.984], [14, 111.265, 153.51, 559.088, 569.192], [14, 123.16499999999999, 383.775, 578.454, 588.558], [14, 111.265, 163.03, 597.8199999999999, 607.924], [14, 111.265, 153.51, 617.1859999999999, 627.29], [14, 160.055, 402.815, 635.7099999999999, 645.814], [14, 129.11499999999998, 274.295, 655.918, 666.0219999999999], [14, 308.805, 418.28499999999997, 655.918, 666.0219999999999], [14, 435.53999999999996, 443.87, 655.918, 664.338], [14, 129.11499999999998, 168.385, 669.39, 679.494], [14, 308.805, 330.22499999999997, 669.39, 679.494]]
2026-08-06 02:19:52,367 INFO     29 [qwen-vl-text] ═══ DONE ═══ 27 positions, pages=1, time=18.6s
2026-08-06 02:19:52,380 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-06 02:19:52,380 INFO     29 [Trace] task=5d401ece | doc=LZK 哮喘 广三(1).pdf | Extractor:Clinical | outputs={"chunks": "5 items, types={'OutpatientRecord': 5}", "html": "", "json": "3678 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "chunks", "chunks_Clinical": "5 items, types={'OutpatientRecord': 5}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 5, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-06 02:19:52,381 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-06 02:19:52,396 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-06 02:19:52,397 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m02:19:52 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:19:52,399 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:19:53,560 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-06 02:19:53,566 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-06 02:19:53,567 INFO     29 [Trace] task=5d401ece | doc=LZK 哮喘 广三(1).pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "3678 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "chunks", "chunks_Clinical": "5 items, types={'OutpatientRecord': 5}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 5, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-06 02:19:53,567 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-06 02:19:53,576 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 02:19:53,576 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-06 02:19:53,576 INFO     29 [qwen-vl-text] positions(26): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 02:19:53,577 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [26]
2026-08-06 02:19:53,731 INFO     29 [qwen-vl-text] page=4, rect=842x595, img=(2339x1653), dpi=200
2026-08-06 02:19:53,732 INFO     29 [qwen-vl-text] LLM extraction start, text_len=198
2026-08-06 02:19:53,732 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-06 02:19:53,732 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 120, \"bbox_end\": 145, \"encounter_dates\": [\"2025-07-18\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-07-18\n就诊科室:内科门诊\n主诊医\n姓名\n性别:男\n年龄:40岁\n卡号:\n患者\n医疗证号:\n处方号\n地址:PT027气雾剂 2024017-呼吸科\n身份证\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n布地奈德福莫特罗吸入粉雾剂0.125/0.006*60吸6盒\n183.41100.46\nSig\n2吸/次,吸入,bid*90天",
    "role": "user"
  }
]
[92m02:19:53 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:19:53,734 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:19:55,712 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-06 02:19:55,712 INFO     29 [qwen-vl-text] LLM output (len=422):
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
      "dosage": "0.125/0.006",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 90,
      "quantity": "6盒",
      "notes": "2吸/次"
    }
  ]
}
2026-08-06 02:19:55,712 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-07-18]
2026-08-06 02:19:55,714 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=919286, prompt_len=889
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["门(急)诊处方", "就诊时间:2025-07-18", "就诊科室:内科门诊", "主诊医", "姓名", "性别:男", "年龄:40岁", "卡号:", "患者", "医疗证号:", "处方号", "地址:PT027气雾剂 2024017-呼吸科", "身份证", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂0.125/0.006*60吸6盒", "183.41100.46", "Sig", "2吸/次,吸入,bid*90天"]

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
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord API raw response (len=1335):
[
	{"text": "门(急)诊处方", "bbox": [385, 24, 624, 91]},
	{"text": "就诊时间:2025-07-18", "bbox": [38, 117, 284, 150]},
	{"text": "就诊科室:内科门诊", "bbox": [320, 117, 531, 150]},
	{"text": "主诊医", "bbox": [617, 117, 685, 150]},
	{"text": "姓名", "bbox": [38, 170, 85, 203]},
	{"text": "性别:男", "bbox": [320, 170, 407, 203]},
	{"text": "年龄:40岁", "bbox": [457, 170, 567, 203]},
	{"text": "卡号:", "bbox": [617, 170, 678, 203]},
	{"text": "患者", "bbox": [38, 222, 85, 255]},
	{"text": "医疗证号:", "bbox": [320, 222, 426, 255]},
	{"text": "处方号", "bbox": [613, 224, 683, 257]},
	{"text": "地址:PT027气雾剂 2024017-呼吸科", "bbox": [38, 275, 436, 309]},
	{"text": "身份证", "bbox": [612, 275, 682, 309]},
	{"text": "诊断:支气管哮喘", "bbox": [38, 324, 222, 358]},
	{"text": "西药处方", "bbox": [434, 383, 564, 416]},
	{"text": "组号", "bbox": [107, 444, 156, 477]},
	{"text": "项目名称", "bbox": [215, 444, 314, 477]},
	{"text": "规格", "bbox": [506, 444, 550, 477]},
	{"text": "总量", "bbox": [709, 444, 755, 477]},
	{"text": "单价", "bbox": [812, 444, 858, 477]},
	{"text": "金额", "bbox": [893, 444, 938, 477]},
	{"text": "R:", "bbox": [60, 504, 108, 554]},
	{"text": "布地奈德福莫特罗吸入粉雾剂0.125/0.006*60吸6盒", "bbox": [195, 498, 737, 531]},
	{"text": "183.41100.46", "bbox": [767, 500, 923, 528]},
	{"text": "Sig", "bbox": [424, 550, 461, 580]},
	{"text": "2吸/次,吸入,bid*90天", "bbox": [504, 548, 747, 580]}
]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=7.2s
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[385, 24, 624, 91]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-07-18, bbox=[38, 117, 284, 150]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[320, 117, 531, 150]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[3]: text=主诊医, bbox=[617, 117, 685, 150]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[38, 170, 85, 203]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[320, 170, 407, 203]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:40岁, bbox=[457, 170, 567, 203]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[7]: text=卡号:, bbox=[617, 170, 678, 203]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[8]: text=患者, bbox=[38, 222, 85, 255]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[320, 222, 426, 255]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[10]: text=处方号, bbox=[613, 224, 683, 257]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[11]: text=地址:PT027气雾剂 2024017-呼吸科, bbox=[38, 275, 436, 309]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[12]: text=身份证, bbox=[612, 275, 682, 309]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[38, 324, 222, 358]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[434, 383, 564, 416]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[107, 444, 156, 477]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[215, 444, 314, 477]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[506, 444, 550, 477]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[709, 444, 755, 477]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[812, 444, 858, 477]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[893, 444, 938, 477]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[60, 504, 108, 554]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[22]: text=布地奈德福莫特罗吸入粉雾剂0.125/0.006*60吸6盒, bbox=[195, 498, 737, 531]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[23]: text=183.41100.46, bbox=[767, 500, 923, 528]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[424, 550, 461, 580]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] coord item[25]: text=2吸/次,吸入,bid*90天, bbox=[504, 548, 747, 580]
2026-08-06 02:20:02,877 INFO     29 [qwen-vl-text] page=4 — 26/26 coords, api_time=7.2s
2026-08-06 02:20:02,878 INFO     29 [qwen-vl-text] new_positions (26):
[[4, 324.17, 525.408, 14.28, 54.144999999999996], [4, 31.996, 239.128, 69.615, 89.25], [4, 269.44, 447.102, 69.615, 89.25], [4, 519.514, 576.77, 69.615, 89.25], [4, 31.996, 71.57, 101.14999999999999, 120.785], [4, 269.44, 342.69399999999996, 101.14999999999999, 120.785], [4, 384.794, 477.414, 101.14999999999999, 120.785], [4, 519.514, 570.876, 101.14999999999999, 120.785], [4, 31.996, 71.57, 132.09, 151.725], [4, 269.44, 358.692, 132.09, 151.725], [4, 516.146, 575.086, 133.28, 152.915], [4, 31.996, 367.11199999999997, 163.625, 183.855], [4, 515.304, 574.244, 163.625, 183.855], [4, 31.996, 186.924, 192.78, 213.01], [4, 365.428, 474.888, 227.885, 247.51999999999998], [4, 90.094, 131.352, 264.18, 283.815], [4, 181.03, 264.388, 264.18, 283.815], [4, 426.05199999999996, 463.09999999999997, 264.18, 283.815], [4, 596.978, 635.7099999999999, 264.18, 283.815], [4, 683.704, 722.4359999999999, 264.18, 283.815], [4, 751.906, 789.7959999999999, 264.18, 283.815], [4, 50.519999999999996, 90.93599999999999, 299.88, 329.63], [4, 164.19, 620.554, 296.31, 315.945], [4, 645.814, 777.1659999999999, 297.5, 314.15999999999997], [4, 357.008, 388.162, 327.25, 345.09999999999997], [4, 424.368, 628.9739999999999, 326.06, 345.09999999999997]]
2026-08-06 02:20:02,878 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=9.3s
2026-08-06 02:20:02,878 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 02:20:02,878 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-06 02:20:02,878 INFO     29 [qwen-vl-text] positions(26): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 02:20:02,878 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [26]
2026-08-06 02:20:03,034 INFO     29 [qwen-vl-text] page=5, rect=842x595, img=(2339x1653), dpi=200
2026-08-06 02:20:03,035 INFO     29 [qwen-vl-text] LLM extraction start, text_len=205
2026-08-06 02:20:03,035 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-06 02:20:03,035 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 146, \"bbox_end\": 171, \"encounter_dates\": [\"2025-04-25\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-04-25\n就诊科室:内科门诊\n主诊\n姓名\n性别:男\n年龄:40岁\n卡号:\n患者类型:GLP支付\n医疗证号:\n处方号\n地址:PT027气雾剂 2024017-呼吸科\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n布地奈德福莫特罗吸入粉雾剂(II)●●@ug*60吸6盒\n183.41100.46\nSig\n2吸/次,吸入,bid*90天",
    "role": "user"
  }
]
[92m02:20:03 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:20:03,037 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:20:05,371 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-06 02:20:05,371 INFO     29 [qwen-vl-text] LLM output (len=417):
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
2026-08-06 02:20:05,371 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-04-25]
2026-08-06 02:20:05,372 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=892488, prompt_len=896
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
2026-08-06 02:20:13,942 INFO     29 [qwen-vl-text] coord API raw response (len=1343):
[
	{"text": "门(急)诊处方", "bbox": [375, 20, 604, 88]},
	{"text": "就诊时间:2025-04-25", "bbox": [48, 117, 283, 153]},
	{"text": "就诊科室:内科门诊", "bbox": [317, 114, 518, 150]},
	{"text": "主诊", "bbox": [601, 114, 661, 150]},
	{"text": "姓名", "bbox": [48, 172, 97, 207]},
	{"text": "性别:男", "bbox": [317, 170, 401, 206]},
	{"text": "年龄:40岁", "bbox": [448, 170, 555, 206]},
	{"text": "卡号:", "bbox": [601, 170, 655, 206]},
	{"text": "患者类型:GLP支付", "bbox": [50, 228, 245, 262]},
	{"text": "医疗证号:", "bbox": [318, 227, 421, 262]},
	{"text": "处方号", "bbox": [601, 227, 661, 262]},
	{"text": "地址:PT027气雾剂 2024017-呼吸科", "bbox": [50, 280, 432, 317]},
	{"text": "身份证号:", "bbox": [601, 280, 704, 316]},
	{"text": "诊断:支气管哮喘", "bbox": [51, 333, 229, 369]},
	{"text": "西药处方", "bbox": [431, 393, 559, 428]},
	{"text": "组号", "bbox": [119, 458, 167, 493]},
	{"text": "项目名称", "bbox": [223, 458, 317, 493]},
	{"text": "规格", "bbox": [503, 458, 546, 491]},
	{"text": "总量", "bbox": [702, 458, 748, 491]},
	{"text": "单价", "bbox": [805, 456, 851, 491]},
	{"text": "金额", "bbox": [886, 456, 933, 491]},
	{"text": "R:", "bbox": [74, 522, 120, 575]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(II)●●@ug*60吸6盒", "bbox": [204, 517, 731, 553]},
	{"text": "183.41100.46", "bbox": [760, 517, 919, 548]},
	{"text": "Sig", "bbox": [424, 571, 462, 604]},
	{"text": "2吸/次,吸入,bid*90天", "bbox": [503, 568, 743, 604]}
]
2026-08-06 02:20:13,942 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=8.6s
2026-08-06 02:20:13,942 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[375, 20, 604, 88]
2026-08-06 02:20:13,942 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-04-25, bbox=[48, 117, 283, 153]
2026-08-06 02:20:13,942 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[317, 114, 518, 150]
2026-08-06 02:20:13,942 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[601, 114, 661, 150]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[48, 172, 97, 207]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[317, 170, 401, 206]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:40岁, bbox=[448, 170, 555, 206]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[7]: text=卡号:, bbox=[601, 170, 655, 206]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[8]: text=患者类型:GLP支付, bbox=[50, 228, 245, 262]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[318, 227, 421, 262]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[10]: text=处方号, bbox=[601, 227, 661, 262]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[11]: text=地址:PT027气雾剂 2024017-呼吸科, bbox=[50, 280, 432, 317]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[601, 280, 704, 316]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[51, 333, 229, 369]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[431, 393, 559, 428]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[119, 458, 167, 493]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[223, 458, 317, 493]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[503, 458, 546, 491]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[702, 458, 748, 491]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[805, 456, 851, 491]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[886, 456, 933, 491]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[74, 522, 120, 575]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[22]: text=布地奈德福莫特罗吸入粉雾剂(II)●●@ug*60吸6盒, bbox=[204, 517, 731, 553]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[23]: text=183.41100.46, bbox=[760, 517, 919, 548]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[424, 571, 462, 604]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] coord item[25]: text=2吸/次,吸入,bid*90天, bbox=[503, 568, 743, 604]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] page=5 — 26/26 coords, api_time=8.6s
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] new_positions (26):
[[5, 315.75, 508.568, 11.899999999999999, 52.36], [5, 40.416, 238.286, 69.615, 91.035], [5, 266.914, 436.156, 67.83, 89.25], [5, 506.042, 556.562, 67.83, 89.25], [5, 40.416, 81.67399999999999, 102.33999999999999, 123.16499999999999], [5, 266.914, 337.642, 101.14999999999999, 122.57], [5, 377.216, 467.31, 101.14999999999999, 122.57], [5, 506.042, 551.51, 101.14999999999999, 122.57], [5, 42.1, 206.29, 135.66, 155.89], [5, 267.756, 354.48199999999997, 135.065, 155.89], [5, 506.042, 556.562, 135.065, 155.89], [5, 42.1, 363.74399999999997, 166.6, 188.61499999999998], [5, 506.042, 592.768, 166.6, 188.01999999999998], [5, 42.942, 192.81799999999998, 198.135, 219.55499999999998], [5, 362.902, 470.678, 233.83499999999998, 254.66], [5, 100.198, 140.614, 272.51, 293.335], [5, 187.766, 266.914, 272.51, 293.335], [5, 423.526, 459.73199999999997, 272.51, 292.145], [5, 591.084, 629.816, 272.51, 292.145], [5, 677.81, 716.542, 271.32, 292.145], [5, 746.012, 785.586, 271.32, 292.145], [5, 62.308, 101.03999999999999, 310.59, 342.125], [5, 171.768, 615.502, 307.615, 329.03499999999997], [5, 639.92, 773.798, 307.615, 326.06], [5, 357.008, 389.00399999999996, 339.745, 359.38], [5, 423.526, 625.606, 337.96, 359.38]]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=11.1s
2026-08-06 02:20:13,943 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] positions(25): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 02:20:13,943 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [25]
2026-08-06 02:20:14,098 INFO     29 [qwen-vl-text] page=6, rect=842x595, img=(2339x1653), dpi=200
2026-08-06 02:20:14,099 INFO     29 [qwen-vl-text] LLM extraction start, text_len=196
2026-08-06 02:20:14,099 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-06 02:20:14,099 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 172, \"bbox_end\": 196, \"encounter_dates\": [\"2025-02-26\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-02-26\n就诊科室:内科门诊\n主诊\n性别:男\n年龄:40岁\n卡号\n医疗证号:\n处方\n015\n地址:PT027气雾剂 2024017-呼吸科\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n布地奈德福莫特罗吸入粉雾剂BDII/●@0.1g*60吸2盒\n183.41 366.82\nSig\n2吸/次,吸入,bid*30天",
    "role": "user"
  }
]
[92m02:20:14 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:20:14,100 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:20:14,101 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T02:20:14.100+00:00", "boot_at": "2026-08-06T01:59:43.412+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"5d401ece913c11f19b5e81513a69a703": {"id": "5d401ece913c11f19b5e81513a69a703", "doc_id": "5963bc44913b11f19b5e81513a69a703", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785982387379, "task_type": "dataflow", "root_trace_id": "7886908ae2584ba69682631c2a66f747", "root_traceparent": "00-7886908ae2584ba69682631c2a66f747-971004a6101741b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 02:20:17,824 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-06 02:20:17,825 INFO     29 [qwen-vl-text] LLM output (len=419):
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
      "dosage": "0.1g*60吸",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 30,
      "quantity": "2盒",
      "notes": "2吸/次"
    }
  ]
}
2026-08-06 02:20:17,825 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-02-26]
2026-08-06 02:20:17,826 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=825853, prompt_len=884
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["门(急)诊处方", "就诊时间:2025-02-26", "就诊科室:内科门诊", "主诊", "性别:男", "年龄:40岁", "卡号", "医疗证号:", "处方", "015", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂BDII/●@0.1g*60吸2盒", "183.41 366.82", "Sig", "2吸/次,吸入,bid*30天"]

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
2026-08-06 02:20:25,094 INFO     29 [qwen-vl-text] coord API raw response (len=1293):
[
	{"text": "门(急)诊处方", "bbox": [394, 28, 630, 94]},
	{"text": "就诊时间:2025-02-26", "bbox": [54, 123, 294, 153]},
	{"text": "就诊科室:内科门诊", "bbox": [330, 120, 536, 155]},
	{"text": "主诊", "bbox": [623, 122, 667, 155]},
	{"text": "性别:男", "bbox": [330, 175, 415, 209]},
	{"text": "年龄:40岁", "bbox": [464, 175, 573, 209]},
	{"text": "卡号", "bbox": [621, 175, 667, 209]},
	{"text": "医疗证号:", "bbox": [330, 230, 435, 264]},
	{"text": "处方", "bbox": [619, 230, 667, 264]},
	{"text": "015", "bbox": [900, 228, 939, 258]},
	{"text": "地址:PT027气雾剂 2024017-呼吸科", "bbox": [54, 281, 444, 316]},
	{"text": "身份证号:", "bbox": [618, 281, 720, 316]},
	{"text": "诊断:支气管哮喘", "bbox": [55, 331, 234, 365]},
	{"text": "西药处方", "bbox": [442, 390, 571, 423]},
	{"text": "组号", "bbox": [120, 452, 169, 485]},
	{"text": "项目名称", "bbox": [227, 452, 324, 485]},
	{"text": "规格", "bbox": [514, 452, 557, 483]},
	{"text": "总量", "bbox": [716, 452, 762, 483]},
	{"text": "单价", "bbox": [820, 452, 866, 483]},
	{"text": "金额", "bbox": [902, 450, 948, 483]},
	{"text": "R:", "bbox": [75, 513, 121, 565]},
	{"text": "布地奈德福莫特罗吸入粉雾剂BDII/●@0.1g*60吸2盒", "bbox": [206, 507, 744, 540]},
	{"text": "183.41 366.82", "bbox": [775, 508, 932, 536]},
	{"text": "Sig", "bbox": [432, 558, 469, 588]},
	{"text": "2吸/次,吸入,bid*30天", "bbox": [511, 557, 754, 588]}
]
2026-08-06 02:20:25,094 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=7.3s
2026-08-06 02:20:25,095 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[394, 28, 630, 94]
2026-08-06 02:20:25,095 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-02-26, bbox=[54, 123, 294, 153]
2026-08-06 02:20:25,095 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[330, 120, 536, 155]
2026-08-06 02:20:25,095 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[623, 122, 667, 155]
2026-08-06 02:20:25,095 INFO     29 [qwen-vl-text] coord item[4]: text=性别:男, bbox=[330, 175, 415, 209]
2026-08-06 02:20:25,095 INFO     29 [qwen-vl-text] coord item[5]: text=年龄:40岁, bbox=[464, 175, 573, 209]
2026-08-06 02:20:25,095 INFO     29 [qwen-vl-text] coord item[6]: text=卡号, bbox=[621, 175, 667, 209]
2026-08-06 02:20:25,095 INFO     29 [qwen-vl-text] coord item[7]: text=医疗证号:, bbox=[330, 230, 435, 264]
2026-08-06 02:20:25,095 INFO     29 [qwen-vl-text] coord item[8]: text=处方, bbox=[619, 230, 667, 264]
2026-08-06 02:20:25,095 INFO     29 [qwen-vl-text] coord item[9]: text=015, bbox=[900, 228, 939, 258]
2026-08-06 02:20:25,096 INFO     29 [qwen-vl-text] coord item[10]: text=地址:PT027气雾剂 2024017-呼吸科, bbox=[54, 281, 444, 316]
2026-08-06 02:20:25,096 INFO     29 [qwen-vl-text] coord item[11]: text=身份证号:, bbox=[618, 281, 720, 316]
2026-08-06 02:20:25,096 INFO     29 [qwen-vl-text] coord item[12]: text=诊断:支气管哮喘, bbox=[55, 331, 234, 365]
2026-08-06 02:20:25,096 INFO     29 [qwen-vl-text] coord item[13]: text=西药处方, bbox=[442, 390, 571, 423]
2026-08-06 02:20:25,096 INFO     29 [qwen-vl-text] coord item[14]: text=组号, bbox=[120, 452, 169, 485]
2026-08-06 02:20:25,096 INFO     29 [qwen-vl-text] coord item[15]: text=项目名称, bbox=[227, 452, 324, 485]
2026-08-06 02:20:25,096 INFO     29 [qwen-vl-text] coord item[16]: text=规格, bbox=[514, 452, 557, 483]
2026-08-06 02:20:25,096 INFO     29 [qwen-vl-text] coord item[17]: text=总量, bbox=[716, 452, 762, 483]
2026-08-06 02:20:25,096 INFO     29 [qwen-vl-text] coord item[18]: text=单价, bbox=[820, 452, 866, 483]
2026-08-06 02:20:25,096 INFO     29 [qwen-vl-text] coord item[19]: text=金额, bbox=[902, 450, 948, 483]
2026-08-06 02:20:25,097 INFO     29 [qwen-vl-text] coord item[20]: text=R:, bbox=[75, 513, 121, 565]
2026-08-06 02:20:25,097 INFO     29 [qwen-vl-text] coord item[21]: text=布地奈德福莫特罗吸入粉雾剂BDII/●@0.1g*60吸2盒, bbox=[206, 507, 744, 540]
2026-08-06 02:20:25,097 INFO     29 [qwen-vl-text] coord item[22]: text=183.41 366.82, bbox=[775, 508, 932, 536]
2026-08-06 02:20:25,097 INFO     29 [qwen-vl-text] coord item[23]: text=Sig, bbox=[432, 558, 469, 588]
2026-08-06 02:20:25,097 INFO     29 [qwen-vl-text] coord item[24]: text=2吸/次,吸入,bid*30天, bbox=[511, 557, 754, 588]
2026-08-06 02:20:25,097 INFO     29 [qwen-vl-text] page=6 — 25/25 coords, api_time=7.3s
2026-08-06 02:20:25,098 INFO     29 [qwen-vl-text] new_positions (25):
[[6, 331.748, 530.46, 16.66, 55.93], [6, 45.467999999999996, 247.548, 73.185, 91.035], [6, 277.86, 451.312, 71.39999999999999, 92.225], [6, 524.566, 561.614, 72.59, 92.225], [6, 277.86, 349.43, 104.125, 124.35499999999999], [6, 390.688, 482.466, 104.125, 124.35499999999999], [6, 522.882, 561.614, 104.125, 124.35499999999999], [6, 277.86, 366.27, 136.85, 157.07999999999998], [6, 521.198, 561.614, 136.85, 157.07999999999998], [6, 757.8, 790.6379999999999, 135.66, 153.51], [6, 45.467999999999996, 373.848, 167.195, 188.01999999999998], [6, 520.356, 606.24, 167.195, 188.01999999999998], [6, 46.309999999999995, 197.028, 196.945, 217.17499999999998], [6, 372.164, 480.782, 232.04999999999998, 251.685], [6, 101.03999999999999, 142.298, 268.94, 288.575], [6, 191.134, 272.808, 268.94, 288.575], [6, 432.788, 468.99399999999997, 268.94, 287.385], [6, 602.872, 641.6039999999999, 268.94, 287.385], [6, 690.4399999999999, 729.172, 268.94, 287.385], [6, 759.4839999999999, 798.216, 267.75, 287.385], [6, 63.15, 101.88199999999999, 305.235, 336.175], [6, 173.452, 626.448, 301.66499999999996, 321.3], [6, 652.55, 784.744, 302.26, 318.91999999999996], [6, 363.74399999999997, 394.89799999999997, 332.01, 349.85999999999996], [6, 430.262, 634.8679999999999, 331.41499999999996, 349.85999999999996]]
2026-08-06 02:20:25,098 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=11.2s
2026-08-06 02:20:25,098 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 02:20:25,098 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-06 02:20:25,099 INFO     29 [qwen-vl-text] positions(26): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 02:20:25,099 INFO     29 [qwen-vl-text] page grouping: [7], lines per page: [26]
2026-08-06 02:20:25,253 INFO     29 [qwen-vl-text] page=7, rect=842x595, img=(2339x1653), dpi=200
2026-08-06 02:20:25,253 INFO     29 [qwen-vl-text] LLM extraction start, text_len=208
2026-08-06 02:20:25,253 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-06 02:20:25,253 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 197, \"bbox_end\": 222, \"encounter_dates\": [\"2025-01-24\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-01-24\n就诊科室:内科门诊\n主诊医\n姓名\n性别:男\n年龄:40岁\n卡号:4\n患者类型:GCP支付\n医疗证号:\n处方号:\n地址:PT027气雾剂 2024017-呼吸科\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n布地奈德福莫特罗吸入粉雾剂HIV●@1ug*60吸4盒\n183.41 733.64\nSig\n2吸/次,吸入,bid*60天",
    "role": "user"
  }
]
[92m02:20:25 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:20:25,255 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:20:28,062 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-06 02:20:28,062 INFO     29 [qwen-vl-text] LLM output (len=418):
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
      "dosage": "1ug*60吸",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 60,
      "quantity": "4盒",
      "notes": "2吸/次"
    }
  ]
}
2026-08-06 02:20:28,062 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-01-24]
2026-08-06 02:20:28,063 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=834734, prompt_len=899
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
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord API raw response (len=1347):
[
	{"text": "门(急)诊处方", "bbox": [385, 24, 604, 87]},
	{"text": "就诊时间:2025-01-24", "bbox": [69, 112, 294, 146]},
	{"text": "就诊科室:内科门诊", "bbox": [327, 111, 521, 145]},
	{"text": "主诊医", "bbox": [602, 112, 670, 146]},
	{"text": "姓名", "bbox": [69, 164, 109, 198]},
	{"text": "性别:男", "bbox": [327, 164, 408, 198]},
	{"text": "年龄:40岁", "bbox": [454, 164, 557, 198]},
	{"text": "卡号:4", "bbox": [602, 164, 672, 198]},
	{"text": "患者类型:GCP支付", "bbox": [69, 216, 258, 250]},
	{"text": "医疗证号:", "bbox": [327, 216, 427, 250]},
	{"text": "处方号:", "bbox": [600, 218, 669, 252]},
	{"text": "地址:PT027气雾剂 2024017-呼吸科", "bbox": [69, 267, 437, 302]},
	{"text": "身份证号:", "bbox": [600, 269, 695, 303]},
	{"text": "诊断:支气管哮喘", "bbox": [70, 317, 240, 351]},
	{"text": "西药处方", "bbox": [436, 376, 559, 409]},
	{"text": "组号", "bbox": [132, 436, 178, 470]},
	{"text": "项目名称", "bbox": [232, 436, 325, 470]},
	{"text": "规格", "bbox": [505, 436, 547, 470]},
	{"text": "总量", "bbox": [697, 436, 740, 470]},
	{"text": "单价", "bbox": [795, 436, 838, 470]},
	{"text": "金额", "bbox": [871, 436, 914, 470]},
	{"text": "R:", "bbox": [89, 497, 134, 548]},
	{"text": "布地奈德福莫特罗吸入粉雾剂HIV●@1ug*60吸4盒", "bbox": [213, 493, 724, 527]},
	{"text": "183.41 733.64", "bbox": [752, 495, 902, 523]},
	{"text": "Sig", "bbox": [428, 545, 465, 576]},
	{"text": "2吸/次,吸入,bid*60天", "bbox": [504, 544, 735, 576]}
]
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=7.2s
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[385, 24, 604, 87]
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-01-24, bbox=[69, 112, 294, 146]
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[327, 111, 521, 145]
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord item[3]: text=主诊医, bbox=[602, 112, 670, 146]
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[69, 164, 109, 198]
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[327, 164, 408, 198]
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:40岁, bbox=[454, 164, 557, 198]
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord item[7]: text=卡号:4, bbox=[602, 164, 672, 198]
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord item[8]: text=患者类型:GCP支付, bbox=[69, 216, 258, 250]
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[327, 216, 427, 250]
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord item[10]: text=处方号:, bbox=[600, 218, 669, 252]
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord item[11]: text=地址:PT027气雾剂 2024017-呼吸科, bbox=[69, 267, 437, 302]
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[600, 269, 695, 303]
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[70, 317, 240, 351]
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[436, 376, 559, 409]
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[132, 436, 178, 470]
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[232, 436, 325, 470]
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[505, 436, 547, 470]
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[697, 436, 740, 470]
2026-08-06 02:20:35,292 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[795, 436, 838, 470]
2026-08-06 02:20:35,293 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[871, 436, 914, 470]
2026-08-06 02:20:35,293 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[89, 497, 134, 548]
2026-08-06 02:20:35,293 INFO     29 [qwen-vl-text] coord item[22]: text=布地奈德福莫特罗吸入粉雾剂HIV●@1ug*60吸4盒, bbox=[213, 493, 724, 527]
2026-08-06 02:20:35,293 INFO     29 [qwen-vl-text] coord item[23]: text=183.41 733.64, bbox=[752, 495, 902, 523]
2026-08-06 02:20:35,293 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[428, 545, 465, 576]
2026-08-06 02:20:35,293 INFO     29 [qwen-vl-text] coord item[25]: text=2吸/次,吸入,bid*60天, bbox=[504, 544, 735, 576]
2026-08-06 02:20:35,293 INFO     29 [qwen-vl-text] page=7 — 26/26 coords, api_time=7.2s
2026-08-06 02:20:35,293 INFO     29 [qwen-vl-text] new_positions (26):
[[7, 324.17, 508.568, 14.28, 51.765], [7, 58.098, 247.548, 66.64, 86.86999999999999], [7, 275.334, 438.68199999999996, 66.045, 86.27499999999999], [7, 506.88399999999996, 564.14, 66.64, 86.86999999999999], [7, 58.098, 91.77799999999999, 97.58, 117.80999999999999], [7, 275.334, 343.536, 97.58, 117.80999999999999], [7, 382.268, 468.99399999999997, 97.58, 117.80999999999999], [7, 506.88399999999996, 565.824, 97.58, 117.80999999999999], [7, 58.098, 217.236, 128.51999999999998, 148.75], [7, 275.334, 359.534, 128.51999999999998, 148.75], [7, 505.2, 563.298, 129.71, 149.94], [7, 58.098, 367.954, 158.86499999999998, 179.69], [7, 505.2, 585.1899999999999, 160.055, 180.285], [7, 58.94, 202.07999999999998, 188.61499999999998, 208.845], [7, 367.11199999999997, 470.678, 223.72, 243.355], [7, 111.14399999999999, 149.876, 259.42, 279.65], [7, 195.344, 273.65, 259.42, 279.65], [7, 425.21, 460.574, 259.42, 279.65], [7, 586.874, 623.0799999999999, 259.42, 279.65], [7, 669.39, 705.596, 259.42, 279.65], [7, 733.382, 769.588, 259.42, 279.65], [7, 74.938, 112.828, 295.715, 326.06], [7, 179.346, 609.608, 293.335, 313.565], [7, 633.184, 759.4839999999999, 294.525, 311.185], [7, 360.376, 391.53, 324.275, 342.71999999999997], [7, 424.368, 618.87, 323.68, 342.71999999999997]]
2026-08-06 02:20:35,293 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=10.2s
2026-08-06 02:20:35,293 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 02:20:35,293 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-06 02:20:35,293 INFO     29 [qwen-vl-text] positions(31): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 02:20:35,293 INFO     29 [qwen-vl-text] page grouping: [8], lines per page: [31]
2026-08-06 02:20:35,460 INFO     29 [qwen-vl-text] page=8, rect=595x842, img=(1653x2339), dpi=200
2026-08-06 02:20:35,461 INFO     29 [qwen-vl-text] LLM extraction start, text_len=234
2026-08-06 02:20:35,461 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-06 02:20:35,462 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 223, \"bbox_end\": 253, \"encounter_dates\": [\"2025-01-03\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-01-03\n就诊科室:内科门诊\n主诊\n性别:男\n年龄:40岁\n卡号\n患者类型:GCP支付\n医疗证号:\n处方\n地址:PT027气雾剂 2024017-呼吸科\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●⑥ug*60吸2盒\n183.41 366.82\nSig\n2吸/次,吸入,bid*30天\n医师:\n医生编号:1326\n配剂人:\n核对人:\n合计:\n收费员:",
    "role": "user"
  }
]
[92m02:20:35 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:20:35,463 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:20:41,122 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-06 02:20:41,122 INFO     29 [qwen-vl-text] LLM output (len=419):
{
  "encounter_date": "2025-01-03",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "布地奈德福莫特罗吸入粉雾剂(Ⅱ型)",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "●⑥ug",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 30,
      "quantity": "2盒",
      "notes": "2吸/次"
    }
  ]
}
2026-08-06 02:20:41,122 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-01-03]
2026-08-06 02:20:41,123 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=595064, prompt_len=940
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共31行）
["门(急)诊处方", "就诊时间:2025-01-03", "就诊科室:内科门诊", "主诊", "性别:男", "年龄:40岁", "卡号", "患者类型:GCP支付", "医疗证号:", "处方", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●⑥ug*60吸2盒", "183.41 366.82", "Sig", "2吸/次,吸入,bid*30天", "医师:", "医生编号:1326", "配剂人:", "核对人:", "合计:", "收费员:"]

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
2026-08-06 02:20:52,079 INFO     29 [qwen-vl-text] coord API raw response (len=1589):
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
	{"text": "身份证号:", "bbox": [603, 186, 708, 204]},
	{"text": "诊断:支气管哮喘", "bbox": [19, 211, 204, 230]},
	{"text": "西药处方", "bbox": [421, 243, 557, 262]},
	{"text": "组号", "bbox": [90, 275, 139, 294]},
	{"text": "项目名称", "bbox": [198, 275, 300, 294]},
	{"text": "规格", "bbox": [497, 275, 544, 294]},
	{"text": "总量", "bbox": [707, 275, 755, 294]},
	{"text": "单价", "bbox": [815, 275, 863, 294]},
	{"text": "金额", "bbox": [899, 275, 947, 294]},
	{"text": "R:", "bbox": [44, 308, 93, 338]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●⑥ug*60吸2盒", "bbox": [178, 305, 738, 325]},
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
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord API: raw_items=31, valid_items=31, elapsed=11.0s
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[366, 58, 604, 92]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-01-03, bbox=[18, 105, 263, 123]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[300, 105, 514, 123]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[603, 105, 648, 123]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[4]: text=性别:男, bbox=[300, 132, 390, 150]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[5]: text=年龄:40岁, bbox=[440, 132, 553, 150]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[6]: text=卡号, bbox=[603, 132, 648, 150]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[7]: text=患者类型:GCP支付, bbox=[18, 159, 224, 177]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[8]: text=医疗证号:, bbox=[301, 159, 412, 177]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[9]: text=处方, bbox=[602, 159, 648, 177]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[10]: text=地址:PT027气雾剂 2024017-呼吸科, bbox=[18, 186, 422, 204]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[11]: text=身份证号:, bbox=[603, 186, 708, 204]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[12]: text=诊断:支气管哮喘, bbox=[19, 211, 204, 230]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[13]: text=西药处方, bbox=[421, 243, 557, 262]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[14]: text=组号, bbox=[90, 275, 139, 294]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[15]: text=项目名称, bbox=[198, 275, 300, 294]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[16]: text=规格, bbox=[497, 275, 544, 294]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[17]: text=总量, bbox=[707, 275, 755, 294]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[18]: text=单价, bbox=[815, 275, 863, 294]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[19]: text=金额, bbox=[899, 275, 947, 294]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[20]: text=R:, bbox=[44, 308, 93, 338]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[21]: text=布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●⑥ug*60吸2盒, bbox=[178, 305, 738, 325]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[22]: text=183.41 366.82, bbox=[768, 307, 934, 323]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[23]: text=Sig, bbox=[415, 333, 455, 351]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[24]: text=2吸/次,吸入,bid*30天, bbox=[497, 333, 751, 351]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[25]: text=医师:, bbox=[43, 627, 98, 646]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[26]: text=医生编号:1326, bbox=[347, 627, 510, 646]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[27]: text=配剂人:, bbox=[556, 627, 637, 646]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[28]: text=核对人:, bbox=[765, 627, 845, 646]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[29]: text=合计:, bbox=[60, 884, 113, 902]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] coord item[30]: text=收费员:, bbox=[270, 884, 350, 902]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] page=8 — 31/31 coords, api_time=11.0s
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] new_positions (31):
[[8, 217.76999999999998, 359.38, 48.836, 77.464], [8, 10.709999999999999, 156.48499999999999, 88.41, 103.566], [8, 178.5, 305.83, 88.41, 103.566], [8, 358.78499999999997, 385.56, 88.41, 103.566], [8, 178.5, 232.04999999999998, 111.14399999999999, 126.3], [8, 261.8, 329.03499999999997, 111.14399999999999, 126.3], [8, 358.78499999999997, 385.56, 111.14399999999999, 126.3], [8, 10.709999999999999, 133.28, 133.878, 149.034], [8, 179.095, 245.14, 133.878, 149.034], [8, 358.19, 385.56, 133.878, 149.034], [8, 10.709999999999999, 251.08999999999997, 156.612, 171.768], [8, 358.78499999999997, 421.26, 156.612, 171.768], [8, 11.305, 121.38, 177.662, 193.66], [8, 250.49499999999998, 331.41499999999996, 204.606, 220.60399999999998], [8, 53.55, 82.705, 231.54999999999998, 247.548], [8, 117.80999999999999, 178.5, 231.54999999999998, 247.548], [8, 295.715, 323.68, 231.54999999999998, 247.548], [8, 420.66499999999996, 449.22499999999997, 231.54999999999998, 247.548], [8, 484.92499999999995, 513.485, 231.54999999999998, 247.548], [8, 534.905, 563.4649999999999, 231.54999999999998, 247.548], [8, 26.18, 55.335, 259.336, 284.596], [8, 105.91, 439.10999999999996, 256.81, 273.65], [8, 456.96, 555.73, 258.49399999999997, 271.966], [8, 246.92499999999998, 270.72499999999997, 280.38599999999997, 295.542], [8, 295.715, 446.84499999999997, 280.38599999999997, 295.542], [8, 25.584999999999997, 58.309999999999995, 527.934, 543.932], [8, 206.465, 303.45, 527.934, 543.932], [8, 330.82, 379.015, 527.934, 543.932], [8, 455.17499999999995, 502.775, 527.934, 543.932], [8, 35.699999999999996, 67.235, 744.328, 759.4839999999999], [8, 160.65, 208.25, 744.328, 759.4839999999999]]
2026-08-06 02:20:52,080 INFO     29 [qwen-vl-text] ═══ DONE ═══ 31 positions, pages=1, time=16.8s
2026-08-06 02:20:52,081 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 02:20:52,081 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-06 02:20:52,081 INFO     29 [qwen-vl-text] positions(26): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 02:20:52,081 INFO     29 [qwen-vl-text] page grouping: [9], lines per page: [26]
2026-08-06 02:20:52,269 INFO     29 [qwen-vl-text] page=9, rect=842x595, img=(2339x1653), dpi=200
2026-08-06 02:20:52,269 INFO     29 [qwen-vl-text] LLM extraction start, text_len=198
2026-08-06 02:20:52,270 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-06 02:20:52,270 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 256, \"bbox_end\": 281, \"encounter_dates\": [\"2024-12-04\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2024-12-04\n就诊科室:内科门诊\n主诊\n姓名\n性别:男\n年龄:39岁\n卡号\n患者\n医疗证号:\n处方\n地址:PT027气雾剂 2024017-呼吸科\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●(50ug*60吸2盒\n183.41 366.82\nSig\n2吸/次,吸入,bid*30天",
    "role": "user"
  }
]
[92m02:20:52 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:20:52,271 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:20:52,462 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T02:20:52.462+00:00", "boot_at": "2026-08-06T01:59:43.412+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"5d401ece913c11f19b5e81513a69a703": {"id": "5d401ece913c11f19b5e81513a69a703", "doc_id": "5963bc44913b11f19b5e81513a69a703", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785982387379, "task_type": "dataflow", "root_trace_id": "7886908ae2584ba69682631c2a66f747", "root_traceparent": "00-7886908ae2584ba69682631c2a66f747-971004a6101741b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 02:20:58,229 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-06 02:20:58,229 INFO     29 [qwen-vl-text] LLM output (len=419):
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
      "dosage": "50ug",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 30,
      "quantity": "2盒",
      "notes": "2吸/次"
    }
  ]
}
2026-08-06 02:20:58,229 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-12-04]
2026-08-06 02:20:58,231 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=820637, prompt_len=889
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["门(急)诊处方", "就诊时间:2024-12-04", "就诊科室:内科门诊", "主诊", "姓名", "性别:男", "年龄:39岁", "卡号", "患者", "医疗证号:", "处方", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●(50ug*60吸2盒", "183.41 366.82", "Sig", "2吸/次,吸入,bid*30天"]

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
2026-08-06 02:21:05,372 INFO     29 [qwen-vl-text] coord API raw response (len=1337):
[
	{"text": "门(急)诊处方", "bbox": [388, 17, 617, 80]},
	{"text": "就诊时间:2024-12-04", "bbox": [60, 110, 293, 143]},
	{"text": "就诊科室:内科门诊", "bbox": [328, 107, 530, 141]},
	{"text": "主诊", "bbox": [615, 107, 654, 141]},
	{"text": "姓名", "bbox": [60, 163, 102, 197]},
	{"text": "性别:男", "bbox": [328, 160, 412, 195]},
	{"text": "年龄:39岁", "bbox": [460, 160, 567, 195]},
	{"text": "卡号", "bbox": [615, 160, 654, 195]},
	{"text": "患者", "bbox": [60, 216, 102, 250]},
	{"text": "医疗证号:", "bbox": [328, 214, 432, 249]},
	{"text": "处方", "bbox": [613, 214, 654, 249]},
	{"text": "地址:PT027气雾剂 2024017-呼吸科", "bbox": [60, 268, 443, 303]},
	{"text": "身份证号:", "bbox": [613, 266, 715, 300]},
	{"text": "诊断:支气管哮喘", "bbox": [60, 319, 236, 354]},
	{"text": "西药处方", "bbox": [441, 378, 570, 413]},
	{"text": "组号", "bbox": [124, 444, 172, 478]},
	{"text": "项目名称", "bbox": [228, 442, 325, 477]},
	{"text": "规格", "bbox": [513, 442, 557, 475]},
	{"text": "总量", "bbox": [714, 440, 760, 474]},
	{"text": "单价", "bbox": [817, 438, 864, 472]},
	{"text": "金额", "bbox": [898, 436, 945, 470]},
	{"text": "R:", "bbox": [80, 508, 126, 561]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●(50ug*60吸2盒", "bbox": [209, 499, 744, 535]},
	{"text": "183.41 366.82", "bbox": [774, 499, 933, 530]},
	{"text": "Sig", "bbox": [433, 554, 471, 586]},
	{"text": "2吸/次,吸入,bid*30天", "bbox": [512, 551, 755, 586]}
]
2026-08-06 02:21:05,372 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=7.1s
2026-08-06 02:21:05,372 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[388, 17, 617, 80]
2026-08-06 02:21:05,373 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2024-12-04, bbox=[60, 110, 293, 143]
2026-08-06 02:21:05,373 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[328, 107, 530, 141]
2026-08-06 02:21:05,373 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[615, 107, 654, 141]
2026-08-06 02:21:05,373 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[60, 163, 102, 197]
2026-08-06 02:21:05,373 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[328, 160, 412, 195]
2026-08-06 02:21:05,373 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:39岁, bbox=[460, 160, 567, 195]
2026-08-06 02:21:05,373 INFO     29 [qwen-vl-text] coord item[7]: text=卡号, bbox=[615, 160, 654, 195]
2026-08-06 02:21:05,373 INFO     29 [qwen-vl-text] coord item[8]: text=患者, bbox=[60, 216, 102, 250]
2026-08-06 02:21:05,373 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[328, 214, 432, 249]
2026-08-06 02:21:05,373 INFO     29 [qwen-vl-text] coord item[10]: text=处方, bbox=[613, 214, 654, 249]
2026-08-06 02:21:05,373 INFO     29 [qwen-vl-text] coord item[11]: text=地址:PT027气雾剂 2024017-呼吸科, bbox=[60, 268, 443, 303]
2026-08-06 02:21:05,373 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[613, 266, 715, 300]
2026-08-06 02:21:05,373 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[60, 319, 236, 354]
2026-08-06 02:21:05,373 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[441, 378, 570, 413]
2026-08-06 02:21:05,373 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[124, 444, 172, 478]
2026-08-06 02:21:05,373 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[228, 442, 325, 477]
2026-08-06 02:21:05,374 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[513, 442, 557, 475]
2026-08-06 02:21:05,374 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[714, 440, 760, 474]
2026-08-06 02:21:05,374 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[817, 438, 864, 472]
2026-08-06 02:21:05,374 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[898, 436, 945, 470]
2026-08-06 02:21:05,374 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[80, 508, 126, 561]
2026-08-06 02:21:05,374 INFO     29 [qwen-vl-text] coord item[22]: text=布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●(50ug*60吸2盒, bbox=[209, 499, 744, 535]
2026-08-06 02:21:05,374 INFO     29 [qwen-vl-text] coord item[23]: text=183.41 366.82, bbox=[774, 499, 933, 530]
2026-08-06 02:21:05,374 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[433, 554, 471, 586]
2026-08-06 02:21:05,374 INFO     29 [qwen-vl-text] coord item[25]: text=2吸/次,吸入,bid*30天, bbox=[512, 551, 755, 586]
2026-08-06 02:21:05,374 INFO     29 [qwen-vl-text] page=9 — 26/26 coords, api_time=7.1s
2026-08-06 02:21:05,374 INFO     29 [qwen-vl-text] new_positions (26):
[[9, 326.69599999999997, 519.514, 10.115, 47.599999999999994], [9, 50.519999999999996, 246.706, 65.45, 85.085], [9, 276.176, 446.26, 63.665, 83.895], [9, 517.8299999999999, 550.668, 63.665, 83.895], [9, 50.519999999999996, 85.884, 96.985, 117.21499999999999], [9, 276.176, 346.904, 95.19999999999999, 116.02499999999999], [9, 387.32, 477.414, 95.19999999999999, 116.02499999999999], [9, 517.8299999999999, 550.668, 95.19999999999999, 116.02499999999999], [9, 50.519999999999996, 85.884, 128.51999999999998, 148.75], [9, 276.176, 363.74399999999997, 127.33, 148.155], [9, 516.146, 550.668, 127.33, 148.155], [9, 50.519999999999996, 373.006, 159.45999999999998, 180.285], [9, 516.146, 602.03, 158.26999999999998, 178.5], [9, 50.519999999999996, 198.712, 189.80499999999998, 210.63], [9, 371.322, 479.94, 224.91, 245.73499999999999], [9, 104.408, 144.82399999999998, 264.18, 284.40999999999997], [9, 191.976, 273.65, 262.99, 283.815], [9, 431.94599999999997, 468.99399999999997, 262.99, 282.625], [9, 601.188, 639.92, 261.8, 282.03], [9, 687.914, 727.4879999999999, 260.61, 280.84], [9, 756.116, 795.6899999999999, 259.42, 279.65], [9, 67.36, 106.092, 302.26, 333.79499999999996], [9, 175.97799999999998, 626.448, 296.905, 318.325], [9, 651.708, 785.586, 296.905, 315.34999999999997], [9, 364.586, 396.582, 329.63, 348.66999999999996], [9, 431.104, 635.7099999999999, 327.84499999999997, 348.66999999999996]]
2026-08-06 02:21:05,374 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=13.3s
2026-08-06 02:21:05,374 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 02:21:05,375 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-06 02:21:05,375 INFO     29 [qwen-vl-text] positions(30): [[12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 02:21:05,375 INFO     29 [qwen-vl-text] page grouping: [12], lines per page: [30]
2026-08-06 02:21:05,544 INFO     29 [qwen-vl-text] page=12, rect=595x842, img=(1653x2339), dpi=200
2026-08-06 02:21:05,544 INFO     29 [qwen-vl-text] LLM extraction start, text_len=258
2026-08-06 02:21:05,544 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-06 02:21:05,545 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 693, \"bbox_end\": 722, \"encounter_dates\": [\"2026-01-05\"], \"department\": \"内科门诊（荔湾）\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "广州医科大学附属第三医院\n处方笺\n普通\n诊疗卡\n患者姓名\n年龄：41岁\n费别：南医保\n科室：内科门诊（荔湾）\n日期：2026-01-05 17:17:14\n处方号\n地址：荔湾\n2024017-呼吸科\n联系电\n身份号码：\n2739\n诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],急性气管支气管炎\nR\nP:\n布地奈德福莫特罗吸入粉雾剂(II) 160ug/4.5ug*60吸\n2盒\n剂量：每次2吸\n（\n1\n30\n盒）\n用法：吸入用药\nbid\n01-05\n处方金额：366.82元\n取药药房：门诊西药房（荔湾）",
    "role": "user"
  }
]
[92m02:21:05 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:21:05,546 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:21:08,643 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-06 02:21:08,643 INFO     29 [qwen-vl-text] LLM output (len=463):
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
      "dosage": "160ug/4.5ug",
      "frequency": "bid",
      "route": "吸入用药",
      "duration_days": null,
      "quantity": "2盒",
      "notes": "每次2吸"
    }
  ]
}
2026-08-06 02:21:08,643 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-05]
2026-08-06 02:21:08,645 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=831131, prompt_len=961
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共30行）
["广州医科大学附属第三医院", "处方笺", "普通", "诊疗卡", "患者姓名", "年龄：41岁", "费别：南医保", "科室：内科门诊（荔湾）", "日期：2026-01-05 17:17:14", "处方号", "地址：荔湾", "2024017-呼吸科", "联系电", "身份号码：", "2739", "诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],急性气管支气管炎", "R", "P:", "布地奈德福莫特罗吸入粉雾剂(II) 160ug/4.5ug*60吸", "2盒", "剂量：每次2吸", "（", "1", "30", "盒）", "用法：吸入用药", "bid", "01-05", "处方金额：366.82元", "取药药房：门诊西药房（荔湾）"]

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
2026-08-06 02:21:17,186 INFO     29 [qwen-vl-text] coord API raw response (len=1581):
[
	{"text": "广州医科大学附属第三医院", "bbox": [325, 100, 667, 123]},
	{"text": "处方笺", "bbox": [465, 135, 570, 160]},
	{"text": "普通", "bbox": [812, 168, 850, 182]},
	{"text": "诊疗卡", "bbox": [218, 211, 280, 227]},
	{"text": "患者姓名", "bbox": [218, 237, 283, 251]},
	{"text": "年龄：41岁", "bbox": [545, 236, 634, 250]},
	{"text": "费别：南医保", "bbox": [702, 235, 810, 248]},
	{"text": "科室：内科门诊（荔湾）", "bbox": [217, 259, 408, 274]},
	{"text": "日期：2026-01-05 17:17:14", "bbox": [437, 259, 661, 273]},
	{"text": "处方号", "bbox": [702, 258, 755, 273]},
	{"text": "地址：荔湾", "bbox": [218, 281, 312, 296]},
	{"text": "2024017-呼吸科", "bbox": [438, 281, 565, 295]},
	{"text": "联系电", "bbox": [702, 281, 755, 296]},
	{"text": "身份号码：", "bbox": [218, 304, 298, 319]},
	{"text": "2739", "bbox": [437, 304, 474, 318]},
	{"text": "诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],急性气管支气管炎", "bbox": [220, 321, 835, 337]},
	{"text": "R", "bbox": [244, 361, 278, 390]},
	{"text": "P:", "bbox": [278, 373, 297, 387]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(II) 160ug/4.5ug*60吸", "bbox": [250, 404, 714, 420]},
	{"text": "2盒", "bbox": [768, 404, 794, 418]},
	{"text": "剂量：每次2吸", "bbox": [328, 430, 438, 444]},
	{"text": "（", "bbox": [462, 428, 474, 444]},
	{"text": "1", "bbox": [485, 424, 497, 438]},
	{"text": "30", "bbox": [483, 438, 502, 451]},
	{"text": "盒）", "bbox": [510, 430, 544, 445]},
	{"text": "用法：吸入用药", "bbox": [580, 431, 697, 445]},
	{"text": "bid", "bbox": [739, 432, 766, 445]},
	{"text": "01-05", "bbox": [784, 433, 838, 447]},
	{"text": "处方金额：366.82元", "bbox": [252, 857, 474, 875]},
	{"text": "取药药房：门诊西药房（荔湾）", "bbox": [625, 858, 917, 875]}
]
2026-08-06 02:21:17,186 INFO     29 [qwen-vl-text] coord API: raw_items=30, valid_items=30, elapsed=8.5s
2026-08-06 02:21:17,186 INFO     29 [qwen-vl-text] coord item[0]: text=广州医科大学附属第三医院, bbox=[325, 100, 667, 123]
2026-08-06 02:21:17,186 INFO     29 [qwen-vl-text] coord item[1]: text=处方笺, bbox=[465, 135, 570, 160]
2026-08-06 02:21:17,186 INFO     29 [qwen-vl-text] coord item[2]: text=普通, bbox=[812, 168, 850, 182]
2026-08-06 02:21:17,186 INFO     29 [qwen-vl-text] coord item[3]: text=诊疗卡, bbox=[218, 211, 280, 227]
2026-08-06 02:21:17,186 INFO     29 [qwen-vl-text] coord item[4]: text=患者姓名, bbox=[218, 237, 283, 251]
2026-08-06 02:21:17,186 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：41岁, bbox=[545, 236, 634, 250]
2026-08-06 02:21:17,186 INFO     29 [qwen-vl-text] coord item[6]: text=费别：南医保, bbox=[702, 235, 810, 248]
2026-08-06 02:21:17,186 INFO     29 [qwen-vl-text] coord item[7]: text=科室：内科门诊（荔湾）, bbox=[217, 259, 408, 274]
2026-08-06 02:21:17,186 INFO     29 [qwen-vl-text] coord item[8]: text=日期：2026-01-05 17:17:14, bbox=[437, 259, 661, 273]
2026-08-06 02:21:17,186 INFO     29 [qwen-vl-text] coord item[9]: text=处方号, bbox=[702, 258, 755, 273]
2026-08-06 02:21:17,186 INFO     29 [qwen-vl-text] coord item[10]: text=地址：荔湾, bbox=[218, 281, 312, 296]
2026-08-06 02:21:17,186 INFO     29 [qwen-vl-text] coord item[11]: text=2024017-呼吸科, bbox=[438, 281, 565, 295]
2026-08-06 02:21:17,187 INFO     29 [qwen-vl-text] coord item[12]: text=联系电, bbox=[702, 281, 755, 296]
2026-08-06 02:21:17,187 INFO     29 [qwen-vl-text] coord item[13]: text=身份号码：, bbox=[218, 304, 298, 319]
2026-08-06 02:21:17,187 INFO     29 [qwen-vl-text] coord item[14]: text=2739, bbox=[437, 304, 474, 318]
2026-08-06 02:21:17,187 INFO     29 [qwen-vl-text] coord item[15]: text=诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],急性气管支气管炎, bbox=[220, 321, 835, 337]
2026-08-06 02:21:17,187 INFO     29 [qwen-vl-text] coord item[16]: text=R, bbox=[244, 361, 278, 390]
2026-08-06 02:21:17,187 INFO     29 [qwen-vl-text] coord item[17]: text=P:, bbox=[278, 373, 297, 387]
2026-08-06 02:21:17,187 INFO     29 [qwen-vl-text] coord item[18]: text=布地奈德福莫特罗吸入粉雾剂(II) 160ug/4.5ug*60吸, bbox=[250, 404, 714, 420]
2026-08-06 02:21:17,187 INFO     29 [qwen-vl-text] coord item[19]: text=2盒, bbox=[768, 404, 794, 418]
2026-08-06 02:21:17,187 INFO     29 [qwen-vl-text] coord item[20]: text=剂量：每次2吸, bbox=[328, 430, 438, 444]
2026-08-06 02:21:17,187 INFO     29 [qwen-vl-text] coord item[21]: text=（, bbox=[462, 428, 474, 444]
2026-08-06 02:21:17,187 INFO     29 [qwen-vl-text] coord item[22]: text=1, bbox=[485, 424, 497, 438]
2026-08-06 02:21:17,187 INFO     29 [qwen-vl-text] coord item[23]: text=30, bbox=[483, 438, 502, 451]
2026-08-06 02:21:17,187 INFO     29 [qwen-vl-text] coord item[24]: text=盒）, bbox=[510, 430, 544, 445]
2026-08-06 02:21:17,187 INFO     29 [qwen-vl-text] coord item[25]: text=用法：吸入用药, bbox=[580, 431, 697, 445]
2026-08-06 02:21:17,187 INFO     29 [qwen-vl-text] coord item[26]: text=bid, bbox=[739, 432, 766, 445]
2026-08-06 02:21:17,187 INFO     29 [qwen-vl-text] coord item[27]: text=01-05, bbox=[784, 433, 838, 447]
2026-08-06 02:21:17,187 INFO     29 [qwen-vl-text] coord item[28]: text=处方金额：366.82元, bbox=[252, 857, 474, 875]
2026-08-06 02:21:17,187 INFO     29 [qwen-vl-text] coord item[29]: text=取药药房：门诊西药房（荔湾）, bbox=[625, 858, 917, 875]
2026-08-06 02:21:17,187 INFO     29 [qwen-vl-text] page=12 — 30/30 coords, api_time=8.5s
2026-08-06 02:21:17,187 INFO     29 [qwen-vl-text] new_positions (30):
[[12, 193.375, 396.865, 84.2, 103.566], [12, 276.675, 339.15, 113.67, 134.72], [12, 483.14, 505.75, 141.456, 153.244], [12, 129.71, 166.6, 177.662, 191.134], [12, 129.71, 168.385, 199.554, 211.34199999999998], [12, 324.275, 377.22999999999996, 198.712, 210.5], [12, 417.69, 481.95, 197.87, 208.816], [12, 129.11499999999998, 242.76, 218.078, 230.708], [12, 260.015, 393.29499999999996, 218.078, 229.86599999999999], [12, 417.69, 449.22499999999997, 217.236, 229.86599999999999], [12, 129.71, 185.64, 236.602, 249.232], [12, 260.61, 336.175, 236.602, 248.39], [12, 417.69, 449.22499999999997, 236.602, 249.232], [12, 129.71, 177.31, 255.968, 268.598], [12, 260.015, 282.03, 255.968, 267.756], [12, 130.9, 496.825, 270.282, 283.75399999999996], [12, 145.18, 165.41, 303.962, 328.38], [12, 165.41, 176.715, 314.066, 325.854], [12, 148.75, 424.83, 340.168, 353.64], [12, 456.96, 472.43, 340.168, 351.95599999999996], [12, 195.16, 260.61, 362.06, 373.848], [12, 274.89, 282.03, 360.376, 373.848], [12, 288.575, 295.715, 357.008, 368.796], [12, 287.385, 298.69, 368.796, 379.74199999999996], [12, 303.45, 323.68, 362.06, 374.69], [12, 345.09999999999997, 414.715, 362.902, 374.69], [12, 439.705, 455.77, 363.74399999999997, 374.69], [12, 466.47999999999996, 498.60999999999996, 364.586, 376.37399999999997], [12, 149.94, 282.03, 721.5939999999999, 736.75], [12, 371.875, 545.615, 722.4359999999999, 736.75]]
2026-08-06 02:21:17,187 INFO     29 [qwen-vl-text] ═══ DONE ═══ 30 positions, pages=1, time=11.8s
2026-08-06 02:21:17,202 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-06 02:21:17,203 INFO     29 [Trace] task=5d401ece | doc=LZK 哮喘 广三(1).pdf | Extractor:Prescription | outputs={"chunks": "7 items, types={'PrescriptionRecord': 7}", "html": "", "json": "3678 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "chunks", "chunks_Clinical": "5 items, types={'OutpatientRecord': 5}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 5, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-06 02:21:17,203 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-06 02:21:17,213 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-06 02:21:17,214 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m02:21:17 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:21:17,215 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:21:23,486 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-06 02:21:23,494 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-06 02:21:23,495 INFO     29 [Trace] task=5d401ece | doc=LZK 哮喘 广三(1).pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "3678 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "chunks", "chunks_Clinical": "5 items, types={'OutpatientRecord': 5}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 5, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-06 02:21:23,495 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-06 02:21:23,506 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 02:21:23,506 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-06 02:21:24,121 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 02:21:24,128 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-06 02:21:24,129 INFO     29 [Trace] task=5d401ece | doc=LZK 哮喘 广三(1).pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "3678 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "chunks", "chunks_Clinical": "5 items, types={'OutpatientRecord': 5}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 5, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-06 02:21:24,129 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-06 02:21:24,142 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 02:21:24,142 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-06 02:21:24,142 INFO     29 [qwen-vl-text] positions(198): [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 02:21:24,143 INFO     29 [qwen-vl-text] page grouping: [10], lines per page: [198]
2026-08-06 02:21:24,369 INFO     29 [qwen-vl-text] page=10, rect=595x842, img=(1653x2339), dpi=200
2026-08-06 02:21:24,370 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1345
2026-08-06 02:21:24,370 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-06 02:21:24,370 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 282, \"bbox_end\": 479, \"encounter_dates\": [\"2022-06-08\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "激发试验检查报告\n姓名：\n测试号：\n门诊/住院号：\n000\n年龄：\n出生日期：\n19\n性别：\n男\n身高：\n170\n病区：\n内科门诊\n体重：\n81 kg\n机器编号：\n床号：\n电话：\nPred\nA1\nA1/Pd\nNS\nP1 chg%1\nP2 chg%2\nP3 chg%3\nFVC\n[L]\n4.84\n4.69\n97.1\n4.29\n4.22\n-10.1\n3.64\n-22.5\n4.01\n-14.6\nPEV 1\n[L]\n4.01\n3.05\n76.2\n2.72\n2.69\n-11.8\n2.24\n-26.5\n2.44\n-20.0\nPEV 1 % PVC\n[%]\n83.32\n65.02\n78.0\n63.54\n63.83\n-1.82\n61.73\n-5.06\n60.92\n-6.30\nPEV 1 % VC MAX\n[%]\n80.55\n64.94\n80.6\n62.34\n63.83\n-1.70\n61.73\n-4.94\n60.92\n-6.18\nVC MAX\n[L]\n5.05\n4.70\n93.1\n4.37\n4.22\n-10.2\n3.64\n-22.6\n4.01\n-14.7\nPEP\n[L/s]\n9.37\n9.95\n106.2\n9.06\n7.81\n-21.5\n6.73\n-32.3\n8.22\n-17.4\nMMEF 75/25\n[L/s]\n4.52\n1.54\n34.1\n1.33\n1.34\n-12.9\n1.14\n-25.8\n1.23\n-20.0\nMEF 50\n[L/s]\n5.17\n1.97\n38.1\n1.66\n1.71\n-13.4\n1.34\n-31.8\n1.42\n-28.0\nMEF 25\n[L/s]\n2.29\n0.58\n25.5\n0.52\n0.53\n-9.87\n0.50\n-14.6\n0.49\n-15.7\nPET\n[s]\n6.72\n6.87\n6.93\n3.16\n6.75\n0.57\n6.74\n0.38\nV backextrapolation ex\n[L]\n0.13\n0.09\n0.10\n-20.0\n0.08\n-41.6\n0.08\n-38.5\nPIF\n[L/s]\n8.04\n7.96\n7.58\n-5.76\n6.16\n-23.3\n7.78\n-3.20\nFIF 50\n[L/s]\n7.99\n7.86\n7.16\n-10.3\n5.36\n-32.9\n7.08\n-11.3\nMVV\n[L/min]\n141.88\nBF MVV\n[1/min]\nCumulated dose\n0.072\n0.078\n0.312\n2 Puf\nF/V ex\nF/V in\nVol [L]\nVol%VCmax\nVCmax\nTime [s]\nPD[-20] FEV 1: 0.2117 mg Cumulated\nPD[-20] PEF: < 0.078 mg Cumulated\nPD[] FEV1%I: could not be calculated!\n意见：\n2022/6/08 10:23:56上午\n1.轻度阻塞性通气功能障碍。\n2.支气管激发试验阳性(累计吸入乙酰甲胆碱0.312mg，FEV1下降大于20%，PD20=0.2117mg，气道高反应性(AHR)为中度\n通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后FEV1恢复至预计值80%。",
    "role": "user"
  }
]
[92m02:21:24 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:21:24,371 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:21:24,954 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T02:21:24.952+00:00", "boot_at": "2026-08-06T01:59:43.412+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"5d401ece913c11f19b5e81513a69a703": {"id": "5d401ece913c11f19b5e81513a69a703", "doc_id": "5963bc44913b11f19b5e81513a69a703", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785982387379, "task_type": "dataflow", "root_trace_id": "7886908ae2584ba69682631c2a66f747", "root_traceparent": "00-7886908ae2584ba69682631c2a66f747-971004a6101741b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 02:21:37,459 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-06 02:21:37,459 INFO     29 [qwen-vl-text] LLM output (len=1955):
{
  "exam_date": "2022-06-08",
  "report_date": "2022-06-08",
  "exam_name": "激发试验检查报告",
  "exam_category": "other",
  "body_part": null,
  "patient_name": null,
  "patient_gender": "男",
  "department": "内科门诊",
  "bed_number": null,
  "findings": "| 指标 | Pred | A1 | A1/Pd | NS | P1 chg%1 | P2 chg%2 | P3 chg%3 |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n| FVC [L] | 4.84 | 4.69 | 97.1 | 4.29 | 4.22 (-10.1) | 3.64 (-22.5) | 4.01 (-14.6) |\n| PEV 1 [L] | 4.01 | 3.05 | 76.2 | 2.72 | 2.69 (-11.8) | 2.24 (-26.5) | 2.44 (-20.0) |\n| PEV 1 % PVC [%] | 83.32 | 65.02 | 78.0 | 63.54 | 63.83 (-1.82) | 61.73 (-5.06) | 60.92 (-6.30) |\n| PEV 1 % VC MAX [%] | 80.55 | 64.94 | 80.6 | 62.34 | 63.83 (-1.70) | 61.73 (-4.94) | 60.92 (-6.18) |\n| VC MAX [L] | 5.05 | 4.70 | 93.1 | 4.37 | 4.22 (-10.2) | 3.64 (-22.6) | 4.01 (-14.7) |\n| PEP [L/s] | 9.37 | 9.95 | 106.2 | 9.06 | 7.81 (-21.5) | 6.73 (-32.3) | 8.22 (-17.4) |\n| MMEF 75/25 [L/s] | 4.52 | 1.54 | 34.1 | 1.33 | 1.34 (-12.9) | 1.14 (-25.8) | 1.23 (-20.0) |\n| MEF 50 [L/s] | 5.17 | 1.97 | 38.1 | 1.66 | 1.71 (-13.4) | 1.34 (-31.8) | 1.42 (-28.0) |\n| MEF 25 [L/s] | 2.29 | 0.58 | 25.5 | 0.52 | 0.53 (-9.87) | 0.50 (-14.6) | 0.49 (-15.7) |\n| PET [s] | 6.72 | 6.87 | 6.93 | 3.16 | 6.75 (0.57) | 6.74 (0.38) | |\n| V backextrapolation ex [L] | 0.13 | 0.09 | 0.10 | -20.0 | 0.08 (-41.6) | 0.08 (-38.5) | |\n| PIF [L/s] | 8.04 | 7.96 | 7.58 | -5.76 | 6.16 (-23.3) | 7.78 (-3.20) | |\n| FIF 50 [L/s] | 7.99 | 7.86 | 7.16 | -10.3 | 5.36 (-32.9) | 7.08 (-11.3) | |\n| MVV [L/min] | 141.88 | | | | | | |\n| BF MVV [1/min] | | | | | | | |\n| Cumulated dose | 0.072 | 0.078 | 0.312 | 2 Puf | | | |\n\nPD[-20] FEV 1: 0.2117 mg Cumulated\nPD[-20] PEF: < 0.078 mg Cumulated\nPD[] FEV1%I: could not be calculated!",
  "conclusion": "1.轻度阻塞性通气功能障碍。\n2.支气管激发试验阳性(累计吸入乙酰甲胆碱0.312mg，FEV1下降大于20%，PD20=0.2117mg，气道高反应性(AHR)为中度\n通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后FEV1恢复至预计值80%。",
  "physician": null,
  "reviewer": null
}
2026-08-06 02:21:37,461 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1393927, prompt_len=2553
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共198行）
["激发试验检查报告", "姓名：", "测试号：", "门诊/住院号：", "000", "年龄：", "出生日期：", "19", "性别：", "男", "身高：", "170", "病区：", "内科门诊", "体重：", "81 kg", "机器编号：", "床号：", "电话：", "Pred", "A1", "A1/Pd", "NS", "P1 chg%1", "P2 chg%2", "P3 chg%3", "FVC", "[L]", "4.84", "4.69", "97.1", "4.29", "4.22", "-10.1", "3.64", "-22.5", "4.01", "-14.6", "PEV 1", "[L]", "4.01", "3.05", "76.2", "2.72", "2.69", "-11.8", "2.24", "-26.5", "2.44", "-20.0", "PEV 1 % PVC", "[%]", "83.32", "65.02", "78.0", "63.54", "63.83", "-1.82", "61.73", "-5.06", "60.92", "-6.30", "PEV 1 % VC MAX", "[%]", "80.55", "64.94", "80.6", "62.34", "63.83", "-1.70", "61.73", "-4.94", "60.92", "-6.18", "VC MAX", "[L]", "5.05", "4.70", "93.1", "4.37", "4.22", "-10.2", "3.64", "-22.6", "4.01", "-14.7", "PEP", "[L/s]", "9.37", "9.95", "106.2", "9.06", "7.81", "-21.5", "6.73", "-32.3", "8.22", "-17.4", "MMEF 75/25", "[L/s]", "4.52", "1.54", "34.1", "1.33", "1.34", "-12.9", "1.14", "-25.8", "1.23", "-20.0", "MEF 50", "[L/s]", "5.17", "1.97", "38.1", "1.66", "1.71", "-13.4", "1.34", "-31.8", "1.42", "-28.0", "MEF 25", "[L/s]", "2.29", "0.58", "25.5", "0.52", "0.53", "-9.87", "0.50", "-14.6", "0.49", "-15.7", "PET", "[s]", "6.72", "6.87", "6.93", "3.16", "6.75", "0.57", "6.74", "0.38", "V backextrapolation ex", "[L]", "0.13", "0.09", "0.10", "-20.0", "0.08", "-41.6", "0.08", "-38.5", "PIF", "[L/s]", "8.04", "7.96", "7.58", "-5.76", "6.16", "-23.3", "7.78", "-3.20", "FIF 50", "[L/s]", "7.99", "7.86", "7.16", "-10.3", "5.36", "-32.9", "7.08", "-11.3", "MVV", "[L/min]", "141.88", "BF MVV", "[1/min]", "Cumulated dose", "0.072", "0.078", "0.312", "2 Puf", "F/V ex", "F/V in", "Vol [L]", "Vol%VCmax", "VCmax", "Time [s]", "PD[-20] FEV 1: 0.2117 mg Cumulated", "PD[-20] PEF: < 0.078 mg Cumulated", "PD[] FEV1%I: could not be calculated!", "意见：", "2022/6/08 10:23:56上午", "1.轻度阻塞性通气功能障碍。", "2.支气管激发试验阳性(累计吸入乙酰甲胆碱0.312mg，FEV1下降大于20%，PD20=0.2117mg，气道高反应性(AHR)为中度", "通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后FEV1恢复至预计值80%。"]

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
2026-08-06 02:22:41,831 INFO     29 [qwen-vl-text] coord API raw response (len=13360):
[
	{"text": "激发试验检查报告", "bbox": [427, 37, 620, 56]},
	{"text": "姓名：", "bbox": [215, 75, 260, 88], "label": "姓名"},
	{"text": "测试号：", "bbox": [215, 89, 275, 102], "label": "测试号"},
	{"text": "门诊/住院号：", "bbox": [542, 74, 644, 87], "label": "门诊/住院号"},
	{"text": "000", "bbox": [699, 75, 724, 87], "label": "000"},
	{"text": "年龄：", "bbox": [215, 103, 260, 116], "label": "年龄"},
	{"text": "出生日期：", "bbox": [542, 88, 618, 101], "label": "出生日期"},
	{"text": "19", "bbox": [700, 90, 724, 102], "label": "19"},
	{"text": "性别：", "bbox": [215, 117, 260, 130], "label": "性别"},
	{"text": "身高：", "bbox": [542, 102, 584, 115], "label": "身高"},
	{"text": "170", "bbox": [700, 103, 724, 115], "label": "170"},
	{"text": "病区：", "bbox": [215, 131, 260, 144], "label": "病区"},
	{"text": "内科门诊", "bbox": [375, 131, 445, 144], "label": "内科门诊"},
	{"text": "体重：", "bbox": [542, 116, 584, 129], "label": "体重"},
	{"text": "81 kg", "bbox": [699, 117, 741, 129], "label": "81 kg"},
	{"text": "机器编号：", "bbox": [215, 145, 293, 158], "label": "机器编号"},
	{"text": "床号：", "bbox": [542, 130, 584, 143], "label": "床号"},
	{"text": "电话：", "bbox": [542, 144, 584, 157], "label": "电话"},
	{"text": "Pred", "bbox": [332, 175, 368, 188], "label": "Pred"},
	{"text": "A1", "bbox": [402, 175, 418, 188], "label": "A1"},
	{"text": "A1/Pd", "bbox": [434, 175, 474, 188], "label": "A1/Pd"},
	{"text": "NS", "bbox": [508, 175, 525, 188], "label": "NS"},
	{"text": "P1 chg%1", "bbox": [558, 175, 628, 188], "label": "P1 chg%1"},
	{"text": "P2 chg%2", "bbox": [664, 175, 734, 188], "label": "P2 chg%2"},
	{"text": "P3 chg%3", "bbox": [769, 175, 839, 188], "label": "P3 chg%3"},
	{"text": "FVC", "bbox": [56, 203, 84, 215], "label": "FVC"},
	{"text": "[L]", "bbox": [263, 203, 287, 216], "label": "[L]"},
	{"text": "4.84", "bbox": [335, 203, 368, 215], "label": "4.84"},
	{"text": "4.69", "bbox": [397, 203, 425, 215], "label": "4.69"},
	{"text": "97.1", "bbox": [438, 203, 471, 215], "label": "97.1"},
	{"text": "4.29", "bbox": [493, 203, 524, 215], "label": "4.29"},
	{"text": "4.22", "bbox": [542, 203, 571, 215], "label": "4.22"},
	{"text": "-10.1", "bbox": [595, 203, 628, 215], "label": "-10.1"},
	{"text": "3.64", "bbox": [648, 203, 677, 215], "label": "3.64"},
	{"text": "-22.5", "bbox": [700, 203, 734, 215], "label": "-22.5"},
	{"text": "4.01", "bbox": [753, 203, 782, 215], "label": "4.01"},
	{"text": "-14.6", "bbox": [805, 203, 839, 215], "label": "-14.6"},
	{"text": "PEV 1", "bbox": [56, 217, 99, 229], "label": "PEV 1"},
	{"text": "[L]", "bbox": [263, 217, 287, 230], "label": "[L]"},
	{"text": "4.01", "bbox": [335, 217, 368, 229], "label": "4.01"},
	{"text": "3.05", "bbox": [397, 217, 425, 229], "label": "3.05"},
	{"text": "76.2", "bbox": [438, 217, 471, 229], "label": "76.2"},
	{"text": "2.72", "bbox": [493, 217, 524, 229], "label": "2.72"},
	{"text": "2.69", "bbox": [542, 217, 571, 229], "label": "2.69"},
	{"text": "-11.8", "bbox": [595, 217, 628, 229], "label": "-11.8"},
	{"text": "2.24", "bbox": [648, 217, 677, 229], "label": "2.24"},
	{"text": "-26.5", "bbox": [700, 217, 734, 229], "label": "-26.5"},
	{"text": "2.44", "bbox": [753, 217, 782, 229], "label": "2.44"},
	{"text": "-20.0", "bbox": [805, 217, 839, 229], "label": "-20.0"},
	{"text": "PEV 1 % PVC", "bbox": [56, 231, 152, 243], "label": "PEV 1 % PVC"},
	{"text": "[%]", "bbox": [263, 231, 287, 244], "label": "[%]"},
	{"text": "83.32", "bbox": [324, 231, 368, 243], "label": "83.32"},
	{"text": "65.02", "bbox": [386, 231, 425, 243], "label": "65.02"},
	{"text": "78.0", "bbox": [438, 231, 471, 243], "label": "78.0"},
	{"text": "63.54", "bbox": [482, 231, 524, 243], "label": "63.54"},
	{"text": "63.83", "bbox": [531, 231, 571, 243], "label": "63.83"},
	{"text": "-1.82", "bbox": [595, 231, 628, 243], "label": "-1.82"},
	{"text": "61.73", "bbox": [648, 231, 677, 243], "label": "61.73"},
	{"text": "-5.06", "bbox": [700, 231, 734, 243], "label": "-5.06"},
	{"text": "60.92", "bbox": [753, 231, 782, 243], "label": "60.92"},
	{"text": "-6.30", "bbox": [805, 231, 839, 243], "label": "-6.30"},
	{"text": "PEV 1 % VC MAX", "bbox": [56, 245, 177, 257], "label": "PEV 1 % VC MAX"},
	{"text": "[%]", "bbox": [263, 245, 287, 258], "label": "[%]"},
	{"text": "80.55", "bbox": [324, 245, 368, 257], "label": "80.55"},
	{"text": "64.94", "bbox": [386, 245, 425, 257], "label": "64.94"},
	{"text": "80.6", "bbox": [438, 245, 471, 257], "label": "80.6"},
	{"text": "62.34", "bbox": [482, 245, 524, 257], "label": "62.34"},
	{"text": "63.83", "bbox": [531, 245, 571, 257], "label": "63.83"},
	{"text": "-1.70", "bbox": [595, 245, 628, 257], "label": "-1.70"},
	{"text": "61.73", "bbox": [648, 245, 677, 257], "label": "61.73"},
	{"text": "-4.94", "bbox": [700, 245, 734, 257], "label": "-4.94"},
	{"text": "60.92", "bbox": [753, 245, 782, 257], "label": "60.92"},
	{"text": "-6.18", "bbox": [805, 245, 839, 257], "label": "-6.18"},
	{"text": "VC MAX", "bbox": [56, 259, 109, 271], "label": "VC MAX"},
	{"text": "[L]", "bbox": [263, 259, 287, 272], "label": "[L]"},
	{"text": "5.05", "bbox": [335, 259, 368, 271], "label": "5.05"},
	{"text": "4.70", "bbox": [397, 259, 425, 271], "label": "4.70"},
	{"text": "93.1", "bbox": [438, 259, 471, 271], "label": "93.1"},
	{"text": "4.37", "bbox": [493, 259, 524, 271], "label": "4.37"},
	{"text": "4.22", "bbox": [542, 259, 571, 271], "label": "4.22"},
	{"text": "-10.2", "bbox": [595, 259, 628, 271], "label": "-10.2"},
	{"text": "3.64", "bbox": [648, 259, 677, 271], "label": "3.64"},
	{"text": "-22.6", "bbox": [700, 259, 734, 271], "label": "-22.6"},
	{"text": "4.01", "bbox": [753, 259, 782, 271], "label": "4.01"},
	{"text": "-14.7", "bbox": [805, 259, 839, 271], "label": "-14.7"},
	{"text": "PEP", "bbox": [56, 273, 83, 285], "label": "PEP"},
	{"text": "[L/s]", "bbox": [246, 273, 287, 286], "label": "[L/s]"},
	{"text": "9.37", "bbox": [335, 273, 368, 285], "label": "9.37"},
	{"text": "9.95", "bbox": [397, 273, 425, 285], "label": "9.95"},
	{"text": "106.2", "bbox": [430, 273, 471, 285], "label": "106.2"},
	{"text": "9.06", "bbox": [493, 273, 524, 285], "label": "9.06"},
	{"text": "7.81", "bbox": [542, 273, 571, 285], "label": "7.81"},
	{"text": "-21.5", "bbox": [595, 273, 628, 285], "label": "-21.5"},
	{"text": "6.73", "bbox": [648, 273, 677, 285], "label": "6.73"},
	{"text": "-32.3", "bbox": [700, 273, 734, 285], "label": "-32.3"},
	{"text": "8.22", "bbox": [753, 273, 782, 285], "label": "8.22"},
	{"text": "-17.4", "bbox": [805, 273, 839, 285], "label": "-17.4"},
	{"text": "MMEF 75/25", "bbox": [56, 287, 143, 300], "label": "MMEF 75/25"},
	{"text": "[L/s]", "bbox": [246, 287, 287, 300], "label": "[L/s]"},
	{"text": "4.52", "bbox": [335, 287, 368, 300], "label": "4.52"},
	{"text": "1.54", "bbox": [397, 287, 425, 300], "label": "1.54"},
	{"text": "34.1", "bbox": [438, 287, 471, 300], "label": "34.1"},
	{"text": "1.33", "bbox": [493, 287, 524, 300], "label": "1.33"},
	{"text": "1.34", "bbox": [542, 287, 571, 300], "label": "1.34"},
	{"text": "-12.9", "bbox": [595, 287, 628, 300], "label": "-12.9"},
	{"text": "1.14", "bbox": [648, 287, 677, 300], "label": "1.14"},
	{"text": "-25.8", "bbox": [700, 287, 734, 300], "label": "-25.8"},
	{"text": "1.23", "bbox": [753, 287, 782, 300], "label": "1.23"},
	{"text": "-20.0", "bbox": [805, 287, 839, 300], "label": "-20.0"},
	{"text": "MEF 50", "bbox": [56, 301, 109, 314], "label": "MEF 50"},
	{"text": "[L/s]", "bbox": [246, 301, 287, 314], "label": "[L/s]"},
	{"text": "5.17", "bbox": [335, 301, 368, 314], "label": "5.17"},
	{"text": "1.97", "bbox": [397, 301, 425, 314], "label": "1.97"},
	{"text": "38.1", "bbox": [438, 301, 471, 314], "label": "38.1"},
	{"text": "1.66", "bbox": [493, 301, 524, 314], "label": "1.66"},
	{"text": "1.71", "bbox": [542, 301, 571, 314], "label": "1.71"},
	{"text": "-13.4", "bbox": [595, 301, 628, 314], "label": "-13.4"},
	{"text": "1.34", "bbox": [648, 301, 677, 314], "label": "1.34"},
	{"text": "-31.8", "bbox": [700, 301, 734, 314], "label": "-31.8"},
	{"text": "1.42", "bbox": [753, 301, 782, 314], "label": "1.42"},
	{"text": "-28.0", "bbox": [805, 301, 839, 314], "label": "-28.0"},
	{"text": "MEF 25", "bbox": [56, 315, 109, 328], "label": "MEF 25"},
	{"text": "[L/s]", "bbox": [246, 315, 287, 328], "label": "[L/s]"},
	{"text": "2.29", "bbox": [335, 315, 368, 328], "label": "2.29"},
	{"text": "0.58", "bbox": [397, 315, 425, 328], "label": "0.58"},
	{"text": "25.5", "bbox": [438, 315, 471, 328], "label": "25.5"},
	{"text": "0.52", "bbox": [493, 315, 524, 328], "label": "0.52"},
	{"text": "0.53", "bbox": [542, 315, 571, 328], "label": "0.53"},
	{"text": "-9.87", "bbox": [595, 315, 628, 328], "label": "-9.87"},
	{"text": "0.50", "bbox": [648, 315, 677, 328], "label": "0.50"},
	{"text": "-14.6", "bbox": [700, 315, 734, 328], "label": "-14.6"},
	{"text": "0.49", "bbox": [753, 315, 782, 328], "label": "0.49"},
	{"text": "-15.7", "bbox": [805, 315, 839, 328], "label": "-15.7"},
	{"text": "PET", "bbox": [56, 330, 83, 342], "label": "PET"},
	{"text": "[s]", "bbox": [263, 330, 287, 343], "label": "[s]"},
	{"text": "6.72", "bbox": [386, 330, 420, 342], "label": "6.72"},
	{"text": "6.87", "bbox": [490, 330, 524, 342], "label": "6.87"},
	{"text": "6.93", "bbox": [542, 330, 571, 342], "label": "6.93"},
	{"text": "3.16", "bbox": [595, 330, 628, 342], "label": "3.16"},
	{"text": "6.75", "bbox": [648, 330, 677, 342], "label": "6.75"},
	{"text": "0.57", "bbox": [700, 330, 734, 342], "label": "0.57"},
	{"text": "6.74", "bbox": [753, 330, 782, 342], "label": "6.74"},
	{"text": "0.38", "bbox": [805, 330, 839, 342], "label": "0.38"},
	{"text": "V backextrapolation ex", "bbox": [56, 344, 234, 357], "label": "V backextrapolation ex"},
	{"text": "[L]", "bbox": [263, 344, 287, 357], "label": "[L]"},
	{"text": "0.13", "bbox": [386, 344, 420, 357], "label": "0.13"},
	{"text": "0.09", "bbox": [490, 344, 524, 357], "label": "0.09"},
	{"text": "0.10", "bbox": [542, 344, 571, 357], "label": "0.10"},
	{"text": "-20.0", "bbox": [595, 344, 628, 357], "label": "-20.0"},
	{"text": "0.08", "bbox": [648, 344, 677, 357], "label": "0.08"},
	{"text": "-41.6", "bbox": [700, 344, 734, 357], "label": "-41.6"},
	{"text": "0.08", "bbox": [753, 344, 782, 357], "label": "0.08"},
	{"text": "-38.5", "bbox": [805, 344, 839, 357], "label": "-38.5"},
	{"text": "PIF", "bbox": [56, 358, 83, 371], "label": "PIF"},
	{"text": "[L/s]", "bbox": [246, 358, 287, 371], "label": "[L/s]"},
	{"text": "8.04", "bbox": [386, 358, 420, 371], "label": "8.04"},
	{"text": "7.96", "bbox": [490, 358, 524, 371], "label": "7.96"},
	{"text": "7.58", "bbox": [542, 358, 571, 371], "label": "7.58"},
	{"text": "-5.76", "bbox": [595, 358, 628, 371], "label": "-5.76"},
	{"text": "6.16", "bbox": [648, 358, 677, 371], "label": "6.16"},
	{"text": "-23.3", "bbox": [700, 358, 734, 371], "label": "-23.3"},
	{"text": "7.78", "bbox": [753, 358, 782, 371], "label": "7.78"},
	{"text": "-3.20", "bbox": [805, 358, 839, 371], "label": "-3.20"},
	{"text": "FIF 50", "bbox": [56, 372, 109, 385], "label": "FIF 50"},
	{"text": "[L/s]", "bbox": [246, 372, 287, 385], "label": "[L/s]"},
	{"text": "7.99", "bbox": [386, 372, 420, 385], "label": "7.99"},
	{"text": "7.86", "bbox": [490, 372, 524, 385], "label": "7.86"},
	{"text": "7.16", "bbox": [542, 372, 571, 385], "label": "7.16"},
	{"text": "-10.3", "bbox": [595, 372, 628, 385], "label": "-10.3"},
	{"text": "5.36", "bbox": [648, 372, 677, 385], "label": "5.36"},
	{"text": "-32.9", "bbox": [700, 372, 734, 385], "label": "-32.9"},
	{"text": "7.08", "bbox": [753, 372, 782, 385], "label": "7.08"},
	{"text": "-11.3", "bbox": [805, 372, 839, 385], "label": "-11.3"},
	{"text": "MVV", "bbox": [56, 386, 83, 399], "label": "MVV"},
	{"text": "[L/min]", "bbox": [229, 386, 287, 399], "label": "[L/min]"},
	{"text": "141.88", "bbox": [317, 386, 368, 399], "label": "141.88"},
	{"text": "BF MVV", "bbox": [56, 400, 109, 413], "label": "BF MVV"},
	{"text": "[1/min]", "bbox": [229, 400, 287, 413], "label": "[1/min]"},
	{"text": "Cumulated dose", "bbox": [56, 428, 179, 441], "label": "Cumulated dose"},
	{"text": "0.072", "bbox": [480, 428, 524, 441], "label": "0.072"},
	{"text": "0.078", "bbox": [542, 428, 575, 441], "label": "0.078"},
	{"text": "0.312", "bbox": [637, 428, 680, 441], "label": "0.312"},
	{"text": "2 Puf", "bbox": [740, 428, 786, 441], "label": "2 Puf"},
	{"text": "F/V ex", "bbox": [349, 472, 386, 484], "label": "F/V ex"},
	{"text": "F/V in", "bbox": [349, 719, 383, 730], "label": "F/V in"},
	{"text": "Vol [L]", "bbox": [644, 507, 681, 520], "label": "Vol [L]"},
	{"text": "Vol%VCmax", "bbox": [590, 530, 659, 540], "label": "Vol%VCmax"},
	{"text": "VCmax", "bbox": [657, 545, 698, 555], "label": "VCmax"},
	{"text": "Time [s]", "bbox": [775, 658, 820, 669], "label": "Time [s]"},
	{"text": "PD[-20] FEV 1: 0.2117 mg Cumulated", "bbox": [96, 750, 389, 763], "label": "PD[-20] FEV 1: 0.2117 mg Cumulated"},
	{"text": "PD[-20] PEF: < 0.078 mg Cumulated", "bbox": [96, 762, 381, 775], "label": "PD[-20] PEF: < 0.078 mg Cumulated"},
	{"text": "PD[] FEV1%I: could not be calculated!", "bbox": [96, 786, 414, 799], "label": "PD[] FEV1%I: could not be calculated!"},
	{"text": "意见：", "bbox": [86, 808, 134, 822], "label": "意见："},
	{"text": "2022/6/08 10:23:56上午", "bbox": [86, 830, 273, 843], "label": "2022/6/08 10:23:56上午"},
	{"text": "1.轻度阻塞性通气功能障碍。", "bbox": [86, 842, 314, 855], "label": "1.轻度阻塞性通气功能障碍。"},
	{"text": "2.支气管激发试验阳性(累计吸入乙酰甲胆碱0.312mg，FEV1
2026-08-06 02:22:41,831 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-06 02:22:41,835 INFO     29 [qwen-vl-text] coord API: raw_items=196, valid_items=195, elapsed=64.4s
2026-08-06 02:22:41,835 INFO     29 [qwen-vl-text] coord item[0]: text=激发试验检查报告, bbox=[427, 37, 620, 56]
2026-08-06 02:22:41,835 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[215, 75, 260, 88]
2026-08-06 02:22:41,835 INFO     29 [qwen-vl-text] coord item[2]: text=测试号：, bbox=[215, 89, 275, 102]
2026-08-06 02:22:41,835 INFO     29 [qwen-vl-text] coord item[3]: text=门诊/住院号：, bbox=[542, 74, 644, 87]
2026-08-06 02:22:41,835 INFO     29 [qwen-vl-text] coord item[4]: text=000, bbox=[699, 75, 724, 87]
2026-08-06 02:22:41,835 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：, bbox=[215, 103, 260, 116]
2026-08-06 02:22:41,835 INFO     29 [qwen-vl-text] coord item[6]: text=出生日期：, bbox=[542, 88, 618, 101]
2026-08-06 02:22:41,835 INFO     29 [qwen-vl-text] coord item[7]: text=19, bbox=[700, 90, 724, 102]
2026-08-06 02:22:41,835 INFO     29 [qwen-vl-text] coord item[8]: text=性别：, bbox=[215, 117, 260, 130]
2026-08-06 02:22:41,835 INFO     29 [qwen-vl-text] coord item[9]: text=身高：, bbox=[542, 102, 584, 115]
2026-08-06 02:22:41,835 INFO     29 [qwen-vl-text] coord item[10]: text=170, bbox=[700, 103, 724, 115]
2026-08-06 02:22:41,835 INFO     29 [qwen-vl-text] coord item[11]: text=病区：, bbox=[215, 131, 260, 144]
2026-08-06 02:22:41,835 INFO     29 [qwen-vl-text] coord item[12]: text=内科门诊, bbox=[375, 131, 445, 144]
2026-08-06 02:22:41,835 INFO     29 [qwen-vl-text] coord item[13]: text=体重：, bbox=[542, 116, 584, 129]
2026-08-06 02:22:41,835 INFO     29 [qwen-vl-text] coord item[14]: text=81 kg, bbox=[699, 117, 741, 129]
2026-08-06 02:22:41,835 INFO     29 [qwen-vl-text] coord item[15]: text=机器编号：, bbox=[215, 145, 293, 158]
2026-08-06 02:22:41,835 INFO     29 [qwen-vl-text] coord item[16]: text=床号：, bbox=[542, 130, 584, 143]
2026-08-06 02:22:41,835 INFO     29 [qwen-vl-text] coord item[17]: text=电话：, bbox=[542, 144, 584, 157]
2026-08-06 02:22:41,835 INFO     29 [qwen-vl-text] coord item[18]: text=Pred, bbox=[332, 175, 368, 188]
2026-08-06 02:22:41,835 INFO     29 [qwen-vl-text] coord item[19]: text=A1, bbox=[402, 175, 418, 188]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[20]: text=A1/Pd, bbox=[434, 175, 474, 188]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[21]: text=NS, bbox=[508, 175, 525, 188]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[22]: text=P1 chg%1, bbox=[558, 175, 628, 188]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[23]: text=P2 chg%2, bbox=[664, 175, 734, 188]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[24]: text=P3 chg%3, bbox=[769, 175, 839, 188]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[25]: text=FVC, bbox=[56, 203, 84, 215]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[26]: text=[L], bbox=[263, 203, 287, 216]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[27]: text=4.84, bbox=[335, 203, 368, 215]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[28]: text=4.69, bbox=[397, 203, 425, 215]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[29]: text=97.1, bbox=[438, 203, 471, 215]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[30]: text=4.29, bbox=[493, 203, 524, 215]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[31]: text=4.22, bbox=[542, 203, 571, 215]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[32]: text=-10.1, bbox=[595, 203, 628, 215]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[33]: text=3.64, bbox=[648, 203, 677, 215]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[34]: text=-22.5, bbox=[700, 203, 734, 215]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[35]: text=4.01, bbox=[753, 203, 782, 215]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[36]: text=-14.6, bbox=[805, 203, 839, 215]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[37]: text=PEV 1, bbox=[56, 217, 99, 229]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[38]: text=[L], bbox=[263, 217, 287, 230]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[39]: text=4.01, bbox=[335, 217, 368, 229]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[40]: text=3.05, bbox=[397, 217, 425, 229]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[41]: text=76.2, bbox=[438, 217, 471, 229]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[42]: text=2.72, bbox=[493, 217, 524, 229]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[43]: text=2.69, bbox=[542, 217, 571, 229]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[44]: text=-11.8, bbox=[595, 217, 628, 229]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[45]: text=2.24, bbox=[648, 217, 677, 229]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[46]: text=-26.5, bbox=[700, 217, 734, 229]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[47]: text=2.44, bbox=[753, 217, 782, 229]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[48]: text=-20.0, bbox=[805, 217, 839, 229]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[49]: text=PEV 1 % PVC, bbox=[56, 231, 152, 243]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[50]: text=[%], bbox=[263, 231, 287, 244]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[51]: text=83.32, bbox=[324, 231, 368, 243]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[52]: text=65.02, bbox=[386, 231, 425, 243]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[53]: text=78.0, bbox=[438, 231, 471, 243]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[54]: text=63.54, bbox=[482, 231, 524, 243]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[55]: text=63.83, bbox=[531, 231, 571, 243]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[56]: text=-1.82, bbox=[595, 231, 628, 243]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[57]: text=61.73, bbox=[648, 231, 677, 243]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[58]: text=-5.06, bbox=[700, 231, 734, 243]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[59]: text=60.92, bbox=[753, 231, 782, 243]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[60]: text=-6.30, bbox=[805, 231, 839, 243]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[61]: text=PEV 1 % VC MAX, bbox=[56, 245, 177, 257]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[62]: text=[%], bbox=[263, 245, 287, 258]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[63]: text=80.55, bbox=[324, 245, 368, 257]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[64]: text=64.94, bbox=[386, 245, 425, 257]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[65]: text=80.6, bbox=[438, 245, 471, 257]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[66]: text=62.34, bbox=[482, 245, 524, 257]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[67]: text=63.83, bbox=[531, 245, 571, 257]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[68]: text=-1.70, bbox=[595, 245, 628, 257]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[69]: text=61.73, bbox=[648, 245, 677, 257]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[70]: text=-4.94, bbox=[700, 245, 734, 257]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[71]: text=60.92, bbox=[753, 245, 782, 257]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[72]: text=-6.18, bbox=[805, 245, 839, 257]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[73]: text=VC MAX, bbox=[56, 259, 109, 271]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[74]: text=[L], bbox=[263, 259, 287, 272]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[75]: text=5.05, bbox=[335, 259, 368, 271]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[76]: text=4.70, bbox=[397, 259, 425, 271]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[77]: text=93.1, bbox=[438, 259, 471, 271]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[78]: text=4.37, bbox=[493, 259, 524, 271]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[79]: text=4.22, bbox=[542, 259, 571, 271]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[80]: text=-10.2, bbox=[595, 259, 628, 271]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[81]: text=3.64, bbox=[648, 259, 677, 271]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[82]: text=-22.6, bbox=[700, 259, 734, 271]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[83]: text=4.01, bbox=[753, 259, 782, 271]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[84]: text=-14.7, bbox=[805, 259, 839, 271]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[85]: text=PEP, bbox=[56, 273, 83, 285]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[86]: text=[L/s], bbox=[246, 273, 287, 286]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[87]: text=9.37, bbox=[335, 273, 368, 285]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[88]: text=9.95, bbox=[397, 273, 425, 285]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[89]: text=106.2, bbox=[430, 273, 471, 285]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[90]: text=9.06, bbox=[493, 273, 524, 285]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[91]: text=7.81, bbox=[542, 273, 571, 285]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[92]: text=-21.5, bbox=[595, 273, 628, 285]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[93]: text=6.73, bbox=[648, 273, 677, 285]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[94]: text=-32.3, bbox=[700, 273, 734, 285]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[95]: text=8.22, bbox=[753, 273, 782, 285]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[96]: text=-17.4, bbox=[805, 273, 839, 285]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[97]: text=MMEF 75/25, bbox=[56, 287, 143, 300]
2026-08-06 02:22:41,836 INFO     29 [qwen-vl-text] coord item[98]: text=[L/s], bbox=[246, 287, 287, 300]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[99]: text=4.52, bbox=[335, 287, 368, 300]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[100]: text=1.54, bbox=[397, 287, 425, 300]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[101]: text=34.1, bbox=[438, 287, 471, 300]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[102]: text=1.33, bbox=[493, 287, 524, 300]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[103]: text=1.34, bbox=[542, 287, 571, 300]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[104]: text=-12.9, bbox=[595, 287, 628, 300]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[105]: text=1.14, bbox=[648, 287, 677, 300]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[106]: text=-25.8, bbox=[700, 287, 734, 300]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[107]: text=1.23, bbox=[753, 287, 782, 300]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[108]: text=-20.0, bbox=[805, 287, 839, 300]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[109]: text=MEF 50, bbox=[56, 301, 109, 314]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[110]: text=[L/s], bbox=[246, 301, 287, 314]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[111]: text=5.17, bbox=[335, 301, 368, 314]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[112]: text=1.97, bbox=[397, 301, 425, 314]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[113]: text=38.1, bbox=[438, 301, 471, 314]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[114]: text=1.66, bbox=[493, 301, 524, 314]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[115]: text=1.71, bbox=[542, 301, 571, 314]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[116]: text=-13.4, bbox=[595, 301, 628, 314]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[117]: text=1.34, bbox=[648, 301, 677, 314]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[118]: text=-31.8, bbox=[700, 301, 734, 314]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[119]: text=1.42, bbox=[753, 301, 782, 314]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[120]: text=-28.0, bbox=[805, 301, 839, 314]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[121]: text=MEF 25, bbox=[56, 315, 109, 328]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[122]: text=[L/s], bbox=[246, 315, 287, 328]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[123]: text=2.29, bbox=[335, 315, 368, 328]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[124]: text=0.58, bbox=[397, 315, 425, 328]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[125]: text=25.5, bbox=[438, 315, 471, 328]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[126]: text=0.52, bbox=[493, 315, 524, 328]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[127]: text=0.53, bbox=[542, 315, 571, 328]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[128]: text=-9.87, bbox=[595, 315, 628, 328]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[129]: text=0.50, bbox=[648, 315, 677, 328]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[130]: text=-14.6, bbox=[700, 315, 734, 328]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[131]: text=0.49, bbox=[753, 315, 782, 328]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[132]: text=-15.7, bbox=[805, 315, 839, 328]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[133]: text=PET, bbox=[56, 330, 83, 342]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[134]: text=[s], bbox=[263, 330, 287, 343]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[135]: text=6.72, bbox=[386, 330, 420, 342]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[136]: text=6.87, bbox=[490, 330, 524, 342]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[137]: text=6.93, bbox=[542, 330, 571, 342]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[138]: text=3.16, bbox=[595, 330, 628, 342]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[139]: text=6.75, bbox=[648, 330, 677, 342]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[140]: text=0.57, bbox=[700, 330, 734, 342]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[141]: text=6.74, bbox=[753, 330, 782, 342]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[142]: text=0.38, bbox=[805, 330, 839, 342]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[143]: text=V backextrapolation ex, bbox=[56, 344, 234, 357]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[144]: text=[L], bbox=[263, 344, 287, 357]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[145]: text=0.13, bbox=[386, 344, 420, 357]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[146]: text=0.09, bbox=[490, 344, 524, 357]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[147]: text=0.10, bbox=[542, 344, 571, 357]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[148]: text=-20.0, bbox=[595, 344, 628, 357]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[149]: text=0.08, bbox=[648, 344, 677, 357]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[150]: text=-41.6, bbox=[700, 344, 734, 357]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[151]: text=0.08, bbox=[753, 344, 782, 357]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[152]: text=-38.5, bbox=[805, 344, 839, 357]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[153]: text=PIF, bbox=[56, 358, 83, 371]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[154]: text=[L/s], bbox=[246, 358, 287, 371]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[155]: text=8.04, bbox=[386, 358, 420, 371]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[156]: text=7.96, bbox=[490, 358, 524, 371]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[157]: text=7.58, bbox=[542, 358, 571, 371]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[158]: text=-5.76, bbox=[595, 358, 628, 371]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[159]: text=6.16, bbox=[648, 358, 677, 371]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[160]: text=-23.3, bbox=[700, 358, 734, 371]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[161]: text=7.78, bbox=[753, 358, 782, 371]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[162]: text=-3.20, bbox=[805, 358, 839, 371]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[163]: text=FIF 50, bbox=[56, 372, 109, 385]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[164]: text=[L/s], bbox=[246, 372, 287, 385]
2026-08-06 02:22:41,837 INFO     29 [qwen-vl-text] coord item[165]: text=7.99, bbox=[386, 372, 420, 385]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[166]: text=7.86, bbox=[490, 372, 524, 385]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[167]: text=7.16, bbox=[542, 372, 571, 385]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[168]: text=-10.3, bbox=[595, 372, 628, 385]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[169]: text=5.36, bbox=[648, 372, 677, 385]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[170]: text=-32.9, bbox=[700, 372, 734, 385]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[171]: text=7.08, bbox=[753, 372, 782, 385]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[172]: text=-11.3, bbox=[805, 372, 839, 385]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[173]: text=MVV, bbox=[56, 386, 83, 399]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[174]: text=[L/min], bbox=[229, 386, 287, 399]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[175]: text=141.88, bbox=[317, 386, 368, 399]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[176]: text=BF MVV, bbox=[56, 400, 109, 413]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[177]: text=[1/min], bbox=[229, 400, 287, 413]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[178]: text=Cumulated dose, bbox=[56, 428, 179, 441]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[179]: text=0.072, bbox=[480, 428, 524, 441]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[180]: text=0.078, bbox=[542, 428, 575, 441]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[181]: text=0.312, bbox=[637, 428, 680, 441]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[182]: text=2 Puf, bbox=[740, 428, 786, 441]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[183]: text=F/V ex, bbox=[349, 472, 386, 484]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[184]: text=F/V in, bbox=[349, 719, 383, 730]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[185]: text=Vol [L], bbox=[644, 507, 681, 520]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[186]: text=Vol%VCmax, bbox=[590, 530, 659, 540]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[187]: text=VCmax, bbox=[657, 545, 698, 555]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[188]: text=Time [s], bbox=[775, 658, 820, 669]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[189]: text=PD[-20] FEV 1: 0.2117 mg Cumulated, bbox=[96, 750, 389, 763]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[190]: text=PD[-20] PEF: < 0.078 mg Cumulated, bbox=[96, 762, 381, 775]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[191]: text=PD[] FEV1%I: could not be calculated!, bbox=[96, 786, 414, 799]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[192]: text=意见：, bbox=[86, 808, 134, 822]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[193]: text=2022/6/08 10:23:56上午, bbox=[86, 830, 273, 843]
2026-08-06 02:22:41,838 INFO     29 [qwen-vl-text] coord item[194]: text=1.轻度阻塞性通气功能障碍。, bbox=[86, 842, 314, 855]
2026-08-06 02:22:41,849 INFO     29 [qwen-vl-text] page=10 — 196/198 coords, api_time=64.4s
2026-08-06 02:22:41,850 INFO     29 [qwen-vl-text] new_positions (198):
[[10, 254.065, 368.9, 31.154, 47.152], [10, 127.925, 154.7, 63.15, 74.096], [10, 127.925, 163.625, 74.938, 85.884], [10, 322.49, 383.18, 62.308, 73.25399999999999], [10, 415.905, 430.78, 63.15, 73.25399999999999], [10, 127.925, 154.7, 86.726, 97.672], [10, 322.49, 367.71, 74.096, 85.042], [10, 416.5, 430.78, 75.78, 85.884], [10, 127.925, 154.7, 98.514, 109.46], [10, 322.49, 347.47999999999996, 85.884, 96.83], [10, 416.5, 430.78, 86.726, 96.83], [10, 127.925, 154.7, 110.30199999999999, 121.24799999999999], [10, 223.125, 264.775, 110.30199999999999, 121.24799999999999], [10, 322.49, 347.47999999999996, 97.672, 108.618], [10, 415.905, 440.895, 98.514, 108.618], [10, 127.925, 174.33499999999998, 122.08999999999999, 133.036], [10, 322.49, 347.47999999999996, 109.46, 120.40599999999999], [10, 322.49, 347.47999999999996, 121.24799999999999, 132.194], [10, 197.54, 218.95999999999998, 147.35, 158.296], [10, 239.19, 248.70999999999998, 147.35, 158.296], [10, 258.22999999999996, 282.03, 147.35, 158.296], [10, 302.26, 312.375, 147.35, 158.296], [10, 332.01, 373.65999999999997, 147.35, 158.296], [10, 395.08, 436.72999999999996, 147.35, 158.296], [10, 457.555, 499.205, 147.35, 158.296], [10, 33.32, 49.98, 170.926, 181.03], [10, 156.48499999999999, 170.765, 170.926, 181.87199999999999], [10, 199.325, 218.95999999999998, 170.926, 181.03], [10, 236.215, 252.875, 170.926, 181.03], [10, 260.61, 280.245, 170.926, 181.03], [10, 293.335, 311.78, 170.926, 181.03], [10, 322.49, 339.745, 170.926, 181.03], [10, 354.025, 373.65999999999997, 170.926, 181.03], [10, 385.56, 402.815, 170.926, 181.03], [10, 416.5, 436.72999999999996, 170.926, 181.03], [10, 448.03499999999997, 465.28999999999996, 170.926, 181.03], [10, 478.97499999999997, 499.205, 170.926, 181.03], [10, 33.32, 58.904999999999994, 182.714, 192.81799999999998], [10, 156.48499999999999, 170.765, 182.714, 193.66], [10, 199.325, 218.95999999999998, 182.714, 192.81799999999998], [10, 236.215, 252.875, 182.714, 192.81799999999998], [10, 260.61, 280.245, 182.714, 192.81799999999998], [10, 293.335, 311.78, 182.714, 192.81799999999998], [10, 322.49, 339.745, 182.714, 192.81799999999998], [10, 354.025, 373.65999999999997, 182.714, 192.81799999999998], [10, 385.56, 402.815, 182.714, 192.81799999999998], [10, 416.5, 436.72999999999996, 182.714, 192.81799999999998], [10, 448.03499999999997, 465.28999999999996, 182.714, 192.81799999999998], [10, 478.97499999999997, 499.205, 182.714, 192.81799999999998], [10, 33.32, 90.44, 194.50199999999998, 204.606], [10, 156.48499999999999, 170.765, 194.50199999999998, 205.44799999999998], [10, 192.78, 218.95999999999998, 194.50199999999998, 204.606], [10, 229.67, 252.875, 194.50199999999998, 204.606], [10, 260.61, 280.245, 194.50199999999998, 204.606], [10, 286.78999999999996, 311.78, 194.50199999999998, 204.606], [10, 315.945, 339.745, 194.50199999999998, 204.606], [10, 354.025, 373.65999999999997, 194.50199999999998, 204.606], [10, 385.56, 402.815, 194.50199999999998, 204.606], [10, 416.5, 436.72999999999996, 194.50199999999998, 204.606], [10, 448.03499999999997, 465.28999999999996, 194.50199999999998, 204.606], [10, 478.97499999999997, 499.205, 194.50199999999998, 204.606], [10, 33.32, 105.315, 206.29, 216.394], [10, 156.48499999999999, 170.765, 206.29, 217.236], [10, 192.78, 218.95999999999998, 206.29, 216.394], [10, 229.67, 252.875, 206.29, 216.394], [10, 260.61, 280.245, 206.29, 216.394], [10, 286.78999999999996, 311.78, 206.29, 216.394], [10, 315.945, 339.745, 206.29, 216.394], [10, 354.025, 373.65999999999997, 206.29, 216.394], [10, 385.56, 402.815, 206.29, 216.394], [10, 416.5, 436.72999999999996, 206.29, 216.394], [10, 448.03499999999997, 465.28999999999996, 206.29, 216.394], [10, 478.97499999999997, 499.205, 206.29, 216.394], [10, 33.32, 64.855, 218.078, 228.182], [10, 156.48499999999999, 170.765, 218.078, 229.024], [10, 199.325, 218.95999999999998, 218.078, 228.182], [10, 236.215, 252.875, 218.078, 228.182], [10, 260.61, 280.245, 218.078, 228.182], [10, 293.335, 311.78, 218.078, 228.182], [10, 322.49, 339.745, 218.078, 228.182], [10, 354.025, 373.65999999999997, 218.078, 228.182], [10, 385.56, 402.815, 218.078, 228.182], [10, 416.5, 436.72999999999996, 218.078, 228.182], [10, 448.03499999999997, 465.28999999999996, 218.078, 228.182], [10, 478.97499999999997, 499.205, 218.078, 228.182], [10, 33.32, 49.385, 229.86599999999999, 239.97], [10, 146.37, 170.765, 229.86599999999999, 240.81199999999998], [10, 199.325, 218.95999999999998, 229.86599999999999, 239.97], [10, 236.215, 252.875, 229.86599999999999, 239.97], [10, 255.85, 280.245, 229.86599999999999, 239.97], [10, 293.335, 311.78, 229.86599999999999, 239.97], [10, 322.49, 339.745, 229.86599999999999, 239.97], [10, 354.025, 373.65999999999997, 229.86599999999999, 239.97], [10, 385.56, 402.815, 229.86599999999999, 239.97], [10, 416.5, 436.72999999999996, 229.86599999999999, 239.97], [10, 448.03499999999997, 465.28999999999996, 229.86599999999999, 239.97], [10, 478.97499999999997, 499.205, 229.86599999999999, 239.97], [10, 33.32, 85.085, 241.654, 252.6], [10, 146.37, 170.765, 241.654, 252.6], [10, 199.325, 218.95999999999998, 241.654, 252.6], [10, 236.215, 252.875, 241.654, 252.6], [10, 260.61, 280.245, 241.654, 252.6], [10, 293.335, 311.78, 241.654, 252.6], [10, 322.49, 339.745, 241.654, 252.6], [10, 354.025, 373.65999999999997, 241.654, 252.6], [10, 385.56, 402.815, 241.654, 252.6], [10, 416.5, 436.72999999999996, 241.654, 252.6], [10, 448.03499999999997, 465.28999999999996, 241.654, 252.6], [10, 478.97499999999997, 499.205, 241.654, 252.6], [10, 33.32, 64.855, 253.44199999999998, 264.388], [10, 146.37, 170.765, 253.44199999999998, 264.388], [10, 199.325, 218.95999999999998, 253.44199999999998, 264.388], [10, 236.215, 252.875, 253.44199999999998, 264.388], [10, 260.61, 280.245, 253.44199999999998, 264.388], [10, 293.335, 311.78, 253.44199999999998, 264.388], [10, 322.49, 339.745, 253.44199999999998, 264.388], [10, 354.025, 373.65999999999997, 253.44199999999998, 264.388], [10, 385.56, 402.815, 253.44199999999998, 264.388], [10, 416.5, 436.72999999999996, 253.44199999999998, 264.388], [10, 448.03499999999997, 465.28999999999996, 253.44199999999998, 264.388], [10, 478.97499999999997, 499.205, 253.44199999999998, 264.388], [10, 33.32, 64.855, 265.23, 276.176], [10, 146.37, 170.765, 265.23, 276.176], [10, 199.325, 218.95999999999998, 265.23, 276.176], [10, 236.215, 252.875, 265.23, 276.176], [10, 260.61, 280.245, 265.23, 276.176], [10, 293.335, 311.78, 265.23, 276.176], [10, 322.49, 339.745, 265.23, 276.176], [10, 354.025, 373.65999999999997, 265.23, 276.176], [10, 385.56, 402.815, 265.23, 276.176], [10, 416.5, 436.72999999999996, 265.23, 276.176], [10, 448.03499999999997, 465.28999999999996, 265.23, 276.176], [10, 478.97499999999997, 499.205, 265.23, 276.176], [10, 33.32, 49.385, 277.86, 287.964], [10, 156.48499999999999, 170.765, 277.86, 288.806], [10, 229.67, 249.89999999999998, 277.86, 287.964], [10, 291.55, 311.78, 277.86, 287.964], [10, 322.49, 339.745, 277.86, 287.964], [10, 354.025, 373.65999999999997, 277.86, 287.964], [10, 385.56, 402.815, 277.86, 287.964], [10, 416.5, 436.72999999999996, 277.86, 287.964], [10, 448.03499999999997, 465.28999999999996, 277.86, 287.964], [10, 478.97499999999997, 499.205, 277.86, 287.964], [10, 33.32, 139.23, 289.64799999999997, 300.594], [10, 156.48499999999999, 170.765, 289.64799999999997, 300.594], [10, 229.67, 249.89999999999998, 289.64799999999997, 300.594], [10, 291.55, 311.78, 289.64799999999997, 300.594], [10, 322.49, 339.745, 289.64799999999997, 300.594], [10, 354.025, 373.65999999999997, 289.64799999999997, 300.594], [10, 385.56, 402.815, 289.64799999999997, 300.594], [10, 416.5, 436.72999999999996, 289.64799999999997, 300.594], [10, 448.03499999999997, 465.28999999999996, 289.64799999999997, 300.594], [10, 478.97499999999997, 499.205, 289.64799999999997, 300.594], [10, 33.32, 49.385, 301.436, 312.382], [10, 146.37, 170.765, 301.436, 312.382], [10, 229.67, 249.89999999999998, 301.436, 312.382], [10, 291.55, 311.78, 301.436, 312.382], [10, 322.49, 339.745, 301.436, 312.382], [10, 354.025, 373.65999999999997, 301.436, 312.382], [10, 385.56, 402.815, 301.436, 312.382], [10, 416.5, 436.72999999999996, 301.436, 312.382], [10, 448.03499999999997, 465.28999999999996, 301.436, 312.382], [10, 478.97499999999997, 499.205, 301.436, 312.382], [10, 33.32, 64.855, 313.224, 324.17], [10, 146.37, 170.765, 313.224, 324.17], [10, 229.67, 249.89999999999998, 313.224, 324.17], [10, 291.55, 311.78, 313.224, 324.17], [10, 322.49, 339.745, 313.224, 324.17], [10, 354.025, 373.65999999999997, 313.224, 324.17], [10, 385.56, 402.815, 313.224, 324.17], [10, 416.5, 436.72999999999996, 313.224, 324.17], [10, 448.03499999999997, 465.28999999999996, 313.224, 324.17], [10, 478.97499999999997, 499.205, 313.224, 324.17], [10, 33.32, 49.385, 325.012, 335.95799999999997], [10, 136.255, 170.765, 325.012, 335.95799999999997], [10, 188.61499999999998, 218.95999999999998, 325.012, 335.95799999999997], [10, 33.32, 64.855, 336.8, 347.746], [10, 136.255, 170.765, 336.8, 347.746], [10, 33.32, 106.505, 360.376, 371.322], [10, 285.59999999999997, 311.78, 360.376, 371.322], [10, 322.49, 342.125, 360.376, 371.322], [10, 379.015, 404.59999999999997, 360.376, 371.322], [10, 440.29999999999995, 467.66999999999996, 360.376, 371.322], [10, 207.655, 229.67, 397.424, 407.52799999999996], [10, 207.655, 227.885, 605.398, 614.66], [10, 383.18, 405.195, 426.894, 437.84], [10, 351.05, 392.10499999999996, 446.26, 454.68], [10, 390.91499999999996, 415.31, 458.89, 467.31], [10, 461.125, 487.9, 554.036, 563.298], [10, 57.12, 231.45499999999998, 631.5, 642.446], [10, 57.12, 226.695, 641.6039999999999, 652.55], [10, 57.12, 246.32999999999998, 661.812, 672.7579999999999], [10, 51.169999999999995, 79.72999999999999, 680.336, 692.124], [10, 51.169999999999995, 162.435, 698.86, 709.8059999999999], [10, 51.169999999999995, 186.82999999999998, 708.9639999999999, 719.91], [10, 51.169999999999995, 186.82999999999998, 708.9639999999999, 719.91], [10, 0, 0, 0, 0], [10, 0, 0, 0, 0]]
2026-08-06 02:22:41,850 INFO     29 [qwen-vl-text] ═══ DONE ═══ 198 positions, pages=1, time=77.7s
2026-08-06 02:22:41,850 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 02:22:41,850 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-06 02:22:41,850 INFO     29 [qwen-vl-text] positions(209): [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 02:22:41,851 INFO     29 [qwen-vl-text] page grouping: [11], lines per page: [209]
2026-08-06 02:22:42,055 INFO     29 [qwen-vl-text] page=11, rect=595x842, img=(1653x2339), dpi=200
2026-08-06 02:22:42,055 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1284
2026-08-06 02:22:42,055 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-06 02:22:42,056 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 482, \"bbox_end\": 690, \"encounter_dates\": [\"2021-01-21\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "检查日期：2021/1/21\n检查时间：16:43\n编号：16\n广州医科大学附属第三医院\n支气管扩张试验检查报告\n姓名：\n测试号：\n年龄：36岁\n性别：男\n病区：\n机器编号：\n门诊/住院号：\n出生日期：\n身高：\n体重：\n床号：\n电话：\nPred\nA1\nA1/Pd\nP1\nA2/Pd\nchg%1\nP2\nA3/Pd\nchg%2\nP3\nA4/Pd\nchg%3\nFVC\n[L]\n4.86\n3.48\n71.5%\n4.01\n82.4%\n15.19\n4.15\n85.4%\n19.47\n4.01\n82.6%\n15.47\nFEV 1\n[L]\n4.03\n1.97\n48.8%\n2.33\n57.9%\n18.59\n2.33\n57.8%\n18.48\n2.44\n60.5%\n24.02\nFEV 1 % FVC\n[%]\n83.32\n56.62\n68.0%\n58.29\n70.0%\n2.95\n56.15\n67.4%\n-0.83\n60.81\n73.0%\n7.40\nFEV 1 % VC MAX\n[%]\n80.73\n56.07\n69.5%\n58.29\n72.2%\n3.96\n56.15\n69.5%\n0.14\n60.81\n75.3%\n8.45\nVC MAX\n[L]\n5.08\n3.51\n69.1%\n4.01\n78.9%\n14.07\n4.15\n81.8%\n18.31\n4.01\n79.1%\n14.35\nPEF\n[L/s]\n9.41\n6.61\n70.3%\n7.99\n85.0%\n20.93\n7.91\n84.1%\n19.63\n8.07\n85.7%\n22.02\nMMEF 75/25\n[L/s]\n4.57\n0.81\n17.7%\n0.96\n21.1%\n19.59\n1.03\n22.6%\n28.17\n1.12\n24.6%\n39.07\nMEF 50\n[L/s]\n5.20\n1.00\n19.2%\n1.29\n24.8%\n29.25\n1.30\n24.9%\n29.87\n1.53\n29.3%\n52.75\nMEF 25\n[L/s]\n2.32\n0.39\n16.7%\n0.38\n16.4%\n-1.68\n0.50\n21.6%\n29.78\n0.41\n17.9%\n7.18\nFET\n[s]\n15.24\n6.42\n-57.87\n6.30\n-58.63\n6.55\n-57.05\nV backextrapolati\n[L/s]\n0.07\n0.07\n0.89\n0.09\n17.79\n0.08\n6.12\nPIF\n[L/s]\n7.03\n7.39\n5.19\n7.17\n1.99\n7.16\n1.91\nFIV1\n[L]\n3.40\n3.76\n10.58\n3.68\n8.26\n3.60\n5.96\nPEF50 % PIF50\n[%]\n16.56\n21.70\n31.06\n19.81\n19.65\n24.71\n49.20\nMVV\n[L/min]\n142.69\nBF MVV\n[1/min]\n意见：\n1.重度混合性肺通气功能障碍。\n2.支气管舒张试验阳性。\n（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后PEV1较基线增加大于12%，且绝对值增加大于200ml）",
    "role": "user"
  }
]
[92m02:22:42 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:22:42,057 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:22:42,058 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T02:22:42.056+00:00", "boot_at": "2026-08-06T01:59:43.412+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"5d401ece913c11f19b5e81513a69a703": {"id": "5d401ece913c11f19b5e81513a69a703", "doc_id": "5963bc44913b11f19b5e81513a69a703", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785982387379, "task_type": "dataflow", "root_trace_id": "7886908ae2584ba69682631c2a66f747", "root_traceparent": "00-7886908ae2584ba69682631c2a66f747-971004a6101741b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 02:22:59,185 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-06 02:22:59,185 INFO     29 [qwen-vl-text] LLM output (len=2062):
{
  "exam_date": "2021-01-21",
  "report_date": null,
  "exam_name": "支气管扩张试验检查报告",
  "exam_category": "other",
  "body_part": null,
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "| 指标 | Pred | A1 | A1/Pd | P1 | A2/Pd | chg%1 | P2 | A3/Pd | chg%2 | P3 | A4/Pd | chg%3 |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n| FVC [L] | 4.86 | 3.48 | 71.5% | 4.01 | 82.4% | 15.19 | 4.15 | 85.4% | 19.47 | 4.01 | 82.6% | 15.47 |\n| FEV 1 [L] | 4.03 | 1.97 | 48.8% | 2.33 | 57.9% | 18.59 | 2.33 | 57.8% | 18.48 | 2.44 | 60.5% | 24.02 |\n| FEV 1 % FVC [%] | 83.32 | 56.62 | 68.0% | 58.29 | 70.0% | 2.95 | 56.15 | 67.4% | -0.83 | 60.81 | 73.0% | 7.40 |\n| FEV 1 % VC MAX [%] | 80.73 | 56.07 | 69.5% | 58.29 | 72.2% | 3.96 | 56.15 | 69.5% | 0.14 | 60.81 | 75.3% | 8.45 |\n| VC MAX [L] | 5.08 | 3.51 | 69.1% | 4.01 | 78.9% | 14.07 | 4.15 | 81.8% | 18.31 | 4.01 | 79.1% | 14.35 |\n| PEF [L/s] | 9.41 | 6.61 | 70.3% | 7.99 | 85.0% | 20.93 | 7.91 | 84.1% | 19.63 | 8.07 | 85.7% | 22.02 |\n| MMEF 75/25 [L/s] | 4.57 | 0.81 | 17.7% | 0.96 | 21.1% | 19.59 | 1.03 | 22.6% | 28.17 | 1.12 | 24.6% | 39.07 |\n| MEF 50 [L/s] | 5.20 | 1.00 | 19.2% | 1.29 | 24.8% | 29.25 | 1.30 | 24.9% | 29.87 | 1.53 | 29.3% | 52.75 |\n| MEF 25 [L/s] | 2.32 | 0.39 | 16.7% | 0.38 | 16.4% | -1.68 | 0.50 | 21.6% | 29.78 | 0.41 | 17.9% | 7.18 |\n| FET [s] | 15.24 | 6.42 | -57.87 | 6.30 | -58.63 | 6.55 | -57.05 | | | | | |\n| V backextrapolati [L/s] | 0.07 | 0.07 | 0.89 | 0.09 | 17.79 | 0.08 | 6.12 | | | | | |\n| PIF [L/s] | 7.03 | 7.39 | 5.19 | 7.17 | 1.99 | 7.16 | 1.91 | | | | | |\n| FIV1 [L] | 3.40 | 3.76 | 10.58 | 3.68 | 8.26 | 3.60 | 5.96 | | | | | |\n| PEF50 % PIF50 [%] | 16.56 | 21.70 | 31.06 | 19.81 | 19.65 | 24.71 | 49.20 | | | | | |\n| MVV [L/min] | 142.69 | | | | | | | | | | | |\n| BF MVV [1/min] | | | | | | | | | | | | |",
  "conclusion": "意见：\n1.重度混合性肺通气功能障碍。\n2.支气管舒张试验阳性。\n（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后PEV1较基线增加大于12%，且绝对值增加大于200ml）",
  "physician": null,
  "reviewer": null
}
2026-08-06 02:22:59,191 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1426724, prompt_len=2525
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
2026-08-06 02:23:51,464 INFO     29 [qwen-vl-text] coord API raw response (len=10399):
[
	{"text": "检查日期：2021/1/21", "bbox": [49, 88, 158, 98]},
	{"text": "检查时间：16:43", "bbox": [187, 88, 273, 98]},
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
	{"text": "P1", "bbox": [457, 231, 473, 243]},
	{"text": "A2/Pd", "bbox": [490, 231, 532, 243]},
	{"text": "chg%1", "bbox": [548, 231, 588, 243]},
	{"text": "P2", "bbox": [630, 231, 647, 243]},
	{"text": "A3/Pd", "bbox": [664, 231, 705, 243]},
	{"text": "chg%2", "bbox": [722, 231, 763, 243]},
	{"text": "P3", "bbox": [804, 231, 820, 243]},
	{"text": "A4/Pd", "bbox": [837, 231, 878, 243]},
	{"text": "chg%3", "bbox": [895, 231, 934, 243]},
	{"text": "FVC", "bbox": [54, 257, 81, 269]},
	{"text": "[L]", "bbox": [198, 257, 221, 270]},
	{"text": "4.86", "bbox": [265, 257, 300, 269]},
	{"text": "3.48", "bbox": [324, 257, 358, 269]},
	{"text": "71.5%", "bbox": [375, 257, 417, 269]},
	{"text": "4.01", "bbox": [444, 257, 473, 269]},
	{"text": "82.4%", "bbox": [490, 257, 532, 269]},
	{"text": "15.19", "bbox": [548, 257, 588, 269]},
	{"text": "4.15", "bbox": [613, 257, 647, 269]},
	{"text": "85.4%", "bbox": [664, 257, 705, 269]},
	{"text": "19.47", "bbox": [722, 257, 763, 269]},
	{"text": "4.01", "bbox": [797, 257, 820, 269]},
	{"text": "82.6%", "bbox": [837, 257, 878, 269]},
	{"text": "15.47", "bbox": [895, 257, 934, 269]},
	{"text": "FEV 1", "bbox": [54, 270, 95, 283]},
	{"text": "[L]", "bbox": [198, 270, 221, 283]},
	{"text": "4.03", "bbox": [265, 270, 300, 283]},
	{"text": "1.97", "bbox": [324, 270, 358, 283]},
	{"text": "48.8%", "bbox": [324, 270, 417, 283]},
	{"text": "2.33", "bbox": [444, 270, 473, 283]},
	{"text": "57.9%", "bbox": [490, 270, 532, 283]},
	{"text": "18.59", "bbox": [548, 270, 588, 283]},
	{"text": "2.33", "bbox": [613, 270, 647, 283]},
	{"text": "57.8%", "bbox": [664, 270, 705, 283]},
	{"text": "18.48", "bbox": [722, 270, 763, 283]},
	{"text": "2.44", "bbox": [797, 270, 820, 283]},
	{"text": "60.5%", "bbox": [797, 270, 878, 283]},
	{"text": "24.02", "bbox": [895, 270, 934, 283]},
	{"text": "FEV 1 % FVC", "bbox": [54, 284, 146, 297]},
	{"text": "[%]", "bbox": [198, 284, 221, 297]},
	{"text": "83.32", "bbox": [258, 284, 300, 297]},
	{"text": "56.62", "bbox": [317, 284, 358, 297]},
	{"text": "68.0%", "bbox": [375, 284, 417, 297]},
	{"text": "58.29", "bbox": [435, 284, 473, 297]},
	{"text": "70.0%", "bbox": [490, 284, 532, 297]},
	{"text": "2.95", "bbox": [556, 284, 588, 297]},
	{"text": "56.15", "bbox": [606, 284, 647, 297]},
	{"text": "67.4%", "bbox": [664, 284, 705, 297]},
	{"text": "-0.83", "bbox": [722, 284, 763, 297]},
	{"text": "60.81", "bbox": [781, 284, 820, 297]},
	{"text": "73.0%", "bbox": [837, 284, 878, 297]},
	{"text": "7.40", "bbox": [902, 284, 934, 297]},
	{"text": "FEV 1 % VC MAX", "bbox": [54, 297, 170, 310]},
	{"text": "[%]", "bbox": [198, 297, 221, 310]},
	{"text": "80.73", "bbox": [258, 297, 300, 310]},
	{"text": "56.07", "bbox": [317, 297, 358, 310]},
	{"text": "69.5%", "bbox": [375, 297, 417, 310]},
	{"text": "58.29", "bbox": [435, 297, 473, 310]},
	{"text": "72.2%", "bbox": [490, 297, 532, 310]},
	{"text": "3.96", "bbox": [556, 297, 588, 310]},
	{"text": "56.15", "bbox": [606, 297, 647, 310]},
	{"text": "69.5%", "bbox": [664, 297, 705, 310]},
	{"text": "0.14", "bbox": [730, 297, 763, 310]},
	{"text": "60.81", "bbox": [781, 297, 820, 310]},
	{"text": "75.3%", "bbox": [837, 297, 878, 310]},
	{"text": "8.45", "bbox": [902, 297, 934, 310]},
	{"text": "VC MAX", "bbox": [54, 310, 105, 323]},
	{"text": "[L]", "bbox": [198, 310, 221, 323]},
	{"text": "5.08", "bbox": [265, 310, 300, 323]},
	{"text": "3.51", "bbox": [324, 310, 358, 323]},
	{"text": "69.1%", "bbox": [375, 310, 417, 323]},
	{"text": "4.01", "bbox": [444, 310, 473, 323]},
	{"text": "78.9%", "bbox": [490, 310, 532, 323]},
	{"text": "14.07", "bbox": [548, 310, 588, 323]},
	{"text": "4.15", "bbox": [613, 310, 647, 323]},
	{"text": "81.8%", "bbox": [664, 310, 705, 323]},
	{"text": "18.31", "bbox": [722, 310, 763, 323]},
	{"text": "4.01", "bbox": [797, 310, 820, 323]},
	{"text": "79.1%", "bbox": [837, 310, 878, 323]},
	{"text": "14.35", "bbox": [895, 310, 934, 323]},
	{"text": "PEF", "bbox": [54, 324, 80, 337]},
	{"text": "[L/s]", "bbox": [183, 324, 221, 337]},
	{"text": "9.41", "bbox": [265, 324, 300, 337]},
	{"text": "6.61", "bbox": [324, 324, 358, 337]},
	{"text": "70.3%", "bbox": [375, 324, 417, 337]},
	{"text": "7.99", "bbox": [444, 324, 473, 337]},
	{"text": "85.0%", "bbox": [490, 324, 532, 337]},
	{"text": "20.93", "bbox": [548, 324, 588, 337]},
	{"text": "7.91", "bbox": [613, 324, 647, 337]},
	{"text": "84.1%", "bbox": [664, 324, 705, 337]},
	{"text": "19.63", "bbox": [722, 324, 763, 337]},
	{"text": "8.07", "bbox": [797, 324, 820, 337]},
	{"text": "85.7%", "bbox": [837, 324, 878, 337]},
	{"text": "22.02", "bbox": [895, 324, 934, 337]},
	{"text": "MMEF 75/25", "bbox": [54, 338, 137, 351]},
	{"text": "[L/s]", "bbox": [183, 338, 221, 351]},
	{"text": "4.57", "bbox": [265, 338, 300, 351]},
	{"text": "0.81", "bbox": [324, 338, 358, 351]},
	{"text": "17.7%", "bbox": [375, 338, 417, 351]},
	{"text": "0.96", "bbox": [444, 338, 473, 351]},
	{"text": "21.1%", "bbox": [490, 338, 532, 351]},
	{"text": "19.59", "bbox": [548, 338, 588, 351]},
	{"text": "1.03", "bbox": [613, 338, 647, 351]},
	{"text": "22.6%", "bbox": [664, 338, 705, 351]},
	{"text": "28.17", "bbox": [722, 338, 763, 351]},
	{"text": "1.12", "bbox": [797, 338, 820, 351]},
	{"text": "24.6%", "bbox": [837, 338, 878, 351]},
	{"text": "39.07", "bbox": [895, 338, 934, 351]},
	{"text": "MEF 50", "bbox": [54, 351, 104, 364]},
	{"text": "[L/s]", "bbox": [183, 351, 221, 364]},
	{"text": "5.20", "bbox": [265, 351, 300, 364]},
	{"text": "1.00", "bbox": [324, 351, 358, 364]},
	{"text": "19.2%", "bbox": [375, 351, 417, 364]},
	{"text": "1.29", "bbox": [444, 351, 473, 364]},
	{"text": "24.8%", "bbox": [490, 351, 532, 364]},
	{"text": "29.25", "bbox": [548, 351, 588, 364]},
	{"text": "1.30", "bbox": [613, 351, 647, 364]},
	{"text": "24.9%", "bbox": [664, 351, 705, 364]},
	{"text": "29.87", "bbox": [722, 351, 763, 364]},
	{"text": "1.53", "bbox": [797, 351, 820, 364]},
	{"text": "29.3%", "bbox": [837, 351, 878, 364]},
	{"text": "52.75", "bbox": [895, 351, 934, 364]},
	{"text": "MEF 25", "bbox": [54, 365, 104, 378]},
	{"text": "[L/s]", "bbox": [183, 365, 221, 378]},
	{"text": "2.32", "bbox": [265, 365, 300, 378]},
	{"text": "0.39", "bbox": [324, 365, 358, 378]},
	{"text": "16.7%", "bbox": [375, 365, 417, 378]},
	{"text": "0.38", "bbox": [444, 365, 473, 378]},
	{"text": "16.4%", "bbox": [490, 365, 532, 378]},
	{"text": "-1.68", "bbox": [548, 365, 588, 378]},
	{"text": "0.50", "bbox": [613, 365, 647, 378]},
	{"text": "21.6%", "bbox": [664, 365, 705, 378]},
	{"text": "29.78", "bbox": [722, 365, 763, 378]},
	{"text": "0.41", "bbox": [797, 365, 820, 378]},
	{"text": "17.9%", "bbox": [837, 365, 878, 378]},
	{"text": "7.18", "bbox": [902, 365, 934, 378]},
	{"text": "FET", "bbox": [54, 378, 80, 391]},
	{"text": "[s]", "bbox": [200, 378, 221, 391]},
	{"text": "15.24", "bbox": [320, 378, 358, 391]},
	{"text": "6.42", "bbox": [441, 378, 473, 391]},
	{"text": "-57.87", "bbox": [542, 378, 588, 391]},
	{"text": "6.30", "bbox": [613, 378, 647, 391]},
	{"text": "-58.63", "bbox": [715, 378, 763, 391]},
	{"text": "6.55", "bbox": [790, 378, 820, 391]},
	{"text": "-57.05", "bbox": [887, 378, 934, 391]},
	{"text": "V backextrapolati", "bbox": [54, 392, 225, 405]},
	{"text": "[L/s]", "bbox": [183, 405, 221, 418]},
	{"text": "0.07", "bbox": [326, 392, 358, 405]},
	{"text": "0.07", "bbox": [441, 392, 473, 405]},
	{"text": "0.89", "bbox": [556, 392, 588, 405]},
	{"text": "0.09", "bbox": [613, 392, 647, 405]},
	{"text": "17.79", "bbox": [722, 392, 763, 405]},
	{"text": "0.08", "bbox": [790, 392, 820, 405]},
	{"text": "6.12", "bbox": [902, 392, 934, 405]},
	{"text": "PIF", "bbox": [54, 405, 80, 418]},
	{"text": "7.03", "bbox": [326, 405, 358, 418]},
	{"text": "7.39", "bbox": [441, 405, 473, 418]},
	{"text": "5.19", "bbox": [556, 405, 588, 418]},
	{"text": "7.17", "bbox": [613, 405, 647, 418]},
	{"text": "1.99", "bbox": [730, 405, 763, 418]},
	{"text": "7.16", "bbox": [790, 405, 820, 418]},
	{"text": "1.91", "bbox": [902, 405, 934, 418]},
	{"text": "FIV1", "bbox": [54, 419, 87, 432]},
	{"text": "[L]", "bbox": [198, 419, 221, 432]},
	{"text": "3.40", "bbox": [326, 419, 358, 432]},
	{"text": "3.76", "bbox": [441, 419, 473, 432]},
	{"text": "10.58", "bbox": [548, 419, 588, 432]},
	{"text": "3.68", "bbox": [613, 419, 647, 432]},
	{"text": "8.26", "bbox": [730, 419, 763, 432]},
	{"text": "3.60", "bbox": [790, 419, 820, 432]},
	{"text": "5.96", "bbox": [902, 419, 934, 432]},
	{"text": "PEF50 % PIF50", "bbox": [54, 432, 162, 445]},
	{"text": "[%]", "bbox": [198, 432, 221, 445]},
	{"text": "16.56", "bbox": [317, 432, 358, 445]},
	{"text": "21.70", "bbox": [435, 432, 473, 445]},
	{"text": "31.06", "bbox": [548, 432, 588, 445]},
	{"text": "19.81", "bbox": [606, 432, 647, 445]},
	{"text": "19.65", "bbox": [722, 432, 763, 445]},
	{"text": "24.71", "bbox": [781, 432, 820, 445]},
	{"text": "49.20", "bbox": [895, 432, 934, 445]},
	{"text": "MVV", "bbox": [54, 446, 80, 459]},
	{"text": "[L/min]", "bbox": [168, 446, 221, 459]},
	{"text": "142.69", "bbox": [251, 446, 300, 459]},
	{"text": "BF MVV", "bbox": [54, 459, 104, 472]},
	{"text": "[1/min]", "bbox": [168, 459, 221, 472]},
	{"text": "意见：", "bbox": [73, 789, 120, 803]},
	{"text": "1.重度混合性肺通气功能障碍。", "bbox": [73, 803, 292, 816]},
	{"text": "2.支气管舒张试验阳性。", "bbox": [73, 815, 244, 828]},
	{"text": "（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后PEV1较基线增加大于12%，且绝对值增加大于200ml）", "bbox": [80, 826, 800, 839]}
]
2026-08-06 02:23:51,464 INFO     29 [qwen-vl-text] coord API: raw_items=208, valid_items=208, elapsed=52.3s
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[0]: text=检查日期：2021/1/21, bbox=[49, 88, 158, 98]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[1]: text=检查时间：16:43, bbox=[187, 88, 273, 98]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[2]: text=编号：16, bbox=[295, 88, 342, 98]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[3]: text=广州医科大学附属第三医院, bbox=[367, 104, 644, 120]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[4]: text=支气管扩张试验检查报告, bbox=[378, 120, 632, 136]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[5]: text=姓名：, bbox=[191, 144, 234, 157]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[6]: text=测试号：, bbox=[191, 157, 248, 170]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[7]: text=年龄：36岁, bbox=[191, 170, 382, 183]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[8]: text=性别：男, bbox=[191, 183, 358, 196]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[9]: text=病区：, bbox=[191, 196, 234, 209]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[10]: text=机器编号：, bbox=[191, 209, 264, 222]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[11]: text=门诊/住院号：, bbox=[500, 143, 596, 156]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[12]: text=出生日期：, bbox=[500, 156, 572, 169]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[13]: text=身高：, bbox=[500, 169, 540, 182]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[14]: text=体重：, bbox=[500, 182, 540, 195]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[15]: text=床号：, bbox=[500, 195, 540, 208]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[16]: text=电话：, bbox=[500, 208, 540, 221]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[17]: text=Pred, bbox=[265, 231, 300, 243]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[18]: text=A1, bbox=[340, 231, 358, 243]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[19]: text=A1/Pd, bbox=[375, 231, 417, 243]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[20]: text=P1, bbox=[457, 231, 473, 243]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[21]: text=A2/Pd, bbox=[490, 231, 532, 243]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[22]: text=chg%1, bbox=[548, 231, 588, 243]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[23]: text=P2, bbox=[630, 231, 647, 243]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[24]: text=A3/Pd, bbox=[664, 231, 705, 243]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[25]: text=chg%2, bbox=[722, 231, 763, 243]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[26]: text=P3, bbox=[804, 231, 820, 243]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[27]: text=A4/Pd, bbox=[837, 231, 878, 243]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[28]: text=chg%3, bbox=[895, 231, 934, 243]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[29]: text=FVC, bbox=[54, 257, 81, 269]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[30]: text=[L], bbox=[198, 257, 221, 270]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[31]: text=4.86, bbox=[265, 257, 300, 269]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[32]: text=3.48, bbox=[324, 257, 358, 269]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[33]: text=71.5%, bbox=[375, 257, 417, 269]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[34]: text=4.01, bbox=[444, 257, 473, 269]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[35]: text=82.4%, bbox=[490, 257, 532, 269]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[36]: text=15.19, bbox=[548, 257, 588, 269]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[37]: text=4.15, bbox=[613, 257, 647, 269]
2026-08-06 02:23:51,465 INFO     29 [qwen-vl-text] coord item[38]: text=85.4%, bbox=[664, 257, 705, 269]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[39]: text=19.47, bbox=[722, 257, 763, 269]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[40]: text=4.01, bbox=[797, 257, 820, 269]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[41]: text=82.6%, bbox=[837, 257, 878, 269]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[42]: text=15.47, bbox=[895, 257, 934, 269]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[43]: text=FEV 1, bbox=[54, 270, 95, 283]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[44]: text=[L], bbox=[198, 270, 221, 283]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[45]: text=4.03, bbox=[265, 270, 300, 283]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[46]: text=1.97, bbox=[324, 270, 358, 283]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[47]: text=48.8%, bbox=[324, 270, 417, 283]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[48]: text=2.33, bbox=[444, 270, 473, 283]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[49]: text=57.9%, bbox=[490, 270, 532, 283]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[50]: text=18.59, bbox=[548, 270, 588, 283]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[51]: text=2.33, bbox=[613, 270, 647, 283]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[52]: text=57.8%, bbox=[664, 270, 705, 283]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[53]: text=18.48, bbox=[722, 270, 763, 283]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[54]: text=2.44, bbox=[797, 270, 820, 283]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[55]: text=60.5%, bbox=[797, 270, 878, 283]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[56]: text=24.02, bbox=[895, 270, 934, 283]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[57]: text=FEV 1 % FVC, bbox=[54, 284, 146, 297]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[58]: text=[%], bbox=[198, 284, 221, 297]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[59]: text=83.32, bbox=[258, 284, 300, 297]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[60]: text=56.62, bbox=[317, 284, 358, 297]
2026-08-06 02:23:51,466 INFO     29 [qwen-vl-text] coord item[61]: text=68.0%, bbox=[375, 284, 417, 297]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[62]: text=58.29, bbox=[435, 284, 473, 297]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[63]: text=70.0%, bbox=[490, 284, 532, 297]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[64]: text=2.95, bbox=[556, 284, 588, 297]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[65]: text=56.15, bbox=[606, 284, 647, 297]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[66]: text=67.4%, bbox=[664, 284, 705, 297]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[67]: text=-0.83, bbox=[722, 284, 763, 297]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[68]: text=60.81, bbox=[781, 284, 820, 297]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[69]: text=73.0%, bbox=[837, 284, 878, 297]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[70]: text=7.40, bbox=[902, 284, 934, 297]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[71]: text=FEV 1 % VC MAX, bbox=[54, 297, 170, 310]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[72]: text=[%], bbox=[198, 297, 221, 310]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[73]: text=80.73, bbox=[258, 297, 300, 310]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[74]: text=56.07, bbox=[317, 297, 358, 310]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[75]: text=69.5%, bbox=[375, 297, 417, 310]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[76]: text=58.29, bbox=[435, 297, 473, 310]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[77]: text=72.2%, bbox=[490, 297, 532, 310]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[78]: text=3.96, bbox=[556, 297, 588, 310]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[79]: text=56.15, bbox=[606, 297, 647, 310]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[80]: text=69.5%, bbox=[664, 297, 705, 310]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[81]: text=0.14, bbox=[730, 297, 763, 310]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[82]: text=60.81, bbox=[781, 297, 820, 310]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[83]: text=75.3%, bbox=[837, 297, 878, 310]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[84]: text=8.45, bbox=[902, 297, 934, 310]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[85]: text=VC MAX, bbox=[54, 310, 105, 323]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[86]: text=[L], bbox=[198, 310, 221, 323]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[87]: text=5.08, bbox=[265, 310, 300, 323]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[88]: text=3.51, bbox=[324, 310, 358, 323]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[89]: text=69.1%, bbox=[375, 310, 417, 323]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[90]: text=4.01, bbox=[444, 310, 473, 323]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[91]: text=78.9%, bbox=[490, 310, 532, 323]
2026-08-06 02:23:51,467 INFO     29 [qwen-vl-text] coord item[92]: text=14.07, bbox=[548, 310, 588, 323]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[93]: text=4.15, bbox=[613, 310, 647, 323]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[94]: text=81.8%, bbox=[664, 310, 705, 323]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[95]: text=18.31, bbox=[722, 310, 763, 323]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[96]: text=4.01, bbox=[797, 310, 820, 323]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[97]: text=79.1%, bbox=[837, 310, 878, 323]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[98]: text=14.35, bbox=[895, 310, 934, 323]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[99]: text=PEF, bbox=[54, 324, 80, 337]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[100]: text=[L/s], bbox=[183, 324, 221, 337]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[101]: text=9.41, bbox=[265, 324, 300, 337]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[102]: text=6.61, bbox=[324, 324, 358, 337]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[103]: text=70.3%, bbox=[375, 324, 417, 337]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[104]: text=7.99, bbox=[444, 324, 473, 337]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[105]: text=85.0%, bbox=[490, 324, 532, 337]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[106]: text=20.93, bbox=[548, 324, 588, 337]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[107]: text=7.91, bbox=[613, 324, 647, 337]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[108]: text=84.1%, bbox=[664, 324, 705, 337]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[109]: text=19.63, bbox=[722, 324, 763, 337]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[110]: text=8.07, bbox=[797, 324, 820, 337]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[111]: text=85.7%, bbox=[837, 324, 878, 337]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[112]: text=22.02, bbox=[895, 324, 934, 337]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[113]: text=MMEF 75/25, bbox=[54, 338, 137, 351]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[114]: text=[L/s], bbox=[183, 338, 221, 351]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[115]: text=4.57, bbox=[265, 338, 300, 351]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[116]: text=0.81, bbox=[324, 338, 358, 351]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[117]: text=17.7%, bbox=[375, 338, 417, 351]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[118]: text=0.96, bbox=[444, 338, 473, 351]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[119]: text=21.1%, bbox=[490, 338, 532, 351]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[120]: text=19.59, bbox=[548, 338, 588, 351]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[121]: text=1.03, bbox=[613, 338, 647, 351]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[122]: text=22.6%, bbox=[664, 338, 705, 351]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[123]: text=28.17, bbox=[722, 338, 763, 351]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[124]: text=1.12, bbox=[797, 338, 820, 351]
2026-08-06 02:23:51,468 INFO     29 [qwen-vl-text] coord item[125]: text=24.6%, bbox=[837, 338, 878, 351]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[126]: text=39.07, bbox=[895, 338, 934, 351]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[127]: text=MEF 50, bbox=[54, 351, 104, 364]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[128]: text=[L/s], bbox=[183, 351, 221, 364]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[129]: text=5.20, bbox=[265, 351, 300, 364]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[130]: text=1.00, bbox=[324, 351, 358, 364]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[131]: text=19.2%, bbox=[375, 351, 417, 364]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[132]: text=1.29, bbox=[444, 351, 473, 364]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[133]: text=24.8%, bbox=[490, 351, 532, 364]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[134]: text=29.25, bbox=[548, 351, 588, 364]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[135]: text=1.30, bbox=[613, 351, 647, 364]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[136]: text=24.9%, bbox=[664, 351, 705, 364]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[137]: text=29.87, bbox=[722, 351, 763, 364]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[138]: text=1.53, bbox=[797, 351, 820, 364]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[139]: text=29.3%, bbox=[837, 351, 878, 364]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[140]: text=52.75, bbox=[895, 351, 934, 364]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[141]: text=MEF 25, bbox=[54, 365, 104, 378]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[142]: text=[L/s], bbox=[183, 365, 221, 378]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[143]: text=2.32, bbox=[265, 365, 300, 378]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[144]: text=0.39, bbox=[324, 365, 358, 378]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[145]: text=16.7%, bbox=[375, 365, 417, 378]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[146]: text=0.38, bbox=[444, 365, 473, 378]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[147]: text=16.4%, bbox=[490, 365, 532, 378]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[148]: text=-1.68, bbox=[548, 365, 588, 378]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[149]: text=0.50, bbox=[613, 365, 647, 378]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[150]: text=21.6%, bbox=[664, 365, 705, 378]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[151]: text=29.78, bbox=[722, 365, 763, 378]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[152]: text=0.41, bbox=[797, 365, 820, 378]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[153]: text=17.9%, bbox=[837, 365, 878, 378]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[154]: text=7.18, bbox=[902, 365, 934, 378]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[155]: text=FET, bbox=[54, 378, 80, 391]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[156]: text=[s], bbox=[200, 378, 221, 391]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[157]: text=15.24, bbox=[320, 378, 358, 391]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[158]: text=6.42, bbox=[441, 378, 473, 391]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[159]: text=-57.87, bbox=[542, 378, 588, 391]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[160]: text=6.30, bbox=[613, 378, 647, 391]
2026-08-06 02:23:51,469 INFO     29 [qwen-vl-text] coord item[161]: text=-58.63, bbox=[715, 378, 763, 391]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[162]: text=6.55, bbox=[790, 378, 820, 391]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[163]: text=-57.05, bbox=[887, 378, 934, 391]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[164]: text=V backextrapolati, bbox=[54, 392, 225, 405]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[165]: text=[L/s], bbox=[183, 405, 221, 418]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[166]: text=0.07, bbox=[326, 392, 358, 405]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[167]: text=0.07, bbox=[441, 392, 473, 405]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[168]: text=0.89, bbox=[556, 392, 588, 405]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[169]: text=0.09, bbox=[613, 392, 647, 405]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[170]: text=17.79, bbox=[722, 392, 763, 405]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[171]: text=0.08, bbox=[790, 392, 820, 405]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[172]: text=6.12, bbox=[902, 392, 934, 405]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[173]: text=PIF, bbox=[54, 405, 80, 418]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[174]: text=7.03, bbox=[326, 405, 358, 418]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[175]: text=7.39, bbox=[441, 405, 473, 418]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[176]: text=5.19, bbox=[556, 405, 588, 418]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[177]: text=7.17, bbox=[613, 405, 647, 418]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[178]: text=1.99, bbox=[730, 405, 763, 418]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[179]: text=7.16, bbox=[790, 405, 820, 418]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[180]: text=1.91, bbox=[902, 405, 934, 418]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[181]: text=FIV1, bbox=[54, 419, 87, 432]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[182]: text=[L], bbox=[198, 419, 221, 432]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[183]: text=3.40, bbox=[326, 419, 358, 432]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[184]: text=3.76, bbox=[441, 419, 473, 432]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[185]: text=10.58, bbox=[548, 419, 588, 432]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[186]: text=3.68, bbox=[613, 419, 647, 432]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[187]: text=8.26, bbox=[730, 419, 763, 432]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[188]: text=3.60, bbox=[790, 419, 820, 432]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[189]: text=5.96, bbox=[902, 419, 934, 432]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[190]: text=PEF50 % PIF50, bbox=[54, 432, 162, 445]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[191]: text=[%], bbox=[198, 432, 221, 445]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[192]: text=16.56, bbox=[317, 432, 358, 445]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[193]: text=21.70, bbox=[435, 432, 473, 445]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[194]: text=31.06, bbox=[548, 432, 588, 445]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[195]: text=19.81, bbox=[606, 432, 647, 445]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[196]: text=19.65, bbox=[722, 432, 763, 445]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[197]: text=24.71, bbox=[781, 432, 820, 445]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[198]: text=49.20, bbox=[895, 432, 934, 445]
2026-08-06 02:23:51,470 INFO     29 [qwen-vl-text] coord item[199]: text=MVV, bbox=[54, 446, 80, 459]
2026-08-06 02:23:51,471 INFO     29 [qwen-vl-text] coord item[200]: text=[L/min], bbox=[168, 446, 221, 459]
2026-08-06 02:23:51,471 INFO     29 [qwen-vl-text] coord item[201]: text=142.69, bbox=[251, 446, 300, 459]
2026-08-06 02:23:51,471 INFO     29 [qwen-vl-text] coord item[202]: text=BF MVV, bbox=[54, 459, 104, 472]
2026-08-06 02:23:51,471 INFO     29 [qwen-vl-text] coord item[203]: text=[1/min], bbox=[168, 459, 221, 472]
2026-08-06 02:23:51,471 INFO     29 [qwen-vl-text] coord item[204]: text=意见：, bbox=[73, 789, 120, 803]
2026-08-06 02:23:51,471 INFO     29 [qwen-vl-text] coord item[205]: text=1.重度混合性肺通气功能障碍。, bbox=[73, 803, 292, 816]
2026-08-06 02:23:51,471 INFO     29 [qwen-vl-text] coord item[206]: text=2.支气管舒张试验阳性。, bbox=[73, 815, 244, 828]
2026-08-06 02:23:51,471 INFO     29 [qwen-vl-text] coord item[207]: text=（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后PEV1较基线增加大于12%，且绝对值增加大于200ml）, bbox=[80, 826, 800, 839]
2026-08-06 02:23:51,472 INFO     29 [qwen-vl-text] page=11 — 209/209 coords, api_time=52.3s
2026-08-06 02:23:51,473 INFO     29 [qwen-vl-text] new_positions (209):
[[11, 29.154999999999998, 94.00999999999999, 74.096, 82.51599999999999], [11, 111.265, 162.435, 74.096, 82.51599999999999], [11, 175.525, 203.48999999999998, 74.096, 82.51599999999999], [11, 218.36499999999998, 383.18, 87.568, 101.03999999999999], [11, 224.91, 376.03999999999996, 101.03999999999999, 114.512], [11, 113.645, 139.23, 121.24799999999999, 132.194], [11, 113.645, 147.56, 132.194, 143.14], [11, 113.645, 227.29, 143.14, 154.08599999999998], [11, 113.645, 213.01, 154.08599999999998, 165.03199999999998], [11, 113.645, 139.23, 165.03199999999998, 175.97799999999998], [11, 113.645, 157.07999999999998, 175.97799999999998, 186.924], [11, 297.5, 354.62, 120.40599999999999, 131.352], [11, 297.5, 340.34, 131.352, 142.298], [11, 297.5, 321.3, 142.298, 153.244], [11, 297.5, 321.3, 153.244, 164.19], [11, 297.5, 321.3, 164.19, 175.136], [11, 297.5, 321.3, 175.136, 186.082], [11, 157.67499999999998, 178.5, 194.50199999999998, 204.606], [11, 202.29999999999998, 213.01, 194.50199999999998, 204.606], [11, 223.125, 248.11499999999998, 194.50199999999998, 204.606], [11, 271.91499999999996, 281.435, 194.50199999999998, 204.606], [11, 291.55, 316.53999999999996, 194.50199999999998, 204.606], [11, 326.06, 349.85999999999996, 194.50199999999998, 204.606], [11, 374.84999999999997, 384.965, 194.50199999999998, 204.606], [11, 395.08, 419.47499999999997, 194.50199999999998, 204.606], [11, 429.59, 453.98499999999996, 194.50199999999998, 204.606], [11, 478.38, 487.9, 194.50199999999998, 204.606], [11, 498.015, 522.41, 194.50199999999998, 204.606], [11, 532.525, 555.73, 194.50199999999998, 204.606], [11, 32.129999999999995, 48.195, 216.394, 226.498], [11, 117.80999999999999, 131.495, 216.394, 227.34], [11, 157.67499999999998, 178.5, 216.394, 226.498], [11, 192.78, 213.01, 216.394, 226.498], [11, 223.125, 248.11499999999998, 216.394, 226.498], [11, 264.18, 281.435, 216.394, 226.498], [11, 291.55, 316.53999999999996, 216.394, 226.498], [11, 326.06, 349.85999999999996, 216.394, 226.498], [11, 364.73499999999996, 384.965, 216.394, 226.498], [11, 395.08, 419.47499999999997, 216.394, 226.498], [11, 429.59, 453.98499999999996, 216.394, 226.498], [11, 474.215, 487.9, 216.394, 226.498], [11, 498.015, 522.41, 216.394, 226.498], [11, 532.525, 555.73, 216.394, 226.498], [11, 32.129999999999995, 56.525, 227.34, 238.286], [11, 117.80999999999999, 131.495, 227.34, 238.286], [11, 157.67499999999998, 178.5, 227.34, 238.286], [11, 192.78, 213.01, 227.34, 238.286], [11, 192.78, 248.11499999999998, 227.34, 238.286], [11, 264.18, 281.435, 227.34, 238.286], [11, 291.55, 316.53999999999996, 227.34, 238.286], [11, 326.06, 349.85999999999996, 227.34, 238.286], [11, 364.73499999999996, 384.965, 227.34, 238.286], [11, 395.08, 419.47499999999997, 227.34, 238.286], [11, 429.59, 453.98499999999996, 227.34, 238.286], [11, 474.215, 487.9, 227.34, 238.286], [11, 474.215, 522.41, 227.34, 238.286], [11, 532.525, 555.73, 227.34, 238.286], [11, 32.129999999999995, 86.86999999999999, 239.128, 250.07399999999998], [11, 117.80999999999999, 131.495, 239.128, 250.07399999999998], [11, 153.51, 178.5, 239.128, 250.07399999999998], [11, 188.61499999999998, 213.01, 239.128, 250.07399999999998], [11, 223.125, 248.11499999999998, 239.128, 250.07399999999998], [11, 258.825, 281.435, 239.128, 250.07399999999998], [11, 291.55, 316.53999999999996, 239.128, 250.07399999999998], [11, 330.82, 349.85999999999996, 239.128, 250.07399999999998], [11, 360.57, 384.965, 239.128, 250.07399999999998], [11, 395.08, 419.47499999999997, 239.128, 250.07399999999998], [11, 429.59, 453.98499999999996, 239.128, 250.07399999999998], [11, 464.695, 487.9, 239.128, 250.07399999999998], [11, 498.015, 522.41, 239.128, 250.07399999999998], [11, 536.6899999999999, 555.73, 239.128, 250.07399999999998], [11, 32.129999999999995, 101.14999999999999, 250.07399999999998, 261.02], [11, 117.80999999999999, 131.495, 250.07399999999998, 261.02], [11, 153.51, 178.5, 250.07399999999998, 261.02], [11, 188.61499999999998, 213.01, 250.07399999999998, 261.02], [11, 223.125, 248.11499999999998, 250.07399999999998, 261.02], [11, 258.825, 281.435, 250.07399999999998, 261.02], [11, 291.55, 316.53999999999996, 250.07399999999998, 261.02], [11, 330.82, 349.85999999999996, 250.07399999999998, 261.02], [11, 360.57, 384.965, 250.07399999999998, 261.02], [11, 395.08, 419.47499999999997, 250.07399999999998, 261.02], [11, 434.34999999999997, 453.98499999999996, 250.07399999999998, 261.02], [11, 464.695, 487.9, 250.07399999999998, 261.02], [11, 498.015, 522.41, 250.07399999999998, 261.02], [11, 536.6899999999999, 555.73, 250.07399999999998, 261.02], [11, 32.129999999999995, 62.474999999999994, 261.02, 271.966], [11, 117.80999999999999, 131.495, 261.02, 271.966], [11, 157.67499999999998, 178.5, 261.02, 271.966], [11, 192.78, 213.01, 261.02, 271.966], [11, 223.125, 248.11499999999998, 261.02, 271.966], [11, 264.18, 281.435, 261.02, 271.966], [11, 291.55, 316.53999999999996, 261.02, 271.966], [11, 326.06, 349.85999999999996, 261.02, 271.966], [11, 364.73499999999996, 384.965, 261.02, 271.966], [11, 395.08, 419.47499999999997, 261.02, 271.966], [11, 429.59, 453.98499999999996, 261.02, 271.966], [11, 474.215, 487.9, 261.02, 271.966], [11, 498.015, 522.41, 261.02, 271.966], [11, 532.525, 555.73, 261.02, 271.966], [11, 32.129999999999995, 47.599999999999994, 272.808, 283.75399999999996], [11, 108.88499999999999, 131.495, 272.808, 283.75399999999996], [11, 157.67499999999998, 178.5, 272.808, 283.75399999999996], [11, 192.78, 213.01, 272.808, 283.75399999999996], [11, 223.125, 248.11499999999998, 272.808, 283.75399999999996], [11, 264.18, 281.435, 272.808, 283.75399999999996], [11, 291.55, 316.53999999999996, 272.808, 283.75399999999996], [11, 326.06, 349.85999999999996, 272.808, 283.75399999999996], [11, 364.73499999999996, 384.965, 272.808, 283.75399999999996], [11, 395.08, 419.47499999999997, 272.808, 283.75399999999996], [11, 429.59, 453.98499999999996, 272.808, 283.75399999999996], [11, 474.215, 487.9, 272.808, 283.75399999999996], [11, 498.015, 522.41, 272.808, 283.75399999999996], [11, 532.525, 555.73, 272.808, 283.75399999999996], [11, 32.129999999999995, 81.515, 284.596, 295.542], [11, 108.88499999999999, 131.495, 284.596, 295.542], [11, 157.67499999999998, 178.5, 284.596, 295.542], [11, 192.78, 213.01, 284.596, 295.542], [11, 223.125, 248.11499999999998, 284.596, 295.542], [11, 264.18, 281.435, 284.596, 295.542], [11, 291.55, 316.53999999999996, 284.596, 295.542], [11, 326.06, 349.85999999999996, 284.596, 295.542], [11, 364.73499999999996, 384.965, 284.596, 295.542], [11, 395.08, 419.47499999999997, 284.596, 295.542], [11, 429.59, 453.98499999999996, 284.596, 295.542], [11, 474.215, 487.9, 284.596, 295.542], [11, 498.015, 522.41, 284.596, 295.542], [11, 532.525, 555.73, 284.596, 295.542], [11, 32.129999999999995, 61.879999999999995, 295.542, 306.488], [11, 108.88499999999999, 131.495, 295.542, 306.488], [11, 157.67499999999998, 178.5, 295.542, 306.488], [11, 192.78, 213.01, 295.542, 306.488], [11, 223.125, 248.11499999999998, 295.542, 306.488], [11, 264.18, 281.435, 295.542, 306.488], [11, 291.55, 316.53999999999996, 295.542, 306.488], [11, 326.06, 349.85999999999996, 295.542, 306.488], [11, 364.73499999999996, 384.965, 295.542, 306.488], [11, 395.08, 419.47499999999997, 295.542, 306.488], [11, 429.59, 453.98499999999996, 295.542, 306.488], [11, 474.215, 487.9, 295.542, 306.488], [11, 498.015, 522.41, 295.542, 306.488], [11, 532.525, 555.73, 295.542, 306.488], [11, 32.129999999999995, 61.879999999999995, 307.33, 318.276], [11, 108.88499999999999, 131.495, 307.33, 318.276], [11, 157.67499999999998, 178.5, 307.33, 318.276], [11, 192.78, 213.01, 307.33, 318.276], [11, 223.125, 248.11499999999998, 307.33, 318.276], [11, 264.18, 281.435, 307.33, 318.276], [11, 291.55, 316.53999999999996, 307.33, 318.276], [11, 326.06, 349.85999999999996, 307.33, 318.276], [11, 364.73499999999996, 384.965, 307.33, 318.276], [11, 395.08, 419.47499999999997, 307.33, 318.276], [11, 429.59, 453.98499999999996, 307.33, 318.276], [11, 474.215, 487.9, 307.33, 318.276], [11, 498.015, 522.41, 307.33, 318.276], [11, 536.6899999999999, 555.73, 307.33, 318.276], [11, 32.129999999999995, 47.599999999999994, 318.276, 329.222], [11, 119.0, 131.495, 318.276, 329.222], [11, 190.39999999999998, 213.01, 318.276, 329.222], [11, 262.395, 281.435, 318.276, 329.222], [11, 322.49, 349.85999999999996, 318.276, 329.222], [11, 364.73499999999996, 384.965, 318.276, 329.222], [11, 425.42499999999995, 453.98499999999996, 318.276, 329.222], [11, 470.04999999999995, 487.9, 318.276, 329.222], [11, 527.765, 555.73, 318.276, 329.222], [11, 32.129999999999995, 133.875, 330.06399999999996, 341.01], [11, 108.88499999999999, 131.495, 341.01, 351.95599999999996], [11, 193.97, 213.01, 330.06399999999996, 341.01], [11, 262.395, 281.435, 330.06399999999996, 341.01], [11, 330.82, 349.85999999999996, 330.06399999999996, 341.01], [11, 364.73499999999996, 384.965, 330.06399999999996, 341.01], [11, 429.59, 453.98499999999996, 330.06399999999996, 341.01], [11, 470.04999999999995, 487.9, 330.06399999999996, 341.01], [11, 536.6899999999999, 555.73, 330.06399999999996, 341.01], [11, 32.129999999999995, 47.599999999999994, 341.01, 351.95599999999996], [11, 193.97, 213.01, 341.01, 351.95599999999996], [11, 262.395, 281.435, 341.01, 351.95599999999996], [11, 330.82, 349.85999999999996, 341.01, 351.95599999999996], [11, 364.73499999999996, 384.965, 341.01, 351.95599999999996], [11, 434.34999999999997, 453.98499999999996, 341.01, 351.95599999999996], [11, 470.04999999999995, 487.9, 341.01, 351.95599999999996], [11, 536.6899999999999, 555.73, 341.01, 351.95599999999996], [11, 32.129999999999995, 51.765, 352.798, 363.74399999999997], [11, 117.80999999999999, 131.495, 352.798, 363.74399999999997], [11, 193.97, 213.01, 352.798, 363.74399999999997], [11, 262.395, 281.435, 352.798, 363.74399999999997], [11, 326.06, 349.85999999999996, 352.798, 363.74399999999997], [11, 364.73499999999996, 384.965, 352.798, 363.74399999999997], [11, 434.34999999999997, 453.98499999999996, 352.798, 363.74399999999997], [11, 470.04999999999995, 487.9, 352.798, 363.74399999999997], [11, 536.6899999999999, 555.73, 352.798, 363.74399999999997], [11, 32.129999999999995, 96.39, 363.74399999999997, 374.69], [11, 117.80999999999999, 131.495, 363.74399999999997, 374.69], [11, 188.61499999999998, 213.01, 363.74399999999997, 374.69], [11, 258.825, 281.435, 363.74399999999997, 374.69], [11, 326.06, 349.85999999999996, 363.74399999999997, 374.69], [11, 360.57, 384.965, 363.74399999999997, 374.69], [11, 429.59, 453.98499999999996, 363.74399999999997, 374.69], [11, 464.695, 487.9, 363.74399999999997, 374.69], [11, 532.525, 555.73, 363.74399999999997, 374.69], [11, 32.129999999999995, 47.599999999999994, 375.532, 386.478], [11, 99.96, 131.495, 375.532, 386.478], [11, 149.345, 178.5, 375.532, 386.478], [11, 32.129999999999995, 61.879999999999995, 386.478, 397.424], [11, 99.96, 131.495, 386.478, 397.424], [11, 43.434999999999995, 71.39999999999999, 664.338, 676.126], [11, 43.434999999999995, 173.73999999999998, 676.126, 687.072], [11, 43.434999999999995, 145.18, 686.23, 697.1759999999999], [11, 47.599999999999994, 476.0, 695.492, 706.438], [11, 47.599999999999994, 476.0, 695.492, 706.438]]
2026-08-06 02:23:51,474 INFO     29 [qwen-vl-text] ═══ DONE ═══ 209 positions, pages=1, time=69.6s
2026-08-06 02:23:51,475 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 02:23:51,475 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-06 02:23:51,477 INFO     29 [qwen-vl-text] positions(2884): [[15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 02:23:51,482 INFO     29 [qwen-vl-text] page grouping: [15], lines per page: [2884]
2026-08-06 02:23:51,709 INFO     29 [qwen-vl-text] page=15, rect=595x842, img=(1653x2339), dpi=200
2026-08-06 02:23:51,710 INFO     29 [qwen-vl-text] LLM extraction start, text_len=13643
2026-08-06 02:23:51,710 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-06 02:23:51,711 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 794, \"bbox_end\": 3677, \"encounter_dates\": [\"2024-10-22\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "广州医科大学附属第三医院\n肺功能检查报告\n地址：广州市多宝路63号 电话：020-81292126\nCOSMED\n姓名：\n科室/床号：\nID：\n出生日期：1984/12/8\n预计值：ERS 93\n日期：2024/10/22\n性别：Male\n地区修正：Chinese\n详细描述：内科门诊\nCompany：\n年龄：39\n体重(Kg)：89.0\n身高(cm)：177.5\nBMI(Kg/m²：28.2\n吸烟：曾经(10/20)\n用力肺活量 Forced Vital Capacity\nF(l/s)\nV(l)\nBEST #3 - 2024/10/22 11:03\n沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38\n沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39\n沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41\n沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38\n沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39\n沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41\nBEST #3 - 2024/10/22 11:03\nFVC\nPEF\nMEF75%\nMEF50%\nMEF25%\nFVC\n6\n7\n8V(l)\nFEV1\nATS\n12t(s)\n-1\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n24\n25\n26\n27\n28\n29\n30\n31\n32\n33\n34\n35\n36\n37\n38\n39\n40\n41\n42\n43\n44\n45\n46\n47\n48\n49\n50\n51\n52\n53\n54\n55\n56\n57\n58\n59\n60\n61\n62\n63\n64\n65\n66\n67\n68\n69\n70\n71\n72\n73\n74\n75\n76\n77\n78\n79\n80\n81\n82\n83\n84\n85\n86\n87\n88\n89\n90\n91\n92\n93\n94\n95\n96\n97\n98\n99\n100\n101\n102\n103\n104\n105\n106\n107\n108\n109\n110\n111\n112\n113\n114\n115\n116\n117\n118\n119\n120\n121\n122\n123\n124\n125\n126\n127\n128\n129\n130\n131\n132\n133\n134\n135\n136\n137\n138\n139\n140\n141\n142\n143\n144\n145\n146\n147\n148\n149\n150\n151\n152\n153\n154\n155\n156\n157\n158\n159\n160\n161\n162\n163\n164\n165\n166\n167\n168\n169\n170\n171\n172\n173\n174\n175\n176\n177\n178\n179\n180\n181\n182\n183\n184\n185\n186\n187\n188\n189\n190\n191\n192\n193\n194\n195\n196\n197\n198\n199\n200\n201\n202\n203\n204\n205\n206\n207\n208\n209\n210\n211\n212\n213\n214\n215\n216\n217\n218\n219\n220\n221\n222\n223\n224\n225\n226\n227\n228\n229\n230\n231\n232\n233\n234\n235\n236\n237\n238\n239\n240\n241\n242\n243\n244\n245\n246\n247\n248\n249\n250\n251\n252\n253\n254\n255\n256\n257\n258\n259\n260\n261\n262\n263\n264\n265\n266\n267\n268\n269\n270\n271\n272\n273\n274\n275\n276\n277\n278\n279\n280\n281\n282\n283\n284\n285\n286\n287\n288\n289\n290\n291\n292\n293\n294\n295\n296\n297\n298\n299\n300\n301\n302\n303\n304\n305\n306\n307\n308\n309\n310\n311\n312\n313\n314\n315\n316\n317\n318\n319\n320\n321\n322\n323\n324\n325\n326\n327\n328\n329\n330\n331\n332\n333\n334\n335\n336\n337\n338\n339\n340\n341\n342\n343\n344\n345\n346\n347\n348\n349\n350\n351\n352\n353\n354\n355\n356\n357\n358\n359\n360\n361\n362\n363\n364\n365\n366\n367\n368\n369\n370\n371\n372\n373\n374\n375\n376\n377\n378\n379\n380\n381\n382\n383\n384\n385\n386\n387\n388\n389\n390\n391\n392\n393\n394\n395\n396\n397\n398\n399\n400\n401\n402\n403\n404\n405\n406\n407\n408\n409\n410\n411\n412\n413\n414\n415\n416\n417\n418\n419\n420\n421\n422\n423\n424\n425\n426\n427\n428\n429\n430\n431\n432\n433\n434\n435\n436\n437\n438\n439\n440\n441\n442\n443\n444\n445\n446\n447\n448\n449\n450\n451\n452\n453\n454\n455\n456\n457\n458\n459\n460\n461\n462\n463\n464\n465\n466\n467\n468\n469\n470\n471\n472\n473\n474\n475\n476\n477\n478\n479\n480\n481\n482\n483\n484\n485\n486\n487\n488\n489\n490\n491\n492\n493\n494\n495\n496\n497\n498\n499\n500\n501\n502\n503\n504\n505\n506\n507\n508\n509\n510\n511\n512\n513\n514\n515\n516\n517\n518\n519\n520\n521\n522\n523\n524\n525\n526\n527\n528\n529\n530\n531\n532\n533\n534\n535\n536\n537\n538\n539\n540\n541\n542\n543\n544\n545\n546\n547\n548\n549\n550\n551\n552\n553\n554\n555\n556\n557\n558\n559\n560\n561\n562\n563\n564\n565\n566\n567\n568\n569\n570\n571\n572\n573\n574\n575\n576\n577\n578\n579\n580\n581\n582\n583\n584\n585\n586\n587\n588\n589\n590\n591\n592\n593\n594\n595\n596\n597\n598\n599\n600\n601\n602\n603\n604\n605\n606\n607\n608\n609\n610\n611\n612\n613\n614\n615\n616\n617\n618\n619\n620\n621\n622\n623\n624\n625\n626\n627\n628\n629\n630\n631\n632\n633\n634\n635\n636\n637\n638\n639\n640\n641\n642\n643\n644\n645\n646\n647\n648\n649\n650\n651\n652\n653\n654\n655\n656\n657\n658\n659\n660\n661\n662\n663\n664\n665\n666\n667\n668\n669\n670\n671\n672\n673\n674\n675\n676\n677\n678\n679\n680\n681\n682\n683\n684\n685\n686\n687\n688\n689\n690\n691\n692\n693\n694\n695\n696\n697\n698\n699\n700\n701\n702\n703\n704\n705\n706\n707\n708\n709\n710\n711\n712\n713\n714\n715\n716\n717\n718\n719\n720\n721\n722\n723\n724\n725\n726\n727\n728\n729\n730\n731\n732\n733\n734\n735\n736\n737\n738\n739\n740\n741\n742\n743\n744\n745\n746\n747\n748\n749\n750\n751\n752\n753\n754\n755\n756\n757\n758\n759\n760\n761\n762\n763\n764\n765\n766\n767\n768\n769\n770\n771\n772\n773\n774\n775\n776\n777\n778\n779\n780\n781\n782\n783\n784\n785\n786\n787\n788\n789\n790\n791\n792\n793\n794\n795\n796\n797\n798\n799\n800\n801\n802\n803\n804\n805\n806\n807\n808\n809\n810\n811\n812\n813\n814\n815\n816\n817\n818\n819\n820\n821\n822\n823\n824\n825\n826\n827\n828\n829\n830\n831\n832\n833\n834\n835\n836\n837\n838\n839\n840\n841\n842\n843\n844\n845\n846\n847\n848\n849\n850\n851\n852\n853\n854\n855\n856\n857\n858\n859\n860\n861\n862\n863\n864\n865\n866\n867\n868\n869\n870\n871\n872\n873\n874\n875\n876\n877\n878\n879\n880\n881\n882\n883\n884\n885\n886\n887\n888\n889\n890\n891\n892\n893\n894\n895\n896\n897\n898\n899\n900\n901\n902\n903\n904\n905\n906\n907\n908\n909\n910\n911\n912\n913\n914\n915\n916\n917\n918\n919\n920\n921\n922\n923\n924\n925\n926\n927\n928\n929\n930\n931\n932\n933\n934\n935\n936\n937\n938\n939\n940\n941\n942\n943\n944\n945\n946\n947\n948\n949\n950\n951\n952\n953\n954\n955\n956\n957\n958\n959\n960\n961\n962\n963\n964\n965\n966\n967\n968\n969\n970\n971\n972\n973\n974\n975\n976\n977\n978\n979\n980\n981\n982\n983\n984\n985\n986\n987\n988\n989\n990\n991\n992\n993\n994\n995\n996\n997\n998\n999\n1000\n1001\n1002\n1003\n1004\n1005\n1006\n1007\n1008\n1009\n1010\n1011\n1012\n1013\n1014\n1015\n1016\n1017\n1018\n1019\n1020\n1021\n1022\n1023\n1024\n1025\n1026\n1027\n1028\n1029\n1030\n1031\n1032\n1033\n1034\n1035\n1036\n1037\n1038\n1039\n1040\n1041\n1042\n1043\n1044\n1045\n1046\n1047\n1048\n1049\n1050\n1051\n1052\n1053\n1054\n1055\n1056\n1057\n1058\n1059\n1060\n1061\n1062\n1063\n1064\n1065\n1066\n1067\n1068\n1069\n1070\n1071\n1072\n1073\n1074\n1075\n1076\n1077\n1078\n1079\n1080\n1081\n1082\n1083\n1084\n1085\n1086\n1087\n1088\n1089\n1090\n1091\n1092\n1093\n1094\n1095\n1096\n1097\n1098\n1099\n1100\n1101\n1102\n1103\n1104\n1105\n1106\n1107\n1108\n1109\n1110\n1111\n1112\n1113\n1114\n1115\n1116\n1117\n1118\n1119\n1120\n1121\n1122\n1123\n1124\n1125\n1126\n1127\n1128\n1129\n1130\n1131\n1132\n1133\n1134\n1135\n1136\n1137\n1138\n1139\n1140\n1141\n1142\n1143\n1144\n1145\n1146\n1147\n1148\n1149\n1150\n1151\n1152\n1153\n1154\n1155\n1156\n1157\n1158\n1159\n1160\n1161\n1162\n1163\n1164\n1165\n1166\n1167\n1168\n1169\n1170\n1171\n1172\n1173\n1174\n1175\n1176\n1177\n1178\n1179\n1180\n1181\n1182\n1183\n1184\n1185\n1186\n1187\n1188\n1189\n1190\n1191\n1192\n1193\n1194\n1195\n1196\n1197\n1198\n1199\n1200\n1201\n1202\n1203\n1204\n1205\n1206\n1207\n1208\n1209\n1210\n1211\n1212\n1213\n1214\n1215\n1216\n1217\n1218\n1219\n1220\n1221\n1222\n1223\n1224\n1225\n1226\n1227\n1228\n1229\n1230\n1231\n1232\n1233\n1234\n1235\n1236\n1237\n1238\n1239\n1240\n1241\n1242\n1243\n1244\n1245\n1246\n1247\n1248\n1249\n1250\n1251\n1252\n1253\n1254\n1255\n1256\n1257\n1258\n1259\n1260\n1261\n1262\n1263\n1264\n1265\n1266\n1267\n1268\n1269\n1270\n1271\n1272\n1273\n1274\n1275\n1276\n1277\n1278\n1279\n1280\n1281\n1282\n1283\n1284\n1285\n1286\n1287\n1288\n1289\n1290\n1291\n1292\n1293\n1294\n1295\n1296\n1297\n1298\n1299\n1300\n1301\n1302\n1303\n1304\n1305\n1306\n1307\n1308\n1309\n1310\n1311\n1312\n1313\n1314\n1315\n1316\n1317\n1318\n1319\n1320\n1321\n1322\n1323\n1324\n1325\n1326\n1327\n1328\n1329\n1330\n1331\n1332\n1333\n1334\n1335\n1336\n1337\n1338\n1339\n1340\n1341\n1342\n1343\n1344\n1345\n1346\n1347\n1348\n1349\n1350\n1351\n1352\n1353\n1354\n1355\n1356\n1357\n1358\n1359\n1360\n1361\n1362\n1363\n1364\n1365\n1366\n1367\n1368\n1369\n1370\n1371\n1372\n1373\n1374\n1375\n1376\n1377\n1378\n1379\n1380\n1381\n1382\n1383\n1384\n1385\n1386\n1387\n1388\n1389\n1390\n1391\n1392\n1393\n1394\n1395\n1396\n1397\n1398\n1399\n1400\n1401\n1402\n1403\n1404\n1405\n1406\n1407\n1408\n1409\n1410\n1411\n1412\n1413\n1414\n1415\n1416\n1417\n1418\n1419\n1420\n1421\n1422\n1423\n1424\n1425\n1426\n1427\n1428\n1429\n1430\n1431\n1432\n1433\n1434\n1435\n1436\n1437\n1438\n1439\n1440\n1441\n1442\n1443\n1444\n1445\n1446\n1447\n1448\n1449\n1450\n1451\n1452\n1453\n1454\n1455\n1456\n1457\n1458\n1459\n1460\n1461\n1462\n1463\n1464\n1465\n1466\n1467\n1468\n1469\n1470\n1471\n1472\n1473\n1474\n1475\n1476\n1477\n1478\n1479\n1480\n1481\n1482\n1483\n1484\n1485\n1486\n1487\n1488\n1489\n1490\n1491\n1492\n1493\n1494\n1495\n1496\n1497\n1498\n1499\n1500\n1501\n1502\n1503\n1504\n1505\n1506\n1507\n1508\n1509\n1510\n1511\n1512\n1513\n1514\n1515\n1516\n1517\n1518\n1519\n1520\n1521\n1522\n1523\n1524\n1525\n1526\n1527\n1528\n1529\n1530\n1531\n1532\n1533\n1534\n1535\n1536\n1537\n1538\n1539\n1540\n1541\n1542\n1543\n1544\n1545\n1546\n1547\n1548\n1549\n1550\n1551\n1552\n1553\n1554\n1555\n1556\n1557\n1558\n1559\n1560\n1561\n1562\n1563\n1564\n1565\n1566\n1567\n1568\n1569\n1570\n1571\n1572\n1573\n1574\n1575\n1576\n1577\n1578\n1579\n1580\n1581\n1582\n1583\n1584\n1585\n1586\n1587\n1588\n1589\n1590\n1591\n1592\n1593\n1594\n1595\n1596\n1597\n1598\n1599\n1600\n1601\n1602\n1603\n1604\n1605\n1606\n1607\n1608\n1609\n1610\n1611\n1612\n1613\n1614\n1615\n1616\n1617\n1618\n1619\n1620\n1621\n1622\n1623\n1624\n1625\n1626\n1627\n1628\n1629\n1630\n1631\n1632\n1633\n1634\n1635\n1636\n1637\n1638\n1639\n1640\n1641\n1642\n1643\n1644\n1645\n1646\n1647\n1648\n1649\n1650\n1651\n1652\n1653\n1654\n1655\n1656\n1657\n1658\n1659\n1660\n1661\n1662\n1663\n1664\n1665\n1666\n1667\n1668\n1669\n1670\n1671\n1672\n1673\n1674\n1675\n1676\n1677\n1678\n1679\n1680\n1681\n1682\n1683\n1684\n1685\n1686\n1687\n1688\n1689\n1690\n1691\n1692\n1693\n1694\n1695\n1696\n1697\n1698\n1699\n1700\n1701\n1702\n1703\n1704\n1705\n1706\n1707\n1708\n1709\n1710\n1711\n1712\n1713\n1714\n1715\n1716\n1717\n1718\n1719\n1720\n1721\n1722\n1723\n1724\n1725\n1726\n1727\n1728\n1729\n1730\n1731\n1732\n1733\n1734\n1735\n1736\n1737\n1738\n1739\n1740\n1741\n1742\n1743\n1744\n1745\n1746\n1747\n1748\n1749\n1750\n1751\n1752\n1753\n1754\n1755\n1756\n1757\n1758\n1759\n1760\n1761\n1762\n1763\n1764\n1765\n1766\n1767\n1768\n1769\n1770\n1771\n1772\n1773\n1774\n1775\n1776\n1777\n1778\n1779\n1780\n1781\n1782\n1783\n1784\n1785\n1786\n1787\n1788\n1789\n1790\n1791\n1792\n1793\n1794\n1795\n1796\n1797\n1798\n1799\n1800\n1801\n1802\n1803\n1804\n1805\n1806\n1807\n1808\n1809\n1810\n1811\n1812\n1813\n1814\n1815\n1816\n1817\n1818\n1819\n1820\n1821\n1822\n1823\n1824\n1825\n1826\n1827\n1828\n1829\n1830\n1831\n1832\n1833\n1834\n1835\n1836\n1837\n1838\n1839\n1840\n1841\n1842\n1843\n1844\n1845\n1846\n1847\n1848\n1849\n1850\n1851\n1852\n1853\n1854\n1855\n1856\n1857\n1858\n1859\n1860\n1861\n1862\n1863\n1864\n1865\n1866\n1867\n1868\n1869\n1870\n1871\n1872\n1873\n1874\n1875\n1876\n1877\n1878\n1879\n1880\n1881\n1882\n1883\n1884\n1885\n1886\n1887\n1888\n1889\n1890\n1891\n1892\n1893\n1894\n1895\n1896\n1897\n1898\n1899\n1900\n1901\n1902\n1903\n1904\n1905\n1906\n1907\n1908\n1909\n1910\n1911\n1912\n1913\n1914\n1915\n1916\n1917\n1918\n1919\n1920\n1921\n1922\n1923\n1924\n1925\n1926\n1927\n1928\n1929\n1930\n1931\n1932\n1933\n1934\n1935\n1936\n1937\n1938\n1939\n1940\n1941\n1942\n1943\n1944\n1945\n1946\n1947\n1948\n1949\n1950\n1951\n1952\n1953\n1954\n1955\n1956\n1957\n1958\n1959\n1960\n1961\n1962\n1963\n1964\n1965\n1966\n1967\n1968\n1969\n1970\n1971\n1972\n1973\n1974\n1975\n1976\n1977\n1978\n1979\n1980\n1981\n1982\n1983\n1984\n1985\n1986\n1987\n1988\n1989\n1990\n1991\n1992\n1993\n1994\n1995\n1996\n1997\n1998\n1999\n2000\n2001\n2002\n2003\n2004\n2005\n2006\n2007\n2008\n2009\n2010\n2011\n2012\n2013\n2014\n2015\n2016\n2017\n2018\n2019\n2020\n2021\n2022\n2023\n2024\n2025\n2026\n2027\n2028\n2029\n2030\n2031\n2032\n2033\n2034\n2035\n2036\n2037\n2038\n2039\n2040\n2041\n2042\n2043\n2044\n2045\n2046\n2047\n2048\n2049\n2050\n2051\n2052\n2053\n2054\n2055\n2056\n2057\n2058\n2059\n2060\n2061\n2062\n2063\n2064\n2065\n2066\n2067\n2068\n2069\n2070\n2071\n2072\n2073\n2074\n2075\n2076\n2077\n2078\n2079\n2080\n2081\n2082\n2083\n2084\n2085\n2086\n2087\n2088\n2089\n2090\n2091\n2092\n2093\n2094\n2095\n2096\n2097\n2098\n2099\n2100\n2101\n2102\n2103\n2104\n2105\n2106\n2107\n2108\n2109\n2110\n2111\n2112\n2113\n2114\n2115\n2116\n2117\n2118\n2119\n2120\n2121\n2122\n2123\n2124\n2125\n2126\n2127\n2128\n2129\n2130\n2131\n2132\n2133\n2134\n2135\n2136\n2137\n2138\n2139\n2140\n2141\n2142\n2143\n2144\n2145\n2146\n2147\n2148\n2149\n2150\n2151\n2152\n2153\n2154\n2155\n2156\n2157\n2158\n2159\n2160\n2161\n2162\n2163\n2164\n2165\n2166\n2167\n2168\n2169\n2170\n2171\n2172\n2173\n2174\n2175\n2176\n2177\n2178\n2179\n2180\n2181\n2182\n2183\n2184\n2185\n2186\n2187\n2188\n2189\n2190\n2191\n2192\n2193\n2194\n2195\n2196\n2197\n2198\n2199\n2200\n2201\n2202\n2203\n2204\n2205\n2206\n2207\n2208\n2209\n2210\n2211\n2212\n2213\n2214\n2215\n2216\n2217\n2218\n2219\n2220\n2221\n2222\n2223\n2224\n2225\n2226\n2227\n2228\n2229\n2230\n2231\n2232\n2233\n2234\n2235\n2236\n2237\n2238\n2239\n2240\n2241\n2242\n2243\n2244\n2245\n2246\n2247\n2248\n2249\n2250\n2251\n2252\n2253\n2254\n2255\n2256\n2257\n2258\n2259\n2260\n2261\n2262\n2263\n2264\n2265\n2266\n2267\n2268\n2269\n2270\n2271\n2272\n2273\n2274\n2275\n2276\n2277\n2278\n2279\n2280\n2281\n2282\n2283\n2284\n2285\n2286\n2287\n2288\n2289\n2290\n2291\n2292\n2293\n2294\n2295\n2296\n2297\n2298\n2299\n2300\n2301\n2302\n2303\n2304\n2305\n2306\n2307\n2308\n2309\n2310\n2311\n2312\n2313\n2314\n2315\n2316\n2317\n2318\n2319\n2320\n2321\n2322\n2323\n2324\n2325\n2326\n2327\n2328\n2329\n2330\n2331\n2332\n2333\n2334\n2335\n2336\n2337\n2338\n2339\n2340\n2341\n2342\n2343\n2344\n2345\n2346\n2347\n2348\n2349\n2350\n2351\n2352\n2353\n2354\n2355\n2356\n2357\n2358\n2359\n2360\n2361\n2362\n2363\n2364\n2365\n2366\n2367\n2368\n2369\n2370\n2371\n2372\n2373\n2374\n2375\n2376\n2377\n2378\n2379\n2380\n2381\n2382\n2383\n2384\n2385\n2386\n2387\n2388\n2389\n2390\n2391\n2392\n2393\n2394\n2395\n2396\n2397\n2398\n2399\n2400\n2401\n2402\n2403\n2404\n2405\n2406\n2407\n2408\n2409\n2410\n2411\n2412\n2413\n2414\n2415\n2416\n2417\n2418\n2419\n2420\n2421\n2422\n2423\n2424\n2425\n2426\n2427\n2428\n2429\n2430\n2431\n2432\n2433\n2434\n2435\n2436\n2437\n2438\n2439\n2440\n2441\n2442\n2443\n2444\n2445\n2446\n2447\n2448\n2449\n2450\n2451\n2452\n2453\n2454\n2455\n2456\n2457\n2458\n2459\n2460\n2461\n2462\n2463\n2464\n2465\n2466\n2467\n2468\n2469\n2470\n2471\n2472\n2473\n2474\n2475\n2476\n2477\n2478\n2479\n2480\n2481\n2482\n2483\n2484\n2485\n2486\n2487\n2488\n2489\n2490\n2491\n2492\n2493\n2494\n2495\n2496\n2497\n2498\n2499\n2500\n2501\n2502\n2503\n2504\n2505\n2506\n2507\n2508\n2509\n2510\n2511\n2512\n2513\n2514\n2515\n2516\n2517\n2518\n2519\n2520\n2521\n2522\n2523\n2524\n2525\n2526\n2527\n2528\n2529\n2530\n2531\n2532\n2533\n2534\n2535\n2536\n2537\n2538\n2539\n2540\n2541\n2542\n2543\n2544\n2545\n2546\n2547\n2548\n2549\n2550\n2551\n2552\n2553\n2554\n2555\n2556\n2557\n2558\n2559\n2560\n2561\n2562\n2563\n2564\n2565\n2566\n2567\n2568\n2569\n2570\n2571\n2572\n2573\n2574\n2575\n2576\n2577\n2578\n2579\n2580\n2581\n2582\n2583\n2584\n2585\n2586\n2587\n2588\n2589\n2590\n2591\n2592\n2593\n2594\n2595\n2596\n2597\n2598\n2599\n2600\n2601\n2602\n2603\n2604\n2605\n2606\n2607\n2608\n2609\n2610\n2611\n2612\n2613\n2614\n2615\n2616\n2617\n2618\n2619\n2620\n2621\n2622\n2623\n2624\n2625\n2626\n2627\n2628\n2629\n2630\n2631\n2632\n2633\n2634\n2635\n2636\n2637\n2638\n2639\n2640\n2641\n2642\n2643\n2644\n2645\n2646\n2647\n2648\n2649\n2650\n2651\n2652\n2653\n2654\n2655\n2656\n2657\n2658\n2659\n2660\n2661\n2662\n2663\n2664\n2665\n2666\n2667\n2668\n2669\n2670\n2671\n2672\n2673\n2674\n2675\n2676\n2677\n2678\n2679\n2680\n2681\n2682\n2683\n2684\n2685\n2686\n2687\n2688\n2689\n2690\n2691\n2692\n2693\n2694\n2695\n2696\n2697\n2698\n2699\n2700\n2701\n2702\n2703\n2704\n2705\n2706\n2707\n2708\n2709\n2710\n2711\n2712\n2713\n2714\n2715\n2716\n2717\n2718\n2719\n2720\n2721\n2722\n2723\n2724\n2725\n2726\n2727\n2728\n2729\n2730\n2731\n2732\n2733\n2734\n2735\n2736\n2737\n2738\n2739\n2740\n2741\n2742\n2743\n2744\n2745\n2746\n2747\n2748\n2749\n2750\n2751\n2752\n2753\n2754\n2755\n2756\n2757\n2758\n2759\n2760\n2761\n2762\n2763\n2764\n2765\n2766\n2767\n2768\n2769\n2770\n2771\n2772\n2773\n2774\n2775\n2776\n2777\n2778\n2779\n2780\n2781\n2782\n2783\n2784\n2785\n2786\n2787\n2788\n2789\n2790\n2791\n2792\n2793\n2794\n2795\n2796\n2797\n2798\n2799\n2800\n2801\n2802\n2803\n2804\n2805\n2806\n2807\n2808\n2809\n2810\n2811\n2812\n2813\n2814",
    "role": "user"
  }
]
[92m02:23:51 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:23:51,712 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-06 02:23:51,714 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T02:23:51.712+00:00", "boot_at": "2026-08-06T01:59:43.412+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"5d401ece913c11f19b5e81513a69a703": {"id": "5d401ece913c11f19b5e81513a69a703", "doc_id": "5963bc44913b11f19b5e81513a69a703", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785982387379, "task_type": "dataflow", "root_trace_id": "7886908ae2584ba69682631c2a66f747", "root_traceparent": "00-7886908ae2584ba69682631c2a66f747-971004a6101741b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 02:23:58,027 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-06 02:23:58,027 INFO     29 [qwen-vl-text] LLM output (len=718):
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
  "findings": "用力肺活量 Forced Vital Capacity\nF(l/s)\nV(l)\nBEST #3 - 2024/10/22 11:03\n沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38\n沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39\n沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41\n沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38\n沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39\n沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41\nBEST #3 - 2024/10/22 11:03\nFVC\nPEF\nMEF75%\nMEF50%\nMEF25%\nFVC\nFEV1\nATS",
  "conclusion": null,
  "physician": null,
  "reviewer": null
}
2026-08-06 02:23:58,030 INFO     29 [qwen-vl-text] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1606814, prompt_len=22910
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共2884行）
["广州医科大学附属第三医院", "肺功能检查报告", "地址：广州市多宝路63号 电话：020-81292126", "COSMED", "姓名：", "科室/床号：", "ID：", "出生日期：1984/12/8", "预计值：ERS 93", "日期：2024/10/22", "性别：Male", "地区修正：Chinese", "详细描述：内科门诊", "Company：", "年龄：39", "体重(Kg)：89.0", "身高(cm)：177.5", "BMI(Kg/m²：28.2", "吸烟：曾经(10/20)", "用力肺活量 Forced Vital Capacity", "F(l/s)", "V(l)", "BEST #3 - 2024/10/22 11:03", "沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38", "沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39", "沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41", "沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38", "沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39", "沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41", "BEST #3 - 2024/10/22 11:03", "FVC", "PEF", "MEF75%", "MEF50%", "MEF25%", "FVC", "6", "7", "8V(l)", "FEV1", "ATS", "12t(s)", "-1", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120", "121", "122", "123", "124", "125", "126", "127", "128", "129", "130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "140", "141", "142", "143", "144", "145", "146", "147", "148", "149", "150", "151", "152", "153", "154", "155", "156", "157", "158", "159", "160", "161", "162", "163", "164", "165", "166", "167", "168", "169", "170", "171", "172", "173", "174", "175", "176", "177", "178", "179", "180", "181", "182", "183", "184", "185", "186", "187", "188", "189", "190", "191", "192", "193", "194", "195", "196", "197", "198", "199", "200", "201", "202", "203", "204", "205", "206", "207", "208", "209", "210", "211", "212", "213", "214", "215", "216", "217", "218", "219", "220", "221", "222", "223", "224", "225", "226", "227", "228", "229", "230", "231", "232", "233", "234", "235", "236", "237", "238", "239", "240", "241", "242", "243", "244", "245", "246", "247", "248", "249", "250", "251", "252", "253", "254", "255", "256", "257", "258", "259", "260", "261", "262", "263", "264", "265", "266", "267", "268", "269", "270", "271", "272", "273", "274", "275", "276", "277", "278", "279", "280", "281", "282", "283", "284", "285", "286", "287", "288", "289", "290", "291", "292", "293", "294", "295", "296", "297", "298", "299", "300", "301", "302", "303", "304", "305", "306", "307", "308", "309", "310", "311", "312", "313", "314", "315", "316", "317", "318", "319", "320", "321", "322", "323", "324", "325", "326", "327", "328", "329", "330", "331", "332", "333", "334", "335", "336", "337", "338", "339", "340", "341", "342", "343", "344", "345", "346", "347", "348", "349", "350", "351", "352", "353", "354", "355", "356", "357", "358", "359", "360", "361", "362", "363", "364", "365", "366", "367", "368", "369", "370", "371", "372", "373", "374", "375", "376", "377", "378", "379", "380", "381", "382", "383", "384", "385", "386", "387", "388", "389", "390", "391", "392", "393", "394", "395", "396", "397", "398", "399", "400", "401", "402", "403", "404", "405", "406", "407", "408", "409", "410", "411", "412", "413", "414", "415", "416", "417", "418", "419", "420", "421", "422", "423", "424", "425", "426", "427", "428", "429", "430", "431", "432", "433", "434", "435", "436", "437", "438", "439", "440", "441", "442", "443", "444", "445", "446", "447", "448", "449", "450", "451", "452", "453", "454", "455", "456", "457", "458", "459", "460", "461", "462", "463", "464", "465", "466", "467", "468", "469", "470", "471", "472", "473", "474", "475", "476", "477", "478", "479", "480", "481", "482", "483", "484", "485", "486", "487", "488", "489", "490", "491", "492", "493", "494", "495", "496", "497", "498", "499", "500", "501", "502", "503", "504", "505", "506", "507", "508", "509", "510", "511", "512", "513", "514", "515", "516", "517", "518", "519", "520", "521", "522", "523", "524", "525", "526", "527", "528", "529", "530", "531", "532", "533", "534", "535", "536", "537", "538", "539", "540", "541", "542", "543", "544", "545", "546", "547", "548", "549", "550", "551", "552", "553", "554", "555", "556", "557", "558", "559", "560", "561", "562", "563", "564", "565", "566", "567", "568", "569", "570", "571", "572", "573", "574", "575", "576", "577", "578", "579", "580", "581", "582", "583", "584", "585", "586", "587", "588", "589", "590", "591", "592", "593", "594", "595", "596", "597", "598", "599", "600", "601", "602", "603", "604", "605", "606", "607", "608", "609", "610", "611", "612", "613", "614", "615", "616", "617", "618", "619", "620", "621", "622", "623", "624", "625", "626", "627", "628", "629", "630", "631", "632", "633", "634", "635", "636", "637", "638", "639", "640", "641", "642", "643", "644", "645", "646", "647", "648", "649", "650", "651", "652", "653", "654", "655", "656", "657", "658", "659", "660", "661", "662", "663", "664", "665", "666", "667", "668", "669", "670", "671", "672", "673", "674", "675", "676", "677", "678", "679", "680", "681", "682", "683", "684", "685", "686", "687", "688", "689", "690", "691", "692", "693", "694", "695", "696", "697", "698", "699", "700", "701", "702", "703", "704", "705", "706", "707", "708", "709", "710", "711", "712", "713", "714", "715", "716", "717", "718", "719", "720", "721", "722", "723", "724", "725", "726", "727", "728", "729", "730", "731", "732", "733", "734", "735", "736", "737", "738", "739", "740", "741", "742", "743", "744", "745", "746", "747", "748", "749", "750", "751", "752", "753", "754", "755", "756", "757", "758", "759", "760", "761", "762", "763", "764", "765", "766", "767", "768", "769", "770", "771", "772", "773", "774", "775", "776", "777", "778", "779", "780", "781", "782", "783", "784", "785", "786", "787", "788", "789", "790", "791", "792", "793", "794", "795", "796", "797", "798", "799", "800", "801", "802", "803", "804", "805", "806", "807", "808", "809", "810", "811", "812", "813", "814", "815", "816", "817", "818", "819", "820", "821", "822", "823", "824", "825", "826", "827", "828", "829", "830", "831", "832", "833", "834", "835", "836", "837", "838", "839", "840", "841", "842", "843", "844", "845", "846", "847", "848", "849", "850", "851", "852", "853", "854", "855", "856", "857", "858", "859", "860", "861", "862", "863", "864", "865", "866", "867", "868", "869", "870", "871", "872", "873", "874", "875", "876", "877", "878", "879", "880", "881", "882", "883", "884", "885", "886", "887", "888", "889", "890", "891", "892", "893", "894", "895", "896", "897", "898", "899", "900", "901", "902", "903", "904", "905", "906", "907", "908", "909", "910", "911", "912", "913", "914", "915", "916", "917", "918", "919", "920", "921", "922", "923", "924", "925", "926", "927", "928", "929", "930", "931", "932", "933", "934", "935", "936", "937", "938", "939", "940", "941", "942", "943", "944", "945", "946", "947", "948", "949", "950", "951", "952", "953", "954", "955", "956", "957", "958", "959", "960", "961", "962", "963", "964", "965", "966", "967", "968", "969", "970", "971", "972", "973", "974", "975", "976", "977", "978", "979", "980", "981", "982", "983", "984", "985", "986", "987", "988", "989", "990", "991", "992", "993", "994", "995", "996", "997", "998", "999", "1000", "1001", "1002", "1003", "1004", "1005", "1006", "1007", "1008", "1009", "1010", "1011", "1012", "1013", "1014", "1015", "1016", "1017", "1018", "1019", "1020", "1021", "1022", "1023", "1024", "1025", "1026", "1027", "1028", "1029", "1030", "1031", "1032", "1033", "1034", "1035", "1036", "1037", "1038", "1039", "1040", "1041", "1042", "1043", "1044", "1045", "1046", "1047", "1048", "1049", "1050", "1051", "1052", "1053", "1054", "1055", "1056", "1057", "1058", "1059", "1060", "1061", "1062", "1063", "1064", "1065", "1066", "1067", "1068", "1069", "1070", "1071", "1072", "1073", "1074", "1075", "1076", "1077", "1078", "1079", "1080", "1081", "1082", "1083", "1084", "1085", "1086", "1087", "1088", "1089", "1090", "1091", "1092", "1093", "1094", "1095", "1096", "1097", "1098", "1099", "1100", "1101", "1102", "1103", "1104", "1105", "1106", "1107", "1108", "1109", "1110", "1111", "1112", "1113", "1114", "1115", "1116", "1117", "1118", "1119", "1120", "1121", "1122", "1123", "1124", "1125", "1126", "1127", "1128", "1129", "1130", "1131", "1132", "1133", "1134", "1135", "1136", "1137", "1138", "1139", "1140", "1141", "1142", "1143", "1144", "1145", "1146", "1147", "1148", "1149", "1150", "1151", "1152", "1153", "1154", "1155", "1156", "1157", "1158", "1159", "1160", "1161", "1162", "1163", "1164", "1165", "1166", "1167", "1168", "1169", "1170", "1171", "1172", "1173", "1174", "1175", "1176", "1177", "1178", "1179", "1180", "1181", "1182", "1183", "1184", "1185", "1186", "1187", "1188", "1189", "1190", "1191", "1192", "1193", "1194", "1195", "1196", "1197", "1198", "1199", "1200", "1201", "1202", "1203", "1204", "1205", "1206", "1207", "1208", "1209", "1210", "1211", "1212", "1213", "1214", "1215", "1216", "1217", "1218", "1219", "1220", "1221", "1222", "1223", "1224", "1225", "1226", "1227", "1228", "1229", "1230", "1231", "1232", "1233", "1234", "1235", "1236", "1237", "1238", "1239", "1240", "1241", "1242", "1243", "1244", "1245", "1246", "1247", "1248", "1249", "1250", "1251", "1252", "1253", "1254", "1255", "1256", "1257", "1258", "1259", "1260", "1261", "1262", "1263", "1264", "1265", "1266", "1267", "1268", "1269", "1270", "1271", "1272", "1273", "1274", "1275", "1276", "1277", "1278", "1279", "1280", "1281", "1282", "1283", "1284", "1285", "1286", "1287", "1288", "1289", "1290", "1291", "1292", "1293", "1294", "1295", "1296", "1297", "1298", "1299", "1300", "1301", "1302", "1303", "1304", "1305", "1306", "1307", "1308", "1309", "1310", "1311", "1312", "1313", "1314", "1315", "1316", "1317", "1318", "1319", "1320", "1321", "1322", "1323", "1324", "1325", "1326", "1327", "1328", "1329", "1330", "1331", "1332", "1333", "1334", "1335", "1336", "1337", "1338", "1339", "1340", "1341", "1342", "1343", "1344", "1345", "1346", "1347", "1348", "1349", "1350", "1351", "1352", "1353", "1354", "1355", "1356", "1357", "1358", "1359", "1360", "1361", "1362", "1363", "1364", "1365", "1366", "1367", "1368", "1369", "1370", "1371", "1372", "1373", "1374", "1375", "1376", "1377", "1378", "1379", "1380", "1381", "1382", "1383", "1384", "1385", "1386", "1387", "1388", "1389", "1390", "1391", "1392", "1393", "1394", "1395", "1396", "1397", "1398", "1399", "1400", "1401", "1402", "1403", "1404", "1405", "1406", "1407", "1408", "1409", "1410", "1411", "1412", "1413", "1414", "1415", "1416", "1417", "1418", "1419", "1420", "1421", "1422", "1423", "1424", "1425", "1426", "1427", "1428", "1429", "1430", "1431", "1432", "1433", "1434", "1435", "1436", "1437", "1438", "1439", "1440", "1441", "1442", "1443", "1444", "1445", "1446", "1447", "1448", "1449", "1450", "1451", "1452", "1453", "1454", "1455", "1456", "1457", "1458", "1459", "1460", "1461", "1462", "1463", "1464", "1465", "1466", "1467", "1468", "1469", "1470", "1471", "1472", "1473", "1474", "1475", "1476", "1477", "1478", "1479", "1480", "1481", "1482", "1483", "1484", "1485", "1486", "1487", "1488", "1489", "1490", "1491", "1492", "1493", "1494", "1495", "1496", "1497", "1498", "1499", "1500", "1501", "1502", "1503", "1504", "1505", "1506", "1507", "1508", "1509", "1510", "1511", "1512", "1513", "1514", "1515", "1516", "1517", "1518", "1519", "1520", "1521", "1522", "1523", "1524", "1525", "1526", "1527", "1528", "1529", "1530", "1531", "1532", "1533", "1534", "1535", "1536", "1537", "1538", "1539", "1540", "1541", "1542", "1543", "1544", "1545", "1546", "1547", "1548", "1549", "1550", "1551", "1552", "1553", "1554", "1555", "1556", "1557", "1558", "1559", "1560", "1561", "1562", "1563", "1564", "1565", "1566", "1567", "1568", "1569", "1570", "1571", "1572", "1573", "1574", "1575", "1576", "1577", "1578", "1579", "1580", "1581", "1582", "1583", "1584", "1585", "1586", "1587", "1588", "1589", "1590", "1591", "1592", "1593", "1594", "1595", "1596", "1597", "1598", "1599", "1600", "1601", "1602", "1603", "1604", "1605", "1606", "1607", "1608", "1609", "1610", "1611", "1612", "1613", "1614", "1615", "1616", "1617", "1618", "1619", "1620", "1621", "1622", "1623", "1624", "1625", "1626", "1627", "1628", "1629", "1630", "1631", "1632", "1633", "1634", "1635", "1636", "1637", "1638", "1639", "1640", "1641", "1642", "1643", "1644", "1645", "1646", "1647", "1648", "1649", "1650", "1651", "1652", "1653", "1654", "1655", "1656", "1657", "1658", "1659", "1660", "1661", "1662", "1663", "1664", "1665", "1666", "1667", "1668", "1669", "1670", "1671", "1672", "1673", "1674", "1675", "1676", "1677", "1678", "1679", "1680", "1681", "1682", "1683", "1684", "1685", "1686", "1687", "1688", "1689", "1690", "1691", "1692", "1693", "1694", "1695", "1696", "1697", "1698", "1699", "1700", "1701", "1702", "1703", "1704", "1705", "1706", "1707", "1708", "1709", "1710", "1711", "1712", "1713", "1714", "1715", "1716", "1717", "1718", "1719", "1720", "1721", "1722", "1723", "1724", "1725", "1726", "1727", "1728", "1729", "1730", "1731", "1732", "1733", "1734", "1735", "1736", "1737", "1738", "1739", "1740", "1741", "1742", "1743", "1744", "1745", "1746", "1747", "1748", "1749", "1750", "1751", "1752", "1753", "1754", "1755", "1756", "1757", "1758", "1759", "1760", "1761", "1762", "1763", "1764", "1765", "1766", "1767", "1768", "1769", "1770", "1771", "1772", "1773", "1774", "1775", "1776", "1777", "1778", "1779", "1780", "1781", "1782", "1783", "1784", "1785", "1786", "1787", "1788", "1789", "1790", "1791", "1792", "1793", "1794", "1795", "1796", "1797", "1798", "1799", "1800", "1801", "1802", "1803", "1804", "1805", "1806", "1807", "1808", "1809", "1810", "1811", "1812", "1813", "1814", "1815", "1816", "1817", "1818", "1819", "1820", "1821", "1822", "1823", "1824", "1825", "1826", "1827", "1828", "1829", "1830", "1831", "1832", "1833", "1834", "1835", "1836", "1837", "1838", "1839", "1840", "1841", "1842", "1843", "1844", "1845", "1846", "1847", "1848", "1849", "1850", "1851", "1852", "1853", "1854", "1855", "1856", "1857", "1858", "1859", "1860", "1861", "1862", "1863", "1864", "1865", "1866", "1867", "1868", "1869", "1870", "1871", "1872", "1873", "1874", "1875", "1876", "1877", "1878", "1879", "1880", "1881", "1882", "1883", "1884", "1885", "1886", "1887", "1888", "1889", "1890", "1891", "1892", "1893", "1894", "1895", "1896", "1897", "1898", "1899", "1900", "1901", "1902", "1903", "1904", "1905", "1906", "1907", "1908", "1909", "1910", "1911", "1912", "1913", "1914", "1915", "1916", "1917", "1918", "1919", "1920", "1921", "1922", "1923", "1924", "1925", "1926", "1927", "1928", "1929", "1930", "1931", "1932", "1933", "1934", "1935", "1936", "1937", "1938", "1939", "1940", "1941", "1942", "1943", "1944", "1945", "1946", "1947", "1948", "1949", "1950", "1951", "1952", "1953", "1954", "1955", "1956", "1957", "1958", "1959", "1960", "1961", "1962", "1963", "1964", "1965", "1966", "1967", "1968", "1969", "1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034", "2035", "2036", "2037", "2038", "2039", "2040", "2041", "2042", "2043", "2044", "2045", "2046", "2047", "2048", "2049", "2050", "2051", "2052", "2053", "2054", "2055", "2056", "2057", "2058", "2059", "2060", "2061", "2062", "2063", "2064", "2065", "2066", "2067", "2068", "2069", "2070", "2071", "2072", "2073", "2074", "2075", "2076", "2077", "2078", "2079", "2080", "2081", "2082", "2083", "2084", "2085", "2086", "2087", "2088", "2089", "2090", "2091", "2092", "2093", "2094", "2095", "2096", "2097", "2098", "2099", "2100", "2101", "2102", "2103", "2104", "2105", "2106", "2107", "2108", "2109", "2110", "2111", "2112", "2113", "2114", "2115", "2116", "2117", "2118", "2119", "2120", "2121", "2122", "2123", "2124", "2125", "2126", "2127", "2128", "2129", "2130", "2131", "2132", "2133", "2134", "2135", "2136", "2137", "2138", "2139", "2140", "2141", "2142", "2143", "2144", "2145", "2146", "2147", "2148", "2149", "2150", "2151", "2152", "2153", "2154", "2155", "2156", "2157", "2158", "2159", "2160", "2161", "2162", "2163", "2164", "2165", "2166", "2167", "2168", "2169", "2170", "2171", "2172", "2173", "2174", "2175", "2176", "2177", "2178", "2179", "2180", "2181", "2182", "2183", "2184", "2185", "2186", "2187", "2188", "2189", "2190", "2191", "2192", "2193", "2194", "2195", "2196", "2197", "2198", "2199", "2200", "2201", "2202", "2203", "2204", "2205", "2206", "2207", "2208", "2209", "2210", "2211", "2212", "2213", "2214", "2215", "2216", "2217", "2218", "2219", "2220", "2221", "2222", "2223", "2224", "2225", "2226", "2227", "2228", "2229", "2230", "2231", "2232", "2233", "2234", "2235", "2236", "2237", "2238", "2239", "2240", "2241", "2242", "2243", "2244", "2245", "2246", "2247", "2248", "2249", "2250", "2251", "2252", "2253", "2254", "2255", "2256", "2257", "2258", "2259", "2260", "2261", "2262", "2263", "2264", "2265", "2266", "2267", "2268", "2269", "2270", "2271", "2272", "2273", "2274", "2275", "2276", "2277", "2278", "2279", "2280", "2281", "2282", "2283", "2284", "2285", "2286", "2287", "2288", "2289", "2290", "2291", "2292", "2293", "2294", "2295", "2296", "2297", "2298", "2299", "2300", "2301", "2302", "2303", "2304", "2305", "2306", "2307", "2308", "2309", "2310", "2311", "2312", "2313", "2314", "2315", "2316", "2317", "2318", "2319", "2320", "2321", "2322", "2323", "2324", "2325", "2326", "2327", "2328", "2329", "2330", "2331", "2332", "2333", "2334", "2335", "2336", "2337", "2338", "2339", "2340", "2341", "2342", "2343", "2344", "2345", "2346", "2347", "2348", "2349", "2350", "2351", "2352", "2353", "2354", "2355", "2356", "2357", "2358", "2359", "2360", "2361", "2362", "2363", "2364", "2365", "2366", "2367", "2368", "2369", "2370", "2371", "2372", "2373", "2374", "2375", "2376", "2377", "2378", "2379", "2380", "2381", "2382", "2383", "2384", "2385", "2386", "2387", "2388", "2389", "2390", "2391", "2392", "2393", "2394", "2395", "2396", "2397", "2398", "2399", "2400", "2401", "2402", "2403", "2404", "2405", "2406", "2407", "2408", "2409", "2410", "2411", "2412", "2413", "2414", "2415", "2416", "2417", "2418", "2419", "2420", "2421", "2422", "2423", "2424", "2425", "2426", "2427", "2428", "2429", "2430", "2431", "2432", "2433", "2434", "2435", "2436", "2437", "2438", "2439", "2440", "2441", "2442", "2443", "2444", "2445", "2446", "2447", "2448", "2449", "2450", "2451", "2452", "2453", "2454", "2455", "2456", "2457", "2458", "2459", "2460", "2461", "2462", "2463", "2464", "2465", "2466", "2467", "2468", "2469", "2470", "2471", "2472", "2473", "2474", "2475", "2476", "2477", "2478", "2479", "2480", "2481", "2482", "2483", "2484", "2485", "2486", "2487", "2488", "2489", "2490", "2491", "2492", "2493", "2494", "2495", "2496", "2497", "2498", "2499", "2500", "2501", "2502", "2503", "2504", "2505", "2506", "2507", "2508", "2509", "2510", "2511", "2512", "2513", "2514", "2515", "2516", "2517", "2518", "2519", "2520", "2521", "2522", "2523", "2524", "2525", "2526", "2527", "2528", "2529", "2530", "2531", "2532", "2533", "2534", "2535", "2536", "2537", "2538", "2539", "2540", "2541", "2542", "2543", "2544", "2545", "2546", "2547", "2548", "2549", "2550", "2551", "2552", "2553", "2554", "2555", "2556", "2557", "2558", "2559", "2560", "2561", "2562", "2563", "2564", "2565", "2566", "2567", "2568", "2569", "2570", "2571", "2572", "2573", "2574", "2575", "2576", "2577", "2578", "2579", "2580", "2581", "2582", "2583", "2584", "2585", "2586", "2587", "2588", "2589", "2590", "2591", "2592", "2593", "2594", "2595", "2596", "2597", "2598", "2599", "2600", "2601", "2602", "2603", "2604", "2605", "2606", "2607", "2608", "2609", "2610", "2611", "2612", "2613", "2614", "2615", "2616", "2617", "2618", "2619", "2620", "2621", "2622", "2623", "2624", "2625", "2626", "2627", "2628", "2629", "2630", "2631", "2632", "2633", "2634", "2635", "2636", "2637", "2638", "2639", "2640", "2641", "2642", "2643", "2644", "2645", "2646", "2647", "2648", "2649", "2650", "2651", "2652", "2653", "2654", "2655", "2656", "2657", "2658", "2659", "2660", "2661", "2662", "2663", "2664", "2665", "2666", "2667", "2668", "2669", "2670", "2671", "2672", "2673", "2674", "2675", "2676", "2677", "2678", "2679", "2680", "2681", "2682", "2683", "2684", "2685", "2686", "2687", "2688", "2689", "2690", "2691", "2692", "2693", "2694", "2695", "2696", "2697", "2698", "2699", "2700", "2701", "2702", "2703", "2704", "2705", "2706", "2707", "2708", "2709", "2710", "2711", "2712", "2713", "2714", "2715", "2716", "2717", "2718", "2719", "2720", "2721", "2722", "2723", "2724", "2725", "2726", "2727", "2728", "2729", "2730", "2731", "2732", "2733", "2734", "2735", "2736", "2737", "2738", "2739", "2740", "2741", "2742", "2743", "2744", "2745", "2746", "2747", "2748", "2749", "2750", "2751", "2752", "2753", "2754", "2755", "2756", "2757", "2758", "2759", "2760", "2761", "2762", "2763", "2764", "2765", "2766", "2767", "2768", "2769", "2770", "2771", "2772", "2773", "2774", "2775", "2776", "2777", "2778", "2779", "2780", "2781", "2782", "2783", "2784", "2785", "2786", "2787", "2788", "2789", "2790", "2791", "2792", "2793", "2794", "2795", "2796", "2797", "2798", "2799", "2800", "2801", "2802", "2803", "2804", "2805", "2806", "2807", "2808", "2809", "2810", "2811", "2812", "2813", "2814"]

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
2026-08-06 02:25:13,593 INFO     29 [qwen-vl-text] coord API raw response (len=12598):
[
	{"text": "广州医科大学附属第三医院", "bbox": [407, 44, 639, 60]},
	{"text": "肺功能检查报告", "bbox": [455, 60, 589, 75]},
	{"text": "地址：广州市多宝路63号 电话：020-81292126", "bbox": [313, 76, 737, 92]},
	{"text": "COSMED", "bbox": [123, 96, 188, 109]},
	{"text": "姓名：", "bbox": [109, 117, 150, 130]},
	{"text": "科室/床号：", "bbox": [109, 130, 185, 144]},
	{"text": "ID：", "bbox": [109, 144, 132, 157]},
	{"text": "出生日期：1984/12/8", "bbox": [109, 157, 266, 171]},
	{"text": "预计值：ERS 93", "bbox": [109, 171, 250, 184]},
	{"text": "日期：2024/10/22", "bbox": [405, 117, 567, 130]},
	{"text": "性别：Male", "bbox": [405, 130, 522, 144]},
	{"text": "地区修正：Chinese", "bbox": [405, 144, 547, 157]},
	{"text": "详细描述：内科门诊", "bbox": [405, 157, 551, 171]},
	{"text": "Company：", "bbox": [405, 171, 481, 184]},
	{"text": "年龄：39", "bbox": [754, 117, 872, 130]},
	{"text": "体重(Kg)：89.0", "bbox": [754, 130, 886, 144]},
	{"text": "身高(cm)：177.5", "bbox": [754, 144, 894, 157]},
	{"text": "BMI(Kg/m²：28.2", "bbox": [754, 157, 886, 171]},
	{"text": "吸烟：曾经(10/20)", "bbox": [754, 171, 936, 184]},
	{"text": "用力肺活量 Forced Vital Capacity", "bbox": [195, 190, 441, 203]},
	{"text": "F(l/s)", "bbox": [127, 205, 157, 216]},
	{"text": "V(l)", "bbox": [531, 190, 555, 203]},
	{"text": "BEST #3 - 2024/10/22 11:03", "bbox": [350, 204, 515, 214]},
	{"text": "沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38", "bbox": [239, 214, 515, 224]},
	{"text": "沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39", "bbox": [239, 224, 515, 234]},
	{"text": "沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41", "bbox": [239, 234, 515, 244]},
	{"text": "沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38", "bbox": [651, 202, 930, 212]},
	{"text": "沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39", "bbox": [651, 212, 930, 222]},
	{"text": "沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41", "bbox": [651, 222, 930, 232]},
	{"text": "BEST #3 - 2024/10/22 11:03", "bbox": [737, 190, 930, 200]},
	{"text": "FVC", "bbox": [112, 624, 142, 636]},
	{"text": "PEF", "bbox": [469, 291, 496, 301]},
	{"text": "MEF75%", "bbox": [193, 311, 250, 323]},
	{"text": "MEF50%", "bbox": [247, 357, 304, 369]},
	{"text": "MEF25%", "bbox": [302, 401, 358, 413]},
	{"text": "FVC", "bbox": [357, 437, 384, 447]},
	{"text": "6", "bbox": [404, 447, 413, 456]},
	{"text": "7", "bbox": [447, 447, 456, 456]},
	{"text": "8V(l)", "bbox": [491, 447, 519, 456]},
	{"text": "FEV1", "bbox": [602, 283, 635, 294]},
	{"text": "ATS", "bbox": [743, 364, 772, 374]},
	{"text": "12t(s)", "bbox": [908, 374, 942, 384]},
	{"text": "-1", "bbox": [543, 374, 555, 384]},
	{"text": "0", "bbox": [574, 374, 584, 384]},
	{"text": "1", "bbox": [603, 374, 612, 384]},
	{"text": "2", "bbox": [632, 374, 641, 384]},
	{"text": "3", "bbox": [660, 374, 669, 384]},
	{"text": "4", "bbox": [689, 374, 698, 384]},
	{"text": "5", "bbox": [716, 374, 725, 384]},
	{"text": "6", "bbox": [744, 374, 753, 384]},
	{"text": "7", "bbox": [772, 374, 781, 384]},
	{"text": "8", "bbox": [800, 374, 809, 384]},
	{"text": "9", "bbox": [828, 374, 837, 384]},
	{"text": "10", "bbox": [855, 374, 867, 384]},
	{"text": "11", "bbox": [883, 374, 894, 384]},
	{"text": "12", "bbox": [911, 374, 923, 384]},
	{"text": "1", "bbox": [184, 447, 190, 456]},
	{"text": "2", "bbox": [227, 447, 234, 456]},
	{"text": "3", "bbox": [272, 447, 279, 456]},
	{"text": "4", "bbox": [316, 447, 323, 456]},
	{"text": "5", "bbox": [359, 447, 367, 456]},
	{"text": "1", "bbox": [123, 417, 131, 427]},
	{"text": "2", "bbox": [123, 403, 131, 413]},
	{"text": "3", "bbox": [123, 389, 131, 399]},
	{"text": "4", "bbox": [123, 374, 131, 384]},
	{"text": "5", "bbox": [123, 357, 131, 367]},
	{"text": "6", "bbox": [123, 342, 131, 352]},
	{"text": "7", "bbox": [123, 327, 131, 337]},
	{"text": "8", "bbox": [123, 311, 131, 321]},
	{"text": "9", "bbox": [123, 296, 131, 306]},
	{"text": "10", "bbox": [117, 280, 131, 290]},
	{"text": "11", "bbox": [117, 264, 131, 274]},
	{"text": "12", "bbox": [117, 248, 131, 258]},
	{"text": "13", "bbox": [117, 232, 131, 242]},
	{"text": "14", "bbox": [117, 216, 131, 226]},
	{"text": "1", "bbox": [117, 477, 127, 487]},
	{"text": "2", "bbox": [117, 462, 127, 472]},
	{"text": "3", "bbox": [117, 447, 127, 456]},
	{"text": "4", "bbox": [117, 431, 127, 441]},
	{"text": "5", "bbox": [117, 417, 127, 427]},
	{"text": "6", "bbox": [117, 403, 127, 413]},
	{"text": "7", "bbox": [117, 389, 127, 399]},
	{"text": "8", "bbox": [117, 374, 127, 384]},
	{"text": "9", "bbox": [117, 357, 127, 367]},
	{"text": "10", "bbox": [117, 342, 127, 352]},
	{"text": "11", "bbox": [117, 327, 127, 337]},
	{"text": "12", "bbox": [117, 311, 127, 321]},
	{"text": "13", "bbox": [117, 296, 127, 306]},
	{"text": "14", "bbox": [117, 280, 127, 290]},
	{"text": "15", "bbox": [117, 264, 127, 274]},
	{"text": "16", "bbox": [117, 248, 127, 258]},
	{"text": "17", "bbox": [117, 232, 127, 242]},
	{"text": "18", "bbox": [117, 216, 127, 226]},
	{"text": "19", "bbox": [117, 200, 127, 210]},
	{"text": "20", "bbox": [117, 184, 127, 194]},
	{"text": "21", "bbox": [117, 168, 127, 178]},
	{"text": "22", "bbox": [117, 152, 127, 162]},
	{"text": "23", "bbox": [117, 136, 127, 146]},
	{"text": "24", "bbox": [117, 120, 127, 130]},
	{"text": "25", "bbox": [117, 104, 127, 114]},
	{"text": "26", "bbox": [117, 88, 127, 98]},
	{"text": "27", "bbox": [117, 72, 127, 82]},
	{"text": "28", "bbox": [117, 56, 127, 66]},
	{"text": "29", "bbox": [117, 40, 127, 50]},
	{"text": "30", "bbox": [117, 24, 127, 34]},
	{"text": "31", "bbox": [117, 8, 127, 18]},
	{"text": "32", "bbox": [145, 8, 155, 18]},
	{"text": "33", "bbox": [173, 8, 183, 18]},
	{"text": "34", "bbox": [201, 8, 211, 18]},
	{"text": "35", "bbox": [229, 8, 239, 18]},
	{"text": "36", "bbox": [257, 8, 267, 18]},
	{"text": "37", "bbox": [285, 8, 295, 18]},
	{"text": "38", "bbox": [313, 8, 323, 18]},
	{"text": "39", "bbox": [341, 8, 351, 18]},
	{"text": "40", "bbox": [369, 8, 379, 18]},
	{"text": "41", "bbox": [397, 8, 407, 18]},
	{"text": "42", "bbox": [425, 8, 435, 18]},
	{"text": "43", "bbox": [453, 8, 463, 18]},
	{"text": "44", "bbox": [481, 8, 491, 18]},
	{"text": "45", "bbox": [509, 8, 519, 18]},
	{"text": "46", "bbox": [537, 8, 547, 18]},
	{"text": "47", "bbox": [565, 8, 575, 18]},
	{"text": "48", "bbox": [593, 8, 603, 18]},
	{"text": "49", "bbox": [621, 8, 631, 18]},
	{"text": "50", "bbox": [649, 8, 659, 18]},
	{"text": "51", "bbox": [677, 8, 687, 18]},
	{"text": "52", "bbox": [705, 8, 715, 18]},
	{"text": "53", "bbox": [733, 8, 743, 18]},
	{"text": "54", "bbox": [761, 8, 771, 18]},
	{"text": "55", "bbox": [789, 8, 799, 18]},
	{"text": "56", "bbox": [817, 8, 827, 18]},
	{"text": "57", "bbox": [845, 8, 855, 18]},
	{"text": "58", "bbox": [873, 8, 883, 18]},
	{"text": "59", "bbox": [901, 8, 911, 18]},
	{"text": "60", "bbox": [929, 8, 939, 18]},
	{"text": "61", "bbox": [957, 8, 967, 18]},
	{"text": "62", "bbox": [985, 8, 995, 18]},
	{"text": "63", "bbox": [117, 104, 127, 114]},
	{"text": "64", "bbox": [117, 88, 127, 98]},
	{"text": "65", "bbox": [117, 72, 127, 82]},
	{"text": "66", "bbox": [117, 56, 127, 66]},
	{"text": "67", "bbox": [117, 40, 127, 50]},
	{"text": "68", "bbox": [117, 24, 127, 34]},
	{"text": "69", "bbox": [117, 8, 127, 18]},
	{"text": "70", "bbox": [145, 8, 155, 18]},
	{"text": "71", "bbox": [173, 8, 183, 18]},
	{"text": "72", "bbox": [201, 8, 211, 18]},
	{"text": "73", "bbox": [229, 8, 239, 18]},
	{"text": "74", "bbox": [257, 8, 267, 18]},
	{"text": "75", "bbox": [285, 8, 295, 18]},
	{"text": "76", "bbox": [313, 8, 323, 18]},
	{"text": "77", "bbox": [341, 8, 351, 18]},
	{"text": "78", "bbox": [369, 8, 379, 18]},
	{"text": "79", "bbox": [397, 8, 407, 18]},
	{"text": "80", "bbox": [425, 8, 435, 18]},
	{"text": "81", "bbox": [453, 8, 463, 18]},
	{"text": "82", "bbox": [481, 8, 491, 18]},
	{"text": "83", "bbox": [509, 8, 519, 18]},
	{"text": "84", "bbox": [537, 8, 547, 18]},
	{"text": "85", "bbox": [565, 8, 575, 18]},
	{"text": "86", "bbox": [593, 8, 603, 18]},
	{"text": "87", "bbox": [621, 8, 631, 18]},
	{"text": "88", "bbox": [649, 8, 659, 18]},
	{"text": "89", "bbox": [677, 8, 687, 18]},
	{"text": "90", "bbox": [705, 8, 715, 18]},
	{"text": "91", "bbox": [733, 8, 743, 18]},
	{"text": "92", "bbox": [761, 8, 771, 18]},
	{"text": "93", "bbox": [789, 8, 799, 18]},
	{"text": "94", "bbox": [817, 8, 827, 18]},
	{"text": "95", "bbox": [845, 8, 855, 18]},
	{"text": "96", "bbox": [873, 8, 883, 18]},
	{"text": "97", "bbox": [901, 8, 911, 18]},
	{"text": "98", "bbox": [929, 8, 939, 18]},
	{"text": "99", "bbox": [957, 8, 967, 18]},
	{"text": "100", "bbox": [985, 8, 995, 18]},
	{"text": "101", "bbox": [117, 104, 127, 114]},
	{"text": "102", "bbox": [117, 88, 127, 98]},
	{"text": "103", "bbox": [117, 72, 127, 82]},
	{"text": "104", "bbox": [117, 56, 127, 66]},
	{"text": "105", "bbox": [117, 40, 127, 50]},
	{"text": "106", "bbox": [117, 24, 127, 34]},
	{"text": "107", "bbox": [117, 8, 127, 18]},
	{"text": "108", "bbox": [145, 8, 155, 18]},
	{"text": "109", "bbox": [173, 8, 183, 18]},
	{"text": "110", "bbox": [201, 8, 211, 18]},
	{"text": "111", "bbox": [229, 8, 239, 18]},
	{"text": "112", "bbox": [257, 8, 267, 18]},
	{"text": "113", "bbox": [285, 8, 295, 18]},
	{"text": "114", "bbox": [313, 8, 323, 18]},
	{"text": "115", "bbox": [341, 8, 351, 18]},
	{"text": "116", "bbox": [369, 8, 379, 18]},
	{"text": "117", "bbox": [397, 8, 407, 18]},
	{"text": "118", "bbox": [425, 8, 435, 18]},
	{"text": "119", "bbox": [453, 8, 463, 18]},
	{"text": "120", "bbox": [481, 8, 491, 18]},
	{"text": "121", "bbox": [509, 8, 519, 18]},
	{"text": "122", "bbox": [537, 8, 547, 18]},
	{"text": "123", "bbox": [565, 8, 575, 18]},
	{"text": "124", "bbox": [593, 8, 603, 18]},
	{"text": "125", "bbox": [621, 8, 631, 18]},
	{"text": "126", "bbox": [649, 8, 659, 18]},
	{"text": "127", "bbox": [677, 8, 687, 18]},
	{"text": "128", "bbox": [705, 8, 715, 18]},
	{"text": "129", "bbox": [733, 8, 743, 18]},
	{"text": "130", "bbox": [761, 8, 771, 18]},
	{"text": "131", "bbox": [789, 8, 799, 18]},
	{"text": "132", "bbox": [817, 8, 827, 18]},
	{"text": "133", "bbox": [845, 8, 855, 18]},
	{"text": "134", "bbox": [873, 8, 883, 18]},
	{"text": "135", "bbox": [901, 8, 911, 18]},
	{"text": "136", "bbox": [929, 8, 939, 18]},
	{"text": "137", "bbox": [957, 8, 967, 18]},
	{"text": "138", "bbox": [985, 8, 995, 18]},
	{"text": "139", "bbox": [117, 104, 127, 114]},
	{"text": "140", "bbox": [117, 88, 127, 98]},
	{"text": "141", "bbox": [117, 72, 127, 82]},
	{"text": "142", "bbox": [117, 56, 127, 66]},
	{"text": "143", "bbox": [117, 40, 127, 50]},
	{"text": "144", "bbox": [117, 24, 127, 34]},
	{"text": "145", "bbox": [117, 8, 127, 18]},
	{"text": "146", "bbox": [145, 8, 155, 18]},
	{"text": "147", "bbox": [173, 8, 183, 18]},
	{"text": "148", "bbox": [201, 8, 211, 18]},
	{"text": "149", "bbox": [229, 8, 239, 18]},
	{"text": "150", "bbox": [257, 8, 267, 18]},
	{"text": "151", "bbox": [285, 8, 295, 18]},
	{"text": "152", "bbox": [313, 8, 323, 18]},
	{"text": "153", "bbox": [341, 8, 351, 18]},
	{"text": "154", "bbox": [369, 8, 379, 18]},
	{"text": "155", "bbox": [397, 8, 407, 18]},
	{"text": "156", "bbox": [425, 8, 435, 18]},
	{"text": "157", "bbox": [453, 8, 463, 18]},
	{"text": "158", "bbox": [481, 8, 491, 18]},
	{"text": "159", "bbox": [509, 8, 519, 18]},
	{"text": "160", "bbox": [537, 8, 547, 18]},
	{"text": "161", "bbox": [565, 8, 575, 18]},
	{"text": "162", "bbox": [593, 8, 603, 18]},
	{"text": "163", "bbox": [621, 8, 631, 18]},
	{"text": "164", "bbox": [649, 8, 659, 18]},
	{"text": "165", "bbox": [677, 8, 687, 18]},
	{"text": "166", "bbox": [705, 8, 715, 18]},
	{"text": "167", "bbox": [733, 8, 743, 18]},
	{"text": "168", "bbox": [761, 8, 771, 18]},
	{"text": "169", "bbox": [789, 8, 799, 18]},
	{"text": "170", "bbox": [817, 8, 827, 18]},
	{"text": "171", "bbox": [845, 8, 855, 18]},
	{"text": "172", "bbox": [873, 8, 883, 18]},
	{"text": "173", "bbox": [901, 8, 911, 18]},
	{"text": "174", "bbox": [929, 8, 939, 18]},
	{"text": "175", "bbox": [957, 8, 967, 18]},
	{"text": "176", "bbox": [985, 8, 995, 18]},
	{"text": "177", "bbox": [117, 104, 127, 114]},
	{"text": "178", "bbox": [117, 88, 127, 98]},
	{"text": "179", "bbox": [117, 72, 127, 82]},
	{"text": "180", "bbox": [117, 56, 127, 66]},
	{"text": "181", "bbox": [117, 40, 127, 50]},
	{"text": "182", "bbox": [117, 24, 127, 34]},
	{"text": "183", "bbox": [117, 8, 127, 18]},
	{"text": "184", "bbox": [145, 8, 155, 18]},
	{"text": "185", "bbox": [173, 8, 183, 18]},
	{"text": "186", "bbox": [201, 8, 211, 18]},
	{"text": "187", "bbox": [229, 8, 239, 18]},
	{"text": "188", "bbox": [257, 8, 267, 18]},
	{"text": "189", "bbox": [285, 8, 295, 18]},
	{"text": "190", "bbox": [313, 8, 323, 18]},
	{"text": "191", "bbox": [341, 8, 351, 18]},
	{"text": "19
2026-08-06 02:25:13,593 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord API: raw_items=267, valid_items=266, elapsed=75.6s
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[0]: text=广州医科大学附属第三医院, bbox=[407, 44, 639, 60]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[1]: text=肺功能检查报告, bbox=[455, 60, 589, 75]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[2]: text=地址：广州市多宝路63号 电话：020-81292126, bbox=[313, 76, 737, 92]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[3]: text=COSMED, bbox=[123, 96, 188, 109]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[109, 117, 150, 130]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[5]: text=科室/床号：, bbox=[109, 130, 185, 144]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[6]: text=ID：, bbox=[109, 144, 132, 157]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[7]: text=出生日期：1984/12/8, bbox=[109, 157, 266, 171]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[8]: text=预计值：ERS 93, bbox=[109, 171, 250, 184]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[9]: text=日期：2024/10/22, bbox=[405, 117, 567, 130]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[10]: text=性别：Male, bbox=[405, 130, 522, 144]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[11]: text=地区修正：Chinese, bbox=[405, 144, 547, 157]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[12]: text=详细描述：内科门诊, bbox=[405, 157, 551, 171]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[13]: text=Company：, bbox=[405, 171, 481, 184]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[14]: text=年龄：39, bbox=[754, 117, 872, 130]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[15]: text=体重(Kg)：89.0, bbox=[754, 130, 886, 144]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[16]: text=身高(cm)：177.5, bbox=[754, 144, 894, 157]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[17]: text=BMI(Kg/m²：28.2, bbox=[754, 157, 886, 171]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[18]: text=吸烟：曾经(10/20), bbox=[754, 171, 936, 184]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[19]: text=用力肺活量 Forced Vital Capacity, bbox=[195, 190, 441, 203]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[20]: text=F(l/s), bbox=[127, 205, 157, 216]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[21]: text=V(l), bbox=[531, 190, 555, 203]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[22]: text=BEST #3 - 2024/10/22 11:03, bbox=[350, 204, 515, 214]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[23]: text=沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38, bbox=[239, 214, 515, 224]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[24]: text=沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39, bbox=[239, 224, 515, 234]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[25]: text=沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41, bbox=[239, 234, 515, 244]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[26]: text=沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38, bbox=[651, 202, 930, 212]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[27]: text=沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39, bbox=[651, 212, 930, 222]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[28]: text=沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41, bbox=[651, 222, 930, 232]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[29]: text=BEST #3 - 2024/10/22 11:03, bbox=[737, 190, 930, 200]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[30]: text=FVC, bbox=[112, 624, 142, 636]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[31]: text=PEF, bbox=[469, 291, 496, 301]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[32]: text=MEF75%, bbox=[193, 311, 250, 323]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[33]: text=MEF50%, bbox=[247, 357, 304, 369]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[34]: text=MEF25%, bbox=[302, 401, 358, 413]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[35]: text=FVC, bbox=[357, 437, 384, 447]
2026-08-06 02:25:13,598 INFO     29 [qwen-vl-text] coord item[36]: text=6, bbox=[404, 447, 413, 456]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[37]: text=7, bbox=[447, 447, 456, 456]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[38]: text=8V(l), bbox=[491, 447, 519, 456]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[39]: text=FEV1, bbox=[602, 283, 635, 294]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[40]: text=ATS, bbox=[743, 364, 772, 374]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[41]: text=12t(s), bbox=[908, 374, 942, 384]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[42]: text=-1, bbox=[543, 374, 555, 384]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[43]: text=0, bbox=[574, 374, 584, 384]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[44]: text=1, bbox=[603, 374, 612, 384]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[45]: text=2, bbox=[632, 374, 641, 384]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[46]: text=3, bbox=[660, 374, 669, 384]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[47]: text=4, bbox=[689, 374, 698, 384]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[48]: text=5, bbox=[716, 374, 725, 384]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[49]: text=6, bbox=[744, 374, 753, 384]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[50]: text=7, bbox=[772, 374, 781, 384]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[51]: text=8, bbox=[800, 374, 809, 384]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[52]: text=9, bbox=[828, 374, 837, 384]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[53]: text=10, bbox=[855, 374, 867, 384]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[54]: text=11, bbox=[883, 374, 894, 384]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[55]: text=12, bbox=[911, 374, 923, 384]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[56]: text=1, bbox=[184, 447, 190, 456]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[57]: text=2, bbox=[227, 447, 234, 456]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[58]: text=3, bbox=[272, 447, 279, 456]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[59]: text=4, bbox=[316, 447, 323, 456]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[60]: text=5, bbox=[359, 447, 367, 456]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[61]: text=1, bbox=[123, 417, 131, 427]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[62]: text=2, bbox=[123, 403, 131, 413]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[63]: text=3, bbox=[123, 389, 131, 399]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[64]: text=4, bbox=[123, 374, 131, 384]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[65]: text=5, bbox=[123, 357, 131, 367]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[66]: text=6, bbox=[123, 342, 131, 352]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[67]: text=7, bbox=[123, 327, 131, 337]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[68]: text=8, bbox=[123, 311, 131, 321]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[69]: text=9, bbox=[123, 296, 131, 306]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[70]: text=10, bbox=[117, 280, 131, 290]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[71]: text=11, bbox=[117, 264, 131, 274]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[72]: text=12, bbox=[117, 248, 131, 258]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[73]: text=13, bbox=[117, 232, 131, 242]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[74]: text=14, bbox=[117, 216, 131, 226]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[75]: text=1, bbox=[117, 477, 127, 487]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[76]: text=2, bbox=[117, 462, 127, 472]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[77]: text=3, bbox=[117, 447, 127, 456]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[78]: text=4, bbox=[117, 431, 127, 441]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[79]: text=5, bbox=[117, 417, 127, 427]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[80]: text=6, bbox=[117, 403, 127, 413]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[81]: text=7, bbox=[117, 389, 127, 399]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[82]: text=8, bbox=[117, 374, 127, 384]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[83]: text=9, bbox=[117, 357, 127, 367]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[84]: text=10, bbox=[117, 342, 127, 352]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[85]: text=11, bbox=[117, 327, 127, 337]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[86]: text=12, bbox=[117, 311, 127, 321]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[87]: text=13, bbox=[117, 296, 127, 306]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[88]: text=14, bbox=[117, 280, 127, 290]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[89]: text=15, bbox=[117, 264, 127, 274]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[90]: text=16, bbox=[117, 248, 127, 258]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[91]: text=17, bbox=[117, 232, 127, 242]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[92]: text=18, bbox=[117, 216, 127, 226]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[93]: text=19, bbox=[117, 200, 127, 210]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[94]: text=20, bbox=[117, 184, 127, 194]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[95]: text=21, bbox=[117, 168, 127, 178]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[96]: text=22, bbox=[117, 152, 127, 162]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[97]: text=23, bbox=[117, 136, 127, 146]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[98]: text=24, bbox=[117, 120, 127, 130]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[99]: text=25, bbox=[117, 104, 127, 114]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[100]: text=26, bbox=[117, 88, 127, 98]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[101]: text=27, bbox=[117, 72, 127, 82]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[102]: text=28, bbox=[117, 56, 127, 66]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[103]: text=29, bbox=[117, 40, 127, 50]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[104]: text=30, bbox=[117, 24, 127, 34]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[105]: text=31, bbox=[117, 8, 127, 18]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[106]: text=32, bbox=[145, 8, 155, 18]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[107]: text=33, bbox=[173, 8, 183, 18]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[108]: text=34, bbox=[201, 8, 211, 18]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[109]: text=35, bbox=[229, 8, 239, 18]
2026-08-06 02:25:13,599 INFO     29 [qwen-vl-text] coord item[110]: text=36, bbox=[257, 8, 267, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[111]: text=37, bbox=[285, 8, 295, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[112]: text=38, bbox=[313, 8, 323, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[113]: text=39, bbox=[341, 8, 351, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[114]: text=40, bbox=[369, 8, 379, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[115]: text=41, bbox=[397, 8, 407, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[116]: text=42, bbox=[425, 8, 435, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[117]: text=43, bbox=[453, 8, 463, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[118]: text=44, bbox=[481, 8, 491, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[119]: text=45, bbox=[509, 8, 519, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[120]: text=46, bbox=[537, 8, 547, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[121]: text=47, bbox=[565, 8, 575, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[122]: text=48, bbox=[593, 8, 603, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[123]: text=49, bbox=[621, 8, 631, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[124]: text=50, bbox=[649, 8, 659, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[125]: text=51, bbox=[677, 8, 687, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[126]: text=52, bbox=[705, 8, 715, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[127]: text=53, bbox=[733, 8, 743, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[128]: text=54, bbox=[761, 8, 771, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[129]: text=55, bbox=[789, 8, 799, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[130]: text=56, bbox=[817, 8, 827, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[131]: text=57, bbox=[845, 8, 855, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[132]: text=58, bbox=[873, 8, 883, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[133]: text=59, bbox=[901, 8, 911, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[134]: text=60, bbox=[929, 8, 939, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[135]: text=61, bbox=[957, 8, 967, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[136]: text=62, bbox=[985, 8, 995, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[137]: text=63, bbox=[117, 104, 127, 114]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[138]: text=64, bbox=[117, 88, 127, 98]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[139]: text=65, bbox=[117, 72, 127, 82]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[140]: text=66, bbox=[117, 56, 127, 66]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[141]: text=67, bbox=[117, 40, 127, 50]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[142]: text=68, bbox=[117, 24, 127, 34]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[143]: text=69, bbox=[117, 8, 127, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[144]: text=70, bbox=[145, 8, 155, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[145]: text=71, bbox=[173, 8, 183, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[146]: text=72, bbox=[201, 8, 211, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[147]: text=73, bbox=[229, 8, 239, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[148]: text=74, bbox=[257, 8, 267, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[149]: text=75, bbox=[285, 8, 295, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[150]: text=76, bbox=[313, 8, 323, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[151]: text=77, bbox=[341, 8, 351, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[152]: text=78, bbox=[369, 8, 379, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[153]: text=79, bbox=[397, 8, 407, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[154]: text=80, bbox=[425, 8, 435, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[155]: text=81, bbox=[453, 8, 463, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[156]: text=82, bbox=[481, 8, 491, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[157]: text=83, bbox=[509, 8, 519, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[158]: text=84, bbox=[537, 8, 547, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[159]: text=85, bbox=[565, 8, 575, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[160]: text=86, bbox=[593, 8, 603, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[161]: text=87, bbox=[621, 8, 631, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[162]: text=88, bbox=[649, 8, 659, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[163]: text=89, bbox=[677, 8, 687, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[164]: text=90, bbox=[705, 8, 715, 18]
2026-08-06 02:25:13,600 INFO     29 [qwen-vl-text] coord item[165]: text=91, bbox=[733, 8, 743, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[166]: text=92, bbox=[761, 8, 771, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[167]: text=93, bbox=[789, 8, 799, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[168]: text=94, bbox=[817, 8, 827, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[169]: text=95, bbox=[845, 8, 855, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[170]: text=96, bbox=[873, 8, 883, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[171]: text=97, bbox=[901, 8, 911, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[172]: text=98, bbox=[929, 8, 939, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[173]: text=99, bbox=[957, 8, 967, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[174]: text=100, bbox=[985, 8, 995, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[175]: text=101, bbox=[117, 104, 127, 114]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[176]: text=102, bbox=[117, 88, 127, 98]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[177]: text=103, bbox=[117, 72, 127, 82]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[178]: text=104, bbox=[117, 56, 127, 66]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[179]: text=105, bbox=[117, 40, 127, 50]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[180]: text=106, bbox=[117, 24, 127, 34]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[181]: text=107, bbox=[117, 8, 127, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[182]: text=108, bbox=[145, 8, 155, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[183]: text=109, bbox=[173, 8, 183, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[184]: text=110, bbox=[201, 8, 211, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[185]: text=111, bbox=[229, 8, 239, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[186]: text=112, bbox=[257, 8, 267, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[187]: text=113, bbox=[285, 8, 295, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[188]: text=114, bbox=[313, 8, 323, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[189]: text=115, bbox=[341, 8, 351, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[190]: text=116, bbox=[369, 8, 379, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[191]: text=117, bbox=[397, 8, 407, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[192]: text=118, bbox=[425, 8, 435, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[193]: text=119, bbox=[453, 8, 463, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[194]: text=120, bbox=[481, 8, 491, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[195]: text=121, bbox=[509, 8, 519, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[196]: text=122, bbox=[537, 8, 547, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[197]: text=123, bbox=[565, 8, 575, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[198]: text=124, bbox=[593, 8, 603, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[199]: text=125, bbox=[621, 8, 631, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[200]: text=126, bbox=[649, 8, 659, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[201]: text=127, bbox=[677, 8, 687, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[202]: text=128, bbox=[705, 8, 715, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[203]: text=129, bbox=[733, 8, 743, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[204]: text=130, bbox=[761, 8, 771, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[205]: text=131, bbox=[789, 8, 799, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[206]: text=132, bbox=[817, 8, 827, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[207]: text=133, bbox=[845, 8, 855, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[208]: text=134, bbox=[873, 8, 883, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[209]: text=135, bbox=[901, 8, 911, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[210]: text=136, bbox=[929, 8, 939, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[211]: text=137, bbox=[957, 8, 967, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[212]: text=138, bbox=[985, 8, 995, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[213]: text=139, bbox=[117, 104, 127, 114]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[214]: text=140, bbox=[117, 88, 127, 98]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[215]: text=141, bbox=[117, 72, 127, 82]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[216]: text=142, bbox=[117, 56, 127, 66]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[217]: text=143, bbox=[117, 40, 127, 50]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[218]: text=144, bbox=[117, 24, 127, 34]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[219]: text=145, bbox=[117, 8, 127, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[220]: text=146, bbox=[145, 8, 155, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[221]: text=147, bbox=[173, 8, 183, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[222]: text=148, bbox=[201, 8, 211, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[223]: text=149, bbox=[229, 8, 239, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[224]: text=150, bbox=[257, 8, 267, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[225]: text=151, bbox=[285, 8, 295, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[226]: text=152, bbox=[313, 8, 323, 18]
2026-08-06 02:25:13,601 INFO     29 [qwen-vl-text] coord item[227]: text=153, bbox=[341, 8, 351, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[228]: text=154, bbox=[369, 8, 379, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[229]: text=155, bbox=[397, 8, 407, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[230]: text=156, bbox=[425, 8, 435, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[231]: text=157, bbox=[453, 8, 463, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[232]: text=158, bbox=[481, 8, 491, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[233]: text=159, bbox=[509, 8, 519, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[234]: text=160, bbox=[537, 8, 547, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[235]: text=161, bbox=[565, 8, 575, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[236]: text=162, bbox=[593, 8, 603, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[237]: text=163, bbox=[621, 8, 631, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[238]: text=164, bbox=[649, 8, 659, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[239]: text=165, bbox=[677, 8, 687, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[240]: text=166, bbox=[705, 8, 715, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[241]: text=167, bbox=[733, 8, 743, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[242]: text=168, bbox=[761, 8, 771, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[243]: text=169, bbox=[789, 8, 799, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[244]: text=170, bbox=[817, 8, 827, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[245]: text=171, bbox=[845, 8, 855, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[246]: text=172, bbox=[873, 8, 883, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[247]: text=173, bbox=[901, 8, 911, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[248]: text=174, bbox=[929, 8, 939, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[249]: text=175, bbox=[957, 8, 967, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[250]: text=176, bbox=[985, 8, 995, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[251]: text=177, bbox=[117, 104, 127, 114]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[252]: text=178, bbox=[117, 88, 127, 98]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[253]: text=179, bbox=[117, 72, 127, 82]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[254]: text=180, bbox=[117, 56, 127, 66]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[255]: text=181, bbox=[117, 40, 127, 50]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[256]: text=182, bbox=[117, 24, 127, 34]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[257]: text=183, bbox=[117, 8, 127, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[258]: text=184, bbox=[145, 8, 155, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[259]: text=185, bbox=[173, 8, 183, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[260]: text=186, bbox=[201, 8, 211, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[261]: text=187, bbox=[229, 8, 239, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[262]: text=188, bbox=[257, 8, 267, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[263]: text=189, bbox=[285, 8, 295, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[264]: text=190, bbox=[313, 8, 323, 18]
2026-08-06 02:25:13,602 INFO     29 [qwen-vl-text] coord item[265]: text=191, bbox=[341, 8, 351, 18]
2026-08-06 02:25:14,893 INFO     29 [qwen-vl-text] page=15 — 2884/2884 coords, api_time=75.6s
2026-08-06 02:25:14,896 INFO     29 [qwen-vl-text] new_positions (2884):
[[15, 242.165, 380.205, 37.048, 50.519999999999996], [15, 270.72499999999997, 350.455, 50.519999999999996, 63.15], [15, 186.23499999999999, 438.515, 63.992, 77.464], [15, 73.185, 111.86, 80.832, 91.77799999999999], [15, 64.855, 89.25, 98.514, 109.46], [15, 64.855, 110.07499999999999, 109.46, 121.24799999999999], [15, 64.855, 78.53999999999999, 121.24799999999999, 132.194], [15, 64.855, 158.26999999999998, 132.194, 143.982], [15, 64.855, 148.75, 143.982, 154.928], [15, 240.975, 337.365, 98.514, 109.46], [15, 240.975, 310.59, 109.46, 121.24799999999999], [15, 240.975, 325.465, 121.24799999999999, 132.194], [15, 240.975, 327.84499999999997, 132.194, 143.982], [15, 240.975, 286.195, 143.982, 154.928], [15, 448.63, 518.84, 98.514, 109.46], [15, 448.63, 527.17, 109.46, 121.24799999999999], [15, 448.63, 531.93, 121.24799999999999, 132.194], [15, 448.63, 527.17, 132.194, 143.982], [15, 448.63, 556.92, 143.982, 154.928], [15, 116.02499999999999, 262.395, 159.98, 170.926], [15, 75.565, 93.41499999999999, 172.60999999999999, 181.87199999999999], [15, 315.945, 330.22499999999997, 159.98, 170.926], [15, 208.25, 306.425, 171.768, 180.188], [15, 142.20499999999998, 306.425, 180.188, 188.608], [15, 142.20499999999998, 306.425, 188.608, 197.028], [15, 142.20499999999998, 306.425, 197.028, 205.44799999999998], [15, 387.34499999999997, 553.35, 170.084, 178.504], [15, 387.34499999999997, 553.35, 178.504, 186.924], [15, 387.34499999999997, 553.35, 186.924, 195.344], [15, 438.515, 553.35, 159.98, 168.4], [15, 66.64, 84.49, 525.408, 535.512], [15, 279.055, 295.12, 245.022, 253.44199999999998], [15, 114.835, 148.75, 261.86199999999997, 271.966], [15, 146.965, 180.88, 300.594, 310.698], [15, 179.69, 213.01, 337.642, 347.746], [15, 212.415, 228.48, 367.954, 376.37399999999997], [15, 240.38, 245.73499999999999, 376.37399999999997, 383.952], [15, 265.965, 271.32, 376.37399999999997, 383.952], [15, 292.145, 308.805, 376.37399999999997, 383.952], [15, 358.19, 377.825, 238.286, 247.548], [15, 442.085, 459.34, 306.488, 314.908], [15, 540.26, 560.49, 314.908, 323.328], [15, 323.085, 330.22499999999997, 314.908, 323.328], [15, 341.53, 347.47999999999996, 314.908, 323.328], [15, 358.78499999999997, 364.14, 314.908, 323.328], [15, 376.03999999999996, 381.395, 314.908, 323.328], [15, 392.7, 398.055, 314.908, 323.328], [15, 409.955, 415.31, 314.908, 323.328], [15, 426.02, 431.375, 314.908, 323.328], [15, 442.68, 448.03499999999997, 314.908, 323.328], [15, 459.34, 464.695, 314.908, 323.328], [15, 476.0, 481.35499999999996, 314.908, 323.328], [15, 492.65999999999997, 498.015, 314.908, 323.328], [15, 508.72499999999997, 515.865, 314.908, 323.328], [15, 525.385, 531.93, 314.908, 323.328], [15, 542.045, 549.185, 314.908, 323.328], [15, 109.47999999999999, 113.05, 376.37399999999997, 383.952], [15, 135.065, 139.23, 376.37399999999997, 383.952], [15, 161.84, 166.005, 376.37399999999997, 383.952], [15, 188.01999999999998, 192.185, 376.37399999999997, 383.952], [15, 213.605, 218.36499999999998, 376.37399999999997, 383.952], [15, 73.185, 77.945, 351.114, 359.534], [15, 73.185, 77.945, 339.32599999999996, 347.746], [15, 73.185, 77.945, 327.538, 335.95799999999997], [15, 73.185, 77.945, 314.908, 323.328], [15, 73.185, 77.945, 300.594, 309.014], [15, 73.185, 77.945, 287.964, 296.384], [15, 73.185, 77.945, 275.334, 283.75399999999996], [15, 73.185, 77.945, 261.86199999999997, 270.282], [15, 73.185, 77.945, 249.232, 257.652], [15, 69.615, 77.945, 235.76, 244.17999999999998], [15, 69.615, 77.945, 222.28799999999998, 230.708], [15, 69.615, 77.945, 208.816, 217.236], [15, 69.615, 77.945, 195.344, 203.76399999999998], [15, 69.615, 77.945, 181.87199999999999, 190.292], [15, 69.615, 75.565, 401.63399999999996, 410.054], [15, 69.615, 75.565, 389.00399999999996, 397.424], [15, 69.615, 75.565, 376.37399999999997, 383.952], [15, 69.615, 75.565, 362.902, 371.322], [15, 69.615, 75.565, 351.114, 359.534], [15, 69.615, 75.565, 339.32599999999996, 347.746], [15, 69.615, 75.565, 327.538, 335.95799999999997], [15, 69.615, 75.565, 314.908, 323.328], [15, 69.615, 75.565, 300.594, 309.014], [15, 69.615, 75.565, 287.964, 296.384], [15, 69.615, 75.565, 275.334, 283.75399999999996], [15, 69.615, 75.565, 261.86199999999997, 270.282], [15, 69.615, 75.565, 249.232, 257.652], [15, 69.615, 75.565, 235.76, 244.17999999999998], [15, 69.615, 75.565, 222.28799999999998, 230.708], [15, 69.615, 75.565, 208.816, 217.236], [15, 69.615, 75.565, 195.344, 203.76399999999998], [15, 69.615, 75.565, 181.87199999999999, 190.292], [15, 69.615, 75.565, 168.4, 176.82], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 69.615, 75.565, 195.344, 203.76399999999998], [15, 69.615, 75.565, 181.87199999999999, 190.292], [15, 69.615, 75.565, 168.4, 176.82], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 287.964, 296.384], [15, 69.615, 75.565, 275.334, 283.75399999999996], [15, 69.615, 75.565, 261.86199999999997, 270.282], [15, 69.615, 75.565, 249.232, 257.652], [15, 69.615, 75.565, 235.76, 244.17999999999998], [15, 69.615, 75.565, 222.28799999999998, 230.708], [15, 69.615, 75.565, 208.816, 217.236], [15, 69.615, 75.565, 195.344, 203.76399999999998], [15, 69.615, 75.565, 181.87199999999999, 190.292], [15, 69.615, 75.565, 168.4, 176.82], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 287.964, 296.384], [15, 69.615, 75.565, 275.334, 283.75399999999996], [15, 69.615, 75.565, 261.86199999999997, 270.282], [15, 69.615, 75.565, 249.232, 257.652], [15, 69.615, 75.565, 235.76, 244.17999999999998], [15, 69.615, 75.565, 222.28799999999998, 230.708], [15, 69.615, 75.565, 208.816, 217.236], [15, 69.615, 75.565, 195.344, 203.76399999999998], [15, 69.615, 75.565, 181.87199999999999, 190.292], [15, 69.615, 75.565, 168.4, 176.82], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 69.615, 75.565, 287.964, 296.384], [15, 69.615, 75.565, 275.334, 283.75399999999996], [15, 69.615, 75.565, 261.86199999999997, 270.282], [15, 69.615, 75.565, 249.232, 257.652], [15, 69.615, 75.565, 235.76, 244.17999999999998], [15, 69.615, 75.565, 222.28799999999998, 230.708], [15, 69.615, 75.565, 208.816, 217.236], [15, 69.615, 75.565, 195.344, 203.76399999999998], [15, 69.615, 75.565, 181.87199999999999, 190.292], [15, 69.615, 75.565, 168.4, 176.82], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 69.615, 75.565, 287.964, 296.384], [15, 69.615, 75.565, 275.334, 283.75399999999996], [15, 69.615, 75.565, 261.86199999999997, 270.282], [15, 69.615, 75.565, 249.232, 257.652], [15, 69.615, 75.565, 235.76, 244.17999999999998], [15, 69.615, 75.565, 222.28799999999998, 230.708], [15, 69.615, 75.565, 208.816, 217.236], [15, 69.615, 75.565, 195.344, 203.76399999999998], [15, 69.615, 75.565, 181.87199999999999, 190.292], [15, 69.615, 75.565, 168.4, 176.82], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 69.615, 75.565, 287.964, 296.384], [15, 69.615, 75.565, 275.334, 283.75399999999996], [15, 69.615, 75.565, 261.86199999999997, 270.282], [15, 69.615, 75.565, 249.232, 257.652], [15, 69.615, 75.565, 235.76, 244.17999999999998], [15, 69.615, 75.565, 222.28799999999998, 230.708], [15, 69.615, 75.565, 208.816, 217.236], [15, 69.615, 75.565, 195.344, 203.76399999999998], [15, 69.615, 75.565, 181.87199999999999, 190.292], [15, 69.615, 75.565, 168.4, 176.82], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 33.68, 42.1], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 20.208, 28.628], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 69.615, 75.565, 287.964, 296.384], [15, 69.615, 75.565, 275.334, 283.75399999999996], [15, 69.615, 75.565, 261.86199999999997, 270.282], [15, 69.615, 75.565, 249.232, 257.652], [15, 69.615, 75.565, 235.76, 244.17999999999998], [15, 69.615, 75.565, 222.28799999999998, 230.708], [15, 69.615, 75.565, 208.816, 217.236], [15, 69.615, 75.565, 195.344, 203.76399999999998], [15, 69.615, 75.565, 181.87199999999999, 190.292], [15, 69.615, 75.565, 168.4, 176.82], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 69.615, 75.565, 287.964, 296.384], [15, 69.615, 75.565, 275.334, 283.75399999999996], [15, 69.615, 75.565, 261.86199999999997, 270.282], [15, 69.615, 75.565, 249.232, 257.652], [15, 69.615, 75.565, 235.76, 244.17999999999998], [15, 69.615, 75.565, 222.28799999999998, 230.708], [15, 69.615, 75.565, 208.816, 217.236], [15, 69.615, 75.565, 195.344, 203.76399999999998], [15, 69.615, 75.565, 181.87199999999999, 190.292], [15, 69.615, 75.565, 168.4, 176.82], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 69.615, 75.565, 287.964, 296.384], [15, 69.615, 75.565, 275.334, 283.75399999999996], [15, 69.615, 75.565, 261.86199999999997, 270.282], [15, 69.615, 75.565, 249.232, 257.652], [15, 69.615, 75.565, 235.76, 244.17999999999998], [15, 69.615, 75.565, 222.28799999999998, 230.708], [15, 69.615, 75.565, 208.816, 217.236], [15, 69.615, 75.565, 195.344, 203.76399999999998], [15, 69.615, 75.565, 181.87199999999999, 190.292], [15, 69.615, 75.565, 168.4, 176.82], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 33.68, 42.1], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 20.208, 28.628], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 69.615, 75.565, 261.86199999999997, 270.282], [15, 69.615, 75.565, 249.232, 257.652], [15, 69.615, 75.565, 235.76, 244.17999999999998], [15, 69.615, 75.565, 222.28799999999998, 230.708], [15, 69.615, 75.565, 208.816, 217.236], [15, 69.615, 75.565, 195.344, 203.76399999999998], [15, 69.615, 75.565, 181.87199999999999, 190.292], [15, 69.615, 75.565, 168.4, 176.82], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 287.964, 296.384], [15, 69.615, 75.565, 275.334, 283.75399999999996], [15, 69.615, 75.565, 261.86199999999997, 270.282], [15, 69.615, 75.565, 249.232, 257.652], [15, 69.615, 75.565, 235.76, 244.17999999999998], [15, 69.615, 75.565, 222.28799999999998, 230.708], [15, 69.615, 75.565, 208.816, 217.236], [15, 69.615, 75.565, 195.344, 203.76399999999998], [15, 69.615, 75.565, 181.87199999999999, 190.292], [15, 69.615, 75.565, 168.4, 176.82], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 219.55499999999998, 225.505, 6.736, 15.155999999999999], [15, 236.215, 242.165, 6.736, 15.155999999999999], [15, 252.875, 258.825, 6.736, 15.155999999999999], [15, 269.53499999999997, 275.485, 6.736, 15.155999999999999], [15, 286.195, 292.145, 6.736, 15.155999999999999], [15, 302.85499999999996, 308.805, 6.736, 15.155999999999999], [15, 319.515, 325.465, 6.736, 15.155999999999999], [15, 336.175, 342.125, 6.736, 15.155999999999999], [15, 352.835, 358.78499999999997, 6.736, 15.155999999999999], [15, 369.495, 375.445, 6.736, 15.155999999999999], [15, 386.155, 392.10499999999996, 6.736, 15.155999999999999], [15, 402.815, 408.765, 6.736, 15.155999999999999], [15, 419.47499999999997, 425.42499999999995, 6.736, 15.155999999999999], [15, 436.135, 442.085, 6.736, 15.155999999999999], [15, 452.79499999999996, 458.745, 6.736, 15.155999999999999], [15, 469.455, 475.405, 6.736, 15.155999999999999], [15, 486.11499999999995, 492.065, 6.736, 15.155999999999999], [15, 502.775, 508.72499999999997, 6.736, 15.155999999999999], [15, 519.435, 525.385, 6.736, 15.155999999999999], [15, 536.095, 542.045, 6.736, 15.155999999999999], [15, 552.755, 558.7049999999999, 6.736, 15.155999999999999], [15, 569.415, 575.365, 6.736, 15.155999999999999], [15, 586.0749999999999, 592.025, 6.736, 15.155999999999999], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 47.152, 55.571999999999996], [15, 69.615, 75.565, 33.68, 42.1], [15, 69.615, 75.565, 20.208, 28.628], [15, 69.615, 75.565, 6.736, 15.155999999999999], [15, 86.27499999999999, 92.225, 6.736, 15.155999999999999], [15, 102.935, 108.88499999999999, 6.736, 15.155999999999999], [15, 119.595, 125.54499999999999, 6.736, 15.155999999999999], [15, 136.255, 142.20499999999998, 6.736, 15.155999999999999], [15, 152.915, 158.86499999999998, 6.736, 15.155999999999999], [15, 169.575, 175.525, 6.736, 15.155999999999999], [15, 186.23499999999999, 192.185, 6.736, 15.155999999999999], [15, 202.89499999999998, 208.845, 6.736, 15.155999999999999], [15, 69.615, 75.565, 261.86199999999997, 270.282], [15, 69.615, 75.565, 249.232, 257.652], [15, 69.615, 75.565, 235.76, 244.17999999999998], [15, 69.615, 75.565, 222.28799999999998, 230.708], [15, 69.615, 75.565, 208.816, 217.236], [15, 69.615, 75.565, 195.344, 203.76399999999998], [15, 69.615, 75.565, 181.87199999999999, 190.292], [15, 69.615, 75.565, 168.4, 176.82], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 287.964, 296.384], [15, 69.615, 75.565, 275.334, 283.75399999999996], [15, 69.615, 75.565, 261.86199999999997, 270.282], [15, 69.615, 75.565, 249.232, 257.652], [15, 69.615, 75.565, 235.76, 244.17999999999998], [15, 69.615, 75.565, 222.28799999999998, 230.708], [15, 69.615, 75.565, 208.816, 217.236], [15, 69.615, 75.565, 195.344, 203.76399999999998], [15, 69.615, 75.565, 181.87199999999999, 190.292], [15, 69.615, 75.565, 168.4, 176.82], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 287.964, 296.384], [15, 69.615, 75.565, 275.334, 283.75399999999996], [15, 69.615, 75.565, 261.86199999999997, 270.282], [15, 69.615, 75.565, 249.232, 257.652], [15, 69.615, 75.565, 235.76, 244.17999999999998], [15, 69.615, 75.565, 222.28799999999998, 230.708], [15, 69.615, 75.565, 208.816, 217.236], [15, 69.615, 75.565, 195.344, 203.76399999999998], [15, 69.615, 75.565, 181.87199999999999, 190.292], [15, 69.615, 75.565, 168.4, 176.82], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 287.964, 296.384], [15, 69.615, 75.565, 275.334, 283.75399999999996], [15, 69.615, 75.565, 261.86199999999997, 270.282], [15, 69.615, 75.565, 249.232, 257.652], [15, 69.615, 75.565, 235.76, 244.17999999999998], [15, 69.615, 75.565, 222.28799999999998, 230.708], [15, 69.615, 75.565, 208.816, 217.236], [15, 69.615, 75.565, 195.344, 203.76399999999998], [15, 69.615, 75.565, 181.87199999999999, 190.292], [15, 69.615, 75.565, 168.4, 176.82], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 287.964, 296.384], [15, 69.615, 75.565, 275.334, 283.75399999999996], [15, 69.615, 75.565, 261.86199999999997, 270.282], [15, 69.615, 75.565, 249.232, 257.652], [15, 69.615, 75.565, 235.76, 244.17999999999998], [15, 69.615, 75.565, 222.28799999999998, 230.708], [15, 69.615, 75.565, 208.816, 217.236], [15, 69.615, 75.565, 195.344, 203.76399999999998], [15, 69.615, 75.565, 181.87199999999999, 190.292], [15, 69.615, 75.565, 168.4, 176.82], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 287.964, 296.384], [15, 69.615, 75.565, 275.334, 283.75399999999996], [15, 69.615, 75.565, 261.86199999999997, 270.282], [15, 69.615, 75.565, 249.232, 257.652], [15, 69.615, 75.565, 235.76, 244.17999999999998], [15, 69.615, 75.565, 222.28799999999998, 230.708], [15, 69.615, 75.565, 208.816, 217.236], [15, 69.615, 75.565, 195.344, 203.76399999999998], [15, 69.615, 75.565, 181.87199999999999, 190.292], [15, 69.615, 75.565, 168.4, 176.82], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 287.964, 296.384], [15, 69.615, 75.565, 275.334, 283.75399999999996], [15, 69.615, 75.565, 261.86199999999997, 270.282], [15, 69.615, 75.565, 249.232, 257.652], [15, 69.615, 75.565, 235.76, 244.17999999999998], [15, 69.615, 75.565, 222.28799999999998, 230.708], [15, 69.615, 75.565, 208.816, 217.236], [15, 69.615, 75.565, 195.344, 203.76399999999998], [15, 69.615, 75.565, 181.87199999999999, 190.292], [15, 69.615, 75.565, 168.4, 176.82], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 141.456, 149.876], [15, 69.615, 75.565, 127.984, 136.404], [15, 69.615, 75.565, 114.512, 122.932], [15, 69.615, 75.565, 101.03999999999999, 109.46], [15, 69.615, 75.565, 87.568, 95.988], [15, 69.615, 75.565, 74.096, 82.51599999999999], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 60.623999999999995, 69.044], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 154.928, 163.34799999999998], [15, 69.615, 75.565, 287.964, 296.384], [15, 69.615, 75.565, 275.334, 283.75399999999996], [15, 69.615, 75.565, 261.86199999999997, 270.282], [15, 69.615, 75.565, 249.232, 257.652], [15, 69.615, 75.565, 235.76, 244.17999999999998]]
2026-08-06 02:25:14,897 INFO     29 [qwen-vl-text] ═══ DONE ═══ 2884 positions, pages=1, time=83.4s
2026-08-06 02:25:14,911 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-06 02:25:14,912 INFO     29 [Trace] task=5d401ece | doc=LZK 哮喘 广三(1).pdf | Extractor:ExaminationReport | outputs={"chunks": "3 items, types={'ExaminationReport': 3}", "html": "", "json": "3678 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "chunks", "chunks_Clinical": "5 items, types={'OutpatientRecord': 5}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 5, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-06 02:25:14,912 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-06 02:25:14,912 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T02:25:14.912+00:00", "boot_at": "2026-08-06T01:59:43.412+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"5d401ece913c11f19b5e81513a69a703": {"id": "5d401ece913c11f19b5e81513a69a703", "doc_id": "5963bc44913b11f19b5e81513a69a703", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785982387379, "task_type": "dataflow", "root_trace_id": "7886908ae2584ba69682631c2a66f747", "root_traceparent": "00-7886908ae2584ba69682631c2a66f747-971004a6101741b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 02:25:14,919 INFO     29 [ChunkMerger] Merged 15 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 5, 'Extractor:Medication': 1, 'Extractor:Prescription': 7, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 3} (filtered 5 noise chunks)
2026-08-06 02:25:15,647 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-06 02:25:15,648 INFO     29 [Trace] task=5d401ece | doc=LZK 哮喘 广三(1).pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "15 items, types={'OutpatientRecord': 5, 'PrescriptionRecord': 7, 'ExaminationReport': 3}", "name": "LZK 哮喘 广三(1).pdf"}
2026-08-06 02:25:15,648 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-06 02:25:16,849 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1785982393795, 'update_date': datetime.datetime(2026, 8, 6, 2, 13, 13), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 408305, 'status': '1'}
2026-08-06 02:25:17,116 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=病历编号：
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
头降使用40瓶，平均每天使用4瓶，2025年9月10日用空4瓶（大木使用试验药剂空瓶2次共4
瓶，2025年9月10日后受试者每七天清光一次后空瓶5次共10瓶，合计空瓶10瓶（qrs记录使
用总共46瓶，与实际使用情况一致。
8、回访qrs以及MD。
既往史：更新合并用药：
1、鼻腔莫米松鼻喷雾剂C025 4 3-2025 7 25 每鼻 2喷/次 qd 治疗过敏性鼻炎。
2、苯环喹莫铵鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。
4、氯卓斯汀氟替卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。
5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/
次 治疗过敏性鼻炎。
6、枯草抗感染治疗（生理性海水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过
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
---
就诊卡
流水号：
姓名
龄：40岁
就诊科
目：2025-10-24 15:45:39
主诉：安全性电话随访
现病史：今日10:27
固定电话（020-
(159
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
---
病历编号：
姓名：
性别：
年龄：40岁
就诊科：
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
复方甲氧那明胶囊(省采)●② 1瓶 1.0粒,餐后口服,一天3次(口服) 5天
盐酸氨溴索分散片(省采)●⑥ 15片 30.0mg,餐后口服,一天3次(口服) 5
天
醋酸泼尼松片●②④ 6片 10.0mg,口服,每早1次(口服) 3天
备 注:建议在住地附近社区医疗机构随诊。
---
门诊/住院病历信息
就诊卡号：0
病历编号：
姓名：
性别：男
年龄：41岁
就诊科室：内科门诊（荔湾）
就诊时间：2026-02-04 11:21:11
主诉：支气管哮喘治疗后复查
现病史：2021年2月前开始出现咳嗽、哮喘，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sg 2吸 bid治疗。
既往史：鼻炎病史无规则治疗，打鼾明显。
过敏史：未发现；
个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。
体格检查：神志清，颈软，双肺呼吸音粗，可闻及散在哮鸣音，口腔粘膜无白斑。
专科情况：
辅助检查：
治疗项目：
门诊诊断：
1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎
单病种：
发病时间：
处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不遥随诊。
布地奈德福莫特罗吸入粉雾剂(II)(省
2 2.0班,吸入用药,一天2次
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
布地奈德福莫特罗吸入粉雾剂0.125/0.006*60吸6盒
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
就诊时间:2025-02-26
就诊科室:内科门诊
主诊
性别:男
年龄:40岁
卡号
医疗证号:
处方
015
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
布地奈德福莫特罗吸入粉雾剂BDII/●@0.1g*60吸2盒
183.41 366.82
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
布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●⑥ug*60吸2盒
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
主诊
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
联系电
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
0.072
0.078
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
6
7
8V(l)
FEV1
ATS
12t(s)
-1
0
1
2
3
4
5
6
7
8
9
10
11
12
1
2
3
4
5
6
7
8
9
10
11
12
13
14
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
747
748
749
750
751
752
753
754
755
756
757
758
759
760
761
762
763
764
765
766
767
768
769
770
771
772
773
774
775
776
777
778
779
780
781
782
783
784
785
786
787
788
789
790
791
792
793
794
795
796
797
798
799
800
801
802
803
804
805
806
807
808
809
810
811
812
813
814
815
816
817
818
819
820
821
822
823
824
825
826
827
828
829
830
831
832
833
834
835
836
837
838
839
840
841
842
843
844
845
846
847
848
849
850
851
852
853
854
855
856
857
858
859
860
861
862
863
864
865
866
867
868
869
870
871
872
873
874
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
890
891
892
893
894
895
896
897
898
899
900
901
902
903
904
905
906
907
908
909
910
911
912
913
914
915
916
917
918
919
920
921
922
923
924
925
926
927
928
929
930
931
932
933
934
935
936
937
938
939
940
941
942
943
944
945
946
947
948
949
950
951
952
953
954
955
956
957
958
959
960
961
962
963
964
965
966
967
968
969
970
971
972
973
974
975
976
977
978
979
980
981
982
983
984
985
986
987
988
989
990
991
992
993
994
995
996
997
998
999
1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
1010
1011
1012
1013
1014
1015
1016
1017
1018
1019
1020
1021
1022
1023
1024
1025
1026
1027
1028
1029
1030
1031
1032
1033
1034
1035
1036
1037
1038
1039
1040
1041
1042
1043
1044
1045
1046
1047
1048
1049
1050
1051
1052
1053
1054
1055
1056
1057
1058
1059
1060
1061
1062
1063
1064
1065
1066
1067
1068
1069
1070
1071
1072
1073
1074
1075
1076
1077
1078
1079
1080
1081
1082
1083
1084
1085
1086
1087
1088
1089
1090
1091
1092
1093
1094
1095
1096
1097
1098
1099
1100
1101
1102
1103
1104
1105
1106
1107
1108
1109
1110
1111
1112
1113
1114
1115
1116
1117
1118
1119
1120
1121
1122
1123
1124
1125
1126
1127
1128
1129
1130
1131
1132
1133
1134
1135
1136
1137
1138
1139
1140
1141
1142
1143
1144
1145
1146
1147
1148
1149
1150
1151
1152
1153
1154
1155
1156
1157
1158
1159
1160
1161
1162
1163
1164
1165
1166
1167
1168
1169
1170
1171
1172
1173
1174
1175
1176
1177
1178
1179
1180
1181
1182
1183
1184
1185
1186
1187
1188
1189
1190
1191
1192
1193
1194
1195
1196
1197
1198
1199
1200
1201
1202
1203
1204
1205
1206
1207
1208
1209
1210
1211
1212
1213
1214
1215
1216
1217
1218
1219
1220
1221
1222
1223
1224
1225
1226
1227
1228
1229
1230
1231
1232
1233
1234
1235
1236
1237
1238
1239
1240
1241
1242
1243
1244
1245
1246
1247
1248
1249
1250
1251
1252
1253
1254
1255
1256
1257
1258
1259
1260
1261
1262
1263
1264
1265
1266
1267
1268
1269
1270
1271
1272
1273
1274
1275
1276
1277
1278
1279
1280
1281
1282
1283
1284
1285
1286
1287
1288
1289
1290
1291
1292
1293
1294
1295
1296
1297
1298
1299
1300
1301
1302
1303
1304
1305
1306
1307
1308
1309
1310
1311
1312
1313
1314
1315
1316
1317
1318
1319
1320
1321
1322
1323
1324
1325
1326
1327
1328
1329
1330
1331
1332
1333
1334
1335
1336
1337
1338
1339
1340
1341
1342
1343
1344
1345
1346
1347
1348
1349
1350
1351
1352
1353
1354
1355
1356
1357
1358
1359
1360
1361
1362
1363
1364
1365
1366
1367
1368
1369
1370
1371
1372
1373
1374
1375
1376
1377
1378
1379
1380
1381
1382
1383
1384
1385
1386
1387
1388
1389
1390
1391
1392
1393
1394
1395
1396
1397
1398
1399
1400
1401
1402
1403
1404
1405
1406
1407
1408
1409
1410
1411
1412
1413
1414
1415
1416
1417
1418
1419
1420
1421
1422
1423
1424
1425
1426
1427
1428
1429
1430
1431
1432
1433
1434
1435
1436
1437
1438
1439
1440
1441
1442
1443
1444
1445
1446
1447
1448
1449
1450
1451
1452
1453
1454
1455
1456
1457
1458
1459
1460
1461
1462
1463
1464
1465
1466
1467
1468
1469
1470
1471
1472
1473
1474
1475
1476
1477
1478
1479
1480
1481
1482
1483
1484
1485
1486
1487
1488
1489
1490
1491
1492
1493
1494
1495
1496
1497
1498
1499
1500
1501
1502
1503
1504
1505
1506
1507
1508
1509
1510
1511
1512
1513
1514
1515
1516
1517
1518
1519
1520
1521
1522
1523
1524
1525
1526
1527
1528
1529
1530
1531
1532
1533
1534
1535
1536
1537
1538
1539
1540
1541
1542
1543
1544
1545
1546
1547
1548
1549
1550
1551
1552
1553
1554
1555
1556
1557
1558
1559
1560
1561
1562
1563
1564
1565
1566
1567
1568
1569
1570
1571
1572
1573
1574
1575
1576
1577
1578
1579
1580
1581
1582
1583
1584
1585
1586
1587
1588
1589
1590
1591
1592
1593
1594
1595
1596
1597
1598
1599
1600
1601
1602
1603
1604
1605
1606
1607
1608
1609
1610
1611
1612
1613
1614
1615
1616
1617
1618
1619
1620
1621
1622
1623
1624
1625
1626
1627
1628
1629
1630
1631
1632
1633
1634
1635
1636
1637
1638
1639
1640
1641
1642
1643
1644
1645
1646
1647
1648
1649
1650
1651
1652
1653
1654
1655
1656
1657
1658
1659
1660
1661
1662
1663
1664
1665
1666
1667
1668
1669
1670
1671
1672
1673
1674
1675
1676
1677
1678
1679
1680
1681
1682
1683
1684
1685
1686
1687
1688
1689
1690
1691
1692
1693
1694
1695
1696
1697
1698
1699
1700
1701
1702
1703
1704
1705
1706
1707
1708
1709
1710
1711
1712
1713
1714
1715
1716
1717
1718
1719
1720
1721
1722
1723
1724
1725
1726
1727
1728
1729
1730
1731
1732
1733
1734
1735
1736
1737
1738
1739
1740
1741
1742
1743
1744
1745
1746
1747
1748
1749
1750
1751
1752
1753
1754
1755
1756
1757
1758
1759
1760
1761
1762
1763
1764
1765
1766
1767
1768
1769
1770
1771
1772
1773
1774
1775
1776
1777
1778
1779
1780
1781
1782
1783
1784
1785
1786
1787
1788
1789
1790
1791
1792
1793
1794
1795
1796
1797
1798
1799
1800
1801
1802
1803
1804
1805
1806
1807
1808
1809
1810
1811
1812
1813
1814
1815
1816
1817
1818
1819
1820
1821
1822
1823
1824
1825
1826
1827
1828
1829
1830
1831
1832
1833
1834
1835
1836
1837
1838
1839
1840
1841
1842
1843
1844
1845
1846
1847
1848
1849
1850
1851
1852
1853
1854
1855
1856
1857
1858
1859
1860
1861
1862
1863
1864
1865
1866
1867
1868
1869
1870
1871
1872
1873
1874
1875
1876
1877
1878
1879
1880
1881
1882
1883
1884
1885
1886
1887
1888
1889
1890
1891
1892
1893
1894
1895
1896
1897
1898
1899
1900
1901
1902
1903
1904
1905
1906
1907
1908
1909
1910
1911
1912
1913
1914
1915
1916
1917
1918
1919
1920
1921
1922
1923
1924
1925
1926
1927
1928
1929
1930
1931
1932
1933
1934
1935
1936
1937
1938
1939
1940
1941
1942
1943
1944
1945
1946
1947
1948
1949
1950
1951
1952
1953
1954
1955
1956
1957
1958
1959
1960
1961
1962
1963
1964
1965
1966
1967
1968
1969
1970
1971
1972
1973
1974
1975
1976
1977
1978
1979
1980
1981
1982
1983
1984
1985
1986
1987
1988
1989
1990
1991
1992
1993
1994
1995
1996
1997
1998
1999
2000
2001
2002
2003
2004
2005
2006
2007
2008
2009
2010
2011
2012
2013
2014
2015
2016
2017
2018
2019
2020
2021
2022
2023
2024
2025
2026
2027
2028
2029
2030
2031
2032
2033
2034
2035
2036
2037
2038
2039
2040
2041
2042
2043
2044
2045
2046
2047
2048
2049
2050
2051
2052
2053
2054
2055
2056
2057
2058
2059
2060
2061
2062
2063
2064
2065
2066
2067
2068
2069
2070
2071
2072
2073
2074
2075
2076
2077
2078
2079
2080
2081
2082
2083
2084
2085
2086
2087
2088
2089
2090
2091
2092
2093
2094
2095
2096
2097
2098
2099
2100
2101
2102
2103
2104
2105
2106
2107
2108
2109
2110
2111
2112
2113
2114
2115
2116
2117
2118
2119
2120
2121
2122
2123
2124
2125
2126
2127
2128
2129
2130
2131
2132
2133
2134
2135
2136
2137
2138
2139
2140
2141
2142
2143
2144
2145
2146
2147
2148
2149
2150
2151
2152
2153
2154
2155
2156
2157
2158
2159
2160
2161
2162
2163
2164
2165
2166
2167
2168
2169
2170
2171
2172
2173
2174
2175
2176
2177
2178
2179
2180
2181
2182
2183
2184
2185
2186
2187
2188
2189
2190
2191
2192
2193
2194
2195
2196
2197
2198
2199
2200
2201
2202
2203
2204
2205
2206
2207
2208
2209
2210
2211
2212
2213
2214
2215
2216
2217
2218
2219
2220
2221
2222
2223
2224
2225
2226
2227
2228
2229
2230
2231
2232
2233
2234
2235
2236
2237
2238
2239
2240
2241
2242
2243
2244
2245
2246
2247
2248
2249
2250
2251
2252
2253
2254
2255
2256
2257
2258
2259
2260
2261
2262
2263
2264
2265
2266
2267
2268
2269
2270
2271
2272
2273
2274
2275
2276
2277
2278
2279
2280
2281
2282
2283
2284
2285
2286
2287
2288
2289
2290
2291
2292
2293
2294
2295
2296
2297
2298
2299
2300
2301
2302
2303
2304
2305
2306
2307
2308
2309
2310
2311
2312
2313
2314
2315
2316
2317
2318
2319
2320
2321
2322
2323
2324
2325
2326
2327
2328
2329
2330
2331
2332
2333
2334
2335
2336
2337
2338
2339
2340
2341
2342
2343
2344
2345
2346
2347
2348
2349
2350
2351
2352
2353
2354
2355
2356
2357
2358
2359
2360
2361
2362
2363
2364
2365
2366
2367
2368
2369
2370
2371
2372
2373
2374
2375
2376
2377
2378
2379
2380
2381
2382
2383
2384
2385
2386
2387
2388
2389
2390
2391
2392
2393
2394
2395
2396
2397
2398
2399
2400
2401
2402
2403
2404
2405
2406
2407
2408
2409
2410
2411
2412
2413
2414
2415
2416
2417
2418
2419
2420
2421
2422
2423
2424
2425
2426
2427
2428
2429
2430
2431
2432
2433
2434
2435
2436
2437
2438
2439
2440
2441
2442
2443
2444
2445
2446
2447
2448
2449
2450
2451
2452
2453
2454
2455
2456
2457
2458
2459
2460
2461
2462
2463
2464
2465
2466
2467
2468
2469
2470
2471
2472
2473
2474
2475
2476
2477
2478
2479
2480
2481
2482
2483
2484
2485
2486
2487
2488
2489
2490
2491
2492
2493
2494
2495
2496
2497
2498
2499
2500
2501
2502
2503
2504
2505
2506
2507
2508
2509
2510
2511
2512
2513
2514
2515
2516
2517
2518
2519
2520
2521
2522
2523
2524
2525
2526
2527
2528
2529
2530
2531
2532
2533
2534
2535
2536
2537
2538
2539
2540
2541
2542
2543
2544
2545
2546
2547
2548
2549
2550
2551
2552
2553
2554
2555
2556
2557
2558
2559
2560
2561
2562
2563
2564
2565
2566
2567
2568
2569
2570
2571
2572
2573
2574
2575
2576
2577
2578
2579
2580
2581
2582
2583
2584
2585
2586
2587
2588
2589
2590
2591
2592
2593
2594
2595
2596
2597
2598
2599
2600
2601
2602
2603
2604
2605
2606
2607
2608
2609
2610
2611
2612
2613
2614
2615
2616
2617
2618
2619
2620
2621
2622
2623
2624
2625
2626
2627
2628
2629
2630
2631
2632
2633
2634
2635
2636
2637
2638
2639
2640
2641
2642
2643
2644
2645
2646
2647
2648
2649
2650
2651
2652
2653
2654
2655
2656
2657
2658
2659
2660
2661
2662
2663
2664
2665
2666
2667
2668
2669
2670
2671
2672
2673
2674
2675
2676
2677
2678
2679
2680
2681
2682
2683
2684
2685
2686
2687
2688
2689
2690
2691
2692
2693
2694
2695
2696
2697
2698
2699
2700
2701
2702
2703
2704
2705
2706
2707
2708
2709
2710
2711
2712
2713
2714
2715
2716
2717
2718
2719
2720
2721
2722
2723
2724
2725
2726
2727
2728
2729
2730
2731
2732
2733
2734
2735
2736
2737
2738
2739
2740
2741
2742
2743
2744
2745
2746
2747
2748
2749
2750
2751
2752
2753
2754
2755
2756
2757
2758
2759
2760
2761
2762
2763
2764
2765
2766
2767
2768
2769
2770
2771
2772
2773
2774
2775
2776
2777
2778
2779
2780
2781
2782
2783
2784
2785
2786
2787
2788
2789
2790
2791
2792
2793
2794
2795
2796
2797
2798
2799
2800
2801
2802
2803
2804
2805
2806
2807
2808
2809
2810
2811
2812
2813
2814
2026-08-06 02:25:18,782 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-06 02:25:18,782 INFO     29 [Trace] task=5d401ece | doc=LZK 哮喘 广三(1).pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "15 items, types={'OutpatientRecord': 5, 'PrescriptionRecord': 7, 'ExaminationReport': 3}", "name": "LZK 哮喘 广三(1).pdf", "embedding_token_consumption": 21055}
2026-08-06 02:25:18,782 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-06 02:25:18,985 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-06 02:25:18,985 INFO     29 [Trace] task=5d401ece | doc=LZK 哮喘 广三(1).pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":15,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-06 02:25:18,996 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 02:25:18,996 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 02:25:18,996 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 02:25:18,996 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 02:25:18,996 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 02:25:18,997 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 02:25:18,997 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 02:25:18,997 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 02:25:18,997 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 02:25:18,997 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 02:25:18,998 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 02:25:18,998 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 02:25:18,998 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 02:25:18,999 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 02:25:19,000 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 02:25:19,006 INFO     29 set_progress(5d401ece913c11f19b5e81513a69a703), progress: 0.82, progress_msg: 02:25:19 [DOC Engine]:
Start to index...
2026-08-06 02:25:19,107 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.095s]
2026-08-06 02:25:19,116 INFO     29 set_progress(5d401ece913c11f19b5e81513a69a703), progress: 0.8066666666666668, progress_msg: 
2026-08-06 02:25:19,153 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.029s]
2026-08-06 02:25:19,192 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.017s]
2026-08-06 02:25:19,219 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.015s]
2026-08-06 02:25:19,233 INFO     29 set_progress(5d401ece913c11f19b5e81513a69a703), progress: 1.0, progress_msg: 02:25:19 Indexing done (0.22s). Task done (668.68s)
2026-08-06 02:25:19,238 INFO     29 [Done], chunks(15), token(21055), elapsed:668.68
2026-08-06 02:25:19,701 INFO     29 handle_task done for task {"id": "5d401ece913c11f19b5e81513a69a703", "doc_id": "5963bc44913b11f19b5e81513a69a703", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1785982387379, "task_type": "dataflow", "root_trace_id": "7886908ae2584ba69682631c2a66f747", "root_traceparent": "00-7886908ae2584ba69682631c2a66f747-971004a6101741b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
