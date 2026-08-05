# 基准结果：麦济ZHYH.pdf

## 基本信息

- 文件：`麦济ZHYH.pdf`
- 大小：10282.5 KB
- PDF 总页数：6
- doc_id：`8b75f8fc909411f1a3da71efcdd7cc1f`
- 上传方式：existing
- 状态：run=None (code=None)  progress=None
- 开始时间：2026-08-05T14:31:25  完成时间：2026-08-05T14:31:26  耗时：0.9s
- progress_msg：`06:14:47 Indexing done (0.05s). Task done (162.15s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | f83dbb06 | 1 | 1-1 | 内蒙古医科大学附属医院门诊病历 姓名： 年龄：62岁 诊疗号：001449878 |
| 2 | c9c92449 | 1 | 2-2 | 萱堂大药房 单号：2025111853212 日期：25/11/18 时间：13 |
| 3 | 599d4f5f | 1 | 3-3 | 电子发票(普通发票) 国家税务总局 江苏省税务局 发票号码：2532200000 |
| 4 | 58777c0c | 2 | 4-5 | 电子发票(普通发票) 国家税务总局 江苏省税务局 发票号码：2532200000 |
| 5 | 6494b5e4 | 1 | 5-5 | 报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录: 病历信息 □痕迹 |
| 6 | 47c12ad1 | 2 | 5-6 | 3:34 星期二 190.1.48.233 版本 王立红 电子发票(普通发票)  |

- chunks 总数：6
- 各 chunk 页数合计（含跨页重复）：8
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
- ChunkMerger：`{"found": true, "merged": 6, "sources": 8, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 2, "Extractor:Medication": 4, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-05 06:14:46,567 INFO     29 [ChunkMerger] Merged 6 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 4, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-05 06:11:50,960 INFO     29 handle_task begin for task {"id": "8c1d03f4909411f1a3da71efcdd7cc1f", "doc_id": "8b75f8fc909411f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHYH.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHYH.pdf", "size": 10529267, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785910310550, "task_type": "dataflow", "root_trace_id": "5845aea086174457a53e2c12052f4abe", "root_traceparent": "00-5845aea086174457a53e2c12052f4abe-577ba8815fd96dc1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-05 06:11:51,230 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-05 06:11:51,270 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-05 06:11:51,283 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-05 06:11:51,283 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-05 06:11:51,291 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-05 06:11:51,291 INFO     29 ============================================================
2026-08-05 06:11:51,291 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-05 06:11:51,291 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-05 06:11:51,291 INFO     29 ============================================================
2026-08-05 06:11:51,292 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-05 06:11:51,292 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-05 06:11:51,295 INFO     29 No torch found.
2026-08-05 06:11:52,303 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=6
2026-08-05 06:11:52,677 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1836114, prompt_len=644
2026-08-05 06:11:54,576 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 06:11:54,576 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-05 06:11:54,589 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1836114, prompt_len=401
2026-08-05 06:11:57,556 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T06:11:57.555+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 25, "failed": 0, "current": {"8c1d03f4909411f1a3da71efcdd7cc1f": {"id": "8c1d03f4909411f1a3da71efcdd7cc1f", "doc_id": "8b75f8fc909411f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHYH.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHYH.pdf", "size": 10529267, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785910310550, "task_type": "dataflow", "root_trace_id": "5845aea086174457a53e2c12052f4abe", "root_traceparent": "00-5845aea086174457a53e2c12052f4abe-577ba8815fd96dc1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 06:11:57,827 INFO     29 [qwen-vl-parser] text API response (len=476):
["内蒙古医科大学附属医院门诊病历", "姓名：", "年龄：62岁", "诊疗号：0014498780", "民族：", "性别：男性", "呼吸内科门诊", "联系电话：", "1 身份证：", "病情：", "就诊状态：", "就诊时间：2026-02-13 09:14", "生命体征（需要时）：", "体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg", "主诉：哮喘史，近3天呼吸困难加重，夜间咳嗽明显", "现病史：哮喘史，近3天呼吸困难加重，夜间咳嗽明显", "既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "无，吸烟史无，无过敏史。", "体格检查：发育正常，营养良好，体型正常，双肺呼吸音清，双肺未闻及啰", "音，双下肢无水肿，体重kg。", "辅助检查：心肺", "过敏史：不详", "初步诊断（西医）：1.支气管哮喘(急性发作期)", "初步诊断（中医）：", "治疗方案：随诊", "醋酸泼尼松片<5mg>", "用量：3.000片/次", "用法：口服，一次/日，5天", "签名："]
2026-08-05 06:11:57,827 INFO     29 [qwen-vl-parser] page=1 text: 29 lines (bbox 0-28)
2026-08-05 06:11:57,827 INFO     29 [qwen-vl-parser] page=1 text: 29 sections
2026-08-05 06:11:58,094 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1481445, prompt_len=644
2026-08-05 06:11:59,848 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 06:11:59,849 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-05 06:11:59,856 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1481445, prompt_len=401
2026-08-05 06:12:01,903 INFO     29 [qwen-vl-parser] text API response (len=259):
["萱堂大药房", "单号：2025111853212", "日期：25/11/18", "时间：13:2", "工号：001", "品名", "规格", "厂家", "金额", "数量", "总计", "布地格福吸入气雾剂", "60ug/7.2ug/4.8ug 吸", "120 撤/支", "支/盒", "219.00", "3", "657.00", "合计：657.00", "应收：657.00", "数量：3", "实收：657.00", "会员：", "药品属于特殊商品", "无质量问题，概不退换"]
2026-08-05 06:12:01,903 INFO     29 [qwen-vl-parser] page=2 text: 25 lines (bbox 29-53)
2026-08-05 06:12:01,903 INFO     29 [qwen-vl-parser] page=2 text: 25 sections
2026-08-05 06:12:02,017 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=778524, prompt_len=644
2026-08-05 06:12:03,569 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 06:12:03,570 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-05 06:12:03,579 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=778524, prompt_len=401
2026-08-05 06:12:06,049 INFO     29 [qwen-vl-parser] text API response (len=467):
["电子发票(普通发票)", "国家税务总局", "江苏省税务局", "发票号码：25322000000382591347", "开票日期：2025年08月20日", "购买方信息", "名称：", "统一社会信用代码/纳税人识别号：", "销售方信息", "名称：无锡邻医大药房有限公司", "统一社会信用代码/纳税人识别号：91320214MA228F680W", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*倍择瑞令", "160μg/7.2μg/4", "盒", "3", "210.029498522124", "630.09", "13%", "81.91", "畅布地格福吸入气雾剂", ".8μg*120揿", "", "", "", "", "", "", "", "合计", "￥630.09", "￥81.91", "价税合计（大写）", "柒佰壹拾贰圆整", "(小写) ￥712.00", "备注", "开票人：奚澳琼"]
2026-08-05 06:12:06,049 INFO     29 [qwen-vl-parser] page=3 text: 37 lines (bbox 54-90)
2026-08-05 06:12:06,049 INFO     29 [qwen-vl-parser] page=3 text: 37 sections
2026-08-05 06:12:06,164 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=730743, prompt_len=644
2026-08-05 06:12:07,551 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 06:12:07,551 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-05 06:12:07,558 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=730743, prompt_len=401
2026-08-05 06:12:10,091 INFO     29 [qwen-vl-parser] text API response (len=424):
["电子发票(普通发票)", "国家税务总局", "江苏省税务局", "发票号码：25322000000226700883", "开票日期：2025年05月20日", "购买方信息", "名称", "统一社会信用代码/纳税人识别号：", "销售方信息", "名称：无锡邻医大药房有限公司", "统一社会信用代码/纳税人识别号：91320214MA228F680W", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*倍择瑞令", "160μg/7.2μg/4", "盒", "3 210.029498522124", "630.09", "13%", "81.91", "畅布地格福吸入气雾剂", ".8μg*120揿", "合计", "￥630.09", "￥81.91", "价税合计（大写）", "柒佰壹拾贰圆整", "(小写) ￥712.00", "备注"]
2026-08-05 06:12:10,092 INFO     29 [qwen-vl-parser] page=4 text: 35 lines (bbox 91-125)
2026-08-05 06:12:10,092 INFO     29 [qwen-vl-parser] page=4 text: 35 sections
2026-08-05 06:12:10,741 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5637139, prompt_len=644
2026-08-05 06:12:14,065 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-12-10"}
```
2026-08-05 06:12:14,066 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=2024-12-10
2026-08-05 06:12:14,085 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5637139, prompt_len=401
2026-08-05 06:12:22,086 INFO     29 [qwen-vl-parser] text API response (len=563):
["挂号号:D20091... 医保余额:0 CM/KG 普通病人|现住址:内蒙古土默特左旗沙尔营乡大有庄村32", "报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录:", "病历信息 □痕迹 □批注 置未 ▼ 状态:只读-仅供查看 120% >", "内蒙古医科大学附属医院门诊病历", "姓名 龄:60岁 诊疗号:0014498780", "民族: 别: 男性 科室:呼吸内科门诊", "联系电话: 身份证:1 病情:", "就诊状态: 就诊时间: 2024-12-10 12:37", "生命体征(需要时):", "体温:℃ 脉搏:次/分 呼吸:次/分 血压:/mmHg", "主诉:SSSJ项目肺功能检查开单", "现病史: 哮喘", "既往史: 患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎", "无,吸烟史无,无过敏史。", "体格检查: 发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰", "音,双下肢无水肿,体重kg。", "辅助检查:", "初步诊断(西医): 1.哮喘", "初步诊断(中医):", "治疗方案:/", "呼吸过滤器 肺通气功能检查", "用量:", "用法:", "签名:崔丽英", "3:34 星期二 190.1.48.233 版本 王立红"]
2026-08-05 06:12:22,087 INFO     29 [qwen-vl-parser] page=5 text: 25 lines (bbox 126-150)
2026-08-05 06:12:22,087 INFO     29 [qwen-vl-parser] page=5 text: 25 sections
2026-08-05 06:12:22,206 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=809094, prompt_len=644
2026-08-05 06:12:23,607 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 06:12:23,608 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-05 06:12:23,616 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=809094, prompt_len=401
2026-08-05 06:12:26,940 INFO     29 [qwen-vl-parser] text API response (len=612):
["电子发票(普通发票)", "国家税务总局", "内蒙古自治区税务局", "发票号码：26152000000119478346", "开票日期：2026年02月09日", "购买方信息", "名称", "统一社会信用代码/纳税人识别号：", "销售方信息", "名称：国药控股国大药房内蒙古有限公司", "统一社会信用代码/纳税人识别号：911501005732872139", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*布地格福", "160ug:7.2ug/4.8u", "盒", "3", "237.16814159292", "711.50", "13%", "92.50", "吸入气雾剂", "g:120揿", "", "", "", "", "", "", "", "*化学药品制剂*布地格福", "160ug:7.2ug/4.8u", "盒", "3", "237.16814159292", "711.50", "13%", "92.50", "吸入气雾剂", "g:120揿", "", "", "", "", "", "", "", "", "合计", "￥1423.00", "￥185.00", "价税合计（大写）", "壹仟陆佰零捌圆整", "(小写) ￥1608.00", "备注", "开票人：刘惠"]
2026-08-05 06:12:26,941 INFO     29 [qwen-vl-parser] page=6 text: 47 lines (bbox 151-197)
2026-08-05 06:12:26,941 INFO     29 [qwen-vl-parser] page=6 text: 47 sections
2026-08-05 06:12:26,941 INFO     29 [qwen-vl-parser] parse_pdf done: 198 sections from 6 pages.
2026-08-05 06:12:26,954 INFO     29 Close text detector.
2026-08-05 06:12:27,314 INFO     29 Close text recognizer.
2026-08-05 06:12:27,638 INFO     29 Close recognizer.
2026-08-05 06:12:27,994 INFO     29 Close recognizer.
2026-08-05 06:12:28,340 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-05 06:12:28,340 INFO     29 [Trace] task=8c1d03f4 | doc=麦济ZHYH.pdf | Parser:MedLink | outputs={"html": "", "json": "198 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "json"}
2026-08-05 06:12:28,340 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-05 06:12:28,359 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 06:12:28,359 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。只有主诉，病史的也属于OutpatientRecord（门诊病历）\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 内蒙古医科大学附属医院门诊病历\n[BBOX-1] 姓名：\n[BBOX-2] 年龄：62岁\n[BBOX-3] 诊疗号：0014498780\n[BBOX-4] 民族：\n[BBOX-5] 性别：男性\n[BBOX-6] 呼吸内科门诊\n[BBOX-7] 联系电话：\n[BBOX-8] 1 身份证：\n[BBOX-9] 病情：\n[BBOX-10] 就诊状态：\n[BBOX-11] 就诊时间：2026-02-13 09:14\n[BBOX-12] 生命体征（需要时）：\n[BBOX-13] 体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg\n[BBOX-14] 主诉：哮喘史，近3天呼吸困难加重，夜间咳嗽明显\n[BBOX-15] 现病史：哮喘史，近3天呼吸困难加重，夜间咳嗽明显\n[BBOX-16] 既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎\n[BBOX-17] 无，吸烟史无，无过敏史。\n[BBOX-18] 体格检查：发育正常，营养良好，体型正常，双肺呼吸音清，双肺未闻及啰\n[BBOX-19] 音，双下肢无水肿，体重kg。\n[BBOX-20] 辅助检查：心肺\n[BBOX-21] 过敏史：不详\n[BBOX-22] 初步诊断（西医）：1.支气管哮喘(急性发作期)\n[BBOX-23] 初步诊断（中医）：\n[BBOX-24] 治疗方案：随诊\n[BBOX-25] 醋酸泼尼松片<5mg>\n[BBOX-26] 用量：3.000片/次\n[BBOX-27] 用法：口服，一次/日，5天\n[BBOX-28] 签名：\n[BBOX-29] 萱堂大药房\n[BBOX-30] 单号：2025111853212\n[BBOX-31] 日期：25/11/18\n[BBOX-32] 时间：13:2\n[BBOX-33] 工号：001\n[BBOX-34] 品名\n[BBOX-35] 规格\n[BBOX-36] 厂家\n[BBOX-37] 金额\n[BBOX-38] 数量\n[BBOX-39] 总计\n[BBOX-40] 布地格福吸入气雾剂\n[BBOX-41] 60ug/7.2ug/4.8ug 吸\n[BBOX-42] 120 撤/支\n[BBOX-43] 支/盒\n[BBOX-44] 219.00\n[BBOX-45] 3\n[BBOX-46] 657.00\n[BBOX-47] 合计：657.00\n[BBOX-48] 应收：657.00\n[BBOX-49] 数量：3\n[BBOX-50] 实收：657.00\n[BBOX-51] 会员：\n[BBOX-52] 药品属于特殊商品\n[BBOX-53] 无质量问题，概不退换\n[BBOX-54] 电子发票(普通发票)\n[BBOX-55] 国家税务总局\n[BBOX-56] 江苏省税务局\n[BBOX-57] 发票号码：25322000000382591347\n[BBOX-58] 开票日期：2025年08月20日\n[BBOX-59] 购买方信息\n[BBOX-60] 名称：\n[BBOX-61] 统一社会信用代码/纳税人识别号：\n[BBOX-62] 销售方信息\n[BBOX-63] 名称：无锡邻医大药房有限公司\n[BBOX-64] 统一社会信用代码/纳税人识别号：91320214MA228F680W\n[BBOX-65] 项目名称\n[BBOX-66] 规格型号\n[BBOX-67] 单位\n[BBOX-68] 数量\n[BBOX-69] 单价\n[BBOX-70] 金额\n[BBOX-71] 税率/征收率\n[BBOX-72] 税额\n[BBOX-73] *化学药品制剂*倍择瑞令\n[BBOX-74] 160μg/7.2μg/4\n[BBOX-75] 盒\n[BBOX-76] 3\n[BBOX-77] 210.029498522124\n[BBOX-78] 630.09\n[BBOX-79] 13%\n[BBOX-80] 81.91\n[BBOX-81] 畅布地格福吸入气雾剂\n[BBOX-82] .8μg*120揿\n[BBOX-83] 合计\n[BBOX-84] ￥630.09\n[BBOX-85] ￥81.91\n[BBOX-86] 价税合计（大写）\n[BBOX-87] 柒佰壹拾贰圆整\n[BBOX-88] (小写) ￥712.00\n[BBOX-89] 备注\n[BBOX-90] 开票人：奚澳琼\n[BBOX-91] 电子发票(普通发票)\n[BBOX-92] 国家税务总局\n[BBOX-93] 江苏省税务局\n[BBOX-94] 发票号码：25322000000226700883\n[BBOX-95] 开票日期：2025年05月20日\n[BBOX-96] 购买方信息\n[BBOX-97] 名称\n[BBOX-98] 统一社会信用代码/纳税人识别号：\n[BBOX-99] 销售方信息\n[BBOX-100] 名称：无锡邻医大药房有限公司\n[BBOX-101] 统一社会信用代码/纳税人识别号：91320214MA228F680W\n[BBOX-102] 项目名称\n[BBOX-103] 规格型号\n[BBOX-104] 单位\n[BBOX-105] 数量\n[BBOX-106] 单价\n[BBOX-107] 金额\n[BBOX-108] 税率/征收率\n[BBOX-109] 税额\n[BBOX-110] *化学药品制剂*倍择瑞令\n[BBOX-111] 160μg/7.2μg/4\n[BBOX-112] 盒\n[BBOX-113] 3 210.029498522124\n[BBOX-114] 630.09\n[BBOX-115] 13%\n[BBOX-116] 81.91\n[BBOX-117] 畅布地格福吸入气雾剂\n[BBOX-118] .8μg*120揿\n[BBOX-119] 合计\n[BBOX-120] ￥630.09\n[BBOX-121] ￥81.91\n[BBOX-122] 价税合计（大写）\n[BBOX-123] 柒佰壹拾贰圆整\n[BBOX-124] (小写) ￥712.00\n[BBOX-125] 备注\n[BBOX-126] 挂号号:D20091... 医保余额:0 CM/KG 普通病人|现住址:内蒙古土默特左旗沙尔营乡大有庄村32\n[BBOX-127] 报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录:\n[BBOX-128] 病历信息 □痕迹 □批注 置未 ▼ 状态:只读-仅供查看 120% >\n[BBOX-129] 内蒙古医科大学附属医院门诊病历\n[BBOX-130] 姓名 龄:60岁 诊疗号:0014498780\n[BBOX-131] 民族: 别: 男性 科室:呼吸内科门诊\n[BBOX-132] 联系电话: 身份证:1 病情:\n[BBOX-133] 就诊状态: 就诊时间: 2024-12-10 12:37\n[BBOX-134] 生命体征(需要时):\n[BBOX-135] 体温:℃ 脉搏:次/分 呼吸:次/分 血压:/mmHg\n[BBOX-136] 主诉:SSSJ项目肺功能检查开单\n[BBOX-137] 现病史: 哮喘\n[BBOX-138] 既往史: 患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎\n[BBOX-139] 无,吸烟史无,无过敏史。\n[BBOX-140] 体格检查: 发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰\n[BBOX-141] 音,双下肢无水肿,体重kg。\n[BBOX-142] 辅助检查:\n[BBOX-143] 初步诊断(西医): 1.哮喘\n[BBOX-144] 初步诊断(中医):\n[BBOX-145] 治疗方案:/\n[BBOX-146] 呼吸过滤器 肺通气功能检查\n[BBOX-147] 用量:\n[BBOX-148] 用法:\n[BBOX-149] 签名:崔丽英\n[BBOX-150] 3:34 星期二 190.1.48.233 版本 王立红\n[BBOX-151] 电子发票(普通发票)\n[BBOX-152] 国家税务总局\n[BBOX-153] 内蒙古自治区税务局\n[BBOX-154] 发票号码：26152000000119478346\n[BBOX-155] 开票日期：2026年02月09日\n[BBOX-156] 购买方信息\n[BBOX-157] 名称\n[BBOX-158] 统一社会信用代码/纳税人识别号：\n[BBOX-159] 销售方信息\n[BBOX-160] 名称：国药控股国大药房内蒙古有限公司\n[BBOX-161] 统一社会信用代码/纳税人识别号：911501005732872139\n[BBOX-162] 项目名称\n[BBOX-163] 规格型号\n[BBOX-164] 单位\n[BBOX-165] 数量\n[BBOX-166] 单价\n[BBOX-167] 金额\n[BBOX-168] 税率/征收率\n[BBOX-169] 税额\n[BBOX-170] *化学药品制剂*布地格福\n[BBOX-171] 160ug:7.2ug/4.8u\n[BBOX-172] 盒\n[BBOX-173] 3\n[BBOX-174] 237.16814159292\n[BBOX-175] 711.50\n[BBOX-176] 13%\n[BBOX-177] 92.50\n[BBOX-178] 吸入气雾剂\n[BBOX-179] g:120揿\n[BBOX-180] *化学药品制剂*布地格福\n[BBOX-181] 160ug:7.2ug/4.8u\n[BBOX-182] 盒\n[BBOX-183] 3\n[BBOX-184] 237.16814159292\n[BBOX-185] 711.50\n[BBOX-186] 13%\n[BBOX-187] 92.50\n[BBOX-188] 吸入气雾剂\n[BBOX-189] g:120揿\n[BBOX-190] 合计\n[BBOX-191] ￥1423.00\n[BBOX-192] ￥185.00\n[BBOX-193] 价税合计（大写）\n[BBOX-194] 壹仟陆佰零捌圆整\n[BBOX-195] (小写) ￥1608.00\n[BBOX-196] 备注\n[BBOX-197] 开票人：刘惠"
  }
]
2026-08-05 06:12:30,165 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T06:12:30.164+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 25, "failed": 0, "current": {"8c1d03f4909411f1a3da71efcdd7cc1f": {"id": "8c1d03f4909411f1a3da71efcdd7cc1f", "doc_id": "8b75f8fc909411f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHYH.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHYH.pdf", "size": 10529267, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785910310550, "task_type": "dataflow", "root_trace_id": "5845aea086174457a53e2c12052f4abe", "root_traceparent": "00-5845aea086174457a53e2c12052f4abe-577ba8815fd96dc1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 06:12:33,662 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 06:12:33,675 INFO     29 [SmartSplitter] SmartSplitter done: 6 chunks from 6 LLM segments (all bbox_id). Types: {'OutpatientRecord': 2, 'MedicationRecord': 4}
2026-08-05 06:12:33,682 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-05 06:12:33,683 INFO     29 [Trace] task=8c1d03f4 | doc=麦济ZHYH.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "198 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 2, 'MedicationRecord': 4}"}
2026-08-05 06:12:33,683 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-05 06:12:33,683 INFO     29 [ChunkRouter] Routed 6 chunks into 2 groups: {'chunks_Clinical': 2, 'chunks_Medication': 4}
2026-08-05 06:12:33,690 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-05 06:12:33,691 INFO     29 [Trace] task=8c1d03f4 | doc=麦济ZHYH.pdf | ChunkRouter:Router | outputs={"html": "", "json": "198 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 2, 'MedicationRecord': 4}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-05 06:12:33,691 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-05 06:12:33,695 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:12:33,695 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m06:12:33 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:12:33,696 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:12:34,526 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:12:34,535 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-05 06:12:34,535 INFO     29 [Trace] task=8c1d03f4 | doc=麦济ZHYH.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "198 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-05 06:12:34,535 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-05 06:12:34,544 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:12:34,544 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m06:12:34 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:12:34,545 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:12:35,509 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:12:35,513 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-05 06:12:35,513 INFO     29 [Trace] task=8c1d03f4 | doc=麦济ZHYH.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "198 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-05 06:12:35,513 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-05 06:12:35,518 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 06:12:35,518 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 06:12:35,518 INFO     29 [qwen-vl-text] positions(29): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 06:12:35,518 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [29]
2026-08-05 06:12:35,927 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 06:12:35,928 INFO     29 [qwen-vl-text] LLM extraction start, text_len=388
2026-08-05 06:12:35,929 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:12:35,930 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 28, \"encounter_dates\": [\"2026-02-13\"], \"department\": \"呼吸内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "内蒙古医科大学附属医院门诊病历\n姓名：\n年龄：62岁\n诊疗号：0014498780\n民族：\n性别：男性\n呼吸内科门诊\n联系电话：\n1 身份证：\n病情：\n就诊状态：\n就诊时间：2026-02-13 09:14\n生命体征（需要时）：\n体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg\n主诉：哮喘史，近3天呼吸困难加重，夜间咳嗽明显\n现病史：哮喘史，近3天呼吸困难加重，夜间咳嗽明显\n既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎\n无，吸烟史无，无过敏史。\n体格检查：发育正常，营养良好，体型正常，双肺呼吸音清，双肺未闻及啰\n音，双下肢无水肿，体重kg。\n辅助检查：心肺\n过敏史：不详\n初步诊断（西医）：1.支气管哮喘(急性发作期)\n初步诊断（中医）：\n治疗方案：随诊\n醋酸泼尼松片<5mg>\n用量：3.000片/次\n用法：口服，一次/日，5天\n签名：",
    "role": "user"
  }
]
[92m06:12:35 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:12:35,932 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:12:38,013 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:12:38,013 INFO     29 [qwen-vl-text] LLM output (len=289):
{
  "encounter_date": "2026-02-13",
  "chief_complaint": "哮喘史，近3天呼吸困难加重，夜间咳嗽明显",
  "present_illness": "哮喘史，近3天呼吸困难加重，夜间咳嗽明显",
  "past_history": "患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎无，吸烟史无，无过敏史。",
  "diagnosis": "西医：1.支气管哮喘(急性发作期) 中医：",
  "treatment_plan": "随诊；醋酸泼尼松片<5mg> 3.000片/次 口服，一次/日，5天"
}
2026-08-05 06:12:38,013 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-13]
2026-08-05 06:12:38,017 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2155471, prompt_len=1088
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["内蒙古医科大学附属医院门诊病历", "姓名：", "年龄：62岁", "诊疗号：0014498780", "民族：", "性别：男性", "呼吸内科门诊", "联系电话：", "1 身份证：", "病情：", "就诊状态：", "就诊时间：2026-02-13 09:14", "生命体征（需要时）：", "体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg", "主诉：哮喘史，近3天呼吸困难加重，夜间咳嗽明显", "现病史：哮喘史，近3天呼吸困难加重，夜间咳嗽明显", "既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "无，吸烟史无，无过敏史。", "体格检查：发育正常，营养良好，体型正常，双肺呼吸音清，双肺未闻及啰", "音，双下肢无水肿，体重kg。", "辅助检查：心肺", "过敏史：不详", "初步诊断（西医）：1.支气管哮喘(急性发作期)", "初步诊断（中医）：", "治疗方案：随诊", "醋酸泼尼松片<5mg>", "用量：3.000片/次", "用法：口服，一次/日，5天", "签名："]

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
2026-08-05 06:12:48,917 INFO     29 [qwen-vl-text] coord API raw response (len=1666):
[
	{"text": "内蒙古医科大学附属医院门诊病历", "bbox": [288, 87, 807, 114]},
	{"text": "姓名：", "bbox": [119, 118, 175, 136]},
	{"text": "年龄：62岁", "bbox": [377, 118, 505, 137]},
	{"text": "诊疗号：0014498780", "bbox": [628, 120, 847, 139]},
	{"text": "民族：", "bbox": [119, 141, 175, 158]},
	{"text": "性别：男性", "bbox": [375, 141, 503, 158]},
	{"text": "呼吸内科门诊", "bbox": [706, 143, 849, 161]},
	{"text": "联系电话：", "bbox": [117, 164, 226, 181]},
	{"text": "1 身份证：", "bbox": [375, 164, 504, 181]},
	{"text": "病情：", "bbox": [790, 167, 849, 184]},
	{"text": "就诊状态：", "bbox": [116, 186, 225, 203]},
	{"text": "就诊时间：2026-02-13 09:14", "bbox": [359, 186, 693, 203]},
	{"text": "生命体征（需要时）：", "bbox": [117, 209, 350, 227]},
	{"text": "体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg", "bbox": [115, 233, 613, 251]},
	{"text": "主诉：哮喘史，近3天呼吸困难加重，夜间咳嗽明显", "bbox": [114, 256, 714, 275]},
	{"text": "现病史：哮喘史，近3天呼吸困难加重，夜间咳嗽明显", "bbox": [114, 280, 714, 298]},
	{"text": "既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "bbox": [112, 304, 965, 323]},
	{"text": "无，吸烟史无，无过敏史。", "bbox": [220, 328, 505, 346]},
	{"text": "体格检查：发育正常，营养良好，体型正常，双肺呼吸音清，双肺未闻及啰", "bbox": [112, 352, 935, 370]},
	{"text": "音，双下肢无水肿，体重kg。", "bbox": [246, 375, 560, 394]},
	{"text": "辅助检查：心肺", "bbox": [111, 401, 304, 419]},
	{"text": "过敏史：不详", "bbox": [112, 425, 292, 443]},
	{"text": "初步诊断（西医）：1.支气管哮喘(急性发作期)", "bbox": [112, 448, 631, 467]},
	{"text": "初步诊断（中医）：", "bbox": [112, 472, 319, 490]},
	{"text": "治疗方案：随诊", "bbox": [112, 495, 292, 513]},
	{"text": "醋酸泼尼松片<5mg>", "bbox": [110, 554, 315, 572]},
	{"text": "用量：3.000片/次", "bbox": [605, 552, 804, 571]},
	{"text": "用法：口服，一次/日，5天", "bbox": [149, 578, 443, 597]},
	{"text": "签名：", "bbox": [575, 675, 634, 693]}
]
2026-08-05 06:12:48,917 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=10.9s
2026-08-05 06:12:48,917 INFO     29 [qwen-vl-text] coord item[0]: text=内蒙古医科大学附属医院门诊病历, bbox=[288, 87, 807, 114]
2026-08-05 06:12:48,917 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[119, 118, 175, 136]
2026-08-05 06:12:48,917 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：62岁, bbox=[377, 118, 505, 137]
2026-08-05 06:12:48,917 INFO     29 [qwen-vl-text] coord item[3]: text=诊疗号：0014498780, bbox=[628, 120, 847, 139]
2026-08-05 06:12:48,917 INFO     29 [qwen-vl-text] coord item[4]: text=民族：, bbox=[119, 141, 175, 158]
2026-08-05 06:12:48,917 INFO     29 [qwen-vl-text] coord item[5]: text=性别：男性, bbox=[375, 141, 503, 158]
2026-08-05 06:12:48,917 INFO     29 [qwen-vl-text] coord item[6]: text=呼吸内科门诊, bbox=[706, 143, 849, 161]
2026-08-05 06:12:48,917 INFO     29 [qwen-vl-text] coord item[7]: text=联系电话：, bbox=[117, 164, 226, 181]
2026-08-05 06:12:48,917 INFO     29 [qwen-vl-text] coord item[8]: text=1 身份证：, bbox=[375, 164, 504, 181]
2026-08-05 06:12:48,917 INFO     29 [qwen-vl-text] coord item[9]: text=病情：, bbox=[790, 167, 849, 184]
2026-08-05 06:12:48,917 INFO     29 [qwen-vl-text] coord item[10]: text=就诊状态：, bbox=[116, 186, 225, 203]
2026-08-05 06:12:48,917 INFO     29 [qwen-vl-text] coord item[11]: text=就诊时间：2026-02-13 09:14, bbox=[359, 186, 693, 203]
2026-08-05 06:12:48,917 INFO     29 [qwen-vl-text] coord item[12]: text=生命体征（需要时）：, bbox=[117, 209, 350, 227]
2026-08-05 06:12:48,917 INFO     29 [qwen-vl-text] coord item[13]: text=体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg, bbox=[115, 233, 613, 251]
2026-08-05 06:12:48,918 INFO     29 [qwen-vl-text] coord item[14]: text=主诉：哮喘史，近3天呼吸困难加重，夜间咳嗽明显, bbox=[114, 256, 714, 275]
2026-08-05 06:12:48,918 INFO     29 [qwen-vl-text] coord item[15]: text=现病史：哮喘史，近3天呼吸困难加重，夜间咳嗽明显, bbox=[114, 280, 714, 298]
2026-08-05 06:12:48,918 INFO     29 [qwen-vl-text] coord item[16]: text=既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎, bbox=[112, 304, 965, 323]
2026-08-05 06:12:48,918 INFO     29 [qwen-vl-text] coord item[17]: text=无，吸烟史无，无过敏史。, bbox=[220, 328, 505, 346]
2026-08-05 06:12:48,918 INFO     29 [qwen-vl-text] coord item[18]: text=体格检查：发育正常，营养良好，体型正常，双肺呼吸音清，双肺未闻及啰, bbox=[112, 352, 935, 370]
2026-08-05 06:12:48,918 INFO     29 [qwen-vl-text] coord item[19]: text=音，双下肢无水肿，体重kg。, bbox=[246, 375, 560, 394]
2026-08-05 06:12:48,918 INFO     29 [qwen-vl-text] coord item[20]: text=辅助检查：心肺, bbox=[111, 401, 304, 419]
2026-08-05 06:12:48,918 INFO     29 [qwen-vl-text] coord item[21]: text=过敏史：不详, bbox=[112, 425, 292, 443]
2026-08-05 06:12:48,918 INFO     29 [qwen-vl-text] coord item[22]: text=初步诊断（西医）：1.支气管哮喘(急性发作期), bbox=[112, 448, 631, 467]
2026-08-05 06:12:48,918 INFO     29 [qwen-vl-text] coord item[23]: text=初步诊断（中医）：, bbox=[112, 472, 319, 490]
2026-08-05 06:12:48,918 INFO     29 [qwen-vl-text] coord item[24]: text=治疗方案：随诊, bbox=[112, 495, 292, 513]
2026-08-05 06:12:48,918 INFO     29 [qwen-vl-text] coord item[25]: text=醋酸泼尼松片<5mg>, bbox=[110, 554, 315, 572]
2026-08-05 06:12:48,918 INFO     29 [qwen-vl-text] coord item[26]: text=用量：3.000片/次, bbox=[605, 552, 804, 571]
2026-08-05 06:12:48,918 INFO     29 [qwen-vl-text] coord item[27]: text=用法：口服，一次/日，5天, bbox=[149, 578, 443, 597]
2026-08-05 06:12:48,918 INFO     29 [qwen-vl-text] coord item[28]: text=签名：, bbox=[575, 675, 634, 693]
2026-08-05 06:12:48,918 INFO     29 [qwen-vl-text] page=0 — 29/29 coords, api_time=10.9s
2026-08-05 06:12:48,918 INFO     29 [qwen-vl-text] new_positions (29):
[[0, 171.35999999999999, 480.16499999999996, 73.25399999999999, 95.988], [0, 70.80499999999999, 104.125, 99.356, 114.512], [0, 224.315, 300.47499999999997, 99.356, 115.354], [0, 373.65999999999997, 503.965, 101.03999999999999, 117.038], [0, 70.80499999999999, 104.125, 118.722, 133.036], [0, 223.125, 299.28499999999997, 118.722, 133.036], [0, 420.07, 505.155, 120.40599999999999, 135.56199999999998], [0, 69.615, 134.47, 138.088, 152.402], [0, 223.125, 299.88, 138.088, 152.402], [0, 470.04999999999995, 505.155, 140.614, 154.928], [0, 69.02, 133.875, 156.612, 170.926], [0, 213.605, 412.335, 156.612, 170.926], [0, 69.615, 208.25, 175.97799999999998, 191.134], [0, 68.425, 364.73499999999996, 196.186, 211.34199999999998], [0, 67.83, 424.83, 215.552, 231.54999999999998], [0, 67.83, 424.83, 235.76, 250.916], [0, 66.64, 574.175, 255.968, 271.966], [0, 130.9, 300.47499999999997, 276.176, 291.332], [0, 66.64, 556.3249999999999, 296.384, 311.53999999999996], [0, 146.37, 333.2, 315.75, 331.748], [0, 66.045, 180.88, 337.642, 352.798], [0, 66.64, 173.73999999999998, 357.84999999999997, 373.006], [0, 66.64, 375.445, 377.216, 393.214], [0, 66.64, 189.80499999999998, 397.424, 412.58], [0, 66.64, 173.73999999999998, 416.78999999999996, 431.94599999999997], [0, 65.45, 187.42499999999998, 466.46799999999996, 481.62399999999997], [0, 359.97499999999997, 478.38, 464.784, 480.782], [0, 88.655, 263.585, 486.676, 502.674], [0, 342.125, 377.22999999999996, 568.35, 583.506]]
2026-08-05 06:12:48,919 INFO     29 [qwen-vl-text] ═══ DONE ═══ 29 positions, pages=1, time=13.4s
2026-08-05 06:12:48,919 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 06:12:48,919 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 06:12:48,919 INFO     29 [qwen-vl-text] positions(23): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 06:12:48,919 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [23]
2026-08-05 06:12:49,443 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 06:12:49,444 INFO     29 [qwen-vl-text] LLM extraction start, text_len=403
2026-08-05 06:12:49,444 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:12:49,445 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 127, \"bbox_end\": 149, \"encounter_dates\": [\"2024-12-10\"], \"department\": \"呼吸内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录:\n病历信息 □痕迹 □批注 置未 ▼ 状态:只读-仅供查看 120% >\n内蒙古医科大学附属医院门诊病历\n姓名 龄:60岁 诊疗号:0014498780\n民族: 别: 男性 科室:呼吸内科门诊\n联系电话: 身份证:1 病情:\n就诊状态: 就诊时间: 2024-12-10 12:37\n生命体征(需要时):\n体温:℃ 脉搏:次/分 呼吸:次/分 血压:/mmHg\n主诉:SSSJ项目肺功能检查开单\n现病史: 哮喘\n既往史: 患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎\n无,吸烟史无,无过敏史。\n体格检查: 发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰\n音,双下肢无水肿,体重kg。\n辅助检查:\n初步诊断(西医): 1.哮喘\n初步诊断(中医):\n治疗方案:/\n呼吸过滤器 肺通气功能检查\n用量:\n用法:\n签名:崔丽英",
    "role": "user"
  }
]
[92m06:12:49 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:12:49,446 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:12:54,872 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:12:54,873 INFO     29 [qwen-vl-text] LLM output (len=233):
{
  "encounter_date": "2024-12-10",
  "chief_complaint": "SSSJ项目肺功能检查开单",
  "present_illness": "哮喘",
  "past_history": "患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎无,吸烟史无,无过敏史。",
  "diagnosis": "西医：1.哮喘 中医：",
  "treatment_plan": "呼吸过滤器 肺通气功能检查"
}
2026-08-05 06:12:54,873 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-12-10]
2026-08-05 06:12:54,892 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7824738, prompt_len=1085
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录:", "病历信息 □痕迹 □批注 置未 ▼ 状态:只读-仅供查看 120% >", "内蒙古医科大学附属医院门诊病历", "姓名 龄:60岁 诊疗号:0014498780", "民族: 别: 男性 科室:呼吸内科门诊", "联系电话: 身份证:1 病情:", "就诊状态: 就诊时间: 2024-12-10 12:37", "生命体征(需要时):", "体温:℃ 脉搏:次/分 呼吸:次/分 血压:/mmHg", "主诉:SSSJ项目肺功能检查开单", "现病史: 哮喘", "既往史: 患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎", "无,吸烟史无,无过敏史。", "体格检查: 发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰", "音,双下肢无水肿,体重kg。", "辅助检查:", "初步诊断(西医): 1.哮喘", "初步诊断(中医):", "治疗方案:/", "呼吸过滤器 肺通气功能检查", "用量:", "用法:", "签名:崔丽英"]

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
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord API raw response (len=1400):
[
	{"text": "报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录:", "bbox": [60, 91, 864, 130]},
	{"text": "病历信息 □痕迹 □批注 置未 ▼ 状态:只读-仅供查看 120% >", "bbox": [6, 128, 948, 175]},
	{"text": "内蒙古医科大学附属医院门诊病历", "bbox": [248, 185, 748, 219]},
	{"text": "姓名 龄:60岁 诊疗号:0014498780", "bbox": [93, 225, 780, 256]},
	{"text": "民族: 别: 男性 科室:呼吸内科门诊", "bbox": [95, 258, 783, 289]},
	{"text": "联系电话: 身份证:1 病情:", "bbox": [95, 290, 780, 320]},
	{"text": "就诊状态: 就诊时间: 2024-12-10 12:37", "bbox": [95, 323, 634, 348]},
	{"text": "生命体征(需要时):", "bbox": [97, 349, 318, 370]},
	{"text": "体温:℃ 脉搏:次/分 呼吸:次/分 血压:/mmHg", "bbox": [97, 370, 563, 393]},
	{"text": "主诉:SSSJ项目肺功能检查开单", "bbox": [97, 390, 454, 412]},
	{"text": "现病史: 哮喘", "bbox": [97, 412, 244, 433]},
	{"text": "既往史: 患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎", "bbox": [97, 434, 884, 458]},
	{"text": "无,吸烟史无,无过敏史。", "bbox": [199, 456, 465, 476]},
	{"text": "体格检查: 发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰", "bbox": [97, 476, 857, 499]},
	{"text": "音,双下肢无水肿,体重kg。", "bbox": [224, 497, 511, 517]},
	{"text": "辅助检查:", "bbox": [97, 518, 199, 537]},
	{"text": "初步诊断(西医): 1.哮喘", "bbox": [97, 538, 380, 560]},
	{"text": "初步诊断(中医):", "bbox": [97, 559, 298, 580]},
	{"text": "治疗方案:/", "bbox": [97, 580, 215, 601]},
	{"text": "呼吸过滤器 肺通气功能检查", "bbox": [100, 617, 525, 638]},
	{"text": "用量:", "bbox": [571, 637, 622, 655]},
	{"text": "用法:", "bbox": [147, 655, 200, 673]},
	{"text": "签名:崔丽英", "bbox": [537, 742, 658, 761]}
]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=10.6s
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[0]: text=报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录:, bbox=[60, 91, 864, 130]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[1]: text=病历信息 □痕迹 □批注 置未 ▼ 状态:只读-仅供查看 120% >, bbox=[6, 128, 948, 175]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[2]: text=内蒙古医科大学附属医院门诊病历, bbox=[248, 185, 748, 219]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[3]: text=姓名 龄:60岁 诊疗号:0014498780, bbox=[93, 225, 780, 256]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[4]: text=民族: 别: 男性 科室:呼吸内科门诊, bbox=[95, 258, 783, 289]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[5]: text=联系电话: 身份证:1 病情:, bbox=[95, 290, 780, 320]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[6]: text=就诊状态: 就诊时间: 2024-12-10 12:37, bbox=[95, 323, 634, 348]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[7]: text=生命体征(需要时):, bbox=[97, 349, 318, 370]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[8]: text=体温:℃ 脉搏:次/分 呼吸:次/分 血压:/mmHg, bbox=[97, 370, 563, 393]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[9]: text=主诉:SSSJ项目肺功能检查开单, bbox=[97, 390, 454, 412]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[10]: text=现病史: 哮喘, bbox=[97, 412, 244, 433]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[11]: text=既往史: 患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎, bbox=[97, 434, 884, 458]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[12]: text=无,吸烟史无,无过敏史。, bbox=[199, 456, 465, 476]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[13]: text=体格检查: 发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰, bbox=[97, 476, 857, 499]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[14]: text=音,双下肢无水肿,体重kg。, bbox=[224, 497, 511, 517]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[15]: text=辅助检查:, bbox=[97, 518, 199, 537]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[16]: text=初步诊断(西医): 1.哮喘, bbox=[97, 538, 380, 560]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[17]: text=初步诊断(中医):, bbox=[97, 559, 298, 580]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[18]: text=治疗方案:/, bbox=[97, 580, 215, 601]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[19]: text=呼吸过滤器 肺通气功能检查, bbox=[100, 617, 525, 638]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[20]: text=用量:, bbox=[571, 637, 622, 655]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[21]: text=用法:, bbox=[147, 655, 200, 673]
2026-08-05 06:13:05,463 INFO     29 [qwen-vl-text] coord item[22]: text=签名:崔丽英, bbox=[537, 742, 658, 761]
2026-08-05 06:13:05,464 INFO     29 [qwen-vl-text] page=4 — 23/23 coords, api_time=10.6s
2026-08-05 06:13:05,464 INFO     29 [qwen-vl-text] new_positions (23):
[[4, 35.699999999999996, 514.0799999999999, 76.622, 109.46], [4, 3.57, 564.06, 107.776, 147.35], [4, 147.56, 445.06, 155.76999999999998, 184.398], [4, 55.335, 464.09999999999997, 189.45, 215.552], [4, 56.525, 465.885, 217.236, 243.338], [4, 56.525, 464.09999999999997, 244.17999999999998, 269.44], [4, 56.525, 377.22999999999996, 271.966, 293.01599999999996], [4, 57.714999999999996, 189.20999999999998, 293.858, 311.53999999999996], [4, 57.714999999999996, 334.98499999999996, 311.53999999999996, 330.906], [4, 57.714999999999996, 270.13, 328.38, 346.904], [4, 57.714999999999996, 145.18, 346.904, 364.586], [4, 57.714999999999996, 525.98, 365.428, 385.63599999999997], [4, 118.405, 276.675, 383.952, 400.792], [4, 57.714999999999996, 509.91499999999996, 400.792, 420.15799999999996], [4, 133.28, 304.04499999999996, 418.474, 435.31399999999996], [4, 57.714999999999996, 118.405, 436.156, 452.154], [4, 57.714999999999996, 226.1, 452.996, 471.52], [4, 57.714999999999996, 177.31, 470.678, 488.35999999999996], [4, 57.714999999999996, 127.925, 488.35999999999996, 506.042], [4, 59.5, 312.375, 519.514, 537.196], [4, 339.745, 370.09, 536.3539999999999, 551.51], [4, 87.46499999999999, 119.0, 551.51, 566.6659999999999], [4, 319.515, 391.51, 624.764, 640.762]]
2026-08-05 06:13:05,465 INFO     29 [qwen-vl-text] ═══ DONE ═══ 23 positions, pages=1, time=16.5s
2026-08-05 06:13:05,476 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-05 06:13:05,476 INFO     29 [Trace] task=8c1d03f4 | doc=麦济ZHYH.pdf | Extractor:Clinical | outputs={"chunks": "2 items, types={'OutpatientRecord': 2}", "html": "", "json": "198 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-05 06:13:05,476 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-05 06:13:05,477 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T06:13:05.477+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 25, "failed": 0, "current": {"8c1d03f4909411f1a3da71efcdd7cc1f": {"id": "8c1d03f4909411f1a3da71efcdd7cc1f", "doc_id": "8b75f8fc909411f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHYH.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHYH.pdf", "size": 10529267, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785910310550, "task_type": "dataflow", "root_trace_id": "5845aea086174457a53e2c12052f4abe", "root_traceparent": "00-5845aea086174457a53e2c12052f4abe-577ba8815fd96dc1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 06:13:05,483 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 06:13:05,483 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 06:13:05,483 INFO     29 [qwen-vl-text] positions(25): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 06:13:05,483 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [25]
2026-08-05 06:13:05,729 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 06:13:05,730 INFO     29 [qwen-vl-text] LLM extraction start, text_len=183
2026-08-05 06:13:05,730 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:13:05,730 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 29, \"bbox_end\": 53, \"encounter_dates\": [\"2025-11-18\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "萱堂大药房\n单号：2025111853212\n日期：25/11/18\n时间：13:2\n工号：001\n品名\n规格\n厂家\n金额\n数量\n总计\n布地格福吸入气雾剂\n60ug/7.2ug/4.8ug 吸\n120 撤/支\n支/盒\n219.00\n3\n657.00\n合计：657.00\n应收：657.00\n数量：3\n实收：657.00\n会员：\n药品属于特殊商品\n无质量问题，概不退换",
    "role": "user"
  }
]
[92m06:13:05 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:13:05,732 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:13:09,000 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:13:09,000 INFO     29 [qwen-vl-text] LLM output (len=432):
{
  "encounter_date": "2025-11-18",
  "pharmacy": "萱堂大药房",
  "medications": [
    {
      "name": "布地格福吸入气雾剂",
      "specification": "60ug/7.2ug/4.8ug 吸, 120撤/支",
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
2026-08-05 06:13:09,000 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-18]
2026-08-05 06:13:09,005 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1978583, prompt_len=871
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
2026-08-05 06:13:16,608 INFO     29 [qwen-vl-text] coord API raw response (len=1286):
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
	{"text": "合计：657.00", "bbox": [214, 647, 460, 678]},
	{"text": "应收：657.00", "bbox": [214, 685, 460, 715]},
	{"text": "数量：3", "bbox": [214, 725, 361, 757]},
	{"text": "实收：657.00", "bbox": [214, 773, 462, 805]},
	{"text": "会员：", "bbox": [214, 823, 311, 855]},
	{"text": "药品属于特殊商品", "bbox": [217, 871, 555, 904]},
	{"text": "无质量问题，概不退换", "bbox": [219, 920, 642, 953]}
]
2026-08-05 06:13:16,608 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=7.6s
2026-08-05 06:13:16,608 INFO     29 [qwen-vl-text] coord item[0]: text=萱堂大药房, bbox=[364, 153, 658, 199]
2026-08-05 06:13:16,609 INFO     29 [qwen-vl-text] coord item[1]: text=单号：2025111853212, bbox=[212, 248, 614, 288]
2026-08-05 06:13:16,609 INFO     29 [qwen-vl-text] coord item[2]: text=日期：25/11/18, bbox=[212, 297, 484, 335]
2026-08-05 06:13:16,609 INFO     29 [qwen-vl-text] coord item[3]: text=时间：13:2, bbox=[570, 305, 807, 338]
2026-08-05 06:13:16,609 INFO     29 [qwen-vl-text] coord item[4]: text=工号：001, bbox=[212, 348, 400, 382]
2026-08-05 06:13:16,609 INFO     29 [qwen-vl-text] coord item[5]: text=品名, bbox=[212, 398, 294, 430]
2026-08-05 06:13:16,609 INFO     29 [qwen-vl-text] coord item[6]: text=规格, bbox=[374, 403, 462, 435]
2026-08-05 06:13:16,609 INFO     29 [qwen-vl-text] coord item[7]: text=厂家, bbox=[542, 405, 628, 437]
2026-08-05 06:13:16,609 INFO     29 [qwen-vl-text] coord item[8]: text=金额, bbox=[732, 406, 810, 438]
2026-08-05 06:13:16,609 INFO     29 [qwen-vl-text] coord item[9]: text=数量, bbox=[212, 447, 292, 479]
2026-08-05 06:13:16,609 INFO     29 [qwen-vl-text] coord item[10]: text=总计, bbox=[382, 452, 468, 483]
2026-08-05 06:13:16,609 INFO     29 [qwen-vl-text] coord item[11]: text=布地格福吸入气雾剂, bbox=[212, 490, 810, 530]
2026-08-05 06:13:16,609 INFO     29 [qwen-vl-text] coord item[12]: text=60ug/7.2ug/4.8ug 吸, bbox=[224, 530, 590, 569]
2026-08-05 06:13:16,609 INFO     29 [qwen-vl-text] coord item[13]: text=120 撤/支, bbox=[642, 536, 810, 569]
2026-08-05 06:13:16,609 INFO     29 [qwen-vl-text] coord item[14]: text=支/盒, bbox=[237, 568, 338, 601]
2026-08-05 06:13:16,609 INFO     29 [qwen-vl-text] coord item[15]: text=219.00, bbox=[214, 609, 327, 637]
2026-08-05 06:13:16,609 INFO     29 [qwen-vl-text] coord item[16]: text=3, bbox=[414, 612, 437, 638]
2026-08-05 06:13:16,610 INFO     29 [qwen-vl-text] coord item[17]: text=657.00, bbox=[546, 613, 664, 640]
2026-08-05 06:13:16,610 INFO     29 [qwen-vl-text] coord item[18]: text=合计：657.00, bbox=[214, 647, 460, 678]
2026-08-05 06:13:16,610 INFO     29 [qwen-vl-text] coord item[19]: text=应收：657.00, bbox=[214, 685, 460, 715]
2026-08-05 06:13:16,610 INFO     29 [qwen-vl-text] coord item[20]: text=数量：3, bbox=[214, 725, 361, 757]
2026-08-05 06:13:16,610 INFO     29 [qwen-vl-text] coord item[21]: text=实收：657.00, bbox=[214, 773, 462, 805]
2026-08-05 06:13:16,610 INFO     29 [qwen-vl-text] coord item[22]: text=会员：, bbox=[214, 823, 311, 855]
2026-08-05 06:13:16,610 INFO     29 [qwen-vl-text] coord item[23]: text=药品属于特殊商品, bbox=[217, 871, 555, 904]
2026-08-05 06:13:16,610 INFO     29 [qwen-vl-text] coord item[24]: text=无质量问题，概不退换, bbox=[219, 920, 642, 953]
2026-08-05 06:13:16,611 INFO     29 [qwen-vl-text] page=1 — 25/25 coords, api_time=7.6s
2026-08-05 06:13:16,612 INFO     29 [qwen-vl-text] new_positions (25):
[[1, 216.57999999999998, 391.51, 128.826, 167.558], [1, 126.14, 365.33, 208.816, 242.49599999999998], [1, 126.14, 287.97999999999996, 250.07399999999998, 282.07], [1, 339.15, 480.16499999999996, 256.81, 284.596], [1, 126.14, 238.0, 293.01599999999996, 321.644], [1, 126.14, 174.92999999999998, 335.116, 362.06], [1, 222.53, 274.89, 339.32599999999996, 366.27], [1, 322.49, 373.65999999999997, 341.01, 367.954], [1, 435.53999999999996, 481.95, 341.852, 368.796], [1, 126.14, 173.73999999999998, 376.37399999999997, 403.318], [1, 227.29, 278.46, 380.584, 406.686], [1, 126.14, 481.95, 412.58, 446.26], [1, 133.28, 351.05, 446.26, 479.09799999999996], [1, 381.99, 481.95, 451.312, 479.09799999999996], [1, 141.015, 201.10999999999999, 478.256, 506.042], [1, 127.33, 194.565, 512.778, 536.3539999999999], [1, 246.32999999999998, 260.015, 515.304, 537.196], [1, 324.87, 395.08, 516.146, 538.88], [1, 127.33, 273.7, 544.774, 570.876], [1, 127.33, 273.7, 576.77, 602.03], [1, 127.33, 214.795, 610.4499999999999, 637.394], [1, 127.33, 274.89, 650.866, 677.81], [1, 127.33, 185.045, 692.966, 719.91], [1, 129.11499999999998, 330.22499999999997, 733.382, 761.168], [1, 130.305, 381.99, 774.64, 802.4259999999999]]
2026-08-05 06:13:16,612 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=11.1s
2026-08-05 06:13:16,612 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 06:13:16,613 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 06:13:16,613 INFO     29 [qwen-vl-text] positions(37): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 06:13:16,613 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [37]
2026-08-05 06:13:16,782 INFO     29 [qwen-vl-text] page=2, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 06:13:16,783 INFO     29 [qwen-vl-text] LLM extraction start, text_len=327
2026-08-05 06:13:16,784 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:13:16,784 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 54, \"bbox_end\": 90, \"encounter_dates\": [\"2025-08-20\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "电子发票(普通发票)\n国家税务总局\n江苏省税务局\n发票号码：25322000000382591347\n开票日期：2025年08月20日\n购买方信息\n名称：\n统一社会信用代码/纳税人识别号：\n销售方信息\n名称：无锡邻医大药房有限公司\n统一社会信用代码/纳税人识别号：91320214MA228F680W\n项目名称\n规格型号\n单位\n数量\n单价\n金额\n税率/征收率\n税额\n*化学药品制剂*倍择瑞令\n160μg/7.2μg/4\n盒\n3\n210.029498522124\n630.09\n13%\n81.91\n畅布地格福吸入气雾剂\n.8μg*120揿\n合计\n￥630.09\n￥81.91\n价税合计（大写）\n柒佰壹拾贰圆整\n(小写) ￥712.00\n备注\n开票人：奚澳琼",
    "role": "user"
  }
]
[92m06:13:16 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:13:16,785 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:13:20,162 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:13:20,162 INFO     29 [qwen-vl-text] LLM output (len=449):
{
  "encounter_date": "2025-08-20",
  "pharmacy": "无锡邻医大药房有限公司",
  "medications": [
    {
      "name": "倍择瑞令畅布地格福吸入气雾剂",
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
2026-08-05 06:13:20,162 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-08-20]
2026-08-05 06:13:20,164 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=931127, prompt_len=1051
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
2026-08-05 06:13:39,776 INFO     29 [qwen-vl-text] coord API raw response (len=3203):
[
	{"text": "电子发票(普通发票)", "bbox": [327, 103, 637, 148]},
	{"text": "国家税务总局", "bbox": [463, 155, 534, 172], "bbox_2d": [463, 155, 534, 172]},
	{"text": "江苏省税务局", "bbox": [463, 187, 537, 210], "bbox_2d": [463, 187, 537, 210]},
	{"text": "发票号码：25322000000382591347", "bbox": [733, 122, 948, 143], "bbox_2d": [733, 122, 948, 143]},
	{"text": "开票日期：2025年08月20日", "bbox": [733, 161, 909, 182], "bbox_2d": [733, 161, 909, 182]},
	{"text": "购买方信息", "bbox": [32, 265, 46, 380], "bbox_2d": [32, 265, 46, 380]},
	{"text": "名称：", "bbox": [59, 282, 194, 302], "bbox_2d": [59, 282, 194, 302]},
	{"text": "统一社会信用代码/纳税人识别号：", "bbox": [59, 346, 258, 366], "bbox_2d": [59, 346, 258, 366]},
	{"text": "销售方信息", "bbox": [507, 265, 521, 380], "bbox_2d": [507, 265, 521, 380]},
	{"text": "名称：无锡邻医大药房有限公司", "bbox": [536, 277, 740, 298], "bbox_2d": [536, 277, 740, 298]},
	{"text": "统一社会信用代码/纳税人识别号：91320214MA228F680W", "bbox": [535, 341, 954, 364], "bbox_2d": [535, 341, 954, 364]},
	{"text": "项目名称", "bbox": [77, 402, 136, 421], "bbox_2d": [77, 402, 136, 421]},
	{"text": "规格型号", "bbox": [199, 402, 258, 421], "bbox_2d": [199, 402, 258, 421]},
	{"text": "单位", "bbox": [319, 402, 363, 421], "bbox_2d": [319, 402, 363, 421]},
	{"text": "数量", "bbox": [442, 402, 486, 421], "bbox_2d": [442, 402, 486, 421]},
	{"text": "单价", "bbox": [558, 402, 602, 421], "bbox_2d": [558, 402, 602, 421]},
	{"text": "金额", "bbox": [680, 402, 724, 421], "bbox_2d": [680, 402, 724, 421]},
	{"text": "税率/征收率", "bbox": [744, 402, 826, 421], "bbox_2d": [744, 402, 826, 421]},
	{"text": "税额", "bbox": [924, 402, 968, 421], "bbox_2d": [924, 402, 968, 421]},
	{"text": "*化学药品制剂*倍择瑞令", "bbox": [26, 427, 187, 449], "bbox_2d": [26, 427, 187, 449]},
	{"text": "160μg/7.2μg/4", "bbox": [200, 427, 301, 451], "bbox_2d": [200, 427, 301, 451]},
	{"text": "盒", "bbox": [333, 427, 349, 449], "bbox_2d": [333, 427, 349, 449]},
	{"text": "3", "bbox": [477, 427, 487, 449], "bbox_2d": [477, 427, 487, 449]},
	{"text": "210.029498522124", "bbox": [493, 427, 602, 449], "bbox_2d": [493, 427, 602, 449]},
	{"text": "630.09", "bbox": [684, 427, 722, 449], "bbox_2d": [684, 427, 722, 449]},
	{"text": "13%", "bbox": [778, 427, 803, 449], "bbox_2d": [778, 427, 803, 449]},
	{"text": "81.91", "bbox": [937, 427, 968, 449], "bbox_2d": [937, 427, 968, 449]},
	{"text": "畅布地格福吸入气雾剂", "bbox": [26, 457, 178, 479], "bbox_2d": [26, 457, 178, 479]},
	{"text": ".8μg*120揿", "bbox": [200, 457, 280, 481], "bbox_2d": [200, 457, 280, 481]},
	{"text": "合计", "bbox": [101, 673, 114, 691], "bbox_2d": [101, 673, 114, 691]},
	{"text": "计", "bbox": [174, 673, 188, 691], "bbox_2d": [174, 673, 188, 691]},
	{"text": "￥630.09", "bbox": [672, 670, 722, 689], "bbox_2d": [672, 670, 722, 689]},
	{"text": "￥81.91", "bbox": [925, 670, 968, 689], "bbox_2d": [925, 670, 968, 689]},
	{"text": "价税合计（大写）", "bbox": [84, 715, 194, 735], "bbox_2d": [84, 715, 194, 735]},
	{"text": "柒佰壹拾贰圆整", "bbox": [301, 710, 408, 733], "bbox_2d": [301, 710, 408, 733]},
	{"text": "(小写) ￥712.00", "bbox": [690, 709, 811, 733], "bbox_2d": [690, 709, 811, 733]},
	{"text": "备注", "bbox": [32, 787, 46, 806], "bbox_2d": [32, 787, 46, 806]},
	{"text": "开票人：奚澳琼", "bbox": [95, 917, 200, 938], "bbox_2d": [95, 917, 200, 938]}
]
2026-08-05 06:13:39,777 INFO     29 [qwen-vl-text] coord API: raw_items=38, valid_items=38, elapsed=19.6s
2026-08-05 06:13:39,777 INFO     29 [qwen-vl-text] coord item[0]: text=电子发票(普通发票), bbox=[327, 103, 637, 148]
2026-08-05 06:13:39,777 INFO     29 [qwen-vl-text] coord item[1]: text=国家税务总局, bbox=[463, 155, 534, 172]
2026-08-05 06:13:39,777 INFO     29 [qwen-vl-text] coord item[2]: text=江苏省税务局, bbox=[463, 187, 537, 210]
2026-08-05 06:13:39,777 INFO     29 [qwen-vl-text] coord item[3]: text=发票号码：25322000000382591347, bbox=[733, 122, 948, 143]
2026-08-05 06:13:39,777 INFO     29 [qwen-vl-text] coord item[4]: text=开票日期：2025年08月20日, bbox=[733, 161, 909, 182]
2026-08-05 06:13:39,777 INFO     29 [qwen-vl-text] coord item[5]: text=购买方信息, bbox=[32, 265, 46, 380]
2026-08-05 06:13:39,777 INFO     29 [qwen-vl-text] coord item[6]: text=名称：, bbox=[59, 282, 194, 302]
2026-08-05 06:13:39,777 INFO     29 [qwen-vl-text] coord item[7]: text=统一社会信用代码/纳税人识别号：, bbox=[59, 346, 258, 366]
2026-08-05 06:13:39,777 INFO     29 [qwen-vl-text] coord item[8]: text=销售方信息, bbox=[507, 265, 521, 380]
2026-08-05 06:13:39,777 INFO     29 [qwen-vl-text] coord item[9]: text=名称：无锡邻医大药房有限公司, bbox=[536, 277, 740, 298]
2026-08-05 06:13:39,777 INFO     29 [qwen-vl-text] coord item[10]: text=统一社会信用代码/纳税人识别号：91320214MA228F680W, bbox=[535, 341, 954, 364]
2026-08-05 06:13:39,777 INFO     29 [qwen-vl-text] coord item[11]: text=项目名称, bbox=[77, 402, 136, 421]
2026-08-05 06:13:39,777 INFO     29 [qwen-vl-text] coord item[12]: text=规格型号, bbox=[199, 402, 258, 421]
2026-08-05 06:13:39,777 INFO     29 [qwen-vl-text] coord item[13]: text=单位, bbox=[319, 402, 363, 421]
2026-08-05 06:13:39,778 INFO     29 [qwen-vl-text] coord item[14]: text=数量, bbox=[442, 402, 486, 421]
2026-08-05 06:13:39,778 INFO     29 [qwen-vl-text] coord item[15]: text=单价, bbox=[558, 402, 602, 421]
2026-08-05 06:13:39,778 INFO     29 [qwen-vl-text] coord item[16]: text=金额, bbox=[680, 402, 724, 421]
2026-08-05 06:13:39,778 INFO     29 [qwen-vl-text] coord item[17]: text=税率/征收率, bbox=[744, 402, 826, 421]
2026-08-05 06:13:39,778 INFO     29 [qwen-vl-text] coord item[18]: text=税额, bbox=[924, 402, 968, 421]
2026-08-05 06:13:39,778 INFO     29 [qwen-vl-text] coord item[19]: text=*化学药品制剂*倍择瑞令, bbox=[26, 427, 187, 449]
2026-08-05 06:13:39,778 INFO     29 [qwen-vl-text] coord item[20]: text=160μg/7.2μg/4, bbox=[200, 427, 301, 451]
2026-08-05 06:13:39,778 INFO     29 [qwen-vl-text] coord item[21]: text=盒, bbox=[333, 427, 349, 449]
2026-08-05 06:13:39,778 INFO     29 [qwen-vl-text] coord item[22]: text=3, bbox=[477, 427, 487, 449]
2026-08-05 06:13:39,778 INFO     29 [qwen-vl-text] coord item[23]: text=210.029498522124, bbox=[493, 427, 602, 449]
2026-08-05 06:13:39,778 INFO     29 [qwen-vl-text] coord item[24]: text=630.09, bbox=[684, 427, 722, 449]
2026-08-05 06:13:39,778 INFO     29 [qwen-vl-text] coord item[25]: text=13%, bbox=[778, 427, 803, 449]
2026-08-05 06:13:39,778 INFO     29 [qwen-vl-text] coord item[26]: text=81.91, bbox=[937, 427, 968, 449]
2026-08-05 06:13:39,778 INFO     29 [qwen-vl-text] coord item[27]: text=畅布地格福吸入气雾剂, bbox=[26, 457, 178, 479]
2026-08-05 06:13:39,778 INFO     29 [qwen-vl-text] coord item[28]: text=.8μg*120揿, bbox=[200, 457, 280, 481]
2026-08-05 06:13:39,778 INFO     29 [qwen-vl-text] coord item[29]: text=合计, bbox=[101, 673, 114, 691]
2026-08-05 06:13:39,778 INFO     29 [qwen-vl-text] coord item[30]: text=计, bbox=[174, 673, 188, 691]
2026-08-05 06:13:39,778 INFO     29 [qwen-vl-text] coord item[31]: text=￥630.09, bbox=[672, 670, 722, 689]
2026-08-05 06:13:39,778 INFO     29 [qwen-vl-text] coord item[32]: text=￥81.91, bbox=[925, 670, 968, 689]
2026-08-05 06:13:39,779 INFO     29 [qwen-vl-text] coord item[33]: text=价税合计（大写）, bbox=[84, 715, 194, 735]
2026-08-05 06:13:39,779 INFO     29 [qwen-vl-text] coord item[34]: text=柒佰壹拾贰圆整, bbox=[301, 710, 408, 733]
2026-08-05 06:13:39,779 INFO     29 [qwen-vl-text] coord item[35]: text=(小写) ￥712.00, bbox=[690, 709, 811, 733]
2026-08-05 06:13:39,779 INFO     29 [qwen-vl-text] coord item[36]: text=备注, bbox=[32, 787, 46, 806]
2026-08-05 06:13:39,779 INFO     29 [qwen-vl-text] coord item[37]: text=开票人：奚澳琼, bbox=[95, 917, 200, 938]
2026-08-05 06:13:39,779 INFO     29 [qwen-vl-text] page=2 — 37/37 coords, api_time=19.6s
2026-08-05 06:13:39,779 INFO     29 [qwen-vl-text] new_positions (37):
[[2, 275.334, 536.3539999999999, 61.285, 88.06], [2, 389.846, 449.628, 92.225, 102.33999999999999], [2, 389.846, 452.154, 111.265, 124.94999999999999], [2, 617.1859999999999, 798.216, 72.59, 85.085], [2, 617.1859999999999, 765.3779999999999, 95.795, 108.28999999999999], [2, 26.944, 38.732, 157.67499999999998, 226.1], [2, 49.678, 163.34799999999998, 167.79, 179.69], [2, 49.678, 217.236, 205.87, 217.76999999999998], [2, 426.894, 438.68199999999996, 157.67499999999998, 226.1], [2, 451.312, 623.0799999999999, 164.815, 177.31], [2, 450.46999999999997, 803.2679999999999, 202.89499999999998, 216.57999999999998], [2, 64.834, 114.512, 239.19, 250.49499999999998], [2, 167.558, 217.236, 239.19, 250.49499999999998], [2, 268.598, 305.646, 239.19, 250.49499999999998], [2, 372.164, 409.212, 239.19, 250.49499999999998], [2, 469.83599999999996, 506.88399999999996, 239.19, 250.49499999999998], [2, 572.56, 609.608, 239.19, 250.49499999999998], [2, 626.448, 695.492, 239.19, 250.49499999999998], [2, 778.0079999999999, 815.0559999999999, 239.19, 250.49499999999998], [2, 21.892, 157.454, 254.065, 267.155], [2, 168.4, 253.44199999999998, 254.065, 268.34499999999997], [2, 280.38599999999997, 293.858, 254.065, 267.155], [2, 401.63399999999996, 410.054, 254.065, 267.155], [2, 415.106, 506.88399999999996, 254.065, 267.155], [2, 575.928, 607.924, 254.065, 267.155], [2, 655.076, 676.126, 254.065, 267.155], [2, 788.954, 815.0559999999999, 254.065, 267.155], [2, 21.892, 149.876, 271.91499999999996, 285.005], [2, 168.4, 235.76, 271.91499999999996, 286.195], [2, 85.042, 95.988, 400.435, 411.145], [2, 146.50799999999998, 158.296, 400.435, 411.145], [2, 565.824, 607.924, 398.65, 409.955], [2, 778.85, 815.0559999999999, 398.65, 409.955], [2, 70.728, 163.34799999999998, 425.42499999999995, 437.325], [2, 253.44199999999998, 343.536, 422.45, 436.135], [2, 580.98, 682.862, 421.85499999999996, 436.135], [2, 26.944, 38.732, 468.265, 479.57]]
2026-08-05 06:13:39,780 INFO     29 [qwen-vl-text] ═══ DONE ═══ 37 positions, pages=1, time=23.2s
2026-08-05 06:13:39,780 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 06:13:39,780 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 06:13:39,780 INFO     29 [qwen-vl-text] positions(36): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 06:13:39,780 INFO     29 [qwen-vl-text] page grouping: [3, 4], lines per page: [35, 1]
2026-08-05 06:13:39,946 INFO     29 [qwen-vl-text] page=3, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 06:13:40,447 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 06:13:40,448 INFO     29 [qwen-vl-text] LLM extraction start, text_len=373
2026-08-05 06:13:40,448 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:13:40,448 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 91, \"bbox_end\": 126, \"encounter_dates\": [\"2025-05-20\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "电子发票(普通发票)\n国家税务总局\n江苏省税务局\n发票号码：25322000000226700883\n开票日期：2025年05月20日\n购买方信息\n名称\n统一社会信用代码/纳税人识别号：\n销售方信息\n名称：无锡邻医大药房有限公司\n统一社会信用代码/纳税人识别号：91320214MA228F680W\n项目名称\n规格型号\n单位\n数量\n单价\n金额\n税率/征收率\n税额\n*化学药品制剂*倍择瑞令\n160μg/7.2μg/4\n盒\n3 210.029498522124\n630.09\n13%\n81.91\n畅布地格福吸入气雾剂\n.8μg*120揿\n合计\n￥630.09\n￥81.91\n价税合计（大写）\n柒佰壹拾贰圆整\n(小写) ￥712.00\n备注\n挂号号:D20091... 医保余额:0 CM/KG 普通病人|现住址:内蒙古土默特左旗沙尔营乡大有庄村32",
    "role": "user"
  }
]
[92m06:13:40 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:13:40,449 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:13:40,450 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T06:13:40.449+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 25, "failed": 0, "current": {"8c1d03f4909411f1a3da71efcdd7cc1f": {"id": "8c1d03f4909411f1a3da71efcdd7cc1f", "doc_id": "8b75f8fc909411f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHYH.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHYH.pdf", "size": 10529267, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785910310550, "task_type": "dataflow", "root_trace_id": "5845aea086174457a53e2c12052f4abe", "root_traceparent": "00-5845aea086174457a53e2c12052f4abe-577ba8815fd96dc1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 06:13:43,743 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:13:43,743 INFO     29 [qwen-vl-text] LLM output (len=439):
{
  "encounter_date": "2025-05-20",
  "pharmacy": "无锡邻医大药房有限公司",
  "medications": [
    {
      "name": "倍择瑞令畅布地格福吸入气雾剂",
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
2026-08-05 06:13:43,743 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-05-20]
2026-08-05 06:13:43,746 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=847478, prompt_len=1036
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["电子发票(普通发票)", "国家税务总局", "江苏省税务局", "发票号码：25322000000226700883", "开票日期：2025年05月20日", "购买方信息", "名称", "统一社会信用代码/纳税人识别号：", "销售方信息", "名称：无锡邻医大药房有限公司", "统一社会信用代码/纳税人识别号：91320214MA228F680W", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*倍择瑞令", "160μg/7.2μg/4", "盒", "3 210.029498522124", "630.09", "13%", "81.91", "畅布地格福吸入气雾剂", ".8μg*120揿", "合计", "￥630.09", "￥81.91", "价税合计（大写）", "柒佰壹拾贰圆整", "(小写) ￥712.00", "备注"]

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
2026-08-05 06:14:02,408 INFO     29 [qwen-vl-text] coord API raw response (len=2965):
[
	{"text": "电子发票(普通发票)", "bbox": [328, 123, 636, 168], "bbox": [328, 123, 636, 168]},
	{"text": "国家税务总局", "bbox": [463, 175, 534, 193], "bbox": [463, 175, 534, 193]},
	{"text": "江苏省税务局", "bbox": [463, 206, 537, 233], "bbox": [463, 206, 537, 233]},
	{"text": "发票号码：25322000000226700883", "bbox": [731, 143, 944, 164], "bbox": [731, 143, 944, 164]},
	{"text": "开票日期：2025年05月20日", "bbox": [731, 181, 905, 202], "bbox": [731, 181, 905, 202]},
	{"text": "购买方信息", "bbox": [36, 284, 50, 398], "bbox": [36, 284, 50, 398]},
	{"text": "名称", "bbox": [62, 302, 89, 321], "bbox": [62, 302, 89, 321]},
	{"text": "统一社会信用代码/纳税人识别号：", "bbox": [62, 365, 259, 384], "bbox": [62, 365, 259, 384]},
	{"text": "销售方信息", "bbox": [507, 284, 521, 398], "bbox": [507, 284, 521, 398]},
	{"text": "名称：无锡邻医大药房有限公司", "bbox": [535, 296, 738, 317], "bbox": [535, 296, 738, 317]},
	{"text": "统一社会信用代码/纳税人识别号：91320214MA228F680W", "bbox": [535, 360, 950, 382], "bbox": [535, 360, 950, 382]},
	{"text": "项目名称", "bbox": [80, 420, 139, 440], "bbox": [80, 420, 139, 440]},
	{"text": "规格型号", "bbox": [201, 420, 260, 440], "bbox": [201, 420, 260, 440]},
	{"text": "单位", "bbox": [320, 420, 364, 440], "bbox": [320, 420, 364, 440]},
	{"text": "数量", "bbox": [442, 420, 486, 440], "bbox": [442, 420, 486, 440]},
	{"text": "单价", "bbox": [557, 420, 601, 440], "bbox": [557, 420, 601, 440]},
	{"text": "金额", "bbox": [679, 420, 722, 440], "bbox": [679, 420, 722, 440]},
	{"text": "税率/征收率", "bbox": [742, 420, 823, 440], "bbox": [742, 420, 823, 440]},
	{"text": "税额", "bbox": [920, 420, 964, 440], "bbox": [920, 420, 964, 440]},
	{"text": "*化学药品制剂*倍择瑞令", "bbox": [30, 445, 190, 467], "bbox": [30, 445, 190, 467]},
	{"text": "160μg/7.2μg/4", "bbox": [203, 447, 303, 470], "bbox": [203, 447, 303, 470]},
	{"text": "盒", "bbox": [334, 447, 350, 467], "bbox": [334, 447, 350, 467]},
	{"text": "3 210.029498522124", "bbox": [477, 447, 601, 467], "bbox": [477, 447, 601, 467]},
	{"text": "630.09", "bbox": [682, 447, 720, 467], "bbox": [682, 447, 720, 467]},
	{"text": "13%", "bbox": [775, 447, 800, 467], "bbox": [775, 447, 800, 467]},
	{"text": "81.91", "bbox": [933, 447, 964, 467], "bbox": [933, 447, 964, 467]},
	{"text": "畅布地格福吸入气雾剂", "bbox": [30, 475, 180, 497], "bbox": [30, 475, 180, 497]},
	{"text": ".8μg*120揿", "bbox": [203, 475, 281, 499], "bbox": [203, 475, 281, 499]},
	{"text": "合计", "bbox": [104, 688, 117, 707], "bbox": [104, 688, 117, 707]},
	{"text": "计", "bbox": [177, 688, 190, 707], "bbox": [177, 688, 190, 707]},
	{"text": "￥630.09", "bbox": [676, 687, 720, 704], "bbox": [676, 687, 720, 704]},
	{"text": "￥81.91", "bbox": [926, 687, 964, 704], "bbox": [926, 687, 964, 704]},
	{"text": "价税合计（大写）", "bbox": [87, 730, 196, 750], "bbox": [87, 730, 196, 750]},
	{"text": "柒佰壹拾贰圆整", "bbox": [303, 725, 408, 747], "bbox": [303, 725, 408, 747]},
	{"text": "(小写) ￥712.00", "bbox": [688, 725, 808, 747], "bbox": [688, 725, 808, 747]},
	{"text": "备注", "bbox": [36, 800, 50, 859], "bbox": [36, 800, 50, 859]}
]
2026-08-05 06:14:02,409 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=18.7s
2026-08-05 06:14:02,409 INFO     29 [qwen-vl-text] coord item[0]: text=电子发票(普通发票), bbox=[328, 123, 636, 168]
2026-08-05 06:14:02,409 INFO     29 [qwen-vl-text] coord item[1]: text=国家税务总局, bbox=[463, 175, 534, 193]
2026-08-05 06:14:02,409 INFO     29 [qwen-vl-text] coord item[2]: text=江苏省税务局, bbox=[463, 206, 537, 233]
2026-08-05 06:14:02,409 INFO     29 [qwen-vl-text] coord item[3]: text=发票号码：25322000000226700883, bbox=[731, 143, 944, 164]
2026-08-05 06:14:02,409 INFO     29 [qwen-vl-text] coord item[4]: text=开票日期：2025年05月20日, bbox=[731, 181, 905, 202]
2026-08-05 06:14:02,409 INFO     29 [qwen-vl-text] coord item[5]: text=购买方信息, bbox=[36, 284, 50, 398]
2026-08-05 06:14:02,409 INFO     29 [qwen-vl-text] coord item[6]: text=名称, bbox=[62, 302, 89, 321]
2026-08-05 06:14:02,409 INFO     29 [qwen-vl-text] coord item[7]: text=统一社会信用代码/纳税人识别号：, bbox=[62, 365, 259, 384]
2026-08-05 06:14:02,409 INFO     29 [qwen-vl-text] coord item[8]: text=销售方信息, bbox=[507, 284, 521, 398]
2026-08-05 06:14:02,409 INFO     29 [qwen-vl-text] coord item[9]: text=名称：无锡邻医大药房有限公司, bbox=[535, 296, 738, 317]
2026-08-05 06:14:02,409 INFO     29 [qwen-vl-text] coord item[10]: text=统一社会信用代码/纳税人识别号：91320214MA228F680W, bbox=[535, 360, 950, 382]
2026-08-05 06:14:02,410 INFO     29 [qwen-vl-text] coord item[11]: text=项目名称, bbox=[80, 420, 139, 440]
2026-08-05 06:14:02,410 INFO     29 [qwen-vl-text] coord item[12]: text=规格型号, bbox=[201, 420, 260, 440]
2026-08-05 06:14:02,410 INFO     29 [qwen-vl-text] coord item[13]: text=单位, bbox=[320, 420, 364, 440]
2026-08-05 06:14:02,410 INFO     29 [qwen-vl-text] coord item[14]: text=数量, bbox=[442, 420, 486, 440]
2026-08-05 06:14:02,410 INFO     29 [qwen-vl-text] coord item[15]: text=单价, bbox=[557, 420, 601, 440]
2026-08-05 06:14:02,410 INFO     29 [qwen-vl-text] coord item[16]: text=金额, bbox=[679, 420, 722, 440]
2026-08-05 06:14:02,410 INFO     29 [qwen-vl-text] coord item[17]: text=税率/征收率, bbox=[742, 420, 823, 440]
2026-08-05 06:14:02,410 INFO     29 [qwen-vl-text] coord item[18]: text=税额, bbox=[920, 420, 964, 440]
2026-08-05 06:14:02,410 INFO     29 [qwen-vl-text] coord item[19]: text=*化学药品制剂*倍择瑞令, bbox=[30, 445, 190, 467]
2026-08-05 06:14:02,410 INFO     29 [qwen-vl-text] coord item[20]: text=160μg/7.2μg/4, bbox=[203, 447, 303, 470]
2026-08-05 06:14:02,410 INFO     29 [qwen-vl-text] coord item[21]: text=盒, bbox=[334, 447, 350, 467]
2026-08-05 06:14:02,410 INFO     29 [qwen-vl-text] coord item[22]: text=3 210.029498522124, bbox=[477, 447, 601, 467]
2026-08-05 06:14:02,410 INFO     29 [qwen-vl-text] coord item[23]: text=630.09, bbox=[682, 447, 720, 467]
2026-08-05 06:14:02,410 INFO     29 [qwen-vl-text] coord item[24]: text=13%, bbox=[775, 447, 800, 467]
2026-08-05 06:14:02,410 INFO     29 [qwen-vl-text] coord item[25]: text=81.91, bbox=[933, 447, 964, 467]
2026-08-05 06:14:02,410 INFO     29 [qwen-vl-text] coord item[26]: text=畅布地格福吸入气雾剂, bbox=[30, 475, 180, 497]
2026-08-05 06:14:02,410 INFO     29 [qwen-vl-text] coord item[27]: text=.8μg*120揿, bbox=[203, 475, 281, 499]
2026-08-05 06:14:02,410 INFO     29 [qwen-vl-text] coord item[28]: text=合计, bbox=[104, 688, 117, 707]
2026-08-05 06:14:02,410 INFO     29 [qwen-vl-text] coord item[29]: text=计, bbox=[177, 688, 190, 707]
2026-08-05 06:14:02,411 INFO     29 [qwen-vl-text] coord item[30]: text=￥630.09, bbox=[676, 687, 720, 704]
2026-08-05 06:14:02,411 INFO     29 [qwen-vl-text] coord item[31]: text=￥81.91, bbox=[926, 687, 964, 704]
2026-08-05 06:14:02,411 INFO     29 [qwen-vl-text] coord item[32]: text=价税合计（大写）, bbox=[87, 730, 196, 750]
2026-08-05 06:14:02,411 INFO     29 [qwen-vl-text] coord item[33]: text=柒佰壹拾贰圆整, bbox=[303, 725, 408, 747]
2026-08-05 06:14:02,411 INFO     29 [qwen-vl-text] coord item[34]: text=(小写) ￥712.00, bbox=[688, 725, 808, 747]
2026-08-05 06:14:02,411 INFO     29 [qwen-vl-text] coord item[35]: text=备注, bbox=[36, 800, 50, 859]
2026-08-05 06:14:02,411 INFO     29 [qwen-vl-text] page=3 — 35/35 coords, api_time=18.7s
2026-08-05 06:14:02,431 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7824738, prompt_len=669
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
2026-08-05 06:14:06,545 INFO     29 [qwen-vl-text] coord API raw response (len=97):
[
	{"text": "挂号号:D20091... 医保余额:0 CM/KG 普通病人|现住址:内蒙古土默特左旗沙尔营乡大有庄村32", "bbox": [0, 48, 999, 94]}
]
2026-08-05 06:14:06,545 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=4.1s
2026-08-05 06:14:06,545 INFO     29 [qwen-vl-text] coord item[0]: text=挂号号:D20091... 医保余额:0 CM/KG 普通病人|现住址:内蒙古土默特左旗沙尔营乡大有庄村32, bbox=[0, 48, 999, 94]
2026-08-05 06:14:06,546 INFO     29 [qwen-vl-text] page=4 — 1/1 coords, api_time=4.1s
2026-08-05 06:14:06,546 INFO     29 [qwen-vl-text] new_positions (36):
[[3, 276.176, 535.512, 73.185, 99.96], [3, 389.846, 449.628, 104.125, 114.835], [3, 389.846, 452.154, 122.57, 138.635], [3, 615.502, 794.848, 85.085, 97.58], [3, 615.502, 762.01, 107.695, 120.19], [3, 30.311999999999998, 42.1, 168.98, 236.81], [3, 52.204, 74.938, 179.69, 190.995], [3, 52.204, 218.078, 217.17499999999998, 228.48], [3, 426.894, 438.68199999999996, 168.98, 236.81], [3, 450.46999999999997, 621.396, 176.12, 188.61499999999998], [3, 450.46999999999997, 799.9, 214.2, 227.29], [3, 67.36, 117.038, 249.89999999999998, 261.8], [3, 169.242, 218.92, 249.89999999999998, 261.8], [3, 269.44, 306.488, 249.89999999999998, 261.8], [3, 372.164, 409.212, 249.89999999999998, 261.8], [3, 468.99399999999997, 506.042, 249.89999999999998, 261.8], [3, 571.718, 607.924, 249.89999999999998, 261.8], [3, 624.764, 692.966, 249.89999999999998, 261.8], [3, 774.64, 811.688, 249.89999999999998, 261.8], [3, 25.259999999999998, 159.98, 264.775, 277.865], [3, 170.926, 255.126, 265.965, 279.65], [3, 281.228, 294.7, 265.965, 277.865], [3, 401.63399999999996, 506.042, 265.965, 277.865], [3, 574.244, 606.24, 265.965, 277.865], [3, 652.55, 673.6, 265.965, 277.865], [3, 785.586, 811.688, 265.965, 277.865], [3, 25.259999999999998, 151.56, 282.625, 295.715], [3, 170.926, 236.602, 282.625, 296.905], [3, 87.568, 98.514, 409.35999999999996, 420.66499999999996], [3, 149.034, 159.98, 409.35999999999996, 420.66499999999996], [3, 569.192, 606.24, 408.765, 418.88], [3, 779.692, 811.688, 408.765, 418.88], [3, 73.25399999999999, 165.03199999999998, 434.34999999999997, 446.25], [3, 255.126, 343.536, 431.375, 444.465], [3, 579.2959999999999, 680.336, 431.375, 444.465], [4, 0.0, 594.405, 40.416, 79.148]]
2026-08-05 06:14:06,546 INFO     29 [qwen-vl-text] ═══ DONE ═══ 36 positions, pages=2, time=26.8s
2026-08-05 06:14:06,546 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 06:14:06,546 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 06:14:06,546 INFO     29 [qwen-vl-text] positions(48): [[4, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 06:14:06,546 INFO     29 [qwen-vl-text] page grouping: [4, 5], lines per page: [1, 47]
2026-08-05 06:14:07,036 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 06:14:07,205 INFO     29 [qwen-vl-text] page=5, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 06:14:07,206 INFO     29 [qwen-vl-text] LLM extraction start, text_len=439
2026-08-05 06:14:07,206 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:14:07,206 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 150, \"bbox_end\": 197, \"encounter_dates\": [\"2026-02-09\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "3:34 星期二 190.1.48.233 版本 王立红\n电子发票(普通发票)\n国家税务总局\n内蒙古自治区税务局\n发票号码：26152000000119478346\n开票日期：2026年02月09日\n购买方信息\n名称\n统一社会信用代码/纳税人识别号：\n销售方信息\n名称：国药控股国大药房内蒙古有限公司\n统一社会信用代码/纳税人识别号：911501005732872139\n项目名称\n规格型号\n单位\n数量\n单价\n金额\n税率/征收率\n税额\n*化学药品制剂*布地格福\n160ug:7.2ug/4.8u\n盒\n3\n237.16814159292\n711.50\n13%\n92.50\n吸入气雾剂\ng:120揿\n*化学药品制剂*布地格福\n160ug:7.2ug/4.8u\n盒\n3\n237.16814159292\n711.50\n13%\n92.50\n吸入气雾剂\ng:120揿\n合计\n￥1423.00\n￥185.00\n价税合计（大写）\n壹仟陆佰零捌圆整\n(小写) ￥1608.00\n备注\n开票人：刘惠",
    "role": "user"
  }
]
[92m06:14:07 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:14:07,208 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:14:11,396 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:14:11,397 INFO     29 [qwen-vl-text] LLM output (len=750):
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
2026-08-05 06:14:11,397 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-09]
2026-08-05 06:14:11,413 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7824738, prompt_len=643
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["3:34 星期二 190.1.48.233 版本 王立红"]

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
2026-08-05 06:14:15,071 INFO     29 [qwen-vl-text] coord API raw response (len=73):
[
	{"text": "3:34 星期二 190.1.48.233 版本 王立红", "bbox": [0, 790, 974, 817]}
]
2026-08-05 06:14:15,071 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=3.7s
2026-08-05 06:14:15,071 INFO     29 [qwen-vl-text] coord item[0]: text=3:34 星期二 190.1.48.233 版本 王立红, bbox=[0, 790, 974, 817]
2026-08-05 06:14:15,074 INFO     29 [qwen-vl-text] page=4 — 1/1 coords, api_time=3.7s
2026-08-05 06:14:15,078 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=946229, prompt_len=1164
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
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord API raw response (len=4156):
[
	{"text": "电子发票(普通发票)", "bbox": [327, 80, 639, 125], "bbox_2d": [327, 80, 639, 125]},
	{"text": "国家税务总局", "bbox": [464, 133, 535, 149], "bbox_2d": [464, 133, 535, 149]},
	{"text": "内蒙古自治区税务局", "bbox": [452, 159, 552, 192], "bbox_2d": [452, 159, 552, 192]},
	{"text": "发票号码：26152000000119478346", "bbox": [735, 100, 951, 121], "bbox_2d": [735, 100, 951, 121]},
	{"text": "开票日期：2026年02月09日", "bbox": [735, 139, 911, 160], "bbox_2d": [735, 139, 911, 160]},
	{"text": "购买方信息", "bbox": [32, 244, 46, 360], "bbox_2d": [32, 244, 46, 360]},
	{"text": "名称", "bbox": [59, 261, 84, 280], "bbox_2d": [59, 261, 84, 280]},
	{"text": "统一社会信用代码/纳税人识别号：", "bbox": [58, 325, 258, 345], "bbox_2d": [58, 325, 258, 345]},
	{"text": "销售方信息", "bbox": [509, 244, 522, 360], "bbox_2d": [509, 244, 522, 360]},
	{"text": "名称：国药控股国大药房内蒙古有限公司", "bbox": [537, 255, 802, 277], "bbox_2d": [537, 255, 802, 277]},
	{"text": "统一社会信用代码/纳税人识别号：911501005732872139", "bbox": [536, 320, 955, 343], "bbox_2d": [536, 320, 955, 343]},
	{"text": "项目名称", "bbox": [77, 380, 136, 400], "bbox_2d": [77, 380, 136, 400]},
	{"text": "规格型号", "bbox": [200, 380, 258, 400], "bbox_2d": [200, 380, 258, 400]},
	{"text": "单位", "bbox": [320, 380, 364, 400], "bbox_2d": [320, 380, 364, 400]},
	{"text": "数量", "bbox": [443, 380, 487, 400], "bbox_2d": [443, 380, 487, 400]},
	{"text": "单价", "bbox": [560, 380, 604, 400], "bbox_2d": [560, 380, 604, 400]},
	{"text": "金额", "bbox": [682, 380, 726, 400], "bbox_2d": [682, 380, 726, 400]},
	{"text": "税率/征收率", "bbox": [746, 380, 828, 400], "bbox_2d": [746, 380, 828, 400]},
	{"text": "税额", "bbox": [926, 380, 971, 400], "bbox_2d": [926, 380, 971, 400]},
	{"text": "*化学药品制剂*布地格福", "bbox": [26, 406, 188, 428], "bbox_2d": [26, 406, 188, 428]},
	{"text": "160ug:7.2ug/4.8u", "bbox": [201, 407, 304, 430], "bbox_2d": [201, 407, 304, 430]},
	{"text": "盒", "bbox": [334, 407, 350, 428], "bbox_2d": [334, 407, 350, 428]},
	{"text": "3", "bbox": [479, 407, 488, 428], "bbox_2d": [479, 407, 488, 428]},
	{"text": "237.16814159292", "bbox": [503, 407, 604, 428], "bbox_2d": [503, 407, 604, 428]},
	{"text": "711.50", "bbox": [686, 407, 724, 428], "bbox_2d": [686, 407, 724, 428]},
	{"text": "13%", "bbox": [780, 407, 805, 428], "bbox_2d": [780, 407, 805, 428]},
	{"text": "92.50", "bbox": [940, 407, 971, 428], "bbox_2d": [940, 407, 971, 428]},
	{"text": "吸入气雾剂", "bbox": [26, 437, 101, 459], "bbox_2d": [26, 437, 101, 459]},
	{"text": "g:120揿", "bbox": [201, 437, 248, 460], "bbox_2d": [201, 437, 248, 460]},
	{"text": "*化学药品制剂*布地格福", "bbox": [26, 467, 188, 490], "bbox_2d": [26, 467, 188, 490]},
	{"text": "160ug:7.2ug/4.8u", "bbox": [201, 468, 304, 491], "bbox_2d": [201, 468, 304, 491]},
	{"text": "盒", "bbox": [334, 468, 350, 490], "bbox_2d": [334, 468, 350, 490]},
	{"text": "3", "bbox": [479, 468, 488, 490], "bbox_2d": [479, 468, 488, 490]},
	{"text": "237.16814159292", "bbox": [503, 468, 604, 490], "bbox_2d": [503, 468, 604, 490]},
	{"text": "711.50", "bbox": [686, 468, 724, 490], "bbox_2d": [686, 468, 724, 490]},
	{"text": "13%", "bbox": [780, 468, 805, 490], "bbox_2d": [780, 468, 805, 490]},
	{"text": "92.50", "bbox": [940, 468, 971, 490], "bbox_2d": [940, 468, 971, 490]},
	{"text": "吸入气雾剂", "bbox": [26, 497, 101, 519], "bbox_2d": [26, 497, 101, 519]},
	{"text": "g:120揿", "bbox": [201, 497, 248, 520], "bbox_2d": [201, 497, 248, 520]},
	{"text": "合计", "bbox": [101, 654, 114, 673], "bbox_2d": [101, 654, 114, 673]},
	{"text": "计", "bbox": [175, 654, 188, 673], "bbox_2d": [175, 654, 188, 673]},
	{"text": "￥1423.00", "bbox": [667, 650, 724, 670], "bbox_2d": [667, 650, 724, 670]},
	{"text": "￥185.00", "bbox": [921, 650, 971, 670], "bbox_2d": [921, 650, 971, 670]},
	{"text": "价税合计（大写）", "bbox": [84, 695, 194, 716], "bbox_2d": [84, 695, 194, 716]},
	{"text": "壹仟陆佰零捌圆整", "bbox": [303, 691, 424, 714], "bbox_2d": [303, 691, 424, 714]},
	{"text": "(小写) ￥1608.00", "bbox": [691, 689, 822, 714], "bbox_2d": [691, 689, 822, 714]},
	{"text": "备注", "bbox": [32, 767, 46, 787], "bbox_2d": [32, 767, 46, 787]},
	{"text": "注", "bbox": [32, 807, 46, 827], "bbox_2d": [32, 807, 46, 827]},
	{"text": "开票人：刘惠", "bbox": [95, 898, 185, 920], "bbox_2d": [95, 898, 185, 920]}
]
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord API: raw_items=49, valid_items=49, elapsed=24.5s
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord item[0]: text=电子发票(普通发票), bbox=[327, 80, 639, 125]
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord item[1]: text=国家税务总局, bbox=[464, 133, 535, 149]
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord item[2]: text=内蒙古自治区税务局, bbox=[452, 159, 552, 192]
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord item[3]: text=发票号码：26152000000119478346, bbox=[735, 100, 951, 121]
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord item[4]: text=开票日期：2026年02月09日, bbox=[735, 139, 911, 160]
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord item[5]: text=购买方信息, bbox=[32, 244, 46, 360]
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord item[6]: text=名称, bbox=[59, 261, 84, 280]
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord item[7]: text=统一社会信用代码/纳税人识别号：, bbox=[58, 325, 258, 345]
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord item[8]: text=销售方信息, bbox=[509, 244, 522, 360]
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord item[9]: text=名称：国药控股国大药房内蒙古有限公司, bbox=[537, 255, 802, 277]
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord item[10]: text=统一社会信用代码/纳税人识别号：911501005732872139, bbox=[536, 320, 955, 343]
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord item[11]: text=项目名称, bbox=[77, 380, 136, 400]
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord item[12]: text=规格型号, bbox=[200, 380, 258, 400]
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord item[13]: text=单位, bbox=[320, 380, 364, 400]
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord item[14]: text=数量, bbox=[443, 380, 487, 400]
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord item[15]: text=单价, bbox=[560, 380, 604, 400]
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord item[16]: text=金额, bbox=[682, 380, 726, 400]
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord item[17]: text=税率/征收率, bbox=[746, 380, 828, 400]
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord item[18]: text=税额, bbox=[926, 380, 971, 400]
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord item[19]: text=*化学药品制剂*布地格福, bbox=[26, 406, 188, 428]
2026-08-05 06:14:39,607 INFO     29 [qwen-vl-text] coord item[20]: text=160ug:7.2ug/4.8u, bbox=[201, 407, 304, 430]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[21]: text=盒, bbox=[334, 407, 350, 428]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[22]: text=3, bbox=[479, 407, 488, 428]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[23]: text=237.16814159292, bbox=[503, 407, 604, 428]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[24]: text=711.50, bbox=[686, 407, 724, 428]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[25]: text=13%, bbox=[780, 407, 805, 428]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[26]: text=92.50, bbox=[940, 407, 971, 428]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[27]: text=吸入气雾剂, bbox=[26, 437, 101, 459]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[28]: text=g:120揿, bbox=[201, 437, 248, 460]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[29]: text=*化学药品制剂*布地格福, bbox=[26, 467, 188, 490]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[30]: text=160ug:7.2ug/4.8u, bbox=[201, 468, 304, 491]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[31]: text=盒, bbox=[334, 468, 350, 490]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[32]: text=3, bbox=[479, 468, 488, 490]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[33]: text=237.16814159292, bbox=[503, 468, 604, 490]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[34]: text=711.50, bbox=[686, 468, 724, 490]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[35]: text=13%, bbox=[780, 468, 805, 490]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[36]: text=92.50, bbox=[940, 468, 971, 490]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[37]: text=吸入气雾剂, bbox=[26, 497, 101, 519]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[38]: text=g:120揿, bbox=[201, 497, 248, 520]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[39]: text=合计, bbox=[101, 654, 114, 673]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[40]: text=计, bbox=[175, 654, 188, 673]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[41]: text=￥1423.00, bbox=[667, 650, 724, 670]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[42]: text=￥185.00, bbox=[921, 650, 971, 670]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[43]: text=价税合计（大写）, bbox=[84, 695, 194, 716]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[44]: text=壹仟陆佰零捌圆整, bbox=[303, 691, 424, 714]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[45]: text=(小写) ￥1608.00, bbox=[691, 689, 822, 714]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[46]: text=备注, bbox=[32, 767, 46, 787]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[47]: text=注, bbox=[32, 807, 46, 827]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] coord item[48]: text=开票人：刘惠, bbox=[95, 898, 185, 920]
2026-08-05 06:14:39,608 INFO     29 [qwen-vl-text] page=5 — 47/47 coords, api_time=24.5s
2026-08-05 06:14:39,609 INFO     29 [qwen-vl-text] new_positions (48):
[[4, 0.0, 579.53, 665.18, 687.914], [5, 275.334, 538.038, 47.599999999999994, 74.375], [5, 390.688, 450.46999999999997, 79.13499999999999, 88.655], [5, 380.584, 464.784, 94.60499999999999, 114.24], [5, 618.87, 800.742, 59.5, 71.99499999999999], [5, 618.87, 767.062, 82.705, 95.19999999999999], [5, 26.944, 38.732, 145.18, 214.2], [5, 49.678, 70.728, 155.295, 166.6], [5, 48.836, 217.236, 193.375, 205.27499999999998], [5, 428.578, 439.524, 145.18, 214.2], [5, 452.154, 675.284, 151.725, 164.815], [5, 451.312, 804.11, 190.39999999999998, 204.08499999999998], [5, 64.834, 114.512, 226.1, 238.0], [5, 168.4, 217.236, 226.1, 238.0], [5, 269.44, 306.488, 226.1, 238.0], [5, 373.006, 410.054, 226.1, 238.0], [5, 471.52, 508.568, 226.1, 238.0], [5, 574.244, 611.292, 226.1, 238.0], [5, 628.132, 697.1759999999999, 226.1, 238.0], [5, 779.692, 817.582, 226.1, 238.0], [5, 21.892, 158.296, 241.57, 254.66], [5, 169.242, 255.968, 242.165, 255.85], [5, 281.228, 294.7, 242.165, 254.66], [5, 403.318, 410.89599999999996, 242.165, 254.66], [5, 423.526, 508.568, 242.165, 254.66], [5, 577.612, 609.608, 242.165, 254.66], [5, 656.76, 677.81, 242.165, 254.66], [5, 791.48, 817.582, 242.165, 254.66], [5, 21.892, 85.042, 260.015, 273.10499999999996], [5, 169.242, 208.816, 260.015, 273.7], [5, 21.892, 158.296, 277.865, 291.55], [5, 169.242, 255.968, 278.46, 292.145], [5, 281.228, 294.7, 278.46, 291.55], [5, 403.318, 410.89599999999996, 278.46, 291.55], [5, 423.526, 508.568, 278.46, 291.55], [5, 577.612, 609.608, 278.46, 291.55], [5, 656.76, 677.81, 278.46, 291.55], [5, 791.48, 817.582, 278.46, 291.55], [5, 21.892, 85.042, 295.715, 308.805], [5, 169.242, 208.816, 295.715, 309.4], [5, 85.042, 95.988, 389.13, 400.435], [5, 147.35, 158.296, 389.13, 400.435], [5, 561.614, 609.608, 386.75, 398.65], [5, 775.482, 817.582, 386.75, 398.65], [5, 70.728, 163.34799999999998, 413.525, 426.02], [5, 255.126, 357.008, 411.145, 424.83], [5, 581.822, 692.124, 409.955, 424.83], [5, 26.944, 38.732, 456.36499999999995, 468.265]]
2026-08-05 06:14:39,609 INFO     29 [qwen-vl-text] ═══ DONE ═══ 48 positions, pages=2, time=33.1s
2026-08-05 06:14:39,616 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-05 06:14:39,616 INFO     29 [Trace] task=8c1d03f4 | doc=麦济ZHYH.pdf | Extractor:Medication | outputs={"chunks": "4 items, types={'MedicationRecord': 4}", "html": "", "json": "198 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-05 06:14:39,616 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-05 06:14:39,617 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T06:14:39.616+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 25, "failed": 0, "current": {"8c1d03f4909411f1a3da71efcdd7cc1f": {"id": "8c1d03f4909411f1a3da71efcdd7cc1f", "doc_id": "8b75f8fc909411f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHYH.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHYH.pdf", "size": 10529267, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785910310550, "task_type": "dataflow", "root_trace_id": "5845aea086174457a53e2c12052f4abe", "root_traceparent": "00-5845aea086174457a53e2c12052f4abe-577ba8815fd96dc1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 06:14:39,623 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:14:39,623 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m06:14:39 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:14:39,624 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:14:40,567 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:14:40,575 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-05 06:14:40,575 INFO     29 [Trace] task=8c1d03f4 | doc=麦济ZHYH.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "198 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-05 06:14:40,575 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-05 06:14:40,581 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:14:40,581 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m06:14:40 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:14:40,582 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:14:44,500 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:14:44,506 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-05 06:14:44,506 INFO     29 [Trace] task=8c1d03f4 | doc=麦济ZHYH.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "198 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-05 06:14:44,506 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-05 06:14:44,511 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 06:14:44,511 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-05 06:14:45,079 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 06:14:45,084 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-05 06:14:45,084 INFO     29 [Trace] task=8c1d03f4 | doc=麦济ZHYH.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "198 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-05 06:14:45,084 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-05 06:14:45,090 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:14:45,090 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m06:14:45 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:14:45,091 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:14:46,561 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:14:46,566 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-05 06:14:46,566 INFO     29 [Trace] task=8c1d03f4 | doc=麦济ZHYH.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "198 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-05 06:14:46,566 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-05 06:14:46,567 INFO     29 [ChunkMerger] Merged 6 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 4, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1} (filtered 6 noise chunks)
2026-08-05 06:14:46,575 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-05 06:14:46,575 INFO     29 [Trace] task=8c1d03f4 | doc=麦济ZHYH.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 2, 'MedicationRecord': 4}", "name": "麦济ZHYH.pdf"}
2026-08-05 06:14:46,575 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-05 06:14:46,620 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1785910311225, 'update_date': datetime.datetime(2026, 8, 5, 6, 11, 51), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 249549, 'status': '1'}
2026-08-05 06:14:46,830 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=内蒙古医科大学附属医院门诊病历
姓名：
年龄：62岁
诊疗号：0014498780
民族：
性别：男性
呼吸内科门诊
联系电话：
1 身份证：
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
民族: 别: 男性 科室:呼吸内科门诊
联系电话: 身份证:1 病情:
就诊状态: 就诊时间: 2024-12-10 12:37
生命体征(需要时):
体温:℃ 脉搏:次/分 呼吸:次/分 血压:/mmHg
主诉:SSSJ项目肺功能检查开单
现病史: 哮喘
既往史: 患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎
无,吸烟史无,无过敏史。
体格检查: 发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰
音,双下肢无水肿,体重kg。
辅助检查:
初步诊断(西医): 1.哮喘
初步诊断(中医):
治疗方案:/
呼吸过滤器 肺通气功能检查
用量:
用法:
签名:崔丽英
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
(小写) ￥712.00
备注
挂号号:D20091... 医保余额:0 CM/KG 普通病人|现住址:内蒙古土默特左旗沙尔营乡大有庄村32
---
3:34 星期二 190.1.48.233 版本 王立红
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
2026-08-05 06:14:47,202 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-05 06:14:47,202 INFO     29 [Trace] task=8c1d03f4 | doc=麦济ZHYH.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 2, 'MedicationRecord': 4}", "name": "麦济ZHYH.pdf", "embedding_token_consumption": 1716}
2026-08-05 06:14:47,202 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-05 06:14:47,819 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-05 06:14:47,819 INFO     29 [Trace] task=8c1d03f4 | doc=麦济ZHYH.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":6,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-05 06:14:47,823 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 06:14:47,823 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 06:14:47,823 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 06:14:47,823 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 06:14:47,823 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 06:14:47,823 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 06:14:47,829 INFO     29 set_progress(8c1d03f4909411f1a3da71efcdd7cc1f), progress: 0.82, progress_msg: 06:14:47 [DOC Engine]:
Start to index...
2026-08-05 06:14:47,856 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.023s]
2026-08-05 06:14:47,861 INFO     29 set_progress(8c1d03f4909411f1a3da71efcdd7cc1f), progress: 0.8166666666666668, progress_msg: 
2026-08-05 06:14:47,872 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.007s]
2026-08-05 06:14:47,879 INFO     29 set_progress(8c1d03f4909411f1a3da71efcdd7cc1f), progress: 1.0, progress_msg: 06:14:47 Indexing done (0.05s). Task done (162.15s)
2026-08-05 06:14:47,883 INFO     29 [Done], chunks(6), token(1716), elapsed:162.15
2026-08-05 06:14:47,963 INFO     29 handle_task done for task {"id": "8c1d03f4909411f1a3da71efcdd7cc1f", "doc_id": "8b75f8fc909411f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHYH.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHYH.pdf", "size": 10529267, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1785910310550, "task_type": "dataflow", "root_trace_id": "5845aea086174457a53e2c12052f4abe", "root_traceparent": "00-5845aea086174457a53e2c12052f4abe-577ba8815fd96dc1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
