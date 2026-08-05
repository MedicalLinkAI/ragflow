# 基准结果：HXJ 哮喘 广三.pdf

## 基本信息

- 文件：`HXJ 哮喘 广三.pdf`
- 大小：8215.2 KB
- PDF 总页数：17
- doc_id：`32f80906908811f1a3da71efcdd7cc1f`
- 上传方式：existing
- 状态：run=None (code=None)  progress=None
- 开始时间：2026-08-05T14:31:11  完成时间：2026-08-05T14:31:12  耗时：0.9s
- progress_msg：`04:49:57 Indexing done (0.08s). Task done (355.24s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | f8f75cd1 | 1 | 1-1 | 门(急)诊病历信息 就诊卡 流水 病历编号: 姓 别:男 年 龄:64岁 就诊科 |
| 2 | d0800dfd | 1 | 2-2 | 门(急)诊病历信息 就诊卡号: 流水号: 病历编号: 性别:男 年 龄:65岁  |
| 3 | bd1e77f7 | 2 | 3-4 | 门(急)诊病历信息 就诊卡号 流水 姓名 性别:男 年 龄:65岁 就诊科室:内 |
| 4 | 8b9dd810 | 1 | 5-5 | 门(急)诊处方 就诊时间:2025-09-15 就诊科室:内科门诊 主诊医 姓名 |
| 5 | 0f2106d0 | 1 | 6-6 | 门(急)诊处方 就诊时间:2025-08-18 就诊科室:内科门诊 主诊 姓名: |
| 6 | a3fd25cc | 1 | 7-7 | 门(急)诊处方 就诊时间:2025-05-30 就诊科室:内科门诊 主 姓名 性 |
| 7 | 3eab1f20 | 1 | 8-8 | 门(急)诊处方 就诊时间:2025-03-05 就诊科室:内科门诊 主诊医 姓名 |
| 8 | 1c5fb903 | 1 | 9-9 | 门(急)诊处方 就诊时间:2025-03-05 就诊科室:内科门诊 主诊 姓名  |
| 9 | dd98b16f | 1 | 10-10 | 门(急)诊处方 就诊时间:2025-02-08 就诊科室:内科门诊 主诊 姓名: |
| 10 | 574d80b9 | 1 | 11-11 | 门(急)诊处方 就诊时间:2025-01-10 就诊科室:内科门诊 主诊 性别: |
| 11 | c77c2188 | 1 | 12-12 | 门(急)诊处方 就诊时间:2024-12-11 就诊科室:内科门诊 主诊 姓名: |
| 12 | a779f1ed | 1 | 13-13 | 门(急)诊处方 就诊时间:2024-11-18 就诊科室:内科门诊 主诊 姓名  |
| 13 | 3d411271 | 1 | 15-15 | 处方笺 普通 诊疗 患者姓 男 年龄：65岁 费别： 科室： 2026-01-0 |
| 14 | c297c088 | 1 | 16-16 | 处方笺 普通 诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿 |
| 15 | 0bcbb185 | 1 | 17-17 | 病历编号： 姓名： 性别：男 年龄：65岁 就诊科室：内科门诊（基础） 医生：  |
| 16 | 8d4ed12a | 1 | 14-14 | <table><tr><td>白细胞</td><td>WBC</td><td>9 |

- chunks 总数：16
- 各 chunk 页数合计（含跨页重复）：17
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]`
- 覆盖页数：17 / 17；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 4 | 0 | 4 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 11 | 11 | 11 | encounter_date, prescriber, diagnosis | **OK** |
| ExaminationReport | 检查报告 | 0 | 1 | 0 | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 1 | 0 | 1 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 4, "PrescriptionRecord": 11, "LabReport": 1}`
- ChunkMerger：`{"found": true, "merged": 16, "sources": 8, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 4, "Extractor:Medication": 1, "Extractor:Prescription": 11, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1}, "filtered_noise": 5}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-05 04:49:56,107 INFO     29 [ChunkMerger] Merged 16 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 4, 'Extractor:Medication': 1, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-05 04:43:29,345 INFO     29 handle_task begin for task {"id": "333155a8908811f1a3da71efcdd7cc1f", "doc_id": "32f80906908811f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412392, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905007404, "task_type": "dataflow", "root_trace_id": "8cc21299ba8c4c4f9376bb5b55f5585f", "root_traceparent": "00-8cc21299ba8c4c4f9376bb5b55f5585f-3809269866d439b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-05 04:43:29,540 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-05 04:43:29,582 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-05 04:43:29,594 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-05 04:43:29,595 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-05 04:43:29,618 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-05 04:43:29,618 INFO     29 ============================================================
2026-08-05 04:43:29,618 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-05 04:43:29,618 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-05 04:43:29,618 INFO     29 ============================================================
2026-08-05 04:43:29,618 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-05 04:43:29,618 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-05 04:43:29,633 INFO     29 No torch found.
2026-08-05 04:43:30,565 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:43:30.560+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 10, "failed": 0, "current": {"333155a8908811f1a3da71efcdd7cc1f": {"id": "333155a8908811f1a3da71efcdd7cc1f", "doc_id": "32f80906908811f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412392, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905007404, "task_type": "dataflow", "root_trace_id": "8cc21299ba8c4c4f9376bb5b55f5585f", "root_traceparent": "00-8cc21299ba8c4c4f9376bb5b55f5585f-3809269866d439b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:43:31,413 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=17
2026-08-05 04:43:31,888 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2726825, prompt_len=644
2026-08-05 04:43:33,555 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-10-21"}
```
2026-08-05 04:43:33,556 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2025-10-21
2026-08-05 04:43:33,571 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2726825, prompt_len=401
2026-08-05 04:43:36,068 INFO     29 [qwen-vl-parser] text API response (len=467):
["门(急)诊病历信息", "就诊卡", "流水", "病历编号:", "姓", "别:男", "年", "龄:64岁", "就诊科室:内科门诊(荔湾)", "医", "诊时间:2025-10-21 16:24:23", "主", "诉:取药", "现病史:", "既往史:", "过敏史:", "个人史:", "体格检查:", "专科情况:", "辅助检查:", "治疗项目:", "门诊诊断:", "支气管哮喘", "单病种:", "发病时间:", "处置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。", "1孟鲁司特钠片(省采)◆", "1瓶10.0mg,口服,每晚1次", "30天", "2倍氯米松福莫特罗吸入气雾剂◆①", "1瓶2.0揿,吸入用药,一天2次", "30天", "备注:建议在住地附近社区医疗机构随诊。", "病情评估:", "病情分级:", "是否抢救病例:否", "是否抢救成功:", "是否为绿色通道患者:否", "病人去向:", "病人来源:自行来院", "是否曾就诊于其他医疗机构:"]
2026-08-05 04:43:36,068 INFO     29 [qwen-vl-parser] page=1 text: 41 lines (bbox 0-40)
2026-08-05 04:43:36,069 INFO     29 [qwen-vl-parser] page=1 text: 41 sections
2026-08-05 04:43:36,299 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1384260, prompt_len=644
2026-08-05 04:43:37,648 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:43:37,648 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-05 04:43:37,660 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1384260, prompt_len=401
2026-08-05 04:43:39,489 INFO     29 [qwen-vl-parser] text API response (len=314):
["门(急)诊病历信息", "就诊卡号:", "流水号:", "病历编号:", "性别:男", "年", "龄:65岁", "就诊科室:内科门诊(荔湾)", "医生:", "就诊时间:2025-11-19 11:33:52", "主诉:取药", "现病史:", "既往史:", "过敏史:", "个人史:", "体格检查:", "专科情况:", "辅助检查:", "治疗项目:", "门诊诊断:", "1、支气管哮喘", "处置:", "1孟鲁司特钠片(省采)◆", "1瓶10.0mg,口服,每晚1次", "30天", "2倍氯米松福莫特罗吸入气雾剂◆①", "1瓶2.0揿,吸入用药,一天2次", "30天", "备注:"]
2026-08-05 04:43:39,490 INFO     29 [qwen-vl-parser] page=2 text: 29 lines (bbox 41-69)
2026-08-05 04:43:39,490 INFO     29 [qwen-vl-parser] page=2 text: 29 sections
2026-08-05 04:43:39,808 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2469560, prompt_len=644
2026-08-05 04:43:41,183 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:43:41,184 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-05 04:43:41,203 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2469560, prompt_len=401
2026-08-05 04:43:50,471 INFO     29 [qwen-vl-parser] text API response (len=1087):
["门(急)诊病历信息", "就诊卡号", "流水", "姓名", "性别:男", "年", "龄:65岁", "就诊科室:内科门诊(荔湾)", "病历编号:", "就诊时间:2025-12-12 09:26:46", "主诉:BAIYUN V8", "现病史:自上次访视至今,询问及查询HIS系统受试者无新增AE、SAE、哮喘急性发作,有新增合并用药。发生过2次医疗相关事件,就诊于荔湾区逢源街道社区中心1次,就诊于专科门诊1次。期间未收到ePRO触发的哮喘警报邮件。", "完成下流操作:", "1、静坐10分钟后,测量坐位生命体征,血压:120/76mmHg,脉搏频率:59次/分(NCS),呼吸:20次/分,体温:36.5℃;", "2、9:20体格检查:神志清,体置合作,自主体位,一般外表无异常,皮肤、粘膜无异常,唇甲无发绀,眼睛、耳、鼻、咽喉无异常,口咽部粘膜无异常,颈软,气管居中,甲状腺未及肿大,全身浅表淋巴结未及肿大,颈静脉无怒张,胸廓无畸形,双肺呼吸运动对称,双肺触觉语颤正常,双肺叩诊清音,双肺呼吸音清,未闻及啰音。心前区无隆起,心尖搏动无弥散,心界不大,心率:59次/分,律齐,各瓣膜听诊区未闻及病理性杂音。腹平软,全腹无压痛、反跳痛。肝、脾肋下未及,肝肾区无叩击痛,肠鸣音存,4次/分,脊柱、四肢无畸形,生理征存,未引出病理征,其他系统未见明显异常。", "3、查看受试者电子日志,受试者漏填2025年10月26日(早间日志)、8月23日、9月10日、9月19日、9月24日、10月5日、10月25日、11月3日、12月2日(晚间日志)。", "4、填写AQLQ+12和ACQ-5问卷,ACQ-5评分:1.0分。", "5、休息至少10分钟后,行12导联ECG检查。", "6、10:42采集中心实验室样本(血常规、血生化)并送往中心实验室。", "7、回收试验药物BDA MDI&AS MDI 3盒(137968-KF未开封、102035-IM未用74喷,实际已用:24喷,发药当天预喷4喷,2025.8.18-2025.9.10期间因超过7天未使用试验药物预喷1次共2喷,2025.9.10-11.19期间每七天清洗装置后预喷10次共20喷,总计预喷26喷;199863-TA未用106喷,实际已用:8喷,2025.11.20当天预喷4喷,2025.11.20-2025.12.12期间每七天清洗装置后预喷3次共6喷,总计预喷10喷)ePro记录使用总共32喷,与实际使用情况一致。", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 04:43:50,473 INFO     29 [qwen-vl-parser] page=3 text: 22 lines (bbox 70-91)
2026-08-05 04:43:50,473 INFO     29 [qwen-vl-parser] page=3 text: 22 sections
2026-08-05 04:43:50,833 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1994294, prompt_len=644
2026-08-05 04:43:52,267 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:43:52,267 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-05 04:43:52,281 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1994294, prompt_len=401
2026-08-05 04:43:57,125 INFO     29 [qwen-vl-parser] text API response (len=834):
["门诊病历", "25/10/21 16时 门诊病历", "25/11/19 11时 门诊病历（GCP专用）", "25/12/12 09时 门诊病历（GCP专用）", "1、颈痛综合征:开始时间:2025年1月8日,持续中,中度,非SAE,与试验药物无关,对试验", "药物采取措施:剂量无需改变,未因该AE退出研究,采取理疗。", "2、功能性消化不良:开始时间:2025年5月20日,持续中,中度,非SAE,与试验药物无", "关,对试验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:药物治疗。", "病因:无诱因,症状:下腹痛,进食后明显,休息后可缓解。", "3、慢性胃炎:开始时间:2025年3月2日,持续中,中度,非SAE,与试验药物无关,对试", "验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:暂无治疗措施。", "跟踪合并用药", "1、糠酸莫米松鼻喷雾剂 2024.7.19-2025.9.26 每日每早一粒 喷鼻 必要时 治疗过敏", "性鼻炎。", "2、盐酸二甲双胍片 2024.10.10-2025.9.14 0.5 TID 治疗2型糖尿病。", "3、达格列净片 2025.9.15至今 10mg qd 治疗2型糖尿病。", "补充合并用药:1、硫酸特布他林雾化吸入用溶液 2025.6.17-2025.6.19 5mg 吸", "入 qd 治疗急性支气管炎。", "预约下次安全性电话随访时间。", "既往史:", "过敏史:", "个人史:", "体格检查:", "专科情况:", "辅助检查:", "治疗项目:", "门诊诊断:", "1、支气管哮喘", "处置:", "心电图(心电图室做)", "伯氟米松福莫特罗吸入气雾剂① 1瓶2.0瓶,吸入用药,一天2次 30天", "孟鲁司特钠片(省采)① 6盒10.0mg,口服,每日1次(口服) 30天", "备注:", "医生:", ""]
2026-08-05 04:43:57,126 INFO     29 [qwen-vl-parser] page=4 text: 34 lines (bbox 92-125)
2026-08-05 04:43:57,126 INFO     29 [qwen-vl-parser] page=4 text: 34 sections
2026-08-05 04:43:57,475 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2243639, prompt_len=644
2026-08-05 04:43:58,808 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:43:58,809 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-05 04:43:58,818 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2243639, prompt_len=401
2026-08-05 04:44:01,285 INFO     29 [qwen-vl-parser] text API response (len=434):
["门(急)诊处方", "就诊时间:2025-09-15", "就诊科室:内科门诊", "主诊医", "姓名", "性别:男", "年龄:64岁", "卡号:4", "患者", "医疗证号:", "处方号", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "孟鲁司特钠片◆", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天", "倍氯米松福莫特罗吸入气雾剂◆", "6ug/揿*120揿", "221.61", "221.61", "Sig", "2揿/次,吸入,bid*30天", "医师", "医生编号:1326", "配剂人:", "核对人:", "合计:", "收费员:", "打印时间:2025-12-19", "为了您的用药安全,药物处方当天有效 第1页共1页"]
2026-08-05 04:44:01,285 INFO     29 [qwen-vl-parser] page=5 text: 43 lines (bbox 126-168)
2026-08-05 04:44:01,285 INFO     29 [qwen-vl-parser] page=5 text: 43 sections
2026-08-05 04:44:01,439 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1137495, prompt_len=644
2026-08-05 04:44:02,714 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:44:02,715 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-05 04:44:02,726 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1137495, prompt_len=401
2026-08-05 04:44:03,336 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:44:03.334+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 10, "failed": 0, "current": {"333155a8908811f1a3da71efcdd7cc1f": {"id": "333155a8908811f1a3da71efcdd7cc1f", "doc_id": "32f80906908811f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412392, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905007404, "task_type": "dataflow", "root_trace_id": "8cc21299ba8c4c4f9376bb5b55f5585f", "root_traceparent": "00-8cc21299ba8c4c4f9376bb5b55f5585f-3809269866d439b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:44:04,615 INFO     29 [qwen-vl-parser] text API response (len=341):
["门(急)诊处方", "就诊时间:2025-08-18", "就诊科室:内科门诊", "主诊", "姓名:", "性别:男", "年龄:64岁", "卡号", "患者类型:GCP支付", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "孟鲁司特钠片◆", "10mg*30/瓶", "28片", "1.05", "29.43", "Sig", "10mg/次,口服,qn*28天", "倍氯米松福莫特罗吸入气雾剂", "6ug/揿*120揿", "221.61", "221.61", "Sig", "2揿/次,吸入,bid*30天"]
2026-08-05 04:44:04,616 INFO     29 [qwen-vl-parser] page=6 text: 35 lines (bbox 169-203)
2026-08-05 04:44:04,616 INFO     29 [qwen-vl-parser] page=6 text: 35 sections
2026-08-05 04:44:04,766 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1097037, prompt_len=644
2026-08-05 04:44:06,225 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:44:06,226 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-05 04:44:06,236 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1097037, prompt_len=401
2026-08-05 04:44:08,149 INFO     29 [qwen-vl-parser] text API response (len=337):
["门(急)诊处方", "就诊时间:2025-05-30", "就诊科室:内科门诊", "主", "姓名", "性别:男", "年龄:64岁", "卡", "患者类型:GCP支付", "医疗证号:", "处", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "孟鲁司特钠片◆", "10mg*5/盒", "90片", "2.56", "230.58", "Sig", "10mg/次,口服,qn*90天", "倍氯米松福莫特罗吸入气雾剂0◆@/6ug/揿*120瓶", "221.61", "664.83", "Sig", "2揿/次,吸入,bid*90天"]
2026-08-05 04:44:08,150 INFO     29 [qwen-vl-parser] page=7 text: 34 lines (bbox 204-237)
2026-08-05 04:44:08,150 INFO     29 [qwen-vl-parser] page=7 text: 34 sections
2026-08-05 04:44:08,330 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1235285, prompt_len=644
2026-08-05 04:44:09,740 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:44:09,740 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-05 04:44:09,755 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1235285, prompt_len=401
2026-08-05 04:44:11,713 INFO     29 [qwen-vl-parser] text API response (len=341):
["门(急)诊处方", "就诊时间:2025-03-05", "就诊科室:内科门诊", "主诊医", "姓名", "性别:男", "年龄:64岁", "卡号:", "患者类型:GCP支付", "医疗证号:", "处方号:", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂*0ug/6ug/瓶*120瓶", "221.61 443.22", "Sig", "2揿/次,吸入,bid*60天", "孟鲁司特钠片", "10mg*30/瓶", "60片", "1.05", "63.06", "Sig", "10mg/次,口服,qn*60天"]
2026-08-05 04:44:11,714 INFO     29 [qwen-vl-parser] page=8 text: 33 lines (bbox 238-270)
2026-08-05 04:44:11,714 INFO     29 [qwen-vl-parser] page=8 text: 33 sections
2026-08-05 04:44:11,884 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1061616, prompt_len=644
2026-08-05 04:44:13,188 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:44:13,189 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-05 04:44:13,197 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1061616, prompt_len=401
2026-08-05 04:44:15,252 INFO     29 [qwen-vl-parser] text API response (len=366):
["门(急)诊处方", "就诊时间:2025-03-05", "就诊科室:内科门诊", "主诊", "姓名", "性别:男", "年龄:64岁", "卡号", "患者类型:GCP支付", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿", "221.61 221.61", "Sig", "2揿/次,吸入,bid*30天", "孟鲁司特钠片", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 04:44:15,252 INFO     29 [qwen-vl-parser] page=9 text: 35 lines (bbox 271-305)
2026-08-05 04:44:15,252 INFO     29 [qwen-vl-parser] page=9 text: 35 sections
2026-08-05 04:44:15,451 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1455567, prompt_len=644
2026-08-05 04:44:16,822 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:44:16,823 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=None
2026-08-05 04:44:16,839 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1455567, prompt_len=401
2026-08-05 04:44:21,681 INFO     29 [qwen-vl-parser] text API response (len=370):
["门(急)诊处方", "就诊时间:2025-02-08", "就诊科室:内科门诊", "主诊", "姓名:", "性别:男", "年龄:64岁", "卡号:", "患者类型:001 支付", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120瓶", "221.61 221.61", "Sig", "2揿/次,吸入,bid*30天", "孟鲁司特钠片◆", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 04:44:21,682 INFO     29 [qwen-vl-parser] page=10 text: 35 lines (bbox 306-340)
2026-08-05 04:44:21,682 INFO     29 [qwen-vl-parser] page=10 text: 35 sections
2026-08-05 04:44:21,860 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1263830, prompt_len=644
2026-08-05 04:44:23,272 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:44:23,273 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=None
2026-08-05 04:44:23,309 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1263830, prompt_len=401
2026-08-05 04:44:25,310 INFO     29 [qwen-vl-parser] text API response (len=328):
["门(急)诊处方", "就诊时间:2025-01-10", "就诊科室:内科门诊", "主诊", "性别:男", "年龄:64岁", "卡号", "患者类型:G", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿", "221.61 221.61", "Sig", "2揿/次,吸入,bid*30天", "孟鲁司特钠片", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天"]
2026-08-05 04:44:25,310 INFO     29 [qwen-vl-parser] page=11 text: 32 lines (bbox 341-372)
2026-08-05 04:44:25,310 INFO     29 [qwen-vl-parser] page=11 text: 32 sections
2026-08-05 04:44:25,462 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1073703, prompt_len=644
2026-08-05 04:44:26,878 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:44:26,878 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=None
2026-08-05 04:44:26,884 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1073703, prompt_len=401
2026-08-05 04:44:28,989 INFO     29 [qwen-vl-parser] text API response (len=368):
["门(急)诊处方", "就诊时间:2024-12-11", "就诊科室:内科门诊", "主诊", "姓名:", "性别:男", "年龄:64岁", "卡号", "患者类型:GCP支付", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂100ug/6ug/瓶*120瓶", "221.61 221.61", "Sig", "2揿/次,吸入,bid*30天", "孟鲁司特钠片◆", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 04:44:28,990 INFO     29 [qwen-vl-parser] page=12 text: 35 lines (bbox 373-407)
2026-08-05 04:44:28,990 INFO     29 [qwen-vl-parser] page=12 text: 35 sections
2026-08-05 04:44:29,143 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1135113, prompt_len=644
2026-08-05 04:44:30,600 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-11-18"}
```
2026-08-05 04:44:30,601 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=2024-11-18
2026-08-05 04:44:30,613 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1135113, prompt_len=401
2026-08-05 04:44:32,699 INFO     29 [qwen-vl-parser] text API response (len=371):
["门(急)诊处方", "就诊时间:2024-11-18", "就诊科室:内科门诊", "主诊", "姓名", "性别:男", "年龄:63岁", "卡号:", "患者类型:GLP支付", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘,非危重", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿", "221.61 221.61", "Sig", "2揿/次,吸入,bid*30天", "孟鲁司特钠片", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 04:44:32,700 INFO     29 [qwen-vl-parser] page=13 text: 35 lines (bbox 408-442)
2026-08-05 04:44:32,700 INFO     29 [qwen-vl-parser] page=13 text: 35 sections
2026-08-05 04:44:32,833 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1009899, prompt_len=644
2026-08-05 04:44:34,209 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-05 04:44:34,210 INFO     29 [qwen-vl-parser] page=14 classify=table report_date=None
2026-08-05 04:44:34,218 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1009899, prompt_len=756
2026-08-05 04:44:36,066 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:44:36.065+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 10, "failed": 0, "current": {"333155a8908811f1a3da71efcdd7cc1f": {"id": "333155a8908811f1a3da71efcdd7cc1f", "doc_id": "32f80906908811f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412392, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905007404, "task_type": "dataflow", "root_trace_id": "8cc21299ba8c4c4f9376bb5b55f5585f", "root_traceparent": "00-8cc21299ba8c4c4f9376bb5b55f5585f-3809269866d439b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:44:42,731 INFO     29 [qwen-vl-parser] table API response (len=1806):
\begin{tabular}{llllllll}
\hline
序号 & 项目代码 & 结果 & 提示 & 单位 & 参考范围 & 试验方法 \\
\hline
1 & 白细胞(WBC) & 9.17 & & 10^9/L & 3.5 -- 9.5 & \\
2 & 中性粒细胞总数(NEU) & 5.71 & & 10^9/L & 1.8 -- 6.3 & \\
3 & 中性粒细胞百分数(NEUN) & 62.30 & & \% & 40 -- 75 & \\
4 & 淋巴细胞总数(LY) & 2.62 & & 10^9/L & 1.1 -- 3.2 & \\
5 & 淋巴细胞百分数(LYN) & 28.60 & & \% & 20 -- 50 & \\
6 & 单核细胞总数(MONO) & 0.47 & & 10^9/L & 0.1 -- 0.6 & \\
7 & 单核细胞百分数(MON0) & 5.10 & & \% & 3 -- 10 & \\
8 & 嗜酸性粒细胞总数(EOS) & 0.34 & & 10^9/L & 0.02 -- 0.52 & \\
9 & 嗜酸性粒细胞百分数(EOS%) & 3.70 & & \% & 0.4 -- 8 & \\
10 & 嗜碱性粒细胞总数(BAS0) & 0.03 & & 10^9/L & 0 -- 0.06 & \\
11 & 嗜碱性粒细胞百分比(BAS0%) & 0.30 & & \% & 0 -- 1 & \\
12 & 红细胞(RBC) & 4.91 & 【广州】 & 10^12/L & 4.3 -- 5.8 & \\
13 & 血红蛋白(HGB) & 158 & 【广州】 & g/L & 130 -- 175 & \\
14 & 红细胞压积(HCT) & 47.10 & 【广州】 & \% & 40 -- 50 & \\
15 & 红细胞平均容积(MCV) & 96.90 & 【广州】 & fl & 82 -- 100 & \\
16 & 红细胞平均血红蛋白(MCH) & 32.20 & 【广州】 & pg & 27 -- 34 & \\
17 & 红细胞平均血红蛋白浓度(MCHC) & 335.00 & 【广州】 & g/L & 316 -- 354 & \\
18 & 红细胞分布宽度(RDW) & 12.40 & & \% & 11.6 -- 14.8 & \\
19 & 红细胞分布宽度-SD(RDW-SD) & 44.10 & & fl & 37.1 -- 49.2 & \\
20 & 血小板(Plt) & 197 & 【广州】 & 10^9/L & 125 -- 350 & \\
21 & 平均血小板容积(MPV) & 10.70 & & fl & 6 -- 12 & \\
22 & 平均血小板比容(Pct) & 0.21 & & \% & 0.10 -- 0.29 & \\
23 & 血小板分布宽度(PDW) & 13.00 & & 10(GSP) & 15.3 -- 20.5 & \\
24 & 大血小板(P-LCR) & 30.90 & & \% & & \\
25 & 网织红细胞绝对值(RETR) & 90.5 & & 10^9/L & 46.4 -- 121.2 & \\
26 & 网织红细胞百分数(RETR) & 1.64 & & \% & & \\
27 & 低荧光强度网织红细胞比率(LFF) & 83.8 & $\downarrow$ & \% & 89.9 -- 98.4 & \\
28 & 中荧光强度网织红细胞比率(MFF) & 13.3 & $\uparrow$ & \% & 1.6 -- 9.5 & \\
29 & 高荧光强度网织红细胞比率(HFF) & 2.9 & $\uparrow$ & \% & 0 -- 1.7 & \\
30 & 未成熟网织红细胞比率(IRF) & 16.2 & $\uparrow$ & \% & 1.6 -- 10.5 & \\
31 & 有核红细胞计数(NRBCW) & 0 & & 10^9/L & & \\
32 & 有核红细胞百分比(NRBC%) & 0 & & \% & & \\
\hline
\end{tabular}
2026-08-05 04:44:42,732 INFO     29 [qwen-vl-parser] page=14 table: 38 LaTeX lines (bbox 443-480)
2026-08-05 04:44:42,732 INFO     29 [qwen-vl-parser] page=14 table: 38 sections
2026-08-05 04:44:42,850 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=716459, prompt_len=644
2026-08-05 04:44:44,178 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:44:44,179 INFO     29 [qwen-vl-parser] page=15 classify=text report_date=None
2026-08-05 04:44:44,185 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=716459, prompt_len=401
2026-08-05 04:44:46,364 INFO     29 [qwen-vl-parser] text API response (len=364):
["处方笺", "普通", "诊疗", "患者姓", "男", "年龄：65岁", "费别：", "科室：", "2026-01-06 11:28:26", "处方号", "地址：", "联系电", "身份号", "诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎", "R", "P:", "倍氯米松福莫特罗吸入气雾剂◆① 100ug/6ug/揿*120", "1瓶", "剂量：每次2揿 ( 1/60 瓶 )", "用法：吸入用药", "bid 01-06", "孟鲁司特钠片(省采)◆", "10mg*5/盒", "30片", "剂量：每次10mg (1 片 )", "用法：口服", "qd 01-06", "处方金额：298.47元", "取药药房：门诊西药房（荔湾）", ""]
2026-08-05 04:44:46,365 INFO     29 [qwen-vl-parser] page=15 text: 29 lines (bbox 481-509)
2026-08-05 04:44:46,365 INFO     29 [qwen-vl-parser] page=15 text: 29 sections
2026-08-05 04:44:46,529 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1049439, prompt_len=644
2026-08-05 04:44:47,864 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:44:47,864 INFO     29 [qwen-vl-parser] page=16 classify=text report_date=None
2026-08-05 04:44:47,878 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1049439, prompt_len=401
2026-08-05 04:44:50,447 INFO     29 [qwen-vl-parser] text API response (len=431):
["处方笺", "普通", "诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎", "患者", "年龄：65岁", "费别", "科室", "6-01-06 11:31:02", "处方", "地址", "联系", "身份", "Rp:", "左氧氟沙星片(省采)●⑥", "0.5g*28片/盒", "3片", "剂量：每次0.5g", "(1 片)", "用法：口服", "qd", "01-06", "醋酸泼尼松片●②⑥", "5mg*100/瓶", "6片", "剂量：每次10mg", "(2 片)", "用法：口服", "qm", "01-06", "盐酸氨溴索分散片(省采)●⑥", "30mg*50/盒", "15片", "剂量：每次30mg", "(1 片)", "用法：餐后口服", "tid", "01-06", "处方金额：3.47元", "取药药房：门诊西药房（荔湾）", "医师手签：", ""]
2026-08-05 04:44:50,447 INFO     29 [qwen-vl-parser] page=16 text: 40 lines (bbox 510-549)
2026-08-05 04:44:50,447 INFO     29 [qwen-vl-parser] page=16 text: 40 sections
2026-08-05 04:44:50,813 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2373698, prompt_len=644
2026-08-05 04:44:55,204 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-02-04"
}
```
2026-08-05 04:44:55,205 INFO     29 [qwen-vl-parser] page=17 classify=text report_date=2026-02-04
2026-08-05 04:44:55,218 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2373698, prompt_len=401
2026-08-05 04:45:00,757 INFO     29 [qwen-vl-parser] text API response (len=942):
["病历编号：", "姓名：", "性别：男", "年龄：65岁", "就诊科室：内科门诊（基础）", "医生：", "就诊时间：2026-02-04 11:23:30", "主诉：支气管哮喘治疗后复诊", "现病史：2022年3月前开始出现咳嗽、咳痰，粘白，量少，能咯出，咳嗽呈阵发性，偶则激性，伴轻度咽痒，无气促，夜间有喘息、胸闷，伴鼻塞、流涕、喉咙，无咽痛，", "无反酸、嗳气、腹胀，无上腹部隐痛不适感，无伴发热、畏寒，曾自服肺力咳症状未见缓解，现病情好转、稳定，本次门诊距上次门诊间隔时间7天；过去4周，症状控制情况：控制良好，吸入药物使用情况：遵医嘱使用；，吸入装置使用情况：有，正确；急性发作情况：", "两次就诊期间急性发作：发作次数：0次，长期规律使用倍氯米松福莫特罗吸入气雾剂治疗。", "既往史：鼻炎病史，有糖尿病史", "过敏史：未发现", "个人史：否认遗传病史，吸烟30年，6支/日，已戒烟8年，饮酒6年，1两/日。", "体格检查：神志清，口腔无溃疡、粘膜白斑，肺部听诊，鼻塞，通气，气管居中，双肺呼吸音稍减弱，未闻及明显干湿性罗音。", "专科情况：", "辅助检查：血常规：Q-CRP：0.54mg/l 白细胞：5.5*109/L 中性粒细胞：", "5.17*109/L 60.5% 淋巴细胞：2.23*109/L 26.2% 单个核细胞：", "0.46*109/L 5.4% 嗜酸性粒细胞：0.6*109/L 7.1% 呼出气一氧化", "氮：FeNO50：130ppb FnNO10：161ppb 肺功能：轻度阻塞性通气功能障碍，支气管激发", "试验阳性（PD20=0.312mg AHI：轻度），胸片：心、肺、膈未见异常", "治疗项目：", "门诊诊断：", "1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、2型糖尿病", "单 种：", "发病时间：", "处 置：请仔细阅读药品说明书等文书资料，遵嘱治疗，不适随诊。", "倍氯米松福莫特罗吸入气雾剂◆① 1瓶2.0瓶，吸入用药，一天2次 30天", "孟鲁司特钠片（省采）◆ 6盒10.0mg，口服，每日1次（口服） 30天", "备 注：建议在停药附近社区医疗机构随访。"]
2026-08-05 04:45:00,758 INFO     29 [qwen-vl-parser] page=17 text: 30 lines (bbox 550-579)
2026-08-05 04:45:00,758 INFO     29 [qwen-vl-parser] page=17 text: 30 sections
2026-08-05 04:45:00,758 INFO     29 [qwen-vl-parser] parse_pdf done: 580 sections from 17 pages.
2026-08-05 04:45:00,769 INFO     29 Close text detector.
2026-08-05 04:45:01,108 INFO     29 Close text recognizer.
2026-08-05 04:45:01,431 INFO     29 Close recognizer.
2026-08-05 04:45:01,768 INFO     29 Close recognizer.
2026-08-05 04:45:02,129 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-05 04:45:02,129 INFO     29 [Trace] task=333155a8 | doc=HXJ 哮喘 广三.pdf | Parser:MedLink | outputs={"html": "", "json": "580 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "json"}
2026-08-05 04:45:02,129 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-05 04:45:02,144 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 04:45:02,144 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。只有主诉，病史的也属于OutpatientRecord（门诊病历）\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 门(急)诊病历信息\n[BBOX-1] 就诊卡\n[BBOX-2] 流水\n[BBOX-3] 病历编号:\n[BBOX-4] 姓\n[BBOX-5] 别:男\n[BBOX-6] 年\n[BBOX-7] 龄:64岁\n[BBOX-8] 就诊科室:内科门诊(荔湾)\n[BBOX-9] 医\n[BBOX-10] 诊时间:2025-10-21 16:24:23\n[BBOX-11] 主\n[BBOX-12] 诉:取药\n[BBOX-13] 现病史:\n[BBOX-14] 既往史:\n[BBOX-15] 过敏史:\n[BBOX-16] 个人史:\n[BBOX-17] 体格检查:\n[BBOX-18] 专科情况:\n[BBOX-19] 辅助检查:\n[BBOX-20] 治疗项目:\n[BBOX-21] 门诊诊断:\n[BBOX-22] 支气管哮喘\n[BBOX-23] 单病种:\n[BBOX-24] 发病时间:\n[BBOX-25] 处置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。\n[BBOX-26] 1孟鲁司特钠片(省采)◆\n[BBOX-27] 1瓶10.0mg,口服,每晚1次\n[BBOX-28] 30天\n[BBOX-29] 2倍氯米松福莫特罗吸入气雾剂◆①\n[BBOX-30] 1瓶2.0揿,吸入用药,一天2次\n[BBOX-31] 30天\n[BBOX-32] 备注:建议在住地附近社区医疗机构随诊。\n[BBOX-33] 病情评估:\n[BBOX-34] 病情分级:\n[BBOX-35] 是否抢救病例:否\n[BBOX-36] 是否抢救成功:\n[BBOX-37] 是否为绿色通道患者:否\n[BBOX-38] 病人去向:\n[BBOX-39] 病人来源:自行来院\n[BBOX-40] 是否曾就诊于其他医疗机构:\n[BBOX-41] 门(急)诊病历信息\n[BBOX-42] 就诊卡号:\n[BBOX-43] 流水号:\n[BBOX-44] 病历编号:\n[BBOX-45] 性别:男\n[BBOX-46] 年\n[BBOX-47] 龄:65岁\n[BBOX-48] 就诊科室:内科门诊(荔湾)\n[BBOX-49] 医生:\n[BBOX-50] 就诊时间:2025-11-19 11:33:52\n[BBOX-51] 主诉:取药\n[BBOX-52] 现病史:\n[BBOX-53] 既往史:\n[BBOX-54] 过敏史:\n[BBOX-55] 个人史:\n[BBOX-56] 体格检查:\n[BBOX-57] 专科情况:\n[BBOX-58] 辅助检查:\n[BBOX-59] 治疗项目:\n[BBOX-60] 门诊诊断:\n[BBOX-61] 1、支气管哮喘\n[BBOX-62] 处置:\n[BBOX-63] 1孟鲁司特钠片(省采)◆\n[BBOX-64] 1瓶10.0mg,口服,每晚1次\n[BBOX-65] 30天\n[BBOX-66] 2倍氯米松福莫特罗吸入气雾剂◆①\n[BBOX-67] 1瓶2.0揿,吸入用药,一天2次\n[BBOX-68] 30天\n[BBOX-69] 备注:\n[BBOX-70] 门(急)诊病历信息\n[BBOX-71] 就诊卡号\n[BBOX-72] 流水\n[BBOX-73] 姓名\n[BBOX-74] 性别:男\n[BBOX-75] 年\n[BBOX-76] 龄:65岁\n[BBOX-77] 就诊科室:内科门诊(荔湾)\n[BBOX-78] 病历编号:\n[BBOX-79] 就诊时间:2025-12-12 09:26:46\n[BBOX-80] 主诉:BAIYUN V8\n[BBOX-81] 现病史:自上次访视至今,询问及查询HIS系统受试者无新增AE、SAE、哮喘急性发作,有新增合并用药。发生过2次医疗相关事件,就诊于荔湾区逢源街道社区中心1次,就诊于专科门诊1次。期间未收到ePRO触发的哮喘警报邮件。\n[BBOX-82] 完成下流操作:\n[BBOX-83] 1、静坐10分钟后,测量坐位生命体征,血压:120/76mmHg,脉搏频率:59次/分(NCS),呼吸:20次/分,体温:36.5℃;\n[BBOX-84] 2、9:20体格检查:神志清,体置合作,自主体位,一般外表无异常,皮肤、粘膜无异常,唇甲无发绀,眼睛、耳、鼻、咽喉无异常,口咽部粘膜无异常,颈软,气管居中,甲状腺未及肿大,全身浅表淋巴结未及肿大,颈静脉无怒张,胸廓无畸形,双肺呼吸运动对称,双肺触觉语颤正常,双肺叩诊清音,双肺呼吸音清,未闻及啰音。心前区无隆起,心尖搏动无弥散,心界不大,心率:59次/分,律齐,各瓣膜听诊区未闻及病理性杂音。腹平软,全腹无压痛、反跳痛。肝、脾肋下未及,肝肾区无叩击痛,肠鸣音存,4次/分,脊柱、四肢无畸形,生理征存,未引出病理征,其他系统未见明显异常。\n[BBOX-85] 3、查看受试者电子日志,受试者漏填2025年10月26日(早间日志)、8月23日、9月10日、9月19日、9月24日、10月5日、10月25日、11月3日、12月2日(晚间日志)。\n[BBOX-86] 4、填写AQLQ+12和ACQ-5问卷,ACQ-5评分:1.0分。\n[BBOX-87] 5、休息至少10分钟后,行12导联ECG检查。\n[BBOX-88] 6、10:42采集中心实验室样本(血常规、血生化)并送往中心实验室。\n[BBOX-89] 7、回收试验药物BDA MDI&AS MDI 3盒(137968-KF未开封、102035-IM未用74喷,实际已用:24喷,发药当天预喷4喷,2025.8.18-2025.9.10期间因超过7天未使用试验药物预喷1次共2喷,2025.9.10-11.19期间每七天清洗装置后预喷10次共20喷,总计预喷26喷;199863-TA未用106喷,实际已用:8喷,2025.11.20当天预喷4喷,2025.11.20-2025.12.12期间每七天清洗装置后预喷3次共6喷,总计预喷10喷)ePro记录使用总共32喷,与实际使用情况一致。\n[BBOX-90] CS 扫描全能王\n[BBOX-91] 3亿人都在用的扫描App\n[BBOX-92] 门诊病历\n[BBOX-93] 25/10/21 16时 门诊病历\n[BBOX-94] 25/11/19 11时 门诊病历（GCP专用）\n[BBOX-95] 25/12/12 09时 门诊病历（GCP专用）\n[BBOX-96] 1、颈痛综合征:开始时间:2025年1月8日,持续中,中度,非SAE,与试验药物无关,对试验\n[BBOX-97] 药物采取措施:剂量无需改变,未因该AE退出研究,采取理疗。\n[BBOX-98] 2、功能性消化不良:开始时间:2025年5月20日,持续中,中度,非SAE,与试验药物无\n[BBOX-99] 关,对试验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:药物治疗。\n[BBOX-100] 病因:无诱因,症状:下腹痛,进食后明显,休息后可缓解。\n[BBOX-101] 3、慢性胃炎:开始时间:2025年3月2日,持续中,中度,非SAE,与试验药物无关,对试\n[BBOX-102] 验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:暂无治疗措施。\n[BBOX-103] 跟踪合并用药\n[BBOX-104] 1、糠酸莫米松鼻喷雾剂 2024.7.19-2025.9.26 每日每早一粒 喷鼻 必要时 治疗过敏\n[BBOX-105] 性鼻炎。\n[BBOX-106] 2、盐酸二甲双胍片 2024.10.10-2025.9.14 0.5 TID 治疗2型糖尿病。\n[BBOX-107] 3、达格列净片 2025.9.15至今 10mg qd 治疗2型糖尿病。\n[BBOX-108] 补充合并用药:1、硫酸特布他林雾化吸入用溶液 2025.6.17-2025.6.19 5mg 吸\n[BBOX-109] 入 qd 治疗急性支气管炎。\n[BBOX-110] 预约下次安全性电话随访时间。\n[BBOX-111] 既往史:\n[BBOX-112] 过敏史:\n[BBOX-113] 个人史:\n[BBOX-114] 体格检查:\n[BBOX-115] 专科情况:\n[BBOX-116] 辅助检查:\n[BBOX-117] 治疗项目:\n[BBOX-118] 门诊诊断:\n[BBOX-119] 1、支气管哮喘\n[BBOX-120] 处置:\n[BBOX-121] 心电图(心电图室做)\n[BBOX-122] 伯氟米松福莫特罗吸入气雾剂① 1瓶2.0瓶,吸入用药,一天2次 30天\n[BBOX-123] 孟鲁司特钠片(省采)① 6盒10.0mg,口服,每日1次(口服) 30天\n[BBOX-124] 备注:\n[BBOX-125] 医生:\n[BBOX-126] 门(急)诊处方\n[BBOX-127] 就诊时间:2025-09-15\n[BBOX-128] 就诊科室:内科门诊\n[BBOX-129] 主诊医\n[BBOX-130] 姓名\n[BBOX-131] 性别:男\n[BBOX-132] 年龄:64岁\n[BBOX-133] 卡号:4\n[BBOX-134] 患者\n[BBOX-135] 医疗证号:\n[BBOX-136] 处方号\n[BBOX-137] 地址:\n[BBOX-138] 身份证号:\n[BBOX-139] 诊断:支气管哮喘\n[BBOX-140] 西药处方\n[BBOX-141] 组号\n[BBOX-142] 项目名称\n[BBOX-143] 规格\n[BBOX-144] 总量\n[BBOX-145] 单价\n[BBOX-146] 金额\n[BBOX-147] R:\n[BBOX-148] 孟鲁司特钠片◆\n[BBOX-149] 10mg*30/瓶\n[BBOX-150] 30片\n[BBOX-151] 1.05\n[BBOX-152] 31.53\n[BBOX-153] Sig\n[BBOX-154] 10mg/次,口服,qn*30天\n[BBOX-155] 倍氯米松福莫特罗吸入气雾剂◆\n[BBOX-156] 6ug/揿*120揿\n[BBOX-157] 221.61\n[BBOX-158] 221.61\n[BBOX-159] Sig\n[BBOX-160] 2揿/次,吸入,bid*30天\n[BBOX-161] 医师\n[BBOX-162] 医生编号:1326\n[BBOX-163] 配剂人:\n[BBOX-164] 核对人:\n[BBOX-165] 合计:\n[BBOX-166] 收费员:\n[BBOX-167] 打印时间:2025-12-19\n[BBOX-168] 为了您的用药安全,药物处方当天有效 第1页共1页\n[BBOX-169] 门(急)诊处方\n[BBOX-170] 就诊时间:2025-08-18\n[BBOX-171] 就诊科室:内科门诊\n[BBOX-172] 主诊\n[BBOX-173] 姓名:\n[BBOX-174] 性别:男\n[BBOX-175] 年龄:64岁\n[BBOX-176] 卡号\n[BBOX-177] 患者类型:GCP支付\n[BBOX-178] 医疗证号:\n[BBOX-179] 处方\n[BBOX-180] 地址:\n[BBOX-181] 身份证号:\n[BBOX-182] 诊断:支气管哮喘\n[BBOX-183] 西药处方\n[BBOX-184] 组号\n[BBOX-185] 项目名称\n[BBOX-186] 规格\n[BBOX-187] 总量\n[BBOX-188] 单价\n[BBOX-189] 金额\n[BBOX-190] R:\n[BBOX-191] 孟鲁司特钠片◆\n[BBOX-192] 10mg*30/瓶\n[BBOX-193] 28片\n[BBOX-194] 1.05\n[BBOX-195] 29.43\n[BBOX-196] Sig\n[BBOX-197] 10mg/次,口服,qn*28天\n[BBOX-198] 倍氯米松福莫特罗吸入气雾剂\n[BBOX-199] 6ug/揿*120揿\n[BBOX-200] 221.61\n[BBOX-201] 221.61\n[BBOX-202] Sig\n[BBOX-203] 2揿/次,吸入,bid*30天\n[BBOX-204] 门(急)诊处方\n[BBOX-205] 就诊时间:2025-05-30\n[BBOX-206] 就诊科室:内科门诊\n[BBOX-207] 主\n[BBOX-208] 姓名\n[BBOX-209] 性别:男\n[BBOX-210] 年龄:64岁\n[BBOX-211] 卡\n[BBOX-212] 患者类型:GCP支付\n[BBOX-213] 医疗证号:\n[BBOX-214] 处\n[BBOX-215] 地址:\n[BBOX-216] 身份证号:\n[BBOX-217] 诊断:支气管哮喘\n[BBOX-218] 西药处方\n[BBOX-219] 组号\n[BBOX-220] 项目名称\n[BBOX-221] 规格\n[BBOX-222] 总量\n[BBOX-223] 单价\n[BBOX-224] 金额\n[BBOX-225] R:\n[BBOX-226] 孟鲁司特钠片◆\n[BBOX-227] 10mg*5/盒\n[BBOX-228] 90片\n[BBOX-229] 2.56\n[BBOX-230] 230.58\n[BBOX-231] Sig\n[BBOX-232] 10mg/次,口服,qn*90天\n[BBOX-233] 倍氯米松福莫特罗吸入气雾剂0◆@/6ug/揿*120瓶\n[BBOX-234] 221.61\n[BBOX-235] 664.83\n[BBOX-236] Sig\n[BBOX-237] 2揿/次,吸入,bid*90天\n[BBOX-238] 门(急)诊处方\n[BBOX-239] 就诊时间:2025-03-05\n[BBOX-240] 就诊科室:内科门诊\n[BBOX-241] 主诊医\n[BBOX-242] 姓名\n[BBOX-243] 性别:男\n[BBOX-244] 年龄:64岁\n[BBOX-245] 卡号:\n[BBOX-246] 患者类型:GCP支付\n[BBOX-247] 医疗证号:\n[BBOX-248] 处方号:\n[BBOX-249] 地址:\n[BBOX-250] 身份证号:\n[BBOX-251] 诊断:支气管哮喘\n[BBOX-252] 西药处方\n[BBOX-253] 组号\n[BBOX-254] 项目名称\n[BBOX-255] 规格\n[BBOX-256] 总量\n[BBOX-257] 单价\n[BBOX-258] 金额\n[BBOX-259] R:\n[BBOX-260] 倍氯米松福莫特罗吸入气雾剂*0ug/6ug/瓶*120瓶\n[BBOX-261] 221.61 443.22\n[BBOX-262] Sig\n[BBOX-263] 2揿/次,吸入,bid*60天\n[BBOX-264] 孟鲁司特钠片\n[BBOX-265] 10mg*30/瓶\n[BBOX-266] 60片\n[BBOX-267] 1.05\n[BBOX-268] 63.06\n[BBOX-269] Sig\n[BBOX-270] 10mg/次,口服,qn*60天\n[BBOX-271] 门(急)诊处方\n[BBOX-272] 就诊时间:2025-03-05\n[BBOX-273] 就诊科室:内科门诊\n[BBOX-274] 主诊\n[BBOX-275] 姓名\n[BBOX-276] 性别:男\n[BBOX-277] 年龄:64岁\n[BBOX-278] 卡号\n[BBOX-279] 患者类型:GCP支付\n[BBOX-280] 医疗证号:\n[BBOX-281] 处方\n[BBOX-282] 地址:\n[BBOX-283] 身份证号:\n[BBOX-284] 诊断:支气管哮喘\n[BBOX-285] 西药处方\n[BBOX-286] 组号\n[BBOX-287] 项目名称\n[BBOX-288] 规格\n[BBOX-289] 总量\n[BBOX-290] 单价\n[BBOX-291] 金额\n[BBOX-292] R:\n[BBOX-293] 倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿\n[BBOX-294] 221.61 221.61\n[BBOX-295] Sig\n[BBOX-296] 2揿/次,吸入,bid*30天\n[BBOX-297] 孟鲁司特钠片\n[BBOX-298] 10mg*30/瓶\n[BBOX-299] 30片\n[BBOX-300] 1.05\n[BBOX-301] 31.53\n[BBOX-302] Sig\n[BBOX-303] 10mg/次,口服,qn*30天\n[BBOX-304] CS 扫描全能王\n[BBOX-305] 3亿人都在用的扫描App\n[BBOX-306] 门(急)诊处方\n[BBOX-307] 就诊时间:2025-02-08\n[BBOX-308] 就诊科室:内科门诊\n[BBOX-309] 主诊\n[BBOX-310] 姓名:\n[BBOX-311] 性别:男\n[BBOX-312] 年龄:64岁\n[BBOX-313] 卡号:\n[BBOX-314] 患者类型:001 支付\n[BBOX-315] 医疗证号:\n[BBOX-316] 处方\n[BBOX-317] 地址:\n[BBOX-318] 身份证号:\n[BBOX-319] 诊断:支气管哮喘\n[BBOX-320] 西药处方\n[BBOX-321] 组号\n[BBOX-322] 项目名称\n[BBOX-323] 规格\n[BBOX-324] 总量\n[BBOX-325] 单价\n[BBOX-326] 金额\n[BBOX-327] R:\n[BBOX-328] 倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120瓶\n[BBOX-329] 221.61 221.61\n[BBOX-330] Sig\n[BBOX-331] 2揿/次,吸入,bid*30天\n[BBOX-332] 孟鲁司特钠片◆\n[BBOX-333] 10mg*30/瓶\n[BBOX-334] 30片\n[BBOX-335] 1.05\n[BBOX-336] 31.53\n[BBOX-337] Sig\n[BBOX-338] 10mg/次,口服,qn*30天\n[BBOX-339] CS 扫描全能王\n[BBOX-340] 3亿人都在用的扫描App\n[BBOX-341] 门(急)诊处方\n[BBOX-342] 就诊时间:2025-01-10\n[BBOX-343] 就诊科室:内科门诊\n[BBOX-344] 主诊\n[BBOX-345] 性别:男\n[BBOX-346] 年龄:64岁\n[BBOX-347] 卡号\n[BBOX-348] 患者类型:G\n[BBOX-349] 医疗证号:\n[BBOX-350] 处方\n[BBOX-351] 地址:\n[BBOX-352] 身份证号:\n[BBOX-353] 诊断:支气管哮喘\n[BBOX-354] 西药处方\n[BBOX-355] 组号\n[BBOX-356] 项目名称\n[BBOX-357] 规格\n[BBOX-358] 总量\n[BBOX-359] 单价\n[BBOX-360] 金额\n[BBOX-361] R:\n[BBOX-362] 倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿\n[BBOX-363] 221.61 221.61\n[BBOX-364] Sig\n[BBOX-365] 2揿/次,吸入,bid*30天\n[BBOX-366] 孟鲁司特钠片\n[BBOX-367] 10mg*30/瓶\n[BBOX-368] 30片\n[BBOX-369] 1.05\n[BBOX-370] 31.53\n[BBOX-371] Sig\n[BBOX-372] 10mg/次,口服,qn*30天\n[BBOX-373] 门(急)诊处方\n[BBOX-374] 就诊时间:2024-12-11\n[BBOX-375] 就诊科室:内科门诊\n[BBOX-376] 主诊\n[BBOX-377] 姓名:\n[BBOX-378] 性别:男\n[BBOX-379] 年龄:64岁\n[BBOX-380] 卡号\n[BBOX-381] 患者类型:GCP支付\n[BBOX-382] 医疗证号:\n[BBOX-383] 处方\n[BBOX-384] 地址:\n[BBOX-385] 身份证号:\n[BBOX-386] 诊断:支气管哮喘\n[BBOX-387] 西药处方\n[BBOX-388] 组号\n[BBOX-389] 项目名称\n[BBOX-390] 规格\n[BBOX-391] 总量\n[BBOX-392] 单价\n[BBOX-393] 金额\n[BBOX-394] R:\n[BBOX-395] 倍氯米松福莫特罗吸入气雾剂100ug/6ug/瓶*120瓶\n[BBOX-396] 221.61 221.61\n[BBOX-397] Sig\n[BBOX-398] 2揿/次,吸入,bid*30天\n[BBOX-399] 孟鲁司特钠片◆\n[BBOX-400] 10mg*30/瓶\n[BBOX-401] 30片\n[BBOX-402] 1.05\n[BBOX-403] 31.53\n[BBOX-404] Sig\n[BBOX-405] 10mg/次,口服,qn*30天\n[BBOX-406] CS 扫描全能王\n[BBOX-407] 3亿人都在用的扫描App\n[BBOX-408] 门(急)诊处方\n[BBOX-409] 就诊时间:2024-11-18\n[BBOX-410] 就诊科室:内科门诊\n[BBOX-411] 主诊\n[BBOX-412] 姓名\n[BBOX-413] 性别:男\n[BBOX-414] 年龄:63岁\n[BBOX-415] 卡号:\n[BBOX-416] 患者类型:GLP支付\n[BBOX-417] 医疗证号:\n[BBOX-418] 处方\n[BBOX-419] 地址:\n[BBOX-420] 身份证号:\n[BBOX-421] 诊断:支气管哮喘,非危重\n[BBOX-422] 西药处方\n[BBOX-423] 组号\n[BBOX-424] 项目名称\n[BBOX-425] 规格\n[BBOX-426] 总量\n[BBOX-427] 单价\n[BBOX-428] 金额\n[BBOX-429] R:\n[BBOX-430] 倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿\n[BBOX-431] 221.61 221.61\n[BBOX-432] Sig\n[BBOX-433] 2揿/次,吸入,bid*30天\n[BBOX-434] 孟鲁司特钠片\n[BBOX-435] 10mg*30/瓶\n[BBOX-436] 30片\n[BBOX-437] 1.05\n[BBOX-438] 31.53\n[BBOX-439] Sig\n[BBOX-440] 10mg/次,口服,qn*30天\n[BBOX-441] CS 扫描全能王\n[BBOX-442] 3亿人都在用的扫描App\n[BBOX-443] \\begin{tabular}{llllllll}\n[BBOX-444] \\hline\n[BBOX-445] 序号 & 项目代码 & 结果 & 提示 & 单位 & 参考范围 & 试验方法 \\\\\n[BBOX-446] \\hline\n[BBOX-447] 1 & 白细胞(WBC) & 9.17 & & 10^9/L & 3.5 -- 9.5 & \\\\\n[BBOX-448] 2 & 中性粒细胞总数(NEU) & 5.71 & & 10^9/L & 1.8 -- 6.3 & \\\\\n[BBOX-449] 3 & 中性粒细胞百分数(NEUN) & 62.30 & & \\% & 40 -- 75 & \\\\\n[BBOX-450] 4 & 淋巴细胞总数(LY) & 2.62 & & 10^9/L & 1.1 -- 3.2 & \\\\\n[BBOX-451] 5 & 淋巴细胞百分数(LYN) & 28.60 & & \\% & 20 -- 50 & \\\\\n[BBOX-452] 6 & 单核细胞总数(MONO) & 0.47 & & 10^9/L & 0.1 -- 0.6 & \\\\\n[BBOX-453] 7 & 单核细胞百分数(MON0) & 5.10 & & \\% & 3 -- 10 & \\\\\n[BBOX-454] 8 & 嗜酸性粒细胞总数(EOS) & 0.34 & & 10^9/L & 0.02 -- 0.52 & \\\\\n[BBOX-455] 9 & 嗜酸性粒细胞百分数(EOS%) & 3.70 & & \\% & 0.4 -- 8 & \\\\\n[BBOX-456] 10 & 嗜碱性粒细胞总数(BAS0) & 0.03 & & 10^9/L & 0 -- 0.06 & \\\\\n[BBOX-457] 11 & 嗜碱性粒细胞百分比(BAS0%) & 0.30 & & \\% & 0 -- 1 & \\\\\n[BBOX-458] 12 & 红细胞(RBC) & 4.91 & 【广州】 & 10^12/L & 4.3 -- 5.8 & \\\\\n[BBOX-459] 13 & 血红蛋白(HGB) & 158 & 【广州】 & g/L & 130 -- 175 & \\\\\n[BBOX-460] 14 & 红细胞压积(HCT) & 47.10 & 【广州】 & \\% & 40 -- 50 & \\\\\n[BBOX-461] 15 & 红细胞平均容积(MCV) & 96.90 & 【广州】 & fl & 82 -- 100 & \\\\\n[BBOX-462] 16 & 红细胞平均血红蛋白(MCH) & 32.20 & 【广州】 & pg & 27 -- 34 & \\\\\n[BBOX-463] 17 & 红细胞平均血红蛋白浓度(MCHC) & 335.00 & 【广州】 & g/L & 316 -- 354 & \\\\\n[BBOX-464] 18 & 红细胞分布宽度(RDW) & 12.40 & & \\% & 11.6 -- 14.8 & \\\\\n[BBOX-465] 19 & 红细胞分布宽度-SD(RDW-SD) & 44.10 & & fl & 37.1 -- 49.2 & \\\\\n[BBOX-466] 20 & 血小板(Plt) & 197 & 【广州】 & 10^9/L & 125 -- 350 & \\\\\n[BBOX-467] 21 & 平均血小板容积(MPV) & 10.70 & & fl & 6 -- 12 & \\\\\n[BBOX-468] 22 & 平均血小板比容(Pct) & 0.21 & & \\% & 0.10 -- 0.29 & \\\\\n[BBOX-469] 23 & 血小板分布宽度(PDW) & 13.00 & & 10(GSP) & 15.3 -- 20.5 & \\\\\n[BBOX-470] 24 & 大血小板(P-LCR) & 30.90 & & \\% & & \\\\\n[BBOX-471] 25 & 网织红细胞绝对值(RETR) & 90.5 & & 10^9/L & 46.4 -- 121.2 & \\\\\n[BBOX-472] 26 & 网织红细胞百分数(RETR) & 1.64 & & \\% & & \\\\\n[BBOX-473] 27 & 低荧光强度网织红细胞比率(LFF) & 83.8 & $\\downarrow$ & \\% & 89.9 -- 98.4 & \\\\\n[BBOX-474] 28 & 中荧光强度网织红细胞比率(MFF) & 13.3 & $\\uparrow$ & \\% & 1.6 -- 9.5 & \\\\\n[BBOX-475] 29 & 高荧光强度网织红细胞比率(HFF) & 2.9 & $\\uparrow$ & \\% & 0 -- 1.7 & \\\\\n[BBOX-476] 30 & 未成熟网织红细胞比率(IRF) & 16.2 & $\\uparrow$ & \\% & 1.6 -- 10.5 & \\\\\n[BBOX-477] 31 & 有核红细胞计数(NRBCW) & 0 & & 10^9/L & & \\\\\n[BBOX-478] 32 & 有核红细胞百分比(NRBC%) & 0 & & \\% & & \\\\\n[BBOX-479] \\hline\n[BBOX-480] \\end{tabular}\n[BBOX-481] 处方笺\n[BBOX-482] 普通\n[BBOX-483] 诊疗\n[BBOX-484] 患者姓\n[BBOX-485] 男\n[BBOX-486] 年龄：65岁\n[BBOX-487] 费别：\n[BBOX-488] 科室：\n[BBOX-489] 2026-01-06 11:28:26\n[BBOX-490] 处方号\n[BBOX-491] 地址：\n[BBOX-492] 联系电\n[BBOX-493] 身份号\n[BBOX-494] 诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎\n[BBOX-495] R\n[BBOX-496] P:\n[BBOX-497] 倍氯米松福莫特罗吸入气雾剂◆① 100ug/6ug/揿*120\n[BBOX-498] 1瓶\n[BBOX-499] 剂量：每次2揿 ( 1/60 瓶 )\n[BBOX-500] 用法：吸入用药\n[BBOX-501] bid 01-06\n[BBOX-502] 孟鲁司特钠片(省采)◆\n[BBOX-503] 10mg*5/盒\n[BBOX-504] 30片\n[BBOX-505] 剂量：每次10mg (1 片 )\n[BBOX-506] 用法：口服\n[BBOX-507] qd 01-06\n[BBOX-508] 处方金额：298.47元\n[BBOX-509] 取药药房：门诊西药房（荔湾）\n[BBOX-510] 处方笺\n[BBOX-511] 普通\n[BBOX-512] 诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎\n[BBOX-513] 患者\n[BBOX-514] 年龄：65岁\n[BBOX-515] 费别\n[BBOX-516] 科室\n[BBOX-517] 6-01-06 11:31:02\n[BBOX-518] 处方\n[BBOX-519] 地址\n[BBOX-520] 联系\n[BBOX-521] 身份\n[BBOX-522] Rp:\n[BBOX-523] 左氧氟沙星片(省采)●⑥\n[BBOX-524] 0.5g*28片/盒\n[BBOX-525] 3片\n[BBOX-526] 剂量：每次0.5g\n[BBOX-527] (1 片)\n[BBOX-528] 用法：口服\n[BBOX-529] qd\n[BBOX-530] 01-06\n[BBOX-531] 醋酸泼尼松片●②⑥\n[BBOX-532] 5mg*100/瓶\n[BBOX-533] 6片\n[BBOX-534] 剂量：每次10mg\n[BBOX-535] (2 片)\n[BBOX-536] 用法：口服\n[BBOX-537] qm\n[BBOX-538] 01-06\n[BBOX-539] 盐酸氨溴索分散片(省采)●⑥\n[BBOX-540] 30mg*50/盒\n[BBOX-541] 15片\n[BBOX-542] 剂量：每次30mg\n[BBOX-543] (1 片)\n[BBOX-544] 用法：餐后口服\n[BBOX-545] tid\n[BBOX-546] 01-06\n[BBOX-547] 处方金额：3.47元\n[BBOX-548] 取药药房：门诊西药房（荔湾）\n[BBOX-549] 医师手签：\n[BBOX-550] 病历编号：\n[BBOX-551] 姓名：\n[BBOX-552] 性别：男\n[BBOX-553] 年龄：65岁\n[BBOX-554] 就诊科室：内科门诊（基础）\n[BBOX-555] 医生：\n[BBOX-556] 就诊时间：2026-02-04 11:23:30\n[BBOX-557] 主诉：支气管哮喘治疗后复诊\n[BBOX-558] 现病史：2022年3月前开始出现咳嗽、咳痰，粘白，量少，能咯出，咳嗽呈阵发性，偶则激性，伴轻度咽痒，无气促，夜间有喘息、胸闷，伴鼻塞、流涕、喉咙，无咽痛，\n[BBOX-559] 无反酸、嗳气、腹胀，无上腹部隐痛不适感，无伴发热、畏寒，曾自服肺力咳症状未见缓解，现病情好转、稳定，本次门诊距上次门诊间隔时间7天；过去4周，症状控制情况：控制良好，吸入药物使用情况：遵医嘱使用；，吸入装置使用情况：有，正确；急性发作情况：\n[BBOX-560] 两次就诊期间急性发作：发作次数：0次，长期规律使用倍氯米松福莫特罗吸入气雾剂治疗。\n[BBOX-561] 既往史：鼻炎病史，有糖尿病史\n[BBOX-562] 过敏史：未发现\n[BBOX-563] 个人史：否认遗传病史，吸烟30年，6支/日，已戒烟8年，饮酒6年，1两/日。\n[BBOX-564] 体格检查：神志清，口腔无溃疡、粘膜白斑，肺部听诊，鼻塞，通气，气管居中，双肺呼吸音稍减弱，未闻及明显干湿性罗音。\n[BBOX-565] 专科情况：\n[BBOX-566] 辅助检查：血常规：Q-CRP：0.54mg/l 白细胞：5.5*109/L 中性粒细胞：\n[BBOX-567] 5.17*109/L 60.5% 淋巴细胞：2.23*109/L 26.2% 单个核细胞：\n[BBOX-568] 0.46*109/L 5.4% 嗜酸性粒细胞：0.6*109/L 7.1% 呼出气一氧化\n[BBOX-569] 氮：FeNO50：130ppb FnNO10：161ppb 肺功能：轻度阻塞性通气功能障碍，支气管激发\n[BBOX-570] 试验阳性（PD20=0.312mg AHI：轻度），胸片：心、肺、膈未见异常\n[BBOX-571] 治疗项目：\n[BBOX-572] 门诊诊断：\n[BBOX-573] 1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、2型糖尿病\n[BBOX-574] 单 种：\n[BBOX-575] 发病时间：\n[BBOX-576] 处 置：请仔细阅读药品说明书等文书资料，遵嘱治疗，不适随诊。\n[BBOX-577] 倍氯米松福莫特罗吸入气雾剂◆① 1瓶2.0瓶，吸入用药，一天2次 30天\n[BBOX-578] 孟鲁司特钠片（省采）◆ 6盒10.0mg，口服，每日1次（口服） 30天\n[BBOX-579] 备 注：建议在停药附近社区医疗机构随访。"
  }
]
2026-08-05 04:45:08,796 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:45:08.795+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 10, "failed": 0, "current": {"333155a8908811f1a3da71efcdd7cc1f": {"id": "333155a8908811f1a3da71efcdd7cc1f", "doc_id": "32f80906908811f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412392, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905007404, "task_type": "dataflow", "root_trace_id": "8cc21299ba8c4c4f9376bb5b55f5585f", "root_traceparent": "00-8cc21299ba8c4c4f9376bb5b55f5585f-3809269866d439b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:45:17,537 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 04:45:17,560 INFO     29 [SmartSplitter] SmartSplitter done: 16 chunks from 16 LLM segments (all bbox_id). Types: {'OutpatientRecord': 4, 'PrescriptionRecord': 11, 'LabReport': 1}
2026-08-05 04:45:17,568 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-05 04:45:17,568 INFO     29 [Trace] task=333155a8 | doc=HXJ 哮喘 广三.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "580 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "chunks", "chunks": "16 items, types={'OutpatientRecord': 4, 'PrescriptionRecord': 11, 'LabReport': 1}"}
2026-08-05 04:45:17,568 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-05 04:45:17,569 INFO     29 [ChunkRouter] Routed 16 chunks into 3 groups: {'chunks_Clinical': 4, 'chunks_Prescription': 11, 'chunks_LabExam': 1}
2026-08-05 04:45:17,576 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-05 04:45:17,576 INFO     29 [Trace] task=333155a8 | doc=HXJ 哮喘 广三.pdf | ChunkRouter:Router | outputs={"html": "", "json": "580 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "chunks", "chunks": "16 items, types={'OutpatientRecord': 4, 'PrescriptionRecord': 11, 'LabReport': 1}", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Prescription": "11 items, types={'PrescriptionRecord': 11}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Prescription\": 11, \"chunks_LabExam\": 1}"}
2026-08-05 04:45:17,576 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-05 04:45:17,581 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:45:17,581 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[13]
2026-08-05 04:45:17,581 INFO     29 [qwen-vl-table] positions ： [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:45:17,759 INFO     29 [qwen-vl-table] page=13, rect=842x595, img=(2339x1653)
2026-08-05 04:45:17,759 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:45:17,759 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 443, \"bbox_end\": 480, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllll}\n\\hline\n序号 & 项目代码 & 结果 & 提示 & 单位 & 参考范围 & 试验方法 \\\\\n\\hline\n1 & 白细胞(WBC) & 9.17 & & 10^9/L & 3.5 -- 9.5 & \\\\\n2 & 中性粒细胞总数(NEU) & 5.71 & & 10^9/L & 1.8 -- 6.3 & \\\\\n3 & 中性粒细胞百分数(NEUN) & 62.30 & & \\% & 40 -- 75 & \\\\\n4 & 淋巴细胞总数(LY) & 2.62 & & 10^9/L & 1.1 -- 3.2 & \\\\\n5 & 淋巴细胞百分数(LYN) & 28.60 & & \\% & 20 -- 50 & \\\\\n6 & 单核细胞总数(MONO) & 0.47 & & 10^9/L & 0.1 -- 0.6 & \\\\\n7 & 单核细胞百分数(MON0) & 5.10 & & \\% & 3 -- 10 & \\\\\n8 & 嗜酸性粒细胞总数(EOS) & 0.34 & & 10^9/L & 0.02 -- 0.52 & \\\\\n9 & 嗜酸性粒细胞百分数(EOS%) & 3.70 & & \\% & 0.4 -- 8 & \\\\\n10 & 嗜碱性粒细胞总数(BAS0) & 0.03 & & 10^9/L & 0 -- 0.06 & \\\\\n11 & 嗜碱性粒细胞百分比(BAS0%) & 0.30 & & \\% & 0 -- 1 & \\\\\n12 & 红细胞(RBC) & 4.91 & 【广州】 & 10^12/L & 4.3 -- 5.8 & \\\\\n13 & 血红蛋白(HGB) & 158 & 【广州】 & g/L & 130 -- 175 & \\\\\n14 & 红细胞压积(HCT) & 47.10 & 【广州】 & \\% & 40 -- 50 & \\\\\n15 & 红细胞平均容积(MCV) & 96.90 & 【广州】 & fl & 82 -- 100 & \\\\\n16 & 红细胞平均血红蛋白(MCH) & 32.20 & 【广州】 & pg & 27 -- 34 & \\\\\n17 & 红细胞平均血红蛋白浓度(MCHC) & 335.00 & 【广州】 & g/L & 316 -- 354 & \\\\\n18 & 红细胞分布宽度(RDW) & 12.40 & & \\% & 11.6 -- 14.8 & \\\\\n19 & 红细胞分布宽度-SD(RDW-SD) & 44.10 & & fl & 37.1 -- 49.2 & \\\\\n20 & 血小板(Plt) & 197 & 【广州】 & 10^9/L & 125 -- 350 & \\\\\n21 & 平均血小板容积(MPV) & 10.70 & & fl & 6 -- 12 & \\\\\n22 & 平均血小板比容(Pct) & 0.21 & & \\% & 0.10 -- 0.29 & \\\\\n23 & 血小板分布宽度(PDW) & 13.00 & & 10(GSP) & 15.3 -- 20.5 & \\\\\n24 & 大血小板(P-LCR) & 30.90 & & \\% & & \\\\\n25 & 网织红细胞绝对值(RETR) & 90.5 & & 10^9/L & 46.4 -- 121.2 & \\\\\n26 & 网织红细胞百分数(RETR) & 1.64 & & \\% & & \\\\\n27 & 低荧光强度网织红细胞比率(LFF) & 83.8 & $\\downarrow$ & \\% & 89.9 -- 98.4 & \\\\\n28 & 中荧光强度网织红细胞比率(MFF) & 13.3 & $\\uparrow$ & \\% & 1.6 -- 9.5 & \\\\\n29 & 高荧光强度网织红细胞比率(HFF) & 2.9 & $\\uparrow$ & \\% & 0 -- 1.7 & \\\\\n30 & 未成熟网织红细胞比率(IRF) & 16.2 & $\\uparrow$ & \\% & 1.6 -- 10.5 & \\\\\n31 & 有核红细胞计数(NRBCW) & 0 & & 10^9/L & & \\\\\n32 & 有核红细胞百分比(NRBC%) & 0 & & \\% & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
[92m04:45:17 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:45:17,760 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:45:41,650 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:45:41.646+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 10, "failed": 0, "current": {"333155a8908811f1a3da71efcdd7cc1f": {"id": "333155a8908811f1a3da71efcdd7cc1f", "doc_id": "32f80906908811f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412392, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905007404, "task_type": "dataflow", "root_trace_id": "8cc21299ba8c4c4f9376bb5b55f5585f", "root_traceparent": "00-8cc21299ba8c4c4f9376bb5b55f5585f-3809269866d439b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:45:43,668 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:45:43,668 INFO     29 [qwen-vl-table] page=13 LLM output (len=5506):
{
  "report_date": null,
  "items": [
    {
      "name": "白细胞",
      "item_code": "WBC",
      "value": "9.17",
      "unit": "10^9/L",
      "reference_range": "3.5 -- 9.5",
      "abnormal": false
    },
    {
      "name": "中性粒细胞总数",
      "item_code": "NEU",
      "value": "5.71",
      "unit": "10^9/L",
      "reference_range": "1.8 -- 6.3",
      "abnormal": false
    },
    {
      "name": "中性粒细胞百分数",
      "item_code": "NEUN",
      "value": "62.30",
      "unit": "%",
      "reference_range": "40 -- 75",
      "abnormal": false
    },
    {
      "name": "淋巴细胞总数",
      "item_code": "LY",
      "value": "2.62",
      "unit": "10^9/L",
      "reference_range": "1.1 -- 3.2",
      "abnormal": false
    },
    {
      "name": "淋巴细胞百分数",
      "item_code": "LYN",
      "value": "28.60",
      "unit": "%",
      "reference_range": "20 -- 50",
      "abnormal": false
    },
    {
      "name": "单核细胞总数",
      "item_code": "MONO",
      "value": "0.47",
      "unit": "10^9/L",
      "reference_range": "0.1 -- 0.6",
      "abnormal": false
    },
    {
      "name": "单核细胞百分数",
      "item_code": "MON0",
      "value": "5.10",
      "unit": "%",
      "reference_range": "3 -- 10",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞总数",
      "item_code": "EOS",
      "value": "0.34",
      "unit": "10^9/L",
      "reference_range": "0.02 -- 0.52",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞百分数",
      "item_code": "EOS%",
      "value": "3.70",
      "unit": "%",
      "reference_range": "0.4 -- 8",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞总数",
      "item_code": "BAS0",
      "value": "0.03",
      "unit": "10^9/L",
      "reference_range": "0 -- 0.06",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞百分比",
      "item_code": "BAS0%",
      "value": "0.30",
      "unit": "%",
      "reference_range": "0 -- 1",
      "abnormal": false
    },
    {
      "name": "红细胞",
      "item_code": "RBC",
      "value": "4.91",
      "unit": "10^12/L",
      "reference_range": "4.3 -- 5.8",
      "abnormal": false
    },
    {
      "name": "血红蛋白",
      "item_code": "HGB",
      "value": "158",
      "unit": "g/L",
      "reference_range": "130 -- 175",
      "abnormal": false
    },
    {
      "name": "红细胞压积",
      "item_code": "HCT",
      "value": "47.10",
      "unit": "%",
      "reference_range": "40 -- 50",
      "abnormal": false
    },
    {
      "name": "红细胞平均容积",
      "item_code": "MCV",
      "value": "96.90",
      "unit": "fl",
      "reference_range": "82 -- 100",
      "abnormal": false
    },
    {
      "name": "红细胞平均血红蛋白",
      "item_code": "MCH",
      "value": "32.20",
      "unit": "pg",
      "reference_range": "27 -- 34",
      "abnormal": false
    },
    {
      "name": "红细胞平均血红蛋白浓度",
      "item_code": "MCHC",
      "value": "335.00",
      "unit": "g/L",
      "reference_range": "316 -- 354",
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度",
      "item_code": "RDW",
      "value": "12.40",
      "unit": "%",
      "reference_range": "11.6 -- 14.8",
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度-SD",
      "item_code": "RDW-SD",
      "value": "44.10",
      "unit": "fl",
      "reference_range": "37.1 -- 49.2",
      "abnormal": false
    },
    {
      "name": "血小板",
      "item_code": "Plt",
      "value": "197",
      "unit": "10^9/L",
      "reference_range": "125 -- 350",
      "abnormal": false
    },
    {
      "name": "平均血小板容积",
      "item_code": "MPV",
      "value": "10.70",
      "unit": "fl",
      "reference_range": "6 -- 12",
      "abnormal": false
    },
    {
      "name": "平均血小板比容",
      "item_code": "Pct",
      "value": "0.21",
      "unit": "%",
      "reference_range": "0.10 -- 0.29",
      "abnormal": false
    },
    {
      "name": "血小板分布宽度",
      "item_code": "PDW",
      "value": "13.00",
      "unit": "10(GSP)",
      "reference_range": "15.3 -- 20.5",
      "abnormal": true
    },
    {
      "name": "大血小板",
      "item_code": "P-LCR",
      "value": "30.90",
      "unit": "%",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "网织红细胞绝对值",
      "item_code": "RETR",
      "value": "90.5",
      "unit": "10^9/L",
      "reference_range": "46.4 -- 121.2",
      "abnormal": false
    },
    {
      "name": "网织红细胞百分数",
      "item_code": "RETR",
      "value": "1.64",
      "unit": "%",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "低荧光强度网织红细胞比率",
      "item_code": "LFF",
      "value": "83.8",
      "unit": "%",
      "reference_range": "89.9 -- 98.4",
      "abnormal": true
    },
    {
      "name": "中荧光强度网织红细胞比率",
      "item_code": "MFF",
      "value": "13.3",
      "unit": "%",
      "reference_range": "1.6 -- 9.5",
      "abnormal": true
    },
    {
      "name": "高荧光强度网织红细胞比率",
      "item_code": "HFF",
      "value": "2.9",
      "unit": "%",
      "reference_range": "0 -- 1.7",
      "abnormal": true
    },
    {
      "name": "未成熟网织红细胞比率",
      "item_code": "IRF",
      "value": "16.2",
      "unit": "%",
      "reference_range": "1.6 -- 10.5",
      "abnormal": true
    },
    {
      "name": "有核红细胞计数",
      "item_code": "NRBCW",
      "value": "0",
      "unit": "10^9/L",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "有核红细胞百分比",
      "item_code": "NRBC%",
      "value": "0",
      "unit": "%",
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-05 04:45:43,668 INFO     29 [qwen-vl-table] coord grouping: {13: 32}
2026-08-05 04:45:43,671 INFO     29 [qwen-vl-table] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1446940, prompt_len=777
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞、中性粒细胞总数、中性粒细胞百分数、淋巴细胞总数、淋巴细胞百分数、单核细胞总数、单核细胞百分数、嗜酸性粒细胞总数、嗜酸性粒细胞百分数、嗜碱性粒细胞总数、嗜碱性粒细胞百分比、红细胞、血红蛋白、红细胞压积、红细胞平均容积、红细胞平均血红蛋白、红细胞平均血红蛋白浓度、红细胞分布宽度、红细胞分布宽度-SD、血小板、平均血小板容积、平均血小板比容、血小板分布宽度、大血小板、网织红细胞绝对值、网织红细胞百分数、低荧光强度网织红细胞比率、中荧光强度网织红细胞比率、高荧光强度网织红细胞比率、未成熟网织红细胞比率、有核红细胞计数、有核红细胞百分比

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
2026-08-05 04:45:52,330 INFO     29 [qwen-vl-table] coord API raw response (len=1681):
[
	{"text": "白细胞", "bbox": [238, 147, 307, 163]},
	{"text": "中性粒细胞总数", "bbox": [238, 170, 356, 186]},
	{"text": "中性粒细胞百分数", "bbox": [238, 193, 375, 209]},
	{"text": "淋巴细胞总数", "bbox": [238, 217, 337, 233]},
	{"text": "淋巴细胞百分数", "bbox": [238, 240, 356, 256]},
	{"text": "单核细胞总数", "bbox": [238, 263, 350, 279]},
	{"text": "单核细胞百分数", "bbox": [238, 287, 368, 303]},
	{"text": "嗜酸性粒细胞总数", "bbox": [238, 310, 369, 326]},
	{"text": "嗜酸性粒细胞百分数", "bbox": [238, 334, 387, 350]},
	{"text": "嗜碱性粒细胞总数", "bbox": [238, 357, 375, 373]},
	{"text": "嗜碱性粒细胞百分比", "bbox": [238, 380, 393, 396]},
	{"text": "红细胞", "bbox": [238, 404, 305, 420]},
	{"text": "血红蛋白", "bbox": [238, 427, 317, 443]},
	{"text": "红细胞压积", "bbox": [238, 450, 331, 466]},
	{"text": "红细胞平均容积", "bbox": [238, 473, 355, 489]},
	{"text": "红细胞平均血红蛋白", "bbox": [238, 496, 380, 512]},
	{"text": "红细胞平均血红蛋白浓度", "bbox": [238, 519, 413, 535]},
	{"text": "红细胞分布宽度", "bbox": [238, 543, 355, 559]},
	{"text": "红细胞分布宽度-SD", "bbox": [238, 566, 393, 582]},
	{"text": "血小板", "bbox": [238, 589, 305, 605]},
	{"text": "平均血小板容积", "bbox": [238, 612, 355, 628]},
	{"text": "平均血小板比容", "bbox": [238, 636, 355, 652]},
	{"text": "血小板分布宽度", "bbox": [238, 659, 355, 675]},
	{"text": "大血小板", "bbox": [238, 682, 330, 698]},
	{"text": "网织红细胞绝对值", "bbox": [238, 705, 374, 721]},
	{"text": "网织红细胞百分数", "bbox": [238, 728, 374, 744]},
	{"text": "低荧光强度网织红细胞比率", "bbox": [238, 751, 420, 767]},
	{"text": "中荧光强度网织红细胞比率", "bbox": [238, 774, 420, 790]},
	{"text": "高荧光强度网织红细胞比率", "bbox": [238, 797, 420, 813]},
	{"text": "未成熟网织红细胞比率", "bbox": [238, 820, 393, 836]},
	{"text": "有核红细胞计数", "bbox": [238, 844, 368, 860]},
	{"text": "有核红细胞百分比", "bbox": [238, 867, 380, 883]}
]
2026-08-05 04:45:52,330 INFO     29 [qwen-vl-table] coord API: raw_items=32, valid_items=32, elapsed=8.7s
2026-08-05 04:45:52,330 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞, bbox=[238, 147, 307, 163]
2026-08-05 04:45:52,330 INFO     29 [qwen-vl-table] coord item[1]: text=中性粒细胞总数, bbox=[238, 170, 356, 186]
2026-08-05 04:45:52,330 INFO     29 [qwen-vl-table] coord item[2]: text=中性粒细胞百分数, bbox=[238, 193, 375, 209]
2026-08-05 04:45:52,330 INFO     29 [qwen-vl-table] coord item[3]: text=淋巴细胞总数, bbox=[238, 217, 337, 233]
2026-08-05 04:45:52,330 INFO     29 [qwen-vl-table] coord item[4]: text=淋巴细胞百分数, bbox=[238, 240, 356, 256]
2026-08-05 04:45:52,330 INFO     29 [qwen-vl-table] coord item[5]: text=单核细胞总数, bbox=[238, 263, 350, 279]
2026-08-05 04:45:52,330 INFO     29 [qwen-vl-table] coord item[6]: text=单核细胞百分数, bbox=[238, 287, 368, 303]
2026-08-05 04:45:52,330 INFO     29 [qwen-vl-table] coord item[7]: text=嗜酸性粒细胞总数, bbox=[238, 310, 369, 326]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[8]: text=嗜酸性粒细胞百分数, bbox=[238, 334, 387, 350]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[9]: text=嗜碱性粒细胞总数, bbox=[238, 357, 375, 373]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[10]: text=嗜碱性粒细胞百分比, bbox=[238, 380, 393, 396]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[11]: text=红细胞, bbox=[238, 404, 305, 420]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[12]: text=血红蛋白, bbox=[238, 427, 317, 443]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[13]: text=红细胞压积, bbox=[238, 450, 331, 466]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[14]: text=红细胞平均容积, bbox=[238, 473, 355, 489]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[15]: text=红细胞平均血红蛋白, bbox=[238, 496, 380, 512]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[16]: text=红细胞平均血红蛋白浓度, bbox=[238, 519, 413, 535]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[17]: text=红细胞分布宽度, bbox=[238, 543, 355, 559]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[18]: text=红细胞分布宽度-SD, bbox=[238, 566, 393, 582]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[19]: text=血小板, bbox=[238, 589, 305, 605]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[20]: text=平均血小板容积, bbox=[238, 612, 355, 628]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[21]: text=平均血小板比容, bbox=[238, 636, 355, 652]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[22]: text=血小板分布宽度, bbox=[238, 659, 355, 675]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[23]: text=大血小板, bbox=[238, 682, 330, 698]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[24]: text=网织红细胞绝对值, bbox=[238, 705, 374, 721]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[25]: text=网织红细胞百分数, bbox=[238, 728, 374, 744]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[26]: text=低荧光强度网织红细胞比率, bbox=[238, 751, 420, 767]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[27]: text=中荧光强度网织红细胞比率, bbox=[238, 774, 420, 790]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[28]: text=高荧光强度网织红细胞比率, bbox=[238, 797, 420, 813]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[29]: text=未成熟网织红细胞比率, bbox=[238, 820, 393, 836]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[30]: text=有核红细胞计数, bbox=[238, 844, 368, 860]
2026-08-05 04:45:52,331 INFO     29 [qwen-vl-table] coord item[31]: text=有核红细胞百分比, bbox=[238, 867, 380, 883]
2026-08-05 04:45:52,332 INFO     29 [qwen-vl-table] page=13 coord: matched 32/32, time=8.7s
2026-08-05 04:45:52,332 INFO     29 [qwen-vl-table] new_positions (32):
[[14, 200.396, 258.49399999999997, 87.46499999999999, 96.985], [14, 200.396, 299.752, 101.14999999999999, 110.67], [14, 200.396, 315.75, 114.835, 124.35499999999999], [14, 200.396, 283.75399999999996, 129.11499999999998, 138.635], [14, 200.396, 299.752, 142.79999999999998, 152.32], [14, 200.396, 294.7, 156.48499999999999, 166.005], [14, 200.396, 309.856, 170.765, 180.285], [14, 200.396, 310.698, 184.45, 193.97], [14, 200.396, 325.854, 198.73, 208.25], [14, 200.396, 315.75, 212.415, 221.935], [14, 200.396, 330.906, 226.1, 235.61999999999998], [14, 200.396, 256.81, 240.38, 249.89999999999998], [14, 200.396, 266.914, 254.065, 263.585], [14, 200.396, 278.702, 267.75, 277.27], [14, 200.396, 298.90999999999997, 281.435, 290.955], [14, 200.396, 319.96, 295.12, 304.64], [14, 200.396, 347.746, 308.805, 318.325], [14, 200.396, 298.90999999999997, 323.085, 332.60499999999996], [14, 200.396, 330.906, 336.77, 346.28999999999996], [14, 200.396, 256.81, 350.455, 359.97499999999997], [14, 200.396, 298.90999999999997, 364.14, 373.65999999999997], [14, 200.396, 298.90999999999997, 378.41999999999996, 387.94], [14, 200.396, 298.90999999999997, 392.10499999999996, 401.625], [14, 200.396, 277.86, 405.78999999999996, 415.31], [14, 200.396, 314.908, 419.47499999999997, 428.995], [14, 200.396, 314.908, 433.15999999999997, 442.68], [14, 200.396, 353.64, 446.84499999999997, 456.36499999999995], [14, 200.396, 353.64, 460.53, 470.04999999999995], [14, 200.396, 353.64, 474.215, 483.73499999999996], [14, 200.396, 330.906, 487.9, 497.41999999999996], [14, 200.396, 309.856, 502.17999999999995, 511.7], [14, 200.396, 319.96, 515.865, 525.385]]
2026-08-05 04:45:52,332 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=32, matched=32, pages=1, time=34.8s
2026-08-05 04:45:52,341 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-05 04:45:52,341 INFO     29 [Trace] task=333155a8 | doc=HXJ 哮喘 广三.pdf | Extractor:LabExam | outputs={"chunks": "1 items, types={'LabReport': 1}", "html": "", "json": "580 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Prescription": "11 items, types={'PrescriptionRecord': 11}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Prescription\": 11, \"chunks_LabExam\": 1}"}
2026-08-05 04:45:52,341 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-05 04:45:52,346 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:45:52,346 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m04:45:52 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:45:52,347 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:45:53,403 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:45:53,408 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-05 04:45:53,408 INFO     29 [Trace] task=333155a8 | doc=HXJ 哮喘 广三.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "580 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Prescription": "11 items, types={'PrescriptionRecord': 11}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Prescription\": 11, \"chunks_LabExam\": 1}"}
2026-08-05 04:45:53,408 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-05 04:45:53,413 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:45:53,413 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 04:45:53,414 INFO     29 [qwen-vl-text] positions(33): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:45:53,414 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [33]
2026-08-05 04:45:53,763 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 04:45:53,765 INFO     29 [qwen-vl-text] LLM extraction start, text_len=272
2026-08-05 04:45:53,765 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:45:53,765 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 32, \"encounter_dates\": [\"2025-10-21\"], \"department\": \"内科门诊(荔湾)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门(急)诊病历信息\n就诊卡\n流水\n病历编号:\n姓\n别:男\n年\n龄:64岁\n就诊科室:内科门诊(荔湾)\n医\n诊时间:2025-10-21 16:24:23\n主\n诉:取药\n现病史:\n既往史:\n过敏史:\n个人史:\n体格检查:\n专科情况:\n辅助检查:\n治疗项目:\n门诊诊断:\n支气管哮喘\n单病种:\n发病时间:\n处置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。\n1孟鲁司特钠片(省采)◆\n1瓶10.0mg,口服,每晚1次\n30天\n2倍氯米松福莫特罗吸入气雾剂◆①\n1瓶2.0揿,吸入用药,一天2次\n30天\n备注:建议在住地附近社区医疗机构随诊。",
    "role": "user"
  }
]
[92m04:45:53 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:45:53,767 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:45:55,604 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:45:55,604 INFO     29 [qwen-vl-text] LLM output (len=241):
{
  "encounter_date": "2025-10-21",
  "chief_complaint": "取药",
  "present_illness": null,
  "past_history": null,
  "diagnosis": "支气管哮喘",
  "treatment_plan": [
    "孟鲁司特钠片(省采) 10.0mg 口服 每晚1次 30天",
    "倍氯米松福莫特罗吸入气雾剂 2.0揿 吸入用药 一天2次 30天"
  ]
}
2026-08-05 04:45:55,604 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-10-21]
2026-08-05 04:45:55,620 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3647382, prompt_len=984
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["门(急)诊病历信息", "就诊卡", "流水", "病历编号:", "姓", "别:男", "年", "龄:64岁", "就诊科室:内科门诊(荔湾)", "医", "诊时间:2025-10-21 16:24:23", "主", "诉:取药", "现病史:", "既往史:", "过敏史:", "个人史:", "体格检查:", "专科情况:", "辅助检查:", "治疗项目:", "门诊诊断:", "支气管哮喘", "单病种:", "发病时间:", "处置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。", "1孟鲁司特钠片(省采)◆", "1瓶10.0mg,口服,每晚1次", "30天", "2倍氯米松福莫特罗吸入气雾剂◆①", "1瓶2.0揿,吸入用药,一天2次", "30天", "备注:建议在住地附近社区医疗机构随诊。"]

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
2026-08-05 04:46:09,161 INFO     29 [qwen-vl-text] coord API raw response (len=2150):
[
	{"text": "门(急)诊病历信息", "bbox": [372, 130, 590, 150]},
	{"text": "就诊卡", "bbox": [196, 184, 246, 200]},
	{"text": "流水", "bbox": [196, 216, 246, 233]},
	{"text": "病历编号:", "bbox": [568, 216, 645, 232]},
	{"text": "姓", "bbox": [196, 249, 214, 265]},
	{"text": "别:男", "bbox": [489, 249, 529, 265]},
	{"text": "年", "bbox": [568, 250, 586, 265]},
	{"text": "龄:64岁", "bbox": [654, 250, 714, 265]},
	{"text": "就诊科室:内科门诊(荔湾)", "bbox": [196, 280, 404, 296]},
	{"text": "医", "bbox": [468, 280, 490, 296]},
	{"text": "诊时间:2025-10-21 16:24:23", "bbox": [578, 280, 816, 296]},
	{"text": "主", "bbox": [196, 312, 214, 328]},
	{"text": "诉:取药", "bbox": [288, 312, 362, 328]},
	{"text": "现病史:", "bbox": [196, 343, 299, 359]},
	{"text": "既往史:", "bbox": [196, 373, 299, 389]},
	{"text": "过敏史:", "bbox": [196, 403, 299, 419]},
	{"text": "个人史:", "bbox": [196, 433, 300, 449]},
	{"text": "体格检查:", "bbox": [199, 463, 283, 478]},
	{"text": "专科情况:", "bbox": [200, 491, 283, 506]},
	{"text": "辅助检查:", "bbox": [200, 519, 283, 534]},
	{"text": "治疗项目:", "bbox": [200, 547, 283, 562]},
	{"text": "门诊诊断:", "bbox": [202, 575, 283, 590]},
	{"text": "支气管哮喘", "bbox": [312, 604, 394, 617]},
	{"text": "单病种:", "bbox": [202, 631, 300, 646]},
	{"text": "发病时间:", "bbox": [202, 660, 283, 674]},
	{"text": "处置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。", "bbox": [291, 686, 735, 700]},
	{"text": "1孟鲁司特钠片(省采)◆", "bbox": [226, 713, 393, 727]},
	{"text": "1瓶10.0mg,口服,每晚1次", "bbox": [528, 713, 708, 727]},
	{"text": "30天", "bbox": [738, 713, 770, 726]},
	{"text": "2倍氯米松福莫特罗吸入气雾剂◆①", "bbox": [226, 739, 474, 753]},
	{"text": "1瓶2.0揿,吸入用药,一天2次", "bbox": [527, 739, 730, 753]},
	{"text": "30天", "bbox": [759, 740, 791, 752]},
	{"text": "备注:建议在住地附近社区医疗机构随诊。", "bbox": [292, 766, 573, 779]},
	{"text": "病情评估:", "bbox": [208, 791, 286, 805]},
	{"text": "病情分级:", "bbox": [512, 791, 590, 805]},
	{"text": "是否抢救病例:否", "bbox": [208, 817, 345, 831]},
	{"text": "是否抢救成功:", "bbox": [437, 817, 545, 831]},
	{"text": "是否为绿色通道患者:否", "bbox": [602, 817, 785, 831]},
	{"text": "病人去向:", "bbox": [210, 844, 287, 857]},
	{"text": "病人来源:自行来院", "bbox": [210, 868, 359, 880]},
	{"text": "是否曾就诊于其他医疗机构:", "bbox": [404, 868, 612, 880]}
]
2026-08-05 04:46:09,161 INFO     29 [qwen-vl-text] coord API: raw_items=41, valid_items=41, elapsed=13.5s
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊病历信息, bbox=[372, 130, 590, 150]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[1]: text=就诊卡, bbox=[196, 184, 246, 200]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[2]: text=流水, bbox=[196, 216, 246, 233]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[3]: text=病历编号:, bbox=[568, 216, 645, 232]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[4]: text=姓, bbox=[196, 249, 214, 265]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[5]: text=别:男, bbox=[489, 249, 529, 265]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[6]: text=年, bbox=[568, 250, 586, 265]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[7]: text=龄:64岁, bbox=[654, 250, 714, 265]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[8]: text=就诊科室:内科门诊(荔湾), bbox=[196, 280, 404, 296]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[9]: text=医, bbox=[468, 280, 490, 296]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[10]: text=诊时间:2025-10-21 16:24:23, bbox=[578, 280, 816, 296]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[11]: text=主, bbox=[196, 312, 214, 328]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[12]: text=诉:取药, bbox=[288, 312, 362, 328]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[13]: text=现病史:, bbox=[196, 343, 299, 359]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[14]: text=既往史:, bbox=[196, 373, 299, 389]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[15]: text=过敏史:, bbox=[196, 403, 299, 419]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[16]: text=个人史:, bbox=[196, 433, 300, 449]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[17]: text=体格检查:, bbox=[199, 463, 283, 478]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[18]: text=专科情况:, bbox=[200, 491, 283, 506]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[19]: text=辅助检查:, bbox=[200, 519, 283, 534]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[20]: text=治疗项目:, bbox=[200, 547, 283, 562]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[21]: text=门诊诊断:, bbox=[202, 575, 283, 590]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[22]: text=支气管哮喘, bbox=[312, 604, 394, 617]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[23]: text=单病种:, bbox=[202, 631, 300, 646]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[24]: text=发病时间:, bbox=[202, 660, 283, 674]
2026-08-05 04:46:09,162 INFO     29 [qwen-vl-text] coord item[25]: text=处置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。, bbox=[291, 686, 735, 700]
2026-08-05 04:46:09,163 INFO     29 [qwen-vl-text] coord item[26]: text=1孟鲁司特钠片(省采)◆, bbox=[226, 713, 393, 727]
2026-08-05 04:46:09,163 INFO     29 [qwen-vl-text] coord item[27]: text=1瓶10.0mg,口服,每晚1次, bbox=[528, 713, 708, 727]
2026-08-05 04:46:09,163 INFO     29 [qwen-vl-text] coord item[28]: text=30天, bbox=[738, 713, 770, 726]
2026-08-05 04:46:09,163 INFO     29 [qwen-vl-text] coord item[29]: text=2倍氯米松福莫特罗吸入气雾剂◆①, bbox=[226, 739, 474, 753]
2026-08-05 04:46:09,163 INFO     29 [qwen-vl-text] coord item[30]: text=1瓶2.0揿,吸入用药,一天2次, bbox=[527, 739, 730, 753]
2026-08-05 04:46:09,163 INFO     29 [qwen-vl-text] coord item[31]: text=30天, bbox=[759, 740, 791, 752]
2026-08-05 04:46:09,163 INFO     29 [qwen-vl-text] coord item[32]: text=备注:建议在住地附近社区医疗机构随诊。, bbox=[292, 766, 573, 779]
2026-08-05 04:46:09,163 INFO     29 [qwen-vl-text] coord item[33]: text=病情评估:, bbox=[208, 791, 286, 805]
2026-08-05 04:46:09,163 INFO     29 [qwen-vl-text] coord item[34]: text=病情分级:, bbox=[512, 791, 590, 805]
2026-08-05 04:46:09,163 INFO     29 [qwen-vl-text] coord item[35]: text=是否抢救病例:否, bbox=[208, 817, 345, 831]
2026-08-05 04:46:09,163 INFO     29 [qwen-vl-text] coord item[36]: text=是否抢救成功:, bbox=[437, 817, 545, 831]
2026-08-05 04:46:09,163 INFO     29 [qwen-vl-text] coord item[37]: text=是否为绿色通道患者:否, bbox=[602, 817, 785, 831]
2026-08-05 04:46:09,163 INFO     29 [qwen-vl-text] coord item[38]: text=病人去向:, bbox=[210, 844, 287, 857]
2026-08-05 04:46:09,163 INFO     29 [qwen-vl-text] coord item[39]: text=病人来源:自行来院, bbox=[210, 868, 359, 880]
2026-08-05 04:46:09,163 INFO     29 [qwen-vl-text] coord item[40]: text=是否曾就诊于其他医疗机构:, bbox=[404, 868, 612, 880]
2026-08-05 04:46:09,163 INFO     29 [qwen-vl-text] page=0 — 33/33 coords, api_time=13.5s
2026-08-05 04:46:09,164 INFO     29 [qwen-vl-text] new_positions (33):
[[0, 221.34, 351.05, 109.46, 126.3], [0, 116.61999999999999, 146.37, 154.928, 168.4], [0, 116.61999999999999, 146.37, 181.87199999999999, 196.186], [0, 337.96, 383.775, 181.87199999999999, 195.344], [0, 116.61999999999999, 127.33, 209.658, 223.13], [0, 290.955, 314.755, 209.658, 223.13], [0, 337.96, 348.66999999999996, 210.5, 223.13], [0, 389.13, 424.83, 210.5, 223.13], [0, 116.61999999999999, 240.38, 235.76, 249.232], [0, 278.46, 291.55, 235.76, 249.232], [0, 343.90999999999997, 485.52, 235.76, 249.232], [0, 116.61999999999999, 127.33, 262.704, 276.176], [0, 171.35999999999999, 215.39, 262.704, 276.176], [0, 116.61999999999999, 177.905, 288.806, 302.27799999999996], [0, 116.61999999999999, 177.905, 314.066, 327.538], [0, 116.61999999999999, 177.905, 339.32599999999996, 352.798], [0, 116.61999999999999, 178.5, 364.586, 378.058], [0, 118.405, 168.385, 389.846, 402.476], [0, 119.0, 168.385, 413.42199999999997, 426.05199999999996], [0, 119.0, 168.385, 436.998, 449.628], [0, 119.0, 168.385, 460.574, 473.204], [0, 120.19, 168.385, 484.15, 496.78], [0, 185.64, 234.42999999999998, 508.568, 519.514], [0, 120.19, 178.5, 531.302, 543.932], [0, 120.19, 168.385, 555.72, 567.5079999999999], [0, 173.14499999999998, 437.325, 577.612, 589.4], [0, 134.47, 233.83499999999998, 600.346, 612.134], [0, 314.15999999999997, 421.26, 600.346, 612.134], [0, 439.10999999999996, 458.15, 600.346, 611.292], [0, 134.47, 282.03, 622.2379999999999, 634.026], [0, 313.565, 434.34999999999997, 622.2379999999999, 634.026], [0, 451.60499999999996, 470.645, 623.0799999999999, 633.184], [0, 173.73999999999998, 340.935, 644.972, 655.918]]
2026-08-05 04:46:09,164 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=15.8s
2026-08-05 04:46:09,164 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:46:09,164 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 04:46:09,164 INFO     29 [qwen-vl-text] positions(29): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:46:09,164 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [29]
2026-08-05 04:46:09,444 INFO     29 [qwen-vl-text] page=1, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 04:46:09,446 INFO     29 [qwen-vl-text] LLM extraction start, text_len=226
2026-08-05 04:46:09,446 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:46:09,447 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 41, \"bbox_end\": 69, \"encounter_dates\": [\"2025-11-19\"], \"department\": \"内科门诊(荔湾)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门(急)诊病历信息\n就诊卡号:\n流水号:\n病历编号:\n性别:男\n年\n龄:65岁\n就诊科室:内科门诊(荔湾)\n医生:\n就诊时间:2025-11-19 11:33:52\n主诉:取药\n现病史:\n既往史:\n过敏史:\n个人史:\n体格检查:\n专科情况:\n辅助检查:\n治疗项目:\n门诊诊断:\n1、支气管哮喘\n处置:\n1孟鲁司特钠片(省采)◆\n1瓶10.0mg,口服,每晚1次\n30天\n2倍氯米松福莫特罗吸入气雾剂◆①\n1瓶2.0揿,吸入用药,一天2次\n30天\n备注:",
    "role": "user"
  }
]
[92m04:46:09 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:46:09,448 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:46:11,979 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:46:11,979 INFO     29 [qwen-vl-text] LLM output (len=241):
{
  "encounter_date": "2025-11-19",
  "chief_complaint": "取药",
  "present_illness": null,
  "past_history": null,
  "diagnosis": "支气管哮喘",
  "treatment_plan": [
    "孟鲁司特钠片(省采) 10.0mg 口服 每晚1次 30天",
    "倍氯米松福莫特罗吸入气雾剂 2.0揿 吸入用药 一天2次 30天"
  ]
}
2026-08-05 04:46:11,979 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-19]
2026-08-05 04:46:11,982 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1618598, prompt_len=926
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["门(急)诊病历信息", "就诊卡号:", "流水号:", "病历编号:", "性别:男", "年", "龄:65岁", "就诊科室:内科门诊(荔湾)", "医生:", "就诊时间:2025-11-19 11:33:52", "主诉:取药", "现病史:", "既往史:", "过敏史:", "个人史:", "体格检查:", "专科情况:", "辅助检查:", "治疗项目:", "门诊诊断:", "1、支气管哮喘", "处置:", "1孟鲁司特钠片(省采)◆", "1瓶10.0mg,口服,每晚1次", "30天", "2倍氯米松福莫特罗吸入气雾剂◆①", "1瓶2.0揿,吸入用药,一天2次", "30天", "备注:"]

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
2026-08-05 04:46:20,255 INFO     29 [qwen-vl-text] coord API raw response (len=1503):
[
	{"text": "门(急)诊病历信息", "bbox": [355, 22, 521, 50]},
	{"text": "就诊卡号:", "bbox": [219, 102, 275, 123]},
	{"text": "流水号:", "bbox": [219, 149, 262, 171]},
	{"text": "病历编号:", "bbox": [506, 150, 563, 171]},
	{"text": "性别:男", "bbox": [439, 199, 478, 220]},
	{"text": "年", "bbox": [506, 200, 520, 220]},
	{"text": "龄:65岁", "bbox": [569, 200, 616, 220]},
	{"text": "就诊科室:内科门诊(荔湾)", "bbox": [220, 246, 382, 267]},
	{"text": "医生:", "bbox": [431, 246, 446, 267]},
	{"text": "就诊时间:2025-11-19 11:33:52", "bbox": [506, 247, 694, 267]},
	{"text": "主诉:取药", "bbox": [219, 293, 350, 314]},
	{"text": "现病史:", "bbox": [219, 339, 302, 360]},
	{"text": "既往史:", "bbox": [219, 384, 302, 405]},
	{"text": "过敏史:", "bbox": [219, 428, 302, 449]},
	{"text": "个人史:", "bbox": [219, 473, 302, 494]},
	{"text": "体格检查:", "bbox": [223, 518, 289, 538]},
	{"text": "专科情况:", "bbox": [223, 563, 289, 583]},
	{"text": "辅助检查:", "bbox": [223, 607, 289, 627]},
	{"text": "治疗项目:", "bbox": [223, 651, 289, 671]},
	{"text": "门诊诊断:", "bbox": [225, 692, 289, 712]},
	{"text": "1、支气管哮喘", "bbox": [294, 735, 378, 754]},
	{"text": "处置:", "bbox": [294, 777, 317, 796]},
	{"text": "1孟鲁司特钠片(省采)◆", "bbox": [244, 819, 375, 839]},
	{"text": "1瓶10.0mg,口服,每晚1次", "bbox": [480, 819, 621, 839]},
	{"text": "30天", "bbox": [645, 820, 670, 838]},
	{"text": "2倍氯米松福莫特罗吸入气雾剂◆①", "bbox": [243, 861, 437, 881]},
	{"text": "1瓶2.0揿,吸入用药,一天2次", "bbox": [480, 861, 638, 881]},
	{"text": "30天", "bbox": [662, 862, 687, 880]},
	{"text": "备注:", "bbox": [228, 902, 242, 919]}
]
2026-08-05 04:46:20,255 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=8.3s
2026-08-05 04:46:20,255 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊病历信息, bbox=[355, 22, 521, 50]
2026-08-05 04:46:20,255 INFO     29 [qwen-vl-text] coord item[1]: text=就诊卡号:, bbox=[219, 102, 275, 123]
2026-08-05 04:46:20,255 INFO     29 [qwen-vl-text] coord item[2]: text=流水号:, bbox=[219, 149, 262, 171]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[3]: text=病历编号:, bbox=[506, 150, 563, 171]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[4]: text=性别:男, bbox=[439, 199, 478, 220]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[5]: text=年, bbox=[506, 200, 520, 220]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[6]: text=龄:65岁, bbox=[569, 200, 616, 220]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[7]: text=就诊科室:内科门诊(荔湾), bbox=[220, 246, 382, 267]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[8]: text=医生:, bbox=[431, 246, 446, 267]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[9]: text=就诊时间:2025-11-19 11:33:52, bbox=[506, 247, 694, 267]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[10]: text=主诉:取药, bbox=[219, 293, 350, 314]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[11]: text=现病史:, bbox=[219, 339, 302, 360]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[12]: text=既往史:, bbox=[219, 384, 302, 405]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[13]: text=过敏史:, bbox=[219, 428, 302, 449]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[14]: text=个人史:, bbox=[219, 473, 302, 494]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[15]: text=体格检查:, bbox=[223, 518, 289, 538]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[16]: text=专科情况:, bbox=[223, 563, 289, 583]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[17]: text=辅助检查:, bbox=[223, 607, 289, 627]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[18]: text=治疗项目:, bbox=[223, 651, 289, 671]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[19]: text=门诊诊断:, bbox=[225, 692, 289, 712]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[20]: text=1、支气管哮喘, bbox=[294, 735, 378, 754]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[21]: text=处置:, bbox=[294, 777, 317, 796]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[22]: text=1孟鲁司特钠片(省采)◆, bbox=[244, 819, 375, 839]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[23]: text=1瓶10.0mg,口服,每晚1次, bbox=[480, 819, 621, 839]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[24]: text=30天, bbox=[645, 820, 670, 838]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[25]: text=2倍氯米松福莫特罗吸入气雾剂◆①, bbox=[243, 861, 437, 881]
2026-08-05 04:46:20,256 INFO     29 [qwen-vl-text] coord item[26]: text=1瓶2.0揿,吸入用药,一天2次, bbox=[480, 861, 638, 881]
2026-08-05 04:46:20,257 INFO     29 [qwen-vl-text] coord item[27]: text=30天, bbox=[662, 862, 687, 880]
2026-08-05 04:46:20,257 INFO     29 [qwen-vl-text] coord item[28]: text=备注:, bbox=[228, 902, 242, 919]
2026-08-05 04:46:20,257 INFO     29 [qwen-vl-text] page=1 — 29/29 coords, api_time=8.3s
2026-08-05 04:46:20,257 INFO     29 [qwen-vl-text] new_positions (29):
[[1, 298.90999999999997, 438.68199999999996, 13.09, 29.75], [1, 184.398, 231.54999999999998, 60.69, 73.185], [1, 184.398, 220.60399999999998, 88.655, 101.74499999999999], [1, 426.05199999999996, 474.046, 89.25, 101.74499999999999], [1, 369.638, 402.476, 118.405, 130.9], [1, 426.05199999999996, 437.84, 119.0, 130.9], [1, 479.09799999999996, 518.672, 119.0, 130.9], [1, 185.23999999999998, 321.644, 146.37, 158.86499999999998], [1, 362.902, 375.532, 146.37, 158.86499999999998], [1, 426.05199999999996, 584.348, 146.965, 158.86499999999998], [1, 184.398, 294.7, 174.33499999999998, 186.82999999999998], [1, 184.398, 254.284, 201.70499999999998, 214.2], [1, 184.398, 254.284, 228.48, 240.975], [1, 184.398, 254.284, 254.66, 267.155], [1, 184.398, 254.284, 281.435, 293.93], [1, 187.766, 243.338, 308.21, 320.11], [1, 187.766, 243.338, 334.98499999999996, 346.885], [1, 187.766, 243.338, 361.16499999999996, 373.065], [1, 187.766, 243.338, 387.34499999999997, 399.245], [1, 189.45, 243.338, 411.74, 423.64], [1, 247.548, 318.276, 437.325, 448.63], [1, 247.548, 266.914, 462.315, 473.62], [1, 205.44799999999998, 315.75, 487.30499999999995, 499.205], [1, 404.15999999999997, 522.882, 487.30499999999995, 499.205], [1, 543.09, 564.14, 487.9, 498.60999999999996], [1, 204.606, 367.954, 512.295, 524.1949999999999], [1, 404.15999999999997, 537.196, 512.295, 524.1949999999999], [1, 557.404, 578.454, 512.89, 523.6], [1, 191.976, 203.76399999999998, 536.6899999999999, 546.805]]
2026-08-05 04:46:20,257 INFO     29 [qwen-vl-text] ═══ DONE ═══ 29 positions, pages=1, time=11.1s
2026-08-05 04:46:20,257 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:46:20,257 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 04:46:20,258 INFO     29 [qwen-vl-text] positions(56): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:46:20,258 INFO     29 [qwen-vl-text] page grouping: [2, 3], lines per page: [22, 34]
2026-08-05 04:46:20,623 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 04:46:20,874 INFO     29 [qwen-vl-text] page=3, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 04:46:20,875 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1748
2026-08-05 04:46:20,875 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:46:20,875 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 70, \"bbox_end\": 125, \"encounter_dates\": [\"2025-12-12\"], \"department\": \"内科门诊(荔湾)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门(急)诊病历信息\n就诊卡号\n流水\n姓名\n性别:男\n年\n龄:65岁\n就诊科室:内科门诊(荔湾)\n病历编号:\n就诊时间:2025-12-12 09:26:46\n主诉:BAIYUN V8\n现病史:自上次访视至今,询问及查询HIS系统受试者无新增AE、SAE、哮喘急性发作,有新增合并用药。发生过2次医疗相关事件,就诊于荔湾区逢源街道社区中心1次,就诊于专科门诊1次。期间未收到ePRO触发的哮喘警报邮件。\n完成下流操作:\n1、静坐10分钟后,测量坐位生命体征,血压:120/76mmHg,脉搏频率:59次/分(NCS),呼吸:20次/分,体温:36.5℃;\n2、9:20体格检查:神志清,体置合作,自主体位,一般外表无异常,皮肤、粘膜无异常,唇甲无发绀,眼睛、耳、鼻、咽喉无异常,口咽部粘膜无异常,颈软,气管居中,甲状腺未及肿大,全身浅表淋巴结未及肿大,颈静脉无怒张,胸廓无畸形,双肺呼吸运动对称,双肺触觉语颤正常,双肺叩诊清音,双肺呼吸音清,未闻及啰音。心前区无隆起,心尖搏动无弥散,心界不大,心率:59次/分,律齐,各瓣膜听诊区未闻及病理性杂音。腹平软,全腹无压痛、反跳痛。肝、脾肋下未及,肝肾区无叩击痛,肠鸣音存,4次/分,脊柱、四肢无畸形,生理征存,未引出病理征,其他系统未见明显异常。\n3、查看受试者电子日志,受试者漏填2025年10月26日(早间日志)、8月23日、9月10日、9月19日、9月24日、10月5日、10月25日、11月3日、12月2日(晚间日志)。\n4、填写AQLQ+12和ACQ-5问卷,ACQ-5评分:1.0分。\n5、休息至少10分钟后,行12导联ECG检查。\n6、10:42采集中心实验室样本(血常规、血生化)并送往中心实验室。\n7、回收试验药物BDA MDI AS MDI 3盒(137968-KF未开封、102035-IM未用74喷,实际已用:24喷,发药当天预喷4喷,2025.8.18-2025.9.10期间因超过7天未使用试验药物预喷1次共2喷,2025.9.10-11.19期间每七天清洗装置后预喷10次共20喷,总计预喷26喷;199863-TA未用106喷,实际已用:8喷,2025.11.20当天预喷4喷,2025.11.20-2025.12.12期间每七天清洗装置后预喷3次共6喷,总计预喷10喷)ePro记录使用总共32喷,与实际使用情况一致。\nCS 扫描全能王\n3亿人都在用的扫描App\n门诊病历\n25/10/21 16时 门诊病历\n25/11/19 11时 门诊病历（GCP专用）\n25/12/12 09时 门诊病历（GCP专用）\n1、颈痛综合征:开始时间:2025年1月8日,持续中,中度,非SAE,与试验药物无关,对试验\n药物采取措施:剂量无需改变,未因该AE退出研究,采取理疗。\n2、功能性消化不良:开始时间:2025年5月20日,持续中,中度,非SAE,与试验药物无\n关,对试验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:药物治疗。\n病因:无诱因,症状:下腹痛,进食后明显,休息后可缓解。\n3、慢性胃炎:开始时间:2025年3月2日,持续中,中度,非SAE,与试验药物无关,对试\n验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:暂无治疗措施。\n跟踪合并用药\n1、糠酸莫米松鼻喷雾剂 2024.7.19-2025.9.26 每日每早一粒 喷鼻 必要时 治疗过敏\n性鼻炎。\n2、盐酸二甲双胍片 2024.10.10-2025.9.14 0.5 TID 治疗2型糖尿病。\n3、达格列净片 2025.9.15至今 10mg qd 治疗2型糖尿病。\n补充合并用药:1、硫酸特布他林雾化吸入用溶液 2025.6.17-2025.6.19 5mg 吸\n入 qd 治疗急性支气管炎。\n预约下次安全性电话随访时间。\n既往史:\n过敏史:\n个人史:\n体格检查:\n专科情况:\n辅助检查:\n治疗项目:\n门诊诊断:\n1、支气管哮喘\n处置:\n心电图(心电图室做)\n伯氟米松福莫特罗吸入气雾剂① 1瓶2.0瓶,吸入用药,一天2次 30天\n孟鲁司特钠片(省采)① 6盒10.0mg,口服,每日1次(口服) 30天\n备注:\n医生:",
    "role": "user"
  }
]
[92m04:46:20 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:46:20,876 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:46:20,877 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:46:20.876+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 10, "failed": 0, "current": {"333155a8908811f1a3da71efcdd7cc1f": {"id": "333155a8908811f1a3da71efcdd7cc1f", "doc_id": "32f80906908811f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412392, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905007404, "task_type": "dataflow", "root_trace_id": "8cc21299ba8c4c4f9376bb5b55f5585f", "root_traceparent": "00-8cc21299ba8c4c4f9376bb5b55f5585f-3809269866d439b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:46:37,168 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:46:37,168 INFO     29 [qwen-vl-text] LLM output (len=1607):
{
  "encounter_date": "2025-12-12",
  "chief_complaint": "BAIYUN V8",
  "present_illness": "自上次访视至今,询问及查询HIS系统受试者无新增AE、SAE、哮喘急性发作,有新增合并用药。发生过2次医疗相关事件,就诊于荔湾区逢源街道社区中心1次,就诊于专科门诊1次。期间未收到ePRO触发的哮喘警报邮件。静坐10分钟后,测量坐位生命体征,血压:120/76mmHg,脉搏频率:59次/分(NCS),呼吸:20次/分,体温:36.5℃。体格检查:神志清,体置合作,自主体位,一般外表无异常,皮肤、粘膜无异常,唇甲无发绀,眼睛、耳、鼻、咽喉无异常,口咽部粘膜无异常,颈软,气管居中,甲状腺未及肿大,全身浅表淋巴结未及肿大,颈静脉无怒张,胸廓无畸形,双肺呼吸运动对称,双肺触觉语颤正常,双肺叩诊清音,双肺呼吸音清,未闻及啰音。心前区无隆起,心尖搏动无弥散,心界不大,心率:59次/分,律齐,各瓣膜听诊区未闻及病理性杂音。腹平软,全腹无压痛、反跳痛。肝、脾肋下未及,肝肾区无叩击痛,肠鸣音存,4次/分,脊柱、四肢无畸形,生理征存,未引出病理征,其他系统未见明显异常。查看受试者电子日志,受试者漏填2025年10月26日(早间日志)、8月23日、9月10日、9月19日、9月24日、10月5日、10月25日、11月3日、12月2日(晚间日志)。填写AQLQ+12和ACQ-5问卷,ACQ-5评分:1.0分。休息至少10分钟后,行12导联ECG检查。10:42采集中心实验室样本(血常规、血生化)并送往中心实验室。回收试验药物BDA MDI AS MDI 3盒(137968-KF未开封、102035-IM未用74喷,实际已用:24喷,发药当天预喷4喷,2025.8.18-2025.9.10期间因超过7天未使用试验药物预喷1次共2喷,2025.9.10-11.19期间每七天清洗装置后预喷10次共20喷,总计预喷26喷;199863-TA未用106喷,实际已用:8喷,2025.11.20当天预喷4喷,2025.11.20-2025.12.12期间每七天清洗装置后预喷3次共6喷,总计预喷10喷)ePro记录使用总共32喷,与实际使用情况一致。颈痛综合征:开始时间:2025年1月8日,持续中,中度,非SAE,与试验药物无关,对试验药物采取措施:剂量无需改变,未因该AE退出研究,采取理疗。功能性消化不良:开始时间:2025年5月20日,持续中,中度,非SAE,与试验药物无关,对试验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:药物治疗。病因:无诱因,症状:下腹痛,进食后明显,休息后可缓解。慢性胃炎:开始时间:2025年3月2日,持续中,中度,非SAE,与试验药物无关,对试验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:暂无治疗措施。跟踪合并用药:1、糠酸莫米松鼻喷雾剂 2024.7.19-2025.9.26 每日每早一粒 喷鼻 必要时 治疗过敏性鼻炎。2、盐酸二甲双胍片 2024.10.10-2025.9.14 0.5 TID 治疗2型糖尿病。3、达格列净片 2025.9.15至今 10mg qd 治疗2型糖尿病。补充合并用药:1、硫酸特布他林雾化吸入用溶液 2025.6.17-2025.6.19 5mg 吸入 qd 治疗急性支气管炎。预约下次安全性电话随访时间。",
  "past_history": null,
  "diagnosis": "支气管哮喘",
  "treatment_plan": "心电图(心电图室做); 伯氟米松福莫特罗吸入气雾剂① 1瓶2.0瓶,吸入用药,一天2次 30天; 孟鲁司特钠片(省采)① 6盒10.0mg,口服,每日1次(口服) 30天"
}
2026-08-05 04:46:37,168 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-12]
2026-08-05 04:46:37,173 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2948002, prompt_len=1699
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["门(急)诊病历信息", "就诊卡号", "流水", "姓名", "性别:男", "年", "龄:65岁", "就诊科室:内科门诊(荔湾)", "病历编号:", "就诊时间:2025-12-12 09:26:46", "主诉:BAIYUN V8", "现病史:自上次访视至今,询问及查询HIS系统受试者无新增AE、SAE、哮喘急性发作,有新增合并用药。发生过2次医疗相关事件,就诊于荔湾区逢源街道社区中心1次,就诊于专科门诊1次。期间未收到ePRO触发的哮喘警报邮件。", "完成下流操作:", "1、静坐10分钟后,测量坐位生命体征,血压:120/76mmHg,脉搏频率:59次/分(NCS),呼吸:20次/分,体温:36.5℃;", "2、9:20体格检查:神志清,体置合作,自主体位,一般外表无异常,皮肤、粘膜无异常,唇甲无发绀,眼睛、耳、鼻、咽喉无异常,口咽部粘膜无异常,颈软,气管居中,甲状腺未及肿大,全身浅表淋巴结未及肿大,颈静脉无怒张,胸廓无畸形,双肺呼吸运动对称,双肺触觉语颤正常,双肺叩诊清音,双肺呼吸音清,未闻及啰音。心前区无隆起,心尖搏动无弥散,心界不大,心率:59次/分,律齐,各瓣膜听诊区未闻及病理性杂音。腹平软,全腹无压痛、反跳痛。肝、脾肋下未及,肝肾区无叩击痛,肠鸣音存,4次/分,脊柱、四肢无畸形,生理征存,未引出病理征,其他系统未见明显异常。", "3、查看受试者电子日志,受试者漏填2025年10月26日(早间日志)、8月23日、9月10日、9月19日、9月24日、10月5日、10月25日、11月3日、12月2日(晚间日志)。", "4、填写AQLQ+12和ACQ-5问卷,ACQ-5评分:1.0分。", "5、休息至少10分钟后,行12导联ECG检查。", "6、10:42采集中心实验室样本(血常规、血生化)并送往中心实验室。", "7、回收试验药物BDA MDI AS MDI 3盒(137968-KF未开封、102035-IM未用74喷,实际已用:24喷,发药当天预喷4喷,2025.8.18-2025.9.10期间因超过7天未使用试验药物预喷1次共2喷,2025.9.10-11.19期间每七天清洗装置后预喷10次共20喷,总计预喷26喷;199863-TA未用106喷,实际已用:8喷,2025.11.20当天预喷4喷,2025.11.20-2025.12.12期间每七天清洗装置后预喷3次共6喷,总计预喷10喷)ePro记录使用总共32喷,与实际使用情况一致。", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-05 04:46:48,512 INFO     29 [qwen-vl-text] coord API raw response (len=1989):
[
	{"text": "门(急)诊病历信息", "bbox": [309, 73, 532, 94]},
	{"text": "就诊卡号", "bbox": [130, 127, 198, 142]},
	{"text": "流水", "bbox": [131, 158, 184, 174]},
	{"text": "姓名", "bbox": [131, 190, 148, 206]},
	{"text": "性别:男", "bbox": [407, 189, 471, 205]},
	{"text": "年", "bbox": [510, 190, 529, 205]},
	{"text": "龄:65岁", "bbox": [597, 190, 657, 205]},
	{"text": "就诊科室:内科门诊(荔湾)", "bbox": [131, 221, 343, 237]},
	{"text": "病历编号:", "bbox": [510, 157, 587, 173]},
	{"text": "就诊时间:2025-12-12 09:26:46", "bbox": [515, 221, 761, 236]},
	{"text": "主诉:BAIYUN V8", "bbox": [130, 253, 352, 269]},
	{"text": "现病史:自上次访视至今,询问及查询HIS系统受试者无新增AE、SAE、哮喘急性发作,有新增合并用药。发生过2次医疗相关事件,就诊于荔湾区逢源街道社区中心1次,就诊于专科门诊1次。期间未收到ePRO触发的哮喘警报邮件。", "bbox": [130, 283, 825, 340]},
	{"text": "完成下流操作:", "bbox": [130, 355, 245, 370]},
	{"text": "1、静坐10分钟后,测量坐位生命体征,血压:120/76mmHg,脉搏频率:59次/分(NCS),呼吸:20次/分,体温:36.5℃;", "bbox": [131, 385, 825, 422]},
	{"text": "2、9:20体格检查:神志清,体置合作,自主体位,一般外表无异常,皮肤、粘膜无异常,唇甲无发绀,眼睛、耳、鼻、咽喉无异常,口咽部粘膜无异常,颈软,气管居中,甲状腺未及肿大,全身浅表淋巴结未及肿大,颈静脉无怒张,胸廓无畸形,双肺呼吸运动对称,双肺触觉语颤正常,双肺叩诊清音,双肺呼吸音清,未闻及啰音。心前区无隆起,心尖搏动无弥散,心界不大,心率:59次/分,律齐,各瓣膜听诊区未闻及病理性杂音。腹平软,全腹无压痛、反跳痛。肝、脾肋下未及,肝肾区无叩击痛,肠鸣音存,4次/分,脊柱、四肢无畸形,生理征存,未引出病理征,其他系统未见明显异常。", "bbox": [131, 436, 823, 574]},
	{"text": "3、查看受试者电子日志,受试者漏填2025年10月26日(早间日志)、8月23日、9月10日、9月19日、9月24日、10月5日、10月25日、11月3日、12月2日(晚间日志)。", "bbox": [135, 588, 794, 645]},
	{"text": "4、填写AQLQ+12和ACQ-5问卷,ACQ-5评分:1.0分。", "bbox": [135, 659, 515, 675]},
	{"text": "5、休息至少10分钟后,行12导联ECG检查。", "bbox": [135, 689, 457, 705]},
	{"text": "6、10:42采集中心实验室样本(血常规、血生化)并送往中心实验室。", "bbox": [135, 720, 658, 736]},
	{"text": "7、回收试验药物BDA MDI&AS MDI 3盒(137968-KF未开封、102035-IM未用74喷,实际已用:24喷,发药当天预喷4喷,2025.8.18-2025.9.10期间因超过7天未使用试验药物预喷1次共2喷,2025.9.10-11.19期间每七天清洗装置后预喷10次共20喷,总计预喷26喷;199863-TA未用106喷,实际已用:8喷,2025.11.20当天预喷4喷,2025.11.20-2025.12.12期间每七天清洗装置后预喷3次共6喷,总计预喷10喷)ePro记录使用总共32喷,与实际使用情况一致。", "bbox": [135, 749, 809, 862]},
	{"text": "CS 扫描全能王", "bbox": [861, 958, 977, 974]},
	{"text": "3亿人都在用的扫描App", "bbox": [861, 977, 977, 987]}
]
2026-08-05 04:46:48,512 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=11.3s
2026-08-05 04:46:48,512 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊病历信息, bbox=[309, 73, 532, 94]
2026-08-05 04:46:48,513 INFO     29 [qwen-vl-text] coord item[1]: text=就诊卡号, bbox=[130, 127, 198, 142]
2026-08-05 04:46:48,513 INFO     29 [qwen-vl-text] coord item[2]: text=流水, bbox=[131, 158, 184, 174]
2026-08-05 04:46:48,513 INFO     29 [qwen-vl-text] coord item[3]: text=姓名, bbox=[131, 190, 148, 206]
2026-08-05 04:46:48,513 INFO     29 [qwen-vl-text] coord item[4]: text=性别:男, bbox=[407, 189, 471, 205]
2026-08-05 04:46:48,513 INFO     29 [qwen-vl-text] coord item[5]: text=年, bbox=[510, 190, 529, 205]
2026-08-05 04:46:48,513 INFO     29 [qwen-vl-text] coord item[6]: text=龄:65岁, bbox=[597, 190, 657, 205]
2026-08-05 04:46:48,513 INFO     29 [qwen-vl-text] coord item[7]: text=就诊科室:内科门诊(荔湾), bbox=[131, 221, 343, 237]
2026-08-05 04:46:48,513 INFO     29 [qwen-vl-text] coord item[8]: text=病历编号:, bbox=[510, 157, 587, 173]
2026-08-05 04:46:48,513 INFO     29 [qwen-vl-text] coord item[9]: text=就诊时间:2025-12-12 09:26:46, bbox=[515, 221, 761, 236]
2026-08-05 04:46:48,513 INFO     29 [qwen-vl-text] coord item[10]: text=主诉:BAIYUN V8, bbox=[130, 253, 352, 269]
2026-08-05 04:46:48,513 INFO     29 [qwen-vl-text] coord item[11]: text=现病史:自上次访视至今,询问及查询HIS系统受试者无新增AE、SAE、哮喘急性发作,有新增合并用药。发生过2次医疗相关事件,就诊于荔湾区逢源街道社区中心1次,就诊于专科门诊1次。期间未收到ePRO触发的哮喘警报邮件。, bbox=[130, 283, 825, 340]
2026-08-05 04:46:48,513 INFO     29 [qwen-vl-text] coord item[12]: text=完成下流操作:, bbox=[130, 355, 245, 370]
2026-08-05 04:46:48,513 INFO     29 [qwen-vl-text] coord item[13]: text=1、静坐10分钟后,测量坐位生命体征,血压:120/76mmHg,脉搏频率:59次/分(NCS),呼吸:20次/分,体温:36.5℃;, bbox=[131, 385, 825, 422]
2026-08-05 04:46:48,513 INFO     29 [qwen-vl-text] coord item[14]: text=2、9:20体格检查:神志清,体置合作,自主体位,一般外表无异常,皮肤、粘膜无异常,唇甲无发绀,眼睛、耳、鼻、咽喉无异常,口咽部粘膜无异常,颈软,气管居中,甲状腺未及肿大,全身浅表淋巴结未及肿大,颈静脉无怒张,胸廓无畸形,双肺呼吸运动对称,双肺触觉语颤正常,双肺叩诊清音,双肺呼吸音清,未闻及啰音。心前区无隆起,心尖搏动无弥散,心界不大,心率:59次/分,律齐,各瓣膜听诊区未闻及病理性杂音。腹平软,全腹无压痛、反跳痛。肝、脾肋下未及,肝肾区无叩击痛,肠鸣音存,4次/分,脊柱、四肢无畸形,生理征存,未引出病理征,其他系统未见明显异常。, bbox=[131, 436, 823, 574]
2026-08-05 04:46:48,514 INFO     29 [qwen-vl-text] coord item[15]: text=3、查看受试者电子日志,受试者漏填2025年10月26日(早间日志)、8月23日、9月10日、9月19日、9月24日、10月5日、10月25日、11月3日、12月2日(晚间日志)。, bbox=[135, 588, 794, 645]
2026-08-05 04:46:48,514 INFO     29 [qwen-vl-text] coord item[16]: text=4、填写AQLQ+12和ACQ-5问卷,ACQ-5评分:1.0分。, bbox=[135, 659, 515, 675]
2026-08-05 04:46:48,514 INFO     29 [qwen-vl-text] coord item[17]: text=5、休息至少10分钟后,行12导联ECG检查。, bbox=[135, 689, 457, 705]
2026-08-05 04:46:48,514 INFO     29 [qwen-vl-text] coord item[18]: text=6、10:42采集中心实验室样本(血常规、血生化)并送往中心实验室。, bbox=[135, 720, 658, 736]
2026-08-05 04:46:48,514 INFO     29 [qwen-vl-text] coord item[19]: text=7、回收试验药物BDA MDI&AS MDI 3盒(137968-KF未开封、102035-IM未用74喷,实际已用:24喷,发药当天预喷4喷,2025.8.18-2025.9.10期间因超过7天未使用试验药物预喷1次共2喷,2025.9.10-11.19期间每七天清洗装置后预喷10次共20喷,总计预喷26喷;199863-TA未用106喷,实际已用:8喷,2025.11.20当天预喷4喷,2025.11.20-2025.12.12期间每七天清洗装置后预喷3次共6喷,总计预喷10喷)ePro记录使用总共32喷,与实际使用情况一致。, bbox=[135, 749, 809, 862]
2026-08-05 04:46:48,514 INFO     29 [qwen-vl-text] coord item[20]: text=CS 扫描全能王, bbox=[861, 958, 977, 974]
2026-08-05 04:46:48,514 INFO     29 [qwen-vl-text] coord item[21]: text=3亿人都在用的扫描App, bbox=[861, 977, 977, 987]
2026-08-05 04:46:48,515 INFO     29 [qwen-vl-text] page=2 — 22/22 coords, api_time=11.3s
2026-08-05 04:46:48,521 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2854201, prompt_len=1442
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共34行）
["门诊病历", "25/10/21 16时 门诊病历", "25/11/19 11时 门诊病历（GCP专用）", "25/12/12 09时 门诊病历（GCP专用）", "1、颈痛综合征:开始时间:2025年1月8日,持续中,中度,非SAE,与试验药物无关,对试验", "药物采取措施:剂量无需改变,未因该AE退出研究,采取理疗。", "2、功能性消化不良:开始时间:2025年5月20日,持续中,中度,非SAE,与试验药物无", "关,对试验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:药物治疗。", "病因:无诱因,症状:下腹痛,进食后明显,休息后可缓解。", "3、慢性胃炎:开始时间:2025年3月2日,持续中,中度,非SAE,与试验药物无关,对试", "验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:暂无治疗措施。", "跟踪合并用药", "1、糠酸莫米松鼻喷雾剂 2024.7.19-2025.9.26 每日每早一粒 喷鼻 必要时 治疗过敏", "性鼻炎。", "2、盐酸二甲双胍片 2024.10.10-2025.9.14 0.5 TID 治疗2型糖尿病。", "3、达格列净片 2025.9.15至今 10mg qd 治疗2型糖尿病。", "补充合并用药:1、硫酸特布他林雾化吸入用溶液 2025.6.17-2025.6.19 5mg 吸", "入 qd 治疗急性支气管炎。", "预约下次安全性电话随访时间。", "既往史:", "过敏史:", "个人史:", "体格检查:", "专科情况:", "辅助检查:", "治疗项目:", "门诊诊断:", "1、支气管哮喘", "处置:", "心电图(心电图室做)", "伯氟米松福莫特罗吸入气雾剂① 1瓶2.0瓶,吸入用药,一天2次 30天", "孟鲁司特钠片(省采)① 6盒10.0mg,口服,每日1次(口服) 30天", "备注:", "医生:"]

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
2026-08-05 04:47:00,224 INFO     29 [qwen-vl-text] coord API raw response (len=2218):
[
	{"text": "门诊病历", "bbox": [15, 86, 60, 104]},
	{"text": "25/10/21 16时 门诊病历", "bbox": [15, 134, 123, 150]},
	{"text": "25/11/19 11时 门诊病历（GCP专用）", "bbox": [15, 182, 175, 198]},
	{"text": "25/12/12 09时 门诊病历（GCP专用）", "bbox": [15, 231, 177, 248]},
	{"text": "1、颈痛综合征:开始时间:2025年1月8日,持续中,中度,非SAE,与试验药物无关,对试验", "bbox": [624, 82, 952, 97]},
	{"text": "药物采取措施:剂量无需改变,未因该AE退出研究,采取理疗。", "bbox": [624, 101, 848, 116]},
	{"text": "2、功能性消化不良:开始时间:2025年5月20日,持续中,中度,非SAE,与试验药物无", "bbox": [624, 130, 939, 145]},
	{"text": "关,对试验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:药物治疗。", "bbox": [624, 149, 948, 164]},
	{"text": "病因:无诱因,症状:下腹痛,进食后明显,休息后可缓解。", "bbox": [624, 169, 844, 184]},
	{"text": "3、慢性胃炎:开始时间:2025年3月2日,持续中,中度,非SAE,与试验药物无关,对试", "bbox": [624, 198, 948, 213]},
	{"text": "验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:暂无治疗措施。", "bbox": [624, 217, 931, 232]},
	{"text": "跟踪合并用药", "bbox": [624, 247, 674, 261]},
	{"text": "1、糠酸莫米松鼻喷雾剂 2024.7.19-2025.9.26 每日每早一粒 喷鼻 必要时 治疗过敏", "bbox": [624, 276, 951, 291]},
	{"text": "性鼻炎。", "bbox": [624, 296, 654, 310]},
	{"text": "2、盐酸二甲双胍片 2024.10.10-2025.9.14 0.5 TID 治疗2型糖尿病。", "bbox": [624, 325, 891, 340]},
	{"text": "3、达格列净片 2025.9.15至今 10mg qd 治疗2型糖尿病。", "bbox": [624, 355, 847, 370]},
	{"text": "补充合并用药:1、硫酸特布他林雾化吸入用溶液 2025.6.17-2025.6.19 5mg 吸", "bbox": [624, 383, 923, 398]},
	{"text": "入 qd 治疗急性支气管炎。", "bbox": [624, 402, 727, 417]},
	{"text": "预约下次安全性电话随访时间。", "bbox": [624, 431, 735, 446]},
	{"text": "既往史:", "bbox": [624, 459, 673, 474]},
	{"text": "过敏史:", "bbox": [624, 488, 673, 503]},
	{"text": "个人史:", "bbox": [624, 517, 673, 532]},
	{"text": "体格检查:", "bbox": [624, 546, 664, 561]},
	{"text": "专科情况:", "bbox": [624, 575, 664, 590]},
	{"text": "辅助检查:", "bbox": [624, 604, 664, 619]},
	{"text": "治疗项目:", "bbox": [624, 633, 664, 648]},
	{"text": "门诊诊断:", "bbox": [624, 662, 664, 677]},
	{"text": "1、支气管哮喘", "bbox": [668, 692, 720, 707]},
	{"text": "处置:", "bbox": [624, 720, 682, 735]},
	{"text": "心电图(心电图室做)", "bbox": [643, 750, 719, 765]},
	{"text": "伯氟米松福莫特罗吸入气雾剂① 1瓶2.0瓶,吸入用药,一天2次 30天", "bbox": [643, 778, 916, 793]},
	{"text": "孟鲁司特钠片(省采)① 6盒10.0mg,口服,每日1次(口服) 30天", "bbox": [643, 807, 927, 822]},
	{"text": "备注:", "bbox": [624, 837, 679, 852]},
	{"text": "医生:", "bbox": [653, 870, 674, 885]}
]
2026-08-05 04:47:00,224 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=11.7s
2026-08-05 04:47:00,224 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[15, 86, 60, 104]
2026-08-05 04:47:00,224 INFO     29 [qwen-vl-text] coord item[1]: text=25/10/21 16时 门诊病历, bbox=[15, 134, 123, 150]
2026-08-05 04:47:00,224 INFO     29 [qwen-vl-text] coord item[2]: text=25/11/19 11时 门诊病历（GCP专用）, bbox=[15, 182, 175, 198]
2026-08-05 04:47:00,224 INFO     29 [qwen-vl-text] coord item[3]: text=25/12/12 09时 门诊病历（GCP专用）, bbox=[15, 231, 177, 248]
2026-08-05 04:47:00,224 INFO     29 [qwen-vl-text] coord item[4]: text=1、颈痛综合征:开始时间:2025年1月8日,持续中,中度,非SAE,与试验药物无关,对试验, bbox=[624, 82, 952, 97]
2026-08-05 04:47:00,224 INFO     29 [qwen-vl-text] coord item[5]: text=药物采取措施:剂量无需改变,未因该AE退出研究,采取理疗。, bbox=[624, 101, 848, 116]
2026-08-05 04:47:00,224 INFO     29 [qwen-vl-text] coord item[6]: text=2、功能性消化不良:开始时间:2025年5月20日,持续中,中度,非SAE,与试验药物无, bbox=[624, 130, 939, 145]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[7]: text=关,对试验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:药物治疗。, bbox=[624, 149, 948, 164]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[8]: text=病因:无诱因,症状:下腹痛,进食后明显,休息后可缓解。, bbox=[624, 169, 844, 184]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[9]: text=3、慢性胃炎:开始时间:2025年3月2日,持续中,中度,非SAE,与试验药物无关,对试, bbox=[624, 198, 948, 213]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[10]: text=验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:暂无治疗措施。, bbox=[624, 217, 931, 232]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[11]: text=跟踪合并用药, bbox=[624, 247, 674, 261]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[12]: text=1、糠酸莫米松鼻喷雾剂 2024.7.19-2025.9.26 每日每早一粒 喷鼻 必要时 治疗过敏, bbox=[624, 276, 951, 291]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[13]: text=性鼻炎。, bbox=[624, 296, 654, 310]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[14]: text=2、盐酸二甲双胍片 2024.10.10-2025.9.14 0.5 TID 治疗2型糖尿病。, bbox=[624, 325, 891, 340]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[15]: text=3、达格列净片 2025.9.15至今 10mg qd 治疗2型糖尿病。, bbox=[624, 355, 847, 370]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[16]: text=补充合并用药:1、硫酸特布他林雾化吸入用溶液 2025.6.17-2025.6.19 5mg 吸, bbox=[624, 383, 923, 398]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[17]: text=入 qd 治疗急性支气管炎。, bbox=[624, 402, 727, 417]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[18]: text=预约下次安全性电话随访时间。, bbox=[624, 431, 735, 446]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[19]: text=既往史:, bbox=[624, 459, 673, 474]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[20]: text=过敏史:, bbox=[624, 488, 673, 503]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[21]: text=个人史:, bbox=[624, 517, 673, 532]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[22]: text=体格检查:, bbox=[624, 546, 664, 561]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[23]: text=专科情况:, bbox=[624, 575, 664, 590]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[24]: text=辅助检查:, bbox=[624, 604, 664, 619]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[25]: text=治疗项目:, bbox=[624, 633, 664, 648]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[26]: text=门诊诊断:, bbox=[624, 662, 664, 677]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[27]: text=1、支气管哮喘, bbox=[668, 692, 720, 707]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[28]: text=处置:, bbox=[624, 720, 682, 735]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[29]: text=心电图(心电图室做), bbox=[643, 750, 719, 765]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[30]: text=伯氟米松福莫特罗吸入气雾剂① 1瓶2.0瓶,吸入用药,一天2次 30天, bbox=[643, 778, 916, 793]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[31]: text=孟鲁司特钠片(省采)① 6盒10.0mg,口服,每日1次(口服) 30天, bbox=[643, 807, 927, 822]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[32]: text=备注:, bbox=[624, 837, 679, 852]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] coord item[33]: text=医生:, bbox=[653, 870, 674, 885]
2026-08-05 04:47:00,225 INFO     29 [qwen-vl-text] page=3 — 34/34 coords, api_time=11.7s
2026-08-05 04:47:00,226 INFO     29 [qwen-vl-text] new_positions (56):
[[2, 183.855, 316.53999999999996, 61.466, 79.148], [2, 77.35, 117.80999999999999, 106.934, 119.564], [2, 77.945, 109.47999999999999, 133.036, 146.50799999999998], [2, 77.945, 88.06, 159.98, 173.452], [2, 242.165, 280.245, 159.138, 172.60999999999999], [2, 303.45, 314.755, 159.98, 172.60999999999999], [2, 355.215, 390.91499999999996, 159.98, 172.60999999999999], [2, 77.945, 204.08499999999998, 186.082, 199.554], [2, 303.45, 349.265, 132.194, 145.666], [2, 306.425, 452.79499999999996, 186.082, 198.712], [2, 77.35, 209.44, 213.02599999999998, 226.498], [2, 77.35, 490.875, 238.286, 286.28], [2, 77.35, 145.775, 298.90999999999997, 311.53999999999996], [2, 77.945, 490.875, 324.17, 355.324], [2, 77.945, 489.685, 367.11199999999997, 483.308], [2, 80.325, 472.43, 495.096, 543.09], [2, 80.325, 306.425, 554.8779999999999, 568.35], [2, 80.325, 271.91499999999996, 580.138, 593.61], [2, 80.325, 391.51, 606.24, 619.712], [2, 80.325, 481.35499999999996, 630.658, 725.804], [2, 512.295, 581.3149999999999, 806.636, 820.108], [2, 512.295, 581.3149999999999, 822.634, 831.054], [3, 12.629999999999999, 50.519999999999996, 51.169999999999995, 61.879999999999995], [3, 12.629999999999999, 103.566, 79.72999999999999, 89.25], [3, 12.629999999999999, 147.35, 108.28999999999999, 117.80999999999999], [3, 12.629999999999999, 149.034, 137.445, 147.56], [3, 525.408, 801.584, 48.79, 57.714999999999996], [3, 525.408, 714.016, 60.095, 69.02], [3, 525.408, 790.6379999999999, 77.35, 86.27499999999999], [3, 525.408, 798.216, 88.655, 97.58], [3, 525.408, 710.648, 100.55499999999999, 109.47999999999999], [3, 525.408, 798.216, 117.80999999999999, 126.735], [3, 525.408, 783.9019999999999, 129.11499999999998, 138.04], [3, 525.408, 567.5079999999999, 146.965, 155.295], [3, 525.408, 800.742, 164.22, 173.14499999999998], [3, 525.408, 550.668, 176.12, 184.45], [3, 525.408, 750.222, 193.375, 202.29999999999998], [3, 525.408, 713.174, 211.225, 220.14999999999998], [3, 525.408, 777.1659999999999, 227.885, 236.81], [3, 525.408, 612.134, 239.19, 248.11499999999998], [3, 525.408, 618.87, 256.445, 265.37], [3, 525.408, 566.6659999999999, 273.10499999999996, 282.03], [3, 525.408, 566.6659999999999, 290.36, 299.28499999999997], [3, 525.408, 566.6659999999999, 307.615, 316.53999999999996], [3, 525.408, 559.088, 324.87, 333.79499999999996], [3, 525.408, 559.088, 342.125, 351.05], [3, 525.408, 559.088, 359.38, 368.305], [3, 525.408, 559.088, 376.635, 385.56], [3, 525.408, 559.088, 393.89, 402.815], [3, 562.456, 606.24, 411.74, 420.66499999999996], [3, 525.408, 574.244, 428.4, 437.325], [3, 541.406, 605.398, 446.25, 455.17499999999995], [3, 541.406, 771.2719999999999, 462.90999999999997, 471.835], [3, 541.406, 780.534, 480.16499999999996, 489.09], [3, 525.408, 571.718, 498.015, 506.94], [3, 549.826, 567.5079999999999, 517.65, 526.5749999999999]]
2026-08-05 04:47:00,226 INFO     29 [qwen-vl-text] ═══ DONE ═══ 56 positions, pages=2, time=40.0s
2026-08-05 04:47:00,226 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:47:00,226 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 04:47:00,226 INFO     29 [qwen-vl-text] positions(30): [[16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:47:00,226 INFO     29 [qwen-vl-text] page grouping: [16], lines per page: [30]
2026-08-05 04:47:00,561 INFO     29 [qwen-vl-text] page=16, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 04:47:00,562 INFO     29 [qwen-vl-text] LLM extraction start, text_len=851
2026-08-05 04:47:00,562 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:47:00,562 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 550, \"bbox_end\": 579, \"encounter_dates\": [\"2026-02-04\"], \"department\": \"内科门诊（基础）\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "病历编号：\n姓名：\n性别：男\n年龄：65岁\n就诊科室：内科门诊（基础）\n医生：\n就诊时间：2026-02-04 11:23:30\n主诉：支气管哮喘治疗后复诊\n现病史：2022年3月前开始出现咳嗽、咳痰，粘白，量少，能咯出，咳嗽呈阵发性，偶则激性，伴轻度咽痒，无气促，夜间有喘息、胸闷，伴鼻塞、流涕、喉咙，无咽痛，\n无反酸、嗳气、腹胀，无上腹部隐痛不适感，无伴发热、畏寒，曾自服肺力咳症状未见缓解，现病情好转、稳定，本次门诊距上次门诊间隔时间7天；过去4周，症状控制情况：控制良好，吸入药物使用情况：遵医嘱使用；，吸入装置使用情况：有，正确；急性发作情况：\n两次就诊期间急性发作：发作次数：0次，长期规律使用倍氯米松福莫特罗吸入气雾剂治疗。\n既往史：鼻炎病史，有糖尿病史\n过敏史：未发现\n个人史：否认遗传病史，吸烟30年，6支/日，已戒烟8年，饮酒6年，1两/日。\n体格检查：神志清，口腔无溃疡、粘膜白斑，肺部听诊，鼻塞，通气，气管居中，双肺呼吸音稍减弱，未闻及明显干湿性罗音。\n专科情况：\n辅助检查：血常规：Q-CRP：0.54mg/l 白细胞：5.5*109/L 中性粒细胞：\n5.17*109/L 60.5% 淋巴细胞：2.23*109/L 26.2% 单个核细胞：\n0.46*109/L 5.4% 嗜酸性粒细胞：0.6*109/L 7.1% 呼出气一氧化\n氮：FeNO50：130ppb FnNO10：161ppb 肺功能：轻度阻塞性通气功能障碍，支气管激发\n试验阳性（PD20=0.312mg AHI：轻度），胸片：心、肺、膈未见异常\n治疗项目：\n门诊诊断：\n1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、2型糖尿病\n单 种：\n发病时间：\n处 置：请仔细阅读药品说明书等文书资料，遵嘱治疗，不适随诊。\n倍氯米松福莫特罗吸入气雾剂◆① 1瓶2.0瓶，吸入用药，一天2次 30天\n孟鲁司特钠片（省采）◆ 6盒10.0mg，口服，每日1次（口服） 30天\n备 注：建议在停药附近社区医疗机构随访。",
    "role": "user"
  }
]
[92m04:47:00 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:47:00,563 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:47:00,564 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:47:00.562+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 10, "failed": 0, "current": {"333155a8908811f1a3da71efcdd7cc1f": {"id": "333155a8908811f1a3da71efcdd7cc1f", "doc_id": "32f80906908811f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412392, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905007404, "task_type": "dataflow", "root_trace_id": "8cc21299ba8c4c4f9376bb5b55f5585f", "root_traceparent": "00-8cc21299ba8c4c4f9376bb5b55f5585f-3809269866d439b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:47:06,280 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:47:06,280 INFO     29 [qwen-vl-text] LLM output (len=521):
{
  "encounter_date": "2026-02-04",
  "chief_complaint": "支气管哮喘治疗后复诊",
  "present_illness": "2022年3月前开始出现咳嗽、咳痰，粘白，量少，能咯出，咳嗽呈阵发性，偶则激性，伴轻度咽痒，无气促，夜间有喘息、胸闷，伴鼻塞、流涕、喉咙，无咽痛，无反酸、嗳气、腹胀，无上腹部隐痛不适感，无伴发热、畏寒，曾自服肺力咳症状未见缓解，现病情好转、稳定，本次门诊距上次门诊间隔时间7天；过去4周，症状控制情况：控制良好，吸入药物使用情况：遵医嘱使用；吸入装置使用情况：有，正确；急性发作情况：两次就诊期间急性发作：发作次数：0次，长期规律使用倍氯米松福莫特罗吸入气雾剂治疗。",
  "past_history": "鼻炎病史，有糖尿病史",
  "diagnosis": "1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、2型糖尿病",
  "treatment_plan": [
    "倍氯米松福莫特罗吸入气雾剂 1瓶2.0瓶，吸入用药，一天2次 30天",
    "孟鲁司特钠片（省采） 6盒10.0mg，口服，每日1次（口服） 30天"
  ]
}
2026-08-05 04:47:06,280 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-04]
2026-08-05 04:47:06,286 INFO     29 [qwen-vl-text] coord API call start, page=16, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3124705, prompt_len=1554
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共30行）
["病历编号：", "姓名：", "性别：男", "年龄：65岁", "就诊科室：内科门诊（基础）", "医生：", "就诊时间：2026-02-04 11:23:30", "主诉：支气管哮喘治疗后复诊", "现病史：2022年3月前开始出现咳嗽、咳痰，粘白，量少，能咯出，咳嗽呈阵发性，偶则激性，伴轻度咽痒，无气促，夜间有喘息、胸闷，伴鼻塞、流涕、喉咙，无咽痛，", "无反酸、嗳气、腹胀，无上腹部隐痛不适感，无伴发热、畏寒，曾自服肺力咳症状未见缓解，现病情好转、稳定，本次门诊距上次门诊间隔时间7天；过去4周，症状控制情况：控制良好，吸入药物使用情况：遵医嘱使用；，吸入装置使用情况：有，正确；急性发作情况：", "两次就诊期间急性发作：发作次数：0次，长期规律使用倍氯米松福莫特罗吸入气雾剂治疗。", "既往史：鼻炎病史，有糖尿病史", "过敏史：未发现", "个人史：否认遗传病史，吸烟30年，6支/日，已戒烟8年，饮酒6年，1两/日。", "体格检查：神志清，口腔无溃疡、粘膜白斑，肺部听诊，鼻塞，通气，气管居中，双肺呼吸音稍减弱，未闻及明显干湿性罗音。", "专科情况：", "辅助检查：血常规：Q-CRP：0.54mg/l 白细胞：5.5*109/L 中性粒细胞：", "5.17*109/L 60.5% 淋巴细胞：2.23*109/L 26.2% 单个核细胞：", "0.46*109/L 5.4% 嗜酸性粒细胞：0.6*109/L 7.1% 呼出气一氧化", "氮：FeNO50：130ppb FnNO10：161ppb 肺功能：轻度阻塞性通气功能障碍，支气管激发", "试验阳性（PD20=0.312mg AHI：轻度），胸片：心、肺、膈未见异常", "治疗项目：", "门诊诊断：", "1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、2型糖尿病", "单 种：", "发病时间：", "处 置：请仔细阅读药品说明书等文书资料，遵嘱治疗，不适随诊。", "倍氯米松福莫特罗吸入气雾剂◆① 1瓶2.0瓶，吸入用药，一天2次 30天", "孟鲁司特钠片（省采）◆ 6盒10.0mg，口服，每日1次（口服） 30天", "备 注：建议在停药附近社区医疗机构随访。"]

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
2026-08-05 04:47:18,089 INFO     29 [qwen-vl-text] coord API raw response (len=2166):
[
	{"text": "病历编号：", "bbox": [515, 50, 600, 66]},
	{"text": "姓名：", "bbox": [114, 84, 134, 99]},
	{"text": "性别：男", "bbox": [515, 84, 535, 99]},
	{"text": "年龄：65岁", "bbox": [607, 84, 678, 99]},
	{"text": "就诊科室：内科门诊（基础）", "bbox": [114, 117, 345, 133]},
	{"text": "医生：", "bbox": [408, 117, 442, 133]},
	{"text": "就诊时间：2026-02-04 11:23:30", "bbox": [515, 117, 808, 133]},
	{"text": "主诉：支气管哮喘治疗后复诊", "bbox": [114, 151, 450, 167]},
	{"text": "现病史：2022年3月前开始出现咳嗽、咳痰，粘白，量少，能咯出，咳嗽呈阵发性，偶则激性，伴轻度咽痒，无气促，夜间有喘息、胸闷，伴鼻塞、流涕、喉咙，无咽痛，", "bbox": [114, 185, 855, 218]},
	{"text": "无反酸、嗳气、腹胀，无上腹部隐痛不适感，无伴发热、畏寒，曾自服肺力咳症状未见缓解，现病情好转、稳定，本次门诊距上次门诊间隔时间7天；过去4周，症状控制情况：控制良好，吸入药物使用情况：遵医嘱使用；，吸入装置使用情况：有，正确；急性发作情况：", "bbox": [114, 227, 868, 290]},
	{"text": "两次就诊期间急性发作：发作次数：0次，长期规律使用倍氯米松福莫特罗吸入气雾剂治疗。", "bbox": [114, 293, 838, 331]},
	{"text": "既往史：鼻炎病史，有糖尿病史", "bbox": [114, 347, 428, 363]},
	{"text": "过敏史：未发现", "bbox": [114, 380, 297, 396]},
	{"text": "个人史：否认遗传病史，吸烟30年，6支/日，已戒烟8年，饮酒6年，1两/日。", "bbox": [114, 410, 797, 427]},
	{"text": "体格检查：神志清，口腔无溃疡、粘膜白斑，肺部听诊，鼻塞，通气，气管居中，双肺呼吸音稍减弱，未闻及明显干湿性罗音。", "bbox": [114, 444, 851, 481]},
	{"text": "专科情况：", "bbox": [114, 497, 205, 512]},
	{"text": "辅助检查：血常规：Q-CRP：0.54mg/l 白细胞：5.5*109/L 中性粒细胞：", "bbox": [114, 529, 748, 545]},
	{"text": "5.17*109/L 60.5% 淋巴细胞：2.23*109/L 26.2% 单个核细胞：", "bbox": [114, 551, 691, 567]},
	{"text": "0.46*109/L 5.4% 嗜酸性粒细胞：0.6*109/L 7.1% 呼出气一氧化", "bbox": [114, 573, 725, 589]},
	{"text": "氮：FeNO50：130ppb FnNO10：161ppb 肺功能：轻度阻塞性通气功能障碍，支气管激发", "bbox": [114, 594, 857, 610]},
	{"text": "试验阳性（PD20=0.312mg AHI：轻度），胸片：心、肺、膈未见异常", "bbox": [114, 616, 686, 632]},
	{"text": "治疗项目：", "bbox": [114, 648, 203, 663]},
	{"text": "门诊诊断：", "bbox": [114, 680, 203, 696]},
	{"text": "1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、2型糖尿病", "bbox": [140, 711, 625, 727]},
	{"text": "单 种：", "bbox": [114, 743, 221, 758]},
	{"text": "发病时间：", "bbox": [114, 773, 201, 789]},
	{"text": "处 置：请仔细阅读药品说明书等文书资料，遵嘱治疗，不适随诊。", "bbox": [114, 805, 720, 821]},
	{"text": "倍氯米松福莫特罗吸入气雾剂◆① 1瓶2.0瓶，吸入用药，一天2次 30天", "bbox": [158, 837, 778, 853]},
	{"text": "孟鲁司特钠片（省采）◆ 6盒10.0mg，口服，每日1次（口服） 30天", "bbox": [158, 867, 808, 883]},
	{"text": "备 注：建议在停药附近社区医疗机构随访。", "bbox": [114, 897, 537, 912]}
]
2026-08-05 04:47:18,090 INFO     29 [qwen-vl-text] coord API: raw_items=30, valid_items=30, elapsed=11.8s
2026-08-05 04:47:18,090 INFO     29 [qwen-vl-text] coord item[0]: text=病历编号：, bbox=[515, 50, 600, 66]
2026-08-05 04:47:18,090 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[114, 84, 134, 99]
2026-08-05 04:47:18,090 INFO     29 [qwen-vl-text] coord item[2]: text=性别：男, bbox=[515, 84, 535, 99]
2026-08-05 04:47:18,091 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：65岁, bbox=[607, 84, 678, 99]
2026-08-05 04:47:18,091 INFO     29 [qwen-vl-text] coord item[4]: text=就诊科室：内科门诊（基础）, bbox=[114, 117, 345, 133]
2026-08-05 04:47:18,092 INFO     29 [qwen-vl-text] coord item[5]: text=医生：, bbox=[408, 117, 442, 133]
2026-08-05 04:47:18,092 INFO     29 [qwen-vl-text] coord item[6]: text=就诊时间：2026-02-04 11:23:30, bbox=[515, 117, 808, 133]
2026-08-05 04:47:18,092 INFO     29 [qwen-vl-text] coord item[7]: text=主诉：支气管哮喘治疗后复诊, bbox=[114, 151, 450, 167]
2026-08-05 04:47:18,092 INFO     29 [qwen-vl-text] coord item[8]: text=现病史：2022年3月前开始出现咳嗽、咳痰，粘白，量少，能咯出，咳嗽呈阵发性，偶则激性，伴轻度咽痒，无气促，夜间有喘息、胸闷，伴鼻塞、流涕、喉咙，无咽痛，, bbox=[114, 185, 855, 218]
2026-08-05 04:47:18,093 INFO     29 [qwen-vl-text] coord item[9]: text=无反酸、嗳气、腹胀，无上腹部隐痛不适感，无伴发热、畏寒，曾自服肺力咳症状未见缓解，现病情好转、稳定，本次门诊距上次门诊间隔时间7天；过去4周，症状控制情况：控制良好，吸入药物使用情况：遵医嘱使用；，吸入装置使用情况：有，正确；急性发作情况：, bbox=[114, 227, 868, 290]
2026-08-05 04:47:18,093 INFO     29 [qwen-vl-text] coord item[10]: text=两次就诊期间急性发作：发作次数：0次，长期规律使用倍氯米松福莫特罗吸入气雾剂治疗。, bbox=[114, 293, 838, 331]
2026-08-05 04:47:18,093 INFO     29 [qwen-vl-text] coord item[11]: text=既往史：鼻炎病史，有糖尿病史, bbox=[114, 347, 428, 363]
2026-08-05 04:47:18,093 INFO     29 [qwen-vl-text] coord item[12]: text=过敏史：未发现, bbox=[114, 380, 297, 396]
2026-08-05 04:47:18,093 INFO     29 [qwen-vl-text] coord item[13]: text=个人史：否认遗传病史，吸烟30年，6支/日，已戒烟8年，饮酒6年，1两/日。, bbox=[114, 410, 797, 427]
2026-08-05 04:47:18,093 INFO     29 [qwen-vl-text] coord item[14]: text=体格检查：神志清，口腔无溃疡、粘膜白斑，肺部听诊，鼻塞，通气，气管居中，双肺呼吸音稍减弱，未闻及明显干湿性罗音。, bbox=[114, 444, 851, 481]
2026-08-05 04:47:18,093 INFO     29 [qwen-vl-text] coord item[15]: text=专科情况：, bbox=[114, 497, 205, 512]
2026-08-05 04:47:18,093 INFO     29 [qwen-vl-text] coord item[16]: text=辅助检查：血常规：Q-CRP：0.54mg/l 白细胞：5.5*109/L 中性粒细胞：, bbox=[114, 529, 748, 545]
2026-08-05 04:47:18,093 INFO     29 [qwen-vl-text] coord item[17]: text=5.17*109/L 60.5% 淋巴细胞：2.23*109/L 26.2% 单个核细胞：, bbox=[114, 551, 691, 567]
2026-08-05 04:47:18,093 INFO     29 [qwen-vl-text] coord item[18]: text=0.46*109/L 5.4% 嗜酸性粒细胞：0.6*109/L 7.1% 呼出气一氧化, bbox=[114, 573, 725, 589]
2026-08-05 04:47:18,093 INFO     29 [qwen-vl-text] coord item[19]: text=氮：FeNO50：130ppb FnNO10：161ppb 肺功能：轻度阻塞性通气功能障碍，支气管激发, bbox=[114, 594, 857, 610]
2026-08-05 04:47:18,093 INFO     29 [qwen-vl-text] coord item[20]: text=试验阳性（PD20=0.312mg AHI：轻度），胸片：心、肺、膈未见异常, bbox=[114, 616, 686, 632]
2026-08-05 04:47:18,093 INFO     29 [qwen-vl-text] coord item[21]: text=治疗项目：, bbox=[114, 648, 203, 663]
2026-08-05 04:47:18,093 INFO     29 [qwen-vl-text] coord item[22]: text=门诊诊断：, bbox=[114, 680, 203, 696]
2026-08-05 04:47:18,093 INFO     29 [qwen-vl-text] coord item[23]: text=1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、2型糖尿病, bbox=[140, 711, 625, 727]
2026-08-05 04:47:18,094 INFO     29 [qwen-vl-text] coord item[24]: text=单 种：, bbox=[114, 743, 221, 758]
2026-08-05 04:47:18,094 INFO     29 [qwen-vl-text] coord item[25]: text=发病时间：, bbox=[114, 773, 201, 789]
2026-08-05 04:47:18,094 INFO     29 [qwen-vl-text] coord item[26]: text=处 置：请仔细阅读药品说明书等文书资料，遵嘱治疗，不适随诊。, bbox=[114, 805, 720, 821]
2026-08-05 04:47:18,094 INFO     29 [qwen-vl-text] coord item[27]: text=倍氯米松福莫特罗吸入气雾剂◆① 1瓶2.0瓶，吸入用药，一天2次 30天, bbox=[158, 837, 778, 853]
2026-08-05 04:47:18,094 INFO     29 [qwen-vl-text] coord item[28]: text=孟鲁司特钠片（省采）◆ 6盒10.0mg，口服，每日1次（口服） 30天, bbox=[158, 867, 808, 883]
2026-08-05 04:47:18,094 INFO     29 [qwen-vl-text] coord item[29]: text=备 注：建议在停药附近社区医疗机构随访。, bbox=[114, 897, 537, 912]
2026-08-05 04:47:18,095 INFO     29 [qwen-vl-text] page=16 — 30/30 coords, api_time=11.8s
2026-08-05 04:47:18,095 INFO     29 [qwen-vl-text] new_positions (30):
[[16, 306.425, 357.0, 42.1, 55.571999999999996], [16, 67.83, 79.72999999999999, 70.728, 83.358], [16, 306.425, 318.325, 70.728, 83.358], [16, 361.16499999999996, 403.40999999999997, 70.728, 83.358], [16, 67.83, 205.27499999999998, 98.514, 111.98599999999999], [16, 242.76, 262.99, 98.514, 111.98599999999999], [16, 306.425, 480.76, 98.514, 111.98599999999999], [16, 67.83, 267.75, 127.142, 140.614], [16, 67.83, 508.72499999999997, 155.76999999999998, 183.55599999999998], [16, 67.83, 516.4599999999999, 191.134, 244.17999999999998], [16, 67.83, 498.60999999999996, 246.706, 278.702], [16, 67.83, 254.66, 292.174, 305.646], [16, 67.83, 176.715, 319.96, 333.432], [16, 67.83, 474.215, 345.21999999999997, 359.534], [16, 67.83, 506.34499999999997, 373.848, 405.002], [16, 67.83, 121.975, 418.474, 431.104], [16, 67.83, 445.06, 445.418, 458.89], [16, 67.83, 411.145, 463.942, 477.414], [16, 67.83, 431.375, 482.466, 495.938], [16, 67.83, 509.91499999999996, 500.14799999999997, 513.62], [16, 67.83, 408.16999999999996, 518.672, 532.144], [16, 67.83, 120.785, 545.616, 558.246], [16, 67.83, 120.785, 572.56, 586.0319999999999], [16, 83.3, 371.875, 598.662, 612.134], [16, 67.83, 131.495, 625.606, 638.236], [16, 67.83, 119.595, 650.866, 664.338], [16, 67.83, 428.4, 677.81, 691.2819999999999], [16, 94.00999999999999, 462.90999999999997, 704.754, 718.226], [16, 94.00999999999999, 480.76, 730.014, 743.486], [16, 67.83, 319.515, 755.274, 767.904]]
2026-08-05 04:47:18,095 INFO     29 [qwen-vl-text] ═══ DONE ═══ 30 positions, pages=1, time=17.9s
2026-08-05 04:47:18,105 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-05 04:47:18,106 INFO     29 [Trace] task=333155a8 | doc=HXJ 哮喘 广三.pdf | Extractor:Clinical | outputs={"chunks": "4 items, types={'OutpatientRecord': 4}", "html": "", "json": "580 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Prescription": "11 items, types={'PrescriptionRecord': 11}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Prescription\": 11, \"chunks_LabExam\": 1}"}
2026-08-05 04:47:18,106 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-05 04:47:18,114 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:47:18,114 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m04:47:18 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:47:18,116 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:47:22,294 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:47:22,304 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-05 04:47:22,304 INFO     29 [Trace] task=333155a8 | doc=HXJ 哮喘 广三.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "580 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Prescription": "11 items, types={'PrescriptionRecord': 11}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Prescription\": 11, \"chunks_LabExam\": 1}"}
2026-08-05 04:47:22,305 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-05 04:47:22,313 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:47:22,313 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 04:47:22,313 INFO     29 [qwen-vl-text] positions(43): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:47:22,313 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [43]
2026-08-05 04:47:22,684 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 04:47:22,685 INFO     29 [qwen-vl-text] LLM extraction start, text_len=304
2026-08-05 04:47:22,685 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:47:22,686 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 126, \"bbox_end\": 168, \"encounter_dates\": [\"2025-09-15\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-09-15\n就诊科室:内科门诊\n主诊医\n姓名\n性别:男\n年龄:64岁\n卡号:4\n患者\n医疗证号:\n处方号\n地址:\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n孟鲁司特钠片◆\n10mg*30/瓶\n30片\n1.05\n31.53\nSig\n10mg/次,口服,qn*30天\n倍氯米松福莫特罗吸入气雾剂◆\n6ug/揿*120揿\n221.61\n221.61\nSig\n2揿/次,吸入,bid*30天\n医师\n医生编号:1326\n配剂人:\n核对人:\n合计:\n收费员:\n打印时间:2025-12-19\n为了您的用药安全,药物处方当天有效 第1页共1页",
    "role": "user"
  }
]
[92m04:47:22 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:47:22,687 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:47:25,754 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:47:25,754 INFO     29 [qwen-vl-text] LLM output (len=667):
{
  "encounter_date": "2025-09-15",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "qn",
      "route": "口服",
      "duration_days": 30,
      "quantity": "30片",
      "notes": null
    },
    {
      "drug_generic_name": "倍氯米松福莫特罗吸入气雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "2揿/次",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 30,
      "quantity": "120揿",
      "notes": null
    }
  ]
}
2026-08-05 04:47:25,754 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-09-15]
2026-08-05 04:47:25,759 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2697300, prompt_len=1046
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共43行）
["门(急)诊处方", "就诊时间:2025-09-15", "就诊科室:内科门诊", "主诊医", "姓名", "性别:男", "年龄:64岁", "卡号:4", "患者", "医疗证号:", "处方号", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "孟鲁司特钠片◆", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天", "倍氯米松福莫特罗吸入气雾剂◆", "6ug/揿*120揿", "221.61", "221.61", "Sig", "2揿/次,吸入,bid*30天", "医师", "医生编号:1326", "配剂人:", "核对人:", "合计:", "收费员:", "打印时间:2025-12-19", "为了您的用药安全,药物处方当天有效 第1页共1页"]

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
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord API raw response (len=2175):
[
	{"text": "门(急)诊处方", "bbox": [383, 15, 617, 50]},
	{"text": "就诊时间:2025-09-15", "bbox": [48, 62, 287, 81]},
	{"text": "就诊科室:内科门诊", "bbox": [321, 62, 527, 82]},
	{"text": "主诊医", "bbox": [613, 64, 683, 84]},
	{"text": "姓名", "bbox": [48, 89, 94, 109]},
	{"text": "性别:男", "bbox": [321, 90, 407, 110]},
	{"text": "年龄:64岁", "bbox": [456, 91, 565, 110]},
	{"text": "卡号:4", "bbox": [613, 93, 683, 111]},
	{"text": "患者", "bbox": [48, 117, 94, 136]},
	{"text": "医疗证号:", "bbox": [321, 118, 427, 138]},
	{"text": "处方号", "bbox": [612, 121, 682, 140]},
	{"text": "地址:", "bbox": [48, 144, 100, 164]},
	{"text": "身份证号:", "bbox": [612, 148, 715, 168]},
	{"text": "诊断:支气管哮喘", "bbox": [48, 170, 226, 190]},
	{"text": "西药处方", "bbox": [435, 206, 566, 227]},
	{"text": "组号", "bbox": [112, 237, 160, 257]},
	{"text": "项目名称", "bbox": [218, 238, 316, 258]},
	{"text": "规格", "bbox": [509, 240, 553, 259]},
	{"text": "总量", "bbox": [714, 240, 760, 260]},
	{"text": "单价", "bbox": [818, 240, 864, 260]},
	{"text": "金额", "bbox": [900, 240, 946, 260]},
	{"text": "R:", "bbox": [67, 270, 112, 300]},
	{"text": "孟鲁司特钠片◆", "bbox": [199, 269, 365, 289]},
	{"text": "10mg*30/瓶", "bbox": [509, 272, 631, 291]},
	{"text": "30片", "bbox": [695, 272, 743, 291]},
	{"text": "1.05", "bbox": [800, 273, 850, 291]},
	{"text": "31.53", "bbox": [868, 273, 933, 291]},
	{"text": "Sig", "bbox": [426, 299, 466, 318]},
	{"text": "10mg/次,口服,qn*30天", "bbox": [509, 300, 755, 319]},
	{"text": "倍氯米松福莫特罗吸入气雾剂◆", "bbox": [199, 325, 535, 345]},
	{"text": "6ug/揿*120揿", "bbox": [553, 326, 743, 345]},
	{"text": "221.61", "bbox": [771, 328, 850, 345]},
	{"text": "221.61", "bbox": [868, 328, 931, 345]},
	{"text": "Sig", "bbox": [426, 355, 466, 374]},
	{"text": "2揿/次,吸入,bid*30天", "bbox": [508, 355, 755, 374]},
	{"text": "医师", "bbox": [50, 607, 98, 627]},
	{"text": "医生编号:1326", "bbox": [353, 608, 514, 627]},
	{"text": "配剂人:", "bbox": [559, 608, 639, 627]},
	{"text": "核对人:", "bbox": [767, 608, 845, 627]},
	{"text": "合计:", "bbox": [57, 880, 111, 900]},
	{"text": "收费员:", "bbox": [270, 881, 350, 901]},
	{"text": "打印时间:2025-12-19", "bbox": [58, 905, 305, 924]},
	{"text": "为了您的用药安全,药物处方当天有效 第1页共1页", "bbox": [388, 904, 980, 924]}
]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord API: raw_items=43, valid_items=43, elapsed=12.5s
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[383, 15, 617, 50]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-09-15, bbox=[48, 62, 287, 81]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[321, 62, 527, 82]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[3]: text=主诊医, bbox=[613, 64, 683, 84]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[48, 89, 94, 109]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[321, 90, 407, 110]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:64岁, bbox=[456, 91, 565, 110]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[7]: text=卡号:4, bbox=[613, 93, 683, 111]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[8]: text=患者, bbox=[48, 117, 94, 136]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[321, 118, 427, 138]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[10]: text=处方号, bbox=[612, 121, 682, 140]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[11]: text=地址:, bbox=[48, 144, 100, 164]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[612, 148, 715, 168]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[48, 170, 226, 190]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[435, 206, 566, 227]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[112, 237, 160, 257]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[218, 238, 316, 258]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[509, 240, 553, 259]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[714, 240, 760, 260]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[818, 240, 864, 260]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[900, 240, 946, 260]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[67, 270, 112, 300]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[22]: text=孟鲁司特钠片◆, bbox=[199, 269, 365, 289]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[23]: text=10mg*30/瓶, bbox=[509, 272, 631, 291]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[24]: text=30片, bbox=[695, 272, 743, 291]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[25]: text=1.05, bbox=[800, 273, 850, 291]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[26]: text=31.53, bbox=[868, 273, 933, 291]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[27]: text=Sig, bbox=[426, 299, 466, 318]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[28]: text=10mg/次,口服,qn*30天, bbox=[509, 300, 755, 319]
2026-08-05 04:47:38,235 INFO     29 [qwen-vl-text] coord item[29]: text=倍氯米松福莫特罗吸入气雾剂◆, bbox=[199, 325, 535, 345]
2026-08-05 04:47:38,236 INFO     29 [qwen-vl-text] coord item[30]: text=6ug/揿*120揿, bbox=[553, 326, 743, 345]
2026-08-05 04:47:38,236 INFO     29 [qwen-vl-text] coord item[31]: text=221.61, bbox=[771, 328, 850, 345]
2026-08-05 04:47:38,236 INFO     29 [qwen-vl-text] coord item[32]: text=221.61, bbox=[868, 328, 931, 345]
2026-08-05 04:47:38,236 INFO     29 [qwen-vl-text] coord item[33]: text=Sig, bbox=[426, 355, 466, 374]
2026-08-05 04:47:38,236 INFO     29 [qwen-vl-text] coord item[34]: text=2揿/次,吸入,bid*30天, bbox=[508, 355, 755, 374]
2026-08-05 04:47:38,236 INFO     29 [qwen-vl-text] coord item[35]: text=医师, bbox=[50, 607, 98, 627]
2026-08-05 04:47:38,236 INFO     29 [qwen-vl-text] coord item[36]: text=医生编号:1326, bbox=[353, 608, 514, 627]
2026-08-05 04:47:38,236 INFO     29 [qwen-vl-text] coord item[37]: text=配剂人:, bbox=[559, 608, 639, 627]
2026-08-05 04:47:38,236 INFO     29 [qwen-vl-text] coord item[38]: text=核对人:, bbox=[767, 608, 845, 627]
2026-08-05 04:47:38,236 INFO     29 [qwen-vl-text] coord item[39]: text=合计:, bbox=[57, 880, 111, 900]
2026-08-05 04:47:38,236 INFO     29 [qwen-vl-text] coord item[40]: text=收费员:, bbox=[270, 881, 350, 901]
2026-08-05 04:47:38,236 INFO     29 [qwen-vl-text] coord item[41]: text=打印时间:2025-12-19, bbox=[58, 905, 305, 924]
2026-08-05 04:47:38,236 INFO     29 [qwen-vl-text] coord item[42]: text=为了您的用药安全,药物处方当天有效 第1页共1页, bbox=[388, 904, 980, 924]
2026-08-05 04:47:38,236 INFO     29 [qwen-vl-text] page=4 — 43/43 coords, api_time=12.5s
2026-08-05 04:47:38,236 INFO     29 [qwen-vl-text] new_positions (43):
[[4, 227.885, 367.115, 12.629999999999999, 42.1], [4, 28.56, 170.765, 52.204, 68.202], [4, 190.995, 313.565, 52.204, 69.044], [4, 364.73499999999996, 406.385, 53.888, 70.728], [4, 28.56, 55.93, 74.938, 91.77799999999999], [4, 190.995, 242.165, 75.78, 92.61999999999999], [4, 271.32, 336.175, 76.622, 92.61999999999999], [4, 364.73499999999996, 406.385, 78.306, 93.462], [4, 28.56, 55.93, 98.514, 114.512], [4, 190.995, 254.065, 99.356, 116.196], [4, 364.14, 405.78999999999996, 101.88199999999999, 117.88], [4, 28.56, 59.5, 121.24799999999999, 138.088], [4, 364.14, 425.42499999999995, 124.616, 141.456], [4, 28.56, 134.47, 143.14, 159.98], [4, 258.825, 336.77, 173.452, 191.134], [4, 66.64, 95.19999999999999, 199.554, 216.394], [4, 129.71, 188.01999999999998, 200.396, 217.236], [4, 302.85499999999996, 329.03499999999997, 202.07999999999998, 218.078], [4, 424.83, 452.2, 202.07999999999998, 218.92], [4, 486.71, 514.0799999999999, 202.07999999999998, 218.92], [4, 535.5, 562.87, 202.07999999999998, 218.92], [4, 39.864999999999995, 66.64, 227.34, 252.6], [4, 118.405, 217.17499999999998, 226.498, 243.338], [4, 302.85499999999996, 375.445, 229.024, 245.022], [4, 413.525, 442.085, 229.024, 245.022], [4, 476.0, 505.75, 229.86599999999999, 245.022], [4, 516.4599999999999, 555.135, 229.86599999999999, 245.022], [4, 253.47, 277.27, 251.75799999999998, 267.756], [4, 302.85499999999996, 449.22499999999997, 252.6, 268.598], [4, 118.405, 318.325, 273.65, 290.49], [4, 329.03499999999997, 442.085, 274.492, 290.49], [4, 458.745, 505.75, 276.176, 290.49], [4, 516.4599999999999, 553.9449999999999, 276.176, 290.49], [4, 253.47, 277.27, 298.90999999999997, 314.908], [4, 302.26, 449.22499999999997, 298.90999999999997, 314.908], [4, 29.75, 58.309999999999995, 511.094, 527.934], [4, 210.035, 305.83, 511.936, 527.934], [4, 332.60499999999996, 380.205, 511.936, 527.934], [4, 456.36499999999995, 502.775, 511.936, 527.934], [4, 33.915, 66.045, 740.9599999999999, 757.8], [4, 160.65, 208.25, 741.802, 758.6419999999999], [4, 34.51, 181.475, 762.01, 778.0079999999999], [4, 230.85999999999999, 583.1, 761.168, 778.0079999999999]]
2026-08-05 04:47:38,236 INFO     29 [qwen-vl-text] ═══ DONE ═══ 43 positions, pages=1, time=15.9s
2026-08-05 04:47:38,236 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:47:38,236 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 04:47:38,237 INFO     29 [qwen-vl-text] positions(35): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:47:38,237 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [35]
2026-08-05 04:47:38,426 INFO     29 [qwen-vl-text] page=5, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 04:47:38,427 INFO     29 [qwen-vl-text] LLM extraction start, text_len=235
2026-08-05 04:47:38,427 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:47:38,427 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 169, \"bbox_end\": 203, \"encounter_dates\": [\"2025-08-18\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-08-18\n就诊科室:内科门诊\n主诊\n姓名:\n性别:男\n年龄:64岁\n卡号\n患者类型:GCP支付\n医疗证号:\n处方\n地址:\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n孟鲁司特钠片◆\n10mg*30/瓶\n28片\n1.05\n29.43\nSig\n10mg/次,口服,qn*28天\n倍氯米松福莫特罗吸入气雾剂\n6ug/揿*120揿\n221.61\n221.61\nSig\n2揿/次,吸入,bid*30天",
    "role": "user"
  }
]
[92m04:47:38 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:47:38,428 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:47:38,430 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:47:38.428+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 10, "failed": 0, "current": {"333155a8908811f1a3da71efcdd7cc1f": {"id": "333155a8908811f1a3da71efcdd7cc1f", "doc_id": "32f80906908811f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412392, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905007404, "task_type": "dataflow", "root_trace_id": "8cc21299ba8c4c4f9376bb5b55f5585f", "root_traceparent": "00-8cc21299ba8c4c4f9376bb5b55f5585f-3809269866d439b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:47:42,135 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:47:42,135 INFO     29 [qwen-vl-text] LLM output (len=673):
{
  "encounter_date": "2025-08-18",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "qn",
      "route": "口服",
      "duration_days": 28,
      "quantity": "28片",
      "notes": null
    },
    {
      "drug_generic_name": "倍氯米松福莫特罗吸入气雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "2揿/次",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 30,
      "quantity": "6ug/揿*120揿",
      "notes": null
    }
  ]
}
2026-08-05 04:47:42,135 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-08-18]
2026-08-05 04:47:42,143 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1559196, prompt_len=953
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["门(急)诊处方", "就诊时间:2025-08-18", "就诊科室:内科门诊", "主诊", "姓名:", "性别:男", "年龄:64岁", "卡号", "患者类型:GCP支付", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "孟鲁司特钠片◆", "10mg*30/瓶", "28片", "1.05", "29.43", "Sig", "10mg/次,口服,qn*28天", "倍氯米松福莫特罗吸入气雾剂", "6ug/揿*120揿", "221.61", "221.61", "Sig", "2揿/次,吸入,bid*30天"]

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
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord API raw response (len=1770):
[
	{"text": "门(急)诊处方", "bbox": [383, 18, 617, 84]},
	{"text": "就诊时间:2025-08-18", "bbox": [50, 110, 287, 146]},
	{"text": "就诊科室:内科门诊", "bbox": [323, 110, 529, 147]},
	{"text": "主诊", "bbox": [615, 116, 661, 150]},
	{"text": "姓名:", "bbox": [50, 166, 105, 201]},
	{"text": "性别:男", "bbox": [324, 166, 410, 202]},
	{"text": "年龄:64岁", "bbox": [458, 168, 567, 204]},
	{"text": "卡号", "bbox": [615, 171, 660, 205]},
	{"text": "患者类型:GCP支付", "bbox": [50, 223, 250, 258]},
	{"text": "医疗证号:", "bbox": [325, 224, 430, 260]},
	{"text": "处方", "bbox": [614, 228, 660, 263]},
	{"text": "地址:", "bbox": [50, 277, 105, 313]},
	{"text": "身份证号:", "bbox": [614, 282, 715, 317]},
	{"text": "诊断:支气管哮喘", "bbox": [50, 329, 232, 365]},
	{"text": "西药处方", "bbox": [440, 394, 570, 430]},
	{"text": "组号", "bbox": [118, 458, 167, 493]},
	{"text": "项目名称", "bbox": [225, 458, 322, 494]},
	{"text": "规格", "bbox": [513, 458, 557, 493]},
	{"text": "总量", "bbox": [716, 461, 761, 496]},
	{"text": "单价", "bbox": [819, 460, 865, 495]},
	{"text": "金额", "bbox": [900, 460, 946, 495]},
	{"text": "R:", "bbox": [73, 524, 119, 578]},
	{"text": "孟鲁司特钠片◆", "bbox": [205, 519, 371, 555]},
	{"text": "10mg*30/瓶", "bbox": [514, 520, 635, 556]},
	{"text": "28片", "bbox": [698, 522, 744, 556]},
	{"text": "1.05", "bbox": [801, 523, 851, 555]},
	{"text": "29.43", "bbox": [870, 523, 934, 555]},
	{"text": "Sig", "bbox": [432, 574, 471, 607]},
	{"text": "10mg/次,口服,qn*28天", "bbox": [514, 568, 757, 609]},
	{"text": "倍氯米松福莫特罗吸入气雾剂", "bbox": [204, 625, 531, 661]},
	{"text": "6ug/揿*120揿", "bbox": [567, 625, 746, 661]},
	{"text": "221.61", "bbox": [774, 630, 852, 661]},
	{"text": "221.61", "bbox": [858, 630, 931, 661]},
	{"text": "Sig", "bbox": [432, 681, 471, 714]},
	{"text": "2揿/次,吸入,bid*30天", "bbox": [513, 679, 758, 714]}
]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord API: raw_items=35, valid_items=35, elapsed=9.2s
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[383, 18, 617, 84]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-08-18, bbox=[50, 110, 287, 146]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[323, 110, 529, 147]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[615, 116, 661, 150]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[4]: text=姓名:, bbox=[50, 166, 105, 201]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[324, 166, 410, 202]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:64岁, bbox=[458, 168, 567, 204]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[7]: text=卡号, bbox=[615, 171, 660, 205]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[8]: text=患者类型:GCP支付, bbox=[50, 223, 250, 258]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[325, 224, 430, 260]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[10]: text=处方, bbox=[614, 228, 660, 263]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[11]: text=地址:, bbox=[50, 277, 105, 313]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[614, 282, 715, 317]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[50, 329, 232, 365]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[440, 394, 570, 430]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[118, 458, 167, 493]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[225, 458, 322, 494]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[513, 458, 557, 493]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[716, 461, 761, 496]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[819, 460, 865, 495]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[900, 460, 946, 495]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[73, 524, 119, 578]
2026-08-05 04:47:51,323 INFO     29 [qwen-vl-text] coord item[22]: text=孟鲁司特钠片◆, bbox=[205, 519, 371, 555]
2026-08-05 04:47:51,324 INFO     29 [qwen-vl-text] coord item[23]: text=10mg*30/瓶, bbox=[514, 520, 635, 556]
2026-08-05 04:47:51,324 INFO     29 [qwen-vl-text] coord item[24]: text=28片, bbox=[698, 522, 744, 556]
2026-08-05 04:47:51,324 INFO     29 [qwen-vl-text] coord item[25]: text=1.05, bbox=[801, 523, 851, 555]
2026-08-05 04:47:51,324 INFO     29 [qwen-vl-text] coord item[26]: text=29.43, bbox=[870, 523, 934, 555]
2026-08-05 04:47:51,324 INFO     29 [qwen-vl-text] coord item[27]: text=Sig, bbox=[432, 574, 471, 607]
2026-08-05 04:47:51,324 INFO     29 [qwen-vl-text] coord item[28]: text=10mg/次,口服,qn*28天, bbox=[514, 568, 757, 609]
2026-08-05 04:47:51,324 INFO     29 [qwen-vl-text] coord item[29]: text=倍氯米松福莫特罗吸入气雾剂, bbox=[204, 625, 531, 661]
2026-08-05 04:47:51,324 INFO     29 [qwen-vl-text] coord item[30]: text=6ug/揿*120揿, bbox=[567, 625, 746, 661]
2026-08-05 04:47:51,324 INFO     29 [qwen-vl-text] coord item[31]: text=221.61, bbox=[774, 630, 852, 661]
2026-08-05 04:47:51,324 INFO     29 [qwen-vl-text] coord item[32]: text=221.61, bbox=[858, 630, 931, 661]
2026-08-05 04:47:51,324 INFO     29 [qwen-vl-text] coord item[33]: text=Sig, bbox=[432, 681, 471, 714]
2026-08-05 04:47:51,324 INFO     29 [qwen-vl-text] coord item[34]: text=2揿/次,吸入,bid*30天, bbox=[513, 679, 758, 714]
2026-08-05 04:47:51,324 INFO     29 [qwen-vl-text] page=5 — 35/35 coords, api_time=9.2s
2026-08-05 04:47:51,324 INFO     29 [qwen-vl-text] new_positions (35):
[[5, 322.486, 519.514, 10.709999999999999, 49.98], [5, 42.1, 241.654, 65.45, 86.86999999999999], [5, 271.966, 445.418, 65.45, 87.46499999999999], [5, 517.8299999999999, 556.562, 69.02, 89.25], [5, 42.1, 88.41, 98.77, 119.595], [5, 272.808, 345.21999999999997, 98.77, 120.19], [5, 385.63599999999997, 477.414, 99.96, 121.38], [5, 517.8299999999999, 555.72, 101.74499999999999, 121.975], [5, 42.1, 210.5, 132.685, 153.51], [5, 273.65, 362.06, 133.28, 154.7], [5, 516.9879999999999, 555.72, 135.66, 156.48499999999999], [5, 42.1, 88.41, 164.815, 186.23499999999999], [5, 516.9879999999999, 602.03, 167.79, 188.61499999999998], [5, 42.1, 195.344, 195.755, 217.17499999999998], [5, 370.47999999999996, 479.94, 234.42999999999998, 255.85], [5, 99.356, 140.614, 272.51, 293.335], [5, 189.45, 271.12399999999997, 272.51, 293.93], [5, 431.94599999999997, 468.99399999999997, 272.51, 293.335], [5, 602.872, 640.762, 274.295, 295.12], [5, 689.598, 728.3299999999999, 273.7, 294.525], [5, 757.8, 796.5319999999999, 273.7, 294.525], [5, 61.466, 100.198, 311.78, 343.90999999999997], [5, 172.60999999999999, 312.382, 308.805, 330.22499999999997], [5, 432.788, 534.67, 309.4, 330.82], [5, 587.716, 626.448, 310.59, 330.82], [5, 674.442, 716.542, 311.185, 330.22499999999997], [5, 732.54, 786.428, 311.185, 330.22499999999997], [5, 363.74399999999997, 396.582, 341.53, 361.16499999999996], [5, 432.788, 637.394, 337.96, 362.35499999999996], [5, 171.768, 447.102, 371.875, 393.29499999999996], [5, 477.414, 628.132, 371.875, 393.29499999999996], [5, 651.708, 717.384, 374.84999999999997, 393.29499999999996], [5, 722.4359999999999, 783.9019999999999, 374.84999999999997, 393.29499999999996], [5, 363.74399999999997, 396.582, 405.195, 424.83], [5, 431.94599999999997, 638.236, 404.005, 424.83]]
2026-08-05 04:47:51,324 INFO     29 [qwen-vl-text] ═══ DONE ═══ 35 positions, pages=1, time=13.1s
2026-08-05 04:47:51,324 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:47:51,324 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 04:47:51,324 INFO     29 [qwen-vl-text] positions(34): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:47:51,324 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [34]
2026-08-05 04:47:51,490 INFO     29 [qwen-vl-text] page=6, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 04:47:51,491 INFO     29 [qwen-vl-text] LLM extraction start, text_len=234
2026-08-05 04:47:51,491 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:47:51,491 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 204, \"bbox_end\": 237, \"encounter_dates\": [\"2025-05-30\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-05-30\n就诊科室:内科门诊\n主\n姓名\n性别:男\n年龄:64岁\n卡\n患者类型:GCP支付\n医疗证号:\n处\n地址:\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n孟鲁司特钠片◆\n10mg*5/盒\n90片\n2.56\n230.58\nSig\n10mg/次,口服,qn*90天\n倍氯米松福莫特罗吸入气雾剂0◆@/6ug/揿*120瓶\n221.61\n664.83\nSig\n2揿/次,吸入,bid*90天",
    "role": "user"
  }
]
[92m04:47:51 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:47:51,493 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:47:55,232 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:47:55,233 INFO     29 [qwen-vl-text] LLM output (len=665):
{
  "encounter_date": "2025-05-30",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "qn",
      "route": "口服",
      "duration_days": 90,
      "quantity": "90片",
      "notes": null
    },
    {
      "drug_generic_name": "倍氯米松福莫特罗吸入气雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "2揿/次",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 90,
      "quantity": "1瓶",
      "notes": null
    }
  ]
}
2026-08-05 04:47:55,233 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-05-30]
2026-08-05 04:47:55,236 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1527432, prompt_len=949
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共34行）
["门(急)诊处方", "就诊时间:2025-05-30", "就诊科室:内科门诊", "主", "姓名", "性别:男", "年龄:64岁", "卡", "患者类型:GCP支付", "医疗证号:", "处", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "孟鲁司特钠片◆", "10mg*5/盒", "90片", "2.56", "230.58", "Sig", "10mg/次,口服,qn*90天", "倍氯米松福莫特罗吸入气雾剂0◆@/6ug/揿*120瓶", "221.61", "664.83", "Sig", "2揿/次,吸入,bid*90天"]

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
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord API raw response (len=1725):
[
	{"text": "门(急)诊处方", "bbox": [387, 38, 624, 104]},
	{"text": "就诊时间:2025-05-30", "bbox": [60, 135, 294, 169]},
	{"text": "就诊科室:内科门诊", "bbox": [328, 132, 535, 167]},
	{"text": "主", "bbox": [620, 135, 644, 170]},
	{"text": "姓名", "bbox": [60, 189, 87, 224]},
	{"text": "性别:男", "bbox": [329, 187, 415, 223]},
	{"text": "年龄:64岁", "bbox": [463, 189, 573, 224]},
	{"text": "卡", "bbox": [620, 189, 644, 224]},
	{"text": "患者类型:GCP支付", "bbox": [60, 244, 258, 280]},
	{"text": "医疗证号:", "bbox": [330, 245, 436, 280]},
	{"text": "处", "bbox": [620, 247, 644, 282]},
	{"text": "地址:", "bbox": [60, 300, 115, 336]},
	{"text": "身份证号:", "bbox": [621, 302, 725, 337]},
	{"text": "诊断:支气管哮喘", "bbox": [61, 351, 240, 387]},
	{"text": "西药处方", "bbox": [446, 414, 578, 450]},
	{"text": "组号", "bbox": [128, 477, 175, 512]},
	{"text": "项目名称", "bbox": [234, 477, 329, 513]},
	{"text": "规格", "bbox": [520, 479, 565, 513]},
	{"text": "总量", "bbox": [725, 479, 772, 514]},
	{"text": "单价", "bbox": [832, 479, 878, 513]},
	{"text": "金额", "bbox": [914, 477, 962, 513]},
	{"text": "R:", "bbox": [81, 543, 129, 596]},
	{"text": "孟鲁司特钠片◆", "bbox": [214, 538, 378, 574]},
	{"text": "10mg*5/盒", "bbox": [520, 540, 630, 576]},
	{"text": "90片", "bbox": [706, 540, 755, 574]},
	{"text": "2.56", "bbox": [810, 541, 868, 573]},
	{"text": "230.58", "bbox": [873, 541, 949, 573]},
	{"text": "Sig", "bbox": [439, 594, 478, 627]},
	{"text": "10mg/次,口服,qn*90天", "bbox": [520, 594, 768, 630]},
	{"text": "倍氯米松福莫特罗吸入气雾剂0◆@/6ug/揿*120瓶", "bbox": [214, 644, 755, 680]},
	{"text": "221.61", "bbox": [784, 648, 862, 679]},
	{"text": "664.83", "bbox": [868, 648, 949, 679]},
	{"text": "Sig", "bbox": [440, 701, 479, 734]},
	{"text": "2揿/次,吸入,bid*90天", "bbox": [520, 698, 768, 734]}
]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=9.0s
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[387, 38, 624, 104]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-05-30, bbox=[60, 135, 294, 169]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[328, 132, 535, 167]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[3]: text=主, bbox=[620, 135, 644, 170]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[60, 189, 87, 224]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[329, 187, 415, 223]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:64岁, bbox=[463, 189, 573, 224]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[7]: text=卡, bbox=[620, 189, 644, 224]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[8]: text=患者类型:GCP支付, bbox=[60, 244, 258, 280]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[330, 245, 436, 280]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[10]: text=处, bbox=[620, 247, 644, 282]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[11]: text=地址:, bbox=[60, 300, 115, 336]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[621, 302, 725, 337]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[61, 351, 240, 387]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[446, 414, 578, 450]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[128, 477, 175, 512]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[234, 477, 329, 513]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[520, 479, 565, 513]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[725, 479, 772, 514]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[832, 479, 878, 513]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[914, 477, 962, 513]
2026-08-05 04:48:04,235 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[81, 543, 129, 596]
2026-08-05 04:48:04,236 INFO     29 [qwen-vl-text] coord item[22]: text=孟鲁司特钠片◆, bbox=[214, 538, 378, 574]
2026-08-05 04:48:04,236 INFO     29 [qwen-vl-text] coord item[23]: text=10mg*5/盒, bbox=[520, 540, 630, 576]
2026-08-05 04:48:04,236 INFO     29 [qwen-vl-text] coord item[24]: text=90片, bbox=[706, 540, 755, 574]
2026-08-05 04:48:04,236 INFO     29 [qwen-vl-text] coord item[25]: text=2.56, bbox=[810, 541, 868, 573]
2026-08-05 04:48:04,236 INFO     29 [qwen-vl-text] coord item[26]: text=230.58, bbox=[873, 541, 949, 573]
2026-08-05 04:48:04,236 INFO     29 [qwen-vl-text] coord item[27]: text=Sig, bbox=[439, 594, 478, 627]
2026-08-05 04:48:04,236 INFO     29 [qwen-vl-text] coord item[28]: text=10mg/次,口服,qn*90天, bbox=[520, 594, 768, 630]
2026-08-05 04:48:04,236 INFO     29 [qwen-vl-text] coord item[29]: text=倍氯米松福莫特罗吸入气雾剂0◆@/6ug/揿*120瓶, bbox=[214, 644, 755, 680]
2026-08-05 04:48:04,236 INFO     29 [qwen-vl-text] coord item[30]: text=221.61, bbox=[784, 648, 862, 679]
2026-08-05 04:48:04,236 INFO     29 [qwen-vl-text] coord item[31]: text=664.83, bbox=[868, 648, 949, 679]
2026-08-05 04:48:04,236 INFO     29 [qwen-vl-text] coord item[32]: text=Sig, bbox=[440, 701, 479, 734]
2026-08-05 04:48:04,236 INFO     29 [qwen-vl-text] coord item[33]: text=2揿/次,吸入,bid*90天, bbox=[520, 698, 768, 734]
2026-08-05 04:48:04,236 INFO     29 [qwen-vl-text] page=6 — 34/34 coords, api_time=9.0s
2026-08-05 04:48:04,236 INFO     29 [qwen-vl-text] new_positions (34):
[[6, 325.854, 525.408, 22.61, 61.879999999999995], [6, 50.519999999999996, 247.548, 80.325, 100.55499999999999], [6, 276.176, 450.46999999999997, 78.53999999999999, 99.365], [6, 522.04, 542.2479999999999, 80.325, 101.14999999999999], [6, 50.519999999999996, 73.25399999999999, 112.455, 133.28], [6, 277.018, 349.43, 111.265, 132.685], [6, 389.846, 482.466, 112.455, 133.28], [6, 522.04, 542.2479999999999, 112.455, 133.28], [6, 50.519999999999996, 217.236, 145.18, 166.6], [6, 277.86, 367.11199999999997, 145.775, 166.6], [6, 522.04, 542.2479999999999, 146.965, 167.79], [6, 50.519999999999996, 96.83, 178.5, 199.92], [6, 522.882, 610.4499999999999, 179.69, 200.515], [6, 51.361999999999995, 202.07999999999998, 208.845, 230.265], [6, 375.532, 486.676, 246.32999999999998, 267.75], [6, 107.776, 147.35, 283.815, 304.64], [6, 197.028, 277.018, 283.815, 305.235], [6, 437.84, 475.72999999999996, 285.005, 305.235], [6, 610.4499999999999, 650.024, 285.005, 305.83], [6, 700.544, 739.276, 285.005, 305.235], [6, 769.588, 810.004, 283.815, 305.235], [6, 68.202, 108.618, 323.085, 354.62], [6, 180.188, 318.276, 320.11, 341.53], [6, 437.84, 530.46, 321.3, 342.71999999999997], [6, 594.452, 635.7099999999999, 321.3, 341.53], [6, 682.02, 730.856, 321.895, 340.935], [6, 735.066, 799.058, 321.895, 340.935], [6, 369.638, 402.476, 353.43, 373.065], [6, 437.84, 646.656, 353.43, 374.84999999999997], [6, 180.188, 635.7099999999999, 383.18, 404.59999999999997], [6, 660.1279999999999, 725.804, 385.56, 404.005], [6, 730.856, 799.058, 385.56, 404.005], [6, 370.47999999999996, 403.318, 417.09499999999997, 436.72999999999996], [6, 437.84, 646.656, 415.31, 436.72999999999996]]
2026-08-05 04:48:04,236 INFO     29 [qwen-vl-text] ═══ DONE ═══ 34 positions, pages=1, time=12.9s
2026-08-05 04:48:04,236 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:48:04,236 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 04:48:04,236 INFO     29 [qwen-vl-text] positions(33): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:48:04,236 INFO     29 [qwen-vl-text] page grouping: [7], lines per page: [33]
2026-08-05 04:48:04,433 INFO     29 [qwen-vl-text] page=7, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 04:48:04,434 INFO     29 [qwen-vl-text] LLM extraction start, text_len=241
2026-08-05 04:48:04,434 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:48:04,434 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 238, \"bbox_end\": 270, \"encounter_dates\": [\"2025-03-05\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-03-05\n就诊科室:内科门诊\n主诊医\n姓名\n性别:男\n年龄:64岁\n卡号:\n患者类型:GCP支付\n医疗证号:\n处方号:\n地址:\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n倍氯米松福莫特罗吸入气雾剂*0ug/6ug/瓶*120瓶\n221.61 443.22\nSig\n2揿/次,吸入,bid*60天\n孟鲁司特钠片\n10mg*30/瓶\n60片\n1.05\n63.06\nSig\n10mg/次,口服,qn*60天",
    "role": "user"
  }
]
[92m04:48:04 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:48:04,436 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:48:11,236 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:48:11,236 INFO     29 [qwen-vl-text] LLM output (len=672):
{
  "encounter_date": "2025-03-05",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "倍氯米松福莫特罗吸入气雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "6ug/揿",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 60,
      "quantity": "1瓶",
      "notes": "2揿/次"
    },
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "qn",
      "route": "口服",
      "duration_days": 60,
      "quantity": "60片",
      "notes": "10mg/次"
    }
  ]
}
2026-08-05 04:48:11,236 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-03-05]
2026-08-05 04:48:11,238 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1740969, prompt_len=953
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["门(急)诊处方", "就诊时间:2025-03-05", "就诊科室:内科门诊", "主诊医", "姓名", "性别:男", "年龄:64岁", "卡号:", "患者类型:GCP支付", "医疗证号:", "处方号:", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂*0ug/6ug/瓶*120瓶", "221.61 443.22", "Sig", "2揿/次,吸入,bid*60天", "孟鲁司特钠片", "10mg*30/瓶", "60片", "1.05", "63.06", "Sig", "10mg/次,口服,qn*60天"]

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
2026-08-05 04:48:20,094 INFO     29 [qwen-vl-text] coord API raw response (len=1687):
[
	{"text": "门(急)诊处方", "bbox": [382, 22, 608, 87]},
	{"text": "就诊时间:2025-03-05", "bbox": [55, 115, 288, 149]},
	{"text": "就诊科室:内科门诊", "bbox": [323, 112, 522, 147]},
	{"text": "主诊医", "bbox": [608, 115, 674, 147]},
	{"text": "姓名", "bbox": [55, 169, 98, 204]},
	{"text": "性别:男", "bbox": [323, 167, 406, 201]},
	{"text": "年龄:64岁", "bbox": [454, 167, 559, 201]},
	{"text": "卡号:", "bbox": [608, 169, 674, 201]},
	{"text": "患者类型:GCP支付", "bbox": [55, 225, 250, 258]},
	{"text": "医疗证号:", "bbox": [323, 223, 425, 257]},
	{"text": "处方号:", "bbox": [607, 223, 674, 257]},
	{"text": "地址:", "bbox": [55, 278, 109, 312]},
	{"text": "身份证号:", "bbox": [607, 276, 707, 310]},
	{"text": "诊断:支气管哮喘", "bbox": [55, 328, 232, 363]},
	{"text": "西药处方", "bbox": [436, 388, 563, 422]},
	{"text": "组号", "bbox": [122, 454, 169, 488]},
	{"text": "项目名称", "bbox": [225, 453, 320, 487]},
	{"text": "规格", "bbox": [508, 453, 551, 485]},
	{"text": "总量", "bbox": [708, 453, 753, 487]},
	{"text": "单价", "bbox": [808, 453, 854, 487]},
	{"text": "金额", "bbox": [889, 451, 934, 485]},
	{"text": "R:", "bbox": [78, 519, 123, 571]},
	{"text": "倍氯米松福莫特罗吸入气雾剂*0ug/6ug/瓶*120瓶", "bbox": [206, 511, 737, 546]},
	{"text": "221.61 443.22", "bbox": [764, 513, 920, 543]},
	{"text": "Sig", "bbox": [428, 565, 467, 597]},
	{"text": "2揿/次,吸入,bid*60天", "bbox": [507, 564, 748, 597]},
	{"text": "孟鲁司特钠片", "bbox": [207, 617, 350, 651]},
	{"text": "10mg*30/瓶", "bbox": [508, 615, 628, 650]},
	{"text": "60片", "bbox": [690, 615, 735, 647]},
	{"text": "1.05", "bbox": [790, 617, 839, 647]},
	{"text": "63.06", "bbox": [856, 617, 919, 647]},
	{"text": "Sig", "bbox": [428, 673, 467, 705]},
	{"text": "10mg/次,口服,qn*60天", "bbox": [508, 670, 748, 705]}
]
2026-08-05 04:48:20,094 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=8.9s
2026-08-05 04:48:20,094 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[382, 22, 608, 87]
2026-08-05 04:48:20,094 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-03-05, bbox=[55, 115, 288, 149]
2026-08-05 04:48:20,094 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[323, 112, 522, 147]
2026-08-05 04:48:20,094 INFO     29 [qwen-vl-text] coord item[3]: text=主诊医, bbox=[608, 115, 674, 147]
2026-08-05 04:48:20,094 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[55, 169, 98, 204]
2026-08-05 04:48:20,094 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[323, 167, 406, 201]
2026-08-05 04:48:20,094 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:64岁, bbox=[454, 167, 559, 201]
2026-08-05 04:48:20,094 INFO     29 [qwen-vl-text] coord item[7]: text=卡号:, bbox=[608, 169, 674, 201]
2026-08-05 04:48:20,094 INFO     29 [qwen-vl-text] coord item[8]: text=患者类型:GCP支付, bbox=[55, 225, 250, 258]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[323, 223, 425, 257]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[10]: text=处方号:, bbox=[607, 223, 674, 257]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[11]: text=地址:, bbox=[55, 278, 109, 312]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[607, 276, 707, 310]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[55, 328, 232, 363]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[436, 388, 563, 422]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[122, 454, 169, 488]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[225, 453, 320, 487]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[508, 453, 551, 485]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[708, 453, 753, 487]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[808, 453, 854, 487]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[889, 451, 934, 485]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[78, 519, 123, 571]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[22]: text=倍氯米松福莫特罗吸入气雾剂*0ug/6ug/瓶*120瓶, bbox=[206, 511, 737, 546]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[23]: text=221.61 443.22, bbox=[764, 513, 920, 543]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[428, 565, 467, 597]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[25]: text=2揿/次,吸入,bid*60天, bbox=[507, 564, 748, 597]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[26]: text=孟鲁司特钠片, bbox=[207, 617, 350, 651]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[27]: text=10mg*30/瓶, bbox=[508, 615, 628, 650]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[28]: text=60片, bbox=[690, 615, 735, 647]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[29]: text=1.05, bbox=[790, 617, 839, 647]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[30]: text=63.06, bbox=[856, 617, 919, 647]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[31]: text=Sig, bbox=[428, 673, 467, 705]
2026-08-05 04:48:20,095 INFO     29 [qwen-vl-text] coord item[32]: text=10mg/次,口服,qn*60天, bbox=[508, 670, 748, 705]
2026-08-05 04:48:20,096 INFO     29 [qwen-vl-text] page=7 — 33/33 coords, api_time=8.9s
2026-08-05 04:48:20,097 INFO     29 [qwen-vl-text] new_positions (33):
[[7, 321.644, 511.936, 13.09, 51.765], [7, 46.309999999999995, 242.49599999999998, 68.425, 88.655], [7, 271.966, 439.524, 66.64, 87.46499999999999], [7, 511.936, 567.5079999999999, 68.425, 87.46499999999999], [7, 46.309999999999995, 82.51599999999999, 100.55499999999999, 121.38], [7, 271.966, 341.852, 99.365, 119.595], [7, 382.268, 470.678, 99.365, 119.595], [7, 511.936, 567.5079999999999, 100.55499999999999, 119.595], [7, 46.309999999999995, 210.5, 133.875, 153.51], [7, 271.966, 357.84999999999997, 132.685, 152.915], [7, 511.094, 567.5079999999999, 132.685, 152.915], [7, 46.309999999999995, 91.77799999999999, 165.41, 185.64], [7, 511.094, 595.294, 164.22, 184.45], [7, 46.309999999999995, 195.344, 195.16, 215.98499999999999], [7, 367.11199999999997, 474.046, 230.85999999999999, 251.08999999999997], [7, 102.72399999999999, 142.298, 270.13, 290.36], [7, 189.45, 269.44, 269.53499999999997, 289.765], [7, 427.736, 463.942, 269.53499999999997, 288.575], [7, 596.136, 634.026, 269.53499999999997, 289.765], [7, 680.336, 719.068, 269.53499999999997, 289.765], [7, 748.538, 786.428, 268.34499999999997, 288.575], [7, 65.676, 103.566, 308.805, 339.745], [7, 173.452, 620.554, 304.04499999999996, 324.87], [7, 643.288, 774.64, 305.235, 323.085], [7, 360.376, 393.214, 336.175, 355.215], [7, 426.894, 629.816, 335.58, 355.215], [7, 174.29399999999998, 294.7, 367.115, 387.34499999999997], [7, 427.736, 528.776, 365.925, 386.75], [7, 580.98, 618.87, 365.925, 384.965], [7, 665.18, 706.438, 367.115, 384.965], [7, 720.752, 773.798, 367.115, 384.965], [7, 360.376, 393.214, 400.435, 419.47499999999997], [7, 427.736, 629.816, 398.65, 419.47499999999997]]
2026-08-05 04:48:20,097 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=15.9s
2026-08-05 04:48:20,097 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:48:20,097 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 04:48:20,097 INFO     29 [qwen-vl-text] positions(33): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:48:20,097 INFO     29 [qwen-vl-text] page grouping: [8], lines per page: [33]
2026-08-05 04:48:20,258 INFO     29 [qwen-vl-text] page=8, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 04:48:20,259 INFO     29 [qwen-vl-text] LLM extraction start, text_len=238
2026-08-05 04:48:20,259 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:48:20,259 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 271, \"bbox_end\": 303, \"encounter_dates\": [\"2025-03-05\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-03-05\n就诊科室:内科门诊\n主诊\n姓名\n性别:男\n年龄:64岁\n卡号\n患者类型:GCP支付\n医疗证号:\n处方\n地址:\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿\n221.61 221.61\nSig\n2揿/次,吸入,bid*30天\n孟鲁司特钠片\n10mg*30/瓶\n30片\n1.05\n31.53\nSig\n10mg/次,口服,qn*30天",
    "role": "user"
  }
]
[92m04:48:20 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:48:20,260 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:48:20,261 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:48:20.260+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 10, "failed": 0, "current": {"333155a8908811f1a3da71efcdd7cc1f": {"id": "333155a8908811f1a3da71efcdd7cc1f", "doc_id": "32f80906908811f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412392, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905007404, "task_type": "dataflow", "root_trace_id": "8cc21299ba8c4c4f9376bb5b55f5585f", "root_traceparent": "00-8cc21299ba8c4c4f9376bb5b55f5585f-3809269866d439b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:48:23,539 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:48:23,540 INFO     29 [qwen-vl-text] LLM output (len=680):
{
  "encounter_date": "2025-03-05",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "倍氯米松福莫特罗吸入气雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "100ug/6ug/揿",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 30,
      "quantity": "120揿",
      "notes": "2揿/次"
    },
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "qn",
      "route": "口服",
      "duration_days": 30,
      "quantity": "30片",
      "notes": "10mg/次"
    }
  ]
}
2026-08-05 04:48:23,540 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-03-05]
2026-08-05 04:48:23,546 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1610510, prompt_len=950
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["门(急)诊处方", "就诊时间:2025-03-05", "就诊科室:内科门诊", "主诊", "姓名", "性别:男", "年龄:64岁", "卡号", "患者类型:GCP支付", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿", "221.61 221.61", "Sig", "2揿/次,吸入,bid*30天", "孟鲁司特钠片", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天"]

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
2026-08-05 04:48:32,318 INFO     29 [qwen-vl-text] coord API raw response (len=1684):
[
	{"text": "门(急)诊处方", "bbox": [382, 31, 617, 97]},
	{"text": "就诊时间:2025-03-05", "bbox": [45, 129, 285, 163]},
	{"text": "就诊科室:内科门诊", "bbox": [321, 123, 527, 158]},
	{"text": "主诊", "bbox": [614, 120, 662, 155]},
	{"text": "姓名", "bbox": [45, 183, 90, 217]},
	{"text": "性别:男", "bbox": [321, 177, 407, 212]},
	{"text": "年龄:64岁", "bbox": [455, 177, 565, 210]},
	{"text": "卡号", "bbox": [614, 175, 660, 209]},
	{"text": "患者类型:GCP支付", "bbox": [46, 236, 247, 269]},
	{"text": "医疗证号:", "bbox": [321, 234, 426, 267]},
	{"text": "处方", "bbox": [613, 231, 660, 265]},
	{"text": "地址:", "bbox": [46, 290, 102, 324]},
	{"text": "身份证号:", "bbox": [613, 283, 716, 317]},
	{"text": "诊断:支气管哮喘", "bbox": [47, 338, 226, 372]},
	{"text": "西药处方", "bbox": [435, 395, 567, 428]},
	{"text": "组号", "bbox": [113, 462, 160, 494]},
	{"text": "项目名称", "bbox": [219, 460, 317, 493]},
	{"text": "规格", "bbox": [509, 457, 554, 489]},
	{"text": "总量", "bbox": [716, 455, 763, 488]},
	{"text": "单价", "bbox": [821, 454, 868, 487]},
	{"text": "金额", "bbox": [904, 452, 951, 485]},
	{"text": "R:", "bbox": [67, 525, 114, 577]},
	{"text": "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿", "bbox": [198, 515, 746, 550]},
	{"text": "221.61 221.61", "bbox": [775, 515, 936, 544]},
	{"text": "Sig", "bbox": [426, 570, 466, 602]},
	{"text": "2揿/次,吸入,bid*30天", "bbox": [508, 567, 758, 600]},
	{"text": "孟鲁司特钠片", "bbox": [200, 620, 347, 654]},
	{"text": "10mg*30/瓶", "bbox": [510, 617, 633, 651]},
	{"text": "30片", "bbox": [697, 617, 745, 649]},
	{"text": "1.05", "bbox": [803, 617, 854, 647]},
	{"text": "31.53", "bbox": [872, 617, 938, 647]},
	{"text": "Sig", "bbox": [427, 674, 467, 707]},
	{"text": "10mg/次,口服,qn*30天", "bbox": [510, 670, 758, 704]}
]
2026-08-05 04:48:32,318 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=8.8s
2026-08-05 04:48:32,318 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[382, 31, 617, 97]
2026-08-05 04:48:32,318 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-03-05, bbox=[45, 129, 285, 163]
2026-08-05 04:48:32,318 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[321, 123, 527, 158]
2026-08-05 04:48:32,318 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[614, 120, 662, 155]
2026-08-05 04:48:32,318 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[45, 183, 90, 217]
2026-08-05 04:48:32,318 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[321, 177, 407, 212]
2026-08-05 04:48:32,318 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:64岁, bbox=[455, 177, 565, 210]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[7]: text=卡号, bbox=[614, 175, 660, 209]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[8]: text=患者类型:GCP支付, bbox=[46, 236, 247, 269]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[321, 234, 426, 267]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[10]: text=处方, bbox=[613, 231, 660, 265]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[11]: text=地址:, bbox=[46, 290, 102, 324]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[613, 283, 716, 317]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[47, 338, 226, 372]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[435, 395, 567, 428]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[113, 462, 160, 494]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[219, 460, 317, 493]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[509, 457, 554, 489]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[716, 455, 763, 488]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[821, 454, 868, 487]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[904, 452, 951, 485]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[67, 525, 114, 577]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[22]: text=倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿, bbox=[198, 515, 746, 550]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[23]: text=221.61 221.61, bbox=[775, 515, 936, 544]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[426, 570, 466, 602]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[25]: text=2揿/次,吸入,bid*30天, bbox=[508, 567, 758, 600]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[26]: text=孟鲁司特钠片, bbox=[200, 620, 347, 654]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[27]: text=10mg*30/瓶, bbox=[510, 617, 633, 651]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[28]: text=30片, bbox=[697, 617, 745, 649]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[29]: text=1.05, bbox=[803, 617, 854, 647]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[30]: text=31.53, bbox=[872, 617, 938, 647]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[31]: text=Sig, bbox=[427, 674, 467, 707]
2026-08-05 04:48:32,319 INFO     29 [qwen-vl-text] coord item[32]: text=10mg/次,口服,qn*30天, bbox=[510, 670, 758, 704]
2026-08-05 04:48:32,320 INFO     29 [qwen-vl-text] page=8 — 33/33 coords, api_time=8.8s
2026-08-05 04:48:32,320 INFO     29 [qwen-vl-text] new_positions (33):
[[8, 321.644, 519.514, 18.445, 57.714999999999996], [8, 37.89, 239.97, 76.755, 96.985], [8, 270.282, 443.734, 73.185, 94.00999999999999], [8, 516.9879999999999, 557.404, 71.39999999999999, 92.225], [8, 37.89, 75.78, 108.88499999999999, 129.11499999999998], [8, 270.282, 342.69399999999996, 105.315, 126.14], [8, 383.11, 475.72999999999996, 105.315, 124.94999999999999], [8, 516.9879999999999, 555.72, 104.125, 124.35499999999999], [8, 38.732, 207.974, 140.42, 160.055], [8, 270.282, 358.692, 139.23, 158.86499999999998], [8, 516.146, 555.72, 137.445, 157.67499999999998], [8, 38.732, 85.884, 172.54999999999998, 192.78], [8, 516.146, 602.872, 168.385, 188.61499999999998], [8, 39.574, 190.292, 201.10999999999999, 221.34], [8, 366.27, 477.414, 235.02499999999998, 254.66], [8, 95.146, 134.72, 274.89, 293.93], [8, 184.398, 266.914, 273.7, 293.335], [8, 428.578, 466.46799999999996, 271.91499999999996, 290.955], [8, 602.872, 642.446, 270.72499999999997, 290.36], [8, 691.2819999999999, 730.856, 270.13, 289.765], [8, 761.168, 800.742, 268.94, 288.575], [8, 56.414, 95.988, 312.375, 343.315], [8, 166.716, 628.132, 306.425, 327.25], [8, 652.55, 788.112, 306.425, 323.68], [8, 358.692, 392.372, 339.15, 358.19], [8, 427.736, 638.236, 337.365, 357.0], [8, 168.4, 292.174, 368.9, 389.13], [8, 429.41999999999996, 532.986, 367.115, 387.34499999999997], [8, 586.874, 627.29, 367.115, 386.155], [8, 676.126, 719.068, 367.115, 384.965], [8, 734.2239999999999, 789.7959999999999, 367.115, 384.965], [8, 359.534, 393.214, 401.03, 420.66499999999996], [8, 429.41999999999996, 638.236, 398.65, 418.88]]
2026-08-05 04:48:32,320 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=12.2s
2026-08-05 04:48:32,320 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:48:32,321 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 04:48:32,321 INFO     29 [qwen-vl-text] positions(33): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:48:32,321 INFO     29 [qwen-vl-text] page grouping: [9], lines per page: [33]
2026-08-05 04:48:32,538 INFO     29 [qwen-vl-text] page=9, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 04:48:32,539 INFO     29 [qwen-vl-text] LLM extraction start, text_len=242
2026-08-05 04:48:32,539 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:48:32,540 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 306, \"bbox_end\": 338, \"encounter_dates\": [\"2025-02-08\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-02-08\n就诊科室:内科门诊\n主诊\n姓名:\n性别:男\n年龄:64岁\n卡号:\n患者类型:001 支付\n医疗证号:\n处方\n地址:\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120瓶\n221.61 221.61\nSig\n2揿/次,吸入,bid*30天\n孟鲁司特钠片◆\n10mg*30/瓶\n30片\n1.05\n31.53\nSig\n10mg/次,口服,qn*30天",
    "role": "user"
  }
]
[92m04:48:32 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:48:32,542 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:48:36,347 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:48:36,348 INFO     29 [qwen-vl-text] LLM output (len=678):
{
  "encounter_date": "2025-02-08",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "倍氯米松福莫特罗吸入气雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "100ug/6ug/揿",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 30,
      "quantity": "1瓶",
      "notes": "2揿/次"
    },
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "qn",
      "route": "口服",
      "duration_days": 30,
      "quantity": "30片",
      "notes": "10mg/次"
    }
  ]
}
2026-08-05 04:48:36,348 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-02-08]
2026-08-05 04:48:36,352 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1920992, prompt_len=954
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["门(急)诊处方", "就诊时间:2025-02-08", "就诊科室:内科门诊", "主诊", "姓名:", "性别:男", "年龄:64岁", "卡号:", "患者类型:001 支付", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120瓶", "221.61 221.61", "Sig", "2揿/次,吸入,bid*30天", "孟鲁司特钠片◆", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天"]

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
2026-08-05 04:48:48,116 INFO     29 [qwen-vl-text] coord API raw response (len=1688):
[
	{"text": "门(急)诊处方", "bbox": [375, 34, 609, 98]},
	{"text": "就诊时间:2025-02-08", "bbox": [40, 130, 278, 166]},
	{"text": "就诊科室:内科门诊", "bbox": [314, 127, 520, 163]},
	{"text": "主诊", "bbox": [606, 129, 662, 163]},
	{"text": "姓名:", "bbox": [40, 185, 100, 221]},
	{"text": "性别:男", "bbox": [314, 182, 400, 218]},
	{"text": "年龄:64岁", "bbox": [448, 182, 558, 218]},
	{"text": "卡号:", "bbox": [606, 183, 662, 218]},
	{"text": "患者类型:001 支付", "bbox": [40, 240, 238, 276]},
	{"text": "医疗证号:", "bbox": [314, 239, 420, 275]},
	{"text": "处方", "bbox": [605, 240, 654, 275]},
	{"text": "地址:", "bbox": [40, 296, 96, 332]},
	{"text": "身份证号:", "bbox": [605, 293, 709, 329]},
	{"text": "诊断:支气管哮喘", "bbox": [40, 348, 219, 384]},
	{"text": "西药处方", "bbox": [428, 407, 561, 443]},
	{"text": "组号", "bbox": [107, 474, 154, 509]},
	{"text": "项目名称", "bbox": [212, 473, 310, 509]},
	{"text": "规格", "bbox": [503, 471, 548, 506]},
	{"text": "总量", "bbox": [708, 471, 755, 506]},
	{"text": "单价", "bbox": [814, 471, 861, 506]},
	{"text": "金额", "bbox": [897, 470, 943, 505]},
	{"text": "R:", "bbox": [61, 540, 108, 593]},
	{"text": "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120瓶", "bbox": [192, 531, 738, 568]},
	{"text": "221.61 221.61", "bbox": [767, 534, 927, 565]},
	{"text": "Sig", "bbox": [420, 587, 460, 620]},
	{"text": "2揿/次,吸入,bid*30天", "bbox": [503, 585, 750, 620]},
	{"text": "孟鲁司特钠片◆", "bbox": [194, 640, 360, 676]},
	{"text": "10mg*30/瓶", "bbox": [504, 637, 625, 673]},
	{"text": "30片", "bbox": [690, 638, 738, 673]},
	{"text": "1.05", "bbox": [795, 641, 846, 672]},
	{"text": "31.53", "bbox": [865, 641, 930, 672]},
	{"text": "Sig", "bbox": [420, 695, 460, 728]},
	{"text": "10mg/次,口服,qn*30天", "bbox": [504, 692, 750, 728]}
]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=11.8s
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[375, 34, 609, 98]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-02-08, bbox=[40, 130, 278, 166]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[314, 127, 520, 163]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[606, 129, 662, 163]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[4]: text=姓名:, bbox=[40, 185, 100, 221]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[314, 182, 400, 218]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:64岁, bbox=[448, 182, 558, 218]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[7]: text=卡号:, bbox=[606, 183, 662, 218]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[8]: text=患者类型:001 支付, bbox=[40, 240, 238, 276]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[314, 239, 420, 275]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[10]: text=处方, bbox=[605, 240, 654, 275]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[11]: text=地址:, bbox=[40, 296, 96, 332]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[605, 293, 709, 329]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[40, 348, 219, 384]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[428, 407, 561, 443]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[107, 474, 154, 509]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[212, 473, 310, 509]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[503, 471, 548, 506]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[708, 471, 755, 506]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[814, 471, 861, 506]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[897, 470, 943, 505]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[61, 540, 108, 593]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[22]: text=倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120瓶, bbox=[192, 531, 738, 568]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[23]: text=221.61 221.61, bbox=[767, 534, 927, 565]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[420, 587, 460, 620]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[25]: text=2揿/次,吸入,bid*30天, bbox=[503, 585, 750, 620]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[26]: text=孟鲁司特钠片◆, bbox=[194, 640, 360, 676]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[27]: text=10mg*30/瓶, bbox=[504, 637, 625, 673]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[28]: text=30片, bbox=[690, 638, 738, 673]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[29]: text=1.05, bbox=[795, 641, 846, 672]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[30]: text=31.53, bbox=[865, 641, 930, 672]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[31]: text=Sig, bbox=[420, 695, 460, 728]
2026-08-05 04:48:48,117 INFO     29 [qwen-vl-text] coord item[32]: text=10mg/次,口服,qn*30天, bbox=[504, 692, 750, 728]
2026-08-05 04:48:48,118 INFO     29 [qwen-vl-text] page=9 — 33/33 coords, api_time=11.8s
2026-08-05 04:48:48,118 INFO     29 [qwen-vl-text] new_positions (33):
[[9, 315.75, 512.778, 20.23, 58.309999999999995], [9, 33.68, 234.076, 77.35, 98.77], [9, 264.388, 437.84, 75.565, 96.985], [9, 510.252, 557.404, 76.755, 96.985], [9, 33.68, 84.2, 110.07499999999999, 131.495], [9, 264.388, 336.8, 108.28999999999999, 129.71], [9, 377.216, 469.83599999999996, 108.28999999999999, 129.71], [9, 510.252, 557.404, 108.88499999999999, 129.71], [9, 33.68, 200.396, 142.79999999999998, 164.22], [9, 264.388, 353.64, 142.20499999999998, 163.625], [9, 509.40999999999997, 550.668, 142.79999999999998, 163.625], [9, 33.68, 80.832, 176.12, 197.54], [9, 509.40999999999997, 596.978, 174.33499999999998, 195.755], [9, 33.68, 184.398, 207.06, 228.48], [9, 360.376, 472.36199999999997, 242.165, 263.585], [9, 90.094, 129.668, 282.03, 302.85499999999996], [9, 178.504, 261.02, 281.435, 302.85499999999996], [9, 423.526, 461.416, 280.245, 301.07], [9, 596.136, 635.7099999999999, 280.245, 301.07], [9, 685.3879999999999, 724.962, 280.245, 301.07], [9, 755.274, 794.006, 279.65, 300.47499999999997], [9, 51.361999999999995, 90.93599999999999, 321.3, 352.835], [9, 161.664, 621.396, 315.945, 337.96], [9, 645.814, 780.534, 317.72999999999996, 336.175], [9, 353.64, 387.32, 349.265, 368.9], [9, 423.526, 631.5, 348.075, 368.9], [9, 163.34799999999998, 303.12, 380.79999999999995, 402.21999999999997], [9, 424.368, 526.25, 379.015, 400.435], [9, 580.98, 621.396, 379.60999999999996, 400.435], [9, 669.39, 712.332, 381.395, 399.84], [9, 728.3299999999999, 783.06, 381.395, 399.84], [9, 353.64, 387.32, 413.525, 433.15999999999997], [9, 424.368, 631.5, 411.74, 433.15999999999997]]
2026-08-05 04:48:48,118 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=15.8s
2026-08-05 04:48:48,118 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:48:48,118 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 04:48:48,118 INFO     29 [qwen-vl-text] positions(32): [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:48:48,118 INFO     29 [qwen-vl-text] page grouping: [10], lines per page: [32]
2026-08-05 04:48:48,338 INFO     29 [qwen-vl-text] page=10, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 04:48:48,339 INFO     29 [qwen-vl-text] LLM extraction start, text_len=231
2026-08-05 04:48:48,339 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:48:48,339 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 341, \"bbox_end\": 372, \"encounter_dates\": [\"2025-01-10\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-01-10\n就诊科室:内科门诊\n主诊\n性别:男\n年龄:64岁\n卡号\n患者类型:G\n医疗证号:\n处方\n地址:\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿\n221.61 221.61\nSig\n2揿/次,吸入,bid*30天\n孟鲁司特钠片\n10mg*30/瓶\n30片\n1.05\n31.53\nSig\n10mg/次,口服,qn*30天",
    "role": "user"
  }
]
[92m04:48:48 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:48:48,340 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:48:52,313 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:48:52,314 INFO     29 [qwen-vl-text] LLM output (len=680):
{
  "encounter_date": "2025-01-10",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "倍氯米松福莫特罗吸入气雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "100ug/6ug/揿",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 30,
      "quantity": "120揿",
      "notes": "2揿/次"
    },
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "qn",
      "route": "口服",
      "duration_days": 30,
      "quantity": "30片",
      "notes": "10mg/次"
    }
  ]
}
2026-08-05 04:48:52,314 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-01-10]
2026-08-05 04:48:52,316 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1610425, prompt_len=940
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共32行）
["门(急)诊处方", "就诊时间:2025-01-10", "就诊科室:内科门诊", "主诊", "性别:男", "年龄:64岁", "卡号", "患者类型:G", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿", "221.61 221.61", "Sig", "2揿/次,吸入,bid*30天", "孟鲁司特钠片", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天"]

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
2026-08-05 04:49:00,752 INFO     29 [qwen-vl-text] coord API raw response (len=1635):
[
	{"text": "门(急)诊处方", "bbox": [378, 20, 595, 83]},
	{"text": "就诊时间:2025-01-10", "bbox": [67, 110, 289, 141]},
	{"text": "就诊科室:内科门诊", "bbox": [322, 108, 514, 141]},
	{"text": "主诊", "bbox": [593, 108, 628, 141]},
	{"text": "性别:男", "bbox": [322, 158, 402, 192]},
	{"text": "年龄:64岁", "bbox": [447, 158, 548, 192]},
	{"text": "卡号", "bbox": [593, 158, 628, 192]},
	{"text": "患者类型:G", "bbox": [70, 211, 187, 244]},
	{"text": "医疗证号:", "bbox": [322, 211, 420, 244]},
	{"text": "处方", "bbox": [592, 211, 628, 244]},
	{"text": "地址:", "bbox": [70, 262, 120, 295]},
	{"text": "身份证号:", "bbox": [593, 262, 689, 295]},
	{"text": "诊断:支气管哮喘", "bbox": [71, 309, 237, 344]},
	{"text": "西药处方", "bbox": [428, 368, 551, 401]},
	{"text": "组号", "bbox": [131, 427, 175, 460]},
	{"text": "项目名称", "bbox": [228, 427, 319, 460]},
	{"text": "规格", "bbox": [498, 427, 539, 460]},
	{"text": "总量", "bbox": [690, 427, 732, 460]},
	{"text": "单价", "bbox": [787, 427, 829, 460]},
	{"text": "金额", "bbox": [863, 427, 906, 460]},
	{"text": "R:", "bbox": [90, 488, 133, 538]},
	{"text": "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿", "bbox": [210, 483, 716, 516]},
	{"text": "221.61 221.61", "bbox": [743, 488, 892, 516]},
	{"text": "Sig", "bbox": [422, 534, 458, 566]},
	{"text": "2揿/次,吸入,bid*30天", "bbox": [497, 534, 727, 566]},
	{"text": "孟鲁司特钠片", "bbox": [212, 582, 348, 615]},
	{"text": "10mg*30/瓶", "bbox": [498, 582, 611, 615]},
	{"text": "30片", "bbox": [671, 582, 715, 615]},
	{"text": "1.05", "bbox": [768, 587, 814, 613]},
	{"text": "31.53", "bbox": [833, 587, 892, 613]},
	{"text": "Sig", "bbox": [422, 634, 458, 666]},
	{"text": "10mg/次,口服,qn*30天", "bbox": [498, 634, 727, 666]}
]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord API: raw_items=32, valid_items=32, elapsed=8.4s
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[378, 20, 595, 83]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-01-10, bbox=[67, 110, 289, 141]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[322, 108, 514, 141]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[593, 108, 628, 141]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[4]: text=性别:男, bbox=[322, 158, 402, 192]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[5]: text=年龄:64岁, bbox=[447, 158, 548, 192]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[6]: text=卡号, bbox=[593, 158, 628, 192]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[7]: text=患者类型:G, bbox=[70, 211, 187, 244]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[8]: text=医疗证号:, bbox=[322, 211, 420, 244]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[9]: text=处方, bbox=[592, 211, 628, 244]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[10]: text=地址:, bbox=[70, 262, 120, 295]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[11]: text=身份证号:, bbox=[593, 262, 689, 295]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[12]: text=诊断:支气管哮喘, bbox=[71, 309, 237, 344]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[13]: text=西药处方, bbox=[428, 368, 551, 401]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[14]: text=组号, bbox=[131, 427, 175, 460]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[15]: text=项目名称, bbox=[228, 427, 319, 460]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[16]: text=规格, bbox=[498, 427, 539, 460]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[17]: text=总量, bbox=[690, 427, 732, 460]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[18]: text=单价, bbox=[787, 427, 829, 460]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[19]: text=金额, bbox=[863, 427, 906, 460]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[20]: text=R:, bbox=[90, 488, 133, 538]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[21]: text=倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿, bbox=[210, 483, 716, 516]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[22]: text=221.61 221.61, bbox=[743, 488, 892, 516]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[23]: text=Sig, bbox=[422, 534, 458, 566]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[24]: text=2揿/次,吸入,bid*30天, bbox=[497, 534, 727, 566]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[25]: text=孟鲁司特钠片, bbox=[212, 582, 348, 615]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[26]: text=10mg*30/瓶, bbox=[498, 582, 611, 615]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[27]: text=30片, bbox=[671, 582, 715, 615]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[28]: text=1.05, bbox=[768, 587, 814, 613]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[29]: text=31.53, bbox=[833, 587, 892, 613]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[30]: text=Sig, bbox=[422, 634, 458, 666]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] coord item[31]: text=10mg/次,口服,qn*30天, bbox=[498, 634, 727, 666]
2026-08-05 04:49:00,753 INFO     29 [qwen-vl-text] page=10 — 32/32 coords, api_time=8.4s
2026-08-05 04:49:00,754 INFO     29 [qwen-vl-text] new_positions (32):
[[10, 318.276, 500.99, 11.899999999999999, 49.385], [10, 56.414, 243.338, 65.45, 83.895], [10, 271.12399999999997, 432.788, 64.25999999999999, 83.895], [10, 499.306, 528.776, 64.25999999999999, 83.895], [10, 271.12399999999997, 338.484, 94.00999999999999, 114.24], [10, 376.37399999999997, 461.416, 94.00999999999999, 114.24], [10, 499.306, 528.776, 94.00999999999999, 114.24], [10, 58.94, 157.454, 125.54499999999999, 145.18], [10, 271.12399999999997, 353.64, 125.54499999999999, 145.18], [10, 498.464, 528.776, 125.54499999999999, 145.18], [10, 58.94, 101.03999999999999, 155.89, 175.525], [10, 499.306, 580.138, 155.89, 175.525], [10, 59.782, 199.554, 183.855, 204.67999999999998], [10, 360.376, 463.942, 218.95999999999998, 238.595], [10, 110.30199999999999, 147.35, 254.065, 273.7], [10, 191.976, 268.598, 254.065, 273.7], [10, 419.316, 453.83799999999997, 254.065, 273.7], [10, 580.98, 616.3439999999999, 254.065, 273.7], [10, 662.654, 698.018, 254.065, 273.7], [10, 726.646, 762.852, 254.065, 273.7], [10, 75.78, 111.98599999999999, 290.36, 320.11], [10, 176.82, 602.872, 287.385, 307.02], [10, 625.606, 751.064, 290.36, 307.02], [10, 355.324, 385.63599999999997, 317.72999999999996, 336.77], [10, 418.474, 612.134, 317.72999999999996, 336.77], [10, 178.504, 293.01599999999996, 346.28999999999996, 365.925], [10, 419.316, 514.462, 346.28999999999996, 365.925], [10, 564.982, 602.03, 346.28999999999996, 365.925], [10, 646.656, 685.3879999999999, 349.265, 364.73499999999996], [10, 701.386, 751.064, 349.265, 364.73499999999996], [10, 355.324, 385.63599999999997, 377.22999999999996, 396.27], [10, 419.316, 612.134, 377.22999999999996, 396.27]]
2026-08-05 04:49:00,754 INFO     29 [qwen-vl-text] ═══ DONE ═══ 32 positions, pages=1, time=12.6s
2026-08-05 04:49:00,754 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:49:00,754 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 04:49:00,754 INFO     29 [qwen-vl-text] positions(33): [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:49:00,754 INFO     29 [qwen-vl-text] page grouping: [11], lines per page: [33]
2026-08-05 04:49:00,924 INFO     29 [qwen-vl-text] page=11, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 04:49:00,925 INFO     29 [qwen-vl-text] LLM extraction start, text_len=240
2026-08-05 04:49:00,925 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:49:00,926 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 373, \"bbox_end\": 405, \"encounter_dates\": [\"2024-12-11\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2024-12-11\n就诊科室:内科门诊\n主诊\n姓名:\n性别:男\n年龄:64岁\n卡号\n患者类型:GCP支付\n医疗证号:\n处方\n地址:\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n倍氯米松福莫特罗吸入气雾剂100ug/6ug/瓶*120瓶\n221.61 221.61\nSig\n2揿/次,吸入,bid*30天\n孟鲁司特钠片◆\n10mg*30/瓶\n30片\n1.05\n31.53\nSig\n10mg/次,口服,qn*30天",
    "role": "user"
  }
]
[92m04:49:00 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:49:00,927 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:49:00,928 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:49:00.926+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 10, "failed": 0, "current": {"333155a8908811f1a3da71efcdd7cc1f": {"id": "333155a8908811f1a3da71efcdd7cc1f", "doc_id": "32f80906908811f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412392, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905007404, "task_type": "dataflow", "root_trace_id": "8cc21299ba8c4c4f9376bb5b55f5585f", "root_traceparent": "00-8cc21299ba8c4c4f9376bb5b55f5585f-3809269866d439b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:49:04,066 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:49:04,066 INFO     29 [qwen-vl-text] LLM output (len=676):
{
  "encounter_date": "2024-12-11",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "倍氯米松福莫特罗吸入气雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "100ug/6ug",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 30,
      "quantity": "1瓶",
      "notes": "2揿/次"
    },
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "qn",
      "route": "口服",
      "duration_days": 30,
      "quantity": "30片",
      "notes": "10mg/次"
    }
  ]
}
2026-08-05 04:49:04,066 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-12-11]
2026-08-05 04:49:04,069 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1414362, prompt_len=952
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["门(急)诊处方", "就诊时间:2024-12-11", "就诊科室:内科门诊", "主诊", "姓名:", "性别:男", "年龄:64岁", "卡号", "患者类型:GCP支付", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂100ug/6ug/瓶*120瓶", "221.61 221.61", "Sig", "2揿/次,吸入,bid*30天", "孟鲁司特钠片◆", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天"]

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
2026-08-05 04:49:12,908 INFO     29 [qwen-vl-text] coord API raw response (len=1688):
[
	{"text": "门(急)诊处方", "bbox": [394, 33, 612, 92]},
	{"text": "就诊时间:2024-12-11", "bbox": [77, 117, 300, 150]},
	{"text": "就诊科室:内科门诊", "bbox": [336, 117, 530, 150]},
	{"text": "主诊", "bbox": [610, 120, 650, 152]},
	{"text": "姓名:", "bbox": [77, 168, 132, 201]},
	{"text": "性别:男", "bbox": [338, 168, 417, 201]},
	{"text": "年龄:64岁", "bbox": [464, 169, 566, 201]},
	{"text": "卡号", "bbox": [611, 170, 650, 201]},
	{"text": "患者类型:GCP支付", "bbox": [80, 219, 267, 252]},
	{"text": "医疗证号:", "bbox": [339, 220, 437, 253]},
	{"text": "处方", "bbox": [610, 223, 650, 255]},
	{"text": "地址:", "bbox": [81, 269, 133, 302]},
	{"text": "身份证号:", "bbox": [610, 271, 707, 304]},
	{"text": "诊断:支气管哮喘", "bbox": [84, 317, 251, 350]},
	{"text": "西药处方", "bbox": [447, 375, 570, 407]},
	{"text": "组号", "bbox": [146, 432, 191, 464]},
	{"text": "项目名称", "bbox": [246, 432, 337, 464]},
	{"text": "规格", "bbox": [517, 432, 558, 464]},
	{"text": "总量", "bbox": [708, 434, 751, 466]},
	{"text": "单价", "bbox": [805, 434, 848, 466]},
	{"text": "金额", "bbox": [880, 434, 922, 466]},
	{"text": "R:", "bbox": [104, 492, 147, 540]},
	{"text": "倍氯米松福莫特罗吸入气雾剂100ug/6ug/瓶*120瓶", "bbox": [227, 487, 735, 520]},
	{"text": "221.61 221.61", "bbox": [762, 490, 908, 517]},
	{"text": "Sig", "bbox": [440, 537, 476, 567]},
	{"text": "2揿/次,吸入,bid*30天", "bbox": [515, 536, 745, 567]},
	{"text": "孟鲁司特钠片◆", "bbox": [228, 584, 383, 616]},
	{"text": "10mg*30/瓶", "bbox": [517, 582, 629, 614]},
	{"text": "30片", "bbox": [688, 583, 732, 613]},
	{"text": "1.05", "bbox": [785, 585, 833, 612]},
	{"text": "31.53", "bbox": [851, 585, 910, 612]},
	{"text": "Sig", "bbox": [440, 633, 476, 663]},
	{"text": "10mg/次,口服,qn*30天", "bbox": [517, 631, 744, 663]}
]
2026-08-05 04:49:12,908 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=8.8s
2026-08-05 04:49:12,908 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[394, 33, 612, 92]
2026-08-05 04:49:12,908 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2024-12-11, bbox=[77, 117, 300, 150]
2026-08-05 04:49:12,908 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[336, 117, 530, 150]
2026-08-05 04:49:12,908 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[610, 120, 650, 152]
2026-08-05 04:49:12,908 INFO     29 [qwen-vl-text] coord item[4]: text=姓名:, bbox=[77, 168, 132, 201]
2026-08-05 04:49:12,908 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[338, 168, 417, 201]
2026-08-05 04:49:12,908 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:64岁, bbox=[464, 169, 566, 201]
2026-08-05 04:49:12,908 INFO     29 [qwen-vl-text] coord item[7]: text=卡号, bbox=[611, 170, 650, 201]
2026-08-05 04:49:12,908 INFO     29 [qwen-vl-text] coord item[8]: text=患者类型:GCP支付, bbox=[80, 219, 267, 252]
2026-08-05 04:49:12,908 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[339, 220, 437, 253]
2026-08-05 04:49:12,908 INFO     29 [qwen-vl-text] coord item[10]: text=处方, bbox=[610, 223, 650, 255]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[11]: text=地址:, bbox=[81, 269, 133, 302]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[610, 271, 707, 304]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[84, 317, 251, 350]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[447, 375, 570, 407]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[146, 432, 191, 464]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[246, 432, 337, 464]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[517, 432, 558, 464]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[708, 434, 751, 466]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[805, 434, 848, 466]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[880, 434, 922, 466]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[104, 492, 147, 540]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[22]: text=倍氯米松福莫特罗吸入气雾剂100ug/6ug/瓶*120瓶, bbox=[227, 487, 735, 520]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[23]: text=221.61 221.61, bbox=[762, 490, 908, 517]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[440, 537, 476, 567]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[25]: text=2揿/次,吸入,bid*30天, bbox=[515, 536, 745, 567]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[26]: text=孟鲁司特钠片◆, bbox=[228, 584, 383, 616]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[27]: text=10mg*30/瓶, bbox=[517, 582, 629, 614]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[28]: text=30片, bbox=[688, 583, 732, 613]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[29]: text=1.05, bbox=[785, 585, 833, 612]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[30]: text=31.53, bbox=[851, 585, 910, 612]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[31]: text=Sig, bbox=[440, 633, 476, 663]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] coord item[32]: text=10mg/次,口服,qn*30天, bbox=[517, 631, 744, 663]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] page=11 — 33/33 coords, api_time=8.8s
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] new_positions (33):
[[11, 331.748, 515.304, 19.634999999999998, 54.739999999999995], [11, 64.834, 252.6, 69.615, 89.25], [11, 282.912, 446.26, 69.615, 89.25], [11, 513.62, 547.3, 71.39999999999999, 90.44], [11, 64.834, 111.14399999999999, 99.96, 119.595], [11, 284.596, 351.114, 99.96, 119.595], [11, 390.688, 476.572, 100.55499999999999, 119.595], [11, 514.462, 547.3, 101.14999999999999, 119.595], [11, 67.36, 224.814, 130.305, 149.94], [11, 285.438, 367.954, 130.9, 150.535], [11, 513.62, 547.3, 132.685, 151.725], [11, 68.202, 111.98599999999999, 160.055, 179.69], [11, 513.62, 595.294, 161.245, 180.88], [11, 70.728, 211.34199999999998, 188.61499999999998, 208.25], [11, 376.37399999999997, 479.94, 223.125, 242.165], [11, 122.932, 160.822, 257.03999999999996, 276.08], [11, 207.132, 283.75399999999996, 257.03999999999996, 276.08], [11, 435.31399999999996, 469.83599999999996, 257.03999999999996, 276.08], [11, 596.136, 632.342, 258.22999999999996, 277.27], [11, 677.81, 714.016, 258.22999999999996, 277.27], [11, 740.9599999999999, 776.324, 258.22999999999996, 277.27], [11, 87.568, 123.774, 292.74, 321.3], [11, 191.134, 618.87, 289.765, 309.4], [11, 641.6039999999999, 764.536, 291.55, 307.615], [11, 370.47999999999996, 400.792, 319.515, 337.365], [11, 433.63, 627.29, 318.91999999999996, 337.365], [11, 191.976, 322.486, 347.47999999999996, 366.52], [11, 435.31399999999996, 529.6179999999999, 346.28999999999996, 365.33], [11, 579.2959999999999, 616.3439999999999, 346.885, 364.73499999999996], [11, 660.97, 701.386, 348.075, 364.14], [11, 716.542, 766.22, 348.075, 364.14], [11, 370.47999999999996, 400.792, 376.635, 394.48499999999996], [11, 435.31399999999996, 626.448, 375.445, 394.48499999999996]]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=12.2s
2026-08-05 04:49:12,909 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] positions(33): [[12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:49:12,909 INFO     29 [qwen-vl-text] page grouping: [12], lines per page: [33]
2026-08-05 04:49:13,109 INFO     29 [qwen-vl-text] page=12, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 04:49:13,111 INFO     29 [qwen-vl-text] LLM extraction start, text_len=243
2026-08-05 04:49:13,111 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:49:13,111 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 408, \"bbox_end\": 440, \"encounter_dates\": [\"2024-11-18\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2024-11-18\n就诊科室:内科门诊\n主诊\n姓名\n性别:男\n年龄:63岁\n卡号:\n患者类型:GLP支付\n医疗证号:\n处方\n地址:\n身份证号:\n诊断:支气管哮喘,非危重\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿\n221.61 221.61\nSig\n2揿/次,吸入,bid*30天\n孟鲁司特钠片\n10mg*30/瓶\n30片\n1.05\n31.53\nSig\n10mg/次,口服,qn*30天",
    "role": "user"
  }
]
[92m04:49:13 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:49:13,113 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:49:19,929 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:49:19,930 INFO     29 [qwen-vl-text] LLM output (len=684):
{
  "encounter_date": "2024-11-18",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘,非危重",
  "items": [
    {
      "drug_generic_name": "倍氯米松福莫特罗吸入气雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "100ug/6ug/揿",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 30,
      "quantity": "120揿",
      "notes": "2揿/次"
    },
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "qn",
      "route": "口服",
      "duration_days": 30,
      "quantity": "30片",
      "notes": "10mg/次"
    }
  ]
}
2026-08-05 04:49:19,930 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-11-18]
2026-08-05 04:49:19,931 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1479468, prompt_len=955
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["门(急)诊处方", "就诊时间:2024-11-18", "就诊科室:内科门诊", "主诊", "姓名", "性别:男", "年龄:63岁", "卡号:", "患者类型:GLP支付", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘,非危重", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿", "221.61 221.61", "Sig", "2揿/次,吸入,bid*30天", "孟鲁司特钠片", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天"]

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
2026-08-05 04:49:28,643 INFO     29 [qwen-vl-text] coord API raw response (len=1691):
[
	{"text": "门(急)诊处方", "bbox": [383, 26, 592, 85]},
	{"text": "就诊时间:2024-11-18", "bbox": [80, 112, 294, 144]},
	{"text": "就诊科室:内科门诊", "bbox": [325, 110, 513, 142]},
	{"text": "主诊", "bbox": [590, 110, 644, 142]},
	{"text": "姓名", "bbox": [80, 163, 118, 195]},
	{"text": "性别:男", "bbox": [325, 160, 403, 192]},
	{"text": "年龄:63岁", "bbox": [447, 160, 547, 192]},
	{"text": "卡号:", "bbox": [590, 160, 640, 192]},
	{"text": "患者类型:GLP支付", "bbox": [80, 214, 257, 245]},
	{"text": "医疗证号:", "bbox": [325, 211, 421, 243]},
	{"text": "处方", "bbox": [590, 211, 640, 243]},
	{"text": "地址:", "bbox": [80, 263, 130, 295]},
	{"text": "身份证号:", "bbox": [590, 260, 685, 292]},
	{"text": "诊断:支气管哮喘,非危重", "bbox": [81, 309, 331, 343]},
	{"text": "西药处方", "bbox": [430, 366, 551, 398]},
	{"text": "组号", "bbox": [140, 425, 183, 458]},
	{"text": "项目名称", "bbox": [235, 425, 323, 458]},
	{"text": "规格", "bbox": [498, 423, 539, 455]},
	{"text": "总量", "bbox": [687, 425, 728, 458]},
	{"text": "单价", "bbox": [780, 423, 822, 455]},
	{"text": "金额", "bbox": [855, 423, 898, 455]},
	{"text": "R:", "bbox": [100, 487, 142, 535]},
	{"text": "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿", "bbox": [217, 480, 713, 513]},
	{"text": "221.61 221.61", "bbox": [738, 480, 884, 510]},
	{"text": "Sig", "bbox": [424, 531, 460, 563]},
	{"text": "2揿/次,吸入,bid*30天", "bbox": [498, 529, 723, 561]},
	{"text": "孟鲁司特钠片", "bbox": [220, 580, 350, 612]},
	{"text": "10mg*30/瓶", "bbox": [500, 577, 610, 610]},
	{"text": "30片", "bbox": [668, 577, 711, 608]},
	{"text": "1.05", "bbox": [763, 577, 808, 607]},
	{"text": "31.53", "bbox": [826, 577, 885, 607]},
	{"text": "Sig", "bbox": [424, 631, 460, 663]},
	{"text": "10mg/次,口服,qn*30天", "bbox": [500, 627, 723, 660]}
]
2026-08-05 04:49:28,643 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=8.7s
2026-08-05 04:49:28,643 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[383, 26, 592, 85]
2026-08-05 04:49:28,643 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2024-11-18, bbox=[80, 112, 294, 144]
2026-08-05 04:49:28,643 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[325, 110, 513, 142]
2026-08-05 04:49:28,643 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[590, 110, 644, 142]
2026-08-05 04:49:28,643 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[80, 163, 118, 195]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[325, 160, 403, 192]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:63岁, bbox=[447, 160, 547, 192]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[7]: text=卡号:, bbox=[590, 160, 640, 192]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[8]: text=患者类型:GLP支付, bbox=[80, 214, 257, 245]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[325, 211, 421, 243]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[10]: text=处方, bbox=[590, 211, 640, 243]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[11]: text=地址:, bbox=[80, 263, 130, 295]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[590, 260, 685, 292]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘,非危重, bbox=[81, 309, 331, 343]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[430, 366, 551, 398]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[140, 425, 183, 458]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[235, 425, 323, 458]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[498, 423, 539, 455]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[687, 425, 728, 458]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[780, 423, 822, 455]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[855, 423, 898, 455]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[100, 487, 142, 535]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[22]: text=倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿, bbox=[217, 480, 713, 513]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[23]: text=221.61 221.61, bbox=[738, 480, 884, 510]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[424, 531, 460, 563]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[25]: text=2揿/次,吸入,bid*30天, bbox=[498, 529, 723, 561]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[26]: text=孟鲁司特钠片, bbox=[220, 580, 350, 612]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[27]: text=10mg*30/瓶, bbox=[500, 577, 610, 610]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[28]: text=30片, bbox=[668, 577, 711, 608]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[29]: text=1.05, bbox=[763, 577, 808, 607]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[30]: text=31.53, bbox=[826, 577, 885, 607]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[31]: text=Sig, bbox=[424, 631, 460, 663]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] coord item[32]: text=10mg/次,口服,qn*30天, bbox=[500, 627, 723, 660]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] page=12 — 33/33 coords, api_time=8.7s
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] new_positions (33):
[[12, 322.486, 498.464, 15.469999999999999, 50.574999999999996], [12, 67.36, 247.548, 66.64, 85.67999999999999], [12, 273.65, 431.94599999999997, 65.45, 84.49], [12, 496.78, 542.2479999999999, 65.45, 84.49], [12, 67.36, 99.356, 96.985, 116.02499999999999], [12, 273.65, 339.32599999999996, 95.19999999999999, 114.24], [12, 376.37399999999997, 460.574, 95.19999999999999, 114.24], [12, 496.78, 538.88, 95.19999999999999, 114.24], [12, 67.36, 216.394, 127.33, 145.775], [12, 273.65, 354.48199999999997, 125.54499999999999, 144.58499999999998], [12, 496.78, 538.88, 125.54499999999999, 144.58499999999998], [12, 67.36, 109.46, 156.48499999999999, 175.525], [12, 496.78, 576.77, 154.7, 173.73999999999998], [12, 68.202, 278.702, 183.855, 204.08499999999998], [12, 362.06, 463.942, 217.76999999999998, 236.81], [12, 117.88, 154.08599999999998, 252.875, 272.51], [12, 197.87, 271.966, 252.875, 272.51], [12, 419.316, 453.83799999999997, 251.685, 270.72499999999997], [12, 578.454, 612.976, 252.875, 272.51], [12, 656.76, 692.124, 251.685, 270.72499999999997], [12, 719.91, 756.116, 251.685, 270.72499999999997], [12, 84.2, 119.564, 289.765, 318.325], [12, 182.714, 600.346, 285.59999999999997, 305.235], [12, 621.396, 744.328, 285.59999999999997, 303.45], [12, 357.008, 387.32, 315.945, 334.98499999999996], [12, 419.316, 608.766, 314.755, 333.79499999999996], [12, 185.23999999999998, 294.7, 345.09999999999997, 364.14], [12, 421.0, 513.62, 343.315, 362.95], [12, 562.456, 598.662, 343.315, 361.76], [12, 642.446, 680.336, 343.315, 361.16499999999996], [12, 695.492, 745.17, 343.315, 361.16499999999996], [12, 357.008, 387.32, 375.445, 394.48499999999996], [12, 421.0, 608.766, 373.065, 392.7]]
2026-08-05 04:49:28,644 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=15.7s
2026-08-05 04:49:28,645 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:49:28,645 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 04:49:28,645 INFO     29 [qwen-vl-text] positions(29): [[14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:49:28,645 INFO     29 [qwen-vl-text] page grouping: [14], lines per page: [29]
2026-08-05 04:49:28,827 INFO     29 [qwen-vl-text] page=14, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 04:49:28,828 INFO     29 [qwen-vl-text] LLM extraction start, text_len=272
2026-08-05 04:49:28,828 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:49:28,829 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 481, \"bbox_end\": 509, \"encounter_dates\": [\"2026-01-06\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "处方笺\n普通\n诊疗\n患者姓\n男\n年龄：65岁\n费别：\n科室：\n2026-01-06 11:28:26\n处方号\n地址：\n联系电\n身份号\n诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎\nR\nP:\n倍氯米松福莫特罗吸入气雾剂◆① 100ug/6ug/揿*120\n1瓶\n剂量：每次2揿 ( 1/60 瓶 )\n用法：吸入用药\nbid 01-06\n孟鲁司特钠片(省采)◆\n10mg*5/盒\n30片\n剂量：每次10mg (1 片 )\n用法：口服\nqd 01-06\n处方金额：298.47元\n取药药房：门诊西药房（荔湾）",
    "role": "user"
  }
]
[92m04:49:28 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:49:28,830 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:49:32,745 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:49:32,745 INFO     29 [qwen-vl-text] LLM output (len=706):
{
  "encounter_date": "2026-01-06",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": null,
  "diagnosis": "支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎",
  "items": [
    {
      "drug_generic_name": "倍氯米松福莫特罗吸入气雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "每次2揿",
      "frequency": "bid",
      "route": "吸入用药",
      "duration_days": null,
      "quantity": "1瓶",
      "notes": null
    },
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "每次10mg",
      "frequency": "qd",
      "route": "口服",
      "duration_days": null,
      "quantity": "30片",
      "notes": null
    }
  ]
}
2026-08-05 04:49:32,745 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-06]
2026-08-05 04:49:32,747 INFO     29 [qwen-vl-text] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=858191, prompt_len=972
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["处方笺", "普通", "诊疗", "患者姓", "男", "年龄：65岁", "费别：", "科室：", "2026-01-06 11:28:26", "处方号", "地址：", "联系电", "身份号", "诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎", "R", "P:", "倍氯米松福莫特罗吸入气雾剂◆① 100ug/6ug/揿*120", "1瓶", "剂量：每次2揿 ( 1/60 瓶 )", "用法：吸入用药", "bid 01-06", "孟鲁司特钠片(省采)◆", "10mg*5/盒", "30片", "剂量：每次10mg (1 片 )", "用法：口服", "qd 01-06", "处方金额：298.47元", "取药药房：门诊西药房（荔湾）"]

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
2026-08-05 04:49:41,114 INFO     29 [qwen-vl-text] coord API raw response (len=1546):
[
	{"text": "处方笺", "bbox": [397, 8, 473, 41]},
	{"text": "普通", "bbox": [643, 54, 671, 74]},
	{"text": "诊疗", "bbox": [229, 115, 260, 135]},
	{"text": "患者姓", "bbox": [229, 149, 264, 167]},
	{"text": "男", "bbox": [412, 145, 424, 163]},
	{"text": "年龄：65岁", "bbox": [452, 143, 517, 161]},
	{"text": "费别：", "bbox": [564, 143, 595, 161]},
	{"text": "科室：", "bbox": [229, 181, 257, 199]},
	{"text": "2026-01-06 11:28:26", "bbox": [411, 177, 535, 194]},
	{"text": "处方号", "bbox": [564, 175, 600, 194]},
	{"text": "地址：", "bbox": [229, 210, 257, 228]},
	{"text": "联系电", "bbox": [563, 207, 600, 226]},
	{"text": "身份号", "bbox": [229, 241, 264, 260]},
	{"text": "诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎", "bbox": [230, 261, 720, 283]},
	{"text": "R", "bbox": [243, 315, 267, 354]},
	{"text": "P:", "bbox": [265, 331, 277, 349]},
	{"text": "倍氯米松福莫特罗吸入气雾剂◆① 100ug/6ug/揿*120", "bbox": [246, 373, 564, 394]},
	{"text": "1瓶", "bbox": [603, 376, 620, 392]},
	{"text": "剂量：每次2揿 ( 1/60 瓶 )", "bbox": [297, 405, 445, 431]},
	{"text": "用法：吸入用药", "bbox": [470, 409, 551, 426]},
	{"text": "bid 01-06", "bbox": [580, 411, 648, 428]},
	{"text": "孟鲁司特钠片(省采)◆", "bbox": [247, 472, 376, 490]},
	{"text": "10mg*5/盒", "bbox": [460, 473, 516, 490]},
	{"text": "30片", "bbox": [597, 474, 620, 489]},
	{"text": "剂量：每次10mg (1 片 )", "bbox": [298, 503, 444, 520]},
	{"text": "用法：口服", "bbox": [469, 504, 523, 520]},
	{"text": "qd 01-06", "bbox": [576, 507, 641, 522]},
	{"text": "处方金额：298.47元", "bbox": [251, 878, 394, 900]},
	{"text": "取药药房：门诊西药房（荔湾）", "bbox": [492, 877, 680, 898]}
]
2026-08-05 04:49:41,115 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=8.4s
2026-08-05 04:49:41,115 INFO     29 [qwen-vl-text] coord item[0]: text=处方笺, bbox=[397, 8, 473, 41]
2026-08-05 04:49:41,115 INFO     29 [qwen-vl-text] coord item[1]: text=普通, bbox=[643, 54, 671, 74]
2026-08-05 04:49:41,116 INFO     29 [qwen-vl-text] coord item[2]: text=诊疗, bbox=[229, 115, 260, 135]
2026-08-05 04:49:41,116 INFO     29 [qwen-vl-text] coord item[3]: text=患者姓, bbox=[229, 149, 264, 167]
2026-08-05 04:49:41,116 INFO     29 [qwen-vl-text] coord item[4]: text=男, bbox=[412, 145, 424, 163]
2026-08-05 04:49:41,116 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：65岁, bbox=[452, 143, 517, 161]
2026-08-05 04:49:41,116 INFO     29 [qwen-vl-text] coord item[6]: text=费别：, bbox=[564, 143, 595, 161]
2026-08-05 04:49:41,116 INFO     29 [qwen-vl-text] coord item[7]: text=科室：, bbox=[229, 181, 257, 199]
2026-08-05 04:49:41,116 INFO     29 [qwen-vl-text] coord item[8]: text=2026-01-06 11:28:26, bbox=[411, 177, 535, 194]
2026-08-05 04:49:41,116 INFO     29 [qwen-vl-text] coord item[9]: text=处方号, bbox=[564, 175, 600, 194]
2026-08-05 04:49:41,116 INFO     29 [qwen-vl-text] coord item[10]: text=地址：, bbox=[229, 210, 257, 228]
2026-08-05 04:49:41,116 INFO     29 [qwen-vl-text] coord item[11]: text=联系电, bbox=[563, 207, 600, 226]
2026-08-05 04:49:41,116 INFO     29 [qwen-vl-text] coord item[12]: text=身份号, bbox=[229, 241, 264, 260]
2026-08-05 04:49:41,116 INFO     29 [qwen-vl-text] coord item[13]: text=诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎, bbox=[230, 261, 720, 283]
2026-08-05 04:49:41,116 INFO     29 [qwen-vl-text] coord item[14]: text=R, bbox=[243, 315, 267, 354]
2026-08-05 04:49:41,117 INFO     29 [qwen-vl-text] coord item[15]: text=P:, bbox=[265, 331, 277, 349]
2026-08-05 04:49:41,117 INFO     29 [qwen-vl-text] coord item[16]: text=倍氯米松福莫特罗吸入气雾剂◆① 100ug/6ug/揿*120, bbox=[246, 373, 564, 394]
2026-08-05 04:49:41,117 INFO     29 [qwen-vl-text] coord item[17]: text=1瓶, bbox=[603, 376, 620, 392]
2026-08-05 04:49:41,117 INFO     29 [qwen-vl-text] coord item[18]: text=剂量：每次2揿 ( 1/60 瓶 ), bbox=[297, 405, 445, 431]
2026-08-05 04:49:41,117 INFO     29 [qwen-vl-text] coord item[19]: text=用法：吸入用药, bbox=[470, 409, 551, 426]
2026-08-05 04:49:41,117 INFO     29 [qwen-vl-text] coord item[20]: text=bid 01-06, bbox=[580, 411, 648, 428]
2026-08-05 04:49:41,117 INFO     29 [qwen-vl-text] coord item[21]: text=孟鲁司特钠片(省采)◆, bbox=[247, 472, 376, 490]
2026-08-05 04:49:41,117 INFO     29 [qwen-vl-text] coord item[22]: text=10mg*5/盒, bbox=[460, 473, 516, 490]
2026-08-05 04:49:41,117 INFO     29 [qwen-vl-text] coord item[23]: text=30片, bbox=[597, 474, 620, 489]
2026-08-05 04:49:41,117 INFO     29 [qwen-vl-text] coord item[24]: text=剂量：每次10mg (1 片 ), bbox=[298, 503, 444, 520]
2026-08-05 04:49:41,117 INFO     29 [qwen-vl-text] coord item[25]: text=用法：口服, bbox=[469, 504, 523, 520]
2026-08-05 04:49:41,117 INFO     29 [qwen-vl-text] coord item[26]: text=qd 01-06, bbox=[576, 507, 641, 522]
2026-08-05 04:49:41,117 INFO     29 [qwen-vl-text] coord item[27]: text=处方金额：298.47元, bbox=[251, 878, 394, 900]
2026-08-05 04:49:41,117 INFO     29 [qwen-vl-text] coord item[28]: text=取药药房：门诊西药房（荔湾）, bbox=[492, 877, 680, 898]
2026-08-05 04:49:41,118 INFO     29 [qwen-vl-text] page=14 — 29/29 coords, api_time=8.4s
2026-08-05 04:49:41,118 INFO     29 [qwen-vl-text] new_positions (29):
[[14, 334.274, 398.26599999999996, 4.76, 24.395], [14, 541.406, 564.982, 32.129999999999995, 44.03], [14, 192.81799999999998, 218.92, 68.425, 80.325], [14, 192.81799999999998, 222.28799999999998, 88.655, 99.365], [14, 346.904, 357.008, 86.27499999999999, 96.985], [14, 380.584, 435.31399999999996, 85.085, 95.795], [14, 474.888, 500.99, 85.085, 95.795], [14, 192.81799999999998, 216.394, 107.695, 118.405], [14, 346.062, 450.46999999999997, 105.315, 115.42999999999999], [14, 474.888, 505.2, 104.125, 115.42999999999999], [14, 192.81799999999998, 216.394, 124.94999999999999, 135.66], [14, 474.046, 505.2, 123.16499999999999, 134.47], [14, 192.81799999999998, 222.28799999999998, 143.39499999999998, 154.7], [14, 193.66, 606.24, 155.295, 168.385], [14, 204.606, 224.814, 187.42499999999998, 210.63], [14, 223.13, 233.23399999999998, 196.945, 207.655], [14, 207.132, 474.888, 221.935, 234.42999999999998], [14, 507.726, 522.04, 223.72, 233.23999999999998], [14, 250.07399999999998, 374.69, 240.975, 256.445], [14, 395.74, 463.942, 243.355, 253.47], [14, 488.35999999999996, 545.616, 244.545, 254.66], [14, 207.974, 316.592, 280.84, 291.55], [14, 387.32, 434.472, 281.435, 291.55], [14, 502.674, 522.04, 282.03, 290.955], [14, 250.916, 373.848, 299.28499999999997, 309.4], [14, 394.89799999999997, 440.366, 299.88, 309.4], [14, 484.99199999999996, 539.722, 301.66499999999996, 310.59], [14, 211.34199999999998, 331.748, 522.41, 535.5], [14, 414.264, 572.56, 521.8149999999999, 534.31]]
2026-08-05 04:49:41,118 INFO     29 [qwen-vl-text] ═══ DONE ═══ 29 positions, pages=1, time=12.5s
2026-08-05 04:49:41,118 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:49:41,118 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 04:49:41,118 INFO     29 [qwen-vl-text] positions(40): [[15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:49:41,119 INFO     29 [qwen-vl-text] page grouping: [15], lines per page: [40]
2026-08-05 04:49:41,338 INFO     29 [qwen-vl-text] page=15, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 04:49:41,339 INFO     29 [qwen-vl-text] LLM extraction start, text_len=306
2026-08-05 04:49:41,340 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:49:41,340 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 510, \"bbox_end\": 549, \"encounter_dates\": [\"2026-01-06\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "处方笺\n普通\n诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎\n患者\n年龄：65岁\n费别\n科室\n6-01-06 11:31:02\n处方\n地址\n联系\n身份\nRp:\n左氧氟沙星片(省采)●⑥\n0.5g*28片/盒\n3片\n剂量：每次0.5g\n(1 片)\n用法：口服\nqd\n01-06\n醋酸泼尼松片●②⑥\n5mg*100/瓶\n6片\n剂量：每次10mg\n(2 片)\n用法：口服\nqm\n01-06\n盐酸氨溴索分散片(省采)●⑥\n30mg*50/盒\n15片\n剂量：每次30mg\n(1 片)\n用法：餐后口服\ntid\n01-06\n处方金额：3.47元\n取药药房：门诊西药房（荔湾）\n医师手签：",
    "role": "user"
  }
]
[92m04:49:41 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:49:41,341 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:49:41,343 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:49:41.342+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 10, "failed": 0, "current": {"333155a8908811f1a3da71efcdd7cc1f": {"id": "333155a8908811f1a3da71efcdd7cc1f", "doc_id": "32f80906908811f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412392, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905007404, "task_type": "dataflow", "root_trace_id": "8cc21299ba8c4c4f9376bb5b55f5585f", "root_traceparent": "00-8cc21299ba8c4c4f9376bb5b55f5585f-3809269866d439b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:49:45,087 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:49:45,087 INFO     29 [qwen-vl-text] LLM output (len=952):
{
  "encounter_date": "2026-01-06",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": null,
  "diagnosis": "支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎",
  "items": [
    {
      "drug_generic_name": "左氧氟沙星片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "0.5g",
      "frequency": "qd",
      "route": "口服",
      "duration_days": null,
      "quantity": "3片",
      "notes": null
    },
    {
      "drug_generic_name": "醋酸泼尼松片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "qm",
      "route": "口服",
      "duration_days": null,
      "quantity": "6片",
      "notes": null
    },
    {
      "drug_generic_name": "盐酸氨溴索分散片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "30mg",
      "frequency": "tid",
      "route": "餐后口服",
      "duration_days": null,
      "quantity": "15片",
      "notes": null
    }
  ]
}
2026-08-05 04:49:45,087 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-06]
2026-08-05 04:49:45,091 INFO     29 [qwen-vl-text] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1247901, prompt_len=1039
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共40行）
["处方笺", "普通", "诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎", "患者", "年龄：65岁", "费别", "科室", "6-01-06 11:31:02", "处方", "地址", "联系", "身份", "Rp:", "左氧氟沙星片(省采)●⑥", "0.5g*28片/盒", "3片", "剂量：每次0.5g", "(1 片)", "用法：口服", "qd", "01-06", "醋酸泼尼松片●②⑥", "5mg*100/瓶", "6片", "剂量：每次10mg", "(2 片)", "用法：口服", "qm", "01-06", "盐酸氨溴索分散片(省采)●⑥", "30mg*50/盒", "15片", "剂量：每次30mg", "(1 片)", "用法：餐后口服", "tid", "01-06", "处方金额：3.47元", "取药药房：门诊西药房（荔湾）", "医师手签："]

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
2026-08-05 04:49:50,201 INFO     29 [qwen-vl-text] coord API raw response (len=231):
[
	{"text": "处方笺", "bbox": [378, 104, 494, 127]},
	{"text": "普通", "bbox": [744, 140, 784, 153]},
	{"text": "诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎", "bbox": [104, 272, 876, 291]},
	{"text": "患者", "bbox": [106, 170, 128, 186]},
2026-08-05 04:49:50,201 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-05 04:49:50,201 INFO     29 [qwen-vl-text] coord API: raw_items=4, valid_items=4, elapsed=5.1s
2026-08-05 04:49:50,201 INFO     29 [qwen-vl-text] coord item[0]: text=处方笺, bbox=[378, 104, 494, 127]
2026-08-05 04:49:50,201 INFO     29 [qwen-vl-text] coord item[1]: text=普通, bbox=[744, 140, 784, 153]
2026-08-05 04:49:50,202 INFO     29 [qwen-vl-text] coord item[2]: text=诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎, bbox=[104, 272, 876, 291]
2026-08-05 04:49:50,202 INFO     29 [qwen-vl-text] coord item[3]: text=患者, bbox=[106, 170, 128, 186]
2026-08-05 04:49:50,206 INFO     29 [qwen-vl-text] page=15 — 5/40 coords, api_time=5.1s
2026-08-05 04:49:50,207 INFO     29 [qwen-vl-text] new_positions (40):
[[15, 224.91, 293.93, 87.568, 106.934], [15, 442.68, 466.47999999999996, 117.88, 128.826], [15, 61.879999999999995, 521.22, 229.024, 245.022], [15, 63.07, 76.16, 143.14, 156.612], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 224.91, 293.93, 87.568, 106.934], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0], [15, 0, 0, 0, 0]]
2026-08-05 04:49:50,207 INFO     29 [qwen-vl-text] ═══ DONE ═══ 40 positions, pages=1, time=9.1s
2026-08-05 04:49:50,227 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-05 04:49:50,227 INFO     29 [Trace] task=333155a8 | doc=HXJ 哮喘 广三.pdf | Extractor:Prescription | outputs={"chunks": "11 items, types={'PrescriptionRecord': 11}", "html": "", "json": "580 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Prescription": "11 items, types={'PrescriptionRecord': 11}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Prescription\": 11, \"chunks_LabExam\": 1}"}
2026-08-05 04:49:50,227 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-05 04:49:50,232 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:49:50,232 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m04:49:50 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:49:50,233 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:49:53,791 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:49:53,798 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-05 04:49:53,798 INFO     29 [Trace] task=333155a8 | doc=HXJ 哮喘 广三.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "580 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Prescription": "11 items, types={'PrescriptionRecord': 11}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Prescription\": 11, \"chunks_LabExam\": 1}"}
2026-08-05 04:49:53,798 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-05 04:49:53,803 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 04:49:53,803 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-05 04:49:54,368 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 04:49:54,380 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-05 04:49:54,381 INFO     29 [Trace] task=333155a8 | doc=HXJ 哮喘 广三.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "580 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Prescription": "11 items, types={'PrescriptionRecord': 11}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Prescription\": 11, \"chunks_LabExam\": 1}"}
2026-08-05 04:49:54,381 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-05 04:49:54,390 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:49:54,391 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m04:49:54 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:49:54,392 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:49:56,092 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:49:56,104 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-05 04:49:56,104 INFO     29 [Trace] task=333155a8 | doc=HXJ 哮喘 广三.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "580 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Prescription": "11 items, types={'PrescriptionRecord': 11}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Prescription\": 11, \"chunks_LabExam\": 1}"}
2026-08-05 04:49:56,104 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-05 04:49:56,107 INFO     29 [ChunkMerger] Merged 16 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 4, 'Extractor:Medication': 1, 'Extractor:Prescription': 11, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1} (filtered 5 noise chunks)
2026-08-05 04:49:56,120 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-05 04:49:56,120 INFO     29 [Trace] task=333155a8 | doc=HXJ 哮喘 广三.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "16 items, types={'LabReport': 1, 'OutpatientRecord': 4, 'PrescriptionRecord': 11}", "name": "HXJ 哮喘 广三.pdf"}
2026-08-05 04:49:56,120 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-05 04:49:56,276 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1785905009537, 'update_date': datetime.datetime(2026, 8, 5, 4, 43, 29), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 163195, 'status': '1'}
2026-08-05 04:49:56,492 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   白细胞  WBC  9.17  10^9/L  3.5 -- 9.5  False    中性粒细胞总数  NEU  5.71  10^9/L  1.8 -- 6.3  False    中性粒细胞百分数  NEUN  62.30  %  40 -- 75  False    淋巴细胞总数  LY  2.62  10^9/L  1.1 -- 3.2  False    淋巴细胞百分数  LYN  28.60  %  20 -- 50  False    单核细胞总数  MONO  0.47  10^9/L  0.1 -- 0.6  False    单核细胞百分数  MON0  5.10  %  3 -- 10  False    嗜酸性粒细胞总数  EOS  0.34  10^9/L  0.02 -- 0.52  False    嗜酸性粒细胞百分数  EOS%  3.70  %  0.4 -- 8  False    嗜碱性粒细胞总数  BAS0  0.03  10^9/L  0 -- 0.06  False    嗜碱性粒细胞百分比  BAS0%  0.30  %  0 -- 1  False    红细胞  RBC  4.91  10^12/L  4.3 -- 5.8  False    血红蛋白  HGB  158  g/L  130 -- 175  False    红细胞压积  HCT  47.10  %  40 -- 50  False    红细胞平均容积  MCV  96.90  fl  82 -- 100  False    红细胞平均血红蛋白  MCH  32.20  pg  27 -- 34  False    红细胞平均血红蛋白浓度  MCHC  335.00  g/L  316 -- 354  False    红细胞分布宽度  RDW  12.40  %  11.6 -- 14.8  False    红细胞分布宽度-SD  RDW-SD  44.10  fl  37.1 -- 49.2  False    血小板  Plt  197  10^9/L  125 -- 350  False    平均血小板容积  MPV  10.70  fl  6 -- 12  False    平均血小板比容  Pct  0.21  %  0.10 -- 0.29  False    血小板分布宽度  PDW  13.00  10(GSP)  15.3 -- 20.5  True    大血小板  P-LCR  30.90  %  None  False    网织红细胞绝对值  RETR  90.5  10^9/L  46.4 -- 121.2  False    网织红细胞百分数  RETR  1.64  %  None  False    低荧光强度网织红细胞比率  LFF  83.8  %  89.9 -- 98.4  True    中荧光强度网织红细胞比率  MFF  13.3  %  1.6 -- 9.5  True    高荧光强度网织红细胞比率  HFF  2.9  %  0 -- 1.7  True    未成熟网织红细胞比率  IRF  16.2  %  1.6 -- 10.5  True    有核红细胞计数  NRBCW  0  10^9/L  None  False    有核红细胞百分比  NRBC%  0  %  None  False   
---
门(急)诊病历信息
就诊卡
流水
病历编号:
姓
别:男
年
龄:64岁
就诊科室:内科门诊(荔湾)
医
诊时间:2025-10-21 16:24:23
主
诉:取药
现病史:
既往史:
过敏史:
个人史:
体格检查:
专科情况:
辅助检查:
治疗项目:
门诊诊断:
支气管哮喘
单病种:
发病时间:
处置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。
1孟鲁司特钠片(省采)◆
1瓶10.0mg,口服,每晚1次
30天
2倍氯米松福莫特罗吸入气雾剂◆①
1瓶2.0揿,吸入用药,一天2次
30天
备注:建议在住地附近社区医疗机构随诊。
---
门(急)诊病历信息
就诊卡号:
流水号:
病历编号:
性别:男
年
龄:65岁
就诊科室:内科门诊(荔湾)
医生:
就诊时间:2025-11-19 11:33:52
主诉:取药
现病史:
既往史:
过敏史:
个人史:
体格检查:
专科情况:
辅助检查:
治疗项目:
门诊诊断:
1、支气管哮喘
处置:
1孟鲁司特钠片(省采)◆
1瓶10.0mg,口服,每晚1次
30天
2倍氯米松福莫特罗吸入气雾剂◆①
1瓶2.0揿,吸入用药,一天2次
30天
备注:
---
门(急)诊病历信息
就诊卡号
流水
姓名
性别:男
年
龄:65岁
就诊科室:内科门诊(荔湾)
病历编号:
就诊时间:2025-12-12 09:26:46
主诉:BAIYUN V8
现病史:自上次访视至今,询问及查询HIS系统受试者无新增AE、SAE、哮喘急性发作,有新增合并用药。发生过2次医疗相关事件,就诊于荔湾区逢源街道社区中心1次,就诊于专科门诊1次。期间未收到ePRO触发的哮喘警报邮件。
完成下流操作:
1、静坐10分钟后,测量坐位生命体征,血压:120/76mmHg,脉搏频率:59次/分(NCS),呼吸:20次/分,体温:36.5℃;
2、9:20体格检查:神志清,体置合作,自主体位,一般外表无异常,皮肤、粘膜无异常,唇甲无发绀,眼睛、耳、鼻、咽喉无异常,口咽部粘膜无异常,颈软,气管居中,甲状腺未及肿大,全身浅表淋巴结未及肿大,颈静脉无怒张,胸廓无畸形,双肺呼吸运动对称,双肺触觉语颤正常,双肺叩诊清音,双肺呼吸音清,未闻及啰音。心前区无隆起,心尖搏动无弥散,心界不大,心率:59次/分,律齐,各瓣膜听诊区未闻及病理性杂音。腹平软,全腹无压痛、反跳痛。肝、脾肋下未及,肝肾区无叩击痛,肠鸣音存,4次/分,脊柱、四肢无畸形,生理征存,未引出病理征,其他系统未见明显异常。
3、查看受试者电子日志,受试者漏填2025年10月26日(早间日志)、8月23日、9月10日、9月19日、9月24日、10月5日、10月25日、11月3日、12月2日(晚间日志)。
4、填写AQLQ+12和ACQ-5问卷,ACQ-5评分:1.0分。
5、休息至少10分钟后,行12导联ECG检查。
6、10:42采集中心实验室样本(血常规、血生化)并送往中心实验室。
7、回收试验药物BDA MDI AS MDI 3盒(137968-KF未开封、102035-IM未用74喷,实际已用:24喷,发药当天预喷4喷,2025.8.18-2025.9.10期间因超过7天未使用试验药物预喷1次共2喷,2025.9.10-11.19期间每七天清洗装置后预喷10次共20喷,总计预喷26喷;199863-TA未用106喷,实际已用:8喷,2025.11.20当天预喷4喷,2025.11.20-2025.12.12期间每七天清洗装置后预喷3次共6喷,总计预喷10喷)ePro记录使用总共32喷,与实际使用情况一致。
CS 扫描全能王
3亿人都在用的扫描App
门诊病历
25/10/21 16时 门诊病历
25/11/19 11时 门诊病历（GCP专用）
25/12/12 09时 门诊病历（GCP专用）
1、颈痛综合征:开始时间:2025年1月8日,持续中,中度,非SAE,与试验药物无关,对试验
药物采取措施:剂量无需改变,未因该AE退出研究,采取理疗。
2、功能性消化不良:开始时间:2025年5月20日,持续中,中度,非SAE,与试验药物无
关,对试验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:药物治疗。
病因:无诱因,症状:下腹痛,进食后明显,休息后可缓解。
3、慢性胃炎:开始时间:2025年3月2日,持续中,中度,非SAE,与试验药物无关,对试
验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:暂无治疗措施。
跟踪合并用药
1、糠酸莫米松鼻喷雾剂 2024.7.19-2025.9.26 每日每早一粒 喷鼻 必要时 治疗过敏
性鼻炎。
2、盐酸二甲双胍片 2024.10.10-2025.9.14 0.5 TID 治疗2型糖尿病。
3、达格列净片 2025.9.15至今 10mg qd 治疗2型糖尿病。
补充合并用药:1、硫酸特布他林雾化吸入用溶液 2025.6.17-2025.6.19 5mg 吸
入 qd 治疗急性支气管炎。
预约下次安全性电话随访时间。
既往史:
过敏史:
个人史:
体格检查:
专科情况:
辅助检查:
治疗项目:
门诊诊断:
1、支气管哮喘
处置:
心电图(心电图室做)
伯氟米松福莫特罗吸入气雾剂① 1瓶2.0瓶,吸入用药,一天2次 30天
孟鲁司特钠片(省采)① 6盒10.0mg,口服,每日1次(口服) 30天
备注:
医生:
---
病历编号：
姓名：
性别：男
年龄：65岁
就诊科室：内科门诊（基础）
医生：
就诊时间：2026-02-04 11:23:30
主诉：支气管哮喘治疗后复诊
现病史：2022年3月前开始出现咳嗽、咳痰，粘白，量少，能咯出，咳嗽呈阵发性，偶则激性，伴轻度咽痒，无气促，夜间有喘息、胸闷，伴鼻塞、流涕、喉咙，无咽痛，
无反酸、嗳气、腹胀，无上腹部隐痛不适感，无伴发热、畏寒，曾自服肺力咳症状未见缓解，现病情好转、稳定，本次门诊距上次门诊间隔时间7天；过去4周，症状控制情况：控制良好，吸入药物使用情况：遵医嘱使用；，吸入装置使用情况：有，正确；急性发作情况：
两次就诊期间急性发作：发作次数：0次，长期规律使用倍氯米松福莫特罗吸入气雾剂治疗。
既往史：鼻炎病史，有糖尿病史
过敏史：未发现
个人史：否认遗传病史，吸烟30年，6支/日，已戒烟8年，饮酒6年，1两/日。
体格检查：神志清，口腔无溃疡、粘膜白斑，肺部听诊，鼻塞，通气，气管居中，双肺呼吸音稍减弱，未闻及明显干湿性罗音。
专科情况：
辅助检查：血常规：Q-CRP：0.54mg/l 白细胞：5.5*109/L 中性粒细胞：
5.17*109/L 60.5% 淋巴细胞：2.23*109/L 26.2% 单个核细胞：
0.46*109/L 5.4% 嗜酸性粒细胞：0.6*109/L 7.1% 呼出气一氧化
氮：FeNO50：130ppb FnNO10：161ppb 肺功能：轻度阻塞性通气功能障碍，支气管激发
试验阳性（PD20=0.312mg AHI：轻度），胸片：心、肺、膈未见异常
治疗项目：
门诊诊断：
1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、2型糖尿病
单 种：
发病时间：
处 置：请仔细阅读药品说明书等文书资料，遵嘱治疗，不适随诊。
倍氯米松福莫特罗吸入气雾剂◆① 1瓶2.0瓶，吸入用药，一天2次 30天
孟鲁司特钠片（省采）◆ 6盒10.0mg，口服，每日1次（口服） 30天
备 注：建议在停药附近社区医疗机构随访。
---
门(急)诊处方
就诊时间:2025-09-15
就诊科室:内科门诊
主诊医
姓名
性别:男
年龄:64岁
卡号:4
患者
医疗证号:
处方号
地址:
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
孟鲁司特钠片◆
10mg*30/瓶
30片
1.05
31.53
Sig
10mg/次,口服,qn*30天
倍氯米松福莫特罗吸入气雾剂◆
6ug/揿*120揿
221.61
221.61
Sig
2揿/次,吸入,bid*30天
医师
医生编号:1326
配剂人:
核对人:
合计:
收费员:
打印时间:2025-12-19
为了您的用药安全,药物处方当天有效 第1页共1页
---
门(急)诊处方
就诊时间:2025-08-18
就诊科室:内科门诊
主诊
姓名:
性别:男
年龄:64岁
卡号
患者类型:GCP支付
医疗证号:
处方
地址:
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
孟鲁司特钠片◆
10mg*30/瓶
28片
1.05
29.43
Sig
10mg/次,口服,qn*28天
倍氯米松福莫特罗吸入气雾剂
6ug/揿*120揿
221.61
221.61
Sig
2揿/次,吸入,bid*30天
---
门(急)诊处方
就诊时间:2025-05-30
就诊科室:内科门诊
主
姓名
性别:男
年龄:64岁
卡
患者类型:GCP支付
医疗证号:
处
地址:
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
孟鲁司特钠片◆
10mg*5/盒
90片
2.56
230.58
Sig
10mg/次,口服,qn*90天
倍氯米松福莫特罗吸入气雾剂0◆@/6ug/揿*120瓶
221.61
664.83
Sig
2揿/次,吸入,bid*90天
---
门(急)诊处方
就诊时间:2025-03-05
就诊科室:内科门诊
主诊医
姓名
性别:男
年龄:64岁
卡号:
患者类型:GCP支付
医疗证号:
处方号:
地址:
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
倍氯米松福莫特罗吸入气雾剂*0ug/6ug/瓶*120瓶
221.61 443.22
Sig
2揿/次,吸入,bid*60天
孟鲁司特钠片
10mg*30/瓶
60片
1.05
63.06
Sig
10mg/次,口服,qn*60天
---
门(急)诊处方
就诊时间:2025-03-05
就诊科室:内科门诊
主诊
姓名
性别:男
年龄:64岁
卡号
患者类型:GCP支付
医疗证号:
处方
地址:
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
倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿
221.61 221.61
Sig
2揿/次,吸入,bid*30天
孟鲁司特钠片
10mg*30/瓶
30片
1.05
31.53
Sig
10mg/次,口服,qn*30天
---
门(急)诊处方
就诊时间:2025-02-08
就诊科室:内科门诊
主诊
姓名:
性别:男
年龄:64岁
卡号:
患者类型:001 支付
医疗证号:
处方
地址:
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
倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120瓶
221.61 221.61
Sig
2揿/次,吸入,bid*30天
孟鲁司特钠片◆
10mg*30/瓶
30片
1.05
31.53
Sig
10mg/次,口服,qn*30天
---
门(急)诊处方
就诊时间:2025-01-10
就诊科室:内科门诊
主诊
性别:男
年龄:64岁
卡号
患者类型:G
医疗证号:
处方
地址:
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
倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿
221.61 221.61
Sig
2揿/次,吸入,bid*30天
孟鲁司特钠片
10mg*30/瓶
30片
1.05
31.53
Sig
10mg/次,口服,qn*30天
---
门(急)诊处方
就诊时间:2024-12-11
就诊科室:内科门诊
主诊
姓名:
性别:男
年龄:64岁
卡号
患者类型:GCP支付
医疗证号:
处方
地址:
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
倍氯米松福莫特罗吸入气雾剂100ug/6ug/瓶*120瓶
221.61 221.61
Sig
2揿/次,吸入,bid*30天
孟鲁司特钠片◆
10mg*30/瓶
30片
1.05
31.53
Sig
10mg/次,口服,qn*30天
---
门(急)诊处方
就诊时间:2024-11-18
就诊科室:内科门诊
主诊
姓名
性别:男
年龄:63岁
卡号:
患者类型:GLP支付
医疗证号:
处方
地址:
身份证号:
诊断:支气管哮喘,非危重
西药处方
组号
项目名称
规格
总量
单价
金额
R:
倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿
221.61 221.61
Sig
2揿/次,吸入,bid*30天
孟鲁司特钠片
10mg*30/瓶
30片
1.05
31.53
Sig
10mg/次,口服,qn*30天
---
处方笺
普通
诊疗
患者姓
男
年龄：65岁
费别：
科室：
2026-01-06 11:28:26
处方号
地址：
联系电
身份号
诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎
R
P:
倍氯米松福莫特罗吸入气雾剂◆① 100ug/6ug/揿*120
1瓶
剂量：每次2揿 ( 1/60 瓶 )
用法：吸入用药
bid 01-06
孟鲁司特钠片(省采)◆
10mg*5/盒
30片
剂量：每次10mg (1 片 )
用法：口服
qd 01-06
处方金额：298.47元
取药药房：门诊西药房（荔湾）
---
处方笺
普通
诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎
患者
年龄：65岁
费别
科室
6-01-06 11:31:02
处方
地址
联系
身份
Rp:
左氧氟沙星片(省采)●⑥
0.5g*28片/盒
3片
剂量：每次0.5g
(1 片)
用法：口服
qd
01-06
醋酸泼尼松片●②⑥
5mg*100/瓶
6片
剂量：每次10mg
(2 片)
用法：口服
qm
01-06
盐酸氨溴索分散片(省采)●⑥
30mg*50/盒
15片
剂量：每次30mg
(1 片)
用法：餐后口服
tid
01-06
处方金额：3.47元
取药药房：门诊西药房（荔湾）
医师手签：
2026-08-05 04:49:57,196 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-05 04:49:57,196 INFO     29 [Trace] task=333155a8 | doc=HXJ 哮喘 广三.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "16 items, types={'LabReport': 1, 'OutpatientRecord': 4, 'PrescriptionRecord': 11}", "name": "HXJ 哮喘 广三.pdf", "embedding_token_consumption": 5814}
2026-08-05 04:49:57,196 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-05 04:49:57,634 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-05 04:49:57,634 INFO     29 [Trace] task=333155a8 | doc=HXJ 哮喘 广三.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":16,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-05 04:49:57,641 INFO     29 [DIAG-EXECUTOR] row_position_int len=32 row[0]=(14, 200, 258, 87, 96) row[-1]=(14, 200, 319, 515, 525)
2026-08-05 04:49:57,642 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:49:57,642 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:49:57,642 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:49:57,642 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:49:57,642 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:49:57,642 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:49:57,642 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:49:57,642 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:49:57,642 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:49:57,642 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:49:57,642 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:49:57,642 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:49:57,642 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:49:57,642 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:49:57,642 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:49:57,647 INFO     29 set_progress(333155a8908811f1a3da71efcdd7cc1f), progress: 0.82, progress_msg: 04:49:57 [DOC Engine]:
Start to index...
2026-08-05 04:49:57,667 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.014s]
2026-08-05 04:49:57,670 INFO     29 set_progress(333155a8908811f1a3da71efcdd7cc1f), progress: 0.80625, progress_msg: 
2026-08-05 04:49:57,688 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.011s]
2026-08-05 04:49:57,704 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.010s]
2026-08-05 04:49:57,720 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.008s]
2026-08-05 04:49:57,726 INFO     29 set_progress(333155a8908811f1a3da71efcdd7cc1f), progress: 1.0, progress_msg: 04:49:57 Indexing done (0.08s). Task done (355.24s)
2026-08-05 04:49:57,729 INFO     29 [Done], chunks(16), token(5814), elapsed:355.24
2026-08-05 04:49:57,911 INFO     29 handle_task done for task {"id": "333155a8908811f1a3da71efcdd7cc1f", "doc_id": "32f80906908811f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412392, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1785905007404, "task_type": "dataflow", "root_trace_id": "8cc21299ba8c4c4f9376bb5b55f5585f", "root_traceparent": "00-8cc21299ba8c4c4f9376bb5b55f5585f-3809269866d439b0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
