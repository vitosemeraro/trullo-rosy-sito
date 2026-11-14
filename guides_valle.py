"""Guide sulla Valle d'Itria, sul mare e sul dormire in un trullo (13/11/2026).

Stesso formato di guides.py. Le distanze sono in linea d'aria dal trullo
(40.6526, 17.3594), arrotondate: in auto la strada è sempre un po' più lunga.
"""

UNESCO_TRULLI = ("UNESCO, \"The Trulli of Alberobello\" (patrimonio mondiale dal 1996)", "https://whc.unesco.org/en/list/787/")
UNESCO_MATERA = ("UNESCO, \"The Sassi and the Park of the Rupestrian Churches of Matera\" (patrimonio mondiale dal 1993)", "https://whc.unesco.org/en/list/670/")
TORRE_GUACETO = ("Riserva Naturale dello Stato e Area Marina Protetta di Torre Guaceto", "https://www.riservaditorreguaceto.it/")


def faq_html(faq):
    return "\n".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)


# ---------------------------------------------------------------- Valle d'Itria
VI_FAQ_IT = [
    ("Quanti giorni servono per vedere la Valle d'Itria?", "Con tre o quattro giorni si vedono con calma Martina Franca, Locorotondo, Cisternino, Alberobello e Ostuni. Con una settimana si aggiungono il mare e Matera."),
    ("Qual è il paese più bello della Valle d'Itria?", "Dipende da cosa cerchi: Alberobello per i trulli patrimonio UNESCO, Locorotondo per il centro storico bianco e circolare, Martina Franca per il barocco, Cisternino per le bombette e i vicoli."),
    ("Serve la macchina?", "Sì, quasi sempre: i paesi sono vicini tra loro ma collegati male dai mezzi pubblici, e i trulli in campagna si raggiungono solo in auto."),
    ("Dove dormire per visitare la Valle d'Itria?", "In mezzo ai paesi, per esempio nella campagna di Martina Franca: da Trullo Rosy Martina Franca è a circa 6 km in linea d'aria, Locorotondo e Cisternino a circa 12, Alberobello a circa 18."),
]
VI_FAQ_EN = [
    ("How many days do you need for the Itria Valley?", "Three or four days are enough to see Martina Franca, Locorotondo, Cisternino, Alberobello and Ostuni at a relaxed pace. With a week you can add the sea and Matera."),
    ("Which is the most beautiful town in the Itria Valley?", "It depends on what you like: Alberobello for its UNESCO-listed trulli, Locorotondo for its round white old town, Martina Franca for its baroque, Cisternino for bombette and narrow lanes."),
    ("Do you need a car?", "Almost always: the towns are close to each other but poorly linked by public transport, and countryside trulli can only be reached by car."),
    ("Where to stay to explore the Itria Valley?", "In the middle of the towns, for example in the countryside of Martina Franca: from Trullo Rosy, Martina Franca is about 6 km as the crow flies, Locorotondo and Cisternino about 12, Alberobello about 18."),
]

