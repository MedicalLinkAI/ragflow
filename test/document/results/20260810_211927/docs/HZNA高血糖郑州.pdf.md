# 基准结果：HZNA高血糖郑州.pdf

## 基本信息

- 文件：`HZNA高血糖郑州.pdf`
- 大小：7407.5 KB
- PDF 总页数：9
- doc_id：`00c2e26894bf11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T21:25:48  完成时间：2026-08-10T21:28:14  耗时：146.2s
- progress_msg：`13:28:13 Indexing done (0.05s). Task done (132.84s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 9099fba1 | 1 | 1-1 | 民医院 出院证 住院号：024 医疗保险证号： 姓名： 性别：男 年龄：37岁  |
| 2 | 2b6c8b7c | 1 | 3-3 | 天医院 门诊患者费用清单(汇总) 证件号:4107251 姓名. 卡号:4 开始 |
| 3 | 00e217ab | 1 | 5-5 | 中心药店 日期: 2025 02 15 19:20:00 销售员: 毛爱青 药品 |
| 4 | 094e0ff5 | 1 | 6-6 | 原阳县人民医院 门诊病历 门诊号：135700000737 姓名： 性别：男 年 |
| 5 | c38657b5 | 1 | 7-7 | 原阳县人民医院处方笺 普通 门诊号：1595205 No： 2504105697 |
| 6 | 7f54e781 | 2 | 8-9 | 原阳县人民医院 姓名： 医保类别：自费 收费时间：2025-04-10 00:0 |
| 7 | 7c45568f | 1 | 4-4 | <table><tr><td>糖化血红蛋白</td><td>HbA1C</td> |
| 8 | 47ee59b2 | 1 | 2-2 | <table><tr><td>糖化血红蛋白</td><td>HbA1C</td> |
| 9 | 4ff6cf7b | 1 | 4-4 | <table><tr><td>随机血糖</td><td>SJXT</td><td |

- chunks 总数：9
- 各 chunk 页数合计（含跨页重复）：10
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9]`
- 覆盖页数：9 / 9；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 1 | 0 | 1 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 1 | 1 | 1 | admission_date, discharge_date, department, outcome | **OK** |
| MedicationRecord | 购药 | 3 | 3 | 3 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 1 | 1 | 1 | encounter_date, prescriber, diagnosis | **OK** |
| ExaminationReport | 检查报告 | 0 | 1 | 0 | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 3 | 0 | 3 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"DischargeRecord": 1, "LabReport": 3, "MedicationRecord": 3, "OutpatientRecord": 1, "PrescriptionRecord": 1}`
- ChunkMerger：`{"found": true, "merged": 9, "sources": 9, "stats": {"Extractor:LabExam": 3, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 3, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 4}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 13:28:12,806 INFO     29 [ChunkMerger] Merged 9 chunks from 9 sources: {'Extractor:LabExam': 3, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 3, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 13:25:53,462 INFO     29 handle_task begin for task {"id": "0108116294bf11f1bd9827cf206dfa2d", "doc_id": "00c2e26894bf11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HZNA\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "type": "pdf", "location": "HZNA\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "size": 7585233, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368350219, "task_type": "dataflow", "root_trace_id": "76162b34ec514c059d062d6d34315295", "root_traceparent": "00-76162b34ec514c059d062d6d34315295-096f88c2095fe0e3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 13:25:53,688 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 13:25:53,801 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 13:25:53,814 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:25:53,814 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 13:25:53,814 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 13:25:53,819 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 13:25:53,819 INFO     29 ============================================================
2026-08-10 13:25:53,819 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 13:25:53,819 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 13:25:53,819 INFO     29 ============================================================
2026-08-10 13:25:53,819 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 13:25:53,819 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 13:25:53,820 INFO     29 No torch found.
2026-08-10 13:25:54,887 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=9
2026-08-10 13:25:54,989 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=723743, prompt_len=764
2026-08-10 13:25:56,390 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-11-24"}
```
2026-08-10 13:25:56,390 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2024-11-24
2026-08-10 13:25:56,401 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=723743, prompt_len=401
2026-08-10 13:25:59,186 INFO     29 [qwen-vl-parser] text API response (len=457):
["民医院", "出院证", "住院号：024", "医疗保险证号：", "姓名：", "性别：男", "年龄：37岁 床号：11床", "籍贯：河南省", "住址：河南省", "+++", "入院时间：2024-11-21 19:58", "出院时间：2024-11-24", "出院诊断：1.社区获得性肺炎，非重症 2.后循环缺血 3.2型糖尿病伴血糖控制不佳 4.冠状动", "脉狭窄 5.脂肪肝 6.甲状腺结节", "出院医嘱：[1.适当运动，控制体重；2.监测血糖，规律服药，二甲双胍缓释片0.5g 1天3次，", "1次1片；依折麦布片10mg 1天1次，1次1片；莫西沙星片0.4g 1天1次，1次1片，肺力咳合剂", "100ml 1天3次，1次10ml(咳", "转停药)；3.戒烟酒，定期复查血脂血糖，肝肾功能，", "避免受凉，不适随诊]", "科二病区医师签名：", "盖章2024-11-24", "达疗业务专用章", "4102251063701", "医院", "扫描全能王 创建"]
2026-08-10 13:25:59,187 INFO     29 [qwen-vl-parser] page=1 text: 24 lines (bbox 0-23)
2026-08-10 13:25:59,187 INFO     29 [qwen-vl-parser] page=1 text: 24 sections
2026-08-10 13:25:59,275 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=620502, prompt_len=764
2026-08-10 13:26:00,716 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2024-11-22"
}
```
2026-08-10 13:26:00,716 INFO     29 [qwen-vl-parser] page=2 classify=table report_date=2024-11-22
2026-08-10 13:26:00,723 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=620502, prompt_len=756
2026-08-10 13:26:01,783 INFO     29 [qwen-vl-parser] table API response (len=161):
\begin{tabular}{ccccccccc}
\hline
序号 & 代号 & 项目名称 & 结果 & 单位 & 参考范围 & 测试方法 & & \\
\hline
1 & HbA1C & 糖化血红蛋白 & 10.20 & ↑ & \% & 4.5--6.5 & & \\
\hline
\end{tabular}
2026-08-10 13:26:01,784 INFO     29 [qwen-vl-parser] page=2 table: 8 LaTeX lines (bbox 24-31)
2026-08-10 13:26:01,785 INFO     29 [qwen-vl-parser] page=2 table: 8 sections
2026-08-10 13:26:01,899 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=928795, prompt_len=764
2026-08-10 13:26:03,354 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 13:26:03,355 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 13:26:03,368 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=928795, prompt_len=401
2026-08-10 13:26:05,050 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:26:05.047+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 49, "failed": 0, "current": {"0108116294bf11f1bd9827cf206dfa2d": {"id": "0108116294bf11f1bd9827cf206dfa2d", "doc_id": "00c2e26894bf11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HZNA\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "type": "pdf", "location": "HZNA\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "size": 7585233, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368350219, "task_type": "dataflow", "root_trace_id": "76162b34ec514c059d062d6d34315295", "root_traceparent": "00-76162b34ec514c059d062d6d34315295-096f88c2095fe0e3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:26:07,182 INFO     29 [qwen-vl-parser] text API response (len=369):
["天医院", "门诊患者费用清单(汇总)", "证件号:4107251", "姓名.", "卡号:4", "开始时间: 2025-01-01 00:00", "结束时间: 2025-03-13:59", "项目名称 单价 单位 数量 金额", "-g3盐酸二甲双胍缓释", ".086 片 64.0 5.50", "片", "病历资料复印 0.4 每张 26.0 10.40", "糖化血红蛋白全定量 256 项 1.00 25.00", "测定", "静脉注射 3.8 次 1.00 3.80", "血糖测定 6 次 1.00 6.00", "共计:5项 金额合计:¥50.70", "打印时间:2025-03-13 10:13:36", "操作员.", "扫描二维码下载电子发票", "此单据作为就诊凭证,请不要随意丢弃", ""]
2026-08-10 13:26:07,182 INFO     29 [qwen-vl-parser] page=3 text: 21 lines (bbox 32-52)
2026-08-10 13:26:07,182 INFO     29 [qwen-vl-parser] page=3 text: 21 sections
2026-08-10 13:26:07,283 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=617714, prompt_len=764
2026-08-10 13:26:08,727 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-02-26"
}
```
2026-08-10 13:26:08,728 INFO     29 [qwen-vl-parser] page=4 classify=table report_date=2025-02-26
2026-08-10 13:26:08,753 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=617714, prompt_len=756
2026-08-10 13:26:10,340 INFO     29 [qwen-vl-parser] table API response (len=298):
\begin{tabular}{llllllll}
\hline
序号 & 代号 & 项目名称 & 结果 & 单位 & 参考范围 & & \\
\hline
1 & SJXT & 随机血糖 & 16.37 & mmol/L & & & \\
\hline
\end{tabular}

