import json
import sqlite3
from pathlib import Path

queues = [
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json'),
]
items = []
for queue in queues:
    data = json.loads(queue.read_text(encoding='utf-8'))
    for item in data.get('items', []):
        req = item.get('daily_request') or {}
        key = req.get('request_key') or item.get('request_key')
        if key:
            items.append((key, queue.name, item.get('order'), item.get('content_key'), item.get('status'), item.get('copy_gate'), item.get('planned_for')))

conn = sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
conn.row_factory = sqlite3.Row
rows = {row['request_key']: dict(row) for row in conn.execute('''
SELECT request_key,topic_key,topic_title,desired_format,copy_text,planned_for,decision,
       decision_note,approved_by,approved_at,figma_url,status,requester,requested_at,updated_at
FROM social_content_requests
''')}
conn.close()

pending_dir = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
pending = {}
if pending_dir.is_dir():
    for path in sorted(pending_dir.glob('*.json')):
        try:
            payload = json.loads(path.read_text(encoding='utf-8'))
        except Exception as exc:
            pending[path.name] = {'error': str(exc)}
            continue
        pending[payload.get('request_key') or path.stem] = {'path': str(path), **payload}

keys = {x[0] for x in items}
queue_items = []
for a,b,c,d,e,f,g in items:
    db = rows.get(a)
    queue_items.append({
        'request_key': a, 'queue': b, 'order': c, 'content_key': d,
        'queue_status': e, 'copy_gate': f, 'planned_for': g,
        'db_status': db.get('status') if db else None,
        'db_decision': db.get('decision') if db else None,
        'db_decision_note': db.get('decision_note') if db else None,
        'db_updated_at': db.get('updated_at') if db else None,
        'has_copy': bool(db and db.get('copy_text')),
        'figma_url': db.get('figma_url') if db else None,
        'pending': pending.get(a),
    })
active_states = {'queued','copy_in_production','copy_review','changes_requested','approved_for_production','in_production'}
print(json.dumps({
    'queue_active_or_mismatch': [x for x in queue_items if x['queue_status'] in active_states or x['db_status'] in active_states or x['queue_status'] != x['db_status']],
    'queue_count': len(queue_items),
    'db_only_active': [row for key,row in rows.items() if key not in keys and row.get('status') in active_states],
    'pending_only': [row for key,row in pending.items() if key not in keys],
    'pending_count': len(pending),
}, ensure_ascii=False, indent=2))
