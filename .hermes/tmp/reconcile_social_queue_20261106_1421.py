import json
import sqlite3

queue_paths = [
    "/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json",
    "/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json",
]
queue_items = []
for queue_path in queue_paths:
    with open(queue_path, encoding="utf-8") as handle:
        queue = json.load(handle)
    for item in queue.get("items", []):
        request_key = (item.get("daily_request") or {}).get("request_key")
        if request_key:
            queue_items.append((queue_path, item, request_key))

connection = sqlite3.connect("/home/simplifique/apps/daily-dashboard/data/users.db")
connection.row_factory = sqlite3.Row
print("ELIGIBLE_DB_ROWS")
for row in connection.execute("SELECT * FROM social_content_requests WHERE status IN ('queued','copy_in_production','copy_review','changes_requested','approved_for_production','in_production') ORDER BY requested_at, COALESCE(planned_for,''), request_key"):
    print(json.dumps(dict(row), ensure_ascii=False))
print("\nQUEUE_RECONCILIATION")
for queue_path, item, request_key in queue_items:
    row = connection.execute("SELECT request_key, topic_key, topic_title, desired_format, planned_for, decision, decision_note, approved_by, approved_at, figma_url, status, requester, requested_at, updated_at, copy_text FROM social_content_requests WHERE request_key=?", (request_key,)).fetchone()
    print(json.dumps({
        "queue": queue_path,
        "content_key": item.get("content_key"),
        "order": item.get("order"),
        "queue_status": item.get("status"),
        "queue_copy_gate": item.get("copy_gate"),
        "queue_planned_for": item.get("planned_for"),
        "request_key": request_key,
        "db": dict(row) if row else None,
    }, ensure_ascii=False))
