import datetime as dt
import hashlib
import json
import urllib.request
from pathlib import Path

ROOT = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08/L08-C09-contexto-agente')
ASSET = ROOT / 'assets/c09-context-pexels-6694547.jpg'
META = ROOT / 'source-metadata/c09-context-pexels-6694547.json'
ASSET.parent.mkdir(parents=True, exist_ok=True)
META.parent.mkdir(parents=True, exist_ok=True)
url = 'https://images.pexels.com/photos/6694547/pexels-photo-6694547.jpeg?cs=srgb&dl=pexels-tima-miroshnichenko-6694547.jpg&fm=jpg'
req = urllib.request.Request(url, headers={'User-Agent': 'Simplifique-Curation/1.0'})
with urllib.request.urlopen(req, timeout=60) as response:
    data = response.read()
if not data.startswith(b'\xff\xd8'):
    raise RuntimeError('Download não é JPEG válido')
ASSET.write_bytes(data)
metadata = {
    'candidate_id': 'C09-CONTEXT-A',
    'source': 'Pexels',
    'pexels_id': 6694547,
    'page_url': 'https://www.pexels.com/photo/a-businesswoman-working-with-papers-in-the-office-6694547/',
    'download_url': url,
    'photographer': 'Tima Miroshnichenko',
    'photographer_url': 'https://www.pexels.com/@tima-miroshnichenko/',
    'dimensions': {'width': 5989, 'height': 3993},
    'accessed_at': dt.datetime.now(dt.timezone.utc).isoformat().replace('+00:00','Z'),
    'planned_use': 'Tela 02 como fotografia full-bleed com overlay escuro; materializa documentos dispersos e interpretação ainda humana.',
    'score': {'function': 2, 'brand_fit': 2, 'naturalness': 2, 'technical': 2, 'traceability': 2, 'total': 10},
    'risks': ['Cena genérica de banco de imagem; não apresentar como cliente ou situação real.', 'Evitar crop que elimine simultaneamente documentos e laptop.'],
    'sha256': hashlib.sha256(data).hexdigest(),
    'bytes': len(data),
}
META.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'asset': str(ASSET), 'metadata': str(META), 'bytes': len(data), 'sha256': metadata['sha256']}, ensure_ascii=False, indent=2))
