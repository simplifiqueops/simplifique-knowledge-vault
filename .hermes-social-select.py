#!/usr/bin/env python3
import json, sqlite3
from pathlib import Path
queues = [
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json'),
]
items = []
for qp in queues:
    data = json.loads(qp.read_text())
    for i in data.get('items', []):
        rk = (i.get('daily_request') or {}).get('request_key') or i.get('request_key')
        if rk:
            items.append((qp.name, i.get('order', i.get('n')), i.get('content_key'), i.get('status'), i.get('copy_gate'), rk, i.get('planned_for')))
con = sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
con.row_factory = sqlite3.Row
by_key = {r['request_key']: dict(r) for r in con.execute('SELECT request_key,status,decision,decision_note,approved_at,figma_url,requested_at,planned_for FROM social_content_requests')}
print('QUEUE_RECONCILIATION')
for x in items:
    q, order, ck, qs, gate, rk, planned = x
    d = by_key.get(rk)
    print(json.dumps({'queue':q,'order':order,'content_key':ck,'queue_status':qs,'copy_gate':gate,'request_key':rk,'planned_for':planned,'daily':d}, ensure_ascii=False))
print('NONTERMINAL_NOT_QUEUED')
keys = {x[5] for x in items}
for rk,d in sorted(by_key.items(), key=lambda kv: (kv[1].get('requested_at') or '', kv[0])):
    if rk not in keys and d.get('status') not in {'ready','discarded','deferred'}:
        print(json.dumps(d, ensure_ascii=False))
print('PENDING_FILES')
pending = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
for p in sorted(pending.glob('*.json')) if pending.exists() else []:
    print(p)
