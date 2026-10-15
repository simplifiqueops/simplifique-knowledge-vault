#!/usr/bin/env python3
import hashlib, json, urllib.request
from datetime import datetime, timezone
from pathlib import Path
base=Path('/home/simplifique/vault/10-Simplifique/Marketing/Conteudo/Lote-09/L09-C25-sua-empresa-está-funcionando-ou-você-está-compen')
asset=base/'assets/c25-information-search-pexels-6325909.jpg'
asset.parent.mkdir(parents=True, exist_ok=True)
url='https://images.pexels.com/photos/6325909/pexels-photo-6325909.jpeg?cs=srgb&dl=pexels-vanessa-garcia-6325909.jpg&fm=jpg'
req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
with urllib.request.urlopen(req,timeout=60) as response:
    data=response.read()
asset.write_bytes(data)
metadata={
  'candidate_id':'C25-INFORMATION-SEARCH-A','source':'Pexels','source_id':6325909,
  'page_url':'https://www.pexels.com/photo/person-working-typing-sitting-6325909/',
  'download_url':url,'photographer':'Vanessa Garcia','photographer_url':'https://www.pexels.com/@vanessa-garcia/',
  'dimensions':'3526x5449','source_license_label':'Free','source_license_url':'https://www.pexels.com/license/',
  'accessed_at':datetime.now(timezone.utc).isoformat(),'local_path':str(asset),
  'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),
  'intended_use':'Imagem full-bleed para tornar visível a procura entre notebook, papéis e telefone; não representa cliente ou caso real.'
}
meta=base/'source-metadata/c25-information-search-pexels-6325909.json'
meta.parent.mkdir(parents=True,exist_ok=True)
meta.write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'asset':str(asset),'metadata':str(meta),'bytes':len(data),'sha256':metadata['sha256']},ensure_ascii=False))
