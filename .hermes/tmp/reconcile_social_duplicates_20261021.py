import json, os, sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
PENDING = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
DUPLICATES = Path('/home/simplifique/.hermes/state/simplifique-social-requests/reconciled/duplicates')
CANONICAL_KEY = 'social-d5384a9b07966269b967802a'
CANONICAL_TOPIC = 'automation-governance-2026-09'
TARGET_KEYS = {'social-7e6fc8295004757b854279a5', 'social-81c635504afeceafc0eb0ffd'}

DUPLICATES.mkdir(parents=True, exist_ok=True, mode=0o700)
con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
canonical = con.execute(
    'select request_key, topic_key, status from social_content_requests where request_key=?',
    (CANONICAL_KEY,),
).fetchone()
if not canonical or canonical['topic_key'] != CANONICAL_TOPIC or canonical['status'] != 'ready':
    raise SystemExit('canonical completed request not verified')

archived = []
for source in sorted(PENDING.glob('*.json')):
    payload = json.loads(source.read_text(encoding='utf-8'))
    key = payload.get('request_key')
    if key not in TARGET_KEYS:
        continue
    if payload.get('topic_key') != CANONICAL_TOPIC:
        raise SystemExit(f'unexpected topic for {key}')
    row = con.execute('select request_key from social_content_requests where request_key=?', (key,)).fetchone()
    if row is not None:
        raise SystemExit(f'{key} unexpectedly exists in database')
    payload['reconciliation'] = {
        'status': 'duplicate_archived',
        'duplicate_of': CANONICAL_KEY,
        'topic_key': CANONICAL_TOPIC,
        'reconciled_at': datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        'database_readback': 'not_found_no_mutation',
    }
    destination = DUPLICATES / source.name
    tmp = destination.with_suffix(destination.suffix + '.tmp')
    raw = json.dumps(payload, ensure_ascii=False, indent=2) + '\n'
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, 'w', encoding='utf-8') as handle:
        handle.write(raw)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(tmp, destination)
    source.unlink()
    archived.append((key, destination))

if {key for key, _ in archived} != TARGET_KEYS:
    raise SystemExit(f'expected {sorted(TARGET_KEYS)}, archived {[key for key, _ in archived]}')

for key, destination in archived:
    check = json.loads(destination.read_text(encoding='utf-8'))
    assert check['request_key'] == key
    assert check['reconciliation']['duplicate_of'] == CANONICAL_KEY
    assert check['reconciliation']['status'] == 'duplicate_archived'
    assert con.execute('select count(*) from social_content_requests where request_key=?', (key,)).fetchone()[0] == 0
remaining = [p.name for p in PENDING.glob('*.json')]
print(json.dumps({
    'archived': [key for key, _ in archived],
    'remaining_pending': remaining,
    'canonical': dict(canonical),
}, ensure_ascii=False))
