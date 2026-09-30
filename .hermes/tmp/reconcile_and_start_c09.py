import datetime as dt
import json
import os
import sqlite3
from collections import defaultdict
from pathlib import Path

QUEUE = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json')
PENDING = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
TARGET = 'social-5fe7013793da6204b625f7a5'
NOW = dt.datetime.now(dt.timezone.utc).isoformat().replace('+00:00', 'Z')

queue = json.loads(QUEUE.read_text(encoding='utf-8'))
by_request = {
    item.get('daily_request', {}).get('request_key'): item
    for item in queue['items'] if item.get('daily_request', {}).get('request_key')
}
max_order = max(item.get('order', 0) for item in queue['items'])
requests = []
for path in sorted(PENDING.glob('*.json')):
    request = json.loads(path.read_text(encoding='utf-8'))
    required = {'request_key', 'topic_key', 'requester', 'requested_at', 'topic_snapshot'}
    missing = required - request.keys()
    if missing:
        raise RuntimeError(f'{path.name}: campos ausentes {sorted(missing)}')
    requests.append((path, request))
groups = defaultdict(list)
for path, request in requests:
    groups[request['topic_key']].append((path, request))

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
try:
    con.execute('BEGIN IMMEDIATE')
    user = con.execute("SELECT id FROM users WHERE username='pablo'").fetchone()
    if not user:
        raise RuntimeError('Usuário pablo não encontrado no DB')
    inserted_db = []
    inserted_queue = []
    deduplicated = {}
    for topic_key, members in groups.items():
        members.sort(key=lambda pair: (pair[1]['requested_at'], pair[1]['request_key']))
        existing = con.execute('SELECT * FROM social_content_requests WHERE user_id=? AND topic_key=?', (user['id'], topic_key)).fetchone()
        canonical = existing['request_key'] if existing else members[0][1]['request_key']
        canonical_request = next((r for _, r in members if r['request_key'] == canonical), members[0][1])
        topic = canonical_request['topic_snapshot']
        if existing is None:
            con.execute('''INSERT INTO social_content_requests
              (request_key,user_id,topic_key,topic_title,sources_json,facts_json,risks_json,
               desired_format,copy_text,planned_for,decision,decision_note,approved_by,approved_at,
               figma_url,status,requester,requested_at,updated_at)
              VALUES (?,?,?,?,?,?,?,?,NULL,?,NULL,NULL,NULL,NULL,NULL,'queued',?,?,?)''',
              (canonical, user['id'], topic_key, topic['title'],
               json.dumps(topic.get('sources', []), ensure_ascii=False),
               json.dumps(topic.get('facts', []), ensure_ascii=False),
               json.dumps(topic.get('risks', []), ensure_ascii=False),
               canonical_request.get('format') or 'carrossel', canonical_request.get('planned_for'),
               canonical_request.get('requester') or 'pablo', canonical_request['requested_at'], NOW))
            inserted_db.append(canonical)
        aliases = [r['request_key'] for _, r in members if r['request_key'] != canonical]
        deduplicated[canonical] = aliases
        if canonical not in by_request:
            max_order += 1
            suffix = canonical.split('-')[-1][:6]
            item = {
                'content_key': f'L08-C{max_order:02d}-governanca-automacoes-{suffix}',
                'order': max_order,
                'status': 'queued',
                'request_status': 'queued',
                'format': 'carousel' if (canonical_request.get('format') or '').lower() in ('carrossel','carousel') else 'static',
                'title': topic['title'],
                'territory': topic.get('territory') or 'automação',
                'source_topic_key': topic_key,
                'objective': topic.get('why_it_matters'),
                'requires_user_on_camera': False,
                'daily_request': {
                    'request_key': canonical,
                    'duplicate_request_keys': aliases,
                    'requested_at': canonical_request['requested_at'],
                    'desired_format': canonical_request.get('format') or 'carrossel',
                    'requester': canonical_request.get('requester'),
                    'planned_for': canonical_request.get('planned_for'),
                },
                'frozen_snapshot': topic,
                'checkpoint': 'daily_request_reconciled',
                'publication_status': 'unpublished',
                'blocking_issues': [],
                'non_blocking_notes': [f'{len(aliases)} clique(s) repetido(s) para o mesmo topic_key foram deduplicados no request canônico.'],
                'updated_at': NOW,
            }
            queue['items'].append(item)
            by_request[canonical] = item
            inserted_queue.append(canonical)
        else:
            by_request[canonical].setdefault('daily_request', {})['duplicate_request_keys'] = aliases

    target_row = con.execute('SELECT status FROM social_content_requests WHERE request_key=?', (TARGET,)).fetchone()
    if not target_row or target_row['status'] != 'approved_for_production':
        raise RuntimeError(f'C09 não está approved_for_production no DB: {dict(target_row) if target_row else None}')
    target_item = by_request[TARGET]
    target_item.update({
        'status': 'in_production', 'request_status': 'in_production',
        'checkpoint': 'approved_copy_confirmed_production_started',
        'updated_at': NOW, 'blocking_issues': [], 'approved_for': 'design_production'
    })
    changed = con.execute("UPDATE social_content_requests SET status='in_production', updated_at=? WHERE request_key=? AND status='approved_for_production'", (NOW, TARGET)).rowcount
    if changed != 1:
        raise RuntimeError('Falha ao marcar C09 in_production')

    temp = QUEUE.with_suffix('.json.tmp')
    temp.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.replace(temp, QUEUE)
    con.commit()

    read_queue = json.loads(QUEUE.read_text(encoding='utf-8'))
    queue_rows = {i.get('daily_request', {}).get('request_key'): i.get('status') for i in read_queue['items'] if i.get('daily_request')}
    keys = [TARGET] + inserted_db
    placeholders = ','.join('?' for _ in keys)
    db_rows = {r['request_key']: r['status'] for r in con.execute(f'SELECT request_key,status FROM social_content_requests WHERE request_key IN ({placeholders})', keys)}
    expected = {TARGET: 'in_production', **{key: 'queued' for key in inserted_db}}
    if any(queue_rows.get(k) != v or db_rows.get(k) != v for k, v in expected.items()):
        raise RuntimeError(f'Read-back divergente: expected={expected} queue={queue_rows} db={db_rows}')
    print(json.dumps({'inserted_db': inserted_db, 'inserted_queue': inserted_queue, 'deduplicated': deduplicated, 'target': TARGET, 'target_status': 'in_production', 'readback': expected}, ensure_ascii=False, indent=2))
except Exception:
    con.rollback()
    raise
finally:
    con.close()
