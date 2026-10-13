import json
import os
import sqlite3
import tempfile
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

REQUEST_KEY = 'social-l09-c15-202610'
DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
QUEUE = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json')
now = datetime.now(ZoneInfo('America/Sao_Paulo')).isoformat(timespec='seconds')

with sqlite3.connect(DB) as connection:
    connection.row_factory = sqlite3.Row
    connection.execute('BEGIN IMMEDIATE')
    row = connection.execute(
        'select status,decision,approved_by,approved_at from social_content_requests where request_key=?',
        (REQUEST_KEY,),
    ).fetchone()
    if row is None:
        raise SystemExit('request missing')
    if row['status'] not in {'approved_for_production', 'in_production'}:
        raise SystemExit(f'incompatible DB state: {row["status"]}')
    if row['status'] == 'approved_for_production':
        connection.execute(
            "update social_content_requests set status='in_production', updated_at=? where request_key=?",
            (now, REQUEST_KEY),
        )
    approved_by, approved_at = row['approved_by'], row['approved_at']

queue = json.loads(QUEUE.read_text(encoding='utf-8'))
matched = [item for item in queue['items'] if (item.get('daily_request') or {}).get('request_key') == REQUEST_KEY]
if len(matched) != 1:
    raise SystemExit(f'queue match count {len(matched)}')
item = matched[0]
item.update({
    'status': 'in_production',
    'copy_gate': 'approved_for_production',
    'design_authorized': True,
    'publication_authorized': False,
    'approved_by': approved_by,
    'approved_at': approved_at,
    'checkpoint': 'figma_image_led_production_started',
    'production_started_at': now,
    'updated_at': now,
})
fd, temporary = tempfile.mkstemp(prefix='.Lote-09-Fila.', suffix='.tmp', dir=str(QUEUE.parent))
try:
    with os.fdopen(fd, 'w', encoding='utf-8') as handle:
        json.dump(queue, handle, ensure_ascii=False, indent=2)
        handle.write('\n')
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, QUEUE)
finally:
    if os.path.exists(temporary):
        os.unlink(temporary)
print(json.dumps({'request_key': REQUEST_KEY, 'db_status': 'in_production', 'queue_status': item['status'], 'updated_at': now}, ensure_ascii=False))
