import json
import sqlite3
from pathlib import Path

DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
PENDING = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
rows = con.execute("""
SELECT request_key, topic_key, topic_title, desired_format, copy_text, planned_for,
       decision, decision_note, approved_by, approved_at, figma_url, status,
       requester, requested_at, updated_at
FROM social_content_requests
ORDER BY requested_at ASC, request_key ASC
""").fetchall()
print('DB_ROWS')
for row in rows:
    d = dict(row)
    if d.get('copy_text'):
        d['copy_text_len'] = len(d['copy_text'])
        del d['copy_text']
    print(json.dumps(d, ensure_ascii=False, sort_keys=True))
print('PENDING_ROWS')
for p in sorted(PENDING.glob('*.json')):
    try:
        d = json.loads(p.read_text(encoding='utf-8'))
        print(json.dumps({'path': str(p), **d}, ensure_ascii=False, sort_keys=True))
    except Exception as exc:
        print(json.dumps({'path': str(p), 'error': str(exc)}, ensure_ascii=False))
con.close()
