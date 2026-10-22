import json, sqlite3
from pathlib import Path
queues = [
 Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),
 Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json')]
keys=[]
for q in queues:
 d=json.loads(q.read_text(encoding='utf-8'))
 print(q.name)
 for i in d.get('items',[]):
  key=(i.get('daily_request') or {}).get('request_key') or i.get('request_key')
  if key: keys.append(key)
  print('|'.join(str(x if x is not None else '') for x in [i.get('order'),key,i.get('status'),i.get('copy_gate'),i.get('planned_for'),i.get('title')]))
con=sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db'); con.row_factory=sqlite3.Row
print('DB_COMPACT')
for key in keys:
 r=con.execute('select request_key,topic_key,topic_title,status,decision,decision_note,planned_for,updated_at from social_content_requests where request_key=?',(key,)).fetchone()
 print(json.dumps(dict(r) if r else {'request_key':key,'missing':True},ensure_ascii=False))
print('PENDING_COMPACT')
for p in sorted(Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending').glob('*.json')):
 d=json.loads(p.read_text(encoding='utf-8'))
 r=con.execute('select request_key,topic_key,status,decision,updated_at from social_content_requests where request_key=?',(d.get('request_key'),)).fetchone()
 print(json.dumps({'file':str(p),'payload':d,'db':dict(r) if r else None},ensure_ascii=False,default=str))