VALLE = {
    "key": "valle-ditria",
    "date": "2026-11-13",
    "modified": "2026-11-13",
    "hero": "luoghi/valle-ditria",
    "paths": {"it": "/guide/cosa-vedere-in-valle-ditria/", "en": "/en/guides/what-to-see-in-the-itria-valley/"},
    "sources": [UNESCO_TRULLI, UNESCO_MATERA],
    "it": dict(
        title="Cosa vedere in Valle d'Itria da Martina Franca",
        desc="Cosa vedere in Valle d'Itria partendo da Martina Franca: Locorotondo, Cisternino, Alberobello e Ostuni, distanze dal trullo e un itinerario di 4 giorni.",
        h1="Cosa vedere in Valle d'Itria partendo da Martina Franca",
        answer="La Valle d'Itria è la campagna dei trulli tra Martina Franca, Locorotondo, Cisternino e Alberobello, con Ostuni poco più in là. I paesi distano tra loro pochi chilometri: dormendo nella campagna di Martina Franca se ne vedono uno o due al giorno, e in tre o quattro giorni si gira tutta la valle.",
        body="""
<h2>Quali sono i paesi da vedere in Valle d'Itria?</h2>
<p>I paesi principali sono cinque, tutti a meno di mezz'ora di strada l'uno dall'altro. Le distanze qui sotto sono in linea d'aria da Trullo Rosy: in auto la strada è un po' più lunga.</p>
<table class="facts">
<thead><tr><th scope="col">Paese</th><th scope="col">Da Trullo Rosy</th><th scope="col">Da non perdere</th></tr></thead>
<tbody>
<tr><th scope="row">Martina Franca</th><td>circa 6 km</td><td>centro storico barocco, Palazzo Ducale, Basilica di San Martino</td></tr>
<tr><th scope="row">Cisternino</th><td>circa 11 km</td><td>vicoli bianchi e le bombette nei fornelli pronti</td></tr>
<tr><th scope="row">Locorotondo</th><td>circa 12 km</td><td>centro storico circolare e il belvedere sulla campagna</td></tr>
<tr><th scope="row">Alberobello</th><td>circa 18 km</td><td>rioni Monti e Aia Piccola, patrimonio UNESCO dal 1996</td></tr>
<tr><th scope="row">Ostuni</th><td>circa 20 km</td><td>la "città bianca" sulla collina, con vista sul mare</td></tr>
</tbody>
</table>
{{img:luoghi/martina-franca|Il centro storico di Martina Franca}}

<h2>Cosa vedere a Martina Franca?</h2>
<p>È il paese più vicino al trullo e il più grande della valle. Il centro storico è barocco: si entra dall'arco di Sant'Antonio, si passa davanti al Palazzo Ducale e si arriva alla Basilica di San Martino, tra vicoli bianchi e balconi in ferro battuto. In estate ospita il Festival della Valle d'Itria, dedicato all'opera.</p>

<h2>Perché Alberobello è patrimonio UNESCO?</h2>
<p>Per i suoi trulli: nei rioni Monti e Aia Piccola ce ne sono centinaia, costruiti in pietra a secco con il tetto a cono. L'UNESCO li ha inseriti nel patrimonio mondiale nel 1996. Il rione Monti è il più fotografato e il più pieno di negozi; Aia Piccola è più tranquillo e abitato.</p>
{{img:luoghi/alberobello|I trulli del rione Monti ad Alberobello}}

<h2>Locorotondo e Cisternino: cosa hanno di speciale?</h2>
<p><strong>Locorotondo</strong> deve il nome alla forma del centro storico, un cerchio di case bianche con i tetti a punta (le "cummerse"). Dalla villa comunale si vede tutta la campagna dei trulli. Cosa vedere nel centro è nella guida <a href="/guide/cosa-vedere-a-locorotondo/">cosa vedere a Locorotondo</a>; a Natale il paese si riempie di luminarie: ne parliamo nella <a href="/guide/natale-a-locorotondo/">guida al Natale a Locorotondo</a>.</p>
<p><strong>Cisternino</strong> è il paese delle bombette: involtini di carne cotti nei "fornelli pronti", macellerie dove scegli la carne e te la cuociono sul momento. Il centro storico è un intreccio di scale e vicoli imbiancati.</p>

<h2>Vale la pena arrivare fino a Ostuni?</h2>
<p>Sì. Ostuni è appena fuori dalla valle, su una collina tra gli ulivi, e dall'alto si vede il mare Adriatico. Si può unire a una giornata al mare sulla costa vicina: trovi le spiagge nella <a href="/guide/spiagge-vicino-martina-franca/">guida alle spiagge vicino a Martina Franca</a>.</p>
{{img:luoghi/ostuni|Ostuni, la città bianca}}

<h2>Un itinerario di 4 giorni partendo dal trullo</h2>
<ul>
<li><strong>Giorno 1:</strong> Martina Franca al mattino, Locorotondo al tramonto.</li>
<li><strong>Giorno 2:</strong> Alberobello presto, prima della folla, poi pranzo con le bombette a Cisternino.</li>
<li><strong>Giorno 3:</strong> Ostuni e il mare Adriatico.</li>
<li><strong>Giorno 4:</strong> Matera, i Sassi patrimonio UNESCO dal 1993 (circa 64 km in linea d'aria).</li>
</ul>
<p>La sera si torna in campagna: a <a href="/il-trullo/">Trullo Rosy</a> c'è il silenzio degli ulivi e, d'inverno, il camino. Altri luoghi da visitare sono nella pagina <a href="/dintorni/">dintorni</a>. Tutte le informazioni per prenotare sono nella pagina del nostro <a href="/">trullo in affitto a Martina Franca</a>.</p>

<h2>Domande frequenti</h2>
""" + faq_html(VI_FAQ_IT),
        faq=VI_FAQ_IT,
        cta_h2="Dormi in un trullo nel cuore della Valle d'Itria",
        sources_h2="Fonti",
        photos_h2="Foto",
        updated="Aggiornato il 13 novembre 2026",
    ),
    "en": dict(
        title="What to see in the Itria Valley from Martina Franca",
        desc="What to see in the Itria Valley from Martina Franca: Locorotondo, Cisternino, Alberobello and Ostuni, distances from the trullo and a 4-day itinerary.",
        h1="What to see in the Itria Valley from Martina Franca",
        answer="The Itria Valley is the trulli countryside between Martina Franca, Locorotondo, Cisternino and Alberobello, with Ostuni just beyond. The towns are only a few kilometres apart: staying in the countryside of Martina Franca you can see one or two a day, and the whole valley in three or four days.",
        body="""
<h2>Which towns should you see in the Itria Valley?</h2>
<p>There are five main towns, all within half an hour's drive of each other. The distances below are as the crow flies from Trullo Rosy: by car the road is a little longer.</p>
<table class="facts">
<thead><tr><th scope="col">Town</th><th scope="col">From Trullo Rosy</th><th scope="col">Don't miss</th></tr></thead>
<tbody>
<tr><th scope="row">Martina Franca</th><td>about 6 km</td><td>baroque old town, Palazzo Ducale, Basilica of San Martino</td></tr>
<tr><th scope="row">Cisternino</th><td>about 11 km</td><td>white lanes and bombette from the "fornelli pronti"</td></tr>
<tr><th scope="row">Locorotondo</th><td>about 12 km</td><td>round old town and the viewpoint over the countryside</td></tr>
<tr><th scope="row">Alberobello</th><td>about 18 km</td><td>Rione Monti and Aia Piccola, UNESCO World Heritage since 1996</td></tr>
<tr><th scope="row">Ostuni</th><td>about 20 km</td><td>the "white city" on its hill, with views of the sea</td></tr>
</tbody>
</table>
{{img:luoghi/martina-franca|The old town of Martina Franca}}

<h2>What to see in Martina Franca?</h2>
<p>It is the town closest to the trullo and the largest in the valley. Its old town is baroque: you enter through the Arch of Sant'Antonio, pass the Palazzo Ducale and reach the Basilica of San Martino, among white lanes and wrought-iron balconies. In summer it hosts the Festival della Valle d'Itria, an opera festival.</p>

<h2>Why is Alberobello a UNESCO site?</h2>
<p>Because of its trulli: the Rione Monti and Aia Piccola districts have hundreds of them, built in dry stone with conical roofs. UNESCO added them to the World Heritage List in 1996. Rione Monti is the most photographed and has the most shops; Aia Piccola is quieter and lived-in.</p>
{{img:luoghi/alberobello|The trulli of Rione Monti in Alberobello}}

<h2>Locorotondo and Cisternino: what makes them special?</h2>
<p><strong>Locorotondo</strong> takes its name from the round shape of its old town, a circle of white houses with pointed roofs (the "cummerse"). From the public garden you can see the whole trulli countryside. What to see in the old town is in our guide <a href="/en/guides/what-to-see-in-locorotondo/">what to see in Locorotondo</a>; at Christmas the town fills with lights: see our <a href="/en/guides/christmas-in-locorotondo/">guide to Christmas in Locorotondo</a>.</p>
<p><strong>Cisternino</strong> is the town of bombette: small meat rolls cooked in the "fornelli pronti", butcher's shops where you pick the meat and they grill it for you on the spot. The old town is a tangle of whitewashed steps and lanes.</p>

<h2>Is Ostuni worth the trip?</h2>
<p>Yes. Ostuni is just outside the valley, on a hill among olive groves, and from the top you can see the Adriatic Sea. You can combine it with a day at the beach on the nearby coast: see our <a href="/en/guides/beaches-near-martina-franca/">guide to the beaches near Martina Franca</a>.</p>
{{img:luoghi/ostuni|Ostuni, the white city}}

<h2>A 4-day itinerary from the trullo</h2>
<ul>
<li><strong>Day 1:</strong> Martina Franca in the morning, Locorotondo at sunset.</li>
<li><strong>Day 2:</strong> Alberobello early, before the crowds, then lunch with bombette in Cisternino.</li>
<li><strong>Day 3:</strong> Ostuni and the Adriatic Sea.</li>
<li><strong>Day 4:</strong> Matera, whose Sassi are UNESCO World Heritage since 1993 (about 64 km as the crow flies).</li>
</ul>
<p>In the evening you come back to the countryside: at <a href="/en/the-trullo/">Trullo Rosy</a> there is the silence of the olive trees and, in winter, the fireplace. More places to visit are on the <a href="/en/surroundings/">surroundings</a> page. Everything you need to book is on the page of our <a href="/en/">trullo for rent in Martina Franca</a>.</p>

<h2>Frequently asked questions</h2>
""" + faq_html(VI_FAQ_EN),
        faq=VI_FAQ_EN,
        cta_h2="Stay in a trullo in the heart of the Itria Valley",
        sources_h2="Sources",
        photos_h2="Photos",
        updated="Updated 13 November 2026",
    ),
}

