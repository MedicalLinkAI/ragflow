# 基准结果：07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf

## 基本信息

- 文件：`07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf`
- 大小：16316.6 KB
- PDF 总页数：12
- doc_id：`8f6c718294e711f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-11T02:16:07  完成时间：2026-08-11T02:24:47  耗时：520.3s
- progress_msg：`18:24:43 Indexing done (0.06s). Task done (479.59s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | ed425497 | 8 | 1-8 | 性别：男 婚姻：已婚 年龄：69岁 入院日期：2026-03-11 08:04  |
| 2 | d0b1f1e6 | 1 | 10-10 | 报告时间: 2026-03-12 【检查日期】: 2026/3/11 12:07 |
| 3 | 153e5a60 | 1 | 11-11 | 【检查日期】：2026/1/8 13:58:55 【检查所见】：右侧胸廓塌陷，右 |
| 4 | 8988e338 | 1 | 11-11 | 【检查描述】：心搏次数：97(60~100) bpm，PR间隔：160 ms，Q |
| 5 | 02b96ed6 | 1 | 12-12 | 【手术信息】：胸腔积液 【取材部位】：1:胸膜×1 2:细胞蜡块1×1 【取材描 |
| 6 | 01868afc | 1 | 8-8 | <table><tr><td>红细胞</td><td>None</td><td> |
| 7 | 145a6ac4 | 1 | 9-9 | <table><tr><td>总蛋白</td><td>TP</td><td>70 |
| 8 | 7477c55b | 1 | 10-10 | <table><tr><td>白细胞</td><td>None</td><td> |
| 9 | fe07ec22 | 1 | 10-10 | <table><tr><td>*白细胞</td><td>None</td><td |
| 10 | 9e363ba4 | 1 | 10-10 | <table><tr><td>大便颜色</td><td>None</td><td |

- chunks 总数：10
- 各 chunk 页数合计（含跨页重复）：17
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]`
- 覆盖页数：12 / 12；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 0 | 0 | 0 | encounter_date, chief_complaint, diagnosis | **-** |
| AdmissionRecord | 入院 | 1 | 1 | 1 | encounter_date, dm_admission_time, cc_text, department | **OK** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 4 | 4 | 4 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 5 | 0 | 5 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"AdmissionRecord": 1, "LabReport": 5, "ExaminationReport": 4}`
- ChunkMerger：`{"found": true, "merged": 10, "sources": 9, "stats": {"Extractor:LabExam": 5, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 4, "Extractor:Progress": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 18:24:41,629 INFO     29 [ChunkMerger] Merged 10 chunks from 9 sources: {'Extractor:LabExam': 5, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 18:16:09,385 INFO     29 handle_task begin for task {"id": "8fa8ece894e711f1bd9827cf206dfa2d", "doc_id": "8f6c718294e711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 16708238, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385769380, "task_type": "dataflow", "root_trace_id": "0aa1bc1a4312482d8e4b2a1774c52cc7", "root_traceparent": "00-0aa1bc1a4312482d8e4b2a1774c52cc7-ad93c0febce673ce-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 18:16:09,613 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 18:16:09,721 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 18:16:09,740 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:16:09,740 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 18:16:09,740 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 18:16:09,755 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 18:16:09,755 INFO     29 ============================================================
2026-08-10 18:16:09,755 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 18:16:09,755 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 18:16:09,755 INFO     29 ============================================================
2026-08-10 18:16:09,755 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 18:16:09,755 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 18:16:09,757 INFO     29 No torch found.
2026-08-10 18:16:10,703 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=12
2026-08-10 18:16:10,920 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1572285, prompt_len=764
2026-08-10 18:16:12,395 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 18:16:12,397 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 18:16:12,412 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1572285, prompt_len=401
2026-08-10 18:16:20,739 INFO     29 [qwen-vl-parser] text API response (len=1483):
["性别：男", "婚姻：已婚", "年龄：69岁", "入院日期：2026-03-11 08:04", "民族：汉族", "记录日期：2026-03-11 08:06", "职业：农民", "病史陈述者：患者本人", "主诉：确诊肺腺癌10月余，咯血2天余。", "现病史：患者因“呼吸困难2月余”于2025-04-05第1次入院，入院后完善检验检查：", "CEA(胸水)：癌胚抗原 538ng/ml；于04-07完善胸腔镜检查：镜下诊断：胸腔积液，胸壁结节", "样改变。病理：（胸膜活检）送检增生的纤维组织内见腺癌浸润，请结合临床诊治。免疫组", "化：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（部分+）、P40（点灶+）、CR（灶", "+）、ALK（1A4）（-）、Ki67（+，40%）。完善评估检查：胸部增强(64排-128层)：1.符合", "右侧胸腔引流术后改变，右侧液气胸并右侧颈根部及胸壁积气，肺组织压缩约70%。2.右肺", "下叶占位，考虑肺癌并纵隔及双肺门淋巴结转移可能，右侧胸膜结节状增厚、强化，考虑转", "移，请结合临床。3.左肺小结节，目前考虑良性，建议短期复查。4.双肺慢性炎症/纤维", "灶。5.动脉粥样硬化表现。6.甲状腺改变，请结合超声检查。7.右侧第8肋骨质改变，请结", "合临床。全身骨显像：1.右侧第6-8侧肋异常放射性浓聚，本院CT（2025-04-09）第6、7肋", "骨未见明显骨质异常，第8肋髓腔内见局灶高密度影，建议短期CT复查。2.左侧坐骨轻度放", "射性浓聚灶，本院CT未见明显骨质破坏，建议随诊。04-14复查胸部CT：对比2025-04-09", "CT：1.符合右侧胸腔引流术后改变，右侧液气胸并右侧颈根部及胸壁积气，较前减轻，肺组", "织压缩约30%。2.右肺下叶占位，较前相仿，考虑肺癌；纵隔及双肺门淋巴结同前；右侧胸", "膜结节状增厚，较前局部稍减轻，请结合临床。3.左肺小结节，较前相仿，建议短期复查。", "余所见大致同前。04-16复查胸片：1.右侧胸腔引流术后表现，对比2025-04-11X线：右侧气", "胸较前明显减少；原右侧胸壁及胸壁皮下积气基本消失；右侧胸腔积液较前减少，建议复查", "或结合CT检查。2.右肺下野占位，请结合临床及CT检查。患者完善基因检测未见基因突变，", "于04-17给予第1周期全身化疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2 q21d，同时辅", "以止吐、护胃、保肝、激素减轻化疗不良反应等治疗。于04-19给予信迪利单抗200mg抗肿瘤", "免疫治疗。患者化疗顺利，准予出院。末次出院诊断：1.肺腺癌伴纵隔淋巴结、肺门淋巴", "结、胸膜转移（T2bN3M1 IV期）恶性胸腔积液 2.气胸 3.左侧大隐静脉曲张 4.肝囊肿 5.双", "肾囊肿 6.前列腺稍大伴钙化", "患者因“确诊肺腺癌1月”于2025-05-07第2次入院，入院后完善相关检查：肺肿瘤检", "验：癌胚抗原 62.1ng/ml，神经元特异性烯醇化酶 19.8ng/ml，细胞角蛋白19片段", "6.21ng/ml；大便常规：未见异常；髂静脉及下肢深静脉、下肢浅静脉：左侧大隐静脉曲张，", "左侧隐股静脉瓣功能不全；胸部平扫(64排-128层)：对比2025-04-14CT：1.符合右侧胸腔引", "流术后改变，右侧液气胸，积液较前增多，积气较前减少；原右侧颈根部及胸壁少量积气本", "第1页"]
2026-08-10 18:16:20,740 INFO     29 [qwen-vl-parser] page=1 text: 38 lines (bbox 0-37)
2026-08-10 18:16:20,740 INFO     29 [qwen-vl-parser] page=1 text: 38 sections
2026-08-10 18:16:20,990 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1826152, prompt_len=764
2026-08-10 18:16:22,328 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 18:16:22,329 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 18:16:22,344 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1826152, prompt_len=401
2026-08-10 18:16:32,058 INFO     29 [qwen-vl-parser] text API response (len=1667):
["次吸收。2.右肺下叶占位，较前略缩小，考虑肺癌；纵隔及双肺门淋巴结部分较前略增大；", "右侧胸膜结节状增厚，较前局部稍减轻，请结合临床。3.左肺小结节，较前相仿，建议短期", "复查。余所见大致同前。入院后于05-09拔除胸腔引流管。排除禁忌于05-09行第2周期全身", "化疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2 q21d，并辅以激素、止吐、护胃、保肝", "等治疗，05-10给予信迪利单抗200mg肿瘤免疫治疗。患者治疗结束，于2025-05-11出院。", "患者因“确诊肺腺癌1月余，发热5天”于2025-05-19第3次入院，入院后完善检验检", "查：大便菌群分析:细菌总数600 个/油镜视野（参考值500～5000个），革兰阳性球菌少量，", "革兰阴性杆菌少量，酵母样真菌孢子+，酵母样真菌菌丝+；艰难梭菌毒素A/B检测:艰难梭", "菌毒素A/B检测 0.02；大便细菌培养+药敏:经两天普通培养，鉴定生长热带念珠菌+++，无", "肠球菌生长，无肠杆菌生长，无沙门氏菌、志贺氏菌生长。痰细菌学检查:经2天普通培养，", "经鉴定为正常菌群生长，无流感嗜血杆菌生长。胸部平扫(64排-128层)：对比", "2025-04-14CT：1.符合右侧胸腔引流术后改变，右侧液气胸，积液较前增多，积气较前减", "少；原右侧颈根部及胸壁少量积气本次吸收。2.右肺下叶占位，较前略缩小，考虑肺癌；纵", "隔及双肺门淋巴结部分较前略增大；右侧胸膜结节状增厚，较前局部稍减轻，请结合临床。", "3.左肺小结节，较前相仿，建议短期复查。余所见大致同前。腹部（包括盆腔）平扫(64", "排)：1.考虑肝多发囊肿、右肾囊肿，必要时增强扫描。2.双肾周桥隔略增厚。3.动脉粥样", "硬化。4.前列腺增大伴钙化。5.L5椎体前滑脱（I°），双侧椎弓峡部裂。胸部平扫(64排", "-128层)：对比2025-05-08CT：1.右侧液气胸，积液较前增多，积气较前减少。2.右肺下叶", "占位，较前缩小，考虑肺癌；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜结节状增", "厚，较前变化不著，请结合临床。3.左肺小结节，较前相仿，建议短期复查。余所见大致同", "前。入院后给予哌拉西林他唑巴坦抗感染，蒙脱石散止泻，枯草杆菌二联活菌胶囊调整消化", "道菌群，利伐沙班抗凝，制霉素片口服治疗，现患者病情稳定，于2025-05-29出院。", "患者因“确诊肺腺癌2月余。”第4次入院，入院后完善辅助检查，入院后排除禁忌，", "06-06行第3周期治疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2，联合信迪利单抗200mg", "抗肿瘤免疫治疗，并辅以激素、止吐、护胃、保肝等治疗，治疗结束后复查血常规未见明显", "骨髓抑制，于2025-06-08出院。末次出院诊断：1.恶性肿瘤维持性化学治疗 2.恶性肿瘤免", "疫治疗 3.肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转移 肺门淋巴结转移 胸膜转移 恶性胸腔", "积液 4.大隐静脉曲张 5.肾囊肿 6.单纯性肝囊肿。", "患者因“确诊肺腺癌2月余，为继续治疗”于2025-06-26第5次入院，入院后完善相关检", "查，排除禁忌，06-27行第4周期治疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2，联合", "信迪利单抗200mg抗肿瘤免疫治疗，并辅以激素、止吐、护胃、保肝等治疗，治疗结束后复", "查血常规未见明显骨髓抑制，于2025-06-29出院。末次出院诊断：1.恶性肿瘤维持性化学治", "疗 2.恶性肿瘤免疫治疗 3.肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转移 肺门淋巴结转移 胸", "膜转移 4.恶性胸腔积液 5.大隐静脉曲张 6.肾囊肿 7.单纯性肝囊肿.", "患者因“确诊肺腺癌3月余，为继续治疗”2025-07-17入院，入院后完善相关必要辅助", "第2页"]
2026-08-10 18:16:32,060 INFO     29 [qwen-vl-parser] page=2 text: 36 lines (bbox 38-73)
2026-08-10 18:16:32,061 INFO     29 [qwen-vl-parser] page=2 text: 36 sections
2026-08-10 18:16:32,318 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1837009, prompt_len=764
2026-08-10 18:16:35,924 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 18:16:35,925 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 18:16:35,942 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1837009, prompt_len=401
2026-08-10 18:16:39,077 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:16:39.075+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 86, "failed": 0, "current": {"8fa8ece894e711f1bd9827cf206dfa2d": {"id": "8fa8ece894e711f1bd9827cf206dfa2d", "doc_id": "8f6c718294e711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 16708238, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385769380, "task_type": "dataflow", "root_trace_id": "0aa1bc1a4312482d8e4b2a1774c52cc7", "root_traceparent": "00-0aa1bc1a4312482d8e4b2a1774c52cc7-ad93c0febce673ce-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:16:46,291 INFO     29 [qwen-vl-parser] text API response (len=1800):
["检查：电解质+血气分析:酸碱度7.476，二氧化碳分压36.4mmHg，氧分压114.0mmHg；急", "查血常规+CRP:红细胞3.61x10^12/L，血红蛋白110g/L，血小板总数222×10^9/L，白细", "胞4.90×10^9/L，中性粒细胞绝对值3.59×10^9/L，淋巴细胞绝对值0.77×10^9/L，超", "敏C-反应蛋白17.92mg/L；肺肿瘤检验：癌胚抗原54.9ng/ml，细胞角蛋白19片段", "5.54ng/ml，胃泌素释放肽前体80.2pg/ml；生化系列36项:白蛋白(溴甲酚绿法)", "31.59g/L，镁0.72mmol/L，肌酐(酶法)55μmol/L，肌酸激酶31U/L；DIC系列-5项:纤维", "蛋白原5.47g/L，D-二聚体3.53mg/L；急查降钙素原、急查心梗三项、皮质醇(7:00-10:", "00am)、促肾上腺皮质激素(8时)、甲状腺功能3项、急查NT-proBNP、大便常规(粪沉渣)+", "潜血、尿液分析+尿沉渣未见明显异常。常规心电图检查(自动分析)：窦性心动过速；心", "脏超声检查(含左心功能测定)：主动脉瓣轻度反流，三尖瓣轻度反流；颅脑平扫+DWI+增", "强(3T)：1.双侧额顶叶及侧脑室旁白质内脱髓鞘改变。2.老年脑改变。3.部分副鼻窦炎；", "右侧乳突炎。4.鼻中隔偏曲，双下鼻甲肥大。颈部：左侧颈部淋巴结稍大，右侧颈部淋巴结", "可见；髂静脉及下肢深静脉、下肢浅静脉：左侧大隐静脉曲张，左侧隐股静脉瓣功能不全；", "腹部(包括盆腔)平扫(64排)：1.考虑肝多发囊肿、右肾囊肿，必要时增强扫描。2.双肾周", "桥隔略增厚。3.动脉粥样硬化。4.前列腺增大伴钙化。5.L5椎体前滑脱(I°)，双侧椎弓", "峡部裂。以上所见较2025-05-26CT变化不著。胸部平扫(64排-128层)：对比2025-05-26CT:", "1.右肺下叶肺癌，较前略缩小、其内新见空洞影；右肺小叶间隔增厚，考虑癌性淋巴管炎可", "能；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜结节状增厚，较前变化不著；请结合", "临床。2.右侧液气胸，积液较前略增多，积气较前明显减少。3.左肺小结节，较前相仿，建", "议短期复查。4.右侧第7-9、12肋骨高密度影，较前密度增高，转移?建议ECT进一步检查。", "余所见大致同前。肋骨平扫+DWI+增强(3T)：1.右侧第7-9、12肋改变，成骨性转移?请结", "合其它影像学检查。2.右侧胸腔积液。3.肝内多发囊肿。排除禁忌，07-18行第5周期治疗：", "培美曲塞0.8gd1+顺铂注射液65mgd1、d2，联合信迪利单抗200mg抗肿瘤免疫治疗，并辅", "以激素、止吐、护胃、保肝等治疗，治疗结束后复查血常规未见明显骨髓抑制，针对肋骨异", "常请放疗科会诊后建议可考虑放疗，07-21出院。", "患者因“确诊肺腺癌4月，为继续治疗”2025-08-07第7次入院，入院后完善相关检查，", "急查血常规+CRP:血红蛋白109g/L，血小板总数205×10^9/L，白细胞4.58×10^9/L，中", "性粒细胞百分率70.9%，超敏C-反应蛋白17.43mg/L；超敏肌钙蛋白T14.80pg/ml；DIC系", "列-5项:纤维蛋白原5.27g/L，D-二聚体4.37mg/L；N端-B型钠尿肽前体71.5pg/ml；促肾", "上腺皮质激素(8时)：促肾上腺皮质激素(8时)31.7pg/ml；生化系列36项:白蛋白(溴甲酚绿", "法)33.34g/L，钾3.93mmol/L，钠140.1mmol/L，氯104.8mmol/L，尿素5.04mmol/L，肌", "酐(酶法)65μmol/L；皮质醇(7:00-10:00am)：皮质醇(7:00-10:00am)295nmol/L；甲状腺", "功能3项：促甲状腺素3.17mIU/L，游离甲状腺素13.6pmol/L，游离三碘甲状腺原氨酸", "4.46pmol/L；肺肿瘤检验：癌胚抗原52.6ng/ml，神经元特异性烯醇化酶20.4ng/ml，", "细胞角蛋白19片段4.81ng/ml，胃泌素释放肽前体92.9pg/ml。常规心电图检查(自动分", "第3页"]
2026-08-10 18:16:46,291 INFO     29 [qwen-vl-parser] page=3 text: 36 lines (bbox 74-109)
2026-08-10 18:16:46,291 INFO     29 [qwen-vl-parser] page=3 text: 36 sections
2026-08-10 18:16:46,535 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1766588, prompt_len=764
2026-08-10 18:16:47,896 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 18:16:47,896 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 18:16:47,912 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1766588, prompt_len=401
2026-08-10 18:16:58,067 INFO     29 [qwen-vl-parser] text API response (len=1757):
["析）：窦性心律，大致正常心电图。排除禁忌，于08-08给予第6周期化疗，方案为培美曲塞", "0.8g+顺铂注射液 65mg d1、d2，联合信迪利单抗200mg 免疫治疗，过程顺利，08-10行地", "舒单抗120mg抗骨转移治疗；复查血常规未见明显骨髓抑制，08-10出院。", "患者因“确诊肺腺癌4月，为继续治疗”于2025-08-28第8次入院，入院后完善辅助检", "查：胸部平扫：对比2025-07-18CT：1.右肺下叶肺癌，较前变化不著；右肺小叶间隔增厚，", "较前变化不著，考虑癌性淋巴管炎可能；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜", "结节状增厚，较前变化不著；请结合临床。2.右侧液气胸，积液较前变化不著，积气较前增", "多。3.左肺小结节，较前相仿，建议短期复查。4.右侧第7-9、12肋骨高密度影，较前变化", "不著，转移？建议ECT进一步检查。余所见大致同前。下腹部平扫：1.考虑右肾囊肿，较", "2025-07-18变化不著，必要时增强扫描。2.双肾周桥隔略增厚。3.动脉粥样硬化。上腹部平", "扫：考虑肝多发囊肿，较2025-07-18变化不明显，建议结合增强检查明确。盆腔平扫：1.前", "列腺增大伴钙化。2.L5椎体前滑脱（I°），双侧椎弓峡部裂。以上所见较2025-07-18变化", "不著。排除禁忌，给予培美曲塞 0.8g 联合信迪利单抗 200mg免疫治疗，并辅以激素、止", "吐、护胃、保肝等治疗，治疗过程顺利，患者病情稳定，2025-08-30出院。出院诊断：1.恶", "性肿瘤维持性化学治疗 2.恶性肿瘤免疫治疗 3.右肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转", "移 肺门淋巴结转移 胸膜转移 骨转移 4.恶性胸腔积液 5.大隐静脉曲张 6.肾囊肿 7.单纯", "性肝囊肿。", "患者因“确诊肺腺癌5月余，为继续治疗”于2025-10-06第9次入院，入院后完善辅助检", "查：急查血常规+CRP:血红蛋白 114g/L，血小板总数 212×10^9/L，白细胞", "7.30×10^9/L，中性粒细胞百分率 80.0%，超敏C-反应蛋白 16.04mg/L；皮质醇(7:00-10:", "00am):皮质醇(7:00-10:00am) 442nmol/L；促肾上腺皮质激素(8时):促肾上腺皮质激素(8", "时) 29.3pg/ml；甲状腺功能3项:促甲状腺素 4.94mIU/L，游离甲状腺素 14.4pmol/L，游离", "三碘甲状腺原氨酸 3.85pmol/L；生化系列36项:白蛋白(溴甲酚绿法) 36.10g/L，白蛋白:球", "蛋白 0.96，天门冬氨酸氨基转移酶 18U/L，丙氨酸氨基转移酶 8U/L，尿素 5.84mmol/L，", "肌酐(酶法) 78μmol/L；肺肿瘤检验-莱山:癌胚抗原 68.6ng/ml，细胞角蛋白19片段", "9.45ng/ml，胃泌素释放肽前体 96.7pg/ml；DIC系列-5项:纤维蛋白原 5.04g/L，D-二聚体", "3.28mg/L；急查NT-proBNP:N端-B型钠尿肽前体 50.1pg/ml；急查心梗三项:超敏肌钙蛋白T", "14.00pg/ml，肌酸激酶-MB同工酶质量测定 0.54ng/ml，肌红蛋白 43.2ng/ml。排除禁忌，", "于2025-10-06给予本周期治疗，方案为培美曲塞 0.8g联合信迪利单抗200mg，并给予地舒单", "抗120mg治疗骨转移，2025-10-07办理出院。出院诊断：1.右肺腺癌（T2bN3M1 IV期） 纵隔", "淋巴结转移 肺门淋巴结转移 胸膜转移 骨转移 2.恶性胸腔积液 3.大隐静脉曲张 4.肾囊肿", "5.单纯性肝囊肿。", "患者因“确诊肺腺癌7月余，为继续治疗”于2025-11-07第10次入院，入院后完善相关", "检查：急查血常规+CRP:血红蛋白 115g/L，血小板总数 214×10^9/L，白细胞", "7.21×10^9/L，中性粒细胞百分率 82.3%，超敏C-反应蛋白 20.50mg/L；DIC系列-5项:纤维", "第 4 页"]
2026-08-10 18:16:58,067 INFO     29 [qwen-vl-parser] page=4 text: 36 lines (bbox 110-145)
2026-08-10 18:16:58,067 INFO     29 [qwen-vl-parser] page=4 text: 36 sections
2026-08-10 18:16:58,323 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1895440, prompt_len=764
2026-08-10 18:16:59,718 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:16:59,719 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 18:16:59,730 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1895440, prompt_len=401
2026-08-10 18:17:11,254 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:17:11.251+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 86, "failed": 0, "current": {"8fa8ece894e711f1bd9827cf206dfa2d": {"id": "8fa8ece894e711f1bd9827cf206dfa2d", "doc_id": "8f6c718294e711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 16708238, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385769380, "task_type": "dataflow", "root_trace_id": "0aa1bc1a4312482d8e4b2a1774c52cc7", "root_traceparent": "00-0aa1bc1a4312482d8e4b2a1774c52cc7-ad93c0febce673ce-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:17:12,205 INFO     29 [qwen-vl-parser] text API response (len=1808):
["蛋白原 5.04g/L，D-二聚体 2.19mg/L；皮质醇(7:00-10:00am):皮质醇(7:00-10:00am)", "286nmol/L；促肾上腺皮质激素(8时):促肾上腺皮质激素(8时)23.3pg/ml；急查心梗三项:", "超敏肌钙蛋白T 17.70pg/ml；肺肿瘤检验-莱山:癌胚抗原 75.8ng/ml，细胞角蛋白19片段", "12.4ng/ml，胃泌素释放肽前体 90.5pg/ml；生化系列36项:白蛋白(溴甲酚绿法)", "32.49g/L，脂蛋白(a)343mg/L，唾液酸 769mg/L；N端-B型钠尿肽前体、甲状腺功能3项未", "见异常。常规心电图检查：窦性心动过速。全身骨显像：与本院2025-04-10骨显像比较：1.", "右侧多根肋骨多发异常放射性浓聚灶，病灶数目较前增多，浓聚程度增高，提示骨转移瘤可", "能大，请结合其他检查综合考虑；2.前次检查所示左侧坐骨轻度放射性浓聚灶，本次检查未", "见显示；3.双肩关节及双膝关节区异常放射性浓聚，考虑炎性病变，请结合临床。颅脑平扫", "+DWI+增强+薄层：1.双侧额顶叶及侧脑室旁白质内脱髓鞘改变；2.老年脑改变，双侧额颞部", "少量硬膜下积液；3.部分副鼻窦炎；右侧乳突炎；4.鼻中隔偏曲，双下鼻甲肥大。心脏超声", "检查（含左心功能测定）：静息状态下：心内结构及血流未见明显异常髂静脉及下肢深静脉", "(双侧)：双侧髂静脉及下肢深静脉血流通畅颈部：双侧颈部未见明显增大淋巴结胸部平扫", "+增强：对比2025-08-28CT：1.右肺下叶肺癌，较前增大；右肺小叶间隔增厚，较前略进", "展，考虑癌性淋巴管炎可能；纵隔及双肺门淋巴结，部分较前略增大；考虑右侧胸膜转移，", "较前明显进展，累及邻近右前胸壁及右侧膈肌可能；请结合临床并复查；2.右侧胸腔积液，", "较前变化不著，原右侧胸腔积气吸收；3.左肺小结节，部分较前略增大（如下叶薄层", "img231、243），部分结节较前相仿，建议短期复查；4.右侧第7-9、12肋骨高密度影，较前", "变化不著，转移？建议ECT进一步检查；余所见大致同前。上腹部平扫+增强：考虑肝多发囊", "肿，较2025-08-28变化不明显。下腹部平扫+增强：1.考虑右肾囊肿，较2025-08-28变化不", "著；2.双肾周桥隔略增厚；3.动脉粥样硬化。排除禁忌给予本周期治疗，方案为培美曲塞", "0.8g、信迪利单抗200mg联合恩度 210mg q21d治疗。治疗结束，患者病情稳定，2025-11-14", "办理出院。出院诊断：1.右肺腺癌(T2bN3M1 IV期) 纵隔淋巴结转移 肺门淋巴结转移 胸", "膜转移 骨转移 2.恶性胸腔积液 3.大隐静脉曲张 4.肾囊肿 5.肝囊肿", "患者因“确诊肺腺癌8月余，为继续治疗”于2026-01-08再入院，入院后完善相关辅助", "检查：01-08：急查NT-proBNP、促肾上腺皮质激素(8时)、皮质醇(7:00-10:00am)等未见明", "显异常。急查血常规+CRP+SAA:红细胞 3.93x10^12/L，血红蛋白 118g/L，红细胞压积", "35.8%，红细胞分布宽度SD 47.4fl，中性粒细胞百分率 77.9%，淋巴细胞百分率 9.4%，单", "核细胞百分率 10.2%，淋巴细胞绝对值 0.67×10^9/L，单核细胞绝对值 0.73×10^9/L，超", "敏C-反应蛋白 30.56mg/L，血清淀粉样蛋白A 26.98mg/L；急查心梗三项:超敏肌钙蛋白T", "15.10pg/ml；DIC系列-5项:纤维蛋白原 6.22g/L，D-二聚体 1.66mg/L；急查降钙素原：", "0.0969ng/ml；生化系列36项:白蛋白(溴甲酚绿法) 31.69g/L，白蛋白:球蛋白 0.87，肾小", "球滤过率 89.97ml/(min·1.73m²)，肌酸激酶 38U/L，脂蛋白(a) 452mg/L，唾液酸", "765mg/L；甲状腺功能6项:促甲状腺素 4.69mIU/L；肺肿瘤检验", "癌胚抗原", "73.4ng/ml，神经元特异性烯醇化酶 18.4ng/ml，细胞角蛋白19片段 19.1ng/ml，胃泌素释", "第5页"]
2026-08-10 18:17:12,207 INFO     29 [qwen-vl-parser] page=5 text: 37 lines (bbox 146-182)
2026-08-10 18:17:12,207 INFO     29 [qwen-vl-parser] page=5 text: 37 sections
2026-08-10 18:17:12,456 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1735998, prompt_len=764
2026-08-10 18:17:13,900 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 18:17:13,900 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-10 18:17:13,913 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1735998, prompt_len=401
2026-08-10 18:17:23,112 INFO     29 [qwen-vl-parser] text API response (len=1653):
["放肽前体81.4pg/ml；常规心电图检查（自动分析）：窦性心动过速。下腹部平扫+增强：", "1.考虑右肾囊肿，较2025-11-08变化不著。2.双肾周桥隔略增厚。3.动脉粥样硬化。上腹部", "平扫+增强：考虑肝多发囊肿，较2025-11-08变化不明显。胸部平扫+增强：对比", "2025-11-08CT：1.右肺下叶肺癌，范围整体较前增大；右肺小叶间隔增厚，较前进展，考虑", "癌性淋巴管炎可能；纵隔及双肺门淋巴结大致同前；考虑右侧胸膜转移，较前进展，累及邻", "近右前胸壁及右侧膈肌可能；请结合临床并复查。2.右侧胸腔积液，较前变化不著。3.左肺", "小结节，较前相仿，建议短期复查。4.右侧第7-9、12肋骨高密度影，局部略进展，转移可", "能，建议ECT进一步检查。余所见大致同前。01-09：髂静脉及下肢深静脉、下肢浅静脉：左", "侧大隐静脉曲张左侧隐股静脉瓣功能不全。01-10：心脏超声检查（含左心功能测定）：静", "息状态下：心内结构及血流未见明显异常。考虑患者肿瘤较前进展，请肿瘤科及放疗科会", "诊，给予更换二线化疗方案，排除禁忌，1-09行开始给予恩度抗血管生成，01-12给予二线", "第1周期全身化疗：白蛋白紫杉醇300mg d1、信迪利单抗200mg，01-13给予地舒单抗120mg抗", "骨转移。期间联合护肝、护胃、止吐、激素等治疗，现病情平稳，准予出院。末次出院诊", "断：1.右肺腺癌（T2bN3M1 IV期）纵隔淋巴结转移肺门淋巴结转移胸膜转移骨转移2.", "恶性胸腔积液3.大隐静脉曲张4.肾囊肿5.肝囊肿6.贫血7.低蛋白血症", "患者出院后规律服药、门诊复诊，偶有咳嗽，咳白薄痰，腰肋部水肿，于2026-2-10再", "入院，", "入院后完善辅助检查：NT-proBNP未见明显异常；血常规+CRP+SAA：红细胞", "4.25x10^12/L，血红蛋白125g/L，红细胞压积38.4%，红细胞分布宽度SD47.8fl，中性粒", "细胞百分率83.4%，淋巴细胞百分率8.0%，中性粒细胞绝对值7.35×10^9/L，淋巴细胞绝", "对值0.70×10^9/L，单核细胞绝对值0.62×10^9/L，超敏C-反应蛋白24.16mg/L，血清淀", "粉样蛋白A13.13mg/L；心梗三项：超敏肌钙蛋白T14.10pg/ml；降钙素原：0.0528ng/ml；生", "化系列36项：白蛋白（溴甲酚绿法）34.82g/L，白蛋白：球蛋白1.02，肾小球滤过率", "89.97ml/(min•1.73m²)，肌酸激酶33U/L，脂蛋白(a)510mg/L，唾液酸792mg/L；肺肿瘤", "检验：癌胚抗原100ng/ml，神经元特异性烯醇化酶31.1ng/ml，细胞角蛋白19片段", "28.8ng/ml，胃泌素释放肽前体87.7pg/ml；DIC系列-5项：纤维蛋白原6.71g/L，D-二聚体", "1.42mg/L；心电图：窦性心律大致正常心电图。尿液分析、大便常规及潜血、促肾上腺皮", "质激素(8时)、皮质醇(7:00-10:00am)、甲状腺功能6项等未见明显异常。排除禁忌，02-10", "开始给予恩度抗血管生成，02-11给予二线第2周期全身化疗：白蛋白紫杉醇300mg d1，同时", "辅以激素、止吐、护胃、保肝治疗，同时给予信迪利单抗200mg抗肿瘤免疫治疗，02-12给予", "地舒单抗120mg抗骨转移治疗。于2026-02-13出院。末次出院诊断：1.恶性肿瘤维持性化学", "治疗2.恶性肿瘤免疫治疗3.恶性肿瘤靶向治疗4.右肺腺癌（T2bN3M1 IV期）纵隔淋巴结", "转移肺门淋巴结转移胸膜转移骨转移5.恶性胸腔积液6.大隐静脉曲张7.肾囊肿8.肝", "囊肿。", "患者出院后规律门诊复诊，偶有咳嗽、咳痰，2天前无明显诱因出现咯血，感痰较前增", "第6页"]
2026-08-10 18:17:23,113 INFO     29 [qwen-vl-parser] page=6 text: 36 lines (bbox 183-218)
2026-08-10 18:17:23,113 INFO     29 [qwen-vl-parser] page=6 text: 36 sections
2026-08-10 18:17:23,341 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1498925, prompt_len=764
2026-08-10 18:17:24,650 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:17:24,651 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-10 18:17:24,667 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1498925, prompt_len=401
2026-08-10 18:17:30,882 INFO     29 [qwen-vl-parser] text API response (len=1037):
["多，每天数十口，色鲜红，今为进一步治疗入院。患者病后神志清，精神状态一般，食欲一", "般，睡眠良好，大便正常，小便正常，体力情况一般，体重无明显变化。", "既往史：否认食物、药物过敏史，参阅既往入院记录。", "个人史：参阅既往入院记录。", "家族史：参阅既往入院记录。", "体 格 检 查", "T 36.3℃ P 107次/分 R 21次/分 Bp 144/99mmHg", "发育正常，营养良好，正常面容，表情自如，自主体位，神志清楚，查体合作。全身皮", "肤粘膜无黄染，无皮疹，无皮下出血，无皮下结节，皮下无水肿，无肝掌、蜘蛛痣，毛发分", "布均匀。全身浅表淋巴结无肿大。眼睑无水肿，结膜无苍白，眼球无突出，无震颤，巩膜无", "黄染，瞳孔等大等圆，对光反射灵敏，耳廓对称，无畸形，牵拉无疼痛，外耳道无异常分泌", "物，乳突无压痛，无听力粗试障碍。鼻无畸形。口唇无发绀，口腔粘膜无充血、糜烂。舌苔", "薄白，伸舌无偏斜、震颤，牙龈无红肿，咽部粘膜无充血，扁桃体无肿大。颈软无抵抗，颈", "动脉无异常搏动，半坐位颈静脉未见充盈，颈部大血管区未闻及血管杂音。气管居中，肝颈", "静脉回流征阴性，甲状腺无肿大，无压痛、震颤、血管杂音。胸廓无畸形，呼吸运动两侧对", "称，肋间隙无狭窄或饱满，胸壁无压痛，语颤无增强、减弱，胸骨无压痛。双肺叩诊清音，", "呼吸规整，双肺呼吸音低，未闻及干湿性啰音，无胸膜摩擦音。心前区无异常隆起、异常搏", "动、震颤，心浊音界不大，心率107次/分，律齐，心音有力，各瓣膜听诊区未闻及杂音，无", "心包摩擦音。腹平坦，软，无压痛、反跳痛，腹部无包块。肝脏未触及，脾脏未触及，", "Murphy氏征阴性，肾区无叩击痛，无移动性浊音。肠鸣音正常，4次/分。肛门及外生殖器未", "查。脊柱正常生理弯曲，四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾），关节无肿", "胀、压痛，下肢无浮肿。", "肌肉无压痛，四肢肌力、肌张力未见异常，双侧肱", "二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性。", "专科检查： 胸廓无畸形，呼吸运动两侧对称，肋间隙无狭窄或饱满，胸壁无压痛，语", "颤无增强、减弱，胸骨无压痛。双肺叩诊清音，呼吸规整，双肺呼吸音低，未闻及干湿性啰", "音，无胸膜摩擦音。", "辅 助 检 查", "检查日期 项目 结果 检查单位 检查编号", "第 7 页"]
2026-08-10 18:17:30,882 INFO     29 [qwen-vl-parser] page=7 text: 30 lines (bbox 219-248)
2026-08-10 18:17:30,882 INFO     29 [qwen-vl-parser] page=7 text: 30 sections
2026-08-10 18:17:31,104 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1250766, prompt_len=764
2026-08-10 18:17:32,543 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 18:17:32,544 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-10 18:17:32,558 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1250766, prompt_len=401
2026-08-10 18:17:42,824 INFO     29 [qwen-vl-parser] text API response (len=1587):
["2025-04-09", "病理", "(胸膜活检)送检增生的纤维组", "织内见腺癌浸润，请结合临床诊", "治。免疫组化：TTF-1（-）、", "NapsinA（-）、CK7（+）、CK5/6", "（部分+）、P40（点灶+）、CR（", "灶+）、ALK（1A4）（-）、Ki67", "(+,40%）。C-MET免疫组化检测", "报告检测平台：Roche Ventana", "Benchmark Ultra；抗体克隆号：", "SP44,Roche；表达部位：细胞膜和", "细胞浆；阳性强度及百分比：++(", "40%),+(60%)阳性等级：1+", "细胞数量：≥100。", "初步诊断：", "1.咯血", "2.右肺腺癌（T2bN3M1 IV期）", "纵隔淋巴结转移", "肺门淋巴结转移", "胸膜转移", "骨转移", "3.恶性胸腔积液", "4.大隐静脉曲张", "5.肾囊肿", "6.肝囊肿", "项目名称", "结果", "单位", "参考范围", "项目名称", "结果", "单位", "参考区间", "*★红细胞", "4.47", "x10^12/L", "4.30-5.80", "*★白细胞", "10.11", "×10^9/L", "3.50-9.50", "*★血红蛋白", "131", "g/L", "130-175", "中性粒细胞百分率", "79.3", "%", "40.0-75.0", "*★红细胞压积", "40.0", "%", "40.0-50.0", "淋巴细胞百分率", "12.1", "%", "20.0-50.0", "*平均红细胞体积", "89.4", "fL", "82.0-100.0", "单核细胞百分率", "7.0", "%", "3.0-10.0", "*平均血红蛋白量", "29.4", "pg", "27.0-34.0", "嗜酸细胞百分率", "1.1", "%", "0.4-8.0", "*平均血红蛋白浓度", "328", "g/L", "316-354", "嗜碱细胞百分率", "0.5", "%", "0.0-1.0", "红细胞分布宽度SD", "48.4", "f1", "39.0-46.0", "↑", "中性粒细胞绝对值", "8.02", "×10^9/L", "1.80-6.30", "红细胞分布宽度CV", "14.8", "%", "10.9-14.5", "↑", "淋巴细胞绝对值", "1.22", "×10^9/L", "1.10-3.20", "*★血小板总数", "256", "×10^9/L", "125-350", "单核细胞绝对值", "0.71", "×10^9/L", "0.10-0.60", "血小板平均容积", "8.5", "fL", "7.6-13.2", "嗜酸细胞绝对值", "0.11", "×10^9/L", "0.02-0.52", "血小板分布宽度", "16.2", "f1", "9.0-17.0", "嗜碱细胞绝对值", "0.05", "×10^9/L", "0.00-0.06", "血小板比积", "0.217", "%", "0.11-0.28", "超敏C-反应蛋白", "28.26", "mg/L", "0.00-6.00", "大血小板比例", "17.5", "%", "13.0-43.0", "血清淀粉样蛋白A", "16.24", "mg/L", "0.00-10.00", "备注评价：", "采集时间：2026-03-11 09:24", "接收时间：2026-03-11 09:57", "报告时间：2026-03-11 10:09"]
2026-08-10 18:17:42,825 INFO     29 [qwen-vl-parser] page=8 text: 144 lines (bbox 249-392)
2026-08-10 18:17:42,825 INFO     29 [qwen-vl-parser] page=8 text: 144 sections
2026-08-10 18:17:43,111 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1529121, prompt_len=764
2026-08-10 18:17:43,386 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:17:43.384+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 86, "failed": 0, "current": {"8fa8ece894e711f1bd9827cf206dfa2d": {"id": "8fa8ece894e711f1bd9827cf206dfa2d", "doc_id": "8f6c718294e711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 16708238, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385769380, "task_type": "dataflow", "root_trace_id": "0aa1bc1a4312482d8e4b2a1774c52cc7", "root_traceparent": "00-0aa1bc1a4312482d8e4b2a1774c52cc7-ad93c0febce673ce-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:17:44,620 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-11"
}
```
2026-08-10 18:17:44,621 INFO     29 [qwen-vl-parser] page=9 classify=table report_date=2026-03-11
2026-08-10 18:17:44,651 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1529121, prompt_len=756
2026-08-10 18:17:54,679 INFO     29 [qwen-vl-parser] table API response (len=2247):
\begin{tabular}{ccccccc}
\hline
序号 & 项目名称 & 项目代码 & 结果 & 单位 & 参考区间 & 提示 \\
\hline
1 & **总蛋白 & TP & 70.10 & g/L & 65.00-85.00 & \\
2 & **白蛋白(溴甲酚绿法) & ALB & 37.19 & g/L & 40.00-55.00 & $\downarrow$ \\
3 & 球蛋白 & GLO & 32.91 & g/L & 20.00-40.00 & \\
4 & 白蛋白:球蛋白 & A:G & 1.13 & & 1.20-2.40 & $\downarrow$ \\
5 & *总胆红素 & TBIL & 12.6 & $\mu$mol/L & $\le$26.0 & \\
6 & *直接胆红素 & DBIL & 2.2 & $\mu$mol/L & 0.0-6.8 & \\
7 & 间接胆红素 & IBIL & 10.4 & $\mu$mol/L & 3.0-19.0 & \\
8 & **$\gamma$-谷氨酰基转移酶 & GGT & 25 & U/L & 10-60 & \\
9 & **碱性磷酸酶 & ALP & 93 & U/L & 45-125 & \\
10 & **天门冬氨酸氨基转移酶 & AST & 21 & U/L & 15-40 & \\
11 & **丙氨酸氨基转移酶 & ALT & 14 & U/L & 9-50 & \\
12 & AST:ALT & AST:ALT & 1.50 & & & \\
13 & 总胆汁酸 & TBA & 1.0 & $\mu$mol/L & 0.0-14.0 & \\
14 & **钾 & K & 4.03 & mmol/L & 3.50-5.30 & \\
15 & **钠 & Na & 140.3 & mmol/L & 137.0-147.0 & \\
16 & **氯 & Cl & 103.5 & mmol/L & 99.0-110.0 & \\
17 & 总二氧化碳 & TCO2 & 25.9 & mmol/L & 21.0-30.0 & \\
18 & 阴离子隙 & ANION & 10.9 & mmol/L & 8.0-16.0 & \\
\hline
\end{tabular}

\begin{tabular}{ccccccc}
\hline
序号 & 项目名称 & 项目代码 & 结果 & 单位 & 参考区间 & 提示 \\
\hline
19 & **钙 & Ca & 2.29 & mmol/L & 2.11-2.52 & \\
20 & **无机磷 & P & 1.09 & mmol/L & 0.85-1.51 & \\
21 & *镁 & MG & 0.85 & mmol/L & 0.75-1.02 & \\
22 & **葡萄糖 & GLU & 5.56 & mmol/L & 3.90-6.10 & \\
23 & **尿素 & UREA & 5.59 & mmol/L & 3.60-9.50 & \\
24 & **肌酐(酶法) & CREA & 71 & $\mu$mol/L & 57-111 & \\
25 & 尿素:肌酐 & UREA:CREA & 0.08 & & & \\
26 & 肾小球滤过率 & eGFR(CKD-EPI) & 91.01 & ml/(min$\cdot$1.73m$^2$) & $\ge$90 & \\
27 & **尿酸 & UA & 367 & $\mu$mol/L & 208-428 & \\
28 & **肌酸激酶 & CK & 33 & U/L & 50-310 & $\downarrow$ \\
29 & **乳酸脱氢酶 & LDH & 192 & U/L & 120-250 & \\
30 & **总胆固醇 & CHOL & 4.41 & mmol/L & 3.12-5.72 & \\
31 & **甘油三酯 & TG & 0.84 & mmol/L & 0.40-1.70 & \\
32 & **高密度脂蛋白胆固醇 & HDL-C & 1.16 & mmol/L & 1.04-1.96 & \\
33 & **低密度脂蛋白胆固醇 & LDL-C & 2.51 & mmol/L & 1.53-3.45 & \\
34 & 非高密度脂蛋白胆固醇 & non-HDL-C & 3.25 & mmol/L & & \\
35 & *脂蛋白(a) & Lp(a) & 538 & mg/L & 0-300 & $\uparrow$ \\
36 & 唾液酸 & SA & 803 & mg/L & 456-754 & $\uparrow$ \\
\hline
\end{tabular}

\begin{tabular}{ccccccc}
\hline
序号 & 项目名称 & 项目代码 & 结果 & 单位 & 参考区间 & 提示 \\
\hline
37 & 渗透压 & OSM & 281.1 & MoSM/L & & \\
38 & 血同型半胱氨酸 & HCY & 10.3 & $\mu$mol/L & 0.0-15.0 & \\
\hline
\end{tabular}
2026-08-10 18:17:54,682 INFO     29 [qwen-vl-parser] page=9 table: 59 LaTeX lines (bbox 393-451)
2026-08-10 18:17:54,682 INFO     29 [qwen-vl-parser] page=9 table: 59 sections
2026-08-10 18:17:54,939 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1782336, prompt_len=764
2026-08-10 18:17:56,410 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-12"
}
```
2026-08-10 18:17:56,411 INFO     29 [qwen-vl-parser] page=10 classify=table report_date=2026-03-12
2026-08-10 18:17:56,420 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1782336, prompt_len=756
2026-08-10 18:18:06,159 INFO     29 [qwen-vl-parser] table API response (len=1973):
\begin{tabular}{cccccc}
\hline
项目名称 & 结果 & 单位 & 参考区间 & 提示 & \\
\hline
白细胞 & 2.2 & 个/ul & 0--9.2 & & \\
红细胞 & 6.7 & 个/ul & 0--13.1 & & \\
上皮细胞 & 2.5 & 个/ul & 0--5.7 & & \\
管型 & 0.00 & 个/ul & 0--2.25 & & \\
电导率 & 15.5 & ms/cm & 3.0--39.0 & & \\
白细胞(高倍视野) & 0 & 个/HPF & 0--3 & & \\
红细胞(高倍视野) & 1 & 个/HPF & 0--2 & & \\
上皮细胞(高倍视野)0 & 0 & 个/HPF & 0--5 & & \\
管型(低倍视野) & 0 & 个/LPF & 0--2 & & \\
小圆上皮细胞 & 无 & & & & \\
类酵母菌 & 无 & & & & \\
结晶 & 无 & & & & \\
红细胞形态信息 & 未提示 & & & & \\
\hline
\end{tabular}

\begin{tabular}{cccccc}
\hline
项目名称 & 结果 & 参考区间 & 提示 & & \\
\hline
*白细胞 & 阴性(-) & 阴性(-) & & & \\
*隐血 & 阴性(-) & 阴性(-) & & & \\
*尿蛋白 & 阴性(-) & 阴性(-) & & & \\
*葡萄糖 & 阴性(-) & 阴性(-) & & & \\
*胆红素 & 阴性(-) & 阴性(-) & & & \\
*尿胆原 & 阴性(-) & 阴性(-) & & & \\
*酸碱度 & 5.0 & 4.5--8.0 & & & \\
*比重 & 1.022 & 1.003--1.030 & & & \\
*亚硝酸盐 & 阴性(-) & 阴性(-) & & & \\
*酮体 & 阴性(-) & 阴性(-) & & & \\
颜色 & 稻黄色 & & & & \\
浊度 & CLEAR & & & & \\
\hline
\end{tabular}

\begin{tabular}{cccccc}
\hline
序号 & 项目名称 & 项目代码 & 结果 & 单位 & 参考区间 & 提示 \\
\hline
1 & 大便颜色 & 大便颜色 & 黄褐色 & & 黄色-黄褐色 & \\
2 & 大便性状 & 大便性状 & 软便 & & 软 & \\
3 & 白细胞 & WBC & 未见 & /HP & 无或偶见 & \\
4 & 红细胞 & RBC & 未见 & /HP & 无 & \\
5 & 巨噬细胞 & 巨噬细胞 & 未见 & 个/HP & & \\
6 & 脂肪球 & 脂肪球 & 未见 & /HP & & \\
7 & 霉菌 & 霉菌 & 未见 & /HP & 无 & \\
8 & 不消化食物 & 不消化食物 & 无 & & & \\
9 & 蛔虫卵 & 蛔虫卵 & 未见 & & & \\
10 & 鞭虫卵 & 鞭虫卵 & 未见 & & & \\
11 & 钩虫卵 & 钩虫卵 & 未见 & & & \\
12 & 蛲虫卵 & 蛲虫卵 & 未见 & & & \\
13 & 肝吸虫卵 & 肝吸虫卵 & 未见 & & & \\
14 & 带绦虫卵 & 带绦虫卵 & 未见 & & & \\
15 & 其它 & 其它 & 未见异常 & & & \\
16 & 隐血 & OB & 阴性(-) & & 阴性(-) & \\
\hline
\end{tabular}

\begin{tabular}{l}
【检查日期】: 2026/3/11 12:07:23 \\
【检查所见】: 脑组织左右对称, 双侧额顶叶及侧脑室旁见斑点状稍长T1稍长T2信号, FLAIR像呈高信号 \\
, DWI未见明显异常信号改变; 双侧基底节区见斑点状长T1长T2信号影; 增强扫描未见强化。脑室系统扩大 \\
, 中线结构居中。脑沟、脑裂、脑池增宽。部分副鼻窦粘膜增厚, 左侧上颌窦内见类圆形长T2长T2信号影。 \\
右侧乳突粘膜增厚。鼻中隔偏曲, 双下鼻甲肥大。 \\
【检查诊断】: 1. 双侧额顶叶及侧脑室旁白质内脱髓鞘改变。 \\
2. 双侧基底节区软化灶形成。 \\
3. 老年脑改变, 双侧额颞部少量硬膜下积液。 \\
4. 部分副鼻窦炎, 左侧上颌窦囊肿; 右侧乳突炎。 \\
5. 鼻中隔偏曲, 双下鼻甲肥大。 \\
以上所见较2025-11-09MR变化不著。 \\
【书写医师】: \\
\end{tabular}
2026-08-10 18:18:06,161 INFO     29 [qwen-vl-parser] page=10 table: 77 LaTeX lines (bbox 452-528)
2026-08-10 18:18:06,162 INFO     29 [qwen-vl-parser] page=10 table: 77 sections
2026-08-10 18:18:06,510 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3190608, prompt_len=764
2026-08-10 18:18:08,000 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-03-11"
}
```
2026-08-10 18:18:08,002 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=2026-03-11
2026-08-10 18:18:08,015 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3190608, prompt_len=401
2026-08-10 18:18:15,496 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:18:15.495+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 86, "failed": 0, "current": {"8fa8ece894e711f1bd9827cf206dfa2d": {"id": "8fa8ece894e711f1bd9827cf206dfa2d", "doc_id": "8f6c718294e711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 16708238, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385769380, "task_type": "dataflow", "root_trace_id": "0aa1bc1a4312482d8e4b2a1774c52cc7", "root_traceparent": "00-0aa1bc1a4312482d8e4b2a1774c52cc7-ad93c0febce673ce-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:18:16,163 INFO     29 [qwen-vl-parser] text API response (len=1073):
["【检查日期】：2026/1/8 13:58:55", "【检查所见】：右侧胸廓塌陷，右侧胸腔内见少量液体密度影，右肺肺组织压缩、密度增高，右肺下叶可", "见一团块状软组织密度影，内见空洞影，增强可见轻度不均匀强化，周围伴条片状密度增高影，与远侧不张", "肺组织分界不清，范围无法测量。右肺小叶间隔增厚。右侧胸膜不均匀增厚伴局部结节状、肿块状，增强可", "见明显强化，邻近右前胸壁及右侧膈肌不规整。双肺内见斑片及索条影。左肺见小结节影，大者位于左肺下", "叶（薄层img180），直径约为0.4cm。纵隔窗未见显示，增强扫描难以评估。气管及主支气管通畅。纵隔右", "偏，纵隔及双肺门内见稍大淋巴结影，大者短径约1.1cm，增强强化欠均匀。心脏大小、形态正常，主动脉", "壁及冠状动脉走行区可见高密度影。", "甲状腺密度不均，内见类圆形低密度影。右侧部分肋骨内缘骨皮质增厚，右侧第7、8、9、12肋局部骨", "质见片状高密度影。", "【检查诊断】：对比2025-11-08CT：", "1.右肺下叶肺癌，范围整体较前增大；右肺小叶间隔增厚，较前进展，考虑癌性淋巴管炎可能；纵隔及双肺", "门淋巴结大致同前；考虑右侧胸膜转移，较前进展，累及邻近右前胸壁及右侧膈肌可能；请结合临床并复查", "。", "2.右侧胸腔积液，较前变化不著。", "3.左肺小结节，较前相仿，建议短期复查。", "4.右侧第7-9、12肋骨高密度影，局部略进展，转移可能，建议ECT进一步检查。", "余所见大致同前。", "【检查描述】：心搏次数：97(60~100) bpm，PR间隔：160 ms，QRS间隔：74 ms，QT间隔：334 ms，QTc", "间隔：424 ms，P轴：51°，QRS轴：7°，T轴：34°", "【检查诊断】：窦性心律", "大致正常心电图", "【检查时间】：2026/3/11 13:54:45", "检查时间", "心率", "2026-03-11 13:54:39", "PR", "97 bpm", "QRS", "160 ms", "QT/QTc", "74 ms", "P/QRS/T", "间期", "334 / 424 ms", "RV5+SV1", "电轴", "51 / 7 / 34 °", "振幅", "/", "mV", "0.000 mV", "AVR", "V1", "V4", "AVL", "V2", "V5", "III", "V3", "V6", "AVF", "II"]
2026-08-10 18:18:16,164 INFO     29 [qwen-vl-parser] page=11 text: 53 lines (bbox 529-581)
2026-08-10 18:18:16,164 INFO     29 [qwen-vl-parser] page=11 text: 53 sections
2026-08-10 18:18:16,311 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=942309, prompt_len=764
2026-08-10 18:18:17,724 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-04-09"
}
```
2026-08-10 18:18:17,725 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=2025-04-09
2026-08-10 18:18:17,745 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=942309, prompt_len=401
2026-08-10 18:18:19,937 INFO     29 [qwen-vl-parser] text API response (len=336):
["【手术信息】：胸腔积液", "【取材部位】：1:胸膜×1", "2:细胞蜡块1×1", "【取材描述】：胸膜×多", "【大体描述】：胸膜：灰白小组织一堆，大小1*0.8*0.5cm。", "【病理所见】：胸膜：灰白小组织一堆，大小1*0.8*0.5cm。", "【病理诊断】：（胸膜活检）送检增生的纤维组织内见腺癌浸润，请结合临床诊治。", "免疫组化：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（部分+）、P40（点灶+）、CR（灶+）、ALK", "（1A4）（-）、Ki67（+，40%）。", "【报告时间】：2025/4/9 10:06:00", "一线：培美曲塞+顺铂+信迪利单抗，二线：培美曲", "塞+顺铂+信迪利单抗+恩度"]
2026-08-10 18:18:19,938 INFO     29 [qwen-vl-parser] page=12 text: 12 lines (bbox 582-593)
2026-08-10 18:18:19,938 INFO     29 [qwen-vl-parser] page=12 text: 12 sections
2026-08-10 18:18:19,939 INFO     29 [qwen-vl-parser] parse_pdf done: 594 sections from 12 pages.
2026-08-10 18:18:19,949 INFO     29 Close text detector.
2026-08-10 18:18:20,338 INFO     29 Close text recognizer.
2026-08-10 18:18:20,758 INFO     29 Close recognizer.
2026-08-10 18:18:21,191 INFO     29 Close recognizer.
2026-08-10 18:18:21,595 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 18:18:21,596 INFO     29 [Trace] task=8fa8ece8 | doc=07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf | Parser:MedLink | outputs={"html": "", "json": "594 items", "markdown": "", "text": "", "name": "07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf", "output_format": "json"}
2026-08-10 18:18:21,596 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 18:18:21,612 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:18:21,612 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 性别：男\n[BBOX-1] 婚姻：已婚\n[BBOX-2] 年龄：69岁\n[BBOX-3] 入院日期：2026-03-11 08:04\n[BBOX-4] 民族：汉族\n[BBOX-5] 记录日期：2026-03-11 08:06\n[BBOX-6] 职业：农民\n[BBOX-7] 病史陈述者：患者本人\n[BBOX-8] 主诉：确诊肺腺癌10月余，咯血2天余。\n[BBOX-9] 现病史：患者因“呼吸困难2月余”于2025-04-05第1次入院，入院后完善检验检查：\n[BBOX-10] CEA(胸水)：癌胚抗原 538ng/ml；于04-07完善胸腔镜检查：镜下诊断：胸腔积液，胸壁结节\n[BBOX-11] 样改变。病理：（胸膜活检）送检增生的纤维组织内见腺癌浸润，请结合临床诊治。免疫组\n[BBOX-12] 化：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（部分+）、P40（点灶+）、CR（灶\n[BBOX-13] +）、ALK（1A4）（-）、Ki67（+，40%）。完善评估检查：胸部增强(64排-128层)：1.符合\n[BBOX-14] 右侧胸腔引流术后改变，右侧液气胸并右侧颈根部及胸壁积气，肺组织压缩约70%。2.右肺\n[BBOX-15] 下叶占位，考虑肺癌并纵隔及双肺门淋巴结转移可能，右侧胸膜结节状增厚、强化，考虑转\n[BBOX-16] 移，请结合临床。3.左肺小结节，目前考虑良性，建议短期复查。4.双肺慢性炎症/纤维\n[BBOX-17] 灶。5.动脉粥样硬化表现。6.甲状腺改变，请结合超声检查。7.右侧第8肋骨质改变，请结\n[BBOX-18] 合临床。全身骨显像：1.右侧第6-8侧肋异常放射性浓聚，本院CT（2025-04-09）第6、7肋\n[BBOX-19] 骨未见明显骨质异常，第8肋髓腔内见局灶高密度影，建议短期CT复查。2.左侧坐骨轻度放\n[BBOX-20] 射性浓聚灶，本院CT未见明显骨质破坏，建议随诊。04-14复查胸部CT：对比2025-04-09\n[BBOX-21] CT：1.符合右侧胸腔引流术后改变，右侧液气胸并右侧颈根部及胸壁积气，较前减轻，肺组\n[BBOX-22] 织压缩约30%。2.右肺下叶占位，较前相仿，考虑肺癌；纵隔及双肺门淋巴结同前；右侧胸\n[BBOX-23] 膜结节状增厚，较前局部稍减轻，请结合临床。3.左肺小结节，较前相仿，建议短期复查。\n[BBOX-24] 余所见大致同前。04-16复查胸片：1.右侧胸腔引流术后表现，对比2025-04-11X线：右侧气\n[BBOX-25] 胸较前明显减少；原右侧胸壁及胸壁皮下积气基本消失；右侧胸腔积液较前减少，建议复查\n[BBOX-26] 或结合CT检查。2.右肺下野占位，请结合临床及CT检查。患者完善基因检测未见基因突变，\n[BBOX-27] 于04-17给予第1周期全身化疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2 q21d，同时辅\n[BBOX-28] 以止吐、护胃、保肝、激素减轻化疗不良反应等治疗。于04-19给予信迪利单抗200mg抗肿瘤\n[BBOX-29] 免疫治疗。患者化疗顺利，准予出院。末次出院诊断：1.肺腺癌伴纵隔淋巴结、肺门淋巴\n[BBOX-30] 结、胸膜转移（T2bN3M1 IV期）恶性胸腔积液 2.气胸 3.左侧大隐静脉曲张 4.肝囊肿 5.双\n[BBOX-31] 肾囊肿 6.前列腺稍大伴钙化\n[BBOX-32] 患者因“确诊肺腺癌1月”于2025-05-07第2次入院，入院后完善相关检查：肺肿瘤检\n[BBOX-33] 验：癌胚抗原 62.1ng/ml，神经元特异性烯醇化酶 19.8ng/ml，细胞角蛋白19片段\n[BBOX-34] 6.21ng/ml；大便常规：未见异常；髂静脉及下肢深静脉、下肢浅静脉：左侧大隐静脉曲张，\n[BBOX-35] 左侧隐股静脉瓣功能不全；胸部平扫(64排-128层)：对比2025-04-14CT：1.符合右侧胸腔引\n[BBOX-36] 流术后改变，右侧液气胸，积液较前增多，积气较前减少；原右侧颈根部及胸壁少量积气本\n[BBOX-37] 第1页\n[BBOX-38] 次吸收。2.右肺下叶占位，较前略缩小，考虑肺癌；纵隔及双肺门淋巴结部分较前略增大；\n[BBOX-39] 右侧胸膜结节状增厚，较前局部稍减轻，请结合临床。3.左肺小结节，较前相仿，建议短期\n[BBOX-40] 复查。余所见大致同前。入院后于05-09拔除胸腔引流管。排除禁忌于05-09行第2周期全身\n[BBOX-41] 化疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2 q21d，并辅以激素、止吐、护胃、保肝\n[BBOX-42] 等治疗，05-10给予信迪利单抗200mg肿瘤免疫治疗。患者治疗结束，于2025-05-11出院。\n[BBOX-43] 患者因“确诊肺腺癌1月余，发热5天”于2025-05-19第3次入院，入院后完善检验检\n[BBOX-44] 查：大便菌群分析:细菌总数600 个/油镜视野（参考值500～5000个），革兰阳性球菌少量，\n[BBOX-45] 革兰阴性杆菌少量，酵母样真菌孢子+，酵母样真菌菌丝+；艰难梭菌毒素A/B检测:艰难梭\n[BBOX-46] 菌毒素A/B检测 0.02；大便细菌培养+药敏:经两天普通培养，鉴定生长热带念珠菌+++，无\n[BBOX-47] 肠球菌生长，无肠杆菌生长，无沙门氏菌、志贺氏菌生长。痰细菌学检查:经2天普通培养，\n[BBOX-48] 经鉴定为正常菌群生长，无流感嗜血杆菌生长。胸部平扫(64排-128层)：对比\n[BBOX-49] 2025-04-14CT：1.符合右侧胸腔引流术后改变，右侧液气胸，积液较前增多，积气较前减\n[BBOX-50] 少；原右侧颈根部及胸壁少量积气本次吸收。2.右肺下叶占位，较前略缩小，考虑肺癌；纵\n[BBOX-51] 隔及双肺门淋巴结部分较前略增大；右侧胸膜结节状增厚，较前局部稍减轻，请结合临床。\n[BBOX-52] 3.左肺小结节，较前相仿，建议短期复查。余所见大致同前。腹部（包括盆腔）平扫(64\n[BBOX-53] 排)：1.考虑肝多发囊肿、右肾囊肿，必要时增强扫描。2.双肾周桥隔略增厚。3.动脉粥样\n[BBOX-54] 硬化。4.前列腺增大伴钙化。5.L5椎体前滑脱（I°），双侧椎弓峡部裂。胸部平扫(64排\n[BBOX-55] -128层)：对比2025-05-08CT：1.右侧液气胸，积液较前增多，积气较前减少。2.右肺下叶\n[BBOX-56] 占位，较前缩小，考虑肺癌；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜结节状增\n[BBOX-57] 厚，较前变化不著，请结合临床。3.左肺小结节，较前相仿，建议短期复查。余所见大致同\n[BBOX-58] 前。入院后给予哌拉西林他唑巴坦抗感染，蒙脱石散止泻，枯草杆菌二联活菌胶囊调整消化\n[BBOX-59] 道菌群，利伐沙班抗凝，制霉素片口服治疗，现患者病情稳定，于2025-05-29出院。\n[BBOX-60] 患者因“确诊肺腺癌2月余。”第4次入院，入院后完善辅助检查，入院后排除禁忌，\n[BBOX-61] 06-06行第3周期治疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2，联合信迪利单抗200mg\n[BBOX-62] 抗肿瘤免疫治疗，并辅以激素、止吐、护胃、保肝等治疗，治疗结束后复查血常规未见明显\n[BBOX-63] 骨髓抑制，于2025-06-08出院。末次出院诊断：1.恶性肿瘤维持性化学治疗 2.恶性肿瘤免\n[BBOX-64] 疫治疗 3.肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转移 肺门淋巴结转移 胸膜转移 恶性胸腔\n[BBOX-65] 积液 4.大隐静脉曲张 5.肾囊肿 6.单纯性肝囊肿。\n[BBOX-66] 患者因“确诊肺腺癌2月余，为继续治疗”于2025-06-26第5次入院，入院后完善相关检\n[BBOX-67] 查，排除禁忌，06-27行第4周期治疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2，联合\n[BBOX-68] 信迪利单抗200mg抗肿瘤免疫治疗，并辅以激素、止吐、护胃、保肝等治疗，治疗结束后复\n[BBOX-69] 查血常规未见明显骨髓抑制，于2025-06-29出院。末次出院诊断：1.恶性肿瘤维持性化学治\n[BBOX-70] 疗 2.恶性肿瘤免疫治疗 3.肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转移 肺门淋巴结转移 胸\n[BBOX-71] 膜转移 4.恶性胸腔积液 5.大隐静脉曲张 6.肾囊肿 7.单纯性肝囊肿.\n[BBOX-72] 患者因“确诊肺腺癌3月余，为继续治疗”2025-07-17入院，入院后完善相关必要辅助\n[BBOX-73] 第2页\n[BBOX-74] 检查：电解质+血气分析:酸碱度7.476，二氧化碳分压36.4mmHg，氧分压114.0mmHg；急\n[BBOX-75] 查血常规+CRP:红细胞3.61x10^12/L，血红蛋白110g/L，血小板总数222×10^9/L，白细\n[BBOX-76] 胞4.90×10^9/L，中性粒细胞绝对值3.59×10^9/L，淋巴细胞绝对值0.77×10^9/L，超\n[BBOX-77] 敏C-反应蛋白17.92mg/L；肺肿瘤检验：癌胚抗原54.9ng/ml，细胞角蛋白19片段\n[BBOX-78] 5.54ng/ml，胃泌素释放肽前体80.2pg/ml；生化系列36项:白蛋白(溴甲酚绿法)\n[BBOX-79] 31.59g/L，镁0.72mmol/L，肌酐(酶法)55μmol/L，肌酸激酶31U/L；DIC系列-5项:纤维\n[BBOX-80] 蛋白原5.47g/L，D-二聚体3.53mg/L；急查降钙素原、急查心梗三项、皮质醇(7:00-10:\n[BBOX-81] 00am)、促肾上腺皮质激素(8时)、甲状腺功能3项、急查NT-proBNP、大便常规(粪沉渣)+\n[BBOX-82] 潜血、尿液分析+尿沉渣未见明显异常。常规心电图检查(自动分析)：窦性心动过速；心\n[BBOX-83] 脏超声检查(含左心功能测定)：主动脉瓣轻度反流，三尖瓣轻度反流；颅脑平扫+DWI+增\n[BBOX-84] 强(3T)：1.双侧额顶叶及侧脑室旁白质内脱髓鞘改变。2.老年脑改变。3.部分副鼻窦炎；\n[BBOX-85] 右侧乳突炎。4.鼻中隔偏曲，双下鼻甲肥大。颈部：左侧颈部淋巴结稍大，右侧颈部淋巴结\n[BBOX-86] 可见；髂静脉及下肢深静脉、下肢浅静脉：左侧大隐静脉曲张，左侧隐股静脉瓣功能不全；\n[BBOX-87] 腹部(包括盆腔)平扫(64排)：1.考虑肝多发囊肿、右肾囊肿，必要时增强扫描。2.双肾周\n[BBOX-88] 桥隔略增厚。3.动脉粥样硬化。4.前列腺增大伴钙化。5.L5椎体前滑脱(I°)，双侧椎弓\n[BBOX-89] 峡部裂。以上所见较2025-05-26CT变化不著。胸部平扫(64排-128层)：对比2025-05-26CT:\n[BBOX-90] 1.右肺下叶肺癌，较前略缩小、其内新见空洞影；右肺小叶间隔增厚，考虑癌性淋巴管炎可\n[BBOX-91] 能；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜结节状增厚，较前变化不著；请结合\n[BBOX-92] 临床。2.右侧液气胸，积液较前略增多，积气较前明显减少。3.左肺小结节，较前相仿，建\n[BBOX-93] 议短期复查。4.右侧第7-9、12肋骨高密度影，较前密度增高，转移?建议ECT进一步检查。\n[BBOX-94] 余所见大致同前。肋骨平扫+DWI+增强(3T)：1.右侧第7-9、12肋改变，成骨性转移?请结\n[BBOX-95] 合其它影像学检查。2.右侧胸腔积液。3.肝内多发囊肿。排除禁忌，07-18行第5周期治疗：\n[BBOX-96] 培美曲塞0.8gd1+顺铂注射液65mgd1、d2，联合信迪利单抗200mg抗肿瘤免疫治疗，并辅\n[BBOX-97] 以激素、止吐、护胃、保肝等治疗，治疗结束后复查血常规未见明显骨髓抑制，针对肋骨异\n[BBOX-98] 常请放疗科会诊后建议可考虑放疗，07-21出院。\n[BBOX-99] 患者因“确诊肺腺癌4月，为继续治疗”2025-08-07第7次入院，入院后完善相关检查，\n[BBOX-100] 急查血常规+CRP:血红蛋白109g/L，血小板总数205×10^9/L，白细胞4.58×10^9/L，中\n[BBOX-101] 性粒细胞百分率70.9%，超敏C-反应蛋白17.43mg/L；超敏肌钙蛋白T14.80pg/ml；DIC系\n[BBOX-102] 列-5项:纤维蛋白原5.27g/L，D-二聚体4.37mg/L；N端-B型钠尿肽前体71.5pg/ml；促肾\n[BBOX-103] 上腺皮质激素(8时)：促肾上腺皮质激素(8时)31.7pg/ml；生化系列36项:白蛋白(溴甲酚绿\n[BBOX-104] 法)33.34g/L，钾3.93mmol/L，钠140.1mmol/L，氯104.8mmol/L，尿素5.04mmol/L，肌\n[BBOX-105] 酐(酶法)65μmol/L；皮质醇(7:00-10:00am)：皮质醇(7:00-10:00am)295nmol/L；甲状腺\n[BBOX-106] 功能3项：促甲状腺素3.17mIU/L，游离甲状腺素13.6pmol/L，游离三碘甲状腺原氨酸\n[BBOX-107] 4.46pmol/L；肺肿瘤检验：癌胚抗原52.6ng/ml，神经元特异性烯醇化酶20.4ng/ml，\n[BBOX-108] 细胞角蛋白19片段4.81ng/ml，胃泌素释放肽前体92.9pg/ml。常规心电图检查(自动分\n[BBOX-109] 第3页\n[BBOX-110] 析）：窦性心律，大致正常心电图。排除禁忌，于08-08给予第6周期化疗，方案为培美曲塞\n[BBOX-111] 0.8g+顺铂注射液 65mg d1、d2，联合信迪利单抗200mg 免疫治疗，过程顺利，08-10行地\n[BBOX-112] 舒单抗120mg抗骨转移治疗；复查血常规未见明显骨髓抑制，08-10出院。\n[BBOX-113] 患者因“确诊肺腺癌4月，为继续治疗”于2025-08-28第8次入院，入院后完善辅助检\n[BBOX-114] 查：胸部平扫：对比2025-07-18CT：1.右肺下叶肺癌，较前变化不著；右肺小叶间隔增厚，\n[BBOX-115] 较前变化不著，考虑癌性淋巴管炎可能；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜\n[BBOX-116] 结节状增厚，较前变化不著；请结合临床。2.右侧液气胸，积液较前变化不著，积气较前增\n[BBOX-117] 多。3.左肺小结节，较前相仿，建议短期复查。4.右侧第7-9、12肋骨高密度影，较前变化\n[BBOX-118] 不著，转移？建议ECT进一步检查。余所见大致同前。下腹部平扫：1.考虑右肾囊肿，较\n[BBOX-119] 2025-07-18变化不著，必要时增强扫描。2.双肾周桥隔略增厚。3.动脉粥样硬化。上腹部平\n[BBOX-120] 扫：考虑肝多发囊肿，较2025-07-18变化不明显，建议结合增强检查明确。盆腔平扫：1.前\n[BBOX-121] 列腺增大伴钙化。2.L5椎体前滑脱（I°），双侧椎弓峡部裂。以上所见较2025-07-18变化\n[BBOX-122] 不著。排除禁忌，给予培美曲塞 0.8g 联合信迪利单抗 200mg免疫治疗，并辅以激素、止\n[BBOX-123] 吐、护胃、保肝等治疗，治疗过程顺利，患者病情稳定，2025-08-30出院。出院诊断：1.恶\n[BBOX-124] 性肿瘤维持性化学治疗 2.恶性肿瘤免疫治疗 3.右肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转\n[BBOX-125] 移 肺门淋巴结转移 胸膜转移 骨转移 4.恶性胸腔积液 5.大隐静脉曲张 6.肾囊肿 7.单纯\n[BBOX-126] 性肝囊肿。\n[BBOX-127] 患者因“确诊肺腺癌5月余，为继续治疗”于2025-10-06第9次入院，入院后完善辅助检\n[BBOX-128] 查：急查血常规+CRP:血红蛋白 114g/L，血小板总数 212×10^9/L，白细胞\n[BBOX-129] 7.30×10^9/L，中性粒细胞百分率 80.0%，超敏C-反应蛋白 16.04mg/L；皮质醇(7:00-10:\n[BBOX-130] 00am):皮质醇(7:00-10:00am) 442nmol/L；促肾上腺皮质激素(8时):促肾上腺皮质激素(8\n[BBOX-131] 时) 29.3pg/ml；甲状腺功能3项:促甲状腺素 4.94mIU/L，游离甲状腺素 14.4pmol/L，游离\n[BBOX-132] 三碘甲状腺原氨酸 3.85pmol/L；生化系列36项:白蛋白(溴甲酚绿法) 36.10g/L，白蛋白:球\n[BBOX-133] 蛋白 0.96，天门冬氨酸氨基转移酶 18U/L，丙氨酸氨基转移酶 8U/L，尿素 5.84mmol/L，\n[BBOX-134] 肌酐(酶法) 78μmol/L；肺肿瘤检验-莱山:癌胚抗原 68.6ng/ml，细胞角蛋白19片段\n[BBOX-135] 9.45ng/ml，胃泌素释放肽前体 96.7pg/ml；DIC系列-5项:纤维蛋白原 5.04g/L，D-二聚体\n[BBOX-136] 3.28mg/L；急查NT-proBNP:N端-B型钠尿肽前体 50.1pg/ml；急查心梗三项:超敏肌钙蛋白T\n[BBOX-137] 14.00pg/ml，肌酸激酶-MB同工酶质量测定 0.54ng/ml，肌红蛋白 43.2ng/ml。排除禁忌，\n[BBOX-138] 于2025-10-06给予本周期治疗，方案为培美曲塞 0.8g联合信迪利单抗200mg，并给予地舒单\n[BBOX-139] 抗120mg治疗骨转移，2025-10-07办理出院。出院诊断：1.右肺腺癌（T2bN3M1 IV期） 纵隔\n[BBOX-140] 淋巴结转移 肺门淋巴结转移 胸膜转移 骨转移 2.恶性胸腔积液 3.大隐静脉曲张 4.肾囊肿\n[BBOX-141] 5.单纯性肝囊肿。\n[BBOX-142] 患者因“确诊肺腺癌7月余，为继续治疗”于2025-11-07第10次入院，入院后完善相关\n[BBOX-143] 检查：急查血常规+CRP:血红蛋白 115g/L，血小板总数 214×10^9/L，白细胞\n[BBOX-144] 7.21×10^9/L，中性粒细胞百分率 82.3%，超敏C-反应蛋白 20.50mg/L；DIC系列-5项:纤维\n[BBOX-145] 第 4 页\n[BBOX-146] 蛋白原 5.04g/L，D-二聚体 2.19mg/L；皮质醇(7:00-10:00am):皮质醇(7:00-10:00am)\n[BBOX-147] 286nmol/L；促肾上腺皮质激素(8时):促肾上腺皮质激素(8时)23.3pg/ml；急查心梗���项:\n[BBOX-148] 超敏肌钙蛋白T 17.70pg/ml；肺肿瘤检验-莱山:癌胚抗原 75.8ng/ml，细胞角蛋白19片段\n[BBOX-149] 12.4ng/ml，胃泌素释放肽前体 90.5pg/ml；生化系列36项:白蛋白(溴甲酚绿法)\n[BBOX-150] 32.49g/L，脂蛋白(a)343mg/L，唾液酸 769mg/L；N端-B型钠尿肽前体、甲状腺功能3项未\n[BBOX-151] 见异常。常规心电图检查：窦性心动过速。全身骨显像：与本院2025-04-10骨显像比较：1.\n[BBOX-152] 右侧多根肋骨多发异常放射性浓聚灶，病灶数目较前增多，浓聚程度增高，提示骨转移瘤可\n[BBOX-153] 能大，请结合其他检查综合考虑；2.前次检查所示左侧坐骨轻度放射性浓聚灶，本次检查未\n[BBOX-154] 见显示；3.双肩关节及双膝关节区异常放射性浓聚，考虑炎性病变，请结合临床。颅脑平扫\n[BBOX-155] +DWI+增强+薄层：1.双侧额顶叶及侧脑室旁白质内脱髓鞘改变；2.老年脑改变，双侧额颞部\n[BBOX-156] 少量硬膜下积液；3.部分副鼻窦炎；右侧乳突炎；4.鼻中隔偏曲，双下鼻甲肥大。心脏超声\n[BBOX-157] 检查（含左心功能测定）：静息状态下：心内结构及血流未见明显异常髂静脉及下肢深静脉\n[BBOX-158] (双侧)：双侧髂静脉及下肢深静脉血流通畅颈部：双侧颈部未见明显增大淋巴结胸部平扫\n[BBOX-159] +增强：对比2025-08-28CT：1.右肺下叶肺癌，较前增大；右肺小叶间隔增厚，较前略进\n[BBOX-160] 展，考虑癌性淋巴管炎可能；纵隔及双肺门淋巴结，部分较前略增大；考虑右侧胸膜转移，\n[BBOX-161] 较前明显进展，累及邻近右前胸壁及右侧膈肌可能；请结合临床并复查；2.右侧胸腔积液，\n[BBOX-162] 较前变化不著，原右侧胸腔积气吸收；3.左肺小结节，部分较前略增大（如下叶薄层\n[BBOX-163] img231、243），部分结节较前相仿，建议短期复查；4.右侧第7-9、12肋骨高密度影，较前\n[BBOX-164] 变化不著，转移？建议ECT进一步检查；余所见大致同前。上腹部平扫+增强：考虑肝多发囊\n[BBOX-165] 肿，较2025-08-28变化不明显。下腹部平扫+增强：1.考虑右肾囊肿，较2025-08-28变化不\n[BBOX-166] 著；2.双肾周桥隔略增厚；3.动脉粥样硬化。排除禁忌给予本周期治疗，方案为培美曲塞\n[BBOX-167] 0.8g、信迪利单抗200mg联合恩度 210mg q21d治疗。治疗结束，患者病情稳定，2025-11-14\n[BBOX-168] 办理出院。出院诊断：1.右肺腺癌(T2bN3M1 IV期) 纵隔淋巴结转移 肺门淋巴结转移 胸\n[BBOX-169] 膜转移 骨转移 2.恶性胸腔积液 3.大隐静脉曲张 4.肾囊肿 5.肝囊肿\n[BBOX-170] 患者因“确诊肺腺癌8月余，为继续治疗”于2026-01-08再入院，入院后完善相关辅助\n[BBOX-171] 检查：01-08：急查NT-proBNP、促肾上腺皮质激素(8时)、皮质醇(7:00-10:00am)等未见明\n[BBOX-172] 显异常。急查血常规+CRP+SAA:红细胞 3.93x10^12/L，血红蛋白 118g/L，红细胞压积\n[BBOX-173] 35.8%，红细胞分布宽度SD 47.4fl，中性粒细胞百分率 77.9%，淋巴细胞百分率 9.4%，单\n[BBOX-174] 核细胞百分率 10.2%，淋巴细胞绝对值 0.67×10^9/L，单核细胞绝对值 0.73×10^9/L，超\n[BBOX-175] 敏C-反应蛋白 30.56mg/L，血清淀粉样蛋白A 26.98mg/L；急查心梗三项:超敏肌钙蛋白T\n[BBOX-176] 15.10pg/ml；DIC系列-5项:纤维蛋白原 6.22g/L，D-二聚体 1.66mg/L；急查降钙素原：\n[BBOX-177] 0.0969ng/ml；生化系列36项:白蛋白(溴甲酚绿法) 31.69g/L，白蛋白:球蛋白 0.87，肾小\n[BBOX-178] 球滤过率 89.97ml/(min·1.73m²)，肌酸激酶 38U/L，脂蛋白(a) 452mg/L，唾液酸\n[BBOX-179] 765mg/L；甲状腺功能6项:促甲状腺素 4.69mIU/L；肺肿瘤检验\n[BBOX-180] 癌胚抗原\n[BBOX-181] 73.4ng/ml，神经元特异性烯醇化酶 18.4ng/ml，细胞角蛋白19片段 19.1ng/ml，胃泌素释\n[BBOX-182] 第5页\n[BBOX-183] 放肽前体81.4pg/ml；常规心电图检查（自动分析）：窦性心动过速。下腹部平扫+增强：\n[BBOX-184] 1.考虑右肾囊肿，较2025-11-08变化不著。2.双肾周桥隔略增厚。3.动脉粥样硬化。上腹部\n[BBOX-185] 平扫+增强：考虑肝多发囊肿，较2025-11-08变化不明显。胸部平扫+增强：对比\n[BBOX-186] 2025-11-08CT：1.右肺下叶肺癌，范围整体较前增大；右肺小叶间隔增厚，较前进展，考虑\n[BBOX-187] 癌性淋巴管炎可能；纵隔及双肺门淋巴结大致同前；考虑右侧胸膜转移，较前进展，累及邻\n[BBOX-188] 近右前胸壁及右侧膈肌可能；请结合临床并复查。2.右侧胸腔积液，较前变化不著。3.左肺\n[BBOX-189] 小结节，较前相仿，建议短期复查。4.右侧第7-9、12肋骨高密度影，局部略进展，转移可\n[BBOX-190] 能，建议ECT进一步检查。余所见大致同前。01-09：髂静脉及下肢深静脉、下肢浅静脉：左\n[BBOX-191] 侧大隐静脉曲张左侧隐股静脉瓣功能不全。01-10：心脏超声检查（含左心功能测定）：静\n[BBOX-192] 息状态下：心内结构及血流未见明显异常。考虑患者肿瘤较前进展，请肿瘤科及放疗科会\n[BBOX-193] 诊，给予更换二线化疗方案，排除禁忌，1-09行开始给予恩度抗血管生成，01-12给予二线\n[BBOX-194] 第1周期全身化疗：白蛋白紫杉醇300mg d1、信迪利单抗200mg，01-13给予地舒单抗120mg抗\n[BBOX-195] 骨转移。期间联合护肝、护胃、止吐、激素等治疗，现病情平稳，准予出院。末次出院诊\n[BBOX-196] 断：1.右肺腺癌（T2bN3M1 IV期）纵隔淋巴结转移肺门淋巴结转移胸膜转移骨转移2.\n[BBOX-197] 恶性胸腔积液3.大隐静脉曲张4.肾囊肿5.肝囊肿6.贫血7.低蛋白血症\n[BBOX-198] 患者出院后规律服药、门诊复诊，偶有咳嗽，咳白薄痰，腰肋部水肿，于2026-2-10再\n[BBOX-199] 入院，\n[BBOX-200] 入院后完善辅助检查：NT-proBNP未见明显异常；血常规+CRP+SAA：红细胞\n[BBOX-201] 4.25x10^12/L，血红蛋白125g/L，红细胞压积38.4%，红细胞分布宽度SD47.8fl，中性粒\n[BBOX-202] 细胞百分率83.4%，淋巴细胞百分率8.0%，中性粒细胞绝对值7.35×10^9/L，淋巴细胞绝\n[BBOX-203] 对值0.70×10^9/L，单核细胞绝对值0.62×10^9/L，超敏C-反应蛋白24.16mg/L，血清淀\n[BBOX-204] 粉样蛋白A13.13mg/L；心梗三项：超敏肌钙蛋白T14.10pg/ml；降钙素原：0.0528ng/ml；生\n[BBOX-205] 化系列36项：白蛋白（溴甲酚绿法）34.82g/L，白蛋白：球蛋白1.02，肾小球滤过率\n[BBOX-206] 89.97ml/(min•1.73m²)，肌酸激酶33U/L，脂蛋白(a)510mg/L，唾液酸792mg/L；肺肿瘤\n[BBOX-207] 检验：癌胚抗原100ng/ml，神经元特异性烯醇化酶31.1ng/ml，细胞角蛋白19片段\n[BBOX-208] 28.8ng/ml，胃泌素释放肽前体87.7pg/ml；DIC系列-5项：纤维蛋白原6.71g/L，D-二聚体\n[BBOX-209] 1.42mg/L；心电图：窦性心律大致正常心电图。尿液分析、大便常规及潜血、促肾上腺皮\n[BBOX-210] 质激素(8时)、皮质醇(7:00-10:00am)、甲状腺功能6项等未见明显异常。排除禁忌，02-10\n[BBOX-211] 开始给予恩度抗血管生成，02-11给予二线第2周期全身化疗：白蛋白紫杉醇300mg d1，同时\n[BBOX-212] 辅以激素、止吐、护胃、保肝治疗，同时给予信迪利单抗200mg抗肿瘤免疫治疗，02-12给予\n[BBOX-213] 地舒单抗120mg抗骨转移治疗。于2026-02-13出院。末次出院诊断：1.恶性肿瘤维持性化学\n[BBOX-214] 治疗2.恶性肿瘤免疫治疗3.恶性肿瘤靶向治疗4.右肺腺癌（T2bN3M1 IV期）纵隔淋巴结\n[BBOX-215] 转移肺门淋巴结转移胸膜转移骨转移5.恶性胸腔积液6.大隐静脉曲张7.肾囊肿8.肝\n[BBOX-216] 囊肿。\n[BBOX-217] 患者出院后规律门诊复诊，偶有咳嗽、咳痰，2天前无明显诱因出现咯血，感痰较前增\n[BBOX-218] 第6页\n[BBOX-219] 多，每天数十口，色鲜红，今为进一步治疗入院。患者病后神志清，精神状态一般，食欲一\n[BBOX-220] 般，睡眠良好，大便正常，小便正常，体力情况一般，体重无明显变化。\n[BBOX-221] 既往史：否认食物、药物过敏史，参阅既往入院记录。\n[BBOX-222] 个人史：参阅既往入院记录。\n[BBOX-223] 家族史：参阅既往入院记录。\n[BBOX-224] 体 格 检 查\n[BBOX-225] T 36.3℃ P 107次/分 R 21次/分 Bp 144/99mmHg\n[BBOX-226] 发育正常，营养良好，正常面容，表情自如，自主体位，神志清楚，查体合作。全身皮\n[BBOX-227] 肤粘膜无黄染，无皮疹，无皮下出血，无皮下结节，皮下无水肿，无肝掌、蜘蛛痣，毛发分\n[BBOX-228] 布均匀。全身浅表淋巴结无肿大。眼睑无水肿，结膜无苍白，眼球无突出，无震颤，巩膜无\n[BBOX-229] 黄染，瞳孔等大等圆，对光反射灵敏，耳廓对称，无畸形，牵拉无疼痛，外耳道无异常分泌\n[BBOX-230] 物，乳突无压痛，无听力粗试障碍。鼻无畸形。口唇无发绀，口腔粘膜无充血、糜烂。舌苔\n[BBOX-231] 薄白，伸舌无偏斜、震颤，牙龈无红肿，咽部粘膜无充血，扁桃体无肿大。颈软无抵抗，颈\n[BBOX-232] 动脉无异常搏动，半坐位颈静脉未见充盈，颈部大血管区未闻及血管杂音。气管居中，肝颈\n[BBOX-233] 静脉回流征阴性，甲状腺无肿大，无压痛、震颤、血管杂音。胸廓无畸形，呼吸运动两侧对\n[BBOX-234] 称，肋间隙无狭窄或饱满，胸壁无压痛，语颤无增强、减弱，胸骨无压痛。双肺叩诊清音，\n[BBOX-235] 呼吸规整，双肺呼吸音低，未闻及干湿性啰音，无胸膜摩擦音。心前区无异常隆起、异常搏\n[BBOX-236] 动、震颤，心浊音界不大，心率107次/分，律齐，心音有力，各瓣膜听诊区未闻及杂音，无\n[BBOX-237] 心包摩擦音。腹平坦，软，无压痛、反跳痛，腹部无包块。肝脏未触及，脾脏未触及，\n[BBOX-238] Murphy氏征阴性，肾区无叩击痛，无移动性浊音。肠鸣音正常，4次/分。肛门及外生殖器未\n[BBOX-239] 查。脊柱正常生理弯曲，四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾），关节无肿\n[BBOX-240] 胀、压痛，下肢无浮肿。\n[BBOX-241] 肌肉无压痛，四肢肌力、肌张力未见异常，双侧肱\n[BBOX-242] 二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性。\n[BBOX-243] 专科检查： 胸廓无畸形，呼吸运动两侧对称，肋间隙无狭窄或饱满，胸壁无压痛，语\n[BBOX-244] 颤无增强、减弱，胸骨无压痛。双肺叩诊清音，呼吸规整，双肺呼吸音低，未闻及干湿性啰\n[BBOX-245] 音，无胸膜摩擦音。\n[BBOX-246] 辅 助 检 查\n[BBOX-247] 检查日期 项目 结果 检查单位 检查编号\n[BBOX-248] 第 7 页\n[BBOX-249] 2025-04-09\n[BBOX-250] 病理\n[BBOX-251] (胸膜活检)送检增生的纤维组\n[BBOX-252] 织内见腺癌浸润，请结合临床诊\n[BBOX-253] 治。免疫组化：TTF-1（-）、\n[BBOX-254] NapsinA（-）、CK7（+）、CK5/6\n[BBOX-255] （部分+）、P40（点灶+）、CR（\n[BBOX-256] 灶+）、ALK（1A4）（-）、Ki67\n[BBOX-257] (+,40%）。C-MET免疫组化检测\n[BBOX-258] 报告检测平台：Roche Ventana\n[BBOX-259] Benchmark Ultra；抗体克隆号：\n[BBOX-260] SP44,Roche；表达部位：细胞膜和\n[BBOX-261] 细胞浆；阳性强度及百分比：++(\n[BBOX-262] 40%),+(60%)阳性等级：1+\n[BBOX-263] 细胞数量：≥100。\n[BBOX-264] 初步诊断：\n[BBOX-265] 1.咯血\n[BBOX-266] 2.右肺腺癌（T2bN3M1 IV期）\n[BBOX-267] 纵隔淋巴结转移\n[BBOX-268] 肺门淋巴结转移\n[BBOX-269] 胸膜转移\n[BBOX-270] 骨转移\n[BBOX-271] 3.恶性胸腔积液\n[BBOX-272] 4.大隐静脉曲张\n[BBOX-273] 5.肾囊肿\n[BBOX-274] 6.肝囊肿\n[BBOX-275] 项目名称\n[BBOX-276] 结果\n[BBOX-277] 单位\n[BBOX-278] 参考范围\n[BBOX-279] 项目名称\n[BBOX-280] 结果\n[BBOX-281] 单位\n[BBOX-282] 参考区间\n[BBOX-283] *★红细胞\n[BBOX-284] 4.47\n[BBOX-285] x10^12/L\n[BBOX-286] 4.30-5.80\n[BBOX-287] *★白细胞\n[BBOX-288] 10.11\n[BBOX-289] ×10^9/L\n[BBOX-290] 3.50-9.50\n[BBOX-291] *★血红蛋白\n[BBOX-292] 131\n[BBOX-293] g/L\n[BBOX-294] 130-175\n[BBOX-295] 中性粒细胞百分率\n[BBOX-296] 79.3\n[BBOX-297] %\n[BBOX-298] 40.0-75.0\n[BBOX-299] *★红细胞压积\n[BBOX-300] 40.0\n[BBOX-301] %\n[BBOX-302] 40.0-50.0\n[BBOX-303] 淋巴细胞百分率\n[BBOX-304] 12.1\n[BBOX-305] %\n[BBOX-306] 20.0-50.0\n[BBOX-307] *平均红细胞体积\n[BBOX-308] 89.4\n[BBOX-309] fL\n[BBOX-310] 82.0-100.0\n[BBOX-311] 单核细胞百分率\n[BBOX-312] 7.0\n[BBOX-313] %\n[BBOX-314] 3.0-10.0\n[BBOX-315] *平均血红蛋白量\n[BBOX-316] 29.4\n[BBOX-317] pg\n[BBOX-318] 27.0-34.0\n[BBOX-319] 嗜酸细胞百分率\n[BBOX-320] 1.1\n[BBOX-321] %\n[BBOX-322] 0.4-8.0\n[BBOX-323] *平均血红蛋白浓度\n[BBOX-324] 328\n[BBOX-325] g/L\n[BBOX-326] 316-354\n[BBOX-327] 嗜碱细胞百分率\n[BBOX-328] 0.5\n[BBOX-329] %\n[BBOX-330] 0.0-1.0\n[BBOX-331] 红细胞分布宽度SD\n[BBOX-332] 48.4\n[BBOX-333] f1\n[BBOX-334] 39.0-46.0\n[BBOX-335] ↑\n[BBOX-336] 中性粒细胞绝对值\n[BBOX-337] 8.02\n[BBOX-338] ×10^9/L\n[BBOX-339] 1.80-6.30\n[BBOX-340] 红细胞分布宽度CV\n[BBOX-341] 14.8\n[BBOX-342] %\n[BBOX-343] 10.9-14.5\n[BBOX-344] ↑\n[BBOX-345] 淋巴细胞绝对值\n[BBOX-346] 1.22\n[BBOX-347] ×10^9/L\n[BBOX-348] 1.10-3.20\n[BBOX-349] *★血小板总数\n[BBOX-350] 256\n[BBOX-351] ×10^9/L\n[BBOX-352] 125-350\n[BBOX-353] 单核细胞绝对值\n[BBOX-354] 0.71\n[BBOX-355] ×10^9/L\n[BBOX-356] 0.10-0.60\n[BBOX-357] 血小板平均容积\n[BBOX-358] 8.5\n[BBOX-359] fL\n[BBOX-360] 7.6-13.2\n[BBOX-361] 嗜酸细胞绝对值\n[BBOX-362] 0.11\n[BBOX-363] ×10^9/L\n[BBOX-364] 0.02-0.52\n[BBOX-365] 血小板分布宽度\n[BBOX-366] 16.2\n[BBOX-367] f1\n[BBOX-368] 9.0-17.0\n[BBOX-369] 嗜碱细胞绝对值\n[BBOX-370] 0.05\n[BBOX-371] ×10^9/L\n[BBOX-372] 0.00-0.06\n[BBOX-373] 血小板比积\n[BBOX-374] 0.217\n[BBOX-375] %\n[BBOX-376] 0.11-0.28\n[BBOX-377] 超敏C-反应蛋白\n[BBOX-378] 28.26\n[BBOX-379] mg/L\n[BBOX-380] 0.00-6.00\n[BBOX-381] 大血小板比例\n[BBOX-382] 17.5\n[BBOX-383] %\n[BBOX-384] 13.0-43.0\n[BBOX-385] 血清淀粉样蛋白A\n[BBOX-386] 16.24\n[BBOX-387] mg/L\n[BBOX-388] 0.00-10.00\n[BBOX-389] 备注评价：\n[BBOX-390] 采集时间：2026-03-11 09:24\n[BBOX-391] 接收时间：2026-03-11 09:57\n[BBOX-392] 报告时间：2026-03-11 10:09\n[BBOX-393] \\begin{tabular}{ccccccc}\n[BBOX-394] 报告时间: 2026-03-11\n[BBOX-395] \\hline\n[BBOX-396] 序号 & 项目名称 & 项目代码 & 结果 & 单位 & 参考区间 & 提示 \\\\\n[BBOX-397] \\hline\n[BBOX-398] 1 & **总蛋白 & TP & 70.10 & g/L & 65.00-85.00 & \\\\\n[BBOX-399] 2 & **白蛋白(溴甲酚绿法) & ALB & 37.19 & g/L & 40.00-55.00 & $\\downarrow$ \\\\\n[BBOX-400] 3 & 球蛋白 & GLO & 32.91 & g/L & 20.00-40.00 & \\\\\n[BBOX-401] 4 & 白蛋白:球蛋白 & A:G & 1.13 & & 1.20-2.40 & $\\downarrow$ \\\\\n[BBOX-402] 5 & *总胆红素 & TBIL & 12.6 & $\\mu$mol/L & $\\le$26.0 & \\\\\n[BBOX-403] 6 & *直接胆红素 & DBIL & 2.2 & $\\mu$mol/L & 0.0-6.8 & \\\\\n[BBOX-404] 7 & 间接胆红素 & IBIL & 10.4 & $\\mu$mol/L & 3.0-19.0 & \\\\\n[BBOX-405] 8 & **$\\gamma$-谷氨酰基转移酶 & GGT & 25 & U/L & 10-60 & \\\\\n[BBOX-406] 9 & **碱性磷酸酶 & ALP & 93 & U/L & 45-125 & \\\\\n[BBOX-407] 10 & **天门冬氨酸氨基转移酶 & AST & 21 & U/L & 15-40 & \\\\\n[BBOX-408] 11 & **丙氨酸氨基转移酶 & ALT & 14 & U/L & 9-50 & \\\\\n[BBOX-409] 12 & AST:ALT & AST:ALT & 1.50 & & & \\\\\n[BBOX-410] 13 & 总胆汁酸 & TBA & 1.0 & $\\mu$mol/L & 0.0-14.0 & \\\\\n[BBOX-411] 14 & **钾 & K & 4.03 & mmol/L & 3.50-5.30 & \\\\\n[BBOX-412] 15 & **钠 & Na & 140.3 & mmol/L & 137.0-147.0 & \\\\\n[BBOX-413] 16 & **氯 & Cl & 103.5 & mmol/L & 99.0-110.0 & \\\\\n[BBOX-414] 17 & 总二氧化碳 & TCO2 & 25.9 & mmol/L & 21.0-30.0 & \\\\\n[BBOX-415] 18 & 阴离子隙 & ANION & 10.9 & mmol/L & 8.0-16.0 & \\\\\n[BBOX-416] \\hline\n[BBOX-417] \\end{tabular}\n[BBOX-418] \\begin{tabular}{ccccccc}\n[BBOX-419] 报告时间: 2026-03-11\n[BBOX-420] \\hline\n[BBOX-421] 序号 & 项目名称 & 项目代码 & 结果 & 单位 & 参考区间 & 提示 \\\\\n[BBOX-422] \\hline\n[BBOX-423] 19 & **钙 & Ca & 2.29 & mmol/L & 2.11-2.52 & \\\\\n[BBOX-424] 20 & **无机磷 & P & 1.09 & mmol/L & 0.85-1.51 & \\\\\n[BBOX-425] 21 & *镁 & MG & 0.85 & mmol/L & 0.75-1.02 & \\\\\n[BBOX-426] 22 & **葡萄糖 & GLU & 5.56 & mmol/L & 3.90-6.10 & \\\\\n[BBOX-427] 23 & **尿素 & UREA & 5.59 & mmol/L & 3.60-9.50 & \\\\\n[BBOX-428] 24 & **肌酐(酶法) & CREA & 71 & $\\mu$mol/L & 57-111 & \\\\\n[BBOX-429] 25 & 尿素:肌酐 & UREA:CREA & 0.08 & & & \\\\\n[BBOX-430] 26 & 肾小球滤过率 & eGFR(CKD-EPI) & 91.01 & ml/(min$\\cdot$1.73m$^2$) & $\\ge$90 & \\\\\n[BBOX-431] 27 & **尿酸 & UA & 367 & $\\mu$mol/L & 208-428 & \\\\\n[BBOX-432] 28 & **肌酸激酶 & CK & 33 & U/L & 50-310 & $\\downarrow$ \\\\\n[BBOX-433] 29 & **乳酸脱氢酶 & LDH & 192 & U/L & 120-250 & \\\\\n[BBOX-434] 30 & **总胆固醇 & CHOL & 4.41 & mmol/L & 3.12-5.72 & \\\\\n[BBOX-435] 31 & **甘油三酯 & TG & 0.84 & mmol/L & 0.40-1.70 & \\\\\n[BBOX-436] 32 & **高密度脂蛋白胆固醇 & HDL-C & 1.16 & mmol/L & 1.04-1.96 & \\\\\n[BBOX-437] 33 & **低密度脂蛋白胆固醇 & LDL-C & 2.51 & mmol/L & 1.53-3.45 & \\\\\n[BBOX-438] 34 & 非高密度脂蛋白胆固醇 & non-HDL-C & 3.25 & mmol/L & & \\\\\n[BBOX-439] 35 & *脂蛋白(a) & Lp(a) & 538 & mg/L & 0-300 & $\\uparrow$ \\\\\n[BBOX-440] 36 & 唾液酸 & SA & 803 & mg/L & 456-754 & $\\uparrow$ \\\\\n[BBOX-441] \\hline\n[BBOX-442] \\end{tabular}\n[BBOX-443] \\begin{tabular}{ccccccc}\n[BBOX-444] 报告时间: 2026-03-11\n[BBOX-445] \\hline\n[BBOX-446] 序号 & 项目名称 & 项目代码 & 结果 & 单位 & 参考区间 & 提示 \\\\\n[BBOX-447] \\hline\n[BBOX-448] 37 & 渗透压 & OSM & 281.1 & MoSM/L & & \\\\\n[BBOX-449] 38 & 血同型半胱氨酸 & HCY & 10.3 & $\\mu$mol/L & 0.0-15.0 & \\\\\n[BBOX-450] \\hline\n[BBOX-451] \\end{tabular}\n[BBOX-452] \\begin{tabular}{cccccc}\n[BBOX-453] 报告时间: 2026-03-12\n[BBOX-454] \\hline\n[BBOX-455] 项目名称 & 结果 & 单位 & 参考区间 & 提示 & \\\\\n[BBOX-456] \\hline\n[BBOX-457] 白细胞 & 2.2 & 个/ul & 0--9.2 & & \\\\\n[BBOX-458] 红细胞 & 6.7 & 个/ul & 0--13.1 & & \\\\\n[BBOX-459] 上皮细胞 & 2.5 & 个/ul & 0--5.7 & & \\\\\n[BBOX-460] 管型 & 0.00 & 个/ul & 0--2.25 & & \\\\\n[BBOX-461] 电导率 & 15.5 & ms/cm & 3.0--39.0 & & \\\\\n[BBOX-462] 白细胞(高倍视野) & 0 & 个/HPF & 0--3 & & \\\\\n[BBOX-463] 红细胞(高倍视野) & 1 & 个/HPF & 0--2 & & \\\\\n[BBOX-464] 上皮细胞(高倍视野)0 & 0 & 个/HPF & 0--5 & & \\\\\n[BBOX-465] 管型(低倍视野) & 0 & 个/LPF & 0--2 & & \\\\\n[BBOX-466] 小圆上皮细胞 & 无 & & & & \\\\\n[BBOX-467] 类酵母菌 & 无 & & & & \\\\\n[BBOX-468] 结晶 & 无 & & & & \\\\\n[BBOX-469] 红细胞形态信息 & 未提示 & & & & \\\\\n[BBOX-470] \\hline\n[BBOX-471] \\end{tabular}\n[BBOX-472] \\begin{tabular}{cccccc}\n[BBOX-473] 报告时间: 2026-03-12\n[BBOX-474] \\hline\n[BBOX-475] 项目名称 & 结果 & 参考区间 & 提示 & & \\\\\n[BBOX-476] \\hline\n[BBOX-477] *白细胞 & 阴性(-) & 阴性(-) & & & \\\\\n[BBOX-478] *隐血 & 阴性(-) & 阴性(-) & & & \\\\\n[BBOX-479] *尿蛋白 & 阴性(-) & 阴性(-) & & & \\\\\n[BBOX-480] *葡萄糖 & 阴性(-) & 阴性(-) & & & \\\\\n[BBOX-481] *胆红素 & 阴性(-) & 阴性(-) & & & \\\\\n[BBOX-482] *尿胆原 & 阴性(-) & 阴性(-) & & & \\\\\n[BBOX-483] *酸碱度 & 5.0 & 4.5--8.0 & & & \\\\\n[BBOX-484] *比重 & 1.022 & 1.003--1.030 & & & \\\\\n[BBOX-485] *亚硝酸盐 & 阴性(-) & 阴性(-) & & & \\\\\n[BBOX-486] *酮体 & 阴性(-) & 阴性(-) & & & \\\\\n[BBOX-487] 颜色 & 稻黄色 & & & & \\\\\n[BBOX-488] 浊度 & CLEAR & & & & \\\\\n[BBOX-489] \\hline\n[BBOX-490] \\end{tabular}\n[BBOX-491] \\begin{tabular}{cccccc}\n[BBOX-492] 报告时间: 2026-03-12\n[BBOX-493] \\hline\n[BBOX-494] 序号 & 项目名称 & 项目代码 & 结果 & 单位 & 参考区间 & 提示 \\\\\n[BBOX-495] \\hline\n[BBOX-496] 1 & 大便颜色 & 大便颜色 & 黄褐色 & & 黄色-黄褐色 & \\\\\n[BBOX-497] 2 & 大便性状 & 大便性状 & 软便 & & 软 & \\\\\n[BBOX-498] 3 & 白细胞 & WBC & 未见 & /HP & 无或偶见 & \\\\\n[BBOX-499] 4 & 红细胞 & RBC & 未见 & /HP & 无 & \\\\\n[BBOX-500] 5 & 巨噬细胞 & 巨噬细胞 & 未见 & 个/HP & & \\\\\n[BBOX-501] 6 & 脂肪球 & 脂肪球 & 未见 & /HP & & \\\\\n[BBOX-502] 7 & 霉菌 & 霉菌 & 未见 & /HP & 无 & \\\\\n[BBOX-503] 8 & 不消化食物 & 不消化食物 & 无 & & & \\\\\n[BBOX-504] 9 & 蛔虫卵 & 蛔虫卵 & 未见 & & & \\\\\n[BBOX-505] 10 & 鞭虫卵 & 鞭虫卵 & 未见 & & & \\\\\n[BBOX-506] 11 & 钩虫卵 & 钩虫卵 & 未见 & & & \\\\\n[BBOX-507] 12 & 蛲虫卵 & 蛲虫卵 & 未见 & & & \\\\\n[BBOX-508] 13 & 肝吸虫卵 & 肝吸虫卵 & 未见 & & & \\\\\n[BBOX-509] 14 & 带绦虫卵 & 带绦虫卵 & 未见 & & & \\\\\n[BBOX-510] 15 & 其它 & 其它 & 未见异常 & & & \\\\\n[BBOX-511] 16 & 隐血 & OB & 阴性(-) & & 阴性(-) & \\\\\n[BBOX-512] \\hline\n[BBOX-513] \\end{tabular}\n[BBOX-514] \\begin{tabular}{l}\n[BBOX-515] 报告时间: 2026-03-12\n[BBOX-516] 【检查日期】: 2026/3/11 12:07:23 \\\\\n[BBOX-517] 【检查所见】: 脑组织左右对称, 双侧额顶叶及侧脑室旁见斑点状稍长T1稍长T2信号, FLAIR像呈高信号 \\\\\n[BBOX-518] , DWI未见明显异常信号改变; 双侧基底节区见斑点状长T1长T2信号影; 增强扫描未见强化。脑室系统扩大 \\\\\n[BBOX-519] , 中线结构居中。脑沟、脑裂、脑池增宽。部分副鼻窦粘膜增厚, 左侧上颌窦内见类圆形长T2长T2信号影。 \\\\\n[BBOX-520] 右侧乳突粘膜增厚。鼻中隔偏曲, 双下鼻甲肥大。 \\\\\n[BBOX-521] 【检查诊断】: 1. 双侧额顶叶及侧脑室旁白质内脱髓鞘改变。 \\\\\n[BBOX-522] 2. 双侧基底节区软化灶形成。 \\\\\n[BBOX-523] 3. 老年脑改变, 双侧额颞部少量硬膜下积液。 \\\\\n[BBOX-524] 4. 部分副鼻窦炎, 左侧上颌窦囊肿; 右侧乳突炎。 \\\\\n[BBOX-525] 5. 鼻中隔偏曲, 双下鼻甲肥大。 \\\\\n[BBOX-526] 以上所见较2025-11-09MR变化不著。 \\\\\n[BBOX-527] 【书写医师】: \\\\\n[BBOX-528] \\end{tabular}\n[BBOX-529] 【检查日期】：2026/1/8 13:58:55\n[BBOX-530] 【检查所见】：右侧胸廓塌陷，右侧胸腔内见少量液体密度影，右肺肺组织压缩、密度增高，右肺下叶可\n[BBOX-531] 见一团块状软组织密度影，内见空洞影，增强可见轻度不均匀强化，周围伴条片状密度增高影，与远侧不张\n[BBOX-532] 肺组织分界不清，范围无法测量。右肺小叶间隔增厚。右侧胸膜不均匀增厚伴局部结节状、肿块状，增强可\n[BBOX-533] 见明显强化，邻近右前胸壁及右侧膈肌不规整。双肺内见斑片及索条影。左肺见小结节影，大者位于左肺下\n[BBOX-534] 叶（薄层img180），直径约为0.4cm。纵隔窗未见显示，增强扫描难以评估。气管及主支气管通畅。纵隔右\n[BBOX-535] 偏，纵隔及双肺门内见稍大淋巴结影，大者短径约1.1cm，增强强化欠均匀。心脏大小、形态正常，主动脉\n[BBOX-536] 壁及冠状动脉走行区可见高密度影。\n[BBOX-537] 甲状腺密度不均，内见类圆形低密度影。右侧部分肋骨内缘骨皮质增厚，右侧第7、8、9、12肋局部骨\n[BBOX-538] 质见片状高密度影。\n[BBOX-539] 【检查诊断】：对比2025-11-08CT：\n[BBOX-540] 1.右肺下叶肺癌，范围整体较前增大；右肺小叶间隔增厚，较前进展，考虑癌性淋巴管炎可能；纵隔及双肺\n[BBOX-541] 门淋巴结大致同前；考虑右侧胸膜转移，较前进展，累及邻近右前胸壁及右侧膈肌可能；请结合临床并复查\n[BBOX-542] 。\n[BBOX-543] 2.右侧胸腔积液，较前变化不著。\n[BBOX-544] 3.左肺小结节，较前相仿，建议短期复查。\n[BBOX-545] 4.右侧第7-9、12肋骨高密度影，局部略进展，转移可能，建议ECT进一步检查。\n[BBOX-546] 余所见大致同前。\n[BBOX-547] 【检查描述】：心搏次数：97(60~100) bpm，PR间隔：160 ms，QRS间隔：74 ms，QT间隔：334 ms，QTc\n[BBOX-548] 间隔：424 ms，P轴：51°，QRS轴：7°，T轴：34°\n[BBOX-549] 【检查诊断】：窦性心律\n[BBOX-550] 大致正常心电图\n[BBOX-551] 【检查时间】：2026/3/11 13:54:45\n[BBOX-552] 检查时间\n[BBOX-553] 心率\n[BBOX-554] 2026-03-11 13:54:39\n[BBOX-555] PR\n[BBOX-556] 97 bpm\n[BBOX-557] QRS\n[BBOX-558] 160 ms\n[BBOX-559] QT/QTc\n[BBOX-560] 74 ms\n[BBOX-561] P/QRS/T\n[BBOX-562] 间期\n[BBOX-563] 334 / 424 ms\n[BBOX-564] RV5+SV1\n[BBOX-565] 电轴\n[BBOX-566] 51 / 7 / 34 °\n[BBOX-567] 振幅\n[BBOX-568] /\n[BBOX-569] mV\n[BBOX-570] 0.000 mV\n[BBOX-571] AVR\n[BBOX-572] V1\n[BBOX-573] V4\n[BBOX-574] AVL\n[BBOX-575] V2\n[BBOX-576] V5\n[BBOX-577] III\n[BBOX-578] V3\n[BBOX-579] V6\n[BBOX-580] AVF\n[BBOX-581] II\n[BBOX-582] 【手术信息】：胸腔积液\n[BBOX-583] 【取材部位】：1:胸膜×1\n[BBOX-584] 2:细胞蜡块1×1\n[BBOX-585] 【取材描述】：胸膜×多\n[BBOX-586] 【大体描述】：胸膜：灰白小组织一堆，大小1*0.8*0.5cm。\n[BBOX-587] 【病理所见】：胸膜：灰白小组织一堆，大小1*0.8*0.5cm。\n[BBOX-588] 【病理诊断】：（胸膜活检）送检增生的纤维组织内见腺癌浸润，请结合临床诊治。\n[BBOX-589] 免疫组化：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（部分+）、P40（点灶+）、CR（灶+）、ALK\n[BBOX-590] （1A4）（-）、Ki67（+，40%）。\n[BBOX-591] 【报告时间】：2025/4/9 10:06:00\n[BBOX-592] 一线：培美曲塞+顺铂+信迪利单抗，二线：培美曲\n[BBOX-593] 塞+顺铂+信迪利单抗+恩度"
  }
]
2026-08-10 18:18:36,524 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:18:36,539 INFO     29 [SmartSplitter] SmartSplitter done: 10 chunks from 10 LLM segments (all bbox_id). Types: {'AdmissionRecord': 1, 'LabReport': 5, 'ExaminationReport': 4}
2026-08-10 18:18:36,548 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 18:18:36,548 INFO     29 [Trace] task=8fa8ece8 | doc=07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "594 items", "markdown": "", "text": "", "name": "07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks": "10 items, types={'AdmissionRecord': 1, 'LabReport': 5, 'ExaminationReport': 4}"}
2026-08-10 18:18:36,548 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 18:18:36,549 INFO     29 [ChunkRouter] Routed 10 chunks into 3 groups: {'chunks_Admission': 1, 'chunks_LabExam': 5, 'chunks_Examination': 4}
2026-08-10 18:18:36,557 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 18:18:36,558 INFO     29 [Trace] task=8fa8ece8 | doc=07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf | ChunkRouter:Router | outputs={"html": "", "json": "594 items", "markdown": "", "text": "", "name": "07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks": "10 items, types={'AdmissionRecord': 1, 'LabReport': 5, 'ExaminationReport': 4}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_LabExam\": 5, \"chunks_Examination\": 4}"}
2026-08-10 18:18:36,558 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 18:18:36,563 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:18:36,564 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:18:36,564 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[7]
2026-08-10 18:18:36,564 INFO     29 [qwen-vl-table] positions ： [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:18:36,817 INFO     29 [qwen-vl-table] page=7, rect=595x842, img=(1654x2339)
2026-08-10 18:18:36,817 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:18:36,817 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 275, \"bbox_end\": 392, \"encounter_dates\": [\"2026-03-11\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "项目名称\n结果\n单位\n参考范围\n项目名称\n结果\n单位\n参考区间\n*★红细胞\n4.47\nx10^12/L\n4.30-5.80\n*★白细胞\n10.11\n×10^9/L\n3.50-9.50\n*★血红蛋白\n131\ng/L\n130-175\n中性粒细胞百分率\n79.3\n%\n40.0-75.0\n*★红细胞压积\n40.0\n%\n40.0-50.0\n淋巴细胞百分率\n12.1\n%\n20.0-50.0\n*平均红细胞体积\n89.4\nfL\n82.0-100.0\n单核细胞百分率\n7.0\n%\n3.0-10.0\n*平均血红蛋白量\n29.4\npg\n27.0-34.0\n嗜酸细胞百分率\n1.1\n%\n0.4-8.0\n*平均血红蛋白浓度\n328\ng/L\n316-354\n嗜碱细胞百分率\n0.5\n%\n0.0-1.0\n红细胞分布宽度SD\n48.4\nf1\n39.0-46.0\n↑\n中性粒细胞绝对值\n8.02\n×10^9/L\n1.80-6.30\n红细胞分布宽度CV\n14.8\n%\n10.9-14.5\n↑\n淋巴细胞绝对值\n1.22\n×10^9/L\n1.10-3.20\n*★血小板总数\n256\n×10^9/L\n125-350\n单核细胞绝对值\n0.71\n×10^9/L\n0.10-0.60\n血小板平均容积\n8.5\nfL\n7.6-13.2\n嗜酸细胞绝对值\n0.11\n×10^9/L\n0.02-0.52\n血小板分布宽度\n16.2\nf1\n9.0-17.0\n嗜碱细胞绝对值\n0.05\n×10^9/L\n0.00-0.06\n血小板比积\n0.217\n%\n0.11-0.28\n超敏C-反应蛋白\n28.26\nmg/L\n0.00-6.00\n大血小板比例\n17.5\n%\n13.0-43.0\n血清淀粉样蛋白A\n16.24\nmg/L\n0.00-10.00\n备注评价：\n采集时间：2026-03-11 09:24\n接收时间：2026-03-11 09:57\n报告时间：2026-03-11 10:09",
    "role": "user"
  }
]
2026-08-10 18:18:47,651 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:18:47.650+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 86, "failed": 0, "current": {"8fa8ece894e711f1bd9827cf206dfa2d": {"id": "8fa8ece894e711f1bd9827cf206dfa2d", "doc_id": "8f6c718294e711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 16708238, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385769380, "task_type": "dataflow", "root_trace_id": "0aa1bc1a4312482d8e4b2a1774c52cc7", "root_traceparent": "00-0aa1bc1a4312482d8e4b2a1774c52cc7-ad93c0febce673ce-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:18:52,761 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:18:52,762 INFO     29 [qwen-vl-table] page=7 LLM output (len=4424):
{
  "report_date": "2026-03-11",
  "items": [
    {
      "name": "红细胞",
      "item_code": null,
      "value": "4.47",
      "unit": "x10^12/L",
      "reference_range": "4.30-5.80",
      "abnormal": false
    },
    {
      "name": "白细胞",
      "item_code": null,
      "value": "10.11",
      "unit": "×10^9/L",
      "reference_range": "3.50-9.50",
      "abnormal": true
    },
    {
      "name": "血红蛋白",
      "item_code": null,
      "value": "131",
      "unit": "g/L",
      "reference_range": "130-175",
      "abnormal": false
    },
    {
      "name": "中性粒细胞百分率",
      "item_code": null,
      "value": "79.3",
      "unit": "%",
      "reference_range": "40.0-75.0",
      "abnormal": true
    },
    {
      "name": "红细胞压积",
      "item_code": null,
      "value": "40.0",
      "unit": "%",
      "reference_range": "40.0-50.0",
      "abnormal": false
    },
    {
      "name": "淋巴细胞百分率",
      "item_code": null,
      "value": "12.1",
      "unit": "%",
      "reference_range": "20.0-50.0",
      "abnormal": true
    },
    {
      "name": "平均红细胞体积",
      "item_code": null,
      "value": "89.4",
      "unit": "fL",
      "reference_range": "82.0-100.0",
      "abnormal": false
    },
    {
      "name": "单核细胞百分率",
      "item_code": null,
      "value": "7.0",
      "unit": "%",
      "reference_range": "3.0-10.0",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白量",
      "item_code": null,
      "value": "29.4",
      "unit": "pg",
      "reference_range": "27.0-34.0",
      "abnormal": false
    },
    {
      "name": "嗜酸细胞百分率",
      "item_code": null,
      "value": "1.1",
      "unit": "%",
      "reference_range": "0.4-8.0",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白浓度",
      "item_code": null,
      "value": "328",
      "unit": "g/L",
      "reference_range": "316-354",
      "abnormal": false
    },
    {
      "name": "嗜碱细胞百分率",
      "item_code": null,
      "value": "0.5",
      "unit": "%",
      "reference_range": "0.0-1.0",
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度SD",
      "item_code": null,
      "value": "48.4",
      "unit": "fL",
      "reference_range": "39.0-46.0",
      "abnormal": true
    },
    {
      "name": "中性粒细胞绝对值",
      "item_code": null,
      "value": "8.02",
      "unit": "×10^9/L",
      "reference_range": "1.80-6.30",
      "abnormal": true
    },
    {
      "name": "红细胞分布宽度CV",
      "item_code": null,
      "value": "14.8",
      "unit": "%",
      "reference_range": "10.9-14.5",
      "abnormal": true
    },
    {
      "name": "淋巴细胞绝对值",
      "item_code": null,
      "value": "1.22",
      "unit": "×10^9/L",
      "reference_range": "1.10-3.20",
      "abnormal": false
    },
    {
      "name": "血小板总数",
      "item_code": null,
      "value": "256",
      "unit": "×10^9/L",
      "reference_range": "125-350",
      "abnormal": false
    },
    {
      "name": "单核细胞绝对值",
      "item_code": null,
      "value": "0.71",
      "unit": "×10^9/L",
      "reference_range": "0.10-0.60",
      "abnormal": true
    },
    {
      "name": "血小板平均容积",
      "item_code": null,
      "value": "8.5",
      "unit": "fL",
      "reference_range": "7.6-13.2",
      "abnormal": false
    },
    {
      "name": "嗜酸细胞绝对值",
      "item_code": null,
      "value": "0.11",
      "unit": "×10^9/L",
      "reference_range": "0.02-0.52",
      "abnormal": false
    },
    {
      "name": "血小板分布宽度",
      "item_code": null,
      "value": "16.2",
      "unit": "fL",
      "reference_range": "9.0-17.0",
      "abnormal": false
    },
    {
      "name": "嗜碱细胞绝对值",
      "item_code": null,
      "value": "0.05",
      "unit": "×10^9/L",
      "reference_range": "0.00-0.06",
      "abnormal": false
    },
    {
      "name": "血小板比积",
      "item_code": null,
      "value": "0.217",
      "unit": "%",
      "reference_range": "0.11-0.28",
      "abnormal": false
    },
    {
      "name": "超敏C-反应蛋白",
      "item_code": null,
      "value": "28.26",
      "unit": "mg/L",
      "reference_range": "0.00-6.00",
      "abnormal": true
    },
    {
      "name": "大血小板比例",
      "item_code": null,
      "value": "17.5",
      "unit": "%",
      "reference_range": "13.0-43.0",
      "abnormal": false
    },
    {
      "name": "血清淀粉样蛋白A",
      "item_code": null,
      "value": "16.24",
      "unit": "mg/L",
      "reference_range": "0.00-10.00",
      "abnormal": true
    }
  ]
}
2026-08-10 18:18:52,762 INFO     29 [qwen-vl-table] coord grouping: {7: 26}
2026-08-10 18:18:52,764 INFO     29 [qwen-vl-table] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1344314, prompt_len=705
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
红细胞、白细胞、血红蛋白、中性粒细胞百分率、红细胞压积、淋巴细胞百分率、平均红细胞体积、单核细胞百分率、平均血红蛋白量、嗜酸细胞百分率、平均血红蛋白浓度、嗜碱细胞百分率、红细胞分布宽度SD、中性粒细胞绝对值、红细胞分布宽度CV、淋巴细胞绝对值、血小板总数、单核细胞绝对值、血小板平均容积、嗜酸细胞绝对值、血小板分布宽度、嗜碱细胞绝对值、血小板比积、超敏C-反应蛋白、大血小板比例、血清淀粉样蛋白A

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
2026-08-10 18:19:00,232 INFO     29 [qwen-vl-table] coord API raw response (len=1345):
[
	{"text": "红细胞", "bbox": [177, 468, 233, 478]},
	{"text": "白细胞", "bbox": [487, 468, 542, 478]},
	{"text": "血红蛋白", "bbox": [177, 479, 244, 489]},
	{"text": "中性粒细胞百分率", "bbox": [487, 479, 584, 489]},
	{"text": "红细胞压积", "bbox": [177, 490, 256, 500]},
	{"text": "淋巴细胞百分率", "bbox": [487, 490, 573, 500]},
	{"text": "平均红细胞体积", "bbox": [177, 501, 267, 511]},
	{"text": "单核细胞百分率", "bbox": [487, 501, 573, 511]},
	{"text": "平均血红蛋白量", "bbox": [177, 512, 267, 522]},
	{"text": "嗜酸细胞百分率", "bbox": [487, 512, 573, 522]},
	{"text": "平均血红蛋白浓度", "bbox": [177, 523, 278, 533]},
	{"text": "嗜碱细胞百分率", "bbox": [487, 523, 573, 533]},
	{"text": "红细胞分布宽度SD", "bbox": [172, 534, 272, 544]},
	{"text": "中性粒细胞绝对值", "bbox": [487, 534, 584, 544]},
	{"text": "红细胞分布宽度CV", "bbox": [172, 545, 272, 555]},
	{"text": "淋巴细胞绝对值", "bbox": [487, 545, 573, 555]},
	{"text": "血小板总数", "bbox": [172, 556, 251, 566]},
	{"text": "单核细胞绝对值", "bbox": [487, 556, 573, 566]},
	{"text": "血小板平均容积", "bbox": [172, 567, 257, 577]},
	{"text": "嗜酸细胞绝对值", "bbox": [487, 567, 573, 577]},
	{"text": "血小板分布宽度", "bbox": [172, 578, 257, 588]},
	{"text": "嗜碱细胞绝对值", "bbox": [487, 578, 573, 588]},
	{"text": "血小板比积", "bbox": [172, 590, 232, 600]},
	{"text": "超敏C-反应蛋白", "bbox": [487, 590, 573, 600]},
	{"text": "大血小板比例", "bbox": [172, 601, 244, 611]},
	{"text": "血清淀粉样蛋白A", "bbox": [487, 601, 582, 611]}
]
2026-08-10 18:19:00,232 INFO     29 [qwen-vl-table] coord API: raw_items=26, valid_items=26, elapsed=7.5s
2026-08-10 18:19:00,232 INFO     29 [qwen-vl-table] coord item[0]: text=红细胞, bbox=[177, 468, 233, 478]
2026-08-10 18:19:00,232 INFO     29 [qwen-vl-table] coord item[1]: text=白细胞, bbox=[487, 468, 542, 478]
2026-08-10 18:19:00,232 INFO     29 [qwen-vl-table] coord item[2]: text=血红蛋白, bbox=[177, 479, 244, 489]
2026-08-10 18:19:00,232 INFO     29 [qwen-vl-table] coord item[3]: text=中性粒细胞百分率, bbox=[487, 479, 584, 489]
2026-08-10 18:19:00,232 INFO     29 [qwen-vl-table] coord item[4]: text=红细胞压积, bbox=[177, 490, 256, 500]
2026-08-10 18:19:00,232 INFO     29 [qwen-vl-table] coord item[5]: text=淋巴细胞百分率, bbox=[487, 490, 573, 500]
2026-08-10 18:19:00,232 INFO     29 [qwen-vl-table] coord item[6]: text=平均红细胞体积, bbox=[177, 501, 267, 511]
2026-08-10 18:19:00,232 INFO     29 [qwen-vl-table] coord item[7]: text=单核细胞百分率, bbox=[487, 501, 573, 511]
2026-08-10 18:19:00,232 INFO     29 [qwen-vl-table] coord item[8]: text=平均血红蛋白量, bbox=[177, 512, 267, 522]
2026-08-10 18:19:00,232 INFO     29 [qwen-vl-table] coord item[9]: text=嗜酸细胞百分率, bbox=[487, 512, 573, 522]
2026-08-10 18:19:00,232 INFO     29 [qwen-vl-table] coord item[10]: text=平均血红蛋白浓度, bbox=[177, 523, 278, 533]
2026-08-10 18:19:00,232 INFO     29 [qwen-vl-table] coord item[11]: text=嗜碱细胞百分率, bbox=[487, 523, 573, 533]
2026-08-10 18:19:00,232 INFO     29 [qwen-vl-table] coord item[12]: text=红细胞分布宽度SD, bbox=[172, 534, 272, 544]
2026-08-10 18:19:00,232 INFO     29 [qwen-vl-table] coord item[13]: text=中性粒细胞绝对值, bbox=[487, 534, 584, 544]
2026-08-10 18:19:00,232 INFO     29 [qwen-vl-table] coord item[14]: text=红细胞分布宽度CV, bbox=[172, 545, 272, 555]
2026-08-10 18:19:00,232 INFO     29 [qwen-vl-table] coord item[15]: text=淋巴细胞绝对值, bbox=[487, 545, 573, 555]
2026-08-10 18:19:00,232 INFO     29 [qwen-vl-table] coord item[16]: text=血小板总数, bbox=[172, 556, 251, 566]
2026-08-10 18:19:00,233 INFO     29 [qwen-vl-table] coord item[17]: text=单核细胞绝对值, bbox=[487, 556, 573, 566]
2026-08-10 18:19:00,233 INFO     29 [qwen-vl-table] coord item[18]: text=血小板平均容积, bbox=[172, 567, 257, 577]
2026-08-10 18:19:00,233 INFO     29 [qwen-vl-table] coord item[19]: text=嗜酸细胞绝对值, bbox=[487, 567, 573, 577]
2026-08-10 18:19:00,233 INFO     29 [qwen-vl-table] coord item[20]: text=血小板分布宽度, bbox=[172, 578, 257, 588]
2026-08-10 18:19:00,233 INFO     29 [qwen-vl-table] coord item[21]: text=嗜碱细胞绝对值, bbox=[487, 578, 573, 588]
2026-08-10 18:19:00,233 INFO     29 [qwen-vl-table] coord item[22]: text=血小板比积, bbox=[172, 590, 232, 600]
2026-08-10 18:19:00,233 INFO     29 [qwen-vl-table] coord item[23]: text=超敏C-反应蛋白, bbox=[487, 590, 573, 600]
2026-08-10 18:19:00,233 INFO     29 [qwen-vl-table] coord item[24]: text=大血小板比例, bbox=[172, 601, 244, 611]
2026-08-10 18:19:00,233 INFO     29 [qwen-vl-table] coord item[25]: text=血清淀粉样蛋白A, bbox=[487, 601, 582, 611]
2026-08-10 18:19:00,233 INFO     29 [qwen-vl-table] page=7 coord: matched 26/26, time=7.5s
2026-08-10 18:19:00,233 INFO     29 [qwen-vl-table] new_positions (26):
[[8, 105.36809783935547, 138.70489715576173, 394.00921142578125, 402.4282116699219], [8, 289.9110940551758, 322.65259338378905, 394.00921142578125, 402.4282116699219], [8, 105.36809783935547, 145.25319702148437, 403.270111694336, 411.6891119384766], [8, 289.9110940551758, 347.6551928710938, 403.270111694336, 411.6891119384766], [8, 105.36809783935547, 152.396796875, 412.53101196289066, 420.95001220703125], [8, 289.9110940551758, 341.1068930053711, 412.53101196289066, 420.95001220703125], [8, 105.36809783935547, 158.94509674072268, 421.79191223144534, 430.2109124755859], [8, 289.9110940551758, 341.1068930053711, 421.79191223144534, 430.2109124755859], [8, 105.36809783935547, 158.94509674072268, 431.0528125, 439.47181274414066], [8, 289.9110940551758, 341.1068930053711, 431.0528125, 439.47181274414066], [8, 105.36809783935547, 165.49339660644532, 440.3137127685547, 448.73271301269534], [8, 289.9110940551758, 341.1068930053711, 440.3137127685547, 448.73271301269534], [8, 102.39159790039064, 161.9215966796875, 449.5746130371094, 457.99361328125], [8, 289.9110940551758, 347.6551928710938, 449.5746130371094, 457.99361328125], [8, 102.39159790039064, 161.9215966796875, 458.83551330566405, 467.2545135498047], [8, 289.9110940551758, 341.1068930053711, 458.83551330566405, 467.2545135498047], [8, 102.39159790039064, 149.42029693603516, 468.0964135742188, 476.5154138183594], [8, 289.9110940551758, 341.1068930053711, 468.0964135742188, 476.5154138183594], [8, 102.39159790039064, 152.99209686279298, 477.35731384277346, 485.77631408691406], [8, 289.9110940551758, 341.1068930053711, 477.35731384277346, 485.77631408691406], [8, 102.39159790039064, 152.99209686279298, 486.61821411132814, 495.0372143554688], [8, 289.9110940551758, 341.1068930053711, 486.61821411132814, 495.0372143554688], [8, 102.39159790039064, 138.10959716796876, 496.7210144042969, 505.1400146484375], [8, 289.9110940551758, 341.1068930053711, 496.7210144042969, 505.1400146484375], [8, 102.39159790039064, 145.25319702148437, 505.9819146728516, 514.4009149169922], [8, 289.9110940551758, 346.46459289550785, 505.9819146728516, 514.4009149169922]]
2026-08-10 18:19:00,233 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=26, matched=26, pages=1, time=23.7s
2026-08-10 18:19:00,235 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:19:00,237 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:19:00,238 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[8]
2026-08-10 18:19:00,238 INFO     29 [qwen-vl-table] positions ： [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:19:00,543 INFO     29 [qwen-vl-table] page=8, rect=595x842, img=(1654x2339)
2026-08-10 18:19:00,544 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:19:00,544 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 393, \"bbox_end\": 451, \"encounter_dates\": [\"2026-03-11\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccc}\n报告时间: 2026-03-11\n\\hline\n序号 & 项目名称 & 项目代码 & 结果 & 单位 & 参考区间 & 提示 \\\\\n\\hline\n1 & **总蛋白 & TP & 70.10 & g/L & 65.00-85.00 & \\\\\n2 & **白蛋白(溴甲酚绿法) & ALB & 37.19 & g/L & 40.00-55.00 & $\\downarrow$ \\\\\n3 & 球蛋白 & GLO & 32.91 & g/L & 20.00-40.00 & \\\\\n4 & 白蛋白:球蛋白 & A:G & 1.13 & & 1.20-2.40 & $\\downarrow$ \\\\\n5 & *总胆红素 & TBIL & 12.6 & $\\mu$mol/L & $\\le$26.0 & \\\\\n6 & *直接胆红素 & DBIL & 2.2 & $\\mu$mol/L & 0.0-6.8 & \\\\\n7 & 间接胆红素 & IBIL & 10.4 & $\\mu$mol/L & 3.0-19.0 & \\\\\n8 & **$\\gamma$-谷氨酰基转移酶 & GGT & 25 & U/L & 10-60 & \\\\\n9 & **碱性磷酸酶 & ALP & 93 & U/L & 45-125 & \\\\\n10 & **天门冬氨酸氨基转移酶 & AST & 21 & U/L & 15-40 & \\\\\n11 & **丙氨酸氨基转移酶 & ALT & 14 & U/L & 9-50 & \\\\\n12 & AST:ALT & AST:ALT & 1.50 & & & \\\\\n13 & 总胆汁酸 & TBA & 1.0 & $\\mu$mol/L & 0.0-14.0 & \\\\\n14 & **钾 & K & 4.03 & mmol/L & 3.50-5.30 & \\\\\n15 & **钠 & Na & 140.3 & mmol/L & 137.0-147.0 & \\\\\n16 & **氯 & Cl & 103.5 & mmol/L & 99.0-110.0 & \\\\\n17 & 总二氧化碳 & TCO2 & 25.9 & mmol/L & 21.0-30.0 & \\\\\n18 & 阴离子隙 & ANION & 10.9 & mmol/L & 8.0-16.0 & \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{ccccccc}\n报告时间: 2026-03-11\n\\hline\n序号 & 项目名称 & 项目代码 & 结果 & 单位 & 参考区间 & 提示 \\\\\n\\hline\n19 & **钙 & Ca & 2.29 & mmol/L & 2.11-2.52 & \\\\\n20 & **无机磷 & P & 1.09 & mmol/L & 0.85-1.51 & \\\\\n21 & *镁 & MG & 0.85 & mmol/L & 0.75-1.02 & \\\\\n22 & **葡萄糖 & GLU & 5.56 & mmol/L & 3.90-6.10 & \\\\\n23 & **尿素 & UREA & 5.59 & mmol/L & 3.60-9.50 & \\\\\n24 & **肌酐(酶法) & CREA & 71 & $\\mu$mol/L & 57-111 & \\\\\n25 & 尿素:肌酐 & UREA:CREA & 0.08 & & & \\\\\n26 & 肾小球滤过率 & eGFR(CKD-EPI) & 91.01 & ml/(min$\\cdot$1.73m$^2$) & $\\ge$90 & \\\\\n27 & **尿酸 & UA & 367 & $\\mu$mol/L & 208-428 & \\\\\n28 & **肌酸激酶 & CK & 33 & U/L & 50-310 & $\\downarrow$ \\\\\n29 & **乳酸脱氢酶 & LDH & 192 & U/L & 120-250 & \\\\\n30 & **总胆固醇 & CHOL & 4.41 & mmol/L & 3.12-5.72 & \\\\\n31 & **甘油三酯 & TG & 0.84 & mmol/L & 0.40-1.70 & \\\\\n32 & **高密度脂蛋白胆固醇 & HDL-C & 1.16 & mmol/L & 1.04-1.96 & \\\\\n33 & **低密度脂蛋白胆固醇 & LDL-C & 2.51 & mmol/L & 1.53-3.45 & \\\\\n34 & 非高密度脂蛋白胆固醇 & non-HDL-C & 3.25 & mmol/L & & \\\\\n35 & *脂蛋白(a) & Lp(a) & 538 & mg/L & 0-300 & $\\uparrow$ \\\\\n36 & 唾液酸 & SA & 803 & mg/L & 456-754 & $\\uparrow$ \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{ccccccc}\n报告时间: 2026-03-11\n\\hline\n序号 & 项目名称 & 项目代码 & 结果 & 单位 & 参考区间 & 提示 \\\\\n\\hline\n37 & 渗透压 & OSM & 281.1 & MoSM/L & & \\\\\n38 & 血同型半胱氨酸 & HCY & 10.3 & $\\mu$mol/L & 0.0-15.0 & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 18:19:19,808 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:19:19.807+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 86, "failed": 0, "current": {"8fa8ece894e711f1bd9827cf206dfa2d": {"id": "8fa8ece894e711f1bd9827cf206dfa2d", "doc_id": "8f6c718294e711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 16708238, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385769380, "task_type": "dataflow", "root_trace_id": "0aa1bc1a4312482d8e4b2a1774c52cc7", "root_traceparent": "00-0aa1bc1a4312482d8e4b2a1774c52cc7-ad93c0febce673ce-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:19:23,741 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:19:23,741 INFO     29 [qwen-vl-table] page=8 LLM output (len=6455):
{
  "report_date": "2026-03-11",
  "items": [
    {
      "name": "总蛋白",
      "item_code": "TP",
      "value": "70.10",
      "unit": "g/L",
      "reference_range": "65.00-85.00",
      "abnormal": false
    },
    {
      "name": "白蛋白(溴甲酚绿法)",
      "item_code": "ALB",
      "value": "37.19",
      "unit": "g/L",
      "reference_range": "40.00-55.00",
      "abnormal": true
    },
    {
      "name": "球蛋白",
      "item_code": "GLO",
      "value": "32.91",
      "unit": "g/L",
      "reference_range": "20.00-40.00",
      "abnormal": false
    },
    {
      "name": "白蛋白:球蛋白",
      "item_code": "A:G",
      "value": "1.13",
      "unit": null,
      "reference_range": "1.20-2.40",
      "abnormal": true
    },
    {
      "name": "总胆红素",
      "item_code": "TBIL",
      "value": "12.6",
      "unit": "μmol/L",
      "reference_range": "≤26.0",
      "abnormal": false
    },
    {
      "name": "直接胆红素",
      "item_code": "DBIL",
      "value": "2.2",
      "unit": "μmol/L",
      "reference_range": "0.0-6.8",
      "abnormal": false
    },
    {
      "name": "间接胆红素",
      "item_code": "IBIL",
      "value": "10.4",
      "unit": "μmol/L",
      "reference_range": "3.0-19.0",
      "abnormal": false
    },
    {
      "name": "γ-谷氨酰基转移酶",
      "item_code": "GGT",
      "value": "25",
      "unit": "U/L",
      "reference_range": "10-60",
      "abnormal": false
    },
    {
      "name": "碱性磷酸酶",
      "item_code": "ALP",
      "value": "93",
      "unit": "U/L",
      "reference_range": "45-125",
      "abnormal": false
    },
    {
      "name": "天门冬氨酸氨基转移酶",
      "item_code": "AST",
      "value": "21",
      "unit": "U/L",
      "reference_range": "15-40",
      "abnormal": false
    },
    {
      "name": "丙氨酸氨基转移酶",
      "item_code": "ALT",
      "value": "14",
      "unit": "U/L",
      "reference_range": "9-50",
      "abnormal": false
    },
    {
      "name": "AST:ALT",
      "item_code": "AST:ALT",
      "value": "1.50",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "总胆汁酸",
      "item_code": "TBA",
      "value": "1.0",
      "unit": "μmol/L",
      "reference_range": "0.0-14.0",
      "abnormal": false
    },
    {
      "name": "钾",
      "item_code": "K",
      "value": "4.03",
      "unit": "mmol/L",
      "reference_range": "3.50-5.30",
      "abnormal": false
    },
    {
      "name": "钠",
      "item_code": "Na",
      "value": "140.3",
      "unit": "mmol/L",
      "reference_range": "137.0-147.0",
      "abnormal": false
    },
    {
      "name": "氯",
      "item_code": "Cl",
      "value": "103.5",
      "unit": "mmol/L",
      "reference_range": "99.0-110.0",
      "abnormal": false
    },
    {
      "name": "总二氧化碳",
      "item_code": "TCO2",
      "value": "25.9",
      "unit": "mmol/L",
      "reference_range": "21.0-30.0",
      "abnormal": false
    },
    {
      "name": "阴离子隙",
      "item_code": "ANION",
      "value": "10.9",
      "unit": "mmol/L",
      "reference_range": "8.0-16.0",
      "abnormal": false
    },
    {
      "name": "钙",
      "item_code": "Ca",
      "value": "2.29",
      "unit": "mmol/L",
      "reference_range": "2.11-2.52",
      "abnormal": false
    },
    {
      "name": "无机磷",
      "item_code": "P",
      "value": "1.09",
      "unit": "mmol/L",
      "reference_range": "0.85-1.51",
      "abnormal": false
    },
    {
      "name": "镁",
      "item_code": "MG",
      "value": "0.85",
      "unit": "mmol/L",
      "reference_range": "0.75-1.02",
      "abnormal": false
    },
    {
      "name": "葡萄糖",
      "item_code": "GLU",
      "value": "5.56",
      "unit": "mmol/L",
      "reference_range": "3.90-6.10",
      "abnormal": false
    },
    {
      "name": "尿素",
      "item_code": "UREA",
      "value": "5.59",
      "unit": "mmol/L",
      "reference_range": "3.60-9.50",
      "abnormal": false
    },
    {
      "name": "肌酐(酶法)",
      "item_code": "CREA",
      "value": "71",
      "unit": "μmol/L",
      "reference_range": "57-111",
      "abnormal": false
    },
    {
      "name": "尿素:肌酐",
      "item_code": "UREA:CREA",
      "value": "0.08",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "肾小球滤过率",
      "item_code": "eGFR(CKD-EPI)",
      "value": "91.01",
      "unit": "ml/(min·1.73m^2)",
      "reference_range": "≥90",
      "abnormal": false
    },
    {
      "name": "尿酸",
      "item_code": "UA",
      "value": "367",
      "unit": "μmol/L",
      "reference_range": "208-428",
      "abnormal": false
    },
    {
      "name": "肌酸激酶",
      "item_code": "CK",
      "value": "33",
      "unit": "U/L",
      "reference_range": "50-310",
      "abnormal": true
    },
    {
      "name": "乳酸脱氢酶",
      "item_code": "LDH",
      "value": "192",
      "unit": "U/L",
      "reference_range": "120-250",
      "abnormal": false
    },
    {
      "name": "总胆固醇",
      "item_code": "CHOL",
      "value": "4.41",
      "unit": "mmol/L",
      "reference_range": "3.12-5.72",
      "abnormal": false
    },
    {
      "name": "甘油三酯",
      "item_code": "TG",
      "value": "0.84",
      "unit": "mmol/L",
      "reference_range": "0.40-1.70",
      "abnormal": false
    },
    {
      "name": "高密度脂蛋白胆固醇",
      "item_code": "HDL-C",
      "value": "1.16",
      "unit": "mmol/L",
      "reference_range": "1.04-1.96",
      "abnormal": false
    },
    {
      "name": "低密度脂蛋白胆固醇",
      "item_code": "LDL-C",
      "value": "2.51",
      "unit": "mmol/L",
      "reference_range": "1.53-3.45",
      "abnormal": false
    },
    {
      "name": "非高密度脂蛋白胆固醇",
      "item_code": "non-HDL-C",
      "value": "3.25",
      "unit": "mmol/L",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "脂蛋白(a)",
      "item_code": "Lp(a)",
      "value": "538",
      "unit": "mg/L",
      "reference_range": "0-300",
      "abnormal": true
    },
    {
      "name": "唾液酸",
      "item_code": "SA",
      "value": "803",
      "unit": "mg/L",
      "reference_range": "456-754",
      "abnormal": true
    },
    {
      "name": "渗透压",
      "item_code": "OSM",
      "value": "281.1",
      "unit": "MoSM/L",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "血同型半胱氨酸",
      "item_code": "HCY",
      "value": "10.3",
      "unit": "μmol/L",
      "reference_range": "0.0-15.0",
      "abnormal": false
    }
  ]
}
2026-08-10 18:19:23,741 INFO     29 [qwen-vl-table] coord grouping: {8: 38}
2026-08-10 18:19:23,744 INFO     29 [qwen-vl-table] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1671054, prompt_len=729
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
总蛋白、白蛋白(溴甲酚绿法)、球蛋白、白蛋白:球蛋白、总胆红素、直接胆红素、间接胆红素、γ-谷氨酰基转移酶、碱性磷酸酶、天门冬氨酸氨基转移酶、丙氨酸氨基转移酶、AST:ALT、总胆汁酸、钾、钠、氯、总二氧化碳、阴离子隙、钙、无机磷、镁、葡萄糖、尿素、肌酐(酶法)、尿素:肌酐、肾小球滤过率、尿酸、肌酸激酶、乳酸脱氢酶、总胆固醇、甘油三酯、高密度脂蛋白胆固醇、低密度脂蛋白胆固醇、非高密度脂蛋白胆固醇、脂蛋白(a)、唾液酸、渗透压、血同型半胱氨酸

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
2026-08-10 18:19:33,582 INFO     29 [qwen-vl-table] coord API raw response (len=1897):
[
	{"text": "总蛋白", "bbox": [224, 107, 274, 115]},
	{"text": "白蛋白(溴甲酚绿法)", "bbox": [224, 116, 338, 124]},
	{"text": "球蛋白", "bbox": [224, 126, 256, 134]},
	{"text": "白蛋白:球蛋白", "bbox": [224, 136, 294, 144]},
	{"text": "总胆红素", "bbox": [224, 146, 269, 154]},
	{"text": "直接胆红素", "bbox": [224, 156, 280, 164]},
	{"text": "间接胆红素", "bbox": [224, 166, 274, 174]},
	{"text": "γ-谷氨酰基转移酶", "bbox": [224, 176, 330, 184]},
	{"text": "碱性磷酸酶", "bbox": [224, 187, 290, 195]},
	{"text": "天门冬氨酸氨基转移酶", "bbox": [224, 197, 347, 205]},
	{"text": "丙氨酸氨基转移酶", "bbox": [224, 207, 323, 215]},
	{"text": "AST:ALT", "bbox": [214, 218, 254, 226]},
	{"text": "总胆汁酸", "bbox": [214, 228, 258, 237]},
	{"text": "钾", "bbox": [214, 239, 240, 247]},
	{"text": "钠", "bbox": [214, 250, 240, 258]},
	{"text": "氯", "bbox": [214, 261, 239, 269]},
	{"text": "总二氧化碳", "bbox": [214, 272, 266, 280]},
	{"text": "阴离子隙", "bbox": [214, 283, 254, 291]},
	{"text": "钙", "bbox": [220, 362, 247, 370]},
	{"text": "无机磷", "bbox": [220, 372, 267, 380]},
	{"text": "镁", "bbox": [220, 382, 234, 390]},
	{"text": "葡萄糖", "bbox": [220, 393, 265, 401]},
	{"text": "尿素", "bbox": [220, 403, 253, 411]},
	{"text": "肌酐(酶法)", "bbox": [220, 413, 283, 421]},
	{"text": "尿素:肌酐", "bbox": [214, 424, 261, 432]},
	{"text": "肾小球滤过率", "bbox": [214, 434, 276, 442]},
	{"text": "尿酸", "bbox": [214, 444, 249, 452]},
	{"text": "肌酸激酶", "bbox": [214, 455, 269, 463]},
	{"text": "乳酸脱氢酶", "bbox": [214, 465, 280, 473]},
	{"text": "总胆固醇", "bbox": [214, 476, 269, 484]},
	{"text": "甘油三酯", "bbox": [214, 486, 267, 494]},
	{"text": "高密度脂蛋白胆固醇", "bbox": [214, 497, 324, 505]},
	{"text": "低密度脂蛋白胆固醇", "bbox": [214, 507, 324, 515]},
	{"text": "非高密度脂蛋白胆固醇", "bbox": [205, 517, 317, 525]},
	{"text": "脂蛋白(a)", "bbox": [205, 528, 257, 536]},
	{"text": "唾液酸", "bbox": [205, 539, 236, 547]},
	{"text": "渗透压", "bbox": [225, 627, 258, 635]},
	{"text": "血同型半胱氨酸", "bbox": [225, 637, 301, 645]}
]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord API: raw_items=38, valid_items=38, elapsed=9.8s
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[0]: text=总蛋白, bbox=[224, 107, 274, 115]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[1]: text=白蛋白(溴甲酚绿法), bbox=[224, 116, 338, 124]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[2]: text=球蛋白, bbox=[224, 126, 256, 134]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[3]: text=白蛋白:球蛋白, bbox=[224, 136, 294, 144]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[4]: text=总胆红素, bbox=[224, 146, 269, 154]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[5]: text=直接胆红素, bbox=[224, 156, 280, 164]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[6]: text=间接胆红素, bbox=[224, 166, 274, 174]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[7]: text=γ-谷氨酰基转移酶, bbox=[224, 176, 330, 184]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[8]: text=碱性磷酸酶, bbox=[224, 187, 290, 195]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[9]: text=天门冬氨酸氨基转移酶, bbox=[224, 197, 347, 205]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[10]: text=丙氨酸氨基转移酶, bbox=[224, 207, 323, 215]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[11]: text=AST:ALT, bbox=[214, 218, 254, 226]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[12]: text=总胆汁酸, bbox=[214, 228, 258, 237]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[13]: text=钾, bbox=[214, 239, 240, 247]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[14]: text=钠, bbox=[214, 250, 240, 258]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[15]: text=氯, bbox=[214, 261, 239, 269]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[16]: text=总二氧化碳, bbox=[214, 272, 266, 280]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[17]: text=阴离子隙, bbox=[214, 283, 254, 291]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[18]: text=钙, bbox=[220, 362, 247, 370]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[19]: text=无机磷, bbox=[220, 372, 267, 380]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[20]: text=镁, bbox=[220, 382, 234, 390]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[21]: text=葡萄糖, bbox=[220, 393, 265, 401]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[22]: text=尿素, bbox=[220, 403, 253, 411]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[23]: text=肌酐(酶法), bbox=[220, 413, 283, 421]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[24]: text=尿素:肌酐, bbox=[214, 424, 261, 432]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[25]: text=肾小球滤过率, bbox=[214, 434, 276, 442]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[26]: text=尿酸, bbox=[214, 444, 249, 452]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[27]: text=肌酸激酶, bbox=[214, 455, 269, 463]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[28]: text=乳酸脱氢酶, bbox=[214, 465, 280, 473]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[29]: text=总胆固醇, bbox=[214, 476, 269, 484]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[30]: text=甘油三酯, bbox=[214, 486, 267, 494]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[31]: text=高密度脂蛋白胆固醇, bbox=[214, 497, 324, 505]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[32]: text=低密度脂蛋白胆固醇, bbox=[214, 507, 324, 515]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[33]: text=非高密度脂蛋白胆固醇, bbox=[205, 517, 317, 525]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[34]: text=脂蛋白(a), bbox=[205, 528, 257, 536]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[35]: text=唾液酸, bbox=[205, 539, 236, 547]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[36]: text=渗透压, bbox=[225, 627, 258, 635]
2026-08-10 18:19:33,583 INFO     29 [qwen-vl-table] coord item[37]: text=血同型半胱氨酸, bbox=[225, 637, 301, 645]
2026-08-10 18:19:33,584 INFO     29 [qwen-vl-table] page=8 coord: matched 38/38, time=9.8s
2026-08-10 18:19:33,584 INFO     29 [qwen-vl-table] new_positions (38):
[[9, 133.347197265625, 163.11219665527344, 90.08330261230469, 96.8185028076172], [9, 133.347197265625, 201.21139587402345, 97.66040283203125, 104.39560302734375], [9, 133.347197265625, 152.396796875, 106.07940307617189, 112.81460327148437], [9, 133.347197265625, 175.01819641113283, 114.4984033203125, 121.233603515625], [9, 133.347197265625, 160.1356967163086, 122.91740356445312, 129.65260375976564], [9, 133.347197265625, 166.68399658203126, 131.33640380859376, 138.07160400390626], [9, 133.347197265625, 163.11219665527344, 139.75540405273438, 146.49060424804688], [9, 133.347197265625, 196.4489959716797, 148.174404296875, 154.9096044921875], [9, 133.347197265625, 172.63699645996095, 157.4353045654297, 164.1705047607422], [9, 133.347197265625, 206.56909576416015, 165.85430480957032, 172.58950500488282], [9, 133.347197265625, 192.2818960571289, 174.27330505371094, 181.00850524902344], [9, 127.39419738769531, 151.20619689941407, 183.53420532226562, 190.26940551757812], [9, 127.39419738769531, 153.58739685058595, 191.95320556640627, 199.53030578613283], [9, 127.39419738769531, 142.87199707031252, 201.21410583496095, 207.94930603027345], [9, 127.39419738769531, 142.87199707031252, 210.47500610351562, 217.21020629882813], [9, 127.39419738769531, 142.27669708251955, 219.73590637207033, 226.47110656738283], [9, 127.39419738769531, 158.3497967529297, 228.996806640625, 235.7320068359375], [9, 127.39419738769531, 151.20619689941407, 238.2577069091797, 244.9929071044922], [9, 130.96599731445312, 147.03909698486328, 304.76780883789064, 311.5030090332031], [9, 130.96599731445312, 158.94509674072268, 313.1868090820313, 319.92200927734376], [9, 130.96599731445312, 139.3001971435547, 321.6058093261719, 328.3410095214844], [9, 130.96599731445312, 157.75449676513674, 330.86670959472656, 337.6019097900391], [9, 130.96599731445312, 150.6108969116211, 339.2857098388672, 346.0209100341797], [9, 130.96599731445312, 168.46989654541017, 347.70471008300785, 354.4399102783203], [9, 127.39419738769531, 155.37329681396486, 356.96561035156253, 363.700810546875], [9, 127.39419738769531, 164.30279663085938, 365.3846105957031, 372.11981079101565], [9, 127.39419738769531, 148.22969696044922, 373.80361083984377, 380.53881103515624], [9, 127.39419738769531, 160.1356967163086, 383.06451110839845, 389.799711303711], [9, 127.39419738769531, 166.68399658203126, 391.4835113525391, 398.21871154785157], [9, 127.39419738769531, 160.1356967163086, 400.7444116210938, 407.47961181640625], [9, 127.39419738769531, 158.94509674072268, 409.16341186523437, 415.8986120605469], [9, 127.39419738769531, 192.87719604492187, 418.4243121337891, 425.1595123291016], [9, 127.39419738769531, 192.87719604492187, 426.8433123779297, 433.5785125732422], [9, 122.0364974975586, 188.7100961303711, 435.26231262207034, 441.9975128173828], [9, 122.0364974975586, 152.99209686279298, 444.523212890625, 451.2584130859375], [9, 122.0364974975586, 140.49079711914064, 453.7841131591797, 460.5193133544922], [9, 133.94249725341797, 153.58739685058595, 527.8713153076172, 534.6065155029297], [9, 133.94249725341797, 179.1852963256836, 536.2903155517579, 543.0255157470704]]
2026-08-10 18:19:33,584 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=38, matched=38, pages=1, time=33.3s
2026-08-10 18:19:33,585 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:19:33,587 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:19:33,587 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[9]
2026-08-10 18:19:33,587 INFO     29 [qwen-vl-table] positions ： [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:19:33,848 INFO     29 [qwen-vl-table] page=9, rect=595x842, img=(1654x2339)
2026-08-10 18:19:33,849 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:19:33,849 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 452, \"bbox_end\": 471, \"encounter_dates\": [\"2026-03-12\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccccc}\n报告时间: 2026-03-12\n\\hline\n项目名称 & 结果 & 单位 & 参考区间 & 提示 & \\\\\n\\hline\n白细胞 & 2.2 & 个/ul & 0--9.2 & & \\\\\n红细胞 & 6.7 & 个/ul & 0--13.1 & & \\\\\n上皮细胞 & 2.5 & 个/ul & 0--5.7 & & \\\\\n管型 & 0.00 & 个/ul & 0--2.25 & & \\\\\n电导率 & 15.5 & ms/cm & 3.0--39.0 & & \\\\\n白细胞(高倍视野) & 0 & 个/HPF & 0--3 & & \\\\\n红细胞(高倍视野) & 1 & 个/HPF & 0--2 & & \\\\\n上皮细胞(高倍视野)0 & 0 & 个/HPF & 0--5 & & \\\\\n管型(低倍视野) & 0 & 个/LPF & 0--2 & & \\\\\n小圆上皮细胞 & 无 & & & & \\\\\n类酵母菌 & 无 & & & & \\\\\n结晶 & 无 & & & & \\\\\n红细胞形态信息 & 未提示 & & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 18:19:40,648 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:19:40,649 INFO     29 [qwen-vl-table] page=9 LLM output (len=2153):
{
  "report_date": "2026-03-12",
  "items": [
    {
      "name": "白细胞",
      "item_code": null,
      "value": "2.2",
      "unit": "个/ul",
      "reference_range": "0--9.2",
      "abnormal": false
    },
    {
      "name": "红细胞",
      "item_code": null,
      "value": "6.7",
      "unit": "个/ul",
      "reference_range": "0--13.1",
      "abnormal": false
    },
    {
      "name": "上皮细胞",
      "item_code": null,
      "value": "2.5",
      "unit": "个/ul",
      "reference_range": "0--5.7",
      "abnormal": false
    },
    {
      "name": "管型",
      "item_code": null,
      "value": "0.00",
      "unit": "个/ul",
      "reference_range": "0--2.25",
      "abnormal": false
    },
    {
      "name": "电导率",
      "item_code": null,
      "value": "15.5",
      "unit": "ms/cm",
      "reference_range": "3.0--39.0",
      "abnormal": false
    },
    {
      "name": "白细胞(高倍视野)",
      "item_code": null,
      "value": "0",
      "unit": "个/HPF",
      "reference_range": "0--3",
      "abnormal": false
    },
    {
      "name": "红细胞(高倍视野)",
      "item_code": null,
      "value": "1",
      "unit": "个/HPF",
      "reference_range": "0--2",
      "abnormal": false
    },
    {
      "name": "上皮细胞(高倍视野)",
      "item_code": null,
      "value": "0",
      "unit": "个/HPF",
      "reference_range": "0--5",
      "abnormal": false
    },
    {
      "name": "管型(低倍视野)",
      "item_code": null,
      "value": "0",
      "unit": "个/LPF",
      "reference_range": "0--2",
      "abnormal": false
    },
    {
      "name": "小圆上皮细胞",
      "item_code": null,
      "value": "无",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "类酵母菌",
      "item_code": null,
      "value": "无",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "结晶",
      "item_code": null,
      "value": "无",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "红细胞形态信息",
      "item_code": null,
      "value": "未提示",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 18:19:40,649 INFO     29 [qwen-vl-table] coord grouping: {9: 13}
2026-08-10 18:19:40,657 INFO     29 [qwen-vl-table] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2085553, prompt_len=589
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞、红细胞、上皮细胞、管型、电导率、白细胞(高倍视野)、红细胞(高倍视野)、上皮细胞(高倍视野)、管型(低倍视野)、小圆上皮细胞、类酵母菌、结晶、红细胞形态信息

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
2026-08-10 18:19:45,010 INFO     29 [qwen-vl-table] coord API raw response (len=669):
```json
[
	{"text": "白细胞", "bbox": [175, 114, 212, 123]},
	{"text": "红细胞", "bbox": [175, 125, 210, 134]},
	{"text": "上皮细胞", "bbox": [175, 136, 220, 145]},
	{"text": "管型", "bbox": [175, 147, 199, 156]},
	{"text": "电导率", "bbox": [175, 157, 207, 166]},
	{"text": "白细胞(高倍视野)", "bbox": [172, 167, 265, 176]},
	{"text": "红细胞(高倍视野)", "bbox": [172, 178, 265, 187]},
	{"text": "上皮细胞(高倍视野)", "bbox": [172, 189, 284, 198]},
	{"text": "管型(低倍视野)", "bbox": [170, 199, 250, 209]},
	{"text": "小圆上皮细胞", "bbox": [170, 210, 240, 220]},
	{"text": "类酵母菌", "bbox": [168, 221, 215, 231]},
	{"text": "结晶", "bbox": [167, 233, 190, 242]},
	{"text": "红细胞形态信息", "bbox": [167, 244, 250, 253]}
]
```
2026-08-10 18:19:45,011 INFO     29 [qwen-vl-table] coord API: raw_items=13, valid_items=13, elapsed=4.4s
2026-08-10 18:19:45,011 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞, bbox=[175, 114, 212, 123]
2026-08-10 18:19:45,011 INFO     29 [qwen-vl-table] coord item[1]: text=红细胞, bbox=[175, 125, 210, 134]
2026-08-10 18:19:45,011 INFO     29 [qwen-vl-table] coord item[2]: text=上皮细胞, bbox=[175, 136, 220, 145]
2026-08-10 18:19:45,011 INFO     29 [qwen-vl-table] coord item[3]: text=管型, bbox=[175, 147, 199, 156]
2026-08-10 18:19:45,011 INFO     29 [qwen-vl-table] coord item[4]: text=电导率, bbox=[175, 157, 207, 166]
2026-08-10 18:19:45,011 INFO     29 [qwen-vl-table] coord item[5]: text=白细胞(高倍视野), bbox=[172, 167, 265, 176]
2026-08-10 18:19:45,011 INFO     29 [qwen-vl-table] coord item[6]: text=红细胞(高倍视野), bbox=[172, 178, 265, 187]
2026-08-10 18:19:45,011 INFO     29 [qwen-vl-table] coord item[7]: text=上皮细胞(高倍视野), bbox=[172, 189, 284, 198]
2026-08-10 18:19:45,012 INFO     29 [qwen-vl-table] coord item[8]: text=管型(低倍视野), bbox=[170, 199, 250, 209]
2026-08-10 18:19:45,012 INFO     29 [qwen-vl-table] coord item[9]: text=小圆上皮细胞, bbox=[170, 210, 240, 220]
2026-08-10 18:19:45,012 INFO     29 [qwen-vl-table] coord item[10]: text=类酵母菌, bbox=[168, 221, 215, 231]
2026-08-10 18:19:45,012 INFO     29 [qwen-vl-table] coord item[11]: text=结晶, bbox=[167, 233, 190, 242]
2026-08-10 18:19:45,012 INFO     29 [qwen-vl-table] coord item[12]: text=红细胞形态信息, bbox=[167, 244, 250, 253]
2026-08-10 18:19:45,013 INFO     29 [qwen-vl-table] page=9 coord: matched 13/13, time=4.4s
2026-08-10 18:19:45,014 INFO     29 [qwen-vl-table] new_positions (13):
[[10, 104.17749786376953, 126.20359741210937, 95.97660278320313, 103.5537030029297], [10, 104.17749786376953, 125.01299743652345, 105.23750305175781, 112.81460327148437], [10, 104.17749786376953, 130.96599731445312, 114.4984033203125, 122.07550354003907], [10, 104.17749786376953, 118.46469757080078, 123.7593035888672, 131.33640380859376], [10, 104.17749786376953, 123.22709747314454, 132.17830383300782, 139.75540405273438], [10, 102.39159790039064, 157.75449676513674, 140.59730407714844, 148.174404296875], [10, 102.39159790039064, 157.75449676513674, 149.85820434570314, 157.4353045654297], [10, 102.39159790039064, 169.06519653320314, 159.11910461425782, 166.69620483398438], [10, 101.2009979248047, 148.8249969482422, 167.53810485839844, 175.95710510253906], [10, 101.2009979248047, 142.87199707031252, 176.79900512695312, 185.21800537109377], [10, 100.01039794921876, 127.98949737548828, 186.05990539550783, 194.47890563964845], [10, 99.41509796142579, 113.10699768066407, 196.16270568847656, 203.73980590820312], [10, 99.41509796142579, 148.8249969482422, 205.42360595703127, 213.00070617675783]]
2026-08-10 18:19:45,014 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=13, matched=13, pages=1, time=11.4s
2026-08-10 18:19:45,016 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:19:45,018 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:19:45,018 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[9]
2026-08-10 18:19:45,018 INFO     29 [qwen-vl-table] positions ： [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:19:45,284 INFO     29 [qwen-vl-table] page=9, rect=595x842, img=(1654x2339)
2026-08-10 18:19:45,284 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:19:45,285 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 472, \"bbox_end\": 490, \"encounter_dates\": [\"2026-03-12\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccccc}\n报告时间: 2026-03-12\n\\hline\n项目名称 & 结果 & 参考区间 & 提示 & & \\\\\n\\hline\n*白细胞 & 阴性(-) & 阴性(-) & & & \\\\\n*隐血 & 阴性(-) & 阴性(-) & & & \\\\\n*尿蛋白 & 阴性(-) & 阴性(-) & & & \\\\\n*葡萄糖 & 阴性(-) & 阴性(-) & & & \\\\\n*胆红素 & 阴性(-) & 阴性(-) & & & \\\\\n*尿胆原 & 阴性(-) & 阴性(-) & & & \\\\\n*酸碱度 & 5.0 & 4.5--8.0 & & & \\\\\n*比重 & 1.022 & 1.003--1.030 & & & \\\\\n*亚硝酸盐 & 阴性(-) & 阴性(-) & & & \\\\\n*酮体 & 阴性(-) & 阴性(-) & & & \\\\\n颜色 & 稻黄色 & & & & \\\\\n浊度 & CLEAR & & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 18:19:51,948 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:19:51.945+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 86, "failed": 0, "current": {"8fa8ece894e711f1bd9827cf206dfa2d": {"id": "8fa8ece894e711f1bd9827cf206dfa2d", "doc_id": "8f6c718294e711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 16708238, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385769380, "task_type": "dataflow", "root_trace_id": "0aa1bc1a4312482d8e4b2a1774c52cc7", "root_traceparent": "00-0aa1bc1a4312482d8e4b2a1774c52cc7-ad93c0febce673ce-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:19:52,974 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:19:52,974 INFO     29 [qwen-vl-table] page=9 LLM output (len=1988):
{
  "report_date": "2026-03-12",
  "items": [
    {
      "name": "*白细胞",
      "item_code": null,
      "value": "阴性(-)",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": false
    },
    {
      "name": "*隐血",
      "item_code": null,
      "value": "阴性(-)",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": false
    },
    {
      "name": "*尿蛋白",
      "item_code": null,
      "value": "阴性(-)",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": false
    },
    {
      "name": "*葡萄糖",
      "item_code": null,
      "value": "阴性(-)",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": false
    },
    {
      "name": "*胆红素",
      "item_code": null,
      "value": "阴性(-)",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": false
    },
    {
      "name": "*尿胆原",
      "item_code": null,
      "value": "阴性(-)",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": false
    },
    {
      "name": "*酸碱度",
      "item_code": null,
      "value": "5.0",
      "unit": null,
      "reference_range": "4.5--8.0",
      "abnormal": false
    },
    {
      "name": "*比重",
      "item_code": null,
      "value": "1.022",
      "unit": null,
      "reference_range": "1.003--1.030",
      "abnormal": false
    },
    {
      "name": "*亚硝酸盐",
      "item_code": null,
      "value": "阴性(-)",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": false
    },
    {
      "name": "*酮体",
      "item_code": null,
      "value": "阴性(-)",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": false
    },
    {
      "name": "颜色",
      "item_code": null,
      "value": "稻黄色",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "浊度",
      "item_code": null,
      "value": "CLEAR",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 18:19:52,974 INFO     29 [qwen-vl-table] coord grouping: {9: 12}
2026-08-10 18:19:52,980 INFO     29 [qwen-vl-table] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2085553, prompt_len=560
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
*白细胞、*隐血、*尿蛋白、*葡萄糖、*胆红素、*尿胆原、*酸碱度、*比重、*亚硝酸盐、*酮体、颜色、浊度

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
2026-08-10 18:19:56,012 INFO     29 [qwen-vl-table] coord API raw response (len=584):
[
	{"text": "*白细胞", "bbox": [514, 115, 552, 124]},
	{"text": "*隐血", "bbox": [514, 125, 541, 134]},
	{"text": "*尿蛋白", "bbox": [514, 135, 552, 144]},
	{"text": "*葡萄糖", "bbox": [514, 145, 552, 154]},
	{"text": "*胆红素", "bbox": [514, 155, 552, 164]},
	{"text": "*尿胆原", "bbox": [514, 165, 552, 174]},
	{"text": "*酸碱度", "bbox": [514, 175, 552, 184]},
	{"text": "*比重", "bbox": [514, 185, 541, 194]},
	{"text": "*亚硝酸盐", "bbox": [514, 195, 563, 204]},
	{"text": "*酮体", "bbox": [514, 205, 541, 214]},
	{"text": "颜色", "bbox": [514, 215, 537, 224]},
	{"text": "浊度", "bbox": [514, 225, 537, 234]}
]
2026-08-10 18:19:56,012 INFO     29 [qwen-vl-table] coord API: raw_items=12, valid_items=12, elapsed=3.0s
2026-08-10 18:19:56,012 INFO     29 [qwen-vl-table] coord item[0]: text=*白细胞, bbox=[514, 115, 552, 124]
2026-08-10 18:19:56,012 INFO     29 [qwen-vl-table] coord item[1]: text=*隐血, bbox=[514, 125, 541, 134]
2026-08-10 18:19:56,012 INFO     29 [qwen-vl-table] coord item[2]: text=*尿蛋白, bbox=[514, 135, 552, 144]
2026-08-10 18:19:56,012 INFO     29 [qwen-vl-table] coord item[3]: text=*葡萄糖, bbox=[514, 145, 552, 154]
2026-08-10 18:19:56,012 INFO     29 [qwen-vl-table] coord item[4]: text=*胆红素, bbox=[514, 155, 552, 164]
2026-08-10 18:19:56,012 INFO     29 [qwen-vl-table] coord item[5]: text=*尿胆原, bbox=[514, 165, 552, 174]
2026-08-10 18:19:56,012 INFO     29 [qwen-vl-table] coord item[6]: text=*酸碱度, bbox=[514, 175, 552, 184]
2026-08-10 18:19:56,012 INFO     29 [qwen-vl-table] coord item[7]: text=*比重, bbox=[514, 185, 541, 194]
2026-08-10 18:19:56,012 INFO     29 [qwen-vl-table] coord item[8]: text=*亚硝酸盐, bbox=[514, 195, 563, 204]
2026-08-10 18:19:56,012 INFO     29 [qwen-vl-table] coord item[9]: text=*酮体, bbox=[514, 205, 541, 214]
2026-08-10 18:19:56,012 INFO     29 [qwen-vl-table] coord item[10]: text=颜色, bbox=[514, 215, 537, 224]
2026-08-10 18:19:56,012 INFO     29 [qwen-vl-table] coord item[11]: text=浊度, bbox=[514, 225, 537, 234]
2026-08-10 18:19:56,012 INFO     29 [qwen-vl-table] page=9 coord: matched 12/12, time=3.0s
2026-08-10 18:19:56,013 INFO     29 [qwen-vl-table] new_positions (12):
[[10, 305.98419372558595, 328.60559326171875, 96.8185028076172, 104.39560302734375], [10, 305.98419372558595, 322.0572933959961, 105.23750305175781, 112.81460327148437], [10, 305.98419372558595, 328.60559326171875, 113.65650329589845, 121.233603515625], [10, 305.98419372558595, 328.60559326171875, 122.07550354003907, 129.65260375976564], [10, 305.98419372558595, 328.60559326171875, 130.4945037841797, 138.07160400390626], [10, 305.98419372558595, 328.60559326171875, 138.91350402832032, 146.49060424804688], [10, 305.98419372558595, 328.60559326171875, 147.33250427246094, 154.9096044921875], [10, 305.98419372558595, 322.0572933959961, 155.75150451660156, 163.32860473632812], [10, 305.98419372558595, 335.15389312744145, 164.1705047607422, 171.74760498046876], [10, 305.98419372558595, 322.0572933959961, 172.58950500488282, 180.16660522460938], [10, 305.98419372558595, 319.67609344482423, 181.00850524902344, 188.58560546875], [10, 305.98419372558595, 319.67609344482423, 189.42750549316406, 197.00460571289062]]
2026-08-10 18:19:56,013 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=12, matched=12, pages=1, time=11.0s
2026-08-10 18:19:56,014 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:19:56,020 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:19:56,020 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[9]
2026-08-10 18:19:56,020 INFO     29 [qwen-vl-table] positions ： [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:19:56,281 INFO     29 [qwen-vl-table] page=9, rect=595x842, img=(1654x2339)
2026-08-10 18:19:56,281 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:19:56,281 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 491, \"bbox_end\": 513, \"encounter_dates\": [\"2026-03-12\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccccc}\n报告时间: 2026-03-12\n\\hline\n序号 & 项目名称 & 项目代码 & 结果 & 单位 & 参考区间 & 提示 \\\\\n\\hline\n1 & 大便颜色 & 大便颜色 & 黄褐色 & & 黄色-黄褐色 & \\\\\n2 & 大便性状 & 大便性状 & 软便 & & 软 & \\\\\n3 & 白细胞 & WBC & 未见 & /HP & 无或偶见 & \\\\\n4 & 红细胞 & RBC & 未见 & /HP & 无 & \\\\\n5 & 巨噬细胞 & 巨噬细胞 & 未见 & 个/HP & & \\\\\n6 & 脂肪球 & 脂肪球 & 未见 & /HP & & \\\\\n7 & 霉菌 & 霉菌 & 未见 & /HP & 无 & \\\\\n8 & 不消化食物 & 不消化食物 & 无 & & & \\\\\n9 & 蛔虫卵 & 蛔虫卵 & 未见 & & & \\\\\n10 & 鞭虫卵 & 鞭虫卵 & 未见 & & & \\\\\n11 & 钩虫卵 & 钩虫卵 & 未见 & & & \\\\\n12 & 蛲虫卵 & 蛲虫卵 & 未见 & & & \\\\\n13 & 肝吸虫卵 & 肝吸虫卵 & 未见 & & & \\\\\n14 & 带绦虫卵 & 带绦虫卵 & 未见 & & & \\\\\n15 & 其它 & 其它 & 未见异常 & & & \\\\\n16 & 隐血 & OB & 阴性(-) & & 阴性(-) & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 18:20:03,249 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:20:03,250 INFO     29 [qwen-vl-table] page=9 LLM output (len=2553):
{
  "report_date": "2026-03-12",
  "items": [
    {
      "name": "大便颜色",
      "item_code": null,
      "value": "黄褐色",
      "unit": null,
      "reference_range": "黄色-黄褐色",
      "abnormal": false
    },
    {
      "name": "大便性状",
      "item_code": null,
      "value": "软便",
      "unit": null,
      "reference_range": "软",
      "abnormal": false
    },
    {
      "name": "白细胞",
      "item_code": "WBC",
      "value": "未见",
      "unit": "/HP",
      "reference_range": "无或偶见",
      "abnormal": false
    },
    {
      "name": "红细胞",
      "item_code": "RBC",
      "value": "未见",
      "unit": "/HP",
      "reference_range": "无",
      "abnormal": false
    },
    {
      "name": "巨噬细胞",
      "item_code": null,
      "value": "未见",
      "unit": "个/HP",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "脂肪球",
      "item_code": null,
      "value": "未见",
      "unit": "/HP",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "霉菌",
      "item_code": null,
      "value": "未见",
      "unit": "/HP",
      "reference_range": "无",
      "abnormal": false
    },
    {
      "name": "不消化食物",
      "item_code": null,
      "value": "无",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "蛔虫卵",
      "item_code": null,
      "value": "未见",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "鞭虫卵",
      "item_code": null,
      "value": "未见",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "钩虫卵",
      "item_code": null,
      "value": "未见",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "蛲虫卵",
      "item_code": null,
      "value": "未见",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "肝吸虫卵",
      "item_code": null,
      "value": "未见",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "带绦虫卵",
      "item_code": null,
      "value": "未见",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "其它",
      "item_code": null,
      "value": "未见异常",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "隐血",
      "item_code": "OB",
      "value": "阴性(-)",
      "unit": null,
      "reference_range": "阴性(-)",
      "abnormal": false
    }
  ]
}
2026-08-10 18:20:03,250 INFO     29 [qwen-vl-table] coord grouping: {9: 16}
2026-08-10 18:20:03,258 INFO     29 [qwen-vl-table] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2085553, prompt_len=574
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
大便颜色、大便性状、白细胞、红细胞、巨噬细胞、脂肪球、霉菌、不消化食物、蛔虫卵、鞭虫卵、钩虫卵、蛲虫卵、肝吸虫卵、带绦虫卵、其它、隐血

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
2026-08-10 18:20:07,207 INFO     29 [qwen-vl-table] coord API raw response (len=774):
[
	{"text": "大便颜色", "bbox": [207, 369, 250, 378]},
	{"text": "大便性状", "bbox": [207, 380, 250, 389]},
	{"text": "白细胞", "bbox": [207, 390, 239, 399]},
	{"text": "红细胞", "bbox": [207, 400, 239, 409]},
	{"text": "巨噬细胞", "bbox": [207, 410, 247, 419]},
	{"text": "脂肪球", "bbox": [207, 420, 236, 429]},
	{"text": "霉菌", "bbox": [207, 430, 224, 439]},
	{"text": "不消化食物", "bbox": [207, 440, 256, 449]},
	{"text": "蛔虫卵", "bbox": [200, 451, 234, 460]},
	{"text": "鞭虫卵", "bbox": [200, 461, 234, 470]},
	{"text": "钩虫卵", "bbox": [200, 471, 234, 480]},
	{"text": "蛲虫卵", "bbox": [200, 481, 234, 490]},
	{"text": "肝吸虫卵", "bbox": [200, 491, 242, 500]},
	{"text": "带绦虫卵", "bbox": [200, 502, 242, 511]},
	{"text": "其它", "bbox": [200, 512, 219, 521]},
	{"text": "隐血", "bbox": [200, 522, 219, 531]}
]
2026-08-10 18:20:07,207 INFO     29 [qwen-vl-table] coord API: raw_items=16, valid_items=16, elapsed=3.9s
2026-08-10 18:20:07,207 INFO     29 [qwen-vl-table] coord item[0]: text=大便颜色, bbox=[207, 369, 250, 378]
2026-08-10 18:20:07,207 INFO     29 [qwen-vl-table] coord item[1]: text=大便性状, bbox=[207, 380, 250, 389]
2026-08-10 18:20:07,207 INFO     29 [qwen-vl-table] coord item[2]: text=白细胞, bbox=[207, 390, 239, 399]
2026-08-10 18:20:07,207 INFO     29 [qwen-vl-table] coord item[3]: text=红细胞, bbox=[207, 400, 239, 409]
2026-08-10 18:20:07,207 INFO     29 [qwen-vl-table] coord item[4]: text=巨噬细胞, bbox=[207, 410, 247, 419]
2026-08-10 18:20:07,207 INFO     29 [qwen-vl-table] coord item[5]: text=脂肪球, bbox=[207, 420, 236, 429]
2026-08-10 18:20:07,207 INFO     29 [qwen-vl-table] coord item[6]: text=霉菌, bbox=[207, 430, 224, 439]
2026-08-10 18:20:07,207 INFO     29 [qwen-vl-table] coord item[7]: text=不消化食物, bbox=[207, 440, 256, 449]
2026-08-10 18:20:07,207 INFO     29 [qwen-vl-table] coord item[8]: text=蛔虫卵, bbox=[200, 451, 234, 460]
2026-08-10 18:20:07,207 INFO     29 [qwen-vl-table] coord item[9]: text=鞭虫卵, bbox=[200, 461, 234, 470]
2026-08-10 18:20:07,207 INFO     29 [qwen-vl-table] coord item[10]: text=钩虫卵, bbox=[200, 471, 234, 480]
2026-08-10 18:20:07,207 INFO     29 [qwen-vl-table] coord item[11]: text=蛲虫卵, bbox=[200, 481, 234, 490]
2026-08-10 18:20:07,207 INFO     29 [qwen-vl-table] coord item[12]: text=肝吸虫卵, bbox=[200, 491, 242, 500]
2026-08-10 18:20:07,207 INFO     29 [qwen-vl-table] coord item[13]: text=带绦虫卵, bbox=[200, 502, 242, 511]
2026-08-10 18:20:07,207 INFO     29 [qwen-vl-table] coord item[14]: text=其它, bbox=[200, 512, 219, 521]
2026-08-10 18:20:07,207 INFO     29 [qwen-vl-table] coord item[15]: text=隐血, bbox=[200, 522, 219, 531]
2026-08-10 18:20:07,208 INFO     29 [qwen-vl-table] page=9 coord: matched 16/16, time=3.9s
2026-08-10 18:20:07,209 INFO     29 [qwen-vl-table] new_positions (16):
[[10, 123.22709747314454, 148.8249969482422, 310.6611090087891, 318.23820922851564], [10, 123.22709747314454, 148.8249969482422, 319.92200927734376, 327.4991094970703], [10, 123.22709747314454, 142.27669708251955, 328.3410095214844, 335.91810974121097], [10, 123.22709747314454, 142.27669708251955, 336.760009765625, 344.33710998535156], [10, 123.22709747314454, 147.03909698486328, 345.17901000976565, 352.7561102294922], [10, 123.22709747314454, 140.49079711914064, 353.59801025390624, 361.1751104736328], [10, 123.22709747314454, 133.347197265625, 362.0170104980469, 369.59411071777345], [10, 123.22709747314454, 152.396796875, 370.43601074218753, 378.0131109619141], [10, 119.05999755859375, 139.3001971435547, 379.6969110107422, 387.2740112304688], [10, 119.05999755859375, 139.3001971435547, 388.1159112548828, 395.69301147460936], [10, 119.05999755859375, 139.3001971435547, 396.53491149902345, 404.11201171875], [10, 119.05999755859375, 139.3001971435547, 404.9539117431641, 412.53101196289066], [10, 119.05999755859375, 144.06259704589846, 413.3729119873047, 420.95001220703125], [10, 119.05999755859375, 144.06259704589846, 422.63381225585937, 430.2109124755859], [10, 119.05999755859375, 130.37069732666015, 431.0528125, 438.6299127197266], [10, 119.05999755859375, 130.37069732666015, 439.47181274414066, 447.0489129638672]]
2026-08-10 18:20:07,209 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=16, matched=16, pages=1, time=11.2s
2026-08-10 18:20:07,218 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 18:20:07,218 INFO     29 [Trace] task=8fa8ece8 | doc=07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf | Extractor:LabExam | outputs={"chunks": "5 items, types={'LabReport': 5}", "html": "", "json": "594 items", "markdown": "", "text": "", "name": "07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_LabExam\": 5, \"chunks_Examination\": 4}"}
2026-08-10 18:20:07,219 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 18:20:07,224 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:20:07,224 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 18:20:07,650 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:20:07,654 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 18:20:07,655 INFO     29 [Trace] task=8fa8ece8 | doc=07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "594 items", "markdown": "", "text": "", "name": "07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_LabExam\": 5, \"chunks_Examination\": 4}"}
2026-08-10 18:20:07,655 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 18:20:07,660 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:20:07,660 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 18:20:08,165 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:20:08,175 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 18:20:08,175 INFO     29 [Trace] task=8fa8ece8 | doc=07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf | Extractor:Clinical | outputs={"chunks": "1 items", "html": "", "json": "594 items", "markdown": "", "text": "", "name": "07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_LabExam\": 5, \"chunks_Examination\": 4}"}
2026-08-10 18:20:08,176 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 18:20:08,183 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:20:08,183 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 18:20:08,885 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:20:08,896 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 18:20:08,896 INFO     29 [Trace] task=8fa8ece8 | doc=07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "594 items", "markdown": "", "text": "", "name": "07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_LabExam\": 5, \"chunks_Examination\": 4}"}
2026-08-10 18:20:08,896 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 18:20:08,902 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:20:08,902 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 18:20:09,359 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:20:09,371 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 18:20:09,371 INFO     29 [Trace] task=8fa8ece8 | doc=07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "594 items", "markdown": "", "text": "", "name": "07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_LabExam\": 5, \"chunks_Examination\": 4}"}
2026-08-10 18:20:09,371 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 18:20:09,384 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:20:09,384 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 18:20:09,810 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:20:09,820 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 18:20:09,820 INFO     29 [Trace] task=8fa8ece8 | doc=07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "594 items", "markdown": "", "text": "", "name": "07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_LabExam\": 5, \"chunks_Examination\": 4}"}
2026-08-10 18:20:09,821 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 18:20:09,828 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:20:09,829 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:20:09,829 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-10 18:20:09,829 INFO     29 [qwen-vl-text] positions(275): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:20:09,830 INFO     29 [qwen-vl-text] page grouping: [0, 1, 2, 3, 4, 5, 6, 7], lines per page: [38, 36, 36, 36, 37, 36, 30, 26]
2026-08-10 18:20:10,036 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 18:20:10,270 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 18:20:10,500 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 18:20:10,730 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 18:20:10,960 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 18:20:11,198 INFO     29 [qwen-vl-text] page=5, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 18:20:11,427 INFO     29 [qwen-vl-text] page=6, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 18:20:11,681 INFO     29 [qwen-vl-text] page=7, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 18:20:11,683 INFO     29 [qwen-vl-text] LLM extraction start, text_len=10800
2026-08-10 18:20:11,684 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:20:11,684 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 0, \"bbox_end\": 274, \"encounter_dates\": [\"2026-03-11\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "性别：男\n婚姻：已婚\n年龄：69岁\n入院日期：2026-03-11 08:04\n民族：汉族\n记录日期：2026-03-11 08:06\n职业：农民\n病史陈述者：患者本人\n主诉：确诊肺腺癌10月余，咯血2天余。\n现病史：患者因“呼吸困难2月余”于2025-04-05第1次入院，入院后完善检验检查：\nCEA(胸水)：癌胚抗原 538ng/ml；于04-07完善胸腔镜检查：镜下诊断：胸腔积液，胸壁结节\n样改变。病理：（胸膜活检）送检增生的纤维组织内见腺癌浸润，请结合临床诊治。免疫组\n化：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（部分+）、P40（点灶+）、CR（灶\n+）、ALK（1A4）（-）、Ki67（+，40%）。完善评估检查：胸部增强(64排-128层)：1.符合\n右侧胸腔引流术后改变，右侧液气胸并右侧颈根部及胸壁积气，肺组织压缩约70%。2.右肺\n下叶占位，考虑肺癌并纵隔及双肺门淋巴结转移可能，右侧胸膜结节状增厚、强化，考虑转\n移，请结合临床。3.左肺小结节，目前考虑良性，建议短期复查。4.双肺慢性炎症/纤维\n灶。5.动脉粥样硬化表现。6.甲状腺改变，请结合超声检查。7.右侧第8肋骨质改变，请结\n合临床。全身骨显像：1.右侧第6-8侧肋异常放射性浓聚，本院CT（2025-04-09）第6、7肋\n骨未见明显骨质异常，第8肋髓腔内见局灶高密度影，建议短期CT复查。2.左侧坐骨轻度放\n射性浓聚灶，本院CT未见明显骨质破坏，建议随诊。04-14复查胸部CT：对比2025-04-09\nCT：1.符合右侧胸腔引流术后改变，右侧液气胸并右侧颈根部及胸壁积气，较前减轻，肺组\n织压缩约30%。2.右肺下叶占位，较前相仿，考虑肺癌；纵隔及双肺门淋巴结同前；右侧胸\n膜结节状增厚，较前局部稍减轻，请结合临床。3.左肺小结节，较前相仿，建议短期复查。\n余所见大致同前。04-16复查胸片：1.右侧胸腔引流术后表现，对比2025-04-11X线：右侧气\n胸较前明显减少；原右侧胸壁及胸壁皮下积气基本消失；右侧胸腔积液较前减少，建议复查\n或结合CT检查。2.右肺下野占位，请结合临床及CT检查。患者完善基因检测未见基因突变，\n于04-17给予第1周期全身化疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2 q21d，同时辅\n以止吐、护胃、保肝、激素减轻化疗不良反应等治疗。于04-19给予信迪利单抗200mg抗肿瘤\n免疫治疗。患者化疗顺利，准予出院。末次出院诊断：1.肺腺癌伴纵隔淋巴结、肺门淋巴\n结、胸膜转移（T2bN3M1 IV期）恶性胸腔积液 2.气胸 3.左侧大隐静脉曲张 4.肝囊肿 5.双\n肾囊肿 6.前列腺稍大伴钙化\n患者因“确诊肺腺癌1月”于2025-05-07第2次入院，入院后完善相关检查：肺肿瘤检\n验：癌胚抗原 62.1ng/ml，神经元特异性烯醇化酶 19.8ng/ml，细胞角蛋白19片段\n6.21ng/ml；大便常规：未见异常；髂静脉及下肢深静脉、下肢浅静脉：左侧大隐静脉曲张，\n左侧隐股静脉瓣功能不全；胸部平扫(64排-128层)：对比2025-04-14CT：1.符合右侧胸腔引\n流术后改变，右侧液气胸，积液较前增多，积气较前减少；原右侧颈根部及胸壁少量积气本\n第1页\n次吸收。2.右肺下叶占位，较前略缩小，考虑肺癌；纵隔及双肺门淋巴结部分较前略增大；\n右侧胸膜结节状增厚，较前局部稍减轻，请结合临床。3.左肺小结节，较前相仿，建议短期\n复查。余所见大致同前。入院后于05-09拔除胸腔引流管。排除禁忌于05-09行第2周期全身\n化疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2 q21d，并辅以激素、止吐、护胃、保肝\n等治疗，05-10给予信迪利单抗200mg肿瘤免疫治疗。患者治疗结束，于2025-05-11出院。\n患者因“确诊肺腺癌1月余，发热5天”于2025-05-19第3次入院，入院后完善检验检\n查：大便菌群分析:细菌总数600 个/油镜视野（参考值500～5000个），革兰阳性球菌少量，\n革兰阴性杆菌少量，酵母样真菌孢子+，酵母样真菌菌丝+；艰难梭菌毒素A/B检测:艰难梭\n菌毒素A/B检测 0.02；大便细菌培养+药敏:经两天普通培养，鉴定生长热带念珠菌+++，无\n肠球菌生长，无肠杆菌生长，无沙门氏菌、志贺氏菌生长。痰细菌学检查:经2天普通培养，\n经鉴定为正常菌群生长，无流感嗜血杆菌生长。胸部平扫(64排-128层)：对比\n2025-04-14CT：1.符合右侧胸腔引流术后改变，右侧液气胸，积液较前增多，积气较前减\n少；原右侧颈根部及胸壁少量积气本次吸收。2.右肺下叶占位，较前略缩小，考虑肺癌；纵\n隔及双肺门淋巴结部分较前略增大；右侧胸膜结节状增厚，较前局部稍减轻，请结合临床。\n3.左肺小结节，较前相仿，建议短期复查。余所见大致同前。腹部（包括盆腔）平扫(64\n排)：1.考虑肝多发囊肿、右肾囊肿，必要时增强扫描。2.双肾周桥隔略增厚。3.动脉粥样\n硬化。4.前列腺增大伴钙化。5.L5椎体前滑脱（I°），双侧椎弓峡部裂。胸部平扫(64排\n-128层)：对比2025-05-08CT：1.右侧液气胸，积液较前增多，积气较前减少。2.右肺下叶\n占位，较前缩小，考虑肺癌；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜结节状增\n厚，较前变化不著，请结合临床。3.左肺小结节，较前相仿，建议短期复查。余所见大致同\n前。入院后给予哌拉西林他唑巴坦抗感染，蒙脱石散止泻，枯草杆菌二联活菌胶囊调整消化\n道菌群，利伐沙班抗凝，制霉素片口服治疗，现患者病情稳定，于2025-05-29出院。\n患者因“确诊肺腺癌2月余。”第4次入院，入院后完善辅助检查，入院后排除禁忌，\n06-06行第3周期治疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2，联合信迪利单抗200mg\n抗肿瘤免疫治疗，并辅以激素、止吐、护胃、保肝等治疗，治疗结束后复查血常规未见明显\n骨髓抑制，于2025-06-08出院。末次出院诊断：1.恶性肿瘤维持性化学治疗 2.恶性肿瘤免\n疫治疗 3.肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转移 肺门淋巴结转移 胸膜转移 恶性胸腔\n积液 4.大隐静脉曲张 5.肾囊肿 6.单纯性肝囊肿。\n患者因“确诊肺腺癌2月余，为继续治疗”于2025-06-26第5次入院，入院后完善相关检\n查，排除禁忌，06-27行第4周期治疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2，联合\n信迪利单抗200mg抗肿瘤免疫治疗，并辅以激素、止吐、护胃、保肝等治疗，治疗结束后复\n查血常规未见明显骨髓抑制，于2025-06-29出院。末次出院诊断：1.恶性肿瘤维持性化学治\n疗 2.恶性肿瘤免疫治疗 3.肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转移 肺门淋巴结转移 胸\n膜转移 4.恶性胸腔积液 5.大隐静脉曲张 6.肾囊肿 7.单纯性肝囊肿.\n患者因“确诊肺腺癌3月余，为继续治疗”2025-07-17入院，入院后完善相关必要辅助\n第2页\n检查：电解质+血气分析:酸碱度7.476，二氧化碳分压36.4mmHg，氧分压114.0mmHg；急\n查血常规+CRP:红细胞3.61x10^12/L，血红蛋白110g/L，血小板总数222×10^9/L，白细\n胞4.90×10^9/L，中性粒细胞绝对值3.59×10^9/L，淋巴细胞绝对值0.77×10^9/L，超\n敏C-反应蛋白17.92mg/L；肺肿瘤检验：癌胚抗原54.9ng/ml，细胞角蛋白19片段\n5.54ng/ml，胃泌素释放肽前体80.2pg/ml；生化系列36项:白蛋白(溴甲酚绿法)\n31.59g/L，镁0.72mmol/L，肌酐(酶法)55μmol/L，肌酸激酶31U/L；DIC系列-5项:纤维\n蛋白原5.47g/L，D-二聚体3.53mg/L；急查降钙素原、急查心梗三项、皮质醇(7:00-10:\n00am)、促肾上腺皮质激素(8时)、甲状腺功能3项、急查NT-proBNP、大便常规(粪沉渣)+\n潜血、尿液分析+尿沉渣未见明显异常。常规心电图检查(自动分析)：窦性心动过速；心\n脏超声检查(含左心功能测定)：主动脉瓣轻度反流，三尖瓣轻度反流；颅脑平扫+DWI+增\n强(3T)：1.双侧额顶叶及侧脑室旁白质内脱髓鞘改变。2.老年脑改变。3.部分副鼻窦炎；\n右侧乳突炎。4.鼻中隔偏曲，双下鼻甲肥大。颈部：左侧颈部淋巴结稍大，右侧颈部淋巴结\n可见；髂静脉及下肢深静脉、下肢浅静脉：左侧大隐静脉曲张，左侧隐股静脉瓣功能不全；\n腹部(包括盆腔)平扫(64排)：1.考虑肝多发囊肿、右肾囊肿，必要时增强扫描。2.双肾周\n桥隔略增厚。3.动脉粥样硬化。4.前列腺增大伴钙化。5.L5椎体前滑脱(I°)，双侧椎弓\n峡部裂。以上所见较2025-05-26CT变化不著。胸部平扫(64排-128层)：对比2025-05-26CT:\n1.右肺下叶肺癌，较前略缩小、其内新见空洞影；右肺小叶间隔增厚，考虑癌性淋巴管炎可\n能；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜结节状增厚，较前变化不著；请结合\n临床。2.右侧液气胸，积液较前略增多，积气较前明显减少。3.左肺小结节，较前相仿，建\n议短期复查。4.右侧第7-9、12肋骨高密度影，较前密度增高，转移?建议ECT进一步检查。\n余所见大致同前。肋骨平扫+DWI+增强(3T)：1.右侧第7-9、12肋改变，成骨性转移?请结\n合其它影像学检查。2.右侧胸腔积液。3.肝内多发囊肿。排除禁忌，07-18行第5周期治疗：\n培美曲塞0.8gd1+顺铂注射液65mgd1、d2，联合信迪利单抗200mg抗肿瘤免疫治疗，并辅\n以激素、止吐、护胃、保肝等治疗，治疗结束后复查血常规未见明显骨髓抑制，针对肋骨异\n常请放疗科会诊后建议可考虑放疗，07-21出院。\n患者因“确诊肺腺癌4月，为继续治疗”2025-08-07第7次入院，入院后完善相关检查，\n急查血常规+CRP:血红蛋白109g/L，血小板总数205×10^9/L，白细胞4.58×10^9/L，中\n性粒细胞百分率70.9%，超敏C-反应蛋白17.43mg/L；超敏肌钙蛋白T14.80pg/ml；DIC系\n列-5项:纤维蛋白原5.27g/L，D-二聚体4.37mg/L；N端-B型钠尿肽前体71.5pg/ml；促肾\n上腺皮质激素(8时)：促肾上腺皮质激素(8时)31.7pg/ml；生化系列36项:白蛋白(溴甲酚绿\n法)33.34g/L，钾3.93mmol/L，钠140.1mmol/L，氯104.8mmol/L，尿素5.04mmol/L，肌\n酐(酶法)65μmol/L；皮质醇(7:00-10:00am)：皮质醇(7:00-10:00am)295nmol/L；甲状腺\n功能3项：促甲状腺素3.17mIU/L，游离甲状腺素13.6pmol/L，游离三碘甲状腺原氨酸\n4.46pmol/L；肺肿瘤检验：癌胚抗原52.6ng/ml，神经元特异性烯醇化酶20.4ng/ml，\n细胞角蛋白19片段4.81ng/ml，胃泌素释放肽前体92.9pg/ml。常规心电图检查(自动分\n第3页\n析）：窦性心律，大致正常心电图。排除禁忌，于08-08给予第6周期化疗，方案为培美曲塞\n0.8g+顺铂注射液 65mg d1、d2，联合信迪利单抗200mg 免疫治疗，过程顺利，08-10行地\n舒单抗120mg抗骨转移治疗；复查血常规未见明显骨髓抑制，08-10出院。\n患者因“确诊肺腺癌4月，为继续治疗”于2025-08-28第8次入院，入院后完善辅助检\n查：胸部平扫：对比2025-07-18CT：1.右肺下叶肺癌，较前变化不著；右肺小叶间隔增厚，\n较前变化不著，考虑癌性淋巴管炎可能；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜\n结节状增厚，较前变化不著；请结合临床。2.右侧液气胸，积液较前变化不著，积气较前增\n多。3.左肺小结节，较前相仿，建议短期复查。4.右侧第7-9、12肋骨高密度影，较前变化\n不著，转移？建议ECT进一步检查。余所见大致同前。下腹部平扫：1.考虑右肾囊肿，较\n2025-07-18变化不著，必要时增强扫描。2.双肾周桥隔略增厚。3.动脉粥样硬化。上腹部平\n扫：考虑肝多发囊肿，较2025-07-18变化不明显，建议结合增强检查明确。盆腔平扫：1.前\n列腺增大伴钙化。2.L5椎体前滑脱（I°），双侧椎弓峡部裂。以上所见较2025-07-18变化\n不著。排除禁忌，给予培美曲塞 0.8g 联合信迪利单抗 200mg免疫治疗，并辅以激素、止\n吐、护胃、保肝等治疗，治疗过程顺利，患者病情稳定，2025-08-30出院。出院诊断：1.恶\n性肿瘤维持性化学治疗 2.恶性肿瘤免疫治疗 3.右肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转\n移 肺门淋巴结转移 胸膜转移 骨转移 4.恶性胸腔积液 5.大隐静脉曲张 6.肾囊肿 7.单纯\n性肝囊肿。\n患者因“确诊肺腺癌5月余，为继续治疗”于2025-10-06第9次入院，入院后完善辅助检\n查：急查血常规+CRP:血红蛋白 114g/L，血小板总数 212×10^9/L，白细胞\n7.30×10^9/L，中性粒细胞百分率 80.0%，超敏C-反应蛋白 16.04mg/L；皮质醇(7:00-10:\n00am):皮质醇(7:00-10:00am) 442nmol/L；促肾上腺皮质激素(8时):促肾上腺皮质激素(8\n时) 29.3pg/ml；甲状腺功能3项:促甲状腺素 4.94mIU/L，游离甲状腺素 14.4pmol/L，游离\n三碘甲状腺原氨酸 3.85pmol/L；生化系列36项:白蛋白(溴甲酚绿法) 36.10g/L，白蛋白:球\n蛋白 0.96，天门冬氨酸氨基转移酶 18U/L，丙氨酸氨基转移酶 8U/L，尿素 5.84mmol/L，\n肌酐(酶法) 78μmol/L；肺肿瘤检验-莱山:癌胚抗原 68.6ng/ml，细胞角蛋白19片段\n9.45ng/ml，胃泌素释放肽前体 96.7pg/ml；DIC系列-5项:纤维蛋白原 5.04g/L，D-二聚体\n3.28mg/L；急查NT-proBNP:N端-B型钠尿肽前体 50.1pg/ml；急查心梗三项:超敏肌钙蛋白T\n14.00pg/ml，肌酸激酶-MB同工酶质量测定 0.54ng/ml，肌红蛋白 43.2ng/ml。排除禁忌，\n于2025-10-06给予本周期治疗，方案为培美曲塞 0.8g联合信迪利单抗200mg，并给予地舒单\n抗120mg治疗骨转移，2025-10-07办理出院。出院诊断：1.右肺腺癌（T2bN3M1 IV期） 纵隔\n淋巴结转移 肺门淋巴结转移 胸膜转移 骨转移 2.恶性胸腔积液 3.大隐静脉曲张 4.肾囊肿\n5.单纯性肝囊肿。\n患者因“确诊肺腺癌7月余，为继续治疗”于2025-11-07第10次入院，入院后完善相关\n检查：急查血常规+CRP:血红蛋白 115g/L，血小板总数 214×10^9/L，白细胞\n7.21×10^9/L，中性粒细胞百分率 82.3%，超敏C-反应蛋白 20.50mg/L；DIC系列-5项:纤维\n第 4 页\n蛋白原 5.04g/L，D-二聚体 2.19mg/L；皮质醇(7:00-10:00am):皮质醇(7:00-10:00am)\n286nmol/L；促肾上腺皮质激素(8时):促肾上腺皮质激素(8时)23.3pg/ml；急查心梗三项:\n超敏肌钙蛋白T 17.70pg/ml；肺肿瘤检验-莱山:癌胚抗原 75.8ng/ml，细胞角蛋白19片段\n12.4ng/ml，胃泌素释放肽前体 90.5pg/ml；生化系列36项:白蛋白(溴甲酚绿法)\n32.49g/L，脂蛋白(a)343mg/L，唾液酸 769mg/L；N端-B型钠尿肽前体、甲状腺功能3项未\n见异常。常规心电图检查：窦性心动过速。全身骨显像：与本院2025-04-10骨显像比较：1.\n右侧多根肋骨多发异常放射性浓聚灶，病灶数目较前增多，浓聚程度增高，提示骨转移瘤可\n能大，请结合其他检查综合考虑；2.前次检查所示左侧坐骨轻度放射性浓聚灶，本次检查未\n见显示；3.双肩关节及双膝关节区异常放射性浓聚，考虑炎性病变，请结合临床。颅脑平扫\n+DWI+增强+薄层：1.双侧额顶叶及侧脑室旁白质内脱髓鞘改变；2.老年脑改变，双侧额颞部\n少量硬膜下积液；3.部分副鼻窦炎；右侧乳突炎；4.鼻中隔偏曲，双下鼻甲肥大。心脏超声\n检查（含左心功能测定）：静息状态下：心内结构及血流未见明显异常髂静脉及下肢深静脉\n(双侧)：双侧髂静脉及下肢深静脉血流通畅颈部：双侧颈部未见明显增大淋巴结胸部平扫\n+增强：对比2025-08-28CT：1.右肺下叶肺癌，较前增大；右肺小叶间隔增厚，较前略进\n展，考虑癌性淋巴管炎可能；纵隔及双肺门淋巴结，部分较前略增大；考虑右侧胸膜转移，\n较前明显进���，累及邻近右前胸壁及右侧膈肌可能；请结合临床并复查；2.右侧胸腔积液，\n较前变化不著，原右侧胸腔积气吸收；3.左肺小结节，部分较前略增大（如下叶薄层\nimg231、243），部分结节较前相仿，建议短期复查；4.右侧第7-9、12肋骨高密度影，较前\n变化不著，转移？建议ECT进一步检查；余所见大致同前。上腹部平扫+增强：考虑肝多发囊\n肿，较2025-08-28变化不明显。下腹部平扫+增强：1.考虑右肾囊肿，较2025-08-28变化不\n著；2.双肾周桥隔略增厚；3.动脉粥样硬化。排除禁忌给予本周期治疗，方案为培美曲塞\n0.8g、信迪利单抗200mg联合恩度 210mg q21d治疗。治疗结束，患者病情稳定，2025-11-14\n办理出院。出院诊断：1.右肺腺癌(T2bN3M1 IV期) 纵隔淋巴结转移 肺门淋巴结转移 胸\n膜转移 骨转移 2.恶性胸腔积液 3.大隐静脉曲张 4.肾囊肿 5.肝囊肿\n患者因“确诊肺腺癌8月余，为继续治疗”于2026-01-08再入院，入院后完善相关辅助\n检查：01-08：急查NT-proBNP、促肾上腺皮质激素(8时)、皮质醇(7:00-10:00am)等未见明\n显异常。急查血常规+CRP+SAA:红细胞 3.93x10^12/L，血红蛋白 118g/L，红细胞压积\n35.8%，红细胞分布宽度SD 47.4fl，中性粒细胞百分率 77.9%，淋巴细胞百分率 9.4%，单\n核细胞百分率 10.2%，淋巴细胞绝对值 0.67×10^9/L，单核细胞绝对值 0.73×10^9/L，超\n敏C-反应蛋白 30.56mg/L，血清淀粉样蛋白A 26.98mg/L；急查心梗三项:超敏肌钙蛋白T\n15.10pg/ml；DIC系列-5项:纤维蛋白原 6.22g/L，D-二聚体 1.66mg/L；急查降钙素原：\n0.0969ng/ml；生化系列36项:白蛋白(溴甲酚绿法) 31.69g/L，白蛋白:球蛋白 0.87，肾小\n球滤过率 89.97ml/(min·1.73m²)，肌酸激酶 38U/L，脂蛋白(a) 452mg/L，唾液酸\n765mg/L；甲状腺功能6项:促甲状腺素 4.69mIU/L；肺肿瘤检验\n癌胚抗原\n73.4ng/ml，神经元特异性烯醇化酶 18.4ng/ml，细胞角蛋白19片段 19.1ng/ml，胃泌素释\n第5页\n放肽前体81.4pg/ml；常规心电图检查（自动分析）：窦性心动过速。下腹部平扫+增强：\n1.考虑右肾囊肿，较2025-11-08变化不著。2.双肾周桥隔略增厚。3.动脉粥样硬化。上腹部\n平扫+增强：考虑肝多发囊肿，较2025-11-08变化不明显。胸部平扫+增强：对比\n2025-11-08CT：1.右肺下叶肺癌，范围整体较前增大；右肺小叶间隔增厚，较前进展，考虑\n癌性淋巴管炎可能；纵隔及双肺门淋巴结大致同前；考虑右侧胸膜转移，较前进展，累及邻\n近右前胸壁及右侧膈肌可能；请结合临床并复查。2.右侧胸腔积液，较前变化不著。3.左肺\n小结节，较前相仿，建议短期复查。4.右侧第7-9、12肋骨高密度影，局部略进展，转移可\n能，建议ECT进一步检查。余所见大致同前。01-09：髂静脉及下肢深静脉、下肢浅静脉：左\n侧大隐静脉曲张左侧隐股静脉瓣功能不全。01-10：心脏超声检查（含左心功能测定）：静\n息状态下：心内结构及血流未见明显异常。考虑患者肿瘤较前进展，请肿瘤科及放疗科会\n诊，给予更换二线化疗方案，排除禁忌，1-09行开始给予恩度抗血管生成，01-12给予二线\n第1周期全身化疗：白蛋白紫杉醇300mg d1、信迪利单抗200mg，01-13给予地舒单抗120mg抗\n骨转移。期间联合护肝、护胃、止吐、激素等治疗，现病情平稳，准予出院。末次出院诊\n断：1.右肺腺癌（T2bN3M1 IV期）纵隔淋巴结转移肺门淋巴结转移胸膜转移骨转移2.\n恶性胸腔积液3.大隐静脉曲张4.肾囊肿5.肝囊肿6.贫血7.低蛋白血症\n患者出院后规律服药、门诊复诊，偶有咳嗽，咳白薄痰，腰肋部水肿，于2026-2-10再\n入院，\n入院后完善辅助检查：NT-proBNP未见明显异常；血常规+CRP+SAA：红细胞\n4.25x10^12/L，血红蛋白125g/L，红细胞压积38.4%，红细胞分布宽度SD47.8fl，中性粒\n细胞百分率83.4%，淋巴细胞百分率8.0%，中性粒细胞绝对值7.35×10^9/L，淋巴细胞绝\n对值0.70×10^9/L，单核细胞绝对值0.62×10^9/L，超敏C-反应蛋白24.16mg/L，血清淀\n粉样蛋白A13.13mg/L；心梗三项：超敏肌钙蛋白T14.10pg/ml；降钙素原：0.0528ng/ml；生\n化系列36项：白蛋白（溴甲酚绿法）34.82g/L，白蛋白：球蛋白1.02，肾小球滤过率\n89.97ml/(min•1.73m²)，肌酸激酶33U/L，脂蛋白(a)510mg/L，唾液酸792mg/L；肺肿瘤\n检验：癌胚抗原100ng/ml，神经元特异性烯醇化酶31.1ng/ml，细胞角蛋白19片段\n28.8ng/ml，胃泌素释放肽前体87.7pg/ml；DIC系列-5项：纤维蛋白原6.71g/L，D-二聚体\n1.42mg/L；心电图：窦性心律大致正常心电图。尿液分析、大便常规及潜血、促肾上腺皮\n质激素(8时)、皮质醇(7:00-10:00am)、甲状腺功能6项等未见明显异常。排除禁忌，02-10\n开始给予恩度抗血管生成，02-11给予二线第2周期全身化疗：白蛋白紫杉醇300mg d1，同时\n辅以激素、止吐、护胃、保肝治疗，同时给予信迪利单抗200mg抗肿瘤免疫治疗，02-12给予\n地舒单抗120mg抗骨转移治疗。于2026-02-13出院。末次出院诊断：1.恶性肿瘤维持性化学\n治疗2.恶性肿瘤免疫治疗3.恶性肿瘤靶向治疗4.右肺腺癌（T2bN3M1 IV期）纵隔淋巴结\n转移肺门淋巴结转移胸膜转移骨转移5.恶性胸腔积液6.大隐静脉曲张7.肾囊肿8.肝\n囊肿。\n患者出院后规律门诊复诊，偶有咳嗽、咳痰，2天前无明显诱因出现咯血，感痰较前增\n第6页\n多，每天数十口，色鲜红，今为进一步治疗入院。患者病后神志清，精神状态一般，食欲一\n般，睡眠良好，大便正常，小便正常，体力情况一般，体重无明显变化。\n既往史：否认食物、药物过敏史，参阅既往入院记录。\n个人史：参阅既往入院记录。\n家族史：参阅既往入院记录。\n体 格 检 查\nT 36.3℃ P 107次/分 R 21次/分 Bp 144/99mmHg\n发育正常，营养良好，正常面容，表情自如，自主体位，神志清楚，查体合作。全身皮\n肤粘膜无黄染，无皮疹，无皮下出血，无皮下结节，皮下无水肿，无肝掌、蜘蛛痣，毛发分\n布均匀。全身浅表淋巴结无肿大。眼睑无水肿，结膜无苍白，眼球无突出，无震颤，巩膜无\n黄染，瞳孔等大等圆，对光反射灵敏，耳廓对称，无畸形，牵拉无疼痛，外耳道无异常分泌\n物，乳突无压痛，无听力粗试障碍。鼻无畸形。口唇无发绀，口腔粘膜无充血、糜烂。舌苔\n薄白，伸舌无偏斜、震颤，牙龈无红肿，咽部粘膜无充血，扁桃体无肿大。颈软无抵抗，颈\n动脉无异常搏动，半坐位颈静脉未见充盈，颈部大血管区未闻及血管杂音。气管居中，肝颈\n静脉回流征阴性，甲状腺无肿大，无压痛、震颤、血管杂音。胸廓无畸形，呼吸运动两侧对\n称，肋间隙无狭窄或饱满，胸壁无压痛，语颤无增强、减弱，胸骨无压痛。双肺叩诊清音，\n呼吸规整，双肺呼吸音低，未闻及干湿性啰音，无胸膜摩擦音。心前区无异常隆起、异常搏\n动、震颤，心浊音界不大，心率107次/分，律齐，心音有力，各瓣膜听诊区未闻及杂音，无\n心包摩擦音。腹平坦，软，无压痛、反跳痛，腹部无包块。肝脏未触及，脾脏未触及，\nMurphy氏征阴性，肾区无叩击痛，无移动性浊音。肠鸣音正常，4次/分。肛门及外生殖器未\n查。脊柱正常生理弯曲，四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾），关节无肿\n胀、压痛，下肢无浮肿。\n肌肉无压痛，四肢肌力、肌张力未见异常，双侧肱\n二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性。\n专科检查： 胸廓无畸形，呼吸运动两侧对称，肋间隙无狭窄或饱满，胸壁无压痛，语\n颤无增强、减弱，胸骨无压痛。双肺叩诊清音，呼吸规整，双肺呼吸音低，未闻及干湿性啰\n音，无胸膜摩擦音。\n辅 助 检 查\n检查日期 项目 结果 检查单位 检查编号\n第 7 页\n2025-04-09\n病理\n(胸膜活检)送检增生的纤维组\n织内见腺癌浸润，请结合临床诊\n治。免疫组化：TTF-1（-）、\nNapsinA（-）、CK7（+）、CK5/6\n（部分+）、P40（点灶+）、CR（\n灶+）、ALK（1A4）（-）、Ki67\n(+,40%）。C-MET免疫组化检测\n报告检测平台：Roche Ventana\nBenchmark Ultra；抗体克隆号：\nSP44,Roche；表达部位：细胞膜和\n细胞浆；阳性强度及百分比：++(\n40%),+(60%)阳性等级：1+\n细胞数量：≥100。\n初步诊断：\n1.咯血\n2.右肺腺癌（T2bN3M1 IV期）\n纵隔淋巴结转移\n肺门淋巴结转移\n胸膜转移\n骨转移\n3.恶性胸腔积液\n4.大隐静脉曲张\n5.肾囊肿\n6.肝囊肿",
    "role": "user"
  }
]
2026-08-10 18:20:24,089 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:20:24.089+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 86, "failed": 0, "current": {"8fa8ece894e711f1bd9827cf206dfa2d": {"id": "8fa8ece894e711f1bd9827cf206dfa2d", "doc_id": "8f6c718294e711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 16708238, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385769380, "task_type": "dataflow", "root_trace_id": "0aa1bc1a4312482d8e4b2a1774c52cc7", "root_traceparent": "00-0aa1bc1a4312482d8e4b2a1774c52cc7-ad93c0febce673ce-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:20:56,222 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:20:56.219+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 86, "failed": 0, "current": {"8fa8ece894e711f1bd9827cf206dfa2d": {"id": "8fa8ece894e711f1bd9827cf206dfa2d", "doc_id": "8f6c718294e711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 16708238, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385769380, "task_type": "dataflow", "root_trace_id": "0aa1bc1a4312482d8e4b2a1774c52cc7", "root_traceparent": "00-0aa1bc1a4312482d8e4b2a1774c52cc7-ad93c0febce673ce-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:21:28,358 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:21:28.358+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 86, "failed": 0, "current": {"8fa8ece894e711f1bd9827cf206dfa2d": {"id": "8fa8ece894e711f1bd9827cf206dfa2d", "doc_id": "8f6c718294e711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 16708238, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385769380, "task_type": "dataflow", "root_trace_id": "0aa1bc1a4312482d8e4b2a1774c52cc7", "root_traceparent": "00-0aa1bc1a4312482d8e4b2a1774c52cc7-ad93c0febce673ce-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:21:39,671 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:21:39,672 INFO     29 [qwen-vl-text] LLM output (len=12126):
{
  "encounter_date": "2026-03-11",
  "dm_name": null,
  "dm_gender": "男",
  "dm_age": 69,
  "dm_ethnicity": "汉族",
  "dm_marital_status": "已婚",
  "dm_occupation": "农民",
  "dm_admission_time": "2026-03-11 08:04",
  "dm_record_time": "2026-03-11 08:06",
  "dm_history_provider": "患者本人",
  "cc_text": "确诊肺腺癌10月余，咯血2天余。",
  "cc_main_symptoms": [
    "确诊肺腺癌",
    "咯血"
  ],
  "cc_duration": "10月余，2天余",
  "pi_text": "患者因“呼吸困难2月余”于2025-04-05第1次入院，入院后完善检验检查：CEA(胸水)：癌胚抗原 538ng/ml；于04-07完善胸腔镜检查：镜下诊断：胸腔积液，胸壁结节样改变。病理：（胸膜活检）送检增生的纤维组织内见腺癌浸润，请结合临床诊治。免疫组化：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（部分+）、P40（点灶+）、CR（灶+）、ALK（1A4）（-）、Ki67（+，40%）。完善评估检查：胸部增强(64排-128层)：1.符合右侧胸腔引流术后改变，右侧液气胸并右侧颈根部及胸壁积气，肺组织压缩约70%。2.右肺下叶占位，考虑肺癌并纵隔及双肺门淋巴结转移可能，右侧胸膜结节状增厚、强化，考虑转移，请结合临床。3.左肺小结节，目前考虑良性，建议短期复查。4.双肺慢性炎症/纤维灶。5.动脉粥样硬化表现。6.甲状腺改变，请结合超声检查。7.右侧第8肋骨质改变，请结合临床。全身骨显像：1.右侧第6-8侧肋异常放射性浓聚，本院CT（2025-04-09）第6、7肋骨未见明显骨质异常，第8肋髓腔内见局灶高密度影，建议短期CT复查。2.左侧坐骨轻度放射性浓聚灶，本院CT未见明显骨质破坏，建议随诊。04-14复查胸部CT：对比2025-04-09CT：1.符合右侧胸腔引流术后改变，右侧液气胸并右侧颈根部及胸壁积气，较前减轻，肺组织压缩约30%。2.右肺下叶占位，较前相仿，考虑肺癌；纵隔及双肺门淋巴结同前；右侧胸膜结节状增厚，较前局部稍减轻，请结合临床。3.左肺小结节，较前相仿，建议短期复查。余所见大致同前。04-16复查胸片：1.右侧胸腔引流术后表现，对比2025-04-11X线：右侧气胸较前明显减少；原右侧胸壁及胸壁皮下积气基本消失；右侧胸腔积液较前减少，建议复查或结合CT检查。2.右肺下野占位，请结合临床及CT检查。患者完善基因检测未见基因突变，于04-17给予第1周期全身化疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2 q21d，同时辅以止吐、护胃、保肝、激素减轻化疗不良反应等治疗。于04-19给予信迪利单抗200mg抗肿瘤免疫治疗。患者化疗顺利，准予出院。末次出院诊断：1.肺腺癌伴纵隔淋巴结、肺门淋巴结、胸膜转移（T2bN3M1 IV期）恶性胸腔积液 2.气胸 3.左侧大隐静脉曲张 4.肝囊肿 5.双肾囊肿 6.前列腺稍大伴钙化\n患者因“确诊肺腺癌1月”于2025-05-07第2次入院，入院后完善相关检查：肺肿瘤检验：癌胚抗原 62.1ng/ml，神经元特异性烯醇化酶 19.8ng/ml，细胞角蛋白19片段 6.21ng/ml；大便常规：未见异常；髂静脉及下肢深静脉、下肢浅静脉：左侧大隐静脉曲张，左侧隐股静脉瓣功能不全；胸部平扫(64排-128层)：对比2025-04-14CT：1.符合右侧胸腔引流术后改变，右侧液气胸，积液较前增多，积气较前减少；原右侧颈根部及胸壁少量积气本次吸收。2.右肺下叶占位，较前略缩小，考虑肺癌；纵隔及双肺门淋巴结部分较前略增大；右侧胸膜结节状增厚，较前局部稍减轻，请结合临床。3.左肺小结节，较前相仿，建议短期复查。余所见大致同前。入院后于05-09拔除胸腔引流管。排除禁忌于05-09行第2周期全身化疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2 q21d，并辅以激素、止吐、护胃、保肝等治疗，05-10给予信迪利单抗200mg肿瘤免疫治疗。患者治疗结束，于2025-05-11出院。\n患者因“确诊肺腺癌1月余，发热5天”于2025-05-19第3次入院，入院后完善检验检查：大便菌群分析:细菌总数600 个/油镜视野（参考值500～5000个），革兰阳性球菌少量，革兰阴性杆菌少量，酵母样真菌孢子+，酵母样真菌菌丝+；艰难梭菌毒素A/B检测:艰难梭菌毒素A/B检测 0.02；大便细菌培养+药敏:经两天普通培养，鉴定生长热带念珠菌+++，无肠球菌生长，无肠杆菌生长，无沙门氏菌、志贺氏菌生长。痰细菌学检查:经2天普通培养，经鉴定为正常菌群生长，无流感嗜血杆菌生长。胸部平扫(64排-128层)：对比2025-04-14CT：1.符合右侧胸腔引流术后改变，右侧液气胸，积液较前增多，积气较前减少；原右侧颈根部及胸壁少量积气本次吸收。2.右肺下叶占位，较前略缩小，考虑肺癌；纵隔及双肺门淋巴结部分较前略增大；右侧胸膜结节状增厚，较前局部稍减轻，请结合临床。3.左肺小结节，较前相仿，建议短期复查。余所见大致同前。腹部（包括盆腔）平扫(64排)：1.考虑肝多发囊肿、右肾囊肿，必要时增强扫描。2.双肾周桥隔略增厚。3.动脉粥样硬化。4.前列腺增大伴钙化。5.L5椎体前滑脱（I°），双侧椎弓峡部裂。胸部平扫(64排-128层)：对比2025-05-08CT：1.右侧液气胸，积液较前增多，积气较前减少。2.右肺下叶占位，较前缩小，考虑肺癌；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜结节状增厚，较前变化不著，请结合临床。3.左肺小结节，较前相仿，建议短期复查。余所见大致同前。入院后给予哌拉西林他唑巴坦抗感染，蒙脱石散止泻，枯草杆菌二联活菌胶囊调整消化道菌群，利伐沙班抗凝，制霉素片口服治疗，现患者病情稳定，于2025-05-29出院。\n患者因“确诊肺腺癌2月余。”第4次入院，入院后完善辅助检查，入院后排除禁忌，06-06行第3周期治疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2，联合信迪利单抗200mg抗肿瘤免疫治疗，并辅以激素、止吐、护胃、保肝等治疗，治疗结束后复查血常规未见明显骨髓抑制，于2025-06-08出院。末次出院诊断：1.恶性肿瘤维持性化学治疗 2.恶性肿瘤免疫治疗 3.肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转移 肺门淋巴结转移 胸膜转移 恶性胸腔积液 4.大隐静脉曲张 5.肾囊肿 6.单纯性肝囊肿。\n患者因“确诊肺腺癌2月余，为继续治疗”于2025-06-26第5次入院，入院后完善相关检查，排除禁忌，06-27行第4周期治疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2，联合信迪利单抗200mg抗肿瘤免疫治疗，并辅以激素、止吐、护胃、保肝等治疗，治疗结束后复查血常规未见明显骨髓抑制，于2025-06-29出院。末次出院诊断：1.恶性肿瘤维持性化学治疗 2.恶性肿瘤免疫治疗 3.肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转移 肺门淋巴结转移 胸膜转移 4.恶性胸腔积液 5.大隐静脉曲张 6.肾囊肿 7.单纯性肝囊肿.\n患者因“确诊肺腺癌3月余，为继续治疗”2025-07-17入院，入院后完善相关必要辅助检查：电解质+血气分析:酸碱度7.476，二氧化碳分压36.4mmHg，氧分压114.0mmHg；急查血常规+CRP:红细胞3.61x10^12/L，血红蛋白110g/L，血小板总数222×10^9/L，白细胞4.90×10^9/L，中性粒细胞绝对值3.59×10^9/L，淋巴细胞绝对值0.77×10^9/L，超敏C-反应蛋白17.92mg/L；肺肿瘤检验：癌胚抗原54.9ng/ml，细胞角蛋白19片段 5.54ng/ml，胃泌素释放肽前体80.2pg/ml；生化系列36项:白蛋白(溴甲酚绿法) 31.59g/L，镁0.72mmol/L，肌酐(酶法)55μmol/L，肌酸激酶31U/L；DIC系列-5项:纤维蛋白原5.47g/L，D-二聚体3.53mg/L；急查降钙素原、急查心梗三项、皮质醇(7:00-10:00am)、促肾上腺皮质激素(8时)、甲状腺功能3项、急查NT-proBNP、大便常规(粪沉渣)+潜血、尿液分析+尿沉渣未见明显异常。常规心电图检查(自动分析)：窦性心动过速；心脏超声检查(含左心功能测定)：主动脉瓣轻度反流，三尖瓣轻度反流；颅脑平扫+DWI+增强(3T)：1.双侧额顶叶及侧脑室旁白质内脱髓鞘改变。2.老年脑改变。3.部分副鼻窦炎；右侧乳突炎。4.鼻中隔偏曲，双下鼻甲肥大。颈部：左侧颈部淋巴结稍大，右侧颈部淋巴结可见；髂静脉及下肢深静脉、下肢浅静脉：左侧大隐静脉曲张，左侧隐股静脉瓣功能不全；腹部(包括盆腔)平扫(64排)：1.考虑肝多发囊肿、右肾囊肿，必要时增强扫描。2.双肾周桥隔略增厚。3.动脉粥样硬化。4.前列腺增大伴钙化。5.L5椎体前滑脱(I°)，双侧椎弓峡部裂。以上所见较2025-05-26CT变化不著。胸部平扫(64排-128层)：对比2025-05-26CT: 1.右肺下叶肺癌，较前略缩小、其内新见空洞影；右肺小叶间隔增厚，考虑癌性淋巴管炎可能；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜结节状增厚，较前变化不著；请结合临床。2.右侧液气胸，积液较前略增多，积气较前明显减少。3.左肺小结节，较前相仿，建议短期复查。4.右侧第7-9、12肋骨高密度影，较前密度增高，转移?建议ECT进一步检查。余所见大致同前。肋骨平扫+DWI+增强(3T)：1.右侧第7-9、12肋改变，成骨性转移?请结合其它影像学检查。2.右侧胸腔积液。3.肝内多发囊肿。排除禁忌，07-18行第5周期治疗：培美曲塞0.8gd1+顺铂注射液65mgd1、d2，联合信迪利单抗200mg抗肿瘤免疫治疗，并辅以激素、止吐、护胃、保肝等治疗，治疗结束后复查血常规未见明显骨髓抑制，针对肋骨异常请放疗科会诊后建议可考虑放疗，07-21出院。\n患者因“确诊肺腺癌4月，为继续治疗”2025-08-07第7次入院，入院后完善相关检查，急查血常规+CRP:血红蛋白109g/L，血小板总数205×10^9/L，白细胞4.58×10^9/L，中性粒细胞百分率70.9%，超敏C-反应蛋白17.43mg/L；超敏肌钙蛋白T14.80pg/ml；DIC系列-5项:纤维蛋白原5.27g/L，D-二聚体4.37mg/L；N端-B型钠尿肽前体71.5pg/ml；促肾上腺皮质激素(8时)：促肾上腺皮质激素(8时)31.7pg/ml；生化系列36项:白蛋白(溴甲酚绿法)33.34g/L，钾3.93mmol/L，钠140.1mmol/L，氯104.8mmol/L，尿素5.04mmol/L，肌酐(酶法)65μmol/L；皮质醇(7:00-10:00am)：皮质醇(7:00-10:00am)295nmol/L；甲状腺功能3项：促甲状腺素3.17mIU/L，游离甲状腺素13.6pmol/L，游离三碘甲状腺原氨酸4.46pmol/L；肺肿瘤检验：癌胚抗原52.6ng/ml，神经元特异性烯醇化酶20.4ng/ml，细胞角蛋白19片段4.81ng/ml，胃泌素释放肽前体92.9pg/ml。常规心电图检查(自动分析）：窦性心律，大致正常心电图。排除禁忌，于08-08给予第6周期化疗，方案为培美曲塞0.8g+顺铂注射液 65mg d1、d2，联合信迪利单抗200mg 免疫治疗，过程顺利，08-10行地舒单抗120mg抗骨转移治疗；复查血常规未见明显骨髓抑制，08-10出院。\n患者因“确诊肺腺癌4月，为继续治疗”于2025-08-28第8次入院，入院后完善辅助检查：胸部平扫：对比2025-07-18CT：1.右肺下叶肺癌，较前变化不著；右肺小叶间隔增厚，较前变化不著，考虑癌性淋巴管炎可能；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜结节状增厚，较前变化不著；请结合临床。2.右侧液气胸，积液较前变化不著，积气较前增多。3.左肺小结节，较前相仿，建议短期复查。4.右侧第7-9、12肋骨高密度影，较前变化不著，转移？建议ECT进一步检查。余所见大致同前。下腹部平扫：1.考虑右肾囊肿，较2025-07-18变化不著，必要时增强扫描。2.双肾周桥隔略增厚。3.动脉粥样硬化。上腹部平扫：考虑肝多发囊肿，较2025-07-18变化不明显，建议结合增强检查明确。盆腔平扫：1.前列腺增大伴钙化。2.L5椎体前滑脱（I°），双侧椎弓峡部裂。以上所见较2025-07-18变化不著。排除禁忌，给予培美曲塞 0.8g 联合信迪利单抗 200mg免疫治疗，并辅以激素、止吐、护胃、保肝等治疗，治疗过程顺利，患者病情稳定，2025-08-30出院。出院诊断：1.恶性肿瘤维持性化学治疗 2.恶性肿瘤免疫治疗 3.右肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转移 肺门淋巴结转移 胸膜转移 骨转移 4.恶性胸腔积液 5.大隐静脉曲张 6.肾囊肿 7.单纯性肝囊肿。\n患者因“确诊肺腺癌5月余，为继续治疗”于2025-10-06第9次入院，入院后完善辅助检查：急查血常规+CRP:血红蛋白 114g/L，血小板总数 212×10^9/L，白细胞7.30×10^9/L，中性粒细胞百分率 80.0%，超敏C-反应蛋白 16.04mg/L；皮质醇(7:00-10:00am):皮质醇(7:00-10:00am) 442nmol/L；促肾上腺皮质激素(8时):促肾上腺皮质激素(8时) 29.3pg/ml；甲状腺功能3项:促甲状腺素 4.94mIU/L，游离甲状腺素 14.4pmol/L，游离三碘甲状腺原氨酸 3.85pmol/L；生化系列36项:白蛋白(溴甲酚绿法) 36.10g/L，白蛋白:球蛋白 0.96，天门冬氨酸氨基转移酶 18U/L，丙氨酸氨基转移酶 8U/L，尿素 5.84mmol/L，肌酐(酶法) 78μmol/L；肺肿瘤检验-莱山:癌胚抗原 68.6ng/ml，细胞角蛋白19片段 9.45ng/ml，胃泌素释放肽前体 96.7pg/ml；DIC系列-5项:纤维蛋白原 5.04g/L，D-二聚体 3.28mg/L；急查NT-proBNP:N端-B型钠尿肽前体 50.1pg/ml；急查心梗三项:超敏肌钙蛋白T 14.00pg/ml，肌酸激酶-MB同工酶质量测定 0.54ng/ml，肌红蛋白 43.2ng/ml。排除禁忌，于2025-10-06给予本周期治疗，方案为培美曲塞 0.8g联合信迪利单抗200mg，并给予地舒单抗120mg治疗骨转移，2025-10-07办理出院。出院诊断：1.右肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转移 肺门淋巴结转移 胸膜转移 骨转移 2.恶性胸腔积液 3.大隐静脉曲张 4.肾囊肿 5.单纯性肝囊肿。\n患者因“确诊肺腺癌7月余，为继续治疗”于2025-11-07第10次入院，入院后完善相关检查：急查血常规+CRP:血红蛋白 115g/L，血小板总数 214×10^9/L，白细胞7.21×10^9/L，中性粒细胞百分率 82.3%，超敏C-反应蛋白 20.50mg/L；DIC系列-5项:纤维蛋白原 5.04g/L，D-二聚体 2.19mg/L；皮质醇(7:00-10:00am):皮质醇(7:00-10:00am) 286nmol/L；促肾上腺皮质激素(8时):促肾上腺皮质激素(8时)23.3pg/ml；急查心梗三项:超敏肌钙蛋白T 17.70pg/ml；肺肿瘤检验-莱山:癌胚抗原 75.8ng/ml，细胞角蛋白19片段 12.4ng/ml，胃泌素释放肽前体 90.5pg/ml；生化系列36项:白蛋白(溴甲酚绿法) 32.49g/L，脂蛋白(a)343mg/L，唾液酸 769mg/L；N端-B型钠尿肽前体、甲状腺功能3项未见异常。常规心电图检查：窦性心动过速。全身骨显像：与本院2025-04-10骨显像比较：1.右侧多根肋骨多发异常放射性浓聚灶，病灶数目较前增多，浓聚程度增高，提示骨转移瘤可能大，请结合其他检查综合考虑；2.前次检查所示左侧坐骨轻度放射性浓聚灶，本次检查未见显示；3.双肩关节及双膝关节区异常放射性浓聚，考虑炎性病变，请结合临床。颅脑平扫+DWI+增强+薄层：1.双侧额顶叶及侧脑室旁白质内脱髓鞘改变；2.老年脑改变，双侧额颞部少量硬膜下积液；3.部分副鼻窦炎；右侧乳突炎；4.鼻中隔偏曲，双下鼻甲肥大。心脏超声检查（含左心功能测定）：静息状态下：心内结构及血流未见明显异常髂静脉及下肢深静脉(双侧)：双侧髂静脉及下肢深静脉血流通畅颈部：双侧颈部未见明显增大淋巴结胸部平扫+增强：对比2025-08-28CT：1.右肺下叶肺癌，较前增大；右肺小叶间隔增厚，较前略进展，考虑癌性淋巴管炎可能；纵隔及双肺门淋巴结，部分较前略增大；考虑右侧胸膜转移，较前明显进展，累及邻近右前胸壁及右侧膈肌可能；请结合临床并复查；2.右侧胸腔积液，较前变化不著，原右侧胸腔积气吸收；3.左肺小结节，部分较前略增大（如下叶薄层img231、243），部分结节较前相仿，建议短期复查；4.右侧第7-9、12肋骨高密度影，较前变化不著，转移？建议ECT进一步检查；余所见大致同前。上腹部平扫+增强：考虑肝多发囊肿，较2025-08-28变化不明显。下腹部平扫+增强：1.考虑右肾囊肿，较2025-08-28变化不���；2.双肾周桥隔略增厚；3.动脉粥样硬化。排除禁忌给予本周期治疗，方案为培美曲塞0.8g、信迪利单抗200mg联合恩度 210mg q21d治疗。治疗结束，患者病情稳定，2025-11-14办理出院。出院诊断：1.右肺腺癌(T2bN3M1 IV期) 纵隔淋巴结转移 肺门淋巴结转移 胸膜转移 骨转移 2.恶性胸腔积液 3.大隐静脉曲张 4.肾囊肿 5.肝囊肿\n患者因“确诊肺腺癌8月余，为继续治疗”于2026-01-08再入院，入院后完善相关辅助检查：01-08：急查NT-proBNP、促肾上腺皮质激素(8时)、皮质醇(7:00-10:00am)等未见明显异常。急查血常规+CRP+SAA:红细胞 3.93x10^12/L，血红蛋白 118g/L，红细胞压积35.8%，红细胞分布宽度SD 47.4fl，中性粒细胞百分率 77.9%，淋巴细胞百分率 9.4%，单核细胞百分率 10.2%，淋巴细胞绝对值 0.67×10^9/L，单核细胞绝对值 0.73×10^9/L，超敏C-反应蛋白 30.56mg/L，血清淀粉样蛋白A 26.98mg/L；急查心梗三项:超敏肌钙蛋白T 15.10pg/ml；DIC系列-5项:纤维蛋白原 6.22g/L，D-二聚体 1.66mg/L；急查降钙素原：0.0969ng/ml；生化系列36项:白蛋白(溴甲酚绿法) 31.69g/L，白蛋白:球蛋白 0.87，肾小球滤过率 89.97ml/(min·1.73m²)，肌酸激酶 38U/L，脂蛋白(a) 452mg/L，唾液酸 765mg/L；甲状腺功能6项:促甲状腺素 4.69mIU/L；肺肿瘤检验癌胚抗原 73.4ng/ml，神经元特异性烯醇化酶 18.4ng/ml，细胞角蛋白19片段 19.1ng/ml，胃泌素释放肽前体81.4pg/ml；常规心电图检查（自动分析）：窦性心动过速。下腹部平扫+增强：1.考虑右肾囊肿，较2025-11-08变化不著。2.双肾周桥隔略增厚。3.动脉粥样硬化。上腹部平扫+增强：考虑肝多发囊肿，较2025-11-08变化不明显。胸部平扫+增强：对比2025-11-08CT：1.右肺下叶肺癌，范围整体较前增大；右肺小叶间隔增厚，较前进展，考虑癌性淋巴管炎可能；纵隔及双肺门淋巴结大致同前；考虑右侧胸膜转移，较前进展，累及邻近右前胸壁及右侧膈肌可能；请结合临床并复查。2.右侧胸腔积液，较前变化不著。3.左肺小结节，较前相仿，建议短期复查。4.右侧第7-9、12肋骨高密度影，局部略进展，转移可能，建议ECT进一步检查。余所见大致同前。01-09：髂静脉及下肢深静脉、下肢浅静脉：左侧大隐静脉曲张左侧隐股静脉瓣功能不全。01-10：心脏超声检查（含左心功能测定）：静息状态下：心内结构及血流未见明显异常。考虑患者肿瘤较前进展，请肿瘤科及放疗科会诊，给予更换二线化疗方案，排除禁忌，1-09行开始给予恩度抗血管生成，01-12给予二线第1周期全身化疗：白蛋白紫杉醇300mg d1、信迪利单抗200mg，01-13给予地舒单抗120mg抗骨转移。期间联合护肝、护胃、止吐、激素等治疗，现病情平稳，准予出院。末次出院诊断：1.右肺腺癌（T2bN3M1 IV期）纵隔淋巴结转移肺门淋巴结转移胸膜转移骨转移2.恶性胸腔积液3.大隐静脉曲张4.肾囊肿5.肝囊肿6.贫血7.低蛋白血症\n患者出院后规律服药、门诊复诊，偶有咳嗽，咳白薄痰，腰肋部水肿，于2026-2-10再入院，入院后完善辅助检查：NT-proBNP未见明显异常；血常规+CRP+SAA：红细胞4.25x10^12/L，血红蛋白125g/L，红细胞压积38.4%，红细胞分布宽度SD47.8fl，中性粒细胞百分率83.4%，淋巴细胞百分率8.0%，中性粒细胞绝对值7.35×10^9/L，淋巴细胞绝对值0.70×10^9/L，单核细胞绝对值0.62×10^9/L，超敏C-反应蛋白24.16mg/L，血清淀粉样蛋白A13.13mg/L；心梗三项：超敏肌钙蛋白T14.10pg/ml；降钙素原：0.0528ng/ml；生化系列36项：白蛋白（溴甲酚绿法）34.82g/L，白蛋白：球蛋白1.02，肾小球滤过率89.97ml/(min•1.73m²)，肌酸激酶33U/L，脂蛋白(a)510mg/L，唾液酸792mg/L；肺肿瘤检验：癌胚抗原100ng/ml，神经元特异性烯醇化酶31.1ng/ml，细胞角蛋白19片段28.8ng/ml，胃泌素释放肽前体87.7pg/ml；DIC系列-5项：纤维蛋白原6.71g/L，D-二聚体1.42mg/L；心电图：窦性心律大致正常心电图。尿液分析、大便常规及潜血、促肾上腺皮质激素(8时)、皮质醇(7:00-10:00am)、甲状腺功能6项等未见明显异常。排除禁忌，02-10开始给予恩度抗血管生成，02-11给予二线第2周期全身化疗：白蛋白紫杉醇300mg d1，同时辅以激素、止吐、护胃、保肝治疗，同时给予信迪利单抗200mg抗肿瘤免疫治疗，02-12给予地舒单抗120mg抗骨转移治疗。于2026-02-13出院。末次出院诊断：1.恶性肿瘤维持性化学治疗2.恶性肿瘤免疫治疗3.恶性肿瘤靶向治疗4.右肺腺癌（T2bN3M1 IV期）纵隔淋巴结转移肺门淋巴结转移胸膜转移骨转移5.恶性胸腔积液6.大隐静脉曲张7.肾囊肿8.肝囊肿。\n患者出院后规律门诊复诊，偶有咳嗽、咳痰，2天前无明显诱因出现咯血，感痰较前增多，每天数十口，色鲜红，今为进一步治疗入院。患者病后神志清，精神状态一般，食欲一般，睡眠良好，大便正常，小便正常，体力情况一般，体重无明显变化。",
  "pmh_disease_history": [
    "肺腺癌",
    "大隐静脉曲张",
    "肾囊肿",
    "肝囊肿",
    "贫血",
    "低蛋白血症"
  ],
  "pmh_allergy_history": [
    "否认食物、药物过敏史"
  ],
  "pmh_surgery_trauma_history": [
    "右侧胸腔引流术"
  ],
  "ph_smoking": null,
  "ph_drinking": null,
  "oh_menarche_age": null,
  "oh_menopause_age": null,
  "oh_pregnancies": null,
  "fh_text": "参阅既往入院记录。",
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36.3,
  "vs_pulse_bpm": 107,
  "vs_respiration_rpm": 21,
  "vs_systolic_bp_mmhg": 144,
  "vs_diastolic_bp_mmhg": 99,
  "pe_general_condition": "发育正常，营养良好，正常面容，表情自如，自主体位，神志清楚，查体合作。",
  "pe_skin_mucosa": "全身皮肤粘膜无黄染，无皮疹，无皮下出血，无皮下结节，皮下无水肿，无肝掌、蜘蛛痣，毛发分布均匀。",
  "pe_lymph_nodes": "全身浅表淋巴结无肿大。",
  "pe_lungs": "胸廓无畸形，呼吸运动两侧对称，肋间隙无狭窄或饱满，胸壁无压痛，语颤无增强、减弱，胸骨无压痛。双肺叩诊清音，呼吸规整，双肺呼吸音低，未闻及干湿性啰音，无胸膜摩擦音。",
  "pe_heart": "心前区无异常隆起、异常搏动、震颤，心浊音界不大，心率107次/分，律齐，心音有力，各瓣膜听诊区未闻及杂音，无心包摩擦音。",
  "pe_abdomen": "腹平坦，软，无压痛、反跳痛，腹部无包块。肝脏未触及，脾脏未触及，Murphy氏征阴性，肾区无叩击痛，无移动性浊音。肠鸣音正常，4次/分。",
  "pe_extremities": "脊柱正常生理弯曲，四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾），关节无肿胀、压痛，下肢无浮肿。肌肉无压痛，四肢肌力、肌张力未见异常，双侧肱二、三头肌腱反射正常，双侧膝、跟腱反射正常。",
  "pe_nervous_system": "双侧Babinski征阴性。",
  "pe_specialist_exam": "胸廓无畸形，呼吸运动两侧对称，肋间隙无狭窄或饱满，胸壁无压痛，语颤无增强、减弱，胸骨无压痛。双肺叩诊清音，呼吸规整，双肺呼吸音低，未闻及干湿性啰音，无胸膜摩擦音。",
  "pe_ecog_score": null,
  "pat_text": "2025-04-09 病理: (胸膜活检)送检增生的纤维组织内见腺癌浸润，请结合临床诊治。免疫组化：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（部分+）、P40（点灶+）、CR（灶+）、ALK（1A4）（-）、Ki67(+,40%)。C-MET免疫组化检测报告检测平台：Roche Ventana Benchmark Ultra；抗体克隆号：SP44,Roche；表达部位：细胞膜和细胞浆；阳性强度及百分比：++(40%),+(60%)阳性等级：1+ 细胞数量：≥100。",
  "pat_items": [
    "2025-04-09 病理: (胸膜活检)送检增生的纤维组织内见腺癌浸润，请结合临床诊治。免疫组化：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（部分+）、P40（点灶+）、CR（灶+）、ALK（1A4）（-）、Ki67(+,40%)。C-MET免疫组化检测报告检测平台：Roche Ventana Benchmark Ultra；抗体克隆号：SP44,Roche；表达部位：细胞膜和细胞浆；阳性强度及百分比：++(40%),+(60%)阳性等级：1+ 细胞数量：≥100。"
  ],
  "preliminary_diagnoses": [
    {
      "name": "咯血",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "右肺腺癌（T2bN3M1 IV期）纵隔淋巴结转移肺门淋巴结转移胸膜转移骨转移",
      "diagnosis_type": "西医",
      "is_primary": true
    },
    {
      "name": "恶性胸腔积液",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "大隐静脉曲张",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "肾囊肿",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "肝囊肿",
      "diagnosis_type": "西医",
      "is_primary": false
    }
  ],
  "department": null
}
2026-08-10 18:21:39,672 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-03-11]
2026-08-10 18:21:39,678 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1781804, prompt_len=2095
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共38行）
["性别：男", "婚姻：已婚", "年龄：69岁", "入院日期：2026-03-11 08:04", "民族：汉族", "记录日期：2026-03-11 08:06", "职业：农民", "病史陈述者：患者本人", "主诉：确诊肺腺癌10月余，咯血2天余。", "现病史：患者因“呼吸困难2月余”于2025-04-05第1次入院，入院后完善检验检查：", "CEA(胸水)：癌胚抗原 538ng/ml；于04-07完善胸腔镜检查：镜下诊断：胸腔积液，胸壁结节", "样改变。病理：（胸膜活检）送检增生的纤维组织内见腺癌浸润，请结合临床诊治。免疫组", "化：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（部分+）、P40（点灶+）、CR（灶", "+）、ALK（1A4）（-）、Ki67（+，40%）。完善评估检查：胸部增强(64排-128层)：1.符合", "右侧胸腔引流术后改变，右侧液气胸并右侧颈根部及胸壁积气，肺组织压缩约70%。2.右肺", "下叶占位，考虑肺癌并纵隔及双肺门淋巴结转移可能，右侧胸膜结节状增厚、强化，考虑转", "移，请结合临床。3.左肺小结节，目前考虑良性，建议短期复查。4.双肺慢性炎症/纤维", "灶。5.动脉粥样硬化表现。6.甲状腺改变，请结合超声检查。7.右侧第8肋骨质改变，请结", "合临床。全身骨显像：1.右侧第6-8侧肋异常放射性浓聚，本院CT（2025-04-09）第6、7肋", "骨未见明显骨质异常，第8肋髓腔内见局灶高密度影，建议短期CT复查。2.左侧坐骨轻度放", "射性浓聚灶，本院CT未见明显骨质破坏，建议随诊。04-14复查胸部CT：对比2025-04-09", "CT：1.符合右侧胸腔引流术后改变，右侧液气胸并右侧颈根部及胸壁积气，较前减轻，肺组", "织压缩约30%。2.右肺下叶占位，较前相仿，考虑肺癌；纵隔及双肺门淋巴结同前；右侧胸", "膜结节状增厚，较前局部稍减轻，请结合临床。3.左肺小结节，较前相仿，建议短期复查。", "余所见大致同前。04-16复查胸片：1.右侧胸腔引流术后表现，对比2025-04-11X线：右侧气", "胸较前明显减少；原右侧胸壁及胸壁皮下积气基本消失；右侧胸腔积液较前减少，建议复查", "或结合CT检查。2.右肺下野占位，请结合临床及CT检查。患者完善基因检测未见基因突变，", "于04-17给予第1周期全身化疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2 q21d，同时辅", "以止吐、护胃、保肝、激素减轻化疗不良反应等治疗。于04-19给予信迪利单抗200mg抗肿瘤", "免疫治疗。患者化疗顺利，准予出院。末次出院诊断：1.肺腺癌伴纵隔淋巴结、肺门淋巴", "结、胸膜转移（T2bN3M1 IV期）恶性胸腔积液 2.气胸 3.左侧大隐静脉曲张 4.肝囊肿 5.双", "肾囊肿 6.前列腺稍大伴钙化", "患者因“确诊肺腺癌1月”于2025-05-07第2次入院，入院后完善相关检查：肺肿瘤检", "验：癌胚抗原 62.1ng/ml，神经元特异性烯醇化酶 19.8ng/ml，细胞角蛋白19片段", "6.21ng/ml；大便常规：未见异常；髂静脉及下肢深静脉、下肢浅静脉：左侧大隐静脉曲张，", "左侧隐股静脉瓣功能不全；胸部平扫(64排-128层)：对比2025-04-14CT：1.符合右侧胸腔引", "流术后改变，右侧液气胸，积液较前增多，积气较前减少；原右侧颈根部及胸壁少量积气本", "第1页"]

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
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord API raw response (len=3039):
[
	{"text": "性别：男", "bbox": [225, 88, 284, 99]},
	{"text": "婚姻：已婚", "bbox": [494, 88, 565, 99]},
	{"text": "年龄：69岁", "bbox": [225, 100, 297, 111]},
	{"text": "入院日期：2026-03-11 08:04", "bbox": [494, 100, 679, 111]},
	{"text": "民族：汉族", "bbox": [225, 112, 297, 123]},
	{"text": "记录日期：2026-03-11 08:06", "bbox": [494, 112, 679, 123]},
	{"text": "职业：农民", "bbox": [225, 124, 297, 135]},
	{"text": "病史陈述者：患者本人", "bbox": [494, 124, 638, 135]},
	{"text": "主诉：确诊肺腺癌10月余，咯血2天余。", "bbox": [225, 137, 488, 148]},
	{"text": "现病史：患者因“呼吸困难2月余”于2025-04-05第1次入院，入院后完善检验检查：", "bbox": [222, 150, 751, 161]},
	{"text": "CEA(胸水)：癌胚抗原 538ng/ml；于04-07完善胸腔镜检查：镜下诊断：胸腔积液，胸壁结节", "bbox": [190, 163, 774, 174]},
	{"text": "样改变。病理：（胸膜活检）送检增生的纤维组织内见腺癌浸润，请结合临床诊治。免疫组", "bbox": [190, 176, 775, 187]},
	{"text": "化：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（部分+）、P40（点灶+）、CR（灶", "bbox": [190, 189, 748, 200]},
	{"text": "+）、ALK（1A4）（-）、Ki67（+，40%）。完善评估检查：胸部增强(64排-128层)：1.符合", "bbox": [190, 202, 771, 213]},
	{"text": "右侧胸腔引流术后改变，右侧液气胸并右侧颈根部及胸壁积气，肺组织压缩约70%。2.右肺", "bbox": [190, 215, 772, 226]},
	{"text": "下叶占位，考虑肺癌并纵隔及双肺门淋巴结转移可能，右侧胸膜结节状增厚、强化，考虑转", "bbox": [190, 228, 780, 240]},
	{"text": "移，请结合临床。3.左肺小结节，目前考虑良性，建议短期复查。4.双肺慢性炎症/纤维", "bbox": [188, 241, 761, 253]},
	{"text": "灶。5.动脉粥样硬化表现。6.甲状腺改变，请结合超声检查。7.右侧第8肋骨质改变，请结", "bbox": [188, 254, 777, 266]},
	{"text": "合临床。全身骨显像：1.右侧第6-8侧肋异常放射性浓聚，本院CT（2025-04-09）第6、7肋", "bbox": [188, 268, 777, 280]},
	{"text": "骨未见明显骨质异常，第8肋髓腔内见局灶高密度影，建议短期CT复查。2.左侧坐骨轻度放", "bbox": [185, 281, 780, 293]},
	{"text": "射性浓聚灶，本院CT未见明显骨质破坏，建议随诊。04-14复查胸部CT：对比2025-04-09", "bbox": [185, 295, 760, 307]},
	{"text": "CT：1.符合右侧胸腔引流术后改变，右侧液气胸并右侧颈根部及胸壁积气，较前减轻，肺组", "bbox": [182, 308, 790, 320]},
	{"text": "织压缩约30%。2.右肺下叶占位，较前相仿，考虑肺癌；纵隔及双肺门淋巴结同前；右侧胸", "bbox": [182, 321, 785, 333]},
	{"text": "膜结节状增厚，较前局部稍减轻，请结合临床。3.左肺小结节，较前相仿，建议短期复查。", "bbox": [182, 335, 787, 347]},
	{"text": "余所见大致同前。04-16复查胸片：1.右侧胸腔引流术后表现，对比2025-04-11X线：右侧气", "bbox": [180, 349, 796, 361]},
	{"text": "胸较前明显减少；原右侧胸壁及胸壁皮下积气基本消失；右侧胸腔积液较前减少，建议复查", "bbox": [180, 363, 797, 375]},
	{"text": "或结合CT检查。2.右肺下野占位，请结合临床及CT检查。患者完善基因检测未见基因突变，", "bbox": [178, 377, 790, 389]},
	{"text": "于04-17给予第1周期全身化疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2 q21d，同时辅", "bbox": [178, 391, 800, 403]},
	{"text": "以止吐、护胃、保肝、激素减轻化疗不良反应等治疗。于04-19给予信迪利单抗200mg抗肿瘤", "bbox": [178, 405, 801, 417]},
	{"text": "免疫治疗。患者化疗顺利，准予出院。末次出院诊断：1.肺腺癌伴纵隔淋巴结、肺门淋巴", "bbox": [176, 419, 790, 431]},
	{"text": "结、胸膜转移（T2bN3M1 IV期）恶性胸腔积液 2.气胸 3.左侧大隐静脉曲张 4.肝囊肿 5.双", "bbox": [175, 433, 806, 445]},
	{"text": "肾囊肿 6.前列腺稍大伴钙化", "bbox": [175, 458, 377, 471]},
	{"text": "患者因“确诊肺腺癌1月”于2025-05-07第2次入院，入院后完善相关检查：肺肿瘤检", "bbox": [207, 468, 792, 484]},
	{"text": "验：癌胚抗原 62.1ng/ml，神经元特异性烯醇化酶 19.8ng/ml，细胞角蛋白19片段", "bbox": [175, 484, 739, 500]},
	{"text": "6.21ng/ml；大便常规：未见异常；髂静脉及下肢深静脉、下肢浅静脉：左侧大隐静脉曲张，", "bbox": [175, 498, 800, 514]},
	{"text": "左侧隐股静脉瓣功能不全；胸部平扫(64排-128层)：对比2025-04-14CT：1.符合右侧胸腔引", "bbox": [175, 512, 808, 528]},
	{"text": "流术后改变，右侧液气胸，积液较前增多，积气较前减少；原右侧颈根部及胸壁少量积气本", "bbox": [175, 526, 809, 543]},
	{"text": "第1页", "bbox": [474, 560, 523, 571]}
]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord API: raw_items=38, valid_items=38, elapsed=18.7s
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[0]: text=性别：男, bbox=[225, 88, 284, 99]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[1]: text=婚姻：已婚, bbox=[494, 88, 565, 99]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：69岁, bbox=[225, 100, 297, 111]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[3]: text=入院日期：2026-03-11 08:04, bbox=[494, 100, 679, 111]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[4]: text=民族：汉族, bbox=[225, 112, 297, 123]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[5]: text=记录日期：2026-03-11 08:06, bbox=[494, 112, 679, 123]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[6]: text=职业：农民, bbox=[225, 124, 297, 135]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[7]: text=病史陈述者：患者本人, bbox=[494, 124, 638, 135]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[8]: text=主诉：确诊肺腺癌10月余，咯血2天余。, bbox=[225, 137, 488, 148]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[9]: text=现病史：患者因“呼吸困难2月余”于2025-04-05第1次入院，入院后完善检验检查：, bbox=[222, 150, 751, 161]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[10]: text=CEA(胸水)：癌胚抗原 538ng/ml；于04-07完善胸腔镜检查：镜下诊断：胸腔积液，胸壁结节, bbox=[190, 163, 774, 174]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[11]: text=样改变。病理：（胸膜活检）送检增生的纤维组织内见腺癌浸润，请结合临床诊治。免疫组, bbox=[190, 176, 775, 187]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[12]: text=化：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（部分+）、P40（点灶+）、CR（灶, bbox=[190, 189, 748, 200]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[13]: text=+）、ALK（1A4）（-）、Ki67（+，40%）。完善评估检查：胸部增强(64排-128层)：1.符合, bbox=[190, 202, 771, 213]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[14]: text=右侧胸腔引流术后改变，右侧液气胸并右侧颈根部及胸壁积气，肺组织压缩约70%。2.右肺, bbox=[190, 215, 772, 226]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[15]: text=下叶占位，考虑肺癌并纵隔及双肺门淋巴结转移可能，右侧胸膜结节状增厚、强化，考虑转, bbox=[190, 228, 780, 240]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[16]: text=移，请结合临床。3.左肺小结节，目前考虑良性，建议短期复查。4.双肺慢性炎症/纤维, bbox=[188, 241, 761, 253]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[17]: text=灶。5.动脉粥样硬化表现。6.甲状腺改变，请结合超声检查。7.右侧第8肋骨质改变，请结, bbox=[188, 254, 777, 266]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[18]: text=合临床。全身骨显像：1.右侧第6-8侧肋异常放射性浓聚，本院CT（2025-04-09）第6、7肋, bbox=[188, 268, 777, 280]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[19]: text=骨未见明显骨质异常，第8肋髓腔内见局灶高密度影，建议短期CT复查。2.左侧坐骨轻度放, bbox=[185, 281, 780, 293]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[20]: text=射性浓聚灶，本院CT未见明显骨质破坏，建议随诊。04-14复查胸部CT：对比2025-04-09, bbox=[185, 295, 760, 307]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[21]: text=CT：1.符合右侧胸腔引流术后改变，右侧液气胸并右侧颈根部及胸壁积气，较前减轻，肺组, bbox=[182, 308, 790, 320]
2026-08-10 18:21:58,329 INFO     29 [qwen-vl-text] coord item[22]: text=织压缩约30%。2.右肺下叶占位，较前相仿，考虑肺癌；纵隔及双肺门淋巴结同前；右侧胸, bbox=[182, 321, 785, 333]
2026-08-10 18:21:58,330 INFO     29 [qwen-vl-text] coord item[23]: text=膜结节状增厚，较前局部稍减轻，请结合临床。3.左肺小结节，较前相仿，建议短期复查。, bbox=[182, 335, 787, 347]
2026-08-10 18:21:58,330 INFO     29 [qwen-vl-text] coord item[24]: text=余所见大致同前。04-16复查胸片：1.右侧胸腔引流术后表现，对比2025-04-11X线：右侧气, bbox=[180, 349, 796, 361]
2026-08-10 18:21:58,330 INFO     29 [qwen-vl-text] coord item[25]: text=胸较前明显减少；原右侧胸壁及胸壁皮下积气基本消失；右侧胸腔积液较前减少，建议复查, bbox=[180, 363, 797, 375]
2026-08-10 18:21:58,330 INFO     29 [qwen-vl-text] coord item[26]: text=或结合CT检查。2.右肺下野占位，请结合临床及CT检查。患者完善基因检测未见基因突变，, bbox=[178, 377, 790, 389]
2026-08-10 18:21:58,330 INFO     29 [qwen-vl-text] coord item[27]: text=于04-17给予第1周期全身化疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2 q21d，同时辅, bbox=[178, 391, 800, 403]
2026-08-10 18:21:58,330 INFO     29 [qwen-vl-text] coord item[28]: text=以止吐、护胃、保肝、激素减轻化疗不良反应等治疗。于04-19给予信迪利单抗200mg抗肿瘤, bbox=[178, 405, 801, 417]
2026-08-10 18:21:58,330 INFO     29 [qwen-vl-text] coord item[29]: text=免疫治疗。患者化疗顺利，准予出院。末次出院诊断：1.肺腺癌伴纵隔淋巴结、肺门淋巴, bbox=[176, 419, 790, 431]
2026-08-10 18:21:58,330 INFO     29 [qwen-vl-text] coord item[30]: text=结、胸膜转移（T2bN3M1 IV期）恶性胸腔积液 2.气胸 3.左侧大隐静脉曲张 4.肝囊肿 5.双, bbox=[175, 433, 806, 445]
2026-08-10 18:21:58,330 INFO     29 [qwen-vl-text] coord item[31]: text=肾囊肿 6.前列腺稍大伴钙化, bbox=[175, 458, 377, 471]
2026-08-10 18:21:58,330 INFO     29 [qwen-vl-text] coord item[32]: text=患者因“确诊肺腺癌1月”于2025-05-07第2次入院，入院后完善相关检查：肺肿瘤检, bbox=[207, 468, 792, 484]
2026-08-10 18:21:58,330 INFO     29 [qwen-vl-text] coord item[33]: text=验：癌胚抗原 62.1ng/ml，神经元特异性烯醇化酶 19.8ng/ml，细胞角蛋白19片段, bbox=[175, 484, 739, 500]
2026-08-10 18:21:58,330 INFO     29 [qwen-vl-text] coord item[34]: text=6.21ng/ml；大便常规：未见异常；髂静脉及下肢深静脉、下肢浅静脉：左侧大隐静脉曲张，, bbox=[175, 498, 800, 514]
2026-08-10 18:21:58,330 INFO     29 [qwen-vl-text] coord item[35]: text=左侧隐股静脉瓣功能不全；胸部平扫(64排-128层)：对比2025-04-14CT：1.符合右侧胸腔引, bbox=[175, 512, 808, 528]
2026-08-10 18:21:58,330 INFO     29 [qwen-vl-text] coord item[36]: text=流术后改变，右侧液气胸，积液较前增多，积气较前减少；原右侧颈根部及胸壁少量积气本, bbox=[175, 526, 809, 543]
2026-08-10 18:21:58,330 INFO     29 [qwen-vl-text] coord item[37]: text=第1页, bbox=[474, 560, 523, 571]
2026-08-10 18:21:58,330 INFO     29 [qwen-vl-text] page=0 — 38/38 coords, api_time=18.7s
2026-08-10 18:21:58,332 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2054929, prompt_len=2279
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共36行）
["次吸收。2.右肺下叶占位，较前略缩小，考虑肺癌；纵隔及双肺门淋巴结部分较前略增大；", "右侧胸膜结节状增厚，较前局部稍减轻，请结合临床。3.左肺小结节，较前相仿，建议短期", "复查。余所见大致同前。入院后于05-09拔除胸腔引流管。排除禁忌于05-09行第2周期全身", "化疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2 q21d，并辅以激素、止吐、护胃、保肝", "等治疗，05-10给予信迪利单抗200mg肿瘤免疫治疗。患者治疗结束，于2025-05-11出院。", "患者因“确诊肺腺癌1月余，发热5天”于2025-05-19第3次入院，入院后完善检验检", "查：大便菌群分析:细菌总数600 个/油镜视野（参考值500～5000个），革兰阳性球菌少量，", "革兰阴性杆菌少量，酵母样真菌孢子+，酵母样真菌菌丝+；艰难梭菌毒素A/B检测:艰难梭", "菌毒素A/B检测 0.02；大便细菌培养+药敏:经两天普通培养，鉴定生长热带念珠菌+++，无", "肠球菌生长，无肠杆菌生长，无沙门氏菌、志贺氏菌生长。痰细菌学检查:经2天普通培养，", "经鉴定为正常菌群生长，无流感嗜血杆菌生长。胸部平扫(64排-128层)：对比", "2025-04-14CT：1.符合右侧胸腔引流术后改变，右侧液气胸，积液较前增多，积气较前减", "少；原右侧颈根部及胸壁少量积气本次吸收。2.右肺下叶占位，较前略缩小，考虑肺癌；纵", "隔及双肺门淋巴结部分较前略增大；右侧胸膜结节状增厚，较前局部稍减轻，请结合临床。", "3.左肺小结节，较前相仿，建议短期复查。余所见大致同前。腹部（包括盆腔）平扫(64", "排)：1.考虑肝多发囊肿、右肾囊肿，必要时增强扫描。2.双肾周桥隔略增厚。3.动脉粥样", "硬化。4.前列腺增大伴钙化。5.L5椎体前滑脱（I°），双侧椎弓峡部裂。胸部平扫(64排", "-128层)：对比2025-05-08CT：1.右侧液气胸，积液较前增多，积气较前减少。2.右肺下叶", "占位，较前缩小，考虑肺癌；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜结节状增", "厚，较前变化不著，请结合临床。3.左肺小结节，较前相仿，建议短期复查。余所见大致同", "前。入院后给予哌拉西林他唑巴坦抗感染，蒙脱石散止泻，枯草杆菌二联活菌胶囊调整消化", "道菌群，利伐沙班抗凝，制霉素片口服治疗，现患者病情稳定，于2025-05-29出院。", "患者因“确诊肺腺癌2月余。”第4次入院，入院后完善辅助检查，入院后排除禁忌，", "06-06行第3周期治疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2，联合信迪利单抗200mg", "抗肿瘤免疫治疗，并辅以激素、止吐、护胃、保肝等治疗，治疗结束后复查血常规未见明显", "骨髓抑制，于2025-06-08出院。末次出院诊断：1.恶性肿瘤维持性化学治疗 2.恶性肿瘤免", "疫治疗 3.肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转移 肺门淋巴结转移 胸膜转移 恶性胸腔", "积液 4.大隐静脉曲张 5.肾囊肿 6.单纯性肝囊肿。", "患者因“确诊肺腺癌2月余，为继续治疗”于2025-06-26第5次入院，入院后完善相关检", "查，排除禁忌，06-27行第4周期治疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2，联合", "信迪利单抗200mg抗肿瘤免疫治疗，并辅以激素、止吐、护胃、保肝等治疗，治疗结束后复", "查血常规未见明显骨髓抑制，于2025-06-29出院。末次出院诊断：1.恶性肿瘤维持性化学治", "疗 2.恶性肿瘤免疫治疗 3.肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转移 肺门淋巴结转移 胸", "膜转移 4.恶性胸腔积液 5.大隐静脉曲张 6.肾囊肿 7.单纯性肝囊肿.", "患者因“确诊肺腺癌3月余，为继续治疗”2025-07-17入院，入院后完善相关必要辅助", "第2页"]

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
2026-08-10 18:22:15,805 INFO     29 [qwen-vl-text] coord API raw response (len=3144):
[
	{"text": "次吸收。2.右肺下叶占位，较前略缩小，考虑肺癌；纵隔及双肺门淋巴结部分较前略增大；", "bbox": [180, 88, 770, 100]},
	{"text": "右侧胸膜结节状增厚，较前局部稍减轻，请结合临床。3.左肺小结节，较前相仿，建议短期", "bbox": [180, 100, 780, 113]},
	{"text": "复查。余所见大致同前。入院后于05-09拔除胸腔引流管。排除禁忌于05-09行第2周期全身", "bbox": [180, 113, 774, 126]},
	{"text": "化疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2 q21d，并辅以激素、止吐、护胃、保肝", "bbox": [180, 126, 783, 139]},
	{"text": "等治疗，05-10给予信迪利单抗200mg肿瘤免疫治疗。患者治疗结束，于2025-05-11出院。", "bbox": [178, 139, 763, 152]},
	{"text": "患者因“确诊肺腺癌1月余，发热5天”于2025-05-19第3次入院，入院后完善检验检", "bbox": [206, 152, 763, 165]},
	{"text": "查：大便菌群分析:细菌总数600 个/油镜视野（参考值500～5000个），革兰阳性球菌少量，", "bbox": [178, 165, 785, 178]},
	{"text": "革兰阴性杆菌少量，酵母样真菌孢子+，酵母样真菌菌丝+；艰难梭菌毒素A/B检测:艰难梭", "bbox": [180, 178, 783, 191]},
	{"text": "菌毒素A/B检测 0.02；大便细菌培养+药敏:经两天普通培养，鉴定生长热带念珠菌+++，无", "bbox": [175, 191, 792, 204]},
	{"text": "肠球菌生长，无肠杆菌生长，无沙门氏菌、志贺氏菌生长。痰细菌学检查:经2天普通培养，", "bbox": [173, 204, 785, 217]},
	{"text": "经鉴定为正常菌群生长，无流感嗜血杆菌生长。胸部平扫(64排-128层)：对比", "bbox": [172, 217, 702, 231]},
	{"text": "2025-04-14CT：1.符合右侧胸腔引流术后改变，右侧液气胸，积液较前增多，积气较前减", "bbox": [171, 231, 782, 245]},
	{"text": "少；原右侧颈根部及胸壁少量积气本次吸收。2.右肺下叶占位，较前略缩小，考虑肺癌；纵", "bbox": [170, 245, 799, 259]},
	{"text": "隔及双肺门淋巴结部分较前略增大；右侧胸膜结节状增厚，较前局部稍减轻，请结合临床。", "bbox": [169, 259, 794, 273]},
	{"text": "3.左肺小结节，较前相仿，建议短期复查。余所见大致同前。腹部（包括盆腔）平扫(64", "bbox": [167, 273, 780, 287]},
	{"text": "排)：1.考虑肝多发囊肿、右肾囊肿，必要时增强扫描。2.双肾周桥隔略增厚。3.动脉粥样", "bbox": [167, 287, 797, 301]},
	{"text": "硬化。4.前列腺增大伴钙化。5.L5椎体前滑脱（I°），双侧椎弓峡部裂。胸部平扫(64排", "bbox": [165, 301, 791, 315]},
	{"text": "-128层)：对比2025-05-08CT：1.右侧液气胸，积液较前增多，积气较前减少。2.右肺下叶", "bbox": [164, 315, 800, 329]},
	{"text": "占位，较前缩小，考虑肺癌；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜结节状增", "bbox": [163, 330, 795, 344]},
	{"text": "厚，较前变化不著，请结合临床。3.左肺小结节，较前相仿，建议短期复查。余所见大致同", "bbox": [160, 345, 811, 360]},
	{"text": "前。入院后给予哌拉西林他唑巴坦抗感染，蒙脱石散止泻，枯草杆菌二联活菌胶囊调整消化", "bbox": [159, 360, 813, 375]},
	{"text": "道菌群，利伐沙班抗凝，制霉素片口服治疗，现患者病情稳定，于2025-05-29出院。", "bbox": [158, 375, 758, 390]},
	{"text": "患者因“确诊肺腺癌2月余。”第4次入院，入院后完善辅助检查，入院后排除禁忌，", "bbox": [191, 392, 790, 410]},
	{"text": "06-06行第3周期治疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2，联合信迪利单抗200mg", "bbox": [156, 409, 817, 427]},
	{"text": "抗肿瘤免疫治疗，并辅以激素、止吐、护胃、保肝等治疗，治疗结束后复查血常规未见明显", "bbox": [156, 425, 817, 443]},
	{"text": "骨髓抑制，于2025-06-08出院。末次出院诊断：1.恶性肿瘤维持性化学治疗 2.恶性肿瘤免", "bbox": [156, 441, 810, 459]},
	{"text": "疫治疗 3.肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转移 肺门淋巴结转移 胸膜转移 恶性胸腔", "bbox": [156, 457, 810, 475]},
	{"text": "积液 4.大隐静脉曲张 5.肾囊肿 6.单纯性肝囊肿。", "bbox": [156, 475, 524, 492]},
	{"text": "患者因“确诊肺腺癌2月余，为继续治疗”于2025-06-26第5次入院，入院后完善相关检", "bbox": [191, 488, 819, 507]},
	{"text": "查，排除禁忌，06-27行第4周期治疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2，联合", "bbox": [158, 504, 810, 522]},
	{"text": "信迪利单抗200mg抗肿瘤免疫治疗，并辅以激素、止吐、护胃、保肝等治疗，治疗结束后复", "bbox": [158, 518, 810, 537]},
	{"text": "查血常规未见明显骨髓抑制，于2025-06-29出院。末次出院诊断：1.恶性肿瘤维持性化学治", "bbox": [158, 533, 818, 552]},
	{"text": "疗 2.恶性肿瘤免疫治疗 3.肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转移 肺门淋巴结转移 胸", "bbox": [158, 548, 810, 567]},
	{"text": "膜转移 4.恶性胸腔积液 5.大隐静脉曲张 6.肾囊肿 7.单纯性肝囊肿.", "bbox": [160, 565, 660, 583]},
	{"text": "患者因“确诊肺腺癌3月余，为继续治疗”2025-07-17入院，入院后完善相关必要辅助", "bbox": [195, 579, 810, 598]},
	{"text": "第2页", "bbox": [470, 613, 520, 625]}
]
2026-08-10 18:22:15,806 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=17.5s
2026-08-10 18:22:15,806 INFO     29 [qwen-vl-text] coord item[0]: text=次吸收。2.右肺下叶占位，较前略缩小，考虑肺癌；纵隔及双肺门淋巴结部分较前略增大；, bbox=[180, 88, 770, 100]
2026-08-10 18:22:15,806 INFO     29 [qwen-vl-text] coord item[1]: text=右侧胸膜结节状增厚，较前局部稍减轻，请结合临床。3.左肺小结节，较前相仿，建议短期, bbox=[180, 100, 780, 113]
2026-08-10 18:22:15,806 INFO     29 [qwen-vl-text] coord item[2]: text=复查。余所见大致同前。入院后于05-09拔除胸腔引流管。排除禁忌于05-09行第2周期全身, bbox=[180, 113, 774, 126]
2026-08-10 18:22:15,806 INFO     29 [qwen-vl-text] coord item[3]: text=化疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2 q21d，并辅以激素、止吐、护胃、保肝, bbox=[180, 126, 783, 139]
2026-08-10 18:22:15,806 INFO     29 [qwen-vl-text] coord item[4]: text=等治疗，05-10给予信迪利单抗200mg肿瘤免疫治疗。患者治疗结束，于2025-05-11出院。, bbox=[178, 139, 763, 152]
2026-08-10 18:22:15,806 INFO     29 [qwen-vl-text] coord item[5]: text=患者因“确诊肺腺癌1月余，发热5天”于2025-05-19第3次入院，入院后完善检验检, bbox=[206, 152, 763, 165]
2026-08-10 18:22:15,806 INFO     29 [qwen-vl-text] coord item[6]: text=查：大便菌群分析:细菌总数600 个/油镜视野（参考值500～5000个），革兰阳性球菌少量，, bbox=[178, 165, 785, 178]
2026-08-10 18:22:15,806 INFO     29 [qwen-vl-text] coord item[7]: text=革兰阴性杆菌少量，酵母样真菌孢子+，酵母样真菌菌丝+；艰难梭菌毒素A/B检测:艰难梭, bbox=[180, 178, 783, 191]
2026-08-10 18:22:15,806 INFO     29 [qwen-vl-text] coord item[8]: text=菌毒素A/B检测 0.02；大便细菌培养+药敏:经两天普通培养，鉴定生长热带念珠菌+++，无, bbox=[175, 191, 792, 204]
2026-08-10 18:22:15,806 INFO     29 [qwen-vl-text] coord item[9]: text=肠球菌生长，无肠杆菌生长，无沙门氏菌、志贺氏菌生长。痰细菌学检查:经2天普通培养，, bbox=[173, 204, 785, 217]
2026-08-10 18:22:15,806 INFO     29 [qwen-vl-text] coord item[10]: text=经鉴定为正常菌群生长，无流感嗜血杆菌生长。胸部平扫(64排-128层)：对比, bbox=[172, 217, 702, 231]
2026-08-10 18:22:15,806 INFO     29 [qwen-vl-text] coord item[11]: text=2025-04-14CT：1.符合右侧胸腔引流术后改变，右侧液气胸，积液较前增多，积气较前减, bbox=[171, 231, 782, 245]
2026-08-10 18:22:15,806 INFO     29 [qwen-vl-text] coord item[12]: text=少；原右侧颈根部及胸壁少量积气本次吸收。2.右肺下叶占位，较前略缩小，考虑肺癌；纵, bbox=[170, 245, 799, 259]
2026-08-10 18:22:15,807 INFO     29 [qwen-vl-text] coord item[13]: text=隔及双肺门淋巴结部分较前略增大；右侧胸膜结节状增厚，较前局部稍减轻，请结合临床。, bbox=[169, 259, 794, 273]
2026-08-10 18:22:15,807 INFO     29 [qwen-vl-text] coord item[14]: text=3.左肺小结节，较前相仿，建议短期复查。余所见大致同前。腹部（包括盆腔）平扫(64, bbox=[167, 273, 780, 287]
2026-08-10 18:22:15,807 INFO     29 [qwen-vl-text] coord item[15]: text=排)：1.考虑肝多发囊肿、右肾囊肿，必要时增强扫描。2.双肾周桥隔略增厚。3.动脉粥样, bbox=[167, 287, 797, 301]
2026-08-10 18:22:15,807 INFO     29 [qwen-vl-text] coord item[16]: text=硬化。4.前列腺增大伴钙化。5.L5椎体前滑脱（I°），双侧椎弓峡部裂。胸部平扫(64排, bbox=[165, 301, 791, 315]
2026-08-10 18:22:15,807 INFO     29 [qwen-vl-text] coord item[17]: text=-128层)：对比2025-05-08CT：1.右侧液气胸，积液较前增多，积气较前减少。2.右肺下叶, bbox=[164, 315, 800, 329]
2026-08-10 18:22:15,807 INFO     29 [qwen-vl-text] coord item[18]: text=占位，较前缩小，考虑肺癌；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜结节状增, bbox=[163, 330, 795, 344]
2026-08-10 18:22:15,807 INFO     29 [qwen-vl-text] coord item[19]: text=厚，较前变化不著，请结合临床。3.左肺小结节，较前相仿，建议短期复查。余所见大致同, bbox=[160, 345, 811, 360]
2026-08-10 18:22:15,807 INFO     29 [qwen-vl-text] coord item[20]: text=前。入院后给予哌拉西林他唑巴坦抗感染，蒙脱石散止泻，枯草杆菌二联活菌胶囊调整消化, bbox=[159, 360, 813, 375]
2026-08-10 18:22:15,807 INFO     29 [qwen-vl-text] coord item[21]: text=道菌群，利伐沙班抗凝，制霉素片口服治疗，现患者病情稳定，于2025-05-29出院。, bbox=[158, 375, 758, 390]
2026-08-10 18:22:15,807 INFO     29 [qwen-vl-text] coord item[22]: text=患者因“确诊肺腺癌2月余。”第4次入院，入院后完善辅助检查，入院后排除禁忌，, bbox=[191, 392, 790, 410]
2026-08-10 18:22:15,807 INFO     29 [qwen-vl-text] coord item[23]: text=06-06行第3周期治疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2，联合信迪利单抗200mg, bbox=[156, 409, 817, 427]
2026-08-10 18:22:15,807 INFO     29 [qwen-vl-text] coord item[24]: text=抗肿瘤免疫治疗，并辅以激素、止吐、护胃、保肝等治疗，治疗结束后复查血常规未见明显, bbox=[156, 425, 817, 443]
2026-08-10 18:22:15,807 INFO     29 [qwen-vl-text] coord item[25]: text=骨髓抑制，于2025-06-08出院。末次出院诊断：1.恶性肿瘤维持性化学治疗 2.恶性肿瘤免, bbox=[156, 441, 810, 459]
2026-08-10 18:22:15,807 INFO     29 [qwen-vl-text] coord item[26]: text=疫治疗 3.肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转移 肺门淋巴结转移 胸膜转移 恶性胸腔, bbox=[156, 457, 810, 475]
2026-08-10 18:22:15,807 INFO     29 [qwen-vl-text] coord item[27]: text=积液 4.大隐静脉曲张 5.肾囊肿 6.单纯性肝囊肿。, bbox=[156, 475, 524, 492]
2026-08-10 18:22:15,807 INFO     29 [qwen-vl-text] coord item[28]: text=患者因“确诊肺腺癌2月余，为继续治疗”于2025-06-26第5次入院，入院后完善相关检, bbox=[191, 488, 819, 507]
2026-08-10 18:22:15,807 INFO     29 [qwen-vl-text] coord item[29]: text=查，排除禁忌，06-27行第4周期治疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2，联合, bbox=[158, 504, 810, 522]
2026-08-10 18:22:15,807 INFO     29 [qwen-vl-text] coord item[30]: text=信迪利单抗200mg抗肿瘤免疫治疗，并辅以激素、止吐、护胃、保肝等治疗，治疗结束后复, bbox=[158, 518, 810, 537]
2026-08-10 18:22:15,808 INFO     29 [qwen-vl-text] coord item[31]: text=查血常规未见明显骨髓抑制，于2025-06-29出院。末次出院诊断：1.恶性肿瘤维持性化学治, bbox=[158, 533, 818, 552]
2026-08-10 18:22:15,808 INFO     29 [qwen-vl-text] coord item[32]: text=疗 2.恶性肿瘤免疫治疗 3.肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转移 肺门淋巴结转移 胸, bbox=[158, 548, 810, 567]
2026-08-10 18:22:15,808 INFO     29 [qwen-vl-text] coord item[33]: text=膜转移 4.恶性胸腔积液 5.大隐静脉曲张 6.肾囊肿 7.单纯性肝囊肿., bbox=[160, 565, 660, 583]
2026-08-10 18:22:15,808 INFO     29 [qwen-vl-text] coord item[34]: text=患者因“确诊肺腺癌3月余，为继续治疗”2025-07-17入院，入院后完善相关必要辅助, bbox=[195, 579, 810, 598]
2026-08-10 18:22:15,808 INFO     29 [qwen-vl-text] coord item[35]: text=第2页, bbox=[470, 613, 520, 625]
2026-08-10 18:22:15,809 INFO     29 [qwen-vl-text] page=1 — 36/36 coords, api_time=17.5s
2026-08-10 18:22:15,812 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2076577, prompt_len=2412
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共36行）
["检查：电解质+血气分析:酸碱度7.476，二氧化碳分压36.4mmHg，氧分压114.0mmHg；急", "查血常规+CRP:红细胞3.61x10^12/L，血红蛋白110g/L，血小板总数222×10^9/L，白细", "胞4.90×10^9/L，中性粒细胞绝对值3.59×10^9/L，淋巴细胞绝对值0.77×10^9/L，超", "敏C-反应蛋白17.92mg/L；肺肿瘤检验：癌胚抗原54.9ng/ml，细胞角蛋白19片段", "5.54ng/ml，胃泌素释放肽前体80.2pg/ml；生化系列36项:白蛋白(溴甲酚绿法)", "31.59g/L，镁0.72mmol/L，肌酐(酶法)55μmol/L，肌酸激酶31U/L；DIC系列-5项:纤维", "蛋白原5.47g/L，D-二聚体3.53mg/L；急查降钙素原、急查心梗三项、皮质醇(7:00-10:", "00am)、促肾上腺皮质激素(8时)、甲状腺功能3项、急查NT-proBNP、大便常规(粪沉渣)+", "潜血、尿液分析+尿沉渣未见明显异常。常规心电图检查(自动分析)：窦性心动过速；心", "脏超声检查(含左心功能测定)：主动脉瓣轻度反流，三尖瓣轻度反流；颅脑平扫+DWI+增", "强(3T)：1.双侧额顶叶及侧脑室旁白质内脱髓鞘改变。2.老年脑改变。3.部分副鼻窦炎；", "右侧乳突炎。4.鼻中隔偏曲，双下鼻甲肥大。颈部：左侧颈部淋巴结稍大，右侧颈部淋巴结", "可见；髂静脉及下肢深静脉、下肢浅静脉：左侧大隐静脉曲张，左侧隐股静脉瓣功能不全；", "腹部(包括盆腔)平扫(64排)：1.考虑肝多发囊肿、右肾囊肿，必要时增强扫描。2.双肾周", "桥隔略增厚。3.动脉粥样硬化。4.前列腺增大伴钙化。5.L5椎体前滑脱(I°)，双侧椎弓", "峡部裂。以上所见较2025-05-26CT变化不著。胸部平扫(64排-128层)：对比2025-05-26CT:", "1.右肺下叶肺癌，较前略缩小、其内新见空洞影；右肺小叶间隔增厚，考虑癌性淋巴管炎可", "能；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜结节状增厚，较前变化不著；请结合", "临床。2.右侧液气胸，积液较前略增多，积气较前明显减少。3.左肺小结节，较前相仿，建", "议短期复查。4.右侧第7-9、12肋骨高密度影，较前密度增高，转移?建议ECT进一步检查。", "余所见大致同前。肋骨平扫+DWI+增强(3T)：1.右侧第7-9、12肋改变，成骨性转移?请结", "合其它影像学检查。2.右侧胸腔积液。3.肝内多发囊肿。排除禁忌，07-18行第5周期治疗：", "培美曲塞0.8gd1+顺铂注射液65mgd1、d2，联合信迪利单抗200mg抗肿瘤免疫治疗，并辅", "以激素、止吐、护胃、保肝等治疗，治疗结束后复查血常规未见明显骨髓抑制，针对肋骨异", "常请放疗科会诊后建议可考虑放疗，07-21出院。", "患者因“确诊肺腺癌4月，为继续治疗”2025-08-07第7次入院，入院后完善相关检查，", "急查血常规+CRP:血红蛋白109g/L，血小板总数205×10^9/L，白细胞4.58×10^9/L，中", "性粒细胞百分率70.9%，超敏C-反应蛋白17.43mg/L；超敏肌钙蛋白T14.80pg/ml；DIC系", "列-5项:纤维蛋白原5.27g/L，D-二聚体4.37mg/L；N端-B型钠尿肽前体71.5pg/ml；促肾", "上腺皮质激素(8时)：促肾上腺皮质激素(8时)31.7pg/ml；生化系列36项:白蛋白(溴甲酚绿", "法)33.34g/L，钾3.93mmol/L，钠140.1mmol/L，氯104.8mmol/L，尿素5.04mmol/L，肌", "酐(酶法)65μmol/L；皮质醇(7:00-10:00am)：皮质醇(7:00-10:00am)295nmol/L；甲状腺", "功能3项：促甲状腺素3.17mIU/L，游离甲状腺素13.6pmol/L，游离三碘甲状腺原氨酸", "4.46pmol/L；肺肿瘤检验：癌胚抗原52.6ng/ml，神经元特异性烯醇化酶20.4ng/ml，", "细胞角蛋白19片段4.81ng/ml，胃泌素释放肽前体92.9pg/ml。常规心电图检查(自动分", "第3页"]

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
2026-08-10 18:22:36,301 INFO     29 [qwen-vl-text] coord API raw response (len=3277):
[
	{"text": "检查：电解质+血气分析:酸碱度7.476，二氧化碳分压36.4mmHg，氧分压114.0mmHg；急", "bbox": [190, 94, 760, 108]},
	{"text": "查血常规+CRP:红细胞3.61x10^12/L，血红蛋白110g/L，血小板总数222×10^9/L，白细", "bbox": [190, 107, 762, 120]},
	{"text": "胞4.90×10^9/L，中性粒细胞绝对值3.59×10^9/L，淋巴细胞绝对值0.77×10^9/L，超", "bbox": [190, 118, 764, 132]},
	{"text": "敏C-反应蛋白17.92mg/L；肺肿瘤检验：癌胚抗原54.9ng/ml，细胞角蛋白19片段", "bbox": [190, 131, 716, 144]},
	{"text": "5.54ng/ml，胃泌素释放肽前体80.2pg/ml；生化系列36项:白蛋白(溴甲酚绿法)", "bbox": [190, 143, 702, 157]},
	{"text": "31.59g/L，镁0.72mmol/L，肌酐(酶法)55μmol/L，肌酸激酶31U/L；DIC系列-5项:纤维", "bbox": [190, 155, 770, 169]},
	{"text": "蛋白原5.47g/L，D-二聚体3.53mg/L；急查降钙素原、急查心梗三项、皮质醇(7:00-10:", "bbox": [190, 167, 764, 181]},
	{"text": "00am)、促肾上腺皮质激素(8时)、甲状腺功能3项、急查NT-proBNP、大便常规(粪沉渣)+", "bbox": [188, 179, 774, 194]},
	{"text": "潜血、尿液分析+尿沉渣未见明显异常。常规心电图检查(自动分析)：窦性心动过速；心", "bbox": [188, 192, 776, 206]},
	{"text": "脏超声检查(含左心功能测定)：主动脉瓣轻度反流，三尖瓣轻度反流；颅脑平扫+DWI+增", "bbox": [188, 204, 778, 218]},
	{"text": "强(3T)：1.双侧额顶叶及侧脑室旁白质内脱髓鞘改变。2.老年脑改变。3.部分副鼻窦炎；", "bbox": [188, 216, 778, 231]},
	{"text": "右侧乳突炎。4.鼻中隔偏曲，双下鼻甲肥大。颈部：左侧颈部淋巴结稍大，右侧颈部淋巴结", "bbox": [188, 229, 789, 244]},
	{"text": "可见；髂静脉及下肢深静脉、下肢浅静脉：左侧大隐静脉曲张，左侧隐股静脉瓣功能不全；", "bbox": [188, 242, 784, 257]},
	{"text": "腹部(包括盆腔)平扫(64排)：1.考虑肝多发囊肿、右肾囊肿，必要时增强扫描。2.双肾周", "bbox": [182, 255, 792, 270]},
	{"text": "桥隔略增厚。3.动脉粥样硬化。4.前列腺增大伴钙化。5.L5椎体前滑脱(I°)，双侧椎弓", "bbox": [182, 268, 787, 283]},
	{"text": "峡部裂。以上所见较2025-05-26CT变化不著。胸部平扫(64排-128层)：对比2025-05-26CT:", "bbox": [180, 281, 787, 296]},
	{"text": "1.右肺下叶肺癌，较前略缩小、其内新见空洞影；右肺小叶间隔增厚，考虑癌性淋巴管炎可", "bbox": [180, 295, 798, 310]},
	{"text": "能；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜结节状增厚，较前变化不著；请结合", "bbox": [178, 308, 800, 324]},
	{"text": "临床。2.右侧液气胸，积液较前略增多，积气较前明显减少。3.左肺小结节，较前相仿，建", "bbox": [178, 322, 802, 338]},
	{"text": "议短期复查。4.右侧第7-9、12肋骨高密度影，较前密度增高，转移?建议ECT进一步检查。", "bbox": [176, 336, 800, 352]},
	{"text": "余所见大致同前。肋骨平扫+DWI+增强(3T)：1.右侧第7-9、12肋改变，成骨性转移?请结", "bbox": [176, 350, 807, 367]},
	{"text": "合其它影像学检查。2.右侧胸腔积液。3.肝内多发囊肿。排除禁忌，07-18行第5周期治疗：", "bbox": [174, 365, 802, 381]},
	{"text": "培美曲塞0.8gd1+顺铂注射液65mgd1、d2，联合信迪利单抗200mg抗肿瘤免疫治疗，并辅", "bbox": [172, 380, 811, 396]},
	{"text": "以激素、止吐、护胃、保肝等治疗，治疗结束后复查血常规未见明显骨髓抑制，针对肋骨异", "bbox": [172, 395, 813, 411]},
	{"text": "常请放疗科会诊后建议可考虑放疗，07-21出院。", "bbox": [170, 410, 511, 427]},
	{"text": "患者因“确诊肺腺癌4月，为继续治疗”2025-08-07第7次入院，入院后完善相关检查，", "bbox": [200, 428, 809, 448]},
	{"text": "急查血常规+CRP:血红蛋白109g/L，血小板总数205×10^9/L，白细胞4.58×10^9/L，中", "bbox": [167, 445, 813, 465]},
	{"text": "性粒细胞百分率70.9%，超敏C-反应蛋白17.43mg/L；超敏肌钙蛋白T14.80pg/ml；DIC系", "bbox": [165, 461, 815, 481]},
	{"text": "列-5项:纤维蛋白原5.27g/L，D-二聚体4.37mg/L；N端-B型钠尿肽前体71.5pg/ml；促肾", "bbox": [165, 477, 817, 497]},
	{"text": "上腺皮质激素(8时)：促肾上腺皮质激素(8时)31.7pg/ml；生化系列36项:白蛋白(溴甲酚绿", "bbox": [165, 493, 819, 513]},
	{"text": "法)33.34g/L，钾3.93mmol/L，钠140.1mmol/L，氯104.8mmol/L，尿素5.04mmol/L，肌", "bbox": [163, 509, 830, 529]},
	{"text": "酐(酶法)65μmol/L；皮质醇(7:00-10:00am)：皮质醇(7:00-10:00am)295nmol/L；甲状腺", "bbox": [163, 525, 823, 545]},
	{"text": "功能3项：促甲状腺素3.17mIU/L，游离甲状腺素13.6pmol/L，游离三碘甲状腺原氨酸", "bbox": [163, 541, 790, 561]},
	{"text": "4.46pmol/L；肺肿瘤检验：癌胚抗原52.6ng/ml，神经元特异性烯醇化酶20.4ng/ml，", "bbox": [163, 557, 823, 577]},
	{"text": "细胞角蛋白19片段4.81ng/ml，胃泌素释放肽前体92.9pg/ml。常规心电图检查(自动分", "bbox": [163, 573, 817, 593]},
	{"text": "第3页", "bbox": [477, 608, 529, 620]}
]
2026-08-10 18:22:36,302 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=20.5s
2026-08-10 18:22:36,302 INFO     29 [qwen-vl-text] coord item[0]: text=检查：电解质+血气分析:酸碱度7.476，二氧化碳分压36.4mmHg，氧分压114.0mmHg；急, bbox=[190, 94, 760, 108]
2026-08-10 18:22:36,302 INFO     29 [qwen-vl-text] coord item[1]: text=查血常规+CRP:红细胞3.61x10^12/L，血红蛋白110g/L，血小板总数222×10^9/L，白细, bbox=[190, 107, 762, 120]
2026-08-10 18:22:36,302 INFO     29 [qwen-vl-text] coord item[2]: text=胞4.90×10^9/L，中性粒细胞绝对值3.59×10^9/L，淋巴细胞绝对值0.77×10^9/L，超, bbox=[190, 118, 764, 132]
2026-08-10 18:22:36,302 INFO     29 [qwen-vl-text] coord item[3]: text=敏C-反应蛋白17.92mg/L；肺肿瘤检验：癌胚抗原54.9ng/ml，细胞角蛋白19片段, bbox=[190, 131, 716, 144]
2026-08-10 18:22:36,302 INFO     29 [qwen-vl-text] coord item[4]: text=5.54ng/ml，胃泌素释放肽前体80.2pg/ml；生化系列36项:白蛋白(溴甲酚绿法), bbox=[190, 143, 702, 157]
2026-08-10 18:22:36,302 INFO     29 [qwen-vl-text] coord item[5]: text=31.59g/L，镁0.72mmol/L，肌酐(酶法)55μmol/L，肌酸激酶31U/L；DIC系列-5项:纤维, bbox=[190, 155, 770, 169]
2026-08-10 18:22:36,302 INFO     29 [qwen-vl-text] coord item[6]: text=蛋白原5.47g/L，D-二聚体3.53mg/L；急查降钙素原、急查心梗三项、皮质醇(7:00-10:, bbox=[190, 167, 764, 181]
2026-08-10 18:22:36,302 INFO     29 [qwen-vl-text] coord item[7]: text=00am)、促肾上腺皮质激素(8时)、甲状腺功能3项、急查NT-proBNP、大便常规(粪沉渣)+, bbox=[188, 179, 774, 194]
2026-08-10 18:22:36,302 INFO     29 [qwen-vl-text] coord item[8]: text=潜血、尿液分析+尿沉渣未见明显异常。常规心电图检查(自动分析)：窦性心动过速；心, bbox=[188, 192, 776, 206]
2026-08-10 18:22:36,302 INFO     29 [qwen-vl-text] coord item[9]: text=脏超声检查(含左心功能测定)：主动脉瓣轻度反流，三尖瓣轻度反流；颅脑平扫+DWI+增, bbox=[188, 204, 778, 218]
2026-08-10 18:22:36,302 INFO     29 [qwen-vl-text] coord item[10]: text=强(3T)：1.双侧额顶叶及侧脑室旁白质内脱髓鞘改变。2.老年脑改变。3.部分副鼻窦炎；, bbox=[188, 216, 778, 231]
2026-08-10 18:22:36,302 INFO     29 [qwen-vl-text] coord item[11]: text=右侧乳突炎。4.鼻中隔偏曲，双下鼻甲肥大。颈部：左侧颈部淋巴结稍大，右侧颈部淋巴结, bbox=[188, 229, 789, 244]
2026-08-10 18:22:36,302 INFO     29 [qwen-vl-text] coord item[12]: text=可见；髂静脉及下肢深静脉、下肢浅静脉：左侧大隐静脉曲张，左侧隐股静脉瓣功能不全；, bbox=[188, 242, 784, 257]
2026-08-10 18:22:36,302 INFO     29 [qwen-vl-text] coord item[13]: text=腹部(包括盆腔)平扫(64排)：1.考虑肝多发囊肿、右肾囊肿，必要时增强扫描。2.双肾周, bbox=[182, 255, 792, 270]
2026-08-10 18:22:36,302 INFO     29 [qwen-vl-text] coord item[14]: text=桥隔略增厚。3.动脉粥样硬化。4.前列腺增大伴钙化。5.L5椎体前滑脱(I°)，双侧椎弓, bbox=[182, 268, 787, 283]
2026-08-10 18:22:36,302 INFO     29 [qwen-vl-text] coord item[15]: text=峡部裂。以上所见较2025-05-26CT变化不著。胸部平扫(64排-128层)：对比2025-05-26CT:, bbox=[180, 281, 787, 296]
2026-08-10 18:22:36,302 INFO     29 [qwen-vl-text] coord item[16]: text=1.右肺下叶肺癌，较前略缩小、其内新见空洞影；右肺小叶间隔增厚，考虑癌性淋巴管炎可, bbox=[180, 295, 798, 310]
2026-08-10 18:22:36,302 INFO     29 [qwen-vl-text] coord item[17]: text=能；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜结节状增厚，较前变化不著；请结合, bbox=[178, 308, 800, 324]
2026-08-10 18:22:36,302 INFO     29 [qwen-vl-text] coord item[18]: text=临床。2.右侧液气胸，积液较前略增多，积气较前明显减少。3.左肺小结节，较前相仿，建, bbox=[178, 322, 802, 338]
2026-08-10 18:22:36,303 INFO     29 [qwen-vl-text] coord item[19]: text=议短期复查。4.右侧第7-9、12肋骨高密度影，较前密度增高，转移?建议ECT进一步检查。, bbox=[176, 336, 800, 352]
2026-08-10 18:22:36,303 INFO     29 [qwen-vl-text] coord item[20]: text=余所见大致同前。肋骨平扫+DWI+增强(3T)：1.右侧第7-9、12肋改变，成骨性转移?请结, bbox=[176, 350, 807, 367]
2026-08-10 18:22:36,303 INFO     29 [qwen-vl-text] coord item[21]: text=合其它影像学检查。2.右侧胸腔积液。3.肝内多发囊肿。排除禁忌，07-18行第5周期治疗：, bbox=[174, 365, 802, 381]
2026-08-10 18:22:36,303 INFO     29 [qwen-vl-text] coord item[22]: text=培美曲塞0.8gd1+顺铂注射液65mgd1、d2，联合信迪利单抗200mg抗肿瘤免疫治疗，并辅, bbox=[172, 380, 811, 396]
2026-08-10 18:22:36,303 INFO     29 [qwen-vl-text] coord item[23]: text=以激素、止吐、护胃、保肝等治疗，治疗结束后复查血常规未见明显骨髓抑制，针对肋骨异, bbox=[172, 395, 813, 411]
2026-08-10 18:22:36,303 INFO     29 [qwen-vl-text] coord item[24]: text=常请放疗科会诊后建议可考虑放疗，07-21出院。, bbox=[170, 410, 511, 427]
2026-08-10 18:22:36,303 INFO     29 [qwen-vl-text] coord item[25]: text=患者因“确诊肺腺癌4月，为继续治疗”2025-08-07第7次入院，入院后完善相关检查，, bbox=[200, 428, 809, 448]
2026-08-10 18:22:36,303 INFO     29 [qwen-vl-text] coord item[26]: text=急查血常规+CRP:血红蛋白109g/L，血小板总数205×10^9/L，白细胞4.58×10^9/L，中, bbox=[167, 445, 813, 465]
2026-08-10 18:22:36,303 INFO     29 [qwen-vl-text] coord item[27]: text=性粒细胞百分率70.9%，超敏C-反应蛋白17.43mg/L；超敏肌钙蛋白T14.80pg/ml；DIC系, bbox=[165, 461, 815, 481]
2026-08-10 18:22:36,303 INFO     29 [qwen-vl-text] coord item[28]: text=列-5项:纤维蛋白原5.27g/L，D-二聚体4.37mg/L；N端-B型钠尿肽前体71.5pg/ml；促肾, bbox=[165, 477, 817, 497]
2026-08-10 18:22:36,303 INFO     29 [qwen-vl-text] coord item[29]: text=上腺皮质激素(8时)：促肾上腺皮质激素(8时)31.7pg/ml；生化系列36项:白蛋白(溴甲酚绿, bbox=[165, 493, 819, 513]
2026-08-10 18:22:36,303 INFO     29 [qwen-vl-text] coord item[30]: text=法)33.34g/L，钾3.93mmol/L，钠140.1mmol/L，氯104.8mmol/L，尿素5.04mmol/L，肌, bbox=[163, 509, 830, 529]
2026-08-10 18:22:36,303 INFO     29 [qwen-vl-text] coord item[31]: text=酐(酶法)65μmol/L；皮质醇(7:00-10:00am)：皮质醇(7:00-10:00am)295nmol/L；甲状腺, bbox=[163, 525, 823, 545]
2026-08-10 18:22:36,303 INFO     29 [qwen-vl-text] coord item[32]: text=功能3项：促甲状腺素3.17mIU/L，游离甲状腺素13.6pmol/L，游离三碘甲状腺原氨酸, bbox=[163, 541, 790, 561]
2026-08-10 18:22:36,303 INFO     29 [qwen-vl-text] coord item[33]: text=4.46pmol/L；肺肿瘤检验：癌胚抗原52.6ng/ml，神经元特异性烯醇化酶20.4ng/ml，, bbox=[163, 557, 823, 577]
2026-08-10 18:22:36,303 INFO     29 [qwen-vl-text] coord item[34]: text=细胞角蛋白19片段4.81ng/ml，胃泌素释放肽前体92.9pg/ml。常规心电图检查(自动分, bbox=[163, 573, 817, 593]
2026-08-10 18:22:36,303 INFO     29 [qwen-vl-text] coord item[35]: text=第3页, bbox=[477, 608, 529, 620]
2026-08-10 18:22:36,304 INFO     29 [qwen-vl-text] page=2 — 36/36 coords, api_time=20.5s
2026-08-10 18:22:36,309 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1986973, prompt_len=2369
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共36行）
["析）：窦性心律，大致正常心电图。排除禁忌，于08-08给予第6周期化疗，方案为培美曲塞", "0.8g+顺铂注射液 65mg d1、d2，联合信迪利单抗200mg 免疫治疗，过程顺利，08-10行地", "舒单抗120mg抗骨转移治疗；复查血常规未见明显骨髓抑制，08-10出院。", "患者因“确诊肺腺癌4月，为继续治疗”于2025-08-28第8次入院，入院后完善辅助检", "查：胸部平扫：对比2025-07-18CT：1.右肺下叶肺癌，较前变化不著；右肺小叶间隔增厚，", "较前变化不著，考虑癌性淋巴管炎可能；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜", "结节状增厚，较前变化不著；请结合临床。2.右侧液气胸，积液较前变化不著，积气较前增", "多。3.左肺小结节，较前相仿，建议短期复查。4.右侧第7-9、12肋骨高密度影，较前变化", "不著，转移？建议ECT进一步检查。余所见大致同前。下腹部平扫：1.考虑右肾囊肿，较", "2025-07-18变化不著，必要时增强扫描。2.双肾周桥隔略增厚。3.动脉粥样硬化。上腹部平", "扫：考虑肝多发囊肿，较2025-07-18变化不明显，建议结合增强检查明确。盆腔平扫：1.前", "列腺增大伴钙化。2.L5椎体前滑脱（I°），双侧椎弓峡部裂。以上所见较2025-07-18变化", "不著。排除禁忌，给予培美曲塞 0.8g 联合信迪利单抗 200mg免疫治疗，并辅以激素、止", "吐、护胃、保肝等治疗，治疗过程顺利，患者病情稳定，2025-08-30出院。出院诊断：1.恶", "性肿瘤维持性化学治疗 2.恶性肿瘤免疫治疗 3.右肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转", "移 肺门淋巴结转移 胸膜转移 骨转移 4.恶性胸腔积液 5.大隐静脉曲张 6.肾囊肿 7.单纯", "性肝囊肿。", "患者因“确诊肺腺癌5月余，为继续治疗”于2025-10-06第9次入院，入院后完善辅助检", "查：急查血常规+CRP:血红蛋白 114g/L，血小板总数 212×10^9/L，白细胞", "7.30×10^9/L，中性粒细胞百分率 80.0%，超敏C-反应蛋白 16.04mg/L；皮质醇(7:00-10:", "00am):皮质醇(7:00-10:00am) 442nmol/L；促肾上腺皮质激素(8时):促肾上腺皮质激素(8", "时) 29.3pg/ml；甲状腺功能3项:促甲状腺素 4.94mIU/L，游离甲状腺素 14.4pmol/L，游离", "三碘甲状腺原氨酸 3.85pmol/L；生化系列36项:白蛋白(溴甲酚绿法) 36.10g/L，白蛋白:球", "蛋白 0.96，天门冬氨酸氨基转移酶 18U/L，丙氨酸氨基转移酶 8U/L，尿素 5.84mmol/L，", "肌酐(酶法) 78μmol/L；肺肿瘤检验-莱山:癌胚抗原 68.6ng/ml，细胞角蛋白19片段", "9.45ng/ml，胃泌素释放肽前体 96.7pg/ml；DIC系列-5项:纤维蛋白原 5.04g/L，D-二聚体", "3.28mg/L；急查NT-proBNP:N端-B型钠尿肽前体 50.1pg/ml；急查心梗三项:超敏肌钙蛋白T", "14.00pg/ml，肌酸激酶-MB同工酶质量测定 0.54ng/ml，肌红蛋白 43.2ng/ml。排除禁忌，", "于2025-10-06给予本周期治疗，方案为培美曲塞 0.8g联合信迪利单抗200mg，并给予地舒单", "抗120mg治疗骨转移，2025-10-07办理出院。出院诊断：1.右肺腺癌（T2bN3M1 IV期） 纵隔", "淋巴结转移 肺门淋巴结转移 胸膜转移 骨转移 2.恶性胸腔积液 3.大隐静脉曲张 4.肾囊肿", "5.单纯性肝囊肿。", "患者因“确诊肺腺癌7月余，为继续治疗”于2025-11-07第10次入院，入院后完善相关", "检查：急查血常规+CRP:血红蛋白 115g/L，血小板总数 214×10^9/L，白细胞", "7.21×10^9/L，中性粒细胞百分率 82.3%，超敏C-反应蛋白 20.50mg/L；DIC系列-5项:纤维", "第 4 页"]

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
2026-08-10 18:22:54,060 INFO     29 [qwen-vl-text] coord API raw response (len=3234):
[
	{"text": "析）：窦性心律，大致正常心电图。排除禁忌，于08-08给予第6周期化疗，方案为培美曲塞", "bbox": [185, 87, 785, 100]},
	{"text": "0.8g+顺铂注射液 65mg d1、d2，联合信迪利单抗200mg 免疫治疗，过程顺利，08-10行地", "bbox": [190, 100, 780, 113]},
	{"text": "舒单抗120mg抗骨转移治疗；复查血常规未见明显骨髓抑制，08-10出院。", "bbox": [184, 113, 661, 126]},
	{"text": "患者因“确诊肺腺癌4月，为继续治疗”于2025-08-28第8次入院，入院后完善辅助检", "bbox": [213, 126, 774, 139]},
	{"text": "查：胸部平扫：对比2025-07-18CT：1.右肺下叶肺癌，较前变化不著；右肺小叶间隔增厚，", "bbox": [182, 139, 782, 152]},
	{"text": "较前变化不著，考虑癌性淋巴管炎可能；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜", "bbox": [181, 152, 792, 166]},
	{"text": "结节状增厚，较前变化不著；请结合临床。2.右侧液气胸，积液较前变化不著，积气较前增", "bbox": [181, 166, 792, 179]},
	{"text": "多。3.左肺小结节，较前相仿，建议短期复查。4.右侧第7-9、12肋骨高密度影，较前变化", "bbox": [181, 179, 787, 192]},
	{"text": "不著，转移？建议ECT进一步检查。余所见大致同前。下腹部平扫：1.考虑右肾囊肿，较", "bbox": [180, 192, 773, 206]},
	{"text": "2025-07-18变化不著，必要时增强扫描。2.双肾周桥隔略增厚。3.动脉粥样硬化。上腹部平", "bbox": [179, 206, 797, 219]},
	{"text": "扫：考虑肝多发囊肿，较2025-07-18变化不明显，建议结合增强检查明确。盆腔平扫：1.前", "bbox": [179, 219, 797, 233]},
	{"text": "列腺增大伴钙化。2.L5椎体前滑脱（I°），双侧椎弓峡部裂。以上所见较2025-07-18变化", "bbox": [179, 233, 792, 246]},
	{"text": "不著。排除禁忌，给予培美曲塞 0.8g 联合信迪利单抗 200mg免疫治疗，并辅以激素、止", "bbox": [178, 246, 786, 260]},
	{"text": "吐、护胃、保肝等治疗，治疗过程顺利，患者病情稳定，2025-08-30出院。出院诊断：1.恶", "bbox": [177, 260, 801, 274]},
	{"text": "性肿瘤维持性化学治疗 2.恶性肿瘤免疫治疗 3.右肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转", "bbox": [177, 274, 796, 287]},
	{"text": "移 肺门淋巴结转移 胸膜转移 骨转移 4.恶性胸腔积液 5.大隐静脉曲张 6.肾囊肿 7.单纯", "bbox": [176, 287, 798, 301]},
	{"text": "性肝囊肿。", "bbox": [175, 301, 246, 314]},
	{"text": "患者因“确诊肺腺癌5月余，为继续治疗”于2025-10-06第9次入院，入院后完善辅助检", "bbox": [205, 319, 808, 336]},
	{"text": "查：急查血常规+CRP:血红蛋白 114g/L，血小板总数 212×10^9/L，白细胞", "bbox": [173, 338, 699, 354]},
	{"text": "7.30×10^9/L，中性粒细胞百分率 80.0%，超敏C-反应蛋白 16.04mg/L；皮质醇(7:00-10:", "bbox": [173, 352, 800, 368]},
	{"text": "00am):皮质醇(7:00-10:00am) 442nmol/L；促肾上腺皮质激素(8时):促肾上腺皮质激素(8", "bbox": [172, 367, 796, 383]},
	{"text": "时) 29.3pg/ml；甲状腺功能3项:促甲状腺素 4.94mIU/L，游离甲状腺素 14.4pmol/L，游离", "bbox": [172, 381, 811, 398]},
	{"text": "三碘甲状腺原氨酸 3.85pmol/L；生化系列36项:白蛋白(溴甲酚绿法) 36.10g/L，白蛋白:球", "bbox": [172, 396, 813, 412]},
	{"text": "蛋白 0.96，天门冬氨酸氨基转移酶 18U/L，丙氨酸氨基转移酶 8U/L，尿素 5.84mmol/L，", "bbox": [171, 410, 798, 427]},
	{"text": "肌酐(酶法) 78μmol/L；肺肿瘤检验-莱山:癌胚抗原 68.6ng/ml，细胞角蛋白19片段", "bbox": [171, 425, 768, 442]},
	{"text": "9.45ng/ml，胃泌素释放肽前体 96.7pg/ml；DIC系列-5项:纤维蛋白原 5.04g/L，D-二聚体", "bbox": [170, 440, 808, 457]},
	{"text": "3.28mg/L；急查NT-proBNP:N端-B型钠尿肽前体 50.1pg/ml；急查心梗三项:超敏肌钙蛋白T", "bbox": [170, 455, 809, 472]},
	{"text": "14.00pg/ml，肌酸激酶-MB同工酶质量测定 0.54ng/ml，肌红蛋白 43.2ng/ml。排除禁忌，", "bbox": [170, 470, 800, 487]},
	{"text": "于2025-10-06给予本周期治疗，方案为培美曲塞 0.8g联合信迪利单抗200mg，并给予地舒单", "bbox": [170, 485, 818, 502]},
	{"text": "抗120mg治疗骨转移，2025-10-07办理出院。出院诊断：1.右肺腺癌（T2bN3M1 IV期） 纵隔", "bbox": [170, 500, 819, 517]},
	{"text": "淋巴结转移 肺门淋巴结转移 胸膜转移 骨转移 2.恶性胸腔积液 3.大隐静脉曲张 4.肾囊肿", "bbox": [170, 515, 820, 532]},
	{"text": "5.单纯性肝囊肿。", "bbox": [177, 538, 301, 554]},
	{"text": "患者因“确诊肺腺癌7月余，为继续治疗”于2025-11-07第10次入院，入院后完善相关", "bbox": [203, 548, 814, 568]},
	{"text": "检查：急查血常规+CRP:血红蛋白 115g/L，血小板总数 214×10^9/L，白细胞", "bbox": [170, 565, 725, 582]},
	{"text": "7.21×10^9/L，中性粒细胞百分率 82.3%，超敏C-反应蛋白 20.50mg/L；DIC系列-5项:纤维", "bbox": [170, 579, 823, 597]},
	{"text": "第 4 页", "bbox": [475, 613, 525, 626]}
]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=17.8s
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[0]: text=析）：窦性心律，大致正常心电图。排除禁忌，于08-08给予第6周期化疗，方案为培美曲塞, bbox=[185, 87, 785, 100]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[1]: text=0.8g+顺铂注射液 65mg d1、d2，联合信迪利单抗200mg 免疫治疗，过程顺利，08-10行地, bbox=[190, 100, 780, 113]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[2]: text=舒单抗120mg抗骨转移治疗；复查血常规未见明显骨髓抑制，08-10出院。, bbox=[184, 113, 661, 126]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[3]: text=患者因“确诊肺腺癌4月，为继续治疗”于2025-08-28第8次入院，入院后完善辅助检, bbox=[213, 126, 774, 139]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[4]: text=查：胸部平扫：对比2025-07-18CT：1.右肺下叶肺癌，较前变化不著；右肺小叶间隔增厚，, bbox=[182, 139, 782, 152]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[5]: text=较前变化不著，考虑癌性淋巴管炎可能；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜, bbox=[181, 152, 792, 166]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[6]: text=结节状增厚，较前变化不著；请结合临床。2.右侧液气胸，积液较前变化不著，积气较前增, bbox=[181, 166, 792, 179]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[7]: text=多。3.左肺小结节，较前相仿，建议短期复查。4.右侧第7-9、12肋骨高密度影，较前变化, bbox=[181, 179, 787, 192]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[8]: text=不著，转移？建议ECT进一步检查。余所见大致同前。下腹部平扫：1.考虑右肾囊肿，较, bbox=[180, 192, 773, 206]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[9]: text=2025-07-18变化不著，必要时增强扫描。2.双肾周桥隔略增厚。3.动脉粥样硬化。上腹部平, bbox=[179, 206, 797, 219]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[10]: text=扫：考虑肝多发囊肿，较2025-07-18变化不明显，建议结合增强检查明确。盆腔平扫：1.前, bbox=[179, 219, 797, 233]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[11]: text=列腺增大伴钙化。2.L5椎体前滑脱（I°），双侧椎弓峡部裂。以上所见较2025-07-18变化, bbox=[179, 233, 792, 246]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[12]: text=不著。排除禁忌，给予培美曲塞 0.8g 联合信迪利单抗 200mg免疫治疗，并辅以激素、止, bbox=[178, 246, 786, 260]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[13]: text=吐、护胃、保肝等治疗，治疗过程顺利，患者病情稳定，2025-08-30出院。出院诊断：1.恶, bbox=[177, 260, 801, 274]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[14]: text=性肿瘤维持性化学治疗 2.恶性肿瘤免疫治疗 3.右肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转, bbox=[177, 274, 796, 287]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[15]: text=移 肺门淋巴结转移 胸膜转移 骨转移 4.恶性胸腔积液 5.大隐静脉曲张 6.肾囊肿 7.单纯, bbox=[176, 287, 798, 301]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[16]: text=性肝囊肿。, bbox=[175, 301, 246, 314]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[17]: text=患者因“确诊肺腺癌5月余，为继续治疗”于2025-10-06第9次入院，入院后完善辅助检, bbox=[205, 319, 808, 336]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[18]: text=查：急查血常规+CRP:血红蛋白 114g/L，血小板总数 212×10^9/L，白细胞, bbox=[173, 338, 699, 354]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[19]: text=7.30×10^9/L，中性粒细胞百分率 80.0%，超敏C-反应蛋白 16.04mg/L；皮质醇(7:00-10:, bbox=[173, 352, 800, 368]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[20]: text=00am):皮质醇(7:00-10:00am) 442nmol/L；促肾上腺皮质激素(8时):促肾上腺皮质激素(8, bbox=[172, 367, 796, 383]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[21]: text=时) 29.3pg/ml；甲状腺功能3项:促甲状腺素 4.94mIU/L，游离甲状腺素 14.4pmol/L，游离, bbox=[172, 381, 811, 398]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[22]: text=三碘甲状腺原氨酸 3.85pmol/L；生化系列36项:白蛋白(溴甲酚绿法) 36.10g/L，白蛋白:球, bbox=[172, 396, 813, 412]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[23]: text=蛋白 0.96，天门冬氨酸氨基转移酶 18U/L，丙氨酸氨基转移酶 8U/L，尿素 5.84mmol/L，, bbox=[171, 410, 798, 427]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[24]: text=肌酐(酶法) 78μmol/L；肺肿瘤检验-莱山:癌胚抗原 68.6ng/ml，细胞角蛋白19片段, bbox=[171, 425, 768, 442]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[25]: text=9.45ng/ml，胃泌素释放肽前体 96.7pg/ml；DIC系列-5项:纤维蛋白原 5.04g/L，D-二聚体, bbox=[170, 440, 808, 457]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[26]: text=3.28mg/L；急查NT-proBNP:N端-B型钠尿肽前体 50.1pg/ml；急查心梗三项:超敏肌钙蛋白T, bbox=[170, 455, 809, 472]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[27]: text=14.00pg/ml，肌酸激酶-MB同工酶质量测定 0.54ng/ml，肌红蛋白 43.2ng/ml。排除禁忌，, bbox=[170, 470, 800, 487]
2026-08-10 18:22:54,061 INFO     29 [qwen-vl-text] coord item[28]: text=于2025-10-06给予本周期治疗，方案为培美曲塞 0.8g联合信迪利单抗200mg，并给予地舒单, bbox=[170, 485, 818, 502]
2026-08-10 18:22:54,062 INFO     29 [qwen-vl-text] coord item[29]: text=抗120mg治疗骨转移，2025-10-07办理出院。出院诊断：1.右肺腺癌（T2bN3M1 IV期） 纵隔, bbox=[170, 500, 819, 517]
2026-08-10 18:22:54,062 INFO     29 [qwen-vl-text] coord item[30]: text=淋巴结转移 肺门淋巴结转移 胸膜转移 骨转移 2.恶性胸腔积液 3.大隐静脉曲张 4.肾囊肿, bbox=[170, 515, 820, 532]
2026-08-10 18:22:54,062 INFO     29 [qwen-vl-text] coord item[31]: text=5.单纯性肝囊肿。, bbox=[177, 538, 301, 554]
2026-08-10 18:22:54,062 INFO     29 [qwen-vl-text] coord item[32]: text=患者因“确诊肺腺癌7月余，为继续治疗”于2025-11-07第10次入院，入院后完善相关, bbox=[203, 548, 814, 568]
2026-08-10 18:22:54,062 INFO     29 [qwen-vl-text] coord item[33]: text=检查：急查血常规+CRP:血红蛋白 115g/L，血小板总数 214×10^9/L，白细胞, bbox=[170, 565, 725, 582]
2026-08-10 18:22:54,062 INFO     29 [qwen-vl-text] coord item[34]: text=7.21×10^9/L，中性粒细胞百分率 82.3%，超敏C-反应蛋白 20.50mg/L；DIC系列-5项:纤维, bbox=[170, 579, 823, 597]
2026-08-10 18:22:54,062 INFO     29 [qwen-vl-text] coord item[35]: text=第 4 页, bbox=[475, 613, 525, 626]
2026-08-10 18:22:54,062 INFO     29 [qwen-vl-text] page=3 — 36/36 coords, api_time=17.8s
2026-08-10 18:22:54,067 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2157328, prompt_len=2420
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共37行）
["蛋白原 5.04g/L，D-二聚体 2.19mg/L；皮质醇(7:00-10:00am):皮质醇(7:00-10:00am)", "286nmol/L；促肾上腺皮质激素(8时):促肾上腺皮质激素(8时)23.3pg/ml；急查心梗三项:", "超敏肌钙蛋白T 17.70pg/ml；肺肿瘤检验-莱山:癌胚抗原 75.8ng/ml，细胞角蛋白19片段", "12.4ng/ml，胃泌素释放肽前体 90.5pg/ml；生化系列36项:白蛋白(溴甲酚绿法)", "32.49g/L，脂蛋白(a)343mg/L，唾液酸 769mg/L；N端-B型钠尿肽前体、甲状腺功能3项未", "见异常。常规心电图检查：窦性心动过速。全身骨显像：与本院2025-04-10骨显像比较：1.", "右侧多根肋骨多发异常放射性浓聚灶，病灶数目较前增多，浓聚程度增高，提示骨转移瘤可", "能大，请结合其他检查综合考虑；2.前次检查所示左侧坐骨轻度放射性浓聚灶，本次检查未", "见显示；3.双肩关节及双膝关节区异常放射性浓聚，考虑炎性病变，请结合临床。颅脑平扫", "+DWI+增强+薄层：1.双侧额顶叶及侧脑室旁白质内脱髓鞘改变；2.老年脑改变，双侧额颞部", "少量硬膜下积液；3.部分副鼻窦炎；右侧乳突炎；4.鼻中隔偏曲，双下鼻甲肥大。心脏超声", "检查（含左心功能测定）：静息状态下：心内结构及血流未见明显异常髂静脉及下肢深静脉", "(双侧)：双侧髂静脉及下肢深静脉血流通畅颈部：双侧颈部未见明显增大淋巴结胸部平扫", "+增强：对比2025-08-28CT：1.右肺下叶肺癌，较前增大；右肺小叶间隔增厚，较前略进", "展，考虑癌性淋巴管炎可能；纵隔及双肺门淋巴结，部分较前略增大；考虑右侧胸膜转移，", "较前明显进展，累及邻近右前胸壁及右侧膈肌可能；请结合临床并复查；2.右侧胸腔积液，", "较前变化不著，原右侧胸腔积气吸收；3.左肺小结节，部分较前略增大（如下叶薄层", "img231、243），部分结节较前相仿，建议短期复查；4.右侧第7-9、12肋骨高密度影，较前", "变化不著，转移？建议ECT进一步检查；余所见大致同前。上腹部平扫+增强：考虑肝多发囊", "肿，较2025-08-28变化不明显。下腹部平扫+增强：1.考虑右肾囊肿，较2025-08-28变化不", "著；2.双肾周桥隔略增厚；3.动脉粥样硬化。排除禁忌给予本周期治疗，方案为培美曲塞", "0.8g、信迪利单抗200mg联合恩度 210mg q21d治疗。治疗结束，患者病情稳定，2025-11-14", "办理出院。出院诊断：1.右肺腺癌(T2bN3M1 IV期) 纵隔淋巴结转移 肺门淋巴结转移 胸", "膜转移 骨转移 2.恶性胸腔积液 3.大隐静脉曲张 4.肾囊肿 5.肝囊肿", "患者因“确诊肺腺癌8月余，为继续治疗”于2026-01-08再入院，入院后完善相关辅助", "检查：01-08：急查NT-proBNP、促肾上腺皮质激素(8时)、皮质醇(7:00-10:00am)等未见明", "显异常。急查血常规+CRP+SAA:红细胞 3.93x10^12/L，血红蛋白 118g/L，红细胞压积", "35.8%，红细胞分布宽度SD 47.4fl，中性粒细胞百分率 77.9%，淋巴细胞百分率 9.4%，单", "核细胞百分率 10.2%，淋巴细胞绝对值 0.67×10^9/L，单核细胞绝对值 0.73×10^9/L，超", "敏C-反应蛋白 30.56mg/L，血清淀粉样蛋白A 26.98mg/L；急查心梗三项:超敏肌钙蛋白T", "15.10pg/ml；DIC系列-5项:纤维蛋白原 6.22g/L，D-二聚体 1.66mg/L；急查降钙素原：", "0.0969ng/ml；生化系列36项:白蛋白(溴甲酚绿法) 31.69g/L，白蛋白:球蛋白 0.87，肾小", "球滤过率 89.97ml/(min·1.73m²)，肌酸激酶 38U/L，脂蛋白(a) 452mg/L，唾液酸", "765mg/L；甲状腺功能6项:促甲状腺素 4.69mIU/L；肺肿瘤检验", "癌胚抗原", "73.4ng/ml，神经元特异性烯醇化酶 18.4ng/ml，细胞角蛋白19片段 19.1ng/ml，胃泌素释", "第5页"]

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
2026-08-10 18:23:14,531 INFO     29 [qwen-vl-text] coord API raw response (len=3326):
[
	{"text": "蛋白原 5.04g/L，D-二聚体 2.19mg/L；皮质醇(7:00-10:00am):皮质醇(7:00-10:00am)", "bbox": [198, 93, 756, 106]},
	{"text": "286nmol/L；促肾上腺皮质激素(8时):促肾上腺皮质激素(8时)23.3pg/ml；急查心梗三项:", "bbox": [198, 106, 780, 118]},
	{"text": "超敏肌钙蛋白T 17.70pg/ml；肺肿瘤检验-莱山:癌胚抗原 75.8ng/ml，细胞角蛋白19片段", "bbox": [198, 118, 775, 131]},
	{"text": "12.4ng/ml，胃泌素释放肽前体 90.5pg/ml；生化系列36项:白蛋白(溴甲酚绿法)", "bbox": [198, 131, 716, 144]},
	{"text": "32.49g/L，脂蛋白(a)343mg/L，唾液酸 769mg/L；N端-B型钠尿肽前体、甲状腺功能3项未", "bbox": [195, 144, 786, 157]},
	{"text": "见异常。常规心电图检查：窦性心动过速。全身骨显像：与本院2025-04-10骨显像比较：1.", "bbox": [195, 157, 792, 170]},
	{"text": "右侧多根肋骨多发异常放射性浓聚灶，病灶数目较前增多，浓聚程度增高，提示骨转移瘤可", "bbox": [195, 170, 796, 183]},
	{"text": "能大，请结合其他检查综合考虑；2.前次检查所示左侧坐骨轻度放射性浓聚灶，本次检查未", "bbox": [195, 183, 798, 196]},
	{"text": "见显示；3.双肩关节及双膝关节区异常放射性浓聚，考虑炎性病变，请结合临床。颅脑平扫", "bbox": [195, 196, 798, 209]},
	{"text": "+DWI+增强+薄层：1.双侧额顶叶及侧脑室旁白质内脱髓鞘改变；2.老年脑改变，双侧额颞部", "bbox": [192, 209, 800, 222]},
	{"text": "少量硬膜下积液；3.部分副鼻窦炎；右侧乳突炎；4.鼻中隔偏曲，双下鼻甲肥大。心脏超声", "bbox": [192, 222, 800, 235]},
	{"text": "检查（含左心功能测定）：静息状态下：心内结构及血流未见明显异常髂静脉及下肢深静脉", "bbox": [190, 235, 803, 248]},
	{"text": "(双侧)：双侧髂静脉及下肢深静脉血流通畅颈部：双侧颈部未见明显增大淋巴结胸部平扫", "bbox": [195, 248, 805, 261]},
	{"text": "+增强：对比2025-08-28CT：1.右肺下叶肺癌，较前增大；右肺小叶间隔增厚，较前略进", "bbox": [188, 261, 784, 275]},
	{"text": "展，考虑癌性淋巴管炎可能；纵隔及双肺门淋巴结，部分较前略增大；考虑右侧胸膜转移，", "bbox": [188, 275, 800, 288]},
	{"text": "较前明显进展，累及邻近右前胸壁及右侧膈肌可能；请结合临床并复查；2.右侧胸腔积液，", "bbox": [188, 288, 800, 301]},
	{"text": "较前变化不著，原右侧胸腔积气吸收；3.左肺小结节，部分较前略增大（如下叶薄层", "bbox": [185, 301, 765, 315]},
	{"text": "img231、243），部分结节较前相仿，建议短期复查；4.右侧第7-9、12肋骨高密度影，较前", "bbox": [185, 315, 811, 328]},
	{"text": "变化不著，转移？建议ECT进一步检查；余所见大致同前。上腹部平扫+增强：考虑肝多发囊", "bbox": [185, 328, 813, 341]},
	{"text": "肿，较2025-08-28变化不明显。下腹部平扫+增强：1.考虑右肾囊肿，较2025-08-28变化不", "bbox": [182, 341, 808, 355]},
	{"text": "著；2.双肾周桥隔略增厚；3.动脉粥样硬化。排除禁忌给予本周期治疗，方案为培美曲塞", "bbox": [182, 355, 802, 368]},
	{"text": "0.8g、信迪利单抗200mg联合恩度 210mg q21d治疗。治疗结束，患者病情稳定，2025-11-14", "bbox": [180, 370, 819, 383]},
	{"text": "办理出院。出院诊断：1.右肺腺癌(T2bN3M1 IV期) 纵隔淋巴结转移 肺门淋巴结转移 胸", "bbox": [180, 383, 813, 397]},
	{"text": "膜转移 骨转移 2.恶性胸腔积液 3.大隐静脉曲张 4.肾囊肿 5.肝囊肿", "bbox": [178, 397, 673, 410]},
	{"text": "患者因“确诊肺腺癌8月余，为继续治疗”于2026-01-08再入院，入院后完善相关辅助", "bbox": [210, 424, 817, 438]},
	{"text": "检查：01-08：急查NT-proBNP、促肾上腺皮质激素(8时)、皮质醇(7:00-10:00am)等未见明", "bbox": [175, 438, 817, 452]},
	{"text": "显异常。急查血常规+CRP+SAA:红细胞 3.93x10^12/L，血红蛋白 118g/L，红细胞压积", "bbox": [175, 452, 789, 466]},
	{"text": "35.8%，红细胞分布宽度SD 47.4fl，中性粒细胞百分率 77.9%，淋巴细胞百分率 9.4%，单", "bbox": [175, 466, 822, 480]},
	{"text": "核细胞百分率 10.2%，淋巴细胞绝对值 0.67×10^9/L，单核细胞绝对值 0.73×10^9/L，超", "bbox": [175, 480, 831, 494]},
	{"text": "敏C-反应蛋白 30.56mg/L，血清淀粉样蛋白A 26.98mg/L；急查心梗三项:超敏肌钙蛋白T", "bbox": [175, 494, 808, 508]},
	{"text": "15.10pg/ml；DIC系列-5项:纤维蛋白原 6.22g/L，D-二聚体 1.66mg/L；急查降钙素原：", "bbox": [175, 508, 800, 522]},
	{"text": "0.0969ng/ml；生化系列36项:白蛋白(溴甲酚绿法) 31.69g/L，白蛋白:球蛋白 0.87，肾小", "bbox": [175, 522, 825, 536]},
	{"text": "球滤过率 89.97ml/(min·1.73m²)，肌酸激酶 38U/L，脂蛋白(a) 452mg/L，唾液酸", "bbox": [175, 536, 778, 550]},
	{"text": "765mg/L；甲状腺功能6项:促甲状腺素 4.69mIU/L；肺肿瘤检验", "bbox": [175, 550, 634, 564]},
	{"text": "癌胚抗原", "bbox": [680, 564, 745, 577]},
	{"text": "73.4ng/ml，神经元特异性烯醇化酶 18.4ng/ml，细胞角蛋白19片段 19.1ng/ml，胃泌素释", "bbox": [175, 577, 827, 591]},
	{"text": "第5页", "bbox": [485, 613, 536, 625]}
]
2026-08-10 18:23:14,531 INFO     29 [qwen-vl-text] coord API: raw_items=37, valid_items=37, elapsed=20.5s
2026-08-10 18:23:14,531 INFO     29 [qwen-vl-text] coord item[0]: text=蛋白原 5.04g/L，D-二聚体 2.19mg/L；皮质醇(7:00-10:00am):皮质醇(7:00-10:00am), bbox=[198, 93, 756, 106]
2026-08-10 18:23:14,531 INFO     29 [qwen-vl-text] coord item[1]: text=286nmol/L；促肾上腺皮质激素(8时):促肾上腺皮质激素(8时)23.3pg/ml；急查心梗三项:, bbox=[198, 106, 780, 118]
2026-08-10 18:23:14,531 INFO     29 [qwen-vl-text] coord item[2]: text=超敏肌钙蛋白T 17.70pg/ml；肺肿瘤检验-莱山:癌胚抗原 75.8ng/ml，细胞角蛋白19片段, bbox=[198, 118, 775, 131]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[3]: text=12.4ng/ml，胃泌素释放肽前体 90.5pg/ml；生化系列36项:白蛋白(溴甲酚绿法), bbox=[198, 131, 716, 144]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[4]: text=32.49g/L，脂蛋白(a)343mg/L，唾液酸 769mg/L；N端-B型钠尿肽前体、甲状腺功能3项未, bbox=[195, 144, 786, 157]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[5]: text=见异常。常规心电图检查：窦性心动过速。全身骨显像：与本院2025-04-10骨显像比较：1., bbox=[195, 157, 792, 170]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[6]: text=右侧多根肋骨多发异常放射性浓聚灶，病灶数目较前增多，浓聚程度增高，提示骨转移瘤可, bbox=[195, 170, 796, 183]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[7]: text=能大，请结合其他检查综合考虑；2.前次检查所示左侧坐骨轻度放射性浓聚灶，本次检查未, bbox=[195, 183, 798, 196]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[8]: text=见显示；3.双肩关节及双膝关节区异常放射性浓聚，考虑炎性病变，请结合临床。颅脑平扫, bbox=[195, 196, 798, 209]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[9]: text=+DWI+增强+薄层：1.双侧额顶叶及侧脑室旁白质内脱髓鞘改变；2.老年脑改变，双侧额颞部, bbox=[192, 209, 800, 222]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[10]: text=少量硬膜下积液；3.部分副鼻窦炎；右侧乳突炎；4.鼻中隔偏曲，双下鼻甲肥大。心脏超声, bbox=[192, 222, 800, 235]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[11]: text=检查（含左心功能测定）：静息状态下：心内结构及血流未见明显异常髂静脉及下肢深静脉, bbox=[190, 235, 803, 248]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[12]: text=(双侧)：双侧髂静脉及下肢深静脉血流通畅颈部：双侧颈部未见明显增大淋巴结胸部平扫, bbox=[195, 248, 805, 261]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[13]: text=+增强：对比2025-08-28CT：1.右肺下叶肺癌，较前增大；右肺小叶间隔增厚，较前略进, bbox=[188, 261, 784, 275]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[14]: text=展，考虑癌性淋巴管炎可能；纵隔及双肺门淋巴结，部分较前略增大；考虑右侧胸膜转移，, bbox=[188, 275, 800, 288]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[15]: text=较前明显进展，累及邻近右前胸壁及右侧膈肌可能；请结合临床并复查；2.右侧胸腔积液，, bbox=[188, 288, 800, 301]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[16]: text=较前变化不著，原右侧胸腔积气吸收；3.左肺小结节，部分较前略增大（如下叶薄层, bbox=[185, 301, 765, 315]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[17]: text=img231、243），部分结节较前相仿，建议短期复查；4.右侧第7-9、12肋骨高密度影，较前, bbox=[185, 315, 811, 328]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[18]: text=变化不著，转移？建议ECT进一步检查；余所见大致同前。上腹部平扫+增强：考虑肝多发囊, bbox=[185, 328, 813, 341]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[19]: text=肿，较2025-08-28变化不明显。下腹部平扫+增强：1.考虑右肾囊肿，较2025-08-28变化不, bbox=[182, 341, 808, 355]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[20]: text=著；2.双肾周桥隔略增厚；3.动脉粥样硬化。排除禁忌给予本周期治疗，方案为培美曲塞, bbox=[182, 355, 802, 368]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[21]: text=0.8g、信迪利单抗200mg联合恩度 210mg q21d治疗。治疗结束，患者病情稳定，2025-11-14, bbox=[180, 370, 819, 383]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[22]: text=办理出院。出院诊断：1.右肺腺癌(T2bN3M1 IV期) 纵隔淋巴结转移 肺门淋巴结转移 胸, bbox=[180, 383, 813, 397]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[23]: text=膜转移 骨转移 2.恶性胸腔积液 3.大隐静脉曲张 4.肾囊肿 5.肝囊肿, bbox=[178, 397, 673, 410]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[24]: text=患者因“确诊肺腺癌8月余，为继续治疗”于2026-01-08再入院，入院后完善相关辅助, bbox=[210, 424, 817, 438]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[25]: text=检查：01-08：急查NT-proBNP、促肾上腺皮质激素(8时)、皮质醇(7:00-10:00am)等未见明, bbox=[175, 438, 817, 452]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[26]: text=显异常。急查血常规+CRP+SAA:红细胞 3.93x10^12/L，血红蛋白 118g/L，红细胞压积, bbox=[175, 452, 789, 466]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[27]: text=35.8%，红细胞分布宽度SD 47.4fl，中性粒细胞百分率 77.9%，淋巴细胞百分率 9.4%，单, bbox=[175, 466, 822, 480]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[28]: text=核细胞百分率 10.2%，淋巴细胞绝对值 0.67×10^9/L，单核细胞绝对值 0.73×10^9/L，超, bbox=[175, 480, 831, 494]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[29]: text=敏C-反应蛋白 30.56mg/L，血清淀粉样蛋白A 26.98mg/L；急查心梗三项:超敏肌钙蛋白T, bbox=[175, 494, 808, 508]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[30]: text=15.10pg/ml；DIC系列-5项:纤维蛋白原 6.22g/L，D-二聚体 1.66mg/L；急查降钙素原：, bbox=[175, 508, 800, 522]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[31]: text=0.0969ng/ml；生化系列36项:白蛋白(溴甲酚绿法) 31.69g/L，白蛋白:球蛋白 0.87，肾小, bbox=[175, 522, 825, 536]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[32]: text=球滤过率 89.97ml/(min·1.73m²)，肌酸激酶 38U/L，脂蛋白(a) 452mg/L，唾液酸, bbox=[175, 536, 778, 550]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[33]: text=765mg/L；甲状腺功能6项:促甲状腺素 4.69mIU/L；肺肿瘤检验, bbox=[175, 550, 634, 564]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[34]: text=癌胚抗原, bbox=[680, 564, 745, 577]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[35]: text=73.4ng/ml，神经元特异性烯醇化酶 18.4ng/ml，细胞角蛋白19片段 19.1ng/ml，胃泌素释, bbox=[175, 577, 827, 591]
2026-08-10 18:23:14,532 INFO     29 [qwen-vl-text] coord item[36]: text=第5页, bbox=[485, 613, 536, 625]
2026-08-10 18:23:14,533 INFO     29 [qwen-vl-text] page=4 — 37/37 coords, api_time=20.5s
2026-08-10 18:23:14,537 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1980171, prompt_len=2265
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共36行）
["放肽前体81.4pg/ml；常规心电图检查（自动分析）：窦性心动过速。下腹部平扫+增强：", "1.考虑右肾囊肿，较2025-11-08变化不著。2.双肾周桥隔略增厚。3.动脉粥样硬化。上腹部", "平扫+增强：考虑肝多发囊肿，较2025-11-08变化不明显。胸部平扫+增强：对比", "2025-11-08CT：1.右肺下叶肺癌，范围整体较前增大；右肺小叶间隔增厚，较前进展，考虑", "癌性淋巴管炎可能；纵隔及双肺门淋巴结大致同前；考虑右侧胸膜转移，较前进展，累及邻", "近右前胸壁及右侧膈肌可能；请结合临床并复查。2.右侧胸腔积液，较前变化不著。3.左肺", "小结节，较前相仿，建议短期复查。4.右侧第7-9、12肋骨高密度影，局部略进展，转移可", "能，建议ECT进一步检查。余所见大致同前。01-09：髂静脉及下肢深静脉、下肢浅静脉：左", "侧大隐静脉曲张左侧隐股静脉瓣功能不全。01-10：心脏超声检查（含左心功能测定）：静", "息状态下：心内结构及血流未见明显异常。考虑患者肿瘤较前进展，请肿瘤科及放疗科会", "诊，给予更换二线化疗方案，排除禁忌，1-09行开始给予恩度抗血管生成，01-12给予二线", "第1周期全身化疗：白蛋白紫杉醇300mg d1、信迪利单抗200mg，01-13给予地舒单抗120mg抗", "骨转移。期间联合护肝、护胃、止吐、激素等治疗，现病情平稳，准予出院。末次出院诊", "断：1.右肺腺癌（T2bN3M1 IV期）纵隔淋巴结转移肺门淋巴结转移胸膜转移骨转移2.", "恶性胸腔积液3.大隐静脉曲张4.肾囊肿5.肝囊肿6.贫血7.低蛋白血症", "患者出院后规律服药、门诊复诊，偶有咳嗽，咳白薄痰，腰肋部水肿，于2026-2-10再", "入院，", "入院后完善辅助检查：NT-proBNP未见明显异常；血常规+CRP+SAA：红细胞", "4.25x10^12/L，血红蛋白125g/L，红细胞压积38.4%，红细胞分布宽度SD47.8fl，中性粒", "细胞百分率83.4%，淋巴细胞百分率8.0%，中性粒细胞绝对值7.35×10^9/L，淋巴细胞绝", "对值0.70×10^9/L，单核细胞绝对值0.62×10^9/L，超敏C-反应蛋白24.16mg/L，血清淀", "粉样蛋白A13.13mg/L；心梗三项：超敏肌钙蛋白T14.10pg/ml；降钙素原：0.0528ng/ml；生", "化系列36项：白蛋白（溴甲酚绿法）34.82g/L，白蛋白：球蛋白1.02，肾小球滤过率", "89.97ml/(min•1.73m²)，肌酸激酶33U/L，脂蛋白(a)510mg/L，唾液酸792mg/L；肺肿瘤", "检验：癌胚抗原100ng/ml，神经元特异性烯醇化酶31.1ng/ml，细胞角蛋白19片段", "28.8ng/ml，胃泌素释放肽前体87.7pg/ml；DIC系列-5项：纤维蛋白原6.71g/L，D-二聚体", "1.42mg/L；心电图：窦性心律大致正常心电图。尿液分析、大便常规及潜血、促肾上腺皮", "质激素(8时)、皮质醇(7:00-10:00am)、甲状腺功能6项等未见明显异常。排除禁忌，02-10", "开始给予恩度抗血管生成，02-11给予二线第2周期全身化疗：白蛋白紫杉醇300mg d1，同时", "辅以激素、止吐、护胃、保肝治疗，同时给予信迪利单抗200mg抗肿瘤免疫治疗，02-12给予", "地舒单抗120mg抗骨转移治疗。于2026-02-13出院。末次出院诊断：1.恶性肿瘤维持性化学", "治疗2.恶性肿瘤免疫治疗3.恶性肿瘤靶向治疗4.右肺腺癌（T2bN3M1 IV期）纵隔淋巴结", "转移肺门淋巴结转移胸膜转移骨转移5.恶性胸腔积液6.大隐静脉曲张7.肾囊肿8.肝", "囊肿。", "患者出院后规律门诊复诊，偶有咳嗽、咳痰，2天前无明显诱因出现咯血，感痰较前增", "第6页"]

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
2026-08-10 18:23:33,753 INFO     29 [qwen-vl-text] coord API raw response (len=3130):
[
	{"text": "放肽前体81.4pg/ml；常规心电图检查（自动分析）：窦性心动过速。下腹部平扫+增强：", "bbox": [185, 88, 768, 101]},
	{"text": "1.考虑右肾囊肿，较2025-11-08变化不著。2.双肾周桥隔略增厚。3.动脉粥样硬化。上腹部", "bbox": [185, 101, 787, 114]},
	{"text": "平扫+增强：考虑肝多发囊肿，较2025-11-08变化不明显。胸部平扫+增强：对比", "bbox": [185, 114, 713, 127]},
	{"text": "2025-11-08CT：1.右肺下叶肺癌，范围整体较前增大；右肺小叶间隔增厚，较前进展，考虑", "bbox": [183, 127, 790, 140]},
	{"text": "癌性淋巴管炎可能；纵隔及双肺门淋巴结大致同前；考虑右侧胸膜转移，较前进展，累及邻", "bbox": [183, 140, 790, 153]},
	{"text": "近右前胸壁及右侧膈肌可能；请结合临床并复查。2.右侧胸腔积液，较前变化不著。3.左肺", "bbox": [183, 153, 790, 166]},
	{"text": "小结节，较前相仿，建议短期复查。4.右侧第7-9、12肋骨高密度影，局部略进展，转移可", "bbox": [183, 166, 787, 179]},
	{"text": "能，建议ECT进一步检查。余所见大致同前。01-09：髂静脉及下肢深静脉、下肢浅静脉：左", "bbox": [183, 179, 795, 192]},
	{"text": "侧大隐静脉曲张左侧隐股静脉瓣功能不全。01-10：心脏超声检查（含左心功能测定）：静", "bbox": [183, 192, 796, 205]},
	{"text": "息状态下：心内结构及血流未见明显异常。考虑患者肿瘤较前进展，请肿瘤科及放疗科会", "bbox": [180, 205, 783, 219]},
	{"text": "诊，给予更换二线化疗方案，排除禁忌，1-09行开始给予恩度抗血管生成，01-12给予二线", "bbox": [178, 219, 793, 232]},
	{"text": "第1周期全身化疗：白蛋白紫杉醇300mg d1、信迪利单抗200mg，01-13给予地舒单抗120mg抗", "bbox": [178, 232, 801, 246]},
	{"text": "骨转移。期间联合护肝、护胃、止吐、激素等治疗，现病情平稳，准予出院。末次出院诊", "bbox": [178, 246, 789, 260]},
	{"text": "断：1.右肺腺癌（T2bN3M1 IV期）纵隔淋巴结转移肺门淋巴结转移胸膜转移骨转移2.", "bbox": [175, 260, 795, 274]},
	{"text": "恶性胸腔积液3.大隐静脉曲张4.肾囊肿5.肝囊肿6.贫血7.低蛋白血症", "bbox": [175, 274, 690, 288]},
	{"text": "患者出院后规律服药、门诊复诊，偶有咳嗽，咳白薄痰，腰肋部水肿，于2026-2-10再", "bbox": [204, 288, 801, 302]},
	{"text": "入院，", "bbox": [171, 309, 208, 323]},
	{"text": "入院后完善辅助检查：NT-proBNP未见明显异常；血常规+CRP+SAA：红细胞", "bbox": [202, 321, 718, 335]},
	{"text": "4.25x10^12/L，血红蛋白125g/L，红细胞压积38.4%，红细胞分布宽度SD47.8fl，中性粒", "bbox": [168, 335, 815, 350]},
	{"text": "细胞百分率83.4%，淋巴细胞百分率8.0%，中性粒细胞绝对值7.35×10^9/L，淋巴细胞绝", "bbox": [168, 349, 816, 364]},
	{"text": "对值0.70×10^9/L，单核细胞绝对值0.62×10^9/L，超敏C-反应蛋白24.16mg/L，血清淀", "bbox": [168, 364, 816, 379]},
	{"text": "粉样蛋白A13.13mg/L；心梗三项：超敏肌钙蛋白T14.10pg/ml；降钙素原：0.0528ng/ml；生", "bbox": [166, 379, 819, 394]},
	{"text": "化系列36项：白蛋白（溴甲酚绿法）34.82g/L，白蛋白：球蛋白1.02，肾小球滤过率", "bbox": [166, 394, 757, 410]},
	{"text": "89.97ml/(min•1.73m²)，肌酸激酶33U/L，脂蛋白(a)510mg/L，唾液酸792mg/L；肺肿瘤", "bbox": [164, 410, 822, 426]},
	{"text": "检验：癌胚抗原100ng/ml，神经元特异性烯醇化酶31.1ng/ml，细胞角蛋白19片段", "bbox": [164, 426, 760, 442]},
	{"text": "28.8ng/ml，胃泌素释放肽前体87.7pg/ml；DIC系列-5项：纤维蛋白原6.71g/L，D-二聚体", "bbox": [162, 442, 818, 458]},
	{"text": "1.42mg/L；心电图：窦性心律大致正常心电图。尿液分析、大便常规及潜血、促肾上腺皮", "bbox": [162, 458, 819, 474]},
	{"text": "质激素(8时)、皮质醇(7:00-10:00am)、甲状腺功能6项等未见明显异常。排除禁忌，02-10", "bbox": [162, 474, 820, 490]},
	{"text": "开始给予恩度抗血管生成，02-11给予二线第2周期全身化疗：白蛋白紫杉醇300mg d1，同时", "bbox": [162, 490, 829, 506]},
	{"text": "辅以激素、止吐、护胃、保肝治疗，同时给予信迪利单抗200mg抗肿瘤免疫治疗，02-12给予", "bbox": [162, 506, 830, 522]},
	{"text": "地舒单抗120mg抗骨转移治疗。于2026-02-13出院。末次出院诊断：1.恶性肿瘤维持性化学", "bbox": [162, 522, 824, 538]},
	{"text": "治疗2.恶性肿瘤免疫治疗3.恶性肿瘤靶向治疗4.右肺腺癌（T2bN3M1 IV期）纵隔淋巴结", "bbox": [162, 538, 833, 554]},
	{"text": "转移肺门淋巴结转移胸膜转移骨转移5.恶性胸腔积液6.大隐静脉曲张7.肾囊肿8.肝", "bbox": [162, 554, 824, 570]},
	{"text": "囊肿。", "bbox": [162, 577, 202, 591]},
	{"text": "患者出院后规律门诊复诊，偶有咳嗽、咳痰，2天前无明显诱因出现咯血，感痰较前增", "bbox": [195, 584, 826, 605]},
	{"text": "第6页", "bbox": [476, 620, 528, 633]}
]
2026-08-10 18:23:33,753 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=19.2s
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[0]: text=放肽前体81.4pg/ml；常规心电图检查（自动分析）：窦性心动过速。下腹部平扫+增强：, bbox=[185, 88, 768, 101]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[1]: text=1.考虑右肾囊肿，较2025-11-08变化不著。2.双肾周桥隔略增厚。3.动脉粥样硬化。上腹部, bbox=[185, 101, 787, 114]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[2]: text=平扫+增强：考虑肝多发囊肿，较2025-11-08变化不明显。胸部平扫+增强：对比, bbox=[185, 114, 713, 127]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[3]: text=2025-11-08CT：1.右肺下叶肺癌，范围整体较前增大；右肺小叶间隔增厚，较前进展，考虑, bbox=[183, 127, 790, 140]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[4]: text=癌性淋巴管炎可能；纵隔及双肺门淋巴结大致同前；考虑右侧胸膜转移，较前进展，累及邻, bbox=[183, 140, 790, 153]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[5]: text=近右前胸壁及右侧膈肌可能；请结合临床并复查。2.右侧胸腔积液，较前变化不著。3.左肺, bbox=[183, 153, 790, 166]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[6]: text=小结节，较前相仿，建议短期复查。4.右侧第7-9、12肋骨高密度影，局部略进展，转移可, bbox=[183, 166, 787, 179]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[7]: text=能，建议ECT进一步检查。余所见大致同前。01-09：髂静脉及下肢深静脉、下肢浅静脉：左, bbox=[183, 179, 795, 192]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[8]: text=侧大隐静脉曲张左侧隐股静脉瓣功能不全。01-10：心脏超声检查（含左心功能测定）：静, bbox=[183, 192, 796, 205]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[9]: text=息状态下：心内结构及血流未见明显异常。考虑患者肿瘤较前进展，请肿瘤科及放疗科会, bbox=[180, 205, 783, 219]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[10]: text=诊，给予更换二线化疗方案，排除禁忌，1-09行开始给予恩度抗血管生成，01-12给予二线, bbox=[178, 219, 793, 232]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[11]: text=第1周期全身化疗：白蛋白紫杉醇300mg d1、信迪利单抗200mg，01-13给予地舒单抗120mg抗, bbox=[178, 232, 801, 246]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[12]: text=骨转移。期间联合护肝、护胃、止吐、激素等治疗，现病情平稳，准予出院。末次出院诊, bbox=[178, 246, 789, 260]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[13]: text=断：1.右肺腺癌（T2bN3M1 IV期）纵隔淋巴结转移肺门淋巴结转移胸膜转移骨转移2., bbox=[175, 260, 795, 274]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[14]: text=恶性胸腔积液3.大隐静脉曲张4.肾囊肿5.肝囊肿6.贫血7.低蛋白血症, bbox=[175, 274, 690, 288]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[15]: text=患者出院后规律服药、门诊复诊，偶有咳嗽，咳白薄痰，腰肋部水肿，于2026-2-10再, bbox=[204, 288, 801, 302]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[16]: text=入院，, bbox=[171, 309, 208, 323]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[17]: text=入院后完善辅助检查：NT-proBNP未见明显异常；血常规+CRP+SAA：红细胞, bbox=[202, 321, 718, 335]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[18]: text=4.25x10^12/L，血红蛋白125g/L，红细胞压积38.4%，红细胞分布宽度SD47.8fl，中性粒, bbox=[168, 335, 815, 350]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[19]: text=细胞百分率83.4%，淋巴细胞百分率8.0%，中性粒细胞绝对值7.35×10^9/L，淋巴细胞绝, bbox=[168, 349, 816, 364]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[20]: text=对值0.70×10^9/L，单核细胞绝对值0.62×10^9/L，超敏C-反应蛋白24.16mg/L，血清淀, bbox=[168, 364, 816, 379]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[21]: text=粉样蛋白A13.13mg/L；心梗三项：超敏肌钙蛋白T14.10pg/ml；降钙素原：0.0528ng/ml；生, bbox=[166, 379, 819, 394]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[22]: text=化系列36项：白蛋白（溴甲酚绿法）34.82g/L，白蛋白：球蛋白1.02，肾小球滤过率, bbox=[166, 394, 757, 410]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[23]: text=89.97ml/(min•1.73m²)，肌酸激酶33U/L，脂蛋白(a)510mg/L，唾液酸792mg/L；肺肿瘤, bbox=[164, 410, 822, 426]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[24]: text=检验：癌胚抗原100ng/ml，神经元特异性烯醇化酶31.1ng/ml，细胞角蛋白19片段, bbox=[164, 426, 760, 442]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[25]: text=28.8ng/ml，胃泌素释放肽前体87.7pg/ml；DIC系列-5项：纤维蛋白原6.71g/L，D-二聚体, bbox=[162, 442, 818, 458]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[26]: text=1.42mg/L；心电图：窦性心律大致正常心电图。尿液分析、大便常规及潜血、促肾上腺皮, bbox=[162, 458, 819, 474]
2026-08-10 18:23:33,754 INFO     29 [qwen-vl-text] coord item[27]: text=质激素(8时)、皮质醇(7:00-10:00am)、甲状腺功能6项等未见明显异常。排除禁忌，02-10, bbox=[162, 474, 820, 490]
2026-08-10 18:23:33,755 INFO     29 [qwen-vl-text] coord item[28]: text=开始给予恩度抗血管生成，02-11给予二线第2周期全身化疗：白蛋白紫杉醇300mg d1，同时, bbox=[162, 490, 829, 506]
2026-08-10 18:23:33,755 INFO     29 [qwen-vl-text] coord item[29]: text=辅以激素、止吐、护胃、保肝治疗，同时给予信迪利单抗200mg抗肿瘤免疫治疗，02-12给予, bbox=[162, 506, 830, 522]
2026-08-10 18:23:33,755 INFO     29 [qwen-vl-text] coord item[30]: text=地舒单抗120mg抗骨转移治疗。于2026-02-13出院。末次出院诊断：1.恶性肿瘤维持性化学, bbox=[162, 522, 824, 538]
2026-08-10 18:23:33,755 INFO     29 [qwen-vl-text] coord item[31]: text=治疗2.恶性肿瘤免疫治疗3.恶性肿瘤靶向治疗4.右肺腺癌（T2bN3M1 IV期）纵隔淋巴结, bbox=[162, 538, 833, 554]
2026-08-10 18:23:33,755 INFO     29 [qwen-vl-text] coord item[32]: text=转移肺门淋巴结转移胸膜转移骨转移5.恶性胸腔积液6.大隐静脉曲张7.肾囊肿8.肝, bbox=[162, 554, 824, 570]
2026-08-10 18:23:33,755 INFO     29 [qwen-vl-text] coord item[33]: text=囊肿。, bbox=[162, 577, 202, 591]
2026-08-10 18:23:33,755 INFO     29 [qwen-vl-text] coord item[34]: text=患者出院后规律门诊复诊，偶有咳嗽、咳痰，2天前无明显诱因出现咯血，感痰较前增, bbox=[195, 584, 826, 605]
2026-08-10 18:23:33,755 INFO     29 [qwen-vl-text] coord item[35]: text=第6页, bbox=[476, 620, 528, 633]
2026-08-10 18:23:33,755 INFO     29 [qwen-vl-text] page=5 — 36/36 coords, api_time=19.2s
2026-08-10 18:23:33,758 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1719007, prompt_len=1649
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共30行）
["多，每天数十口，色鲜红，今为进一步治疗入院。患者病后神志清，精神状态一般，食欲一", "般，睡眠良好，大便正常，小便正常，体力情况一般，体重无明显变化。", "既往史：否认食物、药物过敏史，参阅既往入院记录。", "个人史：参阅既往入院记录。", "家族史：参阅既往入院记录。", "体 格 检 查", "T 36.3℃ P 107次/分 R 21次/分 Bp 144/99mmHg", "发育正常，营养良好，正常面容，表情自如，自主体位，神志清楚，查体合作。全身皮", "肤粘膜无黄染，无皮疹，无皮下出血，无皮下结节，皮下无水肿，无肝掌、蜘蛛痣，毛发分", "布均匀。全身浅表淋巴结无肿大。眼睑无水肿，结膜无苍白，眼球无突出，无震颤，巩膜无", "黄染，瞳孔等大等圆，对光反射灵敏，耳廓对称，无畸形，牵拉无疼痛，外耳道无异常分泌", "物，乳突无压痛，无听力粗试障碍。鼻无畸形。口唇无发绀，口腔粘膜无充血、糜烂。舌苔", "薄白，伸舌无偏斜、震颤，牙龈无红肿，咽部粘膜无充血，扁桃体无肿大。颈软无抵抗，颈", "动脉无异常搏动，半坐位颈静脉未见充盈，颈部大血管区未闻及血管杂音。气管居中，肝颈", "静脉回流征阴性，甲状腺无肿大，无压痛、震颤、血管杂音。胸廓无畸形，呼吸运动两侧对", "称，肋间隙无狭窄或饱满，胸壁无压痛，语颤无增强、减弱，胸骨无压痛。双肺叩诊清音，", "呼吸规整，双肺呼吸音低，未闻及干湿性啰音，无胸膜摩擦音。心前区无异常隆起、异常搏", "动、震颤，心浊音界不大，心率107次/分，律齐，心音有力，各瓣膜听诊区未闻及杂音，无", "心包摩擦音。腹平坦，软，无压痛、反跳痛，腹部无包块。肝脏未触及，脾脏未触及，", "Murphy氏征阴性，肾区无叩击痛，无移动性浊音。肠鸣音正常，4次/分。肛门及外生殖器未", "查。脊柱正常生理弯曲，四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾），关节无肿", "胀、压痛，下肢无浮肿。", "肌肉无压痛，四肢肌力、肌张力未见异常，双侧肱", "二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性。", "专科检查： 胸廓无畸形，呼吸运动两侧对称，肋间隙无狭窄或饱满，胸壁无压痛，语", "颤无增强、减弱，胸骨无压痛。双肺叩诊清音，呼吸规整，双肺呼吸音低，未闻及干湿性啰", "音，无胸膜摩擦音。", "辅 助 检 查", "检查日期 项目 结果 检查单位 检查编号", "第 7 页"]

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
2026-08-10 18:23:46,510 INFO     29 [qwen-vl-text] coord API raw response (len=2268):
[
	{"text": "多，每天数十口，色鲜红，今为进一步治疗入院。患者病后神志清，精神状态一般，食欲一", "bbox": [200, 94, 802, 107]},
	{"text": "般，睡眠良好，大便正常，小便正常，体力情况一般，体重无明显变化。", "bbox": [200, 107, 677, 120]},
	{"text": "既往史：否认食物、药物过敏史，参阅既往入院记录。", "bbox": [230, 120, 588, 133]},
	{"text": "个人史：参阅既往入院记录。", "bbox": [230, 134, 422, 147]},
	{"text": "家族史：参阅既往入院记录。", "bbox": [230, 148, 422, 160]},
	{"text": "体 格 检 查", "bbox": [450, 160, 558, 173]},
	{"text": "T 36.3℃ P 107次/分 R 21次/分 Bp 144/99mmHg", "bbox": [236, 188, 720, 202]},
	{"text": "发育正常，营养良好，正常面容，表情自如，自主体位，神志清楚，查体合作。全身皮", "bbox": [200, 200, 815, 216]},
	{"text": "肤粘膜无黄染，无皮疹，无皮下出血，无皮下结节，皮下无水肿，无肝掌、蜘蛛痣，毛发分", "bbox": [198, 214, 813, 230]},
	{"text": "布均匀。全身浅表淋巴结无肿大。眼睑无水肿，结膜无苍白，眼球无突出，无震颤，巩膜无", "bbox": [198, 228, 815, 244]},
	{"text": "黄染，瞳孔等大等圆，对光反射灵敏，耳廓对称，无畸形，牵拉无疼痛，外耳道无异常分泌", "bbox": [198, 242, 815, 258]},
	{"text": "物，乳突无压痛，无听力粗试障碍。鼻无畸形。口唇无发绀，口腔粘膜无充血、糜烂。舌苔", "bbox": [198, 256, 815, 272]},
	{"text": "薄白，伸舌无偏斜、震颤，牙龈无红肿，咽部粘膜无充血，扁桃体无肿大。颈软无抵抗，颈", "bbox": [198, 270, 818, 286]},
	{"text": "动脉无异常搏动，半坐位颈静脉未见充盈，颈部大血管区未闻及血管杂音。气管居中，肝颈", "bbox": [198, 284, 818, 300]},
	{"text": "静脉回流征阴性，甲状腺无肿大，无压痛、震颤、血管杂音。胸廓无畸形，呼吸运动两侧对", "bbox": [198, 298, 818, 314]},
	{"text": "称，肋间隙无狭窄或饱满，胸壁无压痛，语颤无增强、减弱，胸骨无压痛。双肺叩诊清音，", "bbox": [198, 312, 815, 328]},
	{"text": "呼吸规整，双肺呼吸音低，未闻及干湿性啰音，无胸膜摩擦音。心前区无异常隆起、异常搏", "bbox": [198, 326, 821, 343]},
	{"text": "动、震颤，心浊音界不大，心率107次/分，律齐，心音有力，各瓣膜听诊区未闻及杂音，无", "bbox": [198, 341, 823, 357]},
	{"text": "心包摩擦音。腹平坦，软，无压痛、反跳痛，腹部无包块。肝脏未触及，脾脏未触及，", "bbox": [198, 355, 784, 372]},
	{"text": "Murphy氏征阴性，肾区无叩击痛，无移动性浊音。肠鸣音正常，4次/分。肛门及外生殖器未", "bbox": [196, 370, 825, 387]},
	{"text": "查。脊柱正常生理弯曲，四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾），关节无肿", "bbox": [196, 385, 825, 402]},
	{"text": "胀、压痛，下肢无浮肿。", "bbox": [194, 405, 364, 421]},
	{"text": "肌肉无压痛，四肢肌力、肌张力未见异常，双侧肱", "bbox": [450, 401, 798, 417]},
	{"text": "二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性。", "bbox": [194, 419, 697, 436]},
	{"text": "专科检查： 胸廓无畸形，呼吸运动两侧对称，肋间隙无狭窄或饱满，胸壁无压痛，语", "bbox": [194, 433, 831, 450]},
	{"text": "颤无增强、减弱，胸骨无压痛。双肺叩诊清音，呼吸规整，双肺呼吸音低，未闻及干湿性啰", "bbox": [194, 447, 831, 464]},
	{"text": "音，无胸膜摩擦音。", "bbox": [194, 469, 330, 484]},
	{"text": "辅 助 检 查", "bbox": [455, 481, 570, 495]},
	{"text": "检查日期 项目 结果 检查单位 检查编号", "bbox": [200, 508, 827, 528]},
	{"text": "第 7 页", "bbox": [496, 614, 545, 625]}
]
2026-08-10 18:23:46,510 INFO     29 [qwen-vl-text] coord API: raw_items=30, valid_items=30, elapsed=12.8s
2026-08-10 18:23:46,510 INFO     29 [qwen-vl-text] coord item[0]: text=多，每天数十口，色鲜红，今为进一步治疗入院。患者病后神志清，精神状态一般，食欲一, bbox=[200, 94, 802, 107]
2026-08-10 18:23:46,511 INFO     29 [qwen-vl-text] coord item[1]: text=般，睡眠良好，大便正常，小便正常，体力情况一般，体重无明显变化。, bbox=[200, 107, 677, 120]
2026-08-10 18:23:46,511 INFO     29 [qwen-vl-text] coord item[2]: text=既往史：否认食物、药物过敏史，参阅既往入院记录。, bbox=[230, 120, 588, 133]
2026-08-10 18:23:46,511 INFO     29 [qwen-vl-text] coord item[3]: text=个人史：参阅既往入院记录。, bbox=[230, 134, 422, 147]
2026-08-10 18:23:46,511 INFO     29 [qwen-vl-text] coord item[4]: text=家族史：参阅既往入院记录。, bbox=[230, 148, 422, 160]
2026-08-10 18:23:46,511 INFO     29 [qwen-vl-text] coord item[5]: text=体 格 检 查, bbox=[450, 160, 558, 173]
2026-08-10 18:23:46,511 INFO     29 [qwen-vl-text] coord item[6]: text=T 36.3℃ P 107次/分 R 21次/分 Bp 144/99mmHg, bbox=[236, 188, 720, 202]
2026-08-10 18:23:46,511 INFO     29 [qwen-vl-text] coord item[7]: text=发育正常，营养良好，正常面容，表情自如，自主体位，神志清楚，查体合作。全身皮, bbox=[200, 200, 815, 216]
2026-08-10 18:23:46,511 INFO     29 [qwen-vl-text] coord item[8]: text=肤粘膜无黄染，无皮疹，无皮下出血，无皮下结节，皮下无水肿，无肝掌、蜘蛛痣，毛发分, bbox=[198, 214, 813, 230]
2026-08-10 18:23:46,511 INFO     29 [qwen-vl-text] coord item[9]: text=布均匀。全身浅表淋巴结无肿大。眼睑无水肿，结膜无苍白，眼球无突出，无震颤，巩膜无, bbox=[198, 228, 815, 244]
2026-08-10 18:23:46,511 INFO     29 [qwen-vl-text] coord item[10]: text=黄染，瞳孔等大等圆，对光反射灵敏，耳廓对称，无畸形，牵拉无疼痛，外耳道无异常分泌, bbox=[198, 242, 815, 258]
2026-08-10 18:23:46,511 INFO     29 [qwen-vl-text] coord item[11]: text=物，乳突无压痛，无听力粗试障碍。鼻无畸形。口唇无发绀，口腔粘膜无充血、糜烂。舌苔, bbox=[198, 256, 815, 272]
2026-08-10 18:23:46,511 INFO     29 [qwen-vl-text] coord item[12]: text=薄白，伸舌无偏斜、震颤，牙龈无红肿，咽部粘膜无充血，扁桃体无肿大。颈软无抵抗，颈, bbox=[198, 270, 818, 286]
2026-08-10 18:23:46,511 INFO     29 [qwen-vl-text] coord item[13]: text=动脉无异常搏动，半坐位颈静脉未见充盈，颈部大血管区未闻及血管杂音。气管居中，肝颈, bbox=[198, 284, 818, 300]
2026-08-10 18:23:46,511 INFO     29 [qwen-vl-text] coord item[14]: text=静脉回流征阴性，甲状腺无肿大，无压痛、震颤、血管杂音。胸廓无畸形，呼吸运动两侧对, bbox=[198, 298, 818, 314]
2026-08-10 18:23:46,512 INFO     29 [qwen-vl-text] coord item[15]: text=称，肋间隙无狭窄或饱满，胸壁无压痛，语颤无增强、减弱，胸骨无压痛。双肺叩诊清音，, bbox=[198, 312, 815, 328]
2026-08-10 18:23:46,512 INFO     29 [qwen-vl-text] coord item[16]: text=呼吸规整，双肺呼吸音低，未闻及干湿性啰音，无胸膜摩擦音。心前区无异常隆起、异常搏, bbox=[198, 326, 821, 343]
2026-08-10 18:23:46,512 INFO     29 [qwen-vl-text] coord item[17]: text=动、震颤，心浊音界不大，心率107次/分，律齐，心音有力，各瓣膜听诊区未闻及杂音，无, bbox=[198, 341, 823, 357]
2026-08-10 18:23:46,512 INFO     29 [qwen-vl-text] coord item[18]: text=心包摩擦音。腹平坦，软，无压痛、反跳痛，腹部无包块。肝脏未触及，脾脏未触及，, bbox=[198, 355, 784, 372]
2026-08-10 18:23:46,512 INFO     29 [qwen-vl-text] coord item[19]: text=Murphy氏征阴性，肾区无叩击痛，无移动性浊音。肠鸣音正常，4次/分。肛门及外生殖器未, bbox=[196, 370, 825, 387]
2026-08-10 18:23:46,512 INFO     29 [qwen-vl-text] coord item[20]: text=查。脊柱正常生理弯曲，四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾），关节无肿, bbox=[196, 385, 825, 402]
2026-08-10 18:23:46,512 INFO     29 [qwen-vl-text] coord item[21]: text=胀、压痛，下肢无浮肿。, bbox=[194, 405, 364, 421]
2026-08-10 18:23:46,512 INFO     29 [qwen-vl-text] coord item[22]: text=肌肉无压痛，四肢肌力、肌张力未见异常，双侧肱, bbox=[450, 401, 798, 417]
2026-08-10 18:23:46,512 INFO     29 [qwen-vl-text] coord item[23]: text=二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性。, bbox=[194, 419, 697, 436]
2026-08-10 18:23:46,512 INFO     29 [qwen-vl-text] coord item[24]: text=专科检查： 胸廓无畸形，呼吸运动两侧对称，肋间隙无狭窄或饱满，胸壁无压痛，语, bbox=[194, 433, 831, 450]
2026-08-10 18:23:46,512 INFO     29 [qwen-vl-text] coord item[25]: text=颤无增强、减弱，胸骨无压痛。双肺叩诊清音，呼吸规整，双肺呼吸音低，未闻及干湿性啰, bbox=[194, 447, 831, 464]
2026-08-10 18:23:46,512 INFO     29 [qwen-vl-text] coord item[26]: text=音，无胸膜摩擦音。, bbox=[194, 469, 330, 484]
2026-08-10 18:23:46,512 INFO     29 [qwen-vl-text] coord item[27]: text=辅 助 检 查, bbox=[455, 481, 570, 495]
2026-08-10 18:23:46,512 INFO     29 [qwen-vl-text] coord item[28]: text=检查日期 项目 结果 检查单位 检查编号, bbox=[200, 508, 827, 528]
2026-08-10 18:23:46,512 INFO     29 [qwen-vl-text] coord item[29]: text=第 7 页, bbox=[496, 614, 545, 625]
2026-08-10 18:23:46,513 INFO     29 [qwen-vl-text] page=6 — 30/30 coords, api_time=12.8s
2026-08-10 18:23:46,518 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1344314, prompt_len=1033
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["2025-04-09", "病理", "(胸膜活检)送检增生的纤维组", "织内见腺癌浸润，请结合临床诊", "治。免疫组化：TTF-1（-）、", "NapsinA（-）、CK7（+）、CK5/6", "（部分+）、P40（点灶+）、CR（", "灶+）、ALK（1A4）（-）、Ki67", "(+,40%）。C-MET免疫组化检测", "报告检测平台：Roche Ventana", "Benchmark Ultra；抗体克隆号：", "SP44,Roche；表达部位：细胞膜和", "细胞浆；阳性强度及百分比：++(", "40%),+(60%)阳性等级：1+", "细胞数量：≥100。", "初步诊断：", "1.咯血", "2.右肺腺癌（T2bN3M1 IV期）", "纵隔淋巴结转移", "肺门淋巴结转移", "胸膜转移", "骨转移", "3.恶性胸腔积液", "4.大隐静脉曲张", "5.肾囊肿", "6.肝囊肿"]

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
2026-08-10 18:23:53,978 INFO     29 [qwen-vl-text] coord API raw response (len=1486):
[
	{"text": "2025-04-09", "bbox": [204, 90, 277, 100]},
	{"text": "病理", "bbox": [310, 90, 340, 100]},
	{"text": "(胸膜活检)送检增生的纤维组", "bbox": [389, 91, 582, 102]},
	{"text": "织内见腺癌浸润，请结合临床诊", "bbox": [383, 104, 582, 114]},
	{"text": "治。免疫组化：TTF-1（-）、", "bbox": [383, 116, 561, 127]},
	{"text": "NapsinA（-）、CK7（+）、CK5/6", "bbox": [383, 129, 590, 139]},
	{"text": "（部分+）、P40（点灶+）、CR（", "bbox": [388, 141, 590, 152]},
	{"text": "灶+）、ALK（1A4）（-）、Ki67", "bbox": [381, 154, 584, 164]},
	{"text": "(+,40%）。C-MET免疫组化检测", "bbox": [387, 167, 584, 177]},
	{"text": "报告检测平台：Roche Ventana", "bbox": [381, 180, 570, 190]},
	{"text": "Benchmark Ultra；抗体克隆号：", "bbox": [380, 193, 584, 203]},
	{"text": "SP44,Roche；表达部位：细胞膜和", "bbox": [380, 205, 592, 216]},
	{"text": "细胞浆；阳性强度及百分比：++(", "bbox": [380, 218, 586, 229]},
	{"text": "40%),+(60%)阳性等级：1+", "bbox": [380, 231, 542, 242]},
	{"text": "细胞数量：≥100。", "bbox": [379, 244, 490, 255]},
	{"text": "初步诊断：", "bbox": [482, 272, 548, 284]},
	{"text": "1.咯血", "bbox": [497, 287, 542, 298]},
	{"text": "2.右肺腺癌（T2bN3M1 IV期）", "bbox": [497, 300, 686, 311]},
	{"text": "纵隔淋巴结转移", "bbox": [527, 314, 633, 325]},
	{"text": "肺门淋巴结转移", "bbox": [527, 328, 633, 339]},
	{"text": "胸膜转移", "bbox": [527, 342, 589, 353]},
	{"text": "骨转移", "bbox": [527, 356, 574, 367]},
	{"text": "3.恶性胸腔积液", "bbox": [497, 370, 605, 381]},
	{"text": "4.大隐静脉曲张", "bbox": [497, 384, 605, 395]},
	{"text": "5.肾囊肿", "bbox": [497, 398, 559, 410]},
	{"text": "6.肝囊肿", "bbox": [497, 412, 559, 424]}
]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=7.5s
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[0]: text=2025-04-09, bbox=[204, 90, 277, 100]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[1]: text=病理, bbox=[310, 90, 340, 100]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[2]: text=(胸膜活检)送检增生的纤维组, bbox=[389, 91, 582, 102]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[3]: text=织内见腺癌浸润，请结合临床诊, bbox=[383, 104, 582, 114]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[4]: text=治。免疫组化：TTF-1（-）、, bbox=[383, 116, 561, 127]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[5]: text=NapsinA（-）、CK7（+）、CK5/6, bbox=[383, 129, 590, 139]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[6]: text=（部分+）、P40（点灶+）、CR（, bbox=[388, 141, 590, 152]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[7]: text=灶+）、ALK（1A4）（-）、Ki67, bbox=[381, 154, 584, 164]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[8]: text=(+,40%）。C-MET免疫组化检测, bbox=[387, 167, 584, 177]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[9]: text=报告检测平台：Roche Ventana, bbox=[381, 180, 570, 190]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[10]: text=Benchmark Ultra；抗体克隆号：, bbox=[380, 193, 584, 203]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[11]: text=SP44,Roche；表达部位：细胞膜和, bbox=[380, 205, 592, 216]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[12]: text=细胞浆；阳性强度及百分比：++(, bbox=[380, 218, 586, 229]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[13]: text=40%),+(60%)阳性等级：1+, bbox=[380, 231, 542, 242]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[14]: text=细胞数量：≥100。, bbox=[379, 244, 490, 255]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[15]: text=初步诊断：, bbox=[482, 272, 548, 284]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[16]: text=1.咯血, bbox=[497, 287, 542, 298]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[17]: text=2.右肺腺癌（T2bN3M1 IV期）, bbox=[497, 300, 686, 311]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[18]: text=纵隔淋巴结转移, bbox=[527, 314, 633, 325]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[19]: text=肺门淋巴结转移, bbox=[527, 328, 633, 339]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[20]: text=胸膜转移, bbox=[527, 342, 589, 353]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[21]: text=骨转移, bbox=[527, 356, 574, 367]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[22]: text=3.恶性胸腔积液, bbox=[497, 370, 605, 381]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[23]: text=4.大隐静脉曲张, bbox=[497, 384, 605, 395]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[24]: text=5.肾囊肿, bbox=[497, 398, 559, 410]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] coord item[25]: text=6.肝囊肿, bbox=[497, 412, 559, 424]
2026-08-10 18:23:53,979 INFO     29 [qwen-vl-text] page=7 — 26/26 coords, api_time=7.5s
2026-08-10 18:23:53,980 INFO     29 [qwen-vl-text] new_positions (275):
[[0, 133.94249725341797, 169.06519653320314, 74.0872021484375, 83.34810241699219], [0, 294.07819396972656, 336.34449310302733, 74.0872021484375, 83.34810241699219], [0, 133.94249725341797, 176.80409637451172, 84.19000244140625, 93.45090270996094], [0, 294.07819396972656, 404.2086917114258, 84.19000244140625, 93.45090270996094], [0, 133.94249725341797, 176.80409637451172, 94.292802734375, 103.5537030029297], [0, 294.07819396972656, 404.2086917114258, 94.292802734375, 103.5537030029297], [0, 133.94249725341797, 176.80409637451172, 104.39560302734375, 113.65650329589845], [0, 294.07819396972656, 379.8013922119141, 104.39560302734375, 113.65650329589845], [0, 133.94249725341797, 290.50639404296874, 115.34030334472656, 124.60120361328126], [0, 132.15659729003906, 447.07029083251956, 126.28500366210938, 135.54590393066405], [0, 113.10699768066407, 460.76219055175784, 137.2297039794922, 146.49060424804688], [0, 113.10699768066407, 461.3574905395508, 148.174404296875, 157.4353045654297], [0, 113.10699768066407, 445.2843908691406, 159.11910461425782, 168.3800048828125], [0, 113.10699768066407, 458.9762905883789, 170.06380493164062, 179.32470520019533], [0, 113.10699768066407, 459.5715905761719, 181.00850524902344, 190.26940551757812], [0, 113.10699768066407, 464.33399047851566, 191.95320556640627, 202.056005859375], [0, 111.91639770507813, 453.02329071044926, 202.89790588378906, 213.00070617675783], [0, 111.91639770507813, 462.5480905151367, 213.8426062011719, 223.94540649414063], [0, 111.91639770507813, 462.5480905151367, 225.62920654296875, 235.7320068359375], [0, 110.13049774169923, 464.33399047851566, 236.57390686035157, 246.6767071533203], [0, 110.13049774169923, 452.42799072265626, 248.36050720214845, 258.4633074951172], [0, 108.34459777832032, 470.28699035644536, 259.3052075195313, 269.4080078125], [0, 108.34459777832032, 467.3104904174805, 270.2499078369141, 280.35270812988284], [0, 108.34459777832032, 468.5010903930664, 282.03650817871096, 292.1393084716797], [0, 107.15399780273438, 473.8587902832031, 293.82310852050784, 303.92590881347655], [0, 107.15399780273438, 474.4540902709961, 305.6097088623047, 315.71250915527344], [0, 105.96339782714844, 470.28699035644536, 317.39630920410156, 327.4991094970703], [0, 105.96339782714844, 476.239990234375, 329.18290954589844, 339.2857098388672], [0, 105.96339782714844, 476.835290222168, 340.9695098876953, 351.0723101806641], [0, 104.7727978515625, 470.28699035644536, 352.7561102294922, 362.858910522461], [0, 104.17749786376953, 479.8117901611328, 364.5427105712891, 374.6455108642578], [0, 104.17749786376953, 224.42809539794922, 385.59021118164065, 396.53491149902345], [0, 123.22709747314454, 471.4775903320313, 394.00921142578125, 407.47961181640625], [0, 104.17749786376953, 439.9266909790039, 407.47961181640625, 420.95001220703125], [0, 104.17749786376953, 476.239990234375, 419.26621215820313, 432.73661254882813], [0, 104.17749786376953, 481.00239013671876, 431.0528125, 444.523212890625], [0, 104.17749786376953, 481.59769012451176, 442.8394128417969, 457.15171325683593], [0, 282.1721942138672, 311.34189361572265, 471.464013671875, 480.7249139404297], [1, 107.15399780273438, 458.38099060058596, 74.0872021484375, 84.19000244140625], [1, 107.15399780273438, 464.33399047851566, 84.19000244140625, 95.13470275878906], [1, 107.15399780273438, 460.76219055175784, 95.13470275878906, 106.07940307617189], [1, 107.15399780273438, 466.11989044189454, 106.07940307617189, 117.0241033935547], [1, 105.96339782714844, 454.2138906860352, 117.0241033935547, 127.96880371093751], [1, 122.63179748535157, 454.2138906860352, 127.96880371093751, 138.91350402832032], [1, 105.96339782714844, 467.3104904174805, 138.91350402832032, 149.85820434570314], [1, 107.15399780273438, 466.11989044189454, 149.85820434570314, 160.80290466308594], [1, 104.17749786376953, 471.4775903320313, 160.80290466308594, 171.74760498046876], [1, 102.98689788818359, 467.3104904174805, 171.74760498046876, 182.69230529785156], [1, 102.39159790039064, 417.90059143066406, 182.69230529785156, 194.47890563964845], [1, 101.79629791259767, 465.5245904541016, 194.47890563964845, 206.26550598144533], [1, 101.2009979248047, 475.64469024658206, 206.26550598144533, 218.05210632324219], [1, 100.60569793701173, 472.6681903076172, 218.05210632324219, 229.83870666503907], [1, 99.41509796142579, 464.33399047851566, 229.83870666503907, 241.62530700683595], [1, 99.41509796142579, 474.4540902709961, 241.62530700683595, 253.4119073486328], [1, 98.22449798583985, 470.8822903442383, 253.4119073486328, 265.1985076904297], [1, 97.62919799804688, 476.239990234375, 265.1985076904297, 276.98510803222655], [1, 97.0338980102539, 473.2634902954102, 277.82700805664064, 289.6136083984375], [1, 95.24799804687501, 482.7882901000977, 290.45550842285155, 303.0840087890625], [1, 94.65269805908204, 483.97889007568364, 303.0840087890625, 315.71250915527344], [1, 94.05739807128907, 451.2373907470703, 315.71250915527344, 328.3410095214844], [1, 113.70229766845704, 470.28699035644536, 330.0248095703125, 345.17901000976565], [1, 92.86679809570313, 486.3600900268555, 344.33710998535156, 359.4913104248047], [1, 92.86679809570313, 486.3600900268555, 357.80751037597656, 372.9617108154297], [1, 92.86679809570313, 482.1929901123047, 371.27791076660156, 386.4321112060547], [1, 92.86679809570313, 482.1929901123047, 384.74831115722657, 399.9025115966797], [1, 92.86679809570313, 311.93719360351565, 399.9025115966797, 414.2148120117188], [1, 113.70229766845704, 487.55069000244146, 410.84721191406254, 426.8433123779297], [1, 94.05739807128907, 482.1929901123047, 424.31761230468754, 439.47181274414066], [1, 94.05739807128907, 482.1929901123047, 436.10421264648437, 452.1003131103516], [1, 94.05739807128907, 486.95539001464846, 448.73271301269534, 464.7288134765625], [1, 94.05739807128907, 482.1929901123047, 461.36121337890626, 477.35731384277346], [1, 95.24799804687501, 392.8979919433594, 475.67351379394535, 490.82771423339847], [1, 116.08349761962891, 482.1929901123047, 487.46011413574223, 503.4562145996094], [1, 279.79099426269534, 309.5559936523438, 516.0847149658204, 526.1875152587891], [2, 113.10699768066407, 452.42799072265626, 79.13860229492188, 90.92520263671875], [2, 113.10699768066407, 453.6185906982422, 90.08330261230469, 101.0280029296875], [2, 113.10699768066407, 454.80919067382814, 99.34420288085938, 111.13080322265625], [2, 113.10699768066407, 426.23479125976564, 110.2889031982422, 121.233603515625], [2, 113.10699768066407, 417.90059143066406, 120.39170349121095, 132.17830383300782], [2, 113.10699768066407, 458.38099060058596, 130.4945037841797, 142.28110412597655], [2, 113.10699768066407, 454.80919067382814, 140.59730407714844, 152.38390441894532], [2, 111.91639770507813, 460.76219055175784, 150.7001043701172, 163.32860473632812], [2, 111.91639770507813, 461.9527905273438, 161.6448046875, 173.43140502929688], [2, 111.91639770507813, 463.1433905029297, 171.74760498046876, 183.53420532226562], [2, 111.91639770507813, 463.1433905029297, 181.8504052734375, 194.47890563964845], [2, 111.91639770507813, 469.69169036865236, 192.79510559082033, 205.42360595703127], [2, 111.91639770507813, 466.71519042968754, 203.73980590820312, 216.36830627441407], [2, 108.34459777832032, 471.4775903320313, 214.68450622558595, 227.3130065917969], [2, 108.34459777832032, 468.5010903930664, 225.62920654296875, 238.2577069091797], [2, 107.15399780273438, 468.5010903930664, 236.57390686035157, 249.2024072265625], [2, 107.15399780273438, 475.04939025878906, 248.36050720214845, 260.9890075683594], [2, 105.96339782714844, 476.239990234375, 259.3052075195313, 272.7756079101563], [2, 105.96339782714844, 477.43059020996094, 271.0918078613281, 284.5622082519531], [2, 104.7727978515625, 476.239990234375, 282.878408203125, 296.34880859375], [2, 104.7727978515625, 480.4070901489258, 294.6650085449219, 308.97730895996096], [2, 103.58219787597656, 477.43059020996094, 307.29350891113285, 320.76390930175785], [2, 102.39159790039064, 482.7882901000977, 319.92200927734376, 333.39240966796876], [2, 102.39159790039064, 483.97889007568364, 332.5505096435547, 346.0209100341797], [2, 101.2009979248047, 304.1982937622071, 345.17901000976565, 359.4913104248047], [2, 119.05999755859375, 481.59769012451176, 360.33321044921877, 377.1712109375], [2, 99.41509796142579, 483.97889007568364, 374.6455108642578, 391.4835113525391], [2, 98.22449798583985, 485.1694900512696, 388.1159112548828, 404.9539117431641], [2, 98.22449798583985, 486.3600900268555, 401.5863116455078, 418.4243121337891], [2, 98.22449798583985, 487.55069000244146, 415.0567120361328, 431.8947125244141], [2, 97.0338980102539, 494.0989898681641, 428.5271124267578, 445.3651129150391], [2, 97.0338980102539, 489.9318899536133, 441.9975128173828, 458.83551330566405], [2, 97.0338980102539, 470.28699035644536, 455.4679132080078, 472.30591369628905], [2, 97.0338980102539, 489.9318899536133, 468.9383135986328, 485.77631408691406], [2, 97.0338980102539, 486.3600900268555, 482.4087139892578, 499.24671447753906], [2, 283.9580941772461, 314.9136935424805, 511.87521484375003, 521.9780151367188], [3, 110.13049774169923, 467.3104904174805, 73.24530212402344, 84.19000244140625], [3, 113.10699768066407, 464.33399047851566, 84.19000244140625, 95.13470275878906], [3, 109.53519775390626, 393.4932919311524, 95.13470275878906, 106.07940307617189], [3, 126.79889739990234, 460.76219055175784, 106.07940307617189, 117.0241033935547], [3, 108.34459777832032, 465.5245904541016, 117.0241033935547, 127.96880371093751], [3, 107.74929779052735, 471.4775903320313, 127.96880371093751, 139.75540405273438], [3, 107.74929779052735, 471.4775903320313, 139.75540405273438, 150.7001043701172], [3, 107.74929779052735, 468.5010903930664, 150.7001043701172, 161.6448046875], [3, 107.15399780273438, 460.16689056396484, 161.6448046875, 173.43140502929688], [3, 106.55869781494141, 474.4540902709961, 173.43140502929688, 184.3761053466797], [3, 106.55869781494141, 474.4540902709961, 184.3761053466797, 196.16270568847656], [3, 106.55869781494141, 471.4775903320313, 196.16270568847656, 207.1074060058594], [3, 105.96339782714844, 467.9057904052735, 207.1074060058594, 218.89400634765624], [3, 105.36809783935547, 476.835290222168, 218.89400634765624, 230.68060668945313], [3, 105.36809783935547, 473.8587902832031, 230.68060668945313, 241.62530700683595], [3, 104.7727978515625, 475.04939025878906, 241.62530700683595, 253.4119073486328], [3, 104.17749786376953, 146.4437969970703, 253.4119073486328, 264.35660766601563], [3, 122.0364974975586, 481.00239013671876, 268.56610778808596, 282.878408203125], [3, 102.98689788818359, 416.1146914672852, 284.5622082519531, 298.0326086425781], [3, 102.98689788818359, 476.239990234375, 296.34880859375, 309.819208984375], [3, 102.39159790039064, 473.8587902832031, 308.97730895996096, 322.44770935058597], [3, 102.39159790039064, 482.7882901000977, 320.76390930175785, 335.0762097167969], [3, 102.39159790039064, 483.97889007568364, 333.39240966796876, 346.86281005859377], [3, 101.79629791259767, 475.04939025878906, 345.17901000976565, 359.4913104248047], [3, 101.79629791259767, 457.190390625, 357.80751037597656, 372.11981079101565], [3, 101.2009979248047, 481.00239013671876, 370.43601074218753, 384.74831115722657], [3, 101.2009979248047, 481.59769012451176, 383.06451110839845, 397.37681152343754], [3, 101.2009979248047, 476.239990234375, 395.69301147460936, 410.00531188964845], [3, 101.2009979248047, 486.95539001464846, 408.32151184082034, 422.63381225585937], [3, 101.2009979248047, 487.55069000244146, 420.95001220703125, 435.26231262207034], [3, 101.2009979248047, 488.1459899902344, 433.5785125732422, 447.89081298828125], [3, 105.36809783935547, 179.1852963256836, 452.94221313476567, 466.41261352539067], [3, 120.84589752197266, 484.5741900634766, 461.36121337890626, 478.1992138671875], [3, 101.2009979248047, 431.59249114990234, 475.67351379394535, 489.9858142089844], [3, 101.2009979248047, 489.9318899536133, 487.46011413574223, 502.61431457519535], [3, 282.76749420166016, 312.5324935913086, 516.0847149658204, 527.0294152832031], [4, 117.86939758300782, 450.0467907714844, 78.29670227050782, 89.24140258789063], [4, 117.86939758300782, 464.33399047851566, 89.24140258789063, 99.34420288085938], [4, 117.86939758300782, 461.3574905395508, 99.34420288085938, 110.2889031982422], [4, 117.86939758300782, 426.23479125976564, 110.2889031982422, 121.233603515625], [4, 116.08349761962891, 467.9057904052735, 121.233603515625, 132.17830383300782], [4, 116.08349761962891, 471.4775903320313, 132.17830383300782, 143.12300415039064], [4, 116.08349761962891, 473.8587902832031, 143.12300415039064, 154.06770446777344], [4, 116.08349761962891, 475.04939025878906, 154.06770446777344, 165.01240478515626], [4, 116.08349761962891, 475.04939025878906, 165.01240478515626, 175.95710510253906], [4, 114.29759765625, 476.239990234375, 175.95710510253906, 186.90180541992189], [4, 114.29759765625, 476.239990234375, 186.90180541992189, 197.84650573730468], [4, 113.10699768066407, 478.02589019775394, 197.84650573730468, 208.7912060546875], [4, 116.08349761962891, 479.2164901733399, 208.7912060546875, 219.73590637207033], [4, 111.91639770507813, 466.71519042968754, 219.73590637207033, 231.5225067138672], [4, 111.91639770507813, 476.239990234375, 231.5225067138672, 242.46720703125], [4, 111.91639770507813, 476.239990234375, 242.46720703125, 253.4119073486328], [4, 110.13049774169923, 455.40449066162114, 253.4119073486328, 265.1985076904297], [4, 110.13049774169923, 482.7882901000977, 265.1985076904297, 276.1432080078125], [4, 110.13049774169923, 483.97889007568364, 276.1432080078125, 287.0879083251953], [4, 108.34459777832032, 481.00239013671876, 287.0879083251953, 298.8745086669922], [4, 108.34459777832032, 477.43059020996094, 298.8745086669922, 309.819208984375], [4, 107.15399780273438, 487.55069000244146, 311.5030090332031, 322.44770935058597], [4, 107.15399780273438, 483.97889007568364, 322.44770935058597, 334.23430969238285], [4, 105.96339782714844, 400.63689178466797, 334.23430969238285, 345.17901000976565], [4, 125.01299743652345, 486.3600900268555, 356.96561035156253, 368.7522106933594], [4, 104.17749786376953, 486.3600900268555, 368.7522106933594, 380.53881103515624], [4, 104.17749786376953, 469.69169036865236, 380.53881103515624, 392.3254113769531], [4, 104.17749786376953, 489.33658996582034, 392.3254113769531, 404.11201171875], [4, 104.17749786376953, 494.69428985595704, 404.11201171875, 415.8986120605469], [4, 104.17749786376953, 481.00239013671876, 415.8986120605469, 427.6852124023438], [4, 104.17749786376953, 476.239990234375, 427.6852124023438, 439.47181274414066], [4, 104.17749786376953, 491.1224899291992, 439.47181274414066, 451.2584130859375], [4, 104.17749786376953, 463.1433905029297, 451.2584130859375, 463.0450134277344], [4, 104.17749786376953, 377.4201922607422, 463.0450134277344, 474.83161376953126], [4, 404.8039916992188, 443.49849090576174, 474.83161376953126, 485.77631408691406], [4, 104.17749786376953, 492.31308990478516, 485.77631408691406, 497.56291442871094], [4, 288.72049407958986, 319.0807934570313, 516.0847149658204, 526.1875152587891], [5, 110.13049774169923, 457.190390625, 74.0872021484375, 85.03190246582031], [5, 110.13049774169923, 468.5010903930664, 85.03190246582031, 95.97660278320313], [5, 110.13049774169923, 424.44889129638676, 95.97660278320313, 106.92130310058594], [5, 108.93989776611329, 470.28699035644536, 106.92130310058594, 117.86600341796876], [5, 108.93989776611329, 470.28699035644536, 117.86600341796876, 128.81070373535158], [5, 108.93989776611329, 470.28699035644536, 128.81070373535158, 139.75540405273438], [5, 108.93989776611329, 468.5010903930664, 139.75540405273438, 150.7001043701172], [5, 108.93989776611329, 473.2634902954102, 150.7001043701172, 161.6448046875], [5, 108.93989776611329, 473.8587902832031, 161.6448046875, 172.58950500488282], [5, 107.15399780273438, 466.11989044189454, 172.58950500488282, 184.3761053466797], [5, 105.96339782714844, 472.07289031982424, 184.3761053466797, 195.3208056640625], [5, 105.96339782714844, 476.835290222168, 195.3208056640625, 207.1074060058594], [5, 105.96339782714844, 469.69169036865236, 207.1074060058594, 218.89400634765624], [5, 104.17749786376953, 473.2634902954102, 218.89400634765624, 230.68060668945313], [5, 104.17749786376953, 410.7569915771485, 230.68060668945313, 242.46720703125], [5, 121.44119750976563, 476.835290222168, 242.46720703125, 254.2538073730469], [5, 101.79629791259767, 123.82239746093751, 260.1471075439453, 271.9337078857422], [5, 120.25059753417969, 427.4253912353516, 270.2499078369141, 282.03650817871096], [5, 100.01039794921876, 485.1694900512696, 282.03650817871096, 294.6650085449219], [5, 100.01039794921876, 485.7647900390625, 293.82310852050784, 306.45160888671876], [5, 100.01039794921876, 485.7647900390625, 306.45160888671876, 319.0801092529297], [5, 98.81979797363282, 487.55069000244146, 319.0801092529297, 331.70860961914065], [5, 98.81979797363282, 450.6420907592774, 331.70860961914065, 345.17901000976565], [5, 97.62919799804688, 489.33658996582034, 345.17901000976565, 358.64941040039065], [5, 97.62919799804688, 452.42799072265626, 358.64941040039065, 372.11981079101565], [5, 96.43859802246094, 486.95539001464846, 372.11981079101565, 385.59021118164065], [5, 96.43859802246094, 487.55069000244146, 385.59021118164065, 399.06061157226566], [5, 96.43859802246094, 488.1459899902344, 399.06061157226566, 412.53101196289066], [5, 96.43859802246094, 493.5036898803711, 412.53101196289066, 426.00141235351566], [5, 96.43859802246094, 494.0989898681641, 426.00141235351566, 439.47181274414066], [5, 96.43859802246094, 490.5271899414063, 439.47181274414066, 452.94221313476567], [5, 96.43859802246094, 495.884889831543, 452.94221313476567, 466.41261352539067], [5, 96.43859802246094, 490.5271899414063, 466.41261352539067, 479.88301391601567], [5, 96.43859802246094, 120.25059753417969, 485.77631408691406, 497.56291442871094], [5, 116.08349761962891, 491.7177899169922, 491.6696142578125, 509.3495147705078], [5, 283.36279418945315, 314.31839355468753, 521.9780151367188, 532.9227154541015], [6, 119.05999755859375, 477.43059020996094, 79.13860229492188, 90.08330261230469], [6, 119.05999755859375, 403.01809173583985, 90.08330261230469, 101.0280029296875], [6, 136.91899719238282, 350.03639282226567, 101.0280029296875, 111.97270324707031], [6, 136.91899719238282, 251.21659484863284, 112.81460327148437, 123.7593035888672], [6, 136.91899719238282, 251.21659484863284, 124.60120361328126, 134.70400390625], [6, 267.88499450683594, 332.1773931884766, 134.70400390625, 145.64870422363282], [6, 140.49079711914064, 428.6159912109375, 158.27720458984376, 170.06380493164062], [6, 119.05999755859375, 485.1694900512696, 168.3800048828125, 181.8504052734375], [6, 117.86939758300782, 483.97889007568364, 180.16660522460938, 193.6370056152344], [6, 117.86939758300782, 485.1694900512696, 191.95320556640627, 205.42360595703127], [6, 117.86939758300782, 485.1694900512696, 203.73980590820312, 217.21020629882813], [6, 117.86939758300782, 485.1694900512696, 215.52640625, 228.996806640625], [6, 117.86939758300782, 486.95539001464846, 227.3130065917969, 240.7834069824219], [6, 117.86939758300782, 486.95539001464846, 239.09960693359375, 252.57000732421875], [6, 117.86939758300782, 486.95539001464846, 250.88620727539063, 264.35660766601563], [6, 117.86939758300782, 485.1694900512696, 262.6728076171875, 276.1432080078125], [6, 117.86939758300782, 488.74128997802734, 274.4594079589844, 288.77170837402343], [6, 117.86939758300782, 489.9318899536133, 287.0879083251953, 300.5583087158203], [6, 117.86939758300782, 466.71519042968754, 298.8745086669922, 313.1868090820313], [6, 116.67879760742188, 491.1224899291992, 311.5030090332031, 325.8153094482422], [6, 116.67879760742188, 491.1224899291992, 324.1315093994141, 338.4438098144531], [6, 115.48819763183594, 216.68919555664064, 340.9695098876953, 354.4399102783203], [6, 267.88499450683594, 475.04939025878906, 337.6019097900391, 351.0723101806641], [6, 115.48819763183594, 414.92409149169924, 352.7561102294922, 367.06841064453124], [6, 115.48819763183594, 494.69428985595704, 364.5427105712891, 378.8550109863281], [6, 115.48819763183594, 494.69428985595704, 376.329310913086, 390.641611328125], [6, 115.48819763183594, 196.4489959716797, 394.85111145019533, 407.47961181640625], [6, 270.8614944458008, 339.3209930419922, 404.9539117431641, 416.7405120849609], [6, 119.05999755859375, 492.31308990478516, 427.6852124023438, 444.523212890625], [6, 295.2687939453125, 324.438493347168, 516.9266149902344, 526.1875152587891], [7, 121.44119750976563, 164.89809661865235, 75.77100219726563, 84.19000244140625], [7, 184.54299621582032, 202.4019958496094, 75.77100219726563, 84.19000244140625], [7, 231.57169525146486, 346.46459289550785, 76.61290222167969, 85.87380249023438], [7, 227.99989532470704, 346.46459289550785, 87.5576025390625, 95.97660278320313], [7, 227.99989532470704, 333.9632931518555, 97.66040283203125, 106.92130310058594], [7, 227.99989532470704, 351.22699279785155, 108.60510314941406, 117.0241033935547], [7, 230.9763952636719, 351.22699279785155, 118.70790344238281, 127.96880371093751], [7, 226.8092953491211, 347.6551928710938, 129.65260375976564, 138.07160400390626], [7, 230.38109527587892, 347.6551928710938, 140.59730407714844, 149.01630432128906], [7, 226.8092953491211, 339.3209930419922, 151.54200439453126, 159.96100463867188], [7, 226.21399536132813, 347.6551928710938, 162.48670471191406, 170.9057049560547], [7, 226.21399536132813, 352.4175927734375, 172.58950500488282, 181.8504052734375], [7, 226.21399536132813, 348.84579284667973, 183.53420532226562, 192.79510559082033], [7, 226.21399536132813, 322.65259338378905, 194.47890563964845, 203.73980590820312], [7, 225.61869537353516, 291.6969940185547, 205.42360595703127, 214.68450622558595], [7, 286.934594116211, 326.2243933105469, 228.996806640625, 239.09960693359375], [7, 295.8640939331055, 322.65259338378905, 241.62530700683595, 250.88620727539063], [7, 295.8640939331055, 408.3757916259766, 252.57000732421875, 261.8309075927734], [7, 313.72309356689453, 376.8248922729492, 264.35660766601563, 273.6175079345703], [7, 313.72309356689453, 376.8248922729492, 276.1432080078125, 285.4041082763672], [7, 313.72309356689453, 350.6316928100586, 287.9298083496094, 297.1907086181641], [7, 313.72309356689453, 341.7021929931641, 299.7164086914063, 308.97730895996096], [7, 295.8640939331055, 360.1564926147461, 311.5030090332031, 320.76390930175785], [7, 295.8640939331055, 360.1564926147461, 323.289609375, 332.5505096435547], [7, 295.8640939331055, 332.77269317626957, 335.0762097167969, 345.17901000976565], [7, 295.8640939331055, 332.77269317626957, 346.86281005859377, 356.96561035156253]]
2026-08-10 18:23:53,980 INFO     29 [qwen-vl-text] ═══ DONE ═══ 275 positions, pages=8, time=224.2s
2026-08-10 18:23:53,993 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 18:23:53,993 INFO     29 [Trace] task=8fa8ece8 | doc=07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf | Extractor:Admission | outputs={"chunks": "1 items, types={'AdmissionRecord': 1}", "html": "", "json": "594 items", "markdown": "", "text": "", "name": "07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_LabExam\": 5, \"chunks_Examination\": 4}"}
2026-08-10 18:23:53,993 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 18:23:53,994 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:23:53.993+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 86, "failed": 0, "current": {"8fa8ece894e711f1bd9827cf206dfa2d": {"id": "8fa8ece894e711f1bd9827cf206dfa2d", "doc_id": "8f6c718294e711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 16708238, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385769380, "task_type": "dataflow", "root_trace_id": "0aa1bc1a4312482d8e4b2a1774c52cc7", "root_traceparent": "00-0aa1bc1a4312482d8e4b2a1774c52cc7-ad93c0febce673ce-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:23:53,999 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:23:54,000 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:23:54,000 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 18:23:54,000 INFO     29 [qwen-vl-text] positions(15): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:23:54,000 INFO     29 [qwen-vl-text] page grouping: [9], lines per page: [13]
2026-08-10 18:23:54,258 INFO     29 [qwen-vl-text] page=9, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 18:23:54,260 INFO     29 [qwen-vl-text] LLM extraction start, text_len=374
2026-08-10 18:23:54,260 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:23:54,261 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 514, \"bbox_end\": 528, \"encounter_dates\": [\"2026-03-11\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "报告时间: 2026-03-12\n【检查日期】: 2026/3/11 12:07:23\n【检查所见】: 脑组织左右对称, 双侧额顶叶及侧脑室旁见斑点状稍长T1稍长T2信号, FLAIR像呈高信号\n, DWI未见明显异常信号改变; 双侧基底节区见斑点状长T1长T2信号影; 增强扫描未见强化。脑室系统扩大\n, 中线结构居中。脑沟、脑裂、脑池增宽。部分副鼻窦粘膜增厚, 左侧上颌窦内见类圆形长T2长T2信号影。\n右侧乳突粘膜增厚。鼻中隔偏曲, 双下鼻甲肥大。\n【检查诊断】: 1. 双侧额顶叶及侧脑室旁白质内脱髓鞘改变。\n2. 双侧基底节区软化灶形成。\n3. 老年脑改变, 双侧额颞部少量硬膜下积液。\n4. 部分副鼻窦炎, 左侧上颌窦囊肿; 右侧乳突炎。\n5. 鼻中隔偏曲, 双下鼻甲肥大。\n以上所见较2025-11-09MR变化不著。\n【书写医师】:",
    "role": "user"
  }
]
2026-08-10 18:23:57,853 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:23:57,853 INFO     29 [qwen-vl-text] LLM output (len=621):
{
  "exam_date": "2026-03-11",
  "report_date": "2026-03-12",
  "exam_name": "头颅MRI平扫+增强",
  "exam_category": "imaging",
  "body_part": "脑",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "脑组织左右对称, 双侧额顶叶及侧脑室旁见斑点状稍长T1稍长T2信号, FLAIR像呈高信号, DWI未见明显异常信号改变; 双侧基底节区见斑点状长T1长T2信号影; 增强扫描未见强化。脑室系统扩大, 中线结构居中。脑沟、脑裂、脑池增宽。部分副鼻窦粘膜增厚, 左侧上颌窦内见类圆形长T2长T2信号影。右侧乳突粘膜增厚。鼻中隔偏曲, 双下鼻甲肥大。",
  "conclusion": "1. 双侧额顶叶及侧脑室旁白质内脱髓鞘改变。\n2. 双侧基底节区软化灶形成。\n3. 老年脑改变, 双侧额颞部少量硬膜下积液。\n4. 部分副鼻窦炎, 左侧上颌窦囊肿; 右侧乳突炎。\n5. 鼻中隔偏曲, 双下鼻甲肥大。\n以上所见较2025-11-09MR变化不著。",
  "physician": null,
  "reviewer": null
}
2026-08-10 18:23:57,856 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2085553, prompt_len=1026
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共13行）
["报告时间: 2026-03-12", "【检查日期】: 2026/3/11 12:07:23", "【检查所见】: 脑组织左右对称, 双侧额顶叶及侧脑室旁见斑点状稍长T1稍长T2信号, FLAIR像呈高信号", ", DWI未见明显异常信号改变; 双侧基底节区见斑点状长T1长T2信号影; 增强扫描未见强化。脑室系统扩大", ", 中线结构居中。脑沟、脑裂、脑池增宽。部分副鼻窦粘膜增厚, 左侧上颌窦内见类圆形长T2长T2信号影。", "右侧乳突粘膜增厚。鼻中隔偏曲, 双下鼻甲肥大。", "【检查诊断】: 1. 双侧额顶叶及侧脑室旁白质内脱髓鞘改变。", "2. 双侧基底节区软化灶形成。", "3. 老年脑改变, 双侧额颞部少量硬膜下积液。", "4. 部分副鼻窦炎, 左侧上颌窦囊肿; 右侧乳突炎。", "5. 鼻中隔偏曲, 双下鼻甲肥大。", "以上所见较2025-11-09MR变化不著。", "【书写医师】:"]

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
2026-08-10 18:24:05,858 INFO     29 [qwen-vl-text] coord API raw response (len=955):
[
	{"text": "报告时间: 2026-03-12 09:01", "bbox": [552, 325, 704, 335]},
	{"text": "【检查日期】: 2026/3/11 12:07:23", "bbox": [190, 615, 409, 627]},
	{"text": "【检查所见】: 脑组织左右对称, 双侧额顶叶及侧脑室旁见斑点状稍长T1稍长T2信号, FLAIR像呈高信号", "bbox": [190, 633, 807, 645]},
	{"text": ", DWI未见明显异常信号改变; 双侧基底节区见斑点状长T1长T2信号影; 增强扫描未见强化。脑室系统扩大", "bbox": [171, 644, 807, 655]},
	{"text": ", 中线结构居中。脑沟、脑裂、脑池增宽。部分副鼻窦粘膜增厚, 左侧上颌窦内见类圆形长T2长T2信号影。", "bbox": [171, 654, 807, 665]},
	{"text": "右侧乳突粘膜增厚。鼻中隔偏曲, 双下鼻甲肥大。", "bbox": [171, 664, 470, 675]},
	{"text": "【检查诊断】: 1. 双侧额顶叶及侧脑室旁白质内脱髓鞘改变。", "bbox": [190, 681, 551, 693]},
	{"text": "2. 双侧基底节区软化灶形成。", "bbox": [171, 692, 347, 703]},
	{"text": "3. 老年脑改变, 双侧额颞部少量硬膜下积液。", "bbox": [171, 702, 445, 713]},
	{"text": "4. 部分副鼻窦炎, 左侧上颌窦囊肿; 右侧乳突炎。", "bbox": [171, 712, 470, 723]},
	{"text": "5. 鼻中隔偏曲, 双下鼻甲肥大。", "bbox": [171, 722, 362, 733]},
	{"text": "以上所见较2025-11-09MR变化不著。", "bbox": [171, 731, 389, 742]},
	{"text": "【书写医师】:", "bbox": [190, 748, 276, 760]}
]
2026-08-10 18:24:05,858 INFO     29 [qwen-vl-text] coord API: raw_items=13, valid_items=13, elapsed=8.0s
2026-08-10 18:24:05,859 INFO     29 [qwen-vl-text] coord item[0]: text=报告时间: 2026-03-12 09:01, bbox=[552, 325, 704, 335]
2026-08-10 18:24:05,859 INFO     29 [qwen-vl-text] coord item[1]: text=【检查日期】: 2026/3/11 12:07:23, bbox=[190, 615, 409, 627]
2026-08-10 18:24:05,859 INFO     29 [qwen-vl-text] coord item[2]: text=【检查所见】: 脑组织左右对称, 双侧额顶叶及侧脑室旁见斑点状稍长T1稍长T2信号, FLAIR像呈高信号, bbox=[190, 633, 807, 645]
2026-08-10 18:24:05,859 INFO     29 [qwen-vl-text] coord item[3]: text=, DWI未见明显异常信号改变; 双侧基底节区见斑点状长T1长T2信号影; 增强扫描未见强化。脑室系统扩大, bbox=[171, 644, 807, 655]
2026-08-10 18:24:05,859 INFO     29 [qwen-vl-text] coord item[4]: text=, 中线结构居中。脑沟、脑裂、脑池增宽。部分副鼻窦粘膜增厚, 左侧上颌窦内见类圆形长T2长T2信号影。, bbox=[171, 654, 807, 665]
2026-08-10 18:24:05,859 INFO     29 [qwen-vl-text] coord item[5]: text=右侧乳突粘膜增厚。鼻中隔偏曲, 双下鼻甲肥大。, bbox=[171, 664, 470, 675]
2026-08-10 18:24:05,859 INFO     29 [qwen-vl-text] coord item[6]: text=【检查诊断】: 1. 双侧额顶叶及侧脑室旁白质内脱髓鞘改变。, bbox=[190, 681, 551, 693]
2026-08-10 18:24:05,859 INFO     29 [qwen-vl-text] coord item[7]: text=2. 双侧基底节区软化灶形成。, bbox=[171, 692, 347, 703]
2026-08-10 18:24:05,859 INFO     29 [qwen-vl-text] coord item[8]: text=3. 老年脑改变, 双侧额颞部少量硬膜下积液。, bbox=[171, 702, 445, 713]
2026-08-10 18:24:05,859 INFO     29 [qwen-vl-text] coord item[9]: text=4. 部分副鼻窦炎, 左侧上颌窦囊肿; 右侧乳突炎。, bbox=[171, 712, 470, 723]
2026-08-10 18:24:05,859 INFO     29 [qwen-vl-text] coord item[10]: text=5. 鼻中隔偏曲, 双下鼻甲肥大。, bbox=[171, 722, 362, 733]
2026-08-10 18:24:05,859 INFO     29 [qwen-vl-text] coord item[11]: text=以上所见较2025-11-09MR变化不著。, bbox=[171, 731, 389, 742]
2026-08-10 18:24:05,859 INFO     29 [qwen-vl-text] coord item[12]: text=【书写医师】:, bbox=[190, 748, 276, 760]
2026-08-10 18:24:05,860 INFO     29 [qwen-vl-text] page=9 — 13/13 coords, api_time=8.0s
2026-08-10 18:24:05,860 INFO     29 [qwen-vl-text] new_positions (13):
[[9, 328.60559326171875, 419.09119140625, 273.6175079345703, 282.03650817871096], [9, 113.10699768066407, 243.47769500732423, 517.7685150146484, 527.8713153076172], [9, 113.10699768066407, 480.4070901489258, 532.9227154541015, 543.0255157470704], [9, 101.79629791259767, 480.4070901489258, 542.1836157226562, 551.444515991211], [9, 101.79629791259767, 480.4070901489258, 550.6026159667969, 559.8635162353515], [9, 101.79629791259767, 279.79099426269534, 559.0216162109375, 568.2825164794922], [9, 113.10699768066407, 328.0102932739258, 573.3339166259766, 583.4367169189453], [9, 101.79629791259767, 206.56909576416015, 582.5948168945313, 591.855717163086], [9, 101.79629791259767, 264.9084945678711, 591.0138171386719, 600.2747174072266], [9, 101.79629791259767, 279.79099426269534, 599.4328173828126, 608.6937176513673], [9, 101.79629791259767, 215.4985955810547, 607.8518176269531, 617.1127178955078], [9, 101.79629791259767, 231.57169525146486, 615.4289178466797, 624.6898181152344], [9, 113.10699768066407, 164.30279663085938, 629.7412182617188, 639.8440185546875]]
2026-08-10 18:24:05,861 INFO     29 [qwen-vl-text] ═══ DONE ═══ 13 positions, pages=1, time=11.9s
2026-08-10 18:24:05,861 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:24:05,862 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:24:05,862 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 18:24:05,862 INFO     29 [qwen-vl-text] positions(18): [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:24:05,862 INFO     29 [qwen-vl-text] page grouping: [10], lines per page: [18]
2026-08-10 18:24:06,126 INFO     29 [qwen-vl-text] page=10, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 18:24:06,127 INFO     29 [qwen-vl-text] LLM extraction start, text_len=603
2026-08-10 18:24:06,128 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:24:06,128 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 529, \"bbox_end\": 546, \"encounter_dates\": [\"2026-01-08\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "【检查日期】：2026/1/8 13:58:55\n【检查所见】：右侧胸廓塌陷，右侧胸腔内见少量液体密度影，右肺肺组织压缩、密度增高，右肺下叶可\n见一团块状软组织密度影，内见空洞影，增强可见轻度不均匀强化，周围伴条片状密度增高影，与远侧不张\n肺组织分界不清，范围无法测量。右肺小叶间隔增厚。右侧胸膜不均匀增厚伴局部结节状、肿块状，增强可\n见明显强化，邻近右前胸壁及右侧膈肌不规整。双肺内见斑片及索条影。左肺见小结节影，大者位于左肺下\n叶（薄层img180），直径约为0.4cm。纵隔窗未见显示，增强扫描难以评估。气管及主支气管通畅。纵隔右\n偏，纵隔及双肺门内见稍大淋巴结影，大者短径约1.1cm，增强强化欠均匀。心脏大小、形态正常，主动脉\n壁及冠状动脉走行区可见高密度影。\n甲状腺密度不均，内见类圆形低密度影。右侧部分肋骨内缘骨皮质增厚，右侧第7、8、9、12肋局部骨\n质见片状高密度影。\n【检查诊断】：对比2025-11-08CT：\n1.右肺下叶肺癌，范围整体较前增大；右肺小叶间隔增厚，较前进展，考虑癌性淋巴管炎可能；纵隔及双肺\n门淋巴结大致同前；考虑右侧胸膜转移，较前进展，累及邻近右前胸壁及右侧膈肌可能；请结合临床并复查\n。\n2.右侧胸腔积液，较前变化不著。\n3.左肺小结节，较前相仿，建议短期复查。\n4.右侧第7-9、12肋骨高密度影，局部略进展，转移可能，建议ECT进一步检查。\n余所见大致同前。",
    "role": "user"
  }
]
2026-08-10 18:24:10,922 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:24:10,922 INFO     29 [qwen-vl-text] LLM output (len=863):
{
  "exam_date": "2026-01-08",
  "report_date": null,
  "exam_name": "胸部CT增强",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "右侧胸廓塌陷，右侧胸腔内见少量液体密度影，右肺肺组织压缩、密度增高，右肺下叶可见一团块状软组织密度影，内见空洞影，增强可见轻度不均匀强化，周围伴条片状密度增高影，与远侧不张肺组织分界不清，范围无法测量。右肺小叶间隔增厚。右侧胸膜不均匀增厚伴局部结节状、肿块状，增强可见明显强化，邻近右前胸壁及右侧膈肌不规整。双肺内见斑片及索条影。左肺见小结节影，大者位于左肺下叶（薄层img180），直径约为0.4cm。纵隔窗未见显示，增强扫描难以评估。气管及主支气管通畅。纵隔右偏，纵隔及双肺门内见稍大淋巴结影，大者短径约1.1cm，增强强化欠均匀。心脏大小、形态正常，主动脉壁及冠状动脉走行区可见高密度影。\n甲状腺密度不均，内见类圆形低密度影。右侧部分肋骨内缘骨皮质增厚，右侧第7、8、9、12肋局部骨质见片状高密度影。",
  "conclusion": "对比2025-11-08CT：\n1.右肺下叶肺癌，范围整体较前增大；右肺小叶间隔增厚，较前进展，考虑癌性淋巴管炎可能；纵隔及双肺门淋巴结大致同前；考虑右侧胸膜转移，较前进展，累及邻近右前胸壁及右侧膈肌可能；请结合临床并复查。\n2.右侧胸腔积液，较前变化不著。\n3.左肺小结节，较前相仿，建议短期复查。\n4.右侧第7-9、12肋骨高密度影，局部略进展，转移可能，建议ECT进一步检查。\n余所见大致同前。",
  "physician": null,
  "reviewer": null
}
2026-08-10 18:24:10,931 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4194654, prompt_len=1270
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共18行）
["【检查日期】：2026/1/8 13:58:55", "【检查所见】：右侧胸廓塌陷，右侧胸腔内见少量液体密度影，右肺肺组织压缩、密度增高，右肺下叶可", "见一团块状软组织密度影，内见空洞影，增强可见轻度不均匀强化，周围伴条片状密度增高影，与远侧不张", "肺组织分界不清，范围无法测量。右肺小叶间隔增厚。右侧胸膜不均匀增厚伴局部结节状、肿块状，增强可", "见明显强化，邻近右前胸壁及右侧膈肌不规整。双肺内见斑片及索条影。左肺见小结节影，大者位于左肺下", "叶（薄层img180），直径约为0.4cm。纵隔窗未见显示，增强扫描难以评估。气管及主支气管通畅。纵隔右", "偏，纵隔及双肺门内见稍大淋巴结影，大者短径约1.1cm，增强强化欠均匀。心脏大小、形态正常，主动脉", "壁及冠状动脉走行区可见高密度影。", "甲状腺密度不均，内见类圆形低密度影。右侧部分肋骨内缘骨皮质增厚，右侧第7、8、9、12肋局部骨", "质见片状高密度影。", "【检查诊断】：对比2025-11-08CT：", "1.右肺下叶肺癌，范围整体较前增大；右肺小叶间隔增厚，较前进展，考虑癌性淋巴管炎可能；纵隔及双肺", "门淋巴结大致同前；考虑右侧胸膜转移，较前进展，累及邻近右前胸壁及右侧膈肌可能；请结合临床并复查", "。", "2.右侧胸腔积液，较前变化不著。", "3.左肺小结节，较前相仿，建议短期复查。", "4.右侧第7-9、12肋骨高密度影，局部略进展，转移可能，建议ECT进一步检查。", "余所见大致同前。"]

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
2026-08-10 18:24:19,288 INFO     29 [qwen-vl-text] coord API raw response (len=1397):
[
	{"text": "【检查日期】：2026/1/8 13:58:55", "bbox": [185, 98, 402, 110]},
	{"text": "【检查所见】：右侧胸廓塌陷，右侧胸腔内见少量液体密度影，右肺肺组织压缩、密度增高，右肺下叶可", "bbox": [185, 115, 818, 128]},
	{"text": "见一团块状软组织密度影，内见空洞影，增强可见轻度不均匀强化，周围伴条片状密度增高影，与远侧不张", "bbox": [167, 126, 818, 138]},
	{"text": "肺组织分界不清，范围无法测量。右肺小叶间隔增厚。右侧胸膜不均匀增厚伴局部结节状、肿块状，增强可", "bbox": [167, 136, 818, 148]},
	{"text": "见明显强化，邻近右前胸壁及右侧膈肌不规整。双肺内见斑片及索条影。左肺见小结节影，大者位于左肺下", "bbox": [167, 146, 818, 158]},
	{"text": "叶（薄层img180），直径约为0.4cm。纵隔窗未见显示，增强扫描难以评估。气管及主支气管通畅。纵隔右", "bbox": [167, 156, 818, 168]},
	{"text": "偏，纵隔及双肺门内见稍大淋巴结影，大者短径约1.1cm，增强强化欠均匀。心脏大小、形态正常，主动脉", "bbox": [167, 166, 818, 178]},
	{"text": "壁及冠状动脉走行区可见高密度影。", "bbox": [167, 176, 390, 188]},
	{"text": "甲状腺密度不均，内见类圆形低密度影。右侧部分肋骨内缘骨皮质增厚，右侧第7、8、9、12肋局部骨", "bbox": [167, 184, 818, 197]},
	{"text": "质见片状高密度影。", "bbox": [167, 195, 290, 207]},
	{"text": "【检查诊断】：对比2025-11-08CT：", "bbox": [185, 214, 402, 226]},
	{"text": "1.右肺下叶肺癌，范围整体较前增大；右肺小叶间隔增厚，较前进展，考虑癌性淋巴管炎可能；纵隔及双肺", "bbox": [167, 221, 818, 234]},
	{"text": "门淋巴结大致同前；考虑右侧胸膜转移，较前进展，累及邻近右前胸壁及右侧膈肌可能；请结合临床并复查", "bbox": [167, 231, 818, 244]},
	{"text": "。", "bbox": [167, 241, 177, 254]},
	{"text": "2.右侧胸腔积液，较前变化不著。", "bbox": [167, 254, 375, 266]},
	{"text": "3.左肺小结节，较前相仿，建议短期复查。", "bbox": [167, 264, 431, 276]},
	{"text": "4.右侧第7-9、12肋骨高密度影，局部略进展，转移可能，建议ECT进一步检查。", "bbox": [167, 271, 652, 283]},
	{"text": "余所见大致同前。", "bbox": [167, 283, 277, 295]}
]
2026-08-10 18:24:19,288 INFO     29 [qwen-vl-text] coord API: raw_items=18, valid_items=18, elapsed=8.4s
2026-08-10 18:24:19,288 INFO     29 [qwen-vl-text] coord item[0]: text=【检查日期】：2026/1/8 13:58:55, bbox=[185, 98, 402, 110]
2026-08-10 18:24:19,288 INFO     29 [qwen-vl-text] coord item[1]: text=【检查所见】：右侧胸廓塌陷，右侧胸腔内见少量液体密度影，右肺肺组织压缩、密度增高，右肺下叶可, bbox=[185, 115, 818, 128]
2026-08-10 18:24:19,288 INFO     29 [qwen-vl-text] coord item[2]: text=见一团块状软组织密度影，内见空洞影，增强可见轻度不均匀强化，周围伴条片状密度增高影，与远侧不张, bbox=[167, 126, 818, 138]
2026-08-10 18:24:19,288 INFO     29 [qwen-vl-text] coord item[3]: text=肺组织分界不清，范围无法测量。右肺小叶间隔增厚。右侧胸膜不均匀增厚伴局部结节状、肿块状，增强可, bbox=[167, 136, 818, 148]
2026-08-10 18:24:19,288 INFO     29 [qwen-vl-text] coord item[4]: text=见明显强化，邻近右前胸壁及右侧膈肌不规整。双肺内见斑片及索条影。左肺见小结节影，大者位于左肺下, bbox=[167, 146, 818, 158]
2026-08-10 18:24:19,288 INFO     29 [qwen-vl-text] coord item[5]: text=叶（薄层img180），直径约为0.4cm。纵隔窗未见显示，增强扫描难以评估。气管及主支气管通畅。纵隔右, bbox=[167, 156, 818, 168]
2026-08-10 18:24:19,288 INFO     29 [qwen-vl-text] coord item[6]: text=偏，纵隔及双肺门内见稍大淋巴结影，大者短径约1.1cm，增强强化欠均匀。心脏大小、形态正常，主动脉, bbox=[167, 166, 818, 178]
2026-08-10 18:24:19,288 INFO     29 [qwen-vl-text] coord item[7]: text=壁及冠状动脉走行区可见高密度影。, bbox=[167, 176, 390, 188]
2026-08-10 18:24:19,289 INFO     29 [qwen-vl-text] coord item[8]: text=甲状腺密度不均，内见类圆形低密度影。右侧部分肋骨内缘骨皮质增厚，右侧第7、8、9、12肋局部骨, bbox=[167, 184, 818, 197]
2026-08-10 18:24:19,289 INFO     29 [qwen-vl-text] coord item[9]: text=质见片状高密度影。, bbox=[167, 195, 290, 207]
2026-08-10 18:24:19,289 INFO     29 [qwen-vl-text] coord item[10]: text=【检查诊断】：对比2025-11-08CT：, bbox=[185, 214, 402, 226]
2026-08-10 18:24:19,289 INFO     29 [qwen-vl-text] coord item[11]: text=1.右肺下叶肺癌，范围整体较前增大；右肺小叶间隔增厚，较前进展，考虑癌性淋巴管炎可能；纵隔及双肺, bbox=[167, 221, 818, 234]
2026-08-10 18:24:19,289 INFO     29 [qwen-vl-text] coord item[12]: text=门淋巴结大致同前；考虑右侧胸膜转移，较前进展，累及邻近右前胸壁及右侧膈肌可能；请结合临床并复查, bbox=[167, 231, 818, 244]
2026-08-10 18:24:19,289 INFO     29 [qwen-vl-text] coord item[13]: text=。, bbox=[167, 241, 177, 254]
2026-08-10 18:24:19,289 INFO     29 [qwen-vl-text] coord item[14]: text=2.右侧胸腔积液，较前变化不著。, bbox=[167, 254, 375, 266]
2026-08-10 18:24:19,289 INFO     29 [qwen-vl-text] coord item[15]: text=3.左肺小结节，较前相仿，建议短期复查。, bbox=[167, 264, 431, 276]
2026-08-10 18:24:19,289 INFO     29 [qwen-vl-text] coord item[16]: text=4.右侧第7-9、12肋骨高密度影，局部略进展，转移可能，建议ECT进一步检查。, bbox=[167, 271, 652, 283]
2026-08-10 18:24:19,289 INFO     29 [qwen-vl-text] coord item[17]: text=余所见大致同前。, bbox=[167, 283, 277, 295]
2026-08-10 18:24:19,290 INFO     29 [qwen-vl-text] page=10 — 18/18 coords, api_time=8.4s
2026-08-10 18:24:19,290 INFO     29 [qwen-vl-text] new_positions (18):
[[10, 110.13049774169923, 239.31059509277344, 82.50620239257813, 92.60900268554688], [10, 110.13049774169923, 486.95539001464846, 96.8185028076172, 107.763203125], [10, 99.41509796142579, 486.95539001464846, 106.07940307617189, 116.18220336914062], [10, 99.41509796142579, 486.95539001464846, 114.4984033203125, 124.60120361328126], [10, 99.41509796142579, 486.95539001464846, 122.91740356445312, 133.02020385742188], [10, 99.41509796142579, 486.95539001464846, 131.33640380859376, 141.4392041015625], [10, 99.41509796142579, 486.95539001464846, 139.75540405273438, 149.85820434570314], [10, 99.41509796142579, 232.16699523925783, 148.174404296875, 158.27720458984376], [10, 99.41509796142579, 486.95539001464846, 154.9096044921875, 165.85430480957032], [10, 99.41509796142579, 172.63699645996095, 164.1705047607422, 174.27330505371094], [10, 110.13049774169923, 239.31059509277344, 180.16660522460938, 190.26940551757812], [10, 99.41509796142579, 486.95539001464846, 186.05990539550783, 197.00460571289062], [10, 99.41509796142579, 486.95539001464846, 194.47890563964845, 205.42360595703127], [10, 99.41509796142579, 105.36809783935547, 202.89790588378906, 213.8426062011719], [10, 99.41509796142579, 223.23749542236328, 213.8426062011719, 223.94540649414063], [10, 99.41509796142579, 256.57429473876954, 222.2616064453125, 232.36440673828125], [10, 99.41509796142579, 388.1355920410156, 228.15490661621095, 238.2577069091797], [10, 99.41509796142579, 164.89809661865235, 238.2577069091797, 248.36050720214845]]
2026-08-10 18:24:19,290 INFO     29 [qwen-vl-text] ═══ DONE ═══ 18 positions, pages=1, time=13.4s
2026-08-10 18:24:19,290 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:24:19,291 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:24:19,291 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 18:24:19,291 INFO     29 [qwen-vl-text] positions(35): [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:24:19,291 INFO     29 [qwen-vl-text] page grouping: [10], lines per page: [35]
2026-08-10 18:24:19,551 INFO     29 [qwen-vl-text] page=10, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 18:24:19,552 INFO     29 [qwen-vl-text] LLM extraction start, text_len=309
2026-08-10 18:24:19,552 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:24:19,552 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 547, \"bbox_end\": 581, \"encounter_dates\": [\"2026-03-11\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "【检查描述】：心搏次数：97(60~100) bpm，PR间隔：160 ms，QRS间隔：74 ms，QT间隔：334 ms，QTc\n间隔：424 ms，P轴：51°，QRS轴：7°，T轴：34°\n【检查诊断】：窦性心律\n大致正常心电图\n【检查时间】：2026/3/11 13:54:45\n检查时间\n心率\n2026-03-11 13:54:39\nPR\n97 bpm\nQRS\n160 ms\nQT/QTc\n74 ms\nP/QRS/T\n间期\n334 / 424 ms\nRV5+SV1\n电轴\n51 / 7 / 34 °\n振幅\n/\nmV\n0.000 mV\nAVR\nV1\nV4\nAVL\nV2\nV5\nIII\nV3\nV6\nAVF\nII",
    "role": "user"
  }
]
2026-08-10 18:24:21,732 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:24:21,732 INFO     29 [qwen-vl-text] LLM output (len=415):
{
  "exam_date": "2026-03-11",
  "report_date": null,
  "exam_name": "心电图",
  "exam_category": "other",
  "body_part": "心脏",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "【检查描述】：心搏次数：97(60~100) bpm，PR间隔：160 ms，QRS间隔：74 ms，QT间隔：334 ms，QTc间隔：424 ms，P轴：51°，QRS轴：7°，T轴：34°",
  "conclusion": "【检查诊断】：窦性心律\n大致正常心电图",
  "physician": null,
  "reviewer": null
}
2026-08-10 18:24:21,747 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4194654, prompt_len=1027
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["【检查描述】：心搏次数：97(60~100) bpm，PR间隔：160 ms，QRS间隔：74 ms，QT间隔：334 ms，QTc", "间隔：424 ms，P轴：51°，QRS轴：7°，T轴：34°", "【检查诊断】：窦性心律", "大致正常心电图", "【检查时间】：2026/3/11 13:54:45", "检查时间", "心率", "2026-03-11 13:54:39", "PR", "97 bpm", "QRS", "160 ms", "QT/QTc", "74 ms", "P/QRS/T", "间期", "334 / 424 ms", "RV5+SV1", "电轴", "51 / 7 / 34 °", "振幅", "/", "mV", "0.000 mV", "AVR", "V1", "V4", "AVL", "V2", "V5", "III", "V3", "V6", "AVF", "II"]

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
2026-08-10 18:24:30,960 INFO     29 [qwen-vl-text] coord API raw response (len=1852):
[
	{"text": "【检查描述】：心搏次数：97(60~100) bpm，PR间隔：160 ms，QRS间隔：74 ms，QT间隔：334 ms，QTc", "bbox": [155, 323, 794, 336]},
	{"text": "间隔：424 ms，P轴：51°，QRS轴：7°，T轴：34°", "bbox": [155, 335, 484, 346]},
	{"text": "【检查诊断】：窦性心律", "bbox": [155, 353, 321, 365]},
	{"text": "大致正常心电图", "bbox": [155, 363, 252, 374]},
	{"text": "【检查时间】：2026/3/11 13:54:45", "bbox": [173, 381, 392, 393]},
	{"text": "检查时间", "bbox": [152, 588, 187, 595]},
	{"text": "心率", "bbox": [152, 595, 172, 602]},
	{"text": "2026-03-11 13:54:39", "bbox": [244, 588, 324, 595]},
	{"text": "PR", "bbox": [152, 602, 165, 608]},
	{"text": "97 bpm", "bbox": [298, 595, 326, 602]},
	{"text": "QRS", "bbox": [152, 608, 167, 614]},
	{"text": "160 ms", "bbox": [298, 602, 324, 608]},
	{"text": "QT/QTc", "bbox": [152, 614, 180, 620]},
	{"text": "74 ms", "bbox": [298, 608, 324, 614]},
	{"text": "P/QRS/T", "bbox": [152, 620, 182, 627]},
	{"text": "间期", "bbox": [197, 602, 215, 608]},
	{"text": "334 / 424 ms", "bbox": [270, 614, 324, 620]},
	{"text": "RV5+SV1", "bbox": [152, 633, 182, 639]},
	{"text": "电轴", "bbox": [197, 614, 215, 620]},
	{"text": "51 / 7 / 34 °", "bbox": [262, 620, 324, 627]},
	{"text": "振幅", "bbox": [197, 620, 215, 627]},
	{"text": "/", "bbox": [298, 627, 305, 633]},
	{"text": "mV", "bbox": [312, 627, 324, 633]},
	{"text": "0.000 mV", "bbox": [288, 633, 324, 639]},
	{"text": "AVR", "bbox": [367, 652, 383, 658]},
	{"text": "V1", "bbox": [525, 652, 534, 658]},
	{"text": "V4", "bbox": [679, 652, 688, 658]},
	{"text": "AVL", "bbox": [367, 694, 383, 700]},
	{"text": "V2", "bbox": [525, 694, 534, 700]},
	{"text": "V5", "bbox": [679, 694, 688, 700]},
	{"text": "III", "bbox": [204, 737, 213, 743]},
	{"text": "V3", "bbox": [525, 735, 534, 741]},
	{"text": "V6", "bbox": [679, 735, 688, 741]},
	{"text": "AVF", "bbox": [367, 737, 383, 743]},
	{"text": "II", "bbox": [204, 779, 213, 785]}
]
2026-08-10 18:24:30,960 INFO     29 [qwen-vl-text] coord API: raw_items=35, valid_items=35, elapsed=9.2s
2026-08-10 18:24:30,961 INFO     29 [qwen-vl-text] coord item[0]: text=【检查描述】：心搏次数：97(60~100) bpm，PR间隔：160 ms，QRS间隔：74 ms，QT间隔：334 ms，QTc, bbox=[155, 323, 794, 336]
2026-08-10 18:24:30,961 INFO     29 [qwen-vl-text] coord item[1]: text=间隔：424 ms，P轴：51°，QRS轴：7°，T轴：34°, bbox=[155, 335, 484, 346]
2026-08-10 18:24:30,961 INFO     29 [qwen-vl-text] coord item[2]: text=【检查诊断】：窦性心律, bbox=[155, 353, 321, 365]
2026-08-10 18:24:30,961 INFO     29 [qwen-vl-text] coord item[3]: text=大致正常心电图, bbox=[155, 363, 252, 374]
2026-08-10 18:24:30,961 INFO     29 [qwen-vl-text] coord item[4]: text=【检查时间】：2026/3/11 13:54:45, bbox=[173, 381, 392, 393]
2026-08-10 18:24:30,961 INFO     29 [qwen-vl-text] coord item[5]: text=检查时间, bbox=[152, 588, 187, 595]
2026-08-10 18:24:30,961 INFO     29 [qwen-vl-text] coord item[6]: text=心率, bbox=[152, 595, 172, 602]
2026-08-10 18:24:30,961 INFO     29 [qwen-vl-text] coord item[7]: text=2026-03-11 13:54:39, bbox=[244, 588, 324, 595]
2026-08-10 18:24:30,961 INFO     29 [qwen-vl-text] coord item[8]: text=PR, bbox=[152, 602, 165, 608]
2026-08-10 18:24:30,961 INFO     29 [qwen-vl-text] coord item[9]: text=97 bpm, bbox=[298, 595, 326, 602]
2026-08-10 18:24:30,961 INFO     29 [qwen-vl-text] coord item[10]: text=QRS, bbox=[152, 608, 167, 614]
2026-08-10 18:24:30,961 INFO     29 [qwen-vl-text] coord item[11]: text=160 ms, bbox=[298, 602, 324, 608]
2026-08-10 18:24:30,962 INFO     29 [qwen-vl-text] coord item[12]: text=QT/QTc, bbox=[152, 614, 180, 620]
2026-08-10 18:24:30,962 INFO     29 [qwen-vl-text] coord item[13]: text=74 ms, bbox=[298, 608, 324, 614]
2026-08-10 18:24:30,962 INFO     29 [qwen-vl-text] coord item[14]: text=P/QRS/T, bbox=[152, 620, 182, 627]
2026-08-10 18:24:30,962 INFO     29 [qwen-vl-text] coord item[15]: text=间期, bbox=[197, 602, 215, 608]
2026-08-10 18:24:30,962 INFO     29 [qwen-vl-text] coord item[16]: text=334 / 424 ms, bbox=[270, 614, 324, 620]
2026-08-10 18:24:30,962 INFO     29 [qwen-vl-text] coord item[17]: text=RV5+SV1, bbox=[152, 633, 182, 639]
2026-08-10 18:24:30,962 INFO     29 [qwen-vl-text] coord item[18]: text=电轴, bbox=[197, 614, 215, 620]
2026-08-10 18:24:30,962 INFO     29 [qwen-vl-text] coord item[19]: text=51 / 7 / 34 °, bbox=[262, 620, 324, 627]
2026-08-10 18:24:30,962 INFO     29 [qwen-vl-text] coord item[20]: text=振幅, bbox=[197, 620, 215, 627]
2026-08-10 18:24:30,962 INFO     29 [qwen-vl-text] coord item[21]: text=/, bbox=[298, 627, 305, 633]
2026-08-10 18:24:30,962 INFO     29 [qwen-vl-text] coord item[22]: text=mV, bbox=[312, 627, 324, 633]
2026-08-10 18:24:30,962 INFO     29 [qwen-vl-text] coord item[23]: text=0.000 mV, bbox=[288, 633, 324, 639]
2026-08-10 18:24:30,962 INFO     29 [qwen-vl-text] coord item[24]: text=AVR, bbox=[367, 652, 383, 658]
2026-08-10 18:24:30,962 INFO     29 [qwen-vl-text] coord item[25]: text=V1, bbox=[525, 652, 534, 658]
2026-08-10 18:24:30,962 INFO     29 [qwen-vl-text] coord item[26]: text=V4, bbox=[679, 652, 688, 658]
2026-08-10 18:24:30,962 INFO     29 [qwen-vl-text] coord item[27]: text=AVL, bbox=[367, 694, 383, 700]
2026-08-10 18:24:30,962 INFO     29 [qwen-vl-text] coord item[28]: text=V2, bbox=[525, 694, 534, 700]
2026-08-10 18:24:30,962 INFO     29 [qwen-vl-text] coord item[29]: text=V5, bbox=[679, 694, 688, 700]
2026-08-10 18:24:30,962 INFO     29 [qwen-vl-text] coord item[30]: text=III, bbox=[204, 737, 213, 743]
2026-08-10 18:24:30,962 INFO     29 [qwen-vl-text] coord item[31]: text=V3, bbox=[525, 735, 534, 741]
2026-08-10 18:24:30,963 INFO     29 [qwen-vl-text] coord item[32]: text=V6, bbox=[679, 735, 688, 741]
2026-08-10 18:24:30,963 INFO     29 [qwen-vl-text] coord item[33]: text=AVF, bbox=[367, 737, 383, 743]
2026-08-10 18:24:30,963 INFO     29 [qwen-vl-text] coord item[34]: text=II, bbox=[204, 779, 213, 785]
2026-08-10 18:24:30,965 INFO     29 [qwen-vl-text] page=10 — 35/35 coords, api_time=9.2s
2026-08-10 18:24:30,965 INFO     29 [qwen-vl-text] new_positions (35):
[[10, 92.27149810791016, 472.6681903076172, 271.9337078857422, 282.878408203125], [10, 92.27149810791016, 288.1251940917969, 282.03650817871096, 291.29740844726564], [10, 92.27149810791016, 191.09129608154296, 297.1907086181641, 307.29350891113285], [10, 92.27149810791016, 150.01559692382813, 305.6097088623047, 314.8706091308594], [10, 102.98689788818359, 233.35759521484377, 320.76390930175785, 330.86670959472656], [10, 90.48559814453125, 111.32109771728516, 495.0372143554688, 500.93051452636723], [10, 90.48559814453125, 102.39159790039064, 500.93051452636723, 506.8238146972656], [10, 145.25319702148437, 192.87719604492187, 495.0372143554688, 500.93051452636723], [10, 90.48559814453125, 98.22449798583985, 506.8238146972656, 511.87521484375003], [10, 177.39939636230469, 194.0677960205078, 500.93051452636723, 506.8238146972656], [10, 90.48559814453125, 99.41509796142579, 511.87521484375003, 516.9266149902344], [10, 177.39939636230469, 192.87719604492187, 506.8238146972656, 511.87521484375003], [10, 90.48559814453125, 107.15399780273438, 516.9266149902344, 521.9780151367188], [10, 177.39939636230469, 192.87719604492187, 511.87521484375003, 516.9266149902344], [10, 90.48559814453125, 108.34459777832032, 521.9780151367188, 527.8713153076172], [10, 117.27409759521485, 127.98949737548828, 506.8238146972656, 511.87521484375003], [10, 160.73099670410156, 192.87719604492187, 516.9266149902344, 521.9780151367188], [10, 90.48559814453125, 108.34459777832032, 532.9227154541015, 537.974115600586], [10, 117.27409759521485, 127.98949737548828, 516.9266149902344, 521.9780151367188], [10, 155.96859680175783, 192.87719604492187, 521.9780151367188, 527.8713153076172], [10, 117.27409759521485, 127.98949737548828, 521.9780151367188, 527.8713153076172], [10, 177.39939636230469, 181.56649627685547, 527.8713153076172, 532.9227154541015], [10, 185.73359619140626, 192.87719604492187, 527.8713153076172, 532.9227154541015], [10, 171.44639648437501, 192.87719604492187, 532.9227154541015, 537.974115600586], [10, 218.47509552001955, 227.99989532470704, 548.9188159179688, 553.9702160644531], [10, 312.5324935913086, 317.89019348144535, 548.9188159179688, 553.9702160644531], [10, 404.2086917114258, 409.56639160156254, 548.9188159179688, 553.9702160644531], [10, 218.47509552001955, 227.99989532470704, 584.2786169433595, 589.3300170898438], [10, 312.5324935913086, 317.89019348144535, 584.2786169433595, 589.3300170898438], [10, 404.2086917114258, 409.56639160156254, 584.2786169433595, 589.3300170898438], [10, 121.44119750976563, 126.79889739990234, 620.4803179931641, 625.5317181396484], [10, 312.5324935913086, 317.89019348144535, 618.796517944336, 623.8479180908204], [10, 404.2086917114258, 409.56639160156254, 618.796517944336, 623.8479180908204], [10, 218.47509552001955, 227.99989532470704, 620.4803179931641, 625.5317181396484], [10, 121.44119750976563, 126.79889739990234, 655.8401190185547, 660.8915191650391]]
2026-08-10 18:24:30,965 INFO     29 [qwen-vl-text] ═══ DONE ═══ 35 positions, pages=1, time=11.7s
2026-08-10 18:24:30,966 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:24:30,974 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:24:30,974 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 18:24:30,975 INFO     29 [qwen-vl-text] positions(10): [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:24:30,975 INFO     29 [qwen-vl-text] page grouping: [11], lines per page: [10]
2026-08-10 18:24:31,087 INFO     29 [qwen-vl-text] page=11, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 18:24:31,089 INFO     29 [qwen-vl-text] LLM extraction start, text_len=261
2026-08-10 18:24:31,089 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:24:31,089 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 582, \"bbox_end\": 591, \"encounter_dates\": [\"2025-04-09\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "【手术信息】：胸腔积液\n【取材部位】：1:胸膜×1\n2:细胞蜡块1×1\n【取材描述】：胸膜×多\n【大体描述】：胸膜：灰白小组织一堆，大小1*0.8*0.5cm。\n【病理所见】：胸膜：灰白小组织一堆，大小1*0.8*0.5cm。\n【病理诊断】：（胸膜活检）送检增生的纤维组织内见腺癌浸润，请结合临床诊治。\n免疫组化：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（部分+）、P40（点灶+）、CR（灶+）、ALK\n（1A4）（-）、Ki67（+，40%）。\n【报告时间】：2025/4/9 10:06:00",
    "role": "user"
  }
]
2026-08-10 18:24:31,091 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:24:31.090+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 86, "failed": 0, "current": {"8fa8ece894e711f1bd9827cf206dfa2d": {"id": "8fa8ece894e711f1bd9827cf206dfa2d", "doc_id": "8f6c718294e711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 16708238, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786385769380, "task_type": "dataflow", "root_trace_id": "0aa1bc1a4312482d8e4b2a1774c52cc7", "root_traceparent": "00-0aa1bc1a4312482d8e4b2a1774c52cc7-ad93c0febce673ce-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:24:33,686 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:24:33,687 INFO     29 [qwen-vl-text] LLM output (len=457):
{
  "exam_date": null,
  "report_date": "2025-04-09",
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "胸膜",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "【大体描述】：胸膜：灰白小组织一堆，大小1*0.8*0.5cm。",
  "conclusion": "【病理诊断】：（胸膜活检）送检增生的纤维组织内见腺癌浸润，请结合临床诊治。\n免疫组化：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（部分+）、P40（点灶+）、CR（灶+）、ALK（1A4）（-）、Ki67（+，40%）。",
  "physician": null,
  "reviewer": null
}
2026-08-10 18:24:33,692 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1236355, prompt_len=904
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共10行）
["【手术信息】：胸腔积液", "【取材部位】：1:胸膜×1", "2:细胞蜡块1×1", "【取材描述】：胸膜×多", "【大体描述】：胸膜：灰白小组织一堆，大小1*0.8*0.5cm。", "【病理所见】：胸膜：灰白小组织一堆，大小1*0.8*0.5cm。", "【病理诊断】：（胸膜活检）送检增生的纤维组织内见腺癌浸润，请结合临床诊治。", "免疫组化：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（部分+）、P40（点灶+）、CR（灶+）、ALK", "（1A4）（-）、Ki67（+，40%）。", "【报告时间】：2025/4/9 10:06:00"]

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
2026-08-10 18:24:40,695 INFO     29 [qwen-vl-text] coord API raw response (len=703):
[
	{"text": "【手术信息】：胸腔积液", "bbox": [172, 94, 321, 107]},
	{"text": "【取材部位】：1:胸膜×1", "bbox": [172, 113, 335, 125]},
	{"text": "2:细胞蜡块1×1", "bbox": [375, 113, 486, 125]},
	{"text": "【取材描述】：胸膜×多", "bbox": [172, 133, 319, 145]},
	{"text": "【大体描述】：胸膜：灰白小组织一堆，大小1*0.8*0.5cm。", "bbox": [172, 151, 526, 163]},
	{"text": "【病理所见】：胸膜：灰白小组织一堆，大小1*0.8*0.5cm。", "bbox": [172, 179, 526, 191]},
	{"text": "【病理诊断】：（胸膜活检）送检增生的纤维组织内见腺癌浸润，请结合临床诊治。", "bbox": [172, 206, 670, 219]},
	{"text": "免疫组化：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（部分+）、P40（点灶+）、CR（灶+）、ALK", "bbox": [151, 215, 771, 228]},
	{"text": "（1A4）（-）、Ki67（+，40%）。", "bbox": [157, 228, 350, 240]},
	{"text": "【报告时间】：2025/4/9 10:06:00", "bbox": [172, 287, 385, 299]}
]
2026-08-10 18:24:40,695 INFO     29 [qwen-vl-text] coord API: raw_items=10, valid_items=10, elapsed=7.0s
2026-08-10 18:24:40,695 INFO     29 [qwen-vl-text] coord item[0]: text=【手术信息】：胸腔积液, bbox=[172, 94, 321, 107]
2026-08-10 18:24:40,695 INFO     29 [qwen-vl-text] coord item[1]: text=【取材部位】：1:胸膜×1, bbox=[172, 113, 335, 125]
2026-08-10 18:24:40,695 INFO     29 [qwen-vl-text] coord item[2]: text=2:细胞蜡块1×1, bbox=[375, 113, 486, 125]
2026-08-10 18:24:40,695 INFO     29 [qwen-vl-text] coord item[3]: text=【取材描述】：胸膜×多, bbox=[172, 133, 319, 145]
2026-08-10 18:24:40,695 INFO     29 [qwen-vl-text] coord item[4]: text=【大体描述】：胸膜：灰白小组织一堆，大小1*0.8*0.5cm。, bbox=[172, 151, 526, 163]
2026-08-10 18:24:40,695 INFO     29 [qwen-vl-text] coord item[5]: text=【病理所见】：胸膜：灰白小组织一堆，大小1*0.8*0.5cm。, bbox=[172, 179, 526, 191]
2026-08-10 18:24:40,695 INFO     29 [qwen-vl-text] coord item[6]: text=【病理诊断】：（胸膜活检）送检增生的纤维组织内见腺癌浸润，请结合临床诊治。, bbox=[172, 206, 670, 219]
2026-08-10 18:24:40,695 INFO     29 [qwen-vl-text] coord item[7]: text=免疫组化：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（部分+）、P40（点灶+）、CR（灶+）、ALK, bbox=[151, 215, 771, 228]
2026-08-10 18:24:40,695 INFO     29 [qwen-vl-text] coord item[8]: text=（1A4）（-）、Ki67（+，40%）。, bbox=[157, 228, 350, 240]
2026-08-10 18:24:40,695 INFO     29 [qwen-vl-text] coord item[9]: text=【报告时间】：2025/4/9 10:06:00, bbox=[172, 287, 385, 299]
2026-08-10 18:24:40,695 INFO     29 [qwen-vl-text] page=11 — 10/10 coords, api_time=7.0s
2026-08-10 18:24:40,696 INFO     29 [qwen-vl-text] new_positions (10):
[[11, 102.39159790039064, 191.09129608154296, 79.13860229492188, 90.08330261230469], [11, 102.39159790039064, 199.42549591064454, 95.13470275878906, 105.23750305175781], [11, 223.23749542236328, 289.31579406738285, 95.13470275878906, 105.23750305175781], [11, 102.39159790039064, 189.90069610595705, 111.97270324707031, 122.07550354003907], [11, 102.39159790039064, 313.1277935791016, 127.12690368652345, 137.2297039794922], [11, 102.39159790039064, 313.1277935791016, 150.7001043701172, 160.80290466308594], [11, 102.39159790039064, 398.8509918212891, 173.43140502929688, 184.3761053466797], [11, 89.89029815673828, 458.9762905883789, 181.00850524902344, 191.95320556640627], [11, 93.4620980834961, 208.35499572753906, 191.95320556640627, 202.056005859375], [11, 102.39159790039064, 229.19049530029298, 241.62530700683595, 251.7281072998047]]
2026-08-10 18:24:40,696 INFO     29 [qwen-vl-text] ═══ DONE ═══ 10 positions, pages=1, time=9.7s
2026-08-10 18:24:40,702 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 18:24:40,703 INFO     29 [Trace] task=8fa8ece8 | doc=07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf | Extractor:ExaminationReport | outputs={"chunks": "4 items, types={'ExaminationReport': 4}", "html": "", "json": "594 items", "markdown": "", "text": "", "name": "07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_LabExam\": 5, \"chunks_Examination\": 4}"}
2026-08-10 18:24:40,703 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 18:24:40,707 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:24:40,708 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 18:24:41,617 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:24:41,627 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 18:24:41,627 INFO     29 [Trace] task=8fa8ece8 | doc=07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "594 items", "markdown": "", "text": "", "name": "07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_LabExam\": 5, \"chunks_Examination\": 4}"}
2026-08-10 18:24:41,627 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 18:24:41,629 INFO     29 [ChunkMerger] Merged 10 chunks from 9 sources: {'Extractor:LabExam': 5, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 4, 'Extractor:Progress': 1} (filtered 6 noise chunks)
2026-08-10 18:24:41,641 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 18:24:41,641 INFO     29 [Trace] task=8fa8ece8 | doc=07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "10 items, types={'LabReport': 5, 'AdmissionRecord': 1, 'ExaminationReport': 4}", "name": "07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf"}
2026-08-10 18:24:41,641 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 18:24:41,860 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786385769609, 'update_date': datetime.datetime(2026, 8, 10, 18, 16, 9), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1351205, 'status': '1'}
2026-08-10 18:24:42,050 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   红细胞  None  4.47  x10^12/L  4.30-5.80  False    白细胞  None  10.11  ×10^9/L  3.50-9.50  True    血红蛋白  None  131  g/L  130-175  False    中性粒细胞百分率  None  79.3  %  40.0-75.0  True    红细胞压积  None  40.0  %  40.0-50.0  False    淋巴细胞百分率  None  12.1  %  20.0-50.0  True    平均红细胞体积  None  89.4  fL  82.0-100.0  False    单核细胞百分率  None  7.0  %  3.0-10.0  False    平均血红蛋白量  None  29.4  pg  27.0-34.0  False    嗜酸细胞百分率  None  1.1  %  0.4-8.0  False    平均血红蛋白浓度  None  328  g/L  316-354  False    嗜碱细胞百分率  None  0.5  %  0.0-1.0  False    红细胞分布宽度SD  None  48.4  fL  39.0-46.0  True    中性粒细胞绝对值  None  8.02  ×10^9/L  1.80-6.30  True    红细胞分布宽度CV  None  14.8  %  10.9-14.5  True    淋巴细胞绝对值  None  1.22  ×10^9/L  1.10-3.20  False    血小板总数  None  256  ×10^9/L  125-350  False    单核细胞绝对值  None  0.71  ×10^9/L  0.10-0.60  True    血小板平均容积  None  8.5  fL  7.6-13.2  False    嗜酸细胞绝对值  None  0.11  ×10^9/L  0.02-0.52  False    血小板分布宽度  None  16.2  fL  9.0-17.0  False    嗜碱细胞绝对值  None  0.05  ×10^9/L  0.00-0.06  False    血小板比积  None  0.217  %  0.11-0.28  False    超敏C-反应蛋白  None  28.26  mg/L  0.00-6.00  True    大血小板比例  None  17.5  %  13.0-43.0  False    血清淀粉样蛋白A  None  16.24  mg/L  0.00-10.00  True   
---
   总蛋白  TP  70.10  g/L  65.00-85.00  False    白蛋白(溴甲酚绿法)  ALB  37.19  g/L  40.00-55.00  True    球蛋白  GLO  32.91  g/L  20.00-40.00  False    白蛋白:球蛋白  A:G  1.13  None  1.20-2.40  True    总胆红素  TBIL  12.6  μmol/L  ≤26.0  False    直接胆红素  DBIL  2.2  μmol/L  0.0-6.8  False    间接胆红素  IBIL  10.4  μmol/L  3.0-19.0  False    γ-谷氨酰基转移酶  GGT  25  U/L  10-60  False    碱性磷酸酶  ALP  93  U/L  45-125  False    天门冬氨酸氨基转移酶  AST  21  U/L  15-40  False    丙氨酸氨基转移酶  ALT  14  U/L  9-50  False    AST:ALT  AST:ALT  1.50  None  None  False    总胆汁酸  TBA  1.0  μmol/L  0.0-14.0  False    钾  K  4.03  mmol/L  3.50-5.30  False    钠  Na  140.3  mmol/L  137.0-147.0  False    氯  Cl  103.5  mmol/L  99.0-110.0  False    总二氧化碳  TCO2  25.9  mmol/L  21.0-30.0  False    阴离子隙  ANION  10.9  mmol/L  8.0-16.0  False    钙  Ca  2.29  mmol/L  2.11-2.52  False    无机磷  P  1.09  mmol/L  0.85-1.51  False    镁  MG  0.85  mmol/L  0.75-1.02  False    葡萄糖  GLU  5.56  mmol/L  3.90-6.10  False    尿素  UREA  5.59  mmol/L  3.60-9.50  False    肌酐(酶法)  CREA  71  μmol/L  57-111  False    尿素:肌酐  UREA:CREA  0.08  None  None  False    肾小球滤过率  eGFR(CKD-EPI)  91.01  ml/(min·1.73m^2)  ≥90  False    尿酸  UA  367  μmol/L  208-428  False    肌酸激酶  CK  33  U/L  50-310  True    乳酸脱氢酶  LDH  192  U/L  120-250  False    总胆固醇  CHOL  4.41  mmol/L  3.12-5.72  False    甘油三酯  TG  0.84  mmol/L  0.40-1.70  False    高密度脂蛋白胆固醇  HDL-C  1.16  mmol/L  1.04-1.96  False    低密度脂蛋白胆固醇  LDL-C  2.51  mmol/L  1.53-3.45  False    非高密度脂蛋白胆固醇  non-HDL-C  3.25  mmol/L  None  False    脂蛋白(a)  Lp(a)  538  mg/L  0-300  True    唾液酸  SA  803  mg/L  456-754  True    渗透压  OSM  281.1  MoSM/L  None  False    血同型半胱氨酸  HCY  10.3  μmol/L  0.0-15.0  False   
---
   白细胞  None  2.2  个/ul  0--9.2  False    红细胞  None  6.7  个/ul  0--13.1  False    上皮细胞  None  2.5  个/ul  0--5.7  False    管型  None  0.00  个/ul  0--2.25  False    电导率  None  15.5  ms/cm  3.0--39.0  False    白细胞(高倍视野)  None  0  个/HPF  0--3  False    红细胞(高倍视野)  None  1  个/HPF  0--2  False    上皮细胞(高倍视野)  None  0  个/HPF  0--5  False    管型(低倍视野)  None  0  个/LPF  0--2  False    小圆上皮细胞  None  无  None  None  False    类酵母菌  None  无  None  None  False    结晶  None  无  None  None  False    红细胞形态信息  None  未提示  None  None  False   
---
   *白细胞  None  阴性(-)  None  阴性(-)  False    *隐血  None  阴性(-)  None  阴性(-)  False    *尿蛋白  None  阴性(-)  None  阴性(-)  False    *葡萄糖  None  阴性(-)  None  阴性(-)  False    *胆红素  None  阴性(-)  None  阴性(-)  False    *尿胆原  None  阴性(-)  None  阴性(-)  False    *酸碱度  None  5.0  None  4.5--8.0  False    *比重  None  1.022  None  1.003--1.030  False    *亚硝酸盐  None  阴性(-)  None  阴性(-)  False    *酮体  None  阴性(-)  None  阴性(-)  False    颜色  None  稻黄色  None  None  False    浊度  None  CLEAR  None  None  False   
---
   大便颜色  None  黄褐色  None  黄色-黄褐色  False    大便性状  None  软便  None  软  False    白细胞  WBC  未见  /HP  无或偶见  False    红细胞  RBC  未见  /HP  无  False    巨噬细胞  None  未见  个/HP  None  False    脂肪球  None  未见  /HP  None  False    霉菌  None  未见  /HP  无  False    不消化食物  None  无  None  None  False    蛔虫卵  None  未见  None  None  False    鞭虫卵  None  未见  None  None  False    钩虫卵  None  未见  None  None  False    蛲虫卵  None  未见  None  None  False    肝吸虫卵  None  未见  None  None  False    带绦虫卵  None  未见  None  None  False    其它  None  未见异常  None  None  False    隐血  OB  阴性(-)  None  阴性(-)  False   
---
性别：男
婚姻：已婚
年龄：69岁
入院日期：2026-03-11 08:04
民族：汉族
记录日期：2026-03-11 08:06
职业：农民
病史陈述者：患者本人
主诉：确诊肺腺癌10月余，咯血2天余。
现病史：患者因“呼吸困难2月余”于2025-04-05第1次入院，入院后完善检验检查：
CEA(胸水)：癌胚抗原 538ng/ml；于04-07完善胸腔镜检查：镜下诊断：胸腔积液，胸壁结节
样改变。病理：（胸膜活检）送检增生的纤维组织内见腺癌浸润，请结合临床诊治。免疫组
化：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（部分+）、P40（点灶+）、CR（灶
+）、ALK（1A4）（-）、Ki67（+，40%）。完善评估检查：胸部增强(64排-128层)：1.符合
右侧胸腔引流术后改变，右侧液气胸并右侧颈根部及胸壁积气，肺组织压缩约70%。2.右肺
下叶占位，考虑肺癌并纵隔及双肺门淋巴结转移可能，右侧胸膜结节状增厚、强化，考虑转
移，请结合临床。3.左肺小结节，目前考虑良性，建议短期复查。4.双肺慢性炎症/纤维
灶。5.动脉粥样硬化表现。6.甲状腺改变，请结合超声检查。7.右侧第8肋骨质改变，请结
合临床。全身骨显像：1.右侧第6-8侧肋异常放射性浓聚，本院CT（2025-04-09）第6、7肋
骨未见明显骨质异常，第8肋髓腔内见局灶高密度影，建议短期CT复查。2.左侧坐骨轻度放
射性浓聚灶，本院CT未见明显骨质破坏，建议随诊。04-14复查胸部CT：对比2025-04-09
CT：1.符合右侧胸腔引流术后改变，右侧液气胸并右侧颈根部及胸壁积气，较前减轻，肺组
织压缩约30%。2.右肺下叶占位，较前相仿，考虑肺癌；纵隔及双肺门淋巴结同前；右侧胸
膜结节状增厚，较前局部稍减轻，请结合临床。3.左肺小结节，较前相仿，建议短期复查。
余所见大致同前。04-16复查胸片：1.右侧胸腔引流术后表现，对比2025-04-11X线：右侧气
胸较前明显减少；原右侧胸壁及胸壁皮下积气基本消失；右侧胸腔积液较前减少，建议复查
或结合CT检查。2.右肺下野占位，请结合临床及CT检查。患者完善基因检测未见基因突变，
于04-17给予第1周期全身化疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2 q21d，同时辅
以止吐、护胃、保肝、激素减轻化疗不良反应等治疗。于04-19给予信迪利单抗200mg抗肿瘤
免疫治疗。患者化疗顺利，准予出院。末次出院诊断：1.肺腺癌伴纵隔淋巴结、肺门淋巴
结、胸膜转移（T2bN3M1 IV期）恶性胸腔积液 2.气胸 3.左侧大隐静脉曲张 4.肝囊肿 5.双
肾囊肿 6.前列腺稍大伴钙化
患者因“确诊肺腺癌1月”于2025-05-07第2次入院，入院后完善相关检查：肺肿瘤检
验：癌胚抗原 62.1ng/ml，神经元特异性烯醇化酶 19.8ng/ml，细胞角蛋白19片段
6.21ng/ml；大便常规：未见异常；髂静脉及下肢深静脉、下肢浅静脉：左侧大隐静脉曲张，
左侧隐股静脉瓣功能不全；胸部平扫(64排-128层)：对比2025-04-14CT：1.符合右侧胸腔引
流术后改变，右侧液气胸，积液较前增多，积气较前减少；原右侧颈根部及胸壁少量积气本
第1页
次吸收。2.右肺下叶占位，较前略缩小，考虑肺癌；纵隔及双肺门淋巴结部分较前略增大；
右侧胸膜结节状增厚，较前局部稍减轻，请结合临床。3.左肺小结节，较前相仿，建议短期
复查。余所见大致同前。入院后于05-09拔除胸腔引流管。排除禁忌于05-09行第2周期全身
化疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2 q21d，并辅以激素、止吐、护胃、保肝
等治疗，05-10给予信迪利单抗200mg肿瘤免疫治疗。患者治疗结束，于2025-05-11出院。
患者因“确诊肺腺癌1月余，发热5天”于2025-05-19第3次入院，入院后完善检验检
查：大便菌群分析:细菌总数600 个/油镜视野（参考值500～5000个），革兰阳性球菌少量，
革兰阴性杆菌少量，酵母样真菌孢子+，酵母样真菌菌丝+；艰难梭菌毒素A/B检测:艰难梭
菌毒素A/B检测 0.02；大便细菌培养+药敏:经两天普通培养，鉴定生长热带念珠菌+++，无
肠球菌生长，无肠杆菌生长，无沙门氏菌、志贺氏菌生长。痰细菌学检查:经2天普通培养，
经鉴定为正常菌群生长，无流感嗜血杆菌生长。胸部平扫(64排-128层)：对比
2025-04-14CT：1.符合右侧胸腔引流术后改变，右侧液气胸，积液较前增多，积气较前减
少；原右侧颈根部及胸壁少量积气本次吸收。2.右肺下叶占位，较前略缩小，考虑肺癌；纵
隔及双肺门淋巴结部分较前略增大；右侧胸膜结节状增厚，较前局部稍减轻，请结合临床。
3.左肺小结节，较前相仿，建议短期复查。余所见大致同前。腹部（包括盆腔）平扫(64
排)：1.考虑肝多发囊肿、右肾囊肿，必要时增强扫描。2.双肾周桥隔略增厚。3.动脉粥样
硬化。4.前列腺增大伴钙化。5.L5椎体前滑脱（I°），双侧椎弓峡部裂。胸部平扫(64排
-128层)：对比2025-05-08CT：1.右侧液气胸，积液较前增多，积气较前减少。2.右肺下叶
占位，较前缩小，考虑肺癌；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜结节状增
厚，较前变化不著，请结合临床。3.左肺小结节，较前相仿，建议短期复查。余所见大致同
前。入院后给予哌拉西林他唑巴坦抗感染，蒙脱石散止泻，枯草杆菌二联活菌胶囊调整消化
道菌群，利伐沙班抗凝，制霉素片口服治疗，现患者病情稳定，于2025-05-29出院。
患者因“确诊肺腺癌2月余。”第4次入院，入院后完善辅助检查，入院后排除禁忌，
06-06行第3周期治疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2，联合信迪利单抗200mg
抗肿瘤免疫治疗，并辅以激素、止吐、护胃、保肝等治疗，治疗结束后复查血常规未见明显
骨髓抑制，于2025-06-08出院。末次出院诊断：1.恶性肿瘤维持性化学治疗 2.恶性肿瘤免
疫治疗 3.肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转移 肺门淋巴结转移 胸膜转移 恶性胸腔
积液 4.大隐静脉曲张 5.肾囊肿 6.单纯性肝囊肿。
患者因“确诊肺腺癌2月余，为继续治疗”于2025-06-26第5次入院，入院后完善相关检
查，排除禁忌，06-27行第4周期治疗：培美曲塞 0.8g d1+顺铂注射液 65mg d1、d2，联合
信迪利单抗200mg抗肿瘤免疫治疗，并辅以激素、止吐、护胃、保肝等治疗，治疗结束后复
查血常规未见明显骨髓抑制，于2025-06-29出院。末次出院诊断：1.恶性肿瘤维持性化学治
疗 2.恶性肿瘤免疫治疗 3.肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转移 肺门淋巴结转移 胸
膜转移 4.恶性胸腔积液 5.大隐静脉曲张 6.肾囊肿 7.单纯性肝囊肿.
患者因“确诊肺腺癌3月余，为继续治疗”2025-07-17入院，入院后完善相关必要辅助
第2页
检查：电解质+血气分析:酸碱度7.476，二氧化碳分压36.4mmHg，氧分压114.0mmHg；急
查血常规+CRP:红细胞3.61x10^12/L，血红蛋白110g/L，血小板总数222×10^9/L，白细
胞4.90×10^9/L，中性粒细胞绝对值3.59×10^9/L，淋巴细胞绝对值0.77×10^9/L，超
敏C-反应蛋白17.92mg/L；肺肿瘤检验：癌胚抗原54.9ng/ml，细胞角蛋白19片段
5.54ng/ml，胃泌素释放肽前体80.2pg/ml；生化系列36项:白蛋白(溴甲酚绿法)
31.59g/L，镁0.72mmol/L，肌酐(酶法)55μmol/L，肌酸激酶31U/L；DIC系列-5项:纤维
蛋白原5.47g/L，D-二聚体3.53mg/L；急查降钙素原、急查心梗三项、皮质醇(7:00-10:
00am)、促肾上腺皮质激素(8时)、甲状腺功能3项、急查NT-proBNP、大便常规(粪沉渣)+
潜血、尿液分析+尿沉渣未见明显异常。常规心电图检查(自动分析)：窦性心动过速；心
脏超声检查(含左心功能测定)：主动脉瓣轻度反流，三尖瓣轻度反流；颅脑平扫+DWI+增
强(3T)：1.双侧额顶叶及侧脑室旁白质内脱髓鞘改变。2.老年脑改变。3.部分副鼻窦炎；
右侧乳突炎。4.鼻中隔偏曲，双下鼻甲肥大。颈部：左侧颈部淋巴结稍大，右侧颈部淋巴结
可见；髂静脉及下肢深静脉、下肢浅静脉：左侧大隐静脉曲张，左侧隐股静脉瓣功能不全；
腹部(包括盆腔)平扫(64排)：1.考虑肝多发囊肿、右肾囊肿，必要时增强扫描。2.双肾周
桥隔略增厚。3.动脉粥样硬化。4.前列腺增大伴钙化。5.L5椎体前滑脱(I°)，双侧椎弓
峡部裂。以上所见较2025-05-26CT变化不著。胸部平扫(64排-128层)：对比2025-05-26CT:
1.右肺下叶肺癌，较前略缩小、其内新见空洞影；右肺小叶间隔增厚，考虑癌性淋巴管炎可
能；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜结节状增厚，较前变化不著；请结合
临床。2.右侧液气胸，积液较前略增多，积气较前明显减少。3.左肺小结节，较前相仿，建
议短期复查。4.右侧第7-9、12肋骨高密度影，较前密度增高，转移?建议ECT进一步检查。
余所见大致同前。肋骨平扫+DWI+增强(3T)：1.右侧第7-9、12肋改变，成骨性转移?请结
合其它影像学检查。2.右侧胸腔积液。3.肝内多发囊肿。排除禁忌，07-18行第5周期治疗：
培美曲塞0.8gd1+顺铂注射液65mgd1、d2，联合信迪利单抗200mg抗肿瘤免疫治疗，并辅
以激素、止吐、护胃、保肝等治疗，治疗结束后复查血常规未见明显骨髓抑制，针对肋骨异
常请放疗科会诊后建议可考虑放疗，07-21出院。
患者因“确诊肺腺癌4月，为继续治疗”2025-08-07第7次入院，入院后完善相关检查，
急查血常规+CRP:血红蛋白109g/L，血小板总数205×10^9/L，白细胞4.58×10^9/L，中
性粒细胞百分率70.9%，超敏C-反应蛋白17.43mg/L；超敏肌钙蛋白T14.80pg/ml；DIC系
列-5项:纤维蛋白原5.27g/L，D-二聚体4.37mg/L；N端-B型钠尿肽前体71.5pg/ml；促肾
上腺皮质激素(8时)：促肾上腺皮质激素(8时)31.7pg/ml；生化系列36项:白蛋白(溴甲酚绿
法)33.34g/L，钾3.93mmol/L，钠140.1mmol/L，氯104.8mmol/L，尿素5.04mmol/L，肌
酐(酶法)65μmol/L；皮质醇(7:00-10:00am)：皮质醇(7:00-10:00am)295nmol/L；甲状腺
功能3项：促甲状腺素3.17mIU/L，游离甲状腺素13.6pmol/L，游离三碘甲状腺原氨酸
4.46pmol/L；肺肿瘤检验：癌胚抗原52.6ng/ml，神经元特异性烯醇化酶20.4ng/ml，
细胞角蛋白19片段4.81ng/ml，胃泌素释放肽前体92.9pg/ml。常规心电图检查(自动分
第3页
析）：窦性心律，大致正常心电图。排除禁忌，于08-08给予第6周期化疗，方案为培美曲塞
0.8g+顺铂注射液 65mg d1、d2，联合信迪利单抗200mg 免疫治疗，过程顺利，08-10行地
舒单抗120mg抗骨转移治疗；复查血常规未见明显骨髓抑制，08-10出院。
患者因“确诊肺腺癌4月，为继续治疗”于2025-08-28第8次入院，入院后完善辅助检
查：胸部平扫：对比2025-07-18CT：1.右肺下叶肺癌，较前变化不著；右肺小叶间隔增厚，
较前变化不著，考虑癌性淋巴管炎可能；纵隔及双肺门淋巴结部分较前变化不著；右侧胸膜
结节状增厚，较前变化不著；请结合临床。2.右侧液气胸，积液较前变化不著，积气较前增
多。3.左肺小结节，较前相仿，建议短期复查。4.右侧第7-9、12肋骨高密度影，较前变化
不著，转移？建议ECT进一步检查。余所见大致同前。下腹部平扫：1.考虑右肾囊肿，较
2025-07-18变化不著，必要时增强扫描。2.双肾周桥隔略增厚。3.动脉粥样硬化。上腹部平
扫：考虑肝多发囊肿，较2025-07-18变化不明显，建议结合增强检查明确。盆腔平扫：1.前
列腺增大伴钙化。2.L5椎体前滑脱（I°），双侧椎弓峡部裂。以上所见较2025-07-18变化
不著。排除禁忌，给予培美曲塞 0.8g 联合信迪利单抗 200mg免疫治疗，并辅以激素、止
吐、护胃、保肝等治疗，治疗过程顺利，患者病情稳定，2025-08-30出院。出院诊断：1.恶
性肿瘤维持性化学治疗 2.恶性肿瘤免疫治疗 3.右肺腺癌（T2bN3M1 IV期） 纵隔淋巴结转
移 肺门淋巴结转移 胸膜转移 骨转移 4.恶性胸腔积液 5.大隐静脉曲张 6.肾囊肿 7.单纯
性肝囊肿。
患者因“确诊肺腺癌5月余，为继续治疗”于2025-10-06第9次入院，入院后完善辅助检
查：急查血常规+CRP:血红蛋白 114g/L，血小板总数 212×10^9/L，白细胞
7.30×10^9/L，中性粒细胞百分率 80.0%，超敏C-反应蛋白 16.04mg/L；皮质醇(7:00-10:
00am):皮质醇(7:00-10:00am) 442nmol/L；促肾上腺皮质激素(8时):促肾上腺皮质激素(8
时) 29.3pg/ml；甲状腺功能3项:促甲状腺素 4.94mIU/L，游离甲状腺素 14.4pmol/L，游离
三碘甲状腺原氨酸 3.85pmol/L；生化系列36项:白蛋白(溴甲酚绿法) 36.10g/L，白蛋白:球
蛋白 0.96，天门冬氨酸氨基转移酶 18U/L，丙氨酸氨基转移酶 8U/L，尿素 5.84mmol/L，
肌酐(酶法) 78μmol/L；肺肿瘤检验-莱山:癌胚抗原 68.6ng/ml，细胞角蛋白19片段
9.45ng/ml，胃泌素释放肽前体 96.7pg/ml；DIC系列-5项:纤维蛋白原 5.04g/L，D-二聚体
3.28mg/L；急查NT-proBNP:N端-B型钠尿肽前体 50.1pg/ml；急查心梗三项:超敏肌钙蛋白T
14.00pg/ml，肌酸激酶-MB同工酶质量测定 0.54ng/ml，肌红蛋白 43.2ng/ml。排除禁忌，
于2025-10-06给予本周期治疗，方案为培美曲塞 0.8g联合信迪利单抗200mg，并给予地舒单
抗120mg治疗骨转移，2025-10-07办理出院。出院诊断：1.右肺腺癌（T2bN3M1 IV期） 纵隔
淋巴结转移 肺门淋巴结转移 胸膜转移 骨转移 2.恶性胸腔积液 3.大隐静脉曲张 4.肾囊肿
5.单纯性肝囊肿。
患者因“确诊肺腺癌7月余，为继续治疗”于2025-11-07第10次入院，入院后完善相关
检查：急查血常规+CRP:血红蛋白 115g/L，血小板总数 214×10^9/L，白细胞
7.21×10^9/L，中性粒细胞百分率 82.3%，超敏C-反应蛋白 20.50mg/L；DIC系列-5项:纤维
第 4 页
蛋白原 5.04g/L，D-二聚体 2.19mg/L；皮质醇(7:00-10:00am):皮质醇(7:00-10:00am)
286nmol/L；促肾上腺皮质激素(8时):促肾上腺皮质激素(8时)23.3pg/ml；急查心梗三项:
超敏肌钙蛋白T 17.70pg/ml；肺肿瘤检验-莱山:癌胚抗原 75.8ng/ml，细胞角蛋白19片段
12.4ng/ml，胃泌素释放肽前体 90.5pg/ml；生化系列36项:白蛋白(溴甲酚绿法)
32.49g/L，脂蛋白(a)343mg/L，唾液酸 769mg/L；N端-B型钠尿肽前体、甲状腺功能3项未
见异常。常规心电图检查：窦性心动过速。全身骨显像：与本院2025-04-10骨显像比较：1.
右侧多根肋骨多发异常放射性浓聚灶，病灶数目较前增多，浓聚程度增高，提示骨转移瘤可
能大，请结合其他检查综合考虑；2.前次检查所示左侧坐骨轻度放射性浓聚灶，本次检查未
见显示；3.双肩关节及双膝关节区异常放射性浓聚，考虑炎性病变，请结合临床。颅脑平扫
+DWI+增强+薄层：1.双侧额顶叶及侧脑室旁白质内脱髓鞘改变；2.老年脑改变，双侧额颞部
少量硬膜下积液；3.部分副鼻窦炎；右侧乳突炎；4.鼻中隔偏曲，双下鼻甲肥大。心脏超声
检查（含左心功能测定）：静息状态下：心内结构及血流未见明显异常髂静脉及下肢深静脉
(双侧)：双侧髂静脉及下肢深静脉血流通畅颈部：双侧颈部未见明显增大淋巴结胸部平扫
+增强：对比2025-08-28CT：1.右肺下叶肺癌，较前增大；右肺小叶间隔增厚，较前略进
展，考虑癌性淋巴管炎可能；纵隔及双肺门淋巴结，部分较前略增大；考虑右侧胸膜转移，
较前明显进展，累及邻近右前胸壁及右侧膈肌可能；请结合临床并复查；2.右侧胸腔积液，
较前变化不著，原右侧胸腔积气吸收；3.左肺小结节，部分较前略增大（如下叶薄层
img231、243），部分结节较前相仿，建议短期复查；4.右侧第7-9、12肋骨高密度影，较前
变化不著，转移？建议ECT进一步检查；余所见大致同前。上腹部平扫+增强：考虑肝多发囊
肿，较2025-08-28变化不明显。下腹部平扫+增强：1.考虑右肾囊肿，较2025-08-28变化不
著；2.双肾周桥隔略增厚；3.动脉粥样硬化。排除禁忌给予本周期治疗，方案为培美曲塞
0.8g、信迪利单抗200mg联合恩度 210mg q21d治疗。治疗结束，患者病情稳定，2025-11-14
办理出院。出院诊断：1.右肺腺癌(T2bN3M1 IV期) 纵隔淋巴结转移 肺门淋巴结转移 胸
膜转移 骨转移 2.恶性胸腔积液 3.大隐静脉曲张 4.肾囊肿 5.肝囊肿
患者因“确诊肺腺癌8月余，为继续治疗”于2026-01-08再入院，入院后完善相关辅助
检查：01-08：急查NT-proBNP、促肾上腺皮质激素(8时)、皮质醇(7:00-10:00am)等未见明
显异常。急查血常规+CRP+SAA:红细胞 3.93x10^12/L，血红蛋白 118g/L，红细胞压积
35.8%，红细胞分布宽度SD 47.4fl，中性粒细胞百分率 77.9%，淋巴细胞百分率 9.4%，单
核细胞百分率 10.2%，淋巴细胞绝对值 0.67×10^9/L，单核细胞绝对值 0.73×10^9/L，超
敏C-反应蛋白 30.56mg/L，血清淀粉样蛋白A 26.98mg/L；急查心梗三项:超敏肌钙蛋白T
15.10pg/ml；DIC系列-5项:纤维蛋白原 6.22g/L，D-二聚体 1.66mg/L；急查降钙素原：
0.0969ng/ml；生化系列36项:白蛋白(溴甲酚绿法) 31.69g/L，白蛋白:球蛋白 0.87，肾小
球滤过率 89.97ml/(min·1.73m²)，肌酸激酶 38U/L，脂蛋白(a) 452mg/L，唾液酸
765mg/L；甲状腺功能6项:促甲状腺素 4.69mIU/L；肺肿瘤检验
癌胚抗原
73.4ng/ml，神经元特异性烯醇化酶 18.4ng/ml，细胞角蛋白19片段 19.1ng/ml，胃泌素释
第5页
放肽前体81.4pg/ml；常规心电图检查（自动分析）：窦性心动过速。下腹部平扫+增强：
1.考虑右肾囊肿，较2025-11-08变化不著。2.双肾周桥隔略增厚。3.动脉粥样硬化。上腹部
平扫+增强：考虑肝多发囊肿，较2025-11-08变化不明显。胸部平扫+增强：对比
2025-11-08CT：1.右肺下叶肺癌，范围整体较前增大；右肺小叶间隔增厚，较前进展，考虑
癌性淋巴管炎可能；纵隔及双肺门淋巴结大致同前；考虑右侧胸膜转移，较前进展，累及邻
近右前胸壁及右侧膈肌可能；请结合临床并复查。2.右侧胸腔积液，较前变化不著。3.左肺
小结节，较前相仿，建议短期复查。4.右侧第7-9、12肋骨高密度影，局部略进展，转移可
能，建议ECT进一步检查。余所见大致同前。01-09：髂静脉及下肢深静脉、下肢浅静脉：左
侧大隐静脉曲张左侧隐股静脉瓣功能不全。01-10：心脏超声检查（含左心功能测定）：静
息状态下：心内结构及血流未见明显异常。考虑患者肿瘤较前进展，请肿瘤科及放疗科会
诊，给予更换二线化疗方案，排除禁忌，1-09行开始给予恩度抗血管生成，01-12给予二线
第1周期全身化疗：白蛋白紫杉醇300mg d1、信迪利单抗200mg，01-13给予地舒单抗120mg抗
骨转移。期间联合护肝、护胃、止吐、激素等治疗，现病情平稳，准予出院。末次出院诊
断：1.右肺腺癌（T2bN3M1 IV期）纵隔淋巴结转移肺门淋巴结转移胸膜转移骨转移2.
恶性胸腔积液3.大隐静脉曲张4.肾囊肿5.肝囊肿6.贫血7.低蛋白血症
患者出院后规律服药、门诊复诊，偶有咳嗽，咳白薄痰，腰肋部水肿，于2026-2-10再
入院，
入院后完善辅助检查：NT-proBNP未见明显异常；血常规+CRP+SAA：红细胞
4.25x10^12/L，血红蛋白125g/L，红细胞压积38.4%，红细胞分布宽度SD47.8fl，中性粒
细胞百分率83.4%，淋巴细胞百分率8.0%，中性粒细胞绝对值7.35×10^9/L，淋巴细胞绝
对值0.70×10^9/L，单核细胞绝对值0.62×10^9/L，超敏C-反应蛋白24.16mg/L，血清淀
粉样蛋白A13.13mg/L；心梗三项：超敏肌钙蛋白T14.10pg/ml；降钙素原：0.0528ng/ml；生
化系列36项：白蛋白（溴甲酚绿法）34.82g/L，白蛋白：球蛋白1.02，肾小球滤过率
89.97ml/(min•1.73m²)，肌酸激酶33U/L，脂蛋白(a)510mg/L，唾液酸792mg/L；肺肿瘤
检验：癌胚抗原100ng/ml，神经元特异性烯醇化酶31.1ng/ml，细胞角蛋白19片段
28.8ng/ml，胃泌素释放肽前体87.7pg/ml；DIC系列-5项：纤维蛋白原6.71g/L，D-二聚体
1.42mg/L；心电图：窦性心律大致正常心电图。尿液分析、大便常规及潜血、促肾上腺皮
质激素(8时)、皮质醇(7:00-10:00am)、甲状腺功能6项等未见明显异常。排除禁忌，02-10
开始给予恩度抗血管生成，02-11给予二线第2周期全身化疗：白蛋白紫杉醇300mg d1，同时
辅以激素、止吐、护胃、保肝治疗，同时给予信迪利单抗200mg抗肿瘤免疫治疗，02-12给予
地舒单抗120mg抗骨转移治疗。于2026-02-13出院。末次出院诊断：1.恶性肿瘤维持性化学
治疗2.恶性肿瘤免疫治疗3.恶性肿瘤靶向治疗4.右肺腺癌（T2bN3M1 IV期）纵隔淋巴结
转移肺门淋巴结转移胸膜转移骨转移5.恶性胸腔积液6.大隐静脉曲张7.肾囊肿8.肝
囊肿。
患者出院后规律门诊复诊，偶有咳嗽、咳痰，2天前无明显诱因出现咯血，感痰较前增
第6页
多，每天数十口，色鲜红，今为进一步治疗入院。患者病后神志清，精神状态一般，食欲一
般，睡眠良好，大便正常，小便正常，体力情况一般，体重无明显变化。
既往史：否认食物、药物过敏史，参阅既往入院记录。
个人史：参阅既往入院记录。
家族史：参阅既往入院记录。
体 格 检 查
T 36.3℃ P 107次/分 R 21次/分 Bp 144/99mmHg
发育正常，营养良好，正常面容，表情自如，自主体位，神志清楚，查体合作。全身皮
肤粘膜无黄染，无皮疹，无皮下出血，无皮下结节，皮下无水肿，无肝掌、蜘蛛痣，毛发分
布均匀。全身浅表淋巴结无肿大。眼睑无水肿，结膜无苍白，眼球无突出，无震颤，巩膜无
黄染，瞳孔等大等圆，对光反射灵敏，耳廓对称，无畸形，牵拉无疼痛，外耳道无异常分泌
物，乳突无压痛，无听力粗试障碍。鼻无畸形。口唇无发绀，口腔粘膜无充血、糜烂。舌苔
薄白，伸舌无偏斜、震颤，牙龈无红肿，咽部粘膜无充血，扁桃体无肿大。颈软无抵抗，颈
动脉无异常搏动，半坐位颈静脉未见充盈，颈部大血管区未闻及血管杂音。气管居中，肝颈
静脉回流征阴性，甲状腺无肿大，无压痛、震颤、血管杂音。胸廓无畸形，呼吸运动两侧对
称，肋间隙无狭窄或饱满，胸壁无压痛，语颤无增强、减弱，胸骨无压痛。双肺叩诊清音，
呼吸规整，双肺呼吸音低，未闻及干湿性啰音，无胸膜摩擦音。心前区无异常隆起、异常搏
动、震颤，心浊音界不大，心率107次/分，律齐，心音有力，各瓣膜听诊区未闻及杂音，无
心包摩擦音。腹平坦，软，无压痛、反跳痛，腹部无包块。肝脏未触及，脾脏未触及，
Murphy氏征阴性，肾区无叩击痛，无移动性浊音。肠鸣音正常，4次/分。肛门及外生殖器未
查。脊柱正常生理弯曲，四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾），关节无肿
胀、压痛，下肢无浮肿。
肌肉无压痛，四肢肌力、肌张力未见异常，双侧肱
二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性。
专科检查： 胸廓无畸形，呼吸运动两侧对称，肋间隙无狭窄或饱满，胸壁无压痛，语
颤无增强、减弱，胸骨无压痛。双肺叩诊清音，呼吸规整，双肺呼吸音低，未闻及干湿性啰
音，无胸膜摩擦音。
辅 助 检 查
检查日期 项目 结果 检查单位 检查编号
第 7 页
2025-04-09
病理
(胸膜活检)送检增生的纤维组
织内见腺癌浸润，请结合临床诊
治。免疫组化：TTF-1（-）、
NapsinA（-）、CK7（+）、CK5/6
（部分+）、P40（点灶+）、CR（
灶+）、ALK（1A4）（-）、Ki67
(+,40%）。C-MET免疫组化检测
报告检测平台：Roche Ventana
Benchmark Ultra；抗体克隆号：
SP44,Roche；表达部位：细胞膜和
细胞浆；阳性强度及百分比：++(
40%),+(60%)阳性等级：1+
细胞数量：≥100。
初步诊断：
1.咯血
2.右肺腺癌（T2bN3M1 IV期）
纵隔淋巴结转移
肺门淋巴结转移
胸膜转移
骨转移
3.恶性胸腔积液
4.大隐静脉曲张
5.肾囊肿
6.肝囊肿
---
报告时间: 2026-03-12
【检查日期】: 2026/3/11 12:07:23
【检查所见】: 脑组织左右对称, 双侧额顶叶及侧脑室旁见斑点状稍长T1稍长T2信号, FLAIR像呈高信号
, DWI未见明显异常信号改变; 双侧基底节区见斑点状长T1长T2信号影; 增强扫描未见强化。脑室系统扩大
, 中线结构居中。脑沟、脑裂、脑池增宽。部分副鼻窦粘膜增厚, 左侧上颌窦内见类圆形长T2长T2信号影。
右侧乳突粘膜增厚。鼻中隔偏曲, 双下鼻甲肥大。
【检查诊断】: 1. 双侧额顶叶及侧脑室旁白质内脱髓鞘改变。
2. 双侧基底节区软化灶形成。
3. 老年脑改变, 双侧额颞部少量硬膜下积液。
4. 部分副鼻窦炎, 左侧上颌窦囊肿; 右侧乳突炎。
5. 鼻中隔偏曲, 双下鼻甲肥大。
以上所见较2025-11-09MR变化不著。
【书写医师】:
---
【检查日期】：2026/1/8 13:58:55
【检查所见】：右侧胸廓塌陷，右侧胸腔内见少量液体密度影，右肺肺组织压缩、密度增高，右肺下叶可
见一团块状软组织密度影，内见空洞影，增强可见轻度不均匀强化，周围伴条片状密度增高影，与远侧不张
肺组织分界不清，范围无法测量。右肺小叶间隔增厚。右侧胸膜不均匀增厚伴局部结节状、肿块状，增强可
见明显强化，邻近右前胸壁及右侧膈肌不规整。双肺内见斑片及索条影。左肺见小结节影，大者位于左肺下
叶（薄层img180），直径约为0.4cm。纵隔窗未见显示，增强扫描难以评估。气管及主支气管通畅。纵隔右
偏，纵隔及双肺门内见稍大淋巴结影，大者短径约1.1cm，增强强化欠均匀。心脏大小、形态正常，主动脉
壁及冠状动脉走行区可见高密度影。
甲状腺密度不均，内见类圆形低密度影。右侧部分肋骨内缘骨皮质增厚，右侧第7、8、9、12肋局部骨
质见片状高密度影。
【检查诊断】：对比2025-11-08CT：
1.右肺下叶肺癌，范围整体较前增大；右肺小叶间隔增厚，较前进展，考虑癌性淋巴管炎可能；纵隔及双肺
门淋巴结大致同前；考虑右侧胸膜转移，较前进展，累及邻近右前胸壁及右侧膈肌可能；请结合临床并复查
。
2.右侧胸腔积液，较前变化不著。
3.左肺小结节，较前相仿，建议短期复查。
4.右侧第7-9、12肋骨高密度影，局部略进展，转移可能，建议ECT进一步检查。
余所见大致同前。
---
【检查描述】：心搏次数：97(60~100) bpm，PR间隔：160 ms，QRS间隔：74 ms，QT间隔：334 ms，QTc
间隔：424 ms，P轴：51°，QRS轴：7°，T轴：34°
【检查诊断】：窦性心律
大致正常心电图
【检查时间】：2026/3/11 13:54:45
检查时间
心率
2026-03-11 13:54:39
PR
97 bpm
QRS
160 ms
QT/QTc
74 ms
P/QRS/T
间期
334 / 424 ms
RV5+SV1
电轴
51 / 7 / 34 °
振幅
/
mV
0.000 mV
AVR
V1
V4
AVL
V2
V5
III
V3
V6
AVF
II
---
【手术信息】：胸腔积液
【取材部位】：1:胸膜×1
2:细胞蜡块1×1
【取材描述】：胸膜×多
【大体描述】：胸膜：灰白小组织一堆，大小1*0.8*0.5cm。
【病理所见】：胸膜：灰白小组织一堆，大小1*0.8*0.5cm。
【病理诊断】：（胸膜活检）送检增生的纤维组织内见腺癌浸润，请结合临床诊治。
免疫组化：TTF-1（-）、NapsinA（-）、CK7（+）、CK5/6（部分+）、P40（点灶+）、CR（灶+）、ALK
（1A4）（-）、Ki67（+，40%）。
【报告时间】：2025/4/9 10:06:00
2026-08-10 18:24:43,205 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 18:24:43,205 INFO     29 [Trace] task=8fa8ece8 | doc=07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "10 items, types={'LabReport': 5, 'AdmissionRecord': 1, 'ExaminationReport': 4}", "name": "07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf", "embedding_token_consumption": 9682}
2026-08-10 18:24:43,205 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 18:24:43,441 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 18:24:43,441 INFO     29 [Trace] task=8fa8ece8 | doc=07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":10,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 18:24:43,446 INFO     29 [DIAG-EXECUTOR] row_position_int len=26 row[0]=(8, 105, 138, 394, 402) row[-1]=(8, 289, 346, 505, 514)
2026-08-10 18:24:43,446 INFO     29 [DIAG-EXECUTOR] row_position_int len=38 row[0]=(9, 133, 163, 90, 96) row[-1]=(9, 133, 179, 536, 543)
2026-08-10 18:24:43,446 INFO     29 [DIAG-EXECUTOR] row_position_int len=13 row[0]=(10, 104, 126, 95, 103) row[-1]=(10, 99, 148, 205, 213)
2026-08-10 18:24:43,446 INFO     29 [DIAG-EXECUTOR] row_position_int len=12 row[0]=(10, 305, 328, 96, 104) row[-1]=(10, 305, 319, 189, 197)
2026-08-10 18:24:43,446 INFO     29 [DIAG-EXECUTOR] row_position_int len=16 row[0]=(10, 123, 148, 310, 318) row[-1]=(10, 119, 130, 439, 447)
2026-08-10 18:24:43,447 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 18:24:43,447 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 18:24:43,447 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 18:24:43,447 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 18:24:43,447 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 18:24:43,451 INFO     29 set_progress(8fa8ece894e711f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 18:24:43 [DOC Engine]:
Start to index...
2026-08-10 18:24:43,465 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.009s]
2026-08-10 18:24:43,469 INFO     29 set_progress(8fa8ece894e711f1bd9827cf206dfa2d), progress: 0.81, progress_msg: 
2026-08-10 18:24:43,489 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.012s]
2026-08-10 18:24:43,504 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.010s]
2026-08-10 18:24:43,510 INFO     29 set_progress(8fa8ece894e711f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 18:24:43 Indexing done (0.06s). Task done (479.59s)
2026-08-10 18:24:43,514 INFO     29 [Done], chunks(10), token(9682), elapsed:479.59
2026-08-10 18:24:43,721 INFO     29 handle_task done for task {"id": "8fa8ece894e711f1bd9827cf206dfa2d", "doc_id": "8f6c718294e711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-YSKA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 16708238, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786385769380, "task_type": "dataflow", "root_trace_id": "0aa1bc1a4312482d8e4b2a1774c52cc7", "root_traceparent": "00-0aa1bc1a4312482d8e4b2a1774c52cc7-ad93c0febce673ce-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
