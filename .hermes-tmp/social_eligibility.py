import json, sqlite3
from pathlib import Path
for p in [Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json')]:
 d=json.loads(p.read_text())
 print('\nQUEUE',p.name)
 for x in d['items']:
  rk=(x.get('daily_request') or {}).get('request_key') or x.get('request_key')
  print(json.dumps({k:x.get(k) for k in ['order','content_key','title','status','copy_gate','checkpoint','updated_at','artifact_directory','blocking_issues']},ensure_ascii=False), 'rk=',rk)
con=sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db'); con.row_factory=sqlite3.Row
print('\nDB NON-READY')
for r in con.execute("select request_key,topic_key,topic_title,status,decision,decision_note,requested_at,updated_at,planned_for,figma_url,length(coalesce(copy_text,'')) copy_len from social_content_requests where status <> 'ready' order by requested_at, planned_for, request_key"):
 print(dict(r))
print('\nDB STATUS COUNTS')
for r in con.execute('select status,count(*) n from social_content_requests group by status order by status'): print(dict(r))
print('\nDUP KEYS', con.execute('select count(*) from (select request_key,count(*) c from social_content_requests group by request_key having c>1)').fetchone()[0])
con.close()
