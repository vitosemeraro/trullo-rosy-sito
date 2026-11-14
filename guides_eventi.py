"""Guida "Eventi in Valle d'Itria, inverno 2026-27" (14/11/2026).

Stesso formato di guides.py. Solo date pubblicate da Comuni, enti o testate citate in fondo.
Le date 2026-27 non ancora annunciate sono scritte come "da confermare": aggiornare la pagina
(e il campo modified) quando i Comuni pubblicano i programmi di Natale e Capodanno.
"""

SRC = [
    ("Comune di Locorotondo, avviso \"Natale a Locorotondo 2026\" (7 settembre 2026)",
     "https://www.comune.locorotondo.ba.it/it/news/natale-a-locorotondo-2026-avviso-pubblico-per-la-presentazione-di-proposte-progettuali"),
    ("HelloApulia, \"Capodanno 2026 in Puglia: 5 feste in piazza con orari e programma\" (17 dicembre 2025)",
     "https://www.helloapulia.com/en/blog/capodanno-puglia-cinque-valle-ditria-monopoli"),
    ("Festival della Valle d'Itria / Fondazione Paolo Grassi, \"Concerto di Capodanno 2026 a Martina Franca\" (23 dicembre 2025)",
     "https://www.festivaldellavalleditria.it/en/new-years-concert-2026-martina-franca"),
    ("HelloApulia, \"Mercatini e luci di Natale in Valle d'Itria\" (programma 2025, 26 novembre 2025)",
     "https://www.helloapulia.com/it/blog/mercatini-luci-natale-valle-ditria"),
    ("Carnevale di Putignano, sito ufficiale: \"Carnevale di Putignano 2027: ecco le date della 633ª edizione\"",
     "https://www.carnevalediputignano.it/"),
    ("Italia.it, \"Carnevale di Putignano\" (edizione 26 dicembre 2026 – 2027)",
     "https://www.italia.it/it/puglia/bari/cosa-fare/evento-carnevale-di-putignano"),
]

FAQ_IT = [
    ("Quali eventi ci sono in Valle d'Itria a Capodanno?", "Nel Capodanno 2026 ci sono state feste in piazza a Martina Franca (piazza XX Settembre), Alberobello (largo Martellotta), Cisternino (piazza Vittorio Emanuele) e Ostuni (piazza della Libertà), e il 1° gennaio un concerto gratuito in piazza XX Settembre a Martina Franca. Il programma del Capodanno 2027 non è ancora stato annunciato."),
    ("Fino a quando ci sono le luci di Natale a Locorotondo?", "Il Comune di Locorotondo ha indicato le iniziative di Natale dal 22 novembre 2026 al 6 gennaio 2027, quindi fino all'Epifania."),
    ("Quando inizia il Carnevale di Putignano 2027?", "Il 26 dicembre 2026 con le Propaggini. Le sfilate dei carri partono il 31 gennaio 2027 e il Carnevale finisce il Martedì grasso, che nel 2027 cade il 9 febbraio."),
    ("Dove dormire per gli eventi d'inverno in Valle d'Itria?", "Nella campagna di Martina Franca, per esempio a Trullo Rosy: un trullo intero con tre camere, camino e parcheggio, fino a 6 ospiti, a circa 6 km da Martina Franca e 12 da Locorotondo in linea d'aria."),
]
FAQ_EN = [
    ("What events are there in the Itria Valley at New Year?", "For New Year 2026 there were free square parties in Martina Franca (Piazza XX Settembre), Alberobello (Largo Martellotta), Cisternino (Piazza Vittorio Emanuele) and Ostuni (Piazza della Libertà), and on 1 January a free concert in Piazza XX Settembre, Martina Franca. The New Year 2027 programme has not been announced yet."),
    ("Until when are the Christmas lights on in Locorotondo?", "The Comune di Locorotondo has planned its Christmas events from 22 November 2026 to 6 January 2027, so until Epiphany."),
    ("When does the 2027 Putignano Carnival start?", "On 26 December 2026 with the Propaggini. The float parades start on 31 January 2027 and the Carnival ends on Shrove Tuesday, which in 2027 falls on 9 February."),
    ("Where to stay for winter events in the Itria Valley?", "In the countryside of Martina Franca, for example at Trullo Rosy: an entire trullo with three bedrooms, a fireplace and parking, for up to 6 guests, about 6 km from Martina Franca and 12 from Locorotondo as the crow flies."),
]


