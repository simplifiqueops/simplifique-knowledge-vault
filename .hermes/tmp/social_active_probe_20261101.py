#!/usr/bin/env python3
import json, sqlite3
from pathlib import Path
con=sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
con.row_factory=sqlite3.Row
rows=con.execute("select request_key,topic_key,topic_title,status,decision,decision_note,approved_by,approved_at,planned_for,figma_url,requested_at,updated_at,length(copy_text) copy_len from social_content_requests where status not in ('ready','discarded') order by requested_at,planned_for,request_key").fetchall()
for row in rows:
 print(json.dumps(dict(row),ensure_ascii=False))
outbox=Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')
print('OUTBOX_EXISTS',outbox.exists())
if outbox.exists():
 for p in sorted(outbox.glob('*.json')):
  print('OUTBOX',p.name,p.read_text(encoding='utf-8'))