# ---------------------------------------------------------------- Spiagge
SP_FAQ_IT = [
    ("Qual è il mare più vicino a Martina Franca?", "In linea d'aria il mare più vicino è lo Ionio, verso Taranto (circa 23 km dal trullo), ma anche la costa adriatica di Torre Canne e Savelletri è a circa 23-25 km. Si raggiungono entrambi in giornata."),
    ("Meglio l'Adriatico o lo Ionio?", "Lo Ionio ha spiagge di sabbia lunghe e acqua bassa, comode con i bambini. L'Adriatico ha calette, scogli e paesi sul mare come Polignano e Monopoli."),
    ("Dove fare il bagno in acqua limpida?", "A Torre Guaceto, riserva naturale e area marina protetta sulla costa adriatica, con dune e macchia mediterranea (circa 38 km dal trullo)."),
    ("Si può andare al mare in giornata dormendo in un trullo?", "Sì: da Trullo Rosy le spiagge di entrambi i mari sono tra circa 23 e 45 km in linea d'aria. Al ritorno, la sera in campagna è più fresca che sulla costa."),
]
SP_FAQ_EN = [
    ("Which is the nearest sea to Martina Franca?", "As the crow flies the nearest sea is the Ionian, towards Taranto (about 23 km from the trullo), but the Adriatic coast at Torre Canne and Savelletri is also about 23-25 km away. You can reach both on a day trip."),
    ("Adriatic or Ionian?", "The Ionian has long sandy beaches and shallow water, easy with children. The Adriatic has coves, rocks and seaside towns such as Polignano and Monopoli."),
    ("Where to swim in clear water?", "At Torre Guaceto, a nature reserve and marine protected area on the Adriatic coast, with dunes and Mediterranean scrub (about 38 km from the trullo)."),
    ("Can you go to the beach for the day from a trullo?", "Yes: from Trullo Rosy the beaches of both seas are between about 23 and 45 km as the crow flies. When you come back, evenings in the countryside are cooler than on the coast."),
]

