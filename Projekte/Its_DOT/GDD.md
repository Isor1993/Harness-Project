<!--
Ownership: Design-Absicht des Spiels „It's Dungeon Outbreak Time"
(Harness-Schicht Its_DOT) — was es sein soll, nicht wie
es gebaut wird — und zugleich das
Markdown-Manuskript, aus dem `Kern/Werkzeuge/abgabe_bauen.py` die
.docx-Abgabefassung baut (Formatvorlage und Titelteil im Datenbaum,
`Kern/PFADE.md` → `DATENBAUM`; den Umgang mit der .docx regelt
`Uni/DOCX_RULES.md`). Begründungen gehören in die DECISIONS dieser
Schicht, Aufgaben in die ROADMAP, Technik ins spätere TDD. Aufbau und
Pflege regelt `Kern/GDD_RULES.md`.
Format: feste Kapitelfolge nach `Kern/GDD_RULES.md`, Kapitel als `#`
und Unterkapitel als `##` (Abgabe-Ebenen wie beim TDD); die
Abgabe-Kapitel der Aufgabenstellung
(`Uni/Semester_3/ASSIGNMENT_GAME_PITCH.md`) stehen als „weitere
Kapitel nach Bedarf" dahinter; offene Punkte als `**Offen:**` im
Kapitel und gesammelt unter „Offene Design-Fragen"; Rohes datiert im
Abschnitt „Entwurf". Alles ab der Marke `abgabe-ende` ist intern und
bleibt beim Bauen draußen. Dieser Kommentar wird beim Bauen verworfen.
-->

# Pitch

**It's Dungeon Outbreak Time** (kurz: It's D.O.T) ist eine
Koop-Wellen-Verteidigung mit Basisbau: 3D, in Ego-Perspektive mit Zoom heraus bis in die
dritte Person, für ein bis vier Spieler am PC, solo vollwertig
spielbar. Die Gruppe wacht ohne Vorgeschichte auf einer wilden Insel
in einer hellen Anime-Fantasy-Welt auf und baut einen Außenposten, um
zu überleben. Denn ein Timer zählt auf den nächsten
Outbreak herunter: Wellen von Fantasywesen, die aus den Dungeons der
Insel brechen und die Basis zerlegen wollen. Zwischen den Ausbrüchen
schwärmt die Gruppe aus und sammelt Material. Die Insel um die Basis
ist bald leergesammelt, die Wege werden länger, und die Gier gegen die
Uhr ist der eigentliche Endgegner. Die Wellen sind endlos; Ziel ist, als Team die höchste
Welle zu erreichen.

# Kern-Schleife

It's D.O.T läuft in Echtzeit und erzwingt keine Phasen. Den
Rhythmus geben die Dungeons vor: Ein sichtbar angekündigter Countdown
läuft auf den nächsten Outbreak zu, dann bricht die Welle los und will
an die Basis. Zwischen den Ausbrüchen ist das Team frei und
entscheidet selbst, was ihm die Zeit wert ist: Material sammeln,
bauen, reparieren, Beute einlagern. Die eigentliche Entscheidung jeder
Runde ist die Aufteilung: Wer geht raus, wer bleibt bei der Basis, wer
flickt die Mauern. Die Wellen sind endlos und werden stärker; das Ziel
einer Partie ist, als Team die höchste Welle zu erreichen.

## Ablauf einer Partie

Eine Partie beginnt mit der Gründung: Die Gruppe trägt das Herzobjekt
der Insel im Gepäck (Arbeitsname Siegelstein) und setzt es frei auf
der Karte ab. Wo das Herzobjekt steht, steht die Basis. Wer nach etwa
vier Minuten nicht gesetzt hat, bekommt einen Platz in der Nähe
zugewiesen; der erste Outbreak kommt nach etwa sieben bis acht
Minuten. Das Herzobjekt ist zugleich der Einsatz der Partie: Fällt es,
ist die Partie verloren. Gefallene Spieler beenden die Partie dagegen
nie allein.

**Offen:** Partielänge und Wellen-Takt, Outbreak-Ankündigung,
Herzobjekt — siehe „Offene Design-Fragen".

# Welt-Struktur

