import json
import sqlite3
from pathlib import Path

DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
PENDING = Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending')

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
tables = [r['name'] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
print('TABLES', json.dumps(tables, ensure_ascii=False))
for table in tables:
    if 'social' not in table and 'request' not in table:
        continue
    print('\nSCHEMA', table)
    print(json.dumps([dict(r) for r in con.execute(f'PRAGMA table_info({table})')], ensure_ascii=False))
    rows = [dict(r) for r in con.execute(f'SELECT * FROM {table} ORDER BY rowid DESC LIMIT 100')]
    print(json.dumps(rows, ensure_ascii=False, indent=2))
print('\nPENDING')
if PENDING.exists():
    for path in sorted(PENDING.glob('*.json')):
        try:
            payload = json.loads(path.read_text())
        except Exception as exc:
            payload = {'error': str(exc)}
        print(path.name, json.dumps(payload, ensure_ascii=False))
else:
    print('MISSING')
