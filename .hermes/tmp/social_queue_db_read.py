import json
import os
import sqlite3

DB = "/home/simplifique/apps/daily-dashboard/data/users.db"
con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
print("TABLES")
print("\n".join(row[0] for row in con.execute("select name from sqlite_master where type='table' order by name")))
print("COLUMNS")
print("\t".join(row[1] for row in con.execute("pragma table_info(social_content_requests)")))
keys = [
    "social-d5d16909b0f33f9a0bc007d9",
    "social-l09-c23-202610",
]
for key in keys:
    row = con.execute("select * from social_content_requests where request_key=?", (key,)).fetchone()
    print("ROW", key)
    print(json.dumps(dict(row) if row else None, ensure_ascii=False, indent=2))
print("ACTIVE")
for row in con.execute("select request_key,topic_key,topic_title,status,requested_at,planned_for,updated_at,decision_note from social_content_requests where status in ('queued','copy_in_production','copy_review','changes_requested','approved_for_production','in_production') order by requested_at,coalesce(planned_for,''),request_key"):
    print(json.dumps(dict(row), ensure_ascii=False))

for base in [
    "/home/simplifique/.hermes/state/simplifique-social-requests/pending",
    "/home/simplifique/.hermes/state/simplifique-social-requests/processed",
    "/home/simplifique/.hermes/state/simplifique-social-requests/results",
]:
    print("DIR", base)
    if os.path.isdir(base):
        for name in sorted(os.listdir(base)):
            if name.endswith('.json'):
                print(name)
    else:
        print("MISSING")
