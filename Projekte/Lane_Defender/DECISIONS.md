# DECISIONS.md — Entscheidungen Lane Defender

Ownership: Nur Entscheidungen zum C++-Konsolenprojekt Lane Defender
(früherer Arbeitstitel: Grid Defense) — was
entschieden wurde, warum, und welche Alternativen verworfen wurden. Kein
Plan (ROADMAP), kein Ereignis (LOG), keine Zeitschätzung (ZEITPLAN.md
dieser Schicht). Die Uni-Aufgabenstellung gehört der Uni-Schicht.
Format: `## JJJJ-MM-TT — Titel` mit **Was** / **Warum** / **Verworfen**.
Älteste oben, wie in einer Chronik.

## 2026-09-07 — Konsolen-Tower-Defense als Projektidee
Was: Das C++-Konsolenprojekt des Moduls 5-101 wird ein minimalistisches
Tower-Defense im Konsolen-Grid, Arbeitstitel **Grid Defense** — ein
eigenständiges Projekt ohne Bezug zu Isor's Tower (Isor, ausdrücklich).
Warum: Deckt die Pflichtthemen natürlich ab (Gegner-Hierarchie = OOP,
Zielwahl der Türme = Pointer, Spawn/Despawn je Welle = Memory Management)
und doppelt sich nicht mit Isors früheren Abgaben — die Dozentenschaft
kennt seinen Monsterkampf-Simulator und seinen Escape Room bereits.
Verworfen: Turm-Aufstiegs-Kampfsimulator (zu nah am alten
Monsterkampf-Simulator); Escape Room (schon einmal abgegeben);
Nutz-Tools wie Zeitplaner oder Karteikarten-Trainer (OOP wirkt dort
aufgesetzt, viel Texteingabe); raylib als Grafik-Basis (Setup-Reibung
und Zeitrisiko — als Kür nach fertigem Pflichtteil weiter möglich);
Anbindung an Isor's Tower (separates Projekt gewünscht).
**Fortgeführt am 2026-09-07:** eigenständiges Konsolenspiel ohne
Isor's-Tower-Bezug und ohne raylib-Basis gilt weiter; die Spielform
Tower-Defense ist abgelöst durch „Umschwenk auf den Lane-Shooter" (unten).

## 2026-09-07 — Spielregeln der Pflichtfassung
Was: Zwei Gegnertypen (Tank `♜` viel Leben/langsam · Runner `♞`
schnell/normal), je Welle stärker skaliert. Drei Turmtypen (AOE-Kanone ·
Schnellschütze · Slow-Turm, Slow als Einzelziel), Reichweite fest
3 Zellen, eine Upgrade-Taste, kein Verkaufen. Ein festes Pfad-Layout;
gebaut wird überall außer auf dem Pfad, Cursor per Pfeiltasten,
Turmwahl mit 1/2/3. 20 Leben, −1 je Durchbrecher, bei 0 Niederlage;
10 Wellen bis zum Sieg. Hauptmenü mit Spieltitel, Start/Exit und
Namenseingabe; ein Info-Panel unter dem Grid zeigt kontextabhängig
Baukosten bzw. Turmwerte samt Upgrade-Status. Optik: Konsole mit
Farben, Schüsse als Punkte in Turmfarbe, AOE-Einschlag als kurzer
`✸`-Blitz, verlangsamte Gegner cyan eingefärbt.
Warum: Isors Zuschnitt vom 2026-09-07 — bewusst minimalistisch, damit
die erste Semesterhälfte schnell und trotzdem auf First-Niveau
abschließt; jede Mechanik zahlt auf ein Pflichtthema oder ein
Feedbackelement (Input-Validierung, verständliche Ausgabe) ein.
Verworfen: fünf bis sechs Gegnertypen ab Start (Content-Flut ohne
Lernwert — billiger Ausbau, sobald die Hierarchie steht); AOE-Slow
(komplexeste Mechanik am einfachsten Turm — Ausbau); zweites
Pfad-Layout ab Start (Ausbau); Verkaufen-Funktion (Isor);
Reichweiten-Anzeige je Turm (feste, bekannte Reichweite genügt).
**Abgelöst am 2026-09-07** durch „Umschwenk auf den Lane-Shooter"
(unten); übernommen wurden zwei skalierende Gegnertypen, 20 Leben und
das Hauptmenü mit Namenseingabe.

