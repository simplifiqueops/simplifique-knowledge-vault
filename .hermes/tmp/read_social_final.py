import sqlite3, json
p = "/home/simplifique/apps/daily-dashboard/data/users.db"
key = "social-ca05b4e2991132ea799a14be"
con = sqlite3.connect(f"file:{p}?mode=ro", uri=True)
con.row_factory = sqlite3.Row
cols = [dict(r) for r in con.execute("pragma table_info(social_content_requests)")]
row = con.execute("select * from social_content_requests where request_key=?", (key,)).fetchone()
print(json.dumps({"columns": [c["name"] for c in cols], "row": dict(row) if row else None}, ensure_ascii=False))
