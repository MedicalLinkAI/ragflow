# 基准结果：麦济WZWA222.pdf

## 基本信息

- 文件：`麦济WZWA222.pdf`
- 大小：9514.5 KB
- PDF 总页数：5
- doc_id：`c9526904909311f1a3da71efcdd7cc1f`
- 上传方式：existing
- 状态：run=None (code=None)  progress=None
- 开始时间：2026-08-05T14:31:23  完成时间：2026-08-05T14:31:24  耗时：0.9s
- progress_msg：`06:09:08 Indexing done (0.03s). Task done (147.34s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 7bdaf56a | 1 | 1-1 | 内蒙古医科大学附属医院门诊病历 姓名： 年龄：70岁 诊疗号：002254289 |
| 2 | 0b3bd742 | 2 | 2-3 | 丰镇市医院 诊断证明书 姓名： 年龄： 性别：男 病案号：10017815 印象 |
| 3 | 6dff757e | 2 | 3-4 | 肺常规通气检查报告 测试号：0022542899 姓名： 出生日期： 身高：16 |
| 4 | 661fa862 | 1 | 5-5 | 东吉轩药店 日期: 2026.01.23 09: 23: 37 单号: 2026 |

- chunks 总数：4
- 各 chunk 页数合计（含跨页重复）：6
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
| ExaminationReport | 检查报告 | 1 | 1 | 1 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 2, "ExaminationReport": 1, "MedicationRecord": 1}`
- ChunkMerger：`{"found": true, "merged": 4, "sources": 8, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 2, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1}, "filtered_noise": 5}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-05 06:09:06,204 INFO     29 [ChunkMerger] Merged 4 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-05 06:06:26,918 INFO     29 handle_task begin for task {"id": "c9e5a6ba909311f1a3da71efcdd7cc1f", "doc_id": "c9526904909311f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWZWA222.pdf", "type": "pdf", "location": "\u9ea6\u6d4eWZWA222.pdf", "size": 9742831, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785909984712, "task_type": "dataflow", "root_trace_id": "61b0a1cf64e14ac9b4fd9e1374842905", "root_traceparent": "00-61b0a1cf64e14ac9b4fd9e1374842905-58f4c254cd5a4a04-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-05 06:06:27,134 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-05 06:06:27,179 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-05 06:06:27,219 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-05 06:06:27,219 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-05 06:06:27,227 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-05 06:06:27,228 INFO     29 ============================================================
2026-08-05 06:06:27,228 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-05 06:06:27,228 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-05 06:06:27,228 INFO     29 ============================================================
2026-08-05 06:06:27,228 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-05 06:06:27,228 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-05 06:06:27,229 INFO     29 No torch found.
2026-08-05 06:06:28,331 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=5
2026-08-05 06:06:28,935 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5280516, prompt_len=644
2026-08-05 06:06:32,356 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-12-26"}
```
2026-08-05 06:06:32,356 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2025-12-26
2026-08-05 06:06:32,378 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5280516, prompt_len=401
2026-08-05 06:06:38,778 INFO     29 [qwen-vl-parser] text API response (len=842):
["内蒙古医科大学附属医院门诊病历", "姓名：", "年龄：70岁", "诊疗号：0022542899", "民族：汉族", "性别：男性", "科室：呼吸内科门诊", "联系电话：", "身份：", "4", "病情：", "就诊状态：", "就诊时间：2025-12-26 08:41", "生命体征（需要时）：", "体温：℃ 脉搏：74次/分 呼吸：次/分 血压：/mmHg", "主诉：气短10余年，加重伴咳嗽咳痰1月", "现病史：气短10余年，规律用药（信必可都保320，早晚各一吸），加重伴咳", "嗽咳痰1月，血氧饱和度97%。自己输液治疗（含激素）10余天，气", "短、咳嗽咳痰症状无改善。", "既往史：患者平素身体一般，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "有，10年，吸烟史无，无过敏史。", "体格检查：发育正常，营养中等，体型正力，双肺呼吸音弱，双肺未闻及啰", "音，双下肢无水肿，体重kg：", "辅助检查：肺功能：FVC 74%，FEV1 56.3%，FEV1/FVC 58.6%，舒张试验阳性。", "过敏史：", "初步诊断（西医）：1.支气管哮喘（急性发作期）", "初步诊断（中医）：", "治疗方案：1.胸部CT、血常规、肺功能、心电图；2.建议心内科就诊。", "CT胸部", "常规心电图检查", "血常规", "肾功3项", "肝功9项", "肺通气功能检查(肺功能)", "肺容积检查(肺功能)", "肺弥散功能检查(肺功能) 一次性肺功能仪用过滤嘴", "肺通气功能检查(肺功能) 一次性肺功能仪用过滤嘴", "布地奈德福莫特罗吸入粉雾剂(11)《每支60", "吸，每吸含布地奈德320μg和富马酸福莫特", "罗9.0μg>", "用量：1.000吸/次", "用法：吸入，二次/日，1天", "醋酸泼尼松片<5mg>", "用量：2.000片/次", "用法：口服，一次/日，7天", "签名：王美玲"]
2026-08-05 06:06:38,778 INFO     29 [qwen-vl-parser] page=1 text: 46 lines (bbox 0-45)
2026-08-05 06:06:38,778 INFO     29 [qwen-vl-parser] page=1 text: 46 sections
2026-08-05 06:06:38,908 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=572019, prompt_len=644
2026-08-05 06:06:40,335 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-07-22"}
```
2026-08-05 06:06:40,336 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=2024-07-22
2026-08-05 06:06:40,347 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=572019, prompt_len=401
2026-08-05 06:06:41,373 INFO     29 [qwen-vl-parser] text API response (len=133):
["丰镇市医院", "诊断证明书", "姓名：", "年龄：", "性别：男", "病案号：10017815", "印象：1.慢性支气管炎急性加重期2.支气管哮喘3.慢性胃炎4.肺气肿", "处理意见：住院", "医师：宋志杰", "日期：2024年07月22日"]
2026-08-05 06:06:41,373 INFO     29 [qwen-vl-parser] page=2 text: 10 lines (bbox 46-55)
2026-08-05 06:06:41,373 INFO     29 [qwen-vl-parser] page=2 text: 10 sections
2026-08-05 06:06:41,742 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2180949, prompt_len=644
2026-08-05 06:06:42,272 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T06:06:42.272+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 23, "failed": 0, "current": {"c9e5a6ba909311f1a3da71efcdd7cc1f": {"id": "c9e5a6ba909311f1a3da71efcdd7cc1f", "doc_id": "c9526904909311f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWZWA222.pdf", "type": "pdf", "location": "\u9ea6\u6d4eWZWA222.pdf", "size": 9742831, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785909984712, "task_type": "dataflow", "root_trace_id": "61b0a1cf64e14ac9b4fd9e1374842905", "root_traceparent": "00-61b0a1cf64e14ac9b4fd9e1374842905-58f4c254cd5a4a04-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 06:06:43,732 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-05 06:06:43,732 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-05 06:06:43,741 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2180949, prompt_len=401
2026-08-05 06:06:53,375 INFO     29 [qwen-vl-parser] text API response (len=1369):
["地址：呼和浩特市通道北街一号", "电话：0471--3451056", "肺常规通气检查报告", "测试号：0022542899", "姓名：", "出生日期：", "身高：165 cm", "临床印象：支气管哮喘", "住址：内蒙古自治区乌兰察布", "科别：", "住院号：0022542899", "性别：男", "年龄：70 Years", "体重：47 kg", "吸烟史：否", "联系电话：", "主管医生：", "F/V ex", "F/V in", "Vol [L]", "Vol%VCmax", "VCmax", "Time [s]", "Vol [L]", "Time [s]", "FVC", "[L]", "3.34", "2.48", "74.0", "FEV 1", "[L]", "2.58", "1.45", "56.3", "FEV 2", "[L]", "1.82", "FEV 3", "[L]", "2.06", "FEV6", "[L]", "2.45", "FEV 1 % FVC", "[%]", "83.77", "58.60", "70.0", "FEV 1 % VC MAX", "[%]", "74.61", "58.60", "78.5", "PEF", "[L/s]", "7.27", "5.34", "73.4", "MEF 75", "[L/s]", "6.51", "1.94", "29.8", "MEF 50", "[L/s]", "3.73", "0.72", "19.4", "MEF 25", "[L/s]", "1.15", "0.25", "21.9", "MMEF 75/25", "[L/s]", "2.89", "0.60", "20.9", "FET", "[s]", "7.16", "FET PEF", "[s]", "0.05", "V backextrapolation ex", "[L]", "0.07", "V backextrapol. % FVC", "[%]", "2.82", "MVV", "[L/min]", "101.83", "37.40", "36.7", "FEV 1 % VC MAX", "[%]", "74.61", "58.60", "78.5", "VC EX", "[L]", "3.46", "2.48", "71.6", "FRV", "[L]", "0.93", "IRV", "[L]", "0.80", "VT", "[L]", "0.34", "1.65", "491.4", "IC", "[L]", "2.53", "2.45", "96.9", "BF", "[1/min]", "20.00", "13.38", "66.9", "MV", "[L/min]", "6.71", "22.08", "328.9", "VC MAX", "[L]", "3.46", "2.48", "71.6", "Date", "25/12/26", "Time", "9:49:52", "结论：", "1. 中重度混合性肺通气功能障碍。", "轻度弥散功能障碍", "操作员：刘角玲"]
2026-08-05 06:06:53,376 INFO     29 [qwen-vl-parser] page=3 text: 145 lines (bbox 56-200)
2026-08-05 06:06:53,376 INFO     29 [qwen-vl-parser] page=3 text: 145 sections
2026-08-05 06:06:53,838 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2753800, prompt_len=644
2026-08-05 06:06:56,199 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-12-26"
}
```
2026-08-05 06:06:56,200 INFO     29 [qwen-vl-parser] page=4 classify=table report_date=2025-12-26
2026-08-05 06:06:56,217 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2753800, prompt_len=756
2026-08-05 06:07:03,433 INFO     29 [qwen-vl-parser] table API response (len=1187):
\begin{tabular}{lcccccccccc}
\hline
& 预计值 & 药前 & \%预计 & 药后1 & 改善率\% & 药后2 & 改善率\% & 药后3 & 改善率\% \\
\hline
FVC & [L] & 3.34 & 2.48 & 74.0 & 2.47 & -0.28 & 2.52 & 1.90 & 2.59 & 4.57 \\
FEV 1 & [L] & 2.58 & 1.45 & 56.3 & 1.57 & 7.98 & 1.62 & 11.38 & 1.68 & 15.64 \\
FEV 1 \% FVC & [\%] & 83.77 & 58.60 & 70.0 & 63.46 & 8.29 & 64.05 & 9.30 & 64.81 & 10.59 \\
PEF & [L/s] & 7.27 & 5.34 & 73.4 & 5.97 & 11.92 & 6.55 & 22.75 & 6.30 & 18.12 \\
MEF 75 & [L/s] & 6.51 & 1.94 & 29.8 & 1.93 & -0.49 & 2.25 & 15.90 & 2.48 & 27.48 \\
MEF 50 & [L/s] & 3.73 & 0.72 & 19.4 & 1.08 & 48.95 & 1.10 & 52.54 & 1.10 & 52.19 \\
MEF 25 & [L/s] & 1.15 & 0.25 & 21.9 & 0.37 & 49.20 & 0.35 & 40.24 & 0.38 & 51.20 \\
MMEF 75/25 & [L/s] & 2.89 & 0.60 & 20.9 & 0.82 & 35.86 & 0.83 & 37.61 & 0.89 & 46.55 \\
FET & [s] & & & & 6.24 & -12.85 & 7.29 & 1.83 & 7.07 & -1.26 \\
FET PEF & [s] & & & & 0.05 & -10.65 & 0.04 & -18.54 & 0.05 & -3.25 \\
V backextrapol. \% FVC & [\%] & & & & 3.10 & 10.19 & 2.50 & -11.19 & 3.24 & 15.10 \\
\hline
Date & & & & & & & & & & \\
Time & & 25/12/26 & 9:49:52$\downarrow$ & & 25/12/26 & 10:34:27. & & 25/12/26 & 10:34:52. & \\
& & & & & & & & 25/12/26 & 10:35:14. & \\
\hline
\end{tabular}
2026-08-05 06:07:03,436 INFO     29 [qwen-vl-parser] page=4 table: 22 LaTeX lines (bbox 201-222)
2026-08-05 06:07:03,436 INFO     29 [qwen-vl-parser] page=4 table: 22 sections
2026-08-05 06:07:03,769 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1801140, prompt_len=644
2026-08-05 06:07:05,526 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 06:07:05,527 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-05 06:07:05,548 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1801140, prompt_len=401
2026-08-05 06:07:07,835 INFO     29 [qwen-vl-parser] text API response (len=263):
["东吉轩药店", "日期: 2026.01.23", "09: 23: 37", "单号: 20260123070132", "品名 规格 单价 数量 总计", "布地奈德福莫特罗吸入气雾剂", "(II)320ug/9ug/吸 60 吸/支", "268.00 2 536.00", "应收金额: 536.00", "实收金额: 536.00", "优惠金额: 0.00", "找零金额: 0.00", "会员:", "日期: 2026.01.23", "09: 23: 3", "单号: 20260123070132"]
2026-08-05 06:07:07,835 INFO     29 [qwen-vl-parser] page=5 text: 16 lines (bbox 223-238)
2026-08-05 06:07:07,836 INFO     29 [qwen-vl-parser] page=5 text: 16 sections
2026-08-05 06:07:07,836 INFO     29 [qwen-vl-parser] parse_pdf done: 239 sections from 5 pages.
2026-08-05 06:07:07,845 INFO     29 Close text detector.
2026-08-05 06:07:08,226 INFO     29 Close text recognizer.
2026-08-05 06:07:08,575 INFO     29 Close recognizer.
2026-08-05 06:07:08,879 INFO     29 Close recognizer.
2026-08-05 06:07:09,248 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-05 06:07:09,248 INFO     29 [Trace] task=c9e5a6ba | doc=麦济WZWA222.pdf | Parser:MedLink | outputs={"html": "", "json": "239 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "json"}
2026-08-05 06:07:09,248 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-05 06:07:09,263 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 06:07:09,263 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。只有主诉，病史的也属于OutpatientRecord（门诊病历）\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 内蒙古医科大学附属医院门诊病历\n[BBOX-1] 姓名：\n[BBOX-2] 年龄：70岁\n[BBOX-3] 诊疗号：0022542899\n[BBOX-4] 民族：汉族\n[BBOX-5] 性别：男性\n[BBOX-6] 科室：呼吸内科门诊\n[BBOX-7] 联系电话：\n[BBOX-8] 身份：\n[BBOX-9] 4\n[BBOX-10] 病情：\n[BBOX-11] 就诊状态：\n[BBOX-12] 就诊时间：2025-12-26 08:41\n[BBOX-13] 生命体征（需要时）：\n[BBOX-14] 体温：℃ 脉搏：74次/分 呼吸：次/分 血压：/mmHg\n[BBOX-15] 主诉：气短10余年，加重伴咳嗽咳痰1月\n[BBOX-16] 现病史：气短10余年，规律用药（信必可都保320，早晚各一吸），加重伴咳\n[BBOX-17] 嗽咳痰1月，血氧饱和度97%。自己输液治疗（含激素）10余天，气\n[BBOX-18] 短、咳嗽咳痰症状无改善。\n[BBOX-19] 既往史：患者平素身体一般，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎\n[BBOX-20] 有，10年，吸烟史无，无过敏史。\n[BBOX-21] 体格检查：发育正常，营养中等，体型正力，双肺呼吸音弱，双肺未闻及啰\n[BBOX-22] 音，双下肢无水肿，体重kg：\n[BBOX-23] 辅助检查：肺功能：FVC 74%，FEV1 56.3%，FEV1/FVC 58.6%，舒张试验阳性。\n[BBOX-24] 过敏史：\n[BBOX-25] 初步诊断（西医）：1.支气管哮喘（急性发作期）\n[BBOX-26] 初步诊断（中医）：\n[BBOX-27] 治疗方案：1.胸部CT、血常规、肺功能、心电图；2.建议心内科就诊。\n[BBOX-28] CT胸部\n[BBOX-29] 常规心电图检查\n[BBOX-30] 血常规\n[BBOX-31] 肾功3项\n[BBOX-32] 肝功9项\n[BBOX-33] 肺通气功能检查(肺功能)\n[BBOX-34] 肺容积检查(肺功能)\n[BBOX-35] 肺弥散功能检查(肺功能) 一次性肺功能仪用过滤嘴\n[BBOX-36] 肺通气功能检查(肺功能) 一次性肺功能仪用过滤嘴\n[BBOX-37] 布地奈德福莫特罗吸入粉雾剂(11)《每支60\n[BBOX-38] 吸，每吸含布地奈德320μg和富马酸福莫特\n[BBOX-39] 罗9.0μg>\n[BBOX-40] 用量：1.000吸/次\n[BBOX-41] 用法：吸入，二次/日，1天\n[BBOX-42] 醋酸泼尼松片<5mg>\n[BBOX-43] 用量：2.000片/次\n[BBOX-44] 用法：口服，一次/日，7天\n[BBOX-45] 签名：王美玲\n[BBOX-46] 丰镇市医院\n[BBOX-47] 诊断证明书\n[BBOX-48] 姓名：\n[BBOX-49] 年龄：\n[BBOX-50] 性别：男\n[BBOX-51] 病案号：10017815\n[BBOX-52] 印象：1.慢性支气管炎急性加重期2.支气管哮喘3.慢性胃炎4.肺气肿\n[BBOX-53] 处理意见：住院\n[BBOX-54] 医师：宋志杰\n[BBOX-55] 日期：2024年07月22日\n[BBOX-56] 地址：呼和浩特市通道北街一号\n[BBOX-57] 电话：0471--3451056\n[BBOX-58] 肺常规通气检查报告\n[BBOX-59] 测试号：0022542899\n[BBOX-60] 姓名：\n[BBOX-61] 出生日期：\n[BBOX-62] 身高：165 cm\n[BBOX-63] 临床印象：支气管哮喘\n[BBOX-64] 住址：内蒙古自治区乌兰察布\n[BBOX-65] 科别：\n[BBOX-66] 住院号：0022542899\n[BBOX-67] 性别：男\n[BBOX-68] 年龄：70 Years\n[BBOX-69] 体重：47 kg\n[BBOX-70] 吸烟史：否\n[BBOX-71] 联系电话：\n[BBOX-72] 主管医生：\n[BBOX-73] F/V ex\n[BBOX-74] F/V in\n[BBOX-75] Vol [L]\n[BBOX-76] Vol%VCmax\n[BBOX-77] VCmax\n[BBOX-78] Time [s]\n[BBOX-79] Vol [L]\n[BBOX-80] Time [s]\n[BBOX-81] FVC\n[BBOX-82] [L]\n[BBOX-83] 3.34\n[BBOX-84] 2.48\n[BBOX-85] 74.0\n[BBOX-86] FEV 1\n[BBOX-87] [L]\n[BBOX-88] 2.58\n[BBOX-89] 1.45\n[BBOX-90] 56.3\n[BBOX-91] FEV 2\n[BBOX-92] [L]\n[BBOX-93] 1.82\n[BBOX-94] FEV 3\n[BBOX-95] [L]\n[BBOX-96] 2.06\n[BBOX-97] FEV6\n[BBOX-98] [L]\n[BBOX-99] 2.45\n[BBOX-100] FEV 1 % FVC\n[BBOX-101] [%]\n[BBOX-102] 83.77\n[BBOX-103] 58.60\n[BBOX-104] 70.0\n[BBOX-105] FEV 1 % VC MAX\n[BBOX-106] [%]\n[BBOX-107] 74.61\n[BBOX-108] 58.60\n[BBOX-109] 78.5\n[BBOX-110] PEF\n[BBOX-111] [L/s]\n[BBOX-112] 7.27\n[BBOX-113] 5.34\n[BBOX-114] 73.4\n[BBOX-115] MEF 75\n[BBOX-116] [L/s]\n[BBOX-117] 6.51\n[BBOX-118] 1.94\n[BBOX-119] 29.8\n[BBOX-120] MEF 50\n[BBOX-121] [L/s]\n[BBOX-122] 3.73\n[BBOX-123] 0.72\n[BBOX-124] 19.4\n[BBOX-125] MEF 25\n[BBOX-126] [L/s]\n[BBOX-127] 1.15\n[BBOX-128] 0.25\n[BBOX-129] 21.9\n[BBOX-130] MMEF 75/25\n[BBOX-131] [L/s]\n[BBOX-132] 2.89\n[BBOX-133] 0.60\n[BBOX-134] 20.9\n[BBOX-135] FET\n[BBOX-136] [s]\n[BBOX-137] 7.16\n[BBOX-138] FET PEF\n[BBOX-139] [s]\n[BBOX-140] 0.05\n[BBOX-141] V backextrapolation ex\n[BBOX-142] [L]\n[BBOX-143] 0.07\n[BBOX-144] V backextrapol. % FVC\n[BBOX-145] [%]\n[BBOX-146] 2.82\n[BBOX-147] MVV\n[BBOX-148] [L/min]\n[BBOX-149] 101.83\n[BBOX-150] 37.40\n[BBOX-151] 36.7\n[BBOX-152] FEV 1 % VC MAX\n[BBOX-153] [%]\n[BBOX-154] 74.61\n[BBOX-155] 58.60\n[BBOX-156] 78.5\n[BBOX-157] VC EX\n[BBOX-158] [L]\n[BBOX-159] 3.46\n[BBOX-160] 2.48\n[BBOX-161] 71.6\n[BBOX-162] FRV\n[BBOX-163] [L]\n[BBOX-164] 0.93\n[BBOX-165] IRV\n[BBOX-166] [L]\n[BBOX-167] 0.80\n[BBOX-168] VT\n[BBOX-169] [L]\n[BBOX-170] 0.34\n[BBOX-171] 1.65\n[BBOX-172] 491.4\n[BBOX-173] IC\n[BBOX-174] [L]\n[BBOX-175] 2.53\n[BBOX-176] 2.45\n[BBOX-177] 96.9\n[BBOX-178] BF\n[BBOX-179] [1/min]\n[BBOX-180] 20.00\n[BBOX-181] 13.38\n[BBOX-182] 66.9\n[BBOX-183] MV\n[BBOX-184] [L/min]\n[BBOX-185] 6.71\n[BBOX-186] 22.08\n[BBOX-187] 328.9\n[BBOX-188] VC MAX\n[BBOX-189] [L]\n[BBOX-190] 3.46\n[BBOX-191] 2.48\n[BBOX-192] 71.6\n[BBOX-193] Date\n[BBOX-194] 25/12/26\n[BBOX-195] Time\n[BBOX-196] 9:49:52\n[BBOX-197] 结论：\n[BBOX-198] 1. 中重度混合性肺通气功能障碍。\n[BBOX-199] 轻度弥散功能障碍\n[BBOX-200] 操作员：刘角玲\n[BBOX-201] \\begin{tabular}{lcccccccccc}\n[BBOX-202] 报告时间: 2025-12-26\n[BBOX-203] \\hline\n[BBOX-204] & 预计值 & 药前 & \\%预计 & 药后1 & 改善率\\% & 药后2 & 改善率\\% & 药后3 & 改善率\\% \\\\\n[BBOX-205] \\hline\n[BBOX-206] FVC & [L] & 3.34 & 2.48 & 74.0 & 2.47 & -0.28 & 2.52 & 1.90 & 2.59 & 4.57 \\\\\n[BBOX-207] FEV 1 & [L] & 2.58 & 1.45 & 56.3 & 1.57 & 7.98 & 1.62 & 11.38 & 1.68 & 15.64 \\\\\n[BBOX-208] FEV 1 \\% FVC & [\\%] & 83.77 & 58.60 & 70.0 & 63.46 & 8.29 & 64.05 & 9.30 & 64.81 & 10.59 \\\\\n[BBOX-209] PEF & [L/s] & 7.27 & 5.34 & 73.4 & 5.97 & 11.92 & 6.55 & 22.75 & 6.30 & 18.12 \\\\\n[BBOX-210] MEF 75 & [L/s] & 6.51 & 1.94 & 29.8 & 1.93 & -0.49 & 2.25 & 15.90 & 2.48 & 27.48 \\\\\n[BBOX-211] MEF 50 & [L/s] & 3.73 & 0.72 & 19.4 & 1.08 & 48.95 & 1.10 & 52.54 & 1.10 & 52.19 \\\\\n[BBOX-212] MEF 25 & [L/s] & 1.15 & 0.25 & 21.9 & 0.37 & 49.20 & 0.35 & 40.24 & 0.38 & 51.20 \\\\\n[BBOX-213] MMEF 75/25 & [L/s] & 2.89 & 0.60 & 20.9 & 0.82 & 35.86 & 0.83 & 37.61 & 0.89 & 46.55 \\\\\n[BBOX-214] FET & [s] & & & & 6.24 & -12.85 & 7.29 & 1.83 & 7.07 & -1.26 \\\\\n[BBOX-215] FET PEF & [s] & & & & 0.05 & -10.65 & 0.04 & -18.54 & 0.05 & -3.25 \\\\\n[BBOX-216] V backextrapol. \\% FVC & [\\%] & & & & 3.10 & 10.19 & 2.50 & -11.19 & 3.24 & 15.10 \\\\\n[BBOX-217] \\hline\n[BBOX-218] Date & & & & & & & & & & \\\\\n[BBOX-219] Time & & 25/12/26 & 9:49:52$\\downarrow$ & & 25/12/26 & 10:34:27. & & 25/12/26 & 10:34:52. & \\\\\n[BBOX-220] & & & & & & & & 25/12/26 & 10:35:14. & \\\\\n[BBOX-221] \\hline\n[BBOX-222] \\end{tabular}\n[BBOX-223] 东吉轩药店\n[BBOX-224] 日期: 2026.01.23\n[BBOX-225] 09: 23: 37\n[BBOX-226] 单号: 20260123070132\n[BBOX-227] 品名 规格 单价 数量 总计\n[BBOX-228] 布地奈德福莫特罗吸入气雾剂\n[BBOX-229] (II)320ug/9ug/吸 60 吸/支\n[BBOX-230] 268.00 2 536.00\n[BBOX-231] 应收金额: 536.00\n[BBOX-232] 实收金额: 536.00\n[BBOX-233] 优惠金额: 0.00\n[BBOX-234] 找零金额: 0.00\n[BBOX-235] 会员:\n[BBOX-236] 日期: 2026.01.23\n[BBOX-237] 09: 23: 3\n[BBOX-238] 单号: 20260123070132"
  }
]
2026-08-05 06:07:13,912 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 06:07:13,939 INFO     29 [SmartSplitter] SmartSplitter done: 4 chunks from 4 LLM segments (all bbox_id). Types: {'OutpatientRecord': 2, 'ExaminationReport': 1, 'MedicationRecord': 1}
2026-08-05 06:07:13,951 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-05 06:07:13,951 INFO     29 [Trace] task=c9e5a6ba | doc=麦济WZWA222.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "239 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "chunks", "chunks": "4 items, types={'OutpatientRecord': 2, 'ExaminationReport': 1, 'MedicationRecord': 1}"}
2026-08-05 06:07:13,951 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-05 06:07:13,952 INFO     29 [ChunkRouter] Routed 4 chunks into 3 groups: {'chunks_Clinical': 2, 'chunks_Examination': 1, 'chunks_Medication': 1}
2026-08-05 06:07:13,962 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-05 06:07:13,962 INFO     29 [Trace] task=c9e5a6ba | doc=麦济WZWA222.pdf | ChunkRouter:Router | outputs={"html": "", "json": "239 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "chunks", "chunks": "4 items, types={'OutpatientRecord': 2, 'ExaminationReport': 1, 'MedicationRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 1, \"chunks_Medication\": 1}"}
2026-08-05 06:07:13,962 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-05 06:07:13,968 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:07:13,968 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m06:07:13 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:07:13,969 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:07:14,619 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:07:14,624 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-05 06:07:14,625 INFO     29 [Trace] task=c9e5a6ba | doc=麦济WZWA222.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "239 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 1, \"chunks_Medication\": 1}"}
2026-08-05 06:07:14,625 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-05 06:07:14,629 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:07:14,629 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m06:07:14 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:07:14,630 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:07:15,035 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T06:07:15.033+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 23, "failed": 0, "current": {"c9e5a6ba909311f1a3da71efcdd7cc1f": {"id": "c9e5a6ba909311f1a3da71efcdd7cc1f", "doc_id": "c9526904909311f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWZWA222.pdf", "type": "pdf", "location": "\u9ea6\u6d4eWZWA222.pdf", "size": 9742831, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785909984712, "task_type": "dataflow", "root_trace_id": "61b0a1cf64e14ac9b4fd9e1374842905", "root_traceparent": "00-61b0a1cf64e14ac9b4fd9e1374842905-58f4c254cd5a4a04-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 06:07:15,583 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:07:15,590 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-05 06:07:15,590 INFO     29 [Trace] task=c9e5a6ba | doc=麦济WZWA222.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "239 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 1, \"chunks_Medication\": 1}"}
2026-08-05 06:07:15,590 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-05 06:07:15,595 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 06:07:15,595 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 06:07:15,595 INFO     29 [qwen-vl-text] positions(46): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 06:07:15,595 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [46]
2026-08-05 06:07:16,044 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 06:07:16,045 INFO     29 [qwen-vl-text] LLM extraction start, text_len=703
2026-08-05 06:07:16,045 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:07:16,046 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 45, \"encounter_dates\": [\"2025-12-26\"], \"department\": \"呼吸内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "内蒙古医科大学附属医院门诊病历\n姓名：\n年龄：70岁\n诊疗号：0022542899\n民族：汉族\n性别：男性\n科室：呼吸内科门诊\n联系电话：\n身份：\n4\n病情：\n就诊状态：\n就诊时间：2025-12-26 08:41\n生命体征（需要时）：\n体温：℃ 脉搏：74次/分 呼吸：次/分 血压：/mmHg\n主诉：气短10余年，加重伴咳嗽咳痰1月\n现病史：气短10余年，规律用药（信必可都保320，早晚各一吸），加重伴咳\n嗽咳痰1月，血氧饱和度97%。自己输液治疗（含激素）10余天，气\n短、咳嗽咳痰症状无改善。\n既往史：患者平素身体一般，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎\n有，10年，吸烟史无，无过敏史。\n体格检查：发育正常，营养中等，体型正力，双肺呼吸音弱，双肺未闻及啰\n音，双下肢无水肿，体重kg：\n辅助检查：肺功能：FVC 74%，FEV1 56.3%，FEV1/FVC 58.6%，舒张试验阳性。\n过敏史：\n初步诊断（西医）：1.支气管哮喘（急性发作期）\n初步诊断（中医）：\n治疗方案：1.胸部CT、血常规、肺功能、心电图；2.建议心内科就诊。\nCT胸部\n常规心电图检查\n血常规\n肾功3项\n肝功9项\n肺通气功能检查(肺功能)\n肺容积检查(肺功能)\n肺弥散功能检查(肺功能) 一次性肺功能仪用过滤嘴\n肺通气功能检查(肺功能) 一次性肺功能仪用过滤嘴\n布地奈德福莫特罗吸入粉雾剂(11)《每支60\n吸，每吸含布地奈德320μg和富马酸福莫特\n罗9.0μg>\n用量：1.000吸/次\n用法：吸入，二次/日，1天\n醋酸泼尼松片<5mg>\n用量：2.000片/次\n用法：口服，一次/日，7天\n签名：王美玲",
    "role": "user"
  }
]
[92m06:07:16 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:07:16,048 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:07:19,677 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:07:19,678 INFO     29 [qwen-vl-text] LLM output (len=463):
{
  "encounter_date": "2025-12-26",
  "chief_complaint": "气短10余年，加重伴咳嗽咳痰1月",
  "present_illness": "气短10余年，规律用药（信必可都保320，早晚各一吸），加重伴咳嗽咳痰1月，血氧饱和度97%。自己输液治疗（含激素）10余天，气短、咳嗽咳痰症状无改善。",
  "past_history": "患者平素身体一般，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎有，10年，吸烟史无，无过敏史。",
  "diagnosis": "西医：支气管哮喘（急性发作期）",
  "treatment_plan": [
    "胸部CT、血常规、肺功能、心电图",
    "建议心内科就诊",
    "布地奈德福莫特罗吸入粉雾剂(11)《每支60吸，每吸含布地奈德320μg和富马酸福莫特罗9.0μg> 1.000吸/次 吸入 二次/日 1天",
    "醋酸泼尼松片<5mg> 2.000片/次 口服 一次/日 7天"
  ]
}
2026-08-05 06:07:19,678 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-26]
2026-08-05 06:07:19,705 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8011001, prompt_len=1454
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
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord API raw response (len=2705):
[
	{"text": "内蒙古医科大学附属医院门诊病历", "bbox": [228, 60, 770, 87]},
	{"text": "姓名：", "bbox": [64, 105, 125, 123]},
	{"text": "年龄：70岁", "bbox": [323, 105, 453, 123]},
	{"text": "诊疗号：0022542899", "bbox": [580, 106, 805, 124]},
	{"text": "民族：汉族", "bbox": [67, 139, 195, 156]},
	{"text": "性别：男性", "bbox": [323, 139, 453, 157]},
	{"text": "科室：呼吸内科门诊", "bbox": [580, 140, 809, 158]},
	{"text": "联系电话：", "bbox": [65, 172, 174, 190]},
	{"text": "身份：", "bbox": [373, 172, 428, 190]},
	{"text": "4", "bbox": [682, 174, 698, 189]},
	{"text": "病情：", "bbox": [750, 174, 807, 191]},
	{"text": "就诊状态：", "bbox": [65, 206, 174, 224]},
	{"text": "就诊时间：2025-12-26 08:41", "bbox": [309, 206, 644, 224]},
	{"text": "生命体征（需要时）：", "bbox": [67, 233, 300, 251]},
	{"text": "体温：℃ 脉搏：74次/分 呼吸：次/分 血压：/mmHg", "bbox": [65, 256, 593, 275]},
	{"text": "主诉：气短10余年，加重伴咳嗽咳痰1月", "bbox": [65, 280, 533, 300]},
	{"text": "现病史：气短10余年，规律用药（信必可都保320，早晚各一吸），加重伴咳", "bbox": [65, 304, 928, 324]},
	{"text": "嗽咳痰1月，血氧饱和度97%。自己输液治疗（含激素）10余天，气", "bbox": [171, 328, 928, 348]},
	{"text": "短、咳嗽咳痰症状无改善。", "bbox": [171, 352, 462, 371]},
	{"text": "既往史：患者平素身体一般，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "bbox": [65, 376, 928, 395]},
	{"text": "有，10年，吸烟史无，无过敏史。", "bbox": [171, 399, 536, 418]},
	{"text": "体格检查：发育正常，营养中等，体型正力，双肺呼吸音弱，双肺未闻及啰", "bbox": [65, 423, 899, 442]},
	{"text": "音，双下肢无水肿，体重kg：", "bbox": [200, 446, 512, 465]},
	{"text": "辅助检查：肺功能：FVC 74%，FEV1 56.3%，FEV1/FVC 58.6%，舒张试验阳性。", "bbox": [65, 469, 886, 489]},
	{"text": "过敏史：", "bbox": [65, 494, 149, 512]},
	{"text": "初步诊断（西医）：1.支气管哮喘（急性发作期）", "bbox": [65, 517, 592, 537]},
	{"text": "初步诊断（中医）：", "bbox": [65, 541, 254, 560]},
	{"text": "治疗方案：1.胸部CT、血常规、肺功能、心电图；2.建议心内科就诊。", "bbox": [65, 565, 810, 584]},
	{"text": "CT胸部", "bbox": [67, 607, 142, 624]},
	{"text": "常规心电图检查", "bbox": [359, 607, 530, 624]},
	{"text": "血常规", "bbox": [647, 607, 718, 624]},
	{"text": "肾功3项", "bbox": [70, 629, 153, 647]},
	{"text": "肝功9项", "bbox": [359, 629, 442, 647]},
	{"text": "肺通气功能检查(肺功能)", "bbox": [647, 627, 913, 646]},
	{"text": "肺容积检查(肺功能)", "bbox": [69, 652, 288, 670]},
	{"text": "肺弥散功能检查(肺功能) 一次性肺功能仪用过滤嘴", "bbox": [359, 652, 915, 670]},
	{"text": "肺通气功能检查(肺功能) 一次性肺功能仪用过滤嘴", "bbox": [69, 674, 629, 692]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(11)《每支60", "bbox": [67, 694, 530, 712]},
	{"text": "吸，每吸含布地奈德320μg和富马酸福莫特", "bbox": [67, 714, 528, 732]},
	{"text": "罗9.0μg>", "bbox": [69, 734, 177, 752]},
	{"text": "用量：1.000吸/次", "bbox": [584, 692, 764, 710]},
	{"text": "用法：吸入，二次/日，1天", "bbox": [117, 752, 404, 771]},
	{"text": "醋酸泼尼松片<5mg>", "bbox": [65, 776, 277, 794]},
	{"text": "用量：2.000片/次", "bbox": [584, 773, 764, 791]},
	{"text": "用法：口服，一次/日，7天", "bbox": [117, 794, 404, 813]},
	{"text": "签名：王美玲", "bbox": [545, 888, 740, 922]}
]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord API: raw_items=46, valid_items=46, elapsed=19.7s
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[0]: text=内蒙古医科大学附属医院门诊病历, bbox=[228, 60, 770, 87]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[64, 105, 125, 123]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：70岁, bbox=[323, 105, 453, 123]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[3]: text=诊疗号：0022542899, bbox=[580, 106, 805, 124]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[4]: text=民族：汉族, bbox=[67, 139, 195, 156]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[5]: text=性别：男性, bbox=[323, 139, 453, 157]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[6]: text=科室：呼吸内科门诊, bbox=[580, 140, 809, 158]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[7]: text=联系电话：, bbox=[65, 172, 174, 190]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[8]: text=身份：, bbox=[373, 172, 428, 190]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[9]: text=4, bbox=[682, 174, 698, 189]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[10]: text=病情：, bbox=[750, 174, 807, 191]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[11]: text=就诊状态：, bbox=[65, 206, 174, 224]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[12]: text=就诊时间：2025-12-26 08:41, bbox=[309, 206, 644, 224]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[13]: text=生命体征（需要时）：, bbox=[67, 233, 300, 251]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[14]: text=体温：℃ 脉搏：74次/分 呼吸：次/分 血压：/mmHg, bbox=[65, 256, 593, 275]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[15]: text=主诉：气短10余年，加重伴咳嗽咳痰1月, bbox=[65, 280, 533, 300]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[16]: text=现病史：气短10余年，规律用药（信必可都保320，早晚各一吸），加重伴咳, bbox=[65, 304, 928, 324]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[17]: text=嗽咳痰1月，血氧饱和度97%。自己输液治疗（含激素）10余天，气, bbox=[171, 328, 928, 348]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[18]: text=短、咳嗽咳痰症状无改善。, bbox=[171, 352, 462, 371]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[19]: text=既往史：患者平素身体一般，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎, bbox=[65, 376, 928, 395]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[20]: text=有，10年，吸烟史无，无过敏史。, bbox=[171, 399, 536, 418]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[21]: text=体格检查：发育正常，营养中等，体型正力，双肺呼吸音弱，双肺未闻及啰, bbox=[65, 423, 899, 442]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[22]: text=音，双下肢无水肿，体重kg：, bbox=[200, 446, 512, 465]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[23]: text=辅助检查：肺功能：FVC 74%，FEV1 56.3%，FEV1/FVC 58.6%，舒张试验阳性。, bbox=[65, 469, 886, 489]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[24]: text=过敏史：, bbox=[65, 494, 149, 512]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[25]: text=初步诊断（西医）：1.支气管哮喘（急性发作期）, bbox=[65, 517, 592, 537]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[26]: text=初步诊断（中医）：, bbox=[65, 541, 254, 560]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[27]: text=治疗方案：1.胸部CT、血常规、肺功能、心电图；2.建议心内科就诊。, bbox=[65, 565, 810, 584]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[28]: text=CT胸部, bbox=[67, 607, 142, 624]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[29]: text=常规心电图检查, bbox=[359, 607, 530, 624]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[30]: text=血常规, bbox=[647, 607, 718, 624]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[31]: text=肾功3项, bbox=[70, 629, 153, 647]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[32]: text=肝功9项, bbox=[359, 629, 442, 647]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[33]: text=肺通气功能检查(肺功能), bbox=[647, 627, 913, 646]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[34]: text=肺容积检查(肺功能), bbox=[69, 652, 288, 670]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[35]: text=肺弥散功能检查(肺功能) 一次性肺功能仪用过滤嘴, bbox=[359, 652, 915, 670]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[36]: text=肺通气功能检查(肺功能) 一次性肺功能仪用过滤嘴, bbox=[69, 674, 629, 692]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[37]: text=布地奈德福莫特罗吸入粉雾剂(11)《每支60, bbox=[67, 694, 530, 712]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[38]: text=吸，每吸含布地奈德320μg和富马酸福莫特, bbox=[67, 714, 528, 732]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[39]: text=罗9.0μg>, bbox=[69, 734, 177, 752]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[40]: text=用量：1.000吸/次, bbox=[584, 692, 764, 710]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[41]: text=用法：吸入，二次/日，1天, bbox=[117, 752, 404, 771]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[42]: text=醋酸泼尼松片<5mg>, bbox=[65, 776, 277, 794]
2026-08-05 06:07:39,394 INFO     29 [qwen-vl-text] coord item[43]: text=用量：2.000片/次, bbox=[584, 773, 764, 791]
2026-08-05 06:07:39,395 INFO     29 [qwen-vl-text] coord item[44]: text=用法：口服，一次/日，7天, bbox=[117, 794, 404, 813]
2026-08-05 06:07:39,395 INFO     29 [qwen-vl-text] coord item[45]: text=签名：王美玲, bbox=[545, 888, 740, 922]
2026-08-05 06:07:39,396 INFO     29 [qwen-vl-text] page=0 — 46/46 coords, api_time=19.7s
2026-08-05 06:07:39,396 INFO     29 [qwen-vl-text] new_positions (46):
[[0, 135.66, 458.15, 50.519999999999996, 73.25399999999999], [0, 38.08, 74.375, 88.41, 103.566], [0, 192.185, 269.53499999999997, 88.41, 103.566], [0, 345.09999999999997, 478.97499999999997, 89.252, 104.408], [0, 39.864999999999995, 116.02499999999999, 117.038, 131.352], [0, 192.185, 269.53499999999997, 117.038, 132.194], [0, 345.09999999999997, 481.35499999999996, 117.88, 133.036], [0, 38.675, 103.53, 144.82399999999998, 159.98], [0, 221.935, 254.66, 144.82399999999998, 159.98], [0, 405.78999999999996, 415.31, 146.50799999999998, 159.138], [0, 446.25, 480.16499999999996, 146.50799999999998, 160.822], [0, 38.675, 103.53, 173.452, 188.608], [0, 183.855, 383.18, 173.452, 188.608], [0, 39.864999999999995, 178.5, 196.186, 211.34199999999998], [0, 38.675, 352.835, 215.552, 231.54999999999998], [0, 38.675, 317.135, 235.76, 252.6], [0, 38.675, 552.16, 255.968, 272.808], [0, 101.74499999999999, 552.16, 276.176, 293.01599999999996], [0, 101.74499999999999, 274.89, 296.384, 312.382], [0, 38.675, 552.16, 316.592, 332.59], [0, 101.74499999999999, 318.91999999999996, 335.95799999999997, 351.95599999999996], [0, 38.675, 534.905, 356.166, 372.164], [0, 119.0, 304.64, 375.532, 391.53], [0, 38.675, 527.17, 394.89799999999997, 411.738], [0, 38.675, 88.655, 415.948, 431.104], [0, 38.675, 352.24, 435.31399999999996, 452.154], [0, 38.675, 151.13, 455.522, 471.52], [0, 38.675, 481.95, 475.72999999999996, 491.728], [0, 39.864999999999995, 84.49, 511.094, 525.408], [0, 213.605, 315.34999999999997, 511.094, 525.408], [0, 384.965, 427.21, 511.094, 525.408], [0, 41.65, 91.035, 529.6179999999999, 544.774], [0, 213.605, 262.99, 529.6179999999999, 544.774], [0, 384.965, 543.235, 527.934, 543.932], [0, 41.055, 171.35999999999999, 548.984, 564.14], [0, 213.605, 544.425, 548.984, 564.14], [0, 41.055, 374.255, 567.5079999999999, 582.664], [0, 39.864999999999995, 315.34999999999997, 584.348, 599.504], [0, 39.864999999999995, 314.15999999999997, 601.188, 616.3439999999999], [0, 41.055, 105.315, 618.028, 633.184], [0, 347.47999999999996, 454.58, 582.664, 597.8199999999999], [0, 69.615, 240.38, 633.184, 649.182], [0, 38.675, 164.815, 653.3919999999999, 668.548], [0, 347.47999999999996, 454.58, 650.866, 666.0219999999999], [0, 69.615, 240.38, 668.548, 684.5459999999999], [0, 324.275, 440.29999999999995, 747.696, 776.324]]
2026-08-05 06:07:39,396 INFO     29 [qwen-vl-text] ═══ DONE ═══ 46 positions, pages=1, time=23.8s
2026-08-05 06:07:39,396 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 06:07:39,396 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 06:07:39,396 INFO     29 [qwen-vl-text] positions(12): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 06:07:39,396 INFO     29 [qwen-vl-text] page grouping: [1, 2], lines per page: [10, 2]
2026-08-05 06:07:39,549 INFO     29 [qwen-vl-text] page=1, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 06:07:39,906 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 06:07:39,907 INFO     29 [qwen-vl-text] LLM extraction start, text_len=134
2026-08-05 06:07:39,908 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:07:39,908 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 46, \"bbox_end\": 57, \"encounter_dates\": [\"2024-07-22\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "丰镇市医院\n诊断证明书\n姓名：\n年龄：\n性别：男\n病案号：10017815\n印象：1.慢性支气管炎急性加重期2.支气管哮喘3.慢性胃炎4.肺气肿\n处理意见：住院\n医师：宋志杰\n日期：2024年07月22日\n地址：呼和浩特市通道北街一号\n电话：0471--3451056",
    "role": "user"
  }
]
[92m06:07:39 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:07:39,910 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:07:42,471 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:07:42,471 INFO     29 [qwen-vl-text] LLM output (len=193):
{
  "encounter_date": "2024-07-22",
  "chief_complaint": null,
  "present_illness": null,
  "past_history": null,
  "diagnosis": "1.慢性支气管炎急性加重期 2.支气管哮喘 3.慢性胃炎 4.肺气肿",
  "treatment_plan": "住院"
}
2026-08-05 06:07:42,471 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-07-22]
2026-08-05 06:07:42,472 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=843191, prompt_len=745
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
2026-08-05 06:07:46,210 INFO     29 [qwen-vl-text] coord API raw response (len=545):
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
	{"text": "日期：2024年07月22日", "bbox": [744, 433, 897, 458]}
]
2026-08-05 06:07:46,211 INFO     29 [qwen-vl-text] coord API: raw_items=10, valid_items=10, elapsed=3.7s
2026-08-05 06:07:46,211 INFO     29 [qwen-vl-text] coord item[0]: text=丰镇市医院, bbox=[560, 207, 686, 239]
2026-08-05 06:07:46,211 INFO     29 [qwen-vl-text] coord item[1]: text=诊断证明书, bbox=[533, 252, 707, 295]
2026-08-05 06:07:46,211 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[164, 302, 219, 327]
2026-08-05 06:07:46,211 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：, bbox=[164, 337, 219, 362]
2026-08-05 06:07:46,211 INFO     29 [qwen-vl-text] coord item[4]: text=性别：男, bbox=[740, 304, 825, 327]
2026-08-05 06:07:46,211 INFO     29 [qwen-vl-text] coord item[5]: text=病案号：10017815, bbox=[740, 335, 869, 357]
2026-08-05 06:07:46,211 INFO     29 [qwen-vl-text] coord item[6]: text=印象：1.慢性支气管炎急性加重期2.支气管哮喘3.慢性胃炎4.肺气肿, bbox=[165, 365, 731, 396]
2026-08-05 06:07:46,211 INFO     29 [qwen-vl-text] coord item[7]: text=处理意见：住院, bbox=[165, 402, 307, 429]
2026-08-05 06:07:46,211 INFO     29 [qwen-vl-text] coord item[8]: text=医师：宋志杰, bbox=[165, 441, 330, 496]
2026-08-05 06:07:46,211 INFO     29 [qwen-vl-text] coord item[9]: text=日期：2024年07月22日, bbox=[744, 433, 897, 458]
2026-08-05 06:07:46,211 INFO     29 [qwen-vl-text] page=1 — 10/10 coords, api_time=3.7s
2026-08-05 06:07:46,216 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2828092, prompt_len=649
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
2026-08-05 06:07:48,729 INFO     29 [qwen-vl-text] coord API raw response (len=131):
```json
[
	{"text": "地址：呼和浩特市通道北街一号", "bbox": [306, 73, 679, 90]},
	{"text": "电话：0471--3451056", "bbox": [367, 90, 621, 107]}
]
```
2026-08-05 06:07:48,729 INFO     29 [qwen-vl-text] coord API: raw_items=2, valid_items=2, elapsed=2.5s
2026-08-05 06:07:48,729 INFO     29 [qwen-vl-text] coord item[0]: text=地址：呼和浩特市通道北街一号, bbox=[306, 73, 679, 90]
2026-08-05 06:07:48,729 INFO     29 [qwen-vl-text] coord item[1]: text=电话：0471--3451056, bbox=[367, 90, 621, 107]
2026-08-05 06:07:48,729 INFO     29 [qwen-vl-text] page=2 — 2/2 coords, api_time=2.5s
2026-08-05 06:07:48,730 INFO     29 [qwen-vl-text] new_positions (12):
[[1, 471.52, 577.612, 123.16499999999999, 142.20499999999998], [1, 448.786, 595.294, 149.94, 175.525], [1, 138.088, 184.398, 179.69, 194.565], [1, 138.088, 184.398, 200.515, 215.39], [1, 623.0799999999999, 694.65, 180.88, 194.565], [1, 623.0799999999999, 731.698, 199.325, 212.415], [1, 138.93, 615.502, 217.17499999999998, 235.61999999999998], [1, 138.93, 258.49399999999997, 239.19, 255.255], [1, 138.93, 277.86, 262.395, 295.12], [1, 626.448, 755.274, 257.635, 272.51], [2, 182.07, 404.005, 61.466, 75.78], [2, 218.36499999999998, 369.495, 75.78, 90.094]]
2026-08-05 06:07:48,730 INFO     29 [qwen-vl-text] ═══ DONE ═══ 12 positions, pages=2, time=9.3s
2026-08-05 06:07:48,737 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-05 06:07:48,737 INFO     29 [Trace] task=c9e5a6ba | doc=麦济WZWA222.pdf | Extractor:Clinical | outputs={"chunks": "2 items, types={'OutpatientRecord': 2}", "html": "", "json": "239 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 1, \"chunks_Medication\": 1}"}
2026-08-05 06:07:48,737 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-05 06:07:48,738 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T06:07:48.738+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 23, "failed": 0, "current": {"c9e5a6ba909311f1a3da71efcdd7cc1f": {"id": "c9e5a6ba909311f1a3da71efcdd7cc1f", "doc_id": "c9526904909311f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWZWA222.pdf", "type": "pdf", "location": "\u9ea6\u6d4eWZWA222.pdf", "size": 9742831, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785909984712, "task_type": "dataflow", "root_trace_id": "61b0a1cf64e14ac9b4fd9e1374842905", "root_traceparent": "00-61b0a1cf64e14ac9b4fd9e1374842905-58f4c254cd5a4a04-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 06:07:48,744 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 06:07:48,744 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 06:07:48,744 INFO     29 [qwen-vl-text] positions(16): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 06:07:48,744 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [16]
2026-08-05 06:07:49,050 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 06:07:49,051 INFO     29 [qwen-vl-text] LLM extraction start, text_len=214
2026-08-05 06:07:49,051 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:07:49,051 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 223, \"bbox_end\": 238, \"encounter_dates\": [\"2026-01-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "东吉轩药店\n日期: 2026.01.23\n09: 23: 37\n单号: 20260123070132\n品名 规格 单价 数量 总计\n布地奈德福莫特罗吸入气雾剂\n(II)320ug/9ug/吸 60 吸/支\n268.00 2 536.00\n应收金额: 536.00\n实收金额: 536.00\n优惠金额: 0.00\n找零金额: 0.00\n会员:\n日期: 2026.01.23\n09: 23: 3\n单号: 20260123070132",
    "role": "user"
  }
]
[92m06:07:49 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:07:49,052 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:07:51,953 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:07:51,953 INFO     29 [qwen-vl-text] LLM output (len=427):
{
  "encounter_date": "2026-01-23",
  "pharmacy": "东吉轩药店",
  "medications": [
    {
      "name": "布地奈德福莫特罗吸入气雾剂",
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
2026-08-05 06:07:51,953 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-23]
2026-08-05 06:07:51,957 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2565324, prompt_len=875
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
2026-08-05 06:08:01,243 INFO     29 [qwen-vl-text] coord API raw response (len=920):
[
	{"text": "东吉轩药店", "bbox": [392, 68, 731, 119]},
	{"text": "日期: 2026.01.23", "bbox": [206, 162, 536, 192]},
	{"text": "09: 23: 37", "bbox": [624, 164, 846, 191]},
	{"text": "单号: 20260123070132", "bbox": [204, 217, 646, 248]},
	{"text": "品名 规格 单价 数量 总计", "bbox": [203, 272, 821, 306]},
	{"text": "布地奈德福莫特罗吸入气雾剂", "bbox": [203, 384, 781, 418]},
	{"text": "(II)320ug/9ug/吸 60 吸/支", "bbox": [245, 442, 742, 477]},
	{"text": "268.00 2 536.00", "bbox": [221, 501, 737, 529]},
	{"text": "应收金额: 536.00", "bbox": [202, 553, 548, 588]},
	{"text": "实收金额: 536.00", "bbox": [203, 610, 548, 645]},
	{"text": "优惠金额: 0.00", "bbox": [203, 667, 503, 699]},
	{"text": "找零金额: 0.00", "bbox": [203, 721, 503, 754]},
	{"text": "会员:", "bbox": [204, 776, 308, 810]},
	{"text": "日期: 2026.01.23", "bbox": [208, 888, 534, 920]},
	{"text": "09: 23: 3", "bbox": [645, 893, 852, 920]},
	{"text": "单号: 20260123070132", "bbox": [208, 942, 642, 972]}
]
2026-08-05 06:08:01,244 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=9.3s
2026-08-05 06:08:01,244 INFO     29 [qwen-vl-text] coord item[0]: text=东吉轩药店, bbox=[392, 68, 731, 119]
2026-08-05 06:08:01,244 INFO     29 [qwen-vl-text] coord item[1]: text=日期: 2026.01.23, bbox=[206, 162, 536, 192]
2026-08-05 06:08:01,244 INFO     29 [qwen-vl-text] coord item[2]: text=09: 23: 37, bbox=[624, 164, 846, 191]
2026-08-05 06:08:01,244 INFO     29 [qwen-vl-text] coord item[3]: text=单号: 20260123070132, bbox=[204, 217, 646, 248]
2026-08-05 06:08:01,244 INFO     29 [qwen-vl-text] coord item[4]: text=品名 规格 单价 数量 总计, bbox=[203, 272, 821, 306]
2026-08-05 06:08:01,244 INFO     29 [qwen-vl-text] coord item[5]: text=布地奈德福莫特罗吸入气雾剂, bbox=[203, 384, 781, 418]
2026-08-05 06:08:01,244 INFO     29 [qwen-vl-text] coord item[6]: text=(II)320ug/9ug/吸 60 吸/支, bbox=[245, 442, 742, 477]
2026-08-05 06:08:01,244 INFO     29 [qwen-vl-text] coord item[7]: text=268.00 2 536.00, bbox=[221, 501, 737, 529]
2026-08-05 06:08:01,244 INFO     29 [qwen-vl-text] coord item[8]: text=应收金额: 536.00, bbox=[202, 553, 548, 588]
2026-08-05 06:08:01,244 INFO     29 [qwen-vl-text] coord item[9]: text=实收金额: 536.00, bbox=[203, 610, 548, 645]
2026-08-05 06:08:01,244 INFO     29 [qwen-vl-text] coord item[10]: text=优惠金额: 0.00, bbox=[203, 667, 503, 699]
2026-08-05 06:08:01,244 INFO     29 [qwen-vl-text] coord item[11]: text=找零金额: 0.00, bbox=[203, 721, 503, 754]
2026-08-05 06:08:01,244 INFO     29 [qwen-vl-text] coord item[12]: text=会员:, bbox=[204, 776, 308, 810]
2026-08-05 06:08:01,244 INFO     29 [qwen-vl-text] coord item[13]: text=日期: 2026.01.23, bbox=[208, 888, 534, 920]
2026-08-05 06:08:01,244 INFO     29 [qwen-vl-text] coord item[14]: text=09: 23: 3, bbox=[645, 893, 852, 920]
2026-08-05 06:08:01,244 INFO     29 [qwen-vl-text] coord item[15]: text=单号: 20260123070132, bbox=[208, 942, 642, 972]
2026-08-05 06:08:01,245 INFO     29 [qwen-vl-text] page=4 — 16/16 coords, api_time=9.3s
2026-08-05 06:08:01,245 INFO     29 [qwen-vl-text] new_positions (16):
[[4, 233.23999999999998, 434.945, 57.256, 100.198], [4, 122.57, 318.91999999999996, 136.404, 161.664], [4, 371.28, 503.37, 138.088, 160.822], [4, 121.38, 384.37, 182.714, 208.816], [4, 120.785, 488.495, 229.024, 257.652], [4, 120.785, 464.695, 323.328, 351.95599999999996], [4, 145.775, 441.48999999999995, 372.164, 401.63399999999996], [4, 131.495, 438.515, 421.842, 445.418], [4, 120.19, 326.06, 465.626, 495.096], [4, 120.785, 326.06, 513.62, 543.09], [4, 120.785, 299.28499999999997, 561.614, 588.558], [4, 120.785, 299.28499999999997, 607.082, 634.8679999999999], [4, 121.38, 183.26, 653.3919999999999, 682.02], [4, 123.75999999999999, 317.72999999999996, 747.696, 774.64], [4, 383.775, 506.94, 751.906, 774.64], [4, 123.75999999999999, 381.99, 793.164, 818.424]]
2026-08-05 06:08:01,245 INFO     29 [qwen-vl-text] ═══ DONE ═══ 16 positions, pages=1, time=12.5s
2026-08-05 06:08:01,251 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-05 06:08:01,251 INFO     29 [Trace] task=c9e5a6ba | doc=麦济WZWA222.pdf | Extractor:Medication | outputs={"chunks": "1 items, types={'MedicationRecord': 1}", "html": "", "json": "239 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 1, \"chunks_Medication\": 1}"}
2026-08-05 06:08:01,252 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-05 06:08:01,256 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:08:01,256 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m06:08:01 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:08:01,258 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:08:02,471 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:08:02,480 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-05 06:08:02,480 INFO     29 [Trace] task=c9e5a6ba | doc=麦济WZWA222.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "239 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 1, \"chunks_Medication\": 1}"}
2026-08-05 06:08:02,481 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-05 06:08:02,487 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:08:02,487 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m06:08:02 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:08:02,488 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:08:05,549 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:08:05,557 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-05 06:08:05,557 INFO     29 [Trace] task=c9e5a6ba | doc=麦济WZWA222.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "239 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 1, \"chunks_Medication\": 1}"}
2026-08-05 06:08:05,557 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-05 06:08:05,563 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 06:08:05,563 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-05 06:08:06,133 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 06:08:06,139 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-05 06:08:06,140 INFO     29 [Trace] task=c9e5a6ba | doc=麦济WZWA222.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "239 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 1, \"chunks_Medication\": 1}"}
2026-08-05 06:08:06,140 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-05 06:08:06,149 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 06:08:06,150 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-05 06:08:06,150 INFO     29 [qwen-vl-text] positions(165): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 06:08:06,150 INFO     29 [qwen-vl-text] page grouping: [2, 3], lines per page: [143, 16]
2026-08-05 06:08:06,510 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 06:08:06,923 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 06:08:06,924 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1684
2026-08-05 06:08:06,924 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:08:06,924 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 58, \"bbox_end\": 222, \"encounter_dates\": [\"2025-12-26\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "肺常规通气检查报告\n测试号：0022542899\n姓名：\n出生日期：\n身高：165 cm\n临床印象：支气管哮喘\n住址：内蒙古自治区乌兰察布\n科别：\n住院号：0022542899\n性别：男\n年龄：70 Years\n体重：47 kg\n吸烟史：否\n联系电话：\n主管医生：\nF/V ex\nF/V in\nVol [L]\nVol%VCmax\nVCmax\nTime [s]\nVol [L]\nTime [s]\nFVC\n[L]\n3.34\n2.48\n74.0\nFEV 1\n[L]\n2.58\n1.45\n56.3\nFEV 2\n[L]\n1.82\nFEV 3\n[L]\n2.06\nFEV6\n[L]\n2.45\nFEV 1 % FVC\n[%]\n83.77\n58.60\n70.0\nFEV 1 % VC MAX\n[%]\n74.61\n58.60\n78.5\nPEF\n[L/s]\n7.27\n5.34\n73.4\nMEF 75\n[L/s]\n6.51\n1.94\n29.8\nMEF 50\n[L/s]\n3.73\n0.72\n19.4\nMEF 25\n[L/s]\n1.15\n0.25\n21.9\nMMEF 75/25\n[L/s]\n2.89\n0.60\n20.9\nFET\n[s]\n7.16\nFET PEF\n[s]\n0.05\nV backextrapolation ex\n[L]\n0.07\nV backextrapol. % FVC\n[%]\n2.82\nMVV\n[L/min]\n101.83\n37.40\n36.7\nFEV 1 % VC MAX\n[%]\n74.61\n58.60\n78.5\nVC EX\n[L]\n3.46\n2.48\n71.6\nFRV\n[L]\n0.93\nIRV\n[L]\n0.80\nVT\n[L]\n0.34\n1.65\n491.4\nIC\n[L]\n2.53\n2.45\n96.9\nBF\n[1/min]\n20.00\n13.38\n66.9\nMV\n[L/min]\n6.71\n22.08\n328.9\nVC MAX\n[L]\n3.46\n2.48\n71.6\nDate\n25/12/26\nTime\n9:49:52\n结论：\n1. 中重度混合性肺通气功能障碍。\n轻度弥散功能障碍\n操作员：刘角玲\n报告时间: 2025-12-26\n预计值 药前 %预计 药后1 改善率% 药后2 改善率% 药后3 改善率%\nFVC [L] 3.34 2.48 74.0 2.47 -0.28 2.52 1.90 2.59 4.57\nFEV 1 [L] 2.58 1.45 56.3 1.57 7.98 1.62 11.38 1.68 15.64\nFEV 1 % FVC [%] 83.77 58.60 70.0 63.46 8.29 64.05 9.30 64.81 10.59\nPEF [L/s] 7.27 5.34 73.4 5.97 11.92 6.55 22.75 6.30 18.12\nMEF 75 [L/s] 6.51 1.94 29.8 1.93 -0.49 2.25 15.90 2.48 27.48\nMEF 50 [L/s] 3.73 0.72 19.4 1.08 48.95 1.10 52.54 1.10 52.19\nMEF 25 [L/s] 1.15 0.25 21.9 0.37 49.20 0.35 40.24 0.38 51.20\nMMEF 75/25 [L/s] 2.89 0.60 20.9 0.82 35.86 0.83 37.61 0.89 46.55\nFET [s] 6.24 -12.85 7.29 1.83 7.07 -1.26\nFET PEF [s] 0.05 -10.65 0.04 -18.54 0.05 -3.25\nV backextrapol. % FVC [%] 3.10 10.19 2.50 -11.19 3.24 15.10\nDate\nTime 25/12/26 9:49:52$\\downarrow$ 25/12/26 10:34:27. 25/12/26 10:34:52.\n25/12/26 10:35:14.",
    "role": "user"
  }
]
[92m06:08:06 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:08:06,927 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:08:16,777 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:08:16,778 INFO     29 [qwen-vl-text] LLM output (len=1326):
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
  "findings": "| 指标 | 预计值 | 药前 | %预计 | 药后1 | 改善率% | 药后2 | 改善率% | 药后3 | 改善率% |\n|---|---|---|---|---|---|---|---|---|---|\n| FVC [L] | 3.34 | 2.48 | 74.0 | 2.47 | -0.28 | 2.52 | 1.90 | 2.59 | 4.57 |\n| FEV 1 [L] | 2.58 | 1.45 | 56.3 | 1.57 | 7.98 | 1.62 | 11.38 | 1.68 | 15.64 |\n| FEV 1 % FVC [%] | 83.77 | 58.60 | 70.0 | 63.46 | 8.29 | 64.05 | 9.30 | 64.81 | 10.59 |\n| PEF [L/s] | 7.27 | 5.34 | 73.4 | 5.97 | 11.92 | 6.55 | 22.75 | 6.30 | 18.12 |\n| MEF 75 [L/s] | 6.51 | 1.94 | 29.8 | 1.93 | -0.49 | 2.25 | 15.90 | 2.48 | 27.48 |\n| MEF 50 [L/s] | 3.73 | 0.72 | 19.4 | 1.08 | 48.95 | 1.10 | 52.54 | 1.10 | 52.19 |\n| MEF 25 [L/s] | 1.15 | 0.25 | 21.9 | 0.37 | 49.20 | 0.35 | 40.24 | 0.38 | 51.20 |\n| MMEF 75/25 [L/s] | 2.89 | 0.60 | 20.9 | 0.82 | 35.86 | 0.83 | 37.61 | 0.89 | 46.55 |\n| FET [s] | | 6.24 | -12.85 | 7.29 | 1.83 | 7.07 | -1.26 | | |\n| FET PEF [s] | | 0.05 | -10.65 | 0.04 | -18.54 | 0.05 | -3.25 | | |\n| V backextrapol. % FVC [%] | | 3.10 | 10.19 | 2.50 | -11.19 | 3.24 | 15.10 | | |",
  "conclusion": "1. 中重度混合性肺通气功能障碍。\n轻度弥散功能障碍",
  "physician": "刘角玲",
  "reviewer": null
}
2026-08-05 06:08:16,785 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2828092, prompt_len=1944
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共143行）
["肺常规通气检查报告", "测试号：0022542899", "姓名：", "出生日期：", "身高：165 cm", "临床印象：支气管哮喘", "住址：内蒙古自治区乌兰察布", "科别：", "住院号：0022542899", "性别：男", "年龄：70 Years", "体重：47 kg", "吸烟史：否", "联系电话：", "主管医生：", "F/V ex", "F/V in", "Vol [L]", "Vol%VCmax", "VCmax", "Time [s]", "Vol [L]", "Time [s]", "FVC", "[L]", "3.34", "2.48", "74.0", "FEV 1", "[L]", "2.58", "1.45", "56.3", "FEV 2", "[L]", "1.82", "FEV 3", "[L]", "2.06", "FEV6", "[L]", "2.45", "FEV 1 % FVC", "[%]", "83.77", "58.60", "70.0", "FEV 1 % VC MAX", "[%]", "74.61", "58.60", "78.5", "PEF", "[L/s]", "7.27", "5.34", "73.4", "MEF 75", "[L/s]", "6.51", "1.94", "29.8", "MEF 50", "[L/s]", "3.73", "0.72", "19.4", "MEF 25", "[L/s]", "1.15", "0.25", "21.9", "MMEF 75/25", "[L/s]", "2.89", "0.60", "20.9", "FET", "[s]", "7.16", "FET PEF", "[s]", "0.05", "V backextrapolation ex", "[L]", "0.07", "V backextrapol. % FVC", "[%]", "2.82", "MVV", "[L/min]", "101.83", "37.40", "36.7", "FEV 1 % VC MAX", "[%]", "74.61", "58.60", "78.5", "VC EX", "[L]", "3.46", "2.48", "71.6", "FRV", "[L]", "0.93", "IRV", "[L]", "0.80", "VT", "[L]", "0.34", "1.65", "491.4", "IC", "[L]", "2.53", "2.45", "96.9", "BF", "[1/min]", "20.00", "13.38", "66.9", "MV", "[L/min]", "6.71", "22.08", "328.9", "VC MAX", "[L]", "3.46", "2.48", "71.6", "Date", "25/12/26", "Time", "9:49:52", "结论：", "1. 中重度混合性肺通气功能障碍。", "轻度弥散功能障碍", "操作员：刘角玲"]

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
2026-08-05 06:08:52,836 INFO     29 [qwen-vl-text] coord API raw response (len=7167):
[
	{"text": "肺常规通气检查报告", "bbox": [370, 106, 607, 126]},
	{"text": "测试号：0022542899", "bbox": [176, 128, 398, 140]},
	{"text": "姓名：", "bbox": [176, 140, 218, 152]},
	{"text": "出生日期：", "bbox": [176, 152, 248, 164]},
	{"text": "身高：165 cm", "bbox": [176, 164, 376, 177]},
	{"text": "临床印象：支气管哮喘", "bbox": [176, 177, 409, 189]},
	{"text": "住址：内蒙古自治区乌兰察布", "bbox": [176, 189, 492, 202]},
	{"text": "科别：", "bbox": [176, 202, 214, 214]},
	{"text": "住院号：0022542899", "bbox": [667, 124, 750, 136]},
	{"text": "性别：男", "bbox": [667, 136, 685, 148]},
	{"text": "年龄：70 Years", "bbox": [667, 148, 734, 161]},
	{"text": "体重：47 kg", "bbox": [667, 161, 710, 174]},
	{"text": "吸烟史：否", "bbox": [667, 174, 685, 186]},
	{"text": "联系电话：", "bbox": [517, 189, 590, 201]},
	{"text": "主管医生：", "bbox": [517, 201, 590, 214]},
	{"text": "F/V ex", "bbox": [229, 238, 268, 247]},
	{"text": "F/V in", "bbox": [233, 346, 267, 355]},
	{"text": "Vol [L]", "bbox": [417, 240, 455, 251]},
	{"text": "Vol%VCmax", "bbox": [367, 296, 434, 305]},
	{"text": "VCmax", "bbox": [431, 311, 470, 320]},
	{"text": "Time [s]", "bbox": [502, 330, 547, 340]},
	{"text": "Vol [L]", "bbox": [690, 230, 728, 240]},
	{"text": "Time [s]", "bbox": [789, 327, 835, 337]},
	{"text": "FVC", "bbox": [92, 394, 119, 404]},
	{"text": "[L]", "bbox": [292, 393, 314, 406]},
	{"text": "3.34", "bbox": [462, 394, 497, 404]},
	{"text": "2.48", "bbox": [538, 394, 572, 404]},
	{"text": "74.0", "bbox": [613, 394, 652, 404]},
	{"text": "FEV 1", "bbox": [92, 407, 133, 417]},
	{"text": "[L]", "bbox": [292, 406, 314, 419]},
	{"text": "2.58", "bbox": [462, 407, 497, 417]},
	{"text": "1.45", "bbox": [538, 407, 572, 417]},
	{"text": "56.3", "bbox": [613, 407, 652, 417]},
	{"text": "FEV 2", "bbox": [92, 420, 134, 430]},
	{"text": "[L]", "bbox": [292, 419, 314, 432]},
	{"text": "1.82", "bbox": [538, 420, 572, 430]},
	{"text": "FEV 3", "bbox": [92, 433, 134, 443]},
	{"text": "[L]", "bbox": [292, 432, 314, 445]},
	{"text": "2.06", "bbox": [538, 433, 572, 443]},
	{"text": "FEV6", "bbox": [92, 446, 126, 456]},
	{"text": "[L]", "bbox": [292, 445, 314, 458]},
	{"text": "2.45", "bbox": [538, 446, 572, 456]},
	{"text": "FEV 1 % FVC", "bbox": [92, 459, 183, 469]},
	{"text": "[%]", "bbox": [292, 458, 314, 471]},
	{"text": "83.77", "bbox": [454, 459, 497, 469]},
	{"text": "58.60", "bbox": [530, 459, 572, 469]},
	{"text": "70.0", "bbox": [615, 459, 650, 469]},
	{"text": "FEV 1 % VC MAX", "bbox": [92, 471, 208, 481]},
	{"text": "[%]", "bbox": [292, 471, 314, 484]},
	{"text": "74.61", "bbox": [454, 471, 497, 481]},
	{"text": "58.60", "bbox": [530, 471, 572, 481]},
	{"text": "78.5", "bbox": [615, 471, 650, 481]},
	{"text": "PEF", "bbox": [92, 484, 117, 494]},
	{"text": "[L/s]", "bbox": [274, 483, 314, 496]},
	{"text": "7.27", "bbox": [462, 484, 497, 494]},
	{"text": "5.34", "bbox": [538, 484, 572, 494]},
	{"text": "73.4", "bbox": [615, 484, 650, 494]},
	{"text": "MEF 75", "bbox": [92, 497, 142, 507]},
	{"text": "[L/s]", "bbox": [274, 496, 314, 509]},
	{"text": "6.51", "bbox": [462, 497, 497, 507]},
	{"text": "1.94", "bbox": [538, 497, 572, 507]},
	{"text": "29.8", "bbox": [615, 497, 650, 507]},
	{"text": "MEF 50", "bbox": [92, 510, 142, 520]},
	{"text": "[L/s]", "bbox": [274, 509, 314, 522]},
	{"text": "3.73", "bbox": [462, 510, 497, 520]},
	{"text": "0.72", "bbox": [538, 510, 572, 520]},
	{"text": "19.4", "bbox": [615, 510, 650, 520]},
	{"text": "MEF 25", "bbox": [92, 523, 142, 533]},
	{"text": "[L/s]", "bbox": [274, 522, 314, 535]},
	{"text": "1.15", "bbox": [462, 523, 497, 533]},
	{"text": "0.25", "bbox": [538, 523, 572, 533]},
	{"text": "21.9", "bbox": [615, 523, 650, 533]},
	{"text": "MMEF 75/25", "bbox": [92, 536, 174, 546]},
	{"text": "[L/s]", "bbox": [274, 535, 314, 548]},
	{"text": "2.89", "bbox": [462, 536, 497, 546]},
	{"text": "0.60", "bbox": [538, 536, 572, 546]},
	{"text": "20.9", "bbox": [615, 536, 650, 546]},
	{"text": "FET", "bbox": [92, 549, 116, 559]},
	{"text": "[s]", "bbox": [292, 548, 314, 561]},
	{"text": "7.16", "bbox": [538, 549, 572, 559]},
	{"text": "FET PEF", "bbox": [92, 561, 150, 571]},
	{"text": "[s]", "bbox": [292, 561, 314, 574]},
	{"text": "0.05", "bbox": [538, 561, 572, 571]},
	{"text": "V backextrapolation ex", "bbox": [92, 574, 274, 584]},
	{"text": "[L]", "bbox": [292, 573, 314, 586]},
	{"text": "0.07", "bbox": [538, 574, 572, 584]},
	{"text": "V backextrapol. % FVC", "bbox": [92, 587, 265, 597]},
	{"text": "[%]", "bbox": [292, 586, 314, 599]},
	{"text": "2.82", "bbox": [538, 587, 572, 597]},
	{"text": "MVV", "bbox": [92, 600, 117, 610]},
	{"text": "[L/min]", "bbox": [257, 600, 312, 612]},
	{"text": "101.83", "bbox": [447, 600, 497, 610]},
	{"text": "37.40", "bbox": [530, 600, 572, 610]},
	{"text": "36.7", "bbox": [615, 600, 650, 610]},
	{"text": "FEV 1 % VC MAX", "bbox": [92, 613, 206, 623]},
	{"text": "[%]", "bbox": [292, 612, 314, 625]},
	{"text": "74.61", "bbox": [454, 613, 497, 623]},
	{"text": "58.60", "bbox": [530, 613, 572, 623]},
	{"text": "78.5", "bbox": [615, 613, 650, 623]},
	{"text": "VC EX", "bbox": [92, 639, 133, 649]},
	{"text": "[L]", "bbox": [292, 638, 314, 651]},
	{"text": "3.46", "bbox": [462, 639, 497, 649]},
	{"text": "2.48", "bbox": [538, 639, 572, 649]},
	{"text": "71.6", "bbox": [615, 639, 650, 649]},
	{"text": "FRV", "bbox": [92, 652, 116, 662]},
	{"text": "[L]", "bbox": [292, 651, 314, 664]},
	{"text": "0.93", "bbox": [459, 652, 497, 662]},
	{"text": "IRV", "bbox": [92, 665, 116, 675]},
	{"text": "[L]", "bbox": [292, 664, 314, 677]},
	{"text": "0.80", "bbox": [538, 665, 572, 675]},
	{"text": "VT", "bbox": [92, 678, 107, 688]},
	{"text": "[L]", "bbox": [292, 677, 314, 690]},
	{"text": "0.34", "bbox": [462, 678, 497, 688]},
	{"text": "1.65", "bbox": [538, 678, 572, 688]},
	{"text": "491.4", "bbox": [608, 678, 652, 688]},
	{"text": "IC", "bbox": [92, 691, 107, 701]},
	{"text": "[L]", "bbox": [292, 690, 314, 703]},
	{"text": "2.53", "bbox": [462, 691, 497, 701]},
	{"text": "2.45", "bbox": [538, 691, 572, 701]},
	{"text": "96.9", "bbox": [615, 691, 650, 701]},
	{"text": "BF", "bbox": [92, 704, 107, 714]},
	{"text": "[1/min]", "bbox": [257, 704, 312, 716]},
	{"text": "20.00", "bbox": [454, 704, 497, 714]},
	{"text": "13.38", "bbox": [530, 704, 572, 714]},
	{"text": "66.9", "bbox": [615, 704, 650, 714]},
	{"text": "MV", "bbox": [92, 717, 107, 727]},
	{"text": "[L/min]", "bbox": [257, 717, 312, 729]},
	{"text": "6.71", "bbox": [462, 717, 497, 727]},
	{"text": "22.08", "bbox": [530, 717, 572, 727]},
	{"text": "328.9", "bbox": [608, 717, 652, 727]},
	{"text": "VC MAX", "bbox": [92, 729, 142, 740]},
	{"text": "[L]", "bbox": [292, 729, 314, 742]},
	{"text": "3.46", "bbox": [462, 729, 497, 740]},
	{"text": "2.48", "bbox": [538, 729, 572, 740]},
	{"text": "71.6", "bbox": [615, 729, 650, 740]},
	{"text": "Date", "bbox": [92, 757, 125, 767]},
	{"text": "25/12/26", "bbox": [507, 756, 575, 767]},
	{"text": "Time", "bbox": [92, 770, 125, 780]},
	{"text": "9:49:52", "bbox": [504, 770, 575, 780]},
	{"text": "结论：", "bbox": [97, 795, 150, 812]},
	{"text": "1. 中重度混合性肺通气功能障碍。", "bbox": [112, 816, 363, 828]},
	{"text": "轻度弥散功能障碍", "bbox": [112, 828, 244, 840]},
	{"text": "操作员：刘角玲", "bbox": [792, 847, 950, 873]}
]
2026-08-05 06:08:52,837 INFO     29 [qwen-vl-text] coord API: raw_items=143, valid_items=143, elapsed=36.1s
2026-08-05 06:08:52,838 INFO     29 [qwen-vl-text] coord item[0]: text=肺常规通气检查报告, bbox=[370, 106, 607, 126]
2026-08-05 06:08:52,838 INFO     29 [qwen-vl-text] coord item[1]: text=测试号：0022542899, bbox=[176, 128, 398, 140]
2026-08-05 06:08:52,838 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[176, 140, 218, 152]
2026-08-05 06:08:52,838 INFO     29 [qwen-vl-text] coord item[3]: text=出生日期：, bbox=[176, 152, 248, 164]
2026-08-05 06:08:52,838 INFO     29 [qwen-vl-text] coord item[4]: text=身高：165 cm, bbox=[176, 164, 376, 177]
2026-08-05 06:08:52,838 INFO     29 [qwen-vl-text] coord item[5]: text=临床印象：支气管哮喘, bbox=[176, 177, 409, 189]
2026-08-05 06:08:52,838 INFO     29 [qwen-vl-text] coord item[6]: text=住址：内蒙古自治区乌兰察布, bbox=[176, 189, 492, 202]
2026-08-05 06:08:52,838 INFO     29 [qwen-vl-text] coord item[7]: text=科别：, bbox=[176, 202, 214, 214]
2026-08-05 06:08:52,838 INFO     29 [qwen-vl-text] coord item[8]: text=住院号：0022542899, bbox=[667, 124, 750, 136]
2026-08-05 06:08:52,838 INFO     29 [qwen-vl-text] coord item[9]: text=性别：男, bbox=[667, 136, 685, 148]
2026-08-05 06:08:52,838 INFO     29 [qwen-vl-text] coord item[10]: text=年龄：70 Years, bbox=[667, 148, 734, 161]
2026-08-05 06:08:52,838 INFO     29 [qwen-vl-text] coord item[11]: text=体重：47 kg, bbox=[667, 161, 710, 174]
2026-08-05 06:08:52,838 INFO     29 [qwen-vl-text] coord item[12]: text=吸烟史：否, bbox=[667, 174, 685, 186]
2026-08-05 06:08:52,838 INFO     29 [qwen-vl-text] coord item[13]: text=联系电话：, bbox=[517, 189, 590, 201]
2026-08-05 06:08:52,838 INFO     29 [qwen-vl-text] coord item[14]: text=主管医生：, bbox=[517, 201, 590, 214]
2026-08-05 06:08:52,838 INFO     29 [qwen-vl-text] coord item[15]: text=F/V ex, bbox=[229, 238, 268, 247]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[16]: text=F/V in, bbox=[233, 346, 267, 355]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[17]: text=Vol [L], bbox=[417, 240, 455, 251]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[18]: text=Vol%VCmax, bbox=[367, 296, 434, 305]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[19]: text=VCmax, bbox=[431, 311, 470, 320]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[20]: text=Time [s], bbox=[502, 330, 547, 340]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[21]: text=Vol [L], bbox=[690, 230, 728, 240]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[22]: text=Time [s], bbox=[789, 327, 835, 337]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[23]: text=FVC, bbox=[92, 394, 119, 404]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[24]: text=[L], bbox=[292, 393, 314, 406]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[25]: text=3.34, bbox=[462, 394, 497, 404]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[26]: text=2.48, bbox=[538, 394, 572, 404]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[27]: text=74.0, bbox=[613, 394, 652, 404]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[28]: text=FEV 1, bbox=[92, 407, 133, 417]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[29]: text=[L], bbox=[292, 406, 314, 419]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[30]: text=2.58, bbox=[462, 407, 497, 417]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[31]: text=1.45, bbox=[538, 407, 572, 417]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[32]: text=56.3, bbox=[613, 407, 652, 417]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[33]: text=FEV 2, bbox=[92, 420, 134, 430]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[34]: text=[L], bbox=[292, 419, 314, 432]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[35]: text=1.82, bbox=[538, 420, 572, 430]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[36]: text=FEV 3, bbox=[92, 433, 134, 443]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[37]: text=[L], bbox=[292, 432, 314, 445]
2026-08-05 06:08:52,839 INFO     29 [qwen-vl-text] coord item[38]: text=2.06, bbox=[538, 433, 572, 443]
2026-08-05 06:08:52,840 INFO     29 [qwen-vl-text] coord item[39]: text=FEV6, bbox=[92, 446, 126, 456]
2026-08-05 06:08:52,840 INFO     29 [qwen-vl-text] coord item[40]: text=[L], bbox=[292, 445, 314, 458]
2026-08-05 06:08:52,840 INFO     29 [qwen-vl-text] coord item[41]: text=2.45, bbox=[538, 446, 572, 456]
2026-08-05 06:08:52,840 INFO     29 [qwen-vl-text] coord item[42]: text=FEV 1 % FVC, bbox=[92, 459, 183, 469]
2026-08-05 06:08:52,840 INFO     29 [qwen-vl-text] coord item[43]: text=[%], bbox=[292, 458, 314, 471]
2026-08-05 06:08:52,840 INFO     29 [qwen-vl-text] coord item[44]: text=83.77, bbox=[454, 459, 497, 469]
2026-08-05 06:08:52,840 INFO     29 [qwen-vl-text] coord item[45]: text=58.60, bbox=[530, 459, 572, 469]
2026-08-05 06:08:52,840 INFO     29 [qwen-vl-text] coord item[46]: text=70.0, bbox=[615, 459, 650, 469]
2026-08-05 06:08:52,840 INFO     29 [qwen-vl-text] coord item[47]: text=FEV 1 % VC MAX, bbox=[92, 471, 208, 481]
2026-08-05 06:08:52,840 INFO     29 [qwen-vl-text] coord item[48]: text=[%], bbox=[292, 471, 314, 484]
2026-08-05 06:08:52,840 INFO     29 [qwen-vl-text] coord item[49]: text=74.61, bbox=[454, 471, 497, 481]
2026-08-05 06:08:52,840 INFO     29 [qwen-vl-text] coord item[50]: text=58.60, bbox=[530, 471, 572, 481]
2026-08-05 06:08:52,840 INFO     29 [qwen-vl-text] coord item[51]: text=78.5, bbox=[615, 471, 650, 481]
2026-08-05 06:08:52,840 INFO     29 [qwen-vl-text] coord item[52]: text=PEF, bbox=[92, 484, 117, 494]
2026-08-05 06:08:52,840 INFO     29 [qwen-vl-text] coord item[53]: text=[L/s], bbox=[274, 483, 314, 496]
2026-08-05 06:08:52,840 INFO     29 [qwen-vl-text] coord item[54]: text=7.27, bbox=[462, 484, 497, 494]
2026-08-05 06:08:52,841 INFO     29 [qwen-vl-text] coord item[55]: text=5.34, bbox=[538, 484, 572, 494]
2026-08-05 06:08:52,841 INFO     29 [qwen-vl-text] coord item[56]: text=73.4, bbox=[615, 484, 650, 494]
2026-08-05 06:08:52,841 INFO     29 [qwen-vl-text] coord item[57]: text=MEF 75, bbox=[92, 497, 142, 507]
2026-08-05 06:08:52,841 INFO     29 [qwen-vl-text] coord item[58]: text=[L/s], bbox=[274, 496, 314, 509]
2026-08-05 06:08:52,841 INFO     29 [qwen-vl-text] coord item[59]: text=6.51, bbox=[462, 497, 497, 507]
2026-08-05 06:08:52,841 INFO     29 [qwen-vl-text] coord item[60]: text=1.94, bbox=[538, 497, 572, 507]
2026-08-05 06:08:52,841 INFO     29 [qwen-vl-text] coord item[61]: text=29.8, bbox=[615, 497, 650, 507]
2026-08-05 06:08:52,841 INFO     29 [qwen-vl-text] coord item[62]: text=MEF 50, bbox=[92, 510, 142, 520]
2026-08-05 06:08:52,841 INFO     29 [qwen-vl-text] coord item[63]: text=[L/s], bbox=[274, 509, 314, 522]
2026-08-05 06:08:52,841 INFO     29 [qwen-vl-text] coord item[64]: text=3.73, bbox=[462, 510, 497, 520]
2026-08-05 06:08:52,841 INFO     29 [qwen-vl-text] coord item[65]: text=0.72, bbox=[538, 510, 572, 520]
2026-08-05 06:08:52,841 INFO     29 [qwen-vl-text] coord item[66]: text=19.4, bbox=[615, 510, 650, 520]
2026-08-05 06:08:52,841 INFO     29 [qwen-vl-text] coord item[67]: text=MEF 25, bbox=[92, 523, 142, 533]
2026-08-05 06:08:52,841 INFO     29 [qwen-vl-text] coord item[68]: text=[L/s], bbox=[274, 522, 314, 535]
2026-08-05 06:08:52,841 INFO     29 [qwen-vl-text] coord item[69]: text=1.15, bbox=[462, 523, 497, 533]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[70]: text=0.25, bbox=[538, 523, 572, 533]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[71]: text=21.9, bbox=[615, 523, 650, 533]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[72]: text=MMEF 75/25, bbox=[92, 536, 174, 546]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[73]: text=[L/s], bbox=[274, 535, 314, 548]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[74]: text=2.89, bbox=[462, 536, 497, 546]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[75]: text=0.60, bbox=[538, 536, 572, 546]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[76]: text=20.9, bbox=[615, 536, 650, 546]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[77]: text=FET, bbox=[92, 549, 116, 559]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[78]: text=[s], bbox=[292, 548, 314, 561]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[79]: text=7.16, bbox=[538, 549, 572, 559]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[80]: text=FET PEF, bbox=[92, 561, 150, 571]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[81]: text=[s], bbox=[292, 561, 314, 574]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[82]: text=0.05, bbox=[538, 561, 572, 571]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[83]: text=V backextrapolation ex, bbox=[92, 574, 274, 584]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[84]: text=[L], bbox=[292, 573, 314, 586]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[85]: text=0.07, bbox=[538, 574, 572, 584]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[86]: text=V backextrapol. % FVC, bbox=[92, 587, 265, 597]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[87]: text=[%], bbox=[292, 586, 314, 599]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[88]: text=2.82, bbox=[538, 587, 572, 597]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[89]: text=MVV, bbox=[92, 600, 117, 610]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[90]: text=[L/min], bbox=[257, 600, 312, 612]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[91]: text=101.83, bbox=[447, 600, 497, 610]
2026-08-05 06:08:52,842 INFO     29 [qwen-vl-text] coord item[92]: text=37.40, bbox=[530, 600, 572, 610]
2026-08-05 06:08:52,843 INFO     29 [qwen-vl-text] coord item[93]: text=36.7, bbox=[615, 600, 650, 610]
2026-08-05 06:08:52,843 INFO     29 [qwen-vl-text] coord item[94]: text=FEV 1 % VC MAX, bbox=[92, 613, 206, 623]
2026-08-05 06:08:52,843 INFO     29 [qwen-vl-text] coord item[95]: text=[%], bbox=[292, 612, 314, 625]
2026-08-05 06:08:52,843 INFO     29 [qwen-vl-text] coord item[96]: text=74.61, bbox=[454, 613, 497, 623]
2026-08-05 06:08:52,843 INFO     29 [qwen-vl-text] coord item[97]: text=58.60, bbox=[530, 613, 572, 623]
2026-08-05 06:08:52,843 INFO     29 [qwen-vl-text] coord item[98]: text=78.5, bbox=[615, 613, 650, 623]
2026-08-05 06:08:52,843 INFO     29 [qwen-vl-text] coord item[99]: text=VC EX, bbox=[92, 639, 133, 649]
2026-08-05 06:08:52,843 INFO     29 [qwen-vl-text] coord item[100]: text=[L], bbox=[292, 638, 314, 651]
2026-08-05 06:08:52,843 INFO     29 [qwen-vl-text] coord item[101]: text=3.46, bbox=[462, 639, 497, 649]
2026-08-05 06:08:52,843 INFO     29 [qwen-vl-text] coord item[102]: text=2.48, bbox=[538, 639, 572, 649]
2026-08-05 06:08:52,843 INFO     29 [qwen-vl-text] coord item[103]: text=71.6, bbox=[615, 639, 650, 649]
2026-08-05 06:08:52,843 INFO     29 [qwen-vl-text] coord item[104]: text=FRV, bbox=[92, 652, 116, 662]
2026-08-05 06:08:52,843 INFO     29 [qwen-vl-text] coord item[105]: text=[L], bbox=[292, 651, 314, 664]
2026-08-05 06:08:52,843 INFO     29 [qwen-vl-text] coord item[106]: text=0.93, bbox=[459, 652, 497, 662]
2026-08-05 06:08:52,843 INFO     29 [qwen-vl-text] coord item[107]: text=IRV, bbox=[92, 665, 116, 675]
2026-08-05 06:08:52,844 INFO     29 [qwen-vl-text] coord item[108]: text=[L], bbox=[292, 664, 314, 677]
2026-08-05 06:08:52,844 INFO     29 [qwen-vl-text] coord item[109]: text=0.80, bbox=[538, 665, 572, 675]
2026-08-05 06:08:52,844 INFO     29 [qwen-vl-text] coord item[110]: text=VT, bbox=[92, 678, 107, 688]
2026-08-05 06:08:52,845 INFO     29 [qwen-vl-text] coord item[111]: text=[L], bbox=[292, 677, 314, 690]
2026-08-05 06:08:52,845 INFO     29 [qwen-vl-text] coord item[112]: text=0.34, bbox=[462, 678, 497, 688]
2026-08-05 06:08:52,845 INFO     29 [qwen-vl-text] coord item[113]: text=1.65, bbox=[538, 678, 572, 688]
2026-08-05 06:08:52,845 INFO     29 [qwen-vl-text] coord item[114]: text=491.4, bbox=[608, 678, 652, 688]
2026-08-05 06:08:52,845 INFO     29 [qwen-vl-text] coord item[115]: text=IC, bbox=[92, 691, 107, 701]
2026-08-05 06:08:52,845 INFO     29 [qwen-vl-text] coord item[116]: text=[L], bbox=[292, 690, 314, 703]
2026-08-05 06:08:52,845 INFO     29 [qwen-vl-text] coord item[117]: text=2.53, bbox=[462, 691, 497, 701]
2026-08-05 06:08:52,845 INFO     29 [qwen-vl-text] coord item[118]: text=2.45, bbox=[538, 691, 572, 701]
2026-08-05 06:08:52,845 INFO     29 [qwen-vl-text] coord item[119]: text=96.9, bbox=[615, 691, 650, 701]
2026-08-05 06:08:52,845 INFO     29 [qwen-vl-text] coord item[120]: text=BF, bbox=[92, 704, 107, 714]
2026-08-05 06:08:52,845 INFO     29 [qwen-vl-text] coord item[121]: text=[1/min], bbox=[257, 704, 312, 716]
2026-08-05 06:08:52,845 INFO     29 [qwen-vl-text] coord item[122]: text=20.00, bbox=[454, 704, 497, 714]
2026-08-05 06:08:52,845 INFO     29 [qwen-vl-text] coord item[123]: text=13.38, bbox=[530, 704, 572, 714]
2026-08-05 06:08:52,845 INFO     29 [qwen-vl-text] coord item[124]: text=66.9, bbox=[615, 704, 650, 714]
2026-08-05 06:08:52,845 INFO     29 [qwen-vl-text] coord item[125]: text=MV, bbox=[92, 717, 107, 727]
2026-08-05 06:08:52,846 INFO     29 [qwen-vl-text] coord item[126]: text=[L/min], bbox=[257, 717, 312, 729]
2026-08-05 06:08:52,846 INFO     29 [qwen-vl-text] coord item[127]: text=6.71, bbox=[462, 717, 497, 727]
2026-08-05 06:08:52,846 INFO     29 [qwen-vl-text] coord item[128]: text=22.08, bbox=[530, 717, 572, 727]
2026-08-05 06:08:52,846 INFO     29 [qwen-vl-text] coord item[129]: text=328.9, bbox=[608, 717, 652, 727]
2026-08-05 06:08:52,846 INFO     29 [qwen-vl-text] coord item[130]: text=VC MAX, bbox=[92, 729, 142, 740]
2026-08-05 06:08:52,846 INFO     29 [qwen-vl-text] coord item[131]: text=[L], bbox=[292, 729, 314, 742]
2026-08-05 06:08:52,846 INFO     29 [qwen-vl-text] coord item[132]: text=3.46, bbox=[462, 729, 497, 740]
2026-08-05 06:08:52,846 INFO     29 [qwen-vl-text] coord item[133]: text=2.48, bbox=[538, 729, 572, 740]
2026-08-05 06:08:52,846 INFO     29 [qwen-vl-text] coord item[134]: text=71.6, bbox=[615, 729, 650, 740]
2026-08-05 06:08:52,846 INFO     29 [qwen-vl-text] coord item[135]: text=Date, bbox=[92, 757, 125, 767]
2026-08-05 06:08:52,846 INFO     29 [qwen-vl-text] coord item[136]: text=25/12/26, bbox=[507, 756, 575, 767]
2026-08-05 06:08:52,846 INFO     29 [qwen-vl-text] coord item[137]: text=Time, bbox=[92, 770, 125, 780]
2026-08-05 06:08:52,846 INFO     29 [qwen-vl-text] coord item[138]: text=9:49:52, bbox=[504, 770, 575, 780]
2026-08-05 06:08:52,846 INFO     29 [qwen-vl-text] coord item[139]: text=结论：, bbox=[97, 795, 150, 812]
2026-08-05 06:08:52,846 INFO     29 [qwen-vl-text] coord item[140]: text=1. 中重度混合性肺通气功能障碍。, bbox=[112, 816, 363, 828]
2026-08-05 06:08:52,846 INFO     29 [qwen-vl-text] coord item[141]: text=轻度弥散功能障碍, bbox=[112, 828, 244, 840]
2026-08-05 06:08:52,846 INFO     29 [qwen-vl-text] coord item[142]: text=操作员：刘角玲, bbox=[792, 847, 950, 873]
2026-08-05 06:08:52,848 INFO     29 [qwen-vl-text] page=2 — 143/143 coords, api_time=36.1s
2026-08-05 06:08:52,874 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3667065, prompt_len=1444
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["报告时间: 2025-12-26", "预计值 药前 %预计 药后1 改善率% 药后2 改善率% 药后3 改善率%", "FVC [L] 3.34 2.48 74.0 2.47 -0.28 2.52 1.90 2.59 4.57", "FEV 1 [L] 2.58 1.45 56.3 1.57 7.98 1.62 11.38 1.68 15.64", "FEV 1 % FVC [%] 83.77 58.60 70.0 63.46 8.29 64.05 9.30 64.81 10.59", "PEF [L/s] 7.27 5.34 73.4 5.97 11.92 6.55 22.75 6.30 18.12", "MEF 75 [L/s] 6.51 1.94 29.8 1.93 -0.49 2.25 15.90 2.48 27.48", "MEF 50 [L/s] 3.73 0.72 19.4 1.08 48.95 1.10 52.54 1.10 52.19", "MEF 25 [L/s] 1.15 0.25 21.9 0.37 49.20 0.35 40.24 0.38 51.20", "MMEF 75/25 [L/s] 2.89 0.60 20.9 0.82 35.86 0.83 37.61 0.89 46.55", "FET [s] 6.24 -12.85 7.29 1.83 7.07 -1.26", "FET PEF [s] 0.05 -10.65 0.04 -18.54 0.05 -3.25", "V backextrapol. % FVC [%] 3.10 10.19 2.50 -11.19 3.24 15.10", "Date", "Time 25/12/26 9:49:52$\\downarrow$ 25/12/26 10:34:27. 25/12/26 10:34:52.", "25/12/26 10:35:14."]

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
2026-08-05 06:09:06,188 INFO     29 [qwen-vl-text] coord API raw response (len=1474):
[
	{"text": "测试日期: 2025/12/26", "bbox": [690, 30, 805, 40]},
	{"text": "预计值 药前 %预计 药后1 改善率% 药后2 改善率% 药后3 改善率%", "bbox": [275, 297, 950, 313]},
	{"text": "FVC [L] 3.34 2.48 74.0 2.47 -0.28 2.52 1.90 2.59 4.57", "bbox": [35, 327, 950, 342]},
	{"text": "FEV 1 [L] 2.58 1.45 56.3 1.57 7.98 1.62 11.38 1.68 15.64", "bbox": [35, 342, 950, 356]},
	{"text": "FEV 1 % FVC [%] 83.77 58.60 70.0 63.46 8.29 64.05 9.30 64.81 10.59", "bbox": [35, 356, 950, 370]},
	{"text": "PEF [L/s] 7.27 5.34 73.4 5.97 11.92 6.55 22.75 6.30 18.12", "bbox": [35, 370, 950, 384]},
	{"text": "MEF 75 [L/s] 6.51 1.94 29.8 1.93 -0.49 2.25 15.90 2.48 27.48", "bbox": [35, 384, 950, 398]},
	{"text": "MEF 50 [L/s] 3.73 0.72 19.4 1.08 48.95 1.10 52.54 1.10 52.19", "bbox": [35, 398, 950, 412]},
	{"text": "MEF 25 [L/s] 1.15 0.25 21.9 0.37 49.20 0.35 40.24 0.38 51.20", "bbox": [35, 412, 950, 426]},
	{"text": "MMEF 75/25 [L/s] 2.89 0.60 20.9 0.82 35.86 0.83 37.61 0.89 46.55", "bbox": [35, 426, 950, 440]},
	{"text": "FET [s] 6.24 -12.85 7.29 1.83 7.07 -1.26", "bbox": [35, 440, 950, 454]},
	{"text": "FET PEF [s] 0.05 -10.65 0.04 -18.54 0.05 -3.25", "bbox": [35, 454, 950, 468]},
	{"text": "V backextrapol. % FVC [%] 3.10 10.19 2.50 -11.19 3.24 15.10", "bbox": [35, 468, 950, 482]},
	{"text": "Date", "bbox": [35, 497, 73, 509]},
	{"text": "Time 25/12/26 9:49:52$\\downarrow$ 25/12/26 10:34:27. 25/12/26 10:34:52.", "bbox": [35, 509, 700, 521]},
	{"text": "25/12/26 10:35:14.", "bbox": [788, 490, 858, 502]}
]
2026-08-05 06:09:06,188 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=13.3s
2026-08-05 06:09:06,188 INFO     29 [qwen-vl-text] coord item[0]: text=测试日期: 2025/12/26, bbox=[690, 30, 805, 40]
2026-08-05 06:09:06,188 INFO     29 [qwen-vl-text] coord item[1]: text=预计值 药前 %预计 药后1 改善率% 药后2 改善率% 药后3 改善率%, bbox=[275, 297, 950, 313]
2026-08-05 06:09:06,188 INFO     29 [qwen-vl-text] coord item[2]: text=FVC [L] 3.34 2.48 74.0 2.47 -0.28 2.52 1.90 2.59 4.57, bbox=[35, 327, 950, 342]
2026-08-05 06:09:06,188 INFO     29 [qwen-vl-text] coord item[3]: text=FEV 1 [L] 2.58 1.45 56.3 1.57 7.98 1.62 11.38 1.68 15.64, bbox=[35, 342, 950, 356]
2026-08-05 06:09:06,188 INFO     29 [qwen-vl-text] coord item[4]: text=FEV 1 % FVC [%] 83.77 58.60 70.0 63.46 8.29 64.05 9.30 64.81 10.59, bbox=[35, 356, 950, 370]
2026-08-05 06:09:06,188 INFO     29 [qwen-vl-text] coord item[5]: text=PEF [L/s] 7.27 5.34 73.4 5.97 11.92 6.55 22.75 6.30 18.12, bbox=[35, 370, 950, 384]
2026-08-05 06:09:06,188 INFO     29 [qwen-vl-text] coord item[6]: text=MEF 75 [L/s] 6.51 1.94 29.8 1.93 -0.49 2.25 15.90 2.48 27.48, bbox=[35, 384, 950, 398]
2026-08-05 06:09:06,188 INFO     29 [qwen-vl-text] coord item[7]: text=MEF 50 [L/s] 3.73 0.72 19.4 1.08 48.95 1.10 52.54 1.10 52.19, bbox=[35, 398, 950, 412]
2026-08-05 06:09:06,188 INFO     29 [qwen-vl-text] coord item[8]: text=MEF 25 [L/s] 1.15 0.25 21.9 0.37 49.20 0.35 40.24 0.38 51.20, bbox=[35, 412, 950, 426]
2026-08-05 06:09:06,188 INFO     29 [qwen-vl-text] coord item[9]: text=MMEF 75/25 [L/s] 2.89 0.60 20.9 0.82 35.86 0.83 37.61 0.89 46.55, bbox=[35, 426, 950, 440]
2026-08-05 06:09:06,188 INFO     29 [qwen-vl-text] coord item[10]: text=FET [s] 6.24 -12.85 7.29 1.83 7.07 -1.26, bbox=[35, 440, 950, 454]
2026-08-05 06:09:06,188 INFO     29 [qwen-vl-text] coord item[11]: text=FET PEF [s] 0.05 -10.65 0.04 -18.54 0.05 -3.25, bbox=[35, 454, 950, 468]
2026-08-05 06:09:06,188 INFO     29 [qwen-vl-text] coord item[12]: text=V backextrapol. % FVC [%] 3.10 10.19 2.50 -11.19 3.24 15.10, bbox=[35, 468, 950, 482]
2026-08-05 06:09:06,188 INFO     29 [qwen-vl-text] coord item[13]: text=Date, bbox=[35, 497, 73, 509]
2026-08-05 06:09:06,188 INFO     29 [qwen-vl-text] coord item[14]: text=Time 25/12/26 9:49:52$\downarrow$ 25/12/26 10:34:27. 25/12/26 10:34:52., bbox=[35, 509, 700, 521]
2026-08-05 06:09:06,188 INFO     29 [qwen-vl-text] coord item[15]: text=25/12/26 10:35:14., bbox=[788, 490, 858, 502]
2026-08-05 06:09:06,189 INFO     29 [qwen-vl-text] page=3 — 16/16 coords, api_time=13.3s
2026-08-05 06:09:06,189 INFO     29 [qwen-vl-text] new_positions (159):
[[2, 220.14999999999998, 361.16499999999996, 89.252, 106.092], [2, 104.72, 236.81, 107.776, 117.88], [2, 104.72, 129.71, 117.88, 127.984], [2, 104.72, 147.56, 127.984, 138.088], [2, 104.72, 223.72, 138.088, 149.034], [2, 104.72, 243.355, 149.034, 159.138], [2, 104.72, 292.74, 159.138, 170.084], [2, 104.72, 127.33, 170.084, 180.188], [2, 396.865, 446.25, 104.408, 114.512], [2, 396.865, 407.575, 114.512, 124.616], [2, 396.865, 436.72999999999996, 124.616, 135.56199999999998], [2, 396.865, 422.45, 135.56199999999998, 146.50799999999998], [2, 396.865, 407.575, 146.50799999999998, 156.612], [2, 307.615, 351.05, 159.138, 169.242], [2, 307.615, 351.05, 169.242, 180.188], [2, 136.255, 159.45999999999998, 200.396, 207.974], [2, 138.635, 158.86499999999998, 291.332, 298.90999999999997], [2, 248.11499999999998, 270.72499999999997, 202.07999999999998, 211.34199999999998], [2, 218.36499999999998, 258.22999999999996, 249.232, 256.81], [2, 256.445, 279.65, 261.86199999999997, 269.44], [2, 298.69, 325.465, 277.86, 286.28], [2, 410.54999999999995, 433.15999999999997, 193.66, 202.07999999999998], [2, 469.455, 496.825, 275.334, 283.75399999999996], [2, 54.739999999999995, 70.80499999999999, 331.748, 340.168], [2, 173.73999999999998, 186.82999999999998, 330.906, 341.852], [2, 274.89, 295.715, 331.748, 340.168], [2, 320.11, 340.34, 331.748, 340.168], [2, 364.73499999999996, 387.94, 331.748, 340.168], [2, 54.739999999999995, 79.13499999999999, 342.69399999999996, 351.114], [2, 173.73999999999998, 186.82999999999998, 341.852, 352.798], [2, 274.89, 295.715, 342.69399999999996, 351.114], [2, 320.11, 340.34, 342.69399999999996, 351.114], [2, 364.73499999999996, 387.94, 342.69399999999996, 351.114], [2, 54.739999999999995, 79.72999999999999, 353.64, 362.06], [2, 173.73999999999998, 186.82999999999998, 352.798, 363.74399999999997], [2, 320.11, 340.34, 353.64, 362.06], [2, 54.739999999999995, 79.72999999999999, 364.586, 373.006], [2, 173.73999999999998, 186.82999999999998, 363.74399999999997, 374.69], [2, 320.11, 340.34, 364.586, 373.006], [2, 54.739999999999995, 74.97, 375.532, 383.952], [2, 173.73999999999998, 186.82999999999998, 374.69, 385.63599999999997], [2, 320.11, 340.34, 375.532, 383.952], [2, 54.739999999999995, 108.88499999999999, 386.478, 394.89799999999997], [2, 173.73999999999998, 186.82999999999998, 385.63599999999997, 396.582], [2, 270.13, 295.715, 386.478, 394.89799999999997], [2, 315.34999999999997, 340.34, 386.478, 394.89799999999997], [2, 365.925, 386.75, 386.478, 394.89799999999997], [2, 54.739999999999995, 123.75999999999999, 396.582, 405.002], [2, 173.73999999999998, 186.82999999999998, 396.582, 407.52799999999996], [2, 270.13, 295.715, 396.582, 405.002], [2, 315.34999999999997, 340.34, 396.582, 405.002], [2, 365.925, 386.75, 396.582, 405.002], [2, 54.739999999999995, 69.615, 407.52799999999996, 415.948], [2, 163.03, 186.82999999999998, 406.686, 417.632], [2, 274.89, 295.715, 407.52799999999996, 415.948], [2, 320.11, 340.34, 407.52799999999996, 415.948], [2, 365.925, 386.75, 407.52799999999996, 415.948], [2, 54.739999999999995, 84.49, 418.474, 426.894], [2, 163.03, 186.82999999999998, 417.632, 428.578], [2, 274.89, 295.715, 418.474, 426.894], [2, 320.11, 340.34, 418.474, 426.894], [2, 365.925, 386.75, 418.474, 426.894], [2, 54.739999999999995, 84.49, 429.41999999999996, 437.84], [2, 163.03, 186.82999999999998, 428.578, 439.524], [2, 274.89, 295.715, 429.41999999999996, 437.84], [2, 320.11, 340.34, 429.41999999999996, 437.84], [2, 365.925, 386.75, 429.41999999999996, 437.84], [2, 54.739999999999995, 84.49, 440.366, 448.786], [2, 163.03, 186.82999999999998, 439.524, 450.46999999999997], [2, 274.89, 295.715, 440.366, 448.786], [2, 320.11, 340.34, 440.366, 448.786], [2, 365.925, 386.75, 440.366, 448.786], [2, 54.739999999999995, 103.53, 451.312, 459.73199999999997], [2, 163.03, 186.82999999999998, 450.46999999999997, 461.416], [2, 274.89, 295.715, 451.312, 459.73199999999997], [2, 320.11, 340.34, 451.312, 459.73199999999997], [2, 365.925, 386.75, 451.312, 459.73199999999997], [2, 54.739999999999995, 69.02, 462.258, 470.678], [2, 173.73999999999998, 186.82999999999998, 461.416, 472.36199999999997], [2, 320.11, 340.34, 462.258, 470.678], [2, 54.739999999999995, 89.25, 472.36199999999997, 480.782], [2, 173.73999999999998, 186.82999999999998, 472.36199999999997, 483.308], [2, 320.11, 340.34, 472.36199999999997, 480.782], [2, 54.739999999999995, 163.03, 483.308, 491.728], [2, 173.73999999999998, 186.82999999999998, 482.466, 493.412], [2, 320.11, 340.34, 483.308, 491.728], [2, 54.739999999999995, 157.67499999999998, 494.25399999999996, 502.674], [2, 173.73999999999998, 186.82999999999998, 493.412, 504.358], [2, 320.11, 340.34, 494.25399999999996, 502.674], [2, 54.739999999999995, 69.615, 505.2, 513.62], [2, 152.915, 185.64, 505.2, 515.304], [2, 265.965, 295.715, 505.2, 513.62], [2, 315.34999999999997, 340.34, 505.2, 513.62], [2, 365.925, 386.75, 505.2, 513.62], [2, 54.739999999999995, 122.57, 516.146, 524.566], [2, 173.73999999999998, 186.82999999999998, 515.304, 526.25], [2, 270.13, 295.715, 516.146, 524.566], [2, 315.34999999999997, 340.34, 516.146, 524.566], [2, 365.925, 386.75, 516.146, 524.566], [2, 54.739999999999995, 79.13499999999999, 538.038, 546.458], [2, 173.73999999999998, 186.82999999999998, 537.196, 548.1419999999999], [2, 274.89, 295.715, 538.038, 546.458], [2, 320.11, 340.34, 538.038, 546.458], [2, 365.925, 386.75, 538.038, 546.458], [2, 54.739999999999995, 69.02, 548.984, 557.404], [2, 173.73999999999998, 186.82999999999998, 548.1419999999999, 559.088], [2, 273.10499999999996, 295.715, 548.984, 557.404], [2, 54.739999999999995, 69.02, 559.93, 568.35], [2, 173.73999999999998, 186.82999999999998, 559.088, 570.034], [2, 320.11, 340.34, 559.93, 568.35], [2, 54.739999999999995, 63.665, 570.876, 579.2959999999999], [2, 173.73999999999998, 186.82999999999998, 570.034, 580.98], [2, 274.89, 295.715, 570.876, 579.2959999999999], [2, 320.11, 340.34, 570.876, 579.2959999999999], [2, 361.76, 387.94, 570.876, 579.2959999999999], [2, 54.739999999999995, 63.665, 581.822, 590.242], [2, 173.73999999999998, 186.82999999999998, 580.98, 591.9259999999999], [2, 274.89, 295.715, 581.822, 590.242], [2, 320.11, 340.34, 581.822, 590.242], [2, 365.925, 386.75, 581.822, 590.242], [2, 54.739999999999995, 63.665, 592.768, 601.188], [2, 152.915, 185.64, 592.768, 602.872], [2, 270.13, 295.715, 592.768, 601.188], [2, 315.34999999999997, 340.34, 592.768, 601.188], [2, 365.925, 386.75, 592.768, 601.188], [2, 54.739999999999995, 63.665, 603.7139999999999, 612.134], [2, 152.915, 185.64, 603.7139999999999, 613.818], [2, 274.89, 295.715, 603.7139999999999, 612.134], [2, 315.34999999999997, 340.34, 603.7139999999999, 612.134], [2, 361.76, 387.94, 603.7139999999999, 612.134], [2, 54.739999999999995, 84.49, 613.818, 623.0799999999999], [2, 173.73999999999998, 186.82999999999998, 613.818, 624.764], [2, 274.89, 295.715, 613.818, 623.0799999999999], [2, 320.11, 340.34, 613.818, 623.0799999999999], [2, 365.925, 386.75, 613.818, 623.0799999999999], [2, 54.739999999999995, 74.375, 637.394, 645.814], [2, 301.66499999999996, 342.125, 636.552, 645.814], [2, 54.739999999999995, 74.375, 648.34, 656.76], [2, 299.88, 342.125, 648.34, 656.76], [2, 57.714999999999996, 89.25, 669.39, 683.704], [2, 66.64, 215.98499999999999, 687.072, 697.1759999999999], [2, 66.64, 145.18, 697.1759999999999, 707.28], [2, 471.23999999999995, 565.25, 713.174, 735.066], [3, 410.54999999999995, 478.97499999999997, 25.259999999999998, 33.68], [3, 163.625, 565.25, 250.07399999999998, 263.546], [3, 20.825, 565.25, 275.334, 287.964], [3, 20.825, 565.25, 287.964, 299.752], [3, 20.825, 565.25, 299.752, 311.53999999999996], [3, 20.825, 565.25, 311.53999999999996, 323.328], [3, 20.825, 565.25, 323.328, 335.116], [3, 20.825, 565.25, 335.116, 346.904], [3, 20.825, 565.25, 346.904, 358.692], [3, 20.825, 565.25, 358.692, 370.47999999999996], [3, 20.825, 565.25, 370.47999999999996, 382.268], [3, 20.825, 565.25, 382.268, 394.056], [3, 20.825, 565.25, 394.056, 405.844], [3, 20.825, 43.434999999999995, 418.474, 428.578], [3, 20.825, 416.5, 428.578, 438.68199999999996], [3, 468.85999999999996, 510.51, 412.58, 422.68399999999997]]
2026-08-05 06:09:06,189 INFO     29 [qwen-vl-text] ═══ DONE ═══ 159 positions, pages=2, time=60.0s
2026-08-05 06:09:06,202 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-05 06:09:06,202 INFO     29 [Trace] task=c9e5a6ba | doc=麦济WZWA222.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items, types={'ExaminationReport': 1}", "html": "", "json": "239 items", "markdown": "", "text": "", "name": "麦济WZWA222.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 1, \"chunks_Medication\": 1}"}
2026-08-05 06:09:06,202 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-05 06:09:06,203 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T06:09:06.202+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 23, "failed": 0, "current": {"c9e5a6ba909311f1a3da71efcdd7cc1f": {"id": "c9e5a6ba909311f1a3da71efcdd7cc1f", "doc_id": "c9526904909311f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWZWA222.pdf", "type": "pdf", "location": "\u9ea6\u6d4eWZWA222.pdf", "size": 9742831, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785909984712, "task_type": "dataflow", "root_trace_id": "61b0a1cf64e14ac9b4fd9e1374842905", "root_traceparent": "00-61b0a1cf64e14ac9b4fd9e1374842905-58f4c254cd5a4a04-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 06:09:06,204 INFO     29 [ChunkMerger] Merged 4 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1} (filtered 5 noise chunks)
2026-08-05 06:09:06,554 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-05 06:09:06,554 INFO     29 [Trace] task=c9e5a6ba | doc=麦济WZWA222.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "4 items, types={'OutpatientRecord': 2, 'MedicationRecord': 1, 'ExaminationReport': 1}", "name": "麦济WZWA222.pdf"}
2026-08-05 06:09:06,554 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-05 06:09:06,600 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1785909987130, 'update_date': datetime.datetime(2026, 8, 5, 6, 6, 27), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 245437, 'status': '1'}
2026-08-05 06:09:06,822 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=内蒙古医科大学附属医院门诊病历
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
Date
25/12/26
Time
9:49:52
结论：
1. 中重度混合性肺通气功能障碍。
轻度弥散功能障碍
操作员：刘角玲
报告时间: 2025-12-26
预计值 药前 %预计 药后1 改善率% 药后2 改善率% 药后3 改善率%
FVC [L] 3.34 2.48 74.0 2.47 -0.28 2.52 1.90 2.59 4.57
FEV 1 [L] 2.58 1.45 56.3 1.57 7.98 1.62 11.38 1.68 15.64
FEV 1 % FVC [%] 83.77 58.60 70.0 63.46 8.29 64.05 9.30 64.81 10.59
PEF [L/s] 7.27 5.34 73.4 5.97 11.92 6.55 22.75 6.30 18.12
MEF 75 [L/s] 6.51 1.94 29.8 1.93 -0.49 2.25 15.90 2.48 27.48
MEF 50 [L/s] 3.73 0.72 19.4 1.08 48.95 1.10 52.54 1.10 52.19
MEF 25 [L/s] 1.15 0.25 21.9 0.37 49.20 0.35 40.24 0.38 51.20
MMEF 75/25 [L/s] 2.89 0.60 20.9 0.82 35.86 0.83 37.61 0.89 46.55
FET [s] 6.24 -12.85 7.29 1.83 7.07 -1.26
FET PEF [s] 0.05 -10.65 0.04 -18.54 0.05 -3.25
V backextrapol. % FVC [%] 3.10 10.19 2.50 -11.19 3.24 15.10
Date
Time 25/12/26 9:49:52$\downarrow$ 25/12/26 10:34:27. 25/12/26 10:34:52.
25/12/26 10:35:14.
2026-08-05 06:09:07,149 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-05 06:09:07,149 INFO     29 [Trace] task=c9e5a6ba | doc=麦济WZWA222.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "4 items, types={'OutpatientRecord': 2, 'MedicationRecord': 1, 'ExaminationReport': 1}", "name": "麦济WZWA222.pdf", "embedding_token_consumption": 2259}
2026-08-05 06:09:07,149 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-05 06:09:08,655 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-05 06:09:08,655 INFO     29 [Trace] task=c9e5a6ba | doc=麦济WZWA222.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":4,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-05 06:09:08,658 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 06:09:08,658 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 06:09:08,658 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 06:09:08,658 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 06:09:08,663 INFO     29 set_progress(c9e5a6ba909311f1a3da71efcdd7cc1f), progress: 0.82, progress_msg: 06:09:08 [DOC Engine]:
Start to index...
2026-08-05 06:09:08,687 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.018s]
2026-08-05 06:09:08,690 INFO     29 set_progress(c9e5a6ba909311f1a3da71efcdd7cc1f), progress: 0.8250000000000001, progress_msg: 
2026-08-05 06:09:08,695 INFO     29 set_progress(c9e5a6ba909311f1a3da71efcdd7cc1f), progress: 1.0, progress_msg: 06:09:08 Indexing done (0.03s). Task done (147.34s)
2026-08-05 06:09:08,698 INFO     29 [Done], chunks(4), token(2259), elapsed:147.34
2026-08-05 06:09:08,764 INFO     29 handle_task done for task {"id": "c9e5a6ba909311f1a3da71efcdd7cc1f", "doc_id": "c9526904909311f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWZWA222.pdf", "type": "pdf", "location": "\u9ea6\u6d4eWZWA222.pdf", "size": 9742831, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1785909984712, "task_type": "dataflow", "root_trace_id": "61b0a1cf64e14ac9b4fd9e1374842905", "root_traceparent": "00-61b0a1cf64e14ac9b4fd9e1374842905-58f4c254cd5a4a04-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
