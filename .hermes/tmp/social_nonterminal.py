import sqlite3, json
con=sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db'); con.row_factory=sqlite3.Row
rows=con.execute("select request_key,topic_key,topic_title,status,decision,decision_note,desired_format,planned_for,requester,requested_at,updated_at,approved_by,approved_at,figma_url,length(copy_text) as copy_len from social_content_requests where status not in ('ready','discarded') order by requested_at, coalesce(planned_for,''), request_key").fetchall()
print(json.dumps([dict(r) for r in rows],ensure_ascii=False,indent=2))
