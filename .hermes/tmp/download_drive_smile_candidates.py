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
out=Path('/tmp/rp-neg-smiles');out.mkdir(parents=True,exist_ok=True)
files={
'IMG_7838':'18Zs2ivM8r7J0UIZbtOstDOaS7OjJamvg','IMG_7839':'1ZGcmRcVTnY4-cMBrTtgr9hrObV1rSrLu','IMG_7856':'1DZRNjZ2EbnqBaeefbrts5_l4s5NUSFno','IMG_7864':'1S8PUDFGRdBJan4xkHRu5BcZJWC1DyFV7','IMG_7885':'1TOJL3xHmG-ydgsLBTZIVoTTD1QAhZyMO','IMG_7896':'1N_M7LFHvIyVmkbydm4ZpoRL66wWYL-AR','IMG_7977':'1rj35cokqfGl6iUC-dY54keyUfZvEsYjW','IMG_8243':'14cu8zRzJekGF-qEBhosZmnuwo3_Qtgwz','IMG_8253':'19DRoMC_VsD1ygw1-ytAqKJ1SN2cMx7YZ','IMG_8259':'1ehOsRUVthYzPcCXdHwVUDx2flx_jAO4p','IMG_8266':'1mCH9c8ZGRUBvVdTex14FPSr72gTc3Oba','IMG_8282':'1Q3G8gfiEoRp64c1XBGBbtmbZ0Kz1-v0F','IMG_8296':'1wotmkdHlxBnrrVwvcJXN0cr9pIkVgsw-','IMG_8309':'1FXogrI037ifwiHKBRFxdujGMgjNAI1rd','IMG_8310':'19MoO6gtuKhy4seeVbKeF-ZWT3OB-4BUZ','IMG_8314':'1G1mSZPc0fqqA1vwnj-F9qHzO8B6IZnBS'}
for label,fid in files.items():
    meta=drive.files().get(fileId=fid,fields='id,name,thumbnailLink').execute();thumb=meta.get('thumbnailLink')
    url=thumb.split('=')[0]+'=w1600' if thumb else f'https://www.googleapis.com/drive/v3/files/{fid}?alt=media'
    r=session.get(url,timeout=120);r.raise_for_status();p=out/f'{label}.jpg';p.write_bytes(r.content);print(label,len(r.content))
