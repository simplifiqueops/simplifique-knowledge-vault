import json
import sqlite3
from pathlib import Path

DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
queue_paths = [
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json'),
]
queue_keys = set()
for queue_path in queue_paths:
    payload = json.loads(queue_path.read_text())
    for item in payload.get('items', []):
        request_key = (item.get('daily_request') or {}).get('request_key') or item.get('request_key')
        if request_key:
            queue_keys.add(request_key)

placeholders = ','.join('?' for _ in queue_keys)
rows = con.execute(
    f'''SELECT request_key, topic_key, topic_title, desired_format, status, decision,
               approved_by, approved_at, figma_url, planned_for, requested_at, updated_at,
               CASE WHEN copy_text IS NULL OR trim(copy_text) = '' THEN 0 ELSE 1 END AS has_copy_text
        FROM social_content_requests
        WHERE request_key IN ({placeholders})
           OR status IN ('queued','copy_in_production','copy_review','changes_requested','approved_for_production')
        ORDER BY requested_at, planned_for, request_key''',
    tuple(sorted(queue_keys)),
).fetchall()
print(json.dumps([dict(row) for row in rows], ensure_ascii=False, indent=2))
