#!/usr/bin/env python3
import json, sqlite3
from pathlib import Path
queues=[Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json')]
records=[]
for qp in queues:
    data=json.loads(qp.read_text(encoding='utf-8'))
    for item in data.get('items',[]):
        key=(item.get('daily_request') or {}).get('request_key') or item.get('request_key')
        if key:
            records.append({'queue':qp.name,'key':key,'order':item.get('order',item.get('n')),'planned_for':item.get('planned_for'),'queue_status':item.get('status'),'copy_gate':item.get('copy_gate'),'title':item.get('title')})
con=sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db'); con.row_factory=sqlite3.Row
keys=[r['key'] for r in records]
rows={r['request_key']:dict(r) for r in con.execute('select request_key,status,decision,planned_for,figma_url,copy_text,updated_at from social_content_requests where request_key in (%s)'%(','.join('?'*len(keys))),keys)}
print('queue_records',len(records),'db_matches',len(rows),'missing_db',len([r for r in records if r['key'] not in rows]))
elig=[]
for r in records:
    d=rows.get(r['key'])
    merged={**r,'db_status':d and d['status'],'db_decision':d and d['decision'],'has_figma':bool(d and d['figma_url']),'has_copy':bool(d and d['copy_text']),'db_updated_at':d and d['updated_at']}
    if (merged['db_status'] in {'queued','copy_in_production','copy_review','changes_requested','approved_for_production','in_production'} or merged['db_decision'] in {'changes_requested','approved_for_production'}) and merged['queue_status']!='ready':
        elig.append(merged)
    if r['key'] not in rows or (r['queue_status']!='ready') or (d and d['status']!='ready'):
        print(json.dumps(merged,ensure_ascii=False))
print('eligible',len(elig))
for x in elig: print('ELIGIBLE',json.dumps(x,ensure_ascii=False))
pending=Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
files=sorted(pending.glob('*.json')) if pending.exists() else []
print('pending_files',len(files))
for p in files: print(p.name)
