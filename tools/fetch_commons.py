#!/usr/bin/env python3
"""Scarica da Wikimedia Commons foto con licenza libera per le guide.

Uso: python tools/fetch_commons.py "<ricerca>" <cartella> [max]
Salva le immagini in static/img/<cartella>/ (webp, 1280px) e i crediti in
static/img/<cartella>/crediti.json (autore, licenza, pagina del file).
Tiene solo licenze CC BY, CC BY-SA, CC0 e pubblico dominio.
"""
import io, json, os, re, sys, urllib.parse, urllib.request
from PIL import Image

UA = {"User-Agent": "trullo-rosy-sito-build/1.0 (https://trullo-rosy.it)"}
API = "https://commons.wikimedia.org/w/api.php"
OK = re.compile(r"^(CC BY(-SA)? [0-9.]+|CC0|Public domain|PD)", re.I)


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        return r.read()


def strip(s):
    return re.sub(r"<[^>]+>", "", s or "").strip()


def main():
    q, folder = sys.argv[1], sys.argv[2]
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    root = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static", "img", folder)
    os.makedirs(root, exist_ok=True)
    cred_path = os.path.join(root, "crediti.json")
    credits = json.load(open(cred_path)) if os.path.exists(cred_path) else {}
    params = {"action": "query", "format": "json", "generator": "search", "gsrnamespace": 6,
              "gsrsearch": q + " filetype:bitmap", "gsrlimit": 50, "prop": "imageinfo",
              "iiprop": "url|extmetadata|size", "iiurlwidth": 1280}
    data = json.loads(get(API + "?" + urllib.parse.urlencode(params)))
    pages = sorted(data.get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 0))
    saved = 0
    for p in pages:
        if saved >= n:
            break
        ii = p["imageinfo"][0]
        md = ii.get("extmetadata", {})
        lic = strip(md.get("LicenseShortName", {}).get("value"))
        if not OK.match(lic) or ii.get("width", 0) < 900:
            continue
        slug = re.sub(r"[^a-z0-9]+", "-", p["title"][5:].rsplit(".", 1)[0].lower()).strip("-")[:60]
        if slug in credits:
            saved += 1
            continue
        try:
            im = Image.open(io.BytesIO(get(ii["thumburl"]))).convert("RGB")
        except Exception as ex:  # noqa: BLE001
            print("salto", p["title"], ex)
            continue
        im.save(os.path.join(root, slug + ".webp"), "WEBP", quality=78, method=6)
        credits[slug] = {
            "titolo": p["title"],
            "descrizione": strip(md.get("ImageDescription", {}).get("value"))[:300],
            "autore": strip(md.get("Artist", {}).get("value"))[:120],
            "licenza": lic,
            "licenza_url": md.get("LicenseUrl", {}).get("value", ""),
            "pagina": ii.get("descriptionurl"),
        }
        saved += 1
        print("ok", slug, lic)
    json.dump(credits, open(cred_path, "w"), ensure_ascii=False, indent=1)
    print(saved, "immagini in", root)


if __name__ == "__main__":
    main()
