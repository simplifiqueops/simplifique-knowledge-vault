import json
import sqlite3
from pathlib import Path

DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
rows = con.execute('''
select request_key, topic_key, topic_title, status, requester, requested_at,
       updated_at, decision, decision_note, planned_for, desired_format,
       approved_by, approved_at, figma_url,
       case when copy_text is null then 0 else length(copy_text) end as copy_len
from social_content_requests
where status not in ('ready','discarded')
order by requested_at, coalesce(planned_for,''), request_key
''').fetchall()
print('active_count', len(rows))
for row in rows:
    print(json.dumps(dict(row), ensure_ascii=False, default=str))
con.close()

out = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
files = sorted(out.glob('*.json')) if out.exists() else []
print('pending_count', len(files))
for path in files:
    data = json.loads(path.read_text())
    print(json.dumps({'path': str(path), 'request_key': data.get('request_key'), 'topic_key': data.get('topic_key'), 'status': data.get('status'), 'planned_for': data.get('planned_for')}, ensure_ascii=False))
