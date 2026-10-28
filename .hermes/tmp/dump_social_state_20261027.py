import json
import sqlite3
from pathlib import Path

connection = sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
connection.row_factory = sqlite3.Row
rows = connection.execute('''SELECT request_key, topic_key, topic_title, desired_format, planned_for,
 decision, decision_note, approved_by, approved_at, figma_url, status, requester, requested_at, updated_at,
 length(copy_text) AS copy_len
 FROM social_content_requests ORDER BY requested_at, planned_for, request_key''').fetchall()
print('SOCIAL REQUESTS', len(rows))
for row in rows:
    print(json.dumps(dict(row), ensure_ascii=False))
for directory in [
    Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending'),
    Path('/home/simplifique/.hermes/state/simplifique-social-requests/processed'),
]:
    print('DIR', directory)
    if directory.exists():
        for path in sorted(directory.glob('*.json')):
            try:
                data = json.loads(path.read_text())
                print(json.dumps({'path': str(path), 'request_key': data.get('request_key'), 'status': data.get('status'), 'requested_at': data.get('requested_at'), 'planned_for': data.get('planned_for')}, ensure_ascii=False))
            except Exception as exc:
                print(json.dumps({'path': str(path), 'error': str(exc)}, ensure_ascii=False))
    else:
        print('MISSING')
