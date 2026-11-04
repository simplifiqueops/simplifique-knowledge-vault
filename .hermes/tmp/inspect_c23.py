import json
import sqlite3

DB = '/home/simplifique/apps/daily-dashboard/data/users.db'
request_key = 'social-l09-c23-202610'
con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
row = con.execute('SELECT * FROM social_content_requests WHERE request_key=?', (request_key,)).fetchone()
print(json.dumps(dict(row) if row else None, ensure_ascii=False, indent=2))
con.close()
