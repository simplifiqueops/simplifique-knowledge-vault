#!/usr/bin/env python3
import json
import os
import sqlite3
from pathlib import Path

NOW = '2026-10-12T19:09:09-03:00'
DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
QUEUE = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json')
PENDING = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
PROCESSED = Path('/home/simplifique/.hermes/state/simplifique-social-requests/processed')
CANONICAL_KEY = 'social-d5384a9b07966269b967802a'
TOPIC_KEY = 'automation-governance-2026-09'
ACTIVE_KEY = 'social-d5d16909b0f33f9a0bc007d9'

data = json.loads(QUEUE.read_text())
canonical = next(i for i in data['items'] if (i.get('daily_request') or {}).get('request_key') == CANONICAL_KEY)
active = next(i for i in data['items'] if (i.get('daily_request') or {}).get('request_key') == ACTIVE_KEY)

pending_files = []
for path in sorted(PENDING.glob('*.json')):
    payload = json.loads(path.read_text())
    if payload.get('topic_key') != TOPIC_KEY:
        raise RuntimeError(f'Unexpected pending topic: {path}')
    pending_files.append((path, payload))

with sqlite3.connect(DB) as db:
    db.row_factory = sqlite3.Row
    active_row = db.execute('SELECT status, decision, approved_by, approved_at FROM social_content_requests WHERE request_key=?', (ACTIVE_KEY,)).fetchone()
    if active_row is None or active_row['status'] != 'approved_for_production' or active_row['decision'] != 'approved_for_production':
        raise RuntimeError(f'Active Daily state not approved: {dict(active_row) if active_row else None}')
    for path, payload in pending_files:
        key = payload['request_key']
        row = db.execute('SELECT status, topic_key FROM social_content_requests WHERE request_key=?', (key,)).fetchone()
        if row is None:
            continue
        if row['topic_key'] != TOPIC_KEY:
            raise RuntimeError(f'Topic mismatch for {key}: {row["topic_key"]}')
        db.execute("UPDATE social_content_requests SET status='discarded', decision='discarded', decision_note=?, updated_at=? WHERE request_key=?", (f'Duplicado de {CANONICAL_KEY}; mesmo topic_key {TOPIC_KEY}.', NOW, key))
    db.commit()

PROCESSED.mkdir(parents=True, exist_ok=True)
for path, payload in pending_files:
    target = PROCESSED / path.name
    if target.exists():
        raise RuntimeError(f'Processed target already exists: {target}')
    os.replace(path, target)

req = canonical.setdefault('daily_request', {})
dupes = req.setdefault('duplicate_request_keys', [])
for _, payload in pending_files:
    if payload['request_key'] not in dupes:
        dupes.append(payload['request_key'])
canonical.setdefault('non_blocking_notes', [])
canonical['non_blocking_notes'] = [n for n in canonical['non_blocking_notes'] if 'clique(s) repetido(s)' not in n]
canonical['non_blocking_notes'].insert(0, f'{len(dupes)} clique(s) repetido(s) para o mesmo topic_key foram deduplicados no request canônico.')
canonical['updated_at'] = NOW

active['status'] = 'approved_for_production'
active['request_status'] = 'approved_for_production'
active['copy_gate'] = 'approved_for_production'
active['design_authorized'] = True
active['approved_by'] = active_row['approved_by']
active['approved_at'] = active_row['approved_at']
active['checkpoint'] = 'daily_approval_reconciled_for_visual_production'
active['updated_at'] = NOW

text = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
tmp = QUEUE.with_suffix('.json.tmp')
tmp.write_text(text)
os.replace(tmp, QUEUE)

print(json.dumps({'discarded_pending': len(pending_files), 'canonical_duplicate_count': len(dupes), 'active_request': ACTIVE_KEY, 'active_status': active['status']}, ensure_ascii=False))
