import json
import sqlite3
from pathlib import Path

queue_paths = [
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json'),
]
for path in queue_paths:
    data = json.loads(path.read_text())
    print(f'QUEUE {path.name} items={len(data.get("items", []))}')
    for item in data.get('items', []):
        request_key = (item.get('daily_request') or {}).get('request_key') or item.get('request_key')
        print(json.dumps({
            'order': item.get('order', item.get('n')),
            'status': item.get('status'),
            'copy_gate': item.get('copy_gate'),
            'request_key': request_key,
            'planned_for': item.get('planned_for'),
            'title': item.get('title'),
        }, ensure_ascii=False))

connection = sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
connection.row_factory = sqlite3.Row
print('DB TABLES')
for row in connection.execute("SELECT name, sql FROM sqlite_master WHERE type='table' ORDER BY name"):
    print(row['name'], (row['sql'] or '')[:1200])

print('PENDING FILES')
for root in [Path('/home/simplifique/apps/daily-dashboard'), Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo')]:
    for path in root.rglob('*'):
        if path.is_file() and ('pending' in path.name.lower() or 'outbox' in str(path).lower()):
            print(path)
