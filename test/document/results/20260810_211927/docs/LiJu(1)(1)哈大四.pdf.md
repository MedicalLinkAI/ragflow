# 基准结果：LiJu(1)(1)哈大四.pdf

## 基本信息

- 文件：`LiJu(1)(1)哈大四.pdf`
- 大小：1878.7 KB
- PDF 总页数：7
- doc_id：`4c2d3d1094c011f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T21:35:04  完成时间：2026-08-10T21:36:58  耗时：114.0s
- progress_msg：`13:36:52 Indexing done (0.05s). Task done (100.84s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 58668134 | 1 | 2-2 | 哈尔滨美颐医院门诊单 门诊号：102800000989 诊疗号：00081601 |
| 2 | 88d71f75 | 1 | 5-5 | 哈尔滨康华大药房有限公 NO.55550534536320004523 日期:  |
| 3 | 9c073868 | 1 | 3-3 | <table><tr><td>糖化血红蛋白</td><td>HbA1c</td> |
| 4 | 23904bf4 | 1 | 4-4 | <table><tr><td>糖化血红蛋白</td><td>None</td>< |
| 5 | d429ddc7 | 1 | 6-6 | <table><tr><td>糖化血红蛋白</td><td>None</td>< |
| 6 | e5abbb42 | 1 | 7-7 | <table><tr><td>*葡萄糖</td><td>GLU</td><td> |

- chunks 总数：6
- 各 chunk 页数合计（含跨页重复）：6
- 页码并集：`[2, 3, 4, 5, 6, 7]`
- 覆盖页数：6 / 7；缺失页：`[1]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：❌ 未完全覆盖：覆盖 6/7 页，缺失 [1]，超范围 []**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 1 | 0 | 1 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 1 | 1 | 1 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 0 | 1 | 0 | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 4 | 0 | 4 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 1, "LabReport": 4, "MedicationRecord": 1}`
- ChunkMerger：`{"found": true, "merged": 6, "sources": 9, "stats": {"Extractor:LabExam": 4, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 13:36:52,034 INFO     29 [ChunkMerger] Merged 6 chunks from 9 sources: {'Extractor:LabExam': 4, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 13:35:07,282 INFO     29 handle_task begin for task {"id": "4c58c27894c011f1bd9827cf206dfa2d", "doc_id": "4c2d3d1094c011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LiJu(1)(1)\u54c8\u5927\u56db.pdf", "type": "pdf", "location": "LiJu(1)(1)\u54c8\u5927\u56db.pdf", "size": 1923761, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368906074, "task_type": "dataflow", "root_trace_id": "4f4dfcf132bb46f882e4ea4e62b4012a", "root_traceparent": "00-4f4dfcf132bb46f882e4ea4e62b4012a-9654b1ff0cfeac68-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 13:35:07,531 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 13:35:07,670 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 13:35:07,679 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:35:07,679 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 13:35:07,679 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 13:35:07,687 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 13:35:07,687 INFO     29 ============================================================
2026-08-10 13:35:07,687 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 13:35:07,687 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 13:35:07,687 INFO     29 ============================================================
2026-08-10 13:35:07,687 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 13:35:07,687 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 13:35:07,689 INFO     29 No torch found.
2026-08-10 13:35:08,382 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=7
2026-08-10 13:35:08,506 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=237080, prompt_len=764
2026-08-10 13:35:11,831 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-04-11"}
```
2026-08-10 13:35:11,832 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2025-04-11
2026-08-10 13:35:11,838 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=237080, prompt_len=401
2026-08-10 13:35:13,444 INFO     29 [qwen-vl-parser] text API response (len=234):
["受试者推荐情况汇总", "单药-联合？：联合", "姓名缩写：LIJU", "年龄：66", "性别：男", "身高：173cm", "体重：85kg", "BMI：28.4", "首次诊断T2DM时间：2024.5", "最近血糖&糖化检测结果：8.55", "糖化-日期：2025.4.13", "遗传病学（乙肝、丙肝、梅毒、艾滋", "）是否阳性：否", "既往疾病：无", "推荐的中心：哈大四", "居住地：哈尔滨", "提报时间：2025.4.11"]
2026-08-10 13:35:13,444 INFO     29 [qwen-vl-parser] page=1 text: 17 lines (bbox 0-16)
2026-08-10 13:35:13,444 INFO     29 [qwen-vl-parser] page=1 text: 17 sections
2026-08-10 13:35:13,660 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=781141, prompt_len=764
2026-08-10 13:35:16,921 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:35:16,921 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 13:35:16,927 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=781141, prompt_len=401
2026-08-10 13:35:19,418 INFO     29 [qwen-vl-parser] text API response (len=387):
["哈尔滨美颐医院门诊单", "门诊号：102800000989", "诊疗号：000816012", "姓名：", "性别：男", "年龄：65岁", "接诊时间：2024-05-06 09:37:20", "接诊科室：门诊", "接诊医师：/", "临床诊断：2型糖尿病", "主诉：口干、多尿、多饮半月，无消瘦", "现病史：无诱因出现口干、多尿、多饮症状，来院检查", "既往病史：无", "过敏史：无", "体格检查：未检查", "辅助检查：已回报", "治疗建议：", "1、糖尿病饮食；", "2、适当增加运动；", "3、口服二甲双胍片，每日3次 每次0.5g；", "4、监测血糖；", "5、门诊随访；", "打印日期：2024-05-06 15:48:23", "医师：", "主治医师", "杨泽志", "ZTE", "Axon 40 Ultra"]
2026-08-10 13:35:19,419 INFO     29 [qwen-vl-parser] page=2 text: 28 lines (bbox 17-44)
2026-08-10 13:35:19,419 INFO     29 [qwen-vl-parser] page=2 text: 28 sections
2026-08-10 13:35:19,604 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=629544, prompt_len=764
2026-08-10 13:35:23,107 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2024-05-06"
}
```
2026-08-10 13:35:23,107 INFO     29 [qwen-vl-parser] page=3 classify=table report_date=2024-05-06
2026-08-10 13:35:23,117 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=629544, prompt_len=756
2026-08-10 13:35:25,830 INFO     29 [qwen-vl-parser] table API response (len=427):
\begin{tabular}{llllllll}
\hline
姓名: & & 科室: 门诊 & 仪器: 3.8--5.8 & 样本号: 10 & & & \\
性别: 男 & & 住院号: 无 & 床号: 无 & 标本种类: 60 & & & \\
年龄: 65 岁 & & 门诊号: 102800000989 诊断: 待查 & & 备 & 注: 60 & & \\
\hline
序号 & 代号 & 项目 & 结果 & 状态 & 单位 & 参考值 & \\
\hline
1 & HbA1c & 糖化血红蛋白 & 8.3 & $\uparrow$ & \% & 4.1--6.1 & \\
\hline
送检医生: & & 送检时间: 2024-05-06 & 10:16:18 & & & 检验者: & \\
& & 报告时间: 2024-05-06 & 14:58:47 & & & 审核者: & \\
\hline
\end{tabular}
2026-08-10 13:35:25,832 INFO     29 [qwen-vl-parser] page=3 table: 15 LaTeX lines (bbox 45-59)
2026-08-10 13:35:25,832 INFO     29 [qwen-vl-parser] page=3 table: 15 sections
2026-08-10 13:35:26,519 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3051608, prompt_len=764
2026-08-10 13:35:29,877 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:35:29.874+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 52, "failed": 0, "current": {"4c58c27894c011f1bd9827cf206dfa2d": {"id": "4c58c27894c011f1bd9827cf206dfa2d", "doc_id": "4c2d3d1094c011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LiJu(1)(1)\u54c8\u5927\u56db.pdf", "type": "pdf", "location": "LiJu(1)(1)\u54c8\u5927\u56db.pdf", "size": 1923761, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368906074, "task_type": "dataflow", "root_trace_id": "4f4dfcf132bb46f882e4ea4e62b4012a", "root_traceparent": "00-4f4dfcf132bb46f882e4ea4e62b4012a-9654b1ff0cfeac68-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:35:34,666 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-02-22"
}
```
2026-08-10 13:35:34,667 INFO     29 [qwen-vl-parser] page=4 classify=table report_date=2025-02-22
2026-08-10 13:35:34,683 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3051608, prompt_len=756
2026-08-10 13:35:36,093 INFO     29 [qwen-vl-parser] table API response (len=128):
\begin{tabular}{ccccc}
\hline
序号 & 项目名称 & 结果 & 参考值 & \\
\hline
1 & 糖化血红蛋白 & 7.62 & 3.8--5.8 & $\uparrow$ \\
\hline
\end{tabular}
2026-08-10 13:35:36,094 INFO     29 [qwen-vl-parser] page=4 table: 8 LaTeX lines (bbox 60-67)
2026-08-10 13:35:36,094 INFO     29 [qwen-vl-parser] page=4 table: 8 sections
2026-08-10 13:35:36,453 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1622590, prompt_len=764
2026-08-10 13:35:39,905 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-11-08"}
```
2026-08-10 13:35:39,906 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=2024-11-08
2026-08-10 13:35:39,918 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1622590, prompt_len=401
2026-08-10 13:35:41,945 INFO     29 [qwen-vl-parser] text API response (len=270):
["哈尔滨康华大药房有限公", "NO.55550534536320004523", "日期: 2024/11/08 14:24:49", "会员:  销售: 04", "882457 盐酸二甲双胍缓释片", "规格 0.5gx30T 产地: 北京", "批号 288241049 效期 2027-1", "数量 20 单价 8.00", "金额合计: ￥160.00 元", "应收 实收", "优惠 找零", "付款方式: 01 现金】", "健康热线:", "药品是特殊商品售出不退不", "L ZTE Axon 40 Ultra"]
2026-08-10 13:35:41,945 INFO     29 [qwen-vl-parser] page=5 text: 15 lines (bbox 68-82)
2026-08-10 13:35:41,945 INFO     29 [qwen-vl-parser] page=5 text: 15 sections
2026-08-10 13:35:42,077 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=284101, prompt_len=764
2026-08-10 13:35:45,730 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-04-13"
}
```
2026-08-10 13:35:45,731 INFO     29 [qwen-vl-parser] page=6 classify=table report_date=2025-04-13
2026-08-10 13:35:45,742 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=284101, prompt_len=756
2026-08-10 13:35:46,732 INFO     29 [qwen-vl-parser] table API response (len=134):
\begin{tabular}{ccccccccc}
\hline
序号 & 项目名称 & 结果 & 参考值 & 单位 \\
\hline
1 & 糖化血红蛋白 & 8.55 & 1 & 3.8--5.8 & & & & \\
\hline
\end{tabular}
2026-08-10 13:35:46,734 INFO     29 [qwen-vl-parser] page=6 table: 8 LaTeX lines (bbox 83-90)
2026-08-10 13:35:46,734 INFO     29 [qwen-vl-parser] page=6 table: 8 sections
2026-08-10 13:35:46,873 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=280377, prompt_len=764
2026-08-10 13:35:50,558 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-04-13"
}
```
2026-08-10 13:35:50,559 INFO     29 [qwen-vl-parser] page=7 classify=table report_date=2025-04-13
2026-08-10 13:35:50,572 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=280377, prompt_len=756
2026-08-10 13:35:51,559 INFO     29 [qwen-vl-parser] table API response (len=140):
\begin{tabular}{ccccccc}
\hline
序号 & 项目代码 & 项目名称 & 结果 & 参考值 & 单位 \\
\hline
1 & GLU & *葡萄糖 & 9.71 & 3.9--6.1 & mmol/L \\
\hline
\end{tabular}
2026-08-10 13:35:51,560 INFO     29 [qwen-vl-parser] page=7 table: 8 LaTeX lines (bbox 91-98)
2026-08-10 13:35:51,560 INFO     29 [qwen-vl-parser] page=7 table: 8 sections
2026-08-10 13:35:51,560 INFO     29 [qwen-vl-parser] parse_pdf done: 99 sections from 7 pages.
2026-08-10 13:35:51,569 INFO     29 Close text detector.
2026-08-10 13:35:52,002 INFO     29 Close text recognizer.
2026-08-10 13:35:52,385 INFO     29 Close recognizer.
2026-08-10 13:35:52,875 INFO     29 Close recognizer.
2026-08-10 13:35:53,323 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 13:35:53,323 INFO     29 [Trace] task=4c58c278 | doc=LiJu(1)(1)哈大四.pdf | Parser:MedLink | outputs={"html": "", "json": "99 items", "markdown": "", "text": "", "name": "LiJu(1)(1)哈大四.pdf", "output_format": "json"}
2026-08-10 13:35:53,323 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 13:35:53,338 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:35:53,339 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 受试者推荐情况汇总\n[BBOX-1] 单药-联合？：联合\n[BBOX-2] 姓名缩写：LIJU\n[BBOX-3] 年龄：66\n[BBOX-4] 性别：男\n[BBOX-5] 身高：173cm\n[BBOX-6] 体重：85kg\n[BBOX-7] BMI：28.4\n[BBOX-8] 首次诊断T2DM时间：2024.5\n[BBOX-9] 最近血糖&糖化检测结果：8.55\n[BBOX-10] 糖化-日期：2025.4.13\n[BBOX-11] 遗传病学（乙肝、丙肝、梅毒、艾滋\n[BBOX-12] ）是否阳性：否\n[BBOX-13] 既往疾病：无\n[BBOX-14] 推荐的中心：哈大四\n[BBOX-15] 居住地：哈尔滨\n[BBOX-16] 提报时间：2025.4.11\n[BBOX-17] 哈尔滨美颐医院门诊单\n[BBOX-18] 门诊号：102800000989\n[BBOX-19] 诊疗号：000816012\n[BBOX-20] 姓名：\n[BBOX-21] 性别：男\n[BBOX-22] 年龄：65岁\n[BBOX-23] 接诊时间：2024-05-06 09:37:20\n[BBOX-24] 接诊科室：门诊\n[BBOX-25] 接诊医师：/\n[BBOX-26] 临床诊断：2型糖尿病\n[BBOX-27] 主诉：口干、多尿、多饮半月，无消瘦\n[BBOX-28] 现病史：无诱因出现口干、多尿、多饮症状，来院检查\n[BBOX-29] 既往病史：无\n[BBOX-30] 过敏史：无\n[BBOX-31] 体格检查：未检查\n[BBOX-32] 辅助检查：已回报\n[BBOX-33] 治疗建议：\n[BBOX-34] 1、糖尿病饮食；\n[BBOX-35] 2、适当增加运动；\n[BBOX-36] 3、口服二甲双胍片，每日3次 每次0.5g；\n[BBOX-37] 4、监测血糖；\n[BBOX-38] 5、门诊随访；\n[BBOX-39] 打印日期：2024-05-06 15:48:23\n[BBOX-40] 医师：\n[BBOX-41] 主治医师\n[BBOX-42] 杨泽志\n[BBOX-43] ZTE\n[BBOX-44] Axon 40 Ultra\n[BBOX-45] \\begin{tabular}{llllllll}\n[BBOX-46] 报告时间: 2024-05-06\n[BBOX-47] \\hline\n[BBOX-48] 姓名: & & 科室: 门诊 & 仪器: 3.8--5.8 & 样本号: 10 & & & \\\\\n[BBOX-49] 性别: 男 & & 住院号: 无 & 床号: 无 & 标本种类: 60 & & & \\\\\n[BBOX-50] 年龄: 65 岁 & & 门诊号: 102800000989 诊断: 待查 & & 备 & 注: 60 & & \\\\\n[BBOX-51] \\hline\n[BBOX-52] 序号 & 代号 & 项目 & 结果 & 状态 & 单位 & 参考值 & \\\\\n[BBOX-53] \\hline\n[BBOX-54] 1 & HbA1c & 糖化血红蛋白 & 8.3 & $\\uparrow$ & \\% & 4.1--6.1 & \\\\\n[BBOX-55] \\hline\n[BBOX-56] 送检医生: & & 送检时间: 2024-05-06 & 10:16:18 & & & 检验者: & \\\\\n[BBOX-57] & & 报告时间: 2024-05-06 & 14:58:47 & & & 审核者: & \\\\\n[BBOX-58] \\hline\n[BBOX-59] \\end{tabular}\n[BBOX-60] \\begin{tabular}{ccccc}\n[BBOX-61] 报告时间: 2025-02-22\n[BBOX-62] \\hline\n[BBOX-63] 序号 & 项目名称 & 结果 & 参考值 & \\\\\n[BBOX-64] \\hline\n[BBOX-65] 1 & 糖化血红蛋白 & 7.62 & 3.8--5.8 & $\\uparrow$ \\\\\n[BBOX-66] \\hline\n[BBOX-67] \\end{tabular}\n[BBOX-68] 哈尔滨康华大药房有限公\n[BBOX-69] NO.55550534536320004523\n[BBOX-70] 日期: 2024/11/08 14:24:49\n[BBOX-71] 会员:  销售: 04\n[BBOX-72] 882457 盐酸二甲双胍缓释片\n[BBOX-73] 规格 0.5gx30T 产地: 北京\n[BBOX-74] 批号 288241049 效期 2027-1\n[BBOX-75] 数量 20 单价 8.00\n[BBOX-76] 金额合计: ￥160.00 元\n[BBOX-77] 应收 实收\n[BBOX-78] 优惠 找零\n[BBOX-79] 付款方式: 01 现金】\n[BBOX-80] 健康热线:\n[BBOX-81] 药品是特殊商品售出不退不\n[BBOX-82] L ZTE Axon 40 Ultra\n[BBOX-83] \\begin{tabular}{ccccccccc}\n[BBOX-84] 报告时间: 2025-04-13\n[BBOX-85] \\hline\n[BBOX-86] 序号 & 项目名称 & 结果 & 参考值 & 单位 \\\\\n[BBOX-87] \\hline\n[BBOX-88] 1 & 糖化血红蛋白 & 8.55 & 1 & 3.8--5.8 & & & & \\\\\n[BBOX-89] \\hline\n[BBOX-90] \\end{tabular}\n[BBOX-91] \\begin{tabular}{ccccccc}\n[BBOX-92] 报告时间: 2025-04-13\n[BBOX-93] \\hline\n[BBOX-94] 序号 & 项目代码 & 项目名称 & 结果 & 参考值 & 单位 \\\\\n[BBOX-95] \\hline\n[BBOX-96] 1 & GLU & *葡萄糖 & 9.71 & 3.9--6.1 & mmol/L \\\\\n[BBOX-97] \\hline\n[BBOX-98] \\end{tabular}"
  }
]
2026-08-10 13:35:58,592 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:35:58,608 INFO     29 [SmartSplitter] SmartSplitter done: 6 chunks from 6 LLM segments (all bbox_id). Types: {'OutpatientRecord': 1, 'LabReport': 4, 'MedicationRecord': 1}
2026-08-10 13:35:58,616 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 13:35:58,616 INFO     29 [Trace] task=4c58c278 | doc=LiJu(1)(1)哈大四.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "99 items", "markdown": "", "text": "", "name": "LiJu(1)(1)哈大四.pdf", "output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 1, 'LabReport': 4, 'MedicationRecord': 1}"}
2026-08-10 13:35:58,616 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 13:35:58,616 INFO     29 [ChunkRouter] Routed 6 chunks into 3 groups: {'chunks_Clinical': 1, 'chunks_LabExam': 4, 'chunks_Medication': 1}
2026-08-10 13:35:58,625 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 13:35:58,625 INFO     29 [Trace] task=4c58c278 | doc=LiJu(1)(1)哈大四.pdf | ChunkRouter:Router | outputs={"html": "", "json": "99 items", "markdown": "", "text": "", "name": "LiJu(1)(1)哈大四.pdf", "output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 1, 'LabReport': 4, 'MedicationRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 4, \"chunks_Medication\": 1}"}
2026-08-10 13:35:58,625 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 13:35:58,629 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:35:58,630 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:35:58,630 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[2]
2026-08-10 13:35:58,630 INFO     29 [qwen-vl-table] positions ： [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:35:58,871 INFO     29 [qwen-vl-table] page=2, rect=1278x959, img=(3550x2665)
2026-08-10 13:35:58,872 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:35:58,872 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 45, \"bbox_end\": 59, \"encounter_dates\": [\"2024-05-06\"], \"department\": \"门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllll}\n报告时间: 2024-05-06\n\\hline\n姓名: & & 科室: 门诊 & 仪器: 3.8--5.8 & 样本号: 10 & & & \\\\\n性别: 男 & & 住院号: 无 & 床号: 无 & 标本种类: 60 & & & \\\\\n年龄: 65 岁 & & 门诊号: 102800000989 诊断: 待查 & & 备 & 注: 60 & & \\\\\n\\hline\n序号 & 代号 & 项目 & 结果 & 状态 & 单位 & 参考值 & \\\\\n\\hline\n1 & HbA1c & 糖化血红蛋白 & 8.3 & $\\uparrow$ & \\% & 4.1--6.1 & \\\\\n\\hline\n送检医生: & & 送检时间: 2024-05-06 & 10:16:18 & & & 检验者: & \\\\\n& & 报告时间: 2024-05-06 & 14:58:47 & & & 审核者: & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:36:00,203 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:00,203 INFO     29 [qwen-vl-table] page=2 LLM output (len=216):
{
  "report_date": "2024-05-06",
  "items": [
    {
      "name": "糖化血红蛋白",
      "item_code": "HbA1c",
      "value": "8.3",
      "unit": "%",
      "reference_range": "4.1--6.1",
      "abnormal": true
    }
  ]
}
2026-08-10 13:36:00,203 INFO     29 [qwen-vl-table] coord grouping: {2: 1}
2026-08-10 13:36:00,205 INFO     29 [qwen-vl-table] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1071326, prompt_len=513
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
2026-08-10 13:36:05,449 INFO     29 [qwen-vl-table] coord API raw response (len=65):
```json
[
	{"text": "糖化血红蛋白", "bbox": [234, 456, 340, 480]}
]
```
2026-08-10 13:36:05,449 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=5.2s
2026-08-10 13:36:05,449 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白, bbox=[234, 456, 340, 480]
2026-08-10 13:36:05,450 INFO     29 [qwen-vl-table] page=2 coord: matched 1/1, time=5.2s
2026-08-10 13:36:05,450 INFO     29 [qwen-vl-table] new_positions (1):
[[3, 299.052, 434.52, 437.418, 460.44]]
2026-08-10 13:36:05,450 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=6.8s
2026-08-10 13:36:05,451 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:36:05,459 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:36:05,459 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[3]
2026-08-10 13:36:05,459 INFO     29 [qwen-vl-table] positions ： [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:36:05,913 INFO     29 [qwen-vl-table] page=3, rect=2122x956, img=(5896x2655)
2026-08-10 13:36:05,913 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:05,914 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 60, \"bbox_end\": 67, \"encounter_dates\": [\"2025-02-22\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccc}\n报告时间: 2025-02-22\n\\hline\n序号 & 项目名称 & 结果 & 参考值 & \\\\\n\\hline\n1 & 糖化血红蛋白 & 7.62 & 3.8--5.8 & $\\uparrow$ \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:36:05,915 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:36:05.915+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 52, "failed": 0, "current": {"4c58c27894c011f1bd9827cf206dfa2d": {"id": "4c58c27894c011f1bd9827cf206dfa2d", "doc_id": "4c2d3d1094c011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LiJu(1)(1)\u54c8\u5927\u56db.pdf", "type": "pdf", "location": "LiJu(1)(1)\u54c8\u5927\u56db.pdf", "size": 1923761, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368906074, "task_type": "dataflow", "root_trace_id": "4f4dfcf132bb46f882e4ea4e62b4012a", "root_traceparent": "00-4f4dfcf132bb46f882e4ea4e62b4012a-9654b1ff0cfeac68-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:36:07,040 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:07,040 INFO     29 [qwen-vl-table] page=3 LLM output (len=215):
{
  "report_date": "2025-02-22",
  "items": [
    {
      "name": "糖化血红蛋白",
      "item_code": null,
      "value": "7.62",
      "unit": null,
      "reference_range": "3.8--5.8",
      "abnormal": true
    }
  ]
}
2026-08-10 13:36:07,040 INFO     29 [qwen-vl-table] coord grouping: {3: 1}
2026-08-10 13:36:07,051 INFO     29 [qwen-vl-table] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4963959, prompt_len=513
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
2026-08-10 13:36:13,971 INFO     29 [qwen-vl-table] coord API raw response (len=65):
```json
[
	{"text": "糖化血红蛋白", "bbox": [141, 523, 292, 577]}
]
```
2026-08-10 13:36:13,972 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=6.9s
2026-08-10 13:36:13,972 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白, bbox=[141, 523, 292, 577]
2026-08-10 13:36:13,972 INFO     29 [qwen-vl-table] page=3 coord: matched 1/1, time=6.9s
2026-08-10 13:36:13,972 INFO     29 [qwen-vl-table] new_positions (1):
[[4, 299.2725, 619.77, 499.7265, 551.3235]]
2026-08-10 13:36:13,972 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=8.5s
2026-08-10 13:36:13,974 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:36:13,975 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:36:13,975 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[5]
2026-08-10 13:36:13,975 INFO     29 [qwen-vl-table] positions ： [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:36:14,103 INFO     29 [qwen-vl-table] page=5, rect=958x1276, img=(2662x3544)
2026-08-10 13:36:14,104 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:14,104 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 83, \"bbox_end\": 90, \"encounter_dates\": [\"2025-04-13\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2025-04-13\n\\hline\n序号 & 项目名称 & 结果 & 参考值 & 单位 \\\\\n\\hline\n1 & 糖化血红蛋白 & 8.55 & 1 & 3.8--5.8 & & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:36:15,679 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:15,679 INFO     29 [qwen-vl-table] page=5 LLM output (len=214):
{
  "report_date": "2025-04-13",
  "items": [
    {
      "name": "糖化血红蛋白",
      "item_code": null,
      "value": "8.55",
      "unit": "%",
      "reference_range": "3.8--5.8",
      "abnormal": true
    }
  ]
}
2026-08-10 13:36:15,680 INFO     29 [qwen-vl-table] coord grouping: {5: 1}
2026-08-10 13:36:15,681 INFO     29 [qwen-vl-table] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=460387, prompt_len=513
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
2026-08-10 13:36:19,057 INFO     29 [qwen-vl-table] coord API raw response (len=65):
```json
[
	{"text": "糖化血红蛋白", "bbox": [280, 177, 357, 189]}
]
```
2026-08-10 13:36:19,057 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=3.4s
2026-08-10 13:36:19,057 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白, bbox=[280, 177, 357, 189]
2026-08-10 13:36:19,057 INFO     29 [qwen-vl-table] page=5 coord: matched 1/1, time=3.4s
2026-08-10 13:36:19,057 INFO     29 [qwen-vl-table] new_positions (1):
[[6, 268.27079589843754, 342.04526477050786, 225.7794239501953, 241.08650354003905]]
2026-08-10 13:36:19,057 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=5.1s
2026-08-10 13:36:19,060 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:36:19,061 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:36:19,062 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[6]
2026-08-10 13:36:19,062 INFO     29 [qwen-vl-table] positions ： [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:36:19,225 INFO     29 [qwen-vl-table] page=6, rect=958x1276, img=(2662x3544)
2026-08-10 13:36:19,226 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:19,226 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 91, \"bbox_end\": 98, \"encounter_dates\": [\"2025-04-13\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccc}\n报告时间: 2025-04-13\n\\hline\n序号 & 项目代码 & 项目名称 & 结果 & 参考值 & 单位 \\\\\n\\hline\n1 & GLU & *葡萄糖 & 9.71 & 3.9--6.1 & mmol/L \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:36:20,386 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:20,386 INFO     29 [qwen-vl-table] page=6 LLM output (len=218):
{
  "report_date": "2025-04-13",
  "items": [
    {
      "name": "*葡萄糖",
      "item_code": "GLU",
      "value": "9.71",
      "unit": "mmol/L",
      "reference_range": "3.9--6.1",
      "abnormal": true
    }
  ]
}
2026-08-10 13:36:20,386 INFO     29 [qwen-vl-table] coord grouping: {6: 1}
2026-08-10 13:36:20,387 INFO     29 [qwen-vl-table] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=459871, prompt_len=511
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
*葡萄糖

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
2026-08-10 13:36:23,604 INFO     29 [qwen-vl-table] coord API raw response (len=62):
```json
[
	{"text": "葡萄糖", "bbox": [185, 165, 233, 175]}
]
```
2026-08-10 13:36:23,605 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=3.2s
2026-08-10 13:36:23,605 INFO     29 [qwen-vl-table] coord item[0]: text=葡萄糖, bbox=[185, 165, 233, 175]
2026-08-10 13:36:23,605 INFO     29 [qwen-vl-table] page=6 coord: matched 1/1, time=3.2s
2026-08-10 13:36:23,605 INFO     29 [qwen-vl-table] new_positions (1):
[[7, 177.25034729003906, 223.23962658691408, 210.47234436035157, 223.22824401855468]]
2026-08-10 13:36:23,605 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=4.5s
2026-08-10 13:36:23,612 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 13:36:23,612 INFO     29 [Trace] task=4c58c278 | doc=LiJu(1)(1)哈大四.pdf | Extractor:LabExam | outputs={"chunks": "4 items, types={'LabReport': 4}", "html": "", "json": "99 items", "markdown": "", "text": "", "name": "LiJu(1)(1)哈大四.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 4, \"chunks_Medication\": 1}"}
2026-08-10 13:36:23,612 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 13:36:23,616 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:23,617 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:36:24,036 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:24,047 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 13:36:24,047 INFO     29 [Trace] task=4c58c278 | doc=LiJu(1)(1)哈大四.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "99 items", "markdown": "", "text": "", "name": "LiJu(1)(1)哈大四.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 4, \"chunks_Medication\": 1}"}
2026-08-10 13:36:24,047 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 13:36:24,055 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:36:24,055 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:36:24,055 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 13:36:24,055 INFO     29 [qwen-vl-text] positions(26): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:36:24,055 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [26]
2026-08-10 13:36:24,285 INFO     29 [qwen-vl-text] page=1, rect=959x1278, img=(2665x3550), dpi=200
2026-08-10 13:36:24,286 INFO     29 [qwen-vl-text] LLM extraction start, text_len=284
2026-08-10 13:36:24,286 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:24,286 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 17, \"bbox_end\": 42, \"encounter_dates\": [\"2024-05-06\"], \"department\": \"门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "哈尔滨美颐医院门诊单\n门诊号：102800000989\n诊疗号：000816012\n姓名：\n性别：男\n年龄：65岁\n接诊时间：2024-05-06 09:37:20\n接诊科室：门诊\n接诊医师：/\n临床诊断：2型糖尿病\n主诉：口干、多尿、多饮半月，无消瘦\n现病史：无诱因出现口干、多尿、多饮症状，来院检查\n既往病史：无\n过敏史：无\n体格检查：未检查\n辅助检查：已回报\n治疗建议：\n1、糖尿病饮食；\n2、适当增加运动；\n3、口服二甲双胍片，每日3次 每次0.5g；\n4、监测血糖；\n5、门诊随访；\n打印日期：2024-05-06 15:48:23\n医师：\n主治医师\n杨泽志",
    "role": "user"
  }
]
2026-08-10 13:36:25,951 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:25,951 INFO     29 [qwen-vl-text] LLM output (len=244):
{
  "encounter_date": "2024-05-06",
  "chief_complaint": "口干、多尿、多饮半月，无消瘦",
  "present_illness": "无诱因出现口干、多尿、多饮症状，来院检查",
  "past_history": "无",
  "diagnosis": "2型糖尿病",
  "treatment_plan": "1、糖尿病饮食；2、适当增加运动；3、口服二甲双胍片，每日3次 每次0.5g；4、监测血糖；5、门诊随访；"
}
2026-08-10 13:36:25,951 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-05-06]
2026-08-10 13:36:25,953 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1398411, prompt_len=975
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["哈尔滨美颐医院门诊单", "门诊号：102800000989", "诊疗号：000816012", "姓名：", "性别：男", "年龄：65岁", "接诊时间：2024-05-06 09:37:20", "接诊科室：门诊", "接诊医师：/", "临床诊断：2型糖尿病", "主诉：口干、多尿、多饮半月，无消瘦", "现病史：无诱因出现口干、多尿、多饮症状，来院检查", "既往病史：无", "过敏史：无", "体格检查：未检查", "辅助检查：已回报", "治疗建议：", "1、糖尿病饮食；", "2、适当增加运动；", "3、口服二甲双胍片，每日3次 每次0.5g；", "4、监测血糖；", "5、门诊随访；", "打印日期：2024-05-06 15:48:23", "医师：", "主治医师", "杨泽志"]

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
2026-08-10 13:36:37,842 INFO     29 [qwen-vl-text] coord API raw response (len=1429):
[
	{"text": "哈尔滨美颐医院门诊单", "bbox": [335, 64, 717, 93]},
	{"text": "门诊号：102800000989", "bbox": [212, 117, 405, 133]},
	{"text": "诊疗号：000816012", "bbox": [633, 116, 798, 131]},
	{"text": "姓名：", "bbox": [211, 154, 257, 169]},
	{"text": "性别：男", "bbox": [432, 153, 507, 169]},
	{"text": "年龄：65岁", "bbox": [653, 153, 752, 168]},
	{"text": "接诊时间：2024-05-06 09:37:20", "bbox": [211, 191, 500, 206]},
	{"text": "接诊科室：门诊", "bbox": [538, 190, 671, 205]},
	{"text": "接诊医师：/", "bbox": [711, 189, 818, 204]},
	{"text": "临床诊断：2型糖尿病", "bbox": [211, 228, 399, 244]},
	{"text": "主诉：口干、多尿、多饮半月，无消瘦", "bbox": [211, 265, 537, 280]},
	{"text": "现病史：无诱因出现口干、多尿、多饮症状，来院检查", "bbox": [210, 301, 673, 317]},
	{"text": "既往病史：无", "bbox": [210, 339, 326, 354]},
	{"text": "过敏史：无", "bbox": [209, 376, 326, 392]},
	{"text": "体格检查：未检查", "bbox": [208, 414, 365, 429]},
	{"text": "辅助检查：已回报", "bbox": [208, 452, 365, 468]},
	{"text": "治疗建议：", "bbox": [208, 490, 294, 506]},
	{"text": "1、糖尿病饮食；", "bbox": [305, 510, 441, 525]},
	{"text": "2、适当增加运动；", "bbox": [304, 528, 460, 544]},
	{"text": "3、口服二甲双胍片，每日3次 每次0.5g；", "bbox": [304, 547, 670, 563]},
	{"text": "4、监测血糖；", "bbox": [304, 566, 420, 582]},
	{"text": "5、门诊随访；", "bbox": [304, 585, 420, 601]},
	{"text": "打印日期：2024-05-06 15:48:23", "bbox": [197, 888, 503, 904]},
	{"text": "医师：", "bbox": [727, 887, 775, 903]},
	{"text": "主治医师", "bbox": [788, 868, 868, 897]},
	{"text": "杨泽志", "bbox": [788, 902, 870, 933]}
]
2026-08-10 13:36:37,843 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=11.9s
2026-08-10 13:36:37,843 INFO     29 [qwen-vl-text] coord item[0]: text=哈尔滨美颐医院门诊单, bbox=[335, 64, 717, 93]
2026-08-10 13:36:37,843 INFO     29 [qwen-vl-text] coord item[1]: text=门诊号：102800000989, bbox=[212, 117, 405, 133]
2026-08-10 13:36:37,843 INFO     29 [qwen-vl-text] coord item[2]: text=诊疗号：000816012, bbox=[633, 116, 798, 131]
2026-08-10 13:36:37,843 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[211, 154, 257, 169]
2026-08-10 13:36:37,843 INFO     29 [qwen-vl-text] coord item[4]: text=性别：男, bbox=[432, 153, 507, 169]
2026-08-10 13:36:37,843 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：65岁, bbox=[653, 153, 752, 168]
2026-08-10 13:36:37,843 INFO     29 [qwen-vl-text] coord item[6]: text=接诊时间：2024-05-06 09:37:20, bbox=[211, 191, 500, 206]
2026-08-10 13:36:37,843 INFO     29 [qwen-vl-text] coord item[7]: text=接诊科室：门诊, bbox=[538, 190, 671, 205]
2026-08-10 13:36:37,843 INFO     29 [qwen-vl-text] coord item[8]: text=接诊医师：/, bbox=[711, 189, 818, 204]
2026-08-10 13:36:37,844 INFO     29 [qwen-vl-text] coord item[9]: text=临床诊断：2型糖尿病, bbox=[211, 228, 399, 244]
2026-08-10 13:36:37,844 INFO     29 [qwen-vl-text] coord item[10]: text=主诉：口干、多尿、多饮半月，无消瘦, bbox=[211, 265, 537, 280]
2026-08-10 13:36:37,844 INFO     29 [qwen-vl-text] coord item[11]: text=现病史：无诱因出现口干、多尿、多饮症状，来院检查, bbox=[210, 301, 673, 317]
2026-08-10 13:36:37,844 INFO     29 [qwen-vl-text] coord item[12]: text=既往病史：无, bbox=[210, 339, 326, 354]
2026-08-10 13:36:37,844 INFO     29 [qwen-vl-text] coord item[13]: text=过敏史：无, bbox=[209, 376, 326, 392]
2026-08-10 13:36:37,844 INFO     29 [qwen-vl-text] coord item[14]: text=体格检查：未检查, bbox=[208, 414, 365, 429]
2026-08-10 13:36:37,844 INFO     29 [qwen-vl-text] coord item[15]: text=辅助检查：已回报, bbox=[208, 452, 365, 468]
2026-08-10 13:36:37,844 INFO     29 [qwen-vl-text] coord item[16]: text=治疗建议：, bbox=[208, 490, 294, 506]
2026-08-10 13:36:37,844 INFO     29 [qwen-vl-text] coord item[17]: text=1、糖尿病饮食；, bbox=[305, 510, 441, 525]
2026-08-10 13:36:37,844 INFO     29 [qwen-vl-text] coord item[18]: text=2、适当增加运动；, bbox=[304, 528, 460, 544]
2026-08-10 13:36:37,844 INFO     29 [qwen-vl-text] coord item[19]: text=3、口服二甲双胍片，每日3次 每次0.5g；, bbox=[304, 547, 670, 563]
2026-08-10 13:36:37,844 INFO     29 [qwen-vl-text] coord item[20]: text=4、监测血糖；, bbox=[304, 566, 420, 582]
2026-08-10 13:36:37,844 INFO     29 [qwen-vl-text] coord item[21]: text=5、门诊随访；, bbox=[304, 585, 420, 601]
2026-08-10 13:36:37,844 INFO     29 [qwen-vl-text] coord item[22]: text=打印日期：2024-05-06 15:48:23, bbox=[197, 888, 503, 904]
2026-08-10 13:36:37,844 INFO     29 [qwen-vl-text] coord item[23]: text=医师：, bbox=[727, 887, 775, 903]
2026-08-10 13:36:37,844 INFO     29 [qwen-vl-text] coord item[24]: text=主治医师, bbox=[788, 868, 868, 897]
2026-08-10 13:36:37,844 INFO     29 [qwen-vl-text] coord item[25]: text=杨泽志, bbox=[788, 902, 870, 933]
2026-08-10 13:36:37,845 INFO     29 [qwen-vl-text] page=1 — 26/26 coords, api_time=11.9s
2026-08-10 13:36:37,845 INFO     29 [qwen-vl-text] new_positions (26):
[[1, 321.34875, 687.7822500000001, 81.792, 118.854], [1, 203.36100000000002, 388.49625000000003, 149.526, 169.974], [1, 607.20525, 765.4815, 148.248, 167.418], [1, 202.40175000000002, 246.52725, 196.812, 215.982], [1, 414.396, 486.33975000000004, 195.534, 215.982], [1, 626.39025, 721.356, 195.534, 214.704], [1, 202.40175000000002, 479.625, 244.098, 263.26800000000003], [1, 516.0765, 643.65675, 242.82, 261.99], [1, 682.02675, 784.6665, 241.542, 260.712], [1, 202.40175000000002, 382.74075, 291.384, 311.832], [1, 202.40175000000002, 515.11725, 338.67, 357.84000000000003], [1, 201.44250000000002, 645.57525, 384.678, 405.12600000000003], [1, 201.44250000000002, 312.7155, 433.242, 452.41200000000003], [1, 200.48325, 312.7155, 480.528, 500.976], [1, 199.524, 350.12625, 529.092, 548.2620000000001], [1, 199.524, 350.12625, 577.6560000000001, 598.104], [1, 199.524, 282.0195, 626.22, 646.668], [1, 292.57125, 423.02925000000005, 651.78, 670.95], [1, 291.612, 441.255, 674.784, 695.232], [1, 291.612, 642.6975, 699.066, 719.514], [1, 291.612, 402.88500000000005, 723.3480000000001, 743.796], [1, 291.612, 402.88500000000005, 747.63, 768.078], [1, 188.97225, 482.50275000000005, 1134.864, 1155.3120000000001], [1, 697.3747500000001, 743.41875, 1133.586, 1154.034], [1, 755.889, 832.629, 1109.304, 1146.366], [1, 755.889, 834.5475, 1152.756, 1192.374]]
2026-08-10 13:36:37,845 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=13.8s
2026-08-10 13:36:37,859 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 13:36:37,859 INFO     29 [Trace] task=4c58c278 | doc=LiJu(1)(1)哈大四.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "99 items", "markdown": "", "text": "", "name": "LiJu(1)(1)哈大四.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 4, \"chunks_Medication\": 1}"}
2026-08-10 13:36:37,860 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 13:36:37,860 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:36:37.860+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 52, "failed": 0, "current": {"4c58c27894c011f1bd9827cf206dfa2d": {"id": "4c58c27894c011f1bd9827cf206dfa2d", "doc_id": "4c2d3d1094c011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LiJu(1)(1)\u54c8\u5927\u56db.pdf", "type": "pdf", "location": "LiJu(1)(1)\u54c8\u5927\u56db.pdf", "size": 1923761, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368906074, "task_type": "dataflow", "root_trace_id": "4f4dfcf132bb46f882e4ea4e62b4012a", "root_traceparent": "00-4f4dfcf132bb46f882e4ea4e62b4012a-9654b1ff0cfeac68-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:36:37,866 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:36:37,867 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:36:37,867 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 13:36:37,867 INFO     29 [qwen-vl-text] positions(14): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:36:37,867 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [14]
2026-08-10 13:36:38,136 INFO     29 [qwen-vl-text] page=4, rect=959x1278, img=(2665x3550), dpi=200
2026-08-10 13:36:38,137 INFO     29 [qwen-vl-text] LLM extraction start, text_len=204
2026-08-10 13:36:38,138 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:38,138 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 68, \"bbox_end\": 81, \"encounter_dates\": [\"2024-11-08\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "哈尔滨康华大药房有限公\nNO.55550534536320004523\n日期: 2024/11/08 14:24:49\n会员:  销售: 04\n882457 盐酸二甲双胍缓释片\n规格 0.5gx30T 产地: 北京\n批号 288241049 效期 2027-1\n数量 20 单价 8.00\n金额合计: ￥160.00 元\n应收 实收\n优惠 找零\n付款方式: 01 现金】\n健康热线:\n药品是特殊商品售出不退不",
    "role": "user"
  }
]
2026-08-10 13:36:40,242 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:40,242 INFO     29 [qwen-vl-text] LLM output (len=419):
{
  "encounter_date": "2024-11-08",
  "pharmacy": "哈尔滨康华大药房有限公",
  "medications": [
    {
      "name": "盐酸二甲双胍缓释片",
      "specification": "0.5gx30T",
      "dosage": null,
      "quantity": 20,
      "unit_price": 8.00,
      "total_price": 160.00,
      "frequency": null,
      "route": null,
      "manufacturer": "北京",
      "approval_number": null
    }
  ],
  "payment_total": 160.00,
  "payment_method": "现金"
}
2026-08-10 13:36:40,242 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-11-08]
2026-08-10 13:36:40,247 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2476538, prompt_len=859
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共14行）
["哈尔滨康华大药房有限公", "NO.55550534536320004523", "日期: 2024/11/08 14:24:49", "会员:  销售: 04", "882457 盐酸二甲双胍缓释片", "规格 0.5gx30T 产地: 北京", "批号 288241049 效期 2027-1", "数量 20 单价 8.00", "金额合计: ￥160.00 元", "应收 实收", "优惠 找零", "付款方式: 01 现金】", "健康热线:", "药品是特殊商品售出不退不"]

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
2026-08-10 13:36:48,192 INFO     29 [qwen-vl-text] coord API raw response (len=835):
```json
[
	{"text": "哈尔滨康华大药房有限公", "bbox": [309, 260, 795, 298]},
	{"text": "NO.55550534536320004523", "bbox": [307, 301, 783, 333]},
	{"text": "日期: 2024/11/08 14:24:49", "bbox": [310, 337, 787, 375]},
	{"text": "会员:  销售: 04", "bbox": [309, 375, 719, 412]},
	{"text": "882457 盐酸二甲双胍缓释片", "bbox": [320, 432, 800, 466]},
	{"text": "规格 0.5gx30T 产地: 北京", "bbox": [321, 473, 800, 510]},
	{"text": "批号 288241049 效期 2027-1", "bbox": [320, 520, 802, 552]},
	{"text": "数量 20 单价 8.00", "bbox": [318, 564, 697, 598]},
	{"text": "金额合计: ￥160.00 元", "bbox": [303, 621, 750, 656]},
	{"text": "应收 实收", "bbox": [297, 664, 610, 698]},
	{"text": "优惠 找零", "bbox": [296, 706, 609, 740]},
	{"text": "付款方式: 01 现金】", "bbox": [295, 747, 668, 782]},
	{"text": "健康热线:", "bbox": [295, 790, 481, 825]},
	{"text": "药品是特殊商品售出不退不", "bbox": [294, 831, 803, 867]}
]
```
2026-08-10 13:36:48,192 INFO     29 [qwen-vl-text] coord API: raw_items=14, valid_items=14, elapsed=7.9s
2026-08-10 13:36:48,192 INFO     29 [qwen-vl-text] coord item[0]: text=哈尔滨康华大药房有限公, bbox=[309, 260, 795, 298]
2026-08-10 13:36:48,192 INFO     29 [qwen-vl-text] coord item[1]: text=NO.55550534536320004523, bbox=[307, 301, 783, 333]
2026-08-10 13:36:48,193 INFO     29 [qwen-vl-text] coord item[2]: text=日期: 2024/11/08 14:24:49, bbox=[310, 337, 787, 375]
2026-08-10 13:36:48,193 INFO     29 [qwen-vl-text] coord item[3]: text=会员:  销售: 04, bbox=[309, 375, 719, 412]
2026-08-10 13:36:48,193 INFO     29 [qwen-vl-text] coord item[4]: text=882457 盐酸二甲双胍缓释片, bbox=[320, 432, 800, 466]
2026-08-10 13:36:48,193 INFO     29 [qwen-vl-text] coord item[5]: text=规格 0.5gx30T 产地: 北京, bbox=[321, 473, 800, 510]
2026-08-10 13:36:48,193 INFO     29 [qwen-vl-text] coord item[6]: text=批号 288241049 效期 2027-1, bbox=[320, 520, 802, 552]
2026-08-10 13:36:48,193 INFO     29 [qwen-vl-text] coord item[7]: text=数量 20 单价 8.00, bbox=[318, 564, 697, 598]
2026-08-10 13:36:48,193 INFO     29 [qwen-vl-text] coord item[8]: text=金额合计: ￥160.00 元, bbox=[303, 621, 750, 656]
2026-08-10 13:36:48,193 INFO     29 [qwen-vl-text] coord item[9]: text=应收 实收, bbox=[297, 664, 610, 698]
2026-08-10 13:36:48,193 INFO     29 [qwen-vl-text] coord item[10]: text=优惠 找零, bbox=[296, 706, 609, 740]
2026-08-10 13:36:48,193 INFO     29 [qwen-vl-text] coord item[11]: text=付款方式: 01 现金】, bbox=[295, 747, 668, 782]
2026-08-10 13:36:48,193 INFO     29 [qwen-vl-text] coord item[12]: text=健康热线:, bbox=[295, 790, 481, 825]
2026-08-10 13:36:48,193 INFO     29 [qwen-vl-text] coord item[13]: text=药品是特殊商品售出不退不, bbox=[294, 831, 803, 867]
2026-08-10 13:36:48,194 INFO     29 [qwen-vl-text] page=4 — 14/14 coords, api_time=7.9s
2026-08-10 13:36:48,195 INFO     29 [qwen-vl-text] new_positions (14):
[[4, 296.40825, 762.60375, 332.28000000000003, 380.844], [4, 294.48975, 751.09275, 384.678, 425.574], [4, 297.3675, 754.92975, 430.68600000000004, 479.25], [4, 296.40825, 689.7007500000001, 479.25, 526.5360000000001], [4, 306.96000000000004, 767.4000000000001, 552.096, 595.548], [4, 307.91925000000003, 767.4000000000001, 604.494, 651.78], [4, 306.96000000000004, 769.3185000000001, 664.5600000000001, 705.456], [4, 305.04150000000004, 668.59725, 720.792, 764.244], [4, 290.65275, 719.4375, 793.638, 838.368], [4, 284.89725000000004, 585.1425, 848.592, 892.044], [4, 283.938, 584.18325, 902.268, 945.72], [4, 282.97875, 640.779, 954.666, 999.3960000000001], [4, 282.97875, 461.39925, 1009.62, 1054.35], [4, 282.0195, 770.2777500000001, 1062.018, 1108.026]]
2026-08-10 13:36:48,195 INFO     29 [qwen-vl-text] ═══ DONE ═══ 14 positions, pages=1, time=10.3s
2026-08-10 13:36:48,208 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 13:36:48,209 INFO     29 [Trace] task=4c58c278 | doc=LiJu(1)(1)哈大四.pdf | Extractor:Medication | outputs={"chunks": "1 items, types={'MedicationRecord': 1}", "html": "", "json": "99 items", "markdown": "", "text": "", "name": "LiJu(1)(1)哈大四.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 4, \"chunks_Medication\": 1}"}
2026-08-10 13:36:48,209 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 13:36:48,215 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:48,215 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:36:49,231 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:49,242 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 13:36:49,242 INFO     29 [Trace] task=4c58c278 | doc=LiJu(1)(1)哈大四.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "99 items", "markdown": "", "text": "", "name": "LiJu(1)(1)哈大四.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 4, \"chunks_Medication\": 1}"}
2026-08-10 13:36:49,242 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 13:36:49,249 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:49,249 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:36:49,912 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:49,918 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 13:36:49,918 INFO     29 [Trace] task=4c58c278 | doc=LiJu(1)(1)哈大四.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "99 items", "markdown": "", "text": "", "name": "LiJu(1)(1)哈大四.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 4, \"chunks_Medication\": 1}"}
2026-08-10 13:36:49,919 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 13:36:49,923 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:49,923 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:36:50,423 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:50,429 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 13:36:50,430 INFO     29 [Trace] task=4c58c278 | doc=LiJu(1)(1)哈大四.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "99 items", "markdown": "", "text": "", "name": "LiJu(1)(1)哈大四.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 4, \"chunks_Medication\": 1}"}
2026-08-10 13:36:50,430 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 13:36:50,435 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:50,435 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:36:51,530 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:51,542 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 13:36:51,542 INFO     29 [Trace] task=4c58c278 | doc=LiJu(1)(1)哈大四.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "99 items", "markdown": "", "text": "", "name": "LiJu(1)(1)哈大四.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 4, \"chunks_Medication\": 1}"}
2026-08-10 13:36:51,542 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 13:36:51,552 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:51,552 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:36:52,022 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:36:52,033 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 13:36:52,033 INFO     29 [Trace] task=4c58c278 | doc=LiJu(1)(1)哈大四.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "99 items", "markdown": "", "text": "", "name": "LiJu(1)(1)哈大四.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 4, \"chunks_Medication\": 1}"}
2026-08-10 13:36:52,033 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 13:36:52,034 INFO     29 [ChunkMerger] Merged 6 chunks from 9 sources: {'Extractor:LabExam': 4, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 6 noise chunks)
2026-08-10 13:36:52,044 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 13:36:52,044 INFO     29 [Trace] task=4c58c278 | doc=LiJu(1)(1)哈大四.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "6 items, types={'LabReport': 4, 'OutpatientRecord': 1, 'MedicationRecord': 1}", "name": "LiJu(1)(1)哈大四.pdf"}
2026-08-10 13:36:52,044 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 13:36:52,070 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786368907528, 'update_date': datetime.datetime(2026, 8, 10, 13, 35, 7), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1042886, 'status': '1'}
2026-08-10 13:36:52,282 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   糖化血红蛋白  HbA1c  8.3  %  4.1--6.1  True   
---
   糖化血红蛋白  None  7.62  None  3.8--5.8  True   
---
   糖化血红蛋白  None  8.55  %  3.8--5.8  True   
---
   *葡萄糖  GLU  9.71  mmol/L  3.9--6.1  True   
---
哈尔滨美颐医院门诊单
门诊号：102800000989
诊疗号：000816012
姓名：
性别：男
年龄：65岁
接诊时间：2024-05-06 09:37:20
接诊科室：门诊
接诊医师：/
临床诊断：2型糖尿病
主诉：口干、多尿、多饮半月，无消瘦
现病史：无诱因出现口干、多尿、多饮症状，来院检查
既往病史：无
过敏史：无
体格检查：未检查
辅助检查：已回报
治疗建议：
1、糖尿病饮食；
2、适当增加运动；
3、口服二甲双胍片，每日3次 每次0.5g；
4、监测血糖；
5、门诊随访；
打印日期：2024-05-06 15:48:23
医师：
主治医师
杨泽志
---
哈尔滨康华大药房有限公
NO.55550534536320004523
日期: 2024/11/08 14:24:49
会员:  销售: 04
882457 盐酸二甲双胍缓释片
规格 0.5gx30T 产地: 北京
批号 288241049 效期 2027-1
数量 20 单价 8.00
金额合计: ￥160.00 元
应收 实收
优惠 找零
付款方式: 01 现金】
健康热线:
药品是特殊商品售出不退不
2026-08-10 13:36:52,547 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 13:36:52,547 INFO     29 [Trace] task=4c58c278 | doc=LiJu(1)(1)哈大四.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "6 items, types={'LabReport': 4, 'OutpatientRecord': 1, 'MedicationRecord': 1}", "name": "LiJu(1)(1)哈大四.pdf", "embedding_token_consumption": 553}
2026-08-10 13:36:52,547 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 13:36:52,750 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 13:36:52,750 INFO     29 [Trace] task=4c58c278 | doc=LiJu(1)(1)哈大四.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":6,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 13:36:52,753 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(3, 299, 434, 437, 460) row[-1]=(3, 299, 434, 437, 460)
2026-08-10 13:36:52,753 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(4, 299, 619, 499, 551) row[-1]=(4, 299, 619, 499, 551)
2026-08-10 13:36:52,753 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(6, 268, 342, 225, 241) row[-1]=(6, 268, 342, 225, 241)
2026-08-10 13:36:52,753 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(7, 177, 223, 210, 223) row[-1]=(7, 177, 223, 210, 223)
2026-08-10 13:36:52,753 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:36:52,753 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:36:52,757 INFO     29 set_progress(4c58c27894c011f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 13:36:52 [DOC Engine]:
Start to index...
2026-08-10 13:36:52,783 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.016s]
2026-08-10 13:36:52,787 INFO     29 set_progress(4c58c27894c011f1bd9827cf206dfa2d), progress: 0.8166666666666668, progress_msg: 
2026-08-10 13:36:52,800 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.007s]
2026-08-10 13:36:52,807 INFO     29 set_progress(4c58c27894c011f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 13:36:52 Indexing done (0.05s). Task done (100.84s)
2026-08-10 13:36:52,810 INFO     29 [Done], chunks(6), token(553), elapsed:100.84
2026-08-10 13:36:52,876 INFO     29 handle_task done for task {"id": "4c58c27894c011f1bd9827cf206dfa2d", "doc_id": "4c2d3d1094c011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LiJu(1)(1)\u54c8\u5927\u56db.pdf", "type": "pdf", "location": "LiJu(1)(1)\u54c8\u5927\u56db.pdf", "size": 1923761, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786368906074, "task_type": "dataflow", "root_trace_id": "4f4dfcf132bb46f882e4ea4e62b4012a", "root_traceparent": "00-4f4dfcf132bb46f882e4ea4e62b4012a-9654b1ff0cfeac68-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
