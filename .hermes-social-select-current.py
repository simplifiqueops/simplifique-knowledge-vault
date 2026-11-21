import json, sqlite3, os
qpaths=['/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json','/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json']
items=[]
for p in qpaths:
    d=json.load(open(p))
    for i in d.get('items',[]):
        x=dict(i); x['_queue']=p; items.append(x)
con=sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db'); con.row_factory=sqlite3.Row
cols=[r['name'] for r in con.execute('pragma table_info(social_content_requests)')]
print('DB_COLUMNS',cols)
rows=[dict(r) for r in con.execute('select * from social_content_requests')]
by={r.get('request_key'):r for r in rows}
print('DB_ROWS',len(rows))
print('QUEUE_CANDIDATES')
for i in items:
    req=(i.get('daily_request') or {}).get('request_key') or i.get('request_key')
    db=by.get(req,{})
    qstatus=i.get('status'); qgate=i.get('copy_gate'); dstatus=db.get('status'); decision=db.get('decision')
    if qstatus not in ('ready','deferred_video','discarded','published','scheduled') or qgate in ('copy_review','changes_requested','approved_for_production') or dstatus in ('queued','copy_in_production','copy_review','changes_requested','approved_for_production'):
        print(json.dumps({'queue':os.path.basename(i['_queue']),'order':i.get('order'),'content_key':i.get('content_key'),'qstatus':qstatus,'qgate':qgate,'request_key':req,'planned_for':i.get('planned_for'),'db_status':dstatus,'db_decision':decision,'db_note':db.get('decision_note'),'db_updated':db.get('updated_at')},ensure_ascii=False))
pending='/home/simplifique/.hermes/state/simplifique-social-requests/pending'
print('PENDING_DIR',os.path.isdir(pending))
if os.path.isdir(pending):
    for f in sorted(os.listdir(pending)):
        if f.endswith('.json'):
            p=os.path.join(pending,f)
            try:
                d=json.load(open(p)); print('PENDING',f,d.get('request_key'),d.get('status'),d.get('topic_key'))
            except Exception as e: print('BAD_PENDING',f,str(e))
