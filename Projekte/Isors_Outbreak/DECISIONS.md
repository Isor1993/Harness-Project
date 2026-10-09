# DECISIONS.md — Entscheidungen Isor's Outbreak

Ownership: Nur Entscheidungen zum Koop-Spiel Isor's Outbreak
(Arbeitstitel; das Semester-Spiel des Moduls 5-101) — was entschieden
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
