#!/usr/bin/env python3
"""Genera il sito statico di https://trullo-rosy.it nella cartella dist/.

Uso:  python build.py && python check_links.py
Testi: content.py (6 lingue). Immagini: static/img/. File fissi: static/.
"""
import html
import json
import os
import shutil
from datetime import date

import re

from content import C, DEFAULT, GALLERY_IMAGES, LANGS, PATHS, PLACES
from guides import GUIDES
from guides_valle import GUIDES as GUIDES_VALLE
from guides_eventi import GUIDES as GUIDES_EVENTI
from guides_cibo import GUIDES as GUIDES_CIBO
import reviews as RV

GUIDES = GUIDES + GUIDES_VALLE + GUIDES_EVENTI + GUIDES_CIBO

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
SITE = "https://trullo-rosy.it"
TODAY = date.today().isoformat()

GA4 = "G-91MWCNVPTX"
CF_TOKEN = "15af80a656624e5d92dbbb62ebc88759"
PHONE_VITO, PHONE_VITO_TXT = "+393290614613", "+39 329 06 14 613"
PHONE_ERICA, PHONE_ERICA_TXT = "+393493132669", "+39 349 31 32 669"
EMAIL = "hello@rent-apartment-milan.com"
WHATSAPP = "https://wa.me/393290614613"
AIRBNB = "https://www.airbnb.com/rooms/2627341"
BOOKING = "https://www.booking.com/hotel/it/trullo-rosy.it.html"
ADDR = {"street": "SP70", "zip": "74015", "city": "Martina Franca", "prov": "TA"}
# Dati della struttura (13/11/2026): CIN dalla mail DMS Puglia, orari e ospiti dall'annuncio Airbnb, pin da Google Maps
CIN = "IT073013C200100400"
CHECKIN, CHECKOUT = "15:00", "11:00"
OSPITI_MAX = 6
GEO = {"lat": 40.6526405, "lng": 17.3594071}
NAV_KEYS = ["home", "trullo", "galleria", "dintorni", "contatti"]
ASSET_VER = "6"

# Vecchi indirizzi del sito WordPress -> pagina nuova (usati per le pagine di reindirizzamento)
REDIRECTS = {
    "/contact-trullo-rosy/": "/en/contact/",
    "/contact-us-old/": "/en/contact/",
    "/gallery-2/": "/en/gallery/",
    "/comfort-and-charm-at-trullo-rosy/": "/en/the-trullo/",
    "/accommodation/all-the-rooms/": "/en/the-trullo/",
    "/accommodations/": "/en/the-trullo/",
    "/accommodation-facility/bathroom-essentials/": "/en/the-trullo/",
    "/accommodation-facility/bedroom-comforts/": "/en/the-trullo/",
    "/accommodation-facility/free-parking/": "/en/the-trullo/",
    "/accommodation-facility/heating/": "/en/the-trullo/",
    "/accommodation-facility/terrace/": "/en/the-trullo/",
    "/accommodation-facility/wi-fi/": "/en/the-trullo/",
    "/search-availability/": "/en/contact/",
    "/home/welcome-to-design-hotel/": "/en/",
    "/home/comfortable-rooms/": "/en/the-trullo/",
}

SIZES = {}


def e(s):
    return html.escape(str(s), quote=True)


def load_sizes():
    from PIL import Image
    base = os.path.join(ROOT, "static", "img")
    for dirpath, _, files in os.walk(base):
        for f in files:
            if f.endswith(".webp"):
                rel = os.path.relpath(os.path.join(dirpath, f), base)[:-5].replace(os.sep, "/")
                with Image.open(os.path.join(dirpath, f)) as im:
                    SIZES[rel] = im.size


def img(name, alt, cls="", lazy=True):
    w, h = SIZES[name]
    load = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    c = f' class="{cls}"' if cls else ""
    return f'<img src="/img/{name}.webp" alt="{e(alt)}" width="{w}" height="{h}"{load}{c}>'


def book_buttons(t):
    return (
        '<div class="cta">'
        f'<a class="btn" href="{AIRBNB}" rel="noopener" target="_blank">Airbnb</a>'
        f'<a class="btn" href="{BOOKING}" rel="noopener" target="_blank">Booking.com</a>'
        f'<a class="btn btn-wa" href="{WHATSAPP}" rel="noopener" target="_blank">{e(t["whatsapp"])}</a>'
        "</div>"
    )


