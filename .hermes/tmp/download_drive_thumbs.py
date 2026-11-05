#!/usr/bin/env python3
import os
from pathlib import Path
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.auth.transport.requests import AuthorizedSession

ENV_FILE = "/home/simplifique/.hermes/.env"
if os.path.exists(ENV_FILE):
    for line in open(ENV_FILE, encoding="utf-8"):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k, v)

creds = service_account.Credentials.from_service_account_file(
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
    scopes=["https://www.googleapis.com/auth/drive.readonly"],
)
drive = build("drive", "v3", credentials=creds, cache_discovery=False)
session = AuthorizedSession(creds)
out = Path("/tmp/rp-owned-candidates")
out.mkdir(parents=True, exist_ok=True)

files = {
    "vanessa-BCK_9075": "1mcxJLjZ4lx0muEWsiugnqXXxV_au-E8i",
    "vanessa-BCK_9084": "10L-xzQ-l4G12ydrJGy7zbiKU1DUEvWC_",
    "vanessa-BCK_9098": "1_GsBa3DykgZNfnEm70RpHWsMq7GMWzjW",
    "vanessa-BCK_9101": "1aYmR9m31macGP3eCYUsnY3-4Pn5FbKKV",
    "vanessa-BCK_9104": "1OdfrMbfZ-JuURLkKaOs9E_obi_SKuNu1",
    "vanessa-BCK_9108": "11cgDwbioDPQ1Ix8pdjWXS7SilJXaDTj4",
    "neg-BCK_7417": "1UL-ERtku2IVyrWk2lSZYaHSumbA0Yguc",
    "neg-BCK_7599": "1bpo4wvFxIjSDGy5y6k1VmYu0Fhm2E4zR",
    "neg-BCK_8789": "1_udQo5dIs0bIENmJzWM0qNdcH51IHcBk",
    "neg-BCK_8835": "1GHO11vvvwrGce6Ie1acHqxa0V5WADewm",
    "neg-BCK_8837": "118axcHSpnleZWLM2Srha_n6opPjSHybG",
    "neg-profile": "1MJI2_KZlEtFOw-ApekKPIMGr6BCQYTnn",
    "neg-IMG_8303-smile": "1LRg1Ajn-_lHQOYwzRtMeOLWAlPSRYMIb",
}

for label, file_id in files.items():
    meta = drive.files().get(fileId=file_id, fields="id,name,mimeType,thumbnailLink").execute()
    thumb = meta.get("thumbnailLink")
    if thumb:
        base = thumb.split("=")[0]
        response = session.get(base + "=w1800", timeout=120)
    else:
        response = session.get(f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media", timeout=120)
    response.raise_for_status()
    path = out / f"{label}.jpg"
    path.write_bytes(response.content)
    print(label, meta["name"], len(response.content), path)
