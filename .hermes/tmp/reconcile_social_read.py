import json
import sqlite3

DB = "/home/simplifique/apps/daily-dashboard/data/users.db"
con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
print("USERS", json.dumps([dict(row) for row in con.execute("SELECT id, username FROM users ORDER BY id")], ensure_ascii=False, indent=2))
print("REQUESTS", json.dumps([dict(row) for row in con.execute("""
SELECT request_key, user_id, topic_key, topic_title, desired_format, status,
       requester, requested_at, updated_at, planned_for, decision, approved_at,
       CASE WHEN copy_text IS NULL OR copy_text = '' THEN 0 ELSE 1 END AS has_copy,
       figma_url
FROM social_content_requests
ORDER BY requested_at DESC
LIMIT 20
""")], ensure_ascii=False, indent=2))
con.close()
