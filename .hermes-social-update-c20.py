#!/usr/bin/env python3
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
REQUEST_KEY = 'social-l09-c20-202610'
FIGMA_URL = 'https://www.figma.com/design/aGBW9EAvXjYm9Tz3KkkHcf?node-id=444-122'

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
try:
    con.execute('BEGIN IMMEDIATE')
    before = con.execute(
        'SELECT request_key, decision, status, figma_url FROM social_content_requests WHERE request_key = ?',
        (REQUEST_KEY,),
    ).fetchone()
    if before is None:
        raise RuntimeError('request not found')
    if before['decision'] != 'approved_for_production':
        raise RuntimeError(f"unexpected decision: {before['decision']!r}")
    if before['status'] not in ('approved_for_production', 'in_production', 'ready'):
        raise RuntimeError(f"unexpected status: {before['status']!r}")
    now = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    con.execute(
        '''UPDATE social_content_requests
           SET figma_url = ?, status = 'ready', updated_at = ?
           WHERE request_key = ?''',
        (FIGMA_URL, now, REQUEST_KEY),
    )
    con.commit()
    after = con.execute(
        '''SELECT request_key, topic_key, decision, approved_by, approved_at,
                  figma_url, status, updated_at
           FROM social_content_requests WHERE request_key = ?''',
        (REQUEST_KEY,),
    ).fetchone()
    print(json.dumps({'before': dict(before), 'after': dict(after)}, ensure_ascii=False))
finally:
    con.close()
