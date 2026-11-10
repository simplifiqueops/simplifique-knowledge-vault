#!/usr/bin/env python3
import json
import sqlite3
from pathlib import Path

conn = sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
conn.row_factory = sqlite3.Row
rows = conn.execute('''
SELECT request_key, topic_key, topic_title, desired_format, planned_for,
       decision, decision_note, approved_by, approved_at, figma_url, status,
       requester, requested_at, updated_at,
       CASE WHEN copy_text IS NULL OR trim(copy_text) = '' THEN 0 ELSE 1 END AS has_copy
FROM social_content_requests
WHERE status NOT IN ('discarded','ready')
ORDER BY requested_at, planned_for, request_key
''').fetchall()
print('ACTIVE', len(rows))
for row in rows:
    print(json.dumps(dict(row), ensure_ascii=False))
conn.close()

pending = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
files = sorted(pending.glob('*.json')) if pending.exists() else []
print('PENDING', len(files))
for path in files:
    print(path)
    print(path.read_text())
