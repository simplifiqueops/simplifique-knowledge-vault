#!/usr/bin/env python3
import json, sqlite3
from pathlib import Path
DB=Path('/home/simplifique/apps/daily-dashboard/data/users.db')
keys=[
'social-e88acefa40356db529c779fe',
'social-l09-c15-202610','social-l09-c18-202610','social-l09-c19-202610',
'social-l09-c20-202610','social-l09-c21-202610','social-l09-c22-202610',
'social-l09-c23-202610','social-l09-c24-202610','social-l09-c25-202610',
'social-d9a00c4bae3b06fea931884d','social-5a3dc623786f3d471a85f2ca',
'social-d5d16909b0f33f9a0bc007d9'
]
con=sqlite3.connect(DB); con.row_factory=sqlite3.Row
cols=[r['name'] for r in con.execute('pragma table_info(social_content_requests)')]
print(json.dumps({'columns':cols},ensure_ascii=False))
q='select request_key,topic_key,topic_title,desired_format,copy_text,planned_for,decision,decision_note,approved_by,approved_at,figma_url,status,requester,requested_at,updated_at from social_content_requests where request_key in (%s) or topic_key=? order by requested_at,planned_for'%(','.join('?'*len(keys)))
params=keys+['automation-governance-2026-09']
print(json.dumps([dict(r) for r in con.execute(q,params)],ensure_ascii=False,indent=2))
out=Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
print(json.dumps({'pending':[str(p) for p in sorted(out.glob('*.json'))]},ensure_ascii=False,indent=2))
