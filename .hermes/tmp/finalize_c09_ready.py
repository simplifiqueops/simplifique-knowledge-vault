import datetime as dt
import json
import os
import sqlite3
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08/L08-C09-contexto-agente')
QUEUE = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json')
MANIFEST = ROOT / 'manifest.json'
DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')
REQUEST_KEY = 'social-5fe7013793da6204b625f7a5'
FIGMA_URL = 'https://www.figma.com/design/aGBW9EAvXjYm9Tz3KkkHcf?node-id=328-68'
PROCESSED = Path('/home/simplifique/.hermes/state/simplifique-social-requests/processed') / f'{REQUEST_KEY}.json'
if not PROCESSED.exists():
    raise RuntimeError(f'Outbox processado ausente: {PROCESSED}')
request = json.loads(PROCESSED.read_text(encoding='utf-8'))
if request.get('request_key') != REQUEST_KEY:
    raise RuntimeError('Read-back do outbox não corresponde ao request')
now = dt.datetime.now(ZoneInfo('America/Sao_Paulo')).isoformat()
queue = json.loads(QUEUE.read_text(encoding='utf-8'))
manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
item = next((value for value in queue['items'] if value.get('daily_request', {}).get('request_key') == REQUEST_KEY), None)
if not item:
    raise RuntimeError('C09 não encontrado na fila')
if item.get('status') != 'in_production':
    raise RuntimeError(f'Estado inesperado na fila: {item.get("status")}')

new_artifacts = [
    str(ROOT / '06-Curadoria-Imagens.md'),
    str(ROOT / 'assets/c09-context-pexels-6694547.jpg'),
    str(ROOT / 'source-metadata/c09-context-pexels-6694547.json'),
    str(ROOT / 'audit/pre-image-revision-2026-09-29/section-328-68.png'),
    str(ROOT / 'qa-screenshots/section-image-revision-final.png'),
    str(ROOT / 'qa-screenshots/frame-02-image-revision-final.png'),
    str(ROOT / 'qa-screenshots/figma-readback-image-revision.json'),
]
new_artifacts.extend(str(ROOT / f'qa-screenshots/frame-{i:02d}-image-revision-current.png') for i in range(1, 7))
artifacts = list(item.get('artifacts', []))
for path in new_artifacts:
    if path not in artifacts:
        artifacts.append(path)
item.update({
    'status': 'ready',
    'request_status': 'ready',
    'checkpoint': 'figma_image_revision_in_place_and_post_render_qa_complete',
    'updated_at': now,
    'completed_at': now,
    'qa_decision': 'approved',
    'approved_for': 'user_review',
    'publication_status': 'unpublished',
    'blocking_issues': [],
    'artifacts': artifacts,
    'image_curation': {
        'status': 'recommended_downloaded_and_applied',
        'selected_candidate': 'C09-CONTEXT-A',
        'source': 'Pexels',
        'pexels_id': 6694547,
        'photographer': 'Tima Miroshnichenko',
        'page_url': 'https://www.pexels.com/photo/a-businesswoman-working-with-papers-in-the-office-6694547/',
        'score': 10,
        'approval_required': False,
        'downloaded': True,
    },
    'non_blocking_notes': [
        'A seção existente 328:68 foi revisada no lugar; nenhuma seção paralela foi criada.',
        'A fotografia Pexels 6694547 foi aplicada na tela 02 com origem, autoria e arquivo local preservados.',
        'A seção completa e os seis frames foram reinspecionados após a revisão image-led.',
        'Artefato editável, não exportado, não agendado e não publicado.',
    ],
})
figma = item.setdefault('figma_target', {})
figma.update({
    'file_key': 'aGBW9EAvXjYm9Tz3KkkHcf',
    'page_node': '182:8',
    'section_id': '328:68',
    'frame_ids': ['328:69','328:70','328:71','328:72','328:73','328:74'],
    'image_node_ids': ['337:74'],
    'overlay_node_ids': ['337:75'],
    'mutated_node_ids': sorted(set(figma.get('mutated_node_ids', []) + ['328:80','328:81','328:83','328:85','328:87','328:88','328:89'])),
    'direct_url': FIGMA_URL,
    'revision_mode': 'in_place',
    'duplicate_section_created': False,
})