Eine kleine, fest gestaltete Insel ist das Spielfeld; es gibt genau
eine Karte, und das Wasser ist ihre natürliche Grenze: Hineinlaufen
geht nur ein paar Schritte, schwimmen nicht. Die Gruppe wacht immer am
selben Ort auf, einem Strand am Rand der Insel. Auf der Insel verteilt
liegen sichtbare Dungeons, die Quellen der Outbreaks; ihre Plätze
verteilt das Spiel zu Beginn jeder Partie zufällig neu, danach stehen
sie fest. Aktiv sind nur die Dungeons in einem Radius um die Basis;
mit steigenden Wellen erwachen weitere, und der Druck kommt aus neuen
Richtungen.

Die Materialquellen sind über die ganze Insel verteilt: Häufiges wie
Holz wächst in Wäldern und vereinzelt, Stein liegt verstreut,
seltenere Quellen wie das Mithril-Erz gibt es nur an wenigen Stellen. Abgebaute
Quellen sind verbraucht. Rund um die Basis ist die Insel darum bald
leergesammelt, und die Wege werden mit jeder Runde länger.

**Offen:** Inselgröße, Ressourcen-Respawn und Universum — siehe
„Offene Design-Fragen".

# Spieler

## Perspektive und Kamera

Gespielt wird in Ego-Perspektive. Die Kamera lässt sich herauszoomen;
weiter draußen wird das Spiel zur dritten Person und die eigene Figur
sichtbar. Ein bis vier Spieler; solo vollwertig spielbar, zu viert am
besten.

## Steuerung

Unterstützt werden Maus und Tastatur sowie Controller; die
Controller-Belegung entsteht im Prototyp. Für Maus und Tastatur gilt
diese vorläufige Belegung:

| Eingabe | Wirkung |
|---|---|
| WASD | Laufen |
| Leertaste | Springen |
| Linke Maustaste | Basisangriff und Aktion |
| E | Interagieren |
| I | Inventar |
| B oder Mausrad-Klick | Bauen |
| M | Karte (geplant) |

## Waffen und Rollen

Es gibt kein Klassensystem: Die Waffe entscheidet, was man ist. Jede
Waffe kann in der ersten Version genau eines, ihren Basisangriff auf
der Aktionstaste: Das Schwert schlägt, der Bogen schießt. Besondere
Fähigkeiten je Waffe sind als spätere Erweiterung vorgemerkt. Waffen
liegen im Lager, werden dort entwickelt und jederzeit getauscht:
Rollenwechsel ist ein Griff ins Regal, keine Menüentscheidung. Zum
Start gibt es wenige Waffen, im Prototyp ein Nahkampf und ein
Fernkampf; kreative und witzige Waffen sind ausdrücklich Teil der
Absicht.

## Fall beim Outbreak

Kippt ein Spieler um, bleibt seine getragene Beute in einem Behälter
an der Stelle liegen und kann wieder eingesammelt werden. Spieler-Tode
beenden die Partie nie; wie Gefallene zurückkommen, ist offen.

**Offen:** Fall beim Outbreak (Waffe und Wiederbelebung),
Waffen-Entwicklung und Bau-Eingabe — siehe „Offene Design-Fragen".

# Persistenz

Innerhalb einer Partie wächst alles: Festung, Waffen, Lager. Über die
Partie hinaus bleibt nichts, jede Partie startet bei null. Fortschritt
über Partien hinweg (Festung, Waffen, Freischaltungen) ist als ferne
Erweiterung vorgemerkt.

# Spielmechaniken

Die einzelnen Systeme hinter der Schleife.

## Basis-Bau

Gebaut wird, um sich zu verbarrikadieren: Mauern, frei auf der Karte
platziert, wahlweise aus Holz oder aus Stein. Es gibt keine
vorgegebenen Bauplätze und keinen vorgeschriebenen Grundriss; eigene
Verteidigungs-Strategien zu finden ist ausdrücklich Teil des Spiels.
Tore und Türen gibt es in der ersten Version nicht: Wer seine Basis
schließt, lässt eine Lücke als Eingang und verteidigt genau dort.
Alles Gebaute kann zerbrechen und wird mit Material repariert. Die
einzige Station der ersten Version ist die Werkbank, der Platz zum
Schmieden und Entwickeln; weitere Stationen und Tore sind als
Erweiterung vorgemerkt.

