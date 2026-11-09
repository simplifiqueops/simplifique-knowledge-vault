import json, sqlite3, os
paths = [
    "/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json",
    "/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json",
]
for path in paths:
    data = json.load(open(path, encoding="utf-8"))
    print("\nQUEUE", os.path.basename(path), "items", len(data.get("items", [])))
    for item in data.get("items", []):
        status = item.get("status")
        gate = item.get("copy_gate")
        request_key = (item.get("daily_request") or {}).get("request_key") or item.get("request_key")
        if status not in ("ready", "deferred_video", "discarded", "published", "scheduled") or gate in ("queued", "copy_in_production", "copy_review", "changes_requested", "approved_for_production"):
            print(item.get("order"), item.get("content_key"), "status=", status, "gate=", gate, "rk=", request_key, "planned=", item.get("planned_for"))
con = sqlite3.connect("/home/simplifique/apps/daily-dashboard/data/users.db")
con.row_factory = sqlite3.Row
tables = [row[0] for row in con.execute("select name from sqlite_master where type='table' order by name")]
print("\nTABLES", tables)
for table in tables:
    if any(key in table for key in ("social", "content", "request")):
        print("\nSCHEMA", table)
        for row in con.execute(f"pragma table_info({table})"):
            print(dict(row))
        print("ROWS")
        for row in con.execute(f"select * from {table} order by rowid desc limit 30"):
            print(dict(row))
print("\nPENDING/OUTBOX/REQUEST JSON FILES")
for root, dirs, files in os.walk("/home/simplifique/apps/daily-dashboard"):
    dirs[:] = [d for d in dirs if d not in {".git", "node_modules", "__pycache__"}]
    for filename in files:
        full = os.path.join(root, filename)
        if filename.endswith(".json") and any(key in full.lower() for key in ("pending", "outbox", "request")):
            print(full)