## 2026-09-07 — Tick-Modell: Rundensimulation, Eingabe nur zwischen Wellen
Was: Die Rundenphase läuft als Tick-Schleife — bewegen → schießen →
Projektile → aufräumen → **einmal** zeichnen → ~200 ms Pause. Alle
Zeiten sind Tick-Zähler (Feuerrate, Gegner-Tempo, Slow-Dauer). Gebaut
wird nur in der Bauphase mit blockierender Tastenabfrage. Gezeichnet
wird pro Tick genau einmal: kompletter Frame als Text-Puffer,
Cursor-Home statt Bildschirm löschen; jede Grid-Zelle ist zwei Zeichen
breit.
Warum: Ohne Eingabe während der Welle entfällt die nicht-blockierende
Tastatur — der einzige wirklich fummelige Teil eines Konsolen-TD. Das
Ein-Puffer-Rendering verhindert Flackern und halbe Zustände; die
Doppelzellen halten das Raster stabil, weil Symbole wie Schachfiguren
je nach Schrift verschieden breit sind. Machbarkeit am 2026-09-07 per
interaktiver Tick-Demo gezeigt (Session, Widget).
Verworfen: Echtzeit mit Live-Eingriff (als Ausbau „Speed-Taste"
nachrüstbar); Bildschirm löschen je Frame (Flackern); Einzelzellbreite.
**Fortgeführt am 2026-09-07:** Tick-Schleife, Ein-Puffer-Rendering mit
Cursor-Home und Doppelzellbreite gelten unverändert; abgelöst ist nur
„Eingabe nur zwischen den Wellen" — der Lane-Shooter braucht
Live-Eingabe, siehe „Umschwenk auf den Lane-Shooter" (unten).