# Box "dormi qui" delle guide (13/11/2026): foto del trullo, fatti veri, link con le date già compilate.
# Distanza: dal pin GEO a Locorotondo ~12 km in linea d'aria, circa 20 minuti d'auto.
STAY = {
    "it": dict(facts="Trullo intero per 6 ospiti: 3 camere, camino, giardino e parcheggio. A circa 20 minuti d'auto da Locorotondo, Martina Franca e Alberobello.",
               see="Guarda il trullo e le foto", prices="Vedi prezzi e disponibilità", ask="Chiedi su WhatsApp",
               wa="Ciao, vorrei sapere se Trullo Rosy è libero {d} per {n} persone.",
               dates={"immacolata": "Ponte dell'Immacolata, 5-8 dicembre 2026", "capodanno": "Capodanno, 29 dicembre 2026 - 2 gennaio 2027"}),
    "en": dict(facts="Whole trullo for up to 6 guests: 3 bedrooms, fireplace, garden and parking. About 20 minutes by car from Locorotondo, Martina Franca and Alberobello.",
               see="See the trullo and photos", prices="See prices and availability", ask="Ask on WhatsApp",
               wa="Hi, is Trullo Rosy available {d} for {n} people?",
               dates={"immacolata": "Immaculate Conception weekend, 5-8 December 2026", "capodanno": "New Year, 29 December 2026 - 2 January 2027"}),
    "fr": dict(facts="Trullo entier jusqu'à 6 personnes : 3 chambres, cheminée, jardin et parking. À environ 20 minutes en voiture de Locorotondo, Martina Franca et Alberobello.",
               see="Voir le trullo et les photos", prices="Voir prix et disponibilités", ask="Demander sur WhatsApp",
               wa="Bonjour, Trullo Rosy est-il libre {d} pour {n} personnes ?",
               dates={"immacolata": "Pont de l'Immaculée, 5-8 décembre 2026", "capodanno": "Nouvel An, 29 décembre 2026 - 2 janvier 2027"}),
    "de": dict(facts="Ganzer Trullo für bis zu 6 Gäste: 3 Schlafzimmer, Kamin, Garten und Parkplatz. Etwa 20 Autominuten von Locorotondo, Martina Franca und Alberobello.",
               see="Trullo und Fotos ansehen", prices="Preise und Verfügbarkeit", ask="Per WhatsApp fragen",
               wa="Hallo, ist Trullo Rosy {d} für {n} Personen frei?",
               dates={"immacolata": "Mariä Empfängnis, 5.-8. Dezember 2026", "capodanno": "Silvester, 29. Dezember 2026 - 2. Januar 2027"}),
    "nl": dict(facts="Hele trullo voor maximaal 6 gasten: 3 slaapkamers, open haard, tuin en parkeerplaats. Ongeveer 20 minuten rijden van Locorotondo, Martina Franca en Alberobello.",
               see="Bekijk de trullo en foto's", prices="Bekijk prijzen en beschikbaarheid", ask="Vraag via WhatsApp",
               wa="Hallo, is Trullo Rosy vrij {d} voor {n} personen?",
               dates={"immacolata": "Maria-Onbevlekt-weekend, 5-8 december 2026", "capodanno": "Oud en nieuw, 29 december 2026 - 2 januari 2027"}),
    "es": dict(facts="Trullo entero para hasta 6 huéspedes: 3 dormitorios, chimenea, jardín y aparcamiento. A unos 20 minutos en coche de Locorotondo, Martina Franca y Alberobello.",
               see="Ver el trullo y las fotos", prices="Ver precios y disponibilidad", ask="Preguntar por WhatsApp",
               wa="Hola, ¿está libre Trullo Rosy {d} para {n} personas?",
               dates={"immacolata": "Puente de la Inmaculada, 5-8 de diciembre de 2026", "capodanno": "Fin de año, 29 de diciembre de 2026 - 2 de enero de 2027"}),
}
SEASON_DATES = {
    "natale-locorotondo": [("immacolata", "2026-12-05", "2026-12-08"), ("capodanno", "2026-12-29", "2027-01-02")],
    "mercatini-natale-puglia": [("immacolata", "2026-12-05", "2026-12-08"), ("capodanno", "2026-12-29", "2027-01-02")],
}


