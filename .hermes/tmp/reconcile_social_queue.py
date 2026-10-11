import json
import sqlite3
from pathlib import Path

DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
QUEUE_PATHS = [
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json'),
]

keys = []
for path in QUEUE_PATHS:
    data = json.loads(path.read_text())
    for item in data.get('items', []):
        key = (item.get('daily_request') or {}).get('request_key')
        if key:
            keys.append(key)

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
for table_row in con.execute("SELECT name, sql FROM sqlite_master WHERE type='table' ORDER BY name"):
    table = table_row['name']
    print(f'\nTABLE {table}')
    print(table_row['sql'])
    columns = [r['name'] for r in con.execute(f'PRAGMA table_info("{table}")')]
    if not columns:
        continue
    likely = [c for c in columns if any(part in c.lower() for part in ('request', 'key', 'status', 'copy', 'planned', 'content', 'topic'))]
    if not likely:
        continue
    where_parts = []
    params = []
    for c in columns:
        for key in keys:
            where_parts.append(f'CAST("{c}" AS TEXT) = ?')
            params.append(key)
    query = f'SELECT * FROM "{table}" WHERE ' + ' OR '.join(where_parts)
    rows = list(con.execute(query, params))
    if rows:
        print(f'MATCHED_ROWS {len(rows)}')
        for row in rows:
            print(json.dumps(dict(row), ensure_ascii=False, default=str))
