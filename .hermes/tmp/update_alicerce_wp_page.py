#!/usr/bin/env python3
import hashlib, json, os
from pathlib import Path
import requests

BASE=os.environ['WORDPRESS_URL'].rstrip('/')
AUTH=(os.environ['WORDPRESS_USERNAME'],os.environ['WORDPRESS_APP_PASSWORD'])
PAGE_ID=3446
EXPECTED_SLUG='alicerce-do-extraordinario-evento'
HTML_PATH=Path('/home/simplifique/vault/01-Clientes/Realizando-Potenciais/Alicerce-do-Extraordinario/Pagina-de-Vendas/wordpress/alicerce-page.html')
CHECKOUT='https://pay.principia.net/checkout/realizando-potenciais-cursos-e-treinamentos?classes=75297'
s=requests.Session(); s.auth=AUTH
before=s.get(f'{BASE}/wp-json/wp/v2/pages/{PAGE_ID}',params={'context':'edit'},timeout=60); before.raise_for_status(); old=before.json()
if old.get('slug') != EXPECTED_SLUG:
    raise SystemExit(json.dumps({'error':'target_guard_failed','id':PAGE_ID,'slug':old.get('slug')}))
status=old.get('status')
html=HTML_PATH.read_text(encoding='utf-8')
if CHECKOUT not in html or html.count('href="'+CHECKOUT+'"') < 1:
    raise SystemExit(json.dumps({'error':'checkout_guard_failed'}))
elementor_data=[{'id':'alicerce-root','elType':'container','isInner':False,'settings':{'content_width':'full','width':{'unit':'%','size':100,'sizes':[]},'padding':{'unit':'px','top':'0','right':'0','bottom':'0','left':'0','isLinked':True},'margin':{'unit':'px','top':'0','right':'0','bottom':'0','left':'0','isLinked':True}},'elements':[{'id':'alicerce-html','elType':'widget','widgetType':'html','isInner':False,'settings':{'html':html},'elements':[]}]}]
payload={'status':status,'content':html,'template':'elementor_canvas','meta':{'_elementor_edit_mode':'','_elementor_template_type':'wp-page','_elementor_data':'','_elementor_page_settings':{'hide_title':'yes'}}}
r=s.post(f'{BASE}/wp-json/wp/v2/pages/{PAGE_ID}',json=payload,timeout=180)
if r.status_code not in (200,201): raise SystemExit(json.dumps({'error':'update_failed','http':r.status_code,'body':r.text[:800]}))
read=s.get(f'{BASE}/wp-json/wp/v2/pages/{PAGE_ID}',params={'context':'edit'},timeout=60); read.raise_for_status(); d=read.json(); raw=d['content']['raw']; meta=d.get('meta',{})
required=['class="section hero fold-01"','hero_background','hero_vanessa','hero_halo','fold-02',CHECKOUT,'@media(max-width:520px)']
result={'id':d['id'],'status_before':status,'status_after':d['status'],'link':d['link'],'modified_gmt':d['modified_gmt'],'sha256_matches':hashlib.sha256(raw.encode()).hexdigest()==hashlib.sha256(html.encode()).hexdigest(),'required_markers':all(x in raw for x in required),'checkout_links':raw.count('href="'+CHECKOUT+'"'),'elementor_data_chars':len(meta.get('_elementor_data',''))}
print(json.dumps(result,ensure_ascii=False))
