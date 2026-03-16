#!/usr/bin/env python3
"""
一键恢复 DSL 到指定版本。

用法:
  # 恢复到最新正确版本
  python3 restore_dsl.py

  # 恢复到指定版本文件
  python3 restore_dsl.py dsl_v1.4_verified_20260308_140144.json

  # 只验证当前 DSL（不修改）
  python3 restore_dsl.py --check
"""
import sys, os, json, time
sys.path.insert(0, "/Users/weixiaofeng/Desktop/zxwl/coding/ragflow")

import psycopg2
from psycopg2.extras import Json

CANVAS_ID = "a445e54a1a3311f1a5992a5fbb884ed3"
VERSION_DIR = os.path.dirname(os.path.abspath(__file__))
LATEST = os.path.join(VERSION_DIR, "dsl_v1.4_LATEST.json")

DB_CONF = dict(dbname='ragflow', user='noeticai', password='noeticai', host='localhost', port=5432)


def verify_dsl(dsl):
    """全面验证 DSL 是否符合 v1.4 规范，返回 (pass_count, fail_count, details)"""
    checks = []

    # 组件列表
    expected_comps = {'File', 'Parser:MedLink', 'Splitter:MedLink', 'Extractor:Classify',
                      'Extractor:Extract', 'Extractor:Critique', 'Tokenizer:MedEmbed'}
    actual_comps = set(dsl.get('components', {}).keys())
    checks.append(("组件列表完整", actual_comps == expected_comps))

    # Splitter
    sp = dsl['components']['Splitter:MedLink']['obj']['params']
    checks.append(("Splitter delimiter = \\n (ord 10)", sp.get('delimiters') == ["\n"]))

    # Classify
    cp = dsl['components']['Extractor:Classify']['obj']['params']
    checks.append(("Classify model = deepseek-v3.2", cp.get('llm_id') == 'deepseek-v3.2'))
    checks.append(("Classify field = classify_result_tks", cp.get('field_name') == 'classify_result_tks'))
    checks.append(("Classify 有 department", 'department' in cp.get('sys_prompt', '')))
    checks.append(("Classify 有 禁止使用中文", '禁止使用中文' in cp.get('sys_prompt', '')))
    checks.append(("Classify 有 few-shot", '示例' in cp.get('sys_prompt', '') and '内科门诊' in cp.get('sys_prompt', '')))
    checks.append(("Classify 无 encounter_id", 'encounter_id' not in cp.get('sys_prompt', '')))

    # Extract
    ep = dsl['components']['Extractor:Extract']['obj']['params']
    checks.append(("Extract model = qwen3-max", ep.get('llm_id') == 'qwen3-max'))
    checks.append(("Extract field = extracted_data_tks", ep.get('field_name') == 'extracted_data_tks'))
    checks.append(("Extract 有 {classify_result_tks}", '{classify_result_tks}' in ep.get('sys_prompt', '')))
    checks.append(("Extract 有 禁止编造", '禁止编造' in ep.get('sys_prompt', '')))

    # Critique
    cr = dsl['components']['Extractor:Critique']['obj']['params']
    checks.append(("Critique model = deepseek-v3.2", cr.get('llm_id') == 'deepseek-v3.2'))
    checks.append(("Critique field = critique_result_kwd", cr.get('field_name') == 'critique_result_kwd'))
    checks.append(("Critique 有 {extracted_data_tks}", '{extracted_data_tks}' in cr.get('sys_prompt', '')))
    checks.append(("Critique 有 OCR 容错", 'OCR' in cr.get('sys_prompt', '')))

    # Frontend/Backend 一致性
    for node in dsl.get('graph', {}).get('nodes', []):
        nid = node.get('id', '')
        form = node.get('data', {}).get('form', {})
        if nid in dsl.get('components', {}):
            backend_prompt = dsl['components'][nid]['obj']['params'].get('sys_prompt', '')
            frontend_prompt = form.get('sys_prompt', '')
            backend_model = dsl['components'][nid]['obj']['params'].get('llm_id', '')
            frontend_model = form.get('llm_id', '')
            if backend_prompt and frontend_prompt:
                checks.append((f"{nid} prompt 前后端一致", backend_prompt == frontend_prompt))
            if backend_model and frontend_model:
                checks.append((f"{nid} model 前后端一致", backend_model == frontend_model))

    # Edges
    edges = [(e.get('source'), e.get('target')) for e in dsl.get('graph', {}).get('edges', [])]
    expected_edges = [
        ('File', 'Parser:MedLink'), ('Parser:MedLink', 'Splitter:MedLink'),
        ('Splitter:MedLink', 'Extractor:Classify'), ('Extractor:Classify', 'Extractor:Extract'),
        ('Extractor:Extract', 'Extractor:Critique'), ('Extractor:Critique', 'Tokenizer:MedEmbed'),
    ]
    for s, t in expected_edges:
        checks.append((f"Edge {s}→{t}", (s, t) in edges))

    passed = sum(1 for _, ok in checks if ok)
    failed = sum(1 for _, ok in checks if not ok)
    return passed, failed, checks


