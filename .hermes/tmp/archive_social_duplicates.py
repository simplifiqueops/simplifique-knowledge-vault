#!/usr/bin/env python3
import json
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
PENDING = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
ARCHIVE = Path('/home/simplifique/.hermes/state/simplifique-social-requests/reconciled/duplicates')
CANONICAL_KEY = 'social-d5384a9b07966269b967802a'
TOPIC_KEY = 'automation-governance-2026-09'

pending = []
for path in sorted(PENDING.glob('*.json')):
    payload = json.loads(path.read_text(encoding='utf-8'))
    if payload.get('topic_key') != TOPIC_KEY:
        raise RuntimeError(f'Pending item has unexpected topic: {path}')
    pending.append((path, payload))

with sqlite3.connect(f'file:{DB}?mode=ro', uri=True) as db:
    db.row_factory = sqlite3.Row
    canonical = db.execute(
        'SELECT request_key, topic_key, status FROM social_content_requests WHERE request_key=?',
        (CANONICAL_KEY,),
    ).fetchone()
    if canonical is None or canonical['topic_key'] != TOPIC_KEY or canonical['status'] != 'ready':
        raise RuntimeError(f'Canonical request is not ready: {dict(canonical) if canonical else None}')
    row_states = {}
    for _, payload in pending:
        row = db.execute(
            'SELECT request_key, topic_key, status, decision_note FROM social_content_requests WHERE request_key=?',
            (payload['request_key'],),
        ).fetchone()
        if row is not None and not (
            row['topic_key'] == TOPIC_KEY
            and row['status'] == 'discarded'
            and CANONICAL_KEY in (row['decision_note'] or '')
        ):
            raise RuntimeError(f'Pending key has non-duplicate DB state: {dict(row)}')
        row_states[payload['request_key']] = 'discarded' if row is not None else 'not_found_no_mutation'

ARCHIVE.mkdir(parents=True, exist_ok=True)
reconciled_at = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
for source, payload in pending:
    target = ARCHIVE / source.name
    if target.exists():
        raise RuntimeError(f'Archive target already exists: {target}')
    payload['reconciliation'] = {
        'status': 'duplicate_archived',
        'duplicate_of': CANONICAL_KEY,
        'topic_key': TOPIC_KEY,
        'reconciled_at': reconciled_at,
        'database_readback': row_states[payload['request_key']],
    }
    temp = target.with_suffix('.json.tmp')
    temp.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.chmod(temp, 0o600)
    os.replace(temp, target)
    source.unlink()

print(json.dumps({
    'archived': len(pending),
    'request_keys': [payload['request_key'] for _, payload in pending],
    'duplicate_of': CANONICAL_KEY,
    'reconciled_at': reconciled_at,
}, ensure_ascii=False))
