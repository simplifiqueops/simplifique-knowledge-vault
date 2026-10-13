#!/usr/bin/env python3
import json
import sqlite3
from pathlib import Path

queues = [
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json'),
]
request_keys = []
for path in queues:
    data = json.loads(path.read_text())
    print(f'QUEUE {path.name}')
    for item in data.get('items', []):
        request_key = (item.get('daily_request') or {}).get('request_key') or item.get('request_key')
        if request_key:
            request_keys.append(request_key)
        print(json.dumps({
            'order': item.get('order'),
            'content_key': item.get('content_key'),
            'status': item.get('status'),
            'request_status': item.get('request_status'),
            'copy_gate': item.get('copy_gate'),
            'request_key': request_key,
            'planned_for': item.get('planned_for'),
        }, ensure_ascii=False))

con = sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
con.row_factory = sqlite3.Row
print('DB_SOCIAL')
rows = con.execute('''
SELECT request_key, topic_key, topic_title, desired_format, copy_text, planned_for,
       decision, decision_note, approved_by, approved_at, figma_url, status,
       requester, requested_at, updated_at
FROM social_content_requests
ORDER BY requested_at, request_key
''').fetchall()
for row in rows:
    print(json.dumps(dict(row), ensure_ascii=False))
con.close()

print('PENDING')
pending = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
if pending.exists():
    for path in sorted(pending.glob('*.json')):
        print(path)
        print(path.read_text())