def restore(filepath):
    """从文件恢复 DSL 到 DB"""
    with open(filepath, 'r', encoding='utf-8') as f:
        dsl = json.load(f)

    # 验证
    passed, failed, checks = verify_dsl(dsl)
    if failed > 0:
        print(f"❌ 版本文件验证失败 ({failed} 项):")
        for name, ok in checks:
            if not ok:
                print(f"  ❌ {name}")
        print("放弃恢复。")
        return False

    # 备份当前 DSL
    conn = psycopg2.connect(**DB_CONF)
    cur = conn.cursor()
    cur.execute("SELECT dsl FROM user_canvas WHERE id=%s", (CANVAS_ID,))
    old_dsl = json.loads(cur.fetchone()[0])

    backup_path = os.path.join(VERSION_DIR, f"backup_before_restore_{time.strftime('%Y%m%d_%H%M%S')}.json")
    with open(backup_path, 'w', encoding='utf-8') as f:
        json.dump(old_dsl, f, ensure_ascii=False, indent=2)
    print(f"📦 当前 DSL 已备份: {backup_path}")

    # 写入
    cur.execute(
        "UPDATE user_canvas SET dsl=%s, update_time=EXTRACT(EPOCH FROM NOW())*1000 WHERE id=%s",
        (Json(dsl), CANVAS_ID)
    )
    conn.commit()

    # 读回验证
    cur.execute("SELECT dsl FROM user_canvas WHERE id=%s", (CANVAS_ID,))
    verify = json.loads(cur.fetchone()[0])
    conn.close()

    p2, f2, c2 = verify_dsl(verify)
    if f2 > 0:
        print(f"❌ 写入后验证失败! ({f2} 项)")
        for name, ok in c2:
            if not ok:
                print(f"  ❌ {name}")
        return False

    print(f"✅ DSL 已恢复并验证通过 ({p2}/{p2} 项)")
    return True


def check_current():
    """验证当前 DB 中的 DSL"""
    conn = psycopg2.connect(**DB_CONF)
    cur = conn.cursor()
    cur.execute("SELECT dsl FROM user_canvas WHERE id=%s", (CANVAS_ID,))
    dsl = json.loads(cur.fetchone()[0])
    conn.close()

    passed, failed, checks = verify_dsl(dsl)
    print(f"\n{'='*60}")
    print(f"DSL 全面检查: {passed} 通过, {failed} 失败")
    print(f"{'='*60}")
    for name, ok in checks:
        print(f"  {'✅' if ok else '❌'} {name}")
    print(f"\n{'✅ 全部正确' if failed == 0 else '❌ 有问题需要修复'}")
    return failed == 0


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--check':
        check_current()
    elif len(sys.argv) > 1:
        filepath = sys.argv[1]
        if not os.path.isabs(filepath):
            filepath = os.path.join(VERSION_DIR, filepath)
        if not os.path.exists(filepath):
            print(f"❌ 文件不存在: {filepath}")
            sys.exit(1)
        restore(filepath)
    else:
        if not os.path.exists(LATEST):
            print(f"❌ Latest 版本不存在: {LATEST}")
            sys.exit(1)
        restore(LATEST)
