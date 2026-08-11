# 基准结果：LYBI-艾特美哮喘(1).pdf

## 基本信息

- 文件：`LYBI-艾特美哮喘(1).pdf`
- 大小：2168.4 KB
- PDF 总页数：3
- doc_id：`1ff3926094bd11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T21:12:22  完成时间：2026-08-10T21:14:54  耗时：151.3s
- progress_msg：`13:14:50 Indexing done (0.03s). Task done (139.24s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 0f704148 | 1 | 1-1 | 新乡市第二人民医院 门（急）诊病历 门诊号： 姓名 性别 男性 年龄 35岁 婚 |
| 2 | 5b30abbd | 2 | 1-2 | 2 肺功能测验结果 新乡市第二人民医院 呼吸科 12323 FVC PRE FE |
| 3 | 1c0e5b50 | 1 | 3-3 | 肺功能检验结果 新乡市第二人民医院 呼吸科 12323 FVC FEV1 FEV |

- chunks 总数：3
- 各 chunk 页数合计（含跨页重复）：4
- 页码并集：`[1, 2, 3]`
- 覆盖页数：3 / 3；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 1 | 0 | 1 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 2 | 2 | 2 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 1, "ExaminationReport": 2}`
- ChunkMerger：`{"found": true, "merged": 3, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 2, "Extractor:Progress": 1}, "filtered_noise": 7}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 13:14:49,654 INFO     29 [ChunkMerger] Merged 3 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 13:12:23,941 INFO     29 handle_task begin for task {"id": "2031b7c094bd11f1bd9827cf206dfa2d", "doc_id": "1ff3926094bd11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LYBI-\u827e\u7279\u7f8e\u54ee\u5598(1).pdf", "type": "pdf", "location": "LYBI-\u827e\u7279\u7f8e\u54ee\u5598(1).pdf", "size": 2220448, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367543508, "task_type": "dataflow", "root_trace_id": "e8588e7f2a8f4f7ea72bfd924542e9bc", "root_traceparent": "00-e8588e7f2a8f4f7ea72bfd924542e9bc-f1b6b538ed925a47-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 13:12:24,131 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 13:12:24,238 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 13:12:24,249 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:12:24,249 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 13:12:24,249 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 13:12:24,254 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 13:12:24,254 INFO     29 ============================================================
2026-08-10 13:12:24,254 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 13:12:24,254 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 13:12:24,254 INFO     29 ============================================================
2026-08-10 13:12:24,254 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 13:12:24,254 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 13:12:24,256 INFO     29 No torch found.
2026-08-10 13:12:25,289 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=3
2026-08-10 13:12:25,859 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3056783, prompt_len=764
2026-08-10 13:12:27,989 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:12:27,991 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 13:12:28,013 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3056783, prompt_len=401
2026-08-10 13:12:31,889 INFO     29 [qwen-vl-parser] text API response (len=592):
["新乡市第二人民医院", "门（急）诊病历", "门诊号：", "姓名", "性别", "男性", "年龄", "35岁", "婚姻", "已婚", "职业", "工人", "籍贯", "河南省新乡市", "临时住址", "河南省新乡市卫滨区", "永久住址或工作单位", "联系人", "联系人关系", "本人或户主", "联系电话", "就诊类别", "初诊", "是否需下转至基层医疗机构", "否", "建议下转的基层医疗机构/持续性医疗机构", "是否流感样病例", "否", "应检人员类别", "就诊科室", "呼吸内科门诊", "就诊日期", "2025-05-28", "发病日期", "主诉", "发作性咳嗽、咳痰、胸闷、气喘2年", "现病史", "发作性咳嗽、咳痰、胸闷、气喘2年", "既往史", "无高血压史。", "个人史", "无吸烟史。", "婚育史", "已婚", "过敏史", "无", "家族史", "体格检查", "T 36℃, P", "次/分, R", "次/分, BP", "/", "mmHg, BMI", "/", ",", "辅助检查", "无", "疾病诊断", "西医诊断", "1、支气管哮喘(支气管哮喘)", "治疗意见", "检查", "建议", "接诊医生", "签名时间", "医疗业务专用章", "2", ""]
2026-08-10 13:12:31,892 INFO     29 [qwen-vl-parser] page=1 text: 67 lines (bbox 0-66)
2026-08-10 13:12:31,892 INFO     29 [qwen-vl-parser] page=1 text: 67 sections
2026-08-10 13:12:32,017 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=968778, prompt_len=764
2026-08-10 13:12:33,482 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 13:12:33,482 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 13:12:33,498 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=968778, prompt_len=401
2026-08-10 13:12:41,326 INFO     29 [qwen-vl-parser] text API response (len=1621):
["肺功能测验结果", "新乡市第二人民医院", "呼吸科", "12323", "FVC", "PRE", "FEV1", "PRE", "FEV1%", "PRE", "应诊日期 2025/5/28", "病人号码 W", "姓名", "出生日期 1990/2/5", "人种 中国人", "吸烟 非吸烟者", "患者组", "年龄 35", "性别 男", "高度, cm 170", "重量, kg 85", "BMI 29.41", "包-年", "14", "12", "10", "8", "6", "4", "2", "0", "-2", "-4", "8", "7", "6", "5", "4", "3", "2", "1", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "时间(s)", "已预测的", "质量控制等级: D 变化性: FEV1=0.08L (2.26%), FVC=0.31L (5.56%)", "1 Acceptable trials", "评估", "轻度的阻塞", "WARNING: FEV1/EVC 前 = 39%", "前/测验日期 2025/5/28 17:51:59", "参数", "LLN", "预计", "Best", "%预计", "Z-score", "前 # 1", "前 # 2", "前 # 3", "POST", "%预计", "%激发", "FVC", "L", "3.47", "4.52", "5.89*", "130", "5.89", "5.58", "5.10", "*", "FEV1", "L", "2.91", "3.77", "3.62*", "96", "3.62", "3.50", "3.54", "*", "FEV1/FVC", "%", "73.8", "84.0", "61.5*", "73", "61.5", "62.7", "69.4", "*", "PEF", "L/s", "5.34", "8.76", "5.08*", "58", "4.54", "4.70", "5.08", "*", "ELA", "年", "35", "40", "114", "40", "44", "43", "FEF2575", "L/s", "2.27", "4.05", "2.37", "58", "2.37", "2.39", "2.68", "FET", "s", "6.00", "6.73", "112", "6.73", "6.17", "6.33", "FIVC", "L", "3.47", "4.52", "4.56", "101", "4.56", "4.50", "4.52", "IVC", "L", "3.47", "4.52", "EVC", "L", "3.47", "4.52", "9.38", "207", "VC", "L", "3.47", "4.52", "9.38", "207", "FEV1/VC", "%", "73.8", "84.0", "38.6", "46", "38.6", "37.3", "37.7", "IC", "L", "3.03", "4.50", "148", "MVV", "L/min", "136.2", "99.8", "73", "*全部曲线之最佳值 - BTPS 1.073 29 ° C (84.2 ° F) - 已预测的 Knudson", "结论", "支气管舒张试验阳性。", "签名", "所用仪器", "Spirolab III S/N 313469", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 13:12:41,328 INFO     29 [qwen-vl-parser] page=2 text: 190 lines (bbox 67-256)
2026-08-10 13:12:41,328 INFO     29 [qwen-vl-parser] page=2 text: 190 sections
2026-08-10 13:12:41,448 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=910055, prompt_len=764
2026-08-10 13:12:43,113 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-05-28"
}
```
2026-08-10 13:12:43,114 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=2025-05-28
2026-08-10 13:12:43,121 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=910055, prompt_len=401
2026-08-10 13:12:49,959 INFO     29 [qwen-vl-parser] text API response (len=1263):
["肺功能检验结果", "新乡市第二人民医院", "呼吸科", "12323", "FVC", "FEV1", "FEV1%", "PRE", "PRE", "PRE", "应诊日期 2025/5/28", "病人号码", "年龄 85", "姓氏", "性别 男", "名字", "高度, cm 170", "出生日期 1990/2/5", "重量, kg 85", "人种 中国人", "BMI 29.41", "吸烟 非吸烟者", "患者组 包-年", "14", "12", "10", "8", "6", "4", "2", "0", "-2", "-4", "8", "7", "6", "5", "4", "3", "2", "1", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "时间(s)", "@已预测的", "质量控制等级: D 变化性: FEV1=0.06L (2.63%), FVC=0.45L (10.23%)", "1 Acceptable trials", "评估", "中度的阻塞.", "WARNING: FEF2575 前 = 39%预测, FEV1/EVC 前 = 45%", "前/测验日期 2025/5/28 17:15:41", "参数 LLN 预计 Best %预计 Z-score 前 #1 前 #2 前 #3 POST %预计 %激发", "FVC L 3.47 4.52 4.85* 107 4.85 4.37 4.40 *", "FEV1 L 2.91 3.77 2.34* 62 2.13 2.34 2.28 *", "FEV1/FVC % 73.8 84.0 48.2* 57 43.9 53.5 51.8 *", "PEF L/s 5.34 8.76 2.71* 31 2.71 2.34 2.67 *", "ELA 年 35 91 260 91 84 86", "FEF2575 L/s 2.27 4.05 1.57 39 1.57 1.80 1.57", "FET s 6.00 7.32 122 7.32 5.88 5.68", "FIVC L 3.47 4.52 3.86 85 3.86 4.20 4.24", "IVC L 3.47 4.52", "EVC L 3.47 4.52 5.16 114", "VC L 3.47 4.52 5.16 114", "FEV1/VC % 73.8 84.0 41.3 49", "IC L 3.03 3.58 118", "MVV L/min 136.2 42.9 31", "*全部曲线之最佳值 - BTPS 1.082 27 °C (80.6 °F) - 已预测的 Knudson", "结论", "签名", "所用仪器", "Spirolab III S/N 313469"]
2026-08-10 13:12:49,960 INFO     29 [qwen-vl-parser] page=3 text: 85 lines (bbox 257-341)
2026-08-10 13:12:49,960 INFO     29 [qwen-vl-parser] page=3 text: 85 sections
2026-08-10 13:12:49,960 INFO     29 [qwen-vl-parser] parse_pdf done: 342 sections from 3 pages.
2026-08-10 13:12:49,983 INFO     29 Close text detector.
2026-08-10 13:12:50,421 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:12:50.420+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 41, "failed": 0, "current": {"2031b7c094bd11f1bd9827cf206dfa2d": {"id": "2031b7c094bd11f1bd9827cf206dfa2d", "doc_id": "1ff3926094bd11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LYBI-\u827e\u7279\u7f8e\u54ee\u5598(1).pdf", "type": "pdf", "location": "LYBI-\u827e\u7279\u7f8e\u54ee\u5598(1).pdf", "size": 2220448, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367543508, "task_type": "dataflow", "root_trace_id": "e8588e7f2a8f4f7ea72bfd924542e9bc", "root_traceparent": "00-e8588e7f2a8f4f7ea72bfd924542e9bc-f1b6b538ed925a47-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:12:50,432 INFO     29 Close text recognizer.
2026-08-10 13:12:50,820 INFO     29 Close recognizer.
2026-08-10 13:12:51,194 INFO     29 Close recognizer.
2026-08-10 13:12:51,931 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 13:12:51,931 INFO     29 [Trace] task=2031b7c0 | doc=LYBI-艾特美哮喘(1).pdf | Parser:MedLink | outputs={"html": "", "json": "342 items", "markdown": "", "text": "", "name": "LYBI-艾特美哮喘(1).pdf", "output_format": "json"}
2026-08-10 13:12:51,931 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 13:12:51,958 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:12:51,959 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 新乡市第二人民医院\n[BBOX-1] 门（急）诊病历\n[BBOX-2] 门诊号：\n[BBOX-3] 姓名\n[BBOX-4] 性别\n[BBOX-5] 男性\n[BBOX-6] 年龄\n[BBOX-7] 35岁\n[BBOX-8] 婚姻\n[BBOX-9] 已婚\n[BBOX-10] 职业\n[BBOX-11] 工人\n[BBOX-12] 籍贯\n[BBOX-13] 河南省新乡市\n[BBOX-14] 临时住址\n[BBOX-15] 河南省新乡市卫滨区\n[BBOX-16] 永久住址或工作单位\n[BBOX-17] 联系人\n[BBOX-18] 联系人关系\n[BBOX-19] 本人或户主\n[BBOX-20] 联系电话\n[BBOX-21] 就诊类别\n[BBOX-22] 初诊\n[BBOX-23] 是否需下转至基层医疗机构\n[BBOX-24] 否\n[BBOX-25] 建议下转的基层医疗机构/持续性医疗机构\n[BBOX-26] 是否流感样病例\n[BBOX-27] 否\n[BBOX-28] 应检人员类别\n[BBOX-29] 就诊科室\n[BBOX-30] 呼吸内科门诊\n[BBOX-31] 就诊日期\n[BBOX-32] 2025-05-28\n[BBOX-33] 发病日期\n[BBOX-34] 主诉\n[BBOX-35] 发作性咳嗽、咳痰、胸闷、气喘2年\n[BBOX-36] 现病史\n[BBOX-37] 发作性咳嗽、咳痰、胸闷、气喘2年\n[BBOX-38] 既往史\n[BBOX-39] 无高血压史。\n[BBOX-40] 个人史\n[BBOX-41] 无吸烟史。\n[BBOX-42] 婚育史\n[BBOX-43] 已婚\n[BBOX-44] 过敏史\n[BBOX-45] 无\n[BBOX-46] 家族史\n[BBOX-47] 体格检查\n[BBOX-48] T 36℃, P\n[BBOX-49] 次/分, R\n[BBOX-50] 次/分, BP\n[BBOX-51] /\n[BBOX-52] mmHg, BMI\n[BBOX-53] /\n[BBOX-54] ,\n[BBOX-55] 辅助检查\n[BBOX-56] 无\n[BBOX-57] 疾病诊断\n[BBOX-58] 西医诊断\n[BBOX-59] 1、支气管哮喘(支气管哮喘)\n[BBOX-60] 治疗意见\n[BBOX-61] 检查\n[BBOX-62] 建议\n[BBOX-63] 接诊医生\n[BBOX-64] 签名时间\n[BBOX-65] 医疗业务专用章\n[BBOX-66] 2\n[BBOX-67] 肺功能测验结果\n[BBOX-68] 新乡市第二人民医院\n[BBOX-69] 呼吸科\n[BBOX-70] 12323\n[BBOX-71] FVC\n[BBOX-72] PRE\n[BBOX-73] FEV1\n[BBOX-74] PRE\n[BBOX-75] FEV1%\n[BBOX-76] PRE\n[BBOX-77] 应诊日期 2025/5/28\n[BBOX-78] 病人号码 W\n[BBOX-79] 姓名\n[BBOX-80] 出生日期 1990/2/5\n[BBOX-81] 人种 中国人\n[BBOX-82] 吸烟 非吸烟者\n[BBOX-83] 患者组\n[BBOX-84] 年龄 35\n[BBOX-85] 性别 男\n[BBOX-86] 高度, cm 170\n[BBOX-87] 重量, kg 85\n[BBOX-88] BMI 29.41\n[BBOX-89] 包-年\n[BBOX-90] 14\n[BBOX-91] 12\n[BBOX-92] 10\n[BBOX-93] 8\n[BBOX-94] 6\n[BBOX-95] 4\n[BBOX-96] 2\n[BBOX-97] 0\n[BBOX-98] -2\n[BBOX-99] -4\n[BBOX-100] 8\n[BBOX-101] 7\n[BBOX-102] 6\n[BBOX-103] 5\n[BBOX-104] 4\n[BBOX-105] 3\n[BBOX-106] 2\n[BBOX-107] 1\n[BBOX-108] 0\n[BBOX-109] 1\n[BBOX-110] 2\n[BBOX-111] 3\n[BBOX-112] 4\n[BBOX-113] 5\n[BBOX-114] 6\n[BBOX-115] 7\n[BBOX-116] 8\n[BBOX-117] 9\n[BBOX-118] 10\n[BBOX-119] 11\n[BBOX-120] 12\n[BBOX-121] 13\n[BBOX-122] 14\n[BBOX-123] 15\n[BBOX-124] 时间(s)\n[BBOX-125] 已预测的\n[BBOX-126] 质量控制等级: D 变化性: FEV1=0.08L (2.26%), FVC=0.31L (5.56%)\n[BBOX-127] 1 Acceptable trials\n[BBOX-128] 评估\n[BBOX-129] 轻度的阻塞\n[BBOX-130] WARNING: FEV1/EVC 前 = 39%\n[BBOX-131] 前/测验日期 2025/5/28 17:51:59\n[BBOX-132] 参数\n[BBOX-133] LLN\n[BBOX-134] 预计\n[BBOX-135] Best\n[BBOX-136] %预计\n[BBOX-137] Z-score\n[BBOX-138] 前 # 1\n[BBOX-139] 前 # 2\n[BBOX-140] 前 # 3\n[BBOX-141] POST\n[BBOX-142] %预计\n[BBOX-143] %激发\n[BBOX-144] FVC\n[BBOX-145] L\n[BBOX-146] 3.47\n[BBOX-147] 4.52\n[BBOX-148] 5.89*\n[BBOX-149] 130\n[BBOX-150] 5.89\n[BBOX-151] 5.58\n[BBOX-152] 5.10\n[BBOX-153] FEV1\n[BBOX-154] L\n[BBOX-155] 2.91\n[BBOX-156] 3.77\n[BBOX-157] 3.62*\n[BBOX-158] 96\n[BBOX-159] 3.62\n[BBOX-160] 3.50\n[BBOX-161] 3.54\n[BBOX-162] FEV1/FVC\n[BBOX-163] %\n[BBOX-164] 73.8\n[BBOX-165] 84.0\n[BBOX-166] 61.5*\n[BBOX-167] 73\n[BBOX-168] 61.5\n[BBOX-169] 62.7\n[BBOX-170] 69.4\n[BBOX-171] PEF\n[BBOX-172] L/s\n[BBOX-173] 5.34\n[BBOX-174] 8.76\n[BBOX-175] 5.08*\n[BBOX-176] 58\n[BBOX-177] 4.54\n[BBOX-178] 4.70\n[BBOX-179] 5.08\n[BBOX-180] ELA\n[BBOX-181] 年\n[BBOX-182] 35\n[BBOX-183] 40\n[BBOX-184] 114\n[BBOX-185] 40\n[BBOX-186] 44\n[BBOX-187] 43\n[BBOX-188] FEF2575\n[BBOX-189] L/s\n[BBOX-190] 2.27\n[BBOX-191] 4.05\n[BBOX-192] 2.37\n[BBOX-193] 58\n[BBOX-194] 2.37\n[BBOX-195] 2.39\n[BBOX-196] 2.68\n[BBOX-197] FET\n[BBOX-198] s\n[BBOX-199] 6.00\n[BBOX-200] 6.73\n[BBOX-201] 112\n[BBOX-202] 6.73\n[BBOX-203] 6.17\n[BBOX-204] 6.33\n[BBOX-205] FIVC\n[BBOX-206] L\n[BBOX-207] 3.47\n[BBOX-208] 4.52\n[BBOX-209] 4.56\n[BBOX-210] 101\n[BBOX-211] 4.56\n[BBOX-212] 4.50\n[BBOX-213] 4.52\n[BBOX-214] IVC\n[BBOX-215] L\n[BBOX-216] 3.47\n[BBOX-217] 4.52\n[BBOX-218] EVC\n[BBOX-219] L\n[BBOX-220] 3.47\n[BBOX-221] 4.52\n[BBOX-222] 9.38\n[BBOX-223] 207\n[BBOX-224] VC\n[BBOX-225] L\n[BBOX-226] 3.47\n[BBOX-227] 4.52\n[BBOX-228] 9.38\n[BBOX-229] 207\n[BBOX-230] FEV1/VC\n[BBOX-231] %\n[BBOX-232] 73.8\n[BBOX-233] 84.0\n[BBOX-234] 38.6\n[BBOX-235] 46\n[BBOX-236] 38.6\n[BBOX-237] 37.3\n[BBOX-238] 37.7\n[BBOX-239] IC\n[BBOX-240] L\n[BBOX-241] 3.03\n[BBOX-242] 4.50\n[BBOX-243] 148\n[BBOX-244] MVV\n[BBOX-245] L/min\n[BBOX-246] 136.2\n[BBOX-247] 99.8\n[BBOX-248] 73\n[BBOX-249] *全部曲线之最佳值 - BTPS 1.073 29 ° C (84.2 ° F) - 已预测的 Knudson\n[BBOX-250] 结论\n[BBOX-251] 支气管舒张试验阳性。\n[BBOX-252] 签名\n[BBOX-253] 所用仪器\n[BBOX-254] Spirolab III S/N 313469\n[BBOX-255] CS 扫描全能王\n[BBOX-256] 3亿人都在用的扫描App\n[BBOX-257] 肺功能检验结果\n[BBOX-258] 新乡市第二人民医院\n[BBOX-259] 呼吸科\n[BBOX-260] 12323\n[BBOX-261] FVC\n[BBOX-262] FEV1\n[BBOX-263] FEV1%\n[BBOX-264] PRE\n[BBOX-265] PRE\n[BBOX-266] PRE\n[BBOX-267] 应诊日期 2025/5/28\n[BBOX-268] 病人号码\n[BBOX-269] 年龄 85\n[BBOX-270] 姓氏\n[BBOX-271] 性别 男\n[BBOX-272] 名字\n[BBOX-273] 高度, cm 170\n[BBOX-274] 出生日期 1990/2/5\n[BBOX-275] 重量, kg 85\n[BBOX-276] 人种 中国人\n[BBOX-277] BMI 29.41\n[BBOX-278] 吸烟 非吸烟者\n[BBOX-279] 患者组 包-年\n[BBOX-280] 14\n[BBOX-281] 12\n[BBOX-282] 10\n[BBOX-283] 8\n[BBOX-284] 6\n[BBOX-285] 4\n[BBOX-286] 2\n[BBOX-287] 0\n[BBOX-288] -2\n[BBOX-289] -4\n[BBOX-290] 8\n[BBOX-291] 7\n[BBOX-292] 6\n[BBOX-293] 5\n[BBOX-294] 4\n[BBOX-295] 3\n[BBOX-296] 2\n[BBOX-297] 1\n[BBOX-298] 0\n[BBOX-299] 1\n[BBOX-300] 2\n[BBOX-301] 3\n[BBOX-302] 4\n[BBOX-303] 5\n[BBOX-304] 6\n[BBOX-305] 7\n[BBOX-306] 8\n[BBOX-307] 9\n[BBOX-308] 10\n[BBOX-309] 11\n[BBOX-310] 12\n[BBOX-311] 13\n[BBOX-312] 14\n[BBOX-313] 15\n[BBOX-314] 时间(s)\n[BBOX-315] @已预测的\n[BBOX-316] 质量控制等级: D 变化性: FEV1=0.06L (2.63%), FVC=0.45L (10.23%)\n[BBOX-317] 1 Acceptable trials\n[BBOX-318] 评估\n[BBOX-319] 中度的阻塞.\n[BBOX-320] WARNING: FEF2575 前 = 39%预测, FEV1/EVC 前 = 45%\n[BBOX-321] 前/测验日期 2025/5/28 17:15:41\n[BBOX-322] 参数 LLN 预计 Best %预计 Z-score 前 #1 前 #2 前 #3 POST %预计 %激发\n[BBOX-323] FVC L 3.47 4.52 4.85* 107 4.85 4.37 4.40 *\n[BBOX-324] FEV1 L 2.91 3.77 2.34* 62 2.13 2.34 2.28 *\n[BBOX-325] FEV1/FVC % 73.8 84.0 48.2* 57 43.9 53.5 51.8 *\n[BBOX-326] PEF L/s 5.34 8.76 2.71* 31 2.71 2.34 2.67 *\n[BBOX-327] ELA 年 35 91 260 91 84 86\n[BBOX-328] FEF2575 L/s 2.27 4.05 1.57 39 1.57 1.80 1.57\n[BBOX-329] FET s 6.00 7.32 122 7.32 5.88 5.68\n[BBOX-330] FIVC L 3.47 4.52 3.86 85 3.86 4.20 4.24\n[BBOX-331] IVC L 3.47 4.52\n[BBOX-332] EVC L 3.47 4.52 5.16 114\n[BBOX-333] VC L 3.47 4.52 5.16 114\n[BBOX-334] FEV1/VC % 73.8 84.0 41.3 49\n[BBOX-335] IC L 3.03 3.58 118\n[BBOX-336] MVV L/min 136.2 42.9 31\n[BBOX-337] *全部曲线之最佳值 - BTPS 1.082 27 °C (80.6 °F) - 已预测的 Knudson\n[BBOX-338] 结论\n[BBOX-339] 签名\n[BBOX-340] 所用仪器\n[BBOX-341] Spirolab III S/N 313469"
  }
]
2026-08-10 13:12:56,506 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:12:56,519 INFO     29 [SmartSplitter] SmartSplitter done: 3 chunks from 3 LLM segments (all bbox_id). Types: {'OutpatientRecord': 1, 'ExaminationReport': 2}
2026-08-10 13:12:56,527 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 13:12:56,527 INFO     29 [Trace] task=2031b7c0 | doc=LYBI-艾特美哮喘(1).pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "342 items", "markdown": "", "text": "", "name": "LYBI-艾特美哮喘(1).pdf", "output_format": "chunks", "chunks": "3 items, types={'OutpatientRecord': 1, 'ExaminationReport': 2}"}
2026-08-10 13:12:56,527 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 13:12:56,528 INFO     29 [ChunkRouter] Routed 3 chunks into 2 groups: {'chunks_Clinical': 1, 'chunks_Examination': 2}
2026-08-10 13:12:56,536 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 13:12:56,536 INFO     29 [Trace] task=2031b7c0 | doc=LYBI-艾特美哮喘(1).pdf | ChunkRouter:Router | outputs={"html": "", "json": "342 items", "markdown": "", "text": "", "name": "LYBI-艾特美哮喘(1).pdf", "output_format": "chunks", "chunks": "3 items, types={'OutpatientRecord': 1, 'ExaminationReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 13:12:56,536 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 13:12:56,541 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:12:56,541 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:12:57,321 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:12:57,328 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 13:12:57,329 INFO     29 [Trace] task=2031b7c0 | doc=LYBI-艾特美哮喘(1).pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "342 items", "markdown": "", "text": "", "name": "LYBI-艾特美哮喘(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 13:12:57,329 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 13:12:57,333 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:12:57,333 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:12:57,732 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:12:57,737 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 13:12:57,737 INFO     29 [Trace] task=2031b7c0 | doc=LYBI-艾特美哮喘(1).pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "342 items", "markdown": "", "text": "", "name": "LYBI-艾特美哮喘(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 13:12:57,737 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 13:12:57,741 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:12:57,742 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:12:57,742 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 13:12:57,742 INFO     29 [qwen-vl-text] positions(66): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:12:57,742 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [66]
2026-08-10 13:12:58,260 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:12:58,261 INFO     29 [qwen-vl-text] LLM extraction start, text_len=384
2026-08-10 13:12:58,261 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:12:58,261 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 65, \"encounter_dates\": [\"2025-05-28\"], \"department\": \"呼吸内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "新乡市第二人民医院\n门（急）诊病历\n门诊号：\n姓名\n性别\n男性\n年龄\n35岁\n婚姻\n已婚\n职业\n工人\n籍贯\n河南省新乡市\n临时住址\n河南省新乡市卫滨区\n永久住址或工作单位\n联系人\n联系人关系\n本人或户主\n联系电话\n就诊类别\n初诊\n是否需下转至基层医疗机构\n否\n建议下转的基层医疗机构/持续性医疗机构\n是否流感样病例\n否\n应检人员类别\n就诊科室\n呼吸内科门诊\n就诊日期\n2025-05-28\n发病日期\n主诉\n发作性咳嗽、咳痰、胸闷、气喘2年\n现病史\n发作性咳嗽、咳痰、胸闷、气喘2年\n既往史\n无高血压史。\n个人史\n无吸烟史。\n婚育史\n已婚\n过敏史\n无\n家族史\n体格检查\nT 36℃, P\n次/分, R\n次/分, BP\n/\nmmHg, BMI\n/\n,\n辅助检查\n无\n疾病诊断\n西医诊断\n1、支气管哮喘(支气管哮喘)\n治疗意见\n检查\n建议\n接诊医生\n签名时间\n医疗业务专用章",
    "role": "user"
  }
]
2026-08-10 13:13:00,968 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:13:00,968 INFO     29 [qwen-vl-text] LLM output (len=205):
{
  "encounter_date": "2025-05-28",
  "chief_complaint": "发作性咳嗽、咳痰、胸闷、气喘2年",
  "present_illness": "发作性咳嗽、咳痰、胸闷、气喘2年",
  "past_history": "无高血压史。",
  "diagnosis": "1、支气管哮喘(支气管哮喘)",
  "treatment_plan": null
}
2026-08-10 13:13:00,968 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-05-28]
2026-08-10 13:13:00,978 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3805108, prompt_len=1195
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共66行）
["新乡市第二人民医院", "门（急）诊病历", "门诊号：", "姓名", "性别", "男性", "年龄", "35岁", "婚姻", "已婚", "职业", "工人", "籍贯", "河南省新乡市", "临时住址", "河南省新乡市卫滨区", "永久住址或工作单位", "联系人", "联系人关系", "本人或户主", "联系电话", "就诊类别", "初诊", "是否需下转至基层医疗机构", "否", "建议下转的基层医疗机构/持续性医疗机构", "是否流感样病例", "否", "应检人员类别", "就诊科室", "呼吸内科门诊", "就诊日期", "2025-05-28", "发病日期", "主诉", "发作性咳嗽、咳痰、胸闷、气喘2年", "现病史", "发作性咳嗽、咳痰、胸闷、气喘2年", "既往史", "无高血压史。", "个人史", "无吸烟史。", "婚育史", "已婚", "过敏史", "无", "家族史", "体格检查", "T 36℃, P", "次/分, R", "次/分, BP", "/", "mmHg, BMI", "/", ",", "辅助检查", "无", "疾病诊断", "西医诊断", "1、支气管哮喘(支气管哮喘)", "治疗意见", "检查", "建议", "接诊医生", "签名时间", "医疗业务专用章"]

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
2026-08-10 13:13:14,317 INFO     29 [qwen-vl-text] coord API raw response (len=2213):
[
	{"text": "新乡市第二人民医院", "bbox": [388, 30, 638, 47]},
	{"text": "门（急）诊病历", "bbox": [420, 49, 605, 65]},
	{"text": "门诊号：", "bbox": [70, 72, 132, 84]},
	{"text": "姓名", "bbox": [90, 93, 127, 105],
	"bbox": [278, 90, 317, 103],
	"bbox": [334, 90, 371, 102],
	"bbox": [385, 90, 422, 102],
	"bbox": [432, 90, 470, 101],
	"bbox": [510, 89, 548, 101],
	"bbox": [562, 89, 599, 101],
	"bbox": [626, 88, 667, 100],
	"bbox": [687, 88, 724, 100],
	"bbox": [787, 87, 825, 99],
	"bbox": [858, 86, 976, 98],
	"bbox": [74, 115, 145, 127],
	"bbox": [160, 113, 327, 126],
	"bbox": [433, 111, 605, 123],
	"bbox": [626, 111, 640, 121],
	"bbox": [80, 135, 134, 147],
	"bbox": [276, 131, 371, 144],
	"bbox": [384, 130, 479, 143],
	"bbox": [519, 130, 596, 142],
	"bbox": [776, 128, 853, 141],
	"bbox": [863, 128, 902, 140],
	"bbox": [106, 151, 327, 166],
	"bbox": [383, 150, 402, 163],
	"bbox": [509, 148, 770, 161],
	"bbox": [509, 165, 624, 178],
	"bbox": [100, 189, 225, 204],
	"bbox": [275, 188, 294, 201],
	"bbox": [437, 186, 551, 199],
	"bbox": [70, 212, 142, 226],
	"bbox": [158, 209, 268, 224],
	"bbox": [330, 208, 407, 222],
	"bbox": [428, 208, 526, 220],
	"bbox": [690, 205, 768, 219],
	"bbox": [86, 234, 123, 247],
	"bbox": [158, 230, 449, 245],
	"bbox": [75, 255, 130, 269],
	"bbox": [158, 251, 449, 267],
	"bbox": [75, 277, 130, 291],
	"bbox": [160, 275, 261, 290],
	"bbox": [75, 300, 130, 314],
	"bbox": [160, 298, 243, 312],
	"bbox": [75, 322, 130, 337],
	"bbox": [158, 321, 194, 335],
	"bbox": [75, 346, 130, 360],
	"bbox": [158, 345, 177, 359],
	"bbox": [559, 343, 618, 357],
	"bbox": [68, 369, 141, 383],
	"bbox": [158, 369, 236, 383],
	"bbox": [273, 368, 351, 383],
	"bbox": [387, 368, 472, 383],
	"bbox": [527, 368, 540, 381],
	"bbox": [595, 368, 684, 380],
	"bbox": [722, 368, 734, 381],
	"bbox": [772, 372, 779, 379],
	"bbox": [68, 392, 141, 406],
	"bbox": [158, 391, 178, 405],
	"bbox": [68, 415, 143, 429],
	"bbox": [160, 414, 234, 428],
	"bbox": [210, 433, 224, 445],
	"bbox": [238, 433, 440, 448],
	"bbox": [72, 455, 147, 468],
	"bbox": [162, 455, 200, 468],
	"bbox": [92, 471, 129, 484],
	"bbox": [75, 491, 148, 504],
	"bbox": [516, 492, 591, 505],
	"bbox": [234, 500, 365, 553],
	"bbox": [297, 535, 321, 551]
]
2026-08-10 13:13:14,318 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-10 13:13:14,321 INFO     29 [qwen-vl-text] coord API: raw_items=70, valid_items=4, elapsed=13.3s
2026-08-10 13:13:14,321 INFO     29 [qwen-vl-text] coord item[0]: text=新乡市第二人民医院, bbox=[388, 30, 638, 47]
2026-08-10 13:13:14,321 INFO     29 [qwen-vl-text] coord item[1]: text=门（急）诊病历, bbox=[420, 49, 605, 65]
2026-08-10 13:13:14,321 INFO     29 [qwen-vl-text] coord item[2]: text=门诊号：, bbox=[70, 72, 132, 84]
2026-08-10 13:13:14,321 INFO     29 [qwen-vl-text] coord item[3]: text=姓名, bbox=[90, 93, 127, 105]
2026-08-10 13:13:14,324 INFO     29 [qwen-vl-text] page=0 — 4/66 coords, api_time=13.3s
2026-08-10 13:13:14,324 INFO     29 [qwen-vl-text] new_positions (66):
[[0, 230.85999999999999, 379.60999999999996, 25.259999999999998, 39.574], [0, 249.89999999999998, 359.97499999999997, 41.257999999999996, 54.73], [0, 41.65, 78.53999999999999, 60.623999999999995, 70.728], [0, 53.55, 75.565, 78.306, 88.41], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
2026-08-10 13:13:14,324 INFO     29 [qwen-vl-text] ═══ DONE ═══ 66 positions, pages=1, time=16.6s
2026-08-10 13:13:14,332 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 13:13:14,332 INFO     29 [Trace] task=2031b7c0 | doc=LYBI-艾特美哮喘(1).pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "342 items", "markdown": "", "text": "", "name": "LYBI-艾特美哮喘(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 13:13:14,332 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 13:13:14,337 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:13:14,337 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:13:15,385 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:13:15,392 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 13:13:15,393 INFO     29 [Trace] task=2031b7c0 | doc=LYBI-艾特美哮喘(1).pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "342 items", "markdown": "", "text": "", "name": "LYBI-艾特美哮喘(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 13:13:15,393 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 13:13:15,398 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:13:15,398 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:13:15,825 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:13:15,830 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 13:13:15,830 INFO     29 [Trace] task=2031b7c0 | doc=LYBI-艾特美哮喘(1).pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "342 items", "markdown": "", "text": "", "name": "LYBI-艾特美哮喘(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 13:13:15,830 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 13:13:15,836 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:13:15,836 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:13:16,287 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:13:16,296 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 13:13:16,296 INFO     29 [Trace] task=2031b7c0 | doc=LYBI-艾特美哮喘(1).pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "342 items", "markdown": "", "text": "", "name": "LYBI-艾特美哮喘(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 13:13:16,296 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 13:13:16,303 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:13:16,304 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:13:16,779 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:13:16,787 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 13:13:16,788 INFO     29 [Trace] task=2031b7c0 | doc=LYBI-艾特美哮喘(1).pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "342 items", "markdown": "", "text": "", "name": "LYBI-艾特美哮喘(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 13:13:16,788 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 13:13:16,793 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:13:16,794 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:13:16,794 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 13:13:16,794 INFO     29 [qwen-vl-text] positions(189): [[0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:13:16,794 INFO     29 [qwen-vl-text] page grouping: [0, 1], lines per page: [1, 188]
2026-08-10 13:13:17,317 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:13:17,539 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:13:17,540 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1010
2026-08-10 13:13:17,540 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:13:17,540 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 66, \"bbox_end\": 254, \"encounter_dates\": [\"2025-05-28\"], \"department\": \"呼吸科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "2\n肺功能测验结果\n新乡市第二人民医院\n呼吸科\n12323\nFVC\nPRE\nFEV1\nPRE\nFEV1%\nPRE\n应诊日期 2025/5/28\n病人号码 W\n姓名\n出生日期 1990/2/5\n人种 中国人\n吸烟 非吸烟者\n患者组\n年龄 35\n性别 男\n高度, cm 170\n重量, kg 85\nBMI 29.41\n包-年\n14\n12\n10\n8\n6\n4\n2\n0\n-2\n-4\n8\n7\n6\n5\n4\n3\n2\n1\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n时间(s)\n已预测的\n质量控制等级: D 变化性: FEV1=0.08L (2.26%), FVC=0.31L (5.56%)\n1 Acceptable trials\n评估\n轻度的阻塞\nWARNING: FEV1/EVC 前 = 39%\n前/测验日期 2025/5/28 17:51:59\n参数\nLLN\n预计\nBest\n%预计\nZ-score\n前 # 1\n前 # 2\n前 # 3\nPOST\n%预计\n%激发\nFVC\nL\n3.47\n4.52\n5.89*\n130\n5.89\n5.58\n5.10\nFEV1\nL\n2.91\n3.77\n3.62*\n96\n3.62\n3.50\n3.54\nFEV1/FVC\n%\n73.8\n84.0\n61.5*\n73\n61.5\n62.7\n69.4\nPEF\nL/s\n5.34\n8.76\n5.08*\n58\n4.54\n4.70\n5.08\nELA\n年\n35\n40\n114\n40\n44\n43\nFEF2575\nL/s\n2.27\n4.05\n2.37\n58\n2.37\n2.39\n2.68\nFET\ns\n6.00\n6.73\n112\n6.73\n6.17\n6.33\nFIVC\nL\n3.47\n4.52\n4.56\n101\n4.56\n4.50\n4.52\nIVC\nL\n3.47\n4.52\nEVC\nL\n3.47\n4.52\n9.38\n207\nVC\nL\n3.47\n4.52\n9.38\n207\nFEV1/VC\n%\n73.8\n84.0\n38.6\n46\n38.6\n37.3\n37.7\nIC\nL\n3.03\n4.50\n148\nMVV\nL/min\n136.2\n99.8\n73\n*全部曲线之最佳值 - BTPS 1.073 29 ° C (84.2 ° F) - 已预测的 Knudson\n结论\n支气管舒张试验阳性。\n签名\n所用仪器\nSpirolab III S/N 313469",
    "role": "user"
  }
]
2026-08-10 13:13:21,794 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:13:21.791+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 41, "failed": 0, "current": {"2031b7c094bd11f1bd9827cf206dfa2d": {"id": "2031b7c094bd11f1bd9827cf206dfa2d", "doc_id": "1ff3926094bd11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LYBI-\u827e\u7279\u7f8e\u54ee\u5598(1).pdf", "type": "pdf", "location": "LYBI-\u827e\u7279\u7f8e\u54ee\u5598(1).pdf", "size": 2220448, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367543508, "task_type": "dataflow", "root_trace_id": "e8588e7f2a8f4f7ea72bfd924542e9bc", "root_traceparent": "00-e8588e7f2a8f4f7ea72bfd924542e9bc-f1b6b538ed925a47-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:13:25,165 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:13:25,165 INFO     29 [qwen-vl-text] LLM output (len=1465):
{
  "exam_date": "2025-05-28",
  "report_date": "2025-05-28",
  "exam_name": "肺功能测验",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "男",
  "department": "呼吸科",
  "bed_number": null,
  "findings": "肺功能测验结果\n新乡市第二人民医院\n呼吸科\n12323\nFVC\nPRE\nFEV1\nPRE\nFEV1%\nPRE\n应诊日期 2025/5/28\n病人号码 W\n姓名\n出生日期 1990/2/5\n人种 中国人\n吸烟 非吸烟者\n患者组\n年龄 35\n性别 男\n高度, cm 170\n重量, kg 85\nBMI 29.41\n包-年\n14\n12\n10\n8\n6\n4\n2\n0\n-2\n-4\n8\n7\n6\n5\n4\n3\n2\n1\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n时间(s)\n已预测的\n质量控制等级: D 变化性: FEV1=0.08L (2.26%), FVC=0.31L (5.56%)\n1 Acceptable trials\n评估\n轻度的阻塞\nWARNING: FEV1/EVC 前 = 39%\n前/测验日期 2025/5/28 17:51:59\n参数\nLLN\n预计\nBest\n%预计\nZ-score\n前 # 1\n前 # 2\n前 # 3\nPOST\n%预计\n%激发\nFVC\nL\n3.47\n4.52\n5.89*\n130\n5.89\n5.58\n5.10\nFEV1\nL\n2.91\n3.77\n3.62*\n96\n3.62\n3.50\n3.54\nFEV1/FVC\n%\n73.8\n84.0\n61.5*\n73\n61.5\n62.7\n69.4\nPEF\nL/s\n5.34\n8.76\n5.08*\n58\n4.54\n4.70\n5.08\nELA\n年\n35\n40\n114\n40\n44\n43\nFEF2575\nL/s\n2.27\n4.05\n2.37\n58\n2.37\n2.39\n2.68\nFET\ns\n6.00\n6.73\n112\n6.73\n6.17\n6.33\nFIVC\nL\n3.47\n4.52\n4.56\n101\n4.56\n4.50\n4.52\nIVC\nL\n3.47\n4.52\nEVC\nL\n3.47\n4.52\n9.38\n207\nVC\nL\n3.47\n4.52\n9.38\n207\nFEV1/VC\n%\n73.8\n84.0\n38.6\n46\n38.6\n37.3\n37.7\nIC\nL\n3.03\n4.50\n148\nMVV\nL/min\n136.2\n99.8\n73\n*全部曲线之最佳值 - BTPS 1.073 29 ° C (84.2 ° F) - 已预测的 Knudson",
  "conclusion": "结论\n支气管舒张试验阳性。",
  "physician": null,
  "reviewer": null
}
2026-08-10 13:13:25,174 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3805108, prompt_len=616
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["2"]

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
2026-08-10 13:13:25,951 INFO     29 [qwen-vl-text] coord API raw response (len=60):
```json
[
	{"text": "2", "bbox": [297, 535, 321, 552]}
]
```
2026-08-10 13:13:25,952 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=0.8s
2026-08-10 13:13:25,952 INFO     29 [qwen-vl-text] coord item[0]: text=2, bbox=[297, 535, 321, 552]
2026-08-10 13:13:25,954 INFO     29 [qwen-vl-text] page=0 — 1/1 coords, api_time=0.8s
2026-08-10 13:13:25,958 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=963170, prompt_len=2186
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共188行）
["肺功能测验结果", "新乡市第二人民医院", "呼吸科", "12323", "FVC", "PRE", "FEV1", "PRE", "FEV1%", "PRE", "应诊日期 2025/5/28", "病人号码 W", "姓名", "出生日期 1990/2/5", "人种 中国人", "吸烟 非吸烟者", "患者组", "年龄 35", "性别 男", "高度, cm 170", "重量, kg 85", "BMI 29.41", "包-年", "14", "12", "10", "8", "6", "4", "2", "0", "-2", "-4", "8", "7", "6", "5", "4", "3", "2", "1", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "时间(s)", "已预测的", "质量控制等级: D 变化性: FEV1=0.08L (2.26%), FVC=0.31L (5.56%)", "1 Acceptable trials", "评估", "轻度的阻塞", "WARNING: FEV1/EVC 前 = 39%", "前/测验日期 2025/5/28 17:51:59", "参数", "LLN", "预计", "Best", "%预计", "Z-score", "前 # 1", "前 # 2", "前 # 3", "POST", "%预计", "%激发", "FVC", "L", "3.47", "4.52", "5.89*", "130", "5.89", "5.58", "5.10", "FEV1", "L", "2.91", "3.77", "3.62*", "96", "3.62", "3.50", "3.54", "FEV1/FVC", "%", "73.8", "84.0", "61.5*", "73", "61.5", "62.7", "69.4", "PEF", "L/s", "5.34", "8.76", "5.08*", "58", "4.54", "4.70", "5.08", "ELA", "年", "35", "40", "114", "40", "44", "43", "FEF2575", "L/s", "2.27", "4.05", "2.37", "58", "2.37", "2.39", "2.68", "FET", "s", "6.00", "6.73", "112", "6.73", "6.17", "6.33", "FIVC", "L", "3.47", "4.52", "4.56", "101", "4.56", "4.50", "4.52", "IVC", "L", "3.47", "4.52", "EVC", "L", "3.47", "4.52", "9.38", "207", "VC", "L", "3.47", "4.52", "9.38", "207", "FEV1/VC", "%", "73.8", "84.0", "38.6", "46", "38.6", "37.3", "37.7", "IC", "L", "3.03", "4.50", "148", "MVV", "L/min", "136.2", "99.8", "73", "*全部曲线之最佳值 - BTPS 1.073 29 ° C (84.2 ° F) - 已预测的 Knudson", "结论", "支气管舒张试验阳性。", "签名", "所用仪器", "Spirolab III S/N 313469"]

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
2026-08-10 13:14:14,282 INFO     29 [qwen-vl-text] coord API raw response (len=9323):
[
	{"text": "肺功能测验结果", "bbox": [29, 16, 151, 30]},
	{"text": "新乡市第二人民医院", "bbox": [30, 45, 185, 58]},
	{"text": "呼吸科", "bbox": [30, 80, 77, 93],
	"bbox": [30, 103, 67, 112]},
	{"text": "FVC", "bbox": [37, 141, 60, 150]},
	{"text": "PRE", "bbox": [39, 152, 57, 160]},
	{"text": "FEV1", "bbox": [195, 141, 222, 150]},
	{"text": "PRE", "bbox": [197, 152, 214, 160]},
	{"text": "FEV1%", "bbox": [344, 141, 379, 150]},
	{"text": "PRE", "bbox": [346, 152, 363, 160]},
	{"text": "应诊日期 2025/5/28", "bbox": [498, 59, 650, 72]},
	{"text": "病人号码 W", "bbox": [498, 80, 577, 93]},
	{"text": "姓名", "bbox": [498, 94, 529, 107]},
	{"text": "出生日期 1990/2/5", "bbox": [498, 123, 557, 135]},
	{"text": "人种 中国人", "bbox": [498, 137, 666, 150]},
	{"text": "吸烟 非吸烟者", "bbox": [498, 151, 681, 164]},
	{"text": "患者组", "bbox": [498, 165, 543, 177]},
	{"text": "年龄 35", "bbox": [771, 80, 809, 93]},
	{"text": "性别 男", "bbox": [771, 94, 888, 107]},
	{"text": "高度, cm 170", "bbox": [771, 108, 888, 121]},
	{"text": "重量, kg 85", "bbox": [771, 122, 888, 135]},
	{"text": "BMI 29.41", "bbox": [771, 136, 905, 150]},
	{"text": "包-年", "bbox": [771, 151, 809, 164]},
	{"text": "14", "bbox": [43, 193, 62, 203]},
	{"text": "12", "bbox": [43, 215, 62, 225]},
	{"text": "10", "bbox": [43, 238, 62, 248]},
	{"text": "8", "bbox": [51, 260, 62, 270]},
	{"text": "6", "bbox": [51, 283, 62, 293]},
	{"text": "4", "bbox": [51, 306, 62, 316]},
	{"text": "2", "bbox": [51, 328, 62, 338]},
	{"text": "0", "bbox": [51, 351, 62, 361]},
	{"text": "-2", "bbox": [45, 373, 62, 383]},
	{"text": "-4", "bbox": [45, 396, 62, 406]},
	{"text": "-6", "bbox": [45, 418, 62, 428]},
	{"text": "-8", "bbox": [45, 441, 62, 451]},
	{"text": "-10", "bbox": [39, 463, 62, 473]},
	{"text": "8", "bbox": [367, 193, 376, 203]},
	{"text": "7", "bbox": [367, 215, 376, 225]},
	{"text": "6", "bbox": [367, 238, 376, 248]},
	{"text": "5", "bbox": [367, 260, 376, 270]},
	{"text": "4", "bbox": [367, 283, 376, 293]},
	{"text": "3", "bbox": [367, 306, 376, 316]},
	{"text": "2", "bbox": [367, 328, 376, 338]},
	{"text": "1", "bbox": [367, 351, 376, 361]},
	{"text": "0", "bbox": [367, 373, 376, 383]},
	{"text": "1", "bbox": [413, 396, 421, 406]},
	{"text": "2", "bbox": [448, 396, 457, 406]},
	{"text": "3", "bbox": [486, 396, 495, 406]},
	{"text": "4", "bbox": [522, 396, 531, 406]},
	{"text": "5", "bbox": [558, 396, 567, 406]},
	{"text": "6", "bbox": [594, 396, 603, 406]},
	{"text": "7", "bbox": [630, 396, 639, 406]},
	{"text": "8", "bbox": [666, 396, 675, 406]},
	{"text": "9", "bbox": [702, 396, 711, 406]},
	{"text": "10", "bbox": [737, 396, 753, 406]},
	{"text": "11", "bbox": [773, 396, 788, 406]},
	{"text": "12", "bbox": [809, 396, 825, 406]},
	{"text": "13", "bbox": [845, 396, 864, 406]},
	{"text": "14", "bbox": [881, 396, 899, 406]},
	{"text": "15", "bbox": [918, 396, 940, 406]},
	{"text": "时间(s)", "bbox": [629, 402, 679, 414]},
	{"text": "已预测的", "bbox": [787, 370, 856, 381]},
	{"text": "质量控制等级: D 变化性: FEV1=0.08L (2.26%), FVC=0.31L (5.56%)", "bbox": [373, 418, 854, 431]},
	{"text": "1 Acceptable trials", "bbox": [373, 435, 518, 447]},
	{"text": "评估", "bbox": [373, 456, 408, 469]},
	{"text": "轻度的阻塞", "bbox": [373, 473, 442, 483]},
	{"text": "WARNING: FEV1/EVC 前 = 39%", "bbox": [373, 484, 551, 494]},
	{"text": "前/测验日期 2025/5/28 17:51:59", "bbox": [26, 519, 302, 531]},
	{"text": "参数", "bbox": [53, 540, 82, 551]},
	{"text": "LLN", "bbox": [214, 540, 236, 551]},
	{"text": "预计", "bbox": [276, 540, 303, 551]},
	{"text": "Best", "bbox": [348, 540, 375, 551]},
	{"text": "%预计", "bbox": [411, 540, 445, 551]},
	{"text": "Z-score", "bbox": [473, 540, 522, 551]},
	{"text": "前 # 1", "bbox": [543, 540, 581, 551]},
	{"text": "前 # 2", "bbox": [607, 540, 648, 551]},
	{"text": "前 # 3", "bbox": [671, 540, 711, 551]},
	{"text": "POST", "bbox": [744, 540, 772, 551]},
	{"text": "%预计", "bbox": [813, 540, 848, 551]},
	{"text": "%激发", "bbox": [873, 540, 907, 551]},
	{"text": "FVC", "bbox": [53, 558, 80, 569]},
	{"text": "L", "bbox": [140, 558, 148, 569]},
	{"text": "3.47", "bbox": [211, 558, 241, 569]},
	{"text": "4.52", "bbox": [280, 558, 311, 569]},
	{"text": "5.89*", "bbox": [345, 558, 385, 569]},
	{"text": "130", "bbox": [422, 558, 448, 569]},
	{"text": "5.89", "bbox": [552, 558, 581, 569]},
	{"text": "5.58", "bbox": [612, 558, 642, 569]},
	{"text": "5.10", "bbox": [675, 558, 705, 569]},
	{"text": "FEV1", "bbox": [53, 572, 87, 583]},
	{"text": "L", "bbox": [140, 572, 148, 583]},
	{"text": "2.91", "bbox": [211, 572, 241, 583]},
	{"text": "3.77", "bbox": [280, 572, 311, 583]},
	{"text": "3.62*", "bbox": [345, 572, 385, 583]},
	{"text": "96", "bbox": [428, 572, 448, 583]},
	{"text": "3.62", "bbox": [552, 572, 581, 583]},
	{"text": "3.50", "bbox": [612, 572, 642, 583]},
	{"text": "3.54", "bbox": [675, 572, 705, 583]},
	{"text": "FEV1/FVC", "bbox": [53, 586, 120, 597]},
	{"text": "%", "bbox": [140, 586, 154, 597]},
	{"text": "73.8", "bbox": [211, 586, 241, 597]},
	{"text": "84.0", "bbox": [280, 586, 311, 597]},
	{"text": "61.5*", "bbox": [345, 586, 385, 597]},
	{"text": "73", "bbox": [428, 586, 448, 597]},
	{"text": "61.5", "bbox": [552, 586, 581, 597]},
	{"text": "62.7", "bbox": [608, 586, 642, 597]},
	{"text": "69.4", "bbox": [672, 586, 705, 597]},
	{"text": "PEF", "bbox": [53, 600, 79, 611]},
	{"text": "L/s", "bbox": [140, 600, 158, 611]},
	{"text": "5.34", "bbox": [211, 600, 241, 611]},
	{"text": "8.76", "bbox": [280, 600, 311, 611]},
	{"text": "5.08*", "bbox": [345, 600, 385, 611]},
	{"text": "58", "bbox": [428, 600, 448, 611]},
	{"text": "4.54", "bbox": [552, 600, 581, 611]},
	{"text": "4.70", "bbox": [608, 600, 642, 611]},
	{"text": "5.08", "bbox": [672, 600, 705, 611]},
	{"text": "ELA", "bbox": [53, 614, 79, 625]},
	{"text": "年", "bbox": [140, 614, 154, 625]},
	{"text": "35", "bbox": [293, 614, 311, 625]},
	{"text": "40", "bbox": [357, 614, 375, 625]},
	{"text": "114", "bbox": [422, 614, 448, 625]},
	{"text": "40", "bbox": [564, 614, 581, 625]},
	{"text": "44", "bbox": [624, 614, 642, 625]},
	{"text": "43", "bbox": [690, 614, 705, 625]},
	{"text": "FEF2575", "bbox": [53, 628, 110, 639]},
	{"text": "L/s", "bbox": [140, 628, 158, 639]},
	{"text": "2.27", "bbox": [211, 628, 241, 639]},
	{"text": "4.05", "bbox": [280, 628, 311, 639]},
	{"text": "2.37", "bbox": [345, 628, 375, 639]},
	{"text": "58", "bbox": [428, 628, 448, 639]},
	{"text": "2.37", "bbox": [552, 628, 581, 639]},
	{"text": "2.39", "bbox": [612, 628, 642, 639]},
	{"text": "2.68", "bbox": [675, 628, 705, 639]},
	{"text": "FET", "bbox": [53, 642, 79, 653]},
	{"text": "s", "bbox": [140, 642, 148, 653]},
	{"text": "6.00", "bbox": [280, 642, 311, 653]},
	{"text": "6.73", "bbox": [345, 642, 375, 653]},
	{"text": "112", "bbox": [422, 642, 448, 653]},
	{"text": "6.73", "bbox": [552, 642, 581, 653]},
	{"text": "6.17", "bbox": [612, 642, 642, 653]},
	{"text": "6.33", "bbox": [675, 642, 705, 653]},
	{"text": "FIVC", "bbox": [53, 656, 87, 667]},
	{"text": "L", "bbox": [140, 656, 148, 667]},
	{"text": "3.47", "bbox": [211, 656, 241, 667]},
	{"text": "4.52", "bbox": [280, 656, 311, 667]},
	{"text": "4.56", "bbox": [345, 656, 375, 667]},
	{"text": "101", "bbox": [422, 656, 448, 667]},
	{"text": "4.56", "bbox": [552, 656, 581, 667]},
	{"text": "4.50", "bbox": [612, 656, 642, 667]},
	{"text": "4.52", "bbox": [675, 656, 705, 667]},
	{"text": "IVC", "bbox": [53, 670, 79, 681]},
	{"text": "L", "bbox": [140, 670, 148, 681]},
	{"text": "3.47", "bbox": [211, 670, 241, 681]},
	{"text": "4.52", "bbox": [280, 670, 311, 681]},
	{"text": "EVC", "bbox": [53, 684, 80, 695]},
	{"text": "L", "bbox": [140, 684, 148, 695]},
	{"text": "3.47", "bbox": [211, 684, 241, 695]},
	{"text": "4.52", "bbox": [280, 684, 311, 695]},
	{"text": "9.38", "bbox": [345, 684, 375, 695]},
	{"text": "207", "bbox": [422, 684, 448, 695]},
	{"text": "VC", "bbox": [53, 698, 74, 709]},
	{"text": "L", "bbox": [140, 698, 148, 709]},
	{"text": "3.47", "bbox": [211, 698, 241, 709]},
	{"text": "4.52", "bbox": [280, 698, 311, 709]},
	{"text": "9.38", "bbox": [345, 698, 375, 709]},
	{"text": "207", "bbox": [422, 698, 448, 709]},
	{"text": "FEV1/VC", "bbox": [53, 712, 113, 723]},
	{"text": "%", "bbox": [140, 712, 154, 723]},
	{"text": "73.8", "bbox": [211, 712, 241, 723]},
	{"text": "84.0", "bbox": [280, 712, 311, 723]},
	{"text": "38.6", "bbox": [345, 712, 375, 723]},
	{"text": "46", "bbox": [428, 712, 448, 723]},
	{"text": "38.6", "bbox": [552, 712, 581, 723]},
	{"text": "37.3", "bbox": [608, 712, 642, 723]},
	{"text": "37.7", "bbox": [672, 712, 705, 723]},
	{"text": "IC", "bbox": [53, 726, 69, 737]},
	{"text": "L", "bbox": [140, 726, 148, 737]},
	{"text": "3.03", "bbox": [280, 726, 311, 737]},
	{"text": "4.50", "bbox": [345, 726, 375, 737]},
	{"text": "148", "bbox": [422, 726, 448, 737]},
	{"text": "MVV", "bbox": [53, 739, 84, 750]},
	{"text": "L/min", "bbox": [140, 739, 170, 750]},
	{"text": "136.2", "bbox": [274, 739, 311, 750]},
	{"text": "99.8", "bbox": [345, 739, 375, 750]},
	{"text": "73", "bbox": [428, 739, 448, 750]},
	{"text": "*全部曲线之最佳值 - BTPS 1.073 29 ° C (84.2 ° F) - 已预测的 Knudson", "bbox": [53, 753, 540, 764]},
	{"text": "结论", "bbox": [25, 774, 60, 787]},
	{"text": "支气管舒张试验阳性。", "bbox": [85, 788, 441, 822]},
	{"text": "签名", "bbox": [25, 843, 147, 867]},
	{"text": "所用仪器", "bbox": [884, 848, 940, 860]},
	{"text": "Spirolab III S/N 313469", "bbox": [778, 863, 940, 873]}
]
2026-08-10 13:14:14,283 INFO     29 [qwen-vl-text] coord API: raw_items=190, valid_items=190, elapsed=48.3s
2026-08-10 13:14:14,283 INFO     29 [qwen-vl-text] coord item[0]: text=肺功能测验结果, bbox=[29, 16, 151, 30]
2026-08-10 13:14:14,283 INFO     29 [qwen-vl-text] coord item[1]: text=新乡市第二人民医院, bbox=[30, 45, 185, 58]
2026-08-10 13:14:14,283 INFO     29 [qwen-vl-text] coord item[2]: text=呼吸科, bbox=[30, 103, 67, 112]
2026-08-10 13:14:14,283 INFO     29 [qwen-vl-text] coord item[3]: text=FVC, bbox=[37, 141, 60, 150]
2026-08-10 13:14:14,283 INFO     29 [qwen-vl-text] coord item[4]: text=PRE, bbox=[39, 152, 57, 160]
2026-08-10 13:14:14,283 INFO     29 [qwen-vl-text] coord item[5]: text=FEV1, bbox=[195, 141, 222, 150]
2026-08-10 13:14:14,283 INFO     29 [qwen-vl-text] coord item[6]: text=PRE, bbox=[197, 152, 214, 160]
2026-08-10 13:14:14,283 INFO     29 [qwen-vl-text] coord item[7]: text=FEV1%, bbox=[344, 141, 379, 150]
2026-08-10 13:14:14,283 INFO     29 [qwen-vl-text] coord item[8]: text=PRE, bbox=[346, 152, 363, 160]
2026-08-10 13:14:14,283 INFO     29 [qwen-vl-text] coord item[9]: text=应诊日期 2025/5/28, bbox=[498, 59, 650, 72]
2026-08-10 13:14:14,283 INFO     29 [qwen-vl-text] coord item[10]: text=病人号码 W, bbox=[498, 80, 577, 93]
2026-08-10 13:14:14,283 INFO     29 [qwen-vl-text] coord item[11]: text=姓名, bbox=[498, 94, 529, 107]
2026-08-10 13:14:14,283 INFO     29 [qwen-vl-text] coord item[12]: text=出生日期 1990/2/5, bbox=[498, 123, 557, 135]
2026-08-10 13:14:14,283 INFO     29 [qwen-vl-text] coord item[13]: text=人种 中国人, bbox=[498, 137, 666, 150]
2026-08-10 13:14:14,283 INFO     29 [qwen-vl-text] coord item[14]: text=吸烟 非吸烟者, bbox=[498, 151, 681, 164]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[15]: text=患者组, bbox=[498, 165, 543, 177]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[16]: text=年龄 35, bbox=[771, 80, 809, 93]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[17]: text=性别 男, bbox=[771, 94, 888, 107]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[18]: text=高度, cm 170, bbox=[771, 108, 888, 121]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[19]: text=重量, kg 85, bbox=[771, 122, 888, 135]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[20]: text=BMI 29.41, bbox=[771, 136, 905, 150]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[21]: text=包-年, bbox=[771, 151, 809, 164]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[22]: text=14, bbox=[43, 193, 62, 203]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[23]: text=12, bbox=[43, 215, 62, 225]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[24]: text=10, bbox=[43, 238, 62, 248]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[25]: text=8, bbox=[51, 260, 62, 270]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[26]: text=6, bbox=[51, 283, 62, 293]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[27]: text=4, bbox=[51, 306, 62, 316]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[28]: text=2, bbox=[51, 328, 62, 338]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[29]: text=0, bbox=[51, 351, 62, 361]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[30]: text=-2, bbox=[45, 373, 62, 383]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[31]: text=-4, bbox=[45, 396, 62, 406]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[32]: text=-6, bbox=[45, 418, 62, 428]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[33]: text=-8, bbox=[45, 441, 62, 451]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[34]: text=-10, bbox=[39, 463, 62, 473]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[35]: text=8, bbox=[367, 193, 376, 203]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[36]: text=7, bbox=[367, 215, 376, 225]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[37]: text=6, bbox=[367, 238, 376, 248]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[38]: text=5, bbox=[367, 260, 376, 270]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[39]: text=4, bbox=[367, 283, 376, 293]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[40]: text=3, bbox=[367, 306, 376, 316]
2026-08-10 13:14:14,284 INFO     29 [qwen-vl-text] coord item[41]: text=2, bbox=[367, 328, 376, 338]
2026-08-10 13:14:14,285 INFO     29 [qwen-vl-text] coord item[42]: text=1, bbox=[367, 351, 376, 361]
2026-08-10 13:14:14,285 INFO     29 [qwen-vl-text] coord item[43]: text=0, bbox=[367, 373, 376, 383]
2026-08-10 13:14:14,285 INFO     29 [qwen-vl-text] coord item[44]: text=1, bbox=[413, 396, 421, 406]
2026-08-10 13:14:14,285 INFO     29 [qwen-vl-text] coord item[45]: text=2, bbox=[448, 396, 457, 406]
2026-08-10 13:14:14,285 INFO     29 [qwen-vl-text] coord item[46]: text=3, bbox=[486, 396, 495, 406]
2026-08-10 13:14:14,285 INFO     29 [qwen-vl-text] coord item[47]: text=4, bbox=[522, 396, 531, 406]
2026-08-10 13:14:14,285 INFO     29 [qwen-vl-text] coord item[48]: text=5, bbox=[558, 396, 567, 406]
2026-08-10 13:14:14,285 INFO     29 [qwen-vl-text] coord item[49]: text=6, bbox=[594, 396, 603, 406]
2026-08-10 13:14:14,285 INFO     29 [qwen-vl-text] coord item[50]: text=7, bbox=[630, 396, 639, 406]
2026-08-10 13:14:14,285 INFO     29 [qwen-vl-text] coord item[51]: text=8, bbox=[666, 396, 675, 406]
2026-08-10 13:14:14,285 INFO     29 [qwen-vl-text] coord item[52]: text=9, bbox=[702, 396, 711, 406]
2026-08-10 13:14:14,285 INFO     29 [qwen-vl-text] coord item[53]: text=10, bbox=[737, 396, 753, 406]
2026-08-10 13:14:14,285 INFO     29 [qwen-vl-text] coord item[54]: text=11, bbox=[773, 396, 788, 406]
2026-08-10 13:14:14,285 INFO     29 [qwen-vl-text] coord item[55]: text=12, bbox=[809, 396, 825, 406]
2026-08-10 13:14:14,285 INFO     29 [qwen-vl-text] coord item[56]: text=13, bbox=[845, 396, 864, 406]
2026-08-10 13:14:14,285 INFO     29 [qwen-vl-text] coord item[57]: text=14, bbox=[881, 396, 899, 406]
2026-08-10 13:14:14,285 INFO     29 [qwen-vl-text] coord item[58]: text=15, bbox=[918, 396, 940, 406]
2026-08-10 13:14:14,285 INFO     29 [qwen-vl-text] coord item[59]: text=时间(s), bbox=[629, 402, 679, 414]
2026-08-10 13:14:14,285 INFO     29 [qwen-vl-text] coord item[60]: text=已预测的, bbox=[787, 370, 856, 381]
2026-08-10 13:14:14,286 INFO     29 [qwen-vl-text] coord item[61]: text=质量控制等级: D 变化性: FEV1=0.08L (2.26%), FVC=0.31L (5.56%), bbox=[373, 418, 854, 431]
2026-08-10 13:14:14,286 INFO     29 [qwen-vl-text] coord item[62]: text=1 Acceptable trials, bbox=[373, 435, 518, 447]
2026-08-10 13:14:14,286 INFO     29 [qwen-vl-text] coord item[63]: text=评估, bbox=[373, 456, 408, 469]
2026-08-10 13:14:14,286 INFO     29 [qwen-vl-text] coord item[64]: text=轻度的阻塞, bbox=[373, 473, 442, 483]
2026-08-10 13:14:14,286 INFO     29 [qwen-vl-text] coord item[65]: text=WARNING: FEV1/EVC 前 = 39%, bbox=[373, 484, 551, 494]
2026-08-10 13:14:14,286 INFO     29 [qwen-vl-text] coord item[66]: text=前/测验日期 2025/5/28 17:51:59, bbox=[26, 519, 302, 531]
2026-08-10 13:14:14,286 INFO     29 [qwen-vl-text] coord item[67]: text=参数, bbox=[53, 540, 82, 551]
2026-08-10 13:14:14,286 INFO     29 [qwen-vl-text] coord item[68]: text=LLN, bbox=[214, 540, 236, 551]
2026-08-10 13:14:14,286 INFO     29 [qwen-vl-text] coord item[69]: text=预计, bbox=[276, 540, 303, 551]
2026-08-10 13:14:14,286 INFO     29 [qwen-vl-text] coord item[70]: text=Best, bbox=[348, 540, 375, 551]
2026-08-10 13:14:14,286 INFO     29 [qwen-vl-text] coord item[71]: text=%预计, bbox=[411, 540, 445, 551]
2026-08-10 13:14:14,286 INFO     29 [qwen-vl-text] coord item[72]: text=Z-score, bbox=[473, 540, 522, 551]
2026-08-10 13:14:14,286 INFO     29 [qwen-vl-text] coord item[73]: text=前 # 1, bbox=[543, 540, 581, 551]
2026-08-10 13:14:14,286 INFO     29 [qwen-vl-text] coord item[74]: text=前 # 2, bbox=[607, 540, 648, 551]
2026-08-10 13:14:14,286 INFO     29 [qwen-vl-text] coord item[75]: text=前 # 3, bbox=[671, 540, 711, 551]
2026-08-10 13:14:14,286 INFO     29 [qwen-vl-text] coord item[76]: text=POST, bbox=[744, 540, 772, 551]
2026-08-10 13:14:14,286 INFO     29 [qwen-vl-text] coord item[77]: text=%预计, bbox=[813, 540, 848, 551]
2026-08-10 13:14:14,286 INFO     29 [qwen-vl-text] coord item[78]: text=%激发, bbox=[873, 540, 907, 551]
2026-08-10 13:14:14,287 INFO     29 [qwen-vl-text] coord item[79]: text=FVC, bbox=[53, 558, 80, 569]
2026-08-10 13:14:14,287 INFO     29 [qwen-vl-text] coord item[80]: text=L, bbox=[140, 558, 148, 569]
2026-08-10 13:14:14,287 INFO     29 [qwen-vl-text] coord item[81]: text=3.47, bbox=[211, 558, 241, 569]
2026-08-10 13:14:14,287 INFO     29 [qwen-vl-text] coord item[82]: text=4.52, bbox=[280, 558, 311, 569]
2026-08-10 13:14:14,287 INFO     29 [qwen-vl-text] coord item[83]: text=5.89*, bbox=[345, 558, 385, 569]
2026-08-10 13:14:14,287 INFO     29 [qwen-vl-text] coord item[84]: text=130, bbox=[422, 558, 448, 569]
2026-08-10 13:14:14,287 INFO     29 [qwen-vl-text] coord item[85]: text=5.89, bbox=[552, 558, 581, 569]
2026-08-10 13:14:14,287 INFO     29 [qwen-vl-text] coord item[86]: text=5.58, bbox=[612, 558, 642, 569]
2026-08-10 13:14:14,287 INFO     29 [qwen-vl-text] coord item[87]: text=5.10, bbox=[675, 558, 705, 569]
2026-08-10 13:14:14,287 INFO     29 [qwen-vl-text] coord item[88]: text=FEV1, bbox=[53, 572, 87, 583]
2026-08-10 13:14:14,287 INFO     29 [qwen-vl-text] coord item[89]: text=L, bbox=[140, 572, 148, 583]
2026-08-10 13:14:14,287 INFO     29 [qwen-vl-text] coord item[90]: text=2.91, bbox=[211, 572, 241, 583]
2026-08-10 13:14:14,287 INFO     29 [qwen-vl-text] coord item[91]: text=3.77, bbox=[280, 572, 311, 583]
2026-08-10 13:14:14,287 INFO     29 [qwen-vl-text] coord item[92]: text=3.62*, bbox=[345, 572, 385, 583]
2026-08-10 13:14:14,287 INFO     29 [qwen-vl-text] coord item[93]: text=96, bbox=[428, 572, 448, 583]
2026-08-10 13:14:14,287 INFO     29 [qwen-vl-text] coord item[94]: text=3.62, bbox=[552, 572, 581, 583]
2026-08-10 13:14:14,287 INFO     29 [qwen-vl-text] coord item[95]: text=3.50, bbox=[612, 572, 642, 583]
2026-08-10 13:14:14,287 INFO     29 [qwen-vl-text] coord item[96]: text=3.54, bbox=[675, 572, 705, 583]
2026-08-10 13:14:14,287 INFO     29 [qwen-vl-text] coord item[97]: text=FEV1/FVC, bbox=[53, 586, 120, 597]
2026-08-10 13:14:14,287 INFO     29 [qwen-vl-text] coord item[98]: text=%, bbox=[140, 586, 154, 597]
2026-08-10 13:14:14,287 INFO     29 [qwen-vl-text] coord item[99]: text=73.8, bbox=[211, 586, 241, 597]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[100]: text=84.0, bbox=[280, 586, 311, 597]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[101]: text=61.5*, bbox=[345, 586, 385, 597]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[102]: text=73, bbox=[428, 586, 448, 597]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[103]: text=61.5, bbox=[552, 586, 581, 597]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[104]: text=62.7, bbox=[608, 586, 642, 597]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[105]: text=69.4, bbox=[672, 586, 705, 597]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[106]: text=PEF, bbox=[53, 600, 79, 611]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[107]: text=L/s, bbox=[140, 600, 158, 611]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[108]: text=5.34, bbox=[211, 600, 241, 611]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[109]: text=8.76, bbox=[280, 600, 311, 611]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[110]: text=5.08*, bbox=[345, 600, 385, 611]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[111]: text=58, bbox=[428, 600, 448, 611]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[112]: text=4.54, bbox=[552, 600, 581, 611]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[113]: text=4.70, bbox=[608, 600, 642, 611]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[114]: text=5.08, bbox=[672, 600, 705, 611]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[115]: text=ELA, bbox=[53, 614, 79, 625]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[116]: text=年, bbox=[140, 614, 154, 625]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[117]: text=35, bbox=[293, 614, 311, 625]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[118]: text=40, bbox=[357, 614, 375, 625]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[119]: text=114, bbox=[422, 614, 448, 625]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[120]: text=40, bbox=[564, 614, 581, 625]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[121]: text=44, bbox=[624, 614, 642, 625]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[122]: text=43, bbox=[690, 614, 705, 625]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[123]: text=FEF2575, bbox=[53, 628, 110, 639]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[124]: text=L/s, bbox=[140, 628, 158, 639]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[125]: text=2.27, bbox=[211, 628, 241, 639]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[126]: text=4.05, bbox=[280, 628, 311, 639]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[127]: text=2.37, bbox=[345, 628, 375, 639]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[128]: text=58, bbox=[428, 628, 448, 639]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[129]: text=2.37, bbox=[552, 628, 581, 639]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[130]: text=2.39, bbox=[612, 628, 642, 639]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[131]: text=2.68, bbox=[675, 628, 705, 639]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[132]: text=FET, bbox=[53, 642, 79, 653]
2026-08-10 13:14:14,288 INFO     29 [qwen-vl-text] coord item[133]: text=s, bbox=[140, 642, 148, 653]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[134]: text=6.00, bbox=[280, 642, 311, 653]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[135]: text=6.73, bbox=[345, 642, 375, 653]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[136]: text=112, bbox=[422, 642, 448, 653]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[137]: text=6.73, bbox=[552, 642, 581, 653]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[138]: text=6.17, bbox=[612, 642, 642, 653]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[139]: text=6.33, bbox=[675, 642, 705, 653]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[140]: text=FIVC, bbox=[53, 656, 87, 667]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[141]: text=L, bbox=[140, 656, 148, 667]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[142]: text=3.47, bbox=[211, 656, 241, 667]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[143]: text=4.52, bbox=[280, 656, 311, 667]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[144]: text=4.56, bbox=[345, 656, 375, 667]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[145]: text=101, bbox=[422, 656, 448, 667]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[146]: text=4.56, bbox=[552, 656, 581, 667]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[147]: text=4.50, bbox=[612, 656, 642, 667]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[148]: text=4.52, bbox=[675, 656, 705, 667]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[149]: text=IVC, bbox=[53, 670, 79, 681]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[150]: text=L, bbox=[140, 670, 148, 681]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[151]: text=3.47, bbox=[211, 670, 241, 681]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[152]: text=4.52, bbox=[280, 670, 311, 681]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[153]: text=EVC, bbox=[53, 684, 80, 695]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[154]: text=L, bbox=[140, 684, 148, 695]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[155]: text=3.47, bbox=[211, 684, 241, 695]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[156]: text=4.52, bbox=[280, 684, 311, 695]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[157]: text=9.38, bbox=[345, 684, 375, 695]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[158]: text=207, bbox=[422, 684, 448, 695]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[159]: text=VC, bbox=[53, 698, 74, 709]
2026-08-10 13:14:14,289 INFO     29 [qwen-vl-text] coord item[160]: text=L, bbox=[140, 698, 148, 709]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[161]: text=3.47, bbox=[211, 698, 241, 709]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[162]: text=4.52, bbox=[280, 698, 311, 709]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[163]: text=9.38, bbox=[345, 698, 375, 709]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[164]: text=207, bbox=[422, 698, 448, 709]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[165]: text=FEV1/VC, bbox=[53, 712, 113, 723]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[166]: text=%, bbox=[140, 712, 154, 723]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[167]: text=73.8, bbox=[211, 712, 241, 723]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[168]: text=84.0, bbox=[280, 712, 311, 723]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[169]: text=38.6, bbox=[345, 712, 375, 723]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[170]: text=46, bbox=[428, 712, 448, 723]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[171]: text=38.6, bbox=[552, 712, 581, 723]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[172]: text=37.3, bbox=[608, 712, 642, 723]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[173]: text=37.7, bbox=[672, 712, 705, 723]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[174]: text=IC, bbox=[53, 726, 69, 737]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[175]: text=L, bbox=[140, 726, 148, 737]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[176]: text=3.03, bbox=[280, 726, 311, 737]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[177]: text=4.50, bbox=[345, 726, 375, 737]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[178]: text=148, bbox=[422, 726, 448, 737]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[179]: text=MVV, bbox=[53, 739, 84, 750]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[180]: text=L/min, bbox=[140, 739, 170, 750]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[181]: text=136.2, bbox=[274, 739, 311, 750]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[182]: text=99.8, bbox=[345, 739, 375, 750]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[183]: text=73, bbox=[428, 739, 448, 750]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[184]: text=*全部曲线之最佳值 - BTPS 1.073 29 ° C (84.2 ° F) - 已预测的 Knudson, bbox=[53, 753, 540, 764]
2026-08-10 13:14:14,290 INFO     29 [qwen-vl-text] coord item[185]: text=结论, bbox=[25, 774, 60, 787]
2026-08-10 13:14:14,291 INFO     29 [qwen-vl-text] coord item[186]: text=支气管舒张试验阳性。, bbox=[85, 788, 441, 822]
2026-08-10 13:14:14,291 INFO     29 [qwen-vl-text] coord item[187]: text=签名, bbox=[25, 843, 147, 867]
2026-08-10 13:14:14,291 INFO     29 [qwen-vl-text] coord item[188]: text=所用仪器, bbox=[884, 848, 940, 860]
2026-08-10 13:14:14,291 INFO     29 [qwen-vl-text] coord item[189]: text=Spirolab III S/N 313469, bbox=[778, 863, 940, 873]
2026-08-10 13:14:14,291 INFO     29 [qwen-vl-text] page=1 — 188/188 coords, api_time=48.3s
2026-08-10 13:14:14,291 INFO     29 [qwen-vl-text] new_positions (189):
[[0, 176.715, 190.995, 450.46999999999997, 464.784], [1, 17.255, 89.845, 13.472, 25.259999999999998], [1, 17.849999999999998, 110.07499999999999, 37.89, 48.836], [1, 17.849999999999998, 39.864999999999995, 86.726, 94.304], [1, 22.015, 35.699999999999996, 118.722, 126.3], [1, 23.205, 33.915, 127.984, 134.72], [1, 116.02499999999999, 132.09, 118.722, 126.3], [1, 117.21499999999999, 127.33, 127.984, 134.72], [1, 204.67999999999998, 225.505, 118.722, 126.3], [1, 205.87, 215.98499999999999, 127.984, 134.72], [1, 296.31, 386.75, 49.678, 60.623999999999995], [1, 296.31, 343.315, 67.36, 78.306], [1, 296.31, 314.755, 79.148, 90.094], [1, 296.31, 331.41499999999996, 103.566, 113.67], [1, 296.31, 396.27, 115.354, 126.3], [1, 296.31, 405.195, 127.142, 138.088], [1, 296.31, 323.085, 138.93, 149.034], [1, 458.745, 481.35499999999996, 67.36, 78.306], [1, 458.745, 528.36, 79.148, 90.094], [1, 458.745, 528.36, 90.93599999999999, 101.88199999999999], [1, 458.745, 528.36, 102.72399999999999, 113.67], [1, 458.745, 538.475, 114.512, 126.3], [1, 458.745, 481.35499999999996, 127.142, 138.088], [1, 25.584999999999997, 36.89, 162.506, 170.926], [1, 25.584999999999997, 36.89, 181.03, 189.45], [1, 25.584999999999997, 36.89, 200.396, 208.816], [1, 30.345, 36.89, 218.92, 227.34], [1, 30.345, 36.89, 238.286, 246.706], [1, 30.345, 36.89, 257.652, 266.072], [1, 30.345, 36.89, 276.176, 284.596], [1, 30.345, 36.89, 295.542, 303.962], [1, 26.775, 36.89, 314.066, 322.486], [1, 26.775, 36.89, 333.432, 341.852], [1, 26.775, 36.89, 351.95599999999996, 360.376], [1, 26.775, 36.89, 371.322, 379.74199999999996], [1, 23.205, 36.89, 389.846, 398.26599999999996], [1, 218.36499999999998, 223.72, 162.506, 170.926], [1, 218.36499999999998, 223.72, 181.03, 189.45], [1, 218.36499999999998, 223.72, 200.396, 208.816], [1, 218.36499999999998, 223.72, 218.92, 227.34], [1, 218.36499999999998, 223.72, 238.286, 246.706], [1, 218.36499999999998, 223.72, 257.652, 266.072], [1, 218.36499999999998, 223.72, 276.176, 284.596], [1, 218.36499999999998, 223.72, 295.542, 303.962], [1, 218.36499999999998, 223.72, 314.066, 322.486], [1, 245.73499999999999, 250.49499999999998, 333.432, 341.852], [1, 266.56, 271.91499999999996, 333.432, 341.852], [1, 289.16999999999996, 294.525, 333.432, 341.852], [1, 310.59, 315.945, 333.432, 341.852], [1, 332.01, 337.365, 333.432, 341.852], [1, 353.43, 358.78499999999997, 333.432, 341.852], [1, 374.84999999999997, 380.205, 333.432, 341.852], [1, 396.27, 401.625, 333.432, 341.852], [1, 417.69, 423.04499999999996, 333.432, 341.852], [1, 438.515, 448.03499999999997, 333.432, 341.852], [1, 459.935, 468.85999999999996, 333.432, 341.852], [1, 481.35499999999996, 490.875, 333.432, 341.852], [1, 502.775, 514.0799999999999, 333.432, 341.852], [1, 524.1949999999999, 534.905, 333.432, 341.852], [1, 546.2099999999999, 559.3, 333.432, 341.852], [1, 374.255, 404.005, 338.484, 348.58799999999997], [1, 468.265, 509.32, 311.53999999999996, 320.80199999999996], [1, 221.935, 508.13, 351.95599999999996, 362.902], [1, 221.935, 308.21, 366.27, 376.37399999999997], [1, 221.935, 242.76, 383.952, 394.89799999999997], [1, 221.935, 262.99, 398.26599999999996, 406.686], [1, 221.935, 327.84499999999997, 407.52799999999996, 415.948], [1, 15.469999999999999, 179.69, 436.998, 447.102], [1, 31.535, 48.79, 454.68, 463.942], [1, 127.33, 140.42, 454.68, 463.942], [1, 164.22, 180.285, 454.68, 463.942], [1, 207.06, 223.125, 454.68, 463.942], [1, 244.545, 264.775, 454.68, 463.942], [1, 281.435, 310.59, 454.68, 463.942], [1, 323.085, 345.695, 454.68, 463.942], [1, 361.16499999999996, 385.56, 454.68, 463.942], [1, 399.245, 423.04499999999996, 454.68, 463.942], [1, 442.68, 459.34, 454.68, 463.942], [1, 483.73499999999996, 504.56, 454.68, 463.942], [1, 519.435, 539.665, 454.68, 463.942], [1, 31.535, 47.599999999999994, 469.83599999999996, 479.09799999999996], [1, 83.3, 88.06, 469.83599999999996, 479.09799999999996], [1, 125.54499999999999, 143.39499999999998, 469.83599999999996, 479.09799999999996], [1, 166.6, 185.045, 469.83599999999996, 479.09799999999996], [1, 205.27499999999998, 229.075, 469.83599999999996, 479.09799999999996], [1, 251.08999999999997, 266.56, 469.83599999999996, 479.09799999999996], [1, 328.44, 345.695, 469.83599999999996, 479.09799999999996], [1, 364.14, 381.99, 469.83599999999996, 479.09799999999996], [1, 401.625, 419.47499999999997, 469.83599999999996, 479.09799999999996], [1, 31.535, 51.765, 481.62399999999997, 490.88599999999997], [1, 83.3, 88.06, 481.62399999999997, 490.88599999999997], [1, 125.54499999999999, 143.39499999999998, 481.62399999999997, 490.88599999999997], [1, 166.6, 185.045, 481.62399999999997, 490.88599999999997], [1, 205.27499999999998, 229.075, 481.62399999999997, 490.88599999999997], [1, 254.66, 266.56, 481.62399999999997, 490.88599999999997], [1, 328.44, 345.695, 481.62399999999997, 490.88599999999997], [1, 364.14, 381.99, 481.62399999999997, 490.88599999999997], [1, 401.625, 419.47499999999997, 481.62399999999997, 490.88599999999997], [1, 31.535, 71.39999999999999, 493.412, 502.674], [1, 83.3, 91.63, 493.412, 502.674], [1, 125.54499999999999, 143.39499999999998, 493.412, 502.674], [1, 166.6, 185.045, 493.412, 502.674], [1, 205.27499999999998, 229.075, 493.412, 502.674], [1, 254.66, 266.56, 493.412, 502.674], [1, 328.44, 345.695, 493.412, 502.674], [1, 361.76, 381.99, 493.412, 502.674], [1, 399.84, 419.47499999999997, 493.412, 502.674], [1, 31.535, 47.004999999999995, 505.2, 514.462], [1, 83.3, 94.00999999999999, 505.2, 514.462], [1, 125.54499999999999, 143.39499999999998, 505.2, 514.462], [1, 166.6, 185.045, 505.2, 514.462], [1, 205.27499999999998, 229.075, 505.2, 514.462], [1, 254.66, 266.56, 505.2, 514.462], [1, 328.44, 345.695, 505.2, 514.462], [1, 361.76, 381.99, 505.2, 514.462], [1, 399.84, 419.47499999999997, 505.2, 514.462], [1, 31.535, 47.004999999999995, 516.9879999999999, 526.25], [1, 83.3, 91.63, 516.9879999999999, 526.25], [1, 174.33499999999998, 185.045, 516.9879999999999, 526.25], [1, 212.415, 223.125, 516.9879999999999, 526.25], [1, 251.08999999999997, 266.56, 516.9879999999999, 526.25], [1, 335.58, 345.695, 516.9879999999999, 526.25], [1, 371.28, 381.99, 516.9879999999999, 526.25], [1, 410.54999999999995, 419.47499999999997, 516.9879999999999, 526.25], [1, 31.535, 65.45, 528.776, 538.038], [1, 83.3, 94.00999999999999, 528.776, 538.038], [1, 125.54499999999999, 143.39499999999998, 528.776, 538.038], [1, 166.6, 185.045, 528.776, 538.038], [1, 205.27499999999998, 223.125, 528.776, 538.038], [1, 254.66, 266.56, 528.776, 538.038], [1, 328.44, 345.695, 528.776, 538.038], [1, 364.14, 381.99, 528.776, 538.038], [1, 401.625, 419.47499999999997, 528.776, 538.038], [1, 31.535, 47.004999999999995, 540.564, 549.826], [1, 83.3, 88.06, 540.564, 549.826], [1, 166.6, 185.045, 540.564, 549.826], [1, 205.27499999999998, 223.125, 540.564, 549.826], [1, 251.08999999999997, 266.56, 540.564, 549.826], [1, 328.44, 345.695, 540.564, 549.826], [1, 364.14, 381.99, 540.564, 549.826], [1, 401.625, 419.47499999999997, 540.564, 549.826], [1, 31.535, 51.765, 552.352, 561.614], [1, 83.3, 88.06, 552.352, 561.614], [1, 125.54499999999999, 143.39499999999998, 552.352, 561.614], [1, 166.6, 185.045, 552.352, 561.614], [1, 205.27499999999998, 223.125, 552.352, 561.614], [1, 251.08999999999997, 266.56, 552.352, 561.614], [1, 328.44, 345.695, 552.352, 561.614], [1, 364.14, 381.99, 552.352, 561.614], [1, 401.625, 419.47499999999997, 552.352, 561.614], [1, 31.535, 47.004999999999995, 564.14, 573.4019999999999], [1, 83.3, 88.06, 564.14, 573.4019999999999], [1, 125.54499999999999, 143.39499999999998, 564.14, 573.4019999999999], [1, 166.6, 185.045, 564.14, 573.4019999999999], [1, 31.535, 47.599999999999994, 575.928, 585.1899999999999], [1, 83.3, 88.06, 575.928, 585.1899999999999], [1, 125.54499999999999, 143.39499999999998, 575.928, 585.1899999999999], [1, 166.6, 185.045, 575.928, 585.1899999999999], [1, 205.27499999999998, 223.125, 575.928, 585.1899999999999], [1, 251.08999999999997, 266.56, 575.928, 585.1899999999999], [1, 31.535, 44.03, 587.716, 596.978], [1, 83.3, 88.06, 587.716, 596.978], [1, 125.54499999999999, 143.39499999999998, 587.716, 596.978], [1, 166.6, 185.045, 587.716, 596.978], [1, 205.27499999999998, 223.125, 587.716, 596.978], [1, 251.08999999999997, 266.56, 587.716, 596.978], [1, 31.535, 67.235, 599.504, 608.766], [1, 83.3, 91.63, 599.504, 608.766], [1, 125.54499999999999, 143.39499999999998, 599.504, 608.766], [1, 166.6, 185.045, 599.504, 608.766], [1, 205.27499999999998, 223.125, 599.504, 608.766], [1, 254.66, 266.56, 599.504, 608.766], [1, 328.44, 345.695, 599.504, 608.766], [1, 361.76, 381.99, 599.504, 608.766], [1, 399.84, 419.47499999999997, 599.504, 608.766], [1, 31.535, 41.055, 611.292, 620.554], [1, 83.3, 88.06, 611.292, 620.554], [1, 166.6, 185.045, 611.292, 620.554], [1, 205.27499999999998, 223.125, 611.292, 620.554], [1, 251.08999999999997, 266.56, 611.292, 620.554], [1, 31.535, 49.98, 622.2379999999999, 631.5], [1, 83.3, 101.14999999999999, 622.2379999999999, 631.5], [1, 163.03, 185.045, 622.2379999999999, 631.5], [1, 205.27499999999998, 223.125, 622.2379999999999, 631.5], [1, 254.66, 266.56, 622.2379999999999, 631.5], [1, 31.535, 321.3, 634.026, 643.288], [1, 14.875, 35.699999999999996, 651.708, 662.654], [1, 50.574999999999996, 262.395, 663.496, 692.124], [1, 14.875, 87.46499999999999, 709.8059999999999, 730.014]]
2026-08-10 13:14:14,291 INFO     29 [qwen-vl-text] ═══ DONE ═══ 189 positions, pages=2, time=57.5s
2026-08-10 13:14:14,292 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:14:14,299 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:14:14,299 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 13:14:14,299 INFO     29 [qwen-vl-text] positions(85): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:14:14,299 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [85]
2026-08-10 13:14:14,534 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:14:14,534 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1007
2026-08-10 13:14:14,534 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:14:14,535 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 257, \"bbox_end\": 341, \"encounter_dates\": [\"2025-05-28\"], \"department\": \"呼吸科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "肺功能检验结果\n新乡市第二人民医院\n呼吸科\n12323\nFVC\nFEV1\nFEV1%\nPRE\nPRE\nPRE\n应诊日期 2025/5/28\n病人号码\n年龄 85\n姓氏\n性别 男\n名字\n高度, cm 170\n出生日期 1990/2/5\n重量, kg 85\n人种 中国人\nBMI 29.41\n吸烟 非吸烟者\n患者组 包-年\n14\n12\n10\n8\n6\n4\n2\n0\n-2\n-4\n8\n7\n6\n5\n4\n3\n2\n1\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n时间(s)\n@已预测的\n质量控制等级: D 变化性: FEV1=0.06L (2.63%), FVC=0.45L (10.23%)\n1 Acceptable trials\n评估\n中度的阻塞.\nWARNING: FEF2575 前 = 39%预测, FEV1/EVC 前 = 45%\n前/测验日期 2025/5/28 17:15:41\n参数 LLN 预计 Best %预计 Z-score 前 #1 前 #2 前 #3 POST %预计 %激发\nFVC L 3.47 4.52 4.85* 107 4.85 4.37 4.40 *\nFEV1 L 2.91 3.77 2.34* 62 2.13 2.34 2.28 *\nFEV1/FVC % 73.8 84.0 48.2* 57 43.9 53.5 51.8 *\nPEF L/s 5.34 8.76 2.71* 31 2.71 2.34 2.67 *\nELA 年 35 91 260 91 84 86\nFEF2575 L/s 2.27 4.05 1.57 39 1.57 1.80 1.57\nFET s 6.00 7.32 122 7.32 5.88 5.68\nFIVC L 3.47 4.52 3.86 85 3.86 4.20 4.24\nIVC L 3.47 4.52\nEVC L 3.47 4.52 5.16 114\nVC L 3.47 4.52 5.16 114\nFEV1/VC % 73.8 84.0 41.3 49\nIC L 3.03 3.58 118\nMVV L/min 136.2 42.9 31\n*全部曲线之最佳值 - BTPS 1.082 27 °C (80.6 °F) - 已预测的 Knudson\n结论\n签名\n所用仪器\nSpirolab III S/N 313469",
    "role": "user"
  }
]
2026-08-10 13:14:14,537 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:14:14.536+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 41, "failed": 0, "current": {"2031b7c094bd11f1bd9827cf206dfa2d": {"id": "2031b7c094bd11f1bd9827cf206dfa2d", "doc_id": "1ff3926094bd11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LYBI-\u827e\u7279\u7f8e\u54ee\u5598(1).pdf", "type": "pdf", "location": "LYBI-\u827e\u7279\u7f8e\u54ee\u5598(1).pdf", "size": 2220448, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367543508, "task_type": "dataflow", "root_trace_id": "e8588e7f2a8f4f7ea72bfd924542e9bc", "root_traceparent": "00-e8588e7f2a8f4f7ea72bfd924542e9bc-f1b6b538ed925a47-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:14:22,657 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:14:22,657 INFO     29 [qwen-vl-text] LLM output (len=1496):
{
  "exam_date": "2025-05-28",
  "report_date": "2025-05-28",
  "exam_name": "肺功能检验",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "男",
  "department": "呼吸科",
  "bed_number": null,
  "findings": "质量控制等级: D 变化性: FEV1=0.06L (2.63%), FVC=0.45L (10.23%)\n1 Acceptable trials\n评估\n中度的阻塞.\nWARNING: FEF2575 前 = 39%预测, FEV1/EVC 前 = 45%\n前/测验日期 2025/5/28 17:15:41\n| 参数 | LLN | 预计 | Best | %预计 | Z-score | 前 #1 | 前 #2 | 前 #3 | POST | %预计 | %激发 |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n| FVC L | 3.47 | 4.52 | 4.85* | 107 | | 4.85 | 4.37 | 4.40 | * | | |\n| FEV1 L | 2.91 | 3.77 | 2.34* | 62 | | 2.13 | 2.34 | 2.28 | * | | |\n| FEV1/FVC % | 73.8 | 84.0 | 48.2* | 57 | | 43.9 | 53.5 | 51.8 | * | | |\n| PEF L/s | 5.34 | 8.76 | 2.71* | 31 | | 2.71 | 2.34 | 2.67 | * | | |\n| ELA 年 | 35 | 91 | 260 | 91 | | 84 | 86 | | | | |\n| FEF2575 L/s | 2.27 | 4.05 | 1.57 | 39 | | 1.57 | 1.80 | 1.57 | | | |\n| FET s | 6.00 | 7.32 | 122 | | | 7.32 | 5.88 | 5.68 | | | |\n| FIVC L | 3.47 | 4.52 | 3.86 | 85 | | 3.86 | 4.20 | 4.24 | | | |\n| IVC L | 3.47 | 4.52 | | | | | | | | | |\n| EVC L | 3.47 | 4.52 | 5.16 | 114 | | | | | | | |\n| VC L | 3.47 | 4.52 | 5.16 | 114 | | | | | | | |\n| FEV1/VC % | 73.8 | 84.0 | 41.3 | 49 | | | | | | | |\n| IC L | 3.03 | 3.58 | 118 | | | | | | | | |\n| MVV L/min | 136.2 | 42.9 | 31 | | | | | | | | |\n*全部曲线之最佳值 - BTPS 1.082 27 °C (80.6 °F) - 已预测的 Knudson",
  "conclusion": "中度的阻塞.",
  "physician": null,
  "reviewer": null
}
2026-08-10 13:14:22,659 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=906032, prompt_len=1875
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共85行）
["肺功能检验结果", "新乡市第二人民医院", "呼吸科", "12323", "FVC", "FEV1", "FEV1%", "PRE", "PRE", "PRE", "应诊日期 2025/5/28", "病人号码", "年龄 85", "姓氏", "性别 男", "名字", "高度, cm 170", "出生日期 1990/2/5", "重量, kg 85", "人种 中国人", "BMI 29.41", "吸烟 非吸烟者", "患者组 包-年", "14", "12", "10", "8", "6", "4", "2", "0", "-2", "-4", "8", "7", "6", "5", "4", "3", "2", "1", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "时间(s)", "@已预测的", "质量控制等级: D 变化性: FEV1=0.06L (2.63%), FVC=0.45L (10.23%)", "1 Acceptable trials", "评估", "中度的阻塞.", "WARNING: FEF2575 前 = 39%预测, FEV1/EVC 前 = 45%", "前/测验日期 2025/5/28 17:15:41", "参数 LLN 预计 Best %预计 Z-score 前 #1 前 #2 前 #3 POST %预计 %激发", "FVC L 3.47 4.52 4.85* 107 4.85 4.37 4.40 *", "FEV1 L 2.91 3.77 2.34* 62 2.13 2.34 2.28 *", "FEV1/FVC % 73.8 84.0 48.2* 57 43.9 53.5 51.8 *", "PEF L/s 5.34 8.76 2.71* 31 2.71 2.34 2.67 *", "ELA 年 35 91 260 91 84 86", "FEF2575 L/s 2.27 4.05 1.57 39 1.57 1.80 1.57", "FET s 6.00 7.32 122 7.32 5.88 5.68", "FIVC L 3.47 4.52 3.86 85 3.86 4.20 4.24", "IVC L 3.47 4.52", "EVC L 3.47 4.52 5.16 114", "VC L 3.47 4.52 5.16 114", "FEV1/VC % 73.8 84.0 41.3 49", "IC L 3.03 3.58 118", "MVV L/min 136.2 42.9 31", "*全部曲线之最佳值 - BTPS 1.082 27 °C (80.6 °F) - 已预测的 Knudson", "结论", "签名", "所用仪器", "Spirolab III S/N 313469"]

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
2026-08-10 13:14:48,451 INFO     29 [qwen-vl-text] coord API raw response (len=4814):
[
	{"text": "肺功能检验结果", "bbox": [50, 0, 165, 11]},
	{"text": "新乡市第二人民医院", "bbox": [50, 25, 197, 38]},
	{"text": "呼吸科", "bbox": [50, 62, 95, 73]},
	{"text": "12323", "bbox": [50, 83, 86, 93]},
	{"text": "FVC", "bbox": [57, 121, 80, 130]},
	{"text": "FEV1", "bbox": [207, 121, 234, 130]},
	{"text": "FEV1%", "bbox": [352, 121, 386, 130]},
	{"text": "PRE", "bbox": [60, 133, 77, 141]},
	{"text": "PRE", "bbox": [209, 133, 226, 141]},
	{"text": "PRE", "bbox": [354, 133, 370, 141]},
	{"text": "应诊日期 2025/5/28", "bbox": [498, 39, 642, 52]},
	{"text": "病人号码", "bbox": [498, 60, 555, 72]},
	{"text": "年龄 85", "bbox": [760, 61, 791, 72]},
	{"text": "姓氏", "bbox": [498, 75, 528, 86]},
	{"text": "性别 男", "bbox": [760, 75, 875, 88]},
	{"text": "名字", "bbox": [498, 89, 528, 100]},
	{"text": "高度, cm 170", "bbox": [760, 91, 875, 103]},
	{"text": "出生日期 1990/2/5", "bbox": [498, 103, 555, 115]},
	{"text": "重量, kg 85", "bbox": [760, 105, 867, 116]},
	{"text": "人种 中国人", "bbox": [498, 117, 658, 129]},
	{"text": "BMI 29.41", "bbox": [760, 119, 892, 130]},
	{"text": "吸烟 非吸烟者", "bbox": [498, 131, 674, 143]},
	{"text": "患者组 包-年", "bbox": [498, 145, 541, 156]},
	{"text": "14", "bbox": [64, 172, 81, 183]},
	{"text": "12", "bbox": [64, 193, 81, 204]},
	{"text": "10", "bbox": [64, 215, 81, 226]},
	{"text": "8", "bbox": [71, 238, 81, 249]},
	{"text": "6", "bbox": [71, 261, 81, 272]},
	{"text": "4", "bbox": [71, 284, 81, 295]},
	{"text": "2", "bbox": [71, 307, 81, 318]},
	{"text": "0", "bbox": [71, 330, 81, 341]},
	{"text": "-2", "bbox": [67, 353, 84, 364]},
	{"text": "-4", "bbox": [67, 376, 84, 387]},
	{"text": "-6", "bbox": [67, 399, 84, 410]},
	{"text": "-8", "bbox": [67, 421, 84, 432]},
	{"text": "-10", "bbox": [57, 443, 84, 455]},
	{"text": "8", "bbox": [374, 171, 384, 181]},
	{"text": "7", "bbox": [374, 193, 384, 204]},
	{"text": "6", "bbox": [374, 215, 384, 226]},
	{"text": "5", "bbox": [374, 238, 384, 249]},
	{"text": "4", "bbox": [374, 261, 384, 272]},
	{"text": "3", "bbox": [374, 284, 384, 295]},
	{"text": "2", "bbox": [374, 307, 384, 318]},
	{"text": "1", "bbox": [374, 330, 384, 341]},
	{"text": "0", "bbox": [374, 353, 384, 364]},
	{"text": "1", "bbox": [417, 372, 425, 383]},
	{"text": "2", "bbox": [451, 372, 461, 383]},
	{"text": "3", "bbox": [487, 372, 496, 383]},
	{"text": "4", "bbox": [520, 372, 529, 383]},
	{"text": "5", "bbox": [555, 372, 565, 383]},
	{"text": "6", "bbox": [590, 372, 600, 383]},
	{"text": "7", "bbox": [625, 372, 635, 383]},
	{"text": "8", "bbox": [660, 372, 670, 383]},
	{"text": "9", "bbox": [695, 372, 705, 383]},
	{"text": "10", "bbox": [728, 372, 745, 383]},
	{"text": "11", "bbox": [763, 372, 779, 383]},
	{"text": "12", "bbox": [798, 372, 815, 383]},
	{"text": "13", "bbox": [833, 372, 850, 383]},
	{"text": "14", "bbox": [868, 372, 886, 383]},
	{"text": "15", "bbox": [907, 372, 925, 383]},
	{"text": "时间(s)", "bbox": [624, 380, 672, 392]},
	{"text": "@已预测的", "bbox": [776, 348, 843, 359]},
	{"text": "质量控制等级: D 变化性: FEV1=0.06L (2.63%), FVC=0.45L (10.23%)", "bbox": [379, 398, 849, 410]},
	{"text": "1 Acceptable trials", "bbox": [379, 413, 518, 424]},
	{"text": "评估", "bbox": [379, 434, 414, 446]},
	{"text": "中度的阻塞.", "bbox": [380, 452, 447, 462]},
	{"text": "WARNING: FEF2575 前 = 39%预测, FEV1/EVC 前 = 45%", "bbox": [380, 462, 691, 472]},
	{"text": "前/测验日期 2025/5/28 17:15:41", "bbox": [50, 497, 313, 509]},
	{"text": "参数 LLN 预计 Best %预计 Z-score 前 #1 前 #2 前 #3 POST %预计 %激发", "bbox": [76, 518, 894, 529]},
	{"text": "FVC L 3.47 4.52 4.85* 107 4.85 4.37 4.40 *", "bbox": [76, 534, 705, 546]},
	{"text": "FEV1 L 2.91 3.77 2.34* 62 2.13 2.34 2.28 *", "bbox": [76, 547, 705, 559]},
	{"text": "FEV1/FVC % 73.8 84.0 48.2* 57 43.9 53.5 51.8 *", "bbox": [76, 560, 705, 572]},
	{"text": "PEF L/s 5.34 8.76 2.71* 31 2.71 2.34 2.67 *", "bbox": [76, 573, 705, 585]},
	{"text": "ELA 年 35 91 260 91 84 86", "bbox": [76, 586, 705, 598]},
	{"text": "FEF2575 L/s 2.27 4.05 1.57 39 1.57 1.80 1.57", "bbox": [76, 599, 705, 611]},
	{"text": "FET s 6.00 7.32 122 7.32 5.88 5.68", "bbox": [76, 612, 705, 624]},
	{"text": "FIVC L 3.47 4.52 3.86 85 3.86 4.20 4.24", "bbox": [76, 625, 705, 637]},
	{"text": "IVC L 3.47 4.52", "bbox": [76, 638, 325, 650]},
	{"text": "EVC L 3.47 4.52 5.16 114", "bbox": [76, 651, 452, 663]},
	{"text": "VC L 3.47 4.52 5.16 114", "bbox": [76, 664, 452, 676]},
	{"text": "FEV1/VC % 73.8 84.0 41.3 49", "bbox": [76, 677, 452, 689]},
	{"text": "IC L 3.03 3.58 118", "bbox": [76, 690, 452, 702]},
	{"text": "MVV L/min 136.2 42.9 31", "bbox": [76, 703, 452, 715]},
	{"text": "*全部曲线之最佳值 - BTPS 1.082 27 °C (80.6 °F) - 已预测的 Knudson", "bbox": [76, 722, 539, 733]},
	{"text": "结论", "bbox": [50, 743, 87, 755]},
	{"text": "签名", "bbox": [45, 814, 82, 826]},
	{"text": "所用仪器", "bbox": [870, 817, 925, 827]},
	{"text": "Spirolab III S/N 313469", "bbox": [768, 831, 925, 841]}
]
2026-08-10 13:14:48,451 INFO     29 [qwen-vl-text] coord API: raw_items=88, valid_items=88, elapsed=25.8s
2026-08-10 13:14:48,452 INFO     29 [qwen-vl-text] coord item[0]: text=肺功能检验结果, bbox=[50, 0, 165, 11]
2026-08-10 13:14:48,452 INFO     29 [qwen-vl-text] coord item[1]: text=新乡市第二人民医院, bbox=[50, 25, 197, 38]
2026-08-10 13:14:48,452 INFO     29 [qwen-vl-text] coord item[2]: text=呼吸科, bbox=[50, 62, 95, 73]
2026-08-10 13:14:48,452 INFO     29 [qwen-vl-text] coord item[3]: text=12323, bbox=[50, 83, 86, 93]
2026-08-10 13:14:48,452 INFO     29 [qwen-vl-text] coord item[4]: text=FVC, bbox=[57, 121, 80, 130]
2026-08-10 13:14:48,452 INFO     29 [qwen-vl-text] coord item[5]: text=FEV1, bbox=[207, 121, 234, 130]
2026-08-10 13:14:48,452 INFO     29 [qwen-vl-text] coord item[6]: text=FEV1%, bbox=[352, 121, 386, 130]
2026-08-10 13:14:48,452 INFO     29 [qwen-vl-text] coord item[7]: text=PRE, bbox=[60, 133, 77, 141]
2026-08-10 13:14:48,452 INFO     29 [qwen-vl-text] coord item[8]: text=PRE, bbox=[209, 133, 226, 141]
2026-08-10 13:14:48,452 INFO     29 [qwen-vl-text] coord item[9]: text=PRE, bbox=[354, 133, 370, 141]
2026-08-10 13:14:48,452 INFO     29 [qwen-vl-text] coord item[10]: text=应诊日期 2025/5/28, bbox=[498, 39, 642, 52]
2026-08-10 13:14:48,453 INFO     29 [qwen-vl-text] coord item[11]: text=病人号码, bbox=[498, 60, 555, 72]
2026-08-10 13:14:48,453 INFO     29 [qwen-vl-text] coord item[12]: text=年龄 85, bbox=[760, 61, 791, 72]
2026-08-10 13:14:48,453 INFO     29 [qwen-vl-text] coord item[13]: text=姓氏, bbox=[498, 75, 528, 86]
2026-08-10 13:14:48,453 INFO     29 [qwen-vl-text] coord item[14]: text=性别 男, bbox=[760, 75, 875, 88]
2026-08-10 13:14:48,453 INFO     29 [qwen-vl-text] coord item[15]: text=名字, bbox=[498, 89, 528, 100]
2026-08-10 13:14:48,453 INFO     29 [qwen-vl-text] coord item[16]: text=高度, cm 170, bbox=[760, 91, 875, 103]
2026-08-10 13:14:48,453 INFO     29 [qwen-vl-text] coord item[17]: text=出生日期 1990/2/5, bbox=[498, 103, 555, 115]
2026-08-10 13:14:48,453 INFO     29 [qwen-vl-text] coord item[18]: text=重量, kg 85, bbox=[760, 105, 867, 116]
2026-08-10 13:14:48,453 INFO     29 [qwen-vl-text] coord item[19]: text=人种 中国人, bbox=[498, 117, 658, 129]
2026-08-10 13:14:48,453 INFO     29 [qwen-vl-text] coord item[20]: text=BMI 29.41, bbox=[760, 119, 892, 130]
2026-08-10 13:14:48,453 INFO     29 [qwen-vl-text] coord item[21]: text=吸烟 非吸烟者, bbox=[498, 131, 674, 143]
2026-08-10 13:14:48,453 INFO     29 [qwen-vl-text] coord item[22]: text=患者组 包-年, bbox=[498, 145, 541, 156]
2026-08-10 13:14:48,453 INFO     29 [qwen-vl-text] coord item[23]: text=14, bbox=[64, 172, 81, 183]
2026-08-10 13:14:48,453 INFO     29 [qwen-vl-text] coord item[24]: text=12, bbox=[64, 193, 81, 204]
2026-08-10 13:14:48,453 INFO     29 [qwen-vl-text] coord item[25]: text=10, bbox=[64, 215, 81, 226]
2026-08-10 13:14:48,453 INFO     29 [qwen-vl-text] coord item[26]: text=8, bbox=[71, 238, 81, 249]
2026-08-10 13:14:48,453 INFO     29 [qwen-vl-text] coord item[27]: text=6, bbox=[71, 261, 81, 272]
2026-08-10 13:14:48,454 INFO     29 [qwen-vl-text] coord item[28]: text=4, bbox=[71, 284, 81, 295]
2026-08-10 13:14:48,454 INFO     29 [qwen-vl-text] coord item[29]: text=2, bbox=[71, 307, 81, 318]
2026-08-10 13:14:48,454 INFO     29 [qwen-vl-text] coord item[30]: text=0, bbox=[71, 330, 81, 341]
2026-08-10 13:14:48,454 INFO     29 [qwen-vl-text] coord item[31]: text=-2, bbox=[67, 353, 84, 364]
2026-08-10 13:14:48,454 INFO     29 [qwen-vl-text] coord item[32]: text=-4, bbox=[67, 376, 84, 387]
2026-08-10 13:14:48,454 INFO     29 [qwen-vl-text] coord item[33]: text=-6, bbox=[67, 399, 84, 410]
2026-08-10 13:14:48,454 INFO     29 [qwen-vl-text] coord item[34]: text=-8, bbox=[67, 421, 84, 432]
2026-08-10 13:14:48,454 INFO     29 [qwen-vl-text] coord item[35]: text=-10, bbox=[57, 443, 84, 455]
2026-08-10 13:14:48,454 INFO     29 [qwen-vl-text] coord item[36]: text=8, bbox=[374, 171, 384, 181]
2026-08-10 13:14:48,454 INFO     29 [qwen-vl-text] coord item[37]: text=7, bbox=[374, 193, 384, 204]
2026-08-10 13:14:48,454 INFO     29 [qwen-vl-text] coord item[38]: text=6, bbox=[374, 215, 384, 226]
2026-08-10 13:14:48,454 INFO     29 [qwen-vl-text] coord item[39]: text=5, bbox=[374, 238, 384, 249]
2026-08-10 13:14:48,454 INFO     29 [qwen-vl-text] coord item[40]: text=4, bbox=[374, 261, 384, 272]
2026-08-10 13:14:48,455 INFO     29 [qwen-vl-text] coord item[41]: text=3, bbox=[374, 284, 384, 295]
2026-08-10 13:14:48,455 INFO     29 [qwen-vl-text] coord item[42]: text=2, bbox=[374, 307, 384, 318]
2026-08-10 13:14:48,455 INFO     29 [qwen-vl-text] coord item[43]: text=1, bbox=[374, 330, 384, 341]
2026-08-10 13:14:48,455 INFO     29 [qwen-vl-text] coord item[44]: text=0, bbox=[374, 353, 384, 364]
2026-08-10 13:14:48,455 INFO     29 [qwen-vl-text] coord item[45]: text=1, bbox=[417, 372, 425, 383]
2026-08-10 13:14:48,455 INFO     29 [qwen-vl-text] coord item[46]: text=2, bbox=[451, 372, 461, 383]
2026-08-10 13:14:48,455 INFO     29 [qwen-vl-text] coord item[47]: text=3, bbox=[487, 372, 496, 383]
2026-08-10 13:14:48,455 INFO     29 [qwen-vl-text] coord item[48]: text=4, bbox=[520, 372, 529, 383]
2026-08-10 13:14:48,455 INFO     29 [qwen-vl-text] coord item[49]: text=5, bbox=[555, 372, 565, 383]
2026-08-10 13:14:48,455 INFO     29 [qwen-vl-text] coord item[50]: text=6, bbox=[590, 372, 600, 383]
2026-08-10 13:14:48,455 INFO     29 [qwen-vl-text] coord item[51]: text=7, bbox=[625, 372, 635, 383]
2026-08-10 13:14:48,455 INFO     29 [qwen-vl-text] coord item[52]: text=8, bbox=[660, 372, 670, 383]
2026-08-10 13:14:48,455 INFO     29 [qwen-vl-text] coord item[53]: text=9, bbox=[695, 372, 705, 383]
2026-08-10 13:14:48,455 INFO     29 [qwen-vl-text] coord item[54]: text=10, bbox=[728, 372, 745, 383]
2026-08-10 13:14:48,456 INFO     29 [qwen-vl-text] coord item[55]: text=11, bbox=[763, 372, 779, 383]
2026-08-10 13:14:48,456 INFO     29 [qwen-vl-text] coord item[56]: text=12, bbox=[798, 372, 815, 383]
2026-08-10 13:14:48,456 INFO     29 [qwen-vl-text] coord item[57]: text=13, bbox=[833, 372, 850, 383]
2026-08-10 13:14:48,456 INFO     29 [qwen-vl-text] coord item[58]: text=14, bbox=[868, 372, 886, 383]
2026-08-10 13:14:48,456 INFO     29 [qwen-vl-text] coord item[59]: text=15, bbox=[907, 372, 925, 383]
2026-08-10 13:14:48,456 INFO     29 [qwen-vl-text] coord item[60]: text=时间(s), bbox=[624, 380, 672, 392]
2026-08-10 13:14:48,456 INFO     29 [qwen-vl-text] coord item[61]: text=@已预测的, bbox=[776, 348, 843, 359]
2026-08-10 13:14:48,456 INFO     29 [qwen-vl-text] coord item[62]: text=质量控制等级: D 变化性: FEV1=0.06L (2.63%), FVC=0.45L (10.23%), bbox=[379, 398, 849, 410]
2026-08-10 13:14:48,456 INFO     29 [qwen-vl-text] coord item[63]: text=1 Acceptable trials, bbox=[379, 413, 518, 424]
2026-08-10 13:14:48,456 INFO     29 [qwen-vl-text] coord item[64]: text=评估, bbox=[379, 434, 414, 446]
2026-08-10 13:14:48,456 INFO     29 [qwen-vl-text] coord item[65]: text=中度的阻塞., bbox=[380, 452, 447, 462]
2026-08-10 13:14:48,456 INFO     29 [qwen-vl-text] coord item[66]: text=WARNING: FEF2575 前 = 39%预测, FEV1/EVC 前 = 45%, bbox=[380, 462, 691, 472]
2026-08-10 13:14:48,456 INFO     29 [qwen-vl-text] coord item[67]: text=前/测验日期 2025/5/28 17:15:41, bbox=[50, 497, 313, 509]
2026-08-10 13:14:48,456 INFO     29 [qwen-vl-text] coord item[68]: text=参数 LLN 预计 Best %预计 Z-score 前 #1 前 #2 前 #3 POST %预计 %激发, bbox=[76, 518, 894, 529]
2026-08-10 13:14:48,456 INFO     29 [qwen-vl-text] coord item[69]: text=FVC L 3.47 4.52 4.85* 107 4.85 4.37 4.40 *, bbox=[76, 534, 705, 546]
2026-08-10 13:14:48,456 INFO     29 [qwen-vl-text] coord item[70]: text=FEV1 L 2.91 3.77 2.34* 62 2.13 2.34 2.28 *, bbox=[76, 547, 705, 559]
2026-08-10 13:14:48,457 INFO     29 [qwen-vl-text] coord item[71]: text=FEV1/FVC % 73.8 84.0 48.2* 57 43.9 53.5 51.8 *, bbox=[76, 560, 705, 572]
2026-08-10 13:14:48,457 INFO     29 [qwen-vl-text] coord item[72]: text=PEF L/s 5.34 8.76 2.71* 31 2.71 2.34 2.67 *, bbox=[76, 573, 705, 585]
2026-08-10 13:14:48,457 INFO     29 [qwen-vl-text] coord item[73]: text=ELA 年 35 91 260 91 84 86, bbox=[76, 586, 705, 598]
2026-08-10 13:14:48,457 INFO     29 [qwen-vl-text] coord item[74]: text=FEF2575 L/s 2.27 4.05 1.57 39 1.57 1.80 1.57, bbox=[76, 599, 705, 611]
2026-08-10 13:14:48,457 INFO     29 [qwen-vl-text] coord item[75]: text=FET s 6.00 7.32 122 7.32 5.88 5.68, bbox=[76, 612, 705, 624]
2026-08-10 13:14:48,457 INFO     29 [qwen-vl-text] coord item[76]: text=FIVC L 3.47 4.52 3.86 85 3.86 4.20 4.24, bbox=[76, 625, 705, 637]
2026-08-10 13:14:48,457 INFO     29 [qwen-vl-text] coord item[77]: text=IVC L 3.47 4.52, bbox=[76, 638, 325, 650]
2026-08-10 13:14:48,457 INFO     29 [qwen-vl-text] coord item[78]: text=EVC L 3.47 4.52 5.16 114, bbox=[76, 651, 452, 663]
2026-08-10 13:14:48,457 INFO     29 [qwen-vl-text] coord item[79]: text=VC L 3.47 4.52 5.16 114, bbox=[76, 664, 452, 676]
2026-08-10 13:14:48,457 INFO     29 [qwen-vl-text] coord item[80]: text=FEV1/VC % 73.8 84.0 41.3 49, bbox=[76, 677, 452, 689]
2026-08-10 13:14:48,457 INFO     29 [qwen-vl-text] coord item[81]: text=IC L 3.03 3.58 118, bbox=[76, 690, 452, 702]
2026-08-10 13:14:48,457 INFO     29 [qwen-vl-text] coord item[82]: text=MVV L/min 136.2 42.9 31, bbox=[76, 703, 452, 715]
2026-08-10 13:14:48,457 INFO     29 [qwen-vl-text] coord item[83]: text=*全部曲线之最佳值 - BTPS 1.082 27 °C (80.6 °F) - 已预测的 Knudson, bbox=[76, 722, 539, 733]
2026-08-10 13:14:48,457 INFO     29 [qwen-vl-text] coord item[84]: text=结论, bbox=[50, 743, 87, 755]
2026-08-10 13:14:48,457 INFO     29 [qwen-vl-text] coord item[85]: text=签名, bbox=[45, 814, 82, 826]
2026-08-10 13:14:48,457 INFO     29 [qwen-vl-text] coord item[86]: text=所用仪器, bbox=[870, 817, 925, 827]
2026-08-10 13:14:48,457 INFO     29 [qwen-vl-text] coord item[87]: text=Spirolab III S/N 313469, bbox=[768, 831, 925, 841]
2026-08-10 13:14:48,457 INFO     29 [qwen-vl-text] page=2 — 85/85 coords, api_time=25.8s
2026-08-10 13:14:48,458 INFO     29 [qwen-vl-text] new_positions (85):
[[2, 29.75, 98.175, 0.0, 9.262], [2, 29.75, 117.21499999999999, 21.05, 31.996], [2, 29.75, 56.525, 52.204, 61.466], [2, 29.75, 51.169999999999995, 69.886, 78.306], [2, 33.915, 47.599999999999994, 101.88199999999999, 109.46], [2, 123.16499999999999, 139.23, 101.88199999999999, 109.46], [2, 209.44, 229.67, 101.88199999999999, 109.46], [2, 35.699999999999996, 45.815, 111.98599999999999, 118.722], [2, 124.35499999999999, 134.47, 111.98599999999999, 118.722], [2, 210.63, 220.14999999999998, 111.98599999999999, 118.722], [2, 296.31, 381.99, 32.838, 43.784], [2, 296.31, 330.22499999999997, 50.519999999999996, 60.623999999999995], [2, 452.2, 470.645, 51.361999999999995, 60.623999999999995], [2, 296.31, 314.15999999999997, 63.15, 72.41199999999999], [2, 452.2, 520.625, 63.15, 74.096], [2, 296.31, 314.15999999999997, 74.938, 84.2], [2, 452.2, 520.625, 76.622, 86.726], [2, 296.31, 330.22499999999997, 86.726, 96.83], [2, 452.2, 515.865, 88.41, 97.672], [2, 296.31, 391.51, 98.514, 108.618], [2, 452.2, 530.74, 100.198, 109.46], [2, 296.31, 401.03, 110.30199999999999, 120.40599999999999], [2, 296.31, 321.895, 122.08999999999999, 131.352], [2, 38.08, 48.195, 144.82399999999998, 154.08599999999998], [2, 38.08, 48.195, 162.506, 171.768], [2, 38.08, 48.195, 181.03, 190.292], [2, 42.245, 48.195, 200.396, 209.658], [2, 42.245, 48.195, 219.762, 229.024], [2, 42.245, 48.195, 239.128, 248.39], [2, 42.245, 48.195, 258.49399999999997, 267.756], [2, 42.245, 48.195, 277.86, 287.122], [2, 39.864999999999995, 49.98, 297.226, 306.488], [2, 39.864999999999995, 49.98, 316.592, 325.854], [2, 39.864999999999995, 49.98, 335.95799999999997, 345.21999999999997], [2, 39.864999999999995, 49.98, 354.48199999999997, 363.74399999999997], [2, 33.915, 49.98, 373.006, 383.11], [2, 222.53, 228.48, 143.982, 152.402], [2, 222.53, 228.48, 162.506, 171.768], [2, 222.53, 228.48, 181.03, 190.292], [2, 222.53, 228.48, 200.396, 209.658], [2, 222.53, 228.48, 219.762, 229.024], [2, 222.53, 228.48, 239.128, 248.39], [2, 222.53, 228.48, 258.49399999999997, 267.756], [2, 222.53, 228.48, 277.86, 287.122], [2, 222.53, 228.48, 297.226, 306.488], [2, 248.11499999999998, 252.875, 313.224, 322.486], [2, 268.34499999999997, 274.295, 313.224, 322.486], [2, 289.765, 295.12, 313.224, 322.486], [2, 309.4, 314.755, 313.224, 322.486], [2, 330.22499999999997, 336.175, 313.224, 322.486], [2, 351.05, 357.0, 313.224, 322.486], [2, 371.875, 377.825, 313.224, 322.486], [2, 392.7, 398.65, 313.224, 322.486], [2, 413.525, 419.47499999999997, 313.224, 322.486], [2, 433.15999999999997, 443.275, 313.224, 322.486], [2, 453.98499999999996, 463.505, 313.224, 322.486], [2, 474.81, 484.92499999999995, 313.224, 322.486], [2, 495.635, 505.75, 313.224, 322.486], [2, 516.4599999999999, 527.17, 313.224, 322.486], [2, 539.665, 550.375, 313.224, 322.486], [2, 371.28, 399.84, 319.96, 330.06399999999996], [2, 461.71999999999997, 501.585, 293.01599999999996, 302.27799999999996], [2, 225.505, 505.155, 335.116, 345.21999999999997], [2, 225.505, 308.21, 347.746, 357.008], [2, 225.505, 246.32999999999998, 365.428, 375.532], [2, 226.1, 265.965, 380.584, 389.00399999999996], [2, 226.1, 411.145, 389.00399999999996, 397.424], [2, 29.75, 186.23499999999999, 418.474, 428.578], [2, 45.22, 531.93, 436.156, 445.418], [2, 45.22, 419.47499999999997, 449.628, 459.73199999999997], [2, 45.22, 419.47499999999997, 460.574, 470.678], [2, 45.22, 419.47499999999997, 471.52, 481.62399999999997], [2, 45.22, 419.47499999999997, 482.466, 492.57], [2, 45.22, 419.47499999999997, 493.412, 503.51599999999996], [2, 45.22, 419.47499999999997, 504.358, 514.462], [2, 45.22, 419.47499999999997, 515.304, 525.408], [2, 45.22, 419.47499999999997, 526.25, 536.3539999999999], [2, 45.22, 193.375, 537.196, 547.3], [2, 45.22, 268.94, 548.1419999999999, 558.246], [2, 45.22, 268.94, 559.088, 569.192], [2, 45.22, 268.94, 570.034, 580.138], [2, 45.22, 268.94, 580.98, 591.084], [2, 45.22, 268.94, 591.9259999999999, 602.03], [2, 45.22, 320.705, 607.924, 617.1859999999999], [2, 29.75, 51.765, 625.606, 635.7099999999999]]
2026-08-10 13:14:48,458 INFO     29 [qwen-vl-text] ═══ DONE ═══ 85 positions, pages=1, time=34.2s
2026-08-10 13:14:48,475 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 13:14:48,475 INFO     29 [Trace] task=2031b7c0 | doc=LYBI-艾特美哮喘(1).pdf | Extractor:ExaminationReport | outputs={"chunks": "2 items, types={'ExaminationReport': 2}", "html": "", "json": "342 items", "markdown": "", "text": "", "name": "LYBI-艾特美哮喘(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 13:14:48,475 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 13:14:48,476 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:14:48.476+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 41, "failed": 0, "current": {"2031b7c094bd11f1bd9827cf206dfa2d": {"id": "2031b7c094bd11f1bd9827cf206dfa2d", "doc_id": "1ff3926094bd11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LYBI-\u827e\u7279\u7f8e\u54ee\u5598(1).pdf", "type": "pdf", "location": "LYBI-\u827e\u7279\u7f8e\u54ee\u5598(1).pdf", "size": 2220448, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367543508, "task_type": "dataflow", "root_trace_id": "e8588e7f2a8f4f7ea72bfd924542e9bc", "root_traceparent": "00-e8588e7f2a8f4f7ea72bfd924542e9bc-f1b6b538ed925a47-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:14:48,482 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:14:48,482 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:14:49,644 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:14:49,653 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 13:14:49,653 INFO     29 [Trace] task=2031b7c0 | doc=LYBI-艾特美哮喘(1).pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "342 items", "markdown": "", "text": "", "name": "LYBI-艾特美哮喘(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 13:14:49,653 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 13:14:49,654 INFO     29 [ChunkMerger] Merged 3 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 2, 'Extractor:Progress': 1} (filtered 7 noise chunks)
2026-08-10 13:14:49,684 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 13:14:49,684 INFO     29 [Trace] task=2031b7c0 | doc=LYBI-艾特美哮喘(1).pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "3 items, types={'OutpatientRecord': 1, 'ExaminationReport': 2}", "name": "LYBI-艾特美哮喘(1).pdf"}
2026-08-10 13:14:49,684 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 13:14:49,742 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786367544129, 'update_date': datetime.datetime(2026, 8, 10, 13, 12, 24), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1028840, 'status': '1'}
2026-08-10 13:14:49,971 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=新乡市第二人民医院
门（急）诊病历
门诊号：
姓名
性别
男性
年龄
35岁
婚姻
已婚
职业
工人
籍贯
河南省新乡市
临时住址
河南省新乡市卫滨区
永久住址或工作单位
联系人
联系人关系
本人或户主
联系电话
就诊类别
初诊
是否需下转至基层医疗机构
否
建议下转的基层医疗机构/持续性医疗机构
是否流感样病例
否
应检人员类别
就诊科室
呼吸内科门诊
就诊日期
2025-05-28
发病日期
主诉
发作性咳嗽、咳痰、胸闷、气喘2年
现病史
发作性咳嗽、咳痰、胸闷、气喘2年
既往史
无高血压史。
个人史
无吸烟史。
婚育史
已婚
过敏史
无
家族史
体格检查
T 36℃, P
次/分, R
次/分, BP
/
mmHg, BMI
/
,
辅助检查
无
疾病诊断
西医诊断
1、支气管哮喘(支气管哮喘)
治疗意见
检查
建议
接诊医生
签名时间
医疗业务专用章
---
2
肺功能测验结果
新乡市第二人民医院
呼吸科
12323
FVC
PRE
FEV1
PRE
FEV1%
PRE
应诊日期 2025/5/28
病人号码 W
姓名
出生日期 1990/2/5
人种 中国人
吸烟 非吸烟者
患者组
年龄 35
性别 男
高度, cm 170
重量, kg 85
BMI 29.41
包-年
14
12
10
8
6
4
2
0
-2
-4
8
7
6
5
4
3
2
1
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
13
14
15
时间(s)
已预测的
质量控制等级: D 变化性: FEV1=0.08L (2.26%), FVC=0.31L (5.56%)
1 Acceptable trials
评估
轻度的阻塞
WARNING: FEV1/EVC 前 = 39%
前/测验日期 2025/5/28 17:51:59
参数
LLN
预计
Best
%预计
Z-score
前 # 1
前 # 2
前 # 3
POST
%预计
%激发
FVC
L
3.47
4.52
5.89*
130
5.89
5.58
5.10
FEV1
L
2.91
3.77
3.62*
96
3.62
3.50
3.54
FEV1/FVC
%
73.8
84.0
61.5*
73
61.5
62.7
69.4
PEF
L/s
5.34
8.76
5.08*
58
4.54
4.70
5.08
ELA
年
35
40
114
40
44
43
FEF2575
L/s
2.27
4.05
2.37
58
2.37
2.39
2.68
FET
s
6.00
6.73
112
6.73
6.17
6.33
FIVC
L
3.47
4.52
4.56
101
4.56
4.50
4.52
IVC
L
3.47
4.52
EVC
L
3.47
4.52
9.38
207
VC
L
3.47
4.52
9.38
207
FEV1/VC
%
73.8
84.0
38.6
46
38.6
37.3
37.7
IC
L
3.03
4.50
148
MVV
L/min
136.2
99.8
73
*全部曲线之最佳值 - BTPS 1.073 29 ° C (84.2 ° F) - 已预测的 Knudson
结论
支气管舒张试验阳性。
签名
所用仪器
Spirolab III S/N 313469
---
肺功能检验结果
新乡市第二人民医院
呼吸科
12323
FVC
FEV1
FEV1%
PRE
PRE
PRE
应诊日期 2025/5/28
病人号码
年龄 85
姓氏
性别 男
名字
高度, cm 170
出生日期 1990/2/5
重量, kg 85
人种 中国人
BMI 29.41
吸烟 非吸烟者
患者组 包-年
14
12
10
8
6
4
2
0
-2
-4
8
7
6
5
4
3
2
1
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
13
14
15
时间(s)
@已预测的
质量控制等级: D 变化性: FEV1=0.06L (2.63%), FVC=0.45L (10.23%)
1 Acceptable trials
评估
中度的阻塞.
WARNING: FEF2575 前 = 39%预测, FEV1/EVC 前 = 45%
前/测验日期 2025/5/28 17:15:41
参数 LLN 预计 Best %预计 Z-score 前 #1 前 #2 前 #3 POST %预计 %激发
FVC L 3.47 4.52 4.85* 107 4.85 4.37 4.40 *
FEV1 L 2.91 3.77 2.34* 62 2.13 2.34 2.28 *
FEV1/FVC % 73.8 84.0 48.2* 57 43.9 53.5 51.8 *
PEF L/s 5.34 8.76 2.71* 31 2.71 2.34 2.67 *
ELA 年 35 91 260 91 84 86
FEF2575 L/s 2.27 4.05 1.57 39 1.57 1.80 1.57
FET s 6.00 7.32 122 7.32 5.88 5.68
FIVC L 3.47 4.52 3.86 85 3.86 4.20 4.24
IVC L 3.47 4.52
EVC L 3.47 4.52 5.16 114
VC L 3.47 4.52 5.16 114
FEV1/VC % 73.8 84.0 41.3 49
IC L 3.03 3.58 118
MVV L/min 136.2 42.9 31
*全部曲线之最佳值 - BTPS 1.082 27 °C (80.6 °F) - 已预测的 Knudson
结论
签名
所用仪器
Spirolab III S/N 313469
2026-08-10 13:14:50,242 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 13:14:50,242 INFO     29 [Trace] task=2031b7c0 | doc=LYBI-艾特美哮喘(1).pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "3 items, types={'OutpatientRecord': 1, 'ExaminationReport': 2}", "name": "LYBI-艾特美哮喘(1).pdf", "embedding_token_consumption": 1965}
2026-08-10 13:14:50,242 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 13:14:50,353 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 13:14:50,354 INFO     29 [Trace] task=2031b7c0 | doc=LYBI-艾特美哮喘(1).pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":3,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 13:14:50,357 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:14:50,357 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:14:50,357 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:14:50,360 INFO     29 set_progress(2031b7c094bd11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 13:14:50 [DOC Engine]:
Start to index...
2026-08-10 13:14:50,380 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.015s]
2026-08-10 13:14:50,384 INFO     29 set_progress(2031b7c094bd11f1bd9827cf206dfa2d), progress: 0.8333333333333334, progress_msg: 
2026-08-10 13:14:50,388 INFO     29 set_progress(2031b7c094bd11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 13:14:50 Indexing done (0.03s). Task done (139.24s)
2026-08-10 13:14:50,391 INFO     29 [Done], chunks(3), token(1965), elapsed:139.24
2026-08-10 13:14:50,473 INFO     29 handle_task done for task {"id": "2031b7c094bd11f1bd9827cf206dfa2d", "doc_id": "1ff3926094bd11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LYBI-\u827e\u7279\u7f8e\u54ee\u5598(1).pdf", "type": "pdf", "location": "LYBI-\u827e\u7279\u7f8e\u54ee\u5598(1).pdf", "size": 2220448, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786367543508, "task_type": "dataflow", "root_trace_id": "e8588e7f2a8f4f7ea72bfd924542e9bc", "root_traceparent": "00-e8588e7f2a8f4f7ea72bfd924542e9bc-f1b6b538ed925a47-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
