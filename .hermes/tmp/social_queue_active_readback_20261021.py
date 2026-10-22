import json
import sqlite3
from pathlib import Path

con = sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
con.row_factory = sqlite3.Row
rows = [dict(r) for r in con.execute("SELECT request_key, topic_key, topic_title, desired_format, copy_text, planned_for, decision, decision_note, approved_by, approved_at, figma_url, status, requester, requested_at, updated_at FROM social_content_requests WHERE status IN ('queued','copy_in_production','copy_review','changes_requested','approved_for_production','in_production') ORDER BY requested_at, planned_for, request_key")]
print(json.dumps(rows, ensure_ascii=False, indent=2))
