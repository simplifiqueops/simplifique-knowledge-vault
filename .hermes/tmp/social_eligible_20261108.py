import sqlite3, json
con=sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
con.row_factory=sqlite3.Row
print('STATUS COUNTS')
for r in con.execute('select status,count(*) n from social_content_requests group by status order by status'): print(dict(r))
print('\nELIGIBLE ORDERED')
q="""select request_key,topic_key,topic_title,desired_format,copy_text,planned_for,decision,decision_note,status,requester,requested_at,updated_at,figma_url from social_content_requests where status in ('queued','copy_in_production','copy_review','changes_requested','approved_for_production','in_production') order by requested_at, coalesce(planned_for,'9999'), request_key"""
for r in con.execute(q):
 d=dict(r); d['copy_text_len']=len(d.get('copy_text') or ''); d.pop('copy_text',None); print(json.dumps(d,ensure_ascii=False))
print('\nL08/RQ DB')
for r in con.execute("select request_key,topic_key,topic_title,status,decision,decision_note,requested_at,updated_at,figma_url,length(copy_text) copy_len from social_content_requests where request_key like 'social-%' and (request_key='social-d5d16909b0f33f9a0bc007d9' or topic_key like '%d5d16909%')"): print(dict(r))
