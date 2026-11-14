"""Guide sui prodotti tipici della Valle d'Itria (14/11/2026).

Stesso formato di guides.py. Fatti solo dalle fonti citate in fondo; dove le fonti
non coincidono (es. durata della salagione) si usa la scheda del Presidio Slow Food.
Produttori: solo quelli elencati dal Presidio. Aggiornare se la scheda cambia.
"""

SLOW_FOOD_IT = ("Fondazione Slow Food, Presidio \"Capocollo di Martina Franca\" (scheda aggiornata il 23 marzo 2026)",
                "https://www.fondazioneslowfood.com/it/presidi-slow-food/capocollo-di-martina-franca/")
SLOW_FOOD_EN = ("Slow Food Foundation, \"Martina Franca Capocollo\" Presidium",
                "https://www.fondazioneslowfood.com/en/slow-food-presidia/martina-franca-capocollo/")
ITALIA_IT = ("Italia.it, \"La regione Puglia attraverso la pizza di Gino Sorbillo: il capocollo di Martina Franca\"",
             "https://www.italia.it/it/puglia/cosa-fare/pizza-di-gino-sorbillo-storia-capocollo-di-martina-franca")
FIRSTONLINE = ("FirstOnline, \"Capocollo di Martina Franca, un'antica storia di sapori\"",
               "https://www.firstonline.info/en/capocollo-di-martina-franca-una-antica-storia-di-sapori/")


def faq_html(faq):
    return "\n".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)


CAP_FAQ_IT = [
    ("Cos'è il capocollo di Martina Franca?", "È un salume di maiale fatto con la coppa, la parte tra collo e costata, salato, lavato con vino cotto, affumicato con fragno e mallo di mandorla e stagionato almeno 6 mesi. È un Presidio Slow Food."),
    ("Dove si compra il capocollo di Martina Franca?", "Dai produttori del Presidio Slow Food: Salumi Martina Franca a Martina Franca, la Macelleria Semeraro e C. & L. Carni a Locorotondo, il Salumificio Santoro a Cisternino. I recapiti sono sulla scheda del Presidio."),
    ("Quanto stagiona il capocollo di Martina Franca?", "Secondo il disciplinare del Presidio Slow Food si mangia dopo almeno 6 mesi di stagionatura."),
    ("In che periodo si produce il capocollo?", "Secondo il Presidio Slow Food la produzione va da settembre a maggio. Il disciplinare esclude nitriti, nitrati e altri additivi."),
    ("Dove dormire per un viaggio tra i sapori della Valle d'Itria?", "Nella campagna di Martina Franca, per esempio a Trullo Rosy: un trullo intero con tre camere, camino e parcheggio, a circa 6 km da Martina Franca e 12 da Locorotondo e Cisternino in linea d'aria."),
]
CAP_FAQ_EN = [
    ("What is Martina Franca capocollo?", "It is a pork cured meat made from the coppa, the cut between the neck and the ribs. It is salted, washed with cooked wine, smoked with Macedonian oak and almond husks and aged for at least 6 months. It is a Slow Food Presidium."),
    ("Where can you buy Martina Franca capocollo?", "From the Slow Food Presidium producers: Salumi Martina Franca in Martina Franca, Macelleria Semeraro and C. & L. Carni in Locorotondo, and Salumificio Santoro in Cisternino. Their contacts are on the Presidium page."),
    ("How long is Martina Franca capocollo aged?", "Under the Slow Food Presidium rules it is eaten after at least 6 months of ageing."),
    ("When is capocollo made?", "According to the Slow Food Presidium, production runs from September to May. The rules exclude nitrites, nitrates and other additives."),
    ("Where to stay for a food trip in the Itria Valley?", "In the countryside of Martina Franca, for example at Trullo Rosy: an entire trullo with three bedrooms, a fireplace and parking, about 6 km from Martina Franca and 12 from Locorotondo and Cisternino as the crow flies."),
]