\begin{tabular}{llllllll}
\hline
序号 & 代号 & 项目名称 & 结果 & 单位 & 参考范围 & & 测试方法 \\
\hline
1 & HbA1C & 糖化血红蛋白 & 9.10 & ↑ \% & 4.5--6.5 & & \\
\hline
\end{tabular}
2026-08-10 13:26:10,342 INFO     29 [qwen-vl-parser] page=4 table: 16 LaTeX lines (bbox 53-68)
2026-08-10 13:26:10,343 INFO     29 [qwen-vl-parser] page=4 table: 16 sections
2026-08-10 13:26:10,432 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=575252, prompt_len=764
2026-08-10 13:26:11,683 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:26:11,684 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 13:26:11,697 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=575252, prompt_len=401
2026-08-10 13:26:13,986 INFO     29 [qwen-vl-parser] text API response (len=385):
["中心药店", "日期: 2025 02 15 19:20:00", "销售员: 毛爱青", "药品名称", "生产厂商", "批号", "规格", "数量", "单位", "单价", "金额", "盐酸二甲双胍肠溶片", "贵州天安药业股份有限公司", "20240242", "0.5g/60", "3.00", "瓶", "20.00", "60.00", "应收 60.00 实收 60.00", "找回 0.00 中药付 1.00", "地址: 原阳县西干道", "电话: 7282955", "会员卡: ", "本次积分: 60", "积分余额: 260", "原额: 0.00", "余额: 0", "药品为特殊商品无质量问题", "概不退换", "社会主核心价值观", "富强 民主 文明 和谐", "自由 平等 公正 法治", "扫描全能王 创建"]
2026-08-10 13:26:13,987 INFO     29 [qwen-vl-parser] page=5 text: 34 lines (bbox 69-102)
2026-08-10 13:26:13,987 INFO     29 [qwen-vl-parser] page=5 text: 34 sections
2026-08-10 13:26:14,099 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=861363, prompt_len=764
2026-08-10 13:26:15,464 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:26:15,465 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-10 13:26:15,477 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=861363, prompt_len=401
2026-08-10 13:26:18,605 INFO     29 [qwen-vl-parser] text API response (len=538):
["原阳县人民医院", "门诊病历", "门诊号：135700000737", "姓名：", "性别：男", "年龄：37岁", "婚否：已婚", "民族：汉族", "职业：工人", "身份证号：", "邮编：453500", "籍贯：河南省新乡市", "现住址：河南省新乡市", "X线号：", "工作单位：", "联系电", "心电图号：", "初诊科别：内分泌科门诊", "初诊日期：2025-02-25", "过敏史：无", "主诉：发现血糖高半年余", "现病史：半年前发现血糖高，空腹血糖13mmol/L，平时口服二甲双胍片0.5g 每日三次，", "监测空腹及餐后血糖仍高，门诊就诊。", "既往史：既往体健，无肝炎、结核、疟疾病史，无高血压、心脏疾病病史，无手术、外", "伤、输血史", "婚育史：已婚。", "家族史：无家族性遗传病史。", "体格检查：BMI：38Kg/m²神志清，精神可，体型肥胖，心肺听诊无明显异常，双下肢无水肿", "辅助检查：血糖 糖化", "门诊诊断：", "1、2型糖尿病", "门诊处置：无", "诊疗意见:药物治疗、如有不适，请随时复诊", "医师签名：胡志环", "签名日期：2025-04-10 10:34", ""]
2026-08-10 13:26:18,606 INFO     29 [qwen-vl-parser] page=6 text: 35 lines (bbox 103-137)
2026-08-10 13:26:18,607 INFO     29 [qwen-vl-parser] page=6 text: 35 sections
2026-08-10 13:26:18,700 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=502735, prompt_len=764
2026-08-10 13:26:19,929 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:26:19,929 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-10 13:26:19,941 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=502735, prompt_len=401
2026-08-10 13:26:21,916 INFO     29 [qwen-vl-parser] text API response (len=329):
["原阳县人民医院处方笺", "普通", "门诊号：1595205", "No： 2504105697228", "姓名：.", "性别：男", "年龄：37岁", "科别：内分泌科门诊", "交易号：1053179", "费别：自费", "日期：2025-04-10 10:33:39.0", "地址：河南省原阳县河南省新乡市原阳县", "诊断：2型糖尿病", "慢性病长期用药", "Rp:", "-g3盐酸二甲双胍片（0.25g*60片）", "6瓶", "用法：0.5g", "一日三次", "口服", "审核：吴汉铺", "核对：吴汉铺", "医师：胡光环", "调配：吴汉铺", "发药：吴汉铺", "药费：13.38", "扫描全能王 创建"]
2026-08-10 13:26:21,917 INFO     29 [qwen-vl-parser] page=7 text: 27 lines (bbox 138-164)
2026-08-10 13:26:21,917 INFO     29 [qwen-vl-parser] page=7 text: 27 sections
2026-08-10 13:26:22,039 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=838135, prompt_len=764
2026-08-10 13:26:23,292 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:26:23,293 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-10 13:26:23,308 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=838135, prompt_len=401
2026-08-10 13:26:25,110 INFO     29 [qwen-vl-parser] text API response (len=277):
["原阳县人民医院", "姓名：", "医保类别：自费", "收费时间：2025-04-10 00:00:00", "发票号：41060135H1005655423门诊号：1595205", "患者卡号：410725198706033639", "费用分类", "西药费", "13.38", "金额：壹拾叁圆叁角捌分", "13.38", "现金：0", "账户：13.38", "银联卡：0", "医保账户：0.0", "医保统筹：0.0", "个人自付：0.0", "支付宝：0", "微信：0", "账户余额：0", "医保账户余额：", ""]
2026-08-10 13:26:25,110 INFO     29 [qwen-vl-parser] page=8 text: 21 lines (bbox 165-185)
2026-08-10 13:26:25,112 INFO     29 [qwen-vl-parser] page=8 text: 21 sections
2026-08-10 13:26:25,227 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=905506, prompt_len=764
2026-08-10 13:26:26,601 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:26:26,602 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-10 13:26:26,616 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=905506, prompt_len=401
2026-08-10 13:26:28,486 INFO     29 [qwen-vl-parser] text API response (len=261):
["原阳县人民医院", "门诊患者费用清单", "卡号：410725198706033639 账户余额：0", "姓名：", "流水号：1595205", "开始时间：2025-04-10 10:33", "结束时间：2025-04-10 10:33", "项目名称", "单价", "单位", "数量", "金额", "-g3盐酸二甲双胍片", "3.60", "60", "13.38", "共计：1项", "金额合计：13.38", "打印时间：2025-04-22 16:36:16", "操作员：赵彤", ""]
2026-08-10 13:26:28,487 INFO     29 [qwen-vl-parser] page=9 text: 20 lines (bbox 186-205)
2026-08-10 13:26:28,487 INFO     29 [qwen-vl-parser] page=9 text: 20 sections
2026-08-10 13:26:28,487 INFO     29 [qwen-vl-parser] parse_pdf done: 206 sections from 9 pages.
2026-08-10 13:26:28,499 INFO     29 Close text detector.
2026-08-10 13:26:28,935 INFO     29 Close text recognizer.
2026-08-10 13:26:29,326 INFO     29 Close recognizer.
2026-08-10 13:26:29,749 INFO     29 Close recognizer.
2026-08-10 13:26:30,200 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 13:26:30,200 INFO     29 [Trace] task=01081162 | doc=HZNA高血糖郑州.pdf | Parser:MedLink | outputs={"html": "", "json": "206 items", "markdown": "", "text": "", "name": "HZNA高血糖郑州.pdf", "output_format": "json"}
2026-08-10 13:26:30,200 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 13:26:30,216 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:26:30,216 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 民医院\n[BBOX-1] 出院证\n[BBOX-2] 住院号：024\n[BBOX-3] 医疗保险证号：\n[BBOX-4] 姓名：\n[BBOX-5] 性别：男\n[BBOX-6] 年龄：37岁 床号：11床\n[BBOX-7] 籍贯：河南省\n[BBOX-8] 住址：河南省\n[BBOX-9] 入院时间：2024-11-21 19:58\n[BBOX-10] 出院时间：2024-11-24\n[BBOX-11] 出院诊断：1.社区获得性肺炎，非重症 2.后循环缺血 3.2型糖尿病伴血糖控制不佳 4.冠状动\n[BBOX-12] 脉狭窄 5.脂肪肝 6.甲状腺结节\n[BBOX-13] 出院医嘱：[1.适当运动，控制体重；2.监测血糖，规律服药，二甲双胍缓释片0.5g 1天3次，\n[BBOX-14] 1次1片；依折麦布片10mg 1天1次，1次1片；莫西沙星片0.4g 1天1次，1次1片，肺力咳合剂\n[BBOX-15] 100ml 1天3次，1次10ml(咳\n[BBOX-16] 转停药)；3.戒烟酒，定期复查血脂血糖，肝肾功能，\n[BBOX-17] 避免受凉，不适随诊]\n[BBOX-18] 科二病区医师签名：\n[BBOX-19] 盖章2024-11-24\n[BBOX-20] 达疗业务专用章\n[BBOX-21] 4102251063701\n[BBOX-22] 医院\n[BBOX-23] 扫描全能王 创建\n[BBOX-24] \\begin{tabular}{ccccccccc}\n[BBOX-25] 报告时间: 2024-11-22\n[BBOX-26] \\hline\n[BBOX-27] 序号 & 代号 & 项目名称 & 结果 & 单位 & 参考范围 & 测试方法 & & \\\\\n[BBOX-28] \\hline\n[BBOX-29] 1 & HbA1C & 糖化血红蛋白 & 10.20 & ↑ & \\% & 4.5--6.5 & & \\\\\n[BBOX-30] \\hline\n[BBOX-31] \\end{tabular}\n[BBOX-32] 天医院\n[BBOX-33] 门诊患者费用清单(汇总)\n[BBOX-34] 证件号:4107251\n[BBOX-35] 姓名.\n[BBOX-36] 卡号:4\n[BBOX-37] 开始时间: 2025-01-01 00:00\n[BBOX-38] 结束时间: 2025-03-13:59\n[BBOX-39] 项目名称 单价 单位 数量 金额\n[BBOX-40] -g3盐酸二甲双胍缓释\n[BBOX-41] .086 片 64.0 5.50\n[BBOX-42] 片\n[BBOX-43] 病历资料复印 0.4 每张 26.0 10.40\n[BBOX-44] 糖化血红蛋白全定量 256 项 1.00 25.00\n[BBOX-45] 测定\n[BBOX-46] 静脉注射 3.8 次 1.00 3.80\n[BBOX-47] 血糖测定 6 次 1.00 6.00\n[BBOX-48] 共计:5项 金额合计:¥50.70\n[BBOX-49] 打印时间:2025-03-13 10:13:36\n[BBOX-50] 操作员.\n[BBOX-51] 扫描二维码下载电子发票\n[BBOX-52] 此单据作为就诊凭证,请不要随意丢弃\n[BBOX-53] \\begin{tabular}{llllllll}\n[BBOX-54] 报告时间: 2025-02-26\n[BBOX-55] \\hline\n[BBOX-56] 序号 & 代号 & 项目名称 & 结果 & 单位 & 参考范围 & & \\\\\n[BBOX-57] \\hline\n[BBOX-58] 1 & SJXT & 随机血糖 & 16.37 & mmol/L & & & \\\\\n[BBOX-59] \\hline\n[BBOX-60] \\end{tabular}\n[BBOX-61] \\begin{tabular}{llllllll}\n[BBOX-62] 报告时间: 2025-02-26\n[BBOX-63] \\hline\n[BBOX-64] 序号 & 代号 & 项目名称 & 结果 & 单位 & 参考范围 & & 测试方法 \\\\\n[BBOX-65] \\hline\n[BBOX-66] 1 & HbA1C & 糖化血红蛋白 & 9.10 & ↑ \\% & 4.5--6.5 & & \\\\\n[BBOX-67] \\hline\n[BBOX-68] \\end{tabular}\n[BBOX-69] 中心药店\n[BBOX-70] 日期: 2025 02 15 19:20:00\n[BBOX-71] 销售员: 毛爱青\n[BBOX-72] 药品名称\n[BBOX-73] 生产厂商\n[BBOX-74] 批号\n[BBOX-75] 规格\n[BBOX-76] 数量\n[BBOX-77] 单位\n[BBOX-78] 单价\n[BBOX-79] 金额\n[BBOX-80] 盐酸二甲双胍肠溶片\n[BBOX-81] 贵州天安药业股份有限公司\n[BBOX-82] 20240242\n[BBOX-83] 0.5g/60\n[BBOX-84] 3.00\n[BBOX-85] 瓶\n[BBOX-86] 20.00\n[BBOX-87] 60.00\n[BBOX-88] 应收 60.00 实收 60.00\n[BBOX-89] 找回 0.00 中药付 1.00\n[BBOX-90] 地址: 原阳县西干道\n[BBOX-91] 电话: 7282955\n[BBOX-92] 会员卡:\n[BBOX-93] 本次积分: 60\n[BBOX-94] 积分余额: 260\n[BBOX-95] 原额: 0.00\n[BBOX-96] 余额: 0\n[BBOX-97] 药品为特殊商品无质量问题\n[BBOX-98] 概不退换\n[BBOX-99] 社会主核心价值观\n[BBOX-100] 富强 民主 文明 和谐\n[BBOX-101] 自由 平等 公正 法治\n[BBOX-102] 扫描全能王 创建\n[BBOX-103] 原阳县人民医院\n[BBOX-104] 门诊病历\n[BBOX-105] 门诊号：135700000737\n[BBOX-106] 姓名：\n[BBOX-107] 性别：男\n[BBOX-108] 年龄：37岁\n[BBOX-109] 婚否：已婚\n[BBOX-110] 民族：汉族\n[BBOX-111] 职业：工人\n[BBOX-112] 身份证号：\n[BBOX-113] 邮编：453500\n[BBOX-114] 籍贯：河南省新乡市\n[BBOX-115] 现住址：河南省新乡市\n[BBOX-116] X线号：\n[BBOX-117] 工作单位：\n[BBOX-118] 联系电\n[BBOX-119] 心电图号：\n[BBOX-120] 初诊科别：内分泌科门诊\n[BBOX-121] 初诊日期：2025-02-25\n[BBOX-122] 过敏史：无\n[BBOX-123] 主诉：发现血糖高半年余\n[BBOX-124] 现病史：半年前发现血糖高，空腹血糖13mmol/L，平时口服二甲双胍片0.5g 每日三次，\n[BBOX-125] 监测空腹及餐后血糖仍高，门诊就诊。\n[BBOX-126] 既往史：既往体健，无肝炎、结核、疟疾病史，无高血压、心脏疾病病史，无手术、外\n[BBOX-127] 伤、输血史\n[BBOX-128] 婚育史：已婚。\n[BBOX-129] 家族史：无家族性遗传病史。\n[BBOX-130] 体格检查：BMI：38Kg/m²神志清，精神可，体型肥胖，心肺听诊无明显异常，双下肢无水肿\n[BBOX-131] 辅助检查：血糖 糖化\n[BBOX-132] 门诊诊断：\n[BBOX-133] 1、2型糖尿病\n[BBOX-134] 门诊处置：无\n[BBOX-135] 诊疗意见:药物治疗、如有不适，请随时复诊\n[BBOX-136] 医师签名：胡志环\n[BBOX-137] 签名日期：2025-04-10 10:34\n[BBOX-138] 原阳县人民医院处方笺\n[BBOX-139] 普通\n[BBOX-140] 门诊号：1595205\n[BBOX-141] No： 2504105697228\n[BBOX-142] 姓名：.\n[BBOX-143] 性别：男\n[BBOX-144] 年龄：37岁\n[BBOX-145] 科别：内分泌科门诊\n[BBOX-146] 交易号：1053179\n[BBOX-147] 费别：自费\n[BBOX-148] 日期：2025-04-10 10:33:39.0\n[BBOX-149] 地址：河南省原阳县河南省新乡市原阳县\n[BBOX-150] 诊断：2型糖尿病\n[BBOX-151] 慢性病长期用药\n[BBOX-152] Rp:\n[BBOX-153] -g3盐酸二甲双胍片（0.25g*60片）\n[BBOX-154] 6瓶\n[BBOX-155] 用法：0.5g\n[BBOX-156] 一日三次\n[BBOX-157] 口服\n[BBOX-158] 审核：吴汉铺\n[BBOX-159] 核对：吴汉铺\n[BBOX-160] 医师：胡光环\n[BBOX-161] 调配：吴汉铺\n[BBOX-162] 发药：吴汉铺\n[BBOX-163] 药费：13.38\n[BBOX-164] 扫描全能王 创建\n[BBOX-165] 原阳县人民医院\n[BBOX-166] 姓名：\n[BBOX-167] 医保类别：自费\n[BBOX-168] 收费时间：2025-04-10 00:00:00\n[BBOX-169] 发票号：41060135H1005655423门诊号：1595205\n[BBOX-170] 患者卡号：410725198706033639\n[BBOX-171] 费用分类\n[BBOX-172] 西药费\n[BBOX-173] 13.38\n[BBOX-174] 金额：壹拾叁圆叁角捌分\n[BBOX-175] 13.38\n[BBOX-176] 现金：0\n[BBOX-177] 账户：13.38\n[BBOX-178] 银联卡：0\n[BBOX-179] 医保账户：0.0\n[BBOX-180] 医保统筹：0.0\n[BBOX-181] 个人自付：0.0\n[BBOX-182] 支付宝：0\n[BBOX-183] 微信：0\n[BBOX-184] 账户余额：0\n[BBOX-185] 医保账户余额：\n[BBOX-186] 原阳县人民医院\n[BBOX-187] 门诊患者费用清单\n[BBOX-188] 卡号：410725198706033639 账户余额：0\n[BBOX-189] 姓名：\n[BBOX-190] 流水号：1595205\n[BBOX-191] 开始时间：2025-04-10 10:33\n[BBOX-192] 结束时间：2025-04-10 10:33\n[BBOX-193] 项目名称\n[BBOX-194] 单价\n[BBOX-195] 单位\n[BBOX-196] 数量\n[BBOX-197] 金额\n[BBOX-198] -g3盐酸二甲双胍片\n[BBOX-199] 3.60\n[BBOX-200] 60\n[BBOX-201] 13.38\n[BBOX-202] 共计：1项\n[BBOX-203] 金额合计：13.38\n[BBOX-204] 打印时间：2025-04-22 16:36:16\n[BBOX-205] 操作员：赵彤"
  }
]
2026-08-10 13:26:36,519 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:26:36.519+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 49, "failed": 0, "current": {"0108116294bf11f1bd9827cf206dfa2d": {"id": "0108116294bf11f1bd9827cf206dfa2d", "doc_id": "00c2e26894bf11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HZNA\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "type": "pdf", "location": "HZNA\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "size": 7585233, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368350219, "task_type": "dataflow", "root_trace_id": "76162b34ec514c059d062d6d34315295", "root_traceparent": "00-76162b34ec514c059d062d6d34315295-096f88c2095fe0e3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:26:39,801 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:26:39,814 INFO     29 [SmartSplitter] SmartSplitter done: 9 chunks from 9 LLM segments (all bbox_id). Types: {'DischargeRecord': 1, 'LabReport': 3, 'MedicationRecord': 3, 'OutpatientRecord': 1, 'PrescriptionRecord': 1}
2026-08-10 13:26:39,821 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 13:26:39,821 INFO     29 [Trace] task=01081162 | doc=HZNA高血糖郑州.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "206 items", "markdown": "", "text": "", "name": "HZNA高血糖郑州.pdf", "output_format": "chunks", "chunks": "9 items, types={'DischargeRecord': 1, 'LabReport': 3, 'MedicationRecord': 3, 'OutpatientRecord': 1, 'PrescriptionRecord': 1}"}
2026-08-10 13:26:39,821 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 13:26:39,822 INFO     29 [ChunkRouter] Routed 9 chunks into 5 groups: {'chunks_Discharge': 1, 'chunks_LabExam': 3, 'chunks_Medication': 3, 'chunks_Clinical': 1, 'chunks_Prescription': 1}
2026-08-10 13:26:39,828 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 13:26:39,829 INFO     29 [Trace] task=01081162 | doc=HZNA高血糖郑州.pdf | ChunkRouter:Router | outputs={"html": "", "json": "206 items", "markdown": "", "text": "", "name": "HZNA高血糖郑州.pdf", "output_format": "chunks", "chunks": "9 items, types={'DischargeRecord': 1, 'LabReport': 3, 'MedicationRecord': 3, 'OutpatientRecord': 1, 'PrescriptionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_LabExam\": 3, \"chunks_Medication\": 3, \"chunks_Clinical\": 1, \"chunks_Prescription\": 1}"}
2026-08-10 13:26:39,829 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 13:26:39,833 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:26:39,833 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:26:39,833 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[1]
2026-08-10 13:26:39,833 INFO     29 [qwen-vl-table] positions ： [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:26:40,001 INFO     29 [qwen-vl-table] page=1, rect=842x595, img=(2339x1653)
2026-08-10 13:26:40,002 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:26:40,002 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 24, \"bbox_end\": 31, \"encounter_dates\": [\"2024-11-22\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2024-11-22\n\\hline\n序号 & 代号 & 项目名称 & 结果 & 单位 & 参考范围 & 测试方法 & & \\\\\n\\hline\n1 & HbA1C & 糖化血红蛋白 & 10.20 & ↑ & \\% & 4.5--6.5 & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:26:41,253 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:26:41,253 INFO     29 [qwen-vl-table] page=1 LLM output (len=218):
{
  "report_date": "2024-11-22",
  "items": [
    {
      "name": "糖化血红蛋白",
      "item_code": "HbA1C",
      "value": "10.20",
      "unit": "%",
      "reference_range": "4.5--6.5",
      "abnormal": true
    }
  ]
}
2026-08-10 13:26:41,253 INFO     29 [qwen-vl-table] coord grouping: {1: 1}
2026-08-10 13:26:41,254 INFO     29 [qwen-vl-table] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=594605, prompt_len=513
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
糖化血红蛋白

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
2026-08-10 13:26:42,715 INFO     29 [qwen-vl-table] coord API raw response (len=65):
```json
[
	{"text": "糖化血红蛋白", "bbox": [227, 271, 306, 289]}
]
```
2026-08-10 13:26:42,715 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=1.5s
2026-08-10 13:26:42,715 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白, bbox=[227, 271, 306, 289]
2026-08-10 13:26:42,716 INFO     29 [qwen-vl-table] page=1 coord: matched 1/1, time=1.5s
2026-08-10 13:26:42,716 INFO     29 [qwen-vl-table] new_positions (1):
[[2, 191.134, 257.652, 161.245, 171.95499999999998]]
2026-08-10 13:26:42,716 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=2.9s
2026-08-10 13:26:42,717 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:26:42,719 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:26:42,719 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[3]
2026-08-10 13:26:42,719 INFO     29 [qwen-vl-table] positions ： [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:26:42,903 INFO     29 [qwen-vl-table] page=3, rect=595x842, img=(1653x2339)
2026-08-10 13:26:42,904 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:26:42,904 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 53, \"bbox_end\": 60, \"encounter_dates\": [\"2025-02-26\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllll}\n报告时间: 2025-02-26\n\\hline\n序号 & 代号 & 项目名称 & 结果 & 单位 & 参考范围 & & \\\\\n\\hline\n1 & SJXT & 随机血糖 & 16.37 & mmol/L & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:26:44,009 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:26:44,009 INFO     29 [qwen-vl-table] page=3 LLM output (len=215):
{
  "report_date": "2025-02-26",
  "items": [
    {
      "name": "随机血糖",
      "item_code": "SJXT",
      "value": "16.37",
      "unit": "mmol/L",
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 13:26:44,010 INFO     29 [qwen-vl-table] coord grouping: {3: 1}
2026-08-10 13:26:44,011 INFO     29 [qwen-vl-table] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=541819, prompt_len=511
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
随机血糖

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
2026-08-10 13:26:45,424 INFO     29 [qwen-vl-table] coord API raw response (len=63):
```json
[
	{"text": "随机血糖", "bbox": [191, 124, 257, 135]}
]
```
2026-08-10 13:26:45,425 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=1.4s
2026-08-10 13:26:45,425 INFO     29 [qwen-vl-table] coord item[0]: text=随机血糖, bbox=[191, 124, 257, 135]
2026-08-10 13:26:45,425 INFO     29 [qwen-vl-table] page=3 coord: matched 1/1, time=1.4s
2026-08-10 13:26:45,426 INFO     29 [qwen-vl-table] new_positions (1):
[[4, 113.645, 152.915, 104.408, 113.67]]
2026-08-10 13:26:45,426 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=2.7s
2026-08-10 13:26:45,428 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:26:45,430 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:26:45,430 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[3]
2026-08-10 13:26:45,431 INFO     29 [qwen-vl-table] positions ： [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:26:45,606 INFO     29 [qwen-vl-table] page=3, rect=595x842, img=(1653x2339)
2026-08-10 13:26:45,607 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:26:45,607 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 61, \"bbox_end\": 68, \"encounter_dates\": [\"2025-02-26\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllll}\n报告时间: 2025-02-26\n\\hline\n序号 & 代号 & 项目名称 & 结果 & 单位 & 参考范围 & & 测试方法 \\\\\n\\hline\n1 & HbA1C & 糖化血红蛋白 & 9.10 & ↑ \\% & 4.5--6.5 & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:26:46,768 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:26:46,769 INFO     29 [qwen-vl-table] page=3 LLM output (len=217):
{
  "report_date": "2025-02-26",
  "items": [
    {
      "name": "糖化血红蛋白",
      "item_code": "HbA1C",
      "value": "9.10",
      "unit": "%",
      "reference_range": "4.5--6.5",
      "abnormal": true
    }
  ]
}
2026-08-10 13:26:46,769 INFO     29 [qwen-vl-table] coord grouping: {3: 1}
2026-08-10 13:26:46,770 INFO     29 [qwen-vl-table] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=541819, prompt_len=513
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
糖化血红蛋白

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
2026-08-10 13:26:47,370 INFO     29 [qwen-vl-table] coord API raw response (len=65):
```json
[
	{"text": "糖化血红蛋白", "bbox": [176, 604, 267, 616]}
]
```
2026-08-10 13:26:47,371 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=0.6s
2026-08-10 13:26:47,371 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白, bbox=[176, 604, 267, 616]
2026-08-10 13:26:47,371 INFO     29 [qwen-vl-table] page=3 coord: matched 1/1, time=0.6s
2026-08-10 13:26:47,372 INFO     29 [qwen-vl-table] new_positions (1):
[[4, 104.72, 158.86499999999998, 508.568, 518.672]]
2026-08-10 13:26:47,372 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=1.9s
2026-08-10 13:26:47,382 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 13:26:47,382 INFO     29 [Trace] task=01081162 | doc=HZNA高血糖郑州.pdf | Extractor:LabExam | outputs={"chunks": "3 items, types={'LabReport': 3}", "html": "", "json": "206 items", "markdown": "", "text": "", "name": "HZNA高血糖郑州.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_LabExam\": 3, \"chunks_Medication\": 3, \"chunks_Clinical\": 1, \"chunks_Prescription\": 1}"}
2026-08-10 13:26:47,383 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 13:26:47,388 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:26:47,388 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:26:47,787 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:26:47,793 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 13:26:47,793 INFO     29 [Trace] task=01081162 | doc=HZNA高血糖郑州.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "206 items", "markdown": "", "text": "", "name": "HZNA高血糖郑州.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_LabExam\": 3, \"chunks_Medication\": 3, \"chunks_Clinical\": 1, \"chunks_Prescription\": 1}"}
2026-08-10 13:26:47,794 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 13:26:47,800 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:26:47,801 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:26:47,801 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 13:26:47,801 INFO     29 [qwen-vl-text] positions(35): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:26:47,801 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [35]
2026-08-10 13:26:47,983 INFO     29 [qwen-vl-text] page=5, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:26:47,984 INFO     29 [qwen-vl-text] LLM extraction start, text_len=428
2026-08-10 13:26:47,984 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:26:47,985 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 103, \"bbox_end\": 137, \"encounter_dates\": [\"2025-02-25\"], \"department\": \"内分泌科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "原阳县人民医院\n门诊病历\n门诊号：135700000737\n姓名：\n性别：男\n年龄：37岁\n婚否：已婚\n民族：汉族\n职业：工人\n身份证号：\n邮编：453500\n籍贯：河南省新乡市\n现住址：河南省新乡市\nX线号：\n工作单位：\n联系电\n心电图号：\n初诊科别：内分泌科门诊\n初诊日期：2025-02-25\n过敏史：无\n主诉：发现血糖高半年余\n现病史：半年前发现血糖高，空腹血糖13mmol/L，平时口服二甲双胍片0.5g 每日三次，\n监测空腹及餐后血糖仍高，门诊就诊。\n既往史：既往体健，无肝炎、结核、疟疾病史，无高血压、心脏疾病病史，无手术、外\n伤、输血史\n婚育史：已婚。\n家族史：无家族性遗传病史。\n体格检查：BMI：38Kg/m²神志清，精神可，体型肥胖，心肺听诊无明显异常，双下肢无水肿\n辅助检查：血糖 糖化\n门诊诊断：\n1、2型糖尿病\n门诊处置：无\n诊疗意见:药物治疗、如有不适，请随时复诊\n医师签名：胡志环\n签名日期：2025-04-10 10:34",
    "role": "user"
  }
]
2026-08-10 13:26:49,680 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:26:49,680 INFO     29 [qwen-vl-text] LLM output (len=278):
{
  "encounter_date": "2025-02-25",
  "chief_complaint": "发现血糖高半年余",
  "present_illness": "半年前发现血糖高，空腹血糖13mmol/L，平时口服二甲双胍片0.5g 每日三次，监测空腹及餐后血糖仍高，门诊就诊。",
  "past_history": "既往体健，无肝炎、结核、疟疾病史，无高血压、心脏疾病病史，无手术、外伤、输血史",
  "diagnosis": "1、2型糖尿病",
  "treatment_plan": "药物治疗、如有不适，请随时复诊"
}
2026-08-10 13:26:49,680 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-02-25]
2026-08-10 13:26:49,682 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=817074, prompt_len=1146
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["原阳县人民医院", "门诊病历", "门诊号：135700000737", "姓名：", "性别：男", "年龄：37岁", "婚否：已婚", "民族：汉族", "职业：工人", "身份证号：", "邮编：453500", "籍贯：河南省新乡市", "现住址：河南省新乡市", "X线号：", "工作单位：", "联系电", "心电图号：", "初诊科别：内分泌科门诊", "初诊日期：2025-02-25", "过敏史：无", "主诉：发现血糖高半年余", "现病史：半年前发现血糖高，空腹血糖13mmol/L，平时口服二甲双胍片0.5g 每日三次，", "监测空腹及餐后血糖仍高，门诊就诊。", "既往史：既往体健，无肝炎、结核、疟疾病史，无高血压、心脏疾病病史，无手术、外", "伤、输血史", "婚育史：已婚。", "家族史：无家族性遗传病史。", "体格检查：BMI：38Kg/m²神志清，精神可，体型肥胖，心肺听诊无明显异常，双下肢无水肿", "辅助检查：血糖 糖化", "门诊诊断：", "1、2型糖尿病", "门诊处置：无", "诊疗意见:药物治疗、如有不适，请随时复诊", "医师签名：胡志环", "签名日期：2025-04-10 10:34"]

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
2026-08-10 13:27:00,295 INFO     29 [qwen-vl-text] coord API raw response (len=1985):
[
	{"text": "原阳县人民医院", "bbox": [368, 31, 616, 59]},
	{"text": "门诊病历", "bbox": [426, 72, 564, 98]},
	{"text": "门诊号：135700000737", "bbox": [730, 106, 909, 118]},
	{"text": "姓名：", "bbox": [91, 134, 141, 149]},
	{"text": "性别：男", "bbox": [254, 134, 337, 149]},
	{"text": "年龄：37岁", "bbox": [418, 134, 517, 149]},
	{"text": "婚否：已婚", "bbox": [579, 134, 685, 149]},
	{"text": "民族：汉族", "bbox": [749, 134, 851, 149]},
	{"text": "职业：工人", "bbox": [91, 162, 193, 177]},
	{"text": "身份证号：", "bbox": [366, 162, 454, 177]},
	{"text": "41", "bbox": [366, 188, 398, 197]},
	{"text": "39", "bbox": [525, 190, 547, 201]},
	{"text": "籍贯：河南省新乡市", "bbox": [91, 216, 275, 231]},
	{"text": "现住址：河南省新乡市", "bbox": [366, 216, 565, 231]},
	{"text": "县", "bbox": [366, 243, 386, 258]},
	{"text": "工作单位：", "bbox": [91, 271, 180, 286]},
	{"text": "联系电", "bbox": [366, 271, 425, 286]},
	{"text": "心电图号：", "bbox": [638, 269, 727, 285]},
	{"text": "初诊科别：内分泌科门诊", "bbox": [91, 300, 317, 315]},
	{"text": "初诊日期：2025-02-25", "bbox": [366, 300, 568, 315]},
	{"text": "过敏史：无", "bbox": [637, 299, 742, 314]},
	{"text": "主诉：发现血糖高半年余", "bbox": [87, 328, 334, 344]},
	{"text": "现病史：半年前发现血糖高，空腹血糖13mmol/L，平时口服二甲双胍片0.5g 每日三次，", "bbox": [87, 357, 872, 373]},
	{"text": "监测空腹及餐后血糖仍高，门诊就诊。", "bbox": [87, 386, 423, 402]},
	{"text": "既往史：既往体健，无肝炎、结核、疟疾病史，无高血压、心脏疾病病史，无手术、外", "bbox": [87, 414, 864, 430]},
	{"text": "伤、输血史", "bbox": [87, 443, 188, 459]},
	{"text": "婚育史：已婚。", "bbox": [87, 472, 218, 488]},
	{"text": "家族史：无家族性遗传病史。", "bbox": [87, 502, 343, 518]},
	{"text": "体格检查：BMI：38Kg/m²神志清，精神可，体型肥胖，心肺听诊无明显异常，双下肢无水肿", "bbox": [87, 529, 898, 546]},
	{"text": "辅助检查：血糖 糖化", "bbox": [87, 559, 293, 575]},
	{"text": "门诊诊断：", "bbox": [87, 588, 176, 604]},
	{"text": "1、2型糖尿病", "bbox": [130, 617, 251, 633]},
	{"text": "门诊处置：无", "bbox": [87, 645, 210, 661]},
	{"text": "诊疗意见:药物治疗、如有不适，请随时复诊", "bbox": [87, 674, 481, 690]},
	{"text": "医师签名：胡志环", "bbox": [87, 707, 277, 726]},
	{"text": "签名日期：2025-04-10 10:34", "bbox": [87, 738, 359, 754]}
]
2026-08-10 13:27:00,295 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=10.6s
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[0]: text=原阳县人民医院, bbox=[368, 31, 616, 59]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[426, 72, 564, 98]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[2]: text=门诊号：135700000737, bbox=[730, 106, 909, 118]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[91, 134, 141, 149]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[4]: text=性别：男, bbox=[254, 134, 337, 149]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：37岁, bbox=[418, 134, 517, 149]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[6]: text=婚否：已婚, bbox=[579, 134, 685, 149]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[7]: text=民族：汉族, bbox=[749, 134, 851, 149]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[8]: text=职业：工人, bbox=[91, 162, 193, 177]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[9]: text=身份证号：, bbox=[366, 162, 454, 177]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[10]: text=41, bbox=[366, 188, 398, 197]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[11]: text=39, bbox=[525, 190, 547, 201]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[12]: text=籍贯：河南省新乡市, bbox=[91, 216, 275, 231]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[13]: text=现住址：河南省新乡市, bbox=[366, 216, 565, 231]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[14]: text=县, bbox=[366, 243, 386, 258]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[15]: text=工作单位：, bbox=[91, 271, 180, 286]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[16]: text=联系电, bbox=[366, 271, 425, 286]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[17]: text=心电图号：, bbox=[638, 269, 727, 285]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[18]: text=初诊科别：内分泌科门诊, bbox=[91, 300, 317, 315]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[19]: text=初诊日期：2025-02-25, bbox=[366, 300, 568, 315]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[20]: text=过敏史：无, bbox=[637, 299, 742, 314]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[21]: text=主诉：发现血糖高半年余, bbox=[87, 328, 334, 344]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[22]: text=现病史：半年前发现血糖高，空腹血糖13mmol/L，平时口服二甲双胍片0.5g 每日三次，, bbox=[87, 357, 872, 373]
2026-08-10 13:27:00,296 INFO     29 [qwen-vl-text] coord item[23]: text=监测空腹及餐后血糖仍高，门诊就诊。, bbox=[87, 386, 423, 402]
2026-08-10 13:27:00,297 INFO     29 [qwen-vl-text] coord item[24]: text=既往史：既往体健，无肝炎、结核、疟疾病史，无高血压、心脏疾病病史，无手术、外, bbox=[87, 414, 864, 430]
2026-08-10 13:27:00,297 INFO     29 [qwen-vl-text] coord item[25]: text=伤、输血史, bbox=[87, 443, 188, 459]
2026-08-10 13:27:00,297 INFO     29 [qwen-vl-text] coord item[26]: text=婚育史：已婚。, bbox=[87, 472, 218, 488]
2026-08-10 13:27:00,297 INFO     29 [qwen-vl-text] coord item[27]: text=家族史：无家族性遗传病史。, bbox=[87, 502, 343, 518]
2026-08-10 13:27:00,297 INFO     29 [qwen-vl-text] coord item[28]: text=体格检查：BMI：38Kg/m²神志清，精神可，体型肥胖，心肺听诊无明显异常，双下肢无水肿, bbox=[87, 529, 898, 546]
2026-08-10 13:27:00,297 INFO     29 [qwen-vl-text] coord item[29]: text=辅助检查：血糖 糖化, bbox=[87, 559, 293, 575]
2026-08-10 13:27:00,297 INFO     29 [qwen-vl-text] coord item[30]: text=门诊诊断：, bbox=[87, 588, 176, 604]
2026-08-10 13:27:00,297 INFO     29 [qwen-vl-text] coord item[31]: text=1、2型糖尿病, bbox=[130, 617, 251, 633]
2026-08-10 13:27:00,297 INFO     29 [qwen-vl-text] coord item[32]: text=门诊处置：无, bbox=[87, 645, 210, 661]
2026-08-10 13:27:00,297 INFO     29 [qwen-vl-text] coord item[33]: text=诊疗意见:药物治疗、如有不适，请随时复诊, bbox=[87, 674, 481, 690]
2026-08-10 13:27:00,297 INFO     29 [qwen-vl-text] coord item[34]: text=医师签名：胡志环, bbox=[87, 707, 277, 726]
2026-08-10 13:27:00,297 INFO     29 [qwen-vl-text] coord item[35]: text=签名日期：2025-04-10 10:34, bbox=[87, 738, 359, 754]
2026-08-10 13:27:00,297 INFO     29 [qwen-vl-text] page=5 — 35/35 coords, api_time=10.6s
2026-08-10 13:27:00,297 INFO     29 [qwen-vl-text] new_positions (35):
[[5, 218.95999999999998, 366.52, 26.102, 49.678], [5, 253.47, 335.58, 60.623999999999995, 82.51599999999999], [5, 434.34999999999997, 540.855, 89.252, 99.356], [5, 54.144999999999996, 83.895, 112.828, 125.458], [5, 151.13, 200.515, 112.828, 125.458], [5, 248.70999999999998, 307.615, 112.828, 125.458], [5, 344.505, 407.575, 112.828, 125.458], [5, 445.655, 506.34499999999997, 112.828, 125.458], [5, 54.144999999999996, 114.835, 136.404, 149.034], [5, 217.76999999999998, 270.13, 136.404, 149.034], [5, 217.76999999999998, 236.81, 158.296, 165.874], [5, 312.375, 325.465, 159.98, 169.242], [5, 54.144999999999996, 163.625, 181.87199999999999, 194.50199999999998], [5, 217.76999999999998, 336.175, 181.87199999999999, 194.50199999999998], [5, 217.76999999999998, 229.67, 204.606, 217.236], [5, 54.144999999999996, 107.1, 228.182, 240.81199999999998], [5, 217.76999999999998, 252.875, 228.182, 240.81199999999998], [5, 379.60999999999996, 432.565, 226.498, 239.97], [5, 54.144999999999996, 188.61499999999998, 252.6, 265.23], [5, 217.76999999999998, 337.96, 252.6, 265.23], [5, 379.015, 441.48999999999995, 251.75799999999998, 264.388], [5, 51.765, 198.73, 276.176, 289.64799999999997], [5, 51.765, 518.84, 300.594, 314.066], [5, 51.765, 251.685, 325.012, 338.484], [5, 51.765, 514.0799999999999, 348.58799999999997, 362.06], [5, 51.765, 111.86, 373.006, 386.478], [5, 51.765, 129.71, 397.424, 410.89599999999996], [5, 51.765, 204.08499999999998, 422.68399999999997, 436.156], [5, 51.765, 534.31, 445.418, 459.73199999999997], [5, 51.765, 174.33499999999998, 470.678, 484.15], [5, 51.765, 104.72, 495.096, 508.568], [5, 77.35, 149.345, 519.514, 532.986], [5, 51.765, 124.94999999999999, 543.09, 556.562], [5, 51.765, 286.195, 567.5079999999999, 580.98], [5, 51.765, 164.815, 595.294, 611.292]]
2026-08-10 13:27:00,297 INFO     29 [qwen-vl-text] ═══ DONE ═══ 35 positions, pages=1, time=12.5s
2026-08-10 13:27:00,309 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 13:27:00,310 INFO     29 [Trace] task=01081162 | doc=HZNA高血糖郑州.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "206 items", "markdown": "", "text": "", "name": "HZNA高血糖郑州.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_LabExam\": 3, \"chunks_Medication\": 3, \"chunks_Clinical\": 1, \"chunks_Prescription\": 1}"}
2026-08-10 13:27:00,310 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 13:27:00,320 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:27:00,321 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:27:00,321 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 13:27:00,321 INFO     29 [qwen-vl-text] positions(21): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:27:00,321 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [21]
2026-08-10 13:27:00,505 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:27:00,506 INFO     29 [qwen-vl-text] LLM extraction start, text_len=301
2026-08-10 13:27:00,506 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:27:00,507 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 32, \"bbox_end\": 52, \"encounter_dates\": [\"2025-01-01\", \"2025-03-13\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "天医院\n门诊患者费用清单(汇总)\n证件号:4107251\n姓名.\n卡号:4\n开始时间: 2025-01-01 00:00\n结束时间: 2025-03-13:59\n项目名称 单价 单位 数量 金额\n-g3盐酸二甲双胍缓释\n.086 片 64.0 5.50\n片\n病历资料复印 0.4 每张 26.0 10.40\n糖化血红蛋白全定量 256 项 1.00 25.00\n测定\n静脉注射 3.8 次 1.00 3.80\n血糖测定 6 次 1.00 6.00\n共计:5项 金额合计:¥50.70\n打印时间:2025-03-13 10:13:36\n操作员.\n扫描二维码下载电子发票\n此单据作为就诊凭证,请不要随意丢弃",
    "role": "user"
  }
]
2026-08-10 13:27:02,942 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:27:02,943 INFO     29 [qwen-vl-text] LLM output (len=404):
{
  "encounter_date": "2025-03-13",
  "pharmacy": null,
  "medications": [
    {
      "name": "盐酸二甲双胍缓释片",
      "specification": null,
      "dosage": null,
      "quantity": 64.0,
      "unit_price": 5.50,
      "total_price": 352.0,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 50.70,
  "payment_method": null
}
2026-08-10 13:27:02,943 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-03-13]
2026-08-10 13:27:02,946 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=912902, prompt_len=977
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共21行）
["天医院", "门诊患者费用清单(汇总)", "证件号:4107251", "姓名.", "卡号:4", "开始时间: 2025-01-01 00:00", "结束时间: 2025-03-13:59", "项目名称 单价 单位 数量 金额", "-g3盐酸二甲双胍缓释", ".086 片 64.0 5.50", "片", "病历资料复印 0.4 每张 26.0 10.40", "糖化血红蛋白全定量 256 项 1.00 25.00", "测定", "静脉注射 3.8 次 1.00 3.80", "血糖测定 6 次 1.00 6.00", "共计:5项 金额合计:¥50.70", "打印时间:2025-03-13 10:13:36", "操作员.", "扫描二维码下载电子发票", "此单据作为就诊凭证,请不要随意丢弃"]

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
2026-08-10 13:27:13,693 INFO     29 [qwen-vl-text] coord API raw response (len=1597):
[
	{"text": "天医院", "bbox": [464, 102, 593, 130]},
	{"text": "门诊患者费用清单(汇总)", "bbox": [202, 136, 666, 165]},
	{"text": "证件号:4107251", "bbox": [85, 180, 338, 204]},
	{"text": "姓名.", "bbox": [86, 213, 164, 236]},
	{"text": "卡号:4", "bbox": [352, 213, 438, 237]},
	{"text": "开始时间: 2025-01-01 00:00", "bbox": [86, 245, 573, 269]},
	{"text": "结束时间: 2025-03-13:59", "bbox": [86, 285, 573, 310]},
	{"text": "项目名称 单价 单位 数量 金额", "bbox": [82, 327, 636, 352]},
	{"text": "-g3盐酸二甲双胍缓释", "bbox": [82, 367, 351, 390], "bbox": [82, 367, 351, 390]},
	{"text": ".086 片 64.0 5.50", "bbox": [392, 369, 632, 392], "bbox": [392, 369, 632, 392]},
	{"text": "片", "bbox": [82, 399, 108, 419], "bbox": [82, 399, 108, 419]},
	{"text": "病历资料复印 0.4 每张 26.0 10.40", "bbox": [82, 429, 632, 455], "bbox": [82, 429, 632, 455]},
	{"text": "糖化血红蛋白全定量 256 项 1.00 25.00", "bbox": [82, 490, 636, 516], "bbox": [82, 490, 636, 516]},
	{"text": "测定", "bbox": [82, 520, 139, 540], "bbox": [82, 520, 139, 540]},
	{"text": "静脉注射 3.8 次 1.00 3.80", "bbox": [82, 551, 636, 576], "bbox": [82, 551, 636, 576]},
	{"text": "血糖测定 6 次 1.00 6.00", "bbox": [82, 582, 636, 607], "bbox": [82, 582, 636, 607]},
	{"text": "共计:5项 金额合计:¥50.70", "bbox": [108, 670, 666, 696], "bbox": [108, 670, 666, 696]},
	{"text": "打印时间:2025-03-13 10:13:36", "bbox": [94, 738, 608, 763], "bbox": [94, 738, 608, 763]},
	{"text": "操作员.", "bbox": [104, 793, 220, 818], "bbox": [104, 793, 220, 818]},
	{"text": "扫描二维码下载电子发票", "bbox": [265, 888, 607, 910], "bbox": [265, 888, 607, 910]},
	{"text": "此单据作为就诊凭证,请不要随意丢弃", "bbox": [127, 915, 662, 940], "bbox": [127, 915, 662, 940]}
]
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord API: raw_items=21, valid_items=21, elapsed=10.7s
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord item[0]: text=天医院, bbox=[464, 102, 593, 130]
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord item[1]: text=门诊患者费用清单(汇总), bbox=[202, 136, 666, 165]
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord item[2]: text=证件号:4107251, bbox=[85, 180, 338, 204]
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord item[3]: text=姓名., bbox=[86, 213, 164, 236]
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord item[4]: text=卡号:4, bbox=[352, 213, 438, 237]
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord item[5]: text=开始时间: 2025-01-01 00:00, bbox=[86, 245, 573, 269]
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord item[6]: text=结束时间: 2025-03-13:59, bbox=[86, 285, 573, 310]
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord item[7]: text=项目名称 单价 单位 数量 金额, bbox=[82, 327, 636, 352]
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord item[8]: text=-g3盐酸二甲双胍缓释, bbox=[82, 367, 351, 390]
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord item[9]: text=.086 片 64.0 5.50, bbox=[392, 369, 632, 392]
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord item[10]: text=片, bbox=[82, 399, 108, 419]
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord item[11]: text=病历资料复印 0.4 每张 26.0 10.40, bbox=[82, 429, 632, 455]
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord item[12]: text=糖化血红蛋白全定量 256 项 1.00 25.00, bbox=[82, 490, 636, 516]
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord item[13]: text=测定, bbox=[82, 520, 139, 540]
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord item[14]: text=静脉注射 3.8 次 1.00 3.80, bbox=[82, 551, 636, 576]
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord item[15]: text=血糖测定 6 次 1.00 6.00, bbox=[82, 582, 636, 607]
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord item[16]: text=共计:5项 金额合计:¥50.70, bbox=[108, 670, 666, 696]
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord item[17]: text=打印时间:2025-03-13 10:13:36, bbox=[94, 738, 608, 763]
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord item[18]: text=操作员., bbox=[104, 793, 220, 818]
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord item[19]: text=扫描二维码下载电子发票, bbox=[265, 888, 607, 910]
2026-08-10 13:27:13,694 INFO     29 [qwen-vl-text] coord item[20]: text=此单据作为就诊凭证,请不要随意丢弃, bbox=[127, 915, 662, 940]
2026-08-10 13:27:13,695 INFO     29 [qwen-vl-text] page=2 — 21/21 coords, api_time=10.7s
2026-08-10 13:27:13,695 INFO     29 [qwen-vl-text] new_positions (21):
[[2, 276.08, 352.835, 85.884, 109.46], [2, 120.19, 396.27, 114.512, 138.93], [2, 50.574999999999996, 201.10999999999999, 151.56, 171.768], [2, 51.169999999999995, 97.58, 179.346, 198.712], [2, 209.44, 260.61, 179.346, 199.554], [2, 51.169999999999995, 340.935, 206.29, 226.498], [2, 51.169999999999995, 340.935, 239.97, 261.02], [2, 48.79, 378.41999999999996, 275.334, 296.384], [2, 48.79, 208.845, 309.014, 328.38], [2, 233.23999999999998, 376.03999999999996, 310.698, 330.06399999999996], [2, 48.79, 64.25999999999999, 335.95799999999997, 352.798], [2, 48.79, 376.03999999999996, 361.21799999999996, 383.11], [2, 48.79, 378.41999999999996, 412.58, 434.472], [2, 48.79, 82.705, 437.84, 454.68], [2, 48.79, 378.41999999999996, 463.942, 484.99199999999996], [2, 48.79, 378.41999999999996, 490.044, 511.094], [2, 64.25999999999999, 396.27, 564.14, 586.0319999999999], [2, 55.93, 361.76, 621.396, 642.446], [2, 61.879999999999995, 130.9, 667.706, 688.756], [2, 157.67499999999998, 361.16499999999996, 747.696, 766.22], [2, 75.565, 393.89, 770.43, 791.48]]
2026-08-10 13:27:13,695 INFO     29 [qwen-vl-text] ═══ DONE ═══ 21 positions, pages=1, time=13.4s
2026-08-10 13:27:13,695 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:27:13,701 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:27:13,701 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 13:27:13,701 INFO     29 [qwen-vl-text] positions(33): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:27:13,701 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [33]
2026-08-10 13:27:13,819 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:27:13,820 INFO     29 [qwen-vl-text] LLM extraction start, text_len=272
2026-08-10 13:27:13,820 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:27:13,820 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 69, \"bbox_end\": 101, \"encounter_dates\": [\"2025-02-15\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "中心药店\n日期: 2025 02 15 19:20:00\n销售员: 毛爱青\n药品名称\n生产厂商\n批号\n规格\n数量\n单位\n单价\n金额\n盐酸二甲双胍肠溶片\n贵州天安药业股份有限公司\n20240242\n0.5g/60\n3.00\n瓶\n20.00\n60.00\n应收 60.00 实收 60.00\n找回 0.00 中药付 1.00\n地址: 原阳县西干道\n电话: 7282955\n会员卡:\n本次积分: 60\n积分余额: 260\n原额: 0.00\n余额: 0\n药品为特殊商品无质量问题\n概不退换\n社会主核心价值观\n富强 民主 文明 和谐\n自由 平等 公正 法治",
    "role": "user"
  }
]
2026-08-10 13:27:13,824 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:27:13.823+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 49, "failed": 0, "current": {"0108116294bf11f1bd9827cf206dfa2d": {"id": "0108116294bf11f1bd9827cf206dfa2d", "doc_id": "00c2e26894bf11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HZNA\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "type": "pdf", "location": "HZNA\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "size": 7585233, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368350219, "task_type": "dataflow", "root_trace_id": "76162b34ec514c059d062d6d34315295", "root_traceparent": "00-76162b34ec514c059d062d6d34315295-096f88c2095fe0e3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:27:16,299 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:27:16,300 INFO     29 [qwen-vl-text] LLM output (len=418):
{
  "encounter_date": "2025-02-15",
  "pharmacy": "中心药店",
  "medications": [
    {
      "name": "盐酸二甲双胍肠溶片",
      "specification": "0.5g/60",
      "dosage": null,
      "quantity": 3.0,
      "unit_price": 20.0,
      "total_price": 60.0,
      "frequency": null,
      "route": null,
      "manufacturer": "贵州天安药业股份有限公司",
      "approval_number": null
    }
  ],
  "payment_total": 60.0,
  "payment_method": null
}
2026-08-10 13:27:16,300 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-02-15]
2026-08-10 13:27:16,301 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=628944, prompt_len=984
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["中心药店", "日期: 2025 02 15 19:20:00", "销售员: 毛爱青", "药品名称", "生产厂商", "批号", "规格", "数量", "单位", "单价", "金额", "盐酸二甲双胍肠溶片", "贵州天安药业股份有限公司", "20240242", "0.5g/60", "3.00", "瓶", "20.00", "60.00", "应收 60.00 实收 60.00", "找回 0.00 中药付 1.00", "地址: 原阳县西干道", "电话: 7282955", "会员卡:", "本次积分: 60", "积分余额: 260", "原额: 0.00", "余额: 0", "药品为特殊商品无质量问题", "概不退换", "社会主核心价值观", "富强 民主 文明 和谐", "自由 平等 公正 法治"]

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
2026-08-10 13:27:25,872 INFO     29 [qwen-vl-text] coord API raw response (len=1721):
[
	{"text": "中心药店", "bbox": [427, 10, 560, 31]},
	{"text": "日期: 2025 02 15 19:20:00", "bbox": [285, 31, 685, 65]},
	{"text": "销售员: 毛爱青", "bbox": [283, 70, 493, 93]},
	{"text": "药品名称", "bbox": [283, 103, 400, 125]},
	{"text": "生产厂商", "bbox": [283, 136, 401, 158]},
	{"text": "批号", "bbox": [281, 169, 337, 191]},
	{"text": "规格", "bbox": [595, 171, 652, 193]},
	{"text": "数量", "bbox": [281, 204, 340, 227]},
	{"text": "单位", "bbox": [393, 205, 450, 227]},
	{"text": "单价", "bbox": [504, 205, 558, 227]},
	{"text": "金额", "bbox": [613, 206, 671, 229]},
	{"text": "盐酸二甲双胍肠溶片", "bbox": [281, 239, 557, 262]},
	{"text": "贵州天安药业股份有限公司", "bbox": [281, 272, 654, 295]},
	{"text": "20240242", "bbox": [278, 309, 403, 331]},
	{"text": "0.5g/60", "bbox": [577, 307, 690, 331]},
	{"text": "3.00", "bbox": [276, 346, 341, 368]},
	{"text": "瓶", "bbox": [388, 345, 420, 368]},
	{"text": "20.00", "bbox": [466, 346, 546, 368]},
	{"text": "60.00", "bbox": [594, 344, 674, 366]},
	{"text": "应收 60.00 实收 60.00", "bbox": [275, 414, 661, 439]},
	{"text": "找回 0.00 中药付 1.00", "bbox": [275, 450, 661, 475]},
	{"text": "地址: 原阳县西干道", "bbox": [275, 486, 560, 511]},
	{"text": "电话: 7282955", "bbox": [276, 521, 482, 545]},
	{"text": "会员卡:", "bbox": [275, 557, 384, 582]},
	{"text": "本次积分: 60", "bbox": [275, 595, 467, 621]},
	{"text": "积分余额: 260", "bbox": [275, 632, 482, 658]},
	{"text": "原额: 0.00", "bbox": [275, 670, 498, 696]},
	{"text": "余额: 0", "bbox": [275, 709, 452, 735]},
	{"text": "药品为特殊商品无质量问题", "bbox": [276, 747, 659, 774]},
	{"text": "概不退换", "bbox": [278, 788, 398, 816]},
	{"text": "社会主核心价值观", "bbox": [312, 829, 561, 858]},
	{"text": "富强 民主 文明 和谐", "bbox": [313, 869, 608, 897]},
	{"text": "自由 平等 公正 法治", "bbox": [310, 908, 604, 935]}
]
2026-08-10 13:27:25,872 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=9.6s
2026-08-10 13:27:25,873 INFO     29 [qwen-vl-text] coord item[0]: text=中心药店, bbox=[427, 10, 560, 31]
2026-08-10 13:27:25,873 INFO     29 [qwen-vl-text] coord item[1]: text=日期: 2025 02 15 19:20:00, bbox=[285, 31, 685, 65]
2026-08-10 13:27:25,873 INFO     29 [qwen-vl-text] coord item[2]: text=销售员: 毛爱青, bbox=[283, 70, 493, 93]
2026-08-10 13:27:25,873 INFO     29 [qwen-vl-text] coord item[3]: text=药品名称, bbox=[283, 103, 400, 125]
2026-08-10 13:27:25,873 INFO     29 [qwen-vl-text] coord item[4]: text=生产厂商, bbox=[283, 136, 401, 158]
2026-08-10 13:27:25,873 INFO     29 [qwen-vl-text] coord item[5]: text=批号, bbox=[281, 169, 337, 191]
2026-08-10 13:27:25,873 INFO     29 [qwen-vl-text] coord item[6]: text=规格, bbox=[595, 171, 652, 193]
2026-08-10 13:27:25,873 INFO     29 [qwen-vl-text] coord item[7]: text=数量, bbox=[281, 204, 340, 227]
2026-08-10 13:27:25,873 INFO     29 [qwen-vl-text] coord item[8]: text=单位, bbox=[393, 205, 450, 227]
2026-08-10 13:27:25,873 INFO     29 [qwen-vl-text] coord item[9]: text=单价, bbox=[504, 205, 558, 227]
2026-08-10 13:27:25,873 INFO     29 [qwen-vl-text] coord item[10]: text=金额, bbox=[613, 206, 671, 229]
2026-08-10 13:27:25,873 INFO     29 [qwen-vl-text] coord item[11]: text=盐酸二甲双胍肠溶片, bbox=[281, 239, 557, 262]
2026-08-10 13:27:25,873 INFO     29 [qwen-vl-text] coord item[12]: text=贵州天安药业股份有限公司, bbox=[281, 272, 654, 295]
2026-08-10 13:27:25,873 INFO     29 [qwen-vl-text] coord item[13]: text=20240242, bbox=[278, 309, 403, 331]
2026-08-10 13:27:25,873 INFO     29 [qwen-vl-text] coord item[14]: text=0.5g/60, bbox=[577, 307, 690, 331]
2026-08-10 13:27:25,874 INFO     29 [qwen-vl-text] coord item[15]: text=3.00, bbox=[276, 346, 341, 368]
2026-08-10 13:27:25,874 INFO     29 [qwen-vl-text] coord item[16]: text=瓶, bbox=[388, 345, 420, 368]
2026-08-10 13:27:25,874 INFO     29 [qwen-vl-text] coord item[17]: text=20.00, bbox=[466, 346, 546, 368]
2026-08-10 13:27:25,874 INFO     29 [qwen-vl-text] coord item[18]: text=60.00, bbox=[594, 344, 674, 366]
2026-08-10 13:27:25,874 INFO     29 [qwen-vl-text] coord item[19]: text=应收 60.00 实收 60.00, bbox=[275, 414, 661, 439]
2026-08-10 13:27:25,874 INFO     29 [qwen-vl-text] coord item[20]: text=找回 0.00 中药付 1.00, bbox=[275, 450, 661, 475]
2026-08-10 13:27:25,874 INFO     29 [qwen-vl-text] coord item[21]: text=地址: 原阳县西干道, bbox=[275, 486, 560, 511]
2026-08-10 13:27:25,874 INFO     29 [qwen-vl-text] coord item[22]: text=电话: 7282955, bbox=[276, 521, 482, 545]
2026-08-10 13:27:25,874 INFO     29 [qwen-vl-text] coord item[23]: text=会员卡:, bbox=[275, 557, 384, 582]
2026-08-10 13:27:25,874 INFO     29 [qwen-vl-text] coord item[24]: text=本次积分: 60, bbox=[275, 595, 467, 621]
2026-08-10 13:27:25,874 INFO     29 [qwen-vl-text] coord item[25]: text=积分余额: 260, bbox=[275, 632, 482, 658]
2026-08-10 13:27:25,874 INFO     29 [qwen-vl-text] coord item[26]: text=原额: 0.00, bbox=[275, 670, 498, 696]
2026-08-10 13:27:25,874 INFO     29 [qwen-vl-text] coord item[27]: text=余额: 0, bbox=[275, 709, 452, 735]
2026-08-10 13:27:25,875 INFO     29 [qwen-vl-text] coord item[28]: text=药品为特殊商品无质量问题, bbox=[276, 747, 659, 774]
2026-08-10 13:27:25,875 INFO     29 [qwen-vl-text] coord item[29]: text=概不退换, bbox=[278, 788, 398, 816]
2026-08-10 13:27:25,875 INFO     29 [qwen-vl-text] coord item[30]: text=社会主核心价值观, bbox=[312, 829, 561, 858]
2026-08-10 13:27:25,875 INFO     29 [qwen-vl-text] coord item[31]: text=富强 民主 文明 和谐, bbox=[313, 869, 608, 897]
2026-08-10 13:27:25,875 INFO     29 [qwen-vl-text] coord item[32]: text=自由 平等 公正 法治, bbox=[310, 908, 604, 935]
2026-08-10 13:27:25,875 INFO     29 [qwen-vl-text] page=4 — 33/33 coords, api_time=9.6s
2026-08-10 13:27:25,875 INFO     29 [qwen-vl-text] new_positions (33):
[[4, 254.065, 333.2, 8.42, 26.102], [4, 169.575, 407.575, 26.102, 54.73], [4, 168.385, 293.335, 58.94, 78.306], [4, 168.385, 238.0, 86.726, 105.25], [4, 168.385, 238.595, 114.512, 133.036], [4, 167.195, 200.515, 142.298, 160.822], [4, 354.025, 387.94, 143.982, 162.506], [4, 167.195, 202.29999999999998, 171.768, 191.134], [4, 233.83499999999998, 267.75, 172.60999999999999, 191.134], [4, 299.88, 332.01, 172.60999999999999, 191.134], [4, 364.73499999999996, 399.245, 173.452, 192.81799999999998], [4, 167.195, 331.41499999999996, 201.238, 220.60399999999998], [4, 167.195, 389.13, 229.024, 248.39], [4, 165.41, 239.785, 260.178, 278.702], [4, 343.315, 410.54999999999995, 258.49399999999997, 278.702], [4, 164.22, 202.89499999999998, 291.332, 309.856], [4, 230.85999999999999, 249.89999999999998, 290.49, 309.856], [4, 277.27, 324.87, 291.332, 309.856], [4, 353.43, 401.03, 289.64799999999997, 308.17199999999997], [4, 163.625, 393.29499999999996, 348.58799999999997, 369.638], [4, 163.625, 393.29499999999996, 378.9, 399.95], [4, 163.625, 333.2, 409.212, 430.262], [4, 164.22, 286.78999999999996, 438.68199999999996, 458.89], [4, 163.625, 228.48, 468.99399999999997, 490.044], [4, 163.625, 277.865, 500.99, 522.882], [4, 163.625, 286.78999999999996, 532.144, 554.036], [4, 163.625, 296.31, 564.14, 586.0319999999999], [4, 163.625, 268.94, 596.978, 618.87], [4, 164.22, 392.10499999999996, 628.9739999999999, 651.708], [4, 165.41, 236.81, 663.496, 687.072], [4, 185.64, 333.79499999999996, 698.018, 722.4359999999999], [4, 186.23499999999999, 361.76, 731.698, 755.274], [4, 184.45, 359.38, 764.536, 787.27]]
2026-08-10 13:27:25,875 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=12.2s
2026-08-10 13:27:25,876 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:27:25,877 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:27:25,877 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 13:27:25,877 INFO     29 [qwen-vl-text] positions(41): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:27:25,878 INFO     29 [qwen-vl-text] page grouping: [7, 8], lines per page: [21, 20]
2026-08-10 13:27:26,070 INFO     29 [qwen-vl-text] page=7, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:27:26,257 INFO     29 [qwen-vl-text] page=8, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:27:26,259 INFO     29 [qwen-vl-text] LLM extraction start, text_len=406
2026-08-10 13:27:26,259 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:27:26,259 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 165, \"bbox_end\": 205, \"encounter_dates\": [\"2025-04-10\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "原阳县人民医院\n姓名：\n医保类别：自费\n收费时间：2025-04-10 00:00:00\n发票号：41060135H1005655423门诊号：1595205\n患者卡号：410725198706033639\n费用分类\n西药费\n13.38\n金额：壹拾叁圆叁角捌分\n13.38\n现金：0\n账户：13.38\n银联卡：0\n医保账户：0.0\n医保统筹：0.0\n个人自付：0.0\n支付宝：0\n微信：0\n账户余额：0\n医保账户余额：\n原阳县人民医院\n门诊患者费用清单\n卡号：410725198706033639 账户余额：0\n姓名：\n流水号：1595205\n开始时间：2025-04-10 10:33\n结束时间：2025-04-10 10:33\n项目名称\n单价\n单位\n数量\n金额\n-g3盐酸二甲双胍片\n3.60\n60\n13.38\n共计：1项\n金额合计：13.38\n打印时间：2025-04-22 16:36:16\n操作员：赵彤",
    "role": "user"
  }
]
2026-08-10 13:27:28,733 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:27:28,734 INFO     29 [qwen-vl-text] LLM output (len=403):
{
  "encounter_date": "2025-04-10",
  "pharmacy": "原阳县人民医院",
  "medications": [
    {
      "name": "盐酸二甲双胍片",
      "specification": null,
      "dosage": null,
      "quantity": 1,
      "unit_price": 3.6,
      "total_price": 13.38,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 13.38,
  "payment_method": "账户"
}
2026-08-10 13:27:28,734 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-04-10]
2026-08-10 13:27:28,738 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=791752, prompt_len=885
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共21行）
["原阳县人民医院", "姓名：", "医保类别：自费", "收费时间：2025-04-10 00:00:00", "发票号：41060135H1005655423门诊号：1595205", "患者卡号：410725198706033639", "费用分类", "西药费", "13.38", "金额：壹拾叁圆叁角捌分", "13.38", "现金：0", "账户：13.38", "银联卡：0", "医保账户：0.0", "医保统筹：0.0", "个人自付：0.0", "支付宝：0", "微信：0", "账户余额：0", "医保账户余额："]

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
2026-08-10 13:27:35,417 INFO     29 [qwen-vl-text] coord API raw response (len=1125):
[
	{"text": "原阳县人民医院", "bbox": [289, 34, 674, 65]},
	{"text": "姓名：", "bbox": [70, 81, 164, 104]},
	{"text": "医保类别：自费", "bbox": [511, 83, 768, 106]},
	{"text": "收费时间：2025-04-10 00:00:00", "bbox": [70, 117, 648, 139]},
	{"text": "发票号：41060135H1005655423门诊号：1595205", "bbox": [71, 152, 933, 176]},
	{"text": "患者卡号：410725198706033639", "bbox": [70, 193, 625, 215]},
	{"text": "费用分类", "bbox": [73, 237, 251, 264]},
	{"text": "西药费", "bbox": [97, 286, 210, 311]},
	{"text": "13.38", "bbox": [357, 290, 457, 309]},
	{"text": "金额：壹拾叁圆叁角捌分", "bbox": [88, 476, 595, 504]},
	{"text": "13.38", "bbox": [803, 479, 910, 501]},
	{"text": "现金：0", "bbox": [130, 509, 260, 534]},
	{"text": "账户：13.38", "bbox": [555, 511, 789, 536]},
	{"text": "银联卡：0", "bbox": [131, 545, 305, 571]},
	{"text": "医保账户：0.0", "bbox": [555, 548, 832, 575]},
	{"text": "医保统筹：0.0", "bbox": [131, 581, 418, 608]},
	{"text": "个人自付：0.0", "bbox": [560, 587, 853, 614]},
	{"text": "支付宝：0", "bbox": [131, 624, 308, 652]},
	{"text": "微信：0", "bbox": [560, 627, 705, 654]},
	{"text": "账户余额：0", "bbox": [131, 663, 355, 690]},
	{"text": "医保账户余额：", "bbox": [551, 664, 798, 687]}
]
2026-08-10 13:27:35,418 INFO     29 [qwen-vl-text] coord API: raw_items=21, valid_items=21, elapsed=6.7s
2026-08-10 13:27:35,418 INFO     29 [qwen-vl-text] coord item[0]: text=原阳县人民医院, bbox=[289, 34, 674, 65]
2026-08-10 13:27:35,418 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[70, 81, 164, 104]
2026-08-10 13:27:35,418 INFO     29 [qwen-vl-text] coord item[2]: text=医保类别：自费, bbox=[511, 83, 768, 106]
2026-08-10 13:27:35,418 INFO     29 [qwen-vl-text] coord item[3]: text=收费时间：2025-04-10 00:00:00, bbox=[70, 117, 648, 139]
2026-08-10 13:27:35,419 INFO     29 [qwen-vl-text] coord item[4]: text=发票号：41060135H1005655423门诊号：1595205, bbox=[71, 152, 933, 176]
2026-08-10 13:27:35,419 INFO     29 [qwen-vl-text] coord item[5]: text=患者卡号：410725198706033639, bbox=[70, 193, 625, 215]
2026-08-10 13:27:35,419 INFO     29 [qwen-vl-text] coord item[6]: text=费用分类, bbox=[73, 237, 251, 264]
2026-08-10 13:27:35,419 INFO     29 [qwen-vl-text] coord item[7]: text=西药费, bbox=[97, 286, 210, 311]
2026-08-10 13:27:35,419 INFO     29 [qwen-vl-text] coord item[8]: text=13.38, bbox=[357, 290, 457, 309]
2026-08-10 13:27:35,419 INFO     29 [qwen-vl-text] coord item[9]: text=金额：壹拾叁圆叁角捌分, bbox=[88, 476, 595, 504]
2026-08-10 13:27:35,419 INFO     29 [qwen-vl-text] coord item[10]: text=13.38, bbox=[803, 479, 910, 501]
2026-08-10 13:27:35,419 INFO     29 [qwen-vl-text] coord item[11]: text=现金：0, bbox=[130, 509, 260, 534]
2026-08-10 13:27:35,419 INFO     29 [qwen-vl-text] coord item[12]: text=账户：13.38, bbox=[555, 511, 789, 536]
2026-08-10 13:27:35,419 INFO     29 [qwen-vl-text] coord item[13]: text=银联卡：0, bbox=[131, 545, 305, 571]
2026-08-10 13:27:35,419 INFO     29 [qwen-vl-text] coord item[14]: text=医保账户：0.0, bbox=[555, 548, 832, 575]
2026-08-10 13:27:35,419 INFO     29 [qwen-vl-text] coord item[15]: text=医保统筹：0.0, bbox=[131, 581, 418, 608]
2026-08-10 13:27:35,419 INFO     29 [qwen-vl-text] coord item[16]: text=个人自付：0.0, bbox=[560, 587, 853, 614]
2026-08-10 13:27:35,419 INFO     29 [qwen-vl-text] coord item[17]: text=支付宝：0, bbox=[131, 624, 308, 652]
2026-08-10 13:27:35,419 INFO     29 [qwen-vl-text] coord item[18]: text=微信：0, bbox=[560, 627, 705, 654]
2026-08-10 13:27:35,420 INFO     29 [qwen-vl-text] coord item[19]: text=账户余额：0, bbox=[131, 663, 355, 690]
2026-08-10 13:27:35,420 INFO     29 [qwen-vl-text] coord item[20]: text=医保账户余额：, bbox=[551, 664, 798, 687]
2026-08-10 13:27:35,420 INFO     29 [qwen-vl-text] page=7 — 21/21 coords, api_time=6.7s
2026-08-10 13:27:35,424 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=930873, prompt_len=869
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共20行）
["原阳县人民医院", "门诊患者费用清单", "卡号：410725198706033639 账户余额：0", "姓名：", "流水号：1595205", "开始时间：2025-04-10 10:33", "结束时间：2025-04-10 10:33", "项目名称", "单价", "单位", "数量", "金额", "-g3盐酸二甲双胍片", "3.60", "60", "13.38", "共计：1项", "金额合计：13.38", "打印时间：2025-04-22 16:36:16", "操作员：赵彤"]

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
2026-08-10 13:27:43,317 INFO     29 [qwen-vl-text] coord API raw response (len=1079):
[
	{"text": "原阳县人民医院", "bbox": [344, 340, 715, 372]},
	{"text": "门诊患者费用清单", "bbox": [330, 377, 727, 408]},
	{"text": "卡号：410725198706033639 账户余额：0", "bbox": [114, 418, 841, 445]},
	{"text": "姓名：", "bbox": [117, 456, 206, 482]},
	{"text": "流水号：1595205", "bbox": [623, 456, 920, 482]},
	{"text": "开始时间：2025-04-10 10:33", "bbox": [117, 490, 680, 516]},
	{"text": "结束时间：2025-04-10 10:33", "bbox": [120, 520, 680, 547]},
	{"text": "项目名称", "bbox": [122, 559, 265, 583]},
	{"text": "单价", "bbox": [492, 560, 564, 585]},
	{"text": "单位", "bbox": [586, 560, 668, 585]},
	{"text": "数量", "bbox": [685, 560, 758, 585]},
	{"text": "金额", "bbox": [861, 560, 935, 585]},
	{"text": "-g3盐酸二甲双胍片", "bbox": [119, 602, 395, 624]},
	{"text": "3.60", "bbox": [683, 604, 750, 624]},
	{"text": "60", "bbox": [683, 637, 719, 656]},
	{"text": "13.38", "bbox": [850, 606, 934, 625]},
	{"text": "共计：1项", "bbox": [130, 678, 302, 704]},
	{"text": "金额合计：13.38", "bbox": [464, 687, 790, 712]},
	{"text": "打印时间：2025-04-22 16:36:16", "bbox": [127, 710, 721, 735]},
	{"text": "操作员：赵彤", "bbox": [128, 735, 361, 759]}
]
2026-08-10 13:27:43,318 INFO     29 [qwen-vl-text] coord API: raw_items=20, valid_items=20, elapsed=7.9s
2026-08-10 13:27:43,318 INFO     29 [qwen-vl-text] coord item[0]: text=原阳县人民医院, bbox=[344, 340, 715, 372]
2026-08-10 13:27:43,318 INFO     29 [qwen-vl-text] coord item[1]: text=门诊患者费用清单, bbox=[330, 377, 727, 408]
2026-08-10 13:27:43,318 INFO     29 [qwen-vl-text] coord item[2]: text=卡号：410725198706033639 账户余额：0, bbox=[114, 418, 841, 445]
2026-08-10 13:27:43,318 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[117, 456, 206, 482]
2026-08-10 13:27:43,319 INFO     29 [qwen-vl-text] coord item[4]: text=流水号：1595205, bbox=[623, 456, 920, 482]
2026-08-10 13:27:43,319 INFO     29 [qwen-vl-text] coord item[5]: text=开始时间：2025-04-10 10:33, bbox=[117, 490, 680, 516]
2026-08-10 13:27:43,319 INFO     29 [qwen-vl-text] coord item[6]: text=结束时间：2025-04-10 10:33, bbox=[120, 520, 680, 547]
2026-08-10 13:27:43,319 INFO     29 [qwen-vl-text] coord item[7]: text=项目名称, bbox=[122, 559, 265, 583]
2026-08-10 13:27:43,319 INFO     29 [qwen-vl-text] coord item[8]: text=单价, bbox=[492, 560, 564, 585]
2026-08-10 13:27:43,319 INFO     29 [qwen-vl-text] coord item[9]: text=单位, bbox=[586, 560, 668, 585]
2026-08-10 13:27:43,319 INFO     29 [qwen-vl-text] coord item[10]: text=数量, bbox=[685, 560, 758, 585]
2026-08-10 13:27:43,319 INFO     29 [qwen-vl-text] coord item[11]: text=金额, bbox=[861, 560, 935, 585]
2026-08-10 13:27:43,319 INFO     29 [qwen-vl-text] coord item[12]: text=-g3盐酸二甲双胍片, bbox=[119, 602, 395, 624]
2026-08-10 13:27:43,319 INFO     29 [qwen-vl-text] coord item[13]: text=3.60, bbox=[683, 604, 750, 624]
2026-08-10 13:27:43,319 INFO     29 [qwen-vl-text] coord item[14]: text=60, bbox=[683, 637, 719, 656]
2026-08-10 13:27:43,319 INFO     29 [qwen-vl-text] coord item[15]: text=13.38, bbox=[850, 606, 934, 625]
2026-08-10 13:27:43,319 INFO     29 [qwen-vl-text] coord item[16]: text=共计：1项, bbox=[130, 678, 302, 704]
2026-08-10 13:27:43,319 INFO     29 [qwen-vl-text] coord item[17]: text=金额合计：13.38, bbox=[464, 687, 790, 712]
2026-08-10 13:27:43,319 INFO     29 [qwen-vl-text] coord item[18]: text=打印时间：2025-04-22 16:36:16, bbox=[127, 710, 721, 735]
2026-08-10 13:27:43,320 INFO     29 [qwen-vl-text] coord item[19]: text=操作员：赵彤, bbox=[128, 735, 361, 759]
2026-08-10 13:27:43,320 INFO     29 [qwen-vl-text] page=8 — 20/20 coords, api_time=7.9s
2026-08-10 13:27:43,320 INFO     29 [qwen-vl-text] new_positions (41):
[[7, 171.95499999999998, 401.03, 28.628, 54.73], [7, 41.65, 97.58, 68.202, 87.568], [7, 304.04499999999996, 456.96, 69.886, 89.252], [7, 41.65, 385.56, 98.514, 117.038], [7, 42.245, 555.135, 127.984, 148.192], [7, 41.65, 371.875, 162.506, 181.03], [7, 43.434999999999995, 149.345, 199.554, 222.28799999999998], [7, 57.714999999999996, 124.94999999999999, 240.81199999999998, 261.86199999999997], [7, 212.415, 271.91499999999996, 244.17999999999998, 260.178], [7, 52.36, 354.025, 400.792, 424.368], [7, 477.78499999999997, 541.4499999999999, 403.318, 421.842], [7, 77.35, 154.7, 428.578, 449.628], [7, 330.22499999999997, 469.455, 430.262, 451.312], [7, 77.945, 181.475, 458.89, 480.782], [7, 330.22499999999997, 495.03999999999996, 461.416, 484.15], [7, 77.945, 248.70999999999998, 489.202, 511.936], [7, 333.2, 507.53499999999997, 494.25399999999996, 516.9879999999999], [7, 77.945, 183.26, 525.408, 548.984], [7, 333.2, 419.47499999999997, 527.934, 550.668], [7, 77.945, 211.225, 558.246, 580.98], [7, 327.84499999999997, 474.81, 559.088, 578.454], [8, 204.67999999999998, 425.42499999999995, 286.28, 313.224], [8, 196.35, 432.565, 317.43399999999997, 343.536], [8, 67.83, 500.395, 351.95599999999996, 374.69], [8, 69.615, 122.57, 383.952, 405.844], [8, 370.685, 547.4, 383.952, 405.844], [8, 69.615, 404.59999999999997, 412.58, 434.472], [8, 71.39999999999999, 404.59999999999997, 437.84, 460.574], [8, 72.59, 157.67499999999998, 470.678, 490.88599999999997], [8, 292.74, 335.58, 471.52, 492.57], [8, 348.66999999999996, 397.46, 471.52, 492.57], [8, 407.575, 451.01, 471.52, 492.57], [8, 512.295, 556.3249999999999, 471.52, 492.57], [8, 70.80499999999999, 235.02499999999998, 506.88399999999996, 525.408], [8, 406.385, 446.25, 508.568, 525.408], [8, 406.385, 427.805, 536.3539999999999, 552.352], [8, 505.75, 555.73, 510.252, 526.25], [8, 77.35, 179.69, 570.876, 592.768], [8, 276.08, 470.04999999999995, 578.454, 599.504], [8, 75.565, 428.995, 597.8199999999999, 618.87], [8, 76.16, 214.795, 618.87, 639.078]]
2026-08-10 13:27:43,320 INFO     29 [qwen-vl-text] ═══ DONE ═══ 41 positions, pages=2, time=17.4s
2026-08-10 13:27:43,330 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 13:27:43,330 INFO     29 [Trace] task=01081162 | doc=HZNA高血糖郑州.pdf | Extractor:Medication | outputs={"chunks": "3 items, types={'MedicationRecord': 3}", "html": "", "json": "206 items", "markdown": "", "text": "", "name": "HZNA高血糖郑州.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_LabExam\": 3, \"chunks_Medication\": 3, \"chunks_Clinical\": 1, \"chunks_Prescription\": 1}"}
2026-08-10 13:27:43,330 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 13:27:43,336 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:27:43,337 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:27:43,337 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 13:27:43,337 INFO     29 [qwen-vl-text] positions(26): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:27:43,337 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [26]
2026-08-10 13:27:43,498 INFO     29 [qwen-vl-text] page=6, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:27:43,499 INFO     29 [qwen-vl-text] LLM extraction start, text_len=238
2026-08-10 13:27:43,499 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:27:43,499 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 138, \"bbox_end\": 163, \"encounter_dates\": [\"2025-04-10\"], \"department\": \"内分泌科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "原阳县人民医院处方笺\n普通\n门诊号：1595205\nNo： 2504105697228\n姓名：.\n性别：男\n年龄：37岁\n科别：内分泌科门诊\n交易号：1053179\n费别：自费\n日期：2025-04-10 10:33:39.0\n地址：河南省原阳县河南省新乡市原阳县\n诊断：2型糖尿病\n慢性病长期用药\nRp:\n-g3盐酸二甲双胍片（0.25g*60片）\n6瓶\n用法：0.5g\n一日三次\n口服\n审核：吴汉铺\n核对：吴汉铺\n医师：胡光环\n调配：吴汉铺\n发药：吴汉铺\n药费：13.38",
    "role": "user"
  }
]
2026-08-10 13:27:45,263 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:27:45.263+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 49, "failed": 0, "current": {"0108116294bf11f1bd9827cf206dfa2d": {"id": "0108116294bf11f1bd9827cf206dfa2d", "doc_id": "00c2e26894bf11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HZNA\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "type": "pdf", "location": "HZNA\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "size": 7585233, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368350219, "task_type": "dataflow", "root_trace_id": "76162b34ec514c059d062d6d34315295", "root_traceparent": "00-76162b34ec514c059d062d6d34315295-096f88c2095fe0e3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:27:46,018 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:27:46,018 INFO     29 [qwen-vl-text] LLM output (len=418):
{
  "encounter_date": "2025-04-10",
  "prescription_type": "门诊处方",
  "prescriber": "胡光环",
  "department": "内分泌科门诊",
  "diagnosis": "2型糖尿病",
  "items": [
    {
      "drug_generic_name": "盐酸二甲双胍片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "0.5g",
      "frequency": "一日三次",
      "route": "口服",
      "duration_days": null,
      "quantity": "6瓶",
      "notes": "慢性病长期用药"
    }
  ]
}
2026-08-10 13:27:46,018 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-04-10]
2026-08-10 13:27:46,020 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=457976, prompt_len=929
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["原阳县人民医院处方笺", "普通", "门诊号：1595205", "No： 2504105697228", "姓名：.", "性别：男", "年龄：37岁", "科别：内分泌科门诊", "交易号：1053179", "费别：自费", "日期：2025-04-10 10:33:39.0", "地址：河南省原阳县河南省新乡市原阳县", "诊断：2型糖尿病", "慢性病长期用药", "Rp:", "-g3盐酸二甲双胍片（0.25g*60片）", "6瓶", "用法：0.5g", "一日三次", "口服", "审核：吴汉铺", "核对：吴汉铺", "医师：胡光环", "调配：吴汉铺", "发药：吴汉铺", "药费：13.38"]

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
2026-08-10 13:27:53,751 INFO     29 [qwen-vl-text] coord API raw response (len=1379):
[
	{"text": "原阳县人民医院处方笺", "bbox": [280, 52, 560, 72]},
	{"text": "普通", "bbox": [674, 61, 716, 75]},
	{"text": "门诊号：1595205", "bbox": [150, 94, 312, 108]},
	{"text": "No： 2504105697228", "bbox": [508, 95, 702, 108]},
	{"text": "姓名：.", "bbox": [150, 118, 223, 132]},
	{"text": "性别：男", "bbox": [381, 117, 465, 131]},
	{"text": "年龄：37岁", "bbox": [508, 117, 614, 131]},
	{"text": "科别：内分泌科门诊", "bbox": [150, 139, 347, 153]},
	{"text": "交易号：1053179", "bbox": [508, 138, 670, 152]},
	{"text": "费别：自费", "bbox": [150, 160, 260, 175]},
	{"text": "日期：2025-04-10 10:33:39.0", "bbox": [483, 160, 775, 174]},
	{"text": "地址：河南省原阳县河南省新乡市原阳县", "bbox": [150, 181, 537, 195]},
	{"text": "诊断：2型糖尿病", "bbox": [152, 203, 295, 216]},
	{"text": "慢性病长期用药", "bbox": [560, 203, 675, 216]},
	{"text": "Rp:", "bbox": [162, 246, 217, 272]},
	{"text": "-g3盐酸二甲双胍片（0.25g*60片）", "bbox": [194, 284, 527, 300]},
	{"text": "6瓶", "bbox": [690, 283, 723, 297]},
	{"text": "用法：0.5g", "bbox": [234, 307, 338, 323]},
	{"text": "一日三次", "bbox": [427, 306, 508, 321]},
	{"text": "口服", "bbox": [560, 306, 602, 321]},
	{"text": "审核：吴汉铺", "bbox": [179, 712, 377, 748]},
	{"text": "核对：吴汉铺", "bbox": [408, 712, 625, 754]},
	{"text": "医师：胡光环", "bbox": [665, 718, 880, 757]},
	{"text": "调配：吴汉铺", "bbox": [182, 755, 381, 800]},
	{"text": "发药：吴汉铺", "bbox": [411, 757, 624, 800]},
	{"text": "药费：13.38", "bbox": [663, 762, 803, 781]}
]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=7.7s
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[0]: text=原阳县人民医院处方笺, bbox=[280, 52, 560, 72]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[1]: text=普通, bbox=[674, 61, 716, 75]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[2]: text=门诊号：1595205, bbox=[150, 94, 312, 108]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[3]: text=No： 2504105697228, bbox=[508, 95, 702, 108]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：., bbox=[150, 118, 223, 132]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[5]: text=性别：男, bbox=[381, 117, 465, 131]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[6]: text=年龄：37岁, bbox=[508, 117, 614, 131]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[7]: text=科别：内分泌科门诊, bbox=[150, 139, 347, 153]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[8]: text=交易号：1053179, bbox=[508, 138, 670, 152]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[9]: text=费别：自费, bbox=[150, 160, 260, 175]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[10]: text=日期：2025-04-10 10:33:39.0, bbox=[483, 160, 775, 174]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[11]: text=地址：河南省原阳县河南省新乡市原阳县, bbox=[150, 181, 537, 195]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[12]: text=诊断：2型糖尿病, bbox=[152, 203, 295, 216]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[13]: text=慢性病长期用药, bbox=[560, 203, 675, 216]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[14]: text=Rp:, bbox=[162, 246, 217, 272]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[15]: text=-g3盐酸二甲双胍片（0.25g*60片）, bbox=[194, 284, 527, 300]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[16]: text=6瓶, bbox=[690, 283, 723, 297]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[17]: text=用法：0.5g, bbox=[234, 307, 338, 323]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[18]: text=一日三次, bbox=[427, 306, 508, 321]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[19]: text=口服, bbox=[560, 306, 602, 321]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[20]: text=审核：吴汉铺, bbox=[179, 712, 377, 748]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[21]: text=核对：吴汉铺, bbox=[408, 712, 625, 754]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[22]: text=医师：胡光环, bbox=[665, 718, 880, 757]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[23]: text=调配：吴汉铺, bbox=[182, 755, 381, 800]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[24]: text=发药：吴汉铺, bbox=[411, 757, 624, 800]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] coord item[25]: text=药费：13.38, bbox=[663, 762, 803, 781]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] page=6 — 26/26 coords, api_time=7.7s
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] new_positions (26):
[[6, 166.6, 333.2, 43.784, 60.623999999999995], [6, 401.03, 426.02, 51.361999999999995, 63.15], [6, 89.25, 185.64, 79.148, 90.93599999999999], [6, 302.26, 417.69, 79.99, 90.93599999999999], [6, 89.25, 132.685, 99.356, 111.14399999999999], [6, 226.695, 276.675, 98.514, 110.30199999999999], [6, 302.26, 365.33, 98.514, 110.30199999999999], [6, 89.25, 206.465, 117.038, 128.826], [6, 302.26, 398.65, 116.196, 127.984], [6, 89.25, 154.7, 134.72, 147.35], [6, 287.385, 461.125, 134.72, 146.50799999999998], [6, 89.25, 319.515, 152.402, 164.19], [6, 90.44, 175.525, 170.926, 181.87199999999999], [6, 333.2, 401.625, 170.926, 181.87199999999999], [6, 96.39, 129.11499999999998, 207.132, 229.024], [6, 115.42999999999999, 313.565, 239.128, 252.6], [6, 410.54999999999995, 430.185, 238.286, 250.07399999999998], [6, 139.23, 201.10999999999999, 258.49399999999997, 271.966], [6, 254.065, 302.26, 257.652, 270.282], [6, 333.2, 358.19, 257.652, 270.282], [6, 106.505, 224.315, 599.504, 629.816], [6, 242.76, 371.875, 599.504, 634.8679999999999], [6, 395.67499999999995, 523.6, 604.5559999999999, 637.394], [6, 108.28999999999999, 226.695, 635.7099999999999, 673.6], [6, 244.545, 371.28, 637.394, 673.6], [6, 394.48499999999996, 477.78499999999997, 641.6039999999999, 657.602]]
2026-08-10 13:27:53,752 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=10.4s
2026-08-10 13:27:53,764 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 13:27:53,764 INFO     29 [Trace] task=01081162 | doc=HZNA高血糖郑州.pdf | Extractor:Prescription | outputs={"chunks": "1 items, types={'PrescriptionRecord': 1}", "html": "", "json": "206 items", "markdown": "", "text": "", "name": "HZNA高血糖郑州.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_LabExam\": 3, \"chunks_Medication\": 3, \"chunks_Clinical\": 1, \"chunks_Prescription\": 1}"}
2026-08-10 13:27:53,764 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 13:27:53,769 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:27:53,770 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:27:53,770 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 13:27:53,770 INFO     29 [qwen-vl-text] positions(22): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:27:53,770 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [22]
2026-08-10 13:27:53,952 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:27:53,953 INFO     29 [qwen-vl-text] LLM extraction start, text_len=365
2026-08-10 13:27:53,953 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:27:53,953 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 0, \"bbox_end\": 21, \"encounter_dates\": [\"2024-11-21\", \"2024-11-24\"], \"department\": \"科二病区\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "民医院\n出院证\n住院号：024\n医疗保险证号：\n姓名：\n性别：男\n年龄：37岁 床号：11床\n籍贯：河南省\n住址：河南省\n入院时间：2024-11-21 19:58\n出院时间：2024-11-24\n出院诊断：1.社区获得性肺炎，非重症 2.后循环缺血 3.2型糖尿病伴血糖控制不佳 4.冠状动\n脉狭窄 5.脂肪肝 6.甲状腺结节\n出院医嘱：[1.适当运动，控制体重；2.监测血糖，规律服药，二甲双胍缓释片0.5g 1天3次，\n1次1片；依折麦布片10mg 1天1次，1次1片；莫西沙星片0.4g 1天1次，1次1片，肺力咳合剂\n100ml 1天3次，1次10ml(咳\n转停药)；3.戒烟酒，定期复查血脂血糖，肝肾功能，\n避免受凉，不适随诊]\n科二病区医师签名：\n盖章2024-11-24\n达疗业务专用章\n4102251063701",
    "role": "user"
  }
]
2026-08-10 13:28:00,461 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:28:00,461 INFO     29 [qwen-vl-text] LLM output (len=1499):
{
  "encounter_date": "2024-11-24",
  "admission_date": "2024-11-21",
  "discharge_date": "2024-11-24",
  "hospital_days": 3,
  "department": "科二病区",
  "bed_number": "11床",
  "admission_condition": null,
  "admission_diagnoses": [],
  "treatment_summary": null,
  "auxiliary_exams": null,
  "imaging_findings": null,
  "discharge_diagnoses": [
    {
      "name": "社区获得性肺炎，非重症",
      "diagnosis_type": "西医"
    },
    {
      "name": "后循环缺血",
      "diagnosis_type": "西医"
    },
    {
      "name": "2型糖尿病伴血糖控制不佳",
      "diagnosis_type": "西医"
    },
    {
      "name": "冠状动脉狭窄",
      "diagnosis_type": "西医"
    },
    {
      "name": "脂肪肝",
      "diagnosis_type": "西医"
    },
    {
      "name": "甲状腺结节",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": null,
  "outcome": null,
  "discharge_orders": "1.适当运动，控制体重；2.监测血糖，规律服药，二甲双胍缓释片0.5g 1天3次，1次1片；依折麦布片10mg 1天1次，1次1片；莫西沙星片0.4g 1天1次，1次1片，肺力咳合剂100ml 1天3次，1次10ml(咳转停药)；3.戒烟酒，定期复查血脂血糖，肝肾功能，避免受凉，不适随诊",
  "do_medications": [
    "二甲双胍缓释片 0.5g 1天3次 1次1片",
    "依折麦布片 10mg 1天1次 1次1片",
    "莫西沙星片 0.4g 1天1次 1次1片",
    "肺力咳合剂 10ml 1天3次 1次10ml"
  ],
  "do_follow_up": "定期复查血脂血糖，肝肾功能，不适随诊",
  "do_precautions": [
    "适当运动，控制体重",
    "监测血糖，规律服药",
    "戒烟酒",
    "避免受凉"
  ],
  "next_treatment_date": null,
  "attending_physician": null,
  "pe_ecog_score": null,
  "body_surface_area": null,
  "vs_temperature_c": null,
  "vs_pulse_bpm": null,
  "vs_respiration_rpm": null,
  "vs_systolic_bp_mmhg": null,
  "vs_diastolic_bp_mmhg": null
}
2026-08-10 13:28:00,461 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-11-24]
2026-08-10 13:28:00,462 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=689929, prompt_len=1044
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["民医院", "出院证", "住院号：024", "医疗保险证号：", "姓名：", "性别：男", "年龄：37岁 床号：11床", "籍贯：河南省", "住址：河南省", "入院时间：2024-11-21 19:58", "出院时间：2024-11-24", "出院诊断：1.社区获得性肺炎，非重症 2.后循环缺血 3.2型糖尿病伴血糖控制不佳 4.冠状动", "脉狭窄 5.脂肪肝 6.甲状腺结节", "出院医嘱：[1.适当运动，控制体重；2.监测血糖，规律服药，二甲双胍缓释片0.5g 1天3次，", "1次1片；依折麦布片10mg 1天1次，1次1片；莫西沙星片0.4g 1天1次，1次1片，肺力咳合剂", "100ml 1天3次，1次10ml(咳", "转停药)；3.戒烟酒，定期复查血脂血糖，肝肾功能，", "避免受凉，不适随诊]", "科二病区医师签名：", "盖章2024-11-24", "达疗业务专用章", "4102251063701"]

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
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord API raw response (len=1323):
[
	{"text": "民医院", "bbox": [508, 46, 627, 72]},
	{"text": "出院证", "bbox": [423, 85, 570, 111]},
	{"text": "住院号：024", "bbox": [765, 180, 887, 197]},
	{"text": "医疗保险证号：", "bbox": [786, 209, 916, 226]},
	{"text": "姓名：", "bbox": [62, 240, 132, 257]},
	{"text": "性别：男", "bbox": [335, 240, 420, 257]},
	{"text": "年龄：37岁 床号：11床", "bbox": [608, 240, 823, 257]},
	{"text": "籍贯：河南省", "bbox": [62, 269, 198, 287]},
	{"text": "住址：河南省", "bbox": [335, 269, 480, 287]},
	{"text": "入院时间：2024-11-21 19:58", "bbox": [64, 299, 338, 316]},
	{"text": "出院时间：2024-11-24", "bbox": [64, 329, 275, 346]},
	{"text": "出院诊断：1.社区获得性肺炎，非重症 2.后循环缺血 3.2型糖尿病伴血糖控制不佳 4.冠状动", "bbox": [64, 357, 915, 375]},
	{"text": "脉狭窄 5.脂肪肝 6.甲状腺结节", "bbox": [64, 386, 358, 404]},
	{"text": "出院医嘱：[1.适当运动，控制体重；2.监测血糖，规律服药，二甲双胍缓释片0.5g 1天3次，", "bbox": [64, 414, 902, 433]},
	{"text": "1次1片；依折麦布片10mg 1天1次，1次1片；莫西沙星片0.4g 1天1次，1次1片，肺力咳合剂", "bbox": [65, 443, 894, 462]},
	{"text": "100ml 1天3次，1次10ml(咳", "bbox": [65, 473, 320, 491]},
	{"text": "转停药)；3.戒烟酒，定期复查血脂血糖，肝肾功能，", "bbox": [404, 472, 891, 490]},
	{"text": "避免受凉，不适随诊]", "bbox": [64, 502, 262, 520]},
	{"text": "科二病区医师签名：", "bbox": [657, 539, 830, 557]},
	{"text": "盖章2024-11-24", "bbox": [770, 570, 918, 587]},
	{"text": "达疗业务专用章", "bbox": [617, 570, 752, 610]},
	{"text": "4102251063701", "bbox": [625, 595, 735, 626]}
]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=7.8s
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[0]: text=民医院, bbox=[508, 46, 627, 72]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[1]: text=出院证, bbox=[423, 85, 570, 111]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[2]: text=住院号：024, bbox=[765, 180, 887, 197]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[3]: text=医疗保险证号：, bbox=[786, 209, 916, 226]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[62, 240, 132, 257]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[5]: text=性别：男, bbox=[335, 240, 420, 257]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[6]: text=年龄：37岁 床号：11床, bbox=[608, 240, 823, 257]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[7]: text=籍贯：河南省, bbox=[62, 269, 198, 287]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[8]: text=住址：河南省, bbox=[335, 269, 480, 287]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[9]: text=入院时间：2024-11-21 19:58, bbox=[64, 299, 338, 316]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[10]: text=出院时间：2024-11-24, bbox=[64, 329, 275, 346]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[11]: text=出院诊断：1.社区获得性肺炎，非重症 2.后循环缺血 3.2型糖尿病伴血糖控制不佳 4.冠状动, bbox=[64, 357, 915, 375]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[12]: text=脉狭窄 5.脂肪肝 6.甲状腺结节, bbox=[64, 386, 358, 404]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[13]: text=出院医嘱：[1.适当运动，控制体重；2.监测血糖，规律服药，二甲双胍缓释片0.5g 1天3次，, bbox=[64, 414, 902, 433]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[14]: text=1次1片；依折麦布片10mg 1天1次，1次1片；莫西沙星片0.4g 1天1次，1次1片，肺力咳合剂, bbox=[65, 443, 894, 462]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[15]: text=100ml 1天3次，1次10ml(咳, bbox=[65, 473, 320, 491]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[16]: text=转停药)；3.戒烟酒，定期复查血脂血糖，肝肾功能，, bbox=[404, 472, 891, 490]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[17]: text=避免受凉，不适随诊], bbox=[64, 502, 262, 520]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[18]: text=科二病区医师签名：, bbox=[657, 539, 830, 557]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[19]: text=盖章2024-11-24, bbox=[770, 570, 918, 587]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[20]: text=达疗业务专用章, bbox=[617, 570, 752, 610]
2026-08-10 13:28:08,240 INFO     29 [qwen-vl-text] coord item[21]: text=4102251063701, bbox=[625, 595, 735, 626]
2026-08-10 13:28:08,241 INFO     29 [qwen-vl-text] page=0 — 22/22 coords, api_time=7.8s
2026-08-10 13:28:08,241 INFO     29 [qwen-vl-text] new_positions (22):
[[0, 302.26, 373.065, 38.732, 60.623999999999995], [0, 251.685, 339.15, 71.57, 93.462], [0, 455.17499999999995, 527.765, 151.56, 165.874], [0, 467.66999999999996, 545.02, 175.97799999999998, 190.292], [0, 36.89, 78.53999999999999, 202.07999999999998, 216.394], [0, 199.325, 249.89999999999998, 202.07999999999998, 216.394], [0, 361.76, 489.685, 202.07999999999998, 216.394], [0, 36.89, 117.80999999999999, 226.498, 241.654], [0, 199.325, 285.59999999999997, 226.498, 241.654], [0, 38.08, 201.10999999999999, 251.75799999999998, 266.072], [0, 38.08, 163.625, 277.018, 291.332], [0, 38.08, 544.425, 300.594, 315.75], [0, 38.08, 213.01, 325.012, 340.168], [0, 38.08, 536.6899999999999, 348.58799999999997, 364.586], [0, 38.675, 531.93, 373.006, 389.00399999999996], [0, 38.675, 190.39999999999998, 398.26599999999996, 413.42199999999997], [0, 240.38, 530.145, 397.424, 412.58], [0, 38.08, 155.89, 422.68399999999997, 437.84], [0, 390.91499999999996, 493.84999999999997, 453.83799999999997, 468.99399999999997], [0, 458.15, 546.2099999999999, 479.94, 494.25399999999996], [0, 367.115, 447.44, 479.94, 513.62], [0, 371.875, 437.325, 500.99, 527.092]]
2026-08-10 13:28:08,241 INFO     29 [qwen-vl-text] ═══ DONE ═══ 22 positions, pages=1, time=14.5s
2026-08-10 13:28:08,246 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 13:28:08,247 INFO     29 [Trace] task=01081162 | doc=HZNA高血糖郑州.pdf | Extractor:Discharge | outputs={"chunks": "1 items, types={'DischargeRecord': 1}", "html": "", "json": "206 items", "markdown": "", "text": "", "name": "HZNA高血糖郑州.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_LabExam\": 3, \"chunks_Medication\": 3, \"chunks_Clinical\": 1, \"chunks_Prescription\": 1}"}
2026-08-10 13:28:08,247 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 13:28:08,255 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:28:08,255 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:28:09,620 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:28:09,629 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 13:28:09,629 INFO     29 [Trace] task=01081162 | doc=HZNA高血糖郑州.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "206 items", "markdown": "", "text": "", "name": "HZNA高血糖郑州.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_LabExam\": 3, \"chunks_Medication\": 3, \"chunks_Clinical\": 1, \"chunks_Prescription\": 1}"}
2026-08-10 13:28:09,629 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 13:28:09,633 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:28:09,633 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:28:12,290 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:28:12,302 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 13:28:12,302 INFO     29 [Trace] task=01081162 | doc=HZNA高血糖郑州.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "206 items", "markdown": "", "text": "", "name": "HZNA高血糖郑州.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_LabExam\": 3, \"chunks_Medication\": 3, \"chunks_Clinical\": 1, \"chunks_Prescription\": 1}"}
2026-08-10 13:28:12,302 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 13:28:12,311 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:28:12,311 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:28:12,799 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:28:12,805 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 13:28:12,805 INFO     29 [Trace] task=01081162 | doc=HZNA高血糖郑州.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "206 items", "markdown": "", "text": "", "name": "HZNA高血糖郑州.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_LabExam\": 3, \"chunks_Medication\": 3, \"chunks_Clinical\": 1, \"chunks_Prescription\": 1}"}
2026-08-10 13:28:12,806 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 13:28:12,806 INFO     29 [ChunkMerger] Merged 9 chunks from 9 sources: {'Extractor:LabExam': 3, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 3, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 4 noise chunks)
2026-08-10 13:28:12,817 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 13:28:12,817 INFO     29 [Trace] task=01081162 | doc=HZNA高血糖郑州.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "9 items, types={'LabReport': 3, 'OutpatientRecord': 1, 'MedicationRecord': 3, 'PrescriptionRecord': 1, 'DischargeRecord': 1}", "name": "HZNA高血糖郑州.pdf"}
2026-08-10 13:28:12,817 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 13:28:12,867 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786368353684, 'update_date': datetime.datetime(2026, 8, 10, 13, 25, 53), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1038266, 'status': '1'}
2026-08-10 13:28:13,062 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   糖化血红蛋白  HbA1C  10.20  %  4.5--6.5  True   
---
   随机血糖  SJXT  16.37  mmol/L  None  False   
