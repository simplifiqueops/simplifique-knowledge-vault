import json
import sqlite3
from pathlib import Path

queue_paths = [
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json'),
]
queue_keys = set()
for path in queue_paths:
    data = json.loads(path.read_text(encoding='utf-8'))
    for item in data.get('items', []):
        request_key = (item.get('daily_request') or {}).get('request_key') or item.get('request_key')
        if request_key:
            queue_keys.add(request_key)

active = ('queued', 'copy_in_production', 'copy_review', 'changes_requested', 'approved_for_production', 'in_production')
with sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db') as connection:
    connection.row_factory = sqlite3.Row
    placeholders = ','.join('?' for _ in active)
    rows = connection.execute(
        f'''select request_key, topic_key, topic_title, desired_format, status, decision,
                   decision_note, planned_for, approved_by, approved_at, figma_url,
                   requested_at, updated_at,
                   case when copy_text is null then 0 else length(copy_text) end as copy_chars
            from social_content_requests
            where status in ({placeholders})
            order by requested_at, request_key''',
        active,
    ).fetchall()
    for row in rows:
        record = dict(row)
        record['in_queue'] = record['request_key'] in queue_keys
        print(json.dumps(record, ensure_ascii=False, default=str))
