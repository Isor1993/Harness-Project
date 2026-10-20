# DECISIONS.md — Entscheidungen It's D.O.T

Ownership: Nur Entscheidungen zum Koop-Spiel It's Dungeon Outbreak
Time (Kürzel It's D.O.T; Harness-Schicht Its_DOT; seit dem 2026-10-20
privates Projekt ohne Termin, nicht mehr das Semester-Spiel des Moduls
5FSC0XD101_P) — was entschieden
wurde, warum, und welche Alternativen verworfen wurden. Kein Plan
(ROADMAP), keine Design-Absicht (GDD), kein Ereignis. Die
Uni-Aufgabenstellung gehört der Uni-Schicht.
Format: `## JJJJ-MM-TT — Titel` mit **Was** / **Warum** / **Verworfen**.
Älteste oben, wie in einer Chronik.

## 2026-10-09 — Marktsegment und Rahmen

Was: Das Semester-Spiel wird ein Koop-Kleinspiel: 3D, dritte Person mit
Zoom-Option (Figur sichtbar), ein bis vier Spieler, solo vollwertig
spielbar. Zielgruppe: allgemeine Spieler, kleine Freundesgruppen,
bewusst streamer-tauglich. Optik stylized, hell, freundlich — Grafik-
Nordstern ist Chop Chop Inc. Kleiner, bewusst erweiterbarer Core-Loop;
wenig bis keine Story.
Warum: Isors Marktrecherche vom 2026-10-09 (R.E.P.O., Chop Chop Inc.,
Schedule I, Liar's Bar, How to Fish, RV There Yet?, House Flipper 2,
Bombanana, Meccha Chameleon, Mimic Party, TCG Card Shop Simulator): Das
Segment lebt von Spielspaß pro Baustunde statt Content-Masse — die
Mitspieler erzeugen den Content. 3D ist Isors Vorliebe; die sichtbare
Figur trägt das Koop-Gefühl (Emotes, Missgeschicke). Der stylized Look
passt zum Toon-Shader-Lernpfad.
Verworfen: First Person (Figur soll sichtbar sein); Top-Down à la
Diablo/PoE (bewusst geparkt für ein späteres Spiel); Story-getriebenes
Konzept (Content-Kosten ohne Koop-Nutzen).

## 2026-10-09 — Core-Loop: Sammeln, Bauen, Outbreak

Was: Wellen-Verteidigung um eine selbstgebaute Basis. Kreislauf:
Sammeln, solange der Timer läuft → an der Basis bauen und schmieden →
den Outbreak abwehren → verschnaufen, einlagern, reparieren → nächste
Runde, stärker. Die Gegner wollen an die Basis; was sie blockt oder wer
nahe kämpft, zieht ihre Aggro auf sich. Gebautes lenkt und schützt —
und ist zerstörbar.
Warum: Löst die beiden Probleme, die Isor am klassischen Pfad-TD selbst
benannt hat: Der Nahkämpfer läuft Gegnern hinterher, die an ihm
vorbeirennen, und enge gebaute Gänge töten den Physik-Quatsch
(Wegschubsen, Umfallen). Vorbild für das Belagerungs-Gefühl ist der
Blutmond aus 7 Days to Die.
Verworfen: klassisches Pfad-TD mit Gegnern auf gebauten Wegen (erzeugt
genau die beiden Probleme); reine Belagerung ohne Schutzobjekt (Bauen
verliert den Zweck, Kiting entwertet die Welle).

## 2026-10-09 — Ressourcen-Ströme und Team-Lager

Was: Es gibt getrennte Ströme: Material aus der Welt (Holz, Stein, Erz
— abbaubar, weiter draußen ergiebiger) speist das Bausystem; Beute aus
den Wellen speist Waffen und Upgrades (später Tränke). Jeder Spieler
trägt ein begrenztes eigenes Inventar; abgelegt wird im Team-Lager, dem
Hauptspeicher und Entwicklungsort der Basis. Beute gehört dem Team.
Warum: Jede Loop-Phase füttert so ein eigenes Fortschritts-System —
Sammeln lässt die Basis wachsen, Kämpfen die Waffen; nichts ist
Pflichtübung. Upgraden ist Teamsache (Isor), also gehört auch die Beute
dem Team. Das begrenzte Trage-Inventar erzwingt Rückwege und speist das
Timer-Dilemma der Sammel-Phase.
Verworfen: nur Gegner-Drops als Quelle (die Sammel-Phase wäre leer,
niemand verließe die Basis); Mini-Dungeons als Materialquelle schon im
Grundspiel (eigenes Gewerk — als Ausbaustufe benannt); persönliche
Beute (Claudes Vorschlag — verworfen, weil Upgraden Teamzeug ist).

## 2026-10-09 — Waffen bestimmen die Rolle

