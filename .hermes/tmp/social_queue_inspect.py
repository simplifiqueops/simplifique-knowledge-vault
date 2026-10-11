import json, sqlite3, os
paths = [
    '/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json',
    '/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json',
]
for path in paths:
    queue = json.load(open(path, encoding='utf-8'))
    print('\nQUEUE', os.path.basename(path), len(queue.get('items', [])))
    for item in queue.get('items', []):
        print(json.dumps({
            'order': item.get('order'),
            'content_key': item.get('content_key'),
            'status': item.get('status'),
            'copy_gate': item.get('copy_gate'),
            'planned_for': item.get('planned_for'),
            'request_key': (item.get('daily_request') or {}).get('request_key'),
        }, ensure_ascii=False))
con = sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
con.row_factory = sqlite3.Row
print('\nTABLES')
print([r[0] for r in con.execute("select name from sqlite_master where type='table' order by name")])
row = con.execute("select sql from sqlite_master where type='table' and name='social_content_requests'").fetchone()
print('\nSCHEMA')
print(row[0] if row else None)
rows = con.execute('select * from social_content_requests order by requested_at, request_key').fetchall()
print('\nROWS', len(rows))
keep = {'request_key','topic_key','topic_title','desired_format','status','copy_text','planned_for','decision','decision_note','approved_by','approved_at','figma_url','requester','requested_at','updated_at'}
for row in rows:
    print(json.dumps({k: row[k] for k in row.keys() if k in keep}, ensure_ascii=False))
con.close()