def stay_box(g, lang, title, cls="book-box"):
    from urllib.parse import quote
    s = STAY.get(lang, STAY["en"])
    rows = ""
    for k, ci, co in SEASON_DATES.get(g["key"], []):
        lab = s["dates"][k]
        wa = WHATSAPP + "?text=" + quote(s["wa"].format(d="(" + lab + ")", n=4))
        rows += (f'<li><strong>{e(lab)}</strong><span class="cta">'
                 f'<a class="btn btn-small" href="{AIRBNB}?check_in={ci}&amp;check_out={co}&amp;adults=2" rel="noopener" target="_blank">Airbnb</a>'
                 f'<a class="btn btn-small" href="{BOOKING}?checkin={ci}&amp;checkout={co}&amp;group_adults=2" rel="noopener" target="_blank">Booking.com</a>'
                 f'<a class="btn btn-small btn-wa" href="{wa}" rel="noopener" target="_blank">WhatsApp</a></span></li>')
    dates_html = f'<ul class="stay-dates">{rows}</ul>' if rows else ""
    trullo_url = PATHS["trullo"][lang]
    return f"""<aside class="{cls} stay-box" aria-label="{e(title)}">
    <a class="stay-img" href="{trullo_url}">{img('salotto-camino', s['see'])}</a>
    <div>
      <p class="book-box-t">{e(title)}</p>
      <p class="stay-facts">{e(s['facts'])}</p>
      {dates_html if dates_html else ''}
      {'' if dates_html else book_buttons(C[lang])}
      <p class="stay-more"><a href="{trullo_url}">{e(s['see'])} →</a></p>
    </div>
  </aside>"""


def place_name(lang, key, default):
    return C[lang]["dintorni"]["names"].get(key, default)


# ------------------------------------------------------------------ layout

def page(lang, key, title, desc, body, schemas=(), og_image="facciata", noindex=False, paths=None):
    t = C[lang]
    paths = paths or PATHS[key]
    url = SITE + paths[lang]
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{paths[l]}">' for l in LANGS if l in paths)
    alts += f'<link rel="alternate" hreflang="x-default" href="{SITE}{paths.get(DEFAULT, paths[lang])}">'
    nav = "".join(
        f'<a href="{PATHS[k][lang]}"{" aria-current=\"page\"" if k == key else ""}>{e(label)}</a>'
        for k, label in zip(NAV_KEYS, t["nav"])
    )
    langs = "".join(
        f'<a href="{paths.get(l, PATHS["home"][l])}" hreflang="{l}" lang="{l}"{" aria-current=\"true\"" if l == lang else ""}>{l.upper()}</a>'
        for l in LANGS
    )
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    robots = '<meta name="robots" content="noindex">' if noindex else f'<link rel="canonical" href="{url}">\n{alts}'
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="/assets/consent.js?v={ASSET_VER}" data-ga="{GA4}" data-lang="{lang}" data-policy="{PATHS['privacy'][lang]}" data-legacy="tr_consent" data-accent="#3c5229"></script>
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{robots}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Trullo Rosy">
<meta property="og:locale" content="{t['locale']}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/img/{og_image}.webp">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/style.css?v={ASSET_VER}">
{ld}
</head>
<body>
<a class="skip" href="#main">{e(t['skip'])}</a>
<header class="top">
  <div class="wrap top-in">
    <a class="brand" href="{PATHS['home'][lang]}"><img src="/img/logo.png" alt="Trullo Rosy" width="44" height="44"><span>Trullo Rosy</span></a>
    <nav class="nav" aria-label="Menu">{nav}</nav>
    <nav class="langs" aria-label="{e(t['langs_label'])}">{langs}</nav>
    <a class="btn btn-small" href="{PATHS['contatti'][lang]}#prenota">{e(t['book'])}</a>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="foot">
  <div class="wrap foot-in">
    <div>
      <p class="foot-brand">Trullo Rosy</p>
      <p>{e(t['footer_tag'])}</p>
      <p>{ADDR['street']}, {ADDR['zip']} {ADDR['city']} ({ADDR['prov']}), {e(t['country'])}</p>
      <p>CIN {CIN}</p>
    </div>
    <div>
      <p><a href="tel:{PHONE_VITO}">{PHONE_VITO_TXT}</a> (Vito)<br><a href="tel:{PHONE_ERICA}">{PHONE_ERICA_TXT}</a> (Erica)</p>
      <p><a href="{WHATSAPP}" rel="noopener" target="_blank">WhatsApp</a> · <a href="{AIRBNB}" rel="noopener" target="_blank">Airbnb</a> · <a href="{BOOKING}" rel="noopener" target="_blank">Booking.com</a></p>
      <p><a href="{PATHS['privacy'][lang]}">{e(t['privacy'])}</a> · <a href="{PATHS['privacy'][lang]}" data-cc-open>Cookie</a></p>
    </div>
  </div>
  <p class="wrap copy">© {date.today().year} Trullo Rosy</p>
