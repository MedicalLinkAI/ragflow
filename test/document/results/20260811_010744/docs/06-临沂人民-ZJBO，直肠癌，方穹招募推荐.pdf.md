# 基准结果：06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf

## 基本信息

- 文件：`06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf`
- 大小：3274.2 KB
- PDF 总页数：11
- doc_id：`df229e1a94e011f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-11T01:28:15  完成时间：2026-08-11T01:34:51  耗时：396.8s
- progress_msg：`17:34:48 Indexing done (0.17s). Task done (367.78s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 7acd8617 | 4 | 1-4 | 20200113根治术 术后XELOX 6周期 20240510复发 20240 |
| 2 | 60764c5e | 1 | 5-5 | 性别：男 年龄：64岁 出院日期：2026-01-07 17:10 住院天数：1 |
| 3 | 0ceb5dd4 | 1 | 6-6 | 检测项目：K-RAS、N-ras、Braf基因突变检测 检测方法： ARMS 荧 |
| 4 | f0f475dc | 1 | 8-8 | 【检查描述】：心搏次数：97(60~100)bpm，PR间隔：144ms，QRS |
| 5 | a5f8e5f6 | 1 | 8-8 | 【手术信息】：肿瘤位于直肠上段 【取材部位】：1:直肠×1 【取材描述】：#:肿 |
| 6 | d77721cd | 1 | 9-9 | 【手术信息】：纵隔淋巴结肿大 【取材部位】：1:EBUS组织×1 2:EBUS刷 |
| 7 | 96421b1b | 1 | 9-9 | 【检查日期】：2026/1/16 8:18:01 【检查所见】：右肺术后改变，术 |
| 8 | 49ada3f9 | 1 | 9-9 | 【检查日期】：2025/11/18 14:25:00 【检查所见】：右肺术后改变 |
| 9 | e1a6a81e | 2 | 10-11 | 2026-02-03 10:41 主 诉：本次访视为评价注射用HLN601脂质体 |
| 10 | a52d30af | 1 | 6-6 | <table><tr><td>红细胞</td><td>None</td><td> |
| 11 | f759c1d3 | 1 | 7-7 | <table><tr><td>总蛋白</td><td>TP</td><td>75 |

- chunks 总数：11
- 各 chunk 页数合计（含跨页重复）：15
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`
- 覆盖页数：11 / 11；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 1 | 0 | 1 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 1 | 1 | 1 | encounter_date, dm_admission_time, cc_text, department | **OK** |
| DischargeRecord | 出院 | 1 | 1 | 1 | admission_date, discharge_date, department, outcome | **OK** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 6 | 6 | 6 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 2 | 0 | 2 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"AdmissionRecord": 1, "DischargeRecord": 1, "ExaminationReport": 6, "LabReport": 2, "OutpatientRecord": 1}`
- ChunkMerger：`{"found": true, "merged": 11, "sources": 9, "stats": {"Extractor:LabExam": 2, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 6, "Extractor:Progress": 1}, "filtered_noise": 4}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 17:34:46,478 INFO     29 [ChunkMerger] Merged 11 chunks from 9 sources: {'Extractor:LabExam': 2, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 17:28:16,720 INFO     29 handle_task begin for task {"id": "df5ff51c94e011f1bd9827cf206dfa2d", "doc_id": "df229e1a94e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 3352826, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786382896642, "task_type": "dataflow", "root_trace_id": "02e835c46e184d6daf27401b2b0ac85a", "root_traceparent": "00-02e835c46e184d6daf27401b2b0ac85a-ddd202d54b80a7dd-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 17:28:16,906 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 17:28:17,037 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 17:28:17,049 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:28:17,049 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 17:28:17,049 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 17:28:17,057 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 17:28:17,057 INFO     29 ============================================================
2026-08-10 17:28:17,057 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 17:28:17,057 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 17:28:17,057 INFO     29 ============================================================
2026-08-10 17:28:17,057 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 17:28:17,057 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 17:28:17,059 INFO     29 No torch found.
2026-08-10 17:28:17,782 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=11
2026-08-10 17:28:17,826 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=88744, prompt_len=764
2026-08-10 17:28:19,028 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 17:28:19,029 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 17:28:19,037 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=88744, prompt_len=401
2026-08-10 17:28:20,292 INFO     29 [qwen-vl-parser] text API response (len=175):
["20200113根治术", "术后XELOX 6周期", "20240510复发", "20240601~20240828 7周贝伐+伊利替康+5FU", "20240925贝伐+卡培维持 门诊持续使用，末次25.10", "20251119确诊转移", "20251210参加HLN601脂质体项目，末次20260107行第三周期，进展出组"]
2026-08-10 17:28:20,292 INFO     29 [qwen-vl-parser] page=1 text: 7 lines (bbox 0-6)
2026-08-10 17:28:20,292 INFO     29 [qwen-vl-parser] page=1 text: 7 sections
2026-08-10 17:28:20,523 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1698675, prompt_len=764
2026-08-10 17:28:21,912 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 17:28:21,912 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 17:28:21,919 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1698675, prompt_len=401
2026-08-10 17:28:31,870 INFO     29 [qwen-vl-parser] text API response (len=1535):
["性别：男", "婚姻：丧偶", "年龄：64岁", "入院日期：2026-01-07 09:03", "民族：汉族", "记录日期：2026-01-07 09:25", "职业：离退休人员", "病史陈述者：患者本人及亲属", "主诉：直肠癌术后5年余，左肾上腺转移1年余。", "现病史：患者因“查体发现直肠肿物3天”于2020-01-06第一次住院普外科。入院后完善检查，排除手术禁忌症，行电子肠镜下消化道注药术，EMR，电子肠镜下尼龙绳结扎术，", "电子肠镜下钛夹止血术，电子肠镜下取异物术，积极术前准备，2020-01-13在气管插管全身", "麻醉下行腹腔镜下直肠癌根治术（Dixon），术后病理：（直肠）直肠隆起型中分化腺癌，", "伴脉管内癌栓，侵及浅肌层，标记上切缘、标记下切缘及环周切缘未见癌累及，肠周淋巴结", "3/18枚见癌转移。TNM分期：pT2N1bMx。免疫组化：MLH1（+），PMS2（+），MSH2（+），", "MSH6（+），Ki-67+指数约60%。术后行“XELOX”方案化疗6周期。", "2024-05-10当地医院复查CT：“提示左肾上腺肿物”。2024-05-16住院泌尿外科。入院", "后完善辅助检查：肾上腺增强(64排)：1.左侧肾上腺区占位，考虑恶性肿瘤，转移瘤？皮质", "癌？2.右侧肾上腺外侧肢增粗，增生可能大。3.脂肪肝。胸部平扫(64排-128层)：对比", "2021-10-08CT：1.符合右肺上叶术后改变，请结合临床。2.左肺下叶病灶（img33）较前略", "增大，右肺下叶（img50）结节为新见，余结节变化不著，建议随诊复查。3.新见双肺轻度", "坠积性改变；双肺慢性炎症/纤维灶，较前略增多。余所见较前变化不著。PET-CT全身显", "像：1.直肠术后，术区肠壁略增厚，FDG代谢略高，考虑炎症；肠周未见肿大淋巴结。2.右", "肺上叶结节切除术后，术区未见异常FDG代谢增高灶。3.左肾上腺占位，FDG代谢不均匀增", "高，考虑恶性病变，原发肾上腺肿瘤？4.（1）左肺下叶结节，较本院2020-07-06PET/CT、", "2021-10-09CT，体积略增大；（2）右肺下叶结节，较本院2020-07-06PET/CT、", "2021-10-09CT为新增；以上两枚结节FDG代谢均不高，建议密切随访。5.右侧中耳乳突炎", "症；鼻咽部左侧咽隐窝区炎症；双侧颈部增生淋巴结；双侧扁桃体炎症；甲状腺小结节，", "FDG代谢不高，建议B超随访；余双肺小结节，FDG代谢不高，建议随访观察；脂肪肝；双肾", "小结石；前列腺钙化灶。完善相关辅助检查后，为排除左侧肾上腺是否为转移瘤，遂请介入", "科会诊协助左侧肾上腺穿刺活检术，病理：（左侧肾上腺组织）送检示皮肤组织及大部分坏", "死组织，偶见少许异型腺体，结合病史及免疫组化结果，符合肠癌转移。免疫组化：CK20（", "+）、CK7（-）、CDX-2（+）、SATB2（+）。请我科会诊后转入。转科后于2024-05-28行左", "肾上腺穿刺活检，病理：（左侧肾上腺穿刺标本）腺癌。基因检测：KRAS突变。于", "2024-06-01、2024-06-19、2024-07-03、2024-07-17、2024-07-31、2024-08-14、", "2024-08-28给予一线治疗1-7周期：贝伐珠单抗 400mg d1+伊力替康 280mg d1+左亚叶酸钙", "175mg d1+氟尿嘧啶 0.75g d1+氟尿嘧啶 4.0g持续泵入48h，q14d。过程顺利。6周期治疗后", "第1页"]
2026-08-10 17:28:31,870 INFO     29 [qwen-vl-parser] page=2 text: 37 lines (bbox 7-43)
2026-08-10 17:28:31,870 INFO     29 [qwen-vl-parser] page=2 text: 37 sections
2026-08-10 17:28:32,102 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1785545, prompt_len=764
2026-08-10 17:28:33,455 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 17:28:33,456 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 17:28:33,470 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1785545, prompt_len=401
2026-08-10 17:28:41,116 INFO     29 [qwen-vl-parser] text API response (len=1370):
["复查疗效评价：SD。", "患者分别于2024-09-25、2024-10-14第9、10次入院给予贝伐珠单抗 400mg d1+卡培他", "滨（希罗达）1.5g bid d-14/21d维持治疗。", "出院后患者规律于门诊就诊并应用贝伐珠单抗+卡培他滨维持治疗。2025-08患者感腹", "胀，大便次数改变，大便不尽感，于2025-08-29再次入院保健科，入院后完善相关检查：肠", "镜检查：所见直结肠黏膜大致正常，直肠术后改变。给予调脂、降压、降糖等治疗后好转出", "院。", "患者因“咳嗽”2025-11-17入院全科，入院后完善相关检查排除禁忌后于2025-11-19行", "电子支气管镜检查并留取标本。2025-11-19 病理回示：EBUS组织：送检组织内见腺癌，伴", "大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS刷片）查见肿瘤细胞。2025-11-25门", "诊完善PET/CT躯干显像（颅底到大腿中上部、不含脑）：与本院2024-05-17 PET/CT比较：", "1.直肠癌术后，术区肠壁略增厚，FDG代谢增高，首先考虑炎症，请结合肠镜评价；肠周及", "腹、盆腔未见异常肿大淋巴结。2.左侧锁骨区、纵隔、右侧肺门区多发大小不等淋巴结/结", "节影，FDG代谢增高，结合病理，符合多发淋巴结转移表现。3.左肾上腺肿物治疗后，较前", "体积明显减小，FDG代谢不高，建议随诊。4.（1）右肺下叶结节，较前体积增大，代谢增", "高，考虑转移可能大；（2）左肺下叶结节，代谢不高，较前体积未见著变，建议继续随", "诊；（3）余双肺多发结节，代谢不高，部分较前为新发，不除外部分为转移性，建议治疗", "过程定期复查。5.右肺上叶结节切除术后，术区未见异常FDG代谢增高灶。6.鼻咽部后壁及", "左侧咽隐窝区炎症；甲状腺小结节，FDG代谢不高，建议B超随访；贲门部轻度FDG代谢增高", "及腹腔部分肠道FDG代谢增高，考虑炎性/生理性摄取可能；脂肪肝；双肾小结石；前列腺钙", "化灶。", "患者于2025-12-03入组评价注射用HLN601脂质体在晚期实体瘤患者中的安全性、耐受性", "及药代动力学特征和初步疗效的多中心、开放的I期临床试验。于2025-12-10行第1周期治", "疗：注射用HLN601脂质体20.2mg静脉输液。治疗结束，准予出院。", "患者于2025-12-25再次入院行第2周期治疗：注射用HLN601脂质体20.2mg静脉输液。治", "疗结束，准予出院。", "出院后患者复查血常规、肝肾功无明显异常，今为继续治疗入院。患者精神状态良好，", "食欲一般，睡眠良好，大小便正常，体力情况良好，体重较前无明显变化。", "补充病史：高脂血症（2024.12.uk-持续）", "补充合并用药：于2024.12.uk口服阿托伐他汀钙片 10mg qd 持续中，用药原因：治疗", "既往病史高脂血症（2024.12.uk-持续）。", "既往史：2021-10-15本院胸外科行“胸腔镜右肺上叶楔形切除术”，病理：右肺上", "叶：错构瘤。余参阅首次入院病历。", "个人史：参阅首次入院病历。", "家族史：参阅首次入院病历。", "第2页"]
2026-08-10 17:28:41,116 INFO     29 [qwen-vl-parser] page=3 text: 36 lines (bbox 44-79)
2026-08-10 17:28:41,116 INFO     29 [qwen-vl-parser] page=3 text: 36 sections
2026-08-10 17:28:41,339 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1584071, prompt_len=764
2026-08-10 17:28:42,593 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 17:28:42,594 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 17:28:42,604 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1584071, prompt_len=401
2026-08-10 17:28:47,243 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:28:47.241+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 81, "failed": 0, "current": {"df5ff51c94e011f1bd9827cf206dfa2d": {"id": "df5ff51c94e011f1bd9827cf206dfa2d", "doc_id": "df229e1a94e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 3352826, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786382896642, "task_type": "dataflow", "root_trace_id": "02e835c46e184d6daf27401b2b0ac85a", "root_traceparent": "00-02e835c46e184d6daf27401b2b0ac85a-ddd202d54b80a7dd-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:28:48,484 INFO     29 [qwen-vl-parser] text API response (len=971):
["体格检查", "T 35.4℃", "P 108次/分", "R 20次/分", "Bp 137/90mmHg", "H 168cm", "W 86.1kg", "S 2.02m²", "NRS 0分", "发育正常，营养中等，正常面容，表情自如，自主体位，神志清楚，查体合作。全身皮肤粘膜无黄染，无皮疹，无皮下出血，无皮下结节，皮下无水肿，无肝掌、蜘蛛痣，毛发分布均匀。全身浅表淋巴结无肿大。眼睑无水肿，结膜无苍白，眼球无突出，无震颤，巩膜无黄染，瞳孔等大等圆，对光反射灵敏，耳廓对称，无畸形，牵拉无疼痛，外耳道无异常分泌物，乳突无压痛，无听力粗试障碍。鼻无畸形。口唇无发绀，口腔粘膜无充血、糜烂。舌苔薄白，伸舌无偏斜、震颤，牙龈无红肿，咽部粘膜无充血，扁桃体无肿大。颈软无抵抗，颈动脉无异常搏动，半坐位颈静脉未见充盈，颈部大血管区未闻及血管杂音。气管居中，肝颈静脉回流征阴性，甲状腺无肿大，无压痛、震颤、血管杂音。胸廓无畸形，呼吸运动两侧对称，肋间隙无狭窄或饱满，胸壁无压痛，语颤无增强、减弱，胸骨无压痛。双肺叩诊清音，呼吸规整，双肺呼吸音清晰，未闻及干湿性啰音，无胸膜摩擦音。心前区无异常隆起、异常搏动、震颤，心浊音界不大，心率108次/分，律齐，心音有力，各瓣膜听诊区未闻及杂音，无心包摩擦音。腹平坦，软，无压痛、反跳痛，腹部无包块。肝脏未触及，脾脏未触及，Murphy氏征阴性，肾区无叩击痛，无移动性浊音。肠鸣音正常，4次/分。肛门及外生殖器无异常。脊柱正常生理弯曲，四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾），关节无肿胀、压痛，下肢无水肿。", "肌肉无压痛，四肢肌力、肌张力未见异常，双侧肱", "二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性。", "专科检查： ECOG 1分。浅表淋巴结未及肿大。胸壁、腹部可见手术瘢痕(CS病史)，愈合可。", "辅助检查", "2025-11-19 病理：EBUS组织：送检组织内见腺癌，伴大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS刷片）查见肿瘤细胞。本院。", "初步诊断：", "1.直肠中分化腺癌术后（pT2N1bM0 IIIA", "→IV期）", "左锁骨区、纵膈、右侧肺门区淋巴", "结转移", "左肾上腺转移", "第3页"]
2026-08-10 17:28:48,485 INFO     29 [qwen-vl-parser] page=4 text: 22 lines (bbox 80-101)
2026-08-10 17:28:48,485 INFO     29 [qwen-vl-parser] page=4 text: 22 sections
2026-08-10 17:28:48,665 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1040446, prompt_len=764
2026-08-10 17:28:49,924 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 17:28:49,924 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 17:28:49,947 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1040446, prompt_len=401
2026-08-10 17:28:53,698 INFO     29 [qwen-vl-parser] text API response (len=630):
["性别：男", "年龄：64岁", "出院日期：2026-01-07 17:10", "住院天数：1天", "入院情况：因直肠癌术后5年余，左肾上腺转移1年余入院。查体：ECOG 1分。胸壁、腹部可见手术瘢痕，愈合可。", "入院诊断：1.直肠中分化腺癌术后（pT2N1bM0 IIIA→IV期） 左锁骨区、纵膈、右侧肺门区淋巴结转移 左肾上腺转移 双肺转移 2.2型糖尿病伴多个并发症 2型糖尿病性周围血管病变 2型糖尿病性肾病 3.高血压病3级（极高危） 4.右肺错构瘤术后", "诊疗经过：入院后经患者及其家属同意，无禁忌，于2026-01-07行第3周期治疗：注射用HLN601脂质体20.2mg静脉输液。治疗结束，准予出院。", "治疗前TNM分期：IV期", "出院诊断：1.直肠中分化腺癌术后（pT2N1bM0 IIIA→IV期） 左锁骨区、纵膈、右侧肺门区淋巴结转移 左肾上腺转移 双肺转移 2.2型糖尿病伴多个并发症 2型糖尿病性周围血管病变 2型糖尿病性肾病 3.高血压病3级（极高危） 4.右肺错构瘤术后", "出院情况：一般情况可，查体：ECOG 1分。胸壁、腹部可见手术瘢痕，愈合可。", "出院医嘱：", "1.注意休息，避免劳累、感染；", "2.每周至少查2次血常规（3-4天一次），若白细胞、中性粒细胞或血小板下降，及时升白或升血小板治疗；", "3.出院带药：无。如有不适及时就诊。", "4.按临床试验方案要求随访。"]
2026-08-10 17:28:53,699 INFO     29 [qwen-vl-parser] page=5 text: 15 lines (bbox 102-116)
2026-08-10 17:28:53,699 INFO     29 [qwen-vl-parser] page=5 text: 15 sections
2026-08-10 17:28:54,003 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2841689, prompt_len=764
2026-08-10 17:28:55,635 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2024-05-31"
}
```
2026-08-10 17:28:55,636 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=2024-05-31
2026-08-10 17:28:55,652 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2841689, prompt_len=401
2026-08-10 17:29:08,661 INFO     29 [qwen-vl-parser] text API response (len=2161):
["检测项目：K-RAS、N-ras、Braf基因突变检测", "检测方法： ARMS 荧光定量 PCR", "样本类型：石蜡包埋组织", "质量控制：标本量：30%", "DNA 抽提方法：AmoyDx FFPE DNA Kit", "信号：合格", "试剂信息：K-RAS、N-ras、Braf 基因肿瘤相关", "DNA 质量：合格", "基因突变检测试剂盒", "阳性、阴性对照：合格", "检测结果：", "检测项目", "外显子/密码子", "突变类型", "检测结果", "KRAS Exon-2", "G12S,G12D", "阴性", "KRAS Exon-2", "G12C,G12R,G12V,G12A,G13C", "阴性", "KRAS Exon-2", "G13D", "阴性", "KRAS Exon-3", "Q61L,Q61R,Q61H,183A>C,Q61H,183A>T", "阴性", "KRAS Exon-4", "K117N(351A>T),K117N(351A>C),A146T,A146V,A146P", "阴性", "KNB 基因突变联", "合检测", "NRAS Exon-2", "G12D,G12S", "阳性", "NRAS Exon-2", "G13D", "阴性", "NRAS Exon-2", "G13R,G12C,G12V,G12A,G13V", "阴性", "NRAS Exon-3", "Q61R,Q61K,Q61L,Q61H", "阴性", "NRAS Exon-4", "A146T", "阴性", "BRAF Exon-15", "V600E1,V600K,V600E2,V600R,V600D1,V600D2", "阴性", "检测结论：", "N-ras 基因突变;K-ras、Braf 基因均未突变。", "注：(1) 分子病理检测结果与样本的收集、处理及核酸质量等有关，本报告针对本次检测样本，不一定能反映病变全貌，", "仅供临床医师参考，不能作为临床诊断和治疗的唯一依据，具体治疗方案还需临床医师根据临床情况综合判断进行制定。(2) 分", "子检测结果阴性时，不排除样本质量，未知基因异常，及极低丰度突变等原因。(3) 该检测不承担受检者检测后所产生的心理上、", "法律上及检测结果应用上等方面的任何后果，本检测报告解释权归本检测实验室所有。如有不符或疑问请及时与我们联系", "0535-6691999-83445.", "报告医师签章：", "报告日期： 2024/05/31", "项目名称", "结果", "单位", "参考范围", "项目名称", "结果", "单位", "参考区间", "*★红细胞", "4.20", "x10^12/L", "4.30-5.80", "*★白细胞", "4.59", "×10^9/L", "3.50-9.50", "*★血红蛋白", "145", "g/L", "130-175", "中性粒细胞百分率", "62.1", "%", "40.0-75.0", "*★红细胞压积", "44.0", "%", "40.0-50.0", "淋巴细胞百分率", "24.6", "%", "20.0-50.0", "*平均红细胞体积", "104.8", "fL", "82.0-100.0", "单核细胞百分率", "10.0", "%", "3.0-10.0", "*平均血红蛋白量", "34.5", "pg", "27.0-34.0", "嗜酸细胞百分率", "2.4", "%", "0.4-8.0", "*平均血红蛋白浓度", "330", "g/L", "316-354", "嗜碱细胞百分率", "0.9", "%", "0.0-1.0", "红细胞分布宽度SD", "55.1", "f1", "39.0-46.0", "中性粒细胞绝对值", "2.85", "×10^9/L", "1.80-6.30", "红细胞分布宽度CV", "14.2", "%", "10.9-14.5", "淋巴细胞绝对值", "1.13", "×10^9/L", "1.10-3.20", "*★血小板总数", "166", "×10^9/L", "125-350", "单核细胞绝对值", "0.46", "×10^9/L", "0.10-0.60", "血小板平均容积", "10.0", "fL", "7.6-13.2", "嗜酸细胞绝对值", "0.11", "×10^9/L", "0.02-0.52", "血小板分布宽度", "9.7", "f1", "9.0-17.0", "嗜碱细胞绝对值", "0.04", "×10^9/L", "0.00-0.06", "血小板比积", "0.17", "%", "0.11-0.28", "大血小板比例", "23.9", "%", "13.0-43.0", "备注评价：", "平售时间 2026-02-04 08:18", "接收时间：2026-03-04 08:30", "报告时间：2026-03-04 08:41"]
2026-08-10 17:29:08,663 INFO     29 [qwen-vl-parser] page=6 text: 167 lines (bbox 117-283)
2026-08-10 17:29:08,663 INFO     29 [qwen-vl-parser] page=6 text: 167 sections
2026-08-10 17:29:08,955 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1832828, prompt_len=764
2026-08-10 17:29:10,459 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-04"
}
```
2026-08-10 17:29:10,459 INFO     29 [qwen-vl-parser] page=7 classify=table report_date=2026-03-04
2026-08-10 17:29:10,474 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1832828, prompt_len=756
2026-08-10 17:29:19,327 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:29:19.324+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 81, "failed": 0, "current": {"df5ff51c94e011f1bd9827cf206dfa2d": {"id": "df5ff51c94e011f1bd9827cf206dfa2d", "doc_id": "df229e1a94e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 3352826, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786382896642, "task_type": "dataflow", "root_trace_id": "02e835c46e184d6daf27401b2b0ac85a", "root_traceparent": "00-02e835c46e184d6daf27401b2b0ac85a-ddd202d54b80a7dd-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:29:20,693 INFO     29 [qwen-vl-parser] table API response (len=2293):
\begin{tabular}{ccccccc}
\hline
序号 & 项目名称 & 项目代码 & 结果 & 单位 & 参考区间 & 提示 \\
\hline
1 & *★总蛋白 & TP & 75.96 & g/L & 65.00-85.00 & \\
2 & *★白蛋白(溴甲酚绿法) & ALB & 44.42 & g/L & 40.00-55.00 & \\
3 & 球蛋白 & GLO & 31.54 & g/L & 20.00-40.00 & \\
4 & 白蛋白:球蛋白 & A:G & 1.41 & & 1.20-2.40 & \\
5 & *总胆红素 & TBIL & 14.4 & $\mu$mol/L & $\le$26.0 & \\
6 & *直接胆红素 & DBIL & 2.0 & $\mu$mol/L & 0.0-6.8 & \\
7 & 间接胆红素 & IBIL & 12.4 & $\mu$mol/L & 3.0-19.0 & \\
8 & *★$\gamma$-谷氨酰基转移酶 & GGT & 49 & U/L & 10-60 & \\
9 & *★碱性磷酸酶 & ALP & 61 & U/L & 45-125 & \\
10 & *★天门冬氨酸氨基转移酶 & AST & 16 & U/L & 15-40 & \\
11 & *★丙氨酸氨基转移酶 & ALT & 6 & U/L & 9-50 & $\downarrow$ \\
12 & AST:ALT & AST:ALT & 2.67 & & & \\
13 & 总胆汁酸 & TBA & 4.1 & $\mu$mol/L & 0.0-14.0 & \\
14 & *★钾 & K & 4.67 & mmol/L & 3.50-5.30 & \\
15 & *★钠 & Na & 138.5 & mmol/L & 137.0-147.0 & \\
16 & *★氯 & Cl & 104.6 & mmol/L & 99.0-110.0 & \\
17 & 总二氧化碳 & TCO2 & 26.9 & mmol/L & 21.0-30.0 & \\
18 & 阴离子隙 & ANION & 7.0 & mmol/L & 8.0-16.0 & $\downarrow$ \\
\hline
\end{tabular}

\begin{tabular}{ccccccc}
\hline
序号 & 项目名称 & 项目代码 & 结果 & 单位 & 参考区间 & 提示 \\
\hline
19 & *★钙 & Ca & 2.35 & mmol/L & 2.11-2.52 & \\
20 & *★无机磷 & P & 1.19 & mmol/L & 0.85-1.51 & \\
21 & *镁 & MG & 0.89 & mmol/L & 0.75-1.02 & \\
22 & *★葡萄糖 & GLU & 6.21 & mmol/L & 3.90-6.10 & $\uparrow$ \\
23 & *★尿素 & UREA & 4.85 & mmol/L & 3.60-9.50 & \\
24 & *★肌酐(酶法) & CREA & 58 & $\mu$mol/L & 57-111 & \\
25 & 尿素:肌酐 & UREA:CREA & 0.08 & & & \\
26 & 肾小球滤过率 & eGFR (CKD-EPI) & 102.43 & ml/(min$\cdot$1.73m$^2$) & $\ge$90 & \\
27 & *★尿酸 & UA & 326 & $\mu$mol/L & 208-428 & \\
28 & *★肌酸激酶 & CK & 31 & U/L & 50-310 & $\downarrow$ \\
29 & *★乳酸脱氢酶 & LDH & 226 & U/L & 120-250 & \\
30 & *★总胆固醇 & CHOL & 6.49 & mmol/L & 3.12-5.72 & $\uparrow$ \\
31 & *★甘油三酯 & TG & 2.23 & mmol/L & 0.40-1.70 & $\uparrow$ \\
32 & *★高密度脂蛋白胆固醇 & HDL-C & 1.00 & mmol/L & 1.04-1.96 & $\downarrow$ \\
33 & *★低密度脂蛋白胆固醇 & LDL-C & 3.83 & mmol/L & 1.53-3.45 & $\uparrow$ \\
34 & 非高密度脂蛋白胆固醇 & non-HDL-C & 5.49 & mmol/L & & \\
35 & *脂蛋白(a) & Lp(a) & 309 & mg/L & 0-300 & $\uparrow$ \\
36 & 唾液酸 & SA & 695 & mg/L & 456-754 & \\
\hline
\end{tabular}

\begin{tabular}{ccccccc}
\hline
序号 & 项目名称 & 项目代码 & 结果 & 单位 & 参考区间 & 提示 \\
\hline
37 & 渗透压 & OSM & 277.7 & MoSM/L & & \\
38 & 血同型半胱氨酸 & HCY & 12.4 & $\mu$mol/L & 0.0-15.0 & \\
\hline
\end{tabular}
2026-08-10 17:29:20,695 INFO     29 [qwen-vl-parser] page=7 table: 59 LaTeX lines (bbox 284-342)
2026-08-10 17:29:20,695 INFO     29 [qwen-vl-parser] page=7 table: 59 sections
2026-08-10 17:29:21,014 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2627604, prompt_len=764
2026-08-10 17:29:22,564 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-02-03"
}
```
2026-08-10 17:29:22,565 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=2026-02-03
2026-08-10 17:29:22,586 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2627604, prompt_len=401
2026-08-10 17:29:28,185 INFO     29 [qwen-vl-parser] text API response (len=962):
["【检查描述】：心搏次数：97(60~100)bpm，PR间隔：144ms，QRS间隔：88ms，QT间隔：342ms，QTc", "间隔：434ms，P轴：34°，QRS轴：-30°，T轴：15°", "【检查诊断】：窦性心律", "QRS电轴左偏", "【检查时间】：2026/2/3 8:21:15", "【报告时间】：2026/2/3 8:22:02", "检查时间", "心率", "2026-02-03 08:19:19", "PR", "97 bpm", "QRS", "144 ms", "QT/QTc", "88 ms", "P/QRS/T", "342 / 434 ms", "RV5/SV1", "34 / -30 / 15 -", "RV5+SV1", "振幅", "/", "mV", "0.000 mV", "AVR", "V1", "V4", "AVL", "V2", "V5", "AVF", "V3", "V6", "【手术信息】：肿瘤位于直肠上段", "【取材部位】：1:直肠×1", "【取材描述】：#:肿物×1", "1:肿物×1", "2:肿物×1", "3:标记上切缘×2", "4:标记下切缘×1", "5:环周切缘×1", "6:肠周淋巴结×5", "7:肠周淋巴结×5", "8:肠周淋巴结×4", "【大体描述】：直肠肠管一段，长12cm，周径5-7cm，距上切缘8.5cm，下切缘3cm，见一隆起型", "肿物，范围1.4*1cm，高出粘膜面0.6cm，肿物切面灰白质硬，侵达浅肌层。", "【病理所见】：直肠肠管一段，长12cm，周径5-7cm，距上切缘8.5cm，下切缘3cm，见一隆起型", "肿物，范围1.4*1cm，高出粘膜面0.6cm，肿物切面灰白质硬，侵达浅肌层。", "【病理诊断】：（直肠）直肠隆起型中分化腺癌，伴脉管内癌栓，侵及浅肌层，标记上切缘、标记下切缘", "及环周切缘未见癌累及，肠周淋巴结3/18枚见癌转移。", "TNM分期：pT2N1bMx。", "免疫组化：MLH1（+），PMS2（+），MSH2（+），MSH6（+），Ki-67+指数约60%。", "【审核医师】：", "【报告时间】：2020/1/17 13:49:00"]
2026-08-10 17:29:28,186 INFO     29 [qwen-vl-parser] page=8 text: 54 lines (bbox 343-396)
2026-08-10 17:29:28,186 INFO     29 [qwen-vl-parser] page=8 text: 54 sections
2026-08-10 17:29:28,503 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3097713, prompt_len=764
2026-08-10 17:29:32,065 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-11-20"
}
```
2026-08-10 17:29:32,066 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=2025-11-20
2026-08-10 17:29:32,079 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3097713, prompt_len=401
2026-08-10 17:29:39,100 INFO     29 [qwen-vl-parser] text API response (len=1196):
["【手术信息】：纵隔淋巴结肿大", "【取材部位】：1:EBUS组织×1 2:EBUS刷片×1", "【取材描述】：1:EBUS组织×多", "【大体描述】：灰红碎组织少许，总体积0.4*0.3*0.1cm。", "【病理所见】：灰红碎组织少许，总体积0.4*0.3*0.1cm。", "【病理诊断】：EBUS组织：送检组织内见腺癌，伴大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS", "刷片）查见肿瘤细胞。", "【审核医师】：", "【报告时间】：2025/11/20 11:02:00", "【检查日期】：2026/1/16 8:18:01", "【检查所见】：右肺术后改变，术区可见条索影斑片影，相应支气管截断。双侧胸廓对称，纵隔居中。双", "肺见多发实性结节影，边界清，大者位于右肺下叶（薄层img259），大小约1.2*1.0cm，增强扫描可见不均", "匀强化。双肺见索条状影；双肺背侧胸膜下见条片影。气管支气管通畅，管壁无增厚，无局限性狭窄和扩张", "。纵隔及右肺门区见增大淋巴结影，大者直径约2.4cm，增强扫描可见不均匀强化。心脏大小、形态正常，", "主动脉及冠状动脉管壁见钙化影。右侧胸膜局部略厚，双侧胸腔未见液体密度影。", "【检查诊断】：对比2025-11-28CT：", "1.符合右肺上叶术后改变，术区改变较前相仿，请结合临床复查。", "2.双肺多发结节，部分较前稍饱满、部分新见，考虑转移瘤，建议复查。", "3.纵隔及右肺门增大淋巴结显示，部分较前稍大，考虑转移瘤。", "余所见大致同前。", "【报告医师】：", "【报告时间】：2026/1/16 10:57:25", "【检查日期】：2025/11/18 14:25:00", "【检查所见】：右肺术后改变，术区可见条索影斑片影，相应支气管截断。双侧胸廓对称，纵隔居中。双", "肺见多发实性结节影，边界清，大者位于左肺斜裂处（薄层img168），大小约1.2*0.8cm，增强扫描可见不", "均匀强化。双肺见索条状影；双肺背侧胸膜下见条片影。气管支气管通畅，管壁无增厚，无局限性狭窄和扩", "张。纵隔及右肺门区见增大淋巴结影，大者直径约2.3cm，增强扫描可见不均匀强化。心脏大小、形态正常", "，主动脉及冠状动脉管壁见钙化影。右侧胸膜局部略厚，双侧胸腔未见液体密度影。左侧肾上腺见一", "4.1*2.9cm软组织密度结节，不均匀强化。", "【检查诊断】：对比2025-10-22CT：", "1.符合右肺上叶术后改变，术区改变较前相仿，请结合临床复查。", "2.双肺多发结节，较前相仿，部分考虑转移瘤可能性大，建议密切复查。", "3.纵隔及右肺门增大淋巴结显示，较前相仿，考虑转移瘤。", "4.左侧肾上腺结节，考虑转移瘤，大致同前。", "余所见大致同前。"]
2026-08-10 17:29:39,100 INFO     29 [qwen-vl-parser] page=9 text: 35 lines (bbox 397-431)
2026-08-10 17:29:39,100 INFO     29 [qwen-vl-parser] page=9 text: 35 sections
2026-08-10 17:29:39,364 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1698990, prompt_len=764
2026-08-10 17:29:40,636 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 17:29:40,636 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=None
2026-08-10 17:29:40,647 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1698990, prompt_len=401
2026-08-10 17:29:47,152 INFO     29 [qwen-vl-parser] text API response (len=1137):
["2026-02-03 10:41", "主 诉：本次访视为评价注射用HLN601脂质体在晚期实体瘤患者中的安全性、耐受性及药代动力", "学特征和初步疗效的多中心、开放性的I期临床试验项目安全性随访。", "病 史：同前", "审阅受试者日志卡：不适用", "试验用药品/医疗器械使用的依从性：不适用", "合并用药/合并非药物治疗：", "(1) 合并用药：", "同前", "(2) 合并非药物治疗：", "无", "体格、专科检查以及辅助检查：", "(1) 体格、专科检查：", "2026年2月3日 早 8:36 测 生命体征 ：T:36.5℃ P:78次/分 R:19次/分 BP:137/83 mmHg，体", "重：84.7Kg，体格检查同筛选期，ECOG评分1分", "(2) 辅助检查：", "血细胞分析（5分类）、生化系列（36项）、D-二聚体、尿分析+沉渣、凝血四项、常规心电图，", "第 1 页", "未见明显异常。", "疗效评估：", "本次访视进行以下疗效评估：不适用", "不良事件：", "(1) 既往未转归的不良事件：无", "(2) 新发生的不良事件：", "不适用", "其 他：病历更正：2026-01-20门诊病历中“病历更正：2025.12.24住院病历中Bp:142/92mmHg（", "CS 与既往病史 高血压（2025.UNK-持续）有关），Bp：143/87mmHg（CS 与既往病史 高血压（", "2025.UNK-持续）有关）更正为（CS 与既往病史 高血压（2005.UNK-持续）有关）” 改为“", "2025.12.25住院病历中Bp:142/92mmHg（CS 与既往病史 高血压（2025.UNK-持续）有关），Bp：", "143/87mmHg（CS 与既往病史 高血压（2025.UNK-持续）有关）更正为（CS 与既往病史 高血压（", "2005.UNK-持续）有关）”时间更正错误，应为：“2025.12.25住院病历中Bp:142/92mmHg（CS 与既往", "病史 高血压（2025.UNK-持续）有关），Bp：143/87mmHg（CS 与既往病史 高血压（2025.UNK-持续）", "有关）更正为（CS 与既往病史 高血压（2005.UNK-持续）有关）” 改为“2025.12.25住院病历中Bp：", "142/92mmHg（CS 与既往病史 高血压（2025.UNK-持续）有关），Bp：143/87mmHg（CS 与既往病史 高", "血压（2025.UNK-持续）有关）更正为（CS 与既往病史 高血压（2005.UNK-持续）有关）", "第 2 页"]
2026-08-10 17:29:47,152 INFO     29 [qwen-vl-parser] page=10 text: 36 lines (bbox 432-467)
2026-08-10 17:29:47,153 INFO     29 [qwen-vl-parser] page=10 text: 36 sections
2026-08-10 17:29:47,292 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=686334, prompt_len=764
2026-08-10 17:29:48,658 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 17:29:48,658 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=None
2026-08-10 17:29:48,668 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=686334, prompt_len=401
2026-08-10 17:29:49,485 INFO     29 [qwen-vl-parser] text API response (len=113):
["门诊诊断:", "肺恶性肿瘤", "诊疗意见:", "(1)后续访视:出组,出组原因:疾病进展", "(2)发放试验用药品/医疗器械:不适用", "(3)其他用药/非药物治疗医嘱:无", "(4)其他:无", "第3页"]
2026-08-10 17:29:49,485 INFO     29 [qwen-vl-parser] page=11 text: 8 lines (bbox 468-475)
2026-08-10 17:29:49,485 INFO     29 [qwen-vl-parser] page=11 text: 8 sections
2026-08-10 17:29:49,485 INFO     29 [qwen-vl-parser] parse_pdf done: 476 sections from 11 pages.
2026-08-10 17:29:49,495 INFO     29 Close text detector.
2026-08-10 17:29:49,923 INFO     29 Close text recognizer.
2026-08-10 17:29:50,335 INFO     29 Close recognizer.
2026-08-10 17:29:50,777 INFO     29 Close recognizer.
2026-08-10 17:29:51,268 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 17:29:51,269 INFO     29 [Trace] task=df5ff51c | doc=06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf | Parser:MedLink | outputs={"html": "", "json": "476 items", "markdown": "", "text": "", "name": "06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf", "output_format": "json"}
2026-08-10 17:29:51,269 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 17:29:51,293 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:29:51,293 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 20200113根治术\n[BBOX-1] 术后XELOX 6周期\n[BBOX-2] 20240510复发\n[BBOX-3] 20240601~20240828 7周贝伐+伊利替康+5FU\n[BBOX-4] 20240925贝伐+卡培维持 门诊持续使用，末次25.10\n[BBOX-5] 20251119确诊转移\n[BBOX-6] 20251210参加HLN601脂质体项目，末次20260107行第三周期，进展出组\n[BBOX-7] 性别：男\n[BBOX-8] 婚姻：丧偶\n[BBOX-9] 年龄：64岁\n[BBOX-10] 入院日期：2026-01-07 09:03\n[BBOX-11] 民族：汉族\n[BBOX-12] 记录日期：2026-01-07 09:25\n[BBOX-13] 职业：离退休人员\n[BBOX-14] 病史陈述者：患者本人及亲属\n[BBOX-15] 主诉：直肠癌术后5年余，左肾上腺转移1年余。\n[BBOX-16] 现病史：患者因“查体发现直肠肿物3天”于2020-01-06第一次住院普外科。入院后完善检查，排除手术禁忌症，行电子肠镜下消化道注药术，EMR，电子肠镜下尼龙绳结扎术，\n[BBOX-17] 电子肠镜下钛夹止血术，电子肠镜下取异物术，积极术前准备，2020-01-13在气管插管全身\n[BBOX-18] 麻醉下行腹腔镜下直肠癌根治术（Dixon），术后病理：（直肠）直肠隆起型中分化腺癌，\n[BBOX-19] 伴脉管内癌栓，侵及浅肌层，标记上切缘、标记下切缘及环周切缘未见癌累及，肠周淋巴结\n[BBOX-20] 3/18枚见癌转移。TNM分期：pT2N1bMx。免疫组化：MLH1（+），PMS2（+），MSH2（+），\n[BBOX-21] MSH6（+），Ki-67+指数约60%。术后行“XELOX”方案化疗6周期。\n[BBOX-22] 2024-05-10当地医院复查CT：“提示左肾上腺肿物”。2024-05-16住院泌尿外科。入院\n[BBOX-23] 后完善辅助检查：肾上腺增强(64排)：1.左侧肾上腺区占位，考虑恶性肿瘤，转移瘤？皮质\n[BBOX-24] 癌？2.右侧肾上腺外侧肢增粗，增生可能大。3.脂肪肝。胸部平扫(64排-128层)：对比\n[BBOX-25] 2021-10-08CT：1.符合右肺上叶术后改变，请结合临床。2.左肺下叶病灶（img33）较前略\n[BBOX-26] 增大，右肺下叶（img50）结节为新见，余结节变化不著，建议随诊复查。3.新见双肺轻度\n[BBOX-27] 坠积性改变；双肺慢性炎症/纤维灶，较前略增多。余所见较前变化不著。PET-CT全身显\n[BBOX-28] 像：1.直肠术后，术区肠壁略增厚，FDG代谢略高，考虑炎症；肠周未见肿大淋巴结。2.右\n[BBOX-29] 肺上叶结节切除术后，术区未见异常FDG代谢增高灶。3.左肾上腺占位，FDG代谢不均匀增\n[BBOX-30] 高，考虑恶性病变，原发肾上腺肿瘤？4.（1）左肺下叶结节，较本院2020-07-06PET/CT、\n[BBOX-31] 2021-10-09CT，体积略增大；（2）右肺下叶结节，较本院2020-07-06PET/CT、\n[BBOX-32] 2021-10-09CT为新增；以上两枚结节FDG代谢均不高，建议密切随访。5.右侧中耳乳突炎\n[BBOX-33] 症；鼻咽部左侧咽隐窝区炎症；双侧颈部增生淋巴结；双侧扁桃体炎症；甲状腺小结节，\n[BBOX-34] FDG代谢不高，建议B超随访；余双肺小结节，FDG代谢不高，建议随访观察；脂肪肝；双肾\n[BBOX-35] 小结石；前列腺钙化灶。完善相关辅助检查后，为排除左侧肾上腺是否为转移瘤，遂请介入\n[BBOX-36] 科会诊协助左侧肾上腺穿刺活检术，病理：（左侧肾上腺组织）送检示皮肤组织及大部分坏\n[BBOX-37] 死组织，偶见少许异型腺体，结合病史及免疫组化结果，符合肠癌转移。免疫组化：CK20（\n[BBOX-38] +）、CK7（-）、CDX-2（+）、SATB2（+）。请我科会诊后转入。转科后于2024-05-28行左\n[BBOX-39] 肾上腺穿刺活检，病理：（左侧肾上腺穿刺标本）腺癌。基因检测：KRAS突变。于\n[BBOX-40] 2024-06-01、2024-06-19、2024-07-03、2024-07-17、2024-07-31、2024-08-14、\n[BBOX-41] 2024-08-28给予一线治疗1-7周期：贝伐珠单抗 400mg d1+伊力替康 280mg d1+左亚叶酸钙\n[BBOX-42] 175mg d1+氟尿嘧啶 0.75g d1+氟尿嘧啶 4.0g持续泵入48h，q14d。过程顺利。6周期治疗后\n[BBOX-43] 第1页\n[BBOX-44] 复查疗效评价：SD。\n[BBOX-45] 患者分别于2024-09-25、2024-10-14第9、10次入院给予贝伐珠单抗 400mg d1+卡培他\n[BBOX-46] 滨（希罗达）1.5g bid d-14/21d维持治疗。\n[BBOX-47] 出院后患者规律于门诊就诊并应用贝伐珠单抗+卡培他滨维持治疗。2025-08患者感腹\n[BBOX-48] 胀，大便次数改变，大便不尽感，于2025-08-29再次入院保健科，入院后完善相关检查：肠\n[BBOX-49] 镜检查：所见直结肠黏膜大致正常，直肠术后改变。给予调脂、降压、降糖等治疗后好转出\n[BBOX-50] 院。\n[BBOX-51] 患者因“咳嗽”2025-11-17入院全科，入院后完善相关检查排除禁忌后于2025-11-19行\n[BBOX-52] 电子支气管镜检查并留取标本。2025-11-19 病理回示：EBUS组织：送检组织内见腺癌，伴\n[BBOX-53] 大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS刷片）查见肿瘤细胞。2025-11-25门\n[BBOX-54] 诊完善PET/CT躯干显像（颅底到大腿中上部、不含脑）：与本院2024-05-17 PET/CT比较：\n[BBOX-55] 1.直肠癌术后，术区肠壁略增厚，FDG代谢增高，首先考虑炎症，请结合肠镜评价；肠周及\n[BBOX-56] 腹、盆腔未见异常肿大淋巴结。2.左侧锁骨区、纵隔、右侧肺门区多发大小不等淋巴结/结\n[BBOX-57] 节影，FDG代谢增高，结合病理，符合多发淋巴结转移表现。3.左肾上腺肿物治疗后，较前\n[BBOX-58] 体积明显减小，FDG代谢不高，建议随诊。4.（1）右肺下叶结节，较前体积增大，代谢增\n[BBOX-59] 高，考虑转移可能大；（2）左肺下叶结节，代谢不高，较前体积未见著变，建议继续随\n[BBOX-60] 诊；（3）余双肺多发结节，代谢不高，部分较前为新发，不除外部分为转移性，建议治疗\n[BBOX-61] 过程定期复查。5.右肺上叶结节切除术后，术区未见异常FDG代谢增高灶。6.鼻咽部后壁及\n[BBOX-62] 左侧咽隐窝区炎症；甲状腺小结节，FDG代谢不高，建议B超随访；贲门部轻度FDG代谢增高\n[BBOX-63] 及腹腔部分肠道FDG代谢增高，考虑炎性/生理性摄取可能；脂肪肝；双肾小结石；前列腺钙\n[BBOX-64] 化灶。\n[BBOX-65] 患者于2025-12-03入组评价注射用HLN601脂质体在晚期实体瘤患者中的安全性、耐受性\n[BBOX-66] 及药代动力学特征和初步疗效的多中心、开放的I期临床试验。于2025-12-10行第1周期治\n[BBOX-67] 疗：注射用HLN601脂质体20.2mg静脉输液。治疗结束，准予出院。\n[BBOX-68] 患者于2025-12-25再次入院行第2周期治疗：注射用HLN601脂质体20.2mg静脉输液。治\n[BBOX-69] 疗结束，准予出院。\n[BBOX-70] 出院后患者复查血常规、肝肾功无明显异常，今为继续治疗入院。患者精神状态良好，\n[BBOX-71] 食欲一般，睡眠良好，大小便正常，体力情况良好，体重较前无明显变化。\n[BBOX-72] 补充病史：高脂血症（2024.12.uk-持续）\n[BBOX-73] 补充合并用药：于2024.12.uk口服阿托伐他汀钙片 10mg qd 持续中，用药原因：治疗\n[BBOX-74] 既往病史高脂血症（2024.12.uk-持续）。\n[BBOX-75] 既往史：2021-10-15本院胸外科行“胸腔镜右肺上叶楔形切除术”，病理：右肺上\n[BBOX-76] 叶：错构瘤。余参阅首次入院病历。\n[BBOX-77] 个人史：参阅首次入院病历。\n[BBOX-78] 家族史：参阅首次入院病历。\n[BBOX-79] 第2页\n[BBOX-80] 体格检查\n[BBOX-81] T 35.4℃\n[BBOX-82] P 108次/分\n[BBOX-83] R 20次/分\n[BBOX-84] Bp 137/90mmHg\n[BBOX-85] H 168cm\n[BBOX-86] W 86.1kg\n[BBOX-87] S 2.02m²\n[BBOX-88] NRS 0分\n[BBOX-89] 发育正常，营养中等，正常面容，表情自如，自主体位，神志清楚，查体合作。全身皮肤粘膜无黄染，无皮疹，无皮下出血，无皮下结节，皮下无水肿，无肝掌、蜘蛛痣，毛发分布均匀。全身浅表淋巴结无肿大。眼睑无水肿，结膜无苍白，眼球无突出，无震颤，巩膜无黄染，瞳孔等大等圆，对光反射灵敏，耳廓对称，无畸形，牵拉无疼痛，外耳道无异常分泌物，乳突无压痛，无听力粗试障碍。鼻无畸形。口唇无发绀，口腔粘膜无充血、糜烂。舌苔薄白，伸舌无偏斜、震颤，牙龈无红肿，咽部粘膜无充血，扁桃体无肿大。颈软无抵抗，颈动脉无异常搏动，半坐位颈静脉未见充盈，颈部大血管区未闻及血管杂音。气管居中，肝颈静脉回流征阴性，甲状腺无肿大，无压痛、震颤、血管杂音。胸廓无畸形，呼吸运动两侧对称，肋间隙无狭窄或饱满，胸壁无压痛，语颤无增强、减弱，胸骨无压痛。双肺叩诊清音，呼吸规整，双肺呼吸音清晰，未闻及干湿性啰音，无胸膜摩擦音。心前区无异常隆起、异常搏动、震颤，心浊音界不大，心率108次/分，律齐，心音有力，各瓣膜听诊区未闻及杂音，无心包摩擦音。腹平坦，软，无压痛、反跳痛，腹部无包块。肝脏未触及，脾脏未触及，Murphy氏征阴性，肾区无叩击痛，无移动性浊音。肠鸣音正常，4次/分。肛门及外生殖器无异常。脊柱正常生理弯曲，四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾），关节无肿胀、压痛，下肢无水肿。\n[BBOX-90] 肌肉无压痛，四肢肌力、肌张力未见异常，双侧肱\n[BBOX-91] 二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性。\n[BBOX-92] 专科检查： ECOG 1分。浅表淋巴结未及肿大。胸壁、腹部可见手术瘢痕(CS病史)，愈合可。\n[BBOX-93] 辅助检查\n[BBOX-94] 2025-11-19 病理：EBUS组织：送检组织内见腺癌，伴大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS刷片）查见肿瘤细胞。本院。\n[BBOX-95] 初步诊断：\n[BBOX-96] 1.直肠中分化腺癌术后（pT2N1bM0 IIIA\n[BBOX-97] →IV期）\n[BBOX-98] 左锁骨区、纵膈、右侧肺门区淋巴\n[BBOX-99] 结转移\n[BBOX-100] 左肾上腺转移\n[BBOX-101] 第3页\n[BBOX-102] 性别：男\n[BBOX-103] 年龄：64岁\n[BBOX-104] 出院日期：2026-01-07 17:10\n[BBOX-105] 住院天数：1天\n[BBOX-106] 入院情况：因直肠癌术后5年余，左肾上腺转移1年余入院。查体：ECOG 1分。胸壁、腹部可见手术瘢痕，愈合可。\n[BBOX-107] 入院诊断：1.直肠中分化腺癌术后（pT2N1bM0 IIIA→IV期） 左锁骨区、纵膈、右侧肺门区淋巴结转移 左肾上腺转移 双肺转移 2.2型糖尿病伴多个并发症 2型糖尿病性周围血管病变 2型糖尿病性肾病 3.高血压病3级（极高危） 4.右肺错构瘤术后\n[BBOX-108] 诊疗经过：入院后经患者及其家属同意，无禁忌，于2026-01-07行第3周期治疗：注射用HLN601脂质体20.2mg静脉输液。治疗结束，准予出院。\n[BBOX-109] 治疗前TNM分期：IV期\n[BBOX-110] 出院诊断：1.直肠中分化腺癌术后（pT2N1bM0 IIIA→IV期） 左锁骨区、纵膈、右侧肺门区淋巴结转移 左肾上腺转移 双肺转移 2.2型糖尿病伴多个并发症 2型糖尿病性周围血管病变 2型糖尿病性肾病 3.高血压病3级（极高危） 4.右肺错构瘤术后\n[BBOX-111] 出院情况：一般情况可，查体：ECOG 1分。胸壁、腹部可见手术瘢痕，愈合可。\n[BBOX-112] 出院医嘱：\n[BBOX-113] 1.注意休息，避免劳累、感染；\n[BBOX-114] 2.每周至少查2次血常规（3-4天一次），若白细胞、中性粒细胞或血小板下降，及时升白或升血小板治疗；\n[BBOX-115] 3.出院带药：无。如有不适及时就诊。\n[BBOX-116] 4.按临床试验方案要求随访。\n[BBOX-117] 检测项目：K-RAS、N-ras、Braf基因突变检测\n[BBOX-118] 检测方法： ARMS 荧光定量 PCR\n[BBOX-119] 样本类型：石蜡包埋组织\n[BBOX-120] 质量控制：标本量：30%\n[BBOX-121] DNA 抽提方法：AmoyDx FFPE DNA Kit\n[BBOX-122] 信号：合格\n[BBOX-123] 试剂信息：K-RAS、N-ras、Braf 基因肿瘤相关\n[BBOX-124] DNA 质量：合格\n[BBOX-125] 基因突变检测试剂盒\n[BBOX-126] 阳性、阴性对照：合格\n[BBOX-127] 检测结果：\n[BBOX-128] 检测项目\n[BBOX-129] 外显子/密码子\n[BBOX-130] 突变类型\n[BBOX-131] 检测结果\n[BBOX-132] KRAS Exon-2\n[BBOX-133] G12S,G12D\n[BBOX-134] 阴性\n[BBOX-135] KRAS Exon-2\n[BBOX-136] G12C,G12R,G12V,G12A,G13C\n[BBOX-137] 阴性\n[BBOX-138] KRAS Exon-2\n[BBOX-139] G13D\n[BBOX-140] 阴性\n[BBOX-141] KRAS Exon-3\n[BBOX-142] Q61L,Q61R,Q61H,183A>C,Q61H,183A>T\n[BBOX-143] 阴性\n[BBOX-144] KRAS Exon-4\n[BBOX-145] K117N(351A>T),K117N(351A>C),A146T,A146V,A146P\n[BBOX-146] 阴性\n[BBOX-147] KNB 基因突变联\n[BBOX-148] 合检测\n[BBOX-149] NRAS Exon-2\n[BBOX-150] G12D,G12S\n[BBOX-151] 阳性\n[BBOX-152] NRAS Exon-2\n[BBOX-153] G13D\n[BBOX-154] 阴性\n[BBOX-155] NRAS Exon-2\n[BBOX-156] G13R,G12C,G12V,G12A,G13V\n[BBOX-157] 阴性\n[BBOX-158] NRAS Exon-3\n[BBOX-159] Q61R,Q61K,Q61L,Q61H\n[BBOX-160] 阴性\n[BBOX-161] NRAS Exon-4\n[BBOX-162] A146T\n[BBOX-163] 阴性\n[BBOX-164] BRAF Exon-15\n[BBOX-165] V600E1,V600K,V600E2,V600R,V600D1,V600D2\n[BBOX-166] 阴性\n[BBOX-167] 检测结论：\n[BBOX-168] N-ras 基因突变;K-ras、Braf 基因均未突变。\n[BBOX-169] 注：(1) 分子病理检测结果与样本的收集、处理及核酸质量等有关，本报告针对本次检测样本，不一定能反映病变全貌，\n[BBOX-170] 仅供临床医师参考，不能作为临床诊断和治疗的唯一依据，具体治疗方案还需临床医师根据临床情况综合判断进行制定。(2) 分\n[BBOX-171] 子检测结果阴性时，不排除样本质量，未知基因异常，及极低丰度突变等原因。(3) 该检测不承担受检者检测后所产生的心理上、\n[BBOX-172] 法律上及检测结果应用上等方面的任何后果，本检测报告解释权归本检测实验室所有。如有不符或疑问请及时与我们联系\n[BBOX-173] 0535-6691999-83445.\n[BBOX-174] 报告医师签章：\n[BBOX-175] 报告日期： 2024/05/31\n[BBOX-176] 项目名称\n[BBOX-177] 结果\n[BBOX-178] 单位\n[BBOX-179] 参考范围\n[BBOX-180] 项目名称\n[BBOX-181] 结果\n[BBOX-182] 单位\n[BBOX-183] 参考区间\n[BBOX-184] *★红细胞\n[BBOX-185] 4.20\n[BBOX-186] x10^12/L\n[BBOX-187] 4.30-5.80\n[BBOX-188] *★白细胞\n[BBOX-189] 4.59\n[BBOX-190] ×10^9/L\n[BBOX-191] 3.50-9.50\n[BBOX-192] *★血红蛋白\n[BBOX-193] 145\n[BBOX-194] g/L\n[BBOX-195] 130-175\n[BBOX-196] 中性粒细胞百分率\n[BBOX-197] 62.1\n[BBOX-198] %\n[BBOX-199] 40.0-75.0\n[BBOX-200] *★红细胞压积\n[BBOX-201] 44.0\n[BBOX-202] %\n[BBOX-203] 40.0-50.0\n[BBOX-204] 淋巴细胞百分率\n[BBOX-205] 24.6\n[BBOX-206] %\n[BBOX-207] 20.0-50.0\n[BBOX-208] *平均红细胞体积\n[BBOX-209] 104.8\n[BBOX-210] fL\n[BBOX-211] 82.0-100.0\n[BBOX-212] 单核细胞百分率\n[BBOX-213] 10.0\n[BBOX-214] %\n[BBOX-215] 3.0-10.0\n[BBOX-216] *平均血红蛋白量\n[BBOX-217] 34.5\n[BBOX-218] pg\n[BBOX-219] 27.0-34.0\n[BBOX-220] 嗜酸细胞百分率\n[BBOX-221] 2.4\n[BBOX-222] %\n[BBOX-223] 0.4-8.0\n[BBOX-224] *平均血红蛋白浓度\n[BBOX-225] 330\n[BBOX-226] g/L\n[BBOX-227] 316-354\n[BBOX-228] 嗜碱细胞百分率\n[BBOX-229] 0.9\n[BBOX-230] %\n[BBOX-231] 0.0-1.0\n[BBOX-232] 红细胞分布宽度SD\n[BBOX-233] 55.1\n[BBOX-234] f1\n[BBOX-235] 39.0-46.0\n[BBOX-236] 中性粒细胞绝对值\n[BBOX-237] 2.85\n[BBOX-238] ×10^9/L\n[BBOX-239] 1.80-6.30\n[BBOX-240] 红细胞分布宽度CV\n[BBOX-241] 14.2\n[BBOX-242] %\n[BBOX-243] 10.9-14.5\n[BBOX-244] 淋巴细胞绝对值\n[BBOX-245] 1.13\n[BBOX-246] ×10^9/L\n[BBOX-247] 1.10-3.20\n[BBOX-248] *★血小板总数\n[BBOX-249] 166\n[BBOX-250] ×10^9/L\n[BBOX-251] 125-350\n[BBOX-252] 单核细胞绝对值\n[BBOX-253] 0.46\n[BBOX-254] ×10^9/L\n[BBOX-255] 0.10-0.60\n[BBOX-256] 血小板平均容积\n[BBOX-257] 10.0\n[BBOX-258] fL\n[BBOX-259] 7.6-13.2\n[BBOX-260] 嗜酸细胞绝对值\n[BBOX-261] 0.11\n[BBOX-262] ×10^9/L\n[BBOX-263] 0.02-0.52\n[BBOX-264] 血小板分布宽度\n[BBOX-265] 9.7\n[BBOX-266] f1\n[BBOX-267] 9.0-17.0\n[BBOX-268] 嗜碱细胞绝对值\n[BBOX-269] 0.04\n[BBOX-270] ×10^9/L\n[BBOX-271] 0.00-0.06\n[BBOX-272] 血小板比积\n[BBOX-273] 0.17\n[BBOX-274] %\n[BBOX-275] 0.11-0.28\n[BBOX-276] 大血小板比例\n[BBOX-277] 23.9\n[BBOX-278] %\n[BBOX-279] 13.0-43.0\n[BBOX-280] 备注评价：\n[BBOX-281] 平售时间 2026-02-04 08:18\n[BBOX-282] 接收时间：2026-03-04 08:30\n[BBOX-283] 报告时间：2026-03-04 08:41\n[BBOX-284] \\begin{tabular}{ccccccc}\n[BBOX-285] 报告时间: 2026-03-04\n[BBOX-286] \\hline\n[BBOX-287] 序号 & 项目名称 & 项目代码 & 结果 & 单位 & 参考区间 & 提示 \\\\\n[BBOX-288] \\hline\n[BBOX-289] 1 & *★总蛋白 & TP & 75.96 & g/L & 65.00-85.00 & \\\\\n[BBOX-290] 2 & *★白蛋白(溴甲酚绿法) & ALB & 44.42 & g/L & 40.00-55.00 & \\\\\n[BBOX-291] 3 & 球蛋白 & GLO & 31.54 & g/L & 20.00-40.00 & \\\\\n[BBOX-292] 4 & 白蛋白:球蛋白 & A:G & 1.41 & & 1.20-2.40 & \\\\\n[BBOX-293] 5 & *总胆红素 & TBIL & 14.4 & $\\mu$mol/L & $\\le$26.0 & \\\\\n[BBOX-294] 6 & *直接胆红素 & DBIL & 2.0 & $\\mu$mol/L & 0.0-6.8 & \\\\\n[BBOX-295] 7 & 间接胆红素 & IBIL & 12.4 & $\\mu$mol/L & 3.0-19.0 & \\\\\n[BBOX-296] 8 & *★$\\gamma$-谷氨酰基转移酶 & GGT & 49 & U/L & 10-60 & \\\\\n[BBOX-297] 9 & *★碱性磷酸酶 & ALP & 61 & U/L & 45-125 & \\\\\n[BBOX-298] 10 & *★天门冬氨酸氨基转移酶 & AST & 16 & U/L & 15-40 & \\\\\n[BBOX-299] 11 & *★丙氨酸氨基转移酶 & ALT & 6 & U/L & 9-50 & $\\downarrow$ \\\\\n[BBOX-300] 12 & AST:ALT & AST:ALT & 2.67 & & & \\\\\n[BBOX-301] 13 & 总胆汁酸 & TBA & 4.1 & $\\mu$mol/L & 0.0-14.0 & \\\\\n[BBOX-302] 14 & *★钾 & K & 4.67 & mmol/L & 3.50-5.30 & \\\\\n[BBOX-303] 15 & *★钠 & Na & 138.5 & mmol/L & 137.0-147.0 & \\\\\n[BBOX-304] 16 & *★氯 & Cl & 104.6 & mmol/L & 99.0-110.0 & \\\\\n[BBOX-305] 17 & 总二氧化碳 & TCO2 & 26.9 & mmol/L & 21.0-30.0 & \\\\\n[BBOX-306] 18 & 阴离子隙 & ANION & 7.0 & mmol/L & 8.0-16.0 & $\\downarrow$ \\\\\n[BBOX-307] \\hline\n[BBOX-308] \\end{tabular}\n[BBOX-309] \\begin{tabular}{ccccccc}\n[BBOX-310] 报告时间: 2026-03-04\n[BBOX-311] \\hline\n[BBOX-312] 序号 & 项目名称 & 项目代码 & 结果 & 单位 & 参考区间 & 提示 \\\\\n[BBOX-313] \\hline\n[BBOX-314] 19 & *★钙 & Ca & 2.35 & mmol/L & 2.11-2.52 & \\\\\n[BBOX-315] 20 & *★无机磷 & P & 1.19 & mmol/L & 0.85-1.51 & \\\\\n[BBOX-316] 21 & *镁 & MG & 0.89 & mmol/L & 0.75-1.02 & \\\\\n[BBOX-317] 22 & *★葡萄糖 & GLU & 6.21 & mmol/L & 3.90-6.10 & $\\uparrow$ \\\\\n[BBOX-318] 23 & *★尿素 & UREA & 4.85 & mmol/L & 3.60-9.50 & \\\\\n[BBOX-319] 24 & *★肌酐(酶法) & CREA & 58 & $\\mu$mol/L & 57-111 & \\\\\n[BBOX-320] 25 & 尿素:肌酐 & UREA:CREA & 0.08 & & & \\\\\n[BBOX-321] 26 & 肾小球滤过率 & eGFR (CKD-EPI) & 102.43 & ml/(min$\\cdot$1.73m$^2$) & $\\ge$90 & \\\\\n[BBOX-322] 27 & *★尿酸 & UA & 326 & $\\mu$mol/L & 208-428 & \\\\\n[BBOX-323] 28 & *★肌酸激酶 & CK & 31 & U/L & 50-310 & $\\downarrow$ \\\\\n[BBOX-324] 29 & *★乳酸脱氢酶 & LDH & 226 & U/L & 120-250 & \\\\\n[BBOX-325] 30 & *★总胆固醇 & CHOL & 6.49 & mmol/L & 3.12-5.72 & $\\uparrow$ \\\\\n[BBOX-326] 31 & *★甘油三酯 & TG & 2.23 & mmol/L & 0.40-1.70 & $\\uparrow$ \\\\\n[BBOX-327] 32 & *★高密度脂蛋白胆固醇 & HDL-C & 1.00 & mmol/L & 1.04-1.96 & $\\downarrow$ \\\\\n[BBOX-328] 33 & *★低密度脂蛋白胆固醇 & LDL-C & 3.83 & mmol/L & 1.53-3.45 & $\\uparrow$ \\\\\n[BBOX-329] 34 & 非高密度脂蛋白胆固醇 & non-HDL-C & 5.49 & mmol/L & & \\\\\n[BBOX-330] 35 & *脂蛋白(a) & Lp(a) & 309 & mg/L & 0-300 & $\\uparrow$ \\\\\n[BBOX-331] 36 & 唾液酸 & SA & 695 & mg/L & 456-754 & \\\\\n[BBOX-332] \\hline\n[BBOX-333] \\end{tabular}\n[BBOX-334] \\begin{tabular}{ccccccc}\n[BBOX-335] 报告时间: 2026-03-04\n[BBOX-336] \\hline\n[BBOX-337] 序号 & 项目名称 & 项目代码 & 结果 & 单位 & 参考区间 & 提示 \\\\\n[BBOX-338] \\hline\n[BBOX-339] 37 & 渗透压 & OSM & 277.7 & MoSM/L & & \\\\\n[BBOX-340] 38 & 血同型半胱氨酸 & HCY & 12.4 & $\\mu$mol/L & 0.0-15.0 & \\\\\n[BBOX-341] \\hline\n[BBOX-342] \\end{tabular}\n[BBOX-343] 【检查描述】：心搏次数：97(60~100)bpm，PR间隔：144ms，QRS间隔：88ms，QT间隔：342ms，QTc\n[BBOX-344] 间隔：434ms，P轴：34°，QRS轴：-30°，T轴：15°\n[BBOX-345] 【检查诊断】：窦性心律\n[BBOX-346] QRS电轴左偏\n[BBOX-347] 【检查时间】：2026/2/3 8:21:15\n[BBOX-348] 【报告时间】：2026/2/3 8:22:02\n[BBOX-349] 检查时间\n[BBOX-350] 心率\n[BBOX-351] 2026-02-03 08:19:19\n[BBOX-352] PR\n[BBOX-353] 97 bpm\n[BBOX-354] QRS\n[BBOX-355] 144 ms\n[BBOX-356] QT/QTc\n[BBOX-357] 88 ms\n[BBOX-358] P/QRS/T\n[BBOX-359] 342 / 434 ms\n[BBOX-360] RV5/SV1\n[BBOX-361] 34 / -30 / 15 -\n[BBOX-362] RV5+SV1\n[BBOX-363] 振幅\n[BBOX-364] /\n[BBOX-365] mV\n[BBOX-366] 0.000 mV\n[BBOX-367] AVR\n[BBOX-368] V1\n[BBOX-369] V4\n[BBOX-370] AVL\n[BBOX-371] V2\n[BBOX-372] V5\n[BBOX-373] AVF\n[BBOX-374] V3\n[BBOX-375] V6\n[BBOX-376] 【手术信息】：肿瘤位于直肠上段\n[BBOX-377] 【取材部位】：1:直肠×1\n[BBOX-378] 【取材描述】：#:肿物×1\n[BBOX-379] 1:肿物×1\n[BBOX-380] 2:肿物×1\n[BBOX-381] 3:标记上切缘×2\n[BBOX-382] 4:标记下切缘×1\n[BBOX-383] 5:环周切缘×1\n[BBOX-384] 6:肠周淋巴结×5\n[BBOX-385] 7:肠周淋巴结×5\n[BBOX-386] 8:肠周淋巴结×4\n[BBOX-387] 【大体描述】：直肠肠管一段，长12cm，周径5-7cm，距上切缘8.5cm，下切缘3cm，见一隆起型\n[BBOX-388] 肿物，范围1.4*1cm，高出粘膜面0.6cm，肿物切面灰白质硬，侵达浅肌层。\n[BBOX-389] 【病理所见】：直肠肠管一段，长12cm，周径5-7cm，距上切缘8.5cm，下切缘3cm，见一隆起型\n[BBOX-390] 肿物，范围1.4*1cm，高出粘膜面0.6cm，肿物切面灰白质硬，侵达浅肌层。\n[BBOX-391] 【病理诊断】：（直肠）直肠隆起型中分化腺癌，伴脉管内癌栓，侵及浅肌层，标记上切缘、标记下切缘\n[BBOX-392] 及环周切缘未见癌累及，肠周淋巴结3/18枚见癌转移。\n[BBOX-393] TNM分期：pT2N1bMx。\n[BBOX-394] 免疫组化：MLH1（+），PMS2（+），MSH2（+），MSH6（+），Ki-67+指数约60%。\n[BBOX-395] 【审核医师】：\n[BBOX-396] 【报告时间】：2020/1/17 13:49:00\n[BBOX-397] 【手术信息】：纵隔淋巴结肿大\n[BBOX-398] 【取材部位】：1:EBUS组织×1 2:EBUS刷片×1\n[BBOX-399] 【取材描述】：1:EBUS组织×多\n[BBOX-400] 【大体描述】：灰红碎组织少许，总体积0.4*0.3*0.1cm。\n[BBOX-401] 【病理所见】：灰红碎组织少许，总体积0.4*0.3*0.1cm。\n[BBOX-402] 【病理诊断】：EBUS组织：送检组织内见腺癌，伴大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS\n[BBOX-403] 刷片）查见肿瘤细胞。\n[BBOX-404] 【审核医师】：\n[BBOX-405] 【报告时间】：2025/11/20 11:02:00\n[BBOX-406] 【检查日期】：2026/1/16 8:18:01\n[BBOX-407] 【检查所见】：右肺术后改变，术区可见条索影斑片影，相应支气管截断。双侧胸廓对称，纵隔居中。双\n[BBOX-408] 肺见多发实性结节影，边界清，大者位于右肺下叶（薄层img259），大小约1.2*1.0cm，增强扫描可见不均\n[BBOX-409] 匀强化。双肺见索条状影；双肺背侧胸膜下见条片影。气管支气管通畅，管壁无增厚，无局限性狭窄和扩张\n[BBOX-410] 。纵隔及右肺门区见增大淋巴结影，大者直径约2.4cm，增强扫描可见不均匀强化。心脏大小、形态正常，\n[BBOX-411] 主动脉及冠状动脉管壁见钙化影。右侧胸膜局部略厚，双侧胸腔未见液体密度影。\n[BBOX-412] 【检查诊断】：对比2025-11-28CT：\n[BBOX-413] 1.符合右肺上叶术后改变，术区改变较前相仿，请结合临床复查。\n[BBOX-414] 2.双肺多发结节，部分较前稍饱满、部分新见，考虑转移瘤，建议复查。\n[BBOX-415] 3.纵隔及右肺门增大淋巴结显示，部分较前稍大，考虑转移瘤。\n[BBOX-416] 余所见大致同前。\n[BBOX-417] 【报告医师】：\n[BBOX-418] 【报告时间】：2026/1/16 10:57:25\n[BBOX-419] 【检查日期】：2025/11/18 14:25:00\n[BBOX-420] 【检查所见】：右肺术后改变，术区可见条索影斑片影，相应支气管截断。双侧胸廓对称，纵隔居中。双\n[BBOX-421] 肺见多发实性结节影，边界清，大者位于左肺斜裂处（薄层img168），大小约1.2*0.8cm，增强扫描可见不\n[BBOX-422] 均匀强化。双肺见索条状影；双肺背侧胸膜下见条片影。气管支气管通畅，管壁无增厚，无局限性狭窄和扩\n[BBOX-423] 张。纵隔及右肺门区见增大淋巴结影，大者直径约2.3cm，增强扫描可见不均匀强化。心脏大小、形态正常\n[BBOX-424] ，主动脉及冠状动脉管壁见钙化影。右侧胸膜局部略厚，双侧胸腔未见液体密度影。左侧肾上腺见一\n[BBOX-425] 4.1*2.9cm软组织密度结节，不均匀强化。\n[BBOX-426] 【检查诊断】：对比2025-10-22CT：\n[BBOX-427] 1.符合右肺上叶术后改变，术区改变较前相仿，请结合临床复查。\n[BBOX-428] 2.双肺多发结节，较前相仿，部分考虑转移瘤可能性大，建议密切复查。\n[BBOX-429] 3.纵隔及右肺门增大淋巴结显示，较前相仿，考虑转移瘤。\n[BBOX-430] 4.左侧肾上腺结节，考虑转移瘤，大致同前。\n[BBOX-431] 余所见大致同前。\n[BBOX-432] 2026-02-03 10:41\n[BBOX-433] 主 诉：本次访视为评价注射用HLN601脂质体在晚期实体瘤患者中的安全性、耐受性及药代动力\n[BBOX-434] 学特征和初步疗效的多中心、开放性的I期临床试验项目安全性随访。\n[BBOX-435] 病 史：同前\n[BBOX-436] 审阅受试者日志卡：不适用\n[BBOX-437] 试验用药品/医疗器械使用的依从性：不适用\n[BBOX-438] 合并用药/合并非药物治疗：\n[BBOX-439] (1) 合并用药：\n[BBOX-440] 同前\n[BBOX-441] (2) 合并非药物治疗：\n[BBOX-442] 无\n[BBOX-443] 体格、专科检查以及辅助检查：\n[BBOX-444] (1) 体格、专科检查：\n[BBOX-445] 2026年2月3日 早 8:36 测 生命体征 ：T:36.5℃ P:78次/分 R:19次/分 BP:137/83 mmHg，体\n[BBOX-446] 重：84.7Kg，体格检查同筛选期，ECOG评分1分\n[BBOX-447] (2) 辅助检查：\n[BBOX-448] 血细胞分析（5分类）、生化系列（36项）、D-二聚体、尿分析+沉渣、凝血四项、常规心电图，\n[BBOX-449] 第 1 页\n[BBOX-450] 未见明显异常。\n[BBOX-451] 疗效评估：\n[BBOX-452] 本次访视进行以下疗效评估：不适用\n[BBOX-453] 不良事件：\n[BBOX-454] (1) 既往未转归的不良事件：无\n[BBOX-455] (2) 新发生的不良事件：\n[BBOX-456] 不适用\n[BBOX-457] 其 他：病历更正：2026-01-20门诊病历中“病历更正：2025.12.24住院病历中Bp:142/92mmHg（\n[BBOX-458] CS 与既往病史 高血压（2025.UNK-持续）有关），Bp：143/87mmHg（CS 与既往病史 高血压（\n[BBOX-459] 2025.UNK-持续）有关）更正为（CS 与既往病史 高血压（2005.UNK-持续）有关）” 改为“\n[BBOX-460] 2025.12.25住院病历中Bp:142/92mmHg（CS 与既往病史 高血压（2025.UNK-持续）有关），Bp：\n[BBOX-461] 143/87mmHg（CS 与既往病史 高血压（2025.UNK-持续）有关）更正为（CS 与既往病史 高血压（\n[BBOX-462] 2005.UNK-持续）有关）”时间更正错误，应为：“2025.12.25住院病历中Bp:142/92mmHg（CS 与既往\n[BBOX-463] 病史 高血压（2025.UNK-持续）有关），Bp：143/87mmHg（CS 与既往病史 高血压（2025.UNK-持续）\n[BBOX-464] 有关）更正为（CS 与既往病史 高血压（2005.UNK-持续）有关）” 改为“2025.12.25住院病历中Bp：\n[BBOX-465] 142/92mmHg（CS 与既往病史 高血压（2025.UNK-持续）有关），Bp：143/87mmHg（CS 与既往病史 高\n[BBOX-466] 血压（2025.UNK-持续）有关）更正为（CS 与既往病史 高血压（2005.UNK-持续）有关）\n[BBOX-467] 第 2 页\n[BBOX-468] 门诊诊断:\n[BBOX-469] 肺恶性肿瘤\n[BBOX-470] 诊疗意见:\n[BBOX-471] (1)后续访视:出组,出组原因:疾病进展\n[BBOX-472] (2)发放试验用药品/医疗器械:不适用\n[BBOX-473] (3)其他用药/非药物治疗医嘱:无\n[BBOX-474] (4)其他:无\n[BBOX-475] 第3页"
  }
]
2026-08-10 17:29:51,338 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:29:51.337+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 81, "failed": 0, "current": {"df5ff51c94e011f1bd9827cf206dfa2d": {"id": "df5ff51c94e011f1bd9827cf206dfa2d", "doc_id": "df229e1a94e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 3352826, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786382896642, "task_type": "dataflow", "root_trace_id": "02e835c46e184d6daf27401b2b0ac85a", "root_traceparent": "00-02e835c46e184d6daf27401b2b0ac85a-ddd202d54b80a7dd-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:30:06,467 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:30:06,502 INFO     29 [SmartSplitter] SmartSplitter done: 11 chunks from 11 LLM segments (all bbox_id). Types: {'AdmissionRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 6, 'LabReport': 2, 'OutpatientRecord': 1}
2026-08-10 17:30:06,520 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 17:30:06,520 INFO     29 [Trace] task=df5ff51c | doc=06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "476 items", "markdown": "", "text": "", "name": "06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks": "11 items, types={'AdmissionRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 6, 'LabReport': 2, 'OutpatientRecord': 1}"}
2026-08-10 17:30:06,520 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 17:30:06,521 INFO     29 [ChunkRouter] Routed 11 chunks into 5 groups: {'chunks_Admission': 1, 'chunks_Discharge': 1, 'chunks_Examination': 6, 'chunks_LabExam': 2, 'chunks_Clinical': 1}
2026-08-10 17:30:06,532 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 17:30:06,532 INFO     29 [Trace] task=df5ff51c | doc=06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf | ChunkRouter:Router | outputs={"html": "", "json": "476 items", "markdown": "", "text": "", "name": "06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks": "11 items, types={'AdmissionRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 6, 'LabReport': 2, 'OutpatientRecord': 1}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 2, \"chunks_Clinical\": 1}"}
2026-08-10 17:30:06,533 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 17:30:06,539 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:30:06,540 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:30:06,540 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[5]
2026-08-10 17:30:06,541 INFO     29 [qwen-vl-table] positions ： [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:30:06,778 INFO     29 [qwen-vl-table] page=5, rect=595x842, img=(1654x2339)
2026-08-10 17:30:06,778 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:30:06,778 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 176, \"bbox_end\": 283, \"encounter_dates\": [\"2026-03-04\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "项目名称\n结果\n单位\n参考范围\n项目名称\n结果\n单位\n参考区间\n*★红细胞\n4.20\nx10^12/L\n4.30-5.80\n*★白细胞\n4.59\n×10^9/L\n3.50-9.50\n*★血红蛋白\n145\ng/L\n130-175\n中性粒细胞百分率\n62.1\n%\n40.0-75.0\n*★红细胞压积\n44.0\n%\n40.0-50.0\n淋巴细胞百分率\n24.6\n%\n20.0-50.0\n*平均红细胞体积\n104.8\nfL\n82.0-100.0\n单核细胞百分率\n10.0\n%\n3.0-10.0\n*平均血红蛋白量\n34.5\npg\n27.0-34.0\n嗜酸细胞百分率\n2.4\n%\n0.4-8.0\n*平均血红蛋白浓度\n330\ng/L\n316-354\n嗜碱细胞百分率\n0.9\n%\n0.0-1.0\n红细胞分布宽度SD\n55.1\nf1\n39.0-46.0\n中性粒细胞绝对值\n2.85\n×10^9/L\n1.80-6.30\n红细胞分布宽度CV\n14.2\n%\n10.9-14.5\n淋巴细胞绝对值\n1.13\n×10^9/L\n1.10-3.20\n*★血小板总数\n166\n×10^9/L\n125-350\n单核细胞绝对值\n0.46\n×10^9/L\n0.10-0.60\n血小板平均容积\n10.0\nfL\n7.6-13.2\n嗜酸细胞绝对值\n0.11\n×10^9/L\n0.02-0.52\n血小板分布宽度\n9.7\nf1\n9.0-17.0\n嗜碱细胞绝对值\n0.04\n×10^9/L\n0.00-0.06\n血小板比积\n0.17\n%\n0.11-0.28\n大血小板比例\n23.9\n%\n13.0-43.0\n备注评价：\n平售时间 2026-02-04 08:18\n接收时间：2026-03-04 08:30\n报告时间：2026-03-04 08:41",
    "role": "user"
  }
]
2026-08-10 17:30:19,362 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:30:19,362 INFO     29 [qwen-vl-table] page=5 LLM output (len=4084):
{
  "report_date": "2026-03-04",
  "items": [
    {
      "name": "红细胞",
      "item_code": null,
      "value": "4.20",
      "unit": "x10^12/L",
      "reference_range": "4.30-5.80",
      "abnormal": true
    },
    {
      "name": "白细胞",
      "item_code": null,
      "value": "4.59",
      "unit": "×10^9/L",
      "reference_range": "3.50-9.50",
      "abnormal": false
    },
    {
      "name": "血红蛋白",
      "item_code": null,
      "value": "145",
      "unit": "g/L",
      "reference_range": "130-175",
      "abnormal": false
    },
    {
      "name": "中性粒细胞百分率",
      "item_code": null,
      "value": "62.1",
      "unit": "%",
      "reference_range": "40.0-75.0",
      "abnormal": false
    },
    {
      "name": "红细胞压积",
      "item_code": null,
      "value": "44.0",
      "unit": "%",
      "reference_range": "40.0-50.0",
      "abnormal": false
    },
    {
      "name": "淋巴细胞百分率",
      "item_code": null,
      "value": "24.6",
      "unit": "%",
      "reference_range": "20.0-50.0",
      "abnormal": false
    },
    {
      "name": "平均红细胞体积",
      "item_code": null,
      "value": "104.8",
      "unit": "fL",
      "reference_range": "82.0-100.0",
      "abnormal": true
    },
    {
      "name": "单核细胞百分率",
      "item_code": null,
      "value": "10.0",
      "unit": "%",
      "reference_range": "3.0-10.0",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白量",
      "item_code": null,
      "value": "34.5",
      "unit": "pg",
      "reference_range": "27.0-34.0",
      "abnormal": true
    },
    {
      "name": "嗜酸细胞百分率",
      "item_code": null,
      "value": "2.4",
      "unit": "%",
      "reference_range": "0.4-8.0",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白浓度",
      "item_code": null,
      "value": "330",
      "unit": "g/L",
      "reference_range": "316-354",
      "abnormal": false
    },
    {
      "name": "嗜碱细胞百分率",
      "item_code": null,
      "value": "0.9",
      "unit": "%",
      "reference_range": "0.0-1.0",
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度SD",
      "item_code": null,
      "value": "55.1",
      "unit": "fL",
      "reference_range": "39.0-46.0",
      "abnormal": true
    },
    {
      "name": "中性粒细胞绝对值",
      "item_code": null,
      "value": "2.85",
      "unit": "×10^9/L",
      "reference_range": "1.80-6.30",
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度CV",
      "item_code": null,
      "value": "14.2",
      "unit": "%",
      "reference_range": "10.9-14.5",
      "abnormal": false
    },
    {
      "name": "淋巴细胞绝对值",
      "item_code": null,
      "value": "1.13",
      "unit": "×10^9/L",
      "reference_range": "1.10-3.20",
      "abnormal": false
    },
    {
      "name": "血小板总数",
      "item_code": null,
      "value": "166",
      "unit": "×10^9/L",
      "reference_range": "125-350",
      "abnormal": false
    },
    {
      "name": "单核细胞绝对值",
      "item_code": null,
      "value": "0.46",
      "unit": "×10^9/L",
      "reference_range": "0.10-0.60",
      "abnormal": false
    },
    {
      "name": "血小板平均容积",
      "item_code": null,
      "value": "10.0",
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
      "value": "9.7",
      "unit": "fL",
      "reference_range": "9.0-17.0",
      "abnormal": false
    },
    {
      "name": "嗜碱细胞绝对值",
      "item_code": null,
      "value": "0.04",
      "unit": "×10^9/L",
      "reference_range": "0.00-0.06",
      "abnormal": false
    },
    {
      "name": "血小板比积",
      "item_code": null,
      "value": "0.17",
      "unit": "%",
      "reference_range": "0.11-0.28",
      "abnormal": false
    },
    {
      "name": "大血小板比例",
      "item_code": null,
      "value": "23.9",
      "unit": "%",
      "reference_range": "13.0-43.0",
      "abnormal": false
    }
  ]
}
2026-08-10 17:30:19,362 INFO     29 [qwen-vl-table] coord grouping: {5: 24}
2026-08-10 17:30:19,375 INFO     29 [qwen-vl-table] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3840005, prompt_len=687
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
红细胞、白细胞、血红蛋白、中性粒细胞百分率、红细胞压积、淋巴细胞百分率、平均红细胞体积、单核细胞百分率、平均血红蛋白量、嗜酸细胞百分率、平均血红蛋白浓度、嗜碱细胞百分率、红细胞分布宽度SD、中性粒细胞绝对值、红细胞分布宽度CV、淋巴细胞绝对值、血小板总数、单核细胞绝对值、血小板平均容积、嗜酸细胞绝对值、血小板分布宽度、嗜碱细胞绝对值、血小板比积、大血小板比例

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
2026-08-10 17:30:26,410 INFO     29 [qwen-vl-table] coord API raw response (len=1239):
[
	{"text": "红细胞", "bbox": [190, 592, 250, 602]},
	{"text": "白细胞", "bbox": [509, 592, 564, 602]},
	{"text": "血红蛋白", "bbox": [190, 603, 262, 613]},
	{"text": "中性粒细胞百分率", "bbox": [509, 603, 607, 613]},
	{"text": "红细胞压积", "bbox": [190, 614, 274, 624]},
	{"text": "淋巴细胞百分率", "bbox": [509, 614, 595, 624]},
	{"text": "平均红细胞体积", "bbox": [190, 625, 287, 635]},
	{"text": "单核细胞百分率", "bbox": [509, 625, 595, 635]},
	{"text": "平均血红蛋白量", "bbox": [190, 636, 287, 646]},
	{"text": "嗜酸细胞百分率", "bbox": [509, 636, 595, 646]},
	{"text": "平均血红蛋白浓度", "bbox": [190, 647, 298, 657]},
	{"text": "嗜碱细胞百分率", "bbox": [509, 647, 595, 657]},
	{"text": "红细胞分布宽度SD", "bbox": [190, 658, 293, 668]},
	{"text": "中性粒细胞绝对值", "bbox": [509, 658, 607, 668]},
	{"text": "红细胞分布宽度CV", "bbox": [190, 670, 292, 680]},
	{"text": "淋巴细胞绝对值", "bbox": [509, 670, 595, 680]},
	{"text": "血小板总数", "bbox": [190, 681, 272, 691]},
	{"text": "单核细胞绝对值", "bbox": [509, 681, 595, 691]},
	{"text": "血小板平均容积", "bbox": [190, 692, 277, 702]},
	{"text": "嗜酸细胞绝对值", "bbox": [509, 692, 595, 702]},
	{"text": "血小板分布宽度", "bbox": [190, 704, 277, 714]},
	{"text": "嗜碱细胞绝对值", "bbox": [509, 704, 595, 714]},
	{"text": "血小板比积", "bbox": [190, 715, 251, 725]},
	{"text": "大血小板比例", "bbox": [190, 727, 263, 737]}
]
2026-08-10 17:30:26,411 INFO     29 [qwen-vl-table] coord API: raw_items=24, valid_items=24, elapsed=7.0s
2026-08-10 17:30:26,411 INFO     29 [qwen-vl-table] coord item[0]: text=红细胞, bbox=[190, 592, 250, 602]
2026-08-10 17:30:26,411 INFO     29 [qwen-vl-table] coord item[1]: text=白细胞, bbox=[509, 592, 564, 602]
2026-08-10 17:30:26,412 INFO     29 [qwen-vl-table] coord item[2]: text=血红蛋白, bbox=[190, 603, 262, 613]
2026-08-10 17:30:26,412 INFO     29 [qwen-vl-table] coord item[3]: text=中性粒细胞百分率, bbox=[509, 603, 607, 613]
2026-08-10 17:30:26,412 INFO     29 [qwen-vl-table] coord item[4]: text=红细胞压积, bbox=[190, 614, 274, 624]
2026-08-10 17:30:26,412 INFO     29 [qwen-vl-table] coord item[5]: text=淋巴细胞百分率, bbox=[509, 614, 595, 624]
2026-08-10 17:30:26,412 INFO     29 [qwen-vl-table] coord item[6]: text=平均红细胞体积, bbox=[190, 625, 287, 635]
2026-08-10 17:30:26,412 INFO     29 [qwen-vl-table] coord item[7]: text=单核细胞百分率, bbox=[509, 625, 595, 635]
2026-08-10 17:30:26,412 INFO     29 [qwen-vl-table] coord item[8]: text=平均血红蛋白量, bbox=[190, 636, 287, 646]
2026-08-10 17:30:26,412 INFO     29 [qwen-vl-table] coord item[9]: text=嗜酸细胞百分率, bbox=[509, 636, 595, 646]
2026-08-10 17:30:26,412 INFO     29 [qwen-vl-table] coord item[10]: text=平均血红蛋白浓度, bbox=[190, 647, 298, 657]
2026-08-10 17:30:26,412 INFO     29 [qwen-vl-table] coord item[11]: text=嗜碱细胞百分率, bbox=[509, 647, 595, 657]
2026-08-10 17:30:26,412 INFO     29 [qwen-vl-table] coord item[12]: text=红细胞分布宽度SD, bbox=[190, 658, 293, 668]
2026-08-10 17:30:26,412 INFO     29 [qwen-vl-table] coord item[13]: text=中性粒细胞绝对值, bbox=[509, 658, 607, 668]
2026-08-10 17:30:26,412 INFO     29 [qwen-vl-table] coord item[14]: text=红细胞分布宽度CV, bbox=[190, 670, 292, 680]
2026-08-10 17:30:26,412 INFO     29 [qwen-vl-table] coord item[15]: text=淋巴细胞绝对值, bbox=[509, 670, 595, 680]
2026-08-10 17:30:26,413 INFO     29 [qwen-vl-table] coord item[16]: text=血小板总数, bbox=[190, 681, 272, 691]
2026-08-10 17:30:26,413 INFO     29 [qwen-vl-table] coord item[17]: text=单核细胞绝对值, bbox=[509, 681, 595, 691]
2026-08-10 17:30:26,413 INFO     29 [qwen-vl-table] coord item[18]: text=血小板平均容积, bbox=[190, 692, 277, 702]
2026-08-10 17:30:26,413 INFO     29 [qwen-vl-table] coord item[19]: text=嗜酸细胞绝对值, bbox=[509, 692, 595, 702]
2026-08-10 17:30:26,413 INFO     29 [qwen-vl-table] coord item[20]: text=血小板分布宽度, bbox=[190, 704, 277, 714]
2026-08-10 17:30:26,413 INFO     29 [qwen-vl-table] coord item[21]: text=嗜碱细胞绝对值, bbox=[509, 704, 595, 714]
2026-08-10 17:30:26,413 INFO     29 [qwen-vl-table] coord item[22]: text=血小板比积, bbox=[190, 715, 251, 725]
2026-08-10 17:30:26,413 INFO     29 [qwen-vl-table] coord item[23]: text=大血小板比例, bbox=[190, 727, 263, 737]
2026-08-10 17:30:26,415 INFO     29 [qwen-vl-table] page=5 coord: matched 24/24, time=7.0s
2026-08-10 17:30:26,415 INFO     29 [qwen-vl-table] new_positions (24):
[[6, 113.10699768066407, 148.8249969482422, 498.404814453125, 506.8238146972656], [6, 303.00769378662113, 335.7491931152344, 498.404814453125, 506.8238146972656], [6, 113.10699768066407, 155.96859680175783, 507.6657147216797, 516.0847149658204], [6, 303.00769378662113, 361.34709259033207, 507.6657147216797, 516.0847149658204], [6, 113.10699768066407, 163.11219665527344, 516.9266149902344, 525.345615234375], [6, 303.00769378662113, 354.20349273681643, 516.9266149902344, 525.345615234375], [6, 113.10699768066407, 170.85109649658204, 526.1875152587891, 534.6065155029297], [6, 303.00769378662113, 354.20349273681643, 526.1875152587891, 534.6065155029297], [6, 113.10699768066407, 170.85109649658204, 535.4484155273437, 543.8674157714844], [6, 303.00769378662113, 354.20349273681643, 535.4484155273437, 543.8674157714844], [6, 113.10699768066407, 177.39939636230469, 544.7093157958984, 553.1283160400391], [6, 303.00769378662113, 354.20349273681643, 544.7093157958984, 553.1283160400391], [6, 113.10699768066407, 174.42289642333986, 553.9702160644531, 562.3892163085937], [6, 303.00769378662113, 361.34709259033207, 553.9702160644531, 562.3892163085937], [6, 113.10699768066407, 173.8275964355469, 564.0730163574219, 572.4920166015626], [6, 303.00769378662113, 354.20349273681643, 564.0730163574219, 572.4920166015626], [6, 113.10699768066407, 161.9215966796875, 573.3339166259766, 581.7529168701172], [6, 303.00769378662113, 354.20349273681643, 573.3339166259766, 581.7529168701172], [6, 113.10699768066407, 164.89809661865235, 582.5948168945313, 591.0138171386719], [6, 303.00769378662113, 354.20349273681643, 582.5948168945313, 591.0138171386719], [6, 113.10699768066407, 164.89809661865235, 592.6976171875, 601.1166174316406], [6, 303.00769378662113, 354.20349273681643, 592.6976171875, 601.1166174316406], [6, 113.10699768066407, 149.42029693603516, 601.9585174560547, 610.3775177001953], [6, 113.10699768066407, 156.5638967895508, 612.0613177490235, 620.4803179931641]]
2026-08-10 17:30:26,416 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=24, matched=24, pages=1, time=19.9s
2026-08-10 17:30:26,417 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:30:26,418 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:30:26,418 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[6]
2026-08-10 17:30:26,418 INFO     29 [qwen-vl-table] positions ： [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:30:26,707 INFO     29 [qwen-vl-table] page=6, rect=595x842, img=(1654x2339)
2026-08-10 17:30:26,708 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:30:26,708 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 284, \"bbox_end\": 342, \"encounter_dates\": [\"2026-03-04\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccc}\n报告时间: 2026-03-04\n\\hline\n序号 & 项目名称 & 项目代码 & 结果 & 单位 & 参考区间 & 提示 \\\\\n\\hline\n1 & *★总蛋白 & TP & 75.96 & g/L & 65.00-85.00 & \\\\\n2 & *★白蛋白(溴甲酚绿法) & ALB & 44.42 & g/L & 40.00-55.00 & \\\\\n3 & 球蛋白 & GLO & 31.54 & g/L & 20.00-40.00 & \\\\\n4 & 白蛋白:球蛋白 & A:G & 1.41 & & 1.20-2.40 & \\\\\n5 & *总胆红素 & TBIL & 14.4 & $\\mu$mol/L & $\\le$26.0 & \\\\\n6 & *直接胆红素 & DBIL & 2.0 & $\\mu$mol/L & 0.0-6.8 & \\\\\n7 & 间接胆红素 & IBIL & 12.4 & $\\mu$mol/L & 3.0-19.0 & \\\\\n8 & *★$\\gamma$-谷氨酰基转移酶 & GGT & 49 & U/L & 10-60 & \\\\\n9 & *★碱性磷酸酶 & ALP & 61 & U/L & 45-125 & \\\\\n10 & *★天门冬氨酸氨基转移酶 & AST & 16 & U/L & 15-40 & \\\\\n11 & *★丙氨酸氨基转移酶 & ALT & 6 & U/L & 9-50 & $\\downarrow$ \\\\\n12 & AST:ALT & AST:ALT & 2.67 & & & \\\\\n13 & 总胆汁酸 & TBA & 4.1 & $\\mu$mol/L & 0.0-14.0 & \\\\\n14 & *★钾 & K & 4.67 & mmol/L & 3.50-5.30 & \\\\\n15 & *★钠 & Na & 138.5 & mmol/L & 137.0-147.0 & \\\\\n16 & *★氯 & Cl & 104.6 & mmol/L & 99.0-110.0 & \\\\\n17 & 总二氧化碳 & TCO2 & 26.9 & mmol/L & 21.0-30.0 & \\\\\n18 & 阴离子隙 & ANION & 7.0 & mmol/L & 8.0-16.0 & $\\downarrow$ \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{ccccccc}\n报告时间: 2026-03-04\n\\hline\n序号 & 项目名称 & 项目代码 & 结果 & 单位 & 参考区间 & 提示 \\\\\n\\hline\n19 & *★钙 & Ca & 2.35 & mmol/L & 2.11-2.52 & \\\\\n20 & *★无机磷 & P & 1.19 & mmol/L & 0.85-1.51 & \\\\\n21 & *镁 & MG & 0.89 & mmol/L & 0.75-1.02 & \\\\\n22 & *★葡萄糖 & GLU & 6.21 & mmol/L & 3.90-6.10 & $\\uparrow$ \\\\\n23 & *★尿素 & UREA & 4.85 & mmol/L & 3.60-9.50 & \\\\\n24 & *★肌酐(酶法) & CREA & 58 & $\\mu$mol/L & 57-111 & \\\\\n25 & 尿素:肌酐 & UREA:CREA & 0.08 & & & \\\\\n26 & 肾小球滤过率 & eGFR (CKD-EPI) & 102.43 & ml/(min$\\cdot$1.73m$^2$) & $\\ge$90 & \\\\\n27 & *★尿酸 & UA & 326 & $\\mu$mol/L & 208-428 & \\\\\n28 & *★肌酸激酶 & CK & 31 & U/L & 50-310 & $\\downarrow$ \\\\\n29 & *★乳酸脱氢酶 & LDH & 226 & U/L & 120-250 & \\\\\n30 & *★总胆固醇 & CHOL & 6.49 & mmol/L & 3.12-5.72 & $\\uparrow$ \\\\\n31 & *★甘油三酯 & TG & 2.23 & mmol/L & 0.40-1.70 & $\\uparrow$ \\\\\n32 & *★高密度脂蛋白胆固醇 & HDL-C & 1.00 & mmol/L & 1.04-1.96 & $\\downarrow$ \\\\\n33 & *★低密度脂蛋白胆固醇 & LDL-C & 3.83 & mmol/L & 1.53-3.45 & $\\uparrow$ \\\\\n34 & 非高密度脂蛋白胆固醇 & non-HDL-C & 5.49 & mmol/L & & \\\\\n35 & *脂蛋白(a) & Lp(a) & 309 & mg/L & 0-300 & $\\uparrow$ \\\\\n36 & 唾液酸 & SA & 695 & mg/L & 456-754 & \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{ccccccc}\n报告时间: 2026-03-04\n\\hline\n序号 & 项目名称 & 项目代码 & 结果 & 单位 & 参考区间 & 提示 \\\\\n\\hline\n37 & 渗透压 & OSM & 277.7 & MoSM/L & & \\\\\n38 & 血同型半胱氨酸 & HCY & 12.4 & $\\mu$mol/L & 0.0-15.0 & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 17:30:26,711 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:30:26.711+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 81, "failed": 0, "current": {"df5ff51c94e011f1bd9827cf206dfa2d": {"id": "df5ff51c94e011f1bd9827cf206dfa2d", "doc_id": "df229e1a94e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 3352826, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786382896642, "task_type": "dataflow", "root_trace_id": "02e835c46e184d6daf27401b2b0ac85a", "root_traceparent": "00-02e835c46e184d6daf27401b2b0ac85a-ddd202d54b80a7dd-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:30:49,871 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:30:49,872 INFO     29 [qwen-vl-table] page=6 LLM output (len=6451):
{
  "report_date": "2026-03-04",
  "items": [
    {
      "name": "总蛋白",
      "item_code": "TP",
      "value": "75.96",
      "unit": "g/L",
      "reference_range": "65.00-85.00",
      "abnormal": false
    },
    {
      "name": "白蛋白(溴甲酚绿法)",
      "item_code": "ALB",
      "value": "44.42",
      "unit": "g/L",
      "reference_range": "40.00-55.00",
      "abnormal": false
    },
    {
      "name": "球蛋白",
      "item_code": "GLO",
      "value": "31.54",
      "unit": "g/L",
      "reference_range": "20.00-40.00",
      "abnormal": false
    },
    {
      "name": "白蛋白:球蛋白",
      "item_code": "A:G",
      "value": "1.41",
      "unit": null,
      "reference_range": "1.20-2.40",
      "abnormal": false
    },
    {
      "name": "总胆红素",
      "item_code": "TBIL",
      "value": "14.4",
      "unit": "μmol/L",
      "reference_range": "≤26.0",
      "abnormal": false
    },
    {
      "name": "直接胆红素",
      "item_code": "DBIL",
      "value": "2.0",
      "unit": "μmol/L",
      "reference_range": "0.0-6.8",
      "abnormal": false
    },
    {
      "name": "间接胆红素",
      "item_code": "IBIL",
      "value": "12.4",
      "unit": "μmol/L",
      "reference_range": "3.0-19.0",
      "abnormal": false
    },
    {
      "name": "γ-谷氨酰基转移酶",
      "item_code": "GGT",
      "value": "49",
      "unit": "U/L",
      "reference_range": "10-60",
      "abnormal": false
    },
    {
      "name": "碱性磷酸酶",
      "item_code": "ALP",
      "value": "61",
      "unit": "U/L",
      "reference_range": "45-125",
      "abnormal": false
    },
    {
      "name": "天门冬氨酸氨基转移酶",
      "item_code": "AST",
      "value": "16",
      "unit": "U/L",
      "reference_range": "15-40",
      "abnormal": false
    },
    {
      "name": "丙氨酸氨基转移酶",
      "item_code": "ALT",
      "value": "6",
      "unit": "U/L",
      "reference_range": "9-50",
      "abnormal": true
    },
    {
      "name": "AST:ALT",
      "item_code": "AST:ALT",
      "value": "2.67",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "总胆汁酸",
      "item_code": "TBA",
      "value": "4.1",
      "unit": "μmol/L",
      "reference_range": "0.0-14.0",
      "abnormal": false
    },
    {
      "name": "钾",
      "item_code": "K",
      "value": "4.67",
      "unit": "mmol/L",
      "reference_range": "3.50-5.30",
      "abnormal": false
    },
    {
      "name": "钠",
      "item_code": "Na",
      "value": "138.5",
      "unit": "mmol/L",
      "reference_range": "137.0-147.0",
      "abnormal": false
    },
    {
      "name": "氯",
      "item_code": "Cl",
      "value": "104.6",
      "unit": "mmol/L",
      "reference_range": "99.0-110.0",
      "abnormal": false
    },
    {
      "name": "总二氧化碳",
      "item_code": "TCO2",
      "value": "26.9",
      "unit": "mmol/L",
      "reference_range": "21.0-30.0",
      "abnormal": false
    },
    {
      "name": "阴离子隙",
      "item_code": "ANION",
      "value": "7.0",
      "unit": "mmol/L",
      "reference_range": "8.0-16.0",
      "abnormal": true
    },
    {
      "name": "钙",
      "item_code": "Ca",
      "value": "2.35",
      "unit": "mmol/L",
      "reference_range": "2.11-2.52",
      "abnormal": false
    },
    {
      "name": "无机磷",
      "item_code": "P",
      "value": "1.19",
      "unit": "mmol/L",
      "reference_range": "0.85-1.51",
      "abnormal": false
    },
    {
      "name": "镁",
      "item_code": "MG",
      "value": "0.89",
      "unit": "mmol/L",
      "reference_range": "0.75-1.02",
      "abnormal": false
    },
    {
      "name": "葡萄糖",
      "item_code": "GLU",
      "value": "6.21",
      "unit": "mmol/L",
      "reference_range": "3.90-6.10",
      "abnormal": true
    },
    {
      "name": "尿素",
      "item_code": "UREA",
      "value": "4.85",
      "unit": "mmol/L",
      "reference_range": "3.60-9.50",
      "abnormal": false
    },
    {
      "name": "肌酐(酶法)",
      "item_code": "CREA",
      "value": "58",
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
      "item_code": "eGFR (CKD-EPI)",
      "value": "102.43",
      "unit": "ml/(min·1.73m^2)",
      "reference_range": "≥90",
      "abnormal": false
    },
    {
      "name": "尿酸",
      "item_code": "UA",
      "value": "326",
      "unit": "μmol/L",
      "reference_range": "208-428",
      "abnormal": false
    },
    {
      "name": "肌酸激酶",
      "item_code": "CK",
      "value": "31",
      "unit": "U/L",
      "reference_range": "50-310",
      "abnormal": true
    },
    {
      "name": "乳酸脱氢酶",
      "item_code": "LDH",
      "value": "226",
      "unit": "U/L",
      "reference_range": "120-250",
      "abnormal": false
    },
    {
      "name": "总胆固醇",
      "item_code": "CHOL",
      "value": "6.49",
      "unit": "mmol/L",
      "reference_range": "3.12-5.72",
      "abnormal": true
    },
    {
      "name": "甘油三酯",
      "item_code": "TG",
      "value": "2.23",
      "unit": "mmol/L",
      "reference_range": "0.40-1.70",
      "abnormal": true
    },
    {
      "name": "高密度脂蛋白胆固醇",
      "item_code": "HDL-C",
      "value": "1.00",
      "unit": "mmol/L",
      "reference_range": "1.04-1.96",
      "abnormal": true
    },
    {
      "name": "低密度脂蛋白胆固醇",
      "item_code": "LDL-C",
      "value": "3.83",
      "unit": "mmol/L",
      "reference_range": "1.53-3.45",
      "abnormal": true
    },
    {
      "name": "非高密度脂蛋白胆固醇",
      "item_code": "non-HDL-C",
      "value": "5.49",
      "unit": "mmol/L",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "脂蛋白(a)",
      "item_code": "Lp(a)",
      "value": "309",
      "unit": "mg/L",
      "reference_range": "0-300",
      "abnormal": true
    },
    {
      "name": "唾液酸",
      "item_code": "SA",
      "value": "695",
      "unit": "mg/L",
      "reference_range": "456-754",
      "abnormal": false
    },
    {
      "name": "渗透压",
      "item_code": "OSM",
      "value": "277.7",
      "unit": "MoSM/L",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "血同型半胱氨酸",
      "item_code": "HCY",
      "value": "12.4",
      "unit": "μmol/L",
      "reference_range": "0.0-15.0",
      "abnormal": false
    }
  ]
}
2026-08-10 17:30:49,872 INFO     29 [qwen-vl-table] coord grouping: {6: 38}
2026-08-10 17:30:49,875 INFO     29 [qwen-vl-table] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2136955, prompt_len=729
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
2026-08-10 17:30:59,899 INFO     29 [qwen-vl-table] coord API raw response (len=1897):
[
	{"text": "总蛋白", "bbox": [208, 106, 261, 115]},
	{"text": "白蛋白(溴甲酚绿法)", "bbox": [208, 117, 329, 126]},
	{"text": "球蛋白", "bbox": [208, 128, 243, 137]},
	{"text": "白蛋白:球蛋白", "bbox": [208, 139, 283, 148]},
	{"text": "总胆红素", "bbox": [208, 150, 261, 159]},
	{"text": "直接胆红素", "bbox": [208, 161, 271, 170]},
	{"text": "间接胆红素", "bbox": [208, 172, 265, 181]},
	{"text": "γ-谷氨酰基转移酶", "bbox": [208, 183, 325, 192]},
	{"text": "碱性磷酸酶", "bbox": [208, 194, 284, 203]},
	{"text": "天门冬氨酸氨基转移酶", "bbox": [208, 205, 343, 214]},
	{"text": "丙氨酸氨基转移酶", "bbox": [208, 216, 320, 225]},
	{"text": "AST:ALT", "bbox": [208, 227, 251, 236]},
	{"text": "总胆汁酸", "bbox": [208, 238, 255, 247]},
	{"text": "钾", "bbox": [208, 249, 238, 258]},
	{"text": "钠", "bbox": [208, 260, 238, 269]},
	{"text": "氯", "bbox": [208, 271, 238, 280]},
	{"text": "总二氧化碳", "bbox": [208, 282, 267, 291]},
	{"text": "阴离子隙", "bbox": [208, 293, 255, 302]},
	{"text": "钙", "bbox": [224, 369, 252, 378]},
	{"text": "无机磷", "bbox": [224, 380, 273, 389]},
	{"text": "镁", "bbox": [224, 391, 242, 400]},
	{"text": "葡萄糖", "bbox": [224, 402, 273, 411]},
	{"text": "尿素", "bbox": [224, 413, 261, 422]},
	{"text": "肌酐(酶法)", "bbox": [224, 423, 293, 432]},
	{"text": "尿素:肌酐", "bbox": [224, 434, 273, 443]},
	{"text": "肾小球滤过率", "bbox": [224, 444, 289, 453]},
	{"text": "尿酸", "bbox": [224, 455, 261, 464]},
	{"text": "肌酸激酶", "bbox": [224, 466, 283, 475]},
	{"text": "乳酸脱氢酶", "bbox": [224, 476, 293, 485]},
	{"text": "总胆固醇", "bbox": [224, 487, 283, 496]},
	{"text": "甘油三酯", "bbox": [224, 497, 283, 506]},
	{"text": "高密度脂蛋白胆固醇", "bbox": [224, 508, 338, 517]},
	{"text": "低密度脂蛋白胆固醇", "bbox": [224, 519, 338, 528]},
	{"text": "非高密度脂蛋白胆固醇", "bbox": [224, 529, 332, 538]},
	{"text": "脂蛋白(a)", "bbox": [224, 539, 273, 548]},
	{"text": "唾液酸", "bbox": [224, 549, 254, 558]},
	{"text": "渗透压", "bbox": [208, 628, 241, 637]},
	{"text": "血同型半胱氨酸", "bbox": [208, 639, 285, 648]}
]
2026-08-10 17:30:59,899 INFO     29 [qwen-vl-table] coord API: raw_items=38, valid_items=38, elapsed=10.0s
2026-08-10 17:30:59,899 INFO     29 [qwen-vl-table] coord item[0]: text=总蛋白, bbox=[208, 106, 261, 115]
2026-08-10 17:30:59,899 INFO     29 [qwen-vl-table] coord item[1]: text=白蛋白(溴甲酚绿法), bbox=[208, 117, 329, 126]
2026-08-10 17:30:59,899 INFO     29 [qwen-vl-table] coord item[2]: text=球蛋白, bbox=[208, 128, 243, 137]
2026-08-10 17:30:59,899 INFO     29 [qwen-vl-table] coord item[3]: text=白蛋白:球蛋白, bbox=[208, 139, 283, 148]
2026-08-10 17:30:59,899 INFO     29 [qwen-vl-table] coord item[4]: text=总胆红素, bbox=[208, 150, 261, 159]
2026-08-10 17:30:59,900 INFO     29 [qwen-vl-table] coord item[5]: text=直接胆红素, bbox=[208, 161, 271, 170]
2026-08-10 17:30:59,900 INFO     29 [qwen-vl-table] coord item[6]: text=间接胆红素, bbox=[208, 172, 265, 181]
2026-08-10 17:30:59,900 INFO     29 [qwen-vl-table] coord item[7]: text=γ-谷氨酰基转移酶, bbox=[208, 183, 325, 192]
2026-08-10 17:30:59,900 INFO     29 [qwen-vl-table] coord item[8]: text=碱性磷酸酶, bbox=[208, 194, 284, 203]
2026-08-10 17:30:59,900 INFO     29 [qwen-vl-table] coord item[9]: text=天门冬氨酸氨基转移酶, bbox=[208, 205, 343, 214]
2026-08-10 17:30:59,900 INFO     29 [qwen-vl-table] coord item[10]: text=丙氨酸氨基转移酶, bbox=[208, 216, 320, 225]
2026-08-10 17:30:59,900 INFO     29 [qwen-vl-table] coord item[11]: text=AST:ALT, bbox=[208, 227, 251, 236]
2026-08-10 17:30:59,900 INFO     29 [qwen-vl-table] coord item[12]: text=总胆汁酸, bbox=[208, 238, 255, 247]
2026-08-10 17:30:59,900 INFO     29 [qwen-vl-table] coord item[13]: text=钾, bbox=[208, 249, 238, 258]
2026-08-10 17:30:59,900 INFO     29 [qwen-vl-table] coord item[14]: text=钠, bbox=[208, 260, 238, 269]
2026-08-10 17:30:59,900 INFO     29 [qwen-vl-table] coord item[15]: text=氯, bbox=[208, 271, 238, 280]
2026-08-10 17:30:59,900 INFO     29 [qwen-vl-table] coord item[16]: text=总二氧化碳, bbox=[208, 282, 267, 291]
2026-08-10 17:30:59,900 INFO     29 [qwen-vl-table] coord item[17]: text=阴离子隙, bbox=[208, 293, 255, 302]
2026-08-10 17:30:59,900 INFO     29 [qwen-vl-table] coord item[18]: text=钙, bbox=[224, 369, 252, 378]
2026-08-10 17:30:59,900 INFO     29 [qwen-vl-table] coord item[19]: text=无机磷, bbox=[224, 380, 273, 389]
2026-08-10 17:30:59,900 INFO     29 [qwen-vl-table] coord item[20]: text=镁, bbox=[224, 391, 242, 400]
2026-08-10 17:30:59,901 INFO     29 [qwen-vl-table] coord item[21]: text=葡萄糖, bbox=[224, 402, 273, 411]
2026-08-10 17:30:59,901 INFO     29 [qwen-vl-table] coord item[22]: text=尿素, bbox=[224, 413, 261, 422]
2026-08-10 17:30:59,901 INFO     29 [qwen-vl-table] coord item[23]: text=肌酐(酶法), bbox=[224, 423, 293, 432]
2026-08-10 17:30:59,901 INFO     29 [qwen-vl-table] coord item[24]: text=尿素:肌酐, bbox=[224, 434, 273, 443]
2026-08-10 17:30:59,901 INFO     29 [qwen-vl-table] coord item[25]: text=肾小球滤过率, bbox=[224, 444, 289, 453]
2026-08-10 17:30:59,901 INFO     29 [qwen-vl-table] coord item[26]: text=尿酸, bbox=[224, 455, 261, 464]
2026-08-10 17:30:59,901 INFO     29 [qwen-vl-table] coord item[27]: text=肌酸激酶, bbox=[224, 466, 283, 475]
2026-08-10 17:30:59,901 INFO     29 [qwen-vl-table] coord item[28]: text=乳酸脱氢酶, bbox=[224, 476, 293, 485]
2026-08-10 17:30:59,901 INFO     29 [qwen-vl-table] coord item[29]: text=总胆固醇, bbox=[224, 487, 283, 496]
2026-08-10 17:30:59,901 INFO     29 [qwen-vl-table] coord item[30]: text=甘油三酯, bbox=[224, 497, 283, 506]
2026-08-10 17:30:59,901 INFO     29 [qwen-vl-table] coord item[31]: text=高密度脂蛋白胆固醇, bbox=[224, 508, 338, 517]
2026-08-10 17:30:59,901 INFO     29 [qwen-vl-table] coord item[32]: text=低密度脂蛋白胆固醇, bbox=[224, 519, 338, 528]
2026-08-10 17:30:59,901 INFO     29 [qwen-vl-table] coord item[33]: text=非高密度脂蛋白胆固醇, bbox=[224, 529, 332, 538]
2026-08-10 17:30:59,901 INFO     29 [qwen-vl-table] coord item[34]: text=脂蛋白(a), bbox=[224, 539, 273, 548]
2026-08-10 17:30:59,901 INFO     29 [qwen-vl-table] coord item[35]: text=唾液酸, bbox=[224, 549, 254, 558]
2026-08-10 17:30:59,901 INFO     29 [qwen-vl-table] coord item[36]: text=渗透压, bbox=[208, 628, 241, 637]
2026-08-10 17:30:59,901 INFO     29 [qwen-vl-table] coord item[37]: text=血同型半胱氨酸, bbox=[208, 639, 285, 648]
2026-08-10 17:30:59,902 INFO     29 [qwen-vl-table] page=6 coord: matched 38/38, time=10.0s
2026-08-10 17:30:59,903 INFO     29 [qwen-vl-table] new_positions (38):
[[7, 123.82239746093751, 155.37329681396486, 89.24140258789063, 96.8185028076172], [7, 123.82239746093751, 195.85369598388672, 98.50230285644531, 106.07940307617189], [7, 123.82239746093751, 144.65789703369143, 107.763203125, 115.34030334472656], [7, 123.82239746093751, 168.46989654541017, 117.0241033935547, 124.60120361328126], [7, 123.82239746093751, 155.37329681396486, 126.28500366210938, 133.86210388183594], [7, 123.82239746093751, 161.32629669189453, 135.54590393066405, 143.12300415039064], [7, 123.82239746093751, 157.75449676513674, 144.80680419921876, 152.38390441894532], [7, 123.82239746093751, 193.47249603271484, 154.06770446777344, 161.6448046875], [7, 123.82239746093751, 169.06519653320314, 163.32860473632812, 170.9057049560547], [7, 123.82239746093751, 204.1878958129883, 172.58950500488282, 180.16660522460938], [7, 123.82239746093751, 190.49599609375002, 181.8504052734375, 189.42750549316406], [7, 123.82239746093751, 149.42029693603516, 191.11130554199218, 198.68840576171877], [7, 123.82239746093751, 151.80149688720704, 200.3722058105469, 207.94930603027345], [7, 123.82239746093751, 141.68139709472658, 209.63310607910157, 217.21020629882813], [7, 123.82239746093751, 141.68139709472658, 218.89400634765624, 226.47110656738283], [7, 123.82239746093751, 141.68139709472658, 228.15490661621095, 235.7320068359375], [7, 123.82239746093751, 158.94509674072268, 237.41580688476563, 244.9929071044922], [7, 123.82239746093751, 151.80149688720704, 246.6767071533203, 254.2538073730469], [7, 133.347197265625, 150.01559692382813, 310.6611090087891, 318.23820922851564], [7, 133.347197265625, 162.51689666748047, 319.92200927734376, 327.4991094970703], [7, 133.347197265625, 144.06259704589846, 329.18290954589844, 336.760009765625], [7, 133.347197265625, 162.51689666748047, 338.4438098144531, 346.0209100341797], [7, 133.347197265625, 155.37329681396486, 347.70471008300785, 355.2818103027344], [7, 133.347197265625, 174.42289642333986, 356.12371032714844, 363.700810546875], [7, 133.347197265625, 162.51689666748047, 365.3846105957031, 372.9617108154297], [7, 133.347197265625, 172.04169647216798, 373.80361083984377, 381.38071105957033], [7, 133.347197265625, 155.37329681396486, 383.06451110839845, 390.641611328125], [7, 133.347197265625, 168.46989654541017, 392.3254113769531, 399.9025115966797], [7, 133.347197265625, 174.42289642333986, 400.7444116210938, 408.32151184082034], [7, 133.347197265625, 168.46989654541017, 410.00531188964845, 417.582412109375], [7, 133.347197265625, 168.46989654541017, 418.4243121337891, 426.00141235351566], [7, 133.347197265625, 201.21139587402345, 427.6852124023438, 435.26231262207034], [7, 133.347197265625, 201.21139587402345, 436.94611267089846, 444.523212890625], [7, 133.347197265625, 197.63959594726563, 445.3651129150391, 452.94221313476567], [7, 133.347197265625, 162.51689666748047, 453.7841131591797, 461.36121337890626], [7, 133.347197265625, 151.20619689941407, 462.20311340332034, 469.7802136230469], [7, 123.82239746093751, 143.4672970581055, 528.7132153320313, 536.2903155517579], [7, 123.82239746093751, 169.6604965209961, 537.974115600586, 545.5512158203126]]
2026-08-10 17:30:59,903 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=38, matched=38, pages=1, time=33.5s
2026-08-10 17:30:59,917 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 17:30:59,917 INFO     29 [Trace] task=df5ff51c | doc=06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf | Extractor:LabExam | outputs={"chunks": "2 items, types={'LabReport': 2}", "html": "", "json": "476 items", "markdown": "", "text": "", "name": "06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 2, \"chunks_Clinical\": 1}"}
2026-08-10 17:30:59,917 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 17:30:59,918 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:30:59.917+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 81, "failed": 0, "current": {"df5ff51c94e011f1bd9827cf206dfa2d": {"id": "df5ff51c94e011f1bd9827cf206dfa2d", "doc_id": "df229e1a94e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 3352826, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786382896642, "task_type": "dataflow", "root_trace_id": "02e835c46e184d6daf27401b2b0ac85a", "root_traceparent": "00-02e835c46e184d6daf27401b2b0ac85a-ddd202d54b80a7dd-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:30:59,927 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:30:59,927 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 17:31:01,140 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:31:01,151 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 17:31:01,152 INFO     29 [Trace] task=df5ff51c | doc=06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "476 items", "markdown": "", "text": "", "name": "06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 2, \"chunks_Clinical\": 1}"}
2026-08-10 17:31:01,152 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 17:31:01,165 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:31:01,166 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:31:01,166 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 17:31:01,166 INFO     29 [qwen-vl-text] positions(44): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:31:01,167 INFO     29 [qwen-vl-text] page grouping: [9, 10], lines per page: [36, 8]
2026-08-10 17:31:01,430 INFO     29 [qwen-vl-text] page=9, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 17:31:01,574 INFO     29 [qwen-vl-text] page=10, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 17:31:01,574 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1117
2026-08-10 17:31:01,574 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:31:01,574 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 432, \"bbox_end\": 475, \"encounter_dates\": [\"2026-02-03\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "2026-02-03 10:41\n主 诉：本次访视为评价注射用HLN601脂质体在晚期实体瘤患者中的安全性、耐受性及药代动力\n学特征和初步疗效的多中心、开放性的I期临床试验项目安全性随访。\n病 史：同前\n审阅受试者日志卡：不适用\n试验用药品/医疗器械使用的依从性：不适用\n合并用药/合并非药物治疗：\n(1) 合并用药：\n同前\n(2) 合并非药物治疗：\n无\n体格、专科检查以及辅助检查：\n(1) 体格、专科检查：\n2026年2月3日 早 8:36 测 生命体征 ：T:36.5℃ P:78次/分 R:19次/分 BP:137/83 mmHg，体\n重：84.7Kg，体格检查同筛选期，ECOG评分1分\n(2) 辅助检查：\n血细胞分析（5分类）、生化系列（36项）、D-二聚体、尿分析+沉渣、凝血四项、常规心电图，\n第 1 页\n未见明显异常。\n疗效评估：\n本次访视进行以下疗效评估：不适用\n不良事件：\n(1) 既往未转归的不良事件：无\n(2) 新发生的不良事件：\n不适用\n其 他：病历更正：2026-01-20门诊病历中“病历更正：2025.12.24住院病历中Bp:142/92mmHg（\nCS 与既往病史 高血压（2025.UNK-持续）有关），Bp：143/87mmHg（CS 与既往病史 高血压（\n2025.UNK-持续）有关）更正为（CS 与既往病史 高血压（2005.UNK-持续）有关）” 改为“\n2025.12.25住院病历中Bp:142/92mmHg（CS 与既往病史 高血压（2025.UNK-持续）有关），Bp：\n143/87mmHg（CS 与既往病史 高血压（2025.UNK-持续）有关）更正为（CS 与既往病史 高血压（\n2005.UNK-持续）有关）”时间更正错误，应为：“2025.12.25住院病历中Bp:142/92mmHg（CS 与既往\n病史 高血压（2025.UNK-持续）有关），Bp：143/87mmHg（CS 与既往病史 高血压（2025.UNK-持续）\n有关）更正为（CS 与既往病史 高血压（2005.UNK-持续）有关）” 改为“2025.12.25住院病历中Bp：\n142/92mmHg（CS 与既往病史 高血压（2025.UNK-持续）有关），Bp：143/87mmHg（CS 与既往病史 高\n血压（2025.UNK-持续）有关）更正为（CS 与既往病史 高血压（2005.UNK-持续）有关）\n第 2 页\n门诊诊断:\n肺恶性肿瘤\n诊疗意见:\n(1)后续访视:出组,出组原因:疾病进展\n(2)发放试验用药品/医疗器械:不适用\n(3)其他用药/非药物治疗医嘱:无\n(4)其他:无\n第3页",
    "role": "user"
  }
]
2026-08-10 17:31:03,324 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:31:03,324 INFO     29 [qwen-vl-text] LLM output (len=263):
{
  "encounter_date": "2026-02-03",
  "chief_complaint": "本次访视为评价注射用HLN601脂质体在晚期实体瘤患者中的安全性、耐受性及药代动力学特征和初步疗效的多中心、开放性的I期临床试验项目安全性随访。",
  "present_illness": "同前",
  "past_history": "高血压（2005.UNK-持续）",
  "diagnosis": "肺恶性肿瘤",
  "treatment_plan": "后续访视:出组,出组原因:疾病进展"
}
2026-08-10 17:31:03,324 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-03]
2026-08-10 17:31:03,327 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1977404, prompt_len=1749
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共36行）
["2026-02-03 10:41", "主 诉：本次访视为评价注射用HLN601脂质体在晚期实体瘤患者中的安全性、耐受性及药代动力", "学特征和初步疗效的多中心、开放性的I期临床试验项目安全性随访。", "病 史：同前", "审阅受试者日志卡：不适用", "试验用药品/医疗器械使用的依从性：不适用", "合并用药/合并非药物治疗：", "(1) 合并用药：", "同前", "(2) 合并非药物治疗：", "无", "体格、专科检查以及辅助检查：", "(1) 体格、专科检查：", "2026年2月3日 早 8:36 测 生命体征 ：T:36.5℃ P:78次/分 R:19次/分 BP:137/83 mmHg，体", "重：84.7Kg，体格检查同筛选期，ECOG评分1分", "(2) 辅助检查：", "血细胞分析（5分类）、生化系列（36项）、D-二聚体、尿分析+沉渣、凝血四项、常规心电图，", "第 1 页", "未见明显异常。", "疗效评估：", "本次访视进行以下疗效评估：不适用", "不良事件：", "(1) 既往未转归的不良事件：无", "(2) 新发生的不良事件：", "不适用", "其 他：病历更正：2026-01-20门诊病历中“病历更正：2025.12.24住院病历中Bp:142/92mmHg（", "CS 与既往病史 高血压（2025.UNK-持续）有关），Bp：143/87mmHg（CS 与既往病史 高血压（", "2025.UNK-持续）有关）更正为（CS 与既往病史 高血压（2005.UNK-持续）有关）” 改为“", "2025.12.25住院病历中Bp:142/92mmHg（CS 与既往病史 高血压（2025.UNK-持续）有关），Bp：", "143/87mmHg（CS 与既往病史 高血压（2025.UNK-持续）有关）更正为（CS 与既往病史 高血压（", "2005.UNK-持续）有关）”时间更正错误，应为：“2025.12.25住院病历中Bp:142/92mmHg（CS 与既往", "病史 高血压（2025.UNK-持续）有关），Bp：143/87mmHg（CS 与既往病史 高血压（2025.UNK-持续）", "有关）更正为（CS 与既往病史 高血压（2005.UNK-持续）有关）” 改为“2025.12.25住院病历中Bp：", "142/92mmHg（CS 与既往病史 高血压（2025.UNK-持续）有关），Bp：143/87mmHg（CS 与既往病史 高", "血压（2025.UNK-持续）有关）更正为（CS 与既往病史 高血压（2005.UNK-持续）有关）", "第 2 页"]

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
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord API raw response (len=2614):
[
	{"text": "2026-02-03 10:41", "bbox": [166, 91, 306, 102]},
	{"text": "主 诉：本次访视为评价注射用HLN601脂质体在晚期实体瘤患者中的安全性、耐受性及药代动力", "bbox": [199, 111, 829, 130]},
	{"text": "学特征和初步疗效的多中心、开放性的I期临床试验项目安全性随访。", "bbox": [168, 126, 623, 144]},
	{"text": "病 史：同前", "bbox": [199, 145, 298, 159]},
	{"text": "审阅受试者日志卡：不适用", "bbox": [200, 157, 393, 172]},
	{"text": "试验用药品/医疗器械使用的依从性：不适用", "bbox": [200, 169, 513, 186]},
	{"text": "合并用药/合并非药物治疗：", "bbox": [201, 185, 397, 200]},
	{"text": "(1) 合并用药：", "bbox": [209, 200, 317, 214]},
	{"text": "同前", "bbox": [204, 216, 235, 229]},
	{"text": "(2) 合并非药物治疗：", "bbox": [210, 228, 367, 243]},
	{"text": "无", "bbox": [204, 245, 220, 258]},
	{"text": "体格、专科检查以及辅助检查：", "bbox": [205, 254, 424, 271]},
	{"text": "(1) 体格、专科检查：", "bbox": [212, 269, 369, 284]},
	{"text": "2026年2月3日 早 8:36 测 生命体征 ：T:36.5℃ P:78次/分 R:19次/分 BP:137/83 mmHg，体", "bbox": [206, 274, 825, 298]},
	{"text": "重：84.7Kg，体格检查同筛选期，ECOG评分1分", "bbox": [176, 294, 489, 313]},
	{"text": "(2) 辅助检查：", "bbox": [215, 312, 321, 327]},
	{"text": "血细胞分析（5分类）、生化系列（36项）、D-二聚体、尿分析+沉渣、凝血四项、常规心电图，", "bbox": [208, 314, 825, 342]},
	{"text": "第 1 页", "bbox": [494, 348, 544, 360]},
	{"text": "未见明显异常。", "bbox": [180, 447, 276, 460]},
	{"text": "疗效评估：", "bbox": [210, 460, 279, 473]},
	{"text": "本次访视进行以下疗效评估：不适用", "bbox": [210, 472, 441, 486]},
	{"text": "不良事件：", "bbox": [210, 486, 279, 499]},
	{"text": "(1) 既往未转归的不良事件：无", "bbox": [217, 498, 433, 511]},
	{"text": "(2) 新发生的不良事件：", "bbox": [218, 511, 380, 524]},
	{"text": "不适用", "bbox": [211, 525, 255, 537]},
	{"text": "其 他：病历更正：2026-01-20门诊病历中“病历更正：2025.12.24住院病历中Bp:142/92mmHg（", "bbox": [211, 535, 817, 550]},
	{"text": "CS 与既往病史 高血压（2025.UNK-持续）有关），Bp：143/87mmHg（CS 与既往病史 高血压（", "bbox": [182, 548, 771, 564]},
	{"text": "2025.UNK-持续）有关）更正为（CS 与既往病史 高血压（2005.UNK-持续）有关）” 改为“", "bbox": [183, 561, 757, 577]},
	{"text": "2025.12.25住院病历中Bp:142/92mmHg（CS 与既往病史 高血压（2025.UNK-持续）有关），Bp：", "bbox": [183, 574, 772, 590]},
	{"text": "143/87mmHg（CS 与既往病史 高血压（2025.UNK-持续）有关）更正为（CS 与既往病史 高血压（", "bbox": [184, 587, 786, 603]},
	{"text": "2005.UNK-持续）有关）”时间更正错误，应为：“2025.12.25住院病历中Bp:142/92mmHg（CS 与既往", "bbox": [184, 599, 814, 615]},
	{"text": "病史 高血压（2025.UNK-持续）有关），Bp：143/87mmHg（CS 与既往病史 高血压（2025.UNK-持续）", "bbox": [184, 612, 808, 628]},
	{"text": "有关）更正为（CS 与既往病史 高血压（2005.UNK-持续）有关）” 改为“2025.12.25住院病历中Bp：", "bbox": [184, 625, 814, 641]},
	{"text": "142/92mmHg（CS 与既往病史 高血压（2025.UNK-持续）有关），Bp：143/87mmHg（CS 与既往病史 高", "bbox": [185, 638, 815, 654]},
	{"text": "血压（2025.UNK-持续）有关）更正为（CS 与既往病史 高血压（2005.UNK-持续）有关）", "bbox": [185, 651, 732, 668]},
	{"text": "第 2 页", "bbox": [484, 693, 530, 705]}
]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=16.3s
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[0]: text=2026-02-03 10:41, bbox=[166, 91, 306, 102]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[1]: text=主 诉：本次访视为评价注射用HLN601脂质体在晚期实体瘤患者中的安全性、耐受性及药代动力, bbox=[199, 111, 829, 130]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[2]: text=学特征和初步疗效的多中心、开放性的I期临床试验项目安全性随访。, bbox=[168, 126, 623, 144]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[3]: text=病 史：同前, bbox=[199, 145, 298, 159]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[4]: text=审阅受试者日志卡：不适用, bbox=[200, 157, 393, 172]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[5]: text=试验用药品/医疗器械使用的依从性：不适用, bbox=[200, 169, 513, 186]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[6]: text=合并用药/合并非药物治疗：, bbox=[201, 185, 397, 200]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[7]: text=(1) 合并用药：, bbox=[209, 200, 317, 214]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[8]: text=同前, bbox=[204, 216, 235, 229]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[9]: text=(2) 合并非药物治疗：, bbox=[210, 228, 367, 243]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[10]: text=无, bbox=[204, 245, 220, 258]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[11]: text=体格、专科检查以及辅助检查：, bbox=[205, 254, 424, 271]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[12]: text=(1) 体格、专科检查：, bbox=[212, 269, 369, 284]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[13]: text=2026年2月3日 早 8:36 测 生命体征 ：T:36.5℃ P:78次/分 R:19次/分 BP:137/83 mmHg，体, bbox=[206, 274, 825, 298]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[14]: text=重：84.7Kg，体格检查同筛选期，ECOG评分1分, bbox=[176, 294, 489, 313]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[15]: text=(2) 辅助检查：, bbox=[215, 312, 321, 327]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[16]: text=血细胞分析（5分类）、生化系列（36项）、D-二聚体、尿分析+沉渣、凝血四项、常规心电图，, bbox=[208, 314, 825, 342]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[17]: text=第 1 页, bbox=[494, 348, 544, 360]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[18]: text=未见明显异常。, bbox=[180, 447, 276, 460]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[19]: text=疗效评估：, bbox=[210, 460, 279, 473]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[20]: text=本次访视进行以下疗效评估：不适用, bbox=[210, 472, 441, 486]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[21]: text=不良事件：, bbox=[210, 486, 279, 499]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[22]: text=(1) 既往未转归的不良事件：无, bbox=[217, 498, 433, 511]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[23]: text=(2) 新发生的不良事件：, bbox=[218, 511, 380, 524]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[24]: text=不适用, bbox=[211, 525, 255, 537]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[25]: text=其 他：病历更正：2026-01-20门诊病历中“病历更正：2025.12.24住院病历中Bp:142/92mmHg（, bbox=[211, 535, 817, 550]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[26]: text=CS 与既往病史 高血压（2025.UNK-持续）有关），Bp：143/87mmHg（CS 与既往病史 高血压（, bbox=[182, 548, 771, 564]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[27]: text=2025.UNK-持续）有关）更正为（CS 与既往病史 高血压（2005.UNK-持续）有关）” 改为“, bbox=[183, 561, 757, 577]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[28]: text=2025.12.25住院病历中Bp:142/92mmHg（CS 与既往病史 高血压（2025.UNK-持续）有关），Bp：, bbox=[183, 574, 772, 590]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[29]: text=143/87mmHg（CS 与既往病史 高血压（2025.UNK-持续）有关）更正为（CS 与既往病史 高血压（, bbox=[184, 587, 786, 603]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[30]: text=2005.UNK-持续）有关）”时间更正错误，应为：“2025.12.25住院病历中Bp:142/92mmHg（CS 与既往, bbox=[184, 599, 814, 615]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[31]: text=病史 高血压（2025.UNK-持续）有关），Bp：143/87mmHg（CS 与既往病史 高血压（2025.UNK-持续）, bbox=[184, 612, 808, 628]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[32]: text=有关）更正为（CS 与既往病史 高血压（2005.UNK-持续）有关）” 改为“2025.12.25住院病历中Bp：, bbox=[184, 625, 814, 641]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[33]: text=142/92mmHg（CS 与既往病史 高血压（2025.UNK-持续）有关），Bp：143/87mmHg（CS 与既往病史 高, bbox=[185, 638, 815, 654]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[34]: text=血压（2025.UNK-持续）有关）更正为（CS 与既往病史 高血压（2005.UNK-持续）有关）, bbox=[185, 651, 732, 668]
2026-08-10 17:31:19,638 INFO     29 [qwen-vl-text] coord item[35]: text=第 2 页, bbox=[484, 693, 530, 705]
2026-08-10 17:31:19,639 INFO     29 [qwen-vl-text] page=9 — 36/36 coords, api_time=16.3s
2026-08-10 17:31:19,640 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=813094, prompt_len=724
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共8行）
["门诊诊断:", "肺恶性肿瘤", "诊疗意见:", "(1)后续访视:出组,出组原因:疾病进展", "(2)发放试验用药品/医疗器械:不适用", "(3)其他用药/非药物治疗医嘱:无", "(4)其他:无", "第3页"]

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
2026-08-10 17:31:22,824 INFO     29 [qwen-vl-text] coord API raw response (len=442):
[
	{"text": "门诊诊断:", "bbox": [626, 87, 694, 100]},
	{"text": "肺恶性肿瘤", "bbox": [626, 100, 698, 112]},
	{"text": "诊疗意见:", "bbox": [220, 124, 291, 136]},
	{"text": "(1)后续访视:出组,出组原因:疾病进展", "bbox": [227, 138, 517, 151]},
	{"text": "(2)发放试验用药品/医疗器械:不适用", "bbox": [227, 151, 502, 165]},
	{"text": "(3)其他用药/非药物治疗医嘱:无", "bbox": [227, 165, 474, 178]},
	{"text": "(4)其他:无", "bbox": [227, 178, 341, 191]},
	{"text": "第3页", "bbox": [498, 342, 546, 354]}
]
2026-08-10 17:31:22,824 INFO     29 [qwen-vl-text] coord API: raw_items=8, valid_items=8, elapsed=3.2s
2026-08-10 17:31:22,824 INFO     29 [qwen-vl-text] coord item[0]: text=门诊诊断:, bbox=[626, 87, 694, 100]
2026-08-10 17:31:22,824 INFO     29 [qwen-vl-text] coord item[1]: text=肺恶性肿瘤, bbox=[626, 100, 698, 112]
2026-08-10 17:31:22,824 INFO     29 [qwen-vl-text] coord item[2]: text=诊疗意见:, bbox=[220, 124, 291, 136]
2026-08-10 17:31:22,824 INFO     29 [qwen-vl-text] coord item[3]: text=(1)后续访视:出组,出组原因:疾病进展, bbox=[227, 138, 517, 151]
2026-08-10 17:31:22,824 INFO     29 [qwen-vl-text] coord item[4]: text=(2)发放试验用药品/医疗器械:不适用, bbox=[227, 151, 502, 165]
2026-08-10 17:31:22,824 INFO     29 [qwen-vl-text] coord item[5]: text=(3)其他用药/非药物治疗医嘱:无, bbox=[227, 165, 474, 178]
2026-08-10 17:31:22,825 INFO     29 [qwen-vl-text] coord item[6]: text=(4)其他:无, bbox=[227, 178, 341, 191]
2026-08-10 17:31:22,825 INFO     29 [qwen-vl-text] coord item[7]: text=第3页, bbox=[498, 342, 546, 354]
2026-08-10 17:31:22,825 INFO     29 [qwen-vl-text] page=10 — 8/8 coords, api_time=3.2s
2026-08-10 17:31:22,825 INFO     29 [qwen-vl-text] new_positions (44):
[[9, 98.81979797363282, 182.16179626464844, 76.61290222167969, 85.87380249023438], [9, 118.46469757080078, 493.5036898803711, 93.45090270996094, 109.44700317382812], [9, 100.01039794921876, 370.87189239501953, 106.07940307617189, 121.233603515625], [9, 118.46469757080078, 177.39939636230469, 122.07550354003907, 133.86210388183594], [9, 119.05999755859375, 233.95289520263674, 132.17830383300782, 144.80680419921876], [9, 119.05999755859375, 305.38889373779296, 142.28110412597655, 156.59340454101564], [9, 119.65529754638672, 236.3340951538086, 155.75150451660156, 168.3800048828125], [9, 124.41769744873048, 188.7100961303711, 168.3800048828125, 180.16660522460938], [9, 121.44119750976563, 139.89549713134767, 181.8504052734375, 192.79510559082033], [9, 125.01299743652345, 218.47509552001955, 191.95320556640627, 204.58170593261718], [9, 121.44119750976563, 130.96599731445312, 206.26550598144533, 217.21020629882813], [9, 122.0364974975586, 252.40719482421875, 213.8426062011719, 228.15490661621095], [9, 126.20359741210937, 219.6656954956055, 226.47110656738283, 239.09960693359375], [9, 122.63179748535157, 491.1224899291992, 230.68060668945313, 250.88620727539063], [9, 104.7727978515625, 291.10169403076173, 247.5186071777344, 263.51470764160155], [9, 127.98949737548828, 191.09129608154296, 262.6728076171875, 275.30130798339843], [9, 123.82239746093751, 491.1224899291992, 264.35660766601563, 287.9298083496094], [9, 294.07819396972656, 323.843193359375, 292.98120849609376, 303.0840087890625], [9, 107.15399780273438, 164.30279663085938, 376.329310913086, 387.2740112304688], [9, 125.01299743652345, 166.0886965942383, 387.2740112304688, 398.21871154785157], [9, 125.01299743652345, 262.52729461669924, 397.37681152343754, 409.16341186523437], [9, 125.01299743652345, 166.0886965942383, 409.16341186523437, 420.1081121826172], [9, 129.18009735107424, 257.7648947143555, 419.26621215820313, 430.2109124755859], [9, 129.77539733886718, 226.21399536132813, 430.2109124755859, 441.1556127929688], [9, 125.60829742431642, 151.80149688720704, 441.9975128173828, 452.1003131103516], [9, 125.60829742431642, 486.3600900268555, 450.41651306152346, 463.0450134277344], [9, 108.34459777832032, 458.9762905883789, 461.36121337890626, 474.83161376953126], [9, 108.93989776611329, 450.6420907592774, 472.30591369628905, 485.77631408691406], [9, 108.93989776611329, 459.5715905761719, 483.2506140136719, 496.7210144042969], [9, 109.53519775390626, 467.9057904052735, 494.1953143310547, 507.6657147216797], [9, 109.53519775390626, 484.5741900634766, 504.29811462402347, 517.7685150146484], [9, 109.53519775390626, 481.00239013671876, 515.2428149414063, 528.7132153320313], [9, 109.53519775390626, 484.5741900634766, 526.1875152587891, 539.6579156494141], [9, 110.13049774169923, 485.1694900512696, 537.1322155761719, 550.6026159667969], [9, 110.13049774169923, 435.75959106445316, 548.0769158935547, 562.3892163085937], [9, 288.1251940917969, 315.5089935302735, 583.4367169189453, 593.5395172119141], [10, 372.65779235839847, 413.1381915283203, 73.24530212402344, 84.19000244140625], [10, 372.65779235839847, 415.5193914794922, 84.19000244140625, 94.292802734375], [10, 130.96599731445312, 173.23229644775392, 104.39560302734375, 114.4984033203125], [10, 135.1330972290039, 307.77009368896483, 116.18220336914062, 127.12690368652345], [10, 135.1330972290039, 298.8405938720703, 127.12690368652345, 138.91350402832032], [10, 135.1330972290039, 282.1721942138672, 138.91350402832032, 149.85820434570314], [10, 135.1330972290039, 202.99729583740236, 149.85820434570314, 160.80290466308594], [10, 296.45939392089844, 325.03379333496093, 287.9298083496094, 298.0326086425781]]
2026-08-10 17:31:22,825 INFO     29 [qwen-vl-text] ═══ DONE ═══ 44 positions, pages=2, time=21.7s
2026-08-10 17:31:22,841 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 17:31:22,841 INFO     29 [Trace] task=df5ff51c | doc=06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "476 items", "markdown": "", "text": "", "name": "06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 2, \"chunks_Clinical\": 1}"}
2026-08-10 17:31:22,841 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 17:31:22,848 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:31:22,849 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 17:31:24,310 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:31:24,317 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 17:31:24,317 INFO     29 [Trace] task=df5ff51c | doc=06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "476 items", "markdown": "", "text": "", "name": "06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 2, \"chunks_Clinical\": 1}"}
2026-08-10 17:31:24,317 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 17:31:24,326 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:31:24,326 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 17:31:24,777 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:31:24,783 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 17:31:24,784 INFO     29 [Trace] task=df5ff51c | doc=06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "476 items", "markdown": "", "text": "", "name": "06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 2, \"chunks_Clinical\": 1}"}
2026-08-10 17:31:24,784 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 17:31:24,789 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:31:24,790 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:31:24,790 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 17:31:24,790 INFO     29 [qwen-vl-text] positions(15): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:31:24,790 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [15]
2026-08-10 17:31:24,966 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 17:31:24,966 INFO     29 [qwen-vl-text] LLM extraction start, text_len=584
2026-08-10 17:31:24,966 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:31:24,967 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 102, \"bbox_end\": 116, \"encounter_dates\": [\"2026-01-07\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "性别：男\n年龄：64岁\n出院日期：2026-01-07 17:10\n住院天数：1天\n入院情况：因直肠癌术后5年余，左肾上腺转移1年余入院。查体：ECOG 1分。胸壁、腹部可见手术瘢痕，愈合可。\n入院诊断：1.直肠中分化腺癌术后（pT2N1bM0 IIIA→IV期） 左锁骨区、纵膈、右侧肺门区淋巴结转移 左肾上腺转移 双肺转移 2.2型糖尿病伴多个并发症 2型糖尿病性周围血管病变 2型糖尿病性肾病 3.高血压病3级（极高危） 4.右肺错构瘤术后\n诊疗经过：入院后经患者及其家属同意，无禁忌，于2026-01-07行第3周期治疗：注射用HLN601脂质体20.2mg静脉输液。治疗结束，准予出院。\n治疗前TNM分期：IV期\n出院诊断：1.直肠中分化腺癌术后（pT2N1bM0 IIIA→IV期） 左锁骨区、纵膈、右侧肺门区淋巴结转移 左肾上腺转移 双肺转移 2.2型糖尿病伴多个并发症 2型糖尿病性周围血管病变 2型糖尿病性肾病 3.高血压病3级（极高危） 4.右肺错构瘤术后\n出院情况：一般情况可，查体：ECOG 1分。胸壁、腹部可见手术瘢痕，愈合可。\n出院医嘱：\n1.注意休息，避免劳累、感染；\n2.每周至少查2次血常规（3-4天一次），若白细胞、中性粒细胞或血小板下降，及时升白或升血小板治疗；\n3.出院带药：无。如有不适及时就诊。\n4.按临床试验方案要求随访。",
    "role": "user"
  }
]
2026-08-10 17:31:31,944 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:31:31.943+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 81, "failed": 0, "current": {"df5ff51c94e011f1bd9827cf206dfa2d": {"id": "df5ff51c94e011f1bd9827cf206dfa2d", "doc_id": "df229e1a94e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 3352826, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786382896642, "task_type": "dataflow", "root_trace_id": "02e835c46e184d6daf27401b2b0ac85a", "root_traceparent": "00-02e835c46e184d6daf27401b2b0ac85a-ddd202d54b80a7dd-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:31:32,329 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:31:32,329 INFO     29 [qwen-vl-text] LLM output (len=2037):
{
  "encounter_date": "2026-01-07",
  "admission_date": "2026-01-06",
  "discharge_date": "2026-01-07",
  "hospital_days": 1,
  "department": null,
  "bed_number": null,
  "admission_condition": "因直肠癌术后5年余，左肾上腺转移1年余入院。查体：ECOG 1分。胸壁、腹部可见手术瘢痕，愈合可。",
  "admission_diagnoses": [
    {
      "name": "直肠中分化腺癌术后（pT2N1bM0 IIIA→IV期） 左锁骨区、纵膈、右侧肺门区淋巴结转移 左肾上腺转移 双肺转移",
      "diagnosis_type": "西医"
    },
    {
      "name": "2型糖尿病伴多个并发症",
      "diagnosis_type": "西医"
    },
    {
      "name": "2型糖尿病性周围血管病变",
      "diagnosis_type": "西医"
    },
    {
      "name": "2型糖尿病性肾病",
      "diagnosis_type": "西医"
    },
    {
      "name": "高血压病3级（极高危）",
      "diagnosis_type": "西医"
    },
    {
      "name": "右肺错构瘤术后",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "入院后经患者及其家属同意，无禁忌，于2026-01-07行第3周期治疗：注射用HLN601脂质体20.2mg静脉输液。治疗结束，准予出院。",
  "auxiliary_exams": null,
  "imaging_findings": null,
  "discharge_diagnoses": [
    {
      "name": "直肠中分化腺癌术后（pT2N1bM0 IIIA→IV期） 左锁骨区、纵膈、右侧肺门区淋巴结转移 左肾上腺转移 双肺转移",
      "diagnosis_type": "西医"
    },
    {
      "name": "2型糖尿病伴多个并发症",
      "diagnosis_type": "西医"
    },
    {
      "name": "2型糖尿病性周围血管病变",
      "diagnosis_type": "西医"
    },
    {
      "name": "2型糖尿病性肾病",
      "diagnosis_type": "西医"
    },
    {
      "name": "高血压病3级（极高危）",
      "diagnosis_type": "西医"
    },
    {
      "name": "右肺错构瘤术后",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "一般情况可，查体：ECOG 1分。胸壁、腹部可见手术瘢痕，愈合可。",
  "outcome": null,
  "discharge_orders": "1.注意休息，避免劳累、感染；2.每周至少查2次血常规（3-4天一次），若白细胞、中性粒细胞或血小板下降，及时升白或升血小板治疗；3.出院带药：无。如有不适及时就诊。4.按临床试验方案要求随访。",
  "do_medications": [],
  "do_follow_up": "按临床试验方案要求随访。",
  "do_precautions": [
    "注意休息，避免劳累、感染",
    "每周至少查2次血常规（3-4天一次），若白细胞、中性粒细胞或血小板下降，及时升白或升血小板治疗",
    "如有不适及时就诊"
  ],
  "next_treatment_date": null,
  "attending_physician": null,
  "pe_ecog_score": 1,
  "body_surface_area": null,
  "vs_temperature_c": null,
  "vs_pulse_bpm": null,
  "vs_respiration_rpm": null,
  "vs_systolic_bp_mmhg": null,
  "vs_diastolic_bp_mmhg": null
}
2026-08-10 17:31:32,329 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-07]
2026-08-10 17:31:32,334 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1138845, prompt_len=1242
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共15行）
["性别：男", "年龄：64岁", "出院日期：2026-01-07 17:10", "住院天数：1天", "入院情况：因直肠癌术后5年余，左肾上腺转移1年余入院。查体：ECOG 1分。胸壁、腹部可见手术瘢痕，愈合可。", "入院诊断：1.直肠中分化腺癌术后（pT2N1bM0 IIIA→IV期） 左锁骨区、纵膈、右侧肺门区淋巴结转移 左肾上腺转移 双肺转移 2.2型糖尿病伴多个并发症 2型糖尿病性周围血管病变 2型糖尿病性肾病 3.高血压病3级（极高危） 4.右肺错构瘤术后", "诊疗经过：入院后经患者及其家属同意，无禁忌，于2026-01-07行第3周期治疗：注射用HLN601脂质体20.2mg静脉输液。治疗结束，准予出院。", "治疗前TNM分期：IV期", "出院诊断：1.直肠中分化腺癌术后（pT2N1bM0 IIIA→IV期） 左锁骨区、纵膈、右侧肺门区淋巴结转移 左肾上腺转移 双肺转移 2.2型糖尿病伴多个并发症 2型糖尿病性周围血管病变 2型糖尿病性肾病 3.高血压病3级（极高危） 4.右肺错构瘤术后", "出院情况：一般情况可，查体：ECOG 1分。胸壁、腹部可见手术瘢痕，愈合可。", "出院医嘱：", "1.注意休息，避免劳累、感染；", "2.每周至少查2次血常规（3-4天一次），若白细胞、中性粒细胞或血小板下降，及时升白或升血小板治疗；", "3.出院带药：无。如有不适及时就诊。", "4.按临床试验方案要求随访。"]

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
2026-08-10 17:31:41,931 INFO     29 [qwen-vl-text] coord API raw response (len=1242):
[
	{"text": "性别：男", "bbox": [206, 85, 268, 98]},
	{"text": "年龄：64岁", "bbox": [206, 99, 283, 112]},
	{"text": "出院日期：2026-01-07 17:10", "bbox": [485, 87, 686, 99]},
	{"text": "住院天数：1天", "bbox": [485, 101, 584, 113]},
	{"text": "入院情况：因直肠癌术后5年余，左肾上腺转移1年余入院。查体：ECOG 1分。胸壁、腹部可见手术瘢痕，愈合可。", "bbox": [168, 115, 786, 141]},
	{"text": "入院诊断：1.直肠中分化腺癌术后（pT2N1bM0 IIIA→IV期） 左锁骨区、纵膈、右侧肺门区淋巴结转移 左肾上腺转移 双肺转移 2.2型糖尿病伴多个并发症 2型糖尿病性周围血管病变 2型糖尿病性肾病 3.高血压病3级（极高危） 4.右肺错构瘤术后", "bbox": [168, 144, 786, 185]},
	{"text": "诊疗经过：入院后经患者及其家属同意，无禁忌，于2026-01-07行第3周期治疗：注射用HLN601脂质体20.2mg静脉输液。治疗结束，准予出院。", "bbox": [168, 187, 777, 214]},
	{"text": "治疗前TNM分期：IV期", "bbox": [198, 215, 347, 228]},
	{"text": "出院诊断：1.直肠中分化腺癌术后（pT2N1bM0 IIIA→IV期） 左锁骨区、纵膈、右侧肺门区淋巴结转移 左肾上腺转移 双肺转移 2.2型糖尿病伴多个并发症 2型糖尿病性周围血管病变 2型糖尿病性肾病 3.高血压病3级（极高危） 4.右肺错构瘤术后", "bbox": [168, 230, 784, 271]},
	{"text": "出院情况：一般情况可，查体：ECOG 1分。胸壁、腹部可见手术瘢痕，愈合可。", "bbox": [200, 273, 730, 286]},
	{"text": "出院医嘱：", "bbox": [200, 288, 268, 300]},
	{"text": "1.注意休息，避免劳累、感染；", "bbox": [200, 302, 407, 315]},
	{"text": "2.每周至少查2次血常规（3-4天一次），若白细胞、中性粒细胞或血小板下降，及时升白或升血小板治疗；", "bbox": [168, 317, 783, 344]},
	{"text": "3.出院带药：无。如有不适及时就诊。", "bbox": [198, 346, 454, 359]},
	{"text": "4.按临床试验方案要求随访。", "bbox": [198, 360, 393, 373]}
]
2026-08-10 17:31:41,932 INFO     29 [qwen-vl-text] coord API: raw_items=15, valid_items=15, elapsed=9.6s
2026-08-10 17:31:41,932 INFO     29 [qwen-vl-text] coord item[0]: text=性别：男, bbox=[206, 85, 268, 98]
2026-08-10 17:31:41,932 INFO     29 [qwen-vl-text] coord item[1]: text=年龄：64岁, bbox=[206, 99, 283, 112]
2026-08-10 17:31:41,932 INFO     29 [qwen-vl-text] coord item[2]: text=出院日期：2026-01-07 17:10, bbox=[485, 87, 686, 99]
2026-08-10 17:31:41,932 INFO     29 [qwen-vl-text] coord item[3]: text=住院天数：1天, bbox=[485, 101, 584, 113]
2026-08-10 17:31:41,932 INFO     29 [qwen-vl-text] coord item[4]: text=入院情况：因直肠癌术后5年余，左肾上腺转移1年余入院。查体：ECOG 1分。胸壁、腹部可见手术瘢痕，愈合可。, bbox=[168, 115, 786, 141]
2026-08-10 17:31:41,932 INFO     29 [qwen-vl-text] coord item[5]: text=入院诊断：1.直肠中分化腺癌术后（pT2N1bM0 IIIA→IV期） 左锁骨区、纵膈、右侧肺门区淋巴结转移 左肾上腺转移 双肺转移 2.2型糖尿病伴多个并发症 2型糖尿病性周围血管病变 2型糖尿病性肾病 3.高血压病3级（极高危） 4.右肺错构瘤术后, bbox=[168, 144, 786, 185]
2026-08-10 17:31:41,932 INFO     29 [qwen-vl-text] coord item[6]: text=诊疗经过：入院后经患者及其家属同意，无禁忌，于2026-01-07行第3周期治疗：注射用HLN601脂质体20.2mg静脉输液。治疗结束，准予出院。, bbox=[168, 187, 777, 214]
2026-08-10 17:31:41,932 INFO     29 [qwen-vl-text] coord item[7]: text=治疗前TNM分期：IV期, bbox=[198, 215, 347, 228]
2026-08-10 17:31:41,932 INFO     29 [qwen-vl-text] coord item[8]: text=出院诊断：1.直肠中分化腺癌术后（pT2N1bM0 IIIA→IV期） 左锁骨区、纵膈、右侧肺门区淋巴结转移 左肾上腺转移 双肺转移 2.2型糖尿病伴多个并发症 2型糖尿病性周围血管病变 2型糖尿病性肾病 3.高血压病3级（极高危） 4.右肺错构瘤术后, bbox=[168, 230, 784, 271]
2026-08-10 17:31:41,932 INFO     29 [qwen-vl-text] coord item[9]: text=出院情况：一般情况可，查体：ECOG 1分。胸壁、腹部可见手术瘢痕，愈合可。, bbox=[200, 273, 730, 286]
2026-08-10 17:31:41,932 INFO     29 [qwen-vl-text] coord item[10]: text=出院医嘱：, bbox=[200, 288, 268, 300]
2026-08-10 17:31:41,932 INFO     29 [qwen-vl-text] coord item[11]: text=1.注意休息，避免劳累、感染；, bbox=[200, 302, 407, 315]
2026-08-10 17:31:41,932 INFO     29 [qwen-vl-text] coord item[12]: text=2.每周至少查2次血常规（3-4天一次），若白细胞、中性粒细胞或血小板下降，及时升白或升血小板治疗；, bbox=[168, 317, 783, 344]
2026-08-10 17:31:41,932 INFO     29 [qwen-vl-text] coord item[13]: text=3.出院带药：无。如有不适及时就诊。, bbox=[198, 346, 454, 359]
2026-08-10 17:31:41,932 INFO     29 [qwen-vl-text] coord item[14]: text=4.按临床试验方案要求随访。, bbox=[198, 360, 393, 373]
2026-08-10 17:31:41,932 INFO     29 [qwen-vl-text] page=4 — 15/15 coords, api_time=9.6s
2026-08-10 17:31:41,932 INFO     29 [qwen-vl-text] new_positions (15):
[[4, 122.63179748535157, 159.54039672851565, 71.56150207519532, 82.50620239257813], [4, 122.63179748535157, 168.46989654541017, 83.34810241699219, 94.292802734375], [4, 288.72049407958986, 408.3757916259766, 73.24530212402344, 83.34810241699219], [4, 288.72049407958986, 347.6551928710938, 85.03190246582031, 95.13470275878906], [4, 100.01039794921876, 467.9057904052735, 96.8185028076172, 118.70790344238281], [4, 100.01039794921876, 467.9057904052735, 121.233603515625, 155.75150451660156], [4, 100.01039794921876, 462.5480905151367, 157.4353045654297, 180.16660522460938], [4, 117.86939758300782, 206.56909576416015, 181.00850524902344, 191.95320556640627], [4, 100.01039794921876, 466.71519042968754, 193.6370056152344, 228.15490661621095], [4, 119.05999755859375, 434.5689910888672, 229.83870666503907, 240.7834069824219], [4, 119.05999755859375, 159.54039672851565, 242.46720703125, 252.57000732421875], [4, 119.05999755859375, 242.2870950317383, 254.2538073730469, 265.1985076904297], [4, 100.01039794921876, 466.11989044189454, 266.88230773925784, 289.6136083984375], [4, 117.86939758300782, 270.2661944580078, 291.29740844726564, 302.24210876464844], [4, 117.86939758300782, 233.95289520263674, 303.0840087890625, 314.0287091064453]]
2026-08-10 17:31:41,932 INFO     29 [qwen-vl-text] ═══ DONE ═══ 15 positions, pages=1, time=17.1s
2026-08-10 17:31:41,940 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 17:31:41,940 INFO     29 [Trace] task=df5ff51c | doc=06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf | Extractor:Discharge | outputs={"chunks": "1 items, types={'DischargeRecord': 1}", "html": "", "json": "476 items", "markdown": "", "text": "", "name": "06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 2, \"chunks_Clinical\": 1}"}
2026-08-10 17:31:41,940 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 17:31:41,948 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:31:41,949 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:31:41,949 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-10 17:31:41,949 INFO     29 [qwen-vl-text] positions(102): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:31:41,949 INFO     29 [qwen-vl-text] page grouping: [0, 1, 2, 3], lines per page: [7, 37, 36, 22]
2026-08-10 17:31:41,994 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 17:31:42,200 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 17:31:42,423 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 17:31:42,640 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 17:31:42,641 INFO     29 [qwen-vl-text] LLM extraction start, text_len=3744
2026-08-10 17:31:42,642 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:31:42,642 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 0, \"bbox_end\": 101, \"encounter_dates\": [\"2026-01-07\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "20200113根治术\n术后XELOX 6周期\n20240510复发\n20240601~20240828 7周贝伐+伊利替康+5FU\n20240925贝伐+卡培维持 门诊持续使用，末次25.10\n20251119确诊转移\n20251210参加HLN601脂质体项目，末次20260107行第三周期，进展出组\n性别：男\n婚姻：丧偶\n年龄：64岁\n入院日期：2026-01-07 09:03\n民族：汉族\n记录日期：2026-01-07 09:25\n职业：离退休人员\n病史陈述者：患者本人及亲属\n主诉：直肠癌术后5年余，左肾上腺转移1年余。\n现病史：患者因“查体发现直肠肿物3天”于2020-01-06第一次住院普外科。入院后完善检查，排除手术禁忌症，行电子肠镜下消化道注药术，EMR，电子肠镜下尼龙绳结扎术，\n电子肠镜下钛夹止血术，电子肠镜下取异物术，积极术前准备，2020-01-13在气管插管全身\n麻醉下行腹腔镜下直肠癌根治术（Dixon），术后病理：（直肠）直肠隆起型中分化腺癌，\n伴脉管内癌栓，侵及浅肌层，标记上切缘、标记下切缘及环周切缘未见癌累及，肠周淋巴结\n3/18枚见癌转移。TNM分期：pT2N1bMx。免疫组化：MLH1（+），PMS2（+），MSH2（+），\nMSH6（+），Ki-67+指数约60%。术后行“XELOX”方案化疗6周期。\n2024-05-10当地医院复查CT：“提示左肾上腺肿物”。2024-05-16住院泌尿外科。入院\n后完善辅助检查：肾上腺增强(64排)：1.左侧肾上腺区占位，考虑恶性肿瘤，转移瘤？皮质\n癌？2.右侧肾上腺外侧肢增粗，增生可能大。3.脂肪肝。胸部平扫(64排-128层)：对比\n2021-10-08CT：1.符合右肺上叶术后改变，请结合临床。2.左肺下叶病灶（img33）较前略\n增大，右肺下叶（img50）结节为新见，余结节变化不著，建议随诊复查。3.新见双肺轻度\n坠积性改变；双肺慢性炎症/纤维灶，较前略增多。余所见较前变化不著。PET-CT全身显\n像：1.直肠术后，术区肠壁略增厚，FDG代谢略高，考虑炎症；肠周未见肿大淋巴结。2.右\n肺上叶结节切除术后，术区未见异常FDG代谢增高灶。3.左肾上腺占位，FDG代谢不均匀增\n高，考虑恶性病变，原发肾上腺肿瘤？4.（1）左肺下叶结节，较本院2020-07-06PET/CT、\n2021-10-09CT，体积略增大；（2）右肺下叶结节，较本院2020-07-06PET/CT、\n2021-10-09CT为新增；以上两枚结节FDG代谢均不高，建议密切随访。5.右侧中耳乳突炎\n症；鼻咽部左侧咽隐窝区炎症；双侧颈部增生淋巴结；双侧扁桃体炎症；甲状腺小结节，\nFDG代谢不高，建议B超随访；余双肺小结节，FDG代谢不高，建议随访观察；脂肪肝；双肾\n小结石；前列腺钙化灶。完善相关辅助检查后，为排除左侧肾上腺是否为转移瘤，遂请介入\n科会诊协助左侧肾上腺穿刺活检术，病理：（左侧肾上腺组织）送检示皮肤组织及大部分坏\n死组织，偶见少许异型腺体，结合病史及免疫组化结果，符合肠癌转移。免疫组化：CK20（\n+）、CK7（-）、CDX-2（+）、SATB2（+）。请我科会诊后转入。转科后于2024-05-28行左\n肾上腺穿刺活检，病理：（左侧肾上腺穿刺标本）腺癌。基因检测：KRAS突变。于\n2024-06-01、2024-06-19、2024-07-03、2024-07-17、2024-07-31、2024-08-14、\n2024-08-28给予一线治疗1-7周期：贝伐珠单抗 400mg d1+伊力替康 280mg d1+左亚叶酸钙\n175mg d1+氟尿嘧啶 0.75g d1+氟尿嘧啶 4.0g持续泵入48h，q14d。过程顺利。6周期治疗后\n第1页\n复查疗效评价：SD。\n患者分别于2024-09-25、2024-10-14第9、10次入院给予贝伐珠单抗 400mg d1+卡培他\n滨（希罗达）1.5g bid d-14/21d维持治疗。\n出院后患者规律于门诊就诊并应用贝伐珠单抗+卡培他滨维持治疗。2025-08患者感腹\n胀，大便次数改变，大便不尽感，于2025-08-29再次入院保健科，入院后完善相关检查：肠\n镜检查：所见直结肠黏膜大致正常，直肠术后改变。给予调脂、降压、降糖等治疗后好转出\n院。\n患者因“咳嗽”2025-11-17入院全科，入院后完善相关检查排除禁忌后于2025-11-19行\n电子支气管镜检查并留取标本。2025-11-19 病理回示：EBUS组织：送检组织内见腺癌，伴\n大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS刷片）查见肿瘤细胞。2025-11-25门\n诊完善PET/CT躯干显像（颅底到大腿中上部、不含脑）：与本院2024-05-17 PET/CT比较：\n1.直肠癌术后，术区肠壁略增厚，FDG代谢增高，首先考虑炎症，请结合肠镜评价；肠周及\n腹、盆腔未见异常肿大淋巴结。2.左侧锁骨区、纵隔、右侧肺门区多发大小不等淋巴结/结\n节影，FDG代谢增高，结合病理，符合多发淋巴结转移表现。3.左肾上腺肿物治疗后，较前\n体积明显减小，FDG代谢不高，建议随诊。4.（1）右肺下叶结节，较前体积增大，代谢增\n高，考虑转移可能大；（2）左肺下叶结节，代谢不高，较前体积未见著变，建议继续随\n诊；（3）余双肺多发结节，代谢不高，部分较前为新发，不除外部分为转移性，建议治疗\n过程定期复查。5.右肺上叶结节切除术后，术区未见异常FDG代谢增高灶。6.鼻咽部后壁及\n左侧咽隐窝区炎症；甲状腺小结节，FDG代谢不高，建议B超随访；贲门部轻度FDG代谢增高\n及腹腔部分肠道FDG代谢增高，考虑炎性/生理性摄取可能；脂肪肝；双肾小结石；前列腺钙\n化灶。\n患者于2025-12-03入组评价注射用HLN601脂质体在晚期实体瘤患者中的安全性、耐受性\n及药代动力学特征和初步疗效的多中心、开放的I期临床试验。于2025-12-10行第1周期治\n疗：注射用HLN601脂质体20.2mg静脉输液。治疗结束，准予出院。\n患者于2025-12-25再次入院行第2周期治疗：注射用HLN601脂质体20.2mg静脉输液。治\n疗结束，准予出院。\n出院后患者复查血常规、肝肾功无明显异常，今为继续治疗入院。患者精神状态良好，\n食欲一般，睡眠良好，大小便正常，体力情况良好，体重较前无明显变化。\n补充病史：高脂血症（2024.12.uk-持续）\n补充合并用药：于2024.12.uk口服阿托伐他汀钙片 10mg qd 持续中，用药原因：治疗\n既往病史高脂血症（2024.12.uk-持续）。\n既往史：2021-10-15本院胸外科行“胸腔镜右肺上叶楔形切除术”，病理：右肺上\n叶：错构瘤。余参阅首次入院病历。\n个人史：参阅首次入院病历。\n家族史：参阅首次入院病历。\n第2页\n体格检查\nT 35.4℃\nP 108次/分\nR 20次/分\nBp 137/90mmHg\nH 168cm\nW 86.1kg\nS 2.02m²\nNRS 0分\n发育正常，营养中等，正常面容，表情自如，自主体位，神志清楚，查体合作。全身皮肤粘膜无黄染，无皮疹，无皮下出血，无皮下结节，皮下无水肿，无肝掌、蜘蛛痣，毛发分布均匀。全身浅表淋巴结无肿大。眼睑无水肿，结膜无苍白，眼球无突出，无震颤，巩膜无黄染，瞳孔等大等圆，对光反射灵敏，耳廓对称，无畸形，牵拉无疼痛，外耳道无异常分泌物，乳突无压痛，无听力粗试障碍。鼻无畸形。口唇无发绀，口腔粘膜无充血、糜烂。舌苔薄白，伸舌无偏斜、震颤，牙龈无红肿，咽部粘膜无充血，扁桃体无肿大。颈软无抵抗，颈动脉无异常搏动，半坐位颈静脉未见充盈，颈部大血管区未闻及血管杂音。气管居中，肝颈静脉回流征阴性，甲状腺无肿大，无压痛、震颤、血管杂音。胸廓无畸形，呼吸运动两侧对称，肋间隙无狭窄或饱满，胸壁无压痛，语颤无增强、减弱，胸骨无压痛。双肺叩诊清音，呼吸规整，双肺呼吸音清晰，未闻及干湿性啰音，无胸膜摩擦音。心前区无异常隆起、异常搏动、震颤，心浊音界不大，心率108次/分，律齐，心音有力，各瓣膜听诊区未闻及杂音，无心包摩擦音。腹平坦，软，无压痛、反跳痛，腹部无包块。肝脏未触及，脾脏未触及，Murphy氏征阴性，肾区无叩击痛，无移动性浊音。肠鸣音正常，4次/分。肛门及外生殖器无异常。脊柱正常生理弯曲，四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾），关节无肿胀、压痛，下肢无水肿。\n肌肉无压痛，四肢肌力、肌张力未见异常，双侧肱\n二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性。\n专科检查： ECOG 1分。浅表淋巴结未及肿大。胸壁、腹部可见手术瘢痕(CS病史)，愈合可。\n辅助检查\n2025-11-19 病理：EBUS组织：送检组织内见腺癌，伴大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS刷片）查见肿瘤细胞。本院。\n初步诊断：\n1.直肠中分化腺癌术后（pT2N1bM0 IIIA\n→IV期）\n左锁骨区、纵膈、右侧肺门区淋巴\n结转移\n左肾上腺转移\n第3页",
    "role": "user"
  }
]
2026-08-10 17:32:03,985 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:32:03.982+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 81, "failed": 0, "current": {"df5ff51c94e011f1bd9827cf206dfa2d": {"id": "df5ff51c94e011f1bd9827cf206dfa2d", "doc_id": "df229e1a94e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 3352826, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786382896642, "task_type": "dataflow", "root_trace_id": "02e835c46e184d6daf27401b2b0ac85a", "root_traceparent": "00-02e835c46e184d6daf27401b2b0ac85a-ddd202d54b80a7dd-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:32:07,972 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:32:07,972 INFO     29 [qwen-vl-text] LLM output (len=4620):
{
  "encounter_date": "2026-01-07",
  "dm_name": null,
  "dm_gender": "男",
  "dm_age": 64,
  "dm_ethnicity": "汉族",
  "dm_marital_status": "丧偶",
  "dm_occupation": "离退休人员",
  "dm_admission_time": "2026-01-07 09:03",
  "dm_record_time": "2026-01-07 09:25",
  "dm_history_provider": "患者本人及亲属",
  "cc_text": "直肠癌术后5年余，左肾上腺转移1年余。",
  "cc_main_symptoms": [
    "直肠癌术后",
    "左肾上腺转移"
  ],
  "cc_duration": "5年余",
  "pi_text": "患者因“查体发现直肠肿物3天”于2020-01-06第一次住院普外科。入院后完善检查，排除手术禁忌症，行电子肠镜下消化道注药术，EMR，电子肠镜下尼龙绳结扎术，电子肠镜下钛夹止血术，电子肠镜下取异物术，积极术前准备，2020-01-13在气管插管全身麻醉下行腹腔镜下直肠癌根治术（Dixon），术后病理：（直肠）直肠隆起型中分化腺癌，伴脉管内癌栓，侵及浅肌层，标记上切缘、标记下切缘及环周切缘未见癌累及，肠周淋巴结3/18枚见癌转移。TNM分期：pT2N1bMx。免疫组化：MLH1（+），PMS2（+），MSH2（+），MSH6（+），Ki-67+指数约60%。术后行“XELOX”方案化疗6周期。\n2024-05-10当地医院复查CT：“提示左肾上腺肿物”。2024-05-16住院泌尿外科。入院后完善辅助检查：肾上腺增强(64排)：1.左侧肾上腺区占位，考虑恶性肿瘤，转移瘤？皮质癌？2.右侧肾上腺外侧肢增粗，增生可能大。3.脂肪肝。胸部平扫(64排-128层)：对比2021-10-08CT：1.符合右肺上叶术后改变，请结合临床。2.左肺下叶病灶（img33）较前略增大，右肺下叶（img50）结节为新见，余结节变化不著，建议随诊复查。3.新见双肺轻度坠积性改变；双肺慢性炎症/纤维灶，较前略增多。余所见较前变化不著。PET-CT全身显像：1.直肠术后，术区肠壁略增厚，FDG代谢略高，考虑炎症；肠周未见肿大淋巴结。2.右肺上叶结节切除术后，术区未见异常FDG代谢增高灶。3.左肾上腺占位，FDG代谢不均匀增高，考虑恶性病变，原发肾上腺肿瘤？4.（1）左肺下叶结节，较本院2020-07-06PET/CT、2021-10-09CT，体积略增大；（2）右肺下叶结节，较本院2020-07-06PET/CT、2021-10-09CT为新增；以上两枚结节FDG代谢均不高，建议密切随访。5.右侧中耳乳突炎症；鼻咽部左侧咽隐窝区炎症；双侧颈部增生淋巴结；双侧扁桃体炎症；甲状腺小结节，FDG代谢不高，建议B超随访；余双肺小结节，FDG代谢不高，建议随访观察；脂肪肝；双肾小结石；前列腺钙化灶。完善相关辅助检查后，为排除左侧肾上腺是否为转移瘤，遂请介入科会诊协助左侧肾上腺穿刺活检术，病理：（左侧肾上腺组织）送检示皮肤组织及大部分坏死组织，偶见少许异型腺体，结合病史及免疫组化结果，符合肠癌转移。免疫组化：CK20（+）、CK7（-）、CDX-2（+）、SATB2（+）。请我科会诊后转入。转科后于2024-05-28行左肾上腺穿刺活检，病理：（左侧肾上腺穿刺标本）腺癌。基因检测：KRAS突变。于2024-06-01、2024-06-19、2024-07-03、2024-07-17、2024-07-31、2024-08-14、2024-08-28给予一线治疗1-7周期：贝伐珠单抗 400mg d1+伊力替康 280mg d1+左亚叶酸钙 175mg d1+氟尿嘧啶 0.75g d1+氟尿嘧啶 4.0g持续泵入48h，q14d。过程顺利。6周期治疗后复查疗效评价：SD。\n患者分别于2024-09-25、2024-10-14第9、10次入院给予贝伐珠单抗 400mg d1+卡培他滨（希罗达）1.5g bid d-14/21d维持治疗。\n出院后患者规律于门诊就诊并应用贝伐珠单抗+卡培他滨维持治疗。2025-08患者感腹胀，大便次数改变，大便不尽感，于2025-08-29再次入院保健科，入院后完善相关检查：肠镜检查：所见直结肠黏膜大致正常，直肠术后改变。给予调脂、降压、降糖等治疗后好转出院。\n患者因“咳嗽”2025-11-17入院全科，入院后完善相关检查排除禁忌后于2025-11-19行电子支气管镜检查并留取标本。2025-11-19 病理回示：EBUS组织：送检组织内见腺癌，伴大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS刷片）查见肿瘤细胞。2025-11-25门诊完善PET/CT躯干显像（颅底到大腿中上部、不含脑）：与本院2024-05-17 PET/CT比较：1.直肠癌术后，术区肠壁略增厚，FDG代谢增高，首先考虑炎症，请结合肠镜评价；肠周及腹、盆腔未见异常肿大淋巴结。2.左侧锁骨区、纵隔、右侧肺门区多发大小不等淋巴结/结节影，FDG代谢增高，结合病理，符合多发淋巴结转移表现。3.左肾上腺肿物治疗后，较前体积明显减小，FDG代谢不高，建议随诊。4.（1）右肺下叶结节，较前体积增大，代谢增高，考虑转移可能大；（2）左肺下叶结节，代谢不高，较前体积未见著变，建议继续随诊；（3）余双肺多发结节，代谢不高，部分较前为新发，不除外部分为转移性，建议治疗过程定期复查。5.右肺上叶结节切除术后，术区未见异常FDG代谢增高灶。6.鼻咽部后壁及左侧咽隐窝区炎症；甲状腺小结节，FDG代谢不高，建议B超随访；贲门部轻度FDG代谢增高及腹腔部分肠道FDG代谢增高，考虑炎性/生理性摄取可能；脂肪肝；双肾小结石；前列腺钙化灶。\n患者于2025-12-03入组评价注射用HLN601脂质体在晚期实体瘤患者中的安全性、耐受性及药代动力学特征和初步疗效的多中心、开放的I期临床试验。于2025-12-10行第1周期治疗：注射用HLN601脂质体20.2mg静脉输液。治疗结束，准予出院。\n患者于2025-12-25再次入院行第2周期治疗：注射用HLN601脂质体20.2mg静脉输液。治疗结束，准予出院。\n出院后患者复查血常规、肝肾功无明显异常，今为继续治疗入院。患者精神状态良好，食欲一般，睡眠良好，大小便正常，体力情况良好，体重较前无明显变化。\n补充病史：高脂血症（2024.12.uk-持续）\n补充合并用药：于2024.12.uk口服阿托伐他汀钙片 10mg qd 持续中，用药原因：治疗既往病史高脂血症（2024.12.uk-持续）。",
  "pmh_disease_history": [
    "高脂血症"
  ],
  "pmh_allergy_history": [],
  "pmh_surgery_trauma_history": [
    "2020-01-13 腹腔镜下直肠癌根治术（Dixon）",
    "2021-10-15 胸腔镜右肺上叶楔形切除术"
  ],
  "ph_smoking": null,
  "ph_drinking": null,
  "oh_menarche_age": null,
  "oh_menopause_age": null,
  "oh_pregnancies": null,
  "fh_text": "参阅首次入院病历。",
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 35.4,
  "vs_pulse_bpm": 108,
  "vs_respiration_rpm": 20,
  "vs_systolic_bp_mmhg": 137,
  "vs_diastolic_bp_mmhg": 90,
  "pe_general_condition": "发育正常，营养中等，正常面容，表情自如，自主体位，神志清楚，查体合作。",
  "pe_skin_mucosa": "全身皮肤粘膜无黄染，无皮疹，无皮下出血，无皮下结节，皮下无水肿，无肝掌、蜘蛛痣，毛发分布均匀。",
  "pe_lymph_nodes": "全身浅表淋巴结无肿大。",
  "pe_lungs": "胸廓无畸形，呼吸运动两侧对称，肋间隙无狭窄或饱满，胸壁无压痛，语颤无增强、减弱，胸骨无压痛。双肺叩诊清音，呼吸规整，双肺呼吸音清晰，未闻及干湿性啰音，无胸膜摩擦音。",
  "pe_heart": "心前区无异常隆起、异常搏动、震颤，心浊音界不大，心率108次/分，律齐，心音有力，各瓣膜听诊区未闻及杂音，无心包摩擦音。",
  "pe_abdomen": "腹平坦，软，无压痛、反跳痛，腹部无包块。肝脏未触及，脾脏未触及，Murphy氏征阴性，肾区无叩击痛，无移动性浊音。肠鸣音正常，4次/分。",
  "pe_extremities": "脊柱正常生理弯曲，四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾），关节无肿胀、压痛，下肢无水肿。肌肉无压痛，四肢肌力、肌张力未见异常，双侧肱二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性。",
  "pe_nervous_system": "神志清楚，查体合作。双侧Babinski征阴性。",
  "pe_specialist_exam": "ECOG 1分。浅表淋巴结未及肿大。胸壁、腹部可见手术瘢痕(CS病史)，愈合可。",
  "pe_ecog_score": 1,
  "pat_text": "2025-11-19 病理：EBUS组织：送检组织内见腺癌，伴大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS刷片）查见肿瘤细胞。本院。",
  "pat_items": [
    "2025-11-19 病理：EBUS组织：送检组织内见腺癌，伴大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS刷片）查见肿瘤细胞。本院。"
  ],
  "preliminary_diagnoses": [
    {
      "name": "直肠中分化腺癌术后（pT2N1bM0 IIIA→IV期）",
      "diagnosis_type": "西医",
      "is_primary": true
    },
    {
      "name": "左锁骨区、纵膈、右侧肺门区淋巴结转移",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "左肾上腺转移",
      "diagnosis_type": "西医",
      "is_primary": false
    }
  ],
  "department": null
}
2026-08-10 17:32:07,972 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-07]
2026-08-10 17:32:07,972 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=71677, prompt_len=786
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共7行）
["20200113根治术", "术后XELOX 6周期", "20240510复发", "20240601~20240828 7周贝伐+伊利替康+5FU", "20240925贝伐+卡培维持 门诊持续使用，末次25.10", "20251119确诊转移", "20251210参加HLN601脂质体项目，末次20260107行第三周期，进展出组"]

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
2026-08-10 17:32:13,525 INFO     29 [qwen-vl-text] coord API raw response (len=464):
[
	{"text": "20200113根治术", "bbox": [171, 233, 314, 248]},
	{"text": "术后XELOX 6周期", "bbox": [171, 248, 334, 262]},
	{"text": "20240510复发", "bbox": [171, 262, 293, 276]},
	{"text": "20240601~20240828 7周贝伐+伊利替康+5FU", "bbox": [171, 276, 555, 290]},
	{"text": "20240925贝伐+卡培维持 门诊持续使用，末次25.10", "bbox": [171, 290, 636, 305]},
	{"text": "20251119确诊转移", "bbox": [171, 305, 334, 319]},
	{"text": "20251210参加HLN601脂质体项目，末次20260107行第三周期，进展出组", "bbox": [171, 319, 797, 334]}
]
2026-08-10 17:32:13,525 INFO     29 [qwen-vl-text] coord API: raw_items=7, valid_items=7, elapsed=5.6s
2026-08-10 17:32:13,525 INFO     29 [qwen-vl-text] coord item[0]: text=20200113根治术, bbox=[171, 233, 314, 248]
2026-08-10 17:32:13,525 INFO     29 [qwen-vl-text] coord item[1]: text=术后XELOX 6周期, bbox=[171, 248, 334, 262]
2026-08-10 17:32:13,525 INFO     29 [qwen-vl-text] coord item[2]: text=20240510复发, bbox=[171, 262, 293, 276]
2026-08-10 17:32:13,525 INFO     29 [qwen-vl-text] coord item[3]: text=20240601~20240828 7周贝伐+伊利替康+5FU, bbox=[171, 276, 555, 290]
2026-08-10 17:32:13,525 INFO     29 [qwen-vl-text] coord item[4]: text=20240925贝伐+卡培维持 门诊持续使用，末次25.10, bbox=[171, 290, 636, 305]
2026-08-10 17:32:13,525 INFO     29 [qwen-vl-text] coord item[5]: text=20251119确诊转移, bbox=[171, 305, 334, 319]
2026-08-10 17:32:13,525 INFO     29 [qwen-vl-text] coord item[6]: text=20251210参加HLN601脂质体项目，末次20260107行第三周期，进展出组, bbox=[171, 319, 797, 334]
2026-08-10 17:32:13,526 INFO     29 [qwen-vl-text] page=0 — 7/7 coords, api_time=5.6s
2026-08-10 17:32:13,529 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1895611, prompt_len=2147
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共37行）
["性别：男", "婚姻：丧偶", "年龄：64岁", "入院日期：2026-01-07 09:03", "民族：汉族", "记录日期：2026-01-07 09:25", "职业：离退休人员", "病史陈述者：患者本人及亲属", "主诉：直肠癌术后5年余，左肾上腺转移1年余。", "现病史：患者因“查体发现直肠肿物3天”于2020-01-06第一次住院普外科。入院后完善检查，排除手术禁忌症，行电子肠镜下消化道注药术，EMR，电子肠镜下尼龙绳结扎术，", "电子肠镜下钛夹止血术，电子肠镜下取异物术，积极术前准备，2020-01-13在气管插管全身", "麻醉下行腹腔镜下直肠癌根治术（Dixon），术后病理：（直肠）直肠隆起型中分化腺癌，", "伴脉管内癌栓，侵及浅肌层，标记上切缘、标记下切缘及环周切缘未见癌累及，肠周淋巴结", "3/18枚见癌转移。TNM分期：pT2N1bMx。免疫组化：MLH1（+），PMS2（+），MSH2（+），", "MSH6（+），Ki-67+指数约60%。术后行“XELOX”方案化疗6周期。", "2024-05-10当地医院复查CT：“提示左肾上腺肿物”。2024-05-16住院泌尿外科。入院", "后完善辅助检查：肾上腺增强(64排)：1.左侧肾上腺区占位，考虑恶性肿瘤，转移瘤？皮质", "癌？2.右侧肾上腺外侧肢增粗，增生可能大。3.脂肪肝。胸部平扫(64排-128层)：对比", "2021-10-08CT：1.符合右肺上叶术后改变，请结合临床。2.左肺下叶病灶（img33）较前略", "增大，右肺下叶（img50）结节为新见，余结节变化不著，建议随诊复查。3.新见双肺轻度", "坠积性改变；双肺慢性炎症/纤维灶，较前略增多。余所见较前变化不著。PET-CT全身显", "像：1.直肠术后，术区肠壁略增厚，FDG代谢略高，考虑炎症；肠周未见肿大淋巴结。2.右", "肺上叶结节切除术后，术区未见异常FDG代谢增高灶。3.左肾上腺占位，FDG代谢不均匀增", "高，考虑恶性病变，原发肾上腺肿瘤？4.（1）左肺下叶结节，较本院2020-07-06PET/CT、", "2021-10-09CT，体积略增大；（2）右肺下叶结节，较本院2020-07-06PET/CT、", "2021-10-09CT为新增；以上两枚结节FDG代谢均不高，建议密切随访。5.右侧中耳乳突炎", "症；鼻咽部左侧咽隐窝区炎症；双侧颈部增生淋巴结；双侧扁桃体炎症；甲状腺小结节，", "FDG代谢不高，建议B超随访；余双肺小结节，FDG代谢不高，建议随访观察；脂肪肝；双肾", "小结石；前列腺钙化灶。完善相关辅助检查后，为排除左侧肾上腺是否为转移瘤，遂请介入", "科会诊协助左侧肾上腺穿刺活检术，病理：（左侧肾上腺组织）送检示皮肤组织及大部分坏", "死组织，偶见少许异型腺体，结合病史及免疫组化结果，符合肠癌转移。免疫组化：CK20（", "+）、CK7（-）、CDX-2（+）、SATB2（+）。请我科会诊后转入。转科后于2024-05-28行左", "肾上腺穿刺活检，病理：（左侧肾上腺穿刺标本）腺癌。基因检测：KRAS突变。于", "2024-06-01、2024-06-19、2024-07-03、2024-07-17、2024-07-31、2024-08-14、", "2024-08-28给予一线治疗1-7周期：贝伐珠单抗 400mg d1+伊力替康 280mg d1+左亚叶酸钙", "175mg d1+氟尿嘧啶 0.75g d1+氟尿嘧啶 4.0g持续泵入48h，q14d。过程顺利。6周期治疗后", "第1页"]

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
2026-08-10 17:32:30,524 INFO     29 [qwen-vl-text] coord API raw response (len=3052):
[
	{"text": "性别：男", "bbox": [209, 97, 270, 110]},
	{"text": "婚姻：丧偶", "bbox": [491, 97, 567, 110]},
	{"text": "年龄：64岁", "bbox": [209, 111, 285, 124]},
	{"text": "入院日期：2026-01-07 09:03", "bbox": [491, 111, 690, 124]},
	{"text": "民族：汉族", "bbox": [209, 125, 285, 138]},
	{"text": "记录日期：2026-01-07 09:25", "bbox": [491, 125, 690, 138]},
	{"text": "职业：离退休人员", "bbox": [209, 139, 316, 152]},
	{"text": "病史陈述者：患者本人及亲属", "bbox": [491, 139, 690, 152]},
	{"text": "主诉：直肠癌术后5年余，左肾上腺转移1年余。", "bbox": [209, 153, 537, 166]},
	{"text": "现病史：患者因“查体发现直肠肿物3天”于2020-01-06第一次住院普外科。入院后完善检查，排除手术禁忌症，行电子肠镜下消化道注药术，EMR，电子肠镜下尼龙绳结扎术，", "bbox": [180, 167, 787, 180]},
	{"text": "电子肠镜下钛夹止血术，电子肠镜下取异物术，积极术前准备，2020-01-13在气管插管全身", "bbox": [180, 195, 787, 208]},
	{"text": "麻醉下行腹腔镜下直肠癌根治术（Dixon），术后病理：（直肠）直肠隆起型中分化腺癌，", "bbox": [180, 209, 787, 222]},
	{"text": "伴脉管内癌栓，侵及浅肌层，标记上切缘、标记下切缘及环周切缘未见癌累及，肠周淋巴结", "bbox": [180, 223, 787, 236]},
	{"text": "3/18枚见癌转移。TNM分期：pT2N1bMx。免疫组化：MLH1（+），PMS2（+），MSH2（+），", "bbox": [180, 237, 787, 250]},
	{"text": "MSH6（+），Ki-67+指数约60%。术后行“XELOX”方案化疗6周期。", "bbox": [180, 251, 618, 264]},
	{"text": "2024-05-10当地医院复查CT：“提示左肾上腺肿物”。2024-05-16住院泌尿外科。入院", "bbox": [209, 265, 787, 278]},
	{"text": "后完善辅助检查：肾上腺增强(64排)：1.左侧肾上腺区占位，考虑恶性肿瘤，转移瘤？皮质", "bbox": [180, 280, 787, 293]},
	{"text": "癌？2.右侧肾上腺外侧肢增粗，增生可能大。3.脂肪肝。胸部平扫(64排-128层)：对比", "bbox": [180, 294, 787, 307]},
	{"text": "2021-10-08CT：1.符合右肺上叶术后改变，请结合临床。2.左肺下叶病灶（img33）较前略", "bbox": [180, 308, 787, 321]},
	{"text": "增大，右肺下叶（img50）结节为新见，余结节变化不著，建议随诊复查。3.新见双肺轻度", "bbox": [180, 322, 787, 335]},
	{"text": "坠积性改变；双肺慢性炎症/纤维灶，较前略增多。余所见较前变化不著。PET-CT全身显", "bbox": [180, 336, 787, 349]},
	{"text": "像：1.直肠术后，术区肠壁略增厚，FDG代谢略高，考虑炎症；肠周未见肿大淋巴结。2.右", "bbox": [180, 350, 787, 363]},
	{"text": "肺上叶结节切除术后，术区未见异常FDG代谢增高灶。3.左肾上腺占位，FDG代谢不均匀增", "bbox": [180, 364, 787, 377]},
	{"text": "高，考虑恶性病变，原发肾上腺肿瘤？4.（1）左肺下叶结节，较本院2020-07-06PET/CT、", "bbox": [180, 378, 787, 391]},
	{"text": "2021-10-09CT，体积略增大；（2）右肺下叶结节，较本院2020-07-06PET/CT、", "bbox": [180, 392, 787, 405]},
	{"text": "2021-10-09CT为新增；以上两枚结节FDG代谢均不高，建议密切随访。5.右侧中耳乳突炎", "bbox": [180, 406, 787, 419]},
	{"text": "症；鼻咽部左侧咽隐窝区炎症；双侧颈部增生淋巴结；双侧扁桃体炎症；甲状腺小结节，", "bbox": [180, 420, 787, 433]},
	{"text": "FDG代谢不高，建议B超随访；余双肺小结节，FDG代谢不高，建议随访观察；脂肪肝；双肾", "bbox": [180, 434, 787, 447]},
	{"text": "小结石；前列腺钙化灶。完善相关辅助检查后，为排除左侧肾上腺是否为转移瘤，遂请介入", "bbox": [180, 448, 787, 461]},
	{"text": "科会诊协助左侧肾上腺穿刺活检术，病理：（左侧肾上腺组织）送检示皮肤组织及大部分坏", "bbox": [180, 462, 787, 475]},
	{"text": "死组织，偶见少许异型腺体，结合病史及免疫组化结果，符合肠癌转移。免疫组化：CK20（", "bbox": [180, 476, 787, 489]},
	{"text": "+）、CK7（-）、CDX-2（+）、SATB2（+）。请我科会诊后转入。转科后于2024-05-28行左", "bbox": [180, 490, 787, 503]},
	{"text": "肾上腺穿刺活检，病理：（左侧肾上腺穿刺标本）腺癌。基因检测：KRAS突变。于", "bbox": [180, 504, 787, 517]},
	{"text": "2024-06-01、2024-06-19、2024-07-03、2024-07-17、2024-07-31、2024-08-14、", "bbox": [180, 518, 787, 531]},
	{"text": "2024-08-28给予一线治疗1-7周期：贝伐珠单抗 400mg d1+伊力替康 280mg d1+左亚叶酸钙", "bbox": [180, 532, 787, 545]},
	{"text": "175mg d1+氟尿嘧啶 0.75g d1+氟尿嘧啶 4.0g持续泵入48h，q14d。过程顺利。6周期治疗后", "bbox": [180, 546, 787, 559]},
	{"text": "第1页", "bbox": [460, 575, 508, 586]}
]
2026-08-10 17:32:30,525 INFO     29 [qwen-vl-text] coord API: raw_items=37, valid_items=37, elapsed=17.0s
2026-08-10 17:32:30,525 INFO     29 [qwen-vl-text] coord item[0]: text=性别：男, bbox=[209, 97, 270, 110]
2026-08-10 17:32:30,525 INFO     29 [qwen-vl-text] coord item[1]: text=婚姻：丧偶, bbox=[491, 97, 567, 110]
2026-08-10 17:32:30,525 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：64岁, bbox=[209, 111, 285, 124]
2026-08-10 17:32:30,528 INFO     29 [qwen-vl-text] coord item[3]: text=入院日期：2026-01-07 09:03, bbox=[491, 111, 690, 124]
2026-08-10 17:32:30,528 INFO     29 [qwen-vl-text] coord item[4]: text=民族：汉族, bbox=[209, 125, 285, 138]
2026-08-10 17:32:30,528 INFO     29 [qwen-vl-text] coord item[5]: text=记录日期：2026-01-07 09:25, bbox=[491, 125, 690, 138]
2026-08-10 17:32:30,528 INFO     29 [qwen-vl-text] coord item[6]: text=职业：离退休人员, bbox=[209, 139, 316, 152]
2026-08-10 17:32:30,528 INFO     29 [qwen-vl-text] coord item[7]: text=病史陈述者：患者本人及亲属, bbox=[491, 139, 690, 152]
2026-08-10 17:32:30,528 INFO     29 [qwen-vl-text] coord item[8]: text=主诉：直肠癌术后5年余，左肾上腺转移1年余。, bbox=[209, 153, 537, 166]
2026-08-10 17:32:30,528 INFO     29 [qwen-vl-text] coord item[9]: text=现病史：患者因“查体发现直肠肿物3天”于2020-01-06第一次住院普外科。入院后完善检查，排除手术禁忌症，行电子肠镜下消化道注药术，EMR，电子肠镜下尼龙绳结扎术，, bbox=[180, 167, 787, 180]
2026-08-10 17:32:30,528 INFO     29 [qwen-vl-text] coord item[10]: text=电子肠镜下钛夹止血术，电子肠镜下取异物术，积极术前准备，2020-01-13在气管插管全身, bbox=[180, 195, 787, 208]
2026-08-10 17:32:30,528 INFO     29 [qwen-vl-text] coord item[11]: text=麻醉下行腹腔镜下直肠癌根治术（Dixon），术后病理：（直肠）直肠隆起型中分化腺癌，, bbox=[180, 209, 787, 222]
2026-08-10 17:32:30,528 INFO     29 [qwen-vl-text] coord item[12]: text=伴脉管内癌栓，侵及浅肌层，标记上切缘、标记下切缘及环周切缘未见癌累及，肠周淋巴结, bbox=[180, 223, 787, 236]
2026-08-10 17:32:30,528 INFO     29 [qwen-vl-text] coord item[13]: text=3/18枚见癌转移。TNM分期：pT2N1bMx。免疫组化：MLH1（+），PMS2（+），MSH2（+），, bbox=[180, 237, 787, 250]
2026-08-10 17:32:30,528 INFO     29 [qwen-vl-text] coord item[14]: text=MSH6（+），Ki-67+指数约60%。术后行“XELOX”方案化疗6周期。, bbox=[180, 251, 618, 264]
2026-08-10 17:32:30,528 INFO     29 [qwen-vl-text] coord item[15]: text=2024-05-10当地医院复查CT：“提示左肾上腺肿物”。2024-05-16住院泌尿外科。入院, bbox=[209, 265, 787, 278]
2026-08-10 17:32:30,528 INFO     29 [qwen-vl-text] coord item[16]: text=后完善辅助检查：肾上腺增强(64排)：1.左侧肾上腺区占位，考虑恶性肿瘤，转移瘤？皮质, bbox=[180, 280, 787, 293]
2026-08-10 17:32:30,528 INFO     29 [qwen-vl-text] coord item[17]: text=癌？2.右侧肾上腺外侧肢增粗，增生可能大。3.脂肪肝。胸部平扫(64排-128层)：对比, bbox=[180, 294, 787, 307]
2026-08-10 17:32:30,528 INFO     29 [qwen-vl-text] coord item[18]: text=2021-10-08CT：1.符合右肺上叶术后改变，请结合临床。2.左肺下叶病灶（img33）较前略, bbox=[180, 308, 787, 321]
2026-08-10 17:32:30,528 INFO     29 [qwen-vl-text] coord item[19]: text=增大，右肺下叶（img50）结节为新见，余结节变化不著，建议随诊复查。3.新见双肺轻度, bbox=[180, 322, 787, 335]
2026-08-10 17:32:30,528 INFO     29 [qwen-vl-text] coord item[20]: text=坠积性改变；双肺慢性炎症/纤维灶，较前略增多。余所见较前变化不著。PET-CT全身显, bbox=[180, 336, 787, 349]
2026-08-10 17:32:30,528 INFO     29 [qwen-vl-text] coord item[21]: text=像：1.直肠术后，术区肠壁略增厚，FDG代谢略高，考虑炎症；肠周未见肿大淋巴结。2.右, bbox=[180, 350, 787, 363]
2026-08-10 17:32:30,529 INFO     29 [qwen-vl-text] coord item[22]: text=肺上叶结节切除术后，术区未见异常FDG代谢增高灶。3.左肾上腺占位，FDG代谢不均匀增, bbox=[180, 364, 787, 377]
2026-08-10 17:32:30,529 INFO     29 [qwen-vl-text] coord item[23]: text=高，考虑恶性病变，原发肾上腺肿瘤？4.（1）左肺下叶结节，较本院2020-07-06PET/CT、, bbox=[180, 378, 787, 391]
2026-08-10 17:32:30,529 INFO     29 [qwen-vl-text] coord item[24]: text=2021-10-09CT，体积略增大；（2）右肺下叶结节，较本院2020-07-06PET/CT、, bbox=[180, 392, 787, 405]
2026-08-10 17:32:30,529 INFO     29 [qwen-vl-text] coord item[25]: text=2021-10-09CT为新增；以上两枚结节FDG代谢均不高，建议密切随访。5.右侧中耳乳突炎, bbox=[180, 406, 787, 419]
2026-08-10 17:32:30,529 INFO     29 [qwen-vl-text] coord item[26]: text=症；鼻咽部左侧咽隐窝区炎症；双侧颈部增生淋巴结；双侧扁桃体炎症；甲状腺小结节，, bbox=[180, 420, 787, 433]
2026-08-10 17:32:30,529 INFO     29 [qwen-vl-text] coord item[27]: text=FDG代谢不高，建议B超随访；余双肺小结节，FDG代谢不高，建议随访观察；脂肪肝；双肾, bbox=[180, 434, 787, 447]
2026-08-10 17:32:30,529 INFO     29 [qwen-vl-text] coord item[28]: text=小结石；前列腺钙化灶。完善相关辅助检查后，为排除左侧肾上腺是否为转移瘤，遂请介入, bbox=[180, 448, 787, 461]
2026-08-10 17:32:30,529 INFO     29 [qwen-vl-text] coord item[29]: text=科会诊协助左侧肾上腺穿刺活检术，病理：（左侧肾上腺组织）送检示皮肤组织及大部分坏, bbox=[180, 462, 787, 475]
2026-08-10 17:32:30,529 INFO     29 [qwen-vl-text] coord item[30]: text=死组织，偶见少许异型腺体，结合病史及免疫组化结果，符合肠癌转移。免疫组化：CK20（, bbox=[180, 476, 787, 489]
2026-08-10 17:32:30,529 INFO     29 [qwen-vl-text] coord item[31]: text=+）、CK7（-）、CDX-2（+）、SATB2（+）。请我科会诊后转入。转科后于2024-05-28行左, bbox=[180, 490, 787, 503]
2026-08-10 17:32:30,529 INFO     29 [qwen-vl-text] coord item[32]: text=肾上腺穿刺活检，病理：（左侧肾上腺穿刺标本）腺癌。基因检测：KRAS突变。于, bbox=[180, 504, 787, 517]
2026-08-10 17:32:30,529 INFO     29 [qwen-vl-text] coord item[33]: text=2024-06-01、2024-06-19、2024-07-03、2024-07-17、2024-07-31、2024-08-14、, bbox=[180, 518, 787, 531]
2026-08-10 17:32:30,529 INFO     29 [qwen-vl-text] coord item[34]: text=2024-08-28给予一线治疗1-7周期：贝伐珠单抗 400mg d1+伊力替康 280mg d1+左亚叶酸钙, bbox=[180, 532, 787, 545]
2026-08-10 17:32:30,529 INFO     29 [qwen-vl-text] coord item[35]: text=175mg d1+氟尿嘧啶 0.75g d1+氟尿嘧啶 4.0g持续泵入48h，q14d。过程顺利。6周期治疗后, bbox=[180, 546, 787, 559]
2026-08-10 17:32:30,529 INFO     29 [qwen-vl-text] coord item[36]: text=第1页, bbox=[460, 575, 508, 586]
2026-08-10 17:32:30,529 INFO     29 [qwen-vl-text] page=1 — 37/37 coords, api_time=17.0s
2026-08-10 17:32:30,534 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1958480, prompt_len=1982
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共36行）
["复查疗效评价：SD。", "患者分别于2024-09-25、2024-10-14第9、10次入院给予贝伐珠单抗 400mg d1+卡培他", "滨（希罗达）1.5g bid d-14/21d维持治疗。", "出院后患者规律于门诊就诊并应用贝伐珠单抗+卡培他滨维持治疗。2025-08患者感腹", "胀，大便次数改变，大便不尽感，于2025-08-29再次入院保健科，入院后完善相关检查：肠", "镜检查：所见直结肠黏膜大致正常，直肠术后改变。给予调脂、降压、降糖等治疗后好转出", "院。", "患者因“咳嗽”2025-11-17入院全科，入院后完善相关检查排除禁忌后于2025-11-19行", "电子支气管镜检查并留取标本。2025-11-19 病理回示：EBUS组织：送检组织内见腺癌，伴", "大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS刷片）查见肿瘤细胞。2025-11-25门", "诊完善PET/CT躯干显像（颅底到大腿中上部、不含脑）：与本院2024-05-17 PET/CT比较：", "1.直肠癌术后，术区肠壁略增厚，FDG代谢增高，首先考虑炎症，请结合肠镜评价；肠周及", "腹、盆腔未见异常肿大淋巴结。2.左侧锁骨区、纵隔、右侧肺门区多发大小不等淋巴结/结", "节影，FDG代谢增高，结合病理，符合多发淋巴结转移表现。3.左肾上腺肿物治疗后，较前", "体积明显减小，FDG代谢不高，建议随诊。4.（1）右肺下叶结节，较前体积增大，代谢增", "高，考虑转移可能大；（2）左肺下叶结节，代谢不高，较前体积未见著变，建议继续随", "诊；（3）余双肺多发结节，代谢不高，部分较前为新发，不除外部分为转移性，建议治疗", "过程定期复查。5.右肺上叶结节切除术后，术区未见异常FDG代谢增高灶。6.鼻咽部后壁及", "左侧咽隐窝区炎症；甲状腺小结节，FDG代谢不高，建议B超随访；贲门部轻度FDG代谢增高", "及腹腔部分肠道FDG代谢增高，考虑炎性/生理性摄取可能；脂肪肝；双肾小结石；前列腺钙", "化灶。", "患者于2025-12-03入组评价注射用HLN601脂质体在晚期实体瘤患者中的安全性、耐受性", "及药代动力学特征和初步疗效的多中心、开放的I期临床试验。于2025-12-10行第1周期治", "疗：注射用HLN601脂质体20.2mg静脉输液。治疗结束，准予出院。", "患者于2025-12-25再次入院行第2周期治疗：注射用HLN601脂质体20.2mg静脉输液。治", "疗结束，准予出院。", "出院后患者复查血常规、肝肾功无明显异常，今为继续治疗入院。患者精神状态良好，", "食欲一般，睡眠良好，大小便正常，体力情况良好，体重较前无明显变化。", "补充病史：高脂血症（2024.12.uk-持续）", "补充合并用药：于2024.12.uk口服阿托伐他汀钙片 10mg qd 持续中，用药原因：治疗", "既往病史高脂血症（2024.12.uk-持续）。", "既往史：2021-10-15本院胸外科行“胸腔镜右肺上叶楔形切除术”，病理：右肺上", "叶：错构瘤。余参阅首次入院病历。", "个人史：参阅首次入院病历。", "家族史：参阅首次入院病历。", "第2页"]

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
2026-08-10 17:32:48,099 INFO     29 [qwen-vl-text] coord API raw response (len=2847):
[
	{"text": "复查疗效评价：SD。", "bbox": [180, 86, 314, 99]},
	{"text": "患者分别于2024-09-25、2024-10-14第9、10次入院给予贝伐珠单抗 400mg d1+卡培他", "bbox": [212, 100, 797, 113]},
	{"text": "滨（希罗达）1.5g bid d-14/21d维持治疗。", "bbox": [180, 115, 477, 128]},
	{"text": "出院后患者规律于门诊就诊并应用贝伐珠单抗+卡培他滨维持治疗。2025-08患者感腹", "bbox": [212, 130, 789, 142]},
	{"text": "胀，大便次数改变，大便不尽感，于2025-08-29再次入院保健科，入院后完善相关检查：肠", "bbox": [180, 144, 804, 157]},
	{"text": "镜检查：所见直结肠黏膜大致正常，直肠术后改变。给予调脂、降压、降糖等治疗后好转出", "bbox": [180, 158, 804, 171]},
	{"text": "院。", "bbox": [180, 173, 205, 186]},
	{"text": "患者因“咳嗽”2025-11-17入院全科，入院后完善相关检查排除禁忌后于2025-11-19行", "bbox": [212, 187, 803, 200]},
	{"text": "电子支气管镜检查并留取标本。2025-11-19 病理回示：EBUS组织：送检组织内见腺癌，伴", "bbox": [180, 202, 796, 215]},
	{"text": "大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS刷片）查见肿瘤细胞。2025-11-25门", "bbox": [180, 216, 803, 229]},
	{"text": "诊完善PET/CT躯干显像（颅底到大腿中上部、不含脑）：与本院2024-05-17 PET/CT比较：", "bbox": [180, 231, 785, 244]},
	{"text": "1.直肠癌术后，术区肠壁略增厚，FDG代谢增高，首先考虑炎症，请结合肠镜评价；肠周及", "bbox": [180, 245, 795, 258]},
	{"text": "腹、盆腔未见异常肿大淋巴结。2. 左侧锁骨区、纵隔、右侧肺门区多发大小不等淋巴结/结", "bbox": [180, 260, 802, 273]},
	{"text": "节影，FDG代谢增高，结合病理，符合多发淋巴结转移表现。3.左肾上腺肿物治疗后，较前", "bbox": [180, 274, 794, 287]},
	{"text": "体积明显减小，FDG代谢不高，建议随诊。4.（1）右肺下叶结节，较前体积增大，代谢增", "bbox": [180, 289, 787, 302]},
	{"text": "高，考虑转移可能大；（2）左肺下叶结节，代谢不高，较前体积未见著变，建议继续随", "bbox": [180, 303, 779, 316]},
	{"text": "诊；（3）余双肺多发结节，代谢不高，部分较前为新发，不除外部分为转移性，建议治疗", "bbox": [180, 318, 794, 331]},
	{"text": "过程定期复查。5.右肺上叶结节切除术后，术区未见异常FDG代谢增高灶。6.鼻咽部后壁及", "bbox": [180, 332, 794, 345]},
	{"text": "左侧咽隐窝区炎症；甲状腺小结节，FDG代谢不高，建议B超随访；贲门部轻度FDG代谢增高", "bbox": [180, 347, 794, 360]},
	{"text": "及腹腔部分肠道FDG代谢增高，考虑炎性/生理性摄取可能；脂肪肝；双肾小结石；前列腺钙", "bbox": [180, 361, 801, 374]},
	{"text": "化灶。", "bbox": [180, 376, 222, 389]},
	{"text": "患者于2025-12-03入组评价注射用HLN601脂质体在晚期实体瘤患者中的安全性、耐受性", "bbox": [212, 390, 800, 403]},
	{"text": "及药代动力学特征和初步疗效的多中心、开放的I期临床试验。于2025-12-10行第1周期治", "bbox": [180, 405, 785, 418]},
	{"text": "疗：注射用HLN601脂质体20.2mg静脉输液。治疗结束，准予出院。", "bbox": [180, 419, 622, 432]},
	{"text": "患者于2025-12-25再次入院行第2周期治疗：注射用HLN601脂质体20.2mg静脉输液。治", "bbox": [212, 434, 792, 447]},
	{"text": "疗结束，准予出院。", "bbox": [180, 448, 317, 461]},
	{"text": "出院后患者复查血常规、肝肾功无明显异常，今为继续治疗入院。患者精神状态良好，", "bbox": [212, 462, 790, 475]},
	{"text": "食欲一般，睡眠良好，大小便正常，体力情况良好，体重较前无明显变化。", "bbox": [185, 477, 684, 490]},
	{"text": "补充病史：高脂血症（2024.12.uk-持续）", "bbox": [215, 491, 493, 504]},
	{"text": "补充合并用药：于2024.12.uk口服阿托伐他汀钙片 10mg qd 持续中，用药原因：治疗", "bbox": [215, 505, 790, 518]},
	{"text": "既往病史高脂血症（2024.12.uk-持续）。", "bbox": [185, 520, 463, 533]},
	{"text": "既往史：2021-10-15本院胸外科行“胸腔镜右肺上叶楔形切除术”，病理：右肺上", "bbox": [215, 534, 798, 547]},
	{"text": "叶：错构瘤。余参阅首次入院病历。", "bbox": [185, 548, 424, 561]},
	{"text": "个人史：参阅首次入院病历。", "bbox": [215, 562, 410, 575]},
	{"text": "家族史：参阅首次入院病历。", "bbox": [215, 577, 410, 589]},
	{"text": "第2页", "bbox": [471, 604, 518, 615]}
]
2026-08-10 17:32:48,099 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=17.6s
2026-08-10 17:32:48,099 INFO     29 [qwen-vl-text] coord item[0]: text=复查疗效评价：SD。, bbox=[180, 86, 314, 99]
2026-08-10 17:32:48,099 INFO     29 [qwen-vl-text] coord item[1]: text=患者分别于2024-09-25、2024-10-14第9、10次入院给予贝伐珠单抗 400mg d1+卡培他, bbox=[212, 100, 797, 113]
2026-08-10 17:32:48,099 INFO     29 [qwen-vl-text] coord item[2]: text=滨（希罗达）1.5g bid d-14/21d维持治疗。, bbox=[180, 115, 477, 128]
2026-08-10 17:32:48,100 INFO     29 [qwen-vl-text] coord item[3]: text=出院后患者规律于门诊就诊并应用贝伐珠单抗+卡培他滨维持治疗。2025-08患者感腹, bbox=[212, 130, 789, 142]
2026-08-10 17:32:48,100 INFO     29 [qwen-vl-text] coord item[4]: text=胀，大便次数改变，大便不尽感，于2025-08-29再次入院保健科，入院后完善相关检查：肠, bbox=[180, 144, 804, 157]
2026-08-10 17:32:48,100 INFO     29 [qwen-vl-text] coord item[5]: text=镜检查：所见直结肠黏膜大致正常，直肠术后改变。给予调脂、降压、降糖等治疗后好转出, bbox=[180, 158, 804, 171]
2026-08-10 17:32:48,100 INFO     29 [qwen-vl-text] coord item[6]: text=院。, bbox=[180, 173, 205, 186]
2026-08-10 17:32:48,100 INFO     29 [qwen-vl-text] coord item[7]: text=患者因“咳嗽”2025-11-17入院全科，入院后完善相关检查排除禁忌后于2025-11-19行, bbox=[212, 187, 803, 200]
2026-08-10 17:32:48,100 INFO     29 [qwen-vl-text] coord item[8]: text=电子支气管镜检查并留取标本。2025-11-19 病理回示：EBUS组织：送检组织内见腺癌，伴, bbox=[180, 202, 796, 215]
2026-08-10 17:32:48,100 INFO     29 [qwen-vl-text] coord item[9]: text=大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS刷片）查见肿瘤细胞。2025-11-25门, bbox=[180, 216, 803, 229]
2026-08-10 17:32:48,100 INFO     29 [qwen-vl-text] coord item[10]: text=诊完善PET/CT躯干显像（颅底到大腿中上部、不含脑）：与本院2024-05-17 PET/CT比较：, bbox=[180, 231, 785, 244]
2026-08-10 17:32:48,100 INFO     29 [qwen-vl-text] coord item[11]: text=1.直肠癌术后，术区肠壁略增厚，FDG代谢增高，首先考虑炎症，请结合肠镜评价；肠周及, bbox=[180, 245, 795, 258]
2026-08-10 17:32:48,100 INFO     29 [qwen-vl-text] coord item[12]: text=腹、盆腔未见异常肿大淋巴结。2. 左侧锁骨区、纵隔、右侧肺门区多发大小不等淋巴结/结, bbox=[180, 260, 802, 273]
2026-08-10 17:32:48,100 INFO     29 [qwen-vl-text] coord item[13]: text=节影，FDG代谢增高，结合病理，符合多发淋巴结转移表现。3.左肾上腺肿物治疗后，较前, bbox=[180, 274, 794, 287]
2026-08-10 17:32:48,100 INFO     29 [qwen-vl-text] coord item[14]: text=体积明显减小，FDG代谢不高，建议随诊。4.（1）右肺下叶结节，较前体积增大，代谢增, bbox=[180, 289, 787, 302]
2026-08-10 17:32:48,100 INFO     29 [qwen-vl-text] coord item[15]: text=高，考虑转移可能大；（2）左肺下叶结节，代谢不高，较前体积未见著变，建议继续随, bbox=[180, 303, 779, 316]
2026-08-10 17:32:48,100 INFO     29 [qwen-vl-text] coord item[16]: text=诊；（3）余双肺多发结节，代谢不高，部分较前为新发，不除外部分为转移性，建议治疗, bbox=[180, 318, 794, 331]
2026-08-10 17:32:48,100 INFO     29 [qwen-vl-text] coord item[17]: text=过程定期复查。5.右肺上叶结节切除术后，术区未见异常FDG代谢增高灶。6.鼻咽部后壁及, bbox=[180, 332, 794, 345]
2026-08-10 17:32:48,100 INFO     29 [qwen-vl-text] coord item[18]: text=左侧咽隐窝区炎症；甲状腺小结节，FDG代谢不高，建议B超随访；贲门部轻度FDG代谢增高, bbox=[180, 347, 794, 360]
2026-08-10 17:32:48,100 INFO     29 [qwen-vl-text] coord item[19]: text=及腹腔部分肠道FDG代谢增高，考虑炎性/生理性摄取可能；脂肪肝；双肾小结石；前列腺钙, bbox=[180, 361, 801, 374]
2026-08-10 17:32:48,100 INFO     29 [qwen-vl-text] coord item[20]: text=化灶。, bbox=[180, 376, 222, 389]
2026-08-10 17:32:48,100 INFO     29 [qwen-vl-text] coord item[21]: text=患者于2025-12-03入组评价注射用HLN601脂质体在晚期实体瘤患者中的安全性、耐受性, bbox=[212, 390, 800, 403]
2026-08-10 17:32:48,100 INFO     29 [qwen-vl-text] coord item[22]: text=及药代动力学特征和初步疗效的多中心、开放的I期临床试验。于2025-12-10行第1周期治, bbox=[180, 405, 785, 418]
2026-08-10 17:32:48,101 INFO     29 [qwen-vl-text] coord item[23]: text=疗：注射用HLN601脂质体20.2mg静脉输液。治疗结束，准予出院。, bbox=[180, 419, 622, 432]
2026-08-10 17:32:48,101 INFO     29 [qwen-vl-text] coord item[24]: text=患者于2025-12-25再次入院行第2周期治疗：注射用HLN601脂质体20.2mg静脉输液。治, bbox=[212, 434, 792, 447]
2026-08-10 17:32:48,101 INFO     29 [qwen-vl-text] coord item[25]: text=疗结束，准予出院。, bbox=[180, 448, 317, 461]
2026-08-10 17:32:48,101 INFO     29 [qwen-vl-text] coord item[26]: text=出院后患者复查血常规、肝肾功无明显异常，今为继续治疗入院。患者精神状态良好，, bbox=[212, 462, 790, 475]
2026-08-10 17:32:48,101 INFO     29 [qwen-vl-text] coord item[27]: text=食欲一般，睡眠良好，大小便正常，体力情况良好，体重较前无明显变化。, bbox=[185, 477, 684, 490]
2026-08-10 17:32:48,101 INFO     29 [qwen-vl-text] coord item[28]: text=补充病史：高脂血症（2024.12.uk-持续）, bbox=[215, 491, 493, 504]
2026-08-10 17:32:48,101 INFO     29 [qwen-vl-text] coord item[29]: text=补充合并用药：于2024.12.uk口服阿托伐他汀钙片 10mg qd 持续中，用药原因：治疗, bbox=[215, 505, 790, 518]
2026-08-10 17:32:48,101 INFO     29 [qwen-vl-text] coord item[30]: text=既往病史高脂血症（2024.12.uk-持续）。, bbox=[185, 520, 463, 533]
2026-08-10 17:32:48,101 INFO     29 [qwen-vl-text] coord item[31]: text=既往史：2021-10-15本院胸外科行“胸腔镜右肺上叶楔形切除术”，病理：右肺上, bbox=[215, 534, 798, 547]
2026-08-10 17:32:48,101 INFO     29 [qwen-vl-text] coord item[32]: text=叶：错构瘤。余参阅首次入院病历。, bbox=[185, 548, 424, 561]
2026-08-10 17:32:48,101 INFO     29 [qwen-vl-text] coord item[33]: text=个人史：参阅首次入院病历。, bbox=[215, 562, 410, 575]
2026-08-10 17:32:48,101 INFO     29 [qwen-vl-text] coord item[34]: text=家族史：参阅首次入院病历。, bbox=[215, 577, 410, 589]
2026-08-10 17:32:48,101 INFO     29 [qwen-vl-text] coord item[35]: text=第2页, bbox=[471, 604, 518, 615]
2026-08-10 17:32:48,102 INFO     29 [qwen-vl-text] page=2 — 36/36 coords, api_time=17.6s
2026-08-10 17:32:48,107 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1795160, prompt_len=1583
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["体格检查", "T 35.4℃", "P 108次/分", "R 20次/分", "Bp 137/90mmHg", "H 168cm", "W 86.1kg", "S 2.02m²", "NRS 0分", "发育正常，营养中等，正常面容，表情自如，自主体位，神志清楚，查体合作。全身皮肤粘膜无黄染，无皮疹，无皮下出血，无皮下结节，皮下无水肿，无肝掌、蜘蛛痣，毛发分布均匀。全身浅表淋巴结无肿大。眼睑无水肿，结膜无苍白，眼球无突出，无震颤，巩膜无黄染，瞳孔等大等圆，对光反射灵敏，耳廓对称，无畸形，牵拉无疼痛，外耳道无异常分泌物，乳突无压痛，无听力粗试障碍。鼻无畸形。口唇无发绀，口腔粘膜无充血、糜烂。舌苔薄白，伸舌无偏斜、震颤，牙龈无红肿，咽部粘膜无充血，扁桃体无肿大。颈软无抵抗，颈动脉无异常搏动，半坐位颈静脉未见充盈，颈部大血管区未闻及血管杂音。气管居中，肝颈静脉回流征阴性，甲状腺无肿大，无压痛、震颤、血管杂音。胸廓无畸形，呼吸运动两侧对称，肋间隙无狭窄或饱满，胸壁无压痛，语颤无增强、减弱，胸骨无压痛。双肺叩诊清音，呼吸规整，双肺呼吸音清晰，未闻及干湿性啰音，无胸膜摩擦音。心前区无异常隆起、异常搏动、震颤，心浊音界不大，心率108次/分，律齐，心音有力，各瓣膜听诊区未闻及杂音，无心包摩擦音。腹平坦，软，无压痛、反跳痛，腹部无包块。肝脏未触及，脾脏未触及，Murphy氏征阴性，肾区无叩击痛，无移动性浊音。肠鸣音正常，4次/分。肛门及外生殖器无异常。脊柱正常生理弯曲，四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾），关节无肿胀、压痛，下肢无水肿。", "肌肉无压痛，四肢肌力、肌张力未见异常，双侧肱", "二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性。", "专科检查： ECOG 1分。浅表淋巴结未及肿大。胸壁、腹部可见手术瘢痕(CS病史)，愈合可。", "辅助检查", "2025-11-19 病理：EBUS组织：送检组织内见腺癌，伴大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS刷片）查见肿瘤细胞。本院。", "初步诊断：", "1.直肠中分化腺癌术后（pT2N1bM0 IIIA", "→IV期）", "左锁骨区、纵膈、右侧肺门区淋巴", "结转移", "左肾上腺转移", "第3页"]

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
2026-08-10 17:32:58,939 INFO     29 [qwen-vl-text] coord API raw response (len=1874):
[
	{"text": "体格检查", "bbox": [439, 93, 551, 107]},
	{"text": "T 35.4℃", "bbox": [221, 107, 293, 119]},
	{"text": "P 108次/分", "bbox": [332, 107, 427, 119]},
	{"text": "R 20次/分", "bbox": [468, 107, 554, 119]},
	{"text": "Bp 137/90mmHg", "bbox": [604, 109, 714, 121]},
	{"text": "H 168cm", "bbox": [221, 121, 287, 133]},
	{"text": "W 86.1kg", "bbox": [332, 121, 405, 134]},
	{"text": "S 2.02m²", "bbox": [468, 121, 539, 134]},
	{"text": "NRS 0分", "bbox": [604, 123, 667, 135]},
	{"text": "发育正常，营养中等，正常面容，表情自如，自主体位，神志清楚，查体合作。全身皮肤粘膜无黄染，无皮疹，无皮下出血，无皮下结节，皮下无水肿，无肝掌、蜘蛛痣，毛发分布均匀。全身浅表淋巴结无肿大。眼睑无水肿，结膜无苍白，眼球无突出，无震颤，巩膜无黄染，瞳孔等大等圆，对光反射灵敏，耳廓对称，无畸形，牵拉无疼痛，外耳道无异常分泌物，乳突无压痛，无听力粗试障碍。鼻无畸形。口唇无发绀，口腔粘膜无充血、糜烂。舌苔薄白，伸舌无偏斜、震颤，牙龈无红肿，咽部粘膜无充血，扁桃体无肿大。颈软无抵抗，颈动脉无异常搏动，半坐位颈静脉未见充盈，颈部大血管区未闻及血管杂音。气管居中，肝颈静脉回流征阴性，甲状腺无肿大，无压痛、震颤、血管杂音。胸廓无畸形，呼吸运动两侧对称，肋间隙无狭窄或饱满，胸壁无压痛，语颤无增强、减弱，胸骨无压痛。双肺叩诊清音，呼吸规整，双肺呼吸音清晰，未闻及干湿性啰音，无胸膜摩擦音。心前区无异常隆起、异常搏动、震颤，心浊音界不大，心率108次/分，律齐，心音有力，各瓣膜听诊区未闻及杂音，无心包摩擦音。腹平坦，软，无压痛、反跳痛，腹部无包块。肝脏未触及，脾脏未触及，Murphy氏征阴性，肾区无叩击痛，无移动性浊音。肠鸣音正常，4次/分。肛门及外生殖器无异常。脊柱正常生理弯曲，四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾），关节无肿胀、压痛，下肢无水肿。", "bbox": [184, 137, 808, 355]},
	{"text": "肌肉无压痛，四肢肌力、肌张力未见异常，双侧肱", "bbox": [461, 342, 800, 355]},
	{"text": "二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性。", "bbox": [184, 356, 671, 369]},
	{"text": "专科检查： ECOG 1分。浅表淋巴结未及肿大。胸壁、腹部可见手术瘢痕(CS病史)，愈合可。", "bbox": [184, 370, 802, 396]},
	{"text": "辅助检查", "bbox": [439, 412, 548, 425]},
	{"text": "2025-11-19 病理：EBUS组织：送检组织内见腺癌，伴大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS刷片）查见肿瘤细胞。本院。", "bbox": [184, 442, 800, 468]},
	{"text": "初步诊断：", "bbox": [495, 512, 562, 524]},
	{"text": "1.直肠中分化腺癌术后（pT2N1bM0 IIIA", "bbox": [511, 526, 774, 538]},
	{"text": "→IV期）", "bbox": [495, 540, 549, 552]},
	{"text": "左锁骨区、纵膈、右侧肺门区淋巴", "bbox": [541, 554, 766, 567]},
	{"text": "结转移", "bbox": [495, 569, 540, 581]},
	{"text": "左肾上腺转移", "bbox": [541, 583, 630, 595]},
	{"text": "第3页", "bbox": [473, 610, 520, 621]}
]
2026-08-10 17:32:58,939 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=10.8s
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[0]: text=体格检查, bbox=[439, 93, 551, 107]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[1]: text=T 35.4℃, bbox=[221, 107, 293, 119]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[2]: text=P 108次/分, bbox=[332, 107, 427, 119]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[3]: text=R 20次/分, bbox=[468, 107, 554, 119]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[4]: text=Bp 137/90mmHg, bbox=[604, 109, 714, 121]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[5]: text=H 168cm, bbox=[221, 121, 287, 133]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[6]: text=W 86.1kg, bbox=[332, 121, 405, 134]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[7]: text=S 2.02m², bbox=[468, 121, 539, 134]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[8]: text=NRS 0分, bbox=[604, 123, 667, 135]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[9]: text=发育正常，营养中等，正常面容，表情自如，自主体位，神志清楚，查体合作。全身皮肤粘膜无黄染，无皮疹，无皮下出血，无皮下结节，皮下无水肿，无肝掌、蜘蛛痣，毛发分布均匀。全身浅表淋巴结无肿大。眼睑无水肿，结膜无苍白，眼球无突出，无震颤，巩膜无黄染，瞳孔等大等圆，对光反射灵敏，耳廓对称，无畸形，牵拉无疼痛，外耳道无异常分泌物，乳突无压痛，无听力粗试障碍。鼻无畸形。口唇无发绀，口腔粘膜无充血、糜烂。舌苔薄白，伸舌无偏斜、震颤，牙龈无红肿，咽部粘膜无充血，扁桃体无肿大。颈软无抵抗，颈动脉无异常搏动，半坐位颈静脉未见充盈，颈部大血管区未闻及血管杂音。气管居中，肝颈静脉回流征阴性，甲状腺无肿大，无压痛、震颤、血管杂音。胸廓无畸形，呼吸运动两侧对称，肋间隙无狭窄或饱满，胸壁无压痛，语颤无增强、减弱，胸骨无压痛。双肺叩诊清音，呼吸规整，双肺呼吸音清晰，未闻及干湿性啰音，无胸膜摩擦音。心前区无异常隆起、异常搏动、震颤，心浊音界不大，心率108次/分，律齐，心音有力，各瓣膜听诊区未闻及杂音，无心包摩擦音。腹平坦，软，无压痛、反跳痛，腹部无包块。肝脏未触及，脾脏未触及，Murphy氏征阴性，肾区无叩击痛，无移动性浊音。肠鸣音正常，4次/分。肛门及外生殖器无异常。脊柱正常生理弯曲，四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾），关节无肿胀、压痛，下肢无水肿。, bbox=[184, 137, 808, 355]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[10]: text=肌肉无压痛，四肢肌力、肌张力未见异常，双侧肱, bbox=[461, 342, 800, 355]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[11]: text=二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性。, bbox=[184, 356, 671, 369]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[12]: text=专科检查： ECOG 1分。浅表淋巴结未及肿大。胸壁、腹部可见手术瘢痕(CS病史)，愈合可。, bbox=[184, 370, 802, 396]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[13]: text=辅助检查, bbox=[439, 412, 548, 425]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[14]: text=2025-11-19 病理：EBUS组织：送检组织内见腺癌，伴大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS刷片）查见肿瘤细胞。本院。, bbox=[184, 442, 800, 468]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[15]: text=初步诊断：, bbox=[495, 512, 562, 524]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[16]: text=1.直肠中分化腺癌术后（pT2N1bM0 IIIA, bbox=[511, 526, 774, 538]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[17]: text=→IV期）, bbox=[495, 540, 549, 552]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[18]: text=左锁骨区、纵膈、右侧肺门区淋巴, bbox=[541, 554, 766, 567]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[19]: text=结转移, bbox=[495, 569, 540, 581]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[20]: text=左肾上腺转移, bbox=[541, 583, 630, 595]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] coord item[21]: text=第3页, bbox=[473, 610, 520, 621]
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] page=3 — 22/22 coords, api_time=10.8s
2026-08-10 17:32:58,940 INFO     29 [qwen-vl-text] new_positions (102):
[[0, 101.7921961669922, 186.91666430664063, 196.16037341308595, 208.7887236328125], [0, 101.7921961669922, 198.82218432617188, 208.7887236328125, 220.57518383789062], [0, 101.7921961669922, 174.41586828613282, 220.57518383789062, 232.36164404296875], [0, 101.7921961669922, 330.3781805419922, 232.36164404296875, 244.14810424804688], [0, 101.7921961669922, 378.59553662109374, 244.14810424804688, 256.7764544677734], [0, 101.7921961669922, 198.82218432617188, 256.7764544677734, 268.56291467285155], [0, 101.7921961669922, 474.43497277832034, 268.56291467285155, 281.19126489257815], [1, 124.41769744873048, 160.73099670410156, 81.66430236816406, 92.60900268554688], [1, 292.2922940063477, 337.5350930786133, 81.66430236816406, 92.60900268554688], [1, 124.41769744873048, 169.6604965209961, 93.45090270996094, 104.39560302734375], [1, 292.2922940063477, 410.7569915771485, 93.45090270996094, 104.39560302734375], [1, 124.41769744873048, 169.6604965209961, 105.23750305175781, 116.18220336914062], [1, 292.2922940063477, 410.7569915771485, 105.23750305175781, 116.18220336914062], [1, 124.41769744873048, 188.11479614257814, 117.0241033935547, 127.96880371093751], [1, 292.2922940063477, 410.7569915771485, 117.0241033935547, 127.96880371093751], [1, 124.41769744873048, 319.67609344482423, 128.81070373535158, 139.75540405273438], [1, 107.15399780273438, 468.5010903930664, 140.59730407714844, 151.54200439453126], [1, 107.15399780273438, 468.5010903930664, 164.1705047607422, 175.115205078125], [1, 107.15399780273438, 468.5010903930664, 175.95710510253906, 186.90180541992189], [1, 107.15399780273438, 468.5010903930664, 187.74370544433594, 198.68840576171877], [1, 107.15399780273438, 468.5010903930664, 199.53030578613283, 210.47500610351562], [1, 107.15399780273438, 367.8953924560547, 211.31690612792968, 222.2616064453125], [1, 124.41769744873048, 468.5010903930664, 223.10350646972657, 234.0482067871094], [1, 107.15399780273438, 468.5010903930664, 235.7320068359375, 246.6767071533203], [1, 107.15399780273438, 468.5010903930664, 247.5186071777344, 258.4633074951172], [1, 107.15399780273438, 468.5010903930664, 259.3052075195313, 270.2499078369141], [1, 107.15399780273438, 468.5010903930664, 271.0918078613281, 282.03650817871096], [1, 107.15399780273438, 468.5010903930664, 282.878408203125, 293.82310852050784], [1, 107.15399780273438, 468.5010903930664, 294.6650085449219, 305.6097088623047], [1, 107.15399780273438, 468.5010903930664, 306.45160888671876, 317.39630920410156], [1, 107.15399780273438, 468.5010903930664, 318.23820922851564, 329.18290954589844], [1, 107.15399780273438, 468.5010903930664, 330.0248095703125, 340.9695098876953], [1, 107.15399780273438, 468.5010903930664, 341.8114099121094, 352.7561102294922], [1, 107.15399780273438, 468.5010903930664, 353.59801025390624, 364.5427105712891], [1, 107.15399780273438, 468.5010903930664, 365.3846105957031, 376.329310913086], [1, 107.15399780273438, 468.5010903930664, 377.1712109375, 388.1159112548828], [1, 107.15399780273438, 468.5010903930664, 388.9578112792969, 399.9025115966797], [1, 107.15399780273438, 468.5010903930664, 400.7444116210938, 411.6891119384766], [1, 107.15399780273438, 468.5010903930664, 412.53101196289066, 423.47571228027346], [1, 107.15399780273438, 468.5010903930664, 424.31761230468754, 435.26231262207034], [1, 107.15399780273438, 468.5010903930664, 436.10421264648437, 447.0489129638672], [1, 107.15399780273438, 468.5010903930664, 447.89081298828125, 458.83551330566405], [1, 107.15399780273438, 468.5010903930664, 459.67741333007814, 470.62211364746094], [1, 273.83799438476564, 302.41239379882813, 484.09251403808594, 493.3534143066406], [2, 107.15399780273438, 186.9241961669922, 72.40340209960938, 83.34810241699219], [2, 126.20359741210937, 474.4540902709961, 84.19000244140625, 95.13470275878906], [2, 107.15399780273438, 283.9580941772461, 96.8185028076172, 107.763203125], [2, 126.20359741210937, 469.69169036865236, 109.44700317382812, 119.54980346679687], [2, 107.15399780273438, 478.6211901855469, 121.233603515625, 132.17830383300782], [2, 107.15399780273438, 478.6211901855469, 133.02020385742188, 143.9649041748047], [2, 107.15399780273438, 122.0364974975586, 145.64870422363282, 156.59340454101564], [2, 126.20359741210937, 478.02589019775394, 157.4353045654297, 168.3800048828125], [2, 107.15399780273438, 473.8587902832031, 170.06380493164062, 181.00850524902344], [2, 107.15399780273438, 478.02589019775394, 181.8504052734375, 192.79510559082033], [2, 107.15399780273438, 467.3104904174805, 194.47890563964845, 205.42360595703127], [2, 107.15399780273438, 473.2634902954102, 206.26550598144533, 217.21020629882813], [2, 107.15399780273438, 477.43059020996094, 218.89400634765624, 229.83870666503907], [2, 107.15399780273438, 472.6681903076172, 230.68060668945313, 241.62530700683595], [2, 107.15399780273438, 468.5010903930664, 243.30910705566407, 254.2538073730469], [2, 107.15399780273438, 463.73869049072266, 255.09570739746096, 266.04040771484375], [2, 107.15399780273438, 472.6681903076172, 267.72420776367187, 278.6689080810547], [2, 107.15399780273438, 472.6681903076172, 279.51080810546875, 290.45550842285155], [2, 107.15399780273438, 472.6681903076172, 292.1393084716797, 303.0840087890625], [2, 107.15399780273438, 476.835290222168, 303.92590881347655, 314.8706091308594], [2, 107.15399780273438, 132.15659729003906, 316.5544091796875, 327.4991094970703], [2, 126.20359741210937, 476.239990234375, 328.3410095214844, 339.2857098388672], [2, 107.15399780273438, 467.3104904174805, 340.9695098876953, 351.9142102050781], [2, 107.15399780273438, 370.2765924072266, 352.7561102294922, 363.700810546875], [2, 126.20359741210937, 471.4775903320313, 365.3846105957031, 376.329310913086], [2, 107.15399780273438, 188.7100961303711, 377.1712109375, 388.1159112548828], [2, 126.20359741210937, 470.28699035644536, 388.9578112792969, 399.9025115966797], [2, 110.13049774169923, 407.18519165039066, 401.5863116455078, 412.53101196289066], [2, 127.98949737548828, 293.4828939819336, 413.3729119873047, 424.31761230468754], [2, 127.98949737548828, 470.28699035644536, 425.1595123291016, 436.10421264648437], [2, 110.13049774169923, 275.6238943481445, 437.7880126953125, 448.73271301269534], [2, 127.98949737548828, 475.04939025878906, 449.5746130371094, 460.5193133544922], [2, 110.13049774169923, 252.40719482421875, 461.36121337890626, 472.30591369628905], [2, 127.98949737548828, 244.0729949951172, 473.14781372070314, 484.09251403808594], [2, 127.98949737548828, 244.0729949951172, 485.77631408691406, 495.8791143798828], [2, 280.3862942504883, 308.36539367675783, 508.5076147460938, 517.7685150146484], [3, 261.3366946411133, 328.0102932739258, 78.29670227050782, 90.08330261230469], [3, 131.5612973022461, 174.42289642333986, 90.08330261230469, 100.18610290527344], [3, 197.63959594726563, 254.19309478759766, 90.08330261230469, 100.18610290527344], [3, 278.6003942871094, 329.7961932373047, 90.08330261230469, 100.18610290527344], [3, 359.56119262695313, 425.0441912841797, 91.76710266113281, 101.86990295410156], [3, 131.5612973022461, 170.85109649658204, 101.86990295410156, 111.97270324707031], [3, 197.63959594726563, 241.09649505615235, 101.86990295410156, 112.81460327148437], [3, 278.6003942871094, 320.8666934204102, 101.86990295410156, 112.81460327148437], [3, 359.56119262695313, 397.06509185791015, 103.5537030029297, 113.65650329589845], [3, 109.53519775390626, 481.00239013671876, 115.34030334472656, 298.8745086669922], [3, 274.4332943725586, 476.239990234375, 287.9298083496094, 298.8745086669922], [3, 109.53519775390626, 399.446291809082, 299.7164086914063, 310.6611090087891], [3, 109.53519775390626, 477.43059020996094, 311.5030090332031, 333.39240966796876], [3, 261.3366946411133, 326.2243933105469, 346.86281005859377, 357.80751037597656], [3, 109.53519775390626, 476.239990234375, 372.11981079101565, 394.00921142578125], [3, 294.67349395751955, 334.55859313964845, 431.0528125, 441.1556127929688], [3, 304.1982937622071, 460.76219055175784, 442.8394128417969, 452.94221313476567], [3, 294.67349395751955, 326.81969329833987, 454.6260131835938, 464.7288134765625], [3, 322.0572933959961, 455.9997906494141, 466.41261352539067, 477.35731384277346], [3, 294.67349395751955, 321.4619934082031, 479.0411138916016, 489.14391418457035], [3, 322.0572933959961, 375.03899230957035, 490.82771423339847, 500.93051452636723], [3, 281.5768942260742, 309.5559936523438, 513.5590148925781, 522.8199151611328]]
2026-08-10 17:32:58,941 INFO     29 [qwen-vl-text] ═══ DONE ═══ 102 positions, pages=4, time=77.0s
2026-08-10 17:32:58,955 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 17:32:58,955 INFO     29 [Trace] task=df5ff51c | doc=06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf | Extractor:Admission | outputs={"chunks": "1 items, types={'AdmissionRecord': 1}", "html": "", "json": "476 items", "markdown": "", "text": "", "name": "06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 2, \"chunks_Clinical\": 1}"}
2026-08-10 17:32:58,955 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 17:32:58,956 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:32:58.955+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 81, "failed": 0, "current": {"df5ff51c94e011f1bd9827cf206dfa2d": {"id": "df5ff51c94e011f1bd9827cf206dfa2d", "doc_id": "df229e1a94e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 3352826, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786382896642, "task_type": "dataflow", "root_trace_id": "02e835c46e184d6daf27401b2b0ac85a", "root_traceparent": "00-02e835c46e184d6daf27401b2b0ac85a-ddd202d54b80a7dd-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:32:58,966 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:32:58,967 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:32:58,967 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 17:32:58,967 INFO     29 [qwen-vl-text] positions(59): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:32:58,967 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [59]
2026-08-10 17:32:59,193 INFO     29 [qwen-vl-text] page=5, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 17:32:59,194 INFO     29 [qwen-vl-text] LLM extraction start, text_len=912
2026-08-10 17:32:59,194 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:32:59,195 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 117, \"bbox_end\": 175, \"encounter_dates\": [\"2024-05-31\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "检测项目：K-RAS、N-ras、Braf基因突变检测\n检测方法： ARMS 荧光定量 PCR\n样本类型：石蜡包埋组织\n质量控制：标本量：30%\nDNA 抽提方法：AmoyDx FFPE DNA Kit\n信号：合格\n试剂信息：K-RAS、N-ras、Braf 基因肿瘤相关\nDNA 质量：合格\n基因突变检测试剂盒\n阳性、阴性对照：合格\n检测结果：\n检测项目\n外显子/密码子\n突变类型\n检测结果\nKRAS Exon-2\nG12S,G12D\n阴性\nKRAS Exon-2\nG12C,G12R,G12V,G12A,G13C\n阴性\nKRAS Exon-2\nG13D\n阴性\nKRAS Exon-3\nQ61L,Q61R,Q61H,183A>C,Q61H,183A>T\n阴性\nKRAS Exon-4\nK117N(351A>T),K117N(351A>C),A146T,A146V,A146P\n阴性\nKNB 基因突变联\n合检测\nNRAS Exon-2\nG12D,G12S\n阳性\nNRAS Exon-2\nG13D\n阴性\nNRAS Exon-2\nG13R,G12C,G12V,G12A,G13V\n阴性\nNRAS Exon-3\nQ61R,Q61K,Q61L,Q61H\n阴性\nNRAS Exon-4\nA146T\n阴性\nBRAF Exon-15\nV600E1,V600K,V600E2,V600R,V600D1,V600D2\n阴性\n检测结论：\nN-ras 基因突变;K-ras、Braf 基因均未突变。\n注：(1) 分子病理检测结果与样本的收集、处理及核酸质量等有关，本报告针对本次检测样本，不一定能反映病变全貌，\n仅供临床医师参考，不能作为临床诊断和治疗的唯一依据，具体治疗方案还需临床医师根据临床情况综合判断进行制定。(2) 分\n子检测结果阴性时，不排除样本质量，未知基因异常，及极低丰度突变等原因。(3) 该检测不承担受检者检测后所产生的心理上、\n法律上及检测结果应用上等方面的任何后果，本检测报告解释权归本检测实验室所有。如有不符或疑问请及时与我们联系\n0535-6691999-83445.\n报告医师签章：\n报告日期： 2024/05/31",
    "role": "user"
  }
]
2026-08-10 17:33:06,013 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:33:06,013 INFO     29 [qwen-vl-text] LLM output (len=1350):
{
  "exam_date": null,
  "report_date": "2024-05-31",
  "exam_name": "K-RAS、N-ras、Braf基因突变检测",
  "exam_category": "pathology",
  "body_part": "石蜡包埋组织",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "检测项目：K-RAS、N-ras、Braf基因突变检测\n检测方法： ARMS 荧光定量 PCR\n样本类型：石蜡包埋组织\n质量控制：标本量：30%\nDNA 抽提方法：AmoyDx FFPE DNA Kit\n信号：合格\n试剂信息：K-RAS、N-ras、Braf 基因肿瘤相关\nDNA 质量：合格\n基因突变检测试剂盒\n阳性、阴性对照：合格\n检测结果：\n| 检测项目 | 外显子/密码子 | 突变类型 | 检测结果 |\n|---|---|---|---|\n| KRAS Exon-2 | G12S,G12D | 阴性 |\n| KRAS Exon-2 | G12C,G12R,G12V,G12A,G13C | 阴性 |\n| KRAS Exon-2 | G13D | 阴性 |\n| KRAS Exon-3 | Q61L,Q61R,Q61H,183A>C,Q61H,183A>T | 阴性 |\n| KRAS Exon-4 | K117N(351A>T),K117N(351A>C),A146T,A146V,A146P | 阴性 |\n| KNB 基因突变联合检测 | NRAS Exon-2 | G12D,G12S | 阳性 |\n| NRAS Exon-2 | G13D | 阴性 |\n| NRAS Exon-2 | G13R,G12C,G12V,G12A,G13V | 阴性 |\n| NRAS Exon-3 | Q61R,Q61K,Q61L,Q61H | 阴性 |\n| NRAS Exon-4 | A146T | 阴性 |\n| BRAF Exon-15 | V600E1,V600K,V600E2,V600R,V600D1,V600D2 | 阴性 |",
  "conclusion": "检测结论：\nN-ras 基因突变;K-ras、Braf 基因均未突变。\n注：(1) 分子病理检测结果与样本的收集、处理及核酸质量等有关，本报告针对本次检测样本，不一定能反映病变全貌，仅供临床医师参考，不能作为临床诊断和治疗的唯一依据，具体治疗方案还需临床医师根据临床情况综合判断进行制定。(2) 分子检测结果阴性时，不排除样本质量，未知基因异常，及极低丰度突变等原因。(3) 该检测不承担受检者检测后所产生的心理上、法律上及检测结果应用上等方面的任何后果，本检测报告解释权归本检测实验室所有。如有不符或疑问请及时与我们联系 0535-6691999-83445.",
  "physician": null,
  "reviewer": null
}
2026-08-10 17:33:06,025 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3840005, prompt_len=1702
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共59行）
["检测项目：K-RAS、N-ras、Braf基因突变检测", "检测方法： ARMS 荧光定量 PCR", "样本类型：石蜡包埋组织", "质量控制：标本量：30%", "DNA 抽提方法：AmoyDx FFPE DNA Kit", "信号：合格", "试剂信息：K-RAS、N-ras、Braf 基因肿瘤相关", "DNA 质量：合格", "基因突变检测试剂盒", "阳性、阴性对照：合格", "检测结果：", "检测项目", "外显子/密码子", "突变类型", "检测结果", "KRAS Exon-2", "G12S,G12D", "阴性", "KRAS Exon-2", "G12C,G12R,G12V,G12A,G13C", "阴性", "KRAS Exon-2", "G13D", "阴性", "KRAS Exon-3", "Q61L,Q61R,Q61H,183A>C,Q61H,183A>T", "阴性", "KRAS Exon-4", "K117N(351A>T),K117N(351A>C),A146T,A146V,A146P", "阴性", "KNB 基因突变联", "合检测", "NRAS Exon-2", "G12D,G12S", "阳性", "NRAS Exon-2", "G13D", "阴性", "NRAS Exon-2", "G13R,G12C,G12V,G12A,G13V", "阴性", "NRAS Exon-3", "Q61R,Q61K,Q61L,Q61H", "阴性", "NRAS Exon-4", "A146T", "阴性", "BRAF Exon-15", "V600E1,V600K,V600E2,V600R,V600D1,V600D2", "阴性", "检测结论：", "N-ras 基因突变;K-ras、Braf 基因均未突变。", "注：(1) 分子病理检测结果与样本的收集、处理及核酸质量等有关，本报告针对本次检测样本，不一定能反映病变全貌，", "仅供临床医师参考，不能作为临床诊断和治疗的唯一依据，具体治疗方案还需临床医师根据临床情况综合判断进行制定。(2) 分", "子检测结果阴性时，不排除样本质量，未知基因异常，及极低丰度突变等原因。(3) 该检测不承担受检者检测后所产生的心理上、", "法律上及检测结果应用上等方面的任何后果，本检测报告解释权归本检测实验室所有。如有不符或疑问请及时与我们联系", "0535-6691999-83445.", "报告医师签章：", "报告日期： 2024/05/31"]

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
2026-08-10 17:33:54,673 INFO     29 [qwen-vl-text] coord API raw response (len=9222):
[
	{"text": "检测项目：K-RAS、N-ras、Braf基因突变检测", "bbox": [204, 93, 472, 105]}, "bbox": [496, 93, 562, 105]},
	{"text": "检测方法： ARMS 荧光定量 PCR", "bbox": [496, 93, 705, 105]},
	{"text": "样本类型：石蜡包埋组织", "bbox": [204, 108, 371, 120]},
	{"text": "质量控制：标本量：30%", "bbox": [496, 108, 675, 120]},
	{"text": "DNA 抽提方法：AmoyDx FFPE DNA Kit", "bbox": [204, 124, 432, 136]},
	{"text": "信号：合格", "bbox": [585, 121, 674, 133]},
	{"text": "试剂信息：K-RAS、N-ras、Braf 基因肿瘤相关", "bbox": [204, 139, 485, 151]},
	{"text": "DNA 质量：合格", "bbox": [585, 135, 695, 147]},
	{"text": "基因突变检测试剂盒", "bbox": [280, 153, 398, 165]},
	{"text": "阳性、阴性对照：合格", "bbox": [585, 149, 732, 161]},
	{"text": "检测结果：", "bbox": [204, 167, 272, 179]},
	{"text": "检测项目", "bbox": [218, 200, 264, 210]},
	{"text": "外显子/密码子", "bbox": [321, 200, 395, 210]},
	{"text": "突变类型", "bbox": [420, 200, 465, 210]},
	{"text": "检测结果", "bbox": [693, 200, 737, 210]},
	{"text": "KRAS Exon-2", "bbox": [321, 225, 392, 234]},
	{"text": "G12S,G12D", "bbox": [420, 225, 477, 234]},
	{"text": "阴性", "bbox": [693, 225, 715, 234]},
	{"text": "KRAS Exon-2", "bbox": [321, 240, 392, 248]},
	{"text": "G12C,G12R,G12V,G12A,G13C", "bbox": [420, 240, 567, 248]},
	{"text": "阴性", "bbox": [693, 240, 715, 248]},
	{"text": "KRAS Exon-2", "bbox": [321, 253, 392, 262]},
	{"text": "G13D", "bbox": [420, 253, 450, 262]},
	{"text": "阴性", "bbox": [693, 253, 715, 262]},
	{"text": "KRAS Exon-3", "bbox": [321, 267, 392, 276]},
	{"text": "Q61L,Q61R,Q61H,183A>C,Q61H,183A>T", "bbox": [420, 267, 629, 276]},
	{"text": "阴性", "bbox": [693, 267, 715, 276]},
	{"text": "KRAS Exon-4", "bbox": [321, 281, 392, 290]},
	{"text": "K117N(351A>T),K117N(351A>C),A146T,A146V,A146P", "bbox": [420, 281, 679, 290]},
	{"text": "阴性", "bbox": [693, 281, 715, 290]},
	{"text": "KNB 基因突变联", "bbox": [221, 288, 311, 297]},
	{"text": "合检测", "bbox": [221, 301, 256, 310]},
	{"text": "NRAS Exon-2", "bbox": [321, 295, 392, 304]},
	{"text": "G12D,G12S", "bbox": [420, 295, 478, 304]},
	{"text": "阳性", "bbox": [693, 295, 715, 304]},
	{"text": "NRAS Exon-2", "bbox": [321, 308, 392, 317]},
	{"text": "G13D", "bbox": [420, 308, 450, 317]},
	{"text": "阴性", "bbox": [693, 308, 715, 317]},
	{"text": "NRAS Exon-2", "bbox": [321, 322, 392, 331]},
	{"text": "G13R,G12C,G12V,G12A,G13V", "bbox": [420, 322, 573, 331]},
	{"text": "阴性", "bbox": [693, 322, 715, 331]},
	{"text": "NRAS Exon-3", "bbox": [321, 336, 392, 345]},
	{"text": "Q61R,Q61K,Q61L,Q61H", "bbox": [420, 336, 540, 345]},
	{"text": "阴性", "bbox": [693, 336, 715, 345]},
	{"text": "NRAS Exon-4", "bbox": [321, 350, 392, 359]},
	{"text": "A146T", "bbox": [420, 350, 455, 359]},
	{"text": "阴性", "bbox": [693, 350, 715, 359]},
	{"text": "BRAF Exon-15", "bbox": [321, 363, 398, 372]},
	{"text": "V600E1,V600K,V600E2,V600R,V600D1,V600D2", "bbox": [420, 363, 659, 372]},
	{"text": "阴性", "bbox": [693, 363, 715, 372]},
	{"text": "检测结论：", "bbox": [212, 380, 293, 395]},
	{"text": "N-ras 基因突变;K-ras、Braf 基因均未突变。", "bbox": [332, 380, 664, 395]},
	{"text": "注：(1) 分子病理检测结果与样本的收集、处理及核酸质量等有关，本报告针对本次检测样本，不一定能反映病变全貌，", "bbox": [240, 401, 763, 411]},
	{"text": "仅供临床医师参考，不能作为临床诊断和治疗的唯一依据，具体治疗方案还需临床医师根据临床情况综合判断进行制定。(2) 分", "bbox": [213, 414, 767, 424]},
	{"text": "子检测结果阴性时，不排除样本质量，未知基因异常，及极低丰度突变等原因。(3) 该检测不承担受检者检测后所产生的心理上、", "bbox": [213, 427, 767, 437]},
	{"text": "法律上及检测结果应用上等方面的任何后果，本检测报告解释权归本检测实验室所有。如有不符或疑问请及时与我们联系", "bbox": [213, 440, 740, 450]},
	{"text": "0535-6691999-83445.", "bbox": [213, 455, 306, 464]},
	{"text": "报告医师签章：", "bbox": [496, 466, 588, 478]},
	{"text": "报告日期： 2024/05/31", "bbox": [496, 541, 647, 553]},
	{"text": "项目名称", "bbox": [190, 574, 236, 583]},
	{"text": "结果", "bbox": [311, 574, 334, 583]},
	{"text": "单位", "bbox": [364, 574, 387, 583]},
	{"text": "参考范围", "bbox": [418, 574, 463, 583]},
	{"text": "项目名称", "bbox": [510, 574, 554, 583]},
	{"text": "结果", "bbox": [627, 574, 650, 583]},
	{"text": "单位", "bbox": [680, 574, 702, 583]},
	{"text": "参考区间", "bbox": [733, 574, 776, 583]},
	{"text": "*★红细胞", "bbox": [192, 591, 250, 600]},
	{"text": "4.20", "bbox": [311, 591, 338, 600]},
	{"text": "x10^12/L", "bbox": [366, 591, 413, 600]},
	{"text": "4.30-5.80", "bbox": [418, 591, 477, 600]},
	{"text": "↓", "bbox": [490, 591, 496, 600]},
	{"text": "*★白细胞", "bbox": [509, 591, 564, 600]},
	{"text": "4.59", "bbox": [625, 591, 651, 600]},
	{"text": "×10^9/L", "bbox": [680, 591, 727, 600]},
	{"text": "3.50-9.50", "bbox": [730, 591, 785, 600]},
	{"text": "*★血红蛋白", "bbox": [192, 603, 262, 612]},
	{"text": "145", "bbox": [311, 603, 331, 612]},
	{"text": "g/L", "bbox": [366, 603, 385, 612]},
	{"text": "130-175", "bbox": [418, 603, 465, 612]},
	{"text": "中性粒细胞百分率", "bbox": [509, 603, 607, 612]},
	{"text": "62.1", "bbox": [625, 603, 651, 612]},
	{"text": "%", "bbox": [680, 603, 688, 612]},
	{"text": "40.0-75.0", "bbox": [730, 603, 785, 612]},
	{"text": "*★红细胞压积", "bbox": [192, 614, 274, 623]},
	{"text": "44.0", "bbox": [311, 614, 338, 623]},
	{"text": "%", "bbox": [366, 614, 374, 623]},
	{"text": "40.0-50.0", "bbox": [418, 614, 477, 623]},
	{"text": "淋巴细胞百分率", "bbox": [509, 614, 595, 623]},
	{"text": "24.6", "bbox": [625, 614, 651, 623]},
	{"text": "%", "bbox": [680, 614, 688, 623]},
	{"text": "20.0-50.0", "bbox": [730, 614, 785, 623]},
	{"text": "*平均红细胞体积", "bbox": [192, 625, 287, 634]},
	{"text": "104.8", "bbox": [311, 625, 344, 634]},
	{"text": "fL", "bbox": [366, 625, 378, 634]},
	{"text": "82.0-100.0", "bbox": [418, 625, 485, 634]},
	{"text": "↑", "bbox": [490, 625, 496, 634]},
	{"text": "单核细胞百分率", "bbox": [509, 625, 595, 634]},
	{"text": "10.0", "bbox": [625, 625, 651, 634]},
	{"text": "%", "bbox": [680, 625, 688, 634]},
	{"text": "3.0-10.0", "bbox": [730, 625, 785, 634]},
	{"text": "*平均血红蛋白量", "bbox": [192, 637, 287, 646]},
	{"text": "34.5", "bbox": [311, 637, 338, 646]},
	{"text": "pg", "bbox": [366, 637, 379, 646]},
	{"text": "27.0-34.0", "bbox": [418, 637, 477, 646]},
	{"text": "↑", "bbox": [490, 637, 496, 646]},
	{"text": "嗜酸细胞百分率", "bbox": [509, 637, 595, 646]},
	{"text": "2.4", "bbox": [625, 637, 651, 646]},
	{"text": "%", "bbox": [680, 637, 688, 646]},
	{"text": "0.4-8.0", "bbox": [730, 637, 785, 646]},
	{"text": "*平均血红蛋白浓度", "bbox": [192, 648, 298, 657]},
	{"text": "330", "bbox": [311, 648, 331, 657]},
	{"text": "g/L", "bbox": [366, 648, 385, 657]},
	{"text": "316-354", "bbox": [418, 648, 465, 657]},
	{"text": "嗜碱细胞百分率", "bbox": [509, 648, 595, 657]},
	{"text": "0.9", "bbox": [625, 648, 651, 657]},
	{"text": "%", "bbox": [680, 648, 688, 657]},
	{"text": "0.0-1.0", "bbox": [730, 648, 785, 657]},
	{"text": "红细胞分布宽度SD", "bbox": [190, 660, 293, 669]},
	{"text": "55.1", "bbox": [311, 660, 338, 669]},
	{"text": "f1", "bbox": [366, 660, 378, 669]},
	{"text": "39.0-46.0", "bbox": [418, 660, 477, 669]},
	{"text": "↑", "bbox": [490, 660, 496, 669]},
	{"text": "中性粒细胞绝对值", "bbox": [509, 660, 607, 669]},
	{"text": "2.85", "bbox": [625, 660, 651, 669]},
	{"text": "×10^9/L", "bbox": [680, 660, 727, 669]},
	{"text": "1.80-6.30", "bbox": [730, 660, 785, 669]},
	{"text": "红细胞分布宽度CV", "bbox": [190, 671, 293, 680]},
	{"text": "14.2", "bbox": [311, 671, 338, 680]},
	{"text": "%", "bbox": [366, 671, 378, 680]},
	{"text": "10.9-14.5", "bbox": [418, 671, 477, 680]},
	{"text": "淋巴细胞绝对值", "bbox": [509, 671, 595, 680]},
	{"text": "1.13", "bbox": [625, 671, 651, 680]},
	{"text": "×10^9/L", "bbox": [680, 671, 727, 680]},
	{"text": "1.10-3.20", "bbox": [730, 671, 785, 680]},
	{"text": "*★血小板总数", "bbox": [190, 683, 272, 692]},
	{"text": "166", "bbox": [311, 683, 331, 692]},
	{"text": "×10^9/L", "bbox": [366, 683, 413, 692]},
	{"text": "125-350", "bbox": [418, 683, 465, 692]},
	{"text": "单核细胞绝对值", "bbox": [509, 683, 595, 692]},
	{"text": "0.46", "bbox": [625, 683, 651, 692]},
	{"text": "×10^9/L", "bbox": [680, 683, 727, 692]},
	{"text": "0.10-0.60", "bbox": [730, 683, 785, 692]},
	{"text": "血小板平均容积", "bbox": [190, 694, 277, 703]},
	{"text": "10.0", "bbox": [311, 694, 338, 703]},
	{"text": "fL", "bbox": [366, 694, 378, 703]},
	{"text": "7.6-13.2", "bbox": [418, 694, 471, 703]},
	{"text": "嗜酸细胞绝对值", "bbox": [509, 694, 595, 703]},
	{"text": "0.11", "bbox": [625, 694, 651, 703]},
	{"text": "×10^9/L", "bbox": [680, 694, 727, 703]},
	{"text": "0.02-0.52", "bbox": [730, 694, 785, 703]},
	{"text": "血小板分布宽度", "bbox": [190, 706, 277, 715]},
	{"text": "9.7", "bbox": [311, 706, 331, 715]},
	{"text": "f1", "bbox": [366, 706, 378, 715]},
	{"text": "9.0-17.0", "bbox": [418, 706, 471, 715]},
	{"text": "嗜碱细胞绝对值", "bbox": [509, 706, 595, 715]},
	{"text": "0.04", "bbox": [625, 706, 651, 715]},
	{"text": "×10^9/L", "bbox": [680, 706, 727, 715]},
	{"text": "0.00-0.06", "bbox": [730, 706, 785, 715]},
	{"text": "血小板比积", "bbox": [190, 717, 251, 726]},
	{"text": "0.17", "bbox": [311, 717, 338, 726]},
	{"text": "%", "bbox": [366, 717, 374, 726]},
	{"text": "0.11-0.28", "bbox": [418, 717, 477, 726]},
	{"text": "大血小板比例", "bbox": [186, 729, 263, 738]},
	{"text": "23.9", "bbox": [311, 729, 338, 738]},
	{"text": "%", "bbox": [366, 729, 374, 738]},
	{"text": "13.0-43.0", "bbox": [418, 729, 477, 738]},
	{"text": "备注评价：", "bbox": [178, 806, 230, 816]},
	{"text": "平售时间：2026-03-04 08:18", "bbox": [170, 816, 338, 824]},
	{"text": "接收时间：2026-03-04 08:30", "bbox": [391, 816, 555, 824]},
	{"text": "报告时间：2026-03-04 08:41", "bbox": [616, 813, 776, 822]}
]
2026-08-10 17:33:54,674 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-10 17:33:54,681 INFO     29 [qwen-vl-text] coord API: raw_items=171, valid_items=170, elapsed=48.6s
2026-08-10 17:33:54,681 INFO     29 [qwen-vl-text] coord item[0]: text=检测方法： ARMS 荧光定量 PCR, bbox=[496, 93, 705, 105]
2026-08-10 17:33:54,681 INFO     29 [qwen-vl-text] coord item[1]: text=样本类型：石蜡包埋组织, bbox=[204, 108, 371, 120]
2026-08-10 17:33:54,681 INFO     29 [qwen-vl-text] coord item[2]: text=质量控制：标本量：30%, bbox=[496, 108, 675, 120]
2026-08-10 17:33:54,681 INFO     29 [qwen-vl-text] coord item[3]: text=DNA 抽提方法：AmoyDx FFPE DNA Kit, bbox=[204, 124, 432, 136]
2026-08-10 17:33:54,682 INFO     29 [qwen-vl-text] coord item[4]: text=信号：合格, bbox=[585, 121, 674, 133]
2026-08-10 17:33:54,682 INFO     29 [qwen-vl-text] coord item[5]: text=试剂信息：K-RAS、N-ras、Braf 基因肿瘤相关, bbox=[204, 139, 485, 151]
2026-08-10 17:33:54,682 INFO     29 [qwen-vl-text] coord item[6]: text=DNA 质量：合格, bbox=[585, 135, 695, 147]
2026-08-10 17:33:54,682 INFO     29 [qwen-vl-text] coord item[7]: text=基因突变检测试剂盒, bbox=[280, 153, 398, 165]
2026-08-10 17:33:54,682 INFO     29 [qwen-vl-text] coord item[8]: text=阳性、阴性对照：合格, bbox=[585, 149, 732, 161]
2026-08-10 17:33:54,682 INFO     29 [qwen-vl-text] coord item[9]: text=检测结果：, bbox=[204, 167, 272, 179]
2026-08-10 17:33:54,682 INFO     29 [qwen-vl-text] coord item[10]: text=检测项目, bbox=[218, 200, 264, 210]
2026-08-10 17:33:54,682 INFO     29 [qwen-vl-text] coord item[11]: text=外显子/密码子, bbox=[321, 200, 395, 210]
2026-08-10 17:33:54,682 INFO     29 [qwen-vl-text] coord item[12]: text=突变类型, bbox=[420, 200, 465, 210]
2026-08-10 17:33:54,683 INFO     29 [qwen-vl-text] coord item[13]: text=检测结果, bbox=[693, 200, 737, 210]
2026-08-10 17:33:54,683 INFO     29 [qwen-vl-text] coord item[14]: text=KRAS Exon-2, bbox=[321, 225, 392, 234]
2026-08-10 17:33:54,684 INFO     29 [qwen-vl-text] coord item[15]: text=G12S,G12D, bbox=[420, 225, 477, 234]
2026-08-10 17:33:54,684 INFO     29 [qwen-vl-text] coord item[16]: text=阴性, bbox=[693, 225, 715, 234]
2026-08-10 17:33:54,684 INFO     29 [qwen-vl-text] coord item[17]: text=KRAS Exon-2, bbox=[321, 240, 392, 248]
2026-08-10 17:33:54,685 INFO     29 [qwen-vl-text] coord item[18]: text=G12C,G12R,G12V,G12A,G13C, bbox=[420, 240, 567, 248]
2026-08-10 17:33:54,685 INFO     29 [qwen-vl-text] coord item[19]: text=阴性, bbox=[693, 240, 715, 248]
2026-08-10 17:33:54,686 INFO     29 [qwen-vl-text] coord item[20]: text=KRAS Exon-2, bbox=[321, 253, 392, 262]
2026-08-10 17:33:54,686 INFO     29 [qwen-vl-text] coord item[21]: text=G13D, bbox=[420, 253, 450, 262]
2026-08-10 17:33:54,686 INFO     29 [qwen-vl-text] coord item[22]: text=阴性, bbox=[693, 253, 715, 262]
2026-08-10 17:33:54,686 INFO     29 [qwen-vl-text] coord item[23]: text=KRAS Exon-3, bbox=[321, 267, 392, 276]
2026-08-10 17:33:54,686 INFO     29 [qwen-vl-text] coord item[24]: text=Q61L,Q61R,Q61H,183A>C,Q61H,183A>T, bbox=[420, 267, 629, 276]
2026-08-10 17:33:54,686 INFO     29 [qwen-vl-text] coord item[25]: text=阴性, bbox=[693, 267, 715, 276]
2026-08-10 17:33:54,686 INFO     29 [qwen-vl-text] coord item[26]: text=KRAS Exon-4, bbox=[321, 281, 392, 290]
2026-08-10 17:33:54,687 INFO     29 [qwen-vl-text] coord item[27]: text=K117N(351A>T),K117N(351A>C),A146T,A146V,A146P, bbox=[420, 281, 679, 290]
2026-08-10 17:33:54,687 INFO     29 [qwen-vl-text] coord item[28]: text=阴性, bbox=[693, 281, 715, 290]
2026-08-10 17:33:54,687 INFO     29 [qwen-vl-text] coord item[29]: text=KNB 基因突变联, bbox=[221, 288, 311, 297]
2026-08-10 17:33:54,687 INFO     29 [qwen-vl-text] coord item[30]: text=合检测, bbox=[221, 301, 256, 310]
2026-08-10 17:33:54,687 INFO     29 [qwen-vl-text] coord item[31]: text=NRAS Exon-2, bbox=[321, 295, 392, 304]
2026-08-10 17:33:54,687 INFO     29 [qwen-vl-text] coord item[32]: text=G12D,G12S, bbox=[420, 295, 478, 304]
2026-08-10 17:33:54,687 INFO     29 [qwen-vl-text] coord item[33]: text=阳性, bbox=[693, 295, 715, 304]
2026-08-10 17:33:54,687 INFO     29 [qwen-vl-text] coord item[34]: text=NRAS Exon-2, bbox=[321, 308, 392, 317]
2026-08-10 17:33:54,687 INFO     29 [qwen-vl-text] coord item[35]: text=G13D, bbox=[420, 308, 450, 317]
2026-08-10 17:33:54,687 INFO     29 [qwen-vl-text] coord item[36]: text=阴性, bbox=[693, 308, 715, 317]
2026-08-10 17:33:54,687 INFO     29 [qwen-vl-text] coord item[37]: text=NRAS Exon-2, bbox=[321, 322, 392, 331]
2026-08-10 17:33:54,687 INFO     29 [qwen-vl-text] coord item[38]: text=G13R,G12C,G12V,G12A,G13V, bbox=[420, 322, 573, 331]
2026-08-10 17:33:54,687 INFO     29 [qwen-vl-text] coord item[39]: text=阴性, bbox=[693, 322, 715, 331]
2026-08-10 17:33:54,687 INFO     29 [qwen-vl-text] coord item[40]: text=NRAS Exon-3, bbox=[321, 336, 392, 345]
2026-08-10 17:33:54,687 INFO     29 [qwen-vl-text] coord item[41]: text=Q61R,Q61K,Q61L,Q61H, bbox=[420, 336, 540, 345]
2026-08-10 17:33:54,687 INFO     29 [qwen-vl-text] coord item[42]: text=阴性, bbox=[693, 336, 715, 345]
2026-08-10 17:33:54,687 INFO     29 [qwen-vl-text] coord item[43]: text=NRAS Exon-4, bbox=[321, 350, 392, 359]
2026-08-10 17:33:54,687 INFO     29 [qwen-vl-text] coord item[44]: text=A146T, bbox=[420, 350, 455, 359]
2026-08-10 17:33:54,687 INFO     29 [qwen-vl-text] coord item[45]: text=阴性, bbox=[693, 350, 715, 359]
2026-08-10 17:33:54,688 INFO     29 [qwen-vl-text] coord item[46]: text=BRAF Exon-15, bbox=[321, 363, 398, 372]
2026-08-10 17:33:54,688 INFO     29 [qwen-vl-text] coord item[47]: text=V600E1,V600K,V600E2,V600R,V600D1,V600D2, bbox=[420, 363, 659, 372]
2026-08-10 17:33:54,688 INFO     29 [qwen-vl-text] coord item[48]: text=阴性, bbox=[693, 363, 715, 372]
2026-08-10 17:33:54,688 INFO     29 [qwen-vl-text] coord item[49]: text=检测结论：, bbox=[212, 380, 293, 395]
2026-08-10 17:33:54,688 INFO     29 [qwen-vl-text] coord item[50]: text=N-ras 基因突变;K-ras、Braf 基因均未突变。, bbox=[332, 380, 664, 395]
2026-08-10 17:33:54,688 INFO     29 [qwen-vl-text] coord item[51]: text=注：(1) 分子病理检测结果与样本的收集、处理及核酸质量等有关，本报告针对本次检测样本，不一定能反映病变全貌，, bbox=[240, 401, 763, 411]
2026-08-10 17:33:54,688 INFO     29 [qwen-vl-text] coord item[52]: text=仅供临床医师参考，不能作为临床诊断和治疗的唯一依据，具体治疗方案还需临床医师根据临床情况综合判断进行制定。(2) 分, bbox=[213, 414, 767, 424]
2026-08-10 17:33:54,688 INFO     29 [qwen-vl-text] coord item[53]: text=子检测结果阴性时，不排除样本质量，未知基因异常，及极低丰度突变等原因。(3) 该检测不承担受检者检测后所产生的心理上、, bbox=[213, 427, 767, 437]
2026-08-10 17:33:54,688 INFO     29 [qwen-vl-text] coord item[54]: text=法律上及检测结果应用上等方面的任何后果，本检测报告解释权归本检测实验室所有。如有不符或疑问请及时与我们联系, bbox=[213, 440, 740, 450]
2026-08-10 17:33:54,688 INFO     29 [qwen-vl-text] coord item[55]: text=0535-6691999-83445., bbox=[213, 455, 306, 464]
2026-08-10 17:33:54,688 INFO     29 [qwen-vl-text] coord item[56]: text=报告医师签章：, bbox=[496, 466, 588, 478]
2026-08-10 17:33:54,688 INFO     29 [qwen-vl-text] coord item[57]: text=报告日期： 2024/05/31, bbox=[496, 541, 647, 553]
2026-08-10 17:33:54,688 INFO     29 [qwen-vl-text] coord item[58]: text=项目名称, bbox=[190, 574, 236, 583]
2026-08-10 17:33:54,688 INFO     29 [qwen-vl-text] coord item[59]: text=结果, bbox=[311, 574, 334, 583]
2026-08-10 17:33:54,688 INFO     29 [qwen-vl-text] coord item[60]: text=单位, bbox=[364, 574, 387, 583]
2026-08-10 17:33:54,688 INFO     29 [qwen-vl-text] coord item[61]: text=参考范围, bbox=[418, 574, 463, 583]
2026-08-10 17:33:54,688 INFO     29 [qwen-vl-text] coord item[62]: text=项目名称, bbox=[510, 574, 554, 583]
2026-08-10 17:33:54,688 INFO     29 [qwen-vl-text] coord item[63]: text=结果, bbox=[627, 574, 650, 583]
2026-08-10 17:33:54,688 INFO     29 [qwen-vl-text] coord item[64]: text=单位, bbox=[680, 574, 702, 583]
2026-08-10 17:33:54,689 INFO     29 [qwen-vl-text] coord item[65]: text=参考区间, bbox=[733, 574, 776, 583]
2026-08-10 17:33:54,689 INFO     29 [qwen-vl-text] coord item[66]: text=*★红细胞, bbox=[192, 591, 250, 600]
2026-08-10 17:33:54,689 INFO     29 [qwen-vl-text] coord item[67]: text=4.20, bbox=[311, 591, 338, 600]
2026-08-10 17:33:54,689 INFO     29 [qwen-vl-text] coord item[68]: text=x10^12/L, bbox=[366, 591, 413, 600]
2026-08-10 17:33:54,689 INFO     29 [qwen-vl-text] coord item[69]: text=4.30-5.80, bbox=[418, 591, 477, 600]
2026-08-10 17:33:54,689 INFO     29 [qwen-vl-text] coord item[70]: text=↓, bbox=[490, 591, 496, 600]
2026-08-10 17:33:54,689 INFO     29 [qwen-vl-text] coord item[71]: text=*★白细胞, bbox=[509, 591, 564, 600]
2026-08-10 17:33:54,689 INFO     29 [qwen-vl-text] coord item[72]: text=4.59, bbox=[625, 591, 651, 600]
2026-08-10 17:33:54,689 INFO     29 [qwen-vl-text] coord item[73]: text=×10^9/L, bbox=[680, 591, 727, 600]
2026-08-10 17:33:54,689 INFO     29 [qwen-vl-text] coord item[74]: text=3.50-9.50, bbox=[730, 591, 785, 600]
2026-08-10 17:33:54,689 INFO     29 [qwen-vl-text] coord item[75]: text=*★血红蛋白, bbox=[192, 603, 262, 612]
2026-08-10 17:33:54,689 INFO     29 [qwen-vl-text] coord item[76]: text=145, bbox=[311, 603, 331, 612]
2026-08-10 17:33:54,689 INFO     29 [qwen-vl-text] coord item[77]: text=g/L, bbox=[366, 603, 385, 612]
2026-08-10 17:33:54,689 INFO     29 [qwen-vl-text] coord item[78]: text=130-175, bbox=[418, 603, 465, 612]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[79]: text=中性粒细胞百分率, bbox=[509, 603, 607, 612]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[80]: text=62.1, bbox=[625, 603, 651, 612]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[81]: text=%, bbox=[680, 603, 688, 612]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[82]: text=40.0-75.0, bbox=[730, 603, 785, 612]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[83]: text=*★红细胞压积, bbox=[192, 614, 274, 623]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[84]: text=44.0, bbox=[311, 614, 338, 623]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[85]: text=%, bbox=[366, 614, 374, 623]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[86]: text=40.0-50.0, bbox=[418, 614, 477, 623]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[87]: text=淋巴细胞百分率, bbox=[509, 614, 595, 623]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[88]: text=24.6, bbox=[625, 614, 651, 623]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[89]: text=%, bbox=[680, 614, 688, 623]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[90]: text=20.0-50.0, bbox=[730, 614, 785, 623]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[91]: text=*平均红细胞体积, bbox=[192, 625, 287, 634]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[92]: text=104.8, bbox=[311, 625, 344, 634]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[93]: text=fL, bbox=[366, 625, 378, 634]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[94]: text=82.0-100.0, bbox=[418, 625, 485, 634]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[95]: text=↑, bbox=[490, 625, 496, 634]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[96]: text=单核细胞百分率, bbox=[509, 625, 595, 634]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[97]: text=10.0, bbox=[625, 625, 651, 634]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[98]: text=%, bbox=[680, 625, 688, 634]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[99]: text=3.0-10.0, bbox=[730, 625, 785, 634]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[100]: text=*平均血红蛋白量, bbox=[192, 637, 287, 646]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[101]: text=34.5, bbox=[311, 637, 338, 646]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[102]: text=pg, bbox=[366, 637, 379, 646]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[103]: text=27.0-34.0, bbox=[418, 637, 477, 646]
2026-08-10 17:33:54,690 INFO     29 [qwen-vl-text] coord item[104]: text=↑, bbox=[490, 637, 496, 646]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[105]: text=嗜酸细胞百分率, bbox=[509, 637, 595, 646]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[106]: text=2.4, bbox=[625, 637, 651, 646]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[107]: text=%, bbox=[680, 637, 688, 646]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[108]: text=0.4-8.0, bbox=[730, 637, 785, 646]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[109]: text=*平均血红蛋白浓度, bbox=[192, 648, 298, 657]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[110]: text=330, bbox=[311, 648, 331, 657]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[111]: text=g/L, bbox=[366, 648, 385, 657]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[112]: text=316-354, bbox=[418, 648, 465, 657]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[113]: text=嗜碱细胞百分率, bbox=[509, 648, 595, 657]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[114]: text=0.9, bbox=[625, 648, 651, 657]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[115]: text=%, bbox=[680, 648, 688, 657]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[116]: text=0.0-1.0, bbox=[730, 648, 785, 657]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[117]: text=红细胞分布宽度SD, bbox=[190, 660, 293, 669]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[118]: text=55.1, bbox=[311, 660, 338, 669]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[119]: text=f1, bbox=[366, 660, 378, 669]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[120]: text=39.0-46.0, bbox=[418, 660, 477, 669]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[121]: text=↑, bbox=[490, 660, 496, 669]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[122]: text=中性粒细胞绝对值, bbox=[509, 660, 607, 669]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[123]: text=2.85, bbox=[625, 660, 651, 669]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[124]: text=×10^9/L, bbox=[680, 660, 727, 669]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[125]: text=1.80-6.30, bbox=[730, 660, 785, 669]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[126]: text=红细胞分布宽度CV, bbox=[190, 671, 293, 680]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[127]: text=14.2, bbox=[311, 671, 338, 680]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[128]: text=%, bbox=[366, 671, 378, 680]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[129]: text=10.9-14.5, bbox=[418, 671, 477, 680]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[130]: text=淋巴细胞绝对值, bbox=[509, 671, 595, 680]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[131]: text=1.13, bbox=[625, 671, 651, 680]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[132]: text=×10^9/L, bbox=[680, 671, 727, 680]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[133]: text=1.10-3.20, bbox=[730, 671, 785, 680]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[134]: text=*★血小板总数, bbox=[190, 683, 272, 692]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[135]: text=166, bbox=[311, 683, 331, 692]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[136]: text=×10^9/L, bbox=[366, 683, 413, 692]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[137]: text=125-350, bbox=[418, 683, 465, 692]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[138]: text=单核细胞绝对值, bbox=[509, 683, 595, 692]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[139]: text=0.46, bbox=[625, 683, 651, 692]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[140]: text=×10^9/L, bbox=[680, 683, 727, 692]
2026-08-10 17:33:54,691 INFO     29 [qwen-vl-text] coord item[141]: text=0.10-0.60, bbox=[730, 683, 785, 692]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[142]: text=血小板平均容积, bbox=[190, 694, 277, 703]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[143]: text=10.0, bbox=[311, 694, 338, 703]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[144]: text=fL, bbox=[366, 694, 378, 703]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[145]: text=7.6-13.2, bbox=[418, 694, 471, 703]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[146]: text=嗜酸细胞绝对值, bbox=[509, 694, 595, 703]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[147]: text=0.11, bbox=[625, 694, 651, 703]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[148]: text=×10^9/L, bbox=[680, 694, 727, 703]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[149]: text=0.02-0.52, bbox=[730, 694, 785, 703]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[150]: text=血小板分布宽度, bbox=[190, 706, 277, 715]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[151]: text=9.7, bbox=[311, 706, 331, 715]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[152]: text=f1, bbox=[366, 706, 378, 715]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[153]: text=9.0-17.0, bbox=[418, 706, 471, 715]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[154]: text=嗜碱细胞绝对值, bbox=[509, 706, 595, 715]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[155]: text=0.04, bbox=[625, 706, 651, 715]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[156]: text=×10^9/L, bbox=[680, 706, 727, 715]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[157]: text=0.00-0.06, bbox=[730, 706, 785, 715]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[158]: text=血小板比积, bbox=[190, 717, 251, 726]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[159]: text=0.17, bbox=[311, 717, 338, 726]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[160]: text=%, bbox=[366, 717, 374, 726]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[161]: text=0.11-0.28, bbox=[418, 717, 477, 726]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[162]: text=大血小板比例, bbox=[186, 729, 263, 738]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[163]: text=23.9, bbox=[311, 729, 338, 738]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[164]: text=%, bbox=[366, 729, 374, 738]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[165]: text=13.0-43.0, bbox=[418, 729, 477, 738]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[166]: text=备注评价：, bbox=[178, 806, 230, 816]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[167]: text=平售时间：2026-03-04 08:18, bbox=[170, 816, 338, 824]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[168]: text=接收时间：2026-03-04 08:30, bbox=[391, 816, 555, 824]
2026-08-10 17:33:54,692 INFO     29 [qwen-vl-text] coord item[169]: text=报告时间：2026-03-04 08:41, bbox=[616, 813, 776, 822]
2026-08-10 17:33:54,693 INFO     29 [qwen-vl-text] page=5 — 59/59 coords, api_time=48.6s
2026-08-10 17:33:54,693 INFO     29 [qwen-vl-text] new_positions (59):
[[5, 295.2687939453125, 419.686491394043, 78.29670227050782, 88.39950256347656], [5, 121.44119750976563, 220.85629547119143, 90.92520263671875, 101.0280029296875], [5, 295.2687939453125, 401.8274917602539, 90.92520263671875, 101.0280029296875], [5, 121.44119750976563, 257.16959472656254, 104.39560302734375, 114.4984033203125], [5, 348.25049285888673, 401.23219177246096, 101.86990295410156, 111.97270324707031], [5, 121.44119750976563, 288.72049407958986, 117.0241033935547, 127.12690368652345], [5, 348.25049285888673, 413.7334915161133, 113.65650329589845, 123.7593035888672], [5, 166.68399658203126, 236.92939514160156, 128.81070373535158, 138.91350402832032], [5, 348.25049285888673, 435.75959106445316, 125.44310363769532, 135.54590393066405], [5, 121.44119750976563, 161.9215966796875, 140.59730407714844, 150.7001043701172], [5, 129.77539733886718, 157.15919677734377, 168.3800048828125, 176.79900512695312], [5, 191.09129608154296, 235.14349517822268, 168.3800048828125, 176.79900512695312], [5, 250.0259948730469, 276.81449432373046, 168.3800048828125, 176.79900512695312], [5, 412.54289154052736, 438.736091003418, 168.3800048828125, 176.79900512695312], [5, 191.09129608154296, 233.35759521484377, 189.42750549316406, 197.00460571289062], [5, 250.0259948730469, 283.9580941772461, 189.42750549316406, 197.00460571289062], [5, 412.54289154052736, 425.6394912719727, 189.42750549316406, 197.00460571289062], [5, 191.09129608154296, 233.35759521484377, 202.056005859375, 208.7912060546875], [5, 250.0259948730469, 337.5350930786133, 202.056005859375, 208.7912060546875], [5, 412.54289154052736, 425.6394912719727, 202.056005859375, 208.7912060546875], [5, 191.09129608154296, 233.35759521484377, 213.00070617675783, 220.5778063964844], [5, 250.0259948730469, 267.88499450683594, 213.00070617675783, 220.5778063964844], [5, 412.54289154052736, 425.6394912719727, 213.00070617675783, 220.5778063964844], [5, 191.09129608154296, 233.35759521484377, 224.7873065185547, 232.36440673828125], [5, 250.0259948730469, 374.44369232177735, 224.7873065185547, 232.36440673828125], [5, 412.54289154052736, 425.6394912719727, 224.7873065185547, 232.36440673828125], [5, 191.09129608154296, 233.35759521484377, 236.57390686035157, 244.15100708007813], [5, 250.0259948730469, 404.2086917114258, 236.57390686035157, 244.15100708007813], [5, 412.54289154052736, 425.6394912719727, 236.57390686035157, 244.15100708007813], [5, 131.5612973022461, 185.1382962036133, 242.46720703125, 250.04430725097657], [5, 131.5612973022461, 152.396796875, 253.4119073486328, 260.9890075683594], [5, 191.09129608154296, 233.35759521484377, 248.36050720214845, 255.93760742187501], [5, 250.0259948730469, 284.5533941650391, 248.36050720214845, 255.93760742187501], [5, 412.54289154052736, 425.6394912719727, 248.36050720214845, 255.93760742187501], [5, 191.09129608154296, 233.35759521484377, 259.3052075195313, 266.88230773925784], [5, 250.0259948730469, 267.88499450683594, 259.3052075195313, 266.88230773925784], [5, 412.54289154052736, 425.6394912719727, 259.3052075195313, 266.88230773925784], [5, 191.09129608154296, 233.35759521484377, 271.0918078613281, 278.6689080810547], [5, 250.0259948730469, 341.1068930053711, 271.0918078613281, 278.6689080810547], [5, 412.54289154052736, 425.6394912719727, 271.0918078613281, 278.6689080810547], [5, 191.09129608154296, 233.35759521484377, 282.878408203125, 290.45550842285155], [5, 250.0259948730469, 321.4619934082031, 282.878408203125, 290.45550842285155], [5, 412.54289154052736, 425.6394912719727, 282.878408203125, 290.45550842285155], [5, 191.09129608154296, 233.35759521484377, 294.6650085449219, 302.24210876464844], [5, 250.0259948730469, 270.8614944458008, 294.6650085449219, 302.24210876464844], [5, 412.54289154052736, 425.6394912719727, 294.6650085449219, 302.24210876464844], [5, 191.09129608154296, 236.92939514160156, 305.6097088623047, 313.1868090820313], [5, 250.0259948730469, 392.30269195556644, 305.6097088623047, 313.1868090820313], [5, 412.54289154052736, 425.6394912719727, 305.6097088623047, 313.1868090820313], [5, 126.20359741210937, 174.42289642333986, 319.92200927734376, 332.5505096435547], [5, 197.63959594726563, 395.27919189453127, 319.92200927734376, 332.5505096435547], [5, 142.87199707031252, 454.2138906860352, 337.6019097900391, 346.0209100341797], [5, 126.79889739990234, 456.5950906372071, 348.5466101074219, 356.96561035156253], [5, 126.79889739990234, 456.5950906372071, 359.4913104248047, 367.9103106689453], [5, 126.79889739990234, 440.5219909667969, 370.43601074218753, 378.8550109863281], [5, 126.79889739990234, 182.16179626464844, 383.06451110839845, 390.641611328125], [5, 295.2687939453125, 350.03639282226567, 392.3254113769531, 402.4282116699219], [5, 295.2687939453125, 385.1590921020508, 455.4679132080078, 465.5707135009766], [5, 113.10699768066407, 140.49079711914064, 483.2506140136719, 490.82771423339847]]
2026-08-10 17:33:54,693 INFO     29 [qwen-vl-text] ═══ DONE ═══ 59 positions, pages=1, time=55.7s
2026-08-10 17:33:54,693 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:33:54,702 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:33:54,702 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 17:33:54,702 INFO     29 [qwen-vl-text] positions(33): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:33:54,702 INFO     29 [qwen-vl-text] page grouping: [7], lines per page: [33]
2026-08-10 17:33:54,893 INFO     29 [qwen-vl-text] page=7, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 17:33:54,894 INFO     29 [qwen-vl-text] LLM extraction start, text_len=325
2026-08-10 17:33:54,894 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:33:54,894 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 343, \"bbox_end\": 375, \"encounter_dates\": [\"2026-02-03\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "【检查描述】：心搏次数：97(60~100)bpm，PR间隔：144ms，QRS间隔：88ms，QT间隔：342ms，QTc\n间隔：434ms，P轴：34°，QRS轴：-30°，T轴：15°\n【检查诊断】：窦性心律\nQRS电轴左偏\n【检查时间】：2026/2/3 8:21:15\n【报告时间】：2026/2/3 8:22:02\n检查时间\n心率\n2026-02-03 08:19:19\nPR\n97 bpm\nQRS\n144 ms\nQT/QTc\n88 ms\nP/QRS/T\n342 / 434 ms\nRV5/SV1\n34 / -30 / 15 -\nRV5+SV1\n振幅\n/\nmV\n0.000 mV\nAVR\nV1\nV4\nAVL\nV2\nV5\nAVF\nV3\nV6",
    "role": "user"
  }
]
2026-08-10 17:33:54,896 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:33:54.895+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 81, "failed": 0, "current": {"df5ff51c94e011f1bd9827cf206dfa2d": {"id": "df5ff51c94e011f1bd9827cf206dfa2d", "doc_id": "df229e1a94e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 3352826, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786382896642, "task_type": "dataflow", "root_trace_id": "02e835c46e184d6daf27401b2b0ac85a", "root_traceparent": "00-02e835c46e184d6daf27401b2b0ac85a-ddd202d54b80a7dd-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:33:57,359 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:33:57,360 INFO     29 [qwen-vl-text] LLM output (len=420):
{
  "exam_date": "2026-02-03",
  "report_date": "2026-02-03",
  "exam_name": "心电图",
  "exam_category": "other",
  "body_part": "心脏",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "【检查描述】：心搏次数：97(60~100)bpm，PR间隔：144ms，QRS间隔：88ms，QT间隔：342ms，QTc间隔：434ms，P轴：34°，QRS轴：-30°，T轴：15°",
  "conclusion": "【检查诊断】：窦性心律\nQRS电轴左偏",
  "physician": null,
  "reviewer": null
}
2026-08-10 17:33:57,372 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3678224, prompt_len=1037
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["【检查描述】：心搏次数：97(60~100)bpm，PR间隔：144ms，QRS间隔：88ms，QT间隔：342ms，QTc", "间隔：434ms，P轴：34°，QRS轴：-30°，T轴：15°", "【检查诊断】：窦性心律", "QRS电轴左偏", "【检查时间】：2026/2/3 8:21:15", "【报告时间】：2026/2/3 8:22:02", "检查时间", "心率", "2026-02-03 08:19:19", "PR", "97 bpm", "QRS", "144 ms", "QT/QTc", "88 ms", "P/QRS/T", "342 / 434 ms", "RV5/SV1", "34 / -30 / 15 -", "RV5+SV1", "振幅", "/", "mV", "0.000 mV", "AVR", "V1", "V4", "AVL", "V2", "V5", "AVF", "V3", "V6"]

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
2026-08-10 17:34:06,974 INFO     29 [qwen-vl-text] coord API raw response (len=1779):
[
	{"text": "【检查描述】：心搏次数：97(60~100)bpm，PR间隔：144ms，QRS间隔：88ms，QT间隔：342ms，QTc", "bbox": [185, 97, 805, 110]},
	{"text": "间隔：434ms，P轴：34°，QRS轴：-30°，T轴：15°", "bbox": [172, 108, 514, 119]},
	{"text": "【检查诊断】：窦性心律", "bbox": [190, 126, 338, 137]},
	{"text": "QRS电轴左偏", "bbox": [172, 137, 248, 147]},
	{"text": "【检查时间】：2026/2/3 8:21:15", "bbox": [190, 155, 394, 166]},
	{"text": "【报告时间】：2026/2/3 8:22:02", "bbox": [190, 212, 394, 223]},
	{"text": "检查时间", "bbox": [157, 237, 190, 243]},
	{"text": "心率", "bbox": [157, 243, 173, 249]},
	{"text": "2026-02-03 08:19:19", "bbox": [246, 238, 326, 244]},
	{"text": "PR", "bbox": [157, 249, 167, 255]},
	{"text": "97 bpm", "bbox": [300, 245, 328, 251]},
	{"text": "QRS", "bbox": [157, 255, 169, 261]},
	{"text": "144 ms", "bbox": [274, 251, 326, 257]},
	{"text": "QT/QTc", "bbox": [157, 261, 182, 267]},
	{"text": "88 ms", "bbox": [300, 257, 326, 263]},
	{"text": "P/QRS/T", "bbox": [157, 267, 185, 273]},
	{"text": "342 / 434 ms", "bbox": [272, 263, 326, 269]},
	{"text": "RV5/SV1", "bbox": [157, 273, 185, 279]},
	{"text": "34 / -30 / 15 -", "bbox": [255, 269, 326, 275]},
	{"text": "RV5+SV1", "bbox": [157, 279, 185, 285]},
	{"text": "振幅", "bbox": [200, 275, 217, 281]},
	{"text": "/", "bbox": [296, 275, 302, 281]},
	{"text": "mV", "bbox": [314, 275, 324, 281]},
	{"text": "0.000 mV", "bbox": [289, 281, 324, 287]},
	{"text": "AVR", "bbox": [368, 301, 384, 307]},
	{"text": "V1", "bbox": [527, 301, 536, 307]},
	{"text": "V4", "bbox": [684, 302, 693, 308]},
	{"text": "AVL", "bbox": [368, 344, 383, 350]},
	{"text": "V2", "bbox": [527, 345, 536, 351]},
	{"text": "V5", "bbox": [684, 346, 693, 352]},
	{"text": "AVF", "bbox": [368, 387, 383, 393]},
	{"text": "V3", "bbox": [527, 387, 536, 393]},
	{"text": "V6", "bbox": [684, 388, 693, 394]}
]
2026-08-10 17:34:06,974 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=9.6s
2026-08-10 17:34:06,975 INFO     29 [qwen-vl-text] coord item[0]: text=【检查描述】：心搏次数：97(60~100)bpm，PR间隔：144ms，QRS间隔：88ms，QT间隔：342ms，QTc, bbox=[185, 97, 805, 110]
2026-08-10 17:34:06,975 INFO     29 [qwen-vl-text] coord item[1]: text=间隔：434ms，P轴：34°，QRS轴：-30°，T轴：15°, bbox=[172, 108, 514, 119]
2026-08-10 17:34:06,975 INFO     29 [qwen-vl-text] coord item[2]: text=【检查诊断】：窦性心律, bbox=[190, 126, 338, 137]
2026-08-10 17:34:06,975 INFO     29 [qwen-vl-text] coord item[3]: text=QRS电轴左偏, bbox=[172, 137, 248, 147]
2026-08-10 17:34:06,975 INFO     29 [qwen-vl-text] coord item[4]: text=【检查时间】：2026/2/3 8:21:15, bbox=[190, 155, 394, 166]
2026-08-10 17:34:06,975 INFO     29 [qwen-vl-text] coord item[5]: text=【报告时间】：2026/2/3 8:22:02, bbox=[190, 212, 394, 223]
2026-08-10 17:34:06,975 INFO     29 [qwen-vl-text] coord item[6]: text=检查时间, bbox=[157, 237, 190, 243]
2026-08-10 17:34:06,975 INFO     29 [qwen-vl-text] coord item[7]: text=心率, bbox=[157, 243, 173, 249]
2026-08-10 17:34:06,975 INFO     29 [qwen-vl-text] coord item[8]: text=2026-02-03 08:19:19, bbox=[246, 238, 326, 244]
2026-08-10 17:34:06,975 INFO     29 [qwen-vl-text] coord item[9]: text=PR, bbox=[157, 249, 167, 255]
2026-08-10 17:34:06,975 INFO     29 [qwen-vl-text] coord item[10]: text=97 bpm, bbox=[300, 245, 328, 251]
2026-08-10 17:34:06,975 INFO     29 [qwen-vl-text] coord item[11]: text=QRS, bbox=[157, 255, 169, 261]
2026-08-10 17:34:06,976 INFO     29 [qwen-vl-text] coord item[12]: text=144 ms, bbox=[274, 251, 326, 257]
2026-08-10 17:34:06,976 INFO     29 [qwen-vl-text] coord item[13]: text=QT/QTc, bbox=[157, 261, 182, 267]
2026-08-10 17:34:06,976 INFO     29 [qwen-vl-text] coord item[14]: text=88 ms, bbox=[300, 257, 326, 263]
2026-08-10 17:34:06,976 INFO     29 [qwen-vl-text] coord item[15]: text=P/QRS/T, bbox=[157, 267, 185, 273]
2026-08-10 17:34:06,976 INFO     29 [qwen-vl-text] coord item[16]: text=342 / 434 ms, bbox=[272, 263, 326, 269]
2026-08-10 17:34:06,976 INFO     29 [qwen-vl-text] coord item[17]: text=RV5/SV1, bbox=[157, 273, 185, 279]
2026-08-10 17:34:06,976 INFO     29 [qwen-vl-text] coord item[18]: text=34 / -30 / 15 -, bbox=[255, 269, 326, 275]
2026-08-10 17:34:06,976 INFO     29 [qwen-vl-text] coord item[19]: text=RV5+SV1, bbox=[157, 279, 185, 285]
2026-08-10 17:34:06,976 INFO     29 [qwen-vl-text] coord item[20]: text=振幅, bbox=[200, 275, 217, 281]
2026-08-10 17:34:06,976 INFO     29 [qwen-vl-text] coord item[21]: text=/, bbox=[296, 275, 302, 281]
2026-08-10 17:34:06,976 INFO     29 [qwen-vl-text] coord item[22]: text=mV, bbox=[314, 275, 324, 281]
2026-08-10 17:34:06,976 INFO     29 [qwen-vl-text] coord item[23]: text=0.000 mV, bbox=[289, 281, 324, 287]
2026-08-10 17:34:06,976 INFO     29 [qwen-vl-text] coord item[24]: text=AVR, bbox=[368, 301, 384, 307]
2026-08-10 17:34:06,976 INFO     29 [qwen-vl-text] coord item[25]: text=V1, bbox=[527, 301, 536, 307]
2026-08-10 17:34:06,976 INFO     29 [qwen-vl-text] coord item[26]: text=V4, bbox=[684, 302, 693, 308]
2026-08-10 17:34:06,976 INFO     29 [qwen-vl-text] coord item[27]: text=AVL, bbox=[368, 344, 383, 350]
2026-08-10 17:34:06,977 INFO     29 [qwen-vl-text] coord item[28]: text=V2, bbox=[527, 345, 536, 351]
2026-08-10 17:34:06,977 INFO     29 [qwen-vl-text] coord item[29]: text=V5, bbox=[684, 346, 693, 352]
2026-08-10 17:34:06,977 INFO     29 [qwen-vl-text] coord item[30]: text=AVF, bbox=[368, 387, 383, 393]
2026-08-10 17:34:06,977 INFO     29 [qwen-vl-text] coord item[31]: text=V3, bbox=[527, 387, 536, 393]
2026-08-10 17:34:06,977 INFO     29 [qwen-vl-text] coord item[32]: text=V6, bbox=[684, 388, 693, 394]
2026-08-10 17:34:06,979 INFO     29 [qwen-vl-text] page=7 — 33/33 coords, api_time=9.6s
2026-08-10 17:34:06,979 INFO     29 [qwen-vl-text] new_positions (33):
[[7, 110.13049774169923, 479.2164901733399, 81.66430236816406, 92.60900268554688], [7, 102.39159790039064, 305.98419372558595, 90.92520263671875, 100.18610290527344], [7, 113.10699768066407, 201.21139587402345, 106.07940307617189, 115.34030334472656], [7, 102.39159790039064, 147.63439697265625, 115.34030334472656, 123.7593035888672], [7, 113.10699768066407, 234.5481951904297, 130.4945037841797, 139.75540405273438], [7, 113.10699768066407, 234.5481951904297, 178.48280517578127, 187.74370544433594], [7, 93.4620980834961, 113.10699768066407, 199.53030578613283, 204.58170593261718], [7, 93.4620980834961, 102.98689788818359, 204.58170593261718, 209.63310607910157], [7, 146.4437969970703, 194.0677960205078, 200.3722058105469, 205.42360595703127], [7, 93.4620980834961, 99.41509796142579, 209.63310607910157, 214.68450622558595], [7, 178.58999633789062, 195.25839599609375, 206.26550598144533, 211.31690612792968], [7, 93.4620980834961, 100.60569793701173, 214.68450622558595, 219.73590637207033], [7, 163.11219665527344, 194.0677960205078, 211.31690612792968, 216.36830627441407], [7, 93.4620980834961, 108.34459777832032, 219.73590637207033, 224.7873065185547], [7, 178.58999633789062, 194.0677960205078, 216.36830627441407, 221.41970642089845], [7, 93.4620980834961, 110.13049774169923, 224.7873065185547, 229.83870666503907], [7, 161.9215966796875, 194.0677960205078, 221.41970642089845, 226.47110656738283], [7, 93.4620980834961, 110.13049774169923, 229.83870666503907, 234.89010681152345], [7, 151.80149688720704, 194.0677960205078, 226.47110656738283, 231.5225067138672], [7, 93.4620980834961, 110.13049774169923, 234.89010681152345, 239.94150695800784], [7, 119.05999755859375, 129.18009735107424, 231.5225067138672, 236.57390686035157], [7, 176.20879638671875, 179.78059631347656, 231.5225067138672, 236.57390686035157], [7, 186.9241961669922, 192.87719604492187, 231.5225067138672, 236.57390686035157], [7, 172.04169647216798, 192.87719604492187, 236.57390686035157, 241.62530700683595], [7, 219.07039550781252, 228.5951953125, 253.4119073486328, 258.4633074951172], [7, 313.72309356689453, 319.0807934570313, 253.4119073486328, 258.4633074951172], [7, 407.18519165039066, 412.54289154052736, 254.2538073730469, 259.3052075195313], [7, 219.07039550781252, 227.99989532470704, 289.6136083984375, 294.6650085449219], [7, 313.72309356689453, 319.0807934570313, 290.45550842285155, 295.50690856933596], [7, 407.18519165039066, 412.54289154052736, 291.29740844726564, 296.34880859375], [7, 219.07039550781252, 227.99989532470704, 325.8153094482422, 330.86670959472656], [7, 313.72309356689453, 319.0807934570313, 325.8153094482422, 330.86670959472656], [7, 407.18519165039066, 412.54289154052736, 326.65720947265623, 331.70860961914065]]
2026-08-10 17:34:06,979 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=12.3s
2026-08-10 17:34:06,980 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:34:06,983 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:34:06,983 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 17:34:06,983 INFO     29 [qwen-vl-text] positions(21): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:34:06,984 INFO     29 [qwen-vl-text] page grouping: [7], lines per page: [21]
2026-08-10 17:34:07,179 INFO     29 [qwen-vl-text] page=7, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 17:34:07,180 INFO     29 [qwen-vl-text] LLM extraction start, text_len=473
2026-08-10 17:34:07,180 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:34:07,180 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 376, \"bbox_end\": 396, \"encounter_dates\": [\"2020-01-17\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "【手术信息】：肿瘤位于直肠上段\n【取材部位】：1:直肠×1\n【取材描述】：#:肿物×1\n1:肿物×1\n2:肿物×1\n3:标记上切缘×2\n4:标记下切缘×1\n5:环周切缘×1\n6:肠周淋巴结×5\n7:肠周淋巴结×5\n8:肠周淋巴结×4\n【大体描述】：直肠肠管一段，长12cm，周径5-7cm，距上切缘8.5cm，下切缘3cm，见一隆起型\n肿物，范围1.4*1cm，高出粘膜面0.6cm，肿物切面灰白质硬，侵达浅肌层。\n【病理所见】：直肠肠管一段，长12cm，周径5-7cm，距上切缘8.5cm，下切缘3cm，见一隆起型\n肿物，范围1.4*1cm，高出粘膜面0.6cm，肿物切面灰白质硬，侵达浅肌层。\n【病理诊断】：（直肠）直肠隆起型中分化腺癌，伴脉管内癌栓，侵及浅肌层，标记上切缘、标记下切缘\n及环周切缘未见癌累及，肠周淋巴结3/18枚见癌转移。\nTNM分期：pT2N1bMx。\n免疫组化：MLH1（+），PMS2（+），MSH2（+），MSH6（+），Ki-67+指数约60%。\n【审核医师】：\n【报告时间】：2020/1/17 13:49:00",
    "role": "user"
  }
]
2026-08-10 17:34:10,354 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:34:10,354 INFO     29 [qwen-vl-text] LLM output (len=545):
{
  "exam_date": "2020-01-17",
  "report_date": "2020-01-17",
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "直肠",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "【大体描述】：直肠肠管一段，长12cm，周径5-7cm，距上切缘8.5cm，下切缘3cm，见一隆起型\n肿物，范围1.4*1cm，高出粘膜面0.6cm，肿物切面灰白质硬，侵达浅肌层。",
  "conclusion": "【病理诊断】：（直肠）直肠隆起型中分化腺癌，伴脉管内癌栓，侵及浅肌层，标记上切缘、标记下切缘\n及环周切缘未见癌累及，肠周淋巴结3/18枚见癌转移。\nTNM分期：pT2N1bMx。\n免疫组化：MLH1（+），PMS2（+），MSH2（+），MSH6（+），Ki-67+指数约60%。",
  "physician": null,
  "reviewer": null
}
2026-08-10 17:34:10,362 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3678224, prompt_len=1149
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共21行）
["【手术信息】：肿瘤位于直肠上段", "【取材部位】：1:直肠×1", "【取材描述】：#:肿物×1", "1:肿物×1", "2:肿物×1", "3:标记上切缘×2", "4:标记下切缘×1", "5:环周切缘×1", "6:肠周淋巴结×5", "7:肠周淋巴结×5", "8:肠周淋巴结×4", "【大体描述】：直肠肠管一段，长12cm，周径5-7cm，距上切缘8.5cm，下切缘3cm，见一隆起型", "肿物，范围1.4*1cm，高出粘膜面0.6cm，肿物切面灰白质硬，侵达浅肌层。", "【病理所见】：直肠肠管一段，长12cm，周径5-7cm，距上切缘8.5cm，下切缘3cm，见一隆起型", "肿物，范围1.4*1cm，高出粘膜面0.6cm，肿物切面灰白质硬，侵达浅肌层。", "【病理诊断】：（直肠）直肠隆起型中分化腺癌，伴脉管内癌栓，侵及浅肌层，标记上切缘、标记下切缘", "及环周切缘未见癌累及，肠周淋巴结3/18枚见癌转移。", "TNM分期：pT2N1bMx。", "免疫组化：MLH1（+），PMS2（+），MSH2（+），MSH6（+），Ki-67+指数约60%。", "【审核医师】：", "【报告时间】：2020/1/17 13:49:00"]

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
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord API raw response (len=1400):
[
	{"text": "【手术信息】：肿瘤位于直肠上段", "bbox": [195, 483, 395, 497]},
	{"text": "【取材部位】：1:直肠×1", "bbox": [195, 502, 362, 515]},
	{"text": "【取材描述】：#:肿物×1", "bbox": [195, 520, 348, 532]},
	{"text": "1:肿物×1", "bbox": [407, 523, 468, 534]},
	{"text": "2:肿物×1", "bbox": [525, 523, 585, 534]},
	{"text": "3:标记上切缘×2", "bbox": [643, 523, 741, 534]},
	{"text": "4:标记下切缘×1", "bbox": [176, 530, 279, 541]},
	{"text": "5:环周切缘×1", "bbox": [340, 531, 428, 542]},
	{"text": "6:肠周淋巴结×5", "bbox": [487, 531, 585, 542]},
	{"text": "7:肠周淋巴结×5", "bbox": [643, 531, 741, 542]},
	{"text": "8:肠周淋巴结×4", "bbox": [176, 539, 279, 551]},
	{"text": "【大体描述】：直肠肠管一段，长12cm，周径5-7cm，距上切缘8.5cm，下切缘3cm，见一隆起型", "bbox": [176, 559, 791, 571]},
	{"text": "肿物，范围1.4*1cm，高出粘膜面0.6cm，肿物切面灰白质硬，侵达浅肌层。", "bbox": [176, 569, 637, 580]},
	{"text": "【病理所见】：直肠肠管一段，长12cm，周径5-7cm，距上切缘8.5cm，下切缘3cm，见一隆起型", "bbox": [176, 587, 791, 599]},
	{"text": "肿物，范围1.4*1cm，高出粘膜面0.6cm，肿物切面灰白质硬，侵达浅肌层。", "bbox": [176, 597, 637, 608]},
	{"text": "【病理诊断】：（直肠）直肠隆起型中分化腺癌，伴脉管内癌栓，侵及浅肌层，标记上切缘、标记下切缘", "bbox": [176, 615, 797, 627]},
	{"text": "及环周切缘未见癌累及，肠周淋巴结3/18枚见癌转移。", "bbox": [176, 625, 494, 636]},
	{"text": "TNM分期：pT2N1bMx。", "bbox": [176, 634, 300, 645]},
	{"text": "免疫组化：MLH1（+），PMS2（+），MSH2（+），MSH6（+），Ki-67+指数约60%。", "bbox": [176, 643, 650, 655]},
	{"text": "【审核医师】：", "bbox": [195, 680, 276, 692]},
	{"text": "【报告时间】：2020/1/17 13:49:00", "bbox": [195, 699, 408, 711]}
]
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord API: raw_items=21, valid_items=21, elapsed=8.5s
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord item[0]: text=【手术信息】：肿瘤位于直肠上段, bbox=[195, 483, 395, 497]
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord item[1]: text=【取材部位】：1:直肠×1, bbox=[195, 502, 362, 515]
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord item[2]: text=【取材描述】：#:肿物×1, bbox=[195, 520, 348, 532]
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord item[3]: text=1:肿物×1, bbox=[407, 523, 468, 534]
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord item[4]: text=2:肿物×1, bbox=[525, 523, 585, 534]
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord item[5]: text=3:标记上切缘×2, bbox=[643, 523, 741, 534]
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord item[6]: text=4:标记下切缘×1, bbox=[176, 530, 279, 541]
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord item[7]: text=5:环周切缘×1, bbox=[340, 531, 428, 542]
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord item[8]: text=6:肠周淋巴结×5, bbox=[487, 531, 585, 542]
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord item[9]: text=7:肠周淋巴结×5, bbox=[643, 531, 741, 542]
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord item[10]: text=8:肠周淋巴结×4, bbox=[176, 539, 279, 551]
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord item[11]: text=【大体描述】：直肠肠管一段，长12cm，周径5-7cm，距上切缘8.5cm，下切缘3cm，见一隆起型, bbox=[176, 559, 791, 571]
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord item[12]: text=肿物，范围1.4*1cm，高出粘膜面0.6cm，肿物切面灰白质硬，侵达浅肌层。, bbox=[176, 569, 637, 580]
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord item[13]: text=【病理所见】：直肠肠管一段，长12cm，周径5-7cm，距上切缘8.5cm，下切缘3cm，见一隆起型, bbox=[176, 587, 791, 599]
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord item[14]: text=肿物，范围1.4*1cm，高出粘膜面0.6cm，肿物切面灰白质硬，侵达浅肌层。, bbox=[176, 597, 637, 608]
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord item[15]: text=【病理诊断】：（直肠）直肠隆起型中分化腺癌，伴脉管内癌栓，侵及浅肌层，标记上切缘、标记下切缘, bbox=[176, 615, 797, 627]
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord item[16]: text=及环周切缘未见癌累及，肠周淋巴结3/18枚见癌转移。, bbox=[176, 625, 494, 636]
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord item[17]: text=TNM分期：pT2N1bMx。, bbox=[176, 634, 300, 645]
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord item[18]: text=免疫组化：MLH1（+），PMS2（+），MSH2（+），MSH6（+），Ki-67+指数约60%。, bbox=[176, 643, 650, 655]
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord item[19]: text=【审核医师】：, bbox=[195, 680, 276, 692]
2026-08-10 17:34:18,890 INFO     29 [qwen-vl-text] coord item[20]: text=【报告时间】：2020/1/17 13:49:00, bbox=[195, 699, 408, 711]
2026-08-10 17:34:18,891 INFO     29 [qwen-vl-text] page=7 — 21/21 coords, api_time=8.5s
2026-08-10 17:34:18,891 INFO     29 [qwen-vl-text] new_positions (21):
[[7, 116.08349761962891, 235.14349517822268, 406.6377117919922, 418.4243121337891], [7, 116.08349761962891, 215.4985955810547, 422.63381225585937, 433.5785125732422], [7, 116.08349761962891, 207.16439575195312, 437.7880126953125, 447.89081298828125], [7, 242.2870950317383, 278.6003942871094, 440.3137127685547, 449.5746130371094], [7, 312.5324935913086, 348.25049285888673, 440.3137127685547, 449.5746130371094], [7, 382.7778921508789, 441.11729095458986, 440.3137127685547, 449.5746130371094], [7, 104.7727978515625, 166.0886965942383, 446.20701293945314, 455.4679132080078], [7, 202.4019958496094, 254.78839477539063, 447.0489129638672, 456.3098132324219], [7, 289.9110940551758, 348.25049285888673, 447.0489129638672, 456.3098132324219], [7, 382.7778921508789, 441.11729095458986, 447.0489129638672, 456.3098132324219], [7, 104.7727978515625, 166.0886965942383, 453.7841131591797, 463.88691345214846], [7, 104.7727978515625, 470.8822903442383, 470.62211364746094, 480.7249139404297], [7, 104.7727978515625, 379.2060922241211, 479.0411138916016, 488.30201416015626], [7, 104.7727978515625, 470.8822903442383, 494.1953143310547, 504.29811462402347], [7, 104.7727978515625, 379.2060922241211, 502.61431457519535, 511.87521484375003], [7, 104.7727978515625, 474.4540902709961, 517.7685150146484, 527.8713153076172], [7, 104.7727978515625, 294.07819396972656, 526.1875152587891, 535.4484155273437], [7, 104.7727978515625, 178.58999633789062, 533.7646154785157, 543.0255157470704], [7, 104.7727978515625, 386.9449920654297, 541.3417156982422, 551.444515991211], [7, 116.08349761962891, 164.30279663085938, 572.4920166015626, 582.5948168945313], [7, 116.08349761962891, 242.88239501953126, 588.4881170654297, 598.5909173583984]]
2026-08-10 17:34:18,891 INFO     29 [qwen-vl-text] ═══ DONE ═══ 21 positions, pages=1, time=11.9s
2026-08-10 17:34:18,891 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:34:18,892 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:34:18,892 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 17:34:18,892 INFO     29 [qwen-vl-text] positions(9): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:34:18,892 INFO     29 [qwen-vl-text] page grouping: [8], lines per page: [9]
2026-08-10 17:34:20,278 INFO     29 [qwen-vl-text] page=8, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 17:34:20,279 INFO     29 [qwen-vl-text] LLM extraction start, text_len=224
2026-08-10 17:34:20,279 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:34:20,280 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 397, \"bbox_end\": 405, \"encounter_dates\": [\"2025-11-20\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "【手术信息】：纵隔淋巴结肿大\n【取材部位】：1:EBUS组织×1 2:EBUS刷片×1\n【取材描述】：1:EBUS组织×多\n【大体描述】：灰红碎组织少许，总体积0.4*0.3*0.1cm。\n【病理所见】：灰红碎组织少许，总体积0.4*0.3*0.1cm。\n【病理诊断】：EBUS组织：送检组织内见腺癌，伴大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS\n刷片）查见肿瘤细胞。\n【审核医师】：\n【报告时间】：2025/11/20 11:02:00",
    "role": "user"
  }
]
2026-08-10 17:34:22,419 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:34:22,419 INFO     29 [qwen-vl-text] LLM output (len=399):
{
  "exam_date": null,
  "report_date": "2025-11-20",
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "纵隔淋巴结",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "【大体描述】：灰红碎组织少许，总体积0.4*0.3*0.1cm。",
  "conclusion": "【病理诊断】：EBUS组织：送检组织内见腺癌，伴大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS 刷片）查见肿瘤细胞。",
  "physician": null,
  "reviewer": null
}
2026-08-10 17:34:22,434 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4167120, prompt_len=863
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共9行）
["【手术信息】：纵隔淋巴结肿大", "【取材部位】：1:EBUS组织×1 2:EBUS刷片×1", "【取材描述】：1:EBUS组织×多", "【大体描述】：灰红碎组织少许，总体积0.4*0.3*0.1cm。", "【病理所见】：灰红碎组织少许，总体积0.4*0.3*0.1cm。", "【病理诊断】：EBUS组织：送检组织内见腺癌，伴大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS", "刷片）查见肿瘤细胞。", "【审核医师】：", "【报告时间】：2025/11/20 11:02:00"]

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
2026-08-10 17:34:27,053 INFO     29 [qwen-vl-text] coord API raw response (len=622):
[
	{"text": "【手术信息】：纵隔淋巴结肿大", "bbox": [195, 90, 378, 103]},
	{"text": "【取材部位】：1:EBUS组织×1 2:EBUS刷片×1", "bbox": [195, 109, 489, 121]},
	{"text": "【取材描述】：1:EBUS组织×多", "bbox": [195, 127, 376, 139]},
	{"text": "【大体描述】：灰红碎组织少许，总体积0.4*0.3*0.1cm。", "bbox": [195, 146, 520, 157]},
	{"text": "【病理所见】：灰红碎组织少许，总体积0.4*0.3*0.1cm。", "bbox": [195, 164, 520, 176]},
	{"text": "【病理诊断】：EBUS组织：送检组织内见腺癌，伴大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS", "bbox": [195, 181, 795, 193]},
	{"text": "刷片）查见肿瘤细胞。", "bbox": [176, 192, 304, 203]},
	{"text": "【审核医师】：", "bbox": [195, 228, 276, 240]},
	{"text": "【报告时间】：2025/11/20 11:02:00", "bbox": [195, 247, 410, 259]}
]
2026-08-10 17:34:27,053 INFO     29 [qwen-vl-text] coord API: raw_items=9, valid_items=9, elapsed=4.6s
2026-08-10 17:34:27,053 INFO     29 [qwen-vl-text] coord item[0]: text=【手术信息】：纵隔淋巴结肿大, bbox=[195, 90, 378, 103]
2026-08-10 17:34:27,053 INFO     29 [qwen-vl-text] coord item[1]: text=【取材部位】：1:EBUS组织×1 2:EBUS刷片×1, bbox=[195, 109, 489, 121]
2026-08-10 17:34:27,053 INFO     29 [qwen-vl-text] coord item[2]: text=【取材描述】：1:EBUS组织×多, bbox=[195, 127, 376, 139]
2026-08-10 17:34:27,053 INFO     29 [qwen-vl-text] coord item[3]: text=【大体描述】：灰红碎组织少许，总体积0.4*0.3*0.1cm。, bbox=[195, 146, 520, 157]
2026-08-10 17:34:27,053 INFO     29 [qwen-vl-text] coord item[4]: text=【病理所见】：灰红碎组织少许，总体积0.4*0.3*0.1cm。, bbox=[195, 164, 520, 176]
2026-08-10 17:34:27,053 INFO     29 [qwen-vl-text] coord item[5]: text=【病理诊断】：EBUS组织：送检组织内见腺癌，伴大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS, bbox=[195, 181, 795, 193]
2026-08-10 17:34:27,053 INFO     29 [qwen-vl-text] coord item[6]: text=刷片）查见肿瘤细胞。, bbox=[176, 192, 304, 203]
2026-08-10 17:34:27,053 INFO     29 [qwen-vl-text] coord item[7]: text=【审核医师】：, bbox=[195, 228, 276, 240]
2026-08-10 17:34:27,053 INFO     29 [qwen-vl-text] coord item[8]: text=【报告时间】：2025/11/20 11:02:00, bbox=[195, 247, 410, 259]
2026-08-10 17:34:27,054 INFO     29 [qwen-vl-text] page=8 — 9/9 coords, api_time=4.6s
2026-08-10 17:34:27,054 INFO     29 [qwen-vl-text] new_positions (9):
[[8, 116.08349761962891, 225.0233953857422, 75.77100219726563, 86.71570251464844], [8, 116.08349761962891, 291.10169403076173, 91.76710266113281, 101.86990295410156], [8, 116.08349761962891, 223.83279541015625, 106.92130310058594, 117.0241033935547], [8, 116.08349761962891, 309.5559936523438, 122.91740356445312, 132.17830383300782], [8, 116.08349761962891, 309.5559936523438, 138.07160400390626, 148.174404296875], [8, 116.08349761962891, 473.2634902954102, 152.38390441894532, 162.48670471191406], [8, 104.7727978515625, 180.9711962890625, 161.6448046875, 170.9057049560547], [8, 116.08349761962891, 164.30279663085938, 191.95320556640627, 202.056005859375], [8, 116.08349761962891, 244.0729949951172, 207.94930603027345, 218.05210632324219]]
2026-08-10 17:34:27,054 INFO     29 [qwen-vl-text] ═══ DONE ═══ 9 positions, pages=1, time=8.2s
2026-08-10 17:34:27,055 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:34:27,064 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:34:27,064 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 17:34:27,064 INFO     29 [qwen-vl-text] positions(13): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:34:27,064 INFO     29 [qwen-vl-text] page grouping: [8], lines per page: [13]
2026-08-10 17:34:27,250 INFO     29 [qwen-vl-text] page=8, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 17:34:27,250 INFO     29 [qwen-vl-text] LLM extraction start, text_len=422
2026-08-10 17:34:27,251 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:34:27,251 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 406, \"bbox_end\": 418, \"encounter_dates\": [\"2026-01-16\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "【检查日期】：2026/1/16 8:18:01\n【检查所见】：右肺术后改变，术区可见条索影斑片影，相应支气管截断。双侧胸廓对称，纵隔居中。双\n肺见多发实性结节影，边界清，大者位于右肺下叶（薄层img259），大小约1.2*1.0cm，增强扫描可见不均\n匀强化。双肺见索条状影；双肺背侧胸膜下见条片影。气管支气管通畅，管壁无增厚，无局限性狭窄和扩张\n。纵隔及右肺门区见增大淋巴结影，大者直径约2.4cm，增强扫描可见不均匀强化。心脏大小、形态正常，\n主动脉及冠状动脉管壁见钙化影。右侧胸膜局部略厚，双侧胸腔未见液体密度影。\n【检查诊断】：对比2025-11-28CT：\n1.符合右肺上叶术后改变，术区改变较前相仿，请结合临床复查。\n2.双肺多发结节，部分较前稍饱满、部分新见，考虑转移瘤，建议复查。\n3.纵隔及右肺门增大淋巴结显示，部分较前稍大，考虑转移瘤。\n余所见大致同前。\n【报告医师】：\n【报告时间】：2026/1/16 10:57:25",
    "role": "user"
  }
]
2026-08-10 17:34:27,253 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:34:27.253+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 81, "failed": 0, "current": {"df5ff51c94e011f1bd9827cf206dfa2d": {"id": "df5ff51c94e011f1bd9827cf206dfa2d", "doc_id": "df229e1a94e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 3352826, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786382896642, "task_type": "dataflow", "root_trace_id": "02e835c46e184d6daf27401b2b0ac85a", "root_traceparent": "00-02e835c46e184d6daf27401b2b0ac85a-ddd202d54b80a7dd-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:34:30,447 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:34:30,447 INFO     29 [qwen-vl-text] LLM output (len=662):
{
  "exam_date": "2026-01-16",
  "report_date": "2026-01-16",
  "exam_name": "胸部CT平扫+增强",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "右肺术后改变，术区可见条索影斑片影，相应支气管截断。双侧胸廓对称，纵隔居中。双肺见多发实性结节影，边界清，大者位于右肺下叶（薄层img259），大小约1.2*1.0cm，增强扫描可见不均匀强化。双肺见索条状影；双肺背侧胸膜下见条片影。气管支气管通畅，管壁无增厚，无局限性狭窄和扩张。纵隔及右肺门区见增大淋巴结影，大者直径约2.4cm，增强扫描可见不均匀强化。心脏大小、形态正常，主动脉及冠状动脉管壁见钙化影。右侧胸膜局部略厚，双侧胸腔未见液体密度影。",
  "conclusion": "对比2025-11-28CT：\n1.符合右肺上叶术后改变，术区改变较前相仿，请结合临床复查。\n2.双肺多发结节，部分较前稍饱满、部分新见，考虑转移瘤，建议复查。\n3.纵隔及右肺门增大淋巴结显示，部分较前稍大，考虑转移瘤。\n余所见大致同前。",
  "physician": null,
  "reviewer": null
}
2026-08-10 17:34:30,456 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4167120, prompt_len=1074
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共13行）
["【检查日期】：2026/1/16 8:18:01", "【检查所见】：右肺术后改变，术区可见条索影斑片影，相应支气管截断。双侧胸廓对称，纵隔居中。双", "肺见多发实性结节影，边界清，大者位于右肺下叶（薄层img259），大小约1.2*1.0cm，增强扫描可见不均", "匀强化。双肺见索条状影；双肺背侧胸膜下见条片影。气管支气管通畅，管壁无增厚，无局限性狭窄和扩张", "。纵隔及右肺门区见增大淋巴结影，大者直径约2.4cm，增强扫描可见不均匀强化。心脏大小、形态正常，", "主动脉及冠状动脉管壁见钙化影。右侧胸膜局部略厚，双侧胸腔未见液体密度影。", "【检查诊断】：对比2025-11-28CT：", "1.符合右肺上叶术后改变，术区改变较前相仿，请结合临床复查。", "2.双肺多发结节，部分较前稍饱满、部分新见，考虑转移瘤，建议复查。", "3.纵隔及右肺门增大淋巴结显示，部分较前稍大，考虑转移瘤。", "余所见大致同前。", "【报告医师】：", "【报告时间】：2026/1/16 10:57:25"]

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
2026-08-10 17:34:35,866 INFO     29 [qwen-vl-text] coord API raw response (len=997):
[
	{"text": "【检查日期】：2026/1/16 8:18:01", "bbox": [206, 358, 412, 369]},
	{"text": "【检查所见】：右肺术后改变，术区可见条索影斑片影，相应支气管截断。双侧胸廓对称，纵隔居中。双", "bbox": [206, 376, 807, 388]},
	{"text": "肺见多发实性结节影，边界清，大者位于右肺下叶（薄层img259），大小约1.2*1.0cm，增强扫描可见不均", "bbox": [188, 387, 801, 398]},
	{"text": "匀强化。双肺见索条状影；双肺背侧胸膜下见条片影。气管支气管通畅，管壁无增厚，无局限性狭窄和扩张", "bbox": [188, 397, 807, 408]},
	{"text": "。纵隔及右肺门区见增大淋巴结影，大者直径约2.4cm，增强扫描可见不均匀强化。心脏大小、形态正常，", "bbox": [188, 406, 794, 417]},
	{"text": "主动脉及冠状动脉管壁见钙化影。右侧胸膜局部略厚，双侧胸腔未见液体密度影。", "bbox": [188, 415, 660, 426]},
	{"text": "【检查诊断】：对比2025-11-28CT：", "bbox": [206, 433, 412, 444]},
	{"text": "1.符合右肺上叶术后改变，术区改变较前相仿，请结合临床复查。", "bbox": [188, 443, 568, 454]},
	{"text": "2.双肺多发结节，部分较前稍饱满、部分新见，考虑转移瘤，建议复查。", "bbox": [188, 452, 607, 463]},
	{"text": "3.纵隔及右肺门增大淋巴结显示，部分较前稍大，考虑转移瘤。", "bbox": [188, 461, 557, 472]},
	{"text": "余所见大致同前。", "bbox": [188, 470, 291, 481]},
	{"text": "【报告医师】：", "bbox": [206, 507, 288, 518]},
	{"text": "【报告时间】：2026/1/16 10:57:25", "bbox": [206, 543, 419, 554]}
]
2026-08-10 17:34:35,866 INFO     29 [qwen-vl-text] coord API: raw_items=13, valid_items=13, elapsed=5.4s
2026-08-10 17:34:35,866 INFO     29 [qwen-vl-text] coord item[0]: text=【检查日期】：2026/1/16 8:18:01, bbox=[206, 358, 412, 369]
2026-08-10 17:34:35,866 INFO     29 [qwen-vl-text] coord item[1]: text=【检查所见】：右肺术后改变，术区可见条索影斑片影，相应支气管截断。双侧胸廓对称，纵隔居中。双, bbox=[206, 376, 807, 388]
2026-08-10 17:34:35,866 INFO     29 [qwen-vl-text] coord item[2]: text=肺见多发实性结节影，边界清，大者位于右肺下叶（薄层img259），大小约1.2*1.0cm，增强扫描可见不均, bbox=[188, 387, 801, 398]
2026-08-10 17:34:35,866 INFO     29 [qwen-vl-text] coord item[3]: text=匀强化。双肺见索条状影；双肺背侧胸膜下见条片影。气管支气管通畅，管壁无增厚，无局限性狭窄和扩张, bbox=[188, 397, 807, 408]
2026-08-10 17:34:35,866 INFO     29 [qwen-vl-text] coord item[4]: text=。纵隔及右肺门区见增大淋巴结影，大者直径约2.4cm，增强扫描可见不均匀强化。心脏大小、形态正常，, bbox=[188, 406, 794, 417]
2026-08-10 17:34:35,866 INFO     29 [qwen-vl-text] coord item[5]: text=主动脉及冠状动脉管壁见钙化影。右侧胸膜局部略厚，双侧胸腔未见液体密度影。, bbox=[188, 415, 660, 426]
2026-08-10 17:34:35,866 INFO     29 [qwen-vl-text] coord item[6]: text=【检查诊断】：对比2025-11-28CT：, bbox=[206, 433, 412, 444]
2026-08-10 17:34:35,866 INFO     29 [qwen-vl-text] coord item[7]: text=1.符合右肺上叶术后改变，术区改变较前相仿，请结合临床复查。, bbox=[188, 443, 568, 454]
2026-08-10 17:34:35,866 INFO     29 [qwen-vl-text] coord item[8]: text=2.双肺多发结节，部分较前稍饱满、部分新见，考虑转移瘤，建议复查。, bbox=[188, 452, 607, 463]
2026-08-10 17:34:35,866 INFO     29 [qwen-vl-text] coord item[9]: text=3.纵隔及右肺门增大淋巴结显示，部分较前稍大，考虑转移瘤。, bbox=[188, 461, 557, 472]
2026-08-10 17:34:35,866 INFO     29 [qwen-vl-text] coord item[10]: text=余所见大致同前。, bbox=[188, 470, 291, 481]
2026-08-10 17:34:35,866 INFO     29 [qwen-vl-text] coord item[11]: text=【报告医师】：, bbox=[206, 507, 288, 518]
2026-08-10 17:34:35,866 INFO     29 [qwen-vl-text] coord item[12]: text=【报告时间】：2026/1/16 10:57:25, bbox=[206, 543, 419, 554]
2026-08-10 17:34:35,867 INFO     29 [qwen-vl-text] page=8 — 13/13 coords, api_time=5.4s
2026-08-10 17:34:35,867 INFO     29 [qwen-vl-text] new_positions (13):
[[8, 122.63179748535157, 245.26359497070314, 301.4002087402344, 310.6611090087891], [8, 122.63179748535157, 480.4070901489258, 316.5544091796875, 326.65720947265623], [8, 111.91639770507813, 476.835290222168, 325.8153094482422, 335.0762097167969], [8, 111.91639770507813, 480.4070901489258, 334.23430969238285, 343.49520996093753], [8, 111.91639770507813, 472.6681903076172, 341.8114099121094, 351.0723101806641], [8, 111.91639770507813, 392.8979919433594, 349.388510131836, 358.64941040039065], [8, 122.63179748535157, 245.26359497070314, 364.5427105712891, 373.80361083984377], [8, 111.91639770507813, 338.13039306640627, 372.9617108154297, 382.22261108398436], [8, 111.91639770507813, 361.34709259033207, 380.53881103515624, 389.799711303711], [8, 111.91639770507813, 331.58209320068363, 388.1159112548828, 397.37681152343754], [8, 111.91639770507813, 173.23229644775392, 395.69301147460936, 404.9539117431641], [8, 122.63179748535157, 171.44639648437501, 426.8433123779297, 436.10421264648437], [8, 122.63179748535157, 249.43069488525393, 457.15171325683593, 466.41261352539067]]
2026-08-10 17:34:35,867 INFO     29 [qwen-vl-text] ═══ DONE ═══ 13 positions, pages=1, time=8.8s
2026-08-10 17:34:35,867 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:34:35,868 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:34:35,868 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 17:34:35,868 INFO     29 [qwen-vl-text] positions(13): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:34:35,868 INFO     29 [qwen-vl-text] page grouping: [8], lines per page: [13]
2026-08-10 17:34:36,054 INFO     29 [qwen-vl-text] page=8, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 17:34:36,055 INFO     29 [qwen-vl-text] LLM extraction start, text_len=442
2026-08-10 17:34:36,056 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:34:36,056 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 419, \"bbox_end\": 431, \"encounter_dates\": [\"2025-11-18\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "【检查日期】：2025/11/18 14:25:00\n【检查所见】：右肺术后改变，术区可见条索影斑片影，相应支气管截断。双侧胸廓对称，纵隔居中。双\n肺见多发实性结节影，边界清，大者位于左肺斜裂处（薄层img168），大小约1.2*0.8cm，增强扫描可见不\n均匀强化。双肺见索条状影；双肺背侧胸膜下见条片影。气管支气管通畅，管壁无增厚，无局限性狭窄和扩\n张。纵隔及右肺门区见增大淋巴结影，大者直径约2.3cm，增强扫描可见不均匀强化。心脏大小、形态正常\n，主动脉及冠状动脉管壁见钙化影。右侧胸膜局部略厚，双侧胸腔未见液体密度影。左侧肾上腺见一\n4.1*2.9cm软组织密度结节，不均匀强化。\n【检查诊断】：对比2025-10-22CT：\n1.符合右肺上叶术后改变，术区改变较前相仿，请结合临床复查。\n2.双肺多发结节，较前相仿，部分考虑转移瘤可能性大，建议密切复查。\n3.纵隔及右肺门增大淋巴结显示，较前相仿，考虑转移瘤。\n4.左侧肾上腺结节，考虑转移瘤，大致同前。\n余所见大致同前。",
    "role": "user"
  }
]
2026-08-10 17:34:39,825 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:34:39,825 INFO     29 [qwen-vl-text] LLM output (len=706):
{
  "exam_date": "2025-11-18",
  "report_date": null,
  "exam_name": "胸部CT平扫+增强",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "右肺术后改变，术区可见条索影斑片影，相应支气管截断。双侧胸廓对称，纵隔居中。双肺见多发实性结节影，边界清，大者位于左肺斜裂处（薄层img168），大小约1.2*0.8cm，增强扫描可见不均匀强化。双肺见索条状影；双肺背侧胸膜下见条片影。气管支气管通畅，管壁无增厚，无局限性狭窄和扩张。纵隔及右肺门区见增大淋巴结影，大者直径约2.3cm，增强扫描可见不均匀强化。心脏大小、形态正常，主动脉及冠状动脉管壁见钙化影。右侧胸膜局部略厚，双侧胸腔未见液体密度影。左侧肾上腺见一4.1*2.9cm软组织密度结节，不均匀强化。",
  "conclusion": "对比2025-10-22CT：\n1.符合右肺上叶术后改变，术区改变较前相仿，请结合临床复查。\n2.双肺多发结节，较前相仿，部分考虑转移瘤可能性大，建议密切复查。\n3.纵隔及右肺门增大淋巴结显示，较前相仿，考虑转移瘤。\n4.左侧肾上腺结节，考虑转移瘤，大致同前。\n余所见大致同前。",
  "physician": null,
  "reviewer": null
}
2026-08-10 17:34:39,837 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4167120, prompt_len=1094
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共13行）
["【检查日期】：2025/11/18 14:25:00", "【检查所见】：右肺术后改变，术区可见条索影斑片影，相应支气管截断。双侧胸廓对称，纵隔居中。双", "肺见多发实性结节影，边界清，大者位于左肺斜裂处（薄层img168），大小约1.2*0.8cm，增强扫描可见不", "均匀强化。双肺见索条状影；双肺背侧胸膜下见条片影。气管支气管通畅，管壁无增厚，无局限性狭窄和扩", "张。纵隔及右肺门区见增大淋巴结影，大者直径约2.3cm，增强扫描可见不均匀强化。心脏大小、形态正常", "，主动脉及冠状动脉管壁见钙化影。右侧胸膜局部略厚，双侧胸腔未见液体密度影。左侧肾上腺见一", "4.1*2.9cm软组织密度结节，不均匀强化。", "【检查诊断】：对比2025-10-22CT：", "1.符合右肺上叶术后改变，术区改变较前相仿，请结合临床复查。", "2.双肺多发结节，较前相仿，部分考虑转移瘤可能性大，建议密切复查。", "3.纵隔及右肺门增大淋巴结显示，较前相仿，考虑转移瘤。", "4.左侧肾上腺结节，考虑转移瘤，大致同前。", "余所见大致同前。"]

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
2026-08-10 17:34:45,520 INFO     29 [qwen-vl-text] coord API raw response (len=1017):
[
	{"text": "【检查日期】：2025/11/18 14:25:00", "bbox": [202, 637, 418, 650]},
	{"text": "【检查所见】：右肺术后改变，术区可见条索影斑片影，相应支气管截断。双侧胸廓对称，纵隔居中。双", "bbox": [202, 651, 804, 664]},
	{"text": "肺见多发实性结节影，边界清，大者位于左肺斜裂处（薄层img168），大小约1.2*0.8cm，增强扫描可见不", "bbox": [185, 661, 800, 674]},
	{"text": "均匀强化。双肺见索条状影；双肺背侧胸膜下见条片影。气管支气管通畅，管壁无增厚，无局限性狭窄和扩", "bbox": [185, 671, 800, 684]},
	{"text": "张。纵隔及右肺门区见增大淋巴结影，大者直径约2.3cm，增强扫描可见不均匀强化。心脏大小、形态正常", "bbox": [185, 680, 798, 693]},
	{"text": "，主动脉及冠状动脉管壁见钙化影。右侧胸膜局部略厚，双侧胸腔未见液体密度影。左侧肾上腺见一", "bbox": [185, 690, 764, 703]},
	{"text": "4.1*2.9cm软组织密度结节，不均匀强化。", "bbox": [185, 701, 426, 713]},
	{"text": "【检查诊断】：对比2025-10-22CT：", "bbox": [202, 719, 405, 731]},
	{"text": "1.符合右肺上叶术后改变，术区改变较前相仿，请结合临床复查。", "bbox": [185, 729, 564, 741]},
	{"text": "2.双肺多发结节，较前相仿，部分考虑转移瘤可能性大，建议密切复查。", "bbox": [185, 737, 603, 750]},
	{"text": "3.纵隔及右肺门增大淋巴结显示，较前相仿，考虑转移瘤。", "bbox": [185, 747, 525, 759]},
	{"text": "4.左侧肾上腺结节，考虑转移瘤，大致同前。", "bbox": [185, 756, 448, 769]},
	{"text": "余所见大致同前。", "bbox": [185, 766, 288, 778]}
]
2026-08-10 17:34:45,521 INFO     29 [qwen-vl-text] coord API: raw_items=13, valid_items=13, elapsed=5.7s
2026-08-10 17:34:45,521 INFO     29 [qwen-vl-text] coord item[0]: text=【检查日期】：2025/11/18 14:25:00, bbox=[202, 637, 418, 650]
2026-08-10 17:34:45,521 INFO     29 [qwen-vl-text] coord item[1]: text=【检查所见】：右肺术后改变，术区可见条索影斑片影，相应支气管截断。双侧胸廓对称，纵隔居中。双, bbox=[202, 651, 804, 664]
2026-08-10 17:34:45,521 INFO     29 [qwen-vl-text] coord item[2]: text=肺见多发实性结节影，边界清，大者位于左肺斜裂处（薄层img168），大小约1.2*0.8cm，增强扫描可见不, bbox=[185, 661, 800, 674]
2026-08-10 17:34:45,521 INFO     29 [qwen-vl-text] coord item[3]: text=均匀强化。双肺见索条状影；双肺背侧胸膜下见条片影。气管支气管通畅，管壁无增厚，无局限性狭窄和扩, bbox=[185, 671, 800, 684]
2026-08-10 17:34:45,521 INFO     29 [qwen-vl-text] coord item[4]: text=张。纵隔及右肺门区见增大淋巴结影，大者直径约2.3cm，增强扫描可见不均匀强化。心脏大小、形态正常, bbox=[185, 680, 798, 693]
2026-08-10 17:34:45,521 INFO     29 [qwen-vl-text] coord item[5]: text=，主动脉及冠状动脉管壁见钙化影。右侧胸膜局部略厚，双侧胸腔未见液体密度影。左侧肾上腺见一, bbox=[185, 690, 764, 703]
2026-08-10 17:34:45,522 INFO     29 [qwen-vl-text] coord item[6]: text=4.1*2.9cm软组织密度结节，不均匀强化。, bbox=[185, 701, 426, 713]
2026-08-10 17:34:45,522 INFO     29 [qwen-vl-text] coord item[7]: text=【检查诊断】：对比2025-10-22CT：, bbox=[202, 719, 405, 731]
2026-08-10 17:34:45,522 INFO     29 [qwen-vl-text] coord item[8]: text=1.符合右肺上叶术后改变，术区改变较前相仿，请结合临床复查。, bbox=[185, 729, 564, 741]
2026-08-10 17:34:45,522 INFO     29 [qwen-vl-text] coord item[9]: text=2.双肺多发结节，较前相仿，部分考虑转移瘤可能性大，建议密切复查。, bbox=[185, 737, 603, 750]
2026-08-10 17:34:45,522 INFO     29 [qwen-vl-text] coord item[10]: text=3.纵隔及右肺门增大淋巴结显示，较前相仿，考虑转移瘤。, bbox=[185, 747, 525, 759]
2026-08-10 17:34:45,522 INFO     29 [qwen-vl-text] coord item[11]: text=4.左侧肾上腺结节，考虑转移瘤，大致同前。, bbox=[185, 756, 448, 769]
2026-08-10 17:34:45,522 INFO     29 [qwen-vl-text] coord item[12]: text=余所见大致同前。, bbox=[185, 766, 288, 778]
2026-08-10 17:34:45,523 INFO     29 [qwen-vl-text] page=8 — 13/13 coords, api_time=5.7s
2026-08-10 17:34:45,524 INFO     29 [qwen-vl-text] new_positions (13):
[[8, 120.25059753417969, 248.83539489746096, 536.2903155517579, 547.2350158691406], [8, 120.25059753417969, 478.6211901855469, 548.0769158935547, 559.0216162109375], [8, 110.13049774169923, 476.239990234375, 556.4959161376953, 567.4406164550782], [8, 110.13049774169923, 476.239990234375, 564.914916381836, 575.8596166992188], [8, 110.13049774169923, 475.04939025878906, 572.4920166015626, 583.4367169189453], [8, 110.13049774169923, 454.80919067382814, 580.9110168457031, 591.855717163086], [8, 110.13049774169923, 253.5977947998047, 590.1719171142578, 600.2747174072266], [8, 120.25059753417969, 241.09649505615235, 605.326117553711, 615.4289178466797], [8, 110.13049774169923, 335.7491931152344, 613.7451177978515, 623.8479180908204], [8, 110.13049774169923, 358.9658926391602, 620.4803179931641, 631.4250183105469], [8, 110.13049774169923, 312.5324935913086, 628.8993182373047, 639.0021185302735], [8, 110.13049774169923, 266.69439453125, 636.4764184570313, 647.4211187744141], [8, 110.13049774169923, 171.44639648437501, 644.8954187011719, 654.9982189941406]]
2026-08-10 17:34:45,524 INFO     29 [qwen-vl-text] ═══ DONE ═══ 13 positions, pages=1, time=9.7s
2026-08-10 17:34:45,535 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 17:34:45,536 INFO     29 [Trace] task=df5ff51c | doc=06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf | Extractor:ExaminationReport | outputs={"chunks": "6 items, types={'ExaminationReport': 6}", "html": "", "json": "476 items", "markdown": "", "text": "", "name": "06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 2, \"chunks_Clinical\": 1}"}
2026-08-10 17:34:45,536 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 17:34:45,542 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:34:45,542 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 17:34:46,469 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:34:46,477 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 17:34:46,477 INFO     29 [Trace] task=df5ff51c | doc=06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "476 items", "markdown": "", "text": "", "name": "06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 6, \"chunks_LabExam\": 2, \"chunks_Clinical\": 1}"}
2026-08-10 17:34:46,477 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 17:34:46,478 INFO     29 [ChunkMerger] Merged 11 chunks from 9 sources: {'Extractor:LabExam': 2, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 6, 'Extractor:Progress': 1} (filtered 4 noise chunks)
2026-08-10 17:34:46,487 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 17:34:46,487 INFO     29 [Trace] task=df5ff51c | doc=06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "11 items, types={'LabReport': 2, 'OutpatientRecord': 1, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 6}", "name": "06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf"}
2026-08-10 17:34:46,487 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 17:34:46,672 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786382896902, 'update_date': datetime.datetime(2026, 8, 10, 17, 28, 16), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1290577, 'status': '1'}
2026-08-10 17:34:46,978 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   红细胞  None  4.20  x10^12/L  4.30-5.80  True    白细胞  None  4.59  ×10^9/L  3.50-9.50  False    血红蛋白  None  145  g/L  130-175  False    中性粒细胞百分率  None  62.1  %  40.0-75.0  False    红细胞压积  None  44.0  %  40.0-50.0  False    淋巴细胞百分率  None  24.6  %  20.0-50.0  False    平均红细胞体积  None  104.8  fL  82.0-100.0  True    单核细胞百分率  None  10.0  %  3.0-10.0  False    平均血红蛋白量  None  34.5  pg  27.0-34.0  True    嗜酸细胞百分率  None  2.4  %  0.4-8.0  False    平均血红蛋白浓度  None  330  g/L  316-354  False    嗜碱细胞百分率  None  0.9  %  0.0-1.0  False    红细胞分布宽度SD  None  55.1  fL  39.0-46.0  True    中性粒细胞绝对值  None  2.85  ×10^9/L  1.80-6.30  False    红细胞分布宽度CV  None  14.2  %  10.9-14.5  False    淋巴细胞绝对值  None  1.13  ×10^9/L  1.10-3.20  False    血小板总数  None  166  ×10^9/L  125-350  False    单核细胞绝对值  None  0.46  ×10^9/L  0.10-0.60  False    血小板平均容积  None  10.0  fL  7.6-13.2  False    嗜酸细胞绝对值  None  0.11  ×10^9/L  0.02-0.52  False    血小板分布宽度  None  9.7  fL  9.0-17.0  False    嗜碱细胞绝对值  None  0.04  ×10^9/L  0.00-0.06  False    血小板比积  None  0.17  %  0.11-0.28  False    大血小板比例  None  23.9  %  13.0-43.0  False   
---
   总蛋白  TP  75.96  g/L  65.00-85.00  False    白蛋白(溴甲酚绿法)  ALB  44.42  g/L  40.00-55.00  False    球蛋白  GLO  31.54  g/L  20.00-40.00  False    白蛋白:球蛋白  A:G  1.41  None  1.20-2.40  False    总胆红素  TBIL  14.4  μmol/L  ≤26.0  False    直接胆红素  DBIL  2.0  μmol/L  0.0-6.8  False    间接胆红素  IBIL  12.4  μmol/L  3.0-19.0  False    γ-谷氨酰基转移酶  GGT  49  U/L  10-60  False    碱性磷酸酶  ALP  61  U/L  45-125  False    天门冬氨酸氨基转移酶  AST  16  U/L  15-40  False    丙氨酸氨基转移酶  ALT  6  U/L  9-50  True    AST:ALT  AST:ALT  2.67  None  None  False    总胆汁酸  TBA  4.1  μmol/L  0.0-14.0  False    钾  K  4.67  mmol/L  3.50-5.30  False    钠  Na  138.5  mmol/L  137.0-147.0  False    氯  Cl  104.6  mmol/L  99.0-110.0  False    总二氧化碳  TCO2  26.9  mmol/L  21.0-30.0  False    阴离子隙  ANION  7.0  mmol/L  8.0-16.0  True    钙  Ca  2.35  mmol/L  2.11-2.52  False    无机磷  P  1.19  mmol/L  0.85-1.51  False    镁  MG  0.89  mmol/L  0.75-1.02  False    葡萄糖  GLU  6.21  mmol/L  3.90-6.10  True    尿素  UREA  4.85  mmol/L  3.60-9.50  False    肌酐(酶法)  CREA  58  μmol/L  57-111  False    尿素:肌酐  UREA:CREA  0.08  None  None  False    肾小球滤过率  eGFR (CKD-EPI)  102.43  ml/(min·1.73m^2)  ≥90  False    尿酸  UA  326  μmol/L  208-428  False    肌酸激酶  CK  31  U/L  50-310  True    乳酸脱氢酶  LDH  226  U/L  120-250  False    总胆固醇  CHOL  6.49  mmol/L  3.12-5.72  True    甘油三酯  TG  2.23  mmol/L  0.40-1.70  True    高密度脂蛋白胆固醇  HDL-C  1.00  mmol/L  1.04-1.96  True    低密度脂蛋白胆固醇  LDL-C  3.83  mmol/L  1.53-3.45  True    非高密度脂蛋白胆固醇  non-HDL-C  5.49  mmol/L  None  False    脂蛋白(a)  Lp(a)  309  mg/L  0-300  True    唾液酸  SA  695  mg/L  456-754  False    渗透压  OSM  277.7  MoSM/L  None  False    血同型半胱氨酸  HCY  12.4  μmol/L  0.0-15.0  False   
---
2026-02-03 10:41
主 诉：本次访视为评价注射用HLN601脂质体在晚期实体瘤患者中的安全性、耐受性及药代动力
学特征和初步疗效的多中心、开放性的I期临床试验项目安全性随访。
病 史：同前
审阅受试者日志卡：不适用
试验用药品/医疗器械使用的依从性：不适用
合并用药/合并非药物治疗：
(1) 合并用药：
同前
(2) 合并非药物治疗：
无
体格、专科检查以及辅助检查：
(1) 体格、专科检查：
2026年2月3日 早 8:36 测 生命体征 ：T:36.5℃ P:78次/分 R:19次/分 BP:137/83 mmHg，体
重：84.7Kg，体格检查同筛选期，ECOG评分1分
(2) 辅助检查：
血细胞分析（5分类）、生化系列（36项）、D-二聚体、尿分析+沉渣、凝血四项、常规心电图，
第 1 页
未见明显异常。
疗效评估：
本次访视进行以下疗效评估：不适用
不良事件：
(1) 既往未转归的不良事件：无
(2) 新发生的不良事件：
不适用
其 他：病历更正：2026-01-20门诊病历中“病历更正：2025.12.24住院病历中Bp:142/92mmHg（
CS 与既往病史 高血压（2025.UNK-持续）有关），Bp：143/87mmHg（CS 与既往病史 高血压（
2025.UNK-持续）有关）更正为（CS 与既往病史 高血压（2005.UNK-持续）有关）” 改为“
2025.12.25住院病历中Bp:142/92mmHg（CS 与既往病史 高血压（2025.UNK-持续）有关），Bp：
143/87mmHg（CS 与既往病史 高血压（2025.UNK-持续）有关）更正为（CS 与既往病史 高血压（
2005.UNK-持续）有关）”时间更正错误，应为：“2025.12.25住院病历中Bp:142/92mmHg（CS 与既往
病史 高血压（2025.UNK-持续）有关），Bp：143/87mmHg（CS 与既往病史 高血压（2025.UNK-持续）
有关）更正为（CS 与既往病史 高血压（2005.UNK-持续）有关）” 改为“2025.12.25住院病历中Bp：
142/92mmHg（CS 与既往病史 高血压（2025.UNK-持续）有关），Bp：143/87mmHg（CS 与既往病史 高
血压（2025.UNK-持续）有关）更正为（CS 与既往病史 高血压（2005.UNK-持续）有关）
第 2 页
门诊诊断:
肺恶性肿瘤
诊疗意见:
(1)后续访视:出组,出组原因:疾病进展
(2)发放试验用药品/医疗器械:不适用
(3)其他用药/非药物治疗医嘱:无
(4)其他:无
第3页
---
性别：男
年龄：64岁
出院日期：2026-01-07 17:10
住院天数：1天
入院情况：因直肠癌术后5年余，左肾上腺转移1年余入院。查体：ECOG 1分。胸壁、腹部可见手术瘢痕，愈合可。
入院诊断：1.直肠中分化腺癌术后（pT2N1bM0 IIIA→IV期） 左锁骨区、纵膈、右侧肺门区淋巴结转移 左肾上腺转移 双肺转移 2.2型糖尿病伴多个并发症 2型糖尿病性周围血管病变 2型糖尿病性肾病 3.高血压病3级（极高危） 4.右肺错构瘤术后
诊疗经过：入院后经患者及其家属同意，无禁忌，于2026-01-07行第3周期治疗：注射用HLN601脂质体20.2mg静脉输液。治疗结束，准予出院。
治疗前TNM分期：IV期
出院诊断：1.直肠中分化腺癌术后（pT2N1bM0 IIIA→IV期） 左锁骨区、纵膈、右侧肺门区淋巴结转移 左肾上腺转移 双肺转移 2.2型糖尿病伴多个并发症 2型糖尿病性周围血管病变 2型糖尿病性肾病 3.高血压病3级（极高危） 4.右肺错构瘤术后
出院情况：一般情况可，查体：ECOG 1分。胸壁、腹部可见手术瘢痕，愈合可。
出院医嘱：
1.注意休息，避免劳累、感染；
2.每周至少查2次血常规（3-4天一次），若白细胞、中性粒细胞或血小板下降，及时升白或升血小板治疗；
3.出院带药：无。如有不适及时就诊。
4.按临床试验方案要求随访。
---
20200113根治术
术后XELOX 6周期
20240510复发
20240601~20240828 7周贝伐+伊利替康+5FU
20240925贝伐+卡培维持 门诊持续使用，末次25.10
20251119确诊转移
20251210参加HLN601脂质体项目，末次20260107行第三周期，进展出组
性别：男
婚姻：丧偶
年龄：64岁
入院日期：2026-01-07 09:03
民族：汉族
记录日期：2026-01-07 09:25
职业：离退休人员
病史陈述者：患者本人及亲属
主诉：直肠癌术后5年余，左肾上腺转移1年余。
现病史：患者因“查体发现直肠肿物3天”于2020-01-06第一次住院普外科。入院后完善检查，排除手术禁忌症，行电子肠镜下消化道注药术，EMR，电子肠镜下尼龙绳结扎术，
电子肠镜下钛夹止血术，电子肠镜下取异物术，积极术前准备，2020-01-13在气管插管全身
麻醉下行腹腔镜下直肠癌根治术（Dixon），术后病理：（直肠）直肠隆起型中分化腺癌，
伴脉管内癌栓，侵及浅肌层，标记上切缘、标记下切缘及环周切缘未见癌累及，肠周淋巴结
3/18枚见癌转移。TNM分期：pT2N1bMx。免疫组化：MLH1（+），PMS2（+），MSH2（+），
MSH6（+），Ki-67+指数约60%。术后行“XELOX”方案化疗6周期。
2024-05-10当地医院复查CT：“提示左肾上腺肿物”。2024-05-16住院泌尿外科。入院
后完善辅助检查：肾上腺增强(64排)：1.左侧肾上腺区占位，考虑恶性肿瘤，转移瘤？皮质
癌？2.右侧肾上腺外侧肢增粗，增生可能大。3.脂肪肝。胸部平扫(64排-128层)：对比
2021-10-08CT：1.符合右肺上叶术后改变，请结合临床。2.左肺下叶病灶（img33）较前略
增大，右肺下叶（img50）结节为新见，余结节变化不著，建议随诊复查。3.新见双肺轻度
坠积性改变；双肺慢性炎症/纤维灶，较前略增多。余所见较前变化不著。PET-CT全身显
像：1.直肠术后，术区肠壁略增厚，FDG代谢略高，考虑炎症；肠周未见肿大淋巴结。2.右
肺上叶结节切除术后，术区未见异常FDG代谢增高灶。3.左肾上腺占位，FDG代谢不均匀增
高，考虑恶性病变，原发肾上腺肿瘤？4.（1）左肺下叶结节，较本院2020-07-06PET/CT、
2021-10-09CT，体积略增大；（2）右肺下叶结节，较本院2020-07-06PET/CT、
2021-10-09CT为新增；以上两枚结节FDG代谢均不高，建议密切随访。5.右侧中耳乳突炎
症；鼻咽部左侧咽隐窝区炎症；双侧颈部增生淋巴结；双侧扁桃体炎症；甲状腺小结节，
FDG代谢不高，建议B超随访；余双肺小结节，FDG代谢不高，建议随访观察；脂肪肝；双肾
小结石；前列腺钙化灶。完善相关辅助检查后，为排除左侧肾上腺是否为转移瘤，遂请介入
科会诊协助左侧肾上腺穿刺活检术，病理：（左侧肾上腺组织）送检示皮肤组织及大部分坏
死组织，偶见少许异型腺体，结合病史及免疫组化结果，符合肠癌转移。免疫组化：CK20（
+）、CK7（-）、CDX-2（+）、SATB2（+）。请我科会诊后转入。转科后于2024-05-28行左
肾上腺穿刺活检，病理：（左侧肾上腺穿刺标本）腺癌。基因检测：KRAS突变。于
2024-06-01、2024-06-19、2024-07-03、2024-07-17、2024-07-31、2024-08-14、
2024-08-28给予一线治疗1-7周期：贝伐珠单抗 400mg d1+伊力替康 280mg d1+左亚叶酸钙
175mg d1+氟尿嘧啶 0.75g d1+氟尿嘧啶 4.0g持续泵入48h，q14d。过程顺利。6周期治疗后
第1页
复查疗效评价：SD。
患者分别于2024-09-25、2024-10-14第9、10次入院给予贝伐珠单抗 400mg d1+卡培他
滨（希罗达）1.5g bid d-14/21d维持治疗。
出院后患者规律于门诊就诊并应用贝伐珠单抗+卡培他滨维持治疗。2025-08患者感腹
胀，大便次数改变，大便不尽感，于2025-08-29再次入院保健科，入院后完善相关检查：肠
镜检查：所见直结肠黏膜大致正常，直肠术后改变。给予调脂、降压、降糖等治疗后好转出
院。
患者因“咳嗽”2025-11-17入院全科，入院后完善相关检查排除禁忌后于2025-11-19行
电子支气管镜检查并留取标本。2025-11-19 病理回示：EBUS组织：送检组织内见腺癌，伴
大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS刷片）查见肿瘤细胞。2025-11-25门
诊完善PET/CT躯干显像（颅底到大腿中上部、不含脑）：与本院2024-05-17 PET/CT比较：
1.直肠癌术后，术区肠壁略增厚，FDG代谢增高，首先考虑炎症，请结合肠镜评价；肠周及
腹、盆腔未见异常肿大淋巴结。2.左侧锁骨区、纵隔、右侧肺门区多发大小不等淋巴结/结
节影，FDG代谢增高，结合病理，符合多发淋巴结转移表现。3.左肾上腺肿物治疗后，较前
体积明显减小，FDG代谢不高，建议随诊。4.（1）右肺下叶结节，较前体积增大，代谢增
高，考虑转移可能大；（2）左肺下叶结节，代谢不高，较前体积未见著变，建议继续随
诊；（3）余双肺多发结节，代谢不高，部分较前为新发，不除外部分为转移性，建议治疗
过程定期复查。5.右肺上叶结节切除术后，术区未见异常FDG代谢增高灶。6.鼻咽部后壁及
左侧咽隐窝区炎症；甲状腺小结节，FDG代谢不高，建议B超随访；贲门部轻度FDG代谢增高
及腹腔部分肠道FDG代谢增高，考虑炎性/生理性摄取可能；脂肪肝；双肾小结石；前列腺钙
化灶。
患者于2025-12-03入组评价注射用HLN601脂质体在晚期实体瘤患者中的安全性、耐受性
及药代动力学特征和初步疗效的多中心、开放的I期临床试验。于2025-12-10行第1周期治
疗：注射用HLN601脂质体20.2mg静脉输液。治疗结束，准予出院。
患者于2025-12-25再次入院行第2周期治疗：注射用HLN601脂质体20.2mg静脉输液。治
疗结束，准予出院。
出院后患者复查血常规、肝肾功无明显异常，今为继续治疗入院。患者精神状态良好，
食欲一般，睡眠良好，大小便正常，体力情况良好，体重较前无明显变化。
补充病史：高脂血症（2024.12.uk-持续）
补充合并用药：于2024.12.uk口服阿托伐他汀钙片 10mg qd 持续中，用药原因：治疗
既往病史高脂血症（2024.12.uk-持续）。
既往史：2021-10-15本院胸外科行“胸腔镜右肺上叶楔形切除术”，病理：右肺上
叶：错构瘤。余参阅首次入院病历。
个人史：参阅首次入院病历。
家族史：参阅首次入院病历。
第2页
体格检查
T 35.4℃
P 108次/分
R 20次/分
Bp 137/90mmHg
H 168cm
W 86.1kg
S 2.02m²
NRS 0分
发育正常，营养中等，正常面容，表情自如，自主体位，神志清楚，查体合作。全身皮肤粘膜无黄染，无皮疹，无皮下出血，无皮下结节，皮下无水肿，无肝掌、蜘蛛痣，毛发分布均匀。全身浅表淋巴结无肿大。眼睑无水肿，结膜无苍白，眼球无突出，无震颤，巩膜无黄染，瞳孔等大等圆，对光反射灵敏，耳廓对称，无畸形，牵拉无疼痛，外耳道无异常分泌物，乳突无压痛，无听力粗试障碍。鼻无畸形。口唇无发绀，口腔粘膜无充血、糜烂。舌苔薄白，伸舌无偏斜、震颤，牙龈无红肿，咽部粘膜无充血，扁桃体无肿大。颈软无抵抗，颈动脉无异常搏动，半坐位颈静脉未见充盈，颈部大血管区未闻及血管杂音。气管居中，肝颈静脉回流征阴性，甲状腺无肿大，无压痛、震颤、血管杂音。胸廓无畸形，呼吸运动两侧对称，肋间隙无狭窄或饱满，胸壁无压痛，语颤无增强、减弱，胸骨无压痛。双肺叩诊清音，呼吸规整，双肺呼吸音清晰，未闻及干湿性啰音，无胸膜摩擦音。心前区无异常隆起、异常搏动、震颤，心浊音界不大，心率108次/分，律齐，心音有力，各瓣膜听诊区未闻及杂音，无心包摩擦音。腹平坦，软，无压痛、反跳痛，腹部无包块。肝脏未触及，脾脏未触及，Murphy氏征阴性，肾区无叩击痛，无移动性浊音。肠鸣音正常，4次/分。肛门及外生殖器无异常。脊柱正常生理弯曲，四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾），关节无肿胀、压痛，下肢无水肿。
肌肉无压痛，四肢肌力、肌张力未见异常，双侧肱
二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性。
专科检查： ECOG 1分。浅表淋巴结未及肿大。胸壁、腹部可见手术瘢痕(CS病史)，愈合可。
辅助检查
2025-11-19 病理：EBUS组织：送检组织内见腺癌，伴大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS刷片）查见肿瘤细胞。本院。
初步诊断：
1.直肠中分化腺癌术后（pT2N1bM0 IIIA
→IV期）
左锁骨区、纵膈、右侧肺门区淋巴
结转移
左肾上腺转移
第3页
---
检测项目：K-RAS、N-ras、Braf基因突变检测
检测方法： ARMS 荧光定量 PCR
样本类型：石蜡包埋组织
质量控制：标本量：30%
DNA 抽提方法：AmoyDx FFPE DNA Kit
信号：合格
试剂信息：K-RAS、N-ras、Braf 基因肿瘤相关
DNA 质量：合格
基因突变检测试剂盒
阳性、阴性对照：合格
检测结果：
检测项目
外显子/密码子
突变类型
检测结果
KRAS Exon-2
G12S,G12D
阴性
KRAS Exon-2
G12C,G12R,G12V,G12A,G13C
阴性
KRAS Exon-2
G13D
阴性
KRAS Exon-3
Q61L,Q61R,Q61H,183A>C,Q61H,183A>T
阴性
KRAS Exon-4
K117N(351A>T),K117N(351A>C),A146T,A146V,A146P
阴性
KNB 基因突变联
合检测
NRAS Exon-2
G12D,G12S
阳性
NRAS Exon-2
G13D
阴性
NRAS Exon-2
G13R,G12C,G12V,G12A,G13V
阴性
NRAS Exon-3
Q61R,Q61K,Q61L,Q61H
阴性
NRAS Exon-4
A146T
阴性
BRAF Exon-15
V600E1,V600K,V600E2,V600R,V600D1,V600D2
阴性
检测结论：
N-ras 基因突变;K-ras、Braf 基因均未突变。
注：(1) 分子病理检测结果与样本的收集、处理及核酸质量等有关，本报告针对本次检测样本，不一定能反映病变全貌，
仅供临床医师参考，不能作为临床诊断和治疗的唯一依据，具体治疗方案还需临床医师根据临床情况综合判断进行制定。(2) 分
子检测结果阴性时，不排除样本质量，未知基因异常，及极低丰度突变等原因。(3) 该检测不承担受检者检测后所产生的心理上、
法律上及检测结果应用上等方面的任何后果，本检测报告解释权归本检测实验室所有。如有不符或疑问请及时与我们联系
0535-6691999-83445.
报告医师签章：
报告日期： 2024/05/31
---
【检查描述】：心搏次数：97(60~100)bpm，PR间隔：144ms，QRS间隔：88ms，QT间隔：342ms，QTc
间隔：434ms，P轴：34°，QRS轴：-30°，T轴：15°
【检查诊断】：窦性心律
QRS电轴左偏
【检查时间】：2026/2/3 8:21:15
【报告时间】：2026/2/3 8:22:02
检查时间
心率
2026-02-03 08:19:19
PR
97 bpm
QRS
144 ms
QT/QTc
88 ms
P/QRS/T
342 / 434 ms
RV5/SV1
34 / -30 / 15 -
RV5+SV1
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
AVF
V3
V6
---
【手术信息】：肿瘤位于直肠上段
【取材部位】：1:直肠×1
【取材描述】：#:肿物×1
1:肿物×1
2:肿物×1
3:标记上切缘×2
4:标记下切缘×1
5:环周切缘×1
6:肠周淋巴结×5
7:肠周淋巴结×5
8:肠周淋巴结×4
【大体描述】：直肠肠管一段，长12cm，周径5-7cm，距上切缘8.5cm，下切缘3cm，见一隆起型
肿物，范围1.4*1cm，高出粘膜面0.6cm，肿物切面灰白质硬，侵达浅肌层。
【病理所见】：直肠肠管一段，长12cm，周径5-7cm，距上切缘8.5cm，下切缘3cm，见一隆起型
肿物，范围1.4*1cm，高出粘膜面0.6cm，肿物切面灰白质硬，侵达浅肌层。
【病理诊断】：（直肠）直肠隆起型中分化腺癌，伴脉管内癌栓，侵及浅肌层，标记上切缘、标记下切缘
及环周切缘未见癌累及，肠周淋巴结3/18枚见癌转移。
TNM分期：pT2N1bMx。
免疫组化：MLH1（+），PMS2（+），MSH2（+），MSH6（+），Ki-67+指数约60%。
【审核医师】：
【报告时间】：2020/1/17 13:49:00
---
【手术信息】：纵隔淋巴结肿大
【取材部位】：1:EBUS组织×1 2:EBUS刷片×1
【取材描述】：1:EBUS组织×多
【大体描述】：灰红碎组织少许，总体积0.4*0.3*0.1cm。
【病理所见】：灰红碎组织少许，总体积0.4*0.3*0.1cm。
【病理诊断】：EBUS组织：送检组织内见腺癌，伴大片坏死，结合患者病史，首先考虑肠癌转移。（EBUS
刷片）查见肿瘤细胞。
【审核医师】：
【报告时间】：2025/11/20 11:02:00
---
【检查日期】：2026/1/16 8:18:01
【检查所见】：右肺术后改变，术区可见条索影斑片影，相应支气管截断。双侧胸廓对称，纵隔居中。双
肺见多发实性结节影，边界清，大者位于右肺下叶（薄层img259），大小约1.2*1.0cm，增强扫描可见不均
匀强化。双肺见索条状影；双肺背侧胸膜下见条片影。气管支气管通畅，管壁无增厚，无局限性狭窄和扩张
。纵隔及右肺门区见增大淋巴结影，大者直径约2.4cm，增强扫描可见不均匀强化。心脏大小、形态正常，
主动脉及冠状动脉管壁见钙化影。右侧胸膜局部略厚，双侧胸腔未见液体密度影。
【检查诊断】：对比2025-11-28CT：
1.符合右肺上叶术后改变，术区改变较前相仿，请结合临床复查。
2.双肺多发结节，部分较前稍饱满、部分新见，考虑转移瘤，建议复查。
3.纵隔及右肺门增大淋巴结显示，部分较前稍大，考虑转移瘤。
余所见大致同前。
【报告医师】：
【报告时间】：2026/1/16 10:57:25
---
【检查日期】：2025/11/18 14:25:00
【检查所见】：右肺术后改变，术区可见条索影斑片影，相应支气管截断。双侧胸廓对称，纵隔居中。双
肺见多发实性结节影，边界清，大者位于左肺斜裂处（薄层img168），大小约1.2*0.8cm，增强扫描可见不
均匀强化。双肺见索条状影；双肺背侧胸膜下见条片影。气管支气管通畅，管壁无增厚，无局限性狭窄和扩
张。纵隔及右肺门区见增大淋巴结影，大者直径约2.3cm，增强扫描可见不均匀强化。心脏大小、形态正常
，主动脉及冠状动脉管壁见钙化影。右侧胸膜局部略厚，双侧胸腔未见液体密度影。左侧肾上腺见一
4.1*2.9cm软组织密度结节，不均匀强化。
【检查诊断】：对比2025-10-22CT：
1.符合右肺上叶术后改变，术区改变较前相仿，请结合临床复查。
2.双肺多发结节，较前相仿，部分考虑转移瘤可能性大，建议密切复查。
3.纵隔及右肺门增大淋巴结显示，较前相仿，考虑转移瘤。
4.左侧肾上腺结节，考虑转移瘤，大致同前。
余所见大致同前。
2026-08-10 17:34:47,697 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 17:34:47,697 INFO     29 [Trace] task=df5ff51c | doc=06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "11 items, types={'LabReport': 2, 'OutpatientRecord': 1, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 6}", "name": "06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf", "embedding_token_consumption": 8558}
2026-08-10 17:34:47,697 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 17:34:47,981 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 17:34:47,981 INFO     29 [Trace] task=df5ff51c | doc=06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":11,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 17:34:47,987 INFO     29 [DIAG-EXECUTOR] row_position_int len=24 row[0]=(6, 113, 148, 498, 506) row[-1]=(6, 113, 156, 612, 620)
2026-08-10 17:34:47,987 INFO     29 [DIAG-EXECUTOR] row_position_int len=38 row[0]=(7, 123, 155, 89, 96) row[-1]=(7, 123, 169, 537, 545)
2026-08-10 17:34:47,987 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:34:47,987 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:34:47,987 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:34:47,987 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:34:47,987 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:34:47,987 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:34:47,987 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:34:47,987 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:34:47,987 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:34:47,994 INFO     29 set_progress(df5ff51c94e011f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 17:34:47 [DOC Engine]:
Start to index...
2026-08-10 17:34:48,072 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.073s]
2026-08-10 17:34:48,076 INFO     29 set_progress(df5ff51c94e011f1bd9827cf206dfa2d), progress: 0.8090909090909091, progress_msg: 
2026-08-10 17:34:48,111 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.027s]
2026-08-10 17:34:48,150 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.032s]
2026-08-10 17:34:48,158 INFO     29 set_progress(df5ff51c94e011f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 17:34:48 Indexing done (0.17s). Task done (367.78s)
2026-08-10 17:34:48,165 INFO     29 [Done], chunks(11), token(8558), elapsed:367.78
2026-08-10 17:34:48,358 INFO     29 handle_task done for task {"id": "df5ff51c94e011f1bd9827cf206dfa2d", "doc_id": "df229e1a94e011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "06-\u4e34\u6c82\u4eba\u6c11-ZJBO\uff0c\u76f4\u80a0\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 3352826, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786382896642, "task_type": "dataflow", "root_trace_id": "02e835c46e184d6daf27401b2b0ac85a", "root_traceparent": "00-02e835c46e184d6daf27401b2b0ac85a-ddd202d54b80a7dd-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