## Ressourcen-Ströme und Lager

Getrennte Ströme füttern die Schleife: Material aus der Welt (Holz,
Stein und ein seltenes Erz, Arbeitsname Mithril) baut die Festung aus,
Beute aus den Wellen entwickelt die Waffen. Jeder Spieler trägt ein
begrenztes eigenes Inventar und legt im Team-Lager ab. Volle Taschen
erzwingen Rückwege, und genau daraus entsteht die Spannung der
Sammel-Phase.

## Wellen, Gegner und Verhalten

Die Gegner brechen aus den Dungeons der Insel und folgen festen
Mustern: Sie wollen an die Basis oder greifen die Spieler an, die
sich ihnen in den Weg stellen; wer kämpft oder blockt, zieht ihre
Aufmerksamkeit auf sich. Zum Start gibt es zwei bis vier Gegnertypen;
ihre Rollen und ihr Aussehen beschreibt „Thema, Aussehen und Story".
Die Wellen eskalieren über das gesamte Spielerlebnis: Erst kommen
wenige Gegner, dann mehr, nach und nach treten stärkere Varianten
(etwa ein Goblin-Krieger) und neue Typen auf, und mit höheren Wellen
erwachen weitere Dungeons, sodass der Druck auch aus neuen Richtungen
kommt. Das Verhalten der einzelnen Gegnertypen wird mit der
KI-Planung ausgearbeitet.

# Benutzeroberfläche

Das HUD bleibt schlank. Ständig sichtbar sind die aktuelle Welle, die
Outbreak-Ankündigung, das eigene Leben und eine Quickslot-Leiste am
unteren Rand; die Quickslots sind die erste Reihe des Inventars,
visuell abgesetzt, und bestimmen, was die Figur in der Hand hält.
Dazu kommen die Anzeigen, die das Spielprinzip verlangt: der Zustand
des Herzobjekts samt einem deutlichen Signal, wenn die Basis
angegriffen wird, eine kleine Lebensanzeige der Mitspieler mit klarem
Hinweis, wenn jemand am Boden liegt, und ein Richtungs-Anker, der von
überall den Weg zur Basis zeigt. Zählstände der Materialien wohnen im
Inventar, nicht dauerhaft im Bild.

Die Taste I öffnet das Inventar als Rasterfenster; darüber stehen die
Figur und die aktiv getragenen Slots. Gebaut wird über ein Radialmenü
(vorläufiger Stand, Feinschliff im Prototyp).

Der Menüfluss ist kurz: Hauptmenü, dann Hosten oder Beitreten per
Join-Code, Lobby mit Bereit-Status und Chat, Partie. Im Spiel gibt es
ein kleines Pausenmenü. Endet die Partie, zeigt ein
Abschlussbildschirm die erreichte Welle und die Zahlen der Runde. Eine
Minimap ist als Erweiterung vorgemerkt.

Eine Gestaltungsregel gilt überall: Wichtige Zustände werden nie
allein über Farbe unterschieden, besonders nicht über Rot gegen Grün.
Zusätzlich zeigt immer eine Form oder ein Text denselben Zustand an.

**Offen:** Bau-Eingabe, Outbreak-Ankündigung und Kommunikation im
Spiel — siehe „Offene Design-Fragen".

# Thema, Aussehen und Story

Anime-Fantasy in einer Welt der Abenteurer-Gilden: Die Spieler wachen
ohne Vorgeschichte auf der Insel auf, die Gegner sind klassische
Fantasywesen. Fest sind zunächst ihre Rollen: ein Schwarm, ein
Schneller, ein Robuster, ein Brocken. Welche Wesen diese Rollen
bekommen, entscheidet sich an den verfügbaren Assets; Kandidaten sind
Goblins, Wölfe, Orks und Zyklopen. Die Welt ist keine Parodie,
Bedrohung und Fantasy sind ernst angelegt. Der Spaß entsteht beim
Spielen: hell, freundlich, Physik-Slapstick, Raum für Blödsinn unter
Freunden. Geschriebener Humor bleibt Würze, nicht Fundament.

