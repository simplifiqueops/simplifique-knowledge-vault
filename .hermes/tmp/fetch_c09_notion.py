import json
import os
import urllib.request
from pathlib import Path

TOKEN = os.environ.get('NOTION_API_KEY')
if not TOKEN:
    raise SystemExit('NOTION_API_KEY ausente')
OUT = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08/L08-C09-contexto-agente/sources')
OUT.mkdir(parents=True, exist_ok=True)
pages = {
    'notion-marketing-refresh-2026-09-29.json': '3927266c1ec6816598c3c7943424fba9',
    'notion-benchmark-refresh-2026-09-29.json': '3e67266c1ec68102ba48ebe73b289e73',
    'notion-products-refresh-2026-09-29.json': '3e67266c1ec681c2ab32ed45925b0201',
    'notion-formats-refresh-2026-09-29.json': '3e67266c1ec68146a6cbe7da6b2d9032',
    'notion-awareness-refresh-2026-09-29.json': '3e67266c1ec68180bf63db71fb485c30',
}
results = {}
for filename, page_id in pages.items():
    url = f'https://api.notion.com/v1/pages/{page_id}/markdown'
    req = urllib.request.Request(url, headers={
        'Authorization': f'Bearer {TOKEN}',
        'Notion-Version': '2025-09-03',
        'Accept': 'application/json',
    })
    with urllib.request.urlopen(req, timeout=30) as response:
        body = response.read().decode('utf-8')
        data = json.loads(body)
        if response.status != 200:
            raise RuntimeError(f'{page_id}: HTTP {response.status}')
    (OUT / filename).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    text = data.get('markdown') or data.get('content') or ''
    results[filename] = {'status': response.status, 'chars': len(text), 'keys': sorted(data.keys())}
print(json.dumps(results, ensure_ascii=False, indent=2))
