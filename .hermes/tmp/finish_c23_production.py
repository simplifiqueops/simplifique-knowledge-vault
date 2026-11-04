import json
import os
import sqlite3
from pathlib import Path

REQUEST_KEY = 'social-l09-c23-202610'
CONTENT_KEY = 'L09-C23-automação-sem-trilha-de-decisão-só-deixa-o-erro-'
COMPLETED_AT = '2026-11-03T15:01:03-03:00'
FIGMA_URL = 'https://www.figma.com/design/aGBW9EAvXjYm9Tz3KkkHcf?node-id=694-254'
BASE = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09/L09-C23-automação-sem-trilha-de-decisão-só-deixa-o-erro-')
QUEUE = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json')
DB = Path('/home/simplifique/apps/daily-dashboard/data/users.db')

note = ('Produção visual image-led concluída e QA aprovada em 2026-11-03T15:01:03-03:00. '
        'Seção 694:254 com 1 frame editável em 1080x1350; imagem Pexels 8296972 aplicada com rastreabilidade; '
        'sem clipping, overlap, overflow, duplicata ou comentários Figma vinculados. Não exportado, não agendado e não publicado.')
con = sqlite3.connect(DB)
try:
    con.execute('BEGIN IMMEDIATE')
    row = con.execute('SELECT status FROM social_content_requests WHERE request_key=?', (REQUEST_KEY,)).fetchone()
    if not row or row[0] not in ('in_production', 'ready'):
        raise RuntimeError(f'estado Daily inesperado: {row[0] if row else None}')
    con.execute("""
        UPDATE social_content_requests
        SET status='ready', figma_url=?, decision='approved_for_production', decision_note=?, updated_at=?
        WHERE request_key=?
    """, (FIGMA_URL, note, COMPLETED_AT, REQUEST_KEY))
    con.commit()
finally:
    con.close()

data = json.loads(QUEUE.read_text(encoding='utf-8'))
item = next((x for x in data['items'] if x.get('content_key') == CONTENT_KEY), None)
if not item:
    raise RuntimeError('item não encontrado na fila')
artifacts = [
    str(BASE / '01-Estrategia.md'), str(BASE / '02-Copy-ou-Roteiro.md'),
    str(BASE / '03-Direcao-Visual-ou-Audiovisual.md'), str(BASE / '04-QA.md'),
    str(BASE / '05-Curadoria-Imagens.md'), str(BASE / 'manifest.json'),
    str(BASE / 'assets/c23-investigation-pexels-8296972.jpg'),
    str(BASE / 'source-metadata/c23-investigation-pexels-8296972.json'),
    str(BASE / 'figma-comments-readback.json'),
    str(BASE / 'qa-screenshots/section-initial.png'),
    str(BASE / 'qa-screenshots/frame-initial.png')
]
item.update({
    'status': 'ready', 'copy_gate': 'approved_for_production', 'design_authorized': True,
    'checkpoint': 'figma_image_led_render_and_post_render_qa_complete',
    'updated_at': COMPLETED_AT, 'completed_at': COMPLETED_AT,
    'publication_status': 'unpublished', 'blocking_issues': [],
    'qa_decision': 'approved', 'approved_for': 'human_visual_review',
    'artifact_directory': str(BASE), 'artifacts': artifacts,
    'figma_url': FIGMA_URL, 'figma_section_id': '694:254',
    'rendered_frames': 1, 'rendered_dimensions': '1080x1350', 'rendered_qa': 'approved',
    'figma_target': {
        'file_key': 'aGBW9EAvXjYm9Tz3KkkHcf', 'page_node': '182:8',
        'section_id': '694:254', 'frame_ids': ['694:255'],
        'image_node_ids': ['694:256'], 'overlay_node_ids': ['694:257', '694:258'],
        'text_node_ids': ['694:260', '694:262', '694:263'], 'logo_node_ids': ['694:264'],
        'direct_url': FIGMA_URL, 'rendered': True,
        'revision_mode': 'new_section', 'duplicate_section_created': False
    },
    'image_curation': {
        'status': 'recommended_downloaded_and_applied', 'selected_candidate': 'C23-INVESTIGATION-A',
        'source': 'Pexels', 'source_id': 8296972, 'photographer': 'Mikhail Nilov',
        'page_url': 'https://www.pexels.com/photo/woman-fixing-a-binder-of-documents-8296972/',
        'score': 10, 'approval_required': False
    },
    'non_blocking_notes': [
        'A fotografia Pexels 8296972 foi aplicada com origem, autoria e arquivo local preservados.',
        'A seção e o frame foram inspecionados em 1080×1350; não há clipping, overlap, overflow, fontes ausentes ou comentários Figma vinculados.',
        'Artefato editável, não exportado, não agendado e não publicado.'
    ]
})
tmp = QUEUE.with_suffix('.json.tmp')
tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
os.replace(tmp, QUEUE)
print(json.dumps({'request_key': REQUEST_KEY, 'daily_status': 'ready', 'queue_status': item['status'], 'figma_url': FIGMA_URL}, ensure_ascii=False))
