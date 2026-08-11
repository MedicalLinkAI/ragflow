# 基准结果：XJYo-糖尿病-哈大四.pdf

## 基本信息

- 文件：`XJYo-糖尿病-哈大四.pdf`
- 大小：1624.0 KB
- PDF 总页数：9
- doc_id：`eddf381a94c111f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T21:46:45  完成时间：2026-08-10T21:49:06  耗时：140.8s
- progress_msg：`13:49:00 Indexing done (0.05s). Task done (126.72s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | deefd29c | 1 | 2-2 | 哈尔滨同迈综合门诊 姓名: 就诊日期: 2021-09-12 就诊号: 2021 |
| 2 | 6454dac9 | 1 | 5-5 | 哈尔滨体诚人药房有限公司 (P23010122054)销售单 号12875 日期 |
| 3 | 18cbb394 | 1 | 6-6 | 哈尔滨泽福大药房有限 公司销售单据 NO.8555800415612312005 |
| 4 | c997f23b | 1 | 3-3 | <table><tr><td>糖化血红蛋白</td><td>None</td>< |
| 5 | 651e1ce0 | 1 | 7-7 | <table><tr><td>糖化血红蛋白LA1c</td><td>HbA1c< |
| 6 | 87956bb3 | 1 | 8-8 | <table><tr><td>糖化血红蛋白A1</td><td>None</td |
| 7 | cb4995fe | 1 | 9-9 | <table><tr><td>葡萄糖（已糖激酶法）</td><td>None</ |
| 8 | 798bbe5c | 1 | 4-4 | <table><tr><td>糖化血红蛋白</td><td>None</td>< |

- chunks 总数：8
- 各 chunk 页数合计（含跨页重复）：8
- 页码并集：`[2, 3, 4, 5, 6, 7, 8, 9]`
- 覆盖页数：8 / 9；缺失页：`[1]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：❌ 未完全覆盖：覆盖 8/9 页，缺失 [1]，超范围 []**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 1 | 0 | 1 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 2 | 2 | 2 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 0 | 1 | 0 | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 5 | 0 | 5 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 1, "LabReport": 5, "MedicationRecord": 2}`
- ChunkMerger：`{"found": true, "merged": 8, "sources": 9, "stats": {"Extractor:LabExam": 5, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 2, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 13:48:59,886 INFO     29 [ChunkMerger] Merged 8 chunks from 9 sources: {'Extractor:LabExam': 5, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 2, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 13:46:47,690 INFO     29 handle_task begin for task {"id": "ee0bc9a294c111f1bd9827cf206dfa2d", "doc_id": "eddf381a94c111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "XJYo-\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "type": "pdf", "location": "XJYo-\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "size": 1663007, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786369606857, "task_type": "dataflow", "root_trace_id": "fca2d36450a74bdfa74068ff62a9c874", "root_traceparent": "00-fca2d36450a74bdfa74068ff62a9c874-672b5c2f105370f4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 13:46:47,890 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 13:46:48,000 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 13:46:48,009 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:46:48,010 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 13:46:48,010 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 13:46:48,014 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 13:46:48,014 INFO     29 ============================================================
2026-08-10 13:46:48,014 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 13:46:48,014 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 13:46:48,014 INFO     29 ============================================================
2026-08-10 13:46:48,014 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 13:46:48,014 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 13:46:48,015 INFO     29 No torch found.
2026-08-10 13:46:48,895 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=9
2026-08-10 13:46:49,020 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=241212, prompt_len=764
2026-08-10 13:46:52,416 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-05-08"}
```
2026-08-10 13:46:52,417 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2025-05-08
2026-08-10 13:46:52,427 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=241212, prompt_len=401
2026-08-10 13:46:53,952 INFO     29 [qwen-vl-parser] text API response (len=227):
["受试者推荐情况汇总", "单药-联合？：联合", "姓名缩写：XJYO", "年龄：52", "性别：男", "身高：178cm", "体重：90kg", "BMI：28.4", "首次诊断T2DM时间：2013", "最近血糖&糖化检测结果：8", "糖化-日期：2025.5.8", "遗传病学（乙肝、丙肝、梅毒、艾滋", "）是否阳性：否", "既往疾病：无", "推荐的中心：哈大四", "居住地：哈尔滨", "提报时间：2025.5.8"]
2026-08-10 13:46:53,952 INFO     29 [qwen-vl-parser] page=1 text: 17 lines (bbox 0-16)
2026-08-10 13:46:53,952 INFO     29 [qwen-vl-parser] page=1 text: 17 sections
2026-08-10 13:46:54,206 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=885200, prompt_len=764
2026-08-10 13:46:57,536 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:46:57,537 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 13:46:57,542 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=885200, prompt_len=401
2026-08-10 13:46:59,784 INFO     29 [qwen-vl-parser] text API response (len=338):
["哈尔滨同迈综合门诊", "姓名:", "就诊日期: 2021-09-12", "就诊号: 20210912003", "姓名:", "年龄: 48岁", "性别: 男", "地址:", "药物过敏史:", "主诉: 糖尿病患者体检", "现病史: 患者自述确诊2型糖尿病8年余, 近段时间, 血糖升高, 口服降", "糖灵片, 降糖效果甚微, 自测指尖血糖14.2mmol/L, 来院诊治", "既往史: 2型糖尿病", "查体: T36.5℃ BP135-90mmHg -", "辅助检查: 已回报", "临床诊断: 2型糖尿病", "治疗意见: 盐酸二甲双胍片 每日3次 每次0.5g 随餐口服", "半月后复诊", "医师(签字):", "主治医师", "赵东强"]
2026-08-10 13:46:59,784 INFO     29 [qwen-vl-parser] page=2 text: 21 lines (bbox 17-37)
2026-08-10 13:46:59,784 INFO     29 [qwen-vl-parser] page=2 text: 21 sections
2026-08-10 13:46:59,936 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=546537, prompt_len=764
2026-08-10 13:47:01,764 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2021-09-12"
}
```
2026-08-10 13:47:01,764 INFO     29 [qwen-vl-parser] page=3 classify=table report_date=2021-09-12
2026-08-10 13:47:01,773 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=546537, prompt_len=756
2026-08-10 13:47:02,674 INFO     29 [qwen-vl-parser] table API response (len=128):
\begin{tabular}{ccccccc}
\hline
序号 & 项目 & 结果 & 状态 & 单位 & 参考值 \\
\hline
1 & 糖化血红蛋白 & 9.46 & ↑ & \% & 4--6 \\
\hline
\end{tabular}
2026-08-10 13:47:02,675 INFO     29 [qwen-vl-parser] page=3 table: 8 LaTeX lines (bbox 38-45)
2026-08-10 13:47:02,675 INFO     29 [qwen-vl-parser] page=3 table: 8 sections
2026-08-10 13:47:02,824 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=478180, prompt_len=764
2026-08-10 13:47:06,009 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2024-09-25"
}
```
2026-08-10 13:47:06,010 INFO     29 [qwen-vl-parser] page=4 classify=table report_date=2024-09-25
2026-08-10 13:47:06,019 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=478180, prompt_len=756
2026-08-10 13:47:06,897 INFO     29 [qwen-vl-parser] table API response (len=127):
\begin{tabular}{cccccccc}
\hline
序号 & 项目 & 结果 & 状态 & 单位 & 参考值 \\
\hline
1 & 糖化血红蛋白 & 8.0 & ↑ & \% & 4—6 \\
\hline
\end{tabular}
2026-08-10 13:47:06,898 INFO     29 [qwen-vl-parser] page=4 table: 8 LaTeX lines (bbox 46-53)
2026-08-10 13:47:06,898 INFO     29 [qwen-vl-parser] page=4 table: 8 sections
2026-08-10 13:47:07,127 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=928311, prompt_len=764
2026-08-10 13:47:08,772 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:47:08,772 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 13:47:08,783 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=928311, prompt_len=401
2026-08-10 13:47:09,058 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:47:09.056+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 58, "failed": 0, "current": {"ee0bc9a294c111f1bd9827cf206dfa2d": {"id": "ee0bc9a294c111f1bd9827cf206dfa2d", "doc_id": "eddf381a94c111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "XJYo-\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "type": "pdf", "location": "XJYo-\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "size": 1663007, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786369606857, "task_type": "dataflow", "root_trace_id": "fca2d36450a74bdfa74068ff62a9c874", "root_traceparent": "00-fca2d36450a74bdfa74068ff62a9c874-672b5c2f105370f4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:47:10,678 INFO     29 [qwen-vl-parser] text API response (len=274):
["哈尔滨体诚人药房有限公司", "(P23010122054)销售单", "号12875 日期2024-08-22", "药师：高芳 代码Y2301240061", "品名 盐酸二甲双胍片", "国家编码", "单价6.00 数量15.0 金额90.00", "单位 盒 规格0.25g/24T/2板", "批号22110778 效期2025-11-1", "产地：北京市小康药业有限公", "销售员：05", "合计：90.00 折前金额：90.0", "实收：90.00", "积分 0522", "付款方式：现金01#", "健康热线："]
2026-08-10 13:47:10,679 INFO     29 [qwen-vl-parser] page=5 text: 16 lines (bbox 54-69)
2026-08-10 13:47:10,679 INFO     29 [qwen-vl-parser] page=5 text: 16 sections
2026-08-10 13:47:11,026 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1559104, prompt_len=764
2026-08-10 13:47:14,452 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-12-19"}
```
2026-08-10 13:47:14,452 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=2024-12-19
2026-08-10 13:47:14,461 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1559104, prompt_len=401
2026-08-10 13:47:17,660 INFO     29 [qwen-vl-parser] text API response (len=329):
["哈尔滨泽福大药房有限", "公司销售单据", "NO.8555800415612312005", "2024-12-19 19:10:28", "会员 销售员:张子欣", "01 020749 盐酸二甲双胍片", "规格 0.25gX24片/2板 单位:1", "产地 北京市永康药业有限公司", "批号 23082416 效期 2026/0", "数量:15 单价:7.00", "总金额:￥105.00 元", "应收:￥105.00 实收:￥100.00", "优惠:￥5.00 找零:0.00", "付款方式:现金01#", "健康热线:", "地址:", "药品是特殊商品,一经售出不退", "如需开具发票者,持销售小票1", "到店开具。"]
2026-08-10 13:47:17,661 INFO     29 [qwen-vl-parser] page=6 text: 19 lines (bbox 70-88)
2026-08-10 13:47:17,661 INFO     29 [qwen-vl-parser] page=6 text: 19 sections
2026-08-10 13:47:17,884 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=802739, prompt_len=764
2026-08-10 13:47:23,798 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-02-19"
}
```
2026-08-10 13:47:23,798 INFO     29 [qwen-vl-parser] page=7 classify=table report_date=2025-02-19
2026-08-10 13:47:23,806 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=802739, prompt_len=756
2026-08-10 13:47:24,809 INFO     29 [qwen-vl-parser] table API response (len=88):
\begin{tabular}{cc}
\hline
名称 & 结果 \\
\hline
糖化血红蛋白LA1c & "7.50" \\
\hline
\end{tabular}
2026-08-10 13:47:24,812 INFO     29 [qwen-vl-parser] page=7 table: 8 LaTeX lines (bbox 89-96)
2026-08-10 13:47:24,812 INFO     29 [qwen-vl-parser] page=7 table: 8 sections
2026-08-10 13:47:25,062 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=869493, prompt_len=764
2026-08-10 13:47:30,947 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-05-08"}
```
2026-08-10 13:47:30,947 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=2025-05-08
2026-08-10 13:47:30,954 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=869493, prompt_len=401
2026-08-10 13:47:32,565 INFO     29 [qwen-vl-parser] text API response (len=198):
["15:37", "报告查询", "此报告仅对送检标本负责,结果供送检医生参考。", "糖化血红蛋白测定", "患者姓名 **有(男52)", "患者编号 就诊卡10****6151", "标本编号 4619222", "名称", "结果(参考值)", "★*糖化血红蛋白A1", "↑8%(4--6)", "报告时间 2025-05-08 10:04:30", "报告编号 4619222"]
2026-08-10 13:47:32,566 INFO     29 [qwen-vl-parser] page=8 text: 13 lines (bbox 97-109)
2026-08-10 13:47:32,566 INFO     29 [qwen-vl-parser] page=8 text: 13 sections
2026-08-10 13:47:32,801 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=798592, prompt_len=764
2026-08-10 13:47:40,532 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2025-05-08"}
```
2026-08-10 13:47:40,533 INFO     29 [qwen-vl-parser] page=9 classify=table report_date=2025-05-08
2026-08-10 13:47:40,555 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=798592, prompt_len=756
2026-08-10 13:47:40,620 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:47:40.619+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 58, "failed": 0, "current": {"ee0bc9a294c111f1bd9827cf206dfa2d": {"id": "ee0bc9a294c111f1bd9827cf206dfa2d", "doc_id": "eddf381a94c111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "XJYo-\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "type": "pdf", "location": "XJYo-\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "size": 1663007, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786369606857, "task_type": "dataflow", "root_trace_id": "fca2d36450a74bdfa74068ff62a9c874", "root_traceparent": "00-fca2d36450a74bdfa74068ff62a9c874-672b5c2f105370f4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:47:41,653 INFO     29 [qwen-vl-parser] table API response (len=115):
\begin{tabular}{ccc}
\hline
名称 & 结果(参考值) \\
\hline
★葡萄糖（已糖激酶法） & ↑ 14.46 mmol/L (3.6--6.11) \\
\hline
\end{tabular}
2026-08-10 13:47:41,655 INFO     29 [qwen-vl-parser] page=9 table: 8 LaTeX lines (bbox 110-117)
2026-08-10 13:47:41,656 INFO     29 [qwen-vl-parser] page=9 table: 8 sections
2026-08-10 13:47:41,656 INFO     29 [qwen-vl-parser] parse_pdf done: 118 sections from 9 pages.
2026-08-10 13:47:41,667 INFO     29 Close text detector.
2026-08-10 13:47:42,122 INFO     29 Close text recognizer.
2026-08-10 13:47:42,500 INFO     29 Close recognizer.
2026-08-10 13:47:42,918 INFO     29 Close recognizer.
2026-08-10 13:47:43,890 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 13:47:43,890 INFO     29 [Trace] task=ee0bc9a2 | doc=XJYo-糖尿病-哈大四.pdf | Parser:MedLink | outputs={"html": "", "json": "118 items", "markdown": "", "text": "", "name": "XJYo-糖尿病-哈大四.pdf", "output_format": "json"}
2026-08-10 13:47:43,891 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 13:47:43,910 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:47:43,910 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 受试者推荐情况汇总\n[BBOX-1] 单药-联合？：联合\n[BBOX-2] 姓名缩写：XJYO\n[BBOX-3] 年龄：52\n[BBOX-4] 性别：男\n[BBOX-5] 身高：178cm\n[BBOX-6] 体重：90kg\n[BBOX-7] BMI：28.4\n[BBOX-8] 首次诊断T2DM时间：2013\n[BBOX-9] 最近血糖&糖化检测结果：8\n[BBOX-10] 糖化-日期：2025.5.8\n[BBOX-11] 遗传病学（乙肝、丙肝、梅毒、艾滋\n[BBOX-12] ）是否阳性：否\n[BBOX-13] 既往疾病：无\n[BBOX-14] 推荐的中心：哈大四\n[BBOX-15] 居住地：哈尔滨\n[BBOX-16] 提报时间：2025.5.8\n[BBOX-17] 哈尔滨同迈综合门诊\n[BBOX-18] 姓名:\n[BBOX-19] 就诊日期: 2021-09-12\n[BBOX-20] 就诊号: 20210912003\n[BBOX-21] 姓名:\n[BBOX-22] 年龄: 48岁\n[BBOX-23] 性别: 男\n[BBOX-24] 地址:\n[BBOX-25] 药物过敏史:\n[BBOX-26] 主诉: 糖尿病患者体检\n[BBOX-27] 现病史: 患者自述确诊2型糖尿病8年余, 近段时间, 血糖升高, 口服降\n[BBOX-28] 糖灵片, 降糖效果甚微, 自测指尖血糖14.2mmol/L, 来院诊治\n[BBOX-29] 既往史: 2型糖尿病\n[BBOX-30] 查体: T36.5℃ BP135-90mmHg -\n[BBOX-31] 辅助检查: 已回报\n[BBOX-32] 临床诊断: 2型糖尿病\n[BBOX-33] 治疗意见: 盐酸二甲双胍片 每日3次 每次0.5g 随餐口服\n[BBOX-34] 半月后复诊\n[BBOX-35] 医师(签字):\n[BBOX-36] 主治医师\n[BBOX-37] 赵东强\n[BBOX-38] \\begin{tabular}{ccccccc}\n[BBOX-39] 报告时间: 2021-09-12\n[BBOX-40] \\hline\n[BBOX-41] 序号 & 项目 & 结果 & 状态 & 单位 & 参考值 \\\\\n[BBOX-42] \\hline\n[BBOX-43] 1 & 糖化血红蛋白 & 9.46 & ↑ & \\% & 4--6 \\\\\n[BBOX-44] \\hline\n[BBOX-45] \\end{tabular}\n[BBOX-46] \\begin{tabular}{cccccccc}\n[BBOX-47] 报告时间: 2024-09-25\n[BBOX-48] \\hline\n[BBOX-49] 序号 & 项目 & 结果 & 状态 & 单位 & 参考值 \\\\\n[BBOX-50] \\hline\n[BBOX-51] 1 & 糖化血红蛋白 & 8.0 & ↑ & \\% & 4—6 \\\\\n[BBOX-52] \\hline\n[BBOX-53] \\end{tabular}\n[BBOX-54] 哈尔滨体诚人药房有限公司\n[BBOX-55] (P23010122054)销售单\n[BBOX-56] 号12875 日期2024-08-22\n[BBOX-57] 药师：高芳 代码Y2301240061\n[BBOX-58] 品名 盐酸二甲双胍片\n[BBOX-59] 国家编码\n[BBOX-60] 单价6.00 数量15.0 金额90.00\n[BBOX-61] 单位 盒 规格0.25g/24T/2板\n[BBOX-62] 批号22110778 效期2025-11-1\n[BBOX-63] 产地：北京市小康药业有限公\n[BBOX-64] 销售员：05\n[BBOX-65] 合计：90.00 折前金额：90.0\n[BBOX-66] 实收：90.00\n[BBOX-67] 积分 0522\n[BBOX-68] 付款方式：现金01#\n[BBOX-69] 健康热线：\n[BBOX-70] 哈尔滨泽福大药房有限\n[BBOX-71] 公司销售单据\n[BBOX-72] NO.8555800415612312005\n[BBOX-73] 2024-12-19 19:10:28\n[BBOX-74] 会员 销售员:张子欣\n[BBOX-75] 01 020749 盐酸二甲双胍片\n[BBOX-76] 规格 0.25gX24片/2板 单位:1\n[BBOX-77] 产地 北京市永康药业有限公司\n[BBOX-78] 批号 23082416 效期 2026/0\n[BBOX-79] 数量:15 单价:7.00\n[BBOX-80] 总金额:￥105.00 元\n[BBOX-81] 应收:￥105.00 实收:￥100.00\n[BBOX-82] 优惠:￥5.00 找零:0.00\n[BBOX-83] 付款方式:现金01#\n[BBOX-84] 健康热线:\n[BBOX-85] 地址:\n[BBOX-86] 药品是特殊商品,一经售出不退\n[BBOX-87] 如需开具发票者,持销售小票1\n[BBOX-88] 到店开具。\n[BBOX-89] \\begin{tabular}{cc}\n[BBOX-90] 报告时间: 2025-02-19\n[BBOX-91] \\hline\n[BBOX-92] 名称 & 结果 \\\\\n[BBOX-93] \\hline\n[BBOX-94] 糖化血红蛋白LA1c & \"7.50\" \\\\\n[BBOX-95] \\hline\n[BBOX-96] \\end{tabular}\n[BBOX-97] 15:37\n[BBOX-98] 报告查询\n[BBOX-99] 此报告仅对送检标本负责,结果供送检医生参考。\n[BBOX-100] 糖化血红蛋白测定\n[BBOX-101] 患者姓名 **有(男52)\n[BBOX-102] 患者编号 就诊卡10****6151\n[BBOX-103] 标本编号 4619222\n[BBOX-104] 名称\n[BBOX-105] 结果(参考值)\n[BBOX-106] ★*糖化血红蛋白A1\n[BBOX-107] ↑8%(4--6)\n[BBOX-108] 报告时间 2025-05-08 10:04:30\n[BBOX-109] 报告编号 4619222\n[BBOX-110] \\begin{tabular}{ccc}\n[BBOX-111] 报告时间: 2025-05-08\n[BBOX-112] \\hline\n[BBOX-113] 名称 & 结果(参考值) \\\\\n[BBOX-114] \\hline\n[BBOX-115] ★葡萄糖（已糖激酶法） & ↑ 14.46 mmol/L (3.6--6.11) \\\\\n[BBOX-116] \\hline\n[BBOX-117] \\end{tabular}"
  }
]
2026-08-10 13:47:50,478 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:47:50,492 INFO     29 [SmartSplitter] SmartSplitter done: 8 chunks from 8 LLM segments (all bbox_id). Types: {'OutpatientRecord': 1, 'LabReport': 5, 'MedicationRecord': 2}
2026-08-10 13:47:50,499 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 13:47:50,499 INFO     29 [Trace] task=ee0bc9a2 | doc=XJYo-糖尿病-哈大四.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "118 items", "markdown": "", "text": "", "name": "XJYo-糖尿病-哈大四.pdf", "output_format": "chunks", "chunks": "8 items, types={'OutpatientRecord': 1, 'LabReport': 5, 'MedicationRecord': 2}"}
2026-08-10 13:47:50,500 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 13:47:50,500 INFO     29 [ChunkRouter] Routed 8 chunks into 3 groups: {'chunks_Clinical': 1, 'chunks_LabExam': 5, 'chunks_Medication': 2}
2026-08-10 13:47:50,508 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 13:47:50,508 INFO     29 [Trace] task=ee0bc9a2 | doc=XJYo-糖尿病-哈大四.pdf | ChunkRouter:Router | outputs={"html": "", "json": "118 items", "markdown": "", "text": "", "name": "XJYo-糖尿病-哈大四.pdf", "output_format": "chunks", "chunks": "8 items, types={'OutpatientRecord': 1, 'LabReport': 5, 'MedicationRecord': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 5, \"chunks_Medication\": 2}"}
2026-08-10 13:47:50,508 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 13:47:50,512 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:47:50,513 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:47:50,513 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[2]
2026-08-10 13:47:50,513 INFO     29 [qwen-vl-table] positions ： [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:47:50,642 INFO     29 [qwen-vl-table] page=2, rect=608x1080, img=(1688x3000)
2026-08-10 13:47:50,642 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:47:50,643 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 38, \"bbox_end\": 45, \"encounter_dates\": [\"2021-09-12\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccc}\n报告时间: 2021-09-12\n\\hline\n序号 & 项目 & 结果 & 状态 & 单位 & 参考值 \\\\\n\\hline\n1 & 糖化血红蛋白 & 9.46 & ↑ & \\% & 4--6 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:47:51,827 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:47:51,827 INFO     29 [qwen-vl-table] page=2 LLM output (len=210):
{
  "report_date": "2021-09-12",
  "items": [
    {
      "name": "糖化血红蛋白",
      "item_code": null,
      "value": "9.46",
      "unit": "%",
      "reference_range": "4--6",
      "abnormal": true
    }
  ]
}
2026-08-10 13:47:51,827 INFO     29 [qwen-vl-table] coord grouping: {2: 1}
2026-08-10 13:47:51,829 INFO     29 [qwen-vl-table] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=712135, prompt_len=513
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
2026-08-10 13:47:53,642 INFO     29 [qwen-vl-table] coord API raw response (len=64):
```json
[
	{"text": "糖化血红蛋白", "bbox": [98, 323, 237, 338]}
]
```
2026-08-10 13:47:53,642 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=1.8s
2026-08-10 13:47:53,642 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白, bbox=[98, 323, 237, 338]
2026-08-10 13:47:53,642 INFO     29 [qwen-vl-table] page=2 coord: matched 1/1, time=1.8s
2026-08-10 13:47:53,642 INFO     29 [qwen-vl-table] new_positions (1):
[[3, 59.535000000000004, 143.97750000000002, 348.84000000000003, 365.04]]
2026-08-10 13:47:53,642 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=3.1s
2026-08-10 13:47:53,643 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:47:53,644 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:47:53,644 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[3]
2026-08-10 13:47:53,644 INFO     29 [qwen-vl-table] positions ： [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:47:53,768 INFO     29 [qwen-vl-table] page=3, rect=608x1080, img=(1688x3000)
2026-08-10 13:47:53,768 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:47:53,768 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 46, \"bbox_end\": 53, \"encounter_dates\": [\"2024-09-25\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccccccc}\n报告时间: 2024-09-25\n\\hline\n序号 & 项目 & 结果 & 状态 & 单位 & 参考值 \\\\\n\\hline\n1 & 糖化血红蛋白 & 8.0 & ↑ & \\% & 4—6 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:47:54,880 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:47:54,880 INFO     29 [qwen-vl-table] page=3 LLM output (len=208):
{
  "report_date": "2024-09-25",
  "items": [
    {
      "name": "糖化血红蛋白",
      "item_code": null,
      "value": "8.0",
      "unit": "%",
      "reference_range": "4—6",
      "abnormal": true
    }
  ]
}
2026-08-10 13:47:54,880 INFO     29 [qwen-vl-table] coord grouping: {3: 1}
2026-08-10 13:47:54,881 INFO     29 [qwen-vl-table] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=626050, prompt_len=513
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
2026-08-10 13:47:56,784 INFO     29 [qwen-vl-table] coord API raw response (len=65):
```json
[
	{"text": "糖化血红蛋白", "bbox": [115, 254, 255, 269]}
]
```
2026-08-10 13:47:56,784 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=1.9s
2026-08-10 13:47:56,784 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白, bbox=[115, 254, 255, 269]
2026-08-10 13:47:56,784 INFO     29 [qwen-vl-table] page=3 coord: matched 1/1, time=1.9s
2026-08-10 13:47:56,785 INFO     29 [qwen-vl-table] new_positions (1):
[[4, 69.86250000000001, 154.91250000000002, 274.32, 290.52000000000004]]
2026-08-10 13:47:56,785 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=3.1s
2026-08-10 13:47:56,786 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:47:56,788 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:47:56,788 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[6]
2026-08-10 13:47:56,788 INFO     29 [qwen-vl-table] positions ： [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:47:57,023 INFO     29 [qwen-vl-table] page=6, rect=932x2016, img=(2588x5600)
2026-08-10 13:47:57,024 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:47:57,024 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 89, \"bbox_end\": 96, \"encounter_dates\": [\"2025-02-19\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cc}\n报告时间: 2025-02-19\n\\hline\n名称 & 结果 \\\\\n\\hline\n糖化血红蛋白LA1c & \"7.50\" \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:47:58,150 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:47:58,150 INFO     29 [qwen-vl-table] page=6 LLM output (len=217):
{
  "report_date": "2025-02-19",
  "items": [
    {
      "name": "糖化血红蛋白LA1c",
      "item_code": "HbA1c",
      "value": "7.50",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 13:47:58,150 INFO     29 [qwen-vl-table] coord grouping: {6: 1}
2026-08-10 13:47:58,151 INFO     29 [qwen-vl-table] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=770428, prompt_len=517
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
糖化血红蛋白LA1c

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
2026-08-10 13:48:04,332 INFO     29 [qwen-vl-table] coord API raw response (len=68):
```json
[
	{"text": "糖化血红蛋白LA1c", "bbox": [47, 925, 347, 947]}
]
```
2026-08-10 13:48:04,332 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=6.2s
2026-08-10 13:48:04,332 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白LA1c, bbox=[47, 925, 347, 947]
2026-08-10 13:48:04,333 INFO     29 [qwen-vl-table] page=6 coord: matched 1/1, time=6.2s
2026-08-10 13:48:04,333 INFO     29 [qwen-vl-table] new_positions (1):
[[7, 43.780499999999996, 323.2305, 1864.8, 1909.152]]
2026-08-10 13:48:04,333 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=7.5s
2026-08-10 13:48:04,335 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:48:04,337 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:48:04,337 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[7]
2026-08-10 13:48:04,337 INFO     29 [qwen-vl-table] positions ： [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:48:04,620 INFO     29 [qwen-vl-table] page=7, rect=930x2015, img=(2583x5599)
2026-08-10 13:48:04,620 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:04,620 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 97, \"bbox_end\": 109, \"encounter_dates\": [\"2025-05-08\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "15:37\n报告查询\n此报告仅对送检标本负责,结果供送检医生参考。\n糖化血红蛋白测定\n患者姓名 **有(男52)\n患者编号 就诊卡10****6151\n标本编号 4619222\n名称\n结果(参考值)\n★*糖化血红蛋白A1\n↑8%(4--6)\n报告时间 2025-05-08 10:04:30\n报告编号 4619222",
    "role": "user"
  }
]
2026-08-10 13:48:06,708 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:06,708 INFO     29 [qwen-vl-table] page=7 LLM output (len=210):
{
  "report_date": "2025-05-08",
  "items": [
    {
      "name": "糖化血红蛋白A1",
      "item_code": null,
      "value": "8%",
      "unit": "%",
      "reference_range": "4--6",
      "abnormal": true
    }
  ]
}
2026-08-10 13:48:06,708 INFO     29 [qwen-vl-table] coord grouping: {7: 1}
2026-08-10 13:48:06,710 INFO     29 [qwen-vl-table] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1156715, prompt_len=515
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
糖化血红蛋白A1

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
2026-08-10 13:48:14,232 INFO     29 [qwen-vl-table] coord API raw response (len=67):
```json
[
	{"text": "糖化血红蛋白A1", "bbox": [142, 365, 360, 381]}
]
```
2026-08-10 13:48:14,232 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=7.5s
2026-08-10 13:48:14,232 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白A1, bbox=[142, 365, 360, 381]
2026-08-10 13:48:14,233 INFO     29 [qwen-vl-table] page=7 coord: matched 1/1, time=7.5s
2026-08-10 13:48:14,233 INFO     29 [qwen-vl-table] new_positions (1):
[[8, 132.02648474121094, 334.71503173828125, 735.6319696044922, 767.8788504638671]]
2026-08-10 13:48:14,233 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=9.9s
2026-08-10 13:48:14,235 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:48:14,244 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:48:14,244 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[8]
2026-08-10 13:48:14,244 INFO     29 [qwen-vl-table] positions ： [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:48:14,516 INFO     29 [qwen-vl-table] page=8, rect=930x2015, img=(2583x5599)
2026-08-10 13:48:14,516 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:14,517 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 110, \"bbox_end\": 117, \"encounter_dates\": [\"2025-05-08\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccc}\n报告时间: 2025-05-08\n\\hline\n名称 & 结果(参考值) \\\\\n\\hline\n★葡萄糖（已糖激酶法） & ↑ 14.46 mmol/L (3.6--6.11) \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:48:14,519 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:48:14.518+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 58, "failed": 0, "current": {"ee0bc9a294c111f1bd9827cf206dfa2d": {"id": "ee0bc9a294c111f1bd9827cf206dfa2d", "doc_id": "eddf381a94c111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "XJYo-\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "type": "pdf", "location": "XJYo-\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "size": 1663007, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786369606857, "task_type": "dataflow", "root_trace_id": "fca2d36450a74bdfa74068ff62a9c874", "root_traceparent": "00-fca2d36450a74bdfa74068ff62a9c874-672b5c2f105370f4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:48:16,307 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:16,307 INFO     29 [qwen-vl-table] page=8 LLM output (len=225):
{
  "report_date": "2025-05-08",
  "items": [
    {
      "name": "葡萄糖（已糖激酶法）",
      "item_code": null,
      "value": "14.46",
      "unit": "mmol/L",
      "reference_range": "3.6--6.11",
      "abnormal": true
    }
  ]
}
2026-08-10 13:48:16,307 INFO     29 [qwen-vl-table] coord grouping: {8: 1}
2026-08-10 13:48:16,308 INFO     29 [qwen-vl-table] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1034465, prompt_len=517
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
葡萄糖（已糖激酶法）

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
2026-08-10 13:48:22,461 INFO     29 [qwen-vl-table] coord API raw response (len=69):
```json
[
	{"text": "葡萄糖（已糖激酶法）", "bbox": [170, 355, 435, 372]}
]
```
2026-08-10 13:48:22,461 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=6.2s
2026-08-10 13:48:22,461 INFO     29 [qwen-vl-table] coord item[0]: text=葡萄糖（已糖激酶法）, bbox=[170, 355, 435, 372]
2026-08-10 13:48:22,462 INFO     29 [qwen-vl-table] page=8 coord: matched 1/1, time=6.2s
2026-08-10 13:48:22,462 INFO     29 [qwen-vl-table] new_positions (1):
[[9, 158.05987609863283, 404.4473300170899, 715.4776690673827, 749.7399799804687]]
2026-08-10 13:48:22,462 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=8.2s
2026-08-10 13:48:22,471 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 13:48:22,471 INFO     29 [Trace] task=ee0bc9a2 | doc=XJYo-糖尿病-哈大四.pdf | Extractor:LabExam | outputs={"chunks": "5 items, types={'LabReport': 5}", "html": "", "json": "118 items", "markdown": "", "text": "", "name": "XJYo-糖尿病-哈大四.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 5, \"chunks_Medication\": 2}"}
2026-08-10 13:48:22,471 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 13:48:22,476 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:22,476 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:48:23,318 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:23,330 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 13:48:23,331 INFO     29 [Trace] task=ee0bc9a2 | doc=XJYo-糖尿病-哈大四.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "118 items", "markdown": "", "text": "", "name": "XJYo-糖尿病-哈大四.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 5, \"chunks_Medication\": 2}"}
2026-08-10 13:48:23,331 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 13:48:23,339 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:48:23,340 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:48:23,341 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 13:48:23,341 INFO     29 [qwen-vl-text] positions(21): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:48:23,341 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [21]
2026-08-10 13:48:23,563 INFO     29 [qwen-vl-text] page=1, rect=810x1440, img=(2250x4000), dpi=200
2026-08-10 13:48:23,565 INFO     29 [qwen-vl-text] LLM extraction start, text_len=274
2026-08-10 13:48:23,565 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:23,565 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 17, \"bbox_end\": 37, \"encounter_dates\": [\"2021-09-12\"], \"department\": \"哈尔滨同迈综合门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "哈尔滨同迈综合门诊\n姓名:\n就诊日期: 2021-09-12\n就诊号: 20210912003\n姓名:\n年龄: 48岁\n性别: 男\n地址:\n药物过敏史:\n主诉: 糖尿病患者体检\n现病史: 患者自述确诊2型糖尿病8年余, 近段时间, 血糖升高, 口服降\n糖灵片, 降糖效果甚微, 自测指尖血糖14.2mmol/L, 来院诊治\n既往史: 2型糖尿病\n查体: T36.5℃ BP135-90mmHg -\n辅助检查: 已回报\n临床诊断: 2型糖尿病\n治疗意见: 盐酸二甲双胍片 每日3次 每次0.5g 随餐口服\n半月后复诊\n医师(签字):\n主治医师\n赵东强",
    "role": "user"
  }
]
2026-08-10 13:48:25,154 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:25,154 INFO     29 [qwen-vl-text] LLM output (len=258):
{
  "encounter_date": "2021-09-12",
  "chief_complaint": "糖尿病患者体检",
  "present_illness": "患者自述确诊2型糖尿病8年余, 近段时间, 血糖升高, 口服降糖灵片, 降糖效果甚微, 自测指尖血糖14.2mmol/L, 来院诊治",
  "past_history": "2型糖尿病",
  "diagnosis": "2型糖尿病",
  "treatment_plan": "盐酸二甲双胍片 每日3次 每次0.5g 随餐口服"
}
2026-08-10 13:48:25,155 INFO     29 [qwen-vl-text] Updated encounter_dates=[2021-09-12]
2026-08-10 13:48:25,158 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1151179, prompt_len=950
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共21行）
["哈尔滨同迈综合门诊", "姓名:", "就诊日期: 2021-09-12", "就诊号: 20210912003", "姓名:", "年龄: 48岁", "性别: 男", "地址:", "药物过敏史:", "主诉: 糖尿病患者体检", "现病史: 患者自述确诊2型糖尿病8年余, 近段时间, 血糖升高, 口服降", "糖灵片, 降糖效果甚微, 自测指尖血糖14.2mmol/L, 来院诊治", "既往史: 2型糖尿病", "查体: T36.5℃ BP135-90mmHg -", "辅助检查: 已回报", "临床诊断: 2型糖尿病", "治疗意见: 盐酸二甲双胍片 每日3次 每次0.5g 随餐口服", "半月后复诊", "医师(签字):", "主治医师", "赵东强"]

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
2026-08-10 13:48:34,137 INFO     29 [qwen-vl-text] coord API raw response (len=1189):
[
	{"text": "哈尔滨同迈综合门诊", "bbox": [389, 28, 695, 48]},
	{"text": "姓名:", "bbox": [100, 56, 150, 70]},
	{"text": "就诊日期: 2021-09-12", "bbox": [374, 57, 621, 71]},
	{"text": "就诊号: 20210912003", "bbox": [748, 59, 980, 74]},
	{"text": "姓名:", "bbox": [100, 93, 156, 107]},
	{"text": "年龄: 48岁", "bbox": [291, 93, 425, 107]},
	{"text": "性别: 男", "bbox": [452, 93, 552, 107]},
	{"text": "地址:", "bbox": [591, 94, 652, 107]},
	{"text": "药物过敏史:", "bbox": [162, 111, 300, 125]},
	{"text": "主诉: 糖尿病患者体检", "bbox": [162, 128, 419, 142]},
	{"text": "现病史: 患者自述确诊2型糖尿病8年余, 近段时间, 血糖升高, 口服降", "bbox": [162, 146, 980, 161]},
	{"text": "糖灵片, 降糖效果甚微, 自测指尖血糖14.2mmol/L, 来院诊治", "bbox": [100, 164, 783, 179]},
	{"text": "既往史: 2型糖尿病", "bbox": [162, 182, 386, 197]},
	{"text": "查体: T36.5℃ BP135-90mmHg -", "bbox": [162, 200, 521, 215]},
	{"text": "辅助检查: 已回报", "bbox": [162, 219, 367, 234]},
	{"text": "临床诊断: 2型糖尿病", "bbox": [162, 238, 412, 253]},
	{"text": "治疗意见: 盐酸二甲双胍片 每日3次 每次0.5g 随餐口服", "bbox": [162, 257, 822, 272]},
	{"text": "半月后复诊", "bbox": [291, 275, 419, 290]},
	{"text": "医师(签字):", "bbox": [653, 313, 800, 328]},
	{"text": "主治医师", "bbox": [810, 294, 900, 312]},
	{"text": "赵东强", "bbox": [809, 318, 900, 344]}
]
2026-08-10 13:48:34,137 INFO     29 [qwen-vl-text] coord API: raw_items=21, valid_items=21, elapsed=9.0s
2026-08-10 13:48:34,137 INFO     29 [qwen-vl-text] coord item[0]: text=哈尔滨同迈综合门诊, bbox=[389, 28, 695, 48]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] coord item[1]: text=姓名:, bbox=[100, 56, 150, 70]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] coord item[2]: text=就诊日期: 2021-09-12, bbox=[374, 57, 621, 71]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] coord item[3]: text=就诊号: 20210912003, bbox=[748, 59, 980, 74]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] coord item[4]: text=姓名:, bbox=[100, 93, 156, 107]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] coord item[5]: text=年龄: 48岁, bbox=[291, 93, 425, 107]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] coord item[6]: text=性别: 男, bbox=[452, 93, 552, 107]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] coord item[7]: text=地址:, bbox=[591, 94, 652, 107]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] coord item[8]: text=药物过敏史:, bbox=[162, 111, 300, 125]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] coord item[9]: text=主诉: 糖尿病患者体检, bbox=[162, 128, 419, 142]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] coord item[10]: text=现病史: 患者自述确诊2型糖尿病8年余, 近段时间, 血糖升高, 口服降, bbox=[162, 146, 980, 161]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] coord item[11]: text=糖灵片, 降糖效果甚微, 自测指尖血糖14.2mmol/L, 来院诊治, bbox=[100, 164, 783, 179]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] coord item[12]: text=既往史: 2型糖尿病, bbox=[162, 182, 386, 197]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] coord item[13]: text=查体: T36.5℃ BP135-90mmHg -, bbox=[162, 200, 521, 215]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] coord item[14]: text=辅助检查: 已回报, bbox=[162, 219, 367, 234]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] coord item[15]: text=临床诊断: 2型糖尿病, bbox=[162, 238, 412, 253]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] coord item[16]: text=治疗意见: 盐酸二甲双胍片 每日3次 每次0.5g 随餐口服, bbox=[162, 257, 822, 272]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] coord item[17]: text=半月后复诊, bbox=[291, 275, 419, 290]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] coord item[18]: text=医师(签字):, bbox=[653, 313, 800, 328]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] coord item[19]: text=主治医师, bbox=[810, 294, 900, 312]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] coord item[20]: text=赵东强, bbox=[809, 318, 900, 344]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] page=1 — 21/21 coords, api_time=9.0s
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] new_positions (21):
[[1, 315.09000000000003, 562.95, 40.32, 69.12], [1, 81.0, 121.50000000000001, 80.64, 100.8], [1, 302.94, 503.01000000000005, 82.08, 102.24], [1, 605.88, 793.8000000000001, 84.96, 106.56], [1, 81.0, 126.36000000000001, 133.92, 154.07999999999998], [1, 235.71, 344.25, 133.92, 154.07999999999998], [1, 366.12, 447.12, 133.92, 154.07999999999998], [1, 478.71000000000004, 528.12, 135.35999999999999, 154.07999999999998], [1, 131.22, 243.00000000000003, 159.84, 180.0], [1, 131.22, 339.39000000000004, 184.32, 204.48], [1, 131.22, 793.8000000000001, 210.23999999999998, 231.84], [1, 81.0, 634.23, 236.16, 257.76], [1, 131.22, 312.66, 262.08, 283.68], [1, 131.22, 422.01000000000005, 288.0, 309.59999999999997], [1, 131.22, 297.27000000000004, 315.36, 336.96], [1, 131.22, 333.72, 342.71999999999997, 364.32], [1, 131.22, 665.82, 370.08, 391.68], [1, 235.71, 339.39000000000004, 396.0, 417.59999999999997], [1, 528.9300000000001, 648.0, 450.71999999999997, 472.32], [1, 656.1, 729.0, 423.35999999999996, 449.28], [1, 655.2900000000001, 729.0, 457.91999999999996, 495.35999999999996]]
2026-08-10 13:48:34,138 INFO     29 [qwen-vl-text] ═══ DONE ═══ 21 positions, pages=1, time=10.8s
2026-08-10 13:48:34,145 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 13:48:34,145 INFO     29 [Trace] task=ee0bc9a2 | doc=XJYo-糖尿病-哈大四.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "118 items", "markdown": "", "text": "", "name": "XJYo-糖尿病-哈大四.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 5, \"chunks_Medication\": 2}"}
2026-08-10 13:48:34,146 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 13:48:34,150 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:48:34,151 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:48:34,151 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 13:48:34,151 INFO     29 [qwen-vl-text] positions(16): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:48:34,151 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [16]
2026-08-10 13:48:34,298 INFO     29 [qwen-vl-text] page=4, rect=608x1080, img=(1688x3000), dpi=200
2026-08-10 13:48:34,298 INFO     29 [qwen-vl-text] LLM extraction start, text_len=225
2026-08-10 13:48:34,298 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:34,299 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 54, \"bbox_end\": 69, \"encounter_dates\": [\"2024-08-22\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "哈尔滨体诚人药房有限公司\n(P23010122054)销售单\n号12875 日期2024-08-22\n药师：高芳 代码Y2301240061\n品名 盐酸二甲双胍片\n国家编码\n单价6.00 数量15.0 金额90.00\n单位 盒 规格0.25g/24T/2板\n批号22110778 效期2025-11-1\n产地：北京市小康药业有限公\n销售员：05\n合计：90.00 折前金额：90.0\n实收：90.00\n积分 0522\n付款方式：现金01#\n健康热线：",
    "role": "user"
  }
]
2026-08-10 13:48:36,600 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:36,600 INFO     29 [qwen-vl-text] LLM output (len=430):
{
  "encounter_date": "2024-08-22",
  "pharmacy": "哈尔滨体诚人药房有限公司",
  "medications": [
    {
      "name": "盐酸二甲双胍片",
      "specification": "0.25g/24T/2板",
      "dosage": null,
      "quantity": 15.0,
      "unit_price": 6.00,
      "total_price": 90.00,
      "frequency": null,
      "route": null,
      "manufacturer": "北京市小康药业有限公",
      "approval_number": null
    }
  ],
  "payment_total": 90.00,
  "payment_method": "现金"
}
2026-08-10 13:48:36,600 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-08-22]
2026-08-10 13:48:36,604 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1416593, prompt_len=886
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["哈尔滨体诚人药房有限公司", "(P23010122054)销售单", "号12875 日期2024-08-22", "药师：高芳 代码Y2301240061", "品名 盐酸二甲双胍片", "国家编码", "单价6.00 数量15.0 金额90.00", "单位 盒 规格0.25g/24T/2板", "批号22110778 效期2025-11-1", "产地：北京市小康药业有限公", "销售员：05", "合计：90.00 折前金额：90.0", "实收：90.00", "积分 0522", "付款方式：现金01#", "健康热线："]

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
2026-08-10 13:48:44,271 INFO     29 [qwen-vl-text] coord API raw response (len=932):
[
	{"text": "哈尔滨体诚人药房有限公司", "bbox": [185, 116, 720, 145]},
	{"text": "(P23010122054)销售单", "bbox": [206, 153, 647, 179]},
	{"text": "号12875 日期2024-08-22", "bbox": [190, 191, 732, 216]},
	{"text": "药师：高芳 代码Y2301240061", "bbox": [185, 226, 757, 254]},
	{"text": "品名 盐酸二甲双胍片", "bbox": [182, 263, 593, 292]},
	{"text": "国家编码", "bbox": [182, 307, 358, 334]},
	{"text": "单价6.00 数量15.0 金额90.00", "bbox": [187, 343, 767, 372]},
	{"text": "单位 盒 规格0.25g/24T/2板", "bbox": [188, 381, 754, 411]},
	{"text": "批号22110778 效期2025-11-1", "bbox": [188, 420, 767, 449]},
	{"text": "产地：北京市小康药业有限公", "bbox": [192, 460, 754, 488]},
	{"text": "销售员：05", "bbox": [196, 502, 411, 527]},
	{"text": "合计：90.00 折前金额：90.0", "bbox": [206, 538, 770, 565]},
	{"text": "实收：90.00", "bbox": [216, 577, 428, 601]},
	{"text": "积分 0522", "bbox": [524, 611, 704, 632]},
	{"text": "付款方式：现金01#", "bbox": [218, 647, 577, 671]},
	{"text": "健康热线：", "bbox": [222, 682, 398, 703]}
]
2026-08-10 13:48:44,271 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=7.7s
2026-08-10 13:48:44,271 INFO     29 [qwen-vl-text] coord item[0]: text=哈尔滨体诚人药房有限公司, bbox=[185, 116, 720, 145]
2026-08-10 13:48:44,271 INFO     29 [qwen-vl-text] coord item[1]: text=(P23010122054)销售单, bbox=[206, 153, 647, 179]
2026-08-10 13:48:44,271 INFO     29 [qwen-vl-text] coord item[2]: text=号12875 日期2024-08-22, bbox=[190, 191, 732, 216]
2026-08-10 13:48:44,271 INFO     29 [qwen-vl-text] coord item[3]: text=药师：高芳 代码Y2301240061, bbox=[185, 226, 757, 254]
2026-08-10 13:48:44,271 INFO     29 [qwen-vl-text] coord item[4]: text=品名 盐酸二甲双胍片, bbox=[182, 263, 593, 292]
2026-08-10 13:48:44,271 INFO     29 [qwen-vl-text] coord item[5]: text=国家编码, bbox=[182, 307, 358, 334]
2026-08-10 13:48:44,271 INFO     29 [qwen-vl-text] coord item[6]: text=单价6.00 数量15.0 金额90.00, bbox=[187, 343, 767, 372]
2026-08-10 13:48:44,271 INFO     29 [qwen-vl-text] coord item[7]: text=单位 盒 规格0.25g/24T/2板, bbox=[188, 381, 754, 411]
2026-08-10 13:48:44,271 INFO     29 [qwen-vl-text] coord item[8]: text=批号22110778 效期2025-11-1, bbox=[188, 420, 767, 449]
2026-08-10 13:48:44,271 INFO     29 [qwen-vl-text] coord item[9]: text=产地：北京市小康药业有限公, bbox=[192, 460, 754, 488]
2026-08-10 13:48:44,271 INFO     29 [qwen-vl-text] coord item[10]: text=销售员：05, bbox=[196, 502, 411, 527]
2026-08-10 13:48:44,271 INFO     29 [qwen-vl-text] coord item[11]: text=合计：90.00 折前金额：90.0, bbox=[206, 538, 770, 565]
2026-08-10 13:48:44,271 INFO     29 [qwen-vl-text] coord item[12]: text=实收：90.00, bbox=[216, 577, 428, 601]
2026-08-10 13:48:44,271 INFO     29 [qwen-vl-text] coord item[13]: text=积分 0522, bbox=[524, 611, 704, 632]
2026-08-10 13:48:44,271 INFO     29 [qwen-vl-text] coord item[14]: text=付款方式：现金01#, bbox=[218, 647, 577, 671]
2026-08-10 13:48:44,271 INFO     29 [qwen-vl-text] coord item[15]: text=健康热线：, bbox=[222, 682, 398, 703]
2026-08-10 13:48:44,271 INFO     29 [qwen-vl-text] page=4 — 16/16 coords, api_time=7.7s
2026-08-10 13:48:44,271 INFO     29 [qwen-vl-text] new_positions (16):
[[4, 112.3875, 437.40000000000003, 125.28, 156.60000000000002], [4, 125.14500000000001, 393.0525, 165.24, 193.32000000000002], [4, 115.42500000000001, 444.69000000000005, 206.28, 233.28000000000003], [4, 112.3875, 459.87750000000005, 244.08, 274.32], [4, 110.56500000000001, 360.2475, 284.04, 315.36], [4, 110.56500000000001, 217.485, 331.56, 360.72], [4, 113.6025, 465.95250000000004, 370.44, 401.76000000000005], [4, 114.21000000000001, 458.055, 411.48, 443.88000000000005], [4, 114.21000000000001, 465.95250000000004, 453.6, 484.92], [4, 116.64000000000001, 458.055, 496.8, 527.0400000000001], [4, 119.07000000000001, 249.6825, 542.1600000000001, 569.1600000000001], [4, 125.14500000000001, 467.77500000000003, 581.0400000000001, 610.2], [4, 131.22, 260.01, 623.1600000000001, 649.08], [4, 318.33000000000004, 427.68, 659.88, 682.5600000000001], [4, 132.435, 350.52750000000003, 698.76, 724.6800000000001], [4, 134.865, 241.78500000000003, 736.5600000000001, 759.24]]
2026-08-10 13:48:44,272 INFO     29 [qwen-vl-text] ═══ DONE ═══ 16 positions, pages=1, time=10.1s
2026-08-10 13:48:44,272 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:48:44,278 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:48:44,278 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 13:48:44,278 INFO     29 [qwen-vl-text] positions(19): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:48:44,278 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [19]
2026-08-10 13:48:44,540 INFO     29 [qwen-vl-text] page=5, rect=959x1278, img=(2665x3550), dpi=200
2026-08-10 13:48:44,541 INFO     29 [qwen-vl-text] LLM extraction start, text_len=271
2026-08-10 13:48:44,541 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:44,542 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 70, \"bbox_end\": 88, \"encounter_dates\": [\"2024-12-19\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "哈尔滨泽福大药房有限\n公司销售单据\nNO.8555800415612312005\n2024-12-19 19:10:28\n会员 销售员:张子欣\n01 020749 盐酸二甲双胍片\n规格 0.25gX24片/2板 单位:1\n产地 北京市永康药业有限公司\n批号 23082416 效期 2026/0\n数量:15 单价:7.00\n总金额:￥105.00 元\n应收:￥105.00 实收:￥100.00\n优惠:￥5.00 找零:0.00\n付款方式:现金01#\n健康热线:\n地址:\n药品是特殊商品,一经售出不退\n如需开具发票者,持销售小票1\n到店开具。",
    "role": "user"
  }
]
2026-08-10 13:48:46,038 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:48:46.036+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 58, "failed": 0, "current": {"ee0bc9a294c111f1bd9827cf206dfa2d": {"id": "ee0bc9a294c111f1bd9827cf206dfa2d", "doc_id": "eddf381a94c111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "XJYo-\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "type": "pdf", "location": "XJYo-\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "size": 1663007, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786369606857, "task_type": "dataflow", "root_trace_id": "fca2d36450a74bdfa74068ff62a9c874", "root_traceparent": "00-fca2d36450a74bdfa74068ff62a9c874-672b5c2f105370f4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:48:47,108 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:47,109 INFO     29 [qwen-vl-text] LLM output (len=431):
{
  "encounter_date": "2024-12-19",
  "pharmacy": "哈尔滨泽福大药房有限公司",
  "medications": [
    {
      "name": "盐酸二甲双胍片",
      "specification": "0.25gX24片/2板",
      "dosage": null,
      "quantity": 15,
      "unit_price": 7.00,
      "total_price": 105.00,
      "frequency": null,
      "route": null,
      "manufacturer": "北京市永康药业有限公司",
      "approval_number": null
    }
  ],
  "payment_total": 100.00,
  "payment_method": "现金"
}
2026-08-10 13:48:47,109 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-12-19]
2026-08-10 13:48:47,113 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2331708, prompt_len=941
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共19行）
["哈尔滨泽福大药房有限", "公司销售单据", "NO.8555800415612312005", "2024-12-19 19:10:28", "会员 销售员:张子欣", "01 020749 盐酸二甲双胍片", "规格 0.25gX24片/2板 单位:1", "产地 北京市永康药业有限公司", "批号 23082416 效期 2026/0", "数量:15 单价:7.00", "总金额:￥105.00 元", "应收:￥105.00 实收:￥100.00", "优惠:￥5.00 找零:0.00", "付款方式:现金01#", "健康热线:", "地址:", "药品是特殊商品,一经售出不退", "如需开具发票者,持销售小票1", "到店开具。"]

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
2026-08-10 13:48:56,040 INFO     29 [qwen-vl-text] coord API raw response (len=1110):
[
	{"text": "哈尔滨泽福大药房有限", "bbox": [253, 147, 690, 188]},
	{"text": "公司销售单据", "bbox": [255, 195, 519, 238]},
	{"text": "NO.8555800415612312005", "bbox": [255, 240, 770, 278]},
	{"text": "2024-12-19 19:10:28", "bbox": [255, 284, 695, 318]},
	{"text": "会员 销售员:张子欣", "bbox": [253, 324, 757, 362]},
	{"text": "01 020749 盐酸二甲双胍片", "bbox": [253, 366, 757, 404]},
	{"text": "规格 0.25gX24片/2板 单位:1", "bbox": [255, 409, 792, 448]},
	{"text": "产地 北京市永康药业有限公司", "bbox": [255, 451, 793, 490]},
	{"text": "批号 23082416 效期 2026/0", "bbox": [253, 495, 790, 532]},
	{"text": "数量:15 单价:7.00", "bbox": [253, 540, 748, 577]},
	{"text": "总金额:￥105.00 元", "bbox": [253, 584, 690, 620]},
	{"text": "应收:￥105.00 实收:￥100.00", "bbox": [253, 627, 800, 665]},
	{"text": "优惠:￥5.00 找零:0.00", "bbox": [253, 671, 703, 708]},
	{"text": "付款方式:现金01#", "bbox": [253, 715, 625, 755]},
	{"text": "健康热线:", "bbox": [253, 760, 448, 802]},
	{"text": "地址:", "bbox": [250, 812, 365, 848]},
	{"text": "药品是特殊商品,一经售出不退", "bbox": [253, 853, 810, 894]},
	{"text": "如需开具发票者,持销售小票1", "bbox": [253, 898, 810, 937]},
	{"text": "到店开具。", "bbox": [253, 947, 440, 979]}
]
2026-08-10 13:48:56,040 INFO     29 [qwen-vl-text] coord API: raw_items=19, valid_items=19, elapsed=8.9s
2026-08-10 13:48:56,040 INFO     29 [qwen-vl-text] coord item[0]: text=哈尔滨泽福大药房有限, bbox=[253, 147, 690, 188]
2026-08-10 13:48:56,040 INFO     29 [qwen-vl-text] coord item[1]: text=公司销售单据, bbox=[255, 195, 519, 238]
2026-08-10 13:48:56,040 INFO     29 [qwen-vl-text] coord item[2]: text=NO.8555800415612312005, bbox=[255, 240, 770, 278]
2026-08-10 13:48:56,040 INFO     29 [qwen-vl-text] coord item[3]: text=2024-12-19 19:10:28, bbox=[255, 284, 695, 318]
2026-08-10 13:48:56,040 INFO     29 [qwen-vl-text] coord item[4]: text=会员 销售员:张子欣, bbox=[253, 324, 757, 362]
2026-08-10 13:48:56,040 INFO     29 [qwen-vl-text] coord item[5]: text=01 020749 盐酸二甲双胍片, bbox=[253, 366, 757, 404]
2026-08-10 13:48:56,040 INFO     29 [qwen-vl-text] coord item[6]: text=规格 0.25gX24片/2板 单位:1, bbox=[255, 409, 792, 448]
2026-08-10 13:48:56,040 INFO     29 [qwen-vl-text] coord item[7]: text=产地 北京市永康药业有限公司, bbox=[255, 451, 793, 490]
2026-08-10 13:48:56,040 INFO     29 [qwen-vl-text] coord item[8]: text=批号 23082416 效期 2026/0, bbox=[253, 495, 790, 532]
2026-08-10 13:48:56,040 INFO     29 [qwen-vl-text] coord item[9]: text=数量:15 单价:7.00, bbox=[253, 540, 748, 577]
2026-08-10 13:48:56,040 INFO     29 [qwen-vl-text] coord item[10]: text=总金额:￥105.00 元, bbox=[253, 584, 690, 620]
2026-08-10 13:48:56,040 INFO     29 [qwen-vl-text] coord item[11]: text=应收:￥105.00 实收:￥100.00, bbox=[253, 627, 800, 665]
2026-08-10 13:48:56,040 INFO     29 [qwen-vl-text] coord item[12]: text=优惠:￥5.00 找零:0.00, bbox=[253, 671, 703, 708]
2026-08-10 13:48:56,040 INFO     29 [qwen-vl-text] coord item[13]: text=付款方式:现金01#, bbox=[253, 715, 625, 755]
2026-08-10 13:48:56,040 INFO     29 [qwen-vl-text] coord item[14]: text=健康热线:, bbox=[253, 760, 448, 802]
2026-08-10 13:48:56,040 INFO     29 [qwen-vl-text] coord item[15]: text=地址:, bbox=[250, 812, 365, 848]
2026-08-10 13:48:56,040 INFO     29 [qwen-vl-text] coord item[16]: text=药品是特殊商品,一经售出不退, bbox=[253, 853, 810, 894]
2026-08-10 13:48:56,040 INFO     29 [qwen-vl-text] coord item[17]: text=如需开具发票者,持销售小票1, bbox=[253, 898, 810, 937]
2026-08-10 13:48:56,040 INFO     29 [qwen-vl-text] coord item[18]: text=到店开具。, bbox=[253, 947, 440, 979]
2026-08-10 13:48:56,041 INFO     29 [qwen-vl-text] page=5 — 19/19 coords, api_time=8.9s
2026-08-10 13:48:56,041 INFO     29 [qwen-vl-text] new_positions (19):
[[5, 242.69025000000002, 661.8825, 187.866, 240.264], [5, 244.60875000000001, 497.85075, 249.21, 304.164], [5, 244.60875000000001, 738.6225000000001, 306.72, 355.284], [5, 244.60875000000001, 666.67875, 362.952, 406.404], [5, 242.69025000000002, 726.15225, 414.072, 462.636], [5, 242.69025000000002, 726.15225, 467.748, 516.312], [5, 244.60875000000001, 759.726, 522.702, 572.544], [5, 244.60875000000001, 760.68525, 576.378, 626.22], [5, 242.69025000000002, 757.8075, 632.61, 679.896], [5, 242.69025000000002, 717.519, 690.12, 737.4060000000001], [5, 242.69025000000002, 661.8825, 746.352, 792.36], [5, 242.69025000000002, 767.4000000000001, 801.306, 849.87], [5, 242.69025000000002, 674.35275, 857.538, 904.8240000000001], [5, 242.69025000000002, 599.53125, 913.77, 964.89], [5, 242.69025000000002, 429.744, 971.28, 1024.9560000000001], [5, 239.8125, 350.12625, 1037.736, 1083.744], [5, 242.69025000000002, 776.9925000000001, 1090.134, 1142.532], [5, 242.69025000000002, 776.9925000000001, 1147.644, 1197.486], [5, 242.69025000000002, 422.07, 1210.266, 1251.162]]
2026-08-10 13:48:56,041 INFO     29 [qwen-vl-text] ═══ DONE ═══ 19 positions, pages=1, time=11.8s
2026-08-10 13:48:56,051 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 13:48:56,051 INFO     29 [Trace] task=ee0bc9a2 | doc=XJYo-糖尿病-哈大四.pdf | Extractor:Medication | outputs={"chunks": "2 items, types={'MedicationRecord': 2}", "html": "", "json": "118 items", "markdown": "", "text": "", "name": "XJYo-糖尿病-哈大四.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 5, \"chunks_Medication\": 2}"}
2026-08-10 13:48:56,051 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 13:48:56,056 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:56,056 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:48:57,247 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:57,257 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 13:48:57,257 INFO     29 [Trace] task=ee0bc9a2 | doc=XJYo-糖尿病-哈大四.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "118 items", "markdown": "", "text": "", "name": "XJYo-糖尿病-哈大四.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 5, \"chunks_Medication\": 2}"}
2026-08-10 13:48:57,257 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 13:48:57,264 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:57,265 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:48:57,739 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:57,748 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 13:48:57,748 INFO     29 [Trace] task=ee0bc9a2 | doc=XJYo-糖尿病-哈大四.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "118 items", "markdown": "", "text": "", "name": "XJYo-糖尿病-哈大四.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 5, \"chunks_Medication\": 2}"}
2026-08-10 13:48:57,748 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 13:48:57,754 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:57,754 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:48:58,254 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:58,264 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 13:48:58,264 INFO     29 [Trace] task=ee0bc9a2 | doc=XJYo-糖尿病-哈大四.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "118 items", "markdown": "", "text": "", "name": "XJYo-糖尿病-哈大四.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 5, \"chunks_Medication\": 2}"}
2026-08-10 13:48:58,264 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 13:48:58,270 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:58,271 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:48:59,387 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:59,392 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 13:48:59,392 INFO     29 [Trace] task=ee0bc9a2 | doc=XJYo-糖尿病-哈大四.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "118 items", "markdown": "", "text": "", "name": "XJYo-糖尿病-哈大四.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 5, \"chunks_Medication\": 2}"}
2026-08-10 13:48:59,392 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 13:48:59,396 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:59,397 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:48:59,877 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:48:59,886 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 13:48:59,886 INFO     29 [Trace] task=ee0bc9a2 | doc=XJYo-糖尿病-哈大四.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "118 items", "markdown": "", "text": "", "name": "XJYo-糖尿病-哈大四.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 5, \"chunks_Medication\": 2}"}
2026-08-10 13:48:59,886 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 13:48:59,886 INFO     29 [ChunkMerger] Merged 8 chunks from 9 sources: {'Extractor:LabExam': 5, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 2, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 6 noise chunks)
2026-08-10 13:48:59,895 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 13:48:59,895 INFO     29 [Trace] task=ee0bc9a2 | doc=XJYo-糖尿病-哈大四.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "8 items, types={'LabReport': 5, 'OutpatientRecord': 1, 'MedicationRecord': 2}", "name": "XJYo-糖尿病-哈大四.pdf"}
2026-08-10 13:48:59,895 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 13:48:59,927 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786369607888, 'update_date': datetime.datetime(2026, 8, 10, 13, 46, 47), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1050105, 'status': '1'}
2026-08-10 13:49:00,149 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   糖化血红蛋白  None  9.46  %  4--6  True   
---
   糖化血红蛋白  None  8.0  %  4—6  True   
