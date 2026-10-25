import json, sqlite3
from pathlib import Path
DB=Path('/home/simplifique/apps/daily-dashboard/data/users.db')
con=sqlite3.connect(DB)
con.row_factory=sqlite3.Row
print('TABLES')
print([r['name'] for r in con.execute("select name from sqlite_master where type='table' order by name")])
print('SCHEMA')
for r in con.execute('pragma table_info(social_content_requests)'):
    print(dict(r))
print('ACTIONABLE_ROWS')
for r in con.execute("select request_key,topic_key,topic_title,desired_format,status,requester,requested_at,updated_at,planned_for,decision_note,figma_url from social_content_requests where status not in ('ready','discarded','deferred') order by requested_at, request_key"):
    print(json.dumps(dict(r), ensure_ascii=False))
print('PENDING_DB_ROWS')
pending_keys=tuple(p.stem for p in Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending').glob('*.json'))
for r in con.execute("select request_key,topic_key,topic_title,status,requested_at,updated_at,planned_for from social_content_requests where request_key in (%s) order by requested_at" % ','.join('?'*len(pending_keys)), pending_keys):
    print(json.dumps(dict(r), ensure_ascii=False))
print('PENDING')
for p in sorted(Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending').glob('*.json')):
    try:
        d=json.loads(p.read_text())
        print(p.name, json.dumps({k:d.get(k) for k in ('request_key','topic_key','status','requested_at','planned_for','format')}, ensure_ascii=False))
    except Exception as e:
        print(p.name,'ERROR',e)
