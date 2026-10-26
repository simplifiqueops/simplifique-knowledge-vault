import json
import sqlite3
from pathlib import Path

DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
PENDING = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
Q8 = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json')
Q9 = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json')

keys = []
for queue in (Q8, Q9):
    for item in json.loads(queue.read_text()).get('items', []):
        key = (item.get('daily_request') or {}).get('request_key') or item.get('request_key')
        if key:
            keys.append(key)

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
print('QUEUE_ROWS')
for key in keys:
    row = con.execute('SELECT request_key, topic_key, topic_title, status, decision, decision_note, approved_by, approved_at, figma_url, planned_for, requested_at, updated_at, length(copy_text) AS copy_len FROM social_content_requests WHERE request_key=?', (key,)).fetchone()
    print(json.dumps(dict(row) if row else {'request_key': key, 'missing': True}, ensure_ascii=False))

print('\nACTIVE_OR_RECENT')
for row in con.execute("SELECT request_key, topic_key, topic_title, status, decision, decision_note, approved_by, approved_at, figma_url, planned_for, requested_at, updated_at, length(copy_text) AS copy_len FROM social_content_requests WHERE status NOT IN ('ready','discarded','deferred') ORDER BY requested_at, request_key"):
    print(json.dumps(dict(row), ensure_ascii=False))

print('\nPENDING_GROUPS')
groups = {}
if PENDING.exists():
    for path in PENDING.glob('*.json'):
        payload = json.loads(path.read_text())
        groups.setdefault(payload.get('topic_key'), []).append((payload.get('requested_at'), payload.get('request_key'), path.name))
for topic, entries in sorted(groups.items(), key=lambda kv: min(e[0] or '' for e in kv[1])):
    entries.sort()
    print(json.dumps({'topic_key': topic, 'count': len(entries), 'oldest': entries[0], 'newest': entries[-1]}, ensure_ascii=False))
