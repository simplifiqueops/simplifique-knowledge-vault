import sqlite3, json
p='/home/simplifique/apps/daily-dashboard/data/users.db'
con=sqlite3.connect(p); con.row_factory=sqlite3.Row
rows=con.execute("select request_key,topic_key,topic_title,status,decision,decision_note,planned_for,requested_at,updated_at,approved_by,approved_at,figma_url,copy_text from social_content_requests where status!='discarded' order by requested_at, coalesce(planned_for,''), request_key").fetchall()
for r in rows:
 d=dict(r); d['copy_len']=len(d.pop('copy_text') or '')
 print(json.dumps(d,ensure_ascii=False,default=str))
