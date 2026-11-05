#!/usr/bin/env python3
import os
from pathlib import Path
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.auth.transport.requests import AuthorizedSession
for line in open('/home/simplifique/.hermes/.env', encoding='utf-8'):
    line=line.strip()
    if line and not line.startswith('#') and '=' in line:
        k,v=line.split('=',1);os.environ.setdefault(k,v)
creds=service_account.Credentials.from_service_account_file(os.environ['GOOGLE_APPLICATION_CREDENTIALS'],scopes=['https://www.googleapis.com/auth/drive.readonly'])
drive=build('drive','v3',credentials=creds,cache_discovery=False);session=AuthorizedSession(creds)
out=Path('/tmp/neg-sequence');out.mkdir(parents=True,exist_ok=True)
folder='1zqrPvxea_QTP2AbRYKWt_GwGyGiNIHcJ'
res=drive.files().list(q=f"'{folder}' in parents and trashed=false",pageSize=200,fields='files(id,name,mimeType,thumbnailLink)',orderBy='name').execute()
files=[f for f in res.get('files',[]) if f.get('mimeType','').startswith('image/')]
for i,f in enumerate(files,1):
    thumb=f.get('thumbnailLink')
    if not thumb: continue
    r=session.get(thumb.split('=')[0]+'=w640',timeout=60);r.raise_for_status();p=out/(Path(f['name']).stem+'.jpg');p.write_bytes(r.content)
    if i%20==0: print('downloaded',i)
print('total',len(list(out.glob('*.jpg'))))
