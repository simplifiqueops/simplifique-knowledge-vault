import json
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
PENDING = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
RECONCILED = PENDING.parent / 'reconciled'
RESULT = Path('/home/simplifique/vault/.hermes/tmp/social_pending_reconciliation_result.json')

RECONCILED.mkdir(parents=True, exist_ok=True, mode=0o700)
os.chmod(RECONCILED, 0o700)
now = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
connection = sqlite3.connect(DB)
connection.row_factory = sqlite3.Row
processed = []
skipped = []

try:
    connection.execute('BEGIN IMMEDIATE')
    for path in sorted(PENDING.glob('*.json')):
        payload = json.loads(path.read_text(encoding='utf-8'))
        request_key = payload.get('request_key')
        topic_key = payload.get('topic_key')
        if not request_key or not topic_key:
            skipped.append({'file': str(path), 'reason': 'missing_request_or_topic_key'})
            continue

        existing_key = connection.execute(
            'SELECT request_key,status FROM social_content_requests WHERE request_key=?',
            (request_key,),
        ).fetchone()
        if existing_key:
            canonical_key = existing_key['request_key']
            outcome = 'existing_request_key'
        else:
            canonical = connection.execute(
                """SELECT request_key,user_id,status FROM social_content_requests
                   WHERE topic_key=? AND status!='discarded'
                   ORDER BY requested_at LIMIT 1""",
                (topic_key,),
            ).fetchone()
            if not canonical:
                skipped.append({'file': str(path), 'request_key': request_key, 'reason': 'no_active_canonical_topic'})
                continue
            snapshot = payload.get('topic_snapshot') or {}
            connection.execute(
                """INSERT INTO social_content_requests
                   (request_key,user_id,topic_key,topic_title,sources_json,facts_json,risks_json,
                    desired_format,copy_text,planned_for,decision,decision_note,approved_by,approved_at,
                    figma_url,status,requester,requested_at,updated_at)
                   VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (
                    request_key,
                    canonical['user_id'],
                    topic_key,
                    snapshot.get('title') or topic_key,
                    json.dumps(snapshot.get('sources') or [], ensure_ascii=False),
                    json.dumps(snapshot.get('facts') or [], ensure_ascii=False),
                    json.dumps(snapshot.get('risks') or [], ensure_ascii=False),
                    payload.get('format'),
                    None,
                    payload.get('planned_for'),
                    'discarded',
                    f"Duplicado de {canonical['request_key']}; mesmo topic_key {topic_key}.",
                    None,
                    None,
                    None,
                    'discarded',
                    payload.get('requester') or 'outbox-reconciliation',
                    payload.get('requested_at') or now,
                    now,
                ),
            )
            canonical_key = canonical['request_key']
            outcome = 'inserted_discarded_duplicate'

        target = RECONCILED / path.name
        if target.exists():
            target = RECONCILED / f'{path.stem}-{now.replace(":", "").replace("-", "")}.json'
        os.replace(path, target)
        os.chmod(target, 0o600)
        processed.append({
            'request_key': request_key,
            'topic_key': topic_key,
            'canonical_request_key': canonical_key,
            'outcome': outcome,
            'archived_to': str(target),
        })
    connection.commit()
except Exception:
    connection.rollback()
    raise
finally:
    connection.close()

verification = {'processed': [], 'skipped': skipped, 'pending_remaining': []}
connection = sqlite3.connect(DB)
connection.row_factory = sqlite3.Row
for item in processed:
    row = connection.execute(
        'SELECT request_key,topic_key,status,decision,decision_note FROM social_content_requests WHERE request_key=?',
        (item['request_key'],),
    ).fetchone()
    verification['processed'].append({**item, 'db_readback': dict(row) if row else None})
connection.close()
verification['pending_remaining'] = [str(path) for path in sorted(PENDING.glob('*.json'))]
RESULT.write_text(json.dumps(verification, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
os.chmod(RESULT, 0o600)
print(json.dumps({
    'processed_count': len(verification['processed']),
    'skipped_count': len(skipped),
    'pending_remaining_count': len(verification['pending_remaining']),
    'result': str(RESULT),
}, ensure_ascii=False))
