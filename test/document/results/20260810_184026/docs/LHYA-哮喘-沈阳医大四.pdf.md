# 基准结果：LHYA-哮喘-沈阳医大四.pdf

## 基本信息

- 文件：`LHYA-哮喘-沈阳医大四.pdf`
- 大小：4483.0 KB
- PDF 总页数：7
- doc_id：`e0cfe59494ac11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T19:16:03  完成时间：2026-08-10T19:19:34  耗时：210.4s
- progress_msg：`11:19:32 Indexing done (0.07s). Task done (197.51s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 01fe1282 | 1 | 1-1 | 四平市中心人民医院 门诊诊断书 0003316 (患者保管) SPZXYy-JL |
| 2 | 9b2add43 | 1 | 2-2 | 四平市中医医院 门诊病历 初诊 2025年11月26日 肾病糖尿病科 姓名 性别 |
| 3 | fc0337ce | 1 | 3-3 | 四平市中医医院 内二疗区 门诊病历 初诊 2025年12月31日 姓名 性别：女 |
| 4 | 2ba358e6 | 1 | 4-4 | 四平市中心人民医院 常规通气+舒张试验 姓名： 年龄：53岁 住院号：11163 |
| 5 | b4cd8c5e | 1 | 5-5 | 四平市中心人民医院 常规通气 姓名：李洪燕 性别：女 年龄：53岁 吸烟史： 住 |
| 6 | d1390d26 | 1 | 6-6 | 信康大药房--佳合分店 单号：250927207100156 日期：2025-0 |
| 7 | a4c3ef48 | 1 | 7-7 | 信康大药房--佳合分店 单号：251128207100163 日期：2025-1 |

- chunks 总数：7
- 各 chunk 页数合计（含跨页重复）：7
- 页码并集：`[1, 2, 3, 4, 5, 6, 7]`
- 覆盖页数：7 / 7；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 3 | 0 | 3 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 2 | 2 | 2 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 2 | 2 | 2 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 3, "ExaminationReport": 2, "MedicationRecord": 2}`
- ChunkMerger：`{"found": true, "merged": 7, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 3, "Extractor:Medication": 2, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 2, "Extractor:Progress": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 11:19:31,589 INFO     29 [ChunkMerger] Merged 7 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 3, 'Extractor:Medication': 2, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 11:16:08,046 INFO     29 handle_task begin for task {"id": "e139f7cc94ac11f1bd9827cf206dfa2d", "doc_id": "e0cfe59494ac11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "type": "pdf", "location": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "size": 4593431, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786360565919, "task_type": "dataflow", "root_trace_id": "a7e430023e6144f7a5a82bee44b10046", "root_traceparent": "00-a7e430023e6144f7a5a82bee44b10046-21836b890cf4bf02-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 11:16:08,325 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.002s]
2026-08-10 11:16:08,444 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 11:16:08,456 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:16:08,456 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 11:16:08,456 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 11:16:08,463 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 11:16:08,463 INFO     29 ============================================================
2026-08-10 11:16:08,463 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 11:16:08,463 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 11:16:08,463 INFO     29 ============================================================
2026-08-10 11:16:08,463 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 11:16:08,463 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 11:16:08,465 INFO     29 No torch found.
2026-08-10 11:16:09,371 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=7
2026-08-10 11:16:09,643 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1304753, prompt_len=764
2026-08-10 11:16:11,384 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:16:11,385 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 11:16:11,392 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1304753, prompt_len=401
2026-08-10 11:16:13,076 INFO     29 [qwen-vl-parser] text API response (len=252):
["四平市中心人民医院", "门诊诊断书", "0003316", "(患者保管)", "SPZXYy-JLLC-042", "姓名", "性别", "女", "年龄", "54岁", "单位", "诊断", "支气管哮喘", "病情诊断摘要依据", "发作性喘息30余年，双肺干", "啰音，诊断支气管哮喘", "医生处理意见", "1.平喘治疗", "2.随访", "医生签字：", "门诊部负责人签字：", "科主任签字：", "门诊部盖章：2023年12月27日", "(无公章和医生章无效)"]
2026-08-10 11:16:13,077 INFO     29 [qwen-vl-parser] page=1 text: 24 lines (bbox 0-23)
2026-08-10 11:16:13,077 INFO     29 [qwen-vl-parser] page=1 text: 24 sections
2026-08-10 11:16:13,279 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1189831, prompt_len=764
2026-08-10 11:16:14,688 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:16:14,688 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 11:16:14,708 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1189831, prompt_len=401
2026-08-10 11:16:18,371 INFO     29 [qwen-vl-parser] text API response (len=635):
["四平市中医医院", "门诊病历", "初诊", "2025年11月26日", "肾病糖尿病科", "姓名", "性别", "女性", "年龄", "55岁", "门诊号码", "202511260272", "（1）", "发病日期", "2025-11-26", "类别", "自费", "保险卡号", "就诊方式", "便民门诊费", "医生", "王亚新", "联系地址", "四平铁西", "联系电话", "13689710485", "身份证号", "职业", "体温 36.5 ℃ 血压 130、80 mmHg 脉搏 70 次/分", "药物过敏史", "无", "主诉:", "自述糖尿病4年，支气管哮喘30余年", "病史:", "糖尿病4年，尿中有沫。伴双下肢水肿+。现二甲双胍片，0.5，日3次，口服。血糖控制不佳。葡萄糖：12.39mmol/1.，糖化：", "10.1%，一周前感冒山现间断咳嗽气短胸闷，活动后加重，有夜间憋醒史，咳白痰，无发热，饮食尚可，大小便正常。", "临床诊断：2型糖尿病 支气管哮喘急性发作", "治疗方案:", "建议入院治疗，拒绝。糖尿病饮食，监测血糖，继续用药治疗，有变化随诊。沙美特罗卡替松粉吸入剂50微克/250微克/揿/盒，", "每瓶60揿（30个用药计量），甲泼尼龙片4mg×24片/盒（口服5天）。", "结论:", "病程记录:", "医生（印章）：", "2025年11月27日 11:18"]
2026-08-10 11:16:18,371 INFO     29 [qwen-vl-parser] page=2 text: 44 lines (bbox 24-67)
2026-08-10 11:16:18,371 INFO     29 [qwen-vl-parser] page=2 text: 44 sections
2026-08-10 11:16:18,652 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1440593, prompt_len=764
2026-08-10 11:16:20,222 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-12-31"}
```
2026-08-10 11:16:20,223 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=2025-12-31
2026-08-10 11:16:20,241 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1440593, prompt_len=401
2026-08-10 11:16:24,281 INFO     29 [qwen-vl-parser] text API response (len=488):
["四平市中医医院", "内二疗区", "门诊病历", "初诊", "2025年12月31日", "姓名", "性别：女性", "年龄：55岁", "门诊号码：202512310183", "（1）", "发病日期：2025-12-31", "类别：自费", "保险卡号", "就诊方式：服务号", "医生：张楷婷", "联系地址：吉林省四平市", "联系电话：13689710485", "身份证号：220303197009242283", "职业：", "体温 36.4 ℃ 血压 120/78 mmHg 脉搏 66 次/分", "药物过敏史：否", "主诉：发现血糖升高4年", "病史：发现血糖升高4年，现二甲双胍片0.5g日3次口服控制血糖。测空腹血糖11.41mmol/L，糖化血红蛋白8.9%，尿糖3+。", "临床诊断：2型糖尿病", "治疗方案：建议患者入院治疗，患者暂拒；糖尿病饮食，口服二甲双胍片0.5g日3次，适当饮水，监测血糖，定期复查，病情变化随诊", "结论：", "病程记录：", "医生（印章）：", "2025年12月31日 15:12"]
2026-08-10 11:16:24,281 INFO     29 [qwen-vl-parser] page=3 text: 29 lines (bbox 68-96)
2026-08-10 11:16:24,281 INFO     29 [qwen-vl-parser] page=3 text: 29 sections
2026-08-10 11:16:24,541 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1049499, prompt_len=764
2026-08-10 11:16:26,195 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 11:16:26,195 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 11:16:26,206 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1049499, prompt_len=401
2026-08-10 11:16:31,753 INFO     29 [qwen-vl-parser] text API response (len=1075):
["四平市中心人民医院", "常规通气+舒张试验", "姓名：", "年龄：53岁", "住院号：111630435", "身高：168 cm", "性别：女", "吸烟史：", "测试号：20231227014", "体重：82 kg", "Flow [L/s]", "F/V ex", "Vol [L]", "Vol%VCmax", "VCmax", "Time [s]", "F/V in", "测试日期", "测试时间", "预计值", "药前", "前/预%", "药后", "后/预% 改善率 (%)", "23/12/27", "23/12/27", "15:36:14", "15:51:45", "MV", "[L/min]", "11.71", "27.39", "233.8", "3.78", "115.4", "7.6", "VC MAX", "[L]", "3.28", "3.52", "107.3", "FVC", "[L]", "3.17", "3.52", "110.8", "3.78", "119.2", "7.6", "FEV 1", "[L]", "2.71", "2.11", "77.7", "2.39", "88.3", "13.7", "FEV 1 % FVC", "[%]", "59.91", "63.29", "5.6", "FEV 1 % VC MAX", "[%]", "79.03", "59.91", "75.8", "63.29", "80.1", "5.6", "PEF", "[L/s]", "6.54", "4.76", "72.7", "4.54", "69.4", "-4.6", "MEF 75", "[L/s]", "5.68", "2.64", "46.4", "3.29", "58.0", "24.9", "MEF 50", "[L/s]", "3.95", "1.40", "35.4", "1.80", "45.5", "28.5", "MEF 25", "[L/s]", "1.55", "0.53", "34.2", "0.65", "42.1", "22.9", "MMEF 75/25", "[L/s]", "3.22", "1.15", "35.8", "1.44", "44.6", "24.5", "MVV", "[L/min]", "100.45", "检查意见：", "结果：支气管舒张实验(+)。", "操作者签字：", "医生签字："]
2026-08-10 11:16:31,755 INFO     29 [qwen-vl-parser] page=4 text: 117 lines (bbox 97-213)
2026-08-10 11:16:31,755 INFO     29 [qwen-vl-parser] page=4 text: 117 sections
2026-08-10 11:16:31,968 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=910983, prompt_len=764
2026-08-10 11:16:32,188 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:16:32.186+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 19, "failed": 0, "current": {"e139f7cc94ac11f1bd9827cf206dfa2d": {"id": "e139f7cc94ac11f1bd9827cf206dfa2d", "doc_id": "e0cfe59494ac11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "type": "pdf", "location": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "size": 4593431, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786360565919, "task_type": "dataflow", "root_trace_id": "a7e430023e6144f7a5a82bee44b10046", "root_traceparent": "00-a7e430023e6144f7a5a82bee44b10046-21836b890cf4bf02-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:16:33,648 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2023-12-27"
}
```
2026-08-10 11:16:33,649 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=2023-12-27
2026-08-10 11:16:33,671 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=910983, prompt_len=401
2026-08-10 11:16:39,181 INFO     29 [qwen-vl-parser] text API response (len=1105):
["四平市中心人民医院", "常规通气", "姓名：李洪燕", "性别：女", "年龄：53岁", "吸烟史：", "住院号：111630435", "测试号：20231227014", "身高：168 cm", "体重：82 kg", "Flow [L/s]", "F/V ex", "Vol [L]", "Vol%Vmax", "VCmax", "F/V in", "Time [s]", "测试日期", "测试时间", "预计值", "实测值", "实/预", "23/12/27", "15:36:14下午", "VT", "[L]", "0.59", "1.51", "258.6", "BF", "[1/min]", "20.00", "18.08", "90.4", "MV", "[L/min]", "11.71", "27.39", "233.8", "VC MAX", "[L]", "3.28", "3.52", "107.3", "ERV", "[L]", "0.93", "1.39", "149.9", "IC", "[L]", "2.35", "2.13", "90.5", "FVC", "[L]", "3.17", "3.52", "110.8", "FEV 1", "[L]", "2.71", "2.11", "77.7", "FEV 1 % FVC", "[%]", "79.03", "59.91", "75.8", "FEV 1 % VC MAX", "[%]", "6.54", "4.76", "72.7", "PEF", "[L/s]", "5.68", "2.64", "46.4", "MEF 75", "[L/s]", "3.95", "1.40", "35.4", "MEF 50", "[L/s]", "1.55", "0.53", "34.2", "MEF 25", "[L/s]", "3.22", "1.15", "35.8", "MMEF 75/25", "[L/s]", "0.85", "0.35", "41.0", "FEF 75/85", "[L/s]", "2.16", "78.19", "PIF", "[L/s]", "FEF50 % FIF50", "[%]", "MVV", "[L/min]", "100.45", "63.19", "62.9", "FEV 1*30", "[L/min]", "100.45", "检查意见：", "轻度阻塞型通气功能障碍", "小气道功能异常", "操作者签字：", "医生签字："]
2026-08-10 11:16:39,183 INFO     29 [qwen-vl-parser] page=5 text: 120 lines (bbox 214-333)
2026-08-10 11:16:39,183 INFO     29 [qwen-vl-parser] page=5 text: 120 sections
2026-08-10 11:16:39,681 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2333855, prompt_len=764
2026-08-10 11:16:42,284 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:16:42,285 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-10 11:16:42,299 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2333855, prompt_len=401
2026-08-10 11:16:45,164 INFO     29 [qwen-vl-parser] text API response (len=435):
["信康大药房--佳合分店", "单号：250927207100156", "日期：2025-09-27 17:52:20", "会员卡号：13689710485", "姓名：", "积分：37", "总积分：47", "药品名称", "规格", "生产企业/药品上市许可持有人", "产地", "剂型", "批号", "有效期", "数量", "单价", "金额", "12534", "185.00", "沙美特罗替卡松吸入粉雾剂", "50微克/250微克/60泡/盒", "葛兰素史克集团吸入粉雾剂", "JD6K", "2027-06-18", "2盒", "185.00", "370.00", "信康大药房温馨提示：您购买的", "药品需要常温储存(10℃-30℃)", "合计：", "370.00", "实收：", "370.00", "开票员：王影", "营业员：7139", "药品售出无质量问题不退不换！", "电话：0434-3333658"]
2026-08-10 11:16:45,164 INFO     29 [qwen-vl-parser] page=6 text: 37 lines (bbox 334-370)
2026-08-10 11:16:45,164 INFO     29 [qwen-vl-parser] page=6 text: 37 sections
2026-08-10 11:16:45,628 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2194781, prompt_len=764
2026-08-10 11:16:47,805 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:16:47,806 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-10 11:16:47,816 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2194781, prompt_len=401
2026-08-10 11:16:50,655 INFO     29 [qwen-vl-parser] text API response (len=435):
["信康大药房--佳合分店", "单号：251128207100163", "日期：2025-11-28 16:38:41", "会员卡号：13689710485", "姓名：", "积分：37", "总积分：84", "药品名称", "规格", "生产企业/药品上市许可持有人", "产地", "剂型", "批号", "有效期", "数量", "单价", "金额", "12534", "185.00", "沙美特罗替卡松吸入粉雾剂", "50微克/250微克/60泡/盒", "葛兰素史克集团吸入粉雾剂", "JD6K", "2027-06-18", "2盒", "185.00", "370.00", "信康大药房温馨提示：您购买的", "药品需要常温储存（10℃-30℃）", "合计：", "370.00", "实收：", "370.00", "开票员：张欣", "营业员：7140", "药品售出无质量问题不退不换！", "电话：0434-3333658"]
2026-08-10 11:16:50,655 INFO     29 [qwen-vl-parser] page=7 text: 37 lines (bbox 371-407)
2026-08-10 11:16:50,655 INFO     29 [qwen-vl-parser] page=7 text: 37 sections
2026-08-10 11:16:50,655 INFO     29 [qwen-vl-parser] parse_pdf done: 408 sections from 7 pages.
2026-08-10 11:16:50,663 INFO     29 Close text detector.
2026-08-10 11:16:51,152 INFO     29 Close text recognizer.
2026-08-10 11:16:51,588 INFO     29 Close recognizer.
2026-08-10 11:16:51,993 INFO     29 Close recognizer.
2026-08-10 11:16:52,428 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 11:16:52,428 INFO     29 [Trace] task=e139f7cc | doc=LHYA-哮喘-沈阳医大四.pdf | Parser:MedLink | outputs={"html": "", "json": "408 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "json"}
2026-08-10 11:16:52,428 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 11:16:52,459 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:16:52,459 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 四平市中心人民医院\n[BBOX-1] 门诊诊断书\n[BBOX-2] 0003316\n[BBOX-3] (患者保管)\n[BBOX-4] SPZXYy-JLLC-042\n[BBOX-5] 姓名\n[BBOX-6] 性别\n[BBOX-7] 女\n[BBOX-8] 年龄\n[BBOX-9] 54岁\n[BBOX-10] 单位\n[BBOX-11] 诊断\n[BBOX-12] 支气管哮喘\n[BBOX-13] 病情诊断摘要依据\n[BBOX-14] 发作性喘息30余年，双肺干\n[BBOX-15] 啰音，诊断支气管哮喘\n[BBOX-16] 医生处理意见\n[BBOX-17] 1.平喘治疗\n[BBOX-18] 2.随访\n[BBOX-19] 医生签字：\n[BBOX-20] 门诊部负责人签字：\n[BBOX-21] 科主任签字：\n[BBOX-22] 门诊部盖章：2023年12月27日\n[BBOX-23] (无公章和医生章无效)\n[BBOX-24] 四平市中医医院\n[BBOX-25] 门诊病历\n[BBOX-26] 初诊\n[BBOX-27] 2025年11月26日\n[BBOX-28] 肾病糖尿病科\n[BBOX-29] 姓名\n[BBOX-30] 性别\n[BBOX-31] 女性\n[BBOX-32] 年龄\n[BBOX-33] 55岁\n[BBOX-34] 门诊号码\n[BBOX-35] 202511260272\n[BBOX-36] （1）\n[BBOX-37] 发病日期\n[BBOX-38] 2025-11-26\n[BBOX-39] 类别\n[BBOX-40] 自费\n[BBOX-41] 保险卡号\n[BBOX-42] 就诊方式\n[BBOX-43] 便民门诊费\n[BBOX-44] 医生\n[BBOX-45] 王亚新\n[BBOX-46] 联系地址\n[BBOX-47] 四平铁西\n[BBOX-48] 联系电话\n[BBOX-49] 13689710485\n[BBOX-50] 身份证号\n[BBOX-51] 职业\n[BBOX-52] 体温 36.5 ℃ 血压 130、80 mmHg 脉搏 70 次/分\n[BBOX-53] 药物过敏史\n[BBOX-54] 无\n[BBOX-55] 主诉:\n[BBOX-56] 自述糖尿病4年，支气管哮喘30余年\n[BBOX-57] 病史:\n[BBOX-58] 糖尿病4年，尿中有沫。伴双下肢水肿+。现二甲双胍片，0.5，日3次，口服。血糖控制不佳。葡萄糖：12.39mmol/1.，糖化：\n[BBOX-59] 10.1%，一周前感冒山现间断咳嗽气短胸闷，活动后加重，有夜间憋醒史，咳白痰，无发热，饮食尚可，大小便正常。\n[BBOX-60] 临床诊断：2型糖尿病 支气管哮喘急性发作\n[BBOX-61] 治疗方案:\n[BBOX-62] 建议入院治疗，拒绝。糖尿病饮食，监测血糖，继续用药治疗，有变化随诊。沙美特罗卡替松粉吸入剂50微克/250微克/揿/盒，\n[BBOX-63] 每瓶60揿（30个用药计量），甲泼尼龙片4mg×24片/盒（口服5天）。\n[BBOX-64] 结论:\n[BBOX-65] 病程记录:\n[BBOX-66] 医生（印章）：\n[BBOX-67] 2025年11月27日 11:18\n[BBOX-68] 四平市中医医院\n[BBOX-69] 内二疗区\n[BBOX-70] 门诊病历\n[BBOX-71] 初诊\n[BBOX-72] 2025年12月31日\n[BBOX-73] 姓名\n[BBOX-74] 性别：女性\n[BBOX-75] 年龄：55岁\n[BBOX-76] 门诊号码：202512310183\n[BBOX-77] （1）\n[BBOX-78] 发病日期：2025-12-31\n[BBOX-79] 类别：自费\n[BBOX-80] 保险卡号\n[BBOX-81] 就诊方式：服务号\n[BBOX-82] 医生：张楷婷\n[BBOX-83] 联系地址：吉林省四平市\n[BBOX-84] 联系电话：13689710485\n[BBOX-85] 身份证号：220303197009242283\n[BBOX-86] 职业：\n[BBOX-87] 体温 36.4 ℃ 血压 120/78 mmHg 脉搏 66 次/分\n[BBOX-88] 药物过敏史：否\n[BBOX-89] 主诉：发现血糖升高4年\n[BBOX-90] 病史：发现血糖升高4年，现二甲双胍片0.5g日3次口服控制血糖。测空腹血糖11.41mmol/L，糖化血红蛋白8.9%，尿糖3+。\n[BBOX-91] 临床诊断：2型糖尿病\n[BBOX-92] 治疗方案：建议患者入院治疗，患者暂拒；糖尿病饮食，口服二甲双胍片0.5g日3次，适当饮水，监测血糖，定期复查，病情变化随诊\n[BBOX-93] 结论：\n[BBOX-94] 病程记录：\n[BBOX-95] 医生（印章）：\n[BBOX-96] 2025年12月31日 15:12\n[BBOX-97] 四平市中心人民医院\n[BBOX-98] 常规通气+舒张试验\n[BBOX-99] 姓名：\n[BBOX-100] 年龄：53岁\n[BBOX-101] 住院号：111630435\n[BBOX-102] 身高：168 cm\n[BBOX-103] 性别：女\n[BBOX-104] 吸烟史：\n[BBOX-105] 测试号：20231227014\n[BBOX-106] 体重：82 kg\n[BBOX-107] Flow [L/s]\n[BBOX-108] F/V ex\n[BBOX-109] Vol [L]\n[BBOX-110] Vol%VCmax\n[BBOX-111] VCmax\n[BBOX-112] Time [s]\n[BBOX-113] F/V in\n[BBOX-114] 测试日期\n[BBOX-115] 测试时间\n[BBOX-116] 预计值\n[BBOX-117] 药前\n[BBOX-118] 前/预%\n[BBOX-119] 药后\n[BBOX-120] 后/预% 改善率 (%)\n[BBOX-121] 23/12/27\n[BBOX-122] 23/12/27\n[BBOX-123] 15:36:14\n[BBOX-124] 15:51:45\n[BBOX-125] MV\n[BBOX-126] [L/min]\n[BBOX-127] 11.71\n[BBOX-128] 27.39\n[BBOX-129] 233.8\n[BBOX-130] 3.78\n[BBOX-131] 115.4\n[BBOX-132] 7.6\n[BBOX-133] VC MAX\n[BBOX-134] [L]\n[BBOX-135] 3.28\n[BBOX-136] 3.52\n[BBOX-137] 107.3\n[BBOX-138] FVC\n[BBOX-139] [L]\n[BBOX-140] 3.17\n[BBOX-141] 3.52\n[BBOX-142] 110.8\n[BBOX-143] 3.78\n[BBOX-144] 119.2\n[BBOX-145] 7.6\n[BBOX-146] FEV 1\n[BBOX-147] [L]\n[BBOX-148] 2.71\n[BBOX-149] 2.11\n[BBOX-150] 77.7\n[BBOX-151] 2.39\n[BBOX-152] 88.3\n[BBOX-153] 13.7\n[BBOX-154] FEV 1 % FVC\n[BBOX-155] [%]\n[BBOX-156] 59.91\n[BBOX-157] 63.29\n[BBOX-158] 5.6\n[BBOX-159] FEV 1 % VC MAX\n[BBOX-160] [%]\n[BBOX-161] 79.03\n[BBOX-162] 59.91\n[BBOX-163] 75.8\n[BBOX-164] 63.29\n[BBOX-165] 80.1\n[BBOX-166] 5.6\n[BBOX-167] PEF\n[BBOX-168] [L/s]\n[BBOX-169] 6.54\n[BBOX-170] 4.76\n[BBOX-171] 72.7\n[BBOX-172] 4.54\n[BBOX-173] 69.4\n[BBOX-174] -4.6\n[BBOX-175] MEF 75\n[BBOX-176] [L/s]\n[BBOX-177] 5.68\n[BBOX-178] 2.64\n[BBOX-179] 46.4\n[BBOX-180] 3.29\n[BBOX-181] 58.0\n[BBOX-182] 24.9\n[BBOX-183] MEF 50\n[BBOX-184] [L/s]\n[BBOX-185] 3.95\n[BBOX-186] 1.40\n[BBOX-187] 35.4\n[BBOX-188] 1.80\n[BBOX-189] 45.5\n[BBOX-190] 28.5\n[BBOX-191] MEF 25\n[BBOX-192] [L/s]\n[BBOX-193] 1.55\n[BBOX-194] 0.53\n[BBOX-195] 34.2\n[BBOX-196] 0.65\n[BBOX-197] 42.1\n[BBOX-198] 22.9\n[BBOX-199] MMEF 75/25\n[BBOX-200] [L/s]\n[BBOX-201] 3.22\n[BBOX-202] 1.15\n[BBOX-203] 35.8\n[BBOX-204] 1.44\n[BBOX-205] 44.6\n[BBOX-206] 24.5\n[BBOX-207] MVV\n[BBOX-208] [L/min]\n[BBOX-209] 100.45\n[BBOX-210] 检查意见：\n[BBOX-211] 结果：支气管舒张实验(+)。\n[BBOX-212] 操作者签字：\n[BBOX-213] 医生签字：\n[BBOX-214] 四平市中心人民医院\n[BBOX-215] 常规通气\n[BBOX-216] 姓名：李洪燕\n[BBOX-217] 性别：女\n[BBOX-218] 年龄：53岁\n[BBOX-219] 吸烟史：\n[BBOX-220] 住院号：111630435\n[BBOX-221] 测试号：20231227014\n[BBOX-222] 身高：168 cm\n[BBOX-223] 体重：82 kg\n[BBOX-224] Flow [L/s]\n[BBOX-225] F/V ex\n[BBOX-226] Vol [L]\n[BBOX-227] Vol%Vmax\n[BBOX-228] VCmax\n[BBOX-229] F/V in\n[BBOX-230] Time [s]\n[BBOX-231] 测试日期\n[BBOX-232] 测试时间\n[BBOX-233] 预计值\n[BBOX-234] 实测值\n[BBOX-235] 实/预\n[BBOX-236] 23/12/27\n[BBOX-237] 15:36:14下午\n[BBOX-238] VT\n[BBOX-239] [L]\n[BBOX-240] 0.59\n[BBOX-241] 1.51\n[BBOX-242] 258.6\n[BBOX-243] BF\n[BBOX-244] [1/min]\n[BBOX-245] 20.00\n[BBOX-246] 18.08\n[BBOX-247] 90.4\n[BBOX-248] MV\n[BBOX-249] [L/min]\n[BBOX-250] 11.71\n[BBOX-251] 27.39\n[BBOX-252] 233.8\n[BBOX-253] VC MAX\n[BBOX-254] [L]\n[BBOX-255] 3.28\n[BBOX-256] 3.52\n[BBOX-257] 107.3\n[BBOX-258] ERV\n[BBOX-259] [L]\n[BBOX-260] 0.93\n[BBOX-261] 1.39\n[BBOX-262] 149.9\n[BBOX-263] IC\n[BBOX-264] [L]\n[BBOX-265] 2.35\n[BBOX-266] 2.13\n[BBOX-267] 90.5\n[BBOX-268] FVC\n[BBOX-269] [L]\n[BBOX-270] 3.17\n[BBOX-271] 3.52\n[BBOX-272] 110.8\n[BBOX-273] FEV 1\n[BBOX-274] [L]\n[BBOX-275] 2.71\n[BBOX-276] 2.11\n[BBOX-277] 77.7\n[BBOX-278] FEV 1 % FVC\n[BBOX-279] [%]\n[BBOX-280] 79.03\n[BBOX-281] 59.91\n[BBOX-282] 75.8\n[BBOX-283] FEV 1 % VC MAX\n[BBOX-284] [%]\n[BBOX-285] 6.54\n[BBOX-286] 4.76\n[BBOX-287] 72.7\n[BBOX-288] PEF\n[BBOX-289] [L/s]\n[BBOX-290] 5.68\n[BBOX-291] 2.64\n[BBOX-292] 46.4\n[BBOX-293] MEF 75\n[BBOX-294] [L/s]\n[BBOX-295] 3.95\n[BBOX-296] 1.40\n[BBOX-297] 35.4\n[BBOX-298] MEF 50\n[BBOX-299] [L/s]\n[BBOX-300] 1.55\n[BBOX-301] 0.53\n[BBOX-302] 34.2\n[BBOX-303] MEF 25\n[BBOX-304] [L/s]\n[BBOX-305] 3.22\n[BBOX-306] 1.15\n[BBOX-307] 35.8\n[BBOX-308] MMEF 75/25\n[BBOX-309] [L/s]\n[BBOX-310] 0.85\n[BBOX-311] 0.35\n[BBOX-312] 41.0\n[BBOX-313] FEF 75/85\n[BBOX-314] [L/s]\n[BBOX-315] 2.16\n[BBOX-316] 78.19\n[BBOX-317] PIF\n[BBOX-318] [L/s]\n[BBOX-319] FEF50 % FIF50\n[BBOX-320] [%]\n[BBOX-321] MVV\n[BBOX-322] [L/min]\n[BBOX-323] 100.45\n[BBOX-324] 63.19\n[BBOX-325] 62.9\n[BBOX-326] FEV 1*30\n[BBOX-327] [L/min]\n[BBOX-328] 100.45\n[BBOX-329] 检查意见：\n[BBOX-330] 轻度阻塞型通气功能障碍\n[BBOX-331] 小气道功能异常\n[BBOX-332] 操作者签字：\n[BBOX-333] 医生签字：\n[BBOX-334] 信康大药房--佳合分店\n[BBOX-335] 单号：250927207100156\n[BBOX-336] 日期：2025-09-27 17:52:20\n[BBOX-337] 会员卡号：13689710485\n[BBOX-338] 姓名：\n[BBOX-339] 积分：37\n[BBOX-340] 总积分：47\n[BBOX-341] 药品名称\n[BBOX-342] 规格\n[BBOX-343] 生产企业/药品上市许可持有人\n[BBOX-344] 产地\n[BBOX-345] 剂型\n[BBOX-346] 批号\n[BBOX-347] 有效期\n[BBOX-348] 数量\n[BBOX-349] 单价\n[BBOX-350] 金额\n[BBOX-351] 12534\n[BBOX-352] 185.00\n[BBOX-353] 沙美特罗替卡松吸入粉雾剂\n[BBOX-354] 50微克/250微克/60泡/盒\n[BBOX-355] 葛兰素史克集团吸入粉雾剂\n[BBOX-356] JD6K\n[BBOX-357] 2027-06-18\n[BBOX-358] 2盒\n[BBOX-359] 185.00\n[BBOX-360] 370.00\n[BBOX-361] 信康大药房温馨提示：您购买的\n[BBOX-362] 药品需要常温储存(10℃-30℃)\n[BBOX-363] 合计：\n[BBOX-364] 370.00\n[BBOX-365] 实收：\n[BBOX-366] 370.00\n[BBOX-367] 开票员：王影\n[BBOX-368] 营业员：7139\n[BBOX-369] 药品售出无质量问题不退不换！\n[BBOX-370] 电话：0434-3333658\n[BBOX-371] 信康大药房--佳合分店\n[BBOX-372] 单号：251128207100163\n[BBOX-373] 日期：2025-11-28 16:38:41\n[BBOX-374] 会员卡号：13689710485\n[BBOX-375] 姓名：\n[BBOX-376] 积分：37\n[BBOX-377] 总积分：84\n[BBOX-378] 药品名称\n[BBOX-379] 规格\n[BBOX-380] 生产企业/药品上市许可持有人\n[BBOX-381] 产地\n[BBOX-382] 剂型\n[BBOX-383] 批号\n[BBOX-384] 有效期\n[BBOX-385] 数量\n[BBOX-386] 单价\n[BBOX-387] 金额\n[BBOX-388] 12534\n[BBOX-389] 185.00\n[BBOX-390] 沙美特罗替卡松吸入粉雾剂\n[BBOX-391] 50微克/250微克/60泡/盒\n[BBOX-392] 葛兰素史克集团吸入粉雾剂\n[BBOX-393] JD6K\n[BBOX-394] 2027-06-18\n[BBOX-395] 2盒\n[BBOX-396] 185.00\n[BBOX-397] 370.00\n[BBOX-398] 信康大药房温馨提示：您购买的\n[BBOX-399] 药品需要常温储存（10℃-30℃）\n[BBOX-400] 合计：\n[BBOX-401] 370.00\n[BBOX-402] 实收：\n[BBOX-403] 370.00\n[BBOX-404] 开票员：张欣\n[BBOX-405] 营业员：7140\n[BBOX-406] 药品售出无质量问题不退不换！\n[BBOX-407] 电话：0434-3333658"
  }
]
2026-08-10 11:17:00,653 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:17:00,681 INFO     29 [SmartSplitter] SmartSplitter done: 7 chunks from 7 LLM segments (all bbox_id). Types: {'OutpatientRecord': 3, 'ExaminationReport': 2, 'MedicationRecord': 2}
2026-08-10 11:17:00,696 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 11:17:00,696 INFO     29 [Trace] task=e139f7cc | doc=LHYA-哮喘-沈阳医大四.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "408 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "chunks", "chunks": "7 items, types={'OutpatientRecord': 3, 'ExaminationReport': 2, 'MedicationRecord': 2}"}
2026-08-10 11:17:00,696 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 11:17:00,697 INFO     29 [ChunkRouter] Routed 7 chunks into 3 groups: {'chunks_Clinical': 3, 'chunks_Examination': 2, 'chunks_Medication': 2}
2026-08-10 11:17:00,798 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 11:17:00,801 INFO     29 [Trace] task=e139f7cc | doc=LHYA-哮喘-沈阳医大四.pdf | ChunkRouter:Router | outputs={"html": "", "json": "408 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "chunks", "chunks": "7 items, types={'OutpatientRecord': 3, 'ExaminationReport': 2, 'MedicationRecord': 2}", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Examination\": 2, \"chunks_Medication\": 2}"}
2026-08-10 11:17:00,801 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 11:17:00,820 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:17:00,820 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:17:01,621 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:17:01,634 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 11:17:01,634 INFO     29 [Trace] task=e139f7cc | doc=LHYA-哮喘-沈阳医大四.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "408 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Examination\": 2, \"chunks_Medication\": 2}"}
2026-08-10 11:17:01,634 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 11:17:01,640 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:17:01,640 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:17:02,104 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:17:02,118 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 11:17:02,118 INFO     29 [Trace] task=e139f7cc | doc=LHYA-哮喘-沈阳医大四.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "408 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Examination\": 2, \"chunks_Medication\": 2}"}
2026-08-10 11:17:02,119 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 11:17:02,131 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:17:02,133 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:17:02,133 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:17:02,133 INFO     29 [qwen-vl-text] positions(24): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:17:02,133 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [24]
2026-08-10 11:17:02,365 INFO     29 [qwen-vl-text] page=0, rect=595x1058, img=(1654x2940), dpi=200
2026-08-10 11:17:02,366 INFO     29 [qwen-vl-text] LLM extraction start, text_len=179
2026-08-10 11:17:02,366 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:17:02,366 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 23, \"encounter_dates\": [\"2023-12-27\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "四平市中心人民医院\n门诊诊断书\n0003316\n(患者保管)\nSPZXYy-JLLC-042\n姓名\n性别\n女\n年龄\n54岁\n单位\n诊断\n支气管哮喘\n病情诊断摘要依据\n发作性喘息30余年，双肺干\n啰音，诊断支气管哮喘\n医生处理意见\n1.平喘治疗\n2.随访\n医生签字：\n门诊部负责人签字：\n科主任签字：\n门诊部盖章：2023年12月27日\n(无公章和医生章无效)",
    "role": "user"
  }
]
2026-08-10 11:17:02,641 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:17:02.638+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 19, "failed": 0, "current": {"e139f7cc94ac11f1bd9827cf206dfa2d": {"id": "e139f7cc94ac11f1bd9827cf206dfa2d", "doc_id": "e0cfe59494ac11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "type": "pdf", "location": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "size": 4593431, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786360565919, "task_type": "dataflow", "root_trace_id": "a7e430023e6144f7a5a82bee44b10046", "root_traceparent": "00-a7e430023e6144f7a5a82bee44b10046-21836b890cf4bf02-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:17:03,695 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:17:03,695 INFO     29 [qwen-vl-text] LLM output (len=201):
{
  "encounter_date": "2023-12-27",
  "chief_complaint": "发作性喘息30余年",
  "present_illness": "发作性喘息30余年，双肺干啰音，诊断支气管哮喘",
  "past_history": null,
  "diagnosis": "支气管哮喘",
  "treatment_plan": "1.平喘治疗 2.随访"
}
2026-08-10 11:17:03,696 INFO     29 [qwen-vl-text] Updated encounter_dates=[2023-12-27]
2026-08-10 11:17:03,701 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1984927, prompt_len=864
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共24行）
["四平市中心人民医院", "门诊诊断书", "0003316", "(患者保管)", "SPZXYy-JLLC-042", "姓名", "性别", "女", "年龄", "54岁", "单位", "诊断", "支气管哮喘", "病情诊断摘要依据", "发作性喘息30余年，双肺干", "啰音，诊断支气管哮喘", "医生处理意见", "1.平喘治疗", "2.随访", "医生签字：", "门诊部负责人签字：", "科主任签字：", "门诊部盖章：2023年12月27日", "(无公章和医生章无效)"]

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
2026-08-10 11:17:12,520 INFO     29 [qwen-vl-text] coord API raw response (len=1262):
[
	{"text": "四平市中心人民医院", "bbox": [246, 198, 580, 214]},
	{"text": "门诊诊断书", "bbox": [122, 223, 381, 250]},
	{"text": "0003316", "bbox": [598, 231, 781, 252]},
	{"text": "(患者保管)", "bbox": [50, 272, 195, 289]},
	{"text": "SPZXYy-JLLC-042", "bbox": [575, 268, 831, 282]},
	{"text": "姓名", "bbox": [71, 300, 145, 318]},
	{"text": "性别", "bbox": [365, 300, 423, 317],
	"bbox": [365, 300, 423, 317]},
	{"text": "女", "bbox": [515, 303, 554, 322]},
	{"text": "年龄", "bbox": [615, 300, 672, 316]},
	{"text": "54岁", "bbox": [743, 298, 809, 324]},
	{"text": "单位", "bbox": [69, 334, 144, 351]},
	{"text": "诊断", "bbox": [67, 367, 142, 384]},
	{"text": "支气管哮喘", "bbox": [300, 365, 502, 398]},
	{"text": "病情诊断摘要依据", "bbox": [64, 451, 138, 536]},
	{"text": "发作性喘息30余年，双肺干", "bbox": [275, 400, 777, 440]},
	{"text": "啰音，诊断支气管哮喘", "bbox": [203, 437, 651, 477]},
	{"text": "医生处理意见", "bbox": [78, 632, 108, 769]},
	{"text": "1.平喘治疗", "bbox": [323, 608, 518, 644]},
	{"text": "2.随访", "bbox": [325, 647, 460, 687]},
	{"text": "医生签字：", "bbox": [183, 748, 291, 765]},
	{"text": "门诊部负责人签字：", "bbox": [497, 748, 703, 767]},
	{"text": "科主任签字：", "bbox": [182, 778, 315, 795]},
	{"text": "门诊部盖章：2023年12月27日", "bbox": [498, 778, 828, 798]},
	{"text": "(无公章和医生章无效)", "bbox": [75, 817, 378, 836]}
]
2026-08-10 11:17:12,521 INFO     29 [qwen-vl-text] coord API: raw_items=24, valid_items=24, elapsed=8.8s
2026-08-10 11:17:12,521 INFO     29 [qwen-vl-text] coord item[0]: text=四平市中心人民医院, bbox=[246, 198, 580, 214]
2026-08-10 11:17:12,521 INFO     29 [qwen-vl-text] coord item[1]: text=门诊诊断书, bbox=[122, 223, 381, 250]
2026-08-10 11:17:12,521 INFO     29 [qwen-vl-text] coord item[2]: text=0003316, bbox=[598, 231, 781, 252]
2026-08-10 11:17:12,522 INFO     29 [qwen-vl-text] coord item[3]: text=(患者保管), bbox=[50, 272, 195, 289]
2026-08-10 11:17:12,522 INFO     29 [qwen-vl-text] coord item[4]: text=SPZXYy-JLLC-042, bbox=[575, 268, 831, 282]
2026-08-10 11:17:12,522 INFO     29 [qwen-vl-text] coord item[5]: text=姓名, bbox=[71, 300, 145, 318]
2026-08-10 11:17:12,522 INFO     29 [qwen-vl-text] coord item[6]: text=性别, bbox=[365, 300, 423, 317]
2026-08-10 11:17:12,522 INFO     29 [qwen-vl-text] coord item[7]: text=女, bbox=[515, 303, 554, 322]
2026-08-10 11:17:12,522 INFO     29 [qwen-vl-text] coord item[8]: text=年龄, bbox=[615, 300, 672, 316]
2026-08-10 11:17:12,523 INFO     29 [qwen-vl-text] coord item[9]: text=54岁, bbox=[743, 298, 809, 324]
2026-08-10 11:17:12,523 INFO     29 [qwen-vl-text] coord item[10]: text=单位, bbox=[69, 334, 144, 351]
2026-08-10 11:17:12,523 INFO     29 [qwen-vl-text] coord item[11]: text=诊断, bbox=[67, 367, 142, 384]
2026-08-10 11:17:12,523 INFO     29 [qwen-vl-text] coord item[12]: text=支气管哮喘, bbox=[300, 365, 502, 398]
2026-08-10 11:17:12,523 INFO     29 [qwen-vl-text] coord item[13]: text=病情诊断摘要依据, bbox=[64, 451, 138, 536]
2026-08-10 11:17:12,523 INFO     29 [qwen-vl-text] coord item[14]: text=发作性喘息30余年，双肺干, bbox=[275, 400, 777, 440]
2026-08-10 11:17:12,523 INFO     29 [qwen-vl-text] coord item[15]: text=啰音，诊断支气管哮喘, bbox=[203, 437, 651, 477]
2026-08-10 11:17:12,523 INFO     29 [qwen-vl-text] coord item[16]: text=医生处理意见, bbox=[78, 632, 108, 769]
2026-08-10 11:17:12,523 INFO     29 [qwen-vl-text] coord item[17]: text=1.平喘治疗, bbox=[323, 608, 518, 644]
2026-08-10 11:17:12,523 INFO     29 [qwen-vl-text] coord item[18]: text=2.随访, bbox=[325, 647, 460, 687]
2026-08-10 11:17:12,523 INFO     29 [qwen-vl-text] coord item[19]: text=医生签字：, bbox=[183, 748, 291, 765]
2026-08-10 11:17:12,524 INFO     29 [qwen-vl-text] coord item[20]: text=门诊部负责人签字：, bbox=[497, 748, 703, 767]
2026-08-10 11:17:12,524 INFO     29 [qwen-vl-text] coord item[21]: text=科主任签字：, bbox=[182, 778, 315, 795]
2026-08-10 11:17:12,524 INFO     29 [qwen-vl-text] coord item[22]: text=门诊部盖章：2023年12月27日, bbox=[498, 778, 828, 798]
2026-08-10 11:17:12,524 INFO     29 [qwen-vl-text] coord item[23]: text=(无公章和医生章无效), bbox=[75, 817, 378, 836]
2026-08-10 11:17:12,524 INFO     29 [qwen-vl-text] page=0 — 24/24 coords, api_time=8.8s
2026-08-10 11:17:12,525 INFO     29 [qwen-vl-text] new_positions (24):
[[0, 146.43888720703123, 345.26241699218747, 209.5374638671875, 226.4697841796875], [0, 72.62416357421874, 226.80169116210936, 235.99421435546876, 264.5675048828125], [0, 355.97745751953124, 464.9137028808593, 244.46037451171875, 266.684044921875], [0, 29.764001464843748, 116.07960571289061, 287.8494453125, 305.84003564453127], [0, 342.2860168457031, 494.6777043457031, 283.616365234375, 298.4321455078125], [0, 42.264882080078124, 86.31560424804687, 317.481005859375, 336.5298662109375], [0, 217.27721069335936, 251.8034523925781, 317.481005859375, 335.47159619140626], [0, 306.5692150878906, 329.7851362304687, 320.65581591796877, 340.7629462890625], [0, 366.0972180175781, 400.02817968749997, 317.481005859375, 334.413326171875], [0, 442.2930617675781, 481.5815437011718, 315.3644658203125, 342.879486328125], [0, 41.07432202148437, 85.72032421875, 353.4621865234375, 371.45277685546876], [0, 39.883761962890624, 84.52976416015625, 388.38509716796875, 406.3756875], [0, 178.5840087890625, 298.83057470703125, 386.26855712890625, 421.1914677734375], [0, 38.097921875, 82.14864404296874, 477.27977880859373, 567.23273046875], [0, 163.7020080566406, 462.5325827636718, 423.3080078125, 465.63880859375], [0, 120.84184594726561, 387.5272990722656, 462.46399853515624, 504.7947993164062], [0, 46.43184228515625, 64.2902431640625, 668.82665234375, 813.8096450195312], [0, 192.2754494628906, 308.3550551757812, 643.428171875, 681.525892578125], [0, 193.46600952148435, 273.82881347656246, 684.7007026367188, 727.0315034179688], [0, 108.93624536132812, 173.2264885253906, 791.585974609375, 809.5765649414062], [0, 295.8541745605469, 418.4818605957031, 791.585974609375, 811.6931049804688], [0, 108.34096533203125, 187.51320922851562, 823.3340751953125, 841.3246655273438], [0, 296.44945458984375, 492.8918642578125, 823.3340751953125, 844.4994755859375], [0, 44.646002197265624, 225.01585107421874, 864.6066059570312, 884.713736328125]]
2026-08-10 11:17:12,525 INFO     29 [qwen-vl-text] ═══ DONE ═══ 24 positions, pages=1, time=10.4s
2026-08-10 11:17:12,525 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:17:12,528 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:17:12,528 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:17:12,528 INFO     29 [qwen-vl-text] positions(44): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:17:12,528 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [44]
2026-08-10 11:17:12,708 INFO     29 [qwen-vl-text] page=1, rect=842x592, img=(2339x1644), dpi=200
2026-08-10 11:17:12,709 INFO     29 [qwen-vl-text] LLM extraction start, text_len=502
2026-08-10 11:17:12,709 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:17:12,710 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 24, \"bbox_end\": 67, \"encounter_dates\": [\"2025-11-26\"], \"department\": \"肾病糖尿病科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "四平市中医医院\n门诊病历\n初诊\n2025年11月26日\n肾病糖尿病科\n姓名\n性别\n女性\n年龄\n55岁\n门诊号码\n202511260272\n（1）\n发病日期\n2025-11-26\n类别\n自费\n保险卡号\n就诊方式\n便民门诊费\n医生\n王亚新\n联系地址\n四平铁西\n联系电话\n13689710485\n身份证号\n职业\n体温 36.5 ℃ 血压 130、80 mmHg 脉搏 70 次/分\n药物过敏史\n无\n主诉:\n自述糖尿病4年，支气管哮喘30余年\n病史:\n糖尿病4年，尿中有沫。伴双下肢水肿+。现二甲双胍片，0.5，日3次，口服。血糖控制不佳。葡萄糖：12.39mmol/1.，糖化：\n10.1%，一周前感冒山现间断咳嗽气短胸闷，活动后加重，有夜间憋醒史，咳白痰，无发热，饮食尚可，大小便正常。\n临床诊断：2型糖尿病 支气管哮喘急性发作\n治疗方案:\n建议入院治疗，拒绝。糖尿病饮食，监测血糖，继续用药治疗，有变化随诊。沙美特罗卡替松粉吸入剂50微克/250微克/揿/盒，\n每瓶60揿（30个用药计量），甲泼尼龙片4mg×24片/盒（口服5天）。\n结论:\n病程记录:\n医生（印章）：\n2025年11月27日 11:18",
    "role": "user"
  }
]
2026-08-10 11:17:15,636 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:17:15,636 INFO     29 [qwen-vl-text] LLM output (len=399):
{
  "encounter_date": "2025-11-26",
  "chief_complaint": "自述糖尿病4年，支气管哮喘30余年",
  "present_illness": "糖尿病4年，尿中有沫。伴双下肢水肿+。现二甲双胍片，0.5，日3次，口服。血糖控制不佳。葡萄糖：12.39mmol/1.，糖化：10.1%，一周前感冒山现间断咳嗽气短胸闷，活动后加重，有夜间憋醒史，咳白痰，无发热，饮食尚可，大小便正常。",
  "past_history": null,
  "diagnosis": "2型糖尿病 支气管哮喘急性发作",
  "treatment_plan": "建议入院治疗，拒绝。糖尿病饮食，监测血糖，继续用药治疗，有变化随诊。沙美特罗卡替松粉吸入剂50微克/250微克/揿/盒，每瓶60揿（30个用药计量），甲泼尼龙片4mg×24片/盒（口服5天）。"
}
2026-08-10 11:17:15,636 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-26]
2026-08-10 11:17:15,639 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1404155, prompt_len=1247
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共44行）
["四平市中医医院", "门诊病历", "初诊", "2025年11月26日", "肾病糖尿病科", "姓名", "性别", "女性", "年龄", "55岁", "门诊号码", "202511260272", "（1）", "发病日期", "2025-11-26", "类别", "自费", "保险卡号", "就诊方式", "便民门诊费", "医生", "王亚新", "联系地址", "四平铁西", "联系电话", "13689710485", "身份证号", "职业", "体温 36.5 ℃ 血压 130、80 mmHg 脉搏 70 次/分", "药物过敏史", "无", "主诉:", "自述糖尿病4年，支气管哮喘30余年", "病史:", "糖尿病4年，尿中有沫。伴双下肢水肿+。现二甲双胍片，0.5，日3次，口服。血糖控制不佳。葡萄糖：12.39mmol/1.，糖化：", "10.1%，一周前感冒山现间断咳嗽气短胸闷，活动后加重，有夜间憋醒史，咳白痰，无发热，饮食尚可，大小便正常。", "临床诊断：2型糖尿病 支气管哮喘急性发作", "治疗方案:", "建议入院治疗，拒绝。糖尿病饮食，监测血糖，继续用药治疗，有变化随诊。沙美特罗卡替松粉吸入剂50微克/250微克/揿/盒，", "每瓶60揿（30个用药计量），甲泼尼龙片4mg×24片/盒（口服5天）。", "结论:", "病程记录:", "医生（印章）：", "2025年11月27日 11:18"]

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
2026-08-10 11:17:28,869 INFO     29 [qwen-vl-text] coord API raw response (len=2459):
[
	{"text": "四平市中医医院", "bbox": [448, 122, 565, 149]},
	{"text": "门诊病历", "bbox": [458, 158, 555, 196]},
	{"text": "初诊", "bbox": [818, 117, 854, 143]},
	{"text": "2025年11月26日", "bbox": [774, 154, 896, 185]},
	{"text": "肾病糖尿病科", "bbox": [93, 178, 192, 204]},
	{"text": "姓名", "bbox": [86, 227, 115, 247]},
	{"text": "性别", "bbox": [276, 223, 306, 244]},
	{"text": "女性", "bbox": [331, 223, 362, 244]},
	{"text": "年龄", "bbox": [386, 222, 415, 243]},
	{"text": "55岁", "bbox": [443, 222, 473, 243]},
	{"text": "门诊号码", "bbox": [502, 219, 558, 241]},
	{"text": "202511260272", "bbox": [587, 217, 685, 240]},
	{"text": "（1）", "bbox": [705, 211, 751, 240]},
	{"text": "发病日期", "bbox": [765, 207, 828, 232]},
	{"text": "2025-11-26", "bbox": [837, 206, 918, 229]},
	{"text": "类别", "bbox": [87, 273, 115, 293]},
	{"text": "自费", "bbox": [164, 271, 191, 291]},
	{"text": "保险卡号", "bbox": [271, 269, 330, 290]},
	{"text": "就诊方式", "bbox": [502, 265, 558, 287]},
	{"text": "便民门诊费", "bbox": [635, 260, 707, 283]},
	{"text": "医生", "bbox": [792, 257, 820, 277]},
	{"text": "王亚新", "bbox": [858, 254, 901, 275]},
	{"text": "联系地址", "bbox": [97, 321, 152, 342]},
	{"text": "四平铁西", "bbox": [180, 320, 236, 341]},
	{"text": "联系电话", "bbox": [581, 313, 638, 335]},
	{"text": "13689710485", "bbox": [660, 311, 740, 332]},
	{"text": "身份证号", "bbox": [97, 366, 152, 387]},
	{"text": "职业", "bbox": [354, 363, 384, 384]},
	{"text": "体温 36.5 ℃ 血压 130、80 mmHg 脉搏 70 次/分", "bbox": [578, 349, 918, 377]},
	{"text": "药物过敏史", "bbox": [90, 411, 159, 432]},
	{"text": "无", "bbox": [180, 410, 194, 431]},
	{"text": "主诉:", "bbox": [87, 453, 119, 473]},
	{"text": "自述糖尿病4年，支气管哮喘30余年", "bbox": [147, 451, 353, 472]},
	{"text": "病史:", "bbox": [87, 488, 119, 508]},
	{"text": "糖尿病4年，尿中有沫。伴双下肢水肿+。现二甲双胍片，0.5，日3次，口服。血糖控制不佳。葡萄糖：12.39mmol/1.，糖化：", "bbox": [146, 476, 897, 500]},
	{"text": "10.1%，一周前感冒山现间断咳嗽气短胸闷，活动后加重，有夜间憋醒史，咳白痰，无发热，饮食尚可，大小便正常。", "bbox": [147, 503, 780, 524]},
	{"text": "临床诊断：2型糖尿病 支气管哮喘急性发作", "bbox": [85, 633, 329, 654]},
	{"text": "治疗方案:", "bbox": [85, 668, 143, 689]},
	{"text": "建议入院治疗，拒绝。糖尿病饮食，监测血糖，继续用药治疗，有变化随诊。沙美特罗卡替松粉吸入剂50微克/250微克/揿/盒，", "bbox": [112, 689, 852, 711]},
	{"text": "每瓶60揿（30个用药计量），甲泼尼龙片4mg×24片/盒（口服5天）。", "bbox": [111, 711, 521, 733]},
	{"text": "结论:", "bbox": [86, 908, 117, 928]},
	{"text": "病程记录:", "bbox": [86, 950, 144, 970]},
	{"text": "医生（印章）：", "bbox": [518, 950, 610, 973], "bbox": [614, 918, 712, 975]},
	{"text": "2025年11月27日 11:18", "bbox": [764, 956, 908, 979]}
]
2026-08-10 11:17:28,869 INFO     29 [qwen-vl-text] coord API: raw_items=44, valid_items=44, elapsed=13.2s
2026-08-10 11:17:28,869 INFO     29 [qwen-vl-text] coord item[0]: text=四平市中医医院, bbox=[448, 122, 565, 149]
2026-08-10 11:17:28,869 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[458, 158, 555, 196]
2026-08-10 11:17:28,869 INFO     29 [qwen-vl-text] coord item[2]: text=初诊, bbox=[818, 117, 854, 143]
2026-08-10 11:17:28,869 INFO     29 [qwen-vl-text] coord item[3]: text=2025年11月26日, bbox=[774, 154, 896, 185]
2026-08-10 11:17:28,869 INFO     29 [qwen-vl-text] coord item[4]: text=肾病糖尿病科, bbox=[93, 178, 192, 204]
2026-08-10 11:17:28,869 INFO     29 [qwen-vl-text] coord item[5]: text=姓名, bbox=[86, 227, 115, 247]
2026-08-10 11:17:28,869 INFO     29 [qwen-vl-text] coord item[6]: text=性别, bbox=[276, 223, 306, 244]
2026-08-10 11:17:28,869 INFO     29 [qwen-vl-text] coord item[7]: text=女性, bbox=[331, 223, 362, 244]
2026-08-10 11:17:28,869 INFO     29 [qwen-vl-text] coord item[8]: text=年龄, bbox=[386, 222, 415, 243]
2026-08-10 11:17:28,869 INFO     29 [qwen-vl-text] coord item[9]: text=55岁, bbox=[443, 222, 473, 243]
2026-08-10 11:17:28,869 INFO     29 [qwen-vl-text] coord item[10]: text=门诊号码, bbox=[502, 219, 558, 241]
2026-08-10 11:17:28,869 INFO     29 [qwen-vl-text] coord item[11]: text=202511260272, bbox=[587, 217, 685, 240]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[12]: text=（1）, bbox=[705, 211, 751, 240]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[13]: text=发病日期, bbox=[765, 207, 828, 232]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[14]: text=2025-11-26, bbox=[837, 206, 918, 229]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[15]: text=类别, bbox=[87, 273, 115, 293]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[16]: text=自费, bbox=[164, 271, 191, 291]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[17]: text=保险卡号, bbox=[271, 269, 330, 290]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[18]: text=就诊方式, bbox=[502, 265, 558, 287]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[19]: text=便民门诊费, bbox=[635, 260, 707, 283]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[20]: text=医生, bbox=[792, 257, 820, 277]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[21]: text=王亚新, bbox=[858, 254, 901, 275]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[22]: text=联系地址, bbox=[97, 321, 152, 342]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[23]: text=四平铁西, bbox=[180, 320, 236, 341]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[24]: text=联系电话, bbox=[581, 313, 638, 335]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[25]: text=13689710485, bbox=[660, 311, 740, 332]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[26]: text=身份证号, bbox=[97, 366, 152, 387]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[27]: text=职业, bbox=[354, 363, 384, 384]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[28]: text=体温 36.5 ℃ 血压 130、80 mmHg 脉搏 70 次/分, bbox=[578, 349, 918, 377]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[29]: text=药物过敏史, bbox=[90, 411, 159, 432]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[30]: text=无, bbox=[180, 410, 194, 431]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[31]: text=主诉:, bbox=[87, 453, 119, 473]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[32]: text=自述糖尿病4年，支气管哮喘30余年, bbox=[147, 451, 353, 472]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[33]: text=病史:, bbox=[87, 488, 119, 508]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[34]: text=糖尿病4年，尿中有沫。伴双下肢水肿+。现二甲双胍片，0.5，日3次，口服。血糖控制不佳。葡萄糖：12.39mmol/1.，糖化：, bbox=[146, 476, 897, 500]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[35]: text=10.1%，一周前感冒山现间断咳嗽气短胸闷，活动后加重，有夜间憋醒史，咳白痰，无发热，饮食尚可，大小便正常。, bbox=[147, 503, 780, 524]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[36]: text=临床诊断：2型糖尿病 支气管哮喘急性发作, bbox=[85, 633, 329, 654]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[37]: text=治疗方案:, bbox=[85, 668, 143, 689]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[38]: text=建议入院治疗，拒绝。糖尿病饮食，监测血糖，继续用药治疗，有变化随诊。沙美特罗卡替松粉吸入剂50微克/250微克/揿/盒，, bbox=[112, 689, 852, 711]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[39]: text=每瓶60揿（30个用药计量），甲泼尼龙片4mg×24片/盒（口服5天）。, bbox=[111, 711, 521, 733]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[40]: text=结论:, bbox=[86, 908, 117, 928]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[41]: text=病程记录:, bbox=[86, 950, 144, 970]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[42]: text=医生（印章）：, bbox=[614, 918, 712, 975]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] coord item[43]: text=2025年11月27日 11:18, bbox=[764, 956, 908, 979]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] page=1 — 44/44 coords, api_time=13.2s
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] new_positions (44):
[[1, 377.1667265625, 475.66785827636716, 72.19594238281249, 88.17373291015625], [1, 385.58562670898436, 467.2489581298828, 93.4996630859375, 115.986923828125], [1, 688.6660319824218, 718.9740725097656, 69.23709228515625, 84.62311279296874], [1, 651.6228713378906, 754.333453125, 91.1325830078125, 109.47745361328124], [1, 78.29577136230469, 161.6428828125, 105.3350634765625, 120.721083984375], [1, 72.40254125976563, 96.81735168457031, 134.33179443359376, 146.16719482421874], [1, 232.36164404296875, 257.6183444824219, 131.96471435546874, 144.39188476562498], [1, 278.6655948486328, 304.76418530273435, 131.96471435546874, 144.39188476562498], [1, 324.9695456542969, 349.38435607910156, 131.3729443359375, 143.80011474609375], [1, 372.9572764892578, 398.2139769287109, 131.3729443359375, 143.80011474609375], [1, 422.62878735351563, 469.7746281738281, 129.59763427734373, 142.61657470703125], [1, 494.1894385986328, 576.6946600341797, 128.41409423828125, 142.0248046875], [1, 593.5324603271484, 632.2594010009766, 124.86347412109374, 142.0248046875], [1, 644.0458612060547, 697.0849321289062, 122.49639404296875, 137.29064453125], [1, 704.6619422607422, 772.8550334472657, 121.90462402343749, 135.51533447265624], [1, 73.24443127441405, 96.81735168457031, 161.55321533203124, 173.38861572265625], [1, 138.06996240234375, 160.80099279785156, 160.36967529296874, 172.20507568359375], [1, 228.15219396972657, 277.8237048339844, 159.18613525390623, 171.6133056640625], [1, 422.62878735351563, 469.7746281738281, 156.81905517578124, 169.83799560546873], [1, 534.6001593017578, 595.2162403564453, 153.860205078125, 167.47091552734375], [1, 666.7768916015625, 690.3498120117188, 152.08489501953125, 163.92029541015623], [1, 722.3416325683594, 758.5429031982421, 150.30958496093749, 162.73675537109375], [1, 81.66333142089843, 127.9672822265625, 189.95817626953124, 202.3853466796875], [1, 151.54020263671876, 198.68604345703125, 189.36640624999998, 201.79357666015625], [1, 489.13809851074217, 537.1258293457031, 185.22401611328124, 198.24295654296873], [1, 555.6474096679688, 622.9986108398438, 184.04047607421873, 196.467646484375], [1, 81.66333142089843, 127.9672822265625, 216.5878271484375, 229.01499755859373], [1, 298.02906518554687, 323.285765625, 214.81251708984374, 227.2396875], [1, 486.61242846679687, 772.8550334472657, 206.52773681640625, 223.09729736328123], [1, 75.77010131835938, 133.86051232910157, 243.21747802734373, 255.6446484375], [1, 151.54020263671876, 163.32666284179686, 242.62570800781248, 255.05287841796874], [1, 73.24443127441405, 100.18491174316407, 268.07181884765623, 279.90721923828124], [1, 123.75783215332031, 297.18717517089846, 266.8882788085937, 279.31544921874996], [1, 73.24443127441405, 100.18491174316407, 288.78376953124996, 300.61916992187497], [1, 122.91594213867188, 755.1753431396485, 281.682529296875, 295.885009765625], [1, 123.75783215332031, 656.6742114257812, 297.66031982421873, 310.08749023437497], [1, 71.56065124511719, 276.9818148193359, 374.5904223632812, 387.01759277343746], [1, 71.56065124511719, 120.39027209472655, 395.302373046875, 407.72954345703124], [1, 94.291681640625, 717.2902924804688, 407.72954345703124, 420.7484838867187], [1, 93.44979162597656, 438.62469763183594, 420.7484838867187, 433.7674243164062], [1, 72.40254125976563, 98.50113171386718, 537.327177734375, 549.162578125], [1, 72.40254125976563, 121.232162109375, 562.1815185546875, 574.0169189453125], [1, 516.9204689941406, 599.4256904296875, 543.2448779296875, 576.9757690429688], [1, 643.2039711914063, 764.4361333007812, 565.732138671875, 579.3428491210938]]
2026-08-10 11:17:28,870 INFO     29 [qwen-vl-text] ═══ DONE ═══ 44 positions, pages=1, time=16.3s
2026-08-10 11:17:28,870 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:17:28,872 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:17:28,872 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:17:28,872 INFO     29 [qwen-vl-text] positions(29): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:17:28,872 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [29]
2026-08-10 11:17:29,137 INFO     29 [qwen-vl-text] page=2, rect=842x611, img=(2339x1697), dpi=200
2026-08-10 11:17:29,138 INFO     29 [qwen-vl-text] LLM extraction start, text_len=400
2026-08-10 11:17:29,138 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:17:29,138 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 68, \"bbox_end\": 96, \"encounter_dates\": [\"2025-12-31\"], \"department\": \"内二疗区\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "四平市中医医院\n内二疗区\n门诊病历\n初诊\n2025年12月31日\n姓名\n性别：女性\n年龄：55岁\n门诊号码：202512310183\n（1）\n发病日期：2025-12-31\n类别：自费\n保险卡号\n就诊方式：服务号\n医生：张楷婷\n联系地址：吉林省四平市\n联系电话：13689710485\n身份证号：220303197009242283\n职业：\n体温 36.4 ℃ 血压 120/78 mmHg 脉搏 66 次/分\n药物过敏史：否\n主诉：发现血糖升高4年\n病史：发现血糖升高4年，现二甲双胍片0.5g日3次口服控制血糖。测空腹血糖11.41mmol/L，糖化血红蛋白8.9%，尿糖3+。\n临床诊断：2型糖尿病\n治疗方案：建议患者入院治疗，患者暂拒；糖尿病饮食，口服二甲双胍片0.5g日3次，适当饮水，监测血糖，定期复查，病情变化随诊\n结论：\n病程记录：\n医生（印章）：\n2025年12月31日 15:12",
    "role": "user"
  }
]
2026-08-10 11:17:31,314 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:17:31,314 INFO     29 [qwen-vl-text] LLM output (len=284):
{
  "encounter_date": "2025-12-31",
  "chief_complaint": "发现血糖升高4年",
  "present_illness": "发现血糖升高4年，现二甲双胍片0.5g日3次口服控制血糖。测空腹血糖11.41mmol/L，糖化血红蛋白8.9%，尿糖3+。",
  "past_history": null,
  "diagnosis": "2型糖尿病",
  "treatment_plan": "建议患者入院治疗，患者暂拒；糖尿病饮食，口服二甲双胍片0.5g日3次，适当饮水，监测血糖，定期复查，病情变化随诊"
}
2026-08-10 11:17:31,314 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-31]
2026-08-10 11:17:31,317 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1982923, prompt_len=1100
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["四平市中医医院", "内二疗区", "门诊病历", "初诊", "2025年12月31日", "姓名", "性别：女性", "年龄：55岁", "门诊号码：202512310183", "（1）", "发病日期：2025-12-31", "类别：自费", "保险卡号", "就诊方式：服务号", "医生：张楷婷", "联系地址：吉林省四平市", "联系电话：13689710485", "身份证号：220303197009242283", "职业：", "体温 36.4 ℃ 血压 120/78 mmHg 脉搏 66 次/分", "药物过敏史：否", "主诉：发现血糖升高4年", "病史：发现血糖升高4年，现二甲双胍片0.5g日3次口服控制血糖。测空腹血糖11.41mmol/L，糖化血红蛋白8.9%，尿糖3+。", "临床诊断：2型糖尿病", "治疗方案：建议患者入院治疗，患者暂拒；糖尿病饮食，口服二甲双胍片0.5g日3次，适当饮水，监测血糖，定期复查，病情变化随诊", "结论：", "病程记录：", "医生（印章）：", "2025年12月31日 15:12"]

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
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord API raw response (len=1668):
[
	{"text": "四平市中医医院", "bbox": [453, 103, 575, 130]},
	{"text": "内二疗区", "bbox": [92, 143, 163, 167]},
	{"text": "门诊病历", "bbox": [463, 140, 563, 175]},
	{"text": "初诊", "bbox": [825, 122, 860, 144]},
	{"text": "2025年12月31日", "bbox": [781, 156, 903, 180]},
	{"text": "姓名", "bbox": [86, 187, 118, 208]},
	{"text": "性别：女性", "bbox": [281, 190, 366, 214]},
	{"text": "年龄：55岁", "bbox": [387, 192, 482, 217]},
	{"text": "门诊号码：202512310183", "bbox": [508, 197, 697, 221]},
	{"text": "（1）", "bbox": [713, 198, 760, 224]},
	{"text": "发病日期：2025-12-31", "bbox": [772, 199, 926, 225]},
	{"text": "类别：自费", "bbox": [85, 232, 214, 256]},
	{"text": "保险卡号", "bbox": [277, 236, 335, 259]},
	{"text": "就诊方式：服务号", "bbox": [508, 242, 702, 266]},
	{"text": "医生：张楷婷", "bbox": [800, 246, 910, 269]},
	{"text": "联系地址：吉林省四平市", "bbox": [95, 279, 272, 303]},
	{"text": "联系电话：13689710485", "bbox": [590, 290, 750, 312]},
	{"text": "身份证号：220303197009242283", "bbox": [95, 322, 317, 346]},
	{"text": "职业：", "bbox": [359, 328, 391, 349]},
	{"text": "体温 36.4 ℃ 血压 120/78 mmHg 脉搏 66 次/分", "bbox": [585, 330, 928, 355]},
	{"text": "药物过敏史：否", "bbox": [87, 365, 198, 388]},
	{"text": "主诉：发现血糖升高4年", "bbox": [84, 405, 258, 428]},
	{"text": "病史：发现血糖升高4年，现二甲双胍片0.5g日3次口服控制血糖。测空腹血糖11.41mmol/L，糖化血红蛋白8.9%，尿糖3+。", "bbox": [83, 438, 794, 478]},
	{"text": "临床诊断：2型糖尿病", "bbox": [82, 577, 221, 599]},
	{"text": "治疗方案：建议患者入院治疗，患者暂拒；糖尿病饮食，口服二甲双胍片0.5g日3次，适当饮水，监测血糖，定期复查，病情变化随诊", "bbox": [111, 636, 874, 666]},
	{"text": "结论：", "bbox": [82, 846, 117, 867]},
	{"text": "病程记录：", "bbox": [82, 886, 145, 907]},
	{"text": "医生（印章）：", "bbox": [528, 888, 621, 914]},
	{"text": "2025年12月31日 15:12", "bbox": [780, 897, 923, 918]}
]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=9.4s
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[0]: text=四平市中医医院, bbox=[453, 103, 575, 130]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[1]: text=内二疗区, bbox=[92, 143, 163, 167]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[2]: text=门诊病历, bbox=[463, 140, 563, 175]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[3]: text=初诊, bbox=[825, 122, 860, 144]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[4]: text=2025年12月31日, bbox=[781, 156, 903, 180]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[5]: text=姓名, bbox=[86, 187, 118, 208]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[6]: text=性别：女性, bbox=[281, 190, 366, 214]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[7]: text=年龄：55岁, bbox=[387, 192, 482, 217]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[8]: text=门诊号码：202512310183, bbox=[508, 197, 697, 221]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[9]: text=（1）, bbox=[713, 198, 760, 224]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[10]: text=发病日期：2025-12-31, bbox=[772, 199, 926, 225]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[11]: text=类别：自费, bbox=[85, 232, 214, 256]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[12]: text=保险卡号, bbox=[277, 236, 335, 259]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[13]: text=就诊方式：服务号, bbox=[508, 242, 702, 266]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[14]: text=医生：张楷婷, bbox=[800, 246, 910, 269]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[15]: text=联系地址：吉林省四平市, bbox=[95, 279, 272, 303]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[16]: text=联系电话：13689710485, bbox=[590, 290, 750, 312]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[17]: text=身份证号：220303197009242283, bbox=[95, 322, 317, 346]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[18]: text=职业：, bbox=[359, 328, 391, 349]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[19]: text=体温 36.4 ℃ 血压 120/78 mmHg 脉搏 66 次/分, bbox=[585, 330, 928, 355]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[20]: text=药物过敏史：否, bbox=[87, 365, 198, 388]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[21]: text=主诉：发现血糖升高4年, bbox=[84, 405, 258, 428]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[22]: text=病史：发现血糖升高4年，现二甲双胍片0.5g日3次口服控制血糖。测空腹血糖11.41mmol/L，糖化血红蛋白8.9%，尿糖3+。, bbox=[83, 438, 794, 478]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[23]: text=临床诊断：2型糖尿病, bbox=[82, 577, 221, 599]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[24]: text=治疗方案：建议患者入院治疗，患者暂拒；糖尿病饮食，口服二甲双胍片0.5g日3次，适当饮水，监测血糖，定期复查，病情变化随诊, bbox=[111, 636, 874, 666]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[25]: text=结论：, bbox=[82, 846, 117, 867]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[26]: text=病程记录：, bbox=[82, 886, 145, 907]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[27]: text=医生（印章）：, bbox=[528, 888, 621, 914]
2026-08-10 11:17:40,749 INFO     29 [qwen-vl-text] coord item[28]: text=2025年12月31日 15:12, bbox=[780, 897, 923, 918]
2026-08-10 11:17:40,750 INFO     29 [qwen-vl-text] page=2 — 29/29 coords, api_time=9.4s
2026-08-10 11:17:40,750 INFO     29 [qwen-vl-text] new_positions (29):
[[2, 381.3761766357422, 484.0867584228516, 62.90828100585937, 79.39880126953125], [2, 77.45388134765625, 137.2280723876953, 87.33868139648436, 101.99692163085936], [2, 389.79507678222654, 473.98407824707033, 85.5064013671875, 106.88300170898437], [2, 694.5592620849609, 724.0254125976562, 74.51272119140624, 87.94944140624999], [2, 657.5161014404297, 760.2266832275391, 95.27856152343749, 109.93680175781249], [2, 72.40254125976563, 99.34302172851562, 114.21212182617187, 127.03808203124998], [2, 236.57109411621093, 308.1317453613281, 116.04440185546873, 130.70264208984375], [2, 325.8114356689453, 405.79098706054685, 117.26592187499999, 132.53492211914062], [2, 427.6801274414062, 586.7973402099609, 120.31972192382811, 134.97796215820313], [2, 600.267580444336, 639.8364111328125, 120.93048193359374, 136.8102421875], [2, 649.9390913085938, 779.5901535644531, 121.54124194335937, 137.4210021972656], [2, 71.56065124511719, 180.1644631347656, 141.69632226562499, 156.3545625], [2, 233.2035340576172, 282.03315490722656, 144.1393623046875, 158.18684252929685], [2, 427.6801274414062, 591.0067902832031, 147.80392236328123, 162.46216259765623], [2, 673.51201171875, 766.1199133300781, 150.24696240234374, 164.2944426269531], [2, 79.97955139160156, 228.994083984375, 170.40204272460937, 185.06028295898435], [2, 496.7151086425781, 631.4175109863281, 177.12040283203123, 190.55712304687498], [2, 79.97955139160156, 266.87913464355466, 196.66472314453122, 211.32296337890622], [2, 302.23851525878905, 329.1789957275391, 200.329283203125, 213.15524340820312], [2, 492.50565856933594, 781.27393359375, 201.55080322265624, 216.81980346679686], [2, 73.24443127441405, 166.69422290039063, 222.9274035644531, 236.9748837890625], [2, 70.71876123046874, 217.20762377929688, 247.3578039550781, 261.4052841796875], [2, 69.87687121582032, 668.4606716308593, 267.51288427734374, 291.9432846679687], [2, 69.03498120117187, 186.05769323730468, 352.40852563476557, 365.84524584960934], [2, 93.44979162597656, 735.8118728027343, 388.4433662109375, 406.7661665039062], [2, 69.03498120117187, 98.50113171386718, 516.7029682617188, 529.5289284667969], [2, 69.03498120117187, 122.07405212402344, 541.1333686523437, 553.9593288574218], [2, 444.517927734375, 522.8136990966797, 542.354888671875, 558.2346489257812], [2, 656.6742114257812, 777.0644835205078, 547.8517287597656, 560.6776889648437]]
2026-08-10 11:17:40,750 INFO     29 [qwen-vl-text] ═══ DONE ═══ 29 positions, pages=1, time=11.9s
2026-08-10 11:17:40,764 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 11:17:40,764 INFO     29 [Trace] task=e139f7cc | doc=LHYA-哮喘-沈阳医大四.pdf | Extractor:Clinical | outputs={"chunks": "3 items, types={'OutpatientRecord': 3}", "html": "", "json": "408 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Examination\": 2, \"chunks_Medication\": 2}"}
2026-08-10 11:17:40,764 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 11:17:40,764 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:17:40.764+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 19, "failed": 0, "current": {"e139f7cc94ac11f1bd9827cf206dfa2d": {"id": "e139f7cc94ac11f1bd9827cf206dfa2d", "doc_id": "e0cfe59494ac11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "type": "pdf", "location": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "size": 4593431, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786360565919, "task_type": "dataflow", "root_trace_id": "a7e430023e6144f7a5a82bee44b10046", "root_traceparent": "00-a7e430023e6144f7a5a82bee44b10046-21836b890cf4bf02-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:17:40,773 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:17:40,774 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:17:40,774 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 11:17:40,774 INFO     29 [qwen-vl-text] positions(37): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:17:40,774 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [37]
2026-08-10 11:17:41,280 INFO     29 [qwen-vl-text] page=5, rect=595x1492, img=(1654x4145), dpi=200
2026-08-10 11:17:41,281 INFO     29 [qwen-vl-text] LLM extraction start, text_len=323
2026-08-10 11:17:41,281 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:17:41,282 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 334, \"bbox_end\": 370, \"encounter_dates\": [\"2025-09-27\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "信康大药房--佳合分店\n单号：250927207100156\n日期：2025-09-27 17:52:20\n会员卡号：13689710485\n姓名：\n积分：37\n总积分：47\n药品名称\n规格\n生产企业/药品上市许可持有人\n产地\n剂型\n批号\n有效期\n数量\n单价\n金额\n12534\n185.00\n沙美特罗替卡松吸入粉雾剂\n50微克/250微克/60泡/盒\n葛兰素史克集团吸入粉雾剂\nJD6K\n2027-06-18\n2盒\n185.00\n370.00\n信康大药房温馨提示：您购买的\n药品需要常温储存(10℃-30℃)\n合计：\n370.00\n实收：\n370.00\n开票员：王影\n营业员：7139\n药品售出无质量问题不退不换！\n电话：0434-3333658",
    "role": "user"
  }
]
2026-08-10 11:17:43,585 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:17:43,585 INFO     29 [qwen-vl-text] LLM output (len=436):
{
  "encounter_date": "2025-09-27",
  "pharmacy": "信康大药房--佳合分店",
  "medications": [
    {
      "name": "沙美特罗替卡松吸入粉雾剂",
      "specification": "50微克/250微克/60泡/盒",
      "dosage": null,
      "quantity": 2,
      "unit_price": 185.00,
      "total_price": 370.00,
      "frequency": null,
      "route": null,
      "manufacturer": "葛兰素史克集团",
      "approval_number": null
    }
  ],
  "payment_total": 370.00,
  "payment_method": null
}
2026-08-10 11:17:43,585 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-09-27]
2026-08-10 11:17:43,592 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3298411, prompt_len=1047
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共37行）
["信康大药房--佳合分店", "单号：250927207100156", "日期：2025-09-27 17:52:20", "会员卡号：13689710485", "姓名：", "积分：37", "总积分：47", "药品名称", "规格", "生产企业/药品上市许可持有人", "产地", "剂型", "批号", "有效期", "数量", "单价", "金额", "12534", "185.00", "沙美特罗替卡松吸入粉雾剂", "50微克/250微克/60泡/盒", "葛兰素史克集团吸入粉雾剂", "JD6K", "2027-06-18", "2盒", "185.00", "370.00", "信康大药房温馨提示：您购买的", "药品需要常温储存(10℃-30℃)", "合计：", "370.00", "实收：", "370.00", "开票员：王影", "营业员：7139", "药品售出无质量问题不退不换！", "电话：0434-3333658"]

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
2026-08-10 11:17:56,986 INFO     29 [qwen-vl-text] coord API raw response (len=1954):
[
	{"text": "信康大药房--佳合分店", "bbox": [216, 190, 685, 219]},
	{"text": "单号：250927207100156", "bbox": [120, 220, 627, 245]},
	{"text": "日期：2025-09-27 17:52:20", "bbox": [122, 246, 728, 272]},
	{"text": "会员卡号：13689710485", "bbox": [122, 274, 598, 299]},
	{"text": "姓名：", "bbox": [122, 301, 225, 326]},
	{"text": "积分：37", "bbox": [122, 329, 291, 352]},
	{"text": "总积分：47", "bbox": [124, 355, 339, 378]},
	{"text": "药品名称", "bbox": [127, 400, 315, 422]},
	{"text": "规格", "bbox": [622, 397, 719, 420]},
	{"text": "生产企业/药品上市许可持有人", "bbox": [127, 428, 757, 453]},
	{"text": "产地", "bbox": [127, 460, 218, 482]},
	{"text": "剂型", "bbox": [267, 460, 359, 482]},
	{"text": "批号", "bbox": [408, 460, 496, 482]},
	{"text": "有效期", "bbox": [575, 460, 720, 482]},
	{"text": "数量", "bbox": [127, 489, 218, 511]},
	{"text": "单价", "bbox": [385, 489, 475, 511]},
	{"text": "金额", "bbox": [600, 489, 693, 511]},
	{"text": "12534", "bbox": [130, 533, 258, 553]},
	{"text": "185.00", "bbox": [313, 533, 468, 553]},
	{"text": "沙美特罗替卡松吸入粉雾剂", "bbox": [127, 559, 764, 584]},
	{"text": "50微克/250微克/60泡/盒", "bbox": [127, 590, 719, 614]},
	{"text": "葛兰素史克集团吸入粉雾剂", "bbox": [130, 620, 802, 645]},
	{"text": "JD6K", "bbox": [127, 656, 225, 674]},
	{"text": "2027-06-18", "bbox": [270, 655, 518, 674]},
	{"text": "2盒", "bbox": [127, 684, 212, 705]},
	{"text": "185.00", "bbox": [288, 684, 432, 704]},
	{"text": "370.00", "bbox": [525, 684, 675, 702]},
	{"text": "信康大药房温馨提示：您购买的", "bbox": [132, 709, 864, 734]},
	{"text": "药品需要常温储存(10℃-30℃)", "bbox": [132, 736, 861, 760]},
	{"text": "合计：", "bbox": [135, 781, 252, 807]},
	{"text": "370.00", "bbox": [568, 781, 722, 803]},
	{"text": "实收：", "bbox": [135, 808, 247, 834]},
	{"text": "370.00", "bbox": [568, 807, 724, 829]},
	{"text": "开票员：王影", "bbox": [135, 832, 447, 860]},
	{"text": "营业员：7139", "bbox": [496, 830, 796, 855]},
	{"text": "药品售出无质量问题不退不换！", "bbox": [135, 853, 810, 883]},
	{"text": "电话：0434-3333658", "bbox": [137, 876, 545, 907]}
]
2026-08-10 11:17:56,987 INFO     29 [qwen-vl-text] coord API: raw_items=37, valid_items=37, elapsed=13.4s
2026-08-10 11:17:56,987 INFO     29 [qwen-vl-text] coord item[0]: text=信康大药房--佳合分店, bbox=[216, 190, 685, 219]
2026-08-10 11:17:56,987 INFO     29 [qwen-vl-text] coord item[1]: text=单号：250927207100156, bbox=[120, 220, 627, 245]
2026-08-10 11:17:56,987 INFO     29 [qwen-vl-text] coord item[2]: text=日期：2025-09-27 17:52:20, bbox=[122, 246, 728, 272]
2026-08-10 11:17:56,987 INFO     29 [qwen-vl-text] coord item[3]: text=会员卡号：13689710485, bbox=[122, 274, 598, 299]
2026-08-10 11:17:56,987 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[122, 301, 225, 326]
2026-08-10 11:17:56,987 INFO     29 [qwen-vl-text] coord item[5]: text=积分：37, bbox=[122, 329, 291, 352]
2026-08-10 11:17:56,987 INFO     29 [qwen-vl-text] coord item[6]: text=总积分：47, bbox=[124, 355, 339, 378]
2026-08-10 11:17:56,987 INFO     29 [qwen-vl-text] coord item[7]: text=药品名称, bbox=[127, 400, 315, 422]
2026-08-10 11:17:56,987 INFO     29 [qwen-vl-text] coord item[8]: text=规格, bbox=[622, 397, 719, 420]
2026-08-10 11:17:56,987 INFO     29 [qwen-vl-text] coord item[9]: text=生产企业/药品上市许可持有人, bbox=[127, 428, 757, 453]
2026-08-10 11:17:56,987 INFO     29 [qwen-vl-text] coord item[10]: text=产地, bbox=[127, 460, 218, 482]
2026-08-10 11:17:56,987 INFO     29 [qwen-vl-text] coord item[11]: text=剂型, bbox=[267, 460, 359, 482]
2026-08-10 11:17:56,988 INFO     29 [qwen-vl-text] coord item[12]: text=批号, bbox=[408, 460, 496, 482]
2026-08-10 11:17:56,988 INFO     29 [qwen-vl-text] coord item[13]: text=有效期, bbox=[575, 460, 720, 482]
2026-08-10 11:17:56,988 INFO     29 [qwen-vl-text] coord item[14]: text=数量, bbox=[127, 489, 218, 511]
2026-08-10 11:17:56,988 INFO     29 [qwen-vl-text] coord item[15]: text=单价, bbox=[385, 489, 475, 511]
2026-08-10 11:17:56,988 INFO     29 [qwen-vl-text] coord item[16]: text=金额, bbox=[600, 489, 693, 511]
2026-08-10 11:17:56,988 INFO     29 [qwen-vl-text] coord item[17]: text=12534, bbox=[130, 533, 258, 553]
2026-08-10 11:17:56,988 INFO     29 [qwen-vl-text] coord item[18]: text=185.00, bbox=[313, 533, 468, 553]
2026-08-10 11:17:56,988 INFO     29 [qwen-vl-text] coord item[19]: text=沙美特罗替卡松吸入粉雾剂, bbox=[127, 559, 764, 584]
2026-08-10 11:17:56,988 INFO     29 [qwen-vl-text] coord item[20]: text=50微克/250微克/60泡/盒, bbox=[127, 590, 719, 614]
2026-08-10 11:17:56,988 INFO     29 [qwen-vl-text] coord item[21]: text=葛兰素史克集团吸入粉雾剂, bbox=[130, 620, 802, 645]
2026-08-10 11:17:56,988 INFO     29 [qwen-vl-text] coord item[22]: text=JD6K, bbox=[127, 656, 225, 674]
2026-08-10 11:17:56,988 INFO     29 [qwen-vl-text] coord item[23]: text=2027-06-18, bbox=[270, 655, 518, 674]
2026-08-10 11:17:56,988 INFO     29 [qwen-vl-text] coord item[24]: text=2盒, bbox=[127, 684, 212, 705]
2026-08-10 11:17:56,988 INFO     29 [qwen-vl-text] coord item[25]: text=185.00, bbox=[288, 684, 432, 704]
2026-08-10 11:17:56,988 INFO     29 [qwen-vl-text] coord item[26]: text=370.00, bbox=[525, 684, 675, 702]
2026-08-10 11:17:56,988 INFO     29 [qwen-vl-text] coord item[27]: text=信康大药房温馨提示：您购买的, bbox=[132, 709, 864, 734]
2026-08-10 11:17:56,988 INFO     29 [qwen-vl-text] coord item[28]: text=药品需要常温储存(10℃-30℃), bbox=[132, 736, 861, 760]
2026-08-10 11:17:56,988 INFO     29 [qwen-vl-text] coord item[29]: text=合计：, bbox=[135, 781, 252, 807]
2026-08-10 11:17:56,988 INFO     29 [qwen-vl-text] coord item[30]: text=370.00, bbox=[568, 781, 722, 803]
2026-08-10 11:17:56,988 INFO     29 [qwen-vl-text] coord item[31]: text=实收：, bbox=[135, 808, 247, 834]
2026-08-10 11:17:56,989 INFO     29 [qwen-vl-text] coord item[32]: text=370.00, bbox=[568, 807, 724, 829]
2026-08-10 11:17:56,989 INFO     29 [qwen-vl-text] coord item[33]: text=开票员：王影, bbox=[135, 832, 447, 860]
2026-08-10 11:17:56,989 INFO     29 [qwen-vl-text] coord item[34]: text=营业员：7139, bbox=[496, 830, 796, 855]
2026-08-10 11:17:56,989 INFO     29 [qwen-vl-text] coord item[35]: text=药品售出无质量问题不退不换！, bbox=[135, 853, 810, 883]
2026-08-10 11:17:56,989 INFO     29 [qwen-vl-text] coord item[36]: text=电话：0434-3333658, bbox=[137, 876, 545, 907]
2026-08-10 11:17:56,990 INFO     29 [qwen-vl-text] page=5 — 37/37 coords, api_time=13.4s
2026-08-10 11:17:56,990 INFO     29 [qwen-vl-text] new_positions (37):
[[5, 128.580486328125, 407.7668200683593, 283.46290649414067, 326.72829748535156], [5, 71.433603515625, 373.2405783691406, 328.22020751953124, 365.51795837402346], [5, 72.62416357421874, 433.363861328125, 367.00986840820315, 405.79952929687505], [5, 72.62416357421874, 355.97745751953124, 408.7833493652344, 446.0811002197266], [5, 72.62416357421874, 133.93800659179686, 449.06492028808594, 486.36267114257817], [5, 72.62416357421874, 173.2264885253906, 490.8384012451172, 525.15233203125], [5, 73.8147236328125, 201.7999299316406, 529.6280621337891, 563.9419929199219], [5, 75.60056372070312, 187.51320922851562, 596.7640136718751, 629.5860344238282], [5, 370.2641782226562, 428.00634106445307, 592.2882835693359, 626.6022143554688], [5, 75.60056372070312, 450.62698217773436, 638.5374946289063, 675.8352454833985], [5, 75.60056372070312, 129.77104638671875, 686.2786157226562, 719.1006364746095], [5, 158.93976782226562, 213.7055305175781, 686.2786157226562, 719.1006364746095], [5, 242.874251953125, 295.25889453125, 686.2786157226562, 719.1006364746095], [5, 342.2860168457031, 428.60162109374994, 686.2786157226562, 719.1006364746095], [5, 75.60056372070312, 129.77104638671875, 729.5440067138672, 762.3660274658204], [5, 229.18281127929686, 282.7580139160156, 729.5440067138672, 762.3660274658204], [5, 357.168017578125, 412.52906030273436, 729.5440067138672, 762.3660274658204], [5, 77.38640380859374, 153.58224755859374, 795.1880482177735, 825.0262489013672], [5, 186.32264916992187, 278.5910537109375, 795.1880482177735, 825.0262489013672], [5, 75.60056372070312, 454.7939423828125, 833.9777091064453, 871.2754599609376], [5, 75.60056372070312, 428.00634106445307, 880.2269201660157, 916.0327609863282], [5, 77.38640380859374, 477.4145834960937, 924.9842211914063, 962.2819720458984], [5, 75.60056372070312, 133.93800659179686, 978.6929824218751, 1005.5473630371094], [5, 160.72560791015624, 308.3550551757812, 977.2010723876954, 1005.5473630371094], [5, 75.60056372070312, 126.19936621093748, 1020.4664633789063, 1051.7965740966797], [5, 171.4406484375, 257.16097265625, 1020.4664633789063, 1050.3046640625], [5, 312.52201538085933, 401.8140197753906, 1020.4664633789063, 1047.3208439941407], [5, 78.57696386718749, 514.3219453125, 1057.7642142333984, 1095.0619650878907], [5, 78.57696386718749, 512.5361052246093, 1098.04578515625, 1133.8516259765627], [5, 80.36280395507812, 150.0105673828125, 1165.181736694336, 1203.971397583008], [5, 338.119056640625, 429.79218115234374, 1165.181736694336, 1198.0037574462892], [5, 80.36280395507812, 147.0341672363281, 1205.4633076171876, 1244.2529685058594], [5, 338.119056640625, 430.9827412109375, 1203.971397583008, 1236.793418334961], [5, 80.36280395507812, 266.0901730957031, 1241.2691484375, 1283.0426293945313], [5, 295.25889453125, 473.8429033203125, 1238.2853283691406, 1275.583079223633], [5, 80.36280395507812, 482.1768237304687, 1272.5992591552736, 1317.3565601806642], [5, 81.55336401367187, 324.42761596679685, 1306.9131899414062, 1353.1624010009766]]
2026-08-10 11:17:56,990 INFO     29 [qwen-vl-text] ═══ DONE ═══ 37 positions, pages=1, time=16.2s
2026-08-10 11:17:56,991 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:17:56,993 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:17:56,993 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 11:17:56,993 INFO     29 [qwen-vl-text] positions(37): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:17:56,993 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [37]
2026-08-10 11:17:57,468 INFO     29 [qwen-vl-text] page=6, rect=595x1387, img=(1654x3853), dpi=200
2026-08-10 11:17:57,469 INFO     29 [qwen-vl-text] LLM extraction start, text_len=323
2026-08-10 11:17:57,469 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:17:57,469 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 371, \"bbox_end\": 407, \"encounter_dates\": [\"2025-11-28\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "信康大药房--佳合分店\n单号：251128207100163\n日期：2025-11-28 16:38:41\n会员卡号：13689710485\n姓名：\n积分：37\n总积分：84\n药品名称\n规格\n生产企业/药品上市许可持有人\n产地\n剂型\n批号\n有效期\n数量\n单价\n金额\n12534\n185.00\n沙美特罗替卡松吸入粉雾剂\n50微克/250微克/60泡/盒\n葛兰素史克集团吸入粉雾剂\nJD6K\n2027-06-18\n2盒\n185.00\n370.00\n信康大药房温馨提示：您购买的\n药品需要常温储存（10℃-30℃）\n合计：\n370.00\n实收：\n370.00\n开票员：张欣\n营业员：7140\n药品售出无质量问题不退不换！\n电话：0434-3333658",
    "role": "user"
  }
]
2026-08-10 11:17:59,708 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:17:59,708 INFO     29 [qwen-vl-text] LLM output (len=436):
{
  "encounter_date": "2025-11-28",
  "pharmacy": "信康大药房--佳合分店",
  "medications": [
    {
      "name": "沙美特罗替卡松吸入粉雾剂",
      "specification": "50微克/250微克/60泡/盒",
      "dosage": null,
      "quantity": 2,
      "unit_price": 185.00,
      "total_price": 370.00,
      "frequency": null,
      "route": null,
      "manufacturer": "葛兰素史克集团",
      "approval_number": null
    }
  ],
  "payment_total": 370.00,
  "payment_method": null
}
2026-08-10 11:17:59,708 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-28]
2026-08-10 11:17:59,713 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3086331, prompt_len=1047
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共37行）
["信康大药房--佳合分店", "单号：251128207100163", "日期：2025-11-28 16:38:41", "会员卡号：13689710485", "姓名：", "积分：37", "总积分：84", "药品名称", "规格", "生产企业/药品上市许可持有人", "产地", "剂型", "批号", "有效期", "数量", "单价", "金额", "12534", "185.00", "沙美特罗替卡松吸入粉雾剂", "50微克/250微克/60泡/盒", "葛兰素史克集团吸入粉雾剂", "JD6K", "2027-06-18", "2盒", "185.00", "370.00", "信康大药房温馨提示：您购买的", "药品需要常温储存（10℃-30℃）", "合计：", "370.00", "实收：", "370.00", "开票员：张欣", "营业员：7140", "药品售出无质量问题不退不换！", "电话：0434-3333658"]

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
2026-08-10 11:18:12,517 INFO     29 [qwen-vl-text] coord API raw response (len=1953):
[
	{"text": "信康大药房--佳合分店", "bbox": [252, 174, 692, 201]},
	{"text": "单号：251128207100163", "bbox": [159, 203, 638, 227]},
	{"text": "日期：2025-11-28 16:38:41", "bbox": [161, 230, 725, 254]},
	{"text": "会员卡号：13689710485", "bbox": [161, 257, 612, 279],
	{"text": "姓名：", "bbox": [161, 283, 252, 307]},
	{"text": "积分：37", "bbox": [161, 311, 319, 334]},
	{"text": "总积分：84", "bbox": [161, 338, 364, 360]},
	{"text": "药品名称", "bbox": [161, 382, 339, 405]},
	{"text": "规格", "bbox": [638, 380, 725, 403]},
	{"text": "生产企业/药品上市许可持有人", "bbox": [161, 411, 764, 435]},
	{"text": "产地", "bbox": [161, 444, 248, 466]},
	{"text": "剂型", "bbox": [296, 444, 385, 466]},
	{"text": "批号", "bbox": [432, 444, 519, 466]},
	{"text": "有效期", "bbox": [594, 443, 729, 466]},
	{"text": "数量", "bbox": [161, 474, 248, 496]},
	{"text": "单价", "bbox": [409, 474, 496, 496]},
	{"text": "金额", "bbox": [614, 473, 701, 495]},
	{"text": "12534", "bbox": [165, 518, 288, 537]},
	{"text": "185.00", "bbox": [340, 517, 486, 537]},
	{"text": "沙美特罗替卡松吸入粉雾剂", "bbox": [161, 545, 762, 569]},
	{"text": "50微克/250微克/60泡/盒", "bbox": [161, 575, 714, 598]},
	{"text": "葛兰素史克集团吸入粉雾剂", "bbox": [167, 606, 786, 629]},
	{"text": "JD6K", "bbox": [165, 641, 257, 659]},
	{"text": "2027-06-18", "bbox": [298, 640, 524, 658]},
	{"text": "2盒", "bbox": [165, 670, 244, 690]},
	{"text": "185.00", "bbox": [313, 670, 448, 689]},
	{"text": "370.00", "bbox": [534, 669, 673, 688]},
	{"text": "信康大药房温馨提示：您购买的", "bbox": [167, 696, 845, 719]},
	{"text": "药品需要常温储存（10℃-30℃）", "bbox": [167, 723, 845, 746]},
	{"text": "合计：", "bbox": [171, 770, 280, 793]},
	{"text": "370.00", "bbox": [572, 767, 714, 787]},
	{"text": "实收：", "bbox": [171, 795, 275, 820]},
	{"text": "370.00", "bbox": [572, 791, 714, 812]},
	{"text": "开票员：张欣", "bbox": [171, 817, 458, 845]},
	{"text": "营业员：7140", "bbox": [505, 815, 788, 841]},
	{"text": "药品售出无质量问题不退不换！", "bbox": [171, 840, 800, 867]},
	{"text": "电话：0434-3333658", "bbox": [171, 863, 550, 888]}
]
2026-08-10 11:18:12,517 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord API: raw_items=37, valid_items=37, elapsed=12.8s
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[0]: text=信康大药房--佳合分店, bbox=[252, 174, 692, 201]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[1]: text=单号：251128207100163, bbox=[159, 203, 638, 227]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[2]: text=日期：2025-11-28 16:38:41, bbox=[161, 230, 725, 254]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[3]: text=会员卡号：13689710485, bbox=[161, 257, 612, 279]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[161, 283, 252, 307]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[5]: text=积分：37, bbox=[161, 311, 319, 334]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[6]: text=总积分：84, bbox=[161, 338, 364, 360]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[7]: text=药品名称, bbox=[161, 382, 339, 405]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[8]: text=规格, bbox=[638, 380, 725, 403]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[9]: text=生产企业/药品上市许可持有人, bbox=[161, 411, 764, 435]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[10]: text=产地, bbox=[161, 444, 248, 466]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[11]: text=剂型, bbox=[296, 444, 385, 466]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[12]: text=批号, bbox=[432, 444, 519, 466]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[13]: text=有效期, bbox=[594, 443, 729, 466]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[14]: text=数量, bbox=[161, 474, 248, 496]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[15]: text=单价, bbox=[409, 474, 496, 496]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[16]: text=金额, bbox=[614, 473, 701, 495]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[17]: text=12534, bbox=[165, 518, 288, 537]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[18]: text=185.00, bbox=[340, 517, 486, 537]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[19]: text=沙美特罗替卡松吸入粉雾剂, bbox=[161, 545, 762, 569]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[20]: text=50微克/250微克/60泡/盒, bbox=[161, 575, 714, 598]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[21]: text=葛兰素史克集团吸入粉雾剂, bbox=[167, 606, 786, 629]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[22]: text=JD6K, bbox=[165, 641, 257, 659]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[23]: text=2027-06-18, bbox=[298, 640, 524, 658]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[24]: text=2盒, bbox=[165, 670, 244, 690]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[25]: text=185.00, bbox=[313, 670, 448, 689]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[26]: text=370.00, bbox=[534, 669, 673, 688]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[27]: text=信康大药房温馨提示：您购买的, bbox=[167, 696, 845, 719]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[28]: text=药品需要常温储存（10℃-30℃）, bbox=[167, 723, 845, 746]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[29]: text=合计：, bbox=[171, 770, 280, 793]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[30]: text=370.00, bbox=[572, 767, 714, 787]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[31]: text=实收：, bbox=[171, 795, 275, 820]
2026-08-10 11:18:12,518 INFO     29 [qwen-vl-text] coord item[32]: text=370.00, bbox=[572, 791, 714, 812]
2026-08-10 11:18:12,519 INFO     29 [qwen-vl-text] coord item[33]: text=开票员：张欣, bbox=[171, 817, 458, 845]
2026-08-10 11:18:12,519 INFO     29 [qwen-vl-text] coord item[34]: text=营业员：7140, bbox=[505, 815, 788, 841]
2026-08-10 11:18:12,519 INFO     29 [qwen-vl-text] coord item[35]: text=药品售出无质量问题不退不换！, bbox=[171, 840, 800, 867]
2026-08-10 11:18:12,519 INFO     29 [qwen-vl-text] coord item[36]: text=电话：0434-3333658, bbox=[171, 863, 550, 888]
2026-08-10 11:18:12,519 INFO     29 [qwen-vl-text] page=6 — 37/37 coords, api_time=12.8s
2026-08-10 11:18:12,520 INFO     29 [qwen-vl-text] new_positions (37):
[[6, 150.0105673828125, 411.9337802734375, 241.3049501953125, 278.7488217773437], [6, 94.64952465820312, 379.7886586914062, 281.52244189453126, 314.80588330078126], [6, 95.84008471679687, 431.57802124023436, 318.9663134765625, 352.2497548828125], [6, 95.84008471679687, 364.31137792968747, 356.41018505859375, 386.9200063476562], [6, 95.84008471679687, 150.0105673828125, 392.46724658203124, 425.75068798828124], [6, 95.84008471679687, 189.8943293457031, 431.29792822265625, 463.1945595703125], [6, 95.84008471679687, 216.6819306640625, 468.7417998046875, 499.25162109375], [6, 95.84008471679687, 201.7999299316406, 529.7614423828124, 561.6580737304687], [6, 379.7886586914062, 431.57802124023436, 526.987822265625, 558.8844536132813], [6, 95.84008471679687, 454.7939423828125, 569.9789340820312, 603.2623754882812], [6, 95.84008471679687, 147.629447265625, 615.743666015625, 646.2534873046875], [6, 176.20288867187497, 229.18281127929686, 615.743666015625, 646.2534873046875], [6, 257.16097265625, 308.9503352050781, 615.743666015625, 646.2534873046875], [6, 353.59633740234375, 433.95914135742186, 614.3568559570313, 646.2534873046875], [6, 95.84008471679687, 147.629447265625, 657.3479677734375, 687.8577890624999], [6, 243.46953198242187, 295.25889453125, 657.3479677734375, 687.8577890624999], [6, 365.5019379882812, 417.29130053710935, 655.9611577148437, 686.4709790039062], [6, 98.22120483398437, 171.4406484375, 718.3676103515625, 744.7170014648437], [6, 202.39520996093748, 289.3060942382812, 716.9808002929688, 744.7170014648437], [6, 95.84008471679687, 453.6033823242187, 755.8114819335938, 789.0949233398437], [6, 95.84008471679687, 425.0299409179687, 797.4157836914062, 829.3124150390624], [6, 99.41176489257812, 467.89010302734374, 840.4068955078125, 872.3035268554687], [6, 98.22120483398437, 152.98696752929686, 888.9452475585937, 913.9078286132813], [6, 177.39344873046875, 311.92673535156246, 887.5584375, 912.5210185546874], [6, 98.22120483398437, 145.24832714843748, 929.1627392578125, 956.8989404296875], [6, 186.32264916992187, 266.685453125, 929.1627392578125, 955.5121303710937], [6, 317.87953564453124, 400.62345971679684, 927.7759291992187, 954.1253203125], [6, 99.41176489257812, 503.0116247558593, 965.21980078125, 997.1164321289062], [6, 99.41176489257812, 503.0116247558593, 1002.6636723632812, 1034.5603037109374], [6, 101.79288500976561, 166.678408203125, 1067.8437451171874, 1099.7403764648436], [6, 340.5001767578125, 425.0299409179687, 1063.6833149414063, 1091.4195161132811], [6, 101.79288500976561, 163.7020080566406, 1102.5139965820313, 1137.184248046875], [6, 340.5001767578125, 425.0299409179687, 1096.9667563476562, 1126.089767578125], [6, 101.79288500976561, 272.6382534179687, 1133.0238178710938, 1171.8544995117188], [6, 300.61641479492187, 469.0806630859375, 1130.2501977539061, 1166.3072592773437], [6, 101.79288500976561, 476.22402343749997, 1164.92044921875, 1202.3643208007811], [6, 101.79288500976561, 327.4040161132812, 1196.8170805664063, 1231.48733203125]]
2026-08-10 11:18:12,520 INFO     29 [qwen-vl-text] ═══ DONE ═══ 37 positions, pages=1, time=15.5s
2026-08-10 11:18:12,537 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 11:18:12,537 INFO     29 [Trace] task=e139f7cc | doc=LHYA-哮喘-沈阳医大四.pdf | Extractor:Medication | outputs={"chunks": "2 items, types={'MedicationRecord': 2}", "html": "", "json": "408 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Examination\": 2, \"chunks_Medication\": 2}"}
2026-08-10 11:18:12,537 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 11:18:12,544 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:18:12,544 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:18:12,920 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:18:12.919+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 19, "failed": 0, "current": {"e139f7cc94ac11f1bd9827cf206dfa2d": {"id": "e139f7cc94ac11f1bd9827cf206dfa2d", "doc_id": "e0cfe59494ac11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "type": "pdf", "location": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "size": 4593431, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786360565919, "task_type": "dataflow", "root_trace_id": "a7e430023e6144f7a5a82bee44b10046", "root_traceparent": "00-a7e430023e6144f7a5a82bee44b10046-21836b890cf4bf02-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:18:13,445 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:18:13,452 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 11:18:13,452 INFO     29 [Trace] task=e139f7cc | doc=LHYA-哮喘-沈阳医大四.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "408 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Examination\": 2, \"chunks_Medication\": 2}"}
2026-08-10 11:18:13,452 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 11:18:13,462 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:18:13,462 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:18:13,925 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:18:13,934 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 11:18:13,934 INFO     29 [Trace] task=e139f7cc | doc=LHYA-哮喘-沈阳医大四.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "408 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Examination\": 2, \"chunks_Medication\": 2}"}
2026-08-10 11:18:13,934 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 11:18:13,943 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:18:13,943 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:18:14,593 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:18:14,603 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 11:18:14,603 INFO     29 [Trace] task=e139f7cc | doc=LHYA-哮喘-沈阳医大四.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "408 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Examination\": 2, \"chunks_Medication\": 2}"}
2026-08-10 11:18:14,603 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 11:18:14,612 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:18:14,613 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:18:14,613 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 11:18:14,613 INFO     29 [qwen-vl-text] positions(117): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:18:14,613 INFO     29 [qwen-vl-text] page grouping: [3], lines per page: [117]
2026-08-10 11:18:14,842 INFO     29 [qwen-vl-text] page=3, rect=595x1058, img=(1654x2940), dpi=200
2026-08-10 11:18:14,843 INFO     29 [qwen-vl-text] LLM extraction start, text_len=723
2026-08-10 11:18:14,844 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:18:14,844 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 97, \"bbox_end\": 213, \"encounter_dates\": [\"2023-12-27\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "四平市中心人民医院\n常规通气+舒张试验\n姓名：\n年龄：53岁\n住院号：111630435\n身高：168 cm\n性别：女\n吸烟史：\n测试号：20231227014\n体重：82 kg\nFlow [L/s]\nF/V ex\nVol [L]\nVol%VCmax\nVCmax\nTime [s]\nF/V in\n测试日期\n测试时间\n预计值\n药前\n前/预%\n药后\n后/预% 改善率 (%)\n23/12/27\n23/12/27\n15:36:14\n15:51:45\nMV\n[L/min]\n11.71\n27.39\n233.8\n3.78\n115.4\n7.6\nVC MAX\n[L]\n3.28\n3.52\n107.3\nFVC\n[L]\n3.17\n3.52\n110.8\n3.78\n119.2\n7.6\nFEV 1\n[L]\n2.71\n2.11\n77.7\n2.39\n88.3\n13.7\nFEV 1 % FVC\n[%]\n59.91\n63.29\n5.6\nFEV 1 % VC MAX\n[%]\n79.03\n59.91\n75.8\n63.29\n80.1\n5.6\nPEF\n[L/s]\n6.54\n4.76\n72.7\n4.54\n69.4\n-4.6\nMEF 75\n[L/s]\n5.68\n2.64\n46.4\n3.29\n58.0\n24.9\nMEF 50\n[L/s]\n3.95\n1.40\n35.4\n1.80\n45.5\n28.5\nMEF 25\n[L/s]\n1.55\n0.53\n34.2\n0.65\n42.1\n22.9\nMMEF 75/25\n[L/s]\n3.22\n1.15\n35.8\n1.44\n44.6\n24.5\nMVV\n[L/min]\n100.45\n检查意见：\n结果：支气管舒张实验(+)。\n操作者签字：\n医生签字：",
    "role": "user"
  }
]
2026-08-10 11:18:20,749 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:18:20,750 INFO     29 [qwen-vl-text] LLM output (len=1097):
{
  "exam_date": "2023-12-27",
  "report_date": "2023-12-27",
  "exam_name": "常规通气+舒张试验",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "测试日期: 23/12/27\n测试时间: 15:36:14 (药前), 15:51:45 (药后)\n\n| 指标 | 药前实测值 | 药前/预计% | 药后实测值 | 药后/预计% | 改善率 (%) |\n| :--- | :--- | :--- | :--- | :--- | :--- |\n| MV [L/min] | 11.71 | 27.39 | 233.8 | 3.78 | 115.4 |\n| VC MAX [L] | 3.28 | 3.52 | 107.3 | 7.6 | - |\n| FVC [L] | 3.17 | 3.52 | 110.8 | 3.78 | 119.2 |\n| FEV 1 [L] | 2.71 | 2.11 | 77.7 | 2.39 | 88.3 |\n| FEV 1 % FVC [%] | 59.91 | 63.29 | 5.6 | - | - |\n| FEV 1 % VC MAX [%] | 79.03 | 59.91 | 75.8 | 63.29 | 80.1 |\n| PEF [L/s] | 6.54 | 4.76 | 72.7 | 4.54 | 69.4 |\n| MEF 75 [L/s] | 5.68 | 2.64 | 46.4 | 3.29 | 58.0 |\n| MEF 50 [L/s] | 3.95 | 1.40 | 35.4 | 1.80 | 45.5 |\n| MEF 25 [L/s] | 1.55 | 0.53 | 34.2 | 0.65 | 42.1 |\n| MMEF 75/25 [L/s] | 3.22 | 1.15 | 35.8 | 1.44 | 44.6 |\n| MVV [L/min] | 100.45 | - | - | - | - |",
  "conclusion": "结果：支气管舒张实验(+)。",
  "physician": null,
  "reviewer": null
}
2026-08-10 11:18:20,757 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1505638, prompt_len=1688
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共117行）
["四平市中心人民医院", "常规通气+舒张试验", "姓名：", "年龄：53岁", "住院号：111630435", "身高：168 cm", "性别：女", "吸烟史：", "测试号：20231227014", "体重：82 kg", "Flow [L/s]", "F/V ex", "Vol [L]", "Vol%VCmax", "VCmax", "Time [s]", "F/V in", "测试日期", "测试时间", "预计值", "药前", "前/预%", "药后", "后/预% 改善率 (%)", "23/12/27", "23/12/27", "15:36:14", "15:51:45", "MV", "[L/min]", "11.71", "27.39", "233.8", "3.78", "115.4", "7.6", "VC MAX", "[L]", "3.28", "3.52", "107.3", "FVC", "[L]", "3.17", "3.52", "110.8", "3.78", "119.2", "7.6", "FEV 1", "[L]", "2.71", "2.11", "77.7", "2.39", "88.3", "13.7", "FEV 1 % FVC", "[%]", "59.91", "63.29", "5.6", "FEV 1 % VC MAX", "[%]", "79.03", "59.91", "75.8", "63.29", "80.1", "5.6", "PEF", "[L/s]", "6.54", "4.76", "72.7", "4.54", "69.4", "-4.6", "MEF 75", "[L/s]", "5.68", "2.64", "46.4", "3.29", "58.0", "24.9", "MEF 50", "[L/s]", "3.95", "1.40", "35.4", "1.80", "45.5", "28.5", "MEF 25", "[L/s]", "1.55", "0.53", "34.2", "0.65", "42.1", "22.9", "MMEF 75/25", "[L/s]", "3.22", "1.15", "35.8", "1.44", "44.6", "24.5", "MVV", "[L/min]", "100.45", "检查意见：", "结果：支气管舒张实验(+)。", "操作者签字：", "医生签字："]

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
2026-08-10 11:18:51,400 INFO     29 [qwen-vl-text] coord API raw response (len=5873):
[
	{"text": "四平市中心人民医院", "bbox": [379, 139, 673, 165]},
	{"text": "常规通气+舒张试验", "bbox": [398, 167, 625, 188]},
	{"text": "姓名：", "bbox": [165, 208, 210, 218]},
	{"text": "年龄：53岁", "bbox": [165, 216, 372, 226]},
	{"text": "住院号：111630435", "bbox": [165, 225, 409, 235]},
	{"text": "身高：168 cm", "bbox": [165, 234, 384, 244]},
	{"text": "性别：", "bbox": [495, 200, 540, 210]},
	{"text": "吸烟史：", "bbox": [495, 209, 558, 219]},
	{"text": "测试号：20231227014", "bbox": [657, 211, 757, 221]},
	{"text": "体重：82 kg", "bbox": [657, 221, 705, 231]},
	{"text": "Flow [L/s]", "bbox": [240, 248, 293, 258]},
	{"text": "F/V ex", "bbox": [384, 246, 418, 255]},
	{"text": "Vol [L]", "bbox": [557, 246, 591, 256]},
	{"text": "Vol%VCmax", "bbox": [514, 280, 574, 289]},
	{"text": "VCmax", "bbox": [572, 290, 608, 298]},
	{"text": "Time [s]", "bbox": [653, 317, 695, 326]},
	{"text": "F/V in", "bbox": [392, 333, 424, 342]},
	{"text": "测试日期", "bbox": [133, 364, 208, 374]},
	{"text": "测试时间", "bbox": [133, 373, 208, 383]},
	{"text": "预计值", "bbox": [384, 348, 441, 359]},
	{"text": "药前", "bbox": [483, 346, 520, 357]},
	{"text": "前/预%", "bbox": [547, 344, 602, 355]},
	{"text": "药后", "bbox": [646, 342, 683, 353]},
	{"text": "后/预% 改善率 (%)", "bbox": [709, 337, 867, 350]},
	{"text": "23/12/27", "bbox": [450, 357, 521, 367]},
	{"text": "23/12/27", "bbox": [611, 353, 683, 363]},
	{"text": "15:36:14", "bbox": [450, 366, 521, 376]},
	{"text": "15:51:45", "bbox": [611, 362, 685, 372]},
	{"text": "MV", "bbox": [133, 394, 155, 402]},
	{"text": "[L/min]", "bbox": [310, 389, 370, 399]},
	{"text": "11.71", "bbox": [398, 387, 444, 397]},
	{"text": "27.39", "bbox": [478, 385, 524, 395]},
	{"text": "233.8", "bbox": [558, 383, 605, 393]},
	{"text": "3.78", "bbox": [651, 389, 688, 399]},
	{"text": "115.4", "bbox": [723, 387, 770, 397]},
	{"text": "7.6", "bbox": [851, 384, 881, 393]},
	{"text": "VC MAX", "bbox": [133, 403, 191, 411]},
	{"text": "[L]", "bbox": [347, 399, 370, 408]},
	{"text": "3.28", "bbox": [407, 397, 444, 406]},
	{"text": "3.52", "bbox": [487, 395, 524, 404]},
	{"text": "107.3", "bbox": [558, 393, 605, 402]},
	{"text": "FVC", "bbox": [135, 422, 165, 430]},
	{"text": "[L]", "bbox": [347, 425, 370, 434]},
	{"text": "3.17", "bbox": [407, 415, 444, 424]},
	{"text": "3.52", "bbox": [487, 413, 524, 422]},
	{"text": "110.8", "bbox": [560, 411, 607, 420]},
	{"text": "3.78", "bbox": [651, 409, 690, 418]},
	{"text": "119.2", "bbox": [725, 407, 772, 416]},
	{"text": "7.6", "bbox": [851, 404, 881, 413]},
	{"text": "FEV 1", "bbox": [135, 432, 182, 440]},
	{"text": "[L]", "bbox": [347, 434, 370, 443]},
	{"text": "2.71", "bbox": [407, 425, 444, 434]},
	{"text": "2.11", "bbox": [487, 423, 524, 432]},
	{"text": "77.7", "bbox": [569, 420, 607, 429]},
	{"text": "2.39", "bbox": [651, 418, 690, 427]},
	{"text": "88.3", "bbox": [734, 416, 772, 425]},
	{"text": "13.7", "bbox": [845, 413, 881, 422]},
	{"text": "FEV 1 % FVC", "bbox": [135, 441, 239, 449]},
	{"text": "[%]", "bbox": [347, 437, 370, 446]},
	{"text": "59.91", "bbox": [481, 432, 524, 441]},
	{"text": "63.29", "bbox": [645, 427, 690, 436]},
	{"text": "5.6", "bbox": [855, 422, 881, 431]},
	{"text": "FEV 1 % VC MAX", "bbox": [135, 449, 267, 458]},
	{"text": "[%]", "bbox": [347, 446, 370, 455]},
	{"text": "79.03", "bbox": [401, 444, 447, 453]},
	{"text": "59.91", "bbox": [481, 441, 524, 450]},
	{"text": "75.8", "bbox": [572, 440, 609, 449]},
	{"text": "63.29", "bbox": [645, 436, 690, 445]},
	{"text": "80.1", "bbox": [737, 435, 772, 444]},
	{"text": "5.6", "bbox": [855, 431, 881, 440]},
	{"text": "PEF", "bbox": [135, 460, 167, 468]},
	{"text": "[L/s]", "bbox": [332, 455, 372, 464]},
	{"text": "6.54", "bbox": [411, 453, 447, 462]},
	{"text": "4.76", "bbox": [491, 451, 528, 460]},
	{"text": "72.7", "bbox": [572, 449, 609, 458]},
	{"text": "4.54", "bbox": [655, 445, 690, 454]},
	{"text": "69.4", "bbox": [737, 444, 772, 453]},
	{"text": "-4.6", "bbox": [848, 440, 884, 449]},
	{"text": "MEF 75", "bbox": [135, 469, 194, 477]},
	{"text": "[L/s]", "bbox": [332, 464, 372, 473]},
	{"text": "5.68", "bbox": [411, 462, 447, 471]},
	{"text": "2.64", "bbox": [491, 460, 528, 469]},
	{"text": "46.4", "bbox": [572, 458, 609, 467]},
	{"text": "3.29", "bbox": [655, 454, 690, 463]},
	{"text": "58.0", "bbox": [737, 453, 772, 462]},
	{"text": "24.9", "bbox": [848, 449, 884, 458]},
	{"text": "MEF 50", "bbox": [135, 478, 194, 486]},
	{"text": "[L/s]", "bbox": [332, 473, 372, 482]},
	{"text": "3.95", "bbox": [411, 471, 447, 480]},
	{"text": "1.40", "bbox": [491, 470, 528, 479]},
	{"text": "35.4", "bbox": [572, 467, 609, 476]},
	{"text": "1.80", "bbox": [655, 464, 690, 473]},
	{"text": "45.5", "bbox": [737, 463, 772, 472]},
	{"text": "28.5", "bbox": [848, 458, 884, 467]},
	{"text": "MEF 25", "bbox": [135, 487, 194, 495]},
	{"text": "[L/s]", "bbox": [332, 482, 372, 491]},
	{"text": "1.55", "bbox": [411, 480, 447, 489]},
	{"text": "0.53", "bbox": [491, 479, 528, 488]},
	{"text": "34.2", "bbox": [572, 476, 609, 485]},
	{"text": "0.65", "bbox": [655, 473, 690, 482]},
	{"text": "42.1", "bbox": [737, 472, 772, 481]},
	{"text": "22.9", "bbox": [848, 467, 884, 476]},
	{"text": "MMEF 75/25", "bbox": [135, 496, 232, 505]},
	{"text": "[L/s]", "bbox": [332, 491, 372, 500]},
	{"text": "3.22", "bbox": [411, 490, 447, 499]},
	{"text": "1.15", "bbox": [491, 489, 528, 498]},
	{"text": "35.8", "bbox": [572, 485, 609, 494]},
	{"text": "1.44", "bbox": [655, 483, 690, 492]},
	{"text": "44.6", "bbox": [737, 481, 772, 490]},
	{"text": "24.5", "bbox": [851, 476, 888, 485]},
	{"text": "MVV", "bbox": [138, 516, 170, 524]},
	{"text": "[L/min]", "bbox": [317, 511, 376, 520]},
	{"text": "100.45", "bbox": [398, 509, 452, 518]},
	{"text": "检查意见：", "bbox": [100, 524, 197, 538]},
	{"text": "结果：支气管舒张实验(+)。", "bbox": [125, 550, 347, 566]},
	{"text": "操作者签字：", "bbox": [772, 550, 872, 564]},
	{"text": "医生签字：", "bbox": [774, 569, 857, 584]}
]
2026-08-10 11:18:51,401 INFO     29 [qwen-vl-text] coord API: raw_items=117, valid_items=117, elapsed=30.6s
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[0]: text=四平市中心人民医院, bbox=[379, 139, 673, 165]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[1]: text=常规通气+舒张试验, bbox=[398, 167, 625, 188]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[165, 208, 210, 218]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：53岁, bbox=[165, 216, 372, 226]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[4]: text=住院号：111630435, bbox=[165, 225, 409, 235]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[5]: text=身高：168 cm, bbox=[165, 234, 384, 244]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[6]: text=性别：, bbox=[495, 200, 540, 210]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[7]: text=吸烟史：, bbox=[495, 209, 558, 219]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[8]: text=测试号：20231227014, bbox=[657, 211, 757, 221]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[9]: text=体重：82 kg, bbox=[657, 221, 705, 231]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[10]: text=Flow [L/s], bbox=[240, 248, 293, 258]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[11]: text=F/V ex, bbox=[384, 246, 418, 255]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[12]: text=Vol [L], bbox=[557, 246, 591, 256]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[13]: text=Vol%VCmax, bbox=[514, 280, 574, 289]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[14]: text=VCmax, bbox=[572, 290, 608, 298]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[15]: text=Time [s], bbox=[653, 317, 695, 326]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[16]: text=F/V in, bbox=[392, 333, 424, 342]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[17]: text=测试日期, bbox=[133, 364, 208, 374]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[18]: text=测试时间, bbox=[133, 373, 208, 383]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[19]: text=预计值, bbox=[384, 348, 441, 359]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[20]: text=药前, bbox=[483, 346, 520, 357]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[21]: text=前/预%, bbox=[547, 344, 602, 355]
2026-08-10 11:18:51,402 INFO     29 [qwen-vl-text] coord item[22]: text=药后, bbox=[646, 342, 683, 353]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[23]: text=后/预% 改善率 (%), bbox=[709, 337, 867, 350]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[24]: text=23/12/27, bbox=[450, 357, 521, 367]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[25]: text=23/12/27, bbox=[611, 353, 683, 363]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[26]: text=15:36:14, bbox=[450, 366, 521, 376]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[27]: text=15:51:45, bbox=[611, 362, 685, 372]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[28]: text=MV, bbox=[133, 394, 155, 402]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[29]: text=[L/min], bbox=[310, 389, 370, 399]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[30]: text=11.71, bbox=[398, 387, 444, 397]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[31]: text=27.39, bbox=[478, 385, 524, 395]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[32]: text=233.8, bbox=[558, 383, 605, 393]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[33]: text=3.78, bbox=[651, 389, 688, 399]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[34]: text=115.4, bbox=[723, 387, 770, 397]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[35]: text=7.6, bbox=[851, 384, 881, 393]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[36]: text=VC MAX, bbox=[133, 403, 191, 411]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[37]: text=[L], bbox=[347, 399, 370, 408]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[38]: text=3.28, bbox=[407, 397, 444, 406]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[39]: text=3.52, bbox=[487, 395, 524, 404]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[40]: text=107.3, bbox=[558, 393, 605, 402]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[41]: text=FVC, bbox=[135, 422, 165, 430]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[42]: text=[L], bbox=[347, 425, 370, 434]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[43]: text=3.17, bbox=[407, 415, 444, 424]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[44]: text=3.52, bbox=[487, 413, 524, 422]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[45]: text=110.8, bbox=[560, 411, 607, 420]
2026-08-10 11:18:51,403 INFO     29 [qwen-vl-text] coord item[46]: text=3.78, bbox=[651, 409, 690, 418]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[47]: text=119.2, bbox=[725, 407, 772, 416]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[48]: text=7.6, bbox=[851, 404, 881, 413]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[49]: text=FEV 1, bbox=[135, 432, 182, 440]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[50]: text=[L], bbox=[347, 434, 370, 443]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[51]: text=2.71, bbox=[407, 425, 444, 434]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[52]: text=2.11, bbox=[487, 423, 524, 432]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[53]: text=77.7, bbox=[569, 420, 607, 429]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[54]: text=2.39, bbox=[651, 418, 690, 427]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[55]: text=88.3, bbox=[734, 416, 772, 425]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[56]: text=13.7, bbox=[845, 413, 881, 422]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[57]: text=FEV 1 % FVC, bbox=[135, 441, 239, 449]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[58]: text=[%], bbox=[347, 437, 370, 446]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[59]: text=59.91, bbox=[481, 432, 524, 441]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[60]: text=63.29, bbox=[645, 427, 690, 436]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[61]: text=5.6, bbox=[855, 422, 881, 431]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[62]: text=FEV 1 % VC MAX, bbox=[135, 449, 267, 458]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[63]: text=[%], bbox=[347, 446, 370, 455]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[64]: text=79.03, bbox=[401, 444, 447, 453]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[65]: text=59.91, bbox=[481, 441, 524, 450]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[66]: text=75.8, bbox=[572, 440, 609, 449]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[67]: text=63.29, bbox=[645, 436, 690, 445]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[68]: text=80.1, bbox=[737, 435, 772, 444]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[69]: text=5.6, bbox=[855, 431, 881, 440]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[70]: text=PEF, bbox=[135, 460, 167, 468]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[71]: text=[L/s], bbox=[332, 455, 372, 464]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[72]: text=6.54, bbox=[411, 453, 447, 462]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[73]: text=4.76, bbox=[491, 451, 528, 460]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[74]: text=72.7, bbox=[572, 449, 609, 458]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[75]: text=4.54, bbox=[655, 445, 690, 454]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[76]: text=69.4, bbox=[737, 444, 772, 453]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[77]: text=-4.6, bbox=[848, 440, 884, 449]
2026-08-10 11:18:51,404 INFO     29 [qwen-vl-text] coord item[78]: text=MEF 75, bbox=[135, 469, 194, 477]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[79]: text=[L/s], bbox=[332, 464, 372, 473]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[80]: text=5.68, bbox=[411, 462, 447, 471]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[81]: text=2.64, bbox=[491, 460, 528, 469]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[82]: text=46.4, bbox=[572, 458, 609, 467]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[83]: text=3.29, bbox=[655, 454, 690, 463]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[84]: text=58.0, bbox=[737, 453, 772, 462]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[85]: text=24.9, bbox=[848, 449, 884, 458]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[86]: text=MEF 50, bbox=[135, 478, 194, 486]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[87]: text=[L/s], bbox=[332, 473, 372, 482]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[88]: text=3.95, bbox=[411, 471, 447, 480]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[89]: text=1.40, bbox=[491, 470, 528, 479]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[90]: text=35.4, bbox=[572, 467, 609, 476]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[91]: text=1.80, bbox=[655, 464, 690, 473]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[92]: text=45.5, bbox=[737, 463, 772, 472]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[93]: text=28.5, bbox=[848, 458, 884, 467]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[94]: text=MEF 25, bbox=[135, 487, 194, 495]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[95]: text=[L/s], bbox=[332, 482, 372, 491]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[96]: text=1.55, bbox=[411, 480, 447, 489]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[97]: text=0.53, bbox=[491, 479, 528, 488]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[98]: text=34.2, bbox=[572, 476, 609, 485]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[99]: text=0.65, bbox=[655, 473, 690, 482]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[100]: text=42.1, bbox=[737, 472, 772, 481]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[101]: text=22.9, bbox=[848, 467, 884, 476]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[102]: text=MMEF 75/25, bbox=[135, 496, 232, 505]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[103]: text=[L/s], bbox=[332, 491, 372, 500]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[104]: text=3.22, bbox=[411, 490, 447, 499]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[105]: text=1.15, bbox=[491, 489, 528, 498]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[106]: text=35.8, bbox=[572, 485, 609, 494]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[107]: text=1.44, bbox=[655, 483, 690, 492]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[108]: text=44.6, bbox=[737, 481, 772, 490]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[109]: text=24.5, bbox=[851, 476, 888, 485]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[110]: text=MVV, bbox=[138, 516, 170, 524]
2026-08-10 11:18:51,405 INFO     29 [qwen-vl-text] coord item[111]: text=[L/min], bbox=[317, 511, 376, 520]
2026-08-10 11:18:51,406 INFO     29 [qwen-vl-text] coord item[112]: text=100.45, bbox=[398, 509, 452, 518]
2026-08-10 11:18:51,406 INFO     29 [qwen-vl-text] coord item[113]: text=检查意见：, bbox=[100, 524, 197, 538]
2026-08-10 11:18:51,406 INFO     29 [qwen-vl-text] coord item[114]: text=结果：支气管舒张实验(+)。, bbox=[125, 550, 347, 566]
2026-08-10 11:18:51,406 INFO     29 [qwen-vl-text] coord item[115]: text=操作者签字：, bbox=[772, 550, 872, 564]
2026-08-10 11:18:51,406 INFO     29 [qwen-vl-text] coord item[116]: text=医生签字：, bbox=[774, 569, 857, 584]
2026-08-10 11:18:51,406 INFO     29 [qwen-vl-text] page=3 — 117/117 coords, api_time=30.6s
2026-08-10 11:18:51,406 INFO     29 [qwen-vl-text] new_positions (117):
[[3, 225.61113110351562, 400.62345971679684, 147.09953271484375, 174.61455322265624], [3, 236.92145166015624, 372.0500183105469, 176.73109326171874, 198.95476367187499], [3, 98.22120483398437, 125.00880615234374, 220.1201640625, 230.7028642578125], [3, 98.22120483398437, 221.44417089843748, 228.58632421875, 239.1690244140625], [3, 98.22120483398437, 243.46953198242187, 238.11075439453126, 248.69345458984375], [3, 98.22120483398437, 228.58753124999998, 247.6351845703125, 258.217884765625], [3, 294.6636145019531, 321.4512158203125, 211.65400390625, 222.2367041015625], [3, 294.6636145019531, 332.1662563476562, 221.17843408203126, 231.76113427734376], [3, 391.0989792480469, 450.62698217773436, 223.29497412109376, 233.87767431640626], [3, 391.0989792480469, 419.67242065429684, 233.87767431640626, 244.46037451171875], [3, 142.86720703125, 174.41704858398435, 262.45096484375, 273.0336650390625], [3, 228.58753124999998, 248.82705224609373, 260.3344248046875, 269.8588549804687], [3, 331.5709763183593, 351.8104973144531, 260.3344248046875, 270.917125], [3, 305.9739350585937, 341.69073681640623, 296.31560546875, 305.84003564453127], [3, 340.5001767578125, 361.9302578125, 306.8983056640625, 315.3644658203125], [3, 388.7178591308593, 413.7196203613281, 335.47159619140626, 344.9960263671875], [3, 233.34977148437497, 252.39873242187497, 352.40391650390626, 361.9283466796875], [3, 79.17224389648437, 123.81824609374999, 385.210287109375, 395.7929873046875], [3, 79.17224389648437, 123.81824609374999, 394.73471728515625, 405.31741748046875], [3, 228.58753124999998, 262.51849291992187, 368.277966796875, 379.91893701171875], [3, 287.5202541503906, 309.54561523437496, 366.1614267578125, 377.80239697265625], [3, 325.6181760253906, 358.35857763671873, 364.04488671875, 375.68585693359375], [3, 384.5508989257812, 406.5762600097656, 361.9283466796875, 373.56931689453126], [3, 422.05354077148434, 516.1077854003906, 356.63699658203126, 370.3945068359375], [3, 267.8760131835937, 310.14089526367184, 377.80239697265625, 388.38509716796875], [3, 363.7160979003906, 406.5762600097656, 373.56931689453126, 384.15201708984375], [3, 267.8760131835937, 310.14089526367184, 387.3268271484375, 397.90952734374997], [3, 363.7160979003906, 407.7668200683593, 383.0937470703125, 393.676447265625], [3, 79.17224389648437, 92.26840454101561, 416.9583876953125, 425.4245478515625], [3, 184.53680908203123, 220.25361083984373, 411.66703759765625, 422.24973779296874], [3, 236.92145166015624, 264.3043330078125, 409.55049755859375, 420.13319775390624], [3, 284.54385400390623, 311.92673535156246, 407.43395751953125, 418.01665771484375], [3, 332.1662563476562, 360.14441772460935, 405.31741748046875, 415.90011767578125], [3, 387.5272990722656, 409.55266015625, 411.66703759765625, 422.24973779296874], [3, 430.3874611816406, 458.3656225585937, 409.55049755859375, 420.13319775390624], [3, 506.5833049316406, 524.4417058105469, 406.3756875, 415.90011767578125], [3, 79.17224389648437, 113.69848559570312, 426.48281787109374, 434.94897802734374], [3, 206.56217016601562, 220.25361083984373, 422.24973779296874, 431.77416796875], [3, 242.2789719238281, 264.3043330078125, 420.13319775390624, 429.6576279296875], [3, 289.9013742675781, 311.92673535156246, 418.01665771484375, 427.541087890625], [3, 332.1662563476562, 360.14441772460935, 415.90011767578125, 425.4245478515625], [3, 80.36280395507812, 98.22120483398437, 446.5899482421875, 455.0561083984375], [3, 206.56217016601562, 220.25361083984373, 449.76475830078124, 459.2891884765625], [3, 242.2789719238281, 264.3043330078125, 439.18205810546874, 448.70648828125], [3, 289.9013742675781, 311.92673535156246, 437.06551806640624, 446.5899482421875], [3, 333.35681640625, 361.3349777832031, 434.94897802734374, 444.473408203125], [3, 387.5272990722656, 410.74322021484375, 432.83243798828124, 442.3568681640625], [3, 431.57802124023436, 459.55618261718746, 430.71589794921874, 440.240328125], [3, 506.5833049316406, 524.4417058105469, 427.541087890625, 437.06551806640624], [3, 80.36280395507812, 108.34096533203125, 457.1726484375, 465.63880859375], [3, 206.56217016601562, 220.25361083984373, 459.2891884765625, 468.81361865234373], [3, 242.2789719238281, 264.3043330078125, 449.76475830078124, 459.2891884765625], [3, 289.9013742675781, 311.92673535156246, 447.64821826171874, 457.1726484375], [3, 338.71433666992186, 361.3349777832031, 444.473408203125, 453.99783837890624], [3, 387.5272990722656, 410.74322021484375, 442.3568681640625, 451.88129833984374], [3, 436.9355415039062, 459.55618261718746, 440.240328125, 449.76475830078124], [3, 503.0116247558593, 524.4417058105469, 437.06551806640624, 446.5899482421875], [3, 80.36280395507812, 142.27192700195312, 466.69707861328123, 475.16323876953123], [3, 206.56217016601562, 220.25361083984373, 462.46399853515624, 471.9884287109375], [3, 286.32969409179685, 311.92673535156246, 457.1726484375, 466.69707861328123], [3, 383.95561889648434, 410.74322021484375, 451.88129833984374, 461.405728515625], [3, 508.9644250488281, 524.4417058105469, 446.5899482421875, 456.11437841796874], [3, 80.36280395507812, 158.93976782226562, 475.16323876953123, 484.6876689453125], [3, 206.56217016601562, 220.25361083984373, 471.9884287109375, 481.51285888671873], [3, 238.70729174804686, 266.0901730957031, 469.871888671875, 479.39631884765623], [3, 286.32969409179685, 311.92673535156246, 466.69707861328123, 476.2215087890625], [3, 340.5001767578125, 362.52553784179685, 465.63880859375, 475.16323876953123], [3, 383.95561889648434, 410.74322021484375, 461.405728515625, 470.93015869140623], [3, 438.72138159179684, 459.55618261718746, 460.34745849609374, 469.871888671875], [3, 508.9644250488281, 524.4417058105469, 456.11437841796874, 465.63880859375], [3, 80.36280395507812, 99.41176489257812, 486.804208984375, 495.270369140625], [3, 197.6329697265625, 221.44417089843748, 481.51285888671873, 491.0372890625], [3, 244.66009204101562, 266.0901730957031, 479.39631884765623, 488.9207490234375], [3, 292.2824943847656, 314.30785546874995, 477.27977880859373, 486.804208984375], [3, 340.5001767578125, 362.52553784179685, 475.16323876953123, 484.6876689453125], [3, 389.90841918945307, 410.74322021484375, 470.93015869140623, 480.4545888671875], [3, 438.72138159179684, 459.55618261718746, 469.871888671875, 479.39631884765623], [3, 504.79746484374994, 526.2275458984375, 465.63880859375, 475.16323876953123], [3, 80.36280395507812, 115.48432568359374, 496.32863916015623, 504.7947993164062], [3, 197.6329697265625, 221.44417089843748, 491.0372890625, 500.5617192382812], [3, 244.66009204101562, 266.0901730957031, 488.9207490234375, 498.4451791992187], [3, 292.2824943847656, 314.30785546874995, 486.804208984375, 496.32863916015623], [3, 340.5001767578125, 362.52553784179685, 484.6876689453125, 494.21209912109373], [3, 389.90841918945307, 410.74322021484375, 480.4545888671875, 489.97901904296873], [3, 438.72138159179684, 459.55618261718746, 479.39631884765623, 488.9207490234375], [3, 504.79746484374994, 526.2275458984375, 475.16323876953123, 484.6876689453125], [3, 80.36280395507812, 115.48432568359374, 505.8530693359375, 514.3192294921874], [3, 197.6329697265625, 221.44417089843748, 500.5617192382812, 510.0861494140625], [3, 244.66009204101562, 266.0901730957031, 498.4451791992187, 507.969609375], [3, 292.2824943847656, 314.30785546874995, 497.3869091796875, 506.9113393554687], [3, 340.5001767578125, 362.52553784179685, 494.21209912109373, 503.736529296875], [3, 389.90841918945307, 410.74322021484375, 491.0372890625, 500.5617192382812], [3, 438.72138159179684, 459.55618261718746, 489.97901904296873, 499.50344921875], [3, 504.79746484374994, 526.2275458984375, 484.6876689453125, 494.21209912109373], [3, 80.36280395507812, 115.48432568359374, 515.3774995117187, 523.8436596679687], [3, 197.6329697265625, 221.44417089843748, 510.0861494140625, 519.6105795898437], [3, 244.66009204101562, 266.0901730957031, 507.969609375, 517.4940395507813], [3, 292.2824943847656, 314.30785546874995, 506.9113393554687, 516.43576953125], [3, 340.5001767578125, 362.52553784179685, 503.736529296875, 513.2609594726563], [3, 389.90841918945307, 410.74322021484375, 500.5617192382812, 510.0861494140625], [3, 438.72138159179684, 459.55618261718746, 499.50344921875, 509.0278793945312], [3, 504.79746484374994, 526.2275458984375, 494.21209912109373, 503.736529296875], [3, 80.36280395507812, 138.10496679687498, 524.9019296875, 534.4263598632813], [3, 197.6329697265625, 221.44417089843748, 519.6105795898437, 529.135009765625], [3, 244.66009204101562, 266.0901730957031, 518.5523095703124, 528.0767397460937], [3, 292.2824943847656, 314.30785546874995, 517.4940395507813, 527.0184697265624], [3, 340.5001767578125, 362.52553784179685, 513.2609594726563, 522.7853896484374], [3, 389.90841918945307, 410.74322021484375, 511.1444194335937, 520.668849609375], [3, 438.72138159179684, 459.55618261718746, 509.0278793945312, 518.5523095703124], [3, 506.5833049316406, 528.608666015625, 503.736529296875, 513.2609594726563], [3, 82.14864404296874, 101.19760498046874, 546.067330078125, 554.533490234375], [3, 188.70376928710937, 223.825291015625, 540.7759799804687, 550.30041015625], [3, 236.92145166015624, 269.0665732421875, 538.6594399414063, 548.1838701171876], [3, 59.528002929687496, 117.27016577148437, 554.533490234375, 569.3492705078125], [3, 74.41000366210938, 206.56217016601562, 582.0485107421875, 598.9808310546875], [3, 459.55618261718746, 519.084185546875, 582.0485107421875, 596.864291015625], [3, 460.7467426757812, 510.15498510742185, 602.1556411132813, 618.02969140625]]
2026-08-10 11:18:51,406 INFO     29 [qwen-vl-text] ═══ DONE ═══ 117 positions, pages=1, time=36.8s
2026-08-10 11:18:51,406 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:18:51,415 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:18:51,415 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 11:18:51,415 INFO     29 [qwen-vl-text] positions(120): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:18:51,415 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [120]
2026-08-10 11:18:51,620 INFO     29 [qwen-vl-text] page=4, rect=595x1058, img=(1654x2940), dpi=200
2026-08-10 11:18:51,620 INFO     29 [qwen-vl-text] LLM extraction start, text_len=744
2026-08-10 11:18:51,621 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:18:51,621 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 214, \"bbox_end\": 333, \"encounter_dates\": [\"2023-12-27\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "四平市中心人民医院\n常规通气\n姓名：李洪燕\n性别：女\n年龄：53岁\n吸烟史：\n住院号：111630435\n测试号：20231227014\n身高：168 cm\n体重：82 kg\nFlow [L/s]\nF/V ex\nVol [L]\nVol%Vmax\nVCmax\nF/V in\nTime [s]\n测试日期\n测试时间\n预计值\n实测值\n实/预\n23/12/27\n15:36:14下午\nVT\n[L]\n0.59\n1.51\n258.6\nBF\n[1/min]\n20.00\n18.08\n90.4\nMV\n[L/min]\n11.71\n27.39\n233.8\nVC MAX\n[L]\n3.28\n3.52\n107.3\nERV\n[L]\n0.93\n1.39\n149.9\nIC\n[L]\n2.35\n2.13\n90.5\nFVC\n[L]\n3.17\n3.52\n110.8\nFEV 1\n[L]\n2.71\n2.11\n77.7\nFEV 1 % FVC\n[%]\n79.03\n59.91\n75.8\nFEV 1 % VC MAX\n[%]\n6.54\n4.76\n72.7\nPEF\n[L/s]\n5.68\n2.64\n46.4\nMEF 75\n[L/s]\n3.95\n1.40\n35.4\nMEF 50\n[L/s]\n1.55\n0.53\n34.2\nMEF 25\n[L/s]\n3.22\n1.15\n35.8\nMMEF 75/25\n[L/s]\n0.85\n0.35\n41.0\nFEF 75/85\n[L/s]\n2.16\n78.19\nPIF\n[L/s]\nFEF50 % FIF50\n[%]\nMVV\n[L/min]\n100.45\n63.19\n62.9\nFEV 1*30\n[L/min]\n100.45\n检查意见：\n轻度阻塞型通气功能障碍\n小气道功能异常\n操作者签字：\n医生签字：",
    "role": "user"
  }
]
2026-08-10 11:18:51,623 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:18:51.622+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 19, "failed": 0, "current": {"e139f7cc94ac11f1bd9827cf206dfa2d": {"id": "e139f7cc94ac11f1bd9827cf206dfa2d", "doc_id": "e0cfe59494ac11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "type": "pdf", "location": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "size": 4593431, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786360565919, "task_type": "dataflow", "root_trace_id": "a7e430023e6144f7a5a82bee44b10046", "root_traceparent": "00-a7e430023e6144f7a5a82bee44b10046-21836b890cf4bf02-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:18:59,767 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:18:59,767 INFO     29 [qwen-vl-text] LLM output (len=1178):
{
  "exam_date": "2023-12-27",
  "report_date": "2023-12-27",
  "exam_name": "常规通气",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": "李洪燕",
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "测试日期: 23/12/27\n测试时间: 15:36:14下午\n\n| 指标 | 预计值 | 实测值 | 实/预 (%) |\n| :--- | :--- | :--- | :--- |\n| VT [L] | 0.59 | 1.51 | 258.6 |\n| BF [1/min] | 20.00 | 18.08 | 90.4 |\n| MV [L/min] | 11.71 | 27.39 | 233.8 |\n| VC MAX [L] | 3.28 | 3.52 | 107.3 |\n| ERV [L] | 0.93 | 1.39 | 149.9 |\n| IC [L] | 2.35 | 2.13 | 90.5 |\n| FVC [L] | 3.17 | 3.52 | 110.8 |\n| FEV 1 [L] | 2.71 | 2.11 | 77.7 |\n| FEV 1 % FVC [%] | 79.03 | 59.91 | 75.8 |\n| FEV 1 % VC MAX [%] | 6.54 | 4.76 | 72.7 |\n| PEF [L/s] | 5.68 | 2.64 | 46.4 |\n| MEF 75 [L/s] | 3.95 | 1.40 | 35.4 |\n| MEF 50 [L/s] | 1.55 | 0.53 | 34.2 |\n| MEF 25 [L/s] | 3.22 | 1.15 | 35.8 |\n| MMEF 75/25 [L/s] | 0.85 | 0.35 | 41.0 |\n| FEF 75/85 [L/s] | 2.16 | - | 78.19 |\n| PIF [L/s] | - | - | - |\n| FEF50 % FIF50 [%] | - | - | - |\n| MVV [L/min] | 100.45 | 63.19 | 62.9 |\n| FEV 1*30 [L/min] | 100.45 | - | - |",
  "conclusion": "轻度阻塞型通气功能障碍\n小气道功能异常",
  "physician": null,
  "reviewer": null
}
2026-08-10 11:18:59,770 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1356301, prompt_len=1718
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共120行）
["四平市中心人民医院", "常规通气", "姓名：李洪燕", "性别：女", "年龄：53岁", "吸烟史：", "住院号：111630435", "测试号：20231227014", "身高：168 cm", "体重：82 kg", "Flow [L/s]", "F/V ex", "Vol [L]", "Vol%Vmax", "VCmax", "F/V in", "Time [s]", "测试日期", "测试时间", "预计值", "实测值", "实/预", "23/12/27", "15:36:14下午", "VT", "[L]", "0.59", "1.51", "258.6", "BF", "[1/min]", "20.00", "18.08", "90.4", "MV", "[L/min]", "11.71", "27.39", "233.8", "VC MAX", "[L]", "3.28", "3.52", "107.3", "ERV", "[L]", "0.93", "1.39", "149.9", "IC", "[L]", "2.35", "2.13", "90.5", "FVC", "[L]", "3.17", "3.52", "110.8", "FEV 1", "[L]", "2.71", "2.11", "77.7", "FEV 1 % FVC", "[%]", "79.03", "59.91", "75.8", "FEV 1 % VC MAX", "[%]", "6.54", "4.76", "72.7", "PEF", "[L/s]", "5.68", "2.64", "46.4", "MEF 75", "[L/s]", "3.95", "1.40", "35.4", "MEF 50", "[L/s]", "1.55", "0.53", "34.2", "MEF 25", "[L/s]", "3.22", "1.15", "35.8", "MMEF 75/25", "[L/s]", "0.85", "0.35", "41.0", "FEF 75/85", "[L/s]", "2.16", "78.19", "PIF", "[L/s]", "FEF50 % FIF50", "[%]", "MVV", "[L/min]", "100.45", "63.19", "62.9", "FEV 1*30", "[L/min]", "100.45", "检查意见：", "轻度阻塞型通气功能障碍", "小气道功能异常", "操作者签字：", "医生签字："]

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
2026-08-10 11:19:30,622 INFO     29 [qwen-vl-text] coord API raw response (len=6025):
[
	{"text": "四平市中心人民医院", "bbox": [368, 96, 664, 116]},
	{"text": "常规通气", "bbox": [436, 125, 530, 139]},
	{"text": "姓名：李洪燕", "bbox": [150, 157, 368, 168]},
	{"text": "性别：女", "bbox": [484, 154, 664, 164]},
	{"text": "年龄：53岁", "bbox": [150, 166, 360, 177]},
	{"text": "吸烟史：", "bbox": [484, 163, 545, 173]},
	{"text": "住院号：111630435", "bbox": [150, 175, 395, 186]},
	{"text": "测试号：20231227014", "bbox": [484, 172, 747, 183]},
	{"text": "身高：168 cm", "bbox": [150, 185, 370, 195]},
	{"text": "体重：82 kg", "bbox": [484, 181, 694, 191]},
	{"text": "Flow [L/s]", "bbox": [224, 200, 275, 209]},
	{"text": "F/V ex", "bbox": [368, 199, 404, 207]},
	{"text": "Vol [L]", "bbox": [544, 202, 577, 211]},
	{"text": "Vol%Vmax", "bbox": [498, 240, 559, 248]},
	{"text": "VCmax", "bbox": [557, 250, 592, 258]},
	{"text": "Time [s]", "bbox": [636, 275, 679, 283]},
	{"text": "F/V in", "bbox": [374, 288, 405, 296]},
	{"text": "测试日期", "bbox": [165, 313, 246, 324]},
	{"text": "测试时间", "bbox": [165, 324, 246, 335]},
	{"text": "预计值", "bbox": [487, 298, 548, 309]},
	{"text": "实测值", "bbox": [614, 297, 676, 307]},
	{"text": "实/预", "bbox": [753, 294, 804, 305]},
	{"text": "23/12/27", "bbox": [596, 307, 676, 317]},
	{"text": "15:36:14下午", "bbox": [559, 317, 676, 328]},
	{"text": "VT", "bbox": [165, 346, 187, 355]},
	{"text": "[L]", "bbox": [394, 344, 420, 354]},
	{"text": "0.59", "bbox": [510, 342, 550, 351]},
	{"text": "1.51", "bbox": [637, 340, 677, 350]},
	{"text": "258.6", "bbox": [756, 338, 807, 348]},
	{"text": "BF", "bbox": [165, 357, 187, 366]},
	{"text": "[1/min]", "bbox": [356, 355, 420, 364]},
	{"text": "20.00", "bbox": [501, 352, 550, 362]},
	{"text": "18.08", "bbox": [628, 350, 679, 360]},
	{"text": "90.4", "bbox": [767, 348, 807, 358]},
	{"text": "MV", "bbox": [165, 368, 187, 376]},
	{"text": "[L/min]", "bbox": [356, 365, 420, 374]},
	{"text": "11.71", "bbox": [501, 363, 550, 372]},
	{"text": "27.39", "bbox": [628, 360, 679, 370]},
	{"text": "233.8", "bbox": [756, 358, 807, 368]},
	{"text": "VC MAX", "bbox": [165, 378, 227, 387]},
	{"text": "[L]", "bbox": [394, 376, 420, 385]},
	{"text": "3.28", "bbox": [510, 374, 550, 383]},
	{"text": "3.52", "bbox": [637, 372, 679, 381]},
	{"text": "107.3", "bbox": [758, 370, 807, 379]},
	{"text": "ERV", "bbox": [165, 389, 197, 397]},
	{"text": "[L]", "bbox": [394, 386, 420, 395]},
	{"text": "0.93", "bbox": [510, 384, 550, 393]},
	{"text": "1.39", "bbox": [637, 382, 679, 391]},
	{"text": "149.9", "bbox": [758, 380, 807, 390]},
	{"text": "IC", "bbox": [165, 399, 187, 408]},
	{"text": "[L]", "bbox": [394, 396, 420, 405]},
	{"text": "2.35", "bbox": [510, 394, 550, 404]},
	{"text": "2.13", "bbox": [637, 393, 679, 402]},
	{"text": "90.5", "bbox": [769, 391, 809, 400]},
	{"text": "FVC", "bbox": [165, 420, 197, 429]},
	{"text": "[L]", "bbox": [394, 418, 420, 427]},
	{"text": "3.17", "bbox": [512, 416, 552, 425]},
	{"text": "3.52", "bbox": [640, 414, 681, 423]},
	{"text": "110.8", "bbox": [761, 412, 810, 421]},
	{"text": "FEV 1", "bbox": [165, 431, 217, 440]},
	{"text": "[L]", "bbox": [394, 428, 420, 437]},
	{"text": "2.71", "bbox": [512, 426, 552, 435]},
	{"text": "2.11", "bbox": [640, 425, 681, 434]},
	{"text": "77.7", "bbox": [771, 422, 810, 431]},
	{"text": "FEV 1 % FVC", "bbox": [165, 441, 277, 450]},
	{"text": "[%]", "bbox": [394, 438, 420, 447]},
	{"text": "79.03", "bbox": [505, 447, 554, 456]},
	{"text": "59.91", "bbox": [633, 445, 682, 454]},
	{"text": "75.8", "bbox": [772, 443, 812, 452]},
	{"text": "FEV 1 % VC MAX", "bbox": [165, 452, 308, 461]},
	{"text": "[%]", "bbox": [394, 448, 420, 457]},
	{"text": "6.54", "bbox": [515, 457, 554, 466]},
	{"text": "4.76", "bbox": [643, 455, 684, 464]},
	{"text": "72.7", "bbox": [774, 453, 812, 462]},
	{"text": "PEF", "bbox": [165, 463, 197, 471]},
	{"text": "[L/s]", "bbox": [378, 460, 422, 469]},
	{"text": "5.68", "bbox": [515, 467, 554, 476]},
	{"text": "2.64", "bbox": [643, 465, 684, 474]},
	{"text": "46.4", "bbox": [774, 463, 812, 472]},
	{"text": "MEF 75", "bbox": [165, 473, 228, 482]},
	{"text": "[L/s]", "bbox": [378, 470, 422, 479]},
	{"text": "3.95", "bbox": [515, 477, 554, 486]},
	{"text": "1.40", "bbox": [643, 475, 684, 484]},
	{"text": "35.4", "bbox": [774, 473, 812, 482]},
	{"text": "MEF 50", "bbox": [165, 484, 228, 493]},
	{"text": "[L/s]", "bbox": [378, 480, 422, 489]},
	{"text": "1.55", "bbox": [515, 487, 554, 496]},
	{"text": "0.53", "bbox": [643, 485, 684, 494]},
	{"text": "34.2", "bbox": [774, 483, 812, 492]},
	{"text": "MEF 25", "bbox": [165, 494, 228, 503]},
	{"text": "[L/s]", "bbox": [378, 490, 422, 499]},
	{"text": "3.22", "bbox": [515, 497, 554, 506]},
	{"text": "1.15", "bbox": [643, 495, 684, 504]},
	{"text": "35.8", "bbox": [774, 493, 812, 502]},
	{"text": "MMEF 75/25", "bbox": [165, 505, 269, 514]},
	{"text": "[L/s]", "bbox": [378, 500, 422, 509]},
	{"text": "0.85", "bbox": [515, 507, 554, 516]},
	{"text": "0.35", "bbox": [643, 505, 684, 514]},
	{"text": "41.0", "bbox": [777, 504, 815, 513]},
	{"text": "FEF 75/85", "bbox": [165, 515, 260, 524]},
	{"text": "[L/s]", "bbox": [378, 510, 422, 519]},
	{"text": "2.16", "bbox": [645, 516, 686, 525]},
	{"text": "PIF", "bbox": [165, 526, 199, 535]},
	{"text": "[L/s]", "bbox": [378, 520, 422, 529]},
	{"text": "78.19", "bbox": [637, 526, 687, 536]},
	{"text": "FEF50 % FIF50", "bbox": [165, 536, 300, 545]},
	{"text": "[%]", "bbox": [400, 531, 425, 540]},
	{"text": "MVV", "bbox": [165, 547, 200, 556]},
	{"text": "[L/min]", "bbox": [360, 543, 425, 553]},
	{"text": "100.45", "bbox": [500, 541, 557, 551]},
	{"text": "63.19", "bbox": [638, 550, 690, 560]},
	{"text": "62.9", "bbox": [780, 549, 820, 558]},
	{"text": "FEV 1*30", "bbox": [165, 557, 250, 566]},
	{"text": "[L/min]", "bbox": [360, 554, 425, 563]},
	{"text": "100.45", "bbox": [500, 552, 557, 561]},
	{"text": "检查意见：", "bbox": [74, 580, 173, 593]},
	{"text": "轻度阻塞型通气功能障碍", "bbox": [107, 613, 314, 627]},
	{"text": "小气道功能异常", "bbox": [107, 635, 240, 648]},
	{"text": "操作者签字：", "bbox": [747, 643, 850, 656]},
	{"text": "医生签字：", "bbox": [748, 663, 833, 677]}
]
2026-08-10 11:19:30,623 INFO     29 [qwen-vl-text] coord API: raw_items=120, valid_items=120, elapsed=30.9s
2026-08-10 11:19:30,623 INFO     29 [qwen-vl-text] coord item[0]: text=四平市中心人民医院, bbox=[368, 96, 664, 116]
2026-08-10 11:19:30,623 INFO     29 [qwen-vl-text] coord item[1]: text=常规通气, bbox=[436, 125, 530, 139]
2026-08-10 11:19:30,623 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：李洪燕, bbox=[150, 157, 368, 168]
2026-08-10 11:19:30,623 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女, bbox=[484, 154, 664, 164]
2026-08-10 11:19:30,623 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：53岁, bbox=[150, 166, 360, 177]
2026-08-10 11:19:30,623 INFO     29 [qwen-vl-text] coord item[5]: text=吸烟史：, bbox=[484, 163, 545, 173]
2026-08-10 11:19:30,623 INFO     29 [qwen-vl-text] coord item[6]: text=住院号：111630435, bbox=[150, 175, 395, 186]
2026-08-10 11:19:30,623 INFO     29 [qwen-vl-text] coord item[7]: text=测试号：20231227014, bbox=[484, 172, 747, 183]
2026-08-10 11:19:30,623 INFO     29 [qwen-vl-text] coord item[8]: text=身高：168 cm, bbox=[150, 185, 370, 195]
2026-08-10 11:19:30,623 INFO     29 [qwen-vl-text] coord item[9]: text=体重：82 kg, bbox=[484, 181, 694, 191]
2026-08-10 11:19:30,623 INFO     29 [qwen-vl-text] coord item[10]: text=Flow [L/s], bbox=[224, 200, 275, 209]
2026-08-10 11:19:30,623 INFO     29 [qwen-vl-text] coord item[11]: text=F/V ex, bbox=[368, 199, 404, 207]
2026-08-10 11:19:30,623 INFO     29 [qwen-vl-text] coord item[12]: text=Vol [L], bbox=[544, 202, 577, 211]
2026-08-10 11:19:30,623 INFO     29 [qwen-vl-text] coord item[13]: text=Vol%Vmax, bbox=[498, 240, 559, 248]
2026-08-10 11:19:30,624 INFO     29 [qwen-vl-text] coord item[14]: text=VCmax, bbox=[557, 250, 592, 258]
2026-08-10 11:19:30,624 INFO     29 [qwen-vl-text] coord item[15]: text=Time [s], bbox=[636, 275, 679, 283]
2026-08-10 11:19:30,624 INFO     29 [qwen-vl-text] coord item[16]: text=F/V in, bbox=[374, 288, 405, 296]
2026-08-10 11:19:30,624 INFO     29 [qwen-vl-text] coord item[17]: text=测试日期, bbox=[165, 313, 246, 324]
2026-08-10 11:19:30,624 INFO     29 [qwen-vl-text] coord item[18]: text=测试时间, bbox=[165, 324, 246, 335]
2026-08-10 11:19:30,624 INFO     29 [qwen-vl-text] coord item[19]: text=预计值, bbox=[487, 298, 548, 309]
2026-08-10 11:19:30,624 INFO     29 [qwen-vl-text] coord item[20]: text=实测值, bbox=[614, 297, 676, 307]
2026-08-10 11:19:30,624 INFO     29 [qwen-vl-text] coord item[21]: text=实/预, bbox=[753, 294, 804, 305]
2026-08-10 11:19:30,624 INFO     29 [qwen-vl-text] coord item[22]: text=23/12/27, bbox=[596, 307, 676, 317]
2026-08-10 11:19:30,624 INFO     29 [qwen-vl-text] coord item[23]: text=15:36:14下午, bbox=[559, 317, 676, 328]
2026-08-10 11:19:30,624 INFO     29 [qwen-vl-text] coord item[24]: text=VT, bbox=[165, 346, 187, 355]
2026-08-10 11:19:30,624 INFO     29 [qwen-vl-text] coord item[25]: text=[L], bbox=[394, 344, 420, 354]
2026-08-10 11:19:30,624 INFO     29 [qwen-vl-text] coord item[26]: text=0.59, bbox=[510, 342, 550, 351]
2026-08-10 11:19:30,624 INFO     29 [qwen-vl-text] coord item[27]: text=1.51, bbox=[637, 340, 677, 350]
2026-08-10 11:19:30,624 INFO     29 [qwen-vl-text] coord item[28]: text=258.6, bbox=[756, 338, 807, 348]
2026-08-10 11:19:30,624 INFO     29 [qwen-vl-text] coord item[29]: text=BF, bbox=[165, 357, 187, 366]
2026-08-10 11:19:30,624 INFO     29 [qwen-vl-text] coord item[30]: text=[1/min], bbox=[356, 355, 420, 364]
2026-08-10 11:19:30,625 INFO     29 [qwen-vl-text] coord item[31]: text=20.00, bbox=[501, 352, 550, 362]
2026-08-10 11:19:30,625 INFO     29 [qwen-vl-text] coord item[32]: text=18.08, bbox=[628, 350, 679, 360]
2026-08-10 11:19:30,625 INFO     29 [qwen-vl-text] coord item[33]: text=90.4, bbox=[767, 348, 807, 358]
2026-08-10 11:19:30,625 INFO     29 [qwen-vl-text] coord item[34]: text=MV, bbox=[165, 368, 187, 376]
2026-08-10 11:19:30,625 INFO     29 [qwen-vl-text] coord item[35]: text=[L/min], bbox=[356, 365, 420, 374]
2026-08-10 11:19:30,625 INFO     29 [qwen-vl-text] coord item[36]: text=11.71, bbox=[501, 363, 550, 372]
2026-08-10 11:19:30,625 INFO     29 [qwen-vl-text] coord item[37]: text=27.39, bbox=[628, 360, 679, 370]
2026-08-10 11:19:30,625 INFO     29 [qwen-vl-text] coord item[38]: text=233.8, bbox=[756, 358, 807, 368]
2026-08-10 11:19:30,625 INFO     29 [qwen-vl-text] coord item[39]: text=VC MAX, bbox=[165, 378, 227, 387]
2026-08-10 11:19:30,625 INFO     29 [qwen-vl-text] coord item[40]: text=[L], bbox=[394, 376, 420, 385]
2026-08-10 11:19:30,625 INFO     29 [qwen-vl-text] coord item[41]: text=3.28, bbox=[510, 374, 550, 383]
2026-08-10 11:19:30,625 INFO     29 [qwen-vl-text] coord item[42]: text=3.52, bbox=[637, 372, 679, 381]
2026-08-10 11:19:30,625 INFO     29 [qwen-vl-text] coord item[43]: text=107.3, bbox=[758, 370, 807, 379]
2026-08-10 11:19:30,625 INFO     29 [qwen-vl-text] coord item[44]: text=ERV, bbox=[165, 389, 197, 397]
2026-08-10 11:19:30,625 INFO     29 [qwen-vl-text] coord item[45]: text=[L], bbox=[394, 386, 420, 395]
2026-08-10 11:19:30,625 INFO     29 [qwen-vl-text] coord item[46]: text=0.93, bbox=[510, 384, 550, 393]
2026-08-10 11:19:30,625 INFO     29 [qwen-vl-text] coord item[47]: text=1.39, bbox=[637, 382, 679, 391]
2026-08-10 11:19:30,626 INFO     29 [qwen-vl-text] coord item[48]: text=149.9, bbox=[758, 380, 807, 390]
2026-08-10 11:19:30,626 INFO     29 [qwen-vl-text] coord item[49]: text=IC, bbox=[165, 399, 187, 408]
2026-08-10 11:19:30,626 INFO     29 [qwen-vl-text] coord item[50]: text=[L], bbox=[394, 396, 420, 405]
2026-08-10 11:19:30,626 INFO     29 [qwen-vl-text] coord item[51]: text=2.35, bbox=[510, 394, 550, 404]
2026-08-10 11:19:30,626 INFO     29 [qwen-vl-text] coord item[52]: text=2.13, bbox=[637, 393, 679, 402]
2026-08-10 11:19:30,626 INFO     29 [qwen-vl-text] coord item[53]: text=90.5, bbox=[769, 391, 809, 400]
2026-08-10 11:19:30,626 INFO     29 [qwen-vl-text] coord item[54]: text=FVC, bbox=[165, 420, 197, 429]
2026-08-10 11:19:30,626 INFO     29 [qwen-vl-text] coord item[55]: text=[L], bbox=[394, 418, 420, 427]
2026-08-10 11:19:30,626 INFO     29 [qwen-vl-text] coord item[56]: text=3.17, bbox=[512, 416, 552, 425]
2026-08-10 11:19:30,626 INFO     29 [qwen-vl-text] coord item[57]: text=3.52, bbox=[640, 414, 681, 423]
2026-08-10 11:19:30,626 INFO     29 [qwen-vl-text] coord item[58]: text=110.8, bbox=[761, 412, 810, 421]
2026-08-10 11:19:30,626 INFO     29 [qwen-vl-text] coord item[59]: text=FEV 1, bbox=[165, 431, 217, 440]
2026-08-10 11:19:30,626 INFO     29 [qwen-vl-text] coord item[60]: text=[L], bbox=[394, 428, 420, 437]
2026-08-10 11:19:30,626 INFO     29 [qwen-vl-text] coord item[61]: text=2.71, bbox=[512, 426, 552, 435]
2026-08-10 11:19:30,626 INFO     29 [qwen-vl-text] coord item[62]: text=2.11, bbox=[640, 425, 681, 434]
2026-08-10 11:19:30,626 INFO     29 [qwen-vl-text] coord item[63]: text=77.7, bbox=[771, 422, 810, 431]
2026-08-10 11:19:30,626 INFO     29 [qwen-vl-text] coord item[64]: text=FEV 1 % FVC, bbox=[165, 441, 277, 450]
2026-08-10 11:19:30,626 INFO     29 [qwen-vl-text] coord item[65]: text=[%], bbox=[394, 438, 420, 447]
2026-08-10 11:19:30,626 INFO     29 [qwen-vl-text] coord item[66]: text=79.03, bbox=[505, 447, 554, 456]
2026-08-10 11:19:30,626 INFO     29 [qwen-vl-text] coord item[67]: text=59.91, bbox=[633, 445, 682, 454]
2026-08-10 11:19:30,626 INFO     29 [qwen-vl-text] coord item[68]: text=75.8, bbox=[772, 443, 812, 452]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[69]: text=FEV 1 % VC MAX, bbox=[165, 452, 308, 461]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[70]: text=[%], bbox=[394, 448, 420, 457]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[71]: text=6.54, bbox=[515, 457, 554, 466]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[72]: text=4.76, bbox=[643, 455, 684, 464]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[73]: text=72.7, bbox=[774, 453, 812, 462]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[74]: text=PEF, bbox=[165, 463, 197, 471]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[75]: text=[L/s], bbox=[378, 460, 422, 469]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[76]: text=5.68, bbox=[515, 467, 554, 476]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[77]: text=2.64, bbox=[643, 465, 684, 474]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[78]: text=46.4, bbox=[774, 463, 812, 472]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[79]: text=MEF 75, bbox=[165, 473, 228, 482]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[80]: text=[L/s], bbox=[378, 470, 422, 479]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[81]: text=3.95, bbox=[515, 477, 554, 486]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[82]: text=1.40, bbox=[643, 475, 684, 484]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[83]: text=35.4, bbox=[774, 473, 812, 482]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[84]: text=MEF 50, bbox=[165, 484, 228, 493]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[85]: text=[L/s], bbox=[378, 480, 422, 489]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[86]: text=1.55, bbox=[515, 487, 554, 496]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[87]: text=0.53, bbox=[643, 485, 684, 494]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[88]: text=34.2, bbox=[774, 483, 812, 492]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[89]: text=MEF 25, bbox=[165, 494, 228, 503]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[90]: text=[L/s], bbox=[378, 490, 422, 499]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[91]: text=3.22, bbox=[515, 497, 554, 506]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[92]: text=1.15, bbox=[643, 495, 684, 504]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[93]: text=35.8, bbox=[774, 493, 812, 502]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[94]: text=MMEF 75/25, bbox=[165, 505, 269, 514]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[95]: text=[L/s], bbox=[378, 500, 422, 509]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[96]: text=0.85, bbox=[515, 507, 554, 516]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[97]: text=0.35, bbox=[643, 505, 684, 514]
2026-08-10 11:19:30,627 INFO     29 [qwen-vl-text] coord item[98]: text=41.0, bbox=[777, 504, 815, 513]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] coord item[99]: text=FEF 75/85, bbox=[165, 515, 260, 524]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] coord item[100]: text=[L/s], bbox=[378, 510, 422, 519]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] coord item[101]: text=2.16, bbox=[645, 516, 686, 525]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] coord item[102]: text=PIF, bbox=[165, 526, 199, 535]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] coord item[103]: text=[L/s], bbox=[378, 520, 422, 529]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] coord item[104]: text=78.19, bbox=[637, 526, 687, 536]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] coord item[105]: text=FEF50 % FIF50, bbox=[165, 536, 300, 545]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] coord item[106]: text=[%], bbox=[400, 531, 425, 540]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] coord item[107]: text=MVV, bbox=[165, 547, 200, 556]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] coord item[108]: text=[L/min], bbox=[360, 543, 425, 553]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] coord item[109]: text=100.45, bbox=[500, 541, 557, 551]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] coord item[110]: text=63.19, bbox=[638, 550, 690, 560]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] coord item[111]: text=62.9, bbox=[780, 549, 820, 558]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] coord item[112]: text=FEV 1*30, bbox=[165, 557, 250, 566]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] coord item[113]: text=[L/min], bbox=[360, 554, 425, 563]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] coord item[114]: text=100.45, bbox=[500, 552, 557, 561]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] coord item[115]: text=检查意见：, bbox=[74, 580, 173, 593]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] coord item[116]: text=轻度阻塞型通气功能障碍, bbox=[107, 613, 314, 627]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] coord item[117]: text=小气道功能异常, bbox=[107, 635, 240, 648]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] coord item[118]: text=操作者签字：, bbox=[747, 643, 850, 656]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] coord item[119]: text=医生签字：, bbox=[748, 663, 833, 677]
2026-08-10 11:19:30,628 INFO     29 [qwen-vl-text] page=4 — 120/120 coords, api_time=30.9s
2026-08-10 11:19:30,629 INFO     29 [qwen-vl-text] new_positions (120):
[[4, 219.06305078124998, 395.265939453125, 101.593921875, 122.759322265625], [4, 259.5420927734375, 315.49841552734375, 132.28375244140625, 147.09953271484375], [4, 89.29200439453125, 219.06305078124998, 166.14839306640624, 177.78936328125], [4, 288.1155341796875, 395.265939453125, 162.9735830078125, 173.556283203125], [4, 89.29200439453125, 214.30081054687497, 175.6728232421875, 187.31379345703124], [4, 288.1155341796875, 324.42761596679685, 172.49801318359374, 183.08071337890624], [4, 89.29200439453125, 235.13561157226562, 185.19725341796874, 196.8382236328125], [4, 288.1155341796875, 444.6741818847656, 182.022443359375, 193.66341357421874], [4, 89.29200439453125, 220.25361083984373, 195.77995361328124, 206.36265380859376], [4, 288.1155341796875, 413.12434033203124, 191.54687353515624, 202.12957373046873], [4, 133.3427265625, 163.7020080566406, 211.65400390625, 221.17843408203126], [4, 219.06305078124998, 240.49313183593748, 210.59573388671876, 219.06189404296876], [4, 323.8323359375, 343.47657690429685, 213.7705439453125, 223.29497412109376], [4, 296.44945458984375, 332.7615363769531, 253.9848046875, 262.45096484375], [4, 331.5709763183593, 352.40577734374995, 264.5675048828125, 273.0336650390625], [4, 378.5980986328125, 404.1951398925781, 291.0242553710938, 299.49041552734377], [4, 222.63473095703122, 241.08841186523435, 304.781765625, 313.24792578125], [4, 98.22120483398437, 146.43888720703123, 331.23851611328126, 342.879486328125], [4, 98.22120483398437, 146.43888720703123, 342.879486328125, 354.52045654296876], [4, 289.9013742675781, 326.21345605468747, 315.3644658203125, 327.00543603515627], [4, 365.5019379882812, 402.40929980468746, 314.30619580078127, 324.88889599609377], [4, 448.24586206054687, 478.60514355468746, 311.1313857421875, 322.77235595703127], [4, 354.7868974609375, 402.40929980468746, 324.88889599609377, 335.47159619140626], [4, 332.7615363769531, 402.40929980468746, 335.47159619140626, 347.11256640625], [4, 98.22120483398437, 111.31736547851561, 366.1614267578125, 375.68585693359375], [4, 234.54033154296874, 250.01761230468747, 364.04488671875, 374.6275869140625], [4, 303.59281494140623, 327.4040161132812, 361.9283466796875, 371.45277685546876], [4, 379.19337866210935, 403.00457983398434, 359.811806640625, 370.3945068359375], [4, 450.0317021484375, 480.3909836425781, 357.6952666015625, 368.277966796875], [4, 98.22120483398437, 111.31736547851561, 377.80239697265625, 387.3268271484375], [4, 211.91969042968748, 250.01761230468747, 375.68585693359375, 385.210287109375], [4, 298.2352946777344, 327.4040161132812, 372.511046875, 383.0937470703125], [4, 373.8358583984375, 404.1951398925781, 370.3945068359375, 380.97720703125], [4, 456.5797824707031, 480.3909836425781, 368.277966796875, 378.8606669921875], [4, 98.22120483398437, 111.31736547851561, 389.4433671875, 397.90952734374997], [4, 211.91969042968748, 250.01761230468747, 386.26855712890625, 395.7929873046875], [4, 298.2352946777344, 327.4040161132812, 384.15201708984375, 393.676447265625], [4, 373.8358583984375, 404.1951398925781, 380.97720703125, 391.5599072265625], [4, 450.0317021484375, 480.3909836425781, 378.8606669921875, 389.4433671875], [4, 98.22120483398437, 135.1285666503906, 400.02606738281247, 409.55049755859375], [4, 234.54033154296874, 250.01761230468747, 397.90952734374997, 407.43395751953125], [4, 303.59281494140623, 327.4040161132812, 395.7929873046875, 405.31741748046875], [4, 379.19337866210935, 404.1951398925781, 393.676447265625, 403.20087744140625], [4, 451.22226220703124, 480.3909836425781, 391.5599072265625, 401.08433740234375], [4, 98.22120483398437, 117.27016577148437, 411.66703759765625, 420.13319775390624], [4, 234.54033154296874, 250.01761230468747, 408.4922275390625, 418.01665771484375], [4, 303.59281494140623, 327.4040161132812, 406.3756875, 415.90011767578125], [4, 379.19337866210935, 404.1951398925781, 404.25914746093747, 413.78357763671875], [4, 451.22226220703124, 480.3909836425781, 402.14260742187497, 412.7253076171875], [4, 98.22120483398437, 111.31736547851561, 422.24973779296874, 431.77416796875], [4, 234.54033154296874, 250.01761230468747, 419.074927734375, 428.59935791015624], [4, 303.59281494140623, 327.4040161132812, 416.9583876953125, 427.541087890625], [4, 379.19337866210935, 404.1951398925781, 415.90011767578125, 425.4245478515625], [4, 457.77034252929684, 481.5815437011718, 413.78357763671875, 423.3080078125], [4, 98.22120483398437, 117.27016577148437, 444.473408203125, 453.99783837890624], [4, 234.54033154296874, 250.01761230468747, 442.3568681640625, 451.88129833984374], [4, 304.783375, 328.59457617187496, 440.240328125, 449.76475830078124], [4, 380.97921875, 405.38569995117183, 438.1237880859375, 447.64821826171874], [4, 453.00810229492185, 482.1768237304687, 436.007248046875, 445.53167822265624], [4, 98.22120483398437, 129.17576635742188, 456.11437841796874, 465.63880859375], [4, 234.54033154296874, 250.01761230468747, 452.939568359375, 462.46399853515624], [4, 304.783375, 328.59457617187496, 450.8230283203125, 460.34745849609374], [4, 380.97921875, 405.38569995117183, 449.76475830078124, 459.2891884765625], [4, 458.9609025878906, 482.1768237304687, 446.5899482421875, 456.11437841796874], [4, 98.22120483398437, 164.89256811523435, 466.69707861328123, 476.2215087890625], [4, 234.54033154296874, 250.01761230468747, 463.5222685546875, 473.04669873046873], [4, 300.61641479492187, 329.7851362304687, 473.04669873046873, 482.57112890625], [4, 376.81225854492186, 405.9809799804687, 470.93015869140623, 480.4545888671875], [4, 459.55618261718746, 483.36738378906244, 468.81361865234373, 478.338048828125], [4, 98.22120483398437, 183.34624902343748, 478.338048828125, 487.86247900390623], [4, 234.54033154296874, 250.01761230468747, 474.10496875, 483.62939892578123], [4, 306.5692150878906, 329.7851362304687, 483.62939892578123, 493.1538291015625], [4, 382.7650588378906, 407.17154003906245, 481.51285888671873, 491.0372890625], [4, 460.7467426757812, 483.36738378906244, 479.39631884765623, 488.9207490234375], [4, 98.22120483398437, 117.27016577148437, 489.97901904296873, 498.4451791992187], [4, 225.01585107421874, 251.20817236328122, 486.804208984375, 496.32863916015623], [4, 306.5692150878906, 329.7851362304687, 494.21209912109373, 503.736529296875], [4, 382.7650588378906, 407.17154003906245, 492.09555908203123, 501.6199892578125], [4, 460.7467426757812, 483.36738378906244, 489.97901904296873, 499.50344921875], [4, 98.22120483398437, 135.72384667968748, 500.5617192382812, 510.0861494140625], [4, 225.01585107421874, 251.20817236328122, 497.3869091796875, 506.9113393554687], [4, 306.5692150878906, 329.7851362304687, 504.7947993164062, 514.3192294921874], [4, 382.7650588378906, 407.17154003906245, 502.6782592773437, 512.202689453125], [4, 460.7467426757812, 483.36738378906244, 500.5617192382812, 510.0861494140625], [4, 98.22120483398437, 135.72384667968748, 512.202689453125, 521.7271196289063], [4, 225.01585107421874, 251.20817236328122, 507.969609375, 517.4940395507813], [4, 306.5692150878906, 329.7851362304687, 515.3774995117187, 524.9019296875], [4, 382.7650588378906, 407.17154003906245, 513.2609594726563, 522.7853896484374], [4, 460.7467426757812, 483.36738378906244, 511.1444194335937, 520.668849609375], [4, 98.22120483398437, 135.72384667968748, 522.7853896484374, 532.3098198242187], [4, 225.01585107421874, 251.20817236328122, 518.5523095703124, 528.0767397460937], [4, 306.5692150878906, 329.7851362304687, 525.9601997070313, 535.4846298828124], [4, 382.7650588378906, 407.17154003906245, 523.8436596679687, 533.36808984375], [4, 460.7467426757812, 483.36738378906244, 521.7271196289063, 531.2515498046874], [4, 98.22120483398437, 160.13032788085937, 534.4263598632813, 543.9507900390626], [4, 225.01585107421874, 251.20817236328122, 529.135009765625, 538.6594399414063], [4, 306.5692150878906, 329.7851362304687, 536.5428999023437, 546.067330078125], [4, 382.7650588378906, 407.17154003906245, 534.4263598632813, 543.9507900390626], [4, 462.5325827636718, 485.15322387695306, 533.36808984375, 542.8925200195313], [4, 98.22120483398437, 154.77280761718748, 545.0090600585937, 554.533490234375], [4, 225.01585107421874, 251.20817236328122, 539.7177099609374, 549.2421401367187], [4, 383.95561889648434, 408.3621000976562, 546.067330078125, 555.5917602539063], [4, 98.22120483398437, 118.46072583007812, 556.6500302734376, 566.1744604492187], [4, 225.01585107421874, 251.20817236328122, 550.30041015625, 559.8248403320313], [4, 379.19337866210935, 408.95738012695307, 556.6500302734376, 567.23273046875], [4, 98.22120483398437, 178.5840087890625, 567.23273046875, 576.7571606445313], [4, 238.11201171874998, 252.99401245117187, 561.9413803710937, 571.465810546875], [4, 98.22120483398437, 119.05600585937499, 578.8737006835937, 588.398130859375], [4, 214.30081054687497, 252.99401245117187, 574.6406206054687, 585.2233208007813], [4, 297.6400146484375, 331.5709763183593, 572.5240805664063, 583.1067807617187], [4, 379.7886586914062, 410.74322021484375, 582.0485107421875, 592.6312109375], [4, 464.31842285156245, 488.1296240234375, 580.9902407226563, 590.5146708984375], [4, 98.22120483398437, 148.82000732421875, 589.4564008789063, 598.9808310546875], [4, 214.30081054687497, 252.99401245117187, 586.2815908203125, 595.8060209960937], [4, 297.6400146484375, 331.5709763183593, 584.16505078125, 593.6894809570313], [4, 44.05072216796874, 102.98344506835937, 613.796611328125, 627.5541215820313], [4, 63.69496313476562, 186.91792919921875, 648.7195219726563, 663.5353022460937], [4, 63.69496313476562, 142.86720703125, 672.0014624023437, 685.75897265625], [4, 444.6741818847656, 505.98802490234374, 680.4676225585938, 694.2251328125], [4, 445.26946191406245, 495.86826440429684, 701.6330229492188, 716.4488032226562]]
2026-08-10 11:19:30,629 INFO     29 [qwen-vl-text] ═══ DONE ═══ 120 positions, pages=1, time=39.2s
2026-08-10 11:19:30,643 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 11:19:30,643 INFO     29 [Trace] task=e139f7cc | doc=LHYA-哮喘-沈阳医大四.pdf | Extractor:ExaminationReport | outputs={"chunks": "2 items, types={'ExaminationReport': 2}", "html": "", "json": "408 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Examination\": 2, \"chunks_Medication\": 2}"}
2026-08-10 11:19:30,643 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 11:19:30,644 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:19:30.643+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 19, "failed": 0, "current": {"e139f7cc94ac11f1bd9827cf206dfa2d": {"id": "e139f7cc94ac11f1bd9827cf206dfa2d", "doc_id": "e0cfe59494ac11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "type": "pdf", "location": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "size": 4593431, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786360565919, "task_type": "dataflow", "root_trace_id": "a7e430023e6144f7a5a82bee44b10046", "root_traceparent": "00-a7e430023e6144f7a5a82bee44b10046-21836b890cf4bf02-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:19:30,652 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:19:30,652 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:19:31,578 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:19:31,588 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 11:19:31,588 INFO     29 [Trace] task=e139f7cc | doc=LHYA-哮喘-沈阳医大四.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "408 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Examination\": 2, \"chunks_Medication\": 2}"}
2026-08-10 11:19:31,588 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 11:19:31,589 INFO     29 [ChunkMerger] Merged 7 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 3, 'Extractor:Medication': 2, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 2, 'Extractor:Progress': 1} (filtered 6 noise chunks)
2026-08-10 11:19:31,606 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 11:19:31,606 INFO     29 [Trace] task=e139f7cc | doc=LHYA-哮喘-沈阳医大四.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "7 items, types={'OutpatientRecord': 3, 'MedicationRecord': 2, 'ExaminationReport': 2}", "name": "LHYA-哮喘-沈阳医大四.pdf"}
2026-08-10 11:19:31,606 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 11:19:31,695 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786360568318, 'update_date': datetime.datetime(2026, 8, 10, 11, 16, 8), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 913723, 'status': '1'}
2026-08-10 11:19:31,942 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=四平市中心人民医院
门诊诊断书
0003316
(患者保管)
SPZXYy-JLLC-042
姓名
性别
女
年龄
54岁
单位
诊断
支气管哮喘
病情诊断摘要依据
发作性喘息30余年，双肺干
啰音，诊断支气管哮喘
医生处理意见
1.平喘治疗
2.随访
医生签字：
门诊部负责人签字：
科主任签字：
门诊部盖章：2023年12月27日
(无公章和医生章无效)
---
四平市中医医院
门诊病历
初诊
2025年11月26日
肾病糖尿病科
姓名
性别
女性
年龄
55岁
门诊号码
202511260272
（1）
发病日期
2025-11-26
类别
自费
保险卡号
就诊方式
便民门诊费
医生
王亚新
联系地址
四平铁西
联系电话
13689710485
身份证号
职业
体温 36.5 ℃ 血压 130、80 mmHg 脉搏 70 次/分
药物过敏史
无
主诉:
自述糖尿病4年，支气管哮喘30余年
病史:
糖尿病4年，尿中有沫。伴双下肢水肿+。现二甲双胍片，0.5，日3次，口服。血糖控制不佳。葡萄糖：12.39mmol/1.，糖化：
10.1%，一周前感冒山现间断咳嗽气短胸闷，活动后加重，有夜间憋醒史，咳白痰，无发热，饮食尚可，大小便正常。
临床诊断：2型糖尿病 支气管哮喘急性发作
治疗方案:
建议入院治疗，拒绝。糖尿病饮食，监测血糖，继续用药治疗，有变化随诊。沙美特罗卡替松粉吸入剂50微克/250微克/揿/盒，
每瓶60揿（30个用药计量），甲泼尼龙片4mg×24片/盒（口服5天）。
结论:
病程记录:
医生（印章）：
2025年11月27日 11:18
---
四平市中医医院
内二疗区
门诊病历
初诊
2025年12月31日
姓名
性别：女性
年龄：55岁
门诊号码：202512310183
（1）
发病日期：2025-12-31
类别：自费
保险卡号
就诊方式：服务号
医生：张楷婷
联系地址：吉林省四平市
联系电话：13689710485
身份证号：220303197009242283
职业：
体温 36.4 ℃ 血压 120/78 mmHg 脉搏 66 次/分
药物过敏史：否
主诉：发现血糖升高4年
病史：发现血糖升高4年，现二甲双胍片0.5g日3次口服控制血糖。测空腹血糖11.41mmol/L，糖化血红蛋白8.9%，尿糖3+。
临床诊断：2型糖尿病
治疗方案：建议患者入院治疗，患者暂拒；糖尿病饮食，口服二甲双胍片0.5g日3次，适当饮水，监测血糖，定期复查，病情变化随诊
结论：
病程记录：
医生（印章）：
2025年12月31日 15:12
---
信康大药房--佳合分店
单号：250927207100156
日期：2025-09-27 17:52:20
会员卡号：13689710485
姓名：
积分：37
总积分：47
药品名称
规格
生产企业/药品上市许可持有人
产地
剂型
批号
有效期
数量
单价
金额
12534
185.00
沙美特罗替卡松吸入粉雾剂
50微克/250微克/60泡/盒
葛兰素史克集团吸入粉雾剂
JD6K
2027-06-18
2盒
185.00
370.00
信康大药房温馨提示：您购买的
药品需要常温储存(10℃-30℃)
合计：
370.00
实收：
370.00
开票员：王影
营业员：7139
药品售出无质量问题不退不换！
电话：0434-3333658
---
信康大药房--佳合分店
单号：251128207100163
日期：2025-11-28 16:38:41
会员卡号：13689710485
姓名：
积分：37
总积分：84
药品名称
规格
生产企业/药品上市许可持有人
产地
剂型
批号
有效期
数量
单价
金额
12534
185.00
沙美特罗替卡松吸入粉雾剂
50微克/250微克/60泡/盒
葛兰素史克集团吸入粉雾剂
JD6K
2027-06-18
2盒
185.00
370.00
信康大药房温馨提示：您购买的
药品需要常温储存（10℃-30℃）
合计：
370.00
实收：
370.00
开票员：张欣
营业员：7140
药品售出无质量问题不退不换！
电话：0434-3333658
---
四平市中心人民医院
常规通气+舒张试验
姓名：
年龄：53岁
住院号：111630435
身高：168 cm
性别：女
吸烟史：
测试号：20231227014
体重：82 kg
Flow [L/s]
F/V ex
Vol [L]
Vol%VCmax
VCmax
Time [s]
F/V in
测试日期
测试时间
预计值
药前
前/预%
药后
后/预% 改善率 (%)
23/12/27
23/12/27
15:36:14
15:51:45
MV
[L/min]
11.71
27.39
233.8
3.78
115.4
7.6
VC MAX
[L]
3.28
3.52
107.3
FVC
[L]
3.17
3.52
110.8
3.78
119.2
7.6
FEV 1
[L]
2.71
2.11
77.7
2.39
88.3
13.7
FEV 1 % FVC
[%]
59.91
63.29
5.6
FEV 1 % VC MAX
[%]
79.03
59.91
75.8
63.29
80.1
5.6
PEF
[L/s]
6.54
4.76
72.7
4.54
69.4
-4.6
MEF 75
[L/s]
5.68
2.64
46.4
3.29
58.0
24.9
MEF 50
[L/s]
3.95
1.40
35.4
1.80
45.5
28.5
MEF 25
[L/s]
1.55
0.53
34.2
0.65
42.1
22.9
MMEF 75/25
[L/s]
3.22
1.15
35.8
1.44
44.6
24.5
MVV
[L/min]
100.45
检查意见：
结果：支气管舒张实验(+)。
操作者签字：
医生签字：
---
四平市中心人民医院
常规通气
姓名：李洪燕
性别：女
年龄：53岁
吸烟史：
住院号：111630435
测试号：20231227014
身高：168 cm
体重：82 kg
Flow [L/s]
F/V ex
Vol [L]
Vol%Vmax
VCmax
F/V in
Time [s]
测试日期
测试时间
预计值
实测值
实/预
23/12/27
15:36:14下午
VT
[L]
0.59
1.51
258.6
BF
[1/min]
20.00
18.08
90.4
MV
[L/min]
11.71
27.39
233.8
VC MAX
[L]
3.28
3.52
107.3
ERV
[L]
0.93
1.39
149.9
IC
[L]
2.35
2.13
90.5
FVC
[L]
3.17
3.52
110.8
FEV 1
[L]
2.71
2.11
77.7
FEV 1 % FVC
[%]
79.03
59.91
75.8
FEV 1 % VC MAX
[%]
6.54
4.76
72.7
PEF
[L/s]
5.68
2.64
46.4
MEF 75
[L/s]
3.95
1.40
35.4
MEF 50
[L/s]
1.55
0.53
34.2
MEF 25
[L/s]
3.22
1.15
35.8
MMEF 75/25
[L/s]
0.85
0.35
41.0
FEF 75/85
[L/s]
2.16
78.19
PIF
[L/s]
FEF50 % FIF50
[%]
MVV
[L/min]
100.45
63.19
62.9
FEV 1*30
[L/min]
100.45
检查意见：
轻度阻塞型通气功能障碍
小气道功能异常
操作者签字：
医生签字：
2026-08-10 11:19:32,362 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 11:19:32,363 INFO     29 [Trace] task=e139f7cc | doc=LHYA-哮喘-沈阳医大四.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "7 items, types={'OutpatientRecord': 3, 'MedicationRecord': 2, 'ExaminationReport': 2}", "name": "LHYA-哮喘-沈阳医大四.pdf", "embedding_token_consumption": 2613}
2026-08-10 11:19:32,363 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 11:19:32,525 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 11:19:32,525 INFO     29 [Trace] task=e139f7cc | doc=LHYA-哮喘-沈阳医大四.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":7,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 11:19:32,530 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:19:32,530 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:19:32,530 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:19:32,530 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:19:32,530 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:19:32,530 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:19:32,530 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:19:32,538 INFO     29 set_progress(e139f7cc94ac11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 11:19:32 [DOC Engine]:
Start to index...
2026-08-10 11:19:32,555 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.012s]
2026-08-10 11:19:32,559 INFO     29 set_progress(e139f7cc94ac11f1bd9827cf206dfa2d), progress: 0.8142857142857143, progress_msg: 
2026-08-10 11:19:32,595 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.023s]
2026-08-10 11:19:32,610 INFO     29 set_progress(e139f7cc94ac11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 11:19:32 Indexing done (0.07s). Task done (197.51s)
2026-08-10 11:19:32,615 INFO     29 [Done], chunks(7), token(2613), elapsed:197.51
2026-08-10 11:19:32,730 INFO     29 handle_task done for task {"id": "e139f7cc94ac11f1bd9827cf206dfa2d", "doc_id": "e0cfe59494ac11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "type": "pdf", "location": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "size": 4593431, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786360565919, "task_type": "dataflow", "root_trace_id": "a7e430023e6144f7a5a82bee44b10046", "root_traceparent": "00-a7e430023e6144f7a5a82bee44b10046-21836b890cf4bf02-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