def faq_html(faq):
    return "\n".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)


EVENTI = {
    "key": "eventi-valle-ditria-inverno",
    "date": "2026-11-14",
    "modified": "2026-11-14",
    "hero": "luoghi/martina-franca",
    "paths": {"it": "/guide/eventi-in-valle-ditria/", "en": "/en/guides/itria-valley-events/"},
    "sources": SRC,
    "it": dict(
        title="Eventi in Valle d'Itria: inverno 2026-27 e Capodanno",
        desc="Eventi in Valle d'Itria nell'inverno 2026-27: luci di Natale, Capodanno in piazza, Epifania e Carnevale di Putignano, con date ufficiali e da confermare.",
        h1="Eventi in Valle d'Itria: Natale, Capodanno ed Epifania 2026-27",
        answer="Nell'inverno 2026-27 la Valle d'Itria ha tre momenti forti: le luci di Natale (a Locorotondo dal 22 novembre 2026 al 6 gennaio 2027, secondo il Comune), il Capodanno in piazza a Martina Franca, Alberobello, Cisternino e Ostuni, e l'Epifania. Dal 26 dicembre parte anche il Carnevale di Putignano. Le date 2026-27 non ancora annunciate sono segnate come da confermare.",
        body="""
<h2>Quali sono le date già certe dell'inverno 2026-27?</h2>
<p>Ad oggi (14 novembre 2026) i Comuni della Valle d'Itria hanno pubblicato poche date ufficiali per le feste. Qui sotto trovi quelle certe, con la fonte, e quelle da confermare con l'edizione precedente come riferimento. Aggiorniamo la pagina appena escono i programmi.</p>
<table class="facts">
<thead><tr><th scope="col">Quando</th><th scope="col">Evento</th><th scope="col">Dove</th><th scope="col">Stato</th></tr></thead>
<tbody>
<tr><th scope="row">22 novembre 2026 – 6 gennaio 2027</th><td>Natale a Locorotondo, luci a tema Pinocchio</td><td>Locorotondo, centro storico</td><td>periodo indicato dal Comune</td></tr>
<tr><th scope="row">26 dicembre 2026</th><td>Propaggini, apertura del Carnevale di Putignano</td><td>Putignano</td><td>confermato dal sito ufficiale</td></tr>
<tr><th scope="row">31 dicembre 2026</th><td>Capodanno in piazza</td><td>Martina Franca, Alberobello, Cisternino, Ostuni</td><td>da confermare (nel 2025 c'era in tutti e quattro)</td></tr>
<tr><th scope="row">1° gennaio 2027</th><td>Concerto di Capodanno</td><td>Martina Franca, piazza XX Settembre</td><td>da confermare (nel 2026 alle 18, gratuito)</td></tr>
<tr><th scope="row">6 gennaio 2027</th><td>Epifania, ultimo giorno delle feste</td><td>Locorotondo e paesi vicini</td><td>fine del periodo indicato a Locorotondo</td></tr>
<tr><th scope="row">dal 31 gennaio 2027</th><td>Sfilate dei carri del Carnevale</td><td>Putignano</td><td>annunciate dal sito ufficiale</td></tr>
</tbody>
</table>
{{img:panorama-valle-itria|Panorama della Valle d'Itria}}

<h2>Cosa succede a Locorotondo da Natale all'Epifania?</h2>
<p>Il Comune di Locorotondo ha indicato le iniziative di Natale <strong>dal 22 novembre 2026 al 6 gennaio 2027</strong>, con le luci a tema Pinocchio. Nel 2025 i mercatini sono rimasti aperti fino al 6 gennaio 2026. Accensione, orari e percorso delle luminarie sono nella nostra guida <a href="/guide/natale-a-locorotondo/">Natale a Locorotondo</a>; cosa vedere nel centro storico di giorno è nella guida <a href="/guide/cosa-vedere-a-locorotondo/">cosa vedere a Locorotondo</a>.</p>
{{img:locorotondo/vicolo-sera|Un vicolo del centro storico di Locorotondo la sera}}

<h2>Dove si festeggia il Capodanno in Valle d'Itria?</h2>
<p>Per il Capodanno 2027 i Comuni non hanno ancora annunciato il programma. Nel Capodanno 2026 (31 dicembre 2025) queste sono state le feste in piazza:</p>
<ul>
<li><strong>Martina Franca:</strong> piazza XX Settembre, dalle 22:30.</li>
<li><strong>Alberobello:</strong> largo Martellotta, dalle 22, con lo "Sciamn Fest".</li>
<li><strong>Cisternino:</strong> piazza Vittorio Emanuele, dalle 22:30, ingresso libero, con i Folkabbestia dal vivo e un dj set.</li>
<li><strong>Ostuni:</strong> piazza della Libertà, dalle 21, con il concerto dei Terraross e un dj set.</li>
</ul>
<p>Il 1° gennaio 2026, alle 18, piazza XX Settembre a Martina Franca ha ospitato il <strong>Concerto di Capodanno</strong> della Fondazione Paolo Grassi con l'Orchestra ICO Magna Grecia, gratuito: valzer e polke degli Strauss e arie d'opera. Per il 1° gennaio 2027 non c'è ancora un annuncio.</p>
{{img:luoghi/ostuni|La città bianca di Ostuni}}

<h2>Quali eventi ci sono a Martina Franca in inverno?</h2>
<p>Martina Franca, il paese di Trullo Rosy, concentra gli eventi d'inverno nel centro storico barocco: a Natale il Villaggio di Babbo Natale e, nel 2025, il giardino di luci in villa comunale dal 13 dicembre; a Capodanno la festa e il concerto in piazza XX Settembre. Le date 2026-27 sono da confermare. Il resto dei paesi, con le distanze dal trullo, è nella guida <a href="/guide/cosa-vedere-in-valle-ditria/">cosa vedere in Valle d'Itria</a>.</p>

<h2>Cosa fare all'Epifania?</h2>
<p>Il 6 gennaio è l'ultimo giorno delle feste: nel 2025-26 quel giorno erano ancora aperti i mercatini di Locorotondo e il Villaggio di Natale tra i trulli di Alberobello, e a Cisternino si è tenuto il presepe vivente nel centro storico (anche il 28 dicembre e il 4 gennaio). Le date di ogni paese sono nella guida <a href="/guide/mercatini-di-natale-in-puglia/">mercatini di Natale in Puglia</a>.</p>
{{img:luoghi/alberobello|I trulli di Alberobello}}

<h2>Quando inizia il Carnevale di Putignano 2027?</h2>
<p>Il Carnevale di Putignano, a circa 30 km in linea d'aria dal trullo, si apre il <strong>26 dicembre 2026 con le Propaggini</strong>. Secondo il sito ufficiale, le quattro sfilate dei carri di cartapesta della 633ª edizione partono il <strong>31 gennaio 2027</strong>; il Carnevale finisce il Martedì grasso, che nel 2027 cade il 9 febbraio. Il calendario di ogni sfilata è sul sito ufficiale.</p>

<h2>Come organizzare un soggiorno d'inverno?</h2>
<ul>
<li><strong>Quando:</strong> tra Natale e l'Epifania è aperto quasi tutto; il 31 dicembre e il 6 gennaio sono i giorni più affollati.</li>
<li><strong>Come muoversi:</strong> i paesi sono vicini ma collegati male dai mezzi pubblici, e la sera dopo una festa in piazza l'auto è quasi indispensabile.</li>
<li><strong>Abbigliamento:</strong> la sera in collina fa freddo, e i centri storici sono in pietra.</li>
<li><strong>Dove dormire:</strong> un trullo in campagna come <a href="/il-trullo/">Trullo Rosy</a>, con il camino, è a circa 6 km da Martina Franca e 12 da Locorotondo. Altri luoghi sono nella pagina <a href="/dintorni/">Dintorni</a>, e tutte le informazioni per prenotare nella pagina del nostro <a href="/">trullo in affitto a Martina Franca</a>.</li>
</ul>

<h2>Domande frequenti</h2>
""" + faq_html(FAQ_IT),
        faq=FAQ_IT,
        cta_h2="Passa le feste in un trullo con il camino",
        sources_h2="Fonti",
        photos_h2="Foto",
        updated="Aggiornato il 14 novembre 2026",
    ),
    "en": dict(
        title="Itria Valley events: winter 2026-27 and New Year",
        desc="Itria Valley events in winter 2026-27: Christmas lights, New Year's Eve in the squares, Epiphany and Putignano Carnival, with official and expected dates.",
        h1="Itria Valley events: Christmas, New Year and Epiphany 2026-27",
        answer="Winter 2026-27 in the Itria Valley has three highlights: the Christmas lights (in Locorotondo from 22 November 2026 to 6 January 2027, according to the town council), New Year's Eve in the squares of Martina Franca, Alberobello, Cisternino and Ostuni, and Epiphany. The Putignano Carnival opens on 26 December. Dates not yet announced are marked as to be confirmed.",
        body="""
<h2>Which winter 2026-27 dates are confirmed?</h2>
<p>As of 14 November 2026 the Itria Valley towns have published few official dates for the holidays. Below are the confirmed ones, with their source, and those still to be confirmed, with the previous edition as a guide. We update this page as soon as the programmes come out.</p>
<table class="facts">
<thead><tr><th scope="col">When</th><th scope="col">Event</th><th scope="col">Where</th><th scope="col">Status</th></tr></thead>
<tbody>
<tr><th scope="row">22 November 2026 – 6 January 2027</th><td>Christmas in Locorotondo, Pinocchio-themed lights</td><td>Locorotondo old town</td><td>period set by the council</td></tr>
<tr><th scope="row">26 December 2026</th><td>Propaggini, opening of the Putignano Carnival</td><td>Putignano</td><td>confirmed by the official site</td></tr>
<tr><th scope="row">31 December 2026</th><td>New Year's Eve in the square</td><td>Martina Franca, Alberobello, Cisternino, Ostuni</td><td>to be confirmed (all four held one in 2025)</td></tr>
<tr><th scope="row">1 January 2027</th><td>New Year's concert</td><td>Martina Franca, Piazza XX Settembre</td><td>to be confirmed (6 pm and free in 2026)</td></tr>
<tr><th scope="row">6 January 2027</th><td>Epiphany, last day of the holidays</td><td>Locorotondo and nearby towns</td><td>end of the Locorotondo period</td></tr>
<tr><th scope="row">from 31 January 2027</th><td>Carnival float parades</td><td>Putignano</td><td>announced by the official site</td></tr>
</tbody>
</table>
{{img:panorama-valle-itria|View over the Itria Valley}}

<h2>What happens in Locorotondo from Christmas to Epiphany?</h2>
<p>The Comune di Locorotondo has planned its Christmas events <strong>from 22 November 2026 to 6 January 2027</strong>, with Pinocchio-themed lights. In 2025 the markets stayed open until 6 January 2026. Switch-on, times and the route of the lights are in our guide <a href="/en/guides/christmas-in-locorotondo/">Christmas in Locorotondo</a>; what to see in the old town by day is in <a href="/en/guides/what-to-see-in-locorotondo/">what to see in Locorotondo</a>.</p>
{{img:locorotondo/vicolo-sera|A lane in Locorotondo's old town in the evening}}

<h2>Where to celebrate New Year's Eve in the Itria Valley?</h2>
<p>The towns have not announced their New Year 2027 programmes yet. For New Year 2026 (31 December 2025) these were the square parties:</p>
<ul>
<li><strong>Martina Franca:</strong> Piazza XX Settembre, from 10:30 pm.</li>
<li><strong>Alberobello:</strong> Largo Martellotta, from 10 pm, with the "Sciamn Fest".</li>
<li><strong>Cisternino:</strong> Piazza Vittorio Emanuele, from 10:30 pm, free entry, with Folkabbestia live and a DJ set.</li>
<li><strong>Ostuni:</strong> Piazza della Libertà, from 9 pm, with a Terraross concert and a DJ set.</li>
</ul>
<p>On 1 January 2026 at 6 pm, Piazza XX Settembre in Martina Franca hosted the free <strong>New Year's Concert</strong> of the Fondazione Paolo Grassi with the ICO Magna Grecia Orchestra: Strauss waltzes and polkas and opera arias. Nothing has been announced yet for 1 January 2027.</p>
{{img:luoghi/ostuni|Ostuni, the white town}}

<h2>What events are there in Martina Franca in winter?</h2>
<p>Martina Franca, Trullo Rosy's home town, holds its winter events in the baroque old town: at Christmas a Santa's village and, in 2025, a garden of lights in the public garden from 13 December; at New Year the party and the concert in Piazza XX Settembre. The 2026-27 dates are to be confirmed. The other towns, with distances from the trullo, are in our guide <a href="/en/guides/what-to-see-in-the-itria-valley/">what to see in the Itria Valley</a>.</p>

<h2>What to do at Epiphany?</h2>
<p>6 January is the last day of the holidays: in 2025-26 the Locorotondo markets and Alberobello's Christmas village among the trulli were still open that day, and Cisternino held its living nativity in the old town (also on 28 December and 4 January). Town-by-town dates are in our guide <a href="/en/guides/christmas-markets-in-puglia/">Christmas markets in Puglia</a>.</p>
{{img:luoghi/alberobello|The trulli of Alberobello}}

<h2>When does the 2027 Putignano Carnival start?</h2>
<p>The Putignano Carnival, about 30 km from the trullo as the crow flies, opens on <strong>26 December 2026 with the Propaggini</strong>. According to the official site, the four papier-mâché float parades of the 633rd edition start on <strong>31 January 2027</strong>; the Carnival ends on Shrove Tuesday, which in 2027 falls on 9 February. The schedule of each parade is on the official site.</p>

<h2>How to plan a winter stay?</h2>
<ul>
<li><strong>When:</strong> almost everything is open between Christmas and Epiphany; 31 December and 6 January are the busiest days.</li>
<li><strong>Getting around:</strong> the towns are close but poorly linked by public transport, and after a late party in the square a car is almost essential.</li>
<li><strong>What to wear:</strong> evenings on the hills are cold and old town streets are stone.</li>
<li><strong>Where to stay:</strong> a countryside trullo with a fireplace such as <a href="/en/the-trullo/">Trullo Rosy</a> is about 6 km from Martina Franca and 12 from Locorotondo. More places are on our <a href="/en/surroundings/">Surroundings</a> page, and everything you need to book is on the page of our <a href="/en/">trullo for rent in Martina Franca</a>.</li>
</ul>

<h2>Frequently asked questions</h2>
""" + faq_html(FAQ_EN),
        faq=FAQ_EN,
        cta_h2="Spend the holidays in a trullo with a fireplace",
        sources_h2="Sources",
        photos_h2="Photos",
        updated="Updated 14 November 2026",
    ),
}

GUIDES = [EVENTI]