</footer>
<script src="/assets/site.js?v={ASSET_VER}" defer></script>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "{CF_TOKEN}"}}'></script>
</body>
</html>
"""


# ------------------------------------------------------------------ schema

def rental_schema(lang):
    t = C[lang]
    return {
        "@context": "https://schema.org",
        "@type": "VacationRental",
        "@id": SITE + "/#trullo",
        "name": "Trullo Rosy",
        "url": SITE + PATHS["home"][lang],
        "description": t["schema_desc"],
        "image": [f"{SITE}/img/{n}.webp" for n in ("facciata", "esterno-trulli", "camera-silent-nest", "soggiorno", "cucina")],
        "telephone": PHONE_VITO,
        "address": {"@type": "PostalAddress", "streetAddress": ADDR["street"], "postalCode": ADDR["zip"],
                    "addressLocality": ADDR["city"], "addressRegion": ADDR["prov"], "addressCountry": "IT"},
        "containsPlace": {
            "@type": "Accommodation",
            "additionalType": "EntirePlace",
            "numberOfRooms": 3,
            "numberOfBedrooms": 3,
            "floorSize": {"@type": "QuantitativeValue", "value": 85, "unitCode": "MTK"},
            "occupancy": {"@type": "QuantitativeValue", "maxValue": OSPITI_MAX},
            "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": a, "value": True}
                               for _, items in t["amenities"] for a in items],
        },
        "geo": {"@type": "GeoCoordinates", "latitude": GEO["lat"], "longitude": GEO["lng"]},
        "checkinTime": CHECKIN + ":00",
        "checkoutTime": CHECKOUT + ":00",
        "identifier": {"@type": "PropertyValue", "propertyID": "CIN", "value": CIN},
        "sameAs": [AIRBNB, BOOKING],
    }


def faq_schema(lang):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in C[lang]["faq"]]}


def breadcrumb(lang, key):
    t = C[lang]
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": t["nav"][0], "item": SITE + PATHS["home"][lang]},
        {"@type": "ListItem", "position": 2, "name": t["nav"][NAV_KEYS.index(key)], "item": SITE + PATHS[key][lang]}]}


# ------------------------------------------------------------------ pagine

def guide_links(lang):
    items = "".join(f'<li>→ <a href="{g["paths"][lang]}">{e(g[lang]["h1"])}</a></li>' for g in GUIDES if lang in g["paths"])
    return f'<ul class="guide-links">{items}</ul>' if items else ""


def reviews_section(lang):
    r = RV.TXT[lang]
    scores = "".join(
        f'<li><a href="{AIRBNB if k == "airbnb" else BOOKING}" rel="nofollow noopener" target="_blank">'
        f'<strong>{RV.SOURCE_NAME[k]}</strong> {e(r["score"].format(s=v["score"], m=v["scale"], n=v["count"]))}</a></li>'
        for k, v in RV.SCORES.items())
    quotes = "".join(
        f'<figure class="review"><blockquote lang="{ln}"><p>{e(txt)}</p></blockquote>'
        f'<figcaption>{e(name)}{(", " + e(country)) if country else ""} · {RV.SOURCE_NAME[src]} · {e(RV.month_label(lang, ym))} · {e(vote)}</figcaption></figure>'
        for name, country, src, ym, vote, ln, txt in RV.REVIEWS)
    return f"""
<section class="wrap reviews" id="recensioni">
  <h2>{e(r['h2'])}</h2>
  <p>{e(r['intro'])}</p>
  <ul class="scores">{scores}</ul>
  <div class="review-grid">{quotes}</div>
  <p class="note">{e(r['note'])} {e(r['all'])} <a href="{AIRBNB}" rel="nofollow noopener" target="_blank">Airbnb</a> · <a href="{BOOKING}" rel="nofollow noopener" target="_blank">Booking.com</a></p>