Das Aussehen ist stylized und low-poly im Anime-Stil, mit bewusst
einfachen Assets. Grafisches Vorbild ist der Look von Chop Chop Inc.;
er gibt die Richtung vor, umgesetzt wird sie mit einfacheren Mitteln.

Die Story bleibt bewusst im Hintergrund: Teile von ihr, etwa die
Spuren der Abenteurer-Gilden dieser Welt, lassen sich im Spiel über
die Umgebung und Easter Eggs entdecken, erzählt wird sie nicht.

**Offen:** Gegner-Besetzung — siehe „Offene Design-Fragen".

# Audio und Musik

Die Musik arbeitet als Phasen-Signal: ruhig während des Sammelns,
druckvoll, sobald der Outbreak ansteht und läuft. Den Wechsel soll man
hören, nicht nur sehen.

Sounds decken alle Spielbereiche ab: Waffen und Treffer, die Spieler
(Schritte, Springen, Umkippen), die Gegner samt einem Kriegsschrei
beim Ausbruch, aufgenommene Beute, Bauen und Reparieren sowie die
Benutzeroberfläche. Besonderes Gewicht hat der Physik-Slapstick:
Schubser, Stürze und Scheppern tragen den Humor des Spiels.

Musik und Sounds kommen aus fertigen Packs, frei oder zugekauft.

# Vergleichbare Produkte und Referenzen

It's D.O.T steht zwischen zwei Nachbarschaften: den
Koop-Verteidigungs-Spielen und den kleinen Koop-Spielen, die vom
Miteinander leben.

- **7 Days to Die:** Vorbild für das Belagerungs-Gefühl und die
  Eskalation über das ganze Spielerlebnis. Die Horden-Nächte zeigen,
  wie ein wiederkehrender Angriffs-Termin eine Vorbereitungs-Schleife
  antreibt.
- **Dungeon Defenders** und **Orcs Must Die! Deathtrap:**
  Koop-Verteidigung, in der die Spieler selbst kämpfen statt nur zu
  bauen. Von dort kommt die Mischung aus Verteidigen und eigenem
  Eingreifen.
- **R.E.P.O.** und **RV There Yet?:** der Maßstab für den Ton. Kleine
  Koop-Spiele, deren Spaß aus den Mitspielern entsteht, mit Physik und
  Raum für Missgeschicke.
