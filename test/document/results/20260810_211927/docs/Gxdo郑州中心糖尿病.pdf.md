# 基准结果：Gxdo郑州中心糖尿病.pdf

## 基本信息

- 文件：`Gxdo郑州中心糖尿病.pdf`
- 大小：1439.7 KB
- PDF 总页数：6
- doc_id：`c6bfa85894be11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T21:24:11  完成时间：2026-08-10T21:25:48  耗时：97.2s
- progress_msg：`13:25:38 Indexing done (0.04s). Task done (80.53s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 55c31932 | 1 | 1-1 | 中西医结合医院 病人门（急）诊病历 病人ID M024274 姓名 性别：男 出 |
| 2 | fc92158d | 1 | 3-3 | 普通 .中西医结合医院处方笺 姓名： 性别：男 年龄：53岁 费别：自费 病人I |
| 3 | 079b65ba | 2 | 4-5 | 顺中西医结合医院 527647 自费 西药费 60.00 大额记账: 大病补充: |
| 4 | b10d531c | 1 | 5-5 | 中西医结合医院处方笺 姓名： 性别：男 年龄：53岁 费别：自费 病人ID：M0 |
| 5 | 17530626 | 1 | 6-6 | 529576 0061 2025-03-2 江顺中西医结合医院 529576 男 |
| 6 | 0d7b2912 | 1 | 2-2 | <table><tr><td>糖化血红蛋白测定</td><td>HbA1c</t |

- chunks 总数：6
- 各 chunk 页数合计（含跨页重复）：7
- 页码并集：`[1, 2, 3, 4, 5, 6]`
- 覆盖页数：6 / 6；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 1 | 0 | 1 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 2 | 2 | 2 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 2 | 2 | 2 | encounter_date, prescriber, diagnosis | **OK** |
| ExaminationReport | 检查报告 | 0 | 1 | 0 | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 1 | 0 | 1 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 1, "LabReport": 1, "PrescriptionRecord": 2, "MedicationRecord": 2}`
- ChunkMerger：`{"found": true, "merged": 6, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 2, "Extractor:Prescription": 2, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 5}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 13:25:37,372 INFO     29 [ChunkMerger] Merged 6 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 2, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 13:24:12,939 INFO     29 handle_task begin for task {"id": "c6f37d0494be11f1bd9827cf206dfa2d", "doc_id": "c6bfa85894be11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Gxdo\u90d1\u5dde\u4e2d\u5fc3\u7cd6\u5c3f\u75c5.pdf", "type": "pdf", "location": "Gxdo\u90d1\u5dde\u4e2d\u5fc3\u7cd6\u5c3f\u75c5.pdf", "size": 1474288, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368252776, "task_type": "dataflow", "root_trace_id": "0739225e0c644d63a7cc49e0ecacc097", "root_traceparent": "00-0739225e0c644d63a7cc49e0ecacc097-05128704d7f5e09a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 13:24:13,157 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.002s]
2026-08-10 13:24:13,263 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 13:24:13,271 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:24:13,271 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 13:24:13,271 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 13:24:13,289 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 13:24:13,289 INFO     29 ============================================================
2026-08-10 13:24:13,290 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 13:24:13,290 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 13:24:13,290 INFO     29 ============================================================
2026-08-10 13:24:13,290 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 13:24:13,290 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 13:24:13,292 INFO     29 No torch found.
2026-08-10 13:24:14,080 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=6
2026-08-10 13:24:14,181 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=776877, prompt_len=764
2026-08-10 13:24:15,451 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:24:15,452 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 13:24:15,466 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=776877, prompt_len=401
2026-08-10 13:24:18,409 INFO     29 [qwen-vl-parser] text API response (len=483):
["中西医结合医院", "病人门（急）诊病历", "病人ID M024274 姓名", "性别：男 出生时间： 1972年03月01日", "籍贯： 汉族 婚否：已婚 职业：无", "身份证号： 电话号码：", "工作单位： 常住地址：新密市大隗镇", "门诊号： 71603 接诊时间： 2025年3月26日 14时29分", "就诊时间：2025-03-26 14:29:04 体温：36.5 ℃", "主诉：糖尿病20年", "现病史：20年前出现多饮、多尿、多食，曾规律服用二甲双胍缓释片，格列本脲", "片，消渴丸等药，血糖控制不佳，为求进一步治疗前来就诊。", "体格检查：", "西医诊断：1.糖尿病 中医诊断：", "建议： 1、糖尿病饮食；保持心情愉悦；", "2、适量运动；", "3、规律服药；", "4、定期监测血糖；", "5、不适随诊。", "过敏史：无", "家族史：有", "既往史：无", "处理：给予空腹血糖、糖化血红蛋白检测，以了解血糖控制情况", "备注：", "打印时间：2025.3.26 科室：内科门诊 医生：张建鹏"]
2026-08-10 13:24:18,410 INFO     29 [qwen-vl-parser] page=1 text: 25 lines (bbox 0-24)
2026-08-10 13:24:18,411 INFO     29 [qwen-vl-parser] page=1 text: 25 sections
2026-08-10 13:24:18,505 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=453121, prompt_len=764
2026-08-10 13:24:19,951 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-03-26"
}
```
2026-08-10 13:24:19,951 INFO     29 [qwen-vl-parser] page=2 classify=table report_date=2025-03-26
2026-08-10 13:24:19,957 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=453121, prompt_len=756
2026-08-10 13:24:22,115 INFO     29 [qwen-vl-parser] table API response (len=380):
\begin{tabular}{|l|l|l|l|l|l|}
\hline
姓名 & 性别: 男 & 年龄: 53 & 送检科室: 门诊 & 标本状态: 正常 & 标本类型: 静脉全血 \\
\hline
\multicolumn{5}{|l|}{} & 送检日期: 2025-03-26 \\
\hline
项目名称 & \multicolumn{3}{c|}{结果} & \multicolumn{2}{c|}{参考范围} \\
\hline
糖化血红蛋白测定 (HbA1c) & \multicolumn{3}{c|}{10.7\%} & \multicolumn{2}{c|}{4-6\%} \\
\hline
\end{tabular}

送检医师: 马中杰 检验师: 裴巧玲 审核者: 裴巧玲 报告时间: 2025-03-26
此结果仅对该标本负责
2026-08-10 13:24:22,116 INFO     29 [qwen-vl-parser] page=2 table: 14 LaTeX lines (bbox 25-38)
2026-08-10 13:24:22,116 INFO     29 [qwen-vl-parser] page=2 table: 14 sections
2026-08-10 13:24:22,204 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=463458, prompt_len=764
2026-08-10 13:24:23,552 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:24:23,552 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 13:24:23,557 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=463458, prompt_len=401
2026-08-10 13:24:25,542 INFO     29 [qwen-vl-parser] text API response (len=335):
["普通", ".中西医结合医院处方笺", "姓名：", "性别：男", "年龄：53岁", "费别：自费", "病人ID：M024274", "处方号：71603", "就诊序号：51869", "体重：/（kg）", "药物过敏史：无", "住址：新密市", "开方日期：2024-12-30", "08：16", "就诊科室：内科门诊", "临床诊断：糖", "Rp:", "盐酸二甲双胍片", "0.5g*60 X 6盒", "用法：每次0.5g 一日三次 口服", "备注：", "医师：张建鹏", "审核：", "核对：", "金额合计：60.00元", "调配：", "发药：", "药房：西药费", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 13:24:25,543 INFO     29 [qwen-vl-parser] page=3 text: 30 lines (bbox 39-68)
2026-08-10 13:24:25,543 INFO     29 [qwen-vl-parser] page=3 text: 30 sections
2026-08-10 13:24:25,546 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:24:25.545+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 48, "failed": 0, "current": {"c6f37d0494be11f1bd9827cf206dfa2d": {"id": "c6f37d0494be11f1bd9827cf206dfa2d", "doc_id": "c6bfa85894be11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Gxdo\u90d1\u5dde\u4e2d\u5fc3\u7cd6\u5c3f\u75c5.pdf", "type": "pdf", "location": "Gxdo\u90d1\u5dde\u4e2d\u5fc3\u7cd6\u5c3f\u75c5.pdf", "size": 1474288, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368252776, "task_type": "dataflow", "root_trace_id": "0739225e0c644d63a7cc49e0ecacc097", "root_traceparent": "00-0739225e0c644d63a7cc49e0ecacc097-05128704d7f5e09a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:24:25,636 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=551936, prompt_len=764
2026-08-10 13:24:26,866 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:24:26,867 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 13:24:26,888 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=551936, prompt_len=401
2026-08-10 13:24:27,817 INFO     29 [qwen-vl-parser] text API response (len=123):
["顺中西医结合医院", "527647", "自费", "西药费", "60.00", "大额记账:", "大病补充:", "原账户余额:", "已审核", "现金支付:", "陆拾元整", "60.00", "527647", "0061"]
2026-08-10 13:24:27,818 INFO     29 [qwen-vl-parser] page=4 text: 14 lines (bbox 69-82)
2026-08-10 13:24:27,818 INFO     29 [qwen-vl-parser] page=4 text: 14 sections
2026-08-10 13:24:27,911 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=502164, prompt_len=764
2026-08-10 13:24:29,184 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:24:29,184 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 13:24:29,194 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=502164, prompt_len=401
2026-08-10 13:24:32,924 INFO     29 [qwen-vl-parser] text API response (len=353):
["普通", "中西医结合医院处方笺", "姓名：", "性别：男", "年龄：53岁", "费别：自费", "病人ID：M024274", "处方号：71604", "就诊序号：71603", "体重：80 (kg)", "药物过敏史：无", "住址：河南郑州新密市", "开方日期：2025 03-26 14:42", "就诊科室：内科门诊", "临床诊断：糖尿病", "中医诊断：消渴症", "Rp：", "盐酸二甲双胍片", "0.5g*36", "X 8盒", "用法：每次0.5g TID 口服", "备注：", "医师：张建鹏", "审核：", "核对：", "金额合计：80.00元", "调配：", "发药：", "药房：西药房", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 13:24:32,925 INFO     29 [qwen-vl-parser] page=5 text: 31 lines (bbox 83-113)
2026-08-10 13:24:32,925 INFO     29 [qwen-vl-parser] page=5 text: 31 sections
2026-08-10 13:24:33,008 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=477345, prompt_len=764
2026-08-10 13:24:34,380 INFO     29 [qwen-vl-parser] classify API response (len=56):
```json
{"type": "text", "report_date": "2025-03-2"}
```
2026-08-10 13:24:34,380 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=2025-03-2
2026-08-10 13:24:34,388 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=477345, prompt_len=401
2026-08-10 13:24:35,480 INFO     29 [qwen-vl-parser] text API response (len=144):
["529576", "0061", "2025-03-2", "江顺中西医结合医院", "529576", "男", "自费", "西药费", "80.00", "大额记账：", "大病补充：", "捌拾元整", "原帐户余额：", "现金支付：", "80.00", "80.00"]
2026-08-10 13:24:35,480 INFO     29 [qwen-vl-parser] page=6 text: 16 lines (bbox 114-129)
2026-08-10 13:24:35,481 INFO     29 [qwen-vl-parser] page=6 text: 16 sections
2026-08-10 13:24:35,481 INFO     29 [qwen-vl-parser] parse_pdf done: 130 sections from 6 pages.
2026-08-10 13:24:35,493 INFO     29 Close text detector.
2026-08-10 13:24:35,910 INFO     29 Close text recognizer.
2026-08-10 13:24:36,280 INFO     29 Close recognizer.
2026-08-10 13:24:36,702 INFO     29 Close recognizer.
2026-08-10 13:24:37,157 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 13:24:37,157 INFO     29 [Trace] task=c6f37d04 | doc=Gxdo郑州中心糖尿病.pdf | Parser:MedLink | outputs={"html": "", "json": "130 items", "markdown": "", "text": "", "name": "Gxdo郑州中心糖尿病.pdf", "output_format": "json"}
2026-08-10 13:24:37,157 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 13:24:37,174 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:24:37,174 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 中西医结合医院\n[BBOX-1] 病人门（急）诊病历\n[BBOX-2] 病人ID M024274 姓名\n[BBOX-3] 性别：男 出生时间： 1972年03月01日\n[BBOX-4] 籍贯： 汉族 婚否：已婚 职业：无\n[BBOX-5] 身份证号： 电话号码：\n[BBOX-6] 工作单位： 常住地址：新密市大隗镇\n[BBOX-7] 门诊号： 71603 接诊时间： 2025年3月26日 14时29分\n[BBOX-8] 就诊时间：2025-03-26 14:29:04 体温：36.5 ℃\n[BBOX-9] 主诉：糖尿病20年\n[BBOX-10] 现病史：20年前出现多饮、多尿、多食，曾规律服用二甲双胍缓释片，格列本脲\n[BBOX-11] 片，消渴丸等药，血糖控制不佳，为求进一步治疗前来就诊。\n[BBOX-12] 体格检查：\n[BBOX-13] 西医诊断：1.糖尿病 中医诊断：\n[BBOX-14] 建议： 1、糖尿病饮食；保持心情愉悦；\n[BBOX-15] 2、适量运动；\n[BBOX-16] 3、规律服药；\n[BBOX-17] 4、定期监测血糖；\n[BBOX-18] 5、不适随诊。\n[BBOX-19] 过敏史：无\n[BBOX-20] 家族史：有\n[BBOX-21] 既往史：无\n[BBOX-22] 处理：给予空腹血糖、糖化血红蛋白检测，以了解血糖控制情况\n[BBOX-23] 备注：\n[BBOX-24] 打印时间：2025.3.26 科室：内科门诊 医生：张建鹏\n[BBOX-25] \\begin{tabular}{|l|l|l|l|l|l|}\n[BBOX-26] 报告时间: 2025-03-26\n[BBOX-27] \\hline\n[BBOX-28] 姓名 & 性别: 男 & 年龄: 53 & 送检科室: 门诊 & 标本状态: 正常 & 标本类型: 静脉全血 \\\\\n[BBOX-29] \\hline\n[BBOX-30] \\multicolumn{5}{|l|}{} & 送检日期: 2025-03-26 \\\\\n[BBOX-31] \\hline\n[BBOX-32] 项目名称 & \\multicolumn{3}{c|}{结果} & \\multicolumn{2}{c|}{参考范围} \\\\\n[BBOX-33] \\hline\n[BBOX-34] 糖化血红蛋白测定 (HbA1c) & \\multicolumn{3}{c|}{10.7\\%} & \\multicolumn{2}{c|}{4-6\\%} \\\\\n[BBOX-35] \\hline\n[BBOX-36] \\end{tabular}\n[BBOX-37] 送检医师: 马中杰 检验师: 裴巧玲 审核者: 裴巧玲 报告时间: 2025-03-26\n[BBOX-38] 此结果仅对该标本负责\n[BBOX-39] 普通\n[BBOX-40] .中西医结合医院处方笺\n[BBOX-41] 姓名：\n[BBOX-42] 性别：男\n[BBOX-43] 年龄：53岁\n[BBOX-44] 费别：自费\n[BBOX-45] 病人ID：M024274\n[BBOX-46] 处方号：71603\n[BBOX-47] 就诊序号：51869\n[BBOX-48] 体重：/（kg）\n[BBOX-49] 药物过敏史：无\n[BBOX-50] 住址：新密市\n[BBOX-51] 开方日期：2024-12-30\n[BBOX-52] 08：16\n[BBOX-53] 就诊科室：内科门诊\n[BBOX-54] 临床诊断：糖\n[BBOX-55] Rp:\n[BBOX-56] 盐酸二甲双胍片\n[BBOX-57] 0.5g*60 X 6盒\n[BBOX-58] 用法：每次0.5g 一日三次 口服\n[BBOX-59] 备注：\n[BBOX-60] 医师：张建鹏\n[BBOX-61] 审核：\n[BBOX-62] 核对：\n[BBOX-63] 金额合计：60.00元\n[BBOX-64] 调配：\n[BBOX-65] 发药：\n[BBOX-66] 药房：西药费\n[BBOX-67] CS 扫描全能王\n[BBOX-68] 3亿人都在用的扫描App\n[BBOX-69] 顺中西医结合医院\n[BBOX-70] 527647\n[BBOX-71] 自费\n[BBOX-72] 西药费\n[BBOX-73] 60.00\n[BBOX-74] 大额记账:\n[BBOX-75] 大病补充:\n[BBOX-76] 原账户余额:\n[BBOX-77] 已审核\n[BBOX-78] 现金支付:\n[BBOX-79] 陆拾元整\n[BBOX-80] 60.00\n[BBOX-81] 527647\n[BBOX-82] 0061\n[BBOX-83] 普通\n[BBOX-84] 中西医结合医院处方笺\n[BBOX-85] 姓名：\n[BBOX-86] 性别：男\n[BBOX-87] 年龄：53岁\n[BBOX-88] 费别：自费\n[BBOX-89] 病人ID：M024274\n[BBOX-90] 处方号：71604\n[BBOX-91] 就诊序号：71603\n[BBOX-92] 体重：80 (kg)\n[BBOX-93] 药物过敏史：无\n[BBOX-94] 住址：河南郑州新密市\n[BBOX-95] 开方日期：2025 03-26 14:42\n[BBOX-96] 就诊科室：内科门诊\n[BBOX-97] 临床诊断：糖尿病\n[BBOX-98] 中医诊断：消渴症\n[BBOX-99] Rp：\n[BBOX-100] 盐酸二甲双胍片\n[BBOX-101] 0.5g*36\n[BBOX-102] X 8盒\n[BBOX-103] 用法：每次0.5g TID 口服\n[BBOX-104] 备注：\n[BBOX-105] 医师：张建鹏\n[BBOX-106] 审核：\n[BBOX-107] 核对：\n[BBOX-108] 金额合计：80.00元\n[BBOX-109] 调配：\n[BBOX-110] 发药：\n[BBOX-111] 药房：西药房\n[BBOX-112] CS 扫描全能王\n[BBOX-113] 3亿人都在用的扫描App\n[BBOX-114] 529576\n[BBOX-115] 0061\n[BBOX-116] 2025-03-2\n[BBOX-117] 江顺中西医结合医院\n[BBOX-118] 529576\n[BBOX-119] 男\n[BBOX-120] 自费\n[BBOX-121] 西药费\n[BBOX-122] 80.00\n[BBOX-123] 大额记账：\n[BBOX-124] 大病补充：\n[BBOX-125] 捌拾元整\n[BBOX-126] 原帐户余额：\n[BBOX-127] 现金支付：\n[BBOX-128] 80.00\n[BBOX-129] 80.00"
  }
]
2026-08-10 13:24:42,510 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:24:42,533 INFO     29 [SmartSplitter] SmartSplitter done: 6 chunks from 6 LLM segments (all bbox_id). Types: {'OutpatientRecord': 1, 'LabReport': 1, 'PrescriptionRecord': 2, 'MedicationRecord': 2}
2026-08-10 13:24:42,543 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 13:24:42,543 INFO     29 [Trace] task=c6f37d04 | doc=Gxdo郑州中心糖尿病.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "130 items", "markdown": "", "text": "", "name": "Gxdo郑州中心糖尿病.pdf", "output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 1, 'LabReport': 1, 'PrescriptionRecord': 2, 'MedicationRecord': 2}"}
2026-08-10 13:24:42,543 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 13:24:42,543 INFO     29 [ChunkRouter] Routed 6 chunks into 4 groups: {'chunks_Clinical': 1, 'chunks_LabExam': 1, 'chunks_Prescription': 2, 'chunks_Medication': 2}
2026-08-10 13:24:42,551 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 13:24:42,552 INFO     29 [Trace] task=c6f37d04 | doc=Gxdo郑州中心糖尿病.pdf | ChunkRouter:Router | outputs={"html": "", "json": "130 items", "markdown": "", "text": "", "name": "Gxdo郑州中心糖尿病.pdf", "output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 1, 'LabReport': 1, 'PrescriptionRecord': 2, 'MedicationRecord': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 1, \"chunks_Prescription\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:24:42,552 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 13:24:42,556 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:24:42,557 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:24:42,557 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[1]
2026-08-10 13:24:42,557 INFO     29 [qwen-vl-table] positions ： [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:24:42,715 INFO     29 [qwen-vl-table] page=1, rect=595x842, img=(1653x2339)
2026-08-10 13:24:42,716 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:24:42,716 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 25, \"bbox_end\": 38, \"encounter_dates\": [\"2025-03-26\"], \"department\": \"门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{|l|l|l|l|l|l|}\n报告时间: 2025-03-26\n\\hline\n姓名 & 性别: 男 & 年龄: 53 & 送检科室: 门诊 & 标本状态: 正常 & 标本类型: 静脉全血 \\\\\n\\hline\n\\multicolumn{5}{|l|}{} & 送检日期: 2025-03-26 \\\\\n\\hline\n项目名称 & \\multicolumn{3}{c|}{结果} & \\multicolumn{2}{c|}{参考范围} \\\\\n\\hline\n糖化血红蛋白测定 (HbA1c) & \\multicolumn{3}{c|}{10.7\\%} & \\multicolumn{2}{c|}{4-6\\%} \\\\\n\\hline\n\\end{tabular}\n送检医师: 马中杰 检验师: 裴巧玲 审核者: 裴巧玲 报告时间: 2025-03-26\n此结果仅对该标本负责",
    "role": "user"
  }
]
2026-08-10 13:24:43,943 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:24:43,944 INFO     29 [qwen-vl-table] page=1 LLM output (len=216):
{
  "report_date": "2025-03-26",
  "items": [
    {
      "name": "糖化血红蛋白测定",
      "item_code": "HbA1c",
      "value": "10.7%",
      "unit": "%",
      "reference_range": "4-6%",
      "abnormal": true
    }
  ]
}
2026-08-10 13:24:43,944 INFO     29 [qwen-vl-table] coord grouping: {1: 1}
2026-08-10 13:24:43,945 INFO     29 [qwen-vl-table] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=469379, prompt_len=515
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
糖化血红蛋白测定

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
2026-08-10 13:24:45,490 INFO     29 [qwen-vl-table] coord API raw response (len=67):
```json
[
	{"text": "糖化血红蛋白测定", "bbox": [133, 563, 428, 593]}
]
```
2026-08-10 13:24:45,490 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=1.5s
2026-08-10 13:24:45,490 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白测定, bbox=[133, 563, 428, 593]
2026-08-10 13:24:45,490 INFO     29 [qwen-vl-table] page=1 coord: matched 1/1, time=1.5s
2026-08-10 13:24:45,490 INFO     29 [qwen-vl-table] new_positions (1):
[[2, 79.13499999999999, 254.66, 474.046, 499.306]]
2026-08-10 13:24:45,491 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=2.9s
2026-08-10 13:24:45,502 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 13:24:45,502 INFO     29 [Trace] task=c6f37d04 | doc=Gxdo郑州中心糖尿病.pdf | Extractor:LabExam | outputs={"chunks": "1 items, types={'LabReport': 1}", "html": "", "json": "130 items", "markdown": "", "text": "", "name": "Gxdo郑州中心糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 1, \"chunks_Prescription\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:24:45,502 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 13:24:45,508 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:24:45,508 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:24:46,366 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:24:46,374 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 13:24:46,375 INFO     29 [Trace] task=c6f37d04 | doc=Gxdo郑州中心糖尿病.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "130 items", "markdown": "", "text": "", "name": "Gxdo郑州中心糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 1, \"chunks_Prescription\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:24:46,375 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 13:24:46,381 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:24:46,382 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:24:46,382 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 13:24:46,382 INFO     29 [qwen-vl-text] positions(25): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:24:46,382 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [25]
2026-08-10 13:24:46,546 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:24:46,547 INFO     29 [qwen-vl-text] LLM extraction start, text_len=407
2026-08-10 13:24:46,547 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:24:46,547 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 24, \"encounter_dates\": [\"2025-03-26\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "中西医结合医院\n病人门（急）诊病历\n病人ID M024274 姓名\n性别：男 出生时间： 1972年03月01日\n籍贯： 汉族 婚否：已婚 职业：无\n身份证号： 电话号码：\n工作单位： 常住地址：新密市大隗镇\n门诊号： 71603 接诊时间： 2025年3月26日 14时29分\n就诊时间：2025-03-26 14:29:04 体温：36.5 ℃\n主诉：糖尿病20年\n现病史：20年前出现多饮、多尿、多食，曾规律服用二甲双胍缓释片，格列本脲\n片，消渴丸等药，血糖控制不佳，为求进一步治疗前来就诊。\n体格检查：\n西医诊断：1.糖尿病 中医诊断：\n建议： 1、糖尿病饮食；保持心情愉悦；\n2、适量运动；\n3、规律服药；\n4、定期监测血糖；\n5、不适随诊。\n过敏史：无\n家族史：有\n既往史：无\n处理：给予空腹血糖、糖化血红蛋白检测，以了解血糖控制情况\n备注：\n打印时间：2025.3.26 科室：内科门诊 医生：张建鹏",
    "role": "user"
  }
]
2026-08-10 13:24:48,667 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:24:48,667 INFO     29 [qwen-vl-text] LLM output (len=408):
{
  "encounter_date": "2025-03-26",
  "chief_complaint": "糖尿病20年",
  "present_illness": "20年前出现多饮、多尿、多食，曾规律服用二甲双胍缓释片，格列本脲片，消渴丸等药，血糖控制不佳，为求进一步治疗前来就诊。",
  "past_history": "无",
  "diagnosis": "西医：1.糖尿病",
  "treatment_plan": {
    "lifestyle_advice": [
      "糖尿病饮食",
      "保持心情愉悦",
      "适量运动",
      "规律服药",
      "定期监测血糖",
      "不适随诊"
    ],
    "examinations": [
      "空腹血糖",
      "糖化血红蛋白检测"
    ]
  }
}
2026-08-10 13:24:48,667 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-03-26]
2026-08-10 13:24:48,669 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=739799, prompt_len=1095
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["中西医结合医院", "病人门（急）诊病历", "病人ID M024274 姓名", "性别：男 出生时间： 1972年03月01日", "籍贯： 汉族 婚否：已婚 职业：无", "身份证号： 电话号码：", "工作单位： 常住地址：新密市大隗镇", "门诊号： 71603 接诊时间： 2025年3月26日 14时29分", "就诊时间：2025-03-26 14:29:04 体温：36.5 ℃", "主诉：糖尿病20年", "现病史：20年前出现多饮、多尿、多食，曾规律服用二甲双胍缓释片，格列本脲", "片，消渴丸等药，血糖控制不佳，为求进一步治疗前来就诊。", "体格检查：", "西医诊断：1.糖尿病 中医诊断：", "建议： 1、糖尿病饮食；保持心情愉悦；", "2、适量运动；", "3、规律服药；", "4、定期监测血糖；", "5、不适随诊。", "过敏史：无", "家族史：有", "既往史：无", "处理：给予空腹血糖、糖化血红蛋白检测，以了解血糖控制情况", "备注：", "打印时间：2025.3.26 科室：内科门诊 医生：张建鹏"]

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
2026-08-10 13:24:57,240 INFO     29 [qwen-vl-text] coord API raw response (len=1490):
[
	{"text": "中西医结合医院", "bbox": [458, 29, 706, 57]},
	{"text": "病人门（急）诊病历", "bbox": [290, 74, 708, 108]},
	{"text": "病人ID M024274 姓名", "bbox": [86, 123, 319, 139]},
	{"text": "性别：男 出生时间： 1972年03月01日", "bbox": [456, 123, 880, 140]},
	{"text": "籍贯： 汉族 婚否：已婚 职业：无", "bbox": [86, 151, 754, 169]},
	{"text": "身份证号： 电话号码：", "bbox": [86, 181, 608, 198]},
	{"text": "工作单位： 常住地址：新密市大隗镇", "bbox": [86, 205, 764, 223]},
	{"text": "门诊号： 71603 接诊时间： 2025年3月26日 14时29分", "bbox": [86, 232, 760, 250]},
	{"text": "就诊时间：2025-03-26 14:29:04 体温：36.5 ℃", "bbox": [86, 259, 718, 277]},
	{"text": "主诉：糖尿病20年", "bbox": [86, 292, 283, 310]},
	{"text": "现病史：20年前出现多饮、多尿、多食，曾规律服用二甲双胍缓释片，格列本脲", "bbox": [86, 352, 908, 370]},
	{"text": "片，消渴丸等药，血糖控制不佳，为求进一步治疗前来就诊。", "bbox": [86, 372, 696, 390]},
	{"text": "体格检查：", "bbox": [86, 419, 186, 437]},
	{"text": "西医诊断：1.糖尿病 中医诊断：", "bbox": [86, 465, 509, 483]},
	{"text": "建议： 1、糖尿病饮食；保持心情愉悦；", "bbox": [86, 502, 497, 519]},
	{"text": "2、适量运动；", "bbox": [176, 520, 312, 537]},
	{"text": "3、规律服药；", "bbox": [176, 538, 312, 555]},
	{"text": "4、定期监测血糖；", "bbox": [176, 555, 359, 573]},
	{"text": "5、不适随诊。", "bbox": [176, 573, 315, 590]},
	{"text": "过敏史：无", "bbox": [86, 629, 202, 647]},
	{"text": "家族史：有", "bbox": [86, 666, 200, 684]},
	{"text": "既往史：无", "bbox": [86, 712, 200, 730]},
	{"text": "处理：给予空腹血糖、糖化血红蛋白检测，以了解血糖控制情况", "bbox": [95, 765, 740, 783]},
	{"text": "备注：", "bbox": [95, 805, 150, 823]},
	{"text": "打印时间：2025.3.26 科室：内科门诊 医生：张建鹏", "bbox": [114, 846, 758, 864]}
]
2026-08-10 13:24:57,240 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=8.6s
2026-08-10 13:24:57,241 INFO     29 [qwen-vl-text] coord item[0]: text=中西医结合医院, bbox=[458, 29, 706, 57]
2026-08-10 13:24:57,241 INFO     29 [qwen-vl-text] coord item[1]: text=病人门（急）诊病历, bbox=[290, 74, 708, 108]
2026-08-10 13:24:57,241 INFO     29 [qwen-vl-text] coord item[2]: text=病人ID M024274 姓名, bbox=[86, 123, 319, 139]
2026-08-10 13:24:57,241 INFO     29 [qwen-vl-text] coord item[3]: text=性别：男 出生时间： 1972年03月01日, bbox=[456, 123, 880, 140]
2026-08-10 13:24:57,241 INFO     29 [qwen-vl-text] coord item[4]: text=籍贯： 汉族 婚否：已婚 职业：无, bbox=[86, 151, 754, 169]
2026-08-10 13:24:57,241 INFO     29 [qwen-vl-text] coord item[5]: text=身份证号： 电话号码：, bbox=[86, 181, 608, 198]
2026-08-10 13:24:57,241 INFO     29 [qwen-vl-text] coord item[6]: text=工作单位： 常住地址：新密市大隗镇, bbox=[86, 205, 764, 223]
2026-08-10 13:24:57,241 INFO     29 [qwen-vl-text] coord item[7]: text=门诊号： 71603 接诊时间： 2025年3月26日 14时29分, bbox=[86, 232, 760, 250]
2026-08-10 13:24:57,241 INFO     29 [qwen-vl-text] coord item[8]: text=就诊时间：2025-03-26 14:29:04 体温：36.5 ℃, bbox=[86, 259, 718, 277]
2026-08-10 13:24:57,241 INFO     29 [qwen-vl-text] coord item[9]: text=主诉：糖尿病20年, bbox=[86, 292, 283, 310]
2026-08-10 13:24:57,241 INFO     29 [qwen-vl-text] coord item[10]: text=现病史：20年前出现多饮、多尿、多食，曾规律服用二甲双胍缓释片，格列本脲, bbox=[86, 352, 908, 370]
2026-08-10 13:24:57,241 INFO     29 [qwen-vl-text] coord item[11]: text=片，消渴丸等药，血糖控制不佳，为求进一步治疗前来就诊。, bbox=[86, 372, 696, 390]
2026-08-10 13:24:57,242 INFO     29 [qwen-vl-text] coord item[12]: text=体格检查：, bbox=[86, 419, 186, 437]
2026-08-10 13:24:57,242 INFO     29 [qwen-vl-text] coord item[13]: text=西医诊断：1.糖尿病 中医诊断：, bbox=[86, 465, 509, 483]
2026-08-10 13:24:57,242 INFO     29 [qwen-vl-text] coord item[14]: text=建议： 1、糖尿病饮食；保持心情愉悦；, bbox=[86, 502, 497, 519]
2026-08-10 13:24:57,242 INFO     29 [qwen-vl-text] coord item[15]: text=2、适量运动；, bbox=[176, 520, 312, 537]
2026-08-10 13:24:57,242 INFO     29 [qwen-vl-text] coord item[16]: text=3、规律服药；, bbox=[176, 538, 312, 555]
2026-08-10 13:24:57,242 INFO     29 [qwen-vl-text] coord item[17]: text=4、定期监测血糖；, bbox=[176, 555, 359, 573]
2026-08-10 13:24:57,242 INFO     29 [qwen-vl-text] coord item[18]: text=5、不适随诊。, bbox=[176, 573, 315, 590]
2026-08-10 13:24:57,242 INFO     29 [qwen-vl-text] coord item[19]: text=过敏史：无, bbox=[86, 629, 202, 647]
2026-08-10 13:24:57,242 INFO     29 [qwen-vl-text] coord item[20]: text=家族史：有, bbox=[86, 666, 200, 684]
2026-08-10 13:24:57,242 INFO     29 [qwen-vl-text] coord item[21]: text=既往史：无, bbox=[86, 712, 200, 730]
2026-08-10 13:24:57,242 INFO     29 [qwen-vl-text] coord item[22]: text=处理：给予空腹血糖、糖化血红蛋白检测，以了解血糖控制情况, bbox=[95, 765, 740, 783]
2026-08-10 13:24:57,242 INFO     29 [qwen-vl-text] coord item[23]: text=备注：, bbox=[95, 805, 150, 823]
2026-08-10 13:24:57,242 INFO     29 [qwen-vl-text] coord item[24]: text=打印时间：2025.3.26 科室：内科门诊 医生：张建鹏, bbox=[114, 846, 758, 864]
2026-08-10 13:24:57,243 INFO     29 [qwen-vl-text] page=0 — 25/25 coords, api_time=8.6s
2026-08-10 13:24:57,243 INFO     29 [qwen-vl-text] new_positions (25):
[[0, 272.51, 420.07, 24.418, 47.994], [0, 172.54999999999998, 421.26, 62.308, 90.93599999999999], [0, 51.169999999999995, 189.80499999999998, 103.566, 117.038], [0, 271.32, 523.6, 103.566, 117.88], [0, 51.169999999999995, 448.63, 127.142, 142.298], [0, 51.169999999999995, 361.76, 152.402, 166.716], [0, 51.169999999999995, 454.58, 172.60999999999999, 187.766], [0, 51.169999999999995, 452.2, 195.344, 210.5], [0, 51.169999999999995, 427.21, 218.078, 233.23399999999998], [0, 51.169999999999995, 168.385, 245.864, 261.02], [0, 51.169999999999995, 540.26, 296.384, 311.53999999999996], [0, 51.169999999999995, 414.12, 313.224, 328.38], [0, 51.169999999999995, 110.67, 352.798, 367.954], [0, 51.169999999999995, 302.85499999999996, 391.53, 406.686], [0, 51.169999999999995, 295.715, 422.68399999999997, 436.998], [0, 104.72, 185.64, 437.84, 452.154], [0, 104.72, 185.64, 452.996, 467.31], [0, 104.72, 213.605, 467.31, 482.466], [0, 104.72, 187.42499999999998, 482.466, 496.78], [0, 51.169999999999995, 120.19, 529.6179999999999, 544.774], [0, 51.169999999999995, 119.0, 560.7719999999999, 575.928], [0, 51.169999999999995, 119.0, 599.504, 614.66], [0, 56.525, 440.29999999999995, 644.13, 659.286], [0, 56.525, 89.25, 677.81, 692.966], [0, 67.83, 451.01, 712.332, 727.4879999999999]]
2026-08-10 13:24:57,243 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=10.9s
2026-08-10 13:24:57,261 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 13:24:57,261 INFO     29 [Trace] task=c6f37d04 | doc=Gxdo郑州中心糖尿病.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "130 items", "markdown": "", "text": "", "name": "Gxdo郑州中心糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 1, \"chunks_Prescription\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:24:57,261 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 13:24:57,262 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:24:57.261+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 48, "failed": 0, "current": {"c6f37d0494be11f1bd9827cf206dfa2d": {"id": "c6f37d0494be11f1bd9827cf206dfa2d", "doc_id": "c6bfa85894be11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Gxdo\u90d1\u5dde\u4e2d\u5fc3\u7cd6\u5c3f\u75c5.pdf", "type": "pdf", "location": "Gxdo\u90d1\u5dde\u4e2d\u5fc3\u7cd6\u5c3f\u75c5.pdf", "size": 1474288, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368252776, "task_type": "dataflow", "root_trace_id": "0739225e0c644d63a7cc49e0ecacc097", "root_traceparent": "00-0739225e0c644d63a7cc49e0ecacc097-05128704d7f5e09a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:24:57,268 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:24:57,268 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:24:57,269 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 13:24:57,269 INFO     29 [qwen-vl-text] positions(15): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:24:57,269 INFO     29 [qwen-vl-text] page grouping: [3, 4], lines per page: [14, 1]
2026-08-10 13:24:57,388 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:24:57,544 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:24:57,545 INFO     29 [qwen-vl-text] LLM extraction start, text_len=83
2026-08-10 13:24:57,545 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:24:57,545 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 69, \"bbox_end\": 83, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "顺中西医结合医院\n527647\n自费\n西药费\n60.00\n大额记账:\n大病补充:\n原账户余额:\n已审核\n现金支付:\n陆拾元整\n60.00\n527647\n0061\n普通",
    "role": "user"
  }
]
2026-08-10 13:24:58,748 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:24:58,748 INFO     29 [qwen-vl-text] LLM output (len=129):
{
  "encounter_date": null,
  "pharmacy": "顺中西医结合医院",
  "medications": [],
  "payment_total": 60.00,
  "payment_method": "现金支付"
}
2026-08-10 13:24:58,751 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=743266, prompt_len=735
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共14行）
["顺中西医结合医院", "527647", "自费", "西药费", "60.00", "大额记账:", "大病补充:", "原账户余额:", "已审核", "现金支付:", "陆拾元整", "60.00", "527647", "0061"]

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
2026-08-10 13:25:04,594 INFO     29 [qwen-vl-text] coord API raw response (len=699):
[
	{"text": "顺中西医结合医院", "bbox": [315, 141, 597, 171]},
	{"text": "527647", "bbox": [309, 181, 419, 203]},
	{"text": "自费", "bbox": [528, 252, 589, 277]},
	{"text": "西药费", "bbox": [231, 380, 337, 406]},
	{"text": "60.00", "bbox": [629, 388, 711, 409]},
	{"text": "大额记账:", "bbox": [188, 638, 346, 669]},
	{"text": "大病补充:", "bbox": [185, 683, 346, 714]},
	{"text": "原账户余额:", "bbox": [523, 601, 693, 627]},
	{"text": "已审核", "bbox": [540, 631, 773, 710]},
	{"text": "现金支付:", "bbox": [548, 687, 695, 714]},
	{"text": "陆拾元整", "bbox": [367, 731, 509, 761]},
	{"text": "60.00", "bbox": [762, 724, 865, 749]},
	{"text": "527647", "bbox": [168, 877, 298, 905]},
	{"text": "0061", "bbox": [557, 880, 629, 908]}
]
2026-08-10 13:25:04,594 INFO     29 [qwen-vl-text] coord API: raw_items=14, valid_items=14, elapsed=5.8s
2026-08-10 13:25:04,594 INFO     29 [qwen-vl-text] coord item[0]: text=顺中西医结合医院, bbox=[315, 141, 597, 171]
2026-08-10 13:25:04,594 INFO     29 [qwen-vl-text] coord item[1]: text=527647, bbox=[309, 181, 419, 203]
2026-08-10 13:25:04,594 INFO     29 [qwen-vl-text] coord item[2]: text=自费, bbox=[528, 252, 589, 277]
2026-08-10 13:25:04,594 INFO     29 [qwen-vl-text] coord item[3]: text=西药费, bbox=[231, 380, 337, 406]
2026-08-10 13:25:04,594 INFO     29 [qwen-vl-text] coord item[4]: text=60.00, bbox=[629, 388, 711, 409]
2026-08-10 13:25:04,594 INFO     29 [qwen-vl-text] coord item[5]: text=大额记账:, bbox=[188, 638, 346, 669]
2026-08-10 13:25:04,594 INFO     29 [qwen-vl-text] coord item[6]: text=大病补充:, bbox=[185, 683, 346, 714]
2026-08-10 13:25:04,594 INFO     29 [qwen-vl-text] coord item[7]: text=原账户余额:, bbox=[523, 601, 693, 627]
2026-08-10 13:25:04,594 INFO     29 [qwen-vl-text] coord item[8]: text=已审核, bbox=[540, 631, 773, 710]
2026-08-10 13:25:04,594 INFO     29 [qwen-vl-text] coord item[9]: text=现金支付:, bbox=[548, 687, 695, 714]
2026-08-10 13:25:04,594 INFO     29 [qwen-vl-text] coord item[10]: text=陆拾元整, bbox=[367, 731, 509, 761]
2026-08-10 13:25:04,594 INFO     29 [qwen-vl-text] coord item[11]: text=60.00, bbox=[762, 724, 865, 749]
2026-08-10 13:25:04,594 INFO     29 [qwen-vl-text] coord item[12]: text=527647, bbox=[168, 877, 298, 905]
2026-08-10 13:25:04,594 INFO     29 [qwen-vl-text] coord item[13]: text=0061, bbox=[557, 880, 629, 908]
2026-08-10 13:25:04,594 INFO     29 [qwen-vl-text] page=3 — 14/14 coords, api_time=5.8s
2026-08-10 13:25:04,595 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=459133, prompt_len=617
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["普通"]

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
2026-08-10 13:25:06,062 INFO     29 [qwen-vl-text] coord API raw response (len=59):
```json
[
	{"text": "普通", "bbox": [833, 37, 879, 55]}
]
```
2026-08-10 13:25:06,062 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=1.5s
2026-08-10 13:25:06,063 INFO     29 [qwen-vl-text] coord item[0]: text=普通, bbox=[833, 37, 879, 55]
2026-08-10 13:25:06,063 INFO     29 [qwen-vl-text] page=4 — 1/1 coords, api_time=1.5s
2026-08-10 13:25:06,063 INFO     29 [qwen-vl-text] new_positions (15):
[[3, 187.42499999999998, 355.215, 118.722, 143.982], [3, 183.855, 249.30499999999998, 152.402, 170.926], [3, 314.15999999999997, 350.455, 212.184, 233.23399999999998], [3, 137.445, 200.515, 319.96, 341.852], [3, 374.255, 423.04499999999996, 326.69599999999997, 344.378], [3, 111.86, 205.87, 537.196, 563.298], [3, 110.07499999999999, 205.87, 575.086, 601.188], [3, 311.185, 412.335, 506.042, 527.934], [3, 321.3, 459.935, 531.302, 597.8199999999999], [3, 326.06, 413.525, 578.454, 601.188], [3, 218.36499999999998, 302.85499999999996, 615.502, 640.762], [3, 453.39, 514.675, 609.608, 630.658], [3, 99.96, 177.31, 738.434, 762.01], [3, 331.41499999999996, 374.255, 740.9599999999999, 764.536], [4, 495.635, 523.005, 31.154, 46.309999999999995]]
2026-08-10 13:25:06,063 INFO     29 [qwen-vl-text] ═══ DONE ═══ 15 positions, pages=2, time=8.8s
2026-08-10 13:25:06,063 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:25:06,064 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:25:06,064 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 13:25:06,064 INFO     29 [qwen-vl-text] positions(16): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:25:06,064 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [16]
2026-08-10 13:25:06,222 INFO     29 [qwen-vl-text] page=5, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:25:06,223 INFO     29 [qwen-vl-text] LLM extraction start, text_len=95
2026-08-10 13:25:06,223 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:25:06,223 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 114, \"bbox_end\": 129, \"encounter_dates\": [\"2025-03-26\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "529576\n0061\n2025-03-2\n江顺中西医结合医院\n529576\n男\n自费\n西药费\n80.00\n大额记账：\n大病补充：\n捌拾元整\n原帐户余额：\n现金支付：\n80.00\n80.00",
    "role": "user"
  }
]
2026-08-10 13:25:07,654 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:25:07,654 INFO     29 [qwen-vl-text] LLM output (len=138):
{
  "encounter_date": "2025-03-26",
  "pharmacy": "江顺中西医结合医院",
  "medications": [],
  "payment_total": 80.00,
  "payment_method": "现金支付"
}
2026-08-10 13:25:07,654 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-03-26]
2026-08-10 13:25:07,656 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=488242, prompt_len=756
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["529576", "0061", "2025-03-2", "江顺中西医结合医院", "529576", "男", "自费", "西药费", "80.00", "大额记账：", "大病补充：", "捌拾元整", "原帐户余额：", "现金支付：", "80.00", "80.00"]

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
2026-08-10 13:25:12,561 INFO     29 [qwen-vl-text] coord API raw response (len=794):
[
	{"text": "529576", "bbox": [242, 30, 390, 56]},
	{"text": "0061", "bbox": [592, 28, 687, 54]},
	{"text": "2025-03-2", "bbox": [816, 30, 999, 54]},
	{"text": "江顺中西医结合医院", "bbox": [176, 181, 643, 212]},
	{"text": "529576", "bbox": [299, 230, 420, 253]},
	{"text": "男", "bbox": [481, 270, 511, 294]},
	{"text": "自费", "bbox": [594, 271, 651, 293]},
	{"text": "西药费", "bbox": [223, 362, 334, 389]},
	{"text": "80.00", "bbox": [791, 360, 890, 382]},
	{"text": "大额记账：", "bbox": [161, 663, 327, 688]},
	{"text": "大病补充：", "bbox": [165, 698, 332, 725]},
	{"text": "捌拾元整", "bbox": [339, 752, 509, 784]},
	{"text": "原帐户余额：", "bbox": [589, 620, 791, 649]},
	{"text": "现金支付：", "bbox": [630, 700, 797, 728]},
	{"text": "80.00", "bbox": [848, 754, 956, 780]},
	{"text": "80.00", "bbox": [0, 857, 100, 887]}
]
2026-08-10 13:25:12,561 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=4.9s
2026-08-10 13:25:12,561 INFO     29 [qwen-vl-text] coord item[0]: text=529576, bbox=[242, 30, 390, 56]
2026-08-10 13:25:12,561 INFO     29 [qwen-vl-text] coord item[1]: text=0061, bbox=[592, 28, 687, 54]
2026-08-10 13:25:12,561 INFO     29 [qwen-vl-text] coord item[2]: text=2025-03-2, bbox=[816, 30, 999, 54]
2026-08-10 13:25:12,561 INFO     29 [qwen-vl-text] coord item[3]: text=江顺中西医结合医院, bbox=[176, 181, 643, 212]
2026-08-10 13:25:12,561 INFO     29 [qwen-vl-text] coord item[4]: text=529576, bbox=[299, 230, 420, 253]
2026-08-10 13:25:12,561 INFO     29 [qwen-vl-text] coord item[5]: text=男, bbox=[481, 270, 511, 294]
2026-08-10 13:25:12,561 INFO     29 [qwen-vl-text] coord item[6]: text=自费, bbox=[594, 271, 651, 293]
2026-08-10 13:25:12,561 INFO     29 [qwen-vl-text] coord item[7]: text=西药费, bbox=[223, 362, 334, 389]
2026-08-10 13:25:12,561 INFO     29 [qwen-vl-text] coord item[8]: text=80.00, bbox=[791, 360, 890, 382]
2026-08-10 13:25:12,561 INFO     29 [qwen-vl-text] coord item[9]: text=大额记账：, bbox=[161, 663, 327, 688]
2026-08-10 13:25:12,561 INFO     29 [qwen-vl-text] coord item[10]: text=大病补充：, bbox=[165, 698, 332, 725]
2026-08-10 13:25:12,561 INFO     29 [qwen-vl-text] coord item[11]: text=捌拾元整, bbox=[339, 752, 509, 784]
2026-08-10 13:25:12,561 INFO     29 [qwen-vl-text] coord item[12]: text=原帐户余额：, bbox=[589, 620, 791, 649]
2026-08-10 13:25:12,561 INFO     29 [qwen-vl-text] coord item[13]: text=现金支付：, bbox=[630, 700, 797, 728]
2026-08-10 13:25:12,561 INFO     29 [qwen-vl-text] coord item[14]: text=80.00, bbox=[848, 754, 956, 780]
2026-08-10 13:25:12,561 INFO     29 [qwen-vl-text] coord item[15]: text=80.00, bbox=[0, 857, 100, 887]
2026-08-10 13:25:12,561 INFO     29 [qwen-vl-text] page=5 — 16/16 coords, api_time=4.9s
2026-08-10 13:25:12,561 INFO     29 [qwen-vl-text] new_positions (16):
[[5, 143.98999999999998, 232.04999999999998, 25.259999999999998, 47.152], [5, 352.24, 408.765, 23.576, 45.467999999999996], [5, 485.52, 594.405, 25.259999999999998, 45.467999999999996], [5, 104.72, 382.585, 152.402, 178.504], [5, 177.905, 249.89999999999998, 193.66, 213.02599999999998], [5, 286.195, 304.04499999999996, 227.34, 247.548], [5, 353.43, 387.34499999999997, 228.182, 246.706], [5, 132.685, 198.73, 304.804, 327.538], [5, 470.645, 529.55, 303.12, 321.644], [5, 95.795, 194.565, 558.246, 579.2959999999999], [5, 98.175, 197.54, 587.716, 610.4499999999999], [5, 201.70499999999998, 302.85499999999996, 633.184, 660.1279999999999], [5, 350.455, 470.645, 522.04, 546.458], [5, 374.84999999999997, 474.215, 589.4, 612.976], [5, 504.56, 568.8199999999999, 634.8679999999999, 656.76], [5, 0.0, 59.5, 721.5939999999999, 746.8539999999999]]
2026-08-10 13:25:12,561 INFO     29 [qwen-vl-text] ═══ DONE ═══ 16 positions, pages=1, time=6.5s
2026-08-10 13:25:12,572 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 13:25:12,572 INFO     29 [Trace] task=c6f37d04 | doc=Gxdo郑州中心糖尿病.pdf | Extractor:Medication | outputs={"chunks": "2 items, types={'MedicationRecord': 2}", "html": "", "json": "130 items", "markdown": "", "text": "", "name": "Gxdo郑州中心糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 1, \"chunks_Prescription\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:25:12,572 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 13:25:12,577 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:25:12,578 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:25:12,578 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 13:25:12,578 INFO     29 [qwen-vl-text] positions(28): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:25:12,578 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [28]
2026-08-10 13:25:12,703 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:25:12,704 INFO     29 [qwen-vl-text] LLM extraction start, text_len=222
2026-08-10 13:25:12,704 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:25:12,704 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 39, \"bbox_end\": 66, \"encounter_dates\": [\"2024-12-30\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "普通\n.中西医结合医院处方笺\n姓名：\n性别：男\n年龄：53岁\n费别：自费\n病人ID：M024274\n处方号：71603\n就诊序号：51869\n体重：/（kg）\n药物过敏史：无\n住址：新密市\n开方日期：2024-12-30\n08：16\n就诊科室：内科门诊\n临床诊断：糖\nRp:\n盐酸二甲双胍片\n0.5g*60 X 6盒\n用法：每次0.5g 一日三次 口服\n备注：\n医师：张建鹏\n审核：\n核对：\n金额合计：60.00元\n调配：\n发药：\n药房：西药费",
    "role": "user"
  }
]
2026-08-10 13:25:14,779 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:25:14,779 INFO     29 [qwen-vl-text] LLM output (len=407):
{
  "encounter_date": "2024-12-30",
  "prescription_type": "门诊处方",
  "prescriber": "张建鹏",
  "department": "内科门诊",
  "diagnosis": "糖",
  "items": [
    {
      "drug_generic_name": "盐酸二甲双胍片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "0.5g",
      "frequency": "一日三次",
      "route": "口服",
      "duration_days": null,
      "quantity": "6盒",
      "notes": null
    }
  ]
}
2026-08-10 13:25:14,779 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-12-30]
2026-08-10 13:25:14,780 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=433301, prompt_len=919
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["普通", ".中西医结合医院处方笺", "姓名：", "性别：男", "年龄：53岁", "费别：自费", "病人ID：M024274", "处方号：71603", "就诊序号：51869", "体重：/（kg）", "药物过敏史：无", "住址：新密市", "开方日期：2024-12-30", "08：16", "就诊科室：内科门诊", "临床诊断：糖", "Rp:", "盐酸二甲双胍片", "0.5g*60 X 6盒", "用法：每次0.5g 一日三次 口服", "备注：", "医师：张建鹏", "审核：", "核对：", "金额合计：60.00元", "调配：", "发药：", "药房：西药费"]

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
2026-08-10 13:25:22,901 INFO     29 [qwen-vl-text] coord API raw response (len=1454):
[
	{"text": "普通", "bbox": [802, 55, 845, 72]},
	{"text": ".中西医结合医院处方笺", "bbox": [357, 87, 778, 116]},
	{"text": "姓名：", "bbox": [123, 150, 178, 167]},
	{"text": "性别：男", "bbox": [335, 150, 427, 167]},
	{"text": "年龄：53岁", "bbox": [463, 150, 584, 167]},
	{"text": "费别：自费", "bbox": [681, 150, 799, 167]},
	{"text": "病人ID：M024274", "bbox": [123, 170, 293, 185]},
	{"text": "处方号：71603", "bbox": [355, 170, 492, 185]},
	{"text": "就诊序号：51869", "bbox": [522, 170, 693, 185]},
	{"text": "体重：/（kg）", "bbox": [713, 170, 838, 187]},
	{"text": "药物过敏史：无", "bbox": [123, 190, 288, 207]},
	{"text": "住址：新密市", "bbox": [475, 190, 614, 207]},
	{"text": "开方日期：2024-12-30", "bbox": [123, 217, 350, 234]},
	{"text": "08：16", "bbox": [384, 218, 457, 233]},
	{"text": "就诊科室：内科门诊", "bbox": [491, 217, 702, 234]},
	{"text": "临床诊断：糖", "bbox": [123, 250, 261, 268]},
	{"text": "Rp:", "bbox": [123, 305, 178, 330]},
	{"text": "盐酸二甲双胍片", "bbox": [167, 333, 330, 350]},
	{"text": "0.5g*60 X 6盒", "bbox": [519, 333, 674, 351]},
	{"text": "用法：每次0.5g 一日三次 口服", "bbox": [205, 366, 541, 383]},
	{"text": "备注：", "bbox": [195, 778, 251, 795]},
	{"text": "医师：张建鹏", "bbox": [697, 804, 841, 821]},
	{"text": "审核：", "bbox": [180, 840, 236, 857]},
	{"text": "核对：", "bbox": [408, 840, 465, 857]},
	{"text": "金额合计：60.00元", "bbox": [614, 841, 824, 858]},
	{"text": "调配：", "bbox": [180, 865, 236, 882]},
	{"text": "发药：", "bbox": [408, 865, 465, 882]},
	{"text": "药房：西药费", "bbox": [637, 866, 780, 884]}
]
2026-08-10 13:25:22,901 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=8.1s
2026-08-10 13:25:22,901 INFO     29 [qwen-vl-text] coord item[0]: text=普通, bbox=[802, 55, 845, 72]
2026-08-10 13:25:22,902 INFO     29 [qwen-vl-text] coord item[1]: text=.中西医结合医院处方笺, bbox=[357, 87, 778, 116]
2026-08-10 13:25:22,902 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[123, 150, 178, 167]
2026-08-10 13:25:22,902 INFO     29 [qwen-vl-text] coord item[3]: text=性别：男, bbox=[335, 150, 427, 167]
2026-08-10 13:25:22,902 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：53岁, bbox=[463, 150, 584, 167]
2026-08-10 13:25:22,902 INFO     29 [qwen-vl-text] coord item[5]: text=费别：自费, bbox=[681, 150, 799, 167]
2026-08-10 13:25:22,902 INFO     29 [qwen-vl-text] coord item[6]: text=病人ID：M024274, bbox=[123, 170, 293, 185]
2026-08-10 13:25:22,902 INFO     29 [qwen-vl-text] coord item[7]: text=处方号：71603, bbox=[355, 170, 492, 185]
2026-08-10 13:25:22,903 INFO     29 [qwen-vl-text] coord item[8]: text=就诊序号：51869, bbox=[522, 170, 693, 185]
2026-08-10 13:25:22,903 INFO     29 [qwen-vl-text] coord item[9]: text=体重：/（kg）, bbox=[713, 170, 838, 187]
2026-08-10 13:25:22,903 INFO     29 [qwen-vl-text] coord item[10]: text=药物过敏史：无, bbox=[123, 190, 288, 207]
2026-08-10 13:25:22,903 INFO     29 [qwen-vl-text] coord item[11]: text=住址：新密市, bbox=[475, 190, 614, 207]
2026-08-10 13:25:22,903 INFO     29 [qwen-vl-text] coord item[12]: text=开方日期：2024-12-30, bbox=[123, 217, 350, 234]
2026-08-10 13:25:22,903 INFO     29 [qwen-vl-text] coord item[13]: text=08：16, bbox=[384, 218, 457, 233]
2026-08-10 13:25:22,903 INFO     29 [qwen-vl-text] coord item[14]: text=就诊科室：内科门诊, bbox=[491, 217, 702, 234]
2026-08-10 13:25:22,903 INFO     29 [qwen-vl-text] coord item[15]: text=临床诊断：糖, bbox=[123, 250, 261, 268]
2026-08-10 13:25:22,903 INFO     29 [qwen-vl-text] coord item[16]: text=Rp:, bbox=[123, 305, 178, 330]
2026-08-10 13:25:22,903 INFO     29 [qwen-vl-text] coord item[17]: text=盐酸二甲双胍片, bbox=[167, 333, 330, 350]
2026-08-10 13:25:22,903 INFO     29 [qwen-vl-text] coord item[18]: text=0.5g*60 X 6盒, bbox=[519, 333, 674, 351]
2026-08-10 13:25:22,903 INFO     29 [qwen-vl-text] coord item[19]: text=用法：每次0.5g 一日三次 口服, bbox=[205, 366, 541, 383]
2026-08-10 13:25:22,903 INFO     29 [qwen-vl-text] coord item[20]: text=备注：, bbox=[195, 778, 251, 795]
2026-08-10 13:25:22,904 INFO     29 [qwen-vl-text] coord item[21]: text=医师：张建鹏, bbox=[697, 804, 841, 821]
2026-08-10 13:25:22,904 INFO     29 [qwen-vl-text] coord item[22]: text=审核：, bbox=[180, 840, 236, 857]
2026-08-10 13:25:22,904 INFO     29 [qwen-vl-text] coord item[23]: text=核对：, bbox=[408, 840, 465, 857]
2026-08-10 13:25:22,904 INFO     29 [qwen-vl-text] coord item[24]: text=金额合计：60.00元, bbox=[614, 841, 824, 858]
2026-08-10 13:25:22,904 INFO     29 [qwen-vl-text] coord item[25]: text=调配：, bbox=[180, 865, 236, 882]
2026-08-10 13:25:22,904 INFO     29 [qwen-vl-text] coord item[26]: text=发药：, bbox=[408, 865, 465, 882]
2026-08-10 13:25:22,904 INFO     29 [qwen-vl-text] coord item[27]: text=药房：西药费, bbox=[637, 866, 780, 884]
2026-08-10 13:25:22,904 INFO     29 [qwen-vl-text] page=2 — 28/28 coords, api_time=8.1s
2026-08-10 13:25:22,905 INFO     29 [qwen-vl-text] new_positions (28):
[[2, 477.19, 502.775, 46.309999999999995, 60.623999999999995], [2, 212.415, 462.90999999999997, 73.25399999999999, 97.672], [2, 73.185, 105.91, 126.3, 140.614], [2, 199.325, 254.065, 126.3, 140.614], [2, 275.485, 347.47999999999996, 126.3, 140.614], [2, 405.195, 475.405, 126.3, 140.614], [2, 73.185, 174.33499999999998, 143.14, 155.76999999999998], [2, 211.225, 292.74, 143.14, 155.76999999999998], [2, 310.59, 412.335, 143.14, 155.76999999999998], [2, 424.23499999999996, 498.60999999999996, 143.14, 157.454], [2, 73.185, 171.35999999999999, 159.98, 174.29399999999998], [2, 282.625, 365.33, 159.98, 174.29399999999998], [2, 73.185, 208.25, 182.714, 197.028], [2, 228.48, 271.91499999999996, 183.55599999999998, 196.186], [2, 292.145, 417.69, 182.714, 197.028], [2, 73.185, 155.295, 210.5, 225.656], [2, 73.185, 105.91, 256.81, 277.86], [2, 99.365, 196.35, 280.38599999999997, 294.7], [2, 308.805, 401.03, 280.38599999999997, 295.542], [2, 121.975, 321.895, 308.17199999999997, 322.486], [2, 116.02499999999999, 149.345, 655.076, 669.39], [2, 414.715, 500.395, 676.968, 691.2819999999999], [2, 107.1, 140.42, 707.28, 721.5939999999999], [2, 242.76, 276.675, 707.28, 721.5939999999999], [2, 365.33, 490.28, 708.122, 722.4359999999999], [2, 107.1, 140.42, 728.3299999999999, 742.644], [2, 242.76, 276.675, 728.3299999999999, 742.644], [2, 379.015, 464.09999999999997, 729.172, 744.328]]
2026-08-10 13:25:22,905 INFO     29 [qwen-vl-text] ═══ DONE ═══ 28 positions, pages=1, time=10.3s
2026-08-10 13:25:22,905 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:25:22,907 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:25:22,907 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 13:25:22,908 INFO     29 [qwen-vl-text] positions(30): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:25:22,908 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [30]
2026-08-10 13:25:23,053 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:25:23,054 INFO     29 [qwen-vl-text] LLM extraction start, text_len=256
2026-08-10 13:25:23,054 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:25:23,054 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 84, \"bbox_end\": 113, \"encounter_dates\": [\"2025-03-26\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "中西医结合医院处方笺\n姓名：\n性别：男\n年龄：53岁\n费别：自费\n病人ID：M024274\n处方号：71604\n就诊序号：71603\n体重：80 (kg)\n药物过敏史：无\n住址：河南郑州新密市\n开方日期：2025 03-26 14:42\n就诊科室：内科门诊\n临床诊断：糖尿病\n中医诊断：消渴症\nRp：\n盐酸二甲双胍片\n0.5g*36\nX 8盒\n用法：每次0.5g TID 口服\n备注：\n医师：张建鹏\n审核：\n核对：\n金额合计：80.00元\n调配：\n发药：\n药房：西药房\nCS 扫描全能王\n3亿人都在用的扫描App",
    "role": "user"
  }
]
2026-08-10 13:25:25,163 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:25:25,164 INFO     29 [qwen-vl-text] LLM output (len=412):
{
  "encounter_date": "2025-03-26",
  "prescription_type": "门诊处方",
  "prescriber": "张建鹏",
  "department": "内科门诊",
  "diagnosis": "糖尿病;消渴症",
  "items": [
    {
      "drug_generic_name": "盐酸二甲双胍片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "0.5g",
      "frequency": "TID",
      "route": "口服",
      "duration_days": null,
      "quantity": "8盒",
      "notes": null
    }
  ]
}
2026-08-10 13:25:25,164 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-03-26]
2026-08-10 13:25:25,165 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=459133, prompt_len=959
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共30行）
["中西医结合医院处方笺", "姓名：", "性别：男", "年龄：53岁", "费别：自费", "病人ID：M024274", "处方号：71604", "就诊序号：71603", "体重：80 (kg)", "药物过敏史：无", "住址：河南郑州新密市", "开方日期：2025 03-26 14:42", "就诊科室：内科门诊", "临床诊断：糖尿病", "中医诊断：消渴症", "Rp：", "盐酸二甲双胍片", "0.5g*36", "X 8盒", "用法：每次0.5g TID 口服", "备注：", "医师：张建鹏", "审核：", "核对：", "金额合计：80.00元", "调配：", "发药：", "药房：西药房", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord API raw response (len=1578):
[
	{"text": "中西医结合医院处方笺", "bbox": [234, 72, 807, 103]},
	{"text": "姓名：", "bbox": [148, 130, 284, 146]},
	{"text": "性别：男", "bbox": [370, 129, 456, 145]},
	{"text": "年龄：53岁", "bbox": [500, 128, 607, 144]},
	{"text": "费别：自费", "bbox": [712, 127, 812, 144]},
	{"text": "病人ID：M024274", "bbox": [148, 153, 317, 169]},
	{"text": "处方号：71604", "bbox": [390, 152, 524, 168]},
	{"text": "就诊序号：71603", "bbox": [549, 152, 711, 168]},
	{"text": "体重：80 (kg)", "bbox": [746, 150, 885, 167]},
	{"text": "药物过敏史：无", "bbox": [148, 175, 305, 191]},
	{"text": "住址：河南郑州新密市", "bbox": [500, 175, 716, 191]},
	{"text": "开方日期：2025 03-26 14:42", "bbox": [148, 199, 451, 215]},
	{"text": "就诊科室：内科门诊", "bbox": [500, 198, 706, 214]},
	{"text": "临床诊断：糖尿病", "bbox": [150, 231, 342, 247]},
	{"text": "中医诊断：消渴症", "bbox": [576, 230, 746, 247]},
	{"text": "Rp：", "bbox": [152, 281, 212, 307]},
	{"text": "盐酸二甲双胍片", "bbox": [194, 308, 357, 325]},
	{"text": "0.5g*36", "bbox": [562, 308, 643, 325]},
	{"text": "X 8盒", "bbox": [677, 308, 736, 324]},
	{"text": "用法：每次0.5g TID 口服", "bbox": [241, 340, 529, 356]},
	{"text": "备注：", "bbox": [224, 750, 282, 767]},
	{"text": "医师：张建鹏", "bbox": [666, 774, 798, 791]},
	{"text": "审核：", "bbox": [209, 810, 265, 827]},
	{"text": "核对：", "bbox": [438, 810, 494, 827]},
	{"text": "金额合计：80.00元", "bbox": [639, 810, 838, 827]},
	{"text": "调配：", "bbox": [209, 837, 265, 854]},
	{"text": "发药：", "bbox": [438, 837, 494, 854]},
	{"text": "药房：西药房", "bbox": [686, 837, 820, 854]},
	{"text": "CS 扫描全能王", "bbox": [861, 958, 976, 974]},
	{"text": "3亿人都在用的扫描App", "bbox": [861, 977, 976, 986]}
]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord API: raw_items=30, valid_items=30, elapsed=8.4s
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[0]: text=中西医结合医院处方笺, bbox=[234, 72, 807, 103]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[148, 130, 284, 146]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[2]: text=性别：男, bbox=[370, 129, 456, 145]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：53岁, bbox=[500, 128, 607, 144]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[4]: text=费别：自费, bbox=[712, 127, 812, 144]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[5]: text=病人ID：M024274, bbox=[148, 153, 317, 169]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[6]: text=处方号：71604, bbox=[390, 152, 524, 168]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[7]: text=就诊序号：71603, bbox=[549, 152, 711, 168]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[8]: text=体重：80 (kg), bbox=[746, 150, 885, 167]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[9]: text=药物过敏史：无, bbox=[148, 175, 305, 191]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[10]: text=住址：河南郑州新密市, bbox=[500, 175, 716, 191]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[11]: text=开方日期：2025 03-26 14:42, bbox=[148, 199, 451, 215]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[12]: text=就诊科室：内科门诊, bbox=[500, 198, 706, 214]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[13]: text=临床诊断：糖尿病, bbox=[150, 231, 342, 247]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[14]: text=中医诊断：消渴症, bbox=[576, 230, 746, 247]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[15]: text=Rp：, bbox=[152, 281, 212, 307]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[16]: text=盐酸二甲双胍片, bbox=[194, 308, 357, 325]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[17]: text=0.5g*36, bbox=[562, 308, 643, 325]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[18]: text=X 8盒, bbox=[677, 308, 736, 324]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[19]: text=用法：每次0.5g TID 口服, bbox=[241, 340, 529, 356]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[20]: text=备注：, bbox=[224, 750, 282, 767]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[21]: text=医师：张建鹏, bbox=[666, 774, 798, 791]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[22]: text=审核：, bbox=[209, 810, 265, 827]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[23]: text=核对：, bbox=[438, 810, 494, 827]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[24]: text=金额合计：80.00元, bbox=[639, 810, 838, 827]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[25]: text=调配：, bbox=[209, 837, 265, 854]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[26]: text=发药：, bbox=[438, 837, 494, 854]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[27]: text=药房：西药房, bbox=[686, 837, 820, 854]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[28]: text=CS 扫描全能王, bbox=[861, 958, 976, 974]
2026-08-10 13:25:33,600 INFO     29 [qwen-vl-text] coord item[29]: text=3亿人都在用的扫描App, bbox=[861, 977, 976, 986]
2026-08-10 13:25:33,601 INFO     29 [qwen-vl-text] page=4 — 30/30 coords, api_time=8.4s
2026-08-10 13:25:33,601 INFO     29 [qwen-vl-text] new_positions (30):
[[4, 139.23, 480.16499999999996, 60.623999999999995, 86.726], [4, 88.06, 168.98, 109.46, 122.932], [4, 220.14999999999998, 271.32, 108.618, 122.08999999999999], [4, 297.5, 361.16499999999996, 107.776, 121.24799999999999], [4, 423.64, 483.14, 106.934, 121.24799999999999], [4, 88.06, 188.61499999999998, 128.826, 142.298], [4, 232.04999999999998, 311.78, 127.984, 141.456], [4, 326.655, 423.04499999999996, 127.984, 141.456], [4, 443.87, 526.5749999999999, 126.3, 140.614], [4, 88.06, 181.475, 147.35, 160.822], [4, 297.5, 426.02, 147.35, 160.822], [4, 88.06, 268.34499999999997, 167.558, 181.03], [4, 297.5, 420.07, 166.716, 180.188], [4, 89.25, 203.48999999999998, 194.50199999999998, 207.974], [4, 342.71999999999997, 443.87, 193.66, 207.974], [4, 90.44, 126.14, 236.602, 258.49399999999997], [4, 115.42999999999999, 212.415, 259.336, 273.65], [4, 334.39, 382.585, 259.336, 273.65], [4, 402.815, 437.91999999999996, 259.336, 272.808], [4, 143.39499999999998, 314.755, 286.28, 299.752], [4, 133.28, 167.79, 631.5, 645.814], [4, 396.27, 474.81, 651.708, 666.0219999999999], [4, 124.35499999999999, 157.67499999999998, 682.02, 696.334], [4, 260.61, 293.93, 682.02, 696.334], [4, 380.205, 498.60999999999996, 682.02, 696.334], [4, 124.35499999999999, 157.67499999999998, 704.754, 719.068], [4, 260.61, 293.93, 704.754, 719.068], [4, 408.16999999999996, 487.9, 704.754, 719.068], [4, 512.295, 580.72, 806.636, 820.108], [4, 512.295, 580.72, 822.634, 830.212]]
2026-08-10 13:25:33,601 INFO     29 [qwen-vl-text] ═══ DONE ═══ 30 positions, pages=1, time=10.7s
2026-08-10 13:25:33,615 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 13:25:33,616 INFO     29 [Trace] task=c6f37d04 | doc=Gxdo郑州中心糖尿病.pdf | Extractor:Prescription | outputs={"chunks": "2 items, types={'PrescriptionRecord': 2}", "html": "", "json": "130 items", "markdown": "", "text": "", "name": "Gxdo郑州中心糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 1, \"chunks_Prescription\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:25:33,616 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 13:25:33,616 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:25:33.616+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 48, "failed": 0, "current": {"c6f37d0494be11f1bd9827cf206dfa2d": {"id": "c6f37d0494be11f1bd9827cf206dfa2d", "doc_id": "c6bfa85894be11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Gxdo\u90d1\u5dde\u4e2d\u5fc3\u7cd6\u5c3f\u75c5.pdf", "type": "pdf", "location": "Gxdo\u90d1\u5dde\u4e2d\u5fc3\u7cd6\u5c3f\u75c5.pdf", "size": 1474288, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368252776, "task_type": "dataflow", "root_trace_id": "0739225e0c644d63a7cc49e0ecacc097", "root_traceparent": "00-0739225e0c644d63a7cc49e0ecacc097-05128704d7f5e09a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:25:33,623 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:25:33,623 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:25:35,231 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:25:35,237 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 13:25:35,238 INFO     29 [Trace] task=c6f37d04 | doc=Gxdo郑州中心糖尿病.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "130 items", "markdown": "", "text": "", "name": "Gxdo郑州中心糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 1, \"chunks_Prescription\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:25:35,238 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 13:25:35,242 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:25:35,242 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:25:35,756 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:25:35,761 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 13:25:35,761 INFO     29 [Trace] task=c6f37d04 | doc=Gxdo郑州中心糖尿病.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "130 items", "markdown": "", "text": "", "name": "Gxdo郑州中心糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 1, \"chunks_Prescription\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:25:35,761 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 13:25:35,766 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:25:35,767 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:25:36,862 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:25:36,867 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 13:25:36,867 INFO     29 [Trace] task=c6f37d04 | doc=Gxdo郑州中心糖尿病.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "130 items", "markdown": "", "text": "", "name": "Gxdo郑州中心糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 1, \"chunks_Prescription\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:25:36,867 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 13:25:36,872 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:25:36,872 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:25:37,360 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:25:37,371 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 13:25:37,371 INFO     29 [Trace] task=c6f37d04 | doc=Gxdo郑州中心糖尿病.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "130 items", "markdown": "", "text": "", "name": "Gxdo郑州中心糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 1, \"chunks_Prescription\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:25:37,371 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 13:25:37,372 INFO     29 [ChunkMerger] Merged 6 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 2, 'Extractor:Prescription': 2, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 5 noise chunks)
2026-08-10 13:25:37,386 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 13:25:37,386 INFO     29 [Trace] task=c6f37d04 | doc=Gxdo郑州中心糖尿病.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "6 items, types={'LabReport': 1, 'OutpatientRecord': 1, 'MedicationRecord': 2, 'PrescriptionRecord': 2}", "name": "Gxdo郑州中心糖尿病.pdf"}
2026-08-10 13:25:37,386 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 13:25:37,415 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786368253153, 'update_date': datetime.datetime(2026, 8, 10, 13, 24, 13), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1037354, 'status': '1'}
2026-08-10 13:25:37,642 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   糖化血红蛋白测定  HbA1c  10.7%  %  4-6%  True   
---
中西医结合医院
病人门（急）诊病历
病人ID M024274 姓名
性别：男 出生时间： 1972年03月01日
籍贯： 汉族 婚否：已婚 职业：无
身份证号： 电话号码：
工作单位： 常住地址：新密市大隗镇
门诊号： 71603 接诊时间： 2025年3月26日 14时29分
就诊时间：2025-03-26 14:29:04 体温：36.5 ℃
主诉：糖尿病20年
现病史：20年前出现多饮、多尿、多食，曾规律服用二甲双胍缓释片，格列本脲
片，消渴丸等药，血糖控制不佳，为求进一步治疗前来就诊。
体格检查：
西医诊断：1.糖尿病 中医诊断：
建议： 1、糖尿病饮食；保持心情愉悦；
2、适量运动；
3、规律服药；
4、定期监测血糖；
5、不适随诊。
过敏史：无
家族史：有
既往史：无
处理：给予空腹血糖、糖化血红蛋白检测，以了解血糖控制情况
备注：
打印时间：2025.3.26 科室：内科门诊 医生：张建鹏
---
顺中西医结合医院
527647
自费
西药费
60.00
大额记账:
大病补充:
原账户余额:
已审核
现金支付:
陆拾元整
60.00
527647
0061
普通
---
529576
0061
2025-03-2
江顺中西医结合医院
529576
男
自费
西药费
80.00
大额记账：
大病补充：
捌拾元整
原帐户余额：
现金支付：
80.00
80.00
---
普通
.中西医结合医院处方笺
姓名：
性别：男
年龄：53岁
费别：自费
病人ID：M024274
处方号：71603
就诊序号：51869
体重：/（kg）
药物过敏史：无
住址：新密市
开方日期：2024-12-30
08：16
就诊科室：内科门诊
临床诊断：糖
Rp:
盐酸二甲双胍片
0.5g*60 X 6盒
用法：每次0.5g 一日三次 口服
备注：
医师：张建鹏
审核：
核对：
金额合计：60.00元
调配：
发药：
药房：西药费
---
中西医结合医院处方笺
姓名：
性别：男
年龄：53岁
费别：自费
病人ID：M024274
处方号：71604
就诊序号：71603
体重：80 (kg)
药物过敏史：无
住址：河南郑州新密市
开方日期：2025 03-26 14:42
就诊科室：内科门诊
临床诊断：糖尿病
中医诊断：消渴症
Rp：
盐酸二甲双胍片
0.5g*36
X 8盒
用法：每次0.5g TID 口服
备注：
医师：张建鹏
审核：
核对：
金额合计：80.00元
调配：
发药：
药房：西药房
CS 扫描全能王
3亿人都在用的扫描App
2026-08-10 13:25:37,951 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 13:25:37,951 INFO     29 [Trace] task=c6f37d04 | doc=Gxdo郑州中心糖尿病.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "6 items, types={'LabReport': 1, 'OutpatientRecord': 1, 'MedicationRecord': 2, 'PrescriptionRecord': 2}", "name": "Gxdo郑州中心糖尿病.pdf", "embedding_token_consumption": 910}
2026-08-10 13:25:37,951 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 13:25:38,129 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 13:25:38,129 INFO     29 [Trace] task=c6f37d04 | doc=Gxdo郑州中心糖尿病.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":6,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 13:25:38,132 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(2, 79, 254, 474, 499) row[-1]=(2, 79, 254, 474, 499)
2026-08-10 13:25:38,132 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:25:38,132 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:25:38,132 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:25:38,132 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:25:38,132 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:25:38,137 INFO     29 set_progress(c6f37d0494be11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 13:25:38 [DOC Engine]:
Start to index...
2026-08-10 13:25:38,158 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.016s]
2026-08-10 13:25:38,162 INFO     29 set_progress(c6f37d0494be11f1bd9827cf206dfa2d), progress: 0.8166666666666668, progress_msg: 
2026-08-10 13:25:38,174 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.009s]
2026-08-10 13:25:38,181 INFO     29 set_progress(c6f37d0494be11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 13:25:38 Indexing done (0.04s). Task done (80.53s)
2026-08-10 13:25:38,185 INFO     29 [Done], chunks(6), token(910), elapsed:80.53
2026-08-10 13:25:38,261 INFO     29 handle_task done for task {"id": "c6f37d0494be11f1bd9827cf206dfa2d", "doc_id": "c6bfa85894be11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Gxdo\u90d1\u5dde\u4e2d\u5fc3\u7cd6\u5c3f\u75c5.pdf", "type": "pdf", "location": "Gxdo\u90d1\u5dde\u4e2d\u5fc3\u7cd6\u5c3f\u75c5.pdf", "size": 1474288, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786368252776, "task_type": "dataflow", "root_trace_id": "0739225e0c644d63a7cc49e0ecacc097", "root_traceparent": "00-0739225e0c644d63a7cc49e0ecacc097-05128704d7f5e09a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
