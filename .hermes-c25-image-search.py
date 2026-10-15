#!/usr/bin/env python3
import json
import os
import urllib.parse
import urllib.request
from pathlib import Path

out = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09/L09-C25-sua-empresa-está-funcionando-ou-você-está-compen/curation')
out.mkdir(parents=True, exist_ok=True)
results = {}
pexels = os.environ.get('PEXELS_API_KEY')
if pexels:
    try:
        query = 'person working with phone laptop notes office'
        url = 'https://api.pexels.com/v1/search?' + urllib.parse.urlencode({'query': query, 'per_page': 15, 'orientation': 'portrait'})
        req = urllib.request.Request(url, headers={'Authorization': pexels, 'User-Agent': 'SimplifiqueImageCuration/1.0'})
        with urllib.request.urlopen(req, timeout=30) as response:
            payload = json.loads(response.read().decode('utf-8'))
        (out / 'pexels-search.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
        results['pexels'] = {'query': query, 'count': len(payload.get('photos', [])), 'path': str(out / 'pexels-search.json')}
    except Exception as exc:
        results['pexels_error'] = f'{type(exc).__name__}: {exc}'
pixabay = os.environ.get('PIXABAY_API_KEY')
if pixabay:
    query = 'person laptop phone paperwork office'
    url = 'https://pixabay.com/api/?' + urllib.parse.urlencode({'key': pixabay, 'q': query, 'safesearch': 'true', 'order': 'popular', 'per_page': 20, 'orientation': 'vertical', 'image_type': 'photo'})
    with urllib.request.urlopen(url, timeout=30) as response:
        payload = json.loads(response.read().decode('utf-8'))
    (out / 'pixabay-search.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
    results['pixabay'] = {'query': query, 'count': len(payload.get('hits', [])), 'path': str(out / 'pixabay-search.json')}
if not any(name in results for name in ('pexels', 'pixabay')):
    raise RuntimeError('No Pexels or Pixabay API key available')
print(json.dumps(results, ensure_ascii=False))
