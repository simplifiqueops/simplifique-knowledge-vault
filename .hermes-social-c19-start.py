#!/usr/bin/env python3
import json
import sqlite3
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

request_key = 'social-l09-c19-202610'
queue_path = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json')
now = datetime.now(ZoneInfo('America/Sao_Paulo')).isoformat(timespec='seconds')

queue = json.loads(queue_path.read_text())
item = next(x for x in queue['items'] if (x.get('daily_request') or {}).get('request_key') == request_key)
if item.get('status') not in {'copy_review', 'approved_for_production', 'in_production'}:
    raise SystemExit(f"unexpected queue status: {item.get('status')}")
item['status'] = 'in_production'
item['copy_gate'] = 'approved_for_production'
item['design_authorized'] = True
item['approved_by'] = 'pablo'
item['approved_at'] = '2026-10-12T23:25:13Z'
item['production_started_at'] = now
item['checkpoint'] = 'figma_image_led_production_started'
item['updated_at'] = now
queue_path.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + '\n')

with sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db') as db:
    db.row_factory = sqlite3.Row
    row = db.execute('SELECT request_key,status,approved_by,approved_at FROM social_content_requests WHERE request_key=?', (request_key,)).fetchone()
    if not row or row['status'] not in {'approved_for_production', 'in_production'}:
        raise SystemExit(f'unexpected DB row: {dict(row) if row else None}')
    db.execute('UPDATE social_content_requests SET status=?,updated_at=? WHERE request_key=?', ('in_production', now, request_key))
    readback = dict(db.execute('SELECT request_key,status,approved_by,approved_at,updated_at FROM social_content_requests WHERE request_key=?', (request_key,)).fetchone())

queue_check = json.loads(queue_path.read_text())
item_check = next(x for x in queue_check['items'] if (x.get('daily_request') or {}).get('request_key') == request_key)
print(json.dumps({'queue': {'status': item_check['status'], 'copy_gate': item_check['copy_gate'], 'updated_at': item_check['updated_at']}, 'db': readback}, ensure_ascii=False))
