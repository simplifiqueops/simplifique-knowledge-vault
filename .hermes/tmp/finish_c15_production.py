import json
import os
import sqlite3
import tempfile
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

REQUEST_KEY = "social-l09-c15-202610"
DB = Path("/home/simplifique/apps/daily-dashboard/data/users.db")
QUEUE = Path("/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json")
ARTIFACT_DIR = Path("/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09/L09-C15-quanto-da-sua-empresa-para-quando-você-não-respo")
FIGMA_URL = "https://www.figma.com/design/aGBW9EAvXjYm9Tz3KkkHcf?node-id=519-200"
NOW = datetime.now(ZoneInfo("America/Sao_Paulo")).isoformat(timespec="seconds")

artifact_names = [
    "01-Estrategia.md",
    "02-Copy-ou-Roteiro.md",
    "03-Direcao-Visual-ou-Audiovisual.md",
    "04-QA.md",
    "05-Curadoria-Imagens.md",
    "manifest.json",
    "assets/c15-waiting-phone-pexels-8682773.jpg",
    "source-metadata/c15-waiting-phone-pexels-8682773.json",
    "qa-screenshots/section-initial.png",
    "qa-screenshots/frame-01-initial.png",
    "qa-screenshots/frame-02-initial.png",
    "qa-screenshots/frame-03-initial.png",
    "qa-screenshots/frame-04-initial.png",
    "qa-screenshots/frame-05-initial.png",
    "qa-screenshots/frame-06-initial.png",
    "qa-screenshots/section-final.png",
    "qa-screenshots/frame-01-final.png",
    "qa-screenshots/frame-02-final.png",
    "qa-screenshots/frame-05-final.png",
]
artifacts = [str(ARTIFACT_DIR / name) for name in artifact_names]
missing = [path for path in artifacts if not Path(path).is_file()]
if missing:
    raise SystemExit("missing artifacts: " + json.dumps(missing, ensure_ascii=False))

with sqlite3.connect(DB) as connection:
    connection.row_factory = sqlite3.Row
    connection.execute("BEGIN IMMEDIATE")
    row = connection.execute(
        "select status, decision, approved_by, approved_at from social_content_requests where request_key=?",
        (REQUEST_KEY,),
    ).fetchone()
    if row is None:
        raise SystemExit("request missing")
    if row["status"] not in {"in_production", "ready"}:
        raise SystemExit(f'incompatible DB state: {row["status"]}')
    connection.execute(
        "update social_content_requests set status='ready', figma_url=?, updated_at=? where request_key=?",
        (FIGMA_URL, NOW, REQUEST_KEY),
    )

queue = json.loads(QUEUE.read_text(encoding="utf-8"))
matched = [item for item in queue["items"] if (item.get("daily_request") or {}).get("request_key") == REQUEST_KEY]
if len(matched) != 1:
    raise SystemExit(f"queue match count {len(matched)}")
item = matched[0]
item.update({
    "status": "ready",
    "copy_gate": "approved_for_production",
    "design_authorized": True,
    "publication_authorized": False,
    "publication_status": "unpublished",
    "checkpoint": "figma_image_led_render_and_post_render_qa_complete",
    "updated_at": NOW,
    "completed_at": NOW,
    "blocking_issues": [],
    "qa_decision": "approved",
    "approved_for": "user_review",
    "artifact_directory": str(ARTIFACT_DIR),
    "artifacts": artifacts,
    "figma_target": {
        "file_key": "aGBW9EAvXjYm9Tz3KkkHcf",
        "page_node": "182:8",
        "section_id": "519:200",
        "frame_ids": ["519:201", "519:202", "519:203", "519:204", "519:205", "519:206"],
        "image_node_ids": ["519:207"],
        "logo_node_ids": ["519:212", "519:266"],
        "direct_url": FIGMA_URL,
        "rendered": True,
        "revision_mode": "new_section",
        "duplicate_section_created": False,
    },
    "image_curation": {
        "status": "recommended_downloaded_and_applied",
        "selected_candidate": "C15-WAIT-A",
        "source": "Pexels",
        "source_id": 8682773,
        "photographer": "Ron Lach",
        "page_url": "https://www.pexels.com/photo/woman-talking-on-the-telephone-8682773/",
        "score": 9,
        "approval_required": False,
    },
    "non_blocking_notes": [
        "A fotografia Pexels 8682773 foi aplicada com origem, autoria e arquivo local preservados.",
        "A seção completa e os seis frames foram inspecionados em 1080×1350; nenhum clipping, overlap ou fonte ausente foi detectado.",
        "Artefato editável, não exportado, não agendado e não publicado.",
    ],
})

fd, temporary = tempfile.mkstemp(prefix=".Lote-09-Fila.", suffix=".tmp", dir=str(QUEUE.parent))
try:
    with os.fdopen(fd, "w", encoding="utf-8") as handle:
        json.dump(queue, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, QUEUE)
finally:
    if os.path.exists(temporary):
        os.unlink(temporary)

print(json.dumps({"request_key": REQUEST_KEY, "db_status": "ready", "queue_status": item["status"], "figma_url": FIGMA_URL, "updated_at": NOW}, ensure_ascii=False))
