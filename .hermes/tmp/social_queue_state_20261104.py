import json, sqlite3, os
from pathlib import Path
qpaths = [
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json'),
]
queues = {}
for p in qpaths:
    d = json.loads(p.read_text())
    queues[p.name] = d
    print('\nQUEUE', p.name)
    for i in d.get('items', []):
        if i.get('status') not in ('ready','deferred_video','discarded'):
            print(json.dumps(i, ensure_ascii=False, indent=2))
conn = sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
conn.row_factory = sqlite3.Row
print('\nDB NONTERMINAL')
for r in conn.execute("select request_key,topic_key,topic_title,status,decision,decision_note,desired_format,planned_for,requested_at,updated_at,copy_text,figma_url from social_content_requests where status not in ('ready','discarded') order by requested_at,request_key"):
    x=dict(r); x['copy_text_len']=len(x.pop('copy_text') or '')
    print(json.dumps(x, ensure_ascii=False))
print('\nPENDING CANDIDATES')
for root in ('/home/simplifique/apps/daily-dashboard','/home/simplifique/vault/10-Simplifique/Marketing/Conteudo'):
    for dp,dn,fns in os.walk(root):
        dn[:] = [x for x in dn if x not in {'.git','node_modules','__pycache__','venv','.venv'}]
        for fn in fns:
            low=(dp+'/'+fn).lower()
            if fn.endswith('.json') and any(x in low for x in ('pending','outbox','social-request','production-request')):
                print(dp+'/'+fn)
