#!/usr/bin/env python3
import json
import sqlite3
from pathlib import Path

DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
rows = []
for row in con.execute("""
SELECT request_key, topic_key, topic_title, status, planned_for,
       requested_at, updated_at, decision, decision_note,
       copy_text, figma_url
FROM social_content_requests
WHERE status NOT IN ('ready','discarded','deferred','scheduled','published')
ORDER BY requested_at, planned_for, request_key
"""):
    item = dict(row)
    item['copy_text_len'] = len(item.pop('copy_text') or '')
    rows.append(item)
print(json.dumps(rows, ensure_ascii=False, indent=2))
