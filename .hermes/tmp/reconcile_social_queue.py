import json
import sqlite3
from pathlib import Path

queue_paths = [
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json'),
]
items = []
for path in queue_paths:
    data = json.loads(path.read_text(encoding='utf-8'))
    for item in data.get('items', []):
        items.append({
            'queue': path.name,
            'order': item.get('order'),
            'title': item.get('title'),
            'status': item.get('status'),
            'copy_gate': item.get('copy_gate'),
            'planned_for': item.get('planned_for'),
            'request_key': (item.get('daily_request') or {}).get('request_key'),
            'content_key': item.get('content_key'),
            'artifact_directory': item.get('artifact_directory'),
        })

connection = sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
connection.row_factory = sqlite3.Row
rows = {row['request_key']: dict(row) for row in connection.execute(
    'select request_key,topic_key,topic_title,status,planned_for,decision,decision_note,approved_by,approved_at,figma_url,updated_at,requested_at,copy_text from social_content_requests order by requested_at'
)}
print('QUEUE_RECONCILIATION')
for item in items:
    db = rows.get(item['request_key'])
    if item['status'] not in {'ready', 'discarded', 'deferred_video', 'published', 'scheduled'} or (db and db['status'] not in {'ready', 'discarded'}):
        view = dict(item)
        view['db_status'] = db.get('status') if db else None
        view['db_decision'] = db.get('decision') if db else None
        view['db_note'] = db.get('decision_note') if db else None
        view['db_updated_at'] = db.get('updated_at') if db else None
        view['db_requested_at'] = db.get('requested_at') if db else None
        view['db_figma_url'] = db.get('figma_url') if db else None
        print(json.dumps(view, ensure_ascii=False))

queue_keys = {item['request_key'] for item in items if item['request_key']}
print('UNMATCHED_ACTIVE_DB')
for key, row in rows.items():
    if key not in queue_keys and row['status'] not in {'ready', 'discarded'}:
        row.pop('copy_text', None)
        print(json.dumps(row, ensure_ascii=False))

pending = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
print('PENDING')
for path in sorted(pending.glob('*.json')) if pending.exists() else []:
    data = json.loads(path.read_text(encoding='utf-8'))
    print(json.dumps({'file': str(path), **data}, ensure_ascii=False))
