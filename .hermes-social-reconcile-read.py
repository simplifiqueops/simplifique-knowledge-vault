#!/usr/bin/env python3
import json, sqlite3
from pathlib import Path
queues = [
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json'),
]
items = []
for queue in queues:
    payload = json.loads(queue.read_text())
    for item in payload.get('items', []):
        key = (item.get('daily_request') or {}).get('request_key')
        if key:
            items.append({'queue': queue.name, 'request_key': key, 'content_key': item.get('content_key'), 'queue_status': item.get('status'), 'queue_copy_gate': item.get('copy_gate'), 'planned_for': item.get('planned_for'), 'order': item.get('order')})
con = sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
con.row_factory = sqlite3.Row
keys = [item['request_key'] for item in items]
rows = {}
if keys:
    query = 'select request_key,topic_key,status,decision,decision_note,approved_by,approved_at,figma_url,planned_for,requested_at,updated_at from social_content_requests where request_key in (%s)' % ','.join('?' for _ in keys)
    rows = {row['request_key']: dict(row) for row in con.execute(query, keys)}
for item in items:
    item['daily'] = rows.get(item['request_key'])
pending_dir = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
pending = []
for path in sorted(pending_dir.glob('*.json')):
    try:
        data = json.loads(path.read_text())
    except Exception as exc:
        data = {'error': str(exc)}
    pending.append({'path': str(path), 'request_key': data.get('request_key'), 'status': data.get('status')})
active = [item for item in items if item['queue_status'] not in {'ready','draft_ready','deferred_video','discarded','deferred'} or (item['daily'] and item['daily']['status'] not in {'ready','discarded','deferred'})]
print(json.dumps({'active_or_mismatched': active, 'missing_in_daily': [item for item in items if item['daily'] is None], 'pending': pending}, ensure_ascii=False, indent=2))
