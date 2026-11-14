import json
import sqlite3
from pathlib import Path

DB = "/home/simplifique/apps/daily-dashboard/data/users.db"
con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
print("TABLES")
tables = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
for name in tables:
    print(name)
print("CANDIDATE_SCHEMAS_AND_ROWS")
for name in tables:
    if any(term in name.lower() for term in ("social", "request", "outbox", "editorial", "production")):
        print("SCHEMA", name)
        print(json.dumps([dict(r) for r in con.execute(f'PRAGMA table_info("{name}")')], ensure_ascii=False))
        rows = [dict(r) for r in con.execute(f'SELECT * FROM "{name}" ORDER BY rowid DESC LIMIT 100')]
        print(json.dumps(rows, ensure_ascii=False, default=str))
con.close()
print("PENDING_JSONS")
for root in (Path("/home/simplifique/apps/daily-dashboard"), Path("/home/simplifique/vault")):
    for path in root.rglob("*.json"):
        low = str(path).lower()
        if "pending" in low or "outbox" in low:
            print(path)
