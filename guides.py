"""Guide del sito. Ogni guida ha un testo per lingua (le lingue mancanti non vengono generate).

Corpo in HTML semplice. Le immagini si inseriscono con {{img:cartella/nome|alt}}.
Fonti e date: solo da fonti verificabili, citate in fondo alla guida.
"""

GUIDES = [
    {
        "key": "natale-locorotondo",
        "date": "2026-11-10",
        "hero": "locorotondo/tramonto",
        "paths": {"it": "/guide/natale-a-locorotondo/", "en": "/en/guides/christmas-in-locorotondo/"},
        "sources": [
            ("Comune di Locorotondo, avviso \"Natale a Locorotondo 2026\" (7 settembre 2026)",
             "https://www.comune.locorotondo.ba.it/it/news/natale-a-locorotondo-2026-avviso-pubblico-per-la-presentazione-di-proposte-progettuali"),
            ("Agorà Blog, \"Natale 2026 a Locorotondo: all'avviso pubblico giungono 6 proposte\" (2 ottobre 2026)",
             "https://agorablog.it/ultime-news/natale-2026-a-locorotondo-allavviso-pubblico-giungono-6-proposte/"),
            ("regionepuglia.org, \"Natale a Locorotondo\" (aggiornato al 10 novembre 2026)",
             "https://www.regionepuglia.org/natale-locorotondo/"),
        ],
        "it": dict(
            title="Luminarie e mercatini di Natale a Locorotondo 2026",
            desc="Natale e ponte dell'Immacolata a Locorotondo: quando si accendono le luminarie, dove vederle, mercatini e consigli per dormire vicino, in un trullo.",
            h1="Natale a Locorotondo: luminarie, Immacolata e mercatini",
            answer="A Natale il centro storico di Locorotondo si riempie di luminarie e, come nel 2025, dei mercatini di Natale, tra i vicoli bianchi e le case con i tetti a punta. Per il 2026 il Comune ha indicato un programma dal 22 novembre 2026 al 6 gennaio 2027, quindi il ponte dell'Immacolata (8 dicembre) cade in pieno periodo di luci. Date dei mercatini e orari ufficiali non sono ancora usciti: aggiorneremo questa pagina appena il Comune li pubblica.",
            body="""
<h2>Quando si accendono le luminarie di Locorotondo nel 2026?</h2>
<p>Il Comune di Locorotondo, con l'avviso pubblicato il 7 settembre 2026, ha previsto le iniziative di Natale <strong>indicativamente dal 22 novembre 2026 al 6 gennaio 2027</strong>. Ad oggi (10 novembre 2026) la data esatta dell'accensione non è stata annunciata: al bando hanno risposto sei proposte e la scelta del progetto è ancora in corso.</p>
<p>Negli ultimi anni le luci si sono accese nella seconda metà di novembre e sono rimaste fino ai primi giorni di gennaio.</p>
<table class="facts">
<thead><tr><th scope="col">Anno</th><th scope="col">Accensione</th><th scope="col">Fino a</th></tr></thead>
<tbody>
<tr><th scope="row">2024</th><td>14 novembre</td><td>inizio gennaio</td></tr>
<tr><th scope="row">2025</th><td>22 novembre</td><td>prima settimana di gennaio 2026</td></tr>
<tr><th scope="row">2026</th><td>programma indicato dal 22 novembre (data da confermare)</td><td>6 gennaio 2027</td></tr>
</tbody>
</table>
{{img:locorotondo/vicolo-luci|Un vicolo del centro storico di Locorotondo con le luci sospese}}

<h2>Perché andare a Locorotondo per l'Immacolata?</h2>
<p>L'8 dicembre e il ponte che lo accompagna sono il momento in cui le luminarie sono già tutte accese e i mercatini sono aperti. Il centro storico è piccolo e si gira a piedi: al tramonto, quando le luci si accendono sulle facciate bianche, è il momento più bello per una passeggiata.</p>
<p>Il resto della Valle d'Itria fa festa nello stesso periodo: Martina Franca, Alberobello e Cisternino sono vicini, e in una giornata se ne possono vedere due.</p>

<h2>Dove sono le luci nel centro storico?</h2>
<p>Nel 2025 il percorso delle luminarie partiva da <strong>piazza Aldo Moro</strong> e attraversava <strong>via Porta Nuova, via Morelli, via Montanaro, via Bruno e via Eroi Dogali</strong>, con le luci accese ogni sera dalle 17 circa. Il percorso del 2026 non è ancora stato annunciato.</p>
{{img:locorotondo/via-morelli|Via Morelli, nel centro storico di Locorotondo}}
<p>Lungo la strada vale una sosta la <strong>Chiesa Madre di San Giorgio Martire</strong>, con la sua grande cupola, e il belvedere della villa comunale, che guarda sulla campagna dei trulli.</p>
{{img:locorotondo/san-giorgio|L'interno della Chiesa Madre di San Giorgio a Locorotondo}}

<h2>Ci sono i mercatini di Natale?</h2>
<p>Sì. Nel 2025 i mercatini sono stati aperti <strong>dal 30 novembre 2025 al 6 gennaio 2026</strong> in piazza Aldo Moro, nella villa comunale e nelle vie vicino al Municipio. Le date del 2026 non sono ancora ufficiali.</p>

<h2>Come organizzare la visita</h2>
<ul>
<li><strong>Quando:</strong> arriva nel tardo pomeriggio, così vedi il paese con la luce del giorno e poi con le luminarie accese.</li>
<li><strong>Nei weekend</strong> e al ponte dell'Immacolata c'è molta gente: se puoi, scegli un giorno feriale.</li>
<li><strong>Abbigliamento:</strong> la sera in collina fa freddo, e le strade del centro sono in pietra.</li>
<li><strong>Dove dormire:</strong> Locorotondo confina con Martina Franca. Dormire in un trullo in campagna, come <a href="/il-trullo/">Trullo Rosy</a>, ti permette di girare i paesi della Valle d'Itria e tornare la sera nel silenzio, davanti al camino.</li>
</ul>
{{img:locorotondo/trulli-campagna|La campagna dei trulli vista dalla villa comunale di Locorotondo}}

<h2>Domande frequenti</h2>
<details><summary>Quando iniziano le luminarie di Locorotondo nel 2026?</summary><p>Il Comune ha indicato il periodo dal 22 novembre 2026 al 6 gennaio 2027. La data esatta dell'accensione non è ancora stata annunciata.</p></details>
<details><summary>Le luci sono accese all'Immacolata?</summary><p>Sì: l'8 dicembre cade dentro il periodo indicato dal Comune, e negli ultimi anni le luci erano già accese da fine novembre.</p></details>
<details><summary>A che ora si accendono le luci?</summary><p>Nel 2025 le luci si accendevano ogni sera dalle 17 circa. Gli orari del 2026 non sono ancora stati pubblicati.</p></details>
<details><summary>Dove dormire vicino a Locorotondo a Natale?</summary><p>Nella campagna tra Martina Franca e Locorotondo ci sono trulli in affitto, come Trullo Rosy: un trullo intero con tre camere, camino e parcheggio.</p></details>
""",
            faq=[
                ("Quando iniziano le luminarie di Locorotondo nel 2026?", "Il Comune ha indicato il periodo dal 22 novembre 2026 al 6 gennaio 2027. La data esatta dell'accensione non è ancora stata annunciata."),
                ("Le luci sono accese all'Immacolata?", "Sì: l'8 dicembre cade dentro il periodo indicato dal Comune, e negli ultimi anni le luci erano già accese da fine novembre."),
                ("A che ora si accendono le luci?", "Nel 2025 le luci si accendevano ogni sera dalle 17 circa. Gli orari del 2026 non sono ancora stati pubblicati."),
                ("Dove dormire vicino a Locorotondo a Natale?", "Nella campagna tra Martina Franca e Locorotondo ci sono trulli in affitto, come Trullo Rosy: un trullo intero con tre camere, camino e parcheggio."),
            ],
            cta_h2="Dormi in un trullo a pochi passi dalle luci",
            sources_h2="Fonti",
            photos_h2="Foto",
            updated="Aggiornato il 10 novembre 2026",
        ),
        "en": dict(
            title="Christmas in Locorotondo 2026: lights and dates",
            desc="Christmas and the Immaculate Conception holiday in Locorotondo, Puglia: when the lights go on, where to see them, markets, and where to stay in a trullo.",
            h1="Christmas in Locorotondo: lights, 8 December and markets",
            answer="At Christmas the old town of Locorotondo fills with lights strung across its white lanes and pointed-roof houses. For 2026 the town council has planned events from 22 November 2026 to 6 January 2027, so the Immaculate Conception holiday (8 December) falls right in the middle. The official programme with times has not been published yet: we will update this page as soon as it is.",
            body="""
<h2>When do the Locorotondo Christmas lights go on in 2026?</h2>
<p>In its notice of 7 September 2026, the Comune di Locorotondo planned the Christmas programme <strong>from about 22 November 2026 to 6 January 2027</strong>. As of 10 November 2026 the exact switch-on date has not been announced: six proposals were submitted and the project is still being chosen.</p>
<p>In recent years the lights have gone on in the second half of November and stayed until early January.</p>
<table class="facts">
<thead><tr><th scope="col">Year</th><th scope="col">Switch-on</th><th scope="col">Until</th></tr></thead>
<tbody>
<tr><th scope="row">2024</th><td>14 November</td><td>early January</td></tr>
<tr><th scope="row">2025</th><td>22 November</td><td>first week of January 2026</td></tr>
<tr><th scope="row">2026</th><td>programme planned from 22 November (date to be confirmed)</td><td>6 January 2027</td></tr>
</tbody>
</table>
{{img:locorotondo/vicolo-luci|A lane in Locorotondo's old town with lights strung overhead}}

<h2>Why visit Locorotondo on 8 December?</h2>
<p>The Immaculate Conception holiday on 8 December is when the lights are all on and the Christmas markets are open. The old town is small and easy to walk: at sunset, when the lights come on against the white façades, it is at its most beautiful.</p>
<p>The rest of the Itria Valley celebrates at the same time: Martina Franca, Alberobello and Cisternino are close by, and you can see two of them in a day.</p>

<h2>Where are the lights in the old town?</h2>
<p>In 2025 the lights started from <strong>Piazza Aldo Moro</strong> and ran along <strong>Via Porta Nuova, Via Morelli, Via Montanaro, Via Bruno and Via Eroi Dogali</strong>, lit every evening from about 5 pm. The 2026 route has not been announced yet.</p>
{{img:locorotondo/via-morelli|Via Morelli in Locorotondo's old town}}
<p>Along the way, stop at the <strong>Mother Church of Saint George the Martyr</strong> with its large dome, and at the viewpoint of the public garden (Villa comunale), which looks out over trulli country.</p>
{{img:locorotondo/san-giorgio|Inside the Mother Church of Saint George in Locorotondo}}

<h2>Are there Christmas markets?</h2>
<p>Yes. In 2025 the markets ran <strong>from 30 November 2025 to 6 January 2026</strong> in Piazza Aldo Moro, the public garden and the streets near the town hall. The 2026 dates are not official yet.</p>

<h2>Planning your visit</h2>
<ul>
<li><strong>When:</strong> arrive in the late afternoon to see the town in daylight and then with the lights on.</li>
<li><strong>Weekends</strong> and the 8 December holiday are busy: pick a weekday if you can.</li>
<li><strong>What to wear:</strong> evenings on the hills are cold and the old town streets are stone.</li>
<li><strong>Where to stay:</strong> Locorotondo borders Martina Franca. Staying in a countryside trullo such as <a href="/en/the-trullo/">Trullo Rosy</a> lets you explore the Itria Valley towns and come back to silence and a fireplace in the evening.</li>
</ul>
{{img:locorotondo/trulli-campagna|Trulli countryside seen from Locorotondo's public garden}}

<h2>Frequently asked questions</h2>
<details><summary>When do the Locorotondo lights start in 2026?</summary><p>The town council has planned the period from 22 November 2026 to 6 January 2027. The exact switch-on date has not been announced yet.</p></details>
<details><summary>Are the lights on for 8 December?</summary><p>Yes: 8 December falls within the planned period, and in recent years the lights were already on from late November.</p></details>
<details><summary>What time do the lights come on?</summary><p>In 2025 the lights came on every evening from about 5 pm. The 2026 times have not been published yet.</p></details>
<details><summary>Where to stay near Locorotondo at Christmas?</summary><p>The countryside between Martina Franca and Locorotondo has trulli for rent, such as Trullo Rosy: an entire trullo with three bedrooms, a fireplace and parking.</p></details>
""",
            faq=[
                ("When do the Locorotondo lights start in 2026?", "The town council has planned the period from 22 November 2026 to 6 January 2027. The exact switch-on date has not been announced yet."),
                ("Are the lights on for 8 December?", "Yes: 8 December falls within the planned period, and in recent years the lights were already on from late November."),
                ("What time do the lights come on?", "In 2025 the lights came on every evening from about 5 pm. The 2026 times have not been published yet."),
                ("Where to stay near Locorotondo at Christmas?", "The countryside between Martina Franca and Locorotondo has trulli for rent, such as Trullo Rosy: an entire trullo with three bedrooms, a fireplace and parking."),
            ],
            cta_h2="Stay in a trullo close to the lights",
            sources_h2="Sources",
            photos_h2="Photos",
            updated="Updated 10 November 2026",
        ),
    },
]