</section>
"""


def home(lang):
    t, p = C[lang], C[lang]["home"]
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in t["faq"])
    places = "".join(
        f'<li><a href="{PATHS["dintorni"][lang]}#{k}">{img("luoghi/" + k, place_name(lang, k, n))}<span>{e(place_name(lang, k, n))}</span></a></li>'
        for k, n in PLACES[:6]
    )
    room_imgs = [("camera-silent-nest", "Silent nest"), ("camera-still-bloom", "Still Bloom"), ("alcova", "Alcova")]
    cards = "".join(
        f'<article class="card">{img(i, n)}<h3>{n}</h3><p>{e(txt)}</p></article>'
        for (i, n), txt in zip(room_imgs, p["rooms"])
    )
    body = f"""
<section class="hero">
  {img('facciata', p['hero_alt'], 'hero-img', lazy=False)}
  <div class="hero-text wrap">
    <p class="kicker">{e(p['kicker'])}</p>
    <h1>{e(p['h1'])}</h1>
    <p class="lead">{e(p['lead'])}</p>
    {book_buttons(t)}
  </div>
</section>
<section class="wrap answer">
  <h2>{e(p['what_h2'])}</h2>
  <p>{e(p['what_p'])}</p>
</section>
<section class="wrap split">
  <div>
    <h2>{e(p['story_h2'])}</h2>
    <p>{e(p['story_p'])}</p>
    <p class="motto">{e(p['motto'])}</p>
  </div>
  {img('esterno-trulli', p['ext_alt'], 'round')}
</section>
<section class="band">
  <div class="wrap">
    <h2>{e(p['rooms_h2'])}</h2>
    <div class="cards">{cards}</div>
    <p><a class="more" href="{PATHS['trullo'][lang]}">{e(p['more_rooms'])} →</a></p>
  </div>
</section>
<section class="wrap">
  <h2>{e(p['places_h2'])}</h2>
  <p>{e(p['places_p'])}</p>
  {guide_links(lang)}
  <ul class="places">{places}</ul>
  <p><a class="more" href="{PATHS['dintorni'][lang]}">{e(p['more_places'])} →</a></p>
</section>
{reviews_section(lang)}
<section class="wrap faq">
  <h2>{e(p['faq_h2'])}</h2>
  {faq}
</section>
<section class="wrap final">
  <h2>{e(p['book_h2'])}</h2>
  <p>{e(p['book_p'])}</p>
  {book_buttons(t)}
</section>
"""
    return page(lang, "home", p["title"], p["desc"], body, [rental_schema(lang), faq_schema(lang)])


def trullo(lang):
    t, p = C[lang], C[lang]["trullo"]
    facts = "".join(f'<tr><th scope="row">{e(a)}</th><td>{e(b)}</td></tr>' for a, b in p["facts"])
    am = "".join(f"<div><h3>{e(g)}</h3><ul>{''.join(f'<li>{e(a)}</li>' for a in items)}</ul></div>" for g, items in t["amenities"])
    room_imgs = [("camera-silent-nest-scrittoio", "Silent nest"), ("camera-still-bloom", "Still Bloom"), ("alcova", "Alcova")]
    rooms = "".join(
        f'<article class="room">{img(i, alt)}<div><h2>{n} <small>{e(sub)}</small></h2><p>{e(txt)}</p></div></article>'
        for (i, n), (sub, alt, txt) in zip(room_imgs, p["rooms"])
    )
    body = f"""
<section class="wrap page-head">
  <h1>{e(p['h1'])}</h1>
  <p class="lead">{e(p['lead'])}</p>
</section>
<section class="wrap">
  <h2>{e(p['facts_h2'])}</h2>
  <table class="facts"><tbody>{facts}</tbody></table>
</section>
<section class="wrap rooms">{rooms}</section>
<section class="band">
  <div class="wrap">
    <h2>{e(p['amen_h2'])}</h2>
    <p>{e(p['amen_p'])}</p>
    <div class="amen">{am}</div>
  </div>
</section>
<section class="wrap split">
  <div>
    <h2>{e(p['out_h2'])}</h2>
    <p>{e(p['out_p'])}</p>
  </div>
  {img('pergolato', p['out_alt'], 'round')}
