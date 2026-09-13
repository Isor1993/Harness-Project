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

## 2026-09-11 — int32_t statt int im ganzen Projekt
Was: Ganzzahlen im Lane Defender sind durchgängig `int32_t` (aus
`<cstdint>`, der Include steht ausdrücklich selbst in der Datei); das
SAE-Typkürzel bleibt `i`. Gilt auch für Konstanten und Schleifenzähler
— kein Mischbetrieb.
Warum: Isors Argument vom 2026-09-11 — `int` garantiert seine Breite
nicht (implementierungsabhängig; auf MSVC/Windows x64 fest 32 Bit),
`int32_t` macht die Breiten-Entscheidung im Code sichtbar und ist im
Prüfungsgespräch verteidigbar; zugleich die Brücke zu Unreals `int32`.
Die SAE-Konvention regelt Namen, nicht Typwahl; die Dozentin verlangt
nur Konsistenz innerhalb des Projekts.
Verworfen: `int` nach dem Vorbild der SAE-Beispiele (Claudes erste
Empfehlung — auf der Zielplattform gleichwertig, macht die Breite aber
nicht sichtbar); Mischbetrieb je Stelle (verletzt die
Konsistenz-Vorgabe).

## 2026-09-11 — bool-Ausgaben laufen nicht über PrintMessage
Was: Die Ausgabe-Hilfsfunktion `PrintMessage` (Überladungen für string,
int32_t und float, jeweils mit `a_bNextLine = true` als Default) druckt
keine bool-Werte; die eine Statuszeile schreibt ihren bool direkt über
`std::cout` mit lokalem `boolalpha`.
Warum: Das Endargument `a_bNextLine` macht eine bool-Wert-Überladung
mehrdeutig — `PrintMessage("x", false)` wäre zugleich
„Label ohne Umbruch" und „Wert false mit Default" —, und ohne eigene
bool-Überladung wandelt die Überladungswahl den Wert still zu int
(Ausgabe `1` statt `true`, belegt am 2026-09-11). Eine benannte Grenze
ist billiger als eine verbogene API.
Verworfen: vierte Wert-Überladung `(string, bool, bool)` (mehrdeutig
gegen `(string, bool)`); `boolalpha` global setzen (wirkungslos, weil
der Wert als int ankam).

