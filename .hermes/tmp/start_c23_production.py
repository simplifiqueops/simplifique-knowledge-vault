import json
import os
import sqlite3
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

REQUEST_KEY = 'social-l09-c23-202610'
CONTENT_KEY = 'L09-C23-automação-sem-trilha-de-decisão-só-deixa-o-erro-'
DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
QUEUE = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json')
now = datetime.now(ZoneInfo('America/Sao_Paulo')).isoformat(timespec='seconds')

con = sqlite3.connect(DB)
try:
    con.execute('BEGIN IMMEDIATE')
    row = con.execute('SELECT status FROM social_content_requests WHERE request_key=?', (REQUEST_KEY,)).fetchone()
    if not row or row[0] not in ('approved_for_production', 'in_production'):
        raise RuntimeError(f'estado Daily inesperado: {row[0] if row else None}')
    con.execute("UPDATE social_content_requests SET status='in_production', updated_at=? WHERE request_key=?", (now, REQUEST_KEY))
    con.commit()
finally:
    con.close()

data = json.loads(QUEUE.read_text(encoding='utf-8'))
item = next((x for x in data['items'] if x.get('content_key') == CONTENT_KEY), None)
if not item:
    raise RuntimeError('item não encontrado na fila')
item['status'] = 'in_production'
item['copy_gate'] = 'approved_for_production'
item['design_authorized'] = True
item['production_started_at'] = now
item['updated_at'] = now
item['checkpoint'] = 'figma_image_led_production_started'
tmp = QUEUE.with_suffix('.json.tmp')
tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
os.replace(tmp, QUEUE)
print(json.dumps({'request_key': REQUEST_KEY, 'daily_status': 'in_production', 'queue_status': item['status'], 'production_started_at': now}, ensure_ascii=False))
