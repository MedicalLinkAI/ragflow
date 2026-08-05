# 基准结果：LZK 哮喘 广三(1).pdf

## 基本信息

- 文件：`LZK 哮喘 广三(1).pdf`
- 大小：5325.3 KB
- PDF 总页数：16
- doc_id：`4e10ceb4908b11f1a3da71efcdd7cc1f`
- 上传方式：existing
- 状态：run=None (code=None)  progress=None
- 开始时间：2026-08-05T14:31:15  完成时间：2026-08-05T14:31:16  耗时：1.0s
- progress_msg：`05:16:36 Indexing done (0.13s). Task done (597.77s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | cb1c169e | 4 | 1-4 | 病历编号： 性别：男 年龄：40岁 就诊科室：内科门诊（荔湾） 就诊时间：202 |
| 2 | eb054f5d | 1 | 5-5 | 门(急)诊处方 就诊时间:2025-07-18 就诊科室:内科门诊 主诊医 姓名 |
| 3 | f9fb6ec0 | 1 | 6-6 | 门(急)诊处方 就诊时间:2025-04-25 就诊科室:内科门诊 主诊 姓名  |
| 4 | 0916bd90 | 1 | 7-7 | 门(急)诊处方 就诊时间：2025-02-26 就诊科室：内科门诊 主诊 性别： |
| 5 | 052655c7 | 1 | 8-8 | 门(急)诊处方 就诊时间:2025-01-24 就诊科室:内科门诊 主诊医 姓名 |
| 6 | c245201a | 1 | 9-9 | 门(急)诊处方 就诊时间:2025-01-03 就诊科室:内科门诊 主诊 性别: |
| 7 | 7fd448ce | 2 | 9-10 | CS 扫描全能王 3亿人都在用的扫描App 门(急)诊处方 就诊时间:2024- |
| 8 | 11f761f1 | 1 | 11-11 | 激发试验检查报告 姓名： 测试号： 门诊/住院号： 000 年龄： 出生日期：  |
| 9 | afffd809 | 2 | 11-12 | CS 扫描全能王 3亿人都在用的扫描App 检查日期：2021/1/21 检查时 |
| 10 | bc0673f1 | 2 | 12-13 | CS 扫描全能王 3亿人都在用的扫描App 广州医科大学附属第三医院 处方笺 普 |
| 11 | 75ae8653 | 1 | 14-14 | 广州医科大学附属第三医院 The Third Affiliated Hospit |
| 12 | 75f09510 | 1 | 15-15 | 门诊/住院病历信息 就诊卡号： 病历编号： 姓名： 性别：男 年龄：41岁 就诊 |
| 13 | f7c8b80d | 1 | 16-16 | 广州医科大学附属第三医院 肺功能检查报告 地址：广州市多宝路63号 电话：020 |

- chunks 总数：13
- 各 chunk 页数合计（含跨页重复）：19
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]`
- 覆盖页数：16 / 16；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 3 | 0 | 3 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 7 | 7 | 7 | encounter_date, prescriber, diagnosis | **OK** |
| ExaminationReport | 检查报告 | 3 | 3 | 3 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 3, "PrescriptionRecord": 7, "ExaminationReport": 3}`
- ChunkMerger：`{"found": true, "merged": 13, "sources": 8, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 3, "Extractor:Medication": 1, "Extractor:Prescription": 7, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 3}, "filtered_noise": 5}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-05 05:16:33,929 INFO     29 [ChunkMerger] Merged 13 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 3, 'Extractor:Medication': 1, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-05 05:05:42,450 INFO     29 handle_task begin for task {"id": "4e4700ce908b11f1a3da71efcdd7cc1f", "doc_id": "4e10ceb4908b11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906341337, "task_type": "dataflow", "root_trace_id": "ca345e6640ff4d788f444c3ab712853e", "root_traceparent": "00-ca345e6640ff4d788f444c3ab712853e-8ea193cced1ce3aa-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-05 05:05:42,649 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-05 05:05:42,688 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-05 05:05:42,698 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-05 05:05:42,698 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-05 05:05:42,708 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-05 05:05:42,708 INFO     29 ============================================================
2026-08-05 05:05:42,708 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-05 05:05:42,708 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-05 05:05:42,708 INFO     29 ============================================================
2026-08-05 05:05:42,708 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-05 05:05:42,708 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-05 05:05:42,716 INFO     29 No torch found.
2026-08-05 05:05:44,392 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=16
2026-08-05 05:05:44,581 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1449002, prompt_len=644
2026-08-05 05:05:45,959 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:05:45,959 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-05 05:05:45,966 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1449002, prompt_len=401
2026-08-05 05:05:52,519 INFO     29 [qwen-vl-parser] text API response (len=1148):
["病历编号：", "性别：男", "年龄：40岁", "就诊科室：内科门诊（荔湾）", "就诊时间：2025-10-10 14:36:06", "主诉：BAIYUN V8", "现病史：自上次访视至今，询问及查询HIS系统受试者有新增AE，无SAE、哮喘急性发作，有新增合并用药，发生2次医疗相关事件[2025年9月3日因过敏性鼻炎就诊专科门诊、本周曾因上呼吸道感染到社区医院就诊(具体不详，因HIS系统滞后无法收集具体情况及受试者无法回忆起当时情况及用药情况，待收集具体情况后补充详情)]。于2025年8月4日、2025年9月1日收到加重警报邮件，联系受试者后，均判断非哮喘急性发作。", "完成下流操作：", "1、查看受试者电子日志，受试者漏填2025年8月16日，2025年9月4日晚间日志，2025年9月4日、2025年9月25日早间日志；", "2、填写AQLQ+12和ACQ-5问卷，ACQ-5评分：0.8分；", "3、休息10分钟后，测量坐位生命体征：血压113/81mmHg，脉搏87次/分，呼吸频率20次/分，体温36.6℃，测量身高177.5cm，体重90.5kg(BMI=28.7kg/m2)；", "4、14:35体格检查：神志清，体查合作，自主体位，一般外表无异常，皮肤、粘膜无异常，唇甲无发绀，眼睛、耳、鼻、咽喉无异常，口咽部粘膜无异常，颈软，气管居中，甲状腺未及肿大，全身浅表淋巴结未及肿大，颈静脉无怒张，胸廓无畸形，双肺呼吸运动对称，双肺触觉语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及啰音。心前区无隆起，心尖搏动无弥散，心界不大，心率：87次/分，律齐，各瓣膜听诊区未闻及病理性杂音。腹平软，全腹无压痛、反跳痛。肝、脾肋下未及，肝肾区无叩击痛，肠鸣音存，4次/分，脊柱、四肢无畸形，生理征存，未引出病理征，其他系统未见明显异常；", "5、休息至少10分钟后，于14:58行12导联ECG检查；", "6、于15:01采集中心实验室样本(血常规，血生化)并送往中心试验室；", "7、回收试验药物BDAMDI@ASMDI3盒(152968-AH及185936-HK未开封，148729-UA未用60揿，实际使用46揿，发药当天预喷4揿，2025年9月10日前因超过7天未使用试验药物空喷2次共4揿，2025年9月10日后受试者每七天清洗一次后空喷5次共10揿，总计预喷18揿；epro记录使用总共46揿，与实际使用情况一致。", "8、回收epro以及AM3。", "既往史：更新合并用药：", "1、糠酸莫米松鼻喷雾剂2025.4.3-2025.7.25 每鼻 2喷/次 qm 治疗过敏性鼻炎。", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:05:52,520 INFO     29 [qwen-vl-parser] page=1 text: 20 lines (bbox 0-19)
2026-08-05 05:05:52,520 INFO     29 [qwen-vl-parser] page=1 text: 20 sections
2026-08-05 05:05:52,623 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=608187, prompt_len=644
2026-08-05 05:05:53,919 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:05:53,919 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-05 05:05:53,932 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=608187, prompt_len=401
2026-08-05 05:05:58,542 INFO     29 [qwen-vl-parser] text API response (len=803):
["病历文书", "门诊病历", "25/10/10 14时 门诊病历", "25/10/24 15时 门诊病历（GCP专用）", "25/11/17 10时 门诊病历", "头降使用40瓶，平均每天使用4瓶，2025年9月10日用完4瓶（未使用试验药剂空瓶2次共4", "瓶，2025年9月10日后受试者每七天首先一次后空瓶5次共10瓶，总计使用10瓶（记录使", "用总共46瓶，与实际使用情况一致。", "8、回访ePRO以及MD。", "既往史：更新合并用药：", "1、鼻腔莫米松鼻喷雾剂C025 4 3-2025 7 25 每鼻 2喷/次 qd 治疗过敏性鼻炎。", "2、苯环喹莫铵鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。", "4、氯卓斯汀盐酸卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。", "5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/", "次 治疗过敏性鼻炎。", "6、枯草抗感染治疗（生理性海水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过", "敏性鼻炎", "已预约受试者安全性随访时间。", "过敏史：", "个人史：", "体格检查：", "专科情况：", "辅助检查：", "治疗项目：", "门诊诊断：", "支气管哮喘", "单病种：", "发病时间：", "处", "置：", "1心电图（心电图室做）", "2布地奈德福莫特罗吸入粉雾剂(II)(省采)●①② 2盒2 000.00入用药,一天2次", "30天", "备注：", "病情评估：", "病情分级：", "是否抢救病例：否", "是否抢救成功：", "是否为绿色通道患者：否", "病人去向：", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:05:58,543 INFO     29 [qwen-vl-parser] page=2 text: 42 lines (bbox 20-61)
2026-08-05 05:05:58,543 INFO     29 [qwen-vl-parser] page=2 text: 42 sections
2026-08-05 05:05:58,688 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1138149, prompt_len=644
2026-08-05 05:06:00,040 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:06:00,041 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-05 05:06:00,055 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1138149, prompt_len=401
2026-08-05 05:06:03,775 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:06:03.772+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 15, "failed": 0, "current": {"4e4700ce908b11f1a3da71efcdd7cc1f": {"id": "4e4700ce908b11f1a3da71efcdd7cc1f", "doc_id": "4e10ceb4908b11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906341337, "task_type": "dataflow", "root_trace_id": "ca345e6640ff4d788f444c3ab712853e", "root_traceparent": "00-ca345e6640ff4d788f444c3ab712853e-8ea193cced1ce3aa-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:06:05,583 INFO     29 [qwen-vl-parser] text API response (len=960):
["就诊卡", "流水号：", "姓名", "龄：40岁", "就诊科", "日：2025-10-24 15:45:39", "主诉：安全性电话随访", "现病史：今日10:27", "固定电话（020-", "（159", "5），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无", "不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对", "V8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试", "者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，", "目前无安全性异常表现。", "合并用药更新：", "1、小柴胡颗粒、（自行购药）2025.10.6-2025.10.8 10g tid 治疗上呼吸道感染", "2、苯环喹溴铵鼻喷雾剂 2025.4.3-至今 每鼻2喷/次 qid 治疗过敏性鼻炎", "3、氮卓斯汀氟替卡松鼻喷雾剂 2025.9.3-至今 每鼻2喷/次 bid 治疗过敏性鼻炎", "4、辛芩颗粒 2024.8.21-2024.8.27 1袋 冲服 tid 治疗过敏性鼻炎", "AE：", "上呼吸道感染 2025年10月5日-2025年10月8日 中度，非SAE，采取药物治疗措施，对试验", "药物采取措施：剂量不变，与试验药物无关，未因该AE退出研究。", "病历更正：", "1、更正2024年10月22日病历，合并用药“辛芩颗粒”为“辛芩颗粒”；", "2、更正2024年10月22日病历，合并用药“苯环喹溴铵鼻喷雾剂”为“苯环喹溴铵鼻喷雾", "剂”；", "3、更正2025年1月24日病历，“无收到ePro触发的哮喘警报邮件”为“有收到ePro触发的哮", "喘警报邮件”；", "4、更正2025年7月18日病历，“受试者漏填2025年4月28日晚间日志” 更正为：“受试者", "漏填2025年4月28日早间日志”；", "5、更正2024年11月6日病历，“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共", "计用了26喷”为：“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了28", "喷”。", "医生"]
2026-08-05 05:06:05,583 INFO     29 [qwen-vl-parser] page=3 text: 35 lines (bbox 62-96)
2026-08-05 05:06:05,583 INFO     29 [qwen-vl-parser] page=3 text: 35 sections
2026-08-05 05:06:05,728 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1126349, prompt_len=644
2026-08-05 05:06:06,988 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:06:06,989 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-05 05:06:07,008 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1126349, prompt_len=401
2026-08-05 05:06:14,629 INFO     29 [qwen-vl-parser] text API response (len=842):
["病历编号：", "姓名：", "性别：", "年龄：40岁", "就诊科：", "就诊时间：2025-11-17 10:10:48", "主诉：支气管哮喘治疗后复查：", "现病史：2021年2月前开始出现咳嗽、咯痰，粘白，量中，能咯出，咳嗽呈阵发性、刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏。无咽痛，无伴反酸、嗳气、腹胀。无上腹部隐痛不适感，无伴发热、畏寒，影响睡眠。晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：", "12.52*109/L 嗜酸粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定。本次门诊距上次门诊间隔时间30天。症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确。急性发作情况：两次，就诊期间急性发作：无，发作次数：0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。近3天来出现咽痛不适", "既往史：鼻炎病史无规则治疗。打鼾明显。", "过敏史：未发现。", "个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。", "体格检查：神志清，颈软，双肺呼吸音粗，未闻及明显干、湿性罗音，口腔粘膜无白斑。", "专科情况：", "辅助检查：", "治疗项目：", "门诊诊断：", "1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、阻塞性睡眠呼吸暂停低通气综合征,4、急性咽炎", "单病种：", "发病时间：", "处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不适随诊。", "1金银花口服液◆⑤ 2盒 20.0ml,口服,一天3次(口服) 6天", "2氨卓斯汀氟替卡松鼻喷雾剂◆ 1瓶 2.0喷,喷鼻,一天2次 30天", "3苯环喹溴铵鼻喷雾剂◆ 3瓶 2.0喷,喷鼻,一天4次 30天", "备注：建议在住地附近社区医疗机构随诊。"]
2026-08-05 05:06:14,630 INFO     29 [qwen-vl-parser] page=4 text: 25 lines (bbox 97-121)
2026-08-05 05:06:14,630 INFO     29 [qwen-vl-parser] page=4 text: 25 sections
2026-08-05 05:06:14,740 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=674431, prompt_len=644
2026-08-05 05:06:16,027 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:06:16,027 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-05 05:06:16,034 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=674431, prompt_len=401
2026-08-05 05:06:17,712 INFO     29 [qwen-vl-parser] text API response (len=277):
["门(急)诊处方", "就诊时间:2025-07-18", "就诊科室:内科门诊", "主诊医", "姓名", "性别:男", "年龄:40岁", "卡号:", "患者", "医疗证号:", "处方号", "地址:PT027气雾剂 2024017-呼吸科", "身份证", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂0.125/0.006*60吸6盒", "183.41100.46", "Sig", "2吸/次,吸入,bid*90天"]
2026-08-05 05:06:17,712 INFO     29 [qwen-vl-parser] page=5 text: 26 lines (bbox 122-147)
2026-08-05 05:06:17,712 INFO     29 [qwen-vl-parser] page=5 text: 26 sections
2026-08-05 05:06:17,814 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=687923, prompt_len=644
2026-08-05 05:06:19,171 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-04-25"}
```
2026-08-05 05:06:19,172 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=2025-04-25
2026-08-05 05:06:19,185 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=687923, prompt_len=401
2026-08-05 05:06:20,851 INFO     29 [qwen-vl-parser] text API response (len=284):
["门(急)诊处方", "就诊时间:2025-04-25", "就诊科室:内科门诊", "主诊", "姓名", "性别:男", "年龄:40岁", "卡号:", "患者类型:GLP支付", "医疗证号:", "处方号", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂(II)0.5mg*60吸6盒", "183.41100.46", "Sig", "2吸/次,吸入,bid*90天"]
2026-08-05 05:06:20,852 INFO     29 [qwen-vl-parser] page=6 text: 26 lines (bbox 148-173)
2026-08-05 05:06:20,852 INFO     29 [qwen-vl-parser] page=6 text: 26 sections
2026-08-05 05:06:20,957 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=642003, prompt_len=644
2026-08-05 05:06:22,128 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:06:22,129 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-05 05:06:22,143 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=642003, prompt_len=401
2026-08-05 05:06:23,734 INFO     29 [qwen-vl-parser] text API response (len=272):
["门(急)诊处方", "就诊时间：2025-02-26", "就诊科室：内科门诊", "主诊", "性别：男", "年龄：40岁", "卡号", "医疗证号：", "处方", "015", "地址：PT027气雾剂 2024017-呼吸科", "身份证号：", "诊断：支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂BDI/●@1g*60吸2盒", "183.41", "366.82", "Sig", "2吸/次,吸入,bid*30天"]
2026-08-05 05:06:23,734 INFO     29 [qwen-vl-parser] page=7 text: 26 lines (bbox 174-199)
2026-08-05 05:06:23,734 INFO     29 [qwen-vl-parser] page=7 text: 26 sections
2026-08-05 05:06:23,836 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=635678, prompt_len=644
2026-08-05 05:06:25,076 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-01-24"}
```
2026-08-05 05:06:25,077 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=2025-01-24
2026-08-05 05:06:25,083 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=635678, prompt_len=401
2026-08-05 05:06:26,770 INFO     29 [qwen-vl-parser] text API response (len=288):
["门(急)诊处方", "就诊时间:2025-01-24", "就诊科室:内科门诊", "主诊医", "姓名", "性别:男", "年龄:40岁", "卡号:4", "患者类型:GCP支付", "医疗证号:", "处方号:", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂HIV●(50ug*60吸4盒", "183.41 733.64", "Sig", "2吸/次,吸入,bid*60天"]
2026-08-05 05:06:26,770 INFO     29 [qwen-vl-parser] page=8 text: 26 lines (bbox 200-225)
2026-08-05 05:06:26,770 INFO     29 [qwen-vl-parser] page=8 text: 26 sections
2026-08-05 05:06:26,855 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=545840, prompt_len=644
2026-08-05 05:06:28,125 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:06:28,125 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-05 05:06:28,132 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=545840, prompt_len=401
2026-08-05 05:06:30,045 INFO     29 [qwen-vl-parser] text API response (len=356):
["门(急)诊处方", "就诊时间:2025-01-03", "就诊科室:内科门诊", "主诊", "性别:男", "年龄:40岁", "卡号", "患者类型:GCP支付", "医疗证号:", "处方", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●⑥ug*60吸2盒", "183.41 366.82", "Sig", "2吸/次,吸入,bid*30天", "医师:", "医生编号:1326", "配剂人:", "核对人:", "合计:", "收费员:", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:06:30,046 INFO     29 [qwen-vl-parser] page=9 text: 33 lines (bbox 226-258)
2026-08-05 05:06:30,047 INFO     29 [qwen-vl-parser] page=9 text: 33 sections
2026-08-05 05:06:30,158 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=642925, prompt_len=644
2026-08-05 05:06:31,528 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-12-04"}
```
2026-08-05 05:06:31,528 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=2024-12-04
2026-08-05 05:06:31,536 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=642925, prompt_len=401
2026-08-05 05:06:33,200 INFO     29 [qwen-vl-parser] text API response (len=277):
["门(急)诊处方", "就诊时间:2024-12-04", "就诊科室:内科门诊", "主诊", "姓名", "性别:男", "年龄:39岁", "卡号", "患者", "医疗证号:", "处方", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●(50ug*60吸2盒", "183.41 366.82", "Sig", "2吸/次,吸入,bid*30天"]
2026-08-05 05:06:33,200 INFO     29 [qwen-vl-parser] page=10 text: 26 lines (bbox 259-284)
2026-08-05 05:06:33,200 INFO     29 [qwen-vl-parser] page=10 text: 26 sections
2026-08-05 05:06:33,354 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1233186, prompt_len=644
2026-08-05 05:06:34,695 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2022-06-08"
}
```
2026-08-05 05:06:34,696 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=2022-06-08
2026-08-05 05:06:34,709 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1233186, prompt_len=401
2026-08-05 05:06:36,502 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:06:36.502+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 15, "failed": 0, "current": {"4e4700ce908b11f1a3da71efcdd7cc1f": {"id": "4e4700ce908b11f1a3da71efcdd7cc1f", "doc_id": "4e10ceb4908b11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906341337, "task_type": "dataflow", "root_trace_id": "ca345e6640ff4d788f444c3ab712853e", "root_traceparent": "00-ca345e6640ff4d788f444c3ab712853e-8ea193cced1ce3aa-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:06:46,816 INFO     29 [qwen-vl-parser] text API response (len=1965):
["激发试验检查报告", "姓名：", "测试号：", "门诊/住院号：", "000", "年龄：", "出生日期：", "19", "性别：", "男", "身高：", "170", "病区：", "内科门诊", "体重：", "81 kg", "机器编号：", "床号：", "电话：", "Pred", "A1", "A1/Pd", "NS", "P1 chg%1", "P2 chg%2", "P3 chg%3", "FVC", "[L]", "4.84", "4.69", "97.1", "4.29", "4.22", "-10.1", "3.64", "-22.5", "4.01", "-14.6", "PEV 1", "[L]", "4.01", "3.05", "76.2", "2.72", "2.69", "-11.8", "2.24", "-26.5", "2.44", "-20.0", "PEV 1 % PVC", "[%]", "83.32", "65.02", "78.0", "63.54", "63.83", "-1.82", "61.73", "-5.06", "60.92", "-6.30", "PEV 1 % VC MAX", "[%]", "80.55", "64.94", "80.6", "62.34", "63.83", "-1.70", "61.73", "-4.94", "60.92", "-6.18", "VC MAX", "[L]", "5.05", "4.70", "93.1", "4.37", "4.22", "-10.2", "3.64", "-22.6", "4.01", "-14.7", "PEP", "[L/s]", "9.37", "9.95", "106.2", "9.06", "7.81", "-21.5", "6.73", "-32.3", "8.22", "-17.4", "MMEF 75/25", "[L/s]", "4.52", "1.54", "34.1", "1.33", "1.34", "-12.9", "1.14", "-25.8", "1.23", "-20.0", "MEF 50", "[L/s]", "5.17", "1.97", "38.1", "1.66", "1.71", "-13.4", "1.34", "-31.8", "1.42", "-28.0", "MEF 25", "[L/s]", "2.29", "0.58", "25.5", "0.52", "0.53", "-9.87", "0.50", "-14.6", "0.49", "-15.7", "PET", "[s]", "6.72", "6.87", "6.93", "3.16", "6.75", "0.57", "6.74", "0.38", "V backextrapolation ex [L]", "0.13", "0.09", "0.10", "-20.0", "0.08", "-41.6", "0.08", "-38.5", "PIF", "[L/s]", "8.04", "7.96", "7.58", "-5.76", "6.16", "-23.3", "7.78", "-3.20", "FIF 50", "[L/s]", "7.99", "7.86", "7.16", "-10.3", "5.36", "-32.9", "7.08", "-11.3", "MVV", "[L/min]", "141.88", "BF MVV", "[1/min]", "Cumulated dose", "0.072", "0.078", "0.312", "2 Puf", "F/V ex", "F/V in", "Vol [L]", "Vol%VCmax", "VCmax", "Time [s]", "PD[-20] FEV 1: 0.2117 mg Cumulated", "PD[-20] PEF: < 0.078 mg Cumulated", "PD[] FEV1%I: could not be calculated!", "意见：", "2022/6/08 10:23:56上午", "1.轻度阻塞性通气功能障碍。", "2.支气管激发试验阳性(累计吸入乙酰甲胆碱0.312mg，FEV1下降大于20%，PD20=0.2117mg，气道高反应性(AHR)为中度", "通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后FEV1恢复至预计值80%。", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:06:46,818 INFO     29 [qwen-vl-parser] page=11 text: 199 lines (bbox 285-483)
2026-08-05 05:06:46,818 INFO     29 [qwen-vl-parser] page=11 text: 199 sections
2026-08-05 05:06:46,977 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1298077, prompt_len=644
2026-08-05 05:06:51,013 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2021-01-21"
}
```
2026-08-05 05:06:51,013 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=2021-01-21
2026-08-05 05:06:51,034 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1298077, prompt_len=401
2026-08-05 05:07:00,300 INFO     29 [qwen-vl-parser] text API response (len=1940):
["检查日期：2021/1/21", "检查时间：16.43", "编号：16", "广州医科大学附属第三医院", "支气管扩张试验检查报告", "姓名：", "测试号：", "年龄：36岁", "性别：男", "病区：", "机器编号：", "门诊/住院号：", "出生日期：", "身高：", "体重：", "床号：", "电话：", "Pred", "A1", "A1/Pd", "P1", "A2/Pd", "chg%1", "P2", "A3/Pd", "chg%2", "P3", "A4/Pd", "chg%3", "FVC", "[L]", "4.86", "3.48", "71.5%", "4.01", "82.4%", "15.19", "4.15", "85.4%", "19.47", "4.01", "82.6%", "15.47", "FEV 1", "[L]", "4.03", "1.97", "48.8%", "2.33", "57.9%", "18.59", "2.33", "57.8%", "18.48", "2.44", "60.5%", "24.02", "FEV 1 % FVC", "[%]", "83.32", "56.62", "68.0%", "58.29", "70.0%", "2.95", "56.15", "67.4%", "-0.83", "60.81", "73.0%", "7.40", "FEV 1 % VC MAX", "[%]", "80.73", "56.07", "69.5%", "58.29", "72.2%", "3.96", "56.15", "69.5%", "0.14", "60.81", "75.3%", "8.45", "VC MAX", "[L]", "5.08", "3.51", "69.1%", "4.01", "78.9%", "14.07", "4.15", "81.8%", "18.31", "4.01", "79.1%", "14.35", "PEF", "[L/s]", "9.41", "6.61", "70.3%", "7.99", "85.0%", "20.93", "7.91", "84.1%", "19.63", "8.07", "85.7%", "22.02", "MMEF 75/25", "[L/s]", "4.57", "0.81", "17.7%", "0.96", "21.1%", "19.59", "1.03", "22.6%", "28.17", "1.12", "24.6%", "39.07", "MEF 50", "[L/s]", "5.20", "1.00", "19.2%", "1.29", "24.8%", "29.25", "1.30", "24.9%", "29.87", "1.53", "29.3%", "52.75", "MEF 25", "[L/s]", "2.32", "0.39", "16.7%", "0.38", "16.4%", "-1.68", "0.50", "21.6%", "29.78", "0.41", "17.9%", "7.18", "FET", "[s]", "15.24", "6.42", "-57.87", "6.30", "-58.63", "6.55", "-57.05", "V backextrapolati", "[L/s]", "0.07", "0.07", "0.89", "0.09", "17.79", "0.08", "6.12", "PIF", "[L/s]", "7.03", "7.39", "5.19", "7.17", "1.99", "7.16", "1.91", "FIV1", "[L]", "3.40", "3.76", "10.58", "3.68", "8.26", "3.60", "5.96", "PEF50 % PIF50", "[%]", "16.56", "21.70", "31.06", "19.81", "19.65", "24.71", "49.20", "MVV", "[L/min]", "142.69", "BF MVV", "[1/min]", "意见：", "1.重度混合性肺通气功能障碍。", "2.支气管舒张试验阳性。", "（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后PEV1较基线增加大于12%，且绝对值增加大于200ml）", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:07:00,300 INFO     29 [qwen-vl-parser] page=12 text: 211 lines (bbox 484-694)
2026-08-05 05:07:00,300 INFO     29 [qwen-vl-parser] page=12 text: 211 sections
2026-08-05 05:07:00,426 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=712860, prompt_len=644
2026-08-05 05:07:01,761 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:07:01,762 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=None
2026-08-05 05:07:01,777 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=712860, prompt_len=401
2026-08-05 05:07:03,801 INFO     29 [qwen-vl-parser] text API response (len=350):
["广州医科大学附属第三医院", "处方笺", "普通", "诊疗卡", "患者姓名", "年龄：41岁", "费别：南医保", "科室：内科门诊（荔湾）", "日期：2026-01-05 17:17:14", "处方号", "地址：荔湾", "2024017-呼吸科", "联系电话", "身份号码：", "2739", "诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],急性气管支气管炎", "R", "P:", "布地奈德福莫特罗吸入粉雾剂(II) 160ug/4.5ug*60吸", "2盒", "剂量：每次2吸", "（", "1", "30", "盒）", "用法：吸入用药", "bid", "01-05", "处方金额：366.82元", "取药药房：门诊西药房（荔湾）"]
2026-08-05 05:07:03,802 INFO     29 [qwen-vl-parser] page=13 text: 30 lines (bbox 695-724)
2026-08-05 05:07:03,802 INFO     29 [qwen-vl-parser] page=13 text: 30 sections
2026-08-05 05:07:03,935 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=972380, prompt_len=644
2026-08-05 05:07:05,296 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-01-05"}
```
2026-08-05 05:07:05,296 INFO     29 [qwen-vl-parser] page=14 classify=text report_date=2026-01-05
2026-08-05 05:07:05,302 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=972380, prompt_len=401
2026-08-05 05:07:09,325 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:07:09.322+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 15, "failed": 0, "current": {"4e4700ce908b11f1a3da71efcdd7cc1f": {"id": "4e4700ce908b11f1a3da71efcdd7cc1f", "doc_id": "4e10ceb4908b11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906341337, "task_type": "dataflow", "root_trace_id": "ca345e6640ff4d788f444c3ab712853e", "root_traceparent": "00-ca345e6640ff4d788f444c3ab712853e-8ea193cced1ce3aa-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:07:11,844 INFO     29 [qwen-vl-parser] text API response (len=1267):
["广州医科大学附属第三医院", "The Third Affiliated Hospital of Guangzhou Medical University", "门(急)诊病历信息", "就诊卡", "流水", "姓", "病历编号:", "年 龄:41岁", "就诊科室:内科门诊(荔湾) 医", "就诊时间:2026-01-05 17:07:54", "主 诉:支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天", "现 病 史:2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激", "性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流", "涕、嗅觉,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响", "睡眠,晨起有咽干,曾到本院就诊两次,症状不见明显缓解。2021-1-9血常规:白细胞:", "12.52*109/L 嗜酸粒细胞:0.65*109/L 5.2%,经治疗后症状明显缓解。无咳嗽、咯痰、气", "促。病情稳定,本次门诊距上次门诊间隔时间30天。症状控制情况:过去4周,患者:吸入", "药物使用情况:遵医嘱使用;吸入装置使用情况:正确。急性发作情况:两次,就诊期间急", "性发作:无,发作次数:0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。长期规律使用信必", "可160/4.5ug 2吸 bid治疗,5天前开始出现咳嗽、咯痰,黄白痰,量少,难以咯出,咳嗽以", "夜间为主。无气促,伴咽息,鼻塞、流涕、喷嚏,无发热。", "既 往 史:鼻炎病史无规则治疗。打鼾明显。", "过 敏 史:未发现;", "个 人 史:否认遗传病史,吸烟10年,20支/日,2018年戒烟。偶饮酒。2021-12-20已打第", "三针新冠疫苗。", "体格检查:神志清,颈软,双肺呼吸音粗,可闻及散在哮鸣音,口腔粘膜无白斑。", "专科情况:", "辅助检查:", "治疗项目:", "门诊诊断:", "1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎", "处 置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。", "布地奈德福莫特罗吸入粉雾剂(II)2盒 2.0吸,吸入用药,一天2次 30天", "(省采)●①⑤", "左氧氟沙星片(省采)●⑥ 5片 0.5g,口服,每日1次(口服) 5天", "第1页", "广州医科大学附属第三医院", "The Third Affiliated Hospital of Guangzhou Medical University", "门(急)诊病历信息", "复方甲氧那明胶囊(省采)●② 1瓶 1.0粒,餐后口服,一天3次(口服) 5天", "盐酸氨溴索分散片(省采)●⑥ 15片 30.0mg,餐后口服,一天3次(口服) 5", "天", "醋酸泼尼松片●②④ 6片 10.0mg,口服,每早1次(口服) 3天", "备 注:建议在住地附近社区医疗机构随诊。"]
2026-08-05 05:07:11,845 INFO     29 [qwen-vl-parser] page=14 text: 44 lines (bbox 725-768)
2026-08-05 05:07:11,846 INFO     29 [qwen-vl-parser] page=14 text: 44 sections
2026-08-05 05:07:12,073 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1211412, prompt_len=644
2026-08-05 05:07:16,344 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-02-04"}
```
2026-08-05 05:07:16,345 INFO     29 [qwen-vl-parser] page=15 classify=text report_date=2026-02-04
2026-08-05 05:07:16,360 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1211412, prompt_len=401
2026-08-05 05:07:20,955 INFO     29 [qwen-vl-parser] text API response (len=800):
["门诊/住院病历信息", "就诊卡号：", "病历编号：", "姓名：", "性别：男", "年龄：41岁", "就诊科室：内科门诊（荔湾）", "就诊时间：2026-02-04 11:21:11", "主诉：支气管哮喘治疗后复查", "现病史：2021年2月前开始出现咳嗽、咳痰，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sg 2吸 bid治疗。", "既往史：鼻炎病史无规则治疗，打鼾明显。", "过敏史：未发现；", "个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。", "体格检查：神志清，颈软，双肺呼吸音粗，可闻及散在哮鸣音，口腔粘膜无白斑。", "专科情况：", "辅助检查：", "治疗项目：", "门诊诊断：", "1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、急性气管支气管炎", "单病种：", "发病时间：", "处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不遥随诊。", "布地奈德福莫特罗吸入粉雾剂(II)(省", "2 2.0班，吸入用药，一天2次", "30", "采)●①②", "查天"]
2026-08-05 05:07:20,955 INFO     29 [qwen-vl-parser] page=15 text: 27 lines (bbox 769-795)
2026-08-05 05:07:20,955 INFO     29 [qwen-vl-parser] page=15 text: 27 sections
2026-08-05 05:07:21,119 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1642425, prompt_len=644
2026-08-05 05:07:22,616 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2024-10-22"
}
```
2026-08-05 05:07:22,617 INFO     29 [qwen-vl-parser] page=16 classify=text report_date=2024-10-22
2026-08-05 05:07:22,630 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1642425, prompt_len=401
2026-08-05 05:07:42,142 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:07:42.141+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 15, "failed": 0, "current": {"4e4700ce908b11f1a3da71efcdd7cc1f": {"id": "4e4700ce908b11f1a3da71efcdd7cc1f", "doc_id": "4e10ceb4908b11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906341337, "task_type": "dataflow", "root_trace_id": "ca345e6640ff4d788f444c3ab712853e", "root_traceparent": "00-ca345e6640ff4d788f444c3ab712853e-8ea193cced1ce3aa-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:08:14,873 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:08:14.873+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 15, "failed": 0, "current": {"4e4700ce908b11f1a3da71efcdd7cc1f": {"id": "4e4700ce908b11f1a3da71efcdd7cc1f", "doc_id": "4e10ceb4908b11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906341337, "task_type": "dataflow", "root_trace_id": "ca345e6640ff4d788f444c3ab712853e", "root_traceparent": "00-ca345e6640ff4d788f444c3ab712853e-8ea193cced1ce3aa-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:08:47,634 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:08:47.632+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 15, "failed": 0, "current": {"4e4700ce908b11f1a3da71efcdd7cc1f": {"id": "4e4700ce908b11f1a3da71efcdd7cc1f", "doc_id": "4e10ceb4908b11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906341337, "task_type": "dataflow", "root_trace_id": "ca345e6640ff4d788f444c3ab712853e", "root_traceparent": "00-ca345e6640ff4d788f444c3ab712853e-8ea193cced1ce3aa-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:09:20,503 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:09:20.500+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 15, "failed": 0, "current": {"4e4700ce908b11f1a3da71efcdd7cc1f": {"id": "4e4700ce908b11f1a3da71efcdd7cc1f", "doc_id": "4e10ceb4908b11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906341337, "task_type": "dataflow", "root_trace_id": "ca345e6640ff4d788f444c3ab712853e", "root_traceparent": "00-ca345e6640ff4d788f444c3ab712853e-8ea193cced1ce3aa-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:09:31,741 INFO     29 [qwen-vl-parser] text API response (len=22290):
["广州医科大学附属第三医院", "肺功能检查报告", "地址：广州市多宝路63号 电话：020-81292126", "COSMED", "姓名：", "科室/床号：", "ID：", "出生日期：1984/12/8", "预计值：ERS 93", "日期：2024/10/22", "性别：Male", "地区修正：Chinese", "详细描述：内科门诊", "Company：", "年龄：39", "体重(Kg)：89.0", "身高(cm)：177.5", "BMI(Kg/m²：28.2", "吸烟：曾经(10/20)", "用力肺活量 Forced Vital Capacity", "F(l/s)", "V(l)", "BEST #3 - 2024/10/22 11:03", "沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38", "沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39", "沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41", "沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38", "沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39", "沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41", "MEF75%", "MEF50%", "MEF25%", "FVC", "PEF", "FEV1", "ATS", "12t(s)", "-1", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120", "121", "122", "123", "124", "125", "126", "127", "128", "129", "130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "140", "141", "142", "143", "144", "145", "146", "147", "148", "149", "150", "151", "152", "153", "154", "155", "156", "157", "158", "159", "160", "161", "162", "163", "164", "165", "166", "167", "168", "169", "170", "171", "172", "173", "174", "175", "176", "177", "178", "179", "180", "181", "182", "183", "184", "185", "186", "187", "188", "189", "190", "191", "192", "193", "194", "195", "196", "197", "198", "199", "200", "201", "202", "203", "204", "205", "206", "207", "208", "209", "210", "211", "212", "213", "214", "215", "216", "217", "218", "219", "220", "221", "222", "223", "224", "225", "226", "227", "228", "229", "230", "231", "232", "233", "234", "235", "236", "237", "238", "239", "240", "241", "242", "243", "244", "245", "246", "247", "248", "249", "250", "251", "252", "253", "254", "255", "256", "257", "258", "259", "260", "261", "262", "263", "264", "265", "266", "267", "268", "269", "270", "271", "272", "273", "274", "275", "276", "277", "278", "279", "280", "281", "282", "283", "284", "285", "286", "287", "288", "289", "290", "291", "292", "293", "294", "295", "296", "297", "298", "299", "300", "301", "302", "303", "304", "305", "306", "307", "308", "309", "310", "311", "312", "313", "314", "315", "316", "317", "318", "319", "320", "321", "322", "323", "324", "325", "326", "327", "328", "329", "330", "331", "332", "333", "334", "335", "336", "337", "338", "339", "340", "341", "342", "343", "344", "345", "346", "347", "348", "349", "350", "351", "352", "353", "354", "355", "356", "357", "358", "359", "360", "361", "362", "363", "364", "365", "366", "367", "368", "369", "370", "371", "372", "373", "374", "375", "376", "377", "378", "379", "380", "381", "382", "383", "384", "385", "386", "387", "388", "389", "390", "391", "392", "393", "394", "395", "396", "397", "398", "399", "400", "401", "402", "403", "404", "405", "406", "407", "408", "409", "410", "411", "412", "413", "414", "415", "416", "417", "418", "419", "420", "421", "422", "423", "424", "425", "426", "427", "428", "429", "430", "431", "432", "433", "434", "435", "436", "437", "438", "439", "440", "441", "442", "443", "444", "445", "446", "447", "448", "449", "450", "451", "452", "453", "454", "455", "456", "457", "458", "459", "460", "461", "462", "463", "464", "465", "466", "467", "468", "469", "470", "471", "472", "473", "474", "475", "476", "477", "478", "479", "480", "481", "482", "483", "484", "485", "486", "487", "488", "489", "490", "491", "492", "493", "494", "495", "496", "497", "498", "499", "500", "501", "502", "503", "504", "505", "506", "507", "508", "509", "510", "511", "512", "513", "514", "515", "516", "517", "518", "519", "520", "521", "522", "523", "524", "525", "526", "527", "528", "529", "530", "531", "532", "533", "534", "535", "536", "537", "538", "539", "540", "541", "542", "543", "544", "545", "546", "547", "548", "549", "550", "551", "552", "553", "554", "555", "556", "557", "558", "559", "560", "561", "562", "563", "564", "565", "566", "567", "568", "569", "570", "571", "572", "573", "574", "575", "576", "577", "578", "579", "580", "581", "582", "583", "584", "585", "586", "587", "588", "589", "590", "591", "592", "593", "594", "595", "596", "597", "598", "599", "600", "601", "602", "603", "604", "605", "606", "607", "608", "609", "610", "611", "612", "613", "614", "615", "616", "617", "618", "619", "620", "621", "622", "623", "624", "625", "626", "627", "628", "629", "630", "631", "632", "633", "634", "635", "636", "637", "638", "639", "640", "641", "642", "643", "644", "645", "646", "647", "648", "649", "650", "651", "652", "653", "654", "655", "656", "657", "658", "659", "660", "661", "662", "663", "664", "665", "666", "667", "668", "669", "670", "671", "672", "673", "674", "675", "676", "677", "678", "679", "680", "681", "682", "683", "684", "685", "686", "687", "688", "689", "690", "691", "692", "693", "694", "695", "696", "697", "698", "699", "700", "701", "702", "703", "704", "705", "706", "707", "708", "709", "710", "711", "712", "713", "714", "715", "716", "717", "718", "719", "720", "721", "722", "723", "724", "725", "726", "727", "728", "729", "730", "731", "732", "733", "734", "735", "736", "737", "738", "739", "740", "741", "742", "743", "744", "745", "746", "747", "748", "749", "750", "751", "752", "753", "754", "755", "756", "757", "758", "759", "760", "761", "762", "763", "764", "765", "766", "767", "768", "769", "770", "771", "772", "773", "774", "775", "776", "777", "778", "779", "780", "781", "782", "783", "784", "785", "786", "787", "788", "789", "790", "791", "792", "793", "794", "795", "796", "797", "798", "799", "800", "801", "802", "803", "804", "805", "806", "807", "808", "809", "810", "811", "812", "813", "814", "815", "816", "817", "818", "819", "820", "821", "822", "823", "824", "825", "826", "827", "828", "829", "830", "831", "832", "833", "834", "835", "836", "837", "838", "839", "840", "841", "842", "843", "844", "845", "846", "847", "848", "849", "850", "851", "852", "853", "854", "855", "856", "857", "858", "859", "860", "861", "862", "863", "864", "865", "866", "867", "868", "869", "870", "871", "872", "873", "874", "875", "876", "877", "878", "879", "880", "881", "882", "883", "884", "885", "886", "887", "888", "889", "890", "891", "892", "893", "894", "895", "896", "897", "898", "899", "900", "901", "902", "903", "904", "905", "906", "907", "908", "909", "910", "911", "912", "913", "914", "915", "916", "917", "918", "919", "920", "921", "922", "923", "924", "925", "926", "927", "928", "929", "930", "931", "932", "933", "934", "935", "936", "937", "938", "939", "940", "941", "942", "943", "944", "945", "946", "947", "948", "949", "950", "951", "952", "953", "954", "955", "956", "957", "958", "959", "960", "961", "962", "963", "964", "965", "966", "967", "968", "969", "970", "971", "972", "973", "974", "975", "976", "977", "978", "979", "980", "981", "982", "983", "984", "985", "986", "987", "988", "989", "990", "991", "992", "993", "994", "995", "996", "997", "998", "999", "1000", "1001", "1002", "1003", "1004", "1005", "1006", "1007", "1008", "1009", "1010", "1011", "1012", "1013", "1014", "1015", "1016", "1017", "1018", "1019", "1020", "1021", "1022", "1023", "1024", "1025", "1026", "1027", "1028", "1029", "1030", "1031", "1032", "1033", "1034", "1035", "1036", "1037", "1038", "1039", "1040", "1041", "1042", "1043", "1044", "1045", "1046", "1047", "1048", "1049", "1050", "1051", "1052", "1053", "1054", "1055", "1056", "1057", "1058", "1059", "1060", "1061", "1062", "1063", "1064", "1065", "1066", "1067", "1068", "1069", "1070", "1071", "1072", "1073", "1074", "1075", "1076", "1077", "1078", "1079", "1080", "1081", "1082", "1083", "1084", "1085", "1086", "1087", "1088", "1089", "1090", "1091", "1092", "1093", "1094", "1095", "1096", "1097", "1098", "1099", "1100", "1101", "1102", "1103", "1104", "1105", "1106", "1107", "1108", "1109", "1110", "1111", "1112", "1113", "1114", "1115", "1116", "1117", "1118", "1119", "1120", "1121", "1122", "1123", "1124", "1125", "1126", "1127", "1128", "1129", "1130", "1131", "1132", "1133", "1134", "1135", "1136", "1137", "1138", "1139", "1140", "1141", "1142", "1143", "1144", "1145", "1146", "1147", "1148", "1149", "1150", "1151", "1152", "1153", "1154", "1155", "1156", "1157", "1158", "1159", "1160", "1161", "1162", "1163", "1164", "1165", "1166", "1167", "1168", "1169", "1170", "1171", "1172", "1173", "1174", "1175", "1176", "1177", "1178", "1179", "1180", "1181", "1182", "1183", "1184", "1185", "1186", "1187", "1188", "1189", "1190", "1191", "1192", "1193", "1194", "1195", "1196", "1197", "1198", "1199", "1200", "1201", "1202", "1203", "1204", "1205", "1206", "1207", "1208", "1209", "1210", "1211", "1212", "1213", "1214", "1215", "1216", "1217", "1218", "1219", "1220", "1221", "1222", "1223", "1224", "1225", "1226", "1227", "1228", "1229", "1230", "1231", "1232", "1233", "1234", "1235", "1236", "1237", "1238", "1239", "1240", "1241", "1242", "1243", "1244", "1245", "1246", "1247", "1248", "1249", "1250", "1251", "1252", "1253", "1254", "1255", "1256", "1257", "1258", "1259", "1260", "1261", "1262", "1263", "1264", "1265", "1266", "1267", "1268", "1269", "1270", "1271", "1272", "1273", "1274", "1275", "1276", "1277", "1278", "1279", "1280", "1281", "1282", "1283", "1284", "1285", "1286", "1287", "1288", "1289", "1290", "1291", "1292", "1293", "1294", "1295", "1296", "1297", "1298", "1299", "1300", "1301", "1302", "1303", "1304", "1305", "1306", "1307", "1308", "1309", "1310", "1311", "1312", "1313", "1314", "1315", "1316", "1317", "1318", "1319", "1320", "1321", "1322", "1323", "1324", "1325", "1326", "1327", "1328", "1329", "1330", "1331", "1332", "1333", "1334", "1335", "1336", "1337", "1338", "1339", "1340", "1341", "1342", "1343", "1344", "1345", "1346", "1347", "1348", "1349", "1350", "1351", "1352", "1353", "1354", "1355", "1356", "1357", "1358", "1359", "1360", "1361", "1362", "1363", "1364", "1365", "1366", "1367", "1368", "1369", "1370", "1371", "1372", "1373", "1374", "1375", "1376", "1377", "1378", "1379", "1380", "1381", "1382", "1383", "1384", "1385", "1386", "1387", "1388", "1389", "1390", "1391", "1392", "1393", "1394", "1395", "1396", "1397", "1398", "1399", "1400", "1401", "1402", "1403", "1404", "1405", "1406", "1407", "1408", "1409", "1410", "1411", "1412", "1413", "1414", "1415", "1416", "1417", "1418", "1419", "1420", "1421", "1422", "1423", "1424", "1425", "1426", "1427", "1428", "1429", "1430", "1431", "1432", "1433", "1434", "1435", "1436", "1437", "1438", "1439", "1440", "1441", "1442", "1443", "1444", "1445", "1446", "1447", "1448", "1449", "1450", "1451", "1452", "1453", "1454", "1455", "1456", "1457", "1458", "1459", "1460", "1461", "1462", "1463", "1464", "1465", "1466", "1467", "1468", "1469", "1470", "1471", "1472", "1473", "1474", "1475", "1476", "1477", "1478", "1479", "1480", "1481", "1482", "1483", "1484", "1485", "1486", "1487", "1488", "1489", "1490", "1491", "1492", "1493", "1494", "1495", "1496", "1497", "1498", "1499", "1500", "1501", "1502", "1503", "1504", "1505", "1506", "1507", "1508", "1509", "1510", "1511", "1512", "1513", "1514", "1515", "1516", "1517", "1518", "1519", "1520", "1521", "1522", "1523", "1524", "1525", "1526", "1527", "1528", "1529", "1530", "1531", "1532", "1533", "1534", "1535", "1536", "1537", "1538", "1539", "1540", "1541", "1542", "1543", "1544", "1545", "1546", "1547", "1548", "1549", "1550", "1551", "1552", "1553", "1554", "1555", "1556", "1557", "1558", "1559", "1560", "1561", "1562", "1563", "1564", "1565", "1566", "1567", "1568", "1569", "1570", "1571", "1572", "1573", "1574", "1575", "1576", "1577", "1578", "1579", "1580", "1581", "1582", "1583", "1584", "1585", "1586", "1587", "1588", "1589", "1590", "1591", "1592", "1593", "1594", "1595", "1596", "1597", "1598", "1599", "1600", "1601", "1602", "1603", "1604", "1605", "1606", "1607", "1608", "1609", "1610", "1611", "1612", "1613", "1614", "1615", "1616", "1617", "1618", "1619", "1620", "1621", "1622", "1623", "1624", "1625", "1626", "1627", "1628", "1629", "1630", "1631", "1632", "1633", "1634", "1635", "1636", "1637", "1638", "1639", "1640", "1641", "1642", "1643", "1644", "1645", "1646", "1647", "1648", "1649", "1650", "1651", "1652", "1653", "1654", "1655", "1656", "1657", "1658", "1659", "1660", "1661", "1662", "1663", "1664", "1665", "1666", "1667", "1668", "1669", "1670", "1671", "1672", "1673", "1674", "1675", "1676", "1677", "1678", "1679", "1680", "1681", "1682", "1683", "1684", "1685", "1686", "1687", "1688", "1689", "1690", "1691", "1692", "1693", "1694", "1695", "1696", "1697", "1698", "1699", "1700", "1701", "1702", "1703", "1704", "1705", "1706", "1707", "1708", "1709", "1710", "1711", "1712", "1713", "1714", "1715", "1716", "1717", "1718", "1719", "1720", "1721", "1722", "1723", "1724", "1725", "1726", "1727", "1728", "1729", "1730", "1731", "1732", "1733", "1734", "1735", "1736", "1737", "1738", "1739", "1740", "1741", "1742", "1743", "1744", "1745", "1746", "1747", "1748", "1749", "1750", "1751", "1752", "1753", "1754", "1755", "1756", "1757", "1758", "1759", "1760", "1761", "1762", "1763", "1764", "1765", "1766", "1767", "1768", "1769", "1770", "1771", "1772", "1773", "1774", "1775", "1776", "1777", "1778", "1779", "1780", "1781", "1782", "1783", "1784", "1785", "1786", "1787", "1788", "1789", "1790", "1791", "1792", "1793", "1794", "1795", "1796", "1797", "1798", "1799", "1800", "1801", "1802", "1803", "1804", "1805", "1806", "1807", "1808", "1809", "1810", "1811", "1812", "1813", "1814", "1815", "1816", "1817", "1818", "1819", "1820", "1821", "1822", "1823", "1824", "1825", "1826", "1827", "1828", "1829", "1830", "1831", "1832", "1833", "1834", "1835", "1836", "1837", "1838", "1839", "1840", "1841", "1842", "1843", "1844", "1845", "1846", "1847", "1848", "1849", "1850", "1851", "1852", "1853", "1854", "1855", "1856", "1857", "1858", "1859", "1860", "1861", "1862", "1863", "1864", "1865", "1866", "1867", "1868", "1869", "1870", "1871", "1872", "1873", "1874", "1875", "1876", "1877", "1878", "1879", "1880", "1881", "1882", "1883", "1884", "1885", "1886", "1887", "1888", "1889", "1890", "1891", "1892", "1893", "1894", "1895", "1896", "1897", "1898", "1899", "1900", "1901", "1902", "1903", "1904", "1905", "1906", "1907", "1908", "1909", "1910", "1911", "1912", "1913", "1914", "1915", "1916", "1917", "1918", "1919", "1920", "1921", "1922", "1923", "1924", "1925", "1926", "1927", "1928", "1929", "1930", "1931", "1932", "1933", "1934", "1935", "1936", "1937", "1938", "1939", "1940", "1941", "1942", "1943", "1944", "1945", "1946", "1947", "1948", "1949", "1950", "1951", "1952", "1953", "1954", "1955", "1956", "1957", "1958", "1959", "1960", "1961", "1962", "1963", "1964", "1965", "1966", "1967", "1968", "1969", "1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034", "2035", "2036", "2037", "2038", "2039", "2040", "2041", "2042", "2043", "2044", "2045", "2046", "2047", "2048", "2049", "2050", "2051", "2052", "2053", "2054", "2055", "2056", "2057", "2058", "2059", "2060", "2061", "2062", "2063", "2064", "2065", "2066", "2067", "2068", "2069", "2070", "2071", "2072", "2073", "2074", "2075", "2076", "2077", "2078", "2079", "2080", "2081", "2082", "2083", "2084", "2085", "2086", "2087", "2088", "2089", "2090", "2091", "2092", "2093", "2094", "2095", "2096", "2097", "2098", "2099", "2100", "2101", "2102", "2103", "2104", "2105", "2106", "2107", "2108", "2109", "2110", "2111", "2112", "2113", "2114", "2115", "2116", "2117", "2118", "2119", "2120", "2121", "2122", "2123", "2124", "2125", "2126", "2127", "2128", "2129", "2130", "2131", "2132", "2133", "2134", "2135", "2136", "2137", "2138", "2139", "2140", "2141", "2142", "2143", "2144", "2145", "2146", "2147", "2148", "2149", "2150", "2151", "2152", "2153", "2154", "2155", "2156", "2157", "2158", "2159", "2160", "2161", "2162", "2163", "2164", "2165", "2166", "2167", "2168", "2169", "2170", "2171", "2172", "2173", "2174", "2175", "2176", "2177", "2178", "2179", "2180", "2181", "2182", "2183", "2184", "2185", "2186", "2187", "2188", "2189", "2190", "2191", "2192", "2193", "2194", "2195", "2196", "2197", "2198", "2199", "2200", "2201", "2202", "2203", "2204", "2205", "2206", "2207", "2208", "2209", "2210", "2211", "2212", "2213", "2214", "2215", "2216", "2217", "2218", "2219", "2220", "2221", "2222", "2223", "2224", "2225", "2226", "2227", "2228", "2229", "2230", "2231", "2232", "2233", "2234", "2235", "2236", "2237", "2238", "2239", "2240", "2241", "2242", "2243", "2244", "2245", "2246", "2247", "2248", "2249", "2250", "2251", "2252", "2253", "2254", "2255", "2256", "2257", "2258", "2259", "2260", "2261", "2262", "2263", "2264", "2265", "2266", "2267", "2268", "2269", "2270", "2271", "2272", "2273", "2274", "2275", "2276", "2277", "2278", "2279", "2280", "2281", "2282", "2283", "2284", "2285", "2286", "2287", "2288", "2289", "2290", "2291", "2292", "2293", "2294", "2295", "2296", "2297", "2298", "2299", "2300", "2301", "2302", "2303", "2304", "2305", "2306", "2307", "2308", "2309", "2310", "2311", "2312", "2313", "2314", "2315", "2316", "2317", "2318", "2319", "2320", "2321", "2322", "2323", "2324", "2325", "2326", "2327", "2328", "2329", "2330", "2331", "2332", "2333", "2334", "2335", "2336", "2337", "2338", "2339", "2340", "2341", "2342", "2343", "2344", "2345", "2346", "2347", "2348", "2349", "2350", "2351", "2352", "2353", "2354", "2355", "2356", "2357", "2358", "2359", "2360", "2361", "2362", "2363", "2364", "2365", "2366", "2367", "2368", "2369", "2370", "2371", "2372", "2373", "2374", "2375", "2376", "2377", "2378", "2379", "2380", "2381", "2382", "2383", "2384", "2385", "2386", "2387", "2388", "2389", "2390", "2391", "2392", "2393", "2394", "2395", "2396", "2397", "2398", "2399", "2400", "2401", "2402", "2403", "2404", "2405", "2406", "2407", "2408", "2409", "2410", "2411", "2412", "2413", "2414", "2415", "2416", "2417", "2418", "2419", "2420", "2421", "2422", "2423", "2424", "2425", "2426", "2427", "2428", "2429", "2430", "2431", "2432", "2433", "2434", "2435", "2436", "2437", "2438", "2439", "2440", "2441", "2442", "2443", "2444", "2445", "2446", "2447", "2448", "2449", "2450", "2451", "2452", "2453", "2454", "2455", "2456", "2457", "2458", "2459", "2460", "2461", "2462", "2463", "2464", "2465", "2466", "2467", "2468", "2469", "2470", "2471", "2472", "2473", "2474", "2475", "2476", "2477", "2478", "2479", "2480", "2481", "2482", "2483", "2484", "2485", "2486", "2487", "2488", "2489", "2490", "2491", "2492", "2493", "2494", "2495", "2496", "2497", "2498", "2499", "2500", "2501", "2502", "2503", "2504", "2505", "2506", "2507", "2508", "2509", "2510", "2511", "2512", "2513", "2514", "2515", "2516", "2517", "2518", "2519", "2520", "2521", "2522", "2523", "2524", "2525", "2526", "2527", "2528", "2529", "2530", "2531", "2532", "2533", "2534", "2535", "2536", "2537", "2538", "2539", "2540", "2541", "2542", "2543", "2544", "2545", "2546", "2547", "2548", "2549", "2550", "2551", "2552", "2553", "2554", "2555", "2556", "2557", "2558", "2559", "2560", "2561", "2562", "2563", "2564", "2565", "2566", "2567", "2568", "2569", "2570", "2571", "2572", "2573", "2574", "2575", "2576", "2577", "2578", "2579", "2580", "2581", "2582", "2583", "2584", "2585", "2586", "2587", "2588", "2589", "2590", "2591", "2592", "2593", "2594", "2595", "2596", "2597", "2598", "2599", "2600", "2601", "2602", "2603", "2604", "2605", "2606", "2607", "2608", "2609", "2610", "2611", "2612", "2613", "2614", "2615", "2616", "2617", "2618", "2619", "2620", "2621", "2622", "2623", "2624", "2625", "2626", "2627", "2628", "2629", "2630", "2631", "2632", "2633", "2634", "2635", "2636", "2637", "2638", "2639", "2640", "2641", "2642", "2643", "2644", "2645", "2646", "2647", "2648", "2649", "2650", "2651", "2652", "2653", "2654", "2655", "2656", "2657", "2658", "2659", "2660", "2661", "2662", "2663", "2664", "2665", "2666", "2667", "2668", "2669", "2670", "2671", "2672", "2673", "2674", "2675", "2676", "2677", "2678", "2679", "2680", "2681", "2682", "2683", "2684", "2685", "2686", "2687", "2688", "2689", "2690", "2691", "2692", "2693", "2694", "2695", "2696", "2697", "2698", "2699", "2700", "2701", "2702", "2703", "2704", "2705", "2706", "2707", "2708", "2709", "2710", "2711", "2712", "2713", "2714", "2715", "2716", "2717", "2718", "2719", "2720", "2721", "2722", "2723", "2724", "2725", "2726", "2727", "2728", "2729", "2730", "2731", "2732", "2733", "2734", "2735", "2736", "2737", "2738", "2739", "2740", "2741", "2742", "2743", "2744", "2745", "2746", "2747", "2748", "2749", "2750", "2751", "2752", "2753", "2754", "2755", "2756", "2757", "2758", "2759", "2760", "2761", "2762", "2763", "2764", "2765", "2766", "2767", "2768", "2769", "2770", "2771", "2772", "2773", "2774", "2775", "2776", "2777", "2778", "2779", "2780", "2781", "2782", "2783", "2784", "2785", "2786", "2787", "2788", "2789", "2790", "2791", "2792", "2793", "2794", "2795", "2796", "2797", "2798", "2799", "2800", "2801", "2802", "2803", "2804", "2805", "2806", "2807", "2808", "2809", "2810", "2811", "2812", "2813", "2814", "2815", "2816", "2817", "2818", "2819", "2820", "
2026-08-05 05:09:31,753 INFO     29 [qwen-vl-parser] page=16 text: 2885 lines (bbox 796-3680)
2026-08-05 05:09:31,754 INFO     29 [qwen-vl-parser] page=16 text: 2885 sections
2026-08-05 05:09:31,754 INFO     29 [qwen-vl-parser] parse_pdf done: 3681 sections from 16 pages.
2026-08-05 05:09:31,767 INFO     29 Close text detector.
2026-08-05 05:09:32,115 INFO     29 Close text recognizer.
2026-08-05 05:09:32,440 INFO     29 Close recognizer.
2026-08-05 05:09:32,775 INFO     29 Close recognizer.
2026-08-05 05:09:33,432 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-05 05:09:33,433 INFO     29 [Trace] task=4e4700ce | doc=LZK 哮喘 广三(1).pdf | Parser:MedLink | outputs={"html": "", "json": "3681 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "json"}
2026-08-05 05:09:33,433 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-05 05:09:33,456 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:09:33,456 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。只有主诉，病史的也属于OutpatientRecord（门诊病历）\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 病历编号：\n[BBOX-1] 性别：男\n[BBOX-2] 年龄：40岁\n[BBOX-3] 就诊科室：内科门诊（荔湾）\n[BBOX-4] 就诊时间：2025-10-10 14:36:06\n[BBOX-5] 主诉：BAIYUN V8\n[BBOX-6] 现病史：自上次访视至今，询问及查询HIS系统受试者有新增AE，无SAE、哮喘急性发作，有新增合并用药，发生2次医疗相关事件[2025年9月3日因过敏性鼻炎就诊专科门诊、本周曾因上呼吸道感染到社区医院就诊(具体不详，因HIS系统滞后无法收集具体情况及受试者无法回忆起当时情况及用药情况，待收集具体情况后补充详情)]。于2025年8月4日、2025年9月1日收到加重警报邮件，联系受试者后，均判断非哮喘急性发作。\n[BBOX-7] 完成下流操作：\n[BBOX-8] 1、查看受试者电子日志，受试者漏填2025年8月16日，2025年9月4日晚间日志，2025年9月4日、2025年9月25日早间日志；\n[BBOX-9] 2、填写AQLQ+12和ACQ-5问卷，ACQ-5评分：0.8分；\n[BBOX-10] 3、休息10分钟后，测量坐位生命体征：血压113/81mmHg，脉搏87次/分，呼吸频率20次/分，体温36.6℃，测量身高177.5cm，体重90.5kg(BMI=28.7kg/m2)；\n[BBOX-11] 4、14:35体格检查：神志清，体查合作，自主体位，一般外表无异常，皮肤、粘膜无异常，唇甲无发绀，眼睛、耳、鼻、咽喉无异常，口咽部粘膜无异常，颈软，气管居中，甲状腺未及肿大，全身浅表淋巴结未及肿大，颈静脉无怒张，胸廓无畸形，双肺呼吸运动对称，双肺触觉语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及啰音。心前区无隆起，心尖搏动无弥散，心界不大，心率：87次/分，律齐，各瓣膜听诊区未闻及病理性杂音。腹平软，全腹无压痛、反跳痛。肝、脾肋下未及，肝肾区无叩击痛，肠鸣音存，4次/分，脊柱、四肢无畸形，生理征存，未引出病理征，其他系统未见明显异常；\n[BBOX-12] 5、休息至少10分钟后，于14:58行12导联ECG检查；\n[BBOX-13] 6、于15:01采集中心实验室样本(血常规，血生化)并送往中心试验室；\n[BBOX-14] 7、回收试验药物BDAMDI@ASMDI3盒(152968-AH及185936-HK未开封，148729-UA未用60揿，实际使用46揿，发药当天预喷4揿，2025年9月10日前因超过7天未使用试验药物空喷2次共4揿，2025年9月10日后受试者每七天清洗一次后空喷5次共10揿，总计预喷18揿；epro记录使用总共46揿，与实际使用情况一致。\n[BBOX-15] 8、回收epro以及AM3。\n[BBOX-16] 既往史：更新合并用药：\n[BBOX-17] 1、糠酸莫米松鼻喷雾剂2025.4.3-2025.7.25 每鼻 2喷/次 qm 治疗过敏性鼻炎。\n[BBOX-18] CS 扫描全能王\n[BBOX-19] 3亿人都在用的扫描App\n[BBOX-20] 病历文书\n[BBOX-21] 门诊病历\n[BBOX-22] 25/10/10 14时 门诊病历\n[BBOX-23] 25/10/24 15时 门诊病历（GCP专用）\n[BBOX-24] 25/11/17 10时 门诊病历\n[BBOX-25] 头降使用40瓶，平均每天使用4瓶，2025年9月10日用完4瓶（未使用试验药剂空瓶2次共4\n[BBOX-26] 瓶，2025年9月10日后受试者每七天首先一次后空瓶5次共10瓶，总计使用10瓶（记录使\n[BBOX-27] 用总共46瓶，与实际使用情况一致。\n[BBOX-28] 8、回访ePRO以及MD。\n[BBOX-29] 既往史：更新合并用药：\n[BBOX-30] 1、鼻腔莫米松鼻喷雾剂C025 4 3-2025 7 25 每鼻 2喷/次 qd 治疗过敏性鼻炎。\n[BBOX-31] 2、苯环喹莫铵鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。\n[BBOX-32] 4、氯卓斯汀盐酸卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。\n[BBOX-33] 5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/\n[BBOX-34] 次 治疗过敏性鼻炎。\n[BBOX-35] 6、枯草抗感染治疗（生理性海水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过\n[BBOX-36] 敏性鼻炎\n[BBOX-37] 已预约受试者安全性随访时间。\n[BBOX-38] 过敏史：\n[BBOX-39] 个人史：\n[BBOX-40] 体格检查：\n[BBOX-41] 专科情况：\n[BBOX-42] 辅助检查：\n[BBOX-43] 治疗项目：\n[BBOX-44] 门诊诊断：\n[BBOX-45] 支气管哮喘\n[BBOX-46] 单病种：\n[BBOX-47] 发病时间：\n[BBOX-48] 处\n[BBOX-49] 置：\n[BBOX-50] 1心电图（心电图室做）\n[BBOX-51] 2布地奈德福莫特罗吸入粉雾剂(II)(省采)●①② 2盒2 000.00入用药,一天2次\n[BBOX-52] 30天\n[BBOX-53] 备注：\n[BBOX-54] 病情评估：\n[BBOX-55] 病情分级：\n[BBOX-56] 是否抢救病例：否\n[BBOX-57] 是否抢救成功：\n[BBOX-58] 是否为绿色通道患者：否\n[BBOX-59] 病人去向：\n[BBOX-60] CS 扫描全能王\n[BBOX-61] 3亿人都在用的扫描App\n[BBOX-62] 就诊卡\n[BBOX-63] 流水号：\n[BBOX-64] 姓名\n[BBOX-65] 龄：40岁\n[BBOX-66] 就诊科\n[BBOX-67] 日：2025-10-24 15:45:39\n[BBOX-68] 主诉：安全性电话随访\n[BBOX-69] 现病史：今日10:27\n[BBOX-70] 固定电话（020-\n[BBOX-71] （159\n[BBOX-72] 5），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无\n[BBOX-73] 不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对\n[BBOX-74] V8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试\n[BBOX-75] 者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，\n[BBOX-76] 目前无安全性异常表现。\n[BBOX-77] 合并用药更新：\n[BBOX-78] 1、小柴胡颗粒、（自行购药）2025.10.6-2025.10.8 10g tid 治疗上呼吸道感染\n[BBOX-79] 2、苯环喹溴铵鼻喷雾剂 2025.4.3-至今 每鼻2喷/次 qid 治疗过敏性鼻炎\n[BBOX-80] 3、氮卓斯汀氟替卡松鼻喷雾剂 2025.9.3-至今 每鼻2喷/次 bid 治疗过敏性鼻炎\n[BBOX-81] 4、辛芩颗粒 2024.8.21-2024.8.27 1袋 冲服 tid 治疗过敏性鼻炎\n[BBOX-82] AE：\n[BBOX-83] 上呼吸道感染 2025年10月5日-2025年10月8日 中度，非SAE，采取药物治疗措施，对试验\n[BBOX-84] 药物采取措施：剂量不变，与试验药物无关，未因该AE退出研究。\n[BBOX-85] 病历更正：\n[BBOX-86] 1、更正2024年10月22日病历，合并用药“辛芩颗粒”为“辛芩颗粒”；\n[BBOX-87] 2、更正2024年10月22日病历，合并用药“苯环喹溴铵鼻喷雾剂”为“苯环喹溴铵鼻喷雾\n[BBOX-88] 剂”；\n[BBOX-89] 3、更正2025年1月24日病历，“无收到ePro触发的哮喘警报邮件”为“有收到ePro触发的哮\n[BBOX-90] 喘警报邮件”；\n[BBOX-91] 4、更正2025年7月18日病历，“受试者漏填2025年4月28日晚间日志” 更正为：“受试者\n[BBOX-92] 漏填2025年4月28日早间日志”；\n[BBOX-93] 5、更正2024年11月6日病历，“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共\n[BBOX-94] 计用了26喷”为：“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了28\n[BBOX-95] 喷”。\n[BBOX-96] 医生\n[BBOX-97] 病历编号：\n[BBOX-98] 姓名：\n[BBOX-99] 性别：\n[BBOX-100] 年龄：40岁\n[BBOX-101] 就诊科：\n[BBOX-102] 就诊时间：2025-11-17 10:10:48\n[BBOX-103] 主诉：支气管哮喘治疗后复查：\n[BBOX-104] 现病史：2021年2月前开始出现咳嗽、咯痰，粘白，量中，能咯出，咳嗽呈阵发性、刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏。无咽痛，无伴反酸、嗳气、腹胀。无上腹部隐痛不适感，无伴发热、畏寒，影响睡眠。晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：\n[BBOX-105] 12.52*109/L 嗜酸粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定。本次门诊距上次门诊间隔时间30天。症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确。急性发作情况：两次，就诊期间急性发作：无，发作次数：0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。近3天来出现咽痛不适\n[BBOX-106] 既往史：鼻炎病史无规则治疗。打鼾明显。\n[BBOX-107] 过敏史：未发现。\n[BBOX-108] 个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。\n[BBOX-109] 体格检查：神志清，颈软，双肺呼吸音粗，未闻及明显干、湿性罗音，口腔粘膜无白斑。\n[BBOX-110] 专科情况：\n[BBOX-111] 辅助检查：\n[BBOX-112] 治疗项目：\n[BBOX-113] 门诊诊断：\n[BBOX-114] 1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、阻塞性睡眠呼吸暂停低通气综合征,4、急性咽炎\n[BBOX-115] 单病种：\n[BBOX-116] 发病时间：\n[BBOX-117] 处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不适随诊。\n[BBOX-118] 1金银花口服液◆⑤ 2盒 20.0ml,口服,一天3次(口服) 6天\n[BBOX-119] 2氨卓斯汀氟替卡松鼻喷雾剂◆ 1瓶 2.0喷,喷鼻,一天2次 30天\n[BBOX-120] 3苯环喹溴铵鼻喷雾剂◆ 3瓶 2.0喷,喷鼻,一天4次 30天\n[BBOX-121] 备注：建议在住地附近社区医疗机构随诊。\n[BBOX-122] 门(急)诊处方\n[BBOX-123] 就诊时间:2025-07-18\n[BBOX-124] 就诊科室:内科门诊\n[BBOX-125] 主诊医\n[BBOX-126] 姓名\n[BBOX-127] 性别:男\n[BBOX-128] 年龄:40岁\n[BBOX-129] 卡号:\n[BBOX-130] 患者\n[BBOX-131] 医疗证号:\n[BBOX-132] 处方号\n[BBOX-133] 地址:PT027气雾剂 2024017-呼吸科\n[BBOX-134] 身份证\n[BBOX-135] 诊断:支气管哮喘\n[BBOX-136] 西药处方\n[BBOX-137] 组号\n[BBOX-138] 项目名称\n[BBOX-139] 规格\n[BBOX-140] 总量\n[BBOX-141] 单价\n[BBOX-142] 金额\n[BBOX-143] R:\n[BBOX-144] 布地奈德福莫特罗吸入粉雾剂0.125/0.006*60吸6盒\n[BBOX-145] 183.41100.46\n[BBOX-146] Sig\n[BBOX-147] 2吸/次,吸入,bid*90天\n[BBOX-148] 门(急)诊处方\n[BBOX-149] 就诊时间:2025-04-25\n[BBOX-150] 就诊科室:内科门诊\n[BBOX-151] 主诊\n[BBOX-152] 姓名\n[BBOX-153] 性别:男\n[BBOX-154] 年龄:40岁\n[BBOX-155] 卡号:\n[BBOX-156] 患者类型:GLP支付\n[BBOX-157] 医疗证号:\n[BBOX-158] 处方号\n[BBOX-159] 地址:PT027气雾剂 2024017-呼吸科\n[BBOX-160] 身份证号:\n[BBOX-161] 诊断:支气管哮喘\n[BBOX-162] 西药处方\n[BBOX-163] 组号\n[BBOX-164] 项目名称\n[BBOX-165] 规格\n[BBOX-166] 总量\n[BBOX-167] 单价\n[BBOX-168] 金额\n[BBOX-169] R:\n[BBOX-170] 布地奈德福莫特罗吸入粉雾剂(II)0.5mg*60吸6盒\n[BBOX-171] 183.41100.46\n[BBOX-172] Sig\n[BBOX-173] 2吸/次,吸入,bid*90天\n[BBOX-174] 门(急)诊处方\n[BBOX-175] 就诊时间：2025-02-26\n[BBOX-176] 就诊科室：内科门诊\n[BBOX-177] 主诊\n[BBOX-178] 性别：男\n[BBOX-179] 年龄：40岁\n[BBOX-180] 卡号\n[BBOX-181] 医疗证号：\n[BBOX-182] 处方\n[BBOX-183] 015\n[BBOX-184] 地址：PT027气雾剂 2024017-呼吸科\n[BBOX-185] 身份证号：\n[BBOX-186] 诊断：支气管哮喘\n[BBOX-187] 西药处方\n[BBOX-188] 组号\n[BBOX-189] 项目名称\n[BBOX-190] 规格\n[BBOX-191] 总量\n[BBOX-192] 单价\n[BBOX-193] 金额\n[BBOX-194] R:\n[BBOX-195] 布地奈德福莫特罗吸入粉雾剂BDI/●@1g*60吸2盒\n[BBOX-196] 183.41\n[BBOX-197] 366.82\n[BBOX-198] Sig\n[BBOX-199] 2吸/次,吸入,bid*30天\n[BBOX-200] 门(急)诊处方\n[BBOX-201] 就诊时间:2025-01-24\n[BBOX-202] 就诊科室:内科门诊\n[BBOX-203] 主诊医\n[BBOX-204] 姓名\n[BBOX-205] 性别:男\n[BBOX-206] 年龄:40岁\n[BBOX-207] 卡号:4\n[BBOX-208] 患者类型:GCP支付\n[BBOX-209] 医疗证号:\n[BBOX-210] 处方号:\n[BBOX-211] 地址:PT027气雾剂 2024017-呼吸科\n[BBOX-212] 身份证号:\n[BBOX-213] 诊断:支气管哮喘\n[BBOX-214] 西药处方\n[BBOX-215] 组号\n[BBOX-216] 项目名称\n[BBOX-217] 规格\n[BBOX-218] 总量\n[BBOX-219] 单价\n[BBOX-220] 金额\n[BBOX-221] R:\n[BBOX-222] 布地奈德福莫特罗吸入粉雾剂HIV●(50ug*60吸4盒\n[BBOX-223] 183.41 733.64\n[BBOX-224] Sig\n[BBOX-225] 2吸/次,吸入,bid*60天\n[BBOX-226] 门(急)诊处方\n[BBOX-227] 就诊时间:2025-01-03\n[BBOX-228] 就诊科室:内科门诊\n[BBOX-229] 主诊\n[BBOX-230] 性别:男\n[BBOX-231] 年龄:40岁\n[BBOX-232] 卡号\n[BBOX-233] 患者类型:GCP支付\n[BBOX-234] 医疗证号:\n[BBOX-235] 处方\n[BBOX-236] 地址:PT027气雾剂 2024017-呼吸科\n[BBOX-237] 身份证号:\n[BBOX-238] 诊断:支气管哮喘\n[BBOX-239] 西药处方\n[BBOX-240] 组号\n[BBOX-241] 项目名称\n[BBOX-242] 规格\n[BBOX-243] 总量\n[BBOX-244] 单价\n[BBOX-245] 金额\n[BBOX-246] R:\n[BBOX-247] 布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●⑥ug*60吸2盒\n[BBOX-248] 183.41 366.82\n[BBOX-249] Sig\n[BBOX-250] 2吸/次,吸入,bid*30天\n[BBOX-251] 医师:\n[BBOX-252] 医生编号:1326\n[BBOX-253] 配剂人:\n[BBOX-254] 核对人:\n[BBOX-255] 合计:\n[BBOX-256] 收费员:\n[BBOX-257] CS 扫描全能王\n[BBOX-258] 3亿人都在用的扫描App\n[BBOX-259] 门(急)诊处方\n[BBOX-260] 就诊时间:2024-12-04\n[BBOX-261] 就诊科室:内科门诊\n[BBOX-262] 主诊\n[BBOX-263] 姓名\n[BBOX-264] 性别:男\n[BBOX-265] 年龄:39岁\n[BBOX-266] 卡号\n[BBOX-267] 患者\n[BBOX-268] 医疗证号:\n[BBOX-269] 处方\n[BBOX-270] 地址:PT027气雾剂 2024017-呼吸科\n[BBOX-271] 身份证号:\n[BBOX-272] 诊断:支气管哮喘\n[BBOX-273] 西药处方\n[BBOX-274] 组号\n[BBOX-275] 项目名称\n[BBOX-276] 规格\n[BBOX-277] 总量\n[BBOX-278] 单价\n[BBOX-279] 金额\n[BBOX-280] R:\n[BBOX-281] 布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●(50ug*60吸2盒\n[BBOX-282] 183.41 366.82\n[BBOX-283] Sig\n[BBOX-284] 2吸/次,吸入,bid*30天\n[BBOX-285] 激发试验检查报告\n[BBOX-286] 姓名：\n[BBOX-287] 测试号：\n[BBOX-288] 门诊/住院号：\n[BBOX-289] 000\n[BBOX-290] 年龄：\n[BBOX-291] 出生日期：\n[BBOX-292] 19\n[BBOX-293] 性别：\n[BBOX-294] 男\n[BBOX-295] 身高：\n[BBOX-296] 170\n[BBOX-297] 病区：\n[BBOX-298] 内科门诊\n[BBOX-299] 体重：\n[BBOX-300] 81 kg\n[BBOX-301] 机器编号：\n[BBOX-302] 床号：\n[BBOX-303] 电话：\n[BBOX-304] Pred\n[BBOX-305] A1\n[BBOX-306] A1/Pd\n[BBOX-307] NS\n[BBOX-308] P1 chg%1\n[BBOX-309] P2 chg%2\n[BBOX-310] P3 chg%3\n[BBOX-311] FVC\n[BBOX-312] [L]\n[BBOX-313] 4.84\n[BBOX-314] 4.69\n[BBOX-315] 97.1\n[BBOX-316] 4.29\n[BBOX-317] 4.22\n[BBOX-318] -10.1\n[BBOX-319] 3.64\n[BBOX-320] -22.5\n[BBOX-321] 4.01\n[BBOX-322] -14.6\n[BBOX-323] PEV 1\n[BBOX-324] [L]\n[BBOX-325] 4.01\n[BBOX-326] 3.05\n[BBOX-327] 76.2\n[BBOX-328] 2.72\n[BBOX-329] 2.69\n[BBOX-330] -11.8\n[BBOX-331] 2.24\n[BBOX-332] -26.5\n[BBOX-333] 2.44\n[BBOX-334] -20.0\n[BBOX-335] PEV 1 % PVC\n[BBOX-336] [%]\n[BBOX-337] 83.32\n[BBOX-338] 65.02\n[BBOX-339] 78.0\n[BBOX-340] 63.54\n[BBOX-341] 63.83\n[BBOX-342] -1.82\n[BBOX-343] 61.73\n[BBOX-344] -5.06\n[BBOX-345] 60.92\n[BBOX-346] -6.30\n[BBOX-347] PEV 1 % VC MAX\n[BBOX-348] [%]\n[BBOX-349] 80.55\n[BBOX-350] 64.94\n[BBOX-351] 80.6\n[BBOX-352] 62.34\n[BBOX-353] 63.83\n[BBOX-354] -1.70\n[BBOX-355] 61.73\n[BBOX-356] -4.94\n[BBOX-357] 60.92\n[BBOX-358] -6.18\n[BBOX-359] VC MAX\n[BBOX-360] [L]\n[BBOX-361] 5.05\n[BBOX-362] 4.70\n[BBOX-363] 93.1\n[BBOX-364] 4.37\n[BBOX-365] 4.22\n[BBOX-366] -10.2\n[BBOX-367] 3.64\n[BBOX-368] -22.6\n[BBOX-369] 4.01\n[BBOX-370] -14.7\n[BBOX-371] PEP\n[BBOX-372] [L/s]\n[BBOX-373] 9.37\n[BBOX-374] 9.95\n[BBOX-375] 106.2\n[BBOX-376] 9.06\n[BBOX-377] 7.81\n[BBOX-378] -21.5\n[BBOX-379] 6.73\n[BBOX-380] -32.3\n[BBOX-381] 8.22\n[BBOX-382] -17.4\n[BBOX-383] MMEF 75/25\n[BBOX-384] [L/s]\n[BBOX-385] 4.52\n[BBOX-386] 1.54\n[BBOX-387] 34.1\n[BBOX-388] 1.33\n[BBOX-389] 1.34\n[BBOX-390] -12.9\n[BBOX-391] 1.14\n[BBOX-392] -25.8\n[BBOX-393] 1.23\n[BBOX-394] -20.0\n[BBOX-395] MEF 50\n[BBOX-396] [L/s]\n[BBOX-397] 5.17\n[BBOX-398] 1.97\n[BBOX-399] 38.1\n[BBOX-400] 1.66\n[BBOX-401] 1.71\n[BBOX-402] -13.4\n[BBOX-403] 1.34\n[BBOX-404] -31.8\n[BBOX-405] 1.42\n[BBOX-406] -28.0\n[BBOX-407] MEF 25\n[BBOX-408] [L/s]\n[BBOX-409] 2.29\n[BBOX-410] 0.58\n[BBOX-411] 25.5\n[BBOX-412] 0.52\n[BBOX-413] 0.53\n[BBOX-414] -9.87\n[BBOX-415] 0.50\n[BBOX-416] -14.6\n[BBOX-417] 0.49\n[BBOX-418] -15.7\n[BBOX-419] PET\n[BBOX-420] [s]\n[BBOX-421] 6.72\n[BBOX-422] 6.87\n[BBOX-423] 6.93\n[BBOX-424] 3.16\n[BBOX-425] 6.75\n[BBOX-426] 0.57\n[BBOX-427] 6.74\n[BBOX-428] 0.38\n[BBOX-429] V backextrapolation ex [L]\n[BBOX-430] 0.13\n[BBOX-431] 0.09\n[BBOX-432] 0.10\n[BBOX-433] -20.0\n[BBOX-434] 0.08\n[BBOX-435] -41.6\n[BBOX-436] 0.08\n[BBOX-437] -38.5\n[BBOX-438] PIF\n[BBOX-439] [L/s]\n[BBOX-440] 8.04\n[BBOX-441] 7.96\n[BBOX-442] 7.58\n[BBOX-443] -5.76\n[BBOX-444] 6.16\n[BBOX-445] -23.3\n[BBOX-446] 7.78\n[BBOX-447] -3.20\n[BBOX-448] FIF 50\n[BBOX-449] [L/s]\n[BBOX-450] 7.99\n[BBOX-451] 7.86\n[BBOX-452] 7.16\n[BBOX-453] -10.3\n[BBOX-454] 5.36\n[BBOX-455] -32.9\n[BBOX-456] 7.08\n[BBOX-457] -11.3\n[BBOX-458] MVV\n[BBOX-459] [L/min]\n[BBOX-460] 141.88\n[BBOX-461] BF MVV\n[BBOX-462] [1/min]\n[BBOX-463] Cumulated dose\n[BBOX-464] 0.072\n[BBOX-465] 0.078\n[BBOX-466] 0.312\n[BBOX-467] 2 Puf\n[BBOX-468] F/V ex\n[BBOX-469] F/V in\n[BBOX-470] Vol [L]\n[BBOX-471] Vol%VCmax\n[BBOX-472] VCmax\n[BBOX-473] Time [s]\n[BBOX-474] PD[-20] FEV 1: 0.2117 mg Cumulated\n[BBOX-475] PD[-20] PEF: < 0.078 mg Cumulated\n[BBOX-476] PD[] FEV1%I: could not be calculated!\n[BBOX-477] 意见：\n[BBOX-478] 2022/6/08 10:23:56上午\n[BBOX-479] 1.轻度阻塞性通气功能障碍。\n[BBOX-480] 2.支气管激发试验阳性(累计吸入乙酰甲胆碱0.312mg，FEV1下降大于20%，PD20=0.2117mg，气道高反应性(AHR)为中度\n[BBOX-481] 通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后FEV1恢复至预计值80%。\n[BBOX-482] CS 扫描全能王\n[BBOX-483] 3亿人都在用的扫描App\n[BBOX-484] 检查日期：2021/1/21\n[BBOX-485] 检查时间：16.43\n[BBOX-486] 编号：16\n[BBOX-487] 广州医科大学附属第三医院\n[BBOX-488] 支气管扩张试验检查报告\n[BBOX-489] 姓名：\n[BBOX-490] 测试号：\n[BBOX-491] 年龄：36岁\n[BBOX-492] 性别：男\n[BBOX-493] 病区：\n[BBOX-494] 机器编号：\n[BBOX-495] 门诊/住院号：\n[BBOX-496] 出生日期：\n[BBOX-497] 身高：\n[BBOX-498] 体重：\n[BBOX-499] 床号：\n[BBOX-500] 电话：\n[BBOX-501] Pred\n[BBOX-502] A1\n[BBOX-503] A1/Pd\n[BBOX-504] P1\n[BBOX-505] A2/Pd\n[BBOX-506] chg%1\n[BBOX-507] P2\n[BBOX-508] A3/Pd\n[BBOX-509] chg%2\n[BBOX-510] P3\n[BBOX-511] A4/Pd\n[BBOX-512] chg%3\n[BBOX-513] FVC\n[BBOX-514] [L]\n[BBOX-515] 4.86\n[BBOX-516] 3.48\n[BBOX-517] 71.5%\n[BBOX-518] 4.01\n[BBOX-519] 82.4%\n[BBOX-520] 15.19\n[BBOX-521] 4.15\n[BBOX-522] 85.4%\n[BBOX-523] 19.47\n[BBOX-524] 4.01\n[BBOX-525] 82.6%\n[BBOX-526] 15.47\n[BBOX-527] FEV 1\n[BBOX-528] [L]\n[BBOX-529] 4.03\n[BBOX-530] 1.97\n[BBOX-531] 48.8%\n[BBOX-532] 2.33\n[BBOX-533] 57.9%\n[BBOX-534] 18.59\n[BBOX-535] 2.33\n[BBOX-536] 57.8%\n[BBOX-537] 18.48\n[BBOX-538] 2.44\n[BBOX-539] 60.5%\n[BBOX-540] 24.02\n[BBOX-541] FEV 1 % FVC\n[BBOX-542] [%]\n[BBOX-543] 83.32\n[BBOX-544] 56.62\n[BBOX-545] 68.0%\n[BBOX-546] 58.29\n[BBOX-547] 70.0%\n[BBOX-548] 2.95\n[BBOX-549] 56.15\n[BBOX-550] 67.4%\n[BBOX-551] -0.83\n[BBOX-552] 60.81\n[BBOX-553] 73.0%\n[BBOX-554] 7.40\n[BBOX-555] FEV 1 % VC MAX\n[BBOX-556] [%]\n[BBOX-557] 80.73\n[BBOX-558] 56.07\n[BBOX-559] 69.5%\n[BBOX-560] 58.29\n[BBOX-561] 72.2%\n[BBOX-562] 3.96\n[BBOX-563] 56.15\n[BBOX-564] 69.5%\n[BBOX-565] 0.14\n[BBOX-566] 60.81\n[BBOX-567] 75.3%\n[BBOX-568] 8.45\n[BBOX-569] VC MAX\n[BBOX-570] [L]\n[BBOX-571] 5.08\n[BBOX-572] 3.51\n[BBOX-573] 69.1%\n[BBOX-574] 4.01\n[BBOX-575] 78.9%\n[BBOX-576] 14.07\n[BBOX-577] 4.15\n[BBOX-578] 81.8%\n[BBOX-579] 18.31\n[BBOX-580] 4.01\n[BBOX-581] 79.1%\n[BBOX-582] 14.35\n[BBOX-583] PEF\n[BBOX-584] [L/s]\n[BBOX-585] 9.41\n[BBOX-586] 6.61\n[BBOX-587] 70.3%\n[BBOX-588] 7.99\n[BBOX-589] 85.0%\n[BBOX-590] 20.93\n[BBOX-591] 7.91\n[BBOX-592] 84.1%\n[BBOX-593] 19.63\n[BBOX-594] 8.07\n[BBOX-595] 85.7%\n[BBOX-596] 22.02\n[BBOX-597] MMEF 75/25\n[BBOX-598] [L/s]\n[BBOX-599] 4.57\n[BBOX-600] 0.81\n[BBOX-601] 17.7%\n[BBOX-602] 0.96\n[BBOX-603] 21.1%\n[BBOX-604] 19.59\n[BBOX-605] 1.03\n[BBOX-606] 22.6%\n[BBOX-607] 28.17\n[BBOX-608] 1.12\n[BBOX-609] 24.6%\n[BBOX-610] 39.07\n[BBOX-611] MEF 50\n[BBOX-612] [L/s]\n[BBOX-613] 5.20\n[BBOX-614] 1.00\n[BBOX-615] 19.2%\n[BBOX-616] 1.29\n[BBOX-617] 24.8%\n[BBOX-618] 29.25\n[BBOX-619] 1.30\n[BBOX-620] 24.9%\n[BBOX-621] 29.87\n[BBOX-622] 1.53\n[BBOX-623] 29.3%\n[BBOX-624] 52.75\n[BBOX-625] MEF 25\n[BBOX-626] [L/s]\n[BBOX-627] 2.32\n[BBOX-628] 0.39\n[BBOX-629] 16.7%\n[BBOX-630] 0.38\n[BBOX-631] 16.4%\n[BBOX-632] -1.68\n[BBOX-633] 0.50\n[BBOX-634] 21.6%\n[BBOX-635] 29.78\n[BBOX-636] 0.41\n[BBOX-637] 17.9%\n[BBOX-638] 7.18\n[BBOX-639] FET\n[BBOX-640] [s]\n[BBOX-641] 15.24\n[BBOX-642] 6.42\n[BBOX-643] -57.87\n[BBOX-644] 6.30\n[BBOX-645] -58.63\n[BBOX-646] 6.55\n[BBOX-647] -57.05\n[BBOX-648] V backextrapolati\n[BBOX-649] [L/s]\n[BBOX-650] 0.07\n[BBOX-651] 0.07\n[BBOX-652] 0.89\n[BBOX-653] 0.09\n[BBOX-654] 17.79\n[BBOX-655] 0.08\n[BBOX-656] 6.12\n[BBOX-657] PIF\n[BBOX-658] [L/s]\n[BBOX-659] 7.03\n[BBOX-660] 7.39\n[BBOX-661] 5.19\n[BBOX-662] 7.17\n[BBOX-663] 1.99\n[BBOX-664] 7.16\n[BBOX-665] 1.91\n[BBOX-666] FIV1\n[BBOX-667] [L]\n[BBOX-668] 3.40\n[BBOX-669] 3.76\n[BBOX-670] 10.58\n[BBOX-671] 3.68\n[BBOX-672] 8.26\n[BBOX-673] 3.60\n[BBOX-674] 5.96\n[BBOX-675] PEF50 % PIF50\n[BBOX-676] [%]\n[BBOX-677] 16.56\n[BBOX-678] 21.70\n[BBOX-679] 31.06\n[BBOX-680] 19.81\n[BBOX-681] 19.65\n[BBOX-682] 24.71\n[BBOX-683] 49.20\n[BBOX-684] MVV\n[BBOX-685] [L/min]\n[BBOX-686] 142.69\n[BBOX-687] BF MVV\n[BBOX-688] [1/min]\n[BBOX-689] 意见：\n[BBOX-690] 1.重度混合性肺通气功能障碍。\n[BBOX-691] 2.支气管舒张试验阳性。\n[BBOX-692] （通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后PEV1较基线增加大于12%，且绝对值增加大于200ml）\n[BBOX-693] CS 扫描全能王\n[BBOX-694] 3亿人都在用的扫描App\n[BBOX-695] 广州医科大学附属第三医院\n[BBOX-696] 处方笺\n[BBOX-697] 普通\n[BBOX-698] 诊疗卡\n[BBOX-699] 患者姓名\n[BBOX-700] 年龄：41岁\n[BBOX-701] 费别：南医保\n[BBOX-702] 科室：内科门诊（荔湾）\n[BBOX-703] 日期：2026-01-05 17:17:14\n[BBOX-704] 处方号\n[BBOX-705] 地址：荔湾\n[BBOX-706] 2024017-呼吸科\n[BBOX-707] 联系电话\n[BBOX-708] 身份号码：\n[BBOX-709] 2739\n[BBOX-710] 诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],急性气管支气管炎\n[BBOX-711] R\n[BBOX-712] P:\n[BBOX-713] 布地奈德福莫特罗吸入粉雾剂(II) 160ug/4.5ug*60吸\n[BBOX-714] 2盒\n[BBOX-715] 剂量：每次2吸\n[BBOX-716] （\n[BBOX-717] 1\n[BBOX-718] 30\n[BBOX-719] 盒）\n[BBOX-720] 用法：吸入用药\n[BBOX-721] bid\n[BBOX-722] 01-05\n[BBOX-723] 处方金额：366.82元\n[BBOX-724] 取药药房：门诊西药房（荔湾）\n[BBOX-725] 广州医科大学附属第三医院\n[BBOX-726] The Third Affiliated Hospital of Guangzhou Medical University\n[BBOX-727] 门(急)诊病历信息\n[BBOX-728] 就诊卡\n[BBOX-729] 流水\n[BBOX-730] 姓\n[BBOX-731] 病历编号:\n[BBOX-732] 年 龄:41岁\n[BBOX-733] 就诊科室:内科门诊(荔湾) 医\n[BBOX-734] 就诊时间:2026-01-05 17:07:54\n[BBOX-735] 主 诉:支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天\n[BBOX-736] 现 病 史:2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激\n[BBOX-737] 性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流\n[BBOX-738] 涕、嗅觉,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响\n[BBOX-739] 睡眠,晨起有咽干,曾到本院就诊两次,症状不见明显缓解。2021-1-9血常规:白细胞:\n[BBOX-740] 12.52*109/L 嗜酸粒细胞:0.65*109/L 5.2%,经治疗后症状明显缓解。无咳嗽、咯痰、气\n[BBOX-741] 促。病情稳定,本次门诊距上次门诊间隔时间30天。症状控制情况:过去4周,患者:吸入\n[BBOX-742] 药物使用情况:遵医嘱使用;吸入装置使用情况:正确。急性发作情况:两次,就诊期间急\n[BBOX-743] 性发作:无,发作次数:0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。长期规律使用信必\n[BBOX-744] 可160/4.5ug 2吸 bid治疗,5天前开始出现咳嗽、咯痰,黄白痰,量少,难以咯出,咳嗽以\n[BBOX-745] 夜间为主。无气促,伴咽息,鼻塞、流涕、喷嚏,无发热。\n[BBOX-746] 既 往 史:鼻炎病史无规则治疗。打鼾明显。\n[BBOX-747] 过 敏 史:未发现;\n[BBOX-748] 个 人 史:否认遗传病史,吸烟10年,20支/日,2018年戒烟。偶饮酒。2021-12-20已打第\n[BBOX-749] 三针新冠疫苗。\n[BBOX-750] 体格检查:神志清,颈软,双肺呼吸音粗,可闻及散在哮鸣音,口腔粘膜无白斑。\n[BBOX-751] 专科情况:\n[BBOX-752] 辅助检查:\n[BBOX-753] 治疗项目:\n[BBOX-754] 门诊诊断:\n[BBOX-755] 1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎\n[BBOX-756] 处 置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。\n[BBOX-757] 布地奈德福莫特罗吸入粉雾剂(II)2盒 2.0吸,吸入用药,一天2次 30天\n[BBOX-758] (省采)●①⑤\n[BBOX-759] 左氧氟沙星片(省采)●⑥ 5片 0.5g,口服,每日1次(口服) 5天\n[BBOX-760] 第1页\n[BBOX-761] 广州医科大学附属第三医院\n[BBOX-762] The Third Affiliated Hospital of Guangzhou Medical University\n[BBOX-763] 门(急)诊病历信息\n[BBOX-764] 复方甲氧那明胶囊(省采)●② 1瓶 1.0粒,餐后口服,一天3次(口服) 5天\n[BBOX-765] 盐酸氨溴索分散片(省采)●⑥ 15片 30.0mg,餐后口服,一天3次(口服) 5\n[BBOX-766] 天\n[BBOX-767] 醋酸泼尼松片●②④ 6片 10.0mg,口服,每早1次(口服) 3天\n[BBOX-768] 备 注:建议在住地附近社区医疗机构随诊。\n[BBOX-769] 门诊/住院病历信息\n[BBOX-770] 就诊卡号：\n[BBOX-771] 病历编号：\n[BBOX-772] 姓名：\n[BBOX-773] 性别：男\n[BBOX-774] 年龄：41岁\n[BBOX-775] 就诊科室：内科门诊（荔湾）\n[BBOX-776] 就诊时间：2026-02-04 11:21:11\n[BBOX-777] 主诉：支气管哮喘治疗后复查\n[BBOX-778] 现病史：2021年2月前开始出现咳嗽、咳痰，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sg 2吸 bid治疗。\n[BBOX-779] 既往史：鼻炎病史无规则治疗，打鼾明显。\n[BBOX-780] 过敏史：未发现；\n[BBOX-781] 个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。\n[BBOX-782] 体格检查：神志清，颈软，双肺呼吸音粗，可闻及散在哮鸣音，口腔粘膜无白斑。\n[BBOX-783] 专科情况：\n[BBOX-784] 辅助检查：\n[BBOX-785] 治疗项目：\n[BBOX-786] 门诊诊断：\n[BBOX-787] 1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、急性气管支气管炎\n[BBOX-788] 单病种：\n[BBOX-789] 发病时间：\n[BBOX-790] 处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不遥随诊。\n[BBOX-791] 布地奈德福莫特罗吸入粉雾剂(II)(省\n[BBOX-792] 2 2.0班，吸入用药，一天2次\n[BBOX-793] 30\n[BBOX-794] 采)●①②\n[BBOX-795] 查天\n[BBOX-796] 广州医科大学附属第三医院\n[BBOX-797] 肺功能检查报告\n[BBOX-798] 地址：广州市多宝路63号 电话：020-81292126\n[BBOX-799] COSMED\n[BBOX-800] 姓名：\n[BBOX-801] 科室/床号：\n[BBOX-802] ID：\n[BBOX-803] 出生日期：1984/12/8\n[BBOX-804] 预计值：ERS 93\n[BBOX-805] 日期：2024/10/22\n[BBOX-806] 性别：Male\n[BBOX-807] 地区修正：Chinese\n[BBOX-808] 详细描述：内科门诊\n[BBOX-809] Company：\n[BBOX-810] 年龄：39\n[BBOX-811] 体重(Kg)：89.0\n[BBOX-812] 身高(cm)：177.5\n[BBOX-813] BMI(Kg/m²：28.2\n[BBOX-814] 吸烟：曾经(10/20)\n[BBOX-815] 用力肺活量 Forced Vital Capacity\n[BBOX-816] F(l/s)\n[BBOX-817] V(l)\n[BBOX-818] BEST #3 - 2024/10/22 11:03\n[BBOX-819] 沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38\n[BBOX-820] 沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39\n[BBOX-821] 沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41\n[BBOX-822] 沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38\n[BBOX-823] 沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39\n[BBOX-824] 沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41\n[BBOX-825] MEF75%\n[BBOX-826] MEF50%\n[BBOX-827] MEF25%\n[BBOX-828] FVC\n[BBOX-829] PEF\n[BBOX-830] FEV1\n[BBOX-831] ATS\n[BBOX-832] 12t(s)\n[BBOX-833] -1\n[BBOX-834] 0\n[BBOX-835] 1\n[BBOX-836] 2\n[BBOX-837] 3\n[BBOX-838] 4\n[BBOX-839] 5\n[BBOX-840] 6\n[BBOX-841] 7\n[BBOX-842] 8\n[BBOX-843] 9\n[BBOX-844] 10\n[BBOX-845] 11\n[BBOX-846] 12\n[BBOX-847] 1\n[BBOX-848] 2\n[BBOX-849] 3\n[BBOX-850] 4\n[BBOX-851] 5\n[BBOX-852] 6\n[BBOX-853] 7\n[BBOX-854] 8\n[BBOX-855] 9\n[BBOX-856] 10\n[BBOX-857] 11\n[BBOX-858] 12\n[BBOX-859] 13\n[BBOX-860] 14\n[BBOX-861] 1\n[BBOX-862] 2\n[BBOX-863] 3\n[BBOX-864] 4\n[BBOX-865] 5\n[BBOX-866] 6\n[BBOX-867] 7\n[BBOX-868] 8\n[BBOX-869] 9\n[BBOX-870] 10\n[BBOX-871] 11\n[BBOX-872] 12\n[BBOX-873] 13\n[BBOX-874] 14\n[BBOX-875] 15\n[BBOX-876] 16\n[BBOX-877] 17\n[BBOX-878] 18\n[BBOX-879] 19\n[BBOX-880] 20\n[BBOX-881] 21\n[BBOX-882] 22\n[BBOX-883] 23\n[BBOX-884] 24\n[BBOX-885] 25\n[BBOX-886] 26\n[BBOX-887] 27\n[BBOX-888] 28\n[BBOX-889] 29\n[BBOX-890] 30\n[BBOX-891] 31\n[BBOX-892] 32\n[BBOX-893] 33\n[BBOX-894] 34\n[BBOX-895] 35\n[BBOX-896] 36\n[BBOX-897] 37\n[BBOX-898] 38\n[BBOX-899] 39\n[BBOX-900] 40\n[BBOX-901] 41\n[BBOX-902] 42\n[BBOX-903] 43\n[BBOX-904] 44\n[BBOX-905] 45\n[BBOX-906] 46\n[BBOX-907] 47\n[BBOX-908] 48\n[BBOX-909] 49\n[BBOX-910] 50\n[BBOX-911] 51\n[BBOX-912] 52\n[BBOX-913] 53\n[BBOX-914] 54\n[BBOX-915] 55\n[BBOX-916] 56\n[BBOX-917] 57\n[BBOX-918] 58\n[BBOX-919] 59\n[BBOX-920] 60\n[BBOX-921] 61\n[BBOX-922] 62\n[BBOX-923] 63\n[BBOX-924] 64\n[BBOX-925] 65\n[BBOX-926] 66\n[BBOX-927] 67\n[BBOX-928] 68\n[BBOX-929] 69\n[BBOX-930] 70\n[BBOX-931] 71\n[BBOX-932] 72\n[BBOX-933] 73\n[BBOX-934] 74\n[BBOX-935] 75\n[BBOX-936] 76\n[BBOX-937] 77\n[BBOX-938] 78\n[BBOX-939] 79\n[BBOX-940] 80\n[BBOX-941] 81\n[BBOX-942] 82\n[BBOX-943] 83\n[BBOX-944] 84\n[BBOX-945] 85\n[BBOX-946] 86\n[BBOX-947] 87\n[BBOX-948] 88\n[BBOX-949] 89\n[BBOX-950] 90\n[BBOX-951] 91\n[BBOX-952] 92\n[BBOX-953] 93\n[BBOX-954] 94\n[BBOX-955] 95\n[BBOX-956] 96\n[BBOX-957] 97\n[BBOX-958] 98\n[BBOX-959] 99\n[BBOX-960] 100\n[BBOX-961] 101\n[BBOX-962] 102\n[BBOX-963] 103\n[BBOX-964] 104\n[BBOX-965] 105\n[BBOX-966] 106\n[BBOX-967] 107\n[BBOX-968] 108\n[BBOX-969] 109\n[BBOX-970] 110\n[BBOX-971] 111\n[BBOX-972] 112\n[BBOX-973] 113\n[BBOX-974] 114\n[BBOX-975] 115\n[BBOX-976] 116\n[BBOX-977] 117\n[BBOX-978] 118\n[BBOX-979] 119\n[BBOX-980] 120\n[BBOX-981] 121\n[BBOX-982] 122\n[BBOX-983] 123\n[BBOX-984] 124\n[BBOX-985] 125\n[BBOX-986] 126\n[BBOX-987] 127\n[BBOX-988] 128\n[BBOX-989] 129\n[BBOX-990] 130\n[BBOX-991] 131\n[BBOX-992] 132\n[BBOX-993] 133\n[BBOX-994] 134\n[BBOX-995] 135\n[BBOX-996] 136\n[BBOX-997] 137\n[BBOX-998] 138\n[BBOX-999] 139\n[BBOX-1000] 140\n[BBOX-1001] 141\n[BBOX-1002] 142\n[BBOX-1003] 143\n[BBOX-1004] 144\n[BBOX-1005] 145\n[BBOX-1006] 146\n[BBOX-1007] 147\n[BBOX-1008] 148\n[BBOX-1009] 149\n[BBOX-1010] 150\n[BBOX-1011] 151\n[BBOX-1012] 152\n[BBOX-1013] 153\n[BBOX-1014] 154\n[BBOX-1015] 155\n[BBOX-1016] 156\n[BBOX-1017] 157\n[BBOX-1018] 158\n[BBOX-1019] 159\n[BBOX-1020] 160\n[BBOX-1021] 161\n[BBOX-1022] 162\n[BBOX-1023] 163\n[BBOX-1024] 164\n[BBOX-1025] 165\n[BBOX-1026] 166\n[BBOX-1027] 167\n[BBOX-1028] 168\n[BBOX-1029] 169\n[BBOX-1030] 170\n[BBOX-1031] 171\n[BBOX-1032] 172\n[BBOX-1033] 173\n[BBOX-1034] 174\n[BBOX-1035] 175\n[BBOX-1036] 176\n[BBOX-1037] 177\n[BBOX-1038] 178\n[BBOX-1039] 179\n[BBOX-1040] 180\n[BBOX-1041] 181\n[BBOX-1042] 182\n[BBOX-1043] 183\n[BBOX-1044] 184\n[BBOX-1045] 185\n[BBOX-1046] 186\n[BBOX-1047] 187\n[BBOX-1048] 188\n[BBOX-1049] 189\n[BBOX-1050] 190\n[BBOX-1051] 191\n[BBOX-1052] 192\n[BBOX-1053] 193\n[BBOX-1054] 194\n[BBOX-1055] 195\n[BBOX-1056] 196\n[BBOX-1057] 197\n[BBOX-1058] 198\n[BBOX-1059] 199\n[BBOX-1060] 200\n[BBOX-1061] 201\n[BBOX-1062] 202\n[BBOX-1063] 203\n[BBOX-1064] 204\n[BBOX-1065] 205\n[BBOX-1066] 206\n[BBOX-1067] 207\n[BBOX-1068] 208\n[BBOX-1069] 209\n[BBOX-1070] 210\n[BBOX-1071] 211\n[BBOX-1072] 212\n[BBOX-1073] 213\n[BBOX-1074] 214\n[BBOX-1075] 215\n[BBOX-1076] 216\n[BBOX-1077] 217\n[BBOX-1078] 218\n[BBOX-1079] 219\n[BBOX-1080] 220\n[BBOX-1081] 221\n[BBOX-1082] 222\n[BBOX-1083] 223\n[BBOX-1084] 224\n[BBOX-1085] 225\n[BBOX-1086] 226\n[BBOX-1087] 227\n[BBOX-1088] 228\n[BBOX-1089] 229\n[BBOX-1090] 230\n[BBOX-1091] 231\n[BBOX-1092] 232\n[BBOX-1093] 233\n[BBOX-1094] 234\n[BBOX-1095] 235\n[BBOX-1096] 236\n[BBOX-1097] 237\n[BBOX-1098] 238\n[BBOX-1099] 239\n[BBOX-1100] 240\n[BBOX-1101] 241\n[BBOX-1102] 242\n[BBOX-1103] 243\n[BBOX-1104] 244\n[BBOX-1105] 245\n[BBOX-1106] 246\n[BBOX-1107] 247\n[BBOX-1108] 248\n[BBOX-1109] 249\n[BBOX-1110] 250\n[BBOX-1111] 251\n[BBOX-1112] 252\n[BBOX-1113] 253\n[BBOX-1114] 254\n[BBOX-1115] 255\n[BBOX-1116] 256\n[BBOX-1117] 257\n[BBOX-1118] 258\n[BBOX-1119] 259\n[BBOX-1120] 260\n[BBOX-1121] 261\n[BBOX-1122] 262\n[BBOX-1123] 263\n[BBOX-1124] 264\n[BBOX-1125] 265\n[BBOX-1126] 266\n[BBOX-1127] 267\n[BBOX-1128] 268\n[BBOX-1129] 269\n[BBOX-1130] 270\n[BBOX-1131] 271\n[BBOX-1132] 272\n[BBOX-1133] 273\n[BBOX-1134] 274\n[BBOX-1135] 275\n[BBOX-1136] 276\n[BBOX-1137] 277\n[BBOX-1138] 278\n[BBOX-1139] 279\n[BBOX-1140] 280\n[BBOX-1141] 281\n[BBOX-1142] 282\n[BBOX-1143] 283\n[BBOX-1144] 284\n[BBOX-1145] 285\n[BBOX-1146] 286\n[BBOX-1147] 287\n[BBOX-1148] 288\n[BBOX-1149] 289\n[BBOX-1150] 290\n[BBOX-1151] 291\n[BBOX-1152] 292\n[BBOX-1153] 293\n[BBOX-1154] 294\n[BBOX-1155] 295\n[BBOX-1156] 296\n[BBOX-1157] 297\n[BBOX-1158] 298\n[BBOX-1159] 299\n[BBOX-1160] 300\n[BBOX-1161] 301\n[BBOX-1162] 302\n[BBOX-1163] 303\n[BBOX-1164] 304\n[BBOX-1165] 305\n[BBOX-1166] 306\n[BBOX-1167] 307\n[BBOX-1168] 308\n[BBOX-1169] 309\n[BBOX-1170] 310\n[BBOX-1171] 311\n[BBOX-1172] 312\n[BBOX-1173] 313\n[BBOX-1174] 314\n[BBOX-1175] 315\n[BBOX-1176] 316\n[BBOX-1177] 317\n[BBOX-1178] 318\n[BBOX-1179] 319\n[BBOX-1180] 320\n[BBOX-1181] 321\n[BBOX-1182] 322\n[BBOX-1183] 323\n[BBOX-1184] 324\n[BBOX-1185] 325\n[BBOX-1186] 326\n[BBOX-1187] 327\n[BBOX-1188] 328\n[BBOX-1189] 329\n[BBOX-1190] 330\n[BBOX-1191] 331\n[BBOX-1192] 332\n[BBOX-1193] 333\n[BBOX-1194] 334\n[BBOX-1195] 335\n[BBOX-1196] 336\n[BBOX-1197] 337\n[BBOX-1198] 338\n[BBOX-1199] 339\n[BBOX-1200] 340\n[BBOX-1201] 341\n[BBOX-1202] 342\n[BBOX-1203] 343\n[BBOX-1204] 344\n[BBOX-1205] 345\n[BBOX-1206] 346\n[BBOX-1207] 347\n[BBOX-1208] 348\n[BBOX-1209] 349\n[BBOX-1210] 350\n[BBOX-1211] 351\n[BBOX-1212] 352\n[BBOX-1213] 353\n[BBOX-1214] 354\n[BBOX-1215] 355\n[BBOX-1216] 356\n[BBOX-1217] 357\n[BBOX-1218] 358\n[BBOX-1219] 359\n[BBOX-1220] 360\n[BBOX-1221] 361\n[BBOX-1222] 362\n[BBOX-1223] 363\n[BBOX-1224] 364\n[BBOX-1225] 365\n[BBOX-1226] 366\n[BBOX-1227] 367\n[BBOX-1228] 368\n[BBOX-1229] 369\n[BBOX-1230] 370\n[BBOX-1231] 371\n[BBOX-1232] 372\n[BBOX-1233] 373\n[BBOX-1234] 374\n[BBOX-1235] 375\n[BBOX-1236] 376\n[BBOX-1237] 377\n[BBOX-1238] 378\n[BBOX-1239] 379\n[BBOX-1240] 380\n[BBOX-1241] 381\n[BBOX-1242] 382\n[BBOX-1243] 383\n[BBOX-1244] 384\n[BBOX-1245] 385\n[BBOX-1246] 386\n[BBOX-1247] 387\n[BBOX-1248] 388\n[BBOX-1249] 389\n[BBOX-1250] 390\n[BBOX-1251] 391\n[BBOX-1252] 392\n[BBOX-1253] 393\n[BBOX-1254] 394\n[BBOX-1255] 395\n[BBOX-1256] 396\n[BBOX-1257] 397\n[BBOX-1258] 398\n[BBOX-1259] 399\n[BBOX-1260] 400\n[BBOX-1261] 401\n[BBOX-1262] 402\n[BBOX-1263] 403\n[BBOX-1264] 404\n[BBOX-1265] 405\n[BBOX-1266] 406\n[BBOX-1267] 407\n[BBOX-1268] 408\n[BBOX-1269] 409\n[BBOX-1270] 410\n[BBOX-1271] 411\n[BBOX-1272] 412\n[BBOX-1273] 413\n[BBOX-1274] 414\n[BBOX-1275] 415\n[BBOX-1276] 416\n[BBOX-1277] 417\n[BBOX-1278] 418\n[BBOX-1279] 419\n[BBOX-1280] 420\n[BBOX-1281] 421\n[BBOX-1282] 422\n[BBOX-1283] 423\n[BBOX-1284] 424\n[BBOX-1285] 425\n[BBOX-1286] 426\n[BBOX-1287] 427\n[BBOX-1288] 428\n[BBOX-1289] 429\n[BBOX-1290] 430\n[BBOX-1291] 431\n[BBOX-1292] 432\n[BBOX-1293] 433\n[BBOX-1294] 434\n[BBOX-1295] 435\n[BBOX-1296] 436\n[BBOX-1297] 437\n[BBOX-1298] 438\n[BBOX-1299] 439\n[BBOX-1300] 440\n[BBOX-1301] 441\n[BBOX-1302] 442\n[BBOX-1303] 443\n[BBOX-1304] 444\n[BBOX-1305] 445\n[BBOX-1306] 446\n[BBOX-1307] 447\n[BBOX-1308] 448\n[BBOX-1309] 449\n[BBOX-1310] 450\n[BBOX-1311] 451\n[BBOX-1312] 452\n[BBOX-1313] 453\n[BBOX-1314] 454\n[BBOX-1315] 455\n[BBOX-1316] 456\n[BBOX-1317] 457\n[BBOX-1318] 458\n[BBOX-1319] 459\n[BBOX-1320] 460\n[BBOX-1321] 461\n[BBOX-1322] 462\n[BBOX-1323] 463\n[BBOX-1324] 464\n[BBOX-1325] 465\n[BBOX-1326] 466\n[BBOX-1327] 467\n[BBOX-1328] 468\n[BBOX-1329] 469\n[BBOX-1330] 470\n[BBOX-1331] 471\n[BBOX-1332] 472\n[BBOX-1333] 473\n[BBOX-1334] 474\n[BBOX-1335] 475\n[BBOX-1336] 476\n[BBOX-1337] 477\n[BBOX-1338] 478\n[BBOX-1339] 479\n[BBOX-1340] 480\n[BBOX-1341] 481\n[BBOX-1342] 482\n[BBOX-1343] 483\n[BBOX-1344] 484\n[BBOX-1345] 485\n[BBOX-1346] 486\n[BBOX-1347] 487\n[BBOX-1348] 488\n[BBOX-1349] 489\n[BBOX-1350] 490\n[BBOX-1351] 491\n[BBOX-1352] 492\n[BBOX-1353] 493\n[BBOX-1354] 494\n[BBOX-1355] 495\n[BBOX-1356] 496\n[BBOX-1357] 497\n[BBOX-1358] 498\n[BBOX-1359] 499\n[BBOX-1360] 500\n[BBOX-1361] 501\n[BBOX-1362] 502\n[BBOX-1363] 503\n[BBOX-1364] 504\n[BBOX-1365] 505\n[BBOX-1366] 506\n[BBOX-1367] 507\n[BBOX-1368] 508\n[BBOX-1369] 509\n[BBOX-1370] 510\n[BBOX-1371] 511\n[BBOX-1372] 512\n[BBOX-1373] 513\n[BBOX-1374] 514\n[BBOX-1375] 515\n[BBOX-1376] 516\n[BBOX-1377] 517\n[BBOX-1378] 518\n[BBOX-1379] 519\n[BBOX-1380] 520\n[BBOX-1381] 521\n[BBOX-1382] 522\n[BBOX-1383] 523\n[BBOX-1384] 524\n[BBOX-1385] 525\n[BBOX-1386] 526\n[BBOX-1387] 527\n[BBOX-1388] 528\n[BBOX-1389] 529\n[BBOX-1390] 530\n[BBOX-1391] 531\n[BBOX-1392] 532\n[BBOX-1393] 533\n[BBOX-1394] 534\n[BBOX-1395] 535\n[BBOX-1396] 536\n[BBOX-1397] 537\n[BBOX-1398] 538\n[BBOX-1399] 539\n[BBOX-1400] 540\n[BBOX-1401] 541\n[BBOX-1402] 542\n[BBOX-1403] 543\n[BBOX-1404] 544\n[BBOX-1405] 545\n[BBOX-1406] 546\n[BBOX-1407] 547\n[BBOX-1408] 548\n[BBOX-1409] 549\n[BBOX-1410] 550\n[BBOX-1411] 551\n[BBOX-1412] 552\n[BBOX-1413] 553\n[BBOX-1414] 554\n[BBOX-1415] 555\n[BBOX-1416] 556\n[BBOX-1417] 557\n[BBOX-1418] 558\n[BBOX-1419] 559\n[BBOX-1420] 560\n[BBOX-1421] 561\n[BBOX-1422] 562\n[BBOX-1423] 563\n[BBOX-1424] 564\n[BBOX-1425] 565\n[BBOX-1426] 566\n[BBOX-1427] 567\n[BBOX-1428] 568\n[BBOX-1429] 569\n[BBOX-1430] 570\n[BBOX-1431] 571\n[BBOX-1432] 572\n[BBOX-1433] 573\n[BBOX-1434] 574\n[BBOX-1435] 575\n[BBOX-1436] 576\n[BBOX-1437] 577\n[BBOX-1438] 578\n[BBOX-1439] 579\n[BBOX-1440] 580\n[BBOX-1441] 581\n[BBOX-1442] 582\n[BBOX-1443] 583\n[BBOX-1444] 584\n[BBOX-1445] 585\n[BBOX-1446] 586\n[BBOX-1447] 587\n[BBOX-1448] 588\n[BBOX-1449] 589\n[BBOX-1450] 590\n[BBOX-1451] 591\n[BBOX-1452] 592\n[BBOX-1453] 593\n[BBOX-1454] 594\n[BBOX-1455] 595\n[BBOX-1456] 596\n[BBOX-1457] 597\n[BBOX-1458] 598\n[BBOX-1459] 599\n[BBOX-1460] 600\n[BBOX-1461] 601\n[BBOX-1462] 602\n[BBOX-1463] 603\n[BBOX-1464] 604\n[BBOX-1465] 605\n[BBOX-1466] 606\n[BBOX-1467] 607\n[BBOX-1468] 608\n[BBOX-1469] 609\n[BBOX-1470] 610\n[BBOX-1471] 611\n[BBOX-1472] 612\n[BBOX-1473] 613\n[BBOX-1474] 614\n[BBOX-1475] 615\n[BBOX-1476] 616\n[BBOX-1477] 617\n[BBOX-1478] 618\n[BBOX-1479] 619\n[BBOX-1480] 620\n[BBOX-1481] 621\n[BBOX-1482] 622\n[BBOX-1483] 623\n[BBOX-1484] 624\n[BBOX-1485] 625\n[BBOX-1486] 626\n[BBOX-1487] 627\n[BBOX-1488] 628\n[BBOX-1489] 629\n[BBOX-1490] 630\n[BBOX-1491] 631\n[BBOX-1492] 632\n[BBOX-1493] 633\n[BBOX-1494] 634\n[BBOX-1495] 635\n[BBOX-1496] 636\n[BBOX-1497] 637\n[BBOX-1498] 638\n[BBOX-1499] 639\n[BBOX-1500] 640\n[BBOX-1501] 641\n[BBOX-1502] 642\n[BBOX-1503] 643\n[BBOX-1504] 644\n[BBOX-1505] 645\n[BBOX-1506] 646\n[BBOX-1507] 647\n[BBOX-1508] 648\n[BBOX-1509] 649\n[BBOX-1510] 650\n[BBOX-1511] 651\n[BBOX-1512] 652\n[BBOX-1513] 653\n[BBOX-1514] 654\n[BBOX-1515] 655\n[BBOX-1516] 656\n[BBOX-1517] 657\n[BBOX-1518] 658\n[BBOX-1519] 659\n[BBOX-1520] 660\n[BBOX-1521] 661\n[BBOX-1522] 662\n[BBOX-1523] 663\n[BBOX-1524] 664\n[BBOX-1525] 665\n[BBOX-1526] 666\n[BBOX-1527] 667\n[BBOX-1528] 668\n[BBOX-1529] 669\n[BBOX-1530] 670\n[BBOX-1531] 671\n[BBOX-1532] 672\n[BBOX-1533] 673\n[BBOX-1534] 674\n[BBOX-1535] 675\n[BBOX-1536] 676\n[BBOX-1537] 677\n[BBOX-1538] 678\n[BBOX-1539] 679\n[BBOX-1540] 680\n[BBOX-1541] 681\n[BBOX-1542] 682\n[BBOX-1543] 683\n[BBOX-1544] 684\n[BBOX-1545] 685\n[BBOX-1546] 686\n[BBOX-1547] 687\n[BBOX-1548] 688\n[BBOX-1549] 689\n[BBOX-1550] 690\n[BBOX-1551] 691\n[BBOX-1552] 692\n[BBOX-1553] 693\n[BBOX-1554] 694\n[BBOX-1555] 695\n[BBOX-1556] 696\n[BBOX-1557] 697\n[BBOX-1558] 698\n[BBOX-1559] 699\n[BBOX-1560] 700\n[BBOX-1561] 701\n[BBOX-1562] 702\n[BBOX-1563] 703\n[BBOX-1564] 704\n[BBOX-1565] 705\n[BBOX-1566] 706\n[BBOX-1567] 707\n[BBOX-1568] 708\n[BBOX-1569] 709\n[BBOX-1570] 710\n[BBOX-1571] 711\n[BBOX-1572] 712\n[BBOX-1573] 713\n[BBOX-1574] 714\n[BBOX-1575] 715\n[BBOX-1576] 716\n[BBOX-1577] 717\n[BBOX-1578] 718\n[BBOX-1579] 719\n[BBOX-1580] 720\n[BBOX-1581] 721\n[BBOX-1582] 722\n[BBOX-1583] 723\n[BBOX-1584] 724\n[BBOX-1585] 725\n[BBOX-1586] 726\n[BBOX-1587] 727\n[BBOX-1588] 728\n[BBOX-1589] 729\n[BBOX-1590] 730\n[BBOX-1591] 731\n[BBOX-1592] 732\n[BBOX-1593] 733\n[BBOX-1594] 734\n[BBOX-1595] 735\n[BBOX-1596] 736\n[BBOX-1597] 737\n[BBOX-1598] 738\n[BBOX-1599] 739\n[BBOX-1600] 740\n[BBOX-1601] 741\n[BBOX-1602] 742\n[BBOX-1603] 743\n[BBOX-1604] 744\n[BBOX-1605] 745\n[BBOX-1606] 746\n[BBOX-1607] 747\n[BBOX-1608] 748\n[BBOX-1609] 749\n[BBOX-1610] 750\n[BBOX-1611] 751\n[BBOX-1612] 752\n[BBOX-1613] 753\n[BBOX-1614] 754\n[BBOX-1615] 755\n[BBOX-1616] 756\n[BBOX-1617] 757\n[BBOX-1618] 758\n[BBOX-1619] 759\n[BBOX-1620] 760\n[BBOX-1621] 761\n[BBOX-1622] 762\n[BBOX-1623] 763\n[BBOX-1624] 764\n[BBOX-1625] 765\n[BBOX-1626] 766\n[BBOX-1627] 767\n[BBOX-1628] 768\n[BBOX-1629] 769\n[BBOX-1630] 770\n[BBOX-1631] 771\n[BBOX-1632] 772\n[BBOX-1633] 773\n[BBOX-1634] 774\n[BBOX-1635] 775\n[BBOX-1636] 776\n[BBOX-1637] 777\n[BBOX-1638] 778\n[BBOX-1639] 779\n[BBOX-1640] 780\n[BBOX-1641] 781\n[BBOX-1642] 782\n[BBOX-1643] 783\n[BBOX-1644] 784\n[BBOX-1645] 785\n[BBOX-1646] 786\n[BBOX-1647] 787\n[BBOX-1648] 788\n[BBOX-1649] 789\n[BBOX-1650] 790\n[BBOX-1651] 791\n[BBOX-1652] 792\n[BBOX-1653] 793\n[BBOX-1654] 794\n[BBOX-1655] 795\n[BBOX-1656] 796\n[BBOX-1657] 797\n[BBOX-1658] 798\n[BBOX-1659] 799\n[BBOX-1660] 800\n[BBOX-1661] 801\n[BBOX-1662] 802\n[BBOX-1663] 803\n[BBOX-1664] 804\n[BBOX-1665] 805\n[BBOX-1666] 806\n[BBOX-1667] 807\n[BBOX-1668] 808\n[BBOX-1669] 809\n[BBOX-1670] 810\n[BBOX-1671] 811\n[BBOX-1672] 812\n[BBOX-1673] 813\n[BBOX-1674] 814\n[BBOX-1675] 815\n[BBOX-1676] 816\n[BBOX-1677] 817\n[BBOX-1678] 818\n[BBOX-1679] 819\n[BBOX-1680] 820\n[BBOX-1681] 821\n[BBOX-1682] 822\n[BBOX-1683] 823\n[BBOX-1684] 824\n[BBOX-1685] 825\n[BBOX-1686] 826\n[BBOX-1687] 827\n[BBOX-1688] 828\n[BBOX-1689] 829\n[BBOX-1690] 830\n[BBOX-1691] 831\n[BBOX-1692] 832\n[BBOX-1693] 833\n[BBOX-1694] 834\n[BBOX-1695] 835\n[BBOX-1696] 836\n[BBOX-1697] 837\n[BBOX-1698] 838\n[BBOX-1699] 839\n[BBOX-1700] 840\n[BBOX-1701] 841\n[BBOX-1702] 842\n[BBOX-1703] 843\n[BBOX-1704] 844\n[BBOX-1705] 845\n[BBOX-1706] 846\n[BBOX-1707] 847\n[BBOX-1708] 848\n[BBOX-1709] 849\n[BBOX-1710] 850\n[BBOX-1711] 851\n[BBOX-1712] 852\n[BBOX-1713] 853\n[BBOX-1714] 854\n[BBOX-1715] 855\n[BBOX-1716] 856\n[BBOX-1717] 857\n[BBOX-1718] 858\n[BBOX-1719] 859\n[BBOX-1720] 860\n[BBOX-1721] 861\n[BBOX-1722] 862\n[BBOX-1723] 863\n[BBOX-1724] 864\n[BBOX-1725] 865\n[BBOX-1726] 866\n[BBOX-1727] 867\n[BBOX-1728] 868\n[BBOX-1729] 869\n[BBOX-1730] 870\n[BBOX-1731] 871\n[BBOX-1732] 872\n[BBOX-1733] 873\n[BBOX-1734] 874\n[BBOX-1735] 875\n[BBOX-1736] 876\n[BBOX-1737] 877\n[BBOX-1738] 878\n[BBOX-1739] 879\n[BBOX-1740] 880\n[BBOX-1741] 881\n[BBOX-1742] 882\n[BBOX-1743] 883\n[BBOX-1744] 884\n[BBOX-1745] 885\n[BBOX-1746] 886\n[BBOX-1747] 887\n[BBOX-1748] 888\n[BBOX-1749] 889\n[BBOX-1750] 890\n[BBOX-1751] 891\n[BBOX-1752] 892\n[BBOX-1753] 893\n[BBOX-1754] 894\n[BBOX-1755] 895\n[BBOX-1756] 896\n[BBOX-1757] 897\n[BBOX-1758] 898\n[BBOX-1759] 899\n[BBOX-1760] 900\n[BBOX-1761] 901\n[BBOX-1762] 902\n[BBOX-1763] 903\n[BBOX-1764] 904\n[BBOX-1765] 905\n[BBOX-1766] 906\n[BBOX-1767] 907\n[BBOX-1768] 908\n[BBOX-1769] 909\n[BBOX-1770] 910\n[BBOX-1771] 911\n[BBOX-1772] 912\n[BBOX-1773] 913\n[BBOX-1774] 914\n[BBOX-1775] 915\n[BBOX-1776] 916\n[BBOX-1777] 917\n[BBOX-1778] 918\n[BBOX-1779] 919\n[BBOX-1780] 920\n[BBOX-1781] 921\n[BBOX-1782] 922\n[BBOX-1783] 923\n[BBOX-1784] 924\n[BBOX-1785] 925\n[BBOX-1786] 926\n[BBOX-1787] 927\n[BBOX-1788] 928\n[BBOX-1789] 929\n[BBOX-1790] 930\n[BBOX-1791] 931\n[BBOX-1792] 932\n[BBOX-1793] 933\n[BBOX-1794] 934\n[BBOX-1795] 935\n[BBOX-1796] 936\n[BBOX-1797] 937\n[BBOX-1798] 938\n[BBOX-1799] 939\n[BBOX-1800] 940\n[BBOX-1801] 941\n[BBOX-1802] 942\n[BBOX-1803] 943\n[BBOX-1804] 944\n[BBOX-1805] 945\n[BBOX-1806] 946\n[BBOX-1807] 947\n[BBOX-1808] 948\n[BBOX-1809] 949\n[BBOX-1810] 950\n[BBOX-1811] 951\n[BBOX-1812] 952\n[BBOX-1813] 953\n[BBOX-1814] 954\n[BBOX-1815] 955\n[BBOX-1816] 956\n[BBOX-1817] 957\n[BBOX-1818] 958\n[BBOX-1819] 959\n[BBOX-1820] 960\n[BBOX-1821] 961\n[BBOX-1822] 962\n[BBOX-1823] 963\n[BBOX-1824] 964\n[BBOX-1825] 965\n[BBOX-1826] 966\n[BBOX-1827] 967\n[BBOX-1828] 968\n[BBOX-1829] 969\n[BBOX-1830] 970\n[BBOX-1831] 971\n[BBOX-1832] 972\n[BBOX-1833] 973\n[BBOX-1834] 974\n[BBOX-1835] 975\n[BBOX-1836] 976\n[BBOX-1837] 977\n[BBOX-1838] 978\n[BBOX-1839] 979\n[BBOX-1840] 980\n[BBOX-1841] 981\n[BBOX-1842] 982\n[BBOX-1843] 983\n[BBOX-1844] 984\n[BBOX-1845] 985\n[BBOX-1846] 986\n[BBOX-1847] 987\n[BBOX-1848] 988\n[BBOX-1849] 989\n[BBOX-1850] 990\n[BBOX-1851] 991\n[BBOX-1852] 992\n[BBOX-1853] 993\n[BBOX-1854] 994\n[BBOX-1855] 995\n[BBOX-1856] 996\n[BBOX-1857] 997\n[BBOX-1858] 998\n[BBOX-1859] 999\n[BBOX-1860] 1000\n[BBOX-1861] 1001\n[BBOX-1862] 1002\n[BBOX-1863] 1003\n[BBOX-1864] 1004\n[BBOX-1865] 1005\n[BBOX-1866] 1006\n[BBOX-1867] 1007\n[BBOX-1868] 1008\n[BBOX-1869] 1009\n[BBOX-1870] 1010\n[BBOX-1871] 1011\n[BBOX-1872] 1012\n[BBOX-1873] 1013\n[BBOX-1874] 1014\n[BBOX-1875] 1015\n[BBOX-1876] 1016\n[BBOX-1877] 1017\n[BBOX-1878] 1018\n[BBOX-1879] 1019\n[BBOX-1880] 1020\n[BBOX-1881] 1021\n[BBOX-1882] 1022\n[BBOX-1883] 1023\n[BBOX-1884] 1024\n[BBOX-1885] 1025\n[BBOX-1886] 1026\n[BBOX-1887] 1027\n[BBOX-1888] 1028\n[BBOX-1889] 1029\n[BBOX-1890] 1030\n[BBOX-1891] 1031\n[BBOX-1892] 1032\n[BBOX-1893] 1033\n[BBOX-1894] 1034\n[BBOX-1895] 1035\n[BBOX-1896] 1036\n[BBOX-1897] 1037\n[BBOX-1898] 1038\n[BBOX-1899] 1039\n[BBOX-1900] 1040\n[BBOX-1901] 1041\n[BBOX-1902] 1042\n[BBOX-1903] 1043\n[BBOX-1904] 1044\n[BBOX-1905] 1045\n[BBOX-1906] 1046\n[BBOX-1907] 1047\n[BBOX-1908] 1048\n[BBOX-1909] 1049\n[BBOX-1910] 1050\n[BBOX-1911] 1051\n[BBOX-1912] 1052\n[BBOX-1913] 1053\n[BBOX-1914] 1054\n[BBOX-1915] 1055\n[BBOX-1916] 1056\n[BBOX-1917] 1057\n[BBOX-1918] 1058\n[BBOX-1919] 1059\n[BBOX-1920] 1060\n[BBOX-1921] 1061\n[BBOX-1922] 1062\n[BBOX-1923] 1063\n[BBOX-1924] 1064\n[BBOX-1925] 1065\n[BBOX-1926] 1066\n[BBOX-1927] 1067\n[BBOX-1928] 1068\n[BBOX-1929] 1069\n[BBOX-1930] 1070\n[BBOX-1931] 1071\n[BBOX-1932] 1072\n[BBOX-1933] 1073\n[BBOX-1934] 1074\n[BBOX-1935] 1075\n[BBOX-1936] 1076\n[BBOX-1937] 1077\n[BBOX-1938] 1078\n[BBOX-1939] 1079\n[BBOX-1940] 1080\n[BBOX-1941] 1081\n[BBOX-1942] 1082\n[BBOX-1943] 1083\n[BBOX-1944] 1084\n[BBOX-1945] 1085\n[BBOX-1946] 1086\n[BBOX-1947] 1087\n[BBOX-1948] 1088\n[BBOX-1949] 1089\n[BBOX-1950] 1090\n[BBOX-1951] 1091\n[BBOX-1952] 1092\n[BBOX-1953] 1093\n[BBOX-1954] 1094\n[BBOX-1955] 1095\n[BBOX-1956] 1096\n[BBOX-1957] 1097\n[BBOX-1958] 1098\n[BBOX-1959] 1099\n[BBOX-1960] 1100\n[BBOX-1961] 1101\n[BBOX-1962] 1102\n[BBOX-1963] 1103\n[BBOX-1964] 1104\n[BBOX-1965] 1105\n[BBOX-1966] 1106\n[BBOX-1967] 1107\n[BBOX-1968] 1108\n[BBOX-1969] 1109\n[BBOX-1970] 1110\n[BBOX-1971] 1111\n[BBOX-1972] 1112\n[BBOX-1973] 1113\n[BBOX-1974] 1114\n[BBOX-1975] 1115\n[BBOX-1976] 1116\n[BBOX-1977] 1117\n[BBOX-1978] 1118\n[BBOX-1979] 1119\n[BBOX-1980] 1120\n[BBOX-1981] 1121\n[BBOX-1982] 1122\n[BBOX-1983] 1123\n[BBOX-1984] 1124\n[BBOX-1985] 1125\n[BBOX-1986] 1126\n[BBOX-1987] 1127\n[BBOX-1988] 1128\n[BBOX-1989] 1129\n[BBOX-1990] 1130\n[BBOX-1991] 1131\n[BBOX-1992] 1132\n[BBOX-1993] 1133\n[BBOX-1994] 1134\n[BBOX-1995] 1135\n[BBOX-1996] 1136\n[BBOX-1997] 1137\n[BBOX-1998] 1138\n[BBOX-1999] 1139\n[BBOX-2000] 1140\n[BBOX-2001] 1141\n[BBOX-2002] 1142\n[BBOX-2003] 1143\n[BBOX-2004] 1144\n[BBOX-2005] 1145\n[BBOX-2006] 1146\n[BBOX-2007] 1147\n[BBOX-2008] 1148\n[BBOX-2009] 1149\n[BBOX-2010] 1150\n[BBOX-2011] 1151\n[BBOX-2012] 1152\n[BBOX-2013] 1153\n[BBOX-2014] 1154\n[BBOX-2015] 1155\n[BBOX-2016] 1156\n[BBOX-2017] 1157\n[BBOX-2018] 1158\n[BBOX-2019] 1159\n[BBOX-2020] 1160\n[BBOX-2021] 1161\n[BBOX-2022] 1162\n[BBOX-2023] 1163\n[BBOX-2024] 1164\n[BBOX-2025] 1165\n[BBOX-2026] 1166\n[BBOX-2027] 1167\n[BBOX-2028] 1168\n[BBOX-2029] 1169\n[BBOX-2030] 1170\n[BBOX-2031] 1171\n[BBOX-2032] 1172\n[BBOX-2033] 1173\n[BBOX-2034] 1174\n[BBOX-2035] 1175\n[BBOX-2036] 1176\n[BBOX-2037] 1177\n[BBOX-2038] 1178\n[BBOX-2039] 1179\n[BBOX-2040] 1180\n[BBOX-2041] 1181\n[BBOX-2042] 1182\n[BBOX-2043] 1183\n[BBOX-2044] 1184\n[BBOX-2045] 1185\n[BBOX-2046] 1186\n[BBOX-2047] 1187\n[BBOX-2048] 1188\n[BBOX-2049] 1189\n[BBOX-2050] 1190\n[BBOX-2051] 1191\n[BBOX-2052] 1192\n[BBOX-2053] 1193\n[BBOX-2054] 1194\n[BBOX-2055] 1195\n[BBOX-2056] 1196\n[BBOX-2057] 1197\n[BBOX-2058] 1198\n[BBOX-2059] 1199\n[BBOX-2060] 1200\n[BBOX-2061] 1201\n[BBOX-2062] 1202\n[BBOX-2063] 1203\n[BBOX-2064] 1204\n[BBOX-2065] 1205\n[BBOX-2066] 1206\n[BBOX-2067] 1207\n[BBOX-2068] 1208\n[BBOX-2069] 1209\n[BBOX-2070] 1210\n[BBOX-2071] 1211\n[BBOX-2072] 1212\n[BBOX-2073] 1213\n[BBOX-2074] 1214\n[BBOX-2075] 1215\n[BBOX-2076] 1216\n[BBOX-2077] 1217\n[BBOX-2078] 1218\n[BBOX-2079] 1219\n[BBOX-2080] 1220\n[BBOX-2081] 1221\n[BBOX-2082] 1222\n[BBOX-2083] 1223\n[BBOX-2084] 1224\n[BBOX-2085] 1225\n[BBOX-2086] 1226\n[BBOX-2087] 1227\n[BBOX-2088] 1228\n[BBOX-2089] 1229\n[BBOX-2090] 1230\n[BBOX-2091] 1231\n[BBOX-2092] 1232\n[BBOX-2093] 1233\n[BBOX-2094] 1234\n[BBOX-2095] 1235\n[BBOX-2096] 1236\n[BBOX-2097] 1237\n[BBOX-2098] 1238\n[BBOX-2099] 1239\n[BBOX-2100] 1240\n[BBOX-2101] 1241\n[BBOX-2102] 1242\n[BBOX-2103] 1243\n[BBOX-2104] 1244\n[BBOX-2105] 1245\n[BBOX-2106] 1246\n[BBOX-2107] 1247\n[BBOX-2108] 1248\n[BBOX-2109] 1249\n[BBOX-2110] 1250\n[BBOX-2111] 1251\n[BBOX-2112] 1252\n[BBOX-2113] 1253\n[BBOX-2114] 1254\n[BBOX-2115] 1255\n[BBOX-2116] 1256\n[BBOX-2117] 1257\n[BBOX-2118] 1258\n[BBOX-2119] 1259\n[BBOX-2120] 1260\n[BBOX-2121] 1261\n[BBOX-2122] 1262\n[BBOX-2123] 1263\n[BBOX-2124] 1264\n[BBOX-2125] 1265\n[BBOX-2126] 1266\n[BBOX-2127] 1267\n[BBOX-2128] 1268\n[BBOX-2129] 1269\n[BBOX-2130] 1270\n[BBOX-2131] 1271\n[BBOX-2132] 1272\n[BBOX-2133] 1273\n[BBOX-2134] 1274\n[BBOX-2135] 1275\n[BBOX-2136] 1276\n[BBOX-2137] 1277\n[BBOX-2138] 1278\n[BBOX-2139] 1279\n[BBOX-2140] 1280\n[BBOX-2141] 1281\n[BBOX-2142] 1282\n[BBOX-2143] 1283\n[BBOX-2144] 1284\n[BBOX-2145] 1285\n[BBOX-2146] 1286\n[BBOX-2147] 1287\n[BBOX-2148] 1288\n[BBOX-2149] 1289\n[BBOX-2150] 1290\n[BBOX-2151] 1291\n[BBOX-2152] 1292\n[BBOX-2153] 1293\n[BBOX-2154] 1294\n[BBOX-2155] 1295\n[BBOX-2156] 1296\n[BBOX-2157] 1297\n[BBOX-2158] 1298\n[BBOX-2159] 1299\n[BBOX-2160] 1300\n[BBOX-2161] 1301\n[BBOX-2162] 1302\n[BBOX-2163] 1303\n[BBOX-2164] 1304\n[BBOX-2165] 1305\n[BBOX-2166] 1306\n[BBOX-2167] 1307\n[BBOX-2168] 1308\n[BBOX-2169] 1309\n[BBOX-2170] 1310\n[BBOX-2171] 1311\n[BBOX-2172] 1312\n[BBOX-2173] 1313\n[BBOX-2174] 1314\n[BBOX-2175] 1315\n[BBOX-2176] 1316\n[BBOX-2177] 1317\n[BBOX-2178] 1318\n[BBOX-2179] 1319\n[BBOX-2180] 1320\n[BBOX-2181] 1321\n[BBOX-2182] 1322\n[BBOX-2183] 1323\n[BBOX-2184] 1324\n[BBOX-2185] 1325\n[BBOX-2186] 1326\n[BBOX-2187] 1327\n[BBOX-2188] 1328\n[BBOX-2189] 1329\n[BBOX-2190] 1330\n[BBOX-2191] 1331\n[BBOX-2192] 1332\n[BBOX-2193] 1333\n[BBOX-2194] 1334\n[BBOX-2195] 1335\n[BBOX-2196] 1336\n[BBOX-2197] 1337\n[BBOX-2198] 1338\n[BBOX-2199] 1339\n[BBOX-2200] 1340\n[BBOX-2201] 1341\n[BBOX-2202] 1342\n[BBOX-2203] 1343\n[BBOX-2204] 1344\n[BBOX-2205] 1345\n[BBOX-2206] 1346\n[BBOX-2207] 1347\n[BBOX-2208] 1348\n[BBOX-2209] 1349\n[BBOX-2210] 1350\n[BBOX-2211] 1351\n[BBOX-2212] 1352\n[BBOX-2213] 1353\n[BBOX-2214] 1354\n[BBOX-2215] 1355\n[BBOX-2216] 1356\n[BBOX-2217] 1357\n[BBOX-2218] 1358\n[BBOX-2219] 1359\n[BBOX-2220] 1360\n[BBOX-2221] 1361\n[BBOX-2222] 1362\n[BBOX-2223] 1363\n[BBOX-2224] 1364\n[BBOX-2225] 1365\n[BBOX-2226] 1366\n[BBOX-2227] 1367\n[BBOX-2228] 1368\n[BBOX-2229] 1369\n[BBOX-2230] 1370\n[BBOX-2231] 1371\n[BBOX-2232] 1372\n[BBOX-2233] 1373\n[BBOX-2234] 1374\n[BBOX-2235] 1375\n[BBOX-2236] 1376\n[BBOX-2237] 1377\n[BBOX-2238] 1378\n[BBOX-2239] 1379\n[BBOX-2240] 1380\n[BBOX-2241] 1381\n[BBOX-2242] 1382\n[BBOX-2243] 1383\n[BBOX-2244] 1384\n[BBOX-2245] 1385\n[BBOX-2246] 1386\n[BBOX-2247] 1387\n[BBOX-2248] 1388\n[BBOX-2249] 1389\n[BBOX-2250] 1390\n[BBOX-2251] 1391\n[BBOX-2252] 1392\n[BBOX-2253] 1393\n[BBOX-2254] 1394\n[BBOX-2255] 1395\n[BBOX-2256] 1396\n[BBOX-2257] 1397\n[BBOX-2258] 1398\n[BBOX-2259] 1399\n[BBOX-2260] 1400\n[BBOX-2261] 1401\n[BBOX-2262] 1402\n[BBOX-2263] 1403\n[BBOX-2264] 1404\n[BBOX-2265] 1405\n[BBOX-2266] 1406\n[BBOX-2267] 1407\n[BBOX-2268] 1408\n[BBOX-2269] 1409\n[BBOX-2270] 1410\n[BBOX-2271] 1411\n[BBOX-2272] 1412\n[BBOX-2273] 1413\n[BBOX-2274] 1414\n[BBOX-2275] 1415\n[BBOX-2276] 1416\n[BBOX-2277] 1417\n[BBOX-2278] 1418\n[BBOX-2279] 1419\n[BBOX-2280] 1420\n[BBOX-2281] 1421\n[BBOX-2282] 1422\n[BBOX-2283] 1423\n[BBOX-2284] 1424\n[BBOX-2285] 1425\n[BBOX-2286] 1426\n[BBOX-2287] 1427\n[BBOX-2288] 1428\n[BBOX-2289] 1429\n[BBOX-2290] 1430\n[BBOX-2291] 1431\n[BBOX-2292] 1432\n[BBOX-2293] 1433\n[BBOX-2294] 1434\n[BBOX-2295] 1435\n[BBOX-2296] 1436\n[BBOX-2297] 1437\n[BBOX-2298] 1438\n[BBOX-2299] 1439\n[BBOX-2300] 1440\n[BBOX-2301] 1441\n[BBOX-2302] 1442\n[BBOX-2303] 1443\n[BBOX-2304] 1444\n[BBOX-2305] 1445\n[BBOX-2306] 1446\n[BBOX-2307] 1447\n[BBOX-2308] 1448\n[BBOX-2309] 1449\n[BBOX-2310] 1450\n[BBOX-2311] 1451\n[BBOX-2312] 1452\n[BBOX-2313] 1453\n[BBOX-2314] 1454\n[BBOX-2315] 1455\n[BBOX-2316] 1456\n[BBOX-2317] 1457\n[BBOX-2318] 1458\n[BBOX-2319] 1459\n[BBOX-2320] 1460\n[BBOX-2321] 1461\n[BBOX-2322] 1462\n[BBOX-2323] 1463\n[BBOX-2324] 1464\n[BBOX-2325] 1465\n[BBOX-2326] 1466\n[BBOX-2327] 1467\n[BBOX-2328] 1468\n[BBOX-2329] 1469\n[BBOX-2330] 1470\n[BBOX-2331] 1471\n[BBOX-2332] 1472\n[BBOX-2333] 1473\n[BBOX-2334] 1474\n[BBOX-2335] 1475\n[BBOX-2336] 1476\n[BBOX-2337] 1477\n[BBOX-2338] 1478\n[BBOX-2339] 1479\n[BBOX-2340] 1480\n[BBOX-2341] 1481\n[BBOX-2342] 1482\n[BBOX-2343] 1483\n[BBOX-2344] 1484\n[BBOX-2345] 1485\n[BBOX-2346] 1486\n[BBOX-2347] 1487\n[BBOX-2348] 1488\n[BBOX-2349] 1489\n[BBOX-2350] 1490\n[BBOX-2351] 1491\n[BBOX-2352] 1492\n[BBOX-2353] 1493\n[BBOX-2354] 1494\n[BBOX-2355] 1495\n[BBOX-2356] 1496\n[BBOX-2357] 1497\n[BBOX-2358] 1498\n[BBOX-2359] 1499\n[BBOX-2360] 1500\n[BBOX-2361] 1501\n[BBOX-2362] 1502\n[BBOX-2363] 1503\n[BBOX-2364] 1504\n[BBOX-2365] 1505\n[BBOX-2366] 1506\n[BBOX-2367] 1507\n[BBOX-2368] 1508\n[BBOX-2369] 1509\n[BBOX-2370] 1510\n[BBOX-2371] 1511\n[BBOX-2372] 1512\n[BBOX-2373] 1513\n[BBOX-2374] 1514\n[BBOX-2375] 1515\n[BBOX-2376] 1516\n[BBOX-2377] 1517\n[BBOX-2378] 1518\n[BBOX-2379] 1519\n[BBOX-2380] 1520\n[BBOX-2381] 1521\n[BBOX-2382] 1522\n[BBOX-2383] 1523\n[BBOX-2384] 1524\n[BBOX-2385] 1525\n[BBOX-2386] 1526\n[BBOX-2387] 1527\n[BBOX-2388] 1528\n[BBOX-2389] 1529\n[BBOX-2390] 1530\n[BBOX-2391] 1531\n[BBOX-2392] 1532\n[BBOX-2393] 1533\n[BBOX-2394] 1534\n[BBOX-2395] 1535\n[BBOX-2396] 1536\n[BBOX-2397] 1537\n[BBOX-2398] 1538\n[BBOX-2399] 1539\n[BBOX-2400] 1540\n[BBOX-2401] 1541\n[BBOX-2402] 1542\n[BBOX-2403] 1543\n[BBOX-2404] 1544\n[BBOX-2405] 1545\n[BBOX-2406] 1546\n[BBOX-2407] 1547\n[BBOX-2408] 1548\n[BBOX-2409] 1549\n[BBOX-2410] 1550\n[BBOX-2411] 1551\n[BBOX-2412] 1552\n[BBOX-2413] 1553\n[BBOX-2414] 1554\n[BBOX-2415] 1555\n[BBOX-2416] 1556\n[BBOX-2417] 1557\n[BBOX-2418] 1558\n[BBOX-2419] 1559\n[BBOX-2420] 1560\n[BBOX-2421] 1561\n[BBOX-2422] 1562\n[BBOX-2423] 1563\n[BBOX-2424] 1564\n[BBOX-2425] 1565\n[BBOX-2426] 1566\n[BBOX-2427] 1567\n[BBOX-2428] 1568\n[BBOX-2429] 1569\n[BBOX-2430] 1570\n[BBOX-2431] 1571\n[BBOX-2432] 1572\n[BBOX-2433] 1573\n[BBOX-2434] 1574\n[BBOX-2435] 1575\n[BBOX-2436] 1576\n[BBOX-2437] 1577\n[BBOX-2438] 1578\n[BBOX-2439] 1579\n[BBOX-2440] 1580\n[BBOX-2441] 1581\n[BBOX-2442] 1582\n[BBOX-2443] 1583\n[BBOX-2444] 1584\n[BBOX-2445] 1585\n[BBOX-2446] 1586\n[BBOX-2447] 1587\n[BBOX-2448] 1588\n[BBOX-2449] 1589\n[BBOX-2450] 1590\n[BBOX-2451] 1591\n[BBOX-2452] 1592\n[BBOX-2453] 1593\n[BBOX-2454] 1594\n[BBOX-2455] 1595\n[BBOX-2456] 1596\n[BBOX-2457] 1597\n[BBOX-2458] 1598\n[BBOX-2459] 1599\n[BBOX-2460] 1600\n[BBOX-2461] 1601\n[BBOX-2462] 1602\n[BBOX-2463] 1603\n[BBOX-2464] 1604\n[BBOX-2465] 1605\n[BBOX-2466] 1606\n[BBOX-2467] 1607\n[BBOX-2468] 1608\n[BBOX-2469] 1609\n[BBOX-2470] 1610\n[BBOX-2471] 1611\n[BBOX-2472] 1612\n[BBOX-2473] 1613\n[BBOX-2474] 1614\n[BBOX-2475] 1615\n[BBOX-2476] 1616\n[BBOX-2477] 1617\n[BBOX-2478] 1618\n[BBOX-2479] 1619\n[BBOX-2480] 1620\n[BBOX-2481] 1621\n[BBOX-2482] 1622\n[BBOX-2483] 1623\n[BBOX-2484] 1624\n[BBOX-2485] 1625\n[BBOX-2486] 1626\n[BBOX-2487] 1627\n[BBOX-2488] 1628\n[BBOX-2489] 1629\n[BBOX-2490] 1630\n[BBOX-2491] 1631\n[BBOX-2492] 1632\n[BBOX-2493] 1633\n[BBOX-2494] 1634\n[BBOX-2495] 1635\n[BBOX-2496] 1636\n[BBOX-2497] 1637\n[BBOX-2498] 1638\n[BBOX-2499] 1639\n[BBOX-2500] 1640\n[BBOX-2501] 1641\n[BBOX-2502] 1642\n[BBOX-2503] 1643\n[BBOX-2504] 1644\n[BBOX-2505] 1645\n[BBOX-2506] 1646\n[BBOX-2507] 1647\n[BBOX-2508] 1648\n[BBOX-2509] 1649\n[BBOX-2510] 1650\n[BBOX-2511] 1651\n[BBOX-2512] 1652\n[BBOX-2513] 1653\n[BBOX-2514] 1654\n[BBOX-2515] 1655\n[BBOX-2516] 1656\n[BBOX-2517] 1657\n[BBOX-2518] 1658\n[BBOX-2519] 1659\n[BBOX-2520] 1660\n[BBOX-2521] 1661\n[BBOX-2522] 1662\n[BBOX-2523] 1663\n[BBOX-2524] 1664\n[BBOX-2525] 1665\n[BBOX-2526] 1666\n[BBOX-2527] 1667\n[BBOX-2528] 1668\n[BBOX-2529] 1669\n[BBOX-2530] 1670\n[BBOX-2531] 1671\n[BBOX-2532] 1672\n[BBOX-2533] 1673\n[BBOX-2534] 1674\n[BBOX-2535] 1675\n[BBOX-2536] 1676\n[BBOX-2537] 1677\n[BBOX-2538] 1678\n[BBOX-2539] 1679\n[BBOX-2540] 1680\n[BBOX-2541] 1681\n[BBOX-2542] 1682\n[BBOX-2543] 1683\n[BBOX-2544] 1684\n[BBOX-2545] 1685\n[BBOX-2546] 1686\n[BBOX-2547] 1687\n[BBOX-2548] 1688\n[BBOX-2549] 1689\n[BBOX-2550] 1690\n[BBOX-2551] 1691\n[BBOX-2552] 1692\n[BBOX-2553] 1693\n[BBOX-2554] 1694\n[BBOX-2555] 1695\n[BBOX-2556] 1696\n[BBOX-2557] 1697\n[BBOX-2558] 1698\n[BBOX-2559] 1699\n[BBOX-2560] 1700\n[BBOX-2561] 1701\n[BBOX-2562] 1702\n[BBOX-2563] 1703\n[BBOX-2564] 1704\n[BBOX-2565] 1705\n[BBOX-2566] 1706\n[BBOX-2567] 1707\n[BBOX-2568] 1708\n[BBOX-2569] 1709\n[BBOX-2570] 1710\n[BBOX-2571] 1711\n[BBOX-2572] 1712\n[BBOX-2573] 1713\n[BBOX-2574] 1714\n[BBOX-2575] 1715\n[BBOX-2576] 1716\n[BBOX-2577] 1717\n[BBOX-2578] 1718\n[BBOX-2579] 1719\n[BBOX-2580] 1720\n[BBOX-2581] 1721\n[BBOX-2582] 1722\n[BBOX-2583] 1723\n[BBOX-2584] 1724\n[BBOX-2585] 1725\n[BBOX-2586] 1726\n[BBOX-2587] 1727\n[BBOX-2588] 1728\n[BBOX-2589] 1729\n[BBOX-2590] 1730\n[BBOX-2591] 1731\n[BBOX-2592] 1732\n[BBOX-2593] 1733\n[BBOX-2594] 1734\n[BBOX-2595] 1735\n[BBOX-2596] 1736\n[BBOX-2597] 1737\n[BBOX-2598] 1738\n[BBOX-2599] 1739\n[BBOX-2600] 1740\n[BBOX-2601] 1741\n[BBOX-2602] 1742\n[BBOX-2603] 1743\n[BBOX-2604] 1744\n[BBOX-2605] 1745\n[BBOX-2606] 1746\n[BBOX-2607] 1747\n[BBOX-2608] 1748\n[BBOX-2609] 1749\n[BBOX-2610] 1750\n[BBOX-2611] 1751\n[BBOX-2612] 1752\n[BBOX-2613] 1753\n[BBOX-2614] 1754\n[BBOX-2615] 1755\n[BBOX-2616] 1756\n[BBOX-2617] 1757\n[BBOX-2618] 1758\n[BBOX-2619] 1759\n[BBOX-2620] 1760\n[BBOX-2621] 1761\n[BBOX-2622] 1762\n[BBOX-2623] 1763\n[BBOX-2624] 1764\n[BBOX-2625] 1765\n[BBOX-2626] 1766\n[BBOX-2627] 1767\n[BBOX-2628] 1768\n[BBOX-2629] 1769\n[BBOX-2630] 1770\n[BBOX-2631] 1771\n[BBOX-2632] 1772\n[BBOX-2633] 1773\n[BBOX-2634] 1774\n[BBOX-2635] 1775\n[BBOX-2636] 1776\n[BBOX-2637] 1777\n[BBOX-2638] 1778\n[BBOX-2639] 1779\n[BBOX-2640] 1780\n[BBOX-2641] 1781\n[BBOX-2642] 1782\n[BBOX-2643] 1783\n[BBOX-2644] 1784\n[BBOX-2645] 1785\n[BBOX-2646] 1786\n[BBOX-2647] 1787\n[BBOX-2648] 1788\n[BBOX-2649] 1789\n[BBOX-2650] 1790\n[BBOX-2651] 1791\n[BBOX-2652] 1792\n[BBOX-2653] 1793\n[BBOX-2654] 1794\n[BBOX-2655] 1795\n[BBOX-2656] 1796\n[BBOX-2657] 1797\n[BBOX-2658] 1798\n[BBOX-2659] 1799\n[BBOX-2660] 1800\n[BBOX-2661] 1801\n[BBOX-2662] 1802\n[BBOX-2663] 1803\n[BBOX-2664] 1804\n[BBOX-2665] 1805\n[BBOX-2666] 1806\n[BBOX-2667] 1807\n[BBOX-2668] 1808\n[BBOX-2669] 1809\n[BBOX-2670] 1810\n[BBOX-2671] 1811\n[BBOX-2672] 1812\n[BBOX-2673] 1813\n[BBOX-2674] 1814\n[BBOX-2675] 1815\n[BBOX-2676] 1816\n[BBOX-2677] 1817\n[BBOX-2678] 1818\n[BBOX-2679] 1819\n[BBOX-2680] 1820\n[BBOX-2681] 1821\n[BBOX-2682] 1822\n[BBOX-2683] 1823\n[BBOX-2684] 1824\n[BBOX-2685] 1825\n[BBOX-2686] 1826\n[BBOX-2687] 1827\n[BBOX-2688] 1828\n[BBOX-2689] 1829\n[BBOX-2690] 1830\n[BBOX-2691] 1831\n[BBOX-2692] 1832\n[BBOX-2693] 1833\n[BBOX-2694] 1834\n[BBOX-2695] 1835\n[BBOX-2696] 1836\n[BBOX-2697] 1837\n[BBOX-2698] 1838\n[BBOX-2699] 1839\n[BBOX-2700] 1840\n[BBOX-2701] 1841\n[BBOX-2702] 1842\n[BBOX-2703] 1843\n[BBOX-2704] 1844\n[BBOX-2705] 1845\n[BBOX-2706] 1846\n[BBOX-2707] 1847\n[BBOX-2708] 1848\n[BBOX-2709] 1849\n[BBOX-2710] 1850\n[BBOX-2711] 1851\n[BBOX-2712] 1852\n[BBOX-2713] 1853\n[BBOX-2714] 1854\n[BBOX-2715] 1855\n[BBOX-2716] 1856\n[BBOX-2717] 1857\n[BBOX-2718] 1858\n[BBOX-2719] 1859\n[BBOX-2720] 1860\n[BBOX-2721] 1861\n[BBOX-2722] 1862\n[BBOX-2723] 1863\n[BBOX-2724] 1864\n[BBOX-2725] 1865\n[BBOX-2726] 1866\n[BBOX-2727] 1867\n[BBOX-2728] 1868\n[BBOX-2729] 1869\n[BBOX-2730] 1870\n[BBOX-2731] 1871\n[BBOX-2732] 1872\n[BBOX-2733] 1873\n[BBOX-2734] 1874\n[BBOX-2735] 1875\n[BBOX-2736] 1876\n[BBOX-2737] 1877\n[BBOX-2738] 1878\n[BBOX-2739] 1879\n[BBOX-2740] 1880\n[BBOX-2741] 1881\n[BBOX-2742] 1882\n[BBOX-2743] 1883\n[BBOX-2744] 1884\n[BBOX-2745] 1885\n[BBOX-2746] 1886\n[BBOX-2747] 1887\n[BBOX-2748] 1888\n[BBOX-2749] 1889\n[BBOX-2750] 1890\n[BBOX-2751] 1891\n[BBOX-2752] 1892\n[BBOX-2753] 1893\n[BBOX-2754] 1894\n[BBOX-2755] 1895\n[BBOX-2756] 1896\n[BBOX-2757] 1897\n[BBOX-2758] 1898\n[BBOX-2759] 1899\n[BBOX-2760] 1900\n[BBOX-2761] 1901\n[BBOX-2762] 1902\n[BBOX-2763] 1903\n[BBOX-2764] 1904\n[BBOX-2765] 1905\n[BBOX-2766] 1906\n[BBOX-2767] 1907\n[BBOX-2768] 1908\n[BBOX-2769] 1909\n[BBOX-2770] 1910\n[BBOX-2771] 1911\n[BBOX-2772] 1912\n[BBOX-2773] 1913\n[BBOX-2774] 1914\n[BBOX-2775] 1915\n[BBOX-2776] 1916\n[BBOX-2777] 1917\n[BBOX-2778] 1918\n[BBOX-2779] 1919\n[BBOX-2780] 1920\n[BBOX-2781] 1921\n[BBOX-2782] 1922\n[BBOX-2783] 1923\n[BBOX-2784] 1924\n[BBOX-2785] 1925\n[BBOX-2786] 1926\n[BBOX-2787] 1927\n[BBOX-2788] 1928\n[BBOX-2789] 1929\n[BBOX-2790] 1930\n[BBOX-2791] 1931\n[BBOX-2792] 1932\n[BBOX-2793] 1933\n[BBOX-2794] 1934\n[BBOX-2795] 1935\n[BBOX-2796] 1936\n[BBOX-2797] 1937\n[BBOX-2798] 1938\n[BBOX-2799] 1939\n[BBOX-2800] 1940\n[BBOX-2801] 1941\n[BBOX-2802] 1942\n[BBOX-2803] 1943\n[BBOX-2804] 1944\n[BBOX-2805] 1945\n[BBOX-2806] 1946\n[BBOX-2807] 1947\n[BBOX-2808] 1948\n[BBOX-2809] 1949\n[BBOX-2810] 1950\n[BBOX-2811] 1951\n[BBOX-2812] 1952\n[BBOX-2813] 1953\n[BBOX-2814] 1954\n[BBOX-2815] 1955\n[BBOX-2816] 1956\n[BBOX-2817] 1957\n[BBOX-2818] 1958\n[BBOX-2819] 1959\n[BBOX-2820] 1960\n[BBOX-2821] 1961\n[BBOX-2822] 1962\n[BBOX-2823] 1963\n[BBOX-2824] 1964\n[BBOX-2825] 1965\n[BBOX-2826] 1966\n[BBOX-2827] 1967\n[BBOX-2828] 1968\n[BBOX-2829] 1969\n[BBOX-2830] 1970\n[BBOX-2831] 1971\n[BBOX-2832] 1972\n[BBOX-2833] 1973\n[BBOX-2834] 1974\n[BBOX-2835] 1975\n[BBOX-2836] 1976\n[BBOX-2837] 1977\n[BBOX-2838] 1978\n[BBOX-2839] 1979\n[BBOX-2840] 1980\n[BBOX-2841] 1981\n[BBOX-2842] 1982\n[BBOX-2843] 1983\n[BBOX-2844] 1984\n[BBOX-2845] 1985\n[BBOX-2846] 1986\n[BBOX-2847] 1987\n[BBOX-2848] 1988\n[BBOX-2849] 1989\n[BBOX-2850] 1990\n[BBOX-2851] 1991\n[BBOX-2852] 1992\n[BBOX-2853] 1993\n[BBOX-2854] 1994\n[BBOX-2855] 1995\n[BBOX-2856] 1996\n[BBOX-2857] 1997\n[BBOX-2858] 1998\n[BBOX-2859] 1999\n[BBOX-2860] 2000\n[BBOX-2861] 2001\n[BBOX-2862] 2002\n[BBOX-2863] 2003\n[BBOX-2864] 2004\n[BBOX-2865] 2005\n[BBOX-2866] 2006\n[BBOX-2867] 2007\n[BBOX-2868] 2008\n[BBOX-2869] 2009\n[BBOX-2870] 2010\n[BBOX-2871] 2011\n[BBOX-2872] 2012\n[BBOX-2873] 2013\n[BBOX-2874] 2014\n[BBOX-2875] 2015\n[BBOX-2876] 2016\n[BBOX-2877] 2017\n[BBOX-2878] 2018\n[BBOX-2879] 2019\n[BBOX-2880] 2020\n[BBOX-2881] 2021\n[BBOX-2882] 2022\n[BBOX-2883] 2023\n[BBOX-2884] 2024\n[BBOX-2885] 2025\n[BBOX-2886] 2026\n[BBOX-2887] 2027\n[BBOX-2888] 2028\n[BBOX-2889] 2029\n[BBOX-2890] 2030\n[BBOX-2891] 2031\n[BBOX-2892] 2032\n[BBOX-2893] 2033\n[BBOX-2894] 2034\n[BBOX-2895] 2035\n[BBOX-2896] 2036\n[BBOX-2897] 2037\n[BBOX-2898] 2038\n[BBOX-2899] 2039\n[BBOX-2900] 2040\n[BBOX-2901] 2041\n[BBOX-2902] 2042\n[BBOX-2903] 2043\n[BBOX-2904] 2044\n[BBOX-2905] 2045\n[BBOX-2906] 2046\n[BBOX-2907] 2047\n[BBOX-2908] 2048\n[BBOX-2909] 2049\n[BBOX-2910] 2050\n[BBOX-2911] 2051\n[BBOX-2912] 2052\n[BBOX-2913] 2053\n[BBOX-2914] 2054\n[BBOX-2915] 2055\n[BBOX-2916] 2056\n[BBOX-2917] 2057\n[BBOX-2918] 2058\n[BBOX-2919] 2059\n[BBOX-2920] 2060\n[BBOX-2921] 2061\n[BBOX-2922] 2062\n[BBOX-2923] 2063\n[BBOX-2924] 2064\n[BBOX-2925] 2065\n[BBOX-2926] 2066\n[BBOX-2927] 2067\n[BBOX-2928] 2068\n[BBOX-2929] 2069\n[BBOX-2930] 2070\n[BBOX-2931] 2071\n[BBOX-2932] 2072\n[BBOX-2933] 2073\n[BBOX-2934] 2074\n[BBOX-2935] 2075\n[BBOX-2936] 2076\n[BBOX-2937] 2077\n[BBOX-2938] 2078\n[BBOX-2939] 2079\n[BBOX-2940] 2080\n[BBOX-2941] 2081\n[BBOX-2942] 2082\n[BBOX-2943] 2083\n[BBOX-2944] 2084\n[BBOX-2945] 2085\n[BBOX-2946] 2086\n[BBOX-2947] 2087\n[BBOX-2948] 2088\n[BBOX-2949] 2089\n[BBOX-2950] 2090\n[BBOX-2951] 2091\n[BBOX-2952] 2092\n[BBOX-2953] 2093\n[BBOX-2954] 2094\n[BBOX-2955] 2095\n[BBOX-2956] 2096\n[BBOX-2957] 2097\n[BBOX-2958] 2098\n[BBOX-2959] 2099\n[BBOX-2960] 2100\n[BBOX-2961] 2101\n[BBOX-2962] 2102\n[BBOX-2963] 2103\n[BBOX-2964] 2104\n[BBOX-2965] 2105\n[BBOX-2966] 2106\n[BBOX-2967] 2107\n[BBOX-2968] 2108\n[BBOX-2969] 2109\n[BBOX-2970] 2110\n[BBOX-2971] 2111\n[BBOX-2972] 2112\n[BBOX-2973] 2113\n[BBOX-2974] 2114\n[BBOX-2975] 2115\n[BBOX-2976] 2116\n[BBOX-2977] 2117\n[BBOX-2978] 2118\n[BBOX-2979] 2119\n[BBOX-2980] 2120\n[BBOX-2981] 2121\n[BBOX-2982] 2122\n[BBOX-2983] 2123\n[BBOX-2984] 2124\n[BBOX-2985] 2125\n[BBOX-2986] 2126\n[BBOX-2987] 2127\n[BBOX-2988] 2128\n[BBOX-2989] 2129\n[BBOX-2990] 2130\n[BBOX-2991] 2131\n[BBOX-2992] 2132\n[BBOX-2993] 2133\n[BBOX-2994] 2134\n[BBOX-2995] 2135\n[BBOX-2996] 2136\n[BBOX-2997] 2137\n[BBOX-2998] 2138\n[BBOX-2999] 2139\n[BBOX-3000] 2140\n[BBOX-3001] 2141\n[BBOX-3002] 2142\n[BBOX-3003] 2143\n[BBOX-3004] 2144\n[BBOX-3005] 2145\n[BBOX-3006] 2146\n[BBOX-3007] 2147\n[BBOX-3008] 2148\n[BBOX-3009] 2149\n[BBOX-3010] 2150\n[BBOX-3011] 2151\n[BBOX-3012] 2152\n[BBOX-3013] 2153\n[BBOX-3014] 2154\n[BBOX-3015] 2155\n[BBOX-3016] 2156\n[BBOX-3017] 2157\n[BBOX-3018] 2158\n[BBOX-3019] 2159\n[BBOX-3020] 2160\n[BBOX-3021] 2161\n[BBOX-3022] 2162\n[BBOX-3023] 2163\n[BBOX-3024] 2164\n[BBOX-3025] 2165\n[BBOX-3026] 2166\n[BBOX-3027] 2167\n[BBOX-3028] 2168\n[BBOX-3029] 2169\n[BBOX-3030] 2170\n[BBOX-3031] 2171\n[BBOX-3032] 2172\n[BBOX-3033] 2173\n[BBOX-3034] 2174\n[BBOX-3035] 2175\n[BBOX-3036] 2176\n[BBOX-3037] 2177\n[BBOX-3038] 2178\n[BBOX-3039] 2179\n[BBOX-3040] 2180\n[BBOX-3041] 2181\n[BBOX-3042] 2182\n[BBOX-3043] 2183\n[BBOX-3044] 2184\n[BBOX-3045] 2185\n[BBOX-3046] 2186\n[BBOX-3047] 2187\n[BBOX-3048] 2188\n[BBOX-3049] 2189\n[BBOX-3050] 2190\n[BBOX-3051] 2191\n[BBOX-3052] 2192\n[BBOX-3053] 2193\n[BBOX-3054] 2194\n[BBOX-3055] 2195\n[BBOX-3056] 2196\n[BBOX-3057] 2197\n[BBOX-3058] 2198\n[BBOX-3059] 2199\n[BBOX-3060] 2200\n[BBOX-3061] 2201\n[BBOX-3062] 2202\n[BBOX-3063] 2203\n[BBOX-3064] 2204\n[BBOX-3065] 2205\n[BBOX-3066] 2206\n[BBOX-3067] 2207\n[BBOX-3068] 2208\n[BBOX-3069] 2209\n[BBOX-3070] 2210\n[BBOX-3071] 2211\n[BBOX-3072] 2212\n[BBOX-3073] 2213\n[BBOX-3074] 2214\n[BBOX-3075] 2215\n[BBOX-3076] 2216\n[BBOX-3077] 2217\n[BBOX-3078] 2218\n[BBOX-3079] 2219\n[BBOX-3080] 2220\n[BBOX-3081] 2221\n[BBOX-3082] 2222\n[BBOX-3083] 2223\n[BBOX-3084] 2224\n[BBOX-3085] 2225\n[BBOX-3086] 2226\n[BBOX-3087] 2227\n[BBOX-3088] 2228\n[BBOX-3089] 2229\n[BBOX-3090] 2230\n[BBOX-3091] 2231\n[BBOX-3092] 2232\n[BBOX-3093] 2233\n[BBOX-3094] 2234\n[BBOX-3095] 2235\n[BBOX-3096] 2236\n[BBOX-3097] 2237\n[BBOX-3098] 2238\n[BBOX-3099] 2239\n[BBOX-3100] 2240\n[BBOX-3101] 2241\n[BBOX-3102] 2242\n[BBOX-3103] 2243\n[BBOX-3104] 2244\n[BBOX-3105] 2245\n[BBOX-3106] 2246\n[BBOX-3107] 2247\n[BBOX-3108] 2248\n[BBOX-3109] 2249\n[BBOX-3110] 2250\n[BBOX-3111] 2251\n[BBOX-3112] 2252\n[BBOX-3113] 2253\n[BBOX-3114] 2254\n[BBOX-3115] 2255\n[BBOX-3116] 2256\n[BBOX-3117] 2257\n[BBOX-3118] 2258\n[BBOX-3119] 2259\n[BBOX-3120] 2260\n[BBOX-3121] 2261\n[BBOX-3122] 2262\n[BBOX-3123] 2263\n[BBOX-3124] 2264\n[BBOX-3125] 2265\n[BBOX-3126] 2266\n[BBOX-3127] 2267\n[BBOX-3128] 2268\n[BBOX-3129] 2269\n[BBOX-3130] 2270\n[BBOX-3131] 2271\n[BBOX-3132] 2272\n[BBOX-3133] 2273\n[BBOX-3134] 2274\n[BBOX-3135] 2275\n[BBOX-3136] 2276\n[BBOX-3137] 2277\n[BBOX-3138] 2278\n[BBOX-3139] 2279\n[BBOX-3140] 2280\n[BBOX-3141] 2281\n[BBOX-3142] 2282\n[BBOX-3143] 2283\n[BBOX-3144] 2284\n[BBOX-3145] 2285\n[BBOX-3146] 2286\n[BBOX-3147] 2287\n[BBOX-3148] 2288\n[BBOX-3149] 2289\n[BBOX-3150] 2290\n[BBOX-3151] 2291\n[BBOX-3152] 2292\n[BBOX-3153] 2293\n[BBOX-3154] 2294\n[BBOX-3155] 2295\n[BBOX-3156] 2296\n[BBOX-3157] 2297\n[BBOX-3158] 2298\n[BBOX-3159] 2299\n[BBOX-3160] 2300\n[BBOX-3161] 2301\n[BBOX-3162] 2302\n[BBOX-3163] 2303\n[BBOX-3164] 2304\n[BBOX-3165] 2305\n[BBOX-3166] 2306\n[BBOX-3167] 2307\n[BBOX-3168] 2308\n[BBOX-3169] 2309\n[BBOX-3170] 2310\n[BBOX-3171] 2311\n[BBOX-3172] 2312\n[BBOX-3173] 2313\n[BBOX-3174] 2314\n[BBOX-3175] 2315\n[BBOX-3176] 2316\n[BBOX-3177] 2317\n[BBOX-3178] 2318\n[BBOX-3179] 2319\n[BBOX-3180] 2320\n[BBOX-3181] 2321\n[BBOX-3182] 2322\n[BBOX-3183] 2323\n[BBOX-3184] 2324\n[BBOX-3185] 2325\n[BBOX-3186] 2326\n[BBOX-3187] 2327\n[BBOX-3188] 2328\n[BBOX-3189] 2329\n[BBOX-3190] 2330\n[BBOX-3191] 2331\n[BBOX-3192] 2332\n[BBOX-3193] 2333\n[BBOX-3194] 2334\n[BBOX-3195] 2335\n[BBOX-3196] 2336\n[BBOX-3197] 2337\n[BBOX-3198] 2338\n[BBOX-3199] 2339\n[BBOX-3200] 2340\n[BBOX-3201] 2341\n[BBOX-3202] 2342\n[BBOX-3203] 2343\n[BBOX-3204] 2344\n[BBOX-3205] 2345\n[BBOX-3206] 2346\n[BBOX-3207] 2347\n[BBOX-3208] 2348\n[BBOX-3209] 2349\n[BBOX-3210] 2350\n[BBOX-3211] 2351\n[BBOX-3212] 2352\n[BBOX-3213] 2353\n[BBOX-3214] 2354\n[BBOX-3215] 2355\n[BBOX-3216] 2356\n[BBOX-3217] 2357\n[BBOX-3218] 2358\n[BBOX-3219] 2359\n[BBOX-3220] 2360\n[BBOX-3221] 2361\n[BBOX-3222] 2362\n[BBOX-3223] 2363\n[BBOX-3224] 2364\n[BBOX-3225] 2365\n[BBOX-3226] 2366\n[BBOX-3227] 2367\n[BBOX-3228] 2368\n[BBOX-3229] 2369\n[BBOX-3230] 2370\n[BBOX-3231] 2371\n[BBOX-3232] 2372\n[BBOX-3233] 2373\n[BBOX-3234] 2374\n[BBOX-3235] 2375\n[BBOX-3236] 2376\n[BBOX-3237] 2377\n[BBOX-3238] 2378\n[BBOX-3239] 2379\n[BBOX-3240] 2380\n[BBOX-3241] 2381\n[BBOX-3242] 2382\n[BBOX-3243] 2383\n[BBOX-3244] 2384\n[BBOX-3245] 2385\n[BBOX-3246] 2386\n[BBOX-3247] 2387\n[BBOX-3248] 2388\n[BBOX-3249] 2389\n[BBOX-3250] 2390\n[BBOX-3251] 2391\n[BBOX-3252] 2392\n[BBOX-3253] 2393\n[BBOX-3254] 2394\n[BBOX-3255] 2395\n[BBOX-3256] 2396\n[BBOX-3257] 2397\n[BBOX-3258] 2398\n[BBOX-3259] 2399\n[BBOX-3260] 2400\n[BBOX-3261] 2401\n[BBOX-3262] 2402\n[BBOX-3263] 2403\n[BBOX-3264] 2404\n[BBOX-3265] 2405\n[BBOX-3266] 2406\n[BBOX-3267] 2407\n[BBOX-3268] 2408\n[BBOX-3269] 2409\n[BBOX-3270] 2410\n[BBOX-3271] 2411\n[BBOX-3272] 2412\n[BBOX-3273] 2413\n[BBOX-3274] 2414\n[BBOX-3275] 2415\n[BBOX-3276] 2416\n[BBOX-3277] 2417\n[BBOX-3278] 2418\n[BBOX-3279] 2419\n[BBOX-3280] 2420\n[BBOX-3281] 2421\n[BBOX-3282] 2422\n[BBOX-3283] 2423\n[BBOX-3284] 2424\n[BBOX-3285] 2425\n[BBOX-3286] 2426\n[BBOX-3287] 2427\n[BBOX-3288] 2428\n[BBOX-3289] 2429\n[BBOX-3290] 2430\n[BBOX-3291] 2431\n[BBOX-3292] 2432\n[BBOX-3293] 2433\n[BBOX-3294] 2434\n[BBOX-3295] 2435\n[BBOX-3296] 2436\n[BBOX-3297] 2437\n[BBOX-3298] 2438\n[BBOX-3299] 2439\n[BBOX-3300] 2440\n[BBOX-3301] 2441\n[BBOX-3302] 2442\n[BBOX-3303] 2443\n[BBOX-3304] 2444\n[BBOX-3305] 2445\n[BBOX-3306] 2446\n[BBOX-3307] 2447\n[BBOX-3308] 2448\n[BBOX-3309] 2449\n[BBOX-3310] 2450\n[BBOX-3311] 2451\n[BBOX-3312] 2452\n[BBOX-3313] 2453\n[BBOX-3314] 2454\n[BBOX-3315] 2455\n[BBOX-3316] 2456\n[BBOX-3317] 2457\n[BBOX-3318] 2458\n[BBOX-3319] 2459\n[BBOX-3320] 2460\n[BBOX-3321] 2461\n[BBOX-3322] 2462\n[BBOX-3323] 2463\n[BBOX-3324] 2464\n[BBOX-3325] 2465\n[BBOX-3326] 2466\n[BBOX-3327] 2467\n[BBOX-3328] 2468\n[BBOX-3329] 2469\n[BBOX-3330] 2470\n[BBOX-3331] 2471\n[BBOX-3332] 2472\n[BBOX-3333] 2473\n[BBOX-3334] 2474\n[BBOX-3335] 2475\n[BBOX-3336] 2476\n[BBOX-3337] 2477\n[BBOX-3338] 2478\n[BBOX-3339] 2479\n[BBOX-3340] 2480\n[BBOX-3341] 2481\n[BBOX-3342] 2482\n[BBOX-3343] 2483\n[BBOX-3344] 2484\n[BBOX-3345] 2485\n[BBOX-3346] 2486\n[BBOX-3347] 2487\n[BBOX-3348] 2488\n[BBOX-3349] 2489\n[BBOX-3350] 2490\n[BBOX-3351] 2491\n[BBOX-3352] 2492\n[BBOX-3353] 2493\n[BBOX-3354] 2494\n[BBOX-3355] 2495\n[BBOX-3356] 2496\n[BBOX-3357] 2497\n[BBOX-3358] 2498\n[BBOX-3359] 2499\n[BBOX-3360] 2500\n[BBOX-3361] 2501\n[BBOX-3362] 2502\n[BBOX-3363] 2503\n[BBOX-3364] 2504\n[BBOX-3365] 2505\n[BBOX-3366] 2506\n[BBOX-3367] 2507\n[BBOX-3368] 2508\n[BBOX-3369] 2509\n[BBOX-3370] 2510\n[BBOX-3371] 2511\n[BBOX-3372] 2512\n[BBOX-3373] 2513\n[BBOX-3374] 2514\n[BBOX-3375] 2515\n[BBOX-3376] 2516\n[BBOX-3377] 2517\n[BBOX-3378] 2518\n[BBOX-3379] 2519\n[BBOX-3380] 2520\n[BBOX-3381] 2521\n[BBOX-3382] 2522\n[BBOX-3383] 2523\n[BBOX-3384] 2524\n[BBOX-3385] 2525\n[BBOX-3386] 2526\n[BBOX-3387] 2527\n[BBOX-3388] 2528\n[BBOX-3389] 2529\n[BBOX-3390] 2530\n[BBOX-3391] 2531\n[BBOX-3392] 2532\n[BBOX-3393] 2533\n[BBOX-3394] 2534\n[BBOX-3395] 2535\n[BBOX-3396] 2536\n[BBOX-3397] 2537\n[BBOX-3398] 2538\n[BBOX-3399] 2539\n[BBOX-3400] 2540\n[BBOX-3401] 2541\n[BBOX-3402] 2542\n[BBOX-3403] 2543\n[BBOX-3404] 2544\n[BBOX-3405] 2545\n[BBOX-3406] 2546\n[BBOX-3407] 2547\n[BBOX-3408] 2548\n[BBOX-3409] 2549\n[BBOX-3410] 2550\n[BBOX-3411] 2551\n[BBOX-3412] 2552\n[BBOX-3413] 2553\n[BBOX-3414] 2554\n[BBOX-3415] 2555\n[BBOX-3416] 2556\n[BBOX-3417] 2557\n[BBOX-3418] 2558\n[BBOX-3419] 2559\n[BBOX-3420] 2560\n[BBOX-3421] 2561\n[BBOX-3422] 2562\n[BBOX-3423] 2563\n[BBOX-3424] 2564\n[BBOX-3425] 2565\n[BBOX-3426] 2566\n[BBOX-3427] 2567\n[BBOX-3428] 2568\n[BBOX-3429] 2569\n[BBOX-3430] 2570\n[BBOX-3431] 2571\n[BBOX-3432] 2572\n[BBOX-3433] 2573\n[BBOX-3434] 2574\n[BBOX-3435] 2575\n[BBOX-3436] 2576\n[BBOX-3437] 2577\n[BBOX-3438] 2578\n[BBOX-3439] 2579\n[BBOX-3440] 2580\n[BBOX-3441] 2581\n[BBOX-3442] 2582\n[BBOX-3443] 2583\n[BBOX-3444] 2584\n[BBOX-3445] 2585\n[BBOX-3446] 2586\n[BBOX-3447] 2587\n[BBOX-3448] 2588\n[BBOX-3449] 2589\n[BBOX-3450] 2590\n[BBOX-3451] 2591\n[BBOX-3452] 2592\n[BBOX-3453] 2593\n[BBOX-3454] 2594\n[BBOX-3455] 2595\n[BBOX-3456] 2596\n[BBOX-3457] 2597\n[BBOX-3458] 2598\n[BBOX-3459] 2599\n[BBOX-3460] 2600\n[BBOX-3461] 2601\n[BBOX-3462] 2602\n[BBOX-3463] 2603\n[BBOX-3464] 2604\n[BBOX-3465] 2605\n[BBOX-3466] 2606\n[BBOX-3467] 2607\n[BBOX-3468] 2608\n[BBOX-3469] 2609\n[BBOX-3470] 2610\n[BBOX-3471] 2611\n[BBOX-3472] 2612\n[BBOX-3473] 2613\n[BBOX-3474] 2614\n[BBOX-3475] 2615\n[BBOX-3476] 2616\n[BBOX-3477] 2617\n[BBOX-3478] 2618\n[BBOX-3479] 2619\n[BBOX-3480] 2620\n[BBOX-3481] 2621\n[BBOX-3482] 2622\n[BBOX-3483] 2623\n[BBOX-3484] 2624\n[BBOX-3485] 2625\n[BBOX-3486] 2626\n[BBOX-3487] 2627\n[BBOX-3488] 2628\n[BBOX-3489] 2629\n[BBOX-3490] 2630\n[BBOX-3491] 2631\n[BBOX-3492] 2632\n[BBOX-3493] 2633\n[BBOX-3494] 2634\n[BBOX-3495] 2635\n[BBOX-3496] 2636\n[BBOX-3497] 2637\n[BBOX-3498] 2638\n[BBOX-3499] 2639\n[BBOX-3500] 2640\n[BBOX-3501] 2641\n[BBOX-3502] 2642\n[BBOX-3503] 2643\n[BBOX-3504] 2644\n[BBOX-3505] 2645\n[BBOX-3506] 2646\n[BBOX-3507] 2647\n[BBOX-3508] 2648\n[BBOX-3509] 2649\n[BBOX-3510] 2650\n[BBOX-3511] 2651\n[BBOX-3512] 2652\n[BBOX-3513] 2653\n[BBOX-3514] 2654\n[BBOX-3515] 2655\n[BBOX-3516] 2656\n[BBOX-3517] 2657\n[BBOX-3518] 2658\n[BBOX-3519] 2659\n[BBOX-3520] 2660\n[BBOX-3521] 2661\n[BBOX-3522] 2662\n[BBOX-3523] 2663\n[BBOX-3524] 2664\n[BBOX-3525] 2665\n[BBOX-3526] 2666\n[BBOX-3527] 2667\n[BBOX-3528] 2668\n[BBOX-3529] 2669\n[BBOX-3530] 2670\n[BBOX-3531] 2671\n[BBOX-3532] 2672\n[BBOX-3533] 2673\n[BBOX-3534] 2674\n[BBOX-3535] 2675\n[BBOX-3536] 2676\n[BBOX-3537] 2677\n[BBOX-3538] 2678\n[BBOX-3539] 2679\n[BBOX-3540] 2680\n[BBOX-3541] 2681\n[BBOX-3542] 2682\n[BBOX-3543] 2683\n[BBOX-3544] 2684\n[BBOX-3545] 2685\n[BBOX-3546] 2686\n[BBOX-3547] 2687\n[BBOX-3548] 2688\n[BBOX-3549] 2689\n[BBOX-3550] 2690\n[BBOX-3551] 2691\n[BBOX-3552] 2692\n[BBOX-3553] 2693\n[BBOX-3554] 2694\n[BBOX-3555] 2695\n[BBOX-3556] 2696\n[BBOX-3557] 2697\n[BBOX-3558] 2698\n[BBOX-3559] 2699\n[BBOX-3560] 2700\n[BBOX-3561] 2701\n[BBOX-3562] 2702\n[BBOX-3563] 2703\n[BBOX-3564] 2704\n[BBOX-3565] 2705\n[BBOX-3566] 2706\n[BBOX-3567] 2707\n[BBOX-3568] 2708\n[BBOX-3569] 2709\n[BBOX-3570] 2710\n[BBOX-3571] 2711\n[BBOX-3572] 2712\n[BBOX-3573] 2713\n[BBOX-3574] 2714\n[BBOX-3575] 2715\n[BBOX-3576] 2716\n[BBOX-3577] 2717\n[BBOX-3578] 2718\n[BBOX-3579] 2719\n[BBOX-3580] 2720\n[BBOX-3581] 2721\n[BBOX-3582] 2722\n[BBOX-3583] 2723\n[BBOX-3584] 2724\n[BBOX-3585] 2725\n[BBOX-3586] 2726\n[BBOX-3587] 2727\n[BBOX-3588] 2728\n[BBOX-3589] 2729\n[BBOX-3590] 2730\n[BBOX-3591] 2731\n[BBOX-3592] 2732\n[BBOX-3593] 2733\n[BBOX-3594] 2734\n[BBOX-3595] 2735\n[BBOX-3596] 2736\n[BBOX-3597] 2737\n[BBOX-3598] 2738\n[BBOX-3599] 2739\n[BBOX-3600] 2740\n[BBOX-3601] 2741\n[BBOX-3602] 2742\n[BBOX-3603] 2743\n[BBOX-3604] 2744\n[BBOX-3605] 2745\n[BBOX-3606] 2746\n[BBOX-3607] 2747\n[BBOX-3608] 2748\n[BBOX-3609] 2749\n[BBOX-3610] 2750\n[BBOX-3611] 2751\n[BBOX-3612] 2752\n[BBOX-3613] 2753\n[BBOX-3614] 2754\n[BBOX-3615] 2755\n[BBOX-3616] 2756\n[BBOX-3617] 2757\n[BBOX-3618] 2758\n[BBOX-3619] 2759\n[BBOX-3620] 2760\n[BBOX-3621] 2761\n[BBOX-3622] 2762\n[BBOX-3623] 2763\n[BBOX-3624] 2764\n[BBOX-3625] 2765\n[BBOX-3626] 2766\n[BBOX-3627] 2767\n[BBOX-3628] 2768\n[BBOX-3629] 2769\n[BBOX-3630] 2770\n[BBOX-3631] 2771\n[BBOX-3632] 2772\n[BBOX-3633] 2773\n[BBOX-3634] 2774\n[BBOX-3635] 2775\n[BBOX-3636] 2776\n[BBOX-3637] 2777\n[BBOX-3638] 2778\n[BBOX-3639] 2779\n[BBOX-3640] 2780\n[BBOX-3641] 2781\n[BBOX-3642] 2782\n[BBOX-3643] 2783\n[BBOX-3644] 2784\n[BBOX-3645] 2785\n[BBOX-3646] 2786\n[BBOX-3647] 2787\n[BBOX-3648] 2788\n[BBOX-3649] 2789\n[BBOX-3650] 2790\n[BBOX-3651] 2791\n[BBOX-3652] 2792\n[BBOX-3653] 2793\n[BBOX-3654] 2794\n[BBOX-3655] 2795\n[BBOX-3656] 2796\n[BBOX-3657] 2797\n[BBOX-3658] 2798\n[BBOX-3659] 2799\n[BBOX-3660] 2800\n[BBOX-3661] 2801\n[BBOX-3662] 2802\n[BBOX-3663] 2803\n[BBOX-3664] 2804\n[BBOX-3665] 2805\n[BBOX-3666] 2806\n[BBOX-3667] 2807\n[BBOX-3668] 2808\n[BBOX-3669] 2809\n[BBOX-3670] 2810\n[BBOX-3671] 2811\n[BBOX-3672] 2812\n[BBOX-3673] 2813\n[BBOX-3674] 2814\n[BBOX-3675] 2815\n[BBOX-3676] 2816\n[BBOX-3677] 2817\n[BBOX-3678] 2818\n[BBOX-3679] 2819\n[BBOX-3680] 2820"
  }
]
2026-08-05 05:09:53,229 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:09:53.227+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 15, "failed": 0, "current": {"4e4700ce908b11f1a3da71efcdd7cc1f": {"id": "4e4700ce908b11f1a3da71efcdd7cc1f", "doc_id": "4e10ceb4908b11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906341337, "task_type": "dataflow", "root_trace_id": "ca345e6640ff4d788f444c3ab712853e", "root_traceparent": "00-ca345e6640ff4d788f444c3ab712853e-8ea193cced1ce3aa-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:10:14,550 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:10:14,580 INFO     29 [SmartSplitter] SmartSplitter done: 13 chunks from 13 LLM segments (all bbox_id). Types: {'OutpatientRecord': 3, 'PrescriptionRecord': 7, 'ExaminationReport': 3}
2026-08-05 05:10:14,588 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-05 05:10:14,589 INFO     29 [Trace] task=4e4700ce | doc=LZK 哮喘 广三(1).pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "3681 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "chunks", "chunks": "13 items, types={'OutpatientRecord': 3, 'PrescriptionRecord': 7, 'ExaminationReport': 3}"}
2026-08-05 05:10:14,589 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-05 05:10:14,593 INFO     29 [ChunkRouter] Routed 13 chunks into 3 groups: {'chunks_Clinical': 3, 'chunks_Prescription': 7, 'chunks_Examination': 3}
2026-08-05 05:10:14,600 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-05 05:10:14,601 INFO     29 [Trace] task=4e4700ce | doc=LZK 哮喘 广三(1).pdf | ChunkRouter:Router | outputs={"html": "", "json": "3681 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "chunks", "chunks": "13 items, types={'OutpatientRecord': 3, 'PrescriptionRecord': 7, 'ExaminationReport': 3}", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-05 05:10:14,601 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-05 05:10:14,605 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:10:14,605 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m05:10:14 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:10:14,606 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:10:15,298 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:10:15,305 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-05 05:10:15,306 INFO     29 [Trace] task=4e4700ce | doc=LZK 哮喘 广三(1).pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "3681 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-05 05:10:15,306 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-05 05:10:15,310 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:10:15,311 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m05:10:15 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:10:15,311 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:10:15,903 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:10:15,908 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-05 05:10:15,908 INFO     29 [Trace] task=4e4700ce | doc=LZK 哮喘 广三(1).pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "3681 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-05 05:10:15,908 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-05 05:10:15,912 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:10:15,912 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 05:10:15,912 INFO     29 [qwen-vl-text] positions(122): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:10:15,912 INFO     29 [qwen-vl-text] page grouping: [0, 1, 2, 3], lines per page: [20, 42, 35, 25]
2026-08-05 05:10:16,111 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:10:16,243 INFO     29 [qwen-vl-text] page=1, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:10:16,427 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:10:16,612 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:10:16,613 INFO     29 [qwen-vl-text] LLM extraction start, text_len=3386
2026-08-05 05:10:16,613 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:10:16,613 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 121, \"encounter_dates\": [\"2025-10-10\", \"2025-10-24\", \"2025-11-17\"], \"department\": \"内科门诊（荔湾）\", \"record_count\": 3}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "病历编号：\n性别：男\n年龄：40岁\n就诊科室：内科门诊（荔湾）\n就诊时间：2025-10-10 14:36:06\n主诉：BAIYUN V8\n现病史：自上次访视至今，询问及查询HIS系统受试者有新增AE，无SAE、哮喘急性发作，有新增合并用药，发生2次医疗相关事件[2025年9月3日因过敏性鼻炎就诊专科门诊、本周曾因上呼吸道感染到社区医院就诊(具体不详，因HIS系统滞后无法收集具体情况及受试者无法回忆起当时情况及用药情况，待收集具体情况后补充详情)]。于2025年8月4日、2025年9月1日收到加重警报邮件，联系受试者后，均判断非哮喘急性发作。\n完成下流操作：\n1、查看受试者电子日志，受试者漏填2025年8月16日，2025年9月4日晚间日志，2025年9月4日、2025年9月25日早间日志；\n2、填写AQLQ+12和ACQ-5问卷，ACQ-5评分：0.8分；\n3、休息10分钟后，测量坐位生命体征：血压113/81mmHg，脉搏87次/分，呼吸频率20次/分，体温36.6℃，测量身高177.5cm，体重90.5kg(BMI=28.7kg/m2)；\n4、14:35体格检查：神志清，体查合作，自主体位，一般外表无异常，皮肤、粘膜无异常，唇甲无发绀，眼睛、耳、鼻、咽喉无异常，口咽部粘膜无异常，颈软，气管居中，甲状腺未及肿大，全身浅表淋巴结未及肿大，颈静脉无怒张，胸廓无畸形，双肺呼吸运动对称，双肺触觉语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及啰音。心前区无隆起，心尖搏动无弥散，心界不大，心率：87次/分，律齐，各瓣膜听诊区未闻及病理性杂音。腹平软，全腹无压痛、反跳痛。肝、脾肋下未及，肝肾区无叩击痛，肠鸣音存，4次/分，脊柱、四肢无畸形，生理征存，未引出病理征，其他系统未见明显异常；\n5、休息至少10分钟后，于14:58行12导联ECG检查；\n6、于15:01采集中心实验室样本(血常规，血生化)并送往中心试验室；\n7、回收试验药物BDAMDI@ASMDI3盒(152968-AH及185936-HK未开封，148729-UA未用60揿，实际使用46揿，发药当天预喷4揿，2025年9月10日前因超过7天未使用试验药物空喷2次共4揿，2025年9月10日后受试者每七天清洗一次后空喷5次共10揿，总计预喷18揿；epro记录使用总共46揿，与实际使用情况一致。\n8、回收epro以及AM3。\n既往史：更新合并用药：\n1、糠酸莫米松鼻喷雾剂2025.4.3-2025.7.25 每鼻 2喷/次 qm 治疗过敏性鼻炎。\nCS 扫描全能王\n3亿人都在用的扫描App\n病历文书\n门诊病历\n25/10/10 14时 门诊病历\n25/10/24 15时 门诊病历（GCP专用）\n25/11/17 10时 门诊病历\n头降使用40瓶，平均每天使用4瓶，2025年9月10日用完4瓶（未使用试验药剂空瓶2次共4\n瓶，2025年9月10日后受试者每七天首先一次后空瓶5次共10瓶，总计使用10瓶（记录使\n用总共46瓶，与实际使用情况一致。\n8、回访ePRO以及MD。\n既往史：更新合并用药：\n1、鼻腔莫米松鼻喷雾剂C025 4 3-2025 7 25 每鼻 2喷/次 qd 治疗过敏性鼻炎。\n2、苯环喹莫铵鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。\n4、氯卓斯汀盐酸卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。\n5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/\n次 治疗过敏性鼻炎。\n6、枯草抗感染治疗（生理性海水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过\n敏性鼻炎\n已预约受试者安全性随访时间。\n过敏史：\n个人史：\n体格检查：\n专科情况：\n辅助检查：\n治疗项目：\n门诊诊断：\n支气管哮喘\n单病种：\n发病时间：\n处\n置：\n1心电图（心电图室做）\n2布地奈德福莫特罗吸入粉雾剂(II)(省采)●①② 2盒2 000.00入用药,一天2次\n30天\n备注：\n病情评估：\n病情分级：\n是否抢救病例：否\n是否抢救成功：\n是否为绿色通道患者：否\n病人去向：\nCS 扫描全能王\n3亿人都在用的扫描App\n就诊卡\n流水号：\n姓名\n龄：40岁\n就诊科\n日：2025-10-24 15:45:39\n主诉：安全性电话随访\n现病史：今日10:27\n固定电话（020-\n（159\n5），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无\n不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对\nV8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试\n者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，\n目前无安全性异常表现。\n合并用药更新：\n1、小柴胡颗粒、（自行购药）2025.10.6-2025.10.8 10g tid 治疗上呼吸道感染\n2、苯环喹溴铵鼻喷雾剂 2025.4.3-至今 每鼻2喷/次 qid 治疗过敏性鼻炎\n3、氮卓斯汀氟替卡松鼻喷雾剂 2025.9.3-至今 每鼻2喷/次 bid 治疗过敏性鼻炎\n4、辛芩颗粒 2024.8.21-2024.8.27 1袋 冲服 tid 治疗过敏性鼻炎\nAE：\n上呼吸道感染 2025年10月5日-2025年10月8日 中度，非SAE，采取药物治疗措施，对试验\n药物采取措施：剂量不变，与试验药物无关，未因该AE退出研究。\n病历更正：\n1、更正2024年10月22日病历，合并用药“辛芩颗粒”为“辛芩颗粒”；\n2、更正2024年10月22日病历，合并用药“苯环喹溴铵鼻喷雾剂”为“苯环喹溴铵鼻喷雾\n剂”；\n3、更正2025年1月24日病历，“无收到ePro触发的哮喘警报邮件”为“有收到ePro触发的哮\n喘警报邮件”；\n4、更正2025年7月18日病历，“受试者漏填2025年4月28日晚间日志” 更正为：“受试者\n漏填2025年4月28日早间日志”；\n5、更正2024年11月6日病历，“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共\n计用了26喷”为：“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了28\n喷”。\n医生\n病历编号：\n姓名：\n性别：\n年龄：40岁\n就诊科：\n就诊时间：2025-11-17 10:10:48\n主诉：支气管哮喘治疗后复查：\n现病史：2021年2月前开始出现咳嗽、咯痰，粘白，量中，能咯出，咳嗽呈阵发性、刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏。无咽痛，无伴反酸、嗳气、腹胀。无上腹部隐痛不适感，无伴发热、畏寒，影响睡眠。晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：\n12.52*109/L 嗜酸粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定。本次门诊距上次门诊间隔时间30天。症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确。急性发作情况：两次，就诊期间急性发作：无，发作次数：0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。近3天来出现咽痛不适\n既往史：鼻炎病史无规则治疗。打鼾明显。\n过敏史：未发现。\n个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。\n体格检查：神志清，颈软，双肺呼吸音粗，未闻及明显干、湿性罗音，口腔粘膜无白斑。\n专科情况：\n辅助检查：\n治疗项目：\n门诊诊断：\n1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、阻塞性睡眠呼吸暂停低通气综合征,4、急性咽炎\n单病种：\n发病时间：\n处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不适随诊。\n1金银花口服液◆⑤ 2盒 20.0ml,口服,一天3次(口服) 6天\n2氨卓斯汀氟替卡松鼻喷雾剂◆ 1瓶 2.0喷,喷鼻,一天2次 30天\n3苯环喹溴铵鼻喷雾剂◆ 3瓶 2.0喷,喷鼻,一天4次 30天\n备注：建议在住地附近社区医疗机构随诊。",
    "role": "user"
  }
]
[92m05:10:16 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:10:16,615 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:10:26,070 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:10:26.070+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 15, "failed": 0, "current": {"4e4700ce908b11f1a3da71efcdd7cc1f": {"id": "4e4700ce908b11f1a3da71efcdd7cc1f", "doc_id": "4e10ceb4908b11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906341337, "task_type": "dataflow", "root_trace_id": "ca345e6640ff4d788f444c3ab712853e", "root_traceparent": "00-ca345e6640ff4d788f444c3ab712853e-8ea193cced1ce3aa-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:10:44,326 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:10:44,327 INFO     29 [qwen-vl-text] LLM output (len=3161):
[
  {
    "encounter_date": "2025-10-10",
    "chief_complaint": "BAIYUN V8",
    "present_illness": "自上次访视至今，询问及查询HIS系统受试者有新增AE，无SAE、哮喘急性发作，有新增合并用药，发生2次医疗相关事件[2025年9月3日因过敏性鼻炎就诊专科门诊、本周曾因上呼吸道感染到社区医院就诊(具体不详，因HIS系统滞后无法收集具体情况及受试者无法回忆起当时情况及用药情况，待收集具体情况后补充详情)]。于2025年8月4日、2025年9月1日收到加重警报邮件，联系受试者后，均判断非哮喘急性发作。完成下流操作：1、查看受试者电子日志，受试者漏填2025年8月16日，2025年9月4日晚间日志，2025年9月4日、2025年9月25日早间日志；2、填写AQLQ+12和ACQ-5问卷，ACQ-5评分：0.8分；3、休息10分钟后，测量坐位生命体征：血压113/81mmHg，脉搏87次/分，呼吸频率20次/分，体温36.6℃，测量身高177.5cm，体重90.5kg(BMI=28.7kg/m2)；4、14:35体格检查：神志清，体查合作，自主体位，一般外表无异常，皮肤、粘膜无异常，唇甲无发绀，眼睛、耳、鼻、咽喉无异常，口咽部粘膜无异常，颈软，气管居中，甲状腺未及肿大，全身浅表淋巴结未及肿大，颈静脉无怒张，胸廓无畸形，双肺呼吸运动对称，双肺触觉语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及啰音。心前区无隆起，心尖搏动无弥散，心界不大，心率：87次/分，律齐，各瓣膜听诊区未闻及病理性杂音。腹平软，全腹无压痛、反跳痛。肝、脾肋下未及，肝肾区无叩击痛，肠鸣音存，4次/分，脊柱、四肢无畸形，生理征存，未引出病理征，其他系统未见明显异常；5、休息至少10分钟后，于14:58行12导联ECG检查；6、于15:01采集中心实验室样本(血常规，血生化)并送往中心试验室；7、回收试验药物BDAMDI@ASMDI3盒(152968-AH及185936-HK未开封，148729-UA未用60揿，实际使用46揿，发药当天预喷4揿，2025年9月10日前因超过7天未使用试验药物空喷2次共4揿，2025年9月10日后受试者每七天清洗一次后空喷5次共10揿，总计预喷18揿；epro记录使用总共46揿，与实际使用情况一致。8、回收epro以及AM3。更新合并用药：1、糠酸莫米松鼻喷雾剂2025.4.3-2025.7.25 每鼻 2喷/次 qm 治疗过敏性鼻炎。2、苯环喹溴铵鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 qid 治疗过敏性鼻炎。4、氮卓斯汀氟替卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/次 治疗过敏性鼻炎。6、枯草抗感染治疗（生理性海水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过敏性鼻炎",
    "past_history": null,
    "diagnosis": "支气管哮喘",
    "treatment_plan": [
      "心电图（心电图室做）",
      "布地奈德福莫特罗吸入粉雾剂(II)(省采) 2盒 2000.00入用药,一天2次 30天"
    ]
  },
  {
    "encounter_date": "2025-10-24",
    "chief_complaint": "安全性电话随访",
    "present_illness": "今日10:27固定电话（020-1595），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对V8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，目前无安全性异常表现。合并用药更新：1、小柴胡颗粒、（自行购药）2025.10.6-2025.10.8 10g tid 治疗上呼吸道感染 2、苯环喹溴铵鼻喷雾剂 2025.4.3-至今 每鼻2喷/次 qid 治疗过敏性鼻炎 3、氮卓斯汀氟替卡松鼻喷雾剂 2025.9.3-至今 每鼻2喷/次 bid 治疗过敏性鼻炎 4、辛芩颗粒 2024.8.21-2024.8.27 1袋 冲服 tid 治疗过敏性鼻炎。AE：上呼吸道感染 2025年10月5日-2025年10月8日 中度，非SAE，采取药物治疗措施，对试验药物采取措施：剂量不变，与试验药物无关，未因该AE退出研究。病历更正：1、更正2024年10月22日病历，合并用药“辛芩颗粒”为“辛芩颗粒”；2、更正2024年10月22日病历，合并用药“苯环喹溴铵鼻喷雾剂”为“苯环喹溴铵鼻喷雾剂”；3、更正2025年1月24日病历，“无收到ePro触发的哮喘警报邮件”为“有收到ePro触发的哮喘警报邮件”；4、更正2025年7月18日病历，“受试者漏填2025年4月28日晚间日志” 更正为：“受试者漏填2025年4月28日早间日志”；5、更正2024年11月6日病历，“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了26喷”为：“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了28喷”。",
    "past_history": null,
    "diagnosis": null,
    "treatment_plan": null
  },
  {
    "encounter_date": "2025-11-17",
    "chief_complaint": "支气管哮喘治疗后复查",
    "present_illness": "2021年2月前开始出现咳嗽、咯痰，粘白，量中，能咯出，咳嗽呈阵发性、刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏。无咽痛，无伴反酸、嗳气、腹胀。无上腹部隐痛不适感，无伴发热、畏寒，影响睡眠。晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定。本次门诊距上次门诊间隔时间30天。症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确。急性发作情况：两次，就诊期间急性发作：无，发作次数：0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。近3天来出现咽痛不适",
    "past_history": "鼻炎病史无规则治疗。打鼾明显。过敏史：未发现。个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。",
    "diagnosis": "1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、阻塞性睡眠呼吸暂停低通气综合征,4、急性咽炎",
    "treatment_plan": [
      "金银花口服液 2盒 20.0ml,口服,一天3次(口服) 6天",
      "氨卓斯汀氟替卡松鼻喷雾剂 1瓶 2.0喷,喷鼻,一天2次 30天",
      "苯环喹溴铵鼻喷雾剂 3瓶 2.0喷,喷鼻,一天4次 30天"
    ]
  }
]
2026-08-05 05:10:44,327 WARNING  29 [qwen-vl-text] extracted_data is list, treat as empty
2026-08-05 05:10:44,328 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1320554, prompt_len=1760
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共20行）
["病历编号：", "性别：男", "年龄：40岁", "就诊科室：内科门诊（荔湾）", "就诊时间：2025-10-10 14:36:06", "主诉：BAIYUN V8", "现病史：自上次访视至今，询问及查询HIS系统受试者有新增AE，无SAE、哮喘急性发作，有新增合并用药，发生2次医疗相关事件[2025年9月3日因过敏性鼻炎就诊专科门诊、本周曾因上呼吸道感染到社区医院就诊(具体不详，因HIS系统滞后无法收集具体情况及受试者无法回忆起当时情况及用药情况，待收集具体情况后补充详情)]。于2025年8月4日、2025年9月1日收到加重警报邮件，联系受试者后，均判断非哮喘急性发作。", "完成下流操作：", "1、查看受试者电子日志，受试者漏填2025年8月16日，2025年9月4日晚间日志，2025年9月4日、2025年9月25日早间日志；", "2、填写AQLQ+12和ACQ-5问卷，ACQ-5评分：0.8分；", "3、休息10分钟后，测量坐位生命体征：血压113/81mmHg，脉搏87次/分，呼吸频率20次/分，体温36.6℃，测量身高177.5cm，体重90.5kg(BMI=28.7kg/m2)；", "4、14:35体格检查：神志清，体查合作，自主体位，一般外表无异常，皮肤、粘膜无异常，唇甲无发绀，眼睛、耳、鼻、咽喉无异常，口咽部粘膜无异常，颈软，气管居中，甲状腺未及肿大，全身浅表淋巴结未及肿大，颈静脉无怒张，胸廓无畸形，双肺呼吸运动对称，双肺触觉语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及啰音。心前区无隆起，心尖搏动无弥散，心界不大，心率：87次/分，律齐，各瓣膜听诊区未闻及病理性杂音。腹平软，全腹无压痛、反跳痛。肝、脾肋下未及，肝肾区无叩击痛，肠鸣音存，4次/分，脊柱、四肢无畸形，生理征存，未引出病理征，其他系统未见明显异常；", "5、休息至少10分钟后，于14:58行12导联ECG检查；", "6、于15:01采集中心实验室样本(血常规，血生化)并送往中心试验室；", "7、回收试验药物BDAMDI@ASMDI3盒(152968-AH及185936-HK未开封，148729-UA未用60揿，实际使用46揿，发药当天预喷4揿，2025年9月10日前因超过7天未使用试验药物空喷2次共4揿，2025年9月10日后受试者每七天清洗一次后空喷5次共10揿，总计预喷18揿；epro记录使用总共46揿，与实际使用情况一致。", "8、回收epro以及AM3。", "既往史：更新合并用药：", "1、糠酸莫米松鼻喷雾剂2025.4.3-2025.7.25 每鼻 2喷/次 qm 治疗过敏性鼻炎。", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-05 05:10:55,292 INFO     29 [qwen-vl-text] coord API raw response (len=1970):
[
	{"text": "病历编号：", "bbox": [541, 117, 617, 134]},
	{"text": "性别：男", "bbox": [438, 150, 501, 167]},
	{"text": "年龄：40岁", "bbox": [626, 151, 690, 167]},
	{"text": "就诊科室：内科门诊（荔湾）", "bbox": [162, 182, 372, 199]},
	{"text": "就诊时间：2025-10-10 14:36:06", "bbox": [541, 183, 795, 198]},
	{"text": "主诉：BAIYUN V8", "bbox": [160, 215, 400, 231]},
	{"text": "现病史：自上次访视至今，询问及查询HIS系统受试者有新增AE，无SAE、哮喘急性发作，有新增合并用药，发生2次医疗相关事件[2025年9月3日因过敏性鼻炎就诊专科门诊、本周曾因上呼吸道感染到社区医院就诊(具体不详，因HIS系统滞后无法收集具体情况及受试者无法回忆起当时情况及用药情况，待收集具体情况后补充详情)]。于2025年8月4日、2025年9月1日收到加重警报邮件，联系受试者后，均判断非哮喘急性发作。", "bbox": [160, 246, 855, 345]},
	{"text": "完成下流操作：", "bbox": [160, 360, 275, 375]},
	{"text": "1、查看受试者电子日志，受试者漏填2025年8月16日，2025年9月4日晚间日志，2025年9月4日、2025年9月25日早间日志；", "bbox": [160, 390, 851, 425]},
	{"text": "2、填写AQLQ+12和ACQ-5问卷，ACQ-5评分：0.8分；", "bbox": [160, 439, 539, 455]},
	{"text": "3、休息10分钟后，测量坐位生命体征：血压113/81mmHg，脉搏87次/分，呼吸频率20次/分，体温36.6℃，测量身高177.5cm，体重90.5kg(BMI=28.7kg/m2)；", "bbox": [160, 469, 822, 505]},
	{"text": "4、14:35体格检查：神志清，体查合作，自主体位，一般外表无异常，皮肤、粘膜无异常，唇甲无发绀，眼睛、耳、鼻、咽喉无异常，口咽部粘膜无异常，颈软，气管居中，甲状腺未及肿大，全身浅表淋巴结未及肿大，颈静脉无怒张，胸廓无畸形，双肺呼吸运动对称，双肺触觉语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及啰音。心前区无隆起，心尖搏动无弥散，心界不大，心率：87次/分，律齐，各瓣膜听诊区未闻及病理性杂音。腹平软，全腹无压痛、反跳痛。肝、脾肋下未及，肝肾区无叩击痛，肠鸣音存，4次/分，脊柱、四肢无畸形，生理征存，未引出病理征，其他系统未见明显异常；", "bbox": [160, 520, 842, 658]},
	{"text": "5、休息至少10分钟后，于14:58行12导联ECG检查；", "bbox": [160, 673, 532, 689]},
	{"text": "6、于15:01采集中心实验室样本(血常规，血生化)并送往中心试验室；", "bbox": [160, 703, 672, 719]},
	{"text": "7、回收试验药物BDAMDI@ASMDI3盒(152968-AH及185936-HK未开封，148729-UA未用60揿，实际使用46揿，发药当天预喷4揿，2025年9月10日前因超过7天未使用试验药物空喷2次共4揿，2025年9月10日后受试者每七天清洗一次后空喷5次共10揿，总计预喷18揿；epro记录使用总共46揿，与实际使用情况一致。", "bbox": [160, 733, 822, 809]},
	{"text": "8、回收epro以及AM3。", "bbox": [160, 824, 325, 840]},
	{"text": "既往史：更新合并用药：", "bbox": [160, 855, 379, 871]},
	{"text": "1、糠酸莫米松鼻喷雾剂2025.4.3-2025.7.25 每鼻 2喷/次 qm 治疗过敏性鼻炎。", "bbox": [160, 884, 767, 899]},
	{"text": "CS 扫描全能王", "bbox": [862, 958, 977, 974]},
	{"text": "3亿人都在用的扫描App", "bbox": [862, 977, 977, 987]}
]
2026-08-05 05:10:55,293 INFO     29 [qwen-vl-text] coord API: raw_items=20, valid_items=20, elapsed=11.0s
2026-08-05 05:10:55,293 INFO     29 [qwen-vl-text] coord item[0]: text=病历编号：, bbox=[541, 117, 617, 134]
2026-08-05 05:10:55,293 INFO     29 [qwen-vl-text] coord item[1]: text=性别：男, bbox=[438, 150, 501, 167]
2026-08-05 05:10:55,293 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：40岁, bbox=[626, 151, 690, 167]
2026-08-05 05:10:55,293 INFO     29 [qwen-vl-text] coord item[3]: text=就诊科室：内科门诊（荔湾）, bbox=[162, 182, 372, 199]
2026-08-05 05:10:55,293 INFO     29 [qwen-vl-text] coord item[4]: text=就诊时间：2025-10-10 14:36:06, bbox=[541, 183, 795, 198]
2026-08-05 05:10:55,294 INFO     29 [qwen-vl-text] coord item[5]: text=主诉：BAIYUN V8, bbox=[160, 215, 400, 231]
2026-08-05 05:10:55,294 INFO     29 [qwen-vl-text] coord item[6]: text=现病史：自上次访视至今，询问及查询HIS系统受试者有新增AE，无SAE、哮喘急性发作，有新增合并用药，发生2次医疗相关事件[2025年9月3日因过敏性鼻炎就诊专科门诊、本周曾因上呼吸道感染到社区医院就诊(具体不详，因HIS系统滞后无法收集具体情况及受试者无法回忆起当时情况及用药情况，待收集具体情况后补充详情)]。于2025年8月4日、2025年9月1日收到加重警报邮件，联系受试者后，均判断非哮喘急性发作。, bbox=[160, 246, 855, 345]
2026-08-05 05:10:55,294 INFO     29 [qwen-vl-text] coord item[7]: text=完成下流操作：, bbox=[160, 360, 275, 375]
2026-08-05 05:10:55,294 INFO     29 [qwen-vl-text] coord item[8]: text=1、查看受试者电子日志，受试者漏填2025年8月16日，2025年9月4日晚间日志，2025年9月4日、2025年9月25日早间日志；, bbox=[160, 390, 851, 425]
2026-08-05 05:10:55,294 INFO     29 [qwen-vl-text] coord item[9]: text=2、填写AQLQ+12和ACQ-5问卷，ACQ-5评分：0.8分；, bbox=[160, 439, 539, 455]
2026-08-05 05:10:55,294 INFO     29 [qwen-vl-text] coord item[10]: text=3、休息10分钟后，测量坐位生命体征：血压113/81mmHg，脉搏87次/分，呼吸频率20次/分，体温36.6℃，测量身高177.5cm，体重90.5kg(BMI=28.7kg/m2)；, bbox=[160, 469, 822, 505]
2026-08-05 05:10:55,294 INFO     29 [qwen-vl-text] coord item[11]: text=4、14:35体格检查：神志清，体查合作，自主体位，一般外表无异常，皮肤、粘膜无异常，唇甲无发绀，眼睛、耳、鼻、咽喉无异常，口咽部粘膜无异常，颈软，气管居中，甲状腺未及肿大，全身浅表淋巴结未及肿大，颈静脉无怒张，胸廓无畸形，双肺呼吸运动对称，双肺触觉语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及啰音。心前区无隆起，心尖搏动无弥散，心界不大，心率：87次/分，律齐，各瓣膜听诊区未闻及病理性杂音。腹平软，全腹无压痛、反跳痛。肝、脾肋下未及，肝肾区无叩击痛，肠鸣音存，4次/分，脊柱、四肢无畸形，生理征存，未引出病理征，其他系统未见明显异常；, bbox=[160, 520, 842, 658]
2026-08-05 05:10:55,294 INFO     29 [qwen-vl-text] coord item[12]: text=5、休息至少10分钟后，于14:58行12导联ECG检查；, bbox=[160, 673, 532, 689]
2026-08-05 05:10:55,294 INFO     29 [qwen-vl-text] coord item[13]: text=6、于15:01采集中心实验室样本(血常规，血生化)并送往中心试验室；, bbox=[160, 703, 672, 719]
2026-08-05 05:10:55,294 INFO     29 [qwen-vl-text] coord item[14]: text=7、回收试验药物BDAMDI@ASMDI3盒(152968-AH及185936-HK未开封，148729-UA未用60揿，实际使用46揿，发药当天预喷4揿，2025年9月10日前因超过7天未使用试验药物空喷2次共4揿，2025年9月10日后受试者每七天清洗一次后空喷5次共10揿，总计预喷18揿；epro记录使用总共46揿，与实际使用情况一致。, bbox=[160, 733, 822, 809]
2026-08-05 05:10:55,294 INFO     29 [qwen-vl-text] coord item[15]: text=8、回收epro以及AM3。, bbox=[160, 824, 325, 840]
2026-08-05 05:10:55,294 INFO     29 [qwen-vl-text] coord item[16]: text=既往史：更新合并用药：, bbox=[160, 855, 379, 871]
2026-08-05 05:10:55,294 INFO     29 [qwen-vl-text] coord item[17]: text=1、糠酸莫米松鼻喷雾剂2025.4.3-2025.7.25 每鼻 2喷/次 qm 治疗过敏性鼻炎。, bbox=[160, 884, 767, 899]
2026-08-05 05:10:55,294 INFO     29 [qwen-vl-text] coord item[18]: text=CS 扫描全能王, bbox=[862, 958, 977, 974]
2026-08-05 05:10:55,294 INFO     29 [qwen-vl-text] coord item[19]: text=3亿人都在用的扫描App, bbox=[862, 977, 977, 987]
2026-08-05 05:10:55,295 INFO     29 [qwen-vl-text] page=0 — 20/20 coords, api_time=11.0s
2026-08-05 05:10:55,297 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=708232, prompt_len=1415
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共42行）
["病历文书", "门诊病历", "25/10/10 14时 门诊病历", "25/10/24 15时 门诊病历（GCP专用）", "25/11/17 10时 门诊病历", "头降使用40瓶，平均每天使用4瓶，2025年9月10日用完4瓶（未使用试验药剂空瓶2次共4", "瓶，2025年9月10日后受试者每七天首先一次后空瓶5次共10瓶，总计使用10瓶（记录使", "用总共46瓶，与实际使用情况一致。", "8、回访ePRO以及MD。", "既往史：更新合并用药：", "1、鼻腔莫米松鼻喷雾剂C025 4 3-2025 7 25 每鼻 2喷/次 qd 治疗过敏性鼻炎。", "2、苯环喹莫铵鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。", "4、氯卓斯汀盐酸卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。", "5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/", "次 治疗过敏性鼻炎。", "6、枯草抗感染治疗（生理性海水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过", "敏性鼻炎", "已预约受试者安全性随访时间。", "过敏史：", "个人史：", "体格检查：", "专科情况：", "辅助检查：", "治疗项目：", "门诊诊断：", "支气管哮喘", "单病种：", "发病时间：", "处", "置：", "1心电图（心电图室做）", "2布地奈德福莫特罗吸入粉雾剂(II)(省采)●①② 2盒2 000.00入用药,一天2次", "30天", "备注：", "病情评估：", "病情分级：", "是否抢救病例：否", "是否抢救成功：", "是否为绿色通道患者：否", "病人去向：", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-05 05:11:11,393 INFO     29 [qwen-vl-text] coord API raw response (len=2514):
[
	{"text": "病历文书", "bbox": [18, 35, 58, 49]},
	{"text": "门诊病历", "bbox": [18, 93, 64, 110]},
	{"text": "25/10/10 14时 门诊病历", "bbox": [18, 139, 127, 154]},
	{"text": "25/10/24 15时 门诊病历（GCP专用）", "bbox": [18, 188, 180, 203]},
	{"text": "25/11/17 10时 门诊病历", "bbox": [18, 237, 127, 252]},
	{"text": "头降使用40瓶，平均每天使用4瓶，2025年9月10日用完4瓶（未使用试验药剂空瓶2次共4", "bbox": [630, 73, 943, 86]},
	{"text": "瓶，2025年9月10日后受试者每七天首先一次后空瓶5次共10瓶，总计使用10瓶（记录使", "bbox": [630, 90, 947, 104]},
	{"text": "用总共46瓶，与实际使用情况一致。", "bbox": [630, 109, 754, 122]},
	{"text": "8、回访ePRO以及MD。", "bbox": [630, 138, 707, 151]},
	{"text": "既往史：更新合并用药：", "bbox": [630, 168, 733, 181]},
	{"text": "1、鼻腔莫米松鼻喷雾剂C025 4 3-2025 7 25 每鼻 2喷/次 qd 治疗过敏性鼻炎。", "bbox": [630, 196, 926, 210]},
	{"text": "2、苯环喹莫铵鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。", "bbox": [630, 225, 911, 239]},
	{"text": "4、氯卓斯汀盐酸卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。", "bbox": [630, 253, 942, 267]},
	{"text": "5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/", "bbox": [630, 282, 933, 295]},
	{"text": "次 治疗过敏性鼻炎。", "bbox": [630, 300, 707, 313]},
	{"text": "6、枯草抗感染治疗（生理性海水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过", "bbox": [630, 330, 949, 343]},
	{"text": "敏性鼻炎", "bbox": [630, 350, 663, 363]},
	{"text": "已预约受试者安全性随访时间。", "bbox": [630, 378, 738, 391]},
	{"text": "过敏史：", "bbox": [630, 407, 687, 421]},
	{"text": "个人史：", "bbox": [630, 436, 678, 449]},
	{"text": "体格检查：", "bbox": [630, 464, 670, 477]},
	{"text": "专科情况：", "bbox": [630, 493, 670, 506]},
	{"text": "辅助检查：", "bbox": [630, 521, 670, 534]},
	{"text": "治疗项目：", "bbox": [630, 550, 668, 563]},
	{"text": "门诊诊断：", "bbox": [630, 579, 668, 592]},
	{"text": "支气管哮喘", "bbox": [683, 608, 723, 621]},
	{"text": "单病种：", "bbox": [630, 637, 678, 650]},
	{"text": "发病时间：", "bbox": [630, 666, 668, 679]},
	{"text": "处", "bbox": [630, 694, 639, 707]},
	{"text": "置：", "bbox": [674, 694, 687, 707]},
	{"text": "1心电图（心电图室做）", "bbox": [638, 724, 719, 737]},
	{"text": "2布地奈德福莫特罗吸入粉雾剂(II)(省采)●①② 2盒2 000.00入用药,一天2次", "bbox": [638, 754, 915, 767]},
	{"text": "30天", "bbox": [930, 755, 947, 767]},
	{"text": "备注：", "bbox": [630, 783, 687, 796]},
	{"text": "病情评估：", "bbox": [630, 813, 670, 826]},
	{"text": "病情分级：", "bbox": [787, 813, 825, 826]},
	{"text": "是否抢救病例：否", "bbox": [630, 841, 699, 854]},
	{"text": "是否抢救成功：", "bbox": [748, 841, 803, 854]},
	{"text": "是否为绿色通道患者：否", "bbox": [832, 841, 924, 854]},
	{"text": "病人去向：", "bbox": [630, 869, 670, 882]},
	{"text": "CS 扫描全能王", "bbox": [902, 943, 984, 963]},
	{"text": "3亿人都在用的扫描App", "bbox": [902, 970, 984, 981]}
]
2026-08-05 05:11:11,394 INFO     29 [qwen-vl-text] coord API: raw_items=42, valid_items=42, elapsed=16.1s
2026-08-05 05:11:11,394 INFO     29 [qwen-vl-text] coord item[0]: text=病历文书, bbox=[18, 35, 58, 49]
2026-08-05 05:11:11,394 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[18, 93, 64, 110]
2026-08-05 05:11:11,394 INFO     29 [qwen-vl-text] coord item[2]: text=25/10/10 14时 门诊病历, bbox=[18, 139, 127, 154]
2026-08-05 05:11:11,394 INFO     29 [qwen-vl-text] coord item[3]: text=25/10/24 15时 门诊病历（GCP专用）, bbox=[18, 188, 180, 203]
2026-08-05 05:11:11,394 INFO     29 [qwen-vl-text] coord item[4]: text=25/11/17 10时 门诊病历, bbox=[18, 237, 127, 252]
2026-08-05 05:11:11,394 INFO     29 [qwen-vl-text] coord item[5]: text=头降使用40瓶，平均每天使用4瓶，2025年9月10日用完4瓶（未使用试验药剂空瓶2次共4, bbox=[630, 73, 943, 86]
2026-08-05 05:11:11,394 INFO     29 [qwen-vl-text] coord item[6]: text=瓶，2025年9月10日后受试者每七天首先一次后空瓶5次共10瓶，总计使用10瓶（记录使, bbox=[630, 90, 947, 104]
2026-08-05 05:11:11,394 INFO     29 [qwen-vl-text] coord item[7]: text=用总共46瓶，与实际使用情况一致。, bbox=[630, 109, 754, 122]
2026-08-05 05:11:11,394 INFO     29 [qwen-vl-text] coord item[8]: text=8、回访ePRO以及MD。, bbox=[630, 138, 707, 151]
2026-08-05 05:11:11,394 INFO     29 [qwen-vl-text] coord item[9]: text=既往史：更新合并用药：, bbox=[630, 168, 733, 181]
2026-08-05 05:11:11,394 INFO     29 [qwen-vl-text] coord item[10]: text=1、鼻腔莫米松鼻喷雾剂C025 4 3-2025 7 25 每鼻 2喷/次 qd 治疗过敏性鼻炎。, bbox=[630, 196, 926, 210]
2026-08-05 05:11:11,395 INFO     29 [qwen-vl-text] coord item[11]: text=2、苯环喹莫铵鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。, bbox=[630, 225, 911, 239]
2026-08-05 05:11:11,395 INFO     29 [qwen-vl-text] coord item[12]: text=4、氯卓斯汀盐酸卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。, bbox=[630, 253, 942, 267]
2026-08-05 05:11:11,395 INFO     29 [qwen-vl-text] coord item[13]: text=5、枯草抗感染治疗（活性银离子抗菌素） 2025 9 3-2025 10 1 每日4次，每鼻2喷/, bbox=[630, 282, 933, 295]
2026-08-05 05:11:11,395 INFO     29 [qwen-vl-text] coord item[14]: text=次 治疗过敏性鼻炎。, bbox=[630, 300, 707, 313]
2026-08-05 05:11:11,395 INFO     29 [qwen-vl-text] coord item[15]: text=6、枯草抗感染治疗（生理性海水） 2025 9 3-2025 10 1 每日6次，每鼻4喷/次 治疗过, bbox=[630, 330, 949, 343]
2026-08-05 05:11:11,395 INFO     29 [qwen-vl-text] coord item[16]: text=敏性鼻炎, bbox=[630, 350, 663, 363]
2026-08-05 05:11:11,395 INFO     29 [qwen-vl-text] coord item[17]: text=已预约受试者安全性随访时间。, bbox=[630, 378, 738, 391]
2026-08-05 05:11:11,395 INFO     29 [qwen-vl-text] coord item[18]: text=过敏史：, bbox=[630, 407, 687, 421]
2026-08-05 05:11:11,395 INFO     29 [qwen-vl-text] coord item[19]: text=个人史：, bbox=[630, 436, 678, 449]
2026-08-05 05:11:11,395 INFO     29 [qwen-vl-text] coord item[20]: text=体格检查：, bbox=[630, 464, 670, 477]
2026-08-05 05:11:11,395 INFO     29 [qwen-vl-text] coord item[21]: text=专科情况：, bbox=[630, 493, 670, 506]
2026-08-05 05:11:11,395 INFO     29 [qwen-vl-text] coord item[22]: text=辅助检查：, bbox=[630, 521, 670, 534]
2026-08-05 05:11:11,395 INFO     29 [qwen-vl-text] coord item[23]: text=治疗项目：, bbox=[630, 550, 668, 563]
2026-08-05 05:11:11,395 INFO     29 [qwen-vl-text] coord item[24]: text=门诊诊断：, bbox=[630, 579, 668, 592]
2026-08-05 05:11:11,395 INFO     29 [qwen-vl-text] coord item[25]: text=支气管哮喘, bbox=[683, 608, 723, 621]
2026-08-05 05:11:11,395 INFO     29 [qwen-vl-text] coord item[26]: text=单病种：, bbox=[630, 637, 678, 650]
2026-08-05 05:11:11,395 INFO     29 [qwen-vl-text] coord item[27]: text=发病时间：, bbox=[630, 666, 668, 679]
2026-08-05 05:11:11,395 INFO     29 [qwen-vl-text] coord item[28]: text=处, bbox=[630, 694, 639, 707]
2026-08-05 05:11:11,395 INFO     29 [qwen-vl-text] coord item[29]: text=置：, bbox=[674, 694, 687, 707]
2026-08-05 05:11:11,395 INFO     29 [qwen-vl-text] coord item[30]: text=1心电图（心电图室做）, bbox=[638, 724, 719, 737]
2026-08-05 05:11:11,395 INFO     29 [qwen-vl-text] coord item[31]: text=2布地奈德福莫特罗吸入粉雾剂(II)(省采)●①② 2盒2 000.00入用药,一天2次, bbox=[638, 754, 915, 767]
2026-08-05 05:11:11,396 INFO     29 [qwen-vl-text] coord item[32]: text=30天, bbox=[930, 755, 947, 767]
2026-08-05 05:11:11,396 INFO     29 [qwen-vl-text] coord item[33]: text=备注：, bbox=[630, 783, 687, 796]
2026-08-05 05:11:11,396 INFO     29 [qwen-vl-text] coord item[34]: text=病情评估：, bbox=[630, 813, 670, 826]
2026-08-05 05:11:11,396 INFO     29 [qwen-vl-text] coord item[35]: text=病情分级：, bbox=[787, 813, 825, 826]
2026-08-05 05:11:11,396 INFO     29 [qwen-vl-text] coord item[36]: text=是否抢救病例：否, bbox=[630, 841, 699, 854]
2026-08-05 05:11:11,396 INFO     29 [qwen-vl-text] coord item[37]: text=是否抢救成功：, bbox=[748, 841, 803, 854]
2026-08-05 05:11:11,396 INFO     29 [qwen-vl-text] coord item[38]: text=是否为绿色通道患者：否, bbox=[832, 841, 924, 854]
2026-08-05 05:11:11,396 INFO     29 [qwen-vl-text] coord item[39]: text=病人去向：, bbox=[630, 869, 670, 882]
2026-08-05 05:11:11,396 INFO     29 [qwen-vl-text] coord item[40]: text=CS 扫描全能王, bbox=[902, 943, 984, 963]
2026-08-05 05:11:11,396 INFO     29 [qwen-vl-text] coord item[41]: text=3亿人都在用的扫描App, bbox=[902, 970, 984, 981]
2026-08-05 05:11:11,397 INFO     29 [qwen-vl-text] page=1 — 42/42 coords, api_time=16.1s
2026-08-05 05:11:11,400 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1082890, prompt_len=1572
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["就诊卡", "流水号：", "姓名", "龄：40岁", "就诊科", "日：2025-10-24 15:45:39", "主诉：安全性电话随访", "现病史：今日10:27", "固定电话（020-", "（159", "5），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无", "不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对", "V8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试", "者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，", "目前无安全性异常表现。", "合并用药更新：", "1、小柴胡颗粒、（自行购药）2025.10.6-2025.10.8 10g tid 治疗上呼吸道感染", "2、苯环喹溴铵鼻喷雾剂 2025.4.3-至今 每鼻2喷/次 qid 治疗过敏性鼻炎", "3、氮卓斯汀氟替卡松鼻喷雾剂 2025.9.3-至今 每鼻2喷/次 bid 治疗过敏性鼻炎", "4、辛芩颗粒 2024.8.21-2024.8.27 1袋 冲服 tid 治疗过敏性鼻炎", "AE：", "上呼吸道感染 2025年10月5日-2025年10月8日 中度，非SAE，采取药物治疗措施，对试验", "药物采取措施：剂量不变，与试验药物无关，未因该AE退出研究。", "病历更正：", "1、更正2024年10月22日病历，合并用药“辛芩颗粒”为“辛芩颗粒”；", "2、更正2024年10月22日病历，合并用药“苯环喹溴铵鼻喷雾剂”为“苯环喹溴铵鼻喷雾", "剂”；", "3、更正2025年1月24日病历，“无收到ePro触发的哮喘警报邮件”为“有收到ePro触发的哮", "喘警报邮件”；", "4、更正2025年7月18日病历，“受试者漏填2025年4月28日晚间日志” 更正为：“受试者", "漏填2025年4月28日早间日志”；", "5、更正2024年11月6日病历，“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共", "计用了26喷”为：“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了28", "喷”。", "医生"]

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
2026-08-05 05:11:24,029 INFO     29 [qwen-vl-text] coord API raw response (len=2396):
[
	{"text": "就诊卡", "bbox": [170, 98, 218, 115]},
	{"text": "流水号：", "bbox": [170, 131, 218, 148]},
	{"text": "姓名", "bbox": [170, 165, 187, 181]},
	{"text": "龄：40岁", "bbox": [647, 165, 710, 181]},
	{"text": "就诊科", "bbox": [170, 196, 218, 213]},
	{"text": "日：2025-10-24 15:45:39", "bbox": [616, 197, 818, 212]},
	{"text": "主诉：安全性电话随访", "bbox": [166, 228, 428, 246]},
	{"text": "现病史：今日10:27", "bbox": [166, 259, 362, 276]},
	{"text": "固定电话（020-", "bbox": [513, 260, 644, 276]},
	{"text": "（159", "bbox": [173, 281, 210, 297]},
	{"text": "5），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无", "bbox": [268, 281, 872, 297]},
	{"text": "不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对", "bbox": [166, 302, 878, 319]},
	{"text": "V8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试", "bbox": [166, 323, 877, 340]},
	{"text": "者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，", "bbox": [166, 344, 865, 361]},
	{"text": "目前无安全性异常表现。", "bbox": [166, 365, 355, 381]},
	{"text": "合并用药更新：", "bbox": [166, 395, 280, 411]},
	{"text": "1、小柴胡颗粒、（自行购药）2025.10.6-2025.10.8 10g tid 治疗上呼吸道感染", "bbox": [166, 425, 806, 441]},
	{"text": "2、苯环喹溴铵鼻喷雾剂 2025.4.3-至今 每鼻2喷/次 qid 治疗过敏性鼻炎", "bbox": [166, 455, 767, 471]},
	{"text": "3、氮卓斯汀氟替卡松鼻喷雾剂 2025.9.3-至今 每鼻2喷/次 bid 治疗过敏性鼻炎", "bbox": [166, 484, 817, 500]},
	{"text": "4、辛芩颗粒 2024.8.21-2024.8.27 1袋 冲服 tid 治疗过敏性鼻炎", "bbox": [166, 514, 717, 530]},
	{"text": "AE：", "bbox": [166, 545, 192, 558]},
	{"text": "上呼吸道感染 2025年10月5日-2025年10月8日 中度，非SAE，采取药物治疗措施，对试验", "bbox": [166, 573, 851, 589]},
	{"text": "药物采取措施：剂量不变，与试验药物无关，未因该AE退出研究。", "bbox": [166, 593, 656, 609]},
	{"text": "病历更正：", "bbox": [166, 622, 244, 638]},
	{"text": "1、更正2024年10月22日病历，合并用药“辛芩颗粒”为“辛芩颗粒”；", "bbox": [166, 651, 693, 667]},
	{"text": "2、更正2024年10月22日病历，合并用药“苯环喹溴铵鼻喷雾剂”为“苯环喹溴铵鼻喷雾", "bbox": [166, 679, 812, 695]},
	{"text": "剂”；", "bbox": [166, 698, 210, 713]},
	{"text": "3、更正2025年1月24日病历，“无收到ePro触发的哮喘警报邮件”为“有收到ePro触发的哮", "bbox": [166, 726, 831, 742]},
	{"text": "喘警报邮件”；", "bbox": [166, 745, 277, 760]},
	{"text": "4、更正2025年7月18日病历，“受试者漏填2025年4月28日晚间日志” 更正为：“受试者", "bbox": [166, 772, 817, 788]},
	{"text": "漏填2025年4月28日早间日志”；", "bbox": [166, 790, 402, 805]},
	{"text": "5、更正2024年11月6日病历，“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共", "bbox": [166, 817, 819, 833]},
	{"text": "计用了26喷”为：“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了28", "bbox": [166, 835, 802, 851]},
	{"text": "喷”。", "bbox": [166, 853, 213, 867]},
	{"text": "医生", "bbox": [166, 877, 267, 891]}
]
2026-08-05 05:11:24,029 INFO     29 [qwen-vl-text] coord API: raw_items=35, valid_items=35, elapsed=12.6s
2026-08-05 05:11:24,029 INFO     29 [qwen-vl-text] coord item[0]: text=就诊卡, bbox=[170, 98, 218, 115]
2026-08-05 05:11:24,029 INFO     29 [qwen-vl-text] coord item[1]: text=流水号：, bbox=[170, 131, 218, 148]
2026-08-05 05:11:24,029 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[170, 165, 187, 181]
2026-08-05 05:11:24,029 INFO     29 [qwen-vl-text] coord item[3]: text=龄：40岁, bbox=[647, 165, 710, 181]
2026-08-05 05:11:24,029 INFO     29 [qwen-vl-text] coord item[4]: text=就诊科, bbox=[170, 196, 218, 213]
2026-08-05 05:11:24,029 INFO     29 [qwen-vl-text] coord item[5]: text=日：2025-10-24 15:45:39, bbox=[616, 197, 818, 212]
2026-08-05 05:11:24,029 INFO     29 [qwen-vl-text] coord item[6]: text=主诉：安全性电话随访, bbox=[166, 228, 428, 246]
2026-08-05 05:11:24,029 INFO     29 [qwen-vl-text] coord item[7]: text=现病史：今日10:27, bbox=[166, 259, 362, 276]
2026-08-05 05:11:24,029 INFO     29 [qwen-vl-text] coord item[8]: text=固定电话（020-, bbox=[513, 260, 644, 276]
2026-08-05 05:11:24,029 INFO     29 [qwen-vl-text] coord item[9]: text=（159, bbox=[173, 281, 210, 297]
2026-08-05 05:11:24,029 INFO     29 [qwen-vl-text] coord item[10]: text=5），询问上次访视至今有无不适，及收集合并用药使用情况，受试者告知无, bbox=[268, 281, 872, 297]
2026-08-05 05:11:24,029 INFO     29 [qwen-vl-text] coord item[11]: text=不适，并补充告知上次访视不良事件及合并用药情况，告知受试者2025年10月10日因中心对, bbox=[166, 302, 878, 319]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[12]: text=V8访视窗（理论2025年11月5日±4天）计算错误，提前完成V8随访，今日获知该情况后因受试, bbox=[166, 323, 877, 340]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[13]: text=者不愿返院随访确定于2025年10月10日提前终止药物治疗，因该PD对受试者权益造成影响，, bbox=[166, 344, 865, 361]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[14]: text=目前无安全性异常表现。, bbox=[166, 365, 355, 381]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[15]: text=合并用药更新：, bbox=[166, 395, 280, 411]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[16]: text=1、小柴胡颗粒、（自行购药）2025.10.6-2025.10.8 10g tid 治疗上呼吸道感染, bbox=[166, 425, 806, 441]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[17]: text=2、苯环喹溴铵鼻喷雾剂 2025.4.3-至今 每鼻2喷/次 qid 治疗过敏性鼻炎, bbox=[166, 455, 767, 471]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[18]: text=3、氮卓斯汀氟替卡松鼻喷雾剂 2025.9.3-至今 每鼻2喷/次 bid 治疗过敏性鼻炎, bbox=[166, 484, 817, 500]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[19]: text=4、辛芩颗粒 2024.8.21-2024.8.27 1袋 冲服 tid 治疗过敏性鼻炎, bbox=[166, 514, 717, 530]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[20]: text=AE：, bbox=[166, 545, 192, 558]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[21]: text=上呼吸道感染 2025年10月5日-2025年10月8日 中度，非SAE，采取药物治疗措施，对试验, bbox=[166, 573, 851, 589]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[22]: text=药物采取措施：剂量不变，与试验药物无关，未因该AE退出研究。, bbox=[166, 593, 656, 609]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[23]: text=病历更正：, bbox=[166, 622, 244, 638]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[24]: text=1、更正2024年10月22日病历，合并用药“辛芩颗粒”为“辛芩颗粒”；, bbox=[166, 651, 693, 667]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[25]: text=2、更正2024年10月22日病历，合并用药“苯环喹溴铵鼻喷雾剂”为“苯环喹溴铵鼻喷雾, bbox=[166, 679, 812, 695]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[26]: text=剂”；, bbox=[166, 698, 210, 713]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[27]: text=3、更正2025年1月24日病历，“无收到ePro触发的哮喘警报邮件”为“有收到ePro触发的哮, bbox=[166, 726, 831, 742]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[28]: text=喘警报邮件”；, bbox=[166, 745, 277, 760]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[29]: text=4、更正2025年7月18日病历，“受试者漏填2025年4月28日晚间日志” 更正为：“受试者, bbox=[166, 772, 817, 788]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[30]: text=漏填2025年4月28日早间日志”；, bbox=[166, 790, 402, 805]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[31]: text=5、更正2024年11月6日病历，“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共, bbox=[166, 817, 819, 833]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[32]: text=计用了26喷”为：“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了28, bbox=[166, 835, 802, 851]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[33]: text=喷”。, bbox=[166, 853, 213, 867]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] coord item[34]: text=医生, bbox=[166, 877, 267, 891]
2026-08-05 05:11:24,030 INFO     29 [qwen-vl-text] page=2 — 35/35 coords, api_time=12.6s
2026-08-05 05:11:24,031 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1159920, prompt_len=1454
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
2026-08-05 05:11:34,447 INFO     29 [qwen-vl-text] coord API raw response (len=1869):
[
	{"text": "病历编号：", "bbox": [545, 130, 600, 144]},
	{"text": "姓名：", "bbox": [177, 130, 225, 144]},
	{"text": "性别：", "bbox": [177, 160, 192, 174]},
	{"text": "年龄：40岁", "bbox": [608, 160, 665, 174]},
	{"text": "就诊科：", "bbox": [177, 189, 228, 204]},
	{"text": "就诊时间：2025-11-17 10:10:48", "bbox": [545, 189, 763, 203]},
	{"text": "主诉：支气管哮喘治疗后复查：", "bbox": [175, 218, 466, 234]},
	{"text": "现病史：2021年2月前开始出现咳嗽、咯痰，粘白，量中，能咯出，咳嗽呈阵发性、刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏。无咽痛，无伴反酸、嗳气、腹胀。无上腹部隐痛不适感，无伴发热、畏寒，影响睡眠。晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：", "bbox": [175, 247, 820, 319]},
	{"text": "12.52*109/L 嗜酸粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定。本次门诊距上次门诊间隔时间30天。症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确。急性发作情况：两次，就诊期间急性发作：无，发作次数：0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。近3天来出现咽痛不适", "bbox": [175, 323, 813, 412]},
	{"text": "既往史：鼻炎病史无规则治疗。打鼾明显。", "bbox": [175, 425, 508, 440]},
	{"text": "过敏史：未发现。", "bbox": [175, 453, 335, 468]},
	{"text": "个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。", "bbox": [175, 479, 800, 512]},
	{"text": "体格检查：神志清，颈软，双肺呼吸音粗，未闻及明显干、湿性罗音，口腔粘膜无白斑。", "bbox": [177, 524, 780, 539]},
	{"text": "专科情况：", "bbox": [177, 551, 254, 565]},
	{"text": "辅助检查：", "bbox": [177, 578, 254, 592]},
	{"text": "治疗项目：", "bbox": [177, 605, 254, 619]},
	{"text": "门诊诊断：", "bbox": [177, 630, 254, 644]},
	{"text": "1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、阻塞性睡眠呼吸暂停低通气综合征,4、急性咽炎", "bbox": [193, 657, 770, 688]},
	{"text": "单病种：", "bbox": [177, 700, 269, 714]},
	{"text": "发病时间：", "bbox": [177, 724, 254, 738]},
	{"text": "处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不适随诊。", "bbox": [260, 750, 675, 763]},
	{"text": "1金银花口服液◆⑤ 2盒 20.0ml,口服,一天3次(口服) 6天", "bbox": [198, 774, 716, 788]},
	{"text": "2氨卓斯汀氟替卡松鼻喷雾剂◆ 1瓶 2.0喷,喷鼻,一天2次 30天", "bbox": [198, 800, 672, 813]},
	{"text": "3苯环喹溴铵鼻喷雾剂◆ 3瓶 2.0喷,喷鼻,一天4次 30天", "bbox": [198, 825, 670, 838]},
	{"text": "备注：建议在住地附近社区医疗机构随诊。", "bbox": [260, 848, 521, 861]}
]
2026-08-05 05:11:34,447 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=10.4s
2026-08-05 05:11:34,447 INFO     29 [qwen-vl-text] coord item[0]: text=病历编号：, bbox=[545, 130, 600, 144]
2026-08-05 05:11:34,448 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[177, 130, 225, 144]
2026-08-05 05:11:34,448 INFO     29 [qwen-vl-text] coord item[2]: text=性别：, bbox=[177, 160, 192, 174]
2026-08-05 05:11:34,448 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：40岁, bbox=[608, 160, 665, 174]
2026-08-05 05:11:34,448 INFO     29 [qwen-vl-text] coord item[4]: text=就诊科：, bbox=[177, 189, 228, 204]
2026-08-05 05:11:34,448 INFO     29 [qwen-vl-text] coord item[5]: text=就诊时间：2025-11-17 10:10:48, bbox=[545, 189, 763, 203]
2026-08-05 05:11:34,448 INFO     29 [qwen-vl-text] coord item[6]: text=主诉：支气管哮喘治疗后复查：, bbox=[175, 218, 466, 234]
2026-08-05 05:11:34,448 INFO     29 [qwen-vl-text] coord item[7]: text=现病史：2021年2月前开始出现咳嗽、咯痰，粘白，量中，能咯出，咳嗽呈阵发性、刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏。无咽痛，无伴反酸、嗳气、腹胀。无上腹部隐痛不适感，无伴发热、畏寒，影响睡眠。晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：, bbox=[175, 247, 820, 319]
2026-08-05 05:11:34,448 INFO     29 [qwen-vl-text] coord item[8]: text=12.52*109/L 嗜酸粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定。本次门诊距上次门诊间隔时间30天。症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确。急性发作情况：两次，就诊期间急性发作：无，发作次数：0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。近3天来出现咽痛不适, bbox=[175, 323, 813, 412]
2026-08-05 05:11:34,448 INFO     29 [qwen-vl-text] coord item[9]: text=既往史：鼻炎病史无规则治疗。打鼾明显。, bbox=[175, 425, 508, 440]
2026-08-05 05:11:34,448 INFO     29 [qwen-vl-text] coord item[10]: text=过敏史：未发现。, bbox=[175, 453, 335, 468]
2026-08-05 05:11:34,448 INFO     29 [qwen-vl-text] coord item[11]: text=个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。, bbox=[175, 479, 800, 512]
2026-08-05 05:11:34,448 INFO     29 [qwen-vl-text] coord item[12]: text=体格检查：神志清，颈软，双肺呼吸音粗，未闻及明显干、湿性罗音，口腔粘膜无白斑。, bbox=[177, 524, 780, 539]
2026-08-05 05:11:34,448 INFO     29 [qwen-vl-text] coord item[13]: text=专科情况：, bbox=[177, 551, 254, 565]
2026-08-05 05:11:34,448 INFO     29 [qwen-vl-text] coord item[14]: text=辅助检查：, bbox=[177, 578, 254, 592]
2026-08-05 05:11:34,448 INFO     29 [qwen-vl-text] coord item[15]: text=治疗项目：, bbox=[177, 605, 254, 619]
2026-08-05 05:11:34,448 INFO     29 [qwen-vl-text] coord item[16]: text=门诊诊断：, bbox=[177, 630, 254, 644]
2026-08-05 05:11:34,448 INFO     29 [qwen-vl-text] coord item[17]: text=1、支气管哮喘,2、过敏性鼻炎[变应性鼻炎],3、阻塞性睡眠呼吸暂停低通气综合征,4、急性咽炎, bbox=[193, 657, 770, 688]
2026-08-05 05:11:34,448 INFO     29 [qwen-vl-text] coord item[18]: text=单病种：, bbox=[177, 700, 269, 714]
2026-08-05 05:11:34,448 INFO     29 [qwen-vl-text] coord item[19]: text=发病时间：, bbox=[177, 724, 254, 738]
2026-08-05 05:11:34,448 INFO     29 [qwen-vl-text] coord item[20]: text=处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不适随诊。, bbox=[260, 750, 675, 763]
2026-08-05 05:11:34,448 INFO     29 [qwen-vl-text] coord item[21]: text=1金银花口服液◆⑤ 2盒 20.0ml,口服,一天3次(口服) 6天, bbox=[198, 774, 716, 788]
2026-08-05 05:11:34,449 INFO     29 [qwen-vl-text] coord item[22]: text=2氨卓斯汀氟替卡松鼻喷雾剂◆ 1瓶 2.0喷,喷鼻,一天2次 30天, bbox=[198, 800, 672, 813]
2026-08-05 05:11:34,449 INFO     29 [qwen-vl-text] coord item[23]: text=3苯环喹溴铵鼻喷雾剂◆ 3瓶 2.0喷,喷鼻,一天4次 30天, bbox=[198, 825, 670, 838]
2026-08-05 05:11:34,449 INFO     29 [qwen-vl-text] coord item[24]: text=备注：建议在住地附近社区医疗机构随诊。, bbox=[260, 848, 521, 861]
2026-08-05 05:11:34,449 INFO     29 [qwen-vl-text] page=3 — 25/25 coords, api_time=10.4s
2026-08-05 05:11:34,449 INFO     29 [qwen-vl-text] new_positions (122):
[[0, 321.895, 367.115, 98.514, 112.828], [0, 260.61, 298.09499999999997, 126.3, 140.614], [0, 372.46999999999997, 410.54999999999995, 127.142, 140.614], [0, 96.39, 221.34, 153.244, 167.558], [0, 321.895, 473.025, 154.08599999999998, 166.716], [0, 95.19999999999999, 238.0, 181.03, 194.50199999999998], [0, 95.19999999999999, 508.72499999999997, 207.132, 290.49], [0, 95.19999999999999, 163.625, 303.12, 315.75], [0, 95.19999999999999, 506.34499999999997, 328.38, 357.84999999999997], [0, 95.19999999999999, 320.705, 369.638, 383.11], [0, 95.19999999999999, 489.09, 394.89799999999997, 425.21], [0, 95.19999999999999, 500.98999999999995, 437.84, 554.036], [0, 95.19999999999999, 316.53999999999996, 566.6659999999999, 580.138], [0, 95.19999999999999, 399.84, 591.9259999999999, 605.398], [0, 95.19999999999999, 489.09, 617.1859999999999, 681.178], [0, 95.19999999999999, 193.375, 693.808, 707.28], [0, 95.19999999999999, 225.505, 719.91, 733.382], [0, 95.19999999999999, 456.36499999999995, 744.328, 756.958], [0, 512.89, 581.3149999999999, 806.636, 820.108], [0, 512.89, 581.3149999999999, 822.634, 831.054], [1, 15.155999999999999, 48.836, 20.825, 29.154999999999998], [1, 15.155999999999999, 53.888, 55.335, 65.45], [1, 15.155999999999999, 106.934, 82.705, 91.63], [1, 15.155999999999999, 151.56, 111.86, 120.785], [1, 15.155999999999999, 106.934, 141.015, 149.94], [1, 530.46, 794.006, 43.434999999999995, 51.169999999999995], [1, 530.46, 797.374, 53.55, 61.879999999999995], [1, 530.46, 634.8679999999999, 64.855, 72.59], [1, 530.46, 595.294, 82.11, 89.845], [1, 530.46, 617.1859999999999, 99.96, 107.695], [1, 530.46, 779.692, 116.61999999999999, 124.94999999999999], [1, 530.46, 767.062, 133.875, 142.20499999999998], [1, 530.46, 793.164, 150.535, 158.86499999999998], [1, 530.46, 785.586, 167.79, 175.525], [1, 530.46, 595.294, 178.5, 186.23499999999999], [1, 530.46, 799.058, 196.35, 204.08499999999998], [1, 530.46, 558.246, 208.25, 215.98499999999999], [1, 530.46, 621.396, 224.91, 232.64499999999998], [1, 530.46, 578.454, 242.165, 250.49499999999998], [1, 530.46, 570.876, 259.42, 267.155], [1, 530.46, 564.14, 276.08, 283.815], [1, 530.46, 564.14, 293.335, 301.07], [1, 530.46, 564.14, 309.995, 317.72999999999996], [1, 530.46, 562.456, 327.25, 334.98499999999996], [1, 530.46, 562.456, 344.505, 352.24], [1, 575.086, 608.766, 361.76, 369.495], [1, 530.46, 570.876, 379.015, 386.75], [1, 530.46, 562.456, 396.27, 404.005], [1, 530.46, 538.038, 412.93, 420.66499999999996], [1, 567.5079999999999, 578.454, 412.93, 420.66499999999996], [1, 537.196, 605.398, 430.78, 438.515], [1, 537.196, 770.43, 448.63, 456.36499999999995], [1, 783.06, 797.374, 449.22499999999997, 456.36499999999995], [1, 530.46, 578.454, 465.885, 473.62], [1, 530.46, 564.14, 483.73499999999996, 491.46999999999997], [1, 662.654, 694.65, 483.73499999999996, 491.46999999999997], [1, 530.46, 588.558, 500.395, 508.13], [1, 629.816, 676.126, 500.395, 508.13], [1, 700.544, 778.0079999999999, 500.395, 508.13], [1, 530.46, 564.14, 517.055, 524.79], [1, 759.4839999999999, 828.528, 561.0849999999999, 572.985], [1, 759.4839999999999, 828.528, 577.15, 583.6949999999999], [2, 101.14999999999999, 129.71, 82.51599999999999, 96.83], [2, 101.14999999999999, 129.71, 110.30199999999999, 124.616], [2, 101.14999999999999, 111.265, 138.93, 152.402], [2, 384.965, 422.45, 138.93, 152.402], [2, 101.14999999999999, 129.71, 165.03199999999998, 179.346], [2, 366.52, 486.71, 165.874, 178.504], [2, 98.77, 254.66, 191.976, 207.132], [2, 98.77, 215.39, 218.078, 232.392], [2, 305.235, 383.18, 218.92, 232.392], [2, 102.935, 124.94999999999999, 236.602, 250.07399999999998], [2, 159.45999999999998, 518.84, 236.602, 250.07399999999998], [2, 98.77, 522.41, 254.284, 268.598], [2, 98.77, 521.8149999999999, 271.966, 286.28], [2, 98.77, 514.675, 289.64799999999997, 303.962], [2, 98.77, 211.225, 307.33, 320.80199999999996], [2, 98.77, 166.6, 332.59, 346.062], [2, 98.77, 479.57, 357.84999999999997, 371.322], [2, 98.77, 456.36499999999995, 383.11, 396.582], [2, 98.77, 486.11499999999995, 407.52799999999996, 421.0], [2, 98.77, 426.615, 432.788, 446.26], [2, 98.77, 114.24, 458.89, 469.83599999999996], [2, 98.77, 506.34499999999997, 482.466, 495.938], [2, 98.77, 390.32, 499.306, 512.778], [2, 98.77, 145.18, 523.7239999999999, 537.196], [2, 98.77, 412.335, 548.1419999999999, 561.614], [2, 98.77, 483.14, 571.718, 585.1899999999999], [2, 98.77, 124.94999999999999, 587.716, 600.346], [2, 98.77, 494.445, 611.292, 624.764], [2, 98.77, 164.815, 627.29, 639.92], [2, 98.77, 486.11499999999995, 650.024, 663.496], [2, 98.77, 239.19, 665.18, 677.81], [2, 98.77, 487.30499999999995, 687.914, 701.386], [2, 98.77, 477.19, 703.0699999999999, 716.542], [2, 98.77, 126.735, 718.226, 730.014], [2, 98.77, 158.86499999999998, 738.434, 750.222], [3, 324.275, 357.0, 109.46, 121.24799999999999], [3, 105.315, 133.875, 109.46, 121.24799999999999], [3, 105.315, 114.24, 134.72, 146.50799999999998], [3, 361.76, 395.67499999999995, 134.72, 146.50799999999998], [3, 105.315, 135.66, 159.138, 171.768], [3, 324.275, 453.98499999999996, 159.138, 170.926], [3, 104.125, 277.27, 183.55599999999998, 197.028], [3, 104.125, 487.9, 207.974, 268.598], [3, 104.125, 483.73499999999996, 271.966, 346.904], [3, 104.125, 302.26, 357.84999999999997, 370.47999999999996], [3, 104.125, 199.325, 381.426, 394.056], [3, 104.125, 476.0, 403.318, 431.104], [3, 105.315, 464.09999999999997, 441.20799999999997, 453.83799999999997], [3, 105.315, 151.13, 463.942, 475.72999999999996], [3, 105.315, 151.13, 486.676, 498.464], [3, 105.315, 151.13, 509.40999999999997, 521.198], [3, 105.315, 151.13, 530.46, 542.2479999999999], [3, 114.835, 458.15, 553.194, 579.2959999999999], [3, 105.315, 160.055, 589.4, 601.188], [3, 105.315, 151.13, 609.608, 621.396], [3, 154.7, 401.625, 631.5, 642.446], [3, 117.80999999999999, 426.02, 651.708, 663.496], [3, 117.80999999999999, 399.84, 673.6, 684.5459999999999], [3, 117.80999999999999, 398.65, 694.65, 705.596], [3, 154.7, 309.995, 714.016, 724.962]]
2026-08-05 05:11:34,450 INFO     29 [qwen-vl-text] ═══ DONE ═══ 122 positions, pages=4, time=78.5s
2026-08-05 05:11:34,450 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:11:34,450 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 05:11:34,450 INFO     29 [qwen-vl-text] positions(44): [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:11:34,450 INFO     29 [qwen-vl-text] page grouping: [13], lines per page: [44]
2026-08-05 05:11:34,628 INFO     29 [qwen-vl-text] page=13, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:11:34,629 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1134
2026-08-05 05:11:34,629 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:11:34,629 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 725, \"bbox_end\": 768, \"encounter_dates\": [\"2026-01-05\"], \"department\": \"内科门诊(荔湾)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "广州医科大学附属第三医院\nThe Third Affiliated Hospital of Guangzhou Medical University\n门(急)诊病历信息\n就诊卡\n流水\n姓\n病历编号:\n年 龄:41岁\n就诊科室:内科门诊(荔湾) 医\n就诊时间:2026-01-05 17:07:54\n主 诉:支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天\n现 病 史:2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激\n性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流\n涕、嗅觉,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响\n睡眠,晨起有咽干,曾到本院就诊两次,症状不见明显缓解。2021-1-9血常规:白细胞:\n12.52*109/L 嗜酸粒细胞:0.65*109/L 5.2%,经治疗后症状明显缓解。无咳嗽、咯痰、气\n促。病情稳定,本次门诊距上次门诊间隔时间30天。症状控制情况:过去4周,患者:吸入\n药物使用情况:遵医嘱使用;吸入装置使用情况:正确。急性发作情况:两次,就诊期间急\n性发作:无,发作次数:0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。长期规律使用信必\n可160/4.5ug 2吸 bid治疗,5天前开始出现咳嗽、咯痰,黄白痰,量少,难以咯出,咳嗽以\n夜间为主。无气促,伴咽息,鼻塞、流涕、喷嚏,无发热。\n既 往 史:鼻炎病史无规则治疗。打鼾明显。\n过 敏 史:未发现;\n个 人 史:否认遗传病史,吸烟10年,20支/日,2018年戒烟。偶饮酒。2021-12-20已打第\n三针新冠疫苗。\n体格检查:神志清,颈软,双肺呼吸音粗,可闻及散在哮鸣音,口腔粘膜无白斑。\n专科情况:\n辅助检查:\n治疗项目:\n门诊诊断:\n1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎\n处 置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。\n布地奈德福莫特罗吸入粉雾剂(II)2盒 2.0吸,吸入用药,一天2次 30天\n(省采)●①⑤\n左氧氟沙星片(省采)●⑥ 5片 0.5g,口服,每日1次(口服) 5天\n第1页\n广州医科大学附属第三医院\nThe Third Affiliated Hospital of Guangzhou Medical University\n门(急)诊病历信息\n复方甲氧那明胶囊(省采)●② 1瓶 1.0粒,餐后口服,一天3次(口服) 5天\n盐酸氨溴索分散片(省采)●⑥ 15片 30.0mg,餐后口服,一天3次(口服) 5\n天\n醋酸泼尼松片●②④ 6片 10.0mg,口服,每早1次(口服) 3天\n备 注:建议在住地附近社区医疗机构随诊。",
    "role": "user"
  }
]
[92m05:11:34 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:11:34,630 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:11:34,633 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:11:34.632+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 15, "failed": 0, "current": {"4e4700ce908b11f1a3da71efcdd7cc1f": {"id": "4e4700ce908b11f1a3da71efcdd7cc1f", "doc_id": "4e10ceb4908b11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906341337, "task_type": "dataflow", "root_trace_id": "ca345e6640ff4d788f444c3ab712853e", "root_traceparent": "00-ca345e6640ff4d788f444c3ab712853e-8ea193cced1ce3aa-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:11:44,315 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:11:44,315 INFO     29 [qwen-vl-text] LLM output (len=886):
{
  "encounter_date": "2026-01-05",
  "chief_complaint": "支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天",
  "present_illness": "2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流涕、嗅觉,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响睡眠,晨起有咽干,曾到本院就诊两次,症状不见明显缓解。2021-1-9血常规:白细胞:12.52*109/L 嗜酸粒细胞:0.65*109/L 5.2%,经治疗后症状明显缓解。无咳嗽、咯痰、气促。病情稳定,本次门诊距上次门诊间隔时间30天。症状控制情况:过去4周,患者:吸入药物使用情况:遵医嘱使用;吸入装置使用情况:正确。急性发作情况:两次,就诊期间急性发作:无,发作次数:0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。长期规律使用信必可160/4.5ug 2吸 bid治疗,5天前开始出现咳嗽、咯痰,黄白痰,量少,难以咯出,咳嗽以夜间为主。无气促,伴咽息,鼻塞、流涕、喷嚏,无发热。",
  "past_history": "鼻炎病史无规则治疗。打鼾明显。否认遗传病史,吸烟10年,20支/日,2018年戒烟。偶饮酒。2021-12-20已打第三针新冠疫苗。未发现过敏史。",
  "diagnosis": "1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎",
  "treatment_plan": [
    "布地奈德福莫特罗吸入粉雾剂(II) 2盒 2.0吸 吸入用药 一天2次 30天",
    "左氧氟沙星片 5片 0.5g 口服 每日1次 5天",
    "复方甲氧那明胶囊 1瓶 1.0粒 餐后口服 一天3次 5天",
    "盐酸氨溴索分散片 15片 30.0mg 餐后口服 一天3次 5天",
    "醋酸泼尼松片 6片 10.0mg 口服 每早1次 3天"
  ]
}
2026-08-05 05:11:44,316 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-05]
2026-08-05 05:11:44,319 INFO     29 [qwen-vl-text] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1091238, prompt_len=1879
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共44行）
["广州医科大学附属第三医院", "The Third Affiliated Hospital of Guangzhou Medical University", "门(急)诊病历信息", "就诊卡", "流水", "姓", "病历编号:", "年 龄:41岁", "就诊科室:内科门诊(荔湾) 医", "就诊时间:2026-01-05 17:07:54", "主 诉:支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天", "现 病 史:2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激", "性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流", "涕、嗅觉,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响", "睡眠,晨起有咽干,曾到本院就诊两次,症状不见明显缓解。2021-1-9血常规:白细胞:", "12.52*109/L 嗜酸粒细胞:0.65*109/L 5.2%,经治疗后症状明显缓解。无咳嗽、咯痰、气", "促。病情稳定,本次门诊距上次门诊间隔时间30天。症状控制情况:过去4周,患者:吸入", "药物使用情况:遵医嘱使用;吸入装置使用情况:正确。急性发作情况:两次,就诊期间急", "性发作:无,发作次数:0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。长期规律使用信必", "可160/4.5ug 2吸 bid治疗,5天前开始出现咳嗽、咯痰,黄白痰,量少,难以咯出,咳嗽以", "夜间为主。无气促,伴咽息,鼻塞、流涕、喷嚏,无发热。", "既 往 史:鼻炎病史无规则治疗。打鼾明显。", "过 敏 史:未发现;", "个 人 史:否认遗传病史,吸烟10年,20支/日,2018年戒烟。偶饮酒。2021-12-20已打第", "三针新冠疫苗。", "体格检查:神志清,颈软,双肺呼吸音粗,可闻及散在哮鸣音,口腔粘膜无白斑。", "专科情况:", "辅助检查:", "治疗项目:", "门诊诊断:", "1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎", "处 置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。", "布地奈德福莫特罗吸入粉雾剂(II)2盒 2.0吸,吸入用药,一天2次 30天", "(省采)●①⑤", "左氧氟沙星片(省采)●⑥ 5片 0.5g,口服,每日1次(口服) 5天", "第1页", "广州医科大学附属第三医院", "The Third Affiliated Hospital of Guangzhou Medical University", "门(急)诊病历信息", "复方甲氧那明胶囊(省采)●② 1瓶 1.0粒,餐后口服,一天3次(口服) 5天", "盐酸氨溴索分散片(省采)●⑥ 15片 30.0mg,餐后口服,一天3次(口服) 5", "天", "醋酸泼尼松片●②④ 6片 10.0mg,口服,每早1次(口服) 3天", "备 注:建议在住地附近社区医疗机构随诊。"]

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
2026-08-05 05:12:00,591 INFO     29 [qwen-vl-text] coord API raw response (len=3081):
[
	{"text": "广州医科大学附属第三医院", "bbox": [98, 250, 252, 263]},	
	{"text": "The Third Affiliated Hospital of Guangzhou Medical University", "bbox": [98, 261, 252, 268]},	
	{"text": "门(急)诊病历信息", "bbox": [188, 280, 314, 294]},	
	{"text": "就诊卡", "bbox": [50, 314, 82, 323]},	
	{"text": "流水", "bbox": [50, 327, 77, 336]},	
	{"text": "姓", "bbox": [50, 340, 62, 349]},	
	{"text": "病历编号:", "bbox": [296, 327, 344, 336]},	
	{"text": "年 龄:41岁", "bbox": [296, 340, 366, 349]},	
	{"text": "就诊科室:内科门诊(荔湾) 医", "bbox": [50, 353, 214, 362]},	
	{"text": "就诊时间:2026-01-05 17:07:54", "bbox": [296, 353, 446, 362]},	
	{"text": "主 诉:支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天", "bbox": [50, 365, 314, 374]},	
	{"text": "现 病 史:2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激", "bbox": [50, 378, 460, 387]},	
	{"text": "性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流", "bbox": [50, 391, 455, 400]},	
	{"text": "涕、嗅觉,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响", "bbox": [50, 404, 466, 413]},	
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
	{"text": "体格检查:神志清,颈软,双肺呼吸音粗,可闻及散在哮鸣音,口腔粘膜无白斑。", "bbox": [50, 560, 427, 570]},	
	{"text": "专科情况:", "bbox": [50, 574, 97, 583]},	
	{"text": "辅助检查:", "bbox": [50, 587, 97, 596]},	
	{"text": "治疗项目:", "bbox": [50, 601, 97, 610]},	
	{"text": "门诊诊断:", "bbox": [50, 615, 97, 624]},	
	{"text": "1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎", "bbox": [50, 631, 432, 640]},	
	{"text": "处 置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。", "bbox": [50, 645, 377, 655]},	
	{"text": "布地奈德福莫特罗吸入粉雾剂(II)2盒 2.0吸,吸入用药,一天2次 30天", "bbox": [109, 660, 458, 669]},	
	{"text": "(省采)●①⑤", "bbox": [110, 674, 173, 683]},	
	{"text": "左氧氟沙星片(省采)●⑥ 5片 0.5g,口服,每日1次(口服) 5天", "bbox": [109, 688, 460, 698]},	
	{"text": "第1页", "bbox": [246, 706, 282, 714]},	
	{"text": "广州医科大学附属第三医院", "bbox": [558, 245, 720, 258]},	
	{"text": "The Third Affiliated Hospital of Guangzhou Medical University", "bbox": [558, 256, 720, 263]},	
	{"text": "门(急)诊病历信息", "bbox": [654, 275, 786, 289]},	
	{"text": "复方甲氧那明胶囊(省采)●② 1瓶 1.0粒,餐后口服,一天3次(口服) 5天", "bbox": [569, 309, 945, 319]},	
	{"text": "盐酸氨溴索分散片(省采)●⑥ 15片 30.0mg,餐后口服,一天3次(口服) 5", "bbox": [569, 323, 941, 333]},	
	{"text": "天", "bbox": [766, 336, 779, 345]},	
	{"text": "醋酸泼尼松片●②④ 6片 10.0mg,口服,每早1次(口服) 3天", "bbox": [569, 350, 931, 360]},	
	{"text": "备 注:建议在住地附近社区医疗机构随诊。", "bbox": [511, 363, 732, 372]}
]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord API: raw_items=44, valid_items=44, elapsed=16.3s
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[0]: text=广州医科大学附属第三医院, bbox=[98, 250, 252, 263]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[1]: text=The Third Affiliated Hospital of Guangzhou Medical University, bbox=[98, 261, 252, 268]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[2]: text=门(急)诊病历信息, bbox=[188, 280, 314, 294]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[3]: text=就诊卡, bbox=[50, 314, 82, 323]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[4]: text=流水, bbox=[50, 327, 77, 336]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[5]: text=姓, bbox=[50, 340, 62, 349]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[6]: text=病历编号:, bbox=[296, 327, 344, 336]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[7]: text=年 龄:41岁, bbox=[296, 340, 366, 349]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[8]: text=就诊科室:内科门诊(荔湾) 医, bbox=[50, 353, 214, 362]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[9]: text=就诊时间:2026-01-05 17:07:54, bbox=[296, 353, 446, 362]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[10]: text=主 诉:支气管哮喘治疗后复查,咳嗽、咯痰、喘息5天, bbox=[50, 365, 314, 374]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[11]: text=现 病 史:2021年2月前开始出现咳嗽、咯痰,粘白,量中,能咯出,咳嗽呈阵发性、刺激, bbox=[50, 378, 460, 387]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[12]: text=性,伴咽痒,咳嗽以夜间明显,自觉有吸入性呼吸困难,伴喘息,无胸闷,曾有鼻塞、流, bbox=[50, 391, 455, 400]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[13]: text=涕、嗅觉,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响, bbox=[50, 404, 466, 413]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[14]: text=睡眠,晨起有咽干,曾到本院就诊两次,症状不见明显缓解。2021-1-9血常规:白细胞:, bbox=[50, 417, 451, 426]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[15]: text=12.52*109/L 嗜酸粒细胞:0.65*109/L 5.2%,经治疗后症状明显缓解。无咳嗽、咯痰、气, bbox=[50, 430, 465, 439]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[16]: text=促。病情稳定,本次门诊距上次门诊间隔时间30天。症状控制情况:过去4周,患者:吸入, bbox=[50, 443, 464, 452]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[17]: text=药物使用情况:遵医嘱使用;吸入装置使用情况:正确。急性发作情况:两次,就诊期间急, bbox=[50, 456, 469, 465]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[18]: text=性发作:无,发作次数:0次。病情稳定无诉不适。流涕、鼻塞、喷嚏。长期规律使用信必, bbox=[50, 469, 465, 478]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[19]: text=可160/4.5ug 2吸 bid治疗,5天前开始出现咳嗽、咯痰,黄白痰,量少,难以咯出,咳嗽以, bbox=[50, 482, 472, 491]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[20]: text=夜间为主。无气促,伴咽息,鼻塞、流涕、喷嚏,无发热。, bbox=[50, 495, 319, 504]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[21]: text=既 往 史:鼻炎病史无规则治疗。打鼾明显。, bbox=[50, 508, 255, 517]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[22]: text=过 敏 史:未发现;, bbox=[50, 521, 140, 530]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[23]: text=个 人 史:否认遗传病史,吸烟10年,20支/日,2018年戒烟。偶饮酒。2021-12-20已打第, bbox=[50, 534, 471, 543]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[24]: text=三针新冠疫苗。, bbox=[50, 547, 118, 556]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[25]: text=体格检查:神志清,颈软,双肺呼吸音粗,可闻及散在哮鸣音,口腔粘膜无白斑。, bbox=[50, 560, 427, 570]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[26]: text=专科情况:, bbox=[50, 574, 97, 583]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[27]: text=辅助检查:, bbox=[50, 587, 97, 596]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[28]: text=治疗项目:, bbox=[50, 601, 97, 610]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[29]: text=门诊诊断:, bbox=[50, 615, 97, 624]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[30]: text=1、支气管哮喘(急性发作期),2、过敏性鼻炎[变应性鼻炎],3、急性气管支气管炎, bbox=[50, 631, 432, 640]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[31]: text=处 置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。, bbox=[50, 645, 377, 655]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[32]: text=布地奈德福莫特罗吸入粉雾剂(II)2盒 2.0吸,吸入用药,一天2次 30天, bbox=[109, 660, 458, 669]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[33]: text=(省采)●①⑤, bbox=[110, 674, 173, 683]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[34]: text=左氧氟沙星片(省采)●⑥ 5片 0.5g,口服,每日1次(口服) 5天, bbox=[109, 688, 460, 698]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[35]: text=第1页, bbox=[246, 706, 282, 714]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[36]: text=广州医科大学附属第三医院, bbox=[558, 245, 720, 258]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[37]: text=The Third Affiliated Hospital of Guangzhou Medical University, bbox=[558, 256, 720, 263]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[38]: text=门(急)诊病历信息, bbox=[654, 275, 786, 289]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[39]: text=复方甲氧那明胶囊(省采)●② 1瓶 1.0粒,餐后口服,一天3次(口服) 5天, bbox=[569, 309, 945, 319]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[40]: text=盐酸氨溴索分散片(省采)●⑥ 15片 30.0mg,餐后口服,一天3次(口服) 5, bbox=[569, 323, 941, 333]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[41]: text=天, bbox=[766, 336, 779, 345]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[42]: text=醋酸泼尼松片●②④ 6片 10.0mg,口服,每早1次(口服) 3天, bbox=[569, 350, 931, 360]
2026-08-05 05:12:00,592 INFO     29 [qwen-vl-text] coord item[43]: text=备 注:建议在住地附近社区医疗机构随诊。, bbox=[511, 363, 732, 372]
2026-08-05 05:12:00,593 INFO     29 [qwen-vl-text] page=13 — 44/44 coords, api_time=16.3s
2026-08-05 05:12:00,593 INFO     29 [qwen-vl-text] new_positions (44):
[[13, 58.309999999999995, 149.94, 210.5, 221.446], [13, 58.309999999999995, 149.94, 219.762, 225.656], [13, 111.86, 186.82999999999998, 235.76, 247.548], [13, 29.75, 48.79, 264.388, 271.966], [13, 29.75, 45.815, 275.334, 282.912], [13, 29.75, 36.89, 286.28, 293.858], [13, 176.12, 204.67999999999998, 275.334, 282.912], [13, 176.12, 217.76999999999998, 286.28, 293.858], [13, 29.75, 127.33, 297.226, 304.804], [13, 176.12, 265.37, 297.226, 304.804], [13, 29.75, 186.82999999999998, 307.33, 314.908], [13, 29.75, 273.7, 318.276, 325.854], [13, 29.75, 270.72499999999997, 329.222, 336.8], [13, 29.75, 277.27, 340.168, 347.746], [13, 29.75, 268.34499999999997, 351.114, 358.692], [13, 29.75, 276.675, 362.06, 369.638], [13, 29.75, 276.08, 373.006, 380.584], [13, 29.75, 279.055, 383.952, 391.53], [13, 29.75, 276.675, 394.89799999999997, 402.476], [13, 29.75, 280.84, 405.844, 413.42199999999997], [13, 29.75, 189.80499999999998, 416.78999999999996, 424.368], [13, 29.75, 151.725, 427.736, 435.31399999999996], [13, 29.75, 83.3, 438.68199999999996, 446.26], [13, 29.75, 280.245, 449.628, 457.20599999999996], [13, 29.75, 70.21, 460.574, 468.152], [13, 29.75, 254.065, 471.52, 479.94], [13, 29.75, 57.714999999999996, 483.308, 490.88599999999997], [13, 29.75, 57.714999999999996, 494.25399999999996, 501.832], [13, 29.75, 57.714999999999996, 506.042, 513.62], [13, 29.75, 57.714999999999996, 517.8299999999999, 525.408], [13, 29.75, 257.03999999999996, 531.302, 538.88], [13, 29.75, 224.315, 543.09, 551.51], [13, 64.855, 272.51, 555.72, 563.298], [13, 65.45, 102.935, 567.5079999999999, 575.086], [13, 64.855, 273.7, 579.2959999999999, 587.716], [13, 146.37, 167.79, 594.452, 601.188], [13, 332.01, 428.4, 206.29, 217.236], [13, 332.01, 428.4, 215.552, 221.446], [13, 389.13, 467.66999999999996, 231.54999999999998, 243.338], [13, 338.555, 562.275, 260.178, 268.598], [13, 338.555, 559.895, 271.966, 280.38599999999997], [13, 455.77, 463.505, 282.912, 290.49], [13, 338.555, 553.9449999999999, 294.7, 303.12], [13, 304.04499999999996, 435.53999999999996, 305.646, 313.224]]
2026-08-05 05:12:00,593 INFO     29 [qwen-vl-text] ═══ DONE ═══ 44 positions, pages=1, time=26.1s
2026-08-05 05:12:00,593 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:12:00,593 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 05:12:00,593 INFO     29 [qwen-vl-text] positions(27): [[14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:12:00,593 INFO     29 [qwen-vl-text] page grouping: [14], lines per page: [27]
2026-08-05 05:12:00,803 INFO     29 [qwen-vl-text] page=14, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:12:00,804 INFO     29 [qwen-vl-text] LLM extraction start, text_len=718
2026-08-05 05:12:00,804 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:12:00,804 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 769, \"bbox_end\": 795, \"encounter_dates\": [\"2026-02-04\"], \"department\": \"内科门诊（荔湾）\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊/住院病历信息\n就诊卡号：\n病历编号：\n姓名：\n性别：男\n年龄：41岁\n就诊科室：内科门诊（荔湾）\n就诊时间：2026-02-04 11:21:11\n主诉：支气管哮喘治疗后复查\n现病史：2021年2月前开始出现咳嗽、咳痰，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sg 2吸 bid治疗。\n既往史：鼻炎病史无规则治疗，打鼾明显。\n过敏史：未发现；\n个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。\n体格检查：神志清，颈软，双肺呼吸音粗，可闻及散在哮鸣音，口腔粘膜无白斑。\n专科情况：\n辅助检查：\n治疗项目：\n门诊诊断：\n1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、急性气管支气管炎\n单病种：\n发病时间：\n处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不遥随诊。\n布地奈德福莫特罗吸入粉雾剂(II)(省\n2 2.0班，吸入用药，一天2次\n30\n采)●①②\n查天",
    "role": "user"
  }
]
[92m05:12:00 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:12:00,806 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:12:06,443 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:12:06,443 INFO     29 [qwen-vl-text] LLM output (len=655):
{
  "encounter_date": "2026-02-04",
  "chief_complaint": "支气管哮喘治疗后复查",
  "present_illness": "2021年2月前开始出现咳嗽、咳痰，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sg 2吸 bid治疗。",
  "past_history": "鼻炎病史无规则治疗，打鼾明显。过敏史：未发现；个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。",
  "diagnosis": "1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、急性气管支气管炎",
  "treatment_plan": "布地奈德福莫特罗吸入粉雾剂(II) 2吸 吸入用药 一天2次"
}
2026-08-05 05:12:06,443 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-04]
2026-08-05 05:12:06,446 INFO     29 [qwen-vl-text] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1605519, prompt_len=1412
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共27行）
["门诊/住院病历信息", "就诊卡号：", "病历编号：", "姓名：", "性别：男", "年龄：41岁", "就诊科室：内科门诊（荔湾）", "就诊时间：2026-02-04 11:21:11", "主诉：支气管哮喘治疗后复查", "现病史：2021年2月前开始出现咳嗽、咳痰，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sg 2吸 bid治疗。", "既往史：鼻炎病史无规则治疗，打鼾明显。", "过敏史：未发现；", "个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。", "体格检查：神志清，颈软，双肺呼吸音粗，可闻及散在哮鸣音，口腔粘膜无白斑。", "专科情况：", "辅助检查：", "治疗项目：", "门诊诊断：", "1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、急性气管支气管炎", "单病种：", "发病时间：", "处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不遥随诊。", "布地奈德福莫特罗吸入粉雾剂(II)(省", "2 2.0班，吸入用药，一天2次", "30", "采)●①②", "查天"]

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
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord API raw response (len=1939):
[
	{"text": "门诊/住院病历信息", "bbox": [338, 155, 525, 169]},
	{"text": "就诊卡号：", "bbox": [187, 194, 262, 207], "bbox": [187, 194, 262, 207]},
	{"text": "病历编号：", "bbox": [509, 220, 577, 233]},
	{"text": "姓名：", "bbox": [187, 246, 202, 259]},
	{"text": "性别：男", "bbox": [431, 246, 475, 259]},
	{"text": "年龄：41岁", "bbox": [585, 246, 639, 259]},
	{"text": "就诊科室：内科门诊（荔湾）", "bbox": [187, 271, 373, 284]},
	{"text": "就诊时间：2026-02-04 11:21:11", "bbox": [517, 271, 732, 284]},
	{"text": "主诉：支气管哮喘治疗后复查", "bbox": [187, 297, 465, 310]},
	{"text": "现病史：2021年2月前开始出现咳嗽、咳痰，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sg 2吸 bid治疗。", "bbox": [187, 323, 775, 467]},
	{"text": "既往史：鼻炎病史无规则治疗，打鼾明显。", "bbox": [187, 477, 507, 490]},
	{"text": "过敏史：未发现；", "bbox": [187, 502, 339, 515]},
	{"text": "个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。", "bbox": [187, 526, 762, 554]},
	{"text": "体格检查：神志清，颈软，双肺呼吸音粗，可闻及散在哮鸣音，口腔粘膜无白斑。", "bbox": [187, 567, 727, 580]},
	{"text": "专科情况：", "bbox": [187, 591, 258, 604]},
	{"text": "辅助检查：", "bbox": [187, 615, 258, 628]},
	{"text": "治疗项目：", "bbox": [187, 639, 258, 652]},
	{"text": "门诊诊断：", "bbox": [187, 663, 258, 676]},
	{"text": "1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、急性气管支气管炎", "bbox": [207, 687, 645, 699]},
	{"text": "单病种：", "bbox": [187, 710, 273, 723]},
	{"text": "发病时间：", "bbox": [187, 733, 258, 746]},
	{"text": "处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不遥随诊。", "bbox": [269, 755, 677, 767]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(II)(省", "bbox": [217, 779, 461, 791]},
	{"text": "2 2.0班，吸入用药，一天2次", "bbox": [519, 779, 703, 791]},
	{"text": "30", "bbox": [732, 779, 746, 789]},
	{"text": "采)●①②", "bbox": [217, 795, 283, 807]},
	{"text": "查天", "bbox": [519, 795, 555, 807]}
]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord API: raw_items=27, valid_items=27, elapsed=14.2s
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[0]: text=门诊/住院病历信息, bbox=[338, 155, 525, 169]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[1]: text=就诊卡号：, bbox=[187, 194, 262, 207]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[2]: text=病历编号：, bbox=[509, 220, 577, 233]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[187, 246, 202, 259]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[4]: text=性别：男, bbox=[431, 246, 475, 259]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：41岁, bbox=[585, 246, 639, 259]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[6]: text=就诊科室：内科门诊（荔湾）, bbox=[187, 271, 373, 284]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[7]: text=就诊时间：2026-02-04 11:21:11, bbox=[517, 271, 732, 284]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[8]: text=主诉：支气管哮喘治疗后复查, bbox=[187, 297, 465, 310]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[9]: text=现病史：2021年2月前开始出现咳嗽、咳痰，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sg 2吸 bid治疗。, bbox=[187, 323, 775, 467]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[10]: text=既往史：鼻炎病史无规则治疗，打鼾明显。, bbox=[187, 477, 507, 490]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[11]: text=过敏史：未发现；, bbox=[187, 502, 339, 515]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[12]: text=个人史：否认遗传病史，吸烟10年，20支/日，2016年戒烟，偶饮酒，2021-12-20已打第三针新冠疫苗。, bbox=[187, 526, 762, 554]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[13]: text=体格检查：神志清，颈软，双肺呼吸音粗，可闻及散在哮鸣音，口腔粘膜无白斑。, bbox=[187, 567, 727, 580]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[14]: text=专科情况：, bbox=[187, 591, 258, 604]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[15]: text=辅助检查：, bbox=[187, 615, 258, 628]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[16]: text=治疗项目：, bbox=[187, 639, 258, 652]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[17]: text=门诊诊断：, bbox=[187, 663, 258, 676]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[18]: text=1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、急性气管支气管炎, bbox=[207, 687, 645, 699]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[19]: text=单病种：, bbox=[187, 710, 273, 723]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[20]: text=发病时间：, bbox=[187, 733, 258, 746]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[21]: text=处置：请仔细阅读药品说明书等文书资料，遵嘱诊疗，不遥随诊。, bbox=[269, 755, 677, 767]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[22]: text=布地奈德福莫特罗吸入粉雾剂(II)(省, bbox=[217, 779, 461, 791]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[23]: text=2 2.0班，吸入用药，一天2次, bbox=[519, 779, 703, 791]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[24]: text=30, bbox=[732, 779, 746, 789]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[25]: text=采)●①②, bbox=[217, 795, 283, 807]
2026-08-05 05:12:20,605 INFO     29 [qwen-vl-text] coord item[26]: text=查天, bbox=[519, 795, 555, 807]
2026-08-05 05:12:20,606 INFO     29 [qwen-vl-text] page=14 — 27/27 coords, api_time=14.2s
2026-08-05 05:12:20,606 INFO     29 [qwen-vl-text] new_positions (27):
[[14, 201.10999999999999, 312.375, 130.51, 142.298], [14, 111.265, 155.89, 163.34799999999998, 174.29399999999998], [14, 302.85499999999996, 343.315, 185.23999999999998, 196.186], [14, 111.265, 120.19, 207.132, 218.078], [14, 256.445, 282.625, 207.132, 218.078], [14, 348.075, 380.205, 207.132, 218.078], [14, 111.265, 221.935, 228.182, 239.128], [14, 307.615, 435.53999999999996, 228.182, 239.128], [14, 111.265, 276.675, 250.07399999999998, 261.02], [14, 111.265, 461.125, 271.966, 393.214], [14, 111.265, 301.66499999999996, 401.63399999999996, 412.58], [14, 111.265, 201.70499999999998, 422.68399999999997, 433.63], [14, 111.265, 453.39, 442.892, 466.46799999999996], [14, 111.265, 432.565, 477.414, 488.35999999999996], [14, 111.265, 153.51, 497.62199999999996, 508.568], [14, 111.265, 153.51, 517.8299999999999, 528.776], [14, 111.265, 153.51, 538.038, 548.984], [14, 111.265, 153.51, 558.246, 569.192], [14, 123.16499999999999, 383.775, 578.454, 588.558], [14, 111.265, 162.435, 597.8199999999999, 608.766], [14, 111.265, 153.51, 617.1859999999999, 628.132], [14, 160.055, 402.815, 635.7099999999999, 645.814], [14, 129.11499999999998, 274.295, 655.918, 666.0219999999999], [14, 308.805, 418.28499999999997, 655.918, 666.0219999999999], [14, 435.53999999999996, 443.87, 655.918, 664.338], [14, 129.11499999999998, 168.385, 669.39, 679.494], [14, 308.805, 330.22499999999997, 669.39, 679.494]]
2026-08-05 05:12:20,606 INFO     29 [qwen-vl-text] ═══ DONE ═══ 27 positions, pages=1, time=20.0s
2026-08-05 05:12:20,618 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-05 05:12:20,618 INFO     29 [Trace] task=4e4700ce | doc=LZK 哮喘 广三(1).pdf | Extractor:Clinical | outputs={"chunks": "3 items, types={'OutpatientRecord': 3}", "html": "", "json": "3681 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-05 05:12:20,618 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-05 05:12:20,619 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:12:20.618+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 15, "failed": 0, "current": {"4e4700ce908b11f1a3da71efcdd7cc1f": {"id": "4e4700ce908b11f1a3da71efcdd7cc1f", "doc_id": "4e10ceb4908b11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906341337, "task_type": "dataflow", "root_trace_id": "ca345e6640ff4d788f444c3ab712853e", "root_traceparent": "00-ca345e6640ff4d788f444c3ab712853e-8ea193cced1ce3aa-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:12:20,624 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:12:20,625 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m05:12:20 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:12:20,626 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:12:21,486 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:12:21,495 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-05 05:12:21,496 INFO     29 [Trace] task=4e4700ce | doc=LZK 哮喘 广三(1).pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "3681 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-05 05:12:21,496 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-05 05:12:21,502 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:12:21,502 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 05:12:21,502 INFO     29 [qwen-vl-text] positions(26): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:12:21,503 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [26]
2026-08-05 05:12:21,649 INFO     29 [qwen-vl-text] page=4, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:12:21,651 INFO     29 [qwen-vl-text] LLM extraction start, text_len=198
2026-08-05 05:12:21,651 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:12:21,652 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 122, \"bbox_end\": 147, \"encounter_dates\": [\"2025-07-18\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-07-18\n就诊科室:内科门诊\n主诊医\n姓名\n性别:男\n年龄:40岁\n卡号:\n患者\n医疗证号:\n处方号\n地址:PT027气雾剂 2024017-呼吸科\n身份证\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n布地奈德福莫特罗吸入粉雾剂0.125/0.006*60吸6盒\n183.41100.46\nSig\n2吸/次,吸入,bid*90天",
    "role": "user"
  }
]
[92m05:12:21 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:12:21,654 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:12:23,877 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:12:23,877 INFO     29 [qwen-vl-text] LLM output (len=422):
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
2026-08-05 05:12:23,877 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-07-18]
2026-08-05 05:12:23,879 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=919286, prompt_len=889
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
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord API raw response (len=1335):
[
	{"text": "门(急)诊处方", "bbox": [385, 24, 624, 91]},
	{"text": "就诊时间:2025-07-18", "bbox": [38, 117, 284, 150]},
	{"text": "就诊科室:内科门诊", "bbox": [320, 117, 531, 150]},
	{"text": "主诊医", "bbox": [617, 117, 684, 150]},
	{"text": "姓名", "bbox": [38, 170, 85, 203]},
	{"text": "性别:男", "bbox": [320, 170, 407, 203]},
	{"text": "年龄:40岁", "bbox": [457, 170, 567, 203]},
	{"text": "卡号:", "bbox": [617, 170, 677, 203]},
	{"text": "患者", "bbox": [38, 222, 85, 255]},
	{"text": "医疗证号:", "bbox": [320, 222, 426, 255]},
	{"text": "处方号", "bbox": [613, 224, 684, 257]},
	{"text": "地址:PT027气雾剂 2024017-呼吸科", "bbox": [38, 275, 436, 309]},
	{"text": "身份证", "bbox": [612, 275, 682, 309]},
	{"text": "诊断:支气管哮喘", "bbox": [38, 324, 222, 357]},
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
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=7.2s
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[385, 24, 624, 91]
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-07-18, bbox=[38, 117, 284, 150]
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[320, 117, 531, 150]
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord item[3]: text=主诊医, bbox=[617, 117, 684, 150]
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[38, 170, 85, 203]
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[320, 170, 407, 203]
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:40岁, bbox=[457, 170, 567, 203]
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord item[7]: text=卡号:, bbox=[617, 170, 677, 203]
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord item[8]: text=患者, bbox=[38, 222, 85, 255]
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[320, 222, 426, 255]
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord item[10]: text=处方号, bbox=[613, 224, 684, 257]
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord item[11]: text=地址:PT027气雾剂 2024017-呼吸科, bbox=[38, 275, 436, 309]
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord item[12]: text=身份证, bbox=[612, 275, 682, 309]
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[38, 324, 222, 357]
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[434, 383, 564, 416]
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[107, 444, 156, 477]
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[215, 444, 314, 477]
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[506, 444, 550, 477]
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[709, 444, 755, 477]
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[812, 444, 858, 477]
2026-08-05 05:12:31,107 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[893, 444, 938, 477]
2026-08-05 05:12:31,108 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[60, 504, 108, 554]
2026-08-05 05:12:31,108 INFO     29 [qwen-vl-text] coord item[22]: text=布地奈德福莫特罗吸入粉雾剂0.125/0.006*60吸6盒, bbox=[195, 498, 737, 531]
2026-08-05 05:12:31,108 INFO     29 [qwen-vl-text] coord item[23]: text=183.41100.46, bbox=[767, 500, 923, 528]
2026-08-05 05:12:31,108 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[424, 550, 461, 580]
2026-08-05 05:12:31,108 INFO     29 [qwen-vl-text] coord item[25]: text=2吸/次,吸入,bid*90天, bbox=[504, 548, 747, 580]
2026-08-05 05:12:31,108 INFO     29 [qwen-vl-text] page=4 — 26/26 coords, api_time=7.2s
2026-08-05 05:12:31,108 INFO     29 [qwen-vl-text] new_positions (26):
[[4, 324.17, 525.408, 14.28, 54.144999999999996], [4, 31.996, 239.128, 69.615, 89.25], [4, 269.44, 447.102, 69.615, 89.25], [4, 519.514, 575.928, 69.615, 89.25], [4, 31.996, 71.57, 101.14999999999999, 120.785], [4, 269.44, 342.69399999999996, 101.14999999999999, 120.785], [4, 384.794, 477.414, 101.14999999999999, 120.785], [4, 519.514, 570.034, 101.14999999999999, 120.785], [4, 31.996, 71.57, 132.09, 151.725], [4, 269.44, 358.692, 132.09, 151.725], [4, 516.146, 575.928, 133.28, 152.915], [4, 31.996, 367.11199999999997, 163.625, 183.855], [4, 515.304, 574.244, 163.625, 183.855], [4, 31.996, 186.924, 192.78, 212.415], [4, 365.428, 474.888, 227.885, 247.51999999999998], [4, 90.094, 131.352, 264.18, 283.815], [4, 181.03, 264.388, 264.18, 283.815], [4, 426.05199999999996, 463.09999999999997, 264.18, 283.815], [4, 596.978, 635.7099999999999, 264.18, 283.815], [4, 683.704, 722.4359999999999, 264.18, 283.815], [4, 751.906, 789.7959999999999, 264.18, 283.815], [4, 50.519999999999996, 90.93599999999999, 299.88, 329.63], [4, 164.19, 620.554, 296.31, 315.945], [4, 645.814, 777.1659999999999, 297.5, 314.15999999999997], [4, 357.008, 388.162, 327.25, 345.09999999999997], [4, 424.368, 628.9739999999999, 326.06, 345.09999999999997]]
2026-08-05 05:12:31,108 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=9.6s
2026-08-05 05:12:31,108 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:12:31,108 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 05:12:31,108 INFO     29 [qwen-vl-text] positions(26): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:12:31,108 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [26]
2026-08-05 05:12:31,262 INFO     29 [qwen-vl-text] page=5, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:12:31,263 INFO     29 [qwen-vl-text] LLM extraction start, text_len=205
2026-08-05 05:12:31,263 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:12:31,263 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 148, \"bbox_end\": 173, \"encounter_dates\": [\"2025-04-25\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-04-25\n就诊科室:内科门诊\n主诊\n姓名\n性别:男\n年龄:40岁\n卡号:\n患者类型:GLP支付\n医疗证号:\n处方号\n地址:PT027气雾剂 2024017-呼吸科\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n布地奈德福莫特罗吸入粉雾剂(II)0.5mg*60吸6盒\n183.41100.46\nSig\n2吸/次,吸入,bid*90天",
    "role": "user"
  }
]
[92m05:12:31 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:12:31,264 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:12:33,933 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:12:33,934 INFO     29 [qwen-vl-text] LLM output (len=420):
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
      "dosage": "0.5mg",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 90,
      "quantity": "6盒",
      "notes": "2吸/次"
    }
  ]
}
2026-08-05 05:12:33,934 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-04-25]
2026-08-05 05:12:33,935 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=892488, prompt_len=896
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["门(急)诊处方", "就诊时间:2025-04-25", "就诊科室:内科门诊", "主诊", "姓名", "性别:男", "年龄:40岁", "卡号:", "患者类型:GLP支付", "医疗证号:", "处方号", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂(II)0.5mg*60吸6盒", "183.41100.46", "Sig", "2吸/次,吸入,bid*90天"]

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
2026-08-05 05:12:43,854 INFO     29 [qwen-vl-text] coord API raw response (len=1343):
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
	{"text": "布地奈德福莫特罗吸入粉雾剂(II)0.5mg*60吸6盒", "bbox": [204, 517, 731, 552]},
	{"text": "183.41100.46", "bbox": [760, 517, 919, 548]},
	{"text": "Sig", "bbox": [424, 570, 462, 604]},
	{"text": "2吸/次,吸入,bid*90天", "bbox": [503, 568, 743, 603]}
]
2026-08-05 05:12:43,855 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=9.9s
2026-08-05 05:12:43,855 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[375, 21, 604, 88]
2026-08-05 05:12:43,855 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-04-25, bbox=[48, 117, 283, 153]
2026-08-05 05:12:43,855 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[317, 115, 518, 150]
2026-08-05 05:12:43,855 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[601, 115, 661, 150]
2026-08-05 05:12:43,855 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[48, 172, 97, 207]
2026-08-05 05:12:43,855 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[317, 170, 401, 205]
2026-08-05 05:12:43,855 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:40岁, bbox=[448, 170, 555, 205]
2026-08-05 05:12:43,855 INFO     29 [qwen-vl-text] coord item[7]: text=卡号:, bbox=[601, 170, 655, 205]
2026-08-05 05:12:43,855 INFO     29 [qwen-vl-text] coord item[8]: text=患者类型:GLP支付, bbox=[50, 228, 245, 262]
2026-08-05 05:12:43,855 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[318, 227, 421, 262]
2026-08-05 05:12:43,855 INFO     29 [qwen-vl-text] coord item[10]: text=处方号, bbox=[601, 227, 661, 262]
2026-08-05 05:12:43,855 INFO     29 [qwen-vl-text] coord item[11]: text=地址:PT027气雾剂 2024017-呼吸科, bbox=[50, 280, 432, 317]
2026-08-05 05:12:43,855 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[601, 280, 704, 315]
2026-08-05 05:12:43,855 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[51, 333, 229, 368]
2026-08-05 05:12:43,855 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[431, 393, 559, 428]
2026-08-05 05:12:43,855 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[119, 458, 167, 493]
2026-08-05 05:12:43,855 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[223, 458, 317, 493]
2026-08-05 05:12:43,855 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[503, 458, 546, 491]
2026-08-05 05:12:43,855 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[702, 458, 748, 491]
2026-08-05 05:12:43,855 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[805, 456, 851, 491]
2026-08-05 05:12:43,856 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[886, 456, 933, 491]
2026-08-05 05:12:43,856 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[74, 522, 120, 575]
2026-08-05 05:12:43,856 INFO     29 [qwen-vl-text] coord item[22]: text=布地奈德福莫特罗吸入粉雾剂(II)0.5mg*60吸6盒, bbox=[204, 517, 731, 552]
2026-08-05 05:12:43,856 INFO     29 [qwen-vl-text] coord item[23]: text=183.41100.46, bbox=[760, 517, 919, 548]
2026-08-05 05:12:43,856 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[424, 570, 462, 604]
2026-08-05 05:12:43,856 INFO     29 [qwen-vl-text] coord item[25]: text=2吸/次,吸入,bid*90天, bbox=[503, 568, 743, 603]
2026-08-05 05:12:43,856 INFO     29 [qwen-vl-text] page=5 — 26/26 coords, api_time=9.9s
2026-08-05 05:12:43,856 INFO     29 [qwen-vl-text] new_positions (26):
[[5, 315.75, 508.568, 12.495, 52.36], [5, 40.416, 238.286, 69.615, 91.035], [5, 266.914, 436.156, 68.425, 89.25], [5, 506.042, 556.562, 68.425, 89.25], [5, 40.416, 81.67399999999999, 102.33999999999999, 123.16499999999999], [5, 266.914, 337.642, 101.14999999999999, 121.975], [5, 377.216, 467.31, 101.14999999999999, 121.975], [5, 506.042, 551.51, 101.14999999999999, 121.975], [5, 42.1, 206.29, 135.66, 155.89], [5, 267.756, 354.48199999999997, 135.065, 155.89], [5, 506.042, 556.562, 135.065, 155.89], [5, 42.1, 363.74399999999997, 166.6, 188.61499999999998], [5, 506.042, 592.768, 166.6, 187.42499999999998], [5, 42.942, 192.81799999999998, 198.135, 218.95999999999998], [5, 362.902, 470.678, 233.83499999999998, 254.66], [5, 100.198, 140.614, 272.51, 293.335], [5, 187.766, 266.914, 272.51, 293.335], [5, 423.526, 459.73199999999997, 272.51, 292.145], [5, 591.084, 629.816, 272.51, 292.145], [5, 677.81, 716.542, 271.32, 292.145], [5, 746.012, 785.586, 271.32, 292.145], [5, 62.308, 101.03999999999999, 310.59, 342.125], [5, 171.768, 615.502, 307.615, 328.44], [5, 639.92, 773.798, 307.615, 326.06], [5, 357.008, 389.00399999999996, 339.15, 359.38], [5, 423.526, 625.606, 337.96, 358.78499999999997]]
2026-08-05 05:12:43,856 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=12.7s
2026-08-05 05:12:43,856 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:12:43,856 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 05:12:43,856 INFO     29 [qwen-vl-text] positions(26): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:12:43,857 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [26]
2026-08-05 05:12:44,009 INFO     29 [qwen-vl-text] page=6, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:12:44,009 INFO     29 [qwen-vl-text] LLM extraction start, text_len=193
2026-08-05 05:12:44,009 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:12:44,010 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 174, \"bbox_end\": 199, \"encounter_dates\": [\"2025-02-26\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间：2025-02-26\n就诊科室：内科门诊\n主诊\n性别：男\n年龄：40岁\n卡号\n医疗证号：\n处方\n015\n地址：PT027气雾剂 2024017-呼吸科\n身份证号：\n诊断：支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n布地奈德福莫特罗吸入粉雾剂BDI/●@1g*60吸2盒\n183.41\n366.82\nSig\n2吸/次,吸入,bid*30天",
    "role": "user"
  }
]
[92m05:12:44 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:12:44,011 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:12:46,497 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:12:46,497 INFO     29 [qwen-vl-text] LLM output (len=413):
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
2026-08-05 05:12:46,497 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-02-26]
2026-08-05 05:12:46,498 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=825853, prompt_len=884
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["门(急)诊处方", "就诊时间：2025-02-26", "就诊科室：内科门诊", "主诊", "性别：男", "年龄：40岁", "卡号", "医疗证号：", "处方", "015", "地址：PT027气雾剂 2024017-呼吸科", "身份证号：", "诊断：支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂BDI/●@1g*60吸2盒", "183.41", "366.82", "Sig", "2吸/次,吸入,bid*30天"]

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
2026-08-05 05:12:53,775 INFO     29 [qwen-vl-text] coord API raw response (len=1334):
[
	{"text": "门(急)诊处方", "bbox": [394, 28, 630, 94]},
	{"text": "就诊时间：2025-02-26", "bbox": [54, 123, 294, 153]},
	{"text": "就诊科室：内科门诊", "bbox": [330, 120, 537, 155]},
	{"text": "主诊", "bbox": [623, 122, 667, 156]},
	{"text": "性别：男", "bbox": [330, 175, 415, 209]},
	{"text": "年龄：40岁", "bbox": [464, 175, 573, 209]},
	{"text": "卡号", "bbox": [621, 175, 667, 209]},
	{"text": "医疗证号：", "bbox": [330, 230, 435, 264]},
	{"text": "处方", "bbox": [619, 230, 667, 264]},
	{"text": "015", "bbox": [900, 228, 939, 258]},
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
	{"text": "R:", "bbox": [75, 513, 121, 565]},
	{"text": "布地奈德福莫特罗吸入粉雾剂BDI/●@1g*60吸2盒", "bbox": [206, 507, 744, 541]},
	{"text": "183.41", "bbox": [775, 508, 848, 536]},
	{"text": "366.82", "bbox": [857, 508, 932, 536]},
	{"text": "Sig", "bbox": [432, 558, 469, 589]},
	{"text": "2吸/次,吸入,bid*30天", "bbox": [511, 557, 754, 589]}
]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=7.3s
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[394, 28, 630, 94]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间：2025-02-26, bbox=[54, 123, 294, 153]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室：内科门诊, bbox=[330, 120, 537, 155]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[623, 122, 667, 156]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[4]: text=性别：男, bbox=[330, 175, 415, 209]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：40岁, bbox=[464, 175, 573, 209]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[6]: text=卡号, bbox=[621, 175, 667, 209]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[7]: text=医疗证号：, bbox=[330, 230, 435, 264]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[8]: text=处方, bbox=[619, 230, 667, 264]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[9]: text=015, bbox=[900, 228, 939, 258]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[10]: text=地址：PT027气雾剂 2024017-呼吸科, bbox=[54, 281, 444, 316]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[11]: text=身份证号：, bbox=[618, 281, 721, 316]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[12]: text=诊断：支气管哮喘, bbox=[55, 331, 235, 366]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[13]: text=西药处方, bbox=[442, 390, 571, 423]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[14]: text=组号, bbox=[120, 452, 169, 485]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[15]: text=项目名称, bbox=[227, 452, 324, 485]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[16]: text=规格, bbox=[514, 451, 557, 483]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[17]: text=总量, bbox=[716, 451, 763, 483]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[18]: text=单价, bbox=[820, 451, 866, 483]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[19]: text=金额, bbox=[902, 450, 948, 483]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[20]: text=R:, bbox=[75, 513, 121, 565]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[21]: text=布地奈德福莫特罗吸入粉雾剂BDI/●@1g*60吸2盒, bbox=[206, 507, 744, 541]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[22]: text=183.41, bbox=[775, 508, 848, 536]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[23]: text=366.82, bbox=[857, 508, 932, 536]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[432, 558, 469, 589]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] coord item[25]: text=2吸/次,吸入,bid*30天, bbox=[511, 557, 754, 589]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] page=6 — 26/26 coords, api_time=7.3s
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] new_positions (26):
[[6, 331.748, 530.46, 16.66, 55.93], [6, 45.467999999999996, 247.548, 73.185, 91.035], [6, 277.86, 452.154, 71.39999999999999, 92.225], [6, 524.566, 561.614, 72.59, 92.82], [6, 277.86, 349.43, 104.125, 124.35499999999999], [6, 390.688, 482.466, 104.125, 124.35499999999999], [6, 522.882, 561.614, 104.125, 124.35499999999999], [6, 277.86, 366.27, 136.85, 157.07999999999998], [6, 521.198, 561.614, 136.85, 157.07999999999998], [6, 757.8, 790.6379999999999, 135.66, 153.51], [6, 45.467999999999996, 373.848, 167.195, 188.01999999999998], [6, 520.356, 607.082, 167.195, 188.01999999999998], [6, 46.309999999999995, 197.87, 196.945, 217.76999999999998], [6, 372.164, 480.782, 232.04999999999998, 251.685], [6, 101.03999999999999, 142.298, 268.94, 288.575], [6, 191.134, 272.808, 268.94, 288.575], [6, 432.788, 468.99399999999997, 268.34499999999997, 287.385], [6, 602.872, 642.446, 268.34499999999997, 287.385], [6, 690.4399999999999, 729.172, 268.34499999999997, 287.385], [6, 759.4839999999999, 798.216, 267.75, 287.385], [6, 63.15, 101.88199999999999, 305.235, 336.175], [6, 173.452, 626.448, 301.66499999999996, 321.895], [6, 652.55, 714.016, 302.26, 318.91999999999996], [6, 721.5939999999999, 784.744, 302.26, 318.91999999999996], [6, 363.74399999999997, 394.89799999999997, 332.01, 350.455], [6, 430.262, 634.8679999999999, 331.41499999999996, 350.455]]
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=9.9s
2026-08-05 05:12:53,776 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:12:53,776 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 05:12:53,777 INFO     29 [qwen-vl-text] positions(26): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:12:53,777 INFO     29 [qwen-vl-text] page grouping: [7], lines per page: [26]
2026-08-05 05:12:53,924 INFO     29 [qwen-vl-text] page=7, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:12:53,925 INFO     29 [qwen-vl-text] LLM extraction start, text_len=209
2026-08-05 05:12:53,925 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:12:53,926 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 200, \"bbox_end\": 225, \"encounter_dates\": [\"2025-01-24\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-01-24\n就诊科室:内科门诊\n主诊医\n姓名\n性别:男\n年龄:40岁\n卡号:4\n患者类型:GCP支付\n医疗证号:\n处方号:\n地址:PT027气雾剂 2024017-呼吸科\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n布地奈德福莫特罗吸入粉雾剂HIV●(50ug*60吸4盒\n183.41 733.64\nSig\n2吸/次,吸入,bid*60天",
    "role": "user"
  }
]
[92m05:12:53 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:12:53,927 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:12:53,928 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:12:53.926+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 15, "failed": 0, "current": {"4e4700ce908b11f1a3da71efcdd7cc1f": {"id": "4e4700ce908b11f1a3da71efcdd7cc1f", "doc_id": "4e10ceb4908b11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906341337, "task_type": "dataflow", "root_trace_id": "ca345e6640ff4d788f444c3ab712853e", "root_traceparent": "00-ca345e6640ff4d788f444c3ab712853e-8ea193cced1ce3aa-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:12:56,423 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:12:56,424 INFO     29 [qwen-vl-text] LLM output (len=415):
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
      "dosage": "50ug",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 60,
      "quantity": "4盒",
      "notes": "2吸/次"
    }
  ]
}
2026-08-05 05:12:56,424 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-01-24]
2026-08-05 05:12:56,425 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=834734, prompt_len=900
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["门(急)诊处方", "就诊时间:2025-01-24", "就诊科室:内科门诊", "主诊医", "姓名", "性别:男", "年龄:40岁", "卡号:4", "患者类型:GCP支付", "医疗证号:", "处方号:", "地址:PT027气雾剂 2024017-呼吸科", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "布地奈德福莫特罗吸入粉雾剂HIV●(50ug*60吸4盒", "183.41 733.64", "Sig", "2吸/次,吸入,bid*60天"]

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
2026-08-05 05:13:03,672 INFO     29 [qwen-vl-text] coord API raw response (len=1348):
[
	{"text": "门(急)诊处方", "bbox": [385, 24, 604, 87]},
	{"text": "就诊时间:2025-01-24", "bbox": [69, 112, 294, 146]},
	{"text": "就诊科室:内科门诊", "bbox": [327, 112, 521, 146]},
	{"text": "主诊医", "bbox": [601, 112, 671, 146]},
	{"text": "姓名", "bbox": [69, 164, 110, 198]},
	{"text": "性别:男", "bbox": [327, 164, 408, 198]},
	{"text": "年龄:40岁", "bbox": [454, 164, 557, 198]},
	{"text": "卡号:4", "bbox": [601, 164, 673, 198]},
	{"text": "患者类型:GCP支付", "bbox": [69, 216, 259, 250]},
	{"text": "医疗证号:", "bbox": [327, 216, 428, 250]},
	{"text": "处方号:", "bbox": [600, 216, 670, 250]},
	{"text": "地址:PT027气雾剂 2024017-呼吸科", "bbox": [69, 267, 437, 301]},
	{"text": "身份证号:", "bbox": [600, 267, 695, 301]},
	{"text": "诊断:支气管哮喘", "bbox": [70, 317, 240, 351]},
	{"text": "西药处方", "bbox": [436, 375, 560, 409]},
	{"text": "组号", "bbox": [132, 436, 178, 470]},
	{"text": "项目名称", "bbox": [232, 436, 325, 470]},
	{"text": "规格", "bbox": [505, 436, 547, 470]},
	{"text": "总量", "bbox": [697, 436, 740, 470]},
	{"text": "单价", "bbox": [795, 436, 838, 470]},
	{"text": "金额", "bbox": [870, 436, 914, 470]},
	{"text": "R:", "bbox": [89, 497, 134, 548]},
	{"text": "布地奈德福莫特罗吸入粉雾剂HIV●(50ug*60吸4盒", "bbox": [213, 493, 724, 527]},
	{"text": "183.41 733.64", "bbox": [752, 495, 902, 523]},
	{"text": "Sig", "bbox": [428, 545, 465, 575]},
	{"text": "2吸/次,吸入,bid*60天", "bbox": [504, 545, 735, 575]}
]
2026-08-05 05:13:03,672 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=7.2s
2026-08-05 05:13:03,672 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[385, 24, 604, 87]
2026-08-05 05:13:03,672 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-01-24, bbox=[69, 112, 294, 146]
2026-08-05 05:13:03,672 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[327, 112, 521, 146]
2026-08-05 05:13:03,672 INFO     29 [qwen-vl-text] coord item[3]: text=主诊医, bbox=[601, 112, 671, 146]
2026-08-05 05:13:03,672 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[69, 164, 110, 198]
2026-08-05 05:13:03,672 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[327, 164, 408, 198]
2026-08-05 05:13:03,672 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:40岁, bbox=[454, 164, 557, 198]
2026-08-05 05:13:03,672 INFO     29 [qwen-vl-text] coord item[7]: text=卡号:4, bbox=[601, 164, 673, 198]
2026-08-05 05:13:03,672 INFO     29 [qwen-vl-text] coord item[8]: text=患者类型:GCP支付, bbox=[69, 216, 259, 250]
2026-08-05 05:13:03,672 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[327, 216, 428, 250]
2026-08-05 05:13:03,672 INFO     29 [qwen-vl-text] coord item[10]: text=处方号:, bbox=[600, 216, 670, 250]
2026-08-05 05:13:03,672 INFO     29 [qwen-vl-text] coord item[11]: text=地址:PT027气雾剂 2024017-呼吸科, bbox=[69, 267, 437, 301]
2026-08-05 05:13:03,672 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[600, 267, 695, 301]
2026-08-05 05:13:03,673 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[70, 317, 240, 351]
2026-08-05 05:13:03,673 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[436, 375, 560, 409]
2026-08-05 05:13:03,673 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[132, 436, 178, 470]
2026-08-05 05:13:03,673 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[232, 436, 325, 470]
2026-08-05 05:13:03,673 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[505, 436, 547, 470]
2026-08-05 05:13:03,673 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[697, 436, 740, 470]
2026-08-05 05:13:03,673 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[795, 436, 838, 470]
2026-08-05 05:13:03,673 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[870, 436, 914, 470]
2026-08-05 05:13:03,673 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[89, 497, 134, 548]
2026-08-05 05:13:03,673 INFO     29 [qwen-vl-text] coord item[22]: text=布地奈德福莫特罗吸入粉雾剂HIV●(50ug*60吸4盒, bbox=[213, 493, 724, 527]
2026-08-05 05:13:03,673 INFO     29 [qwen-vl-text] coord item[23]: text=183.41 733.64, bbox=[752, 495, 902, 523]
2026-08-05 05:13:03,673 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[428, 545, 465, 575]
2026-08-05 05:13:03,673 INFO     29 [qwen-vl-text] coord item[25]: text=2吸/次,吸入,bid*60天, bbox=[504, 545, 735, 575]
2026-08-05 05:13:03,673 INFO     29 [qwen-vl-text] page=7 — 26/26 coords, api_time=7.2s
2026-08-05 05:13:03,673 INFO     29 [qwen-vl-text] new_positions (26):
[[7, 324.17, 508.568, 14.28, 51.765], [7, 58.098, 247.548, 66.64, 86.86999999999999], [7, 275.334, 438.68199999999996, 66.64, 86.86999999999999], [7, 506.042, 564.982, 66.64, 86.86999999999999], [7, 58.098, 92.61999999999999, 97.58, 117.80999999999999], [7, 275.334, 343.536, 97.58, 117.80999999999999], [7, 382.268, 468.99399999999997, 97.58, 117.80999999999999], [7, 506.042, 566.6659999999999, 97.58, 117.80999999999999], [7, 58.098, 218.078, 128.51999999999998, 148.75], [7, 275.334, 360.376, 128.51999999999998, 148.75], [7, 505.2, 564.14, 128.51999999999998, 148.75], [7, 58.098, 367.954, 158.86499999999998, 179.095], [7, 505.2, 585.1899999999999, 158.86499999999998, 179.095], [7, 58.94, 202.07999999999998, 188.61499999999998, 208.845], [7, 367.11199999999997, 471.52, 223.125, 243.355], [7, 111.14399999999999, 149.876, 259.42, 279.65], [7, 195.344, 273.65, 259.42, 279.65], [7, 425.21, 460.574, 259.42, 279.65], [7, 586.874, 623.0799999999999, 259.42, 279.65], [7, 669.39, 705.596, 259.42, 279.65], [7, 732.54, 769.588, 259.42, 279.65], [7, 74.938, 112.828, 295.715, 326.06], [7, 179.346, 609.608, 293.335, 313.565], [7, 633.184, 759.4839999999999, 294.525, 311.185], [7, 360.376, 391.53, 324.275, 342.125], [7, 424.368, 618.87, 324.275, 342.125]]
2026-08-05 05:13:03,673 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=9.9s
2026-08-05 05:13:03,673 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:13:03,673 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 05:13:03,673 INFO     29 [qwen-vl-text] positions(31): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:13:03,673 INFO     29 [qwen-vl-text] page grouping: [8], lines per page: [31]
2026-08-05 05:13:03,823 INFO     29 [qwen-vl-text] page=8, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:13:03,824 INFO     29 [qwen-vl-text] LLM extraction start, text_len=234
2026-08-05 05:13:03,825 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:13:03,825 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 226, \"bbox_end\": 256, \"encounter_dates\": [\"2025-01-03\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-01-03\n就诊科室:内科门诊\n主诊\n性别:男\n年龄:40岁\n卡号\n患者类型:GCP支付\n医疗证号:\n处方\n地址:PT027气雾剂 2024017-呼吸科\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●⑥ug*60吸2盒\n183.41 366.82\nSig\n2吸/次,吸入,bid*30天\n医师:\n医生编号:1326\n配剂人:\n核对人:\n合计:\n收费员:",
    "role": "user"
  }
]
[92m05:13:03 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:13:03,827 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:13:06,447 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:13:06,447 INFO     29 [qwen-vl-text] LLM output (len=419):
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
2026-08-05 05:13:06,447 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-01-03]
2026-08-05 05:13:06,449 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=595064, prompt_len=940
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
2026-08-05 05:13:15,869 INFO     29 [qwen-vl-text] coord API raw response (len=1589):
[
	{"text": "门(急)诊处方", "bbox": [365, 58, 604, 92]},
	{"text": "就诊时间:2025-01-03", "bbox": [18, 105, 263, 123]},
	{"text": "就诊科室:内科门诊", "bbox": [300, 105, 514, 123]},
	{"text": "主诊", "bbox": [603, 105, 648, 123]},
	{"text": "性别:男", "bbox": [300, 132, 390, 150]},
	{"text": "年龄:40岁", "bbox": [440, 132, 553, 150]},
	{"text": "卡号", "bbox": [603, 132, 648, 150]},
	{"text": "患者类型:GCP支付", "bbox": [18, 159, 224, 177]},
	{"text": "医疗证号:", "bbox": [300, 159, 412, 177]},
	{"text": "处方", "bbox": [603, 159, 648, 177]},
	{"text": "地址:PT027气雾剂 2024017-呼吸科", "bbox": [18, 187, 422, 205]},
	{"text": "身份证号:", "bbox": [603, 187, 707, 205]},
	{"text": "诊断:支气管哮喘", "bbox": [18, 212, 204, 231]},
	{"text": "西药处方", "bbox": [421, 244, 557, 263]},
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
	{"text": "医师:", "bbox": [43, 627, 98, 647]},
	{"text": "医生编号:1326", "bbox": [347, 627, 510, 647]},
	{"text": "配剂人:", "bbox": [556, 627, 637, 647]},
	{"text": "核对人:", "bbox": [765, 627, 845, 647]},
	{"text": "合计:", "bbox": [60, 884, 113, 902]},
	{"text": "收费员:", "bbox": [270, 884, 350, 902]}
]
2026-08-05 05:13:15,869 INFO     29 [qwen-vl-text] coord API: raw_items=31, valid_items=31, elapsed=9.4s
2026-08-05 05:13:15,869 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[365, 58, 604, 92]
2026-08-05 05:13:15,869 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-01-03, bbox=[18, 105, 263, 123]
2026-08-05 05:13:15,869 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[300, 105, 514, 123]
2026-08-05 05:13:15,869 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[603, 105, 648, 123]
2026-08-05 05:13:15,869 INFO     29 [qwen-vl-text] coord item[4]: text=性别:男, bbox=[300, 132, 390, 150]
2026-08-05 05:13:15,869 INFO     29 [qwen-vl-text] coord item[5]: text=年龄:40岁, bbox=[440, 132, 553, 150]
2026-08-05 05:13:15,869 INFO     29 [qwen-vl-text] coord item[6]: text=卡号, bbox=[603, 132, 648, 150]
2026-08-05 05:13:15,869 INFO     29 [qwen-vl-text] coord item[7]: text=患者类型:GCP支付, bbox=[18, 159, 224, 177]
2026-08-05 05:13:15,870 INFO     29 [qwen-vl-text] coord item[8]: text=医疗证号:, bbox=[300, 159, 412, 177]
2026-08-05 05:13:15,870 INFO     29 [qwen-vl-text] coord item[9]: text=处方, bbox=[603, 159, 648, 177]
2026-08-05 05:13:15,870 INFO     29 [qwen-vl-text] coord item[10]: text=地址:PT027气雾剂 2024017-呼吸科, bbox=[18, 187, 422, 205]
2026-08-05 05:13:15,870 INFO     29 [qwen-vl-text] coord item[11]: text=身份证号:, bbox=[603, 187, 707, 205]
2026-08-05 05:13:15,870 INFO     29 [qwen-vl-text] coord item[12]: text=诊断:支气管哮喘, bbox=[18, 212, 204, 231]
2026-08-05 05:13:15,870 INFO     29 [qwen-vl-text] coord item[13]: text=西药处方, bbox=[421, 244, 557, 263]
2026-08-05 05:13:15,870 INFO     29 [qwen-vl-text] coord item[14]: text=组号, bbox=[90, 275, 139, 294]
2026-08-05 05:13:15,870 INFO     29 [qwen-vl-text] coord item[15]: text=项目名称, bbox=[198, 275, 300, 294]
2026-08-05 05:13:15,870 INFO     29 [qwen-vl-text] coord item[16]: text=规格, bbox=[497, 275, 544, 294]
2026-08-05 05:13:15,870 INFO     29 [qwen-vl-text] coord item[17]: text=总量, bbox=[707, 275, 755, 294]
2026-08-05 05:13:15,870 INFO     29 [qwen-vl-text] coord item[18]: text=单价, bbox=[815, 275, 863, 294]
2026-08-05 05:13:15,870 INFO     29 [qwen-vl-text] coord item[19]: text=金额, bbox=[899, 275, 947, 294]
2026-08-05 05:13:15,870 INFO     29 [qwen-vl-text] coord item[20]: text=R:, bbox=[44, 308, 93, 338]
2026-08-05 05:13:15,870 INFO     29 [qwen-vl-text] coord item[21]: text=布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●⑥ug*60吸2盒, bbox=[178, 305, 738, 325]
2026-08-05 05:13:15,870 INFO     29 [qwen-vl-text] coord item[22]: text=183.41 366.82, bbox=[768, 307, 934, 323]
2026-08-05 05:13:15,870 INFO     29 [qwen-vl-text] coord item[23]: text=Sig, bbox=[415, 333, 455, 351]
2026-08-05 05:13:15,870 INFO     29 [qwen-vl-text] coord item[24]: text=2吸/次,吸入,bid*30天, bbox=[497, 333, 751, 351]
2026-08-05 05:13:15,870 INFO     29 [qwen-vl-text] coord item[25]: text=医师:, bbox=[43, 627, 98, 647]
2026-08-05 05:13:15,870 INFO     29 [qwen-vl-text] coord item[26]: text=医生编号:1326, bbox=[347, 627, 510, 647]
2026-08-05 05:13:15,870 INFO     29 [qwen-vl-text] coord item[27]: text=配剂人:, bbox=[556, 627, 637, 647]
2026-08-05 05:13:15,871 INFO     29 [qwen-vl-text] coord item[28]: text=核对人:, bbox=[765, 627, 845, 647]
2026-08-05 05:13:15,871 INFO     29 [qwen-vl-text] coord item[29]: text=合计:, bbox=[60, 884, 113, 902]
2026-08-05 05:13:15,871 INFO     29 [qwen-vl-text] coord item[30]: text=收费员:, bbox=[270, 884, 350, 902]
2026-08-05 05:13:15,871 INFO     29 [qwen-vl-text] page=8 — 31/31 coords, api_time=9.4s
2026-08-05 05:13:15,871 INFO     29 [qwen-vl-text] new_positions (31):
[[8, 217.17499999999998, 359.38, 48.836, 77.464], [8, 10.709999999999999, 156.48499999999999, 88.41, 103.566], [8, 178.5, 305.83, 88.41, 103.566], [8, 358.78499999999997, 385.56, 88.41, 103.566], [8, 178.5, 232.04999999999998, 111.14399999999999, 126.3], [8, 261.8, 329.03499999999997, 111.14399999999999, 126.3], [8, 358.78499999999997, 385.56, 111.14399999999999, 126.3], [8, 10.709999999999999, 133.28, 133.878, 149.034], [8, 178.5, 245.14, 133.878, 149.034], [8, 358.78499999999997, 385.56, 133.878, 149.034], [8, 10.709999999999999, 251.08999999999997, 157.454, 172.60999999999999], [8, 358.78499999999997, 420.66499999999996, 157.454, 172.60999999999999], [8, 10.709999999999999, 121.38, 178.504, 194.50199999999998], [8, 250.49499999999998, 331.41499999999996, 205.44799999999998, 221.446], [8, 53.55, 82.705, 231.54999999999998, 247.548], [8, 117.80999999999999, 178.5, 231.54999999999998, 247.548], [8, 295.715, 323.68, 231.54999999999998, 247.548], [8, 420.66499999999996, 449.22499999999997, 231.54999999999998, 247.548], [8, 484.92499999999995, 513.485, 231.54999999999998, 247.548], [8, 534.905, 563.4649999999999, 231.54999999999998, 247.548], [8, 26.18, 55.335, 259.336, 284.596], [8, 105.91, 439.10999999999996, 256.81, 273.65], [8, 456.96, 555.73, 258.49399999999997, 271.966], [8, 246.92499999999998, 270.72499999999997, 280.38599999999997, 295.542], [8, 295.715, 446.84499999999997, 280.38599999999997, 295.542], [8, 25.584999999999997, 58.309999999999995, 527.934, 544.774], [8, 206.465, 303.45, 527.934, 544.774], [8, 330.82, 379.015, 527.934, 544.774], [8, 455.17499999999995, 502.775, 527.934, 544.774], [8, 35.699999999999996, 67.235, 744.328, 759.4839999999999], [8, 160.65, 208.25, 744.328, 759.4839999999999]]
2026-08-05 05:13:15,871 INFO     29 [qwen-vl-text] ═══ DONE ═══ 31 positions, pages=1, time=12.2s
2026-08-05 05:13:15,871 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:13:15,871 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 05:13:15,871 INFO     29 [qwen-vl-text] positions(28): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:13:15,871 INFO     29 [qwen-vl-text] page grouping: [8, 9], lines per page: [2, 26]
2026-08-05 05:13:16,031 INFO     29 [qwen-vl-text] page=8, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:13:16,187 INFO     29 [qwen-vl-text] page=9, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:13:16,188 INFO     29 [qwen-vl-text] LLM extraction start, text_len=220
2026-08-05 05:13:16,188 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:13:16,188 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 257, \"bbox_end\": 284, \"encounter_dates\": [\"2024-12-04\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "CS 扫描全能王\n3亿人都在用的扫描App\n门(急)诊处方\n就诊时间:2024-12-04\n就诊科室:内科门诊\n主诊\n姓名\n性别:男\n年龄:39岁\n卡号\n患者\n医疗证号:\n处方\n地址:PT027气雾剂 2024017-呼吸科\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●(50ug*60吸2盒\n183.41 366.82\nSig\n2吸/次,吸入,bid*30天",
    "role": "user"
  }
]
[92m05:13:16 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:13:16,190 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:13:19,211 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:13:19,212 INFO     29 [qwen-vl-text] LLM output (len=419):
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
2026-08-05 05:13:19,212 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-12-04]
2026-08-05 05:13:19,214 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=595064, prompt_len=639
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共2行）
["CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-05 05:13:20,117 INFO     29 [qwen-vl-text] coord API raw response (len=124):
```json
[
	{"text": "CS 扫描全能王", "bbox": [861, 958, 977, 974]},
	{"text": "3亿人都在用的扫描App", "bbox": [861, 977, 977, 987]}
]
```
2026-08-05 05:13:20,117 INFO     29 [qwen-vl-text] coord API: raw_items=2, valid_items=2, elapsed=0.9s
2026-08-05 05:13:20,118 INFO     29 [qwen-vl-text] coord item[0]: text=CS 扫描全能王, bbox=[861, 958, 977, 974]
2026-08-05 05:13:20,118 INFO     29 [qwen-vl-text] coord item[1]: text=3亿人都在用的扫描App, bbox=[861, 977, 977, 987]
2026-08-05 05:13:20,118 INFO     29 [qwen-vl-text] page=8 — 2/2 coords, api_time=0.9s
2026-08-05 05:13:20,120 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=820637, prompt_len=889
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
2026-08-05 05:13:27,396 INFO     29 [qwen-vl-text] coord API raw response (len=1337):
[
	{"text": "门(急)诊处方", "bbox": [387, 17, 617, 81]},
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
	{"text": "Sig", "bbox": [434, 554, 471, 586]},
	{"text": "2吸/次,吸入,bid*30天", "bbox": [513, 551, 755, 585]}
]
2026-08-05 05:13:27,397 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=7.3s
2026-08-05 05:13:27,397 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[387, 17, 617, 81]
2026-08-05 05:13:27,397 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2024-12-04, bbox=[60, 110, 293, 143]
2026-08-05 05:13:27,397 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[328, 107, 530, 141]
2026-08-05 05:13:27,397 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[615, 107, 654, 141]
2026-08-05 05:13:27,397 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[60, 163, 102, 197]
2026-08-05 05:13:27,397 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[328, 160, 412, 195]
2026-08-05 05:13:27,397 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:39岁, bbox=[460, 160, 567, 195]
2026-08-05 05:13:27,397 INFO     29 [qwen-vl-text] coord item[7]: text=卡号, bbox=[615, 160, 654, 195]
2026-08-05 05:13:27,397 INFO     29 [qwen-vl-text] coord item[8]: text=患者, bbox=[60, 216, 102, 250]
2026-08-05 05:13:27,397 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[328, 214, 432, 249]
2026-08-05 05:13:27,397 INFO     29 [qwen-vl-text] coord item[10]: text=处方, bbox=[613, 214, 654, 249]
2026-08-05 05:13:27,398 INFO     29 [qwen-vl-text] coord item[11]: text=地址:PT027气雾剂 2024017-呼吸科, bbox=[60, 268, 443, 303]
2026-08-05 05:13:27,398 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[613, 266, 715, 300]
2026-08-05 05:13:27,398 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[60, 319, 236, 354]
2026-08-05 05:13:27,398 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[441, 378, 570, 413]
2026-08-05 05:13:27,398 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[124, 444, 172, 478]
2026-08-05 05:13:27,398 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[228, 442, 325, 477]
2026-08-05 05:13:27,398 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[513, 442, 557, 475]
2026-08-05 05:13:27,398 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[714, 440, 760, 474]
2026-08-05 05:13:27,398 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[817, 438, 864, 472]
2026-08-05 05:13:27,398 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[898, 436, 945, 470]
2026-08-05 05:13:27,398 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[80, 508, 126, 561]
2026-08-05 05:13:27,398 INFO     29 [qwen-vl-text] coord item[22]: text=布地奈德福莫特罗吸入粉雾剂(Ⅱ型)/●(50ug*60吸2盒, bbox=[209, 499, 744, 535]
2026-08-05 05:13:27,398 INFO     29 [qwen-vl-text] coord item[23]: text=183.41 366.82, bbox=[774, 499, 933, 530]
2026-08-05 05:13:27,398 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[434, 554, 471, 586]
2026-08-05 05:13:27,398 INFO     29 [qwen-vl-text] coord item[25]: text=2吸/次,吸入,bid*30天, bbox=[513, 551, 755, 585]
2026-08-05 05:13:27,399 INFO     29 [qwen-vl-text] page=9 — 26/26 coords, api_time=7.3s
2026-08-05 05:13:27,399 INFO     29 [qwen-vl-text] new_positions (28):
[[8, 512.295, 581.3149999999999, 806.636, 820.108], [8, 512.295, 581.3149999999999, 822.634, 831.054], [9, 325.854, 519.514, 10.115, 48.195], [9, 50.519999999999996, 246.706, 65.45, 85.085], [9, 276.176, 446.26, 63.665, 83.895], [9, 517.8299999999999, 550.668, 63.665, 83.895], [9, 50.519999999999996, 85.884, 96.985, 117.21499999999999], [9, 276.176, 346.904, 95.19999999999999, 116.02499999999999], [9, 387.32, 477.414, 95.19999999999999, 116.02499999999999], [9, 517.8299999999999, 550.668, 95.19999999999999, 116.02499999999999], [9, 50.519999999999996, 85.884, 128.51999999999998, 148.75], [9, 276.176, 363.74399999999997, 127.33, 148.155], [9, 516.146, 550.668, 127.33, 148.155], [9, 50.519999999999996, 373.006, 159.45999999999998, 180.285], [9, 516.146, 602.03, 158.26999999999998, 178.5], [9, 50.519999999999996, 198.712, 189.80499999999998, 210.63], [9, 371.322, 479.94, 224.91, 245.73499999999999], [9, 104.408, 144.82399999999998, 264.18, 284.40999999999997], [9, 191.976, 273.65, 262.99, 283.815], [9, 431.94599999999997, 468.99399999999997, 262.99, 282.625], [9, 601.188, 639.92, 261.8, 282.03], [9, 687.914, 727.4879999999999, 260.61, 280.84], [9, 756.116, 795.6899999999999, 259.42, 279.65], [9, 67.36, 106.092, 302.26, 333.79499999999996], [9, 175.97799999999998, 626.448, 296.905, 318.325], [9, 651.708, 785.586, 296.905, 315.34999999999997], [9, 365.428, 396.582, 329.63, 348.66999999999996], [9, 431.94599999999997, 635.7099999999999, 327.84499999999997, 348.075]]
2026-08-05 05:13:27,399 INFO     29 [qwen-vl-text] ═══ DONE ═══ 28 positions, pages=2, time=11.5s
2026-08-05 05:13:27,399 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:13:27,399 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 05:13:27,400 INFO     29 [qwen-vl-text] positions(32): [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:13:27,400 INFO     29 [qwen-vl-text] page grouping: [11, 12], lines per page: [2, 30]
2026-08-05 05:13:27,605 INFO     29 [qwen-vl-text] page=11, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:13:27,764 INFO     29 [qwen-vl-text] page=12, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:13:27,765 INFO     29 [qwen-vl-text] LLM extraction start, text_len=281
2026-08-05 05:13:27,765 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:13:27,766 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 693, \"bbox_end\": 724, \"encounter_dates\": [\"2026-01-05\"], \"department\": \"内科门诊（荔湾）\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "CS 扫描全能王\n3亿人都在用的扫描App\n广州医科大学附属第三医院\n处方笺\n普通\n诊疗卡\n患者姓名\n年龄：41岁\n费别：南医保\n科室：内科门诊（荔湾）\n日期：2026-01-05 17:17:14\n处方号\n地址：荔湾\n2024017-呼吸科\n联系电话\n身份号码：\n2739\n诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],急性气管支气管炎\nR\nP:\n布地奈德福莫特罗吸入粉雾剂(II) 160ug/4.5ug*60吸\n2盒\n剂量：每次2吸\n（\n1\n30\n盒）\n用法：吸入用药\nbid\n01-05\n处方金额：366.82元\n取药药房：门诊西药房（荔湾）",
    "role": "user"
  }
]
[92m05:13:27 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:13:27,767 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:13:27,768 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:13:27.767+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 15, "failed": 0, "current": {"4e4700ce908b11f1a3da71efcdd7cc1f": {"id": "4e4700ce908b11f1a3da71efcdd7cc1f", "doc_id": "4e10ceb4908b11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906341337, "task_type": "dataflow", "root_trace_id": "ca345e6640ff4d788f444c3ab712853e", "root_traceparent": "00-ca345e6640ff4d788f444c3ab712853e-8ea193cced1ce3aa-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:13:33,836 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:13:33,836 INFO     29 [qwen-vl-text] LLM output (len=463):
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
2026-08-05 05:13:33,836 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-05]
2026-08-05 05:13:33,837 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1426724, prompt_len=639
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共2行）
["CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-05 05:13:35,584 INFO     29 [qwen-vl-text] coord API raw response (len=124):
```json
[
	{"text": "CS 扫描全能王", "bbox": [861, 958, 977, 974]},
	{"text": "3亿人都在用的扫描App", "bbox": [861, 977, 977, 987]}
]
```
2026-08-05 05:13:35,585 INFO     29 [qwen-vl-text] coord API: raw_items=2, valid_items=2, elapsed=1.7s
2026-08-05 05:13:35,585 INFO     29 [qwen-vl-text] coord item[0]: text=CS 扫描全能王, bbox=[861, 958, 977, 974]
2026-08-05 05:13:35,585 INFO     29 [qwen-vl-text] coord item[1]: text=3亿人都在用的扫描App, bbox=[861, 977, 977, 987]
2026-08-05 05:13:35,585 INFO     29 [qwen-vl-text] page=11 — 2/2 coords, api_time=1.7s
2026-08-05 05:13:35,587 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=831131, prompt_len=962
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
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord API raw response (len=1582):
[
	{"text": "广州医科大学附属第三医院", "bbox": [325, 100, 667, 123]},
	{"text": "处方笺", "bbox": [465, 135, 570, 160]},
	{"text": "普通", "bbox": [812, 168, 850, 182]},
	{"text": "诊疗卡", "bbox": [218, 211, 280, 227]},
	{"text": "患者姓名", "bbox": [218, 237, 283, 251]},
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
	{"text": "R", "bbox": [244, 361, 277, 389]},
	{"text": "P:", "bbox": [279, 372, 297, 387]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(II) 160ug/4.5ug*60吸", "bbox": [250, 404, 714, 420]},
	{"text": "2盒", "bbox": [768, 405, 794, 417]},
	{"text": "剂量：每次2吸", "bbox": [328, 430, 438, 444]},
	{"text": "（", "bbox": [463, 428, 474, 444]},
	{"text": "1", "bbox": [485, 425, 497, 438]},
	{"text": "30", "bbox": [483, 438, 502, 450]},
	{"text": "盒）", "bbox": [510, 430, 544, 446]},
	{"text": "用法：吸入用药", "bbox": [581, 431, 697, 445]},
	{"text": "bid", "bbox": [739, 433, 766, 445]},
	{"text": "01-05", "bbox": [784, 433, 838, 447]},
	{"text": "处方金额：366.82元", "bbox": [252, 857, 474, 875]},
	{"text": "取药药房：门诊西药房（荔湾）", "bbox": [625, 858, 917, 875]}
]
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord API: raw_items=30, valid_items=30, elapsed=8.2s
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord item[0]: text=广州医科大学附属第三医院, bbox=[325, 100, 667, 123]
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord item[1]: text=处方笺, bbox=[465, 135, 570, 160]
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord item[2]: text=普通, bbox=[812, 168, 850, 182]
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord item[3]: text=诊疗卡, bbox=[218, 211, 280, 227]
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord item[4]: text=患者姓名, bbox=[218, 237, 283, 251]
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：41岁, bbox=[545, 236, 634, 250]
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord item[6]: text=费别：南医保, bbox=[702, 235, 809, 248]
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord item[7]: text=科室：内科门诊（荔湾）, bbox=[217, 260, 408, 274]
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord item[8]: text=日期：2026-01-05 17:17:14, bbox=[437, 260, 661, 273]
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord item[9]: text=处方号, bbox=[702, 258, 755, 273]
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord item[10]: text=地址：荔湾, bbox=[218, 282, 312, 296]
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord item[11]: text=2024017-呼吸科, bbox=[438, 281, 565, 295]
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord item[12]: text=联系电话, bbox=[702, 282, 755, 296]
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord item[13]: text=身份号码：, bbox=[218, 304, 298, 319]
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord item[14]: text=2739, bbox=[437, 305, 474, 318]
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord item[15]: text=诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],急性气管支气管炎, bbox=[220, 321, 835, 337]
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord item[16]: text=R, bbox=[244, 361, 277, 389]
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord item[17]: text=P:, bbox=[279, 372, 297, 387]
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord item[18]: text=布地奈德福莫特罗吸入粉雾剂(II) 160ug/4.5ug*60吸, bbox=[250, 404, 714, 420]
2026-08-05 05:13:43,803 INFO     29 [qwen-vl-text] coord item[19]: text=2盒, bbox=[768, 405, 794, 417]
2026-08-05 05:13:43,804 INFO     29 [qwen-vl-text] coord item[20]: text=剂量：每次2吸, bbox=[328, 430, 438, 444]
2026-08-05 05:13:43,804 INFO     29 [qwen-vl-text] coord item[21]: text=（, bbox=[463, 428, 474, 444]
2026-08-05 05:13:43,804 INFO     29 [qwen-vl-text] coord item[22]: text=1, bbox=[485, 425, 497, 438]
2026-08-05 05:13:43,804 INFO     29 [qwen-vl-text] coord item[23]: text=30, bbox=[483, 438, 502, 450]
2026-08-05 05:13:43,804 INFO     29 [qwen-vl-text] coord item[24]: text=盒）, bbox=[510, 430, 544, 446]
2026-08-05 05:13:43,804 INFO     29 [qwen-vl-text] coord item[25]: text=用法：吸入用药, bbox=[581, 431, 697, 445]
2026-08-05 05:13:43,804 INFO     29 [qwen-vl-text] coord item[26]: text=bid, bbox=[739, 433, 766, 445]
2026-08-05 05:13:43,804 INFO     29 [qwen-vl-text] coord item[27]: text=01-05, bbox=[784, 433, 838, 447]
2026-08-05 05:13:43,804 INFO     29 [qwen-vl-text] coord item[28]: text=处方金额：366.82元, bbox=[252, 857, 474, 875]
2026-08-05 05:13:43,804 INFO     29 [qwen-vl-text] coord item[29]: text=取药药房：门诊西药房（荔湾）, bbox=[625, 858, 917, 875]
2026-08-05 05:13:43,804 INFO     29 [qwen-vl-text] page=12 — 30/30 coords, api_time=8.2s
2026-08-05 05:13:43,804 INFO     29 [qwen-vl-text] new_positions (32):
[[11, 512.295, 581.3149999999999, 806.636, 820.108], [11, 512.295, 581.3149999999999, 822.634, 831.054], [12, 193.375, 396.865, 84.2, 103.566], [12, 276.675, 339.15, 113.67, 134.72], [12, 483.14, 505.75, 141.456, 153.244], [12, 129.71, 166.6, 177.662, 191.134], [12, 129.71, 168.385, 199.554, 211.34199999999998], [12, 324.275, 377.22999999999996, 198.712, 210.5], [12, 417.69, 481.35499999999996, 197.87, 208.816], [12, 129.11499999999998, 242.76, 218.92, 230.708], [12, 260.015, 393.29499999999996, 218.92, 229.86599999999999], [12, 417.69, 449.22499999999997, 217.236, 229.86599999999999], [12, 129.71, 185.64, 237.444, 249.232], [12, 260.61, 336.175, 236.602, 248.39], [12, 417.69, 449.22499999999997, 237.444, 249.232], [12, 129.71, 177.31, 255.968, 268.598], [12, 260.015, 282.03, 256.81, 267.756], [12, 130.9, 496.825, 270.282, 283.75399999999996], [12, 145.18, 164.815, 303.962, 327.538], [12, 166.005, 176.715, 313.224, 325.854], [12, 148.75, 424.83, 340.168, 353.64], [12, 456.96, 472.43, 341.01, 351.114], [12, 195.16, 260.61, 362.06, 373.848], [12, 275.485, 282.03, 360.376, 373.848], [12, 288.575, 295.715, 357.84999999999997, 368.796], [12, 287.385, 298.69, 368.796, 378.9], [12, 303.45, 323.68, 362.06, 375.532], [12, 345.695, 414.715, 362.902, 374.69], [12, 439.705, 455.77, 364.586, 374.69], [12, 466.47999999999996, 498.60999999999996, 364.586, 376.37399999999997], [12, 149.94, 282.03, 721.5939999999999, 736.75], [12, 371.875, 545.615, 722.4359999999999, 736.75]]
2026-08-05 05:13:43,804 INFO     29 [qwen-vl-text] ═══ DONE ═══ 32 positions, pages=2, time=16.4s
2026-08-05 05:13:43,812 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-05 05:13:43,812 INFO     29 [Trace] task=4e4700ce | doc=LZK 哮喘 广三(1).pdf | Extractor:Prescription | outputs={"chunks": "7 items, types={'PrescriptionRecord': 7}", "html": "", "json": "3681 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-05 05:13:43,812 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-05 05:13:43,816 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:13:43,816 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m05:13:43 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:13:43,817 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:13:47,348 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:13:47,353 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-05 05:13:47,354 INFO     29 [Trace] task=4e4700ce | doc=LZK 哮喘 广三(1).pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "3681 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-05 05:13:47,354 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-05 05:13:47,358 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:13:47,358 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-05 05:13:49,389 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:13:49,399 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-05 05:13:49,400 INFO     29 [Trace] task=4e4700ce | doc=LZK 哮喘 广三(1).pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "3681 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-05 05:13:49,400 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-05 05:13:49,411 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:13:49,411 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-05 05:13:49,411 INFO     29 [qwen-vl-text] positions(197): [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:13:49,411 INFO     29 [qwen-vl-text] page grouping: [10], lines per page: [197]
2026-08-05 05:13:49,612 INFO     29 [qwen-vl-text] page=10, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:13:49,613 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1345
2026-08-05 05:13:49,613 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:13:49,613 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 285, \"bbox_end\": 481, \"encounter_dates\": [\"2022-06-08\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "激发试验检查报告\n姓名：\n测试号：\n门诊/住院号：\n000\n年龄：\n出生日期：\n19\n性别：\n男\n身高：\n170\n病区：\n内科门诊\n体重：\n81 kg\n机器编号：\n床号：\n电话：\nPred\nA1\nA1/Pd\nNS\nP1 chg%1\nP2 chg%2\nP3 chg%3\nFVC\n[L]\n4.84\n4.69\n97.1\n4.29\n4.22\n-10.1\n3.64\n-22.5\n4.01\n-14.6\nPEV 1\n[L]\n4.01\n3.05\n76.2\n2.72\n2.69\n-11.8\n2.24\n-26.5\n2.44\n-20.0\nPEV 1 % PVC\n[%]\n83.32\n65.02\n78.0\n63.54\n63.83\n-1.82\n61.73\n-5.06\n60.92\n-6.30\nPEV 1 % VC MAX\n[%]\n80.55\n64.94\n80.6\n62.34\n63.83\n-1.70\n61.73\n-4.94\n60.92\n-6.18\nVC MAX\n[L]\n5.05\n4.70\n93.1\n4.37\n4.22\n-10.2\n3.64\n-22.6\n4.01\n-14.7\nPEP\n[L/s]\n9.37\n9.95\n106.2\n9.06\n7.81\n-21.5\n6.73\n-32.3\n8.22\n-17.4\nMMEF 75/25\n[L/s]\n4.52\n1.54\n34.1\n1.33\n1.34\n-12.9\n1.14\n-25.8\n1.23\n-20.0\nMEF 50\n[L/s]\n5.17\n1.97\n38.1\n1.66\n1.71\n-13.4\n1.34\n-31.8\n1.42\n-28.0\nMEF 25\n[L/s]\n2.29\n0.58\n25.5\n0.52\n0.53\n-9.87\n0.50\n-14.6\n0.49\n-15.7\nPET\n[s]\n6.72\n6.87\n6.93\n3.16\n6.75\n0.57\n6.74\n0.38\nV backextrapolation ex [L]\n0.13\n0.09\n0.10\n-20.0\n0.08\n-41.6\n0.08\n-38.5\nPIF\n[L/s]\n8.04\n7.96\n7.58\n-5.76\n6.16\n-23.3\n7.78\n-3.20\nFIF 50\n[L/s]\n7.99\n7.86\n7.16\n-10.3\n5.36\n-32.9\n7.08\n-11.3\nMVV\n[L/min]\n141.88\nBF MVV\n[1/min]\nCumulated dose\n0.072\n0.078\n0.312\n2 Puf\nF/V ex\nF/V in\nVol [L]\nVol%VCmax\nVCmax\nTime [s]\nPD[-20] FEV 1: 0.2117 mg Cumulated\nPD[-20] PEF: < 0.078 mg Cumulated\nPD[] FEV1%I: could not be calculated!\n意见：\n2022/6/08 10:23:56上午\n1.轻度阻塞性通气功能障碍。\n2.支气管激发试验阳性(累计吸入乙酰甲胆碱0.312mg，FEV1下降大于20%，PD20=0.2117mg，气道高反应性(AHR)为中度\n通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后FEV1恢复至预计值80%。",
    "role": "user"
  }
]
[92m05:13:49 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:13:49,614 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:14:02,309 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:14:02.308+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 15, "failed": 0, "current": {"4e4700ce908b11f1a3da71efcdd7cc1f": {"id": "4e4700ce908b11f1a3da71efcdd7cc1f", "doc_id": "4e10ceb4908b11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906341337, "task_type": "dataflow", "root_trace_id": "ca345e6640ff4d788f444c3ab712853e", "root_traceparent": "00-ca345e6640ff4d788f444c3ab712853e-8ea193cced1ce3aa-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:14:04,653 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:14:04,653 INFO     29 [qwen-vl-text] LLM output (len=1877):
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
  "findings": "| 指标 | Pred | A1 | A1/Pd | NS | P1 chg%1 | P2 chg%2 | P3 chg%3 |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n| FVC [L] | 4.84 | 4.69 | 97.1 | 4.29 | 4.22 -10.1 | 3.64 -22.5 | 4.01 -14.6 |\n| PEV 1 [L] | 4.01 | 3.05 | 76.2 | 2.72 | 2.69 -11.8 | 2.24 -26.5 | 2.44 -20.0 |\n| PEV 1 % PVC [%] | 83.32 | 65.02 | 78.0 | 63.54 | 63.83 -1.82 | 61.73 -5.06 | 60.92 -6.30 |\n| PEV 1 % VC MAX [%] | 80.55 | 64.94 | 80.6 | 62.34 | 63.83 -1.70 | 61.73 -4.94 | 60.92 -6.18 |\n| VC MAX [L] | 5.05 | 4.70 | 93.1 | 4.37 | 4.22 -10.2 | 3.64 -22.6 | 4.01 -14.7 |\n| PEP [L/s] | 9.37 | 9.95 | 106.2 | 9.06 | 7.81 -21.5 | 6.73 -32.3 | 8.22 -17.4 |\n| MMEF 75/25 [L/s] | 4.52 | 1.54 | 34.1 | 1.33 | 1.34 -12.9 | 1.14 -25.8 | 1.23 -20.0 |\n| MEF 50 [L/s] | 5.17 | 1.97 | 38.1 | 1.66 | 1.71 -13.4 | 1.34 -31.8 | 1.42 -28.0 |\n| MEF 25 [L/s] | 2.29 | 0.58 | 25.5 | 0.52 | 0.53 -9.87 | 0.50 -14.6 | 0.49 -15.7 |\n| PET [s] | 6.72 | 6.87 | 6.93 | 3.16 | 6.75 0.57 | 6.74 0.38 | |\n| V backextrapolation ex [L] | 0.13 | 0.09 | 0.10 | -20.0 | 0.08 -41.6 | 0.08 -38.5 | |\n| PIF [L/s] | 8.04 | 7.96 | 7.58 | -5.76 | 6.16 -23.3 | 7.78 -3.20 | |\n| FIF 50 [L/s] | 7.99 | 7.86 | 7.16 | -10.3 | 5.36 -32.9 | 7.08 -11.3 | |\n| MVV [L/min] | 141.88 | | | | | | |\n| BF MVV [1/min] | | | | | | | |\n| Cumulated dose | 0.072 | 0.078 | 0.312 | 2 Puf | | | |\n\nPD[-20] FEV 1: 0.2117 mg Cumulated\nPD[-20] PEF: < 0.078 mg Cumulated\nPD[] FEV1%I: could not be calculated!",
  "conclusion": "1.轻度阻塞性通气功能障碍。\n2.支气管激发试验阳性(累计吸入乙酰甲胆碱0.312mg，FEV1下降大于20%，PD20=0.2117mg，气道高反应性(AHR)为中度\n通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后FEV1恢复至预计值80%。",
  "physician": null,
  "reviewer": null
}
2026-08-05 05:14:04,655 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1393927, prompt_len=2550
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共197行）
["激发试验检查报告", "姓名：", "测试号：", "门诊/住院号：", "000", "年龄：", "出生日期：", "19", "性别：", "男", "身高：", "170", "病区：", "内科门诊", "体重：", "81 kg", "机器编号：", "床号：", "电话：", "Pred", "A1", "A1/Pd", "NS", "P1 chg%1", "P2 chg%2", "P3 chg%3", "FVC", "[L]", "4.84", "4.69", "97.1", "4.29", "4.22", "-10.1", "3.64", "-22.5", "4.01", "-14.6", "PEV 1", "[L]", "4.01", "3.05", "76.2", "2.72", "2.69", "-11.8", "2.24", "-26.5", "2.44", "-20.0", "PEV 1 % PVC", "[%]", "83.32", "65.02", "78.0", "63.54", "63.83", "-1.82", "61.73", "-5.06", "60.92", "-6.30", "PEV 1 % VC MAX", "[%]", "80.55", "64.94", "80.6", "62.34", "63.83", "-1.70", "61.73", "-4.94", "60.92", "-6.18", "VC MAX", "[L]", "5.05", "4.70", "93.1", "4.37", "4.22", "-10.2", "3.64", "-22.6", "4.01", "-14.7", "PEP", "[L/s]", "9.37", "9.95", "106.2", "9.06", "7.81", "-21.5", "6.73", "-32.3", "8.22", "-17.4", "MMEF 75/25", "[L/s]", "4.52", "1.54", "34.1", "1.33", "1.34", "-12.9", "1.14", "-25.8", "1.23", "-20.0", "MEF 50", "[L/s]", "5.17", "1.97", "38.1", "1.66", "1.71", "-13.4", "1.34", "-31.8", "1.42", "-28.0", "MEF 25", "[L/s]", "2.29", "0.58", "25.5", "0.52", "0.53", "-9.87", "0.50", "-14.6", "0.49", "-15.7", "PET", "[s]", "6.72", "6.87", "6.93", "3.16", "6.75", "0.57", "6.74", "0.38", "V backextrapolation ex [L]", "0.13", "0.09", "0.10", "-20.0", "0.08", "-41.6", "0.08", "-38.5", "PIF", "[L/s]", "8.04", "7.96", "7.58", "-5.76", "6.16", "-23.3", "7.78", "-3.20", "FIF 50", "[L/s]", "7.99", "7.86", "7.16", "-10.3", "5.36", "-32.9", "7.08", "-11.3", "MVV", "[L/min]", "141.88", "BF MVV", "[1/min]", "Cumulated dose", "0.072", "0.078", "0.312", "2 Puf", "F/V ex", "F/V in", "Vol [L]", "Vol%VCmax", "VCmax", "Time [s]", "PD[-20] FEV 1: 0.2117 mg Cumulated", "PD[-20] PEF: < 0.078 mg Cumulated", "PD[] FEV1%I: could not be calculated!", "意见：", "2022/6/08 10:23:56上午", "1.轻度阻塞性通气功能障碍。", "2.支气管激发试验阳性(累计吸入乙酰甲胆碱0.312mg，FEV1下降大于20%，PD20=0.2117mg，气道高反应性(AHR)为中度", "通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后FEV1恢复至预计值80%。"]

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
2026-08-05 05:15:08,984 INFO     29 [qwen-vl-text] coord API raw response (len=13341):
[
	{"text": "激发试验检查报告", "bbox": [427, 37, 620, 56]},
	{"text": "姓名：", "bbox": [215, 75, 260, 88], "label": "姓名："},
	{"text": "测试号：", "bbox": [215, 89, 275, 102], "label": "测试号："},
	{"text": "门诊/住院号：", "bbox": [542, 74, 644, 87], "label": "门诊/住院号："},
	{"text": "000", "bbox": [699, 75, 722, 87], "label": "000"},
	{"text": "年龄：", "bbox": [215, 103, 260, 116], "label": "年龄："},
	{"text": "出生日期：", "bbox": [542, 88, 618, 101], "label": "出生日期："},
	{"text": "19", "bbox": [700, 90, 722, 102], "label": "19"},
	{"text": "性别：", "bbox": [215, 117, 260, 130], "label": "性别："},
	{"text": "身高：", "bbox": [542, 102, 584, 115], "label": "身高："},
	{"text": "170", "bbox": [700, 103, 722, 115], "label": "170"},
	{"text": "病区：", "bbox": [215, 131, 260, 144], "label": "病区："},
	{"text": "内科门诊", "bbox": [375, 131, 445, 144], "label": "内科门诊"},
	{"text": "体重：", "bbox": [542, 116, 584, 129], "label": "体重："},
	{"text": "81 kg", "bbox": [699, 116, 741, 128], "label": "81 kg"},
	{"text": "机器编号：", "bbox": [215, 145, 293, 158], "label": "机器编号："},
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
	{"text": "4.29", "bbox": [492, 203, 524, 215], "label": "4.29"},
	{"text": "4.22", "bbox": [544, 203, 576, 215], "label": "4.22"},
	{"text": "-10.1", "bbox": [596, 203, 628, 215], "label": "-10.1"},
	{"text": "3.64", "bbox": [648, 203, 680, 215], "label": "3.64"},
	{"text": "-22.5", "bbox": [699, 203, 732, 215], "label": "-22.5"},
	{"text": "4.01", "bbox": [751, 203, 783, 215], "label": "4.01"},
	{"text": "-14.6", "bbox": [803, 203, 836, 215], "label": "-14.6"},
	{"text": "PEV 1", "bbox": [56, 217, 98, 229], "label": "PEV 1"},
	{"text": "[L]", "bbox": [263, 217, 287, 230], "label": "[L]"},
	{"text": "4.01", "bbox": [334, 217, 368, 229], "label": "4.01"},
	{"text": "3.05", "bbox": [398, 217, 424, 229], "label": "3.05"},
	{"text": "76.2", "bbox": [438, 217, 472, 229], "label": "76.2"},
	{"text": "2.72", "bbox": [492, 217, 524, 229], "label": "2.72"},
	{"text": "2.69", "bbox": [544, 217, 576, 229], "label": "2.69"},
	{"text": "-11.8", "bbox": [596, 217, 628, 229], "label": "-11.8"},
	{"text": "2.24", "bbox": [648, 217, 680, 229], "label": "2.24"},
	{"text": "-26.5", "bbox": [699, 217, 732, 229], "label": "-26.5"},
	{"text": "2.44", "bbox": [751, 217, 783, 229], "label": "2.44"},
	{"text": "-20.0", "bbox": [803, 217, 836, 229], "label": "-20.0"},
	{"text": "PEV 1 % PVC", "bbox": [56, 231, 152, 243], "label": "PEV 1 % PVC"},
	{"text": "[%]", "bbox": [263, 231, 287, 244], "label": "[%]"},
	{"text": "83.32", "bbox": [324, 231, 368, 243], "label": "83.32"},
	{"text": "65.02", "bbox": [388, 231, 424, 243], "label": "65.02"},
	{"text": "78.0", "bbox": [438, 231, 472, 243], "label": "78.0"},
	{"text": "63.54", "bbox": [482, 231, 524, 243], "label": "63.54"},
	{"text": "63.83", "bbox": [534, 231, 576, 243], "label": "63.83"},
	{"text": "-1.82", "bbox": [586, 231, 628, 243], "label": "-1.82"},
	{"text": "61.73", "bbox": [638, 231, 680, 243], "label": "61.73"},
	{"text": "-5.06", "bbox": [689, 231, 732, 243], "label": "-5.06"},
	{"text": "60.92", "bbox": [741, 231, 783, 243], "label": "60.92"},
	{"text": "-6.30", "bbox": [793, 231, 836, 243], "label": "-6.30"},
	{"text": "PEV 1 % VC MAX", "bbox": [56, 245, 177, 257], "label": "PEV 1 % VC MAX"},
	{"text": "[%]", "bbox": [263, 245, 287, 258], "label": "[%]"},
	{"text": "80.55", "bbox": [324, 245, 368, 257], "label": "80.55"},
	{"text": "64.94", "bbox": [388, 245, 424, 257], "label": "64.94"},
	{"text": "80.6", "bbox": [438, 245, 472, 257], "label": "80.6"},
	{"text": "62.34", "bbox": [482, 245, 524, 257], "label": "62.34"},
	{"text": "63.83", "bbox": [534, 245, 576, 257], "label": "63.83"},
	{"text": "-1.70", "bbox": [586, 245, 628, 257], "label": "-1.70"},
	{"text": "61.73", "bbox": [638, 245, 680, 257], "label": "61.73"},
	{"text": "-4.94", "bbox": [689, 245, 732, 257], "label": "-4.94"},
	{"text": "60.92", "bbox": [741, 245, 783, 257], "label": "60.92"},
	{"text": "-6.18", "bbox": [793, 245, 836, 257], "label": "-6.18"},
	{"text": "VC MAX", "bbox": [56, 259, 109, 271], "label": "VC MAX"},
	{"text": "[L]", "bbox": [263, 259, 287, 272], "label": "[L]"},
	{"text": "5.05", "bbox": [334, 259, 368, 271], "label": "5.05"},
	{"text": "4.70", "bbox": [398, 259, 424, 271], "label": "4.70"},
	{"text": "93.1", "bbox": [438, 259, 472, 271], "label": "93.1"},
	{"text": "4.37", "bbox": [492, 259, 524, 271], "label": "4.37"},
	{"text": "4.22", "bbox": [544, 259, 576, 271], "label": "4.22"},
	{"text": "-10.2", "bbox": [596, 259, 628, 271], "label": "-10.2"},
	{"text": "3.64", "bbox": [648, 259, 680, 271], "label": "3.64"},
	{"text": "-22.6", "bbox": [699, 259, 732, 271], "label": "-22.6"},
	{"text": "4.01", "bbox": [751, 259, 783, 271], "label": "4.01"},
	{"text": "-14.7", "bbox": [803, 259, 836, 271], "label": "-14.7"},
	{"text": "PEP", "bbox": [56, 273, 83, 285], "label": "PEP"},
	{"text": "[L/s]", "bbox": [246, 273, 287, 286], "label": "[L/s]"},
	{"text": "9.37", "bbox": [334, 273, 368, 285], "label": "9.37"},
	{"text": "9.95", "bbox": [398, 273, 424, 285], "label": "9.95"},
	{"text": "106.2", "bbox": [430, 273, 472, 285], "label": "106.2"},
	{"text": "9.06", "bbox": [492, 273, 524, 285], "label": "9.06"},
	{"text": "7.81", "bbox": [544, 273, 576, 285], "label": "7.81"},
	{"text": "-21.5", "bbox": [596, 273, 628, 285], "label": "-21.5"},
	{"text": "6.73", "bbox": [648, 273, 680, 285], "label": "6.73"},
	{"text": "-32.3", "bbox": [699, 273, 732, 285], "label": "-32.3"},
	{"text": "8.22", "bbox": [751, 273, 783, 285], "label": "8.22"},
	{"text": "-17.4", "bbox": [803, 273, 836, 285], "label": "-17.4"},
	{"text": "MMEF 75/25", "bbox": [56, 287, 143, 300], "label": "MMEF 75/25"},
	{"text": "[L/s]", "bbox": [246, 287, 287, 300], "label": "[L/s]"},
	{"text": "4.52", "bbox": [334, 287, 368, 300], "label": "4.52"},
	{"text": "1.54", "bbox": [398, 287, 424, 300], "label": "1.54"},
	{"text": "34.1", "bbox": [438, 287, 472, 300], "label": "34.1"},
	{"text": "1.33", "bbox": [492, 287, 524, 300], "label": "1.33"},
	{"text": "1.34", "bbox": [544, 287, 576, 300], "label": "1.34"},
	{"text": "-12.9", "bbox": [596, 287, 628, 300], "label": "-12.9"},
	{"text": "1.14", "bbox": [648, 287, 680, 300], "label": "1.14"},
	{"text": "-25.8", "bbox": [699, 287, 732, 300], "label": "-25.8"},
	{"text": "1.23", "bbox": [751, 287, 783, 300], "label": "1.23"},
	{"text": "-20.0", "bbox": [803, 287, 836, 300], "label": "-20.0"},
	{"text": "MEF 50", "bbox": [56, 301, 109, 314], "label": "MEF 50"},
	{"text": "[L/s]", "bbox": [246, 301, 287, 314], "label": "[L/s]"},
	{"text": "5.17", "bbox": [334, 301, 368, 314], "label": "5.17"},
	{"text": "1.97", "bbox": [398, 301, 424, 314], "label": "1.97"},
	{"text": "38.1", "bbox": [438, 301, 472, 314], "label": "38.1"},
	{"text": "1.66", "bbox": [492, 301, 524, 314], "label": "1.66"},
	{"text": "1.71", "bbox": [544, 301, 576, 314], "label": "1.71"},
	{"text": "-13.4", "bbox": [596, 301, 628, 314], "label": "-13.4"},
	{"text": "1.34", "bbox": [648, 301, 680, 314], "label": "1.34"},
	{"text": "-31.8", "bbox": [699, 301, 732, 314], "label": "-31.8"},
	{"text": "1.42", "bbox": [751, 301, 783, 314], "label": "1.42"},
	{"text": "-28.0", "bbox": [803, 301, 836, 314], "label": "-28.0"},
	{"text": "MEF 25", "bbox": [56, 315, 109, 328], "label": "MEF 25"},
	{"text": "[L/s]", "bbox": [246, 315, 287, 328], "label": "[L/s]"},
	{"text": "2.29", "bbox": [334, 315, 368, 328], "label": "2.29"},
	{"text": "0.58", "bbox": [398, 315, 424, 328], "label": "0.58"},
	{"text": "25.5", "bbox": [438, 315, 472, 328], "label": "25.5"},
	{"text": "0.52", "bbox": [492, 315, 524, 328], "label": "0.52"},
	{"text": "0.53", "bbox": [544, 315, 576, 328], "label": "0.53"},
	{"text": "-9.87", "bbox": [596, 315, 628, 328], "label": "-9.87"},
	{"text": "0.50", "bbox": [648, 315, 680, 328], "label": "0.50"},
	{"text": "-14.6", "bbox": [699, 315, 732, 328], "label": "-14.6"},
	{"text": "0.49", "bbox": [751, 315, 783, 328], "label": "0.49"},
	{"text": "-15.7", "bbox": [803, 315, 836, 328], "label": "-15.7"},
	{"text": "PET", "bbox": [56, 330, 83, 342], "label": "PET"},
	{"text": "[s]", "bbox": [263, 330, 287, 343], "label": "[s]"},
	{"text": "6.72", "bbox": [388, 330, 421, 342], "label": "6.72"},
	{"text": "6.87", "bbox": [492, 330, 524, 342], "label": "6.87"},
	{"text": "6.93", "bbox": [544, 330, 576, 342], "label": "6.93"},
	{"text": "3.16", "bbox": [596, 330, 628, 342], "label": "3.16"},
	{"text": "6.75", "bbox": [648, 330, 680, 342], "label": "6.75"},
	{"text": "0.57", "bbox": [699, 330, 732, 342], "label": "0.57"},
	{"text": "6.74", "bbox": [751, 330, 783, 342], "label": "6.74"},
	{"text": "0.38", "bbox": [803, 330, 836, 342], "label": "0.38"},
	{"text": "V backextrapolation ex [L]", "bbox": [56, 344, 287, 357], "label": "V backextrapolation ex [L]"},
	{"text": "0.13", "bbox": [388, 344, 421, 357], "label": "0.13"},
	{"text": "0.09", "bbox": [492, 344, 524, 357], "label": "0.09"},
	{"text": "0.10", "bbox": [544, 344, 576, 357], "label": "0.10"},
	{"text": "-20.0", "bbox": [596, 344, 628, 357], "label": "-20.0"},
	{"text": "0.08", "bbox": [648, 344, 680, 357], "label": "0.08"},
	{"text": "-41.6", "bbox": [699, 344, 732, 357], "label": "-41.6"},
	{"text": "0.08", "bbox": [751, 344, 783, 357], "label": "0.08"},
	{"text": "-38.5", "bbox": [803, 344, 836, 357], "label": "-38.5"},
	{"text": "PIF", "bbox": [56, 358, 83, 371], "label": "PIF"},
	{"text": "[L/s]", "bbox": [246, 358, 287, 371], "label": "[L/s]"},
	{"text": "8.04", "bbox": [388, 358, 421, 371], "label": "8.04"},
	{"text": "7.96", "bbox": [492, 358, 524, 371], "label": "7.96"},
	{"text": "7.58", "bbox": [544, 358, 576, 371], "label": "7.58"},
	{"text": "-5.76", "bbox": [596, 358, 628, 371], "label": "-5.76"},
	{"text": "6.16", "bbox": [648, 358, 680, 371], "label": "6.16"},
	{"text": "-23.3", "bbox": [699, 358, 732, 371], "label": "-23.3"},
	{"text": "7.78", "bbox": [751, 358, 783, 371], "label": "7.78"},
	{"text": "-3.20", "bbox": [803, 358, 836, 371], "label": "-3.20"},
	{"text": "FIF 50", "bbox": [56, 372, 109, 385], "label": "FIF 50"},
	{"text": "[L/s]", "bbox": [246, 372, 287, 385], "label": "[L/s]"},
	{"text": "7.99", "bbox": [388, 372, 421, 385], "label": "7.99"},
	{"text": "7.86", "bbox": [492, 372, 524, 385], "label": "7.86"},
	{"text": "7.16", "bbox": [544, 372, 576, 385], "label": "7.16"},
	{"text": "-10.3", "bbox": [596, 372, 628, 385], "label": "-10.3"},
	{"text": "5.36", "bbox": [648, 372, 680, 385], "label": "5.36"},
	{"text": "-32.9", "bbox": [699, 372, 732, 385], "label": "-32.9"},
	{"text": "7.08", "bbox": [751, 372, 783, 385], "label": "7.08"},
	{"text": "-11.3", "bbox": [803, 372, 836, 385], "label": "-11.3"},
	{"text": "MVV", "bbox": [56, 386, 83, 399], "label": "MVV"},
	{"text": "[L/min]", "bbox": [229, 386, 287, 399], "label": "[L/min]"},
	{"text": "141.88", "bbox": [317, 386, 368, 399], "label": "141.88"},
	{"text": "BF MVV", "bbox": [56, 400, 109, 413], "label": "BF MVV"},
	{"text": "[1/min]", "bbox": [229, 400, 287, 413], "label": "[1/min]"},
	{"text": "Cumulated dose", "bbox": [56, 428, 179, 441], "label": "Cumulated dose"},
	{"text": "0.072", "bbox": [480, 428, 524, 441], "label": "0.072"},
	{"text": "0.078", "bbox": [540, 428, 574, 441], "label": "0.078"},
	{"text": "0.312", "bbox": [637, 428, 680, 441], "label": "0.312"},
	{"text": "2 Puf", "bbox": [741, 428, 785, 441], "label": "2 Puf"},
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
2026-08-05 05:15:08,984 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-05 05:15:08,994 INFO     29 [qwen-vl-text] coord API: raw_items=195, valid_items=194, elapsed=64.3s
2026-08-05 05:15:08,995 INFO     29 [qwen-vl-text] coord item[0]: text=激发试验检查报告, bbox=[427, 37, 620, 56]
2026-08-05 05:15:08,995 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[215, 75, 260, 88]
2026-08-05 05:15:08,995 INFO     29 [qwen-vl-text] coord item[2]: text=测试号：, bbox=[215, 89, 275, 102]
2026-08-05 05:15:08,995 INFO     29 [qwen-vl-text] coord item[3]: text=门诊/住院号：, bbox=[542, 74, 644, 87]
2026-08-05 05:15:08,995 INFO     29 [qwen-vl-text] coord item[4]: text=000, bbox=[699, 75, 722, 87]
2026-08-05 05:15:08,995 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：, bbox=[215, 103, 260, 116]
2026-08-05 05:15:08,996 INFO     29 [qwen-vl-text] coord item[6]: text=出生日期：, bbox=[542, 88, 618, 101]
2026-08-05 05:15:08,997 INFO     29 [qwen-vl-text] coord item[7]: text=19, bbox=[700, 90, 722, 102]
2026-08-05 05:15:08,997 INFO     29 [qwen-vl-text] coord item[8]: text=性别：, bbox=[215, 117, 260, 130]
2026-08-05 05:15:08,997 INFO     29 [qwen-vl-text] coord item[9]: text=身高：, bbox=[542, 102, 584, 115]
2026-08-05 05:15:08,997 INFO     29 [qwen-vl-text] coord item[10]: text=170, bbox=[700, 103, 722, 115]
2026-08-05 05:15:08,998 INFO     29 [qwen-vl-text] coord item[11]: text=病区：, bbox=[215, 131, 260, 144]
2026-08-05 05:15:08,998 INFO     29 [qwen-vl-text] coord item[12]: text=内科门诊, bbox=[375, 131, 445, 144]
2026-08-05 05:15:08,998 INFO     29 [qwen-vl-text] coord item[13]: text=体重：, bbox=[542, 116, 584, 129]
2026-08-05 05:15:08,998 INFO     29 [qwen-vl-text] coord item[14]: text=81 kg, bbox=[699, 116, 741, 128]
2026-08-05 05:15:08,998 INFO     29 [qwen-vl-text] coord item[15]: text=机器编号：, bbox=[215, 145, 293, 158]
2026-08-05 05:15:08,998 INFO     29 [qwen-vl-text] coord item[16]: text=床号：, bbox=[542, 130, 584, 143]
2026-08-05 05:15:08,998 INFO     29 [qwen-vl-text] coord item[17]: text=电话：, bbox=[542, 144, 584, 157]
2026-08-05 05:15:08,998 INFO     29 [qwen-vl-text] coord item[18]: text=Pred, bbox=[332, 175, 368, 188]
2026-08-05 05:15:08,998 INFO     29 [qwen-vl-text] coord item[19]: text=A1, bbox=[402, 175, 418, 188]
2026-08-05 05:15:08,998 INFO     29 [qwen-vl-text] coord item[20]: text=A1/Pd, bbox=[434, 175, 474, 188]
2026-08-05 05:15:08,998 INFO     29 [qwen-vl-text] coord item[21]: text=NS, bbox=[508, 175, 525, 188]
2026-08-05 05:15:08,998 INFO     29 [qwen-vl-text] coord item[22]: text=P1 chg%1, bbox=[558, 175, 628, 188]
2026-08-05 05:15:08,999 INFO     29 [qwen-vl-text] coord item[23]: text=P2 chg%2, bbox=[664, 175, 734, 188]
2026-08-05 05:15:08,999 INFO     29 [qwen-vl-text] coord item[24]: text=P3 chg%3, bbox=[769, 175, 838, 188]
2026-08-05 05:15:08,999 INFO     29 [qwen-vl-text] coord item[25]: text=FVC, bbox=[56, 203, 84, 215]
2026-08-05 05:15:08,999 INFO     29 [qwen-vl-text] coord item[26]: text=[L], bbox=[263, 203, 287, 216]
2026-08-05 05:15:08,999 INFO     29 [qwen-vl-text] coord item[27]: text=4.84, bbox=[334, 203, 368, 215]
2026-08-05 05:15:08,999 INFO     29 [qwen-vl-text] coord item[28]: text=4.69, bbox=[398, 203, 424, 215]
2026-08-05 05:15:08,999 INFO     29 [qwen-vl-text] coord item[29]: text=97.1, bbox=[438, 203, 472, 215]
2026-08-05 05:15:08,999 INFO     29 [qwen-vl-text] coord item[30]: text=4.29, bbox=[492, 203, 524, 215]
2026-08-05 05:15:08,999 INFO     29 [qwen-vl-text] coord item[31]: text=4.22, bbox=[544, 203, 576, 215]
2026-08-05 05:15:08,999 INFO     29 [qwen-vl-text] coord item[32]: text=-10.1, bbox=[596, 203, 628, 215]
2026-08-05 05:15:08,999 INFO     29 [qwen-vl-text] coord item[33]: text=3.64, bbox=[648, 203, 680, 215]
2026-08-05 05:15:08,999 INFO     29 [qwen-vl-text] coord item[34]: text=-22.5, bbox=[699, 203, 732, 215]
2026-08-05 05:15:08,999 INFO     29 [qwen-vl-text] coord item[35]: text=4.01, bbox=[751, 203, 783, 215]
2026-08-05 05:15:08,999 INFO     29 [qwen-vl-text] coord item[36]: text=-14.6, bbox=[803, 203, 836, 215]
2026-08-05 05:15:09,000 INFO     29 [qwen-vl-text] coord item[37]: text=PEV 1, bbox=[56, 217, 98, 229]
2026-08-05 05:15:09,000 INFO     29 [qwen-vl-text] coord item[38]: text=[L], bbox=[263, 217, 287, 230]
2026-08-05 05:15:09,000 INFO     29 [qwen-vl-text] coord item[39]: text=4.01, bbox=[334, 217, 368, 229]
2026-08-05 05:15:09,000 INFO     29 [qwen-vl-text] coord item[40]: text=3.05, bbox=[398, 217, 424, 229]
2026-08-05 05:15:09,000 INFO     29 [qwen-vl-text] coord item[41]: text=76.2, bbox=[438, 217, 472, 229]
2026-08-05 05:15:09,000 INFO     29 [qwen-vl-text] coord item[42]: text=2.72, bbox=[492, 217, 524, 229]
2026-08-05 05:15:09,000 INFO     29 [qwen-vl-text] coord item[43]: text=2.69, bbox=[544, 217, 576, 229]
2026-08-05 05:15:09,000 INFO     29 [qwen-vl-text] coord item[44]: text=-11.8, bbox=[596, 217, 628, 229]
2026-08-05 05:15:09,000 INFO     29 [qwen-vl-text] coord item[45]: text=2.24, bbox=[648, 217, 680, 229]
2026-08-05 05:15:09,000 INFO     29 [qwen-vl-text] coord item[46]: text=-26.5, bbox=[699, 217, 732, 229]
2026-08-05 05:15:09,000 INFO     29 [qwen-vl-text] coord item[47]: text=2.44, bbox=[751, 217, 783, 229]
2026-08-05 05:15:09,000 INFO     29 [qwen-vl-text] coord item[48]: text=-20.0, bbox=[803, 217, 836, 229]
2026-08-05 05:15:09,000 INFO     29 [qwen-vl-text] coord item[49]: text=PEV 1 % PVC, bbox=[56, 231, 152, 243]
2026-08-05 05:15:09,000 INFO     29 [qwen-vl-text] coord item[50]: text=[%], bbox=[263, 231, 287, 244]
2026-08-05 05:15:09,000 INFO     29 [qwen-vl-text] coord item[51]: text=83.32, bbox=[324, 231, 368, 243]
2026-08-05 05:15:09,000 INFO     29 [qwen-vl-text] coord item[52]: text=65.02, bbox=[388, 231, 424, 243]
2026-08-05 05:15:09,000 INFO     29 [qwen-vl-text] coord item[53]: text=78.0, bbox=[438, 231, 472, 243]
2026-08-05 05:15:09,000 INFO     29 [qwen-vl-text] coord item[54]: text=63.54, bbox=[482, 231, 524, 243]
2026-08-05 05:15:09,000 INFO     29 [qwen-vl-text] coord item[55]: text=63.83, bbox=[534, 231, 576, 243]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[56]: text=-1.82, bbox=[586, 231, 628, 243]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[57]: text=61.73, bbox=[638, 231, 680, 243]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[58]: text=-5.06, bbox=[689, 231, 732, 243]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[59]: text=60.92, bbox=[741, 231, 783, 243]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[60]: text=-6.30, bbox=[793, 231, 836, 243]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[61]: text=PEV 1 % VC MAX, bbox=[56, 245, 177, 257]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[62]: text=[%], bbox=[263, 245, 287, 258]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[63]: text=80.55, bbox=[324, 245, 368, 257]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[64]: text=64.94, bbox=[388, 245, 424, 257]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[65]: text=80.6, bbox=[438, 245, 472, 257]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[66]: text=62.34, bbox=[482, 245, 524, 257]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[67]: text=63.83, bbox=[534, 245, 576, 257]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[68]: text=-1.70, bbox=[586, 245, 628, 257]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[69]: text=61.73, bbox=[638, 245, 680, 257]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[70]: text=-4.94, bbox=[689, 245, 732, 257]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[71]: text=60.92, bbox=[741, 245, 783, 257]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[72]: text=-6.18, bbox=[793, 245, 836, 257]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[73]: text=VC MAX, bbox=[56, 259, 109, 271]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[74]: text=[L], bbox=[263, 259, 287, 272]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[75]: text=5.05, bbox=[334, 259, 368, 271]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[76]: text=4.70, bbox=[398, 259, 424, 271]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[77]: text=93.1, bbox=[438, 259, 472, 271]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[78]: text=4.37, bbox=[492, 259, 524, 271]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[79]: text=4.22, bbox=[544, 259, 576, 271]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[80]: text=-10.2, bbox=[596, 259, 628, 271]
2026-08-05 05:15:09,001 INFO     29 [qwen-vl-text] coord item[81]: text=3.64, bbox=[648, 259, 680, 271]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[82]: text=-22.6, bbox=[699, 259, 732, 271]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[83]: text=4.01, bbox=[751, 259, 783, 271]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[84]: text=-14.7, bbox=[803, 259, 836, 271]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[85]: text=PEP, bbox=[56, 273, 83, 285]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[86]: text=[L/s], bbox=[246, 273, 287, 286]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[87]: text=9.37, bbox=[334, 273, 368, 285]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[88]: text=9.95, bbox=[398, 273, 424, 285]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[89]: text=106.2, bbox=[430, 273, 472, 285]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[90]: text=9.06, bbox=[492, 273, 524, 285]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[91]: text=7.81, bbox=[544, 273, 576, 285]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[92]: text=-21.5, bbox=[596, 273, 628, 285]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[93]: text=6.73, bbox=[648, 273, 680, 285]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[94]: text=-32.3, bbox=[699, 273, 732, 285]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[95]: text=8.22, bbox=[751, 273, 783, 285]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[96]: text=-17.4, bbox=[803, 273, 836, 285]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[97]: text=MMEF 75/25, bbox=[56, 287, 143, 300]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[98]: text=[L/s], bbox=[246, 287, 287, 300]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[99]: text=4.52, bbox=[334, 287, 368, 300]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[100]: text=1.54, bbox=[398, 287, 424, 300]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[101]: text=34.1, bbox=[438, 287, 472, 300]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[102]: text=1.33, bbox=[492, 287, 524, 300]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[103]: text=1.34, bbox=[544, 287, 576, 300]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[104]: text=-12.9, bbox=[596, 287, 628, 300]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[105]: text=1.14, bbox=[648, 287, 680, 300]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[106]: text=-25.8, bbox=[699, 287, 732, 300]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[107]: text=1.23, bbox=[751, 287, 783, 300]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[108]: text=-20.0, bbox=[803, 287, 836, 300]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[109]: text=MEF 50, bbox=[56, 301, 109, 314]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[110]: text=[L/s], bbox=[246, 301, 287, 314]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[111]: text=5.17, bbox=[334, 301, 368, 314]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[112]: text=1.97, bbox=[398, 301, 424, 314]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[113]: text=38.1, bbox=[438, 301, 472, 314]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[114]: text=1.66, bbox=[492, 301, 524, 314]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[115]: text=1.71, bbox=[544, 301, 576, 314]
2026-08-05 05:15:09,002 INFO     29 [qwen-vl-text] coord item[116]: text=-13.4, bbox=[596, 301, 628, 314]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[117]: text=1.34, bbox=[648, 301, 680, 314]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[118]: text=-31.8, bbox=[699, 301, 732, 314]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[119]: text=1.42, bbox=[751, 301, 783, 314]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[120]: text=-28.0, bbox=[803, 301, 836, 314]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[121]: text=MEF 25, bbox=[56, 315, 109, 328]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[122]: text=[L/s], bbox=[246, 315, 287, 328]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[123]: text=2.29, bbox=[334, 315, 368, 328]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[124]: text=0.58, bbox=[398, 315, 424, 328]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[125]: text=25.5, bbox=[438, 315, 472, 328]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[126]: text=0.52, bbox=[492, 315, 524, 328]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[127]: text=0.53, bbox=[544, 315, 576, 328]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[128]: text=-9.87, bbox=[596, 315, 628, 328]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[129]: text=0.50, bbox=[648, 315, 680, 328]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[130]: text=-14.6, bbox=[699, 315, 732, 328]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[131]: text=0.49, bbox=[751, 315, 783, 328]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[132]: text=-15.7, bbox=[803, 315, 836, 328]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[133]: text=PET, bbox=[56, 330, 83, 342]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[134]: text=[s], bbox=[263, 330, 287, 343]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[135]: text=6.72, bbox=[388, 330, 421, 342]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[136]: text=6.87, bbox=[492, 330, 524, 342]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[137]: text=6.93, bbox=[544, 330, 576, 342]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[138]: text=3.16, bbox=[596, 330, 628, 342]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[139]: text=6.75, bbox=[648, 330, 680, 342]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[140]: text=0.57, bbox=[699, 330, 732, 342]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[141]: text=6.74, bbox=[751, 330, 783, 342]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[142]: text=0.38, bbox=[803, 330, 836, 342]
2026-08-05 05:15:09,003 INFO     29 [qwen-vl-text] coord item[143]: text=V backextrapolation ex [L], bbox=[56, 344, 287, 357]
2026-08-05 05:15:09,004 INFO     29 [qwen-vl-text] coord item[144]: text=0.13, bbox=[388, 344, 421, 357]
2026-08-05 05:15:09,004 INFO     29 [qwen-vl-text] coord item[145]: text=0.09, bbox=[492, 344, 524, 357]
2026-08-05 05:15:09,004 INFO     29 [qwen-vl-text] coord item[146]: text=0.10, bbox=[544, 344, 576, 357]
2026-08-05 05:15:09,004 INFO     29 [qwen-vl-text] coord item[147]: text=-20.0, bbox=[596, 344, 628, 357]
2026-08-05 05:15:09,004 INFO     29 [qwen-vl-text] coord item[148]: text=0.08, bbox=[648, 344, 680, 357]
2026-08-05 05:15:09,004 INFO     29 [qwen-vl-text] coord item[149]: text=-41.6, bbox=[699, 344, 732, 357]
2026-08-05 05:15:09,004 INFO     29 [qwen-vl-text] coord item[150]: text=0.08, bbox=[751, 344, 783, 357]
2026-08-05 05:15:09,004 INFO     29 [qwen-vl-text] coord item[151]: text=-38.5, bbox=[803, 344, 836, 357]
2026-08-05 05:15:09,004 INFO     29 [qwen-vl-text] coord item[152]: text=PIF, bbox=[56, 358, 83, 371]
2026-08-05 05:15:09,004 INFO     29 [qwen-vl-text] coord item[153]: text=[L/s], bbox=[246, 358, 287, 371]
2026-08-05 05:15:09,004 INFO     29 [qwen-vl-text] coord item[154]: text=8.04, bbox=[388, 358, 421, 371]
2026-08-05 05:15:09,004 INFO     29 [qwen-vl-text] coord item[155]: text=7.96, bbox=[492, 358, 524, 371]
2026-08-05 05:15:09,004 INFO     29 [qwen-vl-text] coord item[156]: text=7.58, bbox=[544, 358, 576, 371]
2026-08-05 05:15:09,004 INFO     29 [qwen-vl-text] coord item[157]: text=-5.76, bbox=[596, 358, 628, 371]
2026-08-05 05:15:09,004 INFO     29 [qwen-vl-text] coord item[158]: text=6.16, bbox=[648, 358, 680, 371]
2026-08-05 05:15:09,004 INFO     29 [qwen-vl-text] coord item[159]: text=-23.3, bbox=[699, 358, 732, 371]
2026-08-05 05:15:09,004 INFO     29 [qwen-vl-text] coord item[160]: text=7.78, bbox=[751, 358, 783, 371]
2026-08-05 05:15:09,004 INFO     29 [qwen-vl-text] coord item[161]: text=-3.20, bbox=[803, 358, 836, 371]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[162]: text=FIF 50, bbox=[56, 372, 109, 385]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[163]: text=[L/s], bbox=[246, 372, 287, 385]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[164]: text=7.99, bbox=[388, 372, 421, 385]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[165]: text=7.86, bbox=[492, 372, 524, 385]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[166]: text=7.16, bbox=[544, 372, 576, 385]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[167]: text=-10.3, bbox=[596, 372, 628, 385]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[168]: text=5.36, bbox=[648, 372, 680, 385]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[169]: text=-32.9, bbox=[699, 372, 732, 385]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[170]: text=7.08, bbox=[751, 372, 783, 385]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[171]: text=-11.3, bbox=[803, 372, 836, 385]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[172]: text=MVV, bbox=[56, 386, 83, 399]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[173]: text=[L/min], bbox=[229, 386, 287, 399]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[174]: text=141.88, bbox=[317, 386, 368, 399]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[175]: text=BF MVV, bbox=[56, 400, 109, 413]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[176]: text=[1/min], bbox=[229, 400, 287, 413]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[177]: text=Cumulated dose, bbox=[56, 428, 179, 441]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[178]: text=0.072, bbox=[480, 428, 524, 441]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[179]: text=0.078, bbox=[540, 428, 574, 441]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[180]: text=0.312, bbox=[637, 428, 680, 441]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[181]: text=2 Puf, bbox=[741, 428, 785, 441]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[182]: text=F/V ex, bbox=[349, 472, 386, 484]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[183]: text=F/V in, bbox=[349, 719, 383, 730]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[184]: text=Vol [L], bbox=[644, 507, 680, 520]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[185]: text=Vol%VCmax, bbox=[590, 530, 658, 540]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[186]: text=VCmax, bbox=[657, 545, 697, 555]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[187]: text=Time [s], bbox=[775, 658, 819, 669]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[188]: text=PD[-20] FEV 1: 0.2117 mg Cumulated, bbox=[96, 750, 389, 763]
2026-08-05 05:15:09,005 INFO     29 [qwen-vl-text] coord item[189]: text=PD[-20] PEF: < 0.078 mg Cumulated, bbox=[96, 762, 381, 775]
2026-08-05 05:15:09,006 INFO     29 [qwen-vl-text] coord item[190]: text=PD[] FEV1%I: could not be calculated!, bbox=[96, 786, 414, 799]
2026-08-05 05:15:09,006 INFO     29 [qwen-vl-text] coord item[191]: text=意见：, bbox=[86, 808, 134, 822]
2026-08-05 05:15:09,006 INFO     29 [qwen-vl-text] coord item[192]: text=2022/6/08 10:23:56上午, bbox=[86, 830, 273, 843]
2026-08-05 05:15:09,006 INFO     29 [qwen-vl-text] coord item[193]: text=1.轻度阻塞性通气功能障碍。, bbox=[86, 842, 314, 855]
2026-08-05 05:15:09,029 INFO     29 [qwen-vl-text] page=10 — 195/197 coords, api_time=64.3s
2026-08-05 05:15:09,029 INFO     29 [qwen-vl-text] new_positions (197):
[[10, 254.065, 368.9, 31.154, 47.152], [10, 127.925, 154.7, 63.15, 74.096], [10, 127.925, 163.625, 74.938, 85.884], [10, 322.49, 383.18, 62.308, 73.25399999999999], [10, 415.905, 429.59, 63.15, 73.25399999999999], [10, 127.925, 154.7, 86.726, 97.672], [10, 322.49, 367.71, 74.096, 85.042], [10, 416.5, 429.59, 75.78, 85.884], [10, 127.925, 154.7, 98.514, 109.46], [10, 322.49, 347.47999999999996, 85.884, 96.83], [10, 416.5, 429.59, 86.726, 96.83], [10, 127.925, 154.7, 110.30199999999999, 121.24799999999999], [10, 223.125, 264.775, 110.30199999999999, 121.24799999999999], [10, 322.49, 347.47999999999996, 97.672, 108.618], [10, 415.905, 440.895, 97.672, 107.776], [10, 127.925, 174.33499999999998, 122.08999999999999, 133.036], [10, 322.49, 347.47999999999996, 109.46, 120.40599999999999], [10, 322.49, 347.47999999999996, 121.24799999999999, 132.194], [10, 197.54, 218.95999999999998, 147.35, 158.296], [10, 239.19, 248.70999999999998, 147.35, 158.296], [10, 258.22999999999996, 282.03, 147.35, 158.296], [10, 302.26, 312.375, 147.35, 158.296], [10, 332.01, 373.65999999999997, 147.35, 158.296], [10, 395.08, 436.72999999999996, 147.35, 158.296], [10, 457.555, 498.60999999999996, 147.35, 158.296], [10, 33.32, 49.98, 170.926, 181.03], [10, 156.48499999999999, 170.765, 170.926, 181.87199999999999], [10, 198.73, 218.95999999999998, 170.926, 181.03], [10, 236.81, 252.28, 170.926, 181.03], [10, 260.61, 280.84, 170.926, 181.03], [10, 292.74, 311.78, 170.926, 181.03], [10, 323.68, 342.71999999999997, 170.926, 181.03], [10, 354.62, 373.65999999999997, 170.926, 181.03], [10, 385.56, 404.59999999999997, 170.926, 181.03], [10, 415.905, 435.53999999999996, 170.926, 181.03], [10, 446.84499999999997, 465.885, 170.926, 181.03], [10, 477.78499999999997, 497.41999999999996, 170.926, 181.03], [10, 33.32, 58.309999999999995, 182.714, 192.81799999999998], [10, 156.48499999999999, 170.765, 182.714, 193.66], [10, 198.73, 218.95999999999998, 182.714, 192.81799999999998], [10, 236.81, 252.28, 182.714, 192.81799999999998], [10, 260.61, 280.84, 182.714, 192.81799999999998], [10, 292.74, 311.78, 182.714, 192.81799999999998], [10, 323.68, 342.71999999999997, 182.714, 192.81799999999998], [10, 354.62, 373.65999999999997, 182.714, 192.81799999999998], [10, 385.56, 404.59999999999997, 182.714, 192.81799999999998], [10, 415.905, 435.53999999999996, 182.714, 192.81799999999998], [10, 446.84499999999997, 465.885, 182.714, 192.81799999999998], [10, 477.78499999999997, 497.41999999999996, 182.714, 192.81799999999998], [10, 33.32, 90.44, 194.50199999999998, 204.606], [10, 156.48499999999999, 170.765, 194.50199999999998, 205.44799999999998], [10, 192.78, 218.95999999999998, 194.50199999999998, 204.606], [10, 230.85999999999999, 252.28, 194.50199999999998, 204.606], [10, 260.61, 280.84, 194.50199999999998, 204.606], [10, 286.78999999999996, 311.78, 194.50199999999998, 204.606], [10, 317.72999999999996, 342.71999999999997, 194.50199999999998, 204.606], [10, 348.66999999999996, 373.65999999999997, 194.50199999999998, 204.606], [10, 379.60999999999996, 404.59999999999997, 194.50199999999998, 204.606], [10, 409.955, 435.53999999999996, 194.50199999999998, 204.606], [10, 440.895, 465.885, 194.50199999999998, 204.606], [10, 471.835, 497.41999999999996, 194.50199999999998, 204.606], [10, 33.32, 105.315, 206.29, 216.394], [10, 156.48499999999999, 170.765, 206.29, 217.236], [10, 192.78, 218.95999999999998, 206.29, 216.394], [10, 230.85999999999999, 252.28, 206.29, 216.394], [10, 260.61, 280.84, 206.29, 216.394], [10, 286.78999999999996, 311.78, 206.29, 216.394], [10, 317.72999999999996, 342.71999999999997, 206.29, 216.394], [10, 348.66999999999996, 373.65999999999997, 206.29, 216.394], [10, 379.60999999999996, 404.59999999999997, 206.29, 216.394], [10, 409.955, 435.53999999999996, 206.29, 216.394], [10, 440.895, 465.885, 206.29, 216.394], [10, 471.835, 497.41999999999996, 206.29, 216.394], [10, 33.32, 64.855, 218.078, 228.182], [10, 156.48499999999999, 170.765, 218.078, 229.024], [10, 198.73, 218.95999999999998, 218.078, 228.182], [10, 236.81, 252.28, 218.078, 228.182], [10, 260.61, 280.84, 218.078, 228.182], [10, 292.74, 311.78, 218.078, 228.182], [10, 323.68, 342.71999999999997, 218.078, 228.182], [10, 354.62, 373.65999999999997, 218.078, 228.182], [10, 385.56, 404.59999999999997, 218.078, 228.182], [10, 415.905, 435.53999999999996, 218.078, 228.182], [10, 446.84499999999997, 465.885, 218.078, 228.182], [10, 477.78499999999997, 497.41999999999996, 218.078, 228.182], [10, 33.32, 49.385, 229.86599999999999, 239.97], [10, 146.37, 170.765, 229.86599999999999, 240.81199999999998], [10, 198.73, 218.95999999999998, 229.86599999999999, 239.97], [10, 236.81, 252.28, 229.86599999999999, 239.97], [10, 255.85, 280.84, 229.86599999999999, 239.97], [10, 292.74, 311.78, 229.86599999999999, 239.97], [10, 323.68, 342.71999999999997, 229.86599999999999, 239.97], [10, 354.62, 373.65999999999997, 229.86599999999999, 239.97], [10, 385.56, 404.59999999999997, 229.86599999999999, 239.97], [10, 415.905, 435.53999999999996, 229.86599999999999, 239.97], [10, 446.84499999999997, 465.885, 229.86599999999999, 239.97], [10, 477.78499999999997, 497.41999999999996, 229.86599999999999, 239.97], [10, 33.32, 85.085, 241.654, 252.6], [10, 146.37, 170.765, 241.654, 252.6], [10, 198.73, 218.95999999999998, 241.654, 252.6], [10, 236.81, 252.28, 241.654, 252.6], [10, 260.61, 280.84, 241.654, 252.6], [10, 292.74, 311.78, 241.654, 252.6], [10, 323.68, 342.71999999999997, 241.654, 252.6], [10, 354.62, 373.65999999999997, 241.654, 252.6], [10, 385.56, 404.59999999999997, 241.654, 252.6], [10, 415.905, 435.53999999999996, 241.654, 252.6], [10, 446.84499999999997, 465.885, 241.654, 252.6], [10, 477.78499999999997, 497.41999999999996, 241.654, 252.6], [10, 33.32, 64.855, 253.44199999999998, 264.388], [10, 146.37, 170.765, 253.44199999999998, 264.388], [10, 198.73, 218.95999999999998, 253.44199999999998, 264.388], [10, 236.81, 252.28, 253.44199999999998, 264.388], [10, 260.61, 280.84, 253.44199999999998, 264.388], [10, 292.74, 311.78, 253.44199999999998, 264.388], [10, 323.68, 342.71999999999997, 253.44199999999998, 264.388], [10, 354.62, 373.65999999999997, 253.44199999999998, 264.388], [10, 385.56, 404.59999999999997, 253.44199999999998, 264.388], [10, 415.905, 435.53999999999996, 253.44199999999998, 264.388], [10, 446.84499999999997, 465.885, 253.44199999999998, 264.388], [10, 477.78499999999997, 497.41999999999996, 253.44199999999998, 264.388], [10, 33.32, 64.855, 265.23, 276.176], [10, 146.37, 170.765, 265.23, 276.176], [10, 198.73, 218.95999999999998, 265.23, 276.176], [10, 236.81, 252.28, 265.23, 276.176], [10, 260.61, 280.84, 265.23, 276.176], [10, 292.74, 311.78, 265.23, 276.176], [10, 323.68, 342.71999999999997, 265.23, 276.176], [10, 354.62, 373.65999999999997, 265.23, 276.176], [10, 385.56, 404.59999999999997, 265.23, 276.176], [10, 415.905, 435.53999999999996, 265.23, 276.176], [10, 446.84499999999997, 465.885, 265.23, 276.176], [10, 477.78499999999997, 497.41999999999996, 265.23, 276.176], [10, 33.32, 49.385, 277.86, 287.964], [10, 156.48499999999999, 170.765, 277.86, 288.806], [10, 230.85999999999999, 250.49499999999998, 277.86, 287.964], [10, 292.74, 311.78, 277.86, 287.964], [10, 323.68, 342.71999999999997, 277.86, 287.964], [10, 354.62, 373.65999999999997, 277.86, 287.964], [10, 385.56, 404.59999999999997, 277.86, 287.964], [10, 415.905, 435.53999999999996, 277.86, 287.964], [10, 446.84499999999997, 465.885, 277.86, 287.964], [10, 477.78499999999997, 497.41999999999996, 277.86, 287.964], [10, 33.32, 170.765, 289.64799999999997, 300.594], [10, 230.85999999999999, 250.49499999999998, 289.64799999999997, 300.594], [10, 292.74, 311.78, 289.64799999999997, 300.594], [10, 323.68, 342.71999999999997, 289.64799999999997, 300.594], [10, 354.62, 373.65999999999997, 289.64799999999997, 300.594], [10, 385.56, 404.59999999999997, 289.64799999999997, 300.594], [10, 415.905, 435.53999999999996, 289.64799999999997, 300.594], [10, 446.84499999999997, 465.885, 289.64799999999997, 300.594], [10, 477.78499999999997, 497.41999999999996, 289.64799999999997, 300.594], [10, 33.32, 49.385, 301.436, 312.382], [10, 146.37, 170.765, 301.436, 312.382], [10, 230.85999999999999, 250.49499999999998, 301.436, 312.382], [10, 292.74, 311.78, 301.436, 312.382], [10, 323.68, 342.71999999999997, 301.436, 312.382], [10, 354.62, 373.65999999999997, 301.436, 312.382], [10, 385.56, 404.59999999999997, 301.436, 312.382], [10, 415.905, 435.53999999999996, 301.436, 312.382], [10, 446.84499999999997, 465.885, 301.436, 312.382], [10, 477.78499999999997, 497.41999999999996, 301.436, 312.382], [10, 33.32, 64.855, 313.224, 324.17], [10, 146.37, 170.765, 313.224, 324.17], [10, 230.85999999999999, 250.49499999999998, 313.224, 324.17], [10, 292.74, 311.78, 313.224, 324.17], [10, 323.68, 342.71999999999997, 313.224, 324.17], [10, 354.62, 373.65999999999997, 313.224, 324.17], [10, 385.56, 404.59999999999997, 313.224, 324.17], [10, 415.905, 435.53999999999996, 313.224, 324.17], [10, 446.84499999999997, 465.885, 313.224, 324.17], [10, 477.78499999999997, 497.41999999999996, 313.224, 324.17], [10, 33.32, 49.385, 325.012, 335.95799999999997], [10, 136.255, 170.765, 325.012, 335.95799999999997], [10, 188.61499999999998, 218.95999999999998, 325.012, 335.95799999999997], [10, 33.32, 64.855, 336.8, 347.746], [10, 136.255, 170.765, 336.8, 347.746], [10, 33.32, 106.505, 360.376, 371.322], [10, 285.59999999999997, 311.78, 360.376, 371.322], [10, 321.3, 341.53, 360.376, 371.322], [10, 379.015, 404.59999999999997, 360.376, 371.322], [10, 440.895, 467.075, 360.376, 371.322], [10, 207.655, 229.67, 397.424, 407.52799999999996], [10, 207.655, 227.885, 605.398, 614.66], [10, 383.18, 404.59999999999997, 426.894, 437.84], [10, 351.05, 391.51, 446.26, 454.68], [10, 390.91499999999996, 414.715, 458.89, 467.31], [10, 461.125, 487.30499999999995, 554.036, 563.298], [10, 57.12, 231.45499999999998, 631.5, 642.446], [10, 57.12, 226.695, 641.6039999999999, 652.55], [10, 57.12, 246.32999999999998, 661.812, 672.7579999999999], [10, 51.169999999999995, 79.72999999999999, 680.336, 692.124], [10, 51.169999999999995, 162.435, 698.86, 709.8059999999999], [10, 51.169999999999995, 186.82999999999998, 708.9639999999999, 719.91], [10, 51.169999999999995, 186.82999999999998, 708.9639999999999, 719.91], [10, 0, 0, 0, 0], [10, 0, 0, 0, 0]]
2026-08-05 05:15:09,030 INFO     29 [qwen-vl-text] ═══ DONE ═══ 197 positions, pages=1, time=79.6s
2026-08-05 05:15:09,030 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:15:09,030 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-05 05:15:09,031 INFO     29 [qwen-vl-text] positions(211): [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:15:09,031 INFO     29 [qwen-vl-text] page grouping: [10, 11], lines per page: [2, 209]
2026-08-05 05:15:09,257 INFO     29 [qwen-vl-text] page=10, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:15:09,458 INFO     29 [qwen-vl-text] page=11, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:15:09,459 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1306
2026-08-05 05:15:09,459 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:15:09,460 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 482, \"bbox_end\": 692, \"encounter_dates\": [\"2021-01-21\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "CS 扫描全能王\n3亿人都在用的扫描App\n检查日期：2021/1/21\n检查时间：16.43\n编号：16\n广州医科大学附属第三医院\n支气管扩张试验检查报告\n姓名：\n测试号：\n年龄：36岁\n性别：男\n病区：\n机器编号：\n门诊/住院号：\n出生日期：\n身高：\n体重：\n床号：\n电话：\nPred\nA1\nA1/Pd\nP1\nA2/Pd\nchg%1\nP2\nA3/Pd\nchg%2\nP3\nA4/Pd\nchg%3\nFVC\n[L]\n4.86\n3.48\n71.5%\n4.01\n82.4%\n15.19\n4.15\n85.4%\n19.47\n4.01\n82.6%\n15.47\nFEV 1\n[L]\n4.03\n1.97\n48.8%\n2.33\n57.9%\n18.59\n2.33\n57.8%\n18.48\n2.44\n60.5%\n24.02\nFEV 1 % FVC\n[%]\n83.32\n56.62\n68.0%\n58.29\n70.0%\n2.95\n56.15\n67.4%\n-0.83\n60.81\n73.0%\n7.40\nFEV 1 % VC MAX\n[%]\n80.73\n56.07\n69.5%\n58.29\n72.2%\n3.96\n56.15\n69.5%\n0.14\n60.81\n75.3%\n8.45\nVC MAX\n[L]\n5.08\n3.51\n69.1%\n4.01\n78.9%\n14.07\n4.15\n81.8%\n18.31\n4.01\n79.1%\n14.35\nPEF\n[L/s]\n9.41\n6.61\n70.3%\n7.99\n85.0%\n20.93\n7.91\n84.1%\n19.63\n8.07\n85.7%\n22.02\nMMEF 75/25\n[L/s]\n4.57\n0.81\n17.7%\n0.96\n21.1%\n19.59\n1.03\n22.6%\n28.17\n1.12\n24.6%\n39.07\nMEF 50\n[L/s]\n5.20\n1.00\n19.2%\n1.29\n24.8%\n29.25\n1.30\n24.9%\n29.87\n1.53\n29.3%\n52.75\nMEF 25\n[L/s]\n2.32\n0.39\n16.7%\n0.38\n16.4%\n-1.68\n0.50\n21.6%\n29.78\n0.41\n17.9%\n7.18\nFET\n[s]\n15.24\n6.42\n-57.87\n6.30\n-58.63\n6.55\n-57.05\nV backextrapolati\n[L/s]\n0.07\n0.07\n0.89\n0.09\n17.79\n0.08\n6.12\nPIF\n[L/s]\n7.03\n7.39\n5.19\n7.17\n1.99\n7.16\n1.91\nFIV1\n[L]\n3.40\n3.76\n10.58\n3.68\n8.26\n3.60\n5.96\nPEF50 % PIF50\n[%]\n16.56\n21.70\n31.06\n19.81\n19.65\n24.71\n49.20\nMVV\n[L/min]\n142.69\nBF MVV\n[1/min]\n意见：\n1.重度混合性肺通气功能障碍。\n2.支气管舒张试验阳性。\n（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后PEV1较基线增加大于12%，且绝对值增加大于200ml）",
    "role": "user"
  }
]
[92m05:15:09 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:15:09,461 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:15:09,462 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:15:09.460+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 15, "failed": 0, "current": {"4e4700ce908b11f1a3da71efcdd7cc1f": {"id": "4e4700ce908b11f1a3da71efcdd7cc1f", "doc_id": "4e10ceb4908b11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906341337, "task_type": "dataflow", "root_trace_id": "ca345e6640ff4d788f444c3ab712853e", "root_traceparent": "00-ca345e6640ff4d788f444c3ab712853e-8ea193cced1ce3aa-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:15:29,389 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:15:29,389 INFO     29 [qwen-vl-text] LLM output (len=2062):
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
2026-08-05 05:15:29,395 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1393927, prompt_len=639
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共2行）
["CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-05 05:15:30,384 INFO     29 [qwen-vl-text] coord API raw response (len=124):
```json
[
	{"text": "CS 扫描全能王", "bbox": [861, 958, 977, 974]},
	{"text": "3亿人都在用的扫描App", "bbox": [861, 977, 977, 987]}
]
```
2026-08-05 05:15:30,384 INFO     29 [qwen-vl-text] coord API: raw_items=2, valid_items=2, elapsed=1.0s
2026-08-05 05:15:30,384 INFO     29 [qwen-vl-text] coord item[0]: text=CS 扫描全能王, bbox=[861, 958, 977, 974]
2026-08-05 05:15:30,384 INFO     29 [qwen-vl-text] coord item[1]: text=3亿人都在用的扫描App, bbox=[861, 977, 977, 987]
2026-08-05 05:15:30,384 INFO     29 [qwen-vl-text] page=10 — 2/2 coords, api_time=1.0s
2026-08-05 05:15:30,387 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1426724, prompt_len=2525
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共209行）
["检查日期：2021/1/21", "检查时间：16.43", "编号：16", "广州医科大学附属第三医院", "支气管扩张试验检查报告", "姓名：", "测试号：", "年龄：36岁", "性别：男", "病区：", "机器编号：", "门诊/住院号：", "出生日期：", "身高：", "体重：", "床号：", "电话：", "Pred", "A1", "A1/Pd", "P1", "A2/Pd", "chg%1", "P2", "A3/Pd", "chg%2", "P3", "A4/Pd", "chg%3", "FVC", "[L]", "4.86", "3.48", "71.5%", "4.01", "82.4%", "15.19", "4.15", "85.4%", "19.47", "4.01", "82.6%", "15.47", "FEV 1", "[L]", "4.03", "1.97", "48.8%", "2.33", "57.9%", "18.59", "2.33", "57.8%", "18.48", "2.44", "60.5%", "24.02", "FEV 1 % FVC", "[%]", "83.32", "56.62", "68.0%", "58.29", "70.0%", "2.95", "56.15", "67.4%", "-0.83", "60.81", "73.0%", "7.40", "FEV 1 % VC MAX", "[%]", "80.73", "56.07", "69.5%", "58.29", "72.2%", "3.96", "56.15", "69.5%", "0.14", "60.81", "75.3%", "8.45", "VC MAX", "[L]", "5.08", "3.51", "69.1%", "4.01", "78.9%", "14.07", "4.15", "81.8%", "18.31", "4.01", "79.1%", "14.35", "PEF", "[L/s]", "9.41", "6.61", "70.3%", "7.99", "85.0%", "20.93", "7.91", "84.1%", "19.63", "8.07", "85.7%", "22.02", "MMEF 75/25", "[L/s]", "4.57", "0.81", "17.7%", "0.96", "21.1%", "19.59", "1.03", "22.6%", "28.17", "1.12", "24.6%", "39.07", "MEF 50", "[L/s]", "5.20", "1.00", "19.2%", "1.29", "24.8%", "29.25", "1.30", "24.9%", "29.87", "1.53", "29.3%", "52.75", "MEF 25", "[L/s]", "2.32", "0.39", "16.7%", "0.38", "16.4%", "-1.68", "0.50", "21.6%", "29.78", "0.41", "17.9%", "7.18", "FET", "[s]", "15.24", "6.42", "-57.87", "6.30", "-58.63", "6.55", "-57.05", "V backextrapolati", "[L/s]", "0.07", "0.07", "0.89", "0.09", "17.79", "0.08", "6.12", "PIF", "[L/s]", "7.03", "7.39", "5.19", "7.17", "1.99", "7.16", "1.91", "FIV1", "[L]", "3.40", "3.76", "10.58", "3.68", "8.26", "3.60", "5.96", "PEF50 % PIF50", "[%]", "16.56", "21.70", "31.06", "19.81", "19.65", "24.71", "49.20", "MVV", "[L/min]", "142.69", "BF MVV", "[1/min]", "意见：", "1.重度混合性肺通气功能障碍。", "2.支气管舒张试验阳性。", "（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后PEV1较基线增加大于12%，且绝对值增加大于200ml）"]

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
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord API raw response (len=10399):
[
	{"text": "检查日期：2021/1/21", "bbox": [49, 88, 158, 98]},
	{"text": "检查时间：16.43", "bbox": [186, 88, 273, 98]},
	{"text": "编号：16", "bbox": [295, 88, 342, 98]},
	{"text": "广州医科大学附属第三医院", "bbox": [367, 104, 644, 120]},
	{"text": "支气管扩张试验检查报告", "bbox": [378, 119, 632, 136]},
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
	{"text": "FVC", "bbox": [54, 258, 81, 270]},
	{"text": "[L]", "bbox": [197, 258, 221, 270]},
	{"text": "4.86", "bbox": [265, 258, 300, 270]},
	{"text": "3.48", "bbox": [324, 258, 358, 270]},
	{"text": "71.5%", "bbox": [375, 258, 417, 270]},
	{"text": "4.01", "bbox": [444, 258, 472, 270]},
	{"text": "82.4%", "bbox": [490, 258, 532, 270]},
	{"text": "15.19", "bbox": [549, 258, 589, 270]},
	{"text": "4.15", "bbox": [613, 258, 646, 270]},
	{"text": "85.4%", "bbox": [664, 258, 705, 270]},
	{"text": "19.47", "bbox": [722, 258, 763, 270]},
	{"text": "4.01", "bbox": [797, 258, 819, 270]},
	{"text": "82.6%", "bbox": [837, 258, 878, 270]},
	{"text": "15.47", "bbox": [895, 258, 935, 270]},
	{"text": "FEV 1", "bbox": [54, 271, 95, 283]},
	{"text": "[L]", "bbox": [197, 271, 221, 283]},
	{"text": "4.03", "bbox": [265, 271, 300, 283]},
	{"text": "1.97", "bbox": [324, 271, 358, 283]},
	{"text": "48.8%", "bbox": [324, 271, 417, 283]},
	{"text": "2.33", "bbox": [444, 271, 472, 283]},
	{"text": "57.9%", "bbox": [490, 271, 532, 283]},
	{"text": "18.59", "bbox": [549, 271, 589, 283]},
	{"text": "2.33", "bbox": [613, 271, 646, 283]},
	{"text": "57.8%", "bbox": [664, 271, 705, 283]},
	{"text": "18.48", "bbox": [722, 271, 763, 283]},
	{"text": "2.44", "bbox": [797, 271, 819, 283]},
	{"text": "60.5%", "bbox": [837, 271, 878, 283]},
	{"text": "24.02", "bbox": [895, 271, 935, 283]},
	{"text": "FEV 1 % FVC", "bbox": [54, 284, 146, 297]},
	{"text": "[%]", "bbox": [197, 284, 221, 297]},
	{"text": "83.32", "bbox": [258, 284, 300, 297]},
	{"text": "56.62", "bbox": [317, 284, 358, 297]},
	{"text": "68.0%", "bbox": [375, 284, 417, 297]},
	{"text": "58.29", "bbox": [435, 284, 472, 297]},
	{"text": "70.0%", "bbox": [490, 284, 532, 297]},
	{"text": "2.95", "bbox": [557, 284, 589, 297]},
	{"text": "56.15", "bbox": [606, 284, 646, 297]},
	{"text": "67.4%", "bbox": [664, 284, 705, 297]},
	{"text": "-0.83", "bbox": [722, 284, 763, 297]},
	{"text": "60.81", "bbox": [781, 284, 819, 297]},
	{"text": "73.0%", "bbox": [837, 284, 878, 297]},
	{"text": "7.40", "bbox": [902, 284, 935, 297]},
	{"text": "FEV 1 % VC MAX", "bbox": [54, 297, 170, 310]},
	{"text": "[%]", "bbox": [197, 297, 221, 310]},
	{"text": "80.73", "bbox": [258, 297, 300, 310]},
	{"text": "56.07", "bbox": [317, 297, 358, 310]},
	{"text": "69.5%", "bbox": [375, 297, 417, 310]},
	{"text": "58.29", "bbox": [435, 297, 472, 310]},
	{"text": "72.2%", "bbox": [490, 297, 532, 310]},
	{"text": "3.96", "bbox": [557, 297, 589, 310]},
	{"text": "56.15", "bbox": [606, 297, 646, 310]},
	{"text": "69.5%", "bbox": [664, 297, 705, 310]},
	{"text": "0.14", "bbox": [730, 297, 763, 310]},
	{"text": "60.81", "bbox": [781, 297, 819, 310]},
	{"text": "75.3%", "bbox": [837, 297, 878, 310]},
	{"text": "8.45", "bbox": [902, 297, 935, 310]},
	{"text": "VC MAX", "bbox": [54, 310, 105, 323]},
	{"text": "[L]", "bbox": [197, 310, 221, 323]},
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
	{"text": "MMEF 75/25", "bbox": [54, 337, 137, 350]},
	{"text": "[L/s]", "bbox": [182, 337, 221, 350]},
	{"text": "4.57", "bbox": [265, 337, 300, 350]},
	{"text": "0.81", "bbox": [324, 337, 358, 350]},
	{"text": "17.7%", "bbox": [375, 337, 417, 350]},
	{"text": "0.96", "bbox": [444, 337, 472, 350]},
	{"text": "21.1%", "bbox": [490, 337, 532, 350]},
	{"text": "19.59", "bbox": [549, 337, 589, 350]},
	{"text": "1.03", "bbox": [613, 337, 646, 350]},
	{"text": "22.6%", "bbox": [664, 337, 705, 350]},
	{"text": "28.17", "bbox": [722, 337, 763, 350]},
	{"text": "1.12", "bbox": [797, 337, 819, 350]},
	{"text": "24.6%", "bbox": [837, 337, 878, 350]},
	{"text": "39.07", "bbox": [895, 337, 935, 350]},
	{"text": "MEF 50", "bbox": [54, 350, 104, 363]},
	{"text": "[L/s]", "bbox": [182, 350, 221, 363]},
	{"text": "5.20", "bbox": [265, 350, 300, 363]},
	{"text": "1.00", "bbox": [324, 350, 358, 363]},
	{"text": "19.2%", "bbox": [375, 350, 417, 363]},
	{"text": "1.29", "bbox": [444, 350, 472, 363]},
	{"text": "24.8%", "bbox": [490, 350, 532, 363]},
	{"text": "29.25", "bbox": [549, 350, 589, 363]},
	{"text": "1.30", "bbox": [613, 350, 646, 363]},
	{"text": "24.9%", "bbox": [664, 350, 705, 363]},
	{"text": "29.87", "bbox": [722, 350, 763, 363]},
	{"text": "1.53", "bbox": [797, 350, 819, 363]},
	{"text": "29.3%", "bbox": [837, 350, 878, 363]},
	{"text": "52.75", "bbox": [895, 350, 935, 363]},
	{"text": "MEF 25", "bbox": [54, 364, 104, 377]},
	{"text": "[L/s]", "bbox": [182, 364, 221, 377]},
	{"text": "2.32", "bbox": [265, 364, 300, 377]},
	{"text": "0.39", "bbox": [324, 364, 358, 377]},
	{"text": "16.7%", "bbox": [375, 364, 417, 377]},
	{"text": "0.38", "bbox": [444, 364, 472, 377]},
	{"text": "16.4%", "bbox": [490, 364, 532, 377]},
	{"text": "-1.68", "bbox": [549, 364, 589, 377]},
	{"text": "0.50", "bbox": [613, 364, 646, 377]},
	{"text": "21.6%", "bbox": [664, 364, 705, 377]},
	{"text": "29.78", "bbox": [722, 364, 763, 377]},
	{"text": "0.41", "bbox": [797, 364, 819, 377]},
	{"text": "17.9%", "bbox": [837, 364, 878, 377]},
	{"text": "7.18", "bbox": [902, 364, 935, 377]},
	{"text": "FET", "bbox": [54, 377, 80, 390]},
	{"text": "[s]", "bbox": [200, 377, 221, 390]},
	{"text": "15.24", "bbox": [320, 377, 358, 390]},
	{"text": "6.42", "bbox": [441, 377, 472, 390]},
	{"text": "-57.87", "bbox": [543, 377, 589, 390]},
	{"text": "6.30", "bbox": [613, 377, 646, 390]},
	{"text": "-58.63", "bbox": [715, 377, 763, 390]},
	{"text": "6.55", "bbox": [790, 377, 819, 390]},
	{"text": "-57.05", "bbox": [887, 377, 935, 390]},
	{"text": "V backextrapolati", "bbox": [54, 390, 225, 403]},
	{"text": "[L/s]", "bbox": [182, 403, 221, 416]},
	{"text": "0.07", "bbox": [326, 390, 358, 403]},
	{"text": "0.07", "bbox": [441, 390, 472, 403]},
	{"text": "0.89", "bbox": [555, 390, 589, 403]},
	{"text": "0.09", "bbox": [613, 390, 646, 403]},
	{"text": "17.79", "bbox": [722, 390, 763, 403]},
	{"text": "0.08", "bbox": [790, 390, 819, 403]},
	{"text": "6.12", "bbox": [902, 390, 935, 403]},
	{"text": "PIF", "bbox": [54, 404, 80, 417]},
	{"text": "7.03", "bbox": [326, 404, 358, 417]},
	{"text": "7.39", "bbox": [441, 404, 472, 417]},
	{"text": "5.19", "bbox": [555, 404, 589, 417]},
	{"text": "7.17", "bbox": [613, 404, 646, 417]},
	{"text": "1.99", "bbox": [730, 404, 763, 417]},
	{"text": "7.16", "bbox": [790, 404, 819, 417]},
	{"text": "1.91", "bbox": [902, 404, 935, 417]},
	{"text": "FIV1", "bbox": [54, 417, 87, 430]},
	{"text": "[L]", "bbox": [197, 417, 221, 430]},
	{"text": "3.40", "bbox": [326, 417, 358, 430]},
	{"text": "3.76", "bbox": [441, 417, 472, 430]},
	{"text": "10.58", "bbox": [549, 417, 589, 430]},
	{"text": "3.68", "bbox": [613, 417, 646, 430]},
	{"text": "8.26", "bbox": [730, 417, 763, 430]},
	{"text": "3.60", "bbox": [790, 417, 819, 430]},
	{"text": "5.96", "bbox": [902, 417, 935, 430]},
	{"text": "PEF50 % PIF50", "bbox": [54, 430, 162, 443]},
	{"text": "[%]", "bbox": [197, 430, 221, 443]},
	{"text": "16.56", "bbox": [317, 430, 358, 443]},
	{"text": "21.70", "bbox": [433, 430, 472, 443]},
	{"text": "31.06", "bbox": [549, 430, 589, 443]},
	{"text": "19.81", "bbox": [606, 430, 646, 443]},
	{"text": "19.65", "bbox": [722, 430, 763, 443]},
	{"text": "24.71", "bbox": [781, 430, 819, 443]},
	{"text": "49.20", "bbox": [895, 430, 935, 443]},
	{"text": "MVV", "bbox": [54, 444, 80, 457]},
	{"text": "[L/min]", "bbox": [167, 444, 221, 457]},
	{"text": "142.69", "bbox": [251, 444, 300, 457]},
	{"text": "BF MVV", "bbox": [54, 457, 104, 470]},
	{"text": "[1/min]", "bbox": [167, 457, 221, 470]},
	{"text": "意见：", "bbox": [73, 788, 120, 802]},
	{"text": "1.重度混合性肺通气功能障碍。", "bbox": [73, 802, 292, 815]},
	{"text": "2.支气管舒张试验阳性。", "bbox": [73, 814, 244, 827]},
	{"text": "（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后PEV1较基线增加大于12%，且绝对值增加大于200ml）", "bbox": [80, 825, 800, 838]}
]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord API: raw_items=208, valid_items=208, elapsed=51.0s
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[0]: text=检查日期：2021/1/21, bbox=[49, 88, 158, 98]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[1]: text=检查时间：16.43, bbox=[186, 88, 273, 98]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[2]: text=编号：16, bbox=[295, 88, 342, 98]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[3]: text=广州医科大学附属第三医院, bbox=[367, 104, 644, 120]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[4]: text=支气管扩张试验检查报告, bbox=[378, 119, 632, 136]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[5]: text=姓名：, bbox=[191, 144, 234, 157]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[6]: text=测试号：, bbox=[191, 157, 248, 170]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[7]: text=年龄：36岁, bbox=[191, 170, 382, 183]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[8]: text=性别：男, bbox=[191, 183, 358, 196]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[9]: text=病区：, bbox=[191, 196, 234, 209]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[10]: text=机器编号：, bbox=[191, 209, 264, 222]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[11]: text=门诊/住院号：, bbox=[500, 143, 596, 156]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[12]: text=出生日期：, bbox=[500, 156, 572, 169]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[13]: text=身高：, bbox=[500, 169, 540, 182]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[14]: text=体重：, bbox=[500, 182, 540, 195]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[15]: text=床号：, bbox=[500, 195, 540, 208]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[16]: text=电话：, bbox=[500, 208, 540, 221]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[17]: text=Pred, bbox=[265, 231, 300, 243]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[18]: text=A1, bbox=[340, 231, 358, 243]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[19]: text=A1/Pd, bbox=[375, 231, 417, 243]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[20]: text=P1, bbox=[457, 231, 472, 243]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[21]: text=A2/Pd, bbox=[490, 231, 532, 243]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[22]: text=chg%1, bbox=[549, 231, 589, 243]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[23]: text=P2, bbox=[630, 231, 646, 243]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[24]: text=A3/Pd, bbox=[664, 231, 705, 243]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[25]: text=chg%2, bbox=[722, 231, 763, 243]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[26]: text=P3, bbox=[804, 231, 819, 243]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[27]: text=A4/Pd, bbox=[837, 231, 878, 243]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[28]: text=chg%3, bbox=[895, 231, 935, 243]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[29]: text=FVC, bbox=[54, 258, 81, 270]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[30]: text=[L], bbox=[197, 258, 221, 270]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[31]: text=4.86, bbox=[265, 258, 300, 270]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[32]: text=3.48, bbox=[324, 258, 358, 270]
2026-08-05 05:16:21,369 INFO     29 [qwen-vl-text] coord item[33]: text=71.5%, bbox=[375, 258, 417, 270]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[34]: text=4.01, bbox=[444, 258, 472, 270]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[35]: text=82.4%, bbox=[490, 258, 532, 270]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[36]: text=15.19, bbox=[549, 258, 589, 270]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[37]: text=4.15, bbox=[613, 258, 646, 270]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[38]: text=85.4%, bbox=[664, 258, 705, 270]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[39]: text=19.47, bbox=[722, 258, 763, 270]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[40]: text=4.01, bbox=[797, 258, 819, 270]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[41]: text=82.6%, bbox=[837, 258, 878, 270]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[42]: text=15.47, bbox=[895, 258, 935, 270]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[43]: text=FEV 1, bbox=[54, 271, 95, 283]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[44]: text=[L], bbox=[197, 271, 221, 283]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[45]: text=4.03, bbox=[265, 271, 300, 283]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[46]: text=1.97, bbox=[324, 271, 358, 283]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[47]: text=48.8%, bbox=[324, 271, 417, 283]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[48]: text=2.33, bbox=[444, 271, 472, 283]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[49]: text=57.9%, bbox=[490, 271, 532, 283]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[50]: text=18.59, bbox=[549, 271, 589, 283]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[51]: text=2.33, bbox=[613, 271, 646, 283]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[52]: text=57.8%, bbox=[664, 271, 705, 283]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[53]: text=18.48, bbox=[722, 271, 763, 283]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[54]: text=2.44, bbox=[797, 271, 819, 283]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[55]: text=60.5%, bbox=[837, 271, 878, 283]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[56]: text=24.02, bbox=[895, 271, 935, 283]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[57]: text=FEV 1 % FVC, bbox=[54, 284, 146, 297]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[58]: text=[%], bbox=[197, 284, 221, 297]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[59]: text=83.32, bbox=[258, 284, 300, 297]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[60]: text=56.62, bbox=[317, 284, 358, 297]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[61]: text=68.0%, bbox=[375, 284, 417, 297]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[62]: text=58.29, bbox=[435, 284, 472, 297]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[63]: text=70.0%, bbox=[490, 284, 532, 297]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[64]: text=2.95, bbox=[557, 284, 589, 297]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[65]: text=56.15, bbox=[606, 284, 646, 297]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[66]: text=67.4%, bbox=[664, 284, 705, 297]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[67]: text=-0.83, bbox=[722, 284, 763, 297]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[68]: text=60.81, bbox=[781, 284, 819, 297]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[69]: text=73.0%, bbox=[837, 284, 878, 297]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[70]: text=7.40, bbox=[902, 284, 935, 297]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[71]: text=FEV 1 % VC MAX, bbox=[54, 297, 170, 310]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[72]: text=[%], bbox=[197, 297, 221, 310]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[73]: text=80.73, bbox=[258, 297, 300, 310]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[74]: text=56.07, bbox=[317, 297, 358, 310]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[75]: text=69.5%, bbox=[375, 297, 417, 310]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[76]: text=58.29, bbox=[435, 297, 472, 310]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[77]: text=72.2%, bbox=[490, 297, 532, 310]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[78]: text=3.96, bbox=[557, 297, 589, 310]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[79]: text=56.15, bbox=[606, 297, 646, 310]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[80]: text=69.5%, bbox=[664, 297, 705, 310]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[81]: text=0.14, bbox=[730, 297, 763, 310]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[82]: text=60.81, bbox=[781, 297, 819, 310]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[83]: text=75.3%, bbox=[837, 297, 878, 310]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[84]: text=8.45, bbox=[902, 297, 935, 310]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[85]: text=VC MAX, bbox=[54, 310, 105, 323]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[86]: text=[L], bbox=[197, 310, 221, 323]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[87]: text=5.08, bbox=[265, 310, 300, 323]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[88]: text=3.51, bbox=[324, 310, 358, 323]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[89]: text=69.1%, bbox=[375, 310, 417, 323]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[90]: text=4.01, bbox=[444, 310, 472, 323]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[91]: text=78.9%, bbox=[490, 310, 532, 323]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[92]: text=14.07, bbox=[549, 310, 589, 323]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[93]: text=4.15, bbox=[613, 310, 646, 323]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[94]: text=81.8%, bbox=[664, 310, 705, 323]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[95]: text=18.31, bbox=[722, 310, 763, 323]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[96]: text=4.01, bbox=[797, 310, 819, 323]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[97]: text=79.1%, bbox=[837, 310, 878, 323]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[98]: text=14.35, bbox=[895, 310, 935, 323]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[99]: text=PEF, bbox=[54, 324, 80, 337]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[100]: text=[L/s], bbox=[182, 324, 221, 337]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[101]: text=9.41, bbox=[265, 324, 300, 337]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[102]: text=6.61, bbox=[324, 324, 358, 337]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[103]: text=70.3%, bbox=[375, 324, 417, 337]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[104]: text=7.99, bbox=[444, 324, 472, 337]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[105]: text=85.0%, bbox=[490, 324, 532, 337]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[106]: text=20.93, bbox=[549, 324, 589, 337]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[107]: text=7.91, bbox=[613, 324, 646, 337]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[108]: text=84.1%, bbox=[664, 324, 705, 337]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[109]: text=19.63, bbox=[722, 324, 763, 337]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[110]: text=8.07, bbox=[797, 324, 819, 337]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[111]: text=85.7%, bbox=[837, 324, 878, 337]
2026-08-05 05:16:21,370 INFO     29 [qwen-vl-text] coord item[112]: text=22.02, bbox=[895, 324, 935, 337]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[113]: text=MMEF 75/25, bbox=[54, 337, 137, 350]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[114]: text=[L/s], bbox=[182, 337, 221, 350]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[115]: text=4.57, bbox=[265, 337, 300, 350]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[116]: text=0.81, bbox=[324, 337, 358, 350]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[117]: text=17.7%, bbox=[375, 337, 417, 350]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[118]: text=0.96, bbox=[444, 337, 472, 350]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[119]: text=21.1%, bbox=[490, 337, 532, 350]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[120]: text=19.59, bbox=[549, 337, 589, 350]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[121]: text=1.03, bbox=[613, 337, 646, 350]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[122]: text=22.6%, bbox=[664, 337, 705, 350]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[123]: text=28.17, bbox=[722, 337, 763, 350]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[124]: text=1.12, bbox=[797, 337, 819, 350]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[125]: text=24.6%, bbox=[837, 337, 878, 350]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[126]: text=39.07, bbox=[895, 337, 935, 350]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[127]: text=MEF 50, bbox=[54, 350, 104, 363]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[128]: text=[L/s], bbox=[182, 350, 221, 363]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[129]: text=5.20, bbox=[265, 350, 300, 363]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[130]: text=1.00, bbox=[324, 350, 358, 363]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[131]: text=19.2%, bbox=[375, 350, 417, 363]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[132]: text=1.29, bbox=[444, 350, 472, 363]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[133]: text=24.8%, bbox=[490, 350, 532, 363]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[134]: text=29.25, bbox=[549, 350, 589, 363]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[135]: text=1.30, bbox=[613, 350, 646, 363]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[136]: text=24.9%, bbox=[664, 350, 705, 363]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[137]: text=29.87, bbox=[722, 350, 763, 363]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[138]: text=1.53, bbox=[797, 350, 819, 363]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[139]: text=29.3%, bbox=[837, 350, 878, 363]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[140]: text=52.75, bbox=[895, 350, 935, 363]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[141]: text=MEF 25, bbox=[54, 364, 104, 377]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[142]: text=[L/s], bbox=[182, 364, 221, 377]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[143]: text=2.32, bbox=[265, 364, 300, 377]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[144]: text=0.39, bbox=[324, 364, 358, 377]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[145]: text=16.7%, bbox=[375, 364, 417, 377]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[146]: text=0.38, bbox=[444, 364, 472, 377]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[147]: text=16.4%, bbox=[490, 364, 532, 377]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[148]: text=-1.68, bbox=[549, 364, 589, 377]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[149]: text=0.50, bbox=[613, 364, 646, 377]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[150]: text=21.6%, bbox=[664, 364, 705, 377]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[151]: text=29.78, bbox=[722, 364, 763, 377]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[152]: text=0.41, bbox=[797, 364, 819, 377]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[153]: text=17.9%, bbox=[837, 364, 878, 377]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[154]: text=7.18, bbox=[902, 364, 935, 377]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[155]: text=FET, bbox=[54, 377, 80, 390]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[156]: text=[s], bbox=[200, 377, 221, 390]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[157]: text=15.24, bbox=[320, 377, 358, 390]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[158]: text=6.42, bbox=[441, 377, 472, 390]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[159]: text=-57.87, bbox=[543, 377, 589, 390]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[160]: text=6.30, bbox=[613, 377, 646, 390]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[161]: text=-58.63, bbox=[715, 377, 763, 390]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[162]: text=6.55, bbox=[790, 377, 819, 390]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[163]: text=-57.05, bbox=[887, 377, 935, 390]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[164]: text=V backextrapolati, bbox=[54, 390, 225, 403]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[165]: text=[L/s], bbox=[182, 403, 221, 416]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[166]: text=0.07, bbox=[326, 390, 358, 403]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[167]: text=0.07, bbox=[441, 390, 472, 403]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[168]: text=0.89, bbox=[555, 390, 589, 403]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[169]: text=0.09, bbox=[613, 390, 646, 403]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[170]: text=17.79, bbox=[722, 390, 763, 403]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[171]: text=0.08, bbox=[790, 390, 819, 403]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[172]: text=6.12, bbox=[902, 390, 935, 403]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[173]: text=PIF, bbox=[54, 404, 80, 417]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[174]: text=7.03, bbox=[326, 404, 358, 417]
2026-08-05 05:16:21,371 INFO     29 [qwen-vl-text] coord item[175]: text=7.39, bbox=[441, 404, 472, 417]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[176]: text=5.19, bbox=[555, 404, 589, 417]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[177]: text=7.17, bbox=[613, 404, 646, 417]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[178]: text=1.99, bbox=[730, 404, 763, 417]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[179]: text=7.16, bbox=[790, 404, 819, 417]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[180]: text=1.91, bbox=[902, 404, 935, 417]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[181]: text=FIV1, bbox=[54, 417, 87, 430]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[182]: text=[L], bbox=[197, 417, 221, 430]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[183]: text=3.40, bbox=[326, 417, 358, 430]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[184]: text=3.76, bbox=[441, 417, 472, 430]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[185]: text=10.58, bbox=[549, 417, 589, 430]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[186]: text=3.68, bbox=[613, 417, 646, 430]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[187]: text=8.26, bbox=[730, 417, 763, 430]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[188]: text=3.60, bbox=[790, 417, 819, 430]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[189]: text=5.96, bbox=[902, 417, 935, 430]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[190]: text=PEF50 % PIF50, bbox=[54, 430, 162, 443]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[191]: text=[%], bbox=[197, 430, 221, 443]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[192]: text=16.56, bbox=[317, 430, 358, 443]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[193]: text=21.70, bbox=[433, 430, 472, 443]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[194]: text=31.06, bbox=[549, 430, 589, 443]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[195]: text=19.81, bbox=[606, 430, 646, 443]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[196]: text=19.65, bbox=[722, 430, 763, 443]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[197]: text=24.71, bbox=[781, 430, 819, 443]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[198]: text=49.20, bbox=[895, 430, 935, 443]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[199]: text=MVV, bbox=[54, 444, 80, 457]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[200]: text=[L/min], bbox=[167, 444, 221, 457]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[201]: text=142.69, bbox=[251, 444, 300, 457]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[202]: text=BF MVV, bbox=[54, 457, 104, 470]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[203]: text=[1/min], bbox=[167, 457, 221, 470]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[204]: text=意见：, bbox=[73, 788, 120, 802]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[205]: text=1.重度混合性肺通气功能障碍。, bbox=[73, 802, 292, 815]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[206]: text=2.支气管舒张试验阳性。, bbox=[73, 814, 244, 827]
2026-08-05 05:16:21,372 INFO     29 [qwen-vl-text] coord item[207]: text=（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后PEV1较基线增加大于12%，且绝对值增加大于200ml）, bbox=[80, 825, 800, 838]
2026-08-05 05:16:21,373 INFO     29 [qwen-vl-text] page=11 — 209/209 coords, api_time=51.0s
2026-08-05 05:16:21,373 INFO     29 [qwen-vl-text] new_positions (211):
[[10, 512.295, 581.3149999999999, 806.636, 820.108], [10, 512.295, 581.3149999999999, 822.634, 831.054], [11, 29.154999999999998, 94.00999999999999, 74.096, 82.51599999999999], [11, 110.67, 162.435, 74.096, 82.51599999999999], [11, 175.525, 203.48999999999998, 74.096, 82.51599999999999], [11, 218.36499999999998, 383.18, 87.568, 101.03999999999999], [11, 224.91, 376.03999999999996, 100.198, 114.512], [11, 113.645, 139.23, 121.24799999999999, 132.194], [11, 113.645, 147.56, 132.194, 143.14], [11, 113.645, 227.29, 143.14, 154.08599999999998], [11, 113.645, 213.01, 154.08599999999998, 165.03199999999998], [11, 113.645, 139.23, 165.03199999999998, 175.97799999999998], [11, 113.645, 157.07999999999998, 175.97799999999998, 186.924], [11, 297.5, 354.62, 120.40599999999999, 131.352], [11, 297.5, 340.34, 131.352, 142.298], [11, 297.5, 321.3, 142.298, 153.244], [11, 297.5, 321.3, 153.244, 164.19], [11, 297.5, 321.3, 164.19, 175.136], [11, 297.5, 321.3, 175.136, 186.082], [11, 157.67499999999998, 178.5, 194.50199999999998, 204.606], [11, 202.29999999999998, 213.01, 194.50199999999998, 204.606], [11, 223.125, 248.11499999999998, 194.50199999999998, 204.606], [11, 271.91499999999996, 280.84, 194.50199999999998, 204.606], [11, 291.55, 316.53999999999996, 194.50199999999998, 204.606], [11, 326.655, 350.455, 194.50199999999998, 204.606], [11, 374.84999999999997, 384.37, 194.50199999999998, 204.606], [11, 395.08, 419.47499999999997, 194.50199999999998, 204.606], [11, 429.59, 453.98499999999996, 194.50199999999998, 204.606], [11, 478.38, 487.30499999999995, 194.50199999999998, 204.606], [11, 498.015, 522.41, 194.50199999999998, 204.606], [11, 532.525, 556.3249999999999, 194.50199999999998, 204.606], [11, 32.129999999999995, 48.195, 217.236, 227.34], [11, 117.21499999999999, 131.495, 217.236, 227.34], [11, 157.67499999999998, 178.5, 217.236, 227.34], [11, 192.78, 213.01, 217.236, 227.34], [11, 223.125, 248.11499999999998, 217.236, 227.34], [11, 264.18, 280.84, 217.236, 227.34], [11, 291.55, 316.53999999999996, 217.236, 227.34], [11, 326.655, 350.455, 217.236, 227.34], [11, 364.73499999999996, 384.37, 217.236, 227.34], [11, 395.08, 419.47499999999997, 217.236, 227.34], [11, 429.59, 453.98499999999996, 217.236, 227.34], [11, 474.215, 487.30499999999995, 217.236, 227.34], [11, 498.015, 522.41, 217.236, 227.34], [11, 532.525, 556.3249999999999, 217.236, 227.34], [11, 32.129999999999995, 56.525, 228.182, 238.286], [11, 117.21499999999999, 131.495, 228.182, 238.286], [11, 157.67499999999998, 178.5, 228.182, 238.286], [11, 192.78, 213.01, 228.182, 238.286], [11, 192.78, 248.11499999999998, 228.182, 238.286], [11, 264.18, 280.84, 228.182, 238.286], [11, 291.55, 316.53999999999996, 228.182, 238.286], [11, 326.655, 350.455, 228.182, 238.286], [11, 364.73499999999996, 384.37, 228.182, 238.286], [11, 395.08, 419.47499999999997, 228.182, 238.286], [11, 429.59, 453.98499999999996, 228.182, 238.286], [11, 474.215, 487.30499999999995, 228.182, 238.286], [11, 498.015, 522.41, 228.182, 238.286], [11, 532.525, 556.3249999999999, 228.182, 238.286], [11, 32.129999999999995, 86.86999999999999, 239.128, 250.07399999999998], [11, 117.21499999999999, 131.495, 239.128, 250.07399999999998], [11, 153.51, 178.5, 239.128, 250.07399999999998], [11, 188.61499999999998, 213.01, 239.128, 250.07399999999998], [11, 223.125, 248.11499999999998, 239.128, 250.07399999999998], [11, 258.825, 280.84, 239.128, 250.07399999999998], [11, 291.55, 316.53999999999996, 239.128, 250.07399999999998], [11, 331.41499999999996, 350.455, 239.128, 250.07399999999998], [11, 360.57, 384.37, 239.128, 250.07399999999998], [11, 395.08, 419.47499999999997, 239.128, 250.07399999999998], [11, 429.59, 453.98499999999996, 239.128, 250.07399999999998], [11, 464.695, 487.30499999999995, 239.128, 250.07399999999998], [11, 498.015, 522.41, 239.128, 250.07399999999998], [11, 536.6899999999999, 556.3249999999999, 239.128, 250.07399999999998], [11, 32.129999999999995, 101.14999999999999, 250.07399999999998, 261.02], [11, 117.21499999999999, 131.495, 250.07399999999998, 261.02], [11, 153.51, 178.5, 250.07399999999998, 261.02], [11, 188.61499999999998, 213.01, 250.07399999999998, 261.02], [11, 223.125, 248.11499999999998, 250.07399999999998, 261.02], [11, 258.825, 280.84, 250.07399999999998, 261.02], [11, 291.55, 316.53999999999996, 250.07399999999998, 261.02], [11, 331.41499999999996, 350.455, 250.07399999999998, 261.02], [11, 360.57, 384.37, 250.07399999999998, 261.02], [11, 395.08, 419.47499999999997, 250.07399999999998, 261.02], [11, 434.34999999999997, 453.98499999999996, 250.07399999999998, 261.02], [11, 464.695, 487.30499999999995, 250.07399999999998, 261.02], [11, 498.015, 522.41, 250.07399999999998, 261.02], [11, 536.6899999999999, 556.3249999999999, 250.07399999999998, 261.02], [11, 32.129999999999995, 62.474999999999994, 261.02, 271.966], [11, 117.21499999999999, 131.495, 261.02, 271.966], [11, 157.67499999999998, 178.5, 261.02, 271.966], [11, 192.78, 213.01, 261.02, 271.966], [11, 223.125, 248.11499999999998, 261.02, 271.966], [11, 264.18, 280.84, 261.02, 271.966], [11, 291.55, 316.53999999999996, 261.02, 271.966], [11, 326.655, 350.455, 261.02, 271.966], [11, 364.73499999999996, 384.37, 261.02, 271.966], [11, 395.08, 419.47499999999997, 261.02, 271.966], [11, 429.59, 453.98499999999996, 261.02, 271.966], [11, 474.215, 487.30499999999995, 261.02, 271.966], [11, 498.015, 522.41, 261.02, 271.966], [11, 532.525, 556.3249999999999, 261.02, 271.966], [11, 32.129999999999995, 47.599999999999994, 272.808, 283.75399999999996], [11, 108.28999999999999, 131.495, 272.808, 283.75399999999996], [11, 157.67499999999998, 178.5, 272.808, 283.75399999999996], [11, 192.78, 213.01, 272.808, 283.75399999999996], [11, 223.125, 248.11499999999998, 272.808, 283.75399999999996], [11, 264.18, 280.84, 272.808, 283.75399999999996], [11, 291.55, 316.53999999999996, 272.808, 283.75399999999996], [11, 326.655, 350.455, 272.808, 283.75399999999996], [11, 364.73499999999996, 384.37, 272.808, 283.75399999999996], [11, 395.08, 419.47499999999997, 272.808, 283.75399999999996], [11, 429.59, 453.98499999999996, 272.808, 283.75399999999996], [11, 474.215, 487.30499999999995, 272.808, 283.75399999999996], [11, 498.015, 522.41, 272.808, 283.75399999999996], [11, 532.525, 556.3249999999999, 272.808, 283.75399999999996], [11, 32.129999999999995, 81.515, 283.75399999999996, 294.7], [11, 108.28999999999999, 131.495, 283.75399999999996, 294.7], [11, 157.67499999999998, 178.5, 283.75399999999996, 294.7], [11, 192.78, 213.01, 283.75399999999996, 294.7], [11, 223.125, 248.11499999999998, 283.75399999999996, 294.7], [11, 264.18, 280.84, 283.75399999999996, 294.7], [11, 291.55, 316.53999999999996, 283.75399999999996, 294.7], [11, 326.655, 350.455, 283.75399999999996, 294.7], [11, 364.73499999999996, 384.37, 283.75399999999996, 294.7], [11, 395.08, 419.47499999999997, 283.75399999999996, 294.7], [11, 429.59, 453.98499999999996, 283.75399999999996, 294.7], [11, 474.215, 487.30499999999995, 283.75399999999996, 294.7], [11, 498.015, 522.41, 283.75399999999996, 294.7], [11, 532.525, 556.3249999999999, 283.75399999999996, 294.7], [11, 32.129999999999995, 61.879999999999995, 294.7, 305.646], [11, 108.28999999999999, 131.495, 294.7, 305.646], [11, 157.67499999999998, 178.5, 294.7, 305.646], [11, 192.78, 213.01, 294.7, 305.646], [11, 223.125, 248.11499999999998, 294.7, 305.646], [11, 264.18, 280.84, 294.7, 305.646], [11, 291.55, 316.53999999999996, 294.7, 305.646], [11, 326.655, 350.455, 294.7, 305.646], [11, 364.73499999999996, 384.37, 294.7, 305.646], [11, 395.08, 419.47499999999997, 294.7, 305.646], [11, 429.59, 453.98499999999996, 294.7, 305.646], [11, 474.215, 487.30499999999995, 294.7, 305.646], [11, 498.015, 522.41, 294.7, 305.646], [11, 532.525, 556.3249999999999, 294.7, 305.646], [11, 32.129999999999995, 61.879999999999995, 306.488, 317.43399999999997], [11, 108.28999999999999, 131.495, 306.488, 317.43399999999997], [11, 157.67499999999998, 178.5, 306.488, 317.43399999999997], [11, 192.78, 213.01, 306.488, 317.43399999999997], [11, 223.125, 248.11499999999998, 306.488, 317.43399999999997], [11, 264.18, 280.84, 306.488, 317.43399999999997], [11, 291.55, 316.53999999999996, 306.488, 317.43399999999997], [11, 326.655, 350.455, 306.488, 317.43399999999997], [11, 364.73499999999996, 384.37, 306.488, 317.43399999999997], [11, 395.08, 419.47499999999997, 306.488, 317.43399999999997], [11, 429.59, 453.98499999999996, 306.488, 317.43399999999997], [11, 474.215, 487.30499999999995, 306.488, 317.43399999999997], [11, 498.015, 522.41, 306.488, 317.43399999999997], [11, 536.6899999999999, 556.3249999999999, 306.488, 317.43399999999997], [11, 32.129999999999995, 47.599999999999994, 317.43399999999997, 328.38], [11, 119.0, 131.495, 317.43399999999997, 328.38], [11, 190.39999999999998, 213.01, 317.43399999999997, 328.38], [11, 262.395, 280.84, 317.43399999999997, 328.38], [11, 323.085, 350.455, 317.43399999999997, 328.38], [11, 364.73499999999996, 384.37, 317.43399999999997, 328.38], [11, 425.42499999999995, 453.98499999999996, 317.43399999999997, 328.38], [11, 470.04999999999995, 487.30499999999995, 317.43399999999997, 328.38], [11, 527.765, 556.3249999999999, 317.43399999999997, 328.38], [11, 32.129999999999995, 133.875, 328.38, 339.32599999999996], [11, 108.28999999999999, 131.495, 339.32599999999996, 350.272], [11, 193.97, 213.01, 328.38, 339.32599999999996], [11, 262.395, 280.84, 328.38, 339.32599999999996], [11, 330.22499999999997, 350.455, 328.38, 339.32599999999996], [11, 364.73499999999996, 384.37, 328.38, 339.32599999999996], [11, 429.59, 453.98499999999996, 328.38, 339.32599999999996], [11, 470.04999999999995, 487.30499999999995, 328.38, 339.32599999999996], [11, 536.6899999999999, 556.3249999999999, 328.38, 339.32599999999996], [11, 32.129999999999995, 47.599999999999994, 340.168, 351.114], [11, 193.97, 213.01, 340.168, 351.114], [11, 262.395, 280.84, 340.168, 351.114], [11, 330.22499999999997, 350.455, 340.168, 351.114], [11, 364.73499999999996, 384.37, 340.168, 351.114], [11, 434.34999999999997, 453.98499999999996, 340.168, 351.114], [11, 470.04999999999995, 487.30499999999995, 340.168, 351.114], [11, 536.6899999999999, 556.3249999999999, 340.168, 351.114], [11, 32.129999999999995, 51.765, 351.114, 362.06], [11, 117.21499999999999, 131.495, 351.114, 362.06], [11, 193.97, 213.01, 351.114, 362.06], [11, 262.395, 280.84, 351.114, 362.06], [11, 326.655, 350.455, 351.114, 362.06], [11, 364.73499999999996, 384.37, 351.114, 362.06], [11, 434.34999999999997, 453.98499999999996, 351.114, 362.06], [11, 470.04999999999995, 487.30499999999995, 351.114, 362.06], [11, 536.6899999999999, 556.3249999999999, 351.114, 362.06], [11, 32.129999999999995, 96.39, 362.06, 373.006], [11, 117.21499999999999, 131.495, 362.06, 373.006], [11, 188.61499999999998, 213.01, 362.06, 373.006], [11, 257.635, 280.84, 362.06, 373.006], [11, 326.655, 350.455, 362.06, 373.006], [11, 360.57, 384.37, 362.06, 373.006], [11, 429.59, 453.98499999999996, 362.06, 373.006], [11, 464.695, 487.30499999999995, 362.06, 373.006], [11, 532.525, 556.3249999999999, 362.06, 373.006], [11, 32.129999999999995, 47.599999999999994, 373.848, 384.794], [11, 99.365, 131.495, 373.848, 384.794], [11, 149.345, 178.5, 373.848, 384.794], [11, 32.129999999999995, 61.879999999999995, 384.794, 395.74], [11, 99.365, 131.495, 384.794, 395.74], [11, 43.434999999999995, 71.39999999999999, 663.496, 675.284], [11, 43.434999999999995, 173.73999999999998, 675.284, 686.23], [11, 43.434999999999995, 145.18, 685.3879999999999, 696.334], [11, 47.599999999999994, 476.0, 694.65, 705.596], [11, 47.599999999999994, 476.0, 694.65, 705.596]]
2026-08-05 05:16:21,373 INFO     29 [qwen-vl-text] ═══ DONE ═══ 211 positions, pages=2, time=72.3s
2026-08-05 05:16:21,373 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:16:21,373 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-05 05:16:21,374 INFO     29 [qwen-vl-text] positions(2885): [[15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:16:21,376 INFO     29 [qwen-vl-text] page grouping: [15], lines per page: [2885]
2026-08-05 05:16:21,585 INFO     29 [qwen-vl-text] page=15, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:16:21,586 INFO     29 [qwen-vl-text] LLM extraction start, text_len=13632
2026-08-05 05:16:21,586 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:16:21,586 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 796, \"bbox_end\": 3680, \"encounter_dates\": [\"2024-10-22\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "广州医科大学附属第三医院\n肺功能检查报告\n地址：广州市多宝路63号 电话：020-81292126\nCOSMED\n姓名：\n科室/床号：\nID：\n出生日期：1984/12/8\n预计值：ERS 93\n日期：2024/10/22\n性别：Male\n地区修正：Chinese\n详细描述：内科门诊\nCompany：\n年龄：39\n体重(Kg)：89.0\n身高(cm)：177.5\nBMI(Kg/m²：28.2\n吸烟：曾经(10/20)\n用力肺活量 Forced Vital Capacity\nF(l/s)\nV(l)\nBEST #3 - 2024/10/22 11:03\n沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38\n沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39\n沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41\n沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38\n沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39\n沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41\nMEF75%\nMEF50%\nMEF25%\nFVC\nPEF\nFEV1\nATS\n12t(s)\n-1\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n24\n25\n26\n27\n28\n29\n30\n31\n32\n33\n34\n35\n36\n37\n38\n39\n40\n41\n42\n43\n44\n45\n46\n47\n48\n49\n50\n51\n52\n53\n54\n55\n56\n57\n58\n59\n60\n61\n62\n63\n64\n65\n66\n67\n68\n69\n70\n71\n72\n73\n74\n75\n76\n77\n78\n79\n80\n81\n82\n83\n84\n85\n86\n87\n88\n89\n90\n91\n92\n93\n94\n95\n96\n97\n98\n99\n100\n101\n102\n103\n104\n105\n106\n107\n108\n109\n110\n111\n112\n113\n114\n115\n116\n117\n118\n119\n120\n121\n122\n123\n124\n125\n126\n127\n128\n129\n130\n131\n132\n133\n134\n135\n136\n137\n138\n139\n140\n141\n142\n143\n144\n145\n146\n147\n148\n149\n150\n151\n152\n153\n154\n155\n156\n157\n158\n159\n160\n161\n162\n163\n164\n165\n166\n167\n168\n169\n170\n171\n172\n173\n174\n175\n176\n177\n178\n179\n180\n181\n182\n183\n184\n185\n186\n187\n188\n189\n190\n191\n192\n193\n194\n195\n196\n197\n198\n199\n200\n201\n202\n203\n204\n205\n206\n207\n208\n209\n210\n211\n212\n213\n214\n215\n216\n217\n218\n219\n220\n221\n222\n223\n224\n225\n226\n227\n228\n229\n230\n231\n232\n233\n234\n235\n236\n237\n238\n239\n240\n241\n242\n243\n244\n245\n246\n247\n248\n249\n250\n251\n252\n253\n254\n255\n256\n257\n258\n259\n260\n261\n262\n263\n264\n265\n266\n267\n268\n269\n270\n271\n272\n273\n274\n275\n276\n277\n278\n279\n280\n281\n282\n283\n284\n285\n286\n287\n288\n289\n290\n291\n292\n293\n294\n295\n296\n297\n298\n299\n300\n301\n302\n303\n304\n305\n306\n307\n308\n309\n310\n311\n312\n313\n314\n315\n316\n317\n318\n319\n320\n321\n322\n323\n324\n325\n326\n327\n328\n329\n330\n331\n332\n333\n334\n335\n336\n337\n338\n339\n340\n341\n342\n343\n344\n345\n346\n347\n348\n349\n350\n351\n352\n353\n354\n355\n356\n357\n358\n359\n360\n361\n362\n363\n364\n365\n366\n367\n368\n369\n370\n371\n372\n373\n374\n375\n376\n377\n378\n379\n380\n381\n382\n383\n384\n385\n386\n387\n388\n389\n390\n391\n392\n393\n394\n395\n396\n397\n398\n399\n400\n401\n402\n403\n404\n405\n406\n407\n408\n409\n410\n411\n412\n413\n414\n415\n416\n417\n418\n419\n420\n421\n422\n423\n424\n425\n426\n427\n428\n429\n430\n431\n432\n433\n434\n435\n436\n437\n438\n439\n440\n441\n442\n443\n444\n445\n446\n447\n448\n449\n450\n451\n452\n453\n454\n455\n456\n457\n458\n459\n460\n461\n462\n463\n464\n465\n466\n467\n468\n469\n470\n471\n472\n473\n474\n475\n476\n477\n478\n479\n480\n481\n482\n483\n484\n485\n486\n487\n488\n489\n490\n491\n492\n493\n494\n495\n496\n497\n498\n499\n500\n501\n502\n503\n504\n505\n506\n507\n508\n509\n510\n511\n512\n513\n514\n515\n516\n517\n518\n519\n520\n521\n522\n523\n524\n525\n526\n527\n528\n529\n530\n531\n532\n533\n534\n535\n536\n537\n538\n539\n540\n541\n542\n543\n544\n545\n546\n547\n548\n549\n550\n551\n552\n553\n554\n555\n556\n557\n558\n559\n560\n561\n562\n563\n564\n565\n566\n567\n568\n569\n570\n571\n572\n573\n574\n575\n576\n577\n578\n579\n580\n581\n582\n583\n584\n585\n586\n587\n588\n589\n590\n591\n592\n593\n594\n595\n596\n597\n598\n599\n600\n601\n602\n603\n604\n605\n606\n607\n608\n609\n610\n611\n612\n613\n614\n615\n616\n617\n618\n619\n620\n621\n622\n623\n624\n625\n626\n627\n628\n629\n630\n631\n632\n633\n634\n635\n636\n637\n638\n639\n640\n641\n642\n643\n644\n645\n646\n647\n648\n649\n650\n651\n652\n653\n654\n655\n656\n657\n658\n659\n660\n661\n662\n663\n664\n665\n666\n667\n668\n669\n670\n671\n672\n673\n674\n675\n676\n677\n678\n679\n680\n681\n682\n683\n684\n685\n686\n687\n688\n689\n690\n691\n692\n693\n694\n695\n696\n697\n698\n699\n700\n701\n702\n703\n704\n705\n706\n707\n708\n709\n710\n711\n712\n713\n714\n715\n716\n717\n718\n719\n720\n721\n722\n723\n724\n725\n726\n727\n728\n729\n730\n731\n732\n733\n734\n735\n736\n737\n738\n739\n740\n741\n742\n743\n744\n745\n746\n747\n748\n749\n750\n751\n752\n753\n754\n755\n756\n757\n758\n759\n760\n761\n762\n763\n764\n765\n766\n767\n768\n769\n770\n771\n772\n773\n774\n775\n776\n777\n778\n779\n780\n781\n782\n783\n784\n785\n786\n787\n788\n789\n790\n791\n792\n793\n794\n795\n796\n797\n798\n799\n800\n801\n802\n803\n804\n805\n806\n807\n808\n809\n810\n811\n812\n813\n814\n815\n816\n817\n818\n819\n820\n821\n822\n823\n824\n825\n826\n827\n828\n829\n830\n831\n832\n833\n834\n835\n836\n837\n838\n839\n840\n841\n842\n843\n844\n845\n846\n847\n848\n849\n850\n851\n852\n853\n854\n855\n856\n857\n858\n859\n860\n861\n862\n863\n864\n865\n866\n867\n868\n869\n870\n871\n872\n873\n874\n875\n876\n877\n878\n879\n880\n881\n882\n883\n884\n885\n886\n887\n888\n889\n890\n891\n892\n893\n894\n895\n896\n897\n898\n899\n900\n901\n902\n903\n904\n905\n906\n907\n908\n909\n910\n911\n912\n913\n914\n915\n916\n917\n918\n919\n920\n921\n922\n923\n924\n925\n926\n927\n928\n929\n930\n931\n932\n933\n934\n935\n936\n937\n938\n939\n940\n941\n942\n943\n944\n945\n946\n947\n948\n949\n950\n951\n952\n953\n954\n955\n956\n957\n958\n959\n960\n961\n962\n963\n964\n965\n966\n967\n968\n969\n970\n971\n972\n973\n974\n975\n976\n977\n978\n979\n980\n981\n982\n983\n984\n985\n986\n987\n988\n989\n990\n991\n992\n993\n994\n995\n996\n997\n998\n999\n1000\n1001\n1002\n1003\n1004\n1005\n1006\n1007\n1008\n1009\n1010\n1011\n1012\n1013\n1014\n1015\n1016\n1017\n1018\n1019\n1020\n1021\n1022\n1023\n1024\n1025\n1026\n1027\n1028\n1029\n1030\n1031\n1032\n1033\n1034\n1035\n1036\n1037\n1038\n1039\n1040\n1041\n1042\n1043\n1044\n1045\n1046\n1047\n1048\n1049\n1050\n1051\n1052\n1053\n1054\n1055\n1056\n1057\n1058\n1059\n1060\n1061\n1062\n1063\n1064\n1065\n1066\n1067\n1068\n1069\n1070\n1071\n1072\n1073\n1074\n1075\n1076\n1077\n1078\n1079\n1080\n1081\n1082\n1083\n1084\n1085\n1086\n1087\n1088\n1089\n1090\n1091\n1092\n1093\n1094\n1095\n1096\n1097\n1098\n1099\n1100\n1101\n1102\n1103\n1104\n1105\n1106\n1107\n1108\n1109\n1110\n1111\n1112\n1113\n1114\n1115\n1116\n1117\n1118\n1119\n1120\n1121\n1122\n1123\n1124\n1125\n1126\n1127\n1128\n1129\n1130\n1131\n1132\n1133\n1134\n1135\n1136\n1137\n1138\n1139\n1140\n1141\n1142\n1143\n1144\n1145\n1146\n1147\n1148\n1149\n1150\n1151\n1152\n1153\n1154\n1155\n1156\n1157\n1158\n1159\n1160\n1161\n1162\n1163\n1164\n1165\n1166\n1167\n1168\n1169\n1170\n1171\n1172\n1173\n1174\n1175\n1176\n1177\n1178\n1179\n1180\n1181\n1182\n1183\n1184\n1185\n1186\n1187\n1188\n1189\n1190\n1191\n1192\n1193\n1194\n1195\n1196\n1197\n1198\n1199\n1200\n1201\n1202\n1203\n1204\n1205\n1206\n1207\n1208\n1209\n1210\n1211\n1212\n1213\n1214\n1215\n1216\n1217\n1218\n1219\n1220\n1221\n1222\n1223\n1224\n1225\n1226\n1227\n1228\n1229\n1230\n1231\n1232\n1233\n1234\n1235\n1236\n1237\n1238\n1239\n1240\n1241\n1242\n1243\n1244\n1245\n1246\n1247\n1248\n1249\n1250\n1251\n1252\n1253\n1254\n1255\n1256\n1257\n1258\n1259\n1260\n1261\n1262\n1263\n1264\n1265\n1266\n1267\n1268\n1269\n1270\n1271\n1272\n1273\n1274\n1275\n1276\n1277\n1278\n1279\n1280\n1281\n1282\n1283\n1284\n1285\n1286\n1287\n1288\n1289\n1290\n1291\n1292\n1293\n1294\n1295\n1296\n1297\n1298\n1299\n1300\n1301\n1302\n1303\n1304\n1305\n1306\n1307\n1308\n1309\n1310\n1311\n1312\n1313\n1314\n1315\n1316\n1317\n1318\n1319\n1320\n1321\n1322\n1323\n1324\n1325\n1326\n1327\n1328\n1329\n1330\n1331\n1332\n1333\n1334\n1335\n1336\n1337\n1338\n1339\n1340\n1341\n1342\n1343\n1344\n1345\n1346\n1347\n1348\n1349\n1350\n1351\n1352\n1353\n1354\n1355\n1356\n1357\n1358\n1359\n1360\n1361\n1362\n1363\n1364\n1365\n1366\n1367\n1368\n1369\n1370\n1371\n1372\n1373\n1374\n1375\n1376\n1377\n1378\n1379\n1380\n1381\n1382\n1383\n1384\n1385\n1386\n1387\n1388\n1389\n1390\n1391\n1392\n1393\n1394\n1395\n1396\n1397\n1398\n1399\n1400\n1401\n1402\n1403\n1404\n1405\n1406\n1407\n1408\n1409\n1410\n1411\n1412\n1413\n1414\n1415\n1416\n1417\n1418\n1419\n1420\n1421\n1422\n1423\n1424\n1425\n1426\n1427\n1428\n1429\n1430\n1431\n1432\n1433\n1434\n1435\n1436\n1437\n1438\n1439\n1440\n1441\n1442\n1443\n1444\n1445\n1446\n1447\n1448\n1449\n1450\n1451\n1452\n1453\n1454\n1455\n1456\n1457\n1458\n1459\n1460\n1461\n1462\n1463\n1464\n1465\n1466\n1467\n1468\n1469\n1470\n1471\n1472\n1473\n1474\n1475\n1476\n1477\n1478\n1479\n1480\n1481\n1482\n1483\n1484\n1485\n1486\n1487\n1488\n1489\n1490\n1491\n1492\n1493\n1494\n1495\n1496\n1497\n1498\n1499\n1500\n1501\n1502\n1503\n1504\n1505\n1506\n1507\n1508\n1509\n1510\n1511\n1512\n1513\n1514\n1515\n1516\n1517\n1518\n1519\n1520\n1521\n1522\n1523\n1524\n1525\n1526\n1527\n1528\n1529\n1530\n1531\n1532\n1533\n1534\n1535\n1536\n1537\n1538\n1539\n1540\n1541\n1542\n1543\n1544\n1545\n1546\n1547\n1548\n1549\n1550\n1551\n1552\n1553\n1554\n1555\n1556\n1557\n1558\n1559\n1560\n1561\n1562\n1563\n1564\n1565\n1566\n1567\n1568\n1569\n1570\n1571\n1572\n1573\n1574\n1575\n1576\n1577\n1578\n1579\n1580\n1581\n1582\n1583\n1584\n1585\n1586\n1587\n1588\n1589\n1590\n1591\n1592\n1593\n1594\n1595\n1596\n1597\n1598\n1599\n1600\n1601\n1602\n1603\n1604\n1605\n1606\n1607\n1608\n1609\n1610\n1611\n1612\n1613\n1614\n1615\n1616\n1617\n1618\n1619\n1620\n1621\n1622\n1623\n1624\n1625\n1626\n1627\n1628\n1629\n1630\n1631\n1632\n1633\n1634\n1635\n1636\n1637\n1638\n1639\n1640\n1641\n1642\n1643\n1644\n1645\n1646\n1647\n1648\n1649\n1650\n1651\n1652\n1653\n1654\n1655\n1656\n1657\n1658\n1659\n1660\n1661\n1662\n1663\n1664\n1665\n1666\n1667\n1668\n1669\n1670\n1671\n1672\n1673\n1674\n1675\n1676\n1677\n1678\n1679\n1680\n1681\n1682\n1683\n1684\n1685\n1686\n1687\n1688\n1689\n1690\n1691\n1692\n1693\n1694\n1695\n1696\n1697\n1698\n1699\n1700\n1701\n1702\n1703\n1704\n1705\n1706\n1707\n1708\n1709\n1710\n1711\n1712\n1713\n1714\n1715\n1716\n1717\n1718\n1719\n1720\n1721\n1722\n1723\n1724\n1725\n1726\n1727\n1728\n1729\n1730\n1731\n1732\n1733\n1734\n1735\n1736\n1737\n1738\n1739\n1740\n1741\n1742\n1743\n1744\n1745\n1746\n1747\n1748\n1749\n1750\n1751\n1752\n1753\n1754\n1755\n1756\n1757\n1758\n1759\n1760\n1761\n1762\n1763\n1764\n1765\n1766\n1767\n1768\n1769\n1770\n1771\n1772\n1773\n1774\n1775\n1776\n1777\n1778\n1779\n1780\n1781\n1782\n1783\n1784\n1785\n1786\n1787\n1788\n1789\n1790\n1791\n1792\n1793\n1794\n1795\n1796\n1797\n1798\n1799\n1800\n1801\n1802\n1803\n1804\n1805\n1806\n1807\n1808\n1809\n1810\n1811\n1812\n1813\n1814\n1815\n1816\n1817\n1818\n1819\n1820\n1821\n1822\n1823\n1824\n1825\n1826\n1827\n1828\n1829\n1830\n1831\n1832\n1833\n1834\n1835\n1836\n1837\n1838\n1839\n1840\n1841\n1842\n1843\n1844\n1845\n1846\n1847\n1848\n1849\n1850\n1851\n1852\n1853\n1854\n1855\n1856\n1857\n1858\n1859\n1860\n1861\n1862\n1863\n1864\n1865\n1866\n1867\n1868\n1869\n1870\n1871\n1872\n1873\n1874\n1875\n1876\n1877\n1878\n1879\n1880\n1881\n1882\n1883\n1884\n1885\n1886\n1887\n1888\n1889\n1890\n1891\n1892\n1893\n1894\n1895\n1896\n1897\n1898\n1899\n1900\n1901\n1902\n1903\n1904\n1905\n1906\n1907\n1908\n1909\n1910\n1911\n1912\n1913\n1914\n1915\n1916\n1917\n1918\n1919\n1920\n1921\n1922\n1923\n1924\n1925\n1926\n1927\n1928\n1929\n1930\n1931\n1932\n1933\n1934\n1935\n1936\n1937\n1938\n1939\n1940\n1941\n1942\n1943\n1944\n1945\n1946\n1947\n1948\n1949\n1950\n1951\n1952\n1953\n1954\n1955\n1956\n1957\n1958\n1959\n1960\n1961\n1962\n1963\n1964\n1965\n1966\n1967\n1968\n1969\n1970\n1971\n1972\n1973\n1974\n1975\n1976\n1977\n1978\n1979\n1980\n1981\n1982\n1983\n1984\n1985\n1986\n1987\n1988\n1989\n1990\n1991\n1992\n1993\n1994\n1995\n1996\n1997\n1998\n1999\n2000\n2001\n2002\n2003\n2004\n2005\n2006\n2007\n2008\n2009\n2010\n2011\n2012\n2013\n2014\n2015\n2016\n2017\n2018\n2019\n2020\n2021\n2022\n2023\n2024\n2025\n2026\n2027\n2028\n2029\n2030\n2031\n2032\n2033\n2034\n2035\n2036\n2037\n2038\n2039\n2040\n2041\n2042\n2043\n2044\n2045\n2046\n2047\n2048\n2049\n2050\n2051\n2052\n2053\n2054\n2055\n2056\n2057\n2058\n2059\n2060\n2061\n2062\n2063\n2064\n2065\n2066\n2067\n2068\n2069\n2070\n2071\n2072\n2073\n2074\n2075\n2076\n2077\n2078\n2079\n2080\n2081\n2082\n2083\n2084\n2085\n2086\n2087\n2088\n2089\n2090\n2091\n2092\n2093\n2094\n2095\n2096\n2097\n2098\n2099\n2100\n2101\n2102\n2103\n2104\n2105\n2106\n2107\n2108\n2109\n2110\n2111\n2112\n2113\n2114\n2115\n2116\n2117\n2118\n2119\n2120\n2121\n2122\n2123\n2124\n2125\n2126\n2127\n2128\n2129\n2130\n2131\n2132\n2133\n2134\n2135\n2136\n2137\n2138\n2139\n2140\n2141\n2142\n2143\n2144\n2145\n2146\n2147\n2148\n2149\n2150\n2151\n2152\n2153\n2154\n2155\n2156\n2157\n2158\n2159\n2160\n2161\n2162\n2163\n2164\n2165\n2166\n2167\n2168\n2169\n2170\n2171\n2172\n2173\n2174\n2175\n2176\n2177\n2178\n2179\n2180\n2181\n2182\n2183\n2184\n2185\n2186\n2187\n2188\n2189\n2190\n2191\n2192\n2193\n2194\n2195\n2196\n2197\n2198\n2199\n2200\n2201\n2202\n2203\n2204\n2205\n2206\n2207\n2208\n2209\n2210\n2211\n2212\n2213\n2214\n2215\n2216\n2217\n2218\n2219\n2220\n2221\n2222\n2223\n2224\n2225\n2226\n2227\n2228\n2229\n2230\n2231\n2232\n2233\n2234\n2235\n2236\n2237\n2238\n2239\n2240\n2241\n2242\n2243\n2244\n2245\n2246\n2247\n2248\n2249\n2250\n2251\n2252\n2253\n2254\n2255\n2256\n2257\n2258\n2259\n2260\n2261\n2262\n2263\n2264\n2265\n2266\n2267\n2268\n2269\n2270\n2271\n2272\n2273\n2274\n2275\n2276\n2277\n2278\n2279\n2280\n2281\n2282\n2283\n2284\n2285\n2286\n2287\n2288\n2289\n2290\n2291\n2292\n2293\n2294\n2295\n2296\n2297\n2298\n2299\n2300\n2301\n2302\n2303\n2304\n2305\n2306\n2307\n2308\n2309\n2310\n2311\n2312\n2313\n2314\n2315\n2316\n2317\n2318\n2319\n2320\n2321\n2322\n2323\n2324\n2325\n2326\n2327\n2328\n2329\n2330\n2331\n2332\n2333\n2334\n2335\n2336\n2337\n2338\n2339\n2340\n2341\n2342\n2343\n2344\n2345\n2346\n2347\n2348\n2349\n2350\n2351\n2352\n2353\n2354\n2355\n2356\n2357\n2358\n2359\n2360\n2361\n2362\n2363\n2364\n2365\n2366\n2367\n2368\n2369\n2370\n2371\n2372\n2373\n2374\n2375\n2376\n2377\n2378\n2379\n2380\n2381\n2382\n2383\n2384\n2385\n2386\n2387\n2388\n2389\n2390\n2391\n2392\n2393\n2394\n2395\n2396\n2397\n2398\n2399\n2400\n2401\n2402\n2403\n2404\n2405\n2406\n2407\n2408\n2409\n2410\n2411\n2412\n2413\n2414\n2415\n2416\n2417\n2418\n2419\n2420\n2421\n2422\n2423\n2424\n2425\n2426\n2427\n2428\n2429\n2430\n2431\n2432\n2433\n2434\n2435\n2436\n2437\n2438\n2439\n2440\n2441\n2442\n2443\n2444\n2445\n2446\n2447\n2448\n2449\n2450\n2451\n2452\n2453\n2454\n2455\n2456\n2457\n2458\n2459\n2460\n2461\n2462\n2463\n2464\n2465\n2466\n2467\n2468\n2469\n2470\n2471\n2472\n2473\n2474\n2475\n2476\n2477\n2478\n2479\n2480\n2481\n2482\n2483\n2484\n2485\n2486\n2487\n2488\n2489\n2490\n2491\n2492\n2493\n2494\n2495\n2496\n2497\n2498\n2499\n2500\n2501\n2502\n2503\n2504\n2505\n2506\n2507\n2508\n2509\n2510\n2511\n2512\n2513\n2514\n2515\n2516\n2517\n2518\n2519\n2520\n2521\n2522\n2523\n2524\n2525\n2526\n2527\n2528\n2529\n2530\n2531\n2532\n2533\n2534\n2535\n2536\n2537\n2538\n2539\n2540\n2541\n2542\n2543\n2544\n2545\n2546\n2547\n2548\n2549\n2550\n2551\n2552\n2553\n2554\n2555\n2556\n2557\n2558\n2559\n2560\n2561\n2562\n2563\n2564\n2565\n2566\n2567\n2568\n2569\n2570\n2571\n2572\n2573\n2574\n2575\n2576\n2577\n2578\n2579\n2580\n2581\n2582\n2583\n2584\n2585\n2586\n2587\n2588\n2589\n2590\n2591\n2592\n2593\n2594\n2595\n2596\n2597\n2598\n2599\n2600\n2601\n2602\n2603\n2604\n2605\n2606\n2607\n2608\n2609\n2610\n2611\n2612\n2613\n2614\n2615\n2616\n2617\n2618\n2619\n2620\n2621\n2622\n2623\n2624\n2625\n2626\n2627\n2628\n2629\n2630\n2631\n2632\n2633\n2634\n2635\n2636\n2637\n2638\n2639\n2640\n2641\n2642\n2643\n2644\n2645\n2646\n2647\n2648\n2649\n2650\n2651\n2652\n2653\n2654\n2655\n2656\n2657\n2658\n2659\n2660\n2661\n2662\n2663\n2664\n2665\n2666\n2667\n2668\n2669\n2670\n2671\n2672\n2673\n2674\n2675\n2676\n2677\n2678\n2679\n2680\n2681\n2682\n2683\n2684\n2685\n2686\n2687\n2688\n2689\n2690\n2691\n2692\n2693\n2694\n2695\n2696\n2697\n2698\n2699\n2700\n2701\n2702\n2703\n2704\n2705\n2706\n2707\n2708\n2709\n2710\n2711\n2712\n2713\n2714\n2715\n2716\n2717\n2718\n2719\n2720\n2721\n2722\n2723\n2724\n2725\n2726\n2727\n2728\n2729\n2730\n2731\n2732\n2733\n2734\n2735\n2736\n2737\n2738\n2739\n2740\n2741\n2742\n2743\n2744\n2745\n2746\n2747\n2748\n2749\n2750\n2751\n2752\n2753\n2754\n2755\n2756\n2757\n2758\n2759\n2760\n2761\n2762\n2763\n2764\n2765\n2766\n2767\n2768\n2769\n2770\n2771\n2772\n2773\n2774\n2775\n2776\n2777\n2778\n2779\n2780\n2781\n2782\n2783\n2784\n2785\n2786\n2787\n2788\n2789\n2790\n2791\n2792\n2793\n2794\n2795\n2796\n2797\n2798\n2799\n2800\n2801\n2802\n2803\n2804\n2805\n2806\n2807\n2808\n2809\n2810\n2811\n2812\n2813\n2814\n2815\n2816\n2817\n2818\n2819\n2820",
    "role": "user"
  }
]
[92m05:16:21 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:16:21,587 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:16:21,588 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:16:21.586+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 15, "failed": 0, "current": {"4e4700ce908b11f1a3da71efcdd7cc1f": {"id": "4e4700ce908b11f1a3da71efcdd7cc1f", "doc_id": "4e10ceb4908b11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906341337, "task_type": "dataflow", "root_trace_id": "ca345e6640ff4d788f444c3ab712853e", "root_traceparent": "00-ca345e6640ff4d788f444c3ab712853e-8ea193cced1ce3aa-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:16:28,151 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:16:28,152 INFO     29 [qwen-vl-text] LLM output (len=684):
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
  "findings": "出生日期：1984/12/8\n预计值：ERS 93\n日期：2024/10/22\n性别：Male\n地区修正：Chinese\n详细描述：内科门诊\n年龄：39\n体重(Kg)：89.0\n身高(cm)：177.5\nBMI(Kg/m²)：28.2\n吸烟：曾经(10/20)\n用力肺活量 Forced Vital Capacity\nBEST #3 - 2024/10/22 11:03\n沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38\n沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39\n沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41\nMEF75%\nMEF50%\nMEF25%\nFVC\nPEF\nFEV1\nATS",
  "conclusion": null,
  "physician": null,
  "reviewer": null
}
2026-08-05 05:16:28,159 INFO     29 [qwen-vl-text] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1606814, prompt_len=22902
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共2885行）
["广州医科大学附属第三医院", "肺功能检查报告", "地址：广州市多宝路63号 电话：020-81292126", "COSMED", "姓名：", "科室/床号：", "ID：", "出生日期：1984/12/8", "预计值：ERS 93", "日期：2024/10/22", "性别：Male", "地区修正：Chinese", "详细描述：内科门诊", "Company：", "年龄：39", "体重(Kg)：89.0", "身高(cm)：177.5", "BMI(Kg/m²：28.2", "吸烟：曾经(10/20)", "用力肺活量 Forced Vital Capacity", "F(l/s)", "V(l)", "BEST #3 - 2024/10/22 11:03", "沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38", "沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39", "沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41", "沙丁胺醇 (400.0000 mcg) #4 - 2024/10/22 11:38", "沙丁胺醇 (400.0000 mcg) #5 - 2024/10/22 11:39", "沙丁胺醇 (400.0000 mcg) #6 - 2024/10/22 11:41", "MEF75%", "MEF50%", "MEF25%", "FVC", "PEF", "FEV1", "ATS", "12t(s)", "-1", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120", "121", "122", "123", "124", "125", "126", "127", "128", "129", "130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "140", "141", "142", "143", "144", "145", "146", "147", "148", "149", "150", "151", "152", "153", "154", "155", "156", "157", "158", "159", "160", "161", "162", "163", "164", "165", "166", "167", "168", "169", "170", "171", "172", "173", "174", "175", "176", "177", "178", "179", "180", "181", "182", "183", "184", "185", "186", "187", "188", "189", "190", "191", "192", "193", "194", "195", "196", "197", "198", "199", "200", "201", "202", "203", "204", "205", "206", "207", "208", "209", "210", "211", "212", "213", "214", "215", "216", "217", "218", "219", "220", "221", "222", "223", "224", "225", "226", "227", "228", "229", "230", "231", "232", "233", "234", "235", "236", "237", "238", "239", "240", "241", "242", "243", "244", "245", "246", "247", "248", "249", "250", "251", "252", "253", "254", "255", "256", "257", "258", "259", "260", "261", "262", "263", "264", "265", "266", "267", "268", "269", "270", "271", "272", "273", "274", "275", "276", "277", "278", "279", "280", "281", "282", "283", "284", "285", "286", "287", "288", "289", "290", "291", "292", "293", "294", "295", "296", "297", "298", "299", "300", "301", "302", "303", "304", "305", "306", "307", "308", "309", "310", "311", "312", "313", "314", "315", "316", "317", "318", "319", "320", "321", "322", "323", "324", "325", "326", "327", "328", "329", "330", "331", "332", "333", "334", "335", "336", "337", "338", "339", "340", "341", "342", "343", "344", "345", "346", "347", "348", "349", "350", "351", "352", "353", "354", "355", "356", "357", "358", "359", "360", "361", "362", "363", "364", "365", "366", "367", "368", "369", "370", "371", "372", "373", "374", "375", "376", "377", "378", "379", "380", "381", "382", "383", "384", "385", "386", "387", "388", "389", "390", "391", "392", "393", "394", "395", "396", "397", "398", "399", "400", "401", "402", "403", "404", "405", "406", "407", "408", "409", "410", "411", "412", "413", "414", "415", "416", "417", "418", "419", "420", "421", "422", "423", "424", "425", "426", "427", "428", "429", "430", "431", "432", "433", "434", "435", "436", "437", "438", "439", "440", "441", "442", "443", "444", "445", "446", "447", "448", "449", "450", "451", "452", "453", "454", "455", "456", "457", "458", "459", "460", "461", "462", "463", "464", "465", "466", "467", "468", "469", "470", "471", "472", "473", "474", "475", "476", "477", "478", "479", "480", "481", "482", "483", "484", "485", "486", "487", "488", "489", "490", "491", "492", "493", "494", "495", "496", "497", "498", "499", "500", "501", "502", "503", "504", "505", "506", "507", "508", "509", "510", "511", "512", "513", "514", "515", "516", "517", "518", "519", "520", "521", "522", "523", "524", "525", "526", "527", "528", "529", "530", "531", "532", "533", "534", "535", "536", "537", "538", "539", "540", "541", "542", "543", "544", "545", "546", "547", "548", "549", "550", "551", "552", "553", "554", "555", "556", "557", "558", "559", "560", "561", "562", "563", "564", "565", "566", "567", "568", "569", "570", "571", "572", "573", "574", "575", "576", "577", "578", "579", "580", "581", "582", "583", "584", "585", "586", "587", "588", "589", "590", "591", "592", "593", "594", "595", "596", "597", "598", "599", "600", "601", "602", "603", "604", "605", "606", "607", "608", "609", "610", "611", "612", "613", "614", "615", "616", "617", "618", "619", "620", "621", "622", "623", "624", "625", "626", "627", "628", "629", "630", "631", "632", "633", "634", "635", "636", "637", "638", "639", "640", "641", "642", "643", "644", "645", "646", "647", "648", "649", "650", "651", "652", "653", "654", "655", "656", "657", "658", "659", "660", "661", "662", "663", "664", "665", "666", "667", "668", "669", "670", "671", "672", "673", "674", "675", "676", "677", "678", "679", "680", "681", "682", "683", "684", "685", "686", "687", "688", "689", "690", "691", "692", "693", "694", "695", "696", "697", "698", "699", "700", "701", "702", "703", "704", "705", "706", "707", "708", "709", "710", "711", "712", "713", "714", "715", "716", "717", "718", "719", "720", "721", "722", "723", "724", "725", "726", "727", "728", "729", "730", "731", "732", "733", "734", "735", "736", "737", "738", "739", "740", "741", "742", "743", "744", "745", "746", "747", "748", "749", "750", "751", "752", "753", "754", "755", "756", "757", "758", "759", "760", "761", "762", "763", "764", "765", "766", "767", "768", "769", "770", "771", "772", "773", "774", "775", "776", "777", "778", "779", "780", "781", "782", "783", "784", "785", "786", "787", "788", "789", "790", "791", "792", "793", "794", "795", "796", "797", "798", "799", "800", "801", "802", "803", "804", "805", "806", "807", "808", "809", "810", "811", "812", "813", "814", "815", "816", "817", "818", "819", "820", "821", "822", "823", "824", "825", "826", "827", "828", "829", "830", "831", "832", "833", "834", "835", "836", "837", "838", "839", "840", "841", "842", "843", "844", "845", "846", "847", "848", "849", "850", "851", "852", "853", "854", "855", "856", "857", "858", "859", "860", "861", "862", "863", "864", "865", "866", "867", "868", "869", "870", "871", "872", "873", "874", "875", "876", "877", "878", "879", "880", "881", "882", "883", "884", "885", "886", "887", "888", "889", "890", "891", "892", "893", "894", "895", "896", "897", "898", "899", "900", "901", "902", "903", "904", "905", "906", "907", "908", "909", "910", "911", "912", "913", "914", "915", "916", "917", "918", "919", "920", "921", "922", "923", "924", "925", "926", "927", "928", "929", "930", "931", "932", "933", "934", "935", "936", "937", "938", "939", "940", "941", "942", "943", "944", "945", "946", "947", "948", "949", "950", "951", "952", "953", "954", "955", "956", "957", "958", "959", "960", "961", "962", "963", "964", "965", "966", "967", "968", "969", "970", "971", "972", "973", "974", "975", "976", "977", "978", "979", "980", "981", "982", "983", "984", "985", "986", "987", "988", "989", "990", "991", "992", "993", "994", "995", "996", "997", "998", "999", "1000", "1001", "1002", "1003", "1004", "1005", "1006", "1007", "1008", "1009", "1010", "1011", "1012", "1013", "1014", "1015", "1016", "1017", "1018", "1019", "1020", "1021", "1022", "1023", "1024", "1025", "1026", "1027", "1028", "1029", "1030", "1031", "1032", "1033", "1034", "1035", "1036", "1037", "1038", "1039", "1040", "1041", "1042", "1043", "1044", "1045", "1046", "1047", "1048", "1049", "1050", "1051", "1052", "1053", "1054", "1055", "1056", "1057", "1058", "1059", "1060", "1061", "1062", "1063", "1064", "1065", "1066", "1067", "1068", "1069", "1070", "1071", "1072", "1073", "1074", "1075", "1076", "1077", "1078", "1079", "1080", "1081", "1082", "1083", "1084", "1085", "1086", "1087", "1088", "1089", "1090", "1091", "1092", "1093", "1094", "1095", "1096", "1097", "1098", "1099", "1100", "1101", "1102", "1103", "1104", "1105", "1106", "1107", "1108", "1109", "1110", "1111", "1112", "1113", "1114", "1115", "1116", "1117", "1118", "1119", "1120", "1121", "1122", "1123", "1124", "1125", "1126", "1127", "1128", "1129", "1130", "1131", "1132", "1133", "1134", "1135", "1136", "1137", "1138", "1139", "1140", "1141", "1142", "1143", "1144", "1145", "1146", "1147", "1148", "1149", "1150", "1151", "1152", "1153", "1154", "1155", "1156", "1157", "1158", "1159", "1160", "1161", "1162", "1163", "1164", "1165", "1166", "1167", "1168", "1169", "1170", "1171", "1172", "1173", "1174", "1175", "1176", "1177", "1178", "1179", "1180", "1181", "1182", "1183", "1184", "1185", "1186", "1187", "1188", "1189", "1190", "1191", "1192", "1193", "1194", "1195", "1196", "1197", "1198", "1199", "1200", "1201", "1202", "1203", "1204", "1205", "1206", "1207", "1208", "1209", "1210", "1211", "1212", "1213", "1214", "1215", "1216", "1217", "1218", "1219", "1220", "1221", "1222", "1223", "1224", "1225", "1226", "1227", "1228", "1229", "1230", "1231", "1232", "1233", "1234", "1235", "1236", "1237", "1238", "1239", "1240", "1241", "1242", "1243", "1244", "1245", "1246", "1247", "1248", "1249", "1250", "1251", "1252", "1253", "1254", "1255", "1256", "1257", "1258", "1259", "1260", "1261", "1262", "1263", "1264", "1265", "1266", "1267", "1268", "1269", "1270", "1271", "1272", "1273", "1274", "1275", "1276", "1277", "1278", "1279", "1280", "1281", "1282", "1283", "1284", "1285", "1286", "1287", "1288", "1289", "1290", "1291", "1292", "1293", "1294", "1295", "1296", "1297", "1298", "1299", "1300", "1301", "1302", "1303", "1304", "1305", "1306", "1307", "1308", "1309", "1310", "1311", "1312", "1313", "1314", "1315", "1316", "1317", "1318", "1319", "1320", "1321", "1322", "1323", "1324", "1325", "1326", "1327", "1328", "1329", "1330", "1331", "1332", "1333", "1334", "1335", "1336", "1337", "1338", "1339", "1340", "1341", "1342", "1343", "1344", "1345", "1346", "1347", "1348", "1349", "1350", "1351", "1352", "1353", "1354", "1355", "1356", "1357", "1358", "1359", "1360", "1361", "1362", "1363", "1364", "1365", "1366", "1367", "1368", "1369", "1370", "1371", "1372", "1373", "1374", "1375", "1376", "1377", "1378", "1379", "1380", "1381", "1382", "1383", "1384", "1385", "1386", "1387", "1388", "1389", "1390", "1391", "1392", "1393", "1394", "1395", "1396", "1397", "1398", "1399", "1400", "1401", "1402", "1403", "1404", "1405", "1406", "1407", "1408", "1409", "1410", "1411", "1412", "1413", "1414", "1415", "1416", "1417", "1418", "1419", "1420", "1421", "1422", "1423", "1424", "1425", "1426", "1427", "1428", "1429", "1430", "1431", "1432", "1433", "1434", "1435", "1436", "1437", "1438", "1439", "1440", "1441", "1442", "1443", "1444", "1445", "1446", "1447", "1448", "1449", "1450", "1451", "1452", "1453", "1454", "1455", "1456", "1457", "1458", "1459", "1460", "1461", "1462", "1463", "1464", "1465", "1466", "1467", "1468", "1469", "1470", "1471", "1472", "1473", "1474", "1475", "1476", "1477", "1478", "1479", "1480", "1481", "1482", "1483", "1484", "1485", "1486", "1487", "1488", "1489", "1490", "1491", "1492", "1493", "1494", "1495", "1496", "1497", "1498", "1499", "1500", "1501", "1502", "1503", "1504", "1505", "1506", "1507", "1508", "1509", "1510", "1511", "1512", "1513", "1514", "1515", "1516", "1517", "1518", "1519", "1520", "1521", "1522", "1523", "1524", "1525", "1526", "1527", "1528", "1529", "1530", "1531", "1532", "1533", "1534", "1535", "1536", "1537", "1538", "1539", "1540", "1541", "1542", "1543", "1544", "1545", "1546", "1547", "1548", "1549", "1550", "1551", "1552", "1553", "1554", "1555", "1556", "1557", "1558", "1559", "1560", "1561", "1562", "1563", "1564", "1565", "1566", "1567", "1568", "1569", "1570", "1571", "1572", "1573", "1574", "1575", "1576", "1577", "1578", "1579", "1580", "1581", "1582", "1583", "1584", "1585", "1586", "1587", "1588", "1589", "1590", "1591", "1592", "1593", "1594", "1595", "1596", "1597", "1598", "1599", "1600", "1601", "1602", "1603", "1604", "1605", "1606", "1607", "1608", "1609", "1610", "1611", "1612", "1613", "1614", "1615", "1616", "1617", "1618", "1619", "1620", "1621", "1622", "1623", "1624", "1625", "1626", "1627", "1628", "1629", "1630", "1631", "1632", "1633", "1634", "1635", "1636", "1637", "1638", "1639", "1640", "1641", "1642", "1643", "1644", "1645", "1646", "1647", "1648", "1649", "1650", "1651", "1652", "1653", "1654", "1655", "1656", "1657", "1658", "1659", "1660", "1661", "1662", "1663", "1664", "1665", "1666", "1667", "1668", "1669", "1670", "1671", "1672", "1673", "1674", "1675", "1676", "1677", "1678", "1679", "1680", "1681", "1682", "1683", "1684", "1685", "1686", "1687", "1688", "1689", "1690", "1691", "1692", "1693", "1694", "1695", "1696", "1697", "1698", "1699", "1700", "1701", "1702", "1703", "1704", "1705", "1706", "1707", "1708", "1709", "1710", "1711", "1712", "1713", "1714", "1715", "1716", "1717", "1718", "1719", "1720", "1721", "1722", "1723", "1724", "1725", "1726", "1727", "1728", "1729", "1730", "1731", "1732", "1733", "1734", "1735", "1736", "1737", "1738", "1739", "1740", "1741", "1742", "1743", "1744", "1745", "1746", "1747", "1748", "1749", "1750", "1751", "1752", "1753", "1754", "1755", "1756", "1757", "1758", "1759", "1760", "1761", "1762", "1763", "1764", "1765", "1766", "1767", "1768", "1769", "1770", "1771", "1772", "1773", "1774", "1775", "1776", "1777", "1778", "1779", "1780", "1781", "1782", "1783", "1784", "1785", "1786", "1787", "1788", "1789", "1790", "1791", "1792", "1793", "1794", "1795", "1796", "1797", "1798", "1799", "1800", "1801", "1802", "1803", "1804", "1805", "1806", "1807", "1808", "1809", "1810", "1811", "1812", "1813", "1814", "1815", "1816", "1817", "1818", "1819", "1820", "1821", "1822", "1823", "1824", "1825", "1826", "1827", "1828", "1829", "1830", "1831", "1832", "1833", "1834", "1835", "1836", "1837", "1838", "1839", "1840", "1841", "1842", "1843", "1844", "1845", "1846", "1847", "1848", "1849", "1850", "1851", "1852", "1853", "1854", "1855", "1856", "1857", "1858", "1859", "1860", "1861", "1862", "1863", "1864", "1865", "1866", "1867", "1868", "1869", "1870", "1871", "1872", "1873", "1874", "1875", "1876", "1877", "1878", "1879", "1880", "1881", "1882", "1883", "1884", "1885", "1886", "1887", "1888", "1889", "1890", "1891", "1892", "1893", "1894", "1895", "1896", "1897", "1898", "1899", "1900", "1901", "1902", "1903", "1904", "1905", "1906", "1907", "1908", "1909", "1910", "1911", "1912", "1913", "1914", "1915", "1916", "1917", "1918", "1919", "1920", "1921", "1922", "1923", "1924", "1925", "1926", "1927", "1928", "1929", "1930", "1931", "1932", "1933", "1934", "1935", "1936", "1937", "1938", "1939", "1940", "1941", "1942", "1943", "1944", "1945", "1946", "1947", "1948", "1949", "1950", "1951", "1952", "1953", "1954", "1955", "1956", "1957", "1958", "1959", "1960", "1961", "1962", "1963", "1964", "1965", "1966", "1967", "1968", "1969", "1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034", "2035", "2036", "2037", "2038", "2039", "2040", "2041", "2042", "2043", "2044", "2045", "2046", "2047", "2048", "2049", "2050", "2051", "2052", "2053", "2054", "2055", "2056", "2057", "2058", "2059", "2060", "2061", "2062", "2063", "2064", "2065", "2066", "2067", "2068", "2069", "2070", "2071", "2072", "2073", "2074", "2075", "2076", "2077", "2078", "2079", "2080", "2081", "2082", "2083", "2084", "2085", "2086", "2087", "2088", "2089", "2090", "2091", "2092", "2093", "2094", "2095", "2096", "2097", "2098", "2099", "2100", "2101", "2102", "2103", "2104", "2105", "2106", "2107", "2108", "2109", "2110", "2111", "2112", "2113", "2114", "2115", "2116", "2117", "2118", "2119", "2120", "2121", "2122", "2123", "2124", "2125", "2126", "2127", "2128", "2129", "2130", "2131", "2132", "2133", "2134", "2135", "2136", "2137", "2138", "2139", "2140", "2141", "2142", "2143", "2144", "2145", "2146", "2147", "2148", "2149", "2150", "2151", "2152", "2153", "2154", "2155", "2156", "2157", "2158", "2159", "2160", "2161", "2162", "2163", "2164", "2165", "2166", "2167", "2168", "2169", "2170", "2171", "2172", "2173", "2174", "2175", "2176", "2177", "2178", "2179", "2180", "2181", "2182", "2183", "2184", "2185", "2186", "2187", "2188", "2189", "2190", "2191", "2192", "2193", "2194", "2195", "2196", "2197", "2198", "2199", "2200", "2201", "2202", "2203", "2204", "2205", "2206", "2207", "2208", "2209", "2210", "2211", "2212", "2213", "2214", "2215", "2216", "2217", "2218", "2219", "2220", "2221", "2222", "2223", "2224", "2225", "2226", "2227", "2228", "2229", "2230", "2231", "2232", "2233", "2234", "2235", "2236", "2237", "2238", "2239", "2240", "2241", "2242", "2243", "2244", "2245", "2246", "2247", "2248", "2249", "2250", "2251", "2252", "2253", "2254", "2255", "2256", "2257", "2258", "2259", "2260", "2261", "2262", "2263", "2264", "2265", "2266", "2267", "2268", "2269", "2270", "2271", "2272", "2273", "2274", "2275", "2276", "2277", "2278", "2279", "2280", "2281", "2282", "2283", "2284", "2285", "2286", "2287", "2288", "2289", "2290", "2291", "2292", "2293", "2294", "2295", "2296", "2297", "2298", "2299", "2300", "2301", "2302", "2303", "2304", "2305", "2306", "2307", "2308", "2309", "2310", "2311", "2312", "2313", "2314", "2315", "2316", "2317", "2318", "2319", "2320", "2321", "2322", "2323", "2324", "2325", "2326", "2327", "2328", "2329", "2330", "2331", "2332", "2333", "2334", "2335", "2336", "2337", "2338", "2339", "2340", "2341", "2342", "2343", "2344", "2345", "2346", "2347", "2348", "2349", "2350", "2351", "2352", "2353", "2354", "2355", "2356", "2357", "2358", "2359", "2360", "2361", "2362", "2363", "2364", "2365", "2366", "2367", "2368", "2369", "2370", "2371", "2372", "2373", "2374", "2375", "2376", "2377", "2378", "2379", "2380", "2381", "2382", "2383", "2384", "2385", "2386", "2387", "2388", "2389", "2390", "2391", "2392", "2393", "2394", "2395", "2396", "2397", "2398", "2399", "2400", "2401", "2402", "2403", "2404", "2405", "2406", "2407", "2408", "2409", "2410", "2411", "2412", "2413", "2414", "2415", "2416", "2417", "2418", "2419", "2420", "2421", "2422", "2423", "2424", "2425", "2426", "2427", "2428", "2429", "2430", "2431", "2432", "2433", "2434", "2435", "2436", "2437", "2438", "2439", "2440", "2441", "2442", "2443", "2444", "2445", "2446", "2447", "2448", "2449", "2450", "2451", "2452", "2453", "2454", "2455", "2456", "2457", "2458", "2459", "2460", "2461", "2462", "2463", "2464", "2465", "2466", "2467", "2468", "2469", "2470", "2471", "2472", "2473", "2474", "2475", "2476", "2477", "2478", "2479", "2480", "2481", "2482", "2483", "2484", "2485", "2486", "2487", "2488", "2489", "2490", "2491", "2492", "2493", "2494", "2495", "2496", "2497", "2498", "2499", "2500", "2501", "2502", "2503", "2504", "2505", "2506", "2507", "2508", "2509", "2510", "2511", "2512", "2513", "2514", "2515", "2516", "2517", "2518", "2519", "2520", "2521", "2522", "2523", "2524", "2525", "2526", "2527", "2528", "2529", "2530", "2531", "2532", "2533", "2534", "2535", "2536", "2537", "2538", "2539", "2540", "2541", "2542", "2543", "2544", "2545", "2546", "2547", "2548", "2549", "2550", "2551", "2552", "2553", "2554", "2555", "2556", "2557", "2558", "2559", "2560", "2561", "2562", "2563", "2564", "2565", "2566", "2567", "2568", "2569", "2570", "2571", "2572", "2573", "2574", "2575", "2576", "2577", "2578", "2579", "2580", "2581", "2582", "2583", "2584", "2585", "2586", "2587", "2588", "2589", "2590", "2591", "2592", "2593", "2594", "2595", "2596", "2597", "2598", "2599", "2600", "2601", "2602", "2603", "2604", "2605", "2606", "2607", "2608", "2609", "2610", "2611", "2612", "2613", "2614", "2615", "2616", "2617", "2618", "2619", "2620", "2621", "2622", "2623", "2624", "2625", "2626", "2627", "2628", "2629", "2630", "2631", "2632", "2633", "2634", "2635", "2636", "2637", "2638", "2639", "2640", "2641", "2642", "2643", "2644", "2645", "2646", "2647", "2648", "2649", "2650", "2651", "2652", "2653", "2654", "2655", "2656", "2657", "2658", "2659", "2660", "2661", "2662", "2663", "2664", "2665", "2666", "2667", "2668", "2669", "2670", "2671", "2672", "2673", "2674", "2675", "2676", "2677", "2678", "2679", "2680", "2681", "2682", "2683", "2684", "2685", "2686", "2687", "2688", "2689", "2690", "2691", "2692", "2693", "2694", "2695", "2696", "2697", "2698", "2699", "2700", "2701", "2702", "2703", "2704", "2705", "2706", "2707", "2708", "2709", "2710", "2711", "2712", "2713", "2714", "2715", "2716", "2717", "2718", "2719", "2720", "2721", "2722", "2723", "2724", "2725", "2726", "2727", "2728", "2729", "2730", "2731", "2732", "2733", "2734", "2735", "2736", "2737", "2738", "2739", "2740", "2741", "2742", "2743", "2744", "2745", "2746", "2747", "2748", "2749", "2750", "2751", "2752", "2753", "2754", "2755", "2756", "2757", "2758", "2759", "2760", "2761", "2762", "2763", "2764", "2765", "2766", "2767", "2768", "2769", "2770", "2771", "2772", "2773", "2774", "2775", "2776", "2777", "2778", "2779", "2780", "2781", "2782", "2783", "2784", "2785", "2786", "2787", "2788", "2789", "2790", "2791", "2792", "2793", "2794", "2795", "2796", "2797", "2798", "2799", "2800", "2801", "2802", "2803", "2804", "2805", "2806", "2807", "2808", "2809", "2810", "2811", "2812", "2813", "2814", "2815", "2816", "2817", "2818", "2819", "2820"]

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
2026-08-05 05:16:33,916 INFO     29 [qwen-vl-text] coord API raw response (len=2):
[]
2026-08-05 05:16:33,916 INFO     29 [qwen-vl-text] coord API: raw_items=0, valid_items=0, elapsed=5.8s
2026-08-05 05:16:33,917 WARNING  29 [qwen-vl-text] page=15 coord failed: ok, adding 2885 placeholder(s)
2026-08-05 05:16:33,918 INFO     29 [qwen-vl-text] new_positions (2885):
[[15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0]]
2026-08-05 05:16:33,918 INFO     29 [qwen-vl-text] ═══ DONE ═══ 2885 positions, pages=1, time=12.5s
2026-08-05 05:16:33,924 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-05 05:16:33,925 INFO     29 [Trace] task=4e4700ce | doc=LZK 哮喘 广三(1).pdf | Extractor:ExaminationReport | outputs={"chunks": "3 items, types={'ExaminationReport': 3}", "html": "", "json": "3681 items", "markdown": "", "text": "", "name": "LZK 哮喘 广三(1).pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Prescription": "7 items, types={'PrescriptionRecord': 7}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Prescription\": 7, \"chunks_Examination\": 3}"}
2026-08-05 05:16:33,925 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-05 05:16:33,929 INFO     29 [ChunkMerger] Merged 13 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 3, 'Extractor:Medication': 1, 'Extractor:Prescription': 7, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 3} (filtered 5 noise chunks)
2026-08-05 05:16:33,937 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-05 05:16:33,938 INFO     29 [Trace] task=4e4700ce | doc=LZK 哮喘 广三(1).pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "13 items, types={'OutpatientRecord': 3, 'PrescriptionRecord': 7, 'ExaminationReport': 3}", "name": "LZK 哮喘 广三(1).pdf"}
2026-08-05 05:16:33,938 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-05 05:16:34,168 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1785906342645, 'update_date': datetime.datetime(2026, 8, 5, 5, 5, 42), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 181398, 'status': '1'}
2026-08-05 05:16:34,390 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=病历编号：
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
CS 扫描全能王
3亿人都在用的扫描App
病历文书
门诊病历
25/10/10 14时 门诊病历
25/10/24 15时 门诊病历（GCP专用）
25/11/17 10时 门诊病历
头降使用40瓶，平均每天使用4瓶，2025年9月10日用完4瓶（未使用试验药剂空瓶2次共4
瓶，2025年9月10日后受试者每七天首先一次后空瓶5次共10瓶，总计使用10瓶（记录使
用总共46瓶，与实际使用情况一致。
8、回访ePRO以及MD。
既往史：更新合并用药：
1、鼻腔莫米松鼻喷雾剂C025 4 3-2025 7 25 每鼻 2喷/次 qd 治疗过敏性鼻炎。
2、苯环喹莫铵鼻喷雾剂 2025 4 3-至今每鼻 2喷/次 gid 治疗过敏性鼻炎。
4、氯卓斯汀盐酸卡松鼻喷雾剂 2025 9 3-至今 每鼻 2喷/次 bid 治疗过敏性鼻炎。
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
2布地奈德福莫特罗吸入粉雾剂(II)(省采)●①② 2盒2 000.00入用药,一天2次
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
3、更正2025年1月24日病历，“无收到ePro触发的哮喘警报邮件”为“有收到ePro触发的哮
喘警报邮件”；
4、更正2025年7月18日病历，“受试者漏填2025年4月28日晚间日志” 更正为：“受试者
漏填2025年4月28日早间日志”；
5、更正2024年11月6日病历，“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共
计用了26喷”为：“回收硫酸沙丁胺醇吸入气雾剂，核实电子日志填写无误，共计用了28
喷”。
医生
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
涕、嗅觉,无咽痛,无伴反酸、嗳气、腹胀,无上腹部隐痛不适感,无伴发热、畏寒,影响
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
就诊卡号：
病历编号：
姓名：
性别：男
年龄：41岁
就诊科室：内科门诊（荔湾）
就诊时间：2026-02-04 11:21:11
主诉：支气管哮喘治疗后复查
现病史：2021年2月前开始出现咳嗽、咳痰，粘白，量中，能咳出，咳嗽呈阵发性，刺激性，伴咽痒，咳嗽以夜间明显，自觉有吸入性呼吸困难，伴喘息，无胸闷，曾有鼻塞、流涕、喷嚏，无咽痛，无伴反酸、嗳气、腹胀，无上腹前隐痛不适感，无伴发热，畏寒，影响睡眠，晨起有咽干，曾到本院就诊两次，症状不见明显缓解。2021-1-9血常规：白细胞：12.52*109/L 嗜酸性粒细胞：0.65*109/L 5.2%。经治疗后症状明显缓解，无咳嗽、咯痰、气促，病情稳定，本次门诊距上次门诊间隔时间30天，症状控制情况：过去4周，患者：吸入药物使用情况：遵医嘱使用；吸入装置使用情况：正确，急性发作情况：两次，就诊期间急性发作：无，发作次数：0次，病情稳定无诉不适，流涕、鼻塞、喷嚏，长期规律使用信必可160/4 Sg 2吸 bid治疗。
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
布地奈德福莫特罗吸入粉雾剂(II)0.5mg*60吸6盒
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
布地奈德福莫特罗吸入粉雾剂BDI/●@1g*60吸2盒
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
布地奈德福莫特罗吸入粉雾剂HIV●(50ug*60吸4盒
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
CS 扫描全能王
3亿人都在用的扫描App
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
CS 扫描全能王
3亿人都在用的扫描App
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
V backextrapolation ex [L]
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
CS 扫描全能王
3亿人都在用的扫描App
检查日期：2021/1/21
检查时间：16.43
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
MEF75%
MEF50%
MEF25%
FVC
PEF
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
2815
2816
2817
2818
2819
2820
2026-08-05 05:16:35,948 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-05 05:16:35,948 INFO     29 [Trace] task=4e4700ce | doc=LZK 哮喘 广三(1).pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "13 items, types={'OutpatientRecord': 3, 'PrescriptionRecord': 7, 'ExaminationReport': 3}", "name": "LZK 哮喘 广三(1).pdf", "embedding_token_consumption": 21128}
2026-08-05 05:16:35,948 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-05 05:16:36,185 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-05 05:16:36,185 INFO     29 [Trace] task=4e4700ce | doc=LZK 哮喘 广三(1).pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":13,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-05 05:16:36,201 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:16:36,201 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:16:36,201 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:16:36,201 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:16:36,201 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:16:36,202 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:16:36,202 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:16:36,202 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:16:36,202 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:16:36,202 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:16:36,202 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:16:36,202 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:16:36,204 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:16:36,209 INFO     29 set_progress(4e4700ce908b11f1a3da71efcdd7cc1f), progress: 0.82, progress_msg: 05:16:36 [DOC Engine]:
Start to index...
2026-08-05 05:16:36,241 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.025s]
2026-08-05 05:16:36,246 INFO     29 set_progress(4e4700ce908b11f1a3da71efcdd7cc1f), progress: 0.8076923076923077, progress_msg: 
2026-08-05 05:16:36,269 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.016s]
2026-08-05 05:16:36,302 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.021s]
2026-08-05 05:16:36,327 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.014s]
2026-08-05 05:16:36,338 INFO     29 set_progress(4e4700ce908b11f1a3da71efcdd7cc1f), progress: 1.0, progress_msg: 05:16:36 Indexing done (0.13s). Task done (597.77s)
2026-08-05 05:16:36,343 INFO     29 [Done], chunks(13), token(21128), elapsed:597.77
2026-08-05 05:16:36,763 INFO     29 handle_task done for task {"id": "4e4700ce908b11f1a3da71efcdd7cc1f", "doc_id": "4e10ceb4908b11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "type": "pdf", "location": "LZK \u54ee\u5598 \u5e7f\u4e09(1).pdf", "size": 5453134, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1785906341337, "task_type": "dataflow", "root_trace_id": "ca345e6640ff4d788f444c3ab712853e", "root_traceparent": "00-ca345e6640ff4d788f444c3ab712853e-8ea193cced1ce3aa-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
