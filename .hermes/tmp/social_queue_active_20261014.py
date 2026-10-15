import sqlite3, json, glob
con=sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
con.row_factory=sqlite3.Row
sql="""select request_key,topic_key,topic_title,status,decision,decision_note,planned_for,approved_by,approved_at,figma_url,requested_at,updated_at from social_content_requests where status != 'ready' order by requested_at, request_key"""
rows=[dict(r) for r in con.execute(sql)]
print(json.dumps(rows,ensure_ascii=False,indent=2))
con.close()
pending=glob.glob('/home/simplifique/.hermes/state/simplifique-social-requests/pending/*.json')
print('PENDING_COUNT',len(pending))
for path in pending: print(path)
