import json, os, sqlite3
from pathlib import Path
queues=[Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json')]
keys=[]
for p in queues:
    data=json.loads(p.read_text())
    print(f'QUEUE {p.name} {len(data.get("items",[]))}')
    for item in data.get('items',[]):
        rk=(item.get('daily_request') or {}).get('request_key') or item.get('request_key')
        keys.append(rk)
        print(json.dumps({'order':item.get('order'),'content_key':item.get('content_key'),'status':item.get('status'),'copy_gate':item.get('copy_gate'),'request_key':rk,'planned_for':item.get('planned_for'),'updated_at':item.get('updated_at')},ensure_ascii=False))
db=sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
db.row_factory=sqlite3.Row
print('DB_SOCIAL')
for row in db.execute('select request_key,topic_key,topic_title,desired_format,status,planned_for,decision,decision_note,approved_by,approved_at,figma_url,requester,requested_at,updated_at,length(copy_text) copy_len from social_content_requests order by requested_at,request_key'):
    print(json.dumps(dict(row),ensure_ascii=False))
db.close()
out=Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
print('PENDING',str(out),out.exists())
if out.exists():
    for p in sorted(out.glob('*.json')):
        try:
            d=json.loads(p.read_text())
            print(json.dumps({'file':str(p),'request_key':d.get('request_key'),'status':d.get('status'),'topic_key':d.get('topic_key')},ensure_ascii=False))
        except Exception as e: print('ERR',p,type(e).__name__)
