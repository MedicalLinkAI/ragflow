# 基准结果：麦济WZWA222.pdf

## 基本信息

- 文件：`麦济WZWA222.pdf`
- 大小：9514.5 KB
- PDF 总页数：5
- doc_id：`6e14e31c94b911f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T20:45:54  完成时间：2026-08-10T20:48:42  耗时：167.5s
- progress_msg：`12:48:38 Indexing done (0.04s). Task done (153.81s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 308136ab | 1 | 1-1 | 内蒙古医科大学附属医院门诊病历 姓名： 年龄：70岁 诊疗号：002254289 |
| 2 | 66f05004 | 2 | 2-3 | 丰镇市医院 诊断证明书 姓名： 年龄： 性别：男 病案号：10017815 印象 |
| 3 | ac5c956c | 2 | 3-4 | 肺常规通气检查报告 测试号：0022542899 姓名： 出生日期： 身高：16 |
| 4 | c9343d98 | 1 | 4-4 | 舒张试验测试报告 测试号：0022542899 姓名： 出生日期： 身高：cm  |
| 5 | 47af41c3 | 1 | 5-5 | 东吉轩药店 日期: 2026.01.23 09: 23: 37 单号: 2026 |

- chunks 总数：5
- 各 chunk 页数合计（含跨页重复）：7
- 页码并集：`[1, 2, 3, 4, 5]`
- 覆盖页数：5 / 5；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 2 | 0 | 2 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 1 | 1 | 1 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 2 | 2 | 2 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 2, "ExaminationReport": 2, "MedicationRecord": 1}`
- ChunkMerger：`{"found": true, "merged": 5, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 2, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 2, "Extractor:Progress": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 12:48:37,491 INFO     29 [ChunkMerger] Merged 5 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 12:45:57,975 INFO     29 handle_task begin for task {"id": "6e5574f494b911f1bd9827cf206dfa2d", "doc_id": "6e14e31c94b911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWZWA222.pdf", "type": "pdf", "location": "\u9ea6\u6d4eWZWA222.pdf", "size": 9742831, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786365956617, "task_type": "dataflow", "root_trace_id": "bfb2f1d4af5749ba9e8b269686a95a2b", "root_traceparent": "00-bfb2f1d4af5749ba9e8b269686a95a2b-684dd3f6f78a8650-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 12:45:58,170 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 12:45:58,281 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 12:45:58,295 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:45:58,296 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 12:45:58,296 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 12:45:58,301 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 12:45:58,302 INFO     29 ============================================================
2026-08-10 12:45:58,302 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 12:45:58,302 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 12:45:58,302 INFO     29 ============================================================
2026-08-10 12:45:58,302 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 12:45:58,302 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 12:45:58,309 INFO     29 No torch found.
2026-08-10 12:45:59,256 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=5
2026-08-10 12:45:59,874 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5280516, prompt_len=764
2026-08-10 12:46:01,472 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-12-26"}
```
2026-08-10 12:46:01,474 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2025-12-26
2026-08-10 12:46:01,498 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5280516, prompt_len=401
2026-08-10 12:46:06,471 INFO     29 [qwen-vl-parser] text API response (len=842):
["内蒙古医科大学附属医院门诊病历", "姓名：", "年龄：70岁", "诊疗号：0022542899", "民族：汉族", "性别：男性", "科室：呼吸内科门诊", "联系电话：", "身份：", "4", "病情：", "就诊状态：", "就诊时间：2025-12-26 08:41", "生命体征（需要时）：", "体温：℃ 脉搏：74次/分 呼吸：次/分 血压：/mmHg", "主诉：气短10余年，加重伴咳嗽咳痰1月", "现病史：气短10余年，规律用药（信必可都保320，早晚各一吸），加重伴咳", "嗽咳痰1月，血氧饱和度97%。自己输液治疗（含激素）10余天，气", "短、咳嗽咳痰症状无改善。", "既往史：患者平素身体一般，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "有，10年，吸烟史无，无过敏史。", "体格检查：发育正常，营养中等，体型正力，双肺呼吸音弱，双肺未闻及啰", "音，双下肢无水肿，体重kg：", "辅助检查：肺功能：FVC 74%，FEV1 56.3%，FEV1/FVC 58.6%，舒张试验阳性。", "过敏史：", "初步诊断（西医）：1.支气管哮喘（急性发作期）", "初步诊断（中医）：", "治疗方案：1.胸部CT、血常规、肺功能、心电图；2.建议心内科就诊。", "CT胸部", "常规心电图检查", "血常规", "肾功3项", "肝功9项", "肺通气功能检查(肺功能)", "肺容积检查(肺功能)", "肺弥散功能检查(肺功能) 一次性肺功能仪用过滤嘴", "肺通气功能检查(肺功能) 一次性肺功能仪用过滤嘴", "布地奈德福莫特罗吸入粉雾剂(11)《每支60", "吸，每吸含布地奈德320μg和富马酸福莫特", "罗9.0μg>", "用量：1.000吸/次", "用法：吸入，二次/日，1天", "醋酸泼尼松片<5mg>", "用量：2.000片/次", "用法：口服，一次/日，7天", "签名：王美玲"]
2026-08-10 12:46:06,472 INFO     29 [qwen-vl-parser] page=1 text: 46 lines (bbox 0-45)
2026-08-10 12:46:06,472 INFO     29 [qwen-vl-parser] page=1 text: 46 sections
2026-08-10 12:46:06,612 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=572019, prompt_len=764
2026-08-10 12:46:08,048 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-07-22"}
```
2026-08-10 12:46:08,048 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=2024-07-22
2026-08-10 12:46:08,055 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=572019, prompt_len=401
2026-08-10 12:46:09,446 INFO     29 [qwen-vl-parser] text API response (len=133):
["丰镇市医院", "诊断证明书", "姓名：", "年龄：", "性别：男", "病案号：10017815", "印象：1.慢性支气管炎急性加重期2.支气管哮喘3.慢性胃炎4.肺气肿", "处理意见：住院", "医师：宋志杰", "日期：2024年07月22日"]
2026-08-10 12:46:09,447 INFO     29 [qwen-vl-parser] page=2 text: 10 lines (bbox 46-55)
2026-08-10 12:46:09,447 INFO     29 [qwen-vl-parser] page=2 text: 10 sections
2026-08-10 12:46:09,842 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2180949, prompt_len=764
2026-08-10 12:46:09,988 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:46:09.987+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 32, "failed": 0, "current": {"6e5574f494b911f1bd9827cf206dfa2d": {"id": "6e5574f494b911f1bd9827cf206dfa2d", "doc_id": "6e14e31c94b911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWZWA222.pdf", "type": "pdf", "location": "\u9ea6\u6d4eWZWA222.pdf", "size": 9742831, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786365956617, "task_type": "dataflow", "root_trace_id": "bfb2f1d4af5749ba9e8b269686a95a2b", "root_traceparent": "00-bfb2f1d4af5749ba9e8b269686a95a2b-684dd3f6f78a8650-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:46:11,387 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-12-26"}
```
2026-08-10 12:46:11,388 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=2025-12-26
2026-08-10 12:46:11,415 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2180949, prompt_len=401
2026-08-10 12:46:18,084 INFO     29 [qwen-vl-parser] text API response (len=1434):
["地址：呼和浩特市通道北街一号", "电话：0471--3451056", "肺常规通气检查报告", "测试号：0022542899", "姓名：", "出生日期：", "身高：165 cm", "临床印象：支气管哮喘", "住址：内蒙古自治区乌兰察布", "科别：", "住院号：0022542899", "性别：男", "年龄：70 Years", "体重：47 kg", "吸烟史：否", "联系电话：", "主管医生：", "F/V ex", "F/V in", "Vol [L]", "Vol%VCmax", "VCmax", "Time [s]", "Vol [L]", "Time [s]", "FVC", "[L]", "3.34", "2.48", "74.0", "FEV 1", "[L]", "2.58", "1.45", "56.3", "FEV 2", "[L]", "1.82", "FEV 3", "[L]", "2.06", "FEV6", "[L]", "2.45", "FEV 1 % FVC", "[%]", "83.77", "58.60", "70.0", "FEV 1 % VC MAX", "[%]", "74.61", "58.60", "78.5", "PEF", "[L/s]", "7.27", "5.34", "73.4", "MEF 75", "[L/s]", "6.51", "1.94", "29.8", "MEF 50", "[L/s]", "3.73", "0.72", "19.4", "MEF 25", "[L/s]", "1.15", "0.25", "21.9", "MMEF 75/25", "[L/s]", "2.89", "0.60", "20.9", "FET", "[s]", "7.16", "FET PEF", "[s]", "0.05", "V backextrapolation ex", "[L]", "0.07", "V backextrapol. % FVC", "[%]", "2.82", "MVV", "[L/min]", "101.83", "37.40", "36.7", "FEV 1 % VC MAX", "[%]", "74.61", "58.60", "78.5", "VC EX", "[L]", "3.46", "2.48", "71.6", "FRV", "[L]", "0.93", "IRV", "[L]", "0.80", "VT", "[L]", "0.34", "1.65", "491.4", "IC", "[L]", "2.53", "2.45", "96.9", "BF", "[1/min]", "20.00", "13.38", "66.9", "MV", "[L/min]", "6.71", "22.08", "328.9", "VC MAX", "[L]", "3.46", "2.48", "71.6", "Pred", "TEST1", "%/Pred", "TEST2", "%/Pred", "TEST3", "%/Pred", "Date", "25/12/26", "Time", "9:49:52", "结论：", "1. 中重度混合性肺通气功能障碍。", "轻度弥散功能障碍", "操作员：刘角玲"]
2026-08-10 12:46:18,084 INFO     29 [qwen-vl-parser] page=3 text: 152 lines (bbox 56-207)
2026-08-10 12:46:18,084 INFO     29 [qwen-vl-parser] page=3 text: 152 sections
2026-08-10 12:46:18,556 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2753800, prompt_len=764
2026-08-10 12:46:21,563 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-12-26"
}
```
2026-08-10 12:46:21,564 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=2025-12-26
2026-08-10 12:46:21,572 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2753800, prompt_len=401
2026-08-10 12:46:29,052 INFO     29 [qwen-vl-parser] text API response (len=1207):
["内蒙古医科大学附属医院肺功能报告单", "地址：呼和浩特市通道北街一号", "电话：0471--3451056", "舒张试验测试报告", "测试号：0022542899", "姓名：", "出生日期：", "身高：cm", "临床印象：支气管哮喘", "住址：内蒙古自治区乌兰察布", "科别：", "住院号：0022542899", "性别：男", "年龄：70 Years", "体重：47 kg", "吸烟史：否", "联系电话：", "主管医生：", "预计值 药前 %预计 药后1 改善率% 药后2 改善率% 药后3 改善率%", "FVC [L] 3.34 2.48 74.0 2.47 -0.28 2.52 1.90 2.59 4.57", "FEV 1 [L] 2.58 1.45 56.3 1.57 7.98 1.62 11.38 1.68 15.64", "FEV 1 % FVC [%] 83.77 58.60 70.0 63.46 8.29 64.05 9.30 64.81 10.59", "PEF [L/s] 7.27 5.34 73.4 5.97 11.92 6.55 22.75 6.30 18.12", "MEF 75 [L/s] 6.51 1.94 29.8 1.93 -0.49 2.25 15.90 2.48 27.48", "MEF 50 [L/s] 3.73 0.72 19.4 1.08 48.95 1.10 52.54 1.10 52.19", "MEF 25 [L/s] 1.15 0.25 21.9 0.37 49.20 0.35 40.24 0.38 51.20", "MMEF 75/25 [L/s] 2.89 0.60 20.9 0.82 35.86 0.83 37.61 0.89 46.55", "FET [s] 7.16 6.24 -12.85 7.29 1.83 7.07 -1.26", "FET PEF [s] 0.05 0.05 -10.65 0.04 -18.54 0.05 -3.25", "V backextrapol. % FVC [%] 2.82 3.10 10.19 2.50 -11.19 3.24 15.10", "Date 25/12/26 25/12/26 25/12/26 25/12/26", "Time 9:49:52 10:34:27 10:34:52 10:35:14", "结论：", "1. 中重度混合性肺通气功能障碍。", "轻度弥散功能障碍", "2. 支气管舒张试验阳性。", "(通过吸入沙丁胺醇气雾剂400ug，20min后FEV1 / FVC较基线增加大于12%，且绝对值增加大于200ml)。", "操作员：刘冉玲", "测试日期：2025/12/26 测试时间：10:35 编号：4"]
2026-08-10 12:46:29,053 INFO     29 [qwen-vl-parser] page=4 text: 39 lines (bbox 208-246)
2026-08-10 12:46:29,053 INFO     29 [qwen-vl-parser] page=4 text: 39 sections
2026-08-10 12:46:29,404 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1801140, prompt_len=764
2026-08-10 12:46:30,891 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:46:30,891 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 12:46:30,900 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1801140, prompt_len=401
2026-08-10 12:46:32,880 INFO     29 [qwen-vl-parser] text API response (len=263):
["东吉轩药店", "日期: 2026.01.23", "09: 23: 37", "单号: 20260123070132", "品名 规格 单价 数量 总计", "布地奈德福莫特罗吸入气雾剂", "(II)320ug/9ug/吸 60 吸/支", "268.00 2 536.00", "应收金额: 536.00", "实收金额: 536.00", "优惠金额: 0.00", "找零金额: 0.00", "会员:", "日期: 2026.01.23", "09: 23: 3", "单号: 20260123070132"]
2026-08-10 12:46:32,881 INFO     29 [qwen-vl-parser] page=5 text: 16 lines (bbox 247-262)
2026-08-10 12:46:32,881 INFO     29 [qwen-vl-parser] page=5 text: 16 sections
2026-08-10 12:46:32,881 INFO     29 [qwen-vl-parser] parse_pdf done: 263 sections from 5 pages.
2026-08-10 12:46:32,892 INFO     29 Close text detector.
2026-08-10 12:46:33,352 INFO     29 Close text recognizer.
2026-08-10 12:46:33,788 INFO     29 Close recognizer.
2026-08-10 12:46:34,177 INFO     29 Close recognizer.
2026-08-10 12:46:34,609 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 12:46:34,609 INFO     29 [Trace] task=6e5574f4 | doc=麦济WZWA222.pdf | Parser:MedLink | outputs={"html": "", "json": "263 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "json"}
2026-08-10 12:46:34,609 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 12:46:34,630 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:46:34,631 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 内蒙古医科大学附属医院门诊病历\n[BBOX-1] 姓名：\n[BBOX-2] 年龄：70岁\n[BBOX-3] 诊疗号：0022542899\n[BBOX-4] 民族：汉族\n[BBOX-5] 性别：男性\n[BBOX-6] 科室：呼吸内科门诊\n[BBOX-7] 联系电话：\n[BBOX-8] 身份：\n[BBOX-9] 4\n[BBOX-10] 病情：\n[BBOX-11] 就诊状态：\n[BBOX-12] 就诊时间：2025-12-26 08:41\n[BBOX-13] 生命体征（需要时）：\n[BBOX-14] 体温：℃ 脉搏：74次/分 呼吸：次/分 血压：/mmHg\n[BBOX-15] 主诉：气短10余年，加重伴咳嗽咳痰1月\n[BBOX-16] 现病史：气短10余年，规律用药（信必可都保320，早晚各一吸），加重伴咳\n[BBOX-17] 嗽咳痰1月，血氧饱和度97%。自己输液治疗（含激素）10余天，气\n[BBOX-18] 短、咳嗽咳痰症状无改善。\n[BBOX-19] 既往史：患者平素身体一般，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎\n[BBOX-20] 有，10年，吸烟史无，无过敏史。\n[BBOX-21] 体格检查：发育正常，营养中等，体型正力，双肺呼吸音弱，双肺未闻及啰\n[BBOX-22] 音，双下肢无水肿，体重kg：\n[BBOX-23] 辅助检查：肺功能：FVC 74%，FEV1 56.3%，FEV1/FVC 58.6%，舒张试验阳性。\n[BBOX-24] 过敏史：\n[BBOX-25] 初步诊断（西医）：1.支气管哮喘（急性发作期）\n[BBOX-26] 初步诊断（中医）：\n[BBOX-27] 治疗方案：1.胸部CT、血常规、肺功能、心电图；2.建议心内科就诊。\n[BBOX-28] CT胸部\n[BBOX-29] 常规心电图检查\n[BBOX-30] 血常规\n[BBOX-31] 肾功3项\n[BBOX-32] 肝功9项\n[BBOX-33] 肺通气功能检查(肺功能)\n[BBOX-34] 肺容积检查(肺功能)\n[BBOX-35] 肺弥散功能检查(肺功能) 一次性肺功能仪用过滤嘴\n[BBOX-36] 肺通气功能检查(肺功能) 一次性肺功能仪用过滤嘴\n[BBOX-37] 布地奈德福莫特罗吸入粉雾剂(11)《每支60\n[BBOX-38] 吸，每吸含布地奈德320μg和富马酸福莫特\n[BBOX-39] 罗9.0μg>\n[BBOX-40] 用量：1.000吸/次\n[BBOX-41] 用法：吸入，二次/日，1天\n[BBOX-42] 醋酸泼尼松片<5mg>\n[BBOX-43] 用量：2.000片/次\n[BBOX-44] 用法：口服，一次/日，7天\n[BBOX-45] 签名：王美玲\n[BBOX-46] 丰镇市医院\n[BBOX-47] 诊断证明书\n[BBOX-48] 姓名：\n[BBOX-49] 年龄：\n[BBOX-50] 性别：男\n[BBOX-51] 病案号：10017815\n[BBOX-52] 印象：1.慢性支气管炎急性加重期2.支气管哮喘3.慢性胃炎4.肺气肿\n[BBOX-53] 处理意见：住院\n[BBOX-54] 医师：宋志杰\n[BBOX-55] 日期：2024年07月22日\n[BBOX-56] 地址：呼和浩特市通道北街一号\n[BBOX-57] 电话：0471--3451056\n[BBOX-58] 肺常规通气检查报告\n[BBOX-59] 测试号：0022542899\n[BBOX-60] 姓名：\n[BBOX-61] 出生日期：\n[BBOX-62] 身高：165 cm\n[BBOX-63] 临床印象：支气管哮喘\n[BBOX-64] 住址：内蒙古自治区乌兰察布\n[BBOX-65] 科别：\n[BBOX-66] 住院号：0022542899\n[BBOX-67] 性别：男\n[BBOX-68] 年龄：70 Years\n[BBOX-69] 体重：47 kg\n[BBOX-70] 吸烟史：否\n[BBOX-71] 联系电话：\n[BBOX-72] 主管医生：\n[BBOX-73] F/V ex\n[BBOX-74] F/V in\n[BBOX-75] Vol [L]\n[BBOX-76] Vol%VCmax\n[BBOX-77] VCmax\n[BBOX-78] Time [s]\n[BBOX-79] Vol [L]\n[BBOX-80] Time [s]\n[BBOX-81] FVC\n[BBOX-82] [L]\n[BBOX-83] 3.34\n[BBOX-84] 2.48\n[BBOX-85] 74.0\n[BBOX-86] FEV 1\n[BBOX-87] [L]\n[BBOX-88] 2.58\n[BBOX-89] 1.45\n[BBOX-90] 56.3\n[BBOX-91] FEV 2\n[BBOX-92] [L]\n[BBOX-93] 1.82\n[BBOX-94] FEV 3\n[BBOX-95] [L]\n[BBOX-96] 2.06\n[BBOX-97] FEV6\n[BBOX-98] [L]\n[BBOX-99] 2.45\n[BBOX-100] FEV 1 % FVC\n[BBOX-101] [%]\n[BBOX-102] 83.77\n[BBOX-103] 58.60\n[BBOX-104] 70.0\n[BBOX-105] FEV 1 % VC MAX\n[BBOX-106] [%]\n[BBOX-107] 74.61\n[BBOX-108] 58.60\n[BBOX-109] 78.5\n[BBOX-110] PEF\n[BBOX-111] [L/s]\n[BBOX-112] 7.27\n[BBOX-113] 5.34\n[BBOX-114] 73.4\n[BBOX-115] MEF 75\n[BBOX-116] [L/s]\n[BBOX-117] 6.51\n[BBOX-118] 1.94\n[BBOX-119] 29.8\n[BBOX-120] MEF 50\n[BBOX-121] [L/s]\n[BBOX-122] 3.73\n[BBOX-123] 0.72\n[BBOX-124] 19.4\n[BBOX-125] MEF 25\n[BBOX-126] [L/s]\n[BBOX-127] 1.15\n[BBOX-128] 0.25\n[BBOX-129] 21.9\n[BBOX-130] MMEF 75/25\n[BBOX-131] [L/s]\n[BBOX-132] 2.89\n[BBOX-133] 0.60\n[BBOX-134] 20.9\n[BBOX-135] FET\n[BBOX-136] [s]\n[BBOX-137] 7.16\n[BBOX-138] FET PEF\n[BBOX-139] [s]\n[BBOX-140] 0.05\n[BBOX-141] V backextrapolation ex\n[BBOX-142] [L]\n[BBOX-143] 0.07\n[BBOX-144] V backextrapol. % FVC\n[BBOX-145] [%]\n[BBOX-146] 2.82\n[BBOX-147] MVV\n[BBOX-148] [L/min]\n[BBOX-149] 101.83\n[BBOX-150] 37.40\n[BBOX-151] 36.7\n[BBOX-152] FEV 1 % VC MAX\n[BBOX-153] [%]\n[BBOX-154] 74.61\n[BBOX-155] 58.60\n[BBOX-156] 78.5\n[BBOX-157] VC EX\n[BBOX-158] [L]\n[BBOX-159] 3.46\n[BBOX-160] 2.48\n[BBOX-161] 71.6\n[BBOX-162] FRV\n[BBOX-163] [L]\n[BBOX-164] 0.93\n[BBOX-165] IRV\n[BBOX-166] [L]\n[BBOX-167] 0.80\n[BBOX-168] VT\n[BBOX-169] [L]\n[BBOX-170] 0.34\n[BBOX-171] 1.65\n[BBOX-172] 491.4\n[BBOX-173] IC\n[BBOX-174] [L]\n[BBOX-175] 2.53\n[BBOX-176] 2.45\n[BBOX-177] 96.9\n[BBOX-178] BF\n[BBOX-179] [1/min]\n[BBOX-180] 20.00\n[BBOX-181] 13.38\n[BBOX-182] 66.9\n[BBOX-183] MV\n[BBOX-184] [L/min]\n[BBOX-185] 6.71\n[BBOX-186] 22.08\n[BBOX-187] 328.9\n[BBOX-188] VC MAX\n[BBOX-189] [L]\n[BBOX-190] 3.46\n[BBOX-191] 2.48\n[BBOX-192] 71.6\n[BBOX-193] Pred\n[BBOX-194] TEST1\n[BBOX-195] %/Pred\n[BBOX-196] TEST2\n[BBOX-197] %/Pred\n[BBOX-198] TEST3\n[BBOX-199] %/Pred\n[BBOX-200] Date\n[BBOX-201] 25/12/26\n[BBOX-202] Time\n[BBOX-203] 9:49:52\n[BBOX-204] 结论：\n[BBOX-205] 1. 中重度混合性肺通气功能障碍。\n[BBOX-206] 轻度弥散功能障碍\n[BBOX-207] 操作员：刘角玲\n[BBOX-208] 内蒙古医科大学附属医院肺功能报告单\n[BBOX-209] 地址：呼和浩特市通道北街一号\n[BBOX-210] 电话：0471--3451056\n[BBOX-211] 舒张试验测试报告\n[BBOX-212] 测试号：0022542899\n[BBOX-213] 姓名：\n[BBOX-214] 出生日期：\n[BBOX-215] 身高：cm\n[BBOX-216] 临床印象：支气管哮喘\n[BBOX-217] 住址：内蒙古自治区乌兰察布\n[BBOX-218] 科别：\n[BBOX-219] 住院号：0022542899\n[BBOX-220] 性别：男\n[BBOX-221] 年龄：70 Years\n[BBOX-222] 体重：47 kg\n[BBOX-223] 吸烟史：否\n[BBOX-224] 联系电话：\n[BBOX-225] 主管医生：\n[BBOX-226] 预计值 药前 %预计 药后1 改善率% 药后2 改善率% 药后3 改善率%\n[BBOX-227] FVC [L] 3.34 2.48 74.0 2.47 -0.28 2.52 1.90 2.59 4.57\n[BBOX-228] FEV 1 [L] 2.58 1.45 56.3 1.57 7.98 1.62 11.38 1.68 15.64\n[BBOX-229] FEV 1 % FVC [%] 83.77 58.60 70.0 63.46 8.29 64.05 9.30 64.81 10.59\n[BBOX-230] PEF [L/s] 7.27 5.34 73.4 5.97 11.92 6.55 22.75 6.30 18.12\n[BBOX-231] MEF 75 [L/s] 6.51 1.94 29.8 1.93 -0.49 2.25 15.90 2.48 27.48\n[BBOX-232] MEF 50 [L/s] 3.73 0.72 19.4 1.08 48.95 1.10 52.54 1.10 52.19\n[BBOX-233] MEF 25 [L/s] 1.15 0.25 21.9 0.37 49.20 0.35 40.24 0.38 51.20\n[BBOX-234] MMEF 75/25 [L/s] 2.89 0.60 20.9 0.82 35.86 0.83 37.61 0.89 46.55\n[BBOX-235] FET [s] 7.16 6.24 -12.85 7.29 1.83 7.07 -1.26\n[BBOX-236] FET PEF [s] 0.05 0.05 -10.65 0.04 -18.54 0.05 -3.25\n[BBOX-237] V backextrapol. % FVC [%] 2.82 3.10 10.19 2.50 -11.19 3.24 15.10\n[BBOX-238] Date 25/12/26 25/12/26 25/12/26 25/12/26\n[BBOX-239] Time 9:49:52 10:34:27 10:34:52 10:35:14\n[BBOX-240] 结论：\n[BBOX-241] 1. 中重度混合性肺通气功能障碍。\n[BBOX-242] 轻度弥散功能障碍\n[BBOX-243] 2. 支气管舒张试验阳性。\n[BBOX-244] (通过吸入沙丁胺醇气雾剂400ug，20min后FEV1 / FVC较基线增加大于12%，且绝对值增加大于200ml)。\n[BBOX-245] 操作员：刘冉玲\n[BBOX-246] 测试日期：2025/12/26 测试时间：10:35 编号：4\n[BBOX-247] 东吉轩药店\n[BBOX-248] 日期: 2026.01.23\n[BBOX-249] 09: 23: 37\n[BBOX-250] 单号: 20260123070132\n[BBOX-251] 品名 规格 单价 数量 总计\n[BBOX-252] 布地奈德福莫特罗吸入气雾剂\n[BBOX-253] (II)320ug/9ug/吸 60 吸/支\n[BBOX-254] 268.00 2 536.00\n[BBOX-255] 应收金额: 536.00\n[BBOX-256] 实收金额: 536.00\n[BBOX-257] 优惠金额: 0.00\n[BBOX-258] 找零金额: 0.00\n[BBOX-259] 会员:\n[BBOX-260] 日期: 2026.01.23\n[BBOX-261] 09: 23: 3\n[BBOX-262] 单号: 20260123070132"
  }
]
2026-08-10 12:46:40,493 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:46:40,507 INFO     29 [SmartSplitter] SmartSplitter done: 5 chunks from 5 LLM segments (all bbox_id). Types: {'OutpatientRecord': 2, 'ExaminationReport': 2, 'MedicationRecord': 1}
2026-08-10 12:46:40,515 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 12:46:40,515 INFO     29 [Trace] task=6e5574f4 | doc=麦济WZWA222.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "263 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "chunks", "chunks": "5 items, types={'OutpatientRecord': 2, 'ExaminationReport': 2, 'MedicationRecord': 1}"}
2026-08-10 12:46:40,515 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 12:46:40,516 INFO     29 [ChunkRouter] Routed 5 chunks into 3 groups: {'chunks_Clinical': 2, 'chunks_Examination': 2, 'chunks_Medication': 1}
2026-08-10 12:46:40,524 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 12:46:40,524 INFO     29 [Trace] task=6e5574f4 | doc=麦济WZWA222.pdf | ChunkRouter:Router | outputs={"html": "", "json": "263 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "chunks", "chunks": "5 items, types={'OutpatientRecord': 2, 'ExaminationReport': 2, 'MedicationRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_Medication\": 1}"}
2026-08-10 12:46:40,524 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 12:46:40,529 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:46:40,529 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:46:41,230 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:46:41,242 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 12:46:41,242 INFO     29 [Trace] task=6e5574f4 | doc=麦济WZWA222.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "263 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_Medication\": 1}"}
2026-08-10 12:46:41,242 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 12:46:41,252 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:46:41,252 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:46:41,306 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:46:41.305+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 32, "failed": 0, "current": {"6e5574f494b911f1bd9827cf206dfa2d": {"id": "6e5574f494b911f1bd9827cf206dfa2d", "doc_id": "6e14e31c94b911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWZWA222.pdf", "type": "pdf", "location": "\u9ea6\u6d4eWZWA222.pdf", "size": 9742831, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786365956617, "task_type": "dataflow", "root_trace_id": "bfb2f1d4af5749ba9e8b269686a95a2b", "root_traceparent": "00-bfb2f1d4af5749ba9e8b269686a95a2b-684dd3f6f78a8650-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:46:41,706 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:46:41,712 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 12:46:41,713 INFO     29 [Trace] task=6e5574f4 | doc=麦济WZWA222.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "263 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_Medication\": 1}"}
2026-08-10 12:46:41,713 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 12:46:41,717 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:46:41,718 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:46:41,718 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 12:46:41,718 INFO     29 [qwen-vl-text] positions(46): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:46:41,718 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [46]
2026-08-10 12:46:42,168 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:46:42,169 INFO     29 [qwen-vl-text] LLM extraction start, text_len=703
2026-08-10 12:46:42,169 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:46:42,170 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 45, \"encounter_dates\": [\"2025-12-26\"], \"department\": \"呼吸内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "内蒙古医科大学附属医院门诊病历\n姓名：\n年龄：70岁\n诊疗号：0022542899\n民族：汉族\n性别：男性\n科室：呼吸内科门诊\n联系电话：\n身份：\n4\n病情：\n就诊状态：\n就诊时间：2025-12-26 08:41\n生命体征（需要时）：\n体温：℃ 脉搏：74次/分 呼吸：次/分 血压：/mmHg\n主诉：气短10余年，加重伴咳嗽咳痰1月\n现病史：气短10余年，规律用药（信必可都保320，早晚各一吸），加重伴咳\n嗽咳痰1月，血氧饱和度97%。自己输液治疗（含激素）10余天，气\n短、咳嗽咳痰症状无改善。\n既往史：患者平素身体一般，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎\n有，10年，吸烟史无，无过敏史。\n体格检查：发育正常，营养中等，体型正力，双肺呼吸音弱，双肺未闻及啰\n音，双下肢无水肿，体重kg：\n辅助检查：肺功能：FVC 74%，FEV1 56.3%，FEV1/FVC 58.6%，舒张试验阳性。\n过敏史：\n初步诊断（西医）：1.支气管哮喘（急性发作期）\n初步诊断（中医）：\n治疗方案：1.胸部CT、血常规、肺功能、心电图；2.建议心内科就诊。\nCT胸部\n常规心电图检查\n血常规\n肾功3项\n肝功9项\n肺通气功能检查(肺功能)\n肺容积检查(肺功能)\n肺弥散功能检查(肺功能) 一次性肺功能仪用过滤嘴\n肺通气功能检查(肺功能) 一次性肺功能仪用过滤嘴\n布地奈德福莫特罗吸入粉雾剂(11)《每支60\n吸，每吸含布地奈德320μg和富马酸福莫特\n罗9.0μg>\n用量：1.000吸/次\n用法：吸入，二次/日，1天\n醋酸泼尼松片<5mg>\n用量：2.000片/次\n用法：口服，一次/日，7天\n签名：王美玲",
    "role": "user"
  }
]
2026-08-10 12:46:44,981 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:46:44,981 INFO     29 [qwen-vl-text] LLM output (len=423):
{
  "encounter_date": "2025-12-26",
  "chief_complaint": "气短10余年，加重伴咳嗽咳痰1月",
  "present_illness": "气短10余年，规律用药（信必可都保320，早晚各一吸），加重伴咳嗽咳痰1月，血氧饱和度97%。自己输液治疗（含激素）10余天，气短、咳嗽咳痰症状无改善。",
  "past_history": "患者平素身体一般，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎有，10年，吸烟史无，无过敏史。",
  "diagnosis": "1.支气管哮喘（急性发作期）",
  "treatment_plan": [
    "布地奈德福莫特罗吸入粉雾剂(11)《每支60吸，每吸含布地奈德320μg和富马酸福莫特罗9.0μg> 1.000吸/次 吸入，二次/日，1天",
    "醋酸泼尼松片<5mg> 2.000片/次 口服，一次/日，7天"
  ]
}
2026-08-10 12:46:44,981 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-26]
2026-08-10 12:46:44,999 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8011001, prompt_len=1454
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共46行）
["内蒙古医科大学附属医院门诊病历", "姓名：", "年龄：70岁", "诊疗号：0022542899", "民族：汉族", "性别：男性", "科室：呼吸内科门诊", "联系电话：", "身份：", "4", "病情：", "就诊状态：", "就诊时间：2025-12-26 08:41", "生命体征（需要时）：", "体温：℃ 脉搏：74次/分 呼吸：次/分 血压：/mmHg", "主诉：气短10余年，加重伴咳嗽咳痰1月", "现病史：气短10余年，规律用药（信必可都保320，早晚各一吸），加重伴咳", "嗽咳痰1月，血氧饱和度97%。自己输液治疗（含激素）10余天，气", "短、咳嗽咳痰症状无改善。", "既往史：患者平素身体一般，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "有，10年，吸烟史无，无过敏史。", "体格检查：发育正常，营养中等，体型正力，双肺呼吸音弱，双肺未闻及啰", "音，双下肢无水肿，体重kg：", "辅助检查：肺功能：FVC 74%，FEV1 56.3%，FEV1/FVC 58.6%，舒张试验阳性。", "过敏史：", "初步诊断（西医）：1.支气管哮喘（急性发作期）", "初步诊断（中医）：", "治疗方案：1.胸部CT、血常规、肺功能、心电图；2.建议心内科就诊。", "CT胸部", "常规心电图检查", "血常规", "肾功3项", "肝功9项", "肺通气功能检查(肺功能)", "肺容积检查(肺功能)", "肺弥散功能检查(肺功能) 一次性肺功能仪用过滤嘴", "肺通气功能检查(肺功能) 一次性肺功能仪用过滤嘴", "布地奈德福莫特罗吸入粉雾剂(11)《每支60", "吸，每吸含布地奈德320μg和富马酸福莫特", "罗9.0μg>", "用量：1.000吸/次", "用法：吸入，二次/日，1天", "醋酸泼尼松片<5mg>", "用量：2.000片/次", "用法：口服，一次/日，7天", "签名：王美玲"]

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
2026-08-10 12:47:01,410 INFO     29 [qwen-vl-text] coord API raw response (len=2705):
[
	{"text": "内蒙古医科大学附属医院门诊病历", "bbox": [228, 60, 770, 87]},
	{"text": "姓名：", "bbox": [64, 105, 125, 122]},
	{"text": "年龄：70岁", "bbox": [323, 105, 453, 123]},
	{"text": "诊疗号：0022542899", "bbox": [580, 106, 805, 124]},
	{"text": "民族：汉族", "bbox": [67, 139, 195, 156]},
	{"text": "性别：男性", "bbox": [323, 139, 454, 157]},
	{"text": "科室：呼吸内科门诊", "bbox": [580, 140, 809, 158]},
	{"text": "联系电话：", "bbox": [65, 172, 174, 190]},
	{"text": "身份：", "bbox": [373, 172, 428, 190]},
	{"text": "4", "bbox": [682, 174, 698, 189]},
	{"text": "病情：", "bbox": [750, 174, 807, 191]},
	{"text": "就诊状态：", "bbox": [65, 206, 174, 224]},
	{"text": "就诊时间：2025-12-26 08:41", "bbox": [309, 206, 644, 224]},
	{"text": "生命体征（需要时）：", "bbox": [67, 233, 300, 251]},
	{"text": "体温：℃ 脉搏：74次/分 呼吸：次/分 血压：/mmHg", "bbox": [65, 256, 593, 275]},
	{"text": "主诉：气短10余年，加重伴咳嗽咳痰1月", "bbox": [65, 280, 534, 300]},
	{"text": "现病史：气短10余年，规律用药（信必可都保320，早晚各一吸），加重伴咳", "bbox": [65, 304, 928, 324]},
	{"text": "嗽咳痰1月，血氧饱和度97%。自己输液治疗（含激素）10余天，气", "bbox": [171, 328, 928, 348]},
	{"text": "短、咳嗽咳痰症状无改善。", "bbox": [171, 352, 462, 371]},
	{"text": "既往史：患者平素身体一般，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "bbox": [65, 376, 928, 395]},
	{"text": "有，10年，吸烟史无，无过敏史。", "bbox": [171, 399, 537, 418]},
	{"text": "体格检查：发育正常，营养中等，体型正力，双肺呼吸音弱，双肺未闻及啰", "bbox": [65, 423, 900, 442]},
	{"text": "音，双下肢无水肿，体重kg：", "bbox": [200, 446, 512, 465]},
	{"text": "辅助检查：肺功能：FVC 74%，FEV1 56.3%，FEV1/FVC 58.6%，舒张试验阳性。", "bbox": [65, 469, 887, 489]},
	{"text": "过敏史：", "bbox": [65, 494, 149, 512]},
	{"text": "初步诊断（西医）：1.支气管哮喘（急性发作期）", "bbox": [65, 517, 592, 537]},
	{"text": "初步诊断（中医）：", "bbox": [65, 541, 254, 560]},
	{"text": "治疗方案：1.胸部CT、血常规、肺功能、心电图；2.建议心内科就诊。", "bbox": [65, 565, 810, 584]},
	{"text": "CT胸部", "bbox": [67, 607, 142, 624]},
	{"text": "常规心电图检查", "bbox": [359, 607, 531, 624]},
	{"text": "血常规", "bbox": [647, 607, 718, 624]},
	{"text": "肾功3项", "bbox": [70, 629, 153, 647]},
	{"text": "肝功9项", "bbox": [359, 629, 442, 647]},
	{"text": "肺通气功能检查(肺功能)", "bbox": [647, 627, 913, 646]},
	{"text": "肺容积检查(肺功能)", "bbox": [69, 652, 288, 670]},
	{"text": "肺弥散功能检查(肺功能) 一次性肺功能仪用过滤嘴", "bbox": [359, 652, 915, 670]},
	{"text": "肺通气功能检查(肺功能) 一次性肺功能仪用过滤嘴", "bbox": [69, 674, 629, 692]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(11)《每支60", "bbox": [67, 694, 531, 712]},
	{"text": "吸，每吸含布地奈德320μg和富马酸福莫特", "bbox": [67, 714, 529, 732]},
	{"text": "罗9.0μg>", "bbox": [69, 734, 177, 752]},
	{"text": "用量：1.000吸/次", "bbox": [584, 692, 764, 710]},
	{"text": "用法：吸入，二次/日，1天", "bbox": [117, 752, 404, 771]},
	{"text": "醋酸泼尼松片<5mg>", "bbox": [65, 776, 277, 794]},
	{"text": "用量：2.000片/次", "bbox": [584, 773, 764, 791]},
	{"text": "用法：口服，一次/日，7天", "bbox": [117, 794, 404, 813]},
	{"text": "签名：王美玲", "bbox": [545, 888, 740, 922]}
]
2026-08-10 12:47:01,411 INFO     29 [qwen-vl-text] coord API: raw_items=46, valid_items=46, elapsed=16.4s
2026-08-10 12:47:01,411 INFO     29 [qwen-vl-text] coord item[0]: text=内蒙古医科大学附属医院门诊病历, bbox=[228, 60, 770, 87]
2026-08-10 12:47:01,411 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[64, 105, 125, 122]
2026-08-10 12:47:01,411 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：70岁, bbox=[323, 105, 453, 123]
2026-08-10 12:47:01,411 INFO     29 [qwen-vl-text] coord item[3]: text=诊疗号：0022542899, bbox=[580, 106, 805, 124]
2026-08-10 12:47:01,411 INFO     29 [qwen-vl-text] coord item[4]: text=民族：汉族, bbox=[67, 139, 195, 156]
2026-08-10 12:47:01,411 INFO     29 [qwen-vl-text] coord item[5]: text=性别：男性, bbox=[323, 139, 454, 157]
2026-08-10 12:47:01,411 INFO     29 [qwen-vl-text] coord item[6]: text=科室：呼吸内科门诊, bbox=[580, 140, 809, 158]
2026-08-10 12:47:01,411 INFO     29 [qwen-vl-text] coord item[7]: text=联系电话：, bbox=[65, 172, 174, 190]
2026-08-10 12:47:01,411 INFO     29 [qwen-vl-text] coord item[8]: text=身份：, bbox=[373, 172, 428, 190]
2026-08-10 12:47:01,411 INFO     29 [qwen-vl-text] coord item[9]: text=4, bbox=[682, 174, 698, 189]
2026-08-10 12:47:01,411 INFO     29 [qwen-vl-text] coord item[10]: text=病情：, bbox=[750, 174, 807, 191]
2026-08-10 12:47:01,411 INFO     29 [qwen-vl-text] coord item[11]: text=就诊状态：, bbox=[65, 206, 174, 224]
2026-08-10 12:47:01,411 INFO     29 [qwen-vl-text] coord item[12]: text=就诊时间：2025-12-26 08:41, bbox=[309, 206, 644, 224]
2026-08-10 12:47:01,411 INFO     29 [qwen-vl-text] coord item[13]: text=生命体征（需要时）：, bbox=[67, 233, 300, 251]
2026-08-10 12:47:01,412 INFO     29 [qwen-vl-text] coord item[14]: text=体温：℃ 脉搏：74次/分 呼吸：次/分 血压：/mmHg, bbox=[65, 256, 593, 275]
2026-08-10 12:47:01,412 INFO     29 [qwen-vl-text] coord item[15]: text=主诉：气短10余年，加重伴咳嗽咳痰1月, bbox=[65, 280, 534, 300]
2026-08-10 12:47:01,412 INFO     29 [qwen-vl-text] coord item[16]: text=现病史：气短10余年，规律用药（信必可都保320，早晚各一吸），加重伴咳, bbox=[65, 304, 928, 324]
2026-08-10 12:47:01,412 INFO     29 [qwen-vl-text] coord item[17]: text=嗽咳痰1月，血氧饱和度97%。自己输液治疗（含激素）10余天，气, bbox=[171, 328, 928, 348]
2026-08-10 12:47:01,412 INFO     29 [qwen-vl-text] coord item[18]: text=短、咳嗽咳痰症状无改善。, bbox=[171, 352, 462, 371]
2026-08-10 12:47:01,412 INFO     29 [qwen-vl-text] coord item[19]: text=既往史：患者平素身体一般，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎, bbox=[65, 376, 928, 395]
2026-08-10 12:47:01,412 INFO     29 [qwen-vl-text] coord item[20]: text=有，10年，吸烟史无，无过敏史。, bbox=[171, 399, 537, 418]
2026-08-10 12:47:01,412 INFO     29 [qwen-vl-text] coord item[21]: text=体格检查：发育正常，营养中等，体型正力，双肺呼吸音弱，双肺未闻及啰, bbox=[65, 423, 900, 442]
2026-08-10 12:47:01,412 INFO     29 [qwen-vl-text] coord item[22]: text=音，双下肢无水肿，体重kg：, bbox=[200, 446, 512, 465]
2026-08-10 12:47:01,412 INFO     29 [qwen-vl-text] coord item[23]: text=辅助检查：肺功能：FVC 74%，FEV1 56.3%，FEV1/FVC 58.6%，舒张试验阳性。, bbox=[65, 469, 887, 489]
2026-08-10 12:47:01,412 INFO     29 [qwen-vl-text] coord item[24]: text=过敏史：, bbox=[65, 494, 149, 512]
2026-08-10 12:47:01,412 INFO     29 [qwen-vl-text] coord item[25]: text=初步诊断（西医）：1.支气管哮喘（急性发作期）, bbox=[65, 517, 592, 537]
2026-08-10 12:47:01,412 INFO     29 [qwen-vl-text] coord item[26]: text=初步诊断（中医）：, bbox=[65, 541, 254, 560]
2026-08-10 12:47:01,412 INFO     29 [qwen-vl-text] coord item[27]: text=治疗方案：1.胸部CT、血常规、肺功能、心电图；2.建议心内科就诊。, bbox=[65, 565, 810, 584]
2026-08-10 12:47:01,412 INFO     29 [qwen-vl-text] coord item[28]: text=CT胸部, bbox=[67, 607, 142, 624]
2026-08-10 12:47:01,412 INFO     29 [qwen-vl-text] coord item[29]: text=常规心电图检查, bbox=[359, 607, 531, 624]
2026-08-10 12:47:01,412 INFO     29 [qwen-vl-text] coord item[30]: text=血常规, bbox=[647, 607, 718, 624]
2026-08-10 12:47:01,412 INFO     29 [qwen-vl-text] coord item[31]: text=肾功3项, bbox=[70, 629, 153, 647]
2026-08-10 12:47:01,412 INFO     29 [qwen-vl-text] coord item[32]: text=肝功9项, bbox=[359, 629, 442, 647]
2026-08-10 12:47:01,412 INFO     29 [qwen-vl-text] coord item[33]: text=肺通气功能检查(肺功能), bbox=[647, 627, 913, 646]
2026-08-10 12:47:01,412 INFO     29 [qwen-vl-text] coord item[34]: text=肺容积检查(肺功能), bbox=[69, 652, 288, 670]
2026-08-10 12:47:01,413 INFO     29 [qwen-vl-text] coord item[35]: text=肺弥散功能检查(肺功能) 一次性肺功能仪用过滤嘴, bbox=[359, 652, 915, 670]
2026-08-10 12:47:01,413 INFO     29 [qwen-vl-text] coord item[36]: text=肺通气功能检查(肺功能) 一次性肺功能仪用过滤嘴, bbox=[69, 674, 629, 692]
2026-08-10 12:47:01,413 INFO     29 [qwen-vl-text] coord item[37]: text=布地奈德福莫特罗吸入粉雾剂(11)《每支60, bbox=[67, 694, 531, 712]
2026-08-10 12:47:01,413 INFO     29 [qwen-vl-text] coord item[38]: text=吸，每吸含布地奈德320μg和富马酸福莫特, bbox=[67, 714, 529, 732]
2026-08-10 12:47:01,413 INFO     29 [qwen-vl-text] coord item[39]: text=罗9.0μg>, bbox=[69, 734, 177, 752]
2026-08-10 12:47:01,413 INFO     29 [qwen-vl-text] coord item[40]: text=用量：1.000吸/次, bbox=[584, 692, 764, 710]
2026-08-10 12:47:01,413 INFO     29 [qwen-vl-text] coord item[41]: text=用法：吸入，二次/日，1天, bbox=[117, 752, 404, 771]
2026-08-10 12:47:01,413 INFO     29 [qwen-vl-text] coord item[42]: text=醋酸泼尼松片<5mg>, bbox=[65, 776, 277, 794]
2026-08-10 12:47:01,413 INFO     29 [qwen-vl-text] coord item[43]: text=用量：2.000片/次, bbox=[584, 773, 764, 791]
2026-08-10 12:47:01,413 INFO     29 [qwen-vl-text] coord item[44]: text=用法：口服，一次/日，7天, bbox=[117, 794, 404, 813]
2026-08-10 12:47:01,413 INFO     29 [qwen-vl-text] coord item[45]: text=签名：王美玲, bbox=[545, 888, 740, 922]
2026-08-10 12:47:01,416 INFO     29 [qwen-vl-text] page=0 — 46/46 coords, api_time=16.4s
2026-08-10 12:47:01,416 INFO     29 [qwen-vl-text] new_positions (46):
[[0, 135.66, 458.15, 50.519999999999996, 73.25399999999999], [0, 38.08, 74.375, 88.41, 102.72399999999999], [0, 192.185, 269.53499999999997, 88.41, 103.566], [0, 345.09999999999997, 478.97499999999997, 89.252, 104.408], [0, 39.864999999999995, 116.02499999999999, 117.038, 131.352], [0, 192.185, 270.13, 117.038, 132.194], [0, 345.09999999999997, 481.35499999999996, 117.88, 133.036], [0, 38.675, 103.53, 144.82399999999998, 159.98], [0, 221.935, 254.66, 144.82399999999998, 159.98], [0, 405.78999999999996, 415.31, 146.50799999999998, 159.138], [0, 446.25, 480.16499999999996, 146.50799999999998, 160.822], [0, 38.675, 103.53, 173.452, 188.608], [0, 183.855, 383.18, 173.452, 188.608], [0, 39.864999999999995, 178.5, 196.186, 211.34199999999998], [0, 38.675, 352.835, 215.552, 231.54999999999998], [0, 38.675, 317.72999999999996, 235.76, 252.6], [0, 38.675, 552.16, 255.968, 272.808], [0, 101.74499999999999, 552.16, 276.176, 293.01599999999996], [0, 101.74499999999999, 274.89, 296.384, 312.382], [0, 38.675, 552.16, 316.592, 332.59], [0, 101.74499999999999, 319.515, 335.95799999999997, 351.95599999999996], [0, 38.675, 535.5, 356.166, 372.164], [0, 119.0, 304.64, 375.532, 391.53], [0, 38.675, 527.765, 394.89799999999997, 411.738], [0, 38.675, 88.655, 415.948, 431.104], [0, 38.675, 352.24, 435.31399999999996, 452.154], [0, 38.675, 151.13, 455.522, 471.52], [0, 38.675, 481.95, 475.72999999999996, 491.728], [0, 39.864999999999995, 84.49, 511.094, 525.408], [0, 213.605, 315.945, 511.094, 525.408], [0, 384.965, 427.21, 511.094, 525.408], [0, 41.65, 91.035, 529.6179999999999, 544.774], [0, 213.605, 262.99, 529.6179999999999, 544.774], [0, 384.965, 543.235, 527.934, 543.932], [0, 41.055, 171.35999999999999, 548.984, 564.14], [0, 213.605, 544.425, 548.984, 564.14], [0, 41.055, 374.255, 567.5079999999999, 582.664], [0, 39.864999999999995, 315.945, 584.348, 599.504], [0, 39.864999999999995, 314.755, 601.188, 616.3439999999999], [0, 41.055, 105.315, 618.028, 633.184], [0, 347.47999999999996, 454.58, 582.664, 597.8199999999999], [0, 69.615, 240.38, 633.184, 649.182], [0, 38.675, 164.815, 653.3919999999999, 668.548], [0, 347.47999999999996, 454.58, 650.866, 666.0219999999999], [0, 69.615, 240.38, 668.548, 684.5459999999999], [0, 324.275, 440.29999999999995, 747.696, 776.324]]
2026-08-10 12:47:01,416 INFO     29 [qwen-vl-text] ═══ DONE ═══ 46 positions, pages=1, time=19.7s
2026-08-10 12:47:01,416 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:47:01,418 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:47:01,418 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 12:47:01,418 INFO     29 [qwen-vl-text] positions(12): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:47:01,418 INFO     29 [qwen-vl-text] page grouping: [1, 2], lines per page: [10, 2]
2026-08-10 12:47:01,577 INFO     29 [qwen-vl-text] page=1, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 12:47:01,968 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:47:01,969 INFO     29 [qwen-vl-text] LLM extraction start, text_len=134
2026-08-10 12:47:01,969 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:47:01,969 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 46, \"bbox_end\": 57, \"encounter_dates\": [\"2024-07-22\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "丰镇市医院\n诊断证明书\n姓名：\n年龄：\n性别：男\n病案号：10017815\n印象：1.慢性支气管炎急性加重期2.支气管哮喘3.慢性胃炎4.肺气肿\n处理意见：住院\n医师：宋志杰\n日期：2024年07月22日\n地址：呼和浩特市通道北街一号\n电话：0471--3451056",
    "role": "user"
  }
]
2026-08-10 12:47:03,998 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:47:03,998 INFO     29 [qwen-vl-text] LLM output (len=193):
{
  "encounter_date": "2024-07-22",
  "chief_complaint": null,
  "present_illness": null,
  "past_history": null,
  "diagnosis": "1.慢性支气管炎急性加重期 2.支气管哮喘 3.慢性胃炎 4.肺气肿",
  "treatment_plan": "住院"
}
2026-08-10 12:47:03,998 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-07-22]
2026-08-10 12:47:04,002 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=843191, prompt_len=745
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共10行）
["丰镇市医院", "诊断证明书", "姓名：", "年龄：", "性别：男", "病案号：10017815", "印象：1.慢性支气管炎急性加重期2.支气管哮喘3.慢性胃炎4.肺气肿", "处理意见：住院", "医师：宋志杰", "日期：2024年07月22日"]

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
2026-08-10 12:47:07,944 INFO     29 [qwen-vl-text] coord API raw response (len=545):
[
	{"text": "丰镇市医院", "bbox": [560, 207, 686, 239]},
	{"text": "诊断证明书", "bbox": [533, 252, 707, 295]},
	{"text": "姓名：", "bbox": [164, 302, 219, 327]},
	{"text": "年龄：", "bbox": [164, 337, 219, 362]},
	{"text": "性别：男", "bbox": [740, 304, 825, 327]},
	{"text": "病案号：10017815", "bbox": [740, 335, 869, 357]},
	{"text": "印象：1.慢性支气管炎急性加重期2.支气管哮喘3.慢性胃炎4.肺气肿", "bbox": [165, 365, 731, 396]},
	{"text": "处理意见：住院", "bbox": [165, 402, 307, 429]},
	{"text": "医师：宋志杰", "bbox": [165, 441, 330, 496]},
	{"text": "日期：2024年07月22日", "bbox": [744, 433, 898, 458]}
]
2026-08-10 12:47:07,944 INFO     29 [qwen-vl-text] coord API: raw_items=10, valid_items=10, elapsed=3.9s
2026-08-10 12:47:07,944 INFO     29 [qwen-vl-text] coord item[0]: text=丰镇市医院, bbox=[560, 207, 686, 239]
2026-08-10 12:47:07,944 INFO     29 [qwen-vl-text] coord item[1]: text=诊断证明书, bbox=[533, 252, 707, 295]
2026-08-10 12:47:07,944 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[164, 302, 219, 327]
2026-08-10 12:47:07,945 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：, bbox=[164, 337, 219, 362]
2026-08-10 12:47:07,945 INFO     29 [qwen-vl-text] coord item[4]: text=性别：男, bbox=[740, 304, 825, 327]
2026-08-10 12:47:07,945 INFO     29 [qwen-vl-text] coord item[5]: text=病案号：10017815, bbox=[740, 335, 869, 357]
2026-08-10 12:47:07,945 INFO     29 [qwen-vl-text] coord item[6]: text=印象：1.慢性支气管炎急性加重期2.支气管哮喘3.慢性胃炎4.肺气肿, bbox=[165, 365, 731, 396]
2026-08-10 12:47:07,945 INFO     29 [qwen-vl-text] coord item[7]: text=处理意见：住院, bbox=[165, 402, 307, 429]
2026-08-10 12:47:07,945 INFO     29 [qwen-vl-text] coord item[8]: text=医师：宋志杰, bbox=[165, 441, 330, 496]
2026-08-10 12:47:07,945 INFO     29 [qwen-vl-text] coord item[9]: text=日期：2024年07月22日, bbox=[744, 433, 898, 458]
2026-08-10 12:47:07,945 INFO     29 [qwen-vl-text] page=1 — 10/10 coords, api_time=3.9s
2026-08-10 12:47:07,956 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2828092, prompt_len=649
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共2行）
["地址：呼和浩特市通道北街一号", "电话：0471--3451056"]

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
2026-08-10 12:47:09,940 INFO     29 [qwen-vl-text] coord API raw response (len=131):
```json
[
	{"text": "地址：呼和浩特市通道北街一号", "bbox": [306, 73, 679, 90]},
	{"text": "电话：0471--3451056", "bbox": [367, 90, 622, 107]}
]
```
2026-08-10 12:47:09,940 INFO     29 [qwen-vl-text] coord API: raw_items=2, valid_items=2, elapsed=2.0s
2026-08-10 12:47:09,941 INFO     29 [qwen-vl-text] coord item[0]: text=地址：呼和浩特市通道北街一号, bbox=[306, 73, 679, 90]
2026-08-10 12:47:09,941 INFO     29 [qwen-vl-text] coord item[1]: text=电话：0471--3451056, bbox=[367, 90, 622, 107]
2026-08-10 12:47:09,942 INFO     29 [qwen-vl-text] page=2 — 2/2 coords, api_time=2.0s
2026-08-10 12:47:09,942 INFO     29 [qwen-vl-text] new_positions (12):
[[1, 471.52, 577.612, 123.16499999999999, 142.20499999999998], [1, 448.786, 595.294, 149.94, 175.525], [1, 138.088, 184.398, 179.69, 194.565], [1, 138.088, 184.398, 200.515, 215.39], [1, 623.0799999999999, 694.65, 180.88, 194.565], [1, 623.0799999999999, 731.698, 199.325, 212.415], [1, 138.93, 615.502, 217.17499999999998, 235.61999999999998], [1, 138.93, 258.49399999999997, 239.19, 255.255], [1, 138.93, 277.86, 262.395, 295.12], [1, 626.448, 756.116, 257.635, 272.51], [2, 182.07, 404.005, 61.466, 75.78], [2, 218.36499999999998, 370.09, 75.78, 90.094]]
2026-08-10 12:47:09,943 INFO     29 [qwen-vl-text] ═══ DONE ═══ 12 positions, pages=2, time=8.5s
2026-08-10 12:47:09,956 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 12:47:09,956 INFO     29 [Trace] task=6e5574f4 | doc=麦济WZWA222.pdf | Extractor:Clinical | outputs={"chunks": "2 items, types={'OutpatientRecord': 2}", "html": "", "json": "263 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_Medication\": 1}"}
2026-08-10 12:47:09,956 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 12:47:09,966 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:47:09,967 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:47:09,967 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 12:47:09,967 INFO     29 [qwen-vl-text] positions(16): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:47:09,967 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [16]
2026-08-10 12:47:10,276 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:47:10,278 INFO     29 [qwen-vl-text] LLM extraction start, text_len=214
2026-08-10 12:47:10,278 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:47:10,278 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 247, \"bbox_end\": 262, \"encounter_dates\": [\"2026-01-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "东吉轩药店\n日期: 2026.01.23\n09: 23: 37\n单号: 20260123070132\n品名 规格 单价 数量 总计\n布地奈德福莫特罗吸入气雾剂\n(II)320ug/9ug/吸 60 吸/支\n268.00 2 536.00\n应收金额: 536.00\n实收金额: 536.00\n优惠金额: 0.00\n找零金额: 0.00\n会员:\n日期: 2026.01.23\n09: 23: 3\n单号: 20260123070132",
    "role": "user"
  }
]
2026-08-10 12:47:12,636 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:47:12.633+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 32, "failed": 0, "current": {"6e5574f494b911f1bd9827cf206dfa2d": {"id": "6e5574f494b911f1bd9827cf206dfa2d", "doc_id": "6e14e31c94b911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWZWA222.pdf", "type": "pdf", "location": "\u9ea6\u6d4eWZWA222.pdf", "size": 9742831, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786365956617, "task_type": "dataflow", "root_trace_id": "bfb2f1d4af5749ba9e8b269686a95a2b", "root_traceparent": "00-bfb2f1d4af5749ba9e8b269686a95a2b-684dd3f6f78a8650-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:47:12,871 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:47:12,871 INFO     29 [qwen-vl-text] LLM output (len=431):
{
  "encounter_date": "2026-01-23",
  "pharmacy": "东吉轩药店",
  "medications": [
    {
      "name": "布地奈德福莫特罗吸入气雾剂(II)",
      "specification": "320ug/9ug/吸 60吸/支",
      "dosage": null,
      "quantity": 2,
      "unit_price": 268.00,
      "total_price": 536.00,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 536.00,
  "payment_method": null
}
2026-08-10 12:47:12,871 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-23]
2026-08-10 12:47:12,874 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2565324, prompt_len=875
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["东吉轩药店", "日期: 2026.01.23", "09: 23: 37", "单号: 20260123070132", "品名 规格 单价 数量 总计", "布地奈德福莫特罗吸入气雾剂", "(II)320ug/9ug/吸 60 吸/支", "268.00 2 536.00", "应收金额: 536.00", "实收金额: 536.00", "优惠金额: 0.00", "找零金额: 0.00", "会员:", "日期: 2026.01.23", "09: 23: 3", "单号: 20260123070132"]

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
2026-08-10 12:47:18,802 INFO     29 [qwen-vl-text] coord API raw response (len=920):
[
	{"text": "东吉轩药店", "bbox": [392, 68, 732, 119]},
	{"text": "日期: 2026.01.23", "bbox": [206, 162, 537, 192]},
	{"text": "09: 23: 37", "bbox": [624, 164, 846, 191]},
	{"text": "单号: 20260123070132", "bbox": [204, 217, 646, 248]},
	{"text": "品名 规格 单价 数量 总计", "bbox": [203, 272, 822, 306]},
	{"text": "布地奈德福莫特罗吸入气雾剂", "bbox": [203, 384, 781, 418]},
	{"text": "(II)320ug/9ug/吸 60 吸/支", "bbox": [245, 442, 742, 477]},
	{"text": "268.00 2 536.00", "bbox": [221, 501, 737, 529]},
	{"text": "应收金额: 536.00", "bbox": [202, 553, 549, 588]},
	{"text": "实收金额: 536.00", "bbox": [203, 611, 549, 645]},
	{"text": "优惠金额: 0.00", "bbox": [203, 667, 504, 699]},
	{"text": "找零金额: 0.00", "bbox": [203, 721, 504, 754]},
	{"text": "会员:", "bbox": [204, 776, 309, 810]},
	{"text": "日期: 2026.01.23", "bbox": [208, 888, 535, 920]},
	{"text": "09: 23: 3", "bbox": [645, 893, 853, 921]},
	{"text": "单号: 20260123070132", "bbox": [208, 942, 642, 973]}
]
2026-08-10 12:47:18,802 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=5.9s
2026-08-10 12:47:18,802 INFO     29 [qwen-vl-text] coord item[0]: text=东吉轩药店, bbox=[392, 68, 732, 119]
2026-08-10 12:47:18,802 INFO     29 [qwen-vl-text] coord item[1]: text=日期: 2026.01.23, bbox=[206, 162, 537, 192]
2026-08-10 12:47:18,802 INFO     29 [qwen-vl-text] coord item[2]: text=09: 23: 37, bbox=[624, 164, 846, 191]
2026-08-10 12:47:18,802 INFO     29 [qwen-vl-text] coord item[3]: text=单号: 20260123070132, bbox=[204, 217, 646, 248]
2026-08-10 12:47:18,802 INFO     29 [qwen-vl-text] coord item[4]: text=品名 规格 单价 数量 总计, bbox=[203, 272, 822, 306]
2026-08-10 12:47:18,802 INFO     29 [qwen-vl-text] coord item[5]: text=布地奈德福莫特罗吸入气雾剂, bbox=[203, 384, 781, 418]
2026-08-10 12:47:18,802 INFO     29 [qwen-vl-text] coord item[6]: text=(II)320ug/9ug/吸 60 吸/支, bbox=[245, 442, 742, 477]
2026-08-10 12:47:18,802 INFO     29 [qwen-vl-text] coord item[7]: text=268.00 2 536.00, bbox=[221, 501, 737, 529]
2026-08-10 12:47:18,802 INFO     29 [qwen-vl-text] coord item[8]: text=应收金额: 536.00, bbox=[202, 553, 549, 588]
2026-08-10 12:47:18,802 INFO     29 [qwen-vl-text] coord item[9]: text=实收金额: 536.00, bbox=[203, 611, 549, 645]
2026-08-10 12:47:18,802 INFO     29 [qwen-vl-text] coord item[10]: text=优惠金额: 0.00, bbox=[203, 667, 504, 699]
2026-08-10 12:47:18,802 INFO     29 [qwen-vl-text] coord item[11]: text=找零金额: 0.00, bbox=[203, 721, 504, 754]
2026-08-10 12:47:18,802 INFO     29 [qwen-vl-text] coord item[12]: text=会员:, bbox=[204, 776, 309, 810]
2026-08-10 12:47:18,802 INFO     29 [qwen-vl-text] coord item[13]: text=日期: 2026.01.23, bbox=[208, 888, 535, 920]
2026-08-10 12:47:18,802 INFO     29 [qwen-vl-text] coord item[14]: text=09: 23: 3, bbox=[645, 893, 853, 921]
2026-08-10 12:47:18,802 INFO     29 [qwen-vl-text] coord item[15]: text=单号: 20260123070132, bbox=[208, 942, 642, 973]
2026-08-10 12:47:18,803 INFO     29 [qwen-vl-text] page=4 — 16/16 coords, api_time=5.9s
2026-08-10 12:47:18,803 INFO     29 [qwen-vl-text] new_positions (16):
[[4, 233.23999999999998, 435.53999999999996, 57.256, 100.198], [4, 122.57, 319.515, 136.404, 161.664], [4, 371.28, 503.37, 138.088, 160.822], [4, 121.38, 384.37, 182.714, 208.816], [4, 120.785, 489.09, 229.024, 257.652], [4, 120.785, 464.695, 323.328, 351.95599999999996], [4, 145.775, 441.48999999999995, 372.164, 401.63399999999996], [4, 131.495, 438.515, 421.842, 445.418], [4, 120.19, 326.655, 465.626, 495.096], [4, 120.785, 326.655, 514.462, 543.09], [4, 120.785, 299.88, 561.614, 588.558], [4, 120.785, 299.88, 607.082, 634.8679999999999], [4, 121.38, 183.855, 653.3919999999999, 682.02], [4, 123.75999999999999, 318.325, 747.696, 774.64], [4, 383.775, 507.53499999999997, 751.906, 775.482], [4, 123.75999999999999, 381.99, 793.164, 819.266]]
2026-08-10 12:47:18,803 INFO     29 [qwen-vl-text] ═══ DONE ═══ 16 positions, pages=1, time=8.8s
2026-08-10 12:47:18,812 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 12:47:18,812 INFO     29 [Trace] task=6e5574f4 | doc=麦济WZWA222.pdf | Extractor:Medication | outputs={"chunks": "1 items, types={'MedicationRecord': 1}", "html": "", "json": "263 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_Medication\": 1}"}
2026-08-10 12:47:18,813 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 12:47:18,817 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:47:18,817 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:47:20,076 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:47:20,087 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 12:47:20,088 INFO     29 [Trace] task=6e5574f4 | doc=麦济WZWA222.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "263 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_Medication\": 1}"}
2026-08-10 12:47:20,088 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 12:47:20,096 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:47:20,096 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:47:20,565 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:47:20,572 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 12:47:20,572 INFO     29 [Trace] task=6e5574f4 | doc=麦济WZWA222.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "263 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_Medication\": 1}"}
2026-08-10 12:47:20,572 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 12:47:20,578 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:47:20,578 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:47:21,049 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:47:21,054 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 12:47:21,054 INFO     29 [Trace] task=6e5574f4 | doc=麦济WZWA222.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "263 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_Medication\": 1}"}
2026-08-10 12:47:21,054 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 12:47:21,059 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:47:21,059 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:47:21,059 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 12:47:21,060 INFO     29 [qwen-vl-text] positions(153): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:47:21,060 INFO     29 [qwen-vl-text] page grouping: [2, 3], lines per page: [150, 3]
2026-08-10 12:47:21,439 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:47:23,190 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:47:23,191 INFO     29 [qwen-vl-text] LLM extraction start, text_len=995
2026-08-10 12:47:23,191 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:47:23,192 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 58, \"bbox_end\": 210, \"encounter_dates\": [\"2025-12-26\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "肺常规通气检查报告\n测试号：0022542899\n姓名：\n出生日期：\n身高：165 cm\n临床印象：支气管哮喘\n住址：内蒙古自治区乌兰察布\n科别：\n住院号：0022542899\n性别：男\n年龄：70 Years\n体重：47 kg\n吸烟史：否\n联系电话：\n主管医生：\nF/V ex\nF/V in\nVol [L]\nVol%VCmax\nVCmax\nTime [s]\nVol [L]\nTime [s]\nFVC\n[L]\n3.34\n2.48\n74.0\nFEV 1\n[L]\n2.58\n1.45\n56.3\nFEV 2\n[L]\n1.82\nFEV 3\n[L]\n2.06\nFEV6\n[L]\n2.45\nFEV 1 % FVC\n[%]\n83.77\n58.60\n70.0\nFEV 1 % VC MAX\n[%]\n74.61\n58.60\n78.5\nPEF\n[L/s]\n7.27\n5.34\n73.4\nMEF 75\n[L/s]\n6.51\n1.94\n29.8\nMEF 50\n[L/s]\n3.73\n0.72\n19.4\nMEF 25\n[L/s]\n1.15\n0.25\n21.9\nMMEF 75/25\n[L/s]\n2.89\n0.60\n20.9\nFET\n[s]\n7.16\nFET PEF\n[s]\n0.05\nV backextrapolation ex\n[L]\n0.07\nV backextrapol. % FVC\n[%]\n2.82\nMVV\n[L/min]\n101.83\n37.40\n36.7\nFEV 1 % VC MAX\n[%]\n74.61\n58.60\n78.5\nVC EX\n[L]\n3.46\n2.48\n71.6\nFRV\n[L]\n0.93\nIRV\n[L]\n0.80\nVT\n[L]\n0.34\n1.65\n491.4\nIC\n[L]\n2.53\n2.45\n96.9\nBF\n[1/min]\n20.00\n13.38\n66.9\nMV\n[L/min]\n6.71\n22.08\n328.9\nVC MAX\n[L]\n3.46\n2.48\n71.6\nPred\nTEST1\n%/Pred\nTEST2\n%/Pred\nTEST3\n%/Pred\nDate\n25/12/26\nTime\n9:49:52\n结论：\n1. 中重度混合性肺通气功能障碍。\n轻度弥散功能障碍\n操作员：刘角玲\n内蒙古医科大学附属医院肺功能报告单\n地址：呼和浩特市通道北街一号\n电话：0471--3451056",
    "role": "user"
  }
]
2026-08-10 12:47:32,039 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:47:32,039 INFO     29 [qwen-vl-text] LLM output (len=1828):
{
  "exam_date": "2025-12-26",
  "report_date": "2025-12-26",
  "exam_name": "肺常规通气检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "测试号：0022542899\n姓名：\n出生日期：\n身高：165 cm\n临床印象：支气管哮喘\n住址：内蒙古自治区乌兰察布\n科别：\n住院号：0022542899\n性别：男\n年龄：70 Years\n体重：47 kg\n吸烟史：否\n联系电话：\n主管医生：\n\n| 指标 | 单位 | Pred | TEST1 | %/Pred | TEST2 | %/Pred | TEST3 | %/Pred |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n| FVC | [L] | 3.34 | 2.48 | 74.0 | | | | |\n| FEV 1 | [L] | 2.58 | 1.45 | 56.3 | | | | |\n| FEV 2 | [L] | | 1.82 | | | | | |\n| FEV 3 | [L] | | 2.06 | | | | | |\n| FEV6 | [L] | | 2.45 | | | | | |\n| FEV 1 % FVC | [%] | 83.77 | 58.60 | 70.0 | | | | |\n| FEV 1 % VC MAX | [%] | 74.61 | 58.60 | 78.5 | | | | |\n| PEF | [L/s] | 7.27 | 5.34 | 73.4 | | | | |\n| MEF 75 | [L/s] | 6.51 | 1.94 | 29.8 | | | | |\n| MEF 50 | [L/s] | 3.73 | 0.72 | 19.4 | | | | |\n| MEF 25 | [L/s] | 1.15 | 0.25 | 21.9 | | | | |\n| MMEF 75/25 | [L/s] | 2.89 | 0.60 | 20.9 | | | | |\n| FET | [s] | | 7.16 | | | | | |\n| FET PEF | [s] | | 0.05 | | | | | |\n| V backextrapolation ex | [L] | | 0.07 | | | | | |\n| V backextrapol. % FVC | [%] | | 2.82 | | | | | |\n| MVV | [L/min] | 101.83 | 37.40 | 36.7 | | | | |\n| FEV 1 % VC MAX | [%] | 74.61 | 58.60 | 78.5 | | | | |\n| VC EX | [L] | 3.46 | 2.48 | 71.6 | | | | |\n| FRV | [L] | | 0.93 | | | | | |\n| IRV | [L] | | 0.80 | | | | | |\n| VT | [L] | 0.34 | 1.65 | 491.4 | | | | |\n| IC | [L] | 2.53 | 2.45 | 96.9 | | | | |\n| BF | [1/min] | 20.00 | 13.38 | 66.9 | | | | |\n| MV | [L/min] | 6.71 | 22.08 | 328.9 | | | | |\n| VC MAX | [L] | 3.46 | 2.48 | 71.6 | | | | |\n\nDate: 25/12/26\nTime: 9:49:52",
  "conclusion": "1. 中重度混合性肺通气功能障碍。\n轻度弥散功能障碍",
  "physician": "刘角玲",
  "reviewer": null
}
2026-08-10 12:47:32,045 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2828092, prompt_len=2009
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共150行）
["肺常规通气检查报告", "测试号：0022542899", "姓名：", "出生日期：", "身高：165 cm", "临床印象：支气管哮喘", "住址：内蒙古自治区乌兰察布", "科别：", "住院号：0022542899", "性别：男", "年龄：70 Years", "体重：47 kg", "吸烟史：否", "联系电话：", "主管医生：", "F/V ex", "F/V in", "Vol [L]", "Vol%VCmax", "VCmax", "Time [s]", "Vol [L]", "Time [s]", "FVC", "[L]", "3.34", "2.48", "74.0", "FEV 1", "[L]", "2.58", "1.45", "56.3", "FEV 2", "[L]", "1.82", "FEV 3", "[L]", "2.06", "FEV6", "[L]", "2.45", "FEV 1 % FVC", "[%]", "83.77", "58.60", "70.0", "FEV 1 % VC MAX", "[%]", "74.61", "58.60", "78.5", "PEF", "[L/s]", "7.27", "5.34", "73.4", "MEF 75", "[L/s]", "6.51", "1.94", "29.8", "MEF 50", "[L/s]", "3.73", "0.72", "19.4", "MEF 25", "[L/s]", "1.15", "0.25", "21.9", "MMEF 75/25", "[L/s]", "2.89", "0.60", "20.9", "FET", "[s]", "7.16", "FET PEF", "[s]", "0.05", "V backextrapolation ex", "[L]", "0.07", "V backextrapol. % FVC", "[%]", "2.82", "MVV", "[L/min]", "101.83", "37.40", "36.7", "FEV 1 % VC MAX", "[%]", "74.61", "58.60", "78.5", "VC EX", "[L]", "3.46", "2.48", "71.6", "FRV", "[L]", "0.93", "IRV", "[L]", "0.80", "VT", "[L]", "0.34", "1.65", "491.4", "IC", "[L]", "2.53", "2.45", "96.9", "BF", "[1/min]", "20.00", "13.38", "66.9", "MV", "[L/min]", "6.71", "22.08", "328.9", "VC MAX", "[L]", "3.46", "2.48", "71.6", "Pred", "TEST1", "%/Pred", "TEST2", "%/Pred", "TEST3", "%/Pred", "Date", "25/12/26", "Time", "9:49:52", "结论：", "1. 中重度混合性肺通气功能障碍。", "轻度弥散功能障碍", "操作员：刘角玲"]

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
2026-08-10 12:48:09,148 INFO     29 [qwen-vl-text] coord API raw response (len=7519):
[
	{"text": "肺常规通气检查报告", "bbox": [370, 106, 607, 126]},
	{"text": "测试号：0022542899", "bbox": [176, 127, 398, 140]},
	{"text": "姓名：", "bbox": [176, 140, 218, 152]},
	{"text": "出生日期：", "bbox": [176, 152, 248, 165]},
	{"text": "身高：165 cm", "bbox": [176, 165, 376, 177]},
	{"text": "临床印象：支气管哮喘", "bbox": [176, 177, 409, 190]},
	{"text": "住址：内蒙古自治区乌兰察布", "bbox": [176, 190, 492, 202]},
	{"text": "科别：", "bbox": [176, 202, 214, 215]},
	{"text": "住院号：0022542899", "bbox": [517, 127, 750, 139]},
	{"text": "性别：男", "bbox": [667, 139, 685, 150]},
	{"text": "年龄：70 Years", "bbox": [667, 150, 734, 162]},
	{"text": "体重：47 kg", "bbox": [667, 162, 710, 175]},
	{"text": "吸烟史：否", "bbox": [667, 175, 685, 187]},
	{"text": "联系电话：", "bbox": [517, 190, 589, 202]},
	{"text": "主管医生：", "bbox": [517, 202, 589, 215]},
	{"text": "F/V ex", "bbox": [229, 238, 268, 248]},
	{"text": "F/V in", "bbox": [233, 346, 267, 356]},
	{"text": "Vol [L]", "bbox": [417, 240, 455, 252]},
	{"text": "Vol%VCmax", "bbox": [367, 296, 434, 306]},
	{"text": "VCmax", "bbox": [431, 311, 470, 321]},
	{"text": "Time [s]", "bbox": [502, 330, 547, 341]},
	{"text": "Vol [L]", "bbox": [690, 230, 728, 241]},
	{"text": "Time [s]", "bbox": [788, 327, 835, 338]},
	{"text": "FVC", "bbox": [92, 394, 119, 405]},
	{"text": "[L]", "bbox": [292, 393, 314, 406]},
	{"text": "3.34", "bbox": [462, 394, 497, 405]},
	{"text": "2.48", "bbox": [538, 394, 572, 405]},
	{"text": "74.0", "bbox": [614, 394, 652, 405]},
	{"text": "FEV 1", "bbox": [92, 407, 132, 418]},
	{"text": "[L]", "bbox": [292, 406, 314, 419]},
	{"text": "2.58", "bbox": [462, 407, 497, 418]},
	{"text": "1.45", "bbox": [538, 407, 572, 418]},
	{"text": "56.3", "bbox": [614, 407, 652, 418]},
	{"text": "FEV 2", "bbox": [92, 420, 134, 431]},
	{"text": "[L]", "bbox": [292, 419, 314, 432]},
	{"text": "1.82", "bbox": [538, 420, 572, 431]},
	{"text": "FEV 3", "bbox": [92, 433, 134, 444]},
	{"text": "[L]", "bbox": [292, 432, 314, 445]},
	{"text": "2.06", "bbox": [538, 433, 572, 444]},
	{"text": "FEV6", "bbox": [92, 446, 126, 457]},
	{"text": "[L]", "bbox": [292, 445, 314, 458]},
	{"text": "2.45", "bbox": [538, 446, 572, 457]},
	{"text": "FEV 1 % FVC", "bbox": [92, 459, 183, 470]},
	{"text": "[%]", "bbox": [292, 458, 314, 471]},
	{"text": "83.77", "bbox": [454, 459, 497, 470]},
	{"text": "58.60", "bbox": [530, 459, 572, 470]},
	{"text": "70.0", "bbox": [614, 459, 652, 470]},
	{"text": "FEV 1 % VC MAX", "bbox": [92, 471, 208, 482]},
	{"text": "[%]", "bbox": [292, 471, 314, 483]},
	{"text": "74.61", "bbox": [454, 471, 497, 482]},
	{"text": "58.60", "bbox": [530, 471, 572, 482]},
	{"text": "78.5", "bbox": [614, 471, 652, 482]},
	{"text": "PEF", "bbox": [92, 484, 117, 495]},
	{"text": "[L/s]", "bbox": [274, 483, 314, 496]},
	{"text": "7.27", "bbox": [462, 484, 497, 495]},
	{"text": "5.34", "bbox": [538, 484, 572, 495]},
	{"text": "73.4", "bbox": [614, 484, 652, 495]},
	{"text": "MEF 75", "bbox": [92, 497, 142, 508]},
	{"text": "[L/s]", "bbox": [274, 496, 314, 509]},
	{"text": "6.51", "bbox": [462, 497, 497, 508]},
	{"text": "1.94", "bbox": [538, 497, 572, 508]},
	{"text": "29.8", "bbox": [614, 497, 652, 508]},
	{"text": "MEF 50", "bbox": [92, 510, 142, 521]},
	{"text": "[L/s]", "bbox": [274, 509, 314, 522]},
	{"text": "3.73", "bbox": [462, 510, 497, 521]},
	{"text": "0.72", "bbox": [538, 510, 572, 521]},
	{"text": "19.4", "bbox": [614, 510, 652, 521]},
	{"text": "MEF 25", "bbox": [92, 523, 142, 534]},
	{"text": "[L/s]", "bbox": [274, 522, 314, 535]},
	{"text": "1.15", "bbox": [462, 523, 497, 534]},
	{"text": "0.25", "bbox": [538, 523, 572, 534]},
	{"text": "21.9", "bbox": [614, 523, 652, 534]},
	{"text": "MMEF 75/25", "bbox": [92, 536, 174, 547]},
	{"text": "[L/s]", "bbox": [274, 535, 314, 548]},
	{"text": "2.89", "bbox": [462, 536, 497, 547]},
	{"text": "0.60", "bbox": [538, 536, 572, 547]},
	{"text": "20.9", "bbox": [614, 536, 652, 547]},
	{"text": "FET", "bbox": [92, 549, 117, 560]},
	{"text": "[s]", "bbox": [292, 548, 314, 561]},
	{"text": "7.16", "bbox": [538, 549, 572, 560]},
	{"text": "FET PEF", "bbox": [92, 561, 150, 573]},
	{"text": "[s]", "bbox": [292, 561, 314, 574]},
	{"text": "0.05", "bbox": [538, 561, 572, 573]},
	{"text": "V backextrapolation ex", "bbox": [92, 575, 274, 586]},
	{"text": "[L]", "bbox": [292, 574, 314, 587]},
	{"text": "0.07", "bbox": [538, 575, 572, 586]},
	{"text": "V backextrapol. % FVC", "bbox": [92, 587, 265, 599]},
	{"text": "[%]", "bbox": [292, 587, 314, 600]},
	{"text": "2.82", "bbox": [538, 587, 572, 599]},
	{"text": "MVV", "bbox": [92, 601, 117, 612]},
	{"text": "[L/min]", "bbox": [257, 600, 314, 613]},
	{"text": "101.83", "bbox": [447, 601, 497, 612]},
	{"text": "37.40", "bbox": [530, 601, 572, 612]},
	{"text": "36.7", "bbox": [614, 601, 652, 612]},
	{"text": "FEV 1 % VC MAX", "bbox": [92, 614, 206, 625]},
	{"text": "[%]", "bbox": [292, 613, 314, 626]},
	{"text": "74.61", "bbox": [454, 614, 497, 625]},
	{"text": "58.60", "bbox": [530, 614, 572, 625]},
	{"text": "78.5", "bbox": [614, 614, 652, 625]},
	{"text": "VC EX", "bbox": [92, 640, 132, 651]},
	{"text": "[L]", "bbox": [292, 639, 314, 652]},
	{"text": "3.46", "bbox": [462, 640, 497, 651]},
	{"text": "2.48", "bbox": [538, 640, 572, 651]},
	{"text": "71.6", "bbox": [614, 640, 652, 651]},
	{"text": "FRV", "bbox": [92, 653, 117, 664]},
	{"text": "[L]", "bbox": [292, 652, 314, 665]},
	{"text": "0.93", "bbox": [459, 653, 497, 664]},
	{"text": "IRV", "bbox": [92, 666, 117, 677]},
	{"text": "[L]", "bbox": [292, 665, 314, 678]},
	{"text": "0.80", "bbox": [538, 666, 572, 677]},
	{"text": "VT", "bbox": [92, 679, 107, 690]},
	{"text": "[L]", "bbox": [292, 678, 314, 691]},
	{"text": "0.34", "bbox": [462, 679, 497, 690]},
	{"text": "1.65", "bbox": [538, 679, 572, 690]},
	{"text": "491.4", "bbox": [608, 679, 652, 690]},
	{"text": "IC", "bbox": [92, 692, 107, 703]},
	{"text": "[L]", "bbox": [292, 691, 314, 704]},
	{"text": "2.53", "bbox": [462, 692, 497, 703]},
	{"text": "2.45", "bbox": [538, 692, 572, 703]},
	{"text": "96.9", "bbox": [614, 692, 652, 703]},
	{"text": "BF", "bbox": [92, 705, 107, 716]},
	{"text": "[1/min]", "bbox": [257, 704, 314, 717]},
	{"text": "20.00", "bbox": [454, 705, 497, 716]},
	{"text": "13.38", "bbox": [530, 705, 572, 716]},
	{"text": "66.9", "bbox": [614, 705, 652, 716]},
	{"text": "MV", "bbox": [92, 718, 107, 729]},
	{"text": "[L/min]", "bbox": [257, 717, 314, 730]},
	{"text": "6.71", "bbox": [462, 718, 497, 729]},
	{"text": "22.08", "bbox": [530, 718, 572, 729]},
	{"text": "328.9", "bbox": [608, 718, 652, 729]},
	{"text": "VC MAX", "bbox": [92, 730, 142, 742]},
	{"text": "[L]", "bbox": [292, 730, 314, 743]},
	{"text": "3.46", "bbox": [462, 730, 497, 742]},
	{"text": "2.48", "bbox": [538, 730, 572, 742]},
	{"text": "71.6", "bbox": [614, 730, 652, 742]},
	{"text": "Pred", "bbox": [460, 368, 497, 380]},
	{"text": "TEST1", "bbox": [530, 368, 570, 380]},
	{"text": "%/Pred", "bbox": [597, 368, 650, 380]},
	{"text": "TEST2", "bbox": [685, 368, 728, 380]},
	{"text": "%/Pred", "bbox": [755, 368, 807, 380]},
	{"text": "TEST3", "bbox": [843, 368, 885, 380]},
	{"text": "%/Pred", "bbox": [911, 368, 963, 380]},
	{"text": "Date", "bbox": [92, 757, 125, 768]},
	{"text": "25/12/26", "bbox": [507, 757, 575, 768]},
	{"text": "Time", "bbox": [92, 770, 125, 781]},
	{"text": "9:49:52", "bbox": [504, 770, 575, 781]},
	{"text": "结论：", "bbox": [97, 795, 150, 812]},
	{"text": "1. 中重度混合性肺通气功能障碍。", "bbox": [112, 815, 363, 828]},
	{"text": "轻度弥散功能障碍", "bbox": [112, 827, 244, 840]},
	{"text": "操作员：刘角玲", "bbox": [792, 847, 950, 873]}
]
2026-08-10 12:48:09,149 INFO     29 [qwen-vl-text] coord API: raw_items=150, valid_items=150, elapsed=37.1s
2026-08-10 12:48:09,149 INFO     29 [qwen-vl-text] coord item[0]: text=肺常规通气检查报告, bbox=[370, 106, 607, 126]
2026-08-10 12:48:09,149 INFO     29 [qwen-vl-text] coord item[1]: text=测试号：0022542899, bbox=[176, 127, 398, 140]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[176, 140, 218, 152]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[3]: text=出生日期：, bbox=[176, 152, 248, 165]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[4]: text=身高：165 cm, bbox=[176, 165, 376, 177]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[5]: text=临床印象：支气管哮喘, bbox=[176, 177, 409, 190]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[6]: text=住址：内蒙古自治区乌兰察布, bbox=[176, 190, 492, 202]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[7]: text=科别：, bbox=[176, 202, 214, 215]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[8]: text=住院号：0022542899, bbox=[517, 127, 750, 139]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[9]: text=性别：男, bbox=[667, 139, 685, 150]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[10]: text=年龄：70 Years, bbox=[667, 150, 734, 162]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[11]: text=体重：47 kg, bbox=[667, 162, 710, 175]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[12]: text=吸烟史：否, bbox=[667, 175, 685, 187]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[13]: text=联系电话：, bbox=[517, 190, 589, 202]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[14]: text=主管医生：, bbox=[517, 202, 589, 215]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[15]: text=F/V ex, bbox=[229, 238, 268, 248]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[16]: text=F/V in, bbox=[233, 346, 267, 356]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[17]: text=Vol [L], bbox=[417, 240, 455, 252]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[18]: text=Vol%VCmax, bbox=[367, 296, 434, 306]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[19]: text=VCmax, bbox=[431, 311, 470, 321]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[20]: text=Time [s], bbox=[502, 330, 547, 341]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[21]: text=Vol [L], bbox=[690, 230, 728, 241]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[22]: text=Time [s], bbox=[788, 327, 835, 338]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[23]: text=FVC, bbox=[92, 394, 119, 405]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[24]: text=[L], bbox=[292, 393, 314, 406]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[25]: text=3.34, bbox=[462, 394, 497, 405]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[26]: text=2.48, bbox=[538, 394, 572, 405]
2026-08-10 12:48:09,150 INFO     29 [qwen-vl-text] coord item[27]: text=74.0, bbox=[614, 394, 652, 405]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[28]: text=FEV 1, bbox=[92, 407, 132, 418]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[29]: text=[L], bbox=[292, 406, 314, 419]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[30]: text=2.58, bbox=[462, 407, 497, 418]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[31]: text=1.45, bbox=[538, 407, 572, 418]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[32]: text=56.3, bbox=[614, 407, 652, 418]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[33]: text=FEV 2, bbox=[92, 420, 134, 431]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[34]: text=[L], bbox=[292, 419, 314, 432]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[35]: text=1.82, bbox=[538, 420, 572, 431]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[36]: text=FEV 3, bbox=[92, 433, 134, 444]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[37]: text=[L], bbox=[292, 432, 314, 445]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[38]: text=2.06, bbox=[538, 433, 572, 444]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[39]: text=FEV6, bbox=[92, 446, 126, 457]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[40]: text=[L], bbox=[292, 445, 314, 458]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[41]: text=2.45, bbox=[538, 446, 572, 457]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[42]: text=FEV 1 % FVC, bbox=[92, 459, 183, 470]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[43]: text=[%], bbox=[292, 458, 314, 471]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[44]: text=83.77, bbox=[454, 459, 497, 470]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[45]: text=58.60, bbox=[530, 459, 572, 470]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[46]: text=70.0, bbox=[614, 459, 652, 470]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[47]: text=FEV 1 % VC MAX, bbox=[92, 471, 208, 482]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[48]: text=[%], bbox=[292, 471, 314, 483]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[49]: text=74.61, bbox=[454, 471, 497, 482]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[50]: text=58.60, bbox=[530, 471, 572, 482]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[51]: text=78.5, bbox=[614, 471, 652, 482]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[52]: text=PEF, bbox=[92, 484, 117, 495]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[53]: text=[L/s], bbox=[274, 483, 314, 496]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[54]: text=7.27, bbox=[462, 484, 497, 495]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[55]: text=5.34, bbox=[538, 484, 572, 495]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[56]: text=73.4, bbox=[614, 484, 652, 495]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[57]: text=MEF 75, bbox=[92, 497, 142, 508]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[58]: text=[L/s], bbox=[274, 496, 314, 509]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[59]: text=6.51, bbox=[462, 497, 497, 508]
2026-08-10 12:48:09,151 INFO     29 [qwen-vl-text] coord item[60]: text=1.94, bbox=[538, 497, 572, 508]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[61]: text=29.8, bbox=[614, 497, 652, 508]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[62]: text=MEF 50, bbox=[92, 510, 142, 521]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[63]: text=[L/s], bbox=[274, 509, 314, 522]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[64]: text=3.73, bbox=[462, 510, 497, 521]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[65]: text=0.72, bbox=[538, 510, 572, 521]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[66]: text=19.4, bbox=[614, 510, 652, 521]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[67]: text=MEF 25, bbox=[92, 523, 142, 534]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[68]: text=[L/s], bbox=[274, 522, 314, 535]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[69]: text=1.15, bbox=[462, 523, 497, 534]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[70]: text=0.25, bbox=[538, 523, 572, 534]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[71]: text=21.9, bbox=[614, 523, 652, 534]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[72]: text=MMEF 75/25, bbox=[92, 536, 174, 547]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[73]: text=[L/s], bbox=[274, 535, 314, 548]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[74]: text=2.89, bbox=[462, 536, 497, 547]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[75]: text=0.60, bbox=[538, 536, 572, 547]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[76]: text=20.9, bbox=[614, 536, 652, 547]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[77]: text=FET, bbox=[92, 549, 117, 560]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[78]: text=[s], bbox=[292, 548, 314, 561]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[79]: text=7.16, bbox=[538, 549, 572, 560]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[80]: text=FET PEF, bbox=[92, 561, 150, 573]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[81]: text=[s], bbox=[292, 561, 314, 574]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[82]: text=0.05, bbox=[538, 561, 572, 573]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[83]: text=V backextrapolation ex, bbox=[92, 575, 274, 586]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[84]: text=[L], bbox=[292, 574, 314, 587]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[85]: text=0.07, bbox=[538, 575, 572, 586]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[86]: text=V backextrapol. % FVC, bbox=[92, 587, 265, 599]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[87]: text=[%], bbox=[292, 587, 314, 600]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[88]: text=2.82, bbox=[538, 587, 572, 599]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[89]: text=MVV, bbox=[92, 601, 117, 612]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[90]: text=[L/min], bbox=[257, 600, 314, 613]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[91]: text=101.83, bbox=[447, 601, 497, 612]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[92]: text=37.40, bbox=[530, 601, 572, 612]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[93]: text=36.7, bbox=[614, 601, 652, 612]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[94]: text=FEV 1 % VC MAX, bbox=[92, 614, 206, 625]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[95]: text=[%], bbox=[292, 613, 314, 626]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[96]: text=74.61, bbox=[454, 614, 497, 625]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[97]: text=58.60, bbox=[530, 614, 572, 625]
2026-08-10 12:48:09,152 INFO     29 [qwen-vl-text] coord item[98]: text=78.5, bbox=[614, 614, 652, 625]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[99]: text=VC EX, bbox=[92, 640, 132, 651]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[100]: text=[L], bbox=[292, 639, 314, 652]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[101]: text=3.46, bbox=[462, 640, 497, 651]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[102]: text=2.48, bbox=[538, 640, 572, 651]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[103]: text=71.6, bbox=[614, 640, 652, 651]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[104]: text=FRV, bbox=[92, 653, 117, 664]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[105]: text=[L], bbox=[292, 652, 314, 665]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[106]: text=0.93, bbox=[459, 653, 497, 664]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[107]: text=IRV, bbox=[92, 666, 117, 677]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[108]: text=[L], bbox=[292, 665, 314, 678]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[109]: text=0.80, bbox=[538, 666, 572, 677]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[110]: text=VT, bbox=[92, 679, 107, 690]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[111]: text=[L], bbox=[292, 678, 314, 691]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[112]: text=0.34, bbox=[462, 679, 497, 690]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[113]: text=1.65, bbox=[538, 679, 572, 690]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[114]: text=491.4, bbox=[608, 679, 652, 690]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[115]: text=IC, bbox=[92, 692, 107, 703]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[116]: text=[L], bbox=[292, 691, 314, 704]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[117]: text=2.53, bbox=[462, 692, 497, 703]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[118]: text=2.45, bbox=[538, 692, 572, 703]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[119]: text=96.9, bbox=[614, 692, 652, 703]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[120]: text=BF, bbox=[92, 705, 107, 716]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[121]: text=[1/min], bbox=[257, 704, 314, 717]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[122]: text=20.00, bbox=[454, 705, 497, 716]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[123]: text=13.38, bbox=[530, 705, 572, 716]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[124]: text=66.9, bbox=[614, 705, 652, 716]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[125]: text=MV, bbox=[92, 718, 107, 729]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[126]: text=[L/min], bbox=[257, 717, 314, 730]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[127]: text=6.71, bbox=[462, 718, 497, 729]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[128]: text=22.08, bbox=[530, 718, 572, 729]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[129]: text=328.9, bbox=[608, 718, 652, 729]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[130]: text=VC MAX, bbox=[92, 730, 142, 742]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[131]: text=[L], bbox=[292, 730, 314, 743]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[132]: text=3.46, bbox=[462, 730, 497, 742]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[133]: text=2.48, bbox=[538, 730, 572, 742]
2026-08-10 12:48:09,153 INFO     29 [qwen-vl-text] coord item[134]: text=71.6, bbox=[614, 730, 652, 742]
2026-08-10 12:48:09,154 INFO     29 [qwen-vl-text] coord item[135]: text=Pred, bbox=[460, 368, 497, 380]
2026-08-10 12:48:09,154 INFO     29 [qwen-vl-text] coord item[136]: text=TEST1, bbox=[530, 368, 570, 380]
2026-08-10 12:48:09,154 INFO     29 [qwen-vl-text] coord item[137]: text=%/Pred, bbox=[597, 368, 650, 380]
2026-08-10 12:48:09,154 INFO     29 [qwen-vl-text] coord item[138]: text=TEST2, bbox=[685, 368, 728, 380]
2026-08-10 12:48:09,154 INFO     29 [qwen-vl-text] coord item[139]: text=%/Pred, bbox=[755, 368, 807, 380]
2026-08-10 12:48:09,154 INFO     29 [qwen-vl-text] coord item[140]: text=TEST3, bbox=[843, 368, 885, 380]
2026-08-10 12:48:09,154 INFO     29 [qwen-vl-text] coord item[141]: text=%/Pred, bbox=[911, 368, 963, 380]
2026-08-10 12:48:09,154 INFO     29 [qwen-vl-text] coord item[142]: text=Date, bbox=[92, 757, 125, 768]
2026-08-10 12:48:09,154 INFO     29 [qwen-vl-text] coord item[143]: text=25/12/26, bbox=[507, 757, 575, 768]
2026-08-10 12:48:09,154 INFO     29 [qwen-vl-text] coord item[144]: text=Time, bbox=[92, 770, 125, 781]
2026-08-10 12:48:09,154 INFO     29 [qwen-vl-text] coord item[145]: text=9:49:52, bbox=[504, 770, 575, 781]
2026-08-10 12:48:09,154 INFO     29 [qwen-vl-text] coord item[146]: text=结论：, bbox=[97, 795, 150, 812]
2026-08-10 12:48:09,154 INFO     29 [qwen-vl-text] coord item[147]: text=1. 中重度混合性肺通气功能障碍。, bbox=[112, 815, 363, 828]
2026-08-10 12:48:09,154 INFO     29 [qwen-vl-text] coord item[148]: text=轻度弥散功能障碍, bbox=[112, 827, 244, 840]
2026-08-10 12:48:09,154 INFO     29 [qwen-vl-text] coord item[149]: text=操作员：刘角玲, bbox=[792, 847, 950, 873]
2026-08-10 12:48:09,155 INFO     29 [qwen-vl-text] page=2 — 150/150 coords, api_time=37.1s
2026-08-10 12:48:09,163 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3667065, prompt_len=670
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共3行）
["内蒙古医科大学附属医院肺功能报告单", "地址：呼和浩特市通道北街一号", "电话：0471--3451056"]

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
2026-08-10 12:48:11,256 INFO     29 [qwen-vl-text] coord API raw response (len=193):
```json
[
	{"text": "内蒙古医科大学附属医院肺功能报告单", "bbox": [248, 54, 788, 78]},
	{"text": "地址：呼和浩特市通道北街一号", "bbox": [331, 92, 705, 111]},
	{"text": "电话：0471--3451056", "bbox": [391, 111, 648, 129]}
]
```
2026-08-10 12:48:11,256 INFO     29 [qwen-vl-text] coord API: raw_items=3, valid_items=3, elapsed=2.1s
2026-08-10 12:48:11,257 INFO     29 [qwen-vl-text] coord item[0]: text=内蒙古医科大学附属医院肺功能报告单, bbox=[248, 54, 788, 78]
2026-08-10 12:48:11,257 INFO     29 [qwen-vl-text] coord item[1]: text=地址：呼和浩特市通道北街一号, bbox=[331, 92, 705, 111]
2026-08-10 12:48:11,257 INFO     29 [qwen-vl-text] coord item[2]: text=电话：0471--3451056, bbox=[391, 111, 648, 129]
2026-08-10 12:48:11,258 INFO     29 [qwen-vl-text] page=3 — 3/3 coords, api_time=2.1s
2026-08-10 12:48:11,259 INFO     29 [qwen-vl-text] new_positions (153):
[[2, 220.14999999999998, 361.16499999999996, 89.252, 106.092], [2, 104.72, 236.81, 106.934, 117.88], [2, 104.72, 129.71, 117.88, 127.984], [2, 104.72, 147.56, 127.984, 138.93], [2, 104.72, 223.72, 138.93, 149.034], [2, 104.72, 243.355, 149.034, 159.98], [2, 104.72, 292.74, 159.98, 170.084], [2, 104.72, 127.33, 170.084, 181.03], [2, 307.615, 446.25, 106.934, 117.038], [2, 396.865, 407.575, 117.038, 126.3], [2, 396.865, 436.72999999999996, 126.3, 136.404], [2, 396.865, 422.45, 136.404, 147.35], [2, 396.865, 407.575, 147.35, 157.454], [2, 307.615, 350.455, 159.98, 170.084], [2, 307.615, 350.455, 170.084, 181.03], [2, 136.255, 159.45999999999998, 200.396, 208.816], [2, 138.635, 158.86499999999998, 291.332, 299.752], [2, 248.11499999999998, 270.72499999999997, 202.07999999999998, 212.184], [2, 218.36499999999998, 258.22999999999996, 249.232, 257.652], [2, 256.445, 279.65, 261.86199999999997, 270.282], [2, 298.69, 325.465, 277.86, 287.122], [2, 410.54999999999995, 433.15999999999997, 193.66, 202.922], [2, 468.85999999999996, 496.825, 275.334, 284.596], [2, 54.739999999999995, 70.80499999999999, 331.748, 341.01], [2, 173.73999999999998, 186.82999999999998, 330.906, 341.852], [2, 274.89, 295.715, 331.748, 341.01], [2, 320.11, 340.34, 331.748, 341.01], [2, 365.33, 387.94, 331.748, 341.01], [2, 54.739999999999995, 78.53999999999999, 342.69399999999996, 351.95599999999996], [2, 173.73999999999998, 186.82999999999998, 341.852, 352.798], [2, 274.89, 295.715, 342.69399999999996, 351.95599999999996], [2, 320.11, 340.34, 342.69399999999996, 351.95599999999996], [2, 365.33, 387.94, 342.69399999999996, 351.95599999999996], [2, 54.739999999999995, 79.72999999999999, 353.64, 362.902], [2, 173.73999999999998, 186.82999999999998, 352.798, 363.74399999999997], [2, 320.11, 340.34, 353.64, 362.902], [2, 54.739999999999995, 79.72999999999999, 364.586, 373.848], [2, 173.73999999999998, 186.82999999999998, 363.74399999999997, 374.69], [2, 320.11, 340.34, 364.586, 373.848], [2, 54.739999999999995, 74.97, 375.532, 384.794], [2, 173.73999999999998, 186.82999999999998, 374.69, 385.63599999999997], [2, 320.11, 340.34, 375.532, 384.794], [2, 54.739999999999995, 108.88499999999999, 386.478, 395.74], [2, 173.73999999999998, 186.82999999999998, 385.63599999999997, 396.582], [2, 270.13, 295.715, 386.478, 395.74], [2, 315.34999999999997, 340.34, 386.478, 395.74], [2, 365.33, 387.94, 386.478, 395.74], [2, 54.739999999999995, 123.75999999999999, 396.582, 405.844], [2, 173.73999999999998, 186.82999999999998, 396.582, 406.686], [2, 270.13, 295.715, 396.582, 405.844], [2, 315.34999999999997, 340.34, 396.582, 405.844], [2, 365.33, 387.94, 396.582, 405.844], [2, 54.739999999999995, 69.615, 407.52799999999996, 416.78999999999996], [2, 163.03, 186.82999999999998, 406.686, 417.632], [2, 274.89, 295.715, 407.52799999999996, 416.78999999999996], [2, 320.11, 340.34, 407.52799999999996, 416.78999999999996], [2, 365.33, 387.94, 407.52799999999996, 416.78999999999996], [2, 54.739999999999995, 84.49, 418.474, 427.736], [2, 163.03, 186.82999999999998, 417.632, 428.578], [2, 274.89, 295.715, 418.474, 427.736], [2, 320.11, 340.34, 418.474, 427.736], [2, 365.33, 387.94, 418.474, 427.736], [2, 54.739999999999995, 84.49, 429.41999999999996, 438.68199999999996], [2, 163.03, 186.82999999999998, 428.578, 439.524], [2, 274.89, 295.715, 429.41999999999996, 438.68199999999996], [2, 320.11, 340.34, 429.41999999999996, 438.68199999999996], [2, 365.33, 387.94, 429.41999999999996, 438.68199999999996], [2, 54.739999999999995, 84.49, 440.366, 449.628], [2, 163.03, 186.82999999999998, 439.524, 450.46999999999997], [2, 274.89, 295.715, 440.366, 449.628], [2, 320.11, 340.34, 440.366, 449.628], [2, 365.33, 387.94, 440.366, 449.628], [2, 54.739999999999995, 103.53, 451.312, 460.574], [2, 163.03, 186.82999999999998, 450.46999999999997, 461.416], [2, 274.89, 295.715, 451.312, 460.574], [2, 320.11, 340.34, 451.312, 460.574], [2, 365.33, 387.94, 451.312, 460.574], [2, 54.739999999999995, 69.615, 462.258, 471.52], [2, 173.73999999999998, 186.82999999999998, 461.416, 472.36199999999997], [2, 320.11, 340.34, 462.258, 471.52], [2, 54.739999999999995, 89.25, 472.36199999999997, 482.466], [2, 173.73999999999998, 186.82999999999998, 472.36199999999997, 483.308], [2, 320.11, 340.34, 472.36199999999997, 482.466], [2, 54.739999999999995, 163.03, 484.15, 493.412], [2, 173.73999999999998, 186.82999999999998, 483.308, 494.25399999999996], [2, 320.11, 340.34, 484.15, 493.412], [2, 54.739999999999995, 157.67499999999998, 494.25399999999996, 504.358], [2, 173.73999999999998, 186.82999999999998, 494.25399999999996, 505.2], [2, 320.11, 340.34, 494.25399999999996, 504.358], [2, 54.739999999999995, 69.615, 506.042, 515.304], [2, 152.915, 186.82999999999998, 505.2, 516.146], [2, 265.965, 295.715, 506.042, 515.304], [2, 315.34999999999997, 340.34, 506.042, 515.304], [2, 365.33, 387.94, 506.042, 515.304], [2, 54.739999999999995, 122.57, 516.9879999999999, 526.25], [2, 173.73999999999998, 186.82999999999998, 516.146, 527.092], [2, 270.13, 295.715, 516.9879999999999, 526.25], [2, 315.34999999999997, 340.34, 516.9879999999999, 526.25], [2, 365.33, 387.94, 516.9879999999999, 526.25], [2, 54.739999999999995, 78.53999999999999, 538.88, 548.1419999999999], [2, 173.73999999999998, 186.82999999999998, 538.038, 548.984], [2, 274.89, 295.715, 538.88, 548.1419999999999], [2, 320.11, 340.34, 538.88, 548.1419999999999], [2, 365.33, 387.94, 538.88, 548.1419999999999], [2, 54.739999999999995, 69.615, 549.826, 559.088], [2, 173.73999999999998, 186.82999999999998, 548.984, 559.93], [2, 273.10499999999996, 295.715, 549.826, 559.088], [2, 54.739999999999995, 69.615, 560.7719999999999, 570.034], [2, 173.73999999999998, 186.82999999999998, 559.93, 570.876], [2, 320.11, 340.34, 560.7719999999999, 570.034], [2, 54.739999999999995, 63.665, 571.718, 580.98], [2, 173.73999999999998, 186.82999999999998, 570.876, 581.822], [2, 274.89, 295.715, 571.718, 580.98], [2, 320.11, 340.34, 571.718, 580.98], [2, 361.76, 387.94, 571.718, 580.98], [2, 54.739999999999995, 63.665, 582.664, 591.9259999999999], [2, 173.73999999999998, 186.82999999999998, 581.822, 592.768], [2, 274.89, 295.715, 582.664, 591.9259999999999], [2, 320.11, 340.34, 582.664, 591.9259999999999], [2, 365.33, 387.94, 582.664, 591.9259999999999], [2, 54.739999999999995, 63.665, 593.61, 602.872], [2, 152.915, 186.82999999999998, 592.768, 603.7139999999999], [2, 270.13, 295.715, 593.61, 602.872], [2, 315.34999999999997, 340.34, 593.61, 602.872], [2, 365.33, 387.94, 593.61, 602.872], [2, 54.739999999999995, 63.665, 604.5559999999999, 613.818], [2, 152.915, 186.82999999999998, 603.7139999999999, 614.66], [2, 274.89, 295.715, 604.5559999999999, 613.818], [2, 315.34999999999997, 340.34, 604.5559999999999, 613.818], [2, 361.76, 387.94, 604.5559999999999, 613.818], [2, 54.739999999999995, 84.49, 614.66, 624.764], [2, 173.73999999999998, 186.82999999999998, 614.66, 625.606], [2, 274.89, 295.715, 614.66, 624.764], [2, 320.11, 340.34, 614.66, 624.764], [2, 365.33, 387.94, 614.66, 624.764], [2, 273.7, 295.715, 309.856, 319.96], [2, 315.34999999999997, 339.15, 309.856, 319.96], [2, 355.215, 386.75, 309.856, 319.96], [2, 407.575, 433.15999999999997, 309.856, 319.96], [2, 449.22499999999997, 480.16499999999996, 309.856, 319.96], [2, 501.585, 526.5749999999999, 309.856, 319.96], [2, 542.045, 572.985, 309.856, 319.96], [2, 54.739999999999995, 74.375, 637.394, 646.656], [2, 301.66499999999996, 342.125, 637.394, 646.656], [2, 54.739999999999995, 74.375, 648.34, 657.602], [2, 299.88, 342.125, 648.34, 657.602], [2, 57.714999999999996, 89.25, 669.39, 683.704], [2, 66.64, 215.98499999999999, 686.23, 697.1759999999999], [2, 66.64, 145.18, 696.334, 707.28], [2, 471.23999999999995, 565.25, 713.174, 735.066], [3, 147.56, 468.85999999999996, 45.467999999999996, 65.676], [3, 196.945, 419.47499999999997, 77.464, 93.462], [3, 232.64499999999998, 385.56, 93.462, 108.618]]
2026-08-10 12:48:11,259 INFO     29 [qwen-vl-text] ═══ DONE ═══ 153 positions, pages=2, time=50.2s
2026-08-10 12:48:11,259 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:48:11,269 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:48:11,269 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 12:48:11,269 INFO     29 [qwen-vl-text] positions(36): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:48:11,269 INFO     29 [qwen-vl-text] page grouping: [3], lines per page: [36]
2026-08-10 12:48:11,715 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:48:11,716 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1039
2026-08-10 12:48:11,717 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:48:11,717 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 211, \"bbox_end\": 246, \"encounter_dates\": [\"2025-12-26\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "舒张试验测试报告\n测试号：0022542899\n姓名：\n出生日期：\n身高：cm\n临床印象：支气管哮喘\n住址：内蒙古自治区乌兰察布\n科别：\n住院号：0022542899\n性别：男\n年龄：70 Years\n体重：47 kg\n吸烟史：否\n联系电话：\n主管医生：\n预计值 药前 %预计 药后1 改善率% 药后2 改善率% 药后3 改善率%\nFVC [L] 3.34 2.48 74.0 2.47 -0.28 2.52 1.90 2.59 4.57\nFEV 1 [L] 2.58 1.45 56.3 1.57 7.98 1.62 11.38 1.68 15.64\nFEV 1 % FVC [%] 83.77 58.60 70.0 63.46 8.29 64.05 9.30 64.81 10.59\nPEF [L/s] 7.27 5.34 73.4 5.97 11.92 6.55 22.75 6.30 18.12\nMEF 75 [L/s] 6.51 1.94 29.8 1.93 -0.49 2.25 15.90 2.48 27.48\nMEF 50 [L/s] 3.73 0.72 19.4 1.08 48.95 1.10 52.54 1.10 52.19\nMEF 25 [L/s] 1.15 0.25 21.9 0.37 49.20 0.35 40.24 0.38 51.20\nMMEF 75/25 [L/s] 2.89 0.60 20.9 0.82 35.86 0.83 37.61 0.89 46.55\nFET [s] 7.16 6.24 -12.85 7.29 1.83 7.07 -1.26\nFET PEF [s] 0.05 0.05 -10.65 0.04 -18.54 0.05 -3.25\nV backextrapol. % FVC [%] 2.82 3.10 10.19 2.50 -11.19 3.24 15.10\nDate 25/12/26 25/12/26 25/12/26 25/12/26\nTime 9:49:52 10:34:27 10:34:52 10:35:14\n结论：\n1. 中重度混合性肺通气功能障碍。\n轻度弥散功能障碍\n2. 支气管舒张试验阳性。\n(通过吸入沙丁胺醇气雾剂400ug，20min后FEV1 / FVC较基线增加大于12%，且绝对值增加大于200ml)。\n操作员：刘冉玲\n测试日期：2025/12/26 测试时间：10:35 编号：4",
    "role": "user"
  }
]
2026-08-10 12:48:11,719 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:48:11.718+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 32, "failed": 0, "current": {"6e5574f494b911f1bd9827cf206dfa2d": {"id": "6e5574f494b911f1bd9827cf206dfa2d", "doc_id": "6e14e31c94b911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWZWA222.pdf", "type": "pdf", "location": "\u9ea6\u6d4eWZWA222.pdf", "size": 9742831, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786365956617, "task_type": "dataflow", "root_trace_id": "bfb2f1d4af5749ba9e8b269686a95a2b", "root_traceparent": "00-bfb2f1d4af5749ba9e8b269686a95a2b-684dd3f6f78a8650-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:48:19,372 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:48:19,373 INFO     29 [qwen-vl-text] LLM output (len=1190):
{
  "exam_date": "2025-12-26",
  "report_date": "2025-12-26",
  "exam_name": "舒张试验测试",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "预计值 药前 %预计 药后1 改善率% 药后2 改善率% 药后3 改善率%\nFVC [L] 3.34 2.48 74.0 2.47 -0.28 2.52 1.90 2.59 4.57\nFEV 1 [L] 2.58 1.45 56.3 1.57 7.98 1.62 11.38 1.68 15.64\nFEV 1 % FVC [%] 83.77 58.60 70.0 63.46 8.29 64.05 9.30 64.81 10.59\nPEF [L/s] 7.27 5.34 73.4 5.97 11.92 6.55 22.75 6.30 18.12\nMEF 75 [L/s] 6.51 1.94 29.8 1.93 -0.49 2.25 15.90 2.48 27.48\nMEF 50 [L/s] 3.73 0.72 19.4 1.08 48.95 1.10 52.54 1.10 52.19\nMEF 25 [L/s] 1.15 0.25 21.9 0.37 49.20 0.35 40.24 0.38 51.20\nMMEF 75/25 [L/s] 2.89 0.60 20.9 0.82 35.86 0.83 37.61 0.89 46.55\nFET [s] 7.16 6.24 -12.85 7.29 1.83 7.07 -1.26\nFET PEF [s] 0.05 0.05 -10.65 0.04 -18.54 0.05 -3.25\nV backextrapol. % FVC [%] 2.82 3.10 10.19 2.50 -11.19 3.24 15.10\nDate 25/12/26 25/12/26 25/12/26 25/12/26\nTime 9:49:52 10:34:27 10:34:52 10:35:14",
  "conclusion": "1. 中重度混合性肺通气功能障碍。\n轻度弥散功能障碍\n2. 支气管舒张试验阳性。\n(通过吸入沙丁胺醇气雾剂400ug，20min后FEV1 / FVC较基线增加大于12%，且绝对值增加大于200ml)。",
  "physician": "刘冉玲",
  "reviewer": null
}
2026-08-10 12:48:19,383 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3667065, prompt_len=1760
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共36行）
["舒张试验测试报告", "测试号：0022542899", "姓名：", "出生日期：", "身高：cm", "临床印象：支气管哮喘", "住址：内蒙古自治区乌兰察布", "科别：", "住院号：0022542899", "性别：男", "年龄：70 Years", "体重：47 kg", "吸烟史：否", "联系电话：", "主管医生：", "预计值 药前 %预计 药后1 改善率% 药后2 改善率% 药后3 改善率%", "FVC [L] 3.34 2.48 74.0 2.47 -0.28 2.52 1.90 2.59 4.57", "FEV 1 [L] 2.58 1.45 56.3 1.57 7.98 1.62 11.38 1.68 15.64", "FEV 1 % FVC [%] 83.77 58.60 70.0 63.46 8.29 64.05 9.30 64.81 10.59", "PEF [L/s] 7.27 5.34 73.4 5.97 11.92 6.55 22.75 6.30 18.12", "MEF 75 [L/s] 6.51 1.94 29.8 1.93 -0.49 2.25 15.90 2.48 27.48", "MEF 50 [L/s] 3.73 0.72 19.4 1.08 48.95 1.10 52.54 1.10 52.19", "MEF 25 [L/s] 1.15 0.25 21.9 0.37 49.20 0.35 40.24 0.38 51.20", "MMEF 75/25 [L/s] 2.89 0.60 20.9 0.82 35.86 0.83 37.61 0.89 46.55", "FET [s] 7.16 6.24 -12.85 7.29 1.83 7.07 -1.26", "FET PEF [s] 0.05 0.05 -10.65 0.04 -18.54 0.05 -3.25", "V backextrapol. % FVC [%] 2.82 3.10 10.19 2.50 -11.19 3.24 15.10", "Date 25/12/26 25/12/26 25/12/26 25/12/26", "Time 9:49:52 10:34:27 10:34:52 10:35:14", "结论：", "1. 中重度混合性肺通气功能障碍。", "轻度弥散功能障碍", "2. 支气管舒张试验阳性。", "(通过吸入沙丁胺醇气雾剂400ug，20min后FEV1 / FVC较基线增加大于12%，且绝对值增加大于200ml)。", "操作员：刘冉玲", "测试日期：2025/12/26 测试时间：10:35 编号：4"]

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
2026-08-10 12:48:36,597 INFO     29 [qwen-vl-text] coord API raw response (len=3164):
[
	{"text": "舒张试验测试报告", "bbox": [405, 145, 605, 165]},
	{"text": "测试号：0022542899", "bbox": [158, 181, 400, 196], "label": "测试号"},
	{"text": "姓名：", "bbox": [158, 195, 202, 208], "label": "姓名"},
	{"text": "出生日期：", "bbox": [158, 208, 235, 222], "label": "出生日期"},
	{"text": "身高：cm", "bbox": [158, 222, 366, 237], "label": "身高"},
	{"text": "临床印象：支气管哮喘", "bbox": [158, 237, 400, 251], "label": "临床印象"},
	{"text": "住址：内蒙古自治区乌兰察布", "bbox": [158, 251, 482, 265], "label": "住址"},
	{"text": "科别：", "bbox": [158, 265, 200, 279], "label": "科别"},
	{"text": "住院号：0022542899", "bbox": [508, 181, 741, 196], "label": "住院号"},
	{"text": "性别：男", "bbox": [508, 195, 676, 208], "label": "性别"},
	{"text": "年龄：70 Years", "bbox": [508, 208, 724, 222], "label": "年龄"},
	{"text": "体重：47 kg", "bbox": [508, 222, 700, 237], "label": "体重"},
	{"text": "吸烟史：否", "bbox": [508, 237, 676, 251], "label": "吸烟史"},
	{"text": "联系电话：", "bbox": [508, 251, 580, 265], "label": "联系电话"},
	{"text": "主管医生：", "bbox": [508, 265, 580, 279], "label": "主管医生"},
	{"text": "预计值 药前 %预计 药后1 改善率% 药后2 改善率% 药后3 改善率%", "bbox": [275, 295, 950, 312], "label": "标题行"},
	{"text": "FVC [L] 3.34 2.48 74.0 2.47 -0.28 2.52 1.90 2.59 4.57", "bbox": [35, 327, 950, 342], "label": "数据行"},
	{"text": "FEV 1 [L] 2.58 1.45 56.3 1.57 7.98 1.62 11.38 1.68 15.64", "bbox": [35, 342, 950, 356], "label": "数据行"},
	{"text": "FEV 1 % FVC [%] 83.77 58.60 70.0 63.46 8.29 64.05 9.30 64.81 10.59", "bbox": [35, 356, 950, 370], "label": "数据行"},
	{"text": "PEF [L/s] 7.27 5.34 73.4 5.97 11.92 6.55 22.75 6.30 18.12", "bbox": [35, 370, 950, 384], "label": "数据行"},
	{"text": "MEF 75 [L/s] 6.51 1.94 29.8 1.93 -0.49 2.25 15.90 2.48 27.48", "bbox": [35, 384, 950, 398], "label": "数据行"},
	{"text": "MEF 50 [L/s] 3.73 0.72 19.4 1.08 48.95 1.10 52.54 1.10 52.19", "bbox": [35, 398, 950, 412], "label": "数据行"},
	{"text": "MEF 25 [L/s] 1.15 0.25 21.9 0.37 49.20 0.35 40.24 0.38 51.20", "bbox": [35, 412, 950, 426], "label": "数据行"},
	{"text": "MMEF 75/25 [L/s] 2.89 0.60 20.9 0.82 35.86 0.83 37.61 0.89 46.55", "bbox": [35, 426, 950, 440], "label": "数据行"},
	{"text": "FET [s] 7.16 6.24 -12.85 7.29 1.83 7.07 -1.26", "bbox": [35, 440, 950, 454], "label": "数据行"},
	{"text": "FET PEF [s] 0.05 0.05 -10.65 0.04 -18.54 0.05 -3.25", "bbox": [35, 454, 950, 468], "label": "数据行"},
	{"text": "V backextrapol. % FVC [%] 2.82 3.10 10.19 2.50 -11.19 3.24 15.10", "bbox": [35, 468, 950, 482], "label": "数据行"},
	{"text": "Date 25/12/26 25/12/26 25/12/26 25/12/26", "bbox": [35, 492, 858, 506], "label": "日期行"},
	{"text": "Time 9:49:52 10:34:27 10:34:52 10:35:14", "bbox": [35, 506, 858, 519], "label": "时间行"},
	{"text": "结论：", "bbox": [35, 732, 95, 750], "label": "结论标题"},
	{"text": "1. 中重度混合性肺通气功能障碍。", "bbox": [88, 755, 347, 770], "label": "结论1"},
	{"text": "轻度弥散功能障碍", "bbox": [88, 770, 226, 784], "label": "结论2"},
	{"text": "2. 支气管舒张试验阳性。", "bbox": [88, 784, 277, 797], "label": "结论3"},
	{"text": "(通过吸入沙丁胺醇气雾剂400ug，20min后FEV1 / FVC较基线增加大于12%，且绝对值增加大于200ml)。", "bbox": [97, 791, 870, 808], "label": "结论4"},
	{"text": "操作员：刘冉玲", "bbox": [794, 938, 958, 971], "label": "操作员"},
	{"text": "测试日期：2025/12/26 测试时间：10:35 编号：4", "bbox": [690, 30, 961, 40], "label": "测试信息"}
]
2026-08-10 12:48:36,597 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=17.2s
2026-08-10 12:48:36,597 INFO     29 [qwen-vl-text] coord item[0]: text=舒张试验测试报告, bbox=[405, 145, 605, 165]
2026-08-10 12:48:36,597 INFO     29 [qwen-vl-text] coord item[1]: text=测试号：0022542899, bbox=[158, 181, 400, 196]
2026-08-10 12:48:36,597 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[158, 195, 202, 208]
2026-08-10 12:48:36,597 INFO     29 [qwen-vl-text] coord item[3]: text=出生日期：, bbox=[158, 208, 235, 222]
2026-08-10 12:48:36,597 INFO     29 [qwen-vl-text] coord item[4]: text=身高：cm, bbox=[158, 222, 366, 237]
2026-08-10 12:48:36,597 INFO     29 [qwen-vl-text] coord item[5]: text=临床印象：支气管哮喘, bbox=[158, 237, 400, 251]
2026-08-10 12:48:36,597 INFO     29 [qwen-vl-text] coord item[6]: text=住址：内蒙古自治区乌兰察布, bbox=[158, 251, 482, 265]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[7]: text=科别：, bbox=[158, 265, 200, 279]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[8]: text=住院号：0022542899, bbox=[508, 181, 741, 196]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[9]: text=性别：男, bbox=[508, 195, 676, 208]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[10]: text=年龄：70 Years, bbox=[508, 208, 724, 222]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[11]: text=体重：47 kg, bbox=[508, 222, 700, 237]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[12]: text=吸烟史：否, bbox=[508, 237, 676, 251]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[13]: text=联系电话：, bbox=[508, 251, 580, 265]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[14]: text=主管医生：, bbox=[508, 265, 580, 279]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[15]: text=预计值 药前 %预计 药后1 改善率% 药后2 改善率% 药后3 改善率%, bbox=[275, 295, 950, 312]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[16]: text=FVC [L] 3.34 2.48 74.0 2.47 -0.28 2.52 1.90 2.59 4.57, bbox=[35, 327, 950, 342]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[17]: text=FEV 1 [L] 2.58 1.45 56.3 1.57 7.98 1.62 11.38 1.68 15.64, bbox=[35, 342, 950, 356]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[18]: text=FEV 1 % FVC [%] 83.77 58.60 70.0 63.46 8.29 64.05 9.30 64.81 10.59, bbox=[35, 356, 950, 370]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[19]: text=PEF [L/s] 7.27 5.34 73.4 5.97 11.92 6.55 22.75 6.30 18.12, bbox=[35, 370, 950, 384]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[20]: text=MEF 75 [L/s] 6.51 1.94 29.8 1.93 -0.49 2.25 15.90 2.48 27.48, bbox=[35, 384, 950, 398]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[21]: text=MEF 50 [L/s] 3.73 0.72 19.4 1.08 48.95 1.10 52.54 1.10 52.19, bbox=[35, 398, 950, 412]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[22]: text=MEF 25 [L/s] 1.15 0.25 21.9 0.37 49.20 0.35 40.24 0.38 51.20, bbox=[35, 412, 950, 426]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[23]: text=MMEF 75/25 [L/s] 2.89 0.60 20.9 0.82 35.86 0.83 37.61 0.89 46.55, bbox=[35, 426, 950, 440]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[24]: text=FET [s] 7.16 6.24 -12.85 7.29 1.83 7.07 -1.26, bbox=[35, 440, 950, 454]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[25]: text=FET PEF [s] 0.05 0.05 -10.65 0.04 -18.54 0.05 -3.25, bbox=[35, 454, 950, 468]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[26]: text=V backextrapol. % FVC [%] 2.82 3.10 10.19 2.50 -11.19 3.24 15.10, bbox=[35, 468, 950, 482]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[27]: text=Date 25/12/26 25/12/26 25/12/26 25/12/26, bbox=[35, 492, 858, 506]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[28]: text=Time 9:49:52 10:34:27 10:34:52 10:35:14, bbox=[35, 506, 858, 519]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[29]: text=结论：, bbox=[35, 732, 95, 750]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[30]: text=1. 中重度混合性肺通气功能障碍。, bbox=[88, 755, 347, 770]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[31]: text=轻度弥散功能障碍, bbox=[88, 770, 226, 784]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[32]: text=2. 支气管舒张试验阳性。, bbox=[88, 784, 277, 797]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[33]: text=(通过吸入沙丁胺醇气雾剂400ug，20min后FEV1 / FVC较基线增加大于12%，且绝对值增加大于200ml)。, bbox=[97, 791, 870, 808]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[34]: text=操作员：刘冉玲, bbox=[794, 938, 958, 971]
2026-08-10 12:48:36,598 INFO     29 [qwen-vl-text] coord item[35]: text=测试日期：2025/12/26 测试时间：10:35 编号：4, bbox=[690, 30, 961, 40]
2026-08-10 12:48:36,599 INFO     29 [qwen-vl-text] page=3 — 36/36 coords, api_time=17.2s
2026-08-10 12:48:36,599 INFO     29 [qwen-vl-text] new_positions (36):
[[3, 240.975, 359.97499999999997, 122.08999999999999, 138.93], [3, 94.00999999999999, 238.0, 152.402, 165.03199999999998], [3, 94.00999999999999, 120.19, 164.19, 175.136], [3, 94.00999999999999, 139.825, 175.136, 186.924], [3, 94.00999999999999, 217.76999999999998, 186.924, 199.554], [3, 94.00999999999999, 238.0, 199.554, 211.34199999999998], [3, 94.00999999999999, 286.78999999999996, 211.34199999999998, 223.13], [3, 94.00999999999999, 119.0, 223.13, 234.91799999999998], [3, 302.26, 440.895, 152.402, 165.03199999999998], [3, 302.26, 402.21999999999997, 164.19, 175.136], [3, 302.26, 430.78, 175.136, 186.924], [3, 302.26, 416.5, 186.924, 199.554], [3, 302.26, 402.21999999999997, 199.554, 211.34199999999998], [3, 302.26, 345.09999999999997, 211.34199999999998, 223.13], [3, 302.26, 345.09999999999997, 223.13, 234.91799999999998], [3, 163.625, 565.25, 248.39, 262.704], [3, 20.825, 565.25, 275.334, 287.964], [3, 20.825, 565.25, 287.964, 299.752], [3, 20.825, 565.25, 299.752, 311.53999999999996], [3, 20.825, 565.25, 311.53999999999996, 323.328], [3, 20.825, 565.25, 323.328, 335.116], [3, 20.825, 565.25, 335.116, 346.904], [3, 20.825, 565.25, 346.904, 358.692], [3, 20.825, 565.25, 358.692, 370.47999999999996], [3, 20.825, 565.25, 370.47999999999996, 382.268], [3, 20.825, 565.25, 382.268, 394.056], [3, 20.825, 565.25, 394.056, 405.844], [3, 20.825, 510.51, 414.264, 426.05199999999996], [3, 20.825, 510.51, 426.05199999999996, 436.998], [3, 20.825, 56.525, 616.3439999999999, 631.5], [3, 52.36, 206.465, 635.7099999999999, 648.34], [3, 52.36, 134.47, 648.34, 660.1279999999999], [3, 52.36, 164.815, 660.1279999999999, 671.074], [3, 57.714999999999996, 517.65, 666.0219999999999, 680.336], [3, 472.43, 570.01, 789.7959999999999, 817.582], [3, 410.54999999999995, 571.795, 25.259999999999998, 33.68]]
2026-08-10 12:48:36,599 INFO     29 [qwen-vl-text] ═══ DONE ═══ 36 positions, pages=1, time=25.3s
2026-08-10 12:48:36,606 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 12:48:36,606 INFO     29 [Trace] task=6e5574f4 | doc=麦济WZWA222.pdf | Extractor:ExaminationReport | outputs={"chunks": "2 items, types={'ExaminationReport': 2}", "html": "", "json": "263 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_Medication\": 1}"}
2026-08-10 12:48:36,606 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 12:48:36,610 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:48:36,610 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:48:37,485 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:48:37,490 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 12:48:37,490 INFO     29 [Trace] task=6e5574f4 | doc=麦济WZWA222.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "263 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_Medication\": 1}"}
2026-08-10 12:48:37,490 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 12:48:37,491 INFO     29 [ChunkMerger] Merged 5 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 2, 'Extractor:Progress': 1} (filtered 6 noise chunks)
2026-08-10 12:48:37,499 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 12:48:37,500 INFO     29 [Trace] task=6e5574f4 | doc=麦济WZWA222.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "5 items, types={'OutpatientRecord': 2, 'MedicationRecord': 1, 'ExaminationReport': 2}", "name": "麦济WZWA222.pdf"}
2026-08-10 12:48:37,500 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 12:48:37,555 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786365958167, 'update_date': datetime.datetime(2026, 8, 10, 12, 45, 58), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1000856, 'status': '1'}
2026-08-10 12:48:38,005 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=内蒙古医科大学附属医院门诊病历
姓名：
年龄：70岁
诊疗号：0022542899
民族：汉族
性别：男性
科室：呼吸内科门诊
联系电话：
身份：
4
病情：
就诊状态：
就诊时间：2025-12-26 08:41
生命体征（需要时）：
体温：℃ 脉搏：74次/分 呼吸：次/分 血压：/mmHg
主诉：气短10余年，加重伴咳嗽咳痰1月
现病史：气短10余年，规律用药（信必可都保320，早晚各一吸），加重伴咳
嗽咳痰1月，血氧饱和度97%。自己输液治疗（含激素）10余天，气
短、咳嗽咳痰症状无改善。
既往史：患者平素身体一般，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎
有，10年，吸烟史无，无过敏史。
体格检查：发育正常，营养中等，体型正力，双肺呼吸音弱，双肺未闻及啰
音，双下肢无水肿，体重kg：
辅助检查：肺功能：FVC 74%，FEV1 56.3%，FEV1/FVC 58.6%，舒张试验阳性。
过敏史：
初步诊断（西医）：1.支气管哮喘（急性发作期）
初步诊断（中医）：
治疗方案：1.胸部CT、血常规、肺功能、心电图；2.建议心内科就诊。
CT胸部
常规心电图检查
血常规
肾功3项
肝功9项
肺通气功能检查(肺功能)
肺容积检查(肺功能)
肺弥散功能检查(肺功能) 一次性肺功能仪用过滤嘴
肺通气功能检查(肺功能) 一次性肺功能仪用过滤嘴
布地奈德福莫特罗吸入粉雾剂(11)《每支60
吸，每吸含布地奈德320μg和富马酸福莫特
罗9.0μg>
用量：1.000吸/次
用法：吸入，二次/日，1天
醋酸泼尼松片<5mg>
用量：2.000片/次
用法：口服，一次/日，7天
签名：王美玲
---
丰镇市医院
诊断证明书
姓名：
年龄：
性别：男
病案号：10017815
印象：1.慢性支气管炎急性加重期2.支气管哮喘3.慢性胃炎4.肺气肿
处理意见：住院
医师：宋志杰
日期：2024年07月22日
地址：呼和浩特市通道北街一号
电话：0471--3451056
---
东吉轩药店
日期: 2026.01.23
09: 23: 37
单号: 20260123070132
品名 规格 单价 数量 总计
布地奈德福莫特罗吸入气雾剂
(II)320ug/9ug/吸 60 吸/支
268.00 2 536.00
应收金额: 536.00
实收金额: 536.00
优惠金额: 0.00
找零金额: 0.00
会员:
日期: 2026.01.23
09: 23: 3
单号: 20260123070132
---
肺常规通气检查报告
测试号：0022542899
姓名：
出生日期：
身高：165 cm
临床印象：支气管哮喘
住址：内蒙古自治区乌兰察布
科别：
住院号：0022542899
性别：男
年龄：70 Years
体重：47 kg
吸烟史：否
联系电话：
主管医生：
F/V ex
F/V in
Vol [L]
Vol%VCmax
VCmax
Time [s]
Vol [L]
Time [s]
FVC
[L]
3.34
2.48
74.0
FEV 1
[L]
2.58
1.45
56.3
FEV 2
[L]
1.82
FEV 3
[L]
2.06
FEV6
[L]
2.45
FEV 1 % FVC
[%]
83.77
58.60
70.0
FEV 1 % VC MAX
[%]
74.61
58.60
78.5
PEF
[L/s]
7.27
5.34
73.4
MEF 75
[L/s]
6.51
1.94
29.8
MEF 50
[L/s]
3.73
0.72
19.4
MEF 25
[L/s]
1.15
0.25
21.9
MMEF 75/25
[L/s]
2.89
0.60
20.9
FET
[s]
7.16
FET PEF
[s]
0.05
V backextrapolation ex
[L]
0.07
V backextrapol. % FVC
[%]
2.82
MVV
[L/min]
101.83
37.40
36.7
FEV 1 % VC MAX
[%]
74.61
58.60
78.5
VC EX
[L]
3.46
2.48
71.6
FRV
[L]
0.93
IRV
[L]
0.80
VT
[L]
0.34
1.65
491.4
IC
[L]
2.53
2.45
96.9
BF
[1/min]
20.00
13.38
66.9
MV
[L/min]
6.71
22.08
328.9
VC MAX
[L]
3.46
2.48
71.6
Pred
TEST1
%/Pred
TEST2
%/Pred
TEST3
%/Pred
Date
25/12/26
Time
9:49:52
结论：
1. 中重度混合性肺通气功能障碍。
轻度弥散功能障碍
操作员：刘角玲
内蒙古医科大学附属医院肺功能报告单
地址：呼和浩特市通道北街一号
电话：0471--3451056
---
舒张试验测试报告
测试号：0022542899
姓名：
出生日期：
身高：cm
临床印象：支气管哮喘
住址：内蒙古自治区乌兰察布
科别：
住院号：0022542899
性别：男
年龄：70 Years
体重：47 kg
吸烟史：否
联系电话：
主管医生：
预计值 药前 %预计 药后1 改善率% 药后2 改善率% 药后3 改善率%
FVC [L] 3.34 2.48 74.0 2.47 -0.28 2.52 1.90 2.59 4.57
FEV 1 [L] 2.58 1.45 56.3 1.57 7.98 1.62 11.38 1.68 15.64
FEV 1 % FVC [%] 83.77 58.60 70.0 63.46 8.29 64.05 9.30 64.81 10.59
PEF [L/s] 7.27 5.34 73.4 5.97 11.92 6.55 22.75 6.30 18.12
MEF 75 [L/s] 6.51 1.94 29.8 1.93 -0.49 2.25 15.90 2.48 27.48
MEF 50 [L/s] 3.73 0.72 19.4 1.08 48.95 1.10 52.54 1.10 52.19
MEF 25 [L/s] 1.15 0.25 21.9 0.37 49.20 0.35 40.24 0.38 51.20
MMEF 75/25 [L/s] 2.89 0.60 20.9 0.82 35.86 0.83 37.61 0.89 46.55
FET [s] 7.16 6.24 -12.85 7.29 1.83 7.07 -1.26
FET PEF [s] 0.05 0.05 -10.65 0.04 -18.54 0.05 -3.25
V backextrapol. % FVC [%] 2.82 3.10 10.19 2.50 -11.19 3.24 15.10
Date 25/12/26 25/12/26 25/12/26 25/12/26
Time 9:49:52 10:34:27 10:34:52 10:35:14
结论：
1. 中重度混合性肺通气功能障碍。
轻度弥散功能障碍
2. 支气管舒张试验阳性。
(通过吸入沙丁胺醇气雾剂400ug，20min后FEV1 / FVC较基线增加大于12%，且绝对值增加大于200ml)。
操作员：刘冉玲
测试日期：2025/12/26 测试时间：10:35 编号：4
2026-08-10 12:48:38,376 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 12:48:38,377 INFO     29 [Trace] task=6e5574f4 | doc=麦济WZWA222.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "5 items, types={'OutpatientRecord': 2, 'MedicationRecord': 1, 'ExaminationReport': 2}", "name": "麦济WZWA222.pdf", "embedding_token_consumption": 2506}
2026-08-10 12:48:38,377 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 12:48:38,551 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 12:48:38,552 INFO     29 [Trace] task=6e5574f4 | doc=麦济WZWA222.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":5,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 12:48:38,554 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:48:38,555 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:48:38,555 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:48:38,555 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:48:38,555 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:48:38,559 INFO     29 set_progress(6e5574f494b911f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 12:48:38 [DOC Engine]:
Start to index...
2026-08-10 12:48:38,575 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.011s]
2026-08-10 12:48:38,581 INFO     29 set_progress(6e5574f494b911f1bd9827cf206dfa2d), progress: 0.8200000000000001, progress_msg: 
2026-08-10 12:48:38,594 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.010s]
2026-08-10 12:48:38,602 INFO     29 set_progress(6e5574f494b911f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 12:48:38 Indexing done (0.04s). Task done (153.81s)
2026-08-10 12:48:38,605 INFO     29 [Done], chunks(5), token(2506), elapsed:153.81
2026-08-10 12:48:38,689 INFO     29 handle_task done for task {"id": "6e5574f494b911f1bd9827cf206dfa2d", "doc_id": "6e14e31c94b911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWZWA222.pdf", "type": "pdf", "location": "\u9ea6\u6d4eWZWA222.pdf", "size": 9742831, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786365956617, "task_type": "dataflow", "root_trace_id": "bfb2f1d4af5749ba9e8b269686a95a2b", "root_traceparent": "00-bfb2f1d4af5749ba9e8b269686a95a2b-684dd3f6f78a8650-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
