#!/usr/bin/env python3
import json, os, urllib.request
from datetime import datetime, timezone
from pathlib import Path
out=Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09/L09-C25-sua-empresa-está-funcionando-ou-você-está-compen/figma-comments-readback.json')
token=os.environ.get('FIGMA_ACCESS_TOKEN')
if not token:
    payload={'checked_at':datetime.now(timezone.utc).isoformat(),'status':'token_unavailable','file_key':'aGBW9EAvXjYm9Tz3KkkHcf','section_id':'543:230','comments':[]}
else:
    req=urllib.request.Request('https://api.figma.com/v1/files/aGBW9EAvXjYm9Tz3KkkHcf/comments?as_md=true',headers={'X-Figma-Token':token,'User-Agent':'SimplifiqueSocialQA/1.0'})
    with urllib.request.urlopen(req,timeout=30) as response:
        raw=json.loads(response.read().decode('utf-8'))
    comments=[]
    for c in raw.get('comments',[]):
        meta=c.get('client_meta') or {}
        node_id=meta.get('node_id')
        if node_id in {'543:230','543:231','543:232','543:233','543:234','543:235','543:236','543:237','543:238','543:239','543:240','543:241','543:248'}:
            user=c.get('user') or {}
            comments.append({'id':c.get('id'),'node_id':node_id,'message':c.get('message'),'created_at':c.get('created_at'),'resolved_at':c.get('resolved_at'),'author':user.get('handle') or user.get('display_name')})
    payload={'checked_at':datetime.now(timezone.utc).isoformat(),'status':'read','file_key':'aGBW9EAvXjYm9Tz3KkkHcf','section_id':'543:230','comments':comments,'unresolved_count':sum(1 for c in comments if not c.get('resolved_at'))}
out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(payload,ensure_ascii=False))
