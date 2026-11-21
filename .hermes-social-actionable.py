import json, sqlite3, os
qs=[]
for p in ['/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json','/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json']:
 d=json.load(open(p))
 for i in d.get('items',[]):
  req=(i.get('daily_request') or {}).get('request_key') or i.get('request_key')
  qs.append((req,os.path.basename(p),i))
con=sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db'); con.row_factory=sqlite3.Row
rows=[dict(r) for r in con.execute('select * from social_content_requests order by requested_at, request_key')]
qkeys={x[0] for x in qs if x[0]}
from collections import Counter
print('DB_STATUS_COUNTS',Counter(r.get('status') for r in rows))
print('DB_DECISION_COUNTS',Counter(r.get('decision') for r in rows))
print('DB_ACTIONABLE_OR_UNMATCHED')
for r in rows:
 if r.get('status') in ('queued','copy_in_production','copy_review','changes_requested','approved_for_production') or r.get('decision') in ('changes_requested','approved_for_production') or r['request_key'] not in qkeys:
  print(json.dumps({k:r.get(k) for k in ['request_key','topic_key','topic_title','desired_format','planned_for','decision','decision_note','approved_at','figma_url','status','requester','requested_at','updated_at']},ensure_ascii=False))
print('L08_NONFINAL')
for req,q,i in qs:
 if q=='Lote-08-Fila.json' and i.get('status') not in ('ready','deferred_video','discarded','published','scheduled'):
  print(json.dumps(i,ensure_ascii=False))