Was: Kein Klassensystem. Die ausgerüstete Waffe bestimmt Rolle und
Fähigkeiten: Jede Waffe bringt ihren Basisangriff auf dem Normalklick
mit, dazu eine Leiste aus vier befüllbaren Fähigkeiten-Slots nach
LoL-Vorbild. Waffen liegen im Lager, werden dort entwickelt und sind
jederzeit tauschbar — Rollenwechsel ist ein Griff ins Regal. Zum Start
wenige Waffen (im Prototyp ein Nah-, ein Fernkampf); kreative und
witzige Waffen sind ausdrücklich erwünscht (Kandidat:
Sprungfeder-Boxhandschuh als Knockback-Werkzeug).
Warum: Streicht Klassensystem, Skill-Trees und persönliche
Fortschritts-Verwaltung — im Multiplayer ein geteilter Zustand statt
vier einzelner. Fantasy-Waffen-Archetypen sind sofort lesbar; der
Wechsel am Lager erzeugt den Team-Moment („macht jemand den Magier?")
und trägt auch solo. Waffen dürfen zugleich Gag und Funktion sein.
Verworfen: klassisches Klassensystem mit Charakterwahl; Fähigkeiten an
Charakter-Level gebunden; persönliche Waffen-Progression.

## 2026-10-09 — Wellen endlos, Dungeons als Quellen

Was: Die Wellen sind endlos und werden stärker; Ziel einer Partie ist
die höchste erreichte Welle. Die Spawn-Quellen sind feste, sichtbare
Dungeons auf der Karte; aktiv sind nur die im Radius um das Dorf, mit
steigenden Wellen erwachen weitere — die Eskalation kommt auch über
neue Angriffsrichtungen, nicht nur über stärkere Gegner.
Warum: Endlos mit Highscore ist Isors Zielbild. Sichtbare Quellen
machen die Verteidigung lesbar (Mauern zur Dungeon-Seite), erzeugen
räumliches Risiko beim Sammeln (das beste Material liegt nahe fremder
Dungeons) und legen den Teil-2-Anschluss schon auf die Karte: Dieselben
Eingänge sind später begehbar. Die Sorge „endlos heißt lange Partien"
ist entkräftet — die Partielänge regelt die Eskalationskurve, nicht das
Endlos-Prinzip (Richtwerte im GDD-Entwurf).
Verworfen: Sieg nach fester Wellenzahl (Claudes Vorschlag — Isor wählt
endlos); zufällig spawnende Quellen (unlesbar, kein Teil-2-Anker).

## 2026-10-09 — Werkbank-Gründung und Partie-Eröffnung

Was: Die Spieler starten mit der Werkbank im Gepäck und setzen sie frei
— wo die Bank steht, steht das Dorf. Wer nach etwa vier Minuten nicht
gesetzt hat, bekommt automatisch einen Platz in der Nähe. Der erste
Outbreak kommt nach etwa sieben bis acht Minuten: Zeit zum
Positionieren, für erste Mauern, kurzes Sammeln, Absprache.
Warum: Das Tutorial ist eine Handlung — aufheben und platzieren ist
genau das Kerninterface des Bausystems. Die Platzwahl ist die erste
Team-Entscheidung jeder Partie und macht jede Runde anders. Der
Auto-Timer fängt Unentschlossenheit und beendet Werkbank-Trolling,
ohne den Quatsch ganz zu verbieten.
Verworfen: fest vorgegebener Dorfplatz (leichter zu balancen, aber jede
Runde gleich); Gründung in einem Lobby-Raum außerhalb der Karte (die
Frage „Lobby oder Karte" löst sich auf — das Lager steht auf der Karte
und ist selbst das, was verteidigt wird).

## 2026-10-09 — Thema: Anime-Fantasy mit Abenteurer-Gilden

Was: Fantasy-Welt mit Adventure Guilds; die Spieler sind ein
Gilden-Trupp, der auf einer großen Insel einen Außenposten gründet.
Gegner sind klassische Fantasywesen — Goblins (Schwarm), Wölfe
(schnell), Orks (robust), Zyklopen (Brocken). Der Ton ist ein Mix:
Setting ernst gemeint, Verhalten komisch — hell, freundlich,
Physik-Slapstick. Die Welt ist eine Insel; die Spieler wachen dort auf.
Warum: Fantasy ist sofort lesbar und deckt die Waffen-Archetypen ab.
„Dungeon Break" ist ein etablierter Anime-Trope (Solo Leveling) — die
Zielgruppe kennt die Prämisse. Isor will ausdrücklich Witz dabei
(Ton-Anker: KonoSuba); der Witz entsteht aus Physik und Verhalten,
geschriebener Humor bleibt Würze. Die Insel ist die billigste saubere
Spielfeldgrenze (Wasser statt unsichtbarer Wände) und erlaubt den
Start ohne Story-Text.
Verworfen: reine Ernst-Fantasy (Isor will witzige Sachen); offene bzw.
endlose Welt (Begrenzungs- und Streaming-Aufwand ohne Nutzen für den
Loop).

## 2026-10-09 — Arbeitstitel „Isor's Outbreak"

Was: Der Arbeitstitel ist **Isor's Outbreak**, die Schicht heißt
`Projekte/Isors_Outbreak/`. Der Store-Name wird erst vor einem Release
entschieden.
Warum: Der Arbeitstitel hält die Doku zusammen und bindet nichts; die
Marke „Isor's …" stellt das Spiel neben Isor's Tower.
Verworfen: „Guildbreak" als Arbeitstitel (Claudes Favorit — beschreibt
das Genre für Fremde besser und bleibt Kandidat für den Store-Namen);
„Outpost Break".

## 2026-10-09 — Abgabe-Strategie: erst Mini-GDD, dann volles GDD

