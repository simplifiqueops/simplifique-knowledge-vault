import sqlite3, json
from pathlib import Path
p=Path('/home/simplifique/apps/daily-dashboard/data/users.db')
con=sqlite3.connect(p)
con.row_factory=sqlite3.Row
key='social-l09-c13-202610'
url='https://www.figma.com/design/aGBW9EAvXjYm9Tz3KkkHcf?node-id=419-98'
with con:
    cur=con.execute("update social_content_requests set status=?, figma_url=?, updated_at=? where request_key=? and status='approved_for_production'",('ready',url,'2026-10-03T03:33:01Z',key))
    if cur.rowcount != 1:
        raise SystemExit(f'expected 1 updated row, got {cur.rowcount}')
row=con.execute("select request_key,status,decision,approved_by,approved_at,figma_url,updated_at from social_content_requests where request_key=?",(key,)).fetchone()
print(json.dumps(dict(row),ensure_ascii=False))
con.close()
