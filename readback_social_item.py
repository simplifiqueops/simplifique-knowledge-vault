#!/usr/bin/env python3
import json, sqlite3
from pathlib import Path
REQUEST='social-d5d16909b0f33f9a0bc007d9'
Q=Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json')
item=next(i for i in json.loads(Q.read_text())['items'] if (i.get('daily_request') or {}).get('request_key')==REQUEST)
with sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db') as db:
    db.row_factory=sqlite3.Row
    row=db.execute('SELECT request_key,status,decision,approved_by,approved_at,figma_url,updated_at,decision_note FROM social_content_requests WHERE request_key=?',(REQUEST,)).fetchone()
print(json.dumps({'queue':{'status':item.get('status'),'request_status':item.get('request_status'),'checkpoint':item.get('checkpoint'),'approved_for':item.get('approved_for'),'qa_decision':item.get('qa_decision'),'publication_status':item.get('publication_status'),'export_status':item.get('export_status'),'figma_target':item.get('figma_target'),'artifact_count':len(item.get('artifacts',[]))},'db':dict(row) if row else None},ensure_ascii=False,indent=2))