CAPOCOLLO = {
    "key": "capocollo-martina-franca",
    "date": "2026-11-14",
    "modified": "2026-11-14",
    "hero": "luoghi/martina-franca",
    "paths": {"it": "/guide/capocollo-di-martina-franca/", "en": "/en/guides/martina-franca-capocollo/"},
    "sources": [SLOW_FOOD_IT, SLOW_FOOD_EN, ITALIA_IT, FIRSTONLINE],
    "it": dict(
        title="Capocollo di Martina Franca: cos'è e dove comprarlo",
        desc="Capocollo di Martina Franca, Presidio Slow Food: come si fa, quanto stagiona, i produttori di Martina Franca, Locorotondo e Cisternino e come assaggiarlo.",
        h1="Capocollo di Martina Franca: cos'è, come si fa e dove comprarlo",
        answer="Il capocollo di Martina Franca è un salume di maiale fatto con la coppa, salato per 15-20 giorni, lavato con vino cotto, affumicato con legno di fragno e mallo di mandorla e stagionato almeno 6 mesi. È un Presidio Slow Food e si produce solo a Martina Franca, Locorotondo e Cisternino: si compra direttamente dai quattro produttori del Presidio.",
        body="""
<h2>Cos'è il capocollo di Martina Franca?</h2>
<p>Il capocollo (in dialetto <em>chépecùedde</em>) è il salume tipico della Murgia dei Trulli. Si fa con la <strong>coppa</strong>, la parte del maiale tra il collo e la costata, e secondo la Fondazione Slow Food era già conosciuto nel Regno di Napoli dal XVIII secolo. Italia.it racconta che un tempo i maiali allevati nel Salento e intorno a Taranto venivano portati a Martina Franca per la macellazione: il clima ventilato, secco e fresco della collina era adatto a lavorare i salumi.</p>
<p>Ogni pezzo pesa tra i due chili e mezzo e i quattro chili. Il disciplinare del Presidio esclude nitriti, nitrati e altri additivi e prevede maiali allevati allo stato semibrado, nutriti soprattutto con cereali e legumi locali.</p>
<table class="facts">
<thead><tr><th scope="col">Fase</th><th scope="col">Come si fa (Presidio Slow Food)</th></tr></thead>
<tbody>
<tr><th scope="row">Taglio</th><td>coppa, tra collo e costata</td></tr>
<tr><th scope="row">Salagione</th><td>sotto sale per 15-20 giorni</td></tr>
<tr><th scope="row">Lavaggio</th><td>con vino cotto: mosto cotto, vino di vitigni autoctoni e spezie</td></tr>
<tr><th scope="row">Insacco</th><td>budello naturale di maiale, avvolto in panni di lino o cotone</td></tr>
<tr><th scope="row">Affumicatura</th><td>due giorni con fragno (<em>Quercus trojana</em>) e mallo di mandorla</td></tr>
<tr><th scope="row">Stagionatura</th><td>almeno 6 mesi</td></tr>
<tr><th scope="row">Zona</th><td>Martina Franca (TA), Locorotondo (BA), Cisternino (BR)</td></tr>
<tr><th scope="row">Produzione</th><td>da settembre a maggio</td></tr>
</tbody>
</table>
{{img:luoghi/martina-franca|Il centro storico di Martina Franca}}

<h2>Perché si affumica con il fragno?</h2>
<p>Il fragno è la quercia dei boschi intorno a Martina Franca. Oggi i produttori bruciano insieme fragno e mallo di mandorla per due giorni in appositi camini; un tempo si usavano rami di macchia mediterranea fatti bruciare senza fiamma. È il fumo, insieme al lavaggio nel vino cotto, a dare al capocollo il suo profumo.</p>

<h2>Dove comprare il capocollo di Martina Franca?</h2>
<p>Il modo più sicuro per avere il capocollo del Presidio è comprarlo da chi lo fa. Questi sono i produttori elencati dalla Fondazione Slow Food (scheda aggiornata a marzo 2026); telefono ed email di ciascuno sono sulla <a href="https://www.fondazioneslowfood.com/it/presidi-slow-food/capocollo-di-martina-franca/" rel="noopener" target="_blank">pagina del Presidio</a>, ed è meglio chiamare prima di passare.</p>
<table class="facts">
<thead><tr><th scope="col">Produttore</th><th scope="col">Paese</th></tr></thead>
<tbody>
<tr><th scope="row">Salumi Martina Franca di Stefano Caroli</th><td>Martina Franca</td></tr>
<tr><th scope="row">Macelleria Semeraro di Nicola Semeraro</th><td>Locorotondo</td></tr>
<tr><th scope="row">C. &amp; L. Carni di Francesco Convertini</th><td>Locorotondo</td></tr>
<tr><th scope="row">Salumificio Santoro di Giuseppe Santoro</th><td>Cisternino</td></tr>
</tbody>
</table>
<p>Il capocollo si trova anche in molte salumerie e macellerie della zona: se cerchi quello del Presidio, chiedi chi l'ha prodotto.</p>

<h2>Come si mangia il capocollo?</h2>
<p>Si mangia crudo, tagliato a fette sottili, come antipasto o in un panino. Visto che la produzione va da settembre a maggio, l'autunno e l'inverno sono il momento giusto per assaggiarlo appena stagionato. Nella stessa zona si fa il vino bianco Locorotondo DOC: un abbinamento tutto locale da provare.</p>
<p>Un giro tra i produttori si unisce bene a una visita dei paesi: Locorotondo con il suo centro storico bianco (vedi la guida <a href="/guide/cosa-vedere-a-locorotondo/">cosa vedere a Locorotondo</a>) e Cisternino, il paese delle bombette. Tutti i paesi, con le distanze dal trullo, sono nella guida <a href="/guide/cosa-vedere-in-valle-ditria/">cosa vedere in Valle d'Itria</a>.</p>
{{img:locorotondo/panorama|Locorotondo vista dalla campagna}}

<h2>Dove dormire per un viaggio tra i sapori della Valle d'Itria?</h2>
<p>I tre paesi del capocollo sono vicini: da <a href="/il-trullo/">Trullo Rosy</a>, nella campagna di Martina Franca, Martina Franca è a circa 6 km in linea d'aria, Locorotondo e Cisternino a circa 12. Puoi passare dai produttori di giorno e tornare la sera davanti al camino. Altri luoghi sono nella pagina <a href="/dintorni/">Dintorni</a>, e tutte le informazioni per prenotare nella pagina del nostro <a href="/">trullo in affitto a Martina Franca</a>.</p>

<h2>Domande frequenti</h2>
""" + faq_html(CAP_FAQ_IT),
        faq=CAP_FAQ_IT,
        cta_h2="Assaggia la Valle d'Itria dormendo in un trullo",
        sources_h2="Fonti",
        photos_h2="Foto",
        updated="Aggiornato il 14 novembre 2026",
    ),
    "en": dict(
        title="Martina Franca capocollo: what it is, where to buy",
        desc="Martina Franca capocollo, a Slow Food Presidium: how it is made, how long it ages, makers in Martina Franca, Locorotondo and Cisternino and how to eat it.",
        h1="Martina Franca capocollo: what it is, how it's made, where to buy it",
        answer="Martina Franca capocollo is a pork cured meat made from the coppa, salted for 15-20 days, washed with cooked wine, smoked with Macedonian oak and almond husks and aged for at least 6 months. It is a Slow Food Presidium made only in Martina Franca, Locorotondo and Cisternino, and you buy it directly from the four Presidium producers.",
        body="""
<h2>What is Martina Franca capocollo?</h2>
<p>Capocollo (<em>chépecùedde</em> in dialect) is the typical cured meat of the Murgia dei Trulli. It is made from the <strong>coppa</strong>, the cut of pork between the neck and the ribs, and according to the Slow Food Foundation it was already known in the Kingdom of Naples in the 18th century. Italia.it tells how pigs raised in Salento and around Taranto used to be brought to Martina Franca for slaughter: the windy, dry and cool hill climate was ideal for curing meat.</p>
<p>Each piece weighs between two and a half and four kilos. The Presidium rules exclude nitrites, nitrates and other additives, and require semi-free-range pigs fed mainly on local cereals and legumes.</p>
<table class="facts">
<thead><tr><th scope="col">Step</th><th scope="col">How it's done (Slow Food Presidium)</th></tr></thead>
<tbody>
<tr><th scope="row">Cut</th><td>coppa, between neck and ribs</td></tr>
<tr><th scope="row">Salting</th><td>under salt for 15-20 days</td></tr>
<tr><th scope="row">Washing</th><td>with cooked wine: cooked must, wine from local grapes and spices</td></tr>
<tr><th scope="row">Casing</th><td>natural pork casing, wrapped in linen or cotton cloth</td></tr>
<tr><th scope="row">Smoking</th><td>two days over Macedonian oak (<em>Quercus trojana</em>) and almond husks</td></tr>
<tr><th scope="row">Ageing</th><td>at least 6 months</td></tr>
<tr><th scope="row">Area</th><td>Martina Franca (TA), Locorotondo (BA), Cisternino (BR)</td></tr>
<tr><th scope="row">Production</th><td>September to May</td></tr>
</tbody>
</table>
{{img:luoghi/martina-franca|The old town of Martina Franca}}

<h2>Why is it smoked with Macedonian oak?</h2>
<p>The Macedonian oak (<em>fragno</em>) is the oak of the woods around Martina Franca. Today producers burn it together with almond husks for two days in purpose-built chimneys; in the past they used branches of Mediterranean scrub, smouldering without a flame. The smoke and the cooked-wine wash give capocollo its aroma.</p>

<h2>Where to buy Martina Franca capocollo?</h2>
<p>The surest way to get Presidium capocollo is to buy it from the people who make it. These are the producers listed by the Slow Food Foundation (page updated in March 2026); phone numbers and emails are on the <a href="https://www.fondazioneslowfood.com/en/slow-food-presidia/martina-franca-capocollo/" rel="noopener" target="_blank">Presidium page</a>, and it is best to call before you go.</p>
<table class="facts">
<thead><tr><th scope="col">Producer</th><th scope="col">Town</th></tr></thead>
<tbody>
<tr><th scope="row">Salumi Martina Franca (Stefano Caroli)</th><td>Martina Franca</td></tr>
<tr><th scope="row">Macelleria Semeraro (Nicola Semeraro)</th><td>Locorotondo</td></tr>
<tr><th scope="row">C. &amp; L. Carni (Francesco Convertini)</th><td>Locorotondo</td></tr>
<tr><th scope="row">Salumificio Santoro (Giuseppe Santoro)</th><td>Cisternino</td></tr>
</tbody>
</table>
<p>You will also find capocollo in many delis and butchers in the area: if you want the Presidium one, ask who made it.</p>

<h2>How do you eat capocollo?</h2>
<p>It is eaten raw, thinly sliced, as a starter or in a sandwich. Since production runs from September to May, autumn and winter are a good time to taste it freshly aged. The same area makes Locorotondo DOC white wine: a fully local pairing worth trying.</p>
<p>A tour of the producers fits well with a visit to the towns: Locorotondo and its white old town (see <a href="/en/guides/what-to-see-in-locorotondo/">what to see in Locorotondo</a>) and Cisternino, the town of bombette. All the towns, with distances from the trullo, are in our guide <a href="/en/guides/what-to-see-in-the-itria-valley/">what to see in the Itria Valley</a>.</p>
{{img:locorotondo/panorama|Locorotondo seen from the countryside}}

<h2>Where to stay for a food trip in the Itria Valley?</h2>
<p>The three capocollo towns are close together: from <a href="/en/the-trullo/">Trullo Rosy</a>, in the countryside of Martina Franca, Martina Franca is about 6 km as the crow flies and Locorotondo and Cisternino about 12. You can visit the producers by day and spend the evening by the fireplace. More places are on our <a href="/en/surroundings/">Surroundings</a> page, and everything you need to book is on the page of our <a href="/en/">trullo for rent in Martina Franca</a>.</p>

<h2>Frequently asked questions</h2>
""" + faq_html(CAP_FAQ_EN),
        faq=CAP_FAQ_EN,
        cta_h2="Taste the Itria Valley from a trullo",
        sources_h2="Sources",
        photos_h2="Photos",
        updated="Updated 14 November 2026",
    ),
}

GUIDES = [CAPOCOLLO]
