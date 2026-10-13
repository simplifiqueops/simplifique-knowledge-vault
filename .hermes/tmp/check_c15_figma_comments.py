import json
from pathlib import Path
ids={'519:200','519:201','519:202','519:203','519:204','519:205','519:206'}
data=json.loads(Path('/tmp/figma-comments-c15.json').read_text())
matched=[]
for comment in data.get('comments',[]):
    meta=comment.get('client_meta') or {}
    node=meta.get('node_id')
    stable=set(meta.get('stable_path') or [])
    if node in ids or stable & ids:
        matched.append({k:comment.get(k) for k in ['id','created_at','resolved_at','message']} | {'node_id':node,'stable_path':list(stable)})
print(json.dumps({'total_comments':len(data.get('comments',[])),'matched':matched},ensure_ascii=False))
