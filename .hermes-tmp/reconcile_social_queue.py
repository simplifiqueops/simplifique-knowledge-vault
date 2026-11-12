import json, sqlite3
from pathlib import Path
qpaths=[Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json')]
for p in qpaths:
    d=json.loads(p.read_text())
    print('\nQUEUE',p.name,'items',len(d.get('items',[])))
    for x in d.get('items',[]):
        rk=(x.get('daily_request') or {}).get('request_key') or x.get('request_key')
        print(x.get('order'), x.get('content_key'), 'status=',x.get('status'),'copy_gate=',x.get('copy_gate'),'rk=',rk,'planned=',x.get('planned_for'))

db='/home/simplifique/apps/daily-dashboard/data/users.db'
con=sqlite3.connect(db); con.row_factory=sqlite3.Row
print('\nTABLES')
tables=[r[0] for r in con.execute("select name from sqlite_master where type='table' order by name")]
print(tables)
for t in [n for n in tables if any(k in n.lower() for k in ('social','request','content'))]:
    print('\nSCHEMA',t)
    print(con.execute("select sql from sqlite_master where name=?",(t,)).fetchone()[0])
    rows=con.execute(f'SELECT * FROM "{t}" ORDER BY rowid DESC LIMIT 40').fetchall()
    print('ROWS',len(rows))
    for r in rows: print(dict(r))
con.close()
print('\nPENDING FILES')
root=Path('/home/simplifique/apps/daily-dashboard')
for p in root.rglob('*.json'):
    s=str(p).lower()
    if 'pending' in s or 'outbox' in s:
        print(p)
