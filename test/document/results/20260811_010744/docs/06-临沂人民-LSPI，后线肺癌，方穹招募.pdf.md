# 基准结果：06-临沂人民-LSPI，后线肺癌，方穹招募.pdf

## 基本信息

- 文件：`06-临沂人民-LSPI，后线肺癌，方穹招募.pdf`
- 大小：6420.2 KB
- PDF 总页数：15
- doc_id：`15bf5b9494e011f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-11T01:22:36  完成时间：2026-08-11T01:28:15  耗时：338.1s
- progress_msg：`17:28:13 Indexing done (0.07s). Task done (313.73s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 72e83788 | 1 | 2-2 | 彩色病理图文报告 姓名： 性别：女 年龄：59岁 收到日期：2025-10-24 |
| 2 | 1c2c6065 | 1 | 3-3 | CT检查报告单 患者编号: 扫描日期: 1/13/2026 姓名: 性别:女 年 |
| 3 | cccf5634 | 1 | 4-4 | CT检查报告单 患者编号: 放射编号: 扫描日期:2/26/2026 姓名: 性 |
| 4 | d029fb0f | 3 | 4-6 | 2:11:34 PM 科室：呼吸与危重症医学科 姓名： 出院记录 女，59岁，主 |
| 5 | 586f1f3b | 1 | 7-7 | 科室：呼吸内科 姓名： 门诊病历号： [初诊病历记录(门诊放化疗患者专用)] 就 |
| 6 | 2ec87768 | 1 | 15-15 | <table><tr><td>白细胞计数</td><td>WBC</td><td |
| 7 | 0baa46e8 | 1 | 12-12 | <table><tr><td>EGFR c.2369C>T (p.T790M)< |
| 8 | c1270b44 | 1 | 13-13 | <table><tr><td>尿液分析-酸碱度</td><td>PH</td>< |
| 9 | d69a4975 | 1 | 14-14 | <table><tr><td>血清丙氨酸氨基转移酶测定</td><td>ALT< |

- chunks 总数：9
- 各 chunk 页数合计（含跨页重复）：11
- 页码并集：`[2, 3, 4, 5, 6, 7, 12, 13, 14, 15]`
- 覆盖页数：10 / 15；缺失页：`[1, 8, 9, 10, 11]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：❌ 未完全覆盖：覆盖 10/15 页，缺失 [1, 8, 9, 10, 11]，超范围 []**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 1 | 0 | 1 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 1 | 1 | 1 | admission_date, discharge_date, department, outcome | **OK** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 3 | 3 | 3 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 4 | 0 | 4 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"ExaminationReport": 3, "DischargeRecord": 1, "OutpatientRecord": 1, "LabReport": 4}`
- ChunkMerger：`{"found": true, "merged": 9, "sources": 9, "stats": {"Extractor:LabExam": 4, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 3, "Extractor:Progress": 1}, "filtered_noise": 5}`
- Extractor skip 证据：2 条
  - `[no_items_extracted] 2026-08-10 17:24:35,289 WARNING  29 [qwen-vl-table] page=8 no items extracted`
  - `[no_text_noise] 2026-08-10 17:28:12,534 INFO     29 [ChunkMerger] Merged 9 chunks from 9 sources: {'Extractor:LabExam': 4, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 17:22:38,778 INFO     29 handle_task begin for task {"id": "15f63a1a94e011f1bd9827cf206dfa2d", "doc_id": "15bf5b9494e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "size": 6574298, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786382558729, "task_type": "dataflow", "root_trace_id": "e45d0687fc994f25a61430b755af4825", "root_traceparent": "00-e45d0687fc994f25a61430b755af4825-4f140d87c9e2cd09-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 17:22:38,996 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 17:22:39,576 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 17:22:39,593 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:22:39,593 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 17:22:39,593 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 17:22:39,623 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 17:22:39,623 INFO     29 ============================================================
2026-08-10 17:22:39,623 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 17:22:39,623 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 17:22:39,623 INFO     29 ============================================================
2026-08-10 17:22:39,623 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 17:22:39,623 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 17:22:39,626 INFO     29 No torch found.
2026-08-10 17:22:40,567 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=15
2026-08-10 17:22:40,608 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=69855, prompt_len=764
2026-08-10 17:22:41,883 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 17:22:41,883 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 17:22:41,892 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=69855, prompt_len=401
2026-08-10 17:22:42,948 INFO     29 [qwen-vl-parser] text API response (len=145):
["患者 LSPI 治疗史 女 60 岁 山西 肺腺癌 EGFR19del T790M", "20 年 8 月确诊肺腺癌", "20 年 8 月-25 年 10 月 吉非替尼 PD", "25 年 11 月-26 年 3月 LHX43联合斯鲁利单抗临床项目 PD", "进展：新发肝转移"]
2026-08-10 17:22:42,949 INFO     29 [qwen-vl-parser] page=1 text: 5 lines (bbox 0-4)
2026-08-10 17:22:42,949 INFO     29 [qwen-vl-parser] page=1 text: 5 sections
2026-08-10 17:22:43,061 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=509169, prompt_len=764
2026-08-10 17:22:44,352 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-10-24"}
```
2026-08-10 17:22:44,353 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=2025-10-24
2026-08-10 17:22:44,365 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=509169, prompt_len=401
2026-08-10 17:22:46,904 INFO     29 [qwen-vl-parser] text API response (len=465):
["彩色病理图文报告", "姓名：", "性别：女", "年龄：59岁", "收到日期：2025-10-24", "送检医院：本院", "送检科室：肺病科", "住院号：", "送检医生：0117", "标本名称：", "蜡块数：1", "特征图像：", "大体描述：", "(右肺)穿刺组织3条，长0.2-0.4CM,直径0.1CM。", "病理诊断：", "(右肺)穿刺玻变的纤维组织中可见少许癌巢浸润，结合免疫组化符合：肺腺癌，", "请结合临床及其它检查综合判断。", "免疫组化：CK(+)CK7(+)TTF-1(+)Napsin-A(+)P63(-)P40(-)Syn(-)INSM-1(-)Ki-67", "(+约20%)BRG1(+)。", "报告医生：张瑜", "审核医生：梁晓霞", "1.注：此结果仅针对本次送检样本，仅供临床医生参考。如有疑问，请于7个工作日内与病理科联系。报告日期：2025-10-28", "2.本报告医师签名有效。", "3.本报告电子版仅供参考，请以纸质报告为准。", "电话："]
2026-08-10 17:22:46,905 INFO     29 [qwen-vl-parser] page=2 text: 25 lines (bbox 5-29)
2026-08-10 17:22:46,905 INFO     29 [qwen-vl-parser] page=2 text: 25 sections
2026-08-10 17:22:47,055 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=731664, prompt_len=764
2026-08-10 17:22:48,347 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-01-13"}
```
2026-08-10 17:22:48,347 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=2026-01-13
2026-08-10 17:22:48,358 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=731664, prompt_len=401
2026-08-10 17:22:53,271 INFO     29 [qwen-vl-parser] text API response (len=898):
["CT检查报告单", "患者编号:", "扫描日期: 1/13/2026", "姓名:", "性别:女", "年龄:59岁科别:", "住院号:", "扫描设备:SIEMENS_CT", "扫描方法:平扫+增强12张", "药品:碘普罗胺注射液", "100ml", "药品处理方式:静脉+静脉留置+高压注射", "检查项目:上腹+下腹+盆腔+胸部(平扫+增强)", "扫描所见:", "参考2025-11-21胸部CT,所见如下:", "1.右肺可见巨大不规则肿块,病变范围较广,累及右全肺,增强扫描不均匀强化,较前", "局部略缩小;余双肺见多发结节影,部分内可见空泡,最大径约2cm,较前部分略缩", "小。", "2.右侧腋窝、纵隔及右肺门见增大淋巴结,最大短径约1.5cm,不均匀强化。考虑MT,", "右侧腋窝淋巴结较前缩小,余大致同前。右侧心隔角淋巴结较前增大,短径约0.6cm。", "3.心影不大,心包少量积液同前。", "4.右侧胸膜不均匀增厚,考虑MT,伴少量积液,同前。", "5.肝脏大小形态尚可,肝内散在低密度结节,较大径约2.3cm,大部分界清,增强扫描", "未见明显强化,部分界欠清,同前相仿。", "6.双肾多发囊肿,较大径约0.4cm,同前。", "7.脾脏见稍低密度结节,较大径约0.6cm,边界欠清,边缘似有强化,同前相仿。", "8.胰腺、双侧肾上腺未见明显异常密度影。", "9.腹膜后见小淋巴结显示,最大短径约0.4cm,大致同前。", "10.膀胱充盈尚可,壁未见明显增厚。", "11.双侧附件区见致密影同前。子宫大小形态尚可,子宫肌层强化欠均匀,同前相仿,", "请结合临床。盆腔少量积液较前增多。", "12.双侧髂血管及腹股沟区未见明显增大淋巴结。", "13.骨窗部分肋骨多发斑片状密度增高影,周围软组织增厚,增强后明显强化。考虑", "MT,大致同前。", "印象:", "报告者:王二娟", "审核医师: 何晶晶", "日期:1/13/2026 2:11:3", "本报告仅供临床医师参考,不作为法律依据。妥善保管,遗失不补。"]
2026-08-10 17:22:53,271 INFO     29 [qwen-vl-parser] page=3 text: 39 lines (bbox 30-68)
2026-08-10 17:22:53,271 INFO     29 [qwen-vl-parser] page=3 text: 39 sections
2026-08-10 17:22:53,419 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=738385, prompt_len=764
2026-08-10 17:22:54,797 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-02-26"}
```
2026-08-10 17:22:54,798 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=2026-02-26
2026-08-10 17:22:54,813 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=738385, prompt_len=401
2026-08-10 17:23:00,366 INFO     29 [qwen-vl-parser] text API response (len=1006):
["CT检查报告单", "患者编号:", "放射编号:", "扫描日期:2/26/2026", "姓名:", "性别:女", "年龄:59岁科别:", "住院号:", "扫描设备:SIEMENS_CT", "扫描方法:平扫+增强12张", "药品:碘普罗胺注射液", "100ml", "药品处理方式:静脉+静脉留置+高压注射", "检查项目:上腹+下腹+盆腔+胸部(平扫+增强)", "检查所见:", "参阅2026-01-13胸部CT前片,所见如下:", "1.右肺可见巨大不规则肿块,病变范围较广,累及右全肺,增强扫描不均匀强化,较前", "局部增大(8-31较原片7-31);余双肺见多发结节影,部分内可见空泡,最大径约", "2cm,较前基本相仿。", "2.右侧腋窝、纵隔及右肺门见增大淋巴结,最大短径约1.5cm,增强扫描呈不均匀强", "化,考虑MT,大致同前。右侧心隔角可见稍大淋巴结,短径约0.6cm,同前相仿。", "3.心影不大,心包少量积液同前。", "4.右侧胸膜不均匀增厚,考虑MT,伴少量积液,同前。", "5.肝脏大小形态尚可,肝内散在低密度结节,较大径约2.3cm,大部分界清,增强扫描", "未见明显强化,部分考虑囊肿,部分不典型,同前相仿。", "6.肝内新增稍低密度结节影,较大者位于肝S6段,径约1.7cm,增强扫描呈轻度强化,", "MT不除外,建议MRI检查。", "7.双肾多发囊肿,较大径约0.4cm,同前。脾脏见稍低密度结节,较大径约0.6cm,边界", "欠清,边缘似有强化,同前相仿。", "8.胰腺、双侧肾上腺未见明显异常密度影。", "9.腹膜后见小淋巴结显示,最大短径约0.4cm,大致同前。", "10.膀胱充盈尚可,壁未见明显增厚。", "11.双侧附件区见致密影同前。子宫大小形态尚可,子宫肌层强化欠均匀,同前相仿,", "请结合临床。盆腔少量积液同前。", "12.双侧髂血管及腹股沟区未见明显增大淋巴结。", "13.骨窗:部分肋骨多发斑片状密度增高影,周围软组织增厚,增强后明显强化,考虑", "MT,大致同前。骶管内囊性灶,同前。", "检查者:武康", "报告者:杨东宇审核医师:侯可", "日期:2/26/2026 3:00:48", "本报告仅供临床医师参考,不作为法律依据。妥善保管,遗失不补。", "2:11:34 PM"]
2026-08-10 17:23:00,366 INFO     29 [qwen-vl-parser] page=4 text: 42 lines (bbox 69-110)
2026-08-10 17:23:00,366 INFO     29 [qwen-vl-parser] page=4 text: 42 sections
2026-08-10 17:23:00,543 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1127476, prompt_len=764
2026-08-10 17:23:01,914 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 17:23:01,914 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 17:23:01,930 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1127476, prompt_len=401
2026-08-10 17:23:03,453 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:23:03.453+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 80, "failed": 0, "current": {"15f63a1a94e011f1bd9827cf206dfa2d": {"id": "15f63a1a94e011f1bd9827cf206dfa2d", "doc_id": "15bf5b9494e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "size": 6574298, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786382558729, "task_type": "dataflow", "root_trace_id": "e45d0687fc994f25a61430b755af4825", "root_traceparent": "00-e45d0687fc994f25a61430b755af4825-4f140d87c9e2cd09-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:23:11,921 INFO     29 [qwen-vl-parser] text API response (len=1452):
["科室：呼吸与危重症医学科 姓名：", "出院记录", "女，59岁，主因“确诊右肺腺癌5年”于2025-10-20入院。于", "2025年10月29日出院，住院天数：9天。", "入院情况：患者于2020年8月因咳嗽，咳痰伴右侧胸痛于北京市丰台中西医结合医院", "行胸部CT示：右肺门旁软组织团块影，考虑癌可能；8月31日于我院住院治疗，期间完善", "支气管镜检查，病理结果示：符合浸润性肺腺癌；基因检测示：EGFR Exon21-L858R突变（", "突变比例43.34%），EGFR Exon19缺失突变（突变比例55.81%），KRAS突变（突变比例", "27.72%）；予口服吉非替尼片（伊瑞可）靶向治疗至今，2021年1月复查提示病情稳定，此后", "患者未规律复查。2023年7月31日于我院住院复查，复查提示病情进展，考虑当前靶向药", "耐药，建议患者重新穿刺行基因检查，患者考虑后拒绝，要求继续服药治疗后出院。现患", "者为求全面复查及中西医结合诊治入院。入院症见：神志清，精神可，偶有咳嗽，干咳少", "痰，活动后稍有气喘，口苦，纳食可，夜眠可，二便正常。舌质暗红，苔薄黄，脉弦滑。", "入院诊断：", "中医诊断：肺癌", "痰瘀互结", "西医诊断：右肺腺癌 T2aN2M1a IV期/双肺多发转移/淋巴结多发转移/右侧胸膜", "转移/脑转移？/靶向治疗后，肝囊肿，营养不良性贫血，脂肪肝", "诊疗经过：入院完善相关检查，指导治疗。化验结果回报：血常规+C反应蛋白：白", "细胞计数[WBC]4.810~9/L，红细胞计数[RBC]4.5410^12/L，血红蛋白量[HGB]127.0g/L，", "红细胞平均血红蛋白浓度[MCHC]314.0g/L，淋巴细胞绝对值[LY#]1.0310^9/L，C-反应", "蛋白[CRP]1.98mg/L。免疫球蛋白E[IgE]8.80IU/mL。肝肾功：白蛋白[ALB]36g/L，高密度", "脂蛋白胆固醇[HDL-C]0.92mmol/L，二氧化碳结合力[CO2CP]28.80mmol/L，总蛋白[TP]", "60.7g/L，①肾小球滤过率估算[eGFR]84.2ml/min，②肾小球滤过率估算[eGFR]", "80.3ml/min。肿瘤标志物示：神经元特异性烯醇化酶[NSE]34.3ng/mL，细胞角蛋白19片段", "[CYFRA21-1]11.50ng/mL。甲功示：抗甲状腺过氧化物酶抗体[Anti-TPO]814.00IU/ml。细", "胞因子测定、心肌酶谱+C反应蛋白、凝血+D二聚体未见明显异常。心电图示：窦性心律", "不齐，心电轴不偏，心电图大致正常。过敏源检测未见明显异常。胸部CT回报：1.符合右", "肺ca征像，包绕邻近血管；2.双肺多发结节，考虑MT；3.纵膈、右肺肺门及右侧腋窝淋巴", "结MT；4.右侧胸膜不均匀增厚，MT可能性大；5.右侧7、8测前肋MT伴软组织肿块形成、右", "侧胸壁增厚；6.所示肝右叶多发低密度影；脾内稍低密度灶；右肾小囊肿可能大；右侧肾", "上腺稍增粗，请结合腹部检查。请结合临床及原片，治疗后复查。脑MRI回报：1.右侧脑", "室前角旁异常信号，结合病史考虑MT，请结合临床复查；2.左侧上颌窦炎。气管镜检查：", "右肺下叶外压性闭塞/支气管镜下炎症性改变。心脏彩超回报：心脏形态结构及功能未见明", "电话：", "备注"]
2026-08-10 17:23:11,922 INFO     29 [qwen-vl-parser] page=5 text: 36 lines (bbox 111-146)
2026-08-10 17:23:11,922 INFO     29 [qwen-vl-parser] page=5 text: 36 sections
2026-08-10 17:23:12,087 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=892554, prompt_len=764
2026-08-10 17:23:13,375 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 17:23:13,376 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-10 17:23:13,395 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=892554, prompt_len=401
2026-08-10 17:23:19,283 INFO     29 [qwen-vl-parser] text API response (len=1047):
["科室：呼吸与危重症医学科 姓名：", "显异常。腹部彩超回报：肝囊肿；胆囊张力高；胰脾双肾未见明显异常。淋巴结彩超回", "报：右侧锁骨区多发肿大淋巴结，MT；双侧腋窝肿大淋巴结，MT。双侧腹股沟区及腹盆腔", "探查未见明显异常肿大淋巴结。病理报告（202510924）：（右肺支气管镜活检组织）送", "检组织被覆鳞状上皮呈慢性炎改变；免疫组化：P40(+)P53(低表达)K1-67(+约10%)。液", "基细胞学检查（Y252882）：（右肺肺泡灌洗液）支气管上皮细胞，炎细胞，个别非典型", "细胞，建议临床进一步检查。全身骨扫描：右侧第7、8侧肋局部及右侧第9肋后肋局部骨", "质代谢增高，结合脏器断层显像，考虑MT，与2023-8-21日片对比新发；右侧第4-6前侧肋", "局部骨质代谢轻度增高，建议3个月复查；L4-5左侧椎小关节退行性改变，较前未见明显", "变化；双侧膝关节骨质代谢增高，考虑骨关节炎性改变。病理图文报告（10239191）：（", "右肺）穿刺波变的纤维组织中可见少许癌巢浸润，结合免疫组化符合：肺腺癌，请结合临", "床及其他检查综合判断。免疫组化：CK(+)CK7(+)TTF-1(+)Napsin-A(+)P63(-)P40(-)Syn(", "一)INSM-1(-)Ki-67(+约20%)BRG1(+)。予抑酸护胃、中药抗肿瘤，气道雾化，氧疗及中医", "外治法、中医辨证论治等中西医综合治疗。于10月24日行CT引导下肺穿刺活检以明确病", "理。", "出院情况：患者神志清，精神可，偶有咳嗽减轻，干咳少痰，活动后稍有气喘，口", "苦，纳食可，夜眠可，二便正常。舌质暗红，苔薄黄，脉弦滑。查体：双肺呼吸音清，未", "闻及明显干湿性啰音，未闻及捻发音，胸部摩擦音。患者症状好转，要求出院于家中等待", "基因检测结果，请示上级医师后，准予出院。", "出院诊断：", "中医诊断：肺癌", "痰瘀互结", "西医诊断：右肺腺癌 T2aN2M1a IV期/双肺多发转移/淋巴结多发转移/右侧胸", "膜转移/脑转移/骨转移/靶向治疗后，肝囊肿，营养不良性贫血，脂肪肝", "出院医嘱：1.院外规律用药，中草药日一剂，定期复诊，不适随诊；2.定期复查胸部", "CT、肺功能；3.加强营养，注意保暖，避免感冒；4.做基因检测确定患者基因突变类型。", "中医调护：避风寒，慎起居，节饮食，畅情志。", "签名：孟丽红", "电话："]
2026-08-10 17:23:19,283 INFO     29 [qwen-vl-parser] page=6 text: 29 lines (bbox 147-175)
2026-08-10 17:23:19,283 INFO     29 [qwen-vl-parser] page=6 text: 29 sections
2026-08-10 17:23:19,523 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1557977, prompt_len=764
2026-08-10 17:23:21,010 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-02-27"}
```
2026-08-10 17:23:21,010 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=2026-02-27
2026-08-10 17:23:21,021 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1557977, prompt_len=401
2026-08-10 17:23:26,177 INFO     29 [qwen-vl-parser] text API response (len=953):
["科室：呼吸内科", "姓名：", "门诊病历号：", "[初诊病历记录(门诊放化疗患者专用)]", "就诊时间：2026年02月27日10时50分", "科别：呼吸内科", "主诉：确诊右肺腺癌5+年，临床试验中", "现病史：患者于2020-8开始出现咳嗽，咳痰伴右侧胸痛，就诊于", "完善相关检查，", "诊断：右肺腺癌，双肺多发转移，（具体转移不详）突变类型 Exon21-L858R突变，Exon19缺失突", "变，KRAS突变，一直维持吉非替尼治疗。2025-11复查病情病情进展，PFS1：63个月。诊断：右肺", "腺癌（驱动基因阴性） 右肺门、纵隔及右侧腋窝多发淋巴结转移 双肺多发转移 右侧胸膜转移", "肋骨转移。受试者于2025年11月11日签署知情同意书，自愿参加一项评估HLX43（抗PD-L1的ADC）", "联合斯鲁利单抗（抗PD-1人源化单克隆抗体注射液）的晚期/转移性实体瘤患者中的安全性、耐受", "性和有效性的Ib/II期临床研究（V3.0 2025年08月15日），2025年12月2给予C1D1治疗，2025年12", "月24给予C2D1治疗，2026年1月14日给予C3D1治疗，2026年2月5日给予C4D1治疗。现患者无特殊不", "适，拟行周期性治疗入院。自发病以来，精神食欲可，大小便无异常，体重未见明显减轻。", "既往史：2020年8月诊断：肝囊肿。否认传染病史，无高血压史，否认糖尿病史，否认心脏病史，", "否认外伤史，否认输血史，预防接种史：不详，否认食物、药物过敏史。", "阳性体征：无", "必要的阴性体征和辅助检查：无", "诊断：1.右肺恶性肿瘤（腺癌）淋巴结继发恶性肿瘤（右肺门、纵膈、右腋窝）胸膜继发性恶性", "肿瘤骨继发恶性肿瘤2.肝囊肿", "治疗意见：入组临床试验治疗。", "医师签名：一式其其", "激活W", "2302.250626", "山", "SAMSUNG", "E", "R", "T", "Y", "U", "O", "P", "D", "F", "G", "H", "J", "K", "L", "C", "V", "B", "M", "ViewSonic", "7", "8", "4"]
2026-08-10 17:23:26,177 INFO     29 [qwen-vl-parser] page=7 text: 51 lines (bbox 176-226)
2026-08-10 17:23:26,177 INFO     29 [qwen-vl-parser] page=7 text: 51 sections
2026-08-10 17:23:26,316 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=553203, prompt_len=764
2026-08-10 17:23:27,538 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 17:23:27,539 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-10 17:23:27,556 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=553203, prompt_len=401
2026-08-10 17:23:29,637 INFO     29 [qwen-vl-parser] text API response (len=380):
["方案编号：HLX43HLX10-ST201", "申办方：上海复宏汉霖生物技术股份有限公司", "上海复宏汉霖生物医药有限公司", "生物标志物研究-知情同意书", "(可选)", "(2.1版，2025年09月28日)", "方案名称：一项评估HLX43（抗PD-L1的ADC）联合斯鲁利单抗（抗PD-1人", "源化单克隆抗体注射液）在晚期/转移性实体瘤患者中的安全性、耐受性和有效", "性的Ib/II期临床研究", "方案编号：HLX43HLX10-ST201", "申办者：上海复宏汉霖生物技术股份有限公司", "上海复宏汉霖生物医药有限公司", "研究中心：", "院", "主要研究者：", "受试者姓名拼音首字母：LSPZ", "受试者筛选编号：", "生物标志物知情同意书_CHN033_V2.1_20250928", "第1页共7页"]
2026-08-10 17:23:29,637 INFO     29 [qwen-vl-parser] page=8 text: 19 lines (bbox 227-245)
2026-08-10 17:23:29,638 INFO     29 [qwen-vl-parser] page=8 text: 19 sections
2026-08-10 17:23:29,784 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=679329, prompt_len=764
2026-08-10 17:23:31,131 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-11-05"}
```
2026-08-10 17:23:31,131 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=2025-11-05
2026-08-10 17:23:31,142 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=679329, prompt_len=401
2026-08-10 17:23:34,018 INFO     29 [qwen-vl-parser] text API response (len=548):
["安明康", "01 检测概览", "Test Overview", "1 送检信息", "基本信息", "姓", "性别：女", "联系方式：", "年龄：59岁", "送检单位：", "山西省中医院", "样本类型：", "外周血、石蜡切片*12", "送检医师：", "样本来源：", "临床诊断：", "膀胱癌", "收样日期：", "2025-10-31", "临床分层：", "/", "报告日期：", "2025-11-05", "家族史：", "送检项目：", "NGS 50 基因精准套餐", "肿瘤治疗史：", "/", "既往基因检测结果：/", "检测项目", "项目介绍", "该产品精选 50 个与肿瘤发生发展和用药治疗密切相关的基因 (含 NTRK1/2/3 融合基因)，采用扩增子建库技术和高通量测序法检测 50 个基因的热点区域，检测变异类型", "包括点突变、插入/缺失、拷贝数变异及基因融合，精准指导肿瘤靶向及化疗用药，筛查主要耐药原因，提供临床试验药物信息。", "检测方法", "NGS", "考基因组", "GRCh37/hg19", "阳区阜阳北路与北城大道交口创智天地 A6 号楼 (400-801-9858)", "第 1 页/共 31 页"]
2026-08-10 17:23:34,019 INFO     29 [qwen-vl-parser] page=9 text: 39 lines (bbox 246-284)
2026-08-10 17:23:34,019 INFO     29 [qwen-vl-parser] page=9 text: 39 sections
2026-08-10 17:23:34,102 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=398257, prompt_len=764
2026-08-10 17:23:35,261 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 17:23:35,261 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=None
2026-08-10 17:23:35,278 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=398257, prompt_len=401
2026-08-10 17:23:35,513 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:23:35.512+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 80, "failed": 0, "current": {"15f63a1a94e011f1bd9827cf206dfa2d": {"id": "15f63a1a94e011f1bd9827cf206dfa2d", "doc_id": "15bf5b9494e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "size": 6574298, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786382558729, "task_type": "dataflow", "root_trace_id": "e45d0687fc994f25a61430b755af4825", "root_traceparent": "00-e45d0687fc994f25a61430b755af4825-4f140d87c9e2cd09-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:23:39,808 INFO     29 [qwen-vl-parser] text API response (len=506):
["1.3 检测结果汇总", "[基因变异检测结果汇总]", "具有临床意义的位点或热点基因变异：2个（共检出变异：3个）", "基因", "转录本", "检测结果", "突变丰度/拷贝数", "EGFR", "NM_005228", "c.2369C>T (p.T790M)", "6.6%", "EGFR", "NM_005228", "c.2235_2249del (p.E746_A750del)", "24.4%", "注：所有检出基因变异总览详见第2.2节。", "[化疗用药相关检测结果汇总]", "检测项目", "检测结果", "结果解读", "化疗药物疗效评估", "√ 有效性较高药物：8个", "用药详见2.4节", "化疗药物毒副作用评估", "毒副作用较低药物：3个", "1.4 临床用药提示", "靶向用药提示", "潜在获益药物", "[本癌种获批/指南推荐药物]", "潜在耐药药物", "[其他癌种获批/临床试验药物]", "[本癌种获批/指南收录证据]", "[临床研究/其他癌种耐药提", "注：", "1. 优先选择潜在获益药物中", "2. 若样本同时检出敏感突变"]
2026-08-10 17:23:39,808 INFO     29 [qwen-vl-parser] page=10 text: 36 lines (bbox 285-320)
2026-08-10 17:23:39,808 INFO     29 [qwen-vl-parser] page=10 text: 36 sections
2026-08-10 17:23:39,966 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=839473, prompt_len=764
2026-08-10 17:23:41,205 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 17:23:41,206 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=None
2026-08-10 17:23:41,216 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=839473, prompt_len=401
2026-08-10 17:23:44,430 INFO     29 [qwen-vl-parser] text API response (len=534):
["安明康*", "1.4 临床用药提示", "靶向用药提示", "潜在获益药物", "[本癌种获批/指南推荐药物]", "阿美替尼、奥希替尼、贝福替尼、依沃西单抗、信迪利单抗+贝伐珠单抗、瑞厄替尼、伏美替尼、瑞齐替尼、厄洛替尼、德达博妥单抗、达可替尼、埃万妥单抗、阿法替尼、埃克替尼、吉非替尼、利厄替尼、厄洛替尼+贝伐珠单抗、芦康沙妥珠单抗、厄洛替尼+雷莫西尤单抗、佐利替尼、埃万妥单抗+兰泽替尼", "[其他癌种获批/临床试验药物]", "TY-9591、法米替尼+阿美替尼", "潜在耐药药物", "[本癌种获批/指南收录证据]", "厄洛替尼、吉非替尼、佐利替尼、阿法替尼、埃克替尼、美凡厄替尼、达可替尼", "[临床研究/其他癌种耐药提示]", "无", "注:", "1.优先选择潜在获益药物中本癌种获批/指南推荐药物，表示FDA/NMPA批准或国内外指南推荐用于本癌种的靶向药物;", "2.若样本同时检出敏感突变和耐药突变，用药时请综合考虑，用药循证详见2.3节。用药需遵医嘱，谨慎用药。", "化疗用药提示", "具体分析结果见2.4节。", "安徽省合肥市庐阳区阜阳北路与北城大道交口创智天地A6号楼(400-801-9858)", "第3页/"]
2026-08-10 17:23:44,430 INFO     29 [qwen-vl-parser] page=11 text: 20 lines (bbox 321-340)
2026-08-10 17:23:44,430 INFO     29 [qwen-vl-parser] page=11 text: 20 sections
2026-08-10 17:23:44,590 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=762027, prompt_len=764
2026-08-10 17:23:45,954 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 17:23:45,955 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=None
2026-08-10 17:23:45,971 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=762027, prompt_len=401
2026-08-10 17:23:48,718 INFO     29 [qwen-vl-parser] text API response (len=552):
["武汉思泰得医学检验", "报告", "肿瘤", "2.2基因变异结果总览", "[位点变异结果]", "基因", "转录本", "功能区域", "检测结果", "APC", "NM_000038", "exon16", "c.4487C>G (p.T1496S)", "EGFR", "NM_005228", "exon19", "c.2235_2249del (p.E746_A750del)", "EGFR", "NM_005228", "exon20", "c.2369C>T (p.T790M)", "[基因拷贝数结果]", "基因", "染色体位置", "拷贝数", "EGFR", "chr7", "未扩增", "ERBB2", "chr17", "未扩增", "MET", "chr7", "未扩增", "FGFR1", "chr8", "未扩增", "[融合基因结果]", "基因", "检测结果", "ALK", "未检出", "FGFR1", "未检出", "FGFR2", "未检出", "NTRK1", "未检出", "NTRK2", "未检出", "NTRK3", "未检出", "RET", "未检出", "ROS1", "未检出", "安徽省合肥市庐阳区阜阳北路与北"]
2026-08-10 17:23:48,719 INFO     29 [qwen-vl-parser] page=12 text: 57 lines (bbox 341-397)
2026-08-10 17:23:48,719 INFO     29 [qwen-vl-parser] page=12 text: 57 sections
2026-08-10 17:23:48,951 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1581295, prompt_len=764
2026-08-10 17:23:50,306 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2026-02-12"}
```
2026-08-10 17:23:50,307 INFO     29 [qwen-vl-parser] page=13 classify=table report_date=2026-02-12
2026-08-10 17:23:50,324 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1581295, prompt_len=756
2026-08-10 17:23:57,212 INFO     29 [qwen-vl-parser] table API response (len=1422):
\begin{tabular}{ccccccll}
\hline
序号 & & 检验项目 & 结果 & 提示 & 单位 & 参考区间 & 检验方法/检测系统 \\
\hline
1 & PH & ☆口●尿液分析-酸碱度 & 5.0 & & & 4.5~8.0 & 干化学法/SYSMEX \\
2 & NIT & ☆口●尿液分析-亚硝酸盐 & -- & & & 阴性(-) & 干化学法/SYSMEX \\
3 & GLU & ☆口●尿液分析-葡萄糖 & -- & & & 阴性(-) & 干化学法/SYSMEX \\
4 & SG & ☆口●尿液分析-比重 & 1.024 & & & 1.003~1.030 & 干化学法/SYSMEX \\
5 & BLD & ☆口●尿液分析-潜血 & 2+ & & & 阴性(-) & 干化学法/SYSMEX \\
6 & PRO & ☆口●尿液分析-蛋白质 & -- & & & 阴性(-) & 干化学法/SYSMEX \\
7 & BIL & ☆口●尿液分析-胆红素 & -- & & & 阴性(-) & 干化学法/SYSMEX \\
8 & URO & ☆口●尿液分析-尿胆原 & -- & & & 阴性(-) & 干化学法/SYSMEX \\
9 & KET & ☆口●尿液分析-酮体 & -- & & & 阴性(-) & 干化学法/SYSMEX \\
10 & LEU & ☆口●尿液分析-白细胞 & 2+ & & & 阴性(-) & 干化学法/SYSMEX \\
11 & COL & 尿液分析-颜色 & 稍黄色 & & & 黄色 & 干化学法/SYSMEX \\
12 & TURB & 尿液分析-浊度 & 清晰 & & & 清晰 & 干化学法/SYSMEX \\
13 & WBC & 尿液-白细胞UF & 34.1 & ↑ & /ul & 0.0~30.0 & 流式计数法/SYSMEX \\
14 & RBC & 尿液-红细胞UF & 8.7 & & /ul & 0.0~25.0 & 流式计数法/SYSMEX \\
15 & EC & 尿液-上皮细胞UF & 19.5 & ↑ & /ul & 0.0~15.0 & 流式计数法/SYSMEX \\
16 & BACT & 尿液-细菌UF & 191.1 & & /ul & 0.0~6000.0 & 流式计数法/SYSMEX \\
17 & CAST & 尿液-管型UF & 0.00 & & /ul & 0.00~0.70 & 流式计数法/SYSMEX \\
18 & X-TAL & 尿液-结晶UF & 0.1 & & /ul & & 流式计数法/SYSMEX \\
19 & YLC & 尿液-类酵母菌UF & 0.0 & & /ul & & 流式计数法/SYSMEX \\
20 & MUCUS & 尿液-粘液UF & 0.12 & & /ul & & 流式计数法/SYSMEX \\
21 & RBC-Info & 红细胞信息 & 未提示 & & mS/cm & 3.10~39.00 & 流式计数法/SYSMEX \\
22 & CONDCT & 电导率 & 24.70 & & & 阴性(-) & 镜检法 \\
23 & ELS & 其他 & 阴性(-) & & & & \\
\hline
\end{tabular}
2026-08-10 17:23:57,213 INFO     29 [qwen-vl-parser] page=13 table: 30 LaTeX lines (bbox 398-427)
2026-08-10 17:23:57,213 INFO     29 [qwen-vl-parser] page=13 table: 30 sections
2026-08-10 17:23:57,464 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2147536, prompt_len=764
2026-08-10 17:23:58,855 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2026-02-12"}
```
2026-08-10 17:23:58,856 INFO     29 [qwen-vl-parser] page=14 classify=table report_date=2026-02-12
2026-08-10 17:23:58,866 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2147536, prompt_len=756
2026-08-10 17:24:07,415 INFO     29 [qwen-vl-parser] table API response (len=1664):
\begin{tabular}{cccccccc}
\hline
序号 & & & 结果 & 提示 & 单位 & 参考区间 & 检验方法/检测系统 \\
\hline
1 & ALT & ☆口● 血清丙氨酸氨基转移酶测定 & 41.0 & ↑ & U/L & 7.0~40.0 & 乳酸脱氢酶法/贝克曼 \\
2 & AST & ☆口● 血清天门冬氨酸氨基转移酶测定 & 56.3 & ↑ & U/L & 13.0~35.0 & MDH法/贝克曼 \\
3 & AST/ALT & AST/ALT & 1.37 & & & & 计算法 \\
4 & LDH & ☆口● 乳酸脱氢酶测定 & 151.4 & & U/L & 120.0~250.0 & 乳酸底物法/贝克曼 \\
5 & TP & ☆口● 总蛋白 & 67.5 & & g/L & 65.0~85.0 & 双缩脲法/贝克曼 \\
6 & ALB & ☆口● 白蛋白 & 37.6 & ↓ & g/L & 40.0~55.0 & 溴甲酚绿法/贝克曼 \\
7 & GLB & & 29.9 & & g/L & 20.0~40.0 & 计算法 \\
8 & A/G & & 1.3 & & & 1.2~2.4 & 计算法 \\
9 & ALP & ☆口● 血清碱性磷酸酶测定 & 117.6 & & U/L & 50.0~135.0 & NPP底物-AMP缓冲液法/贝克曼 \\
10 & TBIL & ☆口● 总胆红素 & 12.2 & & µmol/L & ≤23.0 & 重氮盐法/贝克曼 \\
11 & GLU & ☆口● 葡萄糖测定 & 5.0 & & mmol/L & 3.9~6.1 & 己糖激酶法/贝克曼 \\
12 & UREA & ☆口● 尿素测定 & 5.9 & & mmol/L & 2.6~7.5 & 尿素酶-谷氨酸脱氢酶法/贝克曼 \\
13 & CREA & ☆口● 肌酐测定 & 78.8 & ↑ & µmol/L & 41.0~73.0 & 肌氨酸氧化酶法/贝克曼 \\
14 & UA & ☆口● 尿酸测定 & 211.5 & & µmol/L & 154.7~357.0 & 尿酸酶-过氧化物酶法/贝克曼 \\
15 & K & ☆口● 钾测定 & 4.24 & & mmol/L & 3.50~5.30 & 间接离子选择性电极法/贝克曼 \\
16 & NA & ☆口● 钠测定 & 138.6 & & mmol/L & 137.0~147.0 & 间接离子选择性电极法/贝克曼 \\
17 & CL & ☆口● 氯测定 & 104.2 & & mmol/L & 99.0~110.0 & 间接离子选择性电极法/贝克曼 \\
18 & CA & ☆口● 钙测定 & 2.27 & & mmol/L & 2.11~2.52 & 偶氮砷 III 法/贝克曼 \\
19 & P & ☆口● 磷测定 & 1.37 & & mmol/L & 0.85~1.51 & 磷钼酸盐法/贝克曼 \\
20 & MG & & 0.86 & & mmol/L & 0.75~1.02 & 二甲苯胺蓝法/贝克曼 \\
21 & TG & ☆口● 血清甘油三酯 & 0.84 & & mmol/L & ≤1.70 & GPO-POD法/贝克曼 \\
22 & TCH & ☆口● 血清总胆固醇 & 3.25 & & mmol/L & 3.00~5.70 & 酶法/贝克曼 \\
23 & CK & ☆口● 血清肌酸激酶 & 204 & ↑ & U/L & 40~200 & 酶偶联法/贝克曼 \\
24 & LPS & & 28.3 & & U/L & <67.0 & 色原底物法/贝克曼 \\
25 & AMY & ☆● 淀粉酶 & 55 & & U/L & 35~135 & PNP-G7底物法/贝克曼 \\
\hline
\end{tabular}
2026-08-10 17:24:07,417 INFO     29 [qwen-vl-parser] page=14 table: 32 LaTeX lines (bbox 428-459)
2026-08-10 17:24:07,418 INFO     29 [qwen-vl-parser] page=14 table: 32 sections
2026-08-10 17:24:07,517 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:24:07.517+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 80, "failed": 0, "current": {"15f63a1a94e011f1bd9827cf206dfa2d": {"id": "15f63a1a94e011f1bd9827cf206dfa2d", "doc_id": "15bf5b9494e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "size": 6574298, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786382558729, "task_type": "dataflow", "root_trace_id": "e45d0687fc994f25a61430b755af4825", "root_traceparent": "00-e45d0687fc994f25a61430b755af4825-4f140d87c9e2cd09-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:24:07,708 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2764074, prompt_len=764
2026-08-10 17:24:11,324 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2026-02-12"}
```
2026-08-10 17:24:11,325 INFO     29 [qwen-vl-parser] page=15 classify=table report_date=2026-02-12
2026-08-10 17:24:11,346 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2764074, prompt_len=756
2026-08-10 17:24:20,089 INFO     29 [qwen-vl-parser] table API response (len=1684):
\begin{tabular}{cccccccc}
\hline
序号 & & 检验项目 & 结果 & 提示 & 单位 & 参考区间 & 检验方法/检测系统 \\
\hline
1 & WBC & ☆口● 白细胞计数 & 4.35 & & *10^9/L & 3.50~9.50 & 核酸荧光染色法/SYSMEX \\
2 & Neut\% & 中性粒细胞百分数 & 65.1 & & \% & 40.0~75.0 & 核酸荧光染色法/SYSMEX \\
3 & Lymph\% & 淋巴细胞百分数 & 23.2 & & \% & 20.0~50.0 & 核酸荧光染色法/SYSMEX \\
4 & Mono\% & 单核细胞百分数 & 7.4 & & \% & 3.0~10.0 & 核酸荧光染色法/SYSMEX \\
5 & Eos\% & 嗜酸性粒细胞百分数 & 3.4 & & \% & 0.4~8.0 & 核酸荧光染色法/SYSMEX \\
6 & Baso\% & 嗜碱性粒细胞百分数 & 0.9 & & \% & 0.0~1.0 & 核酸荧光染色法/SYSMEX \\
7 & Neut\# & 中性粒细胞绝对值 & 2.83 & & *10^9/L & 1.80~6.30 & 核酸荧光染色法/SYSMEX \\
8 & Lymph\# & 淋巴细胞绝对值 & 1.01 & ↓ & *10^9/L & 1.10~3.20 & 核酸荧光染色法/SYSMEX \\
9 & Mono\# & 单核细胞绝对值 & 0.32 & & *10^9/L & 0.10~0.60 & 核酸荧光染色法/SYSMEX \\
10 & Eos\# & 嗜酸性粒细胞绝对值 & 0.15 & & *10^9/L & 0.02~0.52 & 核酸荧光染色法/SYSMEX \\
11 & Baso\# & 嗜碱性粒细胞绝对值 & 0.04 & & *10^9/L & 0.00~0.06 & 核酸荧光染色法/SYSMEX \\
12 & RBC & ☆口● 红细胞计数 & 4.10 & & *10^12/L & 3.80~5.10 & 电阻抗法/SYSMEX \\
13 & Hb & ☆口● 血红蛋白 & 124 & & g/L & 115~150 & SLS-血红蛋白法/SYSMEX \\
14 & Hct & ☆口● 红细胞比容 & 0.39 & & L/L & 0.35~0.45 & 电阻信号加权法/SYSMEX \\
15 & MCV & ☆口● 平均红细胞容积 & 94.1 & & fL & 82.0~100.0 & 计算法 \\
16 & MCH & ☆口● 平均红细胞血红蛋白量 & 30.2 & & pg & 27.0~34.0 & 计算法 \\
17 & MCHC & ☆口● 平均红细胞血红蛋白浓度 & 321 & & g/L & 316~354 & 计算法 \\
18 & RDW-SD & 红细胞分布宽度-标准差 & 57.1 & ↑ & fL & 41.9~53.9 & 计算法 \\
19 & RDW-CV & 红细胞分布宽度-变异系数 & 16.8 & ↑ & \% & 12.1~15.2 & 计算法 \\
20 & PLT & ☆口● 血小板计数 & 175 & & *10^9/L & 125~350 & 电阻抗法/SYSMEX \\
21 & PDW & 血小板体积分布宽度 & 12.9 & & fL & 9.5~15.2 & 计算法 \\
22 & MPV & 血小板平均体积 & 11.2 & & fL & 9.2~12.1 & 计算法 \\
23 & PCT & 血小板压积 & 0.20 & & \% & 0.19~0.40 & 电阻信号加权法/SYSMEX \\
24 & P-LCR & 大血小板比率 & 33.9 & & \% & 19.6~42.6 & 计算法 \\
\hline
\end{tabular}
2026-08-10 17:24:20,090 INFO     29 [qwen-vl-parser] page=15 table: 31 LaTeX lines (bbox 460-490)
2026-08-10 17:24:20,090 INFO     29 [qwen-vl-parser] page=15 table: 31 sections
2026-08-10 17:24:20,090 INFO     29 [qwen-vl-parser] parse_pdf done: 491 sections from 15 pages.
2026-08-10 17:24:20,101 INFO     29 Close text detector.
2026-08-10 17:24:20,499 INFO     29 Close text recognizer.
2026-08-10 17:24:20,908 INFO     29 Close recognizer.
2026-08-10 17:24:21,296 INFO     29 Close recognizer.
2026-08-10 17:24:21,922 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 17:24:21,922 INFO     29 [Trace] task=15f63a1a | doc=06-临沂人民-LSPI，后线肺癌，方穹招募.pdf | Parser:MedLink | outputs={"html": "", "json": "491 items", "markdown": "", "text": "", "name": "06-临沂人民-LSPI，后线肺癌，方穹招募.pdf", "output_format": "json"}
2026-08-10 17:24:21,923 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 17:24:21,952 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:24:21,952 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 患者 LSPI 治疗史 女 60 岁 山西 肺腺癌 EGFR19del T790M\n[BBOX-1] 20 年 8 月确诊肺腺癌\n[BBOX-2] 20 年 8 月-25 年 10 月 吉非替尼 PD\n[BBOX-3] 25 年 11 月-26 年 3月 LHX43联合斯鲁利单抗临床项目 PD\n[BBOX-4] 进展：新发肝转移\n[BBOX-5] 彩色病理图文报告\n[BBOX-6] 姓名：\n[BBOX-7] 性别：女\n[BBOX-8] 年龄：59岁\n[BBOX-9] 收到日期：2025-10-24\n[BBOX-10] 送检医院：本院\n[BBOX-11] 送检科室：肺病科\n[BBOX-12] 住院号：\n[BBOX-13] 送检医生：0117\n[BBOX-14] 标本名称：\n[BBOX-15] 蜡块数：1\n[BBOX-16] 特征图像：\n[BBOX-17] 大体描述：\n[BBOX-18] (右肺)穿刺组织3条，长0.2-0.4CM,直径0.1CM。\n[BBOX-19] 病理诊断：\n[BBOX-20] (右肺)穿刺玻变的纤维组织中可见少许癌巢浸润，结合免疫组化符合：肺腺癌，\n[BBOX-21] 请结合临床及其它检查综合判断。\n[BBOX-22] 免疫组化：CK(+)CK7(+)TTF-1(+)Napsin-A(+)P63(-)P40(-)Syn(-)INSM-1(-)Ki-67\n[BBOX-23] (+约20%)BRG1(+)。\n[BBOX-24] 报告医生：张瑜\n[BBOX-25] 审核医生：梁晓霞\n[BBOX-26] 1.注：此结果仅针对本次送检样本，仅供临床医生参考。如有疑问，请于7个工作日内与病理科联系。报告日期：2025-10-28\n[BBOX-27] 2.本报告医师签名有效。\n[BBOX-28] 3.本报告电子版仅供参考，请以纸质报告为准。\n[BBOX-29] 电话：\n[BBOX-30] CT检查报告单\n[BBOX-31] 患者编号:\n[BBOX-32] 扫描日期: 1/13/2026\n[BBOX-33] 姓名:\n[BBOX-34] 性别:女\n[BBOX-35] 年龄:59岁科别:\n[BBOX-36] 住院号:\n[BBOX-37] 扫描设备:SIEMENS_CT\n[BBOX-38] 扫描方法:平扫+增强12张\n[BBOX-39] 药品:碘普罗胺注射液\n[BBOX-40] 100ml\n[BBOX-41] 药品处理方式:静脉+静脉留置+高压注射\n[BBOX-42] 检查项目:上腹+下腹+盆腔+胸部(平扫+增强)\n[BBOX-43] 扫描所见:\n[BBOX-44] 参考2025-11-21胸部CT,所见如下:\n[BBOX-45] 1.右肺可见巨大不规则肿块,病变范围较广,累及右全肺,增强扫描不均匀强化,较前\n[BBOX-46] 局部略缩小;余双肺见多发结节影,部分内可见空泡,最大径约2cm,较前部分略缩\n[BBOX-47] 小。\n[BBOX-48] 2.右侧腋窝、纵隔及右肺门见增大淋巴结,最大短径约1.5cm,不均匀强化。考虑MT,\n[BBOX-49] 右侧腋窝淋巴结较前缩小,余大致同前。右侧心隔角淋巴结较前增大,短径约0.6cm。\n[BBOX-50] 3.心影不大,心包少量积液同前。\n[BBOX-51] 4.右侧胸膜不均匀增厚,考虑MT,伴少量积液,同前。\n[BBOX-52] 5.肝脏大小形态尚可,肝内散在低密度结节,较大径约2.3cm,大部分界清,增强扫描\n[BBOX-53] 未见明显强化,部分界欠清,同前相仿。\n[BBOX-54] 6.双肾多发囊肿,较大径约0.4cm,同前。\n[BBOX-55] 7.脾脏见稍低密度结节,较大径约0.6cm,边界欠清,边缘似有强化,同前相仿。\n[BBOX-56] 8.胰腺、双侧肾上腺未见明显异常密度影。\n[BBOX-57] 9.腹膜后见小淋巴结显示,最大短径约0.4cm,大致同前。\n[BBOX-58] 10.膀胱充盈尚可,壁未见明显增厚。\n[BBOX-59] 11.双侧附件区见致密影同前。子宫大小形态尚可,子宫肌层强化欠均匀,同前相仿,\n[BBOX-60] 请结合临床。盆腔少量积液较前增多。\n[BBOX-61] 12.双侧髂血管及腹股沟区未见明显增大淋巴结。\n[BBOX-62] 13.骨窗部分肋骨多发斑片状密度增高影,周围软组织增厚,增强后明显强化。考虑\n[BBOX-63] MT,大致同前。\n[BBOX-64] 印象:\n[BBOX-65] 报告者:王二娟\n[BBOX-66] 审核医师: 何晶晶\n[BBOX-67] 日期:1/13/2026 2:11:3\n[BBOX-68] 本报告仅供临床医师参考,不作为法律依据。妥善保管,遗失不补。\n[BBOX-69] CT检查报告单\n[BBOX-70] 患者编号:\n[BBOX-71] 放射编号:\n[BBOX-72] 扫描日期:2/26/2026\n[BBOX-73] 姓名:\n[BBOX-74] 性别:女\n[BBOX-75] 年龄:59岁科别:\n[BBOX-76] 住院号:\n[BBOX-77] 扫描设备:SIEMENS_CT\n[BBOX-78] 扫描方法:平扫+增强12张\n[BBOX-79] 药品:碘普罗胺注射液\n[BBOX-80] 100ml\n[BBOX-81] 药品处理方式:静脉+静脉留置+高压注射\n[BBOX-82] 检查项目:上腹+下腹+盆腔+胸部(平扫+增强)\n[BBOX-83] 检查所见:\n[BBOX-84] 参阅2026-01-13胸部CT前片,所见如下:\n[BBOX-85] 1.右肺可见巨大不规则肿块,病变范围较广,累及右全肺,增强扫描不均匀强化,较前\n[BBOX-86] 局部增大(8-31较原片7-31);余双肺见多发结节影,部分内可见空泡,最大径约\n[BBOX-87] 2cm,较前基本相仿。\n[BBOX-88] 2.右侧腋窝、纵隔及右肺门见增大淋巴结,最大短径约1.5cm,增强扫描呈不均匀强\n[BBOX-89] 化,考虑MT,大致同前。右侧心隔角可见稍大淋巴结,短径约0.6cm,同前相仿。\n[BBOX-90] 3.心影不大,心包少量积液同前。\n[BBOX-91] 4.右侧胸膜不均匀增厚,考虑MT,伴少量积液,同前。\n[BBOX-92] 5.肝脏大小形态尚可,肝内散在低密度结节,较大径约2.3cm,大部分界清,增强扫描\n[BBOX-93] 未见明显强化,部分考虑囊肿,部分不典型,同前相仿。\n[BBOX-94] 6.肝内新增稍低密度结节影,较大者位于肝S6段,径约1.7cm,增强扫描呈轻度强化,\n[BBOX-95] MT不除外,建议MRI检查。\n[BBOX-96] 7.双肾多发囊肿,较大径约0.4cm,同前。脾脏见稍低密度结节,较大径约0.6cm,边界\n[BBOX-97] 欠清,边缘似有强化,同前相仿。\n[BBOX-98] 8.胰腺、双侧肾上腺未见明显异常密度影。\n[BBOX-99] 9.腹膜后见小淋巴结显示,最大短径约0.4cm,大致同前。\n[BBOX-100] 10.膀胱充盈尚可,壁未见明显增厚。\n[BBOX-101] 11.双侧附件区见致密影同前。子宫大小形态尚可,子宫肌层强化欠均匀,同前相仿,\n[BBOX-102] 请结合临床。盆腔少量积液同前。\n[BBOX-103] 12.双侧髂血管及腹股沟区未见明显增大淋巴结。\n[BBOX-104] 13.骨窗:部分肋骨多发斑片状密度增高影,周围软组织增厚,增强后明显强化,考虑\n[BBOX-105] MT,大致同前。骶管内囊性灶,同前。\n[BBOX-106] 检查者:武康\n[BBOX-107] 报告者:杨东宇审核医师:侯可\n[BBOX-108] 日期:2/26/2026 3:00:48\n[BBOX-109] 本报告仅供临床医师参考,不作为法律依据。妥善保管,遗失不补。\n[BBOX-110] 2:11:34 PM\n[BBOX-111] 科室：呼吸与危重症医学科 姓名：\n[BBOX-112] 出院记录\n[BBOX-113] 女，59岁，主因“确诊右肺腺癌5年”于2025-10-20入院。于\n[BBOX-114] 2025年10月29日出院，住院天数：9天。\n[BBOX-115] 入院情况：患者于2020年8月因咳嗽，咳痰伴右侧胸痛于北京市丰台中西医结合医院\n[BBOX-116] 行胸部CT示：右肺门旁软组织团块影，考虑癌可能；8月31日于我院住院治疗，期间完善\n[BBOX-117] 支气管镜检查，病理结果示：符合浸润性肺腺癌；基因检测示：EGFR Exon21-L858R突变（\n[BBOX-118] 突变比例43.34%），EGFR Exon19缺失突变（突变比例55.81%），KRAS突变（突变比例\n[BBOX-119] 27.72%）；予口服吉非替尼片（伊瑞可）靶向治疗至今，2021年1月复查提示病情稳定，此后\n[BBOX-120] 患者未规律复查。2023年7月31日于我院住院复查，复查提示病情进展，考虑当前靶向药\n[BBOX-121] 耐药，建议患者重新穿刺行基因检查，患者考虑后拒绝，要求继续服药治疗后出院。现患\n[BBOX-122] 者为求全面复查及中西医结合诊治入院。入院症见：神志清，精神可，偶有咳嗽，干咳少\n[BBOX-123] 痰，活动后稍有气喘，口苦，纳食可，夜眠可，二便正常。舌质暗红，苔薄黄，脉弦滑。\n[BBOX-124] 入院诊断：\n[BBOX-125] 中医诊断：肺癌\n[BBOX-126] 痰瘀互结\n[BBOX-127] 西医诊断：右肺腺癌 T2aN2M1a IV期/双肺多发转移/淋巴结多发转移/右侧胸膜\n[BBOX-128] 转移/脑转移？/靶向治疗后，肝囊肿，营养不良性贫血，脂肪肝\n[BBOX-129] 诊疗经过：入院完善相关检查，指导治疗。化验结果回报：血常规+C反应蛋白：白\n[BBOX-130] 细胞计数[WBC]4.810~9/L，红细胞计数[RBC]4.5410^12/L，血红蛋白量[HGB]127.0g/L，\n[BBOX-131] 红细胞平均血红蛋白浓度[MCHC]314.0g/L，淋巴细胞绝对值[LY#]1.0310^9/L，C-反应\n[BBOX-132] 蛋白[CRP]1.98mg/L。免疫球蛋白E[IgE]8.80IU/mL。肝肾功：白蛋白[ALB]36g/L，高密度\n[BBOX-133] 脂蛋白胆固醇[HDL-C]0.92mmol/L，二氧化碳结合力[CO2CP]28.80mmol/L，总蛋白[TP]\n[BBOX-134] 60.7g/L，①肾小球滤过率估算[eGFR]84.2ml/min，②肾小球滤过率估算[eGFR]\n[BBOX-135] 80.3ml/min。肿瘤标志物示：神经元特异性烯醇化酶[NSE]34.3ng/mL，细胞角蛋白19片段\n[BBOX-136] [CYFRA21-1]11.50ng/mL。甲功示：抗甲状腺过氧化物酶抗体[Anti-TPO]814.00IU/ml。细\n[BBOX-137] 胞因子测定、心肌酶谱+C反应蛋白、凝血+D二聚体未见明显异常。心电图示：窦性心律\n[BBOX-138] 不齐，心电轴不偏，心电图大致正常。过敏源检测未见明显异常。胸部CT回报：1.符合右\n[BBOX-139] 肺ca征像，包绕邻近血管；2.双肺多发结节，考虑MT；3.纵膈、右肺肺门及右侧腋窝淋巴\n[BBOX-140] 结MT；4.右侧胸膜不均匀增厚，MT可能性大；5.右侧7、8测前肋MT伴软组织肿块形成、右\n[BBOX-141] 侧胸壁增厚；6.所示肝右叶多发低密度影；脾内稍低密度灶；右肾小囊肿可能大；右侧肾\n[BBOX-142] 上腺稍增粗，请结合腹部检查。请结合临床及原片，治疗后复查。脑MRI回报：1.右侧脑\n[BBOX-143] 室前角旁异常信号，结合病史考虑MT，请结合临床复查；2.左侧上颌窦炎。气管镜检查：\n[BBOX-144] 右肺下叶外压性闭塞/支气管镜下炎症性改变。心脏彩超回报：心脏形态结构及功能未见明\n[BBOX-145] 电话：\n[BBOX-146] 备注\n[BBOX-147] 科室：呼吸与危重症医学科 姓名：\n[BBOX-148] 显异常。腹部彩超回报：肝囊肿；胆囊张力高；胰脾双肾未见明显异常。淋巴结彩超回\n[BBOX-149] 报：右侧锁骨区多发肿大淋巴结，MT；双侧腋窝肿大淋巴结，MT。双侧腹股沟区及腹盆腔\n[BBOX-150] 探查未见明显异常肿大淋巴结。病理报告（202510924）：（右肺支气管镜活检组织）送\n[BBOX-151] 检组织被覆鳞状上皮呈慢性炎改变；免疫组化：P40(+)P53(低表达)K1-67(+约10%)。液\n[BBOX-152] 基细胞学检查（Y252882）：（右肺肺泡灌洗液）支气管上皮细胞，炎细胞，个别非典型\n[BBOX-153] 细胞，建议临床进一步检查。全身骨扫描：右侧第7、8侧肋局部及右侧第9肋后肋局部骨\n[BBOX-154] 质代谢增高，结合脏器断层显像，考虑MT，与2023-8-21日片对比新发；右侧第4-6前侧肋\n[BBOX-155] 局部骨质代谢轻度增高，建议3个月复查；L4-5左侧椎小关节退行性改变，较前未见明显\n[BBOX-156] 变化；双侧膝关节骨质代谢增高，考虑骨关节炎性改变。病理图文报告（10239191）：（\n[BBOX-157] 右肺）穿刺波变的纤维组织中可见少许癌巢浸润，结合免疫组化符合：肺腺癌，请结合临\n[BBOX-158] 床及其他检查综合判断。免疫组化：CK(+)CK7(+)TTF-1(+)Napsin-A(+)P63(-)P40(-)Syn(\n[BBOX-159] 一)INSM-1(-)Ki-67(+约20%)BRG1(+)。予抑酸护胃、中药抗肿瘤，气道雾化，氧疗及中医\n[BBOX-160] 外治法、中医辨证论治等中西医综合治疗。于10月24日行CT引导下肺穿刺活检以明确病\n[BBOX-161] 理。\n[BBOX-162] 出院情况：患者神志清，精神可，偶有咳嗽减轻，干咳少痰，活动后稍有气喘，口\n[BBOX-163] 苦，纳食可，夜眠可，二便正常。舌质暗红，苔薄黄，脉弦滑。查体：双肺呼吸音清，未\n[BBOX-164] 闻及明显干湿性啰音，未闻及捻发音，胸部摩擦音。患者症状好转，要求出院于家中等待\n[BBOX-165] 基因检测结果，请示上级医师后，准予出院。\n[BBOX-166] 出院诊断：\n[BBOX-167] 中医诊断：肺癌\n[BBOX-168] 痰瘀互结\n[BBOX-169] 西医诊断：右肺腺癌 T2aN2M1a IV期/双肺多发转移/淋巴结多发转移/右侧胸\n[BBOX-170] 膜转移/脑转移/骨转移/靶向治疗后，肝囊肿，营养不良性贫血，脂肪肝\n[BBOX-171] 出院医嘱：1.院外规律用药，中草药日一剂，定期复诊，不适随诊；2.定期复查胸部\n[BBOX-172] CT、肺功能；3.加强营养，注意保暖，避免感冒；4.做基因检测确定患者基因突变类型。\n[BBOX-173] 中医调护：避风寒，慎起居，节饮食，畅情志。\n[BBOX-174] 签名：孟丽红\n[BBOX-175] 电话：\n[BBOX-176] 科室：呼吸内科\n[BBOX-177] 姓名：\n[BBOX-178] 门诊病历号：\n[BBOX-179] [初诊病历记录(门诊放化疗患者专用)]\n[BBOX-180] 就诊时间：2026年02月27日10时50分\n[BBOX-181] 科别：呼吸内科\n[BBOX-182] 主诉：确诊右肺腺癌5+年，临床试验中\n[BBOX-183] 现病史：患者于2020-8开始出现咳嗽，咳痰伴右侧胸痛，就诊于\n[BBOX-184] 完善相关检查，\n[BBOX-185] 诊断：右肺腺癌，双肺多发转移，（具体转移不详）突变类型 Exon21-L858R突变，Exon19缺失突\n[BBOX-186] 变，KRAS突变，一直维持吉非替尼治疗。2025-11复查病情病情进展，PFS1：63个月。诊断：右肺\n[BBOX-187] 腺癌（驱动基因阴性） 右肺门、纵隔及右侧腋窝多发淋巴结转移 双肺多发转移 右侧胸膜转移\n[BBOX-188] 肋骨转移。受试者于2025年11月11日签署知情同意书，自愿参加一项评估HLX43（抗PD-L1的ADC）\n[BBOX-189] 联合斯鲁利单抗（抗PD-1人源化单克隆抗体注射液）的晚期/转移性实体瘤患者中的安全性、耐受\n[BBOX-190] 性和有效性的Ib/II期临床研究（V3.0 2025年08月15日），2025年12月2给予C1D1治疗，2025年12\n[BBOX-191] 月24给予C2D1治疗，2026年1月14日给予C3D1治疗，2026年2月5日给予C4D1治疗。现患者无特殊不\n[BBOX-192] 适，拟行周期性治疗入院。自发病以来，精神食欲可，大小便无异常，体重未见明显减轻。\n[BBOX-193] 既往史：2020年8月诊断：肝囊肿。否认传染病史，无高血压史，否认糖尿病史，否认心脏病史，\n[BBOX-194] 否认外伤史，否认输血史，预防接种史：不详，否认食物、药物过敏史。\n[BBOX-195] 阳性体征：无\n[BBOX-196] 必要的阴性体征和辅助检查：无\n[BBOX-197] 诊断：1.右肺恶性肿瘤（腺癌）淋巴结继发恶性肿瘤（右肺门、纵膈、右腋窝）胸膜继发性恶性\n[BBOX-198] 肿瘤骨继发恶性肿瘤2.肝囊肿\n[BBOX-199] 治疗意见：入组临床试验治疗。\n[BBOX-200] 医师签名：一式其其\n[BBOX-201] 激活W\n[BBOX-202] 2302.250626\n[BBOX-203] 山\n[BBOX-204] SAMSUNG\n[BBOX-205] E\n[BBOX-206] R\n[BBOX-207] T\n[BBOX-208] Y\n[BBOX-209] U\n[BBOX-210] O\n[BBOX-211] P\n[BBOX-212] D\n[BBOX-213] F\n[BBOX-214] G\n[BBOX-215] H\n[BBOX-216] J\n[BBOX-217] K\n[BBOX-218] L\n[BBOX-219] C\n[BBOX-220] V\n[BBOX-221] B\n[BBOX-222] M\n[BBOX-223] ViewSonic\n[BBOX-224] 7\n[BBOX-225] 8\n[BBOX-226] 4\n[BBOX-227] 方案编号：HLX43HLX10-ST201\n[BBOX-228] 申办方：上海复宏汉霖生物技术股份有限公司\n[BBOX-229] 上海复宏汉霖生物医药有限公司\n[BBOX-230] 生物标志物研究-知情同意书\n[BBOX-231] (可选)\n[BBOX-232] (2.1版，2025年09月28日)\n[BBOX-233] 方案名称：一项评估HLX43（抗PD-L1的ADC）联合斯鲁利单抗（抗PD-1人\n[BBOX-234] 源化单克隆抗体注射液）在晚期/转移性实体瘤患者中的安全性、耐受性和有效\n[BBOX-235] 性的Ib/II期临床研究\n[BBOX-236] 方案编号：HLX43HLX10-ST201\n[BBOX-237] 申办者：上海复宏汉霖生物技术股份有限公司\n[BBOX-238] 上海复宏汉霖生物医药有限公司\n[BBOX-239] 研究中心：\n[BBOX-240] 院\n[BBOX-241] 主要研究者：\n[BBOX-242] 受试者姓名拼音首字母：LSPZ\n[BBOX-243] 受试者筛选编号：\n[BBOX-244] 生物标志物知情同意书_CHN033_V2.1_20250928\n[BBOX-245] 第1页共7页\n[BBOX-246] 安明康\n[BBOX-247] 01 检测概览\n[BBOX-248] Test Overview\n[BBOX-249] 1 送检信息\n[BBOX-250] 基本信息\n[BBOX-251] 姓\n[BBOX-252] 性别：女\n[BBOX-253] 联系方式：\n[BBOX-254] 年龄：59岁\n[BBOX-255] 送检单位：\n[BBOX-256] 山西省中医院\n[BBOX-257] 样本类型：\n[BBOX-258] 外周血、石蜡切片*12\n[BBOX-259] 送检医师：\n[BBOX-260] 样本来源：\n[BBOX-261] 临床诊断：\n[BBOX-262] 膀胱癌\n[BBOX-263] 收样日期：\n[BBOX-264] 2025-10-31\n[BBOX-265] 临床分层：\n[BBOX-266] /\n[BBOX-267] 报告日期：\n[BBOX-268] 2025-11-05\n[BBOX-269] 家族史：\n[BBOX-270] 送检项目：\n[BBOX-271] NGS 50 基因精准套餐\n[BBOX-272] 肿瘤治疗史：\n[BBOX-273] /\n[BBOX-274] 既往基因检测结果：/\n[BBOX-275] 检测项目\n[BBOX-276] 项目介绍\n[BBOX-277] 该产品精选 50 个与肿瘤发生发展和用药治疗密切相关的基因 (含 NTRK1/2/3 融合基因)，采用扩增子建库技术和高通量测序法检测 50 个基因的热点区域，检测变异类型\n[BBOX-278] 包括点突变、插入/缺失、拷贝数变异及基因融合，精准指导肿瘤靶向及化疗用药，筛查主要耐药原因，提供临床试验药物信息。\n[BBOX-279] 检测方法\n[BBOX-280] NGS\n[BBOX-281] 考基因组\n[BBOX-282] GRCh37/hg19\n[BBOX-283] 阳区阜阳北路与北城大道交口创智天地 A6 号楼 (400-801-9858)\n[BBOX-284] 第 1 页/共 31 页\n[BBOX-285] 1.3 检测结果汇总\n[BBOX-286] [基因变异检测结果汇总]\n[BBOX-287] 具有临床意义的位点或热点基因变异：2个（共检出变异：3个）\n[BBOX-288] 基因\n[BBOX-289] 转录本\n[BBOX-290] 检测结果\n[BBOX-291] 突变丰度/拷贝数\n[BBOX-292] EGFR\n[BBOX-293] NM_005228\n[BBOX-294] c.2369C>T (p.T790M)\n[BBOX-295] 6.6%\n[BBOX-296] EGFR\n[BBOX-297] NM_005228\n[BBOX-298] c.2235_2249del (p.E746_A750del)\n[BBOX-299] 24.4%\n[BBOX-300] 注：所有检出基因变异总览详见第2.2节。\n[BBOX-301] [化疗用药相关检测结果汇总]\n[BBOX-302] 检测项目\n[BBOX-303] 检测结果\n[BBOX-304] 结果解读\n[BBOX-305] 化疗药物疗效评估\n[BBOX-306] √ 有效性较高药物：8个\n[BBOX-307] 用药详见2.4节\n[BBOX-308] 化疗药物毒副作用评估\n[BBOX-309] 毒副作用较低药物：3个\n[BBOX-310] 1.4 临床用药提示\n[BBOX-311] 靶向用药提示\n[BBOX-312] 潜在获益药物\n[BBOX-313] [本癌种获批/指南推荐药物]\n[BBOX-314] 潜在耐药药物\n[BBOX-315] [其他癌种获批/临床试验药物]\n[BBOX-316] [本癌种获批/指南收录证据]\n[BBOX-317] [临床研究/其他癌种耐药提\n[BBOX-318] 注：\n[BBOX-319] 1. 优先选择潜在获益药物中\n[BBOX-320] 2. 若样本同时检出敏感突变\n[BBOX-321] 安明康*\n[BBOX-322] 1.4 临床用药提示\n[BBOX-323] 靶向用药提示\n[BBOX-324] 潜在获益药物\n[BBOX-325] [本癌种获批/指南推荐药物]\n[BBOX-326] 阿美替尼、奥希替尼、贝福替尼、依沃西单抗、信迪利单抗+贝伐珠单抗、瑞厄替尼、伏美替尼、瑞齐替尼、厄洛替尼、德达博妥单抗、达可替尼、埃万妥单抗、阿法替尼、埃克替尼、吉非替尼、利厄替尼、厄洛替尼+贝伐珠单抗、芦康沙妥珠单抗、厄洛替尼+雷莫西尤单抗、佐利替尼、埃万妥单抗+兰泽替尼\n[BBOX-327] [其他癌种获批/临床试验药物]\n[BBOX-328] TY-9591、法米替尼+阿美替尼\n[BBOX-329] 潜在耐药药物\n[BBOX-330] [本癌种获批/指南收录证据]\n[BBOX-331] 厄洛替尼、吉非替尼、佐利替尼、阿法替尼、埃克替尼、美凡厄替尼、达可替尼\n[BBOX-332] [临床研究/其他癌种耐药提示]\n[BBOX-333] 无\n[BBOX-334] 注:\n[BBOX-335] 1.优先选择潜在获益药物中本癌种获批/指南推荐药物，表示FDA/NMPA批准或国内外指南推荐用于本癌种的靶向药物;\n[BBOX-336] 2.若样本同时检出敏感突变和耐药突变，用药时请综合考虑，用药循证详见2.3节。用药需遵医嘱，谨慎用药。\n[BBOX-337] 化疗用药提示\n[BBOX-338] 具体分析结果见2.4节。\n[BBOX-339] 安徽省合肥市庐阳区阜阳北路与北城大道交口创智天地A6号楼(400-801-9858)\n[BBOX-340] 第3页/\n[BBOX-341] 武汉思泰得医学检验\n[BBOX-342] 报告\n[BBOX-343] 肿瘤\n[BBOX-344] 2.2基因变异结果总览\n[BBOX-345] [位点变异结果]\n[BBOX-346] 基因\n[BBOX-347] 转录本\n[BBOX-348] 功能区域\n[BBOX-349] 检测结果\n[BBOX-350] APC\n[BBOX-351] NM_000038\n[BBOX-352] exon16\n[BBOX-353] c.4487C>G (p.T1496S)\n[BBOX-354] EGFR\n[BBOX-355] NM_005228\n[BBOX-356] exon19\n[BBOX-357] c.2235_2249del (p.E746_A750del)\n[BBOX-358] EGFR\n[BBOX-359] NM_005228\n[BBOX-360] exon20\n[BBOX-361] c.2369C>T (p.T790M)\n[BBOX-362] [基因拷贝数结果]\n[BBOX-363] 基因\n[BBOX-364] 染色体位置\n[BBOX-365] 拷贝数\n[BBOX-366] EGFR\n[BBOX-367] chr7\n[BBOX-368] 未扩增\n[BBOX-369] ERBB2\n[BBOX-370] chr17\n[BBOX-371] 未扩增\n[BBOX-372] MET\n[BBOX-373] chr7\n[BBOX-374] 未扩增\n[BBOX-375] FGFR1\n[BBOX-376] chr8\n[BBOX-377] 未扩增\n[BBOX-378] [融合基因结果]\n[BBOX-379] 基因\n[BBOX-380] 检测结果\n[BBOX-381] ALK\n[BBOX-382] 未检出\n[BBOX-383] FGFR1\n[BBOX-384] 未检出\n[BBOX-385] FGFR2\n[BBOX-386] 未检出\n[BBOX-387] NTRK1\n[BBOX-388] 未检出\n[BBOX-389] NTRK2\n[BBOX-390] 未检出\n[BBOX-391] NTRK3\n[BBOX-392] 未检出\n[BBOX-393] RET\n[BBOX-394] 未检出\n[BBOX-395] ROS1\n[BBOX-396] 未检出\n[BBOX-397] 安徽省合肥市庐阳区阜阳北路与北\n[BBOX-398] \\begin{tabular}{ccccccll}\n[BBOX-399] 报告时间: 2026-02-12\n[BBOX-400] \\hline\n[BBOX-401] 序号 & & 检验项目 & 结果 & 提示 & 单位 & 参考区间 & 检验方法/检测系统 \\\\\n[BBOX-402] \\hline\n[BBOX-403] 1 & PH & ☆口●尿液分析-酸碱度 & 5.0 & & & 4.5~8.0 & 干化学法/SYSMEX \\\\\n[BBOX-404] 2 & NIT & ☆口●尿液分析-亚硝酸盐 & -- & & & 阴性(-) & 干化学法/SYSMEX \\\\\n[BBOX-405] 3 & GLU & ☆口●尿液分析-葡萄糖 & -- & & & 阴性(-) & 干化学法/SYSMEX \\\\\n[BBOX-406] 4 & SG & ☆口●尿液分析-比重 & 1.024 & & & 1.003~1.030 & 干化学法/SYSMEX \\\\\n[BBOX-407] 5 & BLD & ☆口●尿液分析-潜血 & 2+ & & & 阴性(-) & 干化学法/SYSMEX \\\\\n[BBOX-408] 6 & PRO & ☆口●尿液分析-蛋白质 & -- & & & 阴性(-) & 干化学法/SYSMEX \\\\\n[BBOX-409] 7 & BIL & ☆口●尿液分析-胆红素 & -- & & & 阴性(-) & 干化学法/SYSMEX \\\\\n[BBOX-410] 8 & URO & ☆口●尿液分析-尿胆原 & -- & & & 阴性(-) & 干化学法/SYSMEX \\\\\n[BBOX-411] 9 & KET & ☆口●尿液分析-酮体 & -- & & & 阴性(-) & 干化学法/SYSMEX \\\\\n[BBOX-412] 10 & LEU & ☆口●尿液分析-白细胞 & 2+ & & & 阴性(-) & 干化学法/SYSMEX \\\\\n[BBOX-413] 11 & COL & 尿液分析-颜色 & 稍黄色 & & & 黄色 & 干化学法/SYSMEX \\\\\n[BBOX-414] 12 & TURB & 尿液分析-浊度 & 清晰 & & & 清晰 & 干化学法/SYSMEX \\\\\n[BBOX-415] 13 & WBC & 尿液-白细胞UF & 34.1 & ↑ & /ul & 0.0~30.0 & 流式计数法/SYSMEX \\\\\n[BBOX-416] 14 & RBC & 尿液-红细胞UF & 8.7 & & /ul & 0.0~25.0 & 流式计数法/SYSMEX \\\\\n[BBOX-417] 15 & EC & 尿液-上皮细胞UF & 19.5 & ↑ & /ul & 0.0~15.0 & 流式计数法/SYSMEX \\\\\n[BBOX-418] 16 & BACT & 尿液-细菌UF & 191.1 & & /ul & 0.0~6000.0 & 流式计数法/SYSMEX \\\\\n[BBOX-419] 17 & CAST & 尿液-管型UF & 0.00 & & /ul & 0.00~0.70 & 流式计数法/SYSMEX \\\\\n[BBOX-420] 18 & X-TAL & 尿液-结晶UF & 0.1 & & /ul & & 流式计数法/SYSMEX \\\\\n[BBOX-421] 19 & YLC & 尿液-类酵母菌UF & 0.0 & & /ul & & 流式计数法/SYSMEX \\\\\n[BBOX-422] 20 & MUCUS & 尿液-粘液UF & 0.12 & & /ul & & 流式计数法/SYSMEX \\\\\n[BBOX-423] 21 & RBC-Info & 红细胞信息 & 未提示 & & mS/cm & 3.10~39.00 & 流式计数法/SYSMEX \\\\\n[BBOX-424] 22 & CONDCT & 电导率 & 24.70 & & & 阴性(-) & 镜检法 \\\\\n[BBOX-425] 23 & ELS & 其他 & 阴性(-) & & & & \\\\\n[BBOX-426] \\hline\n[BBOX-427] \\end{tabular}\n[BBOX-428] \\begin{tabular}{cccccccc}\n[BBOX-429] 报告时间: 2026-02-12\n[BBOX-430] \\hline\n[BBOX-431] 序号 & & & 结果 & 提示 & 单位 & 参考区间 & 检验方法/检测系统 \\\\\n[BBOX-432] \\hline\n[BBOX-433] 1 & ALT & ☆口● 血清丙氨酸氨基转移酶测定 & 41.0 & ↑ & U/L & 7.0~40.0 & 乳酸脱氢酶法/贝克曼 \\\\\n[BBOX-434] 2 & AST & ☆口● 血清天门冬氨酸氨基转移酶测定 & 56.3 & ↑ & U/L & 13.0~35.0 & MDH法/贝克曼 \\\\\n[BBOX-435] 3 & AST/ALT & AST/ALT & 1.37 & & & & 计算法 \\\\\n[BBOX-436] 4 & LDH & ☆口● 乳酸脱氢酶测定 & 151.4 & & U/L & 120.0~250.0 & 乳酸底物法/贝克曼 \\\\\n[BBOX-437] 5 & TP & ☆口● 总蛋白 & 67.5 & & g/L & 65.0~85.0 & 双缩脲法/贝克曼 \\\\\n[BBOX-438] 6 & ALB & ☆口● 白蛋白 & 37.6 & ↓ & g/L & 40.0~55.0 & 溴甲酚绿法/贝克曼 \\\\\n[BBOX-439] 7 & GLB & & 29.9 & & g/L & 20.0~40.0 & 计算法 \\\\\n[BBOX-440] 8 & A/G & & 1.3 & & & 1.2~2.4 & 计算法 \\\\\n[BBOX-441] 9 & ALP & ☆口● 血清碱性磷酸酶测定 & 117.6 & & U/L & 50.0~135.0 & NPP底物-AMP缓冲液法/贝克曼 \\\\\n[BBOX-442] 10 & TBIL & ☆口● 总胆红素 & 12.2 & & µmol/L & ≤23.0 & 重氮盐法/贝克曼 \\\\\n[BBOX-443] 11 & GLU & ☆口● 葡萄糖测定 & 5.0 & & mmol/L & 3.9~6.1 & 己糖激酶法/贝克曼 \\\\\n[BBOX-444] 12 & UREA & ☆口● 尿素测定 & 5.9 & & mmol/L & 2.6~7.5 & 尿素酶-谷氨酸脱氢酶法/贝克曼 \\\\\n[BBOX-445] 13 & CREA & ☆口● 肌酐测定 & 78.8 & ↑ & µmol/L & 41.0~73.0 & 肌氨酸氧化酶法/贝克曼 \\\\\n[BBOX-446] 14 & UA & ☆口● 尿酸测定 & 211.5 & & µmol/L & 154.7~357.0 & 尿酸酶-过氧化物酶法/贝克曼 \\\\\n[BBOX-447] 15 & K & ☆口● 钾测定 & 4.24 & & mmol/L & 3.50~5.30 & 间接离子选择性电极法/贝克曼 \\\\\n[BBOX-448] 16 & NA & ☆口● 钠测定 & 138.6 & & mmol/L & 137.0~147.0 & 间接离子选择性电极法/贝克曼 \\\\\n[BBOX-449] 17 & CL & ☆口● 氯测定 & 104.2 & & mmol/L & 99.0~110.0 & 间接离子选择性电极法/贝克曼 \\\\\n[BBOX-450] 18 & CA & ☆口● 钙测定 & 2.27 & & mmol/L & 2.11~2.52 & 偶氮砷 III 法/贝克曼 \\\\\n[BBOX-451] 19 & P & ☆口● 磷测定 & 1.37 & & mmol/L & 0.85~1.51 & 磷钼酸盐法/贝克曼 \\\\\n[BBOX-452] 20 & MG & & 0.86 & & mmol/L & 0.75~1.02 & 二甲苯胺蓝法/贝克曼 \\\\\n[BBOX-453] 21 & TG & ☆口● 血清甘油三酯 & 0.84 & & mmol/L & ≤1.70 & GPO-POD法/贝克曼 \\\\\n[BBOX-454] 22 & TCH & ☆口● 血清总胆固醇 & 3.25 & & mmol/L & 3.00~5.70 & 酶法/贝克曼 \\\\\n[BBOX-455] 23 & CK & ☆口● 血清肌酸激酶 & 204 & ↑ & U/L & 40~200 & 酶偶联法/贝克曼 \\\\\n[BBOX-456] 24 & LPS & & 28.3 & & U/L & <67.0 & 色原底物法/贝克曼 \\\\\n[BBOX-457] 25 & AMY & ☆● 淀粉酶 & 55 & & U/L & 35~135 & PNP-G7底物法/贝克曼 \\\\\n[BBOX-458] \\hline\n[BBOX-459] \\end{tabular}\n[BBOX-460] \\begin{tabular}{cccccccc}\n[BBOX-461] 报告时间: 2026-02-12\n[BBOX-462] \\hline\n[BBOX-463] 序号 & & 检验项目 & 结果 & 提示 & 单位 & 参考区间 & 检验方法/检测系统 \\\\\n[BBOX-464] \\hline\n[BBOX-465] 1 & WBC & ☆口● 白细胞计数 & 4.35 & & *10^9/L & 3.50~9.50 & 核酸荧光染色法/SYSMEX \\\\\n[BBOX-466] 2 & Neut\\% & 中性粒细胞百分数 & 65.1 & & \\% & 40.0~75.0 & 核酸荧光染色法/SYSMEX \\\\\n[BBOX-467] 3 & Lymph\\% & 淋巴细胞百分数 & 23.2 & & \\% & 20.0~50.0 & 核酸荧光染色法/SYSMEX \\\\\n[BBOX-468] 4 & Mono\\% & 单核细胞百分数 & 7.4 & & \\% & 3.0~10.0 & 核酸荧光染色法/SYSMEX \\\\\n[BBOX-469] 5 & Eos\\% & 嗜酸性粒细胞百分数 & 3.4 & & \\% & 0.4~8.0 & 核酸荧光染色法/SYSMEX \\\\\n[BBOX-470] 6 & Baso\\% & 嗜碱性粒细胞百分数 & 0.9 & & \\% & 0.0~1.0 & 核酸荧光染色法/SYSMEX \\\\\n[BBOX-471] 7 & Neut\\# & 中性粒细胞绝对值 & 2.83 & & *10^9/L & 1.80~6.30 & 核酸荧光染色法/SYSMEX \\\\\n[BBOX-472] 8 & Lymph\\# & 淋巴细胞绝对值 & 1.01 & ↓ & *10^9/L & 1.10~3.20 & 核酸荧光染色法/SYSMEX \\\\\n[BBOX-473] 9 & Mono\\# & 单核细胞绝对值 & 0.32 & & *10^9/L & 0.10~0.60 & 核酸荧光染色法/SYSMEX \\\\\n[BBOX-474] 10 & Eos\\# & 嗜酸性粒细胞绝对值 & 0.15 & & *10^9/L & 0.02~0.52 & 核酸荧光染色法/SYSMEX \\\\\n[BBOX-475] 11 & Baso\\# & 嗜碱性粒细胞绝对值 & 0.04 & & *10^9/L & 0.00~0.06 & 核酸荧光染色法/SYSMEX \\\\\n[BBOX-476] 12 & RBC & ☆口● 红细胞计数 & 4.10 & & *10^12/L & 3.80~5.10 & 电阻抗法/SYSMEX \\\\\n[BBOX-477] 13 & Hb & ☆口● 血红蛋白 & 124 & & g/L & 115~150 & SLS-血红蛋白法/SYSMEX \\\\\n[BBOX-478] 14 & Hct & ☆口● 红细胞比容 & 0.39 & & L/L & 0.35~0.45 & 电阻信号加权法/SYSMEX \\\\\n[BBOX-479] 15 & MCV & ☆口● 平均红细胞容积 & 94.1 & & fL & 82.0~100.0 & 计算法 \\\\\n[BBOX-480] 16 & MCH & ☆口● 平均红细胞血红蛋白量 & 30.2 & & pg & 27.0~34.0 & 计算法 \\\\\n[BBOX-481] 17 & MCHC & ☆口● 平均红细胞血红蛋白浓度 & 321 & & g/L & 316~354 & 计算法 \\\\\n[BBOX-482] 18 & RDW-SD & 红细胞分布宽度-标准差 & 57.1 & ↑ & fL & 41.9~53.9 & 计算法 \\\\\n[BBOX-483] 19 & RDW-CV & 红细胞分布宽度-变异系数 & 16.8 & ↑ & \\% & 12.1~15.2 & 计算法 \\\\\n[BBOX-484] 20 & PLT & ☆口● 血小板计数 & 175 & & *10^9/L & 125~350 & 电阻抗法/SYSMEX \\\\\n[BBOX-485] 21 & PDW & 血小板体积分布宽度 & 12.9 & & fL & 9.5~15.2 & 计算法 \\\\\n[BBOX-486] 22 & MPV & 血小板平均体积 & 11.2 & & fL & 9.2~12.1 & 计算法 \\\\\n[BBOX-487] 23 & PCT & 血小板压积 & 0.20 & & \\% & 0.19~0.40 & 电阻信号加权法/SYSMEX \\\\\n[BBOX-488] 24 & P-LCR & 大血小板比率 & 33.9 & & \\% & 19.6~42.6 & 计算法 \\\\\n[BBOX-489] \\hline\n[BBOX-490] \\end{tabular}"
  }
]
2026-08-10 17:24:34,068 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:24:34,086 INFO     29 [SmartSplitter] SmartSplitter done: 9 chunks from 9 LLM segments (all bbox_id). Types: {'ExaminationReport': 3, 'DischargeRecord': 1, 'OutpatientRecord': 1, 'LabReport': 4}
2026-08-10 17:24:34,099 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 17:24:34,099 INFO     29 [Trace] task=15f63a1a | doc=06-临沂人民-LSPI，后线肺癌，方穹招募.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "491 items", "markdown": "", "text": "", "name": "06-临沂人民-LSPI，后线肺癌，方穹招募.pdf", "output_format": "chunks", "chunks": "9 items, types={'ExaminationReport': 3, 'DischargeRecord': 1, 'OutpatientRecord': 1, 'LabReport': 4}"}
2026-08-10 17:24:34,099 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 17:24:34,100 INFO     29 [ChunkRouter] Routed 9 chunks into 4 groups: {'chunks_Examination': 3, 'chunks_Discharge': 1, 'chunks_Clinical': 1, 'chunks_LabExam': 4}
2026-08-10 17:24:34,110 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 17:24:34,110 INFO     29 [Trace] task=15f63a1a | doc=06-临沂人民-LSPI，后线肺癌，方穹招募.pdf | ChunkRouter:Router | outputs={"html": "", "json": "491 items", "markdown": "", "text": "", "name": "06-临沂人民-LSPI，后线肺癌，方穹招募.pdf", "output_format": "chunks", "chunks": "9 items, types={'ExaminationReport': 3, 'DischargeRecord': 1, 'OutpatientRecord': 1, 'LabReport': 4}", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Examination\": 3, \"chunks_Discharge\": 1, \"chunks_Clinical\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 17:24:34,110 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 17:24:34,119 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:24:34,119 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:24:34,120 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[8, 9, 10, 11]
2026-08-10 17:24:34,120 INFO     29 [qwen-vl-table] positions ： [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:24:34,239 INFO     29 [qwen-vl-table] page=8, rect=595x842, img=(1654x2339)
2026-08-10 17:24:34,309 INFO     29 [qwen-vl-table] page=9, rect=595x842, img=(1654x2339)
2026-08-10 17:24:34,417 INFO     29 [qwen-vl-table] page=10, rect=595x842, img=(1654x2339)
2026-08-10 17:24:34,531 INFO     29 [qwen-vl-table] page=11, rect=595x842, img=(1654x2339)
2026-08-10 17:24:34,531 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:24:34,532 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 246, \"bbox_end\": 396, \"encounter_dates\": [\"2025-10-31\", \"2025-11-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "安明康\n01 检测概览\nTest Overview\n1 送检信息\n基本信息\n姓\n性别：女\n联系方式：\n年龄：59岁\n送检单位：\n山西省中医院\n样本类型：\n外周血、石蜡切片*12\n送检医师：\n样本来源：\n临床诊断：\n膀胱癌\n收样日期：\n2025-10-31\n临床分层：\n/\n报告日期：\n2025-11-05\n家族史：\n送检项目：\nNGS 50 基因精准套餐\n肿瘤治疗史：\n/\n既往基因检测结果：/\n检测项目\n项目介绍\n该产品精选 50 个与肿瘤发生发展和用药治疗密切相关的基因 (含 NTRK1/2/3 融合基因)，采用扩增子建库技术和高通量测序法检测 50 个基因的热点区域，检测变异类型\n包括点突变、插入/缺失、拷贝数变异及基因融合，精准指导肿瘤靶向及化疗用药，筛查主要耐药原因，提供临床试验药物信息。\n检测方法\nNGS\n考基因组\nGRCh37/hg19",
    "role": "user"
  }
]
2026-08-10 17:24:35,289 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:24:35,289 INFO     29 [qwen-vl-table] page=8 LLM output (len=48):
{
  "report_date": "2025-11-05",
  "items": []
}
2026-08-10 17:24:35,289 WARNING  29 [qwen-vl-table] page=8 no items extracted
2026-08-10 17:24:35,290 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:24:35,290 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 246, \"bbox_end\": 396, \"encounter_dates\": [\"2025-10-31\", \"2025-11-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "阳区阜阳北路与北城大道交口创智天地 A6 号楼 (400-801-9858)\n第 1 页/共 31 页\n1.3 检测结果汇总\n[基因变异检测结果汇总]\n具有临床意义的位点或热点基因变异：2个（共检出变异：3个）\n基因\n转录本\n检测结果\n突变丰度/拷贝数\nEGFR\nNM_005228\nc.2369C>T (p.T790M)\n6.6%\nEGFR\nNM_005228\nc.2235_2249del (p.E746_A750del)\n24.4%\n注：所有检出基因变异总览详见第2.2节。\n[化疗用药相关检测结果汇总]\n检测项目\n检测结果\n结果解读\n化疗药物疗效评估\n√ 有效性较高药物：8个\n用药详见2.4节\n化疗药物毒副作用评估\n毒副作用较低药物：3个\n1.4 临床用药提示\n靶向用药提示\n潜在获益药物\n[本癌种获批/指南推荐药物]\n潜在耐药药物\n[其他癌种获批/临床试验药物]\n[本癌种获批/指南收录证据]\n[临床研究/其他癌种耐药提\n注：\n1. 优先选择潜在获益药物中",
    "role": "user"
  }
]
2026-08-10 17:24:37,031 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:24:37,031 INFO     29 [qwen-vl-table] page=9 LLM output (len=411):
{
  "report_date": null,
  "items": [
    {
      "name": "EGFR c.2369C>T (p.T790M)",
      "item_code": "EGFR",
      "value": "6.6%",
      "unit": "%",
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "EGFR c.2235_2249del (p.E746_A750del)",
      "item_code": "EGFR",
      "value": "24.4%",
      "unit": "%",
      "reference_range": null,
      "abnormal": true
    }
  ]
}
2026-08-10 17:24:37,032 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:24:37,032 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 246, \"bbox_end\": 396, \"encounter_dates\": [\"2025-10-31\", \"2025-11-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "2. 若样本同时检出敏感突变\n安明康*\n1.4 临床用药提示\n靶向用药提示\n潜在获益药物\n[本癌种获批/指南推荐药物]\n阿美替尼、奥希替尼、贝福替尼、依沃西单抗、信迪利单抗+贝伐珠单抗、瑞厄替尼、伏美替尼、瑞齐替尼、厄洛替尼、德达博妥单抗、达可替尼、埃万妥单抗、阿法替尼、埃克替尼、吉非替尼、利厄替尼、厄洛替尼+贝伐珠单抗、芦康沙妥珠单抗、厄洛替尼+雷莫西尤单抗、佐利替尼、埃万妥单抗+兰泽替尼\n[其他癌种获批/临床试验药物]\nTY-9591、法米替尼+阿美替尼\n潜在耐药药物\n[本癌种获批/指南收录证据]\n厄洛替尼、吉非替尼、佐利替尼、阿法替尼、埃克替尼、美凡厄替尼、达可替尼\n[临床研究/其他癌种耐药提示]\n无\n注:\n1.优先选择潜在获益药物中本癌种获批/指南推荐药物，表示FDA/NMPA批准或国内外指南推荐用于本癌种的靶向药物;\n2.若样本同时检出敏感突变和耐药突变，用药时请综合考虑，用药循证详见2.3节。用药需遵医嘱，谨慎用药。\n化疗用药提示\n具体分析结果见2.4节。\n安徽省合肥市庐阳区阜阳北路与北城大道交口创智天地A6号楼(400-801-9858)\n第3页/\n武汉思泰得医学检验\n报告\n肿瘤\n2.2基因变异结果总览\n[位点变异结果]\n基因\n转录本\n功能区域\n检测结果\nAPC\nNM_000038\nexon16\nc.4487C>G (p.T1496S)\nEGFR\nNM_005228\nexon19",
    "role": "user"
  }
]
2026-08-10 17:24:38,711 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:24:38,711 INFO     29 [qwen-vl-table] page=10 LLM output (len=383):
{
  "report_date": null,
  "items": [
    {
      "name": "APC",
      "item_code": null,
      "value": "c.4487C>G (p.T1496S)",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "EGFR",
      "item_code": null,
      "value": "NM_005228 exon19",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    }
  ]
}
2026-08-10 17:24:38,712 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:24:38,712 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 246, \"bbox_end\": 396, \"encounter_dates\": [\"2025-10-31\", \"2025-11-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "c.2235_2249del (p.E746_A750del)\nEGFR\nNM_005228\nexon20\nc.2369C>T (p.T790M)\n[基因拷贝数结果]\n基因\n染色体位置\n拷贝数\nEGFR\nchr7\n未扩增\nERBB2\nchr17\n未扩增\nMET\nchr7\n未扩增\nFGFR1\nchr8\n未扩增\n[融合基因结果]\n基因\n检测结果\nALK\n未检出\nFGFR1\n未检出\nFGFR2\n未检出\nNTRK1\n未检出\nNTRK2\n未检出\nNTRK3\n未检出\nRET\n未检出\nROS1\n未检出",
    "role": "user"
  }
]
2026-08-10 17:24:39,562 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:24:39.561+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 80, "failed": 0, "current": {"15f63a1a94e011f1bd9827cf206dfa2d": {"id": "15f63a1a94e011f1bd9827cf206dfa2d", "doc_id": "15bf5b9494e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "size": 6574298, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786382558729, "task_type": "dataflow", "root_trace_id": "e45d0687fc994f25a61430b755af4825", "root_traceparent": "00-e45d0687fc994f25a61430b755af4825-4f140d87c9e2cd09-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:24:47,656 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:24:47,656 INFO     29 [qwen-vl-table] page=11 LLM output (len=2384):
{
  "report_date": null,
  "items": [
    {
      "name": "EGFR c.2235_2249del (p.E746_A750del)",
      "item_code": null,
      "value": "检出",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "EGFR c.2369C>T (p.T790M)",
      "item_code": null,
      "value": "检出",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "EGFR 基因拷贝数",
      "item_code": "EGFR",
      "value": "未扩增",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "ERBB2 基因拷贝数",
      "item_code": "ERBB2",
      "value": "未扩增",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "MET 基因拷贝数",
      "item_code": "MET",
      "value": "未扩增",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "FGFR1 基因拷贝数",
      "item_code": "FGFR1",
      "value": "未扩增",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "ALK 融合基因",
      "item_code": "ALK",
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "FGFR1 融合基因",
      "item_code": "FGFR1",
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "FGFR2 融合基因",
      "item_code": "FGFR2",
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "NTRK1 融合基因",
      "item_code": "NTRK1",
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "NTRK2 融合基因",
      "item_code": "NTRK2",
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "NTRK3 融合基因",
      "item_code": "NTRK3",
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "RET 融合基因",
      "item_code": "RET",
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "ROS1 融合基因",
      "item_code": "ROS1",
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 17:24:47,657 INFO     29 [qwen-vl-table] coord grouping: {11: 18}
2026-08-10 17:24:47,659 INFO     29 [qwen-vl-table] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1301199, prompt_len=767
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
EGFR c.2369C>T (p.T790M)、EGFR c.2235_2249del (p.E746_A750del)、APC、EGFR、EGFR c.2235_2249del (p.E746_A750del)、EGFR c.2369C>T (p.T790M)、EGFR 基因拷贝数、ERBB2 基因拷贝数、MET 基因拷贝数、FGFR1 基因拷贝数、ALK 融合基因、FGFR1 融合基因、FGFR2 融合基因、NTRK1 融合基因、NTRK2 融合基因、NTRK3 融合基因、RET 融合基因、ROS1 融合基因

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
2026-08-10 17:24:53,901 INFO     29 [qwen-vl-table] coord API raw response (len=1055):
[
	{"text": "EGFR c.2369C>T (p.T790M)", "bbox": [626, 388, 740, 399]},
	{"text": "EGFR c.2235_2249del (p.E746_A750del)", "bbox": [598, 373, 771, 384]},
	{"text": "APC", "bbox": [340, 368, 360, 377]},
	{"text": "EGFR", "bbox": [334, 384, 360, 392]},
	{"text": "EGFR c.2235_2249del (p.E746_A750del)", "bbox": [598, 373, 771, 384]},
	{"text": "EGFR c.2369C>T (p.T790M)", "bbox": [626, 388, 740, 399]},
	{"text": "EGFR 基因拷贝数", "bbox": [365, 450, 393, 459]},
	{"text": "ERBB2 基因拷贝数", "bbox": [362, 482, 392, 490]},
	{"text": "MET 基因拷贝数", "bbox": [363, 500, 386, 507]},
	{"text": "FGFR1 基因拷贝数", "bbox": [356, 516, 387, 524]},
	{"text": "ALK 融合基因", "bbox": [389, 577, 414, 586]},
	{"text": "FGFR1 融合基因", "bbox": [381, 611, 413, 620]},
	{"text": "FGFR2 融合基因", "bbox": [378, 630, 411, 639]},
	{"text": "NTRK1 融合基因", "bbox": [376, 650, 408, 659]},
	{"text": "NTRK2 融合基因", "bbox": [373, 669, 407, 678]},
	{"text": "NTRK3 融合基因", "bbox": [370, 688, 404, 697]},
	{"text": "RET 融合基因", "bbox": [373, 708, 394, 717]},
	{"text": "ROS1 融合基因", "bbox": [367, 727, 394, 737]}
]
2026-08-10 17:24:53,901 INFO     29 [qwen-vl-table] coord API: raw_items=18, valid_items=18, elapsed=6.2s
2026-08-10 17:24:53,902 INFO     29 [qwen-vl-table] coord item[0]: text=EGFR c.2369C>T (p.T790M), bbox=[626, 388, 740, 399]
2026-08-10 17:24:53,902 INFO     29 [qwen-vl-table] coord item[1]: text=EGFR c.2235_2249del (p.E746_A750del), bbox=[598, 373, 771, 384]
2026-08-10 17:24:53,902 INFO     29 [qwen-vl-table] coord item[2]: text=APC, bbox=[340, 368, 360, 377]
2026-08-10 17:24:53,902 INFO     29 [qwen-vl-table] coord item[3]: text=EGFR, bbox=[334, 384, 360, 392]
2026-08-10 17:24:53,902 INFO     29 [qwen-vl-table] coord item[4]: text=EGFR c.2235_2249del (p.E746_A750del), bbox=[598, 373, 771, 384]
2026-08-10 17:24:53,902 INFO     29 [qwen-vl-table] coord item[5]: text=EGFR c.2369C>T (p.T790M), bbox=[626, 388, 740, 399]
2026-08-10 17:24:53,902 INFO     29 [qwen-vl-table] coord item[6]: text=EGFR 基因拷贝数, bbox=[365, 450, 393, 459]
2026-08-10 17:24:53,902 INFO     29 [qwen-vl-table] coord item[7]: text=ERBB2 基因拷贝数, bbox=[362, 482, 392, 490]
2026-08-10 17:24:53,902 INFO     29 [qwen-vl-table] coord item[8]: text=MET 基因拷贝数, bbox=[363, 500, 386, 507]
2026-08-10 17:24:53,902 INFO     29 [qwen-vl-table] coord item[9]: text=FGFR1 基因拷贝数, bbox=[356, 516, 387, 524]
2026-08-10 17:24:53,902 INFO     29 [qwen-vl-table] coord item[10]: text=ALK 融合基因, bbox=[389, 577, 414, 586]
2026-08-10 17:24:53,902 INFO     29 [qwen-vl-table] coord item[11]: text=FGFR1 融合基因, bbox=[381, 611, 413, 620]
2026-08-10 17:24:53,903 INFO     29 [qwen-vl-table] coord item[12]: text=FGFR2 融合基因, bbox=[378, 630, 411, 639]
2026-08-10 17:24:53,903 INFO     29 [qwen-vl-table] coord item[13]: text=NTRK1 融合基因, bbox=[376, 650, 408, 659]
2026-08-10 17:24:53,903 INFO     29 [qwen-vl-table] coord item[14]: text=NTRK2 融合基因, bbox=[373, 669, 407, 678]
2026-08-10 17:24:53,903 INFO     29 [qwen-vl-table] coord item[15]: text=NTRK3 融合基因, bbox=[370, 688, 404, 697]
2026-08-10 17:24:53,903 INFO     29 [qwen-vl-table] coord item[16]: text=RET 融合基因, bbox=[373, 708, 394, 717]
2026-08-10 17:24:53,903 INFO     29 [qwen-vl-table] coord item[17]: text=ROS1 融合基因, bbox=[367, 727, 394, 737]
2026-08-10 17:24:53,903 INFO     29 [qwen-vl-table] page=11 coord: matched 18/18, time=6.2s
2026-08-10 17:24:53,904 INFO     29 [qwen-vl-table] new_positions (18):
[[12, 372.65779235839847, 440.5219909667969, 326.65720947265623, 335.91810974121097], [12, 355.9893927001953, 458.9762905883789, 314.0287091064453, 323.289609375], [12, 202.4019958496094, 214.30799560546876, 309.819208984375, 317.39630920410156], [12, 198.83019592285157, 214.30799560546876, 323.289609375, 330.0248095703125], [12, 355.9893927001953, 458.9762905883789, 314.0287091064453, 323.289609375], [12, 372.65779235839847, 440.5219909667969, 326.65720947265623, 335.91810974121097], [12, 217.2844955444336, 233.95289520263674, 378.8550109863281, 386.4321112060547], [12, 215.4985955810547, 233.35759521484377, 405.79581176757813, 412.53101196289066], [12, 216.09389556884767, 229.78579528808595, 420.95001220703125, 426.8433123779297], [12, 211.92679565429688, 230.38109527587892, 434.42041259765625, 441.1556127929688], [12, 231.57169525146486, 246.45419494628908, 485.77631408691406, 493.3534143066406], [12, 226.8092953491211, 245.8588949584961, 514.4009149169922, 521.9780151367188], [12, 225.0233953857422, 244.66829498291017, 530.3970153808594, 537.974115600586], [12, 223.83279541015625, 242.88239501953126, 547.2350158691406, 554.8121160888672], [12, 222.04689544677734, 242.2870950317383, 563.2311163330079, 570.8082165527344], [12, 220.26099548339846, 240.50119506835938, 579.227216796875, 586.8043170166015], [12, 222.04689544677734, 234.5481951904297, 596.0652172851562, 603.6423175048828], [12, 218.47509552001955, 234.5481951904297, 612.0613177490235, 620.4803179931641]]
2026-08-10 17:24:53,904 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=18, matched=18, pages=4, time=19.8s
2026-08-10 17:24:53,905 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:24:53,908 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:24:53,908 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[12]
2026-08-10 17:24:53,908 INFO     29 [qwen-vl-table] positions ： [[12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:24:54,079 INFO     29 [qwen-vl-table] page=12, rect=595x842, img=(1654x2339)
2026-08-10 17:24:54,080 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:24:54,080 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 398, \"bbox_end\": 427, \"encounter_dates\": [\"2026-02-12\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccll}\n报告时间: 2026-02-12\n\\hline\n序号 & & 检验项目 & 结果 & 提示 & 单位 & 参考区间 & 检验方法/检测系统 \\\\\n\\hline\n1 & PH & ☆口●尿液分析-酸碱度 & 5.0 & & & 4.5~8.0 & 干化学法/SYSMEX \\\\\n2 & NIT & ☆口●尿液分析-亚硝酸盐 & -- & & & 阴性(-) & 干化学法/SYSMEX \\\\\n3 & GLU & ☆口●尿液分析-葡萄糖 & -- & & & 阴性(-) & 干化学法/SYSMEX \\\\\n4 & SG & ☆口●尿液分析-比重 & 1.024 & & & 1.003~1.030 & 干化学法/SYSMEX \\\\\n5 & BLD & ☆口●尿液分析-潜血 & 2+ & & & 阴性(-) & 干化学法/SYSMEX \\\\\n6 & PRO & ☆口●尿液分析-蛋白质 & -- & & & 阴性(-) & 干化学法/SYSMEX \\\\\n7 & BIL & ☆口●尿液分析-胆红素 & -- & & & 阴性(-) & 干化学法/SYSMEX \\\\\n8 & URO & ☆口●尿液分析-尿胆原 & -- & & & 阴性(-) & 干化学法/SYSMEX \\\\\n9 & KET & ☆口●尿液分析-酮体 & -- & & & 阴性(-) & 干化学法/SYSMEX \\\\\n10 & LEU & ☆口●尿液分析-白细胞 & 2+ & & & 阴性(-) & 干化学法/SYSMEX \\\\\n11 & COL & 尿液分析-颜色 & 稍黄色 & & & 黄色 & 干化学法/SYSMEX \\\\\n12 & TURB & 尿液分析-浊度 & 清晰 & & & 清晰 & 干化学法/SYSMEX \\\\\n13 & WBC & 尿液-白细胞UF & 34.1 & ↑ & /ul & 0.0~30.0 & 流式计数法/SYSMEX \\\\\n14 & RBC & 尿液-红细胞UF & 8.7 & & /ul & 0.0~25.0 & 流式计数法/SYSMEX \\\\\n15 & EC & 尿液-上皮细胞UF & 19.5 & ↑ & /ul & 0.0~15.0 & 流式计数法/SYSMEX \\\\\n16 & BACT & 尿液-细菌UF & 191.1 & & /ul & 0.0~6000.0 & 流式计数法/SYSMEX \\\\\n17 & CAST & 尿液-管型UF & 0.00 & & /ul & 0.00~0.70 & 流式计数法/SYSMEX \\\\\n18 & X-TAL & 尿液-结晶UF & 0.1 & & /ul & & 流式计数法/SYSMEX \\\\\n19 & YLC & 尿液-类酵母菌UF & 0.0 & & /ul & & 流式计数法/SYSMEX \\\\\n20 & MUCUS & 尿液-粘液UF & 0.12 & & /ul & & 流式计数法/SYSMEX \\\\\n21 & RBC-Info & 红细胞信息 & 未提示 & & mS/cm & 3.10~39.00 & 流式计数法/SYSMEX \\\\\n22 & CONDCT & 电导率 & 24.70 & & & 阴性(-) & 镜检法 \\\\\n23 & ELS & 其他 & 阴性(-) & & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 17:25:05,716 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:25:05,716 INFO     29 [qwen-vl-table] page=12 LLM output (len=3860):
{
  "report_date": "2026-02-12",
  "items": [
    {
      "name": "尿液分析-酸碱度",
      "item_code": "PH",
      "value": "5.0",
      "unit": null,
      "reference_range": "4.5~8.0",
      "abnormal": false
    },
    {
      "name": "尿液分析-亚硝酸盐",
      "item_code": "NIT",
      "value": "--",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": false
    },
    {
      "name": "尿液分析-葡萄糖",
      "item_code": "GLU",
      "value": "--",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": false
    },
    {
      "name": "尿液分析-比重",
      "item_code": "SG",
      "value": "1.024",
      "unit": null,
      "reference_range": "1.003~1.030",
      "abnormal": false
    },
    {
      "name": "尿液分析-潜血",
      "item_code": "BLD",
      "value": "2+",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": true
    },
    {
      "name": "尿液分析-蛋白质",
      "item_code": "PRO",
      "value": "--",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": false
    },
    {
      "name": "尿液分析-胆红素",
      "item_code": "BIL",
      "value": "--",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": false
    },
    {
      "name": "尿液分析-尿胆原",
      "item_code": "URO",
      "value": "--",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": false
    },
    {
      "name": "尿液分析-酮体",
      "item_code": "KET",
      "value": "--",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": false
    },
    {
      "name": "尿液分析-白细胞",
      "item_code": "LEU",
      "value": "2+",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": true
    },
    {
      "name": "尿液分析-颜色",
      "item_code": "COL",
      "value": "稍黄色",
      "unit": null,
      "reference_range": "黄色",
      "abnormal": false
    },
    {
      "name": "尿液分析-浊度",
      "item_code": "TURB",
      "value": "清晰",
      "unit": null,
      "reference_range": "清晰",
      "abnormal": false
    },
    {
      "name": "尿液-白细胞UF",
      "item_code": "WBC",
      "value": "34.1",
      "unit": "/ul",
      "reference_range": "0.0~30.0",
      "abnormal": true
    },
    {
      "name": "尿液-红细胞UF",
      "item_code": "RBC",
      "value": "8.7",
      "unit": "/ul",
      "reference_range": "0.0~25.0",
      "abnormal": false
    },
    {
      "name": "尿液-上皮细胞UF",
      "item_code": "EC",
      "value": "19.5",
      "unit": "/ul",
      "reference_range": "0.0~15.0",
      "abnormal": true
    },
    {
      "name": "尿液-细菌UF",
      "item_code": "BACT",
      "value": "191.1",
      "unit": "/ul",
      "reference_range": "0.0~6000.0",
      "abnormal": false
    },
    {
      "name": "尿液-管型UF",
      "item_code": "CAST",
      "value": "0.00",
      "unit": "/ul",
      "reference_range": "0.00~0.70",
      "abnormal": false
    },
    {
      "name": "尿液-结晶UF",
      "item_code": "X-TAL",
      "value": "0.1",
      "unit": "/ul",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "尿液-类酵母菌UF",
      "item_code": "YLC",
      "value": "0.0",
      "unit": "/ul",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "尿液-粘液UF",
      "item_code": "MUCUS",
      "value": "0.12",
      "unit": "/ul",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "红细胞信息",
      "item_code": "RBC-Info",
      "value": "未提示",
      "unit": "mS/cm",
      "reference_range": "3.10~39.00",
      "abnormal": false
    },
    {
      "name": "电导率",
      "item_code": "CONDCT",
      "value": "24.70",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": false
    },
    {
      "name": "其他",
      "item_code": "ELS",
      "value": "阴性(-)",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 17:25:05,716 INFO     29 [qwen-vl-table] coord grouping: {12: 23}
2026-08-10 17:25:05,719 INFO     29 [qwen-vl-table] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2231082, prompt_len=693
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
尿液分析-酸碱度、尿液分析-亚硝酸盐、尿液分析-葡萄糖、尿液分析-比重、尿液分析-潜血、尿液分析-蛋白质、尿液分析-胆红素、尿液分析-尿胆原、尿液分析-酮体、尿液分析-白细胞、尿液分析-颜色、尿液分析-浊度、尿液-白细胞UF、尿液-红细胞UF、尿液-上皮细胞UF、尿液-细菌UF、尿液-管型UF、尿液-结晶UF、尿液-类酵母菌UF、尿液-粘液UF、红细胞信息、电导率、其他

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
2026-08-10 17:25:12,631 INFO     29 [qwen-vl-table] coord API raw response (len=1201):
[
	{"text": "尿液分析-酸碱度", "bbox": [271, 222, 390, 235]},
	{"text": "尿液分析-亚硝酸盐", "bbox": [271, 235, 401, 248]},
	{"text": "尿液分析-葡萄糖", "bbox": [271, 248, 390, 260]},
	{"text": "尿液分析-比重", "bbox": [271, 260, 380, 273]},
	{"text": "尿液分析-潜血", "bbox": [271, 273, 380, 286]},
	{"text": "尿液分析-蛋白质", "bbox": [271, 286, 391, 299]},
	{"text": "尿液分析-胆红素", "bbox": [271, 299, 391, 312]},
	{"text": "尿液分析-尿胆原", "bbox": [271, 312, 391, 325]},
	{"text": "尿液分析-酮体", "bbox": [271, 325, 381, 338]},
	{"text": "尿液分析-白细胞", "bbox": [271, 338, 393, 351]},
	{"text": "尿液分析-颜色", "bbox": [308, 351, 383, 364]},
	{"text": "尿液分析-浊度", "bbox": [308, 364, 383, 377]},
	{"text": "尿液-白细胞UF", "bbox": [308, 377, 388, 389]},
	{"text": "尿液-红细胞UF", "bbox": [308, 389, 388, 402]},
	{"text": "尿液-上皮细胞UF", "bbox": [308, 402, 400, 414]},
	{"text": "尿液-细菌UF", "bbox": [308, 414, 377, 427]},
	{"text": "尿液-管型UF", "bbox": [308, 427, 377, 439]},
	{"text": "尿液-结晶UF", "bbox": [308, 439, 377, 452]},
	{"text": "尿液-类酵母菌UF", "bbox": [308, 452, 400, 464]},
	{"text": "尿液-粘液UF", "bbox": [308, 464, 377, 477]},
	{"text": "红细胞信息", "bbox": [308, 477, 369, 489]},
	{"text": "电导率", "bbox": [308, 489, 348, 501]},
	{"text": "其他", "bbox": [308, 501, 338, 513]}
]
2026-08-10 17:25:12,631 INFO     29 [qwen-vl-table] coord API: raw_items=23, valid_items=23, elapsed=6.9s
2026-08-10 17:25:12,631 INFO     29 [qwen-vl-table] coord item[0]: text=尿液分析-酸碱度, bbox=[271, 222, 390, 235]
2026-08-10 17:25:12,631 INFO     29 [qwen-vl-table] coord item[1]: text=尿液分析-亚硝酸盐, bbox=[271, 235, 401, 248]
2026-08-10 17:25:12,632 INFO     29 [qwen-vl-table] coord item[2]: text=尿液分析-葡萄糖, bbox=[271, 248, 390, 260]
2026-08-10 17:25:12,632 INFO     29 [qwen-vl-table] coord item[3]: text=尿液分析-比重, bbox=[271, 260, 380, 273]
2026-08-10 17:25:12,632 INFO     29 [qwen-vl-table] coord item[4]: text=尿液分析-潜血, bbox=[271, 273, 380, 286]
2026-08-10 17:25:12,632 INFO     29 [qwen-vl-table] coord item[5]: text=尿液分析-蛋白质, bbox=[271, 286, 391, 299]
2026-08-10 17:25:12,632 INFO     29 [qwen-vl-table] coord item[6]: text=尿液分析-胆红素, bbox=[271, 299, 391, 312]
2026-08-10 17:25:12,632 INFO     29 [qwen-vl-table] coord item[7]: text=尿液分析-尿胆原, bbox=[271, 312, 391, 325]
2026-08-10 17:25:12,632 INFO     29 [qwen-vl-table] coord item[8]: text=尿液分析-酮体, bbox=[271, 325, 381, 338]
2026-08-10 17:25:12,632 INFO     29 [qwen-vl-table] coord item[9]: text=尿液分析-白细胞, bbox=[271, 338, 393, 351]
2026-08-10 17:25:12,632 INFO     29 [qwen-vl-table] coord item[10]: text=尿液分析-颜色, bbox=[308, 351, 383, 364]
2026-08-10 17:25:12,632 INFO     29 [qwen-vl-table] coord item[11]: text=尿液分析-浊度, bbox=[308, 364, 383, 377]
2026-08-10 17:25:12,632 INFO     29 [qwen-vl-table] coord item[12]: text=尿液-白细胞UF, bbox=[308, 377, 388, 389]
2026-08-10 17:25:12,632 INFO     29 [qwen-vl-table] coord item[13]: text=尿液-红细胞UF, bbox=[308, 389, 388, 402]
2026-08-10 17:25:12,632 INFO     29 [qwen-vl-table] coord item[14]: text=尿液-上皮细胞UF, bbox=[308, 402, 400, 414]
2026-08-10 17:25:12,632 INFO     29 [qwen-vl-table] coord item[15]: text=尿液-细菌UF, bbox=[308, 414, 377, 427]
2026-08-10 17:25:12,633 INFO     29 [qwen-vl-table] coord item[16]: text=尿液-管型UF, bbox=[308, 427, 377, 439]
2026-08-10 17:25:12,633 INFO     29 [qwen-vl-table] coord item[17]: text=尿液-结晶UF, bbox=[308, 439, 377, 452]
2026-08-10 17:25:12,633 INFO     29 [qwen-vl-table] coord item[18]: text=尿液-类酵母菌UF, bbox=[308, 452, 400, 464]
2026-08-10 17:25:12,633 INFO     29 [qwen-vl-table] coord item[19]: text=尿液-粘液UF, bbox=[308, 464, 377, 477]
2026-08-10 17:25:12,633 INFO     29 [qwen-vl-table] coord item[20]: text=红细胞信息, bbox=[308, 477, 369, 489]
2026-08-10 17:25:12,633 INFO     29 [qwen-vl-table] coord item[21]: text=电导率, bbox=[308, 489, 348, 501]
2026-08-10 17:25:12,633 INFO     29 [qwen-vl-table] coord item[22]: text=其他, bbox=[308, 501, 338, 513]
2026-08-10 17:25:12,634 INFO     29 [qwen-vl-table] page=12 coord: matched 23/23, time=6.9s
2026-08-10 17:25:12,634 INFO     29 [qwen-vl-table] new_positions (23):
[[13, 161.32629669189453, 232.16699523925783, 186.90180541992189, 197.84650573730468], [13, 161.32629669189453, 238.71529510498047, 197.84650573730468, 208.7912060546875], [13, 161.32629669189453, 232.16699523925783, 208.7912060546875, 218.89400634765624], [13, 161.32629669189453, 226.21399536132813, 218.89400634765624, 229.83870666503907], [13, 161.32629669189453, 226.21399536132813, 229.83870666503907, 240.7834069824219], [13, 161.32629669189453, 232.7622952270508, 240.7834069824219, 251.7281072998047], [13, 161.32629669189453, 232.7622952270508, 251.7281072998047, 262.6728076171875], [13, 161.32629669189453, 232.7622952270508, 262.6728076171875, 273.6175079345703], [13, 161.32629669189453, 226.8092953491211, 273.6175079345703, 284.5622082519531], [13, 161.32629669189453, 233.95289520263674, 284.5622082519531, 295.50690856933596], [13, 183.35239624023438, 227.99989532470704, 295.50690856933596, 306.45160888671876], [13, 183.35239624023438, 227.99989532470704, 306.45160888671876, 317.39630920410156], [13, 183.35239624023438, 230.9763952636719, 317.39630920410156, 327.4991094970703], [13, 183.35239624023438, 230.9763952636719, 327.4991094970703, 338.4438098144531], [13, 183.35239624023438, 238.1199951171875, 338.4438098144531, 348.5466101074219], [13, 183.35239624023438, 224.42809539794922, 348.5466101074219, 359.4913104248047], [13, 183.35239624023438, 224.42809539794922, 359.4913104248047, 369.59411071777345], [13, 183.35239624023438, 224.42809539794922, 369.59411071777345, 380.53881103515624], [13, 183.35239624023438, 238.1199951171875, 380.53881103515624, 390.641611328125], [13, 183.35239624023438, 224.42809539794922, 390.641611328125, 401.5863116455078], [13, 183.35239624023438, 219.6656954956055, 401.5863116455078, 411.6891119384766], [13, 183.35239624023438, 207.16439575195312, 411.6891119384766, 421.79191223144534], [13, 183.35239624023438, 201.21139587402345, 421.79191223144534, 431.8947125244141]]
2026-08-10 17:25:12,635 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=23, matched=23, pages=1, time=18.7s
2026-08-10 17:25:12,636 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:25:12,637 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:25:12,637 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[13]
2026-08-10 17:25:12,637 INFO     29 [qwen-vl-table] positions ： [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:25:12,816 INFO     29 [qwen-vl-table] page=13, rect=595x842, img=(1654x2339)
2026-08-10 17:25:12,817 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:25:12,817 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 428, \"bbox_end\": 459, \"encounter_dates\": [\"2026-02-12\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccccccc}\n报告时间: 2026-02-12\n\\hline\n序号 & & & 结果 & 提示 & 单位 & 参考区间 & 检验方法/检测系统 \\\\\n\\hline\n1 & ALT & ☆口● 血清丙氨酸氨基转移酶测定 & 41.0 & ↑ & U/L & 7.0~40.0 & 乳酸脱氢酶法/贝克曼 \\\\\n2 & AST & ☆口● 血清天门冬氨酸氨基转移酶测定 & 56.3 & ↑ & U/L & 13.0~35.0 & MDH法/贝克曼 \\\\\n3 & AST/ALT & AST/ALT & 1.37 & & & & 计算法 \\\\\n4 & LDH & ☆口● 乳酸脱氢酶测定 & 151.4 & & U/L & 120.0~250.0 & 乳酸底物法/贝克曼 \\\\\n5 & TP & ☆口● 总蛋白 & 67.5 & & g/L & 65.0~85.0 & 双缩脲法/贝克曼 \\\\\n6 & ALB & ☆口● 白蛋白 & 37.6 & ↓ & g/L & 40.0~55.0 & 溴甲酚绿法/贝克曼 \\\\\n7 & GLB & & 29.9 & & g/L & 20.0~40.0 & 计算法 \\\\\n8 & A/G & & 1.3 & & & 1.2~2.4 & 计算法 \\\\\n9 & ALP & ☆口● 血清碱性磷酸酶测定 & 117.6 & & U/L & 50.0~135.0 & NPP底物-AMP缓冲液法/贝克曼 \\\\\n10 & TBIL & ☆口● 总胆红素 & 12.2 & & µmol/L & ≤23.0 & 重氮盐法/贝克曼 \\\\\n11 & GLU & ☆口● 葡萄糖测定 & 5.0 & & mmol/L & 3.9~6.1 & 己糖激酶法/贝克曼 \\\\\n12 & UREA & ☆口● 尿素测定 & 5.9 & & mmol/L & 2.6~7.5 & 尿素酶-谷氨酸脱氢酶法/贝克曼 \\\\\n13 & CREA & ☆口● 肌酐测定 & 78.8 & ↑ & µmol/L & 41.0~73.0 & 肌氨酸氧化酶法/贝克曼 \\\\\n14 & UA & ☆口● 尿酸测定 & 211.5 & & µmol/L & 154.7~357.0 & 尿酸酶-过氧化物酶法/贝克曼 \\\\\n15 & K & ☆口● 钾测定 & 4.24 & & mmol/L & 3.50~5.30 & 间接离子选择性电极法/贝克曼 \\\\\n16 & NA & ☆口● 钠测定 & 138.6 & & mmol/L & 137.0~147.0 & 间接离子选择性电极法/贝克曼 \\\\\n17 & CL & ☆口● 氯测定 & 104.2 & & mmol/L & 99.0~110.0 & 间接离子选择性电极法/贝克曼 \\\\\n18 & CA & ☆口● 钙测定 & 2.27 & & mmol/L & 2.11~2.52 & 偶氮砷 III 法/贝克曼 \\\\\n19 & P & ☆口● 磷测定 & 1.37 & & mmol/L & 0.85~1.51 & 磷钼酸盐法/贝克曼 \\\\\n20 & MG & & 0.86 & & mmol/L & 0.75~1.02 & 二甲苯胺蓝法/贝克曼 \\\\\n21 & TG & ☆口● 血清甘油三酯 & 0.84 & & mmol/L & ≤1.70 & GPO-POD法/贝克曼 \\\\\n22 & TCH & ☆口● 血清总胆固醇 & 3.25 & & mmol/L & 3.00~5.70 & 酶法/贝克曼 \\\\\n23 & CK & ☆口● 血清肌酸激酶 & 204 & ↑ & U/L & 40~200 & 酶偶联法/贝克曼 \\\\\n24 & LPS & & 28.3 & & U/L & <67.0 & 色原底物法/贝克曼 \\\\\n25 & AMY & ☆● 淀粉酶 & 55 & & U/L & 35~135 & PNP-G7底物法/贝克曼 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 17:25:12,819 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:25:12.818+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 80, "failed": 0, "current": {"15f63a1a94e011f1bd9827cf206dfa2d": {"id": "15f63a1a94e011f1bd9827cf206dfa2d", "doc_id": "15bf5b9494e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "size": 6574298, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786382558729, "task_type": "dataflow", "root_trace_id": "e45d0687fc994f25a61430b755af4825", "root_traceparent": "00-e45d0687fc994f25a61430b755af4825-4f140d87c9e2cd09-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:25:29,054 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:25:29,054 INFO     29 [qwen-vl-table] page=13 LLM output (len=4251):
{
  "report_date": "2026-02-12",
  "items": [
    {
      "name": "血清丙氨酸氨基转移酶测定",
      "item_code": "ALT",
      "value": "41.0",
      "unit": "U/L",
      "reference_range": "7.0~40.0",
      "abnormal": true
    },
    {
      "name": "血清天门冬氨酸氨基转移酶测定",
      "item_code": "AST",
      "value": "56.3",
      "unit": "U/L",
      "reference_range": "13.0~35.0",
      "abnormal": true
    },
    {
      "name": "AST/ALT",
      "item_code": "AST/ALT",
      "value": "1.37",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "乳酸脱氢酶测定",
      "item_code": "LDH",
      "value": "151.4",
      "unit": "U/L",
      "reference_range": "120.0~250.0",
      "abnormal": false
    },
    {
      "name": "总蛋白",
      "item_code": "TP",
      "value": "67.5",
      "unit": "g/L",
      "reference_range": "65.0~85.0",
      "abnormal": false
    },
    {
      "name": "白蛋白",
      "item_code": "ALB",
      "value": "37.6",
      "unit": "g/L",
      "reference_range": "40.0~55.0",
      "abnormal": true
    },
    {
      "name": "球蛋白",
      "item_code": "GLB",
      "value": "29.9",
      "unit": "g/L",
      "reference_range": "20.0~40.0",
      "abnormal": false
    },
    {
      "name": "白球比",
      "item_code": "A/G",
      "value": "1.3",
      "unit": null,
      "reference_range": "1.2~2.4",
      "abnormal": false
    },
    {
      "name": "血清碱性磷酸酶测定",
      "item_code": "ALP",
      "value": "117.6",
      "unit": "U/L",
      "reference_range": "50.0~135.0",
      "abnormal": false
    },
    {
      "name": "总胆红素",
      "item_code": "TBIL",
      "value": "12.2",
      "unit": "µmol/L",
      "reference_range": "≤23.0",
      "abnormal": false
    },
    {
      "name": "葡萄糖测定",
      "item_code": "GLU",
      "value": "5.0",
      "unit": "mmol/L",
      "reference_range": "3.9~6.1",
      "abnormal": false
    },
    {
      "name": "尿素测定",
      "item_code": "UREA",
      "value": "5.9",
      "unit": "mmol/L",
      "reference_range": "2.6~7.5",
      "abnormal": false
    },
    {
      "name": "肌酐测定",
      "item_code": "CREA",
      "value": "78.8",
      "unit": "µmol/L",
      "reference_range": "41.0~73.0",
      "abnormal": true
    },
    {
      "name": "尿酸测定",
      "item_code": "UA",
      "value": "211.5",
      "unit": "µmol/L",
      "reference_range": "154.7~357.0",
      "abnormal": false
    },
    {
      "name": "钾测定",
      "item_code": "K",
      "value": "4.24",
      "unit": "mmol/L",
      "reference_range": "3.50~5.30",
      "abnormal": false
    },
    {
      "name": "钠测定",
      "item_code": "NA",
      "value": "138.6",
      "unit": "mmol/L",
      "reference_range": "137.0~147.0",
      "abnormal": false
    },
    {
      "name": "氯测定",
      "item_code": "CL",
      "value": "104.2",
      "unit": "mmol/L",
      "reference_range": "99.0~110.0",
      "abnormal": false
    },
    {
      "name": "钙测定",
      "item_code": "CA",
      "value": "2.27",
      "unit": "mmol/L",
      "reference_range": "2.11~2.52",
      "abnormal": false
    },
    {
      "name": "磷测定",
      "item_code": "P",
      "value": "1.37",
      "unit": "mmol/L",
      "reference_range": "0.85~1.51",
      "abnormal": false
    },
    {
      "name": "镁测定",
      "item_code": "MG",
      "value": "0.86",
      "unit": "mmol/L",
      "reference_range": "0.75~1.02",
      "abnormal": false
    },
    {
      "name": "血清甘油三酯",
      "item_code": "TG",
      "value": "0.84",
      "unit": "mmol/L",
      "reference_range": "≤1.70",
      "abnormal": false
    },
    {
      "name": "血清总胆固醇",
      "item_code": "TCH",
      "value": "3.25",
      "unit": "mmol/L",
      "reference_range": "3.00~5.70",
      "abnormal": false
    },
    {
      "name": "血清肌酸激酶",
      "item_code": "CK",
      "value": "204",
      "unit": "U/L",
      "reference_range": "40~200",
      "abnormal": true
    },
    {
      "name": "脂蛋白",
      "item_code": "LPS",
      "value": "28.3",
      "unit": "U/L",
      "reference_range": "<67.0",
      "abnormal": false
    },
    {
      "name": "淀粉酶",
      "item_code": "AMY",
      "value": "55",
      "unit": "U/L",
      "reference_range": "35~135",
      "abnormal": false
    }
  ]
}
2026-08-10 17:25:29,055 INFO     29 [qwen-vl-table] coord grouping: {13: 25}
2026-08-10 17:25:29,065 INFO     29 [qwen-vl-table] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2952871, prompt_len=655
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
血清丙氨酸氨基转移酶测定、血清天门冬氨酸氨基转移酶测定、AST/ALT、乳酸脱氢酶测定、总蛋白、白蛋白、球蛋白、白球比、血清碱性磷酸酶测定、总胆红素、葡萄糖测定、尿素测定、肌酐测定、尿酸测定、钾测定、钠测定、氯测定、钙测定、磷测定、镁测定、血清甘油三酯、血清总胆固醇、血清肌酸激酶、脂蛋白、淀粉酶

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
2026-08-10 17:25:36,027 INFO     29 [qwen-vl-table] coord API raw response (len=1251):
[
	{"text": "血清丙氨酸氨基转移酶测定", "bbox": [248, 157, 397, 169]},
	{"text": "血清天门冬氨酸氨基转移酶测定", "bbox": [248, 170, 421, 182]},
	{"text": "AST/ALT", "bbox": [248, 185, 298, 196]},
	{"text": "乳酸脱氢酶测定", "bbox": [248, 199, 339, 210]},
	{"text": "总蛋白", "bbox": [248, 213, 290, 225]},
	{"text": "白蛋白", "bbox": [248, 227, 290, 239]},
	{"text": "球蛋白", "bbox": [248, 241, 316, 253]},
	{"text": "白球比", "bbox": [248, 255, 336, 267]},
	{"text": "血清碱性磷酸酶测定", "bbox": [248, 269, 367, 281]},
	{"text": "总胆红素", "bbox": [248, 284, 307, 296]},
	{"text": "葡萄糖测定", "bbox": [248, 298, 320, 310]},
	{"text": "尿素测定", "bbox": [248, 312, 310, 324]},
	{"text": "肌酐测定", "bbox": [248, 326, 310, 338]},
	{"text": "尿酸测定", "bbox": [248, 340, 310, 352]},
	{"text": "钾测定", "bbox": [248, 354, 300, 366]},
	{"text": "钠测定", "bbox": [248, 368, 300, 380]},
	{"text": "氯测定", "bbox": [248, 382, 300, 394]},
	{"text": "钙测定", "bbox": [248, 396, 300, 408]},
	{"text": "磷测定", "bbox": [248, 409, 300, 421]},
	{"text": "镁测定", "bbox": [248, 423, 305, 435]},
	{"text": "血清甘油三酯", "bbox": [248, 436, 344, 448]},
	{"text": "血清总胆固醇", "bbox": [248, 449, 344, 462]},
	{"text": "血清肌酸激酶", "bbox": [248, 462, 344, 475]},
	{"text": "脂蛋白", "bbox": [248, 475, 358, 488]},
	{"text": "淀粉酶", "bbox": [248, 488, 310, 500]}
]
2026-08-10 17:25:36,027 INFO     29 [qwen-vl-table] coord API: raw_items=25, valid_items=25, elapsed=7.0s
2026-08-10 17:25:36,027 INFO     29 [qwen-vl-table] coord item[0]: text=血清丙氨酸氨基转移酶测定, bbox=[248, 157, 397, 169]
2026-08-10 17:25:36,027 INFO     29 [qwen-vl-table] coord item[1]: text=血清天门冬氨酸氨基转移酶测定, bbox=[248, 170, 421, 182]
2026-08-10 17:25:36,027 INFO     29 [qwen-vl-table] coord item[2]: text=AST/ALT, bbox=[248, 185, 298, 196]
2026-08-10 17:25:36,027 INFO     29 [qwen-vl-table] coord item[3]: text=乳酸脱氢酶测定, bbox=[248, 199, 339, 210]
2026-08-10 17:25:36,027 INFO     29 [qwen-vl-table] coord item[4]: text=总蛋白, bbox=[248, 213, 290, 225]
2026-08-10 17:25:36,027 INFO     29 [qwen-vl-table] coord item[5]: text=白蛋白, bbox=[248, 227, 290, 239]
2026-08-10 17:25:36,027 INFO     29 [qwen-vl-table] coord item[6]: text=球蛋白, bbox=[248, 241, 316, 253]
2026-08-10 17:25:36,027 INFO     29 [qwen-vl-table] coord item[7]: text=白球比, bbox=[248, 255, 336, 267]
2026-08-10 17:25:36,027 INFO     29 [qwen-vl-table] coord item[8]: text=血清碱性磷酸酶测定, bbox=[248, 269, 367, 281]
2026-08-10 17:25:36,027 INFO     29 [qwen-vl-table] coord item[9]: text=总胆红素, bbox=[248, 284, 307, 296]
2026-08-10 17:25:36,028 INFO     29 [qwen-vl-table] coord item[10]: text=葡萄糖测定, bbox=[248, 298, 320, 310]
2026-08-10 17:25:36,028 INFO     29 [qwen-vl-table] coord item[11]: text=尿素测定, bbox=[248, 312, 310, 324]
2026-08-10 17:25:36,028 INFO     29 [qwen-vl-table] coord item[12]: text=肌酐测定, bbox=[248, 326, 310, 338]
2026-08-10 17:25:36,028 INFO     29 [qwen-vl-table] coord item[13]: text=尿酸测定, bbox=[248, 340, 310, 352]
2026-08-10 17:25:36,028 INFO     29 [qwen-vl-table] coord item[14]: text=钾测定, bbox=[248, 354, 300, 366]
2026-08-10 17:25:36,028 INFO     29 [qwen-vl-table] coord item[15]: text=钠测定, bbox=[248, 368, 300, 380]
2026-08-10 17:25:36,028 INFO     29 [qwen-vl-table] coord item[16]: text=氯测定, bbox=[248, 382, 300, 394]
2026-08-10 17:25:36,028 INFO     29 [qwen-vl-table] coord item[17]: text=钙测定, bbox=[248, 396, 300, 408]
2026-08-10 17:25:36,028 INFO     29 [qwen-vl-table] coord item[18]: text=磷测定, bbox=[248, 409, 300, 421]
2026-08-10 17:25:36,028 INFO     29 [qwen-vl-table] coord item[19]: text=镁测定, bbox=[248, 423, 305, 435]
2026-08-10 17:25:36,028 INFO     29 [qwen-vl-table] coord item[20]: text=血清甘油三酯, bbox=[248, 436, 344, 448]
2026-08-10 17:25:36,028 INFO     29 [qwen-vl-table] coord item[21]: text=血清总胆固醇, bbox=[248, 449, 344, 462]
2026-08-10 17:25:36,028 INFO     29 [qwen-vl-table] coord item[22]: text=血清肌酸激酶, bbox=[248, 462, 344, 475]
2026-08-10 17:25:36,028 INFO     29 [qwen-vl-table] coord item[23]: text=脂蛋白, bbox=[248, 475, 358, 488]
2026-08-10 17:25:36,028 INFO     29 [qwen-vl-table] coord item[24]: text=淀粉酶, bbox=[248, 488, 310, 500]
2026-08-10 17:25:36,029 INFO     29 [qwen-vl-table] page=13 coord: matched 25/25, time=7.0s
2026-08-10 17:25:36,029 INFO     29 [qwen-vl-table] new_positions (25):
[[14, 147.63439697265625, 236.3340951538086, 132.17830383300782, 142.28110412597655], [14, 147.63439697265625, 250.62129486083987, 143.12300415039064, 153.22580444335938], [14, 147.63439697265625, 177.39939636230469, 155.75150451660156, 165.01240478515626], [14, 147.63439697265625, 201.80669586181642, 167.53810485839844, 176.79900512695312], [14, 147.63439697265625, 172.63699645996095, 179.32470520019533, 189.42750549316406], [14, 147.63439697265625, 172.63699645996095, 191.11130554199218, 201.21410583496095], [14, 147.63439697265625, 188.11479614257814, 202.89790588378906, 213.00070617675783], [14, 147.63439697265625, 200.0207958984375, 214.68450622558595, 224.7873065185547], [14, 147.63439697265625, 218.47509552001955, 226.47110656738283, 236.57390686035157], [14, 147.63439697265625, 182.7570962524414, 239.09960693359375, 249.2024072265625], [14, 147.63439697265625, 190.49599609375002, 250.88620727539063, 260.9890075683594], [14, 147.63439697265625, 184.54299621582032, 262.6728076171875, 272.7756079101563], [14, 147.63439697265625, 184.54299621582032, 274.4594079589844, 284.5622082519531], [14, 147.63439697265625, 184.54299621582032, 286.2460083007813, 296.34880859375], [14, 147.63439697265625, 178.58999633789062, 298.0326086425781, 308.1354089355469], [14, 147.63439697265625, 178.58999633789062, 309.819208984375, 319.92200927734376], [14, 147.63439697265625, 178.58999633789062, 321.6058093261719, 331.70860961914065], [14, 147.63439697265625, 178.58999633789062, 333.39240966796876, 343.49520996093753], [14, 147.63439697265625, 178.58999633789062, 344.33710998535156, 354.4399102783203], [14, 147.63439697265625, 181.56649627685547, 356.12371032714844, 366.2265106201172], [14, 147.63439697265625, 204.78319580078127, 367.06841064453124, 377.1712109375], [14, 147.63439697265625, 204.78319580078127, 378.0131109619141, 388.9578112792969], [14, 147.63439697265625, 204.78319580078127, 388.9578112792969, 399.9025115966797], [14, 147.63439697265625, 213.11739562988282, 399.9025115966797, 410.84721191406254], [14, 147.63439697265625, 184.54299621582032, 410.84721191406254, 420.95001220703125]]
2026-08-10 17:25:36,029 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=25, matched=25, pages=1, time=23.4s
2026-08-10 17:25:36,030 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:25:36,031 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:25:36,031 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[14]
2026-08-10 17:25:36,031 INFO     29 [qwen-vl-table] positions ： [[14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:25:36,316 INFO     29 [qwen-vl-table] page=14, rect=595x842, img=(1654x2339)
2026-08-10 17:25:36,316 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:25:36,318 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 460, \"bbox_end\": 490, \"encounter_dates\": [\"2026-02-12\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccccccc}\n报告时间: 2026-02-12\n\\hline\n序号 & & 检验项目 & 结果 & 提示 & 单位 & 参考区间 & 检验方法/检测系统 \\\\\n\\hline\n1 & WBC & ☆口● 白细胞计数 & 4.35 & & *10^9/L & 3.50~9.50 & 核酸荧光染色法/SYSMEX \\\\\n2 & Neut\\% & 中性粒细胞百分数 & 65.1 & & \\% & 40.0~75.0 & 核酸荧光染色法/SYSMEX \\\\\n3 & Lymph\\% & 淋巴细胞百分数 & 23.2 & & \\% & 20.0~50.0 & 核酸荧光染色法/SYSMEX \\\\\n4 & Mono\\% & 单核细胞百分数 & 7.4 & & \\% & 3.0~10.0 & 核酸荧光染色法/SYSMEX \\\\\n5 & Eos\\% & 嗜酸性粒细胞百分数 & 3.4 & & \\% & 0.4~8.0 & 核酸荧光染色法/SYSMEX \\\\\n6 & Baso\\% & 嗜碱性粒细胞百分数 & 0.9 & & \\% & 0.0~1.0 & 核酸荧光染色法/SYSMEX \\\\\n7 & Neut\\# & 中性粒细胞绝对值 & 2.83 & & *10^9/L & 1.80~6.30 & 核酸荧光染色法/SYSMEX \\\\\n8 & Lymph\\# & 淋巴细胞绝对值 & 1.01 & ↓ & *10^9/L & 1.10~3.20 & 核酸荧光染色法/SYSMEX \\\\\n9 & Mono\\# & 单核细胞绝对值 & 0.32 & & *10^9/L & 0.10~0.60 & 核酸荧光染色法/SYSMEX \\\\\n10 & Eos\\# & 嗜酸性粒细胞绝对值 & 0.15 & & *10^9/L & 0.02~0.52 & 核酸荧光染色法/SYSMEX \\\\\n11 & Baso\\# & 嗜碱性粒细胞绝对值 & 0.04 & & *10^9/L & 0.00~0.06 & 核酸荧光染色法/SYSMEX \\\\\n12 & RBC & ☆口● 红细胞计数 & 4.10 & & *10^12/L & 3.80~5.10 & 电阻抗法/SYSMEX \\\\\n13 & Hb & ☆口● 血红蛋白 & 124 & & g/L & 115~150 & SLS-血红蛋白法/SYSMEX \\\\\n14 & Hct & ☆口● 红细胞比容 & 0.39 & & L/L & 0.35~0.45 & 电阻信号加权法/SYSMEX \\\\\n15 & MCV & ☆口● 平均红细胞容积 & 94.1 & & fL & 82.0~100.0 & 计算法 \\\\\n16 & MCH & ☆口● 平均红细胞血红蛋白量 & 30.2 & & pg & 27.0~34.0 & 计算法 \\\\\n17 & MCHC & ☆口● 平均红细胞血红蛋白浓度 & 321 & & g/L & 316~354 & 计算法 \\\\\n18 & RDW-SD & 红细胞分布宽度-标准差 & 57.1 & ↑ & fL & 41.9~53.9 & 计算法 \\\\\n19 & RDW-CV & 红细胞分布宽度-变异系数 & 16.8 & ↑ & \\% & 12.1~15.2 & 计算法 \\\\\n20 & PLT & ☆口● 血小板计数 & 175 & & *10^9/L & 125~350 & 电阻抗法/SYSMEX \\\\\n21 & PDW & 血小板体积分布宽度 & 12.9 & & fL & 9.5~15.2 & 计算法 \\\\\n22 & MPV & 血小板平均体积 & 11.2 & & fL & 9.2~12.1 & 计算法 \\\\\n23 & PCT & 血小板压积 & 0.20 & & \\% & 0.19~0.40 & 电阻信号加权法/SYSMEX \\\\\n24 & P-LCR & 大血小板比率 & 33.9 & & \\% & 19.6~42.6 & 计算法 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 17:25:44,910 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:25:44.909+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 80, "failed": 0, "current": {"15f63a1a94e011f1bd9827cf206dfa2d": {"id": "15f63a1a94e011f1bd9827cf206dfa2d", "doc_id": "15bf5b9494e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "size": 6574298, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786382558729, "task_type": "dataflow", "root_trace_id": "e45d0687fc994f25a61430b755af4825", "root_traceparent": "00-e45d0687fc994f25a61430b755af4825-4f140d87c9e2cd09-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:25:52,166 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:25:52,166 INFO     29 [qwen-vl-table] page=14 LLM output (len=4163):
{
  "report_date": "2026-02-12",
  "items": [
    {
      "name": "白细胞计数",
      "item_code": "WBC",
      "value": "4.35",
      "unit": "*10^9/L",
      "reference_range": "3.50~9.50",
      "abnormal": false
    },
    {
      "name": "中性粒细胞百分数",
      "item_code": "Neut%",
      "value": "65.1",
      "unit": "%",
      "reference_range": "40.0~75.0",
      "abnormal": false
    },
    {
      "name": "淋巴细胞百分数",
      "item_code": "Lymph%",
      "value": "23.2",
      "unit": "%",
      "reference_range": "20.0~50.0",
      "abnormal": false
    },
    {
      "name": "单核细胞百分数",
      "item_code": "Mono%",
      "value": "7.4",
      "unit": "%",
      "reference_range": "3.0~10.0",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞百分数",
      "item_code": "Eos%",
      "value": "3.4",
      "unit": "%",
      "reference_range": "0.4~8.0",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞百分数",
      "item_code": "Baso%",
      "value": "0.9",
      "unit": "%",
      "reference_range": "0.0~1.0",
      "abnormal": false
    },
    {
      "name": "中性粒细胞绝对值",
      "item_code": "Neut#",
      "value": "2.83",
      "unit": "*10^9/L",
      "reference_range": "1.80~6.30",
      "abnormal": false
    },
    {
      "name": "淋巴细胞绝对值",
      "item_code": "Lymph#",
      "value": "1.01",
      "unit": "*10^9/L",
      "reference_range": "1.10~3.20",
      "abnormal": true
    },
    {
      "name": "单核细胞绝对值",
      "item_code": "Mono#",
      "value": "0.32",
      "unit": "*10^9/L",
      "reference_range": "0.10~0.60",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞绝对值",
      "item_code": "Eos#",
      "value": "0.15",
      "unit": "*10^9/L",
      "reference_range": "0.02~0.52",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞绝对值",
      "item_code": "Baso#",
      "value": "0.04",
      "unit": "*10^9/L",
      "reference_range": "0.00~0.06",
      "abnormal": false
    },
    {
      "name": "红细胞计数",
      "item_code": "RBC",
      "value": "4.10",
      "unit": "*10^12/L",
      "reference_range": "3.80~5.10",
      "abnormal": false
    },
    {
      "name": "血红蛋白",
      "item_code": "Hb",
      "value": "124",
      "unit": "g/L",
      "reference_range": "115~150",
      "abnormal": false
    },
    {
      "name": "红细胞比容",
      "item_code": "Hct",
      "value": "0.39",
      "unit": "L/L",
      "reference_range": "0.35~0.45",
      "abnormal": false
    },
    {
      "name": "平均红细胞容积",
      "item_code": "MCV",
      "value": "94.1",
      "unit": "fL",
      "reference_range": "82.0~100.0",
      "abnormal": false
    },
    {
      "name": "平均红细胞血红蛋白量",
      "item_code": "MCH",
      "value": "30.2",
      "unit": "pg",
      "reference_range": "27.0~34.0",
      "abnormal": false
    },
    {
      "name": "平均红细胞血红蛋白浓度",
      "item_code": "MCHC",
      "value": "321",
      "unit": "g/L",
      "reference_range": "316~354",
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度-标准差",
      "item_code": "RDW-SD",
      "value": "57.1",
      "unit": "fL",
      "reference_range": "41.9~53.9",
      "abnormal": true
    },
    {
      "name": "红细胞分布宽度-变异系数",
      "item_code": "RDW-CV",
      "value": "16.8",
      "unit": "%",
      "reference_range": "12.1~15.2",
      "abnormal": true
    },
    {
      "name": "血小板计数",
      "item_code": "PLT",
      "value": "175",
      "unit": "*10^9/L",
      "reference_range": "125~350",
      "abnormal": false
    },
    {
      "name": "血小板体积分布宽度",
      "item_code": "PDW",
      "value": "12.9",
      "unit": "fL",
      "reference_range": "9.5~15.2",
      "abnormal": false
    },
    {
      "name": "血小板平均体积",
      "item_code": "MPV",
      "value": "11.2",
      "unit": "fL",
      "reference_range": "9.2~12.1",
      "abnormal": false
    },
    {
      "name": "血小板压积",
      "item_code": "PCT",
      "value": "0.20",
      "unit": "%",
      "reference_range": "0.19~0.40",
      "abnormal": false
    },
    {
      "name": "大血小板比率",
      "item_code": "P-LCR",
      "value": "33.9",
      "unit": "%",
      "reference_range": "19.6~42.6",
      "abnormal": false
    }
  ]
}
2026-08-10 17:25:52,167 INFO     29 [qwen-vl-table] coord grouping: {14: 24}
2026-08-10 17:25:52,175 INFO     29 [qwen-vl-table] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3353782, prompt_len=712
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞计数、中性粒细胞百分数、淋巴细胞百分数、单核细胞百分数、嗜酸性粒细胞百分数、嗜碱性粒细胞百分数、中性粒细胞绝对值、淋巴细胞绝对值、单核细胞绝对值、嗜酸性粒细胞绝对值、嗜碱性粒细胞绝对值、红细胞计数、血红蛋白、红细胞比容、平均红细胞容积、平均红细胞血红蛋白量、平均红细胞血红蛋白浓度、红细胞分布宽度-标准差、红细胞分布宽度-变异系数、血小板计数、血小板体积分布宽度、血小板平均体积、血小板压积、大血小板比率

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
2026-08-10 17:25:59,218 INFO     29 [qwen-vl-table] coord API raw response (len=1264):
[
	{"text": "白细胞计数", "bbox": [261, 204, 323, 215]},
	{"text": "中性粒细胞百分数", "bbox": [261, 218, 359, 229]},
	{"text": "淋巴细胞百分数", "bbox": [261, 232, 347, 243]},
	{"text": "单核细胞百分数", "bbox": [261, 246, 347, 257]},
	{"text": "嗜酸性粒细胞百分数", "bbox": [261, 259, 371, 270]},
	{"text": "嗜碱性粒细胞百分数", "bbox": [261, 273, 371, 284]},
	{"text": "中性粒细胞绝对值", "bbox": [261, 287, 360, 298]},
	{"text": "淋巴细胞绝对值", "bbox": [261, 300, 349, 311]},
	{"text": "单核细胞绝对值", "bbox": [261, 314, 349, 325]},
	{"text": "嗜酸性粒细胞绝对值", "bbox": [261, 328, 373, 339]},
	{"text": "嗜碱性粒细胞绝对值", "bbox": [261, 342, 373, 353]},
	{"text": "红细胞计数", "bbox": [261, 355, 325, 366]},
	{"text": "血红蛋白", "bbox": [261, 369, 312, 380]},
	{"text": "红细胞比容", "bbox": [261, 383, 325, 394]},
	{"text": "平均红细胞容积", "bbox": [261, 396, 350, 407]},
	{"text": "平均红细胞血红蛋白量", "bbox": [261, 409, 387, 420]},
	{"text": "平均红细胞血红蛋白浓度", "bbox": [261, 423, 400, 434]},
	{"text": "红细胞分布宽度-标准差", "bbox": [261, 436, 394, 447]},
	{"text": "红细胞分布宽度-变异系数", "bbox": [261, 449, 404, 460]},
	{"text": "血小板计数", "bbox": [261, 463, 325, 474]},
	{"text": "血小板体积分布宽度", "bbox": [261, 476, 375, 487]},
	{"text": "血小板平均体积", "bbox": [261, 490, 351, 501]},
	{"text": "血小板压积", "bbox": [261, 503, 325, 514]},
	{"text": "大血小板比率", "bbox": [261, 516, 339, 527]}
]
2026-08-10 17:25:59,218 INFO     29 [qwen-vl-table] coord API: raw_items=24, valid_items=24, elapsed=7.0s
2026-08-10 17:25:59,218 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞计数, bbox=[261, 204, 323, 215]
2026-08-10 17:25:59,218 INFO     29 [qwen-vl-table] coord item[1]: text=中性粒细胞百分数, bbox=[261, 218, 359, 229]
2026-08-10 17:25:59,218 INFO     29 [qwen-vl-table] coord item[2]: text=淋巴细胞百分数, bbox=[261, 232, 347, 243]
2026-08-10 17:25:59,218 INFO     29 [qwen-vl-table] coord item[3]: text=单核细胞百分数, bbox=[261, 246, 347, 257]
2026-08-10 17:25:59,218 INFO     29 [qwen-vl-table] coord item[4]: text=嗜酸性粒细胞百分数, bbox=[261, 259, 371, 270]
2026-08-10 17:25:59,218 INFO     29 [qwen-vl-table] coord item[5]: text=嗜碱性粒细胞百分数, bbox=[261, 273, 371, 284]
2026-08-10 17:25:59,218 INFO     29 [qwen-vl-table] coord item[6]: text=中性粒细胞绝对值, bbox=[261, 287, 360, 298]
2026-08-10 17:25:59,219 INFO     29 [qwen-vl-table] coord item[7]: text=淋巴细胞绝对值, bbox=[261, 300, 349, 311]
2026-08-10 17:25:59,219 INFO     29 [qwen-vl-table] coord item[8]: text=单核细胞绝对值, bbox=[261, 314, 349, 325]
2026-08-10 17:25:59,219 INFO     29 [qwen-vl-table] coord item[9]: text=嗜酸性粒细胞绝对值, bbox=[261, 328, 373, 339]
2026-08-10 17:25:59,219 INFO     29 [qwen-vl-table] coord item[10]: text=嗜碱性粒细胞绝对值, bbox=[261, 342, 373, 353]
2026-08-10 17:25:59,219 INFO     29 [qwen-vl-table] coord item[11]: text=红细胞计数, bbox=[261, 355, 325, 366]
2026-08-10 17:25:59,219 INFO     29 [qwen-vl-table] coord item[12]: text=血红蛋白, bbox=[261, 369, 312, 380]
2026-08-10 17:25:59,219 INFO     29 [qwen-vl-table] coord item[13]: text=红细胞比容, bbox=[261, 383, 325, 394]
2026-08-10 17:25:59,219 INFO     29 [qwen-vl-table] coord item[14]: text=平均红细胞容积, bbox=[261, 396, 350, 407]
2026-08-10 17:25:59,219 INFO     29 [qwen-vl-table] coord item[15]: text=平均红细胞血红蛋白量, bbox=[261, 409, 387, 420]
2026-08-10 17:25:59,219 INFO     29 [qwen-vl-table] coord item[16]: text=平均红细胞血红蛋白浓度, bbox=[261, 423, 400, 434]
2026-08-10 17:25:59,219 INFO     29 [qwen-vl-table] coord item[17]: text=红细胞分布宽度-标准差, bbox=[261, 436, 394, 447]
2026-08-10 17:25:59,219 INFO     29 [qwen-vl-table] coord item[18]: text=红细胞分布宽度-变异系数, bbox=[261, 449, 404, 460]
2026-08-10 17:25:59,219 INFO     29 [qwen-vl-table] coord item[19]: text=血小板计数, bbox=[261, 463, 325, 474]
2026-08-10 17:25:59,219 INFO     29 [qwen-vl-table] coord item[20]: text=血小板体积分布宽度, bbox=[261, 476, 375, 487]
2026-08-10 17:25:59,219 INFO     29 [qwen-vl-table] coord item[21]: text=血小板平均体积, bbox=[261, 490, 351, 501]
2026-08-10 17:25:59,219 INFO     29 [qwen-vl-table] coord item[22]: text=血小板压积, bbox=[261, 503, 325, 514]
2026-08-10 17:25:59,219 INFO     29 [qwen-vl-table] coord item[23]: text=大血小板比率, bbox=[261, 516, 339, 527]
2026-08-10 17:25:59,221 INFO     29 [qwen-vl-table] page=14 coord: matched 24/24, time=7.0s
2026-08-10 17:25:59,221 INFO     29 [qwen-vl-table] new_positions (24):
[[15, 155.37329681396486, 192.2818960571289, 171.74760498046876, 181.00850524902344], [15, 155.37329681396486, 213.7126956176758, 183.53420532226562, 192.79510559082033], [15, 155.37329681396486, 206.56909576416015, 195.3208056640625, 204.58170593261718], [15, 155.37329681396486, 206.56909576416015, 207.1074060058594, 216.36830627441407], [15, 155.37329681396486, 220.85629547119143, 218.05210632324219, 227.3130065917969], [15, 155.37329681396486, 220.85629547119143, 229.83870666503907, 239.09960693359375], [15, 155.37329681396486, 214.30799560546876, 241.62530700683595, 250.88620727539063], [15, 155.37329681396486, 207.7596957397461, 252.57000732421875, 261.8309075927734], [15, 155.37329681396486, 207.7596957397461, 264.35660766601563, 273.6175079345703], [15, 155.37329681396486, 222.04689544677734, 276.1432080078125, 285.4041082763672], [15, 155.37329681396486, 222.04689544677734, 287.9298083496094, 297.1907086181641], [15, 155.37329681396486, 193.47249603271484, 298.8745086669922, 308.1354089355469], [15, 155.37329681396486, 185.73359619140626, 310.6611090087891, 319.92200927734376], [15, 155.37329681396486, 193.47249603271484, 322.44770935058597, 331.70860961914065], [15, 155.37329681396486, 208.35499572753906, 333.39240966796876, 342.65330993652344], [15, 155.37329681396486, 230.38109527587892, 344.33710998535156, 353.59801025390624], [15, 155.37329681396486, 238.1199951171875, 356.12371032714844, 365.3846105957031], [15, 155.37329681396486, 234.5481951904297, 367.06841064453124, 376.329310913086], [15, 155.37329681396486, 240.50119506835938, 378.0131109619141, 387.2740112304688], [15, 155.37329681396486, 193.47249603271484, 389.799711303711, 399.06061157226566], [15, 155.37329681396486, 223.23749542236328, 400.7444116210938, 410.00531188964845], [15, 155.37329681396486, 208.95029571533203, 412.53101196289066, 421.79191223144534], [15, 155.37329681396486, 193.47249603271484, 423.47571228027346, 432.73661254882813], [15, 155.37329681396486, 201.80669586181642, 434.42041259765625, 443.68131286621093]]
2026-08-10 17:25:59,222 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=24, matched=24, pages=1, time=23.2s
2026-08-10 17:25:59,236 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 17:25:59,236 INFO     29 [Trace] task=15f63a1a | doc=06-临沂人民-LSPI，后线肺癌，方穹招募.pdf | Extractor:LabExam | outputs={"chunks": "4 items, types={'LabReport': 4}", "html": "", "json": "491 items", "markdown": "", "text": "", "name": "06-临沂人民-LSPI，后线肺癌，方穹招募.pdf", "output_format": "chunks", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Examination\": 3, \"chunks_Discharge\": 1, \"chunks_Clinical\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 17:25:59,237 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 17:25:59,243 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:25:59,243 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 17:26:00,166 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:26:00,174 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 17:26:00,174 INFO     29 [Trace] task=15f63a1a | doc=06-临沂人民-LSPI，后线肺癌，方穹招募.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "491 items", "markdown": "", "text": "", "name": "06-临沂人民-LSPI，后线肺癌，方穹招募.pdf", "output_format": "chunks", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Examination\": 3, \"chunks_Discharge\": 1, \"chunks_Clinical\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 17:26:00,174 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 17:26:00,182 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:26:00,183 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:26:00,183 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 17:26:00,183 INFO     29 [qwen-vl-text] positions(25): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:26:00,183 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [25]
2026-08-10 17:26:00,367 INFO     29 [qwen-vl-text] page=6, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 17:26:00,368 INFO     29 [qwen-vl-text] LLM extraction start, text_len=721
2026-08-10 17:26:00,369 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:26:00,369 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 176, \"bbox_end\": 200, \"encounter_dates\": [\"2026-02-27\"], \"department\": \"呼吸内科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "科室：呼吸内科\n姓名：\n门诊病历号：\n[初诊病历记录(门诊放化疗患者专用)]\n就诊时间：2026年02月27日10时50分\n科别：呼吸内科\n主诉：确诊右肺腺癌5+年，临床试验中\n现病史：患者于2020-8开始出现咳嗽，咳痰伴右侧胸痛，就诊于\n完善相关检查，\n诊断：右肺腺癌，双肺多发转移，（具体转移不详）突变类型 Exon21-L858R突变，Exon19缺失突\n变，KRAS突变，一直维持吉非替尼治疗。2025-11复查病情病情进展，PFS1：63个月。诊断：右肺\n腺癌（驱动基因阴性） 右肺门、纵隔及右侧腋窝多发淋巴结转移 双肺多发转移 右侧胸膜转移\n肋骨转移。受试者于2025年11月11日签署知情同意书，自愿参加一项评估HLX43（抗PD-L1的ADC）\n联合斯鲁利单抗（抗PD-1人源化单克隆抗体注射液）的晚期/转移性实体瘤患者中的安全性、耐受\n性和有效性的Ib/II期临床研究（V3.0 2025年08月15日），2025年12月2给予C1D1治疗，2025年12\n月24给予C2D1治疗，2026年1月14日给予C3D1治疗，2026年2月5日给予C4D1治疗。现患者无特殊不\n适，拟行周期性治疗入院。自发病以来，精神食欲可，大小便无异常，体重未见明显减轻。\n既往史：2020年8月诊断：肝囊肿。否认传染病史，无高血压史，否认糖尿病史，否认心脏病史，\n否认外伤史，否认输血史，预防接种史：不详，否认食物、药物过敏史。\n阳性体征：无\n必要的阴性体征和辅助检查：无\n诊断：1.右肺恶性肿瘤（腺癌）淋巴结继发恶性肿瘤（右肺门、纵膈、右腋窝）胸膜继发性恶性\n肿瘤骨继发恶性肿瘤2.肝囊肿\n治疗意见：入组临床试验治疗。\n医师签名：一式其其",
    "role": "user"
  }
]
2026-08-10 17:26:04,550 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:26:04,550 INFO     29 [qwen-vl-text] LLM output (len=736):
{
  "encounter_date": "2026-02-27",
  "chief_complaint": "确诊右肺腺癌5+年，临床试验中",
  "present_illness": "患者于2020-8开始出现咳嗽，咳痰伴右侧胸痛，就诊于完善相关检查，诊断：右肺腺癌，双肺多发转移，（具体转移不详）突变类型 Exon21-L858R突变，Exon19缺失突变，KRAS突变，一直维持吉非替尼治疗。2025-11复查病情病情进展，PFS1：63个月。诊断：右肺腺癌（驱动基因阴性） 右肺门、纵隔及右侧腋窝多发淋巴结转移 双肺多发转移 右侧胸膜转移肋骨转移。受试者于2025年11月11日签署知情同意书，自愿参加一项评估HLX43（抗PD-L1的ADC）联合斯鲁利单抗（抗PD-1人源化单克隆抗体注射液）的晚期/转移性实体瘤患者中的安全性、耐受性和有效性的Ib/II期临床研究（V3.0 2025年08月15日），2025年12月2给予C1D1治疗，2025年12月24给予C2D1治疗，2026年1月14日给予C3D1治疗，2026年2月5日给予C4D1治疗。现患者无特殊不适，拟行周期性治疗入院。自发病以来，精神食欲可，大小便无异常，体重未见明显减轻。",
  "past_history": "2020年8月诊断：肝囊肿。否认传染病史，无高血压史，否认糖尿病史，否认心脏病史，否认外伤史，否认输血史，预防接种史：不详，否认食物、药物过敏史。",
  "diagnosis": "1.右肺恶性肿瘤（腺癌）淋巴结继发恶性肿瘤（右肺门、纵膈、右腋窝）胸膜继发性恶性肿瘤骨继发恶性肿瘤2.肝囊肿",
  "treatment_plan": "入组临床试验治疗。"
}
2026-08-10 17:26:04,550 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-27]
2026-08-10 17:26:04,553 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2150703, prompt_len=1409
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["科室：呼吸内科", "姓名：", "门诊病历号：", "[初诊病历记录(门诊放化疗患者专用)]", "就诊时间：2026年02月27日10时50分", "科别：呼吸内科", "主诉：确诊右肺腺癌5+年，临床试验中", "现病史：患者于2020-8开始出现咳嗽，咳痰伴右侧胸痛，就诊于", "完善相关检查，", "诊断：右肺腺癌，双肺多发转移，（具体转移不详）突变类型 Exon21-L858R突变，Exon19缺失突", "变，KRAS突变，一直维持吉非替尼治疗。2025-11复查病情病情进展，PFS1：63个月。诊断：右肺", "腺癌（驱动基因阴性） 右肺门、纵隔及右侧腋窝多发淋巴结转移 双肺多发转移 右侧胸膜转移", "肋骨转移。受试者于2025年11月11日签署知情同意书，自愿参加一项评估HLX43（抗PD-L1的ADC）", "联合斯鲁利单抗（抗PD-1人源化单克隆抗体注射液）的晚期/转移性实体瘤患者中的安全性、耐受", "性和有效性的Ib/II期临床研究（V3.0 2025年08月15日），2025年12月2给予C1D1治疗，2025年12", "月24给予C2D1治疗，2026年1月14日给予C3D1治疗，2026年2月5日给予C4D1治疗。现患者无特殊不", "适，拟行周期性治疗入院。自发病以来，精神食欲可，大小便无异常，体重未见明显减轻。", "既往史：2020年8月诊断：肝囊肿。否认传染病史，无高血压史，否认糖尿病史，否认心脏病史，", "否认外伤史，否认输血史，预防接种史：不详，否认食物、药物过敏史。", "阳性体征：无", "必要的阴性体征和辅助检查：无", "诊断：1.右肺恶性肿瘤（腺癌）淋巴结继发恶性肿瘤（右肺门、纵膈、右腋窝）胸膜继发性恶性", "肿瘤骨继发恶性肿瘤2.肝囊肿", "治疗意见：入组临床试验治疗。", "医师签名：一式其其"]

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
2026-08-10 17:26:14,700 INFO     29 [qwen-vl-text] coord API raw response (len=1824):
[
	{"text": "科室：呼吸内科", "bbox": [164, 160, 298, 174]},
	{"text": "姓名：", "bbox": [355, 160, 402, 174]},
	{"text": "门诊病历号：", "bbox": [515, 161, 618, 175]},
	{"text": "[初诊病历记录(门诊放化疗患者专用)]", "bbox": [310, 177, 593, 194]},
	{"text": "就诊时间：2026年02月27日10时50分", "bbox": [172, 195, 388, 209]},
	{"text": "科别：呼吸内科", "bbox": [456, 196, 549, 209]},
	{"text": "主诉：确诊右肺腺癌5+年，临床试验中", "bbox": [172, 217, 396, 230]},
	{"text": "现病史：患者于2020-8开始出现咳嗽，咳痰伴右侧胸痛，就诊于", "bbox": [174, 236, 544, 249]},
	{"text": "完善相关检查，", "bbox": [637, 237, 720, 249]},
	{"text": "诊断：右肺腺癌，双肺多发转移，（具体转移不详）突变类型 Exon21-L858R突变，Exon19缺失突", "bbox": [174, 253, 726, 267]},
	{"text": "变，KRAS突变，一直维持吉非替尼治疗。2025-11复查病情病情进展，PFS1：63个月。诊断：右肺", "bbox": [176, 270, 724, 284]},
	{"text": "腺癌（驱动基因阴性） 右肺门、纵隔及右侧腋窝多发淋巴结转移 双肺多发转移 右侧胸膜转移", "bbox": [178, 288, 723, 301]},
	{"text": "肋骨转移。受试者于2025年11月11日签署知情同意书，自愿参加一项评估HLX43（抗PD-L1的ADC）", "bbox": [180, 305, 715, 318]},
	{"text": "联合斯鲁利单抗（抗PD-1人源化单克隆抗体注射液）的晚期/转移性实体瘤患者中的安全性、耐受", "bbox": [181, 322, 720, 335]},
	{"text": "性和有效性的Ib/II期临床研究（V3.0 2025年08月15日），2025年12月2给予C1D1治疗，2025年12", "bbox": [184, 339, 719, 352]},
	{"text": "月24给予C2D1治疗，2026年1月14日给予C3D1治疗，2026年2月5日给予C4D1治疗。现患者无特殊不", "bbox": [187, 355, 715, 368]},
	{"text": "适，拟行周期性治疗入院。自发病以来，精神食欲可，大小便无异常，体重未见明显减轻。", "bbox": [188, 371, 675, 384]},
	{"text": "既往史：2020年8月诊断：肝囊肿。否认传染病史，无高血压史，否认糖尿病史，否认心脏病史，", "bbox": [190, 387, 705, 399]},
	{"text": "否认外伤史，否认输血史，预防接种史：不详，否认食物、药物过敏史。", "bbox": [192, 402, 577, 414]},
	{"text": "阳性体征：无", "bbox": [195, 417, 270, 428]},
	{"text": "必要的阴性体征和辅助检查：无", "bbox": [197, 432, 370, 443]},
	{"text": "诊断：1.右肺恶性肿瘤（腺癌）淋巴结继发恶性肿瘤（右肺门、纵膈、右腋窝）胸膜继发性恶性", "bbox": [200, 446, 705, 458]},
	{"text": "肿瘤骨继发恶性肿瘤2.肝囊肿", "bbox": [201, 461, 359, 472]},
	{"text": "治疗意见：入组临床试验治疗。", "bbox": [203, 475, 366, 486]},
	{"text": "医师签名：一式其其", "bbox": [430, 487, 547, 498]}
]
2026-08-10 17:26:14,701 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=10.1s
2026-08-10 17:26:14,701 INFO     29 [qwen-vl-text] coord item[0]: text=科室：呼吸内科, bbox=[164, 160, 298, 174]
2026-08-10 17:26:14,701 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[355, 160, 402, 174]
2026-08-10 17:26:14,701 INFO     29 [qwen-vl-text] coord item[2]: text=门诊病历号：, bbox=[515, 161, 618, 175]
2026-08-10 17:26:14,701 INFO     29 [qwen-vl-text] coord item[3]: text=[初诊病历记录(门诊放化疗患者专用)], bbox=[310, 177, 593, 194]
2026-08-10 17:26:14,701 INFO     29 [qwen-vl-text] coord item[4]: text=就诊时间：2026年02月27日10时50分, bbox=[172, 195, 388, 209]
2026-08-10 17:26:14,701 INFO     29 [qwen-vl-text] coord item[5]: text=科别：呼吸内科, bbox=[456, 196, 549, 209]
2026-08-10 17:26:14,701 INFO     29 [qwen-vl-text] coord item[6]: text=主诉：确诊右肺腺癌5+年，临床试验中, bbox=[172, 217, 396, 230]
2026-08-10 17:26:14,701 INFO     29 [qwen-vl-text] coord item[7]: text=现病史：患者于2020-8开始出现咳嗽，咳痰伴右侧胸痛，就诊于, bbox=[174, 236, 544, 249]
2026-08-10 17:26:14,701 INFO     29 [qwen-vl-text] coord item[8]: text=完善相关检查，, bbox=[637, 237, 720, 249]
2026-08-10 17:26:14,701 INFO     29 [qwen-vl-text] coord item[9]: text=诊断：右肺腺癌，双肺多发转移，（具体转移不详）突变类型 Exon21-L858R突变，Exon19缺失突, bbox=[174, 253, 726, 267]
2026-08-10 17:26:14,701 INFO     29 [qwen-vl-text] coord item[10]: text=变，KRAS突变，一直维持吉非替尼治疗。2025-11复查病情病情进展，PFS1：63个月。诊断：右肺, bbox=[176, 270, 724, 284]
2026-08-10 17:26:14,701 INFO     29 [qwen-vl-text] coord item[11]: text=腺癌（驱动基因阴性） 右肺门、纵隔及右侧腋窝多发淋巴结转移 双肺多发转移 右侧胸膜转移, bbox=[178, 288, 723, 301]
2026-08-10 17:26:14,701 INFO     29 [qwen-vl-text] coord item[12]: text=肋骨转移。受试者于2025年11月11日签署知情同意书，自愿参加一项评估HLX43（抗PD-L1的ADC）, bbox=[180, 305, 715, 318]
2026-08-10 17:26:14,702 INFO     29 [qwen-vl-text] coord item[13]: text=联合斯鲁利单抗（抗PD-1人源化单克隆抗体注射液）的晚期/转移性实体瘤患者中的安全性、耐受, bbox=[181, 322, 720, 335]
2026-08-10 17:26:14,702 INFO     29 [qwen-vl-text] coord item[14]: text=性和有效性的Ib/II期临床研究（V3.0 2025年08月15日），2025年12月2给予C1D1治疗，2025年12, bbox=[184, 339, 719, 352]
2026-08-10 17:26:14,702 INFO     29 [qwen-vl-text] coord item[15]: text=月24给予C2D1治疗，2026年1月14日给予C3D1治疗，2026年2月5日给予C4D1治疗。现患者无特殊不, bbox=[187, 355, 715, 368]
2026-08-10 17:26:14,702 INFO     29 [qwen-vl-text] coord item[16]: text=适，拟行周期性治疗入院。自发病以来，精神食欲可，大小便无异常，体重未见明显减轻。, bbox=[188, 371, 675, 384]
2026-08-10 17:26:14,702 INFO     29 [qwen-vl-text] coord item[17]: text=既往史：2020年8月诊断：肝囊肿。否认传染病史，无高血压史，否认糖尿病史，否认心脏病史，, bbox=[190, 387, 705, 399]
2026-08-10 17:26:14,702 INFO     29 [qwen-vl-text] coord item[18]: text=否认外伤史，否认输血史，预防接种史：不详，否认食物、药物过敏史。, bbox=[192, 402, 577, 414]
2026-08-10 17:26:14,702 INFO     29 [qwen-vl-text] coord item[19]: text=阳性体征：无, bbox=[195, 417, 270, 428]
2026-08-10 17:26:14,702 INFO     29 [qwen-vl-text] coord item[20]: text=必要的阴性体征和辅助检查：无, bbox=[197, 432, 370, 443]
2026-08-10 17:26:14,702 INFO     29 [qwen-vl-text] coord item[21]: text=诊断：1.右肺恶性肿瘤（腺癌）淋巴结继发恶性肿瘤（右肺门、纵膈、右腋窝）胸膜继发性恶性, bbox=[200, 446, 705, 458]
2026-08-10 17:26:14,702 INFO     29 [qwen-vl-text] coord item[22]: text=肿瘤骨继发恶性肿瘤2.肝囊肿, bbox=[201, 461, 359, 472]
2026-08-10 17:26:14,702 INFO     29 [qwen-vl-text] coord item[23]: text=治疗意见：入组临床试验治疗。, bbox=[203, 475, 366, 486]
2026-08-10 17:26:14,702 INFO     29 [qwen-vl-text] coord item[24]: text=医师签名：一式其其, bbox=[430, 487, 547, 498]
2026-08-10 17:26:14,703 INFO     29 [qwen-vl-text] page=6 — 25/25 coords, api_time=10.1s
2026-08-10 17:26:14,704 INFO     29 [qwen-vl-text] new_positions (25):
[[6, 97.62919799804688, 177.39939636230469, 134.70400390625, 146.49060424804688], [6, 211.3314956665039, 239.31059509277344, 134.70400390625, 146.49060424804688], [6, 306.5794937133789, 367.8953924560547, 135.54590393066405, 147.33250427246094], [6, 184.54299621582032, 353.0128927612305, 149.01630432128906, 163.32860473632812], [6, 102.39159790039064, 230.9763952636719, 164.1705047607422, 175.95710510253906], [6, 271.45679443359376, 326.81969329833987, 165.01240478515626, 175.95710510253906], [6, 102.39159790039064, 235.73879516601565, 182.69230529785156, 193.6370056152344], [6, 103.58219787597656, 323.843193359375, 198.68840576171877, 209.63310607910157], [6, 379.2060922241211, 428.6159912109375, 199.53030578613283, 209.63310607910157], [6, 103.58219787597656, 432.18779113769534, 213.00070617675783, 224.7873065185547], [6, 104.7727978515625, 430.9971911621094, 227.3130065917969, 239.09960693359375], [6, 105.96339782714844, 430.4018911743164, 242.46720703125, 253.4119073486328], [6, 107.15399780273438, 425.6394912719727, 256.7795074462891, 267.72420776367187], [6, 107.74929779052735, 428.6159912109375, 271.0918078613281, 282.03650817871096], [6, 109.53519775390626, 428.0206912231445, 285.4041082763672, 296.34880859375], [6, 111.32109771728516, 425.6394912719727, 298.8745086669922, 309.819208984375], [6, 111.91639770507813, 401.8274917602539, 312.3449090576172, 323.289609375], [6, 113.10699768066407, 419.686491394043, 325.8153094482422, 335.91810974121097], [6, 114.29759765625, 343.48809295654297, 338.4438098144531, 348.5466101074219], [6, 116.08349761962891, 160.73099670410156, 351.0723101806641, 360.33321044921877], [6, 117.27409759521485, 220.26099548339846, 363.700810546875, 372.9617108154297], [6, 119.05999755859375, 419.686491394043, 375.4874108886719, 385.59021118164065], [6, 119.65529754638672, 213.7126956176758, 388.1159112548828, 397.37681152343754], [6, 120.84589752197266, 217.87979553222658, 399.9025115966797, 409.16341186523437], [6, 255.97899475097657, 325.62909332275393, 410.00531188964845, 419.26621215820313]]
2026-08-10 17:26:14,704 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=14.5s
2026-08-10 17:26:14,894 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 17:26:14,894 INFO     29 [Trace] task=15f63a1a | doc=06-临沂人民-LSPI，后线肺癌，方穹招募.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "491 items", "markdown": "", "text": "", "name": "06-临沂人民-LSPI，后线肺癌，方穹招募.pdf", "output_format": "chunks", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Examination\": 3, \"chunks_Discharge\": 1, \"chunks_Clinical\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 17:26:14,894 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 17:26:14,902 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:26:14,902 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 17:26:16,208 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:26:16,216 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 17:26:16,216 INFO     29 [Trace] task=15f63a1a | doc=06-临沂人民-LSPI，后线肺癌，方穹招募.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "491 items", "markdown": "", "text": "", "name": "06-临沂人民-LSPI，后线肺癌，方穹招募.pdf", "output_format": "chunks", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Examination\": 3, \"chunks_Discharge\": 1, \"chunks_Clinical\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 17:26:16,216 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 17:26:16,225 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:26:16,225 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 17:26:16,662 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:26:16,668 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 17:26:16,668 INFO     29 [Trace] task=15f63a1a | doc=06-临沂人民-LSPI，后线肺癌，方穹招募.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "491 items", "markdown": "", "text": "", "name": "06-临沂人民-LSPI，后线肺癌，方穹招募.pdf", "output_format": "chunks", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Examination\": 3, \"chunks_Discharge\": 1, \"chunks_Clinical\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 17:26:16,669 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 17:26:16,676 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:26:16,677 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:26:16,677 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 17:26:16,677 INFO     29 [qwen-vl-text] positions(66): [[3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:26:16,677 INFO     29 [qwen-vl-text] page grouping: [3, 4, 5], lines per page: [1, 36, 29]
2026-08-10 17:26:16,802 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 17:26:16,962 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 17:26:17,106 INFO     29 [qwen-vl-text] page=5, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 17:26:17,107 INFO     29 [qwen-vl-text] LLM extraction start, text_len=2314
2026-08-10 17:26:17,107 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:26:17,107 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 110, \"bbox_end\": 175, \"encounter_dates\": [\"2025-10-20\", \"2025-10-29\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "2:11:34 PM\n科室：呼吸与危重症医学科 姓名：\n出院记录\n女，59岁，主因“确诊右肺腺癌5年”于2025-10-20入院。于\n2025年10月29日出院，住院天数：9天。\n入院情况：患者于2020年8月因咳嗽，咳痰伴右侧胸痛于北京市丰台中西医结合医院\n行胸部CT示：右肺门旁软组织团块影，考虑癌可能；8月31日于我院住院治疗，期间完善\n支气管镜检查，病理结果示：符合浸润性肺腺癌；基因检测示：EGFR Exon21-L858R突变（\n突变比例43.34%），EGFR Exon19缺失突变（突变比例55.81%），KRAS突变（突变比例\n27.72%）；予口服吉非替尼片（伊瑞可）靶向治疗至今，2021年1月复查提示病情稳定，此后\n患者未规律复查。2023年7月31日于我院住院复查，复查提示病情进展，考虑当前靶向药\n耐药，建议患者重新穿刺行基因检查，患者考虑后拒绝，要求继续服药治疗后出院。现患\n者为求全面复查及中西医结合诊治入院。入院症见：神志清，精神可，偶有咳嗽，干咳少\n痰，活动后稍有气喘，口苦，纳食可，夜眠可，二便正常。舌质暗红，苔薄黄，脉弦滑。\n入院诊断：\n中医诊断：肺癌\n痰瘀互结\n西医诊断：右肺腺癌 T2aN2M1a IV期/双肺多发转移/淋巴结多发转移/右侧胸膜\n转移/脑转移？/靶向治疗后，肝囊肿，营养不良性贫血，脂肪肝\n诊疗经过：入院完善相关检查，指导治疗。化验结果回报：血常规+C反应蛋白：白\n细胞计数[WBC]4.810~9/L，红细胞计数[RBC]4.5410^12/L，血红蛋白量[HGB]127.0g/L，\n红细胞平均血红蛋白浓度[MCHC]314.0g/L，淋巴细胞绝对值[LY#]1.0310^9/L，C-反应\n蛋白[CRP]1.98mg/L。免疫球蛋白E[IgE]8.80IU/mL。肝肾功：白蛋白[ALB]36g/L，高密度\n脂蛋白胆固醇[HDL-C]0.92mmol/L，二氧化碳结合力[CO2CP]28.80mmol/L，总蛋白[TP]\n60.7g/L，①肾小球滤过率估算[eGFR]84.2ml/min，②肾小球滤过率估算[eGFR]\n80.3ml/min。肿瘤标志物示：神经元特异性烯醇化酶[NSE]34.3ng/mL，细胞角蛋白19片段\n[CYFRA21-1]11.50ng/mL。甲功示：抗甲状腺过氧化物酶抗体[Anti-TPO]814.00IU/ml。细\n胞因子测定、心肌酶谱+C反应蛋白、凝血+D二聚体未见明显异常。心电图示：窦性心律\n不齐，心电轴不偏，心电图大致正常。过敏源检测未见明显异常。胸部CT回报：1.符合右\n肺ca征像，包绕邻近血管；2.双肺多发结节，考虑MT；3.纵膈、右肺肺门及右侧腋窝淋巴\n结MT；4.右侧胸膜不均匀增厚，MT可能性大；5.右侧7、8测前肋MT伴软组织肿块形成、右\n侧胸壁增厚；6.所示肝右叶多发低密度影；脾内稍低密度灶；右肾小囊肿可能大；右侧肾\n上腺稍增粗，请结合腹部检查。请结合临床及原片，治疗后复查。脑MRI回报：1.右侧脑\n室前角旁异常信号，结合病史考虑MT，请结合临床复查；2.左侧上颌窦炎。气管镜检查：\n右肺下叶外压性闭塞/支气管镜下炎症性改变。心脏彩超回报：心脏形态结构及功能未见明\n电话：\n备注\n科室：呼吸与危重症医学科 姓名：\n显异常。腹部彩超回报：肝囊肿；胆囊张力高；胰脾双肾未见明显异常。淋巴结彩超回\n报：右侧锁骨区多发肿大淋巴结，MT；双侧腋窝肿大淋巴结，MT。双侧腹股沟区及腹盆腔\n探查未见明显异常肿大淋巴结。病理报告（202510924）：（右肺支气管镜活检组织）送\n检组织被覆鳞状上皮呈慢性炎改变；免疫组化：P40(+)P53(低表达)K1-67(+约10%)。液\n基细胞学检查（Y252882）：（右肺肺泡灌洗液）支气管上皮细胞，炎细胞，个别非典型\n细胞，建议临床进一步检查。全身骨扫描：右侧第7、8侧肋局部及右侧第9肋后肋局部骨\n质代谢增高，结合脏器断层显像，考虑MT，与2023-8-21日片对比新发；右侧第4-6前侧肋\n局部骨质代谢轻度增高，建议3个月复查；L4-5左侧椎小关节退行性改变，较前未见明显\n变化；双侧膝关节骨质代谢增高，考虑骨关节炎性改变。病理图文报告（10239191）：（\n右肺）穿刺波变的纤维组织中可见少许癌巢浸润，结合免疫组化符合：肺腺癌，请结合临\n床及其他检查综合判断。免疫组化：CK(+)CK7(+)TTF-1(+)Napsin-A(+)P63(-)P40(-)Syn(\n一)INSM-1(-)Ki-67(+约20%)BRG1(+)。予抑酸护胃、中药抗肿瘤，气道雾化，氧疗及中医\n外治法、中医辨证论治等中西医综合治疗。于10月24日行CT引导下肺穿刺活检以明确病\n理。\n出院情况：患者神志清，精神可，偶有咳嗽减轻，干咳少痰，活动后稍有气喘，口\n苦，纳食可，夜眠可，二便正常。舌质暗红，苔薄黄，脉弦滑。查体：双肺呼吸音清，未\n闻及明显干湿性啰音，未闻及捻发音，胸部摩擦音。患者症状好转，要求出院于家中等待\n基因检测结果，请示上级医师后，准予出院。\n出院诊断：\n中医诊断：肺癌\n痰瘀互结\n西医诊断：右肺腺癌 T2aN2M1a IV期/双肺多发转移/淋巴结多发转移/右侧胸\n膜转移/脑转移/骨转移/靶向治疗后，肝囊肿，营养不良性贫血，脂肪肝\n出院医嘱：1.院外规律用药，中草药日一剂，定期复诊，不适随诊；2.定期复查胸部\nCT、肺功能；3.加强营养，注意保暖，避免感冒；4.做基因检测确定患者基因突变类型。\n中医调护：避风寒，慎起居，节饮食，畅情志。\n签名：孟丽红\n电话：",
    "role": "user"
  }
]
2026-08-10 17:26:17,108 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:26:17.107+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 80, "failed": 0, "current": {"15f63a1a94e011f1bd9827cf206dfa2d": {"id": "15f63a1a94e011f1bd9827cf206dfa2d", "doc_id": "15bf5b9494e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "size": 6574298, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786382558729, "task_type": "dataflow", "root_trace_id": "e45d0687fc994f25a61430b755af4825", "root_traceparent": "00-e45d0687fc994f25a61430b755af4825-4f140d87c9e2cd09-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:26:35,708 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:26:35,708 INFO     29 [qwen-vl-text] LLM output (len=3667):
{
  "encounter_date": "2025-10-29",
  "admission_date": "2025-10-20",
  "discharge_date": "2025-10-29",
  "hospital_days": 9,
  "department": "呼吸与危重症医学科",
  "bed_number": null,
  "admission_condition": "患者于2020年8月因咳嗽，咳痰伴右侧胸痛于北京市丰台中西医结合医院行胸部CT示：右肺门旁软组织团块影，考虑癌可能；8月31日于我院住院治疗，期间完善支气管镜检查，病理结果示：符合浸润性肺腺癌；基因检测示：EGFR Exon21-L858R突变（突变比例43.34%），EGFR Exon19缺失突变（突变比例55.81%），KRAS突变（突变比例27.72%）；予口服吉非替尼片（伊瑞可）靶向治疗至今，2021年1月复查提示病情稳定，此后患者未规律复查。2023年7月31日于我院住院复查，复查提示病情进展，考虑当前靶向药耐药，建议患者重新穿刺行基因检查，患者考虑后拒绝，要求继续服药治疗后出院。现患者为求全面复查及中西医结合诊治入院。入院症见：神志清，精神可，偶有咳嗽，干咳少痰，活动后稍有气喘，口苦，纳食可，夜眠可，二便正常。舌质暗红，苔薄黄，脉弦滑。",
  "admission_diagnoses": [
    {
      "name": "肺癌",
      "diagnosis_type": "中医"
    },
    {
      "name": "痰瘀互结",
      "diagnosis_type": "中医"
    },
    {
      "name": "右肺腺癌 T2aN2M1a IV期/双肺多发转移/淋巴结多发转移/右侧胸膜转移/脑转移？/靶向治疗后",
      "diagnosis_type": "西医"
    },
    {
      "name": "肝囊肿",
      "diagnosis_type": "西医"
    },
    {
      "name": "营养不良性贫血",
      "diagnosis_type": "西医"
    },
    {
      "name": "脂肪肝",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "入院完善相关检查，指导治疗。于10月24日行CT引导下肺穿刺活检以明确病理。予抑酸护胃、中药抗肿瘤，气道雾化，氧疗及中医外治法、中医辨证论治等中西医综合治疗。",
  "auxiliary_exams": "血常规+C反应蛋白：白细胞计数[WBC]4.810~9/L，红细胞计数[RBC]4.5410^12/L，血红蛋白量[HGB]127.0g/L，红细胞平均血红蛋白浓度[MCHC]314.0g/L，淋巴细胞绝对值[LY#]1.0310^9/L，C-反应蛋白[CRP]1.98mg/L。免疫球蛋白E[IgE]8.80IU/mL。肝肾功：白蛋白[ALB]36g/L，高密度脂蛋白胆固醇[HDL-C]0.92mmol/L，二氧化碳结合力[CO2CP]28.80mmol/L，总蛋白[TP]60.7g/L，①肾小球滤过率估算[eGFR]84.2ml/min，②肾小球滤过率估算[eGFR]80.3ml/min。肿瘤标志物示：神经元特异性烯醇化酶[NSE]34.3ng/mL，细胞角蛋白19片段[CYFRA21-1]11.50ng/mL。甲功示：抗甲状腺过氧化物酶抗体[Anti-TPO]814.00IU/ml。细胞因子测定、心肌酶谱+C反应蛋白、凝血+D二聚体未见明显异常。心电图示：窦性心律不齐，心电轴不偏，心电图大致正常。过敏源检测未见明显异常。心脏彩超回报：心脏形态结构及功能未见明显异常。腹部彩超回报：肝囊肿；胆囊张力高；胰脾双肾未见明显异常。淋巴结彩超回报：右侧锁骨区多发肿大淋巴结，MT；双侧腋窝肿大淋巴结，MT。双侧腹股沟区及腹盆腔探查未见明显异常肿大淋巴结。病理报告（202510924）：（右肺支气管镜活检组织）送检组织被覆鳞状上皮呈慢性炎改变；免疫组化：P40(+)P53(低表达)K1-67(+约10%)。液基细胞学检查（Y252882）：（右肺肺泡灌洗液）支气管上皮细胞，炎细胞，个别非典型细胞，建议临床进一步检查。全身骨扫描：右侧第7、8侧肋局部及右侧第9肋后肋局部骨质代谢增高，结合脏器断层显像，考虑MT，与2023-8-21日片对比新发；右侧第4-6前侧肋局部骨质代谢轻度增高，建议3个月复查；L4-5左侧椎小关节退行性改变，较前未见明显变化；双侧膝关节骨质代谢增高，考虑骨关节炎性改变。病理图文报告（10239191）：（右肺）穿刺波变的纤维组织中可见少许癌巢浸润，结合免疫组化符合：肺腺癌，请结合临床及其他检查综合判断。免疫组化：CK(+)CK7(+)TTF-1(+)Napsin-A(+)P63(-)P40(-)Syn(一)INSM-1(-)Ki-67(+约20%)BRG1(+)。",
  "imaging_findings": "胸部CT回报：1.符合右肺ca征像，包绕邻近血管；2.双肺多发结节，考虑MT；3.纵膈、右肺肺门及右侧腋窝淋巴结MT；4.右侧胸膜不均匀增厚，MT可能性大；5.右侧7、8测前肋MT伴软组织肿块形成、右侧胸壁增厚；6.所示肝右叶多发低密度影；脾内稍低密度灶；右肾小囊肿可能大；右侧肾上腺稍增粗，请结合腹部检查。请结合临床及原片，治疗后复查。脑MRI回报：1.右侧脑室前角旁异常信号，结合病史考虑MT，请结合临床复查；2.左侧上颌窦炎。气管镜检查：右肺下叶外压性闭塞/支气管镜下炎症性改变。",
  "discharge_diagnoses": [
    {
      "name": "肺癌",
      "diagnosis_type": "中医"
    },
    {
      "name": "痰瘀互结",
      "diagnosis_type": "中医"
    },
    {
      "name": "右肺腺癌 T2aN2M1a IV期/双肺多发转移/淋巴结多发转移/右侧胸膜转移/脑转移/骨转移/靶向治疗后",
      "diagnosis_type": "西医"
    },
    {
      "name": "肝囊肿",
      "diagnosis_type": "西医"
    },
    {
      "name": "营养不良性贫血",
      "diagnosis_type": "西医"
    },
    {
      "name": "脂肪肝",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "患者神志清，精神可，偶有咳嗽减轻，干咳少痰，活动后稍有气喘，口苦，纳食可，夜眠可，二便正常。舌质暗红，苔薄黄，脉弦滑。查体：双肺呼吸音清，未闻及明显干湿性啰音，未闻及捻发音，胸部摩擦音。患者症状好转，要求出院于家中等待基因检测结果，请示上级医师后，准予出院。",
  "outcome": "好转",
  "discharge_orders": "1.院外规律用药，中草药日一剂，定期复诊，不适随诊；2.定期复查胸部CT、肺功能；3.加强营养，注意保暖，避免感冒；4.做基因检测确定患者基因突变类型。中医调护：避风寒，慎起居，节饮食，畅情志。",
  "do_medications": [
    "中草药 日一剂"
  ],
  "do_follow_up": "定期复诊，不适随诊；定期复查胸部CT、肺功能",
  "do_precautions": [
    "加强营养",
    "注意保暖",
    "避免感冒",
    "避风寒",
    "慎起居",
    "节饮食",
    "畅情志"
  ],
  "next_treatment_date": null,
  "attending_physician": "孟丽红",
  "pe_ecog_score": null,
  "body_surface_area": null,
  "vs_temperature_c": null,
  "vs_pulse_bpm": null,
  "vs_respiration_rpm": null,
  "vs_systolic_bp_mmhg": null,
  "vs_diastolic_bp_mmhg": null
}
2026-08-10 17:26:35,708 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-10-29]
2026-08-10 17:26:35,711 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1077567, prompt_len=625
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["2:11:34 PM"]

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
2026-08-10 17:26:37,284 INFO     29 [qwen-vl-text] coord API raw response (len=69):
```json
[
	{"text": "2:11:34 PM", "bbox": [600, 829, 693, 857]}
]
```
2026-08-10 17:26:37,285 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=1.6s
2026-08-10 17:26:37,285 INFO     29 [qwen-vl-text] coord item[0]: text=2:11:34 PM, bbox=[600, 829, 693, 857]
2026-08-10 17:26:37,285 INFO     29 [qwen-vl-text] page=3 — 1/1 coords, api_time=1.6s
2026-08-10 17:26:37,288 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1477778, prompt_len=2064
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共36行）
["科室：呼吸与危重症医学科 姓名：", "出院记录", "女，59岁，主因“确诊右肺腺癌5年”于2025-10-20入院。于", "2025年10月29日出院，住院天数：9天。", "入院情况：患者于2020年8月因咳嗽，咳痰伴右侧胸痛于北京市丰台中西医结合医院", "行胸部CT示：右肺门旁软组织团块影，考虑癌可能；8月31日于我院住院治疗，期间完善", "支气管镜检查，病理结果示：符合浸润性肺腺癌；基因检测示：EGFR Exon21-L858R突变（", "突变比例43.34%），EGFR Exon19缺失突变（突变比例55.81%），KRAS突变（突变比例", "27.72%）；予口服吉非替尼片（伊瑞可）靶向治疗至今，2021年1月复查提示病情稳定，此后", "患者未规律复查。2023年7月31日于我院住院复查，复查提示病情进展，考虑当前靶向药", "耐药，建议患者重新穿刺行基因检查，患者考虑后拒绝，要求继续服药治疗后出院。现患", "者为求全面复查及中西医结合诊治入院。入院症见：神志清，精神可，偶有咳嗽，干咳少", "痰，活动后稍有气喘，口苦，纳食可，夜眠可，二便正常。舌质暗红，苔薄黄，脉弦滑。", "入院诊断：", "中医诊断：肺癌", "痰瘀互结", "西医诊断：右肺腺癌 T2aN2M1a IV期/双肺多发转移/淋巴结多发转移/右侧胸膜", "转移/脑转移？/靶向治疗后，肝囊肿，营养不良性贫血，脂肪肝", "诊疗经过：入院完善相关检查，指导治疗。化验结果回报：血常规+C反应蛋白：白", "细胞计数[WBC]4.810~9/L，红细胞计数[RBC]4.5410^12/L，血红蛋白量[HGB]127.0g/L，", "红细胞平均血红蛋白浓度[MCHC]314.0g/L，淋巴细胞绝对值[LY#]1.0310^9/L，C-反应", "蛋白[CRP]1.98mg/L。免疫球蛋白E[IgE]8.80IU/mL。肝肾功：白蛋白[ALB]36g/L，高密度", "脂蛋白胆固醇[HDL-C]0.92mmol/L，二氧化碳结合力[CO2CP]28.80mmol/L，总蛋白[TP]", "60.7g/L，①肾小球滤过率估算[eGFR]84.2ml/min，②肾小球滤过率估算[eGFR]", "80.3ml/min。肿瘤标志物示：神经元特异性烯醇化酶[NSE]34.3ng/mL，细胞角蛋白19片段", "[CYFRA21-1]11.50ng/mL。甲功示：抗甲状腺过氧化物酶抗体[Anti-TPO]814.00IU/ml。细", "胞因子测定、心肌酶谱+C反应蛋白、凝血+D二聚体未见明显异常。心电图示：窦性心律", "不齐，心电轴不偏，心电图大致正常。过敏源检测未见明显异常。胸部CT回报：1.符合右", "肺ca征像，包绕邻近血管；2.双肺多发结节，考虑MT；3.纵膈、右肺肺门及右侧腋窝淋巴", "结MT；4.右侧胸膜不均匀增厚，MT可能性大；5.右侧7、8测前肋MT伴软组织肿块形成、右", "侧胸壁增厚；6.所示肝右叶多发低密度影；脾内稍低密度灶；右肾小囊肿可能大；右侧肾", "上腺稍增粗，请结合腹部检查。请结合临床及原片，治疗后复查。脑MRI回报：1.右侧脑", "室前角旁异常信号，结合病史考虑MT，请结合临床复查；2.左侧上颌窦炎。气管镜检查：", "右肺下叶外压性闭塞/支气管镜下炎症性改变。心脏彩超回报：心脏形态结构及功能未见明", "电话：", "备注"]

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
2026-08-10 17:26:55,084 INFO     29 [qwen-vl-text] coord API raw response (len=2930):
[
	{"text": "科室：呼吸与危重症医学科 姓名：", "bbox": [188, 145, 416, 168]},
	{"text": "出院记录", "bbox": [392, 166, 510, 182]},
	{"text": "女，59岁，主因“确诊右肺腺癌5年”于2025-10-20入院。于", "bbox": [292, 184, 725, 198]},
	{"text": "2025年10月29日出院，住院天数：9天。", "bbox": [178, 198, 419, 218]},
	{"text": "入院情况：患者于2020年8月因咳嗽，咳痰伴右侧胸痛于北京市丰台中西医结合医院", "bbox": [204, 213, 723, 231]},
	{"text": "行胸部CT示：右肺门旁软组织团块影，考虑癌可能；8月31日于我院住院治疗，期间完善", "bbox": [175, 227, 724, 247]},
	{"text": "支气管镜检查，病理结果示：符合浸润性肺腺癌；基因检测示：EGFR Exon21-L858R突变（", "bbox": [174, 242, 735, 262]},
	{"text": "突变比例43.34%），EGFR Exon19缺失突变（突变比例55.81%），KRAS突变（突变比例", "bbox": [173, 258, 687, 277]},
	{"text": "27.72%）；予口服吉非替尼片（伊瑞可）靶向治疗至今，2021年1月复查提示病情稳定，此后", "bbox": [172, 273, 738, 292]},
	{"text": "患者未规律复查。2023年7月31日于我院住院复查，复查提示病情进展，考虑当前靶向药", "bbox": [172, 288, 734, 308]},
	{"text": "耐药，建议患者重新穿刺行基因检查，患者考虑后拒绝，要求继续服药治疗后出院。现患", "bbox": [171, 303, 743, 324]},
	{"text": "者为求全面复查及中西医结合诊治入院。入院症见：神志清，精神可，偶有咳嗽，干咳少", "bbox": [171, 319, 744, 340]},
	{"text": "痰，活动后稍有气喘，口苦，纳食可，夜眠可，二便正常。舌质暗红，苔薄黄，脉弦滑。", "bbox": [170, 335, 740, 357]},
	{"text": "入院诊断：", "bbox": [200, 362, 267, 375]},
	{"text": "中医诊断：肺癌", "bbox": [231, 378, 338, 391]},
	{"text": "痰瘀互结", "bbox": [322, 394, 383, 407]},
	{"text": "西医诊断：右肺腺癌 T2aN2M1a IV期/双肺多发转移/淋巴结多发转移/右侧胸膜", "bbox": [232, 401, 755, 424]},
	{"text": "转移/脑转移？/靶向治疗后，肝囊肿，营养不良性贫血，脂肪肝", "bbox": [170, 421, 582, 443]},
	{"text": "诊疗经过：入院完善相关检查，指导治疗。化验结果回报：血常规+C反应蛋白：白", "bbox": [200, 435, 750, 460]},
	{"text": "细胞计数[WBC]4.810~9/L，红细胞计数[RBC]4.5410^12/L，血红蛋白量[HGB]127.0g/L，", "bbox": [170, 452, 750, 477]},
	{"text": "红细胞平均血红蛋白浓度[MCHC]314.0g/L，淋巴细胞绝对值[LY#]1.0310^9/L，C-反应", "bbox": [170, 469, 754, 494]},
	{"text": "蛋白[CRP]1.98mg/L。免疫球蛋白E[IgE]8.80IU/mL。肝肾功：白蛋白[ALB]36g/L，高密度", "bbox": [170, 487, 762, 512]},
	{"text": "脂蛋白胆固醇[HDL-C]0.92mmol/L，二氧化碳结合力[CO2CP]28.80mmol/L，总蛋白[TP]", "bbox": [170, 504, 740, 529]},
	{"text": "60.7g/L，①肾小球滤过率估算[eGFR]84.2ml/min，②肾小球滤过率估算[eGFR]", "bbox": [169, 522, 696, 548]},
	{"text": "80.3ml/min。肿瘤标志物示：神经元特异性烯醇化酶[NSE]34.3ng/mL，细胞角蛋白19片段", "bbox": [169, 538, 770, 566]},
	{"text": "[CYFRA21-1]11.50ng/mL。甲功示：抗甲状腺过氧化物酶抗体[Anti-TPO]814.00IU/ml。细", "bbox": [170, 556, 772, 583]},
	{"text": "胞因子测定、心肌酶谱+C反应蛋白、凝血+D二聚体未见明显异常。心电图示：窦性心律", "bbox": [169, 574, 766, 601]},
	{"text": "不齐，心电轴不偏，心电图大致正常。过敏源检测未见明显异常。胸部CT回报：1.符合右", "bbox": [169, 592, 776, 620]},
	{"text": "肺ca征像，包绕邻近血管；2.双肺多发结节，考虑MT；3.纵膈、右肺肺门及右侧腋窝淋巴", "bbox": [168, 609, 780, 639]},
	{"text": "结MT；4.右侧胸膜不均匀增厚，MT可能性大；5.右侧7、8测前肋MT伴软组织肿块形成、右", "bbox": [168, 628, 782, 658]},
	{"text": "侧胸壁增厚；6.所示肝右叶多发低密度影；脾内稍低密度灶；右肾小囊肿可能大；右侧肾", "bbox": [168, 647, 784, 677]},
	{"text": "上腺稍增粗，请结合腹部检查。请结合临床及原片，治疗后复查。脑MRI回报：1.右侧脑", "bbox": [169, 666, 780, 696]},
	{"text": "室前角旁异常信号，结合病史考虑MT，请结合临床复查；2.左侧上颌窦炎。气管镜检查：", "bbox": [169, 685, 780, 715]},
	{"text": "右肺下叶外压性闭塞/支气管镜下炎症性改变。心脏彩超回报：心脏形态结构及功能未见明", "bbox": [169, 705, 793, 734]},
	{"text": "电话：", "bbox": [580, 841, 617, 852]},
	{"text": "备注", "bbox": [463, 904, 491, 911]}
]
2026-08-10 17:26:55,084 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=17.8s
2026-08-10 17:26:55,084 INFO     29 [qwen-vl-text] coord item[0]: text=科室：呼吸与危重症医学科 姓名：, bbox=[188, 145, 416, 168]
2026-08-10 17:26:55,084 INFO     29 [qwen-vl-text] coord item[1]: text=出院记录, bbox=[392, 166, 510, 182]
2026-08-10 17:26:55,085 INFO     29 [qwen-vl-text] coord item[2]: text=女，59岁，主因“确诊右肺腺癌5年”于2025-10-20入院。于, bbox=[292, 184, 725, 198]
2026-08-10 17:26:55,085 INFO     29 [qwen-vl-text] coord item[3]: text=2025年10月29日出院，住院天数：9天。, bbox=[178, 198, 419, 218]
2026-08-10 17:26:55,085 INFO     29 [qwen-vl-text] coord item[4]: text=入院情况：患者于2020年8月因咳嗽，咳痰伴右侧胸痛于北京市丰台中西医结合医院, bbox=[204, 213, 723, 231]
2026-08-10 17:26:55,085 INFO     29 [qwen-vl-text] coord item[5]: text=行胸部CT示：右肺门旁软组织团块影，考虑癌可能；8月31日于我院住院治疗，期间完善, bbox=[175, 227, 724, 247]
2026-08-10 17:26:55,085 INFO     29 [qwen-vl-text] coord item[6]: text=支气管镜检查，病理结果示：符合浸润性肺腺癌；基因检测示：EGFR Exon21-L858R突变（, bbox=[174, 242, 735, 262]
2026-08-10 17:26:55,085 INFO     29 [qwen-vl-text] coord item[7]: text=突变比例43.34%），EGFR Exon19缺失突变（突变比例55.81%），KRAS突变（突变比例, bbox=[173, 258, 687, 277]
2026-08-10 17:26:55,085 INFO     29 [qwen-vl-text] coord item[8]: text=27.72%）；予口服吉非替尼片（伊瑞可）靶向治疗至今，2021年1月复查提示病情稳定，此后, bbox=[172, 273, 738, 292]
2026-08-10 17:26:55,085 INFO     29 [qwen-vl-text] coord item[9]: text=患者未规律复查。2023年7月31日于我院住院复查，复查提示病情进展，考虑当前靶向药, bbox=[172, 288, 734, 308]
2026-08-10 17:26:55,085 INFO     29 [qwen-vl-text] coord item[10]: text=耐药，建议患者重新穿刺行基因检查，患者考虑后拒绝，要求继续服药治疗后出院。现患, bbox=[171, 303, 743, 324]
2026-08-10 17:26:55,085 INFO     29 [qwen-vl-text] coord item[11]: text=者为求全面复查及中西医结合诊治入院。入院症见：神志清，精神可，偶有咳嗽，干咳少, bbox=[171, 319, 744, 340]
2026-08-10 17:26:55,085 INFO     29 [qwen-vl-text] coord item[12]: text=痰，活动后稍有气喘，口苦，纳食可，夜眠可，二便正常。舌质暗红，苔薄黄，脉弦滑。, bbox=[170, 335, 740, 357]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[13]: text=入院诊断：, bbox=[200, 362, 267, 375]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[14]: text=中医诊断：肺癌, bbox=[231, 378, 338, 391]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[15]: text=痰瘀互结, bbox=[322, 394, 383, 407]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[16]: text=西医诊断：右肺腺癌 T2aN2M1a IV期/双肺多发转移/淋巴结多发转移/右侧胸膜, bbox=[232, 401, 755, 424]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[17]: text=转移/脑转移？/靶向治疗后，肝囊肿，营养不良性贫血，脂肪肝, bbox=[170, 421, 582, 443]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[18]: text=诊疗经过：入院完善相关检查，指导治疗。化验结果回报：血常规+C反应蛋白：白, bbox=[200, 435, 750, 460]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[19]: text=细胞计数[WBC]4.810~9/L，红细胞计数[RBC]4.5410^12/L，血红蛋白量[HGB]127.0g/L，, bbox=[170, 452, 750, 477]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[20]: text=红细胞平均血红蛋白浓度[MCHC]314.0g/L，淋巴细胞绝对值[LY#]1.0310^9/L，C-反应, bbox=[170, 469, 754, 494]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[21]: text=蛋白[CRP]1.98mg/L。免疫球蛋白E[IgE]8.80IU/mL。肝肾功：白蛋白[ALB]36g/L，高密度, bbox=[170, 487, 762, 512]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[22]: text=脂蛋白胆固醇[HDL-C]0.92mmol/L，二氧化碳结合力[CO2CP]28.80mmol/L，总蛋白[TP], bbox=[170, 504, 740, 529]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[23]: text=60.7g/L，①肾小球滤过率估算[eGFR]84.2ml/min，②肾小球滤过率估算[eGFR], bbox=[169, 522, 696, 548]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[24]: text=80.3ml/min。肿瘤标志物示：神经元特异性烯醇化酶[NSE]34.3ng/mL，细胞角蛋白19片段, bbox=[169, 538, 770, 566]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[25]: text=[CYFRA21-1]11.50ng/mL。甲功示：抗甲状腺过氧化物酶抗体[Anti-TPO]814.00IU/ml。细, bbox=[170, 556, 772, 583]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[26]: text=胞因子测定、心肌酶谱+C反应蛋白、凝血+D二聚体未见明显异常。心电图示：窦性心律, bbox=[169, 574, 766, 601]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[27]: text=不齐，心电轴不偏，心电图大致正常。过敏源检测未见明显异常。胸部CT回报：1.符合右, bbox=[169, 592, 776, 620]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[28]: text=肺ca征像，包绕邻近血管；2.双肺多发结节，考虑MT；3.纵膈、右肺肺门及右侧腋窝淋巴, bbox=[168, 609, 780, 639]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[29]: text=结MT；4.右侧胸膜不均匀增厚，MT可能性大；5.右侧7、8测前肋MT伴软组织肿块形成、右, bbox=[168, 628, 782, 658]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[30]: text=侧胸壁增厚；6.所示肝右叶多发低密度影；脾内稍低密度灶；右肾小囊肿可能大；右侧肾, bbox=[168, 647, 784, 677]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[31]: text=上腺稍增粗，请结合腹部检查。请结合临床及原片，治疗后复查。脑MRI回报：1.右侧脑, bbox=[169, 666, 780, 696]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[32]: text=室前角旁异常信号，结合病史考虑MT，请结合临床复查；2.左侧上颌窦炎。气管镜检查：, bbox=[169, 685, 780, 715]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[33]: text=右肺下叶外压性闭塞/支气管镜下炎症性改变。心脏彩超回报：心脏形态结构及功能未见明, bbox=[169, 705, 793, 734]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[34]: text=电话：, bbox=[580, 841, 617, 852]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] coord item[35]: text=备注, bbox=[463, 904, 491, 911]
2026-08-10 17:26:55,086 INFO     29 [qwen-vl-text] page=4 — 36/36 coords, api_time=17.8s
2026-08-10 17:26:55,088 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1266422, prompt_len=1659
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["科室：呼吸与危重症医学科 姓名：", "显异常。腹部彩超回报：肝囊肿；胆囊张力高；胰脾双肾未见明显异常。淋巴结彩超回", "报：右侧锁骨区多发肿大淋巴结，MT；双侧腋窝肿大淋巴结，MT。双侧腹股沟区及腹盆腔", "探查未见明显异常肿大淋巴结。病理报告（202510924）：（右肺支气管镜活检组织）送", "检组织被覆鳞状上皮呈慢性炎改变；免疫组化：P40(+)P53(低表达)K1-67(+约10%)。液", "基细胞学检查（Y252882）：（右肺肺泡灌洗液）支气管上皮细胞，炎细胞，个别非典型", "细胞，建议临床进一步检查。全身骨扫描：右侧第7、8侧肋局部及右侧第9肋后肋局部骨", "质代谢增高，结合脏器断层显像，考虑MT，与2023-8-21日片对比新发；右侧第4-6前侧肋", "局部骨质代谢轻度增高，建议3个月复查；L4-5左侧椎小关节退行性改变，较前未见明显", "变化；双侧膝关节骨质代谢增高，考虑骨关节炎性改变。病理图文报告（10239191）：（", "右肺）穿刺波变的纤维组织中可见少许癌巢浸润，结合免疫组化符合：肺腺癌，请结合临", "床及其他检查综合判断。免疫组化：CK(+)CK7(+)TTF-1(+)Napsin-A(+)P63(-)P40(-)Syn(", "一)INSM-1(-)Ki-67(+约20%)BRG1(+)。予抑酸护胃、中药抗肿瘤，气道雾化，氧疗及中医", "外治法、中医辨证论治等中西医综合治疗。于10月24日行CT引导下肺穿刺活检以明确病", "理。", "出院情况：患者神志清，精神可，偶有咳嗽减轻，干咳少痰，活动后稍有气喘，口", "苦，纳食可，夜眠可，二便正常。舌质暗红，苔薄黄，脉弦滑。查体：双肺呼吸音清，未", "闻及明显干湿性啰音，未闻及捻发音，胸部摩擦音。患者症状好转，要求出院于家中等待", "基因检测结果，请示上级医师后，准予出院。", "出院诊断：", "中医诊断：肺癌", "痰瘀互结", "西医诊断：右肺腺癌 T2aN2M1a IV期/双肺多发转移/淋巴结多发转移/右侧胸", "膜转移/脑转移/骨转移/靶向治疗后，肝囊肿，营养不良性贫血，脂肪肝", "出院医嘱：1.院外规律用药，中草药日一剂，定期复诊，不适随诊；2.定期复查胸部", "CT、肺功能；3.加强营养，注意保暖，避免感冒；4.做基因检测确定患者基因突变类型。", "中医调护：避风寒，慎起居，节饮食，畅情志。", "签名：孟丽红", "电话："]

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
2026-08-10 17:27:07,253 INFO     29 [qwen-vl-text] coord API raw response (len=2236):
[
	{"text": "科室：呼吸与危重症医学科 姓名：", "bbox": [196, 191, 412, 211]},
	{"text": "显异常。腹部彩超回报：肝囊肿；胆囊张力高；胰脾双肾未见明显异常。淋巴结彩超回", "bbox": [190, 214, 714, 234]},
	{"text": "报：右侧锁骨区多发肿大淋巴结，MT；双侧腋窝肿大淋巴结，MT。双侧腹股沟区及腹盆腔", "bbox": [188, 228, 730, 248]},
	{"text": "探查未见明显异常肿大淋巴结。病理报告（202510924）：（右肺支气管镜活检组织）送", "bbox": [187, 242, 726, 262]},
	{"text": "检组织被覆鳞状上皮呈慢性炎改变；免疫组化：P40(+)P53(低表达)K1-67(+约10%)。液", "bbox": [185, 256, 728, 276]},
	{"text": "基细胞学检查（Y252882）：（右肺肺泡灌洗液）支气管上皮细胞，炎细胞，个别非典型", "bbox": [184, 270, 730, 290]},
	{"text": "细胞，建议临床进一步检查。全身骨扫描：右侧第7、8侧肋局部及右侧第9肋后肋局部骨", "bbox": [182, 285, 732, 305],
	"text": "质代谢增高，结合脏器断层显像，考虑MT，与2023-8-21日片对比新发；右侧第4-6前侧肋", "bbox": [181, 300, 734, 319]},
	{"text": "局部骨质代谢轻度增高，建议3个月复查；L4-5左侧椎小关节退行性改变，较前未见明显", "bbox": [180, 315, 736, 335]},
	{"text": "变化；双侧膝关节骨质代谢增高，考虑骨关节炎性改变。病理图文报告（10239191）：（", "bbox": [179, 330, 746, 350]},
	{"text": "右肺）穿刺波变的纤维组织中可见少许癌巢浸润，结合免疫组化符合：肺腺癌，请结合临", "bbox": [178, 346, 748, 366]},
	{"text": "床及其他检查综合判断。免疫组化：CK(+)CK7(+)TTF-1(+)Napsin-A(+)P63(-)P40(-)Syn(", "bbox": [177, 361, 750, 381]},
	{"text": "-)INSM-1(-)Ki-67(+约20%)BRG1(+)。予抑酸护胃、中药抗肿瘤，气道雾化，氧疗及中医", "bbox": [176, 377, 751, 397]},
	{"text": "外治法、中医辨证论治等中西医综合治疗。于10月24日行CT引导下肺穿刺活检以明确病", "bbox": [175, 393, 739, 413]},
	{"text": "理。", "bbox": [175, 421, 200, 434]},
	{"text": "出院情况：患者神志清，精神可，偶有咳嗽减轻，干咳少痰，活动后稍有气喘，口", "bbox": [207, 428, 742, 450]},
	{"text": "苦，纳食可，夜眠可，二便正常。舌质暗红，苔薄黄，脉弦滑。查体：双肺呼吸音清，未", "bbox": [174, 444, 760, 467]},
	{"text": "闻及明显干湿性啰音，未闻及捻发音，胸部摩擦音。患者症状好转，要求出院于家中等待", "bbox": [174, 460, 761, 483]},
	{"text": "基因检测结果，请示上级医师后，准予出院。", "bbox": [174, 483, 470, 502]},
	{"text": "出院诊断：", "bbox": [206, 506, 274, 519]},
	{"text": "中医诊断：肺癌", "bbox": [245, 521, 353, 535]},
	{"text": "痰瘀互结", "bbox": [337, 537, 398, 550]},
	{"text": "西医诊断：右肺腺癌 T2aN2M1a IV期/双肺多发转移/淋巴结多发转移/右侧胸", "bbox": [244, 547, 764, 571]},
	{"text": "膜转移/脑转移/骨转移/靶向治疗后，肝囊肿，营养不良性贫血，脂肪肝", "bbox": [171, 567, 657, 591]},
	{"text": "出院医嘱：1.院外规律用药，中草药日一剂，定期复诊，不适随诊；2.定期复查胸部", "bbox": [204, 583, 777, 609]},
	{"text": "CT、肺功能；3.加强营养，注意保暖，避免感冒；4.做基因检测确定患者基因突变类型。", "bbox": [170, 601, 771, 628]},
	{"text": "中医调护：避风寒，慎起居，节饮食，畅情志。", "bbox": [203, 624, 520, 647]},
	{"text": "签名：孟丽红", "bbox": [528, 648, 638, 671]},
	{"text": "电话：", "bbox": [581, 897, 618, 910]}
]
2026-08-10 17:27:07,253 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=12.2s
2026-08-10 17:27:07,253 INFO     29 [qwen-vl-text] coord item[0]: text=科室：呼吸与危重症医学科 姓名：, bbox=[196, 191, 412, 211]
2026-08-10 17:27:07,254 INFO     29 [qwen-vl-text] coord item[1]: text=显异常。腹部彩超回报：肝囊肿；胆囊张力高；胰脾双肾未见明显异常。淋巴结彩超回, bbox=[190, 214, 714, 234]
2026-08-10 17:27:07,254 INFO     29 [qwen-vl-text] coord item[2]: text=报：右侧锁骨区多发肿大淋巴结，MT；双侧腋窝肿大淋巴结，MT。双侧腹股沟区及腹盆腔, bbox=[188, 228, 730, 248]
2026-08-10 17:27:07,254 INFO     29 [qwen-vl-text] coord item[3]: text=探查未见明显异常肿大淋巴结。病理报告（202510924）：（右肺支气管镜活检组织）送, bbox=[187, 242, 726, 262]
2026-08-10 17:27:07,254 INFO     29 [qwen-vl-text] coord item[4]: text=检组织被覆鳞状上皮呈慢性炎改变；免疫组化：P40(+)P53(低表达)K1-67(+约10%)。液, bbox=[185, 256, 728, 276]
2026-08-10 17:27:07,254 INFO     29 [qwen-vl-text] coord item[5]: text=基细胞学检查（Y252882）：（右肺肺泡灌洗液）支气管上皮细胞，炎细胞，个别非典型, bbox=[184, 270, 730, 290]
2026-08-10 17:27:07,254 INFO     29 [qwen-vl-text] coord item[6]: text=质代谢增高，结合脏器断层显像，考虑MT，与2023-8-21日片对比新发；右侧第4-6前侧肋, bbox=[181, 300, 734, 319]
2026-08-10 17:27:07,254 INFO     29 [qwen-vl-text] coord item[7]: text=局部骨质代谢轻度增高，建议3个月复查；L4-5左侧椎小关节退行性改变，较前未见明显, bbox=[180, 315, 736, 335]
2026-08-10 17:27:07,254 INFO     29 [qwen-vl-text] coord item[8]: text=变化；双侧膝关节骨质代谢增高，考虑骨关节炎性改变。病理图文报告（10239191）：（, bbox=[179, 330, 746, 350]
2026-08-10 17:27:07,254 INFO     29 [qwen-vl-text] coord item[9]: text=右肺）穿刺波变的纤维组织中可见少许癌巢浸润，结合免疫组化符合：肺腺癌，请结合临, bbox=[178, 346, 748, 366]
2026-08-10 17:27:07,254 INFO     29 [qwen-vl-text] coord item[10]: text=床及其他检查综合判断。免疫组化：CK(+)CK7(+)TTF-1(+)Napsin-A(+)P63(-)P40(-)Syn(, bbox=[177, 361, 750, 381]
2026-08-10 17:27:07,254 INFO     29 [qwen-vl-text] coord item[11]: text=-)INSM-1(-)Ki-67(+约20%)BRG1(+)。予抑酸护胃、中药抗肿瘤，气道雾化，氧疗及中医, bbox=[176, 377, 751, 397]
2026-08-10 17:27:07,254 INFO     29 [qwen-vl-text] coord item[12]: text=外治法、中医辨证论治等中西医综合治疗。于10月24日行CT引导下肺穿刺活检以明确病, bbox=[175, 393, 739, 413]
2026-08-10 17:27:07,254 INFO     29 [qwen-vl-text] coord item[13]: text=理。, bbox=[175, 421, 200, 434]
2026-08-10 17:27:07,254 INFO     29 [qwen-vl-text] coord item[14]: text=出院情况：患者神志清，精神可，偶有咳嗽减轻，干咳少痰，活动后稍有气喘，口, bbox=[207, 428, 742, 450]
2026-08-10 17:27:07,254 INFO     29 [qwen-vl-text] coord item[15]: text=苦，纳食可，夜眠可，二便正常。舌质暗红，苔薄黄，脉弦滑。查体：双肺呼吸音清，未, bbox=[174, 444, 760, 467]
2026-08-10 17:27:07,254 INFO     29 [qwen-vl-text] coord item[16]: text=闻及明显干湿性啰音，未闻及捻发音，胸部摩擦音。患者症状好转，要求出院于家中等待, bbox=[174, 460, 761, 483]
2026-08-10 17:27:07,255 INFO     29 [qwen-vl-text] coord item[17]: text=基因检测结果，请示上级医师后，准予出院。, bbox=[174, 483, 470, 502]
2026-08-10 17:27:07,255 INFO     29 [qwen-vl-text] coord item[18]: text=出院诊断：, bbox=[206, 506, 274, 519]
2026-08-10 17:27:07,255 INFO     29 [qwen-vl-text] coord item[19]: text=中医诊断：肺癌, bbox=[245, 521, 353, 535]
2026-08-10 17:27:07,255 INFO     29 [qwen-vl-text] coord item[20]: text=痰瘀互结, bbox=[337, 537, 398, 550]
2026-08-10 17:27:07,255 INFO     29 [qwen-vl-text] coord item[21]: text=西医诊断：右肺腺癌 T2aN2M1a IV期/双肺多发转移/淋巴结多发转移/右侧胸, bbox=[244, 547, 764, 571]
2026-08-10 17:27:07,255 INFO     29 [qwen-vl-text] coord item[22]: text=膜转移/脑转移/骨转移/靶向治疗后，肝囊肿，营养不良性贫血，脂肪肝, bbox=[171, 567, 657, 591]
2026-08-10 17:27:07,255 INFO     29 [qwen-vl-text] coord item[23]: text=出院医嘱：1.院外规律用药，中草药日一剂，定期复诊，不适随诊；2.定期复查胸部, bbox=[204, 583, 777, 609]
2026-08-10 17:27:07,255 INFO     29 [qwen-vl-text] coord item[24]: text=CT、肺功能；3.加强营养，注意保暖，避免感冒；4.做基因检测确定患者基因突变类型。, bbox=[170, 601, 771, 628]
2026-08-10 17:27:07,255 INFO     29 [qwen-vl-text] coord item[25]: text=中医调护：避风寒，慎起居，节饮食，畅情志。, bbox=[203, 624, 520, 647]
2026-08-10 17:27:07,255 INFO     29 [qwen-vl-text] coord item[26]: text=签名：孟丽红, bbox=[528, 648, 638, 671]
2026-08-10 17:27:07,255 INFO     29 [qwen-vl-text] coord item[27]: text=电话：, bbox=[581, 897, 618, 910]
2026-08-10 17:27:07,255 INFO     29 [qwen-vl-text] page=5 — 29/29 coords, api_time=12.2s
2026-08-10 17:27:07,256 INFO     29 [qwen-vl-text] new_positions (66):
[[3, 357.17999267578125, 412.54289154052736, 697.9351202392578, 721.5083209228516], [4, 111.91639770507813, 247.64479492187502, 122.07550354003907, 141.4392041015625], [4, 233.35759521484377, 303.6029937744141, 139.75540405273438, 153.22580444335938], [4, 173.8275964355469, 431.59249114990234, 154.9096044921875, 166.69620483398438], [4, 105.96339782714844, 249.43069488525393, 166.69620483398438, 183.53420532226562], [4, 121.44119750976563, 430.4018911743164, 179.32470520019533, 194.47890563964845], [4, 104.17749786376953, 430.9971911621094, 191.11130554199218, 207.94930603027345], [4, 103.58219787597656, 437.54549102783204, 203.73980590820312, 220.5778063964844], [4, 102.98689788818359, 408.97109161376954, 217.21020629882813, 233.20630676269533], [4, 102.39159790039064, 439.331390991211, 229.83870666503907, 245.83480712890625], [4, 102.39159790039064, 436.9501910400391, 242.46720703125, 259.3052075195313], [4, 101.79629791259767, 442.3078909301758, 255.09570739746096, 272.7756079101563], [4, 101.79629791259767, 442.90319091796874, 268.56610778808596, 286.2460083007813], [4, 101.2009979248047, 440.5219909667969, 282.03650817871096, 300.5583087158203], [4, 119.05999755859375, 158.94509674072268, 304.76780883789064, 315.71250915527344], [4, 137.5142971801758, 201.21139587402345, 318.23820922851564, 329.18290954589844], [4, 191.68659606933593, 227.99989532470704, 331.70860961914065, 342.65330993652344], [4, 138.10959716796876, 449.45149078369144, 337.6019097900391, 356.96561035156253], [4, 101.2009979248047, 346.46459289550785, 354.4399102783203, 372.9617108154297], [4, 119.05999755859375, 446.47499084472656, 366.2265106201172, 387.2740112304688], [4, 101.2009979248047, 446.47499084472656, 380.53881103515624, 401.5863116455078], [4, 101.2009979248047, 448.85619079589844, 394.85111145019533, 415.8986120605469], [4, 101.2009979248047, 453.6185906982422, 410.00531188964845, 431.0528125], [4, 101.2009979248047, 440.5219909667969, 424.31761230468754, 445.3651129150391], [4, 100.60569793701173, 414.32879150390625, 439.47181274414066, 461.36121337890626], [4, 100.60569793701173, 458.38099060058596, 452.94221313476567, 476.5154138183594], [4, 101.2009979248047, 459.5715905761719, 468.0964135742188, 490.82771423339847], [4, 100.60569793701173, 455.9997906494141, 483.2506140136719, 505.9819146728516], [4, 100.60569793701173, 461.9527905273438, 498.404814453125, 521.9780151367188], [4, 100.01039794921876, 464.33399047851566, 512.7171148681641, 537.974115600586], [4, 100.01039794921876, 465.5245904541016, 528.7132153320313, 553.9702160644531], [4, 100.01039794921876, 466.71519042968754, 544.7093157958984, 569.9663165283204], [4, 100.60569793701173, 464.33399047851566, 560.7054162597657, 585.9624169921875], [4, 100.60569793701173, 464.33399047851566, 576.7015167236328, 601.9585174560547], [4, 100.60569793701173, 472.07289031982424, 593.5395172119141, 617.9546179199219], [4, 345.2739929199219, 367.3000924682617, 708.0379205322266, 717.2988208007813], [4, 275.6238943481445, 292.2922940063477, 761.0776220703125, 766.9709222412109], [5, 116.67879760742188, 245.26359497070314, 160.80290466308594, 177.6409051513672], [5, 113.10699768066407, 425.0441912841797, 180.16660522460938, 197.00460571289062], [5, 111.91639770507813, 434.5689910888672, 191.95320556640627, 208.7912060546875], [5, 111.32109771728516, 432.18779113769534, 203.73980590820312, 220.5778063964844], [5, 110.13049774169923, 433.3783911132813, 215.52640625, 232.36440673828125], [5, 109.53519775390626, 434.5689910888672, 227.3130065917969, 244.15100708007813], [5, 107.74929779052735, 436.9501910400391, 252.57000732421875, 268.56610778808596], [5, 107.15399780273438, 438.14079101562504, 265.1985076904297, 282.03650817871096], [5, 106.55869781494141, 444.0937908935547, 277.82700805664064, 294.6650085449219], [5, 105.96339782714844, 445.2843908691406, 291.29740844726564, 308.1354089355469], [5, 105.36809783935547, 446.47499084472656, 303.92590881347655, 320.76390930175785], [5, 104.7727978515625, 447.07029083251956, 317.39630920410156, 334.23430969238285], [5, 104.17749786376953, 439.9266909790039, 330.86670959472656, 347.70471008300785], [5, 104.17749786376953, 119.05999755859375, 354.4399102783203, 365.3846105957031], [5, 123.22709747314454, 441.71259094238286, 360.33321044921877, 378.8550109863281], [5, 103.58219787597656, 452.42799072265626, 373.80361083984377, 393.1673114013672], [5, 103.58219787597656, 453.02329071044926, 387.2740112304688, 406.6377117919922], [5, 103.58219787597656, 279.79099426269534, 406.6377117919922, 422.63381225585937], [5, 122.63179748535157, 163.11219665527344, 426.00141235351566, 436.94611267089846], [5, 145.84849700927734, 210.14089569091797, 438.6299127197266, 450.41651306152346], [5, 200.61609588623048, 236.92939514160156, 452.1003131103516, 463.0450134277344], [5, 145.25319702148437, 454.80919067382814, 460.5193133544922, 480.7249139404297], [5, 101.79629791259767, 391.1120919799805, 477.35731384277346, 497.56291442871094], [5, 121.44119750976563, 462.5480905151367, 490.82771423339847, 512.7171148681641], [5, 101.2009979248047, 458.9762905883789, 505.9819146728516, 528.7132153320313], [5, 120.84589752197266, 309.5559936523438, 525.345615234375, 544.7093157958984], [5, 314.31839355468753, 379.8013922119141, 545.5512158203126, 564.914916381836], [5, 345.86929290771485, 367.8953924560547, 755.184321899414, 766.1290222167969], [5, 345.86929290771485, 367.8953924560547, 755.184321899414, 766.1290222167969]]
2026-08-10 17:27:07,256 INFO     29 [qwen-vl-text] ═══ DONE ═══ 66 positions, pages=3, time=50.6s
2026-08-10 17:27:07,276 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 17:27:07,276 INFO     29 [Trace] task=15f63a1a | doc=06-临沂人民-LSPI，后线肺癌，方穹招募.pdf | Extractor:Discharge | outputs={"chunks": "1 items, types={'DischargeRecord': 1}", "html": "", "json": "491 items", "markdown": "", "text": "", "name": "06-临沂人民-LSPI，后线肺癌，方穹招募.pdf", "output_format": "chunks", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Examination\": 3, \"chunks_Discharge\": 1, \"chunks_Clinical\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 17:27:07,276 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 17:27:07,277 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:27:07.276+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 80, "failed": 0, "current": {"15f63a1a94e011f1bd9827cf206dfa2d": {"id": "15f63a1a94e011f1bd9827cf206dfa2d", "doc_id": "15bf5b9494e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "size": 6574298, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786382558729, "task_type": "dataflow", "root_trace_id": "e45d0687fc994f25a61430b755af4825", "root_traceparent": "00-e45d0687fc994f25a61430b755af4825-4f140d87c9e2cd09-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:27:07,285 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:27:07,285 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 17:27:08,135 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:27:08,144 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 17:27:08,144 INFO     29 [Trace] task=15f63a1a | doc=06-临沂人民-LSPI，后线肺癌，方穹招募.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "491 items", "markdown": "", "text": "", "name": "06-临沂人民-LSPI，后线肺癌，方穹招募.pdf", "output_format": "chunks", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Examination\": 3, \"chunks_Discharge\": 1, \"chunks_Clinical\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 17:27:08,144 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 17:27:08,152 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:27:08,153 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:27:08,153 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 17:27:08,153 INFO     29 [qwen-vl-text] positions(25): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:27:08,153 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [25]
2026-08-10 17:27:08,255 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 17:27:08,256 INFO     29 [qwen-vl-text] LLM extraction start, text_len=389
2026-08-10 17:27:08,256 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:27:08,257 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 5, \"bbox_end\": 29, \"encounter_dates\": [\"2025-10-24\", \"2025-10-28\"], \"department\": \"肺病科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "彩色病理图文报告\n姓名：\n性别：女\n年龄：59岁\n收到日期：2025-10-24\n送检医院：本院\n送检科室：肺病科\n住院号：\n送检医生：0117\n标本名称：\n蜡块数：1\n特征图像：\n大体描述：\n(右肺)穿刺组织3条，长0.2-0.4CM,直径0.1CM。\n病理诊断：\n(右肺)穿刺玻变的纤维组织中可见少许癌巢浸润，结合免疫组化符合：肺腺癌，\n请结合临床及其它检查综合判断。\n免疫组化：CK(+)CK7(+)TTF-1(+)Napsin-A(+)P63(-)P40(-)Syn(-)INSM-1(-)Ki-67\n(+约20%)BRG1(+)。\n报告医生：张瑜\n审核医生：梁晓霞\n1.注：此结果仅针对本次送检样本，仅供临床医生参考。如有疑问，请于7个工作日内与病理科联系。报告日期：2025-10-28\n2.本报告医师签名有效。\n3.本报告电子版仅供参考，请以纸质报告为准。\n电话：",
    "role": "user"
  }
]
2026-08-10 17:27:10,678 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:27:10,679 INFO     29 [qwen-vl-text] LLM output (len=493):
{
  "exam_date": "2025-10-24",
  "report_date": "2025-10-28",
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "右肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": "肺病科",
  "bed_number": null,
  "findings": "大体描述：\n(右肺)穿刺组织3条，长0.2-0.4CM,直径0.1CM。",
  "conclusion": "病理诊断：\n(右肺)穿刺玻变的纤维组织中可见少许癌巢浸润，结合免疫组化符合：肺腺癌，\n请结合临床及其它检查综合判断。\n免疫组化：CK(+)CK7(+)TTF-1(+)Napsin-A(+)P63(-)P40(-)Syn(-)INSM-1(-)Ki-67(+约20%)BRG1(+)。",
  "physician": "张瑜",
  "reviewer": "梁晓霞"
}
2026-08-10 17:27:10,681 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=733145, prompt_len=1077
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["彩色病理图文报告", "姓名：", "性别：女", "年龄：59岁", "收到日期：2025-10-24", "送检医院：本院", "送检科室：肺病科", "住院号：", "送检医生：0117", "标本名称：", "蜡块数：1", "特征图像：", "大体描述：", "(右肺)穿刺组织3条，长0.2-0.4CM,直径0.1CM。", "病理诊断：", "(右肺)穿刺玻变的纤维组织中可见少许癌巢浸润，结合免疫组化符合：肺腺癌，", "请结合临床及其它检查综合判断。", "免疫组化：CK(+)CK7(+)TTF-1(+)Napsin-A(+)P63(-)P40(-)Syn(-)INSM-1(-)Ki-67", "(+约20%)BRG1(+)。", "报告医生：张瑜", "审核医生：梁晓霞", "1.注：此结果仅针对本次送检样本，仅供临床医生参考。如有疑问，请于7个工作日内与病理科联系。报告日期：2025-10-28", "2.本报告医师签名有效。", "3.本报告电子版仅供参考，请以纸质报告为准。", "电话："]

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
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord API raw response (len=2212):
[
	{"text": "彩色病理图文报告", "bbox": [374, 203, 534, 216]},
	{"text": "姓名：", "bbox": [169, 242, 224, 252], "bbox": [169, 242, 224, 252]},
	{"text": "性别：女", "bbox": [339, 238, 414, 248], "bbox": [339, 238, 414, 248]},
	{"text": "年龄：59岁", "bbox": [452, 237, 535, 247], "bbox": [452, 237, 535, 247]},
	{"text": "收到日期：2025-10-24", "bbox": [589, 237, 712, 247], "bbox": [589, 237, 712, 247]},
	{"text": "送检医院：本院", "bbox": [167, 257, 251, 267], "bbox": [167, 257, 251, 267]},
	{"text": "送检科室：肺病科", "bbox": [339, 254, 439, 264], "bbox": [339, 254, 439, 264]},
	{"text": "住院号：", "bbox": [590, 252, 645, 262], "bbox": [590, 252, 645, 262]},
	{"text": "送检医生：0117", "bbox": [165, 274, 251, 284], "bbox": [165, 274, 251, 284]},
	{"text": "标本名称：", "bbox": [339, 272, 396, 282], "bbox": [339, 272, 396, 282]},
	{"text": "蜡块数：1", "bbox": [590, 270, 662, 280], "bbox": [590, 270, 662, 280]},
	{"text": "特征图像：", "bbox": [191, 299, 254, 309], "bbox": [191, 299, 254, 309]},
	{"text": "大体描述：", "bbox": [190, 433, 256, 444], "bbox": [190, 433, 256, 444]},
	{"text": "(右肺)穿刺组织3条，长0.2-0.4CM,直径0.1CM。", "bbox": [230, 443, 528, 456], "bbox": [230, 443, 528, 456]},
	{"text": "病理诊断：", "bbox": [191, 540, 258, 552], "bbox": [191, 540, 258, 552]},
	{"text": "(右肺)穿刺玻变的纤维组织中可见少许癌巢浸润，结合免疫组化符合：肺腺癌，", "bbox": [230, 542, 731, 563], "bbox": [230, 542, 731, 563]},
	{"text": "请结合临床及其它检查综合判断。", "bbox": [222, 560, 434, 575], "bbox": [222, 560, 434, 575]},
	{"text": "免疫组化：CK(+)CK7(+)TTF-1(+)Napsin-A(+)P63(-)P40(-)Syn(-)INSM-1(-)Ki-67", "bbox": [229, 565, 742, 587], "bbox": [229, 565, 742, 587]},
	{"text": "(+约20%)BRG1(+)。", "bbox": [224, 585, 341, 599], "bbox": [224, 585, 341, 599]},
	{"text": "报告医生：张瑜", "bbox": [163, 758, 261, 772], "bbox": [163, 758, 261, 772]},
	{"text": "审核医生：梁晓霞", "bbox": [657, 744, 770, 757], "bbox": [657, 744, 770, 757]},
	{"text": "1.注：此结果仅针对本次送检样本，仅供临床医生参考。如有疑问，请于7个工作日内与病理科联系。报告日期：2025-10-28", "bbox": [152, 766, 800, 788], "bbox": [152, 766, 800, 788]},
	{"text": "2.本报告医师签名有效。", "bbox": [152, 787, 274, 798], "bbox": [152, 787, 274, 798]},
	{"text": "3.本报告电子版仅供参考，请以纸质报告为准。", "bbox": [152, 794, 389, 808], "bbox": [152, 794, 389, 808]},
	{"text": "电话：", "bbox": [580, 863, 614, 875], "bbox": [580, 863, 614, 875]}
]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=14.1s
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[0]: text=彩色病理图文报告, bbox=[374, 203, 534, 216]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[169, 242, 224, 252]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[2]: text=性别：女, bbox=[339, 238, 414, 248]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：59岁, bbox=[452, 237, 535, 247]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[4]: text=收到日期：2025-10-24, bbox=[589, 237, 712, 247]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[5]: text=送检医院：本院, bbox=[167, 257, 251, 267]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[6]: text=送检科室：肺病科, bbox=[339, 254, 439, 264]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[7]: text=住院号：, bbox=[590, 252, 645, 262]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[8]: text=送检医生：0117, bbox=[165, 274, 251, 284]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[9]: text=标本名称：, bbox=[339, 272, 396, 282]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[10]: text=蜡块数：1, bbox=[590, 270, 662, 280]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[11]: text=特征图像：, bbox=[191, 299, 254, 309]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[12]: text=大体描述：, bbox=[190, 433, 256, 444]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[13]: text=(右肺)穿刺组织3条，长0.2-0.4CM,直径0.1CM。, bbox=[230, 443, 528, 456]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[14]: text=病理诊断：, bbox=[191, 540, 258, 552]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[15]: text=(右肺)穿刺玻变的纤维组织中可见少许癌巢浸润，结合免疫组化符合：肺腺癌，, bbox=[230, 542, 731, 563]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[16]: text=请结合临床及其它检查综合判断。, bbox=[222, 560, 434, 575]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[17]: text=免疫组化：CK(+)CK7(+)TTF-1(+)Napsin-A(+)P63(-)P40(-)Syn(-)INSM-1(-)Ki-67, bbox=[229, 565, 742, 587]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[18]: text=(+约20%)BRG1(+)。, bbox=[224, 585, 341, 599]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[19]: text=报告医生：张瑜, bbox=[163, 758, 261, 772]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[20]: text=审核医生：梁晓霞, bbox=[657, 744, 770, 757]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[21]: text=1.注：此结果仅针对本次送检样本，仅供临床医生参考。如有疑问，请于7个工作日内与病理科联系。报告日期：2025-10-28, bbox=[152, 766, 800, 788]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[22]: text=2.本报告医师签名有效。, bbox=[152, 787, 274, 798]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[23]: text=3.本报告电子版仅供参考，请以纸质报告为准。, bbox=[152, 794, 389, 808]
2026-08-10 17:27:24,788 INFO     29 [qwen-vl-text] coord item[24]: text=电话：, bbox=[580, 863, 614, 875]
2026-08-10 17:27:24,789 INFO     29 [qwen-vl-text] page=1 — 25/25 coords, api_time=14.1s
2026-08-10 17:27:24,789 INFO     29 [qwen-vl-text] new_positions (25):
[[1, 222.6421954345703, 317.89019348144535, 170.9057049560547, 181.8504052734375], [1, 100.60569793701173, 133.347197265625, 203.73980590820312, 212.15880615234377], [1, 201.80669586181642, 246.45419494628908, 200.3722058105469, 208.7912060546875], [1, 269.0755944824219, 318.4854934692383, 199.53030578613283, 207.94930603027345], [1, 350.6316928100586, 423.85359130859376, 199.53030578613283, 207.94930603027345], [1, 99.41509796142579, 149.42029693603516, 216.36830627441407, 224.7873065185547], [1, 201.80669586181642, 261.3366946411133, 213.8426062011719, 222.2616064453125], [1, 351.22699279785155, 383.96849212646487, 212.15880615234377, 220.5778063964844], [1, 98.22449798583985, 149.42029693603516, 230.68060668945313, 239.09960693359375], [1, 201.80669586181642, 235.73879516601565, 228.996806640625, 237.41580688476563], [1, 351.22699279785155, 394.0885919189453, 227.3130065917969, 235.7320068359375], [1, 113.70229766845704, 151.20619689941407, 251.7281072998047, 260.1471075439453], [1, 113.10699768066407, 152.396796875, 364.5427105712891, 373.80361083984377], [1, 136.91899719238282, 314.31839355468753, 372.9617108154297, 383.90641113281254], [1, 113.70229766845704, 153.58739685058595, 454.6260131835938, 464.7288134765625], [1, 136.91899719238282, 435.16429107666016, 456.3098132324219, 473.98971374511723], [1, 132.15659729003906, 258.3601947021485, 471.464013671875, 484.09251403808594], [1, 136.32369720458985, 441.71259094238286, 475.67351379394535, 494.1953143310547], [1, 133.347197265625, 202.99729583740236, 492.5115142822266, 504.29811462402347], [1, 97.0338980102539, 155.37329681396486, 638.1602185058593, 649.9468188476562], [1, 391.1120919799805, 458.38099060058596, 626.3736181640626, 637.3183184814453], [1, 90.48559814453125, 476.239990234375, 644.8954187011719, 663.4172192382813], [1, 90.48559814453125, 163.11219665527344, 662.5753192138673, 671.8362194824219], [1, 90.48559814453125, 231.57169525146486, 668.4686193847657, 680.2552197265625], [1, 345.2739929199219, 365.5141925048828, 726.559721069336, 736.6625213623047]]
2026-08-10 17:27:24,789 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=16.6s
2026-08-10 17:27:24,789 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:27:24,790 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:27:24,790 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 17:27:24,790 INFO     29 [qwen-vl-text] positions(39): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:27:24,790 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [39]
2026-08-10 17:27:24,926 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 17:27:24,927 INFO     29 [qwen-vl-text] LLM extraction start, text_len=780
2026-08-10 17:27:24,927 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:27:24,928 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 30, \"bbox_end\": 68, \"encounter_dates\": [\"2026-01-13\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "CT检查报告单\n患者编号:\n扫描日期: 1/13/2026\n姓名:\n性别:女\n年龄:59岁科别:\n住院号:\n扫描设备:SIEMENS_CT\n扫描方法:平扫+增强12张\n药品:碘普罗胺注射液\n100ml\n药品处理方式:静脉+静脉留置+高压注射\n检查项目:上腹+下腹+盆腔+胸部(平扫+增强)\n扫描所见:\n参考2025-11-21胸部CT,所见如下:\n1.右肺可见巨大不规则肿块,病变范围较广,累及右全肺,增强扫描不均匀强化,较前\n局部略缩小;余双肺见多发结节影,部分内可见空泡,最大径约2cm,较前部分略缩\n小。\n2.右侧腋窝、纵隔及右肺门见增大淋巴结,最大短径约1.5cm,不均匀强化。考虑MT,\n右侧腋窝淋巴结较前缩小,余大致同前。右侧心隔角淋巴结较前增大,短径约0.6cm。\n3.心影不大,心包少量积液同前。\n4.右侧胸膜不均匀增厚,考虑MT,伴少量积液,同前。\n5.肝脏大小形态尚可,肝内散在低密度结节,较大径约2.3cm,大部分界清,增强扫描\n未见明显强化,部分界欠清,同前相仿。\n6.双肾多发囊肿,较大径约0.4cm,同前。\n7.脾脏见稍低密度结节,较大径约0.6cm,边界欠清,边缘似有强化,同前相仿。\n8.胰腺、双侧肾上腺未见明显异常密度影。\n9.腹膜后见小淋巴结显示,最大短径约0.4cm,大致同前。\n10.膀胱充盈尚可,壁未见明显增厚。\n11.双侧附件区见致密影同前。子宫大小形态尚可,子宫肌层强化欠均匀,同前相仿,\n请结合临床。盆腔少量积液较前增多。\n12.双侧髂血管及腹股沟区未见明显增大淋巴结。\n13.骨窗部分肋骨多发斑片状密度增高影,周围软组织增厚,增强后明显强化。考虑\nMT,大致同前。\n印象:\n报告者:王二娟\n审核医师: 何晶晶\n日期:1/13/2026 2:11:3\n本报告仅供临床医师参考,不作为法律依据。妥善保管,遗失不补。",
    "role": "user"
  }
]
2026-08-10 17:27:29,969 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:27:29,969 INFO     29 [qwen-vl-text] LLM output (len=906):
{
  "exam_date": "2026-01-13",
  "report_date": "2026-01-13",
  "exam_name": "上腹+下腹+盆腔+胸部(平扫+增强)",
  "exam_category": "imaging",
  "body_part": "上腹+下腹+盆腔+胸部",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "扫描所见:\n参考2025-11-21胸部CT,所见如下:\n1.右肺可见巨大不规则肿块,病变范围较广,累及右全肺,增强扫描不均匀强化,较前局部略缩小;余双肺见多发结节影,部分内可见空泡,最大径约2cm,较前部分略缩小。\n2.右侧腋窝、纵隔及右肺门见增大淋巴结,最大短径约1.5cm,不均匀强化。考虑MT,右侧腋窝淋巴结较前缩小,余大致同前。右侧心隔角淋巴结较前增大,短径约0.6cm。\n3.心影不大,心包少量积液同前。\n4.右侧胸膜不均匀增厚,考虑MT,伴少量积液,同前。\n5.肝脏大小形态尚可,肝内散在低密度结节,较大径约2.3cm,大部分界清,增强扫描未见明显强化,部分界欠清,同前相仿。\n6.双肾多发囊肿,较大径约0.4cm,同前。\n7.脾脏见稍低密度结节,较大径约0.6cm,边界欠清,边缘似有强化,同前相仿。\n8.胰腺、双侧肾上腺未见明显异常密度影。\n9.腹膜后见小淋巴结显示,最大短径约0.4cm,大致同前。\n10.膀胱充盈尚可,壁未见明显增厚。\n11.双侧附件区见致密影同前。子宫大小形态尚可,子宫肌层强化欠均匀,同前相仿,请结合临床。盆腔少量积液较前增多。\n12.双侧髂血管及腹股沟区未见明显增大淋巴结。\n13.骨窗部分肋骨多发斑片状密度增高影,周围软组织增厚,增强后明显强化。考虑MT,大致同前。",
  "conclusion": "印象:",
  "physician": "王二娟",
  "reviewer": "何晶晶"
}
2026-08-10 17:27:29,971 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=977363, prompt_len=1510
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共39行）
["CT检查报告单", "患者编号:", "扫描日期: 1/13/2026", "姓名:", "性别:女", "年龄:59岁科别:", "住院号:", "扫描设备:SIEMENS_CT", "扫描方法:平扫+增强12张", "药品:碘普罗胺注射液", "100ml", "药品处理方式:静脉+静脉留置+高压注射", "检查项目:上腹+下腹+盆腔+胸部(平扫+增强)", "扫描所见:", "参考2025-11-21胸部CT,所见如下:", "1.右肺可见巨大不规则肿块,病变范围较广,累及右全肺,增强扫描不均匀强化,较前", "局部略缩小;余双肺见多发结节影,部分内可见空泡,最大径约2cm,较前部分略缩", "小。", "2.右侧腋窝、纵隔及右肺门见增大淋巴结,最大短径约1.5cm,不均匀强化。考虑MT,", "右侧腋窝淋巴结较前缩小,余大致同前。右侧心隔角淋巴结较前增大,短径约0.6cm。", "3.心影不大,心包少量积液同前。", "4.右侧胸膜不均匀增厚,考虑MT,伴少量积液,同前。", "5.肝脏大小形态尚可,肝内散在低密度结节,较大径约2.3cm,大部分界清,增强扫描", "未见明显强化,部分界欠清,同前相仿。", "6.双肾多发囊肿,较大径约0.4cm,同前。", "7.脾脏见稍低密度结节,较大径约0.6cm,边界欠清,边缘似有强化,同前相仿。", "8.胰腺、双侧肾上腺未见明显异常密度影。", "9.腹膜后见小淋巴结显示,最大短径约0.4cm,大致同前。", "10.膀胱充盈尚可,壁未见明显增厚。", "11.双侧附件区见致密影同前。子宫大小形态尚可,子宫肌层强化欠均匀,同前相仿,", "请结合临床。盆腔少量积液较前增多。", "12.双侧髂血管及腹股沟区未见明显增大淋巴结。", "13.骨窗部分肋骨多发斑片状密度增高影,周围软组织增厚,增强后明显强化。考虑", "MT,大致同前。", "印象:", "报告者:王二娟", "审核医师: 何晶晶", "日期:1/13/2026 2:11:3", "本报告仅供临床医师参考,不作为法律依据。妥善保管,遗失不补。"]

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
2026-08-10 17:27:43,089 INFO     29 [qwen-vl-text] coord API raw response (len=2499):
[
	{"text": "CT检查报告单", "bbox": [428, 188, 573, 205]},
	{"text": "患者编号:", "bbox": [202, 217, 279, 230]},
	{"text": "扫描日期: 1/13/2026", "bbox": [601, 213, 738, 225]},
	{"text": "姓名:", "bbox": [197, 241, 241, 254]},
	{"text": "性别:女", "bbox": [319, 239, 379, 253]},
	{"text": "年龄:59岁科别:", "bbox": [400, 238, 528, 252]},
	{"text": "住院号:", "bbox": [603, 236, 663, 249]},
	{"text": "扫描设备:SIEMENS_CT", "bbox": [197, 259, 341, 271]},
	{"text": "扫描方法:平扫+增强12张", "bbox": [460, 255, 620, 268]},
	{"text": "药品:碘普罗胺注射液", "bbox": [195, 275, 340, 287]},
	{"text": "100ml", "bbox": [388, 273, 427, 284]},
	{"text": "药品处理方式:静脉+静脉留置+高压注射", "bbox": [458, 270, 718, 283]},
	{"text": "检查项目:上腹+下腹+盆腔+胸部(平扫+增强)", "bbox": [194, 289, 497, 301]},
	{"text": "扫描所见:", "bbox": [192, 317, 272, 330]},
	{"text": "参考2025-11-21胸部CT,所见如下:", "bbox": [189, 332, 420, 344]},
	{"text": "1.右肺可见巨大不规则肿块,病变范围较广,累及右全肺,增强扫描不均匀强化,较前", "bbox": [188, 341, 757, 357]},
	{"text": "局部略缩小;余双肺见多发结节影,部分内可见空泡,最大径约2cm,较前部分略缩", "bbox": [188, 355, 737, 370]},
	{"text": "小。", "bbox": [188, 372, 209, 384]},
	{"text": "2.右侧腋窝、纵隔及右肺门见增大淋巴结,最大短径约1.5cm,不均匀强化。考虑MT,", "bbox": [186, 381, 745, 397]},
	{"text": "右侧腋窝淋巴结较前缩小,余大致同前。右侧心隔角淋巴结较前增大,短径约0.6cm。", "bbox": [186, 395, 748, 410]},
	{"text": "3.心影不大,心包少量积液同前。", "bbox": [185, 413, 408, 426]},
	{"text": "4.右侧胸膜不均匀增厚,考虑MT,伴少量积液,同前。", "bbox": [185, 426, 544, 441]},
	{"text": "5.肝脏大小形态尚可,肝内散在低密度结节,较大径约2.3cm,大部分界清,增强扫描", "bbox": [184, 439, 760, 455]},
	{"text": "未见明显强化,部分界欠清,同前相仿。", "bbox": [184, 455, 454, 469]},
	{"text": "6.双肾多发囊肿,较大径约0.4cm,同前。", "bbox": [181, 470, 462, 484]},
	{"text": "7.脾脏见稍低密度结节,较大径约0.6cm,边界欠清,边缘似有强化,同前相仿。", "bbox": [180, 483, 725, 500]},
	{"text": "8.胰腺、双侧肾上腺未见明显异常密度影。", "bbox": [179, 501, 471, 515]},
	{"text": "9.腹膜后见小淋巴结显示,最大短径约0.4cm,大致同前。", "bbox": [178, 515, 572, 530]},
	{"text": "10.膀胱充盈尚可,壁未见明显增厚。", "bbox": [178, 531, 433, 546]},
	{"text": "11.双侧附件区见致密影同前。子宫大小形态尚可,子宫肌层强化欠均匀,同前相仿,", "bbox": [177, 544, 762, 562]},
	{"text": "请结合临床。盆腔少量积液较前增多。", "bbox": [177, 562, 441, 577]},
	{"text": "12.双侧髂血管及腹股沟区未见明显增大淋巴结。", "bbox": [176, 577, 513, 593]},
	{"text": "13.骨窗部分肋骨多发斑片状密度增高影,周围软组织增厚,增强后明显强化。考虑", "bbox": [175, 591, 760, 609]},
	{"text": "MT,大致同前。", "bbox": [172, 613, 279, 627]},
	{"text": "印象:", "bbox": [178, 635, 225, 651]},
	{"text": "报告者:王二娟", "bbox": [174, 757, 319, 775]},
	{"text": "审核医师: 何晶晶", "bbox": [373, 750, 577, 777]},
	{"text": "日期:1/13/2026 2:11:3", "bbox": [577, 749, 783, 769]},
	{"text": "本报告仅供临床医师参考,不作为法律依据。妥善保管,遗失不补。", "bbox": [200, 780, 695, 801]}
]
2026-08-10 17:27:43,090 INFO     29 [qwen-vl-text] coord API: raw_items=39, valid_items=39, elapsed=13.1s
2026-08-10 17:27:43,090 INFO     29 [qwen-vl-text] coord item[0]: text=CT检查报告单, bbox=[428, 188, 573, 205]
2026-08-10 17:27:43,090 INFO     29 [qwen-vl-text] coord item[1]: text=患者编号:, bbox=[202, 217, 279, 230]
2026-08-10 17:27:43,090 INFO     29 [qwen-vl-text] coord item[2]: text=扫描日期: 1/13/2026, bbox=[601, 213, 738, 225]
2026-08-10 17:27:43,090 INFO     29 [qwen-vl-text] coord item[3]: text=姓名:, bbox=[197, 241, 241, 254]
2026-08-10 17:27:43,090 INFO     29 [qwen-vl-text] coord item[4]: text=性别:女, bbox=[319, 239, 379, 253]
2026-08-10 17:27:43,091 INFO     29 [qwen-vl-text] coord item[5]: text=年龄:59岁科别:, bbox=[400, 238, 528, 252]
2026-08-10 17:27:43,091 INFO     29 [qwen-vl-text] coord item[6]: text=住院号:, bbox=[603, 236, 663, 249]
2026-08-10 17:27:43,091 INFO     29 [qwen-vl-text] coord item[7]: text=扫描设备:SIEMENS_CT, bbox=[197, 259, 341, 271]
2026-08-10 17:27:43,091 INFO     29 [qwen-vl-text] coord item[8]: text=扫描方法:平扫+增强12张, bbox=[460, 255, 620, 268]
2026-08-10 17:27:43,091 INFO     29 [qwen-vl-text] coord item[9]: text=药品:碘普罗胺注射液, bbox=[195, 275, 340, 287]
2026-08-10 17:27:43,091 INFO     29 [qwen-vl-text] coord item[10]: text=100ml, bbox=[388, 273, 427, 284]
2026-08-10 17:27:43,091 INFO     29 [qwen-vl-text] coord item[11]: text=药品处理方式:静脉+静脉留置+高压注射, bbox=[458, 270, 718, 283]
2026-08-10 17:27:43,091 INFO     29 [qwen-vl-text] coord item[12]: text=检查项目:上腹+下腹+盆腔+胸部(平扫+增强), bbox=[194, 289, 497, 301]
2026-08-10 17:27:43,091 INFO     29 [qwen-vl-text] coord item[13]: text=扫描所见:, bbox=[192, 317, 272, 330]
2026-08-10 17:27:43,091 INFO     29 [qwen-vl-text] coord item[14]: text=参考2025-11-21胸部CT,所见如下:, bbox=[189, 332, 420, 344]
2026-08-10 17:27:43,091 INFO     29 [qwen-vl-text] coord item[15]: text=1.右肺可见巨大不规则肿块,病变范围较广,累及右全肺,增强扫描不均匀强化,较前, bbox=[188, 341, 757, 357]
2026-08-10 17:27:43,091 INFO     29 [qwen-vl-text] coord item[16]: text=局部略缩小;余双肺见多发结节影,部分内可见空泡,最大径约2cm,较前部分略缩, bbox=[188, 355, 737, 370]
2026-08-10 17:27:43,091 INFO     29 [qwen-vl-text] coord item[17]: text=小。, bbox=[188, 372, 209, 384]
2026-08-10 17:27:43,091 INFO     29 [qwen-vl-text] coord item[18]: text=2.右侧腋窝、纵隔及右肺门见增大淋巴结,最大短径约1.5cm,不均匀强化。考虑MT,, bbox=[186, 381, 745, 397]
2026-08-10 17:27:43,091 INFO     29 [qwen-vl-text] coord item[19]: text=右侧腋窝淋巴结较前缩小,余大致同前。右侧心隔角淋巴结较前增大,短径约0.6cm。, bbox=[186, 395, 748, 410]
2026-08-10 17:27:43,091 INFO     29 [qwen-vl-text] coord item[20]: text=3.心影不大,心包少量积液同前。, bbox=[185, 413, 408, 426]
2026-08-10 17:27:43,091 INFO     29 [qwen-vl-text] coord item[21]: text=4.右侧胸膜不均匀增厚,考虑MT,伴少量积液,同前。, bbox=[185, 426, 544, 441]
2026-08-10 17:27:43,092 INFO     29 [qwen-vl-text] coord item[22]: text=5.肝脏大小形态尚可,肝内散在低密度结节,较大径约2.3cm,大部分界清,增强扫描, bbox=[184, 439, 760, 455]
2026-08-10 17:27:43,092 INFO     29 [qwen-vl-text] coord item[23]: text=未见明显强化,部分界欠清,同前相仿。, bbox=[184, 455, 454, 469]
2026-08-10 17:27:43,092 INFO     29 [qwen-vl-text] coord item[24]: text=6.双肾多发囊肿,较大径约0.4cm,同前。, bbox=[181, 470, 462, 484]
2026-08-10 17:27:43,092 INFO     29 [qwen-vl-text] coord item[25]: text=7.脾脏见稍低密度结节,较大径约0.6cm,边界欠清,边缘似有强化,同前相仿。, bbox=[180, 483, 725, 500]
2026-08-10 17:27:43,092 INFO     29 [qwen-vl-text] coord item[26]: text=8.胰腺、双侧肾上腺未见明显异常密度影。, bbox=[179, 501, 471, 515]
2026-08-10 17:27:43,092 INFO     29 [qwen-vl-text] coord item[27]: text=9.腹膜后见小淋巴结显示,最大短径约0.4cm,大致同前。, bbox=[178, 515, 572, 530]
2026-08-10 17:27:43,092 INFO     29 [qwen-vl-text] coord item[28]: text=10.膀胱充盈尚可,壁未见明显增厚。, bbox=[178, 531, 433, 546]
2026-08-10 17:27:43,092 INFO     29 [qwen-vl-text] coord item[29]: text=11.双侧附件区见致密影同前。子宫大小形态尚可,子宫肌层强化欠均匀,同前相仿,, bbox=[177, 544, 762, 562]
2026-08-10 17:27:43,092 INFO     29 [qwen-vl-text] coord item[30]: text=请结合临床。盆腔少量积液较前增多。, bbox=[177, 562, 441, 577]
2026-08-10 17:27:43,092 INFO     29 [qwen-vl-text] coord item[31]: text=12.双侧髂血管及腹股沟区未见明显增大淋巴结。, bbox=[176, 577, 513, 593]
2026-08-10 17:27:43,092 INFO     29 [qwen-vl-text] coord item[32]: text=13.骨窗部分肋骨多发斑片状密度增高影,周围软组织增厚,增强后明显强化。考虑, bbox=[175, 591, 760, 609]
2026-08-10 17:27:43,092 INFO     29 [qwen-vl-text] coord item[33]: text=MT,大致同前。, bbox=[172, 613, 279, 627]
2026-08-10 17:27:43,092 INFO     29 [qwen-vl-text] coord item[34]: text=印象:, bbox=[178, 635, 225, 651]
2026-08-10 17:27:43,092 INFO     29 [qwen-vl-text] coord item[35]: text=报告者:王二娟, bbox=[174, 757, 319, 775]
2026-08-10 17:27:43,092 INFO     29 [qwen-vl-text] coord item[36]: text=审核医师: 何晶晶, bbox=[373, 750, 577, 777]
2026-08-10 17:27:43,092 INFO     29 [qwen-vl-text] coord item[37]: text=日期:1/13/2026 2:11:3, bbox=[577, 749, 783, 769]
2026-08-10 17:27:43,092 INFO     29 [qwen-vl-text] coord item[38]: text=本报告仅供临床医师参考,不作为法律依据。妥善保管,遗失不补。, bbox=[200, 780, 695, 801]
2026-08-10 17:27:43,093 INFO     29 [qwen-vl-text] page=2 — 39/39 coords, api_time=13.1s
2026-08-10 17:27:43,093 INFO     29 [qwen-vl-text] new_positions (39):
[[2, 254.78839477539063, 341.1068930053711, 158.27720458984376, 172.58950500488282], [2, 120.25059753417969, 166.0886965942383, 182.69230529785156, 193.6370056152344], [2, 357.77529266357425, 439.331390991211, 179.32470520019533, 189.42750549316406], [2, 117.27409759521485, 143.4672970581055, 202.89790588378906, 213.8426062011719], [2, 189.90069610595705, 225.61869537353516, 201.21410583496095, 213.00070617675783], [2, 238.1199951171875, 314.31839355468753, 200.3722058105469, 212.15880615234377], [2, 358.9658926391602, 394.6838919067383, 198.68840576171877, 209.63310607910157], [2, 117.27409759521485, 202.99729583740236, 218.05210632324219, 228.15490661621095], [2, 273.83799438476564, 369.08599243164065, 214.68450622558595, 225.62920654296875], [2, 116.08349761962891, 202.4019958496094, 231.5225067138672, 241.62530700683595], [2, 230.9763952636719, 254.19309478759766, 229.83870666503907, 239.09960693359375], [2, 272.6473944091797, 427.4253912353516, 227.3130065917969, 238.2577069091797], [2, 115.48819763183594, 295.8640939331055, 243.30910705566407, 253.4119073486328], [2, 114.29759765625, 161.9215966796875, 266.88230773925784, 277.82700805664064], [2, 112.5116976928711, 250.0259948730469, 279.51080810546875, 289.6136083984375], [2, 111.91639770507813, 450.6420907592774, 287.0879083251953, 300.5583087158203], [2, 111.91639770507813, 438.736091003418, 298.8745086669922, 311.5030090332031], [2, 111.91639770507813, 124.41769744873048, 313.1868090820313, 323.289609375], [2, 110.72579772949219, 443.49849090576174, 320.76390930175785, 334.23430969238285], [2, 110.72579772949219, 445.2843908691406, 332.5505096435547, 345.17901000976565], [2, 110.13049774169923, 242.88239501953126, 347.70471008300785, 358.64941040039065], [2, 110.13049774169923, 323.843193359375, 358.64941040039065, 371.27791076660156], [2, 109.53519775390626, 452.42799072265626, 369.59411071777345, 383.06451110839845], [2, 109.53519775390626, 270.2661944580078, 383.06451110839845, 394.85111145019533], [2, 107.74929779052735, 275.0285943603516, 395.69301147460936, 407.47961181640625], [2, 107.15399780273438, 431.59249114990234, 406.6377117919922, 420.95001220703125], [2, 106.55869781494141, 280.3862942504883, 421.79191223144534, 433.5785125732422], [2, 105.96339782714844, 340.51159301757815, 433.5785125732422, 446.20701293945314], [2, 105.96339782714844, 257.7648947143555, 447.0489129638672, 459.67741333007814], [2, 105.36809783935547, 453.6185906982422, 457.99361328125, 473.14781372070314], [2, 105.36809783935547, 262.52729461669924, 473.14781372070314, 485.77631408691406], [2, 104.7727978515625, 305.38889373779296, 485.77631408691406, 499.24671447753906], [2, 104.17749786376953, 452.42799072265626, 497.56291442871094, 512.7171148681641], [2, 102.39159790039064, 166.0886965942383, 516.0847149658204, 527.8713153076172], [2, 105.96339782714844, 133.94249725341797, 534.6065155029297, 548.0769158935547], [2, 103.58219787597656, 189.90069610595705, 637.3183184814453, 652.4725189208984], [2, 222.04689544677734, 343.48809295654297, 631.4250183105469, 654.1563189697266], [2, 343.48809295654297, 466.11989044189454, 630.5831182861328, 647.4211187744141], [2, 119.05999755859375, 413.7334915161133, 656.6820190429688, 674.361919555664]]
2026-08-10 17:27:43,093 INFO     29 [qwen-vl-text] ═══ DONE ═══ 39 positions, pages=1, time=18.3s
2026-08-10 17:27:43,093 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:27:43,101 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:27:43,101 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 17:27:43,101 INFO     29 [qwen-vl-text] positions(41): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:27:43,101 INFO     29 [qwen-vl-text] page grouping: [3], lines per page: [41]
2026-08-10 17:27:43,224 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 17:27:43,225 INFO     29 [qwen-vl-text] LLM extraction start, text_len=868
2026-08-10 17:27:43,225 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:27:43,227 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 69, \"bbox_end\": 109, \"encounter_dates\": [\"2026-02-26\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "CT检查报告单\n患者编号:\n放射编号:\n扫描日期:2/26/2026\n姓名:\n性别:女\n年龄:59岁科别:\n住院号:\n扫描设备:SIEMENS_CT\n扫描方法:平扫+增强12张\n药品:碘普罗胺注射液\n100ml\n药品处理方式:静脉+静脉留置+高压注射\n检查项目:上腹+下腹+盆腔+胸部(平扫+增强)\n检查所见:\n参阅2026-01-13胸部CT前片,所见如下:\n1.右肺可见巨大不规则肿块,病变范围较广,累及右全肺,增强扫描不均匀强化,较前\n局部增大(8-31较原片7-31);余双肺见多发结节影,部分内可见空泡,最大径约\n2cm,较前基本相仿。\n2.右侧腋窝、纵隔及右肺门见增大淋巴结,最大短径约1.5cm,增强扫描呈不均匀强\n化,考虑MT,大致同前。右侧心隔角可见稍大淋巴结,短径约0.6cm,同前相仿。\n3.心影不大,心包少量积液同前。\n4.右侧胸膜不均匀增厚,考虑MT,伴少量积液,同前。\n5.肝脏大小形态尚可,肝内散在低密度结节,较大径约2.3cm,大部分界清,增强扫描\n未见明显强化,部分考虑囊肿,部分不典型,同前相仿。\n6.肝内新增稍低密度结节影,较大者位于肝S6段,径约1.7cm,增强扫描呈轻度强化,\nMT不除外,建议MRI检查。\n7.双肾多发囊肿,较大径约0.4cm,同前。脾脏见稍低密度结节,较大径约0.6cm,边界\n欠清,边缘似有强化,同前相仿。\n8.胰腺、双侧肾上腺未见明显异常密度影。\n9.腹膜后见小淋巴结显示,最大短径约0.4cm,大致同前。\n10.膀胱充盈尚可,壁未见明显增厚。\n11.双侧附件区见致密影同前。子宫大小形态尚可,子宫肌层强化欠均匀,同前相仿,\n请结合临床。盆腔少量积液同前。\n12.双侧髂血管及腹股沟区未见明显增大淋巴结。\n13.骨窗:部分肋骨多发斑片状密度增高影,周围软组织增厚,增强后明显强化,考虑\nMT,大致同前。骶管内囊性灶,同前。\n检查者:武康\n报告者:杨东宇审核医师:侯可\n日期:2/26/2026 3:00:48\n本报告仅供临床医师参考,不作为法律依据。妥善保管,遗失不补。",
    "role": "user"
  }
]
2026-08-10 17:27:43,233 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:27:43.231+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 80, "failed": 0, "current": {"15f63a1a94e011f1bd9827cf206dfa2d": {"id": "15f63a1a94e011f1bd9827cf206dfa2d", "doc_id": "15bf5b9494e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "size": 6574298, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786382558729, "task_type": "dataflow", "root_trace_id": "e45d0687fc994f25a61430b755af4825", "root_traceparent": "00-e45d0687fc994f25a61430b755af4825-4f140d87c9e2cd09-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:27:48,748 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:27:48,748 INFO     29 [qwen-vl-text] LLM output (len=977):
{
  "exam_date": "2026-02-26",
  "report_date": "2026-02-26",
  "exam_name": "上腹+下腹+盆腔+胸部(平扫+增强)",
  "exam_category": "imaging",
  "body_part": "上腹+下腹+盆腔+胸部",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "参阅2026-01-13胸部CT前片,所见如下:\n1.右肺可见巨大不规则肿块,病变范围较广,累及右全肺,增强扫描不均匀强化,较前局部增大(8-31较原片7-31);余双肺见多发结节影,部分内可见空泡,最大径约2cm,较前基本相仿。\n2.右侧腋窝、纵隔及右肺门见增大淋巴结,最大短径约1.5cm,增强扫描呈不均匀强化,考虑MT,大致同前。右侧心隔角可见稍大淋巴结,短径约0.6cm,同前相仿。\n3.心影不大,心包少量积液同前。\n4.右侧胸膜不均匀增厚,考虑MT,伴少量积液,同前。\n5.肝脏大小形态尚可,肝内散在低密度结节,较大径约2.3cm,大部分界清,增强扫描未见明显强化,部分考虑囊肿,部分不典型,同前相仿。\n6.肝内新增稍低密度结节影,较大者位于肝S6段,径约1.7cm,增强扫描呈轻度强化,MT不除外,建议MRI检查。\n7.双肾多发囊肿,较大径约0.4cm,同前。脾脏见稍低密度结节,较大径约0.6cm,边界欠清,边缘似有强化,同前相仿。\n8.胰腺、双侧肾上腺未见明显异常密度影。\n9.腹膜后见小淋巴结显示,最大短径约0.4cm,大致同前。\n10.膀胱充盈尚可,壁未见明显增厚。\n11.双侧附件区见致密影同前。子宫大小形态尚可,子宫肌层强化欠均匀,同前相仿,请结合临床。盆腔少量积液同前。\n12.双侧髂血管及腹股沟区未见明显增大淋巴结。\n13.骨窗:部分肋骨多发斑片状密度增高影,周围软组织增厚,增强后明显强化,考虑MT,大致同前。骶管内囊性灶,同前。",
  "conclusion": null,
  "physician": "杨东宇",
  "reviewer": "侯可"
}
2026-08-10 17:27:48,750 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1077567, prompt_len=1604
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共41行）
["CT检查报告单", "患者编号:", "放射编号:", "扫描日期:2/26/2026", "姓名:", "性别:女", "年龄:59岁科别:", "住院号:", "扫描设备:SIEMENS_CT", "扫描方法:平扫+增强12张", "药品:碘普罗胺注射液", "100ml", "药品处理方式:静脉+静脉留置+高压注射", "检查项目:上腹+下腹+盆腔+胸部(平扫+增强)", "检查所见:", "参阅2026-01-13胸部CT前片,所见如下:", "1.右肺可见巨大不规则肿块,病变范围较广,累及右全肺,增强扫描不均匀强化,较前", "局部增大(8-31较原片7-31);余双肺见多发结节影,部分内可见空泡,最大径约", "2cm,较前基本相仿。", "2.右侧腋窝、纵隔及右肺门见增大淋巴结,最大短径约1.5cm,增强扫描呈不均匀强", "化,考虑MT,大致同前。右侧心隔角可见稍大淋巴结,短径约0.6cm,同前相仿。", "3.心影不大,心包少量积液同前。", "4.右侧胸膜不均匀增厚,考虑MT,伴少量积液,同前。", "5.肝脏大小形态尚可,肝内散在低密度结节,较大径约2.3cm,大部分界清,增强扫描", "未见明显强化,部分考虑囊肿,部分不典型,同前相仿。", "6.肝内新增稍低密度结节影,较大者位于肝S6段,径约1.7cm,增强扫描呈轻度强化,", "MT不除外,建议MRI检查。", "7.双肾多发囊肿,较大径约0.4cm,同前。脾脏见稍低密度结节,较大径约0.6cm,边界", "欠清,边缘似有强化,同前相仿。", "8.胰腺、双侧肾上腺未见明显异常密度影。", "9.腹膜后见小淋巴结显示,最大短径约0.4cm,大致同前。", "10.膀胱充盈尚可,壁未见明显增厚。", "11.双侧附件区见致密影同前。子宫大小形态尚可,子宫肌层强化欠均匀,同前相仿,", "请结合临床。盆腔少量积液同前。", "12.双侧髂血管及腹股沟区未见明显增大淋巴结。", "13.骨窗:部分肋骨多发斑片状密度增高影,周围软组织增厚,增强后明显强化,考虑", "MT,大致同前。骶管内囊性灶,同前。", "检查者:武康", "报告者:杨东宇审核医师:侯可", "日期:2/26/2026 3:00:48", "本报告仅供临床医师参考,不作为法律依据。妥善保管,遗失不补。"]

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
2026-08-10 17:28:09,501 INFO     29 [qwen-vl-text] coord API raw response (len=3875):
[
	{"text": "CT检查报告单", "bbox": [405, 251, 532, 271]},
	{"text": "患者编号:", "bbox": [210, 285, 275, 300], "bbox": [210, 285, 275, 300]},
	{"text": "放射编号:", "bbox": [363, 278, 431, 293], "bbox": [363, 278, 431, 293]},
	{"text": "扫描日期:2/26/2026", "bbox": [556, 267, 674, 283], "bbox": [556, 267, 674, 283]},
	{"text": "姓名:", "bbox": [208, 307, 248, 320], "bbox": [208, 307, 248, 320]},
	{"text": "性别:女", "bbox": [314, 302, 367, 317], "bbox": [314, 302, 367, 317]},
	{"text": "年龄:59岁科别:", "bbox": [383, 296, 495, 313], "bbox": [383, 296, 495, 313]},
	{"text": "住院号:", "bbox": [558, 289, 612, 303], "bbox": [558, 289, 612, 303]},
	{"text": "扫描设备:SIEMENS_CT", "bbox": [209, 321, 335, 336], "bbox": [209, 321, 335, 336]},
	{"text": "扫描方法:平扫+增强12张", "bbox": [436, 306, 582, 325], "bbox": [436, 306, 582, 325]},
	{"text": "药品:碘普罗胺注射液", "bbox": [208, 335, 335, 350], "bbox": [208, 335, 335, 350]},
	{"text": "100ml", "bbox": [375, 331, 410, 343], "bbox": [375, 331, 410, 343]},
	{"text": "药品处理方式:静脉+静脉留置+高压注射", "bbox": [436, 317, 661, 339], "bbox": [436, 317, 661, 339]},
	{"text": "检查项目:上腹+下腹+盆腔+胸部(平扫+增强)", "bbox": [208, 343, 471, 362], "bbox": [208, 343, 471, 362]},
	{"text": "检查所见:", "bbox": [209, 373, 279, 387], "bbox": [209, 373, 279, 387]},
	{"text": "参阅2026-01-13胸部CT前片,所见如下:", "bbox": [208, 379, 433, 398], "bbox": [208, 379, 433, 398]},
	{"text": "1.右肺可见巨大不规则肿块,病变范围较广,累及右全肺,增强扫描不均匀强化,较前", "bbox": [208, 377, 697, 411], "bbox": [208, 377, 697, 411]},
	{"text": "局部增大(8-31较原片7-31);余双肺见多发结节影,部分内可见空泡,最大径约", "bbox": [208, 390, 673, 423], "bbox": [208, 390, 673, 423]},
	{"text": "2cm,较前基本相仿。", "bbox": [208, 419, 326, 434], "bbox": [208, 419, 326, 434]},
	{"text": "2.右侧腋窝、纵隔及右肺门见增大淋巴结,最大短径约1.5cm,增强扫描呈不均匀强", "bbox": [208, 413, 684, 446], "bbox": [208, 413, 684, 446]},
	{"text": "化,考虑MT,大致同前。右侧心隔角可见稍大淋巴结,短径约0.6cm,同前相仿。", "bbox": [208, 425, 666, 458], "bbox": [208, 425, 666, 458]},
	{"text": "3.心影不大,心包少量积液同前。", "bbox": [208, 452, 402, 470], "bbox": [208, 452, 402, 470]},
	{"text": "4.右侧胸膜不均匀增厚,考虑MT,伴少量积液,同前。", "bbox": [208, 458, 519, 482], "bbox": [208, 458, 519, 482]},
	{"text": "5.肝脏大小形态尚可,肝内散在低密度结节,较大径约2.3cm,大部分界清,增强扫描", "bbox": [208, 461, 704, 496], "bbox": [208, 461, 704, 496]},
	{"text": "未见明显强化,部分考虑囊肿,部分不典型,同前相仿。", "bbox": [208, 480, 535, 506], "bbox": [208, 480, 535, 506]},
	{"text": "6.肝内新增稍低密度结节影,较大者位于肝S6段,径约1.7cm,增强扫描呈轻度强化,", "bbox": [208, 485, 700, 519], "bbox": [208, 485, 700, 519]},
	{"text": "MT不除外,建议MRI检查。", "bbox": [208, 515, 360, 532], "bbox": [208, 515, 360, 532]},
	{"text": "7.双肾多发囊肿,较大径约0.4cm,同前。脾脏见稍低密度结节,较大径约0.6cm,边界", "bbox": [208, 509, 718, 546], "bbox": [208, 509, 718, 546]},
	{"text": "欠清,边缘似有强化,同前相仿。", "bbox": [208, 537, 409, 557], "bbox": [208, 537, 409, 557]},
	{"text": "8.胰腺、双侧肾上腺未见明显异常密度影。", "bbox": [208, 547, 463, 571], "bbox": [208, 547, 463, 571]},
	{"text": "9.腹膜后见小淋巴结显示,最大短径约0.4cm,大致同前。", "bbox": [208, 556, 551, 584], "bbox": [208, 556, 551, 584]},
	{"text": "10.膀胱充盈尚可,壁未见明显增厚。", "bbox": [210, 577, 433, 600], "bbox": [210, 577, 433, 600]},
	{"text": "11.双侧附件区见致密影同前。子宫大小形态尚可,子宫肌层强化欠均匀,同前相仿,", "bbox": [210, 574, 715, 614], "bbox": [210, 574, 715, 614]},
	{"text": "请结合临床。盆腔少量积液同前。", "bbox": [210, 605, 401, 627], "bbox": [210, 605, 401, 627]},
	{"text": "12.双侧髂血管及腹股沟区未见明显增大淋巴结。", "bbox": [210, 613, 504, 641], "bbox": [210, 613, 504, 641]},
	{"text": "13.骨窗:部分肋骨多发斑片状密度增高影,周围软组织增厚,增强后明显强化,考虑", "bbox": [210, 614, 730, 657], "bbox": [210, 614, 730, 657]},
	{"text": "MT,大致同前。骶管内囊性灶,同前。", "bbox": [210, 644, 446, 669], "bbox": [210, 644, 446, 669]},
	{"text": "检查者:武康", "bbox": [214, 748, 314, 770], "bbox": [214, 748, 314, 770]},
	{"text": "报告者:杨东宇审核医师:侯可", "bbox": [335, 733, 532, 761], "bbox": [335, 733, 532, 761]},
	{"text": "日期:2/26/2026 3:00:48", "bbox": [615, 720, 801, 745], "bbox": [615, 720, 801, 745]},
	{"text": "本报告仅供临床医师参考,不作为法律依据。妥善保管,遗失不补。", "bbox": [244, 751, 667, 791], "bbox": [244, 751, 667, 791]}
]
2026-08-10 17:28:09,501 INFO     29 [qwen-vl-text] coord API: raw_items=41, valid_items=41, elapsed=20.8s
2026-08-10 17:28:09,501 INFO     29 [qwen-vl-text] coord item[0]: text=CT检查报告单, bbox=[405, 251, 532, 271]
2026-08-10 17:28:09,501 INFO     29 [qwen-vl-text] coord item[1]: text=患者编号:, bbox=[210, 285, 275, 300]
2026-08-10 17:28:09,501 INFO     29 [qwen-vl-text] coord item[2]: text=放射编号:, bbox=[363, 278, 431, 293]
2026-08-10 17:28:09,501 INFO     29 [qwen-vl-text] coord item[3]: text=扫描日期:2/26/2026, bbox=[556, 267, 674, 283]
2026-08-10 17:28:09,501 INFO     29 [qwen-vl-text] coord item[4]: text=姓名:, bbox=[208, 307, 248, 320]
2026-08-10 17:28:09,501 INFO     29 [qwen-vl-text] coord item[5]: text=性别:女, bbox=[314, 302, 367, 317]
2026-08-10 17:28:09,501 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:59岁科别:, bbox=[383, 296, 495, 313]
2026-08-10 17:28:09,501 INFO     29 [qwen-vl-text] coord item[7]: text=住院号:, bbox=[558, 289, 612, 303]
2026-08-10 17:28:09,501 INFO     29 [qwen-vl-text] coord item[8]: text=扫描设备:SIEMENS_CT, bbox=[209, 321, 335, 336]
2026-08-10 17:28:09,501 INFO     29 [qwen-vl-text] coord item[9]: text=扫描方法:平扫+增强12张, bbox=[436, 306, 582, 325]
2026-08-10 17:28:09,501 INFO     29 [qwen-vl-text] coord item[10]: text=药品:碘普罗胺注射液, bbox=[208, 335, 335, 350]
2026-08-10 17:28:09,501 INFO     29 [qwen-vl-text] coord item[11]: text=100ml, bbox=[375, 331, 410, 343]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[12]: text=药品处理方式:静脉+静脉留置+高压注射, bbox=[436, 317, 661, 339]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[13]: text=检查项目:上腹+下腹+盆腔+胸部(平扫+增强), bbox=[208, 343, 471, 362]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[14]: text=检查所见:, bbox=[209, 373, 279, 387]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[15]: text=参阅2026-01-13胸部CT前片,所见如下:, bbox=[208, 379, 433, 398]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[16]: text=1.右肺可见巨大不规则肿块,病变范围较广,累及右全肺,增强扫描不均匀强化,较前, bbox=[208, 377, 697, 411]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[17]: text=局部增大(8-31较原片7-31);余双肺见多发结节影,部分内可见空泡,最大径约, bbox=[208, 390, 673, 423]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[18]: text=2cm,较前基本相仿。, bbox=[208, 419, 326, 434]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[19]: text=2.右侧腋窝、纵隔及右肺门见增大淋巴结,最大短径约1.5cm,增强扫描呈不均匀强, bbox=[208, 413, 684, 446]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[20]: text=化,考虑MT,大致同前。右侧心隔角可见稍大淋巴结,短径约0.6cm,同前相仿。, bbox=[208, 425, 666, 458]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[21]: text=3.心影不大,心包少量积液同前。, bbox=[208, 452, 402, 470]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[22]: text=4.右侧胸膜不均匀增厚,考虑MT,伴少量积液,同前。, bbox=[208, 458, 519, 482]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[23]: text=5.肝脏大小形态尚可,肝内散在低密度结节,较大径约2.3cm,大部分界清,增强扫描, bbox=[208, 461, 704, 496]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[24]: text=未见明显强化,部分考虑囊肿,部分不典型,同前相仿。, bbox=[208, 480, 535, 506]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[25]: text=6.肝内新增稍低密度结节影,较大者位于肝S6段,径约1.7cm,增强扫描呈轻度强化,, bbox=[208, 485, 700, 519]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[26]: text=MT不除外,建议MRI检查。, bbox=[208, 515, 360, 532]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[27]: text=7.双肾多发囊肿,较大径约0.4cm,同前。脾脏见稍低密度结节,较大径约0.6cm,边界, bbox=[208, 509, 718, 546]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[28]: text=欠清,边缘似有强化,同前相仿。, bbox=[208, 537, 409, 557]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[29]: text=8.胰腺、双侧肾上腺未见明显异常密度影。, bbox=[208, 547, 463, 571]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[30]: text=9.腹膜后见小淋巴结显示,最大短径约0.4cm,大致同前。, bbox=[208, 556, 551, 584]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[31]: text=10.膀胱充盈尚可,壁未见明显增厚。, bbox=[210, 577, 433, 600]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[32]: text=11.双侧附件区见致密影同前。子宫大小形态尚可,子宫肌层强化欠均匀,同前相仿,, bbox=[210, 574, 715, 614]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[33]: text=请结合临床。盆腔少量积液同前。, bbox=[210, 605, 401, 627]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[34]: text=12.双侧髂血管及腹股沟区未见明显增大淋巴结。, bbox=[210, 613, 504, 641]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[35]: text=13.骨窗:部分肋骨多发斑片状密度增高影,周围软组织增厚,增强后明显强化,考虑, bbox=[210, 614, 730, 657]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[36]: text=MT,大致同前。骶管内囊性灶,同前。, bbox=[210, 644, 446, 669]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[37]: text=检查者:武康, bbox=[214, 748, 314, 770]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[38]: text=报告者:杨东宇审核医师:侯可, bbox=[335, 733, 532, 761]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[39]: text=日期:2/26/2026 3:00:48, bbox=[615, 720, 801, 745]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] coord item[40]: text=本报告仅供临床医师参考,不作为法律依据。妥善保管,遗失不补。, bbox=[244, 751, 667, 791]
2026-08-10 17:28:09,502 INFO     29 [qwen-vl-text] page=3 — 41/41 coords, api_time=20.8s
2026-08-10 17:28:09,503 INFO     29 [qwen-vl-text] new_positions (41):
[[3, 241.09649505615235, 316.6995935058594, 211.31690612792968, 228.15490661621095], [3, 125.01299743652345, 163.7074966430664, 239.94150695800784, 252.57000732421875], [3, 216.09389556884767, 256.57429473876954, 234.0482067871094, 246.6767071533203], [3, 330.98679321289063, 401.23219177246096, 224.7873065185547, 238.2577069091797], [3, 123.82239746093751, 147.63439697265625, 258.4633074951172, 269.4080078125], [3, 186.9241961669922, 218.47509552001955, 254.2538073730469, 266.88230773925784], [3, 227.99989532470704, 294.67349395751955, 249.2024072265625, 263.51470764160155], [3, 332.1773931884766, 364.3235925292969, 243.30910705566407, 255.09570739746096], [3, 124.41769744873048, 199.42549591064454, 270.2499078369141, 282.878408203125], [3, 259.55079467773436, 346.46459289550785, 257.62140747070316, 273.6175079345703], [3, 123.82239746093751, 199.42549591064454, 282.03650817871096, 294.6650085449219], [3, 223.23749542236328, 244.0729949951172, 278.6689080810547, 288.77170837402343], [3, 259.55079467773436, 393.4932919311524, 266.88230773925784, 285.4041082763672], [3, 123.82239746093751, 280.3862942504883, 288.77170837402343, 304.76780883789064], [3, 124.41769744873048, 166.0886965942383, 314.0287091064453, 325.8153094482422], [3, 123.82239746093751, 257.7648947143555, 319.0801092529297, 335.0762097167969], [3, 123.82239746093751, 414.92409149169924, 317.39630920410156, 346.0209100341797], [3, 123.82239746093751, 400.63689178466797, 328.3410095214844, 356.12371032714844], [3, 123.82239746093751, 194.0677960205078, 352.7561102294922, 365.3846105957031], [3, 123.82239746093751, 407.18519165039066, 347.70471008300785, 375.4874108886719], [3, 123.82239746093751, 396.4697918701172, 357.80751037597656, 385.59021118164065], [3, 123.82239746093751, 239.31059509277344, 380.53881103515624, 395.69301147460936], [3, 123.82239746093751, 308.9606936645508, 385.59021118164065, 405.79581176757813], [3, 123.82239746093751, 419.09119140625, 388.1159112548828, 417.582412109375], [3, 123.82239746093751, 318.4854934692383, 404.11201171875, 426.00141235351566], [3, 123.82239746093751, 416.7099914550781, 408.32151184082034, 436.94611267089846], [3, 123.82239746093751, 214.30799560546876, 433.5785125732422, 447.89081298828125], [3, 123.82239746093751, 427.4253912353516, 428.5271124267578, 459.67741333007814], [3, 123.82239746093751, 243.47769500732423, 452.1003131103516, 468.9383135986328], [3, 123.82239746093751, 275.6238943481445, 460.5193133544922, 480.7249139404297], [3, 123.82239746093751, 328.0102932739258, 468.0964135742188, 491.6696142578125], [3, 125.01299743652345, 257.7648947143555, 485.77631408691406, 505.1400146484375], [3, 125.01299743652345, 425.6394912719727, 483.2506140136719, 516.9266149902344], [3, 125.01299743652345, 238.71529510498047, 509.3495147705078, 527.8713153076172], [3, 125.01299743652345, 300.03119384765625, 516.0847149658204, 539.6579156494141], [3, 125.01299743652345, 434.5689910888672, 516.9266149902344, 553.1283160400391], [3, 125.01299743652345, 265.50379455566406, 542.1836157226562, 563.2311163330079], [3, 127.39419738769531, 186.9241961669922, 629.7412182617188, 648.2630187988282], [3, 199.42549591064454, 316.6995935058594, 617.1127178955078, 640.6859185791016], [3, 366.10949249267577, 476.835290222168, 606.168017578125, 627.2155181884766], [3, 145.25319702148437, 397.06509185791015, 632.2669183349609, 665.9429193115235]]
2026-08-10 17:28:09,503 INFO     29 [qwen-vl-text] ═══ DONE ═══ 41 positions, pages=1, time=26.4s
2026-08-10 17:28:09,513 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 17:28:09,514 INFO     29 [Trace] task=15f63a1a | doc=06-临沂人民-LSPI，后线肺癌，方穹招募.pdf | Extractor:ExaminationReport | outputs={"chunks": "3 items, types={'ExaminationReport': 3}", "html": "", "json": "491 items", "markdown": "", "text": "", "name": "06-临沂人民-LSPI，后线肺癌，方穹招募.pdf", "output_format": "chunks", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Examination\": 3, \"chunks_Discharge\": 1, \"chunks_Clinical\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 17:28:09,514 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 17:28:09,521 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:28:09,521 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 17:28:12,517 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:28:12,532 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 17:28:12,533 INFO     29 [Trace] task=15f63a1a | doc=06-临沂人民-LSPI，后线肺癌，方穹招募.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "491 items", "markdown": "", "text": "", "name": "06-临沂人民-LSPI，后线肺癌，方穹招募.pdf", "output_format": "chunks", "chunks_Examination": "3 items, types={'ExaminationReport': 3}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Examination\": 3, \"chunks_Discharge\": 1, \"chunks_Clinical\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 17:28:12,533 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 17:28:12,534 INFO     29 [ChunkMerger] Merged 9 chunks from 9 sources: {'Extractor:LabExam': 4, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 3, 'Extractor:Progress': 1} (filtered 5 noise chunks)
2026-08-10 17:28:12,550 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 17:28:12,550 INFO     29 [Trace] task=15f63a1a | doc=06-临沂人民-LSPI，后线肺癌，方穹招募.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "9 items, types={'LabReport': 4, 'OutpatientRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 3}", "name": "06-临沂人民-LSPI，后线肺癌，方穹招募.pdf"}
2026-08-10 17:28:12,550 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 17:28:12,728 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786382558992, 'update_date': datetime.datetime(2026, 8, 10, 17, 22, 38), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1283955, 'status': '1'}
2026-08-10 17:28:12,930 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   EGFR c.2369C>T (p.T790M)  EGFR  6.6%  %  None  True    EGFR c.2235_2249del (p.E746_A750del)  EGFR  24.4%  %  None  True    APC  None  c.4487C>G (p.T1496S)  None  None  True    EGFR  None  NM_005228 exon19  None  None  True    EGFR c.2235_2249del (p.E746_A750del)  None  检出  None  None  True    EGFR c.2369C>T (p.T790M)  None  检出  None  None  True    EGFR 基因拷贝数  EGFR  未扩增  None  None  False    ERBB2 基因拷贝数  ERBB2  未扩增  None  None  False    MET 基因拷贝数  MET  未扩增  None  None  False    FGFR1 基因拷贝数  FGFR1  未扩增  None  None  False    ALK 融合基因  ALK  未检出  None  None  False    FGFR1 融合基因  FGFR1  未检出  None  None  False    FGFR2 融合基因  FGFR2  未检出  None  None  False    NTRK1 融合基因  NTRK1  未检出  None  None  False    NTRK2 融合基因  NTRK2  未检出  None  None  False    NTRK3 融合基因  NTRK3  未检出  None  None  False    RET 融合基因  RET  未检出  None  None  False    ROS1 融合基因  ROS1  未检出  None  None  False   
---
   尿液分析-酸碱度  PH  5.0  None  4.5~8.0  False    尿液分析-亚硝酸盐  NIT  --  None  阴性(-)  False    尿液分析-葡萄糖  GLU  --  None  阴性(-)  False    尿液分析-比重  SG  1.024  None  1.003~1.030  False    尿液分析-潜血  BLD  2+  None  阴性(-)  True    尿液分析-蛋白质  PRO  --  None  阴性(-)  False    尿液分析-胆红素  BIL  --  None  阴性(-)  False    尿液分析-尿胆原  URO  --  None  阴性(-)  False    尿液分析-酮体  KET  --  None  阴性(-)  False    尿液分析-白细胞  LEU  2+  None  阴性(-)  True    尿液分析-颜色  COL  稍黄色  None  黄色  False    尿液分析-浊度  TURB  清晰  None  清晰  False    尿液-白细胞UF  WBC  34.1  /ul  0.0~30.0  True    尿液-红细胞UF  RBC  8.7  /ul  0.0~25.0  False    尿液-上皮细胞UF  EC  19.5  /ul  0.0~15.0  True    尿液-细菌UF  BACT  191.1  /ul  0.0~6000.0  False    尿液-管型UF  CAST  0.00  /ul  0.00~0.70  False    尿液-结晶UF  X-TAL  0.1  /ul  None  False    尿液-类酵母菌UF  YLC  0.0  /ul  None  False    尿液-粘液UF  MUCUS  0.12  /ul  None  False    红细胞信息  RBC-Info  未提示  mS/cm  3.10~39.00  False    电导率  CONDCT  24.70  None  阴性(-)  False    其他  ELS  阴性(-)  None  None  False   
---
   血清丙氨酸氨基转移酶测定  ALT  41.0  U/L  7.0~40.0  True    血清天门冬氨酸氨基转移酶测定  AST  56.3  U/L  13.0~35.0  True    AST/ALT  AST/ALT  1.37  None  None  False    乳酸脱氢酶测定  LDH  151.4  U/L  120.0~250.0  False    总蛋白  TP  67.5  g/L  65.0~85.0  False    白蛋白  ALB  37.6  g/L  40.0~55.0  True    球蛋白  GLB  29.9  g/L  20.0~40.0  False    白球比  A/G  1.3  None  1.2~2.4  False    血清碱性磷酸酶测定  ALP  117.6  U/L  50.0~135.0  False    总胆红素  TBIL  12.2  µmol/L  ≤23.0  False    葡萄糖测定  GLU  5.0  mmol/L  3.9~6.1  False    尿素测定  UREA  5.9  mmol/L  2.6~7.5  False    肌酐测定  CREA  78.8  µmol/L  41.0~73.0  True    尿酸测定  UA  211.5  µmol/L  154.7~357.0  False    钾测定  K  4.24  mmol/L  3.50~5.30  False    钠测定  NA  138.6  mmol/L  137.0~147.0  False    氯测定  CL  104.2  mmol/L  99.0~110.0  False    钙测定  CA  2.27  mmol/L  2.11~2.52  False    磷测定  P  1.37  mmol/L  0.85~1.51  False    镁测定  MG  0.86  mmol/L  0.75~1.02  False    血清甘油三酯  TG  0.84  mmol/L  ≤1.70  False    血清总胆固醇  TCH  3.25  mmol/L  3.00~5.70  False    血清肌酸激酶  CK  204  U/L  40~200  True    脂蛋白  LPS  28.3  U/L  <67.0  False    淀粉酶  AMY  55  U/L  35~135  False   
---
   白细胞计数  WBC  4.35  *10^9/L  3.50~9.50  False    中性粒细胞百分数  Neut%  65.1  %  40.0~75.0  False    淋巴细胞百分数  Lymph%  23.2  %  20.0~50.0  False    单核细胞百分数  Mono%  7.4  %  3.0~10.0  False    嗜酸性粒细胞百分数  Eos%  3.4  %  0.4~8.0  False    嗜碱性粒细胞百分数  Baso%  0.9  %  0.0~1.0  False    中性粒细胞绝对值  Neut#  2.83  *10^9/L  1.80~6.30  False    淋巴细胞绝对值  Lymph#  1.01  *10^9/L  1.10~3.20  True    单核细胞绝对值  Mono#  0.32  *10^9/L  0.10~0.60  False    嗜酸性粒细胞绝对值  Eos#  0.15  *10^9/L  0.02~0.52  False    嗜碱性粒细胞绝对值  Baso#  0.04  *10^9/L  0.00~0.06  False    红细胞计数  RBC  4.10  *10^12/L  3.80~5.10  False    血红蛋白  Hb  124  g/L  115~150  False    红细胞比容  Hct  0.39  L/L  0.35~0.45  False    平均红细胞容积  MCV  94.1  fL  82.0~100.0  False    平均红细胞血红蛋白量  MCH  30.2  pg  27.0~34.0  False    平均红细胞血红蛋白浓度  MCHC  321  g/L  316~354  False    红细胞分布宽度-标准差  RDW-SD  57.1  fL  41.9~53.9  True    红细胞分布宽度-变异系数  RDW-CV  16.8  %  12.1~15.2  True    血小板计数  PLT  175  *10^9/L  125~350  False    血小板体积分布宽度  PDW  12.9  fL  9.5~15.2  False    血小板平均体积  MPV  11.2  fL  9.2~12.1  False    血小板压积  PCT  0.20  %  0.19~0.40  False    大血小板比率  P-LCR  33.9  %  19.6~42.6  False   
---
科室：呼吸内科
姓名：
门诊病历号：
[初诊病历记录(门诊放化疗患者专用)]
就诊时间：2026年02月27日10时50分
科别：呼吸内科
主诉：确诊右肺腺癌5+年，临床试验中
现病史：患者于2020-8开始出现咳嗽，咳痰伴右侧胸痛，就诊于
完善相关检查，
诊断：右肺腺癌，双肺多发转移，（具体转移不详）突变类型 Exon21-L858R突变，Exon19缺失突
变，KRAS突变，一直维持吉非替尼治疗。2025-11复查病情病情进展，PFS1：63个月。诊断：右肺
腺癌（驱动基因阴性） 右肺门、纵隔及右侧腋窝多发淋巴结转移 双肺多发转移 右侧胸膜转移
肋骨转移。受试者于2025年11月11日签署知情同意书，自愿参加一项评估HLX43（抗PD-L1的ADC）
联合斯鲁利单抗（抗PD-1人源化单克隆抗体注射液）的晚期/转移性实体瘤患者中的安全性、耐受
性和有效性的Ib/II期临床研究（V3.0 2025年08月15日），2025年12月2给予C1D1治疗，2025年12
月24给予C2D1治疗，2026年1月14日给予C3D1治疗，2026年2月5日给予C4D1治疗。现患者无特殊不
适，拟行周期性治疗入院。自发病以来，精神食欲可，大小便无异常，体重未见明显减轻。
既往史：2020年8月诊断：肝囊肿。否认传染病史，无高血压史，否认糖尿病史，否认心脏病史，
否认外伤史，否认输血史，预防接种史：不详，否认食物、药物过敏史。
阳性体征：无
必要的阴性体征和辅助检查：无
诊断：1.右肺恶性肿瘤（腺癌）淋巴结继发恶性肿瘤（右肺门、纵膈、右腋窝）胸膜继发性恶性
肿瘤骨继发恶性肿瘤2.肝囊肿
治疗意见：入组临床试验治疗。
医师签名：一式其其
---
2:11:34 PM
科室：呼吸与危重症医学科 姓名：
出院记录
女，59岁，主因“确诊右肺腺癌5年”于2025-10-20入院。于
2025年10月29日出院，住院天数：9天。
入院情况：患者于2020年8月因咳嗽，咳痰伴右侧胸痛于北京市丰台中西医结合医院
行胸部CT示：右肺门旁软组织团块影，考虑癌可能；8月31日于我院住院治疗，期间完善
支气管镜检查，病理结果示：符合浸润性肺腺癌；基因检测示：EGFR Exon21-L858R突变（
突变比例43.34%），EGFR Exon19缺失突变（突变比例55.81%），KRAS突变（突变比例
27.72%）；予口服吉非替尼片（伊瑞可）靶向治疗至今，2021年1月复查提示病情稳定，此后
患者未规律复查。2023年7月31日于我院住院复查，复查提示病情进展，考虑当前靶向药
耐药，建议患者重新穿刺行基因检查，患者考虑后拒绝，要求继续服药治疗后出院。现患
者为求全面复查及中西医结合诊治入院。入院症见：神志清，精神可，偶有咳嗽，干咳少
痰，活动后稍有气喘，口苦，纳食可，夜眠可，二便正常。舌质暗红，苔薄黄，脉弦滑。
入院诊断：
中医诊断：肺癌
痰瘀互结
西医诊断：右肺腺癌 T2aN2M1a IV期/双肺多发转移/淋巴结多发转移/右侧胸膜
转移/脑转移？/靶向治疗后，肝囊肿，营养不良性贫血，脂肪肝
诊疗经过：入院完善相关检查，指导治疗。化验结果回报：血常规+C反应蛋白：白
细胞计数[WBC]4.810~9/L，红细胞计数[RBC]4.5410^12/L，血红蛋白量[HGB]127.0g/L，
红细胞平均血红蛋白浓度[MCHC]314.0g/L，淋巴细胞绝对值[LY#]1.0310^9/L，C-反应
蛋白[CRP]1.98mg/L。免疫球蛋白E[IgE]8.80IU/mL。肝肾功：白蛋白[ALB]36g/L，高密度
脂蛋白胆固醇[HDL-C]0.92mmol/L，二氧化碳结合力[CO2CP]28.80mmol/L，总蛋白[TP]
60.7g/L，①肾小球滤过率估算[eGFR]84.2ml/min，②肾小球滤过率估算[eGFR]
80.3ml/min。肿瘤标志物示：神经元特异性烯醇化酶[NSE]34.3ng/mL，细胞角蛋白19片段
[CYFRA21-1]11.50ng/mL。甲功示：抗甲状腺过氧化物酶抗体[Anti-TPO]814.00IU/ml。细
胞因子测定、心肌酶谱+C反应蛋白、凝血+D二聚体未见明显异常。心电图示：窦性心律
不齐，心电轴不偏，心电图大致正常。过敏源检测未见明显异常。胸部CT回报：1.符合右
肺ca征像，包绕邻近血管；2.双肺多发结节，考虑MT；3.纵膈、右肺肺门及右侧腋窝淋巴
结MT；4.右侧胸膜不均匀增厚，MT可能性大；5.右侧7、8测前肋MT伴软组织肿块形成、右
侧胸壁增厚；6.所示肝右叶多发低密度影；脾内稍低密度灶；右肾小囊肿可能大；右侧肾
上腺稍增粗，请结合腹部检查。请结合临床及原片，治疗后复查。脑MRI回报：1.右侧脑
室前角旁异常信号，结合病史考虑MT，请结合临床复查；2.左侧上颌窦炎。气管镜检查：
右肺下叶外压性闭塞/支气管镜下炎症性改变。心脏彩超回报：心脏形态结构及功能未见明
电话：
备注
科室：呼吸与危重症医学科 姓名：
显异常。腹部彩超回报：肝囊肿；胆囊张力高；胰脾双肾未见明显异常。淋巴结彩超回
报：右侧锁骨区多发肿大淋巴结，MT；双侧腋窝肿大淋巴结，MT。双侧腹股沟区及腹盆腔
探查未见明显异常肿大淋巴结。病理报告（202510924）：（右肺支气管镜活检组织）送
检组织被覆鳞状上皮呈慢性炎改变；免疫组化：P40(+)P53(低表达)K1-67(+约10%)。液
基细胞学检查（Y252882）：（右肺肺泡灌洗液）支气管上皮细胞，炎细胞，个别非典型
细胞，建议临床进一步检查。全身骨扫描：右侧第7、8侧肋局部及右侧第9肋后肋局部骨
质代谢增高，结合脏器断层显像，考虑MT，与2023-8-21日片对比新发；右侧第4-6前侧肋
局部骨质代谢轻度增高，建议3个月复查；L4-5左侧椎小关节退行性改变，较前未见明显
变化；双侧膝关节骨质代谢增高，考虑骨关节炎性改变。病理图文报告（10239191）：（
右肺）穿刺波变的纤维组织中可见少许癌巢浸润，结合免疫组化符合：肺腺癌，请结合临
床及其他检查综合判断。免疫组化：CK(+)CK7(+)TTF-1(+)Napsin-A(+)P63(-)P40(-)Syn(
一)INSM-1(-)Ki-67(+约20%)BRG1(+)。予抑酸护胃、中药抗肿瘤，气道雾化，氧疗及中医
外治法、中医辨证论治等中西医综合治疗。于10月24日行CT引导下肺穿刺活检以明确病
理。
出院情况：患者神志清，精神可，偶有咳嗽减轻，干咳少痰，活动后稍有气喘，口
苦，纳食可，夜眠可，二便正常。舌质暗红，苔薄黄，脉弦滑。查体：双肺呼吸音清，未
闻及明显干湿性啰音，未闻及捻发音，胸部摩擦音。患者症状好转，要求出院于家中等待
基因检测结果，请示上级医师后，准予出院。
出院诊断：
中医诊断：肺癌
痰瘀互结
西医诊断：右肺腺癌 T2aN2M1a IV期/双肺多发转移/淋巴结多发转移/右侧胸
膜转移/脑转移/骨转移/靶向治疗后，肝囊肿，营养不良性贫血，脂肪肝
出院医嘱：1.院外规律用药，中草药日一剂，定期复诊，不适随诊；2.定期复查胸部
CT、肺功能；3.加强营养，注意保暖，避免感冒；4.做基因检测确定患者基因突变类型。
中医调护：避风寒，慎起居，节饮食，畅情志。
签名：孟丽红
电话：
---
彩色病理图文报告
姓名：
性别：女
年龄：59岁
收到日期：2025-10-24
送检医院：本院
送检科室：肺病科
住院号：
送检医生：0117
标本名称：
蜡块数：1
特征图像：
大体描述：
(右肺)穿刺组织3条，长0.2-0.4CM,直径0.1CM。
病理诊断：
(右肺)穿刺玻变的纤维组织中可见少许癌巢浸润，结合免疫组化符合：肺腺癌，
请结合临床及其它检查综合判断。
免疫组化：CK(+)CK7(+)TTF-1(+)Napsin-A(+)P63(-)P40(-)Syn(-)INSM-1(-)Ki-67
(+约20%)BRG1(+)。
报告医生：张瑜
审核医生：梁晓霞
1.注：此结果仅针对本次送检样本，仅供临床医生参考。如有疑问，请于7个工作日内与病理科联系。报告日期：2025-10-28
2.本报告医师签名有效。
3.本报告电子版仅供参考，请以纸质报告为准。
电话：
---
CT检查报告单
患者编号:
扫描日期: 1/13/2026
姓名:
性别:女
年龄:59岁科别:
住院号:
扫描设备:SIEMENS_CT
扫描方法:平扫+增强12张
药品:碘普罗胺注射液
100ml
药品处理方式:静脉+静脉留置+高压注射
检查项目:上腹+下腹+盆腔+胸部(平扫+增强)
扫描所见:
参考2025-11-21胸部CT,所见如下:
1.右肺可见巨大不规则肿块,病变范围较广,累及右全肺,增强扫描不均匀强化,较前
局部略缩小;余双肺见多发结节影,部分内可见空泡,最大径约2cm,较前部分略缩
小。
2.右侧腋窝、纵隔及右肺门见增大淋巴结,最大短径约1.5cm,不均匀强化。考虑MT,
右侧腋窝淋巴结较前缩小,余大致同前。右侧心隔角淋巴结较前增大,短径约0.6cm。
3.心影不大,心包少量积液同前。
4.右侧胸膜不均匀增厚,考虑MT,伴少量积液,同前。
5.肝脏大小形态尚可,肝内散在低密度结节,较大径约2.3cm,大部分界清,增强扫描
未见明显强化,部分界欠清,同前相仿。
6.双肾多发囊肿,较大径约0.4cm,同前。
7.脾脏见稍低密度结节,较大径约0.6cm,边界欠清,边缘似有强化,同前相仿。
8.胰腺、双侧肾上腺未见明显异常密度影。
9.腹膜后见小淋巴结显示,最大短径约0.4cm,大致同前。
10.膀胱充盈尚可,壁未见明显增厚。
11.双侧附件区见致密影同前。子宫大小形态尚可,子宫肌层强化欠均匀,同前相仿,
请结合临床。盆腔少量积液较前增多。
12.双侧髂血管及腹股沟区未见明显增大淋巴结。
13.骨窗部分肋骨多发斑片状密度增高影,周围软组织增厚,增强后明显强化。考虑
MT,大致同前。
印象:
报告者:王二娟
审核医师: 何晶晶
日期:1/13/2026 2:11:3
本报告仅供临床医师参考,不作为法律依据。妥善保管,遗失不补。
---
CT检查报告单
患者编号:
放射编号:
扫描日期:2/26/2026
姓名:
性别:女
年龄:59岁科别:
住院号:
扫描设备:SIEMENS_CT
扫描方法:平扫+增强12张
药品:碘普罗胺注射液
100ml
药品处理方式:静脉+静脉留置+高压注射
检查项目:上腹+下腹+盆腔+胸部(平扫+增强)
检查所见:
参阅2026-01-13胸部CT前片,所见如下:
1.右肺可见巨大不规则肿块,病变范围较广,累及右全肺,增强扫描不均匀强化,较前
局部增大(8-31较原片7-31);余双肺见多发结节影,部分内可见空泡,最大径约
2cm,较前基本相仿。
2.右侧腋窝、纵隔及右肺门见增大淋巴结,最大短径约1.5cm,增强扫描呈不均匀强
化,考虑MT,大致同前。右侧心隔角可见稍大淋巴结,短径约0.6cm,同前相仿。
3.心影不大,心包少量积液同前。
4.右侧胸膜不均匀增厚,考虑MT,伴少量积液,同前。
5.肝脏大小形态尚可,肝内散在低密度结节,较大径约2.3cm,大部分界清,增强扫描
未见明显强化,部分考虑囊肿,部分不典型,同前相仿。
6.肝内新增稍低密度结节影,较大者位于肝S6段,径约1.7cm,增强扫描呈轻度强化,
MT不除外,建议MRI检查。
7.双肾多发囊肿,较大径约0.4cm,同前。脾脏见稍低密度结节,较大径约0.6cm,边界
欠清,边缘似有强化,同前相仿。
8.胰腺、双侧肾上腺未见明显异常密度影。
9.腹膜后见小淋巴结显示,最大短径约0.4cm,大致同前。
10.膀胱充盈尚可,壁未见明显增厚。
11.双侧附件区见致密影同前。子宫大小形态尚可,子宫肌层强化欠均匀,同前相仿,
请结合临床。盆腔少量积液同前。
12.双侧髂血管及腹股沟区未见明显增大淋巴结。
13.骨窗:部分肋骨多发斑片状密度增高影,周围软组织增厚,增强后明显强化,考虑
MT,大致同前。骶管内囊性灶,同前。
检查者:武康
报告者:杨东宇审核医师:侯可
日期:2/26/2026 3:00:48
本报告仅供临床医师参考,不作为法律依据。妥善保管,遗失不补。
2026-08-10 17:28:13,621 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 17:28:13,622 INFO     29 [Trace] task=15f63a1a | doc=06-临沂人民-LSPI，后线肺癌，方穹招募.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "9 items, types={'LabReport': 4, 'OutpatientRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 3}", "name": "06-临沂人民-LSPI，后线肺癌，方穹招募.pdf", "embedding_token_consumption": 6620}
2026-08-10 17:28:13,622 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 17:28:13,899 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 17:28:13,899 INFO     29 [Trace] task=15f63a1a | doc=06-临沂人民-LSPI，后线肺癌，方穹招募.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"partial\",\"synced_chunks\":8,\"skipped_hallucinated\":0,\"failed\":[{\"chunk_id\":\"0baa46e84ad6396d\",\"error\":\"(sqlalchemy.dialects.postgresql.asyncpg.Error) <class 'asyncpg.exceptions.StringDataRig...(2294 chars)"}
2026-08-10 17:28:13,903 INFO     29 [DIAG-EXECUTOR] row_position_int len=18 row[0]=(12, 372, 440, 326, 335) row[-1]=(12, 218, 234, 612, 620)
2026-08-10 17:28:13,903 INFO     29 [DIAG-EXECUTOR] row_position_int len=23 row[0]=(13, 161, 232, 186, 197) row[-1]=(13, 183, 201, 421, 431)
2026-08-10 17:28:13,903 INFO     29 [DIAG-EXECUTOR] row_position_int len=25 row[0]=(14, 147, 236, 132, 142) row[-1]=(14, 147, 184, 410, 420)
2026-08-10 17:28:13,904 INFO     29 [DIAG-EXECUTOR] row_position_int len=24 row[0]=(15, 155, 192, 171, 181) row[-1]=(15, 155, 201, 434, 443)
2026-08-10 17:28:13,904 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:28:13,904 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:28:13,904 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:28:13,904 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:28:13,904 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:28:13,910 INFO     29 set_progress(15f63a1a94e011f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 17:28:13 [DOC Engine]:
Start to index...
2026-08-10 17:28:13,931 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.016s]
2026-08-10 17:28:13,935 INFO     29 set_progress(15f63a1a94e011f1bd9827cf206dfa2d), progress: 0.8111111111111111, progress_msg: 
2026-08-10 17:28:13,956 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.014s]
2026-08-10 17:28:13,968 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.006s]
2026-08-10 17:28:13,977 INFO     29 set_progress(15f63a1a94e011f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 17:28:13 Indexing done (0.07s). Task done (313.73s)
2026-08-10 17:28:13,983 INFO     29 [Done], chunks(9), token(6620), elapsed:313.73
2026-08-10 17:28:14,155 INFO     29 handle_task done for task {"id": "15f63a1a94e011f1bd9827cf206dfa2d", "doc_id": "15bf5b9494e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-LSPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df.pdf", "size": 6574298, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786382558729, "task_type": "dataflow", "root_trace_id": "e45d0687fc994f25a61430b755af4825", "root_traceparent": "00-e45d0687fc994f25a61430b755af4825-4f140d87c9e2cd09-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
