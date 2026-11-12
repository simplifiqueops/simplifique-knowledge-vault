import json, sqlite3
from pathlib import Path
qpaths=[Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json')]
queue={}
for p in qpaths:
 d=json.loads(p.read_text())
 for x in d['items']:
  rk=(x.get('daily_request') or {}).get('request_key') or x.get('request_key')
  if rk: queue[rk]=(p.name,x)
con=sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db'); con.row_factory=sqlite3.Row
print('SCHEMA')
for r in con.execute('pragma table_info(social_content_requests)'): print(tuple(r))
print('\nROWS_FOR_QUEUE')
cols=[r[1] for r in con.execute('pragma table_info(social_content_requests)')]
for rk,(fn,x) in queue.items():
 r=con.execute('select * from social_content_requests where request_key=?',(rk,)).fetchone()
 print('\n',fn,x.get('order'),rk,'queue_status=',x.get('status'),'queue_gate=',x.get('copy_gate'))
 print(dict(r) if r else 'MISSING')
print('\nACTIVE_OR_PENDING')
for r in con.execute("select * from social_content_requests where state not in ('ready','discarded','deferred') order by requested_at, planned_for, request_key"):
 print(dict(r))
con.close()
