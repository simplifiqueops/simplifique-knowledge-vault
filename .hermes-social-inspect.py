#!/usr/bin/env python3
import json
import sqlite3
from pathlib import Path

queues = [
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json'),
]
print('QUEUE_CANDIDATES')
request_keys = []
for path in queues:
    data = json.loads(path.read_text(encoding='utf-8'))
    for item in data.get('items', []):
        request_key = (item.get('daily_request') or {}).get('request_key')
        if request_key:
            request_keys.append(request_key)
        if item.get('status') not in {'ready', 'published', 'scheduled', 'discarded', 'deferred_video'}:
            print(json.dumps({
                'queue': path.name,
                'order': item.get('order'),
                'content_key': item.get('content_key'),
                'status': item.get('status'),
                'copy_gate': item.get('copy_gate'),
                'request_key': request_key,
                'planned_for': item.get('planned_for'),
            }, ensure_ascii=False))

con = sqlite3.connect('file:/home/simplifique/apps/daily-dashboard/data/users.db?mode=ro', uri=True)
con.row_factory = sqlite3.Row
print('DB_MATCHES')
if request_keys:
    marks = ','.join('?' for _ in request_keys)
    sql = f'''select request_key, topic_key, topic_title, desired_format, status, decision,
                     decision_note, approved_by, approved_at, planned_for, updated_at, figma_url,
                     copy_text
              from social_content_requests where request_key in ({marks})
              order by requested_at, planned_for, request_key'''
    for row in con.execute(sql, request_keys):
        print(json.dumps(dict(row), ensure_ascii=False))
print('DB_UNMATCHED_ACTIVE')
for row in con.execute('''select request_key, topic_key, topic_title, desired_format, status, decision,
                                 decision_note, approved_by, approved_at, planned_for, requested_at,
                                 updated_at, figma_url, copy_text
                          from social_content_requests
                          where status not in ('ready','discarded')
                          order by requested_at, planned_for, request_key'''):
    if row['request_key'] not in request_keys:
        print(json.dumps(dict(row), ensure_ascii=False))

print('PENDING_JSON')
outbox = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
for path in sorted(outbox.glob('*.json')) if outbox.exists() else []:
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        data = {'error': str(exc)}
    print(path, json.dumps(data, ensure_ascii=False))
