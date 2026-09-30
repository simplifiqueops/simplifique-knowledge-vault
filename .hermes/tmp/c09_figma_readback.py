import json
import os
import urllib.parse
import urllib.request
from pathlib import Path

TOKEN = os.environ.get('FIGMA_ACCESS_TOKEN')
if not TOKEN:
    raise SystemExit('FIGMA_ACCESS_TOKEN ausente')
FILE = 'aGBW9EAvXjYm9Tz3KkkHcf'
FRAMES = ['328:69','328:70','328:71','328:72','328:73','328:74']
OUT = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08/L08-C09-contexto-agente/qa-screenshots')
OUT.mkdir(parents=True, exist_ok=True)
headers = {'X-Figma-Token': TOKEN, 'User-Agent': 'Simplifique-QA/1.0'}

def get_json(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as response:
        return json.loads(response.read().decode('utf-8'))

nodes = get_json(f'https://api.figma.com/v1/files/{FILE}/nodes?' + urllib.parse.urlencode({'ids': ','.join(['328:68', *FRAMES, '337:74', '337:75'])}))
(OUT / 'figma-readback-image-revision.json').write_text(json.dumps(nodes, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
images = get_json(f'https://api.figma.com/v1/images/{FILE}?' + urllib.parse.urlencode({'ids': ','.join(FRAMES), 'format':'png', 'scale':1}))
results = []
for index, frame_id in enumerate(FRAMES, 1):
    url = images.get('images', {}).get(frame_id)
    if not url:
        raise RuntimeError(f'Sem imagem para {frame_id}: {images}')
    req = urllib.request.Request(url, headers={'User-Agent':'Simplifique-QA/1.0'})
    with urllib.request.urlopen(req, timeout=60) as response:
        data = response.read()
    path = OUT / f'frame-{index:02d}-image-revision-current.png'
    path.write_bytes(data)
    if not data.startswith(b'\x89PNG'):
        raise RuntimeError(f'{path} não é PNG')
    results.append({'frame_id': frame_id, 'path': str(path), 'bytes': len(data)})
print(json.dumps(results, ensure_ascii=False, indent=2))
