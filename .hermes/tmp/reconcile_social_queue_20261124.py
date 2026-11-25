import json, sqlite3, glob
DB='/home/simplifique/apps/daily-dashboard/data/users.db'
Q=['/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json','/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json']
conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row
tables=[r[0] for r in conn.execute("select name from sqlite_master where type='table' order by name")]
print('TABLES',json.dumps(tables,ensure_ascii=False))
schemas={}
for t in tables:
    cols=[r[1] for r in conn.execute(f'pragma table_info("{t}")')]; schemas[t]=cols
    if any(c in cols for c in ('request_key','copy_text','status','topic_key')): print('SCHEMA',t,json.dumps(cols,ensure_ascii=False))
for qp in Q:
    data=json.load(open(qp)); print('QUEUE',qp)
    for it in data.get('items',[]):
        rk=(it.get('daily_request') or {}).get('request_key')
        if not rk: continue
        hits=[]
        for t,cols in schemas.items():
            if 'request_key' in cols:
                for row in conn.execute(f'SELECT * FROM "{t}" WHERE request_key=?',(rk,)).fetchall():
                    d=dict(row); hits.append({'table':t,**{k:d.get(k) for k in ('id','request_key','topic_key','status','copy_text','planned_for','updated_at','feedback','decision_note') if k in d}})
        print(json.dumps({'request_key':rk,'content_key':it.get('content_key'),'queue_status':it.get('status'),'copy_gate':it.get('copy_gate'),'hits':hits},ensure_ascii=False))
print('JSON_CANDIDATES')
for root in ['/home/simplifique/apps/daily-dashboard/data','/home/simplifique/apps/daily-dashboard/outbox','/home/simplifique/apps/daily-dashboard/runtime']:
    for p in glob.glob(root+'/**/*.json',recursive=True): print(p)
