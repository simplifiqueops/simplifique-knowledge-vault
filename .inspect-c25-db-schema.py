#!/usr/bin/env python3
import json, sqlite3
con=sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
con.row_factory=sqlite3.Row
cols=[dict(r) for r in con.execute('PRAGMA table_info(social_content_requests)')]
row=con.execute('SELECT * FROM social_content_requests WHERE request_key=?',('social-l09-c25-202610',)).fetchone()
print(json.dumps({'columns':cols,'row':dict(row) if row else None},ensure_ascii=False,indent=2))
