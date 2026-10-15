#!/usr/bin/env python3
import json
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
QUEUE = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json')
PENDING = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
DUPLICATES = Path('/home/simplifique/.hermes/state/simplifique-social-requests/reconciled/duplicates')
CANONICAL_KEY = 'social-d5384a9b07966269b967802a'
TOPIC_KEY = 'automation-governance-2026-09'
now = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

queue = json.loads(QUEUE.read_text())
canonical = next(
    item for item in queue['items']
    if (item.get('daily_request') or {}).get('request_key') == CANONICAL_KEY
)
if canonical.get('status') != 'ready':
    raise RuntimeError(f'Canonical item is not ready: {canonical.get("status")}')

pending = []
for path in sorted(PENDING.glob('*.json')):
    payload = json.loads(path.read_text())
    if payload.get('topic_key') == TOPIC_KEY:
        pending.append((path, payload))
if not pending:
    print(json.dumps({'reconciled': 0, 'canonical': CANONICAL_KEY}))
    raise SystemExit(0)

keys = [payload['request_key'] for _, payload in pending]
if len(keys) != len(set(keys)):
    raise RuntimeError('Duplicate request_key inside pending batch')

DUPLICATES.mkdir(parents=True, exist_ok=True)
for path, payload in pending:
    target = DUPLICATES / path.name
    if target.exists():
        raise RuntimeError(f'Duplicate archive already exists: {target}')

with sqlite3.connect(DB) as db:
    db.row_factory = sqlite3.Row
    canonical_row = db.execute(
        'SELECT request_key, topic_key, status FROM social_content_requests WHERE request_key=?',
        (CANONICAL_KEY,),
    ).fetchone()
    if canonical_row is None or canonical_row['topic_key'] != TOPIC_KEY or canonical_row['status'] != 'ready':
        raise RuntimeError(f'Canonical DB state invalid: {dict(canonical_row) if canonical_row else None}')
    database_presence = {}
    for key in keys:
        row = db.execute(
            'SELECT request_key, topic_key, status FROM social_content_requests WHERE request_key=?',
            (key,),
        ).fetchone()
        if row is None:
            database_presence[key] = 'not_found_no_mutation'
            continue
        if row['topic_key'] != TOPIC_KEY or row['status'] not in {'queued', 'discarded'}:
            raise RuntimeError(f'Pending DB state invalid for {key}: {dict(row)}')
        db.execute(
            "UPDATE social_content_requests SET status='discarded', decision='discarded', decision_note=?, updated_at=? WHERE request_key=?",
            (f'Duplicado de {CANONICAL_KEY}; mesmo topic_key {TOPIC_KEY}.', now, key),
        )
        database_presence[key] = 'discarded'
    db.commit()

for path, payload in pending:
    payload['reconciliation'] = {
        'status': 'duplicate_archived',
        'duplicate_of': CANONICAL_KEY,
        'topic_key': TOPIC_KEY,
        'reconciled_at': now,
        'database_readback': database_presence[payload['request_key']],
    }
    target = DUPLICATES / path.name
    tmp = target.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
    os.replace(tmp, target)
    path.unlink()

request = canonical.setdefault('daily_request', {})
duplicates = request.setdefault('duplicate_request_keys', [])
for key in keys:
    if key not in duplicates:
        duplicates.append(key)
notes = canonical.setdefault('non_blocking_notes', [])
notes[:] = [note for note in notes if 'clique(s) repetido(s)' not in note]
notes.insert(0, f'{len(duplicates)} clique(s) repetido(s) para o mesmo topic_key foram deduplicados no request canônico.')
canonical['updated_at'] = now
queue_tmp = QUEUE.with_suffix('.json.tmp')
queue_tmp.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + '\n')
os.replace(queue_tmp, QUEUE)

with sqlite3.connect(DB) as db:
    db.row_factory = sqlite3.Row
    readback = {}
    for key in keys:
        row = db.execute(
            'SELECT request_key, status, decision, decision_note FROM social_content_requests WHERE request_key=?',
            (key,),
        ).fetchone()
        readback[key] = dict(row) if row else None
for key, expected in database_presence.items():
    row = readback[key]
    if expected == 'discarded' and (row is None or row['status'] != 'discarded' or row['decision'] != 'discarded'):
        raise RuntimeError(f'Database read-back failed for {key}: {row}')
    if expected == 'not_found_no_mutation' and row is not None:
        raise RuntimeError(f'Unexpected database row appeared for {key}: {row}')
if any((PENDING / f'{key}.json').exists() for key in keys):
    raise RuntimeError('Pending read-back failed')
if any(not (DUPLICATES / f'{key}.json').exists() for key in keys):
    raise RuntimeError('Archive read-back failed')
queue_readback = json.loads(QUEUE.read_text())
item_readback = next(item for item in queue_readback['items'] if (item.get('daily_request') or {}).get('request_key') == CANONICAL_KEY)
recorded = set((item_readback.get('daily_request') or {}).get('duplicate_request_keys') or [])
if not set(keys).issubset(recorded):
    raise RuntimeError('Queue read-back failed')

print(json.dumps({
    'reconciled': len(keys),
    'canonical': CANONICAL_KEY,
    'canonical_status': item_readback.get('status'),
    'canonical_duplicate_count': len(recorded),
    'database_readback': readback,
}, ensure_ascii=False))
