import json
p='/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json'
d=json.load(open(p,encoding='utf-8'))
for item in d['items']:
    if item.get('status') not in {'ready','discarded','deferred_video','published','scheduled'}:
        print(json.dumps(item,ensure_ascii=False,indent=2))