## 2026-09-12 — Leere Eingabe bleibt stilles Warten
Was: Drückt der Spieler bei der Leben-Abfrage nur Enter, wartet das
Programm still auf weitere Eingabe — `ReadValueInput` behandelt den
Fall nicht gesondert. Grund im Verhalten von `cin >>`: Führender
Whitespace (auch `\n`) wird übersprungen, der Aufruf kehrt erst mit
echten Zeichen zurück — es entsteht weder ein Fehlerzustand noch eine
Endlosschleife.
Warum: Standardverhalten formatierter Konsoleneingabe, kein Absturz;
die Ü4-Testreihe verlangt den Fall nicht, und eine Meldung
rechtfertigt in der Lern-Übung keinen Umbau (Isor, 2026-09-12, nach
Ansicht der drei Wege).
Verworfen: `peek`-Wächter vor dem Lesen (vier Zeilen Sonderweg, fängt
nur den Nur-Enter-Fall); Umbau auf zeilenweises Lesen mit `getline`
plus Parsen (wasserdicht, aber zwei neue Bausteine — als Härtung bei
M1/M7 wieder auf dem Tisch, siehe ROADMAP-Aufgabe „getline-Härtung
bei M1/M7 prüfen").

## 2026-09-12 — String-Parameter laufen als const-Referenz
Was: Die string-Parameter der PrintMessage-Familie tragen durchgängig
`const std::string&` (drei Überladungen, je Prototyp und Definition);
Zahl- und bool-Parameter bleiben by value. Gilt als Konvention für
künftige Funktionen des Projekts.
Warum: Kostenregel aus L3 Ü3 — kleine Werte kopieren (eine
4-Byte-Kopie schlägt den 8-Byte-Adressumweg), große Objekte per
const-Referenz ausleihen; bei Strings entfällt damit die Zeichen-Kopie
je Aufruf (~27 String-Aufrufe je Kurzspiel, gezählt am Bestand vom
2026-09-12). Zugleich die Konvention, die Prüfer erwarten.
Verworfen: string by value (kopiert bei jedem Aufruf alle Zeichen);
nicht-konstante Referenz `std::string&` (bindet nicht an
Literal-Aufrufe und erlaubt versehentliches Schreiben — der
const-lose Zwischenstand scheiterte genau daran).

## 2026-09-12 — Fachbereichs-Austausch zur Projektidee entfällt
Was: Der im Aufgabentext verlangte Austausch mit dem Fachbereichs-Team
vor Festlegung der Projektidee wird nicht geführt; das Projekt startet
auf Basis der bestätigten Vorjahres-Texte
(`Uni/Semester_3/VORJAHR_AUFGABEN.md`).
Warum: Isors Entscheidung vom 2026-09-12 — aus seiner Sicht eine
Formalität; die Erfahrung aus dem ersten Semester zeigt ihm, dass das
Vorgehen reicht.
Verworfen: den Austausch vor Baustart nachholen (Claudes Hinweis; beim
nächsten Unterrichtsblock weiter möglich — das M1-Gerüst trägt jede
Konsolenspiel-Idee und ist davon unabhängig).

## 2026-09-12 — M1-Ablauf: Szenen-Zustandsautomat mit sechs Stationen
Was: Das Gerüst ist ein Zustandsautomat — ein enum-Zustand plus
Schleife in `main`: Hauptmenü → Namenseingabe → Steuerungs-Szene →
Spiel → Endszene; beliebige Taste in der Endszene führt zurück ins
Hauptmenü, beendet wird nur über Exit im Hauptmenü. Die Endszene zeigt
Sieg oder Game Over samt Name und erreichtem Level. Die
Steuerungs-Szene (Tastenbelegung plus ein Satz Spielziel) erscheint vor
jedem Spielstart; beliebige Taste startet das Spiel und wirkt so als
Bereit-Schranke. Szenen sind in M1 Funktionen, keine Klassen.
Warum: Isors Szenen-Modell vom 2026-09-12 (Analogie zu Unity-Szenen);
die Steuerungs-Szene hat er beim Gegenlesen selbst nachgezogen.
Funktionen statt Szenen-Klassen: Eine Klassenhierarchie hätte in M1
nichts zu verwalten — sauberes OOP fürs First-Ziel heißt Klassen dort,
wo Zustand und Verhalten zusammengehören (Player M2, Gegner M3, Skills
M5), nicht Klasse als Selbstzweck; die Begründung ist im
Prüfungsgespräch tragfähig.
Verworfen: Szenen-Klassenhierarchie ab M1 (Umbau bleibt möglich, wenn
Szenen echten Zustand tragen); Programmende direkt nach der Endszene;
Mini-Menü in der Endszene (ein Menü mehr ohne Mehrwert — Exit gibt es
im Hauptmenü); Steuerungs-Anzeige nur beim ersten Spielstart.

## 2026-09-12 — Menü-Bedienung und Titel-Optik
Was: Menüpunkte als umrahmte Buttons (Rahmenzeichen mit
ASCII-Rückfall `+ - |`), Auswahl per ↑/↓ und W/S, Marker `>` plus
gelbe Hervorhebung der gewählten Zeile, nur Enter bestätigt. Titel in
Linien-Schrift (gezeichnete ASCII-Buchstaben), farbig; Einblendung nur
beim Programmstart, per Taste überspringbar — danach steht das Menü
sofort. Die Pfeiltasten-Bedienung zieht die Einzeltasten-Abfrage
(gelieferter Baustein, geplant für M2) nach M1 vor.
Warum: Isors Entwurf vom 2026-09-12 (Buttons, Pfeile/W+S, Marker,
großer Titel mit Einblendung). Enter allein hält die Leertaste
eindeutig beim Schießen; Gelb statt Rot: bei Isors Rot-Grün-Schwäche
hundertprozentig sicher und auf schwarzem Grund kontrastreicher, dazu
trägt die Meldung immer auch als Text. Linien-Schrift fest: pures
ASCII, kein Test-Vorbehalt.
Verworfen: Ziffern-Menü (1/2 eintippen); Leertaste als zweite
Bestätigung; rohe `#`-Blockklötze (Isor: „das Rohe sieht hässlich
aus"); Block-Schrift aus `█ ▀ ▄`, auch als Variante mit Rückfall
(Isor wählte fest die Linien-Schrift); Einblendung bei jedem
Menü-Besuch; Rot als Hervorhebung.

## 2026-09-12 — Namensregeln der Namenseingabe
Was: Der Name wird per `getline` gelesen. Leere Eingabe (nur Enter) →
Standardname „Player". Höchstens 16 Zeichen; erlaubt nur `A–Z`,
`a–z`, `0–9` — keine Leerzeichen, keine Umlaute. Ungültige Eingabe:
Piepton (`\a`), gelbe Meldung, die die Regel nennt, erneut fragen;
geprüft wird nach Enter, nicht je Taste. Bestätigt wird auf der
Szene über die Auswahl Start/Zurück wie im Hauptmenü.
Warum: Isors Vorschlag vom 2026-09-12 (Default „Player", 16 Zeichen,
Buchstaben und Ziffern, Ton plus Kennzeichnung). 16 Zeichen halten
die spätere HUD-Zeile unter ~55 Zeichen; Leerzeichen und Umlaute sind
Parse- bzw. Zeichensatz-Risiko im Sinne der Raster-Regel; `getline`
fängt leere wie Leerzeichen-Eingaben — der getline-Merkposten der
ROADMAP ist damit für M1 entschieden.
Verworfen: Rot als Fehlerfarbe (Isors erster Gedanke — Gelb plus
Text trägt doppelt, siehe Menü-Eintrag); Live-Filterung je Taste
(eigene Eingabeschleife ohne Mehrwert); stilles Abschneiden zu langer
Namen (Überraschung statt Meldung); Namenszwang bei leerer Eingabe.

## 2026-09-12 — Konsolen-Technik: VT-Escape-Sequenzen
Was: Farben, Cursor-Home und Cursor-Verstecken laufen über
VT-Escape-Sequenzen; einmal beim Start aktiviert
(`ENABLE_VIRTUAL_TERMINAL_PROCESSING`), dazu
`SetConsoleOutputCP(CP_UTF8)` für die Rahmenzeichen. Alle Codes
stecken hinter SAE-Konstanten; das Ganze kommt als gelieferter
Baustein `Console.h`/`Console.cpp`.
Warum: Die Codes sind Teil des Ausgabetexts — der ganze Frame bleibt
ein String und ein `cout` je Tick, exakt das beschlossene
Ein-Puffer-Rendering; moderner Standard.
Verworfen: klassische WinAPI-Aufrufe je Farbwechsel
(`SetConsoleTextAttribute` — zerschneidet den Ein-Puffer-Ansatz, bei
geschätzt 30 farbigen Stellen 60+ Aufrufe je Tick statt einem).

## 2026-09-12 — Zeichentest als Szene hinter versteckter Taste T
Was: Der Zeichentest (jeder Kandidat zehnfach zwischen Randlinien,
Urteil per Blick auf den rechten Rand) ist eine eigene Szene,
erreichbar über die im Menü nicht angezeigte Taste `T` im Hauptmenü.
Ob er zur Abgabe drinbleibt, wird bei M7 entschieden.
Warum: Ob ein Zeichen einzellig ist, entscheidet das echte Terminal —
und davon sind mehrere im Spiel (VS-Debug-Konsole, Windows Terminal,
Prüfer-Terminal); so bleibt der Test jederzeit wiederholbar.
Verworfen: sichtbarer Menüpunkt (Werkzeug, kein Spielinhalt);
Wegwerf-Test nur während der M1-Entwicklung (verliert die
Wiederholbarkeit auf fremden Terminals).

## 2026-09-12 — M1-Struktur und Verbleib des Übungscodes
Was: `LaneDefender.cpp` trägt `main`, den Zustandsautomaten und die
Szenen-Funktionen; `Console.h`/`Console.cpp` den gelieferten
Konsolen-Baustein. `PrintMessage` bleibt als Ausgabe-Helfer.
`ReadValueInput` wird entfernt — kein Aufrufer mehr: das Menü läuft
über Einzeltasten, die Leben sind fest 20, der Name kommt über eine
eigene getline-Funktion. Die Übungs-Spielschleife in `main` weicht dem
Automaten; der komplette Übungsstand liegt als Kopie in
`Sandbox/L2_L3_Uebungsstand.cpp` dieser Schicht und in der
Git-Historie des Code-Repos.
Warum: kein toter Code Richtung Abgabe (Feedbackelement „lesbarer,
aufgeräumter Code"); mehr Dateien wachsen erst mit den Klassen ab M2.
Entfernen von `ReadValueInput`: Isor, 2026-09-12.
Verworfen: `ReadValueInput` bis M7 drinlassen (totes, wenn auch
getestetes Werkzeug — kommt bei Bedarf aus der Sicherung zurück, etwa
für den Upgrade-Screen in M4); Aufteilung in Szenen-Dateien schon
in M1.

## 2026-09-12 — Zeitschätzung vor Baustart auf 50 Stunden angehoben
Was: Die Meilenstein-Schätzung steigt von 36 h auf 50 h: M1 6 · M2 7 ·
M3 10 · M4 8 · M5 8 · M6 6 · M7 5. Steht im ZEITPLAN dieser Schicht;
die Ist-Spalte wird ab dem M1-Development-Abschnitt gemessen.
Warum: Isors Ansatz vom 2026-09-12. Der Lern-Vorlauf L1–L3 brauchte
real grob 6–8 h und zeigt den echten Lerntakt, und jeder Meilenstein
trägt ein neues Lernthema; „realistische Zeitabläufe mit Pufferzeiten"
ist zudem benanntes Feedbackelement der Aufgabe. Budget-Rahmen
geprüft: Bis zum Zielfenster ~05.10. stehen rund 75–80 h Wochenbudget,
50 h sind etwa zwei Drittel davon — gedeckt durch die
Semesterstrategie „Lane Defender früh fertig als Zeitquelle". M1
wächst auf 6 h, weil das Design vom 2026-09-12 Steuerungs-Szene,
Button-Rahmen, Titel-Einblendung und Zeichentest-Szene ergänzt hat.
Verworfen: bei 36 h bleiben (eine knappe Schätzung, die überall
reißt, wirkt schlechter als eine ehrliche, die hält).

## 2026-09-12 — Ausgeschriebene Schritte statt Mehrschritt-Zeilen
Was: Aufruf, Vergleich und return bzw. if werden nicht in einer Zeile
verkettet; Zwischenschritte bekommen benannte Variablen
(`bModeWasSet`, `bCodepageWasSet` …). `Console.cpp` ist entsprechend
umgebaut; die Regel gilt als Stil für kommenden Projekt-Code.
Warum: Isors Lesbarkeits-Entscheid vom 2026-09-12 — beide
Verständnis-Hänger des Tages (das `|` im if als Vergleich gelesen,
`return X != FALSE` als bedingtes return) entstanden an kompakten
Zeilen; SAE-Regel 9 („eine Anweisung pro Zeile") stützt die Langform.
Verworfen: kompakte Ketten (idiomatisch und kürzer, hier aber zweimal
die belegte Stolperquelle).

## 2026-09-12 — Zeichentest bleibt statisch, der Lauf-Test wird M2-Einstieg
Was: Die Zeichentest-Szene prüft nur statisch die Breite — jeder
Kandidat zehnfach zwischen ASCII-Rändern unter einer Lineal-Zeile.
Isors eigener Entwurf eines dynamischen Lauf-Tests (ein Symbol läuft
je Tick eine Mini-Lane mit Wänden hinab und prüft die Stabilität beim
Neuzeichnen) wird nicht in M1 gebaut, sondern ist der natürliche erste
Baustein von M2 („Spielfeld mit Lanes zeichnen").
Warum: Zeitentscheid von Isor am 2026-09-12 bei ~3,5 h M1-Stand; der
Lauf-Test prüft genau das, was M2 ohnehin als Erstes baut — es geht
nichts verloren.
Verworfen: beide Tests in M1 (Claudes Empfehlung — vom Zeitbudget
geschlagen); die Ränder des statischen Tests aus den hübschen
Rahmenzeichen zu bauen (die Prüflinge dürfen nicht das Lineal sein,
Ränder bleiben ASCII `|`).