SPIAGGE = {
    "key": "spiagge",
    "date": "2026-11-13",
    "modified": "2026-11-13",
    "hero": "luoghi/polignano",
    "paths": {"it": "/guide/spiagge-vicino-martina-franca/", "en": "/en/guides/beaches-near-martina-franca/"},
    "sources": [TORRE_GUACETO],
    "it": dict(
        title="Spiagge vicino a Martina Franca: Adriatico e Ionio",
        desc="Le spiagge vicino a Martina Franca tra Adriatico e Ionio: Torre Canne, Monopoli, Polignano, Torre Guaceto e lo Ionio, con le distanze dal trullo.",
        h1="Le spiagge vicino a Martina Franca, tra Adriatico e Ionio",
        answer="Martina Franca è in collina, a metà strada tra due mari. Verso nord c'è l'Adriatico, con Torre Canne, Savelletri, Monopoli, Polignano e la riserva di Torre Guaceto; verso sud lo Ionio, con le lunghe spiagge di sabbia della costa di Taranto. Dal trullo entrambi si raggiungono in giornata.",
        body="""
<h2>Quali spiagge si raggiungono dal trullo?</h2>
<p>Le distanze sono in linea d'aria da Trullo Rosy: in auto la strada è un po' più lunga.</p>
<table class="facts">
<thead><tr><th scope="col">Spiaggia</th><th scope="col">Mare</th><th scope="col">Da Trullo Rosy</th><th scope="col">Com'è</th></tr></thead>
<tbody>
<tr><th scope="row">Torre Canne (Fasano)</th><td>Adriatico</td><td>circa 23 km</td><td>sabbia, lidi attrezzati e spiaggia libera</td></tr>
<tr><th scope="row">Savelletri (Fasano)</th><td>Adriatico</td><td>circa 25 km</td><td>scogli bassi e piccole calette</td></tr>
<tr><th scope="row">Monopoli</th><td>Adriatico</td><td>circa 34 km</td><td>calette tra gli scogli lungo la costa a sud del paese</td></tr>
<tr><th scope="row">Torre Guaceto</th><td>Adriatico</td><td>circa 38 km</td><td>riserva naturale, dune e acqua limpida</td></tr>
<tr><th scope="row">Polignano a Mare</th><td>Adriatico</td><td>circa 40 km</td><td>Lama Monachile, piccola spiaggia di ciottoli tra le falesie</td></tr>
<tr><th scope="row">Marina di Pulsano</th><td>Ionio</td><td>circa 32 km</td><td>sabbia e acqua bassa</td></tr>
<tr><th scope="row">Campomarino di Maruggio</th><td>Ionio</td><td>circa 43 km</td><td>sabbia e dune</td></tr>
<tr><th scope="row">Castellaneta Marina</th><td>Ionio</td><td>circa 44 km</td><td>lunghe spiagge di sabbia con la pineta alle spalle</td></tr>
</tbody>
</table>

<h2>Quali sono le spiagge più belle sull'Adriatico?</h2>
<p>La costa adriatica vicina è fatta di calette e scogli, con alcune spiagge di sabbia. <strong>Polignano a Mare</strong> è il paese sulle falesie, con la spiaggia di Lama Monachile incastrata tra le rocce: bellissima, ma in estate molto affollata. <strong>Monopoli</strong> ha un porto antico e, a sud del paese, tante piccole calette. A <strong>Torre Canne</strong> la spiaggia è di sabbia e ci sono anche lidi attrezzati.</p>
{{img:luoghi/monopoli|Il porto antico di Monopoli}}

<h2>Dove fare il bagno in una riserva naturale?</h2>
<p><strong>Torre Guaceto</strong>, tra Carovigno e Brindisi, è una riserva naturale dello Stato e un'area marina protetta: dune, macchia mediterranea, la torre di avvistamento e acqua molto limpida. È uno dei tratti di costa più belli della zona. Prima di andare controlla sul sito della riserva come si accede in estate.</p>
{{img:luoghi/torre-guaceto|La costa di Torre Guaceto}}

<h2>Com'è il mare Ionio vicino a Taranto?</h2>
<p>Sullo Ionio le spiagge sono lunghe, di sabbia chiara, con l'acqua che resta bassa per molti metri: comode con i bambini. Verso est ci sono <strong>Marina di Pulsano</strong> e <strong>Campomarino di Maruggio</strong>, con le dune; verso ovest <strong>Castellaneta Marina</strong>, con la pineta alle spalle della spiaggia.</p>
{{img:luoghi/lizzano|Spiaggia di sabbia sulla costa ionica}}

<h2>Consigli per una giornata al mare</h2>
<ul>
<li><strong>Parti presto:</strong> in luglio e agosto i parcheggi vicino alle spiagge più note si riempiono in mattinata.</li>
<li><strong>Scegli il mare in base al vento:</strong> quando una costa è mossa, spesso l'altra è calma.</li>
<li><strong>Unisci mare e paese:</strong> Ostuni con la costa adriatica, Taranto con lo Ionio. Altri luoghi sono nella pagina <a href="/dintorni/">dintorni</a> e nella <a href="/guide/cosa-vedere-in-valle-ditria/">guida alla Valle d'Itria</a>.</li>
<li><strong>La sera:</strong> in collina fa più fresco che sulla costa, e a <a href="/il-trullo/">Trullo Rosy</a> si cena sotto il pergolato. Tutte le informazioni per prenotare sono nella pagina del nostro <a href="/">trullo in affitto a Martina Franca</a>.</li>
</ul>

<h2>Domande frequenti</h2>
""" + faq_html(SP_FAQ_IT),
        faq=SP_FAQ_IT,
        cta_h2="Dormi in un trullo tra due mari",
        sources_h2="Fonti",
        photos_h2="Foto",
        updated="Aggiornato il 13 novembre 2026",
    ),
    "en": dict(
        title="Beaches near Martina Franca: Adriatic and Ionian",
        desc="Beaches near Martina Franca on the Adriatic and Ionian seas: Torre Canne, Monopoli, Polignano, Torre Guaceto and the Taranto coast, with distances.",
        h1="Beaches near Martina Franca, between the Adriatic and the Ionian",
        answer="Martina Franca sits on the hills halfway between two seas. To the north is the Adriatic, with Torre Canne, Savelletri, Monopoli, Polignano and the Torre Guaceto reserve; to the south the Ionian, with the long sandy beaches of the Taranto coast. From the trullo you can reach both on a day trip.",
        body="""
<h2>Which beaches can you reach from the trullo?</h2>
<p>Distances are as the crow flies from Trullo Rosy: by car the road is a little longer.</p>
<table class="facts">
<thead><tr><th scope="col">Beach</th><th scope="col">Sea</th><th scope="col">From Trullo Rosy</th><th scope="col">What it's like</th></tr></thead>
<tbody>
<tr><th scope="row">Torre Canne (Fasano)</th><td>Adriatic</td><td>about 23 km</td><td>sand, beach clubs and free beach</td></tr>
<tr><th scope="row">Savelletri (Fasano)</th><td>Adriatic</td><td>about 25 km</td><td>low rocks and small coves</td></tr>
<tr><th scope="row">Monopoli</th><td>Adriatic</td><td>about 34 km</td><td>rocky coves along the coast south of the town</td></tr>
<tr><th scope="row">Torre Guaceto</th><td>Adriatic</td><td>about 38 km</td><td>nature reserve, dunes and clear water</td></tr>
<tr><th scope="row">Polignano a Mare</th><td>Adriatic</td><td>about 40 km</td><td>Lama Monachile, a small pebble beach between cliffs</td></tr>
<tr><th scope="row">Marina di Pulsano</th><td>Ionian</td><td>about 32 km</td><td>sand and shallow water</td></tr>
<tr><th scope="row">Campomarino di Maruggio</th><td>Ionian</td><td>about 43 km</td><td>sand and dunes</td></tr>
<tr><th scope="row">Castellaneta Marina</th><td>Ionian</td><td>about 44 km</td><td>long sandy beaches backed by pine woods</td></tr>
</tbody>
</table>

<h2>Which are the best beaches on the Adriatic?</h2>
<p>The nearby Adriatic coast is mostly coves and rocks, with a few sandy beaches. <strong>Polignano a Mare</strong> is the town on the cliffs, with the Lama Monachile beach wedged between the rocks: beautiful, but very crowded in summer. <strong>Monopoli</strong> has an old harbour and many small coves south of the town. <strong>Torre Canne</strong> has a sandy beach with beach clubs.</p>
{{img:luoghi/monopoli|The old harbour of Monopoli}}

<h2>Where to swim in a nature reserve?</h2>
<p><strong>Torre Guaceto</strong>, between Carovigno and Brindisi, is a state nature reserve and marine protected area: dunes, Mediterranean scrub, the watchtower and very clear water. It is one of the most beautiful stretches of coast in the area. Before you go, check the reserve's website for summer access rules.</p>
{{img:luoghi/torre-guaceto|The coast at Torre Guaceto}}

<h2>What is the Ionian Sea like near Taranto?</h2>
<p>On the Ionian the beaches are long, with pale sand and water that stays shallow for many metres: easy with children. To the east are <strong>Marina di Pulsano</strong> and <strong>Campomarino di Maruggio</strong>, with dunes; to the west <strong>Castellaneta Marina</strong>, with pine woods behind the beach.</p>
{{img:luoghi/lizzano|A sandy beach on the Ionian coast}}

<h2>Tips for a day at the beach</h2>
<ul>
<li><strong>Leave early:</strong> in July and August the car parks near the best-known beaches fill up by mid-morning.</li>
<li><strong>Pick the sea by the wind:</strong> when one coast is rough, the other is often calm.</li>
<li><strong>Combine sea and town:</strong> Ostuni with the Adriatic, Taranto with the Ionian. More places are on the <a href="/en/surroundings/">surroundings</a> page and in the <a href="/en/guides/what-to-see-in-the-itria-valley/">Itria Valley guide</a>.</li>
<li><strong>In the evening:</strong> the hills are cooler than the coast, and at <a href="/en/the-trullo/">Trullo Rosy</a> you can have dinner under the pergola. Everything you need to book is on the page of our <a href="/en/">trullo for rent in Martina Franca</a>.</li>
</ul>

<h2>Frequently asked questions</h2>
""" + faq_html(SP_FAQ_EN),
        faq=SP_FAQ_EN,
        cta_h2="Stay in a trullo between two seas",
        sources_h2="Sources",
        photos_h2="Photos",
        updated="Updated 13 November 2026",
    ),
}