</section>
<section class="wrap final">
  <h2>{e(p['avail_h2'])}</h2>
  {book_buttons(t)}
</section>
"""
    return page(lang, "trullo", p["title"], p["desc"], body, [rental_schema(lang), breadcrumb(lang, "trullo")], og_image="camera-silent-nest")


def galleria(lang):
    t, p = C[lang], C[lang]["galleria"]
    items = "".join(f"<figure>{img(n, c)}<figcaption>{e(c)}</figcaption></figure>" for n, c in zip(GALLERY_IMAGES, p["captions"]))
    body = f"""
<section class="wrap page-head">
  <h1>{e(p['h1'])}</h1>
  <p class="lead">{e(p['lead'])}</p>
</section>
<section class="wrap gallery">{items}</section>
<section class="wrap final">{book_buttons(t)}</section>
"""
    return page(lang, "galleria", p["title"], p["desc"], body, [breadcrumb(lang, "galleria")], og_image="esterno-trulli")


def dintorni(lang):
    t, p = C[lang], C[lang]["dintorni"]
    groups = ["Martina Franca, Alberobello, Locorotondo, Cisternino", "Monopoli, Polignano a Mare, Ostuni, Torre Guaceto",
              "Taranto, Lizzano", "Matera, Ginosa, Gravina in Puglia", "Bari, Trani, Brindisi"]
    rows = "".join(f'<tr><th scope="row">{e(a)}</th><td>{e(b)}</td></tr>' for a, b in zip(p["rows"], groups))
    items = "".join(
        f'<article class="place" id="{k}">{img("luoghi/" + k, place_name(lang, k, n))}<div><h3>{e(place_name(lang, k, n))}</h3><p>{e(p["places"][k])}</p></div></article>'
        for k, n in PLACES
    )
    body = f"""
<section class="wrap page-head">
  <h1>{e(p['h1'])}</h1>
  <p class="lead">{e(p['lead'])}</p>
</section>
<section class="wrap">
  <h2>{e(p['table_h2'])}</h2>
  <table class="facts"><thead><tr><th scope="col">{e(p['th'][0])}</th><th scope="col">{e(p['th'][1])}</th></tr></thead><tbody>{rows}</tbody></table>
</section>
<section class="wrap">{guide_links(lang)}</section>
<section class="wrap places-list">{items}</section>
<section class="wrap final">
  <h2>{e(p['final_h2'])}</h2>
  {book_buttons(t)}
</section>
"""
    return page(lang, "dintorni", p["title"], p["desc"], body, [breadcrumb(lang, "dintorni")], og_image="panorama-valle-itria")


def contatti(lang):
    t, p = C[lang], C[lang]["contatti"]
    q = "Trullo+Rosy+SP70+74015+Martina+Franca"
    body = f"""
<section class="wrap page-head">
  <h1>{e(p['h1'])}</h1>
  <p class="lead">{e(p['lead'])}</p>
</section>
<section class="wrap split" id="prenota">
  <div>
    <h2>{e(p['how_h2'])}</h2>
    <p>{e(p['how_p'])}</p>
    {book_buttons(t)}
  </div>
  <div class="contact-box">
    <h2>{e(p['write_h2'])}</h2>
    <p><strong>Vito</strong>: <a href="tel:{PHONE_VITO}">{PHONE_VITO_TXT}</a></p>
    <p><strong>Erica</strong>: <a href="tel:{PHONE_ERICA}">{PHONE_ERICA_TXT}</a></p>
    <p>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <h3>{e(p['address_h2'])}</h3>
    <p>{ADDR['street']}, {ADDR['zip']} {ADDR['city']} ({ADDR['prov']}), {e(t['country'])}</p>
    <p><a href="https://www.google.com/maps/search/?api=1&amp;query={q}" rel="noopener" target="_blank">{e(p['maps'])}</a></p>
  </div>
</section>
"""
    return page(lang, "contatti", p["title"], p["desc"], body, [rental_schema(lang), breadcrumb(lang, "contatti")], og_image="veranda")


def privacy(lang):
    p = C[lang]["privacy_page"]
    body = f"""