- **Chop Chop Inc.:** das grafische Vorbild (siehe „Thema, Aussehen
  und Story").
- **Solo Leveling:** der Anime-Anker für die Prämisse. Dungeons, die
  sich in die Welt öffnen und ausbrechen, sind der Zielgruppe aus
  diesem Umfeld vertraut.

Was keiner dieser Nachbarn besetzt: das Pendel aus Rausgehen und
Standhalten im 3D-Koop. Die Basis ist frei gebaut, die Spieler stehen
selbst im Kampf, und zwischen den Wellen zieht das Sammeln sie von der
Basis weg.

# USP

Das Alleinstellungsmerkmal von It's D.O.T lässt sich in einem
Satz sagen: gemeinsam draußen schuften, gemeinsam drinnen standhalten.
Dieselben Spieler, die draußen sammeln, müssen drinnen verteidigen. Es
gibt keine Arbeitsteilung zwischen Sammeln und Kämpfen, sondern einen
Kreislauf, in dem jede Minute draußen die Verteidigung stärkt und
zugleich das Risiko erhöht, beim Outbreak nicht zu Hause zu sein. Die
Gier gegen die Uhr ist der eigentliche Endgegner. Dazu kommt die freie
Basis: kein vorgegebener Bauplatz, keine vorgegebenen Wege, jede
Gruppe baut und verteidigt anders. In der Nachbarschaft der
Koop-Verteidigungen und der kleinen Koop-Spiele ist diese Mischung aus
freiem Basisbau, eigenem Kampf und erzwungenem Rausgehen unbesetzt.

# Zielpublikum

It's D.O.T zielt auf kleine Freundesgruppen, die abends ein paar
Runden zusammen spielen wollen: ein Spiel, das in Minuten erklärt ist,
dessen Partien bewusst kurz bleiben und dessen Spaß aus den
Mitspielern entsteht. Es braucht kein Genre-Vorwissen; wer
Koop-Kleinspiele wie R.E.P.O. oder RV There Yet? mag, ist hier zu
Hause. Solo ist das Spiel vollwertig spielbar, am besten ist es zu
viert. Die sichtbaren Missgeschicke und der Physik-Slapstick machen es
zugleich streamer-tauglich: Es erzeugt Momente, die man teilen will.
Die Anime-Fantasy-Prämisse holt zusätzlich das Publikum ab, das
Dungeon-Break-Geschichten aus Anime und Manga kennt.

# Ziel und Umfang

Ziel der ersten Version ist ein fertiges, veröffentlichbares kleines
Spiel: der vollständige Kreislauf aus Sammeln, Bauen und Abwehren im
Koop, stabil über das Netz, mit wenigen, aber sauberen Inhalten.
Qualität geht vor Umfang.

Die erste Version enthält:

- Koop für ein bis vier Spieler über Hosten und Beitreten per Code,
  solo vollwertig spielbar
- eine feste, kleine Insel mit je Partie zufällig verteilten
  Dungeon-Plätzen
- die Gründung mit dem Herzobjekt und freien Mauerbau aus Holz oder
  Stein, mit Werkbank und Reparieren
- drei Rohstoffe mit erschöpfbaren Quellen, Team-Lager und begrenztem
  Trage-Inventar
- endlose Wellen mit wachsender Stärke, Varianten und neuen
  Angriffsrichtungen, zum Start zwei bis vier Gegnertypen
- wenige, klar unterschiedliche Waffen mit je einem Basisangriff
  (Nah- und Fernkampf), jederzeit am Lager tauschbar
- den Beute-Behälter beim Umkippen sowie HUD, Menüs und Lobby wie in
  den Kapiteln beschrieben

Bewusst nicht in der ersten Version, als modulare Erweiterungen
vorgemerkt: Fähigkeiten je Waffe, weitere Waffen und Gegnertypen, Tore
und Türen, weitere Werkstationen, Tränke, begehbare Dungeons,
Fortschritt über Partien hinweg, eine Minimap sowie größere oder
weitere Inseln.

# Zeitplan

Der Zeitplan ist als Meilenstein-Folge angelegt, bewusst ohne
Kalenderdaten; Daten bekommt er, sobald das Projekt startet.

1. **Konzept:** Das Design-Dokument steht (dieser Stand).
2. **Fundament** (etwa ein bis zwei Wochen): Die erprobte
   Netz-Grundlage wird übernommen, die Insel entsteht als Blockout,
   die Gründung mit dem Herzobjekt funktioniert.
3. **Basis und Ressourcen** (etwa ein bis zwei Wochen): Mauerbau,
   Abbau der Quellen, Team-Lager und Trage-Inventar.
4. **Wellen und Kampf** (etwa zwei Wochen): Dungeons, Gegner und
   Waffen; der volle Kreislauf läuft, die Partie lässt sich verlieren.
5. **Messrunden** (etwa eine Woche): Partielänge, Gegner-Mengen und
   Inselgröße werden gespielt und gemessen; die offenen Werte-Fragen
   schließen sich.
6. **Feinschliff** (etwa eine Woche): die erste vorzeigbare Fassung;
   das Design-Dokument wird mit den Ergebnissen nachgeführt.
7. **Präsentationsfassung** (wenige Tage): Bilder und kurze Videos
   entstehen aus dem Spiel.

Jeder Meilenstein ist mit Reserve geplant: Was kippt, fällt in die
Erweiterungsliste, statt den Plan zu sprengen.

# Technische Daten

Zielplattform ist der PC. Gespielt wird online: Die Verbindung läuft
über einen Relay-Dienst mit Beitritts-Code, ein eigener Server ist
nicht nötig. Die Hardware-Anforderungen bleiben bescheiden; der
Low-Poly-Stil und die bewusst einfachen Assets halten das Spiel auch
auf schwächeren Rechnern lauffähig. Genaue Mindestanforderungen werden
am Ende der Entwicklung gemessen statt geschätzt.

# Entwicklungsumgebung

Das Spiel entsteht in Unity (C#). Der Mehrspieler-Teil baut auf einer
vorhandenen, erprobten Grundlage auf: Netcode for GameObjects mit
Relay und Beitritts-Code, Lobby und netzsynchronem Laden, getestet
über getrennte Netze. 3D-Assets, Musik und Sounds kommen aus fertigen
Packs, frei oder zugekauft; eigene Inhalte entstehen bei Bedarf in
Blender. Die Versionsverwaltung läuft über Git.

# Vorgehensweise und Qualitätssicherung

It's D.O.T ist ein Ein-Personen-Projekt: Design und Code liegen
in einer Hand. Art und Audio kommen aus freien oder zugekauften
Asset-Packs; was dort fehlt, wird selbst gebaut oder gezielt
dazugekauft.

Gebaut wird Spielmechanik für Spielmechanik. Jedes System ist ein
eigener Baustein: Er wird gebaut, in kleinen Zwischentests geprüft und
dokumentiert, erst dann beginnt der nächste. So gibt es zu jedem
Zeitpunkt einen funktionierenden Stand statt vieler halbfertiger
Baustellen.

Design-Entscheidungen werden mit Begründung festgehalten, und dieses
Dokument wird laufend nachgeführt; gearbeitet wird nach dem Dokument,
und der Umfang der ersten Version bleibt bewusst so klein wie möglich.
Dazu kommen regelmäßige Test-Plays mit anderen Spielern: Ihre Urteile
fließen in die Abwägung ein und machen die Entscheidungen besser;
getroffen werden sie vom Entwickler selbst.

Getestet wird grundsätzlich doppelt: im Koop über das echte Netz und
zugleich solo. Balance-Werte werden gemessen statt geschätzt. Bei
Assets zählen drei Prüfungen vor dem Einsatz: die Lizenz, die Passung
zum Low-Poly-Stil und der Preis.

# Quellenverzeichnis

Das Quellenverzeichnis wird mit der Endfassung des Dokuments
nachgetragen.

<!-- abgabe-ende -->

# Offene Design-Fragen

- **Umfang-Feinschnitt:** Vom Freigabe-Feedback (`Uni/LOG.md`,
  2026-10-12) ist nach dem Kampf-Schnitt (DECISIONS, 2026-10-14) noch
  offen: die Zahl der Gegnertypen und die Ragdoll-Mengen. Entscheidet
  sich bei „Spielmechaniken", „Ziel und Umfang" und im Prototyp
  (ROADMAP → „T1").
- **Partielänge:** Wellen-Takt und Eskalationskurve so, dass eine
  Partie kurz bleibt — Zielwerte im Prototyp messen; Richtwerte im
  Entwurf.
- **Fall beim Outbreak:** Behält der Gefallene seine Waffe, und wie
  kommt er zurück: Wiederbelebung durch Mitspieler, automatischer
  Respawn, oder beides? Solo und der Fall „alle am Boden" brauchen
  eine Antwort, sonst hängt die Partie, obwohl das Herzobjekt steht.
- **Bau-Eingabe:** Endgültige Taste (B oder Mausrad-Klick) und das
  Bau-Menü dahinter — das Menü gehört zum Kapitel
  „Benutzeroberfläche".
- **Waffen-Entwicklung:** Levelt die Waffe als Objekt an der Werkbank
  aus Team-Beute? (Vermutlich ja — noch nicht festgezurrt.)
- **Inselgröße:** Im Blockout durch Ablaufen bestimmen; Richtschnur
  ist, die Insel so klein wie möglich zu halten.
- **Ressourcen-Respawn:** Tauchen erschöpfte Quellen anderswo neu auf,
  oder ist der Vorrat der Insel endlich? Endlich hieße: Irgendwann
  hungert die Verteidigung aus, und das Überranntwerden wird
  unausweichlich — als natürliches Partie-Ende womöglich sogar
  gewollt. Zeigt der Prototyp.
- **Gegner-Besetzung:** Welche Fantasywesen die vier Rollen (Schwarm,
  schnell, robust, Brocken) bekommen, hängt an der Asset-Sichtung;
  Kandidaten sind Goblins, Wölfe, Orks und Zyklopen.
- **Outbreak-Ankündigung:** UI-Timer, Umwelt (etwa ein aufziehendes
  Gewitter) oder Portal-Färbung mit Sound beim Ausbruch: Was zeigt den
  nahenden Outbreak an?
- **Herzobjekt:** Endgültiger Name (Arbeitsname Siegelstein) und die
  Umsetzung der Setz-Mechanik bei der Gründung.
- **Kommunikation im Spiel:** Gibt es Voice und/oder Text-Chat in der
  Partie? Die Lobby bringt den Text-Chat aus der übernommenen
  Grundlage bereits mit.

# Entwurf

*(2026-10-09, Ideenrunde — roh, bindet nichts)*

- Richtwerte Partielänge: Wellen-Takt etwa drei bis vier Minuten; eine
  normale Gruppe fällt um Welle acht bis zwölf; Partie 30–45 Minuten.
  Das Überranntwerden ist der Höhepunkt der Runde, nicht ihr Versagen.
- Technik-Notiz Gegner-Menge (gehört später ins TDD): Spieler volle
  Physik; Schwarm-Gegner als Agenten mit gefaktem Knockback und
  Ragdoll erst im Todesmoment (nur wenige gleichzeitig aktiv);
  Elite-Gegner voll. Wellen-Peak als Zielwert 200 Gegner, gleichzeitig
  lebendig deutlich weniger (Alive-Cap) — alles im Prototyp messen.
- Waffen-Ideen: Sprungfeder-Boxhandschuh als Knockback und
  Crowd-Control; später absurde Kandidaten (Fisch, Besen) und
  Quatsch-Kombos zwischen Waffen.
- Gegner-Verhalten als Comedy (Claude-Vorschlag, unbestätigt): Goblins
  klauen Material aus dem Lager und rennen damit weg.
- Erweiterungs-Detail zu den begehbaren Dungeons (roh): drinnen
  sammeln, während draußen andere Dungeons ausbrechen können.
- Store-Namenskandidat neben dem Arbeitstitel: „Guildbreak".

*(2026-10-14, GDD-Session — roh, bindet nichts)*

- Titelkandidat „It's D.O.T": einsortiert am 2026-10-16 — ist als
  „It's Dungeon Outbreak Time" der Titel des GDD geworden (DECISIONS,
  2026-10-16); die Such- und DoT-Bedenken stehen dort.
- Story-Kandidat: Die Fantasy-Welt bricht in unsere Realität ein —
  möglicher Hintergrund, passt zur Umgebungs-Erzählung über Easter
  Eggs; Story bleibt bewusst offen.
- Klärrunde Kern-Schleife: einsortiert am 2026-10-14 — die Ergebnisse
  stehen als Kapiteltext „Kern-Schleife", in drei DECISIONS-Einträgen
  vom 2026-10-14 und in den offenen Design-Fragen.
- Technik-Notiz Dungeon-Plätze (gehört später ins TDD): Der Zufall
  wählt aus handgesetzten Kandidaten-Plätzen im Level und aktiviert je
  Partie eine Teilmenge; über das Netz läuft nur der Seed.
- Richtungs-Anker als Umwelt statt UI (Claude-Vorschlag, unbestätigt):
  eine Rauchsäule über der Basis zeigt den Heimweg ohne
  Bildschirm-Marker.
- Technik-Notiz Steam (gehört später ins TDD): Hosten und Beitreten
  laufen über Steam später anders als über den Join-Code der
  übernommenen Grundlage; beim Release-Schritt sauber neu bauen.

*(2026-10-16, GDD-Session — roh, bindet nichts)*

- Quellen-Liste für den Nachtrag, verifiziert per Websuche am
  2026-10-16: 7 Days to Die (The Fun Pimps, seit 2013), Dungeon
  Defenders (Trendy Entertainment, 2011), Orcs Must Die! Deathtrap
  (Robot Entertainment, 2025), R.E.P.O. (Semiwork, 2025), RV There
  Yet? (Nuggets Entertainment, 2025), Chop Chop Inc. (NullRef
  Entertainment, 2026), Solo Leveling (Anime von A-1 Pictures, seit
  2024, nach dem Webroman von Chugong); Werkzeuge: Unity samt Netcode
  for GameObjects und Relay (Unity Technologies), Blender (Blender
  Foundation), Git. Beim Nachtragen um die tatsächlich benutzten
  Asset-Packs ergänzen.
