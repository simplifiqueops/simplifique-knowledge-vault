import json
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
PENDING = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
DUPLICATES = Path('/home/simplifique/.hermes/state/simplifique-social-requests/reconciled/duplicates')
RESULT = Path('/home/simplifique/vault/.hermes/tmp/social_single_reconciliation_20261025.json')
DUPLICATES.mkdir(parents=True, exist_ok=True, mode=0o700)

candidates = []
for path in PENDING.glob('*.json'):
    payload = json.loads(path.read_text(encoding='utf-8'))
    candidates.append((payload.get('requested_at') or '', path.name, path, payload))
if not candidates:
    raise SystemExit('no pending request')
_, _, source, payload = sorted(candidates)[0]
request_key = payload['request_key']
topic_key = payload['topic_key']
now = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
try:
    con.execute('BEGIN IMMEDIATE')
    existing = con.execute(
        'SELECT request_key,topic_key,status,decision,decision_note FROM social_content_requests WHERE request_key=?',
        (request_key,),
    ).fetchone()
    canonical = con.execute(
        """SELECT request_key,user_id,topic_key,status FROM social_content_requests
           WHERE topic_key=? AND status!='discarded'
           ORDER BY requested_at,request_key LIMIT 1""",
        (topic_key,),
    ).fetchone()
    if canonical is None:
        raise RuntimeError(f'no active canonical request for topic {topic_key}')
    if existing is None:
        snapshot = payload.get('topic_snapshot') or {}
        note = f"Duplicado de {canonical['request_key']}; mesmo topic_key {topic_key}."
        con.execute(
            """INSERT INTO social_content_requests
               (request_key,user_id,topic_key,topic_title,sources_json,facts_json,risks_json,
                desired_format,copy_text,planned_for,decision,decision_note,approved_by,approved_at,
                figma_url,status,requester,requested_at,updated_at)
               VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (
                request_key, canonical['user_id'], topic_key,
                snapshot.get('title') or topic_key,
                json.dumps(snapshot.get('sources') or [], ensure_ascii=False),
                json.dumps(snapshot.get('facts') or [], ensure_ascii=False),
                json.dumps(snapshot.get('risks') or [], ensure_ascii=False),
                payload.get('format'), None, payload.get('planned_for'),
                'discarded', note, None, None, None, 'discarded',
                payload.get('requester') or 'outbox-reconciliation',
                payload.get('requested_at') or now, now,
            ),
        )
    elif existing['status'] != 'discarded':
        raise RuntimeError(f'existing request is not discarded: {dict(existing)}')
    con.commit()
finally:
    con.close()

payload['reconciliation'] = {
    'status': 'duplicate_archived',
    'duplicate_of': canonical['request_key'],
    'topic_key': topic_key,
    'reconciled_at': now,
    'database_readback': 'discarded',
}
destination = DUPLICATES / source.name
if destination.exists():
    raise RuntimeError(f'destination already exists: {destination}')
tmp = destination.with_suffix('.json.tmp')
fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
with os.fdopen(fd, 'w', encoding='utf-8') as handle:
    handle.write(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
    handle.flush()
    os.fsync(handle.fileno())
os.replace(tmp, destination)
source.unlink()

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
row = con.execute(
    'SELECT request_key,topic_key,status,decision,decision_note,updated_at FROM social_content_requests WHERE request_key=?',
    (request_key,),
).fetchone()
canonical_readback = con.execute(
    'SELECT request_key,topic_key,status FROM social_content_requests WHERE request_key=?',
    (canonical['request_key'],),
).fetchone()
con.close()
archive_readback = json.loads(destination.read_text(encoding='utf-8'))
remaining = sorted(p.name for p in PENDING.glob('*.json'))
result = {
    'processed_request_key': request_key,
    'topic_key': topic_key,
    'daily_readback': dict(row) if row else None,
    'canonical_readback': dict(canonical_readback) if canonical_readback else None,
    'archive': str(destination),
    'archive_reconciliation': archive_readback.get('reconciliation'),
    'source_still_pending': source.exists(),
    'pending_remaining_count': len(remaining),
    'pending_remaining': remaining,
}
RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
os.chmod(RESULT, 0o600)
print(json.dumps(result, ensure_ascii=False))