<section class="wrap page-head prose">
  <h1>{e(p['h1'])}</h1>
  <p>{e(p['p1'])}</p>
  <h2>{e(p['stats_h2'])}</h2>
  <p>{e(p['cf'])}</p>
  <p>{e(p['ga'])} <button type="button" class="linkbtn" data-cc-open>{e(p['reset'])}</button></p>
  <h2>{e(p['book_h2'])}</h2>
  <p>{e(p['book_p'])}</p>
  <h2>{e(p['contact_h2'])}</h2>
  <p>{e(p['contact_p'])} <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</section>
"""
    return page(lang, "privacy", p["title"], p["desc"], body)


def not_found():
    links = " ".join(f'<a class="btn btn-small" href="{PATHS["home"][l]}" lang="{l}">{C[l]["name"]}</a>' for l in LANGS)
    lines = "".join(f'<p lang="{l}">{e(C[l]["notfound"]["p"])}</p>' for l in LANGS)
    body = f"""
<section class="wrap page-head">
  <h1>{e(C['it']['notfound']['h1'])} · {e(C['en']['notfound']['h1'])}</h1>
  {lines}
  <div class="cta">{links}</div>
</section>
"""
    return page("it", "home", C["it"]["notfound"]["title"], C["it"]["notfound"]["p"], body, noindex=True)


def redirect_page(target):
    url = SITE + target
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Trullo Rosy</title>
<link rel="canonical" href="{url}">
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={target}">
<script>location.replace("{target}"+location.hash)</script>
</head><body><p><a href="{target}">{url}</a></p></body></html>
"""


GUIDE_LABEL = {"it": "Guida", "en": "Guide", "fr": "Guide", "de": "Reisetipps", "nl": "Gids", "es": "Guía"}


def guide(g, lang):
    t, p = C[lang], g[lang]
    import json as _json
    cred = {}
    for folder in {m.split("/")[0] for m in re.findall(r"\{\{img:([^|}]+)", p["body"]) + [g["hero"]]}:
        fp = os.path.join(ROOT, "static", "img", folder, "crediti.json")
        if os.path.exists(fp):
            for k, v in _json.load(open(fp, encoding="utf-8")).items():
                cred[f"{folder}/{k}"] = v
    used = [g["hero"]]

    def fig(m):
        name, alt = m.group(1), m.group(2)
        used.append(name)
        c = cred.get(name)
        cap = f'<figcaption>{e(alt)}' + (f' · Foto: {e(c["autore"])}, {e(c["licenza"])}' if c else "") + "</figcaption>"
        return f"<figure class=\"g-fig\">{img(name, alt)}{cap}</figure>"

    body_html = re.sub(r"\{\{img:([^|}]+)\|([^}]+)\}\}", fig, p["body"])
    srcs = "".join(f'<li><a href="{u}" rel="noopener" target="_blank">{e(n)}</a></li>' for n, u in g["sources"])
    photos = "".join(
        f'<li>{e(cred[n]["titolo"][5:])}: {e(cred[n]["autore"])}, <a href="{cred[n]["licenza_url"]}" rel="noopener license" target="_blank">{e(cred[n]["licenza"])}</a>, <a href="{cred[n]["pagina"]}" rel="noopener" target="_blank">Wikimedia Commons</a></li>'
        for n in dict.fromkeys(used) if n in cred
    )
    hero_c = cred.get(g["hero"])
    url = SITE + g["paths"][lang]
    art = {"@context": "https://schema.org", "@type": "Article", "headline": p["h1"], "description": p["desc"],
           "datePublished": g["date"], "dateModified": g.get("modified", g["date"]), "inLanguage": lang, "mainEntityOfPage": url,
           "image": f"{SITE}/img/{g['hero']}.webp", "author": {"@type": "Organization", "name": "Trullo Rosy", "url": SITE},
           "publisher": {"@type": "Organization", "name": "Trullo Rosy", "logo": f"{SITE}/img/logo.png"}}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": t["nav"][0], "item": SITE + PATHS["home"][lang]},
        {"@type": "ListItem", "position": 2, "name": p["h1"], "item": url}]}
    body = f"""
<section class="hero hero-guide">
  {img(g['hero'], p['h1'], 'hero-img', lazy=False)}
  <div class="hero-text wrap">
    <p class="kicker">{GUIDE_LABEL.get(lang, '')} · {e(p['updated'])}</p>
    <h1>{e(p['h1'])}</h1>
  </div>
</section>
<article class="wrap guide">
  <p class="answer-box">{e(p['answer'])}</p>
  {stay_box(g, lang, p['cta_h2'])}
  {body_html}
  <section class="final">
    <h2>{e(p['cta_h2'])}</h2>
    {stay_box(g, lang, p['cta_h2'], cls="stay-final")}
    {book_buttons(t)}
  </section>
  <h2>{e(p['sources_h2'])}</h2>
  <ul class="small">{srcs}</ul>
  {f'<h2>{e(p["photos_h2"])}</h2><ul class="small">{photos}</ul>' if photos else ''}
</article>
"""
    return page(lang, "home", p["title"], p["desc"], body, [art, faq, bc], og_image=g["hero"], paths=g["paths"])


