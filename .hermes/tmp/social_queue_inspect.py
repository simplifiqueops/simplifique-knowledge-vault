import json, sqlite3
from pathlib import Path
queues = []
for name, path in [('L08','/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),('L09','/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json')]:
    data=json.loads(Path(path).read_text(encoding='utf-8'))
    for item in data.get('items',[]):
        key=(item.get('daily_request') or {}).get('request_key')
        if key: queues.append((name,item.get('order',item.get('n')),key,item.get('status'),item.get('copy_gate'),item.get('planned_for'),item.get('title')))
con=sqlite3.connect('file:/home/simplifique/apps/daily-dashboard/data/users.db?mode=ro',uri=True)
con.row_factory=sqlite3.Row
for q in queues:
    row=con.execute('select request_key,status,decision,decision_note,planned_for,updated_at,figma_url,copy_text from social_content_requests where request_key=?',(q[2],)).fetchone()
    print(json.dumps({'queue':q[0],'order':q[1],'request_key':q[2],'queue_status':q[3],'copy_gate':q[4],'queue_planned_for':q[5],'title':q[6],'db':({**dict(row),'copy_text':bool(row['copy_text'])} if row else None)},ensure_ascii=False))
con.close()