---
   糖化血红蛋白LA1c  HbA1c  7.50  None  None  False   
---
   糖化血红蛋白A1  None  8%  %  4--6  True   
---
   葡萄糖（已糖激酶法）  None  14.46  mmol/L  3.6--6.11  True   
---
哈尔滨同迈综合门诊
姓名:
就诊日期: 2021-09-12
就诊号: 20210912003
姓名:
年龄: 48岁
性别: 男
地址:
药物过敏史:
主诉: 糖尿病患者体检
现病史: 患者自述确诊2型糖尿病8年余, 近段时间, 血糖升高, 口服降
糖灵片, 降糖效果甚微, 自测指尖血糖14.2mmol/L, 来院诊治
既往史: 2型糖尿病
查体: T36.5℃ BP135-90mmHg -
辅助检查: 已回报
临床诊断: 2型糖尿病
治疗意见: 盐酸二甲双胍片 每日3次 每次0.5g 随餐口服
半月后复诊
医师(签字):
主治医师
赵东强
---
哈尔滨体诚人药房有限公司
(P23010122054)销售单
号12875 日期2024-08-22
药师：高芳 代码Y2301240061
品名 盐酸二甲双胍片
国家编码
单价6.00 数量15.0 金额90.00
单位 盒 规格0.25g/24T/2板
批号22110778 效期2025-11-1
产地：北京市小康药业有限公
销售员：05
合计：90.00 折前金额：90.0
实收：90.00
积分 0522
付款方式：现金01#
健康热线：
---
哈尔滨泽福大药房有限
公司销售单据
NO.8555800415612312005
2024-12-19 19:10:28
会员 销售员:张子欣
01 020749 盐酸二甲双胍片
规格 0.25gX24片/2板 单位:1
产地 北京市永康药业有限公司
批号 23082416 效期 2026/0
数量:15 单价:7.00
总金额:￥105.00 元
应收:￥105.00 实收:￥100.00
优惠:￥5.00 找零:0.00
付款方式:现金01#
健康热线:
地址:
药品是特殊商品,一经售出不退
如需开具发票者,持销售小票1
到店开具。
2026-08-10 13:49:00,523 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 13:49:00,523 INFO     29 [Trace] task=ee0bc9a2 | doc=XJYo-糖尿病-哈大四.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "8 items, types={'LabReport': 5, 'OutpatientRecord': 1, 'MedicationRecord': 2}", "name": "XJYo-糖尿病-哈大四.pdf", "embedding_token_consumption": 814}
2026-08-10 13:49:00,523 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 13:49:00,695 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 13:49:00,695 INFO     29 [Trace] task=ee0bc9a2 | doc=XJYo-糖尿病-哈大四.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":8,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 13:49:00,699 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(3, 59, 143, 348, 365) row[-1]=(3, 59, 143, 348, 365)
2026-08-10 13:49:00,699 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(4, 69, 154, 274, 290) row[-1]=(4, 69, 154, 274, 290)
2026-08-10 13:49:00,699 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(7, 43, 323, 1864, 1909) row[-1]=(7, 43, 323, 1864, 1909)
2026-08-10 13:49:00,699 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(8, 132, 334, 735, 767) row[-1]=(8, 132, 334, 735, 767)
2026-08-10 13:49:00,699 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(9, 158, 404, 715, 749) row[-1]=(9, 158, 404, 715, 749)
2026-08-10 13:49:00,699 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:49:00,699 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:49:00,699 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:49:00,703 INFO     29 set_progress(ee0bc9a294c111f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 13:49:00 [DOC Engine]:
Start to index...
2026-08-10 13:49:00,722 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.013s]
2026-08-10 13:49:00,726 INFO     29 set_progress(ee0bc9a294c111f1bd9827cf206dfa2d), progress: 0.8125, progress_msg: 
2026-08-10 13:49:00,743 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.008s]
2026-08-10 13:49:00,749 INFO     29 set_progress(ee0bc9a294c111f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 13:49:00 Indexing done (0.05s). Task done (126.72s)
2026-08-10 13:49:00,752 INFO     29 [Done], chunks(8), token(814), elapsed:126.72
2026-08-10 13:49:00,843 INFO     29 handle_task done for task {"id": "ee0bc9a294c111f1bd9827cf206dfa2d", "doc_id": "eddf381a94c111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "XJYo-\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "type": "pdf", "location": "XJYo-\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "size": 1663007, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786369606857, "task_type": "dataflow", "root_trace_id": "fca2d36450a74bdfa74068ff62a9c874", "root_traceparent": "00-fca2d36450a74bdfa74068ff62a9c874-672b5c2f105370f4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
