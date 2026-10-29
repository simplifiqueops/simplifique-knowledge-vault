import json
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
QUEUE = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json')
PENDING = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
ARCHIVE = Path('/home/simplifique/.hermes/state/simplifique-social-requests/reconciled/duplicates')
CANONICAL_KEY = 'social-d5384a9b07966269b967802a'
TOPIC_KEY = 'automation-governance-2026-09'
NOW = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

def atomic_json(path, payload, mode=0o600):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.tmp')
    text = json.dumps(payload, ensure_ascii=False, indent=2) + '\n'
    with open(tmp, 'w', encoding='utf-8') as handle:
        handle.write(text)
        handle.flush()
        os.fsync(handle.fileno())
    os.chmod(tmp, mode)
    os.replace(tmp, path)

pending_records = []
for path in sorted(PENDING.glob('*.json')):
    data = json.loads(path.read_text(encoding='utf-8'))
    if data.get('topic_key') != TOPIC_KEY:
        raise SystemExit(f'unexpected pending topic: {path.name} -> {data.get("topic_key")}')
    if path.stem != data.get('request_key'):
        raise SystemExit(f'request key mismatch: {path.name}')
    pending_records.append((path, data))

if not pending_records:
    print(json.dumps({'status': 'nothing_to_reconcile'}))
    raise SystemExit(0)

queue = json.loads(QUEUE.read_text(encoding='utf-8'))
items = [item for item in queue['items'] if (item.get('daily_request') or {}).get('request_key') == CANONICAL_KEY]
if len(items) != 1:
    raise SystemExit(f'canonical queue item count is {len(items)}')
item = items[0]
if item.get('source_topic_key') != TOPIC_KEY or item.get('status') != 'ready':
    raise SystemExit('canonical queue item is not the expected ready item')

keys = [data['request_key'] for _, data in pending_records]
db_readbacks = {}
con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
try:
    con.execute('BEGIN IMMEDIATE')
    for key in keys:
        row = con.execute('SELECT request_key, topic_key, status FROM social_content_requests WHERE request_key=?', (key,)).fetchone()
        if row is None:
            db_readbacks[key] = 'missing'
            continue
        if row['topic_key'] != TOPIC_KEY:
            raise RuntimeError(f'topic mismatch in database: {key}')
        if row['status'] not in ('queued', 'discarded'):
            raise RuntimeError(f'unexpected database state {row["status"]}: {key}')
        con.execute(
            '''UPDATE social_content_requests
               SET status='discarded', decision='discarded', decision_note=?, updated_at=?
               WHERE request_key=?''',
            (f'Duplicado de {CANONICAL_KEY}; mesmo topic_key {TOPIC_KEY}.', NOW, key),
        )
        db_readbacks[key] = 'discarded'
    con.commit()
except Exception:
    con.rollback()
    raise
finally:
    con.close()

existing = set((item.get('daily_request') or {}).get('duplicate_request_keys') or [])
existing.update(keys)
item['daily_request']['duplicate_request_keys'] = sorted(existing)
item['updated_at'] = NOW
for note_index, note in enumerate(item.get('non_blocking_notes') or []):
    if 'clique(s) repetido(s)' in note and 'request canônico' in note:
        item['non_blocking_notes'][note_index] = (
            f'{len(existing)} clique(s) repetido(s) para o mesmo topic_key foram deduplicados no request canônico.'
        )
        break
atomic_json(QUEUE, queue, mode=0o644)

ARCHIVE.mkdir(parents=True, exist_ok=True, mode=0o700)
for source, data in pending_records:
    data['reconciliation'] = {
        'status': 'duplicate_archived' if db_readbacks[data['request_key']] == 'discarded' else 'duplicate_orphan_archived',
        'duplicate_of': CANONICAL_KEY,
        'topic_key': TOPIC_KEY,
        'reconciled_at': NOW,
        'database_readback': db_readbacks[data['request_key']],
    }
    target = ARCHIVE / source.name
    atomic_json(target, data, mode=0o600)
    source.unlink()

con = sqlite3.connect(DB)
rows = con.execute(
    f"SELECT request_key,status,decision FROM social_content_requests WHERE request_key IN ({','.join('?' for _ in keys)}) ORDER BY request_key",
    keys,
).fetchall()
con.close()
db_rows = {row[0]: (row[1], row[2]) for row in rows}
queue_rb = json.loads(QUEUE.read_text(encoding='utf-8'))
item_rb = next(i for i in queue_rb['items'] if (i.get('daily_request') or {}).get('request_key') == CANONICAL_KEY)
archived = sorted(path.name for path in ARCHIVE.glob('*.json') if path.stem in set(keys))
remaining = sorted(path.name for path in PENDING.glob('*.json'))
database_readback_ok = all(
    (db_readbacks[key] == 'missing' and key not in db_rows)
    or (db_readbacks[key] == 'discarded' and db_rows.get(key) == ('discarded', 'discarded'))
    for key in keys
)
result = {
    'status': 'reconciled',
    'count': len(keys),
    'database_readback_ok': database_readback_ok,
    'database_missing_count': sum(1 for value in db_readbacks.values() if value == 'missing'),
    'database_discarded_count': sum(1 for value in db_readbacks.values() if value == 'discarded'),
    'queue_contains_all': set(keys).issubset(set(item_rb['daily_request']['duplicate_request_keys'])),
    'queue_duplicate_count': len(item_rb['daily_request']['duplicate_request_keys']),
    'archive_count': len(archived),
    'pending_remaining': remaining,
    'canonical_status': item_rb.get('status'),
    'reconciled_at': NOW,
}
print(json.dumps(result, ensure_ascii=False, sort_keys=True))
if not all((result['database_readback_ok'], result['queue_contains_all'], result['archive_count'] == len(keys), not remaining)):
    raise SystemExit(2)
