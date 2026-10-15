#!/usr/bin/env python3
import json, os, sqlite3
from pathlib import Path
from datetime import datetime, timezone

queue_path=Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json')
db_path=Path('/home/simplifique/apps/daily-dashboard/data/users.db')
request_key='social-l09-c25-202610'
content_key='L09-C25-sua-empresa-está-funcionando-ou-você-está-compen'
asset_dir=Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09/L09-C25-sua-empresa-está-funcionando-ou-você-está-compen')
figma_url='https://www.figma.com/design/aGBW9EAvXjYm9Tz3KkkHcf?node-id=543-230'
now_local='2026-10-14T10:23:32-03:00'
now_utc='2026-10-14T13:23:32Z'

queue=json.loads(queue_path.read_text())
items=queue.get('items') if isinstance(queue,dict) else queue
if not isinstance(items, list):
    raise RuntimeError('Queue items must be a list')
matches=[i for i in items if (i.get('daily_request') or {}).get('request_key')==request_key]
if len(matches)!=1:
    raise RuntimeError(f'Expected one queue match, found {len(matches)}')
item=matches[0]
if item.get('content_key')!=content_key:
    raise RuntimeError('Queue content key mismatch')

con=sqlite3.connect(db_path)
con.row_factory=sqlite3.Row
try:
    con.execute('BEGIN IMMEDIATE')
    row=con.execute('SELECT request_key,topic_key,status,approved_by,approved_at FROM social_content_requests WHERE request_key=?',(request_key,)).fetchone()
    if not row:
        raise RuntimeError('Daily request missing')
    if row['topic_key']!=content_key:
        raise RuntimeError('Daily topic key mismatch')
    if row['status'] not in ('approved_for_production','in_production'):
        raise RuntimeError(f'Unexpected Daily status {row["status"]!r}')
    if not row['approved_by'] or not row['approved_at']:
        raise RuntimeError('Copy approval evidence missing')

    artifacts=[str(asset_dir/name) for name in [
        '01-Estrategia.md','02-Copy-ou-Roteiro.md','03-Direcao-Visual-ou-Audiovisual.md','04-QA.md','05-Curadoria-Imagens.md','manifest.json','citations-ledger.json','figma-comments-readback.json',
        'assets/c25-information-search-pexels-6325909.jpg','source-metadata/c25-information-search-pexels-6325909.json',
        'qa-screenshots/section-initial.png','qa-screenshots/frame-initial.png','qa-screenshots/section-final.png','qa-screenshots/frame-final.png']]
    missing=[p for p in artifacts if not Path(p).is_file()]
    if missing:
        raise RuntimeError(f'Missing artifacts: {missing}')

    item.update({
        'status':'ready','design_authorized':True,'copy_gate':'approved_for_production',
        'checkpoint':'figma_image_led_render_and_post_render_qa_complete',
        'production_started_at':now_local,'updated_at':now_local,'completed_at':now_local,
        'artifact_directory':str(asset_dir),'artifacts':artifacts,
        'publication_status':'unpublished','blocking_issues':[],'qa_decision':'approved','approved_for':'user_review',
        'approved_by':row['approved_by'],'approved_at':row['approved_at'],
        'figma_url':figma_url,'figma_section_id':'543:230','rendered_frames':1,'rendered_dimensions':'1080x1350','rendered_qa':'approved',
        'figma_target':{
            'file_key':'aGBW9EAvXjYm9Tz3KkkHcf','page_node':'182:8','section_id':'543:230','frame_ids':['543:231'],
            'image_node_ids':['543:232'],'overlay_node_ids':['543:233','543:234'],'logo_node_ids':['543:241'],
            'direct_url':figma_url,'rendered':True,'revision_mode':'new_section','duplicate_section_created':False},
        'image_curation':{
            'status':'recommended_downloaded_and_applied','selected_candidate':'C25-INFORMATION-SEARCH-A','source':'Pexels',
            'source_id':6325909,'photographer':'Vanessa Garcia','page_url':'https://www.pexels.com/photo/person-working-typing-sitting-6325909/',
            'score':10,'approval_required':False},
        'non_blocking_notes':[
            'A fotografia Pexels 6325909 foi aplicada com origem, autoria e arquivo local preservados.',
            'A seção e o frame foram inspecionados em resolução nativa; não há clipping, overlap, overflow, fontes ausentes, duplicatas ou comentários Figma vinculados ao ativo.',
            'Artefato editável, não exportado, não agendado e não publicado.'
        ]
    })
    tmp=queue_path.with_suffix(queue_path.suffix+'.tmp')
    with tmp.open('w') as f:
        json.dump(queue,f,ensure_ascii=False,indent=2)
        f.write('\n'); f.flush(); os.fsync(f.fileno())
    os.replace(tmp,queue_path)
    dir_fd=os.open(str(queue_path.parent),os.O_DIRECTORY)
    try: os.fsync(dir_fd)
    finally: os.close(dir_fd)

    con.execute('UPDATE social_content_requests SET status=?, figma_url=?, updated_at=? WHERE request_key=?',('ready',figma_url,now_utc,request_key))
    con.commit()
finally:
    con.close()

queue_rb=json.loads(queue_path.read_text())
rb_items=queue_rb.get('items') if isinstance(queue_rb,dict) else queue_rb
if not isinstance(rb_items, list):
    raise RuntimeError('Queue read-back items must be a list')
qrb=next(i for i in rb_items if (i.get('daily_request') or {}).get('request_key')==request_key)
con=sqlite3.connect(db_path); con.row_factory=sqlite3.Row
drb=dict(con.execute('SELECT request_key,topic_key,status,decision,approved_by,approved_at,figma_url,updated_at FROM social_content_requests WHERE request_key=?',(request_key,)).fetchone()); con.close()
if qrb.get('status')!='ready' or qrb.get('figma_url')!=figma_url:
    raise RuntimeError('Queue read-back failed')
if drb.get('status')!='ready' or drb.get('figma_url')!=figma_url:
    raise RuntimeError('Daily read-back failed')
print(json.dumps({'queue':{'request_key':request_key,'status':qrb['status'],'checkpoint':qrb['checkpoint'],'figma_url':qrb['figma_url'],'artifacts':len(qrb['artifacts'])},'daily':drb},ensure_ascii=False,indent=2))