# ---------------------------------------------------------------- Dormire in un trullo
DT_FAQ_IT = [
    ("Fa caldo d'estate in un trullo?", "In genere no: i muri di pietra sono molto spessi e tengono fresco l'interno anche nelle giornate calde. D'inverno, al contrario, serve il riscaldamento: a Trullo Rosy ci sono il riscaldamento e il camino."),
    ("Un trullo è adatto a una famiglia?", "Dipende da quante camere ha. Trullo Rosy si affitta per intero: 85 m², tre camere, fino a 6 ospiti, con culla e seggiolone."),
    ("Nel trullo c'è il Wi-Fi?", "Molti trulli in affitto oggi lo hanno. A Trullo Rosy c'è il Wi-Fi veloce e uno spazio di lavoro dedicato."),
    ("Serve l'auto per dormire in un trullo?", "Quasi sempre sì, perché i trulli sono in campagna. Trullo Rosy ha il parcheggio gratuito dentro la proprietà."),
    ("Come si prenota Trullo Rosy?", "Su Airbnb o Booking.com, oppure scrivendo su WhatsApp al +39 329 06 14 613 per chiedere la disponibilità."),
]
DT_FAQ_EN = [
    ("Is a trullo hot in summer?", "Usually not: the stone walls are very thick and keep the inside cool even on hot days. In winter, on the other hand, you need heating: Trullo Rosy has heating and a fireplace."),
    ("Is a trullo suitable for a family?", "It depends on how many rooms it has. Trullo Rosy is rented as a whole: 85 m², three bedrooms, up to 6 guests, with a cot and a high chair."),
    ("Is there Wi-Fi in a trullo?", "Many trulli for rent have it today. Trullo Rosy has fast Wi-Fi and a dedicated workspace."),
    ("Do you need a car to stay in a trullo?", "Almost always, because trulli are in the countryside. Trullo Rosy has free parking inside the property."),
    ("How do you book Trullo Rosy?", "On Airbnb or Booking.com, or by sending a WhatsApp message to +39 329 06 14 613 to ask about availability."),
]

DORMIRE = {
    "key": "dormire-trullo",
    "date": "2026-11-13",
    "modified": "2026-11-13",
    "hero": "esterno-trulli",
    "paths": {"it": "/guide/dormire-in-un-trullo/", "en": "/en/guides/sleeping-in-a-trullo/"},
    "sources": [UNESCO_TRULLI],
    "it": dict(
        title="Dormire in un trullo in Puglia: domande e risposte",
        desc="Dormire in un trullo in Puglia: com'è fatto, se fa caldo o freddo, cosa controllare prima di prenotare e com'è Trullo Rosy, in campagna a Martina Franca.",
        h1="Dormire in un trullo in Puglia: domande e risposte",
        answer="Dormire in un trullo vuol dire passare la notte sotto un tetto di pietra a cono, con muri spessi che tengono fresco d'estate e il silenzio della campagna intorno. I trulli in affitto sono soprattutto in Valle d'Itria, tra Alberobello, Locorotondo e Martina Franca: prima di prenotare conviene controllare camere, riscaldamento e parcheggio.",
        body="""
<h2>Cos'è un trullo?</h2>
<p>Il trullo è la casa tradizionale in pietra della Murgia dei trulli e della Valle d'Itria. È costruito a secco, cioè senza malta, con pietra calcarea del posto, e ha il tetto a cono fatto di lastre di pietra sovrapposte, spesso con un pinnacolo in cima. Spesso più coni sono uniti tra loro: ogni cono copre una stanza. Ad Alberobello i rioni Monti e Aia Piccola, pieni di trulli, sono patrimonio UNESCO dal 1996.</p>
{{img:esterno-trulli|I coni di Trullo Rosy visti dal giardino}}

<h2>Com'è dormire in un trullo?</h2>
<p>Dentro, le stanze hanno pareti curve, volte in pietra e nicchie scavate nei muri. I muri sono molto spessi: d'estate l'interno resta fresco, d'inverno il calore del camino rimane a lungo. Le finestre sono piccole, quindi la luce è morbida e la notte è buia e silenziosa, soprattutto in campagna.</p>
{{img:camera-silent-nest|La camera Silent nest di Trullo Rosy, sotto le volte in pietra}}

<h2>Cosa controllare prima di prenotare un trullo?</h2>
<table class="facts">
<thead><tr><th scope="col">Da controllare</th><th scope="col">Perché conta</th><th scope="col">A Trullo Rosy</th></tr></thead>
<tbody>
<tr><th scope="row">Casa intera o camera</th><td>alcuni trulli si affittano a camere, con spazi in comune</td><td>casa intera, 85 m²</td></tr>
<tr><th scope="row">Camere e letti</th><td>i coni sono piccoli: non tutte le stanze hanno un letto matrimoniale</td><td>3 camere: 2 letti queen size e 1 letto singolo, fino a 6 ospiti</td></tr>
<tr><th scope="row">Riscaldamento</th><td>d'inverno la pietra è fredda</td><td>riscaldamento e camino</td></tr>
<tr><th scope="row">Cucina</th><td>in campagna i ristoranti sono in paese</td><td>cucina attrezzata, barbecue in giardino</td></tr>
<tr><th scope="row">Parcheggio</th><td>i trulli in campagna si raggiungono in auto</td><td>gratuito nella proprietà</td></tr>
<tr><th scope="row">Wi-Fi</th><td>per lavorare o organizzare le gite</td><td>Wi-Fi veloce e spazio di lavoro</td></tr>
<tr><th scope="row">Orari</th><td>per organizzare il viaggio</td><td>check-in dalle 15:00, check-out entro le 11:00</td></tr>
</tbody>
</table>

<h2>Meglio un trullo ad Alberobello o in campagna?</h2>
<p>Ad Alberobello dormi in mezzo ai trulli più famosi, ma di giorno le strade sono piene di visitatori. In campagna, tra Martina Franca, Locorotondo e Cisternino, hai più spazio, un giardino e il silenzio, e in auto raggiungi tutti i paesi della valle: le distanze sono nella <a href="/guide/cosa-vedere-in-valle-ditria/">guida alla Valle d'Itria</a>.</p>

<h2>Com'è Trullo Rosy?</h2>
<p><a href="/il-trullo/">Trullo Rosy</a> è un trullo tradizionale lungo la SP70, nelle campagne di Martina Franca, tra alberi da frutto e ulivi secolari. Ha tre camere (Silent nest, Still Bloom e l'Alcova), il salotto con il camino, la cucina e, fuori, un cortile in pietra con il pozzo, il pergolato con il tavolo da pranzo, la veranda e l'amaca tra gli ulivi. Le foto sono nella <a href="/galleria/">galleria</a>. Tutte le informazioni per prenotare sono nella pagina del nostro <a href="/">trullo in affitto a Martina Franca</a>.</p>
{{img:salotto-camino|Il salotto con il camino di Trullo Rosy}}

<h2>Quando conviene dormire in un trullo?</h2>
<p>In ogni stagione, per motivi diversi. In estate per il fresco della pietra e le giornate al mare (vedi le <a href="/guide/spiagge-vicino-martina-franca/">spiagge vicino a Martina Franca</a>); in primavera e autunno per girare i paesi senza folla; d'inverno per il camino e le luminarie di Natale, come quelle della <a href="/guide/natale-a-locorotondo/">vicina Locorotondo</a>.</p>

<h2>Domande frequenti</h2>
""" + faq_html(DT_FAQ_IT),
        faq=DT_FAQ_IT,
        cta_h2="Prova a dormire in un trullo",
        sources_h2="Fonti",
        photos_h2="Foto",
        updated="Aggiornato il 13 novembre 2026",
    ),
    "en": dict(
        title="Sleeping in a trullo in Puglia: questions and answers",
        desc="Sleeping in a trullo in Puglia: how it is built, whether it is hot or cold, what to check before booking and what Trullo Rosy is like, near Martina Franca.",
        h1="Sleeping in a trullo in Puglia: questions and answers",
        answer="Sleeping in a trullo means spending the night under a conical stone roof, with thick walls that keep it cool in summer and the silence of the countryside all around. Trulli for rent are mostly in the Itria Valley, between Alberobello, Locorotondo and Martina Franca: before booking, check the rooms, heating and parking.",
        body="""
<h2>What is a trullo?</h2>
<p>The trullo is the traditional stone house of the Murgia dei trulli and the Itria Valley. It is built dry, without mortar, from local limestone, and has a conical roof of overlapping stone slabs, often topped with a pinnacle. Several cones are often joined together: each cone covers one room. In Alberobello the Rione Monti and Aia Piccola districts, full of trulli, are UNESCO World Heritage since 1996.</p>
{{img:esterno-trulli|The cones of Trullo Rosy seen from the garden}}

<h2>What is it like to sleep in a trullo?</h2>
<p>Inside, the rooms have curved walls, stone vaults and niches set into the walls. The walls are very thick: in summer the inside stays cool, in winter the warmth of the fire lasts a long time. The windows are small, so the light is soft and the night is dark and quiet, especially in the countryside.</p>
{{img:camera-silent-nest|The Silent nest bedroom at Trullo Rosy, under the stone vaults}}

<h2>What should you check before booking a trullo?</h2>
<table class="facts">
<thead><tr><th scope="col">Check</th><th scope="col">Why it matters</th><th scope="col">At Trullo Rosy</th></tr></thead>
<tbody>
<tr><th scope="row">Whole house or room</th><td>some trulli are let by the room, with shared spaces</td><td>whole house, 85 m²</td></tr>
<tr><th scope="row">Bedrooms and beds</th><td>cones are small: not every room fits a double bed</td><td>3 bedrooms: 2 queen-size beds and 1 single bed, up to 6 guests</td></tr>
<tr><th scope="row">Heating</th><td>in winter stone is cold</td><td>heating and a fireplace</td></tr>
<tr><th scope="row">Kitchen</th><td>in the countryside restaurants are in town</td><td>equipped kitchen, barbecue in the garden</td></tr>
<tr><th scope="row">Parking</th><td>countryside trulli are reached by car</td><td>free, inside the property</td></tr>
<tr><th scope="row">Wi-Fi</th><td>to work or plan your trips</td><td>fast Wi-Fi and a workspace</td></tr>
<tr><th scope="row">Times</th><td>to plan your journey</td><td>check-in from 3 pm, check-out by 11 am</td></tr>
</tbody>
</table>

<h2>A trullo in Alberobello or in the countryside?</h2>
<p>In Alberobello you sleep among the most famous trulli, but by day the streets are full of visitors. In the countryside between Martina Franca, Locorotondo and Cisternino you get more space, a garden and silence, and by car you can reach every town in the valley: distances are in the <a href="/en/guides/what-to-see-in-the-itria-valley/">Itria Valley guide</a>.</p>

<h2>What is Trullo Rosy like?</h2>
<p><a href="/en/the-trullo/">Trullo Rosy</a> is a traditional trullo on the SP70, in the countryside of Martina Franca, among fruit trees and centuries-old olive trees. It has three bedrooms (Silent nest, Still Bloom and the Alcove), a living room with a fireplace, a kitchen and, outside, a stone courtyard with a well, a pergola with a dining table, a veranda and a hammock among the olive trees. Photos are in the <a href="/en/gallery/">gallery</a>. Everything you need to book is on the page of our <a href="/en/">trullo for rent in Martina Franca</a>.</p>
{{img:salotto-camino|The living room with the fireplace at Trullo Rosy}}

<h2>When is the best time to sleep in a trullo?</h2>
<p>Any season, for different reasons. In summer for the cool stone and beach days (see the <a href="/en/guides/beaches-near-martina-franca/">beaches near Martina Franca</a>); in spring and autumn to visit the towns without crowds; in winter for the fireplace and the Christmas lights, like those in <a href="/en/guides/christmas-in-locorotondo/">nearby Locorotondo</a>.</p>

<h2>Frequently asked questions</h2>
""" + faq_html(DT_FAQ_EN),
        faq=DT_FAQ_EN,
        cta_h2="Try sleeping in a trullo",
        sources_h2="Sources",
        photos_h2="Photos",
        updated="Updated 13 November 2026",
    ),
}


