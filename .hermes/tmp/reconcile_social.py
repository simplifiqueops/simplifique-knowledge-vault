import sqlite3, json
from pathlib import Path
p=Path('/home/simplifique/apps/daily-dashboard/data/users.db')
con=sqlite3.connect(p)
con.row_factory=sqlite3.Row
keys=['social-l09-c13-202610','social-l09-c15-202610','social-l09-c18-202610','social-l09-c19-202610','social-l09-c23-202610','social-l09-c24-202610','social-l09-c25-202610','social-l09-c16-202610','social-l09-c17-202610','social-l09-c20-202610','social-l09-c21-202610','social-l09-c22-202610','social-e88acefa40356db529c779fe']
q='select request_key,status,requester,requested_at,updated_at,decision,decision_note,copy_text,planned_for,approved_by,approved_at,figma_url from social_content_requests where request_key in (%s) order by requested_at,planned_for' % ','.join('?'*len(keys))
for r in con.execute(q,keys):
    print(json.dumps(dict(r),ensure_ascii=False,default=str))
con.close()
