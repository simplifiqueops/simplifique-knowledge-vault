import json
import sqlite3
from pathlib import Path

DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
with sqlite3.connect(f'file:{DB}?mode=ro', uri=True) as db:
    db.row_factory = sqlite3.Row
    rows = db.execute(
        '''SELECT request_key, topic_key, topic_title, status, decision, decision_note,
                  approved_by, approved_at, planned_for, requested_at, updated_at, figma_url,
                  copy_text
           FROM social_content_requests
           WHERE status NOT IN ('ready', 'discarded')
           ORDER BY requested_at ASC, request_key ASC'''
    ).fetchall()
print(json.dumps([dict(row) for row in rows], ensure_ascii=False, indent=2))
