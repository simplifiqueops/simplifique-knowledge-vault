import json
import sqlite3
from pathlib import Path

connection = sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
connection.row_factory = sqlite3.Row
rows = connection.execute('''SELECT request_key, topic_key, topic_title, desired_format, planned_for,
 decision, decision_note, approved_by, approved_at, figma_url, status, requester, requested_at, updated_at,
 length(copy_text) AS copy_len
 FROM social_content_requests
 WHERE status NOT IN ('ready','discarded')
 ORDER BY requested_at, CASE WHEN planned_for IS NULL THEN 1 ELSE 0 END, planned_for, request_key''').fetchall()
print('NONTERMINAL', len(rows))
for row in rows:
    print(json.dumps(dict(row), ensure_ascii=False))
print('STATUS COUNTS')
for row in connection.execute('SELECT status, count(*) AS count FROM social_content_requests GROUP BY status ORDER BY status'):
    print(dict(row))
