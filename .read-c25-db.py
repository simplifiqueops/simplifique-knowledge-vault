#!/usr/bin/env python3
import json, sqlite3
con=sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
con.row_factory=sqlite3.Row
row=con.execute("SELECT request_key, topic_key, status, updated_at, approved_at, approved_by, copy_text FROM social_content_requests WHERE request_key=?", ('social-l09-c25-202610',)).fetchone()
print(json.dumps(dict(row) if row else None, ensure_ascii=False, indent=2))