---
   糖化血红蛋白  HbA1C  9.10  %  4.5--6.5  True   
---
原阳县人民医院
门诊病历
门诊号：135700000737
姓名：
性别：男
年龄：37岁
婚否：已婚
民族：汉族
职业：工人
身份证号：
邮编：453500
籍贯：河南省新乡市
现住址：河南省新乡市
X线号：
工作单位：
联系电
心电图号：
初诊科别：内分泌科门诊
初诊日期：2025-02-25
过敏史：无
主诉：发现血糖高半年余
现病史：半年前发现血糖高，空腹血糖13mmol/L，平时口服二甲双胍片0.5g 每日三次，
监测空腹及餐后血糖仍高，门诊就诊。
既往史：既往体健，无肝炎、结核、疟疾病史，无高血压、心脏疾病病史，无手术、外
伤、输血史
婚育史：已婚。
家族史：无家族性遗传病史。
体格检查：BMI：38Kg/m²神志清，精神可，体型肥胖，心肺听诊无明显异常，双下肢无水肿
辅助检查：血糖 糖化
门诊诊断：
1、2型糖尿病
门诊处置：无
诊疗意见:药物治疗、如有不适，请随时复诊
医师签名：胡志环
签名日期：2025-04-10 10:34
---
天医院
门诊患者费用清单(汇总)
证件号:4107251
姓名.
卡号:4
开始时间: 2025-01-01 00:00
结束时间: 2025-03-13:59
项目名称 单价 单位 数量 金额
-g3盐酸二甲双胍缓释
.086 片 64.0 5.50
片
病历资料复印 0.4 每张 26.0 10.40
糖化血红蛋白全定量 256 项 1.00 25.00
测定
静脉注射 3.8 次 1.00 3.80
血糖测定 6 次 1.00 6.00
共计:5项 金额合计:¥50.70
打印时间:2025-03-13 10:13:36
操作员.
扫描二维码下载电子发票
此单据作为就诊凭证,请不要随意丢弃
---
中心药店
日期: 2025 02 15 19:20:00
销售员: 毛爱青
药品名称
生产厂商
批号
规格
数量
单位
单价
金额
盐酸二甲双胍肠溶片
贵州天安药业股份有限公司
20240242
0.5g/60
3.00
瓶
20.00
60.00
应收 60.00 实收 60.00
找回 0.00 中药付 1.00
地址: 原阳县西干道
电话: 7282955
会员卡:
本次积分: 60
积分余额: 260
原额: 0.00
余额: 0
药品为特殊商品无质量问题
概不退换
社会主核心价值观
富强 民主 文明 和谐
自由 平等 公正 法治
---
原阳县人民医院
姓名：
医保类别：自费
收费时间：2025-04-10 00:00:00
发票号：41060135H1005655423门诊号：1595205
患者卡号：410725198706033639
费用分类
西药费
13.38
金额：壹拾叁圆叁角捌分
13.38
现金：0
账户：13.38
银联卡：0
医保账户：0.0
医保统筹：0.0
个人自付：0.0
支付宝：0
微信：0
账户余额：0
医保账户余额：
原阳县人民医院
门诊患者费用清单
卡号：410725198706033639 账户余额：0
姓名：
流水号：1595205
开始时间：2025-04-10 10:33
结束时间：2025-04-10 10:33
项目名称
单价
单位
数量
金额
-g3盐酸二甲双胍片
3.60
60
13.38
共计：1项
金额合计：13.38
打印时间：2025-04-22 16:36:16
操作员：赵彤
---
原阳县人民医院处方笺
普通
门诊号：1595205
No： 2504105697228
姓名：.
性别：男
年龄：37岁
科别：内分泌科门诊
交易号：1053179
费别：自费
日期：2025-04-10 10:33:39.0
地址：河南省原阳县河南省新乡市原阳县
诊断：2型糖尿病
慢性病长期用药
Rp:
-g3盐酸二甲双胍片（0.25g*60片）
6瓶
用法：0.5g
一日三次
口服
审核：吴汉铺
核对：吴汉铺
医师：胡光环
调配：吴汉铺
发药：吴汉铺
药费：13.38
---
民医院
出院证
住院号：024
医疗保险证号：
姓名：
性别：男
年龄：37岁 床号：11床
籍贯：河南省
住址：河南省
入院时间：2024-11-21 19:58
出院时间：2024-11-24
出院诊断：1.社区获得性肺炎，非重症 2.后循环缺血 3.2型糖尿病伴血糖控制不佳 4.冠状动
脉狭窄 5.脂肪肝 6.甲状腺结节
出院医嘱：[1.适当运动，控制体重；2.监测血糖，规律服药，二甲双胍缓释片0.5g 1天3次，
1次1片；依折麦布片10mg 1天1次，1次1片；莫西沙星片0.4g 1天1次，1次1片，肺力咳合剂
100ml 1天3次，1次10ml(咳
转停药)；3.戒烟酒，定期复查血脂血糖，肝肾功能，
避免受凉，不适随诊]
科二病区医师签名：
盖章2024-11-24
达疗业务专用章
4102251063701
2026-08-10 13:28:13,448 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 13:28:13,448 INFO     29 [Trace] task=01081162 | doc=HZNA高血糖郑州.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "9 items, types={'LabReport': 3, 'OutpatientRecord': 1, 'MedicationRecord': 3, 'PrescriptionRecord': 1, 'DischargeRecord': 1}", "name": "HZNA高血糖郑州.pdf", "embedding_token_consumption": 1779}
2026-08-10 13:28:13,448 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 13:28:13,693 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 13:28:13,693 INFO     29 [Trace] task=01081162 | doc=HZNA高血糖郑州.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":9,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 13:28:13,697 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(2, 191, 257, 161, 171) row[-1]=(2, 191, 257, 161, 171)
2026-08-10 13:28:13,697 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(4, 113, 152, 104, 113) row[-1]=(4, 113, 152, 104, 113)
2026-08-10 13:28:13,697 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(4, 104, 158, 508, 518) row[-1]=(4, 104, 158, 508, 518)
2026-08-10 13:28:13,697 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:28:13,697 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:28:13,697 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:28:13,697 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:28:13,698 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:28:13,698 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:28:13,702 INFO     29 set_progress(0108116294bf11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 13:28:13 [DOC Engine]:
Start to index...
2026-08-10 13:28:13,718 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.011s]
2026-08-10 13:28:13,722 INFO     29 set_progress(0108116294bf11f1bd9827cf206dfa2d), progress: 0.8111111111111111, progress_msg: 
2026-08-10 13:28:13,735 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.007s]
2026-08-10 13:28:13,745 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.006s]
2026-08-10 13:28:13,752 INFO     29 set_progress(0108116294bf11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 13:28:13 Indexing done (0.05s). Task done (132.84s)
2026-08-10 13:28:13,755 INFO     29 [Done], chunks(9), token(1779), elapsed:132.84
2026-08-10 13:28:13,859 INFO     29 handle_task done for task {"id": "0108116294bf11f1bd9827cf206dfa2d", "doc_id": "00c2e26894bf11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HZNA\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "type": "pdf", "location": "HZNA\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "size": 7585233, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786368350219, "task_type": "dataflow", "root_trace_id": "76162b34ec514c059d062d6d34315295", "root_traceparent": "00-76162b34ec514c059d062d6d34315295-096f88c2095fe0e3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
