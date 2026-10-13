#!/usr/bin/env python3
import json
import sqlite3
from pathlib import Path

request_key = 'social-l09-c19-202610'
completed_at = '2026-10-12T21:25:49-03:00'
queue_path = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json')
artifact_dir = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09/L09-C19-responder-rápido-não-é-o-mesmo-que-concluir-o-at')
section_url = 'https://www.figma.com/design/aGBW9EAvXjYm9Tz3KkkHcf?node-id=531-218'

artifacts = [
    artifact_dir / '01-Estrategia.md',
    artifact_dir / '02-Copy-ou-Roteiro.md',
    artifact_dir / '03-Direcao-Visual-ou-Audiovisual.md',
    artifact_dir / '04-QA.md',
    artifact_dir / '05-Curadoria-Imagens.md',
    artifact_dir / 'manifest.json',
    artifact_dir / 'citations-ledger.json',
    artifact_dir / 'assets/c19-customer-waiting-pexels-7339179.jpg',
    artifact_dir / 'source-metadata/c19-customer-waiting-pexels-7339179.json',
    artifact_dir / 'figma-comments-readback.json',
    artifact_dir / 'qa-screenshots/section-initial.png',
    artifact_dir / 'qa-screenshots/frame-initial.png',
    artifact_dir / 'qa-screenshots/section-final.png',
    artifact_dir / 'qa-screenshots/frame-final.png',
]
missing = [str(path) for path in artifacts if not path.exists()]
if missing:
    raise SystemExit(f'missing artifacts: {missing}')

queue = json.loads(queue_path.read_text())
item = next(x for x in queue['items'] if (x.get('daily_request') or {}).get('request_key') == request_key)
if item.get('status') != 'in_production':
    raise SystemExit(f"unexpected queue status: {item.get('status')}")
item.update({
    'status': 'ready',
    'copy_gate': 'approved_for_production',
    'design_authorized': True,
    'checkpoint': 'figma_image_led_render_and_post_render_qa_complete',
    'updated_at': completed_at,
    'completed_at': completed_at,
    'publication_status': 'unpublished',
    'blocking_issues': [],
    'qa_decision': 'approved',
    'approved_for': 'user_review',
    'artifact_directory': str(artifact_dir),
    'artifacts': [str(path) for path in artifacts],
    'figma_target': {
        'file_key': 'aGBW9EAvXjYm9Tz3KkkHcf',
        'page_node': '182:8',
        'section_id': '531:218',
        'frame_ids': ['531:219'],
        'image_node_ids': ['531:220'],
        'overlay_node_ids': ['531:221', '531:222'],
        'logo_node_ids': ['531:228'],
        'direct_url': section_url,
        'rendered': True,
        'revision_mode': 'new_section',
        'duplicate_section_created': False,
    },
    'image_curation': {
        'status': 'recommended_downloaded_and_applied',
        'selected_candidate': 'C19-WAIT-A',
        'source': 'Pexels',
        'source_id': 7339179,
        'photographer': 'cottonbro studio',
        'page_url': 'https://www.pexels.com/photo/man-in-yellow-sweater-holding-a-phone-on-a-cafe-7339179/',
        'score': 9,
        'approval_required': False,
    },
    'non_blocking_notes': [
        'A fotografia Pexels 7339179 foi aplicada com origem, autoria e arquivo local preservados.',
        'O primeiro render ocultava a fotografia; o wash foi removido, o gradiente suavizado e o logo reposicionado antes da reinspeção.',
        'A seção e o frame foram inspecionados em 1080×1350; não há clipping, overlap, overflow ou fontes ausentes.',
        'Artefato editável, não exportado, não agendado e não publicado.',
    ],
})
queue_path.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + '\n')

with sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db') as db:
    db.row_factory = sqlite3.Row
    row = db.execute('SELECT request_key,status,decision,approved_by,approved_at FROM social_content_requests WHERE request_key=?', (request_key,)).fetchone()
    if not row or row['status'] != 'in_production' or row['decision'] != 'approved_for_production':
        raise SystemExit(f'unexpected DB row: {dict(row) if row else None}')
    db.execute('UPDATE social_content_requests SET status=?,figma_url=?,updated_at=? WHERE request_key=?', ('ready', section_url, completed_at, request_key))
    db_readback = dict(db.execute('SELECT request_key,status,decision,approved_by,approved_at,figma_url,updated_at FROM social_content_requests WHERE request_key=?', (request_key,)).fetchone())

queue_readback = json.loads(queue_path.read_text())
item_readback = next(x for x in queue_readback['items'] if (x.get('daily_request') or {}).get('request_key') == request_key)
print(json.dumps({
    'queue': {
        'status': item_readback['status'],
        'copy_gate': item_readback['copy_gate'],
        'checkpoint': item_readback['checkpoint'],
        'figma_url': item_readback['figma_target']['direct_url'],
        'artifact_count': len(item_readback['artifacts']),
        'publication_status': item_readback['publication_status'],
    },
    'db': db_readback,
}, ensure_ascii=False))
