import json, os, sqlite3
from pathlib import Path
pending=Path('/home/simplifique/.hermes/state/simplifique-social-requests/pending/social-36af0dc2e866f470bf886e0b.json')
archive=Path('/home/simplifique/.hermes/state/simplifique-social-requests/reconciled/duplicates/social-36af0dc2e866f470bf886e0b.json')
canonical='social-d5384a9b07966269b967802a'
now='2026-10-20T11:38:09.569301Z'
payload=json.loads(pending.read_text())
topic=payload['topic_snapshot']
request_key=payload['request_key']
archive.parent.mkdir(parents=True,exist_ok=True,mode=0o700)
archive_payload={**payload,'reconciliation':{'status':'duplicate_archived','duplicate_of':canonical,'topic_key':payload['topic_key'],'reconciled_at':now,'database_readback':'discarded'}}
tmp=archive.with_name('.'+archive.name+'.tmp')
tmp.write_text(json.dumps(archive_payload,ensure_ascii=False,indent=2)+'\n')
os.chmod(tmp,0o600)
db=sqlite3.connect('/home/simplifique/apps/daily-dashboard/data/users.db')
try:
    db.execute('BEGIN IMMEDIATE')
    row=db.execute('select user_id from social_content_requests where request_key=?',(canonical,)).fetchone()
    if row is None: raise RuntimeError('canonical request missing')
    existing=db.execute('select status from social_content_requests where request_key=?',(request_key,)).fetchone()
    if existing is None:
        db.execute('''insert into social_content_requests
        (request_key,user_id,topic_key,topic_title,sources_json,facts_json,risks_json,desired_format,copy_text,planned_for,decision,decision_note,approved_by,approved_at,figma_url,status,requester,requested_at,updated_at)
        values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(
            request_key,row[0],payload['topic_key'],topic['title'],json.dumps(topic.get('sources',[]),ensure_ascii=False),
            json.dumps(topic.get('facts',[]),ensure_ascii=False),json.dumps(topic.get('risks',[]),ensure_ascii=False),
            payload.get('format'),None,payload.get('planned_for'),'discarded',f'Duplicado de {canonical}; mesmo topic_key {payload["topic_key"]}.',
            None,None,None,'discarded',payload.get('requester','reconciliation'),payload['requested_at'],now))
    elif existing[0] != 'discarded': raise RuntimeError('existing row has non-discarded status')
    db.commit()
finally:
    db.close()
os.replace(tmp,archive)
pending.unlink(missing_ok=True)
print(request_key,'discarded',archive)
