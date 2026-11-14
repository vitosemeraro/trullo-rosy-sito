# trullo-rosy.it

Sito statico di Trullo Rosy (Martina Franca, Valle d'Itria) in 6 lingue: it, en, fr, de, nl, es.

- `content.py`: tutti i testi, per lingua. Solo fatti veri sul trullo.
- `build.py`: genera il sito in `dist/` (pagine, sitemap con hreflang, llms.txt, schema VacationRental e FAQPage, pagine di reindirizzamento dai vecchi indirizzi WordPress).
- `check_links.py`: controlla link interni, HTML, title e description.
- `static/`: immagini (`img/`), CSS e JS (`assets/`), robots.txt, `.htaccess` (usato solo su hosting Apache).

Prova in locale: `pip install pillow && python build.py && python check_links.py`.

Ogni push su `main` pubblica il sito con il workflow in `.github/workflows/`.

## Contatore anonimo dei clic

`worker/ev.js` è il Cloudflare Worker `trullo-ev` (https://trullo-ev.cfdist2.workers.dev) con il database D1 `trullo-events`.
`static/assets/site.js` gli manda ogni clic su Airbnb, Booking.com, WhatsApp, telefono ed email, anche senza consenso ai cookie:
non usa cookie e salva solo minuto, evento, pagina e lingua. I conteggi si leggono da https://trullo-ev.cfdist2.workers.dev/ev-stats?days=35
oppure con una query D1 dall'API Cloudflare. Se cambi `worker/ev.js`, ricaricalo su Cloudflare (non c'è deploy automatico del worker).
