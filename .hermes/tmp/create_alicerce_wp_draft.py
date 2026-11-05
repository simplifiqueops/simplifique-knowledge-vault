#!/usr/bin/env python3
import hashlib
import json
import os
from pathlib import Path

import requests

BASE = os.environ['WORDPRESS_URL'].rstrip('/')
AUTH = (os.environ['WORDPRESS_USERNAME'], os.environ['WORDPRESS_APP_PASSWORD'])
HTML_PATH = Path('/home/simplifique/vault/01-Clientes/Realizando-Potenciais/Alicerce-do-Extraordinario/Pagina-de-Vendas/wordpress/alicerce-page.html')
OUT_PATH = Path('/home/simplifique/vault/.hermes/tmp/alicerce-wp-page-result.json')
TITLE = 'Alicerce do Extraordinário — Evento'
SLUG = 'alicerce-do-extraordinario-evento'

session = requests.Session()
session.auth = AUTH

# Hard guard: this task may create exactly one new page and must never overwrite an existing page.
r = session.get(f'{BASE}/wp-json/wp/v2/pages', params={'search': TITLE, 'context': 'edit', 'per_page': 100}, timeout=30)
r.raise_for_status()
existing = [p for p in r.json() if p.get('title', {}).get('raw') == TITLE or p.get('slug') == SLUG]
if existing:
    raise SystemExit(json.dumps({'error': 'matching_page_already_exists', 'ids': [p['id'] for p in existing]}))

html = HTML_PATH.read_text(encoding='utf-8')
elementor_data = [{
    'id': 'alicerce-root',
    'elType': 'container',
    'isInner': False,
    'settings': {
        'content_width': 'full',
        'width': {'unit': '%', 'size': 100, 'sizes': []},
        'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0', 'isLinked': True},
        'margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0', 'isLinked': True},
    },
    'elements': [{
        'id': 'alicerce-html',
        'elType': 'widget',
        'widgetType': 'html',
        'isInner': False,
        'settings': {'html': html},
        'elements': [],
    }],
}]

payload = {
    'title': TITLE,
    'slug': SLUG,
    'status': 'draft',
    'template': 'elementor_canvas',
    'comment_status': 'closed',
    'ping_status': 'closed',
    'content': html,
    'meta': {
        '_elementor_edit_mode': 'builder',
        '_elementor_template_type': 'wp-page',
        '_elementor_data': json.dumps(elementor_data, ensure_ascii=False, separators=(',', ':')),
        '_elementor_page_settings': {'hide_title': 'yes'},
    },
}

create = session.post(f'{BASE}/wp-json/wp/v2/pages', json=payload, timeout=180)
if create.status_code not in (200, 201):
    raise SystemExit(json.dumps({'error': 'create_failed', 'http': create.status_code, 'body': create.text[:1000]}))
page = create.json()
page_id = page['id']

# Exact read-back verification of the new target.
read = session.get(f'{BASE}/wp-json/wp/v2/pages/{page_id}', params={'context': 'edit'}, timeout=60)
read.raise_for_status()
check = read.json()
raw_content = check.get('content', {}).get('raw', '')
meta = check.get('meta', {})
result = {
    'id': page_id,
    'title': check.get('title', {}).get('raw'),
    'slug': check.get('slug'),
    'status': check.get('status'),
    'template': check.get('template'),
    'link': check.get('link'),
    'preview_url': f'{BASE}/?page_id={page_id}&preview=true',
    'elementor_edit_mode': meta.get('_elementor_edit_mode'),
    'elementor_template_type': meta.get('_elementor_template_type'),
    'elementor_data_chars': len(meta.get('_elementor_data', '')),
    'content_chars': len(raw_content),
    'content_sha256_matches': hashlib.sha256(raw_content.encode()).hexdigest() == hashlib.sha256(html.encode()).hexdigest(),
    'required_markers_present': all(marker in raw_content for marker in [
        'Transforme o conhecimento que você acumulou',
        'HISTÓRIAS REAIS',
        'DRA. VANESSA CESNIK',
        '12× DE R$ 247,83',
        'Copyright © Realizando Potenciais',
    ]),
}
OUT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(result, ensure_ascii=False))
