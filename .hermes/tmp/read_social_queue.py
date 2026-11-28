import json
import sqlite3
from pathlib import Path

DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
queue_paths = [
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json'),
]
queue_keys = []
for path in queue_paths:
    data = json.loads(path.read_text(encoding='utf-8'))
    for item in data.get('items', []):
        key = (item.get('daily_request') or {}).get('request_key')
        if key:
            queue_keys.append({'queue': path.name, 'request_key': key, 'queue_status': item.get('status'), 'order': item.get('order')})
with sqlite3.connect(f'file:{DB}?mode=ro', uri=True) as db:
    db.row_factory = sqlite3.Row
    db_rows = {row['request_key']: dict(row) for row in db.execute(
        '''SELECT request_key, topic_key, topic_title, status, decision, decision_note,
                  approved_by, approved_at, planned_for, requested_at, updated_at, figma_url,
                  copy_text
           FROM social_content_requests'''
    ).fetchall()}
counts = {}
for entry in queue_keys:
    counts[entry['request_key']] = counts.get(entry['request_key'], 0) + 1
report = {
    'queue_key_count': len(queue_keys),
    'unique_queue_key_count': len(counts),
    'duplicate_queue_keys': sorted(k for k, n in counts.items() if n > 1),
    'missing_in_db': [entry for entry in queue_keys if entry['request_key'] not in db_rows],
    'matches': [dict(entry, db_status=db_rows[entry['request_key']]['status']) for entry in queue_keys if entry['request_key'] in db_rows],
    'nonterminal_db': [row for row in db_rows.values() if row['status'] not in ('ready', 'discarded')],
}
print(json.dumps(report, ensure_ascii=False, indent=2))
