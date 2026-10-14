import json
import sqlite3
from pathlib import Path

queue_paths = [
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json'),
]
queue_items = {}
for queue_path in queue_paths:
    payload = json.loads(queue_path.read_text(encoding='utf-8'))
    for item in payload.get('items', []):
        request_key = (item.get('daily_request') or {}).get('request_key') or item.get('request_key')
        if request_key:
            queue_items[request_key] = {
                'queue': queue_path.name,
                'order': item.get('order'),
                'content_key': item.get('content_key'),
                'queue_status': item.get('status'),
                'copy_gate': item.get('copy_gate'),
                'planned_for': item.get('planned_for'),
            }

connection = sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
connection.row_factory = sqlite3.Row
rows = connection.execute('''
SELECT request_key, topic_key, topic_title, status, decision, decision_note,
       planned_for, requested_at, updated_at, approved_at, copy_text, figma_url
FROM social_content_requests
ORDER BY requested_at, COALESCE(planned_for, ''), request_key
''').fetchall()
for row in rows:
    record = dict(row)
    record['copy_text'] = 'present' if record.get('copy_text') else 'missing'
    record['queue'] = queue_items.get(record['request_key'])
    print(json.dumps(record, ensure_ascii=False))
