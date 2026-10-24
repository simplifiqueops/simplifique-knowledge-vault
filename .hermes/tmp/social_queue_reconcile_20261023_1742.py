import json
import sqlite3

DB = "/home/simplifique/apps/daily-dashboard/data/users.db"
QUEUES = [
    "/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json",
    "/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json",
]
queue_by_request = {}
for path in QUEUES:
    data = json.load(open(path, encoding="utf-8"))
    for item in data.get("items", []):
        key = (item.get("daily_request") or {}).get("request_key") or item.get("request_key")
        if key:
            queue_by_request[key] = {
                "queue": path,
                "content_key": item.get("content_key"),
                "order": item.get("order") or item.get("n"),
                "status": item.get("status"),
                "copy_gate": item.get("copy_gate"),
                "planned_for": item.get("planned_for"),
            }

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
rows = con.execute("""
select request_key, topic_key, topic_title, desired_format, status, decision,
       decision_note, approved_by, approved_at, figma_url, planned_for,
       requester, requested_at, updated_at,
       case when copy_text is null then 0 else length(copy_text) end as copy_len
from social_content_requests
where status not in ('ready','discarded')
order by requested_at, request_key
""").fetchall()
print("ACTIVE", len(rows))
for row in rows:
    record = dict(row)
    record["queue"] = queue_by_request.get(row["request_key"])
    print(json.dumps(record, ensure_ascii=False))

print("QUEUE_DB_MISMATCHES")
for key, q in sorted(queue_by_request.items(), key=lambda entry: ((entry[1].get("planned_for") or ""), entry[1].get("order") or 0)):
    row = con.execute("select status, decision, updated_at, case when copy_text is null then 0 else length(copy_text) end from social_content_requests where request_key=?", (key,)).fetchone()
    if row and (q.get("status") != row[0] or (q.get("copy_gate") and q.get("copy_gate") != row[1])):
        print(json.dumps({"request_key": key, "queue": q, "db_status": row[0], "db_decision": row[1], "db_updated_at": row[2], "copy_len": row[3]}, ensure_ascii=False))
con.close()
