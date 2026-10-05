import sqlite3, json
p = "/home/simplifique/apps/daily-dashboard/data/users.db"
key = "social-ca05b4e2991132ea799a14be"
figma_url = "https://www.figma.com/design/aGBW9EAvXjYm9Tz3KkkHcf?node-id=457-146"
updated_at = "2026-10-04T16:00:52Z"
con = sqlite3.connect(p)
cur = con.execute("update social_content_requests set status=?, figma_url=?, updated_at=? where request_key=? and status=?", ("ready", figma_url, updated_at, key, "in_production"))
if cur.rowcount != 1:
    con.rollback()
    raise SystemExit(f"expected 1 in_production row, updated {cur.rowcount}")
con.commit()
con.row_factory = sqlite3.Row
row = con.execute("select request_key,status,decision,figma_url,updated_at from social_content_requests where request_key=?", (key,)).fetchone()
print(json.dumps(dict(row), ensure_ascii=False))
