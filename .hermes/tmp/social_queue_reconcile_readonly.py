import json
import sqlite3
from pathlib import Path

DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
OUTBOX = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
KEYS = {
    'social-l09-c23-202610',
    'social-l09-c24-202610',
    'social-l09-c25-202610',
    'social-d5d16909b0f33f9a0bc007d9',
    'social-ab9a0cf481c526e48bff6603',
}

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
cols = [row['name'] for row in con.execute('PRAGMA table_info(social_content_requests)')]
print('COLUMNS', json.dumps(cols, ensure_ascii=False))
for key in sorted(KEYS):
    row = con.execute('SELECT * FROM social_content_requests WHERE request_key = ?', (key,)).fetchone()
    if row is None:
        print('DB', key, 'MISSING')
        continue
    data = dict(row)
    keep = {k: data.get(k) for k in ('request_key','topic_key','topic_title','desired_format','copy_text','planned_for','decision','decision_note','approved_by','approved_at','figma_url','status','requester','requested_at','updated_at') if k in data}
    print('DB', json.dumps(keep, ensure_ascii=False, sort_keys=True))
print('ACTIVE_DB_REQUESTS')
for row in con.execute("SELECT * FROM social_content_requests WHERE status NOT IN ('ready','discarded','deferred') ORDER BY requested_at, request_key"):
    data = dict(row)
    keep = {k: data.get(k) for k in ('request_key','topic_key','topic_title','desired_format','planned_for','decision','decision_note','approved_by','approved_at','figma_url','status','requester','requested_at','updated_at') if k in data}
    print('ACTIVE', json.dumps(keep, ensure_ascii=False, sort_keys=True))
con.close()

print('PENDING_DIR', OUTBOX, OUTBOX.exists())
if OUTBOX.exists():
    files = sorted(OUTBOX.glob('*.json'))
    print('PENDING_COUNT', len(files))
    for path in files:
        try:
            data = json.loads(path.read_text())
        except Exception as exc:
            print('PENDING_BAD', str(path), type(exc).__name__)
            continue
        key = data.get('request_key')
        print('PENDING', path.name, json.dumps({k: data.get(k) for k in ('request_key','topic_key','topic_title','format','desired_format','requester','requested_at','planned_for') if k in data}, ensure_ascii=False, sort_keys=True))
