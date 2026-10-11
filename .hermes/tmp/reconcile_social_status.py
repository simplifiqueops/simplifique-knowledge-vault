import json
import sqlite3
from pathlib import Path

paths = [
 Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),
 Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json'),
]
queue = {}
for path in paths:
 data = json.loads(path.read_text())
 for item in data.get('items', []):
  rk = (item.get('daily_request') or {}).get('request_key')
  if rk:
   queue[rk] = {
    'queue': path.name,
    'content_key': item.get('content_key'),
    'queue_status': item.get('status'),
    'copy_gate': item.get('copy_gate'),
    'planned_for': item.get('planned_for'),
    'order': item.get('order'),
   }
con = sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
con.row_factory = sqlite3.Row
rows = {r['request_key']: dict(r) for r in con.execute('SELECT request_key,status,decision,decision_note,approved_by,approved_at,updated_at,planned_for,figma_url,copy_text FROM social_content_requests')}
for key, q in queue.items():
 r = rows.get(key)
 if not r:
  print(json.dumps({**q,'request_key':key,'db':'MISSING'},ensure_ascii=False)); continue
 if q['queue_status'] != r['status'] or (q['copy_gate'] and q['copy_gate'] != r['status'] and not (q['queue_status']=='ready' and r['status']=='ready')):
  print(json.dumps({**q,'request_key':key,'db_status':r['status'],'decision':r['decision'],'decision_note':r['decision_note'],'approved_by':r['approved_by'],'approved_at':r['approved_at'],'db_updated_at':r['updated_at'],'figma_url':r['figma_url'],'copy_text_present':bool(r['copy_text'])},ensure_ascii=False))
