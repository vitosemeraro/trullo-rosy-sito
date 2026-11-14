"""Guide del sito. Ogni guida ha un testo per lingua (le lingue mancanti non vengono generate).

Corpo in HTML semplice. Le immagini si inseriscono con {{img:cartella/nome|alt}}.
Fonti e date: solo da fonti verificabili, citate in fondo alla guida.
"""

GUIDES = [
    {
        "key": "natale-locorotondo",
        "date": "2026-11-10",
        "modified": "2026-11-13",
        "hero": "locorotondo/tramonto",
        "paths": {"it": "/guide/natale-a-locorotondo/", "en": "/en/guides/christmas-in-locorotondo/",
                  "fr": "/fr/guides/noel-a-locorotondo/", "de": "/de/reisetipps/weihnachten-in-locorotondo/",
                  "nl": "/nl/gidsen/kerst-in-locorotondo/", "es": "/es/guias/navidad-en-locorotondo/"},
        "sources": [
            ("Comune di Locorotondo, avviso \"Natale a Locorotondo 2026\" (7 settembre 2026)",
             "https://www.comune.locorotondo.ba.it/it/news/natale-a-locorotondo-2026-avviso-pubblico-per-la-presentazione-di-proposte-progettuali"),
            ("Agorà Blog, \"Natale 2026 a Locorotondo: all'avviso pubblico giungono 6 proposte\" (2 ottobre 2026)",
             "https://agorablog.it/ultime-news/natale-2026-a-locorotondo-allavviso-pubblico-giungono-6-proposte/"),
            ("Comune di Locorotondo, avviso sponsorizzazione \"Luci di Natale a Locorotondo 2026 – Le avventure di Pinocchio\" (5 novembre 2026)",
             "https://www.comune.locorotondo.ba.it/it/news"),
            ("regionepuglia.org, \"Natale a Locorotondo\" (aggiornato al 10 novembre 2026)",
             "https://www.regionepuglia.org/natale-locorotondo/"),
        ],
        "it": dict(
            title="Mercatini di Natale a Locorotondo 2026 e luminarie",
            desc="Mercatini di Natale e luminarie a Locorotondo 2026: periodo indicato dal Comune, dove vederli, il ponte dell'Immacolata e dove dormire in un trullo.",
            h1="Mercatini e luminarie di Natale a Locorotondo 2026",
            answer="A Natale il centro storico di Locorotondo si riempie di luminarie e, come nel 2025, dei mercatini di Natale, tra i vicoli bianchi e le case con i tetti a punta. Per il 2026 il Comune ha indicato un programma dal 22 novembre 2026 al 6 gennaio 2027, quindi il ponte dell'Immacolata (8 dicembre) cade in pieno periodo di luci. Date dei mercatini e orari ufficiali non sono ancora usciti: aggiorneremo questa pagina appena il Comune li pubblica.",
            body="""
<h2>Quando si accendono le luminarie di Locorotondo nel 2026?</h2>
<p>Il Comune di Locorotondo, con l'avviso pubblicato il 7 settembre 2026, ha previsto le iniziative di Natale <strong>indicativamente dal 22 novembre 2026 al 6 gennaio 2027</strong>. Il 5 novembre 2026 il Comune ha aperto la ricerca di sponsor per le <strong>"Luci di Natale a Locorotondo 2026 – Le avventure di Pinocchio"</strong> (domande fino al 16 novembre): il tema dell'edizione 2026 è quindi Pinocchio. Ad oggi (13 novembre 2026) la data esatta dell'accensione, gli orari e il percorso non sono ancora stati annunciati.</p>
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
<p>Il resto della Valle d'Itria fa festa nello stesso periodo: Martina Franca, Alberobello e Cisternino sono vicini, e in una giornata se ne possono vedere due. Date e luoghi paese per paese sono nella guida <a href="/guide/mercatini-di-natale-in-puglia/">Mercatini di Natale in Puglia</a>.</p>

<h2>Dove sono le luci nel centro storico?</h2>
<p>Nel 2025 il percorso delle luminarie partiva da <strong>piazza Aldo Moro</strong> e attraversava <strong>via Porta Nuova, via Morelli, via Montanaro, via Bruno e via Eroi Dogali</strong>, con le luci accese ogni sera dalle 17 circa. Il percorso del 2026 non è ancora stato annunciato.</p>
{{img:locorotondo/via-morelli|Via Morelli, nel centro storico di Locorotondo}}
<p>Lungo la strada vale una sosta la <strong>Chiesa Madre di San Giorgio Martire</strong>, con la sua grande cupola, e il belvedere della villa comunale, che guarda sulla campagna dei trulli. Tutte le tappe del centro storico sono nella guida <a href="/guide/cosa-vedere-a-locorotondo/">cosa vedere a Locorotondo</a>.</p>
{{img:locorotondo/san-giorgio|L'interno della Chiesa Madre di San Giorgio a Locorotondo}}

<h2>Quando ci sono i mercatini di Natale a Locorotondo nel 2026?</h2>
<p>Ad oggi (13 novembre 2026) il Comune non ha ancora pubblicato le date dei mercatini di Natale 2026: il periodo indicato per tutte le iniziative di Natale va dal 22 novembre 2026 al 6 gennaio 2027. Aggiorneremo questa pagina appena escono le date ufficiali.</p>
<p>Nel 2025 i mercatini sono stati aperti <strong>dal 30 novembre 2025 al 6 gennaio 2026</strong> in piazza Aldo Moro, nella villa comunale e nelle vie vicino al Municipio.</p>

<h2>Come organizzare la visita</h2>
<ul>
<li><strong>Quando:</strong> arriva nel tardo pomeriggio, così vedi il paese con la luce del giorno e poi con le luminarie accese.</li>
<li><strong>Nei weekend</strong> e al ponte dell'Immacolata c'è molta gente: se puoi, scegli un giorno feriale.</li>
<li><strong>Abbigliamento:</strong> la sera in collina fa freddo, e le strade del centro sono in pietra.</li>
<li><strong>Dove dormire:</strong> Locorotondo confina con Martina Franca. Dormire in un trullo in campagna, come <a href="/il-trullo/">Trullo Rosy</a>, ti permette di girare i paesi della Valle d'Itria e tornare la sera nel silenzio, davanti al camino. Tutte le informazioni per prenotare sono nella pagina del nostro <a href="/">trullo in affitto a Martina Franca</a>.</li>
</ul>
{{img:locorotondo/trulli-campagna|La campagna dei trulli vista dalla villa comunale di Locorotondo}}

<h2>Domande frequenti</h2>
<details><summary>Quando iniziano le luminarie di Locorotondo nel 2026?</summary><p>Il Comune ha indicato il periodo dal 22 novembre 2026 al 6 gennaio 2027. La data esatta dell'accensione non è ancora stata annunciata.</p></details>
<details><summary>Quando aprono i mercatini di Natale di Locorotondo nel 2026?</summary><p>Le date ufficiali non sono ancora uscite. Il Comune ha indicato per le iniziative di Natale il periodo dal 22 novembre 2026 al 6 gennaio 2027; nel 2025 i mercatini sono stati aperti dal 30 novembre al 6 gennaio.</p></details>
<details><summary>Le luci sono accese all'Immacolata?</summary><p>Sì: l'8 dicembre cade dentro il periodo indicato dal Comune, e negli ultimi anni le luci erano già accese da fine novembre.</p></details>
<details><summary>A che ora si accendono le luci?</summary><p>Nel 2025 le luci si accendevano ogni sera dalle 17 circa. Gli orari del 2026 non sono ancora stati pubblicati.</p></details>
<details><summary>Dove dormire vicino a Locorotondo a Natale?</summary><p>Nella campagna tra Martina Franca e Locorotondo ci sono trulli in affitto, come Trullo Rosy: un trullo intero con tre camere, camino e parcheggio.</p></details>
""",
            faq=[
                ("Quando iniziano le luminarie di Locorotondo nel 2026?", "Il Comune ha indicato il periodo dal 22 novembre 2026 al 6 gennaio 2027. La data esatta dell'accensione non è ancora stata annunciata."),
                ("Quando aprono i mercatini di Natale di Locorotondo nel 2026?", "Le date ufficiali non sono ancora uscite. Il Comune ha indicato per le iniziative di Natale il periodo dal 22 novembre 2026 al 6 gennaio 2027; nel 2025 i mercatini sono stati aperti dal 30 novembre al 6 gennaio."),
                ("Le luci sono accese all'Immacolata?", "Sì: l'8 dicembre cade dentro il periodo indicato dal Comune, e negli ultimi anni le luci erano già accese da fine novembre."),
                ("A che ora si accendono le luci?", "Nel 2025 le luci si accendevano ogni sera dalle 17 circa. Gli orari del 2026 non sono ancora stati pubblicati."),
                ("Dove dormire vicino a Locorotondo a Natale?", "Nella campagna tra Martina Franca e Locorotondo ci sono trulli in affitto, come Trullo Rosy: un trullo intero con tre camere, camino e parcheggio."),
            ],
            cta_h2="Dormi in un trullo a pochi passi dalle luci",
            sources_h2="Fonti",
            photos_h2="Foto",
            updated="Aggiornato il 13 novembre 2026",
        ),
        "en": dict(
            title="Christmas markets in Locorotondo 2026: lights, dates",
            desc="Christmas and the Immaculate Conception holiday in Locorotondo, Puglia: when the lights go on, where to see them, markets, and where to stay in a trullo.",
            h1="Christmas in Locorotondo: lights, 8 December and markets",
            answer="At Christmas the old town of Locorotondo fills with lights strung across its white lanes and pointed-roof houses. For 2026 the town council has planned events from 22 November 2026 to 6 January 2027, so the Immaculate Conception holiday (8 December) falls right in the middle. The official programme with times has not been published yet: we will update this page as soon as it is.",
            body="""
<h2>When do the Locorotondo Christmas lights go on in 2026?</h2>
<p>In its notice of 7 September 2026, the Comune di Locorotondo planned the Christmas programme <strong>from about 22 November 2026 to 6 January 2027</strong>. On 5 November 2026 the Comune opened a call for sponsors of <strong>"Luci di Natale a Locorotondo 2026 – Le avventure di Pinocchio"</strong> (applications until 16 November), so this year's theme is Pinocchio. As of 13 November 2026 the exact switch-on date, times and route have not been announced yet.</p>
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
<p>The rest of the Itria Valley celebrates at the same time: Martina Franca, Alberobello and Cisternino are close by, and you can see two of them in a day. Dates and places town by town are in our guide <a href="/en/guides/christmas-markets-in-puglia/">Christmas markets in Puglia</a>.</p>

<h2>Where are the lights in the old town?</h2>
<p>In 2025 the lights started from <strong>Piazza Aldo Moro</strong> and ran along <strong>Via Porta Nuova, Via Morelli, Via Montanaro, Via Bruno and Via Eroi Dogali</strong>, lit every evening from about 5 pm. The 2026 route has not been announced yet.</p>
{{img:locorotondo/via-morelli|Via Morelli in Locorotondo's old town}}
<p>Along the way, stop at the <strong>Mother Church of Saint George the Martyr</strong> with its large dome, and at the viewpoint of the public garden (Villa comunale), which looks out over trulli country. All the stops in the old town are in our guide <a href="/en/guides/what-to-see-in-locorotondo/">what to see in Locorotondo</a>.</p>
{{img:locorotondo/san-giorgio|Inside the Mother Church of Saint George in Locorotondo}}

<h2>Are there Christmas markets?</h2>
<p>Yes. In 2025 the markets ran <strong>from 30 November 2025 to 6 January 2026</strong> in Piazza Aldo Moro, the public garden and the streets near the town hall. The 2026 dates are not official yet.</p>

<h2>Planning your visit</h2>
<ul>
<li><strong>When:</strong> arrive in the late afternoon to see the town in daylight and then with the lights on.</li>
<li><strong>Weekends</strong> and the 8 December holiday are busy: pick a weekday if you can.</li>
<li><strong>What to wear:</strong> evenings on the hills are cold and the old town streets are stone.</li>
<li><strong>Where to stay:</strong> Locorotondo borders Martina Franca. Staying in a countryside trullo such as <a href="/en/the-trullo/">Trullo Rosy</a> lets you explore the Itria Valley towns and come back to silence and a fireplace in the evening. Everything you need to book is on the page of our <a href="/en/">trullo for rent in Martina Franca</a>.</li>
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
            updated="Updated 13 November 2026",
        ),
        "fr": dict(
            title="Noël à Locorotondo 2026 : illuminations et dates",
            desc="Noël et le pont de l'Immaculée Conception à Locorotondo, dans les Pouilles : dates des illuminations, marchés de Noël et où dormir dans un trullo.",
            h1="Noël à Locorotondo : illuminations, 8 décembre et marchés",
            answer="À Noël, le centre historique de Locorotondo se remplit d'illuminations entre ses ruelles blanches et ses maisons aux toits pointus. Pour 2026, la commune a prévu un programme du 22 novembre 2026 au 6 janvier 2027 : le pont de l'Immaculée Conception (8 décembre) tombe donc en pleine période des lumières. Le programme officiel avec les horaires n'est pas encore publié : nous mettrons cette page à jour dès sa sortie.",
            body="""
<h2>Quand s'allument les illuminations de Locorotondo en 2026 ?</h2>
<p>Dans son avis du 7 septembre 2026, la Commune de Locorotondo a prévu les animations de Noël <strong>du 22 novembre 2026 environ au 6 janvier 2027</strong>. Le 5 novembre 2026, la Commune a lancé un appel à sponsors pour les <strong>« Luci di Natale a Locorotondo 2026 – Le avventure di Pinocchio »</strong> (candidatures jusqu'au 16 novembre) : le thème de cette édition est donc Pinocchio. Au 13 novembre 2026, la date exacte de l'allumage, les horaires et le parcours n'ont pas encore été annoncés.</p>
<p>Ces dernières années, les lumières se sont allumées dans la seconde moitié de novembre et sont restées jusqu'aux premiers jours de janvier.</p>
<table class="facts">
<thead><tr><th scope="col">Année</th><th scope="col">Allumage</th><th scope="col">Jusqu'au</th></tr></thead>
<tbody>
<tr><th scope="row">2024</th><td>14 novembre</td><td>début janvier</td></tr>
<tr><th scope="row">2025</th><td>22 novembre</td><td>première semaine de janvier 2026</td></tr>
<tr><th scope="row">2026</th><td>programme prévu à partir du 22 novembre (date à confirmer)</td><td>6 janvier 2027</td></tr>
</tbody>
</table>
{{img:locorotondo/vicolo-luci|Une ruelle du centre historique de Locorotondo sous les lumières suspendues}}

<h2>Pourquoi aller à Locorotondo le 8 décembre ?</h2>
<p>Le 8 décembre, fête de l'Immaculée Conception, et le pont qui l'accompagne sont le moment où toutes les illuminations sont allumées et où les marchés de Noël sont ouverts. Le centre historique est petit et se visite à pied : au coucher du soleil, quand les lumières s'allument sur les façades blanches, c'est le plus beau moment pour une promenade.</p>
<p>Le reste de la vallée d'Itria fait la fête à la même période : Martina Franca, Alberobello et Cisternino sont tout proches, et on peut en voir deux dans la même journée.</p>

<h2>Où sont les lumières dans le centre historique ?</h2>
<p>En 2025, le parcours des illuminations partait de la <strong>piazza Aldo Moro</strong> et traversait la <strong>via Porta Nuova, la via Morelli, la via Montanaro, la via Bruno et la via Eroi Dogali</strong>, avec les lumières allumées chaque soir à partir de 17 h environ. Le parcours 2026 n'a pas encore été annoncé.</p>
{{img:locorotondo/via-morelli|La via Morelli, dans le centre historique de Locorotondo}}
<p>En chemin, arrêtez-vous à l'<strong>église mère Saint-Georges-Martyr</strong> (Chiesa Madre di San Giorgio Martire), avec sa grande coupole, et au belvédère du jardin public (villa comunale), qui donne sur la campagne des trulli.</p>
{{img:locorotondo/san-giorgio|L'intérieur de l'église mère Saint-Georges à Locorotondo}}

<h2>Y a-t-il des marchés de Noël ?</h2>
<p>Oui. En 2025, les marchés ont été ouverts <strong>du 30 novembre 2025 au 6 janvier 2026</strong> sur la piazza Aldo Moro, dans le jardin public et dans les rues proches de la mairie. Les dates 2026 ne sont pas encore officielles.</p>

<h2>Comment organiser la visite ?</h2>
<ul>
<li><strong>Quand :</strong> arrivez en fin d'après-midi pour voir le village à la lumière du jour, puis avec les illuminations allumées.</li>
<li><strong>Le week-end</strong> et au pont du 8 décembre, il y a beaucoup de monde : si vous le pouvez, choisissez un jour de semaine.</li>
<li><strong>Tenue :</strong> le soir, il fait froid sur les collines et les rues du centre sont pavées de pierre.</li>
<li><strong>Où dormir :</strong> Locorotondo est voisine de Martina Franca. Dormir dans un trullo à la campagne, comme <a href="/fr/le-trullo/">Trullo Rosy</a>, permet de visiter les villages de la vallée d'Itria et de retrouver le soir le calme, devant la cheminée.</li>
</ul>
{{img:locorotondo/trulli-campagna|La campagne des trulli vue depuis le jardin public de Locorotondo}}

<h2>Questions fréquentes</h2>
<details><summary>Quand commencent les illuminations de Locorotondo en 2026 ?</summary><p>La commune a prévu la période du 22 novembre 2026 au 6 janvier 2027. La date exacte de l'allumage n'a pas encore été annoncée.</p></details>
<details><summary>Les lumières sont-elles allumées le 8 décembre ?</summary><p>Oui : le 8 décembre tombe dans la période prévue par la commune, et ces dernières années les lumières étaient déjà allumées dès la fin novembre.</p></details>
<details><summary>À quelle heure s'allument les lumières ?</summary><p>En 2025, les lumières s'allumaient chaque soir à partir de 17 h environ. Les horaires 2026 n'ont pas encore été publiés.</p></details>
<details><summary>Où dormir près de Locorotondo à Noël ?</summary><p>Dans la campagne entre Martina Franca et Locorotondo, il y a des trulli à louer, comme Trullo Rosy : un trullo entier avec trois chambres, une cheminée et un parking.</p></details>
""",
            faq=[
                ("Quand commencent les illuminations de Locorotondo en 2026 ?", "La commune a prévu la période du 22 novembre 2026 au 6 janvier 2027. La date exacte de l'allumage n'a pas encore été annoncée."),
                ("Les lumières sont-elles allumées le 8 décembre ?", "Oui : le 8 décembre tombe dans la période prévue par la commune, et ces dernières années les lumières étaient déjà allumées dès la fin novembre."),
                ("À quelle heure s'allument les lumières ?", "En 2025, les lumières s'allumaient chaque soir à partir de 17 h environ. Les horaires 2026 n'ont pas encore été publiés."),
                ("Où dormir près de Locorotondo à Noël ?", "Dans la campagne entre Martina Franca et Locorotondo, il y a des trulli à louer, comme Trullo Rosy : un trullo entier avec trois chambres, une cheminée et un parking."),
            ],
            cta_h2="Dormez dans un trullo tout près des lumières",
            sources_h2="Sources",
            photos_h2="Photos",
            updated="Mis à jour le 13 novembre 2026",
        ),
        "de": dict(
            title="Weihnachten in Locorotondo 2026: Lichter und Termine",
            desc="Weihnachten und Mariä Empfängnis in Locorotondo, Apulien: wann die Lichter angehen, wo man sie sieht, Weihnachtsmärkte und Übernachten im Trullo.",
            h1="Weihnachten in Locorotondo: Lichter, 8. Dezember und Märkte",
            answer="An Weihnachten füllt sich die Altstadt von Locorotondo mit Lichtern zwischen den weißen Gassen und den Häusern mit spitzen Dächern. Für 2026 hat die Gemeinde ein Programm vom 22. November 2026 bis 6. Januar 2027 vorgesehen, der Feiertag Mariä Empfängnis (8. Dezember) liegt also mitten in der Lichterzeit. Das offizielle Programm mit Uhrzeiten ist noch nicht veröffentlicht: Wir aktualisieren diese Seite, sobald es erscheint.",
            body="""
<h2>Wann gehen die Weihnachtslichter in Locorotondo 2026 an?</h2>
<p>In ihrer Bekanntmachung vom 7. September 2026 hat die Gemeinde Locorotondo das Weihnachtsprogramm <strong>etwa vom 22. November 2026 bis 6. Januar 2027</strong> geplant. Am 5. November 2026 hat die Gemeinde Sponsoren für die <strong>„Luci di Natale a Locorotondo 2026 – Le avventure di Pinocchio“</strong> gesucht (Bewerbungen bis 16. November): Das Thema 2026 ist also Pinocchio. Stand 13. November 2026 sind das genaue Datum der Einschaltung, die Uhrzeiten und der Rundgang noch nicht bekannt gegeben.</p>
<p>In den letzten Jahren gingen die Lichter in der zweiten Novemberhälfte an und blieben bis Anfang Januar.</p>
<table class="facts">
<thead><tr><th scope="col">Jahr</th><th scope="col">Einschaltung</th><th scope="col">Bis</th></tr></thead>
<tbody>
<tr><th scope="row">2024</th><td>14. November</td><td>Anfang Januar</td></tr>
<tr><th scope="row">2025</th><td>22. November</td><td>erste Januarwoche 2026</td></tr>
<tr><th scope="row">2026</th><td>Programm ab 22. November geplant (Datum noch offen)</td><td>6. Januar 2027</td></tr>
</tbody>
</table>
{{img:locorotondo/vicolo-luci|Eine Gasse in der Altstadt von Locorotondo mit aufgehängten Lichtern}}

<h2>Warum am 8. Dezember nach Locorotondo?</h2>
<p>Am 8. Dezember, dem Feiertag Mariä Empfängnis, und am langen Wochenende rund um diesen Tag sind alle Lichter an und die Weihnachtsmärkte geöffnet. Die Altstadt ist klein und lässt sich zu Fuß erkunden: Bei Sonnenuntergang, wenn die Lichter auf den weißen Fassaden angehen, ist der schönste Moment für einen Spaziergang.</p>
<p>Das übrige Itria-Tal feiert zur selben Zeit: Martina Franca, Alberobello und Cisternino liegen ganz in der Nähe, an einem Tag schafft man zwei davon.</p>

<h2>Wo sind die Lichter in der Altstadt?</h2>
<p>2025 begann der Lichterweg an der <strong>Piazza Aldo Moro</strong> und führte durch <strong>Via Porta Nuova, Via Morelli, Via Montanaro, Via Bruno und Via Eroi Dogali</strong>; die Lichter brannten jeden Abend ab etwa 17 Uhr. Der Weg für 2026 ist noch nicht bekannt gegeben.</p>
{{img:locorotondo/via-morelli|Die Via Morelli in der Altstadt von Locorotondo}}
<p>Unterwegs lohnt sich ein Halt an der <strong>Mutterkirche San Giorgio Martire</strong> mit ihrer großen Kuppel und am Aussichtspunkt des Stadtparks (Villa comunale), der über die Trulli-Landschaft blickt.</p>
{{img:locorotondo/san-giorgio|Das Innere der Mutterkirche San Giorgio in Locorotondo}}

<h2>Gibt es Weihnachtsmärkte?</h2>
<p>Ja. 2025 waren die Märkte <strong>vom 30. November 2025 bis 6. Januar 2026</strong> auf der Piazza Aldo Moro, im Stadtpark und in den Straßen beim Rathaus geöffnet. Die Termine 2026 sind noch nicht offiziell.</p>

<h2>Wie plant man den Besuch?</h2>
<ul>
<li><strong>Wann:</strong> Komm am späten Nachmittag, dann siehst du den Ort bei Tageslicht und danach mit den Lichtern.</li>
<li><strong>An Wochenenden</strong> und am langen Wochenende um den 8. Dezember ist viel los: Wähle wenn möglich einen Wochentag.</li>
<li><strong>Kleidung:</strong> Abends ist es auf den Hügeln kalt, und die Straßen der Altstadt sind aus Stein.</li>
<li><strong>Übernachten:</strong> Locorotondo grenzt an Martina Franca. In einem Trullo auf dem Land wie <a href="/de/der-trullo/">Trullo Rosy</a> kannst du die Orte des Itria-Tals besuchen und abends in die Ruhe vor dem Kamin zurückkehren.</li>
</ul>
{{img:locorotondo/trulli-campagna|Die Trulli-Landschaft vom Stadtpark in Locorotondo aus gesehen}}

<h2>Häufige Fragen</h2>
<details><summary>Wann beginnen die Lichter in Locorotondo 2026?</summary><p>Die Gemeinde hat den Zeitraum vom 22. November 2026 bis 6. Januar 2027 geplant. Das genaue Datum der Einschaltung ist noch nicht bekannt gegeben.</p></details>
<details><summary>Sind die Lichter am 8. Dezember an?</summary><p>Ja: Der 8. Dezember liegt im von der Gemeinde geplanten Zeitraum, und in den letzten Jahren waren die Lichter schon ab Ende November an.</p></details>
<details><summary>Um wie viel Uhr gehen die Lichter an?</summary><p>2025 gingen die Lichter jeden Abend ab etwa 17 Uhr an. Die Zeiten für 2026 sind noch nicht veröffentlicht.</p></details>
<details><summary>Wo übernachten in der Nähe von Locorotondo an Weihnachten?</summary><p>Auf dem Land zwischen Martina Franca und Locorotondo gibt es Trulli zur Miete, zum Beispiel Trullo Rosy: ein ganzer Trullo mit drei Schlafzimmern, Kamin und Parkplatz.</p></details>
""",
            faq=[
                ("Wann beginnen die Lichter in Locorotondo 2026?", "Die Gemeinde hat den Zeitraum vom 22. November 2026 bis 6. Januar 2027 geplant. Das genaue Datum der Einschaltung ist noch nicht bekannt gegeben."),
                ("Sind die Lichter am 8. Dezember an?", "Ja: Der 8. Dezember liegt im von der Gemeinde geplanten Zeitraum, und in den letzten Jahren waren die Lichter schon ab Ende November an."),
                ("Um wie viel Uhr gehen die Lichter an?", "2025 gingen die Lichter jeden Abend ab etwa 17 Uhr an. Die Zeiten für 2026 sind noch nicht veröffentlicht."),
                ("Wo übernachten in der Nähe von Locorotondo an Weihnachten?", "Auf dem Land zwischen Martina Franca und Locorotondo gibt es Trulli zur Miete, zum Beispiel Trullo Rosy: ein ganzer Trullo mit drei Schlafzimmern, Kamin und Parkplatz."),
            ],
            cta_h2="Übernachte in einem Trullo nahe den Lichtern",
            sources_h2="Quellen",
            photos_h2="Fotos",
            updated="Aktualisiert am 13. November 2026",
        ),
        "nl": dict(
            title="Kerst in Locorotondo 2026: verlichting en data",
            desc="Kerst en Maria-Onbevlekte-Ontvangenis in Locorotondo, Apulië: wanneer de verlichting aangaat, waar je die ziet, kerstmarkten en slapen in een trullo.",
            h1="Kerst in Locorotondo: verlichting, 8 december en markten",
            answer="Met Kerst vult het historische centrum van Locorotondo zich met lichtjes tussen de witte steegjes en de huizen met puntdaken. Voor 2026 heeft de gemeente een programma gepland van 22 november 2026 tot 6 januari 2027, dus de feestdag van Maria Onbevlekte Ontvangenis (8 december) valt midden in de lichtjesperiode. Het officiële programma met tijden is nog niet gepubliceerd: we werken deze pagina bij zodra het verschijnt.",
            body="""
<h2>Wanneer gaat de kerstverlichting in Locorotondo in 2026 aan?</h2>
<p>In haar bekendmaking van 7 september 2026 heeft de gemeente Locorotondo het kerstprogramma gepland <strong>van ongeveer 22 november 2026 tot 6 januari 2027</strong>. Op 5 november 2026 zocht de gemeente sponsors voor de <strong>“Luci di Natale a Locorotondo 2026 – Le avventure di Pinocchio”</strong> (aanmelden tot 16 november): het thema van 2026 is dus Pinokkio. Op 13 november 2026 zijn de exacte datum van het aangaan, de tijden en de route nog niet bekendgemaakt.</p>
<p>De afgelopen jaren ging de verlichting aan in de tweede helft van november en bleef ze tot begin januari.</p>
<table class="facts">
<thead><tr><th scope="col">Jaar</th><th scope="col">Aangaan</th><th scope="col">Tot</th></tr></thead>
<tbody>
<tr><th scope="row">2024</th><td>14 november</td><td>begin januari</td></tr>
<tr><th scope="row">2025</th><td>22 november</td><td>eerste week van januari 2026</td></tr>
<tr><th scope="row">2026</th><td>programma gepland vanaf 22 november (datum nog te bevestigen)</td><td>6 januari 2027</td></tr>
</tbody>
</table>
{{img:locorotondo/vicolo-luci|Een steegje in het historische centrum van Locorotondo met lichtjes erboven}}

<h2>Waarom op 8 december naar Locorotondo?</h2>
<p>Op 8 december, de feestdag van Maria Onbevlekte Ontvangenis, en in het lange weekend eromheen is alle verlichting aan en zijn de kerstmarkten open. Het historische centrum is klein en goed te voet te doen: bij zonsondergang, als de lichtjes aangaan op de witte gevels, is het mooiste moment voor een wandeling.</p>
<p>De rest van het Itria-dal viert in dezelfde periode feest: Martina Franca, Alberobello en Cisternino liggen vlakbij, en op één dag zie je er twee.</p>

<h2>Waar is de verlichting in het historische centrum?</h2>
<p>In 2025 begon de route van de verlichting op de <strong>Piazza Aldo Moro</strong> en liep door de <strong>Via Porta Nuova, Via Morelli, Via Montanaro, Via Bruno en Via Eroi Dogali</strong>, met de lichtjes elke avond aan vanaf ongeveer 17.00 uur. De route van 2026 is nog niet bekendgemaakt.</p>
{{img:locorotondo/via-morelli|De Via Morelli in het historische centrum van Locorotondo}}
<p>Onderweg is een stop de moeite waard bij de <strong>moederkerk San Giorgio Martire</strong> met haar grote koepel, en bij het uitzichtpunt van het stadspark (Villa comunale), dat uitkijkt over het land van de trulli.</p>
{{img:locorotondo/san-giorgio|Het interieur van de moederkerk San Giorgio in Locorotondo}}

<h2>Zijn er kerstmarkten?</h2>
<p>Ja. In 2025 waren de markten open <strong>van 30 november 2025 tot 6 januari 2026</strong> op de Piazza Aldo Moro, in het stadspark en in de straten bij het gemeentehuis. De data voor 2026 zijn nog niet officieel.</p>

<h2>Hoe plan je je bezoek?</h2>
<ul>
<li><strong>Wanneer:</strong> kom aan het eind van de middag, dan zie je het dorp bij daglicht en daarna met de verlichting aan.</li>
<li><strong>In het weekend</strong> en rond 8 december is het druk: kies als het kan een doordeweekse dag.</li>
<li><strong>Kleding:</strong> 's avonds is het koud op de heuvels, en de straten in het centrum zijn van steen.</li>
<li><strong>Waar slapen:</strong> Locorotondo grenst aan Martina Franca. In een trullo op het platteland, zoals <a href="/nl/de-trullo/">Trullo Rosy</a>, bezoek je de dorpen van het Itria-dal en keer je 's avonds terug naar de rust bij de open haard.</li>
</ul>
{{img:locorotondo/trulli-campagna|Het land van de trulli gezien vanuit het stadspark van Locorotondo}}

<h2>Veelgestelde vragen</h2>
<details><summary>Wanneer begint de verlichting in Locorotondo in 2026?</summary><p>De gemeente heeft de periode van 22 november 2026 tot 6 januari 2027 gepland. De exacte datum van het aangaan is nog niet bekendgemaakt.</p></details>
<details><summary>Is de verlichting aan op 8 december?</summary><p>Ja: 8 december valt binnen de door de gemeente geplande periode, en de afgelopen jaren was de verlichting al vanaf eind november aan.</p></details>
<details><summary>Hoe laat gaat de verlichting aan?</summary><p>In 2025 ging de verlichting elke avond aan vanaf ongeveer 17.00 uur. De tijden voor 2026 zijn nog niet gepubliceerd.</p></details>
<details><summary>Waar slapen in de buurt van Locorotondo met Kerst?</summary><p>Op het platteland tussen Martina Franca en Locorotondo zijn trulli te huur, zoals Trullo Rosy: een hele trullo met drie slaapkamers, open haard en parkeerplaats.</p></details>
""",
            faq=[
                ("Wanneer begint de verlichting in Locorotondo in 2026?", "De gemeente heeft de periode van 22 november 2026 tot 6 januari 2027 gepland. De exacte datum van het aangaan is nog niet bekendgemaakt."),
                ("Is de verlichting aan op 8 december?", "Ja: 8 december valt binnen de door de gemeente geplande periode, en de afgelopen jaren was de verlichting al vanaf eind november aan."),
                ("Hoe laat gaat de verlichting aan?", "In 2025 ging de verlichting elke avond aan vanaf ongeveer 17.00 uur. De tijden voor 2026 zijn nog niet gepubliceerd."),
                ("Waar slapen in de buurt van Locorotondo met Kerst?", "Op het platteland tussen Martina Franca en Locorotondo zijn trulli te huur, zoals Trullo Rosy: een hele trullo met drie slaapkamers, open haard en parkeerplaats."),
            ],
            cta_h2="Slaap in een trullo vlak bij de lichtjes",
            sources_h2="Bronnen",
            photos_h2="Foto's",
            updated="Bijgewerkt op 13 november 2026",
        ),
        "es": dict(
            title="Navidad en Locorotondo 2026: luces y fechas",
            desc="Navidad y el puente de la Inmaculada en Locorotondo, Apulia: cuándo se encienden las luces, dónde verlas, mercadillos y dónde dormir en un trullo.",
            h1="Navidad en Locorotondo: luces, 8 de diciembre y mercadillos",
            answer="En Navidad el casco antiguo de Locorotondo se llena de luces entre sus callejuelas blancas y sus casas de tejado puntiagudo. Para 2026 el Ayuntamiento ha previsto un programa del 22 de noviembre de 2026 al 6 de enero de 2027, así que el puente de la Inmaculada (8 de diciembre) cae en plena temporada de luces. El programa oficial con horarios aún no se ha publicado: actualizaremos esta página en cuanto salga.",
            body="""
<h2>¿Cuándo se encienden las luces de Navidad de Locorotondo en 2026?</h2>
<p>En su aviso del 7 de septiembre de 2026, el Ayuntamiento de Locorotondo previó las actividades de Navidad <strong>aproximadamente del 22 de noviembre de 2026 al 6 de enero de 2027</strong>. El 5 de noviembre de 2026 el Ayuntamiento abrió la búsqueda de patrocinadores para las <strong>«Luci di Natale a Locorotondo 2026 – Le avventure di Pinocchio»</strong> (solicitudes hasta el 16 de noviembre): el tema de 2026 es, por tanto, Pinocho. A 13 de noviembre de 2026 todavía no se han anunciado la fecha exacta del encendido, los horarios ni el recorrido.</p>
<p>En los últimos años las luces se han encendido en la segunda mitad de noviembre y han durado hasta los primeros días de enero.</p>
<table class="facts">
<thead><tr><th scope="col">Año</th><th scope="col">Encendido</th><th scope="col">Hasta</th></tr></thead>
<tbody>
<tr><th scope="row">2024</th><td>14 de noviembre</td><td>principios de enero</td></tr>
<tr><th scope="row">2025</th><td>22 de noviembre</td><td>primera semana de enero de 2026</td></tr>
<tr><th scope="row">2026</th><td>programa previsto desde el 22 de noviembre (fecha por confirmar)</td><td>6 de enero de 2027</td></tr>
</tbody>
</table>
{{img:locorotondo/vicolo-luci|Una callejuela del casco antiguo de Locorotondo con luces colgadas}}

<h2>¿Por qué ir a Locorotondo el 8 de diciembre?</h2>
<p>El 8 de diciembre, fiesta de la Inmaculada, y el puente que lo acompaña son el momento en que todas las luces están encendidas y los mercadillos de Navidad abiertos. El casco antiguo es pequeño y se recorre a pie: al atardecer, cuando las luces se encienden sobre las fachadas blancas, es el mejor momento para pasear.</p>
<p>El resto del valle de Itria celebra en las mismas fechas: Martina Franca, Alberobello y Cisternino están muy cerca, y en un día se pueden ver dos.</p>

<h2>¿Dónde están las luces en el casco antiguo?</h2>
<p>En 2025 el recorrido de las luces salía de la <strong>piazza Aldo Moro</strong> y atravesaba <strong>via Porta Nuova, via Morelli, via Montanaro, via Bruno y via Eroi Dogali</strong>, con las luces encendidas cada tarde desde las 17:00 aproximadamente. El recorrido de 2026 aún no se ha anunciado.</p>
{{img:locorotondo/via-morelli|Via Morelli, en el casco antiguo de Locorotondo}}
<p>Por el camino merece una parada la <strong>iglesia madre de San Jorge Mártir</strong> (Chiesa Madre di San Giorgio Martire), con su gran cúpula, y el mirador del jardín público (villa comunale), que da a la campiña de los trulli.</p>
{{img:locorotondo/san-giorgio|El interior de la iglesia madre de San Jorge en Locorotondo}}

<h2>¿Hay mercadillos de Navidad?</h2>
<p>Sí. En 2025 los mercadillos estuvieron abiertos <strong>del 30 de noviembre de 2025 al 6 de enero de 2026</strong> en la piazza Aldo Moro, en el jardín público y en las calles cercanas al Ayuntamiento. Las fechas de 2026 aún no son oficiales.</p>

<h2>¿Cómo organizar la visita?</h2>
<ul>
<li><strong>Cuándo:</strong> llega a última hora de la tarde para ver el pueblo con luz de día y después con las luces encendidas.</li>
<li><strong>Los fines de semana</strong> y en el puente de la Inmaculada hay mucha gente: si puedes, elige un día laborable.</li>
<li><strong>Ropa:</strong> por la noche hace frío en las colinas y las calles del centro son de piedra.</li>
<li><strong>Dónde dormir:</strong> Locorotondo linda con Martina Franca. Dormir en un trullo en el campo, como <a href="/es/el-trullo/">Trullo Rosy</a>, te permite recorrer los pueblos del valle de Itria y volver por la noche a la tranquilidad, frente a la chimenea.</li>
</ul>
{{img:locorotondo/trulli-campagna|La campiña de los trulli vista desde el jardín público de Locorotondo}}

<h2>Preguntas frecuentes</h2>
<details><summary>¿Cuándo empiezan las luces de Locorotondo en 2026?</summary><p>El Ayuntamiento ha previsto el periodo del 22 de noviembre de 2026 al 6 de enero de 2027. La fecha exacta del encendido aún no se ha anunciado.</p></details>
<details><summary>¿Están encendidas las luces el 8 de diciembre?</summary><p>Sí: el 8 de diciembre cae dentro del periodo previsto por el Ayuntamiento, y en los últimos años las luces ya estaban encendidas desde finales de noviembre.</p></details>
<details><summary>¿A qué hora se encienden las luces?</summary><p>En 2025 las luces se encendían cada tarde desde las 17:00 aproximadamente. Los horarios de 2026 aún no se han publicado.</p></details>
<details><summary>¿Dónde dormir cerca de Locorotondo en Navidad?</summary><p>En el campo entre Martina Franca y Locorotondo hay trulli en alquiler, como Trullo Rosy: un trullo entero con tres dormitorios, chimenea y aparcamiento.</p></details>
""",
            faq=[
                ("¿Cuándo empiezan las luces de Locorotondo en 2026?", "El Ayuntamiento ha previsto el periodo del 22 de noviembre de 2026 al 6 de enero de 2027. La fecha exacta del encendido aún no se ha anunciado."),
                ("¿Están encendidas las luces el 8 de diciembre?", "Sí: el 8 de diciembre cae dentro del periodo previsto por el Ayuntamiento, y en los últimos años las luces ya estaban encendidas desde finales de noviembre."),
                ("¿A qué hora se encienden las luces?", "En 2025 las luces se encendían cada tarde desde las 17:00 aproximadamente. Los horarios de 2026 aún no se han publicado."),
                ("¿Dónde dormir cerca de Locorotondo en Navidad?", "En el campo entre Martina Franca y Locorotondo hay trulli en alquiler, como Trullo Rosy: un trullo entero con tres dormitorios, chimenea y aparcamiento."),
            ],
            cta_h2="Duerme en un trullo cerca de las luces",
            sources_h2="Fuentes",
            photos_h2="Fotos",
            updated="Actualizado el 13 de noviembre de 2026",
        ),
    },
    {
        "key": "mercatini-natale-puglia",
        "date": "2026-11-13",
        "modified": "2026-11-13",
        "hero": "luoghi/valle-ditria",
        "paths": {"it": "/guide/mercatini-di-natale-in-puglia/", "en": "/en/guides/christmas-markets-in-puglia/"},
        "sources": [
            ("Comune di Locorotondo, avviso \"Natale a Locorotondo 2026\" (7 settembre 2026)",
             "https://www.comune.locorotondo.ba.it/it/news/natale-a-locorotondo-2026-avviso-pubblico-per-la-presentazione-di-proposte-progettuali"),
            ("HelloApulia, \"Mercatini e luci di Natale in Valle d'Itria\" (programma 2025, 26 novembre 2025)",
             "https://www.helloapulia.com/it/blog/mercatini-luci-natale-valle-ditria"),
            ("Salento Prime, \"Mercatini di Natale in Puglia e Salento 2026/2027\" (aggiornato il 3 novembre 2026)",
             "https://salentoprime.com/mercatini-di-natale-puglia-salento/"),
        ],
        "it": dict(
            title="Mercatini di Natale in Puglia 2026: Valle d'Itria",
            desc="Mercatini di Natale in Puglia nella Valle d'Itria: Locorotondo, Alberobello, Martina Franca, Cisternino e Ostuni, con le date 2025 e cosa si sa del 2026.",
            h1="Mercatini di Natale in Puglia: la Valle d'Itria paese per paese",
            answer="I mercatini di Natale più vicini tra loro in Puglia sono nella Valle d'Itria: Locorotondo, Alberobello, Martina Franca, Cisternino e Ostuni. Nel 2025 sono stati aperti da fine novembre o inizio dicembre fino al 6 gennaio. Per il 2026 il solo periodo indicato da un Comune è quello di Locorotondo, dal 22 novembre 2026 al 6 gennaio 2027.",
            body="""
<h2>Quali sono i mercatini di Natale della Valle d'Itria?</h2>
<p>La Valle d'Itria è la zona dei trulli tra le province di Bari, Taranto e Brindisi. A dicembre quasi ogni paese ha luminarie, mercatini o un villaggio di Natale, e le distanze sono brevi: in una giornata se ne vedono due. Qui sotto trovi cosa c'era nel 2025 e cosa si sa ad oggi (13 novembre 2026) dell'edizione 2026.</p>
<table class="facts">
<thead><tr><th scope="col">Paese</th><th scope="col">Cosa c'è</th><th scope="col">Edizione 2025</th><th scope="col">2026</th></tr></thead>
<tbody>
<tr><th scope="row">Locorotondo</th><td>Luminarie e mercatini nel centro storico</td><td>mercatini dal 30 novembre 2025 al 6 gennaio 2026</td><td>periodo indicato dal Comune: 22 novembre 2026 – 6 gennaio 2027</td></tr>
<tr><th scope="row">Alberobello</th><td>Luci tra i trulli e Villaggio di Natale in piazza del Popolo</td><td>villaggio dal 6 dicembre 2025 al 6 gennaio 2026</td><td>da confermare</td></tr>
<tr><th scope="row">Martina Franca</th><td>Villaggio di Babbo Natale e giardino di luci in villa comunale</td><td>luci in villa comunale dal 13 dicembre 2025</td><td>da confermare</td></tr>
<tr><th scope="row">Cisternino</th><td>Presepe vivente nel centro storico</td><td>28 dicembre 2025, 4 e 6 gennaio 2026</td><td>da confermare</td></tr>
<tr><th scope="row">Ostuni</th><td>Mercatino "Zucchero e Cannella"</td><td>dal 6 all'8 dicembre 2025</td><td>programma non ancora pubblicato</td></tr>
</tbody>
</table>
{{img:panorama-valle-itria|Panorama della Valle d'Itria}}

<h2>Cosa c'è a Locorotondo a Natale?</h2>
<p>Locorotondo è il paese più noto per le luci: nel 2025 i mercatini sono stati aperti <strong>dal 30 novembre 2025 al 6 gennaio 2026</strong> in piazza Aldo Moro, nella villa comunale e nelle vie vicino al Municipio. Per il 2026 il Comune ha indicato le iniziative <strong>dal 22 novembre 2026 al 6 gennaio 2027</strong>, con le luci a tema Pinocchio. Date, orari e percorso sono nella nostra guida dedicata: <a href="/guide/natale-a-locorotondo/">Natale a Locorotondo</a>.</p>

<h2>Com'è il Natale ad Alberobello?</h2>
<p>Nel 2025 le luminarie hanno illuminato il Rione Monti e l'Aia Piccola <strong>dal 5 dicembre 2025 al 5 gennaio 2026</strong>, e in piazza del Popolo c'era il Villaggio Enogastronomico di Natale tra i Trulli <strong>dal 6 dicembre 2025 al 6 gennaio 2026</strong>, con la casa di Babbo Natale e la pista di ghiaccio. Il presepe vivente si è tenuto dal 26 al 29 dicembre 2025. Il programma 2026 non è ancora uscito.</p>
{{img:luoghi/alberobello|I trulli di Alberobello}}

<h2>Cosa si trova a Martina Franca?</h2>
<p>Martina Franca, il paese di Trullo Rosy, ha nel centro storico barocco il Villaggio di Babbo Natale. Nel 2025 la villa comunale è diventata un giardino di luci ("Lumière") <strong>dal 13 dicembre 2025</strong> per tutte le feste. Le date 2026 sono da confermare.</p>
{{img:luoghi/martina-franca|Il centro storico di Martina Franca}}

<h2>E Cisternino e Ostuni?</h2>
<p>A Cisternino il Natale si vive soprattutto con il <strong>presepe vivente</strong> nei vicoli del centro storico: nel 2025 le serate sono state il 28 dicembre e il 4 e 6 gennaio. A Ostuni il mercatino "Zucchero e Cannella" si è tenuto <strong>dal 6 all'8 dicembre 2025</strong> tra viale Pola e piazza Italia. Per entrambi il programma 2026 non è ancora pubblico.</p>
{{img:luoghi/ostuni|La città bianca di Ostuni}}

<h2>Come organizzare un weekend di mercatini?</h2>
<ul>
<li><strong>Quando:</strong> il ponte dell'Immacolata (8 dicembre) e i giorni tra Natale e l'Epifania sono i momenti in cui è aperto quasi tutto. I weekend sono affollati: se puoi, scegli un giorno feriale.</li>
<li><strong>Un giro possibile:</strong> mattina a Martina Franca, pomeriggio ad Alberobello, sera a Locorotondo con le luci accese.</li>
<li><strong>Abbigliamento:</strong> la sera in collina fa freddo e le strade dei centri storici sono in pietra.</li>
<li><strong>Dove dormire:</strong> un trullo in campagna come <a href="/il-trullo/">Trullo Rosy</a>, tra Martina Franca e Locorotondo, è comodo per tutti i paesi della valle. Altri luoghi da vedere sono nella pagina <a href="/dintorni/">Dintorni</a>. Tutte le informazioni per prenotare sono nella pagina del nostro <a href="/">trullo in affitto a Martina Franca</a>.</li>
</ul>

<h2>Domande frequenti</h2>
<details><summary>Quando aprono i mercatini di Natale in Puglia nel 2026?</summary><p>Ad oggi solo Locorotondo ha un periodo indicato dal Comune: dal 22 novembre 2026 al 6 gennaio 2027. Negli altri paesi della Valle d'Itria, nel 2025 i mercatini sono partiti tra fine novembre e inizio dicembre.</p></details>
<details><summary>Qual è il mercatino di Natale più bello della Valle d'Itria?</summary><p>Locorotondo è il più conosciuto per le luminarie nel centro storico bianco; Alberobello ha il villaggio di Natale tra i trulli in piazza del Popolo.</p></details>
<details><summary>Si possono vedere più mercatini in un giorno?</summary><p>Sì: Martina Franca, Locorotondo e Alberobello sono vicini e si visitano bene nella stessa giornata, lasciando Locorotondo per la sera.</p></details>
<details><summary>Dove dormire per i mercatini della Valle d'Itria?</summary><p>Nella campagna tra Martina Franca e Locorotondo, per esempio a Trullo Rosy: un trullo intero con tre camere, camino e parcheggio, fino a 6 ospiti.</p></details>
""",
            faq=[
                ("Quando aprono i mercatini di Natale in Puglia nel 2026?", "Ad oggi solo Locorotondo ha un periodo indicato dal Comune: dal 22 novembre 2026 al 6 gennaio 2027. Negli altri paesi della Valle d'Itria, nel 2025 i mercatini sono partiti tra fine novembre e inizio dicembre."),
                ("Qual è il mercatino di Natale più bello della Valle d'Itria?", "Locorotondo è il più conosciuto per le luminarie nel centro storico bianco; Alberobello ha il villaggio di Natale tra i trulli in piazza del Popolo."),
                ("Si possono vedere più mercatini in un giorno?", "Sì: Martina Franca, Locorotondo e Alberobello sono vicini e si visitano bene nella stessa giornata, lasciando Locorotondo per la sera."),
                ("Dove dormire per i mercatini della Valle d'Itria?", "Nella campagna tra Martina Franca e Locorotondo, per esempio a Trullo Rosy: un trullo intero con tre camere, camino e parcheggio, fino a 6 ospiti."),
            ],
            cta_h2="Dormi in un trullo tra i mercatini della Valle d'Itria",
            sources_h2="Fonti",
            photos_h2="Foto",
            updated="Aggiornato il 13 novembre 2026",
        ),
        "en": dict(
            title="Christmas markets in Puglia 2026: Itria Valley",
            desc="Christmas markets in Puglia's Itria Valley: Locorotondo, Alberobello, Martina Franca, Cisternino and Ostuni, with 2025 dates and what is known for 2026.",
            h1="Christmas markets in Puglia: the Itria Valley town by town",
            answer="Puglia's most compact cluster of Christmas markets is in the Itria Valley: Locorotondo, Alberobello, Martina Franca, Cisternino and Ostuni are only a few kilometres apart. In 2025 they ran from late November or early December until 6 January. For 2026 the only dates set by a town council so far are Locorotondo's, from 22 November 2026 to 6 January 2027.",
            body="""
<h2>Which Christmas markets are in the Itria Valley?</h2>
<p>The Itria Valley is trulli country, where the provinces of Bari, Taranto and Brindisi meet. In December almost every town has lights, markets or a Christmas village, and distances are short: you can see two in a day. Below is what ran in 2025 and what is known so far (13 November 2026) about 2026.</p>
<table class="facts">
<thead><tr><th scope="col">Town</th><th scope="col">What's on</th><th scope="col">2025 edition</th><th scope="col">2026</th></tr></thead>
<tbody>
<tr><th scope="row">Locorotondo</th><td>Lights and markets in the old town</td><td>markets 30 November 2025 – 6 January 2026</td><td>period set by the council: 22 November 2026 – 6 January 2027</td></tr>
<tr><th scope="row">Alberobello</th><td>Lights among the trulli and Christmas village in Piazza del Popolo</td><td>village 6 December 2025 – 6 January 2026</td><td>to be confirmed</td></tr>
<tr><th scope="row">Martina Franca</th><td>Santa's village and garden of lights in the public garden</td><td>lights in the public garden from 13 December 2025</td><td>to be confirmed</td></tr>
<tr><th scope="row">Cisternino</th><td>Living nativity in the old town</td><td>28 December 2025, 4 and 6 January 2026</td><td>to be confirmed</td></tr>
<tr><th scope="row">Ostuni</th><td>"Zucchero e Cannella" market</td><td>6–8 December 2025</td><td>programme not yet published</td></tr>
</tbody>
</table>
{{img:panorama-valle-itria|View over the Itria Valley}}

<h2>What's on in Locorotondo at Christmas?</h2>
<p>Locorotondo is the best-known town for its lights. In 2025 the markets ran <strong>from 30 November 2025 to 6 January 2026</strong> in Piazza Aldo Moro, the public garden and the streets near the town hall. For 2026 the council has planned events <strong>from 22 November 2026 to 6 January 2027</strong>, with Pinocchio-themed lights. Dates, times and the route are in our dedicated guide: <a href="/en/guides/christmas-in-locorotondo/">Christmas in Locorotondo</a>.</p>

<h2>What is Christmas like in Alberobello?</h2>
<p>In 2025 the lights covered the Rione Monti and Aia Piccola districts <strong>from 5 December 2025 to 5 January 2026</strong>, and Piazza del Popolo hosted a Christmas food village among the trulli <strong>from 6 December 2025 to 6 January 2026</strong>, with Santa's house and an ice rink. The living nativity ran from 26 to 29 December 2025. The 2026 programme has not been published yet.</p>
{{img:luoghi/alberobello|The trulli of Alberobello}}

<h2>What is there in Martina Franca?</h2>
<p>Martina Franca, Trullo Rosy's home town, has a Santa's village in its baroque old town. In 2025 the public garden became a garden of lights ("Lumière") <strong>from 13 December 2025</strong> through the holidays. The 2026 dates are to be confirmed.</p>
{{img:luoghi/martina-franca|The old town of Martina Franca}}

<h2>What about Cisternino and Ostuni?</h2>
<p>In Cisternino, Christmas is mostly about the <strong>living nativity</strong> in the lanes of the old town: in 2025 it ran on 28 December and 4 and 6 January. In Ostuni the "Zucchero e Cannella" market was held <strong>from 6 to 8 December 2025</strong> along Viale Pola and Piazza Italia. Neither has published its 2026 programme yet.</p>
{{img:luoghi/ostuni|Ostuni, the white town}}

<h2>How to plan a Christmas market weekend?</h2>
<ul>
<li><strong>When:</strong> the 8 December holiday weekend and the days between Christmas and Epiphany are when almost everything is open. Weekends are busy: pick a weekday if you can.</li>
<li><strong>A possible route:</strong> morning in Martina Franca, afternoon in Alberobello, evening in Locorotondo with the lights on.</li>
<li><strong>What to wear:</strong> evenings on the hills are cold and old town streets are stone.</li>
<li><strong>Where to stay:</strong> a countryside trullo such as <a href="/en/the-trullo/">Trullo Rosy</a>, between Martina Franca and Locorotondo, is handy for every town in the valley. More places to visit are on our <a href="/en/surroundings/">Surroundings</a> page. Everything you need to book is on the page of our <a href="/en/">trullo for rent in Martina Franca</a>.</li>
</ul>

<h2>Frequently asked questions</h2>
<details><summary>When do the Christmas markets in Puglia open in 2026?</summary><p>So far only Locorotondo has a period set by its council: 22 November 2026 to 6 January 2027. In the other Itria Valley towns, the 2025 markets started between late November and early December.</p></details>
<details><summary>Which is the best Christmas market in the Itria Valley?</summary><p>Locorotondo is the best known for the lights in its white old town; Alberobello has a Christmas village among the trulli in Piazza del Popolo.</p></details>
<details><summary>Can you see several markets in one day?</summary><p>Yes: Martina Franca, Locorotondo and Alberobello are close together and easy to visit in one day, leaving Locorotondo for the evening.</p></details>
<details><summary>Where to stay for the Itria Valley Christmas markets?</summary><p>In the countryside between Martina Franca and Locorotondo, for example at Trullo Rosy: an entire trullo with three bedrooms, a fireplace and parking, for up to 6 guests.</p></details>
""",
            faq=[
                ("When do the Christmas markets in Puglia open in 2026?", "So far only Locorotondo has a period set by its council: 22 November 2026 to 6 January 2027. In the other Itria Valley towns, the 2025 markets started between late November and early December."),
                ("Which is the best Christmas market in the Itria Valley?", "Locorotondo is the best known for the lights in its white old town; Alberobello has a Christmas village among the trulli in Piazza del Popolo."),
                ("Can you see several markets in one day?", "Yes: Martina Franca, Locorotondo and Alberobello are close together and easy to visit in one day, leaving Locorotondo for the evening."),
                ("Where to stay for the Itria Valley Christmas markets?", "In the countryside between Martina Franca and Locorotondo, for example at Trullo Rosy: an entire trullo with three bedrooms, a fireplace and parking, for up to 6 guests."),
            ],
            cta_h2="Stay in a trullo among the Itria Valley markets",
            sources_h2="Sources",
            photos_h2="Photos",
            updated="Updated 13 November 2026",
        ),
    },
]
