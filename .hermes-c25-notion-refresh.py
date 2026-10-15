#!/usr/bin/env python3
import json
import os
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

pages = {
    'marketing': '3927266c1ec6816598c3c7943424fba9',
    'benchmark': '3e67266c1ec68102ba48ebe73b289e73',
    'products': '3e67266c1ec681c2ab32ed45925b0201',
    'formats': '3e67266c1ec68146a6cbe7da6b2d9032',
    'awareness': '3e67266c1ec68180bf63db71fb485c30',
}
token = os.environ.get('NOTION_API_KEY')
if not token:
    raise RuntimeError('NOTION_API_KEY unavailable')
out = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09/L09-C25-sua-empresa-está-funcionando-ou-você-está-compen/sources')
out.mkdir(parents=True, exist_ok=True)
results = {}
for name, page_id in pages.items():
    request = urllib.request.Request(
        f'https://api.notion.com/v1/pages/{page_id}/markdown',
        headers={
            'Authorization': f'Bearer {token}',
            'Notion-Version': '2025-09-03',
            'Accept': 'application/json',
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        body = response.read().decode('utf-8')
        status = response.status
    payload = json.loads(body)
    path = out / f'notion-{name}-refresh-2026-10-14.json'
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
    results[name] = {'status': status, 'path': str(path), 'bytes': len(body)}
print(json.dumps({'fetched_at': datetime.now(timezone.utc).isoformat(), 'results': results}, ensure_ascii=False))
