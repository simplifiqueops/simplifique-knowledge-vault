#!/usr/bin/env python3
import json, sqlite3
from pathlib import Path
queue_paths=[Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json')]
qkeys=set()
for p in queue_paths:
    for item in json.loads(p.read_text()).get('items',[]):
        key=(item.get('daily_request') or {}).get('request_key') or item.get('request_key')
        if key:qkeys.add(key)
con=sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db'); con.row_factory=sqlite3.Row
rows=[dict(r) for r in con.execute("SELECT request_key,topic_key,topic_title,status,decision,decision_note,planned_for,requester,requested_at,updated_at,figma_url,copy_text FROM social_content_requests ORDER BY requested_at,request_key")]
print('DB_COUNT',len(rows),'QUEUE_KEYS',len(qkeys))
for r in rows:
    if r['status'] not in ('ready','discarded','published','scheduled') or r['request_key'] not in qkeys:
        r['in_queue']=r['request_key'] in qkeys
        if r.get('copy_text') is not None:r['copy_text_len']=len(r.pop('copy_text'))
        print(json.dumps(r,ensure_ascii=False))
print('PENDING_FILES')
p=Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
print([str(x) for x in sorted(p.glob('*.json'))] if p.exists() else [])
