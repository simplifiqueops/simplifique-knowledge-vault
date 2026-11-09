import json
for path in ['/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-08-Fila.json','/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09-Fila.json']:
 d=json.load(open(path,encoding='utf-8'))
 print(path)
 for x in d['items']:
  print({k:x.get(k) for k in ['order','content_key','status','copy_gate','design_authorized','publication_authorized','checkpoint','eligibility','superseded_by','planned_for']}, 'rk=',(x.get('daily_request') or {}).get('request_key') or x.get('request_key'))