# ---------------------------------------------------------------- Cosa vedere a Locorotondo (14/11/2026)
WIKI_LOCO_IT = ("Wikipedia, \"Locorotondo\" (voce in italiano: chiese, Via Nardelli, feste patronali)", "https://it.wikipedia.org/wiki/Locorotondo")
ITALIA_LOCO = ("italia.it (ENIT), \"Locorotondo\"", "https://www.italia.it/it/puglia/bari/locorotondo")
WIKI_LOCO_EN = ("Wikipedia, \"Locorotondo\" (voce in inglese: Locorotondo DOC, Borghi più belli d'Italia, Bandiera Arancione)", "https://en.wikipedia.org/wiki/Locorotondo")

LO_FAQ_IT = [
    ("Quanto tempo serve per visitare Locorotondo?", "Per il centro storico bastano due o tre ore a piedi: è piccolo e circolare. Con una sosta al belvedere al tramonto e una cena, mezza giornata è il tempo giusto."),
    ("Perché si chiama Locorotondo?", "Per la forma del centro storico: le case bianche sono disposte ad anelli intorno al punto più alto della collina. Il nome attuale è in uso dal 1834; prima il paese si chiamava Casale Rotondo e poi Luogorotondo."),
    ("Cosa sono le cummerse?", "Sono le case del centro storico con il tetto spiovente e appuntito, fatto di lastre di pietra calcarea. Sono la cosa che rende Locorotondo diverso dagli altri paesi della Valle d'Itria."),
    ("Quanto dista Locorotondo da Trullo Rosy?", "Circa 12 km in linea d'aria: il trullo è nella campagna di Martina Franca, e in auto la strada è un po' più lunga."),
    ("Quando ci sono le feste a Locorotondo?", "Le feste principali sono San Giorgio (dal 21 al 24 aprile) e San Rocco, il patrono, a metà agosto, con la fiera del 14 agosto e i fuochi d'artificio. A Natale il centro si riempie di luminarie."),
]
LO_FAQ_EN = [
    ("How long do you need to visit Locorotondo?", "Two or three hours on foot are enough for the old town: it is small and round. With a stop at the viewpoint at sunset and dinner, half a day is about right."),
    ("Why is it called Locorotondo?", "Because of the shape of its old town: the white houses are laid out in rings around the top of the hill. The current name has been in use since 1834; before that the town was called Casale Rotondo and then Luogorotondo."),
    ("What are cummerse?", "They are the old-town houses with steep, pointed roofs made of limestone slabs. They are what makes Locorotondo look different from the other towns in the Itria Valley."),
    ("How far is Locorotondo from Trullo Rosy?", "About 12 km as the crow flies: the trullo is in the countryside of Martina Franca, and by car the road is a little longer."),
    ("When are the festivals in Locorotondo?", "The main ones are Saint George (21 to 24 April) and Saint Roch, the patron saint, in mid-August, with the fair on 14 August and fireworks. At Christmas the old town fills with lights."),
]

