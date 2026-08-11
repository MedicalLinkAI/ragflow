# 基准结果：麦济WRNA(2).pdf

## 基本信息

- 文件：`麦济WRNA(2).pdf`
- 大小：12723.2 KB
- PDF 总页数：9
- doc_id：`ed520a7a94b811f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T20:42:18  完成时间：2026-08-10T20:45:54  耗时：216.1s
- progress_msg：`12:45:52 Indexing done (0.05s). Task done (200.60s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | e6d0220e | 1 | 1-1 | 内蒙古医科大学附属医院门诊病历 姓名： 年龄：54岁 诊疗号：001030409 |
| 2 | e4221434 | 1 | 2-2 | 内蒙古医科大学附属医院门诊病历 姓名： 年龄：54岁 诊疗号：001030409 |
| 3 | 51280acb | 1 | 3-3 | 鹤春堂大药房 2026-01-21 17:23:52 收银员：张星 名称 单价  |
| 4 | d7d4a599 | 1 | 4-4 | 11:43 美团 5G 4G 24 电子票预览 www.chinaebill.c |
| 5 | 66539eb4 | 3 | 4-6 | 复核人：李姹娜 收款人：李姹娜 查看收费明细 发送到邮箱 15:38 954 w |
| 6 | faea8697 | 1 | 6-6 | 报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录: □痕迹 □批注  |
| 7 | 4cb2ccf4 | 2 | 6-7 | 付丹 26星期二 190.1.48.233 王王立 内蒙古自治区国际蒙医医院 门 |
| 8 | 9f0c7054 | 1 | 8-8 | 医疗收费明细（电子） 所属电 15060125 所属电子票据号码:0127705 |
| 9 | b82453b5 | 1 | 9-9 | 鹤春堂大药房 2025-12-26 12:29:31 收银员：张星 名称 单价  |

- chunks 总数：9
- 各 chunk 页数合计（含跨页重复）：12
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9]`
- 覆盖页数：9 / 9；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 4 | 0 | 4 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 5 | 5 | 5 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 0 | 1 | 0 | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 4, "MedicationRecord": 5}`
- ChunkMerger：`{"found": true, "merged": 9, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 4, "Extractor:Medication": 5, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 7}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 12:45:51,741 INFO     29 [ChunkMerger] Merged 9 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 4, 'Extractor:Medication': 5, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 12:42:22,718 INFO     29 handle_task begin for task {"id": "ed8cac4894b811f1bd9827cf206dfa2d", "doc_id": "ed520a7a94b811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWRNA(2).pdf", "type": "pdf", "location": "\u9ea6\u6d4eWRNA(2).pdf", "size": 13028580, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786365740553, "task_type": "dataflow", "root_trace_id": "cdcb62f1323147c19d5b537cd2e3ed24", "root_traceparent": "00-cdcb62f1323147c19d5b537cd2e3ed24-dbd2f127625489c0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 12:42:22,951 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 12:42:23,062 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 12:42:23,078 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:42:23,078 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 12:42:23,078 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 12:42:23,083 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 12:42:23,084 INFO     29 ============================================================
2026-08-10 12:42:23,084 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 12:42:23,084 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 12:42:23,084 INFO     29 ============================================================
2026-08-10 12:42:23,084 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 12:42:23,084 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 12:42:23,085 INFO     29 No torch found.
2026-08-10 12:42:24,106 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=9
2026-08-10 12:42:24,390 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1384701, prompt_len=764
2026-08-10 12:42:25,930 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-02-27"}
```
2026-08-10 12:42:25,930 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2026-02-27
2026-08-10 12:42:25,938 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1384701, prompt_len=401
2026-08-10 12:42:29,627 INFO     29 [qwen-vl-parser] text API response (len=644):
["内蒙古医科大学附属医院门诊病历", "姓名：", "年龄：54岁", "诊疗号：0010304094", "民族：蒙古", "性别：女性", "科室：呼吸内科门诊", "联系电话：", "身份证：", "病情：", "就诊状态：", "就诊时间：2026-02-27 16:58", "生命体征（需要时）：", "体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg", "主诉：诊断支气管哮喘10余年，加重1月。", "现病史：诊断支气管哮喘10余年，加重1月。夜间发作，咳白色粘痰，有黄", "色鼻涕。每日吸入信必可都保，症状无改善。", "既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "无，吸烟史无，无过敏史。", "体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺未闻及啰", "音，双下肢无水肿，体重kg。", "辅助检查：待回报", "过敏史：不详", "初步诊断（西医）：1.支气管哮喘", "初步诊断（中医）：", "治疗方案：随诊", "血常规", "免疫球蛋白IgE", "一次性肺功能仪用过滤嘴", "肺炎支原体IgM抗体免疫", "肺炎支原体IgG抗体免疫C反应蛋白测定", "室", "室", "磷酸可待因片<15mg>", "用量：1.000片/次", "用法：口服，一次/日，5天", "桉柠蒎肠溶胶囊<桉柠蒎油计0.3g/粒>", "用量：1.000粒/次", "用法：口服，二次/日，7天", "签名："]
2026-08-10 12:42:29,627 INFO     29 [qwen-vl-parser] page=1 text: 40 lines (bbox 0-39)
2026-08-10 12:42:29,627 INFO     29 [qwen-vl-parser] page=1 text: 40 sections
2026-08-10 12:42:29,985 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1695638, prompt_len=764
2026-08-10 12:42:31,401 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-03-01"}
```
2026-08-10 12:42:31,401 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=2024-03-01
2026-08-10 12:42:31,414 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1695638, prompt_len=401
2026-08-10 12:42:34,236 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:42:34.234+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 31, "failed": 0, "current": {"ed8cac4894b811f1bd9827cf206dfa2d": {"id": "ed8cac4894b811f1bd9827cf206dfa2d", "doc_id": "ed520a7a94b811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWRNA(2).pdf", "type": "pdf", "location": "\u9ea6\u6d4eWRNA(2).pdf", "size": 13028580, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786365740553, "task_type": "dataflow", "root_trace_id": "cdcb62f1323147c19d5b537cd2e3ed24", "root_traceparent": "00-cdcb62f1323147c19d5b537cd2e3ed24-dbd2f127625489c0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:42:35,018 INFO     29 [qwen-vl-parser] text API response (len=594):
["内蒙古医科大学附属医院门诊病历", "姓名：", "年龄：54岁", "诊疗号：0010304094", "民族：蒙古", "性别：女性", "科室：呼吸内科门诊", "联系电话：", "身份证：", "病情：", "就诊状态：", "就诊时间：2024-03-01 09:48", "生命体征（需要时）：", "体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg", "主诉：诊断支气管哮喘10余年，加重1月。", "现病史：诊断支气管哮喘10余年，加重1月。夜间发作，咳白色粘痰，有黄", "色鼻涕。每日吸入信必可都保，症状无改善。", "既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "无，吸烟史无，无过敏史。鼻炎", "体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺干鸣音，双", "下肢无水肿，体重kg。", "辅助检查：待回报", "过敏史：不详", "初步诊断（西医）：1.支气管哮喘 2.过敏性鼻炎[变应性鼻炎]", "初步诊断（中医）：", "治疗方案：", "多索茶碱片<0.2g>", "用量：0.200g/次", "用法：口服，一次/日，7天", "布地奈德福莫特罗吸入粉雾剂", "用量：1.000吸/次", "(Ⅱ)<(160μg/4.5μg)/吸*60>", "用法：吸入，二次/日，3天", "签名：李"]
2026-08-10 12:42:35,019 INFO     29 [qwen-vl-parser] page=2 text: 34 lines (bbox 40-73)
2026-08-10 12:42:35,019 INFO     29 [qwen-vl-parser] page=2 text: 34 sections
2026-08-10 12:42:35,303 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1472877, prompt_len=764
2026-08-10 12:42:36,742 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:42:36,742 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 12:42:36,759 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1472877, prompt_len=401
2026-08-10 12:42:38,524 INFO     29 [qwen-vl-parser] text API response (len=249):
["鹤春堂大药房", "2026-01-21 17:23:52", "收银员：张星", "名称 单价 数量 金额", "布地奈德福莫特罗吸入粉雾剂(Ⅱ)", "320 μg /9 μg / 吸 60 吸 / 支", "298.00 2 596.00", "应收金额: 596.00", "实收金额: 596.00", "找零: 0.00", "优惠: 0.00", "会员:", "本次积分: 596", "合计积分: 1325", "祝您身体健康，药品属于特殊商品", "无质量问题，概不退换"]
2026-08-10 12:42:38,525 INFO     29 [qwen-vl-parser] page=3 text: 16 lines (bbox 74-89)
2026-08-10 12:42:38,526 INFO     29 [qwen-vl-parser] page=3 text: 16 sections
2026-08-10 12:42:38,621 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=582067, prompt_len=764
2026-08-10 12:42:41,296 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:42:41,297 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 12:42:41,309 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=582067, prompt_len=401
2026-08-10 12:42:45,493 INFO     29 [qwen-vl-parser] text API response (len=785):
```json
[
"11:43",
"美团",
"5G",
"4G",
"24",
"电子票预览",
"www.chinaebill.cn",
"内蒙古自治区医疗门诊收费票据（电子）",
"内蒙古",
"财政部监制",
"票据代码：15060125",
"票据号码：0127705695",
"交款人",
"用代码：150102********2023",
"校验码：55e825",
"交",
"开票日期：2026-02-12",
"数量/单位",
"金额（元）",
"备注",
"项目名称",
"数量/单位",
"金额（元）",
"备注",
"西药费",
"1",
"项",
"188.21",
"金额合计（大写）壹佰捌拾捌元贰角壹分",
"(小写)188.21",
"业务流水号：202602120002043",
"门诊号：2602120916",
"就诊日期：20260212",
"其",
"医疗机构类型：综合医院",
"医保类型：职工基本医疗保险",
"医保编号：150000NMGZG00000000001",
"性别：女",
"9506",
"信",
"医保统筹基金支付：101.92",
"其他支付：0.00",
"个人账户支付：86.29",
"个人现金支付：0.00",
"息",
"个人自付：86.29",
"个人自费：0.00",
"交费日期：20260212",
"备注：医保总金额：188.21符合统筹：169.87账户余额：4301.09医疗救助基金：0大病保险：0公务员补助：0",
"医疗收费专用章",
"支付：0企业补充保险：0符合政策范围金额：169.87其他基金：0伙食补助：0起付线：0",
"（章）：内蒙古自治区国际蒙医医院",
"复核人：李姹娜",
"收款人：李姹娜",
"查看收费明细",
"发送到邮箱"
]
```
2026-08-10 12:42:45,494 INFO     29 [qwen-vl-parser] page=4 text: 56 lines (bbox 90-145)
2026-08-10 12:42:45,494 INFO     29 [qwen-vl-parser] page=4 text: 56 sections
2026-08-10 12:42:45,573 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=403280, prompt_len=764
2026-08-10 12:42:46,799 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:42:46,800 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 12:42:46,811 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=403280, prompt_len=401
2026-08-10 12:42:49,537 INFO     29 [qwen-vl-parser] text API response (len=484):
["15:38", "954", "wwwwwwwwwwwwwwwwww.pdf", "电子发票(普通发票)", "国家税务总局", "内蒙古自治区税务局", "发票号码：26152000000173167231", "开票日期：2026年03月04日", "购买方信息", "统一社会信用代码/纳税人识别号：150102197111182023", "销售方信息", "名称：国药控股国大药房内蒙古有限公司", "统一社会信用代码/纳税人识别号：911501005732872139", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*布地奈德", "320ug:9ug*60吸", "盒", "1", "274.336283185841", "274.34", "13%", "35.66", "福莫特罗吸入粉雾剂（）", "合计", "￥274.34", "￥35.66", "价税合计（大写）", "叁佰壹拾圆整", "(小写)￥310.00", "备注", "开票人：刘惠"]
2026-08-10 12:42:49,537 INFO     29 [qwen-vl-parser] page=5 text: 38 lines (bbox 146-183)
2026-08-10 12:42:49,537 INFO     29 [qwen-vl-parser] page=5 text: 38 sections
2026-08-10 12:42:50,203 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6255969, prompt_len=764
2026-08-10 12:42:51,784 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2023-03-04"}
```
2026-08-10 12:42:51,787 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=2023-03-04
2026-08-10 12:42:51,814 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6255969, prompt_len=401
2026-08-10 12:42:56,778 INFO     29 [qwen-vl-parser] text API response (len=757):
["号号:D20214...医保余额:3631.8CM/KG普通病人|现住址:内蒙古自治区呼和浩特市赛罕区", "报告", "闭环管理", "治疗", "健康调阅", "三诺血糖", "华益血糖", "门诊记录:", "□痕迹", "□批注", "历信息", "内蒙古医科大学附属医院门诊病历", "姓名", "年龄:51岁", "诊疗号:0010304094", "民族:蒙古族", "性别:女性", "科室:呼吸内科门诊", "联系电话:", "身份证:", "病情:", "就诊状态:", "就诊时间:2023-03-0410:51", "生命体征(需要时):", "体温:℃脉搏:次/分呼吸:次/分血压:/mmHg", "主诉:咳嗽1月,哮喘病史10余年", "现病史:", "既往史:患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎", "有,20年,吸烟史无,无过敏史。", "体格检查:发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰", "音,双下肢无水肿,体重kg。", "辅助检查:肺功能正常", "过敏史:", "初步诊断(西医):1.支气管哮喘", "初步诊断(中医):", "治疗方案:", "CT胸部", "最大通气量功能检查呼吸过滤器", "肺弥散功能检查--口残气容积测定-氮气平肺通气功能检查", "气法", "衡法", "孟鲁司特钠片<10mg>", "用量:1.000片/次", "用法:口服,一次/每晚,7天", "布地奈德福莫特罗吸入粉雾剂(11)", "用量:1.000吸/次", "<(320μg/9μg)/吸*60>", "用法:吸入,二次/日,7天", "签名:", "付丹", "26星期二", "190.1.48.233", "王王立"]
2026-08-10 12:42:56,781 INFO     29 [qwen-vl-parser] page=6 text: 53 lines (bbox 184-236)
2026-08-10 12:42:56,782 INFO     29 [qwen-vl-parser] page=6 text: 53 sections
2026-08-10 12:42:57,186 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1961874, prompt_len=764
2026-08-10 12:42:58,565 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:42:58,565 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-10 12:42:58,574 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1961874, prompt_len=401
2026-08-10 12:43:01,806 INFO     29 [qwen-vl-parser] text API response (len=523):
["内蒙古自治区国际蒙医医院", "门诊病历", "门诊号：2602120916", "姓", "科室：呼吸与危重症医学科门 性别：女性 出生年月：1971-11-18", "诊", "就诊时间：2026-02-12 11:20", "○初诊◎复诊", "过敏史：□否 □不详 □有：", "主 诉：发作性咳嗽、气短5年，加重3天", "现病史：5年前出现发作性咳嗽、气短，吸入刺激性气味后症状明显，就诊于当地医院诊断", "为“支气管哮喘”，长期规律吸入信必可治疗后效果欠佳。近3天喘息加重，伴咳嗽、咳痰较前", "频繁。夜间明显。", "既往史：体健", "家族史：无", "体格检查：意识：清醒", "T：36.5℃ P：71次/分 R：18次/分 BP：115/77mmHg", "双肺可闻及干鸣音", "辅助检查：", "处方信息：", "布地奈德福莫特罗吸入粉雾剂（II）(160μg/4.5μg/吸*60吸/支)*1支", "320μg 吸入 bid", "醋酸泼尼松片(5mg*100片/瓶)*1瓶", "15mg 口服 qd", "其他处置：", "复诊记录：", "门诊诊断：支气管哮喘(急性发作期)", "医生签名：苏佳"]
2026-08-10 12:43:01,807 INFO     29 [qwen-vl-parser] page=7 text: 28 lines (bbox 237-264)
2026-08-10 12:43:01,808 INFO     29 [qwen-vl-parser] page=7 text: 28 sections
2026-08-10 12:43:02,048 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1092602, prompt_len=764
2026-08-10 12:43:03,472 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:43:03,472 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-10 12:43:03,485 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1092602, prompt_len=401
2026-08-10 12:43:05,373 INFO     29 [qwen-vl-parser] text API response (len=286):
["医疗收费明细（电子）", "所属电", "15060125", "所属电子票据号码:0127705695", "交", "开票日期:2026年02月12日", "项目名称", "数量/单位", "金额（元）", "备注", "西药费(小计:188.2100元)", "布地奈德福莫特罗吸入粉雾剂（II）", "60", "吸", "183.4100", "乙", "醋酸泼尼松片", "100", "片", "4.8000", "甲", "小计 188.2100", "合计 188.2100", "收款单位（章）内蒙古自治区国际蒙医医院", "1 页 共 1 页"]
2026-08-10 12:43:05,374 INFO     29 [qwen-vl-parser] page=8 text: 25 lines (bbox 265-289)
2026-08-10 12:43:05,374 INFO     29 [qwen-vl-parser] page=8 text: 25 sections
2026-08-10 12:43:05,575 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:43:05.574+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 31, "failed": 0, "current": {"ed8cac4894b811f1bd9827cf206dfa2d": {"id": "ed8cac4894b811f1bd9827cf206dfa2d", "doc_id": "ed520a7a94b811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWRNA(2).pdf", "type": "pdf", "location": "\u9ea6\u6d4eWRNA(2).pdf", "size": 13028580, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786365740553, "task_type": "dataflow", "root_trace_id": "cdcb62f1323147c19d5b537cd2e3ed24", "root_traceparent": "00-cdcb62f1323147c19d5b537cd2e3ed24-dbd2f127625489c0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:43:05,716 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1776179, prompt_len=764
2026-08-10 12:43:07,154 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:43:07,154 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-10 12:43:07,169 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1776179, prompt_len=401
2026-08-10 12:43:08,944 INFO     29 [qwen-vl-parser] text API response (len=249):
["鹤春堂大药房", "2025-12-26 12:29:31", "收银员：张星", "名称 单价 数量 金额", "布地奈德福莫特罗吸入粉雾剂(II)", "320 μg /9 μg / 吸 60 吸 / 支", "298.00 1 298.00", "应收金额: 298.00", "实收金额: 298.00", "找零: 0.00", "优惠: 0.00", "会员:", "本次积分: 298", "合计积分: 729", "祝您身体健康，药品属于特殊商品", "无质量问题，概不退换"]
2026-08-10 12:43:08,944 INFO     29 [qwen-vl-parser] page=9 text: 16 lines (bbox 290-305)
2026-08-10 12:43:08,944 INFO     29 [qwen-vl-parser] page=9 text: 16 sections
2026-08-10 12:43:08,944 INFO     29 [qwen-vl-parser] parse_pdf done: 306 sections from 9 pages.
2026-08-10 12:43:08,950 INFO     29 Close text detector.
2026-08-10 12:43:09,370 INFO     29 Close text recognizer.
2026-08-10 12:43:09,781 INFO     29 Close recognizer.
2026-08-10 12:43:10,178 INFO     29 Close recognizer.
2026-08-10 12:43:10,609 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 12:43:10,609 INFO     29 [Trace] task=ed8cac48 | doc=麦济WRNA(2).pdf | Parser:MedLink | outputs={"html": "", "json": "306 items", "markdown": "", "text": "", "name": "麦济WRNA(2).pdf", "output_format": "json"}
2026-08-10 12:43:10,609 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 12:43:10,626 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:43:10,626 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 内蒙古医科大学附属医院门诊病历\n[BBOX-1] 姓名：\n[BBOX-2] 年龄：54岁\n[BBOX-3] 诊疗号：0010304094\n[BBOX-4] 民族：蒙古\n[BBOX-5] 性别：女性\n[BBOX-6] 科室：呼吸内科门诊\n[BBOX-7] 联系电话：\n[BBOX-8] 身份证：\n[BBOX-9] 病情：\n[BBOX-10] 就诊状态：\n[BBOX-11] 就诊时间：2026-02-27 16:58\n[BBOX-12] 生命体征（需要时）：\n[BBOX-13] 体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg\n[BBOX-14] 主诉：诊断支气管哮喘10余年，加重1月。\n[BBOX-15] 现病史：诊断支气管哮喘10余年，加重1月。夜间发作，咳白色粘痰，有黄\n[BBOX-16] 色鼻涕。每日吸入信必可都保，症状无改善。\n[BBOX-17] 既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎\n[BBOX-18] 无，吸烟史无，无过敏史。\n[BBOX-19] 体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺未闻及啰\n[BBOX-20] 音，双下肢无水肿，体重kg。\n[BBOX-21] 辅助检查：待回报\n[BBOX-22] 过敏史：不详\n[BBOX-23] 初步诊断（西医）：1.支气管哮喘\n[BBOX-24] 初步诊断（中医）：\n[BBOX-25] 治疗方案：随诊\n[BBOX-26] 血常规\n[BBOX-27] 免疫球蛋白IgE\n[BBOX-28] 一次性肺功能仪用过滤嘴\n[BBOX-29] 肺炎支原体IgM抗体免疫\n[BBOX-30] 肺炎支原体IgG抗体免疫C反应蛋白测定\n[BBOX-31] 室\n[BBOX-32] 室\n[BBOX-33] 磷酸可待因片<15mg>\n[BBOX-34] 用量：1.000片/次\n[BBOX-35] 用法：口服，一次/日，5天\n[BBOX-36] 桉柠蒎肠溶胶囊<桉柠蒎油计0.3g/粒>\n[BBOX-37] 用量：1.000粒/次\n[BBOX-38] 用法：口服，二次/日，7天\n[BBOX-39] 签名：\n[BBOX-40] 内蒙古医科大学附属医院门诊病历\n[BBOX-41] 姓名：\n[BBOX-42] 年龄：54岁\n[BBOX-43] 诊疗号：0010304094\n[BBOX-44] 民族：蒙古\n[BBOX-45] 性别：女性\n[BBOX-46] 科室：呼吸内科门诊\n[BBOX-47] 联系电话：\n[BBOX-48] 身份证：\n[BBOX-49] 病情：\n[BBOX-50] 就诊状态：\n[BBOX-51] 就诊时间：2024-03-01 09:48\n[BBOX-52] 生命体征（需要时）：\n[BBOX-53] 体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg\n[BBOX-54] 主诉：诊断支气管哮喘10余年，加重1月。\n[BBOX-55] 现病史：诊断支气管哮喘10余年，加重1月。夜间发作，咳白色粘痰，有黄\n[BBOX-56] 色鼻涕。每日吸入信必可都保，症状无改善。\n[BBOX-57] 既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎\n[BBOX-58] 无，吸烟史无，无过敏史。鼻炎\n[BBOX-59] 体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺干鸣音，双\n[BBOX-60] 下肢无水肿，体重kg。\n[BBOX-61] 辅助检查：待回报\n[BBOX-62] 过敏史：不详\n[BBOX-63] 初步诊断（西医）：1.支气管哮喘 2.过敏性鼻炎[变应性鼻炎]\n[BBOX-64] 初步诊断（中医）：\n[BBOX-65] 治疗方案：\n[BBOX-66] 多索茶碱片<0.2g>\n[BBOX-67] 用量：0.200g/次\n[BBOX-68] 用法：口服，一次/日，7天\n[BBOX-69] 布地奈德福莫特罗吸入粉雾剂\n[BBOX-70] 用量：1.000吸/次\n[BBOX-71] (Ⅱ)<(160μg/4.5μg)/吸*60>\n[BBOX-72] 用法：吸入，二次/日，3天\n[BBOX-73] 签名：李\n[BBOX-74] 鹤春堂大药房\n[BBOX-75] 2026-01-21 17:23:52\n[BBOX-76] 收银员：张星\n[BBOX-77] 名称 单价 数量 金额\n[BBOX-78] 布地奈德福莫特罗吸入粉雾剂(Ⅱ)\n[BBOX-79] 320 μg /9 μg / 吸 60 吸 / 支\n[BBOX-80] 298.00 2 596.00\n[BBOX-81] 应收金额: 596.00\n[BBOX-82] 实收金额: 596.00\n[BBOX-83] 找零: 0.00\n[BBOX-84] 优惠: 0.00\n[BBOX-85] 会员:\n[BBOX-86] 本次积分: 596\n[BBOX-87] 合计积分: 1325\n[BBOX-88] 祝您身体健康，药品属于特殊商品\n[BBOX-89] 无质量问题，概不退换\n[BBOX-90] 11:43\n[BBOX-91] 美团\n[BBOX-92] 5G\n[BBOX-93] 4G\n[BBOX-94] 24\n[BBOX-95] 电子票预览\n[BBOX-96] www.chinaebill.cn\n[BBOX-97] 内蒙古自治区医疗门诊收费票据（电子）\n[BBOX-98] 内蒙古\n[BBOX-99] 财政部监制\n[BBOX-100] 票据代码：15060125\n[BBOX-101] 票据号码：0127705695\n[BBOX-102] 交款人\n[BBOX-103] 用代码：150102********2023\n[BBOX-104] 校验码：55e825\n[BBOX-105] 交\n[BBOX-106] 开票日期：2026-02-12\n[BBOX-107] 数量/单位\n[BBOX-108] 金额（元）\n[BBOX-109] 备注\n[BBOX-110] 项目名称\n[BBOX-111] 数量/单位\n[BBOX-112] 金额（元）\n[BBOX-113] 备注\n[BBOX-114] 西药费\n[BBOX-115] 1\n[BBOX-116] 项\n[BBOX-117] 188.21\n[BBOX-118] 金额合计（大写）壹佰捌拾捌元贰角壹分\n[BBOX-119] (小写)188.21\n[BBOX-120] 业务流水号：202602120002043\n[BBOX-121] 门诊号：2602120916\n[BBOX-122] 就诊日期：20260212\n[BBOX-123] 其\n[BBOX-124] 医疗机构类型：综合医院\n[BBOX-125] 医保类型：职工基本医疗保险\n[BBOX-126] 医保编号：150000NMGZG00000000001\n[BBOX-127] 性别：女\n[BBOX-128] 9506\n[BBOX-129] 信\n[BBOX-130] 医保统筹基金支付：101.92\n[BBOX-131] 其他支付：0.00\n[BBOX-132] 个人账户支付：86.29\n[BBOX-133] 个人现金支付：0.00\n[BBOX-134] 息\n[BBOX-135] 个人自付：86.29\n[BBOX-136] 个人自费：0.00\n[BBOX-137] 交费日期：20260212\n[BBOX-138] 备注：医保总金额：188.21符合统筹：169.87账户余额：4301.09医疗救助基金：0大病保险：0公务员补助：0\n[BBOX-139] 医疗收费专用章\n[BBOX-140] 支付：0企业补充保险：0符合政策范围金额：169.87其他基金：0伙食补助：0起付线：0\n[BBOX-141] （章）：内蒙古自治区国际蒙医医院\n[BBOX-142] 复核人：李姹娜\n[BBOX-143] 收款人：李姹娜\n[BBOX-144] 查看收费明细\n[BBOX-145] 发送到邮箱\n[BBOX-146] 15:38\n[BBOX-147] 954\n[BBOX-148] wwwwwwwwwwwwwwwwww.pdf\n[BBOX-149] 电子发票(普通发票)\n[BBOX-150] 国家税务总局\n[BBOX-151] 内蒙古自治区税务局\n[BBOX-152] 发票号码：26152000000173167231\n[BBOX-153] 开票日期：2026年03月04日\n[BBOX-154] 购买方信息\n[BBOX-155] 统一社会信用代码/纳税人识别号：150102197111182023\n[BBOX-156] 销售方信息\n[BBOX-157] 名称：国药控股国大药房内蒙古有限公司\n[BBOX-158] 统一社会信用代码/纳税人识别号：911501005732872139\n[BBOX-159] 项目名称\n[BBOX-160] 规格型号\n[BBOX-161] 单位\n[BBOX-162] 数量\n[BBOX-163] 单价\n[BBOX-164] 金额\n[BBOX-165] 税率/征收率\n[BBOX-166] 税额\n[BBOX-167] *化学药品制剂*布地奈德\n[BBOX-168] 320ug:9ug*60吸\n[BBOX-169] 盒\n[BBOX-170] 1\n[BBOX-171] 274.336283185841\n[BBOX-172] 274.34\n[BBOX-173] 13%\n[BBOX-174] 35.66\n[BBOX-175] 福莫特罗吸入粉雾剂（）\n[BBOX-176] 合计\n[BBOX-177] ￥274.34\n[BBOX-178] ￥35.66\n[BBOX-179] 价税合计（大写）\n[BBOX-180] 叁佰壹拾圆整\n[BBOX-181] (小写)￥310.00\n[BBOX-182] 备注\n[BBOX-183] 开票人：刘惠\n[BBOX-184] 号号:D20214...医保余额:3631.8CM/KG普通病人|现住址:内蒙古自治区呼和浩特市赛罕区\n[BBOX-185] 报告\n[BBOX-186] 闭环管理\n[BBOX-187] 治疗\n[BBOX-188] 健康调阅\n[BBOX-189] 三诺血糖\n[BBOX-190] 华益血糖\n[BBOX-191] 门诊记录:\n[BBOX-192] □痕迹\n[BBOX-193] □批注\n[BBOX-194] 历信息\n[BBOX-195] 内蒙古医科大学附属医院门诊病历\n[BBOX-196] 姓名\n[BBOX-197] 年龄:51岁\n[BBOX-198] 诊疗号:0010304094\n[BBOX-199] 民族:蒙古族\n[BBOX-200] 性别:女性\n[BBOX-201] 科室:呼吸内科门诊\n[BBOX-202] 联系电话:\n[BBOX-203] 身份证:\n[BBOX-204] 病情:\n[BBOX-205] 就诊状态:\n[BBOX-206] 就诊时间:2023-03-0410:51\n[BBOX-207] 生命体征(需要时):\n[BBOX-208] 体温:℃脉搏:次/分呼吸:次/分血压:/mmHg\n[BBOX-209] 主诉:咳嗽1月,哮喘病史10余年\n[BBOX-210] 现病史:\n[BBOX-211] 既往史:患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎\n[BBOX-212] 有,20年,吸烟史无,无过敏史。\n[BBOX-213] 体格检查:发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰\n[BBOX-214] 音,双下肢无水肿,体重kg。\n[BBOX-215] 辅助检查:肺功能正常\n[BBOX-216] 过敏史:\n[BBOX-217] 初步诊断(西医):1.支气管哮喘\n[BBOX-218] 初步诊断(中医):\n[BBOX-219] 治疗方案:\n[BBOX-220] CT胸部\n[BBOX-221] 最大通气量功能检查呼吸过滤器\n[BBOX-222] 肺弥散功能检查--口残气容积测定-氮气平肺通气功能检查\n[BBOX-223] 气法\n[BBOX-224] 衡法\n[BBOX-225] 孟鲁司特钠片<10mg>\n[BBOX-226] 用量:1.000片/次\n[BBOX-227] 用法:口服,一次/每晚,7天\n[BBOX-228] 布地奈德福莫特罗吸入粉雾剂(11)\n[BBOX-229] 用量:1.000吸/次\n[BBOX-230] <(320μg/9μg)/吸*60>\n[BBOX-231] 用法:吸入,二次/日,7天\n[BBOX-232] 签名:\n[BBOX-233] 付丹\n[BBOX-234] 26星期二\n[BBOX-235] 190.1.48.233\n[BBOX-236] 王王立\n[BBOX-237] 内蒙古自治区国际蒙医医院\n[BBOX-238] 门诊病历\n[BBOX-239] 门诊号：2602120916\n[BBOX-240] 姓\n[BBOX-241] 科室：呼吸与危重症医学科门 性别：女性 出生年月：1971-11-18\n[BBOX-242] 诊\n[BBOX-243] 就诊时间：2026-02-12 11:20\n[BBOX-244] ○初诊◎复诊\n[BBOX-245] 过敏史：□否 □不详 □有：\n[BBOX-246] 主 诉：发作性咳嗽、气短5年，加重3天\n[BBOX-247] 现病史：5年前出现发作性咳嗽、气短，吸入刺激性气味后症状明显，就诊于当地医院诊断\n[BBOX-248] 为“支气管哮喘”，长期规律吸入信必可治疗后效果欠佳。近3天喘息加重，伴咳嗽、咳痰较前\n[BBOX-249] 频繁。夜间明显。\n[BBOX-250] 既往史：体健\n[BBOX-251] 家族史：无\n[BBOX-252] 体格检查：意识：清醒\n[BBOX-253] T：36.5℃ P：71次/分 R：18次/分 BP：115/77mmHg\n[BBOX-254] 双肺可闻及干鸣音\n[BBOX-255] 辅助检查：\n[BBOX-256] 处方信息：\n[BBOX-257] 布地奈德福莫特罗吸入粉雾剂（II）(160μg/4.5μg/吸*60吸/支)*1支\n[BBOX-258] 320μg 吸入 bid\n[BBOX-259] 醋酸泼尼松片(5mg*100片/瓶)*1瓶\n[BBOX-260] 15mg 口服 qd\n[BBOX-261] 其他处置：\n[BBOX-262] 复诊记录：\n[BBOX-263] 门诊诊断：支气管哮喘(急性发作期)\n[BBOX-264] 医生签名：苏佳\n[BBOX-265] 医疗收费明细（电子）\n[BBOX-266] 所属电\n[BBOX-267] 15060125\n[BBOX-268] 所属电子票据号码:0127705695\n[BBOX-269] 交\n[BBOX-270] 开票日期:2026年02月12日\n[BBOX-271] 项目名称\n[BBOX-272] 数量/单位\n[BBOX-273] 金额（元）\n[BBOX-274] 备注\n[BBOX-275] 西药费(小计:188.2100元)\n[BBOX-276] 布地奈德福莫特罗吸入粉雾剂（II）\n[BBOX-277] 60\n[BBOX-278] 吸\n[BBOX-279] 183.4100\n[BBOX-280] 乙\n[BBOX-281] 醋酸泼尼松片\n[BBOX-282] 100\n[BBOX-283] 片\n[BBOX-284] 4.8000\n[BBOX-285] 甲\n[BBOX-286] 小计 188.2100\n[BBOX-287] 合计 188.2100\n[BBOX-288] 收款单位（章）内蒙古自治区国际蒙医医院\n[BBOX-289] 1 页 共 1 页\n[BBOX-290] 鹤春堂大药房\n[BBOX-291] 2025-12-26 12:29:31\n[BBOX-292] 收银员：张星\n[BBOX-293] 名称 单价 数量 金额\n[BBOX-294] 布地奈德福莫特罗吸入粉雾剂(II)\n[BBOX-295] 320 μg /9 μg / 吸 60 吸 / 支\n[BBOX-296] 298.00 1 298.00\n[BBOX-297] 应收金额: 298.00\n[BBOX-298] 实收金额: 298.00\n[BBOX-299] 找零: 0.00\n[BBOX-300] 优惠: 0.00\n[BBOX-301] 会员:\n[BBOX-302] 本次积分: 298\n[BBOX-303] 合计积分: 729\n[BBOX-304] 祝您身体健康，药品属于特殊商品\n[BBOX-305] 无质量问题，概不退换"
  }
]
2026-08-10 12:43:20,698 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:43:20,712 INFO     29 [SmartSplitter] SmartSplitter done: 9 chunks from 9 LLM segments (all bbox_id). Types: {'OutpatientRecord': 4, 'MedicationRecord': 5}
2026-08-10 12:43:20,718 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 12:43:20,719 INFO     29 [Trace] task=ed8cac48 | doc=麦济WRNA(2).pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "306 items", "markdown": "", "text": "", "name": "麦济WRNA(2).pdf", "output_format": "chunks", "chunks": "9 items, types={'OutpatientRecord': 4, 'MedicationRecord': 5}"}
2026-08-10 12:43:20,719 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 12:43:20,719 INFO     29 [ChunkRouter] Routed 9 chunks into 2 groups: {'chunks_Clinical': 4, 'chunks_Medication': 5}
2026-08-10 12:43:20,726 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 12:43:20,726 INFO     29 [Trace] task=ed8cac48 | doc=麦济WRNA(2).pdf | ChunkRouter:Router | outputs={"html": "", "json": "306 items", "markdown": "", "text": "", "name": "麦济WRNA(2).pdf", "output_format": "chunks", "chunks": "9 items, types={'OutpatientRecord': 4, 'MedicationRecord': 5}", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Medication\": 5}"}
2026-08-10 12:43:20,726 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 12:43:20,730 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:43:20,730 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:43:21,322 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:43:21,334 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 12:43:21,334 INFO     29 [Trace] task=ed8cac48 | doc=麦济WRNA(2).pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "306 items", "markdown": "", "text": "", "name": "麦济WRNA(2).pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Medication\": 5}"}
2026-08-10 12:43:21,334 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 12:43:21,342 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:43:21,343 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:43:21,792 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:43:21,801 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 12:43:21,801 INFO     29 [Trace] task=ed8cac48 | doc=麦济WRNA(2).pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "306 items", "markdown": "", "text": "", "name": "麦济WRNA(2).pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Medication\": 5}"}
2026-08-10 12:43:21,802 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 12:43:21,809 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:43:21,810 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:43:21,810 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 12:43:21,810 INFO     29 [qwen-vl-text] positions(40): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:43:21,810 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [40]
2026-08-10 12:43:22,101 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:43:22,102 INFO     29 [qwen-vl-text] LLM extraction start, text_len=523
2026-08-10 12:43:22,102 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:43:22,103 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 39, \"encounter_dates\": [\"2026-02-27\"], \"department\": \"呼吸内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "内蒙古医科大学附属医院门诊病历\n姓名：\n年龄：54岁\n诊疗号：0010304094\n民族：蒙古\n性别：女性\n科室：呼吸内科门诊\n联系电话：\n身份证：\n病情：\n就诊状态：\n就诊时间：2026-02-27 16:58\n生命体征（需要时）：\n体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg\n主诉：诊断支气管哮喘10余年，加重1月。\n现病史：诊断支气管哮喘10余年，加重1月。夜间发作，咳白色粘痰，有黄\n色鼻涕。每日吸入信必可都保，症状无改善。\n既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎\n无，吸烟史无，无过敏史。\n体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺未闻及啰\n音，双下肢无水肿，体重kg。\n辅助检查：待回报\n过敏史：不详\n初步诊断（西医）：1.支气管哮喘\n初步诊断（中医）：\n治疗方案：随诊\n血常规\n免疫球蛋白IgE\n一次性肺功能仪用过滤嘴\n肺炎支原体IgM抗体免疫\n肺炎支原体IgG抗体免疫C反应蛋白测定\n室\n室\n磷酸可待因片<15mg>\n用量：1.000片/次\n用法：口服，一次/日，5天\n桉柠蒎肠溶胶囊<桉柠蒎油计0.3g/粒>\n用量：1.000粒/次\n用法：口服，二次/日，7天\n签名：",
    "role": "user"
  }
]
2026-08-10 12:43:24,758 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:43:24,758 INFO     29 [qwen-vl-text] LLM output (len=553):
{
  "encounter_date": "2026-02-27",
  "chief_complaint": "诊断支气管哮喘10余年，加重1月。",
  "present_illness": "诊断支气管哮喘10余年，加重1月。夜间发作，咳白色粘痰，有黄色鼻涕。每日吸入信必可都保，症状无改善。",
  "past_history": "患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎无，吸烟史无，无过敏史。",
  "diagnosis": "1.支气管哮喘",
  "treatment_plan": [
    {
      "drug_name": "磷酸可待因片",
      "dosage": "1.000片/次",
      "frequency": "一次/日",
      "duration": "5天",
      "route": "口服"
    },
    {
      "drug_name": "桉柠蒎肠溶胶囊",
      "dosage": "1.000粒/次",
      "frequency": "二次/日",
      "duration": "7天",
      "route": "口服"
    }
  ]
}
2026-08-10 12:43:24,758 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-27]
2026-08-10 12:43:24,761 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1780023, prompt_len=1256
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共40行）
["内蒙古医科大学附属医院门诊病历", "姓名：", "年龄：54岁", "诊疗号：0010304094", "民族：蒙古", "性别：女性", "科室：呼吸内科门诊", "联系电话：", "身份证：", "病情：", "就诊状态：", "就诊时间：2026-02-27 16:58", "生命体征（需要时）：", "体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg", "主诉：诊断支气管哮喘10余年，加重1月。", "现病史：诊断支气管哮喘10余年，加重1月。夜间发作，咳白色粘痰，有黄", "色鼻涕。每日吸入信必可都保，症状无改善。", "既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "无，吸烟史无，无过敏史。", "体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺未闻及啰", "音，双下肢无水肿，体重kg。", "辅助检查：待回报", "过敏史：不详", "初步诊断（西医）：1.支气管哮喘", "初步诊断（中医）：", "治疗方案：随诊", "血常规", "免疫球蛋白IgE", "一次性肺功能仪用过滤嘴", "肺炎支原体IgM抗体免疫", "肺炎支原体IgG抗体免疫C反应蛋白测定", "室", "室", "磷酸可待因片<15mg>", "用量：1.000片/次", "用法：口服，一次/日，5天", "桉柠蒎肠溶胶囊<桉柠蒎油计0.3g/粒>", "用量：1.000粒/次", "用法：口服，二次/日，7天", "签名："]

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
2026-08-10 12:43:37,011 INFO     29 [qwen-vl-text] coord API raw response (len=2282):
[
	{"text": "内蒙古医科大学附属医院门诊病历", "bbox": [262, 80, 783, 107]},
	{"text": "姓名：", "bbox": [98, 114, 157, 132]},
	{"text": "年龄：54岁", "bbox": [353, 114, 481, 132]},
	{"text": "诊疗号：0010304094", "bbox": [604, 112, 824, 130]},
	{"text": "民族：蒙古", "bbox": [99, 138, 224, 155]},
	{"text": "性别：女性", "bbox": [353, 138, 479, 155]},
	{"text": "科室：呼吸内科门诊", "bbox": [604, 135, 827, 152]},
	{"text": "联系电话：", "bbox": [98, 160, 208, 178]},
	{"text": "身份证：", "bbox": [400, 160, 479, 178]},
	{"text": "病情：", "bbox": [768, 158, 827, 176]},
	{"text": "就诊状态：", "bbox": [99, 183, 208, 201]},
	{"text": "就诊时间：2026-02-27 16:58", "bbox": [339, 183, 670, 200]},
	{"text": "生命体征（需要时）：", "bbox": [100, 206, 333, 224]},
	{"text": "体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg", "bbox": [100, 230, 592, 248]},
	{"text": "主诉：诊断支气管哮喘10余年，加重1月。", "bbox": [100, 253, 592, 272]},
	{"text": "现病史：诊断支气管哮喘10余年，加重1月。夜间发作，咳白色粘痰，有黄", "bbox": [100, 276, 945, 295]},
	{"text": "色鼻涕。每日吸入信必可都保，症状无改善。", "bbox": [208, 300, 687, 319]},
	{"text": "既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "bbox": [100, 324, 942, 343]},
	{"text": "无，吸烟史无，无过敏史。", "bbox": [208, 348, 490, 367]},
	{"text": "体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺未闻及啰", "bbox": [102, 373, 913, 392]},
	{"text": "音，双下肢无水肿，体重kg。", "bbox": [232, 398, 545, 417]},
	{"text": "辅助检查：待回报", "bbox": [100, 423, 307, 442]},
	{"text": "过敏史：不详", "bbox": [100, 447, 281, 466]},
	{"text": "初步诊断（西医）：1.支气管哮喘", "bbox": [102, 470, 475, 490]},
	{"text": "初步诊断（中医）：", "bbox": [102, 494, 310, 513]},
	{"text": "治疗方案：随诊", "bbox": [102, 518, 284, 537]},
	{"text": "血常规", "bbox": [108, 551, 182, 569]},
	{"text": "免疫球蛋白IgE", "bbox": [394, 551, 558, 569]},
	{"text": "一次性肺功能仪用过滤嘴", "bbox": [680, 551, 938, 569]},
	{"text": "肺炎支原体IgM抗体免疫", "bbox": [108, 576, 375, 594]},
	{"text": "肺炎支原体IgG抗体免疫 C反应蛋白测定", "bbox": [394, 576, 835, 594]},
	{"text": "室", "bbox": [108, 595, 133, 612]},
	{"text": "室", "bbox": [394, 595, 417, 612]},
	{"text": "磷酸可待因片<15mg>", "bbox": [104, 620, 324, 638]},
	{"text": "用量：1.000片/次", "bbox": [599, 618, 795, 636]},
	{"text": "用法：口服，一次/日，5天", "bbox": [143, 645, 439, 664]},
	{"text": "桉柠蒎肠溶胶囊<桉柠蒎油计0.3g/粒>", "bbox": [105, 671, 539, 690]},
	{"text": "用量：1.000粒/次", "bbox": [599, 670, 795, 688]},
	{"text": "用法：口服，二次/日，7天", "bbox": [144, 696, 440, 715]},
	{"text": "签名：", "bbox": [576, 788, 677, 812]}
]
2026-08-10 12:43:37,012 INFO     29 [qwen-vl-text] coord API: raw_items=40, valid_items=40, elapsed=12.2s
2026-08-10 12:43:37,012 INFO     29 [qwen-vl-text] coord item[0]: text=内蒙古医科大学附属医院门诊病历, bbox=[262, 80, 783, 107]
2026-08-10 12:43:37,012 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[98, 114, 157, 132]
2026-08-10 12:43:37,012 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：54岁, bbox=[353, 114, 481, 132]
2026-08-10 12:43:37,012 INFO     29 [qwen-vl-text] coord item[3]: text=诊疗号：0010304094, bbox=[604, 112, 824, 130]
2026-08-10 12:43:37,012 INFO     29 [qwen-vl-text] coord item[4]: text=民族：蒙古, bbox=[99, 138, 224, 155]
2026-08-10 12:43:37,012 INFO     29 [qwen-vl-text] coord item[5]: text=性别：女性, bbox=[353, 138, 479, 155]
2026-08-10 12:43:37,012 INFO     29 [qwen-vl-text] coord item[6]: text=科室：呼吸内科门诊, bbox=[604, 135, 827, 152]
2026-08-10 12:43:37,012 INFO     29 [qwen-vl-text] coord item[7]: text=联系电话：, bbox=[98, 160, 208, 178]
2026-08-10 12:43:37,012 INFO     29 [qwen-vl-text] coord item[8]: text=身份证：, bbox=[400, 160, 479, 178]
2026-08-10 12:43:37,012 INFO     29 [qwen-vl-text] coord item[9]: text=病情：, bbox=[768, 158, 827, 176]
2026-08-10 12:43:37,012 INFO     29 [qwen-vl-text] coord item[10]: text=就诊状态：, bbox=[99, 183, 208, 201]
2026-08-10 12:43:37,012 INFO     29 [qwen-vl-text] coord item[11]: text=就诊时间：2026-02-27 16:58, bbox=[339, 183, 670, 200]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[12]: text=生命体征（需要时）：, bbox=[100, 206, 333, 224]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[13]: text=体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg, bbox=[100, 230, 592, 248]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[14]: text=主诉：诊断支气管哮喘10余年，加重1月。, bbox=[100, 253, 592, 272]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[15]: text=现病史：诊断支气管哮喘10余年，加重1月。夜间发作，咳白色粘痰，有黄, bbox=[100, 276, 945, 295]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[16]: text=色鼻涕。每日吸入信必可都保，症状无改善。, bbox=[208, 300, 687, 319]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[17]: text=既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎, bbox=[100, 324, 942, 343]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[18]: text=无，吸烟史无，无过敏史。, bbox=[208, 348, 490, 367]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[19]: text=体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺未闻及啰, bbox=[102, 373, 913, 392]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[20]: text=音，双下肢无水肿，体重kg。, bbox=[232, 398, 545, 417]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[21]: text=辅助检查：待回报, bbox=[100, 423, 307, 442]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[22]: text=过敏史：不详, bbox=[100, 447, 281, 466]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[23]: text=初步诊断（西医）：1.支气管哮喘, bbox=[102, 470, 475, 490]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[24]: text=初步诊断（中医）：, bbox=[102, 494, 310, 513]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[25]: text=治疗方案：随诊, bbox=[102, 518, 284, 537]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[26]: text=血常规, bbox=[108, 551, 182, 569]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[27]: text=免疫球蛋白IgE, bbox=[394, 551, 558, 569]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[28]: text=一次性肺功能仪用过滤嘴, bbox=[680, 551, 938, 569]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[29]: text=肺炎支原体IgM抗体免疫, bbox=[108, 576, 375, 594]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[30]: text=肺炎支原体IgG抗体免疫 C反应蛋白测定, bbox=[394, 576, 835, 594]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[31]: text=室, bbox=[108, 595, 133, 612]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[32]: text=室, bbox=[394, 595, 417, 612]
2026-08-10 12:43:37,013 INFO     29 [qwen-vl-text] coord item[33]: text=磷酸可待因片<15mg>, bbox=[104, 620, 324, 638]
2026-08-10 12:43:37,014 INFO     29 [qwen-vl-text] coord item[34]: text=用量：1.000片/次, bbox=[599, 618, 795, 636]
2026-08-10 12:43:37,014 INFO     29 [qwen-vl-text] coord item[35]: text=用法：口服，一次/日，5天, bbox=[143, 645, 439, 664]
2026-08-10 12:43:37,014 INFO     29 [qwen-vl-text] coord item[36]: text=桉柠蒎肠溶胶囊<桉柠蒎油计0.3g/粒>, bbox=[105, 671, 539, 690]
2026-08-10 12:43:37,014 INFO     29 [qwen-vl-text] coord item[37]: text=用量：1.000粒/次, bbox=[599, 670, 795, 688]
2026-08-10 12:43:37,014 INFO     29 [qwen-vl-text] coord item[38]: text=用法：口服，二次/日，7天, bbox=[144, 696, 440, 715]
2026-08-10 12:43:37,014 INFO     29 [qwen-vl-text] coord item[39]: text=签名：, bbox=[576, 788, 677, 812]
2026-08-10 12:43:37,014 INFO     29 [qwen-vl-text] page=0 — 40/40 coords, api_time=12.2s
2026-08-10 12:43:37,014 INFO     29 [qwen-vl-text] new_positions (40):
[[0, 155.89, 465.885, 67.36, 90.094], [0, 58.309999999999995, 93.41499999999999, 95.988, 111.14399999999999], [0, 210.035, 286.195, 95.988, 111.14399999999999], [0, 359.38, 490.28, 94.304, 109.46], [0, 58.904999999999994, 133.28, 116.196, 130.51], [0, 210.035, 285.005, 116.196, 130.51], [0, 359.38, 492.065, 113.67, 127.984], [0, 58.309999999999995, 123.75999999999999, 134.72, 149.876], [0, 238.0, 285.005, 134.72, 149.876], [0, 456.96, 492.065, 133.036, 148.192], [0, 58.904999999999994, 123.75999999999999, 154.08599999999998, 169.242], [0, 201.70499999999998, 398.65, 154.08599999999998, 168.4], [0, 59.5, 198.135, 173.452, 188.608], [0, 59.5, 352.24, 193.66, 208.816], [0, 59.5, 352.24, 213.02599999999998, 229.024], [0, 59.5, 562.275, 232.392, 248.39], [0, 123.75999999999999, 408.765, 252.6, 268.598], [0, 59.5, 560.49, 272.808, 288.806], [0, 123.75999999999999, 291.55, 293.01599999999996, 309.014], [0, 60.69, 543.235, 314.066, 330.06399999999996], [0, 138.04, 324.275, 335.116, 351.114], [0, 59.5, 182.665, 356.166, 372.164], [0, 59.5, 167.195, 376.37399999999997, 392.372], [0, 60.69, 282.625, 395.74, 412.58], [0, 60.69, 184.45, 415.948, 431.94599999999997], [0, 60.69, 168.98, 436.156, 452.154], [0, 64.25999999999999, 108.28999999999999, 463.942, 479.09799999999996], [0, 234.42999999999998, 332.01, 463.942, 479.09799999999996], [0, 404.59999999999997, 558.11, 463.942, 479.09799999999996], [0, 64.25999999999999, 223.125, 484.99199999999996, 500.14799999999997], [0, 234.42999999999998, 496.825, 484.99199999999996, 500.14799999999997], [0, 64.25999999999999, 79.13499999999999, 500.99, 515.304], [0, 234.42999999999998, 248.11499999999998, 500.99, 515.304], [0, 61.879999999999995, 192.78, 522.04, 537.196], [0, 356.405, 473.025, 520.356, 535.512], [0, 85.085, 261.205, 543.09, 559.088], [0, 62.474999999999994, 320.705, 564.982, 580.98], [0, 356.405, 473.025, 564.14, 579.2959999999999], [0, 85.67999999999999, 261.8, 586.0319999999999, 602.03], [0, 342.71999999999997, 402.815, 663.496, 683.704]]
2026-08-10 12:43:37,014 INFO     29 [qwen-vl-text] ═══ DONE ═══ 40 positions, pages=1, time=15.2s
2026-08-10 12:43:37,015 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:43:37,016 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:43:37,016 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 12:43:37,017 INFO     29 [qwen-vl-text] positions(34): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:43:37,017 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [34]
2026-08-10 12:43:37,379 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:43:37,381 INFO     29 [qwen-vl-text] LLM extraction start, text_len=491
2026-08-10 12:43:37,381 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:43:37,382 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 40, \"bbox_end\": 73, \"encounter_dates\": [\"2024-03-01\"], \"department\": \"呼吸内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "内蒙古医科大学附属医院门诊病历\n姓名：\n年龄：54岁\n诊疗号：0010304094\n民族：蒙古\n性别：女性\n科室：呼吸内科门诊\n联系电话：\n身份证：\n病情：\n就诊状态：\n就诊时间：2024-03-01 09:48\n生命体征（需要时）：\n体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg\n主诉：诊断支气管哮喘10余年，加重1月。\n现病史：诊断支气管哮喘10余年，加重1月。夜间发作，咳白色粘痰，有黄\n色鼻涕。每日吸入信必可都保，症状无改善。\n既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎\n无，吸烟史无，无过敏史。鼻炎\n体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺干鸣音，双\n下肢无水肿，体重kg。\n辅助检查：待回报\n过敏史：不详\n初步诊断（西医）：1.支气管哮喘 2.过敏性鼻炎[变应性鼻炎]\n初步诊断（中医）：\n治疗方案：\n多索茶碱片<0.2g>\n用量：0.200g/次\n用法：口服，一次/日，7天\n布地奈德福莫特罗吸入粉雾剂\n用量：1.000吸/次\n(Ⅱ)<(160μg/4.5μg)/吸*60>\n用法：吸入，二次/日，3天\n签名：李",
    "role": "user"
  }
]
2026-08-10 12:43:37,385 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:43:37.384+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 31, "failed": 0, "current": {"ed8cac4894b811f1bd9827cf206dfa2d": {"id": "ed8cac4894b811f1bd9827cf206dfa2d", "doc_id": "ed520a7a94b811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWRNA(2).pdf", "type": "pdf", "location": "\u9ea6\u6d4eWRNA(2).pdf", "size": 13028580, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786365740553, "task_type": "dataflow", "root_trace_id": "cdcb62f1323147c19d5b537cd2e3ed24", "root_traceparent": "00-cdcb62f1323147c19d5b537cd2e3ed24-dbd2f127625489c0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:43:40,840 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:43:40,841 INFO     29 [qwen-vl-text] LLM output (len=657):
{
  "encounter_date": "2024-03-01",
  "chief_complaint": "诊断支气管哮喘10余年，加重1月。",
  "present_illness": "诊断支气管哮喘10余年，加重1月。夜间发作，咳白色粘痰，有黄色鼻涕。每日吸入信必可都保，症状无改善。",
  "past_history": "患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎无，吸烟史无，无过敏史。鼻炎",
  "diagnosis": "西医：1.支气管哮喘 2.过敏性鼻炎[变应性鼻炎]",
  "treatment_plan": [
    {
      "drug_name": "多索茶碱片",
      "specification": "0.2g",
      "dosage": "0.200g/次",
      "route": "口服",
      "frequency": "一次/日",
      "duration": "7天"
    },
    {
      "drug_name": "布地奈德福莫特罗吸入粉雾剂(Ⅱ)",
      "specification": "(160μg/4.5μg)/吸*60",
      "dosage": "1.000吸/次",
      "route": "吸入",
      "frequency": "二次/日",
      "duration": "3天"
    }
  ]
}
2026-08-10 12:43:40,841 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-03-01]
2026-08-10 12:43:40,851 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2140644, prompt_len=1206
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共34行）
["内蒙古医科大学附属医院门诊病历", "姓名：", "年龄：54岁", "诊疗号：0010304094", "民族：蒙古", "性别：女性", "科室：呼吸内科门诊", "联系电话：", "身份证：", "病情：", "就诊状态：", "就诊时间：2024-03-01 09:48", "生命体征（需要时）：", "体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg", "主诉：诊断支气管哮喘10余年，加重1月。", "现病史：诊断支气管哮喘10余年，加重1月。夜间发作，咳白色粘痰，有黄", "色鼻涕。每日吸入信必可都保，症状无改善。", "既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "无，吸烟史无，无过敏史。鼻炎", "体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺干鸣音，双", "下肢无水肿，体重kg。", "辅助检查：待回报", "过敏史：不详", "初步诊断（西医）：1.支气管哮喘 2.过敏性鼻炎[变应性鼻炎]", "初步诊断（中医）：", "治疗方案：", "多索茶碱片<0.2g>", "用量：0.200g/次", "用法：口服，一次/日，7天", "布地奈德福莫特罗吸入粉雾剂", "用量：1.000吸/次", "(Ⅱ)<(160μg/4.5μg)/吸*60>", "用法：吸入，二次/日，3天", "签名：李"]

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
2026-08-10 12:43:52,367 INFO     29 [qwen-vl-text] coord API raw response (len=1989):
[
	{"text": "内蒙古医科大学附属医院门诊病历", "bbox": [268, 82, 790, 110]},
	{"text": "姓名：", "bbox": [103, 115, 158, 134]},
	{"text": "年龄：54岁", "bbox": [360, 114, 489, 133]},
	{"text": "诊疗号：0010304094", "bbox": [612, 114, 831, 133]},
	{"text": "民族：蒙古", "bbox": [104, 140, 235, 158]},
	{"text": "性别：女性", "bbox": [360, 138, 484, 156]},
	{"text": "科室：呼吸内科门诊", "bbox": [614, 137, 833, 155]},
	{"text": "联系电话：", "bbox": [104, 163, 212, 181]},
	{"text": "身份证：", "bbox": [407, 161, 481, 179]},
	{"text": "病情：", "bbox": [775, 160, 833, 178]},
	{"text": "就诊状态：", "bbox": [104, 185, 212, 203]},
	{"text": "就诊时间：2024-03-01 09:48", "bbox": [344, 183, 677, 201]},
	{"text": "生命体征（需要时）：", "bbox": [104, 206, 338, 225]},
	{"text": "体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg", "bbox": [104, 230, 598, 249]},
	{"text": "主诉：诊断支气管哮喘10余年，加重1月。", "bbox": [104, 253, 598, 272]},
	{"text": "现病史：诊断支气管哮喘10余年，加重1月。夜间发作，咳白色粘痰，有黄", "bbox": [104, 276, 951, 296]},
	{"text": "色鼻涕。每日吸入信必可都保，症状无改善。", "bbox": [211, 300, 691, 320]},
	{"text": "既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "bbox": [104, 325, 950, 344]},
	{"text": "无，吸烟史无，无过敏史。鼻炎", "bbox": [211, 349, 554, 368]},
	{"text": "体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺干鸣音，双", "bbox": [104, 373, 947, 392]},
	{"text": "下肢无水肿，体重kg。", "bbox": [237, 398, 476, 417]},
	{"text": "辅助检查：待回报", "bbox": [103, 424, 310, 443]},
	{"text": "过敏史：不详", "bbox": [104, 448, 284, 467]},
	{"text": "初步诊断（西医）：1.支气管哮喘 2.过敏性鼻炎[变应性鼻炎]", "bbox": [104, 469, 782, 490]},
	{"text": "初步诊断（中医）：", "bbox": [104, 495, 312, 514]},
	{"text": "治疗方案：", "bbox": [104, 519, 211, 537]},
	{"text": "多索茶碱片<0.2g>", "bbox": [104, 577, 298, 596]},
	{"text": "用量：0.200g/次", "bbox": [600, 574, 778, 592]},
	{"text": "用法：口服，一次/日，7天", "bbox": [141, 601, 440, 620]},
	{"text": "布地奈德福莫特罗吸入粉雾剂", "bbox": [104, 626, 422, 646]},
	{"text": "用量：1.000吸/次", "bbox": [600, 624, 795, 642]},
	{"text": "(Ⅱ)<(160μg/4.5μg)/吸*60>", "bbox": [106, 661, 437, 680]},
	{"text": "用法：吸入，二次/日，3天", "bbox": [141, 684, 439, 703]},
	{"text": "签名：李", "bbox": [573, 773, 725, 803]}
]
2026-08-10 12:43:52,367 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=11.5s
2026-08-10 12:43:52,367 INFO     29 [qwen-vl-text] coord item[0]: text=内蒙古医科大学附属医院门诊病历, bbox=[268, 82, 790, 110]
2026-08-10 12:43:52,368 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[103, 115, 158, 134]
2026-08-10 12:43:52,368 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：54岁, bbox=[360, 114, 489, 133]
2026-08-10 12:43:52,368 INFO     29 [qwen-vl-text] coord item[3]: text=诊疗号：0010304094, bbox=[612, 114, 831, 133]
2026-08-10 12:43:52,368 INFO     29 [qwen-vl-text] coord item[4]: text=民族：蒙古, bbox=[104, 140, 235, 158]
2026-08-10 12:43:52,368 INFO     29 [qwen-vl-text] coord item[5]: text=性别：女性, bbox=[360, 138, 484, 156]
2026-08-10 12:43:52,368 INFO     29 [qwen-vl-text] coord item[6]: text=科室：呼吸内科门诊, bbox=[614, 137, 833, 155]
2026-08-10 12:43:52,368 INFO     29 [qwen-vl-text] coord item[7]: text=联系电话：, bbox=[104, 163, 212, 181]
2026-08-10 12:43:52,368 INFO     29 [qwen-vl-text] coord item[8]: text=身份证：, bbox=[407, 161, 481, 179]
2026-08-10 12:43:52,368 INFO     29 [qwen-vl-text] coord item[9]: text=病情：, bbox=[775, 160, 833, 178]
2026-08-10 12:43:52,368 INFO     29 [qwen-vl-text] coord item[10]: text=就诊状态：, bbox=[104, 185, 212, 203]
2026-08-10 12:43:52,368 INFO     29 [qwen-vl-text] coord item[11]: text=就诊时间：2024-03-01 09:48, bbox=[344, 183, 677, 201]
2026-08-10 12:43:52,368 INFO     29 [qwen-vl-text] coord item[12]: text=生命体征（需要时）：, bbox=[104, 206, 338, 225]
2026-08-10 12:43:52,368 INFO     29 [qwen-vl-text] coord item[13]: text=体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg, bbox=[104, 230, 598, 249]
2026-08-10 12:43:52,368 INFO     29 [qwen-vl-text] coord item[14]: text=主诉：诊断支气管哮喘10余年，加重1月。, bbox=[104, 253, 598, 272]
2026-08-10 12:43:52,368 INFO     29 [qwen-vl-text] coord item[15]: text=现病史：诊断支气管哮喘10余年，加重1月。夜间发作，咳白色粘痰，有黄, bbox=[104, 276, 951, 296]
2026-08-10 12:43:52,368 INFO     29 [qwen-vl-text] coord item[16]: text=色鼻涕。每日吸入信必可都保，症状无改善。, bbox=[211, 300, 691, 320]
2026-08-10 12:43:52,368 INFO     29 [qwen-vl-text] coord item[17]: text=既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎, bbox=[104, 325, 950, 344]
2026-08-10 12:43:52,369 INFO     29 [qwen-vl-text] coord item[18]: text=无，吸烟史无，无过敏史。鼻炎, bbox=[211, 349, 554, 368]
2026-08-10 12:43:52,369 INFO     29 [qwen-vl-text] coord item[19]: text=体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺干鸣音，双, bbox=[104, 373, 947, 392]
2026-08-10 12:43:52,369 INFO     29 [qwen-vl-text] coord item[20]: text=下肢无水肿，体重kg。, bbox=[237, 398, 476, 417]
2026-08-10 12:43:52,369 INFO     29 [qwen-vl-text] coord item[21]: text=辅助检查：待回报, bbox=[103, 424, 310, 443]
2026-08-10 12:43:52,369 INFO     29 [qwen-vl-text] coord item[22]: text=过敏史：不详, bbox=[104, 448, 284, 467]
2026-08-10 12:43:52,369 INFO     29 [qwen-vl-text] coord item[23]: text=初步诊断（西医）：1.支气管哮喘 2.过敏性鼻炎[变应性鼻炎], bbox=[104, 469, 782, 490]
2026-08-10 12:43:52,369 INFO     29 [qwen-vl-text] coord item[24]: text=初步诊断（中医）：, bbox=[104, 495, 312, 514]
2026-08-10 12:43:52,369 INFO     29 [qwen-vl-text] coord item[25]: text=治疗方案：, bbox=[104, 519, 211, 537]
2026-08-10 12:43:52,369 INFO     29 [qwen-vl-text] coord item[26]: text=多索茶碱片<0.2g>, bbox=[104, 577, 298, 596]
2026-08-10 12:43:52,369 INFO     29 [qwen-vl-text] coord item[27]: text=用量：0.200g/次, bbox=[600, 574, 778, 592]
2026-08-10 12:43:52,369 INFO     29 [qwen-vl-text] coord item[28]: text=用法：口服，一次/日，7天, bbox=[141, 601, 440, 620]
2026-08-10 12:43:52,369 INFO     29 [qwen-vl-text] coord item[29]: text=布地奈德福莫特罗吸入粉雾剂, bbox=[104, 626, 422, 646]
2026-08-10 12:43:52,369 INFO     29 [qwen-vl-text] coord item[30]: text=用量：1.000吸/次, bbox=[600, 624, 795, 642]
2026-08-10 12:43:52,369 INFO     29 [qwen-vl-text] coord item[31]: text=(Ⅱ)<(160μg/4.5μg)/吸*60>, bbox=[106, 661, 437, 680]
2026-08-10 12:43:52,369 INFO     29 [qwen-vl-text] coord item[32]: text=用法：吸入，二次/日，3天, bbox=[141, 684, 439, 703]
2026-08-10 12:43:52,369 INFO     29 [qwen-vl-text] coord item[33]: text=签名：李, bbox=[573, 773, 725, 803]
2026-08-10 12:43:52,370 INFO     29 [qwen-vl-text] page=1 — 34/34 coords, api_time=11.5s
2026-08-10 12:43:52,370 INFO     29 [qwen-vl-text] new_positions (34):
[[1, 159.45999999999998, 470.04999999999995, 69.044, 92.61999999999999], [1, 61.285, 94.00999999999999, 96.83, 112.828], [1, 214.2, 290.955, 95.988, 111.98599999999999], [1, 364.14, 494.445, 95.988, 111.98599999999999], [1, 61.879999999999995, 139.825, 117.88, 133.036], [1, 214.2, 287.97999999999996, 116.196, 131.352], [1, 365.33, 495.635, 115.354, 130.51], [1, 61.879999999999995, 126.14, 137.246, 152.402], [1, 242.165, 286.195, 135.56199999999998, 150.718], [1, 461.125, 495.635, 134.72, 149.876], [1, 61.879999999999995, 126.14, 155.76999999999998, 170.926], [1, 204.67999999999998, 402.815, 154.08599999999998, 169.242], [1, 61.879999999999995, 201.10999999999999, 173.452, 189.45], [1, 61.879999999999995, 355.81, 193.66, 209.658], [1, 61.879999999999995, 355.81, 213.02599999999998, 229.024], [1, 61.879999999999995, 565.845, 232.392, 249.232], [1, 125.54499999999999, 411.145, 252.6, 269.44], [1, 61.879999999999995, 565.25, 273.65, 289.64799999999997], [1, 125.54499999999999, 329.63, 293.858, 309.856], [1, 61.879999999999995, 563.4649999999999, 314.066, 330.06399999999996], [1, 141.015, 283.21999999999997, 335.116, 351.114], [1, 61.285, 184.45, 357.008, 373.006], [1, 61.879999999999995, 168.98, 377.216, 393.214], [1, 61.879999999999995, 465.28999999999996, 394.89799999999997, 412.58], [1, 61.879999999999995, 185.64, 416.78999999999996, 432.788], [1, 61.879999999999995, 125.54499999999999, 436.998, 452.154], [1, 61.879999999999995, 177.31, 485.834, 501.832], [1, 357.0, 462.90999999999997, 483.308, 498.464], [1, 83.895, 261.8, 506.042, 522.04], [1, 61.879999999999995, 251.08999999999997, 527.092, 543.932], [1, 357.0, 473.025, 525.408, 540.564], [1, 63.07, 260.015, 556.562, 572.56], [1, 83.895, 261.205, 575.928, 591.9259999999999], [1, 340.935, 431.375, 650.866, 676.126]]
2026-08-10 12:43:52,370 INFO     29 [qwen-vl-text] ═══ DONE ═══ 34 positions, pages=1, time=15.4s
2026-08-10 12:43:52,370 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:43:52,373 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:43:52,373 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 12:43:52,373 INFO     29 [qwen-vl-text] positions(48): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:43:52,373 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [48]
2026-08-10 12:43:52,895 INFO     29 [qwen-vl-text] page=5, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:43:52,897 INFO     29 [qwen-vl-text] LLM extraction start, text_len=519
2026-08-10 12:43:52,897 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:43:52,897 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 185, \"bbox_end\": 232, \"encounter_dates\": [\"2023-03-04\"], \"department\": \"呼吸内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "报告\n闭环管理\n治疗\n健康调阅\n三诺血糖\n华益血糖\n门诊记录:\n□痕迹\n□批注\n历信息\n内蒙古医科大学附属医院门诊病历\n姓名\n年龄:51岁\n诊疗号:0010304094\n民族:蒙古族\n性别:女性\n科室:呼吸内科门诊\n联系电话:\n身份证:\n病情:\n就诊状态:\n就诊时间:2023-03-0410:51\n生命体征(需要时):\n体温:℃脉搏:次/分呼吸:次/分血压:/mmHg\n主诉:咳嗽1月,哮喘病史10余年\n现病史:\n既往史:患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎\n有,20年,吸烟史无,无过敏史。\n体格检查:发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰\n音,双下肢无水肿,体重kg。\n辅助检查:肺功能正常\n过敏史:\n初步诊断(西医):1.支气管哮喘\n初步诊断(中医):\n治疗方案:\nCT胸部\n最大通气量功能检查呼吸过滤器\n肺弥散功能检查--口残气容积测定-氮气平肺通气功能检查\n气法\n衡法\n孟鲁司特钠片<10mg>\n用量:1.000片/次\n用法:口服,一次/每晚,7天\n布地奈德福莫特罗吸入粉雾剂(11)\n用量:1.000吸/次\n<(320μg/9μg)/吸*60>\n用法:吸入,二次/日,7天\n签名:",
    "role": "user"
  }
]
2026-08-10 12:43:56,092 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:43:56,092 INFO     29 [qwen-vl-text] LLM output (len=594):
{
  "encounter_date": "2023-03-04",
  "chief_complaint": "咳嗽1月,哮喘病史10余年",
  "present_illness": null,
  "past_history": "患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎有,20年,吸烟史无,无过敏史。",
  "diagnosis": "1.支气管哮喘",
  "treatment_plan": [
    {
      "drug_name": "孟鲁司特钠片",
      "specification": "<10mg>",
      "dosage": "1.000片/次",
      "route": "口服",
      "frequency": "一次/每晚",
      "duration": "7天"
    },
    {
      "drug_name": "布地奈德福莫特罗吸入粉雾剂(11)",
      "specification": "<(320μg/9μg)/吸*60>",
      "dosage": "1.000吸/次",
      "route": "吸入",
      "frequency": "二次/日",
      "duration": "7天"
    }
  ]
}
2026-08-10 12:43:56,092 INFO     29 [qwen-vl-text] Updated encounter_dates=[2023-03-04]
2026-08-10 12:43:56,111 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8548994, prompt_len=1276
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共48行）
["报告", "闭环管理", "治疗", "健康调阅", "三诺血糖", "华益血糖", "门诊记录:", "□痕迹", "□批注", "历信息", "内蒙古医科大学附属医院门诊病历", "姓名", "年龄:51岁", "诊疗号:0010304094", "民族:蒙古族", "性别:女性", "科室:呼吸内科门诊", "联系电话:", "身份证:", "病情:", "就诊状态:", "就诊时间:2023-03-0410:51", "生命体征(需要时):", "体温:℃脉搏:次/分呼吸:次/分血压:/mmHg", "主诉:咳嗽1月,哮喘病史10余年", "现病史:", "既往史:患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎", "有,20年,吸烟史无,无过敏史。", "体格检查:发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰", "音,双下肢无水肿,体重kg。", "辅助检查:肺功能正常", "过敏史:", "初步诊断(西医):1.支气管哮喘", "初步诊断(中医):", "治疗方案:", "CT胸部", "最大通气量功能检查呼吸过滤器", "肺弥散功能检查--口残气容积测定-氮气平肺通气功能检查", "气法", "衡法", "孟鲁司特钠片<10mg>", "用量:1.000片/次", "用法:口服,一次/每晚,7天", "布地奈德福莫特罗吸入粉雾剂(11)", "用量:1.000吸/次", "<(320μg/9μg)/吸*60>", "用法:吸入,二次/日,7天", "签名:"]

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
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord API raw response (len=2621):
[
	{"text": "报告", "bbox": [38, 89, 90, 107]},
	{"text": "闭环管理", "bbox": [136, 91, 234, 109]},
	{"text": "治疗", "bbox": [280, 93, 330, 110]},
	{"text": "健康调阅", "bbox": [377, 95, 473, 113]},
	{"text": "三诺血糖", "bbox": [519, 97, 614, 115]},
	{"text": "华益血糖", "bbox": [659, 98, 753, 116]},
	{"text": "门诊记录:", "bbox": [778, 99, 880, 116]},
	{"text": "□痕迹", "bbox": [83, 137, 167, 156]},
	{"text": "□批注", "bbox": [202, 139, 285, 157]},
	{"text": "历信息", "bbox": [0, 148, 57, 164]},
	{"text": "内蒙古医科大学附属医院门诊病历", "bbox": [277, 171, 714, 190]},
	{"text": "姓名", "bbox": [142, 193, 182, 207]},
	{"text": "年龄:51岁", "bbox": [356, 195, 460, 210]},
	{"text": "诊疗号:0010304094", "bbox": [563, 198, 745, 213]},
	{"text": "民族:蒙古族", "bbox": [144, 215, 269, 230]},
	{"text": "性别:女性", "bbox": [356, 216, 461, 231]},
	{"text": "科室:呼吸内科门诊", "bbox": [563, 218, 747, 234]},
	{"text": "联系电话:", "bbox": [143, 236, 234, 251]},
	{"text": "身份证:", "bbox": [395, 238, 462, 253]},
	{"text": "病情:", "bbox": [699, 240, 745, 255]},
	{"text": "就诊状态:", "bbox": [143, 257, 234, 272]},
	{"text": "就诊时间:2023-03-0410:51", "bbox": [344, 259, 614, 274]},
	{"text": "生命体征(需要时):", "bbox": [144, 277, 338, 292]},
	{"text": "体温:℃脉搏:次/分呼吸:次/分血压:/mmHg", "bbox": [144, 295, 604, 312]},
	{"text": "主诉:咳嗽1月,哮喘病史10余年", "bbox": [144, 313, 468, 329]},
	{"text": "现病史:", "bbox": [144, 332, 214, 347]},
	{"text": "既往史:患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎", "bbox": [144, 352, 841, 369]},
	{"text": "有,20年,吸烟史无,无过敏史。", "bbox": [234, 370, 528, 386]},
	{"text": "体格检查:发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰", "bbox": [144, 389, 818, 405]},
	{"text": "音,双下肢无水肿,体重kg。", "bbox": [257, 407, 518, 423]},
	{"text": "辅助检查:肺功能正常", "bbox": [144, 426, 357, 441]},
	{"text": "过敏史:", "bbox": [144, 445, 214, 460]},
	{"text": "初步诊断(西医):1.支气管哮喘", "bbox": [144, 464, 455, 480]},
	{"text": "初步诊断(中医):", "bbox": [144, 482, 318, 498]},
	{"text": "治疗方案:", "bbox": [144, 502, 234, 517]},
	{"text": "CT胸部", "bbox": [202, 526, 264, 540]},
	{"text": "最大通气量功能检查呼吸过滤器", "bbox": [403, 526, 695, 541]},
	{"text": "肺弥散功能检查--口残气容积测定-氮气平肺通气功能检查", "bbox": [202, 543, 734, 558]},
	{"text": "气法", "bbox": [202, 556, 244, 570]},
	{"text": "衡法", "bbox": [402, 556, 442, 570]},
	{"text": "孟鲁司特钠片<10mg>", "bbox": [202, 575, 386, 590]},
	{"text": "用量:1.000片/次", "bbox": [548, 574, 694, 589]},
	{"text": "用法:口服,一次/每晚,7天", "bbox": [230, 595, 482, 610]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(11)", "bbox": [202, 618, 503, 633]},
	{"text": "用量:1.000吸/次", "bbox": [548, 617, 694, 632]},
	{"text": "<(320μg/9μg)/吸*60>", "bbox": [202, 640, 415, 655]},
	{"text": "用法:吸入,二次/日,7天", "bbox": [230, 660, 462, 675]},
	{"text": "签名:", "bbox": [512, 761, 558, 777]}
]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord API: raw_items=48, valid_items=48, elapsed=14.2s
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[0]: text=报告, bbox=[38, 89, 90, 107]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[1]: text=闭环管理, bbox=[136, 91, 234, 109]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[2]: text=治疗, bbox=[280, 93, 330, 110]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[3]: text=健康调阅, bbox=[377, 95, 473, 113]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[4]: text=三诺血糖, bbox=[519, 97, 614, 115]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[5]: text=华益血糖, bbox=[659, 98, 753, 116]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[6]: text=门诊记录:, bbox=[778, 99, 880, 116]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[7]: text=□痕迹, bbox=[83, 137, 167, 156]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[8]: text=□批注, bbox=[202, 139, 285, 157]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[9]: text=历信息, bbox=[0, 148, 57, 164]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[10]: text=内蒙古医科大学附属医院门诊病历, bbox=[277, 171, 714, 190]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[11]: text=姓名, bbox=[142, 193, 182, 207]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[12]: text=年龄:51岁, bbox=[356, 195, 460, 210]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[13]: text=诊疗号:0010304094, bbox=[563, 198, 745, 213]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[14]: text=民族:蒙古族, bbox=[144, 215, 269, 230]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[15]: text=性别:女性, bbox=[356, 216, 461, 231]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[16]: text=科室:呼吸内科门诊, bbox=[563, 218, 747, 234]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[17]: text=联系电话:, bbox=[143, 236, 234, 251]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[18]: text=身份证:, bbox=[395, 238, 462, 253]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[19]: text=病情:, bbox=[699, 240, 745, 255]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[20]: text=就诊状态:, bbox=[143, 257, 234, 272]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[21]: text=就诊时间:2023-03-0410:51, bbox=[344, 259, 614, 274]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[22]: text=生命体征(需要时):, bbox=[144, 277, 338, 292]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[23]: text=体温:℃脉搏:次/分呼吸:次/分血压:/mmHg, bbox=[144, 295, 604, 312]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[24]: text=主诉:咳嗽1月,哮喘病史10余年, bbox=[144, 313, 468, 329]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[25]: text=现病史:, bbox=[144, 332, 214, 347]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[26]: text=既往史:患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎, bbox=[144, 352, 841, 369]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[27]: text=有,20年,吸烟史无,无过敏史。, bbox=[234, 370, 528, 386]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[28]: text=体格检查:发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰, bbox=[144, 389, 818, 405]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[29]: text=音,双下肢无水肿,体重kg。, bbox=[257, 407, 518, 423]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[30]: text=辅助检查:肺功能正常, bbox=[144, 426, 357, 441]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[31]: text=过敏史:, bbox=[144, 445, 214, 460]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[32]: text=初步诊断(西医):1.支气管哮喘, bbox=[144, 464, 455, 480]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[33]: text=初步诊断(中医):, bbox=[144, 482, 318, 498]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[34]: text=治疗方案:, bbox=[144, 502, 234, 517]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[35]: text=CT胸部, bbox=[202, 526, 264, 540]
2026-08-10 12:44:10,344 INFO     29 [qwen-vl-text] coord item[36]: text=最大通气量功能检查呼吸过滤器, bbox=[403, 526, 695, 541]
2026-08-10 12:44:10,345 INFO     29 [qwen-vl-text] coord item[37]: text=肺弥散功能检查--口残气容积测定-氮气平肺通气功能检查, bbox=[202, 543, 734, 558]
2026-08-10 12:44:10,345 INFO     29 [qwen-vl-text] coord item[38]: text=气法, bbox=[202, 556, 244, 570]
2026-08-10 12:44:10,345 INFO     29 [qwen-vl-text] coord item[39]: text=衡法, bbox=[402, 556, 442, 570]
2026-08-10 12:44:10,345 INFO     29 [qwen-vl-text] coord item[40]: text=孟鲁司特钠片<10mg>, bbox=[202, 575, 386, 590]
2026-08-10 12:44:10,345 INFO     29 [qwen-vl-text] coord item[41]: text=用量:1.000片/次, bbox=[548, 574, 694, 589]
2026-08-10 12:44:10,345 INFO     29 [qwen-vl-text] coord item[42]: text=用法:口服,一次/每晚,7天, bbox=[230, 595, 482, 610]
2026-08-10 12:44:10,345 INFO     29 [qwen-vl-text] coord item[43]: text=布地奈德福莫特罗吸入粉雾剂(11), bbox=[202, 618, 503, 633]
2026-08-10 12:44:10,345 INFO     29 [qwen-vl-text] coord item[44]: text=用量:1.000吸/次, bbox=[548, 617, 694, 632]
2026-08-10 12:44:10,345 INFO     29 [qwen-vl-text] coord item[45]: text=<(320μg/9μg)/吸*60>, bbox=[202, 640, 415, 655]
2026-08-10 12:44:10,345 INFO     29 [qwen-vl-text] coord item[46]: text=用法:吸入,二次/日,7天, bbox=[230, 660, 462, 675]
2026-08-10 12:44:10,345 INFO     29 [qwen-vl-text] coord item[47]: text=签名:, bbox=[512, 761, 558, 777]
2026-08-10 12:44:10,346 INFO     29 [qwen-vl-text] page=5 — 48/48 coords, api_time=14.2s
2026-08-10 12:44:10,347 INFO     29 [qwen-vl-text] new_positions (48):
[[5, 22.61, 53.55, 74.938, 90.094], [5, 80.92, 139.23, 76.622, 91.77799999999999], [5, 166.6, 196.35, 78.306, 92.61999999999999], [5, 224.315, 281.435, 79.99, 95.146], [5, 308.805, 365.33, 81.67399999999999, 96.83], [5, 392.10499999999996, 448.03499999999997, 82.51599999999999, 97.672], [5, 462.90999999999997, 523.6, 83.358, 97.672], [5, 49.385, 99.365, 115.354, 131.352], [5, 120.19, 169.575, 117.038, 132.194], [5, 0.0, 33.915, 124.616, 138.088], [5, 164.815, 424.83, 143.982, 159.98], [5, 84.49, 108.28999999999999, 162.506, 174.29399999999998], [5, 211.82, 273.7, 164.19, 176.82], [5, 334.98499999999996, 443.275, 166.716, 179.346], [5, 85.67999999999999, 160.055, 181.03, 193.66], [5, 211.82, 274.295, 181.87199999999999, 194.50199999999998], [5, 334.98499999999996, 444.465, 183.55599999999998, 197.028], [5, 85.085, 139.23, 198.712, 211.34199999999998], [5, 235.02499999999998, 274.89, 200.396, 213.02599999999998], [5, 415.905, 443.275, 202.07999999999998, 214.70999999999998], [5, 85.085, 139.23, 216.394, 229.024], [5, 204.67999999999998, 365.33, 218.078, 230.708], [5, 85.67999999999999, 201.10999999999999, 233.23399999999998, 245.864], [5, 85.67999999999999, 359.38, 248.39, 262.704], [5, 85.67999999999999, 278.46, 263.546, 277.018], [5, 85.67999999999999, 127.33, 279.544, 292.174], [5, 85.67999999999999, 500.395, 296.384, 310.698], [5, 139.23, 314.15999999999997, 311.53999999999996, 325.012], [5, 85.67999999999999, 486.71, 327.538, 341.01], [5, 152.915, 308.21, 342.69399999999996, 356.166], [5, 85.67999999999999, 212.415, 358.692, 371.322], [5, 85.67999999999999, 127.33, 374.69, 387.32], [5, 85.67999999999999, 270.72499999999997, 390.688, 404.15999999999997], [5, 85.67999999999999, 189.20999999999998, 405.844, 419.316], [5, 85.67999999999999, 139.23, 422.68399999999997, 435.31399999999996], [5, 120.19, 157.07999999999998, 442.892, 454.68], [5, 239.785, 413.525, 442.892, 455.522], [5, 120.19, 436.72999999999996, 457.20599999999996, 469.83599999999996], [5, 120.19, 145.18, 468.152, 479.94], [5, 239.19, 262.99, 468.152, 479.94], [5, 120.19, 229.67, 484.15, 496.78], [5, 326.06, 412.93, 483.308, 495.938], [5, 136.85, 286.78999999999996, 500.99, 513.62], [5, 120.19, 299.28499999999997, 520.356, 532.986], [5, 326.06, 412.93, 519.514, 532.144], [5, 120.19, 246.92499999999998, 538.88, 551.51], [5, 136.85, 274.89, 555.72, 568.35], [5, 304.64, 332.01, 640.762, 654.2339999999999]]
2026-08-10 12:44:10,347 INFO     29 [qwen-vl-text] ═══ DONE ═══ 48 positions, pages=1, time=18.0s
2026-08-10 12:44:10,347 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:44:10,348 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:44:10,348 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 12:44:10,348 INFO     29 [qwen-vl-text] positions(32): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:44:10,348 INFO     29 [qwen-vl-text] page grouping: [5, 6], lines per page: [4, 28]
2026-08-10 12:44:10,887 INFO     29 [qwen-vl-text] page=5, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:44:11,296 INFO     29 [qwen-vl-text] page=6, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:44:11,298 INFO     29 [qwen-vl-text] LLM extraction start, text_len=464
2026-08-10 12:44:11,298 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:44:11,298 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 233, \"bbox_end\": 264, \"encounter_dates\": [\"2026-02-12\"], \"department\": \"呼吸与危重症医学科门\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "付丹\n26星期二\n190.1.48.233\n王王立\n内蒙古自治区国际蒙医医院\n门诊病历\n门诊号：2602120916\n姓\n科室：呼吸与危重症医学科门 性别：女性 出生年月：1971-11-18\n诊\n就诊时间：2026-02-12 11:20\n○初诊◎复诊\n过敏史：□否 □不详 □有：\n主 诉：发作性咳嗽、气短5年，加重3天\n现病史：5年前出现发作性咳嗽、气短，吸入刺激性气味后症状明显，就诊于当地医院诊断\n为“支气管哮喘”，长期规律吸入信必可治疗后效果欠佳。近3天喘息加重，伴咳嗽、咳痰较前\n频繁。夜间明显。\n既往史：体健\n家族史：无\n体格检查：意识：清醒\nT：36.5℃ P：71次/分 R：18次/分 BP：115/77mmHg\n双肺可闻及干鸣音\n辅助检查：\n处方信息：\n布地奈德福莫特罗吸入粉雾剂（II）(160μg/4.5μg/吸*60吸/支)*1支\n320μg 吸入 bid\n醋酸泼尼松片(5mg*100片/瓶)*1瓶\n15mg 口服 qd\n其他处置：\n复诊记录：\n门诊诊断：支气管哮喘(急性发作期)\n医生签名：苏佳",
    "role": "user"
  }
]
2026-08-10 12:44:11,300 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:44:11.299+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 31, "failed": 0, "current": {"ed8cac4894b811f1bd9827cf206dfa2d": {"id": "ed8cac4894b811f1bd9827cf206dfa2d", "doc_id": "ed520a7a94b811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWRNA(2).pdf", "type": "pdf", "location": "\u9ea6\u6d4eWRNA(2).pdf", "size": 13028580, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786365740553, "task_type": "dataflow", "root_trace_id": "cdcb62f1323147c19d5b537cd2e3ed24", "root_traceparent": "00-cdcb62f1323147c19d5b537cd2e3ed24-dbd2f127625489c0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:44:16,536 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:44:16,536 INFO     29 [qwen-vl-text] LLM output (len=634):
{
  "encounter_date": "2026-02-12",
  "chief_complaint": "发作性咳嗽、气短5年，加重3天",
  "present_illness": "5年前出现发作性咳嗽、气短，吸入刺激性气味后症状明显，就诊于当地医院诊断为“支气管哮喘”，长期规律吸入信必可治疗后效果欠佳。近3天喘息加重，伴咳嗽、咳痰较前频繁。夜间明显。",
  "past_history": "体健",
  "diagnosis": "支气管哮喘(急性发作期)",
  "treatment_plan": [
    {
      "drug_name": "布地奈德福莫特罗吸入粉雾剂（II）",
      "specification": "160μg/4.5μg/吸*60吸/支",
      "dosage": "320μg",
      "route": "吸入",
      "frequency": "bid",
      "quantity": "1支"
    },
    {
      "drug_name": "醋酸泼尼松片",
      "specification": "5mg*100片/瓶",
      "dosage": "15mg",
      "route": "口服",
      "frequency": "qd",
      "quantity": "1瓶"
    }
  ]
}
2026-08-10 12:44:16,536 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-12]
2026-08-10 12:44:16,560 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8548994, prompt_len=649
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共4行）
["付丹", "26星期二", "190.1.48.233", "王王立"]

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
2026-08-10 12:44:19,098 INFO     29 [qwen-vl-text] coord API raw response (len=243):
```json
[
	{"text": "付丹", "bbox": [587, 753, 638, 777]},
	{"text": "26星期二", "bbox": [0, 838, 74, 854]},
	{"text": "190.1.48.233", "bbox": [150, 837, 255, 852]},
	{"text": "王王立", "bbox": [931, 822, 999, 839], "bbox": [931, 822, 999, 839]}
]
```
2026-08-10 12:44:19,099 INFO     29 [qwen-vl-text] coord API: raw_items=4, valid_items=4, elapsed=2.5s
2026-08-10 12:44:19,099 INFO     29 [qwen-vl-text] coord item[0]: text=付丹, bbox=[587, 753, 638, 777]
2026-08-10 12:44:19,099 INFO     29 [qwen-vl-text] coord item[1]: text=26星期二, bbox=[0, 838, 74, 854]
2026-08-10 12:44:19,099 INFO     29 [qwen-vl-text] coord item[2]: text=190.1.48.233, bbox=[150, 837, 255, 852]
2026-08-10 12:44:19,099 INFO     29 [qwen-vl-text] coord item[3]: text=王王立, bbox=[931, 822, 999, 839]
2026-08-10 12:44:19,103 INFO     29 [qwen-vl-text] page=5 — 4/4 coords, api_time=2.5s
2026-08-10 12:44:19,112 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2515045, prompt_len=1135
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["内蒙古自治区国际蒙医医院", "门诊病历", "门诊号：2602120916", "姓", "科室：呼吸与危重症医学科门 性别：女性 出生年月：1971-11-18", "诊", "就诊时间：2026-02-12 11:20", "○初诊◎复诊", "过敏史：□否 □不详 □有：", "主 诉：发作性咳嗽、气短5年，加重3天", "现病史：5年前出现发作性咳嗽、气短，吸入刺激性气味后症状明显，就诊于当地医院诊断", "为“支气管哮喘”，长期规律吸入信必可治疗后效果欠佳。近3天喘息加重，伴咳嗽、咳痰较前", "频繁。夜间明显。", "既往史：体健", "家族史：无", "体格检查：意识：清醒", "T：36.5℃ P：71次/分 R：18次/分 BP：115/77mmHg", "双肺可闻及干鸣音", "辅助检查：", "处方信息：", "布地奈德福莫特罗吸入粉雾剂（II）(160μg/4.5μg/吸*60吸/支)*1支", "320μg 吸入 bid", "醋酸泼尼松片(5mg*100片/瓶)*1瓶", "15mg 口服 qd", "其他处置：", "复诊记录：", "门诊诊断：支气管哮喘(急性发作期)", "医生签名：苏佳"]

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
2026-08-10 12:44:28,497 INFO     29 [qwen-vl-text] coord API raw response (len=1649):
[
	{"text": "内蒙古自治区国际蒙医医院", "bbox": [81, 40, 302, 57]},
	{"text": "门诊病历", "bbox": [430, 47, 548, 70]},
	{"text": "门诊号：2602120916", "bbox": [734, 86, 915, 101]},
	{"text": "姓", "bbox": [78, 109, 100, 124]},
	{"text": "科室：呼吸与危重症医学科门 性别：女性 出生年月：1971-11-18", "bbox": [300, 110, 901, 126]},
	{"text": "诊", "bbox": [300, 126, 320, 140]},
	{"text": "就诊时间：2026-02-12 11:20", "bbox": [78, 148, 341, 163]},
	{"text": "○初诊◎复诊", "bbox": [578, 148, 708, 163]},
	{"text": "过敏史：□否 □不详 □有：", "bbox": [78, 170, 343, 187]},
	{"text": "主 诉：发作性咳嗽、气短5年，加重3天", "bbox": [78, 193, 439, 209]},
	{"text": "现病史：5年前出现发作性咳嗽、气短，吸入刺激性气味后症状明显，就诊于当地医院诊断", "bbox": [78, 234, 866, 251]},
	{"text": "为“支气管哮喘”，长期规律吸入信必可治疗后效果欠佳。近3天喘息加重，伴咳嗽、咳痰较前", "bbox": [78, 250, 905, 267]},
	{"text": "频繁。夜间明显。", "bbox": [78, 266, 227, 281]},
	{"text": "既往史：体健", "bbox": [78, 304, 195, 319]},
	{"text": "家族史：无", "bbox": [78, 342, 174, 358]},
	{"text": "体格检查：意识：清醒", "bbox": [78, 381, 264, 397]},
	{"text": "T：36.5℃ P：71次/分 R：18次/分 BP：115/77mmHg", "bbox": [78, 398, 631, 414]},
	{"text": "双肺可闻及干鸣音", "bbox": [78, 414, 234, 429]},
	{"text": "辅助检查：", "bbox": [76, 453, 162, 468]},
	{"text": "处方信息：", "bbox": [76, 490, 162, 505]},
	{"text": "布地奈德福莫特罗吸入粉雾剂（II）(160μg/4.5μg/吸*60吸/支)*1支", "bbox": [76, 506, 689, 523]},
	{"text": "320μg 吸入 bid", "bbox": [719, 508, 909, 523]},
	{"text": "醋酸泼尼松片(5mg*100片/瓶)*1瓶", "bbox": [76, 522, 380, 538]},
	{"text": "15mg 口服 qd", "bbox": [411, 523, 570, 539]},
	{"text": "其他处置：", "bbox": [76, 561, 162, 577]},
	{"text": "复诊记录：", "bbox": [78, 600, 165, 616]},
	{"text": "门诊诊断：支气管哮喘(急性发作期)", "bbox": [406, 642, 724, 659]},
	{"text": "医生签名：苏佳", "bbox": [556, 688, 760, 727]}
]
2026-08-10 12:44:28,497 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=9.4s
2026-08-10 12:44:28,497 INFO     29 [qwen-vl-text] coord item[0]: text=内蒙古自治区国际蒙医医院, bbox=[81, 40, 302, 57]
2026-08-10 12:44:28,497 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[430, 47, 548, 70]
2026-08-10 12:44:28,497 INFO     29 [qwen-vl-text] coord item[2]: text=门诊号：2602120916, bbox=[734, 86, 915, 101]
2026-08-10 12:44:28,497 INFO     29 [qwen-vl-text] coord item[3]: text=姓, bbox=[78, 109, 100, 124]
2026-08-10 12:44:28,497 INFO     29 [qwen-vl-text] coord item[4]: text=科室：呼吸与危重症医学科门 性别：女性 出生年月：1971-11-18, bbox=[300, 110, 901, 126]
2026-08-10 12:44:28,497 INFO     29 [qwen-vl-text] coord item[5]: text=诊, bbox=[300, 126, 320, 140]
2026-08-10 12:44:28,497 INFO     29 [qwen-vl-text] coord item[6]: text=就诊时间：2026-02-12 11:20, bbox=[78, 148, 341, 163]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] coord item[7]: text=○初诊◎复诊, bbox=[578, 148, 708, 163]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] coord item[8]: text=过敏史：□否 □不详 □有：, bbox=[78, 170, 343, 187]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] coord item[9]: text=主 诉：发作性咳嗽、气短5年，加重3天, bbox=[78, 193, 439, 209]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] coord item[10]: text=现病史：5年前出现发作性咳嗽、气短，吸入刺激性气味后症状明显，就诊于当地医院诊断, bbox=[78, 234, 866, 251]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] coord item[11]: text=为“支气管哮喘”，长期规律吸入信必可治疗后效果欠佳。近3天喘息加重，伴咳嗽、咳痰较前, bbox=[78, 250, 905, 267]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] coord item[12]: text=频繁。夜间明显。, bbox=[78, 266, 227, 281]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] coord item[13]: text=既往史：体健, bbox=[78, 304, 195, 319]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] coord item[14]: text=家族史：无, bbox=[78, 342, 174, 358]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] coord item[15]: text=体格检查：意识：清醒, bbox=[78, 381, 264, 397]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] coord item[16]: text=T：36.5℃ P：71次/分 R：18次/分 BP：115/77mmHg, bbox=[78, 398, 631, 414]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] coord item[17]: text=双肺可闻及干鸣音, bbox=[78, 414, 234, 429]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] coord item[18]: text=辅助检查：, bbox=[76, 453, 162, 468]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] coord item[19]: text=处方信息：, bbox=[76, 490, 162, 505]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] coord item[20]: text=布地奈德福莫特罗吸入粉雾剂（II）(160μg/4.5μg/吸*60吸/支)*1支, bbox=[76, 506, 689, 523]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] coord item[21]: text=320μg 吸入 bid, bbox=[719, 508, 909, 523]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] coord item[22]: text=醋酸泼尼松片(5mg*100片/瓶)*1瓶, bbox=[76, 522, 380, 538]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] coord item[23]: text=15mg 口服 qd, bbox=[411, 523, 570, 539]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] coord item[24]: text=其他处置：, bbox=[76, 561, 162, 577]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] coord item[25]: text=复诊记录：, bbox=[78, 600, 165, 616]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] coord item[26]: text=门诊诊断：支气管哮喘(急性发作期), bbox=[406, 642, 724, 659]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] coord item[27]: text=医生签名：苏佳, bbox=[556, 688, 760, 727]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] page=6 — 28/28 coords, api_time=9.4s
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] new_positions (32):
[[5, 349.265, 379.60999999999996, 634.026, 654.2339999999999], [5, 0.0, 44.03, 705.596, 719.068], [5, 89.25, 151.725, 704.754, 717.384], [5, 553.9449999999999, 594.405, 692.124, 706.438], [6, 48.195, 179.69, 33.68, 47.994], [6, 255.85, 326.06, 39.574, 58.94], [6, 436.72999999999996, 544.425, 72.41199999999999, 85.042], [6, 46.41, 59.5, 91.77799999999999, 104.408], [6, 178.5, 536.095, 92.61999999999999, 106.092], [6, 178.5, 190.39999999999998, 106.092, 117.88], [6, 46.41, 202.89499999999998, 124.616, 137.246], [6, 343.90999999999997, 421.26, 124.616, 137.246], [6, 46.41, 204.08499999999998, 143.14, 157.454], [6, 46.41, 261.205, 162.506, 175.97799999999998], [6, 46.41, 515.27, 197.028, 211.34199999999998], [6, 46.41, 538.475, 210.5, 224.814], [6, 46.41, 135.065, 223.97199999999998, 236.602], [6, 46.41, 116.02499999999999, 255.968, 268.598], [6, 46.41, 103.53, 287.964, 301.436], [6, 46.41, 157.07999999999998, 320.80199999999996, 334.274], [6, 46.41, 375.445, 335.116, 348.58799999999997], [6, 46.41, 139.23, 348.58799999999997, 361.21799999999996], [6, 45.22, 96.39, 381.426, 394.056], [6, 45.22, 96.39, 412.58, 425.21], [6, 45.22, 409.955, 426.05199999999996, 440.366], [6, 427.805, 540.855, 427.736, 440.366], [6, 45.22, 226.1, 439.524, 452.996], [6, 244.545, 339.15, 440.366, 453.83799999999997], [6, 45.22, 96.39, 472.36199999999997, 485.834], [6, 46.41, 98.175, 505.2, 518.672], [6, 241.57, 430.78, 540.564, 554.8779999999999], [6, 330.82, 452.2, 579.2959999999999, 612.134]]
2026-08-10 12:44:28,498 INFO     29 [qwen-vl-text] ═══ DONE ═══ 32 positions, pages=2, time=18.2s
2026-08-10 12:44:28,512 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 12:44:28,513 INFO     29 [Trace] task=ed8cac48 | doc=麦济WRNA(2).pdf | Extractor:Clinical | outputs={"chunks": "4 items, types={'OutpatientRecord': 4}", "html": "", "json": "306 items", "markdown": "", "text": "", "name": "麦济WRNA(2).pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Medication\": 5}"}
2026-08-10 12:44:28,513 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 12:44:28,518 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:44:28,518 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:44:28,518 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 12:44:28,518 INFO     29 [qwen-vl-text] positions(16): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:44:28,518 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [16]
2026-08-10 12:44:28,774 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:44:28,775 INFO     29 [qwen-vl-text] LLM extraction start, text_len=200
2026-08-10 12:44:28,775 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:44:28,775 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 74, \"bbox_end\": 89, \"encounter_dates\": [\"2026-01-21\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "鹤春堂大药房\n2026-01-21 17:23:52\n收银员：张星\n名称 单价 数量 金额\n布地奈德福莫特罗吸入粉雾剂(Ⅱ)\n320 μg /9 μg / 吸 60 吸 / 支\n298.00 2 596.00\n应收金额: 596.00\n实收金额: 596.00\n找零: 0.00\n优惠: 0.00\n会员:\n本次积分: 596\n合计积分: 1325\n祝您身体健康，药品属于特殊商品\n无质量问题，概不退换",
    "role": "user"
  }
]
2026-08-10 12:44:31,052 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:44:31,052 INFO     29 [qwen-vl-text] LLM output (len=439):
{
  "encounter_date": "2026-01-21",
  "pharmacy": "鹤春堂大药房",
  "medications": [
    {
      "name": "布地奈德福莫特罗吸入粉雾剂(Ⅱ)",
      "specification": "320 μg /9 μg / 吸 60 吸 / 支",
      "dosage": null,
      "quantity": 2,
      "unit_price": 298.00,
      "total_price": 596.00,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 596.00,
  "payment_method": null
}
2026-08-10 12:44:31,052 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-21]
2026-08-10 12:44:31,059 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2066777, prompt_len=861
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["鹤春堂大药房", "2026-01-21 17:23:52", "收银员：张星", "名称 单价 数量 金额", "布地奈德福莫特罗吸入粉雾剂(Ⅱ)", "320 μg /9 μg / 吸 60 吸 / 支", "298.00 2 596.00", "应收金额: 596.00", "实收金额: 596.00", "找零: 0.00", "优惠: 0.00", "会员:", "本次积分: 596", "合计积分: 1325", "祝您身体健康，药品属于特殊商品", "无质量问题，概不退换"]

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
2026-08-10 12:44:36,689 INFO     29 [qwen-vl-text] coord API raw response (len=907):
[
	{"text": "鹤春堂大药房", "bbox": [377, 107, 656, 143]},
	{"text": "2026-01-21 17:23:52", "bbox": [161, 157, 628, 188]},
	{"text": "收银员：张星", "bbox": [162, 200, 438, 235]},
	{"text": "名称 单价 数量 金额", "bbox": [163, 290, 824, 326]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(Ⅱ)", "bbox": [163, 335, 880, 371]},
	{"text": "320 μg /9 μg / 吸 60 吸 / 支", "bbox": [159, 383, 878, 416]},
	{"text": "298.00 2 596.00", "bbox": [159, 430, 633, 461]},
	{"text": "应收金额: 596.00", "bbox": [159, 520, 584, 555]},
	{"text": "实收金额: 596.00", "bbox": [159, 564, 584, 599]},
	{"text": "找零: 0.00", "bbox": [159, 612, 444, 646]},
	{"text": "优惠: 0.00", "bbox": [159, 658, 444, 691]},
	{"text": "会员:", "bbox": [159, 702, 268, 737]},
	{"text": "本次积分: 596", "bbox": [159, 747, 467, 781]},
	{"text": "合计积分: 1325", "bbox": [159, 793, 488, 829]},
	{"text": "祝您身体健康，药品属于特殊商品", "bbox": [159, 844, 878, 879]},
	{"text": "无质量问题，概不退换", "bbox": [159, 904, 624, 938]}
]
2026-08-10 12:44:36,689 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=5.6s
2026-08-10 12:44:36,689 INFO     29 [qwen-vl-text] coord item[0]: text=鹤春堂大药房, bbox=[377, 107, 656, 143]
2026-08-10 12:44:36,689 INFO     29 [qwen-vl-text] coord item[1]: text=2026-01-21 17:23:52, bbox=[161, 157, 628, 188]
2026-08-10 12:44:36,689 INFO     29 [qwen-vl-text] coord item[2]: text=收银员：张星, bbox=[162, 200, 438, 235]
2026-08-10 12:44:36,690 INFO     29 [qwen-vl-text] coord item[3]: text=名称 单价 数量 金额, bbox=[163, 290, 824, 326]
2026-08-10 12:44:36,690 INFO     29 [qwen-vl-text] coord item[4]: text=布地奈德福莫特罗吸入粉雾剂(Ⅱ), bbox=[163, 335, 880, 371]
2026-08-10 12:44:36,690 INFO     29 [qwen-vl-text] coord item[5]: text=320 μg /9 μg / 吸 60 吸 / 支, bbox=[159, 383, 878, 416]
2026-08-10 12:44:36,690 INFO     29 [qwen-vl-text] coord item[6]: text=298.00 2 596.00, bbox=[159, 430, 633, 461]
2026-08-10 12:44:36,690 INFO     29 [qwen-vl-text] coord item[7]: text=应收金额: 596.00, bbox=[159, 520, 584, 555]
2026-08-10 12:44:36,690 INFO     29 [qwen-vl-text] coord item[8]: text=实收金额: 596.00, bbox=[159, 564, 584, 599]
2026-08-10 12:44:36,690 INFO     29 [qwen-vl-text] coord item[9]: text=找零: 0.00, bbox=[159, 612, 444, 646]
2026-08-10 12:44:36,690 INFO     29 [qwen-vl-text] coord item[10]: text=优惠: 0.00, bbox=[159, 658, 444, 691]
2026-08-10 12:44:36,690 INFO     29 [qwen-vl-text] coord item[11]: text=会员:, bbox=[159, 702, 268, 737]
2026-08-10 12:44:36,690 INFO     29 [qwen-vl-text] coord item[12]: text=本次积分: 596, bbox=[159, 747, 467, 781]
2026-08-10 12:44:36,690 INFO     29 [qwen-vl-text] coord item[13]: text=合计积分: 1325, bbox=[159, 793, 488, 829]
2026-08-10 12:44:36,690 INFO     29 [qwen-vl-text] coord item[14]: text=祝您身体健康，药品属于特殊商品, bbox=[159, 844, 878, 879]
2026-08-10 12:44:36,690 INFO     29 [qwen-vl-text] coord item[15]: text=无质量问题，概不退换, bbox=[159, 904, 624, 938]
2026-08-10 12:44:36,691 INFO     29 [qwen-vl-text] page=2 — 16/16 coords, api_time=5.6s
2026-08-10 12:44:36,691 INFO     29 [qwen-vl-text] new_positions (16):
[[2, 224.315, 390.32, 90.094, 120.40599999999999], [2, 95.795, 373.65999999999997, 132.194, 158.296], [2, 96.39, 260.61, 168.4, 197.87], [2, 96.985, 490.28, 244.17999999999998, 274.492], [2, 96.985, 523.6, 282.07, 312.382], [2, 94.60499999999999, 522.41, 322.486, 350.272], [2, 94.60499999999999, 376.635, 362.06, 388.162], [2, 94.60499999999999, 347.47999999999996, 437.84, 467.31], [2, 94.60499999999999, 347.47999999999996, 474.888, 504.358], [2, 94.60499999999999, 264.18, 515.304, 543.932], [2, 94.60499999999999, 264.18, 554.036, 581.822], [2, 94.60499999999999, 159.45999999999998, 591.084, 620.554], [2, 94.60499999999999, 277.865, 628.9739999999999, 657.602], [2, 94.60499999999999, 290.36, 667.706, 698.018], [2, 94.60499999999999, 522.41, 710.648, 740.1179999999999], [2, 94.60499999999999, 371.28, 761.168, 789.7959999999999]]
2026-08-10 12:44:36,691 INFO     29 [qwen-vl-text] ═══ DONE ═══ 16 positions, pages=1, time=8.2s
2026-08-10 12:44:36,691 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:44:36,693 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:44:36,693 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 12:44:36,693 INFO     29 [qwen-vl-text] positions(52): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:44:36,694 INFO     29 [qwen-vl-text] page grouping: [3], lines per page: [52]
2026-08-10 12:44:36,808 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:44:36,810 INFO     29 [qwen-vl-text] LLM extraction start, text_len=573
2026-08-10 12:44:36,810 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:44:36,811 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 90, \"bbox_end\": 141, \"encounter_dates\": [\"2026-02-12\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "11:43\n美团\n5G\n4G\n24\n电子票预览\nwww.chinaebill.cn\n内蒙古自治区医疗门诊收费票据（电子）\n内蒙古\n财政部监制\n票据代码：15060125\n票据号码：0127705695\n交款人\n用代码：150102********2023\n校验码：55e825\n交\n开票日期：2026-02-12\n数量/单位\n金额（元）\n备注\n项目名称\n数量/单位\n金额（元）\n备注\n西药费\n1\n项\n188.21\n金额合计（大写）壹佰捌拾捌元贰角壹分\n(小写)188.21\n业务流水号：202602120002043\n门诊号：2602120916\n就诊日期：20260212\n其\n医疗机构类型：综合医院\n医保类型：职工基本医疗保险\n医保编号：150000NMGZG00000000001\n性别：女\n9506\n信\n医保统筹基金支付：101.92\n其他支付：0.00\n个人账户支付：86.29\n个人现金支付：0.00\n息\n个人自付：86.29\n个人自费：0.00\n交费日期：20260212\n备注：医保总金额：188.21符合统筹：169.87账户余额：4301.09医疗救助基金：0大病保险：0公务员补助：0\n医疗收费专用章\n支付：0企业补充保险：0符合政策范围金额：169.87其他基金：0伙食补助：0起付线：0\n（章）：内蒙古自治区国际蒙医医院",
    "role": "user"
  }
]
2026-08-10 12:44:38,285 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:44:38,286 INFO     29 [qwen-vl-text] LLM output (len=146):
{
  "encounter_date": "2026-02-12",
  "pharmacy": "内蒙古自治区国际蒙医医院",
  "medications": [],
  "payment_total": 188.21,
  "payment_method": "职工基本医疗保险"
}
2026-08-10 12:44:38,286 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-12]
2026-08-10 12:44:38,286 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=623575, prompt_len=1342
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共52行）
["11:43", "美团", "5G", "4G", "24", "电子票预览", "www.chinaebill.cn", "内蒙古自治区医疗门诊收费票据（电子）", "内蒙古", "财政部监制", "票据代码：15060125", "票据号码：0127705695", "交款人", "用代码：150102********2023", "校验码：55e825", "交", "开票日期：2026-02-12", "数量/单位", "金额（元）", "备注", "项目名称", "数量/单位", "金额（元）", "备注", "西药费", "1", "项", "188.21", "金额合计（大写）壹佰捌拾捌元贰角壹分", "(小写)188.21", "业务流水号：202602120002043", "门诊号：2602120916", "就诊日期：20260212", "其", "医疗机构类型：综合医院", "医保类型：职工基本医疗保险", "医保编号：150000NMGZG00000000001", "性别：女", "9506", "信", "医保统筹基金支付：101.92", "其他支付：0.00", "个人账户支付：86.29", "个人现金支付：0.00", "息", "个人自付：86.29", "个人自费：0.00", "交费日期：20260212", "备注：医保总金额：188.21符合统筹：169.87账户余额：4301.09医疗救助基金：0大病保险：0公务员补助：0", "医疗收费专用章", "支付：0企业补充保险：0符合政策范围金额：169.87其他基金：0伙食补助：0起付线：0", "（章）：内蒙古自治区国际蒙医医院"]

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
2026-08-10 12:45:05,355 INFO     29 [qwen-vl-text] coord API raw response (len=4723):
[
	{"text": "11:43", "bbox": [391, 20, 455, 36], "bbox": [391, 20, 455, 36]},
	{"text": "美团", "bbox": [489, 24, 507, 32], "bbox": [489, 24, 507, 32]},
	{"text": "5G", "bbox": [675, 20, 692, 28], "bbox": [675, 20, 692, 28]},
	{"text": "4G", "bbox": [720, 20, 735, 28], "bbox": [720, 20, 735, 28]},
	{"text": "24", "bbox": [765, 20, 790, 36], "bbox": [765, 20, 790, 36]},
	{"text": "电子票预览", "bbox": [426, 58, 570, 80], "bbox": [426, 58, 570, 80]},
	{"text": "www.chinaebill.cn", "bbox": [413, 87, 583, 100], "bbox": [413, 87, 583, 100]},
	{"text": "内蒙古自治区医疗门诊收费票据（电子）", "bbox": [339, 134, 650, 147], "bbox": [339, 134, 650, 147]},
	{"text": "内蒙古", "bbox": [485, 148, 514, 156], "bbox": [485, 148, 514, 156]},
	{"text": "财政部监制", "bbox": [475, 157, 525, 167], "bbox": [475, 157, 525, 167]},
	{"text": "票据代码：15060125", "bbox": [219, 177, 296, 184], "bbox": [219, 177, 296, 184]},
	{"text": "票据号码：0127705695", "bbox": [592, 177, 678, 184], "bbox": [592, 177, 678, 184]},
	{"text": "交款人", "bbox": [219, 187, 234, 194], "bbox": [219, 187, 234, 194]},
	{"text": "用代码：150102********2023", "bbox": [289, 187, 405, 194], "bbox": [289, 187, 405, 194]},
	{"text": "校验码：55e825", "bbox": [592, 187, 660, 194], "bbox": [592, 187, 660, 194]},
	{"text": "交", "bbox": [219, 196, 228, 203], "bbox": [219, 196, 228, 203]},
	{"text": "开票日期：2026-02-12", "bbox": [592, 196, 678, 203], "bbox": [592, 196, 678, 203]},
	{"text": "数量/单位", "bbox": [356, 208, 396, 214], "bbox": [356, 208, 396, 214]},
	{"text": "金额（元）", "bbox": [417, 208, 456, 214], "bbox": [417, 208, 456, 214]},
	{"text": "备注", "bbox": [472, 208, 489, 214], "bbox": [472, 208, 489, 214]},
	{"text": "项目名称", "bbox": [544, 208, 579, 214], "bbox": [544, 208, 579, 214]},
	{"text": "数量/单位", "bbox": [635, 208, 674, 214], "bbox": [635, 208, 674, 214]},
	{"text": "金额（元）", "bbox": [696, 208, 734, 214], "bbox": [696, 208, 734, 214]},
	{"text": "备注", "bbox": [750, 208, 766, 214], "bbox": [750, 208, 766, 214]},
	{"text": "西药费", "bbox": [220, 220, 247, 227], "bbox": [220, 220, 247, 227]},
	{"text": "1", "bbox": [357, 220, 362, 227], "bbox": [357, 220, 362, 227]},
	{"text": "项", "bbox": [385, 220, 394, 227], "bbox": [385, 220, 394, 227]},
	{"text": "188.21", "bbox": [429, 220, 456, 227], "bbox": [429, 220, 456, 227]},
	{"text": "金额合计（大写）壹佰捌拾捌元贰角壹分", "bbox": [222, 314, 381, 321], "bbox": [222, 314, 381, 321]},
	{"text": "(小写)188.21", "bbox": [536, 314, 590, 321], "bbox": [536, 314, 590, 321]},
	{"text": "业务流水号：202602120002043", "bbox": [241, 327, 357, 334], "bbox": [241, 327, 357, 334]},
	{"text": "门诊号：2602120916", "bbox": [382, 327, 460, 334], "bbox": [382, 327, 460, 334]},
	{"text": "就诊日期：20260212", "bbox": [654, 327, 731, 334], "bbox": [654, 327, 731, 334]},
	{"text": "其", "bbox": [226, 338, 234, 345], "bbox": [226, 338, 234, 345]},
	{"text": "医疗机构类型：综合医院", "bbox": [241, 343, 335, 350], "bbox": [241, 343, 335, 350]},
	{"text": "医保类型：职工基本医疗保险", "bbox": [382, 343, 495, 350], "bbox": [382, 343, 495, 350]},
	{"text": "医保编号：150000NMGZG00000000001", "bbox": [510, 343, 649, 350], "bbox": [510, 343, 649, 350]},
	{"text": "性别：女", "bbox": [654, 343, 687, 350], "bbox": [654, 343, 687, 350]},
	{"text": "9506", "bbox": [550, 351, 569, 358], "bbox": [550, 351, 569, 358]},
	{"text": "信", "bbox": [226, 365, 234, 372], "bbox": [226, 365, 234, 372]},
	{"text": "医保统筹基金支付：101.92", "bbox": [241, 359, 345, 366], "bbox": [241, 359, 345, 366]},
	{"text": "其他支付：0.00", "bbox": [382, 359, 441, 366], "bbox": [382, 359, 441, 366]},
	{"text": "个人账户支付：86.29", "bbox": [510, 359, 592, 366], "bbox": [510, 359, 592, 366]},
	{"text": "个人现金支付：0.00", "bbox": [654, 359, 731, 366], "bbox": [654, 359, 731, 366]},
	{"text": "息", "bbox": [226, 376, 234, 383], "bbox": [226, 376, 234, 383]},
	{"text": "个人自付：86.29", "bbox": [241, 372, 305, 379], "bbox": [241, 372, 305, 379]},
	{"text": "个人自费：0.00", "bbox": [382, 372, 441, 379], "bbox": [382, 372, 441, 379]},
	{"text": "交费日期：20260212", "bbox": [510, 372, 588, 379], "bbox": [510, 372, 588, 379]},
	{"text": "备注：医保总金额：188.21符合统筹：169.87账户余额：4301.09医疗救助基金：0大病保险：0公务员补助：0", "bbox": [241, 380, 642, 387], "bbox": [241, 380, 642, 387]},
	{"text": "医疗收费专用章", "bbox": [222, 395, 261, 402], "bbox": [222, 395, 261, 402]},
	{"text": "支付：0企业补充保险：0符合政策范围金额：169.87其他基金：0伙食补助：0起付线：0", "bbox": [241, 388, 602, 395], "bbox": [241, 388, 602, 395]},
	{"text": "（章）：内蒙古自治区国际蒙医医院", "bbox": [265, 400, 400, 407], "bbox": [265, 400, 400, 407]},
	{"text": "复核人：李姹娜", "bbox": [539, 400, 596, 407], "bbox": [539, 400, 596, 407]},
	{"text": "收款人：李姹娜", "bbox": [656, 400, 715, 407], "bbox": [656, 400, 715, 407]},
	{"text": "查看收费明细", "bbox": [416, 497, 580, 518], "bbox": [416, 497, 580, 518]},
	{"text": "发送到邮箱", "bbox": [430, 588, 565, 609], "bbox": [430, 588, 565, 609]}
]
2026-08-10 12:45:05,356 INFO     29 [qwen-vl-text] coord API: raw_items=56, valid_items=56, elapsed=27.1s
2026-08-10 12:45:05,356 INFO     29 [qwen-vl-text] coord item[0]: text=11:43, bbox=[391, 20, 455, 36]
2026-08-10 12:45:05,356 INFO     29 [qwen-vl-text] coord item[1]: text=美团, bbox=[489, 24, 507, 32]
2026-08-10 12:45:05,356 INFO     29 [qwen-vl-text] coord item[2]: text=5G, bbox=[675, 20, 692, 28]
2026-08-10 12:45:05,356 INFO     29 [qwen-vl-text] coord item[3]: text=4G, bbox=[720, 20, 735, 28]
2026-08-10 12:45:05,356 INFO     29 [qwen-vl-text] coord item[4]: text=24, bbox=[765, 20, 790, 36]
2026-08-10 12:45:05,356 INFO     29 [qwen-vl-text] coord item[5]: text=电子票预览, bbox=[426, 58, 570, 80]
2026-08-10 12:45:05,356 INFO     29 [qwen-vl-text] coord item[6]: text=www.chinaebill.cn, bbox=[413, 87, 583, 100]
2026-08-10 12:45:05,356 INFO     29 [qwen-vl-text] coord item[7]: text=内蒙古自治区医疗门诊收费票据（电子）, bbox=[339, 134, 650, 147]
2026-08-10 12:45:05,357 INFO     29 [qwen-vl-text] coord item[8]: text=内蒙古, bbox=[485, 148, 514, 156]
2026-08-10 12:45:05,357 INFO     29 [qwen-vl-text] coord item[9]: text=财政部监制, bbox=[475, 157, 525, 167]
2026-08-10 12:45:05,357 INFO     29 [qwen-vl-text] coord item[10]: text=票据代码：15060125, bbox=[219, 177, 296, 184]
2026-08-10 12:45:05,357 INFO     29 [qwen-vl-text] coord item[11]: text=票据号码：0127705695, bbox=[592, 177, 678, 184]
2026-08-10 12:45:05,357 INFO     29 [qwen-vl-text] coord item[12]: text=交款人, bbox=[219, 187, 234, 194]
2026-08-10 12:45:05,357 INFO     29 [qwen-vl-text] coord item[13]: text=用代码：150102********2023, bbox=[289, 187, 405, 194]
2026-08-10 12:45:05,357 INFO     29 [qwen-vl-text] coord item[14]: text=校验码：55e825, bbox=[592, 187, 660, 194]
2026-08-10 12:45:05,357 INFO     29 [qwen-vl-text] coord item[15]: text=交, bbox=[219, 196, 228, 203]
2026-08-10 12:45:05,357 INFO     29 [qwen-vl-text] coord item[16]: text=开票日期：2026-02-12, bbox=[592, 196, 678, 203]
2026-08-10 12:45:05,357 INFO     29 [qwen-vl-text] coord item[17]: text=数量/单位, bbox=[356, 208, 396, 214]
2026-08-10 12:45:05,357 INFO     29 [qwen-vl-text] coord item[18]: text=金额（元）, bbox=[417, 208, 456, 214]
2026-08-10 12:45:05,357 INFO     29 [qwen-vl-text] coord item[19]: text=备注, bbox=[472, 208, 489, 214]
2026-08-10 12:45:05,357 INFO     29 [qwen-vl-text] coord item[20]: text=项目名称, bbox=[544, 208, 579, 214]
2026-08-10 12:45:05,357 INFO     29 [qwen-vl-text] coord item[21]: text=数量/单位, bbox=[635, 208, 674, 214]
2026-08-10 12:45:05,357 INFO     29 [qwen-vl-text] coord item[22]: text=金额（元）, bbox=[696, 208, 734, 214]
2026-08-10 12:45:05,357 INFO     29 [qwen-vl-text] coord item[23]: text=备注, bbox=[750, 208, 766, 214]
2026-08-10 12:45:05,357 INFO     29 [qwen-vl-text] coord item[24]: text=西药费, bbox=[220, 220, 247, 227]
2026-08-10 12:45:05,357 INFO     29 [qwen-vl-text] coord item[25]: text=1, bbox=[357, 220, 362, 227]
2026-08-10 12:45:05,358 INFO     29 [qwen-vl-text] coord item[26]: text=项, bbox=[385, 220, 394, 227]
2026-08-10 12:45:05,358 INFO     29 [qwen-vl-text] coord item[27]: text=188.21, bbox=[429, 220, 456, 227]
2026-08-10 12:45:05,358 INFO     29 [qwen-vl-text] coord item[28]: text=金额合计（大写）壹佰捌拾捌元贰角壹分, bbox=[222, 314, 381, 321]
2026-08-10 12:45:05,358 INFO     29 [qwen-vl-text] coord item[29]: text=(小写)188.21, bbox=[536, 314, 590, 321]
2026-08-10 12:45:05,358 INFO     29 [qwen-vl-text] coord item[30]: text=业务流水号：202602120002043, bbox=[241, 327, 357, 334]
2026-08-10 12:45:05,358 INFO     29 [qwen-vl-text] coord item[31]: text=门诊号：2602120916, bbox=[382, 327, 460, 334]
2026-08-10 12:45:05,358 INFO     29 [qwen-vl-text] coord item[32]: text=就诊日期：20260212, bbox=[654, 327, 731, 334]
2026-08-10 12:45:05,358 INFO     29 [qwen-vl-text] coord item[33]: text=其, bbox=[226, 338, 234, 345]
2026-08-10 12:45:05,358 INFO     29 [qwen-vl-text] coord item[34]: text=医疗机构类型：综合医院, bbox=[241, 343, 335, 350]
2026-08-10 12:45:05,358 INFO     29 [qwen-vl-text] coord item[35]: text=医保类型：职工基本医疗保险, bbox=[382, 343, 495, 350]
2026-08-10 12:45:05,358 INFO     29 [qwen-vl-text] coord item[36]: text=医保编号：150000NMGZG00000000001, bbox=[510, 343, 649, 350]
2026-08-10 12:45:05,358 INFO     29 [qwen-vl-text] coord item[37]: text=性别：女, bbox=[654, 343, 687, 350]
2026-08-10 12:45:05,358 INFO     29 [qwen-vl-text] coord item[38]: text=9506, bbox=[550, 351, 569, 358]
2026-08-10 12:45:05,359 INFO     29 [qwen-vl-text] coord item[39]: text=信, bbox=[226, 365, 234, 372]
2026-08-10 12:45:05,359 INFO     29 [qwen-vl-text] coord item[40]: text=医保统筹基金支付：101.92, bbox=[241, 359, 345, 366]
2026-08-10 12:45:05,359 INFO     29 [qwen-vl-text] coord item[41]: text=其他支付：0.00, bbox=[382, 359, 441, 366]
2026-08-10 12:45:05,359 INFO     29 [qwen-vl-text] coord item[42]: text=个人账户支付：86.29, bbox=[510, 359, 592, 366]
2026-08-10 12:45:05,359 INFO     29 [qwen-vl-text] coord item[43]: text=个人现金支付：0.00, bbox=[654, 359, 731, 366]
2026-08-10 12:45:05,359 INFO     29 [qwen-vl-text] coord item[44]: text=息, bbox=[226, 376, 234, 383]
2026-08-10 12:45:05,359 INFO     29 [qwen-vl-text] coord item[45]: text=个人自付：86.29, bbox=[241, 372, 305, 379]
2026-08-10 12:45:05,359 INFO     29 [qwen-vl-text] coord item[46]: text=个人自费：0.00, bbox=[382, 372, 441, 379]
2026-08-10 12:45:05,359 INFO     29 [qwen-vl-text] coord item[47]: text=交费日期：20260212, bbox=[510, 372, 588, 379]
2026-08-10 12:45:05,359 INFO     29 [qwen-vl-text] coord item[48]: text=备注：医保总金额：188.21符合统筹：169.87账户余额：4301.09医疗救助基金：0大病保险：0公务员补助：0, bbox=[241, 380, 642, 387]
2026-08-10 12:45:05,359 INFO     29 [qwen-vl-text] coord item[49]: text=医疗收费专用章, bbox=[222, 395, 261, 402]
2026-08-10 12:45:05,359 INFO     29 [qwen-vl-text] coord item[50]: text=支付：0企业补充保险：0符合政策范围金额：169.87其他基金：0伙食补助：0起付线：0, bbox=[241, 388, 602, 395]
2026-08-10 12:45:05,359 INFO     29 [qwen-vl-text] coord item[51]: text=（章）：内蒙古自治区国际蒙医医院, bbox=[265, 400, 400, 407]
2026-08-10 12:45:05,359 INFO     29 [qwen-vl-text] coord item[52]: text=复核人：李姹娜, bbox=[539, 400, 596, 407]
2026-08-10 12:45:05,359 INFO     29 [qwen-vl-text] coord item[53]: text=收款人：李姹娜, bbox=[656, 400, 715, 407]
2026-08-10 12:45:05,359 INFO     29 [qwen-vl-text] coord item[54]: text=查看收费明细, bbox=[416, 497, 580, 518]
2026-08-10 12:45:05,359 INFO     29 [qwen-vl-text] coord item[55]: text=发送到邮箱, bbox=[430, 588, 565, 609]
2026-08-10 12:45:05,360 INFO     29 [qwen-vl-text] page=3 — 52/52 coords, api_time=27.1s
2026-08-10 12:45:05,360 INFO     29 [qwen-vl-text] new_positions (52):
[[3, 232.64499999999998, 270.72499999999997, 16.84, 30.311999999999998], [3, 290.955, 301.66499999999996, 20.208, 26.944], [3, 401.625, 411.74, 16.84, 23.576], [3, 428.4, 437.325, 16.84, 23.576], [3, 455.17499999999995, 470.04999999999995, 16.84, 30.311999999999998], [3, 253.47, 339.15, 48.836, 67.36], [3, 245.73499999999999, 346.885, 73.25399999999999, 84.2], [3, 201.70499999999998, 386.75, 112.828, 123.774], [3, 288.575, 305.83, 124.616, 131.352], [3, 282.625, 312.375, 132.194, 140.614], [3, 130.305, 176.12, 149.034, 154.928], [3, 352.24, 403.40999999999997, 149.034, 154.928], [3, 130.305, 139.23, 157.454, 163.34799999999998], [3, 171.95499999999998, 240.975, 157.454, 163.34799999999998], [3, 352.24, 392.7, 157.454, 163.34799999999998], [3, 130.305, 135.66, 165.03199999999998, 170.926], [3, 352.24, 403.40999999999997, 165.03199999999998, 170.926], [3, 211.82, 235.61999999999998, 175.136, 180.188], [3, 248.11499999999998, 271.32, 175.136, 180.188], [3, 280.84, 290.955, 175.136, 180.188], [3, 323.68, 344.505, 175.136, 180.188], [3, 377.825, 401.03, 175.136, 180.188], [3, 414.12, 436.72999999999996, 175.136, 180.188], [3, 446.25, 455.77, 175.136, 180.188], [3, 130.9, 146.965, 185.23999999999998, 191.134], [3, 212.415, 215.39, 185.23999999999998, 191.134], [3, 229.075, 234.42999999999998, 185.23999999999998, 191.134], [3, 255.255, 271.32, 185.23999999999998, 191.134], [3, 132.09, 226.695, 264.388, 270.282], [3, 318.91999999999996, 351.05, 264.388, 270.282], [3, 143.39499999999998, 212.415, 275.334, 281.228], [3, 227.29, 273.7, 275.334, 281.228], [3, 389.13, 434.945, 275.334, 281.228], [3, 134.47, 139.23, 284.596, 290.49], [3, 143.39499999999998, 199.325, 288.806, 294.7], [3, 227.29, 294.525, 288.806, 294.7], [3, 303.45, 386.155, 288.806, 294.7], [3, 389.13, 408.765, 288.806, 294.7], [3, 327.25, 338.555, 295.542, 301.436], [3, 134.47, 139.23, 307.33, 313.224], [3, 143.39499999999998, 205.27499999999998, 302.27799999999996, 308.17199999999997], [3, 227.29, 262.395, 302.27799999999996, 308.17199999999997], [3, 303.45, 352.24, 302.27799999999996, 308.17199999999997], [3, 389.13, 434.945, 302.27799999999996, 308.17199999999997], [3, 134.47, 139.23, 316.592, 322.486], [3, 143.39499999999998, 181.475, 313.224, 319.118], [3, 227.29, 262.395, 313.224, 319.118], [3, 303.45, 349.85999999999996, 313.224, 319.118], [3, 143.39499999999998, 381.99, 319.96, 325.854], [3, 132.09, 155.295, 332.59, 338.484], [3, 143.39499999999998, 358.19, 326.69599999999997, 332.59], [3, 157.67499999999998, 238.0, 336.8, 342.69399999999996]]
2026-08-10 12:45:05,360 INFO     29 [qwen-vl-text] ═══ DONE ═══ 52 positions, pages=1, time=28.7s
2026-08-10 12:45:05,360 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:45:05,369 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:45:05,370 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 12:45:05,370 INFO     29 [qwen-vl-text] positions(43): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:45:05,370 INFO     29 [qwen-vl-text] page grouping: [3, 4, 5], lines per page: [4, 38, 1]
2026-08-10 12:45:05,486 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:45:05,599 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:45:06,127 INFO     29 [qwen-vl-text] page=5, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:45:06,128 INFO     29 [qwen-vl-text] LLM extraction start, text_len=450
2026-08-10 12:45:06,128 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:45:06,129 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 142, \"bbox_end\": 184, \"encounter_dates\": [\"2026-03-04\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "复核人：李姹娜\n收款人：李姹娜\n查看收费明细\n发送到邮箱\n15:38\n954\nwwwwwwwwwwwwwwwwww.pdf\n电子发票(普通发票)\n国家税务总局\n内蒙古自治区税务局\n发票号码：26152000000173167231\n开票日期：2026年03月04日\n购买方信息\n统一社会信用代码/纳税人识别号：150102197111182023\n销售方信息\n名称：国药控股国大药房内蒙古有限公司\n统一社会信用代码/纳税人识别号：911501005732872139\n项目名称\n规格型号\n单位\n数量\n单价\n金额\n税率/征收率\n税额\n*化学药品制剂*布地奈德\n320ug:9ug*60吸\n盒\n1\n274.336283185841\n274.34\n13%\n35.66\n福莫特罗吸入粉雾剂（）\n合计\n￥274.34\n￥35.66\n价税合计（大写）\n叁佰壹拾圆整\n(小写)￥310.00\n备注\n开票人：刘惠\n号号:D20214...医保余额:3631.8CM/KG普通病人|现住址:内蒙古自治区呼和浩特市赛罕区",
    "role": "user"
  }
]
2026-08-10 12:45:06,132 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:45:06.131+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 31, "failed": 0, "current": {"ed8cac4894b811f1bd9827cf206dfa2d": {"id": "ed8cac4894b811f1bd9827cf206dfa2d", "doc_id": "ed520a7a94b811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWRNA(2).pdf", "type": "pdf", "location": "\u9ea6\u6d4eWRNA(2).pdf", "size": 13028580, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786365740553, "task_type": "dataflow", "root_trace_id": "cdcb62f1323147c19d5b537cd2e3ed24", "root_traceparent": "00-cdcb62f1323147c19d5b537cd2e3ed24-dbd2f127625489c0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:45:08,325 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:45:08,325 INFO     29 [qwen-vl-text] LLM output (len=433):
{
  "encounter_date": "2026-03-04",
  "pharmacy": "国药控股国大药房内蒙古有限公司",
  "medications": [
    {
      "name": "布地奈德福莫特罗吸入粉雾剂",
      "specification": "320ug:9ug*60吸",
      "dosage": null,
      "quantity": 1,
      "unit_price": 274.34,
      "total_price": 274.34,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 310.00,
  "payment_method": null
}
2026-08-10 12:45:08,325 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-03-04]
2026-08-10 12:45:08,326 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=623575, prompt_len=652
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共4行）
["复核人：李姹娜", "收款人：李姹娜", "查看收费明细", "发送到邮箱"]

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
2026-08-10 12:45:09,685 INFO     29 [qwen-vl-text] coord API raw response (len=207):
[
	{"text": "复核人：李姹娜", "bbox": [539, 400, 597, 408]},
	{"text": "收款人：李姹娜", "bbox": [656, 400, 716, 408]},
	{"text": "查看收费明细", "bbox": [416, 497, 580, 519]},
	{"text": "发送到邮箱", "bbox": [430, 588, 565, 610]}
]
2026-08-10 12:45:09,686 INFO     29 [qwen-vl-text] coord API: raw_items=4, valid_items=4, elapsed=1.4s
2026-08-10 12:45:09,686 INFO     29 [qwen-vl-text] coord item[0]: text=复核人：李姹娜, bbox=[539, 400, 597, 408]
2026-08-10 12:45:09,686 INFO     29 [qwen-vl-text] coord item[1]: text=收款人：李姹娜, bbox=[656, 400, 716, 408]
2026-08-10 12:45:09,686 INFO     29 [qwen-vl-text] coord item[2]: text=查看收费明细, bbox=[416, 497, 580, 519]
2026-08-10 12:45:09,686 INFO     29 [qwen-vl-text] coord item[3]: text=发送到邮箱, bbox=[430, 588, 565, 610]
2026-08-10 12:45:09,687 INFO     29 [qwen-vl-text] page=3 — 4/4 coords, api_time=1.4s
2026-08-10 12:45:09,688 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=425361, prompt_len=1096
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共38行）
["15:38", "954", "wwwwwwwwwwwwwwwwww.pdf", "电子发票(普通发票)", "国家税务总局", "内蒙古自治区税务局", "发票号码：26152000000173167231", "开票日期：2026年03月04日", "购买方信息", "统一社会信用代码/纳税人识别号：150102197111182023", "销售方信息", "名称：国药控股国大药房内蒙古有限公司", "统一社会信用代码/纳税人识别号：911501005732872139", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*布地奈德", "320ug:9ug*60吸", "盒", "1", "274.336283185841", "274.34", "13%", "35.66", "福莫特罗吸入粉雾剂（）", "合计", "￥274.34", "￥35.66", "价税合计（大写）", "叁佰壹拾圆整", "(小写)￥310.00", "备注", "开票人：刘惠"]

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
2026-08-10 12:45:24,337 INFO     29 [qwen-vl-text] coord API raw response (len=2856):
[
	{"text": "15:38", "bbox": [241, 28, 344, 45]},
	{"text": "954", "bbox": [724, 29, 762, 43]},
	{"text": "wwwwwwwwwwwwwwwwww.pdf", "bbox": [296, 79, 701, 100]},
	{"text": "电子发票(普通发票)", "bbox": [386, 404, 588, 420], "label": "电子发票(普通发票)"},
	{"text": "国家税务总局", "bbox": [475, 420, 521, 428], "label": "国家税务总局"},
	{"text": "内蒙古自治区税务局", "bbox": [470, 430, 532, 440], "label": "内蒙古自治区税务局"},
	{"text": "发票号码：26152000000173167231", "bbox": [652, 410, 791, 418], "label": "发票号码：26152000000173167231"},
	{"text": "开票日期：2026年03月04日", "bbox": [652, 423, 765, 431], "label": "开票日期：2026年03月04日"},
	{"text": "购买方信息", "bbox": [194, 468, 204, 495], "label": "购买方信息"},
	{"text": "统一社会信用代码/纳税人识别号：150102197111182023", "bbox": [210, 482, 484, 490], "label": "统一社会信用代码/纳税人识别号：150102197111182023"},
	{"text": "销售方信息", "bbox": [505, 457, 514, 495], "label": "销售方信息"},
	{"text": "名称：国药控股国大药房内蒙古有限公司", "bbox": [523, 462, 696, 469], "label": "名称：国药控股国大药房内蒙古有限公司"},
	{"text": "统一社会信用代码/纳税人识别号：911501005732872139", "bbox": [523, 482, 794, 490], "label": "统一社会信用代码/纳税人识别号：911501005732872139"},
	{"text": "项目名称", "bbox": [223, 502, 263, 508], "label": "项目名称"},
	{"text": "规格型号", "bbox": [304, 502, 343, 508], "label": "规格型号"},
	{"text": "单位", "bbox": [382, 502, 410, 508], "label": "单位"},
	{"text": "数量", "bbox": [462, 502, 490, 508], "label": "数量"},
	{"text": "单价", "bbox": [538, 502, 565, 508], "label": "单价"},
	{"text": "金额", "bbox": [617, 502, 645, 508], "label": "金额"},
	{"text": "税率/征收率", "bbox": [658, 502, 711, 508], "label": "税率/征收率"},
	{"text": "税额", "bbox": [777, 502, 805, 508], "label": "税额"},
	{"text": "*化学药品制剂*布地奈德", "bbox": [191, 509, 297, 516], "label": "*化学药品制剂*布地奈德"},
	{"text": "320ug:9ug*60吸", "bbox": [305, 509, 368, 516], "label": "320ug:9ug*60吸"},
	{"text": "盒", "bbox": [390, 509, 402, 516], "label": "盒"},
	{"text": "1", "bbox": [485, 509, 490, 516], "label": "1"},
	{"text": "274.336283185841", "bbox": [495, 509, 565, 516], "label": "274.336283185841"},
	{"text": "274.34", "bbox": [619, 509, 645, 516], "label": "274.34"},
	{"text": "13%", "bbox": [680, 509, 698, 516], "label": "13%"},
	{"text": "35.66", "bbox": [785, 509, 805, 516], "label": "35.66"},
	{"text": "福莫特罗吸入粉雾剂（）", "bbox": [191, 519, 296, 526], "label": "福莫特罗吸入粉雾剂（）"},
	{"text": "合计", "bbox": [240, 589, 248, 595], "label": "合计"},
	{"text": "计", "bbox": [288, 589, 297, 595], "label": "计"},
	{"text": "￥274.34", "bbox": [609, 588, 645, 594], "label": "￥274.34"},
	{"text": "￥35.66", "bbox": [775, 588, 805, 594], "label": "￥35.66"},
	{"text": "价税合计（大写）", "bbox": [228, 603, 300, 610], "label": "价税合计（大写）"},
	{"text": "叁佰壹拾圆整", "bbox": [369, 602, 429, 610], "label": "叁佰壹拾圆整"},
	{"text": "(小写)￥310.00", "bbox": [622, 602, 703, 609], "label": "(小写)￥310.00"},
	{"text": "备注", "bbox": [194, 626, 204, 646], "label": "备注"},
	{"text": "开票人：刘惠", "bbox": [236, 669, 295, 676], "label": "开票人：刘惠"}
]
2026-08-10 12:45:24,337 INFO     29 [qwen-vl-text] coord API: raw_items=39, valid_items=39, elapsed=14.6s
2026-08-10 12:45:24,337 INFO     29 [qwen-vl-text] coord item[0]: text=15:38, bbox=[241, 28, 344, 45]
2026-08-10 12:45:24,337 INFO     29 [qwen-vl-text] coord item[1]: text=954, bbox=[724, 29, 762, 43]
2026-08-10 12:45:24,337 INFO     29 [qwen-vl-text] coord item[2]: text=wwwwwwwwwwwwwwwwww.pdf, bbox=[296, 79, 701, 100]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[3]: text=电子发票(普通发票), bbox=[386, 404, 588, 420]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[4]: text=国家税务总局, bbox=[475, 420, 521, 428]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[5]: text=内蒙古自治区税务局, bbox=[470, 430, 532, 440]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[6]: text=发票号码：26152000000173167231, bbox=[652, 410, 791, 418]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[7]: text=开票日期：2026年03月04日, bbox=[652, 423, 765, 431]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[8]: text=购买方信息, bbox=[194, 468, 204, 495]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[9]: text=统一社会信用代码/纳税人识别号：150102197111182023, bbox=[210, 482, 484, 490]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[10]: text=销售方信息, bbox=[505, 457, 514, 495]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[11]: text=名称：国药控股国大药房内蒙古有限公司, bbox=[523, 462, 696, 469]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[12]: text=统一社会信用代码/纳税人识别号：911501005732872139, bbox=[523, 482, 794, 490]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[13]: text=项目名称, bbox=[223, 502, 263, 508]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[14]: text=规格型号, bbox=[304, 502, 343, 508]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[15]: text=单位, bbox=[382, 502, 410, 508]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[16]: text=数量, bbox=[462, 502, 490, 508]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[17]: text=单价, bbox=[538, 502, 565, 508]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[18]: text=金额, bbox=[617, 502, 645, 508]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[19]: text=税率/征收率, bbox=[658, 502, 711, 508]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[20]: text=税额, bbox=[777, 502, 805, 508]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[21]: text=*化学药品制剂*布地奈德, bbox=[191, 509, 297, 516]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[22]: text=320ug:9ug*60吸, bbox=[305, 509, 368, 516]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[23]: text=盒, bbox=[390, 509, 402, 516]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[24]: text=1, bbox=[485, 509, 490, 516]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[25]: text=274.336283185841, bbox=[495, 509, 565, 516]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[26]: text=274.34, bbox=[619, 509, 645, 516]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[27]: text=13%, bbox=[680, 509, 698, 516]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[28]: text=35.66, bbox=[785, 509, 805, 516]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[29]: text=福莫特罗吸入粉雾剂（）, bbox=[191, 519, 296, 526]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[30]: text=合计, bbox=[240, 589, 248, 595]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[31]: text=计, bbox=[288, 589, 297, 595]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[32]: text=￥274.34, bbox=[609, 588, 645, 594]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[33]: text=￥35.66, bbox=[775, 588, 805, 594]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[34]: text=价税合计（大写）, bbox=[228, 603, 300, 610]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[35]: text=叁佰壹拾圆整, bbox=[369, 602, 429, 610]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[36]: text=(小写)￥310.00, bbox=[622, 602, 703, 609]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[37]: text=备注, bbox=[194, 626, 204, 646]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] coord item[38]: text=开票人：刘惠, bbox=[236, 669, 295, 676]
2026-08-10 12:45:24,338 INFO     29 [qwen-vl-text] page=4 — 38/38 coords, api_time=14.6s
2026-08-10 12:45:24,357 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8548994, prompt_len=666
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["号号:D20214...医保余额:3631.8CM/KG普通病人|现住址:内蒙古自治区呼和浩特市赛罕区"]

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
2026-08-10 12:45:26,026 INFO     29 [qwen-vl-text] coord API raw response (len=95):
[
	{"text": "号号:D20214...医保余额:3631.8CM/KG普通病人|现住址:内蒙古自治区呼和浩特市赛罕区", "bbox": [0, 45, 1000, 78]}
]
2026-08-10 12:45:26,026 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=1.7s
2026-08-10 12:45:26,026 INFO     29 [qwen-vl-text] coord item[0]: text=号号:D20214...医保余额:3631.8CM/KG普通病人|现住址:内蒙古自治区呼和浩特市赛罕区, bbox=[0, 45, 1000, 78]
2026-08-10 12:45:26,029 INFO     29 [qwen-vl-text] page=5 — 1/1 coords, api_time=1.7s
2026-08-10 12:45:26,030 INFO     29 [qwen-vl-text] new_positions (43):
[[3, 320.705, 355.215, 336.8, 343.536], [3, 390.32, 426.02, 336.8, 343.536], [3, 247.51999999999998, 345.09999999999997, 418.474, 436.998], [3, 255.85, 336.175, 495.096, 513.62], [4, 143.39499999999998, 204.67999999999998, 23.576, 37.89], [4, 430.78, 453.39, 24.418, 36.205999999999996], [4, 176.12, 417.09499999999997, 66.518, 84.2], [4, 229.67, 349.85999999999996, 340.168, 353.64], [4, 282.625, 309.995, 353.64, 360.376], [4, 279.65, 316.53999999999996, 362.06, 370.47999999999996], [4, 387.94, 470.645, 345.21999999999997, 351.95599999999996], [4, 387.94, 455.17499999999995, 356.166, 362.902], [4, 115.42999999999999, 121.38, 394.056, 416.78999999999996], [4, 124.94999999999999, 287.97999999999996, 405.844, 412.58], [4, 300.47499999999997, 305.83, 384.794, 416.78999999999996], [4, 311.185, 414.12, 389.00399999999996, 394.89799999999997], [4, 311.185, 472.43, 405.844, 412.58], [4, 132.685, 156.48499999999999, 422.68399999999997, 427.736], [4, 180.88, 204.08499999999998, 422.68399999999997, 427.736], [4, 227.29, 243.95, 422.68399999999997, 427.736], [4, 274.89, 291.55, 422.68399999999997, 427.736], [4, 320.11, 336.175, 422.68399999999997, 427.736], [4, 367.115, 383.775, 422.68399999999997, 427.736], [4, 391.51, 423.04499999999996, 422.68399999999997, 427.736], [4, 462.315, 478.97499999999997, 422.68399999999997, 427.736], [4, 113.645, 176.715, 428.578, 434.472], [4, 181.475, 218.95999999999998, 428.578, 434.472], [4, 232.04999999999998, 239.19, 428.578, 434.472], [4, 288.575, 291.55, 428.578, 434.472], [4, 294.525, 336.175, 428.578, 434.472], [4, 368.305, 383.775, 428.578, 434.472], [4, 404.59999999999997, 415.31, 428.578, 434.472], [4, 467.075, 478.97499999999997, 428.578, 434.472], [4, 113.645, 176.12, 436.998, 442.892], [4, 142.79999999999998, 147.56, 495.938, 500.99], [4, 171.35999999999999, 176.715, 495.938, 500.99], [4, 362.35499999999996, 383.775, 495.096, 500.14799999999997], [4, 461.125, 478.97499999999997, 495.096, 500.14799999999997], [4, 135.66, 178.5, 507.726, 513.62], [4, 219.55499999999998, 255.255, 506.88399999999996, 513.62], [4, 370.09, 418.28499999999997, 506.88399999999996, 512.778], [4, 115.42999999999999, 121.38, 527.092, 543.932], [5, 0.0, 595.0, 37.89, 65.676]]
2026-08-10 12:45:26,030 INFO     29 [qwen-vl-text] ═══ DONE ═══ 43 positions, pages=3, time=20.7s
2026-08-10 12:45:26,031 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:45:26,032 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:45:26,032 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 12:45:26,033 INFO     29 [qwen-vl-text] positions(25): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:45:26,033 INFO     29 [qwen-vl-text] page grouping: [7], lines per page: [25]
2026-08-10 12:45:26,277 INFO     29 [qwen-vl-text] page=7, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:45:26,279 INFO     29 [qwen-vl-text] LLM extraction start, text_len=210
2026-08-10 12:45:26,279 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:45:26,279 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 265, \"bbox_end\": 289, \"encounter_dates\": [\"2026-02-12\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "医疗收费明细（电子）\n所属电\n15060125\n所属电子票据号码:0127705695\n交\n开票日期:2026年02月12日\n项目名称\n数量/单位\n金额（元）\n备注\n西药费(小计:188.2100元)\n布地奈德福莫特罗吸入粉雾剂（II）\n60\n吸\n183.4100\n乙\n醋酸泼尼松片\n100\n片\n4.8000\n甲\n小计 188.2100\n合计 188.2100\n收款单位（章）内蒙古自治区国际蒙医医院\n1 页 共 1 页",
    "role": "user"
  }
]
2026-08-10 12:45:28,980 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:45:28,981 INFO     29 [qwen-vl-text] LLM output (len=689):
{
  "encounter_date": "2026-02-12",
  "pharmacy": "内蒙古自治区国际蒙医医院",
  "medications": [
    {
      "name": "布地奈德福莫特罗吸入粉雾剂（II）",
      "specification": null,
      "dosage": null,
      "quantity": 60,
      "unit_price": null,
      "total_price": 183.41,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    },
    {
      "name": "醋酸泼尼松片",
      "specification": null,
      "dosage": null,
      "quantity": 100,
      "unit_price": null,
      "total_price": 4.8,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 188.21,
  "payment_method": null
}
2026-08-10 12:45:28,981 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-12]
2026-08-10 12:45:28,987 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1418903, prompt_len=898
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["医疗收费明细（电子）", "所属电", "15060125", "所属电子票据号码:0127705695", "交", "开票日期:2026年02月12日", "项目名称", "数量/单位", "金额（元）", "备注", "西药费(小计:188.2100元)", "布地奈德福莫特罗吸入粉雾剂（II）", "60", "吸", "183.4100", "乙", "醋酸泼尼松片", "100", "片", "4.8000", "甲", "小计 188.2100", "合计 188.2100", "收款单位（章）内蒙古自治区国际蒙医医院", "1 页 共 1 页"]

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
2026-08-10 12:45:38,293 INFO     29 [qwen-vl-text] coord API raw response (len=1789):
[
	{"text": "医疗收费明细（电子）", "bbox": [400, 26, 628, 44]},
	{"text": "所属电", "bbox": [170, 69, 214, 81], "label": "所属电"},
	{"text": "15060125", "bbox": [297, 68, 364, 80], "label": "15060125"},
	{"text": "所属电子票据号码:0127705695", "bbox": [631, 63, 860, 79], "label": "所属电子票据号码:0127705695"},
	{"text": "交", "bbox": [170, 85, 194, 97], "label": "交"},
	{"text": "开票日期:2026年02月12日", "bbox": [631, 80, 848, 95], "label": "开票日期:2026年02月12日"},
	{"text": "项目名称", "bbox": [300, 101, 366, 113], "label": "项目名称"},
	{"text": "数量/单位", "bbox": [497, 100, 572, 111], "label": "数量/单位"},
	{"text": "金额（元）", "bbox": [630, 100, 705, 112], "label": "金额（元）"},
	{"text": "备注", "bbox": [768, 100, 800, 111], "label": "备注"},
	{"text": "西药费(小计:188.2100元)", "bbox": [173, 117, 368, 132], "label": "西药费(小计:188.2100元)"},
	{"text": "布地奈德福莫特罗吸入粉雾剂（II）", "bbox": [173, 136, 440, 150], "label": "布地奈德福莫特罗吸入粉雾剂（II）"},
	{"text": "60", "bbox": [496, 136, 515, 147], "label": "60"},
	{"text": "吸", "bbox": [534, 135, 552, 147], "label": "吸"},
	{"text": "183.4100", "bbox": [643, 136, 717, 148], "label": "183.4100"},
	{"text": "乙", "bbox": [735, 136, 752, 148], "label": "乙"},
	{"text": "醋酸泼尼松片", "bbox": [173, 155, 270, 169], "label": "醋酸泼尼松片"},
	{"text": "100", "bbox": [492, 154, 520, 166], "label": "100"},
	{"text": "片", "bbox": [534, 153, 552, 166], "label": "片"},
	{"text": "4.8000", "bbox": [660, 155, 717, 167], "label": "4.8000"},
	{"text": "甲", "bbox": [735, 155, 752, 167], "label": "甲"},
	{"text": "小计 188.2100", "bbox": [178, 737, 273, 750], "label": "小计 188.2100"},
	{"text": "合计 188.2100", "bbox": [178, 750, 273, 764], "label": "合计 188.2100"},
	{"text": "收款单位（章）内蒙古自治区国际蒙医医院", "bbox": [170, 772, 486, 790], "label": "收款单位（章）内蒙古自治区国际蒙医医院"},
	{"text": "1 页 共 1 页", "bbox": [755, 775, 859, 787], "label": "1 页 共 1 页"}
]
2026-08-10 12:45:38,293 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=9.3s
2026-08-10 12:45:38,294 INFO     29 [qwen-vl-text] coord item[0]: text=医疗收费明细（电子）, bbox=[400, 26, 628, 44]
2026-08-10 12:45:38,294 INFO     29 [qwen-vl-text] coord item[1]: text=所属电, bbox=[170, 69, 214, 81]
2026-08-10 12:45:38,294 INFO     29 [qwen-vl-text] coord item[2]: text=15060125, bbox=[297, 68, 364, 80]
2026-08-10 12:45:38,294 INFO     29 [qwen-vl-text] coord item[3]: text=所属电子票据号码:0127705695, bbox=[631, 63, 860, 79]
2026-08-10 12:45:38,294 INFO     29 [qwen-vl-text] coord item[4]: text=交, bbox=[170, 85, 194, 97]
2026-08-10 12:45:38,294 INFO     29 [qwen-vl-text] coord item[5]: text=开票日期:2026年02月12日, bbox=[631, 80, 848, 95]
2026-08-10 12:45:38,294 INFO     29 [qwen-vl-text] coord item[6]: text=项目名称, bbox=[300, 101, 366, 113]
2026-08-10 12:45:38,294 INFO     29 [qwen-vl-text] coord item[7]: text=数量/单位, bbox=[497, 100, 572, 111]
2026-08-10 12:45:38,294 INFO     29 [qwen-vl-text] coord item[8]: text=金额（元）, bbox=[630, 100, 705, 112]
2026-08-10 12:45:38,294 INFO     29 [qwen-vl-text] coord item[9]: text=备注, bbox=[768, 100, 800, 111]
2026-08-10 12:45:38,294 INFO     29 [qwen-vl-text] coord item[10]: text=西药费(小计:188.2100元), bbox=[173, 117, 368, 132]
2026-08-10 12:45:38,294 INFO     29 [qwen-vl-text] coord item[11]: text=布地奈德福莫特罗吸入粉雾剂（II）, bbox=[173, 136, 440, 150]
2026-08-10 12:45:38,295 INFO     29 [qwen-vl-text] coord item[12]: text=60, bbox=[496, 136, 515, 147]
2026-08-10 12:45:38,295 INFO     29 [qwen-vl-text] coord item[13]: text=吸, bbox=[534, 135, 552, 147]
2026-08-10 12:45:38,295 INFO     29 [qwen-vl-text] coord item[14]: text=183.4100, bbox=[643, 136, 717, 148]
2026-08-10 12:45:38,295 INFO     29 [qwen-vl-text] coord item[15]: text=乙, bbox=[735, 136, 752, 148]
2026-08-10 12:45:38,295 INFO     29 [qwen-vl-text] coord item[16]: text=醋酸泼尼松片, bbox=[173, 155, 270, 169]
2026-08-10 12:45:38,295 INFO     29 [qwen-vl-text] coord item[17]: text=100, bbox=[492, 154, 520, 166]
2026-08-10 12:45:38,295 INFO     29 [qwen-vl-text] coord item[18]: text=片, bbox=[534, 153, 552, 166]
2026-08-10 12:45:38,296 INFO     29 [qwen-vl-text] coord item[19]: text=4.8000, bbox=[660, 155, 717, 167]
2026-08-10 12:45:38,296 INFO     29 [qwen-vl-text] coord item[20]: text=甲, bbox=[735, 155, 752, 167]
2026-08-10 12:45:38,296 INFO     29 [qwen-vl-text] coord item[21]: text=小计 188.2100, bbox=[178, 737, 273, 750]
2026-08-10 12:45:38,296 INFO     29 [qwen-vl-text] coord item[22]: text=合计 188.2100, bbox=[178, 750, 273, 764]
2026-08-10 12:45:38,296 INFO     29 [qwen-vl-text] coord item[23]: text=收款单位（章）内蒙古自治区国际蒙医医院, bbox=[170, 772, 486, 790]
2026-08-10 12:45:38,296 INFO     29 [qwen-vl-text] coord item[24]: text=1 页 共 1 页, bbox=[755, 775, 859, 787]
2026-08-10 12:45:38,297 INFO     29 [qwen-vl-text] page=7 — 25/25 coords, api_time=9.3s
2026-08-10 12:45:38,297 INFO     29 [qwen-vl-text] new_positions (25):
[[7, 238.0, 373.65999999999997, 21.892, 37.048], [7, 101.14999999999999, 127.33, 58.098, 68.202], [7, 176.715, 216.57999999999998, 57.256, 67.36], [7, 375.445, 511.7, 53.046, 66.518], [7, 101.14999999999999, 115.42999999999999, 71.57, 81.67399999999999], [7, 375.445, 504.56, 67.36, 79.99], [7, 178.5, 217.76999999999998, 85.042, 95.146], [7, 295.715, 340.34, 84.2, 93.462], [7, 374.84999999999997, 419.47499999999997, 84.2, 94.304], [7, 456.96, 476.0, 84.2, 93.462], [7, 102.935, 218.95999999999998, 98.514, 111.14399999999999], [7, 102.935, 261.8, 114.512, 126.3], [7, 295.12, 306.425, 114.512, 123.774], [7, 317.72999999999996, 328.44, 113.67, 123.774], [7, 382.585, 426.615, 114.512, 124.616], [7, 437.325, 447.44, 114.512, 124.616], [7, 102.935, 160.65, 130.51, 142.298], [7, 292.74, 309.4, 129.668, 139.772], [7, 317.72999999999996, 328.44, 128.826, 139.772], [7, 392.7, 426.615, 130.51, 140.614], [7, 437.325, 447.44, 130.51, 140.614], [7, 105.91, 162.435, 620.554, 631.5], [7, 105.91, 162.435, 631.5, 643.288], [7, 101.14999999999999, 289.16999999999996, 650.024, 665.18], [7, 449.22499999999997, 511.10499999999996, 652.55, 662.654]]
2026-08-10 12:45:38,297 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=12.3s
2026-08-10 12:45:38,297 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:45:38,308 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:45:38,309 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 12:45:38,309 INFO     29 [qwen-vl-text] positions(16): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:45:38,309 INFO     29 [qwen-vl-text] page grouping: [8], lines per page: [16]
2026-08-10 12:45:38,541 INFO     29 [qwen-vl-text] page=8, rect=592x842, img=(1646x2339), dpi=200
2026-08-10 12:45:38,543 INFO     29 [qwen-vl-text] LLM extraction start, text_len=200
2026-08-10 12:45:38,543 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:45:38,543 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 290, \"bbox_end\": 305, \"encounter_dates\": [\"2025-12-26\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "鹤春堂大药房\n2025-12-26 12:29:31\n收银员：张星\n名称 单价 数量 金额\n布地奈德福莫特罗吸入粉雾剂(II)\n320 μg /9 μg / 吸 60 吸 / 支\n298.00 1 298.00\n应收金额: 298.00\n实收金额: 298.00\n找零: 0.00\n优惠: 0.00\n会员:\n本次积分: 298\n合计积分: 729\n祝您身体健康，药品属于特殊商品\n无质量问题，概不退换",
    "role": "user"
  }
]
2026-08-10 12:45:38,547 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:45:38.546+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 31, "failed": 0, "current": {"ed8cac4894b811f1bd9827cf206dfa2d": {"id": "ed8cac4894b811f1bd9827cf206dfa2d", "doc_id": "ed520a7a94b811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWRNA(2).pdf", "type": "pdf", "location": "\u9ea6\u6d4eWRNA(2).pdf", "size": 13028580, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786365740553, "task_type": "dataflow", "root_trace_id": "cdcb62f1323147c19d5b537cd2e3ed24", "root_traceparent": "00-cdcb62f1323147c19d5b537cd2e3ed24-dbd2f127625489c0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:45:40,839 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:45:40,839 INFO     29 [qwen-vl-text] LLM output (len=440):
{
  "encounter_date": "2025-12-26",
  "pharmacy": "鹤春堂大药房",
  "medications": [
    {
      "name": "布地奈德福莫特罗吸入粉雾剂(II)",
      "specification": "320 μg /9 μg / 吸 60 吸 / 支",
      "dosage": null,
      "quantity": 1,
      "unit_price": 298.00,
      "total_price": 298.00,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 298.00,
  "payment_method": null
}
2026-08-10 12:45:40,840 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-26]
2026-08-10 12:45:40,852 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2877163, prompt_len=861
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["鹤春堂大药房", "2025-12-26 12:29:31", "收银员：张星", "名称 单价 数量 金额", "布地奈德福莫特罗吸入粉雾剂(II)", "320 μg /9 μg / 吸 60 吸 / 支", "298.00 1 298.00", "应收金额: 298.00", "实收金额: 298.00", "找零: 0.00", "优惠: 0.00", "会员:", "本次积分: 298", "合计积分: 729", "祝您身体健康，药品属于特殊商品", "无质量问题，概不退换"]

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
2026-08-10 12:45:46,667 INFO     29 [qwen-vl-text] coord API raw response (len=907):
[
	{"text": "鹤春堂大药房", "bbox": [426, 269, 603, 296]},
	{"text": "2025-12-26 12:29:31", "bbox": [282, 289, 585, 322]},
	{"text": "收银员：张星", "bbox": [282, 314, 465, 344]},
	{"text": "名称 单价 数量 金额", "bbox": [280, 368, 707, 400]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(II)", "bbox": [278, 396, 740, 426]},
	{"text": "320 μg /9 μg / 吸 60 吸 / 支", "bbox": [275, 423, 738, 453]},
	{"text": "298.00 1 298.00", "bbox": [274, 452, 582, 477]},
	{"text": "应收金额: 298.00", "bbox": [274, 504, 550, 528]},
	{"text": "实收金额: 298.00", "bbox": [274, 530, 549, 553]},
	{"text": "找零: 0.00", "bbox": [272, 558, 458, 580]},
	{"text": "优惠: 0.00", "bbox": [272, 584, 457, 607]},
	{"text": "会员:", "bbox": [272, 611, 346, 633]},
	{"text": "本次积分: 298", "bbox": [271, 638, 470, 660]},
	{"text": "合计积分: 729", "bbox": [271, 664, 470, 687]},
	{"text": "祝您身体健康，药品属于特殊商品", "bbox": [269, 690, 725, 715]},
	{"text": "无质量问题，概不退换", "bbox": [271, 723, 567, 745]}
]
2026-08-10 12:45:46,667 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=5.8s
2026-08-10 12:45:46,667 INFO     29 [qwen-vl-text] coord item[0]: text=鹤春堂大药房, bbox=[426, 269, 603, 296]
2026-08-10 12:45:46,667 INFO     29 [qwen-vl-text] coord item[1]: text=2025-12-26 12:29:31, bbox=[282, 289, 585, 322]
2026-08-10 12:45:46,667 INFO     29 [qwen-vl-text] coord item[2]: text=收银员：张星, bbox=[282, 314, 465, 344]
2026-08-10 12:45:46,667 INFO     29 [qwen-vl-text] coord item[3]: text=名称 单价 数量 金额, bbox=[280, 368, 707, 400]
2026-08-10 12:45:46,667 INFO     29 [qwen-vl-text] coord item[4]: text=布地奈德福莫特罗吸入粉雾剂(II), bbox=[278, 396, 740, 426]
2026-08-10 12:45:46,667 INFO     29 [qwen-vl-text] coord item[5]: text=320 μg /9 μg / 吸 60 吸 / 支, bbox=[275, 423, 738, 453]
2026-08-10 12:45:46,667 INFO     29 [qwen-vl-text] coord item[6]: text=298.00 1 298.00, bbox=[274, 452, 582, 477]
2026-08-10 12:45:46,667 INFO     29 [qwen-vl-text] coord item[7]: text=应收金额: 298.00, bbox=[274, 504, 550, 528]
2026-08-10 12:45:46,667 INFO     29 [qwen-vl-text] coord item[8]: text=实收金额: 298.00, bbox=[274, 530, 549, 553]
2026-08-10 12:45:46,667 INFO     29 [qwen-vl-text] coord item[9]: text=找零: 0.00, bbox=[272, 558, 458, 580]
2026-08-10 12:45:46,667 INFO     29 [qwen-vl-text] coord item[10]: text=优惠: 0.00, bbox=[272, 584, 457, 607]
2026-08-10 12:45:46,667 INFO     29 [qwen-vl-text] coord item[11]: text=会员:, bbox=[272, 611, 346, 633]
2026-08-10 12:45:46,667 INFO     29 [qwen-vl-text] coord item[12]: text=本次积分: 298, bbox=[271, 638, 470, 660]
2026-08-10 12:45:46,667 INFO     29 [qwen-vl-text] coord item[13]: text=合计积分: 729, bbox=[271, 664, 470, 687]
2026-08-10 12:45:46,667 INFO     29 [qwen-vl-text] coord item[14]: text=祝您身体健康，药品属于特殊商品, bbox=[269, 690, 725, 715]
2026-08-10 12:45:46,667 INFO     29 [qwen-vl-text] coord item[15]: text=无质量问题，概不退换, bbox=[271, 723, 567, 745]
2026-08-10 12:45:46,668 INFO     29 [qwen-vl-text] page=8 — 16/16 coords, api_time=5.8s
2026-08-10 12:45:46,668 INFO     29 [qwen-vl-text] new_positions (16):
[[8, 252.37985705566405, 357.24191033935546, 226.46841394042968, 249.1994443359375], [8, 167.06835607910156, 346.57797271728515, 243.30621423339844, 271.08858471679684], [8, 167.06835607910156, 275.4850552368164, 264.35346459960937, 289.6101650390625], [8, 165.88347412109374, 418.8557721557617, 309.815525390625, 336.756005859375], [8, 164.69859216308595, 438.4063244628906, 333.38844580078126, 358.6451462402344], [8, 162.92126922607423, 437.2214425048828, 356.11947619628904, 381.3761766357422], [8, 162.3288282470703, 344.80064978027343, 380.53428662109377, 401.5815369873047], [8, 162.3288282470703, 325.84253845214846, 424.3125673828125, 444.517927734375], [8, 162.3288282470703, 325.25009747314454, 446.2017077636719, 465.5651781005859], [8, 161.1439462890625, 271.3379683837891, 469.7746281738281, 488.29620849609375], [8, 161.1439462890625, 270.74552740478515, 491.6637685546875, 511.02723889160154], [8, 161.1439462890625, 204.98457873535156, 514.3947989501953, 532.916379272461], [8, 160.5515053100586, 278.44726013183595, 537.1258293457031, 555.6474096679688], [8, 160.5515053100586, 278.44726013183595, 559.0149697265625, 578.3784400634765], [8, 159.36662335205077, 429.519709777832, 580.9041101074218, 601.9513604736328], [8, 160.5515053100586, 335.91403509521484, 608.6864805908203, 627.2080609130859]]
2026-08-10 12:45:46,668 INFO     29 [qwen-vl-text] ═══ DONE ═══ 16 positions, pages=1, time=8.4s
2026-08-10 12:45:46,675 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 12:45:46,676 INFO     29 [Trace] task=ed8cac48 | doc=麦济WRNA(2).pdf | Extractor:Medication | outputs={"chunks": "5 items, types={'MedicationRecord': 5}", "html": "", "json": "306 items", "markdown": "", "text": "", "name": "麦济WRNA(2).pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Medication\": 5}"}
2026-08-10 12:45:46,676 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 12:45:46,681 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:45:46,681 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:45:48,239 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:45:48,248 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 12:45:48,248 INFO     29 [Trace] task=ed8cac48 | doc=麦济WRNA(2).pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "306 items", "markdown": "", "text": "", "name": "麦济WRNA(2).pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Medication\": 5}"}
2026-08-10 12:45:48,248 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 12:45:48,253 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:45:48,253 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:45:49,493 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:45:49,498 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 12:45:49,498 INFO     29 [Trace] task=ed8cac48 | doc=麦济WRNA(2).pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "306 items", "markdown": "", "text": "", "name": "麦济WRNA(2).pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Medication\": 5}"}
2026-08-10 12:45:49,499 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 12:45:49,505 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:45:49,505 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:45:50,096 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:45:50,107 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 12:45:50,108 INFO     29 [Trace] task=ed8cac48 | doc=麦济WRNA(2).pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "306 items", "markdown": "", "text": "", "name": "麦济WRNA(2).pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Medication\": 5}"}
2026-08-10 12:45:50,108 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 12:45:50,118 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:45:50,118 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:45:51,219 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:45:51,227 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 12:45:51,227 INFO     29 [Trace] task=ed8cac48 | doc=麦济WRNA(2).pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "306 items", "markdown": "", "text": "", "name": "麦济WRNA(2).pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Medication\": 5}"}
2026-08-10 12:45:51,227 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 12:45:51,233 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:45:51,233 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:45:51,730 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:45:51,740 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 12:45:51,740 INFO     29 [Trace] task=ed8cac48 | doc=麦济WRNA(2).pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "306 items", "markdown": "", "text": "", "name": "麦济WRNA(2).pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Medication\": 5}"}
2026-08-10 12:45:51,740 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 12:45:51,741 INFO     29 [ChunkMerger] Merged 9 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 4, 'Extractor:Medication': 5, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 7 noise chunks)
2026-08-10 12:45:51,753 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 12:45:51,753 INFO     29 [Trace] task=ed8cac48 | doc=麦济WRNA(2).pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "9 items, types={'OutpatientRecord': 4, 'MedicationRecord': 5}", "name": "麦济WRNA(2).pdf"}
2026-08-10 12:45:51,753 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 12:45:51,821 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786365742947, 'update_date': datetime.datetime(2026, 8, 10, 12, 42, 22), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 997955, 'status': '1'}
2026-08-10 12:45:52,034 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=内蒙古医科大学附属医院门诊病历
姓名：
年龄：54岁
诊疗号：0010304094
民族：蒙古
性别：女性
科室：呼吸内科门诊
联系电话：
身份证：
病情：
就诊状态：
就诊时间：2026-02-27 16:58
生命体征（需要时）：
体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg
主诉：诊断支气管哮喘10余年，加重1月。
现病史：诊断支气管哮喘10余年，加重1月。夜间发作，咳白色粘痰，有黄
色鼻涕。每日吸入信必可都保，症状无改善。
既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎
无，吸烟史无，无过敏史。
体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺未闻及啰
音，双下肢无水肿，体重kg。
辅助检查：待回报
过敏史：不详
初步诊断（西医）：1.支气管哮喘
初步诊断（中医）：
治疗方案：随诊
血常规
免疫球蛋白IgE
一次性肺功能仪用过滤嘴
肺炎支原体IgM抗体免疫
肺炎支原体IgG抗体免疫C反应蛋白测定
室
室
磷酸可待因片<15mg>
用量：1.000片/次
用法：口服，一次/日，5天
桉柠蒎肠溶胶囊<桉柠蒎油计0.3g/粒>
用量：1.000粒/次
用法：口服，二次/日，7天
签名：
---
内蒙古医科大学附属医院门诊病历
姓名：
年龄：54岁
诊疗号：0010304094
民族：蒙古
性别：女性
科室：呼吸内科门诊
联系电话：
身份证：
病情：
就诊状态：
就诊时间：2024-03-01 09:48
生命体征（需要时）：
体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg
主诉：诊断支气管哮喘10余年，加重1月。
现病史：诊断支气管哮喘10余年，加重1月。夜间发作，咳白色粘痰，有黄
色鼻涕。每日吸入信必可都保，症状无改善。
既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎
无，吸烟史无，无过敏史。鼻炎
体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺干鸣音，双
下肢无水肿，体重kg。
辅助检查：待回报
过敏史：不详
初步诊断（西医）：1.支气管哮喘 2.过敏性鼻炎[变应性鼻炎]
初步诊断（中医）：
治疗方案：
多索茶碱片<0.2g>
用量：0.200g/次
用法：口服，一次/日，7天
布地奈德福莫特罗吸入粉雾剂
用量：1.000吸/次
(Ⅱ)<(160μg/4.5μg)/吸*60>
用法：吸入，二次/日，3天
签名：李
---
报告
闭环管理
治疗
健康调阅
三诺血糖
华益血糖
门诊记录:
□痕迹
□批注
历信息
内蒙古医科大学附属医院门诊病历
姓名
年龄:51岁
诊疗号:0010304094
民族:蒙古族
性别:女性
科室:呼吸内科门诊
联系电话:
身份证:
病情:
就诊状态:
就诊时间:2023-03-0410:51
生命体征(需要时):
体温:℃脉搏:次/分呼吸:次/分血压:/mmHg
主诉:咳嗽1月,哮喘病史10余年
现病史:
既往史:患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎
有,20年,吸烟史无,无过敏史。
体格检查:发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰
音,双下肢无水肿,体重kg。
辅助检查:肺功能正常
过敏史:
初步诊断(西医):1.支气管哮喘
初步诊断(中医):
治疗方案:
CT胸部
最大通气量功能检查呼吸过滤器
肺弥散功能检查--口残气容积测定-氮气平肺通气功能检查
气法
衡法
孟鲁司特钠片<10mg>
用量:1.000片/次
用法:口服,一次/每晚,7天
布地奈德福莫特罗吸入粉雾剂(11)
用量:1.000吸/次
<(320μg/9μg)/吸*60>
用法:吸入,二次/日,7天
签名:
---
付丹
26星期二
190.1.48.233
王王立
内蒙古自治区国际蒙医医院
门诊病历
门诊号：2602120916
姓
科室：呼吸与危重症医学科门 性别：女性 出生年月：1971-11-18
诊
就诊时间：2026-02-12 11:20
○初诊◎复诊
过敏史：□否 □不详 □有：
主 诉：发作性咳嗽、气短5年，加重3天
现病史：5年前出现发作性咳嗽、气短，吸入刺激性气味后症状明显，就诊于当地医院诊断
为“支气管哮喘”，长期规律吸入信必可治疗后效果欠佳。近3天喘息加重，伴咳嗽、咳痰较前
频繁。夜间明显。
既往史：体健
家族史：无
体格检查：意识：清醒
T：36.5℃ P：71次/分 R：18次/分 BP：115/77mmHg
双肺可闻及干鸣音
辅助检查：
处方信息：
布地奈德福莫特罗吸入粉雾剂（II）(160μg/4.5μg/吸*60吸/支)*1支
320μg 吸入 bid
醋酸泼尼松片(5mg*100片/瓶)*1瓶
15mg 口服 qd
其他处置：
复诊记录：
门诊诊断：支气管哮喘(急性发作期)
医生签名：苏佳
---
鹤春堂大药房
2026-01-21 17:23:52
收银员：张星
名称 单价 数量 金额
布地奈德福莫特罗吸入粉雾剂(Ⅱ)
320 μg /9 μg / 吸 60 吸 / 支
298.00 2 596.00
应收金额: 596.00
实收金额: 596.00
找零: 0.00
优惠: 0.00
会员:
本次积分: 596
合计积分: 1325
祝您身体健康，药品属于特殊商品
无质量问题，概不退换
---
11:43
美团
5G
4G
24
电子票预览
www.chinaebill.cn
内蒙古自治区医疗门诊收费票据（电子）
内蒙古
财政部监制
票据代码：15060125
票据号码：0127705695
交款人
用代码：150102********2023
校验码：55e825
交
开票日期：2026-02-12
数量/单位
金额（元）
备注
项目名称
数量/单位
金额（元）
备注
西药费
1
项
188.21
金额合计（大写）壹佰捌拾捌元贰角壹分
(小写)188.21
业务流水号：202602120002043
门诊号：2602120916
就诊日期：20260212
其
医疗机构类型：综合医院
医保类型：职工基本医疗保险
医保编号：150000NMGZG00000000001
性别：女
9506
信
医保统筹基金支付：101.92
其他支付：0.00
个人账户支付：86.29
个人现金支付：0.00
息
个人自付：86.29
个人自费：0.00
交费日期：20260212
备注：医保总金额：188.21符合统筹：169.87账户余额：4301.09医疗救助基金：0大病保险：0公务员补助：0
医疗收费专用章
支付：0企业补充保险：0符合政策范围金额：169.87其他基金：0伙食补助：0起付线：0
（章）：内蒙古自治区国际蒙医医院
---
复核人：李姹娜
收款人：李姹娜
查看收费明细
发送到邮箱
15:38
954
wwwwwwwwwwwwwwwwww.pdf
电子发票(普通发票)
国家税务总局
内蒙古自治区税务局
发票号码：26152000000173167231
开票日期：2026年03月04日
购买方信息
统一社会信用代码/纳税人识别号：150102197111182023
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
*化学药品制剂*布地奈德
320ug:9ug*60吸
盒
1
274.336283185841
274.34
13%
35.66
福莫特罗吸入粉雾剂（）
合计
￥274.34
￥35.66
价税合计（大写）
叁佰壹拾圆整
(小写)￥310.00
备注
开票人：刘惠
号号:D20214...医保余额:3631.8CM/KG普通病人|现住址:内蒙古自治区呼和浩特市赛罕区
---
医疗收费明细（电子）
所属电
15060125
所属电子票据号码:0127705695
交
开票日期:2026年02月12日
项目名称
数量/单位
金额（元）
备注
西药费(小计:188.2100元)
布地奈德福莫特罗吸入粉雾剂（II）
60
吸
183.4100
乙
醋酸泼尼松片
100
片
4.8000
甲
小计 188.2100
合计 188.2100
收款单位（章）内蒙古自治区国际蒙医医院
1 页 共 1 页
---
鹤春堂大药房
2025-12-26 12:29:31
收银员：张星
名称 单价 数量 金额
布地奈德福莫特罗吸入粉雾剂(II)
320 μg /9 μg / 吸 60 吸 / 支
298.00 1 298.00
应收金额: 298.00
实收金额: 298.00
找零: 0.00
优惠: 0.00
会员:
本次积分: 298
合计积分: 729
祝您身体健康，药品属于特殊商品
无质量问题，概不退换
2026-08-10 12:45:52,499 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 12:45:52,499 INFO     29 [Trace] task=ed8cac48 | doc=麦济WRNA(2).pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "9 items, types={'OutpatientRecord': 4, 'MedicationRecord': 5}", "name": "麦济WRNA(2).pdf", "embedding_token_consumption": 2899}
2026-08-10 12:45:52,499 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 12:45:52,700 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 12:45:52,700 INFO     29 [Trace] task=ed8cac48 | doc=麦济WRNA(2).pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":9,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 12:45:52,705 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:45:52,705 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:45:52,705 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:45:52,705 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:45:52,705 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:45:52,705 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:45:52,705 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:45:52,705 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:45:52,705 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:45:52,710 INFO     29 set_progress(ed8cac4894b811f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 12:45:52 [DOC Engine]:
Start to index...
2026-08-10 12:45:52,725 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.010s]
2026-08-10 12:45:52,729 INFO     29 set_progress(ed8cac4894b811f1bd9827cf206dfa2d), progress: 0.8111111111111111, progress_msg: 
2026-08-10 12:45:52,743 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.007s]
2026-08-10 12:45:52,751 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.005s]
2026-08-10 12:45:52,763 INFO     29 set_progress(ed8cac4894b811f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 12:45:52 Indexing done (0.05s). Task done (200.60s)
2026-08-10 12:45:52,768 INFO     29 [Done], chunks(9), token(2899), elapsed:200.60
2026-08-10 12:45:52,884 INFO     29 handle_task done for task {"id": "ed8cac4894b811f1bd9827cf206dfa2d", "doc_id": "ed520a7a94b811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWRNA(2).pdf", "type": "pdf", "location": "\u9ea6\u6d4eWRNA(2).pdf", "size": 13028580, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786365740553, "task_type": "dataflow", "root_trace_id": "cdcb62f1323147c19d5b537cd2e3ed24", "root_traceparent": "00-cdcb62f1323147c19d5b537cd2e3ed24-dbd2f127625489c0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
