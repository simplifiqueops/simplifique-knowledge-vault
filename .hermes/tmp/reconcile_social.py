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
order by requested_at, coalesce(planned_for,''), request_key
''').fetchall()
for row in rows:
    print(json.dumps(dict(row), ensure_ascii=False, default=str))
con.close()