## 2026-09-07 — Das Projekt ist der Kurs: Lernen am Bauwerk
Was: C++ wird direkt an Grid Defense gelernt. Kurzer Lern-Vorlauf
(Werkzeug, Syntax-Umzug von C#, Wertsemantik und Pointer-Grundbild) mit
Mini-Snippets in `Sandbox/` dieser Schicht; danach trägt jeder
Meilenstein genau ein Lernthema. Ablauf je Baustein: Theorie-Happen mit
Zahlenbeispiel → Isor beschreibt den Entwurf in zwei Sätzen → Gerüst
mit TODOs → Isor tippt → Review → LERNLOG-Zeile.
Warum: Isors Vorgabe vom 2026-09-07, keine getrennten Übungsprojekte
vor dem echten Programm — vermeidet Doppelarbeit und spart Zeit für
Model-Viewer und Medienproduktion. Entwurf-vor-Gerüst kommt aus
`Kern/WORKFLOW.md`, das Kurs-Log-Format aus dem Python-Lesekurs.
Verworfen: eigenständiges Bootcamp mit Übungsprojekten (Claudes erster
Vorschlag); Crashkurs ohne Fundament direkt ins Projekt.

## 2026-09-07 — Schnittlinien statt Scope-Diskussion
Was: Wird die Zeit knapp, fällt in dieser Reihenfolge: Upgrade-System →
Slow-Turm → AOE wird Einzelschuss. Bei Zeitreserve kommt in dieser
Reihenfolge dazu: dritter Gegnertyp `♟` → zweites Pfad-Layout →
AOE-Slow → Speed-Taste während der Welle → raylib-Anzeige als Kür.
Warum: Jede Kürzungsstufe lässt ein vollständiges, abgabefähiges Spiel
übrig, und die Pflichtthemen stecken im unkürzbaren Kern (Gegner,
Türme, Projektile). Scope-Entscheidungen sind damit vorab getroffen
statt unter Termindruck — der Verlustpunkt des zweiten Semesters.
Verworfen: Scope erst verhandeln, wenn es klemmt.
**Abgelöst am 2026-09-07** durch „Schnittlinien Lane Defender" (unten).

## 2026-09-07 — Umschwenk auf den Lane-Shooter: Lane Defender
Was: Das Spiel wird ein Lane-Shooter nach Tapper-Vorbild statt eines
Tower-Defense; neuer Arbeitstitel **Lane Defender**. Der Spieler steht
unten, wechselt mit den Pfeiltasten zwischen bis zu vier Lanes und
schießt mit der Leertaste nach oben; Gegner spawnen oben je Lane und
laufen abwärts. Zwei Gegnertypen (Tank: viel Leben, langsam · Runner:
schnell, normales Leben), je Level stärker. Gold kauft auf einem
Upgrade-Screen zwischen den Leveln Schaden und Feuerrate. Alle drei
Level kommt eine Lane dazu (Start: eine, Maximum: vier); alle fünf
Level ein Boss — viel Leben, sehr langsam, belegt eine Lane, während
auf den übrigen normale Gegner weiterspawnen. Der erste Boss-Sieg
schaltet die Wahl genau einer von zwei Spezialattacken frei
(**Doppel-Lane**: trifft die aktuelle und die rechte Nachbar-Lane, auf
der äußersten rechten stattdessen die linke · **Durchschlag**: trifft
bis zu zwei Gegner hintereinander); weitere Boss-Siege verbessern die
gewählte. Sieg nach dem dritten Boss (Level 15), Niederlage bei
0 Leben; 20 Leben, −1 je Durchbrecher. Die bisher gezeigten Symbole
sind Pitch-Platzhalter — final gewählt wird beim Bau.
Warum: Die eindimensionale Geometrie streicht die fehleranfälligsten
Teile des TD-Designs ersatzlos — Zielsuche, Projektilverfolgung,
Baucursor, Bauplatz-Prüfung, kontextabhängiges Panel; ein Treffer ist
„gleiche Lane, gleiche Zeile" und damit garantiert, die in der
Tick-Demo sichtbaren Artefakte (Diagonalverfolgung, Überdeckung) können
strukturell nicht auftreten. Die Pflichtthemen bleiben vollständig und
werden teils klarer: Vererbung über Gegnertypen, Boss und
Skill-Klassen; Pointer als polymorpher Skill-Slot (`SpecialAttack*`,
beim Boss-Sieg belegt) und in den Gegner-Listen; Memory Management über
laufendes `new`/`delete` für Gegner und Schüsse. Geschätzt ~36 h statt
43 h. Idee und Zuschnitt: Isor, 2026-09-07, nach den Demo-Artefakten.
Verworfen: das Tower-Defense-Design vom Vormittag (abgelöste Einträge
oben); die Vermeidung von Live-Eingabe — der Preis des Umschwenks ist
eine nicht-blockierende Tastenabfrage (~15 Zeilen, gelieferter
Baustein wie der Farb-Init).

## 2026-09-07 — Schnittlinien Lane Defender
Was: Wird die Zeit knapp, fällt in dieser Reihenfolge: Skill-System
(Bosse bleiben als zähe Gegner) → Lane-Progression (fest vier Lanes ab
Start) → der dritte Boss (Sieg dann nach Level 10). Bei Zeitreserve
kommt in dieser Reihenfolge dazu: dritter Gegnertyp → Endlos-Modus mit
Highscore-Liste (die Namenseingabe existiert bereits) → dritte
Skill-Stufe → raylib-Anzeige als Kür.
Warum: Jede Kürzungsstufe lässt ein vollständiges, abgabefähiges Spiel
übrig; die Pflichtthemen stecken im unkürzbaren Kern aus Spieler,
Gegnern und Schüssen.
Verworfen: Kürzung an den zwei Gegnertypen (zerstörte das
Vererbungs-Pflichtthema).

## 2026-09-07 — Raster-Stabilität vor Schmuck
Was: Das Spielfeld darf sich nie verschieben. Erlaubt sind nur Zeichen,
die im Ziel-Terminal exakt eine Zelle breit sind — im Zweifel
schlichtes ASCII (`#`, `@`, `o`, `*`, `A`, `V`) plus Block- und
Rahmenzeichen; Schachfiguren und andere mehrdeutig breite Symbole
fliegen raus, wenn sie den Test nicht bestehen. Jeder Symbol-Kandidat
läuft beim Setup durch einen Zeichentest: eine Testzeile zwischen zwei
Rahmenlinien ausgeben — bleibt der rechte Rand bündig, ist das Zeichen
freigegeben. Die Doppelzellbreite aus dem Tick-Eintrag bleibt als
zweite Absicherung.
Warum: Isors Vorgabe vom 2026-09-07 — ein verformtes Spielfeld sieht
kaputt aus und kostet beim Feedbackelement „läuft stabil, Ein-/Ausgabe
verständlich" mehr, als jedes hübsche Symbol einbringt. Ob ein Zeichen
einzellig ist, entscheidet das echte Terminal, nicht die Vermutung.
Verworfen: Symbole nach Optik wählen und Verschiebungen später flicken.

## 2026-09-08 — Eigenes Code-Repo neben den anderen
Was: Das VS-Projekt lebt im eigenen Repo `C:\Repos Isor\Lane-Defender`
(angelegt 2026-09-08 mit .gitignore nach VS-C++-Muster und README;
VS-Projektname `LaneDefender`, ohne Bindestrich). Die Sandbox-Snippets
bleiben in dieser Harness-Schicht (`Sandbox/`); die Abgabe-src ist am
Ende eine aufgeräumte Kopie ins Portfolio im Datenbaum.
Warum: Git-Historie und der gewohnte GitHub-Desktop-Ablauf; die
Trennung von Arbeitsstand und Abgabe war der Gewinn des zweiten
Semesters (`Uni/DECISIONS.md` → „2026-08-12 — Neuer Abgabe-Satz statt
Umbau des alten").
Verworfen: direkt in der Abgabe-Struktur des Datenbaums arbeiten
(vermischt Arbeitsstand und Abgabe, keine Historie); ein Unterordner im
Unreal-Repo (das Konsolenprojekt ist ausdrücklich eigenständig).
