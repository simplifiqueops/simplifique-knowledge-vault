#!/usr/bin/env python3
import sqlite3, json
con=sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
con.row_factory=sqlite3.Row
print('STATUS_COUNTS')
for r in con.execute('select status,count(*) n from social_content_requests group by status order by status'):
    print(r['status'],r['n'])
print('NONTERMINAL')
for r in con.execute("select request_key,topic_key,topic_title,desired_format,copy_text,planned_for,decision,decision_note,approved_by,approved_at,figma_url,status,requester,requested_at,updated_at from social_content_requests where status not in ('ready','discarded','deferred') order by requested_at,request_key"):
    print(json.dumps(dict(r),ensure_ascii=False))
