#!/usr/bin/env python3
import json
import mimetypes
import os
from pathlib import Path
from urllib.parse import urlparse

import requests

BASE = os.environ["WORDPRESS_URL"].rstrip("/")
AUTH = (os.environ["WORDPRESS_USERNAME"], os.environ["WORDPRESS_APP_PASSWORD"])
ASSET_DIR = Path("/home/simplifique/vault/01-Clientes/Realizando-Potenciais/Alicerce-do-Extraordinario/Pagina-de-Vendas/assets/editorial")
EXEC_DIR = Path("/tmp/alicerce-figma-exec")
HERO_DIR = Path("/home/simplifique/vault/01-Clientes/Realizando-Potenciais/Alicerce-do-Extraordinario/Pagina-de-Vendas/assets/figma-hero")
SUSTAIN_DIR = Path("/home/simplifique/vault/01-Clientes/Realizando-Potenciais/Alicerce-do-Extraordinario/Pagina-de-Vendas/assets/figma-sustentar")
TESTIMONIAL_DIR = Path("/home/simplifique/vault/01-Clientes/Realizando-Potenciais/Alicerce-do-Extraordinario/Pagina-de-Vendas/assets/depoimentos")
FIGMA_UPDATES_DIR = Path("/home/simplifique/vault/01-Clientes/Realizando-Potenciais/Alicerce-do-Extraordinario/Pagina-de-Vendas/assets/figma-updates-2026-11-05")
OUT = Path("/home/simplifique/vault/.hermes/tmp/alicerce-wp-assets.json")

ASSETS = {
    "projetos": ASSET_DIR / "pexels-19905182-projetos.jpg",
    "valor": ASSET_DIR / "pexels-34086093-valor.jpg",
    "cobranca": ASSET_DIR / "pexels-7688187-cobranca.jpg",
    "agenda": ASSET_DIR / "pexels-8646391-agenda.jpg",
    "implementacao": ASSET_DIR / "pexels-5905852-implementacao.jpg",
    "imersoes": ASSET_DIR / "pexels-18999470-imersoes.jpg",
    "acesso": ASSET_DIR / "pexels-1558691-acesso-anual.jpg",
    "energia": ASSET_DIR / "pexels-10057634-energia.jpg",
    "intimidade": ASSET_DIR / "pexels-34436646-intimidade.jpg",
    "labex": ASSET_DIR / "pexels-19895721-labex.jpg",
    "vanessa": ASSET_DIR / "vanessa-BCK_9101-sorrindo.jpg",
    "neg": ASSET_DIR / "neg-IMG_8303-sorrindo.jpg",
    "grupo": EXEC_DIR / "1.jpeg",
    "whatsapp": EXEC_DIR / "4.png",
    "labex_oficial": EXEC_DIR / "3.jpeg",
    "hero_background": HERO_DIR / "hero-background.png",
    "hero_vanessa": HERO_DIR / "hero-vanessa.png",
    "hero_halo": HERO_DIR / "hero-halo.svg",
    "energia_figma_desktop": SUSTAIN_DIR / "energia-desktop.png",
    "intimidade_figma_desktop": SUSTAIN_DIR / "intimidade-desktop.png",
    "labex_figma_desktop": SUSTAIN_DIR / "labex-desktop.jpg",
    "energia_figma_mobile": SUSTAIN_DIR / "energia-mobile.jpg",
    "intimidade_figma_mobile": SUSTAIN_DIR / "intimidade-mobile.jpg",
    "labex_figma_mobile": SUSTAIN_DIR / "labex-mobile.jpg",
    "testimonial_paloma": TESTIMONIAL_DIR / "paloma-1.png",
    "testimonial_gicela": TESTIMONIAL_DIR / "gicela-1.png",
    "testimonial_andrea": TESTIMONIAL_DIR / "andrea-1.png",
    "testimonial_elaine": TESTIMONIAL_DIR / "elaine-1.png",
    "jornada_background": FIGMA_UPDATES_DIR / "jornada-bg-1.png",
    "construir_background": FIGMA_UPDATES_DIR / "construir-raw-2.png",
    "destravar_csv": FIGMA_UPDATES_DIR / "destravar-csv.png",
    "destravar_grupo": FIGMA_UPDATES_DIR / "destravar-grupo.png",
    "destravar_guardiao": FIGMA_UPDATES_DIR / "destravar-guardiao.png",
    "construir_projeto": FIGMA_UPDATES_DIR / "construir-projeto.png",
    "construir_presenca": FIGMA_UPDATES_DIR / "construir-presenca.png",
    "construir_conexao": FIGMA_UPDATES_DIR / "construir-conexao.png",
}

session = requests.Session()
session.auth = AUTH


def existing_media(filename: str):
    stem = Path(filename).stem
    r = session.get(f"{BASE}/wp-json/wp/v2/media", params={"search": stem, "per_page": 100, "context": "edit"}, timeout=30)
    r.raise_for_status()
    for item in r.json():
        source_name = Path(urlparse(item.get("source_url", "")).path).name
        if source_name == filename or source_name.startswith(stem + ".") or source_name.startswith(stem + "-"):
            return item
    return None


def upload(key: str, path: Path):
    if not path.exists():
        raise FileNotFoundError(path)
    filename = f"alicerce-{key}{path.suffix.lower()}"
    found = existing_media(filename)
    if found:
        return found, False
    mime = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    headers = {
        "Content-Disposition": f'attachment; filename="{filename}"',
        "Content-Type": mime,
    }
    r = session.post(f"{BASE}/wp-json/wp/v2/media", headers=headers, data=path.read_bytes(), timeout=120)
    r.raise_for_status()
    item = r.json()
    # Add traceable alt text/title without changing the source file.
    meta = {
        "title": f"Alicerce — {key.replace('_', ' ').title()}",
        "alt_text": f"Imagem da página Alicerce do Extraordinário — {key.replace('_', ' ')}",
        "caption": "",
        "description": "Ativo aprovado no Figma da página Alicerce do Extraordinário.",
    }
    u = session.post(f"{BASE}/wp-json/wp/v2/media/{item['id']}", json=meta, timeout=30)
    u.raise_for_status()
    return u.json(), True

result = {}
created = []
for key, path in ASSETS.items():
    item, was_created = upload(key, path)
    result[key] = {"id": item["id"], "url": item["source_url"], "created": was_created}
    if was_created:
        created.append(item["id"])

OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({"asset_count": len(result), "created_count": len(created), "created_ids": created, "mapping_path": str(OUT)}, ensure_ascii=False))
