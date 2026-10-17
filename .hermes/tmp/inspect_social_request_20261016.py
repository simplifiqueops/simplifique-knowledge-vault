import json
import sqlite3

key = "social-269b378aede4d1cf23eab950"
con = sqlite3.connect("/home/simplifique/apps/daily-dashboard/data/users.db")
con.row_factory = sqlite3.Row
row = con.execute("SELECT * FROM social_content_requests WHERE request_key=?", (key,)).fetchone()
print(json.dumps(dict(row) if row else None, ensure_ascii=False, default=str))
con.close()