Was: Zuerst entsteht ein Mini-GDD-Pitch nur für die Freigabe durch die
Dozentin, danach das volle Pitch-GDD für die Abgabe. Die Abgabe bleibt
bewusst minimal; Erweiterungsideen stehen dort nur als wenige
Stichpunkte („modular erweiterbar"), die ausführlichen Ausarbeitungen
leben in den eigenen Notizen dieser Schicht. Vor jedem der beiden
Dokumente kommt eine eigene Layout-Runde (Aufbau zuerst, dann Punkt für
Punkt befüllen).
Warum: Isors Einschätzung der Freigabe („okay, aber klein halten") —
die Abgabe soll den minimalen Schnitt zeigen, die Ideen-Fabrik bleibt
intern. Vorarbeit ist gewollt, weil die Idee tragfähig wirkt.
Verworfen: alles direkt und ausführlich ins Abgabe-GDD schreiben (bläht
die Abgabe auf und widerspricht der erwarteten Freigabe-Auflage).

## 2026-10-09 — Mini-GDD: Zuschnitt und Versandweg

Was: Das Mini-GDD besteht aus fünf Blöcken — Kopf, Pitch, Ablauf einer
Partie, Umfang, Rahmen — auf einer Seite und geht als schlichte
Textdatei im Anhang einer Discord-Nachricht an die Dozentin; die
Nachricht selbst schreibt Isor. Der USP steht als Satz im Pitch, nicht
als eigener Block. Manuskript: `MINI_GDD.md` in dieser Schicht;
verschickt am 2026-10-09.
Warum: Die Freigabe beantwortet nur zwei Fragen — was ist es, und wie
groß ist es (Isor). Alles andere gehört ins volle Pitch-GDD
(Abgabe-Strategie oben). Eine Textdatei genügt dem Zweck; der
Abgabe-Bauweg über Word und PDF ist für einen Einseiter Überbau.
Verworfen: eigene Blöcke für USP und Referenzen (für die Entscheidung
der Dozentin unnötig); ein Zeitplan-Block (Isor: für sie egal); eine
Zeile zur vorhandenen Multiplayer-Vorarbeit (Isor: muss sie nicht
wissen, kommt mündlich, falls sie Bedenken äußert); der Versand als
PDF über die docx-Schiene (gebaut, dann als Überbau verworfen).

## 2026-10-09 — Multiplayer-Grundlage aus Isor's Tower wird übernommen

Was: Die für Isor's Tower gebaute und geprüfte Netz-Grundlage — Unity
Netcode for GameObjects mit Relay und Join-Code, Lobby samt
Bereit-Status und Chat, netzsynchrones Laden
(`Projekte/Isor_Tower/DECISIONS/Multiplayer.md`) — wird für Isor's
Outbreak übernommen statt neu gebaut.
Warum: Der Netz-Prüfstand ist bestanden (Verbindung über zwei Netze,
identische Weltgenerierung auf zwei CPUs — `PLAN.md`, Phase 0), und
mit dem Engine-Entscheid (`Uni/DECISIONS.md` → „2026-10-09 —
Engine-Entscheid: Das Semester-Spiel entsteht in Unity") passt die
Grundlage direkt. Multiplayer ist das größte Einzelrisiko des
Semesterspiels; übernommene, getestete Vorarbeit senkt es am
stärksten.
Verworfen: den Netz-Stack für das neue Spiel neu aufsetzen (Arbeit
ohne Erkenntnisgewinn); die Vorarbeit im Mini-GDD erwähnen (Eintrag
darüber).

## 2026-10-09 — Reihenfolge bis zur Abgabe: GDD vor Prototyp

Was: Erst entsteht die Erstfassung des vollen Pitch-GDD (bis zum
18.10.), dann startet der Prototyp. Beides ist am 27.11. fällig (Pitch
und Spieleprototyp), die Pitch-Präsentation am 03.12. nutzt Bilder und
kurze Videos aus dem Prototyp (`Uni/Semester_3/STUNDENPLAN.md`).
Warum: Isors Einschätzung — ein GDD ist ein Textdokument, die
Erstfassung braucht höchstens eine Woche, und ergänzen lässt sie sich
laufend. Die Präsentation nach dem Prototyp liefert echtes Material
und zahlt auf das Feedback-Kriterium „Prototyp berücksichtigt" ein.
Verworfen: Code-Start am Wochenende 17./18.10. vor dem GDD (alte
Übergabe aus der Ideenrunde); Prototyp-Start erst Ende Oktober (erste
Fassung im Gespräch — Isor zieht ihn direkt ans Ende der
GDD-Erstfassung).

## 2026-10-14 — Umfang-Schnitt: Kampf bleibt, aber minimal

Was: Die Spieler kämpfen weiter selbst. Das Kampfsystem schrumpft auf
das Minimum: Jede Waffe hat einen Basisangriff und genau eine
Fähigkeit (Feuerstab: Feuerball; Schwert: Hieb). Die Leiste mit vier
befüllbaren Fähigkeiten-Slots fällt aus dem Semester-Schnitt. Ob die
eine Fähigkeit über die Waffen-Entwicklung modifiziert wird, bleibt
offen (GDD → „Offene Design-Fragen").
Warum: Antwort auf das Freigabe-Feedback vom 2026-10-12 (`Uni/LOG.md`):
kleiner anfangen, vom 3D-Kampfsystem abgeraten. Das Selbst-Kämpfen ist
für Isor der Kern des Outbreak-Gefühls, und Outbreak muss sich von der
TD-Richtung von Isor's Detour unterscheiden; der Minimal-Schnitt zeigt
der Dozentin zugleich den kleinen Fokus.
Verworfen: Kampf streichen und nur Bauten (Türme, Fallen) verteidigen
lassen (rückt Outbreak zu nah an Detour); das Vier-Slots-System im
Semester-Schnitt behalten (widerspricht dem Feedback).

## 2026-10-14 — Kern-Schleife: Echtzeit ohne Phasenzwang

Was: Das Spiel erzwingt keine Phasen. Den Rhythmus gibt der sichtbar
angekündigte Outbreak vor; zwischen den Ausbrüchen ist das Team frei
(sammeln, bauen, reparieren). Die Kern-Spannung ist die Aufteilung:
wer rausgeht, wer bleibt, wer repariert. Wie die Timer ticken (fest
oder zufällig in Grenzen) und wie der Outbreak angekündigt wird
(UI-Timer, Umwelt, Portal-Färbung), bleibt offen; fest steht nur das
Prinzip „sichtbar angekündigt".
Warum: Isors Zielbild (2026-10-14): Die Spieler sollen eigene
Strategien entwickeln, statt einem Phasen-Skript zu folgen; die
Ankündigung muss sichtbar sein, weil „Gier gegen die Uhr" sichtbaren
Druck braucht.
Verworfen: feste Phasen (der Timer beendet das Sammeln, dann kommt
eine Bau-Phase) — die alte Lesart des Schleifen-Textes;
Rundenbasiertheit.

## 2026-10-14 — Herzobjekt: Niederlage und Gründung am selben Objekt

Was: Die Partie ist verloren, wenn das zentrale Herzobjekt der Basis
fällt (Arbeitsname „Siegelstein", Name offen). Spieler-Tode beenden
die Partie nie allein; Respawn-Regeln sind offen. Die Gründung hängt
am selben Objekt: Die Gruppe trägt es im Gepäck und setzt es frei auf
der Karte; die Umsetzung der Setz-Mechanik ist offen. Die Werkbank
verliert ihre Sonderrolle und wird eine normale baubare Station.
Warum: „Alle tot" als Partie-Ende findet Isor langweilig; verteidigt
werden soll ein Objekt, bei dem klar ist, warum ohne es alles verloren
ist. Die Werkbank trägt diese Story nicht (Isor, 2026-10-14). Anfang
und Ende am selben Objekt halten das Spiel klein, und die freie
Platzwahl bleibt erhalten.
Verworfen: die Werkbank als Verloren-Objekt (story-schwach); „alle
Spieler tot" als Kriterium (langweilig); die Kombination aus Objekt
und Spieler-Toden (vorerst, bewusst einfach gehalten).

## 2026-10-14 — Welt-Rahmen: feste Insel, zufällige Dungeon-Plätze

Was: Das Spielfeld ist eine fest gestaltete, bewusst kleine Insel; es
gibt genau eine Karte (Größe im Blockout, so klein wie möglich). Die
Dungeon-Plätze verteilt das Spiel zu Beginn jeder Partie zufällig neu,
danach stehen sie fest und sichtbar. Die Gruppe wacht immer am selben
Ort auf (ein Strand am Inselrand). Das Wasser ist die Grenze: ein paar
Schritte hineinlaufen geht, schwimmen nicht.
Warum: Die feste Insel ist der kleinste Schnitt (kein
Generierungs-Aufwand, Balancing in der Hand) und antwortet auf das
Freigabe-Feedback; die zufälligen Dungeon-Plätze geben trotzdem jeder
Runde ein anderes Gesicht und halten die Platzwahl der Gründung
frisch. Der frühere Verwurf „zufällig spawnende Quellen" (2026-10-09)
meinte Spawnen während der Partie; zufällige Plätze beim Partie-Start,
danach fest, bleiben lesbar. Fester Startstrand und die
Nasse-Füße-Grenze sind die jeweils einfachsten Lösungen (Isor: so
einfach wie möglich).
Verworfen: eine je Partie prozedural erzeugte Insel (durch die
Netz-Grundlage technisch gedeckt, aber größerer Aufwand ohne Not); ein
zufälliger Startpunkt; Schwimmen oder eine Schadens-Kante am Wasser.

## 2026-10-14 — Ressourcen: Staffelung und Verknappung statt Distanz-Regel

Was: Materialquellen liegen über die ganze Insel verteilt, alles
mehrfach, kein einzelner bester Ort: Häufiges wie Holz in Wäldern und
vereinzelt, Stein verstreut, seltenere Quellen wie Erz an wenigen
Stellen. Abgebaute Quellen sind verbraucht. Die Spannung der
Sammel-Phase entsteht aus der Verknappung: Die Umgebung der Basis ist
bald leergesammelt, die Wege werden mit jeder Runde länger. Ob
erschöpfte Quellen anderswo neu auftauchen, ist offen (GDD → „Offene
Design-Fragen"). Der Pitch-Satz „je weiter draußen, desto besser die
Beute" ist entsprechend ersetzt.
Warum: Isors Modell (2026-10-14): Der Spieler wählt den Basis-Platz
frei, eine feste Weiter-draußen-Regel passt dazu nicht. Die
Verknappung erzeugt den Laufweg von selbst und wächst mit der
Partie-Dauer, parallel zur Wellen-Eskalation; gebaut ist sie billig
(eine Quelle hat einen Vorrat und verschwindet leer).
Verworfen: der Distanz-Gradient „weiter draußen ergiebiger" (Teil des
Eintrags „Ressourcen-Ströme und Team-Lager" vom 2026-10-09 und des
alten Welt-Texts „bestes Material nah an fremden Dungeons"); gleiche
Verteilung ohne Seltenheits-Staffelung (ohne sie gäbe es vor dem
Greifen der Verknappung keinen Grund, weit zu gehen).

## 2026-10-15 — Waffen nur mit Basisangriff, Fähigkeiten werden Erweiterung

Was: Jede Waffe kann in der ersten Version genau eines: ihren
Basisangriff auf der Aktionstaste (das Schwert schlägt, der Bogen
schießt). Besondere Fähigkeiten je Waffe sind als spätere Erweiterung
vorgemerkt. Der Rest bleibt: kein Klassensystem, Waffen liegen im
Lager und sind jederzeit tauschbar, Start mit einem Nah- und einem
Fernkampf. Löst den Fähigkeiten-Teil des Eintrags „Umfang-Schnitt:
Kampf bleibt, aber minimal" (2026-10-14) ab; die offene Frage
„Fähigkeits-Modifikation" entfällt damit.
Warum: Noch ein Schnitt kleiner als am Vortag. Der Kampf bleibt Isors
Kern des Outbreak-Gefühls, aber fürs erste Spielgefühl reicht der
Basisangriff; als Erweiterungs-Stichpunkt zeigen die Fähigkeiten
zugleich die Ausbaufähigkeit des Waffen-Systems.
Verworfen: Basisangriff plus genau eine Fähigkeit (der Stand vom
2026-10-14); die Fähigkeit als modifizierbares Element der
Waffen-Entwicklung (stellt sich erst, wenn die Erweiterung kommt).

## 2026-10-15 — Steuerung: Maus/Tastatur und Controller, vorläufige Belegung

Was: Unterstützt werden Maus und Tastatur sowie Controller; die
Controller-Belegung entsteht im Prototyp. Vorläufige Belegung für Maus
und Tastatur: WASD laufen, Leertaste springen, linke Maustaste
Basisangriff und Aktion, E interagieren, I Inventar, B oder
Mausrad-Klick bauen, M Karte (geplant). Feinschliff im Prototyp; die
Bau-Eingabe samt Bau-Menü ist offen (GDD → „Offene Design-Fragen").
Warum: Ein Standard-Layout, das niemand lernen muss (Isor,
2026-10-15); früh festgehalten, damit Prototyp und GDD dieselbe
Sprache sprechen.
Verworfen: nichts — erste Festlegung, bewusst als vorläufig markiert.

## 2026-10-15 — Fall beim Outbreak: Beute bleibt am Fallort

Was: Kippt ein Spieler um, bleibt seine getragene Beute in einem
Behälter an der Stelle liegen und kann wieder eingesammelt werden.
Spieler-Tode beenden die Partie nie (Eintrag „Herzobjekt",
2026-10-14). Offen bleiben die Waffe des Gefallenen und der Rückweg
ins Spiel: Wiederbelebung durch Mitspieler, automatischer Respawn oder
beides — samt dem Rand-Fall „alle am Boden", der ohne Rückweg die
Partie hängen ließe, obwohl das Herzobjekt steht.
Warum: Der Behälter macht den Fall spürbar, ohne hart zu bestrafen,
und der Rückhol-Lauf ist noch einmal Gier gegen die Uhr. Gegenseitiges
Wiederbeleben reizt Isor als Spannungsquelle; entschieden wird das mit
dem Prototyp.
Verworfen: nichts ausdrücklich — der Behälter war Isors einzige
Setzung, Alternativen (Beute-Verlust, Beute bleibt im Inventar) kamen
nicht zur Wahl.

## 2026-10-15 — Persistenz: jede Partie startet bei null

Was: Über die Partie hinaus bleibt nichts bestehen; jede Partie
startet bei null. Fortschritt über Partien hinweg (Festung, Waffen,
Freischaltungen) ist als Erweiterung vorgemerkt, bewusst weit hinten
in der Reihe. Die offene Frage „Persistenz über Partien" ist damit
geschlossen.
Warum: Passt zum Highscore-Prinzip (jede Partie ist ein eigener
Anlauf), hält die erste Version klein und deckt sich mit dem, was das
Mini-GDD bereits als Ausbaustufe benannt hat.
Verworfen: Meta-Progression in der ersten Version (Content- und
Balance-Kosten ohne Not; „ganz weit weg", Isor 2026-10-15).

## 2026-10-15 — Basis-Bau der ersten Version: Mauern, eine Werkbank, drei Rohstoffe

Was: Gebaut werden in der ersten Version nur Mauern, wahlweise aus
Holz oder Stein (der Unterschied läuft über die Textur). Tore und
Türen gibt es nicht; wer die Basis schließt, lässt eine Lücke als
Eingang und verteidigt dort. Einzige Station ist die Werkbank (der
Platz zum Schmieden und Entwickeln); weitere Stationen und Tore sind
als Erweiterung vorgemerkt. Repariert wird mit Material. Die
Rohstoffe sind Holz, Stein und ein seltenes Erz (Arbeitsname
Mithril).
Warum: So klein wie möglich (Isor, 2026-10-15): Tore sind technisch
aufwendig, und die offene Lücke erzeugt von selbst den bewachten
Engpass — eine Verteidigungs-Entscheidung statt einer Tür-Mechanik.
Eine Mauer-Mechanik mit zwei Texturen ist billiger als zwei
Bausysteme.
Verworfen: Tore und Türen in der ersten Version (zu schwer, Isor);
mehrere Werkstationen zum Start.

## 2026-10-15 — Gegner-Eskalation: wenige Typen, Varianten, Nachschub

Was: Zum Start gibt es zwei bis vier Gegnertypen (Kandidaten-Pool
sind die vier aus dem Thema-Kapitel: Goblins, Wölfe, Orks, Zyklopen);
die genaue Zahl entscheidet der Prototyp (GDD → offene Frage
„Umfang-Feinschnitt"). Die Eskalation läuft über das gesamte
Spielerlebnis: erst wenige Gegner, dann mehr, nach und nach stärkere
Varianten (etwa ein Goblin-Krieger) und neue Typen, dazu erwachende
Dungeons als neue Angriffsrichtungen.
Warum: Vorbild ist die Blutmond-Kurve aus 7 Days to Die (Isor,
2026-10-15): Menge, Varianten und neue Typen ergeben eine lange
Eskalation aus wenig Content; Varianten desselben Typs sind
Asset-günstig.
Verworfen: eine feste Festlegung auf alle vier Typen zum Start (der
Feinschnitt bleibt beim Prototyp).

## 2026-10-15 — Benutzeroberfläche: schlankes HUD, Rasterinventar, kurzer Menüfluss

Was: Das HUD zeigt ständig Welle, Outbreak-Ankündigung, eigenes Leben
und die Quickslot-Leiste (erste Inventar-Reihe, bestimmt die Hand);
dazu den Herzobjekt-Zustand mit Basis-Alarm, eine
Mitspieler-Lebensanzeige mit Am-Boden-Signal und einen
Richtungs-Anker zur Basis. Material-Zähler wohnen im Inventar
(Rasterfenster auf I, darüber Figur und getragene Slots). Gebaut wird
über ein Radialmenü (vorläufig). Menüfluss: Hauptmenü,
Hosten/Beitreten per Join-Code, Lobby mit Bereit-Status und Chat,
Partie; dazu ein kleines Pausenmenü und ein Abschlussbildschirm mit
der erreichten Welle. Minimap als Erweiterung. Gestaltungsregel:
Wichtige Zustände nie allein über Farbe unterscheiden (besonders
nicht Rot gegen Grün), immer Form oder Text dazu.
Warum: Ein schlankes HUD passt zum kleinen Schnitt. Herzobjekt-Anzeige
und Basis-Alarm folgen aus der Niederlage am Herzobjekt (sonst verliert
man ungesehen), Mitspieler-Status aus dem Revive-Gedanken,
Richtungs-Anker aus der fehlenden Minimap. Der Abschlussbildschirm ist
die Auszahlung des Highscore-Ziels. Die Farb-Regel ist
Barrierefreiheit und bei Isor gelebte Praxis.
Verworfen: Material-Zähler dauerhaft im HUD (wohnen im Inventar); eine
Minimap in der ersten Version (später, falls Zeit).

## 2026-10-16 — Thema-Rest: Gilden-Welt, eigene Welt, Low-Poly-Stil

Was: Die Welt bleibt eine Welt der Abenteurer-Gilden; die Spieler
selbst gehören keiner an, die Gilden zeigen sich über visuelle
Andeutungen in der Welt (Ruinen, Zeichen, Easter Eggs). Die Welt ist
eine eigene, keine Fortsetzung von Isor's Tower; sie teilt Themen und
Stil-Vorbild (Chop Chop Inc.). Das Aussehen ist stylized und low-poly
im Anime-Stil mit bewusst einfachen Assets; das Vorbild gibt die
Richtung vor, nicht den Detailgrad. Witz wird nicht eigens dosiert
oder geregelt: Der Humor entsteht aus Physik und Waffen-Design. Die
konkreten Gegnertypen bleiben offen, fest sind ihre Rollen (Schwarm,
schnell, robust, Brocken); die Besetzung entscheidet die
Asset-Sichtung (GDD → „Offene Design-Fragen", „Gegner-Besetzung").
Damit sind die offenen Fragen Gilden-Rahmung, Universum und
Witz-Dosierung geschlossen.
Warum: Die Gilden-Welt trägt die Umgebungs-Erzählung und das
Fantasy-Flair ohne Story-Kosten. Eine eigene Welt lässt dem Spiel
Freiheit, der Stil bleibt am Toon-Shader-Lernpfad. Low-Poly mit
einfachen Assets ist der realistische Zuschnitt (Art über fertige
Packs, frei oder zugekauft). Monster erst nach der Asset-Sichtung zu
besetzen vermeidet, dass das GDD Wesen verspricht, für die es keine
Modelle gibt (Isor, 2026-10-16).
Verworfen: die Gilden ganz streichen (die Welt verlöre Flair und
Easter-Egg-Quelle); die Insel in der Tower-Welt verorten; eine feste
Monster-Liste vor der Asset-Sichtung.

## 2026-10-16 — Audio: Musik als Phasen-Signal, Sounds für alle Bereiche

Was: Die Musik arbeitet als Phasen-Signal (ruhig beim Sammeln,
druckvoll zum und im Outbreak); den Wechsel soll man hören, nicht nur
sehen. Sounds decken alle Spielbereiche ab: Waffen und Treffer,
Spieler, Gegner samt Kriegsschrei beim Ausbruch, Beute, Bauen und
Reparieren, Benutzeroberfläche. Besonderes Gewicht hat der
Physik-Slapstick. Quellen sind fertige Packs, frei oder zugekauft,
dieselbe Linie wie bei den 3D-Assets.
Warum: Der Loop lebt von der hörbaren Ankündigung (die
Outbreak-Ankündigung ist noch offen, der Klang trägt sie in jedem
Fall), und der Slapstick funktioniert ohne Sound nicht. Fertige Packs
passen zum Solo-Rahmen; Isors Hinweis vom 2026-10-16: Die Sound-Liste
ist breiter als nur Musik und Kriegsschrei, weil jedes System
(Waffen, Spieler, Drops, Gegner, UI, Bauen) eigene Sounds braucht.
Verworfen: nichts ausdrücklich; eigene Musik- oder Sound-Produktion
stand im Solo-Rahmen nie zur Wahl.

## 2026-10-16 — Referenzen: nur selbst gekannte Titel, keine Quervergleiche

Was: Das Referenzen-Kapitel nennt 7 Days to Die, Dungeon Defenders,
Orcs Must Die! Deathtrap, R.E.P.O., RV There Yet?, Chop Chop Inc. und
Solo Leveling, je mit einem Satz, was Isor's Outbreak daraus zieht.
Dome Keeper und KonoSuba sind gestrichen. Die Abgrenzung beschreibt
nur, was diese Nachbarn nicht besetzen; sie vergleicht nicht gegen
Genres oder Konzepte außerhalb der Liste.
Warum: Ins Dokument kommen nur Referenzen, die Isor selbst kennt und
im Gespräch vertreten kann; Dome Keeper und KonoSuba kamen aus Claudes
Ideenrunde. Und das GDD steht für sich: Verweise auf Ideen außerhalb
des Spiels (etwa Pfad-Verteidigungen) sagen Außenstehenden nichts
(Isor, 2026-10-16).
Verworfen: Dome Keeper und KonoSuba als Referenzen; der
Abgrenzungs-Satz gegen Pfad-Verteidigungen.

## 2026-10-16 — Zeitplan: Meilensteine statt Kalenderdaten

Was: Das Zeitplan-Kapitel besteht aus sieben Meilensteinen mit groben
Dauer-Schätzungen (Wochen), ohne Kalenderdaten; Daten bekommt der Plan
beim Projektstart. Jeder Meilenstein trägt Reserve, Gekipptes fällt in
die Erweiterungsliste.
Warum: Ob Isor's Outbreak gebaut wird, entscheidet die Wahl zwischen
den beiden Konzepten (`Uni/DECISIONS.md` → „2026-10-13 — Zwei Konzepte
parallel bis zur Wahl der Dozentin"); ein datierter Plan für ein
ungewähltes Konzept wäre nach einer Woche falsch (Isor, 2026-10-16).
Dauer-Schätzungen zeigen die Größenordnung trotzdem.
Verworfen: Kalenderdaten oder Monatsangaben (erster Vorschlag);
Meilensteine ganz ohne Dauer-Angaben (die Schätzungen kamen auf Isors
Zuruf dazu).

## 2026-10-16 — Titel: „It's Dungeon Outbreak Time"

Was: Das Spiel heißt im GDD und auf dem Deckblatt „It's Dungeon
Outbreak Time", Kurzform im Text „It's D.O.T". Löst „Isor's Outbreak"
als Außentitel ab (Eintrag „Arbeitstitel ‚Isor's Outbreak'",
2026-10-09); die Harness-Schicht behält ihren Namen
`Projekte/Isors_Outbreak/` — ein Ordner-Umzug brächte nichts und
kostete Verweise.
Warum: Isors Wahl beim Deckblatt-Bau (2026-10-16): Der Name beschreibt
den Kern-Moment des Spiels, und Cover und Manuskript müssen denselben
Titel tragen. Die Bedenken aus der Ideenrunde (DoT-Lesart als Damage
over Time, „dot" als Suchwort schwach) bleiben notiert und werden vor
einem Store-Release erneut gewogen.
Verworfen: „Isor's Outbreak" als Außentitel behalten (dann hätte das
Cover zurückgeglichen werden müssen); die Schicht mit umbenennen.

## 2026-10-17 — Schicht-Umzug nach Its_DOT

Was: Die Schicht heißt jetzt `Projekte/Its_DOT/` statt
`Projekte/Isors_Outbreak/` (git mv, die Datei-Historie bleibt). Damit
trägt alles einen Namen: Spiel „It's Dungeon Outbreak Time" → Kürzel
It's D.O.T → Projekt-Repo `Its-DOT` → Unity-Projekt `ItsDOT` →
Schicht `Its_DOT`. Löst den Schicht-Teil des Eintrags „2026-10-16 —
Titel: ‚It's Dungeon Outbreak Time'" ab; die lebenden Verweise
(PLAN, Uni/ROADMAP, GLOSSARY, ARTIFACT_INDEX, Ownership-Köpfe) sind
nachgezogen, der INDEX ist neu erzeugt, Chroniken bleiben unverändert.
Warum: Isors Zuruf beim P1-Projektstart (2026-10-17): Er will das
Spiel überall unter einem Namen wiederfinden. Das Argument vom
16.10. gegen den Umzug („brächte nichts und kostete Verweise") fiel
mit dem Projektstart: Jetzt entstehen Repo und Unity-Projekt neu, und
jeder weitere Arbeitstag hätte frische Verweise auf den alten Namen
erzeugt — billiger als heute wird der Umzug nie wieder.
Verworfen: `Isors_Outbreak` behalten (ständiger Namensbruch zwischen
Schicht und Spiel); ein `Isors_Its_DOT` (anders als beim Tower steckt
Isors Name nicht im Spieltitel). Das Repo `Its-DOT` bleibt übrigens
auch dann D.O.T-Eigentum, wenn die Konzept-Wahl auf Pathmakers TD
fällt — Pathmakers bekäme ein eigenes Repo, denn D.O.T wird
voraussichtlich irgendwann weiterentwickelt (Isor, 2026-10-17).

## 2026-10-17 — P1-Zuschnitt: Nur die MainMenu-Kette zieht um

Was: Das Spiel entsteht in einem frischen Unity-Projekt (`ItsDOT` im
Repo `Its-DOT`, Marke `PROJEKT_ITS_DOT` in `Kern/PFADE.md`). Aus dem
Tower-Prototyp kommt ausschließlich die MainMenu-Kette mit: die Szene
und alles, was sie referenziert (NetWorking- und GameFlow-Skripte,
Menü-UI, Fonts, Mixer) — per Export Package mit Include dependencies.
Zwei Code-Abhängigkeiten, die der Export nicht sieht, kamen von Hand
nach (`ISessionService`, `RelaySessionService`); der
PlayerLook-Verweis in `GameSettings` wurde gekappt, statt den alten
Player zu holen. Alles andere wird neu gebaut; einzelne Alt-Skripte
gezielt nachzuholen bleibt erlaubt, der Standard ist Neubau.
Warum: Kein Asset- und Code-Altbestand im neuen Spiel — jede Zeile
soll für D.O.T entstanden oder bewusst übernommen sein (Isor,
2026-10-17). Die übernommene Kette ist die „vorhandene, erprobte
Grundlage" aus dem GDD.
Verworfen: Im Prototyp-Projekt weiterarbeiten (voller Altbestand);
breitere Übernahme wiederverwendbarer Systeme — Player, Health,
Timer, Diagnostic (Claudes Vorschlag); Ordner von Hand kopieren statt
Abhängigkeits-Export.

## 2026-10-17 — Unity 6.3 LTS und ein eigenes UGS-Projekt

Was: Das neue Projekt läuft auf Unity 6.3 LTS (6000.3.26f1,
URP-Template) und hängt an einem eigenen
Unity-Gaming-Services-Projekt (ItsDOT, verknüpft am 2026-10-17).
Pakete: Netcode for GameObjects 2.13.3, Multiplayer Services 2.4.1,
Input System 1.20.1.
Warum: LTS trägt über Semester, Abgabe und darüber hinaus
(Kurs-Regel „immer LTS"); die Modul-Vorgabe 6000.0.59f2 läuft aus dem
Support, und die Dozentin sieht die Versionsfrage entspannt. Der
Import aus dem 6000.5-Prototyp war damit ein Downgrade — bewusst in
Kauf genommen, weil nur Szene und Prefabs Format-Risiko trugen und
Skripte als Quelltext sicher ankommen; der Play-Test bestätigte den
Import. Eigenes UGS-Projekt, weil D.O.T ein eigenes Spiel ist: einmal
zehn Minuten Einrichtung statt dauerhaft geteilter Statistik mit dem
Tower.
Verworfen: Unity 6.6 (sichere Import-Richtung, aber kein LTS); beim
6000.5-Stand bleiben (aus dem Installer gefallen, Tech-Support
endet); das UGS-Projekt des Prototyps weiternutzen.

## 2026-10-18 — Alle Startwege zielen auf die Testarea

Was: `SceneId` ist auf `{ MainMenu, Testarea }` geschnitten;
Host-Start, Solo und der alte Direktstart laden dieselbe
Testarea-Szene. Leere Szene angelegt, Build-Szenenliste MainMenu
(Index 0) plus Testarea.
Warum: P1 hat genau ein Ziel — die Testarea; Solo läuft ohnehin als
lokaler Host über dieselbe Netz-Schiene, ein zweites Ziel wäre ein
toter Enum-Eintrag.
Verworfen: Die Tower-Ziele Village/StarterVillage als Platzhalter
behalten.

## 2026-10-18 — Testarea-Zuschnitt: sieben Bausteine, Multiplayer von Tag eins

Was: Die Testarea besteht aus B1–B7 (Testarea + Spieler im Netz ·
Nahkampf + Schaden · simple Gegner-KI · Dungeon-Portal · Loot-Drop ·
Quick-Slot-HUD · Fall + Respawn), geschätzt 27–35 h gegen ein
realistisches Budget von 25–30 h. Fernkampf ist Reserve, der
Relay-Echttest läuft im ersten Koop-Test mit, das Herzobjekt
existiert nur als Spawn-Platzhalter. Die T1-Mengenmessung ist bewusst
in die Vollproduktion verschoben. Jeder Baustein beginnt mit einer
Design-Runde (Isors Entwurf zuerst); der NGO-Wiedereinstieg wird
parallel gelernt, immer im Baustein, der die Technik braucht.
Warum: Zweck der Testarea ist allein Isors Konzept-Entscheidung
(It's D.O.T gegen Pathmakers TD) — gebaut wird nur, was diese
Entscheidung informiert. Die zwei Wochen sind Ziel, keine Frist;
hart ist nur der 27.11. Die Energielage (Rücken, Motivationstief,
von Isor am 2026-10-18 gemeldet) spricht zusätzlich für kleine,
einzeln abschließbare Bausteine.
Verworfen: 200er-Peak jetzt messen (beantwortet keine Konzept-Frage,
kostet die Testarea); erst solo bauen und später vernetzen
(Nachrüsten ist teurer als der Aufschlag je Baustein); zwei Waffen
von Anfang an.

## 2026-10-18 — Fall beim Outbreak: Wiederbeleben und 10-Sekunden-Respawn

Was: Gefallene können von Mitspielern wiederbelebt werden (das Wie
wird später festgelegt); parallel läuft ein 10-Sekunden-Timer,
danach respawnt der Gefallene am Herzobjekt. Getragene Beute bleibt
im Container am Todesort liegen und wird wiedergeholt. Verloren ist
die Partie ausschließlich durch den Fall des Herzobjekts. Offen
bleibt nur der Waffen-Teil der GDD-Frage (behält der Gefallene seine
Waffe?).
Warum: Beantwortet die offene GDD-Frage „Fall beim Outbreak" samt
Hänger-Fall — mit Auto-Respawn kann die Partie nicht mehr hängen,
solange das Herzobjekt steht. Das GDD bleibt bis zur Konzept-Wahl
eingefroren (Eintrag vom 2026-10-16) und wird bei der Vertiefung
nachgezogen; bis dahin trägt dieser Eintrag die Antwort.
Verworfen: nur Wiederbelebung ohne Timer (der Hänger-Fall „alle am
Boden" bliebe offen).

## 2026-10-18 — Quick-Slot-HUD statt Inventar

Was: Kein Inventar-Fenster. Eine Minecraft-artige Hotbar unten im
HUD trägt die Waffen-Slots — die „Slot-Befüllung" aus dem P1-Auftrag
meint genau die Befüllung dieser Quick-Slots. Zwei bis drei
Loot-Sorten laufen daneben als Zähler im HUD. Aufheben belegt oder
ersetzt Slots; kein Drag-and-Drop, kein Grid.
Warum: Liefert das Loot- und Equip-Gefühl für die
Konzept-Entscheidung zum Bruchteil der Kosten und entspricht der
GDD-Linie „Rollenwechsel ist ein Griff ins Regal, keine
Menüentscheidung".
Verworfen: Inventar-Fenster mit Grid (ein Abendblock für eine Frage,
die die Hotbar auch beantwortet); nur Zähler ganz ohne Slots (das
Equip-Gefühl fiele weg).

## 2026-10-18 — Testarea-Aufbau: wachsende Gym-Szene auf Kachel-Plane

Was: Die Testarea ist eine Szene, die als „Gym" wächst: eine flache
Kachel-Plane (1 Kachel = 1 m) statt Unity Terrain, darauf Primitive
als Teststationen (Rampen mit 20/40/60°, Stufen), Zonen nebeneinander
in Laufweite; jedes System soll dort einmal existieren und testbar
sein (Isors Zielbild für jedes Spiel). Spawn versetzt am
Herzobjekt-Platzhalter: vier Punkte im Kreis, damit niemand ineinander
spawnt. Die Szene bleibt eine normale Build-Szene, kein Editor-Ordner.
Leitplanke: Das Movement wird terrain-tauglich gebaut (Bodenabfrage
über Kontakt und Raycast, keine Flachboden-Annahmen), damit die echte
Insel später Unity Terrain sein kann — einmal im Editor erzeugt oder
von Hand, offen bis zur Vollproduktion; die feste Insel vom 2026-10-14
bleibt. Vorgemerkt: Teleporter zwischen Zonen mit Beschriftung, eine
Loot-Schau-Zone, ein eigener Testarea-Editor, ein separater
Test-Build ohne Testarea in der Spiel-Szenenliste, ein Buckelfeld als
Terrain-Probe-Station.
Warum: Am Parcours wird gegen bekannte Werte getestet — eine Rampe aus
einem gedrehten Würfel hat einen exakten Winkel, gemaltes Terrain nie.
Unity nimmt Inhalte von `Editor/`-Ordnern nicht in Builds auf, und der
lokale Multiplayer-Test (Editor + gebauter Spieler) braucht die Szene
im Build; dazu zielen seit dem 2026-10-18 alle Startwege auf die
Testarea. Terrain ist örtlich nur eine Schräge — wer Rampen und Stufen
besteht, besteht Terrain, die Regler wirken auf jedem Collider gleich.
Verworfen: Unity Terrain für die Testarea (Winkel unbekannt,
Terrain-Sonderfälle testen das Movement, bevor es eines gibt); die
Szene in einem Editor-Ordner (fliegt aus jedem Build); alle Spieler
auf demselben Spawnpunkt (Physik schiebt sie auseinander).

## 2026-10-19 — Movement-Fundament: eigener Controller auf Rigidbody-Basis

Was: Die Spielerfigur bekommt einen selbst geschriebenen Controller
auf Rigidbody-Basis: Isor schreibt die Steuerlogik (Input, Absicht,
Sprungkraft, Bodencheck per SphereCast), die Physik-Engine liefert
Kollision und Kräfte. Treppen werden über unsichtbare Rampen-Collider
gelöst. Auf fremden Figuren läuft der Rigidbody kinematisch, nur der
Owner simuliert. Eingabe und Bewegungsabsicht bleiben vom „Motor"
getrennt — die Versicherung, falls das Fundament je getauscht wird.
Warum: D.O.T ist laut GDD ein Physik-Slapstick-Spiel — Schubsen,
Knockback und der Sprungfeder-Boxhandschuh kommen beim Rigidbody echt
aus der Simulation statt nachgebaut. Isors extern eingeholter Rat
(„lieber selbst bauen als Unitys Fertigteil") wurde geprüft und trägt
für dieses Spiel: Beim CharacterController wirken Kräfte nicht
automatisch auf die Figur zurück, und seine Kollisionsauflösung ist
eine Blackbox. Der Mehrpreis (~2–3 h plus Tuning) ist bewusst
akzeptiert; der Code der Testarea ist Original-Code und wird später
erweitert, nicht neu geschrieben (Isor, 2026-10-19).
Verworfen: CharacterController (Claudes erste Empfehlung — die
Budget-Antwort: billiger, aber jede Physik-Reaktion von Hand);
voll-eigener kinematischer Controller mit selbst geschriebener
Kollisionsauflösung (Expertenaufgabe in Wochen statt Stunden — nicht
nie, aber nicht in B1).

## 2026-10-19 — Movement-Umfang V1 und B1-Bau-Reihenfolge

Was: Version 1 des Movements umfasst das Gerüst (Kapsel mit
eingefrorener Rotation, kamera-relatives Laufen mit Beschleunigen und
Bremsen, SphereCast-Bodencheck, Schrägen-Limit, Grundsprung,
Schwerkraft, reduzierte Luftsteuerung, Owner-Autorität im Netz) plus
das komplette Sprunggefühl-Paket — Coyote Time, Jump Buffer, stärkerer
Fall, variable Sprunghöhe — plus die Struktur-Vorhalte:
Knockback-Einstiegspunkt am Motor, Tuning-Werte als einfache
Inspector-Felder, Tempo-Faktor in der Absicht als Sprint-Vorhalt. Die
Kamera wird eine eigene Orbit-Kamera (dritte Person, Maus dreht,
Mausrad zoomt; Wand-Kollision per SphereCast erst, wenn sie stört).
Bau-Reihenfolge: Blockout → NGO-Gerüst → Kamera → Motor →
Sprunggefühl und Vorhalte → Abnahme; das Netz kommt in Schritt 2,
nicht am Ende. Ehrliche B1-Schätzung damit ~8,5 h statt 6–8.
Warum: Isors Vorgabe „nicht zu minimalistisch, Original-Code, später
nur erweitern" — erweiterbar machen die Andockpunkte, nicht die
Featurezahl, und alle vier Sprunggefühl-Posten sind Motor-Interna
ohne Ausbau-Kosten. Netz ab Schritt 2, weil der Testarea-Zuschnitt
Multiplayer von Tag eins verlangt und Solo ohnehin als lokaler Host
läuft: Jeder spätere Schritt wird im echten Netz-Aufbau getestet,
statt Ownership nachzurüsten. Die eigene Kamera passt zur Linie
„original statt Fertigteil" und ist klassischer Semester-Stoff.
Verworfen: Cinemachine (schneller fertig, Wand-Kollision gratis — aber
wieder eine Blackbox); Dash/Rolle in V1 (Kampf-Design-Frage für
später, der Andockpunkt existiert durch die Struktur); Tuning als
ScriptableObject nach dem Awake-Seed-Muster schon jetzt (in B1 gibt es
ein Spieler-Prefab, der Umzug ist später ein mechanischer Handgriff);
Netz zuletzt (Nachrüsten ist teurer als der Aufschlag je Schritt).

## 2026-10-20 — B1-Stopp bei der Konzept-Wahl

Was: Der Testarea-Bau endet mitten in B1, Schritt 1 (Blockout). Gebaut
und im Repo: Kachel-Boden mit Grid-Material (1 Kachel = 1 m),
Wandraster mit 9×10 Räumen à 100×100 m auf Layer Wall, der
Parcours-Rohbau (Treppe maßhaltig; die Rampen noch 1 m kurz, beide
Obstacles noch 1 m hoch), vier Spawn-Punkte um das mittig gesetzte
Herzobjekt (Abstände noch 29–43 m statt 2–3 m), alles Begehbare auf
Layer Ground. Der Teleporter war am 2026-10-20 in B1 vorgezogen worden
(die Räume sind komplett ummauert, ohne ihn kommt niemand hinaus) und
ist nicht mehr entstanden. Die Szene bleibt als Stand im Repo;
B2–B7 starten nicht.
Warum: Konzept-Wahl vom 2026-10-20 (`Uni/DECISIONS.md` → „2026-10-20 —
Semester-Spiel: Pathmakers TD; It's D.O.T wird privates Projekt") —
D.O.T ruht ohne Termin, Weiterbauen nähme dem Semesterprojekt Zeit,
und die Testarea hat ihren Zweck, die Konzept-Entscheidung zu
informieren, mit der Wahl verloren. Das Design der B1-Runde
(Rigidbody-Controller, Movement-V1, Sprunggefühl-Paket, Orbit-Kamera)
bleibt dokumentiert und ist für Pathmakers TD nutzbar — auch dort
kommen vier Spieler über Relay zusammen und brauchen eine Spielerfigur.
Verworfen: B1 noch zu Ende bauen (Zeit gehört ab jetzt Pathmakers TD);
die Testarea-Szene verwerfen (kostet im Repo nichts und trägt den
Stand fürs private Weiterbauen).
