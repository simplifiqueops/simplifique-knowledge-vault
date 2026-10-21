import json
import os
import sqlite3
from pathlib import Path

queue_paths = [
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json'),
]
for path in queue_paths:
    data = json.loads(path.read_text(encoding='utf-8'))
    print(f'QUEUE {path.name} items={len(data.get("items", []))}')
    for item in data.get('items', []):
        request = item.get('daily_request') or {}
        print(json.dumps({
            'order': item.get('order'),
            'content_key': item.get('content_key'),
            'status': item.get('status'),
            'copy_gate': item.get('copy_gate'),
            'request_key': request.get('request_key'),
            'planned_for': item.get('planned_for'),
        }, ensure_ascii=False))

connection = sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
connection.row_factory = sqlite3.Row
tables = [row[0] for row in connection.execute("select name from sqlite_master where type='table' order by name")]
print('TABLES ' + json.dumps(tables))
for table in tables:
    columns = [row[1] for row in connection.execute(f'pragma table_info({table})')]
    if table == 'social_content_requests':
        print('SCHEMA ' + json.dumps(columns))
        rows = connection.execute(f'select * from {table} order by requested_at asc, rowid asc').fetchall()
        for row in rows:
            print('DBROW ' + json.dumps(dict(row), ensure_ascii=False, default=str))

roots = [
    Path('/home/simplifique/.hermes/state'),
    Path('/home/simplifique/apps/daily-dashboard/data'),
]
for root in roots:
    if root.exists():
        for path in root.rglob('*.json'):
            try:
                text = path.read_text(encoding='utf-8')
            except Exception:
                continue
            if 'social-l08-' in text or 'social-l09-' in text:
                print('PENDING_JSON ' + str(path))
