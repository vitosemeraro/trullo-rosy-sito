# trullo-rosy.it

Sito statico di Trullo Rosy (Martina Franca, Valle d'Itria) in 6 lingue: it, en, fr, de, nl, es.

- `content.py`: tutti i testi, per lingua. Solo fatti veri sul trullo.
- `build.py`: genera il sito in `dist/` (pagine, sitemap con hreflang, llms.txt, schema VacationRental e FAQPage, pagine di reindirizzamento dai vecchi indirizzi WordPress).
- `check_links.py`: controlla link interni, HTML, title e description.
- `static/`: immagini (`img/`), CSS e JS (`assets/`), robots.txt, `.htaccess` (usato solo su hosting Apache).

Prova in locale: `pip install pillow && python build.py && python check_links.py`.

Ogni push su `main` pubblica il sito con il workflow in `.github/workflows/`.
