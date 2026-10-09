import json
import sqlite3
from pathlib import Path

DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
query = '''
SELECT request_key, topic_key, topic_title, desired_format, status, planned_for,
       decision, decision_note, approved_by, approved_at, figma_url,
       requester, requested_at, updated_at
FROM social_content_requests
ORDER BY requested_at, planned_for, request_key
'''
for row in conn.execute(query):
    print(json.dumps(dict(row), ensure_ascii=False))
