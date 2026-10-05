import json, sqlite3
p = "/home/simplifique/apps/daily-dashboard/data/users.db"
key = "social-ca05b4e2991132ea799a14be"
now = "2026-10-04T15:48:10Z"
con = sqlite3.connect(p)
con.row_factory = sqlite3.Row
cur = con.execute("UPDATE social_content_requests SET status='in_production', updated_at=? WHERE request_key=? AND status='approved_for_production'", (now, key))
if cur.rowcount != 1:
    con.rollback()
    row = con.execute("SELECT request_key,status,updated_at FROM social_content_requests WHERE request_key=?", (key,)).fetchone()
    raise SystemExit("unexpected state: " + json.dumps(dict(row) if row else None))
con.commit()
row = con.execute("SELECT request_key,status,updated_at,approved_by,approved_at FROM social_content_requests WHERE request_key=?", (key,)).fetchone()
print(json.dumps(dict(row), ensure_ascii=False))