LOCOROTONDO = {
    "key": "cosa-vedere-locorotondo",
    "date": "2026-11-14",
    "modified": "2026-11-14",
    "hero": "locorotondo/panorama",
    "paths": {"it": "/guide/cosa-vedere-a-locorotondo/", "en": "/en/guides/what-to-see-in-locorotondo/"},
    "sources": [WIKI_LOCO_IT, ITALIA_LOCO, WIKI_LOCO_EN],
    "it": dict(
        title="Cosa vedere a Locorotondo: centro storico e belvedere",
        desc="Cosa vedere a Locorotondo: il centro storico circolare, le cummerse, la Chiesa Madre, il belvedere sulla Valle d'Itria, il vino e le feste dell'anno.",
        h1="Cosa vedere a Locorotondo, il paese rotondo della Valle d'Itria",
        answer="A Locorotondo si viene per il centro storico: un cerchio di case bianche con i tetti a punta, le cummerse, sulla cima di una collina a 410 metri. Si gira a piedi in due o tre ore: la Chiesa Madre di San Giorgio, Santa Maria della Greca e via Nardelli, il belvedere sulla Valle d'Itria, da vedere al tramonto.",
        body="""
<h2>Cosa c'è da vedere a Locorotondo?</h2>
<p>Il paese è piccolo e il centro storico si gira tutto a piedi. Queste sono le tappe principali, in un giro ad anello che parte e finisce alla villa comunale.</p>
<table class="facts">
<thead><tr><th scope="col">Cosa</th><th scope="col">Perché vederlo</th><th scope="col">Tempo</th></tr></thead>
<tbody>
<tr><th scope="row">Centro storico e cummerse</th><td>case bianche disposte ad anelli, tetti spioventi in pietra</td><td>1 ora</td></tr>
<tr><th scope="row">Chiesa Madre di San Giorgio Martire</th><td>la chiesa principale, con la facciata neoclassica e la cupola</td><td>20 minuti</td></tr>
<tr><th scope="row">Santa Maria della Greca</th><td>la chiesa più antica del centro, documentata dal 1520</td><td>15 minuti</td></tr>
<tr><th scope="row">Via Nardelli, il "Lungomare"</th><td>il belvedere sulla campagna dei trulli, il più bello al tramonto</td><td>30 minuti</td></tr>
<tr><th scope="row">Villa comunale</th><td>il giardino pubblico all'ingresso del centro, con la vista sulla valle</td><td>15 minuti</td></tr>
</tbody>
</table>
{{img:locorotondo/vicolo-sera|Un vicolo bianco del centro storico di Locorotondo}}

<h2>Perché Locorotondo è rotondo?</h2>
<p>Il nome viene dalla forma del centro storico: le case bianche sono disposte ad anelli concentrici intorno al punto più alto della collina. Il paese è nato intorno all'anno Mille; prima si chiamava Casale San Giorgio, poi Casale Rotondo e Luogorotondo, e il nome Locorotondo è in uso dal 1834.</p>
<p>Le case hanno quasi tutte il tetto spiovente e appuntito, fatto di lastre di pietra calcarea: sono le <strong>cummerse</strong>, che danno al paese un'aria quasi nordica. Locorotondo fa parte dei Borghi più belli d'Italia e ha la Bandiera Arancione del Touring Club.</p>
{{img:locorotondo/via-morelli|Via Morelli, nel centro storico di Locorotondo}}

<h2>Quali chiese visitare nel centro storico?</h2>
<p>La <strong>Chiesa Madre di San Giorgio Martire</strong> è la più grande: fu costruita tra la fine del Settecento e l'inizio dell'Ottocento sui resti di una chiesa più antica, ha la facciata neoclassica e, all'interno, bassorilievi in pietra del Trecento.</p>
<p><strong>Santa Maria della Greca</strong> è la chiesa più antica del centro: la prima notizia è del 1520, ma l'origine è probabilmente precedente. Fuori è semplice, con un rosone sulla facciata; dentro è sobria e raccolta. Lungo il giro si incontrano anche la chiesa di San Rocco (1710), dedicata al patrono, e la piccola chiesa di San Nicola (1582).</p>
{{img:locorotondo/san-giorgio|L'interno della Chiesa Madre di San Giorgio a Locorotondo}}

<h2>Dov'è il belvedere di Locorotondo?</h2>
<p>È <strong>via Nardelli</strong>, che tutti chiamano "Lungomare" anche se il mare non c'è: la strada corre sul bordo del centro storico e si affaccia sulla Valle d'Itria, tra vigneti, muretti a secco e trulli. È il punto più bello al tramonto. Un'altra vista sulla campagna si ha dalla villa comunale, all'ingresso del paese.</p>
{{img:locorotondo/trulli-campagna|La campagna dei trulli vista dalla villa comunale di Locorotondo}}

<h2>Cosa assaggiare e bere a Locorotondo?</h2>
<p>Locorotondo dà il nome a un vino bianco, il <strong>Locorotondo DOC</strong>, fermo o spumante, fatto soprattutto con uve verdeca e bianco d'Alessano coltivate nelle campagne intorno al paese. In tavola si trovano piatti della tradizione come le orecchiette al sugo di carne, il galletto al forno e il calzone di carne e cipolla.</p>

<h2>Quando andare a Locorotondo?</h2>
<ul>
<li><strong>In primavera e in autunno</strong> il paese è tranquillo e si cammina bene.</li>
<li><strong>Ad aprile</strong> c'è la festa di San Giorgio (dal 21 al 24 aprile), con la cerimonia del dono delle chiavi al santo.</li>
<li><strong>A metà agosto</strong> c'è la festa del patrono San Rocco, con la fiera del 14 agosto e la gara di fuochi d'artificio la notte del 16.</li>
<li><strong>A Natale</strong> il centro si riempie di luminarie: date e percorso sono nella guida al <a href="/guide/natale-a-locorotondo/">Natale a Locorotondo</a>.</li>
</ul>
{{img:locorotondo/notte|Locorotondo di notte}}

<h2>Come arrivare da Trullo Rosy e cosa vedere nei dintorni?</h2>
<p>Da <a href="/il-trullo/">Trullo Rosy</a>, nella campagna di Martina Franca, Locorotondo è a circa 12 km in linea d'aria; in auto la strada è un po' più lunga. Da Locorotondo Martina Franca è a circa 6 km, Cisternino e Alberobello a circa 8: si possono unire nella stessa giornata. Le distanze di tutti i paesi sono nella <a href="/guide/cosa-vedere-in-valle-ditria/">guida alla Valle d'Itria</a>, e altri luoghi sono nella pagina <a href="/dintorni/">dintorni</a>. Tutte le informazioni per prenotare sono nella pagina del nostro <a href="/">trullo in affitto a Martina Franca</a>.</p>

<h2>Domande frequenti</h2>
""" + faq_html(LO_FAQ_IT),
        faq=LO_FAQ_IT,
        cta_h2="Dormi in un trullo a pochi chilometri da Locorotondo",
        sources_h2="Fonti",
        photos_h2="Foto",
        updated="Aggiornato il 14 novembre 2026",
    ),
    "en": dict(
        title="What to see in Locorotondo: old town and viewpoint",
        desc="What to see in Locorotondo, Puglia: the round old town, the cummerse roofs, the Mother Church, the Itria Valley viewpoint, local wine and festivals.",
        h1="What to see in Locorotondo, the round town of the Itria Valley",
        answer="People come to Locorotondo for its old town: a circle of white houses with pointed roofs, the cummerse, on top of a hill at 410 metres. You can see it on foot in two or three hours: the Mother Church of Saint George, Santa Maria della Greca and Via Nardelli, the viewpoint over the Itria Valley, best at sunset.",
        body="""
<h2>What is there to see in Locorotondo?</h2>
<p>The town is small and the whole old town can be seen on foot. These are the main stops, on a loop that starts and ends at the public garden.</p>
<table class="facts">
<thead><tr><th scope="col">What</th><th scope="col">Why see it</th><th scope="col">Time</th></tr></thead>
<tbody>
<tr><th scope="row">Old town and cummerse</th><td>white houses laid out in rings, steep stone roofs</td><td>1 hour</td></tr>
<tr><th scope="row">Mother Church of Saint George the Martyr</th><td>the main church, with its neoclassical facade and dome</td><td>20 minutes</td></tr>
<tr><th scope="row">Santa Maria della Greca</th><td>the oldest church in the old town, recorded since 1520</td><td>15 minutes</td></tr>
<tr><th scope="row">Via Nardelli, the "Lungomare"</th><td>the viewpoint over trulli country, best at sunset</td><td>30 minutes</td></tr>
<tr><th scope="row">Public garden (Villa comunale)</th><td>the garden at the entrance to the old town, with a view of the valley</td><td>15 minutes</td></tr>
</tbody>
</table>
{{img:locorotondo/vicolo-sera|A white lane in Locorotondo's old town}}

<h2>Why is Locorotondo round?</h2>
<p>The name comes from the shape of the old town: the white houses are laid out in concentric rings around the top of the hill. The town was founded around the year 1000; it was first called Casale San Giorgio, then Casale Rotondo and Luogorotondo, and the name Locorotondo has been in use since 1834.</p>
<p>Almost all the houses have steep, pointed roofs made of limestone slabs: these are the <strong>cummerse</strong>, which give the town an almost northern European look. Locorotondo is one of the "Borghi più belli d'Italia" (most beautiful villages in Italy) and holds the Touring Club's Orange Flag.</p>
{{img:locorotondo/via-morelli|Via Morelli in Locorotondo's old town}}

<h2>Which churches should you visit in the old town?</h2>
<p>The <strong>Mother Church of Saint George the Martyr</strong> is the largest: it was built between the late 18th and early 19th century on the remains of an older church, has a neoclassical facade and, inside, 14th-century stone bas-reliefs.</p>
<p><strong>Santa Maria della Greca</strong> is the oldest church in the old town: it is first recorded in 1520, but is probably older. It is plain outside, with a rose window on the facade, and simple inside. Along the way you also pass the church of San Rocco (1710), dedicated to the patron saint, and the small church of San Nicola (1582).</p>
{{img:locorotondo/san-giorgio|Inside the Mother Church of Saint George in Locorotondo}}

<h2>Where is the Locorotondo viewpoint?</h2>
<p>It is <strong>Via Nardelli</strong>, which everyone calls the "Lungomare" (seafront) even though there is no sea: the street runs along the edge of the old town and looks out over the Itria Valley, with vineyards, dry-stone walls and trulli. It is at its best at sunset. The public garden at the entrance to the town also has a view of the countryside.</p>
{{img:locorotondo/trulli-campagna|Trulli countryside seen from Locorotondo's public garden}}

<h2>What to eat and drink in Locorotondo?</h2>
<p>Locorotondo gives its name to a white wine, <strong>Locorotondo DOC</strong>, still or sparkling, made mainly from Verdeca and Bianco d'Alessano grapes grown in the countryside around the town. Traditional dishes include orecchiette with meat sauce, roast cockerel and calzone filled with meat and onion.</p>

<h2>When to go to Locorotondo?</h2>
<ul>
<li><strong>In spring and autumn</strong> the town is quiet and good for walking.</li>
<li><strong>In April</strong> there is the feast of Saint George (21 to 24 April), with the ceremony in which the town's keys are given to the saint.</li>
<li><strong>In mid-August</strong> there is the feast of the patron Saint Roch, with the fair on 14 August and a fireworks contest on the night of the 16th.</li>
<li><strong>At Christmas</strong> the old town fills with lights: dates and route are in our guide to <a href="/en/guides/christmas-in-locorotondo/">Christmas in Locorotondo</a>.</li>
</ul>
{{img:locorotondo/notte|Locorotondo at night}}

<h2>How to get there from Trullo Rosy and what is nearby?</h2>
<p>From <a href="/en/the-trullo/">Trullo Rosy</a>, in the countryside of Martina Franca, Locorotondo is about 12 km as the crow flies; by car the road is a little longer. From Locorotondo, Martina Franca is about 6 km away and Cisternino and Alberobello about 8, so you can combine them in one day. Distances to every town are in the <a href="/en/guides/what-to-see-in-the-itria-valley/">Itria Valley guide</a>, and more places are on the <a href="/en/surroundings/">surroundings</a> page. Everything you need to book is on the page of our <a href="/en/">trullo for rent in Martina Franca</a>.</p>

<h2>Frequently asked questions</h2>
""" + faq_html(LO_FAQ_EN),
        faq=LO_FAQ_EN,
        cta_h2="Stay in a trullo a few kilometres from Locorotondo",
        sources_h2="Sources",
        photos_h2="Photos",
        updated="Updated 14 November 2026",
    ),
}

GUIDES = [VALLE, SPIAGGE, DORMIRE, LOCOROTONDO]
