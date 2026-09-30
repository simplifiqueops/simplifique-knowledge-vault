import json
import os
import urllib.parse
import urllib.request
from pathlib import Path

OUT = Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08/L08-C09-contexto-agente/curation')
OUT.mkdir(parents=True, exist_ok=True)
queries = [
    'business owner reviewing documents laptop office',
    'manager overwhelmed paperwork computer office',
    'team data review laptop documents office',
]
summary = []
pexels_key = os.environ.get('PEXELS_API_KEY')
pixabay_key = os.environ.get('PIXABAY_API_KEY')
if not pexels_key and not pixabay_key:
    raise SystemExit('PEXELS_API_KEY e PIXABAY_API_KEY ausentes')
for idx, query in enumerate(queries, 1):
    if pexels_key:
        try:
            url = 'https://api.pexels.com/v1/search?' + urllib.parse.urlencode({'query': query, 'per_page': 12, 'orientation': 'portrait'})
            req = urllib.request.Request(url, headers={'Authorization': pexels_key, 'User-Agent': 'Simplifique-Curation/1.0'})
            with urllib.request.urlopen(req, timeout=30) as response:
                data = json.loads(response.read().decode('utf-8'))
            path = OUT / f'pexels-{idx}.json'
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            for photo in data.get('photos', [])[:6]:
                summary.append({'source':'Pexels','query':query,'id':photo['id'],'page_url':photo['url'],'photographer':photo['photographer'],'photographer_url':photo['photographer_url'],'width':photo['width'],'height':photo['height'],'preview':photo['src'].get('medium'),'download':photo['src'].get('large2x') or photo['src'].get('original')})
        except Exception as exc:
            (OUT / f'pexels-{idx}-error.txt').write_text(f'{type(exc).__name__}: {exc}\n', encoding='utf-8')
    if pixabay_key:
        params = {'key': pixabay_key, 'q': query, 'image_type':'photo','orientation':'vertical','safesearch':'true','order':'popular','per_page':20}
        url = 'https://pixabay.com/api/?' + urllib.parse.urlencode(params)
        with urllib.request.urlopen(url, timeout=30) as response:
            data = json.loads(response.read().decode('utf-8'))
        path = OUT / f'pixabay-{idx}.json'
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        for photo in data.get('hits', [])[:6]:
            summary.append({'source':'Pixabay','query':query,'id':photo['id'],'page_url':photo['pageURL'],'author':photo['user'],'width':photo['imageWidth'],'height':photo['imageHeight'],'preview':photo.get('webformatURL'),'download':photo.get('largeImageURL')})
(OUT / 'candidates-summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(summary, ensure_ascii=False, indent=2))
