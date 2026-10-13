#!/usr/bin/env python3
import json
import os
import sqlite3
from pathlib import Path

NOW='2026-10-12T19:14:48-03:00'
REQUEST='social-d5d16909b0f33f9a0bc007d9'
QUEUE=Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json')
DB=Path('/home/simplifique/apps/daily-dashboard/data/users.db')
ART=Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08/L08-RQ-d5d16909')
URL='https://www.figma.com/design/aGBW9EAvXjYm9Tz3KkkHcf?node-id=524-212'

data=json.loads(QUEUE.read_text())
item=next(i for i in data['items'] if (i.get('daily_request') or {}).get('request_key')==REQUEST)
if item.get('status')!='approved_for_production':
    raise RuntimeError(f'Unexpected queue state: {item.get("status")}')
item.update({
    'status':'ready',
    'request_status':'ready',
    'copy_gate':'approved_for_production',
    'design_authorized':True,
    'checkpoint':'figma_image_led_render_and_post_render_qa_complete',
    'production_started_at':'2026-10-12T19:09:09-03:00',
    'completed_at':NOW,
    'updated_at':NOW,
    'publication_status':'unpublished',
    'blocking_issues':[],
    'qa_decision':'approved',
    'approved_for':'human_figma_review',
    'export_status':'not_exported',
    'artifact_directory':str(ART),
    'artifacts':[
        str(ART/'01-Estrategia.md'),
        str(ART/'02-Copy-ou-Roteiro.md'),
        str(ART/'03-Direcao-Visual-ou-Audiovisual.md'),
        str(ART/'04-QA.md'),
        str(ART/'05-Curadoria-Imagens.md'),
        str(ART/'citations-ledger.json'),
        str(ART/'manifest.json'),
        str(ART/'assets/d5d-handoff-pexels-8867415.jpg'),
        str(ART/'source-metadata/pexels-8867415.json'),
        str(ART/'qa-screenshots/frame-initial.png'),
        str(ART/'qa-screenshots/frame-final.png'),
        str(ART/'qa-screenshots/section-initial.png'),
        str(ART/'figma-comments-readback.json')
    ],
    'figma_target':{
        'file_key':'aGBW9EAvXjYm9Tz3KkkHcf','page_node':'182:8','section_id':'524:212',
        'frame_ids':['524:213'],'image_node_ids':['524:214'],'overlay_node_ids':['524:215'],
        'logo_node_ids':['524:222'],'direct_url':URL,'rendered':True,'editable':True,
        'revision_mode':'new_section','duplicate_section_created':False
    },
    'image_curation':{
        'status':'recommended_downloaded_and_applied','selected_candidate':'PEXELS-8867415',
        'source':'Pexels','source_id':8867415,'photographer':'Yan Krukau',
        'page_url':'https://www.pexels.com/photo/two-women-working-in-the-office-8867415/',
        'score':9,'approval_required':False
    },
    'non_blocking_notes':[
        'A fotografia Pexels 8867415 foi aplicada com origem, autoria e arquivo local preservados.',
        'O primeiro render apresentou sobreposição por colapso de altura no Auto Layout; o reflow foi corrigido e o frame foi reinspecionado em 1080×1350.',
        'Comentários Figma atualizados após o QA; nenhum comentário vinculado à nova seção.',
        'Artefato editável, não exportado, não agendado e não publicado.'
    ]
})
tmp=QUEUE.with_suffix('.json.tmp')
tmp.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
os.replace(tmp,QUEUE)

note='Produção visual image-led concluída e QA aprovada em 2026-10-12T19:14:48-03:00. Seção 524:212 com 1 frame editável em 1080x1350; imagem Pexels 8867415 aplicada com rastreabilidade; sem clipping, overlap, overflow ou comentários novos vinculados. Não exportado, não agendado e não publicado.'
with sqlite3.connect(DB) as db:
    cur=db.execute("UPDATE social_content_requests SET status='ready', figma_url=?, decision_note=?, updated_at=? WHERE request_key=? AND status='approved_for_production'",(URL,note,NOW,REQUEST))
    if cur.rowcount!=1:
        raise RuntimeError(f'DB update affected {cur.rowcount} rows')
    db.commit()
print(json.dumps({'request_key':REQUEST,'status':'ready','figma_url':URL,'queue':QUEUE.name},ensure_ascii=False))
