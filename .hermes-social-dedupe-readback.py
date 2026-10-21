import json, sqlite3
from pathlib import Path
key='social-36af0dc2e866f470bf886e0b'
db=sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
db.row_factory=sqlite3.Row
row=db.execute('select request_key,topic_key,status,decision,decision_note,requested_at,updated_at from social_content_requests where request_key=?',(key,)).fetchone()
print(json.dumps(dict(row) if row else None,ensure_ascii=False))
db.close()
print('pending_exists',Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending/'+key+'.json').exists())
print('archive_exists',Path('/home/simplifique/.hermes/state/simplifique-social-requests/reconciled/duplicates/'+key+'.json').exists())
