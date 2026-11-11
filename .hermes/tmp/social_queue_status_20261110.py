import json
import sqlite3
from pathlib import Path
from collections import Counter

queue_paths = [
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'),
    Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json'),
]
connection = sqlite3.connect('file:/home/simplifique/apps/daily-dashboard/data/users.db?mode=ro', uri=True)
connection.row_factory = sqlite3.Row
rows = [dict(row) for row in connection.execute('select * from social_content_requests')]
by_key = {row['request_key']: row for row in rows}
for path in queue_paths:
    payload = json.loads(path.read_text(encoding='utf-8'))
    print('QUEUE', path.name, 'COUNTS', dict(Counter(item.get('status') for item in payload.get('items', []))))
    for item in payload.get('items', []):
        daily = item.get('daily_request') or {}
        key = daily.get('request_key') or item.get('request_key')
        qstatus = item.get('status')
        db = by_key.get(key)
        dbstatus = db.get('status') if db else None
        if qstatus not in {'ready', 'discarded', 'deferred_video'} or (dbstatus and dbstatus not in {'ready', 'discarded'}):
            print(json.dumps({
                'queue': path.name,
                'order': item.get('order'),
                'content_key': item.get('content_key'),
                'title': item.get('title'),
                'queue_status': qstatus,
                'copy_gate': item.get('copy_gate'),
                'request_key': key,
                'db_status': dbstatus,
                'db_decision': db.get('decision') if db else None,
                'planned_for': item.get('planned_for') or daily.get('planned_for'),
                'publication_status': item.get('publication_status'),
                'publication_authorized': item.get('publication_authorized'),
                'zernio_post_id': item.get('zernio_post_id'),
                'publishing': item.get('publishing'),
                'checkpoint': item.get('checkpoint'),
                'artifacts': item.get('artifacts'),
            }, ensure_ascii=False))
