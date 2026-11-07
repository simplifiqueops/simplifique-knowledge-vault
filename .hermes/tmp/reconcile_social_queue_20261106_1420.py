import json
import os
import sqlite3

queue_paths = [
    "/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json",
    "/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json",
]
for path in queue_paths:
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    print("\nQUEUE", path)
    for item in data.get("items", []):
        daily = item.get("daily_request") or {}
        selected = {
            "content_key": item.get("content_key"),
            "order": item.get("order"),
            "status": item.get("status"),
            "copy_gate": item.get("copy_gate"),
            "planned_for": item.get("planned_for"),
            "request_key": daily.get("request_key"),
            "requested_at": daily.get("requested_at"),
            "design_authorized": item.get("design_authorized"),
            "publication_status": item.get("publication_status"),
        }
        print(json.dumps(selected, ensure_ascii=False))

connection = sqlite3.connect("/home/simplifique/apps/daily-dashboard/data/users.db")
connection.row_factory = sqlite3.Row
print("\nTABLES")
for row in connection.execute("SELECT name, sql FROM sqlite_master WHERE type='table' ORDER BY name"):
    print(row["name"], row["sql"])
print("\nSOCIAL TABLES")
query = "SELECT name FROM sqlite_master WHERE type='table' AND (name LIKE '%social%' OR name LIKE '%request%' OR name LIKE '%content%')"
for row in connection.execute(query):
    name = row["name"]
    count = connection.execute(f'SELECT COUNT(*) FROM "{name}"').fetchone()[0]
    columns = [column[1] for column in connection.execute(f'PRAGMA table_info("{name}")')]
    print(name, count)
    print("cols", columns)
    for record in connection.execute(f'SELECT * FROM "{name}" ORDER BY rowid DESC LIMIT 40'):
        print(dict(record))

print("\nPENDING JSONS")
for root, dirs, files in os.walk("/home/simplifique/apps/daily-dashboard"):
    dirs[:] = [directory for directory in dirs if directory not in {".git", "node_modules", "__pycache__", ".venv", "venv"}]
    for filename in files:
        if filename.endswith(".json") and ("pending" in filename.lower() or "outbox" in root.lower() or "pending" in root.lower()):
            print(os.path.join(root, filename))
