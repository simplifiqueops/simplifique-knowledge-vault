import json
import sqlite3

con = sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
con.row_factory = sqlite3.Row
cols = [r['name'] for r in con.execute('PRAGMA table_info(social_content_requests)')]
print('COLUMNS', json.dumps(cols, ensure_ascii=False))
rows = [dict(r) for r in con.execute('SELECT * FROM social_content_requests ORDER BY requested_at, request_key')]
keep = ['request_key','topic_key','topic_title','desired_format','planned_for','decision','decision_note','requested_at','status','updated_at','copy_text','production_status','figma_url']
for row in rows:
    if row.get('status') not in ('ready','discarded','published','scheduled') or row.get('decision') in ('approved_for_production','changes_requested'):
        out = {k: row.get(k) for k in keep if k in row}
        if out.get('copy_text'):
            out['copy_text'] = out['copy_text'][:160].replace('\n',' / ')
        print(json.dumps(out, ensure_ascii=False, default=str))
con.close()
