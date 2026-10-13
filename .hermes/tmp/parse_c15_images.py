import json
from pathlib import Path
for file in ['/tmp/pexels-c15-a.json','/tmp/pexels-c15-b.json','/tmp/pixabay-c15.json']:
    data=json.loads(Path(file).read_text())
    print('\n'+file)
    if 'photos' in data:
        for p in data['photos']:
            print(json.dumps({'source':'Pexels','id':p['id'],'width':p['width'],'height':p['height'],'url':p['url'],'photographer':p['photographer'],'photographer_url':p['photographer_url'],'preview':p['src'].get('medium'),'large':p['src'].get('large2x') or p['src'].get('large')},ensure_ascii=False))
    else:
        for p in data.get('hits',[]):
            print(json.dumps({'source':'Pixabay','id':p['id'],'width':p['imageWidth'],'height':p['imageHeight'],'url':p['pageURL'],'author':p['user'],'preview':p['previewURL'],'large':p.get('largeImageURL')},ensure_ascii=False))
