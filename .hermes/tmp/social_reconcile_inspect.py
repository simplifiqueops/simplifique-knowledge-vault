import json
import sqlite3
from pathlib import Path

DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
PENDING = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
QUEUE_PATHS = [
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json'),
]
keys = []
for queue_path in QUEUE_PATHS:
    data = json.loads(queue_path.read_text(encoding='utf-8'))
    for item in data.get('items', []):
        request_key = (item.get('daily_request') or {}).get('request_key') or item.get('request_key')
        if request_key:
            keys.append(request_key)

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
columns = [row['name'] for row in con.execute('pragma table_info(social_content_requests)')]
print('COLUMNS', json.dumps(columns, ensure_ascii=False))
placeholders = ','.join('?' for _ in keys)
rows = con.execute(
    f'''select * from social_content_requests where request_key in ({placeholders})
        order by requested_at, coalesce(planned_for, ''), request_key''', keys
).fetchall()
print('MATCHED_ROWS', len(rows), 'QUEUE_KEYS', len(set(keys)))
for row in rows:
    obj = dict(row)
    for name in ('sources_json', 'facts_json', 'risks_json'):
        if name in obj and isinstance(obj[name], str) and len(obj[name]) > 200:
            obj[name] = obj[name][:200] + '…'
    print(json.dumps(obj, ensure_ascii=False, default=str))
con.close()

print('PENDING_DIR', str(PENDING), 'EXISTS', PENDING.exists())
if PENDING.exists():
    files = sorted(PENDING.glob('*.json'))
    print('PENDING_COUNT', len(files))
    for path in files:
        try:
            payload = json.loads(path.read_text(encoding='utf-8'))
        except Exception as exc:
            print(json.dumps({'file': str(path), 'error': str(exc)}, ensure_ascii=False))
            continue
        print(json.dumps({'file': str(path), 'request_key': payload.get('request_key'), 'topic_key': payload.get('topic_key'), 'planned_for': payload.get('planned_for'), 'format': payload.get('format')}, ensure_ascii=False))
