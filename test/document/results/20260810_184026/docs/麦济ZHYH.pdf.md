# 基准结果：麦济ZHYH.pdf

## 基本信息

- 文件：`麦济ZHYH.pdf`
- 大小：10282.5 KB
- PDF 总页数：6
- doc_id：`1f30448e94ba11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T20:50:52  完成时间：2026-08-10T20:53:24  耗时：152.0s
- progress_msg：`12:53:20 Indexing done (0.04s). Task done (140.22s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 578d3eb1 | 1 | 1-1 | 内蒙古医科大学附属医院门诊病历 姓名： 年龄：62岁 诊疗号：001449878 |
| 2 | c8b6bc6d | 1 | 2-2 | 萱堂大药房 单号：2025111853212 日期：25/11/18 时间：13 |
| 3 | 6a3b2944 | 1 | 3-3 | 电子发票(普通发票) 国家税务总局 江苏省税务局 发票号码：2532200000 |
| 4 | 4f57b287 | 2 | 4-5 | 电子发票(普通发票) 国家税务总局 江苏省税务局 发票号码：2532200000 |
| 5 | 6f789f98 | 1 | 5-5 | 报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录: 病历信息 □痕迹 |
| 6 | eb051a8a | 1 | 6-6 | 电子发票(普通发票) 国家税务总局 内蒙古自治区税务局 发票号码：2615200 |

- chunks 总数：6
- 各 chunk 页数合计（含跨页重复）：7
- 页码并集：`[1, 2, 3, 4, 5, 6]`
- 覆盖页数：6 / 6；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 2 | 0 | 2 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 4 | 4 | 4 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 0 | 1 | 0 | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 2, "MedicationRecord": 4}`
- ChunkMerger：`{"found": true, "merged": 6, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 2, "Extractor:Medication": 4, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 7}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 12:53:20,118 INFO     29 [ChunkMerger] Merged 6 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 4, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 12:50:53,723 INFO     29 handle_task begin for task {"id": "1f69c42a94ba11f1bd9827cf206dfa2d", "doc_id": "1f30448e94ba11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHYH.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHYH.pdf", "size": 10529265, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786366253712, "task_type": "dataflow", "root_trace_id": "ccbe99209a7f4a07832eb1586b73139c", "root_traceparent": "00-ccbe99209a7f4a07832eb1586b73139c-b8274641f81bf5ac-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 12:50:53,928 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 12:50:54,036 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 12:50:54,050 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:50:54,050 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 12:50:54,050 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 12:50:54,062 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 12:50:54,062 INFO     29 ============================================================
2026-08-10 12:50:54,062 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 12:50:54,062 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 12:50:54,062 INFO     29 ============================================================
2026-08-10 12:50:54,062 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 12:50:54,062 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 12:50:54,065 INFO     29 No torch found.
2026-08-10 12:50:55,024 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=6
2026-08-10 12:50:55,417 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1836114, prompt_len=764
2026-08-10 12:50:56,983 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2020-02-13"}
```
2026-08-10 12:50:56,984 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2020-02-13
2026-08-10 12:50:56,994 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1836114, prompt_len=401
2026-08-10 12:50:59,796 INFO     29 [qwen-vl-parser] text API response (len=479):
["内蒙古医科大学附属医院门诊病历", "姓名：", "年龄：62岁", "诊疗号：0014498780", "民族：", "性别：男性", "呼吸内科门诊", "联系电话：", "1", "身份证：", "病情：", "就诊状态：", "就诊时间：2026-02-13 09:14", "生命体征（需要时）：", "体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg", "主诉：哮喘史，近3天呼吸困难加重，夜间咳嗽明显", "现病史：哮喘史，近3天呼吸困难加重，夜间咳嗽明显", "既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "无，吸烟史无，无过敏史。", "体格检查：发育正常，营养良好，体型正常，双肺呼吸音清，双肺未闻及啰", "音，双下肢无水肿，体重kg。", "辅助检查：心肺", "过敏史：不详", "初步诊断（西医）：1.支气管哮喘(急性发作期)", "初步诊断（中医）：", "治疗方案：随诊", "醋酸泼尼松片<5mg>", "用量：3.000片/次", "用法：口服，一次/日，5天", "签名："]
2026-08-10 12:50:59,797 INFO     29 [qwen-vl-parser] page=1 text: 30 lines (bbox 0-29)
2026-08-10 12:50:59,797 INFO     29 [qwen-vl-parser] page=1 text: 30 sections
2026-08-10 12:51:00,080 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1481445, prompt_len=764
2026-08-10 12:51:02,750 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:51:02,750 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 12:51:02,759 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1481445, prompt_len=401
2026-08-10 12:51:04,542 INFO     29 [qwen-vl-parser] text API response (len=259):
["萱堂大药房", "单号：2025111853212", "日期：25/11/18", "时间：13:2", "工号：001", "品名", "规格", "厂家", "金额", "数量", "总计", "布地格福吸入气雾剂", "60ug/7.2ug/4.8ug 吸", "120 撤/支", "支/盒", "219.00", "3", "657.00", "合计：657.00", "应收：657.00", "数量：3", "实收：657.00", "会员：", "药品属于特殊商品", "无质量问题，概不退换"]
2026-08-10 12:51:04,542 INFO     29 [qwen-vl-parser] page=2 text: 25 lines (bbox 30-54)
2026-08-10 12:51:04,542 INFO     29 [qwen-vl-parser] page=2 text: 25 sections
2026-08-10 12:51:04,669 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=778524, prompt_len=764
2026-08-10 12:51:06,038 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:51:06,038 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 12:51:06,052 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=778524, prompt_len=401
2026-08-10 12:51:07,228 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:51:07.227+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 34, "failed": 0, "current": {"1f69c42a94ba11f1bd9827cf206dfa2d": {"id": "1f69c42a94ba11f1bd9827cf206dfa2d", "doc_id": "1f30448e94ba11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHYH.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHYH.pdf", "size": 10529265, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786366253712, "task_type": "dataflow", "root_trace_id": "ccbe99209a7f4a07832eb1586b73139c", "root_traceparent": "00-ccbe99209a7f4a07832eb1586b73139c-b8274641f81bf5ac-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:51:08,612 INFO     29 [qwen-vl-parser] text API response (len=463):
["电子发票(普通发票)", "国家税务总局", "江苏省税务局", "发票号码：25322000000382591347", "开票日期：2025年08月20日", "购买方信息", "名称：", "统一社会信用代码/纳税人识别号：", "销售方信息", "名称：无锡邻医大药房有限公司", "统一社会信用代码/纳税人识别号：91320214MA228F680W", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*倍择瑞令", "160μg/7.2μg/4", "盒", "3", "210.029498522124", "630.09", "13%", "81.91", "畅布地格福吸入气雾剂", ".8μg*120揿", "", "", "", "", "", "", "合计", "￥630.09", "￥81.91", "价税合计（大写）", "柒佰壹拾贰圆整", "(小写) ￥712.00", "备注", "开票人：奚澳琼"]
2026-08-10 12:51:08,612 INFO     29 [qwen-vl-parser] page=3 text: 37 lines (bbox 55-91)
2026-08-10 12:51:08,612 INFO     29 [qwen-vl-parser] page=3 text: 37 sections
2026-08-10 12:51:08,735 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=730743, prompt_len=764
2026-08-10 12:51:10,080 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:51:10,080 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 12:51:10,090 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=730743, prompt_len=401
2026-08-10 12:51:12,528 INFO     29 [qwen-vl-parser] text API response (len=423):
["电子发票(普通发票)", "国家税务总局", "江苏省税务局", "发票号码：25322000000226700883", "开票日期：2025年05月20日", "购买方信息", "名称", "统一社会信用代码/纳税人识别号：", "销售方信息", "名称：无锡邻医大药房有限公司", "统一社会信用代码/纳税人识别号：91320214MA228F680W", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*倍择瑞令", "160μg/7.2μg/4", "盒", "3 210.029498522124", "630.09", "13%", "81.91", "畅布地格福吸入气雾剂", ".8μg*120揿", "合计", "￥630.09", "￥81.91", "价税合计（大写）", "柒佰壹拾贰圆整", "(小写）￥712.00", "备注"]
2026-08-10 12:51:12,529 INFO     29 [qwen-vl-parser] page=4 text: 35 lines (bbox 92-126)
2026-08-10 12:51:12,529 INFO     29 [qwen-vl-parser] page=4 text: 35 sections
2026-08-10 12:51:13,191 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5637139, prompt_len=764
2026-08-10 12:51:14,727 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-12-10"}
```
2026-08-10 12:51:14,730 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=2024-12-10
2026-08-10 12:51:14,760 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5637139, prompt_len=401
2026-08-10 12:51:18,214 INFO     29 [qwen-vl-parser] text API response (len=557):
["挂号号:D20091... 医保余额:0 CM/KG 普通病人|现住址:内蒙古土默特左旗沙尔营乡大有庄村32", "报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录:", "病历信息 □痕迹 □批注 置未 ▼ 状态:只读-仅供查看 120% >", "内蒙古医科大学附属医院门诊病历", "姓名 龄:60岁 诊疗号:0014498780", "民族: 别:男性 科室:呼吸内科门诊", "联系电话: 身份证:1 病情:", "就诊状态: 就诊时间:2024-12-10 12:37", "生命体征(需要时):", "体温:℃ 脉搏:次/分 呼吸:次/分 血压:/mmHg", "主诉:SSSJ项目肺功能检查开单", "现病史:哮喘", "既往史:患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎", "无,吸烟史无,无过敏史。", "体格检查:发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰", "音,双下肢无水肿,体重kg。", "辅助检查:", "初步诊断(西医):1.哮喘", "初步诊断(中医):", "治疗方案:/", "呼吸过滤器 肺通气功能检查", "用量:", "用法:", "签名:崔丽英", "3:34 星期二 190.1.48.233 版本 王立红"]
2026-08-10 12:51:18,217 INFO     29 [qwen-vl-parser] page=5 text: 25 lines (bbox 127-151)
2026-08-10 12:51:18,217 INFO     29 [qwen-vl-parser] page=5 text: 25 sections
2026-08-10 12:51:18,343 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=809094, prompt_len=764
2026-08-10 12:51:19,730 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:51:19,731 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-10 12:51:19,737 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=809094, prompt_len=401
2026-08-10 12:51:22,914 INFO     29 [qwen-vl-parser] text API response (len=612):
["电子发票(普通发票)", "国家税务总局", "内蒙古自治区税务局", "发票号码：26152000000119478346", "开票日期：2026年02月09日", "购买方信息", "名称", "统一社会信用代码/纳税人识别号：", "销售方信息", "名称：国药控股国大药房内蒙古有限公司", "统一社会信用代码/纳税人识别号：911501005732872139", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*布地格福", "160ug:7.2ug/4.8u", "盒", "3", "237.16814159292", "711.50", "13%", "92.50", "吸入气雾剂", "g:120揿", "", "", "", "", "", "", "", "*化学药品制剂*布地格福", "160ug:7.2ug/4.8u", "盒", "3", "237.16814159292", "711.50", "13%", "92.50", "吸入气雾剂", "g:120揿", "", "", "", "", "", "", "", "", "合计", "￥1423.00", "￥185.00", "价税合计（大写）", "壹仟陆佰零捌圆整", "(小写) ￥1608.00", "备注", "开票人：刘惠"]
2026-08-10 12:51:22,916 INFO     29 [qwen-vl-parser] page=6 text: 47 lines (bbox 152-198)
2026-08-10 12:51:22,916 INFO     29 [qwen-vl-parser] page=6 text: 47 sections
2026-08-10 12:51:22,916 INFO     29 [qwen-vl-parser] parse_pdf done: 199 sections from 6 pages.
2026-08-10 12:51:22,928 INFO     29 Close text detector.
2026-08-10 12:51:23,373 INFO     29 Close text recognizer.
2026-08-10 12:51:23,783 INFO     29 Close recognizer.
2026-08-10 12:51:24,152 INFO     29 Close recognizer.
2026-08-10 12:51:24,749 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 12:51:24,749 INFO     29 [Trace] task=1f69c42a | doc=麦济ZHYH.pdf | Parser:MedLink | outputs={"html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "json"}
2026-08-10 12:51:24,749 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 12:51:24,769 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:51:24,769 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 内蒙古医科大学附属医院门诊病历\n[BBOX-1] 姓名：\n[BBOX-2] 年龄：62岁\n[BBOX-3] 诊疗号：0014498780\n[BBOX-4] 民族：\n[BBOX-5] 性别：男性\n[BBOX-6] 呼吸内科门诊\n[BBOX-7] 联系电话：\n[BBOX-8] 1\n[BBOX-9] 身份证：\n[BBOX-10] 病情：\n[BBOX-11] 就诊状态：\n[BBOX-12] 就诊时间：2026-02-13 09:14\n[BBOX-13] 生命体征（需要时）：\n[BBOX-14] 体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg\n[BBOX-15] 主诉：哮喘史，近3天呼吸困难加重，夜间咳嗽明显\n[BBOX-16] 现病史：哮喘史，近3天呼吸困难加重，夜间咳嗽明显\n[BBOX-17] 既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎\n[BBOX-18] 无，吸烟史无，无过敏史。\n[BBOX-19] 体格检查：发育正常，营养良好，体型正常，双肺呼吸音清，双肺未闻及啰\n[BBOX-20] 音，双下肢无水肿，体重kg。\n[BBOX-21] 辅助检查：心肺\n[BBOX-22] 过敏史：不详\n[BBOX-23] 初步诊断（西医）：1.支气管哮喘(急性发作期)\n[BBOX-24] 初步诊断（中医）：\n[BBOX-25] 治疗方案：随诊\n[BBOX-26] 醋酸泼尼松片<5mg>\n[BBOX-27] 用量：3.000片/次\n[BBOX-28] 用法：口服，一次/日，5天\n[BBOX-29] 签名：\n[BBOX-30] 萱堂大药房\n[BBOX-31] 单号：2025111853212\n[BBOX-32] 日期：25/11/18\n[BBOX-33] 时间：13:2\n[BBOX-34] 工号：001\n[BBOX-35] 品名\n[BBOX-36] 规格\n[BBOX-37] 厂家\n[BBOX-38] 金额\n[BBOX-39] 数量\n[BBOX-40] 总计\n[BBOX-41] 布地格福吸入气雾剂\n[BBOX-42] 60ug/7.2ug/4.8ug 吸\n[BBOX-43] 120 撤/支\n[BBOX-44] 支/盒\n[BBOX-45] 219.00\n[BBOX-46] 3\n[BBOX-47] 657.00\n[BBOX-48] 合计：657.00\n[BBOX-49] 应收：657.00\n[BBOX-50] 数量：3\n[BBOX-51] 实收：657.00\n[BBOX-52] 会员：\n[BBOX-53] 药品属于特殊商品\n[BBOX-54] 无质量问题，概不退换\n[BBOX-55] 电子发票(普通发票)\n[BBOX-56] 国家税务总局\n[BBOX-57] 江苏省税务局\n[BBOX-58] 发票号码：25322000000382591347\n[BBOX-59] 开票日期：2025年08月20日\n[BBOX-60] 购买方信息\n[BBOX-61] 名称：\n[BBOX-62] 统一社会信用代码/纳税人识别号：\n[BBOX-63] 销售方信息\n[BBOX-64] 名称：无锡邻医大药房有限公司\n[BBOX-65] 统一社会信用代码/纳税人识别号：91320214MA228F680W\n[BBOX-66] 项目名称\n[BBOX-67] 规格型号\n[BBOX-68] 单位\n[BBOX-69] 数量\n[BBOX-70] 单价\n[BBOX-71] 金额\n[BBOX-72] 税率/征收率\n[BBOX-73] 税额\n[BBOX-74] *化学药品制剂*倍择瑞令\n[BBOX-75] 160μg/7.2μg/4\n[BBOX-76] 盒\n[BBOX-77] 3\n[BBOX-78] 210.029498522124\n[BBOX-79] 630.09\n[BBOX-80] 13%\n[BBOX-81] 81.91\n[BBOX-82] 畅布地格福吸入气雾剂\n[BBOX-83] .8μg*120揿\n[BBOX-84] 合计\n[BBOX-85] ￥630.09\n[BBOX-86] ￥81.91\n[BBOX-87] 价税合计（大写）\n[BBOX-88] 柒佰壹拾贰圆整\n[BBOX-89] (小写) ￥712.00\n[BBOX-90] 备注\n[BBOX-91] 开票人：奚澳琼\n[BBOX-92] 电子发票(普通发票)\n[BBOX-93] 国家税务总局\n[BBOX-94] 江苏省税务局\n[BBOX-95] 发票号码：25322000000226700883\n[BBOX-96] 开票日期：2025年05月20日\n[BBOX-97] 购买方信息\n[BBOX-98] 名称\n[BBOX-99] 统一社会信用代码/纳税人识别号：\n[BBOX-100] 销售方信息\n[BBOX-101] 名称：无锡邻医大药房有限公司\n[BBOX-102] 统一社会信用代码/纳税人识别号：91320214MA228F680W\n[BBOX-103] 项目名称\n[BBOX-104] 规格型号\n[BBOX-105] 单位\n[BBOX-106] 数量\n[BBOX-107] 单价\n[BBOX-108] 金额\n[BBOX-109] 税率/征收率\n[BBOX-110] 税额\n[BBOX-111] *化学药品制剂*倍择瑞令\n[BBOX-112] 160μg/7.2μg/4\n[BBOX-113] 盒\n[BBOX-114] 3 210.029498522124\n[BBOX-115] 630.09\n[BBOX-116] 13%\n[BBOX-117] 81.91\n[BBOX-118] 畅布地格福吸入气雾剂\n[BBOX-119] .8μg*120揿\n[BBOX-120] 合计\n[BBOX-121] ￥630.09\n[BBOX-122] ￥81.91\n[BBOX-123] 价税合计（大写）\n[BBOX-124] 柒佰壹拾贰圆整\n[BBOX-125] (小写）￥712.00\n[BBOX-126] 备注\n[BBOX-127] 挂号号:D20091... 医保余额:0 CM/KG 普通病人|现住址:内蒙古土默特左旗沙尔营乡大有庄村32\n[BBOX-128] 报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录:\n[BBOX-129] 病历信息 □痕迹 □批注 置未 ▼ 状态:只读-仅供查看 120% >\n[BBOX-130] 内蒙古医科大学附属医院门诊病历\n[BBOX-131] 姓名 龄:60岁 诊疗号:0014498780\n[BBOX-132] 民族: 别:男性 科室:呼吸内科门诊\n[BBOX-133] 联系电话: 身份证:1 病情:\n[BBOX-134] 就诊状态: 就诊时间:2024-12-10 12:37\n[BBOX-135] 生命体征(需要时):\n[BBOX-136] 体温:℃ 脉搏:次/分 呼吸:次/分 血压:/mmHg\n[BBOX-137] 主诉:SSSJ项目肺功能检查开单\n[BBOX-138] 现病史:哮喘\n[BBOX-139] 既往史:患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎\n[BBOX-140] 无,吸烟史无,无过敏史。\n[BBOX-141] 体格检查:发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰\n[BBOX-142] 音,双下肢无水肿,体重kg。\n[BBOX-143] 辅助检查:\n[BBOX-144] 初步诊断(西医):1.哮喘\n[BBOX-145] 初步诊断(中医):\n[BBOX-146] 治疗方案:/\n[BBOX-147] 呼吸过滤器 肺通气功能检查\n[BBOX-148] 用量:\n[BBOX-149] 用法:\n[BBOX-150] 签名:崔丽英\n[BBOX-151] 3:34 星期二 190.1.48.233 版本 王立红\n[BBOX-152] 电子发票(普通发票)\n[BBOX-153] 国家税务总局\n[BBOX-154] 内蒙古自治区税务局\n[BBOX-155] 发票号码：26152000000119478346\n[BBOX-156] 开票日期：2026年02月09日\n[BBOX-157] 购买方信息\n[BBOX-158] 名称\n[BBOX-159] 统一社会信用代码/纳税人识别号：\n[BBOX-160] 销售方信息\n[BBOX-161] 名称：国药控股国大药房内蒙古有限公司\n[BBOX-162] 统一社会信用代码/纳税人识别号：911501005732872139\n[BBOX-163] 项目名称\n[BBOX-164] 规格型号\n[BBOX-165] 单位\n[BBOX-166] 数量\n[BBOX-167] 单价\n[BBOX-168] 金额\n[BBOX-169] 税率/征收率\n[BBOX-170] 税额\n[BBOX-171] *化学药品制剂*布地格福\n[BBOX-172] 160ug:7.2ug/4.8u\n[BBOX-173] 盒\n[BBOX-174] 3\n[BBOX-175] 237.16814159292\n[BBOX-176] 711.50\n[BBOX-177] 13%\n[BBOX-178] 92.50\n[BBOX-179] 吸入气雾剂\n[BBOX-180] g:120揿\n[BBOX-181] *化学药品制剂*布地格福\n[BBOX-182] 160ug:7.2ug/4.8u\n[BBOX-183] 盒\n[BBOX-184] 3\n[BBOX-185] 237.16814159292\n[BBOX-186] 711.50\n[BBOX-187] 13%\n[BBOX-188] 92.50\n[BBOX-189] 吸入气雾剂\n[BBOX-190] g:120揿\n[BBOX-191] 合计\n[BBOX-192] ￥1423.00\n[BBOX-193] ￥185.00\n[BBOX-194] 价税合计（大写）\n[BBOX-195] 壹仟陆佰零捌圆整\n[BBOX-196] (小写) ￥1608.00\n[BBOX-197] 备注\n[BBOX-198] 开票人：刘惠"
  }
]
2026-08-10 12:51:30,623 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:51:30,645 INFO     29 [SmartSplitter] SmartSplitter done: 6 chunks from 6 LLM segments (all bbox_id). Types: {'OutpatientRecord': 2, 'MedicationRecord': 4}
2026-08-10 12:51:30,654 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 12:51:30,654 INFO     29 [Trace] task=1f69c42a | doc=麦济ZHYH.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 2, 'MedicationRecord': 4}"}
2026-08-10 12:51:30,654 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 12:51:30,655 INFO     29 [ChunkRouter] Routed 6 chunks into 2 groups: {'chunks_Clinical': 2, 'chunks_Medication': 4}
2026-08-10 12:51:30,662 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 12:51:30,662 INFO     29 [Trace] task=1f69c42a | doc=麦济ZHYH.pdf | ChunkRouter:Router | outputs={"html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 2, 'MedicationRecord': 4}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-10 12:51:30,662 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 12:51:30,666 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:51:30,666 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:51:31,257 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:51:31,271 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 12:51:31,271 INFO     29 [Trace] task=1f69c42a | doc=麦济ZHYH.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-10 12:51:31,271 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 12:51:31,280 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:51:31,280 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:51:31,721 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:51:31,726 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 12:51:31,727 INFO     29 [Trace] task=1f69c42a | doc=麦济ZHYH.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-10 12:51:31,727 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 12:51:31,731 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:51:31,732 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:51:31,732 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 12:51:31,732 INFO     29 [qwen-vl-text] positions(30): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:51:31,732 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [30]
2026-08-10 12:51:32,168 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:51:32,169 INFO     29 [qwen-vl-text] LLM extraction start, text_len=388
2026-08-10 12:51:32,169 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:51:32,169 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 29, \"encounter_dates\": [\"2026-02-13\"], \"department\": \"呼吸内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "内蒙古医科大学附属医院门诊病历\n姓名：\n年龄：62岁\n诊疗号：0014498780\n民族：\n性别：男性\n呼吸内科门诊\n联系电话：\n1\n身份证：\n病情：\n就诊状态：\n就诊时间：2026-02-13 09:14\n生命体征（需要时）：\n体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg\n主诉：哮喘史，近3天呼吸困难加重，夜间咳嗽明显\n现病史：哮喘史，近3天呼吸困难加重，夜间咳嗽明显\n既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎\n无，吸烟史无，无过敏史。\n体格检查：发育正常，营养良好，体型正常，双肺呼吸音清，双肺未闻及啰\n音，双下肢无水肿，体重kg。\n辅助检查：心肺\n过敏史：不详\n初步诊断（西医）：1.支气管哮喘(急性发作期)\n初步诊断（中医）：\n治疗方案：随诊\n醋酸泼尼松片<5mg>\n用量：3.000片/次\n用法：口服，一次/日，5天\n签名：",
    "role": "user"
  }
]
2026-08-10 12:51:35,399 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:51:35,399 INFO     29 [qwen-vl-text] LLM output (len=294):
{
  "encounter_date": "2026-02-13",
  "chief_complaint": "哮喘史，近3天呼吸困难加重，夜间咳嗽明显",
  "present_illness": "哮喘史，近3天呼吸困难加重，夜间咳嗽明显",
  "past_history": "患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎无，吸烟史无，无过敏史。",
  "diagnosis": "西医：1.支气管哮喘(急性发作期)",
  "treatment_plan": "随诊\n醋酸泼尼松片<5mg>\n用量：3.000片/次\n用法：口服，一次/日，5天"
}
2026-08-10 12:51:35,399 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-13]
2026-08-10 12:51:35,407 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2155471, prompt_len=1091
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共30行）
["内蒙古医科大学附属医院门诊病历", "姓名：", "年龄：62岁", "诊疗号：0014498780", "民族：", "性别：男性", "呼吸内科门诊", "联系电话：", "1", "身份证：", "病情：", "就诊状态：", "就诊时间：2026-02-13 09:14", "生命体征（需要时）：", "体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg", "主诉：哮喘史，近3天呼吸困难加重，夜间咳嗽明显", "现病史：哮喘史，近3天呼吸困难加重，夜间咳嗽明显", "既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "无，吸烟史无，无过敏史。", "体格检查：发育正常，营养良好，体型正常，双肺呼吸音清，双肺未闻及啰", "音，双下肢无水肿，体重kg。", "辅助检查：心肺", "过敏史：不详", "初步诊断（西医）：1.支气管哮喘(急性发作期)", "初步诊断（中医）：", "治疗方案：随诊", "醋酸泼尼松片<5mg>", "用量：3.000片/次", "用法：口服，一次/日，5天", "签名："]

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
2026-08-10 12:51:44,820 INFO     29 [qwen-vl-text] coord API raw response (len=1710):
[
	{"text": "内蒙古医科大学附属医院门诊病历", "bbox": [288, 87, 807, 114]},
	{"text": "姓名：", "bbox": [119, 118, 175, 136]},
	{"text": "年龄：62岁", "bbox": [377, 118, 505, 137]},
	{"text": "诊疗号：0014498780", "bbox": [628, 120, 847, 139]},
	{"text": "民族：", "bbox": [119, 141, 175, 158]},
	{"text": "性别：男性", "bbox": [375, 141, 503, 158]},
	{"text": "呼吸内科门诊", "bbox": [707, 143, 850, 161]},
	{"text": "联系电话：", "bbox": [117, 164, 226, 181]},
	{"text": "1", "bbox": [375, 164, 390, 180]},
	{"text": "身份证：", "bbox": [422, 164, 504, 181]},
	{"text": "病情：", "bbox": [791, 167, 849, 184]},
	{"text": "就诊状态：", "bbox": [116, 186, 225, 203]},
	{"text": "就诊时间：2026-02-13 09:14", "bbox": [359, 186, 693, 203]},
	{"text": "生命体征（需要时）：", "bbox": [117, 209, 351, 227]},
	{"text": "体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg", "bbox": [115, 233, 613, 251]},
	{"text": "主诉：哮喘史，近3天呼吸困难加重，夜间咳嗽明显", "bbox": [113, 256, 714, 275]},
	{"text": "现病史：哮喘史，近3天呼吸困难加重，夜间咳嗽明显", "bbox": [113, 280, 714, 298]},
	{"text": "既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "bbox": [112, 304, 965, 323]},
	{"text": "无，吸烟史无，无过敏史。", "bbox": [220, 328, 505, 346]},
	{"text": "体格检查：发育正常，营养良好，体型正常，双肺呼吸音清，双肺未闻及啰", "bbox": [112, 352, 935, 370]},
	{"text": "音，双下肢无水肿，体重kg。", "bbox": [245, 375, 560, 394]},
	{"text": "辅助检查：心肺", "bbox": [110, 401, 304, 419]},
	{"text": "过敏史：不详", "bbox": [111, 425, 292, 443]},
	{"text": "初步诊断（西医）：1.支气管哮喘(急性发作期)", "bbox": [111, 448, 631, 467]},
	{"text": "初步诊断（中医）：", "bbox": [111, 472, 319, 490]},
	{"text": "治疗方案：随诊", "bbox": [111, 495, 292, 513]},
	{"text": "醋酸泼尼松片<5mg>", "bbox": [109, 554, 315, 572]},
	{"text": "用量：3.000片/次", "bbox": [605, 552, 804, 571]},
	{"text": "用法：口服，一次/日，5天", "bbox": [148, 578, 443, 597]},
	{"text": "签名：", "bbox": [575, 675, 634, 693]}
]
2026-08-10 12:51:44,820 INFO     29 [qwen-vl-text] coord API: raw_items=30, valid_items=30, elapsed=9.4s
2026-08-10 12:51:44,821 INFO     29 [qwen-vl-text] coord item[0]: text=内蒙古医科大学附属医院门诊病历, bbox=[288, 87, 807, 114]
2026-08-10 12:51:44,821 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[119, 118, 175, 136]
2026-08-10 12:51:44,821 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：62岁, bbox=[377, 118, 505, 137]
2026-08-10 12:51:44,821 INFO     29 [qwen-vl-text] coord item[3]: text=诊疗号：0014498780, bbox=[628, 120, 847, 139]
2026-08-10 12:51:44,821 INFO     29 [qwen-vl-text] coord item[4]: text=民族：, bbox=[119, 141, 175, 158]
2026-08-10 12:51:44,821 INFO     29 [qwen-vl-text] coord item[5]: text=性别：男性, bbox=[375, 141, 503, 158]
2026-08-10 12:51:44,821 INFO     29 [qwen-vl-text] coord item[6]: text=呼吸内科门诊, bbox=[707, 143, 850, 161]
2026-08-10 12:51:44,821 INFO     29 [qwen-vl-text] coord item[7]: text=联系电话：, bbox=[117, 164, 226, 181]
2026-08-10 12:51:44,821 INFO     29 [qwen-vl-text] coord item[8]: text=1, bbox=[375, 164, 390, 180]
2026-08-10 12:51:44,821 INFO     29 [qwen-vl-text] coord item[9]: text=身份证：, bbox=[422, 164, 504, 181]
2026-08-10 12:51:44,821 INFO     29 [qwen-vl-text] coord item[10]: text=病情：, bbox=[791, 167, 849, 184]
2026-08-10 12:51:44,821 INFO     29 [qwen-vl-text] coord item[11]: text=就诊状态：, bbox=[116, 186, 225, 203]
2026-08-10 12:51:44,821 INFO     29 [qwen-vl-text] coord item[12]: text=就诊时间：2026-02-13 09:14, bbox=[359, 186, 693, 203]
2026-08-10 12:51:44,821 INFO     29 [qwen-vl-text] coord item[13]: text=生命体征（需要时）：, bbox=[117, 209, 351, 227]
2026-08-10 12:51:44,821 INFO     29 [qwen-vl-text] coord item[14]: text=体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg, bbox=[115, 233, 613, 251]
2026-08-10 12:51:44,821 INFO     29 [qwen-vl-text] coord item[15]: text=主诉：哮喘史，近3天呼吸困难加重，夜间咳嗽明显, bbox=[113, 256, 714, 275]
2026-08-10 12:51:44,822 INFO     29 [qwen-vl-text] coord item[16]: text=现病史：哮喘史，近3天呼吸困难加重，夜间咳嗽明显, bbox=[113, 280, 714, 298]
2026-08-10 12:51:44,822 INFO     29 [qwen-vl-text] coord item[17]: text=既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎, bbox=[112, 304, 965, 323]
2026-08-10 12:51:44,822 INFO     29 [qwen-vl-text] coord item[18]: text=无，吸烟史无，无过敏史。, bbox=[220, 328, 505, 346]
2026-08-10 12:51:44,822 INFO     29 [qwen-vl-text] coord item[19]: text=体格检查：发育正常，营养良好，体型正常，双肺呼吸音清，双肺未闻及啰, bbox=[112, 352, 935, 370]
2026-08-10 12:51:44,822 INFO     29 [qwen-vl-text] coord item[20]: text=音，双下肢无水肿，体重kg。, bbox=[245, 375, 560, 394]
2026-08-10 12:51:44,822 INFO     29 [qwen-vl-text] coord item[21]: text=辅助检查：心肺, bbox=[110, 401, 304, 419]
2026-08-10 12:51:44,822 INFO     29 [qwen-vl-text] coord item[22]: text=过敏史：不详, bbox=[111, 425, 292, 443]
2026-08-10 12:51:44,822 INFO     29 [qwen-vl-text] coord item[23]: text=初步诊断（西医）：1.支气管哮喘(急性发作期), bbox=[111, 448, 631, 467]
2026-08-10 12:51:44,822 INFO     29 [qwen-vl-text] coord item[24]: text=初步诊断（中医）：, bbox=[111, 472, 319, 490]
2026-08-10 12:51:44,822 INFO     29 [qwen-vl-text] coord item[25]: text=治疗方案：随诊, bbox=[111, 495, 292, 513]
2026-08-10 12:51:44,822 INFO     29 [qwen-vl-text] coord item[26]: text=醋酸泼尼松片<5mg>, bbox=[109, 554, 315, 572]
2026-08-10 12:51:44,822 INFO     29 [qwen-vl-text] coord item[27]: text=用量：3.000片/次, bbox=[605, 552, 804, 571]
2026-08-10 12:51:44,822 INFO     29 [qwen-vl-text] coord item[28]: text=用法：口服，一次/日，5天, bbox=[148, 578, 443, 597]
2026-08-10 12:51:44,822 INFO     29 [qwen-vl-text] coord item[29]: text=签名：, bbox=[575, 675, 634, 693]
2026-08-10 12:51:44,823 INFO     29 [qwen-vl-text] page=0 — 30/30 coords, api_time=9.4s
2026-08-10 12:51:44,824 INFO     29 [qwen-vl-text] new_positions (30):
[[0, 171.35999999999999, 480.16499999999996, 73.25399999999999, 95.988], [0, 70.80499999999999, 104.125, 99.356, 114.512], [0, 224.315, 300.47499999999997, 99.356, 115.354], [0, 373.65999999999997, 503.965, 101.03999999999999, 117.038], [0, 70.80499999999999, 104.125, 118.722, 133.036], [0, 223.125, 299.28499999999997, 118.722, 133.036], [0, 420.66499999999996, 505.75, 120.40599999999999, 135.56199999999998], [0, 69.615, 134.47, 138.088, 152.402], [0, 223.125, 232.04999999999998, 138.088, 151.56], [0, 251.08999999999997, 299.88, 138.088, 152.402], [0, 470.645, 505.155, 140.614, 154.928], [0, 69.02, 133.875, 156.612, 170.926], [0, 213.605, 412.335, 156.612, 170.926], [0, 69.615, 208.845, 175.97799999999998, 191.134], [0, 68.425, 364.73499999999996, 196.186, 211.34199999999998], [0, 67.235, 424.83, 215.552, 231.54999999999998], [0, 67.235, 424.83, 235.76, 250.916], [0, 66.64, 574.175, 255.968, 271.966], [0, 130.9, 300.47499999999997, 276.176, 291.332], [0, 66.64, 556.3249999999999, 296.384, 311.53999999999996], [0, 145.775, 333.2, 315.75, 331.748], [0, 65.45, 180.88, 337.642, 352.798], [0, 66.045, 173.73999999999998, 357.84999999999997, 373.006], [0, 66.045, 375.445, 377.216, 393.214], [0, 66.045, 189.80499999999998, 397.424, 412.58], [0, 66.045, 173.73999999999998, 416.78999999999996, 431.94599999999997], [0, 64.855, 187.42499999999998, 466.46799999999996, 481.62399999999997], [0, 359.97499999999997, 478.38, 464.784, 480.782], [0, 88.06, 263.585, 486.676, 502.674], [0, 342.125, 377.22999999999996, 568.35, 583.506]]
2026-08-10 12:51:44,824 INFO     29 [qwen-vl-text] ═══ DONE ═══ 30 positions, pages=1, time=13.1s
2026-08-10 12:51:44,824 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:51:44,834 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:51:44,834 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 12:51:44,834 INFO     29 [qwen-vl-text] positions(24): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:51:44,834 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [24]
2026-08-10 12:51:45,356 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:51:45,358 INFO     29 [qwen-vl-text] LLM extraction start, text_len=426
2026-08-10 12:51:45,358 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:51:45,358 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 128, \"bbox_end\": 151, \"encounter_dates\": [\"2024-12-10\"], \"department\": \"呼吸内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录:\n病历信息 □痕迹 □批注 置未 ▼ 状态:只读-仅供查看 120% >\n内蒙古医科大学附属医院门诊病历\n姓名 龄:60岁 诊疗号:0014498780\n民族: 别:男性 科室:呼吸内科门诊\n联系电话: 身份证:1 病情:\n就诊状态: 就诊时间:2024-12-10 12:37\n生命体征(需要时):\n体温:℃ 脉搏:次/分 呼吸:次/分 血压:/mmHg\n主诉:SSSJ项目肺功能检查开单\n现病史:哮喘\n既往史:患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎\n无,吸烟史无,无过敏史。\n体格检查:发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰\n音,双下肢无水肿,体重kg。\n辅助检查:\n初步诊断(西医):1.哮喘\n初步诊断(中医):\n治疗方案:/\n呼吸过滤器 肺通气功能检查\n用量:\n用法:\n签名:崔丽英\n3:34 星期二 190.1.48.233 版本 王立红",
    "role": "user"
  }
]
2026-08-10 12:51:45,360 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:51:45.360+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 34, "failed": 0, "current": {"1f69c42a94ba11f1bd9827cf206dfa2d": {"id": "1f69c42a94ba11f1bd9827cf206dfa2d", "doc_id": "1f30448e94ba11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHYH.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHYH.pdf", "size": 10529265, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786366253712, "task_type": "dataflow", "root_trace_id": "ccbe99209a7f4a07832eb1586b73139c", "root_traceparent": "00-ccbe99209a7f4a07832eb1586b73139c-b8274641f81bf5ac-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:51:47,165 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:51:47,165 INFO     29 [qwen-vl-text] LLM output (len=215):
{
  "encounter_date": "2024-12-10",
  "chief_complaint": "SSSJ项目肺功能检查开单",
  "present_illness": "哮喘",
  "past_history": "患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎无,吸烟史无,无过敏史。",
  "diagnosis": "1.哮喘",
  "treatment_plan": null
}
2026-08-10 12:51:47,166 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-12-10]
2026-08-10 12:51:47,192 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7824738, prompt_len=1111
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共24行）
["报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录:", "病历信息 □痕迹 □批注 置未 ▼ 状态:只读-仅供查看 120% >", "内蒙古医科大学附属医院门诊病历", "姓名 龄:60岁 诊疗号:0014498780", "民族: 别:男性 科室:呼吸内科门诊", "联系电话: 身份证:1 病情:", "就诊状态: 就诊时间:2024-12-10 12:37", "生命体征(需要时):", "体温:℃ 脉搏:次/分 呼吸:次/分 血压:/mmHg", "主诉:SSSJ项目肺功能检查开单", "现病史:哮喘", "既往史:患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎", "无,吸烟史无,无过敏史。", "体格检查:发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰", "音,双下肢无水肿,体重kg。", "辅助检查:", "初步诊断(西医):1.哮喘", "初步诊断(中医):", "治疗方案:/", "呼吸过滤器 肺通气功能检查", "用量:", "用法:", "签名:崔丽英", "3:34 星期二 190.1.48.233 版本 王立红"]

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
2026-08-10 12:51:56,382 INFO     29 [qwen-vl-text] coord API raw response (len=1465):
[
	{"text": "报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录:", "bbox": [60, 92, 864, 129]},
	{"text": "病历信息 □痕迹 □批注 置未 ▼ 状态:只读-仅供查看 120% >", "bbox": [7, 129, 948, 174]},
	{"text": "内蒙古医科大学附属医院门诊病历", "bbox": [248, 185, 748, 219]},
	{"text": "姓名 龄:60岁 诊疗号:0014498780", "bbox": [93, 225, 780, 256]},
	{"text": "民族: 别:男性 科室:呼吸内科门诊", "bbox": [95, 258, 783, 288]},
	{"text": "联系电话: 身份证:1 病情:", "bbox": [95, 290, 780, 319]},
	{"text": "就诊状态: 就诊时间:2024-12-10 12:37", "bbox": [95, 323, 634, 348]},
	{"text": "生命体征(需要时):", "bbox": [97, 349, 318, 369]},
	{"text": "体温:℃ 脉搏:次/分 呼吸:次/分 血压:/mmHg", "bbox": [97, 370, 562, 392]},
	{"text": "主诉:SSSJ项目肺功能检查开单", "bbox": [97, 391, 454, 411]},
	{"text": "现病史:哮喘", "bbox": [97, 411, 244, 431]},
	{"text": "既往史:患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎", "bbox": [97, 433, 884, 457]},
	{"text": "无,吸烟史无,无过敏史。", "bbox": [199, 455, 465, 475]},
	{"text": "体格检查:发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰", "bbox": [97, 475, 857, 498]},
	{"text": "音,双下肢无水肿,体重kg。", "bbox": [224, 497, 511, 516]},
	{"text": "辅助检查:", "bbox": [97, 518, 200, 537]},
	{"text": "初步诊断(西医):1.哮喘", "bbox": [97, 538, 380, 559]},
	{"text": "初步诊断(中医):", "bbox": [97, 559, 298, 579]},
	{"text": "治疗方案:/", "bbox": [97, 580, 214, 600]},
	{"text": "呼吸过滤器 肺通气功能检查", "bbox": [100, 617, 525, 637]},
	{"text": "用量:", "bbox": [571, 637, 622, 654]},
	{"text": "用法:", "bbox": [147, 655, 200, 672]},
	{"text": "签名:崔丽英", "bbox": [537, 743, 658, 761]},
	{"text": "3:34 星期二 190.1.48.233 版本 王立红", "bbox": [3, 797, 974, 817]}
]
2026-08-10 12:51:56,382 INFO     29 [qwen-vl-text] coord API: raw_items=24, valid_items=24, elapsed=9.2s
2026-08-10 12:51:56,382 INFO     29 [qwen-vl-text] coord item[0]: text=报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录:, bbox=[60, 92, 864, 129]
2026-08-10 12:51:56,382 INFO     29 [qwen-vl-text] coord item[1]: text=病历信息 □痕迹 □批注 置未 ▼ 状态:只读-仅供查看 120% >, bbox=[7, 129, 948, 174]
2026-08-10 12:51:56,382 INFO     29 [qwen-vl-text] coord item[2]: text=内蒙古医科大学附属医院门诊病历, bbox=[248, 185, 748, 219]
2026-08-10 12:51:56,382 INFO     29 [qwen-vl-text] coord item[3]: text=姓名 龄:60岁 诊疗号:0014498780, bbox=[93, 225, 780, 256]
2026-08-10 12:51:56,382 INFO     29 [qwen-vl-text] coord item[4]: text=民族: 别:男性 科室:呼吸内科门诊, bbox=[95, 258, 783, 288]
2026-08-10 12:51:56,382 INFO     29 [qwen-vl-text] coord item[5]: text=联系电话: 身份证:1 病情:, bbox=[95, 290, 780, 319]
2026-08-10 12:51:56,382 INFO     29 [qwen-vl-text] coord item[6]: text=就诊状态: 就诊时间:2024-12-10 12:37, bbox=[95, 323, 634, 348]
2026-08-10 12:51:56,382 INFO     29 [qwen-vl-text] coord item[7]: text=生命体征(需要时):, bbox=[97, 349, 318, 369]
2026-08-10 12:51:56,382 INFO     29 [qwen-vl-text] coord item[8]: text=体温:℃ 脉搏:次/分 呼吸:次/分 血压:/mmHg, bbox=[97, 370, 562, 392]
2026-08-10 12:51:56,382 INFO     29 [qwen-vl-text] coord item[9]: text=主诉:SSSJ项目肺功能检查开单, bbox=[97, 391, 454, 411]
2026-08-10 12:51:56,383 INFO     29 [qwen-vl-text] coord item[10]: text=现病史:哮喘, bbox=[97, 411, 244, 431]
2026-08-10 12:51:56,383 INFO     29 [qwen-vl-text] coord item[11]: text=既往史:患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎, bbox=[97, 433, 884, 457]
2026-08-10 12:51:56,383 INFO     29 [qwen-vl-text] coord item[12]: text=无,吸烟史无,无过敏史。, bbox=[199, 455, 465, 475]
2026-08-10 12:51:56,383 INFO     29 [qwen-vl-text] coord item[13]: text=体格检查:发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰, bbox=[97, 475, 857, 498]
2026-08-10 12:51:56,383 INFO     29 [qwen-vl-text] coord item[14]: text=音,双下肢无水肿,体重kg。, bbox=[224, 497, 511, 516]
2026-08-10 12:51:56,383 INFO     29 [qwen-vl-text] coord item[15]: text=辅助检查:, bbox=[97, 518, 200, 537]
2026-08-10 12:51:56,383 INFO     29 [qwen-vl-text] coord item[16]: text=初步诊断(西医):1.哮喘, bbox=[97, 538, 380, 559]
2026-08-10 12:51:56,383 INFO     29 [qwen-vl-text] coord item[17]: text=初步诊断(中医):, bbox=[97, 559, 298, 579]
2026-08-10 12:51:56,383 INFO     29 [qwen-vl-text] coord item[18]: text=治疗方案:/, bbox=[97, 580, 214, 600]
2026-08-10 12:51:56,383 INFO     29 [qwen-vl-text] coord item[19]: text=呼吸过滤器 肺通气功能检查, bbox=[100, 617, 525, 637]
2026-08-10 12:51:56,383 INFO     29 [qwen-vl-text] coord item[20]: text=用量:, bbox=[571, 637, 622, 654]
2026-08-10 12:51:56,383 INFO     29 [qwen-vl-text] coord item[21]: text=用法:, bbox=[147, 655, 200, 672]
2026-08-10 12:51:56,383 INFO     29 [qwen-vl-text] coord item[22]: text=签名:崔丽英, bbox=[537, 743, 658, 761]
2026-08-10 12:51:56,383 INFO     29 [qwen-vl-text] coord item[23]: text=3:34 星期二 190.1.48.233 版本 王立红, bbox=[3, 797, 974, 817]
2026-08-10 12:51:56,386 INFO     29 [qwen-vl-text] page=4 — 24/24 coords, api_time=9.2s
2026-08-10 12:51:56,386 INFO     29 [qwen-vl-text] new_positions (24):
[[4, 35.699999999999996, 514.0799999999999, 77.464, 108.618], [4, 4.165, 564.06, 108.618, 146.50799999999998], [4, 147.56, 445.06, 155.76999999999998, 184.398], [4, 55.335, 464.09999999999997, 189.45, 215.552], [4, 56.525, 465.885, 217.236, 242.49599999999998], [4, 56.525, 464.09999999999997, 244.17999999999998, 268.598], [4, 56.525, 377.22999999999996, 271.966, 293.01599999999996], [4, 57.714999999999996, 189.20999999999998, 293.858, 310.698], [4, 57.714999999999996, 334.39, 311.53999999999996, 330.06399999999996], [4, 57.714999999999996, 270.13, 329.222, 346.062], [4, 57.714999999999996, 145.18, 346.062, 362.902], [4, 57.714999999999996, 525.98, 364.586, 384.794], [4, 118.405, 276.675, 383.11, 399.95], [4, 57.714999999999996, 509.91499999999996, 399.95, 419.316], [4, 133.28, 304.04499999999996, 418.474, 434.472], [4, 57.714999999999996, 119.0, 436.156, 452.154], [4, 57.714999999999996, 226.1, 452.996, 470.678], [4, 57.714999999999996, 177.31, 470.678, 487.518], [4, 57.714999999999996, 127.33, 488.35999999999996, 505.2], [4, 59.5, 312.375, 519.514, 536.3539999999999], [4, 339.745, 370.09, 536.3539999999999, 550.668], [4, 87.46499999999999, 119.0, 551.51, 565.824], [4, 319.515, 391.51, 625.606, 640.762], [4, 1.785, 579.53, 671.074, 687.914]]
2026-08-10 12:51:56,386 INFO     29 [qwen-vl-text] ═══ DONE ═══ 24 positions, pages=1, time=11.6s
2026-08-10 12:51:56,394 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 12:51:56,394 INFO     29 [Trace] task=1f69c42a | doc=麦济ZHYH.pdf | Extractor:Clinical | outputs={"chunks": "2 items, types={'OutpatientRecord': 2}", "html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-10 12:51:56,395 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 12:51:56,399 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:51:56,400 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:51:56,400 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 12:51:56,400 INFO     29 [qwen-vl-text] positions(25): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:51:56,400 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [25]
2026-08-10 12:51:56,669 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:51:56,671 INFO     29 [qwen-vl-text] LLM extraction start, text_len=183
2026-08-10 12:51:56,671 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:51:56,672 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 30, \"bbox_end\": 54, \"encounter_dates\": [\"2025-11-18\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "萱堂大药房\n单号：2025111853212\n日期：25/11/18\n时间：13:2\n工号：001\n品名\n规格\n厂家\n金额\n数量\n总计\n布地格福吸入气雾剂\n60ug/7.2ug/4.8ug 吸\n120 撤/支\n支/盒\n219.00\n3\n657.00\n合计：657.00\n应收：657.00\n数量：3\n实收：657.00\n会员：\n药品属于特殊商品\n无质量问题，概不退换",
    "role": "user"
  }
]
2026-08-10 12:51:58,934 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:51:58,935 INFO     29 [qwen-vl-text] LLM output (len=436):
{
  "encounter_date": "2025-11-18",
  "pharmacy": "萱堂大药房",
  "medications": [
    {
      "name": "布地格福吸入气雾剂",
      "specification": "60ug/7.2ug/4.8ug 吸 120 撤/支 支/盒",
      "dosage": null,
      "quantity": 3,
      "unit_price": 219.00,
      "total_price": 657.00,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 657.00,
  "payment_method": null
}
2026-08-10 12:51:58,935 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-18]
2026-08-10 12:51:58,942 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1978583, prompt_len=871
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["萱堂大药房", "单号：2025111853212", "日期：25/11/18", "时间：13:2", "工号：001", "品名", "规格", "厂家", "金额", "数量", "总计", "布地格福吸入气雾剂", "60ug/7.2ug/4.8ug 吸", "120 撤/支", "支/盒", "219.00", "3", "657.00", "合计：657.00", "应收：657.00", "数量：3", "实收：657.00", "会员：", "药品属于特殊商品", "无质量问题，概不退换"]

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
2026-08-10 12:52:07,911 INFO     29 [qwen-vl-text] coord API raw response (len=1286):
[
	{"text": "萱堂大药房", "bbox": [364, 153, 658, 199]},
	{"text": "单号：2025111853212", "bbox": [212, 248, 614, 288]},
	{"text": "日期：25/11/18", "bbox": [212, 297, 484, 335]},
	{"text": "时间：13:2", "bbox": [570, 305, 807, 338]},
	{"text": "工号：001", "bbox": [212, 348, 400, 382]},
	{"text": "品名", "bbox": [212, 398, 294, 430]},
	{"text": "规格", "bbox": [374, 403, 462, 435]},
	{"text": "厂家", "bbox": [542, 405, 628, 437]},
	{"text": "金额", "bbox": [732, 406, 810, 438]},
	{"text": "数量", "bbox": [212, 447, 292, 479]},
	{"text": "总计", "bbox": [382, 452, 468, 483]},
	{"text": "布地格福吸入气雾剂", "bbox": [212, 490, 810, 530]},
	{"text": "60ug/7.2ug/4.8ug 吸", "bbox": [224, 530, 590, 569]},
	{"text": "120 撤/支", "bbox": [642, 536, 810, 569]},
	{"text": "支/盒", "bbox": [237, 568, 338, 601]},
	{"text": "219.00", "bbox": [214, 609, 327, 637]},
	{"text": "3", "bbox": [414, 612, 437, 638]},
	{"text": "657.00", "bbox": [546, 613, 664, 640]},
	{"text": "合计：657.00", "bbox": [214, 646, 460, 678]},
	{"text": "应收：657.00", "bbox": [214, 684, 460, 715]},
	{"text": "数量：3", "bbox": [214, 724, 361, 757]},
	{"text": "实收：657.00", "bbox": [214, 772, 462, 805]},
	{"text": "会员：", "bbox": [214, 823, 311, 855]},
	{"text": "药品属于特殊商品", "bbox": [217, 871, 555, 904]},
	{"text": "无质量问题，概不退换", "bbox": [219, 920, 642, 953]}
]
2026-08-10 12:52:07,911 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=9.0s
2026-08-10 12:52:07,911 INFO     29 [qwen-vl-text] coord item[0]: text=萱堂大药房, bbox=[364, 153, 658, 199]
2026-08-10 12:52:07,911 INFO     29 [qwen-vl-text] coord item[1]: text=单号：2025111853212, bbox=[212, 248, 614, 288]
2026-08-10 12:52:07,911 INFO     29 [qwen-vl-text] coord item[2]: text=日期：25/11/18, bbox=[212, 297, 484, 335]
2026-08-10 12:52:07,911 INFO     29 [qwen-vl-text] coord item[3]: text=时间：13:2, bbox=[570, 305, 807, 338]
2026-08-10 12:52:07,911 INFO     29 [qwen-vl-text] coord item[4]: text=工号：001, bbox=[212, 348, 400, 382]
2026-08-10 12:52:07,911 INFO     29 [qwen-vl-text] coord item[5]: text=品名, bbox=[212, 398, 294, 430]
2026-08-10 12:52:07,912 INFO     29 [qwen-vl-text] coord item[6]: text=规格, bbox=[374, 403, 462, 435]
2026-08-10 12:52:07,912 INFO     29 [qwen-vl-text] coord item[7]: text=厂家, bbox=[542, 405, 628, 437]
2026-08-10 12:52:07,912 INFO     29 [qwen-vl-text] coord item[8]: text=金额, bbox=[732, 406, 810, 438]
2026-08-10 12:52:07,912 INFO     29 [qwen-vl-text] coord item[9]: text=数量, bbox=[212, 447, 292, 479]
2026-08-10 12:52:07,912 INFO     29 [qwen-vl-text] coord item[10]: text=总计, bbox=[382, 452, 468, 483]
2026-08-10 12:52:07,912 INFO     29 [qwen-vl-text] coord item[11]: text=布地格福吸入气雾剂, bbox=[212, 490, 810, 530]
2026-08-10 12:52:07,912 INFO     29 [qwen-vl-text] coord item[12]: text=60ug/7.2ug/4.8ug 吸, bbox=[224, 530, 590, 569]
2026-08-10 12:52:07,912 INFO     29 [qwen-vl-text] coord item[13]: text=120 撤/支, bbox=[642, 536, 810, 569]
2026-08-10 12:52:07,912 INFO     29 [qwen-vl-text] coord item[14]: text=支/盒, bbox=[237, 568, 338, 601]
2026-08-10 12:52:07,912 INFO     29 [qwen-vl-text] coord item[15]: text=219.00, bbox=[214, 609, 327, 637]
2026-08-10 12:52:07,912 INFO     29 [qwen-vl-text] coord item[16]: text=3, bbox=[414, 612, 437, 638]
2026-08-10 12:52:07,912 INFO     29 [qwen-vl-text] coord item[17]: text=657.00, bbox=[546, 613, 664, 640]
2026-08-10 12:52:07,912 INFO     29 [qwen-vl-text] coord item[18]: text=合计：657.00, bbox=[214, 646, 460, 678]
2026-08-10 12:52:07,912 INFO     29 [qwen-vl-text] coord item[19]: text=应收：657.00, bbox=[214, 684, 460, 715]
2026-08-10 12:52:07,912 INFO     29 [qwen-vl-text] coord item[20]: text=数量：3, bbox=[214, 724, 361, 757]
2026-08-10 12:52:07,912 INFO     29 [qwen-vl-text] coord item[21]: text=实收：657.00, bbox=[214, 772, 462, 805]
2026-08-10 12:52:07,912 INFO     29 [qwen-vl-text] coord item[22]: text=会员：, bbox=[214, 823, 311, 855]
2026-08-10 12:52:07,913 INFO     29 [qwen-vl-text] coord item[23]: text=药品属于特殊商品, bbox=[217, 871, 555, 904]
2026-08-10 12:52:07,913 INFO     29 [qwen-vl-text] coord item[24]: text=无质量问题，概不退换, bbox=[219, 920, 642, 953]
2026-08-10 12:52:07,914 INFO     29 [qwen-vl-text] page=1 — 25/25 coords, api_time=9.0s
2026-08-10 12:52:07,914 INFO     29 [qwen-vl-text] new_positions (25):
[[1, 216.57999999999998, 391.51, 128.826, 167.558], [1, 126.14, 365.33, 208.816, 242.49599999999998], [1, 126.14, 287.97999999999996, 250.07399999999998, 282.07], [1, 339.15, 480.16499999999996, 256.81, 284.596], [1, 126.14, 238.0, 293.01599999999996, 321.644], [1, 126.14, 174.92999999999998, 335.116, 362.06], [1, 222.53, 274.89, 339.32599999999996, 366.27], [1, 322.49, 373.65999999999997, 341.01, 367.954], [1, 435.53999999999996, 481.95, 341.852, 368.796], [1, 126.14, 173.73999999999998, 376.37399999999997, 403.318], [1, 227.29, 278.46, 380.584, 406.686], [1, 126.14, 481.95, 412.58, 446.26], [1, 133.28, 351.05, 446.26, 479.09799999999996], [1, 381.99, 481.95, 451.312, 479.09799999999996], [1, 141.015, 201.10999999999999, 478.256, 506.042], [1, 127.33, 194.565, 512.778, 536.3539999999999], [1, 246.32999999999998, 260.015, 515.304, 537.196], [1, 324.87, 395.08, 516.146, 538.88], [1, 127.33, 273.7, 543.932, 570.876], [1, 127.33, 273.7, 575.928, 602.03], [1, 127.33, 214.795, 609.608, 637.394], [1, 127.33, 274.89, 650.024, 677.81], [1, 127.33, 185.045, 692.966, 719.91], [1, 129.11499999999998, 330.22499999999997, 733.382, 761.168], [1, 130.305, 381.99, 774.64, 802.4259999999999]]
2026-08-10 12:52:07,914 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=11.5s
2026-08-10 12:52:07,914 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:52:07,916 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:52:07,916 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 12:52:07,916 INFO     29 [qwen-vl-text] positions(37): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:52:07,916 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [37]
2026-08-10 12:52:08,101 INFO     29 [qwen-vl-text] page=2, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 12:52:08,102 INFO     29 [qwen-vl-text] LLM extraction start, text_len=327
2026-08-10 12:52:08,102 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:52:08,102 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 55, \"bbox_end\": 91, \"encounter_dates\": [\"2025-08-20\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "电子发票(普通发票)\n国家税务总局\n江苏省税务局\n发票号码：25322000000382591347\n开票日期：2025年08月20日\n购买方信息\n名称：\n统一社会信用代码/纳税人识别号：\n销售方信息\n名称：无锡邻医大药房有限公司\n统一社会信用代码/纳税人识别号：91320214MA228F680W\n项目名称\n规格型号\n单位\n数量\n单价\n金额\n税率/征收率\n税额\n*化学药品制剂*倍择瑞令\n160μg/7.2μg/4\n盒\n3\n210.029498522124\n630.09\n13%\n81.91\n畅布地格福吸入气雾剂\n.8μg*120揿\n合计\n￥630.09\n￥81.91\n价税合计（大写）\n柒佰壹拾贰圆整\n(小写) ￥712.00\n备注\n开票人：奚澳琼",
    "role": "user"
  }
]
2026-08-10 12:52:10,378 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:52:10,378 INFO     29 [qwen-vl-text] LLM output (len=438):
{
  "encounter_date": "2025-08-20",
  "pharmacy": "无锡邻医大药房有限公司",
  "medications": [
    {
      "name": "倍择瑞",
      "specification": "160μg/7.2μg/4.8μg*120揿",
      "dosage": null,
      "quantity": 3,
      "unit_price": 210.029498522124,
      "total_price": 630.09,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 712.00,
  "payment_method": null
}
2026-08-10 12:52:10,378 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-08-20]
2026-08-10 12:52:10,382 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=931127, prompt_len=1051
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共37行）
["电子发票(普通发票)", "国家税务总局", "江苏省税务局", "发票号码：25322000000382591347", "开票日期：2025年08月20日", "购买方信息", "名称：", "统一社会信用代码/纳税人识别号：", "销售方信息", "名称：无锡邻医大药房有限公司", "统一社会信用代码/纳税人识别号：91320214MA228F680W", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*倍择瑞令", "160μg/7.2μg/4", "盒", "3", "210.029498522124", "630.09", "13%", "81.91", "畅布地格福吸入气雾剂", ".8μg*120揿", "合计", "￥630.09", "￥81.91", "价税合计（大写）", "柒佰壹拾贰圆整", "(小写) ￥712.00", "备注", "开票人：奚澳琼"]

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
2026-08-10 12:52:27,860 INFO     29 [qwen-vl-text] coord API raw response (len=3201):
[
	{"text": "电子发票(普通发票)", "bbox": [327, 103, 637, 148]},
	{"text": "国家税务总局", "bbox": [463, 155, 534, 172], "bbox_2d": [463, 155, 534, 172]},
	{"text": "江苏省税务局", "bbox": [463, 187, 537, 210], "bbox_2d": [463, 187, 537, 210]},
	{"text": "发票号码：25322000000382591347", "bbox": [733, 122, 948, 143], "bbox_2d": [733, 122, 948, 143]},
	{"text": "开票日期：2025年08月20日", "bbox": [733, 161, 909, 182], "bbox_2d": [733, 161, 909, 182]},
	{"text": "购买方信息", "bbox": [32, 265, 46, 380], "bbox_2d": [32, 265, 46, 380]},
	{"text": "名称：", "bbox": [59, 282, 92, 302], "bbox_2d": [59, 282, 92, 302]},
	{"text": "统一社会信用代码/纳税人识别号：", "bbox": [58, 346, 258, 366], "bbox_2d": [58, 346, 258, 366]},
	{"text": "销售方信息", "bbox": [507, 265, 521, 380], "bbox_2d": [507, 265, 521, 380]},
	{"text": "名称：无锡邻医大药房有限公司", "bbox": [536, 277, 740, 298], "bbox_2d": [536, 277, 740, 298]},
	{"text": "统一社会信用代码/纳税人识别号：91320214MA228F680W", "bbox": [535, 341, 954, 364], "bbox_2d": [535, 341, 954, 364]},
	{"text": "项目名称", "bbox": [77, 402, 136, 421], "bbox_2d": [77, 402, 136, 421]},
	{"text": "规格型号", "bbox": [199, 402, 258, 421], "bbox_2d": [199, 402, 258, 421]},
	{"text": "单位", "bbox": [319, 402, 363, 421], "bbox_2d": [319, 402, 363, 421]},
	{"text": "数量", "bbox": [441, 402, 486, 421], "bbox_2d": [441, 402, 486, 421]},
	{"text": "单价", "bbox": [558, 402, 602, 421], "bbox_2d": [558, 402, 602, 421]},
	{"text": "金额", "bbox": [680, 402, 724, 421], "bbox_2d": [680, 402, 724, 421]},
	{"text": "税率/征收率", "bbox": [744, 402, 826, 421], "bbox_2d": [744, 402, 826, 421]},
	{"text": "税额", "bbox": [923, 402, 968, 421], "bbox_2d": [923, 402, 968, 421]},
	{"text": "*化学药品制剂*倍择瑞令", "bbox": [26, 427, 187, 449], "bbox_2d": [26, 427, 187, 449]},
	{"text": "160μg/7.2μg/4", "bbox": [200, 428, 301, 452], "bbox_2d": [200, 428, 301, 452]},
	{"text": "盒", "bbox": [333, 428, 349, 449], "bbox_2d": [333, 428, 349, 449]},
	{"text": "3", "bbox": [477, 428, 487, 449], "bbox_2d": [477, 428, 487, 449]},
	{"text": "210.029498522124", "bbox": [493, 428, 602, 449], "bbox_2d": [493, 428, 602, 449]},
	{"text": "630.09", "bbox": [684, 428, 722, 449], "bbox_2d": [684, 428, 722, 449]},
	{"text": "13%", "bbox": [778, 428, 803, 449], "bbox_2d": [778, 428, 803, 449]},
	{"text": "81.91", "bbox": [937, 428, 968, 449], "bbox_2d": [937, 428, 968, 449]},
	{"text": "畅布地格福吸入气雾剂", "bbox": [26, 457, 178, 479], "bbox_2d": [26, 457, 178, 479]},
	{"text": ".8μg*120揿", "bbox": [200, 457, 280, 482], "bbox_2d": [200, 457, 280, 482]},
	{"text": "合计", "bbox": [101, 673, 114, 692], "bbox_2d": [101, 673, 114, 692]},
	{"text": "计", "bbox": [174, 673, 188, 692], "bbox_2d": [174, 673, 188, 692]},
	{"text": "￥630.09", "bbox": [672, 669, 722, 689], "bbox_2d": [672, 669, 722, 689]},
	{"text": "￥81.91", "bbox": [925, 669, 968, 689], "bbox_2d": [925, 669, 968, 689]},
	{"text": "价税合计（大写）", "bbox": [84, 715, 194, 735], "bbox_2d": [84, 715, 194, 735]},
	{"text": "柒佰壹拾贰圆整", "bbox": [301, 710, 408, 733], "bbox_2d": [301, 710, 408, 733]},
	{"text": "(小写) ￥712.00", "bbox": [690, 709, 811, 733], "bbox_2d": [690, 709, 811, 733]},
	{"text": "备注", "bbox": [32, 787, 46, 806], "bbox_2d": [32, 787, 46, 806]},
	{"text": "开票人：奚澳琼", "bbox": [95, 917, 200, 938], "bbox_2d": [95, 917, 200, 938]}
]
2026-08-10 12:52:27,860 INFO     29 [qwen-vl-text] coord API: raw_items=38, valid_items=38, elapsed=17.5s
2026-08-10 12:52:27,861 INFO     29 [qwen-vl-text] coord item[0]: text=电子发票(普通发票), bbox=[327, 103, 637, 148]
2026-08-10 12:52:27,861 INFO     29 [qwen-vl-text] coord item[1]: text=国家税务总局, bbox=[463, 155, 534, 172]
2026-08-10 12:52:27,861 INFO     29 [qwen-vl-text] coord item[2]: text=江苏省税务局, bbox=[463, 187, 537, 210]
2026-08-10 12:52:27,861 INFO     29 [qwen-vl-text] coord item[3]: text=发票号码：25322000000382591347, bbox=[733, 122, 948, 143]
2026-08-10 12:52:27,861 INFO     29 [qwen-vl-text] coord item[4]: text=开票日期：2025年08月20日, bbox=[733, 161, 909, 182]
2026-08-10 12:52:27,861 INFO     29 [qwen-vl-text] coord item[5]: text=购买方信息, bbox=[32, 265, 46, 380]
2026-08-10 12:52:27,861 INFO     29 [qwen-vl-text] coord item[6]: text=名称：, bbox=[59, 282, 92, 302]
2026-08-10 12:52:27,861 INFO     29 [qwen-vl-text] coord item[7]: text=统一社会信用代码/纳税人识别号：, bbox=[58, 346, 258, 366]
2026-08-10 12:52:27,861 INFO     29 [qwen-vl-text] coord item[8]: text=销售方信息, bbox=[507, 265, 521, 380]
2026-08-10 12:52:27,861 INFO     29 [qwen-vl-text] coord item[9]: text=名称：无锡邻医大药房有限公司, bbox=[536, 277, 740, 298]
2026-08-10 12:52:27,861 INFO     29 [qwen-vl-text] coord item[10]: text=统一社会信用代码/纳税人识别号：91320214MA228F680W, bbox=[535, 341, 954, 364]
2026-08-10 12:52:27,861 INFO     29 [qwen-vl-text] coord item[11]: text=项目名称, bbox=[77, 402, 136, 421]
2026-08-10 12:52:27,861 INFO     29 [qwen-vl-text] coord item[12]: text=规格型号, bbox=[199, 402, 258, 421]
2026-08-10 12:52:27,861 INFO     29 [qwen-vl-text] coord item[13]: text=单位, bbox=[319, 402, 363, 421]
2026-08-10 12:52:27,862 INFO     29 [qwen-vl-text] coord item[14]: text=数量, bbox=[441, 402, 486, 421]
2026-08-10 12:52:27,862 INFO     29 [qwen-vl-text] coord item[15]: text=单价, bbox=[558, 402, 602, 421]
2026-08-10 12:52:27,862 INFO     29 [qwen-vl-text] coord item[16]: text=金额, bbox=[680, 402, 724, 421]
2026-08-10 12:52:27,862 INFO     29 [qwen-vl-text] coord item[17]: text=税率/征收率, bbox=[744, 402, 826, 421]
2026-08-10 12:52:27,862 INFO     29 [qwen-vl-text] coord item[18]: text=税额, bbox=[923, 402, 968, 421]
2026-08-10 12:52:27,862 INFO     29 [qwen-vl-text] coord item[19]: text=*化学药品制剂*倍择瑞令, bbox=[26, 427, 187, 449]
2026-08-10 12:52:27,862 INFO     29 [qwen-vl-text] coord item[20]: text=160μg/7.2μg/4, bbox=[200, 428, 301, 452]
2026-08-10 12:52:27,862 INFO     29 [qwen-vl-text] coord item[21]: text=盒, bbox=[333, 428, 349, 449]
2026-08-10 12:52:27,862 INFO     29 [qwen-vl-text] coord item[22]: text=3, bbox=[477, 428, 487, 449]
2026-08-10 12:52:27,862 INFO     29 [qwen-vl-text] coord item[23]: text=210.029498522124, bbox=[493, 428, 602, 449]
2026-08-10 12:52:27,862 INFO     29 [qwen-vl-text] coord item[24]: text=630.09, bbox=[684, 428, 722, 449]
2026-08-10 12:52:27,862 INFO     29 [qwen-vl-text] coord item[25]: text=13%, bbox=[778, 428, 803, 449]
2026-08-10 12:52:27,862 INFO     29 [qwen-vl-text] coord item[26]: text=81.91, bbox=[937, 428, 968, 449]
2026-08-10 12:52:27,863 INFO     29 [qwen-vl-text] coord item[27]: text=畅布地格福吸入气雾剂, bbox=[26, 457, 178, 479]
2026-08-10 12:52:27,863 INFO     29 [qwen-vl-text] coord item[28]: text=.8μg*120揿, bbox=[200, 457, 280, 482]
2026-08-10 12:52:27,863 INFO     29 [qwen-vl-text] coord item[29]: text=合计, bbox=[101, 673, 114, 692]
2026-08-10 12:52:27,863 INFO     29 [qwen-vl-text] coord item[30]: text=计, bbox=[174, 673, 188, 692]
2026-08-10 12:52:27,863 INFO     29 [qwen-vl-text] coord item[31]: text=￥630.09, bbox=[672, 669, 722, 689]
2026-08-10 12:52:27,863 INFO     29 [qwen-vl-text] coord item[32]: text=￥81.91, bbox=[925, 669, 968, 689]
2026-08-10 12:52:27,863 INFO     29 [qwen-vl-text] coord item[33]: text=价税合计（大写）, bbox=[84, 715, 194, 735]
2026-08-10 12:52:27,863 INFO     29 [qwen-vl-text] coord item[34]: text=柒佰壹拾贰圆整, bbox=[301, 710, 408, 733]
2026-08-10 12:52:27,863 INFO     29 [qwen-vl-text] coord item[35]: text=(小写) ￥712.00, bbox=[690, 709, 811, 733]
2026-08-10 12:52:27,863 INFO     29 [qwen-vl-text] coord item[36]: text=备注, bbox=[32, 787, 46, 806]
2026-08-10 12:52:27,863 INFO     29 [qwen-vl-text] coord item[37]: text=开票人：奚澳琼, bbox=[95, 917, 200, 938]
2026-08-10 12:52:27,864 INFO     29 [qwen-vl-text] page=2 — 37/37 coords, api_time=17.5s
2026-08-10 12:52:27,864 INFO     29 [qwen-vl-text] new_positions (37):
[[2, 275.334, 536.3539999999999, 61.285, 88.06], [2, 389.846, 449.628, 92.225, 102.33999999999999], [2, 389.846, 452.154, 111.265, 124.94999999999999], [2, 617.1859999999999, 798.216, 72.59, 85.085], [2, 617.1859999999999, 765.3779999999999, 95.795, 108.28999999999999], [2, 26.944, 38.732, 157.67499999999998, 226.1], [2, 49.678, 77.464, 167.79, 179.69], [2, 48.836, 217.236, 205.87, 217.76999999999998], [2, 426.894, 438.68199999999996, 157.67499999999998, 226.1], [2, 451.312, 623.0799999999999, 164.815, 177.31], [2, 450.46999999999997, 803.2679999999999, 202.89499999999998, 216.57999999999998], [2, 64.834, 114.512, 239.19, 250.49499999999998], [2, 167.558, 217.236, 239.19, 250.49499999999998], [2, 268.598, 305.646, 239.19, 250.49499999999998], [2, 371.322, 409.212, 239.19, 250.49499999999998], [2, 469.83599999999996, 506.88399999999996, 239.19, 250.49499999999998], [2, 572.56, 609.608, 239.19, 250.49499999999998], [2, 626.448, 695.492, 239.19, 250.49499999999998], [2, 777.1659999999999, 815.0559999999999, 239.19, 250.49499999999998], [2, 21.892, 157.454, 254.065, 267.155], [2, 168.4, 253.44199999999998, 254.66, 268.94], [2, 280.38599999999997, 293.858, 254.66, 267.155], [2, 401.63399999999996, 410.054, 254.66, 267.155], [2, 415.106, 506.88399999999996, 254.66, 267.155], [2, 575.928, 607.924, 254.66, 267.155], [2, 655.076, 676.126, 254.66, 267.155], [2, 788.954, 815.0559999999999, 254.66, 267.155], [2, 21.892, 149.876, 271.91499999999996, 285.005], [2, 168.4, 235.76, 271.91499999999996, 286.78999999999996], [2, 85.042, 95.988, 400.435, 411.74], [2, 146.50799999999998, 158.296, 400.435, 411.74], [2, 565.824, 607.924, 398.055, 409.955], [2, 778.85, 815.0559999999999, 398.055, 409.955], [2, 70.728, 163.34799999999998, 425.42499999999995, 437.325], [2, 253.44199999999998, 343.536, 422.45, 436.135], [2, 580.98, 682.862, 421.85499999999996, 436.135], [2, 26.944, 38.732, 468.265, 479.57]]
2026-08-10 12:52:27,864 INFO     29 [qwen-vl-text] ═══ DONE ═══ 37 positions, pages=1, time=19.9s
2026-08-10 12:52:27,864 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:52:27,872 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:52:27,872 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 12:52:27,872 INFO     29 [qwen-vl-text] positions(36): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:52:27,872 INFO     29 [qwen-vl-text] page grouping: [3, 4], lines per page: [35, 1]
2026-08-10 12:52:28,033 INFO     29 [qwen-vl-text] page=3, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 12:52:28,574 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:52:28,576 INFO     29 [qwen-vl-text] LLM extraction start, text_len=372
2026-08-10 12:52:28,576 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:52:28,576 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 92, \"bbox_end\": 127, \"encounter_dates\": [\"2025-05-20\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "电子发票(普通发票)\n国家税务总局\n江苏省税务局\n发票号码：25322000000226700883\n开票日期：2025年05月20日\n购买方信息\n名称\n统一社会信用代码/纳税人识别号：\n销售方信息\n名称：无锡邻医大药房有限公司\n统一社会信用代码/纳税人识别号：91320214MA228F680W\n项目名称\n规格型号\n单位\n数量\n单价\n金额\n税率/征收率\n税额\n*化学药品制剂*倍择瑞令\n160μg/7.2μg/4\n盒\n3 210.029498522124\n630.09\n13%\n81.91\n畅布地格福吸入气雾剂\n.8μg*120揿\n合计\n￥630.09\n￥81.91\n价税合计（大写）\n柒佰壹拾贰圆整\n(小写）￥712.00\n备注\n挂号号:D20091... 医保余额:0 CM/KG 普通病人|现住址:内蒙古土默特左旗沙尔营乡大有庄村32",
    "role": "user"
  }
]
2026-08-10 12:52:28,578 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:52:28.577+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 34, "failed": 0, "current": {"1f69c42a94ba11f1bd9827cf206dfa2d": {"id": "1f69c42a94ba11f1bd9827cf206dfa2d", "doc_id": "1f30448e94ba11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHYH.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHYH.pdf", "size": 10529265, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786366253712, "task_type": "dataflow", "root_trace_id": "ccbe99209a7f4a07832eb1586b73139c", "root_traceparent": "00-ccbe99209a7f4a07832eb1586b73139c-b8274641f81bf5ac-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:52:30,812 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:52:30,813 INFO     29 [qwen-vl-text] LLM output (len=428):
{
  "encounter_date": "2025-05-20",
  "pharmacy": "无锡邻医大药房有限公司",
  "medications": [
    {
      "name": "倍择瑞",
      "specification": "160μg/7.2μg/4.8μg*120揿",
      "dosage": null,
      "quantity": 3,
      "unit_price": 210.03,
      "total_price": 630.09,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 712.00,
  "payment_method": null
}
2026-08-10 12:52:30,813 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-05-20]
2026-08-10 12:52:30,815 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=847478, prompt_len=1035
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["电子发票(普通发票)", "国家税务总局", "江苏省税务局", "发票号码：25322000000226700883", "开票日期：2025年05月20日", "购买方信息", "名称", "统一社会信用代码/纳税人识别号：", "销售方信息", "名称：无锡邻医大药房有限公司", "统一社会信用代码/纳税人识别号：91320214MA228F680W", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*倍择瑞令", "160μg/7.2μg/4", "盒", "3 210.029498522124", "630.09", "13%", "81.91", "畅布地格福吸入气雾剂", ".8μg*120揿", "合计", "￥630.09", "￥81.91", "价税合计（大写）", "柒佰壹拾贰圆整", "(小写）￥712.00", "备注"]

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
2026-08-10 12:52:48,227 INFO     29 [qwen-vl-text] coord API raw response (len=2976):
```json
[
	{"text": "电子发票(普通发票)", "bbox": [328, 123, 635, 168], "bbox": [328, 123, 635, 168]},
	{"text": "国家税务总局", "bbox": [463, 175, 534, 192], "bbox": [463, 175, 534, 192]},
	{"text": "江苏省税务局", "bbox": [463, 206, 537, 232], "bbox": [463, 206, 537, 232]},
	{"text": "发票号码：25322000000226700883", "bbox": [731, 143, 944, 164], "bbox": [731, 143, 944, 164]},
	{"text": "开票日期：2025年05月20日", "bbox": [731, 181, 905, 202], "bbox": [731, 181, 905, 202]},
	{"text": "购买方信息", "bbox": [36, 284, 50, 398], "bbox": [36, 284, 50, 398]},
	{"text": "名称", "bbox": [62, 302, 89, 321], "bbox": [62, 302, 89, 321]},
	{"text": "统一社会信用代码/纳税人识别号：", "bbox": [61, 365, 259, 384], "bbox": [61, 365, 259, 384]},
	{"text": "销售方信息", "bbox": [507, 284, 520, 398], "bbox": [507, 284, 520, 398]},
	{"text": "名称：无锡邻医大药房有限公司", "bbox": [535, 296, 738, 317], "bbox": [535, 296, 738, 317]},
	{"text": "统一社会信用代码/纳税人识别号：91320214MA228F680W", "bbox": [534, 360, 950, 382], "bbox": [534, 360, 950, 382]},
	{"text": "项目名称", "bbox": [80, 420, 139, 440], "bbox": [80, 420, 139, 440]},
	{"text": "规格型号", "bbox": [201, 420, 260, 440], "bbox": [201, 420, 260, 440]},
	{"text": "单位", "bbox": [320, 420, 364, 440], "bbox": [320, 420, 364, 440]},
	{"text": "数量", "bbox": [442, 420, 486, 440], "bbox": [442, 420, 486, 440]},
	{"text": "单价", "bbox": [557, 420, 600, 440], "bbox": [557, 420, 600, 440]},
	{"text": "金额", "bbox": [679, 420, 721, 440], "bbox": [679, 420, 721, 440]},
	{"text": "税率/征收率", "bbox": [741, 420, 823, 440], "bbox": [741, 420, 823, 440]},
	{"text": "税额", "bbox": [920, 420, 964, 440], "bbox": [920, 420, 964, 440]},
	{"text": "*化学药品制剂*倍择瑞令", "bbox": [30, 445, 190, 467], "bbox": [30, 445, 190, 467]},
	{"text": "160μg/7.2μg/4", "bbox": [203, 447, 303, 470], "bbox": [203, 447, 303, 470]},
	{"text": "盒", "bbox": [334, 447, 350, 467], "bbox": [334, 447, 350, 467]},
	{"text": "3 210.029498522124", "bbox": [477, 447, 601, 467], "bbox": [477, 447, 601, 467]},
	{"text": "630.09", "bbox": [682, 447, 720, 467], "bbox": [682, 447, 720, 467]},
	{"text": "13%", "bbox": [775, 447, 800, 467], "bbox": [775, 447, 800, 467]},
	{"text": "81.91", "bbox": [933, 447, 964, 467], "bbox": [933, 447, 964, 467]},
	{"text": "畅布地格福吸入气雾剂", "bbox": [30, 474, 180, 497], "bbox": [30, 474, 180, 497]},
	{"text": ".8μg*120揿", "bbox": [203, 475, 281, 499], "bbox": [203, 475, 281, 499]},
	{"text": "合计", "bbox": [104, 688, 117, 707], "bbox": [104, 688, 117, 707]},
	{"text": "计", "bbox": [177, 688, 190, 707], "bbox": [177, 688, 190, 707]},
	{"text": "￥630.09", "bbox": [676, 687, 720, 704], "bbox": [676, 687, 720, 704]},
	{"text": "￥81.91", "bbox": [926, 687, 964, 704], "bbox": [926, 687, 964, 704]},
	{"text": "价税合计（大写）", "bbox": [87, 730, 196, 750], "bbox": [87, 730, 196, 750]},
	{"text": "柒佰壹拾贰圆整", "bbox": [303, 725, 408, 747], "bbox": [303, 725, 408, 747]},
	{"text": "(小写）￥712.00", "bbox": [688, 725, 808, 747], "bbox": [688, 725, 808, 747]},
	{"text": "备注", "bbox": [36, 800, 50, 858], "bbox": [36, 800, 50, 858]}
]
```
2026-08-10 12:52:48,228 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=17.4s
2026-08-10 12:52:48,228 INFO     29 [qwen-vl-text] coord item[0]: text=电子发票(普通发票), bbox=[328, 123, 635, 168]
2026-08-10 12:52:48,228 INFO     29 [qwen-vl-text] coord item[1]: text=国家税务总局, bbox=[463, 175, 534, 192]
2026-08-10 12:52:48,228 INFO     29 [qwen-vl-text] coord item[2]: text=江苏省税务局, bbox=[463, 206, 537, 232]
2026-08-10 12:52:48,228 INFO     29 [qwen-vl-text] coord item[3]: text=发票号码：25322000000226700883, bbox=[731, 143, 944, 164]
2026-08-10 12:52:48,228 INFO     29 [qwen-vl-text] coord item[4]: text=开票日期：2025年05月20日, bbox=[731, 181, 905, 202]
2026-08-10 12:52:48,228 INFO     29 [qwen-vl-text] coord item[5]: text=购买方信息, bbox=[36, 284, 50, 398]
2026-08-10 12:52:48,229 INFO     29 [qwen-vl-text] coord item[6]: text=名称, bbox=[62, 302, 89, 321]
2026-08-10 12:52:48,229 INFO     29 [qwen-vl-text] coord item[7]: text=统一社会信用代码/纳税人识别号：, bbox=[61, 365, 259, 384]
2026-08-10 12:52:48,229 INFO     29 [qwen-vl-text] coord item[8]: text=销售方信息, bbox=[507, 284, 520, 398]
2026-08-10 12:52:48,229 INFO     29 [qwen-vl-text] coord item[9]: text=名称：无锡邻医大药房有限公司, bbox=[535, 296, 738, 317]
2026-08-10 12:52:48,229 INFO     29 [qwen-vl-text] coord item[10]: text=统一社会信用代码/纳税人识别号：91320214MA228F680W, bbox=[534, 360, 950, 382]
2026-08-10 12:52:48,229 INFO     29 [qwen-vl-text] coord item[11]: text=项目名称, bbox=[80, 420, 139, 440]
2026-08-10 12:52:48,229 INFO     29 [qwen-vl-text] coord item[12]: text=规格型号, bbox=[201, 420, 260, 440]
2026-08-10 12:52:48,229 INFO     29 [qwen-vl-text] coord item[13]: text=单位, bbox=[320, 420, 364, 440]
2026-08-10 12:52:48,230 INFO     29 [qwen-vl-text] coord item[14]: text=数量, bbox=[442, 420, 486, 440]
2026-08-10 12:52:48,230 INFO     29 [qwen-vl-text] coord item[15]: text=单价, bbox=[557, 420, 600, 440]
2026-08-10 12:52:48,230 INFO     29 [qwen-vl-text] coord item[16]: text=金额, bbox=[679, 420, 721, 440]
2026-08-10 12:52:48,230 INFO     29 [qwen-vl-text] coord item[17]: text=税率/征收率, bbox=[741, 420, 823, 440]
2026-08-10 12:52:48,230 INFO     29 [qwen-vl-text] coord item[18]: text=税额, bbox=[920, 420, 964, 440]
2026-08-10 12:52:48,230 INFO     29 [qwen-vl-text] coord item[19]: text=*化学药品制剂*倍择瑞令, bbox=[30, 445, 190, 467]
2026-08-10 12:52:48,230 INFO     29 [qwen-vl-text] coord item[20]: text=160μg/7.2μg/4, bbox=[203, 447, 303, 470]
2026-08-10 12:52:48,231 INFO     29 [qwen-vl-text] coord item[21]: text=盒, bbox=[334, 447, 350, 467]
2026-08-10 12:52:48,231 INFO     29 [qwen-vl-text] coord item[22]: text=3 210.029498522124, bbox=[477, 447, 601, 467]
2026-08-10 12:52:48,231 INFO     29 [qwen-vl-text] coord item[23]: text=630.09, bbox=[682, 447, 720, 467]
2026-08-10 12:52:48,231 INFO     29 [qwen-vl-text] coord item[24]: text=13%, bbox=[775, 447, 800, 467]
2026-08-10 12:52:48,231 INFO     29 [qwen-vl-text] coord item[25]: text=81.91, bbox=[933, 447, 964, 467]
2026-08-10 12:52:48,231 INFO     29 [qwen-vl-text] coord item[26]: text=畅布地格福吸入气雾剂, bbox=[30, 474, 180, 497]
2026-08-10 12:52:48,231 INFO     29 [qwen-vl-text] coord item[27]: text=.8μg*120揿, bbox=[203, 475, 281, 499]
2026-08-10 12:52:48,231 INFO     29 [qwen-vl-text] coord item[28]: text=合计, bbox=[104, 688, 117, 707]
2026-08-10 12:52:48,231 INFO     29 [qwen-vl-text] coord item[29]: text=计, bbox=[177, 688, 190, 707]
2026-08-10 12:52:48,231 INFO     29 [qwen-vl-text] coord item[30]: text=￥630.09, bbox=[676, 687, 720, 704]
2026-08-10 12:52:48,231 INFO     29 [qwen-vl-text] coord item[31]: text=￥81.91, bbox=[926, 687, 964, 704]
2026-08-10 12:52:48,231 INFO     29 [qwen-vl-text] coord item[32]: text=价税合计（大写）, bbox=[87, 730, 196, 750]
2026-08-10 12:52:48,231 INFO     29 [qwen-vl-text] coord item[33]: text=柒佰壹拾贰圆整, bbox=[303, 725, 408, 747]
2026-08-10 12:52:48,231 INFO     29 [qwen-vl-text] coord item[34]: text=(小写）￥712.00, bbox=[688, 725, 808, 747]
2026-08-10 12:52:48,231 INFO     29 [qwen-vl-text] coord item[35]: text=备注, bbox=[36, 800, 50, 858]
2026-08-10 12:52:48,231 INFO     29 [qwen-vl-text] page=3 — 35/35 coords, api_time=17.4s
2026-08-10 12:52:48,249 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7824738, prompt_len=669
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["挂号号:D20091... 医保余额:0 CM/KG 普通病人|现住址:内蒙古土默特左旗沙尔营乡大有庄村32"]

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
2026-08-10 12:52:49,656 INFO     29 [qwen-vl-text] coord API raw response (len=97):
[
	{"text": "挂号号:D20091... 医保余额:0 CM/KG 普通病人|现住址:内蒙古土默特左旗沙尔营乡大有庄村32", "bbox": [0, 48, 999, 94]}
]
2026-08-10 12:52:49,656 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=1.4s
2026-08-10 12:52:49,657 INFO     29 [qwen-vl-text] coord item[0]: text=挂号号:D20091... 医保余额:0 CM/KG 普通病人|现住址:内蒙古土默特左旗沙尔营乡大有庄村32, bbox=[0, 48, 999, 94]
2026-08-10 12:52:49,659 INFO     29 [qwen-vl-text] page=4 — 1/1 coords, api_time=1.4s
2026-08-10 12:52:49,660 INFO     29 [qwen-vl-text] new_positions (36):
[[3, 276.176, 534.67, 73.185, 99.96], [3, 389.846, 449.628, 104.125, 114.24], [3, 389.846, 452.154, 122.57, 138.04], [3, 615.502, 794.848, 85.085, 97.58], [3, 615.502, 762.01, 107.695, 120.19], [3, 30.311999999999998, 42.1, 168.98, 236.81], [3, 52.204, 74.938, 179.69, 190.995], [3, 51.361999999999995, 218.078, 217.17499999999998, 228.48], [3, 426.894, 437.84, 168.98, 236.81], [3, 450.46999999999997, 621.396, 176.12, 188.61499999999998], [3, 449.628, 799.9, 214.2, 227.29], [3, 67.36, 117.038, 249.89999999999998, 261.8], [3, 169.242, 218.92, 249.89999999999998, 261.8], [3, 269.44, 306.488, 249.89999999999998, 261.8], [3, 372.164, 409.212, 249.89999999999998, 261.8], [3, 468.99399999999997, 505.2, 249.89999999999998, 261.8], [3, 571.718, 607.082, 249.89999999999998, 261.8], [3, 623.922, 692.966, 249.89999999999998, 261.8], [3, 774.64, 811.688, 249.89999999999998, 261.8], [3, 25.259999999999998, 159.98, 264.775, 277.865], [3, 170.926, 255.126, 265.965, 279.65], [3, 281.228, 294.7, 265.965, 277.865], [3, 401.63399999999996, 506.042, 265.965, 277.865], [3, 574.244, 606.24, 265.965, 277.865], [3, 652.55, 673.6, 265.965, 277.865], [3, 785.586, 811.688, 265.965, 277.865], [3, 25.259999999999998, 151.56, 282.03, 295.715], [3, 170.926, 236.602, 282.625, 296.905], [3, 87.568, 98.514, 409.35999999999996, 420.66499999999996], [3, 149.034, 159.98, 409.35999999999996, 420.66499999999996], [3, 569.192, 606.24, 408.765, 418.88], [3, 779.692, 811.688, 408.765, 418.88], [3, 73.25399999999999, 165.03199999999998, 434.34999999999997, 446.25], [3, 255.126, 343.536, 431.375, 444.465], [3, 579.2959999999999, 680.336, 431.375, 444.465], [4, 0.0, 594.405, 40.416, 79.148]]
2026-08-10 12:52:49,660 INFO     29 [qwen-vl-text] ═══ DONE ═══ 36 positions, pages=2, time=21.8s
2026-08-10 12:52:49,661 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:52:49,662 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:52:49,662 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 12:52:49,662 INFO     29 [qwen-vl-text] positions(47): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:52:49,662 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [47]
2026-08-10 12:52:49,834 INFO     29 [qwen-vl-text] page=5, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 12:52:49,836 INFO     29 [qwen-vl-text] LLM extraction start, text_len=410
2026-08-10 12:52:49,836 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:52:49,836 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 152, \"bbox_end\": 198, \"encounter_dates\": [\"2026-02-09\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "电子发票(普通发票)\n国家税务总局\n内蒙古自治区税务局\n发票号码：26152000000119478346\n开票日期：2026年02月09日\n购买方信息\n名称\n统一社会信用代码/纳税人识别号：\n销售方信息\n名称：国药控股国大药房内蒙古有限公司\n统一社会信用代码/纳税人识别号：911501005732872139\n项目名称\n规格型号\n单位\n数量\n单价\n金额\n税率/征收率\n税额\n*化学药品制剂*布地格福\n160ug:7.2ug/4.8u\n盒\n3\n237.16814159292\n711.50\n13%\n92.50\n吸入气雾剂\ng:120揿\n*化学药品制剂*布地格福\n160ug:7.2ug/4.8u\n盒\n3\n237.16814159292\n711.50\n13%\n92.50\n吸入气雾剂\ng:120揿\n合计\n￥1423.00\n￥185.00\n价税合计（大写）\n壹仟陆佰零捌圆整\n(小写) ￥1608.00\n备注\n开票人：刘惠",
    "role": "user"
  }
]
2026-08-10 12:52:53,054 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:52:53,054 INFO     29 [qwen-vl-text] LLM output (len=750):
{
  "encounter_date": "2026-02-09",
  "pharmacy": "国药控股国大药房内蒙古有限公司",
  "medications": [
    {
      "name": "布地格福吸入气雾剂",
      "specification": "160ug:7.2ug/4.8ug:120揿",
      "dosage": null,
      "quantity": 3,
      "unit_price": 237.16814159292,
      "total_price": 711.50,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    },
    {
      "name": "布地格福吸入气雾剂",
      "specification": "160ug:7.2ug/4.8ug:120揿",
      "dosage": null,
      "quantity": 3,
      "unit_price": 237.16814159292,
      "total_price": 711.50,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 1608.00,
  "payment_method": null
}
2026-08-10 12:52:53,054 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-09]
2026-08-10 12:52:53,056 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=946229, prompt_len=1164
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共47行）
["电子发票(普通发票)", "国家税务总局", "内蒙古自治区税务局", "发票号码：26152000000119478346", "开票日期：2026年02月09日", "购买方信息", "名称", "统一社会信用代码/纳税人识别号：", "销售方信息", "名称：国药控股国大药房内蒙古有限公司", "统一社会信用代码/纳税人识别号：911501005732872139", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*布地格福", "160ug:7.2ug/4.8u", "盒", "3", "237.16814159292", "711.50", "13%", "92.50", "吸入气雾剂", "g:120揿", "*化学药品制剂*布地格福", "160ug:7.2ug/4.8u", "盒", "3", "237.16814159292", "711.50", "13%", "92.50", "吸入气雾剂", "g:120揿", "合计", "￥1423.00", "￥185.00", "价税合计（大写）", "壹仟陆佰零捌圆整", "(小写) ￥1608.00", "备注", "开票人：刘惠"]

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
2026-08-10 12:53:16,654 INFO     29 [qwen-vl-text] coord API raw response (len=4156):
[
	{"text": "电子发票(普通发票)", "bbox": [327, 80, 639, 125], "bbox_2d": [327, 80, 639, 125]},
	{"text": "国家税务总局", "bbox": [464, 133, 535, 149], "bbox_2d": [464, 133, 535, 149]},
	{"text": "内蒙古自治区税务局", "bbox": [452, 159, 552, 192], "bbox_2d": [452, 159, 552, 192]},
	{"text": "发票号码：26152000000119478346", "bbox": [735, 100, 951, 120], "bbox_2d": [735, 100, 951, 120]},
	{"text": "开票日期：2026年02月09日", "bbox": [735, 139, 911, 160], "bbox_2d": [735, 139, 911, 160]},
	{"text": "购买方信息", "bbox": [32, 244, 46, 360], "bbox_2d": [32, 244, 46, 360]},
	{"text": "名称", "bbox": [59, 260, 84, 280], "bbox_2d": [59, 260, 84, 280]},
	{"text": "统一社会信用代码/纳税人识别号：", "bbox": [58, 324, 258, 344], "bbox_2d": [58, 324, 258, 344]},
	{"text": "销售方信息", "bbox": [509, 244, 522, 360], "bbox_2d": [509, 244, 522, 360]},
	{"text": "名称：国药控股国大药房内蒙古有限公司", "bbox": [537, 255, 802, 277], "bbox_2d": [537, 255, 802, 277]},
	{"text": "统一社会信用代码/纳税人识别号：911501005732872139", "bbox": [536, 320, 955, 343], "bbox_2d": [536, 320, 955, 343]},
	{"text": "项目名称", "bbox": [77, 380, 136, 400], "bbox_2d": [77, 380, 136, 400]},
	{"text": "规格型号", "bbox": [199, 380, 258, 400], "bbox_2d": [199, 380, 258, 400]},
	{"text": "单位", "bbox": [320, 380, 364, 400], "bbox_2d": [320, 380, 364, 400]},
	{"text": "数量", "bbox": [443, 380, 487, 400], "bbox_2d": [443, 380, 487, 400]},
	{"text": "单价", "bbox": [560, 380, 603, 400], "bbox_2d": [560, 380, 603, 400]},
	{"text": "金额", "bbox": [682, 380, 725, 400], "bbox_2d": [682, 380, 725, 400]},
	{"text": "税率/征收率", "bbox": [746, 380, 828, 400], "bbox_2d": [746, 380, 828, 400]},
	{"text": "税额", "bbox": [926, 380, 970, 400], "bbox_2d": [926, 380, 970, 400]},
	{"text": "*化学药品制剂*布地格福", "bbox": [26, 405, 188, 428], "bbox_2d": [26, 405, 188, 428]},
	{"text": "160ug:7.2ug/4.8u", "bbox": [201, 407, 304, 430], "bbox_2d": [201, 407, 304, 430]},
	{"text": "盒", "bbox": [334, 407, 350, 428], "bbox_2d": [334, 407, 350, 428]},
	{"text": "3", "bbox": [478, 407, 488, 428], "bbox_2d": [478, 407, 488, 428]},
	{"text": "237.16814159292", "bbox": [503, 407, 604, 428], "bbox_2d": [503, 407, 604, 428]},
	{"text": "711.50", "bbox": [686, 407, 724, 428], "bbox_2d": [686, 407, 724, 428]},
	{"text": "13%", "bbox": [780, 407, 805, 428], "bbox_2d": [780, 407, 805, 428]},
	{"text": "92.50", "bbox": [940, 407, 971, 428], "bbox_2d": [940, 407, 971, 428]},
	{"text": "吸入气雾剂", "bbox": [26, 436, 101, 459], "bbox_2d": [26, 436, 101, 459]},
	{"text": "g:120揿", "bbox": [201, 437, 249, 460], "bbox_2d": [201, 437, 249, 460]},
	{"text": "*化学药品制剂*布地格福", "bbox": [26, 467, 188, 490], "bbox_2d": [26, 467, 188, 490]},
	{"text": "160ug:7.2ug/4.8u", "bbox": [201, 468, 304, 491], "bbox_2d": [201, 468, 304, 491]},
	{"text": "盒", "bbox": [334, 468, 350, 490], "bbox_2d": [334, 468, 350, 490]},
	{"text": "3", "bbox": [478, 468, 488, 490], "bbox_2d": [478, 468, 488, 490]},
	{"text": "237.16814159292", "bbox": [503, 468, 604, 490], "bbox_2d": [503, 468, 604, 490]},
	{"text": "711.50", "bbox": [686, 468, 724, 490], "bbox_2d": [686, 468, 724, 490]},
	{"text": "13%", "bbox": [780, 468, 805, 490], "bbox_2d": [780, 468, 805, 490]},
	{"text": "92.50", "bbox": [940, 468, 971, 490], "bbox_2d": [940, 468, 971, 490]},
	{"text": "吸入气雾剂", "bbox": [26, 497, 101, 520], "bbox_2d": [26, 497, 101, 520]},
	{"text": "g:120揿", "bbox": [201, 498, 249, 521], "bbox_2d": [201, 498, 249, 521]},
	{"text": "合计", "bbox": [101, 654, 114, 672], "bbox_2d": [101, 654, 114, 672]},
	{"text": "计", "bbox": [175, 654, 188, 672], "bbox_2d": [175, 654, 188, 672]},
	{"text": "￥1423.00", "bbox": [667, 650, 724, 670], "bbox_2d": [667, 650, 724, 670]},
	{"text": "￥185.00", "bbox": [920, 650, 971, 670], "bbox_2d": [920, 650, 971, 670]},
	{"text": "价税合计（大写）", "bbox": [84, 695, 194, 715], "bbox_2d": [84, 695, 194, 715]},
	{"text": "壹仟陆佰零捌圆整", "bbox": [303, 691, 424, 713], "bbox_2d": [303, 691, 424, 713]},
	{"text": "(小写) ￥1608.00", "bbox": [691, 689, 821, 713], "bbox_2d": [691, 689, 821, 713]},
	{"text": "备注", "bbox": [32, 767, 46, 787], "bbox_2d": [32, 767, 46, 787]},
	{"text": "注", "bbox": [32, 807, 46, 827], "bbox_2d": [32, 807, 46, 827]},
	{"text": "开票人：刘惠", "bbox": [95, 898, 185, 920], "bbox_2d": [95, 898, 185, 920]}
]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord API: raw_items=49, valid_items=49, elapsed=23.6s
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[0]: text=电子发票(普通发票), bbox=[327, 80, 639, 125]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[1]: text=国家税务总局, bbox=[464, 133, 535, 149]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[2]: text=内蒙古自治区税务局, bbox=[452, 159, 552, 192]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[3]: text=发票号码：26152000000119478346, bbox=[735, 100, 951, 120]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[4]: text=开票日期：2026年02月09日, bbox=[735, 139, 911, 160]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[5]: text=购买方信息, bbox=[32, 244, 46, 360]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[6]: text=名称, bbox=[59, 260, 84, 280]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[7]: text=统一社会信用代码/纳税人识别号：, bbox=[58, 324, 258, 344]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[8]: text=销售方信息, bbox=[509, 244, 522, 360]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[9]: text=名称：国药控股国大药房内蒙古有限公司, bbox=[537, 255, 802, 277]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[10]: text=统一社会信用代码/纳税人识别号：911501005732872139, bbox=[536, 320, 955, 343]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[11]: text=项目名称, bbox=[77, 380, 136, 400]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[12]: text=规格型号, bbox=[199, 380, 258, 400]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[13]: text=单位, bbox=[320, 380, 364, 400]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[14]: text=数量, bbox=[443, 380, 487, 400]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[15]: text=单价, bbox=[560, 380, 603, 400]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[16]: text=金额, bbox=[682, 380, 725, 400]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[17]: text=税率/征收率, bbox=[746, 380, 828, 400]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[18]: text=税额, bbox=[926, 380, 970, 400]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[19]: text=*化学药品制剂*布地格福, bbox=[26, 405, 188, 428]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[20]: text=160ug:7.2ug/4.8u, bbox=[201, 407, 304, 430]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[21]: text=盒, bbox=[334, 407, 350, 428]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[22]: text=3, bbox=[478, 407, 488, 428]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[23]: text=237.16814159292, bbox=[503, 407, 604, 428]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[24]: text=711.50, bbox=[686, 407, 724, 428]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[25]: text=13%, bbox=[780, 407, 805, 428]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[26]: text=92.50, bbox=[940, 407, 971, 428]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[27]: text=吸入气雾剂, bbox=[26, 436, 101, 459]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[28]: text=g:120揿, bbox=[201, 437, 249, 460]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[29]: text=*化学药品制剂*布地格福, bbox=[26, 467, 188, 490]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[30]: text=160ug:7.2ug/4.8u, bbox=[201, 468, 304, 491]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[31]: text=盒, bbox=[334, 468, 350, 490]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[32]: text=3, bbox=[478, 468, 488, 490]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[33]: text=237.16814159292, bbox=[503, 468, 604, 490]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[34]: text=711.50, bbox=[686, 468, 724, 490]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[35]: text=13%, bbox=[780, 468, 805, 490]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[36]: text=92.50, bbox=[940, 468, 971, 490]
2026-08-10 12:53:16,655 INFO     29 [qwen-vl-text] coord item[37]: text=吸入气雾剂, bbox=[26, 497, 101, 520]
2026-08-10 12:53:16,656 INFO     29 [qwen-vl-text] coord item[38]: text=g:120揿, bbox=[201, 498, 249, 521]
2026-08-10 12:53:16,656 INFO     29 [qwen-vl-text] coord item[39]: text=合计, bbox=[101, 654, 114, 672]
2026-08-10 12:53:16,656 INFO     29 [qwen-vl-text] coord item[40]: text=计, bbox=[175, 654, 188, 672]
2026-08-10 12:53:16,656 INFO     29 [qwen-vl-text] coord item[41]: text=￥1423.00, bbox=[667, 650, 724, 670]
2026-08-10 12:53:16,656 INFO     29 [qwen-vl-text] coord item[42]: text=￥185.00, bbox=[920, 650, 971, 670]
2026-08-10 12:53:16,656 INFO     29 [qwen-vl-text] coord item[43]: text=价税合计（大写）, bbox=[84, 695, 194, 715]
2026-08-10 12:53:16,656 INFO     29 [qwen-vl-text] coord item[44]: text=壹仟陆佰零捌圆整, bbox=[303, 691, 424, 713]
2026-08-10 12:53:16,656 INFO     29 [qwen-vl-text] coord item[45]: text=(小写) ￥1608.00, bbox=[691, 689, 821, 713]
2026-08-10 12:53:16,656 INFO     29 [qwen-vl-text] coord item[46]: text=备注, bbox=[32, 767, 46, 787]
2026-08-10 12:53:16,656 INFO     29 [qwen-vl-text] coord item[47]: text=注, bbox=[32, 807, 46, 827]
2026-08-10 12:53:16,656 INFO     29 [qwen-vl-text] coord item[48]: text=开票人：刘惠, bbox=[95, 898, 185, 920]
2026-08-10 12:53:16,656 INFO     29 [qwen-vl-text] page=5 — 47/47 coords, api_time=23.6s
2026-08-10 12:53:16,656 INFO     29 [qwen-vl-text] new_positions (47):
[[5, 275.334, 538.038, 47.599999999999994, 74.375], [5, 390.688, 450.46999999999997, 79.13499999999999, 88.655], [5, 380.584, 464.784, 94.60499999999999, 114.24], [5, 618.87, 800.742, 59.5, 71.39999999999999], [5, 618.87, 767.062, 82.705, 95.19999999999999], [5, 26.944, 38.732, 145.18, 214.2], [5, 49.678, 70.728, 154.7, 166.6], [5, 48.836, 217.236, 192.78, 204.67999999999998], [5, 428.578, 439.524, 145.18, 214.2], [5, 452.154, 675.284, 151.725, 164.815], [5, 451.312, 804.11, 190.39999999999998, 204.08499999999998], [5, 64.834, 114.512, 226.1, 238.0], [5, 167.558, 217.236, 226.1, 238.0], [5, 269.44, 306.488, 226.1, 238.0], [5, 373.006, 410.054, 226.1, 238.0], [5, 471.52, 507.726, 226.1, 238.0], [5, 574.244, 610.4499999999999, 226.1, 238.0], [5, 628.132, 697.1759999999999, 226.1, 238.0], [5, 779.692, 816.74, 226.1, 238.0], [5, 21.892, 158.296, 240.975, 254.66], [5, 169.242, 255.968, 242.165, 255.85], [5, 281.228, 294.7, 242.165, 254.66], [5, 402.476, 410.89599999999996, 242.165, 254.66], [5, 423.526, 508.568, 242.165, 254.66], [5, 577.612, 609.608, 242.165, 254.66], [5, 656.76, 677.81, 242.165, 254.66], [5, 791.48, 817.582, 242.165, 254.66], [5, 21.892, 85.042, 259.42, 273.10499999999996], [5, 169.242, 209.658, 260.015, 273.7], [5, 21.892, 158.296, 277.865, 291.55], [5, 169.242, 255.968, 278.46, 292.145], [5, 281.228, 294.7, 278.46, 291.55], [5, 402.476, 410.89599999999996, 278.46, 291.55], [5, 423.526, 508.568, 278.46, 291.55], [5, 577.612, 609.608, 278.46, 291.55], [5, 656.76, 677.81, 278.46, 291.55], [5, 791.48, 817.582, 278.46, 291.55], [5, 21.892, 85.042, 295.715, 309.4], [5, 169.242, 209.658, 296.31, 309.995], [5, 85.042, 95.988, 389.13, 399.84], [5, 147.35, 158.296, 389.13, 399.84], [5, 561.614, 609.608, 386.75, 398.65], [5, 774.64, 817.582, 386.75, 398.65], [5, 70.728, 163.34799999999998, 413.525, 425.42499999999995], [5, 255.126, 357.008, 411.145, 424.23499999999996], [5, 581.822, 691.2819999999999, 409.955, 424.23499999999996], [5, 26.944, 38.732, 456.36499999999995, 468.265]]
2026-08-10 12:53:16,656 INFO     29 [qwen-vl-text] ═══ DONE ═══ 47 positions, pages=1, time=27.0s
2026-08-10 12:53:16,670 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 12:53:16,670 INFO     29 [Trace] task=1f69c42a | doc=麦济ZHYH.pdf | Extractor:Medication | outputs={"chunks": "4 items, types={'MedicationRecord': 4}", "html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-10 12:53:16,670 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 12:53:16,671 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:53:16.670+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 34, "failed": 0, "current": {"1f69c42a94ba11f1bd9827cf206dfa2d": {"id": "1f69c42a94ba11f1bd9827cf206dfa2d", "doc_id": "1f30448e94ba11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHYH.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHYH.pdf", "size": 10529265, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786366253712, "task_type": "dataflow", "root_trace_id": "ccbe99209a7f4a07832eb1586b73139c", "root_traceparent": "00-ccbe99209a7f4a07832eb1586b73139c-b8274641f81bf5ac-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:53:16,676 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:53:16,677 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:53:17,521 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:53:17,530 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 12:53:17,530 INFO     29 [Trace] task=1f69c42a | doc=麦济ZHYH.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-10 12:53:17,531 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 12:53:17,537 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:53:17,538 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:53:17,985 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:53:17,991 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 12:53:17,991 INFO     29 [Trace] task=1f69c42a | doc=麦济ZHYH.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-10 12:53:17,991 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 12:53:17,996 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:53:17,996 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:53:18,472 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:53:18,476 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 12:53:18,477 INFO     29 [Trace] task=1f69c42a | doc=麦济ZHYH.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-10 12:53:18,477 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 12:53:18,481 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:53:18,481 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:53:19,629 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:53:19,638 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 12:53:19,638 INFO     29 [Trace] task=1f69c42a | doc=麦济ZHYH.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-10 12:53:19,638 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 12:53:19,644 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:53:19,644 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:53:20,113 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:53:20,118 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 12:53:20,118 INFO     29 [Trace] task=1f69c42a | doc=麦济ZHYH.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-10 12:53:20,118 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 12:53:20,118 INFO     29 [ChunkMerger] Merged 6 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 4, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 7 noise chunks)
2026-08-10 12:53:20,126 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 12:53:20,127 INFO     29 [Trace] task=1f69c42a | doc=麦济ZHYH.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 2, 'MedicationRecord': 4}", "name": "麦济ZHYH.pdf"}
2026-08-10 12:53:20,127 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 12:53:20,174 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786366253924, 'update_date': datetime.datetime(2026, 8, 10, 12, 50, 53), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1005210, 'status': '1'}
2026-08-10 12:53:20,374 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=内蒙古医科大学附属医院门诊病历
姓名：
年龄：62岁
诊疗号：0014498780
民族：
性别：男性
呼吸内科门诊
联系电话：
1
身份证：
病情：
就诊状态：
就诊时间：2026-02-13 09:14
生命体征（需要时）：
体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg
主诉：哮喘史，近3天呼吸困难加重，夜间咳嗽明显
现病史：哮喘史，近3天呼吸困难加重，夜间咳嗽明显
既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎
无，吸烟史无，无过敏史。
体格检查：发育正常，营养良好，体型正常，双肺呼吸音清，双肺未闻及啰
音，双下肢无水肿，体重kg。
辅助检查：心肺
过敏史：不详
初步诊断（西医）：1.支气管哮喘(急性发作期)
初步诊断（中医）：
治疗方案：随诊
醋酸泼尼松片<5mg>
用量：3.000片/次
用法：口服，一次/日，5天
签名：
---
报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录:
病历信息 □痕迹 □批注 置未 ▼ 状态:只读-仅供查看 120% >
内蒙古医科大学附属医院门诊病历
姓名 龄:60岁 诊疗号:0014498780
民族: 别:男性 科室:呼吸内科门诊
联系电话: 身份证:1 病情:
就诊状态: 就诊时间:2024-12-10 12:37
生命体征(需要时):
体温:℃ 脉搏:次/分 呼吸:次/分 血压:/mmHg
主诉:SSSJ项目肺功能检查开单
现病史:哮喘
既往史:患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎
无,吸烟史无,无过敏史。
体格检查:发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰
音,双下肢无水肿,体重kg。
辅助检查:
初步诊断(西医):1.哮喘
初步诊断(中医):
治疗方案:/
呼吸过滤器 肺通气功能检查
用量:
用法:
签名:崔丽英
3:34 星期二 190.1.48.233 版本 王立红
---
萱堂大药房
单号：2025111853212
日期：25/11/18
时间：13:2
工号：001
品名
规格
厂家
金额
数量
总计
布地格福吸入气雾剂
60ug/7.2ug/4.8ug 吸
120 撤/支
支/盒
219.00
3
657.00
合计：657.00
应收：657.00
数量：3
实收：657.00
会员：
药品属于特殊商品
无质量问题，概不退换
---
电子发票(普通发票)
国家税务总局
江苏省税务局
发票号码：25322000000382591347
开票日期：2025年08月20日
购买方信息
名称：
统一社会信用代码/纳税人识别号：
销售方信息
名称：无锡邻医大药房有限公司
统一社会信用代码/纳税人识别号：91320214MA228F680W
项目名称
规格型号
单位
数量
单价
金额
税率/征收率
税额
*化学药品制剂*倍择瑞令
160μg/7.2μg/4
盒
3
210.029498522124
630.09
13%
81.91
畅布地格福吸入气雾剂
.8μg*120揿
合计
￥630.09
￥81.91
价税合计（大写）
柒佰壹拾贰圆整
(小写) ￥712.00
备注
开票人：奚澳琼
---
电子发票(普通发票)
国家税务总局
江苏省税务局
发票号码：25322000000226700883
开票日期：2025年05月20日
购买方信息
名称
统一社会信用代码/纳税人识别号：
销售方信息
名称：无锡邻医大药房有限公司
统一社会信用代码/纳税人识别号：91320214MA228F680W
项目名称
规格型号
单位
数量
单价
金额
税率/征收率
税额
*化学药品制剂*倍择瑞令
160μg/7.2μg/4
盒
3 210.029498522124
630.09
13%
81.91
畅布地格福吸入气雾剂
.8μg*120揿
合计
￥630.09
￥81.91
价税合计（大写）
柒佰壹拾贰圆整
(小写）￥712.00
备注
挂号号:D20091... 医保余额:0 CM/KG 普通病人|现住址:内蒙古土默特左旗沙尔营乡大有庄村32
---
电子发票(普通发票)
国家税务总局
内蒙古自治区税务局
发票号码：26152000000119478346
开票日期：2026年02月09日
购买方信息
名称
统一社会信用代码/纳税人识别号：
销售方信息
名称：国药控股国大药房内蒙古有限公司
统一社会信用代码/纳税人识别号：911501005732872139
项目名称
规格型号
单位
数量
单价
金额
税率/征收率
税额
*化学药品制剂*布地格福
160ug:7.2ug/4.8u
盒
3
237.16814159292
711.50
13%
92.50
吸入气雾剂
g:120揿
*化学药品制剂*布地格福
160ug:7.2ug/4.8u
盒
3
237.16814159292
711.50
13%
92.50
吸入气雾剂
g:120揿
合计
￥1423.00
￥185.00
价税合计（大写）
壹仟陆佰零捌圆整
(小写) ￥1608.00
备注
开票人：刘惠
2026-08-10 12:53:20,712 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 12:53:20,712 INFO     29 [Trace] task=1f69c42a | doc=麦济ZHYH.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 2, 'MedicationRecord': 4}", "name": "麦济ZHYH.pdf", "embedding_token_consumption": 1703}
2026-08-10 12:53:20,712 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 12:53:20,856 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 12:53:20,856 INFO     29 [Trace] task=1f69c42a | doc=麦济ZHYH.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":6,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 12:53:20,859 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:53:20,859 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:53:20,859 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:53:20,860 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:53:20,860 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:53:20,860 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:53:20,863 INFO     29 set_progress(1f69c42a94ba11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 12:53:20 [DOC Engine]:
Start to index...
2026-08-10 12:53:20,878 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.010s]
2026-08-10 12:53:20,882 INFO     29 set_progress(1f69c42a94ba11f1bd9827cf206dfa2d), progress: 0.8166666666666668, progress_msg: 
2026-08-10 12:53:20,893 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.007s]
2026-08-10 12:53:20,899 INFO     29 set_progress(1f69c42a94ba11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 12:53:20 Indexing done (0.04s). Task done (140.22s)
2026-08-10 12:53:20,903 INFO     29 [Done], chunks(6), token(1703), elapsed:140.22
2026-08-10 12:53:20,988 INFO     29 handle_task done for task {"id": "1f69c42a94ba11f1bd9827cf206dfa2d", "doc_id": "1f30448e94ba11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHYH.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHYH.pdf", "size": 10529265, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786366253712, "task_type": "dataflow", "root_trace_id": "ccbe99209a7f4a07832eb1586b73139c", "root_traceparent": "00-ccbe99209a7f4a07832eb1586b73139c-b8274641f81bf5ac-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