manifest_artifacts = list(manifest.get('artifacts', []))
for path in [
    '06-Curadoria-Imagens.md', 'assets/c09-context-pexels-6694547.jpg',
    'source-metadata/c09-context-pexels-6694547.json',
    'audit/pre-image-revision-2026-09-29/section-328-68.png',
    'qa-screenshots/section-image-revision-final.png',
    'qa-screenshots/frame-02-image-revision-final.png',
    'qa-screenshots/figma-readback-image-revision.json',
    *[f'qa-screenshots/frame-{i:02d}-image-revision-current.png' for i in range(1,7)],
]:
    if path not in manifest_artifacts:
        manifest_artifacts.append(path)
manifest.update({
    'status': 'ready', 'checkpoint': 'figma_image_revision_in_place_and_post_render_qa_complete',
    'qa_decision': 'approved', 'publication_status': 'unpublished', 'approved_for': 'user_review',
    'blocking_issues': [], 'image_direction': 'image_applied', 'artifacts': manifest_artifacts,
    'updated_at': now,
    'non_blocking_notes': item['non_blocking_notes'],
    'image_curation': item['image_curation'],
})
manifest['daily_request']['status'] = 'ready'
manifest['daily_request']['snapshot'] = str(PROCESSED)
manifest['figma']['image_node_ids'] = ['337:74']
manifest['figma']['overlay_node_ids'] = ['337:75']
manifest['figma']['revision_mode'] = 'in_place'
manifest['figma']['duplicate_section_created'] = False
manifest['figma']['direct_url'] = FIGMA_URL
manifest['figma']['mutated_node_ids'] = sorted(set(manifest['figma'].get('mutated_node_ids', []) + ['328:80','328:81','328:83','328:85','328:87','328:88','328:89']))
for source in [
    'sources/notion-marketing-refresh-2026-09-29.json',
    'sources/notion-benchmark-refresh-2026-09-29.json',
    'sources/notion-products-refresh-2026-09-29.json',
    'sources/notion-formats-refresh-2026-09-29.json',
    'sources/notion-awareness-refresh-2026-09-29.json',
    str(PROCESSED),
]:
    if source not in manifest['sources']:
        manifest['sources'].append(source)
manifest['sources'] = [source for source in manifest['sources'] if '/pending/' not in source]

con = sqlite3.connect(DB)
try:
    con.execute('BEGIN IMMEDIATE')
    current = con.execute('SELECT status FROM social_content_requests WHERE request_key=?', (REQUEST_KEY,)).fetchone()
    if not current or current[0] != 'in_production':
        raise RuntimeError(f'Estado DB inesperado: {current}')
    changed = con.execute("UPDATE social_content_requests SET status='ready', figma_url=?, updated_at=? WHERE request_key=? AND status='in_production'", (FIGMA_URL, now, REQUEST_KEY)).rowcount
    if changed != 1:
        raise RuntimeError('Falha ao avançar DB para ready')
    qtmp = QUEUE.with_suffix('.json.tmp')
    mtmp = MANIFEST.with_suffix('.json.tmp')
    qtmp.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    mtmp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.replace(qtmp, QUEUE)
    os.replace(mtmp, MANIFEST)
    con.commit()

    db_row = con.execute('SELECT status,figma_url FROM social_content_requests WHERE request_key=?', (REQUEST_KEY,)).fetchone()
    queue_check = next(value for value in json.loads(QUEUE.read_text(encoding='utf-8'))['items'] if value.get('daily_request', {}).get('request_key') == REQUEST_KEY)
    manifest_check = json.loads(MANIFEST.read_text(encoding='utf-8'))
    if db_row != ('ready', FIGMA_URL) or queue_check.get('status') != 'ready' or manifest_check.get('status') != 'ready':
        raise RuntimeError(f'Read-back divergente: db={db_row}, queue={queue_check.get("status")}, manifest={manifest_check.get("status")}')
    print(json.dumps({'request_key': REQUEST_KEY, 'db_status': db_row[0], 'queue_status': queue_check['status'], 'manifest_status': manifest_check['status'], 'figma_url': db_row[1], 'processed_outbox': str(PROCESSED)}, ensure_ascii=False, indent=2))
except Exception:
    con.rollback()
    raise
finally:
    con.close()
