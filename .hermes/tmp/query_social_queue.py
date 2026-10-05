import json, sqlite3
p = "/home/simplifique/apps/daily-dashboard/data/users.db"
con = sqlite3.connect(f"file:{p}?mode=ro", uri=True)
con.row_factory = sqlite3.Row
rows = con.execute("""
SELECT request_key, topic_key, topic_title, desired_format, status, requester,
       requested_at, updated_at, planned_for, decision, decision_note,
       approved_by, approved_at, figma_url, copy_text
FROM social_content_requests
WHERE status IN ('queued','copy_in_production','copy_review','changes_requested','approved_for_production','in_production')
ORDER BY requested_at, COALESCE(planned_for,''), request_key
""").fetchall()
print(json.dumps([dict(r) for r in rows], ensure_ascii=False, indent=2))
