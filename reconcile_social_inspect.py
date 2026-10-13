#!/usr/bin/env python3
import json
import sqlite3
from pathlib import Path
DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
PENDING = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
QUEUES = [Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'), Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json')]
print('QUEUE_ITEMS')
for queue in QUEUES:
    data = json.loads(queue.read_text())
    for item in data.get('items', []):
        req = item.get('daily_request') or {}
        print(json.dumps({'queue': queue.name, 'order': item.get('order'), 'content_key': item.get('content_key'), 'request_key': req.get('request_key'), 'topic_key': item.get('source_topic_key') or item.get('topic_key'), 'status': item.get('status'), 'copy_gate': item.get('copy_gate'), 'planned_for': item.get('planned_for') or req.get('planned_for'), 'requested_at': req.get('requested_at')}, ensure_ascii=False, sort_keys=True))
print('PENDING')
for path in sorted(PENDING.glob('*.json')):
    data = json.loads(path.read_text())
    print(json.dumps({'file': path.name, 'request_key': data.get('request_key'), 'topic_key': data.get('topic_key'), 'requested_at': data.get('requested_at'), 'planned_for': data.get('planned_for')}, ensure_ascii=False, sort_keys=True))
with sqlite3.connect(DB) as db:
    db.row_factory = sqlite3.Row
    rows = db.execute('SELECT request_key, topic_key, topic_title, desired_format, status, requester, requested_at, updated_at, planned_for, decision, decision_note, approved_by, approved_at, figma_url, copy_text FROM social_content_requests ORDER BY requested_at, request_key').fetchall()
print('DB_ROWS')
for row in rows:
    print(json.dumps(dict(row), ensure_ascii=False, sort_keys=True))
