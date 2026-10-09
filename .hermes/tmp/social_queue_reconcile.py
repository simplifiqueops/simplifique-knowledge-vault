import json
import sqlite3
from pathlib import Path
from collections import Counter

queue_paths = [
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json'),
]
items = []
for path in queue_paths:
    payload = json.loads(path.read_text())
    for item in payload.get('items', []):
        daily = item.get('daily_request') or {}
        items.append({
            'queue_path': str(path),
            'queue': path.name,
            'content_key': item.get('content_key'),
            'order': item.get('order'),
            'queue_status': item.get('status'),
            'copy_gate': item.get('copy_gate'),
            'planned_for': item.get('planned_for') or daily.get('planned_for'),
            'request_key': daily.get('request_key') or item.get('request_key'),
            'title': item.get('title'),
        })

connection = sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
connection.row_factory = sqlite3.Row
columns = [row['name'] for row in connection.execute('pragma table_info(social_content_requests)')]
rows = [dict(row) for row in connection.execute(
    'select * from social_content_requests order by requested_at, planned_for, request_key'
)]
by_key = {row['request_key']: row for row in rows}

print('DB_STATUS_COUNTS', json.dumps(Counter(row.get('status') for row in rows), ensure_ascii=False))
print('RECONCILIATION')
for item in items:
    row = by_key.get(item['request_key'])
    if not row:
        continue
    if item['queue_status'] != row.get('status') or row.get('status') in {
        'queued', 'copy_in_production', 'approved_for_production', 'in_production', 'changes_requested'
    }:
        db = {key: row.get(key) for key in (
            'request_key', 'topic_key', 'topic_title', 'desired_format', 'status', 'requester',
            'requested_at', 'updated_at', 'planned_for', 'decision', 'decision_note',
            'approved_by', 'approved_at', 'figma_url'
        ) if key in columns}
        db['copy_text_len'] = len(row.get('copy_text') or '')
        print(json.dumps({'queue': item, 'db': db}, ensure_ascii=False))

print('UNMATCHED_ACTIVE_DB')
queue_keys = {item['request_key'] for item in items if item['request_key']}
for row in rows:
    if row['request_key'] not in queue_keys and row.get('status') in {
        'queued', 'copy_in_production', 'approved_for_production', 'in_production', 'changes_requested'
    }:
        print(json.dumps({key: row.get(key) for key in (
            'request_key', 'topic_key', 'topic_title', 'desired_format', 'status', 'requester',
            'requested_at', 'updated_at', 'planned_for', 'decision', 'decision_note'
        )}, ensure_ascii=False))

pending = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
files = sorted(pending.glob('*')) if pending.exists() else []
print('PENDING_COUNT', len(files))
for path in files:
    try:
        payload = json.loads(path.read_text())
        print(json.dumps({
            'file': str(path),
            **{key: payload.get(key) for key in (
                'request_key', 'topic_key', 'topic_title', 'requested_at', 'planned_for',
                'status', 'desired_format', 'format'
            )}
        }, ensure_ascii=False))
    except Exception as exc:
        print(json.dumps({'file': str(path), 'error': str(exc)}, ensure_ascii=False))
