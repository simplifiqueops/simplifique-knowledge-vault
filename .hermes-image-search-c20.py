#!/usr/bin/env python3
import json, os, urllib.parse, urllib.request
from pathlib import Path
out=Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09/L09-C20-lead-parado-não-é-falta-de-interesse-até-você-pr/curation')
out.mkdir(parents=True,exist_ok=True)
queries=['sales follow up desk calendar','business person checking customer records laptop','sales pipeline notes office']
all_results=[]
pex=os.environ.get('PEXELS_API_KEY')
pix=os.environ.get('PIXABAY_API_KEY')
for q in queries:
    if pex:
        try:
            url='https://api.pexels.com/v1/search?'+urllib.parse.urlencode({'query':q,'per_page':8,'orientation':'portrait'})
            req=urllib.request.Request(url,headers={'Authorization':pex,'User-Agent':'SimplifiqueContentWorker/1.0'})
            with urllib.request.urlopen(req,timeout=30) as r: data=json.load(r)
            (out/('pexels-'+urllib.parse.quote(q,safe='').replace('%20','-')+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
            for p in data.get('photos',[]):
                all_results.append({'source':'Pexels','query':q,'id':p['id'],'page_url':p['url'],'author':p['photographer'],'author_url':p['photographer_url'],'width':p['width'],'height':p['height'],'preview':p['src'].get('medium'),'download':p['src'].get('original')})
        except Exception as e:
            all_results.append({'source':'Pexels','query':q,'error':type(e).__name__+': '+str(e)})
    if pix:
        try:
            url='https://pixabay.com/api/?'+urllib.parse.urlencode({'key':pix,'q':q,'image_type':'photo','orientation':'vertical','safesearch':'true','order':'popular','per_page':8})
            req=urllib.request.Request(url,headers={'User-Agent':'SimplifiqueContentWorker/1.0'})
            with urllib.request.urlopen(req,timeout=30) as r: data=json.load(r)
            (out/('pixabay-'+urllib.parse.quote(q,safe='').replace('%20','-')+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
            for p in data.get('hits',[]):
                all_results.append({'source':'Pixabay','query':q,'id':p['id'],'page_url':p['pageURL'],'author':p['user'],'width':p['imageWidth'],'height':p['imageHeight'],'preview':p.get('webformatURL'),'download':p.get('largeImageURL')})
        except Exception as e:
            all_results.append({'source':'Pixabay','query':q,'error':type(e).__name__+': '+str(e)})
(out/'search-summary.json').write_text(json.dumps(all_results,ensure_ascii=False,indent=2))
print(json.dumps(all_results,ensure_ascii=False,indent=2))