BUILDERS = {"home": home, "trullo": trullo, "galleria": galleria, "dintorni": dintorni, "contatti": contatti, "privacy": privacy}


def write(path, content):
    full = os.path.join(DIST, path.lstrip("/"))
    if path.endswith("/"):
        full = os.path.join(full, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def sitemap():
    out = []
    for key, langs in PATHS.items():
        if key == "privacy":
            continue
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{SITE}{langs[l]}"/>' for l in LANGS)
        alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{langs[DEFAULT]}"/>'
        for l in LANGS:
            out.append(f"<url><loc>{SITE}{langs[l]}</loc><lastmod>{TODAY}</lastmod>{alts}</url>")
    for g in GUIDES:
        ps = g["paths"]
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{SITE}{p}"/>' for l, p in ps.items())
        for l, p in ps.items():
            out.append(f"<url><loc>{SITE}{p}</loc><lastmod>{g.get('modified', g['date'])}</lastmod>{alts}</url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + "\n".join(out) + "\n</urlset>\n")


def llms():
    lines = [
        "# Trullo Rosy", "",
        "> Trullo tradizionale in affitto (intera casa) nelle campagne di Martina Franca (TA), Valle d'Itria, Puglia. "
        "85 m², 3 camere (2 letti queen size, 1 letto singolo), fino a 6 ospiti, check-in dalle 15:00 e check-out entro le 11:00, CIN IT073013C200100400, cucina attrezzata, Wi-Fi, "
        "parcheggio gratuito, giardino con uliveto, amaca e barbecue. Indirizzo: SP70, 74015 Martina Franca (TA). "
        "Prenotazioni: Airbnb, Booking.com, WhatsApp +39 329 06 14 613.", "",
    ]
    for l in LANGS:
        t = C[l]
        lines.append(f"## {t['name']}")
        for k, label in zip(NAV_KEYS, t["nav"]):
            lines.append(f"- [{label}]({SITE}{PATHS[k][l]})")
        lines.append("")
    lines.append("## Guide / Guides")
    for g in GUIDES:
        for l, p in g["paths"].items():
            lines.append(f"- [{g[l]['h1']}]({SITE}{p})")
    lines.append("")
    lines += ["## Recensioni / Reviews",
              f"- Airbnb: {RV.SCORES['airbnb']['score']}/5 su {RV.SCORES['airbnb']['count']} recensioni ({AIRBNB})",
              f"- Booking.com: {RV.SCORES['booking']['score']}/10 su {RV.SCORES['booking']['count']} recensioni ({BOOKING})",
              f"- Dati letti il {RV.LETTE_IL}; estratti in {SITE}/#recensioni", ""]
    lines += ["## Prenotazioni / Booking", f"- Airbnb: {AIRBNB}", f"- Booking.com: {BOOKING}", f"- WhatsApp: {WHATSAPP}", ""]
    return "\n".join(lines)


def main():
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    load_sizes()
    shutil.copytree(os.path.join(ROOT, "static"), DIST)
    for key, fn in BUILDERS.items():
        for lang in LANGS:
            write(PATHS[key][lang], fn(lang))
    for g in GUIDES:
        for lang, path in g["paths"].items():
            write(path, guide(g, lang))
    for old, new in REDIRECTS.items():
        write(old, redirect_page(new))
    write("/404.html", not_found())
    write("/sitemap.xml", sitemap())
    write("/llms.txt", llms())
    n = sum(len(v) for v in PATHS.values())
    print(f"{n} pagine, {len(REDIRECTS)} reindirizzamenti -> {DIST}")


if __name__ == "__main__":
    main()
