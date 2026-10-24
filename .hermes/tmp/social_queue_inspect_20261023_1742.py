import json
import sqlite3
import os

queue_paths = [
    "/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json",
    "/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json",
]
for path in queue_paths:
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    print("QUEUE", os.path.basename(path), "items", len(data.get("items", [])))
    for item in data.get("items", []):
        request_key = (item.get("daily_request") or {}).get("request_key") or item.get("request_key")
        print(item.get("order") or item.get("n"), item.get("content_key"), "status=", item.get("status"), "copy_gate=", item.get("copy_gate"), "rk=", request_key, "planned=", item.get("planned_for"))

connection = sqlite3.connect("/home/simplifique/apps/daily-dashboard/data/users.db")
print("TABLES")
for name, sql in connection.execute("select name, sql from sqlite_master where type='table' order by name"):
    print(name, (sql or "")[:1000].replace("\n", " "))

print("JSON CANDIDATES")
for root, dirs, files in os.walk("/home/simplifique/apps/daily-dashboard"):
    dirs[:] = [entry for entry in dirs if entry not in {".git", "node_modules", "__pycache__"}]
    for filename in files:
        if filename.endswith(".json") and ("pending" in root.lower() or "outbox" in root.lower() or "request" in filename.lower()):
            print(os.path.join(root, filename))
