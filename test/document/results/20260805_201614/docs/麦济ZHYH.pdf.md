# 基准结果：麦济ZHYH.pdf

## 基本信息

- 文件：`麦济ZHYH.pdf`
- 大小：10282.5 KB
- PDF 总页数：6
- doc_id：`b2448c9e90be11f1a3da71efcdd7cc1f`
- 上传方式：existing
- 状态：run=None (code=None)  progress=None
- 开始时间：2026-08-05T20:16:33  完成时间：2026-08-05T20:16:34  耗时：0.9s
- progress_msg：`12:06:00 Indexing done (0.05s). Task done (401.23s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | b374f610 | 1 | 1-1 | 内蒙古医科大学附属医院门诊病历 姓名： 年龄：62岁 诊疗号：001449878 |
| 2 | e38862c0 | 1 | 2-2 | 萱堂大药房 单号：2025111853212 日期：25/11/18 时间：13 |
| 3 | e1d4cb24 | 1 | 3-3 | 电子发票(普通发票) 国家税务总局 江苏省税务局 发票号码：2532200000 |
| 4 | 9a7bd366 | 2 | 4-5 | 电子发票(普通发票) 国家税务总局 江苏省税务局 发票号码：2532200000 |
| 5 | 46b6148f | 1 | 5-5 | 报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录: 病历信息 □痕迹 |
| 6 | dc27349c | 1 | 6-6 | 电子发票(普通发票) 国家税务总局 内蒙古自治区税务局 发票号码：2615200 |

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
- ChunkMerger：`{"found": true, "merged": 6, "sources": 8, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 2, "Extractor:Medication": 4, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1}, "filtered_noise": 6}`
- Extractor skip 证据：5 条
  - `[no_text_noise] 2026-08-05 12:01:26,096 INFO     29 [ChunkMerger] Merged 9 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 4, 'Extractor:Medication': 5, 'Extractor:Prescr`
  - `[no_text_noise] 2026-08-05 12:03:48,680 INFO     29 [ChunkMerger] Merged 13 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Presc`
  - `[no_text_noise] 2026-08-05 12:03:51,930 INFO     29 [ChunkMerger] Merged 5 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 3, 'Extractor:Prescr`
  - `[no_text_noise] 2026-08-05 12:04:12,921 INFO     29 [ChunkMerger] Merged 7 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 3, 'Extractor:Medication': 1, 'Extractor:Prescr`
  - `[no_text_noise] 2026-08-05 12:05:59,813 INFO     29 [ChunkMerger] Merged 6 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 4, 'Extractor:Prescr`
- worker 日志错误：1 条
  - `2026-08-05 12:01:09,186 ERROR    29 LoggingWorker error:`

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-05 11:59:18,559 INFO     29 handle_task begin for task {"id": "b28be2ce90be11f1a3da71efcdd7cc1f", "doc_id": "b2448c9e90be11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHYH.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHYH.pdf", "size": 10529265, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785928413891, "task_type": "dataflow", "root_trace_id": "e3dcb8801128457d8d83b73c11855569", "root_traceparent": "00-e3dcb8801128457d8d83b73c11855569-a468dda7915c610d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-05 11:59:18,762 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-05 11:59:18,808 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-05 11:59:18,830 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:59:18,832 WARNING  29 lock update_progress failed: acquire postgres lock update_progress timeout, retrying (1/3)
2026-08-05 11:59:18,835 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-05 11:59:18,835 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-05 11:59:18,855 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-05 11:59:18,855 INFO     29 ============================================================
2026-08-05 11:59:18,855 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-05 11:59:18,855 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-05 11:59:18,855 INFO     29 ============================================================
2026-08-05 11:59:18,855 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-05 11:59:18,855 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-05 11:59:18,857 INFO     29 No torch found.
2026-08-05 11:59:19,756 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=6
2026-08-05 11:59:19,837 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-05 11:59:19,837 INFO     29 [Trace] task=aff34070 | doc=麦济WRNA(2).pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "304 items", "markdown": "", "text": "", "name": "麦济WRNA(2).pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Medication\": 5}"}
2026-08-05 11:59:19,837 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-05 11:59:19,840 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:59:19,840 INFO     29 [qwen-vl-text] LLM output (len=442):
{
  "encounter_date": "2025-12-24",
  "pharmacy": "国药控股国大药房内蒙古有限公司第三百七十三分公司",
  "medications": [
    {
      "name": "布地奈德福莫特罗吸入粉雾剂",
      "specification": "320ug:9ug*60吸",
      "dosage": null,
      "quantity": 1,
      "unit_price": 306.93,
      "total_price": 306.93,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 310.00,
  "payment_method": null
}
2026-08-05 11:59:19,840 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-24]
2026-08-05 11:59:19,842 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1352692, prompt_len=1040
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["电子发票(普通发票)", "发票号码：25152000000077385777", "开票日期：2025年12月24日", "购买方信息", "统一社会信用代码/纳税人识别号", "销售方信息", "名称：国药控股国大药房内蒙古有限公司第三百七十三分公司", "统一社会信用代码/纳税人识别号：91150121MACGJJ2Q46", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*布地奈德", "320ug:9ug*60吸", "盒", "1", "306.930693069307", "306.93", "1%", "3.07", "福莫特罗吸入粉雾剂", "合计", "¥306.93", "¥3.07", "价税合计(大写)", "叁佰壹拾圆整", "(小写)¥310.00", "收款人:马利亚;", "复核人:梁会荣", "备注", "开票人:梁会荣"]

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
2026-08-05 11:59:20,167 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1836114, prompt_len=764
2026-08-05 11:59:22,160 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2020-02-13"}
```
2026-08-05 11:59:22,160 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2020-02-13
2026-08-05 11:59:22,174 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1836114, prompt_len=401
2026-08-05 11:59:25,449 INFO     29 [qwen-vl-parser] text API response (len=479):
["内蒙古医科大学附属医院门诊病历", "姓名：", "年龄：62岁", "诊疗号：0014498780", "民族：", "性别：男性", "呼吸内科门诊", "联系电话：", "1", "身份证：", "病情：", "就诊状态：", "就诊时间：2026-02-13 09:14", "生命体征（需要时）：", "体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg", "主诉：哮喘史，近3天呼吸困难加重，夜间咳嗽明显", "现病史：哮喘史，近3天呼吸困难加重，夜间咳嗽明显", "既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "无，吸烟史无，无过敏史。", "体格检查：发育正常，营养良好，体型正常，双肺呼吸音清，双肺未闻及啰", "音，双下肢无水肿，体重kg。", "辅助检查：心肺", "过敏史：不详", "初步诊断（西医）：1.支气管哮喘(急性发作期)", "初步诊断（中医）：", "治疗方案：随诊", "醋酸泼尼松片<5mg>", "用量：3.000片/次", "用法：口服，一次/日，5天", "签名："]
2026-08-05 11:59:25,450 INFO     29 [qwen-vl-parser] page=1 text: 30 lines (bbox 0-29)
2026-08-05 11:59:25,450 INFO     29 [qwen-vl-parser] page=1 text: 30 sections
2026-08-05 11:59:25,746 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1481445, prompt_len=764
2026-08-05 11:59:27,284 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 11:59:27,285 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-05 11:59:27,294 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1481445, prompt_len=401
2026-08-05 11:59:29,997 INFO     29 [qwen-vl-parser] text API response (len=259):
["萱堂大药房", "单号：2025111853212", "日期：25/11/18", "时间：13:2", "工号：001", "品名", "规格", "厂家", "金额", "数量", "总计", "布地格福吸入气雾剂", "60ug/7.2ug/4.8ug 吸", "120 撤/支", "支/盒", "219.00", "3", "657.00", "合计：657.00", "应收：657.00", "数量：3", "实收：657.00", "会员：", "药品属于特殊商品", "无质量问题，概不退换"]
2026-08-05 11:59:29,998 INFO     29 [qwen-vl-parser] page=2 text: 25 lines (bbox 30-54)
2026-08-05 11:59:29,998 INFO     29 [qwen-vl-parser] page=2 text: 25 sections
2026-08-05 11:59:30,125 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=778524, prompt_len=764
2026-08-05 11:59:31,489 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 11:59:31,490 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-05 11:59:31,497 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=778524, prompt_len=401
2026-08-05 11:59:34,713 INFO     29 [qwen-vl-parser] text API response (len=467):
["电子发票(普通发票)", "国家税务总局", "江苏省税务局", "发票号码：25322000000382591347", "开票日期：2025年08月20日", "购买方信息", "名称：", "统一社会信用代码/纳税人识别号：", "销售方信息", "名称：无锡邻医大药房有限公司", "统一社会信用代码/纳税人识别号：91320214MA228F680W", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*倍择瑞令", "160μg/7.2μg/4", "盒", "3", "210.029498522124", "630.09", "13%", "81.91", "畅布地格福吸入气雾剂", ".8μg*120揿", "", "", "", "", "", "", "", "合计", "￥630.09", "￥81.91", "价税合计（大写）", "柒佰壹拾贰圆整", "(小写) ￥712.00", "备注", "开票人：奚澳琼"]
2026-08-05 11:59:34,713 INFO     29 [qwen-vl-parser] page=3 text: 37 lines (bbox 55-91)
2026-08-05 11:59:34,713 INFO     29 [qwen-vl-parser] page=3 text: 37 sections
2026-08-05 11:59:34,839 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=730743, prompt_len=764
2026-08-05 11:59:36,351 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 11:59:36,351 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-05 11:59:36,361 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=730743, prompt_len=401
2026-08-05 11:59:39,288 INFO     29 [qwen-vl-parser] text API response (len=423):
["电子发票(普通发票)", "国家税务总局", "江苏省税务局", "发票号码：25322000000226700883", "开票日期：2025年05月20日", "购买方信息", "名称", "统一社会信用代码/纳税人识别号：", "销售方信息", "名称：无锡邻医大药房有限公司", "统一社会信用代码/纳税人识别号：91320214MA228F680W", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*倍择瑞令", "160μg/7.2μg/4", "盒", "3 210.029498522124", "630.09", "13%", "81.91", "畅布地格福吸入气雾剂", ".8μg*120揿", "合计", "￥630.09", "￥81.91", "价税合计（大写）", "柒佰壹拾贰圆整", "(小写）￥712.00", "备注"]
2026-08-05 11:59:39,289 INFO     29 [qwen-vl-parser] page=4 text: 35 lines (bbox 92-126)
2026-08-05 11:59:39,289 INFO     29 [qwen-vl-parser] page=4 text: 35 sections
2026-08-05 11:59:39,980 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5637139, prompt_len=764
2026-08-05 11:59:41,019 INFO     29 [qwen-vl-text] coord API raw response (len=3077):
[
	{"text": "电子发票(普通发票)", "bbox": [328, 82, 645, 128], "bbox_2d": [328, 82, 645, 128]},
	{"text": "发票号码：25152000000077385777", "bbox": [738, 103, 965, 125], "bbox_2d": [738, 103, 965, 125]},
	{"text": "开票日期：2025年12月24日", "bbox": [737, 146, 918, 168], "bbox_2d": [737, 146, 918, 168]},
	{"text": "购买方信息", "bbox": [32, 257, 45, 378], "bbox_2d": [32, 257, 45, 378]},
	{"text": "统一社会信用代码/纳税人识别号", "bbox": [58, 340, 251, 360], "bbox_2d": [58, 340, 251, 360]},
	{"text": "销售方信息", "bbox": [510, 258, 522, 380], "bbox_2d": [510, 258, 522, 380]},
	{"text": "名称：国药控股国大药房内蒙古有限公司第三百七十三分公司", "bbox": [537, 265, 936, 288], "bbox_2d": [537, 265, 936, 288]},
	{"text": "统一社会信用代码/纳税人识别号：91150121MACGJJ2Q46", "bbox": [535, 340, 956, 363], "bbox_2d": [535, 340, 956, 363]},
	{"text": "项目名称", "bbox": [80, 403, 140, 423], "bbox_2d": [80, 403, 140, 423]},
	{"text": "规格型号", "bbox": [202, 404, 262, 424], "bbox_2d": [202, 404, 262, 424]},
	{"text": "单位", "bbox": [322, 404, 367, 424], "bbox_2d": [322, 404, 367, 424]},
	{"text": "数量", "bbox": [445, 405, 490, 425], "bbox_2d": [445, 405, 490, 425]},
	{"text": "单价", "bbox": [565, 405, 609, 425], "bbox_2d": [565, 405, 609, 425]},
	{"text": "金额", "bbox": [687, 406, 731, 426], "bbox_2d": [687, 406, 731, 426]},
	{"text": "税率/征收率", "bbox": [752, 406, 836, 426], "bbox_2d": [752, 406, 836, 426]},
	{"text": "税额", "bbox": [929, 406, 974, 426], "bbox_2d": [929, 406, 974, 426]},
	{"text": "*化学药品制剂*布地奈德", "bbox": [25, 424, 190, 447], "bbox_2d": [25, 424, 190, 447]},
	{"text": "320ug:9ug*60吸", "bbox": [201, 428, 308, 450], "bbox_2d": [201, 428, 308, 450]},
	{"text": "盒", "bbox": [335, 428, 352, 450], "bbox_2d": [335, 428, 352, 450]},
	{"text": "1", "bbox": [483, 431, 491, 449], "bbox_2d": [483, 431, 491, 449]},
	{"text": "306.930693069307", "bbox": [502, 431, 609, 449], "bbox_2d": [502, 431, 609, 449]},
	{"text": "306.93", "bbox": [686, 431, 731, 450], "bbox_2d": [686, 431, 731, 450]},
	{"text": "1%", "bbox": [789, 432, 804, 450], "bbox_2d": [789, 432, 804, 450]},
	{"text": "3.07", "bbox": [951, 432, 982, 450], "bbox_2d": [951, 432, 982, 450]},
	{"text": "福莫特罗吸入粉雾剂", "bbox": [25, 457, 160, 479], "bbox_2d": [25, 457, 160, 479]},
	{"text": "合计", "bbox": [105, 678, 118, 696], "bbox_2d": [105, 678, 118, 696]},
	{"text": "计", "bbox": [178, 678, 192, 697], "bbox_2d": [178, 678, 192, 697]},
	{"text": "¥306.93", "bbox": [677, 684, 733, 704], "bbox_2d": [677, 684, 733, 704]},
	{"text": "¥3.07", "bbox": [940, 685, 981, 705], "bbox_2d": [940, 685, 981, 705]},
	{"text": "价税合计(大写)", "bbox": [88, 722, 198, 743], "bbox_2d": [88, 722, 198, 743]},
	{"text": "叁佰壹拾圆整", "bbox": [303, 720, 393, 744], "bbox_2d": [303, 720, 393, 744]},
	{"text": "(小写)¥310.00", "bbox": [692, 727, 807, 752], "bbox_2d": [692, 727, 807, 752]},
	{"text": "收款人:马利亚;", "bbox": [60, 760, 163, 782], "bbox_2d": [60, 760, 163, 782]},
	{"text": "复核人:梁会荣", "bbox": [193, 763, 290, 785], "bbox_2d": [193, 763, 290, 785]},
	{"text": "备注", "bbox": [38, 794, 51, 813], "bbox_2d": [38, 794, 51, 813]},
	{"text": "开票人:梁会荣", "bbox": [100, 932, 200, 956], "bbox_2d": [100, 932, 200, 956]}
]
2026-08-05 11:59:41,019 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=21.2s
2026-08-05 11:59:41,019 INFO     29 [qwen-vl-text] coord item[0]: text=电子发票(普通发票), bbox=[328, 82, 645, 128]
2026-08-05 11:59:41,019 INFO     29 [qwen-vl-text] coord item[1]: text=发票号码：25152000000077385777, bbox=[738, 103, 965, 125]
2026-08-05 11:59:41,019 INFO     29 [qwen-vl-text] coord item[2]: text=开票日期：2025年12月24日, bbox=[737, 146, 918, 168]
2026-08-05 11:59:41,019 INFO     29 [qwen-vl-text] coord item[3]: text=购买方信息, bbox=[32, 257, 45, 378]
2026-08-05 11:59:41,019 INFO     29 [qwen-vl-text] coord item[4]: text=统一社会信用代码/纳税人识别号, bbox=[58, 340, 251, 360]
2026-08-05 11:59:41,019 INFO     29 [qwen-vl-text] coord item[5]: text=销售方信息, bbox=[510, 258, 522, 380]
2026-08-05 11:59:41,019 INFO     29 [qwen-vl-text] coord item[6]: text=名称：国药控股国大药房内蒙古有限公司第三百七十三分公司, bbox=[537, 265, 936, 288]
2026-08-05 11:59:41,019 INFO     29 [qwen-vl-text] coord item[7]: text=统一社会信用代码/纳税人识别号：91150121MACGJJ2Q46, bbox=[535, 340, 956, 363]
2026-08-05 11:59:41,019 INFO     29 [qwen-vl-text] coord item[8]: text=项目名称, bbox=[80, 403, 140, 423]
2026-08-05 11:59:41,019 INFO     29 [qwen-vl-text] coord item[9]: text=规格型号, bbox=[202, 404, 262, 424]
2026-08-05 11:59:41,019 INFO     29 [qwen-vl-text] coord item[10]: text=单位, bbox=[322, 404, 367, 424]
2026-08-05 11:59:41,019 INFO     29 [qwen-vl-text] coord item[11]: text=数量, bbox=[445, 405, 490, 425]
2026-08-05 11:59:41,019 INFO     29 [qwen-vl-text] coord item[12]: text=单价, bbox=[565, 405, 609, 425]
2026-08-05 11:59:41,019 INFO     29 [qwen-vl-text] coord item[13]: text=金额, bbox=[687, 406, 731, 426]
2026-08-05 11:59:41,019 INFO     29 [qwen-vl-text] coord item[14]: text=税率/征收率, bbox=[752, 406, 836, 426]
2026-08-05 11:59:41,019 INFO     29 [qwen-vl-text] coord item[15]: text=税额, bbox=[929, 406, 974, 426]
2026-08-05 11:59:41,019 INFO     29 [qwen-vl-text] coord item[16]: text=*化学药品制剂*布地奈德, bbox=[25, 424, 190, 447]
2026-08-05 11:59:41,019 INFO     29 [qwen-vl-text] coord item[17]: text=320ug:9ug*60吸, bbox=[201, 428, 308, 450]
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] coord item[18]: text=盒, bbox=[335, 428, 352, 450]
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] coord item[19]: text=1, bbox=[483, 431, 491, 449]
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] coord item[20]: text=306.930693069307, bbox=[502, 431, 609, 449]
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] coord item[21]: text=306.93, bbox=[686, 431, 731, 450]
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] coord item[22]: text=1%, bbox=[789, 432, 804, 450]
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] coord item[23]: text=3.07, bbox=[951, 432, 982, 450]
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] coord item[24]: text=福莫特罗吸入粉雾剂, bbox=[25, 457, 160, 479]
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] coord item[25]: text=合计, bbox=[105, 678, 118, 696]
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] coord item[26]: text=计, bbox=[178, 678, 192, 697]
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] coord item[27]: text=¥306.93, bbox=[677, 684, 733, 704]
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] coord item[28]: text=¥3.07, bbox=[940, 685, 981, 705]
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] coord item[29]: text=价税合计(大写), bbox=[88, 722, 198, 743]
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] coord item[30]: text=叁佰壹拾圆整, bbox=[303, 720, 393, 744]
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] coord item[31]: text=(小写)¥310.00, bbox=[692, 727, 807, 752]
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] coord item[32]: text=收款人:马利亚;, bbox=[60, 760, 163, 782]
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] coord item[33]: text=复核人:梁会荣, bbox=[193, 763, 290, 785]
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] coord item[34]: text=备注, bbox=[38, 794, 51, 813]
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] coord item[35]: text=开票人:梁会荣, bbox=[100, 932, 200, 956]
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] page=0 — 35/35 coords, api_time=21.2s
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] new_positions (35):
[[0, 276.176, 543.09, 48.79, 76.16], [0, 621.396, 812.53, 61.285, 74.375], [0, 620.554, 772.956, 86.86999999999999, 99.96], [0, 26.944, 37.89, 152.915, 224.91], [0, 48.836, 211.34199999999998, 202.29999999999998, 214.2], [0, 429.41999999999996, 439.524, 153.51, 226.1], [0, 452.154, 788.112, 157.67499999999998, 171.35999999999999], [0, 450.46999999999997, 804.952, 202.29999999999998, 215.98499999999999], [0, 67.36, 117.88, 239.785, 251.685], [0, 170.084, 220.60399999999998, 240.38, 252.28], [0, 271.12399999999997, 309.014, 240.38, 252.28], [0, 374.69, 412.58, 240.975, 252.875], [0, 475.72999999999996, 512.778, 240.975, 252.875], [0, 578.454, 615.502, 241.57, 253.47], [0, 633.184, 703.9119999999999, 241.57, 253.47], [0, 782.218, 820.108, 241.57, 253.47], [0, 21.05, 159.98, 252.28, 265.965], [0, 169.242, 259.336, 254.66, 267.75], [0, 282.07, 296.384, 254.66, 267.75], [0, 406.686, 413.42199999999997, 256.445, 267.155], [0, 422.68399999999997, 512.778, 256.445, 267.155], [0, 577.612, 615.502, 256.445, 267.75], [0, 664.338, 676.968, 257.03999999999996, 267.75], [0, 800.742, 826.8439999999999, 257.03999999999996, 267.75], [0, 21.05, 134.72, 271.91499999999996, 285.005], [0, 88.41, 99.356, 403.40999999999997, 414.12], [0, 149.876, 161.664, 403.40999999999997, 414.715], [0, 570.034, 617.1859999999999, 406.97999999999996, 418.88], [0, 791.48, 826.002, 407.575, 419.47499999999997], [0, 74.096, 166.716, 429.59, 442.085], [0, 255.126, 330.906, 428.4, 442.68], [0, 582.664, 679.494, 432.565, 447.44], [0, 50.519999999999996, 137.246, 452.2, 465.28999999999996], [0, 162.506, 244.17999999999998, 453.98499999999996, 467.075], [0, 31.996, 42.942, 472.43, 483.73499999999996]]
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] ═══ DONE ═══ 35 positions, pages=1, time=120.8s
2026-08-05 11:59:41,020 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] positions(23): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:59:41,020 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [23]
2026-08-05 11:59:41,369 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 11:59:41,370 INFO     29 [qwen-vl-text] LLM extraction start, text_len=205
2026-08-05 11:59:41,370 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:59:41,371 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 119, \"bbox_end\": 141, \"encounter_dates\": [\"2026-01-19\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "欣源药业\nNO:2026011900323\n商品名称\n单价\n数量\n小计\n布地奈德福莫特罗吸入粉雾剂320ug:\n9ug*60吸/盒\n309.00\n2\n618.00\n阿斯利康\n批号: PKGF\n效期:2027-03 规格:1支/盒\n总计:\n2.00\n618.00\n会员卡号:800310\n会员姓名:\n本次积分:618.00\n累计积分:2518.10\n收银员004营业员004\n日期26-01-1910:53:22",
    "role": "user"
  }
]
[92m11:59:41 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:59:41,373 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:59:41,380 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:59:41,380 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m11:59:41 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:59:41,384 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:59:41,385 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:59:41,385 INFO     29 [qwen-vl-text] LLM output (len=1145):
{
  "exam_date": "2026-02-09",
  "report_date": null,
  "exam_name": "一口气法弥散功能报告",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "测定结果：FeNO 60:11ppb CaNO :1.0ppb\n操作员：蒋细萍\n张日石\n一口气法弥散功能报告\n姓名：\n年龄：38岁\n性别：女\n科别：\n保险：\n预计值模式：Standard-now\n测试号：2026020917\n身高：155 cm\n体重：60 kg\n备注：\n联系电话：\n操作者：蒋细萍\nCO (%)\nVolume (L)\nCH4 [%]\n-0.25\n-0.20\n-0.15\n-0.10\n-0.05\n0\n5\n10\n15\n20\n25\n30\nTime [s]\nPred\nBest\nBest%\nAct1\nDLCO SB\n[mmol/min/kPa]\n8.08\n9.45\n116.9\n9.45\nDLCO/VA\n[mmol/min/kPa/L]\n1.82\n2.38\n130.8\n2.38\nVA\n[L]\n4.29\n3.97\n92.5\n3.97\nVC IN\n[L]\n3.03\n2.26\n74.6\n1.00\nDiscard vol\n[L]\n0.53\nSample vol\n[L]\nERV\n[L]\n1.10\nIRV\n[L]\nIC\n[L]\n1.93\nVT\n[L]\n0.43\nVC MAX\n[L]\n3.03\n2.26\n74.6\nTLC-SB\n[L]\n4.44\n4.10\n92.4\n4.10\nRV-SB\n[L]\n1.41\n2.18\n154.5\n2.18\nRV%TLC-SB\n[%]\n31.88\n53.26\n167.1\n53.26\nFRC-SB\n[L]\n2.51\n2.39\n95.2\n2.39\nFRC%TLC-SB\n[%]\n51.18\n58.28\n113.9\n58.28\n测试日期\n26/2/0",
  "conclusion": "意见：\n1.弥散功能在正常范围。\n2.残气量、残总比增高，肺总量在正常范围。",
  "physician": null,
  "reviewer": null
}
2026-08-05 11:59:41,386 INFO     29 [qwen-vl-text] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1026194, prompt_len=664
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共3行）
["测定结果：FeNO 60:11ppb CaNO :1.0ppb", "操作员：蒋细萍", "张日石"]

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
2026-08-05 11:59:42,030 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-12-10"}
```
2026-08-05 11:59:42,031 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=2024-12-10
2026-08-05 11:59:42,050 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5637139, prompt_len=401
2026-08-05 11:59:42,765 INFO     29 [qwen-vl-text] coord API raw response (len=190):
```json
[
	{"text": "测定结果：FeNO 60:11ppb CaNO :1.0ppb", "bbox": [176, 833, 544, 848]},
	{"text": "操作员：蒋细萍", "bbox": [176, 853, 297, 867]},
	{"text": "张日石", "bbox": [718, 870, 786, 897]}
]
```
2026-08-05 11:59:42,765 INFO     29 [qwen-vl-text] coord API: raw_items=3, valid_items=3, elapsed=1.4s
2026-08-05 11:59:42,765 INFO     29 [qwen-vl-text] coord item[0]: text=测定结果：FeNO 60:11ppb CaNO :1.0ppb, bbox=[176, 833, 544, 848]
2026-08-05 11:59:42,765 INFO     29 [qwen-vl-text] coord item[1]: text=操作员：蒋细萍, bbox=[176, 853, 297, 867]
2026-08-05 11:59:42,765 INFO     29 [qwen-vl-text] coord item[2]: text=张日石, bbox=[718, 870, 786, 897]
2026-08-05 11:59:42,765 INFO     29 [qwen-vl-text] page=15 — 3/3 coords, api_time=1.4s
2026-08-05 11:59:42,766 INFO     29 [qwen-vl-text] coord API call start, page=16, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=658017, prompt_len=1638
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共113行）
["一口气法弥散功能报告", "姓名：", "年龄：38岁", "性别：女", "科别：", "保险：", "预计值模式：Standard-now", "测试号：2026020917", "身高：155 cm", "体重：60 kg", "备注：", "联系电话：", "操作者：蒋细萍", "CO (%)", "Volume (L)", "CH4 [%]", "-0.25", "-0.20", "-0.15", "-0.10", "-0.05", "0", "5", "10", "15", "20", "25", "30", "Time [s]", "Pred", "Best", "Best%", "Act1", "DLCO SB", "[mmol/min/kPa]", "8.08", "9.45", "116.9", "9.45", "DLCO/VA", "[mmol/min/kPa/L]", "1.82", "2.38", "130.8", "2.38", "VA", "[L]", "4.29", "3.97", "92.5", "3.97", "VC IN", "[L]", "3.03", "2.26", "74.6", "1.00", "Discard vol", "[L]", "0.53", "Sample vol", "[L]", "ERV", "[L]", "1.10", "IRV", "[L]", "IC", "[L]", "1.93", "VT", "[L]", "0.43", "VC MAX", "[L]", "3.03", "2.26", "74.6", "TLC-SB", "[L]", "4.44", "4.10", "92.4", "4.10", "RV-SB", "[L]", "1.41", "2.18", "154.5", "2.18", "RV%TLC-SB", "[%]", "31.88", "53.26", "167.1", "53.26", "FRC-SB", "[L]", "2.51", "2.39", "95.2", "2.39", "FRC%TLC-SB", "[%]", "51.18", "58.28", "113.9", "58.28", "测试日期", "26/2/0", "意见：", "1.弥散功能在正常范围。", "2.残气量、残总比增高，肺总量在正常范围。"]

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
2026-08-05 11:59:47,686 INFO     29 [qwen-vl-parser] text API response (len=557):
["挂号号:D20091... 医保余额:0 CM/KG 普通病人|现住址:内蒙古土默特左旗沙尔营乡大有庄村32", "报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录:", "病历信息 □痕迹 □批注 置未 ▼ 状态:只读-仅供查看 120% >", "内蒙古医科大学附属医院门诊病历", "姓名 龄:60岁 诊疗号:0014498780", "民族: 别:男性 科室:呼吸内科门诊", "联系电话: 身份证:1 病情:", "就诊状态: 就诊时间:2024-12-10 12:37", "生命体征(需要时):", "体温:℃ 脉搏:次/分 呼吸:次/分 血压:/mmHg", "主诉:SSSJ项目肺功能检查开单", "现病史:哮喘", "既往史:患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎", "无,吸烟史无,无过敏史。", "体格检查:发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰", "音,双下肢无水肿,体重kg。", "辅助检查:", "初步诊断(西医):1.哮喘", "初步诊断(中医):", "治疗方案:/", "呼吸过滤器 肺通气功能检查", "用量:", "用法:", "签名:崔丽英", "3:34 星期二 190.1.48.233 版本 王立红"]
2026-08-05 11:59:47,688 INFO     29 [qwen-vl-parser] page=5 text: 25 lines (bbox 127-151)
2026-08-05 11:59:47,688 INFO     29 [qwen-vl-parser] page=5 text: 25 sections
2026-08-05 11:59:47,816 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=809094, prompt_len=764
2026-08-05 11:59:49,296 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 11:59:49,296 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-05 11:59:49,310 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=809094, prompt_len=401
2026-08-05 11:59:53,147 INFO     29 [qwen-vl-parser] text API response (len=612):
["电子发票(普通发票)", "国家税务总局", "内蒙古自治区税务局", "发票号码：26152000000119478346", "开票日期：2026年02月09日", "购买方信息", "名称", "统一社会信用代码/纳税人识别号：", "销售方信息", "名称：国药控股国大药房内蒙古有限公司", "统一社会信用代码/纳税人识别号：911501005732872139", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*布地格福", "160ug:7.2ug/4.8u", "盒", "3", "237.16814159292", "711.50", "13%", "92.50", "吸入气雾剂", "g:120揿", "", "", "", "", "", "", "", "*化学药品制剂*布地格福", "160ug:7.2ug/4.8u", "盒", "3", "237.16814159292", "711.50", "13%", "92.50", "吸入气雾剂", "g:120揿", "", "", "", "", "", "", "", "", "合计", "￥1423.00", "￥185.00", "价税合计（大写）", "壹仟陆佰零捌圆整", "(小写) ￥1608.00", "备注", "开票人：刘惠"]
2026-08-05 11:59:53,147 INFO     29 [qwen-vl-parser] page=6 text: 47 lines (bbox 152-198)
2026-08-05 11:59:53,147 INFO     29 [qwen-vl-parser] page=6 text: 47 sections
2026-08-05 11:59:53,147 INFO     29 [qwen-vl-parser] parse_pdf done: 199 sections from 6 pages.
2026-08-05 11:59:53,159 INFO     29 Close text detector.
2026-08-05 11:59:53,570 INFO     29 Close text recognizer.
2026-08-05 11:59:53,968 INFO     29 Close recognizer.
2026-08-05 11:59:54,377 INFO     29 Close recognizer.
2026-08-05 12:00:13,155 INFO     29 [qwen-vl-text] coord API raw response (len=5659):
[
	{"text": "一口气法弥散功能报告", "bbox": [417, 91, 678, 107]},
	{"text": "姓名：", "bbox": [222, 119, 261, 131]},
	{"text": "年龄：38岁", "bbox": [222, 132, 405, 145]},
	{"text": "性别：女", "bbox": [222, 145, 382, 158]},
	{"text": "科别：", "bbox": [222, 158, 261, 170]},
	{"text": "保险：", "bbox": [222, 170, 261, 182]},
	{"text": "预计值模式：Standard-now", "bbox": [222, 183, 463, 196]},
	{"text": "测试号：2026020917", "bbox": [517, 119, 740, 131]},
	{"text": "身高：155 cm", "bbox": [517, 132, 709, 145]},
	{"text": "体重：60 kg", "bbox": [517, 145, 702, 158]},
	{"text": "备注：", "bbox": [517, 158, 556, 170]},
	{"text": "联系电话：", "bbox": [517, 170, 587, 182]},
	{"text": "操作者：蒋细萍", "bbox": [517, 183, 710, 196]},
	{"text": "CO (%)", "bbox": [798, 204, 835, 216]},
	{"text": "Volume (L)", "bbox": [249, 206, 307, 216]},
	{"text": "CH4 [%]", "bbox": [249, 216, 296, 226]},
	{"text": "-0.25", "bbox": [250, 233, 278, 243]},
	{"text": "-0.20", "bbox": [250, 264, 278, 274]},
	{"text": "-0.15", "bbox": [250, 295, 278, 305]},
	{"text": "-0.10", "bbox": [250, 327, 278, 337]},
	{"text": "-0.05", "bbox": [250, 359, 278, 369]},
	{"text": "0", "bbox": [235, 384, 250, 394]},
	{"text": "5", "bbox": [343, 400, 354, 410]},
	{"text": "10", "bbox": [441, 400, 456, 410]},
	{"text": "15", "bbox": [539, 400, 554, 410]},
	{"text": "20", "bbox": [637, 400, 652, 410]},
	{"text": "25", "bbox": [735, 400, 750, 410]},
	{"text": "30", "bbox": [833, 400, 850, 410]},
	{"text": "Time [s]", "bbox": [523, 383, 567, 393]},
	{"text": "Pred", "bbox": [454, 413, 502, 424]},
	{"text": "Best", "bbox": [534, 413, 580, 424]},
	{"text": "Best%", "bbox": [602, 413, 660, 424]},
	{"text": "Act1", "bbox": [693, 413, 740, 424]},
	{"text": "DLCO SB", "bbox": [116, 444, 199, 456]},
	{"text": "[mmol/min/kPa]", "bbox": [260, 444, 417, 456]},
	{"text": "8.08", "bbox": [455, 444, 500, 456]},
	{"text": "9.45", "bbox": [536, 444, 580, 456]},
	{"text": "116.9", "bbox": [604, 444, 660, 456]},
	{"text": "9.45", "bbox": [696, 444, 740, 456]},
	{"text": "DLCO/VA", "bbox": [116, 460, 199, 472]},
	{"text": "[mmol/min/kPa/L]", "bbox": [236, 460, 417, 472]},
	{"text": "1.82", "bbox": [455, 460, 500, 472]},
	{"text": "2.38", "bbox": [536, 460, 580, 472]},
	{"text": "130.8", "bbox": [604, 460, 660, 472]},
	{"text": "2.38", "bbox": [696, 460, 740, 472]},
	{"text": "VA", "bbox": [116, 476, 141, 488]},
	{"text": "[L]", "bbox": [387, 476, 417, 488]},
	{"text": "4.29", "bbox": [455, 476, 500, 488]},
	{"text": "3.97", "bbox": [536, 476, 580, 488]},
	{"text": "92.5", "bbox": [615, 476, 660, 488]},
	{"text": "3.97", "bbox": [696, 476, 740, 488]},
	{"text": "VC IN", "bbox": [116, 492, 176, 504]},
	{"text": "[L]", "bbox": [387, 492, 417, 504]},
	{"text": "3.03", "bbox": [455, 492, 500, 504]},
	{"text": "2.26", "bbox": [536, 492, 580, 504]},
	{"text": "74.6", "bbox": [615, 492, 660, 504]},
	{"text": "Discard vol", "bbox": [116, 508, 245, 520]},
	{"text": "[L]", "bbox": [387, 508, 417, 520]},
	{"text": "1.00", "bbox": [696, 508, 740, 520]},
	{"text": "Sample vol", "bbox": [116, 524, 234, 536]},
	{"text": "[L]", "bbox": [387, 524, 417, 536]},
	{"text": "0.53", "bbox": [696, 524, 740, 536]},
	{"text": "ERV", "bbox": [116, 557, 153, 569]},
	{"text": "[L]", "bbox": [387, 557, 417, 569]},
	{"text": "1.10", "bbox": [455, 557, 500, 569]},
	{"text": "IRV", "bbox": [116, 573, 153, 585]},
	{"text": "[L]", "bbox": [387, 573, 417, 585]},
	{"text": "IC", "bbox": [116, 589, 141, 601]},
	{"text": "[L]", "bbox": [387, 589, 417, 601]},
	{"text": "1.93", "bbox": [455, 589, 500, 601]},
	{"text": "VT", "bbox": [116, 605, 141, 617]},
	{"text": "[L]", "bbox": [387, 605, 417, 617]},
	{"text": "0.43", "bbox": [455, 605, 500, 617]},
	{"text": "VC MAX", "bbox": [116, 621, 189, 633]},
	{"text": "[L]", "bbox": [387, 621, 417, 633]},
	{"text": "3.03", "bbox": [455, 621, 500, 633]},
	{"text": "2.26", "bbox": [536, 621, 580, 633]},
	{"text": "74.6", "bbox": [615, 621, 660, 633]},
	{"text": "TLC-SB", "bbox": [116, 638, 187, 650]},
	{"text": "[L]", "bbox": [387, 638, 417, 650]},
	{"text": "4.44", "bbox": [455, 638, 500, 650]},
	{"text": "4.10", "bbox": [536, 638, 580, 650]},
	{"text": "92.4", "bbox": [615, 638, 660, 650]},
	{"text": "4.10", "bbox": [696, 638, 740, 650]},
	{"text": "RV-SB", "bbox": [116, 654, 176, 666]},
	{"text": "[L]", "bbox": [387, 654, 417, 666]},
	{"text": "1.41", "bbox": [455, 654, 500, 666]},
	{"text": "2.18", "bbox": [536, 654, 580, 666]},
	{"text": "154.5", "bbox": [604, 654, 660, 666]},
	{"text": "2.18", "bbox": [696, 654, 740, 666]},
	{"text": "RV%TLC-SB", "bbox": [116, 670, 222, 682]},
	{"text": "[%]", "bbox": [387, 670, 417, 682]},
	{"text": "31.88", "bbox": [444, 670, 500, 682]},
	{"text": "53.26", "bbox": [524, 670, 580, 682]},
	{"text": "167.1", "bbox": [604, 670, 660, 682]},
	{"text": "53.26", "bbox": [685, 670, 740, 682]},
	{"text": "FRC-SB", "bbox": [116, 687, 187, 699]},
	{"text": "[L]", "bbox": [387, 687, 417, 699]},
	{"text": "2.51", "bbox": [455, 687, 500, 699]},
	{"text": "2.39", "bbox": [536, 687, 580, 699]},
	{"text": "95.2", "bbox": [615, 687, 660, 699]},
	{"text": "2.39", "bbox": [696, 687, 740, 699]},
	{"text": "FRC%TLC-SB", "bbox": [116, 703, 234, 715]},
	{"text": "[%]", "bbox": [387, 703, 417, 715]},
	{"text": "51.18", "bbox": [444, 703, 500, 715]},
	{"text": "58.28", "bbox": [524, 703, 580, 715]},
	{"text": "113.9", "bbox": [604, 703, 660, 715]},
	{"text": "58.28", "bbox": [685, 703, 740, 715]},
	{"text": "测试日期", "bbox": [116, 735, 210, 750]},
	{"text": "26/2/0", "bbox": [513, 737, 580, 749]},
	{"text": "意见：", "bbox": [116, 752, 173, 767]},
	{"text": "1.弥散功能在正常范围。", "bbox": [140, 771, 345, 784]},
	{"text": "2.残气量、残总比增高，肺总量在正常范围。", "bbox": [140, 784, 518, 797]}
]
2026-08-05 12:00:13,156 INFO     29 [qwen-vl-text] coord API: raw_items=113, valid_items=113, elapsed=30.4s
2026-08-05 12:00:13,156 INFO     29 [qwen-vl-text] coord item[0]: text=一口气法弥散功能报告, bbox=[417, 91, 678, 107]
2026-08-05 12:00:13,156 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[222, 119, 261, 131]
2026-08-05 12:00:13,156 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：38岁, bbox=[222, 132, 405, 145]
2026-08-05 12:00:13,156 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女, bbox=[222, 145, 382, 158]
2026-08-05 12:00:13,156 INFO     29 [qwen-vl-text] coord item[4]: text=科别：, bbox=[222, 158, 261, 170]
2026-08-05 12:00:13,156 INFO     29 [qwen-vl-text] coord item[5]: text=保险：, bbox=[222, 170, 261, 182]
2026-08-05 12:00:13,156 INFO     29 [qwen-vl-text] coord item[6]: text=预计值模式：Standard-now, bbox=[222, 183, 463, 196]
2026-08-05 12:00:13,156 INFO     29 [qwen-vl-text] coord item[7]: text=测试号：2026020917, bbox=[517, 119, 740, 131]
2026-08-05 12:00:13,156 INFO     29 [qwen-vl-text] coord item[8]: text=身高：155 cm, bbox=[517, 132, 709, 145]
2026-08-05 12:00:13,156 INFO     29 [qwen-vl-text] coord item[9]: text=体重：60 kg, bbox=[517, 145, 702, 158]
2026-08-05 12:00:13,156 INFO     29 [qwen-vl-text] coord item[10]: text=备注：, bbox=[517, 158, 556, 170]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[11]: text=联系电话：, bbox=[517, 170, 587, 182]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[12]: text=操作者：蒋细萍, bbox=[517, 183, 710, 196]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[13]: text=CO (%), bbox=[798, 204, 835, 216]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[14]: text=Volume (L), bbox=[249, 206, 307, 216]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[15]: text=CH4 [%], bbox=[249, 216, 296, 226]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[16]: text=-0.25, bbox=[250, 233, 278, 243]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[17]: text=-0.20, bbox=[250, 264, 278, 274]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[18]: text=-0.15, bbox=[250, 295, 278, 305]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[19]: text=-0.10, bbox=[250, 327, 278, 337]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[20]: text=-0.05, bbox=[250, 359, 278, 369]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[21]: text=0, bbox=[235, 384, 250, 394]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[22]: text=5, bbox=[343, 400, 354, 410]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[23]: text=10, bbox=[441, 400, 456, 410]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[24]: text=15, bbox=[539, 400, 554, 410]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[25]: text=20, bbox=[637, 400, 652, 410]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[26]: text=25, bbox=[735, 400, 750, 410]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[27]: text=30, bbox=[833, 400, 850, 410]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[28]: text=Time [s], bbox=[523, 383, 567, 393]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[29]: text=Pred, bbox=[454, 413, 502, 424]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[30]: text=Best, bbox=[534, 413, 580, 424]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[31]: text=Best%, bbox=[602, 413, 660, 424]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[32]: text=Act1, bbox=[693, 413, 740, 424]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[33]: text=DLCO SB, bbox=[116, 444, 199, 456]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[34]: text=[mmol/min/kPa], bbox=[260, 444, 417, 456]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[35]: text=8.08, bbox=[455, 444, 500, 456]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[36]: text=9.45, bbox=[536, 444, 580, 456]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[37]: text=116.9, bbox=[604, 444, 660, 456]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[38]: text=9.45, bbox=[696, 444, 740, 456]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[39]: text=DLCO/VA, bbox=[116, 460, 199, 472]
2026-08-05 12:00:13,157 INFO     29 [qwen-vl-text] coord item[40]: text=[mmol/min/kPa/L], bbox=[236, 460, 417, 472]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[41]: text=1.82, bbox=[455, 460, 500, 472]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[42]: text=2.38, bbox=[536, 460, 580, 472]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[43]: text=130.8, bbox=[604, 460, 660, 472]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[44]: text=2.38, bbox=[696, 460, 740, 472]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[45]: text=VA, bbox=[116, 476, 141, 488]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[46]: text=[L], bbox=[387, 476, 417, 488]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[47]: text=4.29, bbox=[455, 476, 500, 488]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[48]: text=3.97, bbox=[536, 476, 580, 488]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[49]: text=92.5, bbox=[615, 476, 660, 488]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[50]: text=3.97, bbox=[696, 476, 740, 488]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[51]: text=VC IN, bbox=[116, 492, 176, 504]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[52]: text=[L], bbox=[387, 492, 417, 504]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[53]: text=3.03, bbox=[455, 492, 500, 504]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[54]: text=2.26, bbox=[536, 492, 580, 504]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[55]: text=74.6, bbox=[615, 492, 660, 504]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[56]: text=Discard vol, bbox=[116, 508, 245, 520]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[57]: text=[L], bbox=[387, 508, 417, 520]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[58]: text=1.00, bbox=[696, 508, 740, 520]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[59]: text=Sample vol, bbox=[116, 524, 234, 536]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[60]: text=[L], bbox=[387, 524, 417, 536]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[61]: text=0.53, bbox=[696, 524, 740, 536]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[62]: text=ERV, bbox=[116, 557, 153, 569]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[63]: text=[L], bbox=[387, 557, 417, 569]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[64]: text=1.10, bbox=[455, 557, 500, 569]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[65]: text=IRV, bbox=[116, 573, 153, 585]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[66]: text=[L], bbox=[387, 573, 417, 585]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[67]: text=IC, bbox=[116, 589, 141, 601]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[68]: text=[L], bbox=[387, 589, 417, 601]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[69]: text=1.93, bbox=[455, 589, 500, 601]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[70]: text=VT, bbox=[116, 605, 141, 617]
2026-08-05 12:00:13,158 INFO     29 [qwen-vl-text] coord item[71]: text=[L], bbox=[387, 605, 417, 617]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[72]: text=0.43, bbox=[455, 605, 500, 617]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[73]: text=VC MAX, bbox=[116, 621, 189, 633]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[74]: text=[L], bbox=[387, 621, 417, 633]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[75]: text=3.03, bbox=[455, 621, 500, 633]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[76]: text=2.26, bbox=[536, 621, 580, 633]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[77]: text=74.6, bbox=[615, 621, 660, 633]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[78]: text=TLC-SB, bbox=[116, 638, 187, 650]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[79]: text=[L], bbox=[387, 638, 417, 650]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[80]: text=4.44, bbox=[455, 638, 500, 650]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[81]: text=4.10, bbox=[536, 638, 580, 650]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[82]: text=92.4, bbox=[615, 638, 660, 650]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[83]: text=4.10, bbox=[696, 638, 740, 650]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[84]: text=RV-SB, bbox=[116, 654, 176, 666]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[85]: text=[L], bbox=[387, 654, 417, 666]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[86]: text=1.41, bbox=[455, 654, 500, 666]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[87]: text=2.18, bbox=[536, 654, 580, 666]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[88]: text=154.5, bbox=[604, 654, 660, 666]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[89]: text=2.18, bbox=[696, 654, 740, 666]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[90]: text=RV%TLC-SB, bbox=[116, 670, 222, 682]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[91]: text=[%], bbox=[387, 670, 417, 682]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[92]: text=31.88, bbox=[444, 670, 500, 682]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[93]: text=53.26, bbox=[524, 670, 580, 682]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[94]: text=167.1, bbox=[604, 670, 660, 682]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[95]: text=53.26, bbox=[685, 670, 740, 682]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[96]: text=FRC-SB, bbox=[116, 687, 187, 699]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[97]: text=[L], bbox=[387, 687, 417, 699]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[98]: text=2.51, bbox=[455, 687, 500, 699]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[99]: text=2.39, bbox=[536, 687, 580, 699]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[100]: text=95.2, bbox=[615, 687, 660, 699]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[101]: text=2.39, bbox=[696, 687, 740, 699]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[102]: text=FRC%TLC-SB, bbox=[116, 703, 234, 715]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[103]: text=[%], bbox=[387, 703, 417, 715]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[104]: text=51.18, bbox=[444, 703, 500, 715]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[105]: text=58.28, bbox=[524, 703, 580, 715]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[106]: text=113.9, bbox=[604, 703, 660, 715]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[107]: text=58.28, bbox=[685, 703, 740, 715]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[108]: text=测试日期, bbox=[116, 735, 210, 750]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[109]: text=26/2/0, bbox=[513, 737, 580, 749]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[110]: text=意见：, bbox=[116, 752, 173, 767]
2026-08-05 12:00:13,159 INFO     29 [qwen-vl-text] coord item[111]: text=1.弥散功能在正常范围。, bbox=[140, 771, 345, 784]
2026-08-05 12:00:13,160 INFO     29 [qwen-vl-text] coord item[112]: text=2.残气量、残总比增高，肺总量在正常范围。, bbox=[140, 784, 518, 797]
2026-08-05 12:00:13,160 INFO     29 [qwen-vl-text] page=16 — 113/113 coords, api_time=30.4s
2026-08-05 12:00:13,160 INFO     29 [qwen-vl-text] new_positions (116):
[[15, 104.72, 323.68, 701.386, 714.016], [15, 104.72, 176.715, 718.226, 730.014], [15, 427.21, 467.66999999999996, 732.54, 755.274], [16, 248.11499999999998, 403.40999999999997, 76.622, 90.094], [16, 132.09, 155.295, 100.198, 110.30199999999999], [16, 132.09, 240.975, 111.14399999999999, 122.08999999999999], [16, 132.09, 227.29, 122.08999999999999, 133.036], [16, 132.09, 155.295, 133.036, 143.14], [16, 132.09, 155.295, 143.14, 153.244], [16, 132.09, 275.485, 154.08599999999998, 165.03199999999998], [16, 307.615, 440.29999999999995, 100.198, 110.30199999999999], [16, 307.615, 421.85499999999996, 111.14399999999999, 122.08999999999999], [16, 307.615, 417.69, 122.08999999999999, 133.036], [16, 307.615, 330.82, 133.036, 143.14], [16, 307.615, 349.265, 143.14, 153.244], [16, 307.615, 422.45, 154.08599999999998, 165.03199999999998], [16, 474.81, 496.825, 171.768, 181.87199999999999], [16, 148.155, 182.665, 173.452, 181.87199999999999], [16, 148.155, 176.12, 181.87199999999999, 190.292], [16, 148.75, 165.41, 196.186, 204.606], [16, 148.75, 165.41, 222.28799999999998, 230.708], [16, 148.75, 165.41, 248.39, 256.81], [16, 148.75, 165.41, 275.334, 283.75399999999996], [16, 148.75, 165.41, 302.27799999999996, 310.698], [16, 139.825, 148.75, 323.328, 331.748], [16, 204.08499999999998, 210.63, 336.8, 345.21999999999997], [16, 262.395, 271.32, 336.8, 345.21999999999997], [16, 320.705, 329.63, 336.8, 345.21999999999997], [16, 379.015, 387.94, 336.8, 345.21999999999997], [16, 437.325, 446.25, 336.8, 345.21999999999997], [16, 495.635, 505.75, 336.8, 345.21999999999997], [16, 311.185, 337.365, 322.486, 330.906], [16, 270.13, 298.69, 347.746, 357.008], [16, 317.72999999999996, 345.09999999999997, 347.746, 357.008], [16, 358.19, 392.7, 347.746, 357.008], [16, 412.335, 440.29999999999995, 347.746, 357.008], [16, 69.02, 118.405, 373.848, 383.952], [16, 154.7, 248.11499999999998, 373.848, 383.952], [16, 270.72499999999997, 297.5, 373.848, 383.952], [16, 318.91999999999996, 345.09999999999997, 373.848, 383.952], [16, 359.38, 392.7, 373.848, 383.952], [16, 414.12, 440.29999999999995, 373.848, 383.952], [16, 69.02, 118.405, 387.32, 397.424], [16, 140.42, 248.11499999999998, 387.32, 397.424], [16, 270.72499999999997, 297.5, 387.32, 397.424], [16, 318.91999999999996, 345.09999999999997, 387.32, 397.424], [16, 359.38, 392.7, 387.32, 397.424], [16, 414.12, 440.29999999999995, 387.32, 397.424], [16, 69.02, 83.895, 400.792, 410.89599999999996], [16, 230.265, 248.11499999999998, 400.792, 410.89599999999996], [16, 270.72499999999997, 297.5, 400.792, 410.89599999999996], [16, 318.91999999999996, 345.09999999999997, 400.792, 410.89599999999996], [16, 365.925, 392.7, 400.792, 410.89599999999996], [16, 414.12, 440.29999999999995, 400.792, 410.89599999999996], [16, 69.02, 104.72, 414.264, 424.368], [16, 230.265, 248.11499999999998, 414.264, 424.368], [16, 270.72499999999997, 297.5, 414.264, 424.368], [16, 318.91999999999996, 345.09999999999997, 414.264, 424.368], [16, 365.925, 392.7, 414.264, 424.368], [16, 69.02, 145.775, 427.736, 437.84], [16, 230.265, 248.11499999999998, 427.736, 437.84], [16, 414.12, 440.29999999999995, 427.736, 437.84], [16, 69.02, 139.23, 441.20799999999997, 451.312], [16, 230.265, 248.11499999999998, 441.20799999999997, 451.312], [16, 414.12, 440.29999999999995, 441.20799999999997, 451.312], [16, 69.02, 91.035, 468.99399999999997, 479.09799999999996], [16, 230.265, 248.11499999999998, 468.99399999999997, 479.09799999999996], [16, 270.72499999999997, 297.5, 468.99399999999997, 479.09799999999996], [16, 69.02, 91.035, 482.466, 492.57], [16, 230.265, 248.11499999999998, 482.466, 492.57], [16, 69.02, 83.895, 495.938, 506.042], [16, 230.265, 248.11499999999998, 495.938, 506.042], [16, 270.72499999999997, 297.5, 495.938, 506.042], [16, 69.02, 83.895, 509.40999999999997, 519.514], [16, 230.265, 248.11499999999998, 509.40999999999997, 519.514], [16, 270.72499999999997, 297.5, 509.40999999999997, 519.514], [16, 69.02, 112.455, 522.882, 532.986], [16, 230.265, 248.11499999999998, 522.882, 532.986], [16, 270.72499999999997, 297.5, 522.882, 532.986], [16, 318.91999999999996, 345.09999999999997, 522.882, 532.986], [16, 365.925, 392.7, 522.882, 532.986], [16, 69.02, 111.265, 537.196, 547.3], [16, 230.265, 248.11499999999998, 537.196, 547.3], [16, 270.72499999999997, 297.5, 537.196, 547.3], [16, 318.91999999999996, 345.09999999999997, 537.196, 547.3], [16, 365.925, 392.7, 537.196, 547.3], [16, 414.12, 440.29999999999995, 537.196, 547.3], [16, 69.02, 104.72, 550.668, 560.7719999999999], [16, 230.265, 248.11499999999998, 550.668, 560.7719999999999], [16, 270.72499999999997, 297.5, 550.668, 560.7719999999999], [16, 318.91999999999996, 345.09999999999997, 550.668, 560.7719999999999], [16, 359.38, 392.7, 550.668, 560.7719999999999], [16, 414.12, 440.29999999999995, 550.668, 560.7719999999999], [16, 69.02, 132.09, 564.14, 574.244], [16, 230.265, 248.11499999999998, 564.14, 574.244], [16, 264.18, 297.5, 564.14, 574.244], [16, 311.78, 345.09999999999997, 564.14, 574.244], [16, 359.38, 392.7, 564.14, 574.244], [16, 407.575, 440.29999999999995, 564.14, 574.244], [16, 69.02, 111.265, 578.454, 588.558], [16, 230.265, 248.11499999999998, 578.454, 588.558], [16, 270.72499999999997, 297.5, 578.454, 588.558], [16, 318.91999999999996, 345.09999999999997, 578.454, 588.558], [16, 365.925, 392.7, 578.454, 588.558], [16, 414.12, 440.29999999999995, 578.454, 588.558], [16, 69.02, 139.23, 591.9259999999999, 602.03], [16, 230.265, 248.11499999999998, 591.9259999999999, 602.03], [16, 264.18, 297.5, 591.9259999999999, 602.03], [16, 311.78, 345.09999999999997, 591.9259999999999, 602.03], [16, 359.38, 392.7, 591.9259999999999, 602.03], [16, 407.575, 440.29999999999995, 591.9259999999999, 602.03], [16, 69.02, 124.94999999999999, 618.87, 631.5], [16, 305.235, 345.09999999999997, 620.554, 630.658], [16, 69.02, 102.935, 633.184, 645.814], [16, 83.3, 205.27499999999998, 649.182, 660.1279999999999], [16, 83.3, 308.21, 660.1279999999999, 671.074]]
2026-08-05 12:00:13,160 INFO     29 [qwen-vl-text] ═══ DONE ═══ 116 positions, pages=2, time=56.7s
2026-08-05 12:00:13,160 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 12:00:13,160 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-05 12:00:13,161 INFO     29 [qwen-vl-text] positions(255): [[16, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 12:00:13,161 INFO     29 [qwen-vl-text] page grouping: [16, 17], lines per page: [1, 254]
2026-08-05 12:00:13,360 INFO     29 [qwen-vl-text] page=16, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 12:00:13,550 INFO     29 [qwen-vl-text] page=17, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 12:00:13,552 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1460
2026-08-05 12:00:13,552 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 12:00:13,552 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 5399, \"bbox_end\": 5653, \"encounter_dates\": [\"2026-02-09\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "张\n肺功能试验报告\n姓名：\n年龄：38岁\n性别：女\n科别：\n保险：\n预计值模式：Standard-new\n测试号：2026020017\n身高：166 cm\n体重：60 kg\n备注：\n联系电话：\n操作者：蒋细萍\nPred\nA1 A1/Pd\nP1 A2/Pd\nchg%l\nP2 A3/Pd\nchg%2\nP3 A4/Pd\nchg%3\nFVC\n[L]\n2.99\n2.21\n74.0\n2.63\n87.9\n18.72\n2.04\n88.2\n19.17\n2.67\n86.0\n16.23\nFEV 1\n[L]\n2.67\n1.25\n48.6\n1.62\n69.2\n21.85\n1.84\n69.8\n23.23\n1.60\n68.4\n20.23\nFEV 1 % FVC\n[%]\n84.19\n56.48\n67.1\n67.97\n68.9\n2.64\n68.40\n69.4\n3.41\n68.42\n69.4\n3.44\nFEV 1 % VC MAX\n[%]\n81.88\n65.26\n67.6\n67.97\n70.8\n4.91\n68.40\n71.3\n6.70\n68.42\n71.4\n5.73\nVC MAX\n[L]\n3.03\n2.26\n74.6\n2.63\n86.6\n16.14\n2.64\n87.0\n16.69\n2.57\n84.8\n13.71\nPEF\n[L/s]\n6.28\n2.66\n42.4\n2.90\n46.2\n9.17\n3.37\n53.7\n26.79\n3.42\n64.6\n28.64\nMMEF 75/25\n[L/s]\n3.57\n0.61\n14.4\n0.67\n18.8\n31.03\n0.73\n20.4\n42.01\n0.69\n19.4\n35.02\nMEF 50\n[L/s]\n4.01\n0.68\n17.0\n0.90\n22.5\n32.75\n0.89\n22.1\n30.15\n0.88\n21.9\n29.17\nMEF 25\n[L/s]\n1.79\n0.19\n10.5\n0.27\n15.2\n44.16\n0.33\n18.7\n77.66\n0.31\n17.6\n66.49\nFET\n[s]\n7.63\n8.01\n4.99\n7.79\n2.14\n7.43\n-2.60\nV backextrapolation ex [L]\n0.05\n0.04\n-11.67\n0.04\n-18.64\n0.04\n-13.51\nPIF\n[L/s]\n3.04\n3.37\n10.91\n3.51\n15.70\n3.60\n18.67\nFIV1\n[L]\n2.21\n2.56\n15.71\n2.56\n15.66\n2.50\n13.09\nPEF50 % FIF50\n[%]\n22.86\n28.15\n23.14\n25.36\n10.95\n27.28\n19.33\nMVV\n[L/min]\n99.77\n46.21\n46.3\nBF MVV\n[1/min]\n75.55\n10\nFlow [L/s]\nF/V ex\n1\n2\n3\n4\n6\n4\n2\n0\nVol [L]\n1\n2\n3\n4\n5\n2\n4\n6\n8\n10\nF/V In\nVol%VCmax\n0\n0\nVol [L]\n20\n40\n60\n80\n100\n1\n2\nVCmax\n3\n4\n5\n6\nTime [s]\n0\n2\n4\n6\n8\n10\n12\n14\n意见：\n1. 中重度阻塞性肺通气功能障碍。\n2. 支气管舒张试验阳性。\n(1. 24h内无支气管舒张药物使用史)\n(2. 吸入万托林气雾剂400ug15分钟后，FEV1和FVC上升≥12%，绝对值增加≥200ml)\n(3. 检查质量：舒张前：A级；舒张后：A级)\n张四彩",
    "role": "user"
  }
]
[92m12:00:13 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:00:13,554 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:00:13,560 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 12:00:13,560 INFO     29 [qwen-vl-text] LLM output (len=2305):
{
  "encounter_date": "2025-05-26",
  "dm_name": "胡金超",
  "dm_gender": "男",
  "dm_age": 46,
  "dm_ethnicity": "汉族",
  "dm_marital_status": "未婚",
  "dm_occupation": "自由职业者",
  "dm_admission_time": "2025-05-26 08:34",
  "dm_record_time": "2025-05-26 09:31",
  "dm_history_provider": "本人",
  "cc_text": "反复胸闷气喘20余年，再发2天。",
  "cc_main_symptoms": [
    "胸闷",
    "气喘"
  ],
  "cc_duration": "20余年，再发2天",
  "pi_text": "患者20余年前无明显诱因下开始出现胸闷气喘不适，休息后缓解，少许咳嗽，无明显咳痰，无畏寒寒战，无胸痛等不适。在当地医院按“支气管哮喘”给予抗感染、平喘等治疗后症状缓解。此后每因受凉上述症状反复发作，现长期予“信必可160”改善症状。2天前，患者受凉后再次出现胸闷、气喘，活动后加重，休息可缓解，伴咳嗽咳痰，呈阵发性，咳少许黄白粘痰，质粘，不易咳出，无发热，无盗汗消瘦，无畏寒寒战，无胸痛，无咯血，无腹痛腹泻等不适。现为进一步诊治，来我院就诊，拟“支气管哮喘”收住我科。患者起病以来，神志清，精神稍软，胃纳、睡眠一般，二便无明显异常，体重近期无增减。",
  "pmh_disease_history": [
    "脂肪肝"
  ],
  "pmh_allergy_history": [
    "头孢克洛"
  ],
  "pmh_surgery_trauma_history": [],
  "ph_smoking": "无",
  "ph_drinking": "无",
  "oh_menarche_age": null,
  "oh_menopause_age": null,
  "oh_pregnancies": null,
  "fh_text": "父亲[体健]，母亲[体健]，1兄弟姐妹[体健]，直系亲属[无]类似疾病项。患者[否认]二系三代有遗传病史。患者[否认]有遗传倾向的疾病。",
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36.8,
  "vs_pulse_bpm": 87,
  "vs_respiration_rpm": 19,
  "vs_systolic_bp_mmhg": 157,
  "vs_diastolic_bp_mmhg": 87,
  "pe_general_condition": "意识[清楚]，[自主体位]，[急性面容]，查体[合作]，身高：[167.5]cm，体重：[83.8]kg,BMI指数：[29.9]。",
  "pe_skin_mucosa": "[皮肤粘膜无黄染]，[无水肿]，[无]。",
  "pe_lymph_nodes": "[全身浅表淋巴结无肿大]。",
  "pe_lungs": "呼吸运动[两侧对称]。叩诊[清音]，双肺闻及哮鸣音。",
  "pe_heart": "心率[87]次/分，律[齐]，心音[有力]，[未闻及病理性杂音]。",
  "pe_abdomen": "腹[平坦]，对称，无胃肠型和蠕动波，腹部[柔软]，无[压痛，反跳痛]，腹部[无包块]。肝脾肾[未触及]。肾区[无叩击痛]。肠鸣音[4]次/分,移动性浊音[阴性]。",
  "pe_extremities": null,
  "pe_nervous_system": "肌张力无增高或降低，四肢肌力[V级]，双侧膝腱反射[++]，[双侧]Babinski征[阴性]。",
  "pe_specialist_exam": "一般情况：[无]发绀，[无]鼻翼扇动，[无]端坐呼吸，气管[居中]，浅表颈静脉[无怒张]，肝颈静脉返流征[阴性]，[无]皮疹结节，[无]皮下气肿，[无]浮肿，[无]皮下瘀点、瘀斑，[无]无杵状指（趾）；胸部：胸廓[无畸形]，肋间隙[无增宽或缩窄]，局部[无殊]，胸壁浅表静脉[无]曲张，脊柱[无畸形]，呼吸动度[对称]，[无]胸壁压痛；肺部 视诊：[胸式]呼吸为主，呼吸频率[19]次/分，节律[规律]，呼吸运动[对称]，[无]呼吸困难；触诊：语颤[对称]，[无]胸膜摩擦感，[无]皮下捻发感；叩诊：[清音]。听诊：两肺[呼吸音粗]，可闻及哮鸣音，[无]呼气延长，语音传导[对称]，[无]胸膜摩擦音；",
  "pe_ecog_score": null,
  "pat_text": "[本次暂缺。]",
  "pat_items": [],
  "preliminary_diagnoses": [
    {
      "name": "支气管哮喘",
      "diagnosis_type": "西医",
      "is_primary": true
    },
    {
      "name": "脂肪肝",
      "diagnosis_type": "西医",
      "is_primary": false
    }
  ],
  "department": "呼吸与危重症医学科病房"
}
2026-08-05 12:00:13,560 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-05-26]
2026-08-05 12:00:13,561 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=833196, prompt_len=1485
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共68行）
["浏览", "病案首页 x", "刷新", "关闭文", "留痕记录", "编辑", "打印", "预览", "•基本信息 •出院诊断 •病理诊断 •其他信息 •医务工 作 •手术及操作记录 •出院情况 •费用 •住院首页附页内容", "基本信息", "医疗付费方式 城镇职工基本医疗保险", "健康卡号 -", "住院次数 1", "病案号", "姓名", "性别 男", "证件号 居民身份证", "出生日期 1978年12月13日", "33260219;", "年龄 46岁", "(年龄不足一周岁)年龄 -", "新生儿出生体重(g) 克", "新生儿入院体重(g) 克", "国籍 中国", "民族 汉族", "职业 自由职业者", "0", "出生地 中国浙江省台州市临海市", "籍贯 浙江省台州市临海市", "现住址 中国浙江省台州市临海市", "村", "邮政编码 317000", "户籍地址 中国浙江省台州市临海市.", ".村", "邮政编码 317000", "婚姻 未婚", "本人电话 1", "3", "工作单位 石鼓村", "工作单位电话 3", "单位地址 中国浙江省台州市临海市石鼓村", "邮政编码 317000", "联系人姓名", "关系 兄、弟、姐、妹", "电话", "联系人地址 浙江省", "水丰", "镇石鼓", "入院途径 门诊", "入院情况 一般", "0", "0", "入院情况：1.有，2.临床未确定，3.情况不明，4.无", "门(急)诊诊断 支气管哮喘", "入院初诊 支气管哮喘", "入院诊断编码 J45.900x001", "疾病编码 J45.900x001", "入院时间 2025-05-26 08:34", "入院科别 呼吸与危重症医学科病房", "入院病区 七病区", "0", "0", "转科科别 -", "出院时间 2025-05-31 10:46", "出院科别 呼吸与危重症医学科病房", "出院病区 七病区", "实际住院天数 5天", "0"]

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
2026-08-05 12:00:32,950 INFO     29 [qwen-vl-text] coord API raw response (len=3651):
[
	{"text": "浏览", "bbox": [40, 309, 59, 320]},
	{"text": "病案首页 x", "bbox": [93, 310, 155, 320]},
	{"text": "刷新", "bbox": [875, 307, 903, 318]},
	{"text": "关闭文", "bbox": [924, 308, 957, 318]},
	{"text": "留痕记录", "bbox": [754, 333, 798, 344]},
	{"text": "编辑", "bbox": [823, 333, 850, 344]},
	{"text": "打印", "bbox": [874, 333, 900, 344]},
	{"text": "预览", "bbox": [924, 333, 953, 344]},
	{"text": "•基本信息 •出院诊断 •病理诊断 •其他信息 •医务工 作 •手术及操作记录 •出院情况 •费用 •住院首页附页内容", "bbox": [204, 359, 774, 369]},
	{"text": "基本信息", "bbox": [47, 384, 90, 394]},
	{"text": "医疗付费方式 城镇职工基本医疗保险", "bbox": [68, 406, 247, 416]},
	{"text": "健康卡号 -", "bbox": [303, 406, 362, 416]},
	{"text": "住院次数 1", "bbox": [522, 406, 567, 416]},
	{"text": "病案号", "bbox": [751, 406, 784, 416]},
	{"text": "姓名", "bbox": [110, 422, 132, 432]},
	{"text": "性别 男", "bbox": [325, 422, 371, 432]},
	{"text": "证件号 居民身份证", "bbox": [534, 422, 632, 432]},
	{"text": "出生日期 1978年12月13日", "bbox": [741, 422, 874, 432]},
	{"text": "33260219;", "bbox": [579, 438, 630, 447]},
	{"text": "年龄 46岁", "bbox": [112, 453, 166, 463]},
	{"text": "(年龄不足一周岁)年龄 -", "bbox": [276, 453, 378, 463]},
	{"text": "新生儿出生体重(g) 克", "bbox": [495, 453, 607, 463]},
	{"text": "新生儿入院体重(g) 克", "bbox": [712, 453, 822, 463]},
	{"text": "国籍 中国", "bbox": [112, 468, 166, 478]},
	{"text": "民族 汉族", "bbox": [327, 468, 383, 478]},
	{"text": "职业 自由职业者", "bbox": [545, 468, 631, 478]},
	{"text": "0", "bbox": [777, 468, 785, 478]},
	{"text": "出生地 中国浙江省台州市临海市", "bbox": [103, 483, 260, 493]},
	{"text": "籍贯 浙江省台州市临海市", "bbox": [763, 483, 892, 493]},
	{"text": "现住址 中国浙江省台州市临海市", "bbox": [103, 499, 260, 508]},
	{"text": "村", "bbox": [315, 499, 325, 508]},
	{"text": "邮政编码 317000", "bbox": [741, 499, 832, 508]},
	{"text": "户籍地址 中国浙江省台州市临海市.", "bbox": [93, 514, 264, 523]},
	{"text": ".村", "bbox": [312, 514, 325, 523]},
	{"text": "邮政编码 317000", "bbox": [741, 514, 832, 523]},
	{"text": "婚姻 未婚", "bbox": [114, 529, 168, 539]},
	{"text": "本人电话 1", "bbox": [308, 529, 354, 539]},
	{"text": "3", "bbox": [418, 529, 428, 539]},
	{"text": "工作单位 石鼓村", "bbox": [95, 544, 178, 554]},
	{"text": "工作单位电话 3", "bbox": [288, 544, 352, 554]},
	{"text": "单位地址 中国浙江省台州市临海市石鼓村", "bbox": [95, 560, 295, 570]},
	{"text": "邮政编码 317000", "bbox": [741, 560, 832, 570]},
	{"text": "联系人姓名", "bbox": [87, 575, 136, 585]},
	{"text": "关系 兄、弟、姐、妹", "bbox": [331, 575, 439, 585]},
	{"text": "电话", "bbox": [545, 575, 567, 585]},
	{"text": "联系人地址 浙江省", "bbox": [730, 575, 828, 585]},
	{"text": "水丰", "bbox": [895, 575, 913, 585]},
	{"text": "镇石鼓", "bbox": [797, 591, 828, 600]},
	{"text": "入院途径 门诊", "bbox": [97, 606, 170, 616]},
	{"text": "入院情况 一般", "bbox": [311, 606, 388, 616]},
	{"text": "0", "bbox": [560, 606, 568, 616]},
	{"text": "0", "bbox": [778, 606, 786, 616]},
	{"text": "入院情况：1.有，2.临床未确定，3.情况不明，4.无", "bbox": [81, 621, 311, 631]},
	{"text": "门(急)诊诊断 支气管哮喘", "bbox": [725, 621, 851, 631]},
	{"text": "入院初诊 支气管哮喘", "bbox": [100, 637, 204, 647]},
	{"text": "入院诊断编码 J45.900x001", "bbox": [290, 637, 425, 647]},
	{"text": "疾病编码 J45.900x001", "bbox": [527, 637, 638, 647]},
	{"text": "入院时间 2025-05-26 08:34", "bbox": [743, 637, 882, 647]},
	{"text": "入院科别 呼吸与危重症医学科病房", "bbox": [100, 652, 266, 662]},
	{"text": "入院病区 七病区", "bbox": [312, 652, 400, 662]},
	{"text": "0", "bbox": [561, 652, 569, 662]},
	{"text": "0", "bbox": [778, 652, 786, 662]},
	{"text": "转科科别 -", "bbox": [100, 668, 141, 678]},
	{"text": "出院时间 2025-05-31 10:46", "bbox": [743, 668, 882, 678]},
	{"text": "出院科别 呼吸与危重症医学科病房", "bbox": [100, 683, 268, 693]},
	{"text": "出院病区 七病区", "bbox": [314, 683, 400, 693]},
	{"text": "实际住院天数 5天", "bbox": [507, 683, 601, 693]},
	{"text": "0", "bbox": [778, 683, 786, 693]}
]
2026-08-05 12:00:32,950 INFO     29 [qwen-vl-text] coord API: raw_items=68, valid_items=68, elapsed=19.4s
2026-08-05 12:00:32,950 INFO     29 [qwen-vl-text] coord item[0]: text=浏览, bbox=[40, 309, 59, 320]
2026-08-05 12:00:32,950 INFO     29 [qwen-vl-text] coord item[1]: text=病案首页 x, bbox=[93, 310, 155, 320]
2026-08-05 12:00:32,951 INFO     29 [qwen-vl-text] coord item[2]: text=刷新, bbox=[875, 307, 903, 318]
2026-08-05 12:00:32,951 INFO     29 [qwen-vl-text] coord item[3]: text=关闭文, bbox=[924, 308, 957, 318]
2026-08-05 12:00:32,951 INFO     29 [qwen-vl-text] coord item[4]: text=留痕记录, bbox=[754, 333, 798, 344]
2026-08-05 12:00:32,951 INFO     29 [qwen-vl-text] coord item[5]: text=编辑, bbox=[823, 333, 850, 344]
2026-08-05 12:00:32,951 INFO     29 [qwen-vl-text] coord item[6]: text=打印, bbox=[874, 333, 900, 344]
2026-08-05 12:00:32,951 INFO     29 [qwen-vl-text] coord item[7]: text=预览, bbox=[924, 333, 953, 344]
2026-08-05 12:00:32,951 INFO     29 [qwen-vl-text] coord item[8]: text=•基本信息 •出院诊断 •病理诊断 •其他信息 •医务工 作 •手术及操作记录 •出院情况 •费用 •住院首页附页内容, bbox=[204, 359, 774, 369]
2026-08-05 12:00:32,951 INFO     29 [qwen-vl-text] coord item[9]: text=基本信息, bbox=[47, 384, 90, 394]
2026-08-05 12:00:32,951 INFO     29 [qwen-vl-text] coord item[10]: text=医疗付费方式 城镇职工基本医疗保险, bbox=[68, 406, 247, 416]
2026-08-05 12:00:32,951 INFO     29 [qwen-vl-text] coord item[11]: text=健康卡号 -, bbox=[303, 406, 362, 416]
2026-08-05 12:00:32,951 INFO     29 [qwen-vl-text] coord item[12]: text=住院次数 1, bbox=[522, 406, 567, 416]
2026-08-05 12:00:32,951 INFO     29 [qwen-vl-text] coord item[13]: text=病案号, bbox=[751, 406, 784, 416]
2026-08-05 12:00:32,951 INFO     29 [qwen-vl-text] coord item[14]: text=姓名, bbox=[110, 422, 132, 432]
2026-08-05 12:00:32,951 INFO     29 [qwen-vl-text] coord item[15]: text=性别 男, bbox=[325, 422, 371, 432]
2026-08-05 12:00:32,952 INFO     29 [qwen-vl-text] coord item[16]: text=证件号 居民身份证, bbox=[534, 422, 632, 432]
2026-08-05 12:00:32,952 INFO     29 [qwen-vl-text] coord item[17]: text=出生日期 1978年12月13日, bbox=[741, 422, 874, 432]
2026-08-05 12:00:32,952 INFO     29 [qwen-vl-text] coord item[18]: text=33260219;, bbox=[579, 438, 630, 447]
2026-08-05 12:00:32,952 INFO     29 [qwen-vl-text] coord item[19]: text=年龄 46岁, bbox=[112, 453, 166, 463]
2026-08-05 12:00:32,952 INFO     29 [qwen-vl-text] coord item[20]: text=(年龄不足一周岁)年龄 -, bbox=[276, 453, 378, 463]
2026-08-05 12:00:32,952 INFO     29 [qwen-vl-text] coord item[21]: text=新生儿出生体重(g) 克, bbox=[495, 453, 607, 463]
2026-08-05 12:00:32,952 INFO     29 [qwen-vl-text] coord item[22]: text=新生儿入院体重(g) 克, bbox=[712, 453, 822, 463]
2026-08-05 12:00:32,952 INFO     29 [qwen-vl-text] coord item[23]: text=国籍 中国, bbox=[112, 468, 166, 478]
2026-08-05 12:00:32,952 INFO     29 [qwen-vl-text] coord item[24]: text=民族 汉族, bbox=[327, 468, 383, 478]
2026-08-05 12:00:32,952 INFO     29 [qwen-vl-text] coord item[25]: text=职业 自由职业者, bbox=[545, 468, 631, 478]
2026-08-05 12:00:32,952 INFO     29 [qwen-vl-text] coord item[26]: text=0, bbox=[777, 468, 785, 478]
2026-08-05 12:00:32,953 INFO     29 [qwen-vl-text] coord item[27]: text=出生地 中国浙江省台州市临海市, bbox=[103, 483, 260, 493]
2026-08-05 12:00:32,953 INFO     29 [qwen-vl-text] coord item[28]: text=籍贯 浙江省台州市临海市, bbox=[763, 483, 892, 493]
2026-08-05 12:00:32,953 INFO     29 [qwen-vl-text] coord item[29]: text=现住址 中国浙江省台州市临海市, bbox=[103, 499, 260, 508]
2026-08-05 12:00:32,953 INFO     29 [qwen-vl-text] coord item[30]: text=村, bbox=[315, 499, 325, 508]
2026-08-05 12:00:32,953 INFO     29 [qwen-vl-text] coord item[31]: text=邮政编码 317000, bbox=[741, 499, 832, 508]
2026-08-05 12:00:32,953 INFO     29 [qwen-vl-text] coord item[32]: text=户籍地址 中国浙江省台州市临海市., bbox=[93, 514, 264, 523]
2026-08-05 12:00:32,953 INFO     29 [qwen-vl-text] coord item[33]: text=.村, bbox=[312, 514, 325, 523]
2026-08-05 12:00:32,953 INFO     29 [qwen-vl-text] coord item[34]: text=邮政编码 317000, bbox=[741, 514, 832, 523]
2026-08-05 12:00:32,953 INFO     29 [qwen-vl-text] coord item[35]: text=婚姻 未婚, bbox=[114, 529, 168, 539]
2026-08-05 12:00:32,953 INFO     29 [qwen-vl-text] coord item[36]: text=本人电话 1, bbox=[308, 529, 354, 539]
2026-08-05 12:00:32,953 INFO     29 [qwen-vl-text] coord item[37]: text=3, bbox=[418, 529, 428, 539]
2026-08-05 12:00:32,953 INFO     29 [qwen-vl-text] coord item[38]: text=工作单位 石鼓村, bbox=[95, 544, 178, 554]
2026-08-05 12:00:32,953 INFO     29 [qwen-vl-text] coord item[39]: text=工作单位电话 3, bbox=[288, 544, 352, 554]
2026-08-05 12:00:32,953 INFO     29 [qwen-vl-text] coord item[40]: text=单位地址 中国浙江省台州市临海市石鼓村, bbox=[95, 560, 295, 570]
2026-08-05 12:00:32,953 INFO     29 [qwen-vl-text] coord item[41]: text=邮政编码 317000, bbox=[741, 560, 832, 570]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[42]: text=联系人姓名, bbox=[87, 575, 136, 585]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[43]: text=关系 兄、弟、姐、妹, bbox=[331, 575, 439, 585]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[44]: text=电话, bbox=[545, 575, 567, 585]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[45]: text=联系人地址 浙江省, bbox=[730, 575, 828, 585]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[46]: text=水丰, bbox=[895, 575, 913, 585]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[47]: text=镇石鼓, bbox=[797, 591, 828, 600]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[48]: text=入院途径 门诊, bbox=[97, 606, 170, 616]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[49]: text=入院情况 一般, bbox=[311, 606, 388, 616]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[50]: text=0, bbox=[560, 606, 568, 616]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[51]: text=0, bbox=[778, 606, 786, 616]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[52]: text=入院情况：1.有，2.临床未确定，3.情况不明，4.无, bbox=[81, 621, 311, 631]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[53]: text=门(急)诊诊断 支气管哮喘, bbox=[725, 621, 851, 631]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[54]: text=入院初诊 支气管哮喘, bbox=[100, 637, 204, 647]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[55]: text=入院诊断编码 J45.900x001, bbox=[290, 637, 425, 647]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[56]: text=疾病编码 J45.900x001, bbox=[527, 637, 638, 647]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[57]: text=入院时间 2025-05-26 08:34, bbox=[743, 637, 882, 647]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[58]: text=入院科别 呼吸与危重症医学科病房, bbox=[100, 652, 266, 662]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[59]: text=入院病区 七病区, bbox=[312, 652, 400, 662]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[60]: text=0, bbox=[561, 652, 569, 662]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[61]: text=0, bbox=[778, 652, 786, 662]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[62]: text=转科科别 -, bbox=[100, 668, 141, 678]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[63]: text=出院时间 2025-05-31 10:46, bbox=[743, 668, 882, 678]
2026-08-05 12:00:32,954 INFO     29 [qwen-vl-text] coord item[64]: text=出院科别 呼吸与危重症医学科病房, bbox=[100, 683, 268, 693]
2026-08-05 12:00:32,955 INFO     29 [qwen-vl-text] coord item[65]: text=出院病区 七病区, bbox=[314, 683, 400, 693]
2026-08-05 12:00:32,955 INFO     29 [qwen-vl-text] coord item[66]: text=实际住院天数 5天, bbox=[507, 683, 601, 693]
2026-08-05 12:00:32,955 INFO     29 [qwen-vl-text] coord item[67]: text=0, bbox=[778, 683, 786, 693]
2026-08-05 12:00:32,955 INFO     29 [qwen-vl-text] page=2 — 68/68 coords, api_time=19.4s
2026-08-05 12:00:32,957 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=817664, prompt_len=1461
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共37行）
["住院病历", "姓名：胡金超 病历号：100", "科室名称：呼吸与危重症医学科病房 病区：七病区 床号：0747", "入院记录", "姓名：", "工作单位：石鼓村", "性别：男", "住址：中国浙江省台州市", "年龄：46岁", "出生地：中国浙江省台州市临海市", "婚姻：未婚", "入院日期：2025-05-26 08:34", "民族：汉族", "记录日期：2025-05-26 09:31", "职业：自由职业者", "病史陈述者：本人", "主诉：", "反复胸闷气喘20余年，再发2天。", "现病史：患者20余年前无明显诱因下开始出现胸闷气喘不适，休息后缓解，少许咳嗽，无明显咳痰，无畏", "寒寒战，无胸痛等不适。在当地医院按“支气管哮喘”给予抗感染、平喘等治疗后症状缓解。此后每因受", "凉上述症状反复发作，现长期予“信必可160”改善症状。2天前，患者受凉后再次出现胸闷、气喘，活动", "后加重，休息可缓解，伴咳嗽咳痰，呈阵发性，咳少许黄白粘痰，质粘，不易咳出，无发热，无盗汗消", "瘦，无畏寒寒战，无胸痛，无咯血，无腹痛腹泻等不适。现为进一步诊治，来我院就诊，拟“支气管哮", "喘”收住我科。", "患者起病以来，神志清，精神稍软，胃纳、睡眠一般，二便无明显异常，体重近期无增减。", "既往有“脂肪肝”5年余，具体不详，未规律复查。", "既往史：[否认]内分泌疾病史；[否认]心血管疾病史；[否认]脑血管疾病史；[否认]肾病史；[否认]肝病", "史；[否认]其他重大内科疾病史；[否认]肺结核；[否认]病毒性肝炎；[否认]其他传染病；有“头孢克", "洛”过敏史，服用后表现为胸闷；[否认]食物、其他药物过敏；[否认]外伤史；[否认]手术史；[否认]输", "血史；[否认]中毒史；[否认]长期用药史；[否认]可能成瘾药物。疫苗接种史不详。", "显示", "既往史", "婚育史", "家族史", "生命体征", "生命体征", "110%"]

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
2026-08-05 12:00:46,321 INFO     29 [qwen-vl-text] coord API raw response (len=2368):
[
	{"text": "住院病历", "bbox": [429, 287, 550, 303]},
	{"text": "姓名：胡金超 病历号：100", "bbox": [156, 308, 338, 321]},
	{"text": "科室名称：呼吸与危重症医学科病房 病区：七病区 床号：0747", "bbox": [397, 308, 813, 321]},
	{"text": "入院记录", "bbox": [430, 329, 550, 345]},
	{"text": "姓名：", "bbox": [165, 355, 233, 368]},
	{"text": "工作单位：石鼓村", "bbox": [513, 353, 634, 366]},
	{"text": "性别：男", "bbox": [165, 380, 263, 393]},
	{"text": "住址：中国浙江省台州市", "bbox": [513, 378, 709, 391]},
	{"text": "年龄：46岁", "bbox": [165, 416, 275, 429]},
	{"text": "出生地：中国浙江省台州市临海市", "bbox": [513, 413, 747, 426]},
	{"text": "婚姻：未婚", "bbox": [165, 437, 275, 450]},
	{"text": "入院日期：2025-05-26 08:34", "bbox": [512, 434, 705, 447]},
	{"text": "民族：汉族", "bbox": [165, 458, 275, 471]},
	{"text": "记录日期：2025-05-26 09:31", "bbox": [510, 456, 703, 469]},
	{"text": "职业：自由职业者", "bbox": [165, 479, 317, 492]},
	{"text": "病史陈述者：本人", "bbox": [494, 477, 617, 489]},
	{"text": "主诉：", "bbox": [160, 498, 197, 510]},
	{"text": "反复胸闷气喘20余年，再发2天。", "bbox": [160, 513, 356, 525]},
	{"text": "现病史：患者20余年前无明显诱因下开始出现胸闷气喘不适，休息后缓解，少许咳嗽，无明显咳痰，无畏", "bbox": [160, 527, 811, 540]},
	{"text": "寒寒战，无胸痛等不适。在当地医院按“支气管哮喘”给予抗感染、平喘等治疗后症状缓解。此后每因受", "bbox": [160, 543, 807, 556]},
	{"text": "凉上述症状反复发作，现长期予“信必可160”改善症状。2天前，患者受凉后再次出现胸闷、气喘，活动", "bbox": [160, 558, 807, 571]},
	{"text": "后加重，休息可缓解，伴咳嗽咳痰，呈阵发性，咳少许黄白粘痰，质粘，不易咳出，无发热，无盗汗消", "bbox": [160, 574, 792, 587]},
	{"text": "瘦，无畏寒寒战，无胸痛，无咯血，无腹痛腹泻等不适。现为进一步诊治，来我院就诊，拟“支气管哮", "bbox": [160, 590, 792, 603]},
	{"text": "喘”收住我科。", "bbox": [160, 606, 254, 619]},
	{"text": "患者起病以来，神志清，精神稍软，胃纳、睡眠一般，二便无明显异常，体重近期无增减。", "bbox": [190, 621, 744, 634]},
	{"text": "既往有“脂肪肝”5年余，具体不详，未规律复查。", "bbox": [190, 637, 498, 649]},
	{"text": "既往史：[否认]内分泌疾病史；[否认]心血管疾病史；[否认]脑血管疾病史；[否认]肾病史；[否认]肝病", "bbox": [163, 653, 809, 666]},
	{"text": "史；[否认]其他重大内科疾病史；[否认]肺结核；[否认]病毒性肝炎；[否认]其他传染病；有“头孢克", "bbox": [163, 669, 792, 681]},
	{"text": "洛”过敏史，服用后表现为胸闷；[否认]食物、其他药物过敏；[否认]外伤史；[否认]手术史；[否认]输", "bbox": [163, 684, 804, 697]},
	{"text": "血史；[否认]中毒史；[否认]长期用药史；[否认]可能成瘾药物。疫苗接种史不详。", "bbox": [163, 699, 669, 712]},
	{"text": "显示", "bbox": [925, 266, 954, 278]},
	{"text": "既往史", "bbox": [865, 633, 900, 644]},
	{"text": "婚育史", "bbox": [865, 649, 900, 660]},
	{"text": "家族史", "bbox": [865, 665, 900, 676]},
	{"text": "生命体征", "bbox": [865, 680, 909, 691]},
	{"text": "生命体征", "bbox": [865, 695, 909, 706]},
	{"text": "110%", "bbox": [921, 720, 954, 730]}
]
2026-08-05 12:00:46,321 INFO     29 [qwen-vl-text] coord API: raw_items=37, valid_items=37, elapsed=13.4s
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[0]: text=住院病历, bbox=[429, 287, 550, 303]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：胡金超 病历号：100, bbox=[156, 308, 338, 321]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[2]: text=科室名称：呼吸与危重症医学科病房 病区：七病区 床号：0747, bbox=[397, 308, 813, 321]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[3]: text=入院记录, bbox=[430, 329, 550, 345]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[165, 355, 233, 368]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[5]: text=工作单位：石鼓村, bbox=[513, 353, 634, 366]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[6]: text=性别：男, bbox=[165, 380, 263, 393]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[7]: text=住址：中国浙江省台州市, bbox=[513, 378, 709, 391]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[8]: text=年龄：46岁, bbox=[165, 416, 275, 429]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[9]: text=出生地：中国浙江省台州市临海市, bbox=[513, 413, 747, 426]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[10]: text=婚姻：未婚, bbox=[165, 437, 275, 450]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[11]: text=入院日期：2025-05-26 08:34, bbox=[512, 434, 705, 447]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[12]: text=民族：汉族, bbox=[165, 458, 275, 471]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[13]: text=记录日期：2025-05-26 09:31, bbox=[510, 456, 703, 469]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[14]: text=职业：自由职业者, bbox=[165, 479, 317, 492]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[15]: text=病史陈述者：本人, bbox=[494, 477, 617, 489]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[16]: text=主诉：, bbox=[160, 498, 197, 510]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[17]: text=反复胸闷气喘20余年，再发2天。, bbox=[160, 513, 356, 525]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[18]: text=现病史：患者20余年前无明显诱因下开始出现胸闷气喘不适，休息后缓解，少许咳嗽，无明显咳痰，无畏, bbox=[160, 527, 811, 540]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[19]: text=寒寒战，无胸痛等不适。在当地医院按“支气管哮喘”给予抗感染、平喘等治疗后症状缓解。此后每因受, bbox=[160, 543, 807, 556]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[20]: text=凉上述症状反复发作，现长期予“信必可160”改善症状。2天前，患者受凉后再次出现胸闷、气喘，活动, bbox=[160, 558, 807, 571]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[21]: text=后加重，休息可缓解，伴咳嗽咳痰，呈阵发性，咳少许黄白粘痰，质粘，不易咳出，无发热，无盗汗消, bbox=[160, 574, 792, 587]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[22]: text=瘦，无畏寒寒战，无胸痛，无咯血，无腹痛腹泻等不适。现为进一步诊治，来我院就诊，拟“支气管哮, bbox=[160, 590, 792, 603]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[23]: text=喘”收住我科。, bbox=[160, 606, 254, 619]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[24]: text=患者起病以来，神志清，精神稍软，胃纳、睡眠一般，二便无明显异常，体重近期无增减。, bbox=[190, 621, 744, 634]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[25]: text=既往有“脂肪肝”5年余，具体不详，未规律复查。, bbox=[190, 637, 498, 649]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[26]: text=既往史：[否认]内分泌疾病史；[否认]心血管疾病史；[否认]脑血管疾病史；[否认]肾病史；[否认]肝病, bbox=[163, 653, 809, 666]
2026-08-05 12:00:46,322 INFO     29 [qwen-vl-text] coord item[27]: text=史；[否认]其他重大内科疾病史；[否认]肺结核；[否认]病毒性肝炎；[否认]其他传染病；有“头孢克, bbox=[163, 669, 792, 681]
2026-08-05 12:00:46,323 INFO     29 [qwen-vl-text] coord item[28]: text=洛”过敏史，服用后表现为胸闷；[否认]食物、其他药物过敏；[否认]外伤史；[否认]手术史；[否认]输, bbox=[163, 684, 804, 697]
2026-08-05 12:00:46,323 INFO     29 [qwen-vl-text] coord item[29]: text=血史；[否认]中毒史；[否认]长期用药史；[否认]可能成瘾药物。疫苗接种史不详。, bbox=[163, 699, 669, 712]
2026-08-05 12:00:46,323 INFO     29 [qwen-vl-text] coord item[30]: text=显示, bbox=[925, 266, 954, 278]
2026-08-05 12:00:46,323 INFO     29 [qwen-vl-text] coord item[31]: text=既往史, bbox=[865, 633, 900, 644]
2026-08-05 12:00:46,323 INFO     29 [qwen-vl-text] coord item[32]: text=婚育史, bbox=[865, 649, 900, 660]
2026-08-05 12:00:46,323 INFO     29 [qwen-vl-text] coord item[33]: text=家族史, bbox=[865, 665, 900, 676]
2026-08-05 12:00:46,323 INFO     29 [qwen-vl-text] coord item[34]: text=生命体征, bbox=[865, 680, 909, 691]
2026-08-05 12:00:46,323 INFO     29 [qwen-vl-text] coord item[35]: text=生命体征, bbox=[865, 695, 909, 706]
2026-08-05 12:00:46,323 INFO     29 [qwen-vl-text] coord item[36]: text=110%, bbox=[921, 720, 954, 730]
2026-08-05 12:00:46,323 INFO     29 [qwen-vl-text] page=3 — 37/37 coords, api_time=13.4s
2026-08-05 12:00:46,326 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=879141, prompt_len=1594
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共31行）
["洛”过敏史，服用后表现为胸闷；[否认]食物、其他药物过敏；[否认]外伤史；[否认]手术史；[否认]输", "血史；[否认]中毒史；[否认]长期用药史；[否认]可能成瘾药物。疫苗接种史不详。", "个人史：出生于[中国浙江省台州市临海市]，居住较长地：[台州临海]，职业：[自由职业者]，学历：", "[普通高中毕业]，宗教：[无]。[无]饮酒习惯。[无]吸烟习惯。[无]毒物、粉尘及放射性物质接触史。", "[无]冶游史，[无]疫区居留史。", "婚育史：[未婚][未育]，。", "家族史：父亲[体健]，母亲[体健]，1兄弟姐妹[体健]，直系亲属[无]类似疾病项。患者[否认]二系三代", "有遗传病史。患者[否认]有遗传倾向的疾病。", "换页符", "体格检查", "生命体征：体温：[36.8]℃， 脉搏：[87]次/分， 呼吸：[19]次/分， 血压：[157]/ [87]mmHg", "一般情况：意识[清楚]，[自主体位]，[急性面容]，查体[合作]，身高：[167.5]cm，体重：[83.8]kg,B", "MI指数：[29.9]。", "皮肤黏膜：[皮肤粘膜无黄染]，[无水肿]，[无]。", "浅表淋巴结：[全身浅表淋巴结无肿大]。", "头颅五官：头颅[无畸形]，听力粗测[良好]。结膜[无充血水肿]，巩膜[无黄染]，瞳孔[双侧等大同圆]，", "对光反射[灵敏]，鼻通气良好，副鼻窦[无压痛]，[乳突无压痛]，口腔粘膜[无充血、糜烂、溃疡]，咽部", "充血，两侧扁桃体[无肿大]。", "颈部：颈[软]，气管[居中]，甲状腺[未触及肿大]，颈静脉[无怒张]。", "胸部：[胸廓无畸形]，肋间隙[无增宽变窄]，乳房[双侧对称、未及肿块]。", "肺部：呼吸运动[两侧对称]。叩诊[清音]，双肺闻及哮鸣音。", "心脏：心率[87]次/分，律[齐]，心音[有力]，[未闻及病理性杂音]。", "血管检查：周围血管征：阴性。", "腹部：腹[平坦]，对称，无胃肠型和蠕动波，腹部[柔软]，无[压痛，反跳痛]，腹部[无包块]。肝", "脾肾[未触及]。肾区[无叩击痛]。肠鸣音[4]次/分,移动性浊音[阴性]。", "外生殖器：外生殖器[无异常]，见专科情况。", "既往史", "婚育史", "家族史", "生命体征", "生命体征"]

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
2026-08-05 12:00:59,808 INFO     29 [qwen-vl-text] coord API raw response (len=2255):
[
	{"text": "洛”过敏史，服用后表现为胸闷；[否认]食物、其他药物过敏；[否认]外伤史；[否认]手术史；[否认]输", "bbox": [164, 294, 855, 308]},
	{"text": "血史；[否认]中毒史；[否认]长期用药史；[否认]可能成瘾药物。疫苗接种史不详。", "bbox": [164, 310, 715, 325]},
	{"text": "个人史：出生于[中国浙江省台州市临海市]，居住较长地：[台州临海]，职业：[自由职业者]，学历：", "bbox": [164, 327, 836, 341]},
	{"text": "[普通高中毕业]，宗教：[无]。[无]饮酒习惯。[无]吸烟习惯。[无]毒物、粉尘及放射性物质接触史。", "bbox": [167, 344, 834, 358]},
	{"text": "[无]冶游史，[无]疫区居留史。", "bbox": [167, 362, 374, 375]},
	{"text": "婚育史：[未婚][未育]，。", "bbox": [164, 379, 348, 392]},
	{"text": "家族史：父亲[体健]，母亲[体健]，1兄弟姐妹[体健]，直系亲属[无]类似疾病项。患者[否认]二系三代", "bbox": [164, 393, 851, 407]},
	{"text": "有遗传病史。患者[否认]有遗传倾向的疾病。", "bbox": [164, 412, 463, 425]},
	{"text": "换页符", "bbox": [864, 434, 903, 444]},
	{"text": "体格检查", "bbox": [470, 448, 561, 465]},
	{"text": "生命体征：体温：[36.8]℃， 脉搏：[87]次/分， 呼吸：[19]次/分， 血压：[157]/ [87]mmHg", "bbox": [163, 469, 780, 483]},
	{"text": "一般情况：意识[清楚]，[自主体位]，[急性面容]，查体[合作]，身高：[167.5]cm，体重：[83.8]kg,B", "bbox": [163, 484, 853, 499]},
	{"text": "MI指数：[29.9]。", "bbox": [163, 505, 276, 518]},
	{"text": "皮肤黏膜：[皮肤粘膜无黄染]，[无水肿]，[无]。", "bbox": [163, 521, 495, 534]},
	{"text": "浅表淋巴结：[全身浅表淋巴结无肿大]。", "bbox": [163, 538, 435, 551]},
	{"text": "头颅五官：头颅[无畸形]，听力粗测[良好]。结膜[无充血水肿]，巩膜[无黄染]，瞳孔[双侧等大同圆]，", "bbox": [163, 552, 849, 566]},
	{"text": "对光反射[灵敏]，鼻通气良好，副鼻窦[无压痛]，[乳突无压痛]，口腔粘膜[无充血、糜烂、溃疡]，咽部", "bbox": [163, 569, 849, 583]},
	{"text": "充血，两侧扁桃体[无肿大]。", "bbox": [163, 587, 351, 600]},
	{"text": "颈部：颈[软]，气管[居中]，甲状腺[未触及肿大]，颈静脉[无怒张]。", "bbox": [163, 603, 659, 617]},
	{"text": "胸部：[胸廓无畸形]，肋间隙[无增宽变窄]，乳房[双侧对称、未及肿块]。", "bbox": [163, 619, 687, 633]},
	{"text": "肺部：呼吸运动[两侧对称]。叩诊[清音]，双肺闻及哮鸣音。", "bbox": [163, 636, 594, 650]},
	{"text": "心脏：心率[87]次/分，律[齐]，心音[有力]，[未闻及病理性杂音]。", "bbox": [163, 653, 647, 667]},
	{"text": "血管检查：周围血管征：阴性。", "bbox": [163, 670, 368, 683]},
	{"text": "腹部：腹[平坦]，对称，无胃肠型和蠕动波，腹部[柔软]，无[压痛，反跳痛]，腹部[无包块]。肝", "bbox": [163, 686, 840, 699]},
	{"text": "脾肾[未触及]。肾区[无叩击痛]。肠鸣音[4]次/分,移动性浊音[阴性]。", "bbox": [163, 702, 621, 716]},
	{"text": "外生殖器：外生殖器[无异常]，见专科情况。", "bbox": [163, 719, 456, 732]},
	{"text": "既往史", "bbox": [908, 651, 946, 662]},
	{"text": "婚育史", "bbox": [908, 668, 946, 679]},
	{"text": "家族史", "bbox": [908, 685, 946, 696]},
	{"text": "生命体征", "bbox": [908, 702, 958, 713]},
	{"text": "生命体征", "bbox": [908, 719, 958, 730]}
]
2026-08-05 12:00:59,809 INFO     29 [qwen-vl-text] coord API: raw_items=31, valid_items=31, elapsed=13.5s
2026-08-05 12:00:59,809 INFO     29 [qwen-vl-text] coord item[0]: text=洛”过敏史，服用后表现为胸闷；[否认]食物、其他药物过敏；[否认]外伤史；[否认]手术史；[否认]输, bbox=[164, 294, 855, 308]
2026-08-05 12:00:59,809 INFO     29 [qwen-vl-text] coord item[1]: text=血史；[否认]中毒史；[否认]长期用药史；[否认]可能成瘾药物。疫苗接种史不详。, bbox=[164, 310, 715, 325]
2026-08-05 12:00:59,809 INFO     29 [qwen-vl-text] coord item[2]: text=个人史：出生于[中国浙江省台州市临海市]，居住较长地：[台州临海]，职业：[自由职业者]，学历：, bbox=[164, 327, 836, 341]
2026-08-05 12:00:59,809 INFO     29 [qwen-vl-text] coord item[3]: text=[普通高中毕业]，宗教：[无]。[无]饮酒习惯。[无]吸烟习惯。[无]毒物、粉尘及放射性物质接触史。, bbox=[167, 344, 834, 358]
2026-08-05 12:00:59,809 INFO     29 [qwen-vl-text] coord item[4]: text=[无]冶游史，[无]疫区居留史。, bbox=[167, 362, 374, 375]
2026-08-05 12:00:59,809 INFO     29 [qwen-vl-text] coord item[5]: text=婚育史：[未婚][未育]，。, bbox=[164, 379, 348, 392]
2026-08-05 12:00:59,809 INFO     29 [qwen-vl-text] coord item[6]: text=家族史：父亲[体健]，母亲[体健]，1兄弟姐妹[体健]，直系亲属[无]类似疾病项。患者[否认]二系三代, bbox=[164, 393, 851, 407]
2026-08-05 12:00:59,809 INFO     29 [qwen-vl-text] coord item[7]: text=有遗传病史。患者[否认]有遗传倾向的疾病。, bbox=[164, 412, 463, 425]
2026-08-05 12:00:59,809 INFO     29 [qwen-vl-text] coord item[8]: text=换页符, bbox=[864, 434, 903, 444]
2026-08-05 12:00:59,809 INFO     29 [qwen-vl-text] coord item[9]: text=体格检查, bbox=[470, 448, 561, 465]
2026-08-05 12:00:59,809 INFO     29 [qwen-vl-text] coord item[10]: text=生命体征：体温：[36.8]℃， 脉搏：[87]次/分， 呼吸：[19]次/分， 血压：[157]/ [87]mmHg, bbox=[163, 469, 780, 483]
2026-08-05 12:00:59,809 INFO     29 [qwen-vl-text] coord item[11]: text=一般情况：意识[清楚]，[自主体位]，[急性面容]，查体[合作]，身高：[167.5]cm，体重：[83.8]kg,B, bbox=[163, 484, 853, 499]
2026-08-05 12:00:59,809 INFO     29 [qwen-vl-text] coord item[12]: text=MI指数：[29.9]。, bbox=[163, 505, 276, 518]
2026-08-05 12:00:59,809 INFO     29 [qwen-vl-text] coord item[13]: text=皮肤黏膜：[皮肤粘膜无黄染]，[无水肿]，[无]。, bbox=[163, 521, 495, 534]
2026-08-05 12:00:59,809 INFO     29 [qwen-vl-text] coord item[14]: text=浅表淋巴结：[全身浅表淋巴结无肿大]。, bbox=[163, 538, 435, 551]
2026-08-05 12:00:59,809 INFO     29 [qwen-vl-text] coord item[15]: text=头颅五官：头颅[无畸形]，听力粗测[良好]。结膜[无充血水肿]，巩膜[无黄染]，瞳孔[双侧等大同圆]，, bbox=[163, 552, 849, 566]
2026-08-05 12:00:59,810 INFO     29 [qwen-vl-text] coord item[16]: text=对光反射[灵敏]，鼻通气良好，副鼻窦[无压痛]，[乳突无压痛]，口腔粘膜[无充血、糜烂、溃疡]，咽部, bbox=[163, 569, 849, 583]
2026-08-05 12:00:59,810 INFO     29 [qwen-vl-text] coord item[17]: text=充血，两侧扁桃体[无肿大]。, bbox=[163, 587, 351, 600]
2026-08-05 12:00:59,810 INFO     29 [qwen-vl-text] coord item[18]: text=颈部：颈[软]，气管[居中]，甲状腺[未触及肿大]，颈静脉[无怒张]。, bbox=[163, 603, 659, 617]
2026-08-05 12:00:59,810 INFO     29 [qwen-vl-text] coord item[19]: text=胸部：[胸廓无畸形]，肋间隙[无增宽变窄]，乳房[双侧对称、未及肿块]。, bbox=[163, 619, 687, 633]
2026-08-05 12:00:59,810 INFO     29 [qwen-vl-text] coord item[20]: text=肺部：呼吸运动[两侧对称]。叩诊[清音]，双肺闻及哮鸣音。, bbox=[163, 636, 594, 650]
2026-08-05 12:00:59,810 INFO     29 [qwen-vl-text] coord item[21]: text=心脏：心率[87]次/分，律[齐]，心音[有力]，[未闻及病理性杂音]。, bbox=[163, 653, 647, 667]
2026-08-05 12:00:59,810 INFO     29 [qwen-vl-text] coord item[22]: text=血管检查：周围血管征：阴性。, bbox=[163, 670, 368, 683]
2026-08-05 12:00:59,810 INFO     29 [qwen-vl-text] coord item[23]: text=腹部：腹[平坦]，对称，无胃肠型和蠕动波，腹部[柔软]，无[压痛，反跳痛]，腹部[无包块]。肝, bbox=[163, 686, 840, 699]
2026-08-05 12:00:59,810 INFO     29 [qwen-vl-text] coord item[24]: text=脾肾[未触及]。肾区[无叩击痛]。肠鸣音[4]次/分,移动性浊音[阴性]。, bbox=[163, 702, 621, 716]
2026-08-05 12:00:59,810 INFO     29 [qwen-vl-text] coord item[25]: text=外生殖器：外生殖器[无异常]，见专科情况。, bbox=[163, 719, 456, 732]
2026-08-05 12:00:59,810 INFO     29 [qwen-vl-text] coord item[26]: text=既往史, bbox=[908, 651, 946, 662]
2026-08-05 12:00:59,810 INFO     29 [qwen-vl-text] coord item[27]: text=婚育史, bbox=[908, 668, 946, 679]
2026-08-05 12:00:59,810 INFO     29 [qwen-vl-text] coord item[28]: text=家族史, bbox=[908, 685, 946, 696]
2026-08-05 12:00:59,810 INFO     29 [qwen-vl-text] coord item[29]: text=生命体征, bbox=[908, 702, 958, 713]
2026-08-05 12:00:59,810 INFO     29 [qwen-vl-text] coord item[30]: text=生命体征, bbox=[908, 719, 958, 730]
2026-08-05 12:00:59,810 INFO     29 [qwen-vl-text] page=4 — 31/31 coords, api_time=13.5s
2026-08-05 12:00:59,812 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=675996, prompt_len=1206
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共27行）
["肿}。", "神经系统：肌张力无增高或降低，四肢肌力[V级]，双侧膝腱反射[++]，[双侧]Babinski征[阴性]。", "其他：见专科检查", "补充及专科情况", "一般情况：[无]发绀，[无]鼻翼扇动，[无]端坐呼吸，气管[居中]，浅表颈静脉[无怒张]，肝颈静脉返流", "征[阴性]，[无]皮疹结节，[无]皮下气肿，[无]浮肿，[无]皮下瘀点、瘀斑，[无]无杵状指（趾）；", "胸部：胸廓[无畸形]，肋间隙[无增宽或缩窄]，局部[无殊]，胸壁浅表静脉[无]曲张，脊柱[无畸形]，呼", "吸动度[对称]，[无]胸壁压痛；", "肺部 视诊：[胸式]呼吸为主，呼吸频率[19]次/分，节律[规律]，呼吸运动[对称]，[无]呼吸困难；触", "诊：语颤[对称]，[无]胸膜摩擦感，[无]皮下捻发感；叩诊：[清音]。", "浊音 实音 鼓音", "湿啰音 干啰音", "肺下界(肋间)", "锁骨中线", "腋中线", "右", "6", "8", "左", "6", "8", "肺下界移动范围：左{6}cm，右{6}cm", "听诊：两肺[呼吸音粗]，可闻及哮鸣音，[无]呼气延长，语音传导[对称]，[无]胸膜摩擦音；", "辅助检查：[本次暂缺。]", "初步诊断：", "1.支气管哮喘", "2.脂肪肝 诊断医生：吴蓉 诊断时间：2025-05-26 09:41"]

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
2026-08-05 12:01:09,155 INFO     29 [qwen-vl-text] coord API raw response (len=1703):
[
	{"text": "肿}。", "bbox": [182, 271, 215, 282]},
	{"text": "神经系统：肌张力无增高或降低，四肢肌力[V级]，双侧膝腱反射[++]，[双侧]Babinski征[阴性]。", "bbox": [182, 288, 840, 307]},
	{"text": "其他：见专科检查", "bbox": [182, 305, 344, 319]},
	{"text": "补充及专科情况", "bbox": [456, 328, 615, 345]},
	{"text": "一般情况：[无]发绀，[无]鼻翼扇动，[无]端坐呼吸，气管[居中]，浅表颈静脉[无怒张]，肝颈静脉返流", "bbox": [176, 349, 870, 365]},
	{"text": "征[阴性]，[无]皮疹结节，[无]皮下气肿，[无]浮肿，[无]皮下瘀点、瘀斑，[无]无杵状指（趾）；", "bbox": [176, 365, 835, 380]},
	{"text": "胸部：胸廓[无畸形]，肋间隙[无增宽或缩窄]，局部[无殊]，胸壁浅表静脉[无]曲张，脊柱[无畸形]，呼", "bbox": [176, 381, 870, 397]},
	{"text": "吸动度[对称]，[无]胸壁压痛；", "bbox": [176, 398, 388, 412]},
	{"text": "肺部 视诊：[胸式]呼吸为主，呼吸频率[19]次/分，节律[规律]，呼吸运动[对称]，[无]呼吸困难；触", "bbox": [176, 415, 862, 431]},
	{"text": "诊：语颤[对称]，[无]胸膜摩擦感，[无]皮下捻发感；叩诊：[清音]。", "bbox": [176, 432, 642, 447]},
	{"text": "浊音 实音 鼓音", "bbox": [457, 520, 587, 531]},
	{"text": "湿啰音 干啰音", "bbox": [457, 533, 562, 544]},
	{"text": "肺下界(肋间)", "bbox": [236, 574, 327, 587]},
	{"text": "锁骨中线", "bbox": [496, 572, 557, 585]},
	{"text": "腋中线", "bbox": [735, 570, 780, 583]},
	{"text": "右", "bbox": [275, 598, 290, 610]},
	{"text": "6", "bbox": [523, 598, 532, 607]},
	{"text": "8", "bbox": [753, 596, 762, 606]},
	{"text": "左", "bbox": [275, 622, 291, 634]},
	{"text": "6", "bbox": [523, 622, 532, 631]},
	{"text": "8", "bbox": [753, 620, 762, 630]},
	{"text": "肺下界移动范围：左{6}cm，右{6}cm", "bbox": [162, 643, 425, 656]},
	{"text": "听诊：两肺[呼吸音粗]，可闻及哮鸣音，[无]呼气延长，语音传导[对称]，[无]胸膜摩擦音；", "bbox": [162, 658, 785, 672]},
	{"text": "辅助检查：[本次暂缺。]", "bbox": [162, 677, 340, 690]},
	{"text": "初步诊断：", "bbox": [162, 694, 237, 707]},
	{"text": "1.支气管哮喘", "bbox": [162, 712, 255, 725]},
	{"text": "2.脂肪肝 诊断医生：吴蓉 诊断时间：2025-05-26 09:41", "bbox": [162, 727, 547, 740]}
]
2026-08-05 12:01:09,156 INFO     29 [qwen-vl-text] coord API: raw_items=27, valid_items=27, elapsed=9.3s
2026-08-05 12:01:09,156 INFO     29 [qwen-vl-text] coord item[0]: text=肿}。, bbox=[182, 271, 215, 282]
2026-08-05 12:01:09,156 INFO     29 [qwen-vl-text] coord item[1]: text=神经系统：肌张力无增高或降低，四肢肌力[V级]，双侧膝腱反射[++]，[双侧]Babinski征[阴性]。, bbox=[182, 288, 840, 307]
2026-08-05 12:01:09,156 INFO     29 [qwen-vl-text] coord item[2]: text=其他：见专科检查, bbox=[182, 305, 344, 319]
2026-08-05 12:01:09,156 INFO     29 [qwen-vl-text] coord item[3]: text=补充及专科情况, bbox=[456, 328, 615, 345]
2026-08-05 12:01:09,157 INFO     29 [qwen-vl-text] coord item[4]: text=一般情况：[无]发绀，[无]鼻翼扇动，[无]端坐呼吸，气管[居中]，浅表颈静脉[无怒张]，肝颈静脉返流, bbox=[176, 349, 870, 365]
2026-08-05 12:01:09,157 INFO     29 [qwen-vl-text] coord item[5]: text=征[阴性]，[无]皮疹结节，[无]皮下气肿，[无]浮肿，[无]皮下瘀点、瘀斑，[无]无杵状指（趾）；, bbox=[176, 365, 835, 380]
2026-08-05 12:01:09,157 INFO     29 [qwen-vl-text] coord item[6]: text=胸部：胸廓[无畸形]，肋间隙[无增宽或缩窄]，局部[无殊]，胸壁浅表静脉[无]曲张，脊柱[无畸形]，呼, bbox=[176, 381, 870, 397]
2026-08-05 12:01:09,157 INFO     29 [qwen-vl-text] coord item[7]: text=吸动度[对称]，[无]胸壁压痛；, bbox=[176, 398, 388, 412]
2026-08-05 12:01:09,157 INFO     29 [qwen-vl-text] coord item[8]: text=肺部 视诊：[胸式]呼吸为主，呼吸频率[19]次/分，节律[规律]，呼吸运动[对称]，[无]呼吸困难；触, bbox=[176, 415, 862, 431]
2026-08-05 12:01:09,157 INFO     29 [qwen-vl-text] coord item[9]: text=诊：语颤[对称]，[无]胸膜摩擦感，[无]皮下捻发感；叩诊：[清音]。, bbox=[176, 432, 642, 447]
2026-08-05 12:01:09,157 INFO     29 [qwen-vl-text] coord item[10]: text=浊音 实音 鼓音, bbox=[457, 520, 587, 531]
2026-08-05 12:01:09,157 INFO     29 [qwen-vl-text] coord item[11]: text=湿啰音 干啰音, bbox=[457, 533, 562, 544]
2026-08-05 12:01:09,157 INFO     29 [qwen-vl-text] coord item[12]: text=肺下界(肋间), bbox=[236, 574, 327, 587]
2026-08-05 12:01:09,157 INFO     29 [qwen-vl-text] coord item[13]: text=锁骨中线, bbox=[496, 572, 557, 585]
2026-08-05 12:01:09,157 INFO     29 [qwen-vl-text] coord item[14]: text=腋中线, bbox=[735, 570, 780, 583]
2026-08-05 12:01:09,157 INFO     29 [qwen-vl-text] coord item[15]: text=右, bbox=[275, 598, 290, 610]
2026-08-05 12:01:09,157 INFO     29 [qwen-vl-text] coord item[16]: text=6, bbox=[523, 598, 532, 607]
2026-08-05 12:01:09,157 INFO     29 [qwen-vl-text] coord item[17]: text=8, bbox=[753, 596, 762, 606]
2026-08-05 12:01:09,157 INFO     29 [qwen-vl-text] coord item[18]: text=左, bbox=[275, 622, 291, 634]
2026-08-05 12:01:09,157 INFO     29 [qwen-vl-text] coord item[19]: text=6, bbox=[523, 622, 532, 631]
2026-08-05 12:01:09,157 INFO     29 [qwen-vl-text] coord item[20]: text=8, bbox=[753, 620, 762, 630]
2026-08-05 12:01:09,157 INFO     29 [qwen-vl-text] coord item[21]: text=肺下界移动范围：左{6}cm，右{6}cm, bbox=[162, 643, 425, 656]
2026-08-05 12:01:09,158 INFO     29 [qwen-vl-text] coord item[22]: text=听诊：两肺[呼吸音粗]，可闻及哮鸣音，[无]呼气延长，语音传导[对称]，[无]胸膜摩擦音；, bbox=[162, 658, 785, 672]
2026-08-05 12:01:09,158 INFO     29 [qwen-vl-text] coord item[23]: text=辅助检查：[本次暂缺。], bbox=[162, 677, 340, 690]
2026-08-05 12:01:09,158 INFO     29 [qwen-vl-text] coord item[24]: text=初步诊断：, bbox=[162, 694, 237, 707]
2026-08-05 12:01:09,158 INFO     29 [qwen-vl-text] coord item[25]: text=1.支气管哮喘, bbox=[162, 712, 255, 725]
2026-08-05 12:01:09,158 INFO     29 [qwen-vl-text] coord item[26]: text=2.脂肪肝 诊断医生：吴蓉 诊断时间：2025-05-26 09:41, bbox=[162, 727, 547, 740]
2026-08-05 12:01:09,158 INFO     29 [qwen-vl-text] page=5 — 27/27 coords, api_time=9.3s
2026-08-05 12:01:09,159 INFO     29 [qwen-vl-text] new_positions (163):
[[2, 23.8110400390625, 35.12128405761719, 260.1440145263672, 269.4048046875], [2, 55.36066809082031, 92.26778015136719, 260.9859045410156, 269.4048046875], [2, 520.8665008544922, 537.5342288818359, 258.4602344970703, 267.72102465820313], [2, 550.0350249023438, 569.6791329345704, 259.3021245117188, 267.72102465820313], [2, 448.83810473632815, 475.03024877929687, 280.3493748779297, 289.6101650390625], [2, 489.912148803711, 505.98460083007814, 280.3493748779297, 289.6101650390625], [2, 520.2712248535156, 535.7484008789063, 280.3493748779297, 289.6101650390625], [2, 550.0350249023438, 567.298028930664, 280.3493748779297, 289.6101650390625], [2, 121.43630419921875, 460.7436247558594, 302.23851525878905, 310.6574154052734], [2, 27.97797204589844, 53.57484008789063, 323.285765625, 331.7046657714844], [2, 40.47876806640625, 147.03317224121093, 341.8073459472656, 350.22624609375], [2, 180.36862829589845, 215.48991235351562, 341.8073459472656, 350.22624609375], [2, 310.7340725097656, 337.52149255371097, 341.8073459472656, 350.22624609375], [2, 447.05227673339846, 466.696384765625, 341.8073459472656, 350.22624609375], [2, 65.48036010742187, 78.57643212890625, 355.27758618164063, 363.696486328125], [2, 193.4647003173828, 220.8473963623047, 355.27758618164063, 363.696486328125], [2, 317.8773845214844, 376.2144326171875, 355.27758618164063, 363.696486328125], [2, 441.0995167236328, 520.2712248535156, 355.27758618164063, 363.696486328125], [2, 344.6648045654297, 375.0238806152344, 368.74782641601564, 376.32483654785153], [2, 66.670912109375, 98.81581616210939, 381.3761766357422, 389.79507678222654], [2, 164.29617626953126, 225.01432836914063, 381.3761766357422, 389.79507678222654], [2, 294.66162048339845, 361.3325325927735, 381.3761766357422, 389.79507678222654], [2, 423.83651269531254, 489.3168728027344, 381.3761766357422, 389.79507678222654], [2, 66.670912109375, 98.81581616210939, 394.0045268554687, 402.42342700195314], [2, 194.65525231933594, 227.99070837402346, 394.0045268554687, 402.42342700195314], [2, 324.42542053222655, 375.61915661621094, 394.0045268554687, 402.42342700195314], [2, 462.5294527587891, 467.2916607666016, 394.0045268554687, 402.42342700195314], [2, 61.31342810058594, 154.77176025390625, 406.6328770751953, 415.0517772216797], [2, 454.1955887451172, 530.9861928710937, 406.6328770751953, 415.0517772216797], [2, 61.31342810058594, 154.77176025390625, 420.1031173095703, 427.6801274414062], [2, 187.5119403076172, 193.4647003173828, 420.1031173095703, 427.6801274414062], [2, 441.0995167236328, 495.26963281250005, 420.1031173095703, 427.6801274414062], [2, 55.36066809082031, 157.1528642578125, 432.7314675292969, 440.3084776611328], [2, 185.72611230468752, 193.4647003173828, 432.7314675292969, 440.3084776611328], [2, 441.0995167236328, 495.26963281250005, 432.7314675292969, 440.3084776611328], [2, 67.86146411132813, 100.00636816406251, 445.3598177490234, 453.7787178955078], [2, 183.34500830078125, 210.72770434570313, 445.3598177490234, 453.7787178955078], [2, 248.82536840820313, 254.77812841796876, 445.3598177490234, 453.7787178955078], [2, 56.55122009277344, 105.95912817382813, 457.98816796875, 466.4070681152344], [2, 171.43948828125002, 209.53715234375, 457.98816796875, 466.4070681152344], [2, 56.55122009277344, 175.60642028808596, 471.458408203125, 479.8773083496094], [2, 441.0995167236328, 495.26963281250005, 471.458408203125, 479.8773083496094], [2, 51.78901208496094, 80.9575361328125, 484.0867584228516, 492.50565856933594], [2, 197.0363563232422, 261.32616442871097, 484.0867584228516, 492.50565856933594], [2, 324.42542053222655, 337.52149255371097, 484.0867584228516, 492.50565856933594], [2, 434.5514807128906, 492.8885288085938, 484.0867584228516, 492.50565856933594], [2, 532.7720208740235, 543.4869888916016, 484.0867584228516, 492.50565856933594], [2, 474.43497277832034, 492.8885288085938, 497.55699865722653, 505.1340087890625], [2, 57.741772094726564, 101.19692016601563, 510.1853488769531, 518.6042490234375], [2, 185.13083630371094, 230.96708837890625, 510.1853488769531, 518.6042490234375], [2, 333.354560546875, 338.1167685546875, 510.1853488769531, 518.6042490234375], [2, 463.1247287597656, 467.88693676757816, 510.1853488769531, 518.6042490234375], [2, 48.21735607910156, 185.13083630371094, 522.8136990966797, 531.232599243164], [2, 431.5751007080078, 506.5798768310547, 522.8136990966797, 531.232599243164], [2, 59.527600097656254, 121.43630419921875, 536.2839393310546, 544.7028394775391], [2, 172.63004028320313, 252.99230041503907, 536.2839393310546, 544.7028394775391], [2, 313.71045251464847, 379.7860886230469, 536.2839393310546, 544.7028394775391], [2, 442.29006872558597, 525.0334328613282, 536.2839393310546, 544.7028394775391], [2, 59.527600097656254, 158.34341625976563, 548.9122895507812, 557.3311896972656], [2, 185.72611230468752, 238.11040039062502, 548.9122895507812, 557.3311896972656], [2, 333.9498365478516, 338.7120445556641, 548.9122895507812, 557.3311896972656], [2, 463.1247287597656, 467.88693676757816, 548.9122895507812, 557.3311896972656], [2, 59.527600097656254, 83.93391613769532, 562.3825297851563, 570.8014299316407], [2, 442.29006872558597, 525.0334328613282, 562.3825297851563, 570.8014299316407], [2, 59.527600097656254, 159.53396826171877, 575.0108800048828, 583.4297801513671], [2, 186.91666430664063, 238.11040039062502, 575.0108800048828, 583.4297801513671], [2, 301.8049324951172, 357.7608765869141, 575.0108800048828, 583.4297801513671], [2, 463.1247287597656, 467.88693676757816, 575.0108800048828, 583.4297801513671], [3, 255.3734044189453, 327.4018005371094, 241.62243420410155, 255.09267443847656], [3, 92.86305615234376, 201.20328833007812, 259.3021245117188, 270.24669470214843], [3, 236.32457238769533, 483.9593887939453, 259.3021245117188, 270.24669470214843], [3, 255.9686804199219, 327.4018005371094, 276.9818148193359, 290.4520550537109], [3, 98.22054016113282, 138.69930822753906, 298.8709552001953, 309.815525390625], [3, 305.3765885009766, 377.40498461914063, 297.18717517089846, 308.1317453613281], [3, 98.22054016113282, 156.55758825683594, 319.91820556640624, 330.86277575683596], [3, 305.3765885009766, 422.05068469238284, 318.23442553710936, 329.1789957275391], [3, 98.22054016113282, 163.7009002685547, 350.22624609375, 361.1708162841797], [3, 305.3765885009766, 444.6711727294922, 347.7005760498047, 358.6451462402344], [3, 98.22054016113282, 163.7009002685547, 367.90593640136717, 378.8505065917969], [3, 304.7813125, 419.6695806884766, 365.3802663574219, 376.32483654785153], [3, 98.22054016113282, 163.7009002685547, 385.58562670898436, 396.5301968994141], [3, 303.5907604980469, 418.47902868652346, 383.9018466796875, 394.8464168701172], [3, 98.22054016113282, 188.70249230957032, 403.26531701660156, 414.2098872070313], [3, 294.06634448242187, 367.2852926025391, 401.5815369873047, 411.6842171630859], [3, 95.24416015625, 117.26937219238282, 419.26122729492187, 429.3639074707031], [3, 95.24416015625, 211.91825634765627, 431.8895775146484, 441.9922576904297], [3, 95.24416015625, 482.7688367919922, 443.67603771972654, 454.62060791015625], [3, 95.24416015625, 480.38773278808594, 457.14627795410155, 468.09084814453126], [3, 95.24416015625, 480.38773278808594, 469.7746281738281, 480.7191983642578], [3, 95.24416015625, 471.45859277343754, 483.2448684082031, 494.1894385986328], [3, 95.24416015625, 471.45859277343754, 496.7151086425781, 507.65967883300783], [3, 95.24416015625, 151.20010424804687, 510.1853488769531, 521.1299190673828], [3, 113.10244018554688, 442.8853447265625, 522.8136990966797, 533.7582692871093], [3, 113.10244018554688, 296.44744848632814, 536.2839393310546, 546.3866195068359], [3, 97.0299881591797, 481.5782847900391, 549.7541795654297, 560.6987497558594], [3, 97.0299881591797, 471.45859277343754, 563.2244197998047, 573.327099975586], [3, 97.0299881591797, 478.60190478515625, 575.8527700195312, 586.7973402099609], [3, 97.0299881591797, 398.23964465332034, 588.4811202392578, 599.4256904296875], [3, 550.6303009033203, 567.8933049316406, 223.94274389648436, 234.04542407226563], [3, 514.9137408447266, 535.7484008789063, 532.916379272461, 542.1771694335937], [3, 514.9137408447266, 535.7484008789063, 546.3866195068359, 555.6474096679688], [3, 514.9137408447266, 535.7484008789063, 559.8568597412109, 569.1176499023437], [3, 514.9137408447266, 541.1058848876953, 572.4852099609375, 581.7460001220703], [3, 514.9137408447266, 541.1058848876953, 585.1135601806641, 594.3743503417969], [3, 548.2491968994141, 567.8933049316406, 606.160810546875, 614.5797106933594], [4, 97.62526416015625, 508.96098083496094, 247.51566430664062, 259.3021245117188], [4, 97.62526416015625, 425.6223406982422, 260.9859045410156, 273.6142547607422], [4, 97.62526416015625, 497.65073681640627, 275.2980347900391, 287.0844949951172], [4, 99.41109216308594, 496.46018481445316, 289.6101650390625, 301.39662524414064], [4, 99.41109216308594, 222.63322436523438, 304.76418530273435, 315.70875549316406], [4, 97.62526416015625, 207.15604833984375, 319.07631555175783, 330.0208857421875], [4, 97.62526416015625, 506.5798768310547, 330.86277575683596, 342.64923596191403], [4, 97.62526416015625, 275.61278845214844, 346.85868603515627, 357.8032562255859], [4, 514.31846484375, 537.5342288818359, 365.3802663574219, 373.79916650390624], [4, 279.7797204589844, 333.9498365478516, 377.1667265625, 391.4788568115234], [4, 97.0299881591797, 464.3152807617188, 394.8464168701172, 406.6328770751953], [4, 97.0299881591797, 507.7704288330078, 407.47476708984374, 420.1031173095703], [4, 97.0299881591797, 164.29617626953126, 425.15445739746093, 436.09902758789065], [4, 97.0299881591797, 294.66162048339845, 438.62469763183594, 449.5692678222656], [4, 97.0299881591797, 258.9450604248047, 452.93682788085937, 463.8813980712891], [4, 97.0299881591797, 505.3893248291016, 464.7232880859375, 476.5097482910156], [4, 97.0299881591797, 505.3893248291016, 479.0354183349609, 490.82187854003905], [4, 97.0299881591797, 208.94187634277344, 494.1894385986328, 505.1340087890625], [4, 97.0299881591797, 392.2868846435547, 507.65967883300783, 519.4461390380859], [4, 97.0299881591797, 408.9546126708984, 521.1299190673828, 532.916379272461], [4, 97.0299881591797, 353.59394458007813, 535.4420493164063, 547.2285095214844], [4, 97.0299881591797, 385.143572631836, 549.7541795654297, 561.5406397705078], [4, 97.0299881591797, 219.061568359375, 564.0663098144531, 575.0108800048828], [4, 97.0299881591797, 500.03184082031254, 577.5365500488281, 588.4811202392578], [4, 97.0299881591797, 369.66639660644535, 591.0067902832031, 602.7932504882813], [4, 97.0299881591797, 271.44585644531253, 605.3189205322266, 616.2634907226562], [4, 540.5106088867187, 563.1310969238282, 548.0703995361328, 557.3311896972656], [4, 540.5106088867187, 563.1310969238282, 562.3825297851563, 571.643319946289], [4, 540.5106088867187, 563.1310969238282, 576.6946600341797, 585.9554501953124], [4, 540.5106088867187, 570.274408935547, 591.0067902832031, 600.267580444336], [4, 540.5106088867187, 570.274408935547, 605.3189205322266, 614.5797106933594], [5, 108.34023217773438, 127.98434020996095, 228.15219396972657, 237.41298413085937], [5, 108.34023217773438, 500.03184082031254, 242.46432421875, 258.4602344970703], [5, 108.34023217773438, 204.7749443359375, 256.7764544677734, 268.56291467285155], [5, 271.44585644531253, 366.09474060058596, 276.1399248046875, 290.4520550537109], [5, 104.768576171875, 517.8901208496094, 293.8196151123047, 307.2898553466797], [5, 104.768576171875, 497.0554608154297, 307.2898553466797, 319.91820556640624], [5, 104.768576171875, 517.8901208496094, 320.76009558105466, 334.23033581542967], [5, 104.768576171875, 230.96708837890625, 335.07222583007814, 346.85868603515627], [5, 104.768576171875, 513.1279128417968, 349.38435607910156, 362.8545963134766], [5, 104.768576171875, 382.1671926269531, 363.696486328125, 376.32483654785153], [5, 272.04113244628905, 349.4270125732422, 437.7828076171875, 447.0435977783203], [5, 272.04113244628905, 334.5451125488281, 448.7273778076172, 457.98816796875], [5, 140.48513623046875, 194.65525231933594, 483.2448684082031, 494.1894385986328], [5, 295.25689648437503, 331.5687325439453, 481.5610883789062, 492.50565856933594], [5, 437.5278607177735, 464.3152807617188, 479.8773083496094, 490.82187854003905], [5, 163.7009002685547, 172.63004028320313, 503.4502287597656, 513.5529089355468], [5, 311.3293485107422, 316.68683251953127, 503.4502287597656, 511.02723889160154], [5, 448.24282873535157, 453.60031274414064, 501.76644873046877, 510.1853488769531], [5, 163.7009002685547, 173.22531628417968, 523.6555891113281, 533.7582692871093], [5, 311.3293485107422, 316.68683251953127, 523.6555891113281, 531.232599243164], [5, 448.24282873535157, 453.60031274414064, 521.9718090820312, 530.3907092285157], [5, 96.43471215820313, 252.99230041503907, 541.3352794189453, 552.279849609375], [5, 96.43471215820313, 467.2916607666016, 553.9636296386718, 565.75008984375], [5, 96.43471215820313, 202.39384033203126, 569.9595399169922, 580.9041101074218], [5, 96.43471215820313, 141.0804122314453, 584.2716701660156, 595.2162403564453], [5, 96.43471215820313, 151.79538024902345, 599.4256904296875, 610.3702606201172], [5, 96.43471215820313, 325.6159725341797, 612.0540406494141, 622.9986108398438]]
2026-08-05 12:01:09,159 INFO     29 [qwen-vl-text] ═══ DONE ═══ 163 positions, pages=4, time=112.3s
2026-08-05 12:01:09,184 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T12:01:09.183+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 11, "lag": 1, "done": 14, "failed": 0, "current": {"add7faa690be11f1a3da71efcdd7cc1f": {"id": "add7faa690be11f1a3da71efcdd7cc1f", "doc_id": "ad4ce53890be11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785928406003, "task_type": "dataflow", "root_trace_id": "97b6871067dc44d0a8770cc05c1f97d7", "root_traceparent": "00-97b6871067dc44d0a8770cc05c1f97d7-b9788b06415dfedf-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "aeebe39490be11f1a3da71efcdd7cc1f": {"id": "aeebe39490be11f1a3da71efcdd7cc1f", "doc_id": "ae83c98a90be11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u54ee\u5598-HJCH222   2.27.pdf", "type": "pdf", "location": "\u54ee\u5598-HJCH222   2.27.pdf", "size": 16296401, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785928407811, "task_type": "dataflow", "root_trace_id": "d72ca28b91c84f599f1151379b451f37", "root_traceparent": "00-d72ca28b91c84f599f1151379b451f37-5c87c8a5dc8089ce-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "aff3407090be11f1a3da71efcdd7cc1f": {"id": "aff3407090be11f1a3da71efcdd7cc1f", "doc_id": "af8df0da90be11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWRNA(2).pdf", "type": "pdf", "location": "\u9ea6\u6d4eWRNA(2).pdf", "size": 13028582, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785928409538, "task_type": "dataflow", "root_trace_id": "a5accc15990a4c4988975b37b8223be2", "root_traceparent": "00-a5accc15990a4c4988975b37b8223be2-e1a2a450add9e6ea-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "b1a9baa290be11f1a3da71efcdd7cc1f": {"id": "b1a9baa290be11f1a3da71efcdd7cc1f", "doc_id": "b169d0b890be11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHGL.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHGL.pdf", "size": 4836707, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785928412411, "task_type": "dataflow", "root_trace_id": "d2b4e8b95ec14beebe14377dfeb00869", "root_traceparent": "00-d2b4e8b95ec14beebe14377dfeb00869-8210764337b1d147-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "b28be2ce90be11f1a3da71efcdd7cc1f": {"id": "b28be2ce90be11f1a3da71efcdd7cc1f", "doc_id": "b2448c9e90be11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHYH.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHYH.pdf", "size": 10529265, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785928413891, "task_type": "dataflow", "root_trace_id": "e3dcb8801128457d8d83b73c11855569", "root_traceparent": "00-e3dcb8801128457d8d83b73c11855569-a468dda7915c610d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
[92m12:01:09 - LiteLLM:ERROR[0m: logging_worker.py:103 - LoggingWorker error: 
Traceback (most recent call last):
  File "/root/.local/share/uv/python/cpython-3.12.12-linux-x86_64-gnu/lib/python3.12/asyncio/tasks.py", line 520, in wait_for
    return await fut
           ^^^^^^^^^
  File "/root/.local/share/uv/python/cpython-3.12.12-linux-x86_64-gnu/lib/python3.12/asyncio/futures.py", line 289, in __await__
    yield self  # This tells Task to wait for completion.
    ^^^^^^^^^^
asyncio.exceptions.CancelledError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/ragflow/.venv/lib/python3.12/site-packages/litellm/litellm_core_utils/logging_worker.py", line 98, in _process_log_task
    await asyncio.wait_for(
  File "/root/.local/share/uv/python/cpython-3.12.12-linux-x86_64-gnu/lib/python3.12/asyncio/tasks.py", line 519, in wait_for
    async with timeouts.timeout(timeout):
               ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/.local/share/uv/python/cpython-3.12.12-linux-x86_64-gnu/lib/python3.12/asyncio/timeouts.py", line 115, in __aexit__
    raise TimeoutError from exc_val
TimeoutError
2026-08-05 12:01:09,186 ERROR    29 LoggingWorker error: 
Traceback (most recent call last):
  File "/root/.local/share/uv/python/cpython-3.12.12-linux-x86_64-gnu/lib/python3.12/asyncio/tasks.py", line 520, in wait_for
    return await fut
           ^^^^^^^^^
  File "/root/.local/share/uv/python/cpython-3.12.12-linux-x86_64-gnu/lib/python3.12/asyncio/futures.py", line 289, in __await__
    yield self  # This tells Task to wait for completion.
    ^^^^^^^^^^
asyncio.exceptions.CancelledError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/ragflow/.venv/lib/python3.12/site-packages/litellm/litellm_core_utils/logging_worker.py", line 98, in _process_log_task
    await asyncio.wait_for(
  File "/root/.local/share/uv/python/cpython-3.12.12-linux-x86_64-gnu/lib/python3.12/asyncio/tasks.py", line 519, in wait_for
    async with timeouts.timeout(timeout):
               ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/.local/share/uv/python/cpython-3.12.12-linux-x86_64-gnu/lib/python3.12/asyncio/timeouts.py", line 115, in __aexit__
    raise TimeoutError from exc_val
TimeoutError
2026-08-05 12:01:09,187 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-05 12:01:09,188 INFO     29 [Trace] task=aeebe394 | doc=哮喘-HJCH222   2.27.pdf | Extractor:Admission | outputs={"chunks": "1 items, types={'AdmissionRecord': 1}", "html": "", "json": "1181 items", "markdown": "", "text": "", "name": "哮喘-HJCH222   2.27.pdf", "output_format": "chunks", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "route_summary": "{\"chunks_Examination\": 2, \"chunks_Clinical\": 3, \"chunks_Admission\": 1, \"chunks_Discharge\": 1}"}
2026-08-05 12:01:09,188 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-05 12:01:09,191 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 12:01:09,191 INFO     29 [qwen-vl-text] LLM output (len=426):
{
  "encounter_date": "2026-01-19",
  "pharmacy": "欣源药业",
  "medications": [
    {
      "name": "布地奈德福莫特罗吸入粉雾剂",
      "specification": "320ug:9ug*60吸/盒",
      "dosage": null,
      "quantity": 2,
      "unit_price": 309.00,
      "total_price": 618.00,
      "frequency": null,
      "route": null,
      "manufacturer": "阿斯利康",
      "approval_number": null
    }
  ],
  "payment_total": 618.00,
  "payment_method": null
}
2026-08-05 12:01:09,191 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-19]
2026-08-05 12:01:09,196 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2602355, prompt_len=887
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["欣源药业", "NO:2026011900323", "商品名称", "单价", "数量", "小计", "布地奈德福莫特罗吸入粉雾剂320ug:", "9ug*60吸/盒", "309.00", "2", "618.00", "阿斯利康", "批号: PKGF", "效期:2027-03 规格:1支/盒", "总计:", "2.00", "618.00", "会员卡号:800310", "会员姓名:", "本次积分:618.00", "累计积分:2518.10", "收银员004营业员004", "日期26-01-1910:53:22"]

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
2026-08-05 12:01:16,778 INFO     29 [qwen-vl-text] coord API raw response (len=1204):
[
	{"text": "欣源药业", "bbox": [408, 207, 636, 252]},
	{"text": "NO:2026011900323", "bbox": [148, 296, 502, 330]},
	{"text": "商品名称", "bbox": [148, 335, 327, 370],
	"bbox": [464, 340, 550, 374]},
	{"text": "单价", "bbox": [594, 341, 683, 374]},
	{"text": "小计", "bbox": [752, 341, 843, 374]},
	{"text": "布地奈德福莫特罗吸入粉雾剂320ug:", "bbox": [148, 417, 868, 454]},
	{"text": "9ug*60吸/盒", "bbox": [144, 460, 422, 494]},
	{"text": "309.00", "bbox": [485, 463, 621, 491]},
	{"text": "2", "bbox": [660, 464, 685, 491]},
	{"text": "618.00", "bbox": [752, 464, 895, 492]},
	{"text": "阿斯利康", "bbox": [144, 499, 324, 533]},
	{"text": "批号: PKGF", "bbox": [440, 501, 664, 533]},
	{"text": "效期:2027-03 规格:1支/盒", "bbox": [144, 539, 706, 574]},
	{"text": "总计:", "bbox": [144, 624, 247, 658]},
	{"text": "2.00", "bbox": [461, 626, 553, 654]},
	{"text": "618.00", "bbox": [672, 627, 811, 656]},
	{"text": "会员卡号:800310", "bbox": [144, 665, 498, 698]},
	{"text": "会员姓名:", "bbox": [144, 704, 338, 738]},
	{"text": "本次积分:618.00", "bbox": [142, 784, 498, 819]},
	{"text": "累计积分:2518.10", "bbox": [144, 827, 521, 861]},
	{"text": "收银员004营业员004", "bbox": [142, 865, 586, 899]},
	{"text": "日期26-01-1910:53:22", "bbox": [144, 907, 631, 937]}
]
2026-08-05 12:01:16,779 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=7.6s
2026-08-05 12:01:16,779 INFO     29 [qwen-vl-text] coord item[0]: text=欣源药业, bbox=[408, 207, 636, 252]
2026-08-05 12:01:16,779 INFO     29 [qwen-vl-text] coord item[1]: text=NO:2026011900323, bbox=[148, 296, 502, 330]
2026-08-05 12:01:16,779 INFO     29 [qwen-vl-text] coord item[2]: text=商品名称, bbox=[464, 340, 550, 374]
2026-08-05 12:01:16,779 INFO     29 [qwen-vl-text] coord item[3]: text=单价, bbox=[594, 341, 683, 374]
2026-08-05 12:01:16,780 INFO     29 [qwen-vl-text] coord item[4]: text=小计, bbox=[752, 341, 843, 374]
2026-08-05 12:01:16,780 INFO     29 [qwen-vl-text] coord item[5]: text=布地奈德福莫特罗吸入粉雾剂320ug:, bbox=[148, 417, 868, 454]
2026-08-05 12:01:16,780 INFO     29 [qwen-vl-text] coord item[6]: text=9ug*60吸/盒, bbox=[144, 460, 422, 494]
2026-08-05 12:01:16,780 INFO     29 [qwen-vl-text] coord item[7]: text=309.00, bbox=[485, 463, 621, 491]
2026-08-05 12:01:16,780 INFO     29 [qwen-vl-text] coord item[8]: text=2, bbox=[660, 464, 685, 491]
2026-08-05 12:01:16,780 INFO     29 [qwen-vl-text] coord item[9]: text=618.00, bbox=[752, 464, 895, 492]
2026-08-05 12:01:16,780 INFO     29 [qwen-vl-text] coord item[10]: text=阿斯利康, bbox=[144, 499, 324, 533]
2026-08-05 12:01:16,780 INFO     29 [qwen-vl-text] coord item[11]: text=批号: PKGF, bbox=[440, 501, 664, 533]
2026-08-05 12:01:16,780 INFO     29 [qwen-vl-text] coord item[12]: text=效期:2027-03 规格:1支/盒, bbox=[144, 539, 706, 574]
2026-08-05 12:01:16,780 INFO     29 [qwen-vl-text] coord item[13]: text=总计:, bbox=[144, 624, 247, 658]
2026-08-05 12:01:16,780 INFO     29 [qwen-vl-text] coord item[14]: text=2.00, bbox=[461, 626, 553, 654]
2026-08-05 12:01:16,780 INFO     29 [qwen-vl-text] coord item[15]: text=618.00, bbox=[672, 627, 811, 656]
2026-08-05 12:01:16,780 INFO     29 [qwen-vl-text] coord item[16]: text=会员卡号:800310, bbox=[144, 665, 498, 698]
2026-08-05 12:01:16,780 INFO     29 [qwen-vl-text] coord item[17]: text=会员姓名:, bbox=[144, 704, 338, 738]
2026-08-05 12:01:16,780 INFO     29 [qwen-vl-text] coord item[18]: text=本次积分:618.00, bbox=[142, 784, 498, 819]
2026-08-05 12:01:16,780 INFO     29 [qwen-vl-text] coord item[19]: text=累计积分:2518.10, bbox=[144, 827, 521, 861]
2026-08-05 12:01:16,780 INFO     29 [qwen-vl-text] coord item[20]: text=收银员004营业员004, bbox=[142, 865, 586, 899]
2026-08-05 12:01:16,781 INFO     29 [qwen-vl-text] coord item[21]: text=日期26-01-1910:53:22, bbox=[144, 907, 631, 937]
2026-08-05 12:01:16,781 INFO     29 [qwen-vl-text] page=4 — 23/23 coords, api_time=7.6s
2026-08-05 12:01:16,781 INFO     29 [qwen-vl-text] new_positions (23):
[[4, 242.76, 378.41999999999996, 174.29399999999998, 212.184], [4, 88.06, 298.69, 249.232, 277.86], [4, 276.08, 327.25, 286.28, 314.908], [4, 353.43, 406.385, 287.122, 314.908], [4, 447.44, 501.585, 287.122, 314.908], [4, 88.06, 516.4599999999999, 351.114, 382.268], [4, 85.67999999999999, 251.08999999999997, 387.32, 415.948], [4, 288.575, 369.495, 389.846, 413.42199999999997], [4, 392.7, 407.575, 390.688, 413.42199999999997], [4, 447.44, 532.525, 390.688, 414.264], [4, 85.67999999999999, 192.78, 420.15799999999996, 448.786], [4, 261.8, 395.08, 421.842, 448.786], [4, 85.67999999999999, 420.07, 453.83799999999997, 483.308], [4, 85.67999999999999, 146.965, 525.408, 554.036], [4, 274.295, 329.03499999999997, 527.092, 550.668], [4, 399.84, 482.54499999999996, 527.934, 552.352], [4, 85.67999999999999, 296.31, 559.93, 587.716], [4, 85.67999999999999, 201.10999999999999, 592.768, 621.396], [4, 84.49, 296.31, 660.1279999999999, 689.598], [4, 85.67999999999999, 309.995, 696.334, 724.962], [4, 84.49, 348.66999999999996, 728.3299999999999, 756.958], [4, 85.67999999999999, 375.445, 763.694, 788.954], [4, 85.67999999999999, 375.445, 763.694, 788.954]]
2026-08-05 12:01:16,781 INFO     29 [qwen-vl-text] ═══ DONE ═══ 23 positions, pages=1, time=95.8s
2026-08-05 12:01:16,781 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 12:01:16,782 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 12:01:16,782 INFO     29 [qwen-vl-text] positions(20): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 12:01:16,782 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [20]
2026-08-05 12:01:17,050 INFO     29 [qwen-vl-text] page=5, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 12:01:17,051 INFO     29 [qwen-vl-text] LLM extraction start, text_len=244
2026-08-05 12:01:17,051 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 12:01:17,052 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 142, \"bbox_end\": 161, \"encounter_dates\": [\"2026-02-13\"], \"department\": \"呼吸内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "内蒙古医科大学附属医院\n门诊缴费凭证\n诊疗号: 0011072747\n姓名:\n收费项目\n总额(元)\n西药\n301.53\n(取药窗口: 门诊二楼西药房3号窗口)\n开单科室: 呼吸内科门诊\n结算类型: 自费\n总金额: 301.53元\n实付金额: 301.53元\n机器编号: zzj217\n缴费时间: 2026-02-13 10:13:31\n支付方式: 微信\n交易订单号: 39N6260213101311FYAzzj217D4230\n温馨提示:\n如需发票, 请关注我院微信公众号获取\n电子发票",
    "role": "user"
  }
]
[92m12:01:17 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:01:17,053 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:01:17,060 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 12:01:17,060 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-05 12:01:17,060 INFO     29 [qwen-vl-text] positions(254): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 12:01:17,060 INFO     29 [qwen-vl-text] page grouping: [0, 1], lines per page: [253, 1]
2026-08-05 12:01:17,289 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1654x2339), dpi=200
2026-08-05 12:01:17,380 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1654x2339), dpi=200
2026-08-05 12:01:17,381 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1172
2026-08-05 12:01:17,381 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 12:01:17,382 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 0, \"bbox_end\": 253, \"encounter_dates\": [\"2025-06-09\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "临海市第一人民医院医共体\n肺功能报告\nCOSMED\n姓名:\n科室/床号:\n100004\nID:\n日期:\n2025/6/9\n预计值:\nERS 93\n出生日期: 1978/12/13\n性别: Male\n地区修正.: Chinese\n详细描述:\nCompany:\n年龄: 46\n体重 (Kg): 84.0\n身高 (cm): 178.0\nBMI (Kg/m²): 26.5\n吸烟: 否\n用力肺活量 Forced Vital Capacity\nF(l/s)\n14\n13\n12\n11\n10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n0\n-1\n-2\n-3\n-4\n-5\n-6\n-7\n-8\nV(l)\n8\n7\n6\n5\n4\n3\n2\n1\n0\n-1\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12t(s)\nFVC\nPEF\nMEF75%\nMEF50%\nMEF25%\nFVC\nV(l)\n8\n7\n6\n5\n4\n3\n2\n1\n0\n-1\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12t(s)\nFEV1\nATS\nFVC\nPEF\nMEF75%\nMEF50%\nMEF25%\nFVC\nV(l)\n8\n7\n6\n5\n4\n3\n2\n1\n0\n-1\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12t(s)\nParameter\nUM\nPred.\nBEST#1\n%Pred.\nPOST#3\n%Pred.\n%Test#1\nBest FVC\nl(btps)\n4.72\n2.74\n58\n3.22\n68\n+17.4\nFVC\nl(btps)\n4.72\n2.74\n58\n3.22\n68\n+17.4\nFEV1\nl(btps)\n3.83\n1.35\n35\n1.72\n45\n+27.5\nPEF\nl/sec\n9.10\n2.96\n32\n3.30\n36\n+11.4\nFEV6\nl(btps)\n5.01\n2.71\n54\n3.20\n64\n+18.2\nPIF\nl/sec\n4.61\n5.52\n+19.9\nFEV1/FVC%\n%\n78.9\n49.1\n62\n53.4\n68\n+8.7\nFEV6/FVC%\n%\n98.8\n99.5\n+0.7\nFEV1/FEV6%\n%\n49.7\n53.6\n+7.9\nFEF25-75%\nl/sec\n4.18\n0.64\n15\n0.86\n21\n+34.7\nMEF75%\nl/sec\n7.91\n1.42\n18\n1.98\n25\n+39.2\nMEF50%\nl/sec\n4.97\n0.75\n15\n1.02\n20\n+36.2\nMEF25%\nl/sec\n2.11\n0.31\n15\n0.41\n19\n+32.4\nFET100%\nsec\n6.2\n6.1\n-1.9\nVEXT\nml\n60\n73\n+21.7\nIC\nl(btps)\n2.47\n2.27\n-8.1\n诊断:\n支气管舒张试验阳性。\n签名:\n2025-03-16",
    "role": "user"
  }
]
[92m12:01:17 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:01:17,382 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:01:17,392 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 12:01:17,399 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-05 12:01:17,399 INFO     29 [Trace] task=b28be2ce | doc=麦济ZHYH.pdf | Parser:MedLink | outputs={"html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "json"}
2026-08-05 12:01:17,399 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-05 12:01:17,399 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-05 12:01:17,400 INFO     29 [Trace] task=aff34070 | doc=麦济WRNA(2).pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "304 items", "markdown": "", "text": "", "name": "麦济WRNA(2).pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Medication\": 5}"}
2026-08-05 12:01:17,400 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-05 12:01:17,417 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 12:01:17,418 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。只有主诉，病史的也属于OutpatientRecord（门诊病历）\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 内蒙古医科大学附属医院门诊病历\n[BBOX-1] 姓名：\n[BBOX-2] 年龄：62岁\n[BBOX-3] 诊疗号：0014498780\n[BBOX-4] 民族：\n[BBOX-5] 性别：男性\n[BBOX-6] 呼吸内科门诊\n[BBOX-7] 联系电话：\n[BBOX-8] 1\n[BBOX-9] 身份证：\n[BBOX-10] 病情：\n[BBOX-11] 就诊状态：\n[BBOX-12] 就诊时间：2026-02-13 09:14\n[BBOX-13] 生命体征（需要时）：\n[BBOX-14] 体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg\n[BBOX-15] 主诉：哮喘史，近3天呼吸困难加重，夜间咳嗽明显\n[BBOX-16] 现病史：哮喘史，近3天呼吸困难加重，夜间咳嗽明显\n[BBOX-17] 既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎\n[BBOX-18] 无，吸烟史无，无过敏史。\n[BBOX-19] 体格检查：发育正常，营养良好，体型正常，双肺呼吸音清，双肺未闻及啰\n[BBOX-20] 音，双下肢无水肿，体重kg。\n[BBOX-21] 辅助检查：心肺\n[BBOX-22] 过敏史：不详\n[BBOX-23] 初步诊断（西医）：1.支气管哮喘(急性发作期)\n[BBOX-24] 初步诊断（中医）：\n[BBOX-25] 治疗方案：随诊\n[BBOX-26] 醋酸泼尼松片<5mg>\n[BBOX-27] 用量：3.000片/次\n[BBOX-28] 用法：口服，一次/日，5天\n[BBOX-29] 签名：\n[BBOX-30] 萱堂大药房\n[BBOX-31] 单号：2025111853212\n[BBOX-32] 日期：25/11/18\n[BBOX-33] 时间：13:2\n[BBOX-34] 工号：001\n[BBOX-35] 品名\n[BBOX-36] 规格\n[BBOX-37] 厂家\n[BBOX-38] 金额\n[BBOX-39] 数量\n[BBOX-40] 总计\n[BBOX-41] 布地格福吸入气雾剂\n[BBOX-42] 60ug/7.2ug/4.8ug 吸\n[BBOX-43] 120 撤/支\n[BBOX-44] 支/盒\n[BBOX-45] 219.00\n[BBOX-46] 3\n[BBOX-47] 657.00\n[BBOX-48] 合计：657.00\n[BBOX-49] 应收：657.00\n[BBOX-50] 数量：3\n[BBOX-51] 实收：657.00\n[BBOX-52] 会员：\n[BBOX-53] 药品属于特殊商品\n[BBOX-54] 无质量问题，概不退换\n[BBOX-55] 电子发票(普通发票)\n[BBOX-56] 国家税务总局\n[BBOX-57] 江苏省税务局\n[BBOX-58] 发票号码：25322000000382591347\n[BBOX-59] 开票日期：2025年08月20日\n[BBOX-60] 购买方信息\n[BBOX-61] 名称：\n[BBOX-62] 统一社会信用代码/纳税人识别号：\n[BBOX-63] 销售方信息\n[BBOX-64] 名称：无锡邻医大药房有限公司\n[BBOX-65] 统一社会信用代码/纳税人识别号：91320214MA228F680W\n[BBOX-66] 项目名称\n[BBOX-67] 规格型号\n[BBOX-68] 单位\n[BBOX-69] 数量\n[BBOX-70] 单价\n[BBOX-71] 金额\n[BBOX-72] 税率/征收率\n[BBOX-73] 税额\n[BBOX-74] *化学药品制剂*倍择瑞令\n[BBOX-75] 160μg/7.2μg/4\n[BBOX-76] 盒\n[BBOX-77] 3\n[BBOX-78] 210.029498522124\n[BBOX-79] 630.09\n[BBOX-80] 13%\n[BBOX-81] 81.91\n[BBOX-82] 畅布地格福吸入气雾剂\n[BBOX-83] .8μg*120揿\n[BBOX-84] 合计\n[BBOX-85] ￥630.09\n[BBOX-86] ￥81.91\n[BBOX-87] 价税合计（大写）\n[BBOX-88] 柒佰壹拾贰圆整\n[BBOX-89] (小写) ￥712.00\n[BBOX-90] 备注\n[BBOX-91] 开票人：奚澳琼\n[BBOX-92] 电子发票(普通发票)\n[BBOX-93] 国家税务总局\n[BBOX-94] 江苏省税务局\n[BBOX-95] 发票号码：25322000000226700883\n[BBOX-96] 开票日期：2025年05月20日\n[BBOX-97] 购买方信息\n[BBOX-98] 名称\n[BBOX-99] 统一社会信用代码/纳税人识别号：\n[BBOX-100] 销售方信息\n[BBOX-101] 名称：无锡邻医大药房有限公司\n[BBOX-102] 统一社会信用代码/纳税人识别号：91320214MA228F680W\n[BBOX-103] 项目名称\n[BBOX-104] 规格型号\n[BBOX-105] 单位\n[BBOX-106] 数量\n[BBOX-107] 单价\n[BBOX-108] 金额\n[BBOX-109] 税率/征收率\n[BBOX-110] 税额\n[BBOX-111] *化学药品制剂*倍择瑞令\n[BBOX-112] 160μg/7.2μg/4\n[BBOX-113] 盒\n[BBOX-114] 3 210.029498522124\n[BBOX-115] 630.09\n[BBOX-116] 13%\n[BBOX-117] 81.91\n[BBOX-118] 畅布地格福吸入气雾剂\n[BBOX-119] .8μg*120揿\n[BBOX-120] 合计\n[BBOX-121] ￥630.09\n[BBOX-122] ￥81.91\n[BBOX-123] 价税合计（大写）\n[BBOX-124] 柒佰壹拾贰圆整\n[BBOX-125] (小写）￥712.00\n[BBOX-126] 备注\n[BBOX-127] 挂号号:D20091... 医保余额:0 CM/KG 普通病人|现住址:内蒙古土默特左旗沙尔营乡大有庄村32\n[BBOX-128] 报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录:\n[BBOX-129] 病历信息 □痕迹 □批注 置未 ▼ 状态:只读-仅供查看 120% >\n[BBOX-130] 内蒙古医科大学附属医院门诊病历\n[BBOX-131] 姓名 龄:60岁 诊疗号:0014498780\n[BBOX-132] 民族: 别:男性 科室:呼吸内科门诊\n[BBOX-133] 联系电话: 身份证:1 病情:\n[BBOX-134] 就诊状态: 就诊时间:2024-12-10 12:37\n[BBOX-135] 生命体征(需要时):\n[BBOX-136] 体温:℃ 脉搏:次/分 呼吸:次/分 血压:/mmHg\n[BBOX-137] 主诉:SSSJ项目肺功能检查开单\n[BBOX-138] 现病史:哮喘\n[BBOX-139] 既往史:患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎\n[BBOX-140] 无,吸烟史无,无过敏史。\n[BBOX-141] 体格检查:发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰\n[BBOX-142] 音,双下肢无水肿,体重kg。\n[BBOX-143] 辅助检查:\n[BBOX-144] 初步诊断(西医):1.哮喘\n[BBOX-145] 初步诊断(中医):\n[BBOX-146] 治疗方案:/\n[BBOX-147] 呼吸过滤器 肺通气功能检查\n[BBOX-148] 用量:\n[BBOX-149] 用法:\n[BBOX-150] 签名:崔丽英\n[BBOX-151] 3:34 星期二 190.1.48.233 版本 王立红\n[BBOX-152] 电子发票(普通发票)\n[BBOX-153] 国家税务总局\n[BBOX-154] 内蒙古自治区税务局\n[BBOX-155] 发票号码：26152000000119478346\n[BBOX-156] 开票日期：2026年02月09日\n[BBOX-157] 购买方信息\n[BBOX-158] 名称\n[BBOX-159] 统一社会信用代码/纳税人识别号：\n[BBOX-160] 销售方信息\n[BBOX-161] 名称：国药控股国大药房内蒙古有限公司\n[BBOX-162] 统一社会信用代码/纳税人识别号：911501005732872139\n[BBOX-163] 项目名称\n[BBOX-164] 规格型号\n[BBOX-165] 单位\n[BBOX-166] 数量\n[BBOX-167] 单价\n[BBOX-168] 金额\n[BBOX-169] 税率/征收率\n[BBOX-170] 税额\n[BBOX-171] *化学药品制剂*布地格福\n[BBOX-172] 160ug:7.2ug/4.8u\n[BBOX-173] 盒\n[BBOX-174] 3\n[BBOX-175] 237.16814159292\n[BBOX-176] 711.50\n[BBOX-177] 13%\n[BBOX-178] 92.50\n[BBOX-179] 吸入气雾剂\n[BBOX-180] g:120揿\n[BBOX-181] *化学药品制剂*布地格福\n[BBOX-182] 160ug:7.2ug/4.8u\n[BBOX-183] 盒\n[BBOX-184] 3\n[BBOX-185] 237.16814159292\n[BBOX-186] 711.50\n[BBOX-187] 13%\n[BBOX-188] 92.50\n[BBOX-189] 吸入气雾剂\n[BBOX-190] g:120揿\n[BBOX-191] 合计\n[BBOX-192] ￥1423.00\n[BBOX-193] ￥185.00\n[BBOX-194] 价税合计（大写）\n[BBOX-195] 壹仟陆佰零捌圆整\n[BBOX-196] (小写) ￥1608.00\n[BBOX-197] 备注\n[BBOX-198] 开票人：刘惠"
  }
]
2026-08-05 12:01:17,423 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 12:01:17,424 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-05 12:01:17,985 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 12:01:17,992 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-05 12:01:17,992 INFO     29 [Trace] task=aff34070 | doc=麦济WRNA(2).pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "304 items", "markdown": "", "text": "", "name": "麦济WRNA(2).pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Medication\": 5}"}
2026-08-05 12:01:17,992 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-05 12:01:17,997 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 12:01:17,997 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m12:01:17 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:01:17,998 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:01:18,872 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 12:01:18,872 INFO     29 [qwen-vl-text] LLM output (len=139):
{
  "encounter_date": "2026-02-13",
  "pharmacy": "门诊二楼西药房3号窗口",
  "medications": [],
  "payment_total": 301.53,
  "payment_method": "微信"
}
2026-08-05 12:01:18,872 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-13]
2026-08-05 12:01:18,876 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1773307, prompt_len=917
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共20行）
["内蒙古医科大学附属医院", "门诊缴费凭证", "诊疗号: 0011072747", "姓名:", "收费项目", "总额(元)", "西药", "301.53", "(取药窗口: 门诊二楼西药房3号窗口)", "开单科室: 呼吸内科门诊", "结算类型: 自费", "总金额: 301.53元", "实付金额: 301.53元", "机器编号: zzj217", "缴费时间: 2026-02-13 10:13:31", "支付方式: 微信", "交易订单号: 39N6260213101311FYAzzj217D4230", "温馨提示:", "如需发票, 请关注我院微信公众号获取", "电子发票"]

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
2026-08-05 12:01:26,054 INFO     29 [qwen-vl-text] coord API raw response (len=1123):
[
	{"text": "内蒙古医科大学附属医院", "bbox": [292, 14, 807, 47]},
	{"text": "门诊缴费凭证", "bbox": [402, 43, 626, 67]},
	{"text": "诊疗号: 0011072747", "bbox": [252, 280, 554, 311]},
	{"text": "姓名:", "bbox": [255, 327, 360, 360]},
	{"text": "收费项目", "bbox": [255, 388, 391, 417]},
	{"text": "总额(元)", "bbox": [691, 385, 812, 417]},
	{"text": "西药", "bbox": [255, 428, 317, 454]},
	{"text": "301.53", "bbox": [688, 430, 782, 452]},
	{"text": "(取药窗口: 门诊二楼西药房3号窗口)", "bbox": [268, 457, 807, 485]},
	{"text": "开单科室: 呼吸内科门诊", "bbox": [255, 496, 620, 522]},
	{"text": "结算类型: 自费", "bbox": [255, 557, 500, 584]},
	{"text": "总金额: 301.53元", "bbox": [255, 596, 551, 622]},
	{"text": "实付金额: 301.53元", "bbox": [255, 635, 551, 661]},
	{"text": "机器编号: zzj217", "bbox": [255, 687, 515, 715]},
	{"text": "缴费时间: 2026-02-13 10:13:31", "bbox": [255, 719, 698, 744]},
	{"text": "支付方式: 微信", "bbox": [255, 747, 491, 774]},
	{"text": "交易订单号: 39N6260213101311FYAzzj217D4230", "bbox": [255, 778, 741, 798]},
	{"text": "温馨提示:", "bbox": [255, 834, 394, 859]},
	{"text": "如需发票, 请关注我院微信公众号获取", "bbox": [255, 871, 790, 898]},
	{"text": "电子发票", "bbox": [255, 909, 381, 933]}
]
2026-08-05 12:01:26,054 INFO     29 [qwen-vl-text] coord API: raw_items=20, valid_items=20, elapsed=7.2s
2026-08-05 12:01:26,055 INFO     29 [qwen-vl-text] coord item[0]: text=内蒙古医科大学附属医院, bbox=[292, 14, 807, 47]
2026-08-05 12:01:26,055 INFO     29 [qwen-vl-text] coord item[1]: text=门诊缴费凭证, bbox=[402, 43, 626, 67]
2026-08-05 12:01:26,055 INFO     29 [qwen-vl-text] coord item[2]: text=诊疗号: 0011072747, bbox=[252, 280, 554, 311]
2026-08-05 12:01:26,055 INFO     29 [qwen-vl-text] coord item[3]: text=姓名:, bbox=[255, 327, 360, 360]
2026-08-05 12:01:26,055 INFO     29 [qwen-vl-text] coord item[4]: text=收费项目, bbox=[255, 388, 391, 417]
2026-08-05 12:01:26,055 INFO     29 [qwen-vl-text] coord item[5]: text=总额(元), bbox=[691, 385, 812, 417]
2026-08-05 12:01:26,055 INFO     29 [qwen-vl-text] coord item[6]: text=西药, bbox=[255, 428, 317, 454]
2026-08-05 12:01:26,055 INFO     29 [qwen-vl-text] coord item[7]: text=301.53, bbox=[688, 430, 782, 452]
2026-08-05 12:01:26,055 INFO     29 [qwen-vl-text] coord item[8]: text=(取药窗口: 门诊二楼西药房3号窗口), bbox=[268, 457, 807, 485]
2026-08-05 12:01:26,055 INFO     29 [qwen-vl-text] coord item[9]: text=开单科室: 呼吸内科门诊, bbox=[255, 496, 620, 522]
2026-08-05 12:01:26,055 INFO     29 [qwen-vl-text] coord item[10]: text=结算类型: 自费, bbox=[255, 557, 500, 584]
2026-08-05 12:01:26,055 INFO     29 [qwen-vl-text] coord item[11]: text=总金额: 301.53元, bbox=[255, 596, 551, 622]
2026-08-05 12:01:26,055 INFO     29 [qwen-vl-text] coord item[12]: text=实付金额: 301.53元, bbox=[255, 635, 551, 661]
2026-08-05 12:01:26,055 INFO     29 [qwen-vl-text] coord item[13]: text=机器编号: zzj217, bbox=[255, 687, 515, 715]
2026-08-05 12:01:26,055 INFO     29 [qwen-vl-text] coord item[14]: text=缴费时间: 2026-02-13 10:13:31, bbox=[255, 719, 698, 744]
2026-08-05 12:01:26,055 INFO     29 [qwen-vl-text] coord item[15]: text=支付方式: 微信, bbox=[255, 747, 491, 774]
2026-08-05 12:01:26,055 INFO     29 [qwen-vl-text] coord item[16]: text=交易订单号: 39N6260213101311FYAzzj217D4230, bbox=[255, 778, 741, 798]
2026-08-05 12:01:26,055 INFO     29 [qwen-vl-text] coord item[17]: text=温馨提示:, bbox=[255, 834, 394, 859]
2026-08-05 12:01:26,055 INFO     29 [qwen-vl-text] coord item[18]: text=如需发票, 请关注我院微信公众号获取, bbox=[255, 871, 790, 898]
2026-08-05 12:01:26,055 INFO     29 [qwen-vl-text] coord item[19]: text=电子发票, bbox=[255, 909, 381, 933]
2026-08-05 12:01:26,056 INFO     29 [qwen-vl-text] page=5 — 20/20 coords, api_time=7.2s
2026-08-05 12:01:26,056 INFO     29 [qwen-vl-text] new_positions (20):
[[5, 173.73999999999998, 480.16499999999996, 11.788, 39.574], [5, 239.19, 372.46999999999997, 36.205999999999996, 56.414], [5, 149.94, 329.63, 235.76, 261.86199999999997], [5, 151.725, 214.2, 275.334, 303.12], [5, 151.725, 232.64499999999998, 326.69599999999997, 351.114], [5, 411.145, 483.14, 324.17, 351.114], [5, 151.725, 188.61499999999998, 360.376, 382.268], [5, 409.35999999999996, 465.28999999999996, 362.06, 380.584], [5, 159.45999999999998, 480.16499999999996, 384.794, 408.37], [5, 151.725, 368.9, 417.632, 439.524], [5, 151.725, 297.5, 468.99399999999997, 491.728], [5, 151.725, 327.84499999999997, 501.832, 523.7239999999999], [5, 151.725, 327.84499999999997, 534.67, 556.562], [5, 151.725, 306.425, 578.454, 602.03], [5, 151.725, 415.31, 605.398, 626.448], [5, 151.725, 292.145, 628.9739999999999, 651.708], [5, 151.725, 440.895, 655.076, 671.9159999999999], [5, 151.725, 234.42999999999998, 702.228, 723.278], [5, 151.725, 470.04999999999995, 733.382, 756.116], [5, 151.725, 226.695, 765.3779999999999, 785.586]]
2026-08-05 12:01:26,056 INFO     29 [qwen-vl-text] ═══ DONE ═══ 20 positions, pages=1, time=9.3s
2026-08-05 12:01:26,065 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-05 12:01:26,065 INFO     29 [Trace] task=b1a9baa2 | doc=麦济ZHGL.pdf | Extractor:Medication | outputs={"chunks": "3 items, types={'MedicationRecord': 3}", "html": "", "json": "162 items", "markdown": "", "text": "", "name": "麦济ZHGL.pdf", "output_format": "chunks", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "route_summary": "{\"chunks_Medication\": 3, \"chunks_Clinical\": 2}"}
2026-08-05 12:01:26,066 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-05 12:01:26,068 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 12:01:26,079 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 12:01:26,079 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m12:01:26 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:01:26,080 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:01:26,082 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 12:01:26,095 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-05 12:01:26,095 INFO     29 [Trace] task=aff34070 | doc=麦济WRNA(2).pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "304 items", "markdown": "", "text": "", "name": "麦济WRNA(2).pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Medication\": 5}"}
2026-08-05 12:01:26,095 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-05 12:01:26,096 INFO     29 [ChunkMerger] Merged 9 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 4, 'Extractor:Medication': 5, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1} (filtered 6 noise chunks)
2026-08-05 12:01:26,106 INFO     29 [SmartSplitter] SmartSplitter done: 6 chunks from 6 LLM segments (all bbox_id). Types: {'OutpatientRecord': 2, 'MedicationRecord': 4}
2026-08-05 12:01:26,115 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-05 12:01:26,115 INFO     29 [Trace] task=aff34070 | doc=麦济WRNA(2).pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "9 items, types={'OutpatientRecord': 4, 'MedicationRecord': 5}", "name": "麦济WRNA(2).pdf"}
2026-08-05 12:01:26,115 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-05 12:01:26,185 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1785931158758, 'update_date': datetime.datetime(2026, 8, 5, 11, 59, 18), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 366527, 'status': '1'}
2026-08-05 12:01:26,415 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=内蒙古医科大学附属医院门诊病历
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
用法：口服，三次/日，7天
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
既往史：患者平素身体健康，高血压无，腰痛病无，心脏病无，肺结核无，鼻炎
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
号号:D20214...医保余额:3631.8 CM/KG 普通病人|现住址:内蒙古自治区呼和浩特市赛罕区
报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录:
□痕迹 □批注
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
就诊时间:2023-03-04 10:51
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
签名:付丹
---
26 星期二
190.1.48.233
王王立
内蒙古自治区国际蒙医医院
门诊病历
门诊号：2602120916
姓
科室：呼吸与危重症医学科门诊
性别：女性
出生年月：1971-11-18
就诊时间：2026-02-12 11:20
○初诊◎复诊
过敏史：□否 □不详 □有：
主诉：发作性咳嗽、气短5年，加重3天
现病史：5年前出现发作性咳嗽、气短，吸入刺激性气味后症状明显，就诊于当地医院诊断
为“支气管哮喘”，长期规律吸入信必可治疗后效果欠佳。近3天喘息加重，伴咳嗽、咳痰较前
频繁。夜间明显。
既往史：体健
家族史：无
体格检查：意识：清醒
T：36.5℃
P：71次/分
R：18次/分
BP：115/77mmHg
双肺可闻及干鸣音
辅助检查：
处方信息：
布地奈德福莫特罗吸入粉雾剂（II）(160μg/4.5μg/吸*60吸/支)*1支
320μg
吸入
bid
醋酸泼尼松片(5mg*100片/瓶)*1瓶
15mg
口服
qd
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
320 μg /9 μg /吸 60 吸/支
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
×
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
信
9506
医保基金支付：101.92
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
复核人：李姹娜
收款人：李姹娜
---
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
2026-08-05 12:01:26,415 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-05 12:01:26,415 INFO     29 [Trace] task=b28be2ce | doc=麦济ZHYH.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 2, 'MedicationRecord': 4}"}
2026-08-05 12:01:26,415 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-05 12:01:26,423 INFO     29 [ChunkRouter] Routed 6 chunks into 2 groups: {'chunks_Clinical': 2, 'chunks_Medication': 4}
2026-08-05 12:01:26,455 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-05 12:01:26,455 INFO     29 [Trace] task=b28be2ce | doc=麦济ZHYH.pdf | ChunkRouter:Router | outputs={"html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 2, 'MedicationRecord': 4}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-05 12:01:26,455 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-05 12:01:26,461 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 12:01:26,461 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m12:01:26 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:01:26,462 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:01:26,708 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 12:01:26,714 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-05 12:01:26,714 INFO     29 [Trace] task=b1a9baa2 | doc=麦济ZHGL.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "162 items", "markdown": "", "text": "", "name": "麦济ZHGL.pdf", "output_format": "chunks", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "route_summary": "{\"chunks_Medication\": 3, \"chunks_Clinical\": 2}"}
2026-08-05 12:01:26,714 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-05 12:01:26,719 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 12:01:26,719 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m12:01:26 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:01:26,720 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:01:26,930 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-05 12:01:26,931 INFO     29 [Trace] task=aff34070 | doc=麦济WRNA(2).pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "9 items, types={'OutpatientRecord': 4, 'MedicationRecord': 5}", "name": "麦济WRNA(2).pdf", "embedding_token_consumption": 2897}
2026-08-05 12:01:26,931 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-05 12:01:27,082 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-05 12:01:27,082 INFO     29 [Trace] task=aff34070 | doc=麦济WRNA(2).pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":9,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-05 12:01:27,090 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:01:27,090 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:01:27,090 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:01:27,090 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:01:27,090 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:01:27,090 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:01:27,090 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:01:27,090 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:01:27,091 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:01:27,098 INFO     29 set_progress(aff3407090be11f1a3da71efcdd7cc1f), progress: 0.82, progress_msg: 12:01:27 [DOC Engine]:
Start to index...
2026-08-05 12:01:27,127 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.022s]
2026-08-05 12:01:27,133 INFO     29 set_progress(aff3407090be11f1a3da71efcdd7cc1f), progress: 0.8111111111111111, progress_msg: 
2026-08-05 12:01:27,162 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.016s]
2026-08-05 12:01:27,177 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.010s]
2026-08-05 12:01:27,188 INFO     29 set_progress(aff3407090be11f1a3da71efcdd7cc1f), progress: 1.0, progress_msg: 12:01:27 Indexing done (0.09s). Task done (958.44s)
2026-08-05 12:01:27,192 INFO     29 [Done], chunks(9), token(2897), elapsed:958.44
2026-08-05 12:01:27,327 INFO     29 handle_task done for task {"id": "aff3407090be11f1a3da71efcdd7cc1f", "doc_id": "af8df0da90be11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eWRNA(2).pdf", "type": "pdf", "location": "\u9ea6\u6d4eWRNA(2).pdf", "size": 13028582, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1785928409538, "task_type": "dataflow", "root_trace_id": "a5accc15990a4c4988975b37b8223be2", "root_traceparent": "00-a5accc15990a4c4988975b37b8223be2-e1a2a450add9e6ea-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-05 12:01:27,372 INFO     29 [DEBUG-COLLECT] got redis_msg, msg_id=1785928648863-0
2026-08-05 12:01:27,372 INFO     29 [DEBUG-COLLECT] msg keys=['id', 'doc_id', 'from_page', 'to_page', 'task_type', 'priority', 'begin_at', 'create_time', 'create_date', 'update_time', 'update_date', 'root_trace_id', 'root_traceparent', 'trace_source', 'kb_id', 'tenant_id', 'dataflow_id', 'file'], task_type=dataflow, id=3e98f84c90bf11f1a3da71efcdd7cc1f
2026-08-05 12:01:27,372 INFO     29 [DEBUG-COLLECT] normal branch, calling TaskService.get_task(3e98f84c90bf11f1a3da71efcdd7cc1f)
2026-08-05 12:01:27,376 INFO     29 [DEBUG-COLLECT] get_task returned: <class 'dict'>, is_none=False
2026-08-05 12:01:27,377 INFO     29 handle_task begin for task {"id": "3e98f84c90bf11f1a3da71efcdd7cc1f", "doc_id": "3543a40e90bf11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "XALI\u9ea6\u6d4e\u65b0\u4e61 2026-03-06 17.04 (1).pdf", "type": "pdf", "location": "XALI\u9ea6\u6d4e\u65b0\u4e61 2026-03-06 17.04 (1).pdf", "size": 161316076, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785928648860, "task_type": "dataflow", "root_trace_id": "011798f1ac614ad79dfcf6d230b3fd04", "root_traceparent": "00-011798f1ac614ad79dfcf6d230b3fd04-a0d937a531746558-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-05 12:01:27,577 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-05 12:01:27,621 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-05 12:01:27,822 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 12:01:27,823 INFO     29 [qwen-vl-text] LLM output (len=2084):
{
  "exam_date": "2026-02-09",
  "report_date": null,
  "exam_name": "肺功能试验",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": "张四彩",
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "| 指标 | Pred | A1 | A1/Pd | P1 | A2/Pd | chg%l | P2 | A3/Pd | chg%2 | P3 | A4/Pd | chg%3 |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n| FVC [L] | 2.99 | 2.21 | 74.0 | 2.63 | 87.9 | 18.72 | 2.04 | 88.2 | 19.17 | 2.67 | 86.0 | 16.23 |\n| FEV 1 [L] | 2.67 | 1.25 | 48.6 | 1.62 | 69.2 | 21.85 | 1.84 | 69.8 | 23.23 | 1.60 | 68.4 | 20.23 |\n| FEV 1 % FVC [%] | 84.19 | 56.48 | 67.1 | 67.97 | 68.9 | 2.64 | 68.40 | 69.4 | 3.41 | 68.42 | 69.4 | 3.44 |\n| FEV 1 % VC MAX [%] | 81.88 | 65.26 | 67.6 | 67.97 | 70.8 | 4.91 | 68.40 | 71.3 | 6.70 | 68.42 | 71.4 | 5.73 |\n| VC MAX [L] | 3.03 | 2.26 | 74.6 | 2.63 | 86.6 | 16.14 | 2.64 | 87.0 | 16.69 | 2.57 | 84.8 | 13.71 |\n| PEF [L/s] | 6.28 | 2.66 | 42.4 | 2.90 | 46.2 | 9.17 | 3.37 | 53.7 | 26.79 | 3.42 | 64.6 | 28.64 |\n| MMEF 75/25 [L/s] | 3.57 | 0.61 | 14.4 | 0.67 | 18.8 | 31.03 | 0.73 | 20.4 | 42.01 | 0.69 | 19.4 | 35.02 |\n| MEF 50 [L/s] | 4.01 | 0.68 | 17.0 | 0.90 | 22.5 | 32.75 | 0.89 | 22.1 | 30.15 | 0.88 | 21.9 | 29.17 |\n| MEF 25 [L/s] | 1.79 | 0.19 | 10.5 | 0.27 | 15.2 | 44.16 | 0.33 | 18.7 | 77.66 | 0.31 | 17.6 | 66.49 |\n| FET [s] | 7.63 | 8.01 | | 4.99 | | | 7.79 | | 2.14 | 7.43 | | -2.60 |\n| V backextrapolation ex [L] | 0.05 | 0.04 | -11.67 | 0.04 | -18.64 | | 0.04 | -13.51 | | | | |\n| PIF [L/s] | 3.04 | 3.37 | 10.91 | 3.51 | 15.70 | | 3.60 | 18.67 | | | | |\n| FIV1 [L] | 2.21 | 2.56 | 15.71 | 2.56 | 15.66 | | 2.50 | 13.09 | | | | |\n| PEF50 % FIF50 [%] | 22.86 | 28.15 | 23.14 | 25.36 | 10.95 | | 27.28 | 19.33 | | | | |\n| MVV [L/min] | 99.77 | 46.21 | 46.3 | | | | | | | | | |\n| BF MVV [1/min] | 75.55 | 10 | | | | | | | | | | |",
  "conclusion": "1. 中重度阻塞性肺通气功能障碍。\n2. 支气管舒张试验阳性。\n(1. 24h内无支气管舒张药物使用史)\n(2. 吸入万托林气雾剂400ug15分钟后，FEV1和FVC上升≥12%，绝对值增加≥200ml)\n(3. 检查质量：舒张前：A级；舒张后：A级)",
  "physician": null,
  "reviewer": null
}
2026-08-05 12:01:27,824 INFO     29 [qwen-vl-text] coord API call start, page=16, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=658017, prompt_len=616
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["张"]

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
2026-08-05 12:01:27,831 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-05 12:01:27,831 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-05 12:01:27,840 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-05 12:01:27,840 INFO     29 ============================================================
2026-08-05 12:01:27,840 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-05 12:01:27,840 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-05 12:01:27,840 INFO     29 ============================================================
2026-08-05 12:01:27,840 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-05 12:01:27,841 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-05 12:01:27,842 INFO     29 No torch found.
2026-08-05 12:01:28,547 INFO     29 [qwen-vl-text] coord API raw response (len=60):
```json
[
	{"text": "张", "bbox": [879, 875, 930, 897]}
]
```
2026-08-05 12:01:28,552 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=0.7s
2026-08-05 12:01:28,552 INFO     29 [qwen-vl-text] coord item[0]: text=张, bbox=[879, 875, 930, 897]
2026-08-05 12:01:28,552 INFO     29 [qwen-vl-text] page=16 — 1/1 coords, api_time=0.7s
2026-08-05 12:01:28,553 INFO     29 [qwen-vl-text] coord API call start, page=17, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=864636, prompt_len=2834
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共254行）
["肺功能试验报告", "姓名：", "年龄：38岁", "性别：女", "科别：", "保险：", "预计值模式：Standard-new", "测试号：2026020017", "身高：166 cm", "体重：60 kg", "备注：", "联系电话：", "操作者：蒋细萍", "Pred", "A1 A1/Pd", "P1 A2/Pd", "chg%l", "P2 A3/Pd", "chg%2", "P3 A4/Pd", "chg%3", "FVC", "[L]", "2.99", "2.21", "74.0", "2.63", "87.9", "18.72", "2.04", "88.2", "19.17", "2.67", "86.0", "16.23", "FEV 1", "[L]", "2.67", "1.25", "48.6", "1.62", "69.2", "21.85", "1.84", "69.8", "23.23", "1.60", "68.4", "20.23", "FEV 1 % FVC", "[%]", "84.19", "56.48", "67.1", "67.97", "68.9", "2.64", "68.40", "69.4", "3.41", "68.42", "69.4", "3.44", "FEV 1 % VC MAX", "[%]", "81.88", "65.26", "67.6", "67.97", "70.8", "4.91", "68.40", "71.3", "6.70", "68.42", "71.4", "5.73", "VC MAX", "[L]", "3.03", "2.26", "74.6", "2.63", "86.6", "16.14", "2.64", "87.0", "16.69", "2.57", "84.8", "13.71", "PEF", "[L/s]", "6.28", "2.66", "42.4", "2.90", "46.2", "9.17", "3.37", "53.7", "26.79", "3.42", "64.6", "28.64", "MMEF 75/25", "[L/s]", "3.57", "0.61", "14.4", "0.67", "18.8", "31.03", "0.73", "20.4", "42.01", "0.69", "19.4", "35.02", "MEF 50", "[L/s]", "4.01", "0.68", "17.0", "0.90", "22.5", "32.75", "0.89", "22.1", "30.15", "0.88", "21.9", "29.17", "MEF 25", "[L/s]", "1.79", "0.19", "10.5", "0.27", "15.2", "44.16", "0.33", "18.7", "77.66", "0.31", "17.6", "66.49", "FET", "[s]", "7.63", "8.01", "4.99", "7.79", "2.14", "7.43", "-2.60", "V backextrapolation ex [L]", "0.05", "0.04", "-11.67", "0.04", "-18.64", "0.04", "-13.51", "PIF", "[L/s]", "3.04", "3.37", "10.91", "3.51", "15.70", "3.60", "18.67", "FIV1", "[L]", "2.21", "2.56", "15.71", "2.56", "15.66", "2.50", "13.09", "PEF50 % FIF50", "[%]", "22.86", "28.15", "23.14", "25.36", "10.95", "27.28", "19.33", "MVV", "[L/min]", "99.77", "46.21", "46.3", "BF MVV", "[1/min]", "75.55", "10", "Flow [L/s]", "F/V ex", "1", "2", "3", "4", "6", "4", "2", "0", "Vol [L]", "1", "2", "3", "4", "5", "2", "4", "6", "8", "10", "F/V In", "Vol%VCmax", "0", "0", "Vol [L]", "20", "40", "60", "80", "100", "1", "2", "VCmax", "3", "4", "5", "6", "Time [s]", "0", "2", "4", "6", "8", "10", "12", "14", "意见：", "1. 中重度阻塞性肺通气功能障碍。", "2. 支气管舒张试验阳性。", "(1. 24h内无支气管舒张药物使用史)", "(2. 吸入万托林气雾剂400ug15分钟后，FEV1和FVC上升≥12%，绝对值增加≥200ml)", "(3. 检查质量：舒张前：A级；舒张后：A级)", "张四彩"]

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
2026-08-05 12:01:32,563 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=27
2026-08-05 12:01:32,946 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6860007, prompt_len=764
2026-08-05 12:01:35,156 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-12-24"}
```
2026-08-05 12:01:35,158 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2024-12-24
2026-08-05 12:01:35,184 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6860007, prompt_len=401
2026-08-05 12:01:39,397 INFO     29 [qwen-vl-parser] text API response (len=518):
["门(急)诊初诊病历", "姓名：", "性别：女性", "年龄：66岁", "门诊号：202300464183", "就诊时间：2024-12-24 10:00", "科别：呼吸与危重症一科门诊", "婚姻：已婚", "职业：退(离)休人员", "证件号码：", "电话", "工作单位或住址：/新乡", "主诉：反复咳嗽喘30余年", "现病史：反复咳嗽喘30余年", "既往史：有“高血压病”病史。", "过敏史：无", "流行病学史：无疫区流行病学史", "家族史：无", "体格检查：36.8°C；P:72次/min；R:20次/min；BP:130/70mmHg，双肺呼吸音粗，两肺未闻及干湿", "性啰音。辅助检查结果：无", "发病日期：2024-07-06", "诊断：支气管哮喘(慢性持续期)", "诊疗意见：1.乌美溴铵维兰特罗吸入粉雾剂，30吸×1盒/盒、1吸、吸入、QD（每日一次），30天、1盒、", "2024-12-24 10:03；", "2.醋酸泼尼松片，5mg*100片/瓶、10.5mg、口服、BID（每日两次）、23天、100片、2024-12-24", "10:17；", "医师签名："]
2026-08-05 12:01:39,400 INFO     29 [qwen-vl-parser] page=1 text: 27 lines (bbox 0-26)
2026-08-05 12:01:39,400 INFO     29 [qwen-vl-parser] page=1 text: 27 sections
2026-08-05 12:01:39,813 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7891833, prompt_len=764
2026-08-05 12:01:41,927 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 12:01:41,929 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-05 12:01:41,955 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7891833, prompt_len=401
2026-08-05 12:01:50,628 INFO     29 [qwen-vl-parser] text API response (len=1073):
["门诊病历", "姓名：", "性别：女", "年龄：67岁", "婚否：已婚", "民族：汉族", "职业：退（离）休人员", "身份证号", "邮", "编：453000", "籍贯：河南省新乡", "现住址：河南省", "市", "号", "X线号：无", "工作单位：不详", "联系电", "心电图号：", "无", "初诊科别：呼吸一科", "初诊日期：2026-01-04", "过敏史：无", "主诉：反复咳嗽喘6年余，再发10余天。", "现病史：6年余来患者每遇吸入刺激性气味或冷空气后出现咳嗽、咳痰及胸闷、气", "喘，咳嗽咳痰症状呈阵发性发作，痰液易咳出，多为白粘痰，不伴发热，不伴胸痛，无夜", "间阵发性呼吸困难及端坐呼吸，每次症状发作时多就诊于我院呼吸内科，曾完善肺功能检", "查确诊为“支气管哮喘”，经抗感染、抗炎、解痉平喘、雾化吸入及对症治疗后症状好转", "出院，出院后院外规律吸入“布地格福气雾剂2揿/次，一日两次”治疗，胸闷、气喘症", "状控制不佳，活动耐力呈进行性下降（以致目前上2层楼或步行500米左右即气喘严重），3", "月余前患者因受凉再次出现咳嗽、咳痰、胸闷、气喘，在家应用“布地格福气雾剂”吸入", "治疗及口服“罗红霉素胶囊7天及甲泼尼龙片8mg/次，一日两次，间隔1-2天每日减1", "片”治疗，咳嗽咳痰及胸闷、气喘症状有所好转后停用上述口服药物，后改为应用“布地", "奈德气雾剂2揿/次，一日三次联合乌美溴铵维兰特罗粉雾剂1吸/次，一日一次”联合维持", "治疗。10余天前患者无诱因再次出现咳嗽、咳痰、胸闷、气喘，不伴发热，在家应用“布", "地奈德气雾剂2揿/次，一日三次联合乌美溴铵维兰特罗粉雾剂1吸/次，一日一次”吸入治", "疗及再次口服“罗红霉素胶囊7天及甲泼尼龙片8mg/次，一日两次，间隔1-2天每日减1", "片”治疗10余天来咳嗽咳痰及胸闷、气喘症状未见好转，为求诊治故来我院就诊，门诊以", "“支气管哮喘”收治住院。患者神志清，精神差，饮食差，夜间睡眠差，大小便正常。", "既往史：有“高血压”病史10年，最高达160/80mmHg，目前服用降压药“奥美沙坦", "酯片20mg/次，一日一次”治疗，血压控制在120/80mmHg水平，否认过敏史。", "查体：体温：36.1℃，脉搏：84次/分，呼吸：22次/分，血压：154/81mmHg，体", "重：58.0Kg，神志清晰，精神差，颜面部轻度紫绀，喘息貌，自主体位，表情痛苦，步态", ""]
2026-08-05 12:01:50,630 INFO     29 [qwen-vl-parser] page=2 text: 42 lines (bbox 27-68)
2026-08-05 12:01:50,630 INFO     29 [qwen-vl-parser] page=2 text: 42 sections
2026-08-05 12:01:51,172 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7522860, prompt_len=764
2026-08-05 12:01:54,008 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 12:01:54,011 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-05 12:01:54,038 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7522860, prompt_len=401
2026-08-05 12:02:03,828 INFO     29 [qwen-vl-parser] text API response (len=1209):
["初诊科别:呼吸一科初诊日期:2026-01-04", "过敏史:无", "主诉:反复咳痰喘6年余,再发10余天。", "现病史:6年余来患者每遇吸入刺激性气味或冷空气后出现咳嗽、咳痰及胸闷、气", "喘,咳嗽咳痰症状呈阵发性发作,痰液易咳出,多为白粘痰,不伴发热,不伴胸痛,无夜", "间阵发性呼吸困难及端坐呼吸,每次症状发作时多就诊于我院呼吸内科,曾完善肺功能检", "查确诊为“支气管哮喘”,经抗感染、抗炎、解痉平喘、雾化吸入及对症治疗后症状好转", "出院,出院后院外规律吸入“布地格福气雾剂2揿/次,一日两次”治疗,胸闷、气喘症", "状控制不佳,活动耐力呈进行性下降(以致目前上2层楼或步行500米左右即气喘严重),3", "月余前患者因受凉再次出现咳嗽、咳痰、胸闷、气喘,在家应用“布地格福气雾剂”吸入", "治疗及口服“罗红霉素胶囊7天及甲泼尼龙片8mg/次,一日两次,间隔1-2天每日减1", "片”治疗,咳嗽咳痰及胸闷、气喘症状有所好转后停用上述口服药物,后改为应用“布地", "奈德气雾剂2揿/次,一日三次联合乌美溴铵维兰特罗粉雾剂1吸/次,一日一次”联合维持", "治疗。10余天前患者无诱因再次出现咳嗽、咳痰、胸闷、气喘,不伴发热,在家应用“布", "地奈德气雾剂2揿/次,一日三次联合乌美溴铵维兰特罗粉雾剂1吸/次,一日一次”吸入治", "疗及再次口服“罗红霉素胶囊7天及甲泼尼龙片8mg/次,一日两次,间隔1-2天每日减1", "片”治疗10余天来咳嗽咳痰及胸闷、气喘症状未见好转,为求诊治故来我院就诊,门诊以", "“支气管哮喘”收治住院。患者神志清,精神差,饮食差,夜间睡眠差,大小便正常。", "既往史:有“高血压”病史10年,最高达160/80mmHg,目前服用降压药“奥美沙坦", "酯片20mg/次,一日一次”治疗,血压控制在120/60mmHg水平,否认过敏史。", "查体:体温:36.1℃,脉搏:84次/分,呼吸:22次/分,血压:154/81mmHg,体", "重:58.0Kg,神志清晰,精神差,颜面部轻度紫绀,喘息貌,自主体位,表情痛苦,步态", "正常,检查合作。全身皮肤粘膜未见皮疹及出血点。无肝掌及蜘蛛痣。全身浅表淋巴结均", "未触及肿大。双瞳孔等大等圆,直径为3mm,对光反射灵敏。口唇轻度紫绀,咽腔充血,", "双侧扁桃腺未见肿大及脓点。颈软,颈静脉充盈。双肺呼吸音粗,两肺均可闻及干啰音及", "呼气相哮鸣音。心率84次/分,律齐,心脏各瓣膜听诊区均未闻及病理性杂音。腹平软,", "全腹无压痛及反跳痛。肝脾肋下未触及。双下肢无浮肿。", "辅助检查:暂无。", "初步诊断:1.支气管哮喘急性发作;2.慢性阻塞性肺疾病?3.高血压病2级低危组。", "处理意见:住院治疗。", "医师签名:", "签名日期:2026-01-04", "第1页"]
2026-08-05 12:02:03,831 INFO     29 [qwen-vl-parser] page=3 text: 33 lines (bbox 69-101)
2026-08-05 12:02:03,831 INFO     29 [qwen-vl-parser] page=3 text: 33 sections
2026-08-05 12:02:04,273 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7032042, prompt_len=764
2026-08-05 12:02:07,737 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-01-04"}
```
2026-08-05 12:02:07,740 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=2026-01-04
2026-08-05 12:02:07,768 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7032042, prompt_len=401
2026-08-05 12:02:14,174 INFO     29 [qwen-vl-parser] text API response (len=804):
["IV", "V", "5", "7", "左锁骨中线距前正中线8cm", "桡动脉：脉搏正常，节律规则，无奇脉、交替脉。", "周围血管征：无毛细血管搏动、射枪音、水冲脉、动脉异常搏动。", "腹部：腹部平坦，胃肠蠕动波无，腹式呼吸存在，未见腹壁静脉曲张。腹柔软，液波震颤", "无，振水声无，腹部包块未触及，无压痛、无反跳痛，脾肝未触及，Murphy,s征阴性，肾无", "压痛，叩击痛，腹部血管搏动未见明显异常。输尿管压痛点无明显压痛。肝浊音界正常，肝", "上界位于右锁骨中线第5肋间，移动性浊音无。无明显肾区叩击痛，肠鸣音正常。", "肛门、直肠：未查。", "脊柱四肢：脊柱正常，棘突无压痛及叩击痛，活动度自由活动，四肢无畸形，四肢关节", "活动及动脉搏动未见明显异常，双下肢无浮肿。", "神经反射：腹壁反射正常，四肢肌张力正常，四肢肌力V级，左 右上 下无肢体瘫痪，左", "右肱二头肌反射：正常，双侧膝腱反射：正常，双侧跟腱反射：正常，双侧Hoffmann征阴", "性，双侧Babinski征阴性，双侧Oppenheim征阴性，双侧Kernig征阴性，双侧Brudzinski征", "阴性。脑膜刺激征阴性。", "专科检查", "颜面部轻度紫绀，喘息貌，口唇轻度紫绀，咽腔充血，双侧扁桃腺未见肿大及脓点。颈软，", "颈静脉充盈。双肺呼吸音粗，两肺均可闻及干啰音及呼气相哮鸣音。", "辅助检查", "2026-01-04 血气生化（呼一）：PH值 7.448，二氧化碳分压（9-HR） 39.7，氧分压（9-", "HR） 80.5↓，氧饱和度 95.9%，剩余碱 3.2mmol/L↑，细胞外剩余碱 3.4mmol/L↑。", "初步诊断：", "1.支气管哮喘急性发作", "2.慢性阻塞性肺疾病？", "3.高血压病2级（低危）", "副主任医师签名：", "第 4 页"]
2026-08-05 12:02:14,175 INFO     29 [qwen-vl-parser] page=4 text: 30 lines (bbox 102-131)
2026-08-05 12:02:14,175 INFO     29 [qwen-vl-parser] page=4 text: 30 sections
2026-08-05 12:02:14,663 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9378127, prompt_len=764
2026-08-05 12:02:17,147 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 12:02:17,150 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-05 12:02:17,177 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9378127, prompt_len=401
2026-08-05 12:02:31,790 INFO     29 [qwen-vl-parser] text API response (len=1770):
["2026-01-04 09:30 首次病程记录", "病例特点：患者：性别：女，年龄：67岁，以“[反复咳嗽喘6年余，再发10余", "天。]”为主诉入院。入院情况：[6年余来患者每遇吸入刺激性气味或冷空气后出现咳", "嗽、咳痰及胸闷、气喘，咳嗽咳痰症状呈阵发性发作，痰液易咳出，多为白粘痰，每次症", "状发作时多就诊于我院呼吸内科，曾完善肺功能检查确诊为“支气管哮喘”，经抗感染、", "抗炎、解痉平喘、雾化吸入及对症治疗后症状好转出院，出院后院外规律吸入“布地格福", "气雾剂 2揿/次，一日两次”治疗，胸闷、气喘症状控制不佳，活动耐力呈进行性下降", "(以致目前上2层楼或步行500米左右即气喘严重)，3月余前患者因受凉再次出现咳嗽、咳", "痰、胸闷、气喘，在家应用“布地格福气雾剂”吸入治疗及口服“罗红霉素胶囊7天及甲", "泼尼龙片 8mg/次，一日两次，间隔1-2天每日减1片”治疗，咳嗽咳痰及胸闷、气喘症状", "有所好转后停用上述口服药物，后改为应用“布地奈德气雾剂2揿/次，一日三次联合乌美", "溴铵维兰特罗粉雾剂1吸/次，一日一次”联合维持治疗。10余天前患者无诱因再次出现咳", "嗽、咳痰、胸闷、气喘，不伴发热，在家应用“布地奈德气雾剂2揿/次，一日三次联合乌", "美溴铵维兰特罗粉雾剂1吸/次，一日一次”吸入治疗及再次口服“罗红霉素胶囊7天及甲", "泼尼龙片 8mg/次，一日两次，间隔1-2天每日减1片”治疗10余天来咳嗽咳痰及胸闷、气", "喘症状未见好转，为求诊治故来我院就诊，门诊以“支气管哮喘”收治住院。患者神志", "清，精神差，饮食差，夜间睡眠差，大小便正常。]既往史：有“高血压病”病史10年，", "最高达160/80mmHg，目前服用降压药“奥美沙坦酯片 20mg/次，一日一次”治疗，血压", "控制在120/60mmHg水平，否认过敏史。]入院查体：[T:36.1℃，P:84次/分，R:22次/分，", "BP:154/81mmHg，SPO2:93%，发育正常，营养中等，体型中等，神志清，精神差，颜面部", "轻度紫绀，喘息貌，自主体位，查体合作。全身皮肤粘膜未见皮疹及出血点。无肝掌及蜘", "蛛痣。全身浅表淋巴结均未触及肿大。双瞳孔等大等圆，直径为3mm，对光反射灵敏。口", "唇轻度紫绀，咽腔充血，双侧扁桃腺未见肿大及脓点。颈软，颈静脉充盈。双肺呼吸音", "粗，两肺均可闻及干啰音及呼气相哮鸣音。心率84次/分，律齐，心脏各瓣膜听诊区均未", "闻及病理性杂音。腹平软，全腹无压痛及反跳痛。肝脾肋下未触及。双下肢无浮肿。]专", "科检查：颜面部轻度紫绀，喘息貌，口唇轻度紫绀，咽腔充血，双侧扁桃腺未见肿大及脓", "点。颈软，颈静脉充盈。双肺呼吸音粗，两肺均可闻及干啰音及呼气相哮鸣音。]辅助检", "查：暂无。]初步诊断：1.支气管哮喘急性发作；2.慢性阻塞性肺疾病？3.高血压病2", "级 低危组。诊断依据：1.老年女性；2.反复咳痰喘6年余，再发10余天；3.临床表现：6", "年余来患者每遇吸入刺激性气味或冷空气后出现咳嗽、咳痰及胸闷、气喘，咳嗽咳痰症状", "呈阵发性发作，痰液易咳出，多为白粘痰，每次症状发作时多就诊于我院呼吸内科，曾完", "善肺功能检查确诊为“支气管哮喘”，经抗感染、抗炎、解痉平喘、雾化吸入及对症治疗", "后症状好转出院，出院后院外规律吸入“布地格福气雾剂 2揿/次，一日两次”治疗，胸", "闷、气喘症状控制不佳，活动耐力呈进行性下降(以致目前上2层楼或步行500米左右即气", "喘严重)，3月余前患者因受凉再次出现咳嗽、咳痰、胸闷、气喘，在家应用“布地格福气", "雾剂”吸入治疗及口服“罗红霉素胶囊7天及甲泼尼龙片 8mg/次，一日两次，间隔1-2天", "每日减1片”治疗，咳嗽咳痰及胸闷、气喘症状有所好转后停用上述口服药物，后改为应", "用“布地奈德气雾剂2揿/次，一日三次联合乌美溴铵维兰特罗粉雾剂1吸/次，一日一次”", "联合维持治疗。10余天前患者无诱因再次出现咳嗽、咳痰、胸闷、气喘，不伴发热，在家", "应用“布地奈德气雾剂2揿/次，一日三次联合乌美溴铵维兰特罗粉雾剂1吸/次，一日一"]
2026-08-05 12:02:31,794 INFO     29 [qwen-vl-parser] page=5 text: 40 lines (bbox 132-171)
2026-08-05 12:02:31,794 INFO     29 [qwen-vl-parser] page=5 text: 40 sections
2026-08-05 12:02:32,257 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9695772, prompt_len=764
2026-08-05 12:02:35,136 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 12:02:35,139 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-05 12:02:35,170 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9695772, prompt_len=401
2026-08-05 12:02:42,447 INFO     29 [qwen-vl-text] coord API raw response (len=12390):
[
	{"text": "肺功能试验报告", "bbox": [475, 71, 562, 84]},
	{"text": "姓名：", "bbox": [250, 100, 286, 112]},
	{"text": "年龄：38岁", "bbox": [250, 112, 422, 124]},
	{"text": "性别：女", "bbox": [250, 124, 402, 137]},
	{"text": "科别：", "bbox": [250, 137, 286, 149]},
	{"text": "保险：", "bbox": [250, 149, 286, 161]},
	{"text": "预计值模式：Standard-new", "bbox": [250, 161, 476, 174]},
	{"text": "测试号：2026020017", "bbox": [529, 98, 740, 110]},
	{"text": "身高：166 cm", "bbox": [529, 110, 710, 123]},
	{"text": "体重：60 kg", "bbox": [529, 123, 704, 135]},
	{"text": "备注：", "bbox": [529, 135, 565, 148]},
	{"text": "联系电话：", "bbox": [529, 148, 594, 160]},
	{"text": "操作者：蒋细萍", "bbox": [666, 161, 709, 173]},
	{"text": "Pred", "bbox": [338, 188, 370, 200]},
	{"text": "A1 A1/Pd", "bbox": [398, 188, 462, 200]},
	{"text": "P1 A2/Pd", "bbox": [490, 188, 552, 200]},
	{"text": "chg%l", "bbox": [566, 188, 602, 200]},
	{"text": "P2 A3/Pd", "bbox": [634, 188, 697, 200]},
	{"text": "chg%2", "bbox": [711, 188, 749, 200]},
	{"text": "P3 A4/Pd", "bbox": [780, 188, 841, 200]},
	{"text": "chg%3", "bbox": [855, 188, 892, 200]},
	{"text": "FVC", "bbox": [128, 215, 152, 227]},
	{"text": "[L]", "bbox": [303, 215, 323, 227]},
	{"text": "2.99", "bbox": [338, 215, 370, 227]},
	{"text": "2.21", "bbox": [384, 215, 415, 227]},
	{"text": "74.0", "bbox": [429, 215, 462, 227]},
	{"text": "2.63", "bbox": [475, 215, 506, 227]},
	{"text": "87.9", "bbox": [520, 215, 552, 227]},
	{"text": "18.72", "bbox": [566, 215, 602, 227]},
	{"text": "2.04", "bbox": [619, 215, 650, 227]},
	{"text": "88.2", "bbox": [666, 215, 697, 227]},
	{"text": "19.17", "bbox": [711, 215, 749, 227]},
	{"text": "2.67", "bbox": [764, 215, 795, 227]},
	{"text": "86.0", "bbox": [810, 215, 841, 227]},
	{"text": "16.23", "bbox": [855, 215, 892, 227]},
	{"text": "FEV 1", "bbox": [128, 227, 165, 240]},
	{"text": "[L]", "bbox": [303, 227, 323, 240]},
	{"text": "2.67", "bbox": [338, 227, 370, 240]},
	{"text": "1.25", "bbox": [384, 227, 415, 240]},
	{"text": "48.6", "bbox": [429, 227, 462, 240]},
	{"text": "1.62", "bbox": [475, 227, 506, 240]},
	{"text": "69.2", "bbox": [520, 227, 552, 240]},
	{"text": "21.85", "bbox": [566, 227, 602, 240]},
	{"text": "1.84", "bbox": [619, 227, 650, 240]},
	{"text": "69.8", "bbox": [666, 227, 697, 240]},
	{"text": "23.23", "bbox": [711, 227, 749, 240]},
	{"text": "1.60", "bbox": [764, 227, 795, 240]},
	{"text": "68.4", "bbox": [810, 227, 841, 240]},
	{"text": "20.23", "bbox": [855, 227, 892, 240]},
	{"text": "FEV 1 % FVC", "bbox": [128, 240, 212, 252]},
	{"text": "[%]", "bbox": [303, 240, 323, 252]},
	{"text": "84.19", "bbox": [338, 240, 370, 252]},
	{"text": "56.48", "bbox": [384, 240, 415, 252]},
	{"text": "67.1", "bbox": [429, 240, 462, 252]},
	{"text": "67.97", "bbox": [475, 240, 506, 252]},
	{"text": "68.9", "bbox": [520, 240, 552, 252]},
	{"text": "2.64", "bbox": [566, 240, 602, 252]},
	{"text": "68.40", "bbox": [619, 240, 650, 252]},
	{"text": "69.4", "bbox": [666, 240, 697, 252]},
	{"text": "3.41", "bbox": [711, 240, 749, 252]},
	{"text": "68.42", "bbox": [764, 240, 795, 252]},
	{"text": "69.4", "bbox": [810, 240, 841, 252]},
	{"text": "3.44", "bbox": [855, 240, 892, 252]},
	{"text": "FEV 1 % VC MAX", "bbox": [128, 252, 234, 265]},
	{"text": "[%]", "bbox": [303, 252, 323, 265]},
	{"text": "81.88", "bbox": [338, 252, 370, 265]},
	{"text": "65.26", "bbox": [384, 252, 415, 265]},
	{"text": "67.6", "bbox": [429, 252, 462, 265]},
	{"text": "67.97", "bbox": [475, 252, 506, 265]},
	{"text": "70.8", "bbox": [520, 252, 552, 265]},
	{"text": "4.91", "bbox": [566, 252, 602, 265]},
	{"text": "68.40", "bbox": [619, 252, 650, 265]},
	{"text": "71.3", "bbox": [666, 252, 697, 265]},
	{"text": "6.70", "bbox": [711, 252, 749, 265]},
	{"text": "68.42", "bbox": [764, 252, 795, 265]},
	{"text": "71.4", "bbox": [810, 252, 841, 265]},
	{"text": "5.73", "bbox": [855, 252, 892, 265]},
	{"text": "VC MAX", "bbox": [128, 265, 174, 277]},
	{"text": "[L]", "bbox": [303, 265, 323, 277]},
	{"text": "3.03", "bbox": [338, 265, 370, 277]},
	{"text": "2.26", "bbox": [384, 265, 415, 277]},
	{"text": "74.6", "bbox": [429, 265, 462, 277]},
	{"text": "2.63", "bbox": [475, 265, 506, 277]},
	{"text": "86.6", "bbox": [520, 265, 552, 277]},
	{"text": "16.14", "bbox": [566, 265, 602, 277]},
	{"text": "2.64", "bbox": [619, 265, 650, 277]},
	{"text": "87.0", "bbox": [666, 265, 697, 277]},
	{"text": "16.69", "bbox": [711, 265, 749, 277]},
	{"text": "2.57", "bbox": [764, 265, 795, 277]},
	{"text": "84.8", "bbox": [810, 265, 841, 277]},
	{"text": "13.71", "bbox": [855, 265, 892, 277]},
	{"text": "PEF", "bbox": [128, 277, 152, 290]},
	{"text": "[L/s]", "bbox": [288, 277, 323, 290]},
	{"text": "6.28", "bbox": [338, 277, 370, 290]},
	{"text": "2.66", "bbox": [384, 277, 415, 290]},
	{"text": "42.4", "bbox": [429, 277, 462, 290]},
	{"text": "2.90", "bbox": [475, 277, 506, 290]},
	{"text": "46.2", "bbox": [520, 277, 552, 290]},
	{"text": "9.17", "bbox": [566, 277, 602, 290]},
	{"text": "3.37", "bbox": [619, 277, 650, 290]},
	{"text": "53.7", "bbox": [666, 277, 697, 290]},
	{"text": "26.79", "bbox": [711, 277, 749, 290]},
	{"text": "3.42", "bbox": [764, 277, 795, 290]},
	{"text": "64.6", "bbox": [810, 277, 841, 290]},
	{"text": "28.64", "bbox": [855, 277, 892, 290]},
	{"text": "MMEF 75/25", "bbox": [128, 290, 203, 303]},
	{"text": "[L/s]", "bbox": [288, 290, 323, 303]},
	{"text": "3.57", "bbox": [338, 290, 370, 303]},
	{"text": "0.61", "bbox": [384, 290, 415, 303]},
	{"text": "14.4", "bbox": [429, 290, 462, 303]},
	{"text": "0.67", "bbox": [475, 290, 506, 303]},
	{"text": "18.8", "bbox": [520, 290, 552, 303]},
	{"text": "31.03", "bbox": [566, 290, 602, 303]},
	{"text": "0.73", "bbox": [619, 290, 650, 303]},
	{"text": "20.4", "bbox": [666, 290, 697, 303]},
	{"text": "42.01", "bbox": [711, 290, 749, 303]},
	{"text": "0.69", "bbox": [764, 290, 795, 303]},
	{"text": "19.4", "bbox": [810, 290, 841, 303]},
	{"text": "35.02", "bbox": [855, 290, 892, 303]},
	{"text": "MEF 50", "bbox": [128, 303, 174, 315]},
	{"text": "[L/s]", "bbox": [288, 303, 323, 315]},
	{"text": "4.01", "bbox": [338, 303, 370, 315]},
	{"text": "0.68", "bbox": [384, 303, 415, 315]},
	{"text": "17.0", "bbox": [429, 303, 462, 315]},
	{"text": "0.90", "bbox": [475, 303, 506, 315]},
	{"text": "22.5", "bbox": [520, 303, 552, 315]},
	{"text": "32.75", "bbox": [566, 303, 602, 315]},
	{"text": "0.89", "bbox": [619, 303, 650, 315]},
	{"text": "22.1", "bbox": [666, 303, 697, 315]},
	{"text": "30.15", "bbox": [711, 303, 749, 315]},
	{"text": "0.88", "bbox": [764, 303, 795, 315]},
	{"text": "21.9", "bbox": [810, 303, 841, 315]},
	{"text": "29.17", "bbox": [855, 303, 892, 315]},
	{"text": "MEF 25", "bbox": [128, 315, 174, 328]},
	{"text": "[L/s]", "bbox": [288, 315, 323, 328]},
	{"text": "1.79", "bbox": [338, 315, 370, 328]},
	{"text": "0.19", "bbox": [384, 315, 415, 328]},
	{"text": "10.5", "bbox": [429, 315, 462, 328]},
	{"text": "0.27", "bbox": [475, 315, 506, 328]},
	{"text": "15.2", "bbox": [520, 315, 552, 328]},
	{"text": "44.16", "bbox": [566, 315, 602, 328]},
	{"text": "0.33", "bbox": [619, 315, 650, 328]},
	{"text": "18.7", "bbox": [666, 315, 697, 328]},
	{"text": "77.66", "bbox": [711, 315, 749, 328]},
	{"text": "0.31", "bbox": [764, 315, 795, 328]},
	{"text": "17.6", "bbox": [810, 315, 841, 328]},
	{"text": "66.49", "bbox": [855, 315, 892, 328]},
	{"text": "FET", "bbox": [128, 328, 152, 341]},
	{"text": "[s]", "bbox": [303, 328, 323, 341]},
	{"text": "7.63", "bbox": [384, 328, 415, 341]},
	{"text": "8.01", "bbox": [475, 328, 506, 341]},
	{"text": "4.99", "bbox": [572, 328, 602, 341]},
	{"text": "7.79", "bbox": [619, 328, 650, 341]},
	{"text": "2.14", "bbox": [717, 328, 749, 341]},
	{"text": "7.43", "bbox": [764, 328, 795, 341]},
	{"text": "-2.60", "bbox": [855, 328, 892, 341]},
	{"text": "V backextrapolation ex [L]", "bbox": [128, 341, 323, 354]},
	{"text": "0.05", "bbox": [384, 341, 415, 354]},
	{"text": "0.04", "bbox": [475, 341, 506, 354]},
	{"text": "-11.67", "bbox": [557, 341, 602, 354]},
	{"text": "0.04", "bbox": [619, 341, 650, 354]},
	{"text": "-18.64", "bbox": [704, 341, 749, 354]},
	{"text": "0.04", "bbox": [764, 341, 795, 354]},
	{"text": "-13.51", "bbox": [847, 341, 892, 354]},
	{"text": "PIF", "bbox": [128, 354, 152, 367]},
	{"text": "[L/s]", "bbox": [288, 354, 323, 367]},
	{"text": "3.04", "bbox": [384, 354, 415, 367]},
	{"text": "3.37", "bbox": [475, 354, 506, 367]},
	{"text": "10.91", "bbox": [566, 354, 602, 367]},
	{"text": "3.51", "bbox": [619, 354, 650, 367]},
	{"text": "15.70", "bbox": [711, 354, 749, 367]},
	{"text": "3.60", "bbox": [764, 354, 795, 367]},
	{"text": "18.67", "bbox": [855, 354, 892, 367]},
	{"text": "FIV1", "bbox": [128, 367, 158, 380]},
	{"text": "[L]", "bbox": [303, 367, 323, 380]},
	{"text": "2.21", "bbox": [384, 367, 415, 380]},
	{"text": "2.56", "bbox": [475, 367, 506, 380]},
	{"text": "15.71", "bbox": [566, 367, 602, 380]},
	{"text": "2.56", "bbox": [619, 367, 650, 380]},
	{"text": "15.66", "bbox": [711, 367, 749, 380]},
	{"text": "2.50", "bbox": [764, 367, 795, 380]},
	{"text": "13.09", "bbox": [855, 367, 892, 380]},
	{"text": "PEF50 % FIF50", "bbox": [128, 380, 225, 393]},
	{"text": "[%]", "bbox": [303, 380, 323, 393]},
	{"text": "22.86", "bbox": [375, 380, 415, 393]},
	{"text": "28.15", "bbox": [467, 380, 506, 393]},
	{"text": "23.14", "bbox": [566, 380, 602, 393]},
	{"text": "25.36", "bbox": [619, 380, 650, 393]},
	{"text": "10.95", "bbox": [711, 380, 749, 393]},
	{"text": "27.28", "bbox": [755, 380, 795, 393]},
	{"text": "19.33", "bbox": [855, 380, 892, 393]},
	{"text": "MVV", "bbox": [128, 393, 152, 406]},
	{"text": "[L/min]", "bbox": [272, 393, 323, 406]},
	{"text": "99.77", "bbox": [330, 393, 370, 406]},
	{"text": "46.21", "bbox": [377, 393, 415, 406]},
	{"text": "46.3", "bbox": [429, 393, 462, 406]},
	{"text": "BF MVV", "bbox": [128, 406, 174, 419]},
	{"text": "[1/min]", "bbox": [272, 406, 323, 419]},
	{"text": "75.55", "bbox": [377, 406, 415, 419]},
	{"text": "10", "bbox": [216, 457, 227, 467]},
	{"text": "Flow [L/s]", "bbox": [234, 460, 284, 471]},
	{"text": "F/V ex", "bbox": [328, 460, 361, 470]},
	{"text": "1", "bbox": [430, 461, 459, 471]},
	{"text": "2", "bbox": [430, 471, 459, 481]},
	{"text": "3", "bbox": [430, 481, 459, 491]},
	{"text": "4", "bbox": [430, 491, 459, 501]},
	{"text": "6", "bbox": [220, 508, 228, 517]},
	{"text": "4", "bbox": [220, 533, 228, 542]},
	{"text": "2", "bbox": [220, 558, 228, 568]},
	{"text": "0", "bbox": [220, 584, 228, 593]},
	{"text": "Vol [L]", "bbox": [367, 574, 402, 585]},
	{"text": "1", "bbox": [264, 593, 271, 602]},
	{"text": "2", "bbox": [297, 593, 304, 602]},
	{"text": "3", "bbox": [330, 593, 337, 602]},
	{"text": "4", "bbox": [364, 593, 371, 602]},
	{"text": "5", "bbox": [397, 593, 404, 602]},
	{"text": "2", "bbox": [220, 610, 228, 619]},
	{"text": "4", "bbox": [220, 635, 228, 644]},
	{"text": "6", "bbox": [220, 661, 228, 670]},
	{"text": "8", "bbox": [220, 686, 228, 696]},
	{"text": "10", "bbox": [216, 711, 230, 720]},
	{"text": "F/V In", "bbox": [330, 706, 360, 716]},
	{"text": "Vol%VCmax", "bbox": [516, 503, 575, 513]},
	{"text": "0", "bbox": [529, 513, 537, 523]},
	{"text": "0", "bbox": [548, 513, 556, 523]},
	{"text": "Vol [L]", "bbox": [562, 517, 594, 528]},
	{"text": "20", "bbox": [524, 525, 538, 535]},
	{"text": "40", "bbox": [524, 537, 538, 547]},
	{"text": "60", "bbox": [524, 549, 538, 559]},
	{"text": "80", "bbox": [524, 561, 538, 571]},
	{"text": "100", "bbox": [519, 573, 538, 583]},
	{"text": "2", "bbox": [548, 559, 556, 569]},
	{"text": "VCmax", "bbox": [572, 570, 608, 579]},
	{"text": "3", "bbox": [548, 582, 556, 592]},
	{"text": "4", "bbox": [548, 605, 556, 615]},
	{"text": "5", "bbox": [548, 628, 556, 638]},
	{"text": "6", "bbox": [548, 651, 556, 661]},
	{"text": "Time [s]", "bbox": [714, 642, 754, 652]},
	{"text": "0", "bbox": [557, 661, 564, 670]},
	{"text": "2", "bbox": [603, 661, 611, 670]},
	{"text": "4", "bbox": [650, 661, 657, 670]},
	{"text": "6", "bbox": [697, 661, 704, 670]},
	{"text": "8", "bbox": [743, 661, 750, 670]},
	{"text": "10", "bbox": [789, 661, 800, 670]},
	{"text": "12", "bbox": [835, 661, 846, 670]},
	{"text": "14", "bbox": [882, 661, 894, 670]},
	{"text": "意见：", "bbox": [107, 735, 151, 749]},
	{"text": "1. 中重度阻塞性肺通气功能障碍。", "bbox": [107, 750, 325, 762]},
	{"text": "2. 支气管舒张试验阳性。", "bbox": [107, 762, 265, 774]},
	{"text": "(1. 24h内无支气管舒张药物使用史)", "bbox": [112, 774, 348, 786]},
	{"text": "(2
2026-08-05 12:02:42,448 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-05 12:02:42,456 INFO     29 [qwen-vl-text] coord API: raw_items=251, valid_items=250, elapsed=73.9s
2026-08-05 12:02:42,456 INFO     29 [qwen-vl-text] coord item[0]: text=肺功能试验报告, bbox=[475, 71, 562, 84]
2026-08-05 12:02:42,456 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[250, 100, 286, 112]
2026-08-05 12:02:42,456 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：38岁, bbox=[250, 112, 422, 124]
2026-08-05 12:02:42,456 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女, bbox=[250, 124, 402, 137]
2026-08-05 12:02:42,457 INFO     29 [qwen-vl-text] coord item[4]: text=科别：, bbox=[250, 137, 286, 149]
2026-08-05 12:02:42,457 INFO     29 [qwen-vl-text] coord item[5]: text=保险：, bbox=[250, 149, 286, 161]
2026-08-05 12:02:42,457 INFO     29 [qwen-vl-text] coord item[6]: text=预计值模式：Standard-new, bbox=[250, 161, 476, 174]
2026-08-05 12:02:42,457 INFO     29 [qwen-vl-text] coord item[7]: text=测试号：2026020017, bbox=[529, 98, 740, 110]
2026-08-05 12:02:42,457 INFO     29 [qwen-vl-text] coord item[8]: text=身高：166 cm, bbox=[529, 110, 710, 123]
2026-08-05 12:02:42,457 INFO     29 [qwen-vl-text] coord item[9]: text=体重：60 kg, bbox=[529, 123, 704, 135]
2026-08-05 12:02:42,458 INFO     29 [qwen-vl-text] coord item[10]: text=备注：, bbox=[529, 135, 565, 148]
2026-08-05 12:02:42,458 INFO     29 [qwen-vl-text] coord item[11]: text=联系电话：, bbox=[529, 148, 594, 160]
2026-08-05 12:02:42,459 INFO     29 [qwen-vl-text] coord item[12]: text=操作者：蒋细萍, bbox=[666, 161, 709, 173]
2026-08-05 12:02:42,459 INFO     29 [qwen-vl-text] coord item[13]: text=Pred, bbox=[338, 188, 370, 200]
2026-08-05 12:02:42,460 INFO     29 [qwen-vl-text] coord item[14]: text=A1 A1/Pd, bbox=[398, 188, 462, 200]
2026-08-05 12:02:42,460 INFO     29 [qwen-vl-text] coord item[15]: text=P1 A2/Pd, bbox=[490, 188, 552, 200]
2026-08-05 12:02:42,460 INFO     29 [qwen-vl-text] coord item[16]: text=chg%l, bbox=[566, 188, 602, 200]
2026-08-05 12:02:42,461 INFO     29 [qwen-vl-text] coord item[17]: text=P2 A3/Pd, bbox=[634, 188, 697, 200]
2026-08-05 12:02:42,462 INFO     29 [qwen-vl-text] coord item[18]: text=chg%2, bbox=[711, 188, 749, 200]
2026-08-05 12:02:42,462 INFO     29 [qwen-vl-text] coord item[19]: text=P3 A4/Pd, bbox=[780, 188, 841, 200]
2026-08-05 12:02:42,462 INFO     29 [qwen-vl-text] coord item[20]: text=chg%3, bbox=[855, 188, 892, 200]
2026-08-05 12:02:42,463 INFO     29 [qwen-vl-text] coord item[21]: text=FVC, bbox=[128, 215, 152, 227]
2026-08-05 12:02:42,463 INFO     29 [qwen-vl-text] coord item[22]: text=[L], bbox=[303, 215, 323, 227]
2026-08-05 12:02:42,463 INFO     29 [qwen-vl-text] coord item[23]: text=2.99, bbox=[338, 215, 370, 227]
2026-08-05 12:02:42,463 INFO     29 [qwen-vl-text] coord item[24]: text=2.21, bbox=[384, 215, 415, 227]
2026-08-05 12:02:42,463 INFO     29 [qwen-vl-text] coord item[25]: text=74.0, bbox=[429, 215, 462, 227]
2026-08-05 12:02:42,463 INFO     29 [qwen-vl-text] coord item[26]: text=2.63, bbox=[475, 215, 506, 227]
2026-08-05 12:02:42,463 INFO     29 [qwen-vl-text] coord item[27]: text=87.9, bbox=[520, 215, 552, 227]
2026-08-05 12:02:42,463 INFO     29 [qwen-vl-text] coord item[28]: text=18.72, bbox=[566, 215, 602, 227]
2026-08-05 12:02:42,463 INFO     29 [qwen-vl-text] coord item[29]: text=2.04, bbox=[619, 215, 650, 227]
2026-08-05 12:02:42,463 INFO     29 [qwen-vl-text] coord item[30]: text=88.2, bbox=[666, 215, 697, 227]
2026-08-05 12:02:42,464 INFO     29 [qwen-vl-text] coord item[31]: text=19.17, bbox=[711, 215, 749, 227]
2026-08-05 12:02:42,464 INFO     29 [qwen-vl-text] coord item[32]: text=2.67, bbox=[764, 215, 795, 227]
2026-08-05 12:02:42,464 INFO     29 [qwen-vl-text] coord item[33]: text=86.0, bbox=[810, 215, 841, 227]
2026-08-05 12:02:42,464 INFO     29 [qwen-vl-text] coord item[34]: text=16.23, bbox=[855, 215, 892, 227]
2026-08-05 12:02:42,464 INFO     29 [qwen-vl-text] coord item[35]: text=FEV 1, bbox=[128, 227, 165, 240]
2026-08-05 12:02:42,464 INFO     29 [qwen-vl-text] coord item[36]: text=[L], bbox=[303, 227, 323, 240]
2026-08-05 12:02:42,464 INFO     29 [qwen-vl-text] coord item[37]: text=2.67, bbox=[338, 227, 370, 240]
2026-08-05 12:02:42,464 INFO     29 [qwen-vl-text] coord item[38]: text=1.25, bbox=[384, 227, 415, 240]
2026-08-05 12:02:42,464 INFO     29 [qwen-vl-text] coord item[39]: text=48.6, bbox=[429, 227, 462, 240]
2026-08-05 12:02:42,464 INFO     29 [qwen-vl-text] coord item[40]: text=1.62, bbox=[475, 227, 506, 240]
2026-08-05 12:02:42,464 INFO     29 [qwen-vl-text] coord item[41]: text=69.2, bbox=[520, 227, 552, 240]
2026-08-05 12:02:42,464 INFO     29 [qwen-vl-text] coord item[42]: text=21.85, bbox=[566, 227, 602, 240]
2026-08-05 12:02:42,464 INFO     29 [qwen-vl-text] coord item[43]: text=1.84, bbox=[619, 227, 650, 240]
2026-08-05 12:02:42,464 INFO     29 [qwen-vl-text] coord item[44]: text=69.8, bbox=[666, 227, 697, 240]
2026-08-05 12:02:42,464 INFO     29 [qwen-vl-text] coord item[45]: text=23.23, bbox=[711, 227, 749, 240]
2026-08-05 12:02:42,465 INFO     29 [qwen-vl-text] coord item[46]: text=1.60, bbox=[764, 227, 795, 240]
2026-08-05 12:02:42,465 INFO     29 [qwen-vl-text] coord item[47]: text=68.4, bbox=[810, 227, 841, 240]
2026-08-05 12:02:42,465 INFO     29 [qwen-vl-text] coord item[48]: text=20.23, bbox=[855, 227, 892, 240]
2026-08-05 12:02:42,465 INFO     29 [qwen-vl-text] coord item[49]: text=FEV 1 % FVC, bbox=[128, 240, 212, 252]
2026-08-05 12:02:42,465 INFO     29 [qwen-vl-text] coord item[50]: text=[%], bbox=[303, 240, 323, 252]
2026-08-05 12:02:42,465 INFO     29 [qwen-vl-text] coord item[51]: text=84.19, bbox=[338, 240, 370, 252]
2026-08-05 12:02:42,465 INFO     29 [qwen-vl-text] coord item[52]: text=56.48, bbox=[384, 240, 415, 252]
2026-08-05 12:02:42,465 INFO     29 [qwen-vl-text] coord item[53]: text=67.1, bbox=[429, 240, 462, 252]
2026-08-05 12:02:42,465 INFO     29 [qwen-vl-text] coord item[54]: text=67.97, bbox=[475, 240, 506, 252]
2026-08-05 12:02:42,465 INFO     29 [qwen-vl-text] coord item[55]: text=68.9, bbox=[520, 240, 552, 252]
2026-08-05 12:02:42,465 INFO     29 [qwen-vl-text] coord item[56]: text=2.64, bbox=[566, 240, 602, 252]
2026-08-05 12:02:42,466 INFO     29 [qwen-vl-text] coord item[57]: text=68.40, bbox=[619, 240, 650, 252]
2026-08-05 12:02:42,466 INFO     29 [qwen-vl-text] coord item[58]: text=69.4, bbox=[666, 240, 697, 252]
2026-08-05 12:02:42,466 INFO     29 [qwen-vl-text] coord item[59]: text=3.41, bbox=[711, 240, 749, 252]
2026-08-05 12:02:42,466 INFO     29 [qwen-vl-text] coord item[60]: text=68.42, bbox=[764, 240, 795, 252]
2026-08-05 12:02:42,466 INFO     29 [qwen-vl-text] coord item[61]: text=69.4, bbox=[810, 240, 841, 252]
2026-08-05 12:02:42,466 INFO     29 [qwen-vl-text] coord item[62]: text=3.44, bbox=[855, 240, 892, 252]
2026-08-05 12:02:42,466 INFO     29 [qwen-vl-text] coord item[63]: text=FEV 1 % VC MAX, bbox=[128, 252, 234, 265]
2026-08-05 12:02:42,466 INFO     29 [qwen-vl-text] coord item[64]: text=[%], bbox=[303, 252, 323, 265]
2026-08-05 12:02:42,466 INFO     29 [qwen-vl-text] coord item[65]: text=81.88, bbox=[338, 252, 370, 265]
2026-08-05 12:02:42,466 INFO     29 [qwen-vl-text] coord item[66]: text=65.26, bbox=[384, 252, 415, 265]
2026-08-05 12:02:42,466 INFO     29 [qwen-vl-text] coord item[67]: text=67.6, bbox=[429, 252, 462, 265]
2026-08-05 12:02:42,466 INFO     29 [qwen-vl-text] coord item[68]: text=67.97, bbox=[475, 252, 506, 265]
2026-08-05 12:02:42,466 INFO     29 [qwen-vl-text] coord item[69]: text=70.8, bbox=[520, 252, 552, 265]
2026-08-05 12:02:42,466 INFO     29 [qwen-vl-text] coord item[70]: text=4.91, bbox=[566, 252, 602, 265]
2026-08-05 12:02:42,466 INFO     29 [qwen-vl-text] coord item[71]: text=68.40, bbox=[619, 252, 650, 265]
2026-08-05 12:02:42,466 INFO     29 [qwen-vl-text] coord item[72]: text=71.3, bbox=[666, 252, 697, 265]
2026-08-05 12:02:42,466 INFO     29 [qwen-vl-text] coord item[73]: text=6.70, bbox=[711, 252, 749, 265]
2026-08-05 12:02:42,467 INFO     29 [qwen-vl-text] coord item[74]: text=68.42, bbox=[764, 252, 795, 265]
2026-08-05 12:02:42,467 INFO     29 [qwen-vl-text] coord item[75]: text=71.4, bbox=[810, 252, 841, 265]
2026-08-05 12:02:42,467 INFO     29 [qwen-vl-text] coord item[76]: text=5.73, bbox=[855, 252, 892, 265]
2026-08-05 12:02:42,467 INFO     29 [qwen-vl-text] coord item[77]: text=VC MAX, bbox=[128, 265, 174, 277]
2026-08-05 12:02:42,467 INFO     29 [qwen-vl-text] coord item[78]: text=[L], bbox=[303, 265, 323, 277]
2026-08-05 12:02:42,467 INFO     29 [qwen-vl-text] coord item[79]: text=3.03, bbox=[338, 265, 370, 277]
2026-08-05 12:02:42,467 INFO     29 [qwen-vl-text] coord item[80]: text=2.26, bbox=[384, 265, 415, 277]
2026-08-05 12:02:42,467 INFO     29 [qwen-vl-text] coord item[81]: text=74.6, bbox=[429, 265, 462, 277]
2026-08-05 12:02:42,467 INFO     29 [qwen-vl-text] coord item[82]: text=2.63, bbox=[475, 265, 506, 277]
2026-08-05 12:02:42,467 INFO     29 [qwen-vl-text] coord item[83]: text=86.6, bbox=[520, 265, 552, 277]
2026-08-05 12:02:42,468 INFO     29 [qwen-vl-text] coord item[84]: text=16.14, bbox=[566, 265, 602, 277]
2026-08-05 12:02:42,468 INFO     29 [qwen-vl-text] coord item[85]: text=2.64, bbox=[619, 265, 650, 277]
2026-08-05 12:02:42,468 INFO     29 [qwen-vl-text] coord item[86]: text=87.0, bbox=[666, 265, 697, 277]
2026-08-05 12:02:42,468 INFO     29 [qwen-vl-text] coord item[87]: text=16.69, bbox=[711, 265, 749, 277]
2026-08-05 12:02:42,468 INFO     29 [qwen-vl-text] coord item[88]: text=2.57, bbox=[764, 265, 795, 277]
2026-08-05 12:02:42,468 INFO     29 [qwen-vl-text] coord item[89]: text=84.8, bbox=[810, 265, 841, 277]
2026-08-05 12:02:42,468 INFO     29 [qwen-vl-text] coord item[90]: text=13.71, bbox=[855, 265, 892, 277]
2026-08-05 12:02:42,468 INFO     29 [qwen-vl-text] coord item[91]: text=PEF, bbox=[128, 277, 152, 290]
2026-08-05 12:02:42,468 INFO     29 [qwen-vl-text] coord item[92]: text=[L/s], bbox=[288, 277, 323, 290]
2026-08-05 12:02:42,468 INFO     29 [qwen-vl-text] coord item[93]: text=6.28, bbox=[338, 277, 370, 290]
2026-08-05 12:02:42,468 INFO     29 [qwen-vl-text] coord item[94]: text=2.66, bbox=[384, 277, 415, 290]
2026-08-05 12:02:42,468 INFO     29 [qwen-vl-text] coord item[95]: text=42.4, bbox=[429, 277, 462, 290]
2026-08-05 12:02:42,468 INFO     29 [qwen-vl-text] coord item[96]: text=2.90, bbox=[475, 277, 506, 290]
2026-08-05 12:02:42,468 INFO     29 [qwen-vl-text] coord item[97]: text=46.2, bbox=[520, 277, 552, 290]
2026-08-05 12:02:42,468 INFO     29 [qwen-vl-text] coord item[98]: text=9.17, bbox=[566, 277, 602, 290]
2026-08-05 12:02:42,468 INFO     29 [qwen-vl-text] coord item[99]: text=3.37, bbox=[619, 277, 650, 290]
2026-08-05 12:02:42,469 INFO     29 [qwen-vl-text] coord item[100]: text=53.7, bbox=[666, 277, 697, 290]
2026-08-05 12:02:42,469 INFO     29 [qwen-vl-text] coord item[101]: text=26.79, bbox=[711, 277, 749, 290]
2026-08-05 12:02:42,469 INFO     29 [qwen-vl-text] coord item[102]: text=3.42, bbox=[764, 277, 795, 290]
2026-08-05 12:02:42,469 INFO     29 [qwen-vl-text] coord item[103]: text=64.6, bbox=[810, 277, 841, 290]
2026-08-05 12:02:42,469 INFO     29 [qwen-vl-text] coord item[104]: text=28.64, bbox=[855, 277, 892, 290]
2026-08-05 12:02:42,469 INFO     29 [qwen-vl-text] coord item[105]: text=MMEF 75/25, bbox=[128, 290, 203, 303]
2026-08-05 12:02:42,469 INFO     29 [qwen-vl-text] coord item[106]: text=[L/s], bbox=[288, 290, 323, 303]
2026-08-05 12:02:42,469 INFO     29 [qwen-vl-text] coord item[107]: text=3.57, bbox=[338, 290, 370, 303]
2026-08-05 12:02:42,469 INFO     29 [qwen-vl-text] coord item[108]: text=0.61, bbox=[384, 290, 415, 303]
2026-08-05 12:02:42,469 INFO     29 [qwen-vl-text] coord item[109]: text=14.4, bbox=[429, 290, 462, 303]
2026-08-05 12:02:42,470 INFO     29 [qwen-vl-text] coord item[110]: text=0.67, bbox=[475, 290, 506, 303]
2026-08-05 12:02:42,470 INFO     29 [qwen-vl-text] coord item[111]: text=18.8, bbox=[520, 290, 552, 303]
2026-08-05 12:02:42,470 INFO     29 [qwen-vl-text] coord item[112]: text=31.03, bbox=[566, 290, 602, 303]
2026-08-05 12:02:42,470 INFO     29 [qwen-vl-text] coord item[113]: text=0.73, bbox=[619, 290, 650, 303]
2026-08-05 12:02:42,470 INFO     29 [qwen-vl-text] coord item[114]: text=20.4, bbox=[666, 290, 697, 303]
2026-08-05 12:02:42,470 INFO     29 [qwen-vl-text] coord item[115]: text=42.01, bbox=[711, 290, 749, 303]
2026-08-05 12:02:42,470 INFO     29 [qwen-vl-text] coord item[116]: text=0.69, bbox=[764, 290, 795, 303]
2026-08-05 12:02:42,470 INFO     29 [qwen-vl-text] coord item[117]: text=19.4, bbox=[810, 290, 841, 303]
2026-08-05 12:02:42,470 INFO     29 [qwen-vl-text] coord item[118]: text=35.02, bbox=[855, 290, 892, 303]
2026-08-05 12:02:42,470 INFO     29 [qwen-vl-text] coord item[119]: text=MEF 50, bbox=[128, 303, 174, 315]
2026-08-05 12:02:42,470 INFO     29 [qwen-vl-text] coord item[120]: text=[L/s], bbox=[288, 303, 323, 315]
2026-08-05 12:02:42,470 INFO     29 [qwen-vl-text] coord item[121]: text=4.01, bbox=[338, 303, 370, 315]
2026-08-05 12:02:42,471 INFO     29 [qwen-vl-text] coord item[122]: text=0.68, bbox=[384, 303, 415, 315]
2026-08-05 12:02:42,471 INFO     29 [qwen-vl-text] coord item[123]: text=17.0, bbox=[429, 303, 462, 315]
2026-08-05 12:02:42,471 INFO     29 [qwen-vl-text] coord item[124]: text=0.90, bbox=[475, 303, 506, 315]
2026-08-05 12:02:42,472 INFO     29 [qwen-vl-text] coord item[125]: text=22.5, bbox=[520, 303, 552, 315]
2026-08-05 12:02:42,473 INFO     29 [qwen-vl-text] coord item[126]: text=32.75, bbox=[566, 303, 602, 315]
2026-08-05 12:02:42,473 INFO     29 [qwen-vl-text] coord item[127]: text=0.89, bbox=[619, 303, 650, 315]
2026-08-05 12:02:42,474 INFO     29 [qwen-vl-text] coord item[128]: text=22.1, bbox=[666, 303, 697, 315]
2026-08-05 12:02:42,474 INFO     29 [qwen-vl-text] coord item[129]: text=30.15, bbox=[711, 303, 749, 315]
2026-08-05 12:02:42,474 INFO     29 [qwen-vl-text] coord item[130]: text=0.88, bbox=[764, 303, 795, 315]
2026-08-05 12:02:42,475 INFO     29 [qwen-vl-text] coord item[131]: text=21.9, bbox=[810, 303, 841, 315]
2026-08-05 12:02:42,475 INFO     29 [qwen-vl-text] coord item[132]: text=29.17, bbox=[855, 303, 892, 315]
2026-08-05 12:02:42,475 INFO     29 [qwen-vl-text] coord item[133]: text=MEF 25, bbox=[128, 315, 174, 328]
2026-08-05 12:02:42,475 INFO     29 [qwen-vl-text] coord item[134]: text=[L/s], bbox=[288, 315, 323, 328]
2026-08-05 12:02:42,475 INFO     29 [qwen-vl-text] coord item[135]: text=1.79, bbox=[338, 315, 370, 328]
2026-08-05 12:02:42,475 INFO     29 [qwen-vl-text] coord item[136]: text=0.19, bbox=[384, 315, 415, 328]
2026-08-05 12:02:42,475 INFO     29 [qwen-vl-text] coord item[137]: text=10.5, bbox=[429, 315, 462, 328]
2026-08-05 12:02:42,475 INFO     29 [qwen-vl-text] coord item[138]: text=0.27, bbox=[475, 315, 506, 328]
2026-08-05 12:02:42,475 INFO     29 [qwen-vl-text] coord item[139]: text=15.2, bbox=[520, 315, 552, 328]
2026-08-05 12:02:42,475 INFO     29 [qwen-vl-text] coord item[140]: text=44.16, bbox=[566, 315, 602, 328]
2026-08-05 12:02:42,475 INFO     29 [qwen-vl-text] coord item[141]: text=0.33, bbox=[619, 315, 650, 328]
2026-08-05 12:02:42,476 INFO     29 [qwen-vl-text] coord item[142]: text=18.7, bbox=[666, 315, 697, 328]
2026-08-05 12:02:42,476 INFO     29 [qwen-vl-text] coord item[143]: text=77.66, bbox=[711, 315, 749, 328]
2026-08-05 12:02:42,476 INFO     29 [qwen-vl-text] coord item[144]: text=0.31, bbox=[764, 315, 795, 328]
2026-08-05 12:02:42,476 INFO     29 [qwen-vl-text] coord item[145]: text=17.6, bbox=[810, 315, 841, 328]
2026-08-05 12:02:42,476 INFO     29 [qwen-vl-text] coord item[146]: text=66.49, bbox=[855, 315, 892, 328]
2026-08-05 12:02:42,476 INFO     29 [qwen-vl-text] coord item[147]: text=FET, bbox=[128, 328, 152, 341]
2026-08-05 12:02:42,476 INFO     29 [qwen-vl-text] coord item[148]: text=[s], bbox=[303, 328, 323, 341]
2026-08-05 12:02:42,476 INFO     29 [qwen-vl-text] coord item[149]: text=7.63, bbox=[384, 328, 415, 341]
2026-08-05 12:02:42,476 INFO     29 [qwen-vl-text] coord item[150]: text=8.01, bbox=[475, 328, 506, 341]
2026-08-05 12:02:42,476 INFO     29 [qwen-vl-text] coord item[151]: text=4.99, bbox=[572, 328, 602, 341]
2026-08-05 12:02:42,476 INFO     29 [qwen-vl-text] coord item[152]: text=7.79, bbox=[619, 328, 650, 341]
2026-08-05 12:02:42,476 INFO     29 [qwen-vl-text] coord item[153]: text=2.14, bbox=[717, 328, 749, 341]
2026-08-05 12:02:42,476 INFO     29 [qwen-vl-text] coord item[154]: text=7.43, bbox=[764, 328, 795, 341]
2026-08-05 12:02:42,476 INFO     29 [qwen-vl-text] coord item[155]: text=-2.60, bbox=[855, 328, 892, 341]
2026-08-05 12:02:42,476 INFO     29 [qwen-vl-text] coord item[156]: text=V backextrapolation ex [L], bbox=[128, 341, 323, 354]
2026-08-05 12:02:42,476 INFO     29 [qwen-vl-text] coord item[157]: text=0.05, bbox=[384, 341, 415, 354]
2026-08-05 12:02:42,477 INFO     29 [qwen-vl-text] coord item[158]: text=0.04, bbox=[475, 341, 506, 354]
2026-08-05 12:02:42,477 INFO     29 [qwen-vl-text] coord item[159]: text=-11.67, bbox=[557, 341, 602, 354]
2026-08-05 12:02:42,477 INFO     29 [qwen-vl-text] coord item[160]: text=0.04, bbox=[619, 341, 650, 354]
2026-08-05 12:02:42,477 INFO     29 [qwen-vl-text] coord item[161]: text=-18.64, bbox=[704, 341, 749, 354]
2026-08-05 12:02:42,477 INFO     29 [qwen-vl-text] coord item[162]: text=0.04, bbox=[764, 341, 795, 354]
2026-08-05 12:02:42,477 INFO     29 [qwen-vl-text] coord item[163]: text=-13.51, bbox=[847, 341, 892, 354]
2026-08-05 12:02:42,477 INFO     29 [qwen-vl-text] coord item[164]: text=PIF, bbox=[128, 354, 152, 367]
2026-08-05 12:02:42,477 INFO     29 [qwen-vl-text] coord item[165]: text=[L/s], bbox=[288, 354, 323, 367]
2026-08-05 12:02:42,477 INFO     29 [qwen-vl-text] coord item[166]: text=3.04, bbox=[384, 354, 415, 367]
2026-08-05 12:02:42,477 INFO     29 [qwen-vl-text] coord item[167]: text=3.37, bbox=[475, 354, 506, 367]
2026-08-05 12:02:42,478 INFO     29 [qwen-vl-text] coord item[168]: text=10.91, bbox=[566, 354, 602, 367]
2026-08-05 12:02:42,478 INFO     29 [qwen-vl-text] coord item[169]: text=3.51, bbox=[619, 354, 650, 367]
2026-08-05 12:02:42,478 INFO     29 [qwen-vl-text] coord item[170]: text=15.70, bbox=[711, 354, 749, 367]
2026-08-05 12:02:42,478 INFO     29 [qwen-vl-text] coord item[171]: text=3.60, bbox=[764, 354, 795, 367]
2026-08-05 12:02:42,479 INFO     29 [qwen-vl-text] coord item[172]: text=18.67, bbox=[855, 354, 892, 367]
2026-08-05 12:02:42,479 INFO     29 [qwen-vl-text] coord item[173]: text=FIV1, bbox=[128, 367, 158, 380]
2026-08-05 12:02:42,480 INFO     29 [qwen-vl-text] coord item[174]: text=[L], bbox=[303, 367, 323, 380]
2026-08-05 12:02:42,480 INFO     29 [qwen-vl-text] coord item[175]: text=2.21, bbox=[384, 367, 415, 380]
2026-08-05 12:02:42,480 INFO     29 [qwen-vl-text] coord item[176]: text=2.56, bbox=[475, 367, 506, 380]
2026-08-05 12:02:42,480 INFO     29 [qwen-vl-text] coord item[177]: text=15.71, bbox=[566, 367, 602, 380]
2026-08-05 12:02:42,480 INFO     29 [qwen-vl-text] coord item[178]: text=2.56, bbox=[619, 367, 650, 380]
2026-08-05 12:02:42,480 INFO     29 [qwen-vl-text] coord item[179]: text=15.66, bbox=[711, 367, 749, 380]
2026-08-05 12:02:42,480 INFO     29 [qwen-vl-text] coord item[180]: text=2.50, bbox=[764, 367, 795, 380]
2026-08-05 12:02:42,480 INFO     29 [qwen-vl-text] coord item[181]: text=13.09, bbox=[855, 367, 892, 380]
2026-08-05 12:02:42,480 INFO     29 [qwen-vl-text] coord item[182]: text=PEF50 % FIF50, bbox=[128, 380, 225, 393]
2026-08-05 12:02:42,480 INFO     29 [qwen-vl-text] coord item[183]: text=[%], bbox=[303, 380, 323, 393]
2026-08-05 12:02:42,481 INFO     29 [qwen-vl-text] coord item[184]: text=22.86, bbox=[375, 380, 415, 393]
2026-08-05 12:02:42,481 INFO     29 [qwen-vl-text] coord item[185]: text=28.15, bbox=[467, 380, 506, 393]
2026-08-05 12:02:42,481 INFO     29 [qwen-vl-text] coord item[186]: text=23.14, bbox=[566, 380, 602, 393]
2026-08-05 12:02:42,481 INFO     29 [qwen-vl-text] coord item[187]: text=25.36, bbox=[619, 380, 650, 393]
2026-08-05 12:02:42,481 INFO     29 [qwen-vl-text] coord item[188]: text=10.95, bbox=[711, 380, 749, 393]
2026-08-05 12:02:42,481 INFO     29 [qwen-vl-text] coord item[189]: text=27.28, bbox=[755, 380, 795, 393]
2026-08-05 12:02:42,482 INFO     29 [qwen-vl-text] coord item[190]: text=19.33, bbox=[855, 380, 892, 393]
2026-08-05 12:02:42,482 INFO     29 [qwen-vl-text] coord item[191]: text=MVV, bbox=[128, 393, 152, 406]
2026-08-05 12:02:42,482 INFO     29 [qwen-vl-text] coord item[192]: text=[L/min], bbox=[272, 393, 323, 406]
2026-08-05 12:02:42,482 INFO     29 [qwen-vl-text] coord item[193]: text=99.77, bbox=[330, 393, 370, 406]
2026-08-05 12:02:42,482 INFO     29 [qwen-vl-text] coord item[194]: text=46.21, bbox=[377, 393, 415, 406]
2026-08-05 12:02:42,482 INFO     29 [qwen-vl-text] coord item[195]: text=46.3, bbox=[429, 393, 462, 406]
2026-08-05 12:02:42,482 INFO     29 [qwen-vl-text] coord item[196]: text=BF MVV, bbox=[128, 406, 174, 419]
2026-08-05 12:02:42,482 INFO     29 [qwen-vl-text] coord item[197]: text=[1/min], bbox=[272, 406, 323, 419]
2026-08-05 12:02:42,482 INFO     29 [qwen-vl-text] coord item[198]: text=75.55, bbox=[377, 406, 415, 419]
2026-08-05 12:02:42,482 INFO     29 [qwen-vl-text] coord item[199]: text=10, bbox=[216, 457, 227, 467]
2026-08-05 12:02:42,483 INFO     29 [qwen-vl-text] coord item[200]: text=Flow [L/s], bbox=[234, 460, 284, 471]
2026-08-05 12:02:42,483 INFO     29 [qwen-vl-text] coord item[201]: text=F/V ex, bbox=[328, 460, 361, 470]
2026-08-05 12:02:42,483 INFO     29 [qwen-vl-text] coord item[202]: text=1, bbox=[430, 461, 459, 471]
2026-08-05 12:02:42,483 INFO     29 [qwen-vl-text] coord item[203]: text=2, bbox=[430, 471, 459, 481]
2026-08-05 12:02:42,483 INFO     29 [qwen-vl-text] coord item[204]: text=3, bbox=[430, 481, 459, 491]
2026-08-05 12:02:42,483 INFO     29 [qwen-vl-text] coord item[205]: text=4, bbox=[430, 491, 459, 501]
2026-08-05 12:02:42,484 INFO     29 [qwen-vl-text] coord item[206]: text=6, bbox=[220, 508, 228, 517]
2026-08-05 12:02:42,484 INFO     29 [qwen-vl-text] coord item[207]: text=4, bbox=[220, 533, 228, 542]
2026-08-05 12:02:42,484 INFO     29 [qwen-vl-text] coord item[208]: text=2, bbox=[220, 558, 228, 568]
2026-08-05 12:02:42,484 INFO     29 [qwen-vl-text] coord item[209]: text=0, bbox=[220, 584, 228, 593]
2026-08-05 12:02:42,484 INFO     29 [qwen-vl-text] coord item[210]: text=Vol [L], bbox=[367, 574, 402, 585]
2026-08-05 12:02:42,485 INFO     29 [qwen-vl-text] coord item[211]: text=1, bbox=[264, 593, 271, 602]
2026-08-05 12:02:42,485 INFO     29 [qwen-vl-text] coord item[212]: text=2, bbox=[297, 593, 304, 602]
2026-08-05 12:02:42,485 INFO     29 [qwen-vl-text] coord item[213]: text=3, bbox=[330, 593, 337, 602]
2026-08-05 12:02:42,485 INFO     29 [qwen-vl-text] coord item[214]: text=4, bbox=[364, 593, 371, 602]
2026-08-05 12:02:42,486 INFO     29 [qwen-vl-text] coord item[215]: text=5, bbox=[397, 593, 404, 602]
2026-08-05 12:02:42,486 INFO     29 [qwen-vl-text] coord item[216]: text=2, bbox=[220, 610, 228, 619]
2026-08-05 12:02:42,486 INFO     29 [qwen-vl-text] coord item[217]: text=4, bbox=[220, 635, 228, 644]
2026-08-05 12:02:42,486 INFO     29 [qwen-vl-text] coord item[218]: text=6, bbox=[220, 661, 228, 670]
2026-08-05 12:02:42,486 INFO     29 [qwen-vl-text] coord item[219]: text=8, bbox=[220, 686, 228, 696]
2026-08-05 12:02:42,486 INFO     29 [qwen-vl-text] coord item[220]: text=10, bbox=[216, 711, 230, 720]
2026-08-05 12:02:42,487 INFO     29 [qwen-vl-text] coord item[221]: text=F/V In, bbox=[330, 706, 360, 716]
2026-08-05 12:02:42,487 INFO     29 [qwen-vl-text] coord item[222]: text=Vol%VCmax, bbox=[516, 503, 575, 513]
2026-08-05 12:02:42,487 INFO     29 [qwen-vl-text] coord item[223]: text=0, bbox=[529, 513, 537, 523]
2026-08-05 12:02:42,487 INFO     29 [qwen-vl-text] coord item[224]: text=0, bbox=[548, 513, 556, 523]
2026-08-05 12:02:42,487 INFO     29 [qwen-vl-text] coord item[225]: text=Vol [L], bbox=[562, 517, 594, 528]
2026-08-05 12:02:42,487 INFO     29 [qwen-vl-text] coord item[226]: text=20, bbox=[524, 525, 538, 535]
2026-08-05 12:02:42,487 INFO     29 [qwen-vl-text] coord item[227]: text=40, bbox=[524, 537, 538, 547]
2026-08-05 12:02:42,488 INFO     29 [qwen-vl-text] coord item[228]: text=60, bbox=[524, 549, 538, 559]
2026-08-05 12:02:42,488 INFO     29 [qwen-vl-text] coord item[229]: text=80, bbox=[524, 561, 538, 571]
2026-08-05 12:02:42,488 INFO     29 [qwen-vl-text] coord item[230]: text=100, bbox=[519, 573, 538, 583]
2026-08-05 12:02:42,488 INFO     29 [qwen-vl-text] coord item[231]: text=2, bbox=[548, 559, 556, 569]
2026-08-05 12:02:42,488 INFO     29 [qwen-vl-text] coord item[232]: text=VCmax, bbox=[572, 570, 608, 579]
2026-08-05 12:02:42,488 INFO     29 [qwen-vl-text] coord item[233]: text=3, bbox=[548, 582, 556, 592]
2026-08-05 12:02:42,488 INFO     29 [qwen-vl-text] coord item[234]: text=4, bbox=[548, 605, 556, 615]
2026-08-05 12:02:42,488 INFO     29 [qwen-vl-text] coord item[235]: text=5, bbox=[548, 628, 556, 638]
2026-08-05 12:02:42,488 INFO     29 [qwen-vl-text] coord item[236]: text=6, bbox=[548, 651, 556, 661]
2026-08-05 12:02:42,488 INFO     29 [qwen-vl-text] coord item[237]: text=Time [s], bbox=[714, 642, 754, 652]
2026-08-05 12:02:42,489 INFO     29 [qwen-vl-text] coord item[238]: text=0, bbox=[557, 661, 564, 670]
2026-08-05 12:02:42,489 INFO     29 [qwen-vl-text] coord item[239]: text=2, bbox=[603, 661, 611, 670]
2026-08-05 12:02:42,489 INFO     29 [qwen-vl-text] coord item[240]: text=4, bbox=[650, 661, 657, 670]
2026-08-05 12:02:42,489 INFO     29 [qwen-vl-text] coord item[241]: text=6, bbox=[697, 661, 704, 670]
2026-08-05 12:02:42,489 INFO     29 [qwen-vl-text] coord item[242]: text=8, bbox=[743, 661, 750, 670]
2026-08-05 12:02:42,489 INFO     29 [qwen-vl-text] coord item[243]: text=10, bbox=[789, 661, 800, 670]
2026-08-05 12:02:42,489 INFO     29 [qwen-vl-text] coord item[244]: text=12, bbox=[835, 661, 846, 670]
2026-08-05 12:02:42,489 INFO     29 [qwen-vl-text] coord item[245]: text=14, bbox=[882, 661, 894, 670]
2026-08-05 12:02:42,489 INFO     29 [qwen-vl-text] coord item[246]: text=意见：, bbox=[107, 735, 151, 749]
2026-08-05 12:02:42,489 INFO     29 [qwen-vl-text] coord item[247]: text=1. 中重度阻塞性肺通气功能障碍。, bbox=[107, 750, 325, 762]
2026-08-05 12:02:42,489 INFO     29 [qwen-vl-text] coord item[248]: text=2. 支气管舒张试验阳性。, bbox=[107, 762, 265, 774]
2026-08-05 12:02:42,489 INFO     29 [qwen-vl-text] coord item[249]: text=(1. 24h内无支气管舒张药物使用史), bbox=[112, 774, 348, 786]
2026-08-05 12:02:42,500 INFO     29 [qwen-vl-text] page=17 — 251/254 coords, api_time=73.9s
2026-08-05 12:02:42,501 INFO     29 [qwen-vl-text] new_positions (255):
[[16, 523.005, 553.35, 736.75, 755.274], [17, 282.625, 334.39, 59.782, 70.728], [17, 148.75, 170.17, 84.2, 94.304], [17, 148.75, 251.08999999999997, 94.304, 104.408], [17, 148.75, 239.19, 104.408, 115.354], [17, 148.75, 170.17, 115.354, 125.458], [17, 148.75, 170.17, 125.458, 135.56199999999998], [17, 148.75, 283.21999999999997, 135.56199999999998, 146.50799999999998], [17, 314.755, 440.29999999999995, 82.51599999999999, 92.61999999999999], [17, 314.755, 422.45, 92.61999999999999, 103.566], [17, 314.755, 418.88, 103.566, 113.67], [17, 314.755, 336.175, 113.67, 124.616], [17, 314.755, 353.43, 124.616, 134.72], [17, 396.27, 421.85499999999996, 135.56199999999998, 145.666], [17, 201.10999999999999, 220.14999999999998, 158.296, 168.4], [17, 236.81, 274.89, 158.296, 168.4], [17, 291.55, 328.44, 158.296, 168.4], [17, 336.77, 358.19, 158.296, 168.4], [17, 377.22999999999996, 414.715, 158.296, 168.4], [17, 423.04499999999996, 445.655, 158.296, 168.4], [17, 464.09999999999997, 500.395, 158.296, 168.4], [17, 508.72499999999997, 530.74, 158.296, 168.4], [17, 76.16, 90.44, 181.03, 191.134], [17, 180.285, 192.185, 181.03, 191.134], [17, 201.10999999999999, 220.14999999999998, 181.03, 191.134], [17, 228.48, 246.92499999999998, 181.03, 191.134], [17, 255.255, 274.89, 181.03, 191.134], [17, 282.625, 301.07, 181.03, 191.134], [17, 309.4, 328.44, 181.03, 191.134], [17, 336.77, 358.19, 181.03, 191.134], [17, 368.305, 386.75, 181.03, 191.134], [17, 396.27, 414.715, 181.03, 191.134], [17, 423.04499999999996, 445.655, 181.03, 191.134], [17, 454.58, 473.025, 181.03, 191.134], [17, 481.95, 500.395, 181.03, 191.134], [17, 508.72499999999997, 530.74, 181.03, 191.134], [17, 76.16, 98.175, 191.134, 202.07999999999998], [17, 180.285, 192.185, 191.134, 202.07999999999998], [17, 201.10999999999999, 220.14999999999998, 191.134, 202.07999999999998], [17, 228.48, 246.92499999999998, 191.134, 202.07999999999998], [17, 255.255, 274.89, 191.134, 202.07999999999998], [17, 282.625, 301.07, 191.134, 202.07999999999998], [17, 309.4, 328.44, 191.134, 202.07999999999998], [17, 336.77, 358.19, 191.134, 202.07999999999998], [17, 368.305, 386.75, 191.134, 202.07999999999998], [17, 396.27, 414.715, 191.134, 202.07999999999998], [17, 423.04499999999996, 445.655, 191.134, 202.07999999999998], [17, 454.58, 473.025, 191.134, 202.07999999999998], [17, 481.95, 500.395, 191.134, 202.07999999999998], [17, 508.72499999999997, 530.74, 191.134, 202.07999999999998], [17, 76.16, 126.14, 202.07999999999998, 212.184], [17, 180.285, 192.185, 202.07999999999998, 212.184], [17, 201.10999999999999, 220.14999999999998, 202.07999999999998, 212.184], [17, 228.48, 246.92499999999998, 202.07999999999998, 212.184], [17, 255.255, 274.89, 202.07999999999998, 212.184], [17, 282.625, 301.07, 202.07999999999998, 212.184], [17, 309.4, 328.44, 202.07999999999998, 212.184], [17, 336.77, 358.19, 202.07999999999998, 212.184], [17, 368.305, 386.75, 202.07999999999998, 212.184], [17, 396.27, 414.715, 202.07999999999998, 212.184], [17, 423.04499999999996, 445.655, 202.07999999999998, 212.184], [17, 454.58, 473.025, 202.07999999999998, 212.184], [17, 481.95, 500.395, 202.07999999999998, 212.184], [17, 508.72499999999997, 530.74, 202.07999999999998, 212.184], [17, 76.16, 139.23, 212.184, 223.13], [17, 180.285, 192.185, 212.184, 223.13], [17, 201.10999999999999, 220.14999999999998, 212.184, 223.13], [17, 228.48, 246.92499999999998, 212.184, 223.13], [17, 255.255, 274.89, 212.184, 223.13], [17, 282.625, 301.07, 212.184, 223.13], [17, 309.4, 328.44, 212.184, 223.13], [17, 336.77, 358.19, 212.184, 223.13], [17, 368.305, 386.75, 212.184, 223.13], [17, 396.27, 414.715, 212.184, 223.13], [17, 423.04499999999996, 445.655, 212.184, 223.13], [17, 454.58, 473.025, 212.184, 223.13], [17, 481.95, 500.395, 212.184, 223.13], [17, 508.72499999999997, 530.74, 212.184, 223.13], [17, 76.16, 103.53, 223.13, 233.23399999999998], [17, 180.285, 192.185, 223.13, 233.23399999999998], [17, 201.10999999999999, 220.14999999999998, 223.13, 233.23399999999998], [17, 228.48, 246.92499999999998, 223.13, 233.23399999999998], [17, 255.255, 274.89, 223.13, 233.23399999999998], [17, 282.625, 301.07, 223.13, 233.23399999999998], [17, 309.4, 328.44, 223.13, 233.23399999999998], [17, 336.77, 358.19, 223.13, 233.23399999999998], [17, 368.305, 386.75, 223.13, 233.23399999999998], [17, 396.27, 414.715, 223.13, 233.23399999999998], [17, 423.04499999999996, 445.655, 223.13, 233.23399999999998], [17, 454.58, 473.025, 223.13, 233.23399999999998], [17, 481.95, 500.395, 223.13, 233.23399999999998], [17, 508.72499999999997, 530.74, 223.13, 233.23399999999998], [17, 76.16, 90.44, 233.23399999999998, 244.17999999999998], [17, 171.35999999999999, 192.185, 233.23399999999998, 244.17999999999998], [17, 201.10999999999999, 220.14999999999998, 233.23399999999998, 244.17999999999998], [17, 228.48, 246.92499999999998, 233.23399999999998, 244.17999999999998], [17, 255.255, 274.89, 233.23399999999998, 244.17999999999998], [17, 282.625, 301.07, 233.23399999999998, 244.17999999999998], [17, 309.4, 328.44, 233.23399999999998, 244.17999999999998], [17, 336.77, 358.19, 233.23399999999998, 244.17999999999998], [17, 368.305, 386.75, 233.23399999999998, 244.17999999999998], [17, 396.27, 414.715, 233.23399999999998, 244.17999999999998], [17, 423.04499999999996, 445.655, 233.23399999999998, 244.17999999999998], [17, 454.58, 473.025, 233.23399999999998, 244.17999999999998], [17, 481.95, 500.395, 233.23399999999998, 244.17999999999998], [17, 508.72499999999997, 530.74, 233.23399999999998, 244.17999999999998], [17, 76.16, 120.785, 244.17999999999998, 255.126], [17, 171.35999999999999, 192.185, 244.17999999999998, 255.126], [17, 201.10999999999999, 220.14999999999998, 244.17999999999998, 255.126], [17, 228.48, 246.92499999999998, 244.17999999999998, 255.126], [17, 255.255, 274.89, 244.17999999999998, 255.126], [17, 282.625, 301.07, 244.17999999999998, 255.126], [17, 309.4, 328.44, 244.17999999999998, 255.126], [17, 336.77, 358.19, 244.17999999999998, 255.126], [17, 368.305, 386.75, 244.17999999999998, 255.126], [17, 396.27, 414.715, 244.17999999999998, 255.126], [17, 423.04499999999996, 445.655, 244.17999999999998, 255.126], [17, 454.58, 473.025, 244.17999999999998, 255.126], [17, 481.95, 500.395, 244.17999999999998, 255.126], [17, 508.72499999999997, 530.74, 244.17999999999998, 255.126], [17, 76.16, 103.53, 255.126, 265.23], [17, 171.35999999999999, 192.185, 255.126, 265.23], [17, 201.10999999999999, 220.14999999999998, 255.126, 265.23], [17, 228.48, 246.92499999999998, 255.126, 265.23], [17, 255.255, 274.89, 255.126, 265.23], [17, 282.625, 301.07, 255.126, 265.23], [17, 309.4, 328.44, 255.126, 265.23], [17, 336.77, 358.19, 255.126, 265.23], [17, 368.305, 386.75, 255.126, 265.23], [17, 396.27, 414.715, 255.126, 265.23], [17, 423.04499999999996, 445.655, 255.126, 265.23], [17, 454.58, 473.025, 255.126, 265.23], [17, 481.95, 500.395, 255.126, 265.23], [17, 508.72499999999997, 530.74, 255.126, 265.23], [17, 76.16, 103.53, 265.23, 276.176], [17, 171.35999999999999, 192.185, 265.23, 276.176], [17, 201.10999999999999, 220.14999999999998, 265.23, 276.176], [17, 228.48, 246.92499999999998, 265.23, 276.176], [17, 255.255, 274.89, 265.23, 276.176], [17, 282.625, 301.07, 265.23, 276.176], [17, 309.4, 328.44, 265.23, 276.176], [17, 336.77, 358.19, 265.23, 276.176], [17, 368.305, 386.75, 265.23, 276.176], [17, 396.27, 414.715, 265.23, 276.176], [17, 423.04499999999996, 445.655, 265.23, 276.176], [17, 454.58, 473.025, 265.23, 276.176], [17, 481.95, 500.395, 265.23, 276.176], [17, 508.72499999999997, 530.74, 265.23, 276.176], [17, 76.16, 90.44, 276.176, 287.122], [17, 180.285, 192.185, 276.176, 287.122], [17, 228.48, 246.92499999999998, 276.176, 287.122], [17, 282.625, 301.07, 276.176, 287.122], [17, 340.34, 358.19, 276.176, 287.122], [17, 368.305, 386.75, 276.176, 287.122], [17, 426.615, 445.655, 276.176, 287.122], [17, 454.58, 473.025, 276.176, 287.122], [17, 508.72499999999997, 530.74, 276.176, 287.122], [17, 76.16, 192.185, 287.122, 298.068], [17, 228.48, 246.92499999999998, 287.122, 298.068], [17, 282.625, 301.07, 287.122, 298.068], [17, 331.41499999999996, 358.19, 287.122, 298.068], [17, 368.305, 386.75, 287.122, 298.068], [17, 418.88, 445.655, 287.122, 298.068], [17, 454.58, 473.025, 287.122, 298.068], [17, 503.965, 530.74, 287.122, 298.068], [17, 76.16, 90.44, 298.068, 309.014], [17, 171.35999999999999, 192.185, 298.068, 309.014], [17, 228.48, 246.92499999999998, 298.068, 309.014], [17, 282.625, 301.07, 298.068, 309.014], [17, 336.77, 358.19, 298.068, 309.014], [17, 368.305, 386.75, 298.068, 309.014], [17, 423.04499999999996, 445.655, 298.068, 309.014], [17, 454.58, 473.025, 298.068, 309.014], [17, 508.72499999999997, 530.74, 298.068, 309.014], [17, 76.16, 94.00999999999999, 309.014, 319.96], [17, 180.285, 192.185, 309.014, 319.96], [17, 228.48, 246.92499999999998, 309.014, 319.96], [17, 282.625, 301.07, 309.014, 319.96], [17, 336.77, 358.19, 309.014, 319.96], [17, 368.305, 386.75, 309.014, 319.96], [17, 423.04499999999996, 445.655, 309.014, 319.96], [17, 454.58, 473.025, 309.014, 319.96], [17, 508.72499999999997, 530.74, 309.014, 319.96], [17, 76.16, 133.875, 319.96, 330.906], [17, 180.285, 192.185, 319.96, 330.906], [17, 223.125, 246.92499999999998, 319.96, 330.906], [17, 277.865, 301.07, 319.96, 330.906], [17, 336.77, 358.19, 319.96, 330.906], [17, 368.305, 386.75, 319.96, 330.906], [17, 423.04499999999996, 445.655, 319.96, 330.906], [17, 449.22499999999997, 473.025, 319.96, 330.906], [17, 508.72499999999997, 530.74, 319.96, 330.906], [17, 76.16, 90.44, 330.906, 341.852], [17, 161.84, 192.185, 330.906, 341.852], [17, 196.35, 220.14999999999998, 330.906, 341.852], [17, 224.315, 246.92499999999998, 330.906, 341.852], [17, 255.255, 274.89, 330.906, 341.852], [17, 76.16, 103.53, 341.852, 352.798], [17, 161.84, 192.185, 341.852, 352.798], [17, 224.315, 246.92499999999998, 341.852, 352.798], [17, 128.51999999999998, 135.065, 384.794, 393.214], [17, 139.23, 168.98, 387.32, 396.582], [17, 195.16, 214.795, 387.32, 395.74], [17, 255.85, 273.10499999999996, 388.162, 396.582], [17, 255.85, 273.10499999999996, 396.582, 405.002], [17, 255.85, 273.10499999999996, 405.002, 413.42199999999997], [17, 255.85, 273.10499999999996, 413.42199999999997, 421.842], [17, 130.9, 135.66, 427.736, 435.31399999999996], [17, 130.9, 135.66, 448.786, 456.364], [17, 130.9, 135.66, 469.83599999999996, 478.256], [17, 130.9, 135.66, 491.728, 499.306], [17, 218.36499999999998, 239.19, 483.308, 492.57], [17, 157.07999999999998, 161.245, 499.306, 506.88399999999996], [17, 176.715, 180.88, 499.306, 506.88399999999996], [17, 196.35, 200.515, 499.306, 506.88399999999996], [17, 216.57999999999998, 220.74499999999998, 499.306, 506.88399999999996], [17, 236.215, 240.38, 499.306, 506.88399999999996], [17, 130.9, 135.66, 513.62, 521.198], [17, 130.9, 135.66, 534.67, 542.2479999999999], [17, 130.9, 135.66, 556.562, 564.14], [17, 130.9, 135.66, 577.612, 586.0319999999999], [17, 128.51999999999998, 136.85, 598.662, 606.24], [17, 196.35, 214.2, 594.452, 602.872], [17, 307.02, 342.125, 423.526, 431.94599999999997], [17, 314.755, 319.515, 431.94599999999997, 440.366], [17, 326.06, 330.82, 431.94599999999997, 440.366], [17, 334.39, 353.43, 435.31399999999996, 444.57599999999996], [17, 311.78, 320.11, 442.05, 450.46999999999997], [17, 311.78, 320.11, 452.154, 460.574], [17, 311.78, 320.11, 462.258, 470.678], [17, 311.78, 320.11, 472.36199999999997, 480.782], [17, 308.805, 320.11, 482.466, 490.88599999999997], [17, 326.06, 330.82, 470.678, 479.09799999999996], [17, 340.34, 361.76, 479.94, 487.518], [17, 326.06, 330.82, 490.044, 498.464], [17, 326.06, 330.82, 509.40999999999997, 517.8299999999999], [17, 326.06, 330.82, 528.776, 537.196], [17, 326.06, 330.82, 548.1419999999999, 556.562], [17, 424.83, 448.63, 540.564, 548.984], [17, 331.41499999999996, 335.58, 556.562, 564.14], [17, 358.78499999999997, 363.54499999999996, 556.562, 564.14], [17, 386.75, 390.91499999999996, 556.562, 564.14], [17, 414.715, 418.88, 556.562, 564.14], [17, 442.085, 446.25, 556.562, 564.14], [17, 469.455, 476.0, 556.562, 564.14], [17, 496.825, 503.37, 556.562, 564.14], [17, 524.79, 531.93, 556.562, 564.14], [17, 63.665, 89.845, 618.87, 630.658], [17, 63.665, 193.375, 631.5, 641.6039999999999], [17, 63.665, 157.67499999999998, 641.6039999999999, 651.708], [17, 66.64, 207.06, 651.708, 661.812], [17, 66.64, 207.06, 651.708, 661.812], [17, 0, 0, 0, 0], [17, 0, 0, 0, 0], [17, 0, 0, 0, 0]]
2026-08-05 12:02:42,501 INFO     29 [qwen-vl-text] ═══ DONE ═══ 255 positions, pages=2, time=149.3s
2026-08-05 12:02:42,518 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 12:02:42,518 INFO     29 [qwen-vl-text] LLM output (len=1436):
{
  "exam_date": "2025-06-09",
  "report_date": "2025-03-16",
  "exam_name": "肺功能报告",
  "exam_category": "other",
  "body_part": null,
  "patient_name": null,
  "patient_gender": "Male",
  "department": null,
  "bed_number": "100004",
  "findings": "预计值: ERS 93\n出生日期: 1978/12/13\n性别: Male\n地区修正.: Chinese\n年龄: 46\n体重 (Kg): 84.0\n身高 (cm): 178.0\nBMI (Kg/m²): 26.5\n吸烟: 否\n\n| Parameter | UM | Pred. | BEST#1 | %Pred. | POST#3 | %Pred. | %Test#1 |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n| Best FVC | l(btps) | 4.72 | 2.74 | 58 | 3.22 | 68 | +17.4 |\n| FVC | l(btps) | 4.72 | 2.74 | 58 | 3.22 | 68 | +17.4 |\n| FEV1 | l(btps) | 3.83 | 1.35 | 35 | 1.72 | 45 | +27.5 |\n| PEF | l/sec | 9.10 | 2.96 | 32 | 3.30 | 36 | +11.4 |\n| FEV6 | l(btps) | 5.01 | 2.71 | 54 | 3.20 | 64 | +18.2 |\n| PIF | l/sec | 4.61 | 5.52 | | | | +19.9 |\n| FEV1/FVC% | % | 78.9 | 49.1 | 62 | 53.4 | 68 | +8.7 |\n| FEV6/FVC% | % | 98.8 | 99.5 | | | | +0.7 |\n| FEV1/FEV6% | % | 49.7 | 53.6 | | | | +7.9 |\n| FEF25-75% | l/sec | 4.18 | 0.64 | 15 | 0.86 | 21 | +34.7 |\n| MEF75% | l/sec | 7.91 | 1.42 | 18 | 1.98 | 25 | +39.2 |\n| MEF50% | l/sec | 4.97 | 0.75 | 15 | 1.02 | 20 | +36.2 |\n| MEF25% | l/sec | 2.11 | 0.31 | 15 | 0.41 | 19 | +32.4 |\n| FET100% | sec | 6.2 | 6.1 | | | | -1.9 |\n| VEXT | ml | 60 | 73 | | | | +21.7 |\n| IC | l(btps) | 2.47 | 2.27 | | | | -8.1 |",
  "conclusion": "支气管舒张试验阳性。",
  "physician": null,
  "reviewer": null
}
2026-08-05 12:02:42,519 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1003494, prompt_len=2534
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共253行）
["临海市第一人民医院医共体", "肺功能报告", "COSMED", "姓名:", "科室/床号:", "100004", "ID:", "日期:", "2025/6/9", "预计值:", "ERS 93", "出生日期: 1978/12/13", "性别: Male", "地区修正.: Chinese", "详细描述:", "Company:", "年龄: 46", "体重 (Kg): 84.0", "身高 (cm): 178.0", "BMI (Kg/m²): 26.5", "吸烟: 否", "用力肺活量 Forced Vital Capacity", "F(l/s)", "14", "13", "12", "11", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0", "-1", "-2", "-3", "-4", "-5", "-6", "-7", "-8", "V(l)", "8", "7", "6", "5", "4", "3", "2", "1", "0", "-1", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12t(s)", "FVC", "PEF", "MEF75%", "MEF50%", "MEF25%", "FVC", "V(l)", "8", "7", "6", "5", "4", "3", "2", "1", "0", "-1", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12t(s)", "FEV1", "ATS", "FVC", "PEF", "MEF75%", "MEF50%", "MEF25%", "FVC", "V(l)", "8", "7", "6", "5", "4", "3", "2", "1", "0", "-1", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12t(s)", "Parameter", "UM", "Pred.", "BEST#1", "%Pred.", "POST#3", "%Pred.", "%Test#1", "Best FVC", "l(btps)", "4.72", "2.74", "58", "3.22", "68", "+17.4", "FVC", "l(btps)", "4.72", "2.74", "58", "3.22", "68", "+17.4", "FEV1", "l(btps)", "3.83", "1.35", "35", "1.72", "45", "+27.5", "PEF", "l/sec", "9.10", "2.96", "32", "3.30", "36", "+11.4", "FEV6", "l(btps)", "5.01", "2.71", "54", "3.20", "64", "+18.2", "PIF", "l/sec", "4.61", "5.52", "+19.9", "FEV1/FVC%", "%", "78.9", "49.1", "62", "53.4", "68", "+8.7", "FEV6/FVC%", "%", "98.8", "99.5", "+0.7", "FEV1/FEV6%", "%", "49.7", "53.6", "+7.9", "FEF25-75%", "l/sec", "4.18", "0.64", "15", "0.86", "21", "+34.7", "MEF75%", "l/sec", "7.91", "1.42", "18", "1.98", "25", "+39.2", "MEF50%", "l/sec", "4.97", "0.75", "15", "1.02", "20", "+36.2", "MEF25%", "l/sec", "2.11", "0.31", "15", "0.41", "19", "+32.4", "FET100%", "sec", "6.2", "6.1", "-1.9", "VEXT", "ml", "60", "73", "+21.7", "IC", "l(btps)", "2.47", "2.27", "-8.1", "诊断:", "支气管舒张试验阳性。", "签名:"]

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
2026-08-05 12:02:47,966 INFO     29 [qwen-vl-parser] text API response (len=1572):
["粗，两肺均可闻及干啰音及呼气相哮鸣音。心率84次/分，律齐，心脏各瓣膜听诊区均未", "闻及病理性杂音。腹平软，全腹无压痛及反跳痛。肝脾肋下未触及。双下肢无浮肿。][专", "科检查：颜面部轻度紫绀，喘息貌，口唇轻度紫绀，咽腔充血，双侧扁桃腺未见肿大及脓", "点。颈软，颈静脉充盈。双肺呼吸音粗，两肺均可闻及干啰音及呼气相哮鸣音。][辅助检", "查：暂无。]初步诊断：1.支气管哮喘急性发作；2.慢性阻塞性肺疾病？3.高血压病2", "级 低危组。诊断依据：1.老年女性；2.反复咳痰喘6年余，再发10余天；3.临床表现：6", "年余来患者每遇吸入刺激性气味或冷空气后出现咳嗽、咳痰及胸闷、气喘，咳嗽咳痰症状", "呈阵发性发作，痰液易咳出，多为白粘痰，每次症状发作时多就诊于我院呼吸内科，曾完", "善肺功能检查确诊为“支气管哮喘”，经抗感染、抗炎、解痉平喘、雾化吸入及对症治疗", "后症状好转出院，出院后院外规律吸入“布地格福气雾剂 2揿/次，一日两次”治疗，胸", "闷、气喘症状控制不佳，活动耐力呈进行性下降(以致目前上2层楼或步行500米左右即气", "喘严重)，3月余前患者因受凉再次出现咳嗽、咳痰、胸闷、气喘，在家应用“布地格福气", "雾剂”吸入治疗及口服“罗红霉素胶囊7天及甲泼尼龙片 8mg/次，一日两次，间隔1-2天", "每日减1片”治疗，咳嗽咳痰及胸闷、气喘症状有所好转后停用上述口服药物，后改为应", "用“布地奈德气雾剂2揿/次，一日三次联合乌美溴铵维兰特罗粉雾剂1吸/次，一日一次”", "联合维持治疗。10余天前患者无诱因再次出现咳嗽、咳痰、胸闷、气喘，不伴发热，在家", "应用“布地奈德气雾剂2揿/次，一日三次联合乌美溴铵维兰特罗粉雾剂1吸/次，一日一", "次”吸入治疗及再次口服“罗红霉素胶囊7天及甲泼尼龙片 8mg/次，一日两次，间隔1-2", "天每日减1片”治疗10余天来咳嗽咳痰及胸闷、气喘症状未见好转；4.既往史及查体：颜面", "部轻度紫绀，喘息貌，口唇轻度紫绀，咽腔充血，双侧扁桃腺未见肿大及脓点。颈软，颈", "静脉充盈。双肺呼吸音粗，两肺均可闻及干啰音及呼气相哮鸣音。鉴别诊断：①慢性阻", "塞性肺疾病 急性加重期：支持点为患者有胸闷、气短或呼吸困难症状，早期在劳力时出", "现，后逐渐加重，以致在日常活动甚至休息时也感到气短；早期胸片可无变化，不支持点", "为患者无慢性支气管炎病史及长期吸烟史，肺功能检查提示有气流受限可进一步明确；②", "急性左心衰引起的呼吸困难：支持点为多有突发胸闷、气喘及呼吸困难症状，不支持点为", "患者无咯粉红色泡沫痰，查体未闻及肺底湿啰音及心脏杂音等，需进一步行胸部CT检查进", "一步明确；③急性肺动脉栓塞：支持点为不明原因的胸闷、胸痛、呼吸困难，咳嗽，咯", "血，且多与体位改变有关，不支持点为血气分析可见低氧、低二氧化碳血症，D-二聚体阳", "性，心电图可见SIQIII综合征，胸部CT可见楔形高密度影，CTA、MRA、肺通气灌注扫", "描及血管造影可见肺动脉充盈缺损。针对病情制定以下诊疗计划： 1.进一步完善心", "电图、肺功能、胸部CT、动脉血气、血常规、C反应蛋白、PCT、白介素-6等相关检查明确", "肺部有无炎性病变、目前肺功能情况以及各器官功能有无异常；2.患者病史长，无长期吸", "烟史，可给予吸氧、解痉平喘、雾化吸入、扩张气管及对症治疗，必要时给予无创呼吸机", "辅助呼吸或气管插管转入重症监护室治疗；3.已将目前病情及治疗措施告知患者，患者表", "示理解并签字，因患者既往有“高血压病”病史，嘱患者低盐低脂饮食，戒烟戒酒等健康", "教育。", "副主任医师签名：", "第 2 页"]
2026-08-05 12:02:47,969 INFO     29 [qwen-vl-parser] page=6 text: 38 lines (bbox 172-209)
2026-08-05 12:02:47,969 INFO     29 [qwen-vl-parser] page=6 text: 38 sections
2026-08-05 12:02:48,577 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6475922, prompt_len=764
2026-08-05 12:02:51,595 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-01-04"}
```
2026-08-05 12:02:51,596 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=2026-01-04
2026-08-05 12:02:51,616 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6475922, prompt_len=401
2026-08-05 12:02:54,085 INFO     29 [qwen-vl-parser] text API response (len=270):
["病程记录", "姓名：", "科室：呼吸与危重症医学一科 床号：054 住院号：26000328", "2026-01-04 13:40 VTE防治病程记录", "2026-01-04 13:30对患者进行入院后24小时VTE风险评估，Padua评估总分为1分，评估级别为：低危。出血风险：", "无。无机械预防禁忌症。防治措施：（一）一般预防方法：进行静脉血栓栓塞症相关知识宣教，鼓励及早进行主动与被动活", "动，早期进行功能锻炼，需进一步完善检查，根据病情变化，评估、调整预防治疗措施。", "主任医师签名：", "第 1 页"]
2026-08-05 12:02:54,086 INFO     29 [qwen-vl-parser] page=7 text: 9 lines (bbox 210-218)
2026-08-05 12:02:54,086 INFO     29 [qwen-vl-parser] page=7 text: 9 sections
2026-08-05 12:02:54,571 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9479503, prompt_len=764
2026-08-05 12:02:57,256 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 12:02:57,259 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-05 12:02:57,291 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9479503, prompt_len=401
2026-08-05 12:03:07,793 INFO     29 [qwen-vl-parser] text API response (len=1418):
["2026-01-05 09:00", "医师查房记录", "今随", "任医师查房，患者神志清，精神差，饮食尚可，昨日入院至今晨无", "发热，间断咳嗽咳痰，痰不易咳出，胸闷、气喘症状较入院时未见好转，咳嗽咳痰后胸", "闷、气喘症状明显加重，无胸痛，无夜间阵发性呼吸困难及端坐呼吸，大小便正常，夜间", "睡眠差，今查体：T:36.4℃，R:21次/分，BP:168/95mmHg，颜面部无紫绀，全身皮肤粘", "膜未见皮疹及出血点。全身浅表淋巴结均未触及肿大。双瞳孔等大等圆，直径为3mm，对", "光反射灵敏。口唇无紫绀，咽腔充血，双侧扁桃腺未见肿大及脓点。颈软，颈静脉充盈。", "双肺呼吸音粗，两肺均可闻及干啰音及呼气相哮鸣音。心率84次/分，律齐，心脏各瓣膜", "听诊区均未闻及病理性杂音。腹平软，全腹无压痛及反跳痛。肝脾肋下未触及。双下肢无", "浮肿。辅助检查：2026-01-04 血气生化（呼一）：PH值 7.448，二氧化碳分压（9-", "HR）39.7，氧分压（9-HR）80.5↓，氧饱和度 95.9%，剩余碱 3.2mmol/L↑，细胞外", "剩余碱 3.4mmol/L↑；2026-01-04 常规心电图检查（十二导）诊断意见：大致正常心电", "图，", "任医师详细听取病史及查检病人后指出患者为老年女性，综合分析如下：①", "病史长达6年余；②无长期吸烟史；③既往曾在我院呼吸二科住院期间完善检查“支气管", "哮喘”诊断明确，院外先后规律应用“布地格福气雾剂、布地奈德气雾剂联合乌美溴铵维", "兰特罗粉雾剂”治疗，胸闷、气喘症状时轻时重，根据支气管哮喘发病机制，导致该病机", "制主要为气道免疫-炎症机制及神经调节机制，因气道慢性炎症反应是由多种炎症细胞、", "炎症介质和细胞因子共同参与相互作用的结果，同时哮喘病人β肾上腺素受体功能低下，", "病人对吸入组胺和乙酰甲胆碱的气道反应性显著增高提示存在胆碱能神经张力的增加，结", "合患者临床表现及发病机制，建议完善胸部CT了解此次发病有无合并肺部感染性病变综上", "所述，同时完善肺功能检查、FeNO检查了解目前气道阻塞程度、评估气道炎症、哮喘控制", "水平及及吸入性激素治疗的反应，完善血常规、C反应蛋白、PCT、血沉、白介素-6等炎症", "指标以决定有无炎性因子大量释放，因患者入院时未出现讲话时有中断、三凹征、烦躁、", "大汗淋漓以及响亮的哮鸣音，故将患者病情程度列为轻度，此类病人机体免疫力低下，极", "易因上呼吸道感染诱发肺部感染导致气道持续痉挛继而合并呼吸衰竭危及生命，此次住院", "需通过肺功能了解肺廓清能力有无下降、气道有无重塑，目前建议给予二羟丙茶碱注射液", "0.5g，ivgtt，qd扩张气管、奥美拉唑钠注射液40mg，ivgtt，qd抑酸护胃、吸入用布地奈", "德混悬液2mg+硫酸特布他林雾化吸入用溶液5mg+吸入用乙酰半胱氨酸溶液3ml雾化吸入抗炎", "及减轻气道水肿治疗，根据症状缓解程度、体征及哮鸣音的变化以决定是否应用全身糖皮", "质激素，密切观察病情变化，嘱患者避免受凉，减少活动及氧耗，注意休息，已将目前病", "情及风险告知患者及其家属，其家属表示理解并签署知情同意书，上级医师指示已执", "行。", "主任医师签名：", "副主任医师签名：", "第 2 页"]
2026-08-05 12:03:07,797 INFO     29 [qwen-vl-parser] page=8 text: 38 lines (bbox 219-256)
2026-08-05 12:03:07,797 INFO     29 [qwen-vl-parser] page=8 text: 38 sections
2026-08-05 12:03:08,263 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9207727, prompt_len=764
2026-08-05 12:03:11,702 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 12:03:11,703 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-05 12:03:11,731 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9207727, prompt_len=401
2026-08-05 12:03:21,286 INFO     29 [qwen-vl-parser] text API response (len=1188):
["病程记录", "姓名：", "科室：呼吸与危重症医学一科  床号：054  住院号：26000328", "2026-01-06  09:00  任医师查房记录", "今随...主任医师查房，患者神志清，精神差，饮食尚可，昨日至今晨无发", "热，间断咳嗽咳痰，痰不易咳出，胸闷、气喘症状较入院时略有好转，咳嗽咳痰后胸闷、", "气喘症状明显加重，无胸痛，无夜间阵发性呼吸困难及端坐呼吸，大小便正常，夜间睡眠", "差，今查体：T:36.5℃，R:21次/分，BP:127/69mmHg，颜面部无紫绀，全身皮肤粘膜未", "见皮疹及出血点。全身浅表淋巴结均未触及肿大。双瞳孔等大等圆，直径为3mm，对光反", "射灵敏。口唇无紫绀，咽腔充血，双侧扁桃腺未见肿大及脓点。颈软，颈静脉充盈。双肺", "呼吸音粗，两肺仍可闻及干啰音及呼气相哮鸣音。心率80次/分，律齐，心脏各瓣膜听诊", "区均未闻及病理性杂音。腹平软，全腹无压痛及反跳痛。肝脾肋下未触及。双下肢无浮", "肿。辅助检查：2026-01-05  血沉：血沉 5mm/h；2026-01-05  血常规+快速C反应蛋", "白：白细胞(9-HR) 5.3×10^9/L，中性粒细胞百分比 53.2%，淋巴细胞百分比 29.0%，", "嗜酸性粒细胞计数 0.54×10^9/L↑，C反应蛋白 <5.0mg/L；2026-01-05  心肌酶谱：", "乳酸脱氢酶(9-HR) 113U/L↓；2026-01-05  纤溶两项(D-Dimer FDP)、D-二聚体测", "定、凝血四项、血糖测定、肾功三项、肝功九项、电解质四项、降钙素原(PCT)定里检", "测、N末端B型钠尿肽原测定、肺癌五项均在正常范围；2026-01-06  尿常规、粪便常规", "均在正常范围，张祥杰主任医师查检病人后指出患者气道痉挛未见缓解及解除，建议加大", "吸入性糖皮质激素剂量及频率以减轻气道免疫炎症，同时加用高流里给氧纠正缺氧的同时", "湿化气道以改善气道痉挛，尽快完善胸部CT了解此次发病有无合并肺部感染性病变综上所", "述，完善肺功能检查、FeNO检查了解目前气道阻塞程度、评估气道炎症、哮喘控制水平及", "及吸入性激素治疗的反应，继续给予二羟丙茶碱注射液0.5g，ivgtt，qd扩张气管、奥美", "拉唑钠注射液40mg，ivgtt，qd抑酸护胃、吸入用布地奈德混悬液2mg+硫酸特布他林雾化", "吸入用溶液5mg+吸入用乙酰半胱氨酸溶液3ml雾化吸入抗炎及减轻气道水肿治疗，根据症状", "缓解程度、体征及哮鸣音的变化以决定是否应用全身糖皮质激素，密切观察病情变化，嘱", "患者避免受凉，减少活动及氧耗，注意休息，上级医师指示已执行。", "主任医师签名：", "副主任医师签名：", "第 1 页"]
2026-08-05 12:03:21,288 INFO     29 [qwen-vl-parser] page=9 text: 30 lines (bbox 257-286)
2026-08-05 12:03:21,288 INFO     29 [qwen-vl-parser] page=9 text: 30 sections
2026-08-05 12:03:21,768 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9205486, prompt_len=764
2026-08-05 12:03:24,744 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 12:03:24,747 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=None
2026-08-05 12:03:24,782 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9205486, prompt_len=401
2026-08-05 12:03:34,785 INFO     29 [qwen-vl-parser] text API response (len=1278):
["病程记录", "姓名：", "科室：呼吸与危重症医学一科 床号：004 住院号：26000328", "2026-01-09 09:00 查房记录", "今随", "主任医师查房，患者神志清，精神差，饮食尚可，近几日来无发热，", "间断咳嗽咳痰，痰不易咳出，偶可咳出白粘痰，自01月07日给予静脉输注甲泼尼龙琥珀酸", "钠注射液40mg/日后近两日来胸闷、气喘症状较入院时有所减轻，咳嗽咳痰后胸闷、气喘", "症状亦较前减轻，无胸痛，无夜间阵发性呼吸困难及端坐呼吸，大小便正常，夜间睡眠", "差，今查体：T:36.4℃，R:22次/分，BP:124/68mmHg，口唇无紫绀，咽腔无充血，双侧", "扁桃腺未见肿大及脓点。颈软，颈静脉充盈。双肺呼吸音粗，两肺仍可闻及干啰音及呼气", "相哮鸣音。心率84次/分，律齐。腹平软，全腹无压痛及反跳痛。肝脾肋下未触及。双下", "肢无浮肿。辅助检查：2026-01-08 痰涂片组合：革兰氏阳性球菌 查到，革兰氏阳性杆", "菌 查到，革兰氏阴性杆菌 查到；2026-01-08 痰液一般细菌培养：嗜血杆菌未生长；", "2026-01-07 呼出气一氧化氮测定（FeNO）诊断意见：76ppb，提示嗜酸性气道炎症；2026-", "01-07 肺功能报告示1.一秒量低，肺活量正常，未见限制因素，一秒率异常，提示存在", "阻塞型通气功能障碍；2.峰流量过低，提示可能存在大气道阻塞，呼气末指标低，小气道", "功能异常，中度阻塞型通气功能障碍；3.最大分钟通气量下降，MVV:57.93L/min，占预计", "值70.5%，通气储备92%，4.弥散量和比弥散量都正常，未见换气功能障碍；5.FEV1改善率", "0.6%，改善量为8.3ml，舒张试验阴性；2026-01-07 胸部CT平扫复查并与2024年04月23", "日前片检查CT对比诊断意见：1.提示支气管炎；2.左下肺前内基底段磨玻璃结节，较前略", "示饱满，余双肺数个磨玻璃结节较前相仿；3.双肺多发实性微小结节，请随诊；5.纵隔内", "多发淋巴结，部分稍大；6.主动脉及冠状动脉粥样硬化征象，张祥杰主任医师结合上述检", "查结果，查房后指示患者应用全身糖皮质激素后气道痉挛有所减轻，胸闷、气喘症状有所", "好转，同时患者血常规示嗜酸性粒细胞数目明显偏高，FeNO提示嗜酸性气道炎症，故建议", "继续给予吸入性激素联合全身应用糖皮质激素抗气道炎症治疗，胸部CT提示肺部支气管炎", "性改变，痰涂片检出混合细菌感染，故建议继续给予莫西沙星氯化钠注射液0.4g，", "ivgtt，qd感染治疗，余治疗继续同前，待气道痉挛完全解除后复查肺功能了解气道有无", "阻塞及有无哮喘因素存在，密切观察病情变化，必要时给予短期无创呼吸机辅助呼吸治疗", "以防止呼吸肌疲劳导致呼吸衰竭的发生，嘱患者避免受凉，减少活动及氧耗，注意休息，", "上级医师指示已执行。", "主任医师签名：", "副主任医师签名：", "第 2 页"]
2026-08-05 12:03:34,787 INFO     29 [qwen-vl-parser] page=10 text: 34 lines (bbox 287-320)
2026-08-05 12:03:34,787 INFO     29 [qwen-vl-parser] page=10 text: 34 sections
2026-08-05 12:03:35,253 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9230618, prompt_len=764
2026-08-05 12:03:38,811 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 12:03:38,813 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=None
2026-08-05 12:03:38,840 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9230618, prompt_len=401
2026-08-05 12:03:44,963 INFO     29 [qwen-vl-parser] text API response (len=672):
["病程记录", "姓名：", "科室：呼吸与危重症医学一科 床号：004 住院号：26000328", "2026-01-12 09:00 日常病程记录", "今查患者神志清，精神较前有所好转，饮食可，近几日来无发热，间断咳嗽咳", "痰，痰较前易咳出，痰多为白粘痰，痰量较前减少，且患者诉偶有恶心干呕，胸闷、气喘", "症状较入院时明显减轻，咳嗽咳痰后胸闷、气喘症状亦较前进一步减轻，未诉其他不适症", "状，大小便正常，夜间睡眠可，今查体：T:36.6℃，R:22次/分，BP:131/67mmHg，口唇", "无紫绀，咽腔无充血，双侧扁桃腺未见肿大及脓点。颈软，颈静脉充盈。双肺呼吸音粗，", "两肺仍可闻及少许干啰音，未闻及湿啰音及呼气相哮鸣音。心率80次/分，律齐。腹平", "软，全腹无压痛及反跳痛。肝脾肋下未触及。双下肢无浮肿。患者应用全身糖皮质激素后", "气道痉挛明显减轻，胸闷、气喘症状有所好转，提示治疗有效，患者血常规示嗜酸性粒细", "胞数目明显偏高，FeNO提示嗜酸性气道炎症，继续给予吸入性激素联合全身应用糖皮质激", "素抗气道炎症治疗，注意糖皮质激素的逐步减量，防止撤停激素过快导致反跳现象发生，", "可停用二羟丙茶碱主要是扩张气管治疗，建议停用莫西沙星氯化钠注射液，观察胃肠道症", "状有无改善，余治疗继续同前，密切观察病情变化，必要时给予短期无创呼吸机辅助呼吸", "治疗以防止呼吸肌疲劳导致呼吸衰竭的发生，嘱患者避免受凉，减少活动及氧耗，注意休", "息。", "副主任医师签名", "第 1 页"]
2026-08-05 12:03:44,966 INFO     29 [qwen-vl-parser] page=11 text: 20 lines (bbox 321-340)
2026-08-05 12:03:44,966 INFO     29 [qwen-vl-parser] page=11 text: 20 sections
2026-08-05 12:03:45,438 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8923813, prompt_len=764
2026-08-05 12:03:47,849 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 12:03:47,852 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=None
2026-08-05 12:03:47,879 INFO     29 [qwen-vl-text] coord API raw response (len=11284):
[
	{"text": "临海市第一人民医院医共体", "bbox": [386, 71, 610, 85]},
	{"text": "肺功能报告", "bbox": [451, 85, 544, 99]},
	{"text": "COSMED", "bbox": [87, 119, 150, 130]},
	{"text": "姓名:", "bbox": [73, 139, 111, 150]},
	{"text": "科室/床号:", "bbox": [73, 150, 146, 161]},
	{"text": "ID:", "bbox": [73, 163, 94, 174]},
	{"text": "日期:", "bbox": [73, 174, 111, 185]},
	{"text": "预计值:", "bbox": [73, 185, 126, 197]},
	{"text": "出生日期: 1978/12/13", "bbox": [428, 137, 587, 147]},
	{"text": "性别: Male", "bbox": [428, 148, 544, 159]},
	{"text": "地区修正.: Chinese", "bbox": [428, 160, 567, 170]},
	{"text": "详细描述:", "bbox": [428, 171, 498, 182]},
	{"text": "Company:", "bbox": [428, 183, 507, 194]},
	{"text": "年龄: 46", "bbox": [784, 137, 892, 147]},
	{"text": "体重 (Kg): 84.0", "bbox": [784, 148, 909, 159]},
	{"text": "身高 (cm): 178.0", "bbox": [784, 159, 917, 170]},
	{"text": "BMI (Kg/m²): 26.5", "bbox": [784, 170, 909, 181]},
	{"text": "吸烟: 否", "bbox": [784, 182, 895, 193]},
	{"text": "用力肺活量 Forced Vital Capacity", "bbox": [165, 203, 407, 214]},
	{"text": "F(l/s)", "bbox": [88, 216, 119, 226]},
	{"text": "14", "bbox": [76, 224, 90, 233]},
	{"text": "13", "bbox": [76, 240, 90, 249]},
	{"text": "12", "bbox": [76, 256, 90, 265]},
	{"text": "11", "bbox": [76, 271, 90, 280]},
	{"text": "10", "bbox": [76, 287, 90, 296]},
	{"text": "9", "bbox": [81, 303, 90, 312]},
	{"text": "8", "bbox": [81, 319, 90, 328]},
	{"text": "7", "bbox": [81, 335, 90, 344]},
	{"text": "6", "bbox": [81, 351, 90, 360]},
	{"text": "5", "bbox": [81, 367, 90, 376]},
	{"text": "4", "bbox": [81, 383, 90, 392]},
	{"text": "3", "bbox": [81, 399, 90, 408]},
	{"text": "2", "bbox": [81, 415, 90, 424]},
	{"text": "1", "bbox": [81, 431, 90, 440]},
	{"text": "0", "bbox": [81, 447, 90, 456]},
	{"text": "-1", "bbox": [79, 463, 90, 472]},
	{"text": "-2", "bbox": [81, 479, 90, 488]},
	{"text": "-3", "bbox": [81, 495, 90, 504]},
	{"text": "-4", "bbox": [81, 511, 90, 520]},
	{"text": "-5", "bbox": [81, 527, 90, 536]},
	{"text": "-6", "bbox": [81, 543, 90, 552]},
	{"text": "-7", "bbox": [81, 559, 90, 568]},
	{"text": "-8", "bbox": [81, 575, 90, 584]},
	{"text": "V(l)", "bbox": [509, 202, 528, 211]},
	{"text": "8", "bbox": [502, 211, 511, 220]},
	{"text": "7", "bbox": [502, 230, 511, 239]},
	{"text": "6", "bbox": [502, 250, 511, 259]},
	{"text": "5", "bbox": [502, 270, 511, 279]},
	{"text": "4", "bbox": [502, 290, 511, 299]},
	{"text": "3", "bbox": [502, 310, 511, 319]},
	{"text": "2", "bbox": [502, 330, 511, 339]},
	{"text": "1", "bbox": [502, 350, 511, 359]},
	{"text": "0", "bbox": [502, 370, 511, 379]},
	{"text": "-1", "bbox": [515, 385, 526, 394]},
	{"text": "0", "bbox": [548, 385, 557, 394]},
	{"text": "1", "bbox": [577, 385, 585, 394]},
	{"text": "2", "bbox": [605, 385, 614, 394]},
	{"text": "3", "bbox": [635, 385, 644, 394]},
	{"text": "4", "bbox": [664, 385, 673, 394]},
	{"text": "5", "bbox": [693, 385, 702, 394]},
	{"text": "6", "bbox": [723, 385, 732, 394]},
	{"text": "7", "bbox": [752, 385, 761, 394]},
	{"text": "8", "bbox": [782, 385, 791, 394]},
	{"text": "9", "bbox": [811, 385, 820, 394]},
	{"text": "10", "bbox": [838, 385, 852, 394]},
	{"text": "11", "bbox": [867, 385, 881, 394]},
	{"text": "12t(s)", "bbox": [897, 385, 931, 396]},
	{"text": "FVC", "bbox": [877, 279, 903, 289]},
	{"text": "PEF", "bbox": [444, 303, 471, 312]},
	{"text": "MEF75%", "bbox": [154, 324, 208, 334]},
	{"text": "MEF50%", "bbox": [210, 370, 263, 380]},
	{"text": "MEF25%", "bbox": [262, 414, 317, 424]},
	{"text": "FVC", "bbox": [319, 448, 346, 458]},
	{"text": "V(l)", "bbox": [465, 458, 494, 468]},
	{"text": "8", "bbox": [465, 458, 474, 467]},
	{"text": "7", "bbox": [420, 458, 428, 467]},
	{"text": "6", "bbox": [375, 458, 383, 467]},
	{"text": "5", "bbox": [330, 458, 338, 467]},
	{"text": "4", "bbox": [285, 458, 293, 467]},
	{"text": "3", "bbox": [238, 458, 246, 467]},
	{"text": "2", "bbox": [192, 458, 200, 467]},
	{"text": "1", "bbox": [146, 458, 154, 467]},
	{"text": "FVC", "bbox": [877, 279, 903, 289]},
	{"text": "PEF", "bbox": [444, 303, 471, 312]},
	{"text": "MEF75%", "bbox": [154, 324, 208, 334]},
	{"text": "MEF50%", "bbox": [210, 370, 263, 380]},
	{"text": "MEF25%", "bbox": [262, 414, 317, 424]},
	{"text": "FVC", "bbox": [319, 448, 346, 458]},
	{"text": "V(l)", "bbox": [465, 458, 494, 468]},
	{"text": "8", "bbox": [465, 458, 474, 467]},
	{"text": "7", "bbox": [420, 458, 428, 467]},
	{"text": "6", "bbox": [375, 458, 383, 467]},
	{"text": "5", "bbox": [330, 458, 338, 467]},
	{"text": "4", "bbox": [285, 458, 293, 467]},
	{"text": "3", "bbox": [238, 458, 246, 467]},
	{"text": "2", "bbox": [192, 458, 200, 467]},
	{"text": "1", "bbox": [146, 458, 154, 467]},
	{"text": "FVC", "bbox": [877, 279, 903, 289]},
	{"text": "PEF", "bbox": [444, 303, 471, 312]},
	{"text": "MEF75%", "bbox": [154, 324, 208, 334]},
	{"text": "MEF50%", "bbox": [210, 370, 263, 380]},
	{"text": "MEF25%", "bbox": [262, 414, 317, 424]},
	{"text": "FVC", "bbox": [319, 448, 346, 458]},
	{"text": "V(l)", "bbox": [465, 458, 494, 468]},
	{"text": "8", "bbox": [465, 458, 474, 467]},
	{"text": "7", "bbox": [420, 458, 428, 467]},
	{"text": "6", "bbox": [375, 458, 383, 467]},
	{"text": "5", "bbox": [330, 458, 338, 467]},
	{"text": "4", "bbox": [285, 458, 293, 467]},
	{"text": "3", "bbox": [238, 458, 246, 467]},
	{"text": "2", "bbox": [192, 458, 200, 467]},
	{"text": "1", "bbox": [146, 458, 154, 467]},
	{"text": "Parameter", "bbox": [76, 680, 146, 690]},
	{"text": "UM", "bbox": [169, 680, 191, 690]},
	{"text": "Pred.", "bbox": [237, 680, 271, 690]},
	{"text": "BEST#1", "bbox": [286, 680, 338, 690]},
	{"text": "%Pred.", "bbox": [353, 680, 401, 690]},
	{"text": "POST#3", "bbox": [413, 680, 466, 690]},
	{"text": "%Pred.", "bbox": [480, 680, 526, 690]},
	{"text": "%Test#1", "bbox": [539, 680, 593, 690]},
	{"text": "Best FVC", "bbox": [76, 697, 137, 707]},
	{"text": "l(btps)", "bbox": [169, 697, 208, 707]},
	{"text": "4.72", "bbox": [246, 697, 278, 707]},
	{"text": "2.74", "bbox": [295, 697, 327, 707]},
	{"text": "58", "bbox": [370, 697, 387, 707]},
	{"text": "3.22", "bbox": [420, 697, 454, 707]},
	{"text": "68", "bbox": [497, 697, 514, 707]},
	{"text": "+17.4", "bbox": [538, 697, 580, 707]},
	{"text": "FVC", "bbox": [76, 710, 106, 720]},
	{"text": "l(btps)", "bbox": [169, 710, 208, 720]},
	{"text": "4.72", "bbox": [246, 710, 278, 720]},
	{"text": "2.74", "bbox": [295, 710, 327, 720]},
	{"text": "58", "bbox": [370, 710, 387, 720]},
	{"text": "3.22", "bbox": [420, 710, 454, 720]},
	{"text": "68", "bbox": [497, 710, 514, 720]},
	{"text": "+17.4", "bbox": [538, 710, 580, 720]},
	{"text": "FEV1", "bbox": [76, 722, 112, 732]},
	{"text": "l(btps)", "bbox": [169, 722, 208, 732]},
	{"text": "3.83", "bbox": [246, 722, 278, 732]},
	{"text": "1.35", "bbox": [295, 722, 327, 732]},
	{"text": "35", "bbox": [370, 722, 387, 732]},
	{"text": "1.72", "bbox": [420, 722, 454, 732]},
	{"text": "45", "bbox": [497, 722, 514, 732]},
	{"text": "+27.5", "bbox": [538, 722, 580, 732]},
	{"text": "PEF", "bbox": [76, 734, 105, 744]},
	{"text": "l/sec", "bbox": [169, 734, 200, 744]},
	{"text": "9.10", "bbox": [246, 734, 278, 744]},
	{"text": "2.96", "bbox": [295, 734, 327, 744]},
	{"text": "32", "bbox": [370, 734, 387, 744]},
	{"text": "3.30", "bbox": [420, 734, 454, 744]},
	{"text": "36", "bbox": [497, 734, 514, 744]},
	{"text": "+11.4", "bbox": [538, 734, 580, 744]},
	{"text": "FEV6", "bbox": [76, 746, 113, 756]},
	{"text": "l(btps)", "bbox": [169, 746, 208, 756]},
	{"text": "5.01", "bbox": [246, 746, 278, 756]},
	{"text": "2.71", "bbox": [295, 746, 327, 756]},
	{"text": "54", "bbox": [370, 746, 387, 756]},
	{"text": "3.20", "bbox": [420, 746, 454, 756]},
	{"text": "64", "bbox": [497, 746, 514, 756]},
	{"text": "+18.2", "bbox": [538, 746, 580, 756]},
	{"text": "PIF", "bbox": [76, 758, 101, 768]},
	{"text": "l/sec", "bbox": [169, 758, 200, 768]},
	{"text": "4.61", "bbox": [295, 758, 327, 768]},
	{"text": "5.52", "bbox": [420, 758, 454, 768]},
	{"text": "+19.9", "bbox": [538, 758, 580, 768]},
	{"text": "FEV1/FVC%", "bbox": [76, 769, 157, 779]},
	{"text": "%", "bbox": [169, 769, 182, 779]},
	{"text": "78.9", "bbox": [246, 769, 278, 779]},
	{"text": "49.1", "bbox": [295, 769, 327, 779]},
	{"text": "62", "bbox": [370, 769, 387, 779]},
	{"text": "53.4", "bbox": [420, 769, 454, 779]},
	{"text": "68", "bbox": [497, 769, 514, 779]},
	{"text": "+8.7", "bbox": [538, 769, 580, 779]},
	{"text": "FEV6/FVC%", "bbox": [76, 781, 157, 791]},
	{"text": "%", "bbox": [169, 781, 182, 791]},
	{"text": "98.8", "bbox": [295, 781, 327, 791]},
	{"text": "99.5", "bbox": [420, 781, 454, 791]},
	{"text": "+0.7", "bbox": [538, 781, 580, 791]},
	{"text": "FEV1/FEV6%", "bbox": [76, 793, 164, 803]},
	{"text": "%", "bbox": [169, 793, 182, 803]},
	{"text": "49.7", "bbox": [295, 793, 327, 803]},
	{"text": "53.6", "bbox": [420, 793, 454, 803]},
	{"text": "+7.9", "bbox": [538, 793, 580, 803]},
	{"text": "FEF25-75%", "bbox": [76, 805, 153, 815]},
	{"text": "l/sec", "bbox": [169, 805, 200, 815]},
	{"text": "4.18", "bbox": [246, 805, 278, 815]},
	{"text": "0.64", "bbox": [295, 805, 327, 815]},
	{"text": "15", "bbox": [370, 805, 387, 815]},
	{"text": "0.86", "bbox": [420, 805, 454, 815]},
	{"text": "21", "bbox": [497, 805, 514, 815]},
	{"text": "+34.7", "bbox": [538, 805, 580, 815]},
	{"text": "MEF75%", "bbox": [76, 817, 135, 827]},
	{"text": "l/sec", "bbox": [169, 817, 200, 827]},
	{"text": "7.91", "bbox": [246, 817, 278, 827]},
	{"text": "1.42", "bbox": [295, 817, 327, 827]},
	{"text": "18", "bbox": [370, 817, 387, 827]},
	{"text": "1.98", "bbox": [420, 817, 454, 827]},
	{"text": "25", "bbox": [497, 817, 514, 827]},
	{"text": "+39.2", "bbox": [538, 817, 580, 827]},
	{"text": "MEF50%", "bbox": [76, 829, 135, 839]},
	{"text": "l/sec", "bbox": [169, 829, 200, 839]},
	{"text": "4.97", "bbox": [246, 829, 278, 839]},
	{"text": "0.75", "bbox": [295, 829, 327, 839]},
	{"text": "15", "bbox": [370, 829, 387, 839]},
	{"text": "1.02", "bbox": [420, 829, 454, 839]},
	{"text": "20", "bbox": [497, 829, 514, 839]},
	{"text": "+36.2", "bbox": [538, 829, 580, 839]},
	{"text": "MEF25%", "bbox": [76, 841, 135, 851]},
	{"text": "l/sec", "bbox": [169, 841, 200, 851]},
	{"text": "2.11", "bbox": [246, 841, 278, 851]},
	{"text": "0.31", "bbox": [295, 841, 327, 851]},
	{"text": "15", "bbox": [370, 841, 387, 851]},
	{"text": "0.41", "bbox": [420, 841, 454, 851]},
	{"text": "19", "bbox": [497, 841, 514, 851]},
	{"text": "+32.4", "bbox": [538, 841, 580, 851]},
	{"text": "FET100%", "bbox": [76, 853, 140, 863]},
	{"text": "sec", "bbox": [169, 853, 193, 863]},
	{"text": "6.2", "bbox": [295, 853, 320, 863]},
	{"text": "6.1", "bbox": [420, 853, 446, 863]},
	{"text": "-1.9", "bbox": [538, 853, 572, 863]},
	{"text": "VEXT", "bbox": [76, 865, 114, 875]},
	{"text": "ml", "bbox": [169, 865, 185, 875]},
	{"text": "60", "bbox": [312, 865, 328, 875]},
	{"text": "73", "bbox": [438, 865, 455, 875]},
	{"text": "+21.7", "bbox": [538, 865, 580, 875]},
	{"text": "IC", "bbox": [76, 877, 92, 887]},
	{"text": "l(btps)", "bbox": [169, 877, 208, 887]},
	{"text": "2.47", "bbox": [295, 877, 327, 887]},
	{"text": "2.27", "bbox": [420, 877, 454, 887]},
	{"text": "-8.1", "bbox": [538, 877, 572, 887]},
	{"text": "诊断:", "bbox": [76, 891, 115, 902]},
	{"text": "支气管舒张试验阳性。", "bbox": [76, 903, 226, 915]},
	{"text": "签名:", "bbox": [718, 921, 750, 932]}
]
2026-08-05 12:03:47,883 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8923813, prompt_len=401
2026-08-05 12:03:47,883 INFO     29 [qwen-vl-text] coord API: raw_items=233, valid_items=233, elapsed=65.4s
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[0]: text=临海市第一人民医院医共体, bbox=[386, 71, 610, 85]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[1]: text=肺功能报告, bbox=[451, 85, 544, 99]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[2]: text=COSMED, bbox=[87, 119, 150, 130]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[3]: text=姓名:, bbox=[73, 139, 111, 150]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[4]: text=科室/床号:, bbox=[73, 150, 146, 161]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[5]: text=ID:, bbox=[73, 163, 94, 174]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[6]: text=日期:, bbox=[73, 174, 111, 185]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[7]: text=预计值:, bbox=[73, 185, 126, 197]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[8]: text=出生日期: 1978/12/13, bbox=[428, 137, 587, 147]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[9]: text=性别: Male, bbox=[428, 148, 544, 159]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[10]: text=地区修正.: Chinese, bbox=[428, 160, 567, 170]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[11]: text=详细描述:, bbox=[428, 171, 498, 182]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[12]: text=Company:, bbox=[428, 183, 507, 194]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[13]: text=年龄: 46, bbox=[784, 137, 892, 147]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[14]: text=体重 (Kg): 84.0, bbox=[784, 148, 909, 159]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[15]: text=身高 (cm): 178.0, bbox=[784, 159, 917, 170]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[16]: text=BMI (Kg/m²): 26.5, bbox=[784, 170, 909, 181]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[17]: text=吸烟: 否, bbox=[784, 182, 895, 193]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[18]: text=用力肺活量 Forced Vital Capacity, bbox=[165, 203, 407, 214]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[19]: text=F(l/s), bbox=[88, 216, 119, 226]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[20]: text=14, bbox=[76, 224, 90, 233]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[21]: text=13, bbox=[76, 240, 90, 249]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[22]: text=12, bbox=[76, 256, 90, 265]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[23]: text=11, bbox=[76, 271, 90, 280]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[24]: text=10, bbox=[76, 287, 90, 296]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[25]: text=9, bbox=[81, 303, 90, 312]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[26]: text=8, bbox=[81, 319, 90, 328]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[27]: text=7, bbox=[81, 335, 90, 344]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[28]: text=6, bbox=[81, 351, 90, 360]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[29]: text=5, bbox=[81, 367, 90, 376]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[30]: text=4, bbox=[81, 383, 90, 392]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[31]: text=3, bbox=[81, 399, 90, 408]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[32]: text=2, bbox=[81, 415, 90, 424]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[33]: text=1, bbox=[81, 431, 90, 440]
2026-08-05 12:03:47,912 INFO     29 [qwen-vl-text] coord item[34]: text=0, bbox=[81, 447, 90, 456]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[35]: text=-1, bbox=[79, 463, 90, 472]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[36]: text=-2, bbox=[81, 479, 90, 488]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[37]: text=-3, bbox=[81, 495, 90, 504]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[38]: text=-4, bbox=[81, 511, 90, 520]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[39]: text=-5, bbox=[81, 527, 90, 536]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[40]: text=-6, bbox=[81, 543, 90, 552]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[41]: text=-7, bbox=[81, 559, 90, 568]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[42]: text=-8, bbox=[81, 575, 90, 584]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[43]: text=V(l), bbox=[509, 202, 528, 211]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[44]: text=8, bbox=[502, 211, 511, 220]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[45]: text=7, bbox=[502, 230, 511, 239]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[46]: text=6, bbox=[502, 250, 511, 259]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[47]: text=5, bbox=[502, 270, 511, 279]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[48]: text=4, bbox=[502, 290, 511, 299]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[49]: text=3, bbox=[502, 310, 511, 319]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[50]: text=2, bbox=[502, 330, 511, 339]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[51]: text=1, bbox=[502, 350, 511, 359]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[52]: text=0, bbox=[502, 370, 511, 379]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[53]: text=-1, bbox=[515, 385, 526, 394]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[54]: text=0, bbox=[548, 385, 557, 394]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[55]: text=1, bbox=[577, 385, 585, 394]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[56]: text=2, bbox=[605, 385, 614, 394]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[57]: text=3, bbox=[635, 385, 644, 394]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[58]: text=4, bbox=[664, 385, 673, 394]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[59]: text=5, bbox=[693, 385, 702, 394]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[60]: text=6, bbox=[723, 385, 732, 394]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[61]: text=7, bbox=[752, 385, 761, 394]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[62]: text=8, bbox=[782, 385, 791, 394]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[63]: text=9, bbox=[811, 385, 820, 394]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[64]: text=10, bbox=[838, 385, 852, 394]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[65]: text=11, bbox=[867, 385, 881, 394]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[66]: text=12t(s), bbox=[897, 385, 931, 396]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[67]: text=FVC, bbox=[877, 279, 903, 289]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[68]: text=PEF, bbox=[444, 303, 471, 312]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[69]: text=MEF75%, bbox=[154, 324, 208, 334]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[70]: text=MEF50%, bbox=[210, 370, 263, 380]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[71]: text=MEF25%, bbox=[262, 414, 317, 424]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[72]: text=FVC, bbox=[319, 448, 346, 458]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[73]: text=V(l), bbox=[465, 458, 494, 468]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[74]: text=8, bbox=[465, 458, 474, 467]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[75]: text=7, bbox=[420, 458, 428, 467]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[76]: text=6, bbox=[375, 458, 383, 467]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[77]: text=5, bbox=[330, 458, 338, 467]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[78]: text=4, bbox=[285, 458, 293, 467]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[79]: text=3, bbox=[238, 458, 246, 467]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[80]: text=2, bbox=[192, 458, 200, 467]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[81]: text=1, bbox=[146, 458, 154, 467]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[82]: text=FVC, bbox=[877, 279, 903, 289]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[83]: text=PEF, bbox=[444, 303, 471, 312]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[84]: text=MEF75%, bbox=[154, 324, 208, 334]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[85]: text=MEF50%, bbox=[210, 370, 263, 380]
2026-08-05 12:03:47,913 INFO     29 [qwen-vl-text] coord item[86]: text=MEF25%, bbox=[262, 414, 317, 424]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[87]: text=FVC, bbox=[319, 448, 346, 458]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[88]: text=V(l), bbox=[465, 458, 494, 468]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[89]: text=8, bbox=[465, 458, 474, 467]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[90]: text=7, bbox=[420, 458, 428, 467]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[91]: text=6, bbox=[375, 458, 383, 467]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[92]: text=5, bbox=[330, 458, 338, 467]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[93]: text=4, bbox=[285, 458, 293, 467]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[94]: text=3, bbox=[238, 458, 246, 467]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[95]: text=2, bbox=[192, 458, 200, 467]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[96]: text=1, bbox=[146, 458, 154, 467]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[97]: text=FVC, bbox=[877, 279, 903, 289]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[98]: text=PEF, bbox=[444, 303, 471, 312]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[99]: text=MEF75%, bbox=[154, 324, 208, 334]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[100]: text=MEF50%, bbox=[210, 370, 263, 380]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[101]: text=MEF25%, bbox=[262, 414, 317, 424]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[102]: text=FVC, bbox=[319, 448, 346, 458]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[103]: text=V(l), bbox=[465, 458, 494, 468]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[104]: text=8, bbox=[465, 458, 474, 467]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[105]: text=7, bbox=[420, 458, 428, 467]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[106]: text=6, bbox=[375, 458, 383, 467]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[107]: text=5, bbox=[330, 458, 338, 467]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[108]: text=4, bbox=[285, 458, 293, 467]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[109]: text=3, bbox=[238, 458, 246, 467]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[110]: text=2, bbox=[192, 458, 200, 467]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[111]: text=1, bbox=[146, 458, 154, 467]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[112]: text=Parameter, bbox=[76, 680, 146, 690]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[113]: text=UM, bbox=[169, 680, 191, 690]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[114]: text=Pred., bbox=[237, 680, 271, 690]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[115]: text=BEST#1, bbox=[286, 680, 338, 690]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[116]: text=%Pred., bbox=[353, 680, 401, 690]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[117]: text=POST#3, bbox=[413, 680, 466, 690]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[118]: text=%Pred., bbox=[480, 680, 526, 690]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[119]: text=%Test#1, bbox=[539, 680, 593, 690]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[120]: text=Best FVC, bbox=[76, 697, 137, 707]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[121]: text=l(btps), bbox=[169, 697, 208, 707]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[122]: text=4.72, bbox=[246, 697, 278, 707]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[123]: text=2.74, bbox=[295, 697, 327, 707]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[124]: text=58, bbox=[370, 697, 387, 707]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[125]: text=3.22, bbox=[420, 697, 454, 707]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[126]: text=68, bbox=[497, 697, 514, 707]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[127]: text=+17.4, bbox=[538, 697, 580, 707]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[128]: text=FVC, bbox=[76, 710, 106, 720]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[129]: text=l(btps), bbox=[169, 710, 208, 720]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[130]: text=4.72, bbox=[246, 710, 278, 720]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[131]: text=2.74, bbox=[295, 710, 327, 720]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[132]: text=58, bbox=[370, 710, 387, 720]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[133]: text=3.22, bbox=[420, 710, 454, 720]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[134]: text=68, bbox=[497, 710, 514, 720]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[135]: text=+17.4, bbox=[538, 710, 580, 720]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[136]: text=FEV1, bbox=[76, 722, 112, 732]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[137]: text=l(btps), bbox=[169, 722, 208, 732]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[138]: text=3.83, bbox=[246, 722, 278, 732]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[139]: text=1.35, bbox=[295, 722, 327, 732]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[140]: text=35, bbox=[370, 722, 387, 732]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[141]: text=1.72, bbox=[420, 722, 454, 732]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[142]: text=45, bbox=[497, 722, 514, 732]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[143]: text=+27.5, bbox=[538, 722, 580, 732]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[144]: text=PEF, bbox=[76, 734, 105, 744]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[145]: text=l/sec, bbox=[169, 734, 200, 744]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[146]: text=9.10, bbox=[246, 734, 278, 744]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[147]: text=2.96, bbox=[295, 734, 327, 744]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[148]: text=32, bbox=[370, 734, 387, 744]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[149]: text=3.30, bbox=[420, 734, 454, 744]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[150]: text=36, bbox=[497, 734, 514, 744]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[151]: text=+11.4, bbox=[538, 734, 580, 744]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[152]: text=FEV6, bbox=[76, 746, 113, 756]
2026-08-05 12:03:47,914 INFO     29 [qwen-vl-text] coord item[153]: text=l(btps), bbox=[169, 746, 208, 756]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[154]: text=5.01, bbox=[246, 746, 278, 756]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[155]: text=2.71, bbox=[295, 746, 327, 756]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[156]: text=54, bbox=[370, 746, 387, 756]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[157]: text=3.20, bbox=[420, 746, 454, 756]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[158]: text=64, bbox=[497, 746, 514, 756]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[159]: text=+18.2, bbox=[538, 746, 580, 756]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[160]: text=PIF, bbox=[76, 758, 101, 768]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[161]: text=l/sec, bbox=[169, 758, 200, 768]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[162]: text=4.61, bbox=[295, 758, 327, 768]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[163]: text=5.52, bbox=[420, 758, 454, 768]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[164]: text=+19.9, bbox=[538, 758, 580, 768]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[165]: text=FEV1/FVC%, bbox=[76, 769, 157, 779]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[166]: text=%, bbox=[169, 769, 182, 779]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[167]: text=78.9, bbox=[246, 769, 278, 779]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[168]: text=49.1, bbox=[295, 769, 327, 779]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[169]: text=62, bbox=[370, 769, 387, 779]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[170]: text=53.4, bbox=[420, 769, 454, 779]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[171]: text=68, bbox=[497, 769, 514, 779]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[172]: text=+8.7, bbox=[538, 769, 580, 779]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[173]: text=FEV6/FVC%, bbox=[76, 781, 157, 791]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[174]: text=%, bbox=[169, 781, 182, 791]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[175]: text=98.8, bbox=[295, 781, 327, 791]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[176]: text=99.5, bbox=[420, 781, 454, 791]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[177]: text=+0.7, bbox=[538, 781, 580, 791]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[178]: text=FEV1/FEV6%, bbox=[76, 793, 164, 803]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[179]: text=%, bbox=[169, 793, 182, 803]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[180]: text=49.7, bbox=[295, 793, 327, 803]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[181]: text=53.6, bbox=[420, 793, 454, 803]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[182]: text=+7.9, bbox=[538, 793, 580, 803]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[183]: text=FEF25-75%, bbox=[76, 805, 153, 815]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[184]: text=l/sec, bbox=[169, 805, 200, 815]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[185]: text=4.18, bbox=[246, 805, 278, 815]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[186]: text=0.64, bbox=[295, 805, 327, 815]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[187]: text=15, bbox=[370, 805, 387, 815]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[188]: text=0.86, bbox=[420, 805, 454, 815]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[189]: text=21, bbox=[497, 805, 514, 815]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[190]: text=+34.7, bbox=[538, 805, 580, 815]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[191]: text=MEF75%, bbox=[76, 817, 135, 827]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[192]: text=l/sec, bbox=[169, 817, 200, 827]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[193]: text=7.91, bbox=[246, 817, 278, 827]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[194]: text=1.42, bbox=[295, 817, 327, 827]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[195]: text=18, bbox=[370, 817, 387, 827]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[196]: text=1.98, bbox=[420, 817, 454, 827]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[197]: text=25, bbox=[497, 817, 514, 827]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[198]: text=+39.2, bbox=[538, 817, 580, 827]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[199]: text=MEF50%, bbox=[76, 829, 135, 839]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[200]: text=l/sec, bbox=[169, 829, 200, 839]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[201]: text=4.97, bbox=[246, 829, 278, 839]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[202]: text=0.75, bbox=[295, 829, 327, 839]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[203]: text=15, bbox=[370, 829, 387, 839]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[204]: text=1.02, bbox=[420, 829, 454, 839]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[205]: text=20, bbox=[497, 829, 514, 839]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[206]: text=+36.2, bbox=[538, 829, 580, 839]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[207]: text=MEF25%, bbox=[76, 841, 135, 851]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[208]: text=l/sec, bbox=[169, 841, 200, 851]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[209]: text=2.11, bbox=[246, 841, 278, 851]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[210]: text=0.31, bbox=[295, 841, 327, 851]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[211]: text=15, bbox=[370, 841, 387, 851]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[212]: text=0.41, bbox=[420, 841, 454, 851]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[213]: text=19, bbox=[497, 841, 514, 851]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[214]: text=+32.4, bbox=[538, 841, 580, 851]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[215]: text=FET100%, bbox=[76, 853, 140, 863]
2026-08-05 12:03:47,915 INFO     29 [qwen-vl-text] coord item[216]: text=sec, bbox=[169, 853, 193, 863]
2026-08-05 12:03:47,916 INFO     29 [qwen-vl-text] coord item[217]: text=6.2, bbox=[295, 853, 320, 863]
2026-08-05 12:03:47,916 INFO     29 [qwen-vl-text] coord item[218]: text=6.1, bbox=[420, 853, 446, 863]
2026-08-05 12:03:47,916 INFO     29 [qwen-vl-text] coord item[219]: text=-1.9, bbox=[538, 853, 572, 863]
2026-08-05 12:03:47,916 INFO     29 [qwen-vl-text] coord item[220]: text=VEXT, bbox=[76, 865, 114, 875]
2026-08-05 12:03:47,916 INFO     29 [qwen-vl-text] coord item[221]: text=ml, bbox=[169, 865, 185, 875]
2026-08-05 12:03:47,916 INFO     29 [qwen-vl-text] coord item[222]: text=60, bbox=[312, 865, 328, 875]
2026-08-05 12:03:47,916 INFO     29 [qwen-vl-text] coord item[223]: text=73, bbox=[438, 865, 455, 875]
2026-08-05 12:03:47,916 INFO     29 [qwen-vl-text] coord item[224]: text=+21.7, bbox=[538, 865, 580, 875]
2026-08-05 12:03:47,916 INFO     29 [qwen-vl-text] coord item[225]: text=IC, bbox=[76, 877, 92, 887]
2026-08-05 12:03:47,916 INFO     29 [qwen-vl-text] coord item[226]: text=l(btps), bbox=[169, 877, 208, 887]
2026-08-05 12:03:47,916 INFO     29 [qwen-vl-text] coord item[227]: text=2.47, bbox=[295, 877, 327, 887]
2026-08-05 12:03:47,916 INFO     29 [qwen-vl-text] coord item[228]: text=2.27, bbox=[420, 877, 454, 887]
2026-08-05 12:03:47,916 INFO     29 [qwen-vl-text] coord item[229]: text=-8.1, bbox=[538, 877, 572, 887]
2026-08-05 12:03:47,916 INFO     29 [qwen-vl-text] coord item[230]: text=诊断:, bbox=[76, 891, 115, 902]
2026-08-05 12:03:47,916 INFO     29 [qwen-vl-text] coord item[231]: text=支气管舒张试验阳性。, bbox=[76, 903, 226, 915]
2026-08-05 12:03:47,916 INFO     29 [qwen-vl-text] coord item[232]: text=签名:, bbox=[718, 921, 750, 932]
2026-08-05 12:03:47,916 INFO     29 [qwen-vl-text] page=0 — 253/253 coords, api_time=65.4s
2026-08-05 12:03:47,917 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=335094, prompt_len=625
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["2025-03-16"]

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
2026-08-05 12:03:48,529 INFO     29 [qwen-vl-text] coord API raw response (len=55):
[
	{"text": "2025-03-16", "bbox": [38, 322, 87, 330]}
]
2026-08-05 12:03:48,530 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=0.6s
2026-08-05 12:03:48,530 INFO     29 [qwen-vl-text] coord item[0]: text=2025-03-16, bbox=[38, 322, 87, 330]
2026-08-05 12:03:48,530 INFO     29 [qwen-vl-text] page=1 — 1/1 coords, api_time=0.6s
2026-08-05 12:03:48,530 INFO     29 [qwen-vl-text] new_positions (254):
[[0, 229.77653637695315, 363.11836059570317, 59.774191040039064, 71.56065124511719], [0, 268.4694764404297, 323.83014453125, 71.56065124511719, 83.34711145019531], [0, 51.78901208496094, 89.29140014648438, 100.18491174316407, 109.44570190429687], [0, 43.45514807128907, 66.07563610839844, 117.02271203613282, 126.28350219726562], [0, 43.45514807128907, 86.91029614257813, 126.28350219726562, 135.54429235839842], [0, 43.45514807128907, 55.95594409179688, 137.2280723876953, 146.4888625488281], [0, 43.45514807128907, 66.07563610839844, 146.4888625488281, 155.74965270996094], [0, 43.45514807128907, 75.00477612304688, 155.74965270996094, 165.8523328857422], [0, 254.77812841796876, 349.4270125732422, 115.33893200683593, 123.75783215332031], [0, 254.77812841796876, 323.83014453125, 124.59972216796875, 133.86051232910157], [0, 254.77812841796876, 337.52149255371097, 134.70240234375, 143.12130249023437], [0, 254.77812841796876, 296.44744848632814, 143.9631925048828, 153.22398266601562], [0, 254.77812841796876, 301.8049324951172, 154.06587268066406, 163.32666284179686], [0, 466.696384765625, 530.9861928710937, 115.33893200683593, 123.75783215332031], [0, 466.696384765625, 541.1058848876953, 124.59972216796875, 133.86051232910157], [0, 466.696384765625, 545.8680928955079, 133.86051232910157, 143.12130249023437], [0, 466.696384765625, 541.1058848876953, 143.12130249023437, 152.38209265136717], [0, 466.696384765625, 532.7720208740235, 153.22398266601562, 162.48477282714845], [0, 98.22054016113282, 242.27733239746095, 170.9036729736328, 180.1644631347656], [0, 52.3842880859375, 70.83784411621095, 181.8482431640625, 190.26714331054689], [0, 45.24097607421875, 53.57484008789063, 188.58336328125, 196.16037341308595], [0, 45.24097607421875, 53.57484008789063, 202.05360351562499, 209.63061364746093], [0, 45.24097607421875, 53.57484008789063, 215.52384375, 223.10085388183595], [0, 45.24097607421875, 53.57484008789063, 228.15219396972657, 235.7292041015625], [0, 45.24097607421875, 53.57484008789063, 241.62243420410155, 249.1994443359375], [0, 48.21735607910156, 53.57484008789063, 255.09267443847656, 262.6696845703125], [0, 48.21735607910156, 53.57484008789063, 268.56291467285155, 276.1399248046875], [0, 48.21735607910156, 53.57484008789063, 282.03315490722656, 289.6101650390625], [0, 48.21735607910156, 53.57484008789063, 295.5033951416016, 303.0804052734375], [0, 48.21735607910156, 53.57484008789063, 308.9736353759766, 316.5506455078125], [0, 48.21735607910156, 53.57484008789063, 322.44387561035154, 330.0208857421875], [0, 48.21735607910156, 53.57484008789063, 335.91411584472655, 343.4911259765625], [0, 48.21735607910156, 53.57484008789063, 349.38435607910156, 356.9613662109375], [0, 48.21735607910156, 53.57484008789063, 362.8545963134766, 370.43160644531247], [0, 48.21735607910156, 53.57484008789063, 376.32483654785153, 383.9018466796875], [0, 47.02680407714844, 53.57484008789063, 389.79507678222654, 397.3720869140625], [0, 48.21735607910156, 53.57484008789063, 403.26531701660156, 410.8423271484375], [0, 48.21735607910156, 53.57484008789063, 416.73555725097657, 424.3125673828125], [0, 48.21735607910156, 53.57484008789063, 430.2057974853516, 437.7828076171875], [0, 48.21735607910156, 53.57484008789063, 443.67603771972654, 451.2530478515625], [0, 48.21735607910156, 53.57484008789063, 457.14627795410155, 464.7232880859375], [0, 48.21735607910156, 53.57484008789063, 470.61651818847656, 478.1935283203125], [0, 48.21735607910156, 53.57484008789063, 484.0867584228516, 491.6637685546875], [0, 302.9954844970703, 314.305728515625, 170.06178295898437, 177.63879309082031], [0, 298.8285524902344, 304.18603649902343, 177.63879309082031, 185.21580322265623], [0, 298.8285524902344, 304.18603649902343, 193.63470336914062, 201.21171350097657], [0, 298.8285524902344, 304.18603649902343, 210.47250366210938, 218.04951379394532], [0, 298.8285524902344, 304.18603649902343, 227.31030395507813, 234.88731408691405], [0, 298.8285524902344, 304.18603649902343, 244.14810424804688, 251.7251143798828], [0, 298.8285524902344, 304.18603649902343, 260.9859045410156, 268.56291467285155], [0, 298.8285524902344, 304.18603649902343, 277.8237048339844, 285.4007149658203], [0, 298.8285524902344, 304.18603649902343, 294.6615051269531, 302.23851525878905], [0, 298.8285524902344, 304.18603649902343, 311.4993054199219, 319.07631555175783], [0, 306.5671405029297, 313.1151765136719, 324.1276556396484, 331.7046657714844], [0, 326.21124853515624, 331.5687325439453, 324.1276556396484, 331.7046657714844], [0, 343.47425256347657, 348.23646057128906, 324.1276556396484, 331.7046657714844], [0, 360.1419805908203, 365.4994645996094, 324.1276556396484, 331.7046657714844], [0, 378.0002606201172, 383.3577446289063, 324.1276556396484, 331.7046657714844], [0, 395.26326464843754, 400.62074865722656, 324.1276556396484, 331.7046657714844], [0, 412.5262686767578, 417.8837526855469, 324.1276556396484, 331.7046657714844], [0, 430.3845487060547, 435.7420327148438, 324.1276556396484, 331.7046657714844], [0, 447.64755273437504, 453.00503674316406, 324.1276556396484, 331.7046657714844], [0, 465.5058327636719, 470.86331677246096, 324.1276556396484, 331.7046657714844], [0, 482.7688367919922, 488.1263208007813, 324.1276556396484, 331.7046657714844], [0, 498.8412888183594, 507.17515283203124, 324.1276556396484, 331.7046657714844], [0, 516.1042928466798, 524.4381568603516, 324.1276556396484, 331.7046657714844], [0, 533.9625728759765, 554.2019569091797, 324.1276556396484, 333.38844580078126], [0, 522.0570528564454, 537.5342288818359, 234.88731408691405, 243.30621423339844], [0, 264.30254443359377, 280.3749964599609, 255.09267443847656, 262.6696845703125], [0, 91.67250415039062, 123.81740820312501, 272.77236474609373, 281.19126489257815], [0, 125.00796020507813, 156.55758825683594, 311.4993054199219, 319.91820556640624], [0, 155.9623122558594, 188.70249230957032, 348.5424660644531, 356.9613662109375], [0, 189.89304431152345, 205.96549633789064, 377.1667265625, 385.58562670898436], [0, 276.8033404541016, 294.06634448242187, 385.58562670898436, 394.0045268554687], [0, 276.8033404541016, 282.1608244628906, 385.58562670898436, 393.1626368408203], [0, 250.01592041015627, 254.77812841796876, 385.58562670898436, 393.1626368408203], [0, 223.22850036621094, 227.99070837402346, 385.58562670898436, 393.1626368408203], [0, 196.44108032226563, 201.20328833007812, 385.58562670898436, 393.1626368408203], [0, 169.65366027832033, 174.41586828613282, 385.58562670898436, 393.1626368408203], [0, 141.6756882324219, 146.43789624023438, 385.58562670898436, 393.1626368408203], [0, 114.2929921875, 119.05520019531251, 385.58562670898436, 393.1626368408203], [0, 86.91029614257813, 91.67250415039062, 385.58562670898436, 393.1626368408203], [0, 522.0570528564454, 537.5342288818359, 234.88731408691405, 243.30621423339844], [0, 264.30254443359377, 280.3749964599609, 255.09267443847656, 262.6696845703125], [0, 91.67250415039062, 123.81740820312501, 272.77236474609373, 281.19126489257815], [0, 125.00796020507813, 156.55758825683594, 311.4993054199219, 319.91820556640624], [0, 155.9623122558594, 188.70249230957032, 348.5424660644531, 356.9613662109375], [0, 189.89304431152345, 205.96549633789064, 377.1667265625, 385.58562670898436], [0, 276.8033404541016, 294.06634448242187, 385.58562670898436, 394.0045268554687], [0, 276.8033404541016, 282.1608244628906, 385.58562670898436, 393.1626368408203], [0, 250.01592041015627, 254.77812841796876, 385.58562670898436, 393.1626368408203], [0, 223.22850036621094, 227.99070837402346, 385.58562670898436, 393.1626368408203], [0, 196.44108032226563, 201.20328833007812, 385.58562670898436, 393.1626368408203], [0, 169.65366027832033, 174.41586828613282, 385.58562670898436, 393.1626368408203], [0, 141.6756882324219, 146.43789624023438, 385.58562670898436, 393.1626368408203], [0, 114.2929921875, 119.05520019531251, 385.58562670898436, 393.1626368408203], [0, 86.91029614257813, 91.67250415039062, 385.58562670898436, 393.1626368408203], [0, 522.0570528564454, 537.5342288818359, 234.88731408691405, 243.30621423339844], [0, 264.30254443359377, 280.3749964599609, 255.09267443847656, 262.6696845703125], [0, 91.67250415039062, 123.81740820312501, 272.77236474609373, 281.19126489257815], [0, 125.00796020507813, 156.55758825683594, 311.4993054199219, 319.91820556640624], [0, 155.9623122558594, 188.70249230957032, 348.5424660644531, 356.9613662109375], [0, 189.89304431152345, 205.96549633789064, 377.1667265625, 385.58562670898436], [0, 276.8033404541016, 294.06634448242187, 385.58562670898436, 394.0045268554687], [0, 276.8033404541016, 282.1608244628906, 385.58562670898436, 393.1626368408203], [0, 250.01592041015627, 254.77812841796876, 385.58562670898436, 393.1626368408203], [0, 223.22850036621094, 227.99070837402346, 385.58562670898436, 393.1626368408203], [0, 196.44108032226563, 201.20328833007812, 385.58562670898436, 393.1626368408203], [0, 169.65366027832033, 174.41586828613282, 385.58562670898436, 393.1626368408203], [0, 141.6756882324219, 146.43789624023438, 385.58562670898436, 393.1626368408203], [0, 114.2929921875, 119.05520019531251, 385.58562670898436, 393.1626368408203], [0, 86.91029614257813, 91.67250415039062, 385.58562670898436, 393.1626368408203], [0, 45.24097607421875, 86.91029614257813, 572.4852099609375, 580.9041101074218], [0, 100.60164416503906, 113.69771618652344, 572.4852099609375, 580.9041101074218], [0, 141.0804122314453, 161.31979626464843, 572.4852099609375, 580.9041101074218], [0, 170.24893627929688, 201.20328833007812, 572.4852099609375, 580.9041101074218], [0, 210.13242834472658, 238.70567639160157, 572.4852099609375, 580.9041101074218], [0, 245.84898840332033, 277.3986164550781, 572.4852099609375, 580.9041101074218], [0, 285.73248046875, 313.1151765136719, 572.4852099609375, 580.9041101074218], [0, 320.85376452636723, 352.9986685791016, 572.4852099609375, 580.9041101074218], [0, 45.24097607421875, 81.55281213378906, 586.7973402099609, 595.2162403564453], [0, 100.60164416503906, 123.81740820312501, 586.7973402099609, 595.2162403564453], [0, 146.43789624023438, 165.4867282714844, 586.7973402099609, 595.2162403564453], [0, 175.60642028808596, 194.65525231933594, 586.7973402099609, 595.2162403564453], [0, 220.25212036132814, 230.3718123779297, 586.7973402099609, 595.2162403564453], [0, 250.01592041015627, 270.25530444335936, 586.7973402099609, 595.2162403564453], [0, 295.85217248535156, 305.9718645019531, 586.7973402099609, 595.2162403564453], [0, 320.25848852539065, 345.26008056640626, 586.7973402099609, 595.2162403564453], [0, 45.24097607421875, 63.09925610351563, 597.7419104003906, 606.160810546875], [0, 100.60164416503906, 123.81740820312501, 597.7419104003906, 606.160810546875], [0, 146.43789624023438, 165.4867282714844, 597.7419104003906, 606.160810546875], [0, 175.60642028808596, 194.65525231933594, 597.7419104003906, 606.160810546875], [0, 220.25212036132814, 230.3718123779297, 597.7419104003906, 606.160810546875], [0, 250.01592041015627, 270.25530444335936, 597.7419104003906, 606.160810546875], [0, 295.85217248535156, 305.9718645019531, 597.7419104003906, 606.160810546875], [0, 320.25848852539065, 345.26008056640626, 597.7419104003906, 606.160810546875], [0, 45.24097607421875, 66.670912109375, 607.8445905761719, 616.2634907226562], [0, 100.60164416503906, 123.81740820312501, 607.8445905761719, 616.2634907226562], [0, 146.43789624023438, 165.4867282714844, 607.8445905761719, 616.2634907226562], [0, 175.60642028808596, 194.65525231933594, 607.8445905761719, 616.2634907226562], [0, 220.25212036132814, 230.3718123779297, 607.8445905761719, 616.2634907226562], [0, 250.01592041015627, 270.25530444335936, 607.8445905761719, 616.2634907226562], [0, 295.85217248535156, 305.9718645019531, 607.8445905761719, 616.2634907226562], [0, 320.25848852539065, 345.26008056640626, 607.8445905761719, 616.2634907226562], [0, 45.24097607421875, 62.50398010253907, 617.9472707519532, 626.3661708984375], [0, 100.60164416503906, 119.05520019531251, 617.9472707519532, 626.3661708984375], [0, 146.43789624023438, 165.4867282714844, 617.9472707519532, 626.3661708984375], [0, 175.60642028808596, 194.65525231933594, 617.9472707519532, 626.3661708984375], [0, 220.25212036132814, 230.3718123779297, 617.9472707519532, 626.3661708984375], [0, 250.01592041015627, 270.25530444335936, 617.9472707519532, 626.3661708984375], [0, 295.85217248535156, 305.9718645019531, 617.9472707519532, 626.3661708984375], [0, 320.25848852539065, 345.26008056640626, 617.9472707519532, 626.3661708984375], [0, 45.24097607421875, 67.26618811035156, 628.0499509277344, 636.4688510742187], [0, 100.60164416503906, 123.81740820312501, 628.0499509277344, 636.4688510742187], [0, 146.43789624023438, 165.4867282714844, 628.0499509277344, 636.4688510742187], [0, 175.60642028808596, 194.65525231933594, 628.0499509277344, 636.4688510742187], [0, 220.25212036132814, 230.3718123779297, 628.0499509277344, 636.4688510742187], [0, 250.01592041015627, 270.25530444335936, 628.0499509277344, 636.4688510742187], [0, 295.85217248535156, 305.9718645019531, 628.0499509277344, 636.4688510742187], [0, 320.25848852539065, 345.26008056640626, 628.0499509277344, 636.4688510742187], [0, 45.24097607421875, 60.122876098632815, 638.1526311035157, 646.57153125], [0, 100.60164416503906, 119.05520019531251, 638.1526311035157, 646.57153125], [0, 175.60642028808596, 194.65525231933594, 638.1526311035157, 646.57153125], [0, 250.01592041015627, 270.25530444335936, 638.1526311035157, 646.57153125], [0, 320.25848852539065, 345.26008056640626, 638.1526311035157, 646.57153125], [0, 45.24097607421875, 93.45833215332031, 647.4134212646484, 655.8323214111329], [0, 100.60164416503906, 108.34023217773438, 647.4134212646484, 655.8323214111329], [0, 146.43789624023438, 165.4867282714844, 647.4134212646484, 655.8323214111329], [0, 175.60642028808596, 194.65525231933594, 647.4134212646484, 655.8323214111329], [0, 220.25212036132814, 230.3718123779297, 647.4134212646484, 655.8323214111329], [0, 250.01592041015627, 270.25530444335936, 647.4134212646484, 655.8323214111329], [0, 295.85217248535156, 305.9718645019531, 647.4134212646484, 655.8323214111329], [0, 320.25848852539065, 345.26008056640626, 647.4134212646484, 655.8323214111329], [0, 45.24097607421875, 93.45833215332031, 657.5161014404297, 665.935001586914], [0, 100.60164416503906, 108.34023217773438, 657.5161014404297, 665.935001586914], [0, 175.60642028808596, 194.65525231933594, 657.5161014404297, 665.935001586914], [0, 250.01592041015627, 270.25530444335936, 657.5161014404297, 665.935001586914], [0, 320.25848852539065, 345.26008056640626, 657.5161014404297, 665.935001586914], [0, 45.24097607421875, 97.62526416015625, 667.618781616211, 676.0376817626953], [0, 100.60164416503906, 108.34023217773438, 667.618781616211, 676.0376817626953], [0, 175.60642028808596, 194.65525231933594, 667.618781616211, 676.0376817626953], [0, 250.01592041015627, 270.25530444335936, 667.618781616211, 676.0376817626953], [0, 320.25848852539065, 345.26008056640626, 667.618781616211, 676.0376817626953], [0, 45.24097607421875, 91.07722814941407, 677.7214617919922, 686.1403619384765], [0, 100.60164416503906, 119.05520019531251, 677.7214617919922, 686.1403619384765], [0, 146.43789624023438, 165.4867282714844, 677.7214617919922, 686.1403619384765], [0, 175.60642028808596, 194.65525231933594, 677.7214617919922, 686.1403619384765], [0, 220.25212036132814, 230.3718123779297, 677.7214617919922, 686.1403619384765], [0, 250.01592041015627, 270.25530444335936, 677.7214617919922, 686.1403619384765], [0, 295.85217248535156, 305.9718645019531, 677.7214617919922, 686.1403619384765], [0, 320.25848852539065, 345.26008056640626, 677.7214617919922, 686.1403619384765], [0, 45.24097607421875, 80.36226013183594, 687.8241419677735, 696.2430421142578], [0, 100.60164416503906, 119.05520019531251, 687.8241419677735, 696.2430421142578], [0, 146.43789624023438, 165.4867282714844, 687.8241419677735, 696.2430421142578], [0, 175.60642028808596, 194.65525231933594, 687.8241419677735, 696.2430421142578], [0, 220.25212036132814, 230.3718123779297, 687.8241419677735, 696.2430421142578], [0, 250.01592041015627, 270.25530444335936, 687.8241419677735, 696.2430421142578], [0, 295.85217248535156, 305.9718645019531, 687.8241419677735, 696.2430421142578], [0, 320.25848852539065, 345.26008056640626, 687.8241419677735, 696.2430421142578], [0, 45.24097607421875, 80.36226013183594, 697.9268221435547, 706.345722290039], [0, 100.60164416503906, 119.05520019531251, 697.9268221435547, 706.345722290039], [0, 146.43789624023438, 165.4867282714844, 697.9268221435547, 706.345722290039], [0, 175.60642028808596, 194.65525231933594, 697.9268221435547, 706.345722290039], [0, 220.25212036132814, 230.3718123779297, 697.9268221435547, 706.345722290039], [0, 250.01592041015627, 270.25530444335936, 697.9268221435547, 706.345722290039], [0, 295.85217248535156, 305.9718645019531, 697.9268221435547, 706.345722290039], [0, 320.25848852539065, 345.26008056640626, 697.9268221435547, 706.345722290039], [0, 45.24097607421875, 80.36226013183594, 708.029502319336, 716.4484024658203], [0, 100.60164416503906, 119.05520019531251, 708.029502319336, 716.4484024658203], [0, 146.43789624023438, 165.4867282714844, 708.029502319336, 716.4484024658203], [0, 175.60642028808596, 194.65525231933594, 708.029502319336, 716.4484024658203], [0, 220.25212036132814, 230.3718123779297, 708.029502319336, 716.4484024658203], [0, 250.01592041015627, 270.25530444335936, 708.029502319336, 716.4484024658203], [0, 295.85217248535156, 305.9718645019531, 708.029502319336, 716.4484024658203], [0, 320.25848852539065, 345.26008056640626, 708.029502319336, 716.4484024658203], [0, 45.24097607421875, 83.33864013671875, 718.1321824951171, 726.5510826416015], [0, 100.60164416503906, 114.88826818847657, 718.1321824951171, 726.5510826416015], [0, 175.60642028808596, 190.4883203125, 718.1321824951171, 726.5510826416015], [0, 250.01592041015627, 265.4930964355469, 718.1321824951171, 726.5510826416015], [0, 320.25848852539065, 340.49787255859377, 718.1321824951171, 726.5510826416015], [0, 45.24097607421875, 67.86146411132813, 728.2348626708985, 736.6537628173828], [0, 100.60164416503906, 110.12606018066407, 728.2348626708985, 736.6537628173828], [0, 185.72611230468752, 195.2505283203125, 728.2348626708985, 736.6537628173828], [0, 260.7308884277344, 270.85058044433595, 728.2348626708985, 736.6537628173828], [0, 320.25848852539065, 345.26008056640626, 728.2348626708985, 736.6537628173828], [0, 45.24097607421875, 54.76539208984375, 738.3375428466796, 746.756442993164], [0, 100.60164416503906, 123.81740820312501, 738.3375428466796, 746.756442993164], [0, 175.60642028808596, 194.65525231933594, 738.3375428466796, 746.756442993164], [0, 250.01592041015627, 270.25530444335936, 738.3375428466796, 746.756442993164], [0, 320.25848852539065, 340.49787255859377, 738.3375428466796, 746.756442993164], [0, 45.24097607421875, 68.45674011230469, 750.1240030517578, 759.3847932128906], [0, 45.24097607421875, 134.53237622070313, 760.2266832275391, 770.3293634033203], [0, 427.4081687011719, 446.4570007324219, 775.380703491211, 784.6414936523438], [0, 295.85217248535156, 305.9718645019531, 708.029502319336, 716.4484024658203], [0, 320.25848852539065, 345.26008056640626, 708.029502319336, 716.4484024658203], [0, 45.24097607421875, 83.33864013671875, 718.1321824951171, 726.5510826416015], [0, 100.60164416503906, 114.88826818847657, 718.1321824951171, 726.5510826416015], [0, 175.60642028808596, 190.4883203125, 718.1321824951171, 726.5510826416015], [0, 250.01592041015627, 265.4930964355469, 718.1321824951171, 726.5510826416015], [0, 320.25848852539065, 340.49787255859377, 718.1321824951171, 726.5510826416015], [0, 45.24097607421875, 67.86146411132813, 728.2348626708985, 736.6537628173828], [0, 100.60164416503906, 110.12606018066407, 728.2348626708985, 736.6537628173828], [0, 185.72611230468752, 195.2505283203125, 728.2348626708985, 736.6537628173828], [0, 260.7308884277344, 270.85058044433595, 728.2348626708985, 736.6537628173828], [0, 320.25848852539065, 345.26008056640626, 728.2348626708985, 736.6537628173828], [0, 45.24097607421875, 54.76539208984375, 738.3375428466796, 746.756442993164], [0, 100.60164416503906, 123.81740820312501, 738.3375428466796, 746.756442993164], [0, 175.60642028808596, 194.65525231933594, 738.3375428466796, 746.756442993164], [0, 250.01592041015627, 270.25530444335936, 738.3375428466796, 746.756442993164], [0, 320.25848852539065, 340.49787255859377, 738.3375428466796, 746.756442993164], [0, 45.24097607421875, 68.45674011230469, 750.1240030517578, 759.3847932128906], [0, 45.24097607421875, 134.53237622070313, 760.2266832275391, 770.3293634033203], [0, 427.4081687011719, 446.4570007324219, 775.380703491211, 784.6414936523438], [1, 22.620488037109375, 51.78901208496094, 271.08858471679684, 277.8237048339844]]
2026-08-05 12:03:48,531 INFO     29 [qwen-vl-text] ═══ DONE ═══ 254 positions, pages=2, time=151.5s
2026-08-05 12:03:48,531 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 12:03:48,531 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-05 12:03:48,531 INFO     29 [qwen-vl-text] positions(17): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 12:03:48,531 INFO     29 [qwen-vl-text] page grouping: [8], lines per page: [17]
2026-08-05 12:03:48,650 INFO     29 [qwen-vl-text] page=8, rect=595x842, img=(1654x2339), dpi=200
2026-08-05 12:03:48,652 INFO     29 [qwen-vl-text] LLM extraction start, text_len=421
2026-08-05 12:03:48,652 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 12:03:48,652 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 499, \"bbox_end\": 515, \"encounter_dates\": [\"2025-05-26\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "CT胸部薄扫\n基本信息\n就诊类型：住院\n开单医生：吴蓉\n报告医生：马之逸\n审核医生：李莹\n开单时间：2025-05-26 09:11:52\n报告时间：2025-05-26 14:53:14\n审核时间：2025-05-26 14:55:24\n检查时间：2025-05-26 14:43:29\n影像及诊断\n影像所见：两侧胸廓对称，气管居中，两肺纹理增多，两肺少许条索影，界清，两上肺局部胸膜增厚；两肺见多发结节，其中最大者位于左肺下叶背段(Se2，Im124-128)，为实性结节，大小约为7×4mm，气管及分支走形自然，未见狭窄，两肺门及纵隔内未见明显肿大淋巴结影；心脏各房室无殊；冠脉壁钙化；两侧胸膜腔内未见积液征；所扫层面肋骨未见明显异常。\n诊断意见：前片2025-1-17所示两肺炎症基本吸收。\n两肺多发小结节，建议年度随诊。\n两肺少许纤维灶，两上肺局部胸膜增厚；冠脉壁钙化。\n气管内结节状突起，痰栓？建议复查。\n附见：脂肪肝，胆囊结石。",
    "role": "user"
  }
]
[92m12:03:48 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:03:48,653 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:03:48,653 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-05 12:03:48,655 INFO     29 [Trace] task=add7faa6 | doc=YXLA（支气管哮喘）222.pdf | Extractor:ExaminationReport | outputs={"chunks": "6 items, types={'ExaminationReport': 6}", "html": "", "json": "5685 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "2 items, types={'AdmissionRecord': 2}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Prescription\": 2, \"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 2, \"chunks_Medication\": 1}"}
2026-08-05 12:03:48,655 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-05 12:03:48,660 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 12:03:48,667 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 12:03:48,672 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T12:03:48.671+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 11, "lag": 0, "done": 15, "failed": 0, "current": {"add7faa690be11f1a3da71efcdd7cc1f": {"id": "add7faa690be11f1a3da71efcdd7cc1f", "doc_id": "ad4ce53890be11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785928406003, "task_type": "dataflow", "root_trace_id": "97b6871067dc44d0a8770cc05c1f97d7", "root_traceparent": "00-97b6871067dc44d0a8770cc05c1f97d7-b9788b06415dfedf-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "aeebe39490be11f1a3da71efcdd7cc1f": {"id": "aeebe39490be11f1a3da71efcdd7cc1f", "doc_id": "ae83c98a90be11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u54ee\u5598-HJCH222   2.27.pdf", "type": "pdf", "location": "\u54ee\u5598-HJCH222   2.27.pdf", "size": 16296401, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785928407811, "task_type": "dataflow", "root_trace_id": "d72ca28b91c84f599f1151379b451f37", "root_traceparent": "00-d72ca28b91c84f599f1151379b451f37-5c87c8a5dc8089ce-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "b1a9baa290be11f1a3da71efcdd7cc1f": {"id": "b1a9baa290be11f1a3da71efcdd7cc1f", "doc_id": "b169d0b890be11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHGL.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHGL.pdf", "size": 4836707, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785928412411, "task_type": "dataflow", "root_trace_id": "d2b4e8b95ec14beebe14377dfeb00869", "root_traceparent": "00-d2b4e8b95ec14beebe14377dfeb00869-8210764337b1d147-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "b28be2ce90be11f1a3da71efcdd7cc1f": {"id": "b28be2ce90be11f1a3da71efcdd7cc1f", "doc_id": "b2448c9e90be11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHYH.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHYH.pdf", "size": 10529265, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785928413891, "task_type": "dataflow", "root_trace_id": "e3dcb8801128457d8d83b73c11855569", "root_traceparent": "00-e3dcb8801128457d8d83b73c11855569-a468dda7915c610d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "3e98f84c90bf11f1a3da71efcdd7cc1f": {"id": "3e98f84c90bf11f1a3da71efcdd7cc1f", "doc_id": "3543a40e90bf11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "XALI\u9ea6\u6d4e\u65b0\u4e61 2026-03-06 17.04 (1).pdf", "type": "pdf", "location": "XALI\u9ea6\u6d4e\u65b0\u4e61 2026-03-06 17.04 (1).pdf", "size": 161316076, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785928648860, "task_type": "dataflow", "root_trace_id": "011798f1ac614ad79dfcf6d230b3fd04", "root_traceparent": "00-011798f1ac614ad79dfcf6d230b3fd04-a0d937a531746558-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 12:03:48,680 INFO     29 [ChunkMerger] Merged 13 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 2, 'Extractor:Discharge': 2, 'Extractor:Admission': 2, 'Extractor:ExaminationReport': 6} (filtered 3 noise chunks)
2026-08-05 12:03:48,690 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-05 12:03:48,691 INFO     29 [Trace] task=b28be2ce | doc=麦济ZHYH.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-05 12:03:48,691 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-05 12:03:48,691 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-05 12:03:48,691 INFO     29 [Trace] task=b1a9baa2 | doc=麦济ZHGL.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "162 items", "markdown": "", "text": "", "name": "麦济ZHGL.pdf", "output_format": "chunks", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "route_summary": "{\"chunks_Medication\": 3, \"chunks_Clinical\": 2}"}
2026-08-05 12:03:48,691 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-05 12:03:48,691 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-05 12:03:48,691 INFO     29 [Trace] task=add7faa6 | doc=YXLA（支气管哮喘）222.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "13 items, types={'MedicationRecord': 1, 'PrescriptionRecord': 2, 'DischargeRecord': 2, 'AdmissionRecord': 2, 'ExaminationReport': 6}", "name": "YXLA（支气管哮喘）222.pdf"}
2026-08-05 12:03:48,692 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-05 12:03:48,697 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 12:03:48,697 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m12:03:48 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:03:48,698 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:03:48,703 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 12:03:48,703 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-05 12:03:48,997 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1785931287574, 'update_date': datetime.datetime(2026, 8, 5, 12, 1, 27), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 369426, 'status': '1'}
2026-08-05 12:03:49,268 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=CS 扫描全能王
3 亿人都在用的扫描 App
金城大药房
会员号:
积分:112550
本次积分:596.00
名称
规格
数量
厂家
批号
单价
金额
1-布地奈德福莫特罗吸入粉雾剂
320ug:9ug*60吸/支
2.00
阿斯利康制药
PKMR
300.00
596.00
运动员慎用!!!
***重打销售单***
总计数量:2.00
应收:600.00
优惠:4.00
付款:596.00
找零:0.00
销售单号:251210031062
款台号:2
日期:2025-12-10
15:21:53
---
人民医院
H43120200207, 院区: 燕城院区)
基本就诊信息
姓名: 梳
医生: 旅
挂号单: 25000448502
医保号: 5200002600000000600637839
付款: 城乡居民基本医疗 费别: 普通
门诊号: 2502240221
社区号:
门诊就诊:呼吸内科门诊,2025-09-30 14:50
医嘱 | 报告
☑ 已作废 | ☐ 全部
☐ 处方 ☐ 其他
生效时间
内容
用法
2025-09-30
孟鲁司特钠片(杭州默沙东) ▪ (默沙东)10mg*5s/
睡前口服,每天一次,共30天
14:51
盒,共10盒,每次10mg
---
基本就诊信息
姓名：杨
医生：
挂号单：26000068319
医保号：52000026000000006006378395
付款：城乡居民基本医疗 费别：普通
门诊号：2502240221
社区号：
门诊就诊：怀化市刘仁水介入呼吸病学工作室,2026-02-09 11:04
医嘱|报告|
已作废|全部|处方|其他
生效时间
内容
用法
2026-02-09
肺功能全套+支气管舒张试验,共1次
2026-02-09
(基)硫酸沙丁胺醇吸入气雾剂 (山东)
吸入,一次,共1天
11:08
100ug*200揿/瓶,共1瓶,每次400ug
2026-02-09
呼出气一氧化氮测定,共1次
2026-02-09
沙美特罗替卡松粉吸入剂(法国GLAXO)
吸入,每天二次,共1天
12.33
50ug/500ug*60吸/瓶,共1瓶,每次50ug
---
HUAIHUA CENTRAL HOSPITAL
怀化市肿瘤医院
姓名：
性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：
221028180
3.0ppd。神经传导速度，结果：MCV 提示：双侧桡神经、尺神经、正中神经、胫神经、腓总
神经波幅、潜伏期、传导速度在正常范围，SCV 提示：双侧桡神经、尺神经、腓肠神经、腓
浅神经波幅、传导速度在正常范围；双侧正中神经传导速度减慢，结论：考虑双侧正中神经
(感觉纤维)呈脱髓鞘病损。【痰液】革兰氏染色检查：上皮细胞 <10 /LP、白细胞
<10 /LP、GS阳性杆菌 偶见、GS阳性链状排列球菌 1+，标本不合格；抗酸染色、结核杆菌
(TB-DNA)定性、细菌及真菌培养均阴性。请相关科室会诊，结合病史查体及资料，目前不支
持EGPA诊断。入院后予以甲泼尼龙40mg qd静滴抗炎、止咳祛痰、雾化舒张支气管、孟鲁司
特钠片抗气道炎症、解痉平喘、补液、中药调理及中医外治等对症支持治疗，患者病情较前
好转，今患者要求出院，请示张田慧副主任医师后，予以办理出院。
出院情况：患者胸闷气促基本缓解，偶有咳嗽，少许白痰，无胸痛咯血、盗汗，无畏寒发
热。精神、饮食、睡眠尚可，大小便正常。查体：T36.8℃，P68次/分，R20次/分，
BP118/72mmHg，指脉氧饱和度96%。神志清楚，精神尚可。双肺呼吸音清，未闻及明显啰音。
心率68次/分，律齐无杂音。腹部平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。
出院诊断：1.支气管哮喘急性发作期 IgE介导；2.肺炎（CURB-65 0分） 3.右肺中叶内侧
段结节（LU-RADS 2类）。
出院医嘱：
1.注意休息，避免着凉及感染，避免二手烟、厨房油烟及刺激性气体吸入，保持良好生
活习惯，增强体质，适当运动，加强营养；
2.2-3月后返院复查嗜酸性粒细胞、总IgE、肺功能、呼出气一氧化氮评估病情，定期复
查尿常规、尿沉渣、电解质等检查，每年复查胸部CT评估肺结节变化；
3.出院后继续服用中药。
4.出院带药：
舒张支气管：布地奈德福莫特罗吸入粉雾剂 每次320ug（1泡）吸入 每天2次（吸入后漱
口，根据动态复查肺功能结果，调整用药）
祛痰：乙酰半胱氨酸片 每天0.6g（1片） 口服 一天两次
抗气道炎症：孟鲁司特钠片 每次10mg（1片） 口服 每晚一次
5.定期复查神经传导速度，神经内科、风湿免疫科门诊随诊；
6.如有不适，随时医院就诊，我科随诊。
科室护士办公室电话：0745-2329117。主管医师电话：13789357317
医师签名：主治医师
zz1028180
---
第2次入院记录
姓名：
出生地：贵州省天柱县
性别：女
民族：苗族
年龄：37岁
职业：农民
婚姻：已婚
住址：贵州省天柱县远口镇大祥村白蜡树脚组
入院时间：2025-07-11 08:57
记录时间：2025-07-11 14:36
入院方式：步行
主诉：反复胸闷、气促8年，加重1月。
现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。
出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。
既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。
病史陈述者签名：
体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。
出院记录
入院时间：2025-02-24 12:22
出院时间：2025-03-01 10:00
住院天数：5天
记录时间：2025-02-28 20:39
入院诊断：胸闷、气促查因：支气管哮喘可能性大
入院情况：青年女性，因“反复胸闷、气促8年，加重半年”入院。既往体质一般无特殊。
体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸
氧），急性面容，神志清晰，颈静脉无充盈，双肺呼吸音清，可闻及弥漫性哮鸣音。心率89
次/分，心律齐，无杂音。腹部平软，无压痛及反跳痛。双下肢无浮肿。辅助检查：无。
诊疗经过：入院后完善检查：尿常规：隐血 +2.00、PH 6.00、尿比重 1.02、维生素C
+3.00。血清总IgE 221.59IU/ml。血气分析、血常规、大便常规、降钙素原、白介素6测定、
肝功能、心肌酶谱、肾功能、葡萄糖测定、电解质、超敏C反应蛋白、凝血常规、D-二聚体
测定、输血前常规、新冠肺炎病毒核酸检测、甲乙流感病毒抗原快速检测均未见明显异常。
心电图：1.窦性心律 2.正常心电图。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1
0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性；2.弥散功能在正常范
围；肺总量在正常范围，残气量、残总比增高。呼出气一氧化氮试验：FeNO50 11ppd，CaNO
2.0ppd。[痰液]革兰氏染色检查：上皮细胞 >25 /LP、白细胞 <10 /LP、GS阳性链状排列球
菌 2+、GS阴性杆菌 少量、GS阴性双球菌 少量、GS阳性球菌 1+，痰标本不合格；细菌培养、
两次抗酸染色、TB-DNA均阴性。心电图：正常心电图。胸部CT平扫：右肺中叶内侧段结节，
LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。结合患者病史、临床表现及肺功能
结果，可诊断“支气管哮喘急性发作期”，住院期间经抗炎平喘、舒张支气管、止咳化痰、
抗气道炎症、护胃、促进胃肠动力、调节胃肠功能、补液等治疗后，症状较前好转，今患者
及家属要求出院，请示刘仁水主任医师后，予以办理带药出院。
出院情况：患者诉胸闷、气促明显好转，夜间稍有喘息，无发热、咳痰，无腹痛、腹胀、恶
心，精神、食纳、睡眠尚可，大小便正常。查体：T36.6℃，P78次/分，R21次/分，
BP126/78mmHg，血氧饱和度96%。神清，精神尚可。双肺呼吸音清，可闻及少许哮鸣音。心
率78次/分，律齐无杂音。腹平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。
出院诊断：1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：
功能性消化不良？反流性食管炎？其他。
出院医嘱：
（1）避免接触一切可能过敏源，注意保暖，避免感冒受凉，避免剧烈运动，避免接触刺
激性烟雾及吸入二手烟；
姓名：
性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：
220999152
(2) 3月后返院复查肺功能、呼出气一氧化氮评估病情，每年复查胸部CT评估肺结节变化；
(3) 哮喘控制稳定期，腹胀无缓解，建议消化内科就诊，进一步完善胃镜检查；
(4) 继续用药：
舒张支气管：复方甲氧那明胶囊 每次2粒 每天3次，口服
布地奈德福莫特罗吸入粉雾剂 每次320ug（1包）每天1次，吸入
(吸入后漱口，根据动态复查肺功能结果，调整用药)
抗气道炎症：孟鲁司特钠片 每次10mg（1片） 每晚1次，口服
止咳祛痰：润肺膏 每次15g 每天2次，口服
调节肠道功能：马来酸曲美布汀片 每次0.1g（1片） 每天3次，口服
(5) 如有不适，随时医院就诊，我科随诊。
科室电话：0745-2329117 主管医师电话：13789357317
医师签名：主治医师：
---
37岁 科室：呼吸与危重症医学科 床号：42 住院号：
出院记录
入院时间：2025-07-11 08:57
出院时间：2025-07-22 15:00
住院天数：11天
记录时间：2025-07-21 16:14
入院诊断：1.支气管哮喘急性发作期；2.肺炎？3.右肺中叶内侧段结节（LU-RADS 2类）；
4.腹胀查因：功能性消化不良？反流性食管炎？其他。
入院情况：患者女性，37岁，因“反复胸闷、气促8年，加重1月”入院。体格检查：T
36.5℃，P70次/分，R24次/分钟，BP139/92mmHg，指脉氧氧饱和度95%（未吸氧），急性面
容，神志清晰，精神欠佳，气促貌，球结膜无水肿，颈静脉无充盈，双肺呼吸音清，可闻及
少许湿啰音及弥漫性哮鸣音，无胸膜摩擦音。心率70次/分，心律齐，无杂音。腹部平软，
无压痛及反跳痛。双下肢无浮肿。辅助检查：2025-02-25胸部CT平扫，右肺中叶内侧段结节，
LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功
能障碍（FEV1 0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散
功能在正常范围；肺总量在正常范围，残气量、残总比增高。
诊疗经过：入院后完善相关检查：血气分析：吸氧浓度 20.90 %、pH 7.42，m二氧化碳分
压 34.50 mmHg ↓、二氧化碳总量 23.50 mmol/L ↓；血常规：白细胞 5.94×10^9/L、中
性粒细胞比率 52.5%、嗜酸性粒细胞比率 8.1%↑、血红蛋白 139g/L、血小板 239×10^9/L；
尿常规：白细胞 +--、葡萄糖 +1.00、隐血 +2.00、（镜检）白细胞 0-2 /HP、（镜检）红
细胞 + /HP、（镜检）上皮细胞 + /LP；尿沉渣：草酸钙结晶 132个/ul、白细胞 +1.00；
电解质：钾 3.48 mmol/L ↓；总IgE 261.95IU/ml；大便常规、肝肾功能、心肌酶、超敏C
蛋白、凝血功能、D二聚体、PCT、白介素6、输血前四项、葡萄糖、乳酸、双链DNA、单链
DNA、肺炎支原体IgM、肺炎衣原体IgG、过敏源综合14项、新冠肺炎病毒核酸检测、脑寄生
虫全套、IgG4、血管炎四项均未见明显异常。心电图：1.窦性心律 2.正常心电图。CT成套：
胸部(平扫(三维重建))：1.右肺中叶内侧段结节大致同前，LU-RADS 2类，建议年度复查。2.
支气管疾患并双肺少许炎性病变，病灶较前稍增多。肺功能常规通气：1.重度混合性肺通气
功能障碍（FVC占预计值60.06%，FEV1占预计值36.5%，FEV1/FVC52.34%，MMEF75/25、MEF50、
MEF25占预计值的比值分别为10.89%、12.13%、8.6%）；2、最大分钟通气量（MVV）：严重
减退（占预计值39.61%）。舒张试验：1.重度混合性肺通气功能障碍，2.支气管舒张试验阳
性（1.24h无支气管舒张药物使用史；2.吸入万托林气雾剂400ug15分钟后，FEV1/EVC≥12%，
绝对值增加≥200ml）。一口气法弥散功能报告：弥散功能在正常范围（DLCO SB 102.9%），
2.残气量上升、残总比上升 肺总量在正常范围。呼出气一氧化氮，FeNO50：20ppd，CaNO：
怀化市中心医院
HUAIHUA CENTRAL HOSPITAL
怀化市肿瘤医院
姓名：
性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：
221028180
[心前区无隆起]，心尖搏动在左第5肋间锁骨中线内0.5cm处，心率70次/分钟，心律齐，
[各瓣膜听诊区未闻及杂音]。腹部平坦，[腹壁静脉无曲张]，无胃肠型和蠕动波，[全
腹柔软]，[腹部无压痛]，[腹部无反跳痛]，[肝脾肋下未扪及]，Murphy征(-)，叩
诊呈[鼓音]，移动性浊音(-)。肠鸣音正常，[无气过水声]。外生殖器[未查]，肛门
直肠[正常]。脊柱四肢[正常]。 双下肢无浮肿，生理反射正常，病理反射阴性。
辅助检查结果：2025-02-25胸部CT平扫：右肺中叶内侧段结节，LU-RADS 2类，建议年度复
查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1 0.99L，占
预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散功能在正常范围；肺总量
在正常范围，残气量、残总比增高。
入院初步诊断：1.支气管哮喘急性发作期；2.肺炎？
3.右肺中叶内侧段结节（LU-RADS 2类）；4.腹胀查因：功能性消化不良？反流性食管炎？其
他。
主治医师：
副主任医师：
221028180
---
221028180
第2次入院记录
姓名：
性别：女
年龄：37岁
婚姻：已婚
入院时间：2025-07-11 08:57
入院方式：步行
主诉：反复胸闷、气促8年，加重1月。
现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。
出生地：贵州省天柱县
民族：苗族
职业：农民
住址：贵
记录时间：2025-07-11 14:36
出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。
既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。
病史陈述者签名：
体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。
家族史：家族中无同类病人。直系亲属体健。([无遗传倾向疾患])。
病史陈述者签名：
体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软，气管居中，颈静脉无怒张，肝-颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦音。心前区无隆起，无震颤，心率89次/分钟，心律齐，各瓣膜听诊区未闻及杂音。腹部平坦，腹壁静脉无曲张，无胃肠型和蠕动波，全腹柔软，腹部无压痛，腹部无反跳痛，肝脾肋
姓名：杨细兰 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：
220999152
下未扪及，Murphy征(-)，叩诊呈鼓音，肝区无叩痛，肾区无叩痛，移动性浊音(-)。肠鸣音正常，无气过水声。外生殖器无异常，肛门直肠正常。脊柱四肢正常。生理反射正常，病理反射阴性。双下肢无浮肿。:
辅助检查结果：无
入院初步诊断：胸闷、气促查因：支气管哮喘可能性大
主治医师：
主任医师：
姓名：
性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：
220999152
入院记录
姓名：
出生地：贵州省天柱县远口镇大样村白蜡树脚组
性别：女
民族：苗族
年龄：37岁
职业：自由职业者
婚姻：已婚
住址：贵
入院时间：2025-02-24 12:22
记录时间：2025-02-24 14:28
入院方式：步行
主诉：反复胸闷、气促8年，加重半年。
现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳
嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。半年前上述症状逐
渐加重，夜间平卧后尤甚，每晚夜间可闻及喉鸣音，无端坐呼吸、夜间憋醒，无畏寒发热，
无胸闷胸痛心悸，无恶心呕吐，无头痛头晕，无黑朦晕厥等不适，急性发作频率明显增加，
约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，现为诊治来我院，
门诊以“支气管哮喘”收入我科，自起病以来，患者精神食欲睡眠一般，大小便正常，近期
体重无改变。
既往史：平素身体一般。否认高血压病、糖尿病、心脏病病史。否认肝炎、结核等传染病病
史，预防接种史不详。无手术史。无外伤史。无输血史。无食物、药物过敏史。
个人史：[出生于原籍 ， 常住本地 ， 无粉尘放射性物质接触史 ， 否认疫区居住
史]，[无吸烟史 ， 无饮酒史 ， 否认性病及治游史 。
月经史：16 2~3 2025/2/21， 月经周期规律，色红，量少，无痛经。
29~30
婚育史：24岁结婚，育有1子1女，配偶及子女体健。
家族史：家族中无同类病人。直系亲属体健。 无遗传倾向疾患 。
病史陈述者签名：
体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸
氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜
色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，
巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常
分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软、气管居中，颈静脉无怒张，肝-
颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤
正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦
---
报告时间: 2025-02-24
怀化市肿瘤医院
怀化市第二人民医院
鹤城院区
湖南HR
CT影像诊断报告单
ID: 86562633
检查号: CT00525514
姓名:
性别: 女
年龄: 37岁
住院号: 220999152
床号: 46
申请科室: 呼吸与危重症医学科
申请医生: 易莹
检查日期: 2025.02.25
报告日期: 2025.02.25 09:45:16
检查项目: CT成套:胸部(平扫(三维重建))
检查所见:
右肺中叶内侧段叶间裂旁见结节影, 大小约5mm×3mm, 边界清楚。右肺中叶另见
条片状高密度影与胸膜粘连。双肺血管支气管束清晰。两肺门结构清楚, 气管及其主
要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。
意见:
1. 右肺中叶内侧段结节, LU-RADS 2类, 建议年度复查。
2. 右肺中叶少许慢性炎症。
---
怀化市中心医院
HUAIHUA CENTRAL HOSPITAL
怀化市肿瘤医院
湖南HR
CT影像诊断报告单
ID: 93717786
检查号: CT00568277
姓名:
性别: 女
年龄: 37岁
住院号: 221028180
床号: 42
申请科室: 呼吸与危重症医学科
申请医生:
检查日期: 2025.07.11
报告日期: 2025.07.11 16:08:56
检查项目: CT成套胸部平扫(三维重建)
检查所见:
与2025-02-25片对比, 现: 右肺中叶内侧段叶间裂旁见结节影大致同前, 大小约5mm×3mm, 边界清楚。
右肺中叶见条片状高密度影与胸膜粘连较前无明显改变。双肺另见少许絮片状模糊影。双肺血管支气管束部
分增多增粗。两肺门结构清楚, 气管及其主要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。
意见:
1. 右肺中叶内侧段结节大致同前, LU-RADS 2类, 建议年度复查。
2. 支气管疾患并双肺少许炎性病变, 病灶较前稍增多。
---
常规通气报告
姓名：
年龄：38岁
性别：女
科别：
保险：
预计值模式：Standard-new
测试号：2026020917
身高：165 cm
体重：60 kg
备注：
联系电话：
操作者：蒋细萍
Pred
Bst % (B/Pd
A1
A2
A3
FVC
[L]
2.99
2.21
74.02
2.21
2.12
2.09
FEV 1
[L]
2.67
1.26
48.56
1.26
1.13
1.18
FEV6
[L]
2.12
2.12
2.05
2.02
FEV 1 % FVC
[%]
84.19
56.48
67.09
56.48
53.33
56.67
FEV 1 % VC MAX
[%]
81.88
55.26
67.48
55.26
50.10
52.31
VC MAX
[L]
3.03
2.26
74.60
PEF
[L/s]
6.28
2.66
42.36
2.66
2.58
2.43
MMEF 75/25
[L/s]
3.57
0.51
14.35
0.51
0.49
0.41
MEF 75
[L/s]
5.64
1.47
26.14
1.47
0.80
1.21
MEF 50
[L/s]
4.01
0.68
16.97
0.68
0.72
0.57
MEF 25
[L/s]
1.79
0.19
10.52
0.19
0.18
0.15
V backextrapolation ex
[L]
0.05
0.05
0.03
0.04
V backextrapol. % FVC
[%]
2.07
2.07
1.50
1.81
FET
[s]
7.63
7.63
7.35
7.55
FEF 200-1200
[L/s]
1.19
1.19
0.98
1.05
FVC IN
[L]
3.03
2.26
74.60
2.26
2.15
2.13
FIV1
[L]
2.21
2.21
2.12
2.09
FIV1 % FVC
[%]
97.79
97.79
98.68
98.05
FEF50 % FIF50
[%]
22.86
22.86
25.05
19.46
PIF
[L/s]
3.04
3.04
3.04
2.99
MVV
[L/min]
99.77
46.21
46.32
46.21
BF MVV
[1/min]
75.55
75.55
意见：
1. 重度混合性肺通气功能障碍。
2. 最大分钟通气量（MVV）：显著减退。
---
Flow [L/s]
F/V ex
Vol [L]
Vol%VCmax
Vol [L]
Time [s]
Time [s]
10
8
6
4
2
0
1
2
3
4
5
F/V in
6
4
2
0
100
80
60
40
20
0
2
4
6
8
10
12
1
0
2
4
6
8
10
12
1
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
8
6
4
2
0
2
4
6
8
10
12
1
10
呼出气一氧化氮检测报告单
姓名：杨
性别：女
出生日期：1987-12-01
年龄：38岁2个月
ID号：
测试日期：2026-02-09
科室：呼吸科门诊
医生：张
问卷调查：
激素：正在使用口 三天内未使用口 从未使用口
抗生素：正在使用口 三天内未使用口 从未使用口
吸烟史：已戒烟口 1h内未吸烟口 从未吸烟口
症状：咳嗽口 咳痰口 喘息口 鼻塞口 喷嚏口 其他：
病史：过敏史口 其他：
注：检测前1小时内禁水禁食、禁止吸烟、避免剧烈运动；2小时内禁食含硝酸盐食物；4小时内禁酒。
检测信息：
项目：在线
呼气压力：8.8cmH2O 呼气流速：45ml/s
呼气时间：5s 温度：21.8℃ 湿度：38.9%
呼气浓度：10、11、12、11、11、11、10、10、10、
10、10、10、11、10、11、11、11、11ppb
项目：小气道
呼气压力：11.3cmH2O 呼气流速：202ml/s
呼气时间：3s 温度：22.0℃ 湿度：39.0%
呼气浓度：1.0、1.0、1.0、0.0、1.0、0.0
0.0、0.0、0.0、0.0、1.0、1.0、1.0、
1.0、1.0、0.0、0.0、0.0ppb
参考意义：
(根据ATS及ERS 2001及2004年eNO临床指南，结合NO呼气浓度的测定结果及症状判断)
测试项目 FeNO参考值（>12岁） FeNO参考值（≤12岁） 炎症鉴别类型
FeNO < 25ppb < 20ppb* 非嗜酸性气道炎症
25 - 50ppb 20 - 35ppb* 混合型气道炎症
> 50ppb > 35ppb* 嗜酸性气道炎症
CaNO ≤ 5ppb ≤ 3ppb 小气道正常
> 5ppb > 3ppb 小气道炎症
FaNO < 125ppb 考虑Kartagener综合征、PCD、CF或
重度的鼻窦炎或鼻息肉
125 - 250ppb 鼻窦口开放不佳，考虑鼻窦炎或鼻息肉
250 - 500ppb 非过敏性（嗜中性）炎症，考虑感染或其他诊断
> 500ppb 考虑过敏性鼻炎
(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)
此结果仅对本次呼气检测负责
---
测定结果：FeNO 60:11ppb CaNO :1.0ppb
操作员：蒋细萍
张日石
一口气法弥散功能报告
姓名：
年龄：38岁
性别：女
科别：
保险：
预计值模式：Standard-now
测试号：2026020917
身高：155 cm
体重：60 kg
备注：
联系电话：
操作者：蒋细萍
CO (%)
Volume (L)
CH4 [%]
-0.25
-0.20
-0.15
-0.10
-0.05
0
5
10
15
20
25
30
Time [s]
Pred
Best
Best%
Act1
DLCO SB
[mmol/min/kPa]
8.08
9.45
116.9
9.45
DLCO/VA
[mmol/min/kPa/L]
1.82
2.38
130.8
2.38
VA
[L]
4.29
3.97
92.5
3.97
VC IN
[L]
3.03
2.26
74.6
1.00
Discard vol
[L]
0.53
Sample vol
[L]
ERV
[L]
1.10
IRV
[L]
IC
[L]
1.93
VT
[L]
0.43
VC MAX
[L]
3.03
2.26
74.6
TLC-SB
[L]
4.44
4.10
92.4
4.10
RV-SB
[L]
1.41
2.18
154.5
2.18
RV%TLC-SB
[%]
31.88
53.26
167.1
53.26
FRC-SB
[L]
2.51
2.39
95.2
2.39
FRC%TLC-SB
[%]
51.18
58.28
113.9
58.28
测试日期
26/2/0
意见：
1.弥散功能在正常范围。
2.残气量、残总比增高，肺总量在正常范围。
---
张
肺功能试验报告
姓名：
年龄：38岁
性别：女
科别：
保险：
预计值模式：Standard-new
测试号：2026020017
身高：166 cm
体重：60 kg
备注：
联系电话：
操作者：蒋细萍
Pred
A1 A1/Pd
P1 A2/Pd
chg%l
P2 A3/Pd
chg%2
P3 A4/Pd
chg%3
FVC
[L]
2.99
2.21
74.0
2.63
87.9
18.72
2.04
88.2
19.17
2.67
86.0
16.23
FEV 1
[L]
2.67
1.25
48.6
1.62
69.2
21.85
1.84
69.8
23.23
1.60
68.4
20.23
FEV 1 % FVC
[%]
84.19
56.48
67.1
67.97
68.9
2.64
68.40
69.4
3.41
68.42
69.4
3.44
FEV 1 % VC MAX
[%]
81.88
65.26
67.6
67.97
70.8
4.91
68.40
71.3
6.70
68.42
71.4
5.73
VC MAX
[L]
3.03
2.26
74.6
2.63
86.6
16.14
2.64
87.0
16.69
2.57
84.8
13.71
PEF
[L/s]
6.28
2.66
42.4
2.90
46.2
9.17
3.37
53.7
26.79
3.42
64.6
28.64
MMEF 75/25
[L/s]
3.57
0.61
14.4
0.67
18.8
31.03
0.73
20.4
42.01
0.69
19.4
35.02
MEF 50
[L/s]
4.01
0.68
17.0
0.90
22.5
32.75
0.89
22.1
30.15
0.88
21.9
29.17
MEF 25
[L/s]
1.79
0.19
10.5
0.27
15.2
44.16
0.33
18.7
77.66
0.31
17.6
66.49
FET
[s]
7.63
8.01
4.99
7.79
2.14
7.43
-2.60
V backextrapolation ex [L]
0.05
0.04
-11.67
0.04
-18.64
0.04
-13.51
PIF
[L/s]
3.04
3.37
10.91
3.51
15.70
3.60
18.67
FIV1
[L]
2.21
2.56
15.71
2.56
15.66
2.50
13.09
PEF50 % FIF50
[%]
22.86
28.15
23.14
25.36
10.95
27.28
19.33
MVV
[L/min]
99.77
46.21
46.3
BF MVV
[1/min]
75.55
10
Flow [L/s]
F/V ex
1
2
3
4
6
4
2
0
Vol [L]
1
2
3
4
5
2
4
6
8
10
F/V In
Vol%VCmax
0
0
Vol [L]
20
40
60
80
100
1
2
VCmax
3
4
5
6
Time [s]
0
2
4
6
8
10
12
14
意见：
1. 中重度阻塞性肺通气功能障碍。
2. 支气管舒张试验阳性。
(1. 24h内无支气管舒张药物使用史)
(2. 吸入万托林气雾剂400ug15分钟后，FEV1和FVC上升≥12%，绝对值增加≥200ml)
(3. 检查质量：舒张前：A级；舒张后：A级)
张四彩
2026-08-05 12:03:49,858 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 12:03:49,865 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-05 12:03:49,865 INFO     29 [Trace] task=b1a9baa2 | doc=麦济ZHGL.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "162 items", "markdown": "", "text": "", "name": "麦济ZHGL.pdf", "output_format": "chunks", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "route_summary": "{\"chunks_Medication\": 3, \"chunks_Clinical\": 2}"}
2026-08-05 12:03:49,865 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-05 12:03:49,871 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 12:03:49,872 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m12:03:49 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:03:49,873 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:03:50,057 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 12:03:50,062 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-05 12:03:50,062 INFO     29 [Trace] task=b28be2ce | doc=麦济ZHYH.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-05 12:03:50,062 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-05 12:03:50,067 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 12:03:50,067 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 12:03:50,067 INFO     29 [qwen-vl-text] positions(30): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 12:03:50,067 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [30]
2026-08-05 12:03:50,526 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 12:03:50,528 INFO     29 [qwen-vl-text] LLM extraction start, text_len=388
2026-08-05 12:03:50,528 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 12:03:50,528 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 29, \"encounter_dates\": [\"2026-02-13\"], \"department\": \"呼吸内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "内蒙古医科大学附属医院门诊病历\n姓名：\n年龄：62岁\n诊疗号：0014498780\n民族：\n性别：男性\n呼吸内科门诊\n联系电话：\n1\n身份证：\n病情：\n就诊状态：\n就诊时间：2026-02-13 09:14\n生命体征（需要时）：\n体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg\n主诉：哮喘史，近3天呼吸困难加重，夜间咳嗽明显\n现病史：哮喘史，近3天呼吸困难加重，夜间咳嗽明显\n既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎\n无，吸烟史无，无过敏史。\n体格检查：发育正常，营养良好，体型正常，双肺呼吸音清，双肺未闻及啰\n音，双下肢无水肿，体重kg。\n辅助检查：心肺\n过敏史：不详\n初步诊断（西医）：1.支气管哮喘(急性发作期)\n初步诊断（中医）：\n治疗方案：随诊\n醋酸泼尼松片<5mg>\n用量：3.000片/次\n用法：口服，一次/日，5天\n签名：",
    "role": "user"
  }
]
[92m12:03:50 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:03:50,530 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:03:50,769 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-05 12:03:50,769 INFO     29 [Trace] task=add7faa6 | doc=YXLA（支气管哮喘）222.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "13 items, types={'MedicationRecord': 1, 'PrescriptionRecord': 2, 'DischargeRecord': 2, 'AdmissionRecord': 2, 'ExaminationReport': 6}", "name": "YXLA（支气管哮喘）222.pdf", "embedding_token_consumption": 20048}
2026-08-05 12:03:50,769 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-05 12:03:51,006 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-05 12:03:51,006 INFO     29 [Trace] task=add7faa6 | doc=YXLA（支气管哮喘）222.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":13,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-05 12:03:51,021 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:03:51,022 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:03:51,022 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:03:51,022 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:03:51,022 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:03:51,022 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:03:51,022 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:03:51,022 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:03:51,022 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:03:51,022 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:03:51,025 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:03:51,025 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:03:51,025 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:03:51,030 INFO     29 set_progress(add7faa690be11f1a3da71efcdd7cc1f), progress: 0.82, progress_msg: 12:03:51 [DOC Engine]:
Start to index...
2026-08-05 12:03:51,051 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.016s]
2026-08-05 12:03:51,055 INFO     29 set_progress(add7faa690be11f1a3da71efcdd7cc1f), progress: 0.8076923076923077, progress_msg: 
2026-08-05 12:03:51,073 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.011s]
2026-08-05 12:03:51,110 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.020s]
2026-08-05 12:03:51,123 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.008s]
2026-08-05 12:03:51,131 INFO     29 set_progress(add7faa690be11f1a3da71efcdd7cc1f), progress: 1.0, progress_msg: 12:03:51 Indexing done (0.10s). Task done (1893.39s)
2026-08-05 12:03:51,135 INFO     29 [Done], chunks(13), token(20048), elapsed:1893.39
2026-08-05 12:03:51,772 INFO     29 handle_task done for task {"id": "add7faa690be11f1a3da71efcdd7cc1f", "doc_id": "ad4ce53890be11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1785928406003, "task_type": "dataflow", "root_trace_id": "97b6871067dc44d0a8770cc05c1f97d7", "root_traceparent": "00-97b6871067dc44d0a8770cc05c1f97d7-b9788b06415dfedf-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-05 12:03:51,917 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 12:03:51,929 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-05 12:03:51,929 INFO     29 [Trace] task=b1a9baa2 | doc=麦济ZHGL.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "162 items", "markdown": "", "text": "", "name": "麦济ZHGL.pdf", "output_format": "chunks", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "route_summary": "{\"chunks_Medication\": 3, \"chunks_Clinical\": 2}"}
2026-08-05 12:03:51,929 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-05 12:03:51,930 INFO     29 [ChunkMerger] Merged 5 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 3, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1} (filtered 6 noise chunks)
2026-08-05 12:03:51,939 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-05 12:03:51,939 INFO     29 [Trace] task=b1a9baa2 | doc=麦济ZHGL.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "5 items, types={'OutpatientRecord': 2, 'MedicationRecord': 3}", "name": "麦济ZHGL.pdf"}
2026-08-05 12:03:51,939 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-05 12:03:51,996 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1785931430756, 'update_date': datetime.datetime(2026, 8, 5, 12, 3, 50), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 389474, 'status': '1'}
2026-08-05 12:03:52,229 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=内蒙古医科大学附属医院门诊病历
姓名：
年龄：51岁
诊疗号：0011072747
民族：汉族
性别：女性
内科门诊
联系电话：
身份证：
病情：
就诊状态：
就诊时间：2020-02-13 09:12
生命体征（需要时）：
体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg
主诉：哮喘史，近几日咳嗽、胸闷气短症状加重
现病史：哮喘史，近几日咳嗽、胸闷气短症状加重
既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎
无，吸烟史无，无过敏史。
体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺未闻及啰
音，双下肢无水肿，体重kg。
辅助检查：心肺
过敏史：不详
初步诊断（西医）：1.支气管哮喘(急性发作期)
初步诊断（中医）：
治疗方案：随诊
醋酸泼尼松片<5mg>
用量：3.000片/次
用法：口服，一次/日，5天
布地奈德福莫特罗吸入粉雾剂
用量：1.000吸/次
(II)<(320μg/9μg)/吸*60>
用法：吸入，二次/日，30天
签名：
---
内蒙古医科大学附属医院门诊病历
姓名：
年龄：51岁
诊疗号：0011072747
民族：汉族
性别：女性
呼吸内科门诊
联系电话：
身份证：
病情：
就诊状态：
就诊时间：2026-02-09 07:39
生命体征（需要时）：
体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg
主诉：本次为V16访视
现病史：今患者按约回院，受试者自上次访视至今，哮喘症状控制平稳，无哮
喘急性恶化，无哮喘急性发作，无AE,无SAE，无新增合并用药或非
药物治疗。检查并回收发放的日记卡1本，版本号/版本日期
(V2.0/20250916)，受试者日记卡填写正确，发放新的日记卡1本，
指导受试者填写。患者诉自上次访视至今未使用硫酸沙丁胺醇气雾剂
(万托林)，既往发放批号：6J7C，有效期2026-7患者今日出门忘
记携带，嘱患者从今日起停用，择期尽快送回。
既往史：背景用药：2022.12.4-至今规律吸入布地奈德福莫特罗吸入粉雾剂
<(320μg/9μg)用量：1.000吸/次用法：吸入，二次/日 类别
ICS+LABA。
既往病史：
1.肝功能异常：开始时间：2024.12.05，筛选时持续，筛选时接受治
疗，查看今日血生化结果：ALT:46.9U/L,正常值范围：7-40U/L 评
判结果：NCS；SAT：27.7U/L，正常值范围：27.7U/L在正常值范围
内；AST/ALT 0.6 正常值范围：0.8-2 评判结果NCS；以上异常结果与
筛选期结果比较，无恶化，持续状态，故不继续跟进。嘱患者定期复
查肝功。
2.尿路感染：开始时间：2024.12.05，筛选时持续，因患者无不适症
状，未行药物或非药物与治疗。今日查看结果：白细胞：3+，白细胞
计数：169.70；上皮细胞：31.00；管型：1.53 评判结果均CS异常
有临床意义，以上异常结果与筛选期结果比较，无恶化，持续状态，
嘱患者必要时会诊，行药物或非药物治疗，建议4周后回院复查。
此外无持续跟进AE。
体格检查：
辅助检查：8:35休息至少5min完成生命体征检查，结果详见生命体征表；至
少空腹8h，8:36空腹采集血生化、凝血检查，8:56留尿常规检
查，8:30按照中心实验室要求，采集血常规、ADA/Nab检查，按照
要求处理储存并寄送。
过敏史：
初步诊断（西医）：1.支气管哮喘
初步诊断（中医）：
治疗方案：随诊告知受试者继续规律吸入布地奈德福莫特罗吸入粉雾剂
(II)<(320μg/9μg)/吸*60>用量:1.000吸/次用法:吸入,二次/
日。告知患者今日出组。4周后会回院复测尿常规。患者表示无症
状，未给予明确答复是否回院，4周后电话联系。
签名：
---
电子发票(普通发票)
发票号码：25152000000077385777
开票日期：2025年12月24日
购买方信息
统一社会信用代码/纳税人识别号
销售方信息
名称：国药控股国大药房内蒙古有限公司第三百七十三分公司
统一社会信用代码/纳税人识别号：91150121MACGJJ2Q46
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
306.930693069307
306.93
1%
3.07
福莫特罗吸入粉雾剂
合计
¥306.93
¥3.07
价税合计(大写)
叁佰壹拾圆整
(小写)¥310.00
收款人:马利亚;
复核人:梁会荣
备注
开票人:梁会荣
---
欣源药业
NO:2026011900323
商品名称
单价
数量
小计
布地奈德福莫特罗吸入粉雾剂320ug:
9ug*60吸/盒
309.00
2
618.00
阿斯利康
批号: PKGF
效期:2027-03 规格:1支/盒
总计:
2.00
618.00
会员卡号:800310
会员姓名:
本次积分:618.00
累计积分:2518.10
收银员004营业员004
日期26-01-1910:53:22
---
内蒙古医科大学附属医院
门诊缴费凭证
诊疗号: 0011072747
姓名:
收费项目
总额(元)
西药
301.53
(取药窗口: 门诊二楼西药房3号窗口)
开单科室: 呼吸内科门诊
结算类型: 自费
总金额: 301.53元
实付金额: 301.53元
机器编号: zzj217
缴费时间: 2026-02-13 10:13:31
支付方式: 微信
交易订单号: 39N6260213101311FYAzzj217D4230
温馨提示:
如需发票, 请关注我院微信公众号获取
电子发票
2026-08-05 12:03:52,571 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-05 12:03:52,571 INFO     29 [Trace] task=b1a9baa2 | doc=麦济ZHGL.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "5 items, types={'OutpatientRecord': 2, 'MedicationRecord': 3}", "name": "麦济ZHGL.pdf", "embedding_token_consumption": 1844}
2026-08-05 12:03:52,571 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-05 12:03:52,675 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-05 12:03:52,676 INFO     29 [Trace] task=b1a9baa2 | doc=麦济ZHGL.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":5,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-05 12:03:52,679 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:03:52,679 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:03:52,679 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:03:52,679 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:03:52,679 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:03:52,683 INFO     29 set_progress(b1a9baa290be11f1a3da71efcdd7cc1f), progress: 0.82, progress_msg: 12:03:52 [DOC Engine]:
Start to index...
2026-08-05 12:03:52,698 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.010s]
2026-08-05 12:03:52,702 INFO     29 set_progress(b1a9baa290be11f1a3da71efcdd7cc1f), progress: 0.8200000000000001, progress_msg: 
2026-08-05 12:03:52,711 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.006s]
2026-08-05 12:03:52,717 INFO     29 set_progress(b1a9baa290be11f1a3da71efcdd7cc1f), progress: 1.0, progress_msg: 12:03:52 Indexing done (0.03s). Task done (801.37s)
2026-08-05 12:03:52,719 INFO     29 [Done], chunks(5), token(1844), elapsed:801.37
2026-08-05 12:03:52,792 INFO     29 handle_task done for task {"id": "b1a9baa290be11f1a3da71efcdd7cc1f", "doc_id": "b169d0b890be11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHGL.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHGL.pdf", "size": 4836707, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1785928412411, "task_type": "dataflow", "root_trace_id": "d2b4e8b95ec14beebe14377dfeb00869", "root_traceparent": "00-d2b4e8b95ec14beebe14377dfeb00869-8210764337b1d147-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-05 12:03:52,917 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 12:03:52,917 INFO     29 [qwen-vl-text] LLM output (len=585):
{
  "exam_date": "2025-05-26",
  "report_date": "2025-05-26",
  "exam_name": "CT胸部薄扫",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "影像所见：两侧胸廓对称，气管居中，两肺纹理增多，两肺少许条索影，界清，两上肺局部胸膜增厚；两肺见多发结节，其中最大者位于左肺下叶背段(Se2，Im124-128)，为实性结节，大小约为7×4mm，气管及分支走形自然，未见狭窄，两肺门及纵隔内未见明显肿大淋巴结影；心脏各房室无殊；冠脉壁钙化；两侧胸膜腔内未见积液征；所扫层面肋骨未见明显异常。",
  "conclusion": "诊断意见：前片2025-1-17所示两肺炎症基本吸收。\n两肺多发小结节，建议年度随诊。\n两肺少许纤维灶，两上肺局部胸膜增厚；冠脉壁钙化。\n气管内结节状突起，痰栓？建议复查。\n附见：脂肪肝，胆囊结石。",
  "physician": "马之逸",
  "reviewer": "李莹"
}
2026-08-05 12:03:52,917 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=275195, prompt_len=1085
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共17行）
["CT胸部薄扫", "基本信息", "就诊类型：住院", "开单医生：吴蓉", "报告医生：马之逸", "审核医生：李莹", "开单时间：2025-05-26 09:11:52", "报告时间：2025-05-26 14:53:14", "审核时间：2025-05-26 14:55:24", "检查时间：2025-05-26 14:43:29", "影像及诊断", "影像所见：两侧胸廓对称，气管居中，两肺纹理增多，两肺少许条索影，界清，两上肺局部胸膜增厚；两肺见多发结节，其中最大者位于左肺下叶背段(Se2，Im124-128)，为实性结节，大小约为7×4mm，气管及分支走形自然，未见狭窄，两肺门及纵隔内未见明显肿大淋巴结影；心脏各房室无殊；冠脉壁钙化；两侧胸膜腔内未见积液征；所扫层面肋骨未见明显异常。", "诊断意见：前片2025-1-17所示两肺炎症基本吸收。", "两肺多发小结节，建议年度随诊。", "两肺少许纤维灶，两上肺局部胸膜增厚；冠脉壁钙化。", "气管内结节状突起，痰栓？建议复查。", "附见：脂肪肝，胆囊结石。"]

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
2026-08-05 12:03:57,108 INFO     29 [qwen-vl-parser] text API response (len=927):
["病程记录", "姓名：", "科室：呼吸与危重症医学一科  床号：100  住院号：26000328", "2026-01-14  09:00  任医师查房记录", "今随", "医师查房，患者神志清，精神较前明显好转，饮食可，近几日来", "无发热，咳嗽咳痰症状基本消失，胸闷、气喘症状较入院时明显减轻，咳嗽咳痰后胸闷、", "气喘症状亦较前明显减轻，未诉其他不适症状，大小便正常，夜间睡眠可，今查", "体：T:36.6℃，R:22次/分，BP:130/72mmHg，双肺呼吸音粗，两肺未闻及干湿性啰音及", "呼气相哮鸣音。心率82次/分，律齐。双下肢无浮肿。辅助检查：2026-01-14  血常规", "+快速C反应蛋白:白细胞(9-HR) 10.7×10^9/L↑，淋巴细胞计数 4.2×10^9/L↑，单核", "细胞计数 0.8×10^9/L↑，嗜酸性粒细胞计数 0.11×10^9/L；2026-01-14 肺最大通", "气里检查诊断意见:受试者配合不错，通气测试质控优良，满足A级质控标准；1.一秒里", "低，肺活里正常，未见限制因素，一秒率正常，未见阻塞因素，呼气末指标低，小气道功", "能异常，肺通气功能损害分级 轻度；2.MVV测试数据为79.39L/min，占预计值96.6%，通", "气储备86%；2026-01-14 支气管舒张试验诊断意见:受试者配合不错，通气测试质控优", "良，满足A级质控标准，FEV1改善率为20.7%，改善果为309.7ml，PEF变异率大于20%，舒", "张试验阳性，气道反应性轻度可逆，", "医师结合症状、复查血常规及复查肺功能", "结果，查房后指示根据肺功能对比结果，患者经抗感染、扩张气管、雾化吸入、抗炎、解", "痉平喘及改善肺功能治疗，患者目前“支气管哮喘”诊断明确，血常规示嗜酸性粒细胞数", "目已恢复至正常范围，临床症状明显好转准予出院，注意口服糖皮质激素的续贯治疗，并", "注意逐步减量，防止撤停激素过快导致反跳现象发生，同时继续应用三联吸入性药物控制", "症状，上级医师指示已执行。", "主任医师签名：", "副主任医师签名：", "第 1 页"]
2026-08-05 12:03:57,109 INFO     29 [qwen-vl-parser] page=12 text: 27 lines (bbox 341-367)
2026-08-05 12:03:57,110 INFO     29 [qwen-vl-parser] page=12 text: 27 sections
2026-08-05 12:03:57,628 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7531273, prompt_len=764
2026-08-05 12:04:00,409 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 12:04:00,411 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=None
2026-08-05 12:04:00,443 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7531273, prompt_len=401
2026-08-05 12:04:01,298 INFO     29 [qwen-vl-text] coord API raw response (len=1162):
[
	{"text": "CT胸部薄扫", "bbox": [41, 310, 117, 323]},
	{"text": "基本信息", "bbox": [41, 336, 93, 346]},
	{"text": "就诊类型：住院", "bbox": [53, 354, 123, 363]},
	{"text": "开单医生：吴蓉", "bbox": [53, 369, 123, 378]},
	{"text": "报告医生：马之逸", "bbox": [53, 385, 134, 394]},
	{"text": "审核医生：李莹", "bbox": [53, 400, 126, 409]},
	{"text": "开单时间：2025-05-26 09:11:52", "bbox": [431, 369, 570, 378]},
	{"text": "报告时间：2025-05-26 14:53:14", "bbox": [431, 385, 570, 394]},
	{"text": "审核时间：2025-05-26 14:55:24", "bbox": [431, 400, 570, 409]},
	{"text": "检查时间：2025-05-26 14:43:29", "bbox": [797, 369, 933, 378]},
	{"text": "影像及诊断", "bbox": [49, 427, 109, 436]},
	{"text": "影像所见：两侧胸廓对称，气管居中，两肺纹理增多，两肺少许条索影，界清，两上肺局部胸膜增厚；两肺见多发结节，其中最大者位于左肺下叶背段(Se2，Im124-128)，为实性结节，大小约为7×4mm，气管及分支走形自然，未见狭窄，两肺门及纵隔内未见明显肿大淋巴结影；心脏各房室无殊；冠脉壁钙化；两侧胸膜腔内未见积液征；所扫层面肋骨未见明显异常。", "bbox": [59, 443, 952, 464]},
	{"text": "诊断意见：前片2025-1-17所示两肺炎症基本吸收。", "bbox": [59, 471, 276, 480]},
	{"text": "两肺多发小结节，建议年度随诊。", "bbox": [109, 483, 252, 492]},
	{"text": "两肺少许纤维灶，两上肺局部胸膜增厚；冠脉壁钙化。", "bbox": [109, 494, 341, 503]},
	{"text": "气管内结节状突起，痰栓？建议复查。", "bbox": [109, 505, 272, 514]},
	{"text": "附见：脂肪肝，胆囊结石。", "bbox": [109, 516, 222, 525]}
]
2026-08-05 12:04:01,298 INFO     29 [qwen-vl-text] coord API: raw_items=17, valid_items=17, elapsed=8.4s
2026-08-05 12:04:01,298 INFO     29 [qwen-vl-text] coord item[0]: text=CT胸部薄扫, bbox=[41, 310, 117, 323]
2026-08-05 12:04:01,298 INFO     29 [qwen-vl-text] coord item[1]: text=基本信息, bbox=[41, 336, 93, 346]
2026-08-05 12:04:01,299 INFO     29 [qwen-vl-text] coord item[2]: text=就诊类型：住院, bbox=[53, 354, 123, 363]
2026-08-05 12:04:01,299 INFO     29 [qwen-vl-text] coord item[3]: text=开单医生：吴蓉, bbox=[53, 369, 123, 378]
2026-08-05 12:04:01,299 INFO     29 [qwen-vl-text] coord item[4]: text=报告医生：马之逸, bbox=[53, 385, 134, 394]
2026-08-05 12:04:01,299 INFO     29 [qwen-vl-text] coord item[5]: text=审核医生：李莹, bbox=[53, 400, 126, 409]
2026-08-05 12:04:01,299 INFO     29 [qwen-vl-text] coord item[6]: text=开单时间：2025-05-26 09:11:52, bbox=[431, 369, 570, 378]
2026-08-05 12:04:01,299 INFO     29 [qwen-vl-text] coord item[7]: text=报告时间：2025-05-26 14:53:14, bbox=[431, 385, 570, 394]
2026-08-05 12:04:01,299 INFO     29 [qwen-vl-text] coord item[8]: text=审核时间：2025-05-26 14:55:24, bbox=[431, 400, 570, 409]
2026-08-05 12:04:01,299 INFO     29 [qwen-vl-text] coord item[9]: text=检查时间：2025-05-26 14:43:29, bbox=[797, 369, 933, 378]
2026-08-05 12:04:01,299 INFO     29 [qwen-vl-text] coord item[10]: text=影像及诊断, bbox=[49, 427, 109, 436]
2026-08-05 12:04:01,299 INFO     29 [qwen-vl-text] coord item[11]: text=影像所见：两侧胸廓对称，气管居中，两肺纹理增多，两肺少许条索影，界清，两上肺局部胸膜增厚；两肺见多发结节，其中最大者位于左肺下叶背段(Se2，Im124-128)，为实性结节，大小约为7×4mm，气管及分支走形自然，未见狭窄，两肺门及纵隔内未见明显肿大淋巴结影；心脏各房室无殊；冠脉壁钙化；两侧胸膜腔内未见积液征；所扫层面肋骨未见明显异常。, bbox=[59, 443, 952, 464]
2026-08-05 12:04:01,299 INFO     29 [qwen-vl-text] coord item[12]: text=诊断意见：前片2025-1-17所示两肺炎症基本吸收。, bbox=[59, 471, 276, 480]
2026-08-05 12:04:01,299 INFO     29 [qwen-vl-text] coord item[13]: text=两肺多发小结节，建议年度随诊。, bbox=[109, 483, 252, 492]
2026-08-05 12:04:01,299 INFO     29 [qwen-vl-text] coord item[14]: text=两肺少许纤维灶，两上肺局部胸膜增厚；冠脉壁钙化。, bbox=[109, 494, 341, 503]
2026-08-05 12:04:01,299 INFO     29 [qwen-vl-text] coord item[15]: text=气管内结节状突起，痰栓？建议复查。, bbox=[109, 505, 272, 514]
2026-08-05 12:04:01,299 INFO     29 [qwen-vl-text] coord item[16]: text=附见：脂肪肝，胆囊结石。, bbox=[109, 516, 222, 525]
2026-08-05 12:04:01,300 INFO     29 [qwen-vl-text] page=8 — 17/17 coords, api_time=8.4s
2026-08-05 12:04:01,300 INFO     29 [qwen-vl-text] new_positions (17):
[[8, 24.406316040039062, 69.64729211425781, 260.9859045410156, 271.9304747314453], [8, 24.406316040039062, 55.36066809082031, 282.875044921875, 291.2939450683594], [8, 31.549628051757814, 73.21894812011719, 298.02906518554687, 305.6060753173828], [8, 31.549628051757814, 73.21894812011719, 310.6574154052734, 318.23442553710936], [8, 31.549628051757814, 79.76698413085938, 324.1276556396484, 331.7046657714844], [8, 31.549628051757814, 75.00477612304688, 336.756005859375, 344.3330159912109], [8, 256.5639564208984, 339.30732055664066, 310.6574154052734, 318.23442553710936], [8, 256.5639564208984, 339.30732055664066, 324.1276556396484, 331.7046657714844], [8, 256.5639564208984, 339.30732055664066, 336.756005859375, 344.3330159912109], [8, 474.43497277832034, 555.3925089111328, 310.6574154052734, 318.23442553710936], [8, 29.168524047851562, 64.88508410644532, 359.4870362548828, 367.06404638671876], [8, 35.12128405761719, 566.7027529296876, 372.9572764892578, 390.636966796875], [8, 35.12128405761719, 164.29617626953126, 396.5301968994141, 404.10720703124997], [8, 64.88508410644532, 150.00955224609376, 406.6328770751953, 414.2098872070313], [8, 64.88508410644532, 202.98911633300781, 415.8936672363281, 423.47067736816405], [8, 64.88508410644532, 161.915072265625, 425.15445739746093, 432.7314675292969], [8, 64.88508410644532, 132.15127221679688, 434.41524755859376, 441.9922576904297]]
2026-08-05 12:04:01,300 INFO     29 [qwen-vl-text] ═══ DONE ═══ 17 positions, pages=1, time=12.8s
2026-08-05 12:04:01,310 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-05 12:04:01,310 INFO     29 [Trace] task=aeebe394 | doc=哮喘-HJCH222   2.27.pdf | Extractor:ExaminationReport | outputs={"chunks": "2 items, types={'ExaminationReport': 2}", "html": "", "json": "1181 items", "markdown": "", "text": "", "name": "哮喘-HJCH222   2.27.pdf", "output_format": "chunks", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "route_summary": "{\"chunks_Examination\": 2, \"chunks_Clinical\": 3, \"chunks_Admission\": 1, \"chunks_Discharge\": 1}"}
2026-08-05 12:04:01,310 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-05 12:04:01,314 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 12:04:01,314 INFO     29 [qwen-vl-text] LLM output (len=289):
{
  "encounter_date": "2026-02-13",
  "chief_complaint": "哮喘史，近3天呼吸困难加重，夜间咳嗽明显",
  "present_illness": "哮喘史，近3天呼吸困难加重，夜间咳嗽明显",
  "past_history": "患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎无，吸烟史无，无过敏史。",
  "diagnosis": "西医：1.支气管哮喘(急性发作期) 中医：",
  "treatment_plan": "随诊；醋酸泼尼松片<5mg> 3.000片/次 口服，一次/日，5天"
}
2026-08-05 12:04:01,314 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-13]
2026-08-05 12:04:01,318 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2155471, prompt_len=1091
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
2026-08-05 12:04:03,352 INFO     29 [qwen-vl-parser] text API response (len=261):
["病程记录", "姓名：", "科室：呼吸与危重症医学一科 床号：100 住院号：26000328", "2026-01-14 15:30 VTE防治病程记录", "2026-01-14 15:20对患者进行出院前24小时VTE风险评估，Padua评估总分为1分，评估级别为：低危。出血风险：", "无。无机械预防禁忌症。防治措施：（一）一般预防方法：进行静脉血栓栓塞症相关知识宣教，鼓励及早进行主动与被动活", "动，早期进行功能锻炼，根据病情变化，评估、调整预防治疗措施。", "主任医师签名：", "第 1 页"]
2026-08-05 12:04:03,354 INFO     29 [qwen-vl-parser] page=13 text: 9 lines (bbox 368-376)
2026-08-05 12:04:03,354 INFO     29 [qwen-vl-parser] page=13 text: 9 sections
2026-08-05 12:04:03,833 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9437520, prompt_len=764
2026-08-05 12:04:06,628 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 12:04:06,631 INFO     29 [qwen-vl-parser] page=14 classify=text report_date=None
2026-08-05 12:04:06,661 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9437520, prompt_len=401
2026-08-05 12:04:12,360 INFO     29 [qwen-vl-text] coord API raw response (len=1710):
[
	{"text": "内蒙古医科大学附属医院门诊病历", "bbox": [288, 87, 807, 114]},
	{"text": "姓名：", "bbox": [119, 118, 175, 136]},
	{"text": "年龄：62岁", "bbox": [377, 118, 505, 137]},
	{"text": "诊疗号：0014498780", "bbox": [628, 120, 847, 139]},
	{"text": "民族：", "bbox": [119, 141, 175, 158]},
	{"text": "性别：男性", "bbox": [375, 141, 503, 158]},
	{"text": "呼吸内科门诊", "bbox": [707, 143, 849, 161]},
	{"text": "联系电话：", "bbox": [117, 164, 226, 181]},
	{"text": "1", "bbox": [375, 164, 389, 180]},
	{"text": "身份证：", "bbox": [422, 164, 504, 181]},
	{"text": "病情：", "bbox": [791, 167, 849, 184]},
	{"text": "就诊状态：", "bbox": [116, 186, 225, 203]},
	{"text": "就诊时间：2026-02-13 09:14", "bbox": [359, 186, 693, 203]},
	{"text": "生命体征（需要时）：", "bbox": [117, 209, 350, 227]},
	{"text": "体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg", "bbox": [115, 233, 613, 251]},
	{"text": "主诉：哮喘史，近3天呼吸困难加重，夜间咳嗽明显", "bbox": [113, 256, 714, 275]},
	{"text": "现病史：哮喘史，近3天呼吸困难加重，夜间咳嗽明显", "bbox": [113, 280, 714, 298]},
	{"text": "既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "bbox": [112, 304, 965, 323]},
	{"text": "无，吸烟史无，无过敏史。", "bbox": [220, 328, 505, 346]},
	{"text": "体格检查：发育正常，营养良好，体型正常，双肺呼吸音清，双肺未闻及啰", "bbox": [112, 352, 935, 370]},
	{"text": "音，双下肢无水肿，体重kg。", "bbox": [245, 375, 561, 394]},
	{"text": "辅助检查：心肺", "bbox": [110, 401, 304, 419]},
	{"text": "过敏史：不详", "bbox": [112, 425, 292, 443]},
	{"text": "初步诊断（西医）：1.支气管哮喘(急性发作期)", "bbox": [112, 448, 631, 467]},
	{"text": "初步诊断（中医）：", "bbox": [112, 472, 319, 490]},
	{"text": "治疗方案：随诊", "bbox": [112, 495, 292, 513]},
	{"text": "醋酸泼尼松片<5mg>", "bbox": [110, 554, 315, 572]},
	{"text": "用量：3.000片/次", "bbox": [605, 552, 804, 571]},
	{"text": "用法：口服，一次/日，5天", "bbox": [148, 578, 443, 597]},
	{"text": "签名：", "bbox": [575, 675, 634, 693]}
]
2026-08-05 12:04:12,360 INFO     29 [qwen-vl-text] coord API: raw_items=30, valid_items=30, elapsed=11.0s
2026-08-05 12:04:12,360 INFO     29 [qwen-vl-text] coord item[0]: text=内蒙古医科大学附属医院门诊病历, bbox=[288, 87, 807, 114]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[119, 118, 175, 136]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：62岁, bbox=[377, 118, 505, 137]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[3]: text=诊疗号：0014498780, bbox=[628, 120, 847, 139]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[4]: text=民族：, bbox=[119, 141, 175, 158]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[5]: text=性别：男性, bbox=[375, 141, 503, 158]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[6]: text=呼吸内科门诊, bbox=[707, 143, 849, 161]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[7]: text=联系电话：, bbox=[117, 164, 226, 181]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[8]: text=1, bbox=[375, 164, 389, 180]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[9]: text=身份证：, bbox=[422, 164, 504, 181]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[10]: text=病情：, bbox=[791, 167, 849, 184]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[11]: text=就诊状态：, bbox=[116, 186, 225, 203]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[12]: text=就诊时间：2026-02-13 09:14, bbox=[359, 186, 693, 203]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[13]: text=生命体征（需要时）：, bbox=[117, 209, 350, 227]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[14]: text=体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg, bbox=[115, 233, 613, 251]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[15]: text=主诉：哮喘史，近3天呼吸困难加重，夜间咳嗽明显, bbox=[113, 256, 714, 275]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[16]: text=现病史：哮喘史，近3天呼吸困难加重，夜间咳嗽明显, bbox=[113, 280, 714, 298]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[17]: text=既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎, bbox=[112, 304, 965, 323]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[18]: text=无，吸烟史无，无过敏史。, bbox=[220, 328, 505, 346]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[19]: text=体格检查：发育正常，营养良好，体型正常，双肺呼吸音清，双肺未闻及啰, bbox=[112, 352, 935, 370]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[20]: text=音，双下肢无水肿，体重kg。, bbox=[245, 375, 561, 394]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[21]: text=辅助检查：心肺, bbox=[110, 401, 304, 419]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[22]: text=过敏史：不详, bbox=[112, 425, 292, 443]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[23]: text=初步诊断（西医）：1.支气管哮喘(急性发作期), bbox=[112, 448, 631, 467]
2026-08-05 12:04:12,361 INFO     29 [qwen-vl-text] coord item[24]: text=初步诊断（中医）：, bbox=[112, 472, 319, 490]
2026-08-05 12:04:12,362 INFO     29 [qwen-vl-text] coord item[25]: text=治疗方案：随诊, bbox=[112, 495, 292, 513]
2026-08-05 12:04:12,362 INFO     29 [qwen-vl-text] coord item[26]: text=醋酸泼尼松片<5mg>, bbox=[110, 554, 315, 572]
2026-08-05 12:04:12,362 INFO     29 [qwen-vl-text] coord item[27]: text=用量：3.000片/次, bbox=[605, 552, 804, 571]
2026-08-05 12:04:12,362 INFO     29 [qwen-vl-text] coord item[28]: text=用法：口服，一次/日，5天, bbox=[148, 578, 443, 597]
2026-08-05 12:04:12,362 INFO     29 [qwen-vl-text] coord item[29]: text=签名：, bbox=[575, 675, 634, 693]
2026-08-05 12:04:12,362 INFO     29 [qwen-vl-text] page=0 — 30/30 coords, api_time=11.0s
2026-08-05 12:04:12,363 INFO     29 [qwen-vl-text] new_positions (30):
[[0, 171.35999999999999, 480.16499999999996, 73.25399999999999, 95.988], [0, 70.80499999999999, 104.125, 99.356, 114.512], [0, 224.315, 300.47499999999997, 99.356, 115.354], [0, 373.65999999999997, 503.965, 101.03999999999999, 117.038], [0, 70.80499999999999, 104.125, 118.722, 133.036], [0, 223.125, 299.28499999999997, 118.722, 133.036], [0, 420.66499999999996, 505.155, 120.40599999999999, 135.56199999999998], [0, 69.615, 134.47, 138.088, 152.402], [0, 223.125, 231.45499999999998, 138.088, 151.56], [0, 251.08999999999997, 299.88, 138.088, 152.402], [0, 470.645, 505.155, 140.614, 154.928], [0, 69.02, 133.875, 156.612, 170.926], [0, 213.605, 412.335, 156.612, 170.926], [0, 69.615, 208.25, 175.97799999999998, 191.134], [0, 68.425, 364.73499999999996, 196.186, 211.34199999999998], [0, 67.235, 424.83, 215.552, 231.54999999999998], [0, 67.235, 424.83, 235.76, 250.916], [0, 66.64, 574.175, 255.968, 271.966], [0, 130.9, 300.47499999999997, 276.176, 291.332], [0, 66.64, 556.3249999999999, 296.384, 311.53999999999996], [0, 145.775, 333.79499999999996, 315.75, 331.748], [0, 65.45, 180.88, 337.642, 352.798], [0, 66.64, 173.73999999999998, 357.84999999999997, 373.006], [0, 66.64, 375.445, 377.216, 393.214], [0, 66.64, 189.80499999999998, 397.424, 412.58], [0, 66.64, 173.73999999999998, 416.78999999999996, 431.94599999999997], [0, 65.45, 187.42499999999998, 466.46799999999996, 481.62399999999997], [0, 359.97499999999997, 478.38, 464.784, 480.782], [0, 88.06, 263.585, 486.676, 502.674], [0, 342.125, 377.22999999999996, 568.35, 583.506]]
2026-08-05 12:04:12,363 INFO     29 [qwen-vl-text] ═══ DONE ═══ 30 positions, pages=1, time=22.3s
2026-08-05 12:04:12,363 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 12:04:12,363 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 12:04:12,363 INFO     29 [qwen-vl-text] positions(24): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 12:04:12,363 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [24]
2026-08-05 12:04:12,918 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 12:04:12,920 INFO     29 [qwen-vl-text] LLM extraction start, text_len=426
2026-08-05 12:04:12,920 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 12:04:12,920 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 128, \"bbox_end\": 151, \"encounter_dates\": [\"2024-12-10\"], \"department\": \"呼吸内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录:\n病历信息 □痕迹 □批注 置未 ▼ 状态:只读-仅供查看 120% >\n内蒙古医科大学附属医院门诊病历\n姓名 龄:60岁 诊疗号:0014498780\n民族: 别:男性 科室:呼吸内科门诊\n联系电话: 身份证:1 病情:\n就诊状态: 就诊时间:2024-12-10 12:37\n生命体征(需要时):\n体温:℃ 脉搏:次/分 呼吸:次/分 血压:/mmHg\n主诉:SSSJ项目肺功能检查开单\n现病史:哮喘\n既往史:患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎\n无,吸烟史无,无过敏史。\n体格检查:发育正常,营养良好,体型正力,双肺呼吸音清,双肺未闻及啰\n音,双下肢无水肿,体重kg。\n辅助检查:\n初步诊断(西医):1.哮喘\n初步诊断(中医):\n治疗方案:/\n呼吸过滤器 肺通气功能检查\n用量:\n用法:\n签名:崔丽英\n3:34 星期二 190.1.48.233 版本 王立红",
    "role": "user"
  }
]
2026-08-05 12:04:12,921 INFO     29 [ChunkMerger] Merged 7 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 3, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 2} (filtered 4 noise chunks)
[92m12:04:12 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:04:12,922 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:04:13,285 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-05 12:04:13,285 INFO     29 [Trace] task=aeebe394 | doc=哮喘-HJCH222   2.27.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "7 items, types={'OutpatientRecord': 3, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 2}", "name": "哮喘-HJCH222   2.27.pdf"}
2026-08-05 12:04:13,286 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-05 12:04:13,423 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1785931432560, 'update_date': datetime.datetime(2026, 8, 5, 12, 3, 52), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 391318, 'status': '1'}
2026-08-05 12:04:13,641 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=验(0)
输血(0)
基本
姓名
就诊号：2003700
性别：男
就诊年龄：46岁
就诊时间：08:38:26
科室：呼吸与危重医学科门诊
接诊医生：吴睿
病史
主诉：反复咳嗽咳痰20年余，加重2月余。
现病史：患者既往20年前确诊支气管哮喘，间断服用倍必可。2月前，患者咳嗽咳痰加重，咽痒时明显，痰不多，白痰为主，少许黄粘痰，无畏寒发热，伴胸痛无咯血，无胸闷气促等不适。现为进一步诊治来我院就诊。
婚育史：-
家族史：否认家族精神病史、家族遗传病、家族传染病、家族肿瘤史。
个人史：否认吸烟史，否认饮酒史，否认疫区游历及疫水、疫源接触史。
既往史：否认高血压、糖尿病、心脏病、脑血管意外、肺部疾病、肾病等重大疾病病史，否认肝炎、结核、疟疾等传染病史，否认外伤、手术史否认药物食物过敏史。否认长期用药史
专科检查：-
体格检查：皮肤巩膜无黄染无黄染，浅表淋巴结无肿大浅表淋巴结无肿大，神志清，颈静脉无充盈无充盈，气管居中居中，心律齐齐，未闻及心脏杂音未闻及心脏杂音。左左肺呼吸音清清，右右肺呼吸音清清，双肺未闻及干湿啰音，肺未闻及干湿啰音。腹部平坦平坦，腹软软，腹部无压痛腹部无压痛，未扪及腹部肿块未扪及腹部肿块，肝脏无肿大肝脏无肿大，脾脏无肿大脾脏无肿大，双肾区双肾区无叩痛无叩痛，双下肢无水肿无水肿，病理征未引出未引出
诊断与处置
初步诊断：支气管哮喘
处置意见：忌烟酒。
其他内容
---
基本信息
姓名:
就诊号: 20037
性别: 男
就诊年龄: 47岁
就诊时间: 2026-01-05 08:05:48
科室: 呼吸与危重症医学科门诊
接诊医生: 黄连军
病史
主诉: 哮喘3年, 配药
现病史: 患者哮喘3年, 稳定期, 配药
婚育史: -
家族史: 否认家族精神病史、家族遗传病、家族传染病史、家族肿瘤史。
个人史: 否认吸烟史, 否认饮酒史。否认疫区游历及疫水、疫源接触史。
既往史: 否认高血压、糖尿病、心脏疾病、脑血管意外、其他肺部疾病、胃病等重大疾病病史, 否认肝炎、结核、疟疾等传染病史, 否认外伤、手术史 否认药物食物过敏史。
专科检查: -
体格检查: SpO2 99%, 营养状况好 好, 皮肤巩膜无黄染 无黄染, 浅表淋巴结无肿大 浅表淋巴结无肿大, 神智清 神智清, 颈静脉 无充盈 无充盈, 气管 居中 居中, 心律 齐 齐, 未闻及心脏杂音 未闻及心脏杂音。
呼吸音 粗 粗, 双肺未闻及干湿啰音 双肺未闻及干湿啰音。腹部 平坦 平坦, 腹肌 软 软, 腹部无压痛 腹部无压痛, 未扪及腹部肿块 未扪及腹部肿块, 肝脏无肿大 肝脏无肿大, 脾脏无肿大 脾脏无肿大, 双
双下肢 无水肿 无水肿, 病理征 未引出 未引出。
诊断与处置
初步诊断: 支气管哮喘
处置意见: 处方药品: 1布地奈德福莫特罗吸入粉雾剂(Ⅲ)(信必可都保320)320μg:9μg*60吸/支 1支 1吸 口腔吸入 每日2次 30天 2桉柠蒎肠溶软胶囊(切诺)0.3g*18粒/盒 1盒 1粒 口服(饭前) 每日2次 8天 3 盐酸氨溴索口服溶液
口服 每日2次 10天 4 氨雷他定片(雷苏)10mg*12片/盒 1盒 1片 口服 每天一次 7天
---
学科门诊 2026-02-02
[0]
检验(0)
输血(0)
基本信户
姓名
就诊号: 2
60
性别: 男
就诊
就诊时间: 2026-02-02 14:19:31
科室: 呼吸与危重症医学科门诊
接诊医生: 黄连军
病史
主诉: 哮喘3年, 配药
现病史: 患者哮喘3年, 稳定期, 配药
婚育史: -
家族史: 否认家族精神病史、家族遗传病、家族传染病史、家族肿瘤史。
个人史: 否认吸烟, 否认饮酒史。否认疫区游历及疫水、疫源接触史。
既往史: 否认高血压、糖尿病、心脏疾病、脑血管意外、肺部疾病、胃病等重大疾病病史, 否认肝炎、结核、疟疾等传染病史, 否认外伤、手术史 否认药物食物过敏史, 否认长期用药史
专科检查: -
体格检查: SpO2 97%, 营养状况好 好, 皮肤巩膜 无黄染 无黄染, 浅表淋巴结无肿大 浅表淋巴结无肿大, 神智清 神智清, 颈静脉 无充盈 无充盈, 气管 居中 居中, 心律 齐 齐, 未闻及心脏杂
呼吸音 清 清, 双肺未闻及干湿啰音 双肺未闻及干湿啰音。腹部 平坦 平坦, 腹肌 软 软, 腹部无压痛 腹部无压痛, 未扪及腹部肿块 未扪及腹部肿块, 肝脏无肿大 肝脏无肿大, 脾脏无
双下肢 无水肿 无水肿, 病理征 未引出 未引出
诊断与处置
初步诊断: 支气管哮喘
处置意见: 处方药品: 1布地奈德福莫特罗吸入粉雾剂(Ⅲ)(信必可都保320)320μg:9μg*60吸/支 1支 1吸 口腔吸入 每日2次 30天 2厄多司坦胶囊(坦通)0.15g*12粒/盒 2盒 2粒 口服 每日2次 6天 3银黄颗粒
天
---
换页符
既往史
婚育史
家族史
生命体
生命体
出院记录
姓名：
病历号：
7 科室名称：呼吸与危重症医学科病房 病区：七病区 床号：0747
入院时间：2025-05-26 出院时间：2025-05-31 住院天数：[5]天
入院诊断：1.支气管哮喘 2.脂肪肝
出院诊断：1.支气管哮喘 2.脂肪肝 3.癌胚抗原CEA升高 4.肺诊断性影像异常(肺结节) 5.胆囊结
石 6.(右侧)单纯性肾囊肿 7.肺炎
入院情况：[1、患者性别：男，中年，自由职业者，因反复胸闷气喘20余年，再发2天。既往有“脂肪
肝”病史。2、查体：神志清，精神稍软，双肺呼吸音粗，可闻及哮鸣音，心律齐，未闻及病理性杂音，
肝脾肾未触及，双下肢无明显浮肿。3、辅助检查：本次暂缺。]
住院期间辅助检查：
阳性结果：2025-05-28 03:37 免疫球蛋白IgE测定：总IgE 439.00↑ IU/mL。2025-05-27 08:26 生化检查
项目：胆碱脂酶 12031↑ U/L，葡萄糖 6.42↑ mmol/L，总胆固醇 6.03↑ mmol/L，低密度脂蛋白 3.47
↑ mmol/L，尿酸 430↑ μmol/L。2025-05-27 10:15 肿瘤标志系列(男)：癌胚抗原 8.87↑ ng/ml。2025
-05-27 09:14 免疫六项、梅毒艾滋筛查：乙肝核心抗体 16.31↑ PEI U/ml。2025-05-26 10:24 血气分析
+全血乳酸：动脉氧分压 79.1↓ mmHg，高铁血红蛋白 0.1↓ %，肺泡氧分压 105.0↑ mmHg，肺泡动脉氧
分压差 25.9↑ mmHg，体温下氧分压 77.6↓ mmHg。2025-05-27 08:12 血常规+超敏C+血型：Rh血型 阳性
↑，中性粒细胞绝对值 6.55↑ 10^9/L，淋巴细胞绝对值 0.94↓ 10^9/L，嗜酸性细胞绝对值 0.01↓ 10
^9/L，中性粒细胞百分数 84.70↑ %，淋巴细胞百分数 12.20↓ %，单核细胞百分数 2.90↓ %，嗜酸性
细胞百分数 0.10↓ %。2025-05-28 08:48 细菌培养及鉴定(咽拭子*含真菌)：细菌培养及鉴定(咽拭子*含
真菌) 未检到嗜血杆菌，细菌培养及鉴定(咽拭子*含真菌) 培养无真菌生长，细菌培养及鉴定(咽拭子*含
真菌) 正常菌群生长+++。2025-05-26 15:14 常规心电图：大致正常心电图。2025-05-26 14:53 CT胸部
薄扫：前片2025-1-17所示两肺炎症基本吸收。 两肺多发小结节，建议年度随诊。 两肺少许纤维灶，两
上肺局部胸膜增厚；冠脉壁钙化。 气管内结节状突起，痰栓？建议复查。 附见：脂肪肝，胆囊结石。20
25-05-26 14:52 双肾输尿管膀胱前列腺，脂肪肝。胆囊多发结石。右肾囊肿。前列腺钙化灶。2025-0
^9/L, 中性粒细胞百分数 84.70↑%, 淋巴细胞百分数 12.20↓%, 单核细胞百分数 2.90↓%, 嗜酸性
细胞百分数 0.10↓%。2025-05-28 08:48 细菌培养及鉴定(咽拭子*含真菌):细菌培养及鉴定(咽拭子*含
真菌) 未检到嗜血杆菌, 细菌培养及鉴定(咽拭子*含真菌) 培养无真菌生长, 细菌培养及鉴定(咽拭子*含
真菌) 正常菌群生长+++。2025-05-26 15:14 常规心电图:大致正常心电图。2025-05-26 14:53 CT胸部
薄扫:前片2025-1-17所示两肺炎症基本吸收。两肺多发小结节,建议年度随诊。两肺少许纤维灶,两
上肺局部胸膜增厚;冠脉壁钙化。气管内结节状突起,痰栓?建议复查。附见:脂肪肝,胆囊结石。20
25-05-26 14:52 双肾输尿管膀胱前列腺:脂肪肝。胆囊多发结石。右肾囊肿。前列腺钙化灶。2025-0
5-26 14:50 心超(心脏彩色多普勒超声+左心功能测定):左室舒张功能减退。2025-05-28 03:37 免疫
球蛋白IgE测定
阴性结果:2025-05-28 08:40 大便常规+轮状病毒、2025-05-27 09:12 降钙素原+白介素-6测定、2025-0
5-27 08:53 尿常规组套、2025-05-27 08:46 凝血功能五项、2025-05-27 08:16 脑钠肽(普)、2025-05-2
7 08:09 呼吸道病毒抗体五项、2025-05-27 07:55 血沉、2025-05-27 07:33 肌钙蛋白I2025-05-28 08:4
8 细菌培养及鉴定(咽拭子*含真菌)2025-05-28 08:40 大便常规+轮状病毒:未见明显异常。
[诊治经过(包括重要发现和结论、接受的手术和操作、药物和其他治疗)]
入院后完善相关辅助检查予甲泼尼龙琥珀酸钠针抗炎平喘,莫西沙星针抗感染,氨溴索针联合厄多司坦胶
囊化痰,雾化舒张支气管、补液等对症处理。
出院情况:
患者胸闷气促缓解,咳嗽咳痰好转,体温正常,无胸痛心悸,无畏寒寒战,无恶心呕吐等不适。查体:
[血氧饱和度:98,血压:上肢120/74mmHg,神志清,精神尚可,双肺呼吸音粗,未闻及明显哮鸣音,心
律齐,未闻及病理性杂音,肝脾肾未触及,双下肢无明显浮肿。]现患者病情恢复良好,一般情况尚可,
今予以出院。
VTE分析及出血风险评估:VTE:{低危};出血风险评估:{低危},鼓励适当活动,如有不适请及时就诊。
并发症:无。
治疗效果:{好转}
出院医嘱:1.门诊复查肺功能协助诊治。
出院带药:布地奈德福莫特罗吸入粉雾剂(II)(信必可都保320)每次1吸每日2次;
厄多司坦胶囊(坦通)0.15g*12粒/盒每次2粒每日2次;
---
浏览
病案首页 x
刷新
关闭文
留痕记录
编辑
打印
预览
•基本信息 •出院诊断 •病理诊断 •其他信息 •医务工 作 •手术及操作记录 •出院情况 •费用 •住院首页附页内容
基本信息
医疗付费方式 城镇职工基本医疗保险
健康卡号 -
住院次数 1
病案号
姓名
性别 男
证件号 居民身份证
出生日期 1978年12月13日
33260219;
年龄 46岁
(年龄不足一周岁)年龄 -
新生儿出生体重(g) 克
新生儿入院体重(g) 克
国籍 中国
民族 汉族
职业 自由职业者
0
出生地 中国浙江省台州市临海市
籍贯 浙江省台州市临海市
现住址 中国浙江省台州市临海市
村
邮政编码 317000
户籍地址 中国浙江省台州市临海市.
.村
邮政编码 317000
婚姻 未婚
本人电话 1
3
工作单位 石鼓村
工作单位电话 3
单位地址 中国浙江省台州市临海市石鼓村
邮政编码 317000
联系人姓名
关系 兄、弟、姐、妹
电话
联系人地址 浙江省
水丰
镇石鼓
入院途径 门诊
入院情况 一般
0
0
入院情况：1.有，2.临床未确定，3.情况不明，4.无
门(急)诊诊断 支气管哮喘
入院初诊 支气管哮喘
入院诊断编码 J45.900x001
疾病编码 J45.900x001
入院时间 2025-05-26 08:34
入院科别 呼吸与危重症医学科病房
入院病区 七病区
0
0
转科科别 -
出院时间 2025-05-31 10:46
出院科别 呼吸与危重症医学科病房
出院病区 七病区
实际住院天数 5天
0
住院病历
姓名：胡金超 病历号：100
科室名称：呼吸与危重症医学科病房 病区：七病区 床号：0747
入院记录
姓名：
工作单位：石鼓村
性别：男
住址：中国浙江省台州市
年龄：46岁
出生地：中国浙江省台州市临海市
婚姻：未婚
入院日期：2025-05-26 08:34
民族：汉族
记录日期：2025-05-26 09:31
职业：自由职业者
病史陈述者：本人
主诉：
反复胸闷气喘20余年，再发2天。
现病史：患者20余年前无明显诱因下开始出现胸闷气喘不适，休息后缓解，少许咳嗽，无明显咳痰，无畏
寒寒战，无胸痛等不适。在当地医院按“支气管哮喘”给予抗感染、平喘等治疗后症状缓解。此后每因受
凉上述症状反复发作，现长期予“信必可160”改善症状。2天前，患者受凉后再次出现胸闷、气喘，活动
后加重，休息可缓解，伴咳嗽咳痰，呈阵发性，咳少许黄白粘痰，质粘，不易咳出，无发热，无盗汗消
瘦，无畏寒寒战，无胸痛，无咯血，无腹痛腹泻等不适。现为进一步诊治，来我院就诊，拟“支气管哮
喘”收住我科。
患者起病以来，神志清，精神稍软，胃纳、睡眠一般，二便无明显异常，体重近期无增减。
既往有“脂肪肝”5年余，具体不详，未规律复查。
既往史：[否认]内分泌疾病史；[否认]心血管疾病史；[否认]脑血管疾病史；[否认]肾病史；[否认]肝病
史；[否认]其他重大内科疾病史；[否认]肺结核；[否认]病毒性肝炎；[否认]其他传染病；有“头孢克
洛”过敏史，服用后表现为胸闷；[否认]食物、其他药物过敏；[否认]外伤史；[否认]手术史；[否认]输
血史；[否认]中毒史；[否认]长期用药史；[否认]可能成瘾药物。疫苗接种史不详。
显示
既往史
婚育史
家族史
生命体征
生命体征
110%
洛”过敏史，服用后表现为胸闷；[否认]食物、其他药物过敏；[否认]外伤史；[否认]手术史；[否认]输
血史；[否认]中毒史；[否认]长期用药史；[否认]可能成瘾药物。疫苗接种史不详。
个人史：出生于[中国浙江省台州市临海市]，居住较长地：[台州临海]，职业：[自由职业者]，学历：
[普通高中毕业]，宗教：[无]。[无]饮酒习惯。[无]吸烟习惯。[无]毒物、粉尘及放射性物质接触史。
[无]冶游史，[无]疫区居留史。
婚育史：[未婚][未育]，。
家族史：父亲[体健]，母亲[体健]，1兄弟姐妹[体健]，直系亲属[无]类似疾病项。患者[否认]二系三代
有遗传病史。患者[否认]有遗传倾向的疾病。
换页符
体格检查
生命体征：体温：[36.8]℃， 脉搏：[87]次/分， 呼吸：[19]次/分， 血压：[157]/ [87]mmHg
一般情况：意识[清楚]，[自主体位]，[急性面容]，查体[合作]，身高：[167.5]cm，体重：[83.8]kg,B
MI指数：[29.9]。
皮肤黏膜：[皮肤粘膜无黄染]，[无水肿]，[无]。
浅表淋巴结：[全身浅表淋巴结无肿大]。
头颅五官：头颅[无畸形]，听力粗测[良好]。结膜[无充血水肿]，巩膜[无黄染]，瞳孔[双侧等大同圆]，
对光反射[灵敏]，鼻通气良好，副鼻窦[无压痛]，[乳突无压痛]，口腔粘膜[无充血、糜烂、溃疡]，咽部
充血，两侧扁桃体[无肿大]。
颈部：颈[软]，气管[居中]，甲状腺[未触及肿大]，颈静脉[无怒张]。
胸部：[胸廓无畸形]，肋间隙[无增宽变窄]，乳房[双侧对称、未及肿块]。
肺部：呼吸运动[两侧对称]。叩诊[清音]，双肺闻及哮鸣音。
心脏：心率[87]次/分，律[齐]，心音[有力]，[未闻及病理性杂音]。
血管检查：周围血管征：阴性。
腹部：腹[平坦]，对称，无胃肠型和蠕动波，腹部[柔软]，无[压痛，反跳痛]，腹部[无包块]。肝
脾肾[未触及]。肾区[无叩击痛]。肠鸣音[4]次/分,移动性浊音[阴性]。
外生殖器：外生殖器[无异常]，见专科情况。
既往史
婚育史
家族史
生命体征
生命体征
肿}。
神经系统：肌张力无增高或降低，四肢肌力[V级]，双侧膝腱反射[++]，[双侧]Babinski征[阴性]。
其他：见专科检查
补充及专科情况
一般情况：[无]发绀，[无]鼻翼扇动，[无]端坐呼吸，气管[居中]，浅表颈静脉[无怒张]，肝颈静脉返流
征[阴性]，[无]皮疹结节，[无]皮下气肿，[无]浮肿，[无]皮下瘀点、瘀斑，[无]无杵状指（趾）；
胸部：胸廓[无畸形]，肋间隙[无增宽或缩窄]，局部[无殊]，胸壁浅表静脉[无]曲张，脊柱[无畸形]，呼
吸动度[对称]，[无]胸壁压痛；
肺部 视诊：[胸式]呼吸为主，呼吸频率[19]次/分，节律[规律]，呼吸运动[对称]，[无]呼吸困难；触
诊：语颤[对称]，[无]胸膜摩擦感，[无]皮下捻发感；叩诊：[清音]。
浊音 实音 鼓音
湿啰音 干啰音
肺下界(肋间)
锁骨中线
腋中线
右
6
8
左
6
8
肺下界移动范围：左{6}cm，右{6}cm
听诊：两肺[呼吸音粗]，可闻及哮鸣音，[无]呼气延长，语音传导[对称]，[无]胸膜摩擦音；
辅助检查：[本次暂缺。]
初步诊断：
1.支气管哮喘
2.脂肪肝 诊断医生：吴蓉 诊断时间：2025-05-26 09:41
---
临海市第一人民医院医共体
肺功能报告
COSMED
姓名:
科室/床号:
100004
ID:
日期:
2025/6/9
预计值:
ERS 93
出生日期: 1978/12/13
性别: Male
地区修正.: Chinese
详细描述:
Company:
年龄: 46
体重 (Kg): 84.0
身高 (cm): 178.0
BMI (Kg/m²): 26.5
吸烟: 否
用力肺活量 Forced Vital Capacity
F(l/s)
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
-1
-2
-3
-4
-5
-6
-7
-8
V(l)
8
7
6
5
4
3
2
1
0
-1
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
12t(s)
FVC
PEF
MEF75%
MEF50%
MEF25%
FVC
V(l)
8
7
6
5
4
3
2
1
0
-1
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
12t(s)
FEV1
ATS
FVC
PEF
MEF75%
MEF50%
MEF25%
FVC
V(l)
8
7
6
5
4
3
2
1
0
-1
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
12t(s)
Parameter
UM
Pred.
BEST#1
%Pred.
POST#3
%Pred.
%Test#1
Best FVC
l(btps)
4.72
2.74
58
3.22
68
+17.4
FVC
l(btps)
4.72
2.74
58
3.22
68
+17.4
FEV1
l(btps)
3.83
1.35
35
1.72
45
+27.5
PEF
l/sec
9.10
2.96
32
3.30
36
+11.4
FEV6
l(btps)
5.01
2.71
54
3.20
64
+18.2
PIF
l/sec
4.61
5.52
+19.9
FEV1/FVC%
%
78.9
49.1
62
53.4
68
+8.7
FEV6/FVC%
%
98.8
99.5
+0.7
FEV1/FEV6%
%
49.7
53.6
+7.9
FEF25-75%
l/sec
4.18
0.64
15
0.86
21
+34.7
MEF75%
l/sec
7.91
1.42
18
1.98
25
+39.2
MEF50%
l/sec
4.97
0.75
15
1.02
20
+36.2
MEF25%
l/sec
2.11
0.31
15
0.41
19
+32.4
FET100%
sec
6.2
6.1
-1.9
VEXT
ml
60
73
+21.7
IC
l(btps)
2.47
2.27
-8.1
诊断:
支气管舒张试验阳性。
签名:
2025-03-16
---
CT胸部薄扫
基本信息
就诊类型：住院
开单医生：吴蓉
报告医生：马之逸
审核医生：李莹
开单时间：2025-05-26 09:11:52
报告时间：2025-05-26 14:53:14
审核时间：2025-05-26 14:55:24
检查时间：2025-05-26 14:43:29
影像及诊断
影像所见：两侧胸廓对称，气管居中，两肺纹理增多，两肺少许条索影，界清，两上肺局部胸膜增厚；两肺见多发结节，其中最大者位于左肺下叶背段(Se2，Im124-128)，为实性结节，大小约为7×4mm，气管及分支走形自然，未见狭窄，两肺门及纵隔内未见明显肿大淋巴结影；心脏各房室无殊；冠脉壁钙化；两侧胸膜腔内未见积液征；所扫层面肋骨未见明显异常。
诊断意见：前片2025-1-17所示两肺炎症基本吸收。
两肺多发小结节，建议年度随诊。
两肺少许纤维灶，两上肺局部胸膜增厚；冠脉壁钙化。
气管内结节状突起，痰栓？建议复查。
附见：脂肪肝，胆囊结石。
2026-08-05 12:04:14,289 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-05 12:04:14,289 INFO     29 [Trace] task=aeebe394 | doc=哮喘-HJCH222   2.27.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "7 items, types={'OutpatientRecord': 3, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 2}", "name": "哮喘-HJCH222   2.27.pdf", "embedding_token_consumption": 7366}
2026-08-05 12:04:14,289 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-05 12:04:14,455 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-05 12:04:14,455 INFO     29 [Trace] task=aeebe394 | doc=哮喘-HJCH222   2.27.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":7,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-05 12:04:14,459 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:04:14,460 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:04:14,460 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:04:14,461 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:04:14,461 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:04:14,461 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:04:14,461 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:04:14,465 INFO     29 set_progress(aeebe39490be11f1a3da71efcdd7cc1f), progress: 0.82, progress_msg: 12:04:14 [DOC Engine]:
Start to index...
2026-08-05 12:04:14,482 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.010s]
2026-08-05 12:04:14,486 INFO     29 set_progress(aeebe39490be11f1a3da71efcdd7cc1f), progress: 0.8142857142857143, progress_msg: 
2026-08-05 12:04:14,502 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.009s]
2026-08-05 12:04:14,509 INFO     29 set_progress(aeebe39490be11f1a3da71efcdd7cc1f), progress: 1.0, progress_msg: 12:04:14 Indexing done (0.04s). Task done (1144.94s)
2026-08-05 12:04:14,512 INFO     29 [Done], chunks(7), token(7366), elapsed:1144.94
2026-08-05 12:04:14,692 INFO     29 handle_task done for task {"id": "aeebe39490be11f1a3da71efcdd7cc1f", "doc_id": "ae83c98a90be11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u54ee\u5598-HJCH222   2.27.pdf", "type": "pdf", "location": "\u54ee\u5598-HJCH222   2.27.pdf", "size": 16296401, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1785928407811, "task_type": "dataflow", "root_trace_id": "d72ca28b91c84f599f1151379b451f37", "root_traceparent": "00-d72ca28b91c84f599f1151379b451f37-5c87c8a5dc8089ce-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-05 12:04:15,065 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 12:04:15,065 INFO     29 [qwen-vl-text] LLM output (len=233):
{
  "encounter_date": "2024-12-10",
  "chief_complaint": "SSSJ项目肺功能检查开单",
  "present_illness": "哮喘",
  "past_history": "患者平素身体健康,高血压无,糖尿病无,心脏病无,肺结核无,鼻炎无,吸烟史无,无过敏史。",
  "diagnosis": "西医：1.哮喘 中医：",
  "treatment_plan": "呼吸过滤器 肺通气功能检查"
}
2026-08-05 12:04:15,066 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-12-10]
2026-08-05 12:04:15,091 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7824738, prompt_len=1111
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
2026-08-05 12:04:15,595 WARNING  29 [qwen-vl-text] coord API request failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
2026-08-05 12:04:15,595 WARNING  29 [qwen-vl-text] page=4 coord failed: request error: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response')), adding 24 placeholder(s)
2026-08-05 12:04:15,595 INFO     29 [qwen-vl-text] new_positions (24):
[[4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0], [4, 0, 0, 0, 0]]
2026-08-05 12:04:15,595 INFO     29 [qwen-vl-text] ═══ DONE ═══ 24 positions, pages=1, time=3.2s
2026-08-05 12:04:15,602 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-05 12:04:15,602 INFO     29 [Trace] task=b28be2ce | doc=麦济ZHYH.pdf | Extractor:Clinical | outputs={"chunks": "2 items, types={'OutpatientRecord': 2}", "html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-05 12:04:15,602 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-05 12:04:15,607 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 12:04:15,607 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 12:04:15,607 INFO     29 [qwen-vl-text] positions(25): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 12:04:15,608 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [25]
2026-08-05 12:04:15,892 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 12:04:15,893 INFO     29 [qwen-vl-text] LLM extraction start, text_len=183
2026-08-05 12:04:15,893 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 12:04:15,893 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 30, \"bbox_end\": 54, \"encounter_dates\": [\"2025-11-18\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "萱堂大药房\n单号：2025111853212\n日期：25/11/18\n时间：13:2\n工号：001\n品名\n规格\n厂家\n金额\n数量\n总计\n布地格福吸入气雾剂\n60ug/7.2ug/4.8ug 吸\n120 撤/支\n支/盒\n219.00\n3\n657.00\n合计：657.00\n应收：657.00\n数量：3\n实收：657.00\n会员：\n药品属于特殊商品\n无质量问题，概不退换",
    "role": "user"
  }
]
[92m12:04:15 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:04:15,894 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:04:16,980 INFO     29 [qwen-vl-parser] text API response (len=1479):
["入院日期:2026-01-04 09:19", "出院日期: 2026-01-14 18:33", "住院天数:10天", "入院情况:患者以“[反复咳痰喘6年余,再发10余天。]”为主诉入院。入院情", "况:[6年余来患者每遇吸入刺激性气味或冷空气后出现咳嗽、咳痰及胸闷、气喘,咳嗽咳", "痰症状呈阵发性发作,痰液易咳出,多为白粘痰,每次症状发作时多就诊于我院呼吸内", "科,曾完善肺功能检查确诊为“支气管哮喘”,经抗感染、抗炎、解痉平喘、雾化吸入及", "对症治疗后症状好转出院,出院后院外规律吸入“布地格福气雾剂2揿/次,一日两次”", "治疗,胸闷、气喘症状控制不佳,活动耐力呈进行性下降(以致目前上2层楼或步行500米", "左右即气喘严重),3月余前患者因受凉再次出现咳嗽、咳痰、胸闷、气喘,在家应用“布", "地格福气雾剂”吸入治疗及口服“罗红霉素胶囊7天及甲泼尼龙片8mg/次,一日两次,", "间隔1-2天每日减1片”治疗,咳嗽咳痰及胸闷、气喘症状有所好转后停用上述口服药物,", "后改为应用“布地奈德气雾剂2揿/次,一日三次联合乌美溴铵维兰特罗粉雾剂1吸/次,一", "日一次”联合维持治疗。10余天前患者无诱因再次出现咳嗽、咳痰、胸闷、气喘,不伴发", "热,在家应用“布地奈德气雾剂2揿/次,一日三次联合乌美溴铵维兰特罗粉雾剂1吸/次,", "一日一次”吸入治疗及再次口服“罗红霉素胶囊7天及甲泼尼龙片8mg/次,一日两次,", "间隔1-2天每日减1片”治疗10余天来咳嗽咳痰及胸闷、气喘症状未见好转,为求诊治故来", "我院就诊,门诊以“支气管哮喘”收治住院。患者神志清,精神差,饮食差,夜间睡眠", "差,大小便正常。[既往史:有“高血压病”病史10年,最高达160/80mmHg,目前服用降", "压药“奥美沙坦酯片20mg/次,一日一次”治疗,血压控制在120/60mmHg水平,否认过", "敏史。]入院查体:[T:36.1℃,P:84次/分,R:22次/分,BP:154/81mmHg,SPO2:93%,发", "育正常,营养中等,体型中等,神志清,精神差,颜面部轻度紫绀,喘息貌,自主体位,", "查体合作。全身皮肤粘膜未见皮疹及出血点。无肝掌及蜘蛛痣。全身浅表淋巴结均未触及", "肿大。双瞳孔等大等圆,直径为3mm,对光反射灵敏。口唇轻度紫绀,咽腔充血,双侧扁", "桃腺未见肿大及脓点。颈软,颈静脉充盈。双肺呼吸音粗,两肺均可闻及干啰音及呼气相", "哮鸣音。心率84次/分,律齐,心脏各瓣膜听诊区均未闻及病理性杂音。腹平软,全腹无", "压痛及反跳痛。肝脾肋下未触及。双下肢无浮肿。]", "入院诊断:1.支气管哮喘急性发作;2.慢性阻塞性肺疾病?3.高血压病2级低", "危组。", "诊疗经过:患者入院后积极完善检查,并予抗感染、扩张气管、雾化吸入、抗", "炎、解痉平喘及改善肺功能治疗", "出院诊断:1.支气管哮喘急性发作;2.革兰氏阴性细菌性肺炎;3.高血压病2", "级低危组。", "出院情况:患者神志清,精神较前明显好转,饮食可,近几日来无发热,咳嗽咳", "痰症状基本消失,胸闷、气喘症状较入院时明显减轻,咳嗽咳痰后胸闷、气喘症状亦较前", "明显减轻,未诉其他不适症状,大小便正常,夜间睡眠可,患者目前血常规示嗜酸性粒细", "胞数目已恢复至正常范围,肺功能明显改善,临床症状明显好转准予出院。", "出院医嘱:一、保持呼吸道通畅,规律应用布地奈德气雾剂联合乌美溴铵维兰特"]
2026-08-05 12:04:16,982 INFO     29 [qwen-vl-parser] page=14 text: 38 lines (bbox 377-414)
2026-08-05 12:04:16,982 INFO     29 [qwen-vl-parser] page=14 text: 38 sections
2026-08-05 12:04:17,472 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9188677, prompt_len=764
2026-08-05 12:04:18,492 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 12:04:18,492 INFO     29 [qwen-vl-text] LLM output (len=431):
{
  "encounter_date": "2025-11-18",
  "pharmacy": "萱堂大药房",
  "medications": [
    {
      "name": "布地格福吸入气雾剂",
      "specification": "60ug/7.2ug/4.8ug 吸 120撤/支",
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
2026-08-05 12:04:18,492 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-18]
2026-08-05 12:04:18,495 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1978583, prompt_len=871
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
2026-08-05 12:04:20,572 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 12:04:20,574 INFO     29 [qwen-vl-parser] page=15 classify=text report_date=None
2026-08-05 12:04:20,603 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9188677, prompt_len=401
2026-08-05 12:04:27,625 INFO     29 [qwen-vl-text] coord API raw response (len=1286):
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
	{"text": "支/盒", "bbox": [238, 568, 338, 601]},
	{"text": "219.00", "bbox": [214, 609, 327, 637]},
	{"text": "3", "bbox": [414, 612, 437, 638]},
	{"text": "657.00", "bbox": [545, 613, 664, 640]},
	{"text": "合计：657.00", "bbox": [214, 646, 460, 678]},
	{"text": "应收：657.00", "bbox": [214, 684, 460, 715]},
	{"text": "数量：3", "bbox": [214, 724, 361, 757]},
	{"text": "实收：657.00", "bbox": [214, 772, 462, 805]},
	{"text": "会员：", "bbox": [214, 823, 311, 855]},
	{"text": "药品属于特殊商品", "bbox": [217, 871, 555, 904]},
	{"text": "无质量问题，概不退换", "bbox": [219, 920, 642, 953]}
]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=9.1s
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[0]: text=萱堂大药房, bbox=[364, 153, 658, 199]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[1]: text=单号：2025111853212, bbox=[212, 248, 614, 288]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[2]: text=日期：25/11/18, bbox=[212, 297, 484, 335]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[3]: text=时间：13:2, bbox=[570, 305, 807, 338]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[4]: text=工号：001, bbox=[212, 348, 400, 382]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[5]: text=品名, bbox=[212, 398, 294, 430]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[6]: text=规格, bbox=[374, 403, 462, 435]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[7]: text=厂家, bbox=[542, 405, 628, 437]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[8]: text=金额, bbox=[732, 406, 810, 438]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[9]: text=数量, bbox=[212, 447, 292, 479]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[10]: text=总计, bbox=[382, 452, 468, 483]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[11]: text=布地格福吸入气雾剂, bbox=[212, 490, 810, 530]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[12]: text=60ug/7.2ug/4.8ug 吸, bbox=[224, 530, 590, 569]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[13]: text=120 撤/支, bbox=[642, 536, 810, 569]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[14]: text=支/盒, bbox=[238, 568, 338, 601]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[15]: text=219.00, bbox=[214, 609, 327, 637]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[16]: text=3, bbox=[414, 612, 437, 638]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[17]: text=657.00, bbox=[545, 613, 664, 640]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[18]: text=合计：657.00, bbox=[214, 646, 460, 678]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[19]: text=应收：657.00, bbox=[214, 684, 460, 715]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[20]: text=数量：3, bbox=[214, 724, 361, 757]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[21]: text=实收：657.00, bbox=[214, 772, 462, 805]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[22]: text=会员：, bbox=[214, 823, 311, 855]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[23]: text=药品属于特殊商品, bbox=[217, 871, 555, 904]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] coord item[24]: text=无质量问题，概不退换, bbox=[219, 920, 642, 953]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] page=1 — 25/25 coords, api_time=9.1s
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] new_positions (25):
[[1, 216.57999999999998, 391.51, 128.826, 167.558], [1, 126.14, 365.33, 208.816, 242.49599999999998], [1, 126.14, 287.97999999999996, 250.07399999999998, 282.07], [1, 339.15, 480.16499999999996, 256.81, 284.596], [1, 126.14, 238.0, 293.01599999999996, 321.644], [1, 126.14, 174.92999999999998, 335.116, 362.06], [1, 222.53, 274.89, 339.32599999999996, 366.27], [1, 322.49, 373.65999999999997, 341.01, 367.954], [1, 435.53999999999996, 481.95, 341.852, 368.796], [1, 126.14, 173.73999999999998, 376.37399999999997, 403.318], [1, 227.29, 278.46, 380.584, 406.686], [1, 126.14, 481.95, 412.58, 446.26], [1, 133.28, 351.05, 446.26, 479.09799999999996], [1, 381.99, 481.95, 451.312, 479.09799999999996], [1, 141.60999999999999, 201.10999999999999, 478.256, 506.042], [1, 127.33, 194.565, 512.778, 536.3539999999999], [1, 246.32999999999998, 260.015, 515.304, 537.196], [1, 324.275, 395.08, 516.146, 538.88], [1, 127.33, 273.7, 543.932, 570.876], [1, 127.33, 273.7, 575.928, 602.03], [1, 127.33, 214.795, 609.608, 637.394], [1, 127.33, 274.89, 650.024, 677.81], [1, 127.33, 185.045, 692.966, 719.91], [1, 129.11499999999998, 330.22499999999997, 733.382, 761.168], [1, 130.305, 381.99, 774.64, 802.4259999999999]]
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=12.0s
2026-08-05 12:04:27,626 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 12:04:27,626 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 12:04:27,627 INFO     29 [qwen-vl-text] positions(37): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 12:04:27,627 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [37]
2026-08-05 12:04:27,810 INFO     29 [qwen-vl-text] page=2, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 12:04:27,811 INFO     29 [qwen-vl-text] LLM extraction start, text_len=327
2026-08-05 12:04:27,811 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 12:04:27,811 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 55, \"bbox_end\": 91, \"encounter_dates\": [\"2025-08-20\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "电子发票(普通发票)\n国家税务总局\n江苏省税务局\n发票号码：25322000000382591347\n开票日期：2025年08月20日\n购买方信息\n名称：\n统一社会信用代码/纳税人识别号：\n销售方信息\n名称：无锡邻医大药房有限公司\n统一社会信用代码/纳税人识别号：91320214MA228F680W\n项目名称\n规格型号\n单位\n数量\n单价\n金额\n税率/征收率\n税额\n*化学药品制剂*倍择瑞令\n160μg/7.2μg/4\n盒\n3\n210.029498522124\n630.09\n13%\n81.91\n畅布地格福吸入气雾剂\n.8μg*120揿\n合计\n￥630.09\n￥81.91\n价税合计（大写）\n柒佰壹拾贰圆整\n(小写) ￥712.00\n备注\n开票人：奚澳琼",
    "role": "user"
  }
]
[92m12:04:27 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:04:27,812 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:04:27,814 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T12:04:27.812+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 8, "lag": 0, "done": 18, "failed": 0, "current": {"b28be2ce90be11f1a3da71efcdd7cc1f": {"id": "b28be2ce90be11f1a3da71efcdd7cc1f", "doc_id": "b2448c9e90be11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHYH.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHYH.pdf", "size": 10529265, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785928413891, "task_type": "dataflow", "root_trace_id": "e3dcb8801128457d8d83b73c11855569", "root_traceparent": "00-e3dcb8801128457d8d83b73c11855569-a468dda7915c610d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "3e98f84c90bf11f1a3da71efcdd7cc1f": {"id": "3e98f84c90bf11f1a3da71efcdd7cc1f", "doc_id": "3543a40e90bf11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "XALI\u9ea6\u6d4e\u65b0\u4e61 2026-03-06 17.04 (1).pdf", "type": "pdf", "location": "XALI\u9ea6\u6d4e\u65b0\u4e61 2026-03-06 17.04 (1).pdf", "size": 161316076, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785928648860, "task_type": "dataflow", "root_trace_id": "011798f1ac614ad79dfcf6d230b3fd04", "root_traceparent": "00-011798f1ac614ad79dfcf6d230b3fd04-a0d937a531746558-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 12:04:28,982 INFO     29 [qwen-vl-parser] text API response (len=1053):
["一曰一次”吸入治疗及再次口服“罗红霉素胶囊7天及甲泼尼龙片8mg/次，一日两次，", "间隔1-2天每日减1片”治疗10余天来咳嗽咳痰及胸闷、气喘症状未见好转，为求诊治故来", "我院就诊，门诊以“支气管哮喘”收治住院。患者神志清，精神差，饮食差，夜间睡眠", "差，大小便正常。][既往史：有“高血压病”病史10年，最高达160/80mmHg，目前服用降", "压药“奥美沙坦酯片20mg/次，一日一次”治疗，血压控制在120/60mmHg水平，否认过", "敏史。]入院查体：[T:36.1℃，P:84次/分，R:22次/分，BP:154/81mmHg，SPO2:93%，发", "育正常，营养中等，体型中等，神志清，精神差，颜面部轻度紫绀，喘息貌，自主体位，", "查体合作。全身皮肤粘膜未见皮疹及出血点。无肝掌及蜘蛛痣。全身浅表淋巴结均未触及", "肿大。双瞳孔等大等圆，直径为3mm，对光反射灵敏。口唇轻度紫绀，咽腔充血，双侧扁", "桃腺未见肿大及脓点。颈软，颈静脉充盈。双肺呼吸音粗，两肺均可闻及干啰音及呼气相", "哮鸣音。心率84次/分，律齐，心脏各瓣膜听诊区均未闻及病理性杂音。腹平软，全腹无", "压痛及反跳痛。肝脾肋下未触及。双下肢无浮肿。]", "入院诊断：1.支气管哮喘急性发作；2.慢性阻塞性肺疾病？3.高血压病2级低", "危组。", "诊疗经过：患者入院后积极完善检查，并予抗感染、扩张气管、雾化吸入、抗", "炎、解痉平喘及改善肺功能治疗", "出院诊断：1.支气管哮喘急性发作；2.革兰氏阴性细菌性肺炎；3.高血压病2", "级低危组。", "出院情况：患者神志清，精神较前明显好转，饮食可，近几日来无发热，咳嗽咳", "痰症状基本消失，胸闷、气喘症状较入院时明显减轻，咳嗽咳痰后胸闷、气喘症状亦较前", "明显减轻，未诉其他不适症状，大小便正常，夜间睡眠可，患者目前血常规示嗜酸性粒细", "胞数目已恢复至正常范围，肺功能明显改善，临床症状明显好转准予出院。", "出院医嘱：一、保持呼吸道通畅，规律应用布地奈德气雾剂联合乌美溴铵维兰特", "罗吸入粉雾剂吸入治疗；", "二、适当运动，低盐饮食，避免受京、劳累及接触易导致哮", "喘发作的过敏物质，规律应用降压药物控制血压；", "三、定期复查胸部CT及肺功能，不适随诊。", "滨", "主管医师", "主任医师", "副主任医师签名", "注：出院记录一式两份，一份存病历，一份交患者。", "第2页"]
2026-08-05 12:04:28,986 INFO     29 [qwen-vl-parser] page=15 text: 33 lines (bbox 415-447)
2026-08-05 12:04:28,986 INFO     29 [qwen-vl-parser] page=15 text: 33 sections
2026-08-05 12:04:29,474 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9030352, prompt_len=764
2026-08-05 12:04:30,588 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 12:04:30,588 INFO     29 [qwen-vl-text] LLM output (len=448):
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
  "payment_total": 712.0,
  "payment_method": null
}
2026-08-05 12:04:30,588 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-08-20]
2026-08-05 12:04:30,590 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=931127, prompt_len=1051
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
2026-08-05 12:04:32,716 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 12:04:32,719 INFO     29 [qwen-vl-parser] page=16 classify=text report_date=None
2026-08-05 12:04:32,753 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9030352, prompt_len=401
2026-08-05 12:04:36,605 INFO     29 [qwen-vl-parser] text API response (len=365):
["出院证", "住院号：26000328", "医疗保障证号：医保号", "姓名", "性别：女", "年龄：67岁", "籍贯：河南省新乡市", "住址：河南省新乡", "入院日期：2026-01-04 09:19", "出院日期：2026-01-14 18:33", "出院诊断：1.支气管哮喘急性发作；2.革兰氏阴性细菌性肺炎；3.高血压病2级 低危", "组。", "出院医嘱：一、保持呼吸道通畅，规律应用布地奈德气雾剂联合乌美溴铵维兰特罗吸入", "粉雾剂吸入治疗；", "二、适当运动，低盐饮食，避免受凉、劳累及接触易导致哮喘发", "作的过敏物质，规律应用降压药物控制血压；", "三、定期复查胸部CT及肺功能，不适随诊。", "呼吸与危重症医学一科医师签名：", "盖章2026-01-14", "第 1 页"]
2026-08-05 12:04:36,608 INFO     29 [qwen-vl-parser] page=16 text: 20 lines (bbox 448-467)
2026-08-05 12:04:36,608 INFO     29 [qwen-vl-parser] page=16 text: 20 sections
2026-08-05 12:04:37,130 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8217552, prompt_len=764
2026-08-05 12:04:39,536 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-01-14"}
```
2026-08-05 12:04:39,539 INFO     29 [qwen-vl-parser] page=17 classify=text report_date=2026-01-14
2026-08-05 12:04:39,569 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8217552, prompt_len=401
2026-08-05 12:04:42,804 INFO     29 [qwen-vl-parser] text API response (len=314):
["诊断证明书", "门诊号：", "住院号：26000328", "姓名：", "性别：女", "年龄：67岁", "科室：呼吸与危重症医学一科", "诊断意见：1.支气管哮喘急性发作；2.革兰氏阴性细菌性肺炎；3.高血压病2级 低危", "组。", "治疗经过及处理意见：", "患者以“反复咳痰喘6年余,再发10余天。”为主诉入院，患者入院后积极完善检查，并", "予抗感染、扩张气管、雾化吸入、抗炎、解痉平喘及改善肺功能治疗，患者目前血常规", "示嗜酸性粒细胞数目已恢复至正常范围，肺功能明显改善，临床症状明显好转准予出", "院。", "医师：", "2026-01-14", "(未盖章无效)", "第 1 页"]
2026-08-05 12:04:42,807 INFO     29 [qwen-vl-parser] page=17 text: 18 lines (bbox 468-485)
2026-08-05 12:04:42,807 INFO     29 [qwen-vl-parser] page=17 text: 18 sections
2026-08-05 12:04:43,396 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7029128, prompt_len=764
2026-08-05 12:04:45,262 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 12:04:45,263 INFO     29 [qwen-vl-parser] page=18 classify=text report_date=None
2026-08-05 12:04:45,286 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7029128, prompt_len=401
2026-08-05 12:04:51,995 INFO     29 [qwen-vl-text] coord API raw response (len=3203):
[
	{"text": "电子发票(普通发票)", "bbox": [327, 103, 637, 148]},
	{"text": "国家税务总局", "bbox": [463, 155, 534, 172], "bbox_2d": [463, 155, 534, 172]},
	{"text": "江苏省税务局", "bbox": [463, 187, 537, 210], "bbox_2d": [463, 187, 537, 210]},
	{"text": "发票号码：25322000000382591347", "bbox": [733, 122, 948, 143], "bbox_2d": [733, 122, 948, 143]},
	{"text": "开票日期：2025年08月20日", "bbox": [733, 161, 909, 182], "bbox_2d": [733, 161, 909, 182]},
	{"text": "购买方信息", "bbox": [32, 265, 46, 380], "bbox_2d": [32, 265, 46, 380]},
	{"text": "名称：", "bbox": [59, 282, 194, 302], "bbox_2d": [59, 282, 194, 302]},
	{"text": "统一社会信用代码/纳税人识别号：", "bbox": [58, 346, 258, 366], "bbox_2d": [58, 346, 258, 366]},
	{"text": "销售方信息", "bbox": [507, 265, 521, 380], "bbox_2d": [507, 265, 521, 380]},
	{"text": "名称：无锡邻医大药房有限公司", "bbox": [536, 277, 740, 298], "bbox_2d": [536, 277, 740, 298]},
	{"text": "统一社会信用代码/纳税人识别号：91320214MA228F680W", "bbox": [535, 341, 954, 363], "bbox_2d": [535, 341, 954, 363]},
	{"text": "项目名称", "bbox": [77, 402, 136, 421], "bbox_2d": [77, 402, 136, 421]},
	{"text": "规格型号", "bbox": [199, 402, 258, 421], "bbox_2d": [199, 402, 258, 421]},
	{"text": "单位", "bbox": [319, 402, 363, 421], "bbox_2d": [319, 402, 363, 421]},
	{"text": "数量", "bbox": [442, 402, 487, 421], "bbox_2d": [442, 402, 487, 421]},
	{"text": "单价", "bbox": [558, 402, 602, 421], "bbox_2d": [558, 402, 602, 421]},
	{"text": "金额", "bbox": [680, 402, 724, 421], "bbox_2d": [680, 402, 724, 421]},
	{"text": "税率/征收率", "bbox": [744, 402, 826, 421], "bbox_2d": [744, 402, 826, 421]},
	{"text": "税额", "bbox": [923, 402, 968, 421], "bbox_2d": [923, 402, 968, 421]},
	{"text": "*化学药品制剂*倍择瑞令", "bbox": [26, 427, 187, 449], "bbox_2d": [26, 427, 187, 449]},
	{"text": "160μg/7.2μg/4", "bbox": [200, 428, 301, 451], "bbox_2d": [200, 428, 301, 451]},
	{"text": "盒", "bbox": [333, 428, 349, 449], "bbox_2d": [333, 428, 349, 449]},
	{"text": "3", "bbox": [477, 428, 487, 449], "bbox_2d": [477, 428, 487, 449]},
	{"text": "210.029498522124", "bbox": [493, 428, 602, 449], "bbox_2d": [493, 428, 602, 449]},
	{"text": "630.09", "bbox": [684, 428, 722, 449], "bbox_2d": [684, 428, 722, 449]},
	{"text": "13%", "bbox": [778, 428, 803, 449], "bbox_2d": [778, 428, 803, 449]},
	{"text": "81.91", "bbox": [937, 428, 968, 449], "bbox_2d": [937, 428, 968, 449]},
	{"text": "畅布地格福吸入气雾剂", "bbox": [26, 457, 178, 479], "bbox_2d": [26, 457, 178, 479]},
	{"text": ".8μg*120揿", "bbox": [200, 457, 280, 481], "bbox_2d": [200, 457, 280, 481]},
	{"text": "合计", "bbox": [101, 673, 114, 692], "bbox_2d": [101, 673, 114, 692]},
	{"text": "计", "bbox": [174, 673, 188, 692], "bbox_2d": [174, 673, 188, 692]},
	{"text": "￥630.09", "bbox": [672, 670, 722, 689], "bbox_2d": [672, 670, 722, 689]},
	{"text": "￥81.91", "bbox": [925, 670, 968, 689], "bbox_2d": [925, 670, 968, 689]},
	{"text": "价税合计（大写）", "bbox": [84, 715, 194, 735], "bbox_2d": [84, 715, 194, 735]},
	{"text": "柒佰壹拾贰圆整", "bbox": [301, 711, 408, 733], "bbox_2d": [301, 711, 408, 733]},
	{"text": "(小写) ￥712.00", "bbox": [690, 710, 811, 733], "bbox_2d": [690, 710, 811, 733]},
	{"text": "备注", "bbox": [32, 787, 46, 844], "bbox_2d": [32, 787, 46, 844]},
	{"text": "开票人：奚澳琼", "bbox": [95, 917, 200, 938], "bbox_2d": [95, 917, 200, 938]}
]
2026-08-05 12:04:51,995 INFO     29 [qwen-vl-text] coord API: raw_items=38, valid_items=38, elapsed=21.4s
2026-08-05 12:04:51,995 INFO     29 [qwen-vl-text] coord item[0]: text=电子发票(普通发票), bbox=[327, 103, 637, 148]
2026-08-05 12:04:51,995 INFO     29 [qwen-vl-text] coord item[1]: text=国家税务总局, bbox=[463, 155, 534, 172]
2026-08-05 12:04:51,995 INFO     29 [qwen-vl-text] coord item[2]: text=江苏省税务局, bbox=[463, 187, 537, 210]
2026-08-05 12:04:51,995 INFO     29 [qwen-vl-text] coord item[3]: text=发票号码：25322000000382591347, bbox=[733, 122, 948, 143]
2026-08-05 12:04:51,995 INFO     29 [qwen-vl-text] coord item[4]: text=开票日期：2025年08月20日, bbox=[733, 161, 909, 182]
2026-08-05 12:04:51,995 INFO     29 [qwen-vl-text] coord item[5]: text=购买方信息, bbox=[32, 265, 46, 380]
2026-08-05 12:04:51,995 INFO     29 [qwen-vl-text] coord item[6]: text=名称：, bbox=[59, 282, 194, 302]
2026-08-05 12:04:51,995 INFO     29 [qwen-vl-text] coord item[7]: text=统一社会信用代码/纳税人识别号：, bbox=[58, 346, 258, 366]
2026-08-05 12:04:51,995 INFO     29 [qwen-vl-text] coord item[8]: text=销售方信息, bbox=[507, 265, 521, 380]
2026-08-05 12:04:51,995 INFO     29 [qwen-vl-text] coord item[9]: text=名称：无锡邻医大药房有限公司, bbox=[536, 277, 740, 298]
2026-08-05 12:04:51,995 INFO     29 [qwen-vl-text] coord item[10]: text=统一社会信用代码/纳税人识别号：91320214MA228F680W, bbox=[535, 341, 954, 363]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[11]: text=项目名称, bbox=[77, 402, 136, 421]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[12]: text=规格型号, bbox=[199, 402, 258, 421]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[13]: text=单位, bbox=[319, 402, 363, 421]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[14]: text=数量, bbox=[442, 402, 487, 421]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[15]: text=单价, bbox=[558, 402, 602, 421]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[16]: text=金额, bbox=[680, 402, 724, 421]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[17]: text=税率/征收率, bbox=[744, 402, 826, 421]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[18]: text=税额, bbox=[923, 402, 968, 421]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[19]: text=*化学药品制剂*倍择瑞令, bbox=[26, 427, 187, 449]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[20]: text=160μg/7.2μg/4, bbox=[200, 428, 301, 451]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[21]: text=盒, bbox=[333, 428, 349, 449]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[22]: text=3, bbox=[477, 428, 487, 449]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[23]: text=210.029498522124, bbox=[493, 428, 602, 449]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[24]: text=630.09, bbox=[684, 428, 722, 449]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[25]: text=13%, bbox=[778, 428, 803, 449]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[26]: text=81.91, bbox=[937, 428, 968, 449]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[27]: text=畅布地格福吸入气雾剂, bbox=[26, 457, 178, 479]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[28]: text=.8μg*120揿, bbox=[200, 457, 280, 481]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[29]: text=合计, bbox=[101, 673, 114, 692]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[30]: text=计, bbox=[174, 673, 188, 692]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[31]: text=￥630.09, bbox=[672, 670, 722, 689]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[32]: text=￥81.91, bbox=[925, 670, 968, 689]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[33]: text=价税合计（大写）, bbox=[84, 715, 194, 735]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[34]: text=柒佰壹拾贰圆整, bbox=[301, 711, 408, 733]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[35]: text=(小写) ￥712.00, bbox=[690, 710, 811, 733]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[36]: text=备注, bbox=[32, 787, 46, 844]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] coord item[37]: text=开票人：奚澳琼, bbox=[95, 917, 200, 938]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] page=2 — 37/37 coords, api_time=21.4s
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] new_positions (37):
[[2, 275.334, 536.3539999999999, 61.285, 88.06], [2, 389.846, 449.628, 92.225, 102.33999999999999], [2, 389.846, 452.154, 111.265, 124.94999999999999], [2, 617.1859999999999, 798.216, 72.59, 85.085], [2, 617.1859999999999, 765.3779999999999, 95.795, 108.28999999999999], [2, 26.944, 38.732, 157.67499999999998, 226.1], [2, 49.678, 163.34799999999998, 167.79, 179.69], [2, 48.836, 217.236, 205.87, 217.76999999999998], [2, 426.894, 438.68199999999996, 157.67499999999998, 226.1], [2, 451.312, 623.0799999999999, 164.815, 177.31], [2, 450.46999999999997, 803.2679999999999, 202.89499999999998, 215.98499999999999], [2, 64.834, 114.512, 239.19, 250.49499999999998], [2, 167.558, 217.236, 239.19, 250.49499999999998], [2, 268.598, 305.646, 239.19, 250.49499999999998], [2, 372.164, 410.054, 239.19, 250.49499999999998], [2, 469.83599999999996, 506.88399999999996, 239.19, 250.49499999999998], [2, 572.56, 609.608, 239.19, 250.49499999999998], [2, 626.448, 695.492, 239.19, 250.49499999999998], [2, 777.1659999999999, 815.0559999999999, 239.19, 250.49499999999998], [2, 21.892, 157.454, 254.065, 267.155], [2, 168.4, 253.44199999999998, 254.66, 268.34499999999997], [2, 280.38599999999997, 293.858, 254.66, 267.155], [2, 401.63399999999996, 410.054, 254.66, 267.155], [2, 415.106, 506.88399999999996, 254.66, 267.155], [2, 575.928, 607.924, 254.66, 267.155], [2, 655.076, 676.126, 254.66, 267.155], [2, 788.954, 815.0559999999999, 254.66, 267.155], [2, 21.892, 149.876, 271.91499999999996, 285.005], [2, 168.4, 235.76, 271.91499999999996, 286.195], [2, 85.042, 95.988, 400.435, 411.74], [2, 146.50799999999998, 158.296, 400.435, 411.74], [2, 565.824, 607.924, 398.65, 409.955], [2, 778.85, 815.0559999999999, 398.65, 409.955], [2, 70.728, 163.34799999999998, 425.42499999999995, 437.325], [2, 253.44199999999998, 343.536, 423.04499999999996, 436.135], [2, 580.98, 682.862, 422.45, 436.135], [2, 26.944, 38.732, 468.265, 502.17999999999995]]
2026-08-05 12:04:51,996 INFO     29 [qwen-vl-text] ═══ DONE ═══ 37 positions, pages=1, time=24.4s
2026-08-05 12:04:51,996 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 12:04:51,997 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 12:04:51,997 INFO     29 [qwen-vl-text] positions(36): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 12:04:51,997 INFO     29 [qwen-vl-text] page grouping: [3, 4], lines per page: [35, 1]
2026-08-05 12:04:52,171 INFO     29 [qwen-vl-text] page=3, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 12:04:52,731 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 12:04:52,732 INFO     29 [qwen-vl-text] LLM extraction start, text_len=372
2026-08-05 12:04:52,732 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 12:04:52,732 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 92, \"bbox_end\": 127, \"encounter_dates\": [\"2025-05-20\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "电子发票(普通发票)\n国家税务总局\n江苏省税务局\n发票号码：25322000000226700883\n开票日期：2025年05月20日\n购买方信息\n名称\n统一社会信用代码/纳税人识别号：\n销售方信息\n名称：无锡邻医大药房有限公司\n统一社会信用代码/纳税人识别号：91320214MA228F680W\n项目名称\n规格型号\n单位\n数量\n单价\n金额\n税率/征收率\n税额\n*化学药品制剂*倍择瑞令\n160μg/7.2μg/4\n盒\n3 210.029498522124\n630.09\n13%\n81.91\n畅布地格福吸入气雾剂\n.8μg*120揿\n合计\n￥630.09\n￥81.91\n价税合计（大写）\n柒佰壹拾贰圆整\n(小写）￥712.00\n备注\n挂号号:D20091... 医保余额:0 CM/KG 普通病人|现住址:内蒙古土默特左旗沙尔营乡大有庄村32",
    "role": "user"
  }
]
[92m12:04:52 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:04:52,734 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:04:55,999 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 12:04:55,999 INFO     29 [qwen-vl-text] LLM output (len=439):
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
2026-08-05 12:04:55,999 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-05-20]
2026-08-05 12:04:56,003 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=847478, prompt_len=1035
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
2026-08-05 12:05:16,208 INFO     29 [qwen-vl-text] coord API raw response (len=3084):
```json
[
	{"text": "电子发票(普通发票)", "bbox": [328, 123, 635, 168], "bbox_2d": [328, 123, 635, 168]},
	{"text": "国家税务总局", "bbox": [463, 175, 534, 192], "bbox_2d": [463, 175, 534, 192]},
	{"text": "江苏省税务局", "bbox": [463, 206, 537, 232], "bbox_2d": [463, 206, 537, 232]},
	{"text": "发票号码：25322000000226700883", "bbox": [731, 143, 944, 164], "bbox_2d": [731, 143, 944, 164]},
	{"text": "开票日期：2025年05月20日", "bbox": [731, 181, 905, 202], "bbox_2d": [731, 181, 905, 202]},
	{"text": "购买方信息", "bbox": [36, 284, 50, 398], "bbox_2d": [36, 284, 50, 398]},
	{"text": "名称", "bbox": [62, 302, 89, 321], "bbox_2d": [62, 302, 89, 321]},
	{"text": "统一社会信用代码/纳税人识别号：", "bbox": [61, 365, 259, 384], "bbox_2d": [61, 365, 259, 384]},
	{"text": "销售方信息", "bbox": [507, 284, 520, 398], "bbox_2d": [507, 284, 520, 398]},
	{"text": "名称：无锡邻医大药房有限公司", "bbox": [535, 296, 738, 317], "bbox_2d": [535, 296, 738, 317]},
	{"text": "统一社会信用代码/纳税人识别号：91320214MA228F680W", "bbox": [534, 360, 950, 382], "bbox_2d": [534, 360, 950, 382]},
	{"text": "项目名称", "bbox": [80, 420, 139, 440], "bbox_2d": [80, 420, 139, 440]},
	{"text": "规格型号", "bbox": [201, 420, 260, 440], "bbox_2d": [201, 420, 260, 440]},
	{"text": "单位", "bbox": [320, 420, 364, 440], "bbox_2d": [320, 420, 364, 440]},
	{"text": "数量", "bbox": [442, 420, 486, 440], "bbox_2d": [442, 420, 486, 440]},
	{"text": "单价", "bbox": [557, 420, 600, 440], "bbox_2d": [557, 420, 600, 440]},
	{"text": "金额", "bbox": [678, 420, 721, 440], "bbox_2d": [678, 420, 721, 440]},
	{"text": "税率/征收率", "bbox": [742, 420, 823, 440], "bbox_2d": [742, 420, 823, 440]},
	{"text": "税额", "bbox": [920, 420, 964, 440], "bbox_2d": [920, 420, 964, 440]},
	{"text": "*化学药品制剂*倍择瑞令", "bbox": [30, 445, 190, 467], "bbox_2d": [30, 445, 190, 467]},
	{"text": "160μg/7.2μg/4", "bbox": [203, 447, 303, 470], "bbox_2d": [203, 447, 303, 470]},
	{"text": "盒", "bbox": [334, 447, 350, 467], "bbox_2d": [334, 447, 350, 467]},
	{"text": "3 210.029498522124", "bbox": [477, 447, 601, 467], "bbox_2d": [477, 447, 601, 467]},
	{"text": "630.09", "bbox": [682, 447, 720, 467], "bbox_2d": [682, 447, 720, 467]},
	{"text": "13%", "bbox": [775, 447, 800, 467], "bbox_2d": [775, 447, 800, 467]},
	{"text": "81.91", "bbox": [933, 447, 964, 467], "bbox_2d": [933, 447, 964, 467]},
	{"text": "畅布地格福吸入气雾剂", "bbox": [30, 475, 180, 497], "bbox_2d": [30, 475, 180, 497]},
	{"text": ".8μg*120揿", "bbox": [203, 475, 281, 499], "bbox_2d": [203, 475, 281, 499]},
	{"text": "合计", "bbox": [104, 688, 117, 707], "bbox_2d": [104, 688, 117, 707]},
	{"text": "计", "bbox": [177, 688, 190, 707], "bbox_2d": [177, 688, 190, 707]},
	{"text": "￥630.09", "bbox": [676, 687, 720, 704], "bbox_2d": [676, 687, 720, 704]},
	{"text": "￥81.91", "bbox": [926, 687, 964, 704], "bbox_2d": [926, 687, 964, 704]},
	{"text": "价税合计（大写）", "bbox": [87, 730, 196, 750], "bbox_2d": [87, 730, 196, 750]},
	{"text": "柒佰壹拾贰圆整", "bbox": [303, 725, 408, 747], "bbox_2d": [303, 725, 408, 747]},
	{"text": "(小写）￥712.00", "bbox": [688, 725, 808, 747], "bbox_2d": [688, 725, 808, 747]},
	{"text": "备注", "bbox": [36, 800, 50, 859], "bbox_2d": [36, 800, 50, 859]}
]
```
2026-08-05 12:05:16,208 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=20.2s
2026-08-05 12:05:16,209 INFO     29 [qwen-vl-text] coord item[0]: text=电子发票(普通发票), bbox=[328, 123, 635, 168]
2026-08-05 12:05:16,209 INFO     29 [qwen-vl-text] coord item[1]: text=国家税务总局, bbox=[463, 175, 534, 192]
2026-08-05 12:05:16,209 INFO     29 [qwen-vl-text] coord item[2]: text=江苏省税务局, bbox=[463, 206, 537, 232]
2026-08-05 12:05:16,210 INFO     29 [qwen-vl-text] coord item[3]: text=发票号码：25322000000226700883, bbox=[731, 143, 944, 164]
2026-08-05 12:05:16,210 INFO     29 [qwen-vl-text] coord item[4]: text=开票日期：2025年05月20日, bbox=[731, 181, 905, 202]
2026-08-05 12:05:16,210 INFO     29 [qwen-vl-text] coord item[5]: text=购买方信息, bbox=[36, 284, 50, 398]
2026-08-05 12:05:16,210 INFO     29 [qwen-vl-text] coord item[6]: text=名称, bbox=[62, 302, 89, 321]
2026-08-05 12:05:16,210 INFO     29 [qwen-vl-text] coord item[7]: text=统一社会信用代码/纳税人识别号：, bbox=[61, 365, 259, 384]
2026-08-05 12:05:16,210 INFO     29 [qwen-vl-text] coord item[8]: text=销售方信息, bbox=[507, 284, 520, 398]
2026-08-05 12:05:16,210 INFO     29 [qwen-vl-text] coord item[9]: text=名称：无锡邻医大药房有限公司, bbox=[535, 296, 738, 317]
2026-08-05 12:05:16,210 INFO     29 [qwen-vl-text] coord item[10]: text=统一社会信用代码/纳税人识别号：91320214MA228F680W, bbox=[534, 360, 950, 382]
2026-08-05 12:05:16,210 INFO     29 [qwen-vl-text] coord item[11]: text=项目名称, bbox=[80, 420, 139, 440]
2026-08-05 12:05:16,210 INFO     29 [qwen-vl-text] coord item[12]: text=规格型号, bbox=[201, 420, 260, 440]
2026-08-05 12:05:16,210 INFO     29 [qwen-vl-text] coord item[13]: text=单位, bbox=[320, 420, 364, 440]
2026-08-05 12:05:16,210 INFO     29 [qwen-vl-text] coord item[14]: text=数量, bbox=[442, 420, 486, 440]
2026-08-05 12:05:16,211 INFO     29 [qwen-vl-text] coord item[15]: text=单价, bbox=[557, 420, 600, 440]
2026-08-05 12:05:16,211 INFO     29 [qwen-vl-text] coord item[16]: text=金额, bbox=[678, 420, 721, 440]
2026-08-05 12:05:16,211 INFO     29 [qwen-vl-text] coord item[17]: text=税率/征收率, bbox=[742, 420, 823, 440]
2026-08-05 12:05:16,211 INFO     29 [qwen-vl-text] coord item[18]: text=税额, bbox=[920, 420, 964, 440]
2026-08-05 12:05:16,211 INFO     29 [qwen-vl-text] coord item[19]: text=*化学药品制剂*倍择瑞令, bbox=[30, 445, 190, 467]
2026-08-05 12:05:16,211 INFO     29 [qwen-vl-text] coord item[20]: text=160μg/7.2μg/4, bbox=[203, 447, 303, 470]
2026-08-05 12:05:16,211 INFO     29 [qwen-vl-text] coord item[21]: text=盒, bbox=[334, 447, 350, 467]
2026-08-05 12:05:16,211 INFO     29 [qwen-vl-text] coord item[22]: text=3 210.029498522124, bbox=[477, 447, 601, 467]
2026-08-05 12:05:16,211 INFO     29 [qwen-vl-text] coord item[23]: text=630.09, bbox=[682, 447, 720, 467]
2026-08-05 12:05:16,211 INFO     29 [qwen-vl-text] coord item[24]: text=13%, bbox=[775, 447, 800, 467]
2026-08-05 12:05:16,211 INFO     29 [qwen-vl-text] coord item[25]: text=81.91, bbox=[933, 447, 964, 467]
2026-08-05 12:05:16,211 INFO     29 [qwen-vl-text] coord item[26]: text=畅布地格福吸入气雾剂, bbox=[30, 475, 180, 497]
2026-08-05 12:05:16,211 INFO     29 [qwen-vl-text] coord item[27]: text=.8μg*120揿, bbox=[203, 475, 281, 499]
2026-08-05 12:05:16,211 INFO     29 [qwen-vl-text] coord item[28]: text=合计, bbox=[104, 688, 117, 707]
2026-08-05 12:05:16,211 INFO     29 [qwen-vl-text] coord item[29]: text=计, bbox=[177, 688, 190, 707]
2026-08-05 12:05:16,211 INFO     29 [qwen-vl-text] coord item[30]: text=￥630.09, bbox=[676, 687, 720, 704]
2026-08-05 12:05:16,211 INFO     29 [qwen-vl-text] coord item[31]: text=￥81.91, bbox=[926, 687, 964, 704]
2026-08-05 12:05:16,211 INFO     29 [qwen-vl-text] coord item[32]: text=价税合计（大写）, bbox=[87, 730, 196, 750]
2026-08-05 12:05:16,211 INFO     29 [qwen-vl-text] coord item[33]: text=柒佰壹拾贰圆整, bbox=[303, 725, 408, 747]
2026-08-05 12:05:16,211 INFO     29 [qwen-vl-text] coord item[34]: text=(小写）￥712.00, bbox=[688, 725, 808, 747]
2026-08-05 12:05:16,211 INFO     29 [qwen-vl-text] coord item[35]: text=备注, bbox=[36, 800, 50, 859]
2026-08-05 12:05:16,212 INFO     29 [qwen-vl-text] page=3 — 35/35 coords, api_time=20.2s
2026-08-05 12:05:16,238 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7824738, prompt_len=669
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
2026-08-05 12:05:19,935 INFO     29 [qwen-vl-text] coord API raw response (len=97):
[
	{"text": "挂号号:D20091... 医保余额:0 CM/KG 普通病人|现住址:内蒙古土默特左旗沙尔营乡大有庄村32", "bbox": [0, 48, 999, 94]}
]
2026-08-05 12:05:19,935 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=3.7s
2026-08-05 12:05:19,935 INFO     29 [qwen-vl-text] coord item[0]: text=挂号号:D20091... 医保余额:0 CM/KG 普通病人|现住址:内蒙古土默特左旗沙尔营乡大有庄村32, bbox=[0, 48, 999, 94]
2026-08-05 12:05:19,938 INFO     29 [qwen-vl-text] page=4 — 1/1 coords, api_time=3.7s
2026-08-05 12:05:19,939 INFO     29 [qwen-vl-text] new_positions (36):
[[3, 276.176, 534.67, 73.185, 99.96], [3, 389.846, 449.628, 104.125, 114.24], [3, 389.846, 452.154, 122.57, 138.04], [3, 615.502, 794.848, 85.085, 97.58], [3, 615.502, 762.01, 107.695, 120.19], [3, 30.311999999999998, 42.1, 168.98, 236.81], [3, 52.204, 74.938, 179.69, 190.995], [3, 51.361999999999995, 218.078, 217.17499999999998, 228.48], [3, 426.894, 437.84, 168.98, 236.81], [3, 450.46999999999997, 621.396, 176.12, 188.61499999999998], [3, 449.628, 799.9, 214.2, 227.29], [3, 67.36, 117.038, 249.89999999999998, 261.8], [3, 169.242, 218.92, 249.89999999999998, 261.8], [3, 269.44, 306.488, 249.89999999999998, 261.8], [3, 372.164, 409.212, 249.89999999999998, 261.8], [3, 468.99399999999997, 505.2, 249.89999999999998, 261.8], [3, 570.876, 607.082, 249.89999999999998, 261.8], [3, 624.764, 692.966, 249.89999999999998, 261.8], [3, 774.64, 811.688, 249.89999999999998, 261.8], [3, 25.259999999999998, 159.98, 264.775, 277.865], [3, 170.926, 255.126, 265.965, 279.65], [3, 281.228, 294.7, 265.965, 277.865], [3, 401.63399999999996, 506.042, 265.965, 277.865], [3, 574.244, 606.24, 265.965, 277.865], [3, 652.55, 673.6, 265.965, 277.865], [3, 785.586, 811.688, 265.965, 277.865], [3, 25.259999999999998, 151.56, 282.625, 295.715], [3, 170.926, 236.602, 282.625, 296.905], [3, 87.568, 98.514, 409.35999999999996, 420.66499999999996], [3, 149.034, 159.98, 409.35999999999996, 420.66499999999996], [3, 569.192, 606.24, 408.765, 418.88], [3, 779.692, 811.688, 408.765, 418.88], [3, 73.25399999999999, 165.03199999999998, 434.34999999999997, 446.25], [3, 255.126, 343.536, 431.375, 444.465], [3, 579.2959999999999, 680.336, 431.375, 444.465], [4, 0.0, 594.405, 40.416, 79.148]]
2026-08-05 12:05:19,939 INFO     29 [qwen-vl-text] ═══ DONE ═══ 36 positions, pages=2, time=27.9s
2026-08-05 12:05:19,939 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 12:05:19,940 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 12:05:19,940 INFO     29 [qwen-vl-text] positions(47): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 12:05:19,940 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [47]
2026-08-05 12:05:20,129 INFO     29 [qwen-vl-text] page=5, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 12:05:20,131 INFO     29 [qwen-vl-text] LLM extraction start, text_len=410
2026-08-05 12:05:20,131 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 12:05:20,131 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 152, \"bbox_end\": 198, \"encounter_dates\": [\"2026-02-09\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "电子发票(普通发票)\n国家税务总局\n内蒙古自治区税务局\n发票号码：26152000000119478346\n开票日期：2026年02月09日\n购买方信息\n名称\n统一社会信用代码/纳税人识别号：\n销售方信息\n名称：国药控股国大药房内蒙古有限公司\n统一社会信用代码/纳税人识别号：911501005732872139\n项目名称\n规格型号\n单位\n数量\n单价\n金额\n税率/征收率\n税额\n*化学药品制剂*布地格福\n160ug:7.2ug/4.8u\n盒\n3\n237.16814159292\n711.50\n13%\n92.50\n吸入气雾剂\ng:120揿\n*化学药品制剂*布地格福\n160ug:7.2ug/4.8u\n盒\n3\n237.16814159292\n711.50\n13%\n92.50\n吸入气雾剂\ng:120揿\n合计\n￥1423.00\n￥185.00\n价税合计（大写）\n壹仟陆佰零捌圆整\n(小写) ￥1608.00\n备注\n开票人：刘惠",
    "role": "user"
  }
]
[92m12:05:20 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:05:20,132 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:05:20,133 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T12:05:20.131+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 8, "lag": 0, "done": 18, "failed": 0, "current": {"b28be2ce90be11f1a3da71efcdd7cc1f": {"id": "b28be2ce90be11f1a3da71efcdd7cc1f", "doc_id": "b2448c9e90be11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHYH.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHYH.pdf", "size": 10529265, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785928413891, "task_type": "dataflow", "root_trace_id": "e3dcb8801128457d8d83b73c11855569", "root_traceparent": "00-e3dcb8801128457d8d83b73c11855569-a468dda7915c610d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "3e98f84c90bf11f1a3da71efcdd7cc1f": {"id": "3e98f84c90bf11f1a3da71efcdd7cc1f", "doc_id": "3543a40e90bf11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "XALI\u9ea6\u6d4e\u65b0\u4e61 2026-03-06 17.04 (1).pdf", "type": "pdf", "location": "XALI\u9ea6\u6d4e\u65b0\u4e61 2026-03-06 17.04 (1).pdf", "size": 161316076, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785928648860, "task_type": "dataflow", "root_trace_id": "011798f1ac614ad79dfcf6d230b3fd04", "root_traceparent": "00-011798f1ac614ad79dfcf6d230b3fd04-a0d937a531746558-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 12:05:24,678 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 12:05:24,678 INFO     29 [qwen-vl-text] LLM output (len=750):
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
2026-08-05 12:05:24,678 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-09]
2026-08-05 12:05:24,680 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=946229, prompt_len=1164
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
2026-08-05 12:05:52,322 INFO     29 [qwen-vl-text] coord API raw response (len=4156):
[
	{"text": "电子发票(普通发票)", "bbox": [327, 80, 639, 125], "bbox_2d": [327, 80, 639, 125]},
	{"text": "国家税务总局", "bbox": [464, 133, 535, 149], "bbox_2d": [464, 133, 535, 149]},
	{"text": "内蒙古自治区税务局", "bbox": [452, 159, 552, 192], "bbox_2d": [452, 159, 552, 192]},
	{"text": "发票号码：26152000000119478346", "bbox": [735, 100, 951, 120], "bbox_2d": [735, 100, 951, 120]},
	{"text": "开票日期：2026年02月09日", "bbox": [735, 139, 911, 160], "bbox_2d": [735, 139, 911, 160]},
	{"text": "购买方信息", "bbox": [32, 244, 46, 360], "bbox_2d": [32, 244, 46, 360]},
	{"text": "名称", "bbox": [59, 261, 84, 280], "bbox_2d": [59, 261, 84, 280]},
	{"text": "统一社会信用代码/纳税人识别号：", "bbox": [58, 325, 258, 345], "bbox_2d": [58, 325, 258, 345]},
	{"text": "销售方信息", "bbox": [509, 244, 522, 360], "bbox_2d": [509, 244, 522, 360]},
	{"text": "名称：国药控股国大药房内蒙古有限公司", "bbox": [537, 255, 802, 277], "bbox_2d": [537, 255, 802, 277]},
	{"text": "统一社会信用代码/纳税人识别号：911501005732872139", "bbox": [536, 320, 955, 343], "bbox_2d": [536, 320, 955, 343]},
	{"text": "项目名称", "bbox": [77, 380, 136, 400], "bbox_2d": [77, 380, 136, 400]},
	{"text": "规格型号", "bbox": [199, 380, 258, 400], "bbox_2d": [199, 380, 258, 400]},
	{"text": "单位", "bbox": [320, 380, 364, 400], "bbox_2d": [320, 380, 364, 400]},
	{"text": "数量", "bbox": [443, 380, 487, 400], "bbox_2d": [443, 380, 487, 400]},
	{"text": "单价", "bbox": [560, 380, 604, 400], "bbox_2d": [560, 380, 604, 400]},
	{"text": "金额", "bbox": [682, 380, 726, 400], "bbox_2d": [682, 380, 726, 400]},
	{"text": "税率/征收率", "bbox": [746, 380, 828, 400], "bbox_2d": [746, 380, 828, 400]},
	{"text": "税额", "bbox": [926, 380, 971, 400], "bbox_2d": [926, 380, 971, 400]},
	{"text": "*化学药品制剂*布地格福", "bbox": [26, 406, 188, 428], "bbox_2d": [26, 406, 188, 428]},
	{"text": "160ug:7.2ug/4.8u", "bbox": [201, 407, 304, 430], "bbox_2d": [201, 407, 304, 430]},
	{"text": "盒", "bbox": [334, 407, 350, 428], "bbox_2d": [334, 407, 350, 428]},
	{"text": "3", "bbox": [478, 407, 488, 428], "bbox_2d": [478, 407, 488, 428]},
	{"text": "237.16814159292", "bbox": [503, 407, 604, 428], "bbox_2d": [503, 407, 604, 428]},
	{"text": "711.50", "bbox": [686, 407, 724, 428], "bbox_2d": [686, 407, 724, 428]},
	{"text": "13%", "bbox": [780, 407, 805, 428], "bbox_2d": [780, 407, 805, 428]},
	{"text": "92.50", "bbox": [940, 407, 971, 428], "bbox_2d": [940, 407, 971, 428]},
	{"text": "吸入气雾剂", "bbox": [26, 437, 101, 459], "bbox_2d": [26, 437, 101, 459]},
	{"text": "g:120揿", "bbox": [201, 437, 249, 460], "bbox_2d": [201, 437, 249, 460]},
	{"text": "*化学药品制剂*布地格福", "bbox": [26, 467, 188, 490], "bbox_2d": [26, 467, 188, 490]},
	{"text": "160ug:7.2ug/4.8u", "bbox": [201, 468, 304, 491], "bbox_2d": [201, 468, 304, 491]},
	{"text": "盒", "bbox": [334, 468, 350, 490], "bbox_2d": [334, 468, 350, 490]},
	{"text": "3", "bbox": [478, 468, 488, 490], "bbox_2d": [478, 468, 488, 490]},
	{"text": "237.16814159292", "bbox": [503, 468, 604, 490], "bbox_2d": [503, 468, 604, 490]},
	{"text": "711.50", "bbox": [686, 468, 724, 490], "bbox_2d": [686, 468, 724, 490]},
	{"text": "13%", "bbox": [780, 468, 805, 490], "bbox_2d": [780, 468, 805, 490]},
	{"text": "92.50", "bbox": [940, 468, 971, 490], "bbox_2d": [940, 468, 971, 490]},
	{"text": "吸入气雾剂", "bbox": [26, 497, 101, 519], "bbox_2d": [26, 497, 101, 519]},
	{"text": "g:120揿", "bbox": [201, 497, 249, 520], "bbox_2d": [201, 497, 249, 520]},
	{"text": "合计", "bbox": [101, 654, 114, 673], "bbox_2d": [101, 654, 114, 673]},
	{"text": "计", "bbox": [175, 654, 188, 673], "bbox_2d": [175, 654, 188, 673]},
	{"text": "￥1423.00", "bbox": [667, 650, 724, 670], "bbox_2d": [667, 650, 724, 670]},
	{"text": "￥185.00", "bbox": [921, 650, 971, 670], "bbox_2d": [921, 650, 971, 670]},
	{"text": "价税合计（大写）", "bbox": [84, 695, 194, 715], "bbox_2d": [84, 695, 194, 715]},
	{"text": "壹仟陆佰零捌圆整", "bbox": [303, 691, 424, 713], "bbox_2d": [303, 691, 424, 713]},
	{"text": "(小写) ￥1608.00", "bbox": [691, 690, 821, 713], "bbox_2d": [691, 690, 821, 713]},
	{"text": "备注", "bbox": [32, 767, 46, 787], "bbox_2d": [32, 767, 46, 787]},
	{"text": "注", "bbox": [32, 807, 46, 827], "bbox_2d": [32, 807, 46, 827]},
	{"text": "开票人：刘惠", "bbox": [95, 898, 185, 920], "bbox_2d": [95, 898, 185, 920]}
]
2026-08-05 12:05:52,322 INFO     29 [qwen-vl-text] coord API: raw_items=49, valid_items=49, elapsed=27.6s
2026-08-05 12:05:52,322 INFO     29 [qwen-vl-text] coord item[0]: text=电子发票(普通发票), bbox=[327, 80, 639, 125]
2026-08-05 12:05:52,323 INFO     29 [qwen-vl-text] coord item[1]: text=国家税务总局, bbox=[464, 133, 535, 149]
2026-08-05 12:05:52,323 INFO     29 [qwen-vl-text] coord item[2]: text=内蒙古自治区税务局, bbox=[452, 159, 552, 192]
2026-08-05 12:05:52,323 INFO     29 [qwen-vl-text] coord item[3]: text=发票号码：26152000000119478346, bbox=[735, 100, 951, 120]
2026-08-05 12:05:52,323 INFO     29 [qwen-vl-text] coord item[4]: text=开票日期：2026年02月09日, bbox=[735, 139, 911, 160]
2026-08-05 12:05:52,323 INFO     29 [qwen-vl-text] coord item[5]: text=购买方信息, bbox=[32, 244, 46, 360]
2026-08-05 12:05:52,323 INFO     29 [qwen-vl-text] coord item[6]: text=名称, bbox=[59, 261, 84, 280]
2026-08-05 12:05:52,323 INFO     29 [qwen-vl-text] coord item[7]: text=统一社会信用代码/纳税人识别号：, bbox=[58, 325, 258, 345]
2026-08-05 12:05:52,323 INFO     29 [qwen-vl-text] coord item[8]: text=销售方信息, bbox=[509, 244, 522, 360]
2026-08-05 12:05:52,323 INFO     29 [qwen-vl-text] coord item[9]: text=名称：国药控股国大药房内蒙古有限公司, bbox=[537, 255, 802, 277]
2026-08-05 12:05:52,323 INFO     29 [qwen-vl-text] coord item[10]: text=统一社会信用代码/纳税人识别号：911501005732872139, bbox=[536, 320, 955, 343]
2026-08-05 12:05:52,323 INFO     29 [qwen-vl-text] coord item[11]: text=项目名称, bbox=[77, 380, 136, 400]
2026-08-05 12:05:52,323 INFO     29 [qwen-vl-text] coord item[12]: text=规格型号, bbox=[199, 380, 258, 400]
2026-08-05 12:05:52,323 INFO     29 [qwen-vl-text] coord item[13]: text=单位, bbox=[320, 380, 364, 400]
2026-08-05 12:05:52,323 INFO     29 [qwen-vl-text] coord item[14]: text=数量, bbox=[443, 380, 487, 400]
2026-08-05 12:05:52,323 INFO     29 [qwen-vl-text] coord item[15]: text=单价, bbox=[560, 380, 604, 400]
2026-08-05 12:05:52,323 INFO     29 [qwen-vl-text] coord item[16]: text=金额, bbox=[682, 380, 726, 400]
2026-08-05 12:05:52,323 INFO     29 [qwen-vl-text] coord item[17]: text=税率/征收率, bbox=[746, 380, 828, 400]
2026-08-05 12:05:52,323 INFO     29 [qwen-vl-text] coord item[18]: text=税额, bbox=[926, 380, 971, 400]
2026-08-05 12:05:52,324 INFO     29 [qwen-vl-text] coord item[19]: text=*化学药品制剂*布地格福, bbox=[26, 406, 188, 428]
2026-08-05 12:05:52,324 INFO     29 [qwen-vl-text] coord item[20]: text=160ug:7.2ug/4.8u, bbox=[201, 407, 304, 430]
2026-08-05 12:05:52,324 INFO     29 [qwen-vl-text] coord item[21]: text=盒, bbox=[334, 407, 350, 428]
2026-08-05 12:05:52,324 INFO     29 [qwen-vl-text] coord item[22]: text=3, bbox=[478, 407, 488, 428]
2026-08-05 12:05:52,324 INFO     29 [qwen-vl-text] coord item[23]: text=237.16814159292, bbox=[503, 407, 604, 428]
2026-08-05 12:05:52,324 INFO     29 [qwen-vl-text] coord item[24]: text=711.50, bbox=[686, 407, 724, 428]
2026-08-05 12:05:52,324 INFO     29 [qwen-vl-text] coord item[25]: text=13%, bbox=[780, 407, 805, 428]
2026-08-05 12:05:52,324 INFO     29 [qwen-vl-text] coord item[26]: text=92.50, bbox=[940, 407, 971, 428]
2026-08-05 12:05:52,324 INFO     29 [qwen-vl-text] coord item[27]: text=吸入气雾剂, bbox=[26, 437, 101, 459]
2026-08-05 12:05:52,324 INFO     29 [qwen-vl-text] coord item[28]: text=g:120揿, bbox=[201, 437, 249, 460]
2026-08-05 12:05:52,324 INFO     29 [qwen-vl-text] coord item[29]: text=*化学药品制剂*布地格福, bbox=[26, 467, 188, 490]
2026-08-05 12:05:52,324 INFO     29 [qwen-vl-text] coord item[30]: text=160ug:7.2ug/4.8u, bbox=[201, 468, 304, 491]
2026-08-05 12:05:52,324 INFO     29 [qwen-vl-text] coord item[31]: text=盒, bbox=[334, 468, 350, 490]
2026-08-05 12:05:52,324 INFO     29 [qwen-vl-text] coord item[32]: text=3, bbox=[478, 468, 488, 490]
2026-08-05 12:05:52,324 INFO     29 [qwen-vl-text] coord item[33]: text=237.16814159292, bbox=[503, 468, 604, 490]
2026-08-05 12:05:52,324 INFO     29 [qwen-vl-text] coord item[34]: text=711.50, bbox=[686, 468, 724, 490]
2026-08-05 12:05:52,324 INFO     29 [qwen-vl-text] coord item[35]: text=13%, bbox=[780, 468, 805, 490]
2026-08-05 12:05:52,324 INFO     29 [qwen-vl-text] coord item[36]: text=92.50, bbox=[940, 468, 971, 490]
2026-08-05 12:05:52,325 INFO     29 [qwen-vl-text] coord item[37]: text=吸入气雾剂, bbox=[26, 497, 101, 519]
2026-08-05 12:05:52,325 INFO     29 [qwen-vl-text] coord item[38]: text=g:120揿, bbox=[201, 497, 249, 520]
2026-08-05 12:05:52,325 INFO     29 [qwen-vl-text] coord item[39]: text=合计, bbox=[101, 654, 114, 673]
2026-08-05 12:05:52,325 INFO     29 [qwen-vl-text] coord item[40]: text=计, bbox=[175, 654, 188, 673]
2026-08-05 12:05:52,325 INFO     29 [qwen-vl-text] coord item[41]: text=￥1423.00, bbox=[667, 650, 724, 670]
2026-08-05 12:05:52,325 INFO     29 [qwen-vl-text] coord item[42]: text=￥185.00, bbox=[921, 650, 971, 670]
2026-08-05 12:05:52,325 INFO     29 [qwen-vl-text] coord item[43]: text=价税合计（大写）, bbox=[84, 695, 194, 715]
2026-08-05 12:05:52,325 INFO     29 [qwen-vl-text] coord item[44]: text=壹仟陆佰零捌圆整, bbox=[303, 691, 424, 713]
2026-08-05 12:05:52,325 INFO     29 [qwen-vl-text] coord item[45]: text=(小写) ￥1608.00, bbox=[691, 690, 821, 713]
2026-08-05 12:05:52,325 INFO     29 [qwen-vl-text] coord item[46]: text=备注, bbox=[32, 767, 46, 787]
2026-08-05 12:05:52,325 INFO     29 [qwen-vl-text] coord item[47]: text=注, bbox=[32, 807, 46, 827]
2026-08-05 12:05:52,325 INFO     29 [qwen-vl-text] coord item[48]: text=开票人：刘惠, bbox=[95, 898, 185, 920]
2026-08-05 12:05:52,325 INFO     29 [qwen-vl-text] page=5 — 47/47 coords, api_time=27.6s
2026-08-05 12:05:52,326 INFO     29 [qwen-vl-text] new_positions (47):
[[5, 275.334, 538.038, 47.599999999999994, 74.375], [5, 390.688, 450.46999999999997, 79.13499999999999, 88.655], [5, 380.584, 464.784, 94.60499999999999, 114.24], [5, 618.87, 800.742, 59.5, 71.39999999999999], [5, 618.87, 767.062, 82.705, 95.19999999999999], [5, 26.944, 38.732, 145.18, 214.2], [5, 49.678, 70.728, 155.295, 166.6], [5, 48.836, 217.236, 193.375, 205.27499999999998], [5, 428.578, 439.524, 145.18, 214.2], [5, 452.154, 675.284, 151.725, 164.815], [5, 451.312, 804.11, 190.39999999999998, 204.08499999999998], [5, 64.834, 114.512, 226.1, 238.0], [5, 167.558, 217.236, 226.1, 238.0], [5, 269.44, 306.488, 226.1, 238.0], [5, 373.006, 410.054, 226.1, 238.0], [5, 471.52, 508.568, 226.1, 238.0], [5, 574.244, 611.292, 226.1, 238.0], [5, 628.132, 697.1759999999999, 226.1, 238.0], [5, 779.692, 817.582, 226.1, 238.0], [5, 21.892, 158.296, 241.57, 254.66], [5, 169.242, 255.968, 242.165, 255.85], [5, 281.228, 294.7, 242.165, 254.66], [5, 402.476, 410.89599999999996, 242.165, 254.66], [5, 423.526, 508.568, 242.165, 254.66], [5, 577.612, 609.608, 242.165, 254.66], [5, 656.76, 677.81, 242.165, 254.66], [5, 791.48, 817.582, 242.165, 254.66], [5, 21.892, 85.042, 260.015, 273.10499999999996], [5, 169.242, 209.658, 260.015, 273.7], [5, 21.892, 158.296, 277.865, 291.55], [5, 169.242, 255.968, 278.46, 292.145], [5, 281.228, 294.7, 278.46, 291.55], [5, 402.476, 410.89599999999996, 278.46, 291.55], [5, 423.526, 508.568, 278.46, 291.55], [5, 577.612, 609.608, 278.46, 291.55], [5, 656.76, 677.81, 278.46, 291.55], [5, 791.48, 817.582, 278.46, 291.55], [5, 21.892, 85.042, 295.715, 308.805], [5, 169.242, 209.658, 295.715, 309.4], [5, 85.042, 95.988, 389.13, 400.435], [5, 147.35, 158.296, 389.13, 400.435], [5, 561.614, 609.608, 386.75, 398.65], [5, 775.482, 817.582, 386.75, 398.65], [5, 70.728, 163.34799999999998, 413.525, 425.42499999999995], [5, 255.126, 357.008, 411.145, 424.23499999999996], [5, 581.822, 691.2819999999999, 410.54999999999995, 424.23499999999996], [5, 26.944, 38.732, 456.36499999999995, 468.265]]
2026-08-05 12:05:52,326 INFO     29 [qwen-vl-text] ═══ DONE ═══ 47 positions, pages=1, time=32.4s
2026-08-05 12:05:52,356 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-05 12:05:52,357 INFO     29 [Trace] task=b28be2ce | doc=麦济ZHYH.pdf | Extractor:Medication | outputs={"chunks": "4 items, types={'MedicationRecord': 4}", "html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-05 12:05:52,357 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-05 12:05:52,358 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T12:05:52.357+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 8, "lag": 0, "done": 18, "failed": 0, "current": {"b28be2ce90be11f1a3da71efcdd7cc1f": {"id": "b28be2ce90be11f1a3da71efcdd7cc1f", "doc_id": "b2448c9e90be11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHYH.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHYH.pdf", "size": 10529265, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785928413891, "task_type": "dataflow", "root_trace_id": "e3dcb8801128457d8d83b73c11855569", "root_traceparent": "00-e3dcb8801128457d8d83b73c11855569-a468dda7915c610d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "3e98f84c90bf11f1a3da71efcdd7cc1f": {"id": "3e98f84c90bf11f1a3da71efcdd7cc1f", "doc_id": "3543a40e90bf11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "XALI\u9ea6\u6d4e\u65b0\u4e61 2026-03-06 17.04 (1).pdf", "type": "pdf", "location": "XALI\u9ea6\u6d4e\u65b0\u4e61 2026-03-06 17.04 (1).pdf", "size": 161316076, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785928648860, "task_type": "dataflow", "root_trace_id": "011798f1ac614ad79dfcf6d230b3fd04", "root_traceparent": "00-011798f1ac614ad79dfcf6d230b3fd04-a0d937a531746558-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 12:05:52,367 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 12:05:52,367 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m12:05:52 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:05:52,369 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:05:53,596 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 12:05:53,603 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-05 12:05:53,603 INFO     29 [Trace] task=b28be2ce | doc=麦济ZHYH.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-05 12:05:53,603 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-05 12:05:53,609 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 12:05:53,610 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m12:05:53 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:05:53,611 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:05:57,350 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 12:05:57,357 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-05 12:05:57,357 INFO     29 [Trace] task=b28be2ce | doc=麦济ZHYH.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-05 12:05:57,357 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-05 12:05:57,362 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 12:05:57,362 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-05 12:05:58,052 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 12:05:58,060 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-05 12:05:58,060 INFO     29 [Trace] task=b28be2ce | doc=麦济ZHYH.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-05 12:05:58,061 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-05 12:05:58,065 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 12:05:58,066 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m12:05:58 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:05:58,066 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 12:05:59,804 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 12:05:59,812 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-05 12:05:59,812 INFO     29 [Trace] task=b28be2ce | doc=麦济ZHYH.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "199 items", "markdown": "", "text": "", "name": "麦济ZHYH.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-05 12:05:59,812 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-05 12:05:59,813 INFO     29 [ChunkMerger] Merged 6 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 4, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1} (filtered 6 noise chunks)
2026-08-05 12:05:59,823 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-05 12:05:59,823 INFO     29 [Trace] task=b28be2ce | doc=麦济ZHYH.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 2, 'MedicationRecord': 4}", "name": "麦济ZHYH.pdf"}
2026-08-05 12:05:59,823 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-05 12:05:59,867 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1785931454270, 'update_date': datetime.datetime(2026, 8, 5, 12, 4, 14), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 398684, 'status': '1'}
2026-08-05 12:06:00,100 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=内蒙古医科大学附属医院门诊病历
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
2026-08-05 12:06:00,480 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-05 12:06:00,480 INFO     29 [Trace] task=b28be2ce | doc=麦济ZHYH.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 2, 'MedicationRecord': 4}", "name": "麦济ZHYH.pdf", "embedding_token_consumption": 1703}
2026-08-05 12:06:00,480 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-05 12:06:00,656 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-05 12:06:00,656 INFO     29 [Trace] task=b28be2ce | doc=麦济ZHYH.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":6,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-05 12:06:00,659 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:06:00,660 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:06:00,660 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:06:00,660 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:06:00,660 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:06:00,660 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 12:06:00,664 INFO     29 set_progress(b28be2ce90be11f1a3da71efcdd7cc1f), progress: 0.82, progress_msg: 12:06:00 [DOC Engine]:
Start to index...
2026-08-05 12:06:00,683 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.014s]
2026-08-05 12:06:00,688 INFO     29 set_progress(b28be2ce90be11f1a3da71efcdd7cc1f), progress: 0.8166666666666668, progress_msg: 
2026-08-05 12:06:00,708 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.015s]
2026-08-05 12:06:00,715 INFO     29 set_progress(b28be2ce90be11f1a3da71efcdd7cc1f), progress: 1.0, progress_msg: 12:06:00 Indexing done (0.05s). Task done (401.23s)
2026-08-05 12:06:00,720 INFO     29 [Done], chunks(6), token(1703), elapsed:401.23
2026-08-05 12:06:00,810 INFO     29 handle_task done for task {"id": "b28be2ce90be11f1a3da71efcdd7cc1f", "doc_id": "b2448c9e90be11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHYH.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHYH.pdf", "size": 10529265, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1785928413891, "task_type": "dataflow", "root_trace_id": "e3dcb8801128457d8d83b73c11855569", "root_traceparent": "00-e3dcb8801128457d8d83b73c11855569-a468dda7915c610d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
