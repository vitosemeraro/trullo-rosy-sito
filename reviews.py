"""Recensioni vere di Trullo Rosy, copiate da Airbnb e Booking.com il 14/11/2026.

Regola: solo recensioni reali, testo originale (eventuali tagli segnati con …),
nome come appare sul portale, mese del soggiorno. Niente traduzioni inventate.
Per aggiornare: rileggi https://www.airbnb.it/rooms/2627341/reviews e la scheda Booking.
"""

LETTE_IL = "2026-11-14"

SCORES = {
    "airbnb": {"score": "4,6", "scale": "5", "count": 30},
    "booking": {"score": "8,4", "scale": "10", "count": 6},
}

# (nome, provenienza o "", fonte, mese AAAA-MM, voto, lingua del testo, testo)
REVIEWS = [
    ("Martina", "", "airbnb", "2026-08", "5/5", "it",
     "Abbiamo soggiornato nel trullo di Vito e ci siamo trovati davvero benissimo! Vito è stato un host super reattivo, "
     "disponibile e sempre molto amichevole. Il trullo è bellissimo e avere tutto il giardino a nostra disposizione ha reso "
     "il soggiorno ancora più piacevole. … La casa è inoltre super fornita: ci sono piatti, padelle e tutto quello che può "
     "servire, davvero non manca nulla."),
    ("Lucia", "Italia", "booking", "2025-12", "9/10", "it",
     "Casa accogliente e confortevole, ideale per un soggiorno in totale relax. L'host Vito ci ha seguito con puntualità e "
     "cortesia per ogni esigenza."),
    ("Jules", "France", "booking", "2025-07", "8/10", "fr",
     "Logement très agréable, fonctionnel et bien placé. L’échange avec Vito a été fluide et les réponses rapides. "
     "À recommander"),
    ("Antonella", "", "airbnb", "2023-09", "5/5", "it",
     "Vito è stato un host gentilissimo e attento, i trulletti sono davvero un posto magico e rilassante!! Oltre che pulito.. "
     "Ci tornerei volentieri e raccomando Vito e il suo fantastico alloggio!"),
    ("Lyn", "", "airbnb", "2023-07", "5/5", "en",
     "We stayed at Trullo Rosa for 9 nights, it was in a really good location for getting to other towns. Martina Franca, "
     "the nearest town, is just stunning and has a brilliant Wednesday Market. Trullo Rosa is just like the photos, "
     "characterful and tastefully furnished."),
    ("Karen", "", "airbnb", "2023-06", "5/5", "en",
     "We had a wonderful holiday at Trullo Rosy. The Trullo is beautiful and very clean with every facility anyone could "
     "need. the garden is quiet and private, a lovely place to relax after a day out sightseeing. … thank you Vito, youre "
     "home is the best we have stayed in."),
    ("Carla", "", "airbnb", "2023-03", "5/5", "fr",
     "Endroit très agréable et surtout tranquille, a proximité de tout ce que nous souhaitions visiter. Vito est très "
     "accessible et réactif. Je recommande"),
    ("Sebastian", "", "airbnb", "2023-01", "5/5", "en",
     "Wonderful trullo, full of magic for a dream vacation with kids. Just the perfect place in the middle of the most "
     "beautiful cities and landscapes of Puglia. Highly recommended."),
]

MONTHS = {
    "it": ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"],
    "en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "fr": ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"],
    "de": ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"],
    "nl": ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober", "november", "december"],
    "es": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
}

TXT = {
    "it": dict(h2="Cosa dicono gli ospiti",
               intro="Valutazioni e recensioni vere degli ospiti su Airbnb e Booking.com, nella lingua in cui sono state scritte.",
               score="{s} su {m} · {n} recensioni", note="Dati letti il 14 novembre 2026.", all="Leggi tutte le recensioni su"),
    "en": dict(h2="What our guests say",
               intro="Real ratings and guest reviews from Airbnb and Booking.com, in the language they were written in.",
               score="{s} out of {m} · {n} reviews", note="Figures checked on 14 November 2026.", all="Read all reviews on"),
    "fr": dict(h2="L'avis de nos hôtes",
               intro="Notes et avis réels des voyageurs sur Airbnb et Booking.com, dans la langue où ils ont été écrits.",
               score="{s} sur {m} · {n} avis", note="Données relevées le 14 novembre 2026.", all="Lire tous les avis sur"),
    "de": dict(h2="Was unsere Gäste sagen",
               intro="Echte Bewertungen von Gästen auf Airbnb und Booking.com, in der Sprache, in der sie geschrieben wurden.",
               score="{s} von {m} · {n} Bewertungen", note="Stand: 14. November 2026.", all="Alle Bewertungen auf"),
    "nl": dict(h2="Wat onze gasten zeggen",
               intro="Echte beoordelingen van gasten op Airbnb en Booking.com, in de taal waarin ze zijn geschreven.",
               score="{s} van {m} · {n} beoordelingen", note="Gegevens van 14 november 2026.", all="Lees alle beoordelingen op"),
    "es": dict(h2="Lo que dicen nuestros huéspedes",
               intro="Valoraciones y reseñas reales de huéspedes en Airbnb y Booking.com, en el idioma en que se escribieron.",
               score="{s} de {m} · {n} reseñas", note="Datos consultados el 14 de noviembre de 2026.", all="Lee todas las reseñas en"),
}

SOURCE_NAME = {"airbnb": "Airbnb", "booking": "Booking.com"}


def month_label(lang, ym):
    y, m = ym.split("-")
    return f"{MONTHS[lang][int(m) - 1]} {y}"
