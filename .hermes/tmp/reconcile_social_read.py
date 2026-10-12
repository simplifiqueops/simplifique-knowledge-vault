import json
import sqlite3

DB = "/home/simplifique/apps/daily-dashboard/data/users.db"
con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
request_keys = [
    "social-d5d16909b0f33f9a0bc007d9",
    "social-l09-c15-202610",
    "social-l09-c18-202610",
    "social-l09-c19-202610",
    "social-l09-c23-202610",
    "social-l09-c24-202610",
    "social-l09-c25-202610",
]
placeholders = ",".join("?" for _ in request_keys)
rows = [dict(row) for row in con.execute(f"""
SELECT request_key, user_id, topic_key, topic_title, desired_format, status,
       requester, requested_at, updated_at, planned_for, decision, decision_note,
       approved_by, approved_at,
       CASE WHEN copy_text IS NULL OR copy_text = '' THEN 0 ELSE 1 END AS has_copy,
       copy_text, figma_url
FROM social_content_requests
WHERE request_key IN ({placeholders})
ORDER BY requested_at, request_key
""", request_keys)]
print(json.dumps(rows, ensure_ascii=False, indent=2))
con.close()
